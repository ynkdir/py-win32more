from win32more import *
import win32more.NetworkManagement.Rras
import win32more.Foundation
import win32more.NetworkManagement.IpHelper
import win32more.Networking.WinSock
import win32more.Security.Cryptography

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.NetworkManagement.Rras, name, eval(f"_define_{name}()"))
    return getattr(win32more.NetworkManagement.Rras, name)
RASNAP_ProbationTime = 1
RASTUNNELENDPOINT_UNKNOWN = 0
RASTUNNELENDPOINT_IPv4 = 1
RASTUNNELENDPOINT_IPv6 = 2
RAS_MaxDeviceType = 16
RAS_MaxPhoneNumber = 128
RAS_MaxIpAddress = 15
RAS_MaxIpxAddress = 21
RAS_MaxEntryName = 256
RAS_MaxDeviceName = 128
RAS_MaxCallbackNumber = 128
RAS_MaxAreaCode = 10
RAS_MaxPadType = 32
RAS_MaxX25Address = 200
RAS_MaxFacilities = 200
RAS_MaxUserData = 200
RAS_MaxReplyMessage = 1024
RAS_MaxDnsSuffix = 256
RASCF_AllUsers = 1
RASCF_GlobalCreds = 2
RASCF_OwnerKnown = 4
RASCF_OwnerMatch = 8
RAS_MaxIDSize = 256
RASCS_PAUSED = 4096
RASCS_DONE = 8192
RASCSS_DONE = 8192
RDEOPT_UsePrefixSuffix = 1
RDEOPT_PausedStates = 2
RDEOPT_IgnoreModemSpeaker = 4
RDEOPT_SetModemSpeaker = 8
RDEOPT_IgnoreSoftwareCompression = 16
RDEOPT_SetSoftwareCompression = 32
RDEOPT_DisableConnectedUI = 64
RDEOPT_DisableReconnectUI = 128
RDEOPT_DisableReconnect = 256
RDEOPT_NoUser = 512
RDEOPT_PauseOnScript = 1024
RDEOPT_Router = 2048
RDEOPT_CustomDial = 4096
RDEOPT_UseCustomScripting = 8192
RDEOPT_InvokeAutoTriggerCredentialUI = 16384
RDEOPT_EapInfoCryptInCapable = 32768
REN_User = 0
REN_AllUsers = 1
RASIPO_VJ = 1
RASLCPO_PFC = 1
RASLCPO_ACFC = 2
RASLCPO_SSHF = 4
RASLCPO_DES_56 = 8
RASLCPO_3_DES = 16
RASLCPO_AES_128 = 32
RASLCPO_AES_256 = 64
RASLCPO_AES_192 = 128
RASLCPO_GCM_AES_128 = 256
RASLCPO_GCM_AES_192 = 512
RASLCPO_GCM_AES_256 = 1024
RASCCPCA_MPPC = 6
RASCCPCA_STAC = 5
RASCCPO_Compression = 1
RASCCPO_HistoryLess = 2
RASCCPO_Encryption56bit = 16
RASCCPO_Encryption40bit = 32
RASCCPO_Encryption128bit = 64
RASIKEv2_AUTH_MACHINECERTIFICATES = 1
RASIKEv2_AUTH_EAP = 2
RASIKEv2_AUTH_PSK = 3
WM_RASDIALEVENT = 52429
ET_None = 0
ET_Require = 1
ET_RequireMax = 2
ET_Optional = 3
VS_Default = 0
VS_PptpOnly = 1
VS_PptpFirst = 2
VS_L2tpOnly = 3
VS_L2tpFirst = 4
VS_SstpOnly = 5
VS_SstpFirst = 6
VS_Ikev2Only = 7
VS_Ikev2First = 8
VS_GREOnly = 9
VS_PptpSstp = 12
VS_L2tpSstp = 13
VS_Ikev2Sstp = 14
VS_ProtocolList = 15
RASEO_UseCountryAndAreaCodes = 1
RASEO_SpecificIpAddr = 2
RASEO_SpecificNameServers = 4
RASEO_IpHeaderCompression = 8
RASEO_RemoteDefaultGateway = 16
RASEO_DisableLcpExtensions = 32
RASEO_TerminalBeforeDial = 64
RASEO_TerminalAfterDial = 128
RASEO_ModemLights = 256
RASEO_SwCompression = 512
RASEO_RequireEncryptedPw = 1024
RASEO_RequireMsEncryptedPw = 2048
RASEO_RequireDataEncryption = 4096
RASEO_NetworkLogon = 8192
RASEO_UseLogonCredentials = 16384
RASEO_PromoteAlternates = 32768
RASEO_SecureLocalFiles = 65536
RASEO_RequireEAP = 131072
RASEO_RequirePAP = 262144
RASEO_RequireSPAP = 524288
RASEO_Custom = 1048576
RASEO_PreviewPhoneNumber = 2097152
RASEO_SharedPhoneNumbers = 8388608
RASEO_PreviewUserPw = 16777216
RASEO_PreviewDomain = 33554432
RASEO_ShowDialingProgress = 67108864
RASEO_RequireCHAP = 134217728
RASEO_RequireMsCHAP = 268435456
RASEO_RequireMsCHAP2 = 536870912
RASEO_RequireW95MSCHAP = 1073741824
RASEO_CustomScript = 2147483648
RASEO2_SecureFileAndPrint = 1
RASEO2_SecureClientForMSNet = 2
RASEO2_DontNegotiateMultilink = 4
RASEO2_DontUseRasCredentials = 8
RASEO2_UsePreSharedKey = 16
RASEO2_Internet = 32
RASEO2_DisableNbtOverIP = 64
RASEO2_UseGlobalDeviceSettings = 128
RASEO2_ReconnectIfDropped = 256
RASEO2_SharePhoneNumbers = 512
RASEO2_SecureRoutingCompartment = 1024
RASEO2_UseTypicalSettings = 2048
RASEO2_IPv6SpecificNameServers = 4096
RASEO2_IPv6RemoteDefaultGateway = 8192
RASEO2_RegisterIpWithDNS = 16384
RASEO2_UseDNSSuffixForRegistration = 32768
RASEO2_IPv4ExplicitMetric = 65536
RASEO2_IPv6ExplicitMetric = 131072
RASEO2_DisableIKENameEkuCheck = 262144
RASEO2_DisableClassBasedStaticRoute = 524288
RASEO2_SpecificIPv6Addr = 1048576
RASEO2_DisableMobility = 2097152
RASEO2_RequireMachineCertificates = 4194304
RASEO2_UsePreSharedKeyForIkev2Initiator = 8388608
RASEO2_UsePreSharedKeyForIkev2Responder = 16777216
RASEO2_CacheCredentials = 33554432
RASEO2_AutoTriggerCapable = 67108864
RASEO2_IsThirdPartyProfile = 134217728
RASEO2_AuthTypeIsOtp = 268435456
RASEO2_IsAlwaysOn = 536870912
RASEO2_IsPrivateNetwork = 1073741824
RASEO2_PlumbIKEv2TSAsRoutes = 2147483648
RASNP_NetBEUI = 1
RASNP_Ipx = 2
RASNP_Ip = 4
RASNP_Ipv6 = 8
RASFP_Ppp = 1
RASFP_Slip = 2
RASFP_Ras = 4
RASET_Phone = 1
RASET_Vpn = 2
RASET_Direct = 3
RASET_Internet = 4
RASET_Broadband = 5
RASCN_Connection = 1
RASCN_Disconnection = 2
RASCN_BandwidthAdded = 4
RASCN_BandwidthRemoved = 8
RASCN_Dormant = 16
RASCN_ReConnection = 32
RASCN_EPDGPacketArrival = 64
RASIDS_Disabled = 4294967295
RASIDS_UseGlobalValue = 0
RASADFLG_PositionDlg = 1
RASCM_UserName = 1
RASCM_Password = 2
RASCM_Domain = 4
RASCM_DefaultCreds = 8
RASCM_PreSharedKey = 16
RASCM_ServerPreSharedKey = 32
RASCM_DDMPreSharedKey = 64
RASADP_DisableConnectionQuery = 0
RASADP_LoginSessionDisable = 1
RASADP_SavedAddressesLimit = 2
RASADP_FailedConnectionTimeout = 3
RASADP_ConnectionQueryTimeout = 4
RASEAPF_NonInteractive = 2
RASEAPF_Logon = 4
RASEAPF_Preview = 8
RCD_SingleUser = 0
RCD_AllUsers = 1
RCD_Eap = 2
RCD_Logon = 4
RASPBDEVENT_AddEntry = 1
RASPBDEVENT_EditEntry = 2
RASPBDEVENT_RemoveEntry = 3
RASPBDEVENT_DialEntry = 4
RASPBDEVENT_EditGlobals = 5
RASPBDEVENT_NoUser = 6
RASPBDEVENT_NoUserEdit = 7
RASNOUSER_SmartCard = 1
RASPBDFLAG_PositionDlg = 1
RASPBDFLAG_ForceCloseOnDial = 2
RASPBDFLAG_NoUser = 16
RASPBDFLAG_UpdateDefaults = 2147483648
RASEDFLAG_PositionDlg = 1
RASEDFLAG_NewEntry = 2
RASEDFLAG_CloneEntry = 4
RASEDFLAG_NoRename = 8
RASEDFLAG_ShellOwned = 1073741824
RASEDFLAG_NewPhoneEntry = 16
RASEDFLAG_NewTunnelEntry = 32
RASEDFLAG_NewDirectEntry = 64
RASEDFLAG_NewBroadbandEntry = 128
RASEDFLAG_InternetEntry = 256
RASEDFLAG_NAT = 512
RASEDFLAG_IncomingConnection = 1024
RASDDFLAG_PositionDlg = 1
RASDDFLAG_NoPrompt = 2
RASDDFLAG_AoacRedial = 4
RASDDFLAG_LinkFailure = 2147483648
PID_IPX = 43
PID_IP = 33
PID_IPV6 = 87
PID_NBF = 63
PID_ATALK = 41
MPR_INTERFACE_OUT_OF_RESOURCES = 1
MPR_INTERFACE_ADMIN_DISABLED = 2
MPR_INTERFACE_CONNECTION_FAILURE = 4
MPR_INTERFACE_SERVICE_PAUSED = 8
MPR_INTERFACE_DIALOUT_HOURS_RESTRICTION = 16
MPR_INTERFACE_NO_MEDIA_SENSE = 32
MPR_INTERFACE_NO_DEVICE = 64
MPR_MaxDeviceType = 16
MPR_MaxPhoneNumber = 128
MPR_MaxIpAddress = 15
MPR_MaxIpxAddress = 21
MPR_MaxEntryName = 256
MPR_MaxDeviceName = 128
MPR_MaxCallbackNumber = 128
MPR_MaxAreaCode = 10
MPR_MaxPadType = 32
MPR_MaxX25Address = 200
MPR_MaxFacilities = 200
MPR_MaxUserData = 200
MPRIO_SpecificIpAddr = 2
MPRIO_SpecificNameServers = 4
MPRIO_IpHeaderCompression = 8
MPRIO_RemoteDefaultGateway = 16
MPRIO_DisableLcpExtensions = 32
MPRIO_SwCompression = 512
MPRIO_RequireEncryptedPw = 1024
MPRIO_RequireMsEncryptedPw = 2048
MPRIO_RequireDataEncryption = 4096
MPRIO_NetworkLogon = 8192
MPRIO_PromoteAlternates = 32768
MPRIO_SecureLocalFiles = 65536
MPRIO_RequireEAP = 131072
MPRIO_RequirePAP = 262144
MPRIO_RequireSPAP = 524288
MPRIO_SharedPhoneNumbers = 8388608
MPRIO_RequireCHAP = 134217728
MPRIO_RequireMsCHAP = 268435456
MPRIO_RequireMsCHAP2 = 536870912
MPRIO_IpSecPreSharedKey = 2147483648
MPRIO_RequireMachineCertificates = 16777216
MPRIO_UsePreSharedKeyForIkev2Initiator = 33554432
MPRIO_UsePreSharedKeyForIkev2Responder = 67108864
MPRNP_Ipx = 2
MPRNP_Ip = 4
MPRNP_Ipv6 = 8
MPRET_Phone = 1
MPRET_Vpn = 2
MPRET_Direct = 3
MPRIDS_Disabled = 4294967295
MPRIDS_UseGlobalValue = 0
MPR_VS_Ikev2Only = 7
MPR_VS_Ikev2First = 8
MPR_ENABLE_RAS_ON_DEVICE = 1
MPR_ENABLE_ROUTING_ON_DEVICE = 2
IPADDRESSLEN = 15
IPXADDRESSLEN = 22
ATADDRESSLEN = 32
MAXIPADRESSLEN = 64
PPP_IPCP_VJ = 1
PPP_CCP_COMPRESSION = 1
PPP_CCP_ENCRYPTION40BITOLD = 16
PPP_CCP_ENCRYPTION40BIT = 32
PPP_CCP_ENCRYPTION128BIT = 64
PPP_CCP_ENCRYPTION56BIT = 128
PPP_CCP_HISTORYLESS = 16777216
PPP_LCP_MULTILINK_FRAMING = 1
PPP_LCP_PFC = 2
PPP_LCP_ACFC = 4
PPP_LCP_SSHF = 8
PPP_LCP_DES_56 = 16
PPP_LCP_3_DES = 32
PPP_LCP_AES_128 = 64
PPP_LCP_AES_256 = 128
PPP_LCP_AES_192 = 256
PPP_LCP_GCM_AES_128 = 512
PPP_LCP_GCM_AES_192 = 1024
PPP_LCP_GCM_AES_256 = 2048
RAS_FLAGS_RAS_CONNECTION = 4
RASPRIV_NoCallback = 1
RASPRIV_AdminSetCallback = 2
RASPRIV_CallerSetCallback = 4
RASPRIV_DialinPrivilege = 8
RASPRIV2_DialinPolicy = 1
MPRAPI_IKEV2_AUTH_USING_CERT = 1
MPRAPI_IKEV2_AUTH_USING_EAP = 2
MPRAPI_PPP_PROJECTION_INFO_TYPE = 1
MPRAPI_IKEV2_PROJECTION_INFO_TYPE = 2
MPRAPI_RAS_CONNECTION_OBJECT_REVISION_1 = 1
MPRAPI_MPR_IF_CUSTOM_CONFIG_OBJECT_REVISION_1 = 1
MPRAPI_IF_CUSTOM_CONFIG_FOR_IKEV2 = 1
MPRAPI_MPR_IF_CUSTOM_CONFIG_OBJECT_REVISION_3 = 3
MPRAPI_MPR_IF_CUSTOM_CONFIG_OBJECT_REVISION_2 = 2
MPRAPI_IKEV2_SET_TUNNEL_CONFIG_PARAMS = 1
MPRAPI_L2TP_SET_TUNNEL_CONFIG_PARAMS = 1
MAX_SSTP_HASH_SIZE = 32
MPRAPI_MPR_SERVER_OBJECT_REVISION_1 = 1
MPRAPI_MPR_SERVER_OBJECT_REVISION_2 = 2
MPRAPI_MPR_SERVER_OBJECT_REVISION_3 = 3
MPRAPI_MPR_SERVER_OBJECT_REVISION_4 = 4
MPRAPI_MPR_SERVER_OBJECT_REVISION_5 = 5
MPRAPI_MPR_SERVER_SET_CONFIG_OBJECT_REVISION_1 = 1
MPRAPI_MPR_SERVER_SET_CONFIG_OBJECT_REVISION_2 = 2
MPRAPI_MPR_SERVER_SET_CONFIG_OBJECT_REVISION_3 = 3
MPRAPI_MPR_SERVER_SET_CONFIG_OBJECT_REVISION_4 = 4
MPRAPI_MPR_SERVER_SET_CONFIG_OBJECT_REVISION_5 = 5
MPRAPI_SET_CONFIG_PROTOCOL_FOR_PPTP = 1
MPRAPI_SET_CONFIG_PROTOCOL_FOR_L2TP = 2
MPRAPI_SET_CONFIG_PROTOCOL_FOR_SSTP = 4
MPRAPI_SET_CONFIG_PROTOCOL_FOR_IKEV2 = 8
MPRAPI_SET_CONFIG_PROTOCOL_FOR_GRE = 16
ALLOW_NO_AUTH = 1
DO_NOT_ALLOW_NO_AUTH = 0
MPRAPI_RAS_UPDATE_CONNECTION_OBJECT_REVISION_1 = 1
MPRAPI_ADMIN_DLL_VERSION_1 = 1
MPRAPI_ADMIN_DLL_VERSION_2 = 2
MGM_JOIN_STATE_FLAG = 1
MGM_FORWARD_STATE_FLAG = 2
MGM_MFE_STATS_0 = 1
MGM_MFE_STATS_1 = 2
RTM_MAX_ADDRESS_SIZE = 16
RTM_MAX_VIEWS = 32
RTM_VIEW_ID_UCAST = 0
RTM_VIEW_ID_MCAST = 1
RTM_VIEW_MASK_SIZE = 32
RTM_VIEW_MASK_NONE = 0
RTM_VIEW_MASK_ANY = 0
RTM_VIEW_MASK_UCAST = 1
RTM_VIEW_MASK_MCAST = 2
RTM_VIEW_MASK_ALL = 4294967295
IPV6_ADDRESS_LEN_IN_BYTES = 16
RTM_DEST_FLAG_NATURAL_NET = 1
RTM_DEST_FLAG_FWD_ENGIN_ADD = 2
RTM_DEST_FLAG_DONT_FORWARD = 4
RTM_ROUTE_STATE_CREATED = 0
RTM_ROUTE_STATE_DELETING = 1
RTM_ROUTE_STATE_DELETED = 2
RTM_ROUTE_FLAGS_MARTIAN = 1
RTM_ROUTE_FLAGS_BLACKHOLE = 2
RTM_ROUTE_FLAGS_DISCARD = 4
RTM_ROUTE_FLAGS_INACTIVE = 8
RTM_ROUTE_FLAGS_LOCAL = 16
RTM_ROUTE_FLAGS_REMOTE = 32
RTM_ROUTE_FLAGS_MYSELF = 64
RTM_ROUTE_FLAGS_LOOPBACK = 128
RTM_ROUTE_FLAGS_MCAST = 256
RTM_ROUTE_FLAGS_LOCAL_MCAST = 512
RTM_ROUTE_FLAGS_LIMITED_BC = 1024
RTM_ROUTE_FLAGS_ZEROS_NETBC = 4096
RTM_ROUTE_FLAGS_ZEROS_SUBNETBC = 8192
RTM_ROUTE_FLAGS_ONES_NETBC = 16384
RTM_ROUTE_FLAGS_ONES_SUBNETBC = 32768
RTM_NEXTHOP_STATE_CREATED = 0
RTM_NEXTHOP_STATE_DELETED = 1
RTM_NEXTHOP_FLAGS_REMOTE = 1
RTM_NEXTHOP_FLAGS_DOWN = 2
METHOD_TYPE_ALL_METHODS = 4294967295
METHOD_RIP2_NEIGHBOUR_ADDR = 1
METHOD_RIP2_OUTBOUND_INTF = 2
METHOD_RIP2_ROUTE_TAG = 4
METHOD_RIP2_ROUTE_TIMESTAMP = 8
METHOD_BGP4_AS_PATH = 1
METHOD_BGP4_PEER_ID = 2
METHOD_BGP4_PA_ORIGIN = 4
METHOD_BGP4_NEXTHOP_ATTR = 8
RTM_RESUME_METHODS = 0
RTM_BLOCK_METHODS = 1
RTM_ROUTE_CHANGE_FIRST = 1
RTM_ROUTE_CHANGE_NEW = 2
RTM_ROUTE_CHANGE_BEST = 65536
RTM_NEXTHOP_CHANGE_NEW = 1
RTM_MATCH_NONE = 0
RTM_MATCH_OWNER = 1
RTM_MATCH_NEIGHBOUR = 2
RTM_MATCH_PREF = 4
RTM_MATCH_NEXTHOP = 8
RTM_MATCH_INTERFACE = 16
RTM_MATCH_FULL = 65535
RTM_ENUM_START = 0
RTM_ENUM_NEXT = 1
RTM_ENUM_RANGE = 2
RTM_ENUM_ALL_DESTS = 0
RTM_ENUM_OWN_DESTS = 16777216
RTM_ENUM_ALL_ROUTES = 0
RTM_ENUM_OWN_ROUTES = 65536
RTM_NUM_CHANGE_TYPES = 3
RTM_CHANGE_TYPE_ALL = 1
RTM_CHANGE_TYPE_BEST = 2
RTM_CHANGE_TYPE_FORWARDING = 4
RTM_NOTIFY_ONLY_MARKED_DESTS = 65536
RASBASE = 600
PENDING = 600
ERROR_INVALID_PORT_HANDLE = 601
ERROR_PORT_ALREADY_OPEN = 602
ERROR_BUFFER_TOO_SMALL = 603
ERROR_WRONG_INFO_SPECIFIED = 604
ERROR_CANNOT_SET_PORT_INFO = 605
ERROR_PORT_NOT_CONNECTED = 606
ERROR_EVENT_INVALID = 607
ERROR_DEVICE_DOES_NOT_EXIST = 608
ERROR_DEVICETYPE_DOES_NOT_EXIST = 609
ERROR_BUFFER_INVALID = 610
ERROR_ROUTE_NOT_AVAILABLE = 611
ERROR_ROUTE_NOT_ALLOCATED = 612
ERROR_INVALID_COMPRESSION_SPECIFIED = 613
ERROR_OUT_OF_BUFFERS = 614
ERROR_PORT_NOT_FOUND = 615
ERROR_ASYNC_REQUEST_PENDING = 616
ERROR_ALREADY_DISCONNECTING = 617
ERROR_PORT_NOT_OPEN = 618
ERROR_PORT_DISCONNECTED = 619
ERROR_NO_ENDPOINTS = 620
ERROR_CANNOT_OPEN_PHONEBOOK = 621
ERROR_CANNOT_LOAD_PHONEBOOK = 622
ERROR_CANNOT_FIND_PHONEBOOK_ENTRY = 623
ERROR_CANNOT_WRITE_PHONEBOOK = 624
ERROR_CORRUPT_PHONEBOOK = 625
ERROR_CANNOT_LOAD_STRING = 626
ERROR_KEY_NOT_FOUND = 627
ERROR_DISCONNECTION = 628
ERROR_REMOTE_DISCONNECTION = 629
ERROR_HARDWARE_FAILURE = 630
ERROR_USER_DISCONNECTION = 631
ERROR_INVALID_SIZE = 632
ERROR_PORT_NOT_AVAILABLE = 633
ERROR_CANNOT_PROJECT_CLIENT = 634
ERROR_UNKNOWN = 635
ERROR_WRONG_DEVICE_ATTACHED = 636
ERROR_BAD_STRING = 637
ERROR_REQUEST_TIMEOUT = 638
ERROR_CANNOT_GET_LANA = 639
ERROR_NETBIOS_ERROR = 640
ERROR_SERVER_OUT_OF_RESOURCES = 641
ERROR_NAME_EXISTS_ON_NET = 642
ERROR_SERVER_GENERAL_NET_FAILURE = 643
WARNING_MSG_ALIAS_NOT_ADDED = 644
ERROR_AUTH_INTERNAL = 645
ERROR_RESTRICTED_LOGON_HOURS = 646
ERROR_ACCT_DISABLED = 647
ERROR_PASSWD_EXPIRED = 648
ERROR_NO_DIALIN_PERMISSION = 649
ERROR_SERVER_NOT_RESPONDING = 650
ERROR_FROM_DEVICE = 651
ERROR_UNRECOGNIZED_RESPONSE = 652
ERROR_MACRO_NOT_FOUND = 653
ERROR_MACRO_NOT_DEFINED = 654
ERROR_MESSAGE_MACRO_NOT_FOUND = 655
ERROR_DEFAULTOFF_MACRO_NOT_FOUND = 656
ERROR_FILE_COULD_NOT_BE_OPENED = 657
ERROR_DEVICENAME_TOO_LONG = 658
ERROR_DEVICENAME_NOT_FOUND = 659
ERROR_NO_RESPONSES = 660
ERROR_NO_COMMAND_FOUND = 661
ERROR_WRONG_KEY_SPECIFIED = 662
ERROR_UNKNOWN_DEVICE_TYPE = 663
ERROR_ALLOCATING_MEMORY = 664
ERROR_PORT_NOT_CONFIGURED = 665
ERROR_DEVICE_NOT_READY = 666
ERROR_READING_INI_FILE = 667
ERROR_NO_CONNECTION = 668
ERROR_BAD_USAGE_IN_INI_FILE = 669
ERROR_READING_SECTIONNAME = 670
ERROR_READING_DEVICETYPE = 671
ERROR_READING_DEVICENAME = 672
ERROR_READING_USAGE = 673
ERROR_READING_MAXCONNECTBPS = 674
ERROR_READING_MAXCARRIERBPS = 675
ERROR_LINE_BUSY = 676
ERROR_VOICE_ANSWER = 677
ERROR_NO_ANSWER = 678
ERROR_NO_CARRIER = 679
ERROR_NO_DIALTONE = 680
ERROR_IN_COMMAND = 681
ERROR_WRITING_SECTIONNAME = 682
ERROR_WRITING_DEVICETYPE = 683
ERROR_WRITING_DEVICENAME = 684
ERROR_WRITING_MAXCONNECTBPS = 685
ERROR_WRITING_MAXCARRIERBPS = 686
ERROR_WRITING_USAGE = 687
ERROR_WRITING_DEFAULTOFF = 688
ERROR_READING_DEFAULTOFF = 689
ERROR_EMPTY_INI_FILE = 690
ERROR_AUTHENTICATION_FAILURE = 691
ERROR_PORT_OR_DEVICE = 692
ERROR_NOT_BINARY_MACRO = 693
ERROR_DCB_NOT_FOUND = 694
ERROR_STATE_MACHINES_NOT_STARTED = 695
ERROR_STATE_MACHINES_ALREADY_STARTED = 696
ERROR_PARTIAL_RESPONSE_LOOPING = 697
ERROR_UNKNOWN_RESPONSE_KEY = 698
ERROR_RECV_BUF_FULL = 699
ERROR_CMD_TOO_LONG = 700
ERROR_UNSUPPORTED_BPS = 701
ERROR_UNEXPECTED_RESPONSE = 702
ERROR_INTERACTIVE_MODE = 703
ERROR_BAD_CALLBACK_NUMBER = 704
ERROR_INVALID_AUTH_STATE = 705
ERROR_WRITING_INITBPS = 706
ERROR_X25_DIAGNOSTIC = 707
ERROR_ACCT_EXPIRED = 708
ERROR_CHANGING_PASSWORD = 709
ERROR_OVERRUN = 710
ERROR_RASMAN_CANNOT_INITIALIZE = 711
ERROR_BIPLEX_PORT_NOT_AVAILABLE = 712
ERROR_NO_ACTIVE_ISDN_LINES = 713
ERROR_NO_ISDN_CHANNELS_AVAILABLE = 714
ERROR_TOO_MANY_LINE_ERRORS = 715
ERROR_IP_CONFIGURATION = 716
ERROR_NO_IP_ADDRESSES = 717
ERROR_PPP_TIMEOUT = 718
ERROR_PPP_REMOTE_TERMINATED = 719
ERROR_PPP_NO_PROTOCOLS_CONFIGURED = 720
ERROR_PPP_NO_RESPONSE = 721
ERROR_PPP_INVALID_PACKET = 722
ERROR_PHONE_NUMBER_TOO_LONG = 723
ERROR_IPXCP_NO_DIALOUT_CONFIGURED = 724
ERROR_IPXCP_NO_DIALIN_CONFIGURED = 725
ERROR_IPXCP_DIALOUT_ALREADY_ACTIVE = 726
ERROR_ACCESSING_TCPCFGDLL = 727
ERROR_NO_IP_RAS_ADAPTER = 728
ERROR_SLIP_REQUIRES_IP = 729
ERROR_PROJECTION_NOT_COMPLETE = 730
ERROR_PROTOCOL_NOT_CONFIGURED = 731
ERROR_PPP_NOT_CONVERGING = 732
ERROR_PPP_CP_REJECTED = 733
ERROR_PPP_LCP_TERMINATED = 734
ERROR_PPP_REQUIRED_ADDRESS_REJECTED = 735
ERROR_PPP_NCP_TERMINATED = 736
ERROR_PPP_LOOPBACK_DETECTED = 737
ERROR_PPP_NO_ADDRESS_ASSIGNED = 738
ERROR_CANNOT_USE_LOGON_CREDENTIALS = 739
ERROR_TAPI_CONFIGURATION = 740
ERROR_NO_LOCAL_ENCRYPTION = 741
ERROR_NO_REMOTE_ENCRYPTION = 742
ERROR_REMOTE_REQUIRES_ENCRYPTION = 743
ERROR_IPXCP_NET_NUMBER_CONFLICT = 744
ERROR_INVALID_SMM = 745
ERROR_SMM_UNINITIALIZED = 746
ERROR_NO_MAC_FOR_PORT = 747
ERROR_SMM_TIMEOUT = 748
ERROR_BAD_PHONE_NUMBER = 749
ERROR_WRONG_MODULE = 750
ERROR_INVALID_CALLBACK_NUMBER = 751
ERROR_SCRIPT_SYNTAX = 752
ERROR_HANGUP_FAILED = 753
ERROR_BUNDLE_NOT_FOUND = 754
ERROR_CANNOT_DO_CUSTOMDIAL = 755
ERROR_DIAL_ALREADY_IN_PROGRESS = 756
ERROR_RASAUTO_CANNOT_INITIALIZE = 757
ERROR_CONNECTION_ALREADY_SHARED = 758
ERROR_SHARING_CHANGE_FAILED = 759
ERROR_SHARING_ROUTER_INSTALL = 760
ERROR_SHARE_CONNECTION_FAILED = 761
ERROR_SHARING_PRIVATE_INSTALL = 762
ERROR_CANNOT_SHARE_CONNECTION = 763
ERROR_NO_SMART_CARD_READER = 764
ERROR_SHARING_ADDRESS_EXISTS = 765
ERROR_NO_CERTIFICATE = 766
ERROR_SHARING_MULTIPLE_ADDRESSES = 767
ERROR_FAILED_TO_ENCRYPT = 768
ERROR_BAD_ADDRESS_SPECIFIED = 769
ERROR_CONNECTION_REJECT = 770
ERROR_CONGESTION = 771
ERROR_INCOMPATIBLE = 772
ERROR_NUMBERCHANGED = 773
ERROR_TEMPFAILURE = 774
ERROR_BLOCKED = 775
ERROR_DONOTDISTURB = 776
ERROR_OUTOFORDER = 777
ERROR_UNABLE_TO_AUTHENTICATE_SERVER = 778
ERROR_SMART_CARD_REQUIRED = 779
ERROR_INVALID_FUNCTION_FOR_ENTRY = 780
ERROR_CERT_FOR_ENCRYPTION_NOT_FOUND = 781
ERROR_SHARING_RRAS_CONFLICT = 782
ERROR_SHARING_NO_PRIVATE_LAN = 783
ERROR_NO_DIFF_USER_AT_LOGON = 784
ERROR_NO_REG_CERT_AT_LOGON = 785
ERROR_OAKLEY_NO_CERT = 786
ERROR_OAKLEY_AUTH_FAIL = 787
ERROR_OAKLEY_ATTRIB_FAIL = 788
ERROR_OAKLEY_GENERAL_PROCESSING = 789
ERROR_OAKLEY_NO_PEER_CERT = 790
ERROR_OAKLEY_NO_POLICY = 791
ERROR_OAKLEY_TIMED_OUT = 792
ERROR_OAKLEY_ERROR = 793
ERROR_UNKNOWN_FRAMED_PROTOCOL = 794
ERROR_WRONG_TUNNEL_TYPE = 795
ERROR_UNKNOWN_SERVICE_TYPE = 796
ERROR_CONNECTING_DEVICE_NOT_FOUND = 797
ERROR_NO_EAPTLS_CERTIFICATE = 798
ERROR_SHARING_HOST_ADDRESS_CONFLICT = 799
ERROR_AUTOMATIC_VPN_FAILED = 800
ERROR_VALIDATING_SERVER_CERT = 801
ERROR_READING_SCARD = 802
ERROR_INVALID_PEAP_COOKIE_CONFIG = 803
ERROR_INVALID_PEAP_COOKIE_USER = 804
ERROR_INVALID_MSCHAPV2_CONFIG = 805
ERROR_VPN_GRE_BLOCKED = 806
ERROR_VPN_DISCONNECT = 807
ERROR_VPN_REFUSED = 808
ERROR_VPN_TIMEOUT = 809
ERROR_VPN_BAD_CERT = 810
ERROR_VPN_BAD_PSK = 811
ERROR_SERVER_POLICY = 812
ERROR_BROADBAND_ACTIVE = 813
ERROR_BROADBAND_NO_NIC = 814
ERROR_BROADBAND_TIMEOUT = 815
ERROR_FEATURE_DEPRECATED = 816
ERROR_CANNOT_DELETE = 817
ERROR_RASQEC_RESOURCE_CREATION_FAILED = 818
ERROR_RASQEC_NAPAGENT_NOT_ENABLED = 819
ERROR_RASQEC_NAPAGENT_NOT_CONNECTED = 820
ERROR_RASQEC_CONN_DOESNOTEXIST = 821
ERROR_RASQEC_TIMEOUT = 822
ERROR_PEAP_CRYPTOBINDING_INVALID = 823
ERROR_PEAP_CRYPTOBINDING_NOTRECEIVED = 824
ERROR_INVALID_VPNSTRATEGY = 825
ERROR_EAPTLS_CACHE_CREDENTIALS_INVALID = 826
ERROR_IPSEC_SERVICE_STOPPED = 827
ERROR_IDLE_TIMEOUT = 828
ERROR_LINK_FAILURE = 829
ERROR_USER_LOGOFF = 830
ERROR_FAST_USER_SWITCH = 831
ERROR_HIBERNATION = 832
ERROR_SYSTEM_SUSPENDED = 833
ERROR_RASMAN_SERVICE_STOPPED = 834
ERROR_INVALID_SERVER_CERT = 835
ERROR_NOT_NAP_CAPABLE = 836
ERROR_INVALID_TUNNELID = 837
ERROR_UPDATECONNECTION_REQUEST_IN_PROCESS = 838
ERROR_PROTOCOL_ENGINE_DISABLED = 839
ERROR_INTERNAL_ADDRESS_FAILURE = 840
ERROR_FAILED_CP_REQUIRED = 841
ERROR_TS_UNACCEPTABLE = 842
ERROR_MOBIKE_DISABLED = 843
ERROR_CANNOT_INITIATE_MOBIKE_UPDATE = 844
ERROR_PEAP_SERVER_REJECTED_CLIENT_TLV = 845
ERROR_INVALID_PREFERENCES = 846
ERROR_EAPTLS_SCARD_CACHE_CREDENTIALS_INVALID = 847
ERROR_SSTP_COOKIE_SET_FAILURE = 848
ERROR_INVALID_PEAP_COOKIE_ATTRIBUTES = 849
ERROR_EAP_METHOD_NOT_INSTALLED = 850
ERROR_EAP_METHOD_DOES_NOT_SUPPORT_SSO = 851
ERROR_EAP_METHOD_OPERATION_NOT_SUPPORTED = 852
ERROR_EAP_USER_CERT_INVALID = 853
ERROR_EAP_USER_CERT_EXPIRED = 854
ERROR_EAP_USER_CERT_REVOKED = 855
ERROR_EAP_USER_CERT_OTHER_ERROR = 856
ERROR_EAP_SERVER_CERT_INVALID = 857
ERROR_EAP_SERVER_CERT_EXPIRED = 858
ERROR_EAP_SERVER_CERT_REVOKED = 859
ERROR_EAP_SERVER_CERT_OTHER_ERROR = 860
ERROR_EAP_USER_ROOT_CERT_NOT_FOUND = 861
ERROR_EAP_USER_ROOT_CERT_INVALID = 862
ERROR_EAP_USER_ROOT_CERT_EXPIRED = 863
ERROR_EAP_SERVER_ROOT_CERT_NOT_FOUND = 864
ERROR_EAP_SERVER_ROOT_CERT_INVALID = 865
ERROR_EAP_SERVER_ROOT_CERT_NAME_REQUIRED = 866
ERROR_PEAP_IDENTITY_MISMATCH = 867
ERROR_DNSNAME_NOT_RESOLVABLE = 868
ERROR_EAPTLS_PASSWD_INVALID = 869
ERROR_IKEV2_PSK_INTERFACE_ALREADY_EXISTS = 870
ERROR_INVALID_DESTINATION_IP = 871
ERROR_INVALID_INTERFACE_CONFIG = 872
ERROR_VPN_PLUGIN_GENERIC = 873
ERROR_SSO_CERT_MISSING = 874
ERROR_DEVICE_COMPLIANCE = 875
ERROR_PLUGIN_NOT_INSTALLED = 876
ERROR_ACTION_REQUIRED = 877
RASBASEEND = 877
MPR_INTERFACE_DIAL_MODE = UInt32
MPRDM_DialFirst = 0
MPRDM_DialAll = 1
MPRDM_DialAsNeeded = 2
RASENTRY_DIAL_MODE = UInt32
RASEDM_DialAll = 1
RASEDM_DialAsNeeded = 2
RAS_FLAGS = UInt32
RAS_FLAGS_PPP_CONNECTION = 1
RAS_FLAGS_MESSENGER_PRESENT = 2
RAS_FLAGS_QUARANTINE_PRESENT = 8
RAS_FLAGS_ARAP_CONNECTION = 16
RAS_FLAGS_IKEV2_CONNECTION = 16
RAS_FLAGS_DORMANT = 32
MPR_ET = UInt32
MPR_ET_None = 0
MPR_ET_Require = 1
MPR_ET_RequireMax = 2
MPR_ET_Optional = 3
RASPPP_PROJECTION_INFO_SERVER_AUTH_DATA = UInt32
RASLCPAD_CHAP_MD5 = 5
RASLCPAD_CHAP_MS = 128
RASLCPAD_CHAP_MSV2 = 129
PPP_LCP = UInt32
PPP_LCP_PAP = 49187
PPP_LCP_CHAP = 49699
PPP_LCP_EAP = 49703
PPP_LCP_SPAP = 49191
RASPPP_PROJECTION_INFO_SERVER_AUTH_PROTOCOL = UInt32
RASLCPAP_PAP = 49187
RASLCPAP_SPAP = 49191
RASLCPAP_CHAP = 49699
RASLCPAP_EAP = 49703
PPP_LCP_INFO_AUTH_DATA = UInt32
PPP_LCP_CHAP_MD5 = 5
PPP_LCP_CHAP_MS = 128
PPP_LCP_CHAP_MSV2 = 129
RASIKEV_PROJECTION_INFO_FLAGS = UInt32
RASIKEv2_FLAGS_MOBIKESUPPORTED = 1
RASIKEv2_FLAGS_BEHIND_NAT = 2
RASIKEv2_FLAGS_SERVERBEHIND_NAT = 4
MPR_VS = UInt32
MPR_VS_Default = 0
MPR_VS_PptpOnly = 1
MPR_VS_PptpFirst = 2
MPR_VS_L2tpOnly = 3
MPR_VS_L2tpFirst = 4
SECURITY_MESSAGE_MSG_ID = UInt32
SECURITYMSG_SUCCESS = 1
SECURITYMSG_FAILURE = 2
SECURITYMSG_ERROR = 3
HRASCONN = IntPtr
RASAPIVERSION = Int32
RASAPIVERSION_500 = 1
RASAPIVERSION_501 = 2
RASAPIVERSION_600 = 3
RASAPIVERSION_601 = 4
def _define_RASIPADDR_head():
    class RASIPADDR(Structure):
        pass
    return RASIPADDR
def _define_RASIPADDR():
    RASIPADDR = win32more.NetworkManagement.Rras.RASIPADDR_head
    RASIPADDR._fields_ = [
        ("a", Byte),
        ("b", Byte),
        ("c", Byte),
        ("d", Byte),
    ]
    return RASIPADDR
def _define_RASTUNNELENDPOINT_head():
    class RASTUNNELENDPOINT(Structure):
        pass
    return RASTUNNELENDPOINT
def _define_RASTUNNELENDPOINT():
    RASTUNNELENDPOINT = win32more.NetworkManagement.Rras.RASTUNNELENDPOINT_head
    class RASTUNNELENDPOINT__Anonymous_e__Union(Union):
        pass
    RASTUNNELENDPOINT__Anonymous_e__Union._fields_ = [
        ("ipv4", win32more.Networking.WinSock.IN_ADDR),
        ("ipv6", win32more.Networking.WinSock.IN6_ADDR),
    ]
    RASTUNNELENDPOINT._anonymous_ = [
        'Anonymous',
    ]
    RASTUNNELENDPOINT._fields_ = [
        ("dwType", UInt32),
        ("Anonymous", RASTUNNELENDPOINT__Anonymous_e__Union),
    ]
    return RASTUNNELENDPOINT
def _define_RASCONNW_head():
    class RASCONNW(Structure):
        pass
    return RASCONNW
def _define_RASCONNW():
    RASCONNW = win32more.NetworkManagement.Rras.RASCONNW_head
    RASCONNW._pack_ = 4
    RASCONNW._fields_ = [
        ("dwSize", UInt32),
        ("hrasconn", win32more.NetworkManagement.Rras.HRASCONN),
        ("szEntryName", Char * 257),
        ("szDeviceType", Char * 17),
        ("szDeviceName", Char * 129),
        ("szPhonebook", Char * 260),
        ("dwSubEntry", UInt32),
        ("guidEntry", Guid),
        ("dwFlags", UInt32),
        ("luid", win32more.Foundation.LUID),
        ("guidCorrelationId", Guid),
    ]
    return RASCONNW
def _define_RASCONNA_head():
    class RASCONNA(Structure):
        pass
    return RASCONNA
def _define_RASCONNA():
    RASCONNA = win32more.NetworkManagement.Rras.RASCONNA_head
    RASCONNA._pack_ = 4
    RASCONNA._fields_ = [
        ("dwSize", UInt32),
        ("hrasconn", win32more.NetworkManagement.Rras.HRASCONN),
        ("szEntryName", win32more.Foundation.CHAR * 257),
        ("szDeviceType", win32more.Foundation.CHAR * 17),
        ("szDeviceName", win32more.Foundation.CHAR * 129),
        ("szPhonebook", win32more.Foundation.CHAR * 260),
        ("dwSubEntry", UInt32),
        ("guidEntry", Guid),
        ("dwFlags", UInt32),
        ("luid", win32more.Foundation.LUID),
        ("guidCorrelationId", Guid),
    ]
    return RASCONNA
RASCONNSTATE = Int32
RASCS_OpenPort = 0
RASCS_PortOpened = 1
RASCS_ConnectDevice = 2
RASCS_DeviceConnected = 3
RASCS_AllDevicesConnected = 4
RASCS_Authenticate = 5
RASCS_AuthNotify = 6
RASCS_AuthRetry = 7
RASCS_AuthCallback = 8
RASCS_AuthChangePassword = 9
RASCS_AuthProject = 10
RASCS_AuthLinkSpeed = 11
RASCS_AuthAck = 12
RASCS_ReAuthenticate = 13
RASCS_Authenticated = 14
RASCS_PrepareForCallback = 15
RASCS_WaitForModemReset = 16
RASCS_WaitForCallback = 17
RASCS_Projected = 18
RASCS_StartAuthentication = 19
RASCS_CallbackComplete = 20
RASCS_LogonNetwork = 21
RASCS_SubEntryConnected = 22
RASCS_SubEntryDisconnected = 23
RASCS_ApplySettings = 24
RASCS_Interactive = 4096
RASCS_RetryAuthentication = 4097
RASCS_CallbackSetByCaller = 4098
RASCS_PasswordExpired = 4099
RASCS_InvokeEapUI = 4100
RASCS_Connected = 8192
RASCS_Disconnected = 8193
RASCONNSUBSTATE = Int32
RASCSS_None = 0
RASCSS_Dormant = 1
RASCSS_Reconnecting = 2
RASCSS_Reconnected = 8192
def _define_RASCONNSTATUSW_head():
    class RASCONNSTATUSW(Structure):
        pass
    return RASCONNSTATUSW
def _define_RASCONNSTATUSW():
    RASCONNSTATUSW = win32more.NetworkManagement.Rras.RASCONNSTATUSW_head
    RASCONNSTATUSW._fields_ = [
        ("dwSize", UInt32),
        ("rasconnstate", win32more.NetworkManagement.Rras.RASCONNSTATE),
        ("dwError", UInt32),
        ("szDeviceType", Char * 17),
        ("szDeviceName", Char * 129),
        ("szPhoneNumber", Char * 129),
        ("localEndPoint", win32more.NetworkManagement.Rras.RASTUNNELENDPOINT),
        ("remoteEndPoint", win32more.NetworkManagement.Rras.RASTUNNELENDPOINT),
        ("rasconnsubstate", win32more.NetworkManagement.Rras.RASCONNSUBSTATE),
    ]
    return RASCONNSTATUSW
def _define_RASCONNSTATUSA_head():
    class RASCONNSTATUSA(Structure):
        pass
    return RASCONNSTATUSA
def _define_RASCONNSTATUSA():
    RASCONNSTATUSA = win32more.NetworkManagement.Rras.RASCONNSTATUSA_head
    RASCONNSTATUSA._fields_ = [
        ("dwSize", UInt32),
        ("rasconnstate", win32more.NetworkManagement.Rras.RASCONNSTATE),
        ("dwError", UInt32),
        ("szDeviceType", win32more.Foundation.CHAR * 17),
        ("szDeviceName", win32more.Foundation.CHAR * 129),
        ("szPhoneNumber", win32more.Foundation.CHAR * 129),
        ("localEndPoint", win32more.NetworkManagement.Rras.RASTUNNELENDPOINT),
        ("remoteEndPoint", win32more.NetworkManagement.Rras.RASTUNNELENDPOINT),
        ("rasconnsubstate", win32more.NetworkManagement.Rras.RASCONNSUBSTATE),
    ]
    return RASCONNSTATUSA
def _define_RASDIALPARAMSW_head():
    class RASDIALPARAMSW(Structure):
        pass
    return RASDIALPARAMSW
def _define_RASDIALPARAMSW():
    RASDIALPARAMSW = win32more.NetworkManagement.Rras.RASDIALPARAMSW_head
    RASDIALPARAMSW._pack_ = 4
    RASDIALPARAMSW._fields_ = [
        ("dwSize", UInt32),
        ("szEntryName", Char * 257),
        ("szPhoneNumber", Char * 129),
        ("szCallbackNumber", Char * 129),
        ("szUserName", Char * 257),
        ("szPassword", Char * 257),
        ("szDomain", Char * 16),
        ("dwSubEntry", UInt32),
        ("dwCallbackId", UIntPtr),
        ("dwIfIndex", UInt32),
        ("szEncPassword", win32more.Foundation.PWSTR),
    ]
    return RASDIALPARAMSW
def _define_RASDIALPARAMSA_head():
    class RASDIALPARAMSA(Structure):
        pass
    return RASDIALPARAMSA
def _define_RASDIALPARAMSA():
    RASDIALPARAMSA = win32more.NetworkManagement.Rras.RASDIALPARAMSA_head
    RASDIALPARAMSA._pack_ = 4
    RASDIALPARAMSA._fields_ = [
        ("dwSize", UInt32),
        ("szEntryName", win32more.Foundation.CHAR * 257),
        ("szPhoneNumber", win32more.Foundation.CHAR * 129),
        ("szCallbackNumber", win32more.Foundation.CHAR * 129),
        ("szUserName", win32more.Foundation.CHAR * 257),
        ("szPassword", win32more.Foundation.CHAR * 257),
        ("szDomain", win32more.Foundation.CHAR * 16),
        ("dwSubEntry", UInt32),
        ("dwCallbackId", UIntPtr),
        ("dwIfIndex", UInt32),
        ("szEncPassword", win32more.Foundation.PSTR),
    ]
    return RASDIALPARAMSA
def _define_RASEAPINFO_head():
    class RASEAPINFO(Structure):
        pass
    return RASEAPINFO
def _define_RASEAPINFO():
    RASEAPINFO = win32more.NetworkManagement.Rras.RASEAPINFO_head
    RASEAPINFO._pack_ = 4
    RASEAPINFO._fields_ = [
        ("dwSizeofEapInfo", UInt32),
        ("pbEapInfo", c_char_p_no),
    ]
    return RASEAPINFO
def _define_RASDEVSPECIFICINFO_head():
    class RASDEVSPECIFICINFO(Structure):
        pass
    return RASDEVSPECIFICINFO
def _define_RASDEVSPECIFICINFO():
    RASDEVSPECIFICINFO = win32more.NetworkManagement.Rras.RASDEVSPECIFICINFO_head
    RASDEVSPECIFICINFO._pack_ = 4
    RASDEVSPECIFICINFO._fields_ = [
        ("dwSize", UInt32),
        ("pbDevSpecificInfo", c_char_p_no),
    ]
    return RASDEVSPECIFICINFO
def _define_RASDIALEXTENSIONS_head():
    class RASDIALEXTENSIONS(Structure):
        pass
    return RASDIALEXTENSIONS
def _define_RASDIALEXTENSIONS():
    RASDIALEXTENSIONS = win32more.NetworkManagement.Rras.RASDIALEXTENSIONS_head
    RASDIALEXTENSIONS._pack_ = 4
    RASDIALEXTENSIONS._fields_ = [
        ("dwSize", UInt32),
        ("dwfOptions", UInt32),
        ("hwndParent", win32more.Foundation.HWND),
        ("reserved", UIntPtr),
        ("reserved1", UIntPtr),
        ("RasEapInfo", win32more.NetworkManagement.Rras.RASEAPINFO),
        ("fSkipPppAuth", win32more.Foundation.BOOL),
        ("RasDevSpecificInfo", win32more.NetworkManagement.Rras.RASDEVSPECIFICINFO),
    ]
    return RASDIALEXTENSIONS
def _define_RASENTRYNAMEW_head():
    class RASENTRYNAMEW(Structure):
        pass
    return RASENTRYNAMEW
def _define_RASENTRYNAMEW():
    RASENTRYNAMEW = win32more.NetworkManagement.Rras.RASENTRYNAMEW_head
    RASENTRYNAMEW._fields_ = [
        ("dwSize", UInt32),
        ("szEntryName", Char * 257),
        ("dwFlags", UInt32),
        ("szPhonebookPath", Char * 261),
    ]
    return RASENTRYNAMEW
def _define_RASENTRYNAMEA_head():
    class RASENTRYNAMEA(Structure):
        pass
    return RASENTRYNAMEA
def _define_RASENTRYNAMEA():
    RASENTRYNAMEA = win32more.NetworkManagement.Rras.RASENTRYNAMEA_head
    RASENTRYNAMEA._fields_ = [
        ("dwSize", UInt32),
        ("szEntryName", win32more.Foundation.CHAR * 257),
        ("dwFlags", UInt32),
        ("szPhonebookPath", win32more.Foundation.CHAR * 261),
    ]
    return RASENTRYNAMEA
RASPROJECTION = Int32
RASP_Amb = 65536
RASP_PppNbf = 32831
RASP_PppIpx = 32811
RASP_PppIp = 32801
RASP_PppCcp = 33021
RASP_PppLcp = 49185
RASP_PppIpv6 = 32855
def _define_RASAMBW_head():
    class RASAMBW(Structure):
        pass
    return RASAMBW
def _define_RASAMBW():
    RASAMBW = win32more.NetworkManagement.Rras.RASAMBW_head
    RASAMBW._fields_ = [
        ("dwSize", UInt32),
        ("dwError", UInt32),
        ("szNetBiosError", Char * 17),
        ("bLana", Byte),
    ]
    return RASAMBW
def _define_RASAMBA_head():
    class RASAMBA(Structure):
        pass
    return RASAMBA
def _define_RASAMBA():
    RASAMBA = win32more.NetworkManagement.Rras.RASAMBA_head
    RASAMBA._fields_ = [
        ("dwSize", UInt32),
        ("dwError", UInt32),
        ("szNetBiosError", win32more.Foundation.CHAR * 17),
        ("bLana", Byte),
    ]
    return RASAMBA
def _define_RASPPPNBFW_head():
    class RASPPPNBFW(Structure):
        pass
    return RASPPPNBFW
def _define_RASPPPNBFW():
    RASPPPNBFW = win32more.NetworkManagement.Rras.RASPPPNBFW_head
    RASPPPNBFW._fields_ = [
        ("dwSize", UInt32),
        ("dwError", UInt32),
        ("dwNetBiosError", UInt32),
        ("szNetBiosError", Char * 17),
        ("szWorkstationName", Char * 17),
        ("bLana", Byte),
    ]
    return RASPPPNBFW
def _define_RASPPPNBFA_head():
    class RASPPPNBFA(Structure):
        pass
    return RASPPPNBFA
def _define_RASPPPNBFA():
    RASPPPNBFA = win32more.NetworkManagement.Rras.RASPPPNBFA_head
    RASPPPNBFA._fields_ = [
        ("dwSize", UInt32),
        ("dwError", UInt32),
        ("dwNetBiosError", UInt32),
        ("szNetBiosError", win32more.Foundation.CHAR * 17),
        ("szWorkstationName", win32more.Foundation.CHAR * 17),
        ("bLana", Byte),
    ]
    return RASPPPNBFA
def _define_RASIPXW_head():
    class RASIPXW(Structure):
        pass
    return RASIPXW
def _define_RASIPXW():
    RASIPXW = win32more.NetworkManagement.Rras.RASIPXW_head
    RASIPXW._fields_ = [
        ("dwSize", UInt32),
        ("dwError", UInt32),
        ("szIpxAddress", Char * 22),
    ]
    return RASIPXW
def _define_RASPPPIPXA_head():
    class RASPPPIPXA(Structure):
        pass
    return RASPPPIPXA
def _define_RASPPPIPXA():
    RASPPPIPXA = win32more.NetworkManagement.Rras.RASPPPIPXA_head
    RASPPPIPXA._fields_ = [
        ("dwSize", UInt32),
        ("dwError", UInt32),
        ("szIpxAddress", win32more.Foundation.CHAR * 22),
    ]
    return RASPPPIPXA
def _define_RASPPPIPW_head():
    class RASPPPIPW(Structure):
        pass
    return RASPPPIPW
def _define_RASPPPIPW():
    RASPPPIPW = win32more.NetworkManagement.Rras.RASPPPIPW_head
    RASPPPIPW._fields_ = [
        ("dwSize", UInt32),
        ("dwError", UInt32),
        ("szIpAddress", Char * 16),
        ("szServerIpAddress", Char * 16),
        ("dwOptions", UInt32),
        ("dwServerOptions", UInt32),
    ]
    return RASPPPIPW
def _define_RASPPPIPA_head():
    class RASPPPIPA(Structure):
        pass
    return RASPPPIPA
def _define_RASPPPIPA():
    RASPPPIPA = win32more.NetworkManagement.Rras.RASPPPIPA_head
    RASPPPIPA._fields_ = [
        ("dwSize", UInt32),
        ("dwError", UInt32),
        ("szIpAddress", win32more.Foundation.CHAR * 16),
        ("szServerIpAddress", win32more.Foundation.CHAR * 16),
        ("dwOptions", UInt32),
        ("dwServerOptions", UInt32),
    ]
    return RASPPPIPA
def _define_RASPPPIPV6_head():
    class RASPPPIPV6(Structure):
        pass
    return RASPPPIPV6
def _define_RASPPPIPV6():
    RASPPPIPV6 = win32more.NetworkManagement.Rras.RASPPPIPV6_head
    RASPPPIPV6._fields_ = [
        ("dwSize", UInt32),
        ("dwError", UInt32),
        ("bLocalInterfaceIdentifier", Byte * 8),
        ("bPeerInterfaceIdentifier", Byte * 8),
        ("bLocalCompressionProtocol", Byte * 2),
        ("bPeerCompressionProtocol", Byte * 2),
    ]
    return RASPPPIPV6
def _define_RASPPPLCPW_head():
    class RASPPPLCPW(Structure):
        pass
    return RASPPPLCPW
def _define_RASPPPLCPW():
    RASPPPLCPW = win32more.NetworkManagement.Rras.RASPPPLCPW_head
    RASPPPLCPW._fields_ = [
        ("dwSize", UInt32),
        ("fBundled", win32more.Foundation.BOOL),
        ("dwError", UInt32),
        ("dwAuthenticationProtocol", UInt32),
        ("dwAuthenticationData", UInt32),
        ("dwEapTypeId", UInt32),
        ("dwServerAuthenticationProtocol", UInt32),
        ("dwServerAuthenticationData", UInt32),
        ("dwServerEapTypeId", UInt32),
        ("fMultilink", win32more.Foundation.BOOL),
        ("dwTerminateReason", UInt32),
        ("dwServerTerminateReason", UInt32),
        ("szReplyMessage", Char * 1024),
        ("dwOptions", UInt32),
        ("dwServerOptions", UInt32),
    ]
    return RASPPPLCPW
def _define_RASPPPLCPA_head():
    class RASPPPLCPA(Structure):
        pass
    return RASPPPLCPA
def _define_RASPPPLCPA():
    RASPPPLCPA = win32more.NetworkManagement.Rras.RASPPPLCPA_head
    RASPPPLCPA._fields_ = [
        ("dwSize", UInt32),
        ("fBundled", win32more.Foundation.BOOL),
        ("dwError", UInt32),
        ("dwAuthenticationProtocol", UInt32),
        ("dwAuthenticationData", UInt32),
        ("dwEapTypeId", UInt32),
        ("dwServerAuthenticationProtocol", UInt32),
        ("dwServerAuthenticationData", UInt32),
        ("dwServerEapTypeId", UInt32),
        ("fMultilink", win32more.Foundation.BOOL),
        ("dwTerminateReason", UInt32),
        ("dwServerTerminateReason", UInt32),
        ("szReplyMessage", win32more.Foundation.CHAR * 1024),
        ("dwOptions", UInt32),
        ("dwServerOptions", UInt32),
    ]
    return RASPPPLCPA
def _define_RASPPPCCP_head():
    class RASPPPCCP(Structure):
        pass
    return RASPPPCCP
def _define_RASPPPCCP():
    RASPPPCCP = win32more.NetworkManagement.Rras.RASPPPCCP_head
    RASPPPCCP._fields_ = [
        ("dwSize", UInt32),
        ("dwError", UInt32),
        ("dwCompressionAlgorithm", UInt32),
        ("dwOptions", UInt32),
        ("dwServerCompressionAlgorithm", UInt32),
        ("dwServerOptions", UInt32),
    ]
    return RASPPPCCP
def _define_RASPPP_PROJECTION_INFO_head():
    class RASPPP_PROJECTION_INFO(Structure):
        pass
    return RASPPP_PROJECTION_INFO
def _define_RASPPP_PROJECTION_INFO():
    RASPPP_PROJECTION_INFO = win32more.NetworkManagement.Rras.RASPPP_PROJECTION_INFO_head
    RASPPP_PROJECTION_INFO._fields_ = [
        ("dwIPv4NegotiationError", UInt32),
        ("ipv4Address", win32more.Networking.WinSock.IN_ADDR),
        ("ipv4ServerAddress", win32more.Networking.WinSock.IN_ADDR),
        ("dwIPv4Options", UInt32),
        ("dwIPv4ServerOptions", UInt32),
        ("dwIPv6NegotiationError", UInt32),
        ("bInterfaceIdentifier", Byte * 8),
        ("bServerInterfaceIdentifier", Byte * 8),
        ("fBundled", win32more.Foundation.BOOL),
        ("fMultilink", win32more.Foundation.BOOL),
        ("dwAuthenticationProtocol", win32more.NetworkManagement.Rras.RASPPP_PROJECTION_INFO_SERVER_AUTH_PROTOCOL),
        ("dwAuthenticationData", win32more.NetworkManagement.Rras.RASPPP_PROJECTION_INFO_SERVER_AUTH_DATA),
        ("dwServerAuthenticationProtocol", win32more.NetworkManagement.Rras.RASPPP_PROJECTION_INFO_SERVER_AUTH_PROTOCOL),
        ("dwServerAuthenticationData", win32more.NetworkManagement.Rras.RASPPP_PROJECTION_INFO_SERVER_AUTH_DATA),
        ("dwEapTypeId", UInt32),
        ("dwServerEapTypeId", UInt32),
        ("dwLcpOptions", UInt32),
        ("dwLcpServerOptions", UInt32),
        ("dwCcpError", UInt32),
        ("dwCcpCompressionAlgorithm", UInt32),
        ("dwCcpServerCompressionAlgorithm", UInt32),
        ("dwCcpOptions", UInt32),
        ("dwCcpServerOptions", UInt32),
    ]
    return RASPPP_PROJECTION_INFO
def _define_RASIKEV2_PROJECTION_INFO_head():
    class RASIKEV2_PROJECTION_INFO(Structure):
        pass
    return RASIKEV2_PROJECTION_INFO
def _define_RASIKEV2_PROJECTION_INFO():
    RASIKEV2_PROJECTION_INFO = win32more.NetworkManagement.Rras.RASIKEV2_PROJECTION_INFO_head
    RASIKEV2_PROJECTION_INFO._pack_ = 4
    RASIKEV2_PROJECTION_INFO._fields_ = [
        ("dwIPv4NegotiationError", UInt32),
        ("ipv4Address", win32more.Networking.WinSock.IN_ADDR),
        ("ipv4ServerAddress", win32more.Networking.WinSock.IN_ADDR),
        ("dwIPv6NegotiationError", UInt32),
        ("ipv6Address", win32more.Networking.WinSock.IN6_ADDR),
        ("ipv6ServerAddress", win32more.Networking.WinSock.IN6_ADDR),
        ("dwPrefixLength", UInt32),
        ("dwAuthenticationProtocol", UInt32),
        ("dwEapTypeId", UInt32),
        ("dwFlags", win32more.NetworkManagement.Rras.RASIKEV_PROJECTION_INFO_FLAGS),
        ("dwEncryptionMethod", UInt32),
        ("numIPv4ServerAddresses", UInt32),
        ("ipv4ServerAddresses", POINTER(win32more.Networking.WinSock.IN_ADDR_head)),
        ("numIPv6ServerAddresses", UInt32),
        ("ipv6ServerAddresses", POINTER(win32more.Networking.WinSock.IN6_ADDR_head)),
    ]
    return RASIKEV2_PROJECTION_INFO
RASPROJECTION_INFO_TYPE = Int32
PROJECTION_INFO_TYPE_PPP = 1
PROJECTION_INFO_TYPE_IKEv2 = 2
IKEV2_ID_PAYLOAD_TYPE = Int32
IKEV2_ID_PAYLOAD_TYPE_INVALID = 0
IKEV2_ID_PAYLOAD_TYPE_IPV4_ADDR = 1
IKEV2_ID_PAYLOAD_TYPE_FQDN = 2
IKEV2_ID_PAYLOAD_TYPE_RFC822_ADDR = 3
IKEV2_ID_PAYLOAD_TYPE_RESERVED1 = 4
IKEV2_ID_PAYLOAD_TYPE_ID_IPV6_ADDR = 5
IKEV2_ID_PAYLOAD_TYPE_RESERVED2 = 6
IKEV2_ID_PAYLOAD_TYPE_RESERVED3 = 7
IKEV2_ID_PAYLOAD_TYPE_RESERVED4 = 8
IKEV2_ID_PAYLOAD_TYPE_DER_ASN1_DN = 9
IKEV2_ID_PAYLOAD_TYPE_DER_ASN1_GN = 10
IKEV2_ID_PAYLOAD_TYPE_KEY_ID = 11
IKEV2_ID_PAYLOAD_TYPE_MAX = 12
def _define_RAS_PROJECTION_INFO_head():
    class RAS_PROJECTION_INFO(Structure):
        pass
    return RAS_PROJECTION_INFO
def _define_RAS_PROJECTION_INFO():
    RAS_PROJECTION_INFO = win32more.NetworkManagement.Rras.RAS_PROJECTION_INFO_head
    class RAS_PROJECTION_INFO__Anonymous_e__Union(Union):
        pass
    RAS_PROJECTION_INFO__Anonymous_e__Union._fields_ = [
        ("ppp", win32more.NetworkManagement.Rras.RASPPP_PROJECTION_INFO),
        ("ikev2", win32more.NetworkManagement.Rras.RASIKEV2_PROJECTION_INFO),
    ]
    RAS_PROJECTION_INFO._anonymous_ = [
        'Anonymous',
    ]
    RAS_PROJECTION_INFO._fields_ = [
        ("version", win32more.NetworkManagement.Rras.RASAPIVERSION),
        ("type", win32more.NetworkManagement.Rras.RASPROJECTION_INFO_TYPE),
        ("Anonymous", RAS_PROJECTION_INFO__Anonymous_e__Union),
    ]
    return RAS_PROJECTION_INFO
def _define_RASDIALFUNC():
    return CFUNCTYPE(Void,UInt32,win32more.NetworkManagement.Rras.RASCONNSTATE,UInt32, use_last_error=False)
def _define_RASDIALFUNC1():
    return CFUNCTYPE(Void,win32more.NetworkManagement.Rras.HRASCONN,UInt32,win32more.NetworkManagement.Rras.RASCONNSTATE,UInt32,UInt32, use_last_error=False)
def _define_RASDIALFUNC2():
    return CFUNCTYPE(UInt32,UIntPtr,UInt32,win32more.NetworkManagement.Rras.HRASCONN,UInt32,win32more.NetworkManagement.Rras.RASCONNSTATE,UInt32,UInt32, use_last_error=False)
def _define_RASDEVINFOW_head():
    class RASDEVINFOW(Structure):
        pass
    return RASDEVINFOW
def _define_RASDEVINFOW():
    RASDEVINFOW = win32more.NetworkManagement.Rras.RASDEVINFOW_head
    RASDEVINFOW._fields_ = [
        ("dwSize", UInt32),
        ("szDeviceType", Char * 17),
        ("szDeviceName", Char * 129),
    ]
    return RASDEVINFOW
def _define_RASDEVINFOA_head():
    class RASDEVINFOA(Structure):
        pass
    return RASDEVINFOA
def _define_RASDEVINFOA():
    RASDEVINFOA = win32more.NetworkManagement.Rras.RASDEVINFOA_head
    RASDEVINFOA._fields_ = [
        ("dwSize", UInt32),
        ("szDeviceType", win32more.Foundation.CHAR * 17),
        ("szDeviceName", win32more.Foundation.CHAR * 129),
    ]
    return RASDEVINFOA
def _define_RASCTRYINFO_head():
    class RASCTRYINFO(Structure):
        pass
    return RASCTRYINFO
def _define_RASCTRYINFO():
    RASCTRYINFO = win32more.NetworkManagement.Rras.RASCTRYINFO_head
    RASCTRYINFO._fields_ = [
        ("dwSize", UInt32),
        ("dwCountryID", UInt32),
        ("dwNextCountryID", UInt32),
        ("dwCountryCode", UInt32),
        ("dwCountryNameOffset", UInt32),
    ]
    return RASCTRYINFO
def _define_RASENTRYA_head():
    class RASENTRYA(Structure):
        pass
    return RASENTRYA
def _define_RASENTRYA():
    RASENTRYA = win32more.NetworkManagement.Rras.RASENTRYA_head
    RASENTRYA._fields_ = [
        ("dwSize", UInt32),
        ("dwfOptions", UInt32),
        ("dwCountryID", UInt32),
        ("dwCountryCode", UInt32),
        ("szAreaCode", win32more.Foundation.CHAR * 11),
        ("szLocalPhoneNumber", win32more.Foundation.CHAR * 129),
        ("dwAlternateOffset", UInt32),
        ("ipaddr", win32more.NetworkManagement.Rras.RASIPADDR),
        ("ipaddrDns", win32more.NetworkManagement.Rras.RASIPADDR),
        ("ipaddrDnsAlt", win32more.NetworkManagement.Rras.RASIPADDR),
        ("ipaddrWins", win32more.NetworkManagement.Rras.RASIPADDR),
        ("ipaddrWinsAlt", win32more.NetworkManagement.Rras.RASIPADDR),
        ("dwFrameSize", UInt32),
        ("dwfNetProtocols", UInt32),
        ("dwFramingProtocol", UInt32),
        ("szScript", win32more.Foundation.CHAR * 260),
        ("szAutodialDll", win32more.Foundation.CHAR * 260),
        ("szAutodialFunc", win32more.Foundation.CHAR * 260),
        ("szDeviceType", win32more.Foundation.CHAR * 17),
        ("szDeviceName", win32more.Foundation.CHAR * 129),
        ("szX25PadType", win32more.Foundation.CHAR * 33),
        ("szX25Address", win32more.Foundation.CHAR * 201),
        ("szX25Facilities", win32more.Foundation.CHAR * 201),
        ("szX25UserData", win32more.Foundation.CHAR * 201),
        ("dwChannels", UInt32),
        ("dwReserved1", UInt32),
        ("dwReserved2", UInt32),
        ("dwSubEntries", UInt32),
        ("dwDialMode", win32more.NetworkManagement.Rras.RASENTRY_DIAL_MODE),
        ("dwDialExtraPercent", UInt32),
        ("dwDialExtraSampleSeconds", UInt32),
        ("dwHangUpExtraPercent", UInt32),
        ("dwHangUpExtraSampleSeconds", UInt32),
        ("dwIdleDisconnectSeconds", UInt32),
        ("dwType", UInt32),
        ("dwEncryptionType", UInt32),
        ("dwCustomAuthKey", UInt32),
        ("guidId", Guid),
        ("szCustomDialDll", win32more.Foundation.CHAR * 260),
        ("dwVpnStrategy", UInt32),
        ("dwfOptions2", UInt32),
        ("dwfOptions3", UInt32),
        ("szDnsSuffix", win32more.Foundation.CHAR * 256),
        ("dwTcpWindowSize", UInt32),
        ("szPrerequisitePbk", win32more.Foundation.CHAR * 260),
        ("szPrerequisiteEntry", win32more.Foundation.CHAR * 257),
        ("dwRedialCount", UInt32),
        ("dwRedialPause", UInt32),
        ("ipv6addrDns", win32more.Networking.WinSock.IN6_ADDR),
        ("ipv6addrDnsAlt", win32more.Networking.WinSock.IN6_ADDR),
        ("dwIPv4InterfaceMetric", UInt32),
        ("dwIPv6InterfaceMetric", UInt32),
        ("ipv6addr", win32more.Networking.WinSock.IN6_ADDR),
        ("dwIPv6PrefixLength", UInt32),
        ("dwNetworkOutageTime", UInt32),
        ("szIDi", win32more.Foundation.CHAR * 257),
        ("szIDr", win32more.Foundation.CHAR * 257),
        ("fIsImsConfig", win32more.Foundation.BOOL),
        ("IdiType", win32more.NetworkManagement.Rras.IKEV2_ID_PAYLOAD_TYPE),
        ("IdrType", win32more.NetworkManagement.Rras.IKEV2_ID_PAYLOAD_TYPE),
        ("fDisableIKEv2Fragmentation", win32more.Foundation.BOOL),
    ]
    return RASENTRYA
def _define_RASENTRYW_head():
    class RASENTRYW(Structure):
        pass
    return RASENTRYW
def _define_RASENTRYW():
    RASENTRYW = win32more.NetworkManagement.Rras.RASENTRYW_head
    RASENTRYW._fields_ = [
        ("dwSize", UInt32),
        ("dwfOptions", UInt32),
        ("dwCountryID", UInt32),
        ("dwCountryCode", UInt32),
        ("szAreaCode", Char * 11),
        ("szLocalPhoneNumber", Char * 129),
        ("dwAlternateOffset", UInt32),
        ("ipaddr", win32more.NetworkManagement.Rras.RASIPADDR),
        ("ipaddrDns", win32more.NetworkManagement.Rras.RASIPADDR),
        ("ipaddrDnsAlt", win32more.NetworkManagement.Rras.RASIPADDR),
        ("ipaddrWins", win32more.NetworkManagement.Rras.RASIPADDR),
        ("ipaddrWinsAlt", win32more.NetworkManagement.Rras.RASIPADDR),
        ("dwFrameSize", UInt32),
        ("dwfNetProtocols", UInt32),
        ("dwFramingProtocol", UInt32),
        ("szScript", Char * 260),
        ("szAutodialDll", Char * 260),
        ("szAutodialFunc", Char * 260),
        ("szDeviceType", Char * 17),
        ("szDeviceName", Char * 129),
        ("szX25PadType", Char * 33),
        ("szX25Address", Char * 201),
        ("szX25Facilities", Char * 201),
        ("szX25UserData", Char * 201),
        ("dwChannels", UInt32),
        ("dwReserved1", UInt32),
        ("dwReserved2", UInt32),
        ("dwSubEntries", UInt32),
        ("dwDialMode", win32more.NetworkManagement.Rras.RASENTRY_DIAL_MODE),
        ("dwDialExtraPercent", UInt32),
        ("dwDialExtraSampleSeconds", UInt32),
        ("dwHangUpExtraPercent", UInt32),
        ("dwHangUpExtraSampleSeconds", UInt32),
        ("dwIdleDisconnectSeconds", UInt32),
        ("dwType", UInt32),
        ("dwEncryptionType", UInt32),
        ("dwCustomAuthKey", UInt32),
        ("guidId", Guid),
        ("szCustomDialDll", Char * 260),
        ("dwVpnStrategy", UInt32),
        ("dwfOptions2", UInt32),
        ("dwfOptions3", UInt32),
        ("szDnsSuffix", Char * 256),
        ("dwTcpWindowSize", UInt32),
        ("szPrerequisitePbk", Char * 260),
        ("szPrerequisiteEntry", Char * 257),
        ("dwRedialCount", UInt32),
        ("dwRedialPause", UInt32),
        ("ipv6addrDns", win32more.Networking.WinSock.IN6_ADDR),
        ("ipv6addrDnsAlt", win32more.Networking.WinSock.IN6_ADDR),
        ("dwIPv4InterfaceMetric", UInt32),
        ("dwIPv6InterfaceMetric", UInt32),
        ("ipv6addr", win32more.Networking.WinSock.IN6_ADDR),
        ("dwIPv6PrefixLength", UInt32),
        ("dwNetworkOutageTime", UInt32),
        ("szIDi", Char * 257),
        ("szIDr", Char * 257),
        ("fIsImsConfig", win32more.Foundation.BOOL),
        ("IdiType", win32more.NetworkManagement.Rras.IKEV2_ID_PAYLOAD_TYPE),
        ("IdrType", win32more.NetworkManagement.Rras.IKEV2_ID_PAYLOAD_TYPE),
        ("fDisableIKEv2Fragmentation", win32more.Foundation.BOOL),
    ]
    return RASENTRYW
def _define_ORASADFUNC():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,win32more.Foundation.PSTR,UInt32,POINTER(UInt32), use_last_error=False)
def _define_RASADPARAMS_head():
    class RASADPARAMS(Structure):
        pass
    return RASADPARAMS
def _define_RASADPARAMS():
    RASADPARAMS = win32more.NetworkManagement.Rras.RASADPARAMS_head
    RASADPARAMS._pack_ = 4
    RASADPARAMS._fields_ = [
        ("dwSize", UInt32),
        ("hwndOwner", win32more.Foundation.HWND),
        ("dwFlags", UInt32),
        ("xDlg", Int32),
        ("yDlg", Int32),
    ]
    return RASADPARAMS
def _define_RASADFUNCA():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(win32more.NetworkManagement.Rras.RASADPARAMS_head),POINTER(UInt32), use_last_error=False)
def _define_RASADFUNCW():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Rras.RASADPARAMS_head),POINTER(UInt32), use_last_error=False)
def _define_RASSUBENTRYA_head():
    class RASSUBENTRYA(Structure):
        pass
    return RASSUBENTRYA
def _define_RASSUBENTRYA():
    RASSUBENTRYA = win32more.NetworkManagement.Rras.RASSUBENTRYA_head
    RASSUBENTRYA._fields_ = [
        ("dwSize", UInt32),
        ("dwfFlags", UInt32),
        ("szDeviceType", win32more.Foundation.CHAR * 17),
        ("szDeviceName", win32more.Foundation.CHAR * 129),
        ("szLocalPhoneNumber", win32more.Foundation.CHAR * 129),
        ("dwAlternateOffset", UInt32),
    ]
    return RASSUBENTRYA
def _define_RASSUBENTRYW_head():
    class RASSUBENTRYW(Structure):
        pass
    return RASSUBENTRYW
def _define_RASSUBENTRYW():
    RASSUBENTRYW = win32more.NetworkManagement.Rras.RASSUBENTRYW_head
    RASSUBENTRYW._fields_ = [
        ("dwSize", UInt32),
        ("dwfFlags", UInt32),
        ("szDeviceType", Char * 17),
        ("szDeviceName", Char * 129),
        ("szLocalPhoneNumber", Char * 129),
        ("dwAlternateOffset", UInt32),
    ]
    return RASSUBENTRYW
def _define_RASCREDENTIALSA_head():
    class RASCREDENTIALSA(Structure):
        pass
    return RASCREDENTIALSA
def _define_RASCREDENTIALSA():
    RASCREDENTIALSA = win32more.NetworkManagement.Rras.RASCREDENTIALSA_head
    RASCREDENTIALSA._fields_ = [
        ("dwSize", UInt32),
        ("dwMask", UInt32),
        ("szUserName", win32more.Foundation.CHAR * 257),
        ("szPassword", win32more.Foundation.CHAR * 257),
        ("szDomain", win32more.Foundation.CHAR * 16),
    ]
    return RASCREDENTIALSA
def _define_RASCREDENTIALSW_head():
    class RASCREDENTIALSW(Structure):
        pass
    return RASCREDENTIALSW
def _define_RASCREDENTIALSW():
    RASCREDENTIALSW = win32more.NetworkManagement.Rras.RASCREDENTIALSW_head
    RASCREDENTIALSW._fields_ = [
        ("dwSize", UInt32),
        ("dwMask", UInt32),
        ("szUserName", Char * 257),
        ("szPassword", Char * 257),
        ("szDomain", Char * 16),
    ]
    return RASCREDENTIALSW
def _define_RASAUTODIALENTRYA_head():
    class RASAUTODIALENTRYA(Structure):
        pass
    return RASAUTODIALENTRYA
def _define_RASAUTODIALENTRYA():
    RASAUTODIALENTRYA = win32more.NetworkManagement.Rras.RASAUTODIALENTRYA_head
    RASAUTODIALENTRYA._fields_ = [
        ("dwSize", UInt32),
        ("dwFlags", UInt32),
        ("dwDialingLocation", UInt32),
        ("szEntry", win32more.Foundation.CHAR * 257),
    ]
    return RASAUTODIALENTRYA
def _define_RASAUTODIALENTRYW_head():
    class RASAUTODIALENTRYW(Structure):
        pass
    return RASAUTODIALENTRYW
def _define_RASAUTODIALENTRYW():
    RASAUTODIALENTRYW = win32more.NetworkManagement.Rras.RASAUTODIALENTRYW_head
    RASAUTODIALENTRYW._fields_ = [
        ("dwSize", UInt32),
        ("dwFlags", UInt32),
        ("dwDialingLocation", UInt32),
        ("szEntry", Char * 257),
    ]
    return RASAUTODIALENTRYW
def _define_RASEAPUSERIDENTITYA_head():
    class RASEAPUSERIDENTITYA(Structure):
        pass
    return RASEAPUSERIDENTITYA
def _define_RASEAPUSERIDENTITYA():
    RASEAPUSERIDENTITYA = win32more.NetworkManagement.Rras.RASEAPUSERIDENTITYA_head
    RASEAPUSERIDENTITYA._fields_ = [
        ("szUserName", win32more.Foundation.CHAR * 257),
        ("dwSizeofEapInfo", UInt32),
        ("pbEapInfo", Byte * 0),
    ]
    return RASEAPUSERIDENTITYA
def _define_RASEAPUSERIDENTITYW_head():
    class RASEAPUSERIDENTITYW(Structure):
        pass
    return RASEAPUSERIDENTITYW
def _define_RASEAPUSERIDENTITYW():
    RASEAPUSERIDENTITYW = win32more.NetworkManagement.Rras.RASEAPUSERIDENTITYW_head
    RASEAPUSERIDENTITYW._fields_ = [
        ("szUserName", Char * 257),
        ("dwSizeofEapInfo", UInt32),
        ("pbEapInfo", Byte * 0),
    ]
    return RASEAPUSERIDENTITYW
def _define_PFNRASGETBUFFER():
    return CFUNCTYPE(UInt32,POINTER(c_char_p_no),POINTER(UInt32), use_last_error=False)
def _define_PFNRASFREEBUFFER():
    return CFUNCTYPE(UInt32,c_char_p_no, use_last_error=False)
def _define_PFNRASSENDBUFFER():
    return CFUNCTYPE(UInt32,win32more.Foundation.HANDLE,c_char_p_no,UInt32, use_last_error=False)
def _define_PFNRASRECEIVEBUFFER():
    return CFUNCTYPE(UInt32,win32more.Foundation.HANDLE,c_char_p_no,POINTER(UInt32),UInt32,win32more.Foundation.HANDLE, use_last_error=False)
def _define_PFNRASRETRIEVEBUFFER():
    return CFUNCTYPE(UInt32,win32more.Foundation.HANDLE,c_char_p_no,POINTER(UInt32), use_last_error=False)
def _define_RasCustomScriptExecuteFn():
    return CFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.NetworkManagement.Rras.PFNRASGETBUFFER,win32more.NetworkManagement.Rras.PFNRASFREEBUFFER,win32more.NetworkManagement.Rras.PFNRASSENDBUFFER,win32more.NetworkManagement.Rras.PFNRASRECEIVEBUFFER,win32more.NetworkManagement.Rras.PFNRASRETRIEVEBUFFER,win32more.Foundation.HWND,POINTER(win32more.NetworkManagement.Rras.RASDIALPARAMSA_head),c_void_p, use_last_error=False)
def _define_RASCOMMSETTINGS_head():
    class RASCOMMSETTINGS(Structure):
        pass
    return RASCOMMSETTINGS
def _define_RASCOMMSETTINGS():
    RASCOMMSETTINGS = win32more.NetworkManagement.Rras.RASCOMMSETTINGS_head
    RASCOMMSETTINGS._fields_ = [
        ("dwSize", UInt32),
        ("bParity", Byte),
        ("bStop", Byte),
        ("bByteSize", Byte),
        ("bAlign", Byte),
    ]
    return RASCOMMSETTINGS
def _define_PFNRASSETCOMMSETTINGS():
    return CFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(win32more.NetworkManagement.Rras.RASCOMMSETTINGS_head),c_void_p, use_last_error=False)
def _define_RASCUSTOMSCRIPTEXTENSIONS_head():
    class RASCUSTOMSCRIPTEXTENSIONS(Structure):
        pass
    return RASCUSTOMSCRIPTEXTENSIONS
def _define_RASCUSTOMSCRIPTEXTENSIONS():
    RASCUSTOMSCRIPTEXTENSIONS = win32more.NetworkManagement.Rras.RASCUSTOMSCRIPTEXTENSIONS_head
    RASCUSTOMSCRIPTEXTENSIONS._pack_ = 4
    RASCUSTOMSCRIPTEXTENSIONS._fields_ = [
        ("dwSize", UInt32),
        ("pfnRasSetCommSettings", win32more.NetworkManagement.Rras.PFNRASSETCOMMSETTINGS),
    ]
    return RASCUSTOMSCRIPTEXTENSIONS
def _define_RAS_STATS_head():
    class RAS_STATS(Structure):
        pass
    return RAS_STATS
def _define_RAS_STATS():
    RAS_STATS = win32more.NetworkManagement.Rras.RAS_STATS_head
    RAS_STATS._fields_ = [
        ("dwSize", UInt32),
        ("dwBytesXmited", UInt32),
        ("dwBytesRcved", UInt32),
        ("dwFramesXmited", UInt32),
        ("dwFramesRcved", UInt32),
        ("dwCrcErr", UInt32),
        ("dwTimeoutErr", UInt32),
        ("dwAlignmentErr", UInt32),
        ("dwHardwareOverrunErr", UInt32),
        ("dwFramingErr", UInt32),
        ("dwBufferOverrunErr", UInt32),
        ("dwCompressionRatioIn", UInt32),
        ("dwCompressionRatioOut", UInt32),
        ("dwBps", UInt32),
        ("dwConnectDuration", UInt32),
    ]
    return RAS_STATS
def _define_RasCustomHangUpFn():
    return CFUNCTYPE(UInt32,win32more.NetworkManagement.Rras.HRASCONN, use_last_error=False)
def _define_RasCustomDialFn():
    return CFUNCTYPE(UInt32,win32more.Foundation.HINSTANCE,POINTER(win32more.NetworkManagement.Rras.RASDIALEXTENSIONS_head),win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Rras.RASDIALPARAMSA_head),UInt32,c_void_p,POINTER(win32more.NetworkManagement.Rras.HRASCONN),UInt32, use_last_error=False)
def _define_RasCustomDeleteEntryNotifyFn():
    return CFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32, use_last_error=False)
def _define_RASUPDATECONN_head():
    class RASUPDATECONN(Structure):
        pass
    return RASUPDATECONN
def _define_RASUPDATECONN():
    RASUPDATECONN = win32more.NetworkManagement.Rras.RASUPDATECONN_head
    RASUPDATECONN._fields_ = [
        ("version", win32more.NetworkManagement.Rras.RASAPIVERSION),
        ("dwSize", UInt32),
        ("dwFlags", UInt32),
        ("dwIfIndex", UInt32),
        ("localEndPoint", win32more.NetworkManagement.Rras.RASTUNNELENDPOINT),
        ("remoteEndPoint", win32more.NetworkManagement.Rras.RASTUNNELENDPOINT),
    ]
    return RASUPDATECONN
def _define_RASPBDLGFUNCW():
    return CFUNCTYPE(Void,UIntPtr,UInt32,win32more.Foundation.PWSTR,c_void_p, use_last_error=False)
def _define_RASPBDLGFUNCA():
    return CFUNCTYPE(Void,UIntPtr,UInt32,win32more.Foundation.PSTR,c_void_p, use_last_error=False)
def _define_RASNOUSERW_head():
    class RASNOUSERW(Structure):
        pass
    return RASNOUSERW
def _define_RASNOUSERW():
    RASNOUSERW = win32more.NetworkManagement.Rras.RASNOUSERW_head
    RASNOUSERW._fields_ = [
        ("dwSize", UInt32),
        ("dwFlags", UInt32),
        ("dwTimeoutMs", UInt32),
        ("szUserName", Char * 257),
        ("szPassword", Char * 257),
        ("szDomain", Char * 16),
    ]
    return RASNOUSERW
def _define_RASNOUSERA_head():
    class RASNOUSERA(Structure):
        pass
    return RASNOUSERA
def _define_RASNOUSERA():
    RASNOUSERA = win32more.NetworkManagement.Rras.RASNOUSERA_head
    RASNOUSERA._fields_ = [
        ("dwSize", UInt32),
        ("dwFlags", UInt32),
        ("dwTimeoutMs", UInt32),
        ("szUserName", win32more.Foundation.CHAR * 257),
        ("szPassword", win32more.Foundation.CHAR * 257),
        ("szDomain", win32more.Foundation.CHAR * 16),
    ]
    return RASNOUSERA
def _define_RASPBDLGW_head():
    class RASPBDLGW(Structure):
        pass
    return RASPBDLGW
def _define_RASPBDLGW():
    RASPBDLGW = win32more.NetworkManagement.Rras.RASPBDLGW_head
    RASPBDLGW._pack_ = 4
    RASPBDLGW._fields_ = [
        ("dwSize", UInt32),
        ("hwndOwner", win32more.Foundation.HWND),
        ("dwFlags", UInt32),
        ("xDlg", Int32),
        ("yDlg", Int32),
        ("dwCallbackId", UIntPtr),
        ("pCallback", win32more.NetworkManagement.Rras.RASPBDLGFUNCW),
        ("dwError", UInt32),
        ("reserved", UIntPtr),
        ("reserved2", UIntPtr),
    ]
    return RASPBDLGW
def _define_RASPBDLGA_head():
    class RASPBDLGA(Structure):
        pass
    return RASPBDLGA
def _define_RASPBDLGA():
    RASPBDLGA = win32more.NetworkManagement.Rras.RASPBDLGA_head
    RASPBDLGA._pack_ = 4
    RASPBDLGA._fields_ = [
        ("dwSize", UInt32),
        ("hwndOwner", win32more.Foundation.HWND),
        ("dwFlags", UInt32),
        ("xDlg", Int32),
        ("yDlg", Int32),
        ("dwCallbackId", UIntPtr),
        ("pCallback", win32more.NetworkManagement.Rras.RASPBDLGFUNCA),
        ("dwError", UInt32),
        ("reserved", UIntPtr),
        ("reserved2", UIntPtr),
    ]
    return RASPBDLGA
def _define_RASENTRYDLGW_head():
    class RASENTRYDLGW(Structure):
        pass
    return RASENTRYDLGW
def _define_RASENTRYDLGW():
    RASENTRYDLGW = win32more.NetworkManagement.Rras.RASENTRYDLGW_head
    RASENTRYDLGW._pack_ = 4
    RASENTRYDLGW._fields_ = [
        ("dwSize", UInt32),
        ("hwndOwner", win32more.Foundation.HWND),
        ("dwFlags", UInt32),
        ("xDlg", Int32),
        ("yDlg", Int32),
        ("szEntry", Char * 257),
        ("dwError", UInt32),
        ("reserved", UIntPtr),
        ("reserved2", UIntPtr),
    ]
    return RASENTRYDLGW
def _define_RASENTRYDLGA_head():
    class RASENTRYDLGA(Structure):
        pass
    return RASENTRYDLGA
def _define_RASENTRYDLGA():
    RASENTRYDLGA = win32more.NetworkManagement.Rras.RASENTRYDLGA_head
    RASENTRYDLGA._pack_ = 4
    RASENTRYDLGA._fields_ = [
        ("dwSize", UInt32),
        ("hwndOwner", win32more.Foundation.HWND),
        ("dwFlags", UInt32),
        ("xDlg", Int32),
        ("yDlg", Int32),
        ("szEntry", win32more.Foundation.CHAR * 257),
        ("dwError", UInt32),
        ("reserved", UIntPtr),
        ("reserved2", UIntPtr),
    ]
    return RASENTRYDLGA
def _define_RASDIALDLG_head():
    class RASDIALDLG(Structure):
        pass
    return RASDIALDLG
def _define_RASDIALDLG():
    RASDIALDLG = win32more.NetworkManagement.Rras.RASDIALDLG_head
    RASDIALDLG._pack_ = 4
    RASDIALDLG._fields_ = [
        ("dwSize", UInt32),
        ("hwndOwner", win32more.Foundation.HWND),
        ("dwFlags", UInt32),
        ("xDlg", Int32),
        ("yDlg", Int32),
        ("dwSubEntry", UInt32),
        ("dwError", UInt32),
        ("reserved", UIntPtr),
        ("reserved2", UIntPtr),
    ]
    return RASDIALDLG
def _define_RasCustomDialDlgFn():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HINSTANCE,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Rras.RASDIALDLG_head),c_void_p, use_last_error=False)
def _define_RasCustomEntryDlgFn():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HINSTANCE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Rras.RASENTRYDLGA_head),UInt32, use_last_error=False)
ROUTER_INTERFACE_TYPE = Int32
ROUTER_IF_TYPE_CLIENT = 0
ROUTER_IF_TYPE_HOME_ROUTER = 1
ROUTER_IF_TYPE_FULL_ROUTER = 2
ROUTER_IF_TYPE_DEDICATED = 3
ROUTER_IF_TYPE_INTERNAL = 4
ROUTER_IF_TYPE_LOOPBACK = 5
ROUTER_IF_TYPE_TUNNEL1 = 6
ROUTER_IF_TYPE_DIALOUT = 7
ROUTER_IF_TYPE_MAX = 8
ROUTER_CONNECTION_STATE = Int32
ROUTER_IF_STATE_UNREACHABLE = 0
ROUTER_IF_STATE_DISCONNECTED = 1
ROUTER_IF_STATE_CONNECTING = 2
ROUTER_IF_STATE_CONNECTED = 3
def _define_MPR_INTERFACE_0_head():
    class MPR_INTERFACE_0(Structure):
        pass
    return MPR_INTERFACE_0
def _define_MPR_INTERFACE_0():
    MPR_INTERFACE_0 = win32more.NetworkManagement.Rras.MPR_INTERFACE_0_head
    MPR_INTERFACE_0._fields_ = [
        ("wszInterfaceName", Char * 257),
        ("hInterface", win32more.Foundation.HANDLE),
        ("fEnabled", win32more.Foundation.BOOL),
        ("dwIfType", win32more.NetworkManagement.Rras.ROUTER_INTERFACE_TYPE),
        ("dwConnectionState", win32more.NetworkManagement.Rras.ROUTER_CONNECTION_STATE),
        ("fUnReachabilityReasons", UInt32),
        ("dwLastError", UInt32),
    ]
    return MPR_INTERFACE_0
def _define_MPR_IPINIP_INTERFACE_0_head():
    class MPR_IPINIP_INTERFACE_0(Structure):
        pass
    return MPR_IPINIP_INTERFACE_0
def _define_MPR_IPINIP_INTERFACE_0():
    MPR_IPINIP_INTERFACE_0 = win32more.NetworkManagement.Rras.MPR_IPINIP_INTERFACE_0_head
    MPR_IPINIP_INTERFACE_0._fields_ = [
        ("wszFriendlyName", Char * 257),
        ("Guid", Guid),
    ]
    return MPR_IPINIP_INTERFACE_0
def _define_MPR_INTERFACE_1_head():
    class MPR_INTERFACE_1(Structure):
        pass
    return MPR_INTERFACE_1
def _define_MPR_INTERFACE_1():
    MPR_INTERFACE_1 = win32more.NetworkManagement.Rras.MPR_INTERFACE_1_head
    MPR_INTERFACE_1._fields_ = [
        ("wszInterfaceName", Char * 257),
        ("hInterface", win32more.Foundation.HANDLE),
        ("fEnabled", win32more.Foundation.BOOL),
        ("dwIfType", win32more.NetworkManagement.Rras.ROUTER_INTERFACE_TYPE),
        ("dwConnectionState", win32more.NetworkManagement.Rras.ROUTER_CONNECTION_STATE),
        ("fUnReachabilityReasons", UInt32),
        ("dwLastError", UInt32),
        ("lpwsDialoutHoursRestriction", win32more.Foundation.PWSTR),
    ]
    return MPR_INTERFACE_1
def _define_MPR_INTERFACE_2_head():
    class MPR_INTERFACE_2(Structure):
        pass
    return MPR_INTERFACE_2
def _define_MPR_INTERFACE_2():
    MPR_INTERFACE_2 = win32more.NetworkManagement.Rras.MPR_INTERFACE_2_head
    MPR_INTERFACE_2._fields_ = [
        ("wszInterfaceName", Char * 257),
        ("hInterface", win32more.Foundation.HANDLE),
        ("fEnabled", win32more.Foundation.BOOL),
        ("dwIfType", win32more.NetworkManagement.Rras.ROUTER_INTERFACE_TYPE),
        ("dwConnectionState", win32more.NetworkManagement.Rras.ROUTER_CONNECTION_STATE),
        ("fUnReachabilityReasons", UInt32),
        ("dwLastError", UInt32),
        ("dwfOptions", UInt32),
        ("szLocalPhoneNumber", Char * 129),
        ("szAlternates", win32more.Foundation.PWSTR),
        ("ipaddr", UInt32),
        ("ipaddrDns", UInt32),
        ("ipaddrDnsAlt", UInt32),
        ("ipaddrWins", UInt32),
        ("ipaddrWinsAlt", UInt32),
        ("dwfNetProtocols", UInt32),
        ("szDeviceType", Char * 17),
        ("szDeviceName", Char * 129),
        ("szX25PadType", Char * 33),
        ("szX25Address", Char * 201),
        ("szX25Facilities", Char * 201),
        ("szX25UserData", Char * 201),
        ("dwChannels", UInt32),
        ("dwSubEntries", UInt32),
        ("dwDialMode", win32more.NetworkManagement.Rras.MPR_INTERFACE_DIAL_MODE),
        ("dwDialExtraPercent", UInt32),
        ("dwDialExtraSampleSeconds", UInt32),
        ("dwHangUpExtraPercent", UInt32),
        ("dwHangUpExtraSampleSeconds", UInt32),
        ("dwIdleDisconnectSeconds", UInt32),
        ("dwType", UInt32),
        ("dwEncryptionType", win32more.NetworkManagement.Rras.MPR_ET),
        ("dwCustomAuthKey", UInt32),
        ("dwCustomAuthDataSize", UInt32),
        ("lpbCustomAuthData", c_char_p_no),
        ("guidId", Guid),
        ("dwVpnStrategy", win32more.NetworkManagement.Rras.MPR_VS),
    ]
    return MPR_INTERFACE_2
def _define_MPR_INTERFACE_3_head():
    class MPR_INTERFACE_3(Structure):
        pass
    return MPR_INTERFACE_3
def _define_MPR_INTERFACE_3():
    MPR_INTERFACE_3 = win32more.NetworkManagement.Rras.MPR_INTERFACE_3_head
    MPR_INTERFACE_3._fields_ = [
        ("wszInterfaceName", Char * 257),
        ("hInterface", win32more.Foundation.HANDLE),
        ("fEnabled", win32more.Foundation.BOOL),
        ("dwIfType", win32more.NetworkManagement.Rras.ROUTER_INTERFACE_TYPE),
        ("dwConnectionState", win32more.NetworkManagement.Rras.ROUTER_CONNECTION_STATE),
        ("fUnReachabilityReasons", UInt32),
        ("dwLastError", UInt32),
        ("dwfOptions", UInt32),
        ("szLocalPhoneNumber", Char * 129),
        ("szAlternates", win32more.Foundation.PWSTR),
        ("ipaddr", UInt32),
        ("ipaddrDns", UInt32),
        ("ipaddrDnsAlt", UInt32),
        ("ipaddrWins", UInt32),
        ("ipaddrWinsAlt", UInt32),
        ("dwfNetProtocols", UInt32),
        ("szDeviceType", Char * 17),
        ("szDeviceName", Char * 129),
        ("szX25PadType", Char * 33),
        ("szX25Address", Char * 201),
        ("szX25Facilities", Char * 201),
        ("szX25UserData", Char * 201),
        ("dwChannels", UInt32),
        ("dwSubEntries", UInt32),
        ("dwDialMode", win32more.NetworkManagement.Rras.MPR_INTERFACE_DIAL_MODE),
        ("dwDialExtraPercent", UInt32),
        ("dwDialExtraSampleSeconds", UInt32),
        ("dwHangUpExtraPercent", UInt32),
        ("dwHangUpExtraSampleSeconds", UInt32),
        ("dwIdleDisconnectSeconds", UInt32),
        ("dwType", UInt32),
        ("dwEncryptionType", win32more.NetworkManagement.Rras.MPR_ET),
        ("dwCustomAuthKey", UInt32),
        ("dwCustomAuthDataSize", UInt32),
        ("lpbCustomAuthData", c_char_p_no),
        ("guidId", Guid),
        ("dwVpnStrategy", win32more.NetworkManagement.Rras.MPR_VS),
        ("AddressCount", UInt32),
        ("ipv6addrDns", win32more.Networking.WinSock.IN6_ADDR),
        ("ipv6addrDnsAlt", win32more.Networking.WinSock.IN6_ADDR),
        ("ipv6addr", POINTER(win32more.Networking.WinSock.IN6_ADDR_head)),
    ]
    return MPR_INTERFACE_3
def _define_MPR_DEVICE_0_head():
    class MPR_DEVICE_0(Structure):
        pass
    return MPR_DEVICE_0
def _define_MPR_DEVICE_0():
    MPR_DEVICE_0 = win32more.NetworkManagement.Rras.MPR_DEVICE_0_head
    MPR_DEVICE_0._fields_ = [
        ("szDeviceType", Char * 17),
        ("szDeviceName", Char * 129),
    ]
    return MPR_DEVICE_0
def _define_MPR_DEVICE_1_head():
    class MPR_DEVICE_1(Structure):
        pass
    return MPR_DEVICE_1
def _define_MPR_DEVICE_1():
    MPR_DEVICE_1 = win32more.NetworkManagement.Rras.MPR_DEVICE_1_head
    MPR_DEVICE_1._fields_ = [
        ("szDeviceType", Char * 17),
        ("szDeviceName", Char * 129),
        ("szLocalPhoneNumber", Char * 129),
        ("szAlternates", win32more.Foundation.PWSTR),
    ]
    return MPR_DEVICE_1
def _define_MPR_CREDENTIALSEX_0_head():
    class MPR_CREDENTIALSEX_0(Structure):
        pass
    return MPR_CREDENTIALSEX_0
def _define_MPR_CREDENTIALSEX_0():
    MPR_CREDENTIALSEX_0 = win32more.NetworkManagement.Rras.MPR_CREDENTIALSEX_0_head
    MPR_CREDENTIALSEX_0._fields_ = [
        ("dwSize", UInt32),
        ("lpbCredentialsInfo", c_char_p_no),
    ]
    return MPR_CREDENTIALSEX_0
def _define_MPR_CREDENTIALSEX_1_head():
    class MPR_CREDENTIALSEX_1(Structure):
        pass
    return MPR_CREDENTIALSEX_1
def _define_MPR_CREDENTIALSEX_1():
    MPR_CREDENTIALSEX_1 = win32more.NetworkManagement.Rras.MPR_CREDENTIALSEX_1_head
    MPR_CREDENTIALSEX_1._fields_ = [
        ("dwSize", UInt32),
        ("lpbCredentialsInfo", c_char_p_no),
    ]
    return MPR_CREDENTIALSEX_1
def _define_MPR_TRANSPORT_0_head():
    class MPR_TRANSPORT_0(Structure):
        pass
    return MPR_TRANSPORT_0
def _define_MPR_TRANSPORT_0():
    MPR_TRANSPORT_0 = win32more.NetworkManagement.Rras.MPR_TRANSPORT_0_head
    MPR_TRANSPORT_0._fields_ = [
        ("dwTransportId", UInt32),
        ("hTransport", win32more.Foundation.HANDLE),
        ("wszTransportName", Char * 41),
    ]
    return MPR_TRANSPORT_0
def _define_MPR_IFTRANSPORT_0_head():
    class MPR_IFTRANSPORT_0(Structure):
        pass
    return MPR_IFTRANSPORT_0
def _define_MPR_IFTRANSPORT_0():
    MPR_IFTRANSPORT_0 = win32more.NetworkManagement.Rras.MPR_IFTRANSPORT_0_head
    MPR_IFTRANSPORT_0._fields_ = [
        ("dwTransportId", UInt32),
        ("hIfTransport", win32more.Foundation.HANDLE),
        ("wszIfTransportName", Char * 41),
    ]
    return MPR_IFTRANSPORT_0
def _define_MPR_SERVER_0_head():
    class MPR_SERVER_0(Structure):
        pass
    return MPR_SERVER_0
def _define_MPR_SERVER_0():
    MPR_SERVER_0 = win32more.NetworkManagement.Rras.MPR_SERVER_0_head
    MPR_SERVER_0._fields_ = [
        ("fLanOnlyMode", win32more.Foundation.BOOL),
        ("dwUpTime", UInt32),
        ("dwTotalPorts", UInt32),
        ("dwPortsInUse", UInt32),
    ]
    return MPR_SERVER_0
def _define_MPR_SERVER_1_head():
    class MPR_SERVER_1(Structure):
        pass
    return MPR_SERVER_1
def _define_MPR_SERVER_1():
    MPR_SERVER_1 = win32more.NetworkManagement.Rras.MPR_SERVER_1_head
    MPR_SERVER_1._fields_ = [
        ("dwNumPptpPorts", UInt32),
        ("dwPptpPortFlags", UInt32),
        ("dwNumL2tpPorts", UInt32),
        ("dwL2tpPortFlags", UInt32),
    ]
    return MPR_SERVER_1
def _define_MPR_SERVER_2_head():
    class MPR_SERVER_2(Structure):
        pass
    return MPR_SERVER_2
def _define_MPR_SERVER_2():
    MPR_SERVER_2 = win32more.NetworkManagement.Rras.MPR_SERVER_2_head
    MPR_SERVER_2._fields_ = [
        ("dwNumPptpPorts", UInt32),
        ("dwPptpPortFlags", UInt32),
        ("dwNumL2tpPorts", UInt32),
        ("dwL2tpPortFlags", UInt32),
        ("dwNumSstpPorts", UInt32),
        ("dwSstpPortFlags", UInt32),
    ]
    return MPR_SERVER_2
RAS_PORT_CONDITION = Int32
RAS_PORT_NON_OPERATIONAL = 0
RAS_PORT_DISCONNECTED = 1
RAS_PORT_CALLING_BACK = 2
RAS_PORT_LISTENING = 3
RAS_PORT_AUTHENTICATING = 4
RAS_PORT_AUTHENTICATED = 5
RAS_PORT_INITIALIZING = 6
RAS_HARDWARE_CONDITION = Int32
RAS_HARDWARE_OPERATIONAL = 0
RAS_HARDWARE_FAILURE = 1
def _define_RAS_PORT_0_head():
    class RAS_PORT_0(Structure):
        pass
    return RAS_PORT_0
def _define_RAS_PORT_0():
    RAS_PORT_0 = win32more.NetworkManagement.Rras.RAS_PORT_0_head
    RAS_PORT_0._fields_ = [
        ("hPort", win32more.Foundation.HANDLE),
        ("hConnection", win32more.Foundation.HANDLE),
        ("dwPortCondition", win32more.NetworkManagement.Rras.RAS_PORT_CONDITION),
        ("dwTotalNumberOfCalls", UInt32),
        ("dwConnectDuration", UInt32),
        ("wszPortName", Char * 17),
        ("wszMediaName", Char * 17),
        ("wszDeviceName", Char * 129),
        ("wszDeviceType", Char * 17),
    ]
    return RAS_PORT_0
def _define_RAS_PORT_1_head():
    class RAS_PORT_1(Structure):
        pass
    return RAS_PORT_1
def _define_RAS_PORT_1():
    RAS_PORT_1 = win32more.NetworkManagement.Rras.RAS_PORT_1_head
    RAS_PORT_1._fields_ = [
        ("hPort", win32more.Foundation.HANDLE),
        ("hConnection", win32more.Foundation.HANDLE),
        ("dwHardwareCondition", win32more.NetworkManagement.Rras.RAS_HARDWARE_CONDITION),
        ("dwLineSpeed", UInt32),
        ("dwBytesXmited", UInt32),
        ("dwBytesRcved", UInt32),
        ("dwFramesXmited", UInt32),
        ("dwFramesRcved", UInt32),
        ("dwCrcErr", UInt32),
        ("dwTimeoutErr", UInt32),
        ("dwAlignmentErr", UInt32),
        ("dwHardwareOverrunErr", UInt32),
        ("dwFramingErr", UInt32),
        ("dwBufferOverrunErr", UInt32),
        ("dwCompressionRatioIn", UInt32),
        ("dwCompressionRatioOut", UInt32),
    ]
    return RAS_PORT_1
def _define_RAS_PORT_2_head():
    class RAS_PORT_2(Structure):
        pass
    return RAS_PORT_2
def _define_RAS_PORT_2():
    RAS_PORT_2 = win32more.NetworkManagement.Rras.RAS_PORT_2_head
    RAS_PORT_2._fields_ = [
        ("hPort", win32more.Foundation.HANDLE),
        ("hConnection", win32more.Foundation.HANDLE),
        ("dwConn_State", UInt32),
        ("wszPortName", Char * 17),
        ("wszMediaName", Char * 17),
        ("wszDeviceName", Char * 129),
        ("wszDeviceType", Char * 17),
        ("dwHardwareCondition", win32more.NetworkManagement.Rras.RAS_HARDWARE_CONDITION),
        ("dwLineSpeed", UInt32),
        ("dwCrcErr", UInt32),
        ("dwSerialOverRunErrs", UInt32),
        ("dwTimeoutErr", UInt32),
        ("dwAlignmentErr", UInt32),
        ("dwHardwareOverrunErr", UInt32),
        ("dwFramingErr", UInt32),
        ("dwBufferOverrunErr", UInt32),
        ("dwCompressionRatioIn", UInt32),
        ("dwCompressionRatioOut", UInt32),
        ("dwTotalErrors", UInt32),
        ("ullBytesXmited", UInt64),
        ("ullBytesRcved", UInt64),
        ("ullFramesXmited", UInt64),
        ("ullFramesRcved", UInt64),
        ("ullBytesTxUncompressed", UInt64),
        ("ullBytesTxCompressed", UInt64),
        ("ullBytesRcvUncompressed", UInt64),
        ("ullBytesRcvCompressed", UInt64),
    ]
    return RAS_PORT_2
def _define_PPP_NBFCP_INFO_head():
    class PPP_NBFCP_INFO(Structure):
        pass
    return PPP_NBFCP_INFO
def _define_PPP_NBFCP_INFO():
    PPP_NBFCP_INFO = win32more.NetworkManagement.Rras.PPP_NBFCP_INFO_head
    PPP_NBFCP_INFO._fields_ = [
        ("dwError", UInt32),
        ("wszWksta", Char * 17),
    ]
    return PPP_NBFCP_INFO
def _define_PPP_IPCP_INFO_head():
    class PPP_IPCP_INFO(Structure):
        pass
    return PPP_IPCP_INFO
def _define_PPP_IPCP_INFO():
    PPP_IPCP_INFO = win32more.NetworkManagement.Rras.PPP_IPCP_INFO_head
    PPP_IPCP_INFO._fields_ = [
        ("dwError", UInt32),
        ("wszAddress", Char * 16),
        ("wszRemoteAddress", Char * 16),
    ]
    return PPP_IPCP_INFO
def _define_PPP_IPCP_INFO2_head():
    class PPP_IPCP_INFO2(Structure):
        pass
    return PPP_IPCP_INFO2
def _define_PPP_IPCP_INFO2():
    PPP_IPCP_INFO2 = win32more.NetworkManagement.Rras.PPP_IPCP_INFO2_head
    PPP_IPCP_INFO2._fields_ = [
        ("dwError", UInt32),
        ("wszAddress", Char * 16),
        ("wszRemoteAddress", Char * 16),
        ("dwOptions", UInt32),
        ("dwRemoteOptions", UInt32),
    ]
    return PPP_IPCP_INFO2
def _define_PPP_IPXCP_INFO_head():
    class PPP_IPXCP_INFO(Structure):
        pass
    return PPP_IPXCP_INFO
def _define_PPP_IPXCP_INFO():
    PPP_IPXCP_INFO = win32more.NetworkManagement.Rras.PPP_IPXCP_INFO_head
    PPP_IPXCP_INFO._fields_ = [
        ("dwError", UInt32),
        ("wszAddress", Char * 23),
    ]
    return PPP_IPXCP_INFO
def _define_PPP_ATCP_INFO_head():
    class PPP_ATCP_INFO(Structure):
        pass
    return PPP_ATCP_INFO
def _define_PPP_ATCP_INFO():
    PPP_ATCP_INFO = win32more.NetworkManagement.Rras.PPP_ATCP_INFO_head
    PPP_ATCP_INFO._fields_ = [
        ("dwError", UInt32),
        ("wszAddress", Char * 33),
    ]
    return PPP_ATCP_INFO
def _define_PPP_IPV6_CP_INFO_head():
    class PPP_IPV6_CP_INFO(Structure):
        pass
    return PPP_IPV6_CP_INFO
def _define_PPP_IPV6_CP_INFO():
    PPP_IPV6_CP_INFO = win32more.NetworkManagement.Rras.PPP_IPV6_CP_INFO_head
    PPP_IPV6_CP_INFO._fields_ = [
        ("dwVersion", UInt32),
        ("dwSize", UInt32),
        ("dwError", UInt32),
        ("bInterfaceIdentifier", Byte * 8),
        ("bRemoteInterfaceIdentifier", Byte * 8),
        ("dwOptions", UInt32),
        ("dwRemoteOptions", UInt32),
        ("bPrefix", Byte * 8),
        ("dwPrefixLength", UInt32),
    ]
    return PPP_IPV6_CP_INFO
def _define_PPP_INFO_head():
    class PPP_INFO(Structure):
        pass
    return PPP_INFO
def _define_PPP_INFO():
    PPP_INFO = win32more.NetworkManagement.Rras.PPP_INFO_head
    PPP_INFO._fields_ = [
        ("nbf", win32more.NetworkManagement.Rras.PPP_NBFCP_INFO),
        ("ip", win32more.NetworkManagement.Rras.PPP_IPCP_INFO),
        ("ipx", win32more.NetworkManagement.Rras.PPP_IPXCP_INFO),
        ("at", win32more.NetworkManagement.Rras.PPP_ATCP_INFO),
    ]
    return PPP_INFO
def _define_PPP_CCP_INFO_head():
    class PPP_CCP_INFO(Structure):
        pass
    return PPP_CCP_INFO
def _define_PPP_CCP_INFO():
    PPP_CCP_INFO = win32more.NetworkManagement.Rras.PPP_CCP_INFO_head
    PPP_CCP_INFO._fields_ = [
        ("dwError", UInt32),
        ("dwCompressionAlgorithm", UInt32),
        ("dwOptions", UInt32),
        ("dwRemoteCompressionAlgorithm", UInt32),
        ("dwRemoteOptions", UInt32),
    ]
    return PPP_CCP_INFO
def _define_PPP_LCP_INFO_head():
    class PPP_LCP_INFO(Structure):
        pass
    return PPP_LCP_INFO
def _define_PPP_LCP_INFO():
    PPP_LCP_INFO = win32more.NetworkManagement.Rras.PPP_LCP_INFO_head
    PPP_LCP_INFO._fields_ = [
        ("dwError", UInt32),
        ("dwAuthenticationProtocol", win32more.NetworkManagement.Rras.PPP_LCP),
        ("dwAuthenticationData", win32more.NetworkManagement.Rras.PPP_LCP_INFO_AUTH_DATA),
        ("dwRemoteAuthenticationProtocol", UInt32),
        ("dwRemoteAuthenticationData", UInt32),
        ("dwTerminateReason", UInt32),
        ("dwRemoteTerminateReason", UInt32),
        ("dwOptions", UInt32),
        ("dwRemoteOptions", UInt32),
        ("dwEapTypeId", UInt32),
        ("dwRemoteEapTypeId", UInt32),
    ]
    return PPP_LCP_INFO
def _define_PPP_INFO_2_head():
    class PPP_INFO_2(Structure):
        pass
    return PPP_INFO_2
def _define_PPP_INFO_2():
    PPP_INFO_2 = win32more.NetworkManagement.Rras.PPP_INFO_2_head
    PPP_INFO_2._fields_ = [
        ("nbf", win32more.NetworkManagement.Rras.PPP_NBFCP_INFO),
        ("ip", win32more.NetworkManagement.Rras.PPP_IPCP_INFO2),
        ("ipx", win32more.NetworkManagement.Rras.PPP_IPXCP_INFO),
        ("at", win32more.NetworkManagement.Rras.PPP_ATCP_INFO),
        ("ccp", win32more.NetworkManagement.Rras.PPP_CCP_INFO),
        ("lcp", win32more.NetworkManagement.Rras.PPP_LCP_INFO),
    ]
    return PPP_INFO_2
def _define_PPP_INFO_3_head():
    class PPP_INFO_3(Structure):
        pass
    return PPP_INFO_3
def _define_PPP_INFO_3():
    PPP_INFO_3 = win32more.NetworkManagement.Rras.PPP_INFO_3_head
    PPP_INFO_3._fields_ = [
        ("nbf", win32more.NetworkManagement.Rras.PPP_NBFCP_INFO),
        ("ip", win32more.NetworkManagement.Rras.PPP_IPCP_INFO2),
        ("ipv6", win32more.NetworkManagement.Rras.PPP_IPV6_CP_INFO),
        ("ccp", win32more.NetworkManagement.Rras.PPP_CCP_INFO),
        ("lcp", win32more.NetworkManagement.Rras.PPP_LCP_INFO),
    ]
    return PPP_INFO_3
def _define_RAS_CONNECTION_0_head():
    class RAS_CONNECTION_0(Structure):
        pass
    return RAS_CONNECTION_0
def _define_RAS_CONNECTION_0():
    RAS_CONNECTION_0 = win32more.NetworkManagement.Rras.RAS_CONNECTION_0_head
    RAS_CONNECTION_0._fields_ = [
        ("hConnection", win32more.Foundation.HANDLE),
        ("hInterface", win32more.Foundation.HANDLE),
        ("dwConnectDuration", UInt32),
        ("dwInterfaceType", win32more.NetworkManagement.Rras.ROUTER_INTERFACE_TYPE),
        ("dwConnectionFlags", win32more.NetworkManagement.Rras.RAS_FLAGS),
        ("wszInterfaceName", Char * 257),
        ("wszUserName", Char * 257),
        ("wszLogonDomain", Char * 16),
        ("wszRemoteComputer", Char * 17),
    ]
    return RAS_CONNECTION_0
def _define_RAS_CONNECTION_1_head():
    class RAS_CONNECTION_1(Structure):
        pass
    return RAS_CONNECTION_1
def _define_RAS_CONNECTION_1():
    RAS_CONNECTION_1 = win32more.NetworkManagement.Rras.RAS_CONNECTION_1_head
    RAS_CONNECTION_1._fields_ = [
        ("hConnection", win32more.Foundation.HANDLE),
        ("hInterface", win32more.Foundation.HANDLE),
        ("PppInfo", win32more.NetworkManagement.Rras.PPP_INFO),
        ("dwBytesXmited", UInt32),
        ("dwBytesRcved", UInt32),
        ("dwFramesXmited", UInt32),
        ("dwFramesRcved", UInt32),
        ("dwCrcErr", UInt32),
        ("dwTimeoutErr", UInt32),
        ("dwAlignmentErr", UInt32),
        ("dwHardwareOverrunErr", UInt32),
        ("dwFramingErr", UInt32),
        ("dwBufferOverrunErr", UInt32),
        ("dwCompressionRatioIn", UInt32),
        ("dwCompressionRatioOut", UInt32),
    ]
    return RAS_CONNECTION_1
def _define_RAS_CONNECTION_2_head():
    class RAS_CONNECTION_2(Structure):
        pass
    return RAS_CONNECTION_2
def _define_RAS_CONNECTION_2():
    RAS_CONNECTION_2 = win32more.NetworkManagement.Rras.RAS_CONNECTION_2_head
    RAS_CONNECTION_2._fields_ = [
        ("hConnection", win32more.Foundation.HANDLE),
        ("wszUserName", Char * 257),
        ("dwInterfaceType", win32more.NetworkManagement.Rras.ROUTER_INTERFACE_TYPE),
        ("guid", Guid),
        ("PppInfo2", win32more.NetworkManagement.Rras.PPP_INFO_2),
    ]
    return RAS_CONNECTION_2
RAS_QUARANTINE_STATE = Int32
RAS_QUAR_STATE_NORMAL = 0
RAS_QUAR_STATE_QUARANTINE = 1
RAS_QUAR_STATE_PROBATION = 2
RAS_QUAR_STATE_NOT_CAPABLE = 3
def _define_RAS_CONNECTION_3_head():
    class RAS_CONNECTION_3(Structure):
        pass
    return RAS_CONNECTION_3
def _define_RAS_CONNECTION_3():
    RAS_CONNECTION_3 = win32more.NetworkManagement.Rras.RAS_CONNECTION_3_head
    RAS_CONNECTION_3._fields_ = [
        ("dwVersion", UInt32),
        ("dwSize", UInt32),
        ("hConnection", win32more.Foundation.HANDLE),
        ("wszUserName", Char * 257),
        ("dwInterfaceType", win32more.NetworkManagement.Rras.ROUTER_INTERFACE_TYPE),
        ("guid", Guid),
        ("PppInfo3", win32more.NetworkManagement.Rras.PPP_INFO_3),
        ("rasQuarState", win32more.NetworkManagement.Rras.RAS_QUARANTINE_STATE),
        ("timer", win32more.Foundation.FILETIME),
    ]
    return RAS_CONNECTION_3
def _define_RAS_USER_0_head():
    class RAS_USER_0(Structure):
        pass
    return RAS_USER_0
def _define_RAS_USER_0():
    RAS_USER_0 = win32more.NetworkManagement.Rras.RAS_USER_0_head
    RAS_USER_0._fields_ = [
        ("bfPrivilege", Byte),
        ("wszPhoneNumber", Char * 129),
    ]
    return RAS_USER_0
def _define_RAS_USER_1_head():
    class RAS_USER_1(Structure):
        pass
    return RAS_USER_1
def _define_RAS_USER_1():
    RAS_USER_1 = win32more.NetworkManagement.Rras.RAS_USER_1_head
    RAS_USER_1._fields_ = [
        ("bfPrivilege", Byte),
        ("wszPhoneNumber", Char * 129),
        ("bfPrivilege2", Byte),
    ]
    return RAS_USER_1
def _define_MPR_FILTER_0_head():
    class MPR_FILTER_0(Structure):
        pass
    return MPR_FILTER_0
def _define_MPR_FILTER_0():
    MPR_FILTER_0 = win32more.NetworkManagement.Rras.MPR_FILTER_0_head
    MPR_FILTER_0._fields_ = [
        ("fEnable", win32more.Foundation.BOOL),
    ]
    return MPR_FILTER_0
def _define_MPRAPI_OBJECT_HEADER_head():
    class MPRAPI_OBJECT_HEADER(Structure):
        pass
    return MPRAPI_OBJECT_HEADER
def _define_MPRAPI_OBJECT_HEADER():
    MPRAPI_OBJECT_HEADER = win32more.NetworkManagement.Rras.MPRAPI_OBJECT_HEADER_head
    MPRAPI_OBJECT_HEADER._fields_ = [
        ("revision", Byte),
        ("type", Byte),
        ("size", UInt16),
    ]
    return MPRAPI_OBJECT_HEADER
MPRAPI_OBJECT_TYPE = Int32
MPRAPI_OBJECT_TYPE_RAS_CONNECTION_OBJECT = 1
MPRAPI_OBJECT_TYPE_MPR_SERVER_OBJECT = 2
MPRAPI_OBJECT_TYPE_MPR_SERVER_SET_CONFIG_OBJECT = 3
MPRAPI_OBJECT_TYPE_AUTH_VALIDATION_OBJECT = 4
MPRAPI_OBJECT_TYPE_UPDATE_CONNECTION_OBJECT = 5
MPRAPI_OBJECT_TYPE_IF_CUSTOM_CONFIG_OBJECT = 6
def _define_PPP_PROJECTION_INFO_head():
    class PPP_PROJECTION_INFO(Structure):
        pass
    return PPP_PROJECTION_INFO
def _define_PPP_PROJECTION_INFO():
    PPP_PROJECTION_INFO = win32more.NetworkManagement.Rras.PPP_PROJECTION_INFO_head
    PPP_PROJECTION_INFO._fields_ = [
        ("dwIPv4NegotiationError", UInt32),
        ("wszAddress", Char * 16),
        ("wszRemoteAddress", Char * 16),
        ("dwIPv4Options", UInt32),
        ("dwIPv4RemoteOptions", UInt32),
        ("IPv4SubInterfaceIndex", UInt64),
        ("dwIPv6NegotiationError", UInt32),
        ("bInterfaceIdentifier", Byte * 8),
        ("bRemoteInterfaceIdentifier", Byte * 8),
        ("bPrefix", Byte * 8),
        ("dwPrefixLength", UInt32),
        ("IPv6SubInterfaceIndex", UInt64),
        ("dwLcpError", UInt32),
        ("dwAuthenticationProtocol", win32more.NetworkManagement.Rras.PPP_LCP),
        ("dwAuthenticationData", win32more.NetworkManagement.Rras.PPP_LCP_INFO_AUTH_DATA),
        ("dwRemoteAuthenticationProtocol", win32more.NetworkManagement.Rras.PPP_LCP),
        ("dwRemoteAuthenticationData", win32more.NetworkManagement.Rras.PPP_LCP_INFO_AUTH_DATA),
        ("dwLcpTerminateReason", UInt32),
        ("dwLcpRemoteTerminateReason", UInt32),
        ("dwLcpOptions", UInt32),
        ("dwLcpRemoteOptions", UInt32),
        ("dwEapTypeId", UInt32),
        ("dwRemoteEapTypeId", UInt32),
        ("dwCcpError", UInt32),
        ("dwCompressionAlgorithm", UInt32),
        ("dwCcpOptions", UInt32),
        ("dwRemoteCompressionAlgorithm", UInt32),
        ("dwCcpRemoteOptions", UInt32),
    ]
    return PPP_PROJECTION_INFO
def _define_PPP_PROJECTION_INFO2_head():
    class PPP_PROJECTION_INFO2(Structure):
        pass
    return PPP_PROJECTION_INFO2
def _define_PPP_PROJECTION_INFO2():
    PPP_PROJECTION_INFO2 = win32more.NetworkManagement.Rras.PPP_PROJECTION_INFO2_head
    PPP_PROJECTION_INFO2._fields_ = [
        ("dwIPv4NegotiationError", UInt32),
        ("wszAddress", Char * 16),
        ("wszRemoteAddress", Char * 16),
        ("dwIPv4Options", UInt32),
        ("dwIPv4RemoteOptions", UInt32),
        ("IPv4SubInterfaceIndex", UInt64),
        ("dwIPv6NegotiationError", UInt32),
        ("bInterfaceIdentifier", Byte * 8),
        ("bRemoteInterfaceIdentifier", Byte * 8),
        ("bPrefix", Byte * 8),
        ("dwPrefixLength", UInt32),
        ("IPv6SubInterfaceIndex", UInt64),
        ("dwLcpError", UInt32),
        ("dwAuthenticationProtocol", win32more.NetworkManagement.Rras.PPP_LCP),
        ("dwAuthenticationData", win32more.NetworkManagement.Rras.PPP_LCP_INFO_AUTH_DATA),
        ("dwRemoteAuthenticationProtocol", win32more.NetworkManagement.Rras.PPP_LCP),
        ("dwRemoteAuthenticationData", win32more.NetworkManagement.Rras.PPP_LCP_INFO_AUTH_DATA),
        ("dwLcpTerminateReason", UInt32),
        ("dwLcpRemoteTerminateReason", UInt32),
        ("dwLcpOptions", UInt32),
        ("dwLcpRemoteOptions", UInt32),
        ("dwEapTypeId", UInt32),
        ("dwEmbeddedEAPTypeId", UInt32),
        ("dwRemoteEapTypeId", UInt32),
        ("dwCcpError", UInt32),
        ("dwCompressionAlgorithm", UInt32),
        ("dwCcpOptions", UInt32),
        ("dwRemoteCompressionAlgorithm", UInt32),
        ("dwCcpRemoteOptions", UInt32),
    ]
    return PPP_PROJECTION_INFO2
def _define_IKEV2_PROJECTION_INFO_head():
    class IKEV2_PROJECTION_INFO(Structure):
        pass
    return IKEV2_PROJECTION_INFO
def _define_IKEV2_PROJECTION_INFO():
    IKEV2_PROJECTION_INFO = win32more.NetworkManagement.Rras.IKEV2_PROJECTION_INFO_head
    IKEV2_PROJECTION_INFO._fields_ = [
        ("dwIPv4NegotiationError", UInt32),
        ("wszAddress", Char * 16),
        ("wszRemoteAddress", Char * 16),
        ("IPv4SubInterfaceIndex", UInt64),
        ("dwIPv6NegotiationError", UInt32),
        ("bInterfaceIdentifier", Byte * 8),
        ("bRemoteInterfaceIdentifier", Byte * 8),
        ("bPrefix", Byte * 8),
        ("dwPrefixLength", UInt32),
        ("IPv6SubInterfaceIndex", UInt64),
        ("dwOptions", UInt32),
        ("dwAuthenticationProtocol", UInt32),
        ("dwEapTypeId", UInt32),
        ("dwCompressionAlgorithm", UInt32),
        ("dwEncryptionMethod", UInt32),
    ]
    return IKEV2_PROJECTION_INFO
def _define_IKEV2_PROJECTION_INFO2_head():
    class IKEV2_PROJECTION_INFO2(Structure):
        pass
    return IKEV2_PROJECTION_INFO2
def _define_IKEV2_PROJECTION_INFO2():
    IKEV2_PROJECTION_INFO2 = win32more.NetworkManagement.Rras.IKEV2_PROJECTION_INFO2_head
    IKEV2_PROJECTION_INFO2._fields_ = [
        ("dwIPv4NegotiationError", UInt32),
        ("wszAddress", Char * 16),
        ("wszRemoteAddress", Char * 16),
        ("IPv4SubInterfaceIndex", UInt64),
        ("dwIPv6NegotiationError", UInt32),
        ("bInterfaceIdentifier", Byte * 8),
        ("bRemoteInterfaceIdentifier", Byte * 8),
        ("bPrefix", Byte * 8),
        ("dwPrefixLength", UInt32),
        ("IPv6SubInterfaceIndex", UInt64),
        ("dwOptions", UInt32),
        ("dwAuthenticationProtocol", UInt32),
        ("dwEapTypeId", UInt32),
        ("dwEmbeddedEAPTypeId", UInt32),
        ("dwCompressionAlgorithm", UInt32),
        ("dwEncryptionMethod", UInt32),
    ]
    return IKEV2_PROJECTION_INFO2
def _define_PROJECTION_INFO_head():
    class PROJECTION_INFO(Structure):
        pass
    return PROJECTION_INFO
def _define_PROJECTION_INFO():
    PROJECTION_INFO = win32more.NetworkManagement.Rras.PROJECTION_INFO_head
    class PROJECTION_INFO__Anonymous_e__Union(Union):
        pass
    PROJECTION_INFO__Anonymous_e__Union._fields_ = [
        ("PppProjectionInfo", win32more.NetworkManagement.Rras.PPP_PROJECTION_INFO),
        ("Ikev2ProjectionInfo", win32more.NetworkManagement.Rras.IKEV2_PROJECTION_INFO),
    ]
    PROJECTION_INFO._anonymous_ = [
        'Anonymous',
    ]
    PROJECTION_INFO._fields_ = [
        ("projectionInfoType", Byte),
        ("Anonymous", PROJECTION_INFO__Anonymous_e__Union),
    ]
    return PROJECTION_INFO
def _define_PROJECTION_INFO2_head():
    class PROJECTION_INFO2(Structure):
        pass
    return PROJECTION_INFO2
def _define_PROJECTION_INFO2():
    PROJECTION_INFO2 = win32more.NetworkManagement.Rras.PROJECTION_INFO2_head
    class PROJECTION_INFO2__Anonymous_e__Union(Union):
        pass
    PROJECTION_INFO2__Anonymous_e__Union._fields_ = [
        ("PppProjectionInfo", win32more.NetworkManagement.Rras.PPP_PROJECTION_INFO2),
        ("Ikev2ProjectionInfo", win32more.NetworkManagement.Rras.IKEV2_PROJECTION_INFO2),
    ]
    PROJECTION_INFO2._anonymous_ = [
        'Anonymous',
    ]
    PROJECTION_INFO2._fields_ = [
        ("projectionInfoType", Byte),
        ("Anonymous", PROJECTION_INFO2__Anonymous_e__Union),
    ]
    return PROJECTION_INFO2
def _define_RAS_CONNECTION_EX_head():
    class RAS_CONNECTION_EX(Structure):
        pass
    return RAS_CONNECTION_EX
def _define_RAS_CONNECTION_EX():
    RAS_CONNECTION_EX = win32more.NetworkManagement.Rras.RAS_CONNECTION_EX_head
    RAS_CONNECTION_EX._fields_ = [
        ("Header", win32more.NetworkManagement.Rras.MPRAPI_OBJECT_HEADER),
        ("dwConnectDuration", UInt32),
        ("dwInterfaceType", win32more.NetworkManagement.Rras.ROUTER_INTERFACE_TYPE),
        ("dwConnectionFlags", win32more.NetworkManagement.Rras.RAS_FLAGS),
        ("wszInterfaceName", Char * 257),
        ("wszUserName", Char * 257),
        ("wszLogonDomain", Char * 16),
        ("wszRemoteComputer", Char * 17),
        ("guid", Guid),
        ("rasQuarState", win32more.NetworkManagement.Rras.RAS_QUARANTINE_STATE),
        ("probationTime", win32more.Foundation.FILETIME),
        ("dwBytesXmited", UInt32),
        ("dwBytesRcved", UInt32),
        ("dwFramesXmited", UInt32),
        ("dwFramesRcved", UInt32),
        ("dwCrcErr", UInt32),
        ("dwTimeoutErr", UInt32),
        ("dwAlignmentErr", UInt32),
        ("dwHardwareOverrunErr", UInt32),
        ("dwFramingErr", UInt32),
        ("dwBufferOverrunErr", UInt32),
        ("dwCompressionRatioIn", UInt32),
        ("dwCompressionRatioOut", UInt32),
        ("dwNumSwitchOvers", UInt32),
        ("wszRemoteEndpointAddress", Char * 65),
        ("wszLocalEndpointAddress", Char * 65),
        ("ProjectionInfo", win32more.NetworkManagement.Rras.PROJECTION_INFO),
        ("hConnection", win32more.Foundation.HANDLE),
        ("hInterface", win32more.Foundation.HANDLE),
    ]
    return RAS_CONNECTION_EX
def _define_RAS_CONNECTION_4_head():
    class RAS_CONNECTION_4(Structure):
        pass
    return RAS_CONNECTION_4
def _define_RAS_CONNECTION_4():
    RAS_CONNECTION_4 = win32more.NetworkManagement.Rras.RAS_CONNECTION_4_head
    RAS_CONNECTION_4._fields_ = [
        ("dwConnectDuration", UInt32),
        ("dwInterfaceType", win32more.NetworkManagement.Rras.ROUTER_INTERFACE_TYPE),
        ("dwConnectionFlags", win32more.NetworkManagement.Rras.RAS_FLAGS),
        ("wszInterfaceName", Char * 257),
        ("wszUserName", Char * 257),
        ("wszLogonDomain", Char * 16),
        ("wszRemoteComputer", Char * 17),
        ("guid", Guid),
        ("rasQuarState", win32more.NetworkManagement.Rras.RAS_QUARANTINE_STATE),
        ("probationTime", win32more.Foundation.FILETIME),
        ("connectionStartTime", win32more.Foundation.FILETIME),
        ("ullBytesXmited", UInt64),
        ("ullBytesRcved", UInt64),
        ("dwFramesXmited", UInt32),
        ("dwFramesRcved", UInt32),
        ("dwCrcErr", UInt32),
        ("dwTimeoutErr", UInt32),
        ("dwAlignmentErr", UInt32),
        ("dwHardwareOverrunErr", UInt32),
        ("dwFramingErr", UInt32),
        ("dwBufferOverrunErr", UInt32),
        ("dwCompressionRatioIn", UInt32),
        ("dwCompressionRatioOut", UInt32),
        ("dwNumSwitchOvers", UInt32),
        ("wszRemoteEndpointAddress", Char * 65),
        ("wszLocalEndpointAddress", Char * 65),
        ("ProjectionInfo", win32more.NetworkManagement.Rras.PROJECTION_INFO2),
        ("hConnection", win32more.Foundation.HANDLE),
        ("hInterface", win32more.Foundation.HANDLE),
        ("dwDeviceType", UInt32),
    ]
    return RAS_CONNECTION_4
def _define_ROUTER_CUSTOM_IKEv2_POLICY0_head():
    class ROUTER_CUSTOM_IKEv2_POLICY0(Structure):
        pass
    return ROUTER_CUSTOM_IKEv2_POLICY0
def _define_ROUTER_CUSTOM_IKEv2_POLICY0():
    ROUTER_CUSTOM_IKEv2_POLICY0 = win32more.NetworkManagement.Rras.ROUTER_CUSTOM_IKEv2_POLICY0_head
    ROUTER_CUSTOM_IKEv2_POLICY0._fields_ = [
        ("dwIntegrityMethod", UInt32),
        ("dwEncryptionMethod", UInt32),
        ("dwCipherTransformConstant", UInt32),
        ("dwAuthTransformConstant", UInt32),
        ("dwPfsGroup", UInt32),
        ("dwDhGroup", UInt32),
    ]
    return ROUTER_CUSTOM_IKEv2_POLICY0
def _define_ROUTER_IKEv2_IF_CUSTOM_CONFIG0_head():
    class ROUTER_IKEv2_IF_CUSTOM_CONFIG0(Structure):
        pass
    return ROUTER_IKEv2_IF_CUSTOM_CONFIG0
def _define_ROUTER_IKEv2_IF_CUSTOM_CONFIG0():
    ROUTER_IKEv2_IF_CUSTOM_CONFIG0 = win32more.NetworkManagement.Rras.ROUTER_IKEv2_IF_CUSTOM_CONFIG0_head
    ROUTER_IKEv2_IF_CUSTOM_CONFIG0._fields_ = [
        ("dwSaLifeTime", UInt32),
        ("dwSaDataSize", UInt32),
        ("certificateName", win32more.Security.Cryptography.CRYPTOAPI_BLOB),
        ("customPolicy", POINTER(win32more.NetworkManagement.Rras.ROUTER_CUSTOM_IKEv2_POLICY0_head)),
    ]
    return ROUTER_IKEv2_IF_CUSTOM_CONFIG0
def _define_MPR_IF_CUSTOMINFOEX0_head():
    class MPR_IF_CUSTOMINFOEX0(Structure):
        pass
    return MPR_IF_CUSTOMINFOEX0
def _define_MPR_IF_CUSTOMINFOEX0():
    MPR_IF_CUSTOMINFOEX0 = win32more.NetworkManagement.Rras.MPR_IF_CUSTOMINFOEX0_head
    MPR_IF_CUSTOMINFOEX0._fields_ = [
        ("Header", win32more.NetworkManagement.Rras.MPRAPI_OBJECT_HEADER),
        ("dwFlags", UInt32),
        ("customIkev2Config", win32more.NetworkManagement.Rras.ROUTER_IKEv2_IF_CUSTOM_CONFIG0),
    ]
    return MPR_IF_CUSTOMINFOEX0
def _define_MPR_CERT_EKU_head():
    class MPR_CERT_EKU(Structure):
        pass
    return MPR_CERT_EKU
def _define_MPR_CERT_EKU():
    MPR_CERT_EKU = win32more.NetworkManagement.Rras.MPR_CERT_EKU_head
    MPR_CERT_EKU._fields_ = [
        ("dwSize", UInt32),
        ("IsEKUOID", win32more.Foundation.BOOL),
        ("pwszEKU", win32more.Foundation.PWSTR),
    ]
    return MPR_CERT_EKU
def _define_VPN_TS_IP_ADDRESS_head():
    class VPN_TS_IP_ADDRESS(Structure):
        pass
    return VPN_TS_IP_ADDRESS
def _define_VPN_TS_IP_ADDRESS():
    VPN_TS_IP_ADDRESS = win32more.NetworkManagement.Rras.VPN_TS_IP_ADDRESS_head
    class VPN_TS_IP_ADDRESS__Anonymous_e__Union(Union):
        pass
    VPN_TS_IP_ADDRESS__Anonymous_e__Union._fields_ = [
        ("v4", win32more.Networking.WinSock.IN_ADDR),
        ("v6", win32more.Networking.WinSock.IN6_ADDR),
    ]
    VPN_TS_IP_ADDRESS._anonymous_ = [
        'Anonymous',
    ]
    VPN_TS_IP_ADDRESS._fields_ = [
        ("Type", UInt16),
        ("Anonymous", VPN_TS_IP_ADDRESS__Anonymous_e__Union),
    ]
    return VPN_TS_IP_ADDRESS
MPR_VPN_TS_TYPE = Int32
MPR_VPN_TS_IPv4_ADDR_RANGE = 7
MPR_VPN_TS_IPv6_ADDR_RANGE = 8
def _define__MPR_VPN_SELECTOR_head():
    class _MPR_VPN_SELECTOR(Structure):
        pass
    return _MPR_VPN_SELECTOR
def _define__MPR_VPN_SELECTOR():
    _MPR_VPN_SELECTOR = win32more.NetworkManagement.Rras._MPR_VPN_SELECTOR_head
    _MPR_VPN_SELECTOR._fields_ = [
        ("type", win32more.NetworkManagement.Rras.MPR_VPN_TS_TYPE),
        ("protocolId", Byte),
        ("portStart", UInt16),
        ("portEnd", UInt16),
        ("tsPayloadId", UInt16),
        ("addrStart", win32more.NetworkManagement.Rras.VPN_TS_IP_ADDRESS),
        ("addrEnd", win32more.NetworkManagement.Rras.VPN_TS_IP_ADDRESS),
    ]
    return _MPR_VPN_SELECTOR
def _define_MPR_VPN_TRAFFIC_SELECTORS_head():
    class MPR_VPN_TRAFFIC_SELECTORS(Structure):
        pass
    return MPR_VPN_TRAFFIC_SELECTORS
def _define_MPR_VPN_TRAFFIC_SELECTORS():
    MPR_VPN_TRAFFIC_SELECTORS = win32more.NetworkManagement.Rras.MPR_VPN_TRAFFIC_SELECTORS_head
    MPR_VPN_TRAFFIC_SELECTORS._fields_ = [
        ("numTsi", UInt32),
        ("numTsr", UInt32),
        ("tsI", POINTER(win32more.NetworkManagement.Rras._MPR_VPN_SELECTOR_head)),
        ("tsR", POINTER(win32more.NetworkManagement.Rras._MPR_VPN_SELECTOR_head)),
    ]
    return MPR_VPN_TRAFFIC_SELECTORS
def _define_ROUTER_IKEv2_IF_CUSTOM_CONFIG2_head():
    class ROUTER_IKEv2_IF_CUSTOM_CONFIG2(Structure):
        pass
    return ROUTER_IKEv2_IF_CUSTOM_CONFIG2
def _define_ROUTER_IKEv2_IF_CUSTOM_CONFIG2():
    ROUTER_IKEv2_IF_CUSTOM_CONFIG2 = win32more.NetworkManagement.Rras.ROUTER_IKEv2_IF_CUSTOM_CONFIG2_head
    ROUTER_IKEv2_IF_CUSTOM_CONFIG2._fields_ = [
        ("dwSaLifeTime", UInt32),
        ("dwSaDataSize", UInt32),
        ("certificateName", win32more.Security.Cryptography.CRYPTOAPI_BLOB),
        ("customPolicy", POINTER(win32more.NetworkManagement.Rras.ROUTER_CUSTOM_IKEv2_POLICY0_head)),
        ("certificateHash", win32more.Security.Cryptography.CRYPTOAPI_BLOB),
        ("dwMmSaLifeTime", UInt32),
        ("vpnTrafficSelectors", win32more.NetworkManagement.Rras.MPR_VPN_TRAFFIC_SELECTORS),
    ]
    return ROUTER_IKEv2_IF_CUSTOM_CONFIG2
def _define_MPR_IF_CUSTOMINFOEX2_head():
    class MPR_IF_CUSTOMINFOEX2(Structure):
        pass
    return MPR_IF_CUSTOMINFOEX2
def _define_MPR_IF_CUSTOMINFOEX2():
    MPR_IF_CUSTOMINFOEX2 = win32more.NetworkManagement.Rras.MPR_IF_CUSTOMINFOEX2_head
    MPR_IF_CUSTOMINFOEX2._fields_ = [
        ("Header", win32more.NetworkManagement.Rras.MPRAPI_OBJECT_HEADER),
        ("dwFlags", UInt32),
        ("customIkev2Config", win32more.NetworkManagement.Rras.ROUTER_IKEv2_IF_CUSTOM_CONFIG2),
    ]
    return MPR_IF_CUSTOMINFOEX2
def _define_IKEV2_TUNNEL_CONFIG_PARAMS4_head():
    class IKEV2_TUNNEL_CONFIG_PARAMS4(Structure):
        pass
    return IKEV2_TUNNEL_CONFIG_PARAMS4
def _define_IKEV2_TUNNEL_CONFIG_PARAMS4():
    IKEV2_TUNNEL_CONFIG_PARAMS4 = win32more.NetworkManagement.Rras.IKEV2_TUNNEL_CONFIG_PARAMS4_head
    IKEV2_TUNNEL_CONFIG_PARAMS4._fields_ = [
        ("dwIdleTimeout", UInt32),
        ("dwNetworkBlackoutTime", UInt32),
        ("dwSaLifeTime", UInt32),
        ("dwSaDataSizeForRenegotiation", UInt32),
        ("dwConfigOptions", UInt32),
        ("dwTotalCertificates", UInt32),
        ("certificateNames", POINTER(win32more.Security.Cryptography.CRYPTOAPI_BLOB_head)),
        ("machineCertificateName", win32more.Security.Cryptography.CRYPTOAPI_BLOB),
        ("dwEncryptionType", UInt32),
        ("customPolicy", POINTER(win32more.NetworkManagement.Rras.ROUTER_CUSTOM_IKEv2_POLICY0_head)),
        ("dwTotalEkus", UInt32),
        ("certificateEKUs", POINTER(win32more.NetworkManagement.Rras.MPR_CERT_EKU_head)),
        ("machineCertificateHash", win32more.Security.Cryptography.CRYPTOAPI_BLOB),
        ("dwMmSaLifeTime", UInt32),
    ]
    return IKEV2_TUNNEL_CONFIG_PARAMS4
def _define_ROUTER_IKEv2_IF_CUSTOM_CONFIG1_head():
    class ROUTER_IKEv2_IF_CUSTOM_CONFIG1(Structure):
        pass
    return ROUTER_IKEv2_IF_CUSTOM_CONFIG1
def _define_ROUTER_IKEv2_IF_CUSTOM_CONFIG1():
    ROUTER_IKEv2_IF_CUSTOM_CONFIG1 = win32more.NetworkManagement.Rras.ROUTER_IKEv2_IF_CUSTOM_CONFIG1_head
    ROUTER_IKEv2_IF_CUSTOM_CONFIG1._fields_ = [
        ("dwSaLifeTime", UInt32),
        ("dwSaDataSize", UInt32),
        ("certificateName", win32more.Security.Cryptography.CRYPTOAPI_BLOB),
        ("customPolicy", POINTER(win32more.NetworkManagement.Rras.ROUTER_CUSTOM_IKEv2_POLICY0_head)),
        ("certificateHash", win32more.Security.Cryptography.CRYPTOAPI_BLOB),
    ]
    return ROUTER_IKEv2_IF_CUSTOM_CONFIG1
def _define_MPR_IF_CUSTOMINFOEX1_head():
    class MPR_IF_CUSTOMINFOEX1(Structure):
        pass
    return MPR_IF_CUSTOMINFOEX1
def _define_MPR_IF_CUSTOMINFOEX1():
    MPR_IF_CUSTOMINFOEX1 = win32more.NetworkManagement.Rras.MPR_IF_CUSTOMINFOEX1_head
    MPR_IF_CUSTOMINFOEX1._fields_ = [
        ("Header", win32more.NetworkManagement.Rras.MPRAPI_OBJECT_HEADER),
        ("dwFlags", UInt32),
        ("customIkev2Config", win32more.NetworkManagement.Rras.ROUTER_IKEv2_IF_CUSTOM_CONFIG1),
    ]
    return MPR_IF_CUSTOMINFOEX1
def _define_IKEV2_TUNNEL_CONFIG_PARAMS3_head():
    class IKEV2_TUNNEL_CONFIG_PARAMS3(Structure):
        pass
    return IKEV2_TUNNEL_CONFIG_PARAMS3
def _define_IKEV2_TUNNEL_CONFIG_PARAMS3():
    IKEV2_TUNNEL_CONFIG_PARAMS3 = win32more.NetworkManagement.Rras.IKEV2_TUNNEL_CONFIG_PARAMS3_head
    IKEV2_TUNNEL_CONFIG_PARAMS3._fields_ = [
        ("dwIdleTimeout", UInt32),
        ("dwNetworkBlackoutTime", UInt32),
        ("dwSaLifeTime", UInt32),
        ("dwSaDataSizeForRenegotiation", UInt32),
        ("dwConfigOptions", UInt32),
        ("dwTotalCertificates", UInt32),
        ("certificateNames", POINTER(win32more.Security.Cryptography.CRYPTOAPI_BLOB_head)),
        ("machineCertificateName", win32more.Security.Cryptography.CRYPTOAPI_BLOB),
        ("dwEncryptionType", UInt32),
        ("customPolicy", POINTER(win32more.NetworkManagement.Rras.ROUTER_CUSTOM_IKEv2_POLICY0_head)),
        ("dwTotalEkus", UInt32),
        ("certificateEKUs", POINTER(win32more.NetworkManagement.Rras.MPR_CERT_EKU_head)),
        ("machineCertificateHash", win32more.Security.Cryptography.CRYPTOAPI_BLOB),
    ]
    return IKEV2_TUNNEL_CONFIG_PARAMS3
def _define_IKEV2_TUNNEL_CONFIG_PARAMS2_head():
    class IKEV2_TUNNEL_CONFIG_PARAMS2(Structure):
        pass
    return IKEV2_TUNNEL_CONFIG_PARAMS2
def _define_IKEV2_TUNNEL_CONFIG_PARAMS2():
    IKEV2_TUNNEL_CONFIG_PARAMS2 = win32more.NetworkManagement.Rras.IKEV2_TUNNEL_CONFIG_PARAMS2_head
    IKEV2_TUNNEL_CONFIG_PARAMS2._fields_ = [
        ("dwIdleTimeout", UInt32),
        ("dwNetworkBlackoutTime", UInt32),
        ("dwSaLifeTime", UInt32),
        ("dwSaDataSizeForRenegotiation", UInt32),
        ("dwConfigOptions", UInt32),
        ("dwTotalCertificates", UInt32),
        ("certificateNames", POINTER(win32more.Security.Cryptography.CRYPTOAPI_BLOB_head)),
        ("machineCertificateName", win32more.Security.Cryptography.CRYPTOAPI_BLOB),
        ("dwEncryptionType", UInt32),
        ("customPolicy", POINTER(win32more.NetworkManagement.Rras.ROUTER_CUSTOM_IKEv2_POLICY0_head)),
    ]
    return IKEV2_TUNNEL_CONFIG_PARAMS2
def _define_L2TP_TUNNEL_CONFIG_PARAMS2_head():
    class L2TP_TUNNEL_CONFIG_PARAMS2(Structure):
        pass
    return L2TP_TUNNEL_CONFIG_PARAMS2
def _define_L2TP_TUNNEL_CONFIG_PARAMS2():
    L2TP_TUNNEL_CONFIG_PARAMS2 = win32more.NetworkManagement.Rras.L2TP_TUNNEL_CONFIG_PARAMS2_head
    L2TP_TUNNEL_CONFIG_PARAMS2._fields_ = [
        ("dwIdleTimeout", UInt32),
        ("dwEncryptionType", UInt32),
        ("dwSaLifeTime", UInt32),
        ("dwSaDataSizeForRenegotiation", UInt32),
        ("customPolicy", POINTER(win32more.NetworkManagement.Rras.ROUTER_CUSTOM_IKEv2_POLICY0_head)),
        ("dwMmSaLifeTime", UInt32),
    ]
    return L2TP_TUNNEL_CONFIG_PARAMS2
def _define_L2TP_TUNNEL_CONFIG_PARAMS1_head():
    class L2TP_TUNNEL_CONFIG_PARAMS1(Structure):
        pass
    return L2TP_TUNNEL_CONFIG_PARAMS1
def _define_L2TP_TUNNEL_CONFIG_PARAMS1():
    L2TP_TUNNEL_CONFIG_PARAMS1 = win32more.NetworkManagement.Rras.L2TP_TUNNEL_CONFIG_PARAMS1_head
    L2TP_TUNNEL_CONFIG_PARAMS1._fields_ = [
        ("dwIdleTimeout", UInt32),
        ("dwEncryptionType", UInt32),
        ("dwSaLifeTime", UInt32),
        ("dwSaDataSizeForRenegotiation", UInt32),
        ("customPolicy", POINTER(win32more.NetworkManagement.Rras.ROUTER_CUSTOM_IKEv2_POLICY0_head)),
    ]
    return L2TP_TUNNEL_CONFIG_PARAMS1
def _define_IKEV2_CONFIG_PARAMS_head():
    class IKEV2_CONFIG_PARAMS(Structure):
        pass
    return IKEV2_CONFIG_PARAMS
def _define_IKEV2_CONFIG_PARAMS():
    IKEV2_CONFIG_PARAMS = win32more.NetworkManagement.Rras.IKEV2_CONFIG_PARAMS_head
    IKEV2_CONFIG_PARAMS._fields_ = [
        ("dwNumPorts", UInt32),
        ("dwPortFlags", UInt32),
        ("dwTunnelConfigParamFlags", UInt32),
        ("TunnelConfigParams", win32more.NetworkManagement.Rras.IKEV2_TUNNEL_CONFIG_PARAMS4),
    ]
    return IKEV2_CONFIG_PARAMS
def _define_PPTP_CONFIG_PARAMS_head():
    class PPTP_CONFIG_PARAMS(Structure):
        pass
    return PPTP_CONFIG_PARAMS
def _define_PPTP_CONFIG_PARAMS():
    PPTP_CONFIG_PARAMS = win32more.NetworkManagement.Rras.PPTP_CONFIG_PARAMS_head
    PPTP_CONFIG_PARAMS._fields_ = [
        ("dwNumPorts", UInt32),
        ("dwPortFlags", UInt32),
    ]
    return PPTP_CONFIG_PARAMS
def _define_L2TP_CONFIG_PARAMS1_head():
    class L2TP_CONFIG_PARAMS1(Structure):
        pass
    return L2TP_CONFIG_PARAMS1
def _define_L2TP_CONFIG_PARAMS1():
    L2TP_CONFIG_PARAMS1 = win32more.NetworkManagement.Rras.L2TP_CONFIG_PARAMS1_head
    L2TP_CONFIG_PARAMS1._fields_ = [
        ("dwNumPorts", UInt32),
        ("dwPortFlags", UInt32),
        ("dwTunnelConfigParamFlags", UInt32),
        ("TunnelConfigParams", win32more.NetworkManagement.Rras.L2TP_TUNNEL_CONFIG_PARAMS2),
    ]
    return L2TP_CONFIG_PARAMS1
def _define_GRE_CONFIG_PARAMS0_head():
    class GRE_CONFIG_PARAMS0(Structure):
        pass
    return GRE_CONFIG_PARAMS0
def _define_GRE_CONFIG_PARAMS0():
    GRE_CONFIG_PARAMS0 = win32more.NetworkManagement.Rras.GRE_CONFIG_PARAMS0_head
    GRE_CONFIG_PARAMS0._fields_ = [
        ("dwNumPorts", UInt32),
        ("dwPortFlags", UInt32),
    ]
    return GRE_CONFIG_PARAMS0
def _define_L2TP_CONFIG_PARAMS0_head():
    class L2TP_CONFIG_PARAMS0(Structure):
        pass
    return L2TP_CONFIG_PARAMS0
def _define_L2TP_CONFIG_PARAMS0():
    L2TP_CONFIG_PARAMS0 = win32more.NetworkManagement.Rras.L2TP_CONFIG_PARAMS0_head
    L2TP_CONFIG_PARAMS0._fields_ = [
        ("dwNumPorts", UInt32),
        ("dwPortFlags", UInt32),
    ]
    return L2TP_CONFIG_PARAMS0
def _define_SSTP_CERT_INFO_head():
    class SSTP_CERT_INFO(Structure):
        pass
    return SSTP_CERT_INFO
def _define_SSTP_CERT_INFO():
    SSTP_CERT_INFO = win32more.NetworkManagement.Rras.SSTP_CERT_INFO_head
    SSTP_CERT_INFO._fields_ = [
        ("isDefault", win32more.Foundation.BOOL),
        ("certBlob", win32more.Security.Cryptography.CRYPTOAPI_BLOB),
    ]
    return SSTP_CERT_INFO
def _define_SSTP_CONFIG_PARAMS_head():
    class SSTP_CONFIG_PARAMS(Structure):
        pass
    return SSTP_CONFIG_PARAMS
def _define_SSTP_CONFIG_PARAMS():
    SSTP_CONFIG_PARAMS = win32more.NetworkManagement.Rras.SSTP_CONFIG_PARAMS_head
    SSTP_CONFIG_PARAMS._fields_ = [
        ("dwNumPorts", UInt32),
        ("dwPortFlags", UInt32),
        ("isUseHttps", win32more.Foundation.BOOL),
        ("certAlgorithm", UInt32),
        ("sstpCertDetails", win32more.NetworkManagement.Rras.SSTP_CERT_INFO),
    ]
    return SSTP_CONFIG_PARAMS
def _define_MPRAPI_TUNNEL_CONFIG_PARAMS0_head():
    class MPRAPI_TUNNEL_CONFIG_PARAMS0(Structure):
        pass
    return MPRAPI_TUNNEL_CONFIG_PARAMS0
def _define_MPRAPI_TUNNEL_CONFIG_PARAMS0():
    MPRAPI_TUNNEL_CONFIG_PARAMS0 = win32more.NetworkManagement.Rras.MPRAPI_TUNNEL_CONFIG_PARAMS0_head
    MPRAPI_TUNNEL_CONFIG_PARAMS0._fields_ = [
        ("IkeConfigParams", win32more.NetworkManagement.Rras.IKEV2_CONFIG_PARAMS),
        ("PptpConfigParams", win32more.NetworkManagement.Rras.PPTP_CONFIG_PARAMS),
        ("L2tpConfigParams", win32more.NetworkManagement.Rras.L2TP_CONFIG_PARAMS1),
        ("SstpConfigParams", win32more.NetworkManagement.Rras.SSTP_CONFIG_PARAMS),
    ]
    return MPRAPI_TUNNEL_CONFIG_PARAMS0
def _define_MPRAPI_TUNNEL_CONFIG_PARAMS1_head():
    class MPRAPI_TUNNEL_CONFIG_PARAMS1(Structure):
        pass
    return MPRAPI_TUNNEL_CONFIG_PARAMS1
def _define_MPRAPI_TUNNEL_CONFIG_PARAMS1():
    MPRAPI_TUNNEL_CONFIG_PARAMS1 = win32more.NetworkManagement.Rras.MPRAPI_TUNNEL_CONFIG_PARAMS1_head
    MPRAPI_TUNNEL_CONFIG_PARAMS1._fields_ = [
        ("IkeConfigParams", win32more.NetworkManagement.Rras.IKEV2_CONFIG_PARAMS),
        ("PptpConfigParams", win32more.NetworkManagement.Rras.PPTP_CONFIG_PARAMS),
        ("L2tpConfigParams", win32more.NetworkManagement.Rras.L2TP_CONFIG_PARAMS1),
        ("SstpConfigParams", win32more.NetworkManagement.Rras.SSTP_CONFIG_PARAMS),
        ("GREConfigParams", win32more.NetworkManagement.Rras.GRE_CONFIG_PARAMS0),
    ]
    return MPRAPI_TUNNEL_CONFIG_PARAMS1
def _define_MPR_SERVER_EX0_head():
    class MPR_SERVER_EX0(Structure):
        pass
    return MPR_SERVER_EX0
def _define_MPR_SERVER_EX0():
    MPR_SERVER_EX0 = win32more.NetworkManagement.Rras.MPR_SERVER_EX0_head
    MPR_SERVER_EX0._fields_ = [
        ("Header", win32more.NetworkManagement.Rras.MPRAPI_OBJECT_HEADER),
        ("fLanOnlyMode", UInt32),
        ("dwUpTime", UInt32),
        ("dwTotalPorts", UInt32),
        ("dwPortsInUse", UInt32),
        ("Reserved", UInt32),
        ("ConfigParams", win32more.NetworkManagement.Rras.MPRAPI_TUNNEL_CONFIG_PARAMS0),
    ]
    return MPR_SERVER_EX0
def _define_MPR_SERVER_EX1_head():
    class MPR_SERVER_EX1(Structure):
        pass
    return MPR_SERVER_EX1
def _define_MPR_SERVER_EX1():
    MPR_SERVER_EX1 = win32more.NetworkManagement.Rras.MPR_SERVER_EX1_head
    MPR_SERVER_EX1._fields_ = [
        ("Header", win32more.NetworkManagement.Rras.MPRAPI_OBJECT_HEADER),
        ("fLanOnlyMode", UInt32),
        ("dwUpTime", UInt32),
        ("dwTotalPorts", UInt32),
        ("dwPortsInUse", UInt32),
        ("Reserved", UInt32),
        ("ConfigParams", win32more.NetworkManagement.Rras.MPRAPI_TUNNEL_CONFIG_PARAMS1),
    ]
    return MPR_SERVER_EX1
def _define_MPR_SERVER_SET_CONFIG_EX0_head():
    class MPR_SERVER_SET_CONFIG_EX0(Structure):
        pass
    return MPR_SERVER_SET_CONFIG_EX0
def _define_MPR_SERVER_SET_CONFIG_EX0():
    MPR_SERVER_SET_CONFIG_EX0 = win32more.NetworkManagement.Rras.MPR_SERVER_SET_CONFIG_EX0_head
    MPR_SERVER_SET_CONFIG_EX0._fields_ = [
        ("Header", win32more.NetworkManagement.Rras.MPRAPI_OBJECT_HEADER),
        ("setConfigForProtocols", UInt32),
        ("ConfigParams", win32more.NetworkManagement.Rras.MPRAPI_TUNNEL_CONFIG_PARAMS0),
    ]
    return MPR_SERVER_SET_CONFIG_EX0
def _define_MPR_SERVER_SET_CONFIG_EX1_head():
    class MPR_SERVER_SET_CONFIG_EX1(Structure):
        pass
    return MPR_SERVER_SET_CONFIG_EX1
def _define_MPR_SERVER_SET_CONFIG_EX1():
    MPR_SERVER_SET_CONFIG_EX1 = win32more.NetworkManagement.Rras.MPR_SERVER_SET_CONFIG_EX1_head
    MPR_SERVER_SET_CONFIG_EX1._fields_ = [
        ("Header", win32more.NetworkManagement.Rras.MPRAPI_OBJECT_HEADER),
        ("setConfigForProtocols", UInt32),
        ("ConfigParams", win32more.NetworkManagement.Rras.MPRAPI_TUNNEL_CONFIG_PARAMS1),
    ]
    return MPR_SERVER_SET_CONFIG_EX1
def _define_AUTH_VALIDATION_EX_head():
    class AUTH_VALIDATION_EX(Structure):
        pass
    return AUTH_VALIDATION_EX
def _define_AUTH_VALIDATION_EX():
    AUTH_VALIDATION_EX = win32more.NetworkManagement.Rras.AUTH_VALIDATION_EX_head
    AUTH_VALIDATION_EX._fields_ = [
        ("Header", win32more.NetworkManagement.Rras.MPRAPI_OBJECT_HEADER),
        ("hRasConnection", win32more.Foundation.HANDLE),
        ("wszUserName", Char * 257),
        ("wszLogonDomain", Char * 16),
        ("AuthInfoSize", UInt32),
        ("AuthInfo", Byte * 0),
    ]
    return AUTH_VALIDATION_EX
def _define_RAS_UPDATE_CONNECTION_head():
    class RAS_UPDATE_CONNECTION(Structure):
        pass
    return RAS_UPDATE_CONNECTION
def _define_RAS_UPDATE_CONNECTION():
    RAS_UPDATE_CONNECTION = win32more.NetworkManagement.Rras.RAS_UPDATE_CONNECTION_head
    RAS_UPDATE_CONNECTION._fields_ = [
        ("Header", win32more.NetworkManagement.Rras.MPRAPI_OBJECT_HEADER),
        ("dwIfIndex", UInt32),
        ("wszLocalEndpointAddress", Char * 65),
        ("wszRemoteEndpointAddress", Char * 65),
    ]
    return RAS_UPDATE_CONNECTION
def _define_PMPRADMINGETIPADDRESSFORUSER():
    return CFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(win32more.Foundation.BOOL), use_last_error=False)
def _define_PMPRADMINRELEASEIPADRESS():
    return CFUNCTYPE(Void,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)
def _define_PMPRADMINGETIPV6ADDRESSFORUSER():
    return CFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Networking.WinSock.IN6_ADDR_head),POINTER(win32more.Foundation.BOOL), use_last_error=False)
def _define_PMPRADMINRELEASEIPV6ADDRESSFORUSER():
    return CFUNCTYPE(Void,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Networking.WinSock.IN6_ADDR_head), use_last_error=False)
def _define_PMPRADMINACCEPTNEWCONNECTION():
    return CFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.NetworkManagement.Rras.RAS_CONNECTION_0_head),POINTER(win32more.NetworkManagement.Rras.RAS_CONNECTION_1_head), use_last_error=False)
def _define_PMPRADMINACCEPTNEWCONNECTION2():
    return CFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.NetworkManagement.Rras.RAS_CONNECTION_0_head),POINTER(win32more.NetworkManagement.Rras.RAS_CONNECTION_1_head),POINTER(win32more.NetworkManagement.Rras.RAS_CONNECTION_2_head), use_last_error=False)
def _define_PMPRADMINACCEPTNEWCONNECTION3():
    return CFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.NetworkManagement.Rras.RAS_CONNECTION_0_head),POINTER(win32more.NetworkManagement.Rras.RAS_CONNECTION_1_head),POINTER(win32more.NetworkManagement.Rras.RAS_CONNECTION_2_head),POINTER(win32more.NetworkManagement.Rras.RAS_CONNECTION_3_head), use_last_error=False)
def _define_PMPRADMINACCEPTNEWLINK():
    return CFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.NetworkManagement.Rras.RAS_PORT_0_head),POINTER(win32more.NetworkManagement.Rras.RAS_PORT_1_head), use_last_error=False)
def _define_PMPRADMINCONNECTIONHANGUPNOTIFICATION():
    return CFUNCTYPE(Void,POINTER(win32more.NetworkManagement.Rras.RAS_CONNECTION_0_head),POINTER(win32more.NetworkManagement.Rras.RAS_CONNECTION_1_head), use_last_error=False)
def _define_PMPRADMINCONNECTIONHANGUPNOTIFICATION2():
    return CFUNCTYPE(Void,POINTER(win32more.NetworkManagement.Rras.RAS_CONNECTION_0_head),POINTER(win32more.NetworkManagement.Rras.RAS_CONNECTION_1_head),POINTER(win32more.NetworkManagement.Rras.RAS_CONNECTION_2_head), use_last_error=False)
def _define_PMPRADMINCONNECTIONHANGUPNOTIFICATION3():
    return CFUNCTYPE(Void,POINTER(win32more.NetworkManagement.Rras.RAS_CONNECTION_0_head),POINTER(win32more.NetworkManagement.Rras.RAS_CONNECTION_1_head),POINTER(win32more.NetworkManagement.Rras.RAS_CONNECTION_2_head),win32more.NetworkManagement.Rras.RAS_CONNECTION_3, use_last_error=False)
def _define_PMPRADMINLINKHANGUPNOTIFICATION():
    return CFUNCTYPE(Void,POINTER(win32more.NetworkManagement.Rras.RAS_PORT_0_head),POINTER(win32more.NetworkManagement.Rras.RAS_PORT_1_head), use_last_error=False)
def _define_PMPRADMINTERMINATEDLL():
    return CFUNCTYPE(UInt32, use_last_error=False)
def _define_PMPRADMINACCEPTREAUTHENTICATION():
    return CFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.NetworkManagement.Rras.RAS_CONNECTION_0_head),POINTER(win32more.NetworkManagement.Rras.RAS_CONNECTION_1_head),POINTER(win32more.NetworkManagement.Rras.RAS_CONNECTION_2_head),POINTER(win32more.NetworkManagement.Rras.RAS_CONNECTION_3_head), use_last_error=False)
def _define_PMPRADMINACCEPTNEWCONNECTIONEX():
    return CFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.NetworkManagement.Rras.RAS_CONNECTION_EX_head), use_last_error=False)
def _define_PMPRADMINACCEPTREAUTHENTICATIONEX():
    return CFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.NetworkManagement.Rras.RAS_CONNECTION_EX_head), use_last_error=False)
def _define_PMPRADMINACCEPTTUNNELENDPOINTCHANGEEX():
    return CFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.NetworkManagement.Rras.RAS_CONNECTION_EX_head), use_last_error=False)
def _define_PMPRADMINCONNECTIONHANGUPNOTIFICATIONEX():
    return CFUNCTYPE(Void,POINTER(win32more.NetworkManagement.Rras.RAS_CONNECTION_EX_head), use_last_error=False)
def _define_PMPRADMINRASVALIDATEPREAUTHENTICATEDCONNECTIONEX():
    return CFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.Rras.AUTH_VALIDATION_EX_head), use_last_error=False)
def _define_MPRAPI_ADMIN_DLL_CALLBACKS_head():
    class MPRAPI_ADMIN_DLL_CALLBACKS(Structure):
        pass
    return MPRAPI_ADMIN_DLL_CALLBACKS
def _define_MPRAPI_ADMIN_DLL_CALLBACKS():
    MPRAPI_ADMIN_DLL_CALLBACKS = win32more.NetworkManagement.Rras.MPRAPI_ADMIN_DLL_CALLBACKS_head
    MPRAPI_ADMIN_DLL_CALLBACKS._fields_ = [
        ("revision", Byte),
        ("lpfnMprAdminGetIpAddressForUser", win32more.NetworkManagement.Rras.PMPRADMINGETIPADDRESSFORUSER),
        ("lpfnMprAdminReleaseIpAddress", win32more.NetworkManagement.Rras.PMPRADMINRELEASEIPADRESS),
        ("lpfnMprAdminGetIpv6AddressForUser", win32more.NetworkManagement.Rras.PMPRADMINGETIPV6ADDRESSFORUSER),
        ("lpfnMprAdminReleaseIpV6AddressForUser", win32more.NetworkManagement.Rras.PMPRADMINRELEASEIPV6ADDRESSFORUSER),
        ("lpfnRasAdminAcceptNewLink", win32more.NetworkManagement.Rras.PMPRADMINACCEPTNEWLINK),
        ("lpfnRasAdminLinkHangupNotification", win32more.NetworkManagement.Rras.PMPRADMINLINKHANGUPNOTIFICATION),
        ("lpfnRasAdminTerminateDll", win32more.NetworkManagement.Rras.PMPRADMINTERMINATEDLL),
        ("lpfnRasAdminAcceptNewConnectionEx", win32more.NetworkManagement.Rras.PMPRADMINACCEPTNEWCONNECTIONEX),
        ("lpfnRasAdminAcceptEndpointChangeEx", win32more.NetworkManagement.Rras.PMPRADMINACCEPTTUNNELENDPOINTCHANGEEX),
        ("lpfnRasAdminAcceptReauthenticationEx", win32more.NetworkManagement.Rras.PMPRADMINACCEPTREAUTHENTICATIONEX),
        ("lpfnRasAdminConnectionHangupNotificationEx", win32more.NetworkManagement.Rras.PMPRADMINCONNECTIONHANGUPNOTIFICATIONEX),
        ("lpfnRASValidatePreAuthenticatedConnectionEx", win32more.NetworkManagement.Rras.PMPRADMINRASVALIDATEPREAUTHENTICATEDCONNECTIONEX),
    ]
    return MPRAPI_ADMIN_DLL_CALLBACKS
def _define_SECURITY_MESSAGE_head():
    class SECURITY_MESSAGE(Structure):
        pass
    return SECURITY_MESSAGE
def _define_SECURITY_MESSAGE():
    SECURITY_MESSAGE = win32more.NetworkManagement.Rras.SECURITY_MESSAGE_head
    SECURITY_MESSAGE._fields_ = [
        ("dwMsgId", win32more.NetworkManagement.Rras.SECURITY_MESSAGE_MSG_ID),
        ("hPort", IntPtr),
        ("dwError", UInt32),
        ("UserName", win32more.Foundation.CHAR * 257),
        ("Domain", win32more.Foundation.CHAR * 16),
    ]
    return SECURITY_MESSAGE
def _define_RAS_SECURITY_INFO_head():
    class RAS_SECURITY_INFO(Structure):
        pass
    return RAS_SECURITY_INFO
def _define_RAS_SECURITY_INFO():
    RAS_SECURITY_INFO = win32more.NetworkManagement.Rras.RAS_SECURITY_INFO_head
    RAS_SECURITY_INFO._fields_ = [
        ("LastError", UInt32),
        ("BytesReceived", UInt32),
        ("DeviceName", win32more.Foundation.CHAR * 129),
    ]
    return RAS_SECURITY_INFO
def _define_RASSECURITYPROC():
    return CFUNCTYPE(UInt32, use_last_error=False)
def _define_MGM_IF_ENTRY_head():
    class MGM_IF_ENTRY(Structure):
        pass
    return MGM_IF_ENTRY
def _define_MGM_IF_ENTRY():
    MGM_IF_ENTRY = win32more.NetworkManagement.Rras.MGM_IF_ENTRY_head
    MGM_IF_ENTRY._fields_ = [
        ("dwIfIndex", UInt32),
        ("dwIfNextHopAddr", UInt32),
        ("bIGMP", win32more.Foundation.BOOL),
        ("bIsEnabled", win32more.Foundation.BOOL),
    ]
    return MGM_IF_ENTRY
def _define_PMGM_RPF_CALLBACK():
    return CFUNCTYPE(UInt32,UInt32,UInt32,UInt32,UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32),UInt32,c_char_p_no,c_char_p_no, use_last_error=False)
def _define_PMGM_CREATION_ALERT_CALLBACK():
    return CFUNCTYPE(UInt32,UInt32,UInt32,UInt32,UInt32,UInt32,UInt32,UInt32,POINTER(win32more.NetworkManagement.Rras.MGM_IF_ENTRY_head), use_last_error=False)
def _define_PMGM_PRUNE_ALERT_CALLBACK():
    return CFUNCTYPE(UInt32,UInt32,UInt32,UInt32,UInt32,UInt32,UInt32,win32more.Foundation.BOOL,POINTER(UInt32), use_last_error=False)
def _define_PMGM_JOIN_ALERT_CALLBACK():
    return CFUNCTYPE(UInt32,UInt32,UInt32,UInt32,UInt32,win32more.Foundation.BOOL, use_last_error=False)
def _define_PMGM_WRONG_IF_CALLBACK():
    return CFUNCTYPE(UInt32,UInt32,UInt32,UInt32,UInt32,UInt32,c_char_p_no, use_last_error=False)
def _define_PMGM_LOCAL_JOIN_CALLBACK():
    return CFUNCTYPE(UInt32,UInt32,UInt32,UInt32,UInt32,UInt32,UInt32, use_last_error=False)
def _define_PMGM_LOCAL_LEAVE_CALLBACK():
    return CFUNCTYPE(UInt32,UInt32,UInt32,UInt32,UInt32,UInt32,UInt32, use_last_error=False)
def _define_PMGM_DISABLE_IGMP_CALLBACK():
    return CFUNCTYPE(UInt32,UInt32,UInt32, use_last_error=False)
def _define_PMGM_ENABLE_IGMP_CALLBACK():
    return CFUNCTYPE(UInt32,UInt32,UInt32, use_last_error=False)
def _define_ROUTING_PROTOCOL_CONFIG_head():
    class ROUTING_PROTOCOL_CONFIG(Structure):
        pass
    return ROUTING_PROTOCOL_CONFIG
def _define_ROUTING_PROTOCOL_CONFIG():
    ROUTING_PROTOCOL_CONFIG = win32more.NetworkManagement.Rras.ROUTING_PROTOCOL_CONFIG_head
    ROUTING_PROTOCOL_CONFIG._fields_ = [
        ("dwCallbackFlags", UInt32),
        ("pfnRpfCallback", win32more.NetworkManagement.Rras.PMGM_RPF_CALLBACK),
        ("pfnCreationAlertCallback", win32more.NetworkManagement.Rras.PMGM_CREATION_ALERT_CALLBACK),
        ("pfnPruneAlertCallback", win32more.NetworkManagement.Rras.PMGM_PRUNE_ALERT_CALLBACK),
        ("pfnJoinAlertCallback", win32more.NetworkManagement.Rras.PMGM_JOIN_ALERT_CALLBACK),
        ("pfnWrongIfCallback", win32more.NetworkManagement.Rras.PMGM_WRONG_IF_CALLBACK),
        ("pfnLocalJoinCallback", win32more.NetworkManagement.Rras.PMGM_LOCAL_JOIN_CALLBACK),
        ("pfnLocalLeaveCallback", win32more.NetworkManagement.Rras.PMGM_LOCAL_LEAVE_CALLBACK),
        ("pfnDisableIgmpCallback", win32more.NetworkManagement.Rras.PMGM_DISABLE_IGMP_CALLBACK),
        ("pfnEnableIgmpCallback", win32more.NetworkManagement.Rras.PMGM_ENABLE_IGMP_CALLBACK),
    ]
    return ROUTING_PROTOCOL_CONFIG
MGM_ENUM_TYPES = Int32
ANY_SOURCE = 0
ALL_SOURCES = 1
def _define_SOURCE_GROUP_ENTRY_head():
    class SOURCE_GROUP_ENTRY(Structure):
        pass
    return SOURCE_GROUP_ENTRY
def _define_SOURCE_GROUP_ENTRY():
    SOURCE_GROUP_ENTRY = win32more.NetworkManagement.Rras.SOURCE_GROUP_ENTRY_head
    SOURCE_GROUP_ENTRY._fields_ = [
        ("dwSourceAddr", UInt32),
        ("dwSourceMask", UInt32),
        ("dwGroupAddr", UInt32),
        ("dwGroupMask", UInt32),
    ]
    return SOURCE_GROUP_ENTRY
def _define_RTM_REGN_PROFILE_head():
    class RTM_REGN_PROFILE(Structure):
        pass
    return RTM_REGN_PROFILE
def _define_RTM_REGN_PROFILE():
    RTM_REGN_PROFILE = win32more.NetworkManagement.Rras.RTM_REGN_PROFILE_head
    RTM_REGN_PROFILE._fields_ = [
        ("MaxNextHopsInRoute", UInt32),
        ("MaxHandlesInEnum", UInt32),
        ("ViewsSupported", UInt32),
        ("NumberOfViews", UInt32),
    ]
    return RTM_REGN_PROFILE
def _define_RTM_NET_ADDRESS_head():
    class RTM_NET_ADDRESS(Structure):
        pass
    return RTM_NET_ADDRESS
def _define_RTM_NET_ADDRESS():
    RTM_NET_ADDRESS = win32more.NetworkManagement.Rras.RTM_NET_ADDRESS_head
    RTM_NET_ADDRESS._fields_ = [
        ("AddressFamily", UInt16),
        ("NumBits", UInt16),
        ("AddrBits", Byte * 16),
    ]
    return RTM_NET_ADDRESS
def _define_RTM_PREF_INFO_head():
    class RTM_PREF_INFO(Structure):
        pass
    return RTM_PREF_INFO
def _define_RTM_PREF_INFO():
    RTM_PREF_INFO = win32more.NetworkManagement.Rras.RTM_PREF_INFO_head
    RTM_PREF_INFO._fields_ = [
        ("Metric", UInt32),
        ("Preference", UInt32),
    ]
    return RTM_PREF_INFO
def _define_RTM_NEXTHOP_LIST_head():
    class RTM_NEXTHOP_LIST(Structure):
        pass
    return RTM_NEXTHOP_LIST
def _define_RTM_NEXTHOP_LIST():
    RTM_NEXTHOP_LIST = win32more.NetworkManagement.Rras.RTM_NEXTHOP_LIST_head
    RTM_NEXTHOP_LIST._fields_ = [
        ("NumNextHops", UInt16),
        ("NextHops", IntPtr * 0),
    ]
    return RTM_NEXTHOP_LIST
def _define_RTM_DEST_INFO_head():
    class RTM_DEST_INFO(Structure):
        pass
    return RTM_DEST_INFO
def _define_RTM_DEST_INFO():
    RTM_DEST_INFO = win32more.NetworkManagement.Rras.RTM_DEST_INFO_head
    class RTM_DEST_INFO__Anonymous_e__Struct(Structure):
        pass
    RTM_DEST_INFO__Anonymous_e__Struct._fields_ = [
        ("ViewId", Int32),
        ("NumRoutes", UInt32),
        ("Route", IntPtr),
        ("Owner", IntPtr),
        ("DestFlags", UInt32),
        ("HoldRoute", IntPtr),
    ]
    RTM_DEST_INFO._fields_ = [
        ("DestHandle", IntPtr),
        ("DestAddress", win32more.NetworkManagement.Rras.RTM_NET_ADDRESS),
        ("LastChanged", win32more.Foundation.FILETIME),
        ("BelongsToViews", UInt32),
        ("NumberOfViews", UInt32),
        ("ViewInfo", RTM_DEST_INFO__Anonymous_e__Struct * 0),
    ]
    return RTM_DEST_INFO
def _define_RTM_ROUTE_INFO_head():
    class RTM_ROUTE_INFO(Structure):
        pass
    return RTM_ROUTE_INFO
def _define_RTM_ROUTE_INFO():
    RTM_ROUTE_INFO = win32more.NetworkManagement.Rras.RTM_ROUTE_INFO_head
    RTM_ROUTE_INFO._fields_ = [
        ("DestHandle", IntPtr),
        ("RouteOwner", IntPtr),
        ("Neighbour", IntPtr),
        ("State", Byte),
        ("Flags1", Byte),
        ("Flags", UInt16),
        ("PrefInfo", win32more.NetworkManagement.Rras.RTM_PREF_INFO),
        ("BelongsToViews", UInt32),
        ("EntitySpecificInfo", c_void_p),
        ("NextHopsList", win32more.NetworkManagement.Rras.RTM_NEXTHOP_LIST),
    ]
    return RTM_ROUTE_INFO
def _define_RTM_NEXTHOP_INFO_head():
    class RTM_NEXTHOP_INFO(Structure):
        pass
    return RTM_NEXTHOP_INFO
def _define_RTM_NEXTHOP_INFO():
    RTM_NEXTHOP_INFO = win32more.NetworkManagement.Rras.RTM_NEXTHOP_INFO_head
    RTM_NEXTHOP_INFO._fields_ = [
        ("NextHopAddress", win32more.NetworkManagement.Rras.RTM_NET_ADDRESS),
        ("NextHopOwner", IntPtr),
        ("InterfaceIndex", UInt32),
        ("State", UInt16),
        ("Flags", UInt16),
        ("EntitySpecificInfo", c_void_p),
        ("RemoteNextHop", IntPtr),
    ]
    return RTM_NEXTHOP_INFO
def _define_RTM_ENTITY_ID_head():
    class RTM_ENTITY_ID(Structure):
        pass
    return RTM_ENTITY_ID
def _define_RTM_ENTITY_ID():
    RTM_ENTITY_ID = win32more.NetworkManagement.Rras.RTM_ENTITY_ID_head
    class RTM_ENTITY_ID__Anonymous_e__Union(Union):
        pass
    class RTM_ENTITY_ID__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    RTM_ENTITY_ID__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ("EntityProtocolId", UInt32),
        ("EntityInstanceId", UInt32),
    ]
    RTM_ENTITY_ID__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    RTM_ENTITY_ID__Anonymous_e__Union._fields_ = [
        ("Anonymous", RTM_ENTITY_ID__Anonymous_e__Union__Anonymous_e__Struct),
        ("EntityId", UInt64),
    ]
    RTM_ENTITY_ID._anonymous_ = [
        'Anonymous',
    ]
    RTM_ENTITY_ID._fields_ = [
        ("Anonymous", RTM_ENTITY_ID__Anonymous_e__Union),
    ]
    return RTM_ENTITY_ID
def _define_RTM_ENTITY_INFO_head():
    class RTM_ENTITY_INFO(Structure):
        pass
    return RTM_ENTITY_INFO
def _define_RTM_ENTITY_INFO():
    RTM_ENTITY_INFO = win32more.NetworkManagement.Rras.RTM_ENTITY_INFO_head
    RTM_ENTITY_INFO._fields_ = [
        ("RtmInstanceId", UInt16),
        ("AddressFamily", UInt16),
        ("EntityId", win32more.NetworkManagement.Rras.RTM_ENTITY_ID),
    ]
    return RTM_ENTITY_INFO
RTM_EVENT_TYPE = Int32
RTM_ENTITY_REGISTERED = 0
RTM_ENTITY_DEREGISTERED = 1
RTM_ROUTE_EXPIRED = 2
RTM_CHANGE_NOTIFICATION = 3
def _define_RTM_EVENT_CALLBACK():
    return CFUNCTYPE(UInt32,IntPtr,win32more.NetworkManagement.Rras.RTM_EVENT_TYPE,c_void_p,c_void_p, use_last_error=False)
def _define_RTM_ENTITY_METHOD_INPUT_head():
    class RTM_ENTITY_METHOD_INPUT(Structure):
        pass
    return RTM_ENTITY_METHOD_INPUT
def _define_RTM_ENTITY_METHOD_INPUT():
    RTM_ENTITY_METHOD_INPUT = win32more.NetworkManagement.Rras.RTM_ENTITY_METHOD_INPUT_head
    RTM_ENTITY_METHOD_INPUT._fields_ = [
        ("MethodType", UInt32),
        ("InputSize", UInt32),
        ("InputData", Byte * 0),
    ]
    return RTM_ENTITY_METHOD_INPUT
def _define_RTM_ENTITY_METHOD_OUTPUT_head():
    class RTM_ENTITY_METHOD_OUTPUT(Structure):
        pass
    return RTM_ENTITY_METHOD_OUTPUT
def _define_RTM_ENTITY_METHOD_OUTPUT():
    RTM_ENTITY_METHOD_OUTPUT = win32more.NetworkManagement.Rras.RTM_ENTITY_METHOD_OUTPUT_head
    RTM_ENTITY_METHOD_OUTPUT._fields_ = [
        ("MethodType", UInt32),
        ("MethodStatus", UInt32),
        ("OutputSize", UInt32),
        ("OutputData", Byte * 0),
    ]
    return RTM_ENTITY_METHOD_OUTPUT
def _define_RTM_ENTITY_EXPORT_METHOD():
    return CFUNCTYPE(Void,IntPtr,IntPtr,POINTER(win32more.NetworkManagement.Rras.RTM_ENTITY_METHOD_INPUT_head),POINTER(win32more.NetworkManagement.Rras.RTM_ENTITY_METHOD_OUTPUT_head), use_last_error=False)
def _define_RTM_ENTITY_EXPORT_METHODS_head():
    class RTM_ENTITY_EXPORT_METHODS(Structure):
        pass
    return RTM_ENTITY_EXPORT_METHODS
def _define_RTM_ENTITY_EXPORT_METHODS():
    RTM_ENTITY_EXPORT_METHODS = win32more.NetworkManagement.Rras.RTM_ENTITY_EXPORT_METHODS_head
    RTM_ENTITY_EXPORT_METHODS._fields_ = [
        ("NumMethods", UInt32),
        ("Methods", win32more.NetworkManagement.Rras.RTM_ENTITY_EXPORT_METHOD * 0),
    ]
    return RTM_ENTITY_EXPORT_METHODS
def _define_RasDialA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.Rras.RASDIALEXTENSIONS_head),win32more.Foundation.PSTR,POINTER(win32more.NetworkManagement.Rras.RASDIALPARAMSA_head),UInt32,c_void_p,POINTER(win32more.NetworkManagement.Rras.HRASCONN), use_last_error=False)(("RasDialA", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),(1, 'param4'),(1, 'param5'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasDialW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.Rras.RASDIALEXTENSIONS_head),win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Rras.RASDIALPARAMSW_head),UInt32,c_void_p,POINTER(win32more.NetworkManagement.Rras.HRASCONN), use_last_error=False)(("RasDialW", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),(1, 'param4'),(1, 'param5'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasDial():
    return win32more.NetworkManagement.Rras.RasDialW
def _define_RasEnumConnectionsA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.Rras.RASCONNA_head),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("RasEnumConnectionsA", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasEnumConnectionsW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.Rras.RASCONNW_head),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("RasEnumConnectionsW", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasEnumConnections():
    return win32more.NetworkManagement.Rras.RasEnumConnectionsW
def _define_RasEnumEntriesA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(win32more.NetworkManagement.Rras.RASENTRYNAMEA_head),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("RasEnumEntriesA", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),(1, 'param4'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasEnumEntriesW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Rras.RASENTRYNAMEW_head),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("RasEnumEntriesW", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),(1, 'param4'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasEnumEntries():
    return win32more.NetworkManagement.Rras.RasEnumEntriesW
def _define_RasGetConnectStatusA():
    try:
        return WINFUNCTYPE(UInt32,win32more.NetworkManagement.Rras.HRASCONN,POINTER(win32more.NetworkManagement.Rras.RASCONNSTATUSA_head), use_last_error=False)(("RasGetConnectStatusA", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasGetConnectStatusW():
    try:
        return WINFUNCTYPE(UInt32,win32more.NetworkManagement.Rras.HRASCONN,POINTER(win32more.NetworkManagement.Rras.RASCONNSTATUSW_head), use_last_error=False)(("RasGetConnectStatusW", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasGetConnectStatus():
    return win32more.NetworkManagement.Rras.RasGetConnectStatusW
def _define_RasGetErrorStringA():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(Byte),UInt32, use_last_error=False)(("RasGetErrorStringA", windll["RASAPI32"]), ((1, 'ResourceId'),(1, 'lpszString'),(1, 'InBufSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasGetErrorStringW():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(Char),UInt32, use_last_error=False)(("RasGetErrorStringW", windll["RASAPI32"]), ((1, 'ResourceId'),(1, 'lpszString'),(1, 'InBufSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasGetErrorString():
    return win32more.NetworkManagement.Rras.RasGetErrorStringW
def _define_RasHangUpA():
    try:
        return WINFUNCTYPE(UInt32,win32more.NetworkManagement.Rras.HRASCONN, use_last_error=False)(("RasHangUpA", windll["RASAPI32"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasHangUpW():
    try:
        return WINFUNCTYPE(UInt32,win32more.NetworkManagement.Rras.HRASCONN, use_last_error=False)(("RasHangUpW", windll["RASAPI32"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasHangUp():
    return win32more.NetworkManagement.Rras.RasHangUpW
def _define_RasGetProjectionInfoA():
    try:
        return WINFUNCTYPE(UInt32,win32more.NetworkManagement.Rras.HRASCONN,win32more.NetworkManagement.Rras.RASPROJECTION,c_void_p,POINTER(UInt32), use_last_error=False)(("RasGetProjectionInfoA", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasGetProjectionInfoW():
    try:
        return WINFUNCTYPE(UInt32,win32more.NetworkManagement.Rras.HRASCONN,win32more.NetworkManagement.Rras.RASPROJECTION,c_void_p,POINTER(UInt32), use_last_error=False)(("RasGetProjectionInfoW", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasGetProjectionInfo():
    return win32more.NetworkManagement.Rras.RasGetProjectionInfoW
def _define_RasCreatePhonebookEntryA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HWND,win32more.Foundation.PSTR, use_last_error=False)(("RasCreatePhonebookEntryA", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasCreatePhonebookEntryW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HWND,win32more.Foundation.PWSTR, use_last_error=False)(("RasCreatePhonebookEntryW", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasCreatePhonebookEntry():
    return win32more.NetworkManagement.Rras.RasCreatePhonebookEntryW
def _define_RasEditPhonebookEntryA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HWND,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("RasEditPhonebookEntryA", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasEditPhonebookEntryW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HWND,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("RasEditPhonebookEntryW", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasEditPhonebookEntry():
    return win32more.NetworkManagement.Rras.RasEditPhonebookEntryW
def _define_RasSetEntryDialParamsA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,POINTER(win32more.NetworkManagement.Rras.RASDIALPARAMSA_head),win32more.Foundation.BOOL, use_last_error=False)(("RasSetEntryDialParamsA", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasSetEntryDialParamsW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Rras.RASDIALPARAMSW_head),win32more.Foundation.BOOL, use_last_error=False)(("RasSetEntryDialParamsW", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasSetEntryDialParams():
    return win32more.NetworkManagement.Rras.RasSetEntryDialParamsW
def _define_RasGetEntryDialParamsA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,POINTER(win32more.NetworkManagement.Rras.RASDIALPARAMSA_head),POINTER(Int32), use_last_error=False)(("RasGetEntryDialParamsA", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasGetEntryDialParamsW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Rras.RASDIALPARAMSW_head),POINTER(Int32), use_last_error=False)(("RasGetEntryDialParamsW", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasGetEntryDialParams():
    return win32more.NetworkManagement.Rras.RasGetEntryDialParamsW
def _define_RasEnumDevicesA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.Rras.RASDEVINFOA_head),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("RasEnumDevicesA", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasEnumDevicesW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.Rras.RASDEVINFOW_head),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("RasEnumDevicesW", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasEnumDevices():
    return win32more.NetworkManagement.Rras.RasEnumDevicesW
def _define_RasGetCountryInfoA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.Rras.RASCTRYINFO_head),POINTER(UInt32), use_last_error=False)(("RasGetCountryInfoA", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasGetCountryInfoW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.Rras.RASCTRYINFO_head),POINTER(UInt32), use_last_error=False)(("RasGetCountryInfoW", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasGetCountryInfo():
    return win32more.NetworkManagement.Rras.RasGetCountryInfoW
def _define_RasGetEntryPropertiesA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(win32more.NetworkManagement.Rras.RASENTRYA_head),POINTER(UInt32),c_char_p_no,POINTER(UInt32), use_last_error=False)(("RasGetEntryPropertiesA", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),(1, 'param4'),(1, 'param5'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasGetEntryPropertiesW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Rras.RASENTRYW_head),POINTER(UInt32),c_char_p_no,POINTER(UInt32), use_last_error=False)(("RasGetEntryPropertiesW", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),(1, 'param4'),(1, 'param5'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasGetEntryProperties():
    return win32more.NetworkManagement.Rras.RasGetEntryPropertiesW
def _define_RasSetEntryPropertiesA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(win32more.NetworkManagement.Rras.RASENTRYA_head),UInt32,c_char_p_no,UInt32, use_last_error=False)(("RasSetEntryPropertiesA", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),(1, 'param4'),(1, 'param5'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasSetEntryPropertiesW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Rras.RASENTRYW_head),UInt32,c_char_p_no,UInt32, use_last_error=False)(("RasSetEntryPropertiesW", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),(1, 'param4'),(1, 'param5'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasSetEntryProperties():
    return win32more.NetworkManagement.Rras.RasSetEntryPropertiesW
def _define_RasRenameEntryA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("RasRenameEntryA", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasRenameEntryW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("RasRenameEntryW", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasRenameEntry():
    return win32more.NetworkManagement.Rras.RasRenameEntryW
def _define_RasDeleteEntryA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("RasDeleteEntryA", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasDeleteEntryW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("RasDeleteEntryW", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasDeleteEntry():
    return win32more.NetworkManagement.Rras.RasDeleteEntryW
def _define_RasValidateEntryNameA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("RasValidateEntryNameA", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasValidateEntryNameW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("RasValidateEntryNameW", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasValidateEntryName():
    return win32more.NetworkManagement.Rras.RasValidateEntryNameW
def _define_RasConnectionNotificationA():
    try:
        return WINFUNCTYPE(UInt32,win32more.NetworkManagement.Rras.HRASCONN,win32more.Foundation.HANDLE,UInt32, use_last_error=False)(("RasConnectionNotificationA", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasConnectionNotificationW():
    try:
        return WINFUNCTYPE(UInt32,win32more.NetworkManagement.Rras.HRASCONN,win32more.Foundation.HANDLE,UInt32, use_last_error=False)(("RasConnectionNotificationW", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasConnectionNotification():
    return win32more.NetworkManagement.Rras.RasConnectionNotificationW
def _define_RasGetSubEntryHandleA():
    try:
        return WINFUNCTYPE(UInt32,win32more.NetworkManagement.Rras.HRASCONN,UInt32,POINTER(win32more.NetworkManagement.Rras.HRASCONN), use_last_error=False)(("RasGetSubEntryHandleA", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasGetSubEntryHandleW():
    try:
        return WINFUNCTYPE(UInt32,win32more.NetworkManagement.Rras.HRASCONN,UInt32,POINTER(win32more.NetworkManagement.Rras.HRASCONN), use_last_error=False)(("RasGetSubEntryHandleW", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasGetSubEntryHandle():
    return win32more.NetworkManagement.Rras.RasGetSubEntryHandleW
def _define_RasGetCredentialsA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(win32more.NetworkManagement.Rras.RASCREDENTIALSA_head), use_last_error=False)(("RasGetCredentialsA", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasGetCredentialsW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Rras.RASCREDENTIALSW_head), use_last_error=False)(("RasGetCredentialsW", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasGetCredentials():
    return win32more.NetworkManagement.Rras.RasGetCredentialsW
def _define_RasSetCredentialsA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(win32more.NetworkManagement.Rras.RASCREDENTIALSA_head),win32more.Foundation.BOOL, use_last_error=False)(("RasSetCredentialsA", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasSetCredentialsW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Rras.RASCREDENTIALSW_head),win32more.Foundation.BOOL, use_last_error=False)(("RasSetCredentialsW", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasSetCredentials():
    return win32more.NetworkManagement.Rras.RasSetCredentialsW
def _define_RasGetSubEntryPropertiesA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32,POINTER(win32more.NetworkManagement.Rras.RASSUBENTRYA_head),POINTER(UInt32),c_char_p_no,POINTER(UInt32), use_last_error=False)(("RasGetSubEntryPropertiesA", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),(1, 'param4'),(1, 'param5'),(1, 'param6'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasGetSubEntryPropertiesW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.NetworkManagement.Rras.RASSUBENTRYW_head),POINTER(UInt32),c_char_p_no,POINTER(UInt32), use_last_error=False)(("RasGetSubEntryPropertiesW", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),(1, 'param4'),(1, 'param5'),(1, 'param6'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasGetSubEntryProperties():
    return win32more.NetworkManagement.Rras.RasGetSubEntryPropertiesW
def _define_RasSetSubEntryPropertiesA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32,POINTER(win32more.NetworkManagement.Rras.RASSUBENTRYA_head),UInt32,c_char_p_no,UInt32, use_last_error=False)(("RasSetSubEntryPropertiesA", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),(1, 'param4'),(1, 'param5'),(1, 'param6'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasSetSubEntryPropertiesW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.NetworkManagement.Rras.RASSUBENTRYW_head),UInt32,c_char_p_no,UInt32, use_last_error=False)(("RasSetSubEntryPropertiesW", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),(1, 'param4'),(1, 'param5'),(1, 'param6'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasSetSubEntryProperties():
    return win32more.NetworkManagement.Rras.RasSetSubEntryPropertiesW
def _define_RasGetAutodialAddressA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,POINTER(UInt32),POINTER(win32more.NetworkManagement.Rras.RASAUTODIALENTRYA_head),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("RasGetAutodialAddressA", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),(1, 'param4'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasGetAutodialAddressW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(win32more.NetworkManagement.Rras.RASAUTODIALENTRYW_head),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("RasGetAutodialAddressW", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),(1, 'param4'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasGetAutodialAddress():
    return win32more.NetworkManagement.Rras.RasGetAutodialAddressW
def _define_RasSetAutodialAddressA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,UInt32,POINTER(win32more.NetworkManagement.Rras.RASAUTODIALENTRYA_head),UInt32,UInt32, use_last_error=False)(("RasSetAutodialAddressA", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),(1, 'param4'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasSetAutodialAddressW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.NetworkManagement.Rras.RASAUTODIALENTRYW_head),UInt32,UInt32, use_last_error=False)(("RasSetAutodialAddressW", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),(1, 'param4'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasSetAutodialAddress():
    return win32more.NetworkManagement.Rras.RasSetAutodialAddressW
def _define_RasEnumAutodialAddressesA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Foundation.PSTR),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("RasEnumAutodialAddressesA", windll["RASAPI32"]), ((1, 'lppRasAutodialAddresses'),(1, 'lpdwcbRasAutodialAddresses'),(1, 'lpdwcRasAutodialAddresses'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasEnumAutodialAddressesW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Foundation.PWSTR),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("RasEnumAutodialAddressesW", windll["RASAPI32"]), ((1, 'lppRasAutodialAddresses'),(1, 'lpdwcbRasAutodialAddresses'),(1, 'lpdwcRasAutodialAddresses'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasEnumAutodialAddresses():
    return win32more.NetworkManagement.Rras.RasEnumAutodialAddressesW
def _define_RasGetAutodialEnableA():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(Int32), use_last_error=False)(("RasGetAutodialEnableA", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasGetAutodialEnableW():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(Int32), use_last_error=False)(("RasGetAutodialEnableW", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasGetAutodialEnable():
    return win32more.NetworkManagement.Rras.RasGetAutodialEnableW
def _define_RasSetAutodialEnableA():
    try:
        return WINFUNCTYPE(UInt32,UInt32,win32more.Foundation.BOOL, use_last_error=False)(("RasSetAutodialEnableA", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasSetAutodialEnableW():
    try:
        return WINFUNCTYPE(UInt32,UInt32,win32more.Foundation.BOOL, use_last_error=False)(("RasSetAutodialEnableW", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasSetAutodialEnable():
    return win32more.NetworkManagement.Rras.RasSetAutodialEnableW
def _define_RasGetAutodialParamA():
    try:
        return WINFUNCTYPE(UInt32,UInt32,c_void_p,POINTER(UInt32), use_last_error=False)(("RasGetAutodialParamA", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasGetAutodialParamW():
    try:
        return WINFUNCTYPE(UInt32,UInt32,c_void_p,POINTER(UInt32), use_last_error=False)(("RasGetAutodialParamW", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasGetAutodialParam():
    return win32more.NetworkManagement.Rras.RasGetAutodialParamW
def _define_RasSetAutodialParamA():
    try:
        return WINFUNCTYPE(UInt32,UInt32,c_void_p,UInt32, use_last_error=False)(("RasSetAutodialParamA", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasSetAutodialParamW():
    try:
        return WINFUNCTYPE(UInt32,UInt32,c_void_p,UInt32, use_last_error=False)(("RasSetAutodialParamW", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasSetAutodialParam():
    return win32more.NetworkManagement.Rras.RasSetAutodialParamW
def _define_RasGetPCscf():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR, use_last_error=False)(("RasGetPCscf", windll["RASAPI32"]), ((1, 'lpszPCscf'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasInvokeEapUI():
    try:
        return WINFUNCTYPE(UInt32,win32more.NetworkManagement.Rras.HRASCONN,UInt32,POINTER(win32more.NetworkManagement.Rras.RASDIALEXTENSIONS_head),win32more.Foundation.HWND, use_last_error=False)(("RasInvokeEapUI", windll["RASAPI32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasGetLinkStatistics():
    try:
        return WINFUNCTYPE(UInt32,win32more.NetworkManagement.Rras.HRASCONN,UInt32,POINTER(win32more.NetworkManagement.Rras.RAS_STATS_head), use_last_error=False)(("RasGetLinkStatistics", windll["RASAPI32"]), ((1, 'hRasConn'),(1, 'dwSubEntry'),(1, 'lpStatistics'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasGetConnectionStatistics():
    try:
        return WINFUNCTYPE(UInt32,win32more.NetworkManagement.Rras.HRASCONN,POINTER(win32more.NetworkManagement.Rras.RAS_STATS_head), use_last_error=False)(("RasGetConnectionStatistics", windll["RASAPI32"]), ((1, 'hRasConn'),(1, 'lpStatistics'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasClearLinkStatistics():
    try:
        return WINFUNCTYPE(UInt32,win32more.NetworkManagement.Rras.HRASCONN,UInt32, use_last_error=False)(("RasClearLinkStatistics", windll["RASAPI32"]), ((1, 'hRasConn'),(1, 'dwSubEntry'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasClearConnectionStatistics():
    try:
        return WINFUNCTYPE(UInt32,win32more.NetworkManagement.Rras.HRASCONN, use_last_error=False)(("RasClearConnectionStatistics", windll["RASAPI32"]), ((1, 'hRasConn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasGetEapUserDataA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,win32more.Foundation.PSTR,c_char_p_no,POINTER(UInt32), use_last_error=False)(("RasGetEapUserDataA", windll["RASAPI32"]), ((1, 'hToken'),(1, 'pszPhonebook'),(1, 'pszEntry'),(1, 'pbEapData'),(1, 'pdwSizeofEapData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasGetEapUserDataW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,c_char_p_no,POINTER(UInt32), use_last_error=False)(("RasGetEapUserDataW", windll["RASAPI32"]), ((1, 'hToken'),(1, 'pszPhonebook'),(1, 'pszEntry'),(1, 'pbEapData'),(1, 'pdwSizeofEapData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasGetEapUserData():
    return win32more.NetworkManagement.Rras.RasGetEapUserDataW
def _define_RasSetEapUserDataA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,win32more.Foundation.PSTR,c_char_p_no,UInt32, use_last_error=False)(("RasSetEapUserDataA", windll["RASAPI32"]), ((1, 'hToken'),(1, 'pszPhonebook'),(1, 'pszEntry'),(1, 'pbEapData'),(1, 'dwSizeofEapData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasSetEapUserDataW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,c_char_p_no,UInt32, use_last_error=False)(("RasSetEapUserDataW", windll["RASAPI32"]), ((1, 'hToken'),(1, 'pszPhonebook'),(1, 'pszEntry'),(1, 'pbEapData'),(1, 'dwSizeofEapData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasSetEapUserData():
    return win32more.NetworkManagement.Rras.RasSetEapUserDataW
def _define_RasGetCustomAuthDataA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,c_char_p_no,POINTER(UInt32), use_last_error=False)(("RasGetCustomAuthDataA", windll["RASAPI32"]), ((1, 'pszPhonebook'),(1, 'pszEntry'),(1, 'pbCustomAuthData'),(1, 'pdwSizeofCustomAuthData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasGetCustomAuthDataW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,c_char_p_no,POINTER(UInt32), use_last_error=False)(("RasGetCustomAuthDataW", windll["RASAPI32"]), ((1, 'pszPhonebook'),(1, 'pszEntry'),(1, 'pbCustomAuthData'),(1, 'pdwSizeofCustomAuthData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasGetCustomAuthData():
    return win32more.NetworkManagement.Rras.RasGetCustomAuthDataW
def _define_RasSetCustomAuthDataA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,c_char_p_no,UInt32, use_last_error=False)(("RasSetCustomAuthDataA", windll["RASAPI32"]), ((1, 'pszPhonebook'),(1, 'pszEntry'),(1, 'pbCustomAuthData'),(1, 'dwSizeofCustomAuthData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasSetCustomAuthDataW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,c_char_p_no,UInt32, use_last_error=False)(("RasSetCustomAuthDataW", windll["RASAPI32"]), ((1, 'pszPhonebook'),(1, 'pszEntry'),(1, 'pbCustomAuthData'),(1, 'dwSizeofCustomAuthData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasSetCustomAuthData():
    return win32more.NetworkManagement.Rras.RasSetCustomAuthDataW
def _define_RasGetEapUserIdentityW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.HWND,POINTER(POINTER(win32more.NetworkManagement.Rras.RASEAPUSERIDENTITYW_head)), use_last_error=False)(("RasGetEapUserIdentityW", windll["RASAPI32"]), ((1, 'pszPhonebook'),(1, 'pszEntry'),(1, 'dwFlags'),(1, 'hwnd'),(1, 'ppRasEapUserIdentity'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasGetEapUserIdentity():
    return win32more.NetworkManagement.Rras.RasGetEapUserIdentityW
def _define_RasGetEapUserIdentityA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32,win32more.Foundation.HWND,POINTER(POINTER(win32more.NetworkManagement.Rras.RASEAPUSERIDENTITYA_head)), use_last_error=False)(("RasGetEapUserIdentityA", windll["RASAPI32"]), ((1, 'pszPhonebook'),(1, 'pszEntry'),(1, 'dwFlags'),(1, 'hwnd'),(1, 'ppRasEapUserIdentity'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasFreeEapUserIdentityW():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.NetworkManagement.Rras.RASEAPUSERIDENTITYW_head), use_last_error=False)(("RasFreeEapUserIdentityW", windll["RASAPI32"]), ((1, 'pRasEapUserIdentity'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasFreeEapUserIdentity():
    return win32more.NetworkManagement.Rras.RasFreeEapUserIdentityW
def _define_RasFreeEapUserIdentityA():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.NetworkManagement.Rras.RASEAPUSERIDENTITYA_head), use_last_error=False)(("RasFreeEapUserIdentityA", windll["RASAPI32"]), ((1, 'pRasEapUserIdentity'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasDeleteSubEntryA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32, use_last_error=False)(("RasDeleteSubEntryA", windll["RASAPI32"]), ((1, 'pszPhonebook'),(1, 'pszEntry'),(1, 'dwSubentryId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasDeleteSubEntryW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(("RasDeleteSubEntryW", windll["RASAPI32"]), ((1, 'pszPhonebook'),(1, 'pszEntry'),(1, 'dwSubEntryId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasDeleteSubEntry():
    return win32more.NetworkManagement.Rras.RasDeleteSubEntryW
def _define_RasUpdateConnection():
    try:
        return WINFUNCTYPE(UInt32,win32more.NetworkManagement.Rras.HRASCONN,POINTER(win32more.NetworkManagement.Rras.RASUPDATECONN_head), use_last_error=False)(("RasUpdateConnection", windll["RASAPI32"]), ((1, 'hrasconn'),(1, 'lprasupdateconn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasGetProjectionInfoEx():
    try:
        return WINFUNCTYPE(UInt32,win32more.NetworkManagement.Rras.HRASCONN,POINTER(win32more.NetworkManagement.Rras.RAS_PROJECTION_INFO_head),POINTER(UInt32), use_last_error=False)(("RasGetProjectionInfoEx", windll["RASAPI32"]), ((1, 'hrasconn'),(1, 'pRasProjection'),(1, 'lpdwSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasPhonebookDlgA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(win32more.NetworkManagement.Rras.RASPBDLGA_head), use_last_error=False)(("RasPhonebookDlgA", windll["RASDLG"]), ((1, 'lpszPhonebook'),(1, 'lpszEntry'),(1, 'lpInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasPhonebookDlgW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Rras.RASPBDLGW_head), use_last_error=False)(("RasPhonebookDlgW", windll["RASDLG"]), ((1, 'lpszPhonebook'),(1, 'lpszEntry'),(1, 'lpInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasPhonebookDlg():
    return win32more.NetworkManagement.Rras.RasPhonebookDlgW
def _define_RasEntryDlgA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(win32more.NetworkManagement.Rras.RASENTRYDLGA_head), use_last_error=False)(("RasEntryDlgA", windll["RASDLG"]), ((1, 'lpszPhonebook'),(1, 'lpszEntry'),(1, 'lpInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasEntryDlgW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Rras.RASENTRYDLGW_head), use_last_error=False)(("RasEntryDlgW", windll["RASDLG"]), ((1, 'lpszPhonebook'),(1, 'lpszEntry'),(1, 'lpInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasEntryDlg():
    return win32more.NetworkManagement.Rras.RasEntryDlgW
def _define_RasDialDlgA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(win32more.NetworkManagement.Rras.RASDIALDLG_head), use_last_error=False)(("RasDialDlgA", windll["RASDLG"]), ((1, 'lpszPhonebook'),(1, 'lpszEntry'),(1, 'lpszPhoneNumber'),(1, 'lpInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasDialDlgW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Rras.RASDIALDLG_head), use_last_error=False)(("RasDialDlgW", windll["RASDLG"]), ((1, 'lpszPhonebook'),(1, 'lpszEntry'),(1, 'lpszPhoneNumber'),(1, 'lpInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RasDialDlg():
    return win32more.NetworkManagement.Rras.RasDialDlgW
def _define_MprAdminConnectionEnumEx():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,POINTER(win32more.NetworkManagement.Rras.MPRAPI_OBJECT_HEADER_head),UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(POINTER(win32more.NetworkManagement.Rras.RAS_CONNECTION_EX_head)),POINTER(UInt32), use_last_error=False)(("MprAdminConnectionEnumEx", windll["MPRAPI"]), ((1, 'hRasServer'),(1, 'pObjectHeader'),(1, 'dwPreferedMaxLen'),(1, 'lpdwEntriesRead'),(1, 'lpdwTotalEntries'),(1, 'ppRasConn'),(1, 'lpdwResumeHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminConnectionGetInfoEx():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,win32more.Foundation.HANDLE,POINTER(win32more.NetworkManagement.Rras.RAS_CONNECTION_EX_head), use_last_error=False)(("MprAdminConnectionGetInfoEx", windll["MPRAPI"]), ((1, 'hRasServer'),(1, 'hRasConnection'),(1, 'pRasConnection'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminServerGetInfoEx():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,POINTER(win32more.NetworkManagement.Rras.MPR_SERVER_EX1_head), use_last_error=False)(("MprAdminServerGetInfoEx", windll["MPRAPI"]), ((1, 'hMprServer'),(1, 'pServerInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminServerSetInfoEx():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,POINTER(win32more.NetworkManagement.Rras.MPR_SERVER_SET_CONFIG_EX1_head), use_last_error=False)(("MprAdminServerSetInfoEx", windll["MPRAPI"]), ((1, 'hMprServer'),(1, 'pServerInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprConfigServerGetInfoEx():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(win32more.NetworkManagement.Rras.MPR_SERVER_EX1_head), use_last_error=False)(("MprConfigServerGetInfoEx", windll["MPRAPI"]), ((1, 'hMprConfig'),(1, 'pServerInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprConfigServerSetInfoEx():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(win32more.NetworkManagement.Rras.MPR_SERVER_SET_CONFIG_EX1_head), use_last_error=False)(("MprConfigServerSetInfoEx", windll["MPRAPI"]), ((1, 'hMprConfig'),(1, 'pSetServerConfig'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminUpdateConnection():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,win32more.Foundation.HANDLE,POINTER(win32more.NetworkManagement.Rras.RAS_UPDATE_CONNECTION_head), use_last_error=False)(("MprAdminUpdateConnection", windll["MPRAPI"]), ((1, 'hRasServer'),(1, 'hRasConnection'),(1, 'pRasUpdateConnection'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminIsServiceInitialized():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.BOOL), use_last_error=False)(("MprAdminIsServiceInitialized", windll["MPRAPI"]), ((1, 'lpwsServerName'),(1, 'fIsServiceInitialized'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminInterfaceSetCustomInfoEx():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,win32more.Foundation.HANDLE,POINTER(win32more.NetworkManagement.Rras.MPR_IF_CUSTOMINFOEX2_head), use_last_error=False)(("MprAdminInterfaceSetCustomInfoEx", windll["MPRAPI"]), ((1, 'hMprServer'),(1, 'hInterface'),(1, 'pCustomInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminInterfaceGetCustomInfoEx():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,win32more.Foundation.HANDLE,POINTER(win32more.NetworkManagement.Rras.MPR_IF_CUSTOMINFOEX2_head), use_last_error=False)(("MprAdminInterfaceGetCustomInfoEx", windll["MPRAPI"]), ((1, 'hMprServer'),(1, 'hInterface'),(1, 'pCustomInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprConfigInterfaceGetCustomInfoEx():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,POINTER(win32more.NetworkManagement.Rras.MPR_IF_CUSTOMINFOEX2_head), use_last_error=False)(("MprConfigInterfaceGetCustomInfoEx", windll["MPRAPI"]), ((1, 'hMprConfig'),(1, 'hRouterInterface'),(1, 'pCustomInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprConfigInterfaceSetCustomInfoEx():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,POINTER(win32more.NetworkManagement.Rras.MPR_IF_CUSTOMINFOEX2_head), use_last_error=False)(("MprConfigInterfaceSetCustomInfoEx", windll["MPRAPI"]), ((1, 'hMprConfig'),(1, 'hRouterInterface'),(1, 'pCustomInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminConnectionEnum():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,UInt32,POINTER(c_char_p_no),UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("MprAdminConnectionEnum", windll["MPRAPI"]), ((1, 'hRasServer'),(1, 'dwLevel'),(1, 'lplpbBuffer'),(1, 'dwPrefMaxLen'),(1, 'lpdwEntriesRead'),(1, 'lpdwTotalEntries'),(1, 'lpdwResumeHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminPortEnum():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,UInt32,win32more.Foundation.HANDLE,POINTER(c_char_p_no),UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("MprAdminPortEnum", windll["MPRAPI"]), ((1, 'hRasServer'),(1, 'dwLevel'),(1, 'hRasConnection'),(1, 'lplpbBuffer'),(1, 'dwPrefMaxLen'),(1, 'lpdwEntriesRead'),(1, 'lpdwTotalEntries'),(1, 'lpdwResumeHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminConnectionGetInfo():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,UInt32,win32more.Foundation.HANDLE,POINTER(c_char_p_no), use_last_error=False)(("MprAdminConnectionGetInfo", windll["MPRAPI"]), ((1, 'hRasServer'),(1, 'dwLevel'),(1, 'hRasConnection'),(1, 'lplpbBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminPortGetInfo():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,UInt32,win32more.Foundation.HANDLE,POINTER(c_char_p_no), use_last_error=False)(("MprAdminPortGetInfo", windll["MPRAPI"]), ((1, 'hRasServer'),(1, 'dwLevel'),(1, 'hPort'),(1, 'lplpbBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminConnectionClearStats():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,win32more.Foundation.HANDLE, use_last_error=False)(("MprAdminConnectionClearStats", windll["MPRAPI"]), ((1, 'hRasServer'),(1, 'hRasConnection'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminPortClearStats():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,win32more.Foundation.HANDLE, use_last_error=False)(("MprAdminPortClearStats", windll["MPRAPI"]), ((1, 'hRasServer'),(1, 'hPort'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminPortReset():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,win32more.Foundation.HANDLE, use_last_error=False)(("MprAdminPortReset", windll["MPRAPI"]), ((1, 'hRasServer'),(1, 'hPort'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminPortDisconnect():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,win32more.Foundation.HANDLE, use_last_error=False)(("MprAdminPortDisconnect", windll["MPRAPI"]), ((1, 'hRasServer'),(1, 'hPort'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminConnectionRemoveQuarantine():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,win32more.Foundation.BOOL, use_last_error=False)(("MprAdminConnectionRemoveQuarantine", windll["MPRAPI"]), ((1, 'hRasServer'),(1, 'hRasConnection'),(1, 'fIsIpAddress'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminUserGetInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,c_char_p_no, use_last_error=False)(("MprAdminUserGetInfo", windll["MPRAPI"]), ((1, 'lpszServer'),(1, 'lpszUser'),(1, 'dwLevel'),(1, 'lpbBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminUserSetInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,c_char_p_no, use_last_error=False)(("MprAdminUserSetInfo", windll["MPRAPI"]), ((1, 'lpszServer'),(1, 'lpszUser'),(1, 'dwLevel'),(1, 'lpbBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminSendUserMessage():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR, use_last_error=False)(("MprAdminSendUserMessage", windll["MPRAPI"]), ((1, 'hMprServer'),(1, 'hConnection'),(1, 'lpwszMessage'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminGetPDCServer():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("MprAdminGetPDCServer", windll["MPRAPI"]), ((1, 'lpszDomain'),(1, 'lpszServer'),(1, 'lpszPDCServer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminIsServiceRunning():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR, use_last_error=False)(("MprAdminIsServiceRunning", windll["MPRAPI"]), ((1, 'lpwsServerName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminServerConnect():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(IntPtr), use_last_error=False)(("MprAdminServerConnect", windll["MPRAPI"]), ((1, 'lpwsServerName'),(1, 'phMprServer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminServerDisconnect():
    try:
        return WINFUNCTYPE(Void,IntPtr, use_last_error=False)(("MprAdminServerDisconnect", windll["MPRAPI"]), ((1, 'hMprServer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminServerGetCredentials():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,UInt32,POINTER(c_char_p_no), use_last_error=False)(("MprAdminServerGetCredentials", windll["MPRAPI"]), ((1, 'hMprServer'),(1, 'dwLevel'),(1, 'lplpbBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminServerSetCredentials():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,UInt32,c_char_p_no, use_last_error=False)(("MprAdminServerSetCredentials", windll["MPRAPI"]), ((1, 'hMprServer'),(1, 'dwLevel'),(1, 'lpbBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminBufferFree():
    try:
        return WINFUNCTYPE(UInt32,c_void_p, use_last_error=False)(("MprAdminBufferFree", windll["MPRAPI"]), ((1, 'pBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminGetErrorString():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("MprAdminGetErrorString", windll["MPRAPI"]), ((1, 'dwError'),(1, 'lplpwsErrorString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminServerGetInfo():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,UInt32,POINTER(c_char_p_no), use_last_error=False)(("MprAdminServerGetInfo", windll["MPRAPI"]), ((1, 'hMprServer'),(1, 'dwLevel'),(1, 'lplpbBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminServerSetInfo():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,UInt32,c_char_p_no, use_last_error=False)(("MprAdminServerSetInfo", windll["MPRAPI"]), ((1, 'hMprServer'),(1, 'dwLevel'),(1, 'lpbBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminEstablishDomainRasServer():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.BOOL, use_last_error=False)(("MprAdminEstablishDomainRasServer", windll["MPRAPI"]), ((1, 'pszDomain'),(1, 'pszMachine'),(1, 'bEnable'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminIsDomainRasServer():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.BOOL), use_last_error=False)(("MprAdminIsDomainRasServer", windll["MPRAPI"]), ((1, 'pszDomain'),(1, 'pszMachine'),(1, 'pbIsRasServer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminTransportCreate():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,UInt32,win32more.Foundation.PWSTR,c_char_p_no,UInt32,c_char_p_no,UInt32,win32more.Foundation.PWSTR, use_last_error=False)(("MprAdminTransportCreate", windll["MPRAPI"]), ((1, 'hMprServer'),(1, 'dwTransportId'),(1, 'lpwsTransportName'),(1, 'pGlobalInfo'),(1, 'dwGlobalInfoSize'),(1, 'pClientInterfaceInfo'),(1, 'dwClientInterfaceInfoSize'),(1, 'lpwsDLLPath'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminTransportSetInfo():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,UInt32,c_char_p_no,UInt32,c_char_p_no,UInt32, use_last_error=False)(("MprAdminTransportSetInfo", windll["MPRAPI"]), ((1, 'hMprServer'),(1, 'dwTransportId'),(1, 'pGlobalInfo'),(1, 'dwGlobalInfoSize'),(1, 'pClientInterfaceInfo'),(1, 'dwClientInterfaceInfoSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminTransportGetInfo():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,UInt32,POINTER(c_char_p_no),POINTER(UInt32),POINTER(c_char_p_no),POINTER(UInt32), use_last_error=False)(("MprAdminTransportGetInfo", windll["MPRAPI"]), ((1, 'hMprServer'),(1, 'dwTransportId'),(1, 'ppGlobalInfo'),(1, 'lpdwGlobalInfoSize'),(1, 'ppClientInterfaceInfo'),(1, 'lpdwClientInterfaceInfoSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminDeviceEnum():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,UInt32,POINTER(c_char_p_no),POINTER(UInt32), use_last_error=False)(("MprAdminDeviceEnum", windll["MPRAPI"]), ((1, 'hMprServer'),(1, 'dwLevel'),(1, 'lplpbBuffer'),(1, 'lpdwTotalEntries'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminInterfaceGetHandle():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.HANDLE),win32more.Foundation.BOOL, use_last_error=False)(("MprAdminInterfaceGetHandle", windll["MPRAPI"]), ((1, 'hMprServer'),(1, 'lpwsInterfaceName'),(1, 'phInterface'),(1, 'fIncludeClientInterfaces'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminInterfaceCreate():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,UInt32,c_char_p_no,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("MprAdminInterfaceCreate", windll["MPRAPI"]), ((1, 'hMprServer'),(1, 'dwLevel'),(1, 'lpbBuffer'),(1, 'phInterface'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminInterfaceGetInfo():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,win32more.Foundation.HANDLE,UInt32,POINTER(c_char_p_no), use_last_error=False)(("MprAdminInterfaceGetInfo", windll["MPRAPI"]), ((1, 'hMprServer'),(1, 'hInterface'),(1, 'dwLevel'),(1, 'lplpbBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminInterfaceSetInfo():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,win32more.Foundation.HANDLE,UInt32,c_char_p_no, use_last_error=False)(("MprAdminInterfaceSetInfo", windll["MPRAPI"]), ((1, 'hMprServer'),(1, 'hInterface'),(1, 'dwLevel'),(1, 'lpbBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminInterfaceDelete():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,win32more.Foundation.HANDLE, use_last_error=False)(("MprAdminInterfaceDelete", windll["MPRAPI"]), ((1, 'hMprServer'),(1, 'hInterface'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminInterfaceDeviceGetInfo():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,win32more.Foundation.HANDLE,UInt32,UInt32,POINTER(c_char_p_no), use_last_error=False)(("MprAdminInterfaceDeviceGetInfo", windll["MPRAPI"]), ((1, 'hMprServer'),(1, 'hInterface'),(1, 'dwIndex'),(1, 'dwLevel'),(1, 'lplpBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminInterfaceDeviceSetInfo():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,win32more.Foundation.HANDLE,UInt32,UInt32,c_char_p_no, use_last_error=False)(("MprAdminInterfaceDeviceSetInfo", windll["MPRAPI"]), ((1, 'hMprServer'),(1, 'hInterface'),(1, 'dwIndex'),(1, 'dwLevel'),(1, 'lpbBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminInterfaceTransportRemove():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,win32more.Foundation.HANDLE,UInt32, use_last_error=False)(("MprAdminInterfaceTransportRemove", windll["MPRAPI"]), ((1, 'hMprServer'),(1, 'hInterface'),(1, 'dwTransportId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminInterfaceTransportAdd():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,win32more.Foundation.HANDLE,UInt32,c_char_p_no,UInt32, use_last_error=False)(("MprAdminInterfaceTransportAdd", windll["MPRAPI"]), ((1, 'hMprServer'),(1, 'hInterface'),(1, 'dwTransportId'),(1, 'pInterfaceInfo'),(1, 'dwInterfaceInfoSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminInterfaceTransportGetInfo():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,win32more.Foundation.HANDLE,UInt32,POINTER(c_char_p_no),POINTER(UInt32), use_last_error=False)(("MprAdminInterfaceTransportGetInfo", windll["MPRAPI"]), ((1, 'hMprServer'),(1, 'hInterface'),(1, 'dwTransportId'),(1, 'ppInterfaceInfo'),(1, 'lpdwInterfaceInfoSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminInterfaceTransportSetInfo():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,win32more.Foundation.HANDLE,UInt32,c_char_p_no,UInt32, use_last_error=False)(("MprAdminInterfaceTransportSetInfo", windll["MPRAPI"]), ((1, 'hMprServer'),(1, 'hInterface'),(1, 'dwTransportId'),(1, 'pInterfaceInfo'),(1, 'dwInterfaceInfoSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminInterfaceEnum():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,UInt32,POINTER(c_char_p_no),UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("MprAdminInterfaceEnum", windll["MPRAPI"]), ((1, 'hMprServer'),(1, 'dwLevel'),(1, 'lplpbBuffer'),(1, 'dwPrefMaxLen'),(1, 'lpdwEntriesRead'),(1, 'lpdwTotalEntries'),(1, 'lpdwResumeHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminInterfaceSetCredentials():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("MprAdminInterfaceSetCredentials", windll["MPRAPI"]), ((1, 'lpwsServer'),(1, 'lpwsInterfaceName'),(1, 'lpwsUserName'),(1, 'lpwsDomainName'),(1, 'lpwsPassword'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminInterfaceGetCredentials():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("MprAdminInterfaceGetCredentials", windll["MPRAPI"]), ((1, 'lpwsServer'),(1, 'lpwsInterfaceName'),(1, 'lpwsUserName'),(1, 'lpwsPassword'),(1, 'lpwsDomainName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminInterfaceSetCredentialsEx():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,win32more.Foundation.HANDLE,UInt32,c_char_p_no, use_last_error=False)(("MprAdminInterfaceSetCredentialsEx", windll["MPRAPI"]), ((1, 'hMprServer'),(1, 'hInterface'),(1, 'dwLevel'),(1, 'lpbBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminInterfaceGetCredentialsEx():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,win32more.Foundation.HANDLE,UInt32,POINTER(c_char_p_no), use_last_error=False)(("MprAdminInterfaceGetCredentialsEx", windll["MPRAPI"]), ((1, 'hMprServer'),(1, 'hInterface'),(1, 'dwLevel'),(1, 'lplpbBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminInterfaceConnect():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,win32more.Foundation.BOOL, use_last_error=False)(("MprAdminInterfaceConnect", windll["MPRAPI"]), ((1, 'hMprServer'),(1, 'hInterface'),(1, 'hEvent'),(1, 'fSynchronous'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminInterfaceDisconnect():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,win32more.Foundation.HANDLE, use_last_error=False)(("MprAdminInterfaceDisconnect", windll["MPRAPI"]), ((1, 'hMprServer'),(1, 'hInterface'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminInterfaceUpdateRoutes():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,win32more.Foundation.HANDLE,UInt32,win32more.Foundation.HANDLE, use_last_error=False)(("MprAdminInterfaceUpdateRoutes", windll["MPRAPI"]), ((1, 'hMprServer'),(1, 'hInterface'),(1, 'dwProtocolId'),(1, 'hEvent'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminInterfaceQueryUpdateResult():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,win32more.Foundation.HANDLE,UInt32,POINTER(UInt32), use_last_error=False)(("MprAdminInterfaceQueryUpdateResult", windll["MPRAPI"]), ((1, 'hMprServer'),(1, 'hInterface'),(1, 'dwProtocolId'),(1, 'lpdwUpdateResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminInterfaceUpdatePhonebookInfo():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,win32more.Foundation.HANDLE, use_last_error=False)(("MprAdminInterfaceUpdatePhonebookInfo", windll["MPRAPI"]), ((1, 'hMprServer'),(1, 'hInterface'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminRegisterConnectionNotification():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,win32more.Foundation.HANDLE, use_last_error=False)(("MprAdminRegisterConnectionNotification", windll["MPRAPI"]), ((1, 'hMprServer'),(1, 'hEventNotification'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminDeregisterConnectionNotification():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,win32more.Foundation.HANDLE, use_last_error=False)(("MprAdminDeregisterConnectionNotification", windll["MPRAPI"]), ((1, 'hMprServer'),(1, 'hEventNotification'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminMIBServerConnect():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(IntPtr), use_last_error=False)(("MprAdminMIBServerConnect", windll["MPRAPI"]), ((1, 'lpwsServerName'),(1, 'phMibServer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminMIBServerDisconnect():
    try:
        return WINFUNCTYPE(Void,IntPtr, use_last_error=False)(("MprAdminMIBServerDisconnect", windll["MPRAPI"]), ((1, 'hMibServer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminMIBEntryCreate():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,UInt32,UInt32,c_void_p,UInt32, use_last_error=False)(("MprAdminMIBEntryCreate", windll["MPRAPI"]), ((1, 'hMibServer'),(1, 'dwPid'),(1, 'dwRoutingPid'),(1, 'lpEntry'),(1, 'dwEntrySize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminMIBEntryDelete():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,UInt32,UInt32,c_void_p,UInt32, use_last_error=False)(("MprAdminMIBEntryDelete", windll["MPRAPI"]), ((1, 'hMibServer'),(1, 'dwProtocolId'),(1, 'dwRoutingPid'),(1, 'lpEntry'),(1, 'dwEntrySize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminMIBEntrySet():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,UInt32,UInt32,c_void_p,UInt32, use_last_error=False)(("MprAdminMIBEntrySet", windll["MPRAPI"]), ((1, 'hMibServer'),(1, 'dwProtocolId'),(1, 'dwRoutingPid'),(1, 'lpEntry'),(1, 'dwEntrySize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminMIBEntryGet():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,UInt32,UInt32,c_void_p,UInt32,POINTER(c_void_p),POINTER(UInt32), use_last_error=False)(("MprAdminMIBEntryGet", windll["MPRAPI"]), ((1, 'hMibServer'),(1, 'dwProtocolId'),(1, 'dwRoutingPid'),(1, 'lpInEntry'),(1, 'dwInEntrySize'),(1, 'lplpOutEntry'),(1, 'lpOutEntrySize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminMIBEntryGetFirst():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,UInt32,UInt32,c_void_p,UInt32,POINTER(c_void_p),POINTER(UInt32), use_last_error=False)(("MprAdminMIBEntryGetFirst", windll["MPRAPI"]), ((1, 'hMibServer'),(1, 'dwProtocolId'),(1, 'dwRoutingPid'),(1, 'lpInEntry'),(1, 'dwInEntrySize'),(1, 'lplpOutEntry'),(1, 'lpOutEntrySize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminMIBEntryGetNext():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,UInt32,UInt32,c_void_p,UInt32,POINTER(c_void_p),POINTER(UInt32), use_last_error=False)(("MprAdminMIBEntryGetNext", windll["MPRAPI"]), ((1, 'hMibServer'),(1, 'dwProtocolId'),(1, 'dwRoutingPid'),(1, 'lpInEntry'),(1, 'dwInEntrySize'),(1, 'lplpOutEntry'),(1, 'lpOutEntrySize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprAdminMIBBufferFree():
    try:
        return WINFUNCTYPE(UInt32,c_void_p, use_last_error=False)(("MprAdminMIBBufferFree", windll["MPRAPI"]), ((1, 'pBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprConfigServerInstall():
    try:
        return WINFUNCTYPE(UInt32,UInt32,c_void_p, use_last_error=False)(("MprConfigServerInstall", windll["MPRAPI"]), ((1, 'dwLevel'),(1, 'pBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprConfigServerConnect():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("MprConfigServerConnect", windll["MPRAPI"]), ((1, 'lpwsServerName'),(1, 'phMprConfig'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprConfigServerDisconnect():
    try:
        return WINFUNCTYPE(Void,win32more.Foundation.HANDLE, use_last_error=False)(("MprConfigServerDisconnect", windll["MPRAPI"]), ((1, 'hMprConfig'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprConfigServerRefresh():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE, use_last_error=False)(("MprConfigServerRefresh", windll["MPRAPI"]), ((1, 'hMprConfig'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprConfigBufferFree():
    try:
        return WINFUNCTYPE(UInt32,c_void_p, use_last_error=False)(("MprConfigBufferFree", windll["MPRAPI"]), ((1, 'pBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprConfigServerGetInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt32,POINTER(c_char_p_no), use_last_error=False)(("MprConfigServerGetInfo", windll["MPRAPI"]), ((1, 'hMprConfig'),(1, 'dwLevel'),(1, 'lplpbBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprConfigServerSetInfo():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,UInt32,c_char_p_no, use_last_error=False)(("MprConfigServerSetInfo", windll["MPRAPI"]), ((1, 'hMprServer'),(1, 'dwLevel'),(1, 'lpbBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprConfigServerBackup():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR, use_last_error=False)(("MprConfigServerBackup", windll["MPRAPI"]), ((1, 'hMprConfig'),(1, 'lpwsPath'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprConfigServerRestore():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR, use_last_error=False)(("MprConfigServerRestore", windll["MPRAPI"]), ((1, 'hMprConfig'),(1, 'lpwsPath'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprConfigTransportCreate():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt32,win32more.Foundation.PWSTR,c_char_p_no,UInt32,c_char_p_no,UInt32,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("MprConfigTransportCreate", windll["MPRAPI"]), ((1, 'hMprConfig'),(1, 'dwTransportId'),(1, 'lpwsTransportName'),(1, 'pGlobalInfo'),(1, 'dwGlobalInfoSize'),(1, 'pClientInterfaceInfo'),(1, 'dwClientInterfaceInfoSize'),(1, 'lpwsDLLPath'),(1, 'phRouterTransport'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprConfigTransportDelete():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE, use_last_error=False)(("MprConfigTransportDelete", windll["MPRAPI"]), ((1, 'hMprConfig'),(1, 'hRouterTransport'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprConfigTransportGetHandle():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt32,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("MprConfigTransportGetHandle", windll["MPRAPI"]), ((1, 'hMprConfig'),(1, 'dwTransportId'),(1, 'phRouterTransport'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprConfigTransportSetInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,c_char_p_no,UInt32,c_char_p_no,UInt32,win32more.Foundation.PWSTR, use_last_error=False)(("MprConfigTransportSetInfo", windll["MPRAPI"]), ((1, 'hMprConfig'),(1, 'hRouterTransport'),(1, 'pGlobalInfo'),(1, 'dwGlobalInfoSize'),(1, 'pClientInterfaceInfo'),(1, 'dwClientInterfaceInfoSize'),(1, 'lpwsDLLPath'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprConfigTransportGetInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,POINTER(c_char_p_no),POINTER(UInt32),POINTER(c_char_p_no),POINTER(UInt32),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("MprConfigTransportGetInfo", windll["MPRAPI"]), ((1, 'hMprConfig'),(1, 'hRouterTransport'),(1, 'ppGlobalInfo'),(1, 'lpdwGlobalInfoSize'),(1, 'ppClientInterfaceInfo'),(1, 'lpdwClientInterfaceInfoSize'),(1, 'lplpwsDLLPath'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprConfigTransportEnum():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt32,POINTER(c_char_p_no),UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("MprConfigTransportEnum", windll["MPRAPI"]), ((1, 'hMprConfig'),(1, 'dwLevel'),(1, 'lplpBuffer'),(1, 'dwPrefMaxLen'),(1, 'lpdwEntriesRead'),(1, 'lpdwTotalEntries'),(1, 'lpdwResumeHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprConfigInterfaceCreate():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt32,c_char_p_no,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("MprConfigInterfaceCreate", windll["MPRAPI"]), ((1, 'hMprConfig'),(1, 'dwLevel'),(1, 'lpbBuffer'),(1, 'phRouterInterface'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprConfigInterfaceDelete():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE, use_last_error=False)(("MprConfigInterfaceDelete", windll["MPRAPI"]), ((1, 'hMprConfig'),(1, 'hRouterInterface'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprConfigInterfaceGetHandle():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("MprConfigInterfaceGetHandle", windll["MPRAPI"]), ((1, 'hMprConfig'),(1, 'lpwsInterfaceName'),(1, 'phRouterInterface'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprConfigInterfaceGetInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,UInt32,POINTER(c_char_p_no),POINTER(UInt32), use_last_error=False)(("MprConfigInterfaceGetInfo", windll["MPRAPI"]), ((1, 'hMprConfig'),(1, 'hRouterInterface'),(1, 'dwLevel'),(1, 'lplpBuffer'),(1, 'lpdwBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprConfigInterfaceSetInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,UInt32,c_char_p_no, use_last_error=False)(("MprConfigInterfaceSetInfo", windll["MPRAPI"]), ((1, 'hMprConfig'),(1, 'hRouterInterface'),(1, 'dwLevel'),(1, 'lpbBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprConfigInterfaceEnum():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt32,POINTER(c_char_p_no),UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("MprConfigInterfaceEnum", windll["MPRAPI"]), ((1, 'hMprConfig'),(1, 'dwLevel'),(1, 'lplpBuffer'),(1, 'dwPrefMaxLen'),(1, 'lpdwEntriesRead'),(1, 'lpdwTotalEntries'),(1, 'lpdwResumeHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprConfigInterfaceTransportAdd():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,UInt32,win32more.Foundation.PWSTR,c_char_p_no,UInt32,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("MprConfigInterfaceTransportAdd", windll["MPRAPI"]), ((1, 'hMprConfig'),(1, 'hRouterInterface'),(1, 'dwTransportId'),(1, 'lpwsTransportName'),(1, 'pInterfaceInfo'),(1, 'dwInterfaceInfoSize'),(1, 'phRouterIfTransport'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprConfigInterfaceTransportRemove():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE, use_last_error=False)(("MprConfigInterfaceTransportRemove", windll["MPRAPI"]), ((1, 'hMprConfig'),(1, 'hRouterInterface'),(1, 'hRouterIfTransport'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprConfigInterfaceTransportGetHandle():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,UInt32,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("MprConfigInterfaceTransportGetHandle", windll["MPRAPI"]), ((1, 'hMprConfig'),(1, 'hRouterInterface'),(1, 'dwTransportId'),(1, 'phRouterIfTransport'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprConfigInterfaceTransportGetInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,POINTER(c_char_p_no),POINTER(UInt32), use_last_error=False)(("MprConfigInterfaceTransportGetInfo", windll["MPRAPI"]), ((1, 'hMprConfig'),(1, 'hRouterInterface'),(1, 'hRouterIfTransport'),(1, 'ppInterfaceInfo'),(1, 'lpdwInterfaceInfoSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprConfigInterfaceTransportSetInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,c_char_p_no,UInt32, use_last_error=False)(("MprConfigInterfaceTransportSetInfo", windll["MPRAPI"]), ((1, 'hMprConfig'),(1, 'hRouterInterface'),(1, 'hRouterIfTransport'),(1, 'pInterfaceInfo'),(1, 'dwInterfaceInfoSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprConfigInterfaceTransportEnum():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,UInt32,POINTER(c_char_p_no),UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("MprConfigInterfaceTransportEnum", windll["MPRAPI"]), ((1, 'hMprConfig'),(1, 'hRouterInterface'),(1, 'dwLevel'),(1, 'lplpBuffer'),(1, 'dwPrefMaxLen'),(1, 'lpdwEntriesRead'),(1, 'lpdwTotalEntries'),(1, 'lpdwResumeHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprConfigGetFriendlyName():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(("MprConfigGetFriendlyName", windll["MPRAPI"]), ((1, 'hMprConfig'),(1, 'pszGuidName'),(1, 'pszBuffer'),(1, 'dwBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprConfigGetGuidName():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(("MprConfigGetGuidName", windll["MPRAPI"]), ((1, 'hMprConfig'),(1, 'pszFriendlyName'),(1, 'pszBuffer'),(1, 'dwBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprConfigFilterGetInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt32,UInt32,c_char_p_no, use_last_error=False)(("MprConfigFilterGetInfo", windll["MPRAPI"]), ((1, 'hMprConfig'),(1, 'dwLevel'),(1, 'dwTransportId'),(1, 'lpBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprConfigFilterSetInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt32,UInt32,c_char_p_no, use_last_error=False)(("MprConfigFilterSetInfo", windll["MPRAPI"]), ((1, 'hMprConfig'),(1, 'dwLevel'),(1, 'dwTransportId'),(1, 'lpBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprInfoCreate():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(c_void_p), use_last_error=False)(("MprInfoCreate", windll["MPRAPI"]), ((1, 'dwVersion'),(1, 'lplpNewHeader'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprInfoDelete():
    try:
        return WINFUNCTYPE(UInt32,c_void_p, use_last_error=False)(("MprInfoDelete", windll["MPRAPI"]), ((1, 'lpHeader'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprInfoRemoveAll():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,POINTER(c_void_p), use_last_error=False)(("MprInfoRemoveAll", windll["MPRAPI"]), ((1, 'lpHeader'),(1, 'lplpNewHeader'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprInfoDuplicate():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,POINTER(c_void_p), use_last_error=False)(("MprInfoDuplicate", windll["MPRAPI"]), ((1, 'lpHeader'),(1, 'lplpNewHeader'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprInfoBlockAdd():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,UInt32,UInt32,UInt32,c_char_p_no,POINTER(c_void_p), use_last_error=False)(("MprInfoBlockAdd", windll["MPRAPI"]), ((1, 'lpHeader'),(1, 'dwInfoType'),(1, 'dwItemSize'),(1, 'dwItemCount'),(1, 'lpItemData'),(1, 'lplpNewHeader'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprInfoBlockRemove():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,UInt32,POINTER(c_void_p), use_last_error=False)(("MprInfoBlockRemove", windll["MPRAPI"]), ((1, 'lpHeader'),(1, 'dwInfoType'),(1, 'lplpNewHeader'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprInfoBlockSet():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,UInt32,UInt32,UInt32,c_char_p_no,POINTER(c_void_p), use_last_error=False)(("MprInfoBlockSet", windll["MPRAPI"]), ((1, 'lpHeader'),(1, 'dwInfoType'),(1, 'dwItemSize'),(1, 'dwItemCount'),(1, 'lpItemData'),(1, 'lplpNewHeader'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprInfoBlockFind():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(c_char_p_no), use_last_error=False)(("MprInfoBlockFind", windll["MPRAPI"]), ((1, 'lpHeader'),(1, 'dwInfoType'),(1, 'lpdwItemSize'),(1, 'lpdwItemCount'),(1, 'lplpItemData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MprInfoBlockQuerySize():
    try:
        return WINFUNCTYPE(UInt32,c_void_p, use_last_error=False)(("MprInfoBlockQuerySize", windll["MPRAPI"]), ((1, 'lpHeader'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MgmRegisterMProtocol():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.Rras.ROUTING_PROTOCOL_CONFIG_head),UInt32,UInt32,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("MgmRegisterMProtocol", windll["rtm"]), ((1, 'prpiInfo'),(1, 'dwProtocolId'),(1, 'dwComponentId'),(1, 'phProtocol'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MgmDeRegisterMProtocol():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE, use_last_error=False)(("MgmDeRegisterMProtocol", windll["rtm"]), ((1, 'hProtocol'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MgmTakeInterfaceOwnership():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt32,UInt32, use_last_error=False)(("MgmTakeInterfaceOwnership", windll["rtm"]), ((1, 'hProtocol'),(1, 'dwIfIndex'),(1, 'dwIfNextHopAddr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MgmReleaseInterfaceOwnership():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt32,UInt32, use_last_error=False)(("MgmReleaseInterfaceOwnership", windll["rtm"]), ((1, 'hProtocol'),(1, 'dwIfIndex'),(1, 'dwIfNextHopAddr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MgmGetProtocolOnInterface():
    try:
        return WINFUNCTYPE(UInt32,UInt32,UInt32,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("MgmGetProtocolOnInterface", windll["rtm"]), ((1, 'dwIfIndex'),(1, 'dwIfNextHopAddr'),(1, 'pdwIfProtocolId'),(1, 'pdwIfComponentId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MgmAddGroupMembershipEntry():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt32,UInt32,UInt32,UInt32,UInt32,UInt32,UInt32, use_last_error=False)(("MgmAddGroupMembershipEntry", windll["rtm"]), ((1, 'hProtocol'),(1, 'dwSourceAddr'),(1, 'dwSourceMask'),(1, 'dwGroupAddr'),(1, 'dwGroupMask'),(1, 'dwIfIndex'),(1, 'dwIfNextHopIPAddr'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MgmDeleteGroupMembershipEntry():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt32,UInt32,UInt32,UInt32,UInt32,UInt32,UInt32, use_last_error=False)(("MgmDeleteGroupMembershipEntry", windll["rtm"]), ((1, 'hProtocol'),(1, 'dwSourceAddr'),(1, 'dwSourceMask'),(1, 'dwGroupAddr'),(1, 'dwGroupMask'),(1, 'dwIfIndex'),(1, 'dwIfNextHopIPAddr'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MgmGetMfe():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.MIB_IPMCAST_MFE_head),POINTER(UInt32),c_char_p_no, use_last_error=False)(("MgmGetMfe", windll["rtm"]), ((1, 'pimm'),(1, 'pdwBufferSize'),(1, 'pbBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MgmGetFirstMfe():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),c_char_p_no,POINTER(UInt32), use_last_error=False)(("MgmGetFirstMfe", windll["rtm"]), ((1, 'pdwBufferSize'),(1, 'pbBuffer'),(1, 'pdwNumEntries'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MgmGetNextMfe():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.MIB_IPMCAST_MFE_head),POINTER(UInt32),c_char_p_no,POINTER(UInt32), use_last_error=False)(("MgmGetNextMfe", windll["rtm"]), ((1, 'pimmStart'),(1, 'pdwBufferSize'),(1, 'pbBuffer'),(1, 'pdwNumEntries'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MgmGetMfeStats():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.MIB_IPMCAST_MFE_head),POINTER(UInt32),c_char_p_no,UInt32, use_last_error=False)(("MgmGetMfeStats", windll["rtm"]), ((1, 'pimm'),(1, 'pdwBufferSize'),(1, 'pbBuffer'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MgmGetFirstMfeStats():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),c_char_p_no,POINTER(UInt32),UInt32, use_last_error=False)(("MgmGetFirstMfeStats", windll["rtm"]), ((1, 'pdwBufferSize'),(1, 'pbBuffer'),(1, 'pdwNumEntries'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MgmGetNextMfeStats():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.MIB_IPMCAST_MFE_head),POINTER(UInt32),c_char_p_no,POINTER(UInt32),UInt32, use_last_error=False)(("MgmGetNextMfeStats", windll["rtm"]), ((1, 'pimmStart'),(1, 'pdwBufferSize'),(1, 'pbBuffer'),(1, 'pdwNumEntries'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MgmGroupEnumerationStart():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.NetworkManagement.Rras.MGM_ENUM_TYPES,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("MgmGroupEnumerationStart", windll["rtm"]), ((1, 'hProtocol'),(1, 'metEnumType'),(1, 'phEnumHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MgmGroupEnumerationGetNext():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(UInt32),c_char_p_no,POINTER(UInt32), use_last_error=False)(("MgmGroupEnumerationGetNext", windll["rtm"]), ((1, 'hEnum'),(1, 'pdwBufferSize'),(1, 'pbBuffer'),(1, 'pdwNumEntries'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MgmGroupEnumerationEnd():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE, use_last_error=False)(("MgmGroupEnumerationEnd", windll["rtm"]), ((1, 'hEnum'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmConvertNetAddressToIpv6AddressAndLength():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.Rras.RTM_NET_ADDRESS_head),POINTER(win32more.Networking.WinSock.IN6_ADDR_head),POINTER(UInt32),UInt32, use_last_error=False)(("RtmConvertNetAddressToIpv6AddressAndLength", windll["rtm"]), ((1, 'pNetAddress'),(1, 'pAddress'),(1, 'pLength'),(1, 'dwAddressSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmConvertIpv6AddressAndLengthToNetAddress():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.Rras.RTM_NET_ADDRESS_head),win32more.Networking.WinSock.IN6_ADDR,UInt32,UInt32, use_last_error=False)(("RtmConvertIpv6AddressAndLengthToNetAddress", windll["rtm"]), ((1, 'pNetAddress'),(1, 'Address'),(1, 'dwLength'),(1, 'dwAddressSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmRegisterEntity():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.Rras.RTM_ENTITY_INFO_head),POINTER(win32more.NetworkManagement.Rras.RTM_ENTITY_EXPORT_METHODS_head),win32more.NetworkManagement.Rras.RTM_EVENT_CALLBACK,win32more.Foundation.BOOL,POINTER(win32more.NetworkManagement.Rras.RTM_REGN_PROFILE_head),POINTER(IntPtr), use_last_error=False)(("RtmRegisterEntity", windll["rtm"]), ((1, 'RtmEntityInfo'),(1, 'ExportMethods'),(1, 'EventCallback'),(1, 'ReserveOpaquePointer'),(1, 'RtmRegProfile'),(1, 'RtmRegHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmDeregisterEntity():
    try:
        return WINFUNCTYPE(UInt32,IntPtr, use_last_error=False)(("RtmDeregisterEntity", windll["rtm"]), ((1, 'RtmRegHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmGetRegisteredEntities():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,POINTER(UInt32),POINTER(IntPtr),POINTER(win32more.NetworkManagement.Rras.RTM_ENTITY_INFO_head), use_last_error=False)(("RtmGetRegisteredEntities", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'NumEntities'),(1, 'EntityHandles'),(1, 'EntityInfos'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmReleaseEntities():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,UInt32,POINTER(IntPtr), use_last_error=False)(("RtmReleaseEntities", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'NumEntities'),(1, 'EntityHandles'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmLockDestination():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr,win32more.Foundation.BOOL,win32more.Foundation.BOOL, use_last_error=False)(("RtmLockDestination", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'DestHandle'),(1, 'Exclusive'),(1, 'LockDest'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmGetOpaqueInformationPointer():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr,POINTER(c_void_p), use_last_error=False)(("RtmGetOpaqueInformationPointer", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'DestHandle'),(1, 'OpaqueInfoPointer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmGetEntityMethods():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr,POINTER(UInt32),POINTER(win32more.NetworkManagement.Rras.RTM_ENTITY_EXPORT_METHOD), use_last_error=False)(("RtmGetEntityMethods", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'EntityHandle'),(1, 'NumMethods'),(1, 'ExptMethods'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmInvokeMethod():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr,POINTER(win32more.NetworkManagement.Rras.RTM_ENTITY_METHOD_INPUT_head),POINTER(UInt32),POINTER(win32more.NetworkManagement.Rras.RTM_ENTITY_METHOD_OUTPUT_head), use_last_error=False)(("RtmInvokeMethod", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'EntityHandle'),(1, 'Input'),(1, 'OutputSize'),(1, 'Output'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmBlockMethods():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,win32more.Foundation.HANDLE,Byte,UInt32, use_last_error=False)(("RtmBlockMethods", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'TargetHandle'),(1, 'TargetType'),(1, 'BlockingFlag'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmGetEntityInfo():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr,POINTER(win32more.NetworkManagement.Rras.RTM_ENTITY_INFO_head), use_last_error=False)(("RtmGetEntityInfo", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'EntityHandle'),(1, 'EntityInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmGetDestInfo():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr,UInt32,UInt32,POINTER(win32more.NetworkManagement.Rras.RTM_DEST_INFO_head), use_last_error=False)(("RtmGetDestInfo", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'DestHandle'),(1, 'ProtocolId'),(1, 'TargetViews'),(1, 'DestInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmGetRouteInfo():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr,POINTER(win32more.NetworkManagement.Rras.RTM_ROUTE_INFO_head),POINTER(win32more.NetworkManagement.Rras.RTM_NET_ADDRESS_head), use_last_error=False)(("RtmGetRouteInfo", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'RouteHandle'),(1, 'RouteInfo'),(1, 'DestAddress'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmGetNextHopInfo():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr,POINTER(win32more.NetworkManagement.Rras.RTM_NEXTHOP_INFO_head), use_last_error=False)(("RtmGetNextHopInfo", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'NextHopHandle'),(1, 'NextHopInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmReleaseEntityInfo():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,POINTER(win32more.NetworkManagement.Rras.RTM_ENTITY_INFO_head), use_last_error=False)(("RtmReleaseEntityInfo", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'EntityInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmReleaseDestInfo():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,POINTER(win32more.NetworkManagement.Rras.RTM_DEST_INFO_head), use_last_error=False)(("RtmReleaseDestInfo", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'DestInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmReleaseRouteInfo():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,POINTER(win32more.NetworkManagement.Rras.RTM_ROUTE_INFO_head), use_last_error=False)(("RtmReleaseRouteInfo", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'RouteInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmReleaseNextHopInfo():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,POINTER(win32more.NetworkManagement.Rras.RTM_NEXTHOP_INFO_head), use_last_error=False)(("RtmReleaseNextHopInfo", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'NextHopInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmAddRouteToDest():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,POINTER(IntPtr),POINTER(win32more.NetworkManagement.Rras.RTM_NET_ADDRESS_head),POINTER(win32more.NetworkManagement.Rras.RTM_ROUTE_INFO_head),UInt32,IntPtr,UInt32,IntPtr,POINTER(UInt32), use_last_error=False)(("RtmAddRouteToDest", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'RouteHandle'),(1, 'DestAddress'),(1, 'RouteInfo'),(1, 'TimeToLive'),(1, 'RouteListHandle'),(1, 'NotifyType'),(1, 'NotifyHandle'),(1, 'ChangeFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmDeleteRouteToDest():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr,POINTER(UInt32), use_last_error=False)(("RtmDeleteRouteToDest", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'RouteHandle'),(1, 'ChangeFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmHoldDestination():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr,UInt32,UInt32, use_last_error=False)(("RtmHoldDestination", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'DestHandle'),(1, 'TargetViews'),(1, 'HoldTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmGetRoutePointer():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr,POINTER(POINTER(win32more.NetworkManagement.Rras.RTM_ROUTE_INFO_head)), use_last_error=False)(("RtmGetRoutePointer", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'RouteHandle'),(1, 'RoutePointer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmLockRoute():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr,win32more.Foundation.BOOL,win32more.Foundation.BOOL,POINTER(POINTER(win32more.NetworkManagement.Rras.RTM_ROUTE_INFO_head)), use_last_error=False)(("RtmLockRoute", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'RouteHandle'),(1, 'Exclusive'),(1, 'LockRoute'),(1, 'RoutePointer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmUpdateAndUnlockRoute():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr,UInt32,IntPtr,UInt32,IntPtr,POINTER(UInt32), use_last_error=False)(("RtmUpdateAndUnlockRoute", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'RouteHandle'),(1, 'TimeToLive'),(1, 'RouteListHandle'),(1, 'NotifyType'),(1, 'NotifyHandle'),(1, 'ChangeFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmGetExactMatchDestination():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,POINTER(win32more.NetworkManagement.Rras.RTM_NET_ADDRESS_head),UInt32,UInt32,POINTER(win32more.NetworkManagement.Rras.RTM_DEST_INFO_head), use_last_error=False)(("RtmGetExactMatchDestination", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'DestAddress'),(1, 'ProtocolId'),(1, 'TargetViews'),(1, 'DestInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmGetMostSpecificDestination():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,POINTER(win32more.NetworkManagement.Rras.RTM_NET_ADDRESS_head),UInt32,UInt32,POINTER(win32more.NetworkManagement.Rras.RTM_DEST_INFO_head), use_last_error=False)(("RtmGetMostSpecificDestination", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'DestAddress'),(1, 'ProtocolId'),(1, 'TargetViews'),(1, 'DestInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmGetLessSpecificDestination():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr,UInt32,UInt32,POINTER(win32more.NetworkManagement.Rras.RTM_DEST_INFO_head), use_last_error=False)(("RtmGetLessSpecificDestination", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'DestHandle'),(1, 'ProtocolId'),(1, 'TargetViews'),(1, 'DestInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmGetExactMatchRoute():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,POINTER(win32more.NetworkManagement.Rras.RTM_NET_ADDRESS_head),UInt32,POINTER(win32more.NetworkManagement.Rras.RTM_ROUTE_INFO_head),UInt32,UInt32,POINTER(IntPtr), use_last_error=False)(("RtmGetExactMatchRoute", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'DestAddress'),(1, 'MatchingFlags'),(1, 'RouteInfo'),(1, 'InterfaceIndex'),(1, 'TargetViews'),(1, 'RouteHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmIsBestRoute():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr,POINTER(UInt32), use_last_error=False)(("RtmIsBestRoute", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'RouteHandle'),(1, 'BestInViews'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmAddNextHop():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,POINTER(win32more.NetworkManagement.Rras.RTM_NEXTHOP_INFO_head),POINTER(IntPtr),POINTER(UInt32), use_last_error=False)(("RtmAddNextHop", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'NextHopInfo'),(1, 'NextHopHandle'),(1, 'ChangeFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmFindNextHop():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,POINTER(win32more.NetworkManagement.Rras.RTM_NEXTHOP_INFO_head),POINTER(IntPtr),POINTER(POINTER(win32more.NetworkManagement.Rras.RTM_NEXTHOP_INFO_head)), use_last_error=False)(("RtmFindNextHop", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'NextHopInfo'),(1, 'NextHopHandle'),(1, 'NextHopPointer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmDeleteNextHop():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr,POINTER(win32more.NetworkManagement.Rras.RTM_NEXTHOP_INFO_head), use_last_error=False)(("RtmDeleteNextHop", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'NextHopHandle'),(1, 'NextHopInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmGetNextHopPointer():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr,POINTER(POINTER(win32more.NetworkManagement.Rras.RTM_NEXTHOP_INFO_head)), use_last_error=False)(("RtmGetNextHopPointer", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'NextHopHandle'),(1, 'NextHopPointer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmLockNextHop():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr,win32more.Foundation.BOOL,win32more.Foundation.BOOL,POINTER(POINTER(win32more.NetworkManagement.Rras.RTM_NEXTHOP_INFO_head)), use_last_error=False)(("RtmLockNextHop", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'NextHopHandle'),(1, 'Exclusive'),(1, 'LockNextHop'),(1, 'NextHopPointer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmCreateDestEnum():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,UInt32,UInt32,POINTER(win32more.NetworkManagement.Rras.RTM_NET_ADDRESS_head),UInt32,POINTER(IntPtr), use_last_error=False)(("RtmCreateDestEnum", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'TargetViews'),(1, 'EnumFlags'),(1, 'NetAddress'),(1, 'ProtocolId'),(1, 'RtmEnumHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmGetEnumDests():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr,POINTER(UInt32),POINTER(win32more.NetworkManagement.Rras.RTM_DEST_INFO_head), use_last_error=False)(("RtmGetEnumDests", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'EnumHandle'),(1, 'NumDests'),(1, 'DestInfos'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmReleaseDests():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,UInt32,POINTER(win32more.NetworkManagement.Rras.RTM_DEST_INFO_head), use_last_error=False)(("RtmReleaseDests", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'NumDests'),(1, 'DestInfos'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmCreateRouteEnum():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr,UInt32,UInt32,POINTER(win32more.NetworkManagement.Rras.RTM_NET_ADDRESS_head),UInt32,POINTER(win32more.NetworkManagement.Rras.RTM_ROUTE_INFO_head),UInt32,POINTER(IntPtr), use_last_error=False)(("RtmCreateRouteEnum", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'DestHandle'),(1, 'TargetViews'),(1, 'EnumFlags'),(1, 'StartDest'),(1, 'MatchingFlags'),(1, 'CriteriaRoute'),(1, 'CriteriaInterface'),(1, 'RtmEnumHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmGetEnumRoutes():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr,POINTER(UInt32),POINTER(IntPtr), use_last_error=False)(("RtmGetEnumRoutes", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'EnumHandle'),(1, 'NumRoutes'),(1, 'RouteHandles'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmReleaseRoutes():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,UInt32,POINTER(IntPtr), use_last_error=False)(("RtmReleaseRoutes", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'NumRoutes'),(1, 'RouteHandles'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmCreateNextHopEnum():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,UInt32,POINTER(win32more.NetworkManagement.Rras.RTM_NET_ADDRESS_head),POINTER(IntPtr), use_last_error=False)(("RtmCreateNextHopEnum", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'EnumFlags'),(1, 'NetAddress'),(1, 'RtmEnumHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmGetEnumNextHops():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr,POINTER(UInt32),POINTER(IntPtr), use_last_error=False)(("RtmGetEnumNextHops", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'EnumHandle'),(1, 'NumNextHops'),(1, 'NextHopHandles'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmReleaseNextHops():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,UInt32,POINTER(IntPtr), use_last_error=False)(("RtmReleaseNextHops", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'NumNextHops'),(1, 'NextHopHandles'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmDeleteEnumHandle():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr, use_last_error=False)(("RtmDeleteEnumHandle", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'EnumHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmRegisterForChangeNotification():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,UInt32,UInt32,c_void_p,POINTER(IntPtr), use_last_error=False)(("RtmRegisterForChangeNotification", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'TargetViews'),(1, 'NotifyFlags'),(1, 'NotifyContext'),(1, 'NotifyHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmGetChangedDests():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr,POINTER(UInt32),POINTER(win32more.NetworkManagement.Rras.RTM_DEST_INFO_head), use_last_error=False)(("RtmGetChangedDests", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'NotifyHandle'),(1, 'NumDests'),(1, 'ChangedDests'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmReleaseChangedDests():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr,UInt32,POINTER(win32more.NetworkManagement.Rras.RTM_DEST_INFO_head), use_last_error=False)(("RtmReleaseChangedDests", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'NotifyHandle'),(1, 'NumDests'),(1, 'ChangedDests'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmIgnoreChangedDests():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr,UInt32,POINTER(IntPtr), use_last_error=False)(("RtmIgnoreChangedDests", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'NotifyHandle'),(1, 'NumDests'),(1, 'ChangedDests'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmGetChangeStatus():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr,IntPtr,POINTER(win32more.Foundation.BOOL), use_last_error=False)(("RtmGetChangeStatus", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'NotifyHandle'),(1, 'DestHandle'),(1, 'ChangeStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmMarkDestForChangeNotification():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr,IntPtr,win32more.Foundation.BOOL, use_last_error=False)(("RtmMarkDestForChangeNotification", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'NotifyHandle'),(1, 'DestHandle'),(1, 'MarkDest'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmIsMarkedForChangeNotification():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr,IntPtr,POINTER(win32more.Foundation.BOOL), use_last_error=False)(("RtmIsMarkedForChangeNotification", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'NotifyHandle'),(1, 'DestHandle'),(1, 'DestMarked'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmDeregisterFromChangeNotification():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr, use_last_error=False)(("RtmDeregisterFromChangeNotification", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'NotifyHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmCreateRouteList():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,POINTER(IntPtr), use_last_error=False)(("RtmCreateRouteList", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'RouteListHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmInsertInRouteList():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr,UInt32,POINTER(IntPtr), use_last_error=False)(("RtmInsertInRouteList", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'RouteListHandle'),(1, 'NumRoutes'),(1, 'RouteHandles'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmCreateRouteListEnum():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr,POINTER(IntPtr), use_last_error=False)(("RtmCreateRouteListEnum", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'RouteListHandle'),(1, 'RtmEnumHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmGetListEnumRoutes():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr,POINTER(UInt32),POINTER(IntPtr), use_last_error=False)(("RtmGetListEnumRoutes", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'EnumHandle'),(1, 'NumRoutes'),(1, 'RouteHandles'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmDeleteRouteList():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr, use_last_error=False)(("RtmDeleteRouteList", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'RouteListHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtmReferenceHandles():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,UInt32,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("RtmReferenceHandles", windll["rtm"]), ((1, 'RtmRegHandle'),(1, 'NumHandles'),(1, 'RtmHandles'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "RASNAP_ProbationTime",
    "RASTUNNELENDPOINT_UNKNOWN",
    "RASTUNNELENDPOINT_IPv4",
    "RASTUNNELENDPOINT_IPv6",
    "RAS_MaxDeviceType",
    "RAS_MaxPhoneNumber",
    "RAS_MaxIpAddress",
    "RAS_MaxIpxAddress",
    "RAS_MaxEntryName",
    "RAS_MaxDeviceName",
    "RAS_MaxCallbackNumber",
    "RAS_MaxAreaCode",
    "RAS_MaxPadType",
    "RAS_MaxX25Address",
    "RAS_MaxFacilities",
    "RAS_MaxUserData",
    "RAS_MaxReplyMessage",
    "RAS_MaxDnsSuffix",
    "RASCF_AllUsers",
    "RASCF_GlobalCreds",
    "RASCF_OwnerKnown",
    "RASCF_OwnerMatch",
    "RAS_MaxIDSize",
    "RASCS_PAUSED",
    "RASCS_DONE",
    "RASCSS_DONE",
    "RDEOPT_UsePrefixSuffix",
    "RDEOPT_PausedStates",
    "RDEOPT_IgnoreModemSpeaker",
    "RDEOPT_SetModemSpeaker",
    "RDEOPT_IgnoreSoftwareCompression",
    "RDEOPT_SetSoftwareCompression",
    "RDEOPT_DisableConnectedUI",
    "RDEOPT_DisableReconnectUI",
    "RDEOPT_DisableReconnect",
    "RDEOPT_NoUser",
    "RDEOPT_PauseOnScript",
    "RDEOPT_Router",
    "RDEOPT_CustomDial",
    "RDEOPT_UseCustomScripting",
    "RDEOPT_InvokeAutoTriggerCredentialUI",
    "RDEOPT_EapInfoCryptInCapable",
    "REN_User",
    "REN_AllUsers",
    "RASIPO_VJ",
    "RASLCPO_PFC",
    "RASLCPO_ACFC",
    "RASLCPO_SSHF",
    "RASLCPO_DES_56",
    "RASLCPO_3_DES",
    "RASLCPO_AES_128",
    "RASLCPO_AES_256",
    "RASLCPO_AES_192",
    "RASLCPO_GCM_AES_128",
    "RASLCPO_GCM_AES_192",
    "RASLCPO_GCM_AES_256",
    "RASCCPCA_MPPC",
    "RASCCPCA_STAC",
    "RASCCPO_Compression",
    "RASCCPO_HistoryLess",
    "RASCCPO_Encryption56bit",
    "RASCCPO_Encryption40bit",
    "RASCCPO_Encryption128bit",
    "RASIKEv2_AUTH_MACHINECERTIFICATES",
    "RASIKEv2_AUTH_EAP",
    "RASIKEv2_AUTH_PSK",
    "WM_RASDIALEVENT",
    "ET_None",
    "ET_Require",
    "ET_RequireMax",
    "ET_Optional",
    "VS_Default",
    "VS_PptpOnly",
    "VS_PptpFirst",
    "VS_L2tpOnly",
    "VS_L2tpFirst",
    "VS_SstpOnly",
    "VS_SstpFirst",
    "VS_Ikev2Only",
    "VS_Ikev2First",
    "VS_GREOnly",
    "VS_PptpSstp",
    "VS_L2tpSstp",
    "VS_Ikev2Sstp",
    "VS_ProtocolList",
    "RASEO_UseCountryAndAreaCodes",
    "RASEO_SpecificIpAddr",
    "RASEO_SpecificNameServers",
    "RASEO_IpHeaderCompression",
    "RASEO_RemoteDefaultGateway",
    "RASEO_DisableLcpExtensions",
    "RASEO_TerminalBeforeDial",
    "RASEO_TerminalAfterDial",
    "RASEO_ModemLights",
    "RASEO_SwCompression",
    "RASEO_RequireEncryptedPw",
    "RASEO_RequireMsEncryptedPw",
    "RASEO_RequireDataEncryption",
    "RASEO_NetworkLogon",
    "RASEO_UseLogonCredentials",
    "RASEO_PromoteAlternates",
    "RASEO_SecureLocalFiles",
    "RASEO_RequireEAP",
    "RASEO_RequirePAP",
    "RASEO_RequireSPAP",
    "RASEO_Custom",
    "RASEO_PreviewPhoneNumber",
    "RASEO_SharedPhoneNumbers",
    "RASEO_PreviewUserPw",
    "RASEO_PreviewDomain",
    "RASEO_ShowDialingProgress",
    "RASEO_RequireCHAP",
    "RASEO_RequireMsCHAP",
    "RASEO_RequireMsCHAP2",
    "RASEO_RequireW95MSCHAP",
    "RASEO_CustomScript",
    "RASEO2_SecureFileAndPrint",
    "RASEO2_SecureClientForMSNet",
    "RASEO2_DontNegotiateMultilink",
    "RASEO2_DontUseRasCredentials",
    "RASEO2_UsePreSharedKey",
    "RASEO2_Internet",
    "RASEO2_DisableNbtOverIP",
    "RASEO2_UseGlobalDeviceSettings",
    "RASEO2_ReconnectIfDropped",
    "RASEO2_SharePhoneNumbers",
    "RASEO2_SecureRoutingCompartment",
    "RASEO2_UseTypicalSettings",
    "RASEO2_IPv6SpecificNameServers",
    "RASEO2_IPv6RemoteDefaultGateway",
    "RASEO2_RegisterIpWithDNS",
    "RASEO2_UseDNSSuffixForRegistration",
    "RASEO2_IPv4ExplicitMetric",
    "RASEO2_IPv6ExplicitMetric",
    "RASEO2_DisableIKENameEkuCheck",
    "RASEO2_DisableClassBasedStaticRoute",
    "RASEO2_SpecificIPv6Addr",
    "RASEO2_DisableMobility",
    "RASEO2_RequireMachineCertificates",
    "RASEO2_UsePreSharedKeyForIkev2Initiator",
    "RASEO2_UsePreSharedKeyForIkev2Responder",
    "RASEO2_CacheCredentials",
    "RASEO2_AutoTriggerCapable",
    "RASEO2_IsThirdPartyProfile",
    "RASEO2_AuthTypeIsOtp",
    "RASEO2_IsAlwaysOn",
    "RASEO2_IsPrivateNetwork",
    "RASEO2_PlumbIKEv2TSAsRoutes",
    "RASNP_NetBEUI",
    "RASNP_Ipx",
    "RASNP_Ip",
    "RASNP_Ipv6",
    "RASFP_Ppp",
    "RASFP_Slip",
    "RASFP_Ras",
    "RASET_Phone",
    "RASET_Vpn",
    "RASET_Direct",
    "RASET_Internet",
    "RASET_Broadband",
    "RASCN_Connection",
    "RASCN_Disconnection",
    "RASCN_BandwidthAdded",
    "RASCN_BandwidthRemoved",
    "RASCN_Dormant",
    "RASCN_ReConnection",
    "RASCN_EPDGPacketArrival",
    "RASIDS_Disabled",
    "RASIDS_UseGlobalValue",
    "RASADFLG_PositionDlg",
    "RASCM_UserName",
    "RASCM_Password",
    "RASCM_Domain",
    "RASCM_DefaultCreds",
    "RASCM_PreSharedKey",
    "RASCM_ServerPreSharedKey",
    "RASCM_DDMPreSharedKey",
    "RASADP_DisableConnectionQuery",
    "RASADP_LoginSessionDisable",
    "RASADP_SavedAddressesLimit",
    "RASADP_FailedConnectionTimeout",
    "RASADP_ConnectionQueryTimeout",
    "RASEAPF_NonInteractive",
    "RASEAPF_Logon",
    "RASEAPF_Preview",
    "RCD_SingleUser",
    "RCD_AllUsers",
    "RCD_Eap",
    "RCD_Logon",
    "RASPBDEVENT_AddEntry",
    "RASPBDEVENT_EditEntry",
    "RASPBDEVENT_RemoveEntry",
    "RASPBDEVENT_DialEntry",
    "RASPBDEVENT_EditGlobals",
    "RASPBDEVENT_NoUser",
    "RASPBDEVENT_NoUserEdit",
    "RASNOUSER_SmartCard",
    "RASPBDFLAG_PositionDlg",
    "RASPBDFLAG_ForceCloseOnDial",
    "RASPBDFLAG_NoUser",
    "RASPBDFLAG_UpdateDefaults",
    "RASEDFLAG_PositionDlg",
    "RASEDFLAG_NewEntry",
    "RASEDFLAG_CloneEntry",
    "RASEDFLAG_NoRename",
    "RASEDFLAG_ShellOwned",
    "RASEDFLAG_NewPhoneEntry",
    "RASEDFLAG_NewTunnelEntry",
    "RASEDFLAG_NewDirectEntry",
    "RASEDFLAG_NewBroadbandEntry",
    "RASEDFLAG_InternetEntry",
    "RASEDFLAG_NAT",
    "RASEDFLAG_IncomingConnection",
    "RASDDFLAG_PositionDlg",
    "RASDDFLAG_NoPrompt",
    "RASDDFLAG_AoacRedial",
    "RASDDFLAG_LinkFailure",
    "PID_IPX",
    "PID_IP",
    "PID_IPV6",
    "PID_NBF",
    "PID_ATALK",
    "MPR_INTERFACE_OUT_OF_RESOURCES",
    "MPR_INTERFACE_ADMIN_DISABLED",
    "MPR_INTERFACE_CONNECTION_FAILURE",
    "MPR_INTERFACE_SERVICE_PAUSED",
    "MPR_INTERFACE_DIALOUT_HOURS_RESTRICTION",
    "MPR_INTERFACE_NO_MEDIA_SENSE",
    "MPR_INTERFACE_NO_DEVICE",
    "MPR_MaxDeviceType",
    "MPR_MaxPhoneNumber",
    "MPR_MaxIpAddress",
    "MPR_MaxIpxAddress",
    "MPR_MaxEntryName",
    "MPR_MaxDeviceName",
    "MPR_MaxCallbackNumber",
    "MPR_MaxAreaCode",
    "MPR_MaxPadType",
    "MPR_MaxX25Address",
    "MPR_MaxFacilities",
    "MPR_MaxUserData",
    "MPRIO_SpecificIpAddr",
    "MPRIO_SpecificNameServers",
    "MPRIO_IpHeaderCompression",
    "MPRIO_RemoteDefaultGateway",
    "MPRIO_DisableLcpExtensions",
    "MPRIO_SwCompression",
    "MPRIO_RequireEncryptedPw",
    "MPRIO_RequireMsEncryptedPw",
    "MPRIO_RequireDataEncryption",
    "MPRIO_NetworkLogon",
    "MPRIO_PromoteAlternates",
    "MPRIO_SecureLocalFiles",
    "MPRIO_RequireEAP",
    "MPRIO_RequirePAP",
    "MPRIO_RequireSPAP",
    "MPRIO_SharedPhoneNumbers",
    "MPRIO_RequireCHAP",
    "MPRIO_RequireMsCHAP",
    "MPRIO_RequireMsCHAP2",
    "MPRIO_IpSecPreSharedKey",
    "MPRIO_RequireMachineCertificates",
    "MPRIO_UsePreSharedKeyForIkev2Initiator",
    "MPRIO_UsePreSharedKeyForIkev2Responder",
    "MPRNP_Ipx",
    "MPRNP_Ip",
    "MPRNP_Ipv6",
    "MPRET_Phone",
    "MPRET_Vpn",
    "MPRET_Direct",
    "MPRIDS_Disabled",
    "MPRIDS_UseGlobalValue",
    "MPR_VS_Ikev2Only",
    "MPR_VS_Ikev2First",
    "MPR_ENABLE_RAS_ON_DEVICE",
    "MPR_ENABLE_ROUTING_ON_DEVICE",
    "IPADDRESSLEN",
    "IPXADDRESSLEN",
    "ATADDRESSLEN",
    "MAXIPADRESSLEN",
    "PPP_IPCP_VJ",
    "PPP_CCP_COMPRESSION",
    "PPP_CCP_ENCRYPTION40BITOLD",
    "PPP_CCP_ENCRYPTION40BIT",
    "PPP_CCP_ENCRYPTION128BIT",
    "PPP_CCP_ENCRYPTION56BIT",
    "PPP_CCP_HISTORYLESS",
    "PPP_LCP_MULTILINK_FRAMING",
    "PPP_LCP_PFC",
    "PPP_LCP_ACFC",
    "PPP_LCP_SSHF",
    "PPP_LCP_DES_56",
    "PPP_LCP_3_DES",
    "PPP_LCP_AES_128",
    "PPP_LCP_AES_256",
    "PPP_LCP_AES_192",
    "PPP_LCP_GCM_AES_128",
    "PPP_LCP_GCM_AES_192",
    "PPP_LCP_GCM_AES_256",
    "RAS_FLAGS_RAS_CONNECTION",
    "RASPRIV_NoCallback",
    "RASPRIV_AdminSetCallback",
    "RASPRIV_CallerSetCallback",
    "RASPRIV_DialinPrivilege",
    "RASPRIV2_DialinPolicy",
    "MPRAPI_IKEV2_AUTH_USING_CERT",
    "MPRAPI_IKEV2_AUTH_USING_EAP",
    "MPRAPI_PPP_PROJECTION_INFO_TYPE",
    "MPRAPI_IKEV2_PROJECTION_INFO_TYPE",
    "MPRAPI_RAS_CONNECTION_OBJECT_REVISION_1",
    "MPRAPI_MPR_IF_CUSTOM_CONFIG_OBJECT_REVISION_1",
    "MPRAPI_IF_CUSTOM_CONFIG_FOR_IKEV2",
    "MPRAPI_MPR_IF_CUSTOM_CONFIG_OBJECT_REVISION_3",
    "MPRAPI_MPR_IF_CUSTOM_CONFIG_OBJECT_REVISION_2",
    "MPRAPI_IKEV2_SET_TUNNEL_CONFIG_PARAMS",
    "MPRAPI_L2TP_SET_TUNNEL_CONFIG_PARAMS",
    "MAX_SSTP_HASH_SIZE",
    "MPRAPI_MPR_SERVER_OBJECT_REVISION_1",
    "MPRAPI_MPR_SERVER_OBJECT_REVISION_2",
    "MPRAPI_MPR_SERVER_OBJECT_REVISION_3",
    "MPRAPI_MPR_SERVER_OBJECT_REVISION_4",
    "MPRAPI_MPR_SERVER_OBJECT_REVISION_5",
    "MPRAPI_MPR_SERVER_SET_CONFIG_OBJECT_REVISION_1",
    "MPRAPI_MPR_SERVER_SET_CONFIG_OBJECT_REVISION_2",
    "MPRAPI_MPR_SERVER_SET_CONFIG_OBJECT_REVISION_3",
    "MPRAPI_MPR_SERVER_SET_CONFIG_OBJECT_REVISION_4",
    "MPRAPI_MPR_SERVER_SET_CONFIG_OBJECT_REVISION_5",
    "MPRAPI_SET_CONFIG_PROTOCOL_FOR_PPTP",
    "MPRAPI_SET_CONFIG_PROTOCOL_FOR_L2TP",
    "MPRAPI_SET_CONFIG_PROTOCOL_FOR_SSTP",
    "MPRAPI_SET_CONFIG_PROTOCOL_FOR_IKEV2",
    "MPRAPI_SET_CONFIG_PROTOCOL_FOR_GRE",
    "ALLOW_NO_AUTH",
    "DO_NOT_ALLOW_NO_AUTH",
    "MPRAPI_RAS_UPDATE_CONNECTION_OBJECT_REVISION_1",
    "MPRAPI_ADMIN_DLL_VERSION_1",
    "MPRAPI_ADMIN_DLL_VERSION_2",
    "MGM_JOIN_STATE_FLAG",
    "MGM_FORWARD_STATE_FLAG",
    "MGM_MFE_STATS_0",
    "MGM_MFE_STATS_1",
    "RTM_MAX_ADDRESS_SIZE",
    "RTM_MAX_VIEWS",
    "RTM_VIEW_ID_UCAST",
    "RTM_VIEW_ID_MCAST",
    "RTM_VIEW_MASK_SIZE",
    "RTM_VIEW_MASK_NONE",
    "RTM_VIEW_MASK_ANY",
    "RTM_VIEW_MASK_UCAST",
    "RTM_VIEW_MASK_MCAST",
    "RTM_VIEW_MASK_ALL",
    "IPV6_ADDRESS_LEN_IN_BYTES",
    "RTM_DEST_FLAG_NATURAL_NET",
    "RTM_DEST_FLAG_FWD_ENGIN_ADD",
    "RTM_DEST_FLAG_DONT_FORWARD",
    "RTM_ROUTE_STATE_CREATED",
    "RTM_ROUTE_STATE_DELETING",
    "RTM_ROUTE_STATE_DELETED",
    "RTM_ROUTE_FLAGS_MARTIAN",
    "RTM_ROUTE_FLAGS_BLACKHOLE",
    "RTM_ROUTE_FLAGS_DISCARD",
    "RTM_ROUTE_FLAGS_INACTIVE",
    "RTM_ROUTE_FLAGS_LOCAL",
    "RTM_ROUTE_FLAGS_REMOTE",
    "RTM_ROUTE_FLAGS_MYSELF",
    "RTM_ROUTE_FLAGS_LOOPBACK",
    "RTM_ROUTE_FLAGS_MCAST",
    "RTM_ROUTE_FLAGS_LOCAL_MCAST",
    "RTM_ROUTE_FLAGS_LIMITED_BC",
    "RTM_ROUTE_FLAGS_ZEROS_NETBC",
    "RTM_ROUTE_FLAGS_ZEROS_SUBNETBC",
    "RTM_ROUTE_FLAGS_ONES_NETBC",
    "RTM_ROUTE_FLAGS_ONES_SUBNETBC",
    "RTM_NEXTHOP_STATE_CREATED",
    "RTM_NEXTHOP_STATE_DELETED",
    "RTM_NEXTHOP_FLAGS_REMOTE",
    "RTM_NEXTHOP_FLAGS_DOWN",
    "METHOD_TYPE_ALL_METHODS",
    "METHOD_RIP2_NEIGHBOUR_ADDR",
    "METHOD_RIP2_OUTBOUND_INTF",
    "METHOD_RIP2_ROUTE_TAG",
    "METHOD_RIP2_ROUTE_TIMESTAMP",
    "METHOD_BGP4_AS_PATH",
    "METHOD_BGP4_PEER_ID",
    "METHOD_BGP4_PA_ORIGIN",
    "METHOD_BGP4_NEXTHOP_ATTR",
    "RTM_RESUME_METHODS",
    "RTM_BLOCK_METHODS",
    "RTM_ROUTE_CHANGE_FIRST",
    "RTM_ROUTE_CHANGE_NEW",
    "RTM_ROUTE_CHANGE_BEST",
    "RTM_NEXTHOP_CHANGE_NEW",
    "RTM_MATCH_NONE",
    "RTM_MATCH_OWNER",
    "RTM_MATCH_NEIGHBOUR",
    "RTM_MATCH_PREF",
    "RTM_MATCH_NEXTHOP",
    "RTM_MATCH_INTERFACE",
    "RTM_MATCH_FULL",
    "RTM_ENUM_START",
    "RTM_ENUM_NEXT",
    "RTM_ENUM_RANGE",
    "RTM_ENUM_ALL_DESTS",
    "RTM_ENUM_OWN_DESTS",
    "RTM_ENUM_ALL_ROUTES",
    "RTM_ENUM_OWN_ROUTES",
    "RTM_NUM_CHANGE_TYPES",
    "RTM_CHANGE_TYPE_ALL",
    "RTM_CHANGE_TYPE_BEST",
    "RTM_CHANGE_TYPE_FORWARDING",
    "RTM_NOTIFY_ONLY_MARKED_DESTS",
    "RASBASE",
    "PENDING",
    "ERROR_INVALID_PORT_HANDLE",
    "ERROR_PORT_ALREADY_OPEN",
    "ERROR_BUFFER_TOO_SMALL",
    "ERROR_WRONG_INFO_SPECIFIED",
    "ERROR_CANNOT_SET_PORT_INFO",
    "ERROR_PORT_NOT_CONNECTED",
    "ERROR_EVENT_INVALID",
    "ERROR_DEVICE_DOES_NOT_EXIST",
    "ERROR_DEVICETYPE_DOES_NOT_EXIST",
    "ERROR_BUFFER_INVALID",
    "ERROR_ROUTE_NOT_AVAILABLE",
    "ERROR_ROUTE_NOT_ALLOCATED",
    "ERROR_INVALID_COMPRESSION_SPECIFIED",
    "ERROR_OUT_OF_BUFFERS",
    "ERROR_PORT_NOT_FOUND",
    "ERROR_ASYNC_REQUEST_PENDING",
    "ERROR_ALREADY_DISCONNECTING",
    "ERROR_PORT_NOT_OPEN",
    "ERROR_PORT_DISCONNECTED",
    "ERROR_NO_ENDPOINTS",
    "ERROR_CANNOT_OPEN_PHONEBOOK",
    "ERROR_CANNOT_LOAD_PHONEBOOK",
    "ERROR_CANNOT_FIND_PHONEBOOK_ENTRY",
    "ERROR_CANNOT_WRITE_PHONEBOOK",
    "ERROR_CORRUPT_PHONEBOOK",
    "ERROR_CANNOT_LOAD_STRING",
    "ERROR_KEY_NOT_FOUND",
    "ERROR_DISCONNECTION",
    "ERROR_REMOTE_DISCONNECTION",
    "ERROR_HARDWARE_FAILURE",
    "ERROR_USER_DISCONNECTION",
    "ERROR_INVALID_SIZE",
    "ERROR_PORT_NOT_AVAILABLE",
    "ERROR_CANNOT_PROJECT_CLIENT",
    "ERROR_UNKNOWN",
    "ERROR_WRONG_DEVICE_ATTACHED",
    "ERROR_BAD_STRING",
    "ERROR_REQUEST_TIMEOUT",
    "ERROR_CANNOT_GET_LANA",
    "ERROR_NETBIOS_ERROR",
    "ERROR_SERVER_OUT_OF_RESOURCES",
    "ERROR_NAME_EXISTS_ON_NET",
    "ERROR_SERVER_GENERAL_NET_FAILURE",
    "WARNING_MSG_ALIAS_NOT_ADDED",
    "ERROR_AUTH_INTERNAL",
    "ERROR_RESTRICTED_LOGON_HOURS",
    "ERROR_ACCT_DISABLED",
    "ERROR_PASSWD_EXPIRED",
    "ERROR_NO_DIALIN_PERMISSION",
    "ERROR_SERVER_NOT_RESPONDING",
    "ERROR_FROM_DEVICE",
    "ERROR_UNRECOGNIZED_RESPONSE",
    "ERROR_MACRO_NOT_FOUND",
    "ERROR_MACRO_NOT_DEFINED",
    "ERROR_MESSAGE_MACRO_NOT_FOUND",
    "ERROR_DEFAULTOFF_MACRO_NOT_FOUND",
    "ERROR_FILE_COULD_NOT_BE_OPENED",
    "ERROR_DEVICENAME_TOO_LONG",
    "ERROR_DEVICENAME_NOT_FOUND",
    "ERROR_NO_RESPONSES",
    "ERROR_NO_COMMAND_FOUND",
    "ERROR_WRONG_KEY_SPECIFIED",
    "ERROR_UNKNOWN_DEVICE_TYPE",
    "ERROR_ALLOCATING_MEMORY",
    "ERROR_PORT_NOT_CONFIGURED",
    "ERROR_DEVICE_NOT_READY",
    "ERROR_READING_INI_FILE",
    "ERROR_NO_CONNECTION",
    "ERROR_BAD_USAGE_IN_INI_FILE",
    "ERROR_READING_SECTIONNAME",
    "ERROR_READING_DEVICETYPE",
    "ERROR_READING_DEVICENAME",
    "ERROR_READING_USAGE",
    "ERROR_READING_MAXCONNECTBPS",
    "ERROR_READING_MAXCARRIERBPS",
    "ERROR_LINE_BUSY",
    "ERROR_VOICE_ANSWER",
    "ERROR_NO_ANSWER",
    "ERROR_NO_CARRIER",
    "ERROR_NO_DIALTONE",
    "ERROR_IN_COMMAND",
    "ERROR_WRITING_SECTIONNAME",
    "ERROR_WRITING_DEVICETYPE",
    "ERROR_WRITING_DEVICENAME",
    "ERROR_WRITING_MAXCONNECTBPS",
    "ERROR_WRITING_MAXCARRIERBPS",
    "ERROR_WRITING_USAGE",
    "ERROR_WRITING_DEFAULTOFF",
    "ERROR_READING_DEFAULTOFF",
    "ERROR_EMPTY_INI_FILE",
    "ERROR_AUTHENTICATION_FAILURE",
    "ERROR_PORT_OR_DEVICE",
    "ERROR_NOT_BINARY_MACRO",
    "ERROR_DCB_NOT_FOUND",
    "ERROR_STATE_MACHINES_NOT_STARTED",
    "ERROR_STATE_MACHINES_ALREADY_STARTED",
    "ERROR_PARTIAL_RESPONSE_LOOPING",
    "ERROR_UNKNOWN_RESPONSE_KEY",
    "ERROR_RECV_BUF_FULL",
    "ERROR_CMD_TOO_LONG",
    "ERROR_UNSUPPORTED_BPS",
    "ERROR_UNEXPECTED_RESPONSE",
    "ERROR_INTERACTIVE_MODE",
    "ERROR_BAD_CALLBACK_NUMBER",
    "ERROR_INVALID_AUTH_STATE",
    "ERROR_WRITING_INITBPS",
    "ERROR_X25_DIAGNOSTIC",
    "ERROR_ACCT_EXPIRED",
    "ERROR_CHANGING_PASSWORD",
    "ERROR_OVERRUN",
    "ERROR_RASMAN_CANNOT_INITIALIZE",
    "ERROR_BIPLEX_PORT_NOT_AVAILABLE",
    "ERROR_NO_ACTIVE_ISDN_LINES",
    "ERROR_NO_ISDN_CHANNELS_AVAILABLE",
    "ERROR_TOO_MANY_LINE_ERRORS",
    "ERROR_IP_CONFIGURATION",
    "ERROR_NO_IP_ADDRESSES",
    "ERROR_PPP_TIMEOUT",
    "ERROR_PPP_REMOTE_TERMINATED",
    "ERROR_PPP_NO_PROTOCOLS_CONFIGURED",
    "ERROR_PPP_NO_RESPONSE",
    "ERROR_PPP_INVALID_PACKET",
    "ERROR_PHONE_NUMBER_TOO_LONG",
    "ERROR_IPXCP_NO_DIALOUT_CONFIGURED",
    "ERROR_IPXCP_NO_DIALIN_CONFIGURED",
    "ERROR_IPXCP_DIALOUT_ALREADY_ACTIVE",
    "ERROR_ACCESSING_TCPCFGDLL",
    "ERROR_NO_IP_RAS_ADAPTER",
    "ERROR_SLIP_REQUIRES_IP",
    "ERROR_PROJECTION_NOT_COMPLETE",
    "ERROR_PROTOCOL_NOT_CONFIGURED",
    "ERROR_PPP_NOT_CONVERGING",
    "ERROR_PPP_CP_REJECTED",
    "ERROR_PPP_LCP_TERMINATED",
    "ERROR_PPP_REQUIRED_ADDRESS_REJECTED",
    "ERROR_PPP_NCP_TERMINATED",
    "ERROR_PPP_LOOPBACK_DETECTED",
    "ERROR_PPP_NO_ADDRESS_ASSIGNED",
    "ERROR_CANNOT_USE_LOGON_CREDENTIALS",
    "ERROR_TAPI_CONFIGURATION",
    "ERROR_NO_LOCAL_ENCRYPTION",
    "ERROR_NO_REMOTE_ENCRYPTION",
    "ERROR_REMOTE_REQUIRES_ENCRYPTION",
    "ERROR_IPXCP_NET_NUMBER_CONFLICT",
    "ERROR_INVALID_SMM",
    "ERROR_SMM_UNINITIALIZED",
    "ERROR_NO_MAC_FOR_PORT",
    "ERROR_SMM_TIMEOUT",
    "ERROR_BAD_PHONE_NUMBER",
    "ERROR_WRONG_MODULE",
    "ERROR_INVALID_CALLBACK_NUMBER",
    "ERROR_SCRIPT_SYNTAX",
    "ERROR_HANGUP_FAILED",
    "ERROR_BUNDLE_NOT_FOUND",
    "ERROR_CANNOT_DO_CUSTOMDIAL",
    "ERROR_DIAL_ALREADY_IN_PROGRESS",
    "ERROR_RASAUTO_CANNOT_INITIALIZE",
    "ERROR_CONNECTION_ALREADY_SHARED",
    "ERROR_SHARING_CHANGE_FAILED",
    "ERROR_SHARING_ROUTER_INSTALL",
    "ERROR_SHARE_CONNECTION_FAILED",
    "ERROR_SHARING_PRIVATE_INSTALL",
    "ERROR_CANNOT_SHARE_CONNECTION",
    "ERROR_NO_SMART_CARD_READER",
    "ERROR_SHARING_ADDRESS_EXISTS",
    "ERROR_NO_CERTIFICATE",
    "ERROR_SHARING_MULTIPLE_ADDRESSES",
    "ERROR_FAILED_TO_ENCRYPT",
    "ERROR_BAD_ADDRESS_SPECIFIED",
    "ERROR_CONNECTION_REJECT",
    "ERROR_CONGESTION",
    "ERROR_INCOMPATIBLE",
    "ERROR_NUMBERCHANGED",
    "ERROR_TEMPFAILURE",
    "ERROR_BLOCKED",
    "ERROR_DONOTDISTURB",
    "ERROR_OUTOFORDER",
    "ERROR_UNABLE_TO_AUTHENTICATE_SERVER",
    "ERROR_SMART_CARD_REQUIRED",
    "ERROR_INVALID_FUNCTION_FOR_ENTRY",
    "ERROR_CERT_FOR_ENCRYPTION_NOT_FOUND",
    "ERROR_SHARING_RRAS_CONFLICT",
    "ERROR_SHARING_NO_PRIVATE_LAN",
    "ERROR_NO_DIFF_USER_AT_LOGON",
    "ERROR_NO_REG_CERT_AT_LOGON",
    "ERROR_OAKLEY_NO_CERT",
    "ERROR_OAKLEY_AUTH_FAIL",
    "ERROR_OAKLEY_ATTRIB_FAIL",
    "ERROR_OAKLEY_GENERAL_PROCESSING",
    "ERROR_OAKLEY_NO_PEER_CERT",
    "ERROR_OAKLEY_NO_POLICY",
    "ERROR_OAKLEY_TIMED_OUT",
    "ERROR_OAKLEY_ERROR",
    "ERROR_UNKNOWN_FRAMED_PROTOCOL",
    "ERROR_WRONG_TUNNEL_TYPE",
    "ERROR_UNKNOWN_SERVICE_TYPE",
    "ERROR_CONNECTING_DEVICE_NOT_FOUND",
    "ERROR_NO_EAPTLS_CERTIFICATE",
    "ERROR_SHARING_HOST_ADDRESS_CONFLICT",
    "ERROR_AUTOMATIC_VPN_FAILED",
    "ERROR_VALIDATING_SERVER_CERT",
    "ERROR_READING_SCARD",
    "ERROR_INVALID_PEAP_COOKIE_CONFIG",
    "ERROR_INVALID_PEAP_COOKIE_USER",
    "ERROR_INVALID_MSCHAPV2_CONFIG",
    "ERROR_VPN_GRE_BLOCKED",
    "ERROR_VPN_DISCONNECT",
    "ERROR_VPN_REFUSED",
    "ERROR_VPN_TIMEOUT",
    "ERROR_VPN_BAD_CERT",
    "ERROR_VPN_BAD_PSK",
    "ERROR_SERVER_POLICY",
    "ERROR_BROADBAND_ACTIVE",
    "ERROR_BROADBAND_NO_NIC",
    "ERROR_BROADBAND_TIMEOUT",
    "ERROR_FEATURE_DEPRECATED",
    "ERROR_CANNOT_DELETE",
    "ERROR_RASQEC_RESOURCE_CREATION_FAILED",
    "ERROR_RASQEC_NAPAGENT_NOT_ENABLED",
    "ERROR_RASQEC_NAPAGENT_NOT_CONNECTED",
    "ERROR_RASQEC_CONN_DOESNOTEXIST",
    "ERROR_RASQEC_TIMEOUT",
    "ERROR_PEAP_CRYPTOBINDING_INVALID",
    "ERROR_PEAP_CRYPTOBINDING_NOTRECEIVED",
    "ERROR_INVALID_VPNSTRATEGY",
    "ERROR_EAPTLS_CACHE_CREDENTIALS_INVALID",
    "ERROR_IPSEC_SERVICE_STOPPED",
    "ERROR_IDLE_TIMEOUT",
    "ERROR_LINK_FAILURE",
    "ERROR_USER_LOGOFF",
    "ERROR_FAST_USER_SWITCH",
    "ERROR_HIBERNATION",
    "ERROR_SYSTEM_SUSPENDED",
    "ERROR_RASMAN_SERVICE_STOPPED",
    "ERROR_INVALID_SERVER_CERT",
    "ERROR_NOT_NAP_CAPABLE",
    "ERROR_INVALID_TUNNELID",
    "ERROR_UPDATECONNECTION_REQUEST_IN_PROCESS",
    "ERROR_PROTOCOL_ENGINE_DISABLED",
    "ERROR_INTERNAL_ADDRESS_FAILURE",
    "ERROR_FAILED_CP_REQUIRED",
    "ERROR_TS_UNACCEPTABLE",
    "ERROR_MOBIKE_DISABLED",
    "ERROR_CANNOT_INITIATE_MOBIKE_UPDATE",
    "ERROR_PEAP_SERVER_REJECTED_CLIENT_TLV",
    "ERROR_INVALID_PREFERENCES",
    "ERROR_EAPTLS_SCARD_CACHE_CREDENTIALS_INVALID",
    "ERROR_SSTP_COOKIE_SET_FAILURE",
    "ERROR_INVALID_PEAP_COOKIE_ATTRIBUTES",
    "ERROR_EAP_METHOD_NOT_INSTALLED",
    "ERROR_EAP_METHOD_DOES_NOT_SUPPORT_SSO",
    "ERROR_EAP_METHOD_OPERATION_NOT_SUPPORTED",
    "ERROR_EAP_USER_CERT_INVALID",
    "ERROR_EAP_USER_CERT_EXPIRED",
    "ERROR_EAP_USER_CERT_REVOKED",
    "ERROR_EAP_USER_CERT_OTHER_ERROR",
    "ERROR_EAP_SERVER_CERT_INVALID",
    "ERROR_EAP_SERVER_CERT_EXPIRED",
    "ERROR_EAP_SERVER_CERT_REVOKED",
    "ERROR_EAP_SERVER_CERT_OTHER_ERROR",
    "ERROR_EAP_USER_ROOT_CERT_NOT_FOUND",
    "ERROR_EAP_USER_ROOT_CERT_INVALID",
    "ERROR_EAP_USER_ROOT_CERT_EXPIRED",
    "ERROR_EAP_SERVER_ROOT_CERT_NOT_FOUND",
    "ERROR_EAP_SERVER_ROOT_CERT_INVALID",
    "ERROR_EAP_SERVER_ROOT_CERT_NAME_REQUIRED",
    "ERROR_PEAP_IDENTITY_MISMATCH",
    "ERROR_DNSNAME_NOT_RESOLVABLE",
    "ERROR_EAPTLS_PASSWD_INVALID",
    "ERROR_IKEV2_PSK_INTERFACE_ALREADY_EXISTS",
    "ERROR_INVALID_DESTINATION_IP",
    "ERROR_INVALID_INTERFACE_CONFIG",
    "ERROR_VPN_PLUGIN_GENERIC",
    "ERROR_SSO_CERT_MISSING",
    "ERROR_DEVICE_COMPLIANCE",
    "ERROR_PLUGIN_NOT_INSTALLED",
    "ERROR_ACTION_REQUIRED",
    "RASBASEEND",
    "MPR_INTERFACE_DIAL_MODE",
    "MPRDM_DialFirst",
    "MPRDM_DialAll",
    "MPRDM_DialAsNeeded",
    "RASENTRY_DIAL_MODE",
    "RASEDM_DialAll",
    "RASEDM_DialAsNeeded",
    "RAS_FLAGS",
    "RAS_FLAGS_PPP_CONNECTION",
    "RAS_FLAGS_MESSENGER_PRESENT",
    "RAS_FLAGS_QUARANTINE_PRESENT",
    "RAS_FLAGS_ARAP_CONNECTION",
    "RAS_FLAGS_IKEV2_CONNECTION",
    "RAS_FLAGS_DORMANT",
    "MPR_ET",
    "MPR_ET_None",
    "MPR_ET_Require",
    "MPR_ET_RequireMax",
    "MPR_ET_Optional",
    "RASPPP_PROJECTION_INFO_SERVER_AUTH_DATA",
    "RASLCPAD_CHAP_MD5",
    "RASLCPAD_CHAP_MS",
    "RASLCPAD_CHAP_MSV2",
    "PPP_LCP",
    "PPP_LCP_PAP",
    "PPP_LCP_CHAP",
    "PPP_LCP_EAP",
    "PPP_LCP_SPAP",
    "RASPPP_PROJECTION_INFO_SERVER_AUTH_PROTOCOL",
    "RASLCPAP_PAP",
    "RASLCPAP_SPAP",
    "RASLCPAP_CHAP",
    "RASLCPAP_EAP",
    "PPP_LCP_INFO_AUTH_DATA",
    "PPP_LCP_CHAP_MD5",
    "PPP_LCP_CHAP_MS",
    "PPP_LCP_CHAP_MSV2",
    "RASIKEV_PROJECTION_INFO_FLAGS",
    "RASIKEv2_FLAGS_MOBIKESUPPORTED",
    "RASIKEv2_FLAGS_BEHIND_NAT",
    "RASIKEv2_FLAGS_SERVERBEHIND_NAT",
    "MPR_VS",
    "MPR_VS_Default",
    "MPR_VS_PptpOnly",
    "MPR_VS_PptpFirst",
    "MPR_VS_L2tpOnly",
    "MPR_VS_L2tpFirst",
    "SECURITY_MESSAGE_MSG_ID",
    "SECURITYMSG_SUCCESS",
    "SECURITYMSG_FAILURE",
    "SECURITYMSG_ERROR",
    "HRASCONN",
    "RASAPIVERSION",
    "RASAPIVERSION_500",
    "RASAPIVERSION_501",
    "RASAPIVERSION_600",
    "RASAPIVERSION_601",
    "RASIPADDR",
    "RASTUNNELENDPOINT",
    "RASCONNW",
    "RASCONNA",
    "RASCONNSTATE",
    "RASCS_OpenPort",
    "RASCS_PortOpened",
    "RASCS_ConnectDevice",
    "RASCS_DeviceConnected",
    "RASCS_AllDevicesConnected",
    "RASCS_Authenticate",
    "RASCS_AuthNotify",
    "RASCS_AuthRetry",
    "RASCS_AuthCallback",
    "RASCS_AuthChangePassword",
    "RASCS_AuthProject",
    "RASCS_AuthLinkSpeed",
    "RASCS_AuthAck",
    "RASCS_ReAuthenticate",
    "RASCS_Authenticated",
    "RASCS_PrepareForCallback",
    "RASCS_WaitForModemReset",
    "RASCS_WaitForCallback",
    "RASCS_Projected",
    "RASCS_StartAuthentication",
    "RASCS_CallbackComplete",
    "RASCS_LogonNetwork",
    "RASCS_SubEntryConnected",
    "RASCS_SubEntryDisconnected",
    "RASCS_ApplySettings",
    "RASCS_Interactive",
    "RASCS_RetryAuthentication",
    "RASCS_CallbackSetByCaller",
    "RASCS_PasswordExpired",
    "RASCS_InvokeEapUI",
    "RASCS_Connected",
    "RASCS_Disconnected",
    "RASCONNSUBSTATE",
    "RASCSS_None",
    "RASCSS_Dormant",
    "RASCSS_Reconnecting",
    "RASCSS_Reconnected",
    "RASCONNSTATUSW",
    "RASCONNSTATUSA",
    "RASDIALPARAMSW",
    "RASDIALPARAMSA",
    "RASEAPINFO",
    "RASDEVSPECIFICINFO",
    "RASDIALEXTENSIONS",
    "RASENTRYNAMEW",
    "RASENTRYNAMEA",
    "RASPROJECTION",
    "RASP_Amb",
    "RASP_PppNbf",
    "RASP_PppIpx",
    "RASP_PppIp",
    "RASP_PppCcp",
    "RASP_PppLcp",
    "RASP_PppIpv6",
    "RASAMBW",
    "RASAMBA",
    "RASPPPNBFW",
    "RASPPPNBFA",
    "RASIPXW",
    "RASPPPIPXA",
    "RASPPPIPW",
    "RASPPPIPA",
    "RASPPPIPV6",
    "RASPPPLCPW",
    "RASPPPLCPA",
    "RASPPPCCP",
    "RASPPP_PROJECTION_INFO",
    "RASIKEV2_PROJECTION_INFO",
    "RASPROJECTION_INFO_TYPE",
    "PROJECTION_INFO_TYPE_PPP",
    "PROJECTION_INFO_TYPE_IKEv2",
    "IKEV2_ID_PAYLOAD_TYPE",
    "IKEV2_ID_PAYLOAD_TYPE_INVALID",
    "IKEV2_ID_PAYLOAD_TYPE_IPV4_ADDR",
    "IKEV2_ID_PAYLOAD_TYPE_FQDN",
    "IKEV2_ID_PAYLOAD_TYPE_RFC822_ADDR",
    "IKEV2_ID_PAYLOAD_TYPE_RESERVED1",
    "IKEV2_ID_PAYLOAD_TYPE_ID_IPV6_ADDR",
    "IKEV2_ID_PAYLOAD_TYPE_RESERVED2",
    "IKEV2_ID_PAYLOAD_TYPE_RESERVED3",
    "IKEV2_ID_PAYLOAD_TYPE_RESERVED4",
    "IKEV2_ID_PAYLOAD_TYPE_DER_ASN1_DN",
    "IKEV2_ID_PAYLOAD_TYPE_DER_ASN1_GN",
    "IKEV2_ID_PAYLOAD_TYPE_KEY_ID",
    "IKEV2_ID_PAYLOAD_TYPE_MAX",
    "RAS_PROJECTION_INFO",
    "RASDIALFUNC",
    "RASDIALFUNC1",
    "RASDIALFUNC2",
    "RASDEVINFOW",
    "RASDEVINFOA",
    "RASCTRYINFO",
    "RASENTRYA",
    "RASENTRYW",
    "ORASADFUNC",
    "RASADPARAMS",
    "RASADFUNCA",
    "RASADFUNCW",
    "RASSUBENTRYA",
    "RASSUBENTRYW",
    "RASCREDENTIALSA",
    "RASCREDENTIALSW",
    "RASAUTODIALENTRYA",
    "RASAUTODIALENTRYW",
    "RASEAPUSERIDENTITYA",
    "RASEAPUSERIDENTITYW",
    "PFNRASGETBUFFER",
    "PFNRASFREEBUFFER",
    "PFNRASSENDBUFFER",
    "PFNRASRECEIVEBUFFER",
    "PFNRASRETRIEVEBUFFER",
    "RasCustomScriptExecuteFn",
    "RASCOMMSETTINGS",
    "PFNRASSETCOMMSETTINGS",
    "RASCUSTOMSCRIPTEXTENSIONS",
    "RAS_STATS",
    "RasCustomHangUpFn",
    "RasCustomDialFn",
    "RasCustomDeleteEntryNotifyFn",
    "RASUPDATECONN",
    "RASPBDLGFUNCW",
    "RASPBDLGFUNCA",
    "RASNOUSERW",
    "RASNOUSERA",
    "RASPBDLGW",
    "RASPBDLGA",
    "RASENTRYDLGW",
    "RASENTRYDLGA",
    "RASDIALDLG",
    "RasCustomDialDlgFn",
    "RasCustomEntryDlgFn",
    "ROUTER_INTERFACE_TYPE",
    "ROUTER_IF_TYPE_CLIENT",
    "ROUTER_IF_TYPE_HOME_ROUTER",
    "ROUTER_IF_TYPE_FULL_ROUTER",
    "ROUTER_IF_TYPE_DEDICATED",
    "ROUTER_IF_TYPE_INTERNAL",
    "ROUTER_IF_TYPE_LOOPBACK",
    "ROUTER_IF_TYPE_TUNNEL1",
    "ROUTER_IF_TYPE_DIALOUT",
    "ROUTER_IF_TYPE_MAX",
    "ROUTER_CONNECTION_STATE",
    "ROUTER_IF_STATE_UNREACHABLE",
    "ROUTER_IF_STATE_DISCONNECTED",
    "ROUTER_IF_STATE_CONNECTING",
    "ROUTER_IF_STATE_CONNECTED",
    "MPR_INTERFACE_0",
    "MPR_IPINIP_INTERFACE_0",
    "MPR_INTERFACE_1",
    "MPR_INTERFACE_2",
    "MPR_INTERFACE_3",
    "MPR_DEVICE_0",
    "MPR_DEVICE_1",
    "MPR_CREDENTIALSEX_0",
    "MPR_CREDENTIALSEX_1",
    "MPR_TRANSPORT_0",
    "MPR_IFTRANSPORT_0",
    "MPR_SERVER_0",
    "MPR_SERVER_1",
    "MPR_SERVER_2",
    "RAS_PORT_CONDITION",
    "RAS_PORT_NON_OPERATIONAL",
    "RAS_PORT_DISCONNECTED",
    "RAS_PORT_CALLING_BACK",
    "RAS_PORT_LISTENING",
    "RAS_PORT_AUTHENTICATING",
    "RAS_PORT_AUTHENTICATED",
    "RAS_PORT_INITIALIZING",
    "RAS_HARDWARE_CONDITION",
    "RAS_HARDWARE_OPERATIONAL",
    "RAS_HARDWARE_FAILURE",
    "RAS_PORT_0",
    "RAS_PORT_1",
    "RAS_PORT_2",
    "PPP_NBFCP_INFO",
    "PPP_IPCP_INFO",
    "PPP_IPCP_INFO2",
    "PPP_IPXCP_INFO",
    "PPP_ATCP_INFO",
    "PPP_IPV6_CP_INFO",
    "PPP_INFO",
    "PPP_CCP_INFO",
    "PPP_LCP_INFO",
    "PPP_INFO_2",
    "PPP_INFO_3",
    "RAS_CONNECTION_0",
    "RAS_CONNECTION_1",
    "RAS_CONNECTION_2",
    "RAS_QUARANTINE_STATE",
    "RAS_QUAR_STATE_NORMAL",
    "RAS_QUAR_STATE_QUARANTINE",
    "RAS_QUAR_STATE_PROBATION",
    "RAS_QUAR_STATE_NOT_CAPABLE",
    "RAS_CONNECTION_3",
    "RAS_USER_0",
    "RAS_USER_1",
    "MPR_FILTER_0",
    "MPRAPI_OBJECT_HEADER",
    "MPRAPI_OBJECT_TYPE",
    "MPRAPI_OBJECT_TYPE_RAS_CONNECTION_OBJECT",
    "MPRAPI_OBJECT_TYPE_MPR_SERVER_OBJECT",
    "MPRAPI_OBJECT_TYPE_MPR_SERVER_SET_CONFIG_OBJECT",
    "MPRAPI_OBJECT_TYPE_AUTH_VALIDATION_OBJECT",
    "MPRAPI_OBJECT_TYPE_UPDATE_CONNECTION_OBJECT",
    "MPRAPI_OBJECT_TYPE_IF_CUSTOM_CONFIG_OBJECT",
    "PPP_PROJECTION_INFO",
    "PPP_PROJECTION_INFO2",
    "IKEV2_PROJECTION_INFO",
    "IKEV2_PROJECTION_INFO2",
    "PROJECTION_INFO",
    "PROJECTION_INFO2",
    "RAS_CONNECTION_EX",
    "RAS_CONNECTION_4",
    "ROUTER_CUSTOM_IKEv2_POLICY0",
    "ROUTER_IKEv2_IF_CUSTOM_CONFIG0",
    "MPR_IF_CUSTOMINFOEX0",
    "MPR_CERT_EKU",
    "VPN_TS_IP_ADDRESS",
    "MPR_VPN_TS_TYPE",
    "MPR_VPN_TS_IPv4_ADDR_RANGE",
    "MPR_VPN_TS_IPv6_ADDR_RANGE",
    "_MPR_VPN_SELECTOR",
    "MPR_VPN_TRAFFIC_SELECTORS",
    "ROUTER_IKEv2_IF_CUSTOM_CONFIG2",
    "MPR_IF_CUSTOMINFOEX2",
    "IKEV2_TUNNEL_CONFIG_PARAMS4",
    "ROUTER_IKEv2_IF_CUSTOM_CONFIG1",
    "MPR_IF_CUSTOMINFOEX1",
    "IKEV2_TUNNEL_CONFIG_PARAMS3",
    "IKEV2_TUNNEL_CONFIG_PARAMS2",
    "L2TP_TUNNEL_CONFIG_PARAMS2",
    "L2TP_TUNNEL_CONFIG_PARAMS1",
    "IKEV2_CONFIG_PARAMS",
    "PPTP_CONFIG_PARAMS",
    "L2TP_CONFIG_PARAMS1",
    "GRE_CONFIG_PARAMS0",
    "L2TP_CONFIG_PARAMS0",
    "SSTP_CERT_INFO",
    "SSTP_CONFIG_PARAMS",
    "MPRAPI_TUNNEL_CONFIG_PARAMS0",
    "MPRAPI_TUNNEL_CONFIG_PARAMS1",
    "MPR_SERVER_EX0",
    "MPR_SERVER_EX1",
    "MPR_SERVER_SET_CONFIG_EX0",
    "MPR_SERVER_SET_CONFIG_EX1",
    "AUTH_VALIDATION_EX",
    "RAS_UPDATE_CONNECTION",
    "PMPRADMINGETIPADDRESSFORUSER",
    "PMPRADMINRELEASEIPADRESS",
    "PMPRADMINGETIPV6ADDRESSFORUSER",
    "PMPRADMINRELEASEIPV6ADDRESSFORUSER",
    "PMPRADMINACCEPTNEWCONNECTION",
    "PMPRADMINACCEPTNEWCONNECTION2",
    "PMPRADMINACCEPTNEWCONNECTION3",
    "PMPRADMINACCEPTNEWLINK",
    "PMPRADMINCONNECTIONHANGUPNOTIFICATION",
    "PMPRADMINCONNECTIONHANGUPNOTIFICATION2",
    "PMPRADMINCONNECTIONHANGUPNOTIFICATION3",
    "PMPRADMINLINKHANGUPNOTIFICATION",
    "PMPRADMINTERMINATEDLL",
    "PMPRADMINACCEPTREAUTHENTICATION",
    "PMPRADMINACCEPTNEWCONNECTIONEX",
    "PMPRADMINACCEPTREAUTHENTICATIONEX",
    "PMPRADMINACCEPTTUNNELENDPOINTCHANGEEX",
    "PMPRADMINCONNECTIONHANGUPNOTIFICATIONEX",
    "PMPRADMINRASVALIDATEPREAUTHENTICATEDCONNECTIONEX",
    "MPRAPI_ADMIN_DLL_CALLBACKS",
    "SECURITY_MESSAGE",
    "RAS_SECURITY_INFO",
    "RASSECURITYPROC",
    "MGM_IF_ENTRY",
    "PMGM_RPF_CALLBACK",
    "PMGM_CREATION_ALERT_CALLBACK",
    "PMGM_PRUNE_ALERT_CALLBACK",
    "PMGM_JOIN_ALERT_CALLBACK",
    "PMGM_WRONG_IF_CALLBACK",
    "PMGM_LOCAL_JOIN_CALLBACK",
    "PMGM_LOCAL_LEAVE_CALLBACK",
    "PMGM_DISABLE_IGMP_CALLBACK",
    "PMGM_ENABLE_IGMP_CALLBACK",
    "ROUTING_PROTOCOL_CONFIG",
    "MGM_ENUM_TYPES",
    "ANY_SOURCE",
    "ALL_SOURCES",
    "SOURCE_GROUP_ENTRY",
    "RTM_REGN_PROFILE",
    "RTM_NET_ADDRESS",
    "RTM_PREF_INFO",
    "RTM_NEXTHOP_LIST",
    "RTM_DEST_INFO",
    "RTM_ROUTE_INFO",
    "RTM_NEXTHOP_INFO",
    "RTM_ENTITY_ID",
    "RTM_ENTITY_INFO",
    "RTM_EVENT_TYPE",
    "RTM_ENTITY_REGISTERED",
    "RTM_ENTITY_DEREGISTERED",
    "RTM_ROUTE_EXPIRED",
    "RTM_CHANGE_NOTIFICATION",
    "RTM_EVENT_CALLBACK",
    "RTM_ENTITY_METHOD_INPUT",
    "RTM_ENTITY_METHOD_OUTPUT",
    "RTM_ENTITY_EXPORT_METHOD",
    "RTM_ENTITY_EXPORT_METHODS",
    "RasDialA",
    "RasDialW",
    "RasDial",
    "RasEnumConnectionsA",
    "RasEnumConnectionsW",
    "RasEnumConnections",
    "RasEnumEntriesA",
    "RasEnumEntriesW",
    "RasEnumEntries",
    "RasGetConnectStatusA",
    "RasGetConnectStatusW",
    "RasGetConnectStatus",
    "RasGetErrorStringA",
    "RasGetErrorStringW",
    "RasGetErrorString",
    "RasHangUpA",
    "RasHangUpW",
    "RasHangUp",
    "RasGetProjectionInfoA",
    "RasGetProjectionInfoW",
    "RasGetProjectionInfo",
    "RasCreatePhonebookEntryA",
    "RasCreatePhonebookEntryW",
    "RasCreatePhonebookEntry",
    "RasEditPhonebookEntryA",
    "RasEditPhonebookEntryW",
    "RasEditPhonebookEntry",
    "RasSetEntryDialParamsA",
    "RasSetEntryDialParamsW",
    "RasSetEntryDialParams",
    "RasGetEntryDialParamsA",
    "RasGetEntryDialParamsW",
    "RasGetEntryDialParams",
    "RasEnumDevicesA",
    "RasEnumDevicesW",
    "RasEnumDevices",
    "RasGetCountryInfoA",
    "RasGetCountryInfoW",
    "RasGetCountryInfo",
    "RasGetEntryPropertiesA",
    "RasGetEntryPropertiesW",
    "RasGetEntryProperties",
    "RasSetEntryPropertiesA",
    "RasSetEntryPropertiesW",
    "RasSetEntryProperties",
    "RasRenameEntryA",
    "RasRenameEntryW",
    "RasRenameEntry",
    "RasDeleteEntryA",
    "RasDeleteEntryW",
    "RasDeleteEntry",
    "RasValidateEntryNameA",
    "RasValidateEntryNameW",
    "RasValidateEntryName",
    "RasConnectionNotificationA",
    "RasConnectionNotificationW",
    "RasConnectionNotification",
    "RasGetSubEntryHandleA",
    "RasGetSubEntryHandleW",
    "RasGetSubEntryHandle",
    "RasGetCredentialsA",
    "RasGetCredentialsW",
    "RasGetCredentials",
    "RasSetCredentialsA",
    "RasSetCredentialsW",
    "RasSetCredentials",
    "RasGetSubEntryPropertiesA",
    "RasGetSubEntryPropertiesW",
    "RasGetSubEntryProperties",
    "RasSetSubEntryPropertiesA",
    "RasSetSubEntryPropertiesW",
    "RasSetSubEntryProperties",
    "RasGetAutodialAddressA",
    "RasGetAutodialAddressW",
    "RasGetAutodialAddress",
    "RasSetAutodialAddressA",
    "RasSetAutodialAddressW",
    "RasSetAutodialAddress",
    "RasEnumAutodialAddressesA",
    "RasEnumAutodialAddressesW",
    "RasEnumAutodialAddresses",
    "RasGetAutodialEnableA",
    "RasGetAutodialEnableW",
    "RasGetAutodialEnable",
    "RasSetAutodialEnableA",
    "RasSetAutodialEnableW",
    "RasSetAutodialEnable",
    "RasGetAutodialParamA",
    "RasGetAutodialParamW",
    "RasGetAutodialParam",
    "RasSetAutodialParamA",
    "RasSetAutodialParamW",
    "RasSetAutodialParam",
    "RasGetPCscf",
    "RasInvokeEapUI",
    "RasGetLinkStatistics",
    "RasGetConnectionStatistics",
    "RasClearLinkStatistics",
    "RasClearConnectionStatistics",
    "RasGetEapUserDataA",
    "RasGetEapUserDataW",
    "RasGetEapUserData",
    "RasSetEapUserDataA",
    "RasSetEapUserDataW",
    "RasSetEapUserData",
    "RasGetCustomAuthDataA",
    "RasGetCustomAuthDataW",
    "RasGetCustomAuthData",
    "RasSetCustomAuthDataA",
    "RasSetCustomAuthDataW",
    "RasSetCustomAuthData",
    "RasGetEapUserIdentityW",
    "RasGetEapUserIdentity",
    "RasGetEapUserIdentityA",
    "RasFreeEapUserIdentityW",
    "RasFreeEapUserIdentity",
    "RasFreeEapUserIdentityA",
    "RasDeleteSubEntryA",
    "RasDeleteSubEntryW",
    "RasDeleteSubEntry",
    "RasUpdateConnection",
    "RasGetProjectionInfoEx",
    "RasPhonebookDlgA",
    "RasPhonebookDlgW",
    "RasPhonebookDlg",
    "RasEntryDlgA",
    "RasEntryDlgW",
    "RasEntryDlg",
    "RasDialDlgA",
    "RasDialDlgW",
    "RasDialDlg",
    "MprAdminConnectionEnumEx",
    "MprAdminConnectionGetInfoEx",
    "MprAdminServerGetInfoEx",
    "MprAdminServerSetInfoEx",
    "MprConfigServerGetInfoEx",
    "MprConfigServerSetInfoEx",
    "MprAdminUpdateConnection",
    "MprAdminIsServiceInitialized",
    "MprAdminInterfaceSetCustomInfoEx",
    "MprAdminInterfaceGetCustomInfoEx",
    "MprConfigInterfaceGetCustomInfoEx",
    "MprConfigInterfaceSetCustomInfoEx",
    "MprAdminConnectionEnum",
    "MprAdminPortEnum",
    "MprAdminConnectionGetInfo",
    "MprAdminPortGetInfo",
    "MprAdminConnectionClearStats",
    "MprAdminPortClearStats",
    "MprAdminPortReset",
    "MprAdminPortDisconnect",
    "MprAdminConnectionRemoveQuarantine",
    "MprAdminUserGetInfo",
    "MprAdminUserSetInfo",
    "MprAdminSendUserMessage",
    "MprAdminGetPDCServer",
    "MprAdminIsServiceRunning",
    "MprAdminServerConnect",
    "MprAdminServerDisconnect",
    "MprAdminServerGetCredentials",
    "MprAdminServerSetCredentials",
    "MprAdminBufferFree",
    "MprAdminGetErrorString",
    "MprAdminServerGetInfo",
    "MprAdminServerSetInfo",
    "MprAdminEstablishDomainRasServer",
    "MprAdminIsDomainRasServer",
    "MprAdminTransportCreate",
    "MprAdminTransportSetInfo",
    "MprAdminTransportGetInfo",
    "MprAdminDeviceEnum",
    "MprAdminInterfaceGetHandle",
    "MprAdminInterfaceCreate",
    "MprAdminInterfaceGetInfo",
    "MprAdminInterfaceSetInfo",
    "MprAdminInterfaceDelete",
    "MprAdminInterfaceDeviceGetInfo",
    "MprAdminInterfaceDeviceSetInfo",
    "MprAdminInterfaceTransportRemove",
    "MprAdminInterfaceTransportAdd",
    "MprAdminInterfaceTransportGetInfo",
    "MprAdminInterfaceTransportSetInfo",
    "MprAdminInterfaceEnum",
    "MprAdminInterfaceSetCredentials",
    "MprAdminInterfaceGetCredentials",
    "MprAdminInterfaceSetCredentialsEx",
    "MprAdminInterfaceGetCredentialsEx",
    "MprAdminInterfaceConnect",
    "MprAdminInterfaceDisconnect",
    "MprAdminInterfaceUpdateRoutes",
    "MprAdminInterfaceQueryUpdateResult",
    "MprAdminInterfaceUpdatePhonebookInfo",
    "MprAdminRegisterConnectionNotification",
    "MprAdminDeregisterConnectionNotification",
    "MprAdminMIBServerConnect",
    "MprAdminMIBServerDisconnect",
    "MprAdminMIBEntryCreate",
    "MprAdminMIBEntryDelete",
    "MprAdminMIBEntrySet",
    "MprAdminMIBEntryGet",
    "MprAdminMIBEntryGetFirst",
    "MprAdminMIBEntryGetNext",
    "MprAdminMIBBufferFree",
    "MprConfigServerInstall",
    "MprConfigServerConnect",
    "MprConfigServerDisconnect",
    "MprConfigServerRefresh",
    "MprConfigBufferFree",
    "MprConfigServerGetInfo",
    "MprConfigServerSetInfo",
    "MprConfigServerBackup",
    "MprConfigServerRestore",
    "MprConfigTransportCreate",
    "MprConfigTransportDelete",
    "MprConfigTransportGetHandle",
    "MprConfigTransportSetInfo",
    "MprConfigTransportGetInfo",
    "MprConfigTransportEnum",
    "MprConfigInterfaceCreate",
    "MprConfigInterfaceDelete",
    "MprConfigInterfaceGetHandle",
    "MprConfigInterfaceGetInfo",
    "MprConfigInterfaceSetInfo",
    "MprConfigInterfaceEnum",
    "MprConfigInterfaceTransportAdd",
    "MprConfigInterfaceTransportRemove",
    "MprConfigInterfaceTransportGetHandle",
    "MprConfigInterfaceTransportGetInfo",
    "MprConfigInterfaceTransportSetInfo",
    "MprConfigInterfaceTransportEnum",
    "MprConfigGetFriendlyName",
    "MprConfigGetGuidName",
    "MprConfigFilterGetInfo",
    "MprConfigFilterSetInfo",
    "MprInfoCreate",
    "MprInfoDelete",
    "MprInfoRemoveAll",
    "MprInfoDuplicate",
    "MprInfoBlockAdd",
    "MprInfoBlockRemove",
    "MprInfoBlockSet",
    "MprInfoBlockFind",
    "MprInfoBlockQuerySize",
    "MgmRegisterMProtocol",
    "MgmDeRegisterMProtocol",
    "MgmTakeInterfaceOwnership",
    "MgmReleaseInterfaceOwnership",
    "MgmGetProtocolOnInterface",
    "MgmAddGroupMembershipEntry",
    "MgmDeleteGroupMembershipEntry",
    "MgmGetMfe",
    "MgmGetFirstMfe",
    "MgmGetNextMfe",
    "MgmGetMfeStats",
    "MgmGetFirstMfeStats",
    "MgmGetNextMfeStats",
    "MgmGroupEnumerationStart",
    "MgmGroupEnumerationGetNext",
    "MgmGroupEnumerationEnd",
    "RtmConvertNetAddressToIpv6AddressAndLength",
    "RtmConvertIpv6AddressAndLengthToNetAddress",
    "RtmRegisterEntity",
    "RtmDeregisterEntity",
    "RtmGetRegisteredEntities",
    "RtmReleaseEntities",
    "RtmLockDestination",
    "RtmGetOpaqueInformationPointer",
    "RtmGetEntityMethods",
    "RtmInvokeMethod",
    "RtmBlockMethods",
    "RtmGetEntityInfo",
    "RtmGetDestInfo",
    "RtmGetRouteInfo",
    "RtmGetNextHopInfo",
    "RtmReleaseEntityInfo",
    "RtmReleaseDestInfo",
    "RtmReleaseRouteInfo",
    "RtmReleaseNextHopInfo",
    "RtmAddRouteToDest",
    "RtmDeleteRouteToDest",
    "RtmHoldDestination",
    "RtmGetRoutePointer",
    "RtmLockRoute",
    "RtmUpdateAndUnlockRoute",
    "RtmGetExactMatchDestination",
    "RtmGetMostSpecificDestination",
    "RtmGetLessSpecificDestination",
    "RtmGetExactMatchRoute",
    "RtmIsBestRoute",
    "RtmAddNextHop",
    "RtmFindNextHop",
    "RtmDeleteNextHop",
    "RtmGetNextHopPointer",
    "RtmLockNextHop",
    "RtmCreateDestEnum",
    "RtmGetEnumDests",
    "RtmReleaseDests",
    "RtmCreateRouteEnum",
    "RtmGetEnumRoutes",
    "RtmReleaseRoutes",
    "RtmCreateNextHopEnum",
    "RtmGetEnumNextHops",
    "RtmReleaseNextHops",
    "RtmDeleteEnumHandle",
    "RtmRegisterForChangeNotification",
    "RtmGetChangedDests",
    "RtmReleaseChangedDests",
    "RtmIgnoreChangedDests",
    "RtmGetChangeStatus",
    "RtmMarkDestForChangeNotification",
    "RtmIsMarkedForChangeNotification",
    "RtmDeregisterFromChangeNotification",
    "RtmCreateRouteList",
    "RtmInsertInRouteList",
    "RtmCreateRouteListEnum",
    "RtmGetListEnumRoutes",
    "RtmDeleteRouteList",
    "RtmReferenceHandles",
]
