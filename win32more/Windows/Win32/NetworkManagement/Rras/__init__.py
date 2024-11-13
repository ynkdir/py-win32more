from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.NetworkManagement.IpHelper
import win32more.Windows.Win32.NetworkManagement.Rras
import win32more.Windows.Win32.Networking.WinSock
import win32more.Windows.Win32.Security.Cryptography
class AUTH_VALIDATION_EX(Structure):
    Header: win32more.Windows.Win32.NetworkManagement.Rras.MPRAPI_OBJECT_HEADER
    hRasConnection: win32more.Windows.Win32.Foundation.HANDLE
    wszUserName: Char * 257
    wszLogonDomain: Char * 16
    AuthInfoSize: UInt32
    AuthInfo: Byte * 1
RASNAP_ProbationTime: UInt32 = 1
RASTUNNELENDPOINT_UNKNOWN: UInt32 = 0
RASTUNNELENDPOINT_IPv4: UInt32 = 1
RASTUNNELENDPOINT_IPv6: UInt32 = 2
RAS_MaxDeviceType: UInt32 = 16
RAS_MaxPhoneNumber: UInt32 = 128
RAS_MaxIpAddress: UInt32 = 15
RAS_MaxIpxAddress: UInt32 = 21
RAS_MaxEntryName: UInt32 = 256
RAS_MaxDeviceName: UInt32 = 128
RAS_MaxCallbackNumber: UInt32 = 128
RAS_MaxAreaCode: UInt32 = 10
RAS_MaxPadType: UInt32 = 32
RAS_MaxX25Address: UInt32 = 200
RAS_MaxFacilities: UInt32 = 200
RAS_MaxUserData: UInt32 = 200
RAS_MaxReplyMessage: UInt32 = 1024
RAS_MaxDnsSuffix: UInt32 = 256
RASCF_AllUsers: UInt32 = 1
RASCF_GlobalCreds: UInt32 = 2
RASCF_OwnerKnown: UInt32 = 4
RASCF_OwnerMatch: UInt32 = 8
RAS_MaxIDSize: UInt32 = 256
RASCS_PAUSED: UInt32 = 4096
RASCS_DONE: UInt32 = 8192
RASCSS_DONE: UInt32 = 8192
RDEOPT_UsePrefixSuffix: UInt32 = 1
RDEOPT_PausedStates: UInt32 = 2
RDEOPT_IgnoreModemSpeaker: UInt32 = 4
RDEOPT_SetModemSpeaker: UInt32 = 8
RDEOPT_IgnoreSoftwareCompression: UInt32 = 16
RDEOPT_SetSoftwareCompression: UInt32 = 32
RDEOPT_DisableConnectedUI: UInt32 = 64
RDEOPT_DisableReconnectUI: UInt32 = 128
RDEOPT_DisableReconnect: UInt32 = 256
RDEOPT_NoUser: UInt32 = 512
RDEOPT_PauseOnScript: UInt32 = 1024
RDEOPT_Router: UInt32 = 2048
RDEOPT_CustomDial: UInt32 = 4096
RDEOPT_UseCustomScripting: UInt32 = 8192
RDEOPT_InvokeAutoTriggerCredentialUI: UInt32 = 16384
RDEOPT_EapInfoCryptInCapable: UInt32 = 32768
REN_User: UInt32 = 0
REN_AllUsers: UInt32 = 1
RASIPO_VJ: UInt32 = 1
RASLCPO_PFC: UInt32 = 1
RASLCPO_ACFC: UInt32 = 2
RASLCPO_SSHF: UInt32 = 4
RASLCPO_DES_56: UInt32 = 8
RASLCPO_3_DES: UInt32 = 16
RASLCPO_AES_128: UInt32 = 32
RASLCPO_AES_256: UInt32 = 64
RASLCPO_AES_192: UInt32 = 128
RASLCPO_GCM_AES_128: UInt32 = 256
RASLCPO_GCM_AES_192: UInt32 = 512
RASLCPO_GCM_AES_256: UInt32 = 1024
RASCCPCA_MPPC: UInt32 = 6
RASCCPCA_STAC: UInt32 = 5
RASCCPO_Compression: UInt32 = 1
RASCCPO_HistoryLess: UInt32 = 2
RASCCPO_Encryption56bit: UInt32 = 16
RASCCPO_Encryption40bit: UInt32 = 32
RASCCPO_Encryption128bit: UInt32 = 64
RASIKEv2_AUTH_MACHINECERTIFICATES: UInt32 = 1
RASIKEv2_AUTH_EAP: UInt32 = 2
RASIKEv2_AUTH_PSK: UInt32 = 3
RASDIALEVENT: String = 'RasDialEvent'
WM_RASDIALEVENT: UInt32 = 52429
ET_None: UInt32 = 0
ET_Require: UInt32 = 1
ET_RequireMax: UInt32 = 2
ET_Optional: UInt32 = 3
VS_Default: UInt32 = 0
VS_PptpOnly: UInt32 = 1
VS_PptpFirst: UInt32 = 2
VS_L2tpOnly: UInt32 = 3
VS_L2tpFirst: UInt32 = 4
VS_SstpOnly: UInt32 = 5
VS_SstpFirst: UInt32 = 6
VS_Ikev2Only: UInt32 = 7
VS_Ikev2First: UInt32 = 8
VS_GREOnly: UInt32 = 9
VS_PptpSstp: UInt32 = 12
VS_L2tpSstp: UInt32 = 13
VS_Ikev2Sstp: UInt32 = 14
VS_ProtocolList: UInt32 = 15
RASEO_UseCountryAndAreaCodes: UInt32 = 1
RASEO_SpecificIpAddr: UInt32 = 2
RASEO_SpecificNameServers: UInt32 = 4
RASEO_IpHeaderCompression: UInt32 = 8
RASEO_RemoteDefaultGateway: UInt32 = 16
RASEO_DisableLcpExtensions: UInt32 = 32
RASEO_TerminalBeforeDial: UInt32 = 64
RASEO_TerminalAfterDial: UInt32 = 128
RASEO_ModemLights: UInt32 = 256
RASEO_SwCompression: UInt32 = 512
RASEO_RequireEncryptedPw: UInt32 = 1024
RASEO_RequireMsEncryptedPw: UInt32 = 2048
RASEO_RequireDataEncryption: UInt32 = 4096
RASEO_NetworkLogon: UInt32 = 8192
RASEO_UseLogonCredentials: UInt32 = 16384
RASEO_PromoteAlternates: UInt32 = 32768
RASEO_SecureLocalFiles: UInt32 = 65536
RASEO_RequireEAP: UInt32 = 131072
RASEO_RequirePAP: UInt32 = 262144
RASEO_RequireSPAP: UInt32 = 524288
RASEO_Custom: UInt32 = 1048576
RASEO_PreviewPhoneNumber: UInt32 = 2097152
RASEO_SharedPhoneNumbers: UInt32 = 8388608
RASEO_PreviewUserPw: UInt32 = 16777216
RASEO_PreviewDomain: UInt32 = 33554432
RASEO_ShowDialingProgress: UInt32 = 67108864
RASEO_RequireCHAP: UInt32 = 134217728
RASEO_RequireMsCHAP: UInt32 = 268435456
RASEO_RequireMsCHAP2: UInt32 = 536870912
RASEO_RequireW95MSCHAP: UInt32 = 1073741824
RASEO_CustomScript: UInt32 = 2147483648
RASEO2_SecureFileAndPrint: UInt32 = 1
RASEO2_SecureClientForMSNet: UInt32 = 2
RASEO2_DontNegotiateMultilink: UInt32 = 4
RASEO2_DontUseRasCredentials: UInt32 = 8
RASEO2_UsePreSharedKey: UInt32 = 16
RASEO2_Internet: UInt32 = 32
RASEO2_DisableNbtOverIP: UInt32 = 64
RASEO2_UseGlobalDeviceSettings: UInt32 = 128
RASEO2_ReconnectIfDropped: UInt32 = 256
RASEO2_SharePhoneNumbers: UInt32 = 512
RASEO2_SecureRoutingCompartment: UInt32 = 1024
RASEO2_UseTypicalSettings: UInt32 = 2048
RASEO2_IPv6SpecificNameServers: UInt32 = 4096
RASEO2_IPv6RemoteDefaultGateway: UInt32 = 8192
RASEO2_RegisterIpWithDNS: UInt32 = 16384
RASEO2_UseDNSSuffixForRegistration: UInt32 = 32768
RASEO2_IPv4ExplicitMetric: UInt32 = 65536
RASEO2_IPv6ExplicitMetric: UInt32 = 131072
RASEO2_DisableIKENameEkuCheck: UInt32 = 262144
RASEO2_DisableClassBasedStaticRoute: UInt32 = 524288
RASEO2_SpecificIPv6Addr: UInt32 = 1048576
RASEO2_DisableMobility: UInt32 = 2097152
RASEO2_RequireMachineCertificates: UInt32 = 4194304
RASEO2_UsePreSharedKeyForIkev2Initiator: UInt32 = 8388608
RASEO2_UsePreSharedKeyForIkev2Responder: UInt32 = 16777216
RASEO2_CacheCredentials: UInt32 = 33554432
RASEO2_AutoTriggerCapable: UInt32 = 67108864
RASEO2_IsThirdPartyProfile: UInt32 = 134217728
RASEO2_AuthTypeIsOtp: UInt32 = 268435456
RASEO2_IsAlwaysOn: UInt32 = 536870912
RASEO2_IsPrivateNetwork: UInt32 = 1073741824
RASEO2_PlumbIKEv2TSAsRoutes: UInt32 = 2147483648
RASNP_NetBEUI: UInt32 = 1
RASNP_Ipx: UInt32 = 2
RASNP_Ip: UInt32 = 4
RASNP_Ipv6: UInt32 = 8
RASFP_Ppp: UInt32 = 1
RASFP_Slip: UInt32 = 2
RASFP_Ras: UInt32 = 4
RASDT_Modem: String = 'modem'
RASDT_Isdn: String = 'isdn'
RASDT_X25: String = 'x25'
RASDT_Vpn: String = 'vpn'
RASDT_Pad: String = 'pad'
RASDT_Generic: String = 'GENERIC'
RASDT_Serial: String = 'SERIAL'
RASDT_FrameRelay: String = 'FRAMERELAY'
RASDT_Atm: String = 'ATM'
RASDT_Sonet: String = 'SONET'
RASDT_SW56: String = 'SW56'
RASDT_Irda: String = 'IRDA'
RASDT_Parallel: String = 'PARALLEL'
RASDT_PPPoE: String = 'PPPoE'
RASET_Phone: UInt32 = 1
RASET_Vpn: UInt32 = 2
RASET_Direct: UInt32 = 3
RASET_Internet: UInt32 = 4
RASET_Broadband: UInt32 = 5
RASCN_Connection: UInt32 = 1
RASCN_Disconnection: UInt32 = 2
RASCN_BandwidthAdded: UInt32 = 4
RASCN_BandwidthRemoved: UInt32 = 8
RASCN_Dormant: UInt32 = 16
RASCN_ReConnection: UInt32 = 32
RASCN_EPDGPacketArrival: UInt32 = 64
RASIDS_Disabled: UInt32 = 4294967295
RASIDS_UseGlobalValue: UInt32 = 0
RASADFLG_PositionDlg: UInt32 = 1
RASCM_UserName: UInt32 = 1
RASCM_Password: UInt32 = 2
RASCM_Domain: UInt32 = 4
RASCM_DefaultCreds: UInt32 = 8
RASCM_PreSharedKey: UInt32 = 16
RASCM_ServerPreSharedKey: UInt32 = 32
RASCM_DDMPreSharedKey: UInt32 = 64
RASADP_DisableConnectionQuery: UInt32 = 0
RASADP_LoginSessionDisable: UInt32 = 1
RASADP_SavedAddressesLimit: UInt32 = 2
RASADP_FailedConnectionTimeout: UInt32 = 3
RASADP_ConnectionQueryTimeout: UInt32 = 4
RASEAPF_NonInteractive: UInt32 = 2
RASEAPF_Logon: UInt32 = 4
RASEAPF_Preview: UInt32 = 8
RCD_SingleUser: UInt32 = 0
RCD_AllUsers: UInt32 = 1
RCD_Eap: UInt32 = 2
RCD_Logon: UInt32 = 4
RASPBDEVENT_AddEntry: UInt32 = 1
RASPBDEVENT_EditEntry: UInt32 = 2
RASPBDEVENT_RemoveEntry: UInt32 = 3
RASPBDEVENT_DialEntry: UInt32 = 4
RASPBDEVENT_EditGlobals: UInt32 = 5
RASPBDEVENT_NoUser: UInt32 = 6
RASPBDEVENT_NoUserEdit: UInt32 = 7
RASNOUSER_SmartCard: UInt32 = 1
RASPBDFLAG_PositionDlg: UInt32 = 1
RASPBDFLAG_ForceCloseOnDial: UInt32 = 2
RASPBDFLAG_NoUser: UInt32 = 16
RASPBDFLAG_UpdateDefaults: UInt32 = 2147483648
RASEDFLAG_PositionDlg: UInt32 = 1
RASEDFLAG_NewEntry: UInt32 = 2
RASEDFLAG_CloneEntry: UInt32 = 4
RASEDFLAG_NoRename: UInt32 = 8
RASEDFLAG_ShellOwned: UInt32 = 1073741824
RASEDFLAG_NewPhoneEntry: UInt32 = 16
RASEDFLAG_NewTunnelEntry: UInt32 = 32
RASEDFLAG_NewDirectEntry: UInt32 = 64
RASEDFLAG_NewBroadbandEntry: UInt32 = 128
RASEDFLAG_InternetEntry: UInt32 = 256
RASEDFLAG_NAT: UInt32 = 512
RASEDFLAG_IncomingConnection: UInt32 = 1024
RASDDFLAG_PositionDlg: UInt32 = 1
RASDDFLAG_NoPrompt: UInt32 = 2
RASDDFLAG_AoacRedial: UInt32 = 4
RASDDFLAG_LinkFailure: UInt32 = 2147483648
RRAS_SERVICE_NAME: String = 'RemoteAccess'
PID_IPX: UInt32 = 43
PID_IP: UInt32 = 33
PID_IPV6: UInt32 = 87
PID_NBF: UInt32 = 63
PID_ATALK: UInt32 = 41
MPR_INTERFACE_OUT_OF_RESOURCES: UInt32 = 1
MPR_INTERFACE_ADMIN_DISABLED: UInt32 = 2
MPR_INTERFACE_CONNECTION_FAILURE: UInt32 = 4
MPR_INTERFACE_SERVICE_PAUSED: UInt32 = 8
MPR_INTERFACE_DIALOUT_HOURS_RESTRICTION: UInt32 = 16
MPR_INTERFACE_NO_MEDIA_SENSE: UInt32 = 32
MPR_INTERFACE_NO_DEVICE: UInt32 = 64
MPR_MaxDeviceType: UInt32 = 16
MPR_MaxPhoneNumber: UInt32 = 128
MPR_MaxIpAddress: UInt32 = 15
MPR_MaxIpxAddress: UInt32 = 21
MPR_MaxEntryName: UInt32 = 256
MPR_MaxDeviceName: UInt32 = 128
MPR_MaxCallbackNumber: UInt32 = 128
MPR_MaxAreaCode: UInt32 = 10
MPR_MaxPadType: UInt32 = 32
MPR_MaxX25Address: UInt32 = 200
MPR_MaxFacilities: UInt32 = 200
MPR_MaxUserData: UInt32 = 200
MPRIO_SpecificIpAddr: UInt32 = 2
MPRIO_SpecificNameServers: UInt32 = 4
MPRIO_IpHeaderCompression: UInt32 = 8
MPRIO_RemoteDefaultGateway: UInt32 = 16
MPRIO_DisableLcpExtensions: UInt32 = 32
MPRIO_SwCompression: UInt32 = 512
MPRIO_RequireEncryptedPw: UInt32 = 1024
MPRIO_RequireMsEncryptedPw: UInt32 = 2048
MPRIO_RequireDataEncryption: UInt32 = 4096
MPRIO_NetworkLogon: UInt32 = 8192
MPRIO_PromoteAlternates: UInt32 = 32768
MPRIO_SecureLocalFiles: UInt32 = 65536
MPRIO_RequireEAP: UInt32 = 131072
MPRIO_RequirePAP: UInt32 = 262144
MPRIO_RequireSPAP: UInt32 = 524288
MPRIO_SharedPhoneNumbers: UInt32 = 8388608
MPRIO_RequireCHAP: UInt32 = 134217728
MPRIO_RequireMsCHAP: UInt32 = 268435456
MPRIO_RequireMsCHAP2: UInt32 = 536870912
MPRIO_IpSecPreSharedKey: UInt32 = 2147483648
MPRIO_RequireMachineCertificates: UInt32 = 16777216
MPRIO_UsePreSharedKeyForIkev2Initiator: UInt32 = 33554432
MPRIO_UsePreSharedKeyForIkev2Responder: UInt32 = 67108864
MPRNP_Ipx: UInt32 = 2
MPRNP_Ip: UInt32 = 4
MPRNP_Ipv6: UInt32 = 8
MPRDT_Modem: String = 'modem'
MPRDT_Isdn: String = 'isdn'
MPRDT_X25: String = 'x25'
MPRDT_Vpn: String = 'vpn'
MPRDT_Pad: String = 'pad'
MPRDT_Generic: String = 'GENERIC'
MPRDT_Serial: String = 'SERIAL'
MPRDT_FrameRelay: String = 'FRAMERELAY'
MPRDT_Atm: String = 'ATM'
MPRDT_Sonet: String = 'SONET'
MPRDT_SW56: String = 'SW56'
MPRDT_Irda: String = 'IRDA'
MPRDT_Parallel: String = 'PARALLEL'
MPRET_Phone: UInt32 = 1
MPRET_Vpn: UInt32 = 2
MPRET_Direct: UInt32 = 3
MPRIDS_Disabled: UInt32 = 4294967295
MPRIDS_UseGlobalValue: UInt32 = 0
MPR_VS_Ikev2Only: UInt32 = 7
MPR_VS_Ikev2First: UInt32 = 8
MPR_ENABLE_RAS_ON_DEVICE: UInt32 = 1
MPR_ENABLE_ROUTING_ON_DEVICE: UInt32 = 2
IPADDRESSLEN: UInt32 = 15
IPXADDRESSLEN: UInt32 = 22
ATADDRESSLEN: UInt32 = 32
MAXIPADRESSLEN: UInt32 = 64
PPP_IPCP_VJ: UInt32 = 1
PPP_CCP_COMPRESSION: UInt32 = 1
PPP_CCP_ENCRYPTION40BITOLD: UInt32 = 16
PPP_CCP_ENCRYPTION40BIT: UInt32 = 32
PPP_CCP_ENCRYPTION128BIT: UInt32 = 64
PPP_CCP_ENCRYPTION56BIT: UInt32 = 128
PPP_CCP_HISTORYLESS: UInt32 = 16777216
PPP_LCP_MULTILINK_FRAMING: UInt32 = 1
PPP_LCP_PFC: UInt32 = 2
PPP_LCP_ACFC: UInt32 = 4
PPP_LCP_SSHF: UInt32 = 8
PPP_LCP_DES_56: UInt32 = 16
PPP_LCP_3_DES: UInt32 = 32
PPP_LCP_AES_128: UInt32 = 64
PPP_LCP_AES_256: UInt32 = 128
PPP_LCP_AES_192: UInt32 = 256
PPP_LCP_GCM_AES_128: UInt32 = 512
PPP_LCP_GCM_AES_192: UInt32 = 1024
PPP_LCP_GCM_AES_256: UInt32 = 2048
RAS_FLAGS_RAS_CONNECTION: UInt32 = 4
RASPRIV_NoCallback: UInt32 = 1
RASPRIV_AdminSetCallback: UInt32 = 2
RASPRIV_CallerSetCallback: UInt32 = 4
RASPRIV_DialinPrivilege: UInt32 = 8
RASPRIV2_DialinPolicy: UInt32 = 1
MPRAPI_IKEV2_AUTH_USING_CERT: UInt32 = 1
MPRAPI_IKEV2_AUTH_USING_EAP: UInt32 = 2
MPRAPI_PPP_PROJECTION_INFO_TYPE: UInt32 = 1
MPRAPI_IKEV2_PROJECTION_INFO_TYPE: UInt32 = 2
MPRAPI_RAS_CONNECTION_OBJECT_REVISION_1: UInt32 = 1
MPRAPI_MPR_IF_CUSTOM_CONFIG_OBJECT_REVISION_1: UInt32 = 1
MPRAPI_IF_CUSTOM_CONFIG_FOR_IKEV2: UInt32 = 1
MPRAPI_MPR_IF_CUSTOM_CONFIG_OBJECT_REVISION_3: UInt32 = 3
MPRAPI_MPR_IF_CUSTOM_CONFIG_OBJECT_REVISION_2: UInt32 = 2
MPRAPI_IKEV2_SET_TUNNEL_CONFIG_PARAMS: UInt32 = 1
MPRAPI_L2TP_SET_TUNNEL_CONFIG_PARAMS: UInt32 = 1
MAX_SSTP_HASH_SIZE: UInt32 = 32
MPRAPI_MPR_SERVER_OBJECT_REVISION_1: UInt32 = 1
MPRAPI_MPR_SERVER_OBJECT_REVISION_2: UInt32 = 2
MPRAPI_MPR_SERVER_OBJECT_REVISION_3: UInt32 = 3
MPRAPI_MPR_SERVER_OBJECT_REVISION_4: UInt32 = 4
MPRAPI_MPR_SERVER_OBJECT_REVISION_5: UInt32 = 5
MPRAPI_MPR_SERVER_SET_CONFIG_OBJECT_REVISION_1: UInt32 = 1
MPRAPI_MPR_SERVER_SET_CONFIG_OBJECT_REVISION_2: UInt32 = 2
MPRAPI_MPR_SERVER_SET_CONFIG_OBJECT_REVISION_3: UInt32 = 3
MPRAPI_MPR_SERVER_SET_CONFIG_OBJECT_REVISION_4: UInt32 = 4
MPRAPI_MPR_SERVER_SET_CONFIG_OBJECT_REVISION_5: UInt32 = 5
MPRAPI_SET_CONFIG_PROTOCOL_FOR_PPTP: UInt32 = 1
MPRAPI_SET_CONFIG_PROTOCOL_FOR_L2TP: UInt32 = 2
MPRAPI_SET_CONFIG_PROTOCOL_FOR_SSTP: UInt32 = 4
MPRAPI_SET_CONFIG_PROTOCOL_FOR_IKEV2: UInt32 = 8
MPRAPI_SET_CONFIG_PROTOCOL_FOR_GRE: UInt32 = 16
ALLOW_NO_AUTH: UInt32 = 1
DO_NOT_ALLOW_NO_AUTH: UInt32 = 0
MPRAPI_RAS_UPDATE_CONNECTION_OBJECT_REVISION_1: UInt32 = 1
MPRAPI_ADMIN_DLL_VERSION_1: UInt32 = 1
MPRAPI_ADMIN_DLL_VERSION_2: UInt32 = 2
MGM_JOIN_STATE_FLAG: UInt32 = 1
MGM_FORWARD_STATE_FLAG: UInt32 = 2
MGM_MFE_STATS_0: UInt32 = 1
MGM_MFE_STATS_1: UInt32 = 2
RTM_MAX_ADDRESS_SIZE: UInt32 = 16
RTM_MAX_VIEWS: UInt32 = 32
RTM_VIEW_ID_UCAST: UInt32 = 0
RTM_VIEW_ID_MCAST: UInt32 = 1
RTM_VIEW_MASK_SIZE: UInt32 = 32
RTM_VIEW_MASK_NONE: UInt32 = 0
RTM_VIEW_MASK_ANY: UInt32 = 0
RTM_VIEW_MASK_UCAST: UInt32 = 1
RTM_VIEW_MASK_MCAST: UInt32 = 2
RTM_VIEW_MASK_ALL: UInt32 = 4294967295
IPV6_ADDRESS_LEN_IN_BYTES: UInt32 = 16
RTM_DEST_FLAG_NATURAL_NET: UInt32 = 1
RTM_DEST_FLAG_FWD_ENGIN_ADD: UInt32 = 2
RTM_DEST_FLAG_DONT_FORWARD: UInt32 = 4
RTM_ROUTE_STATE_CREATED: UInt32 = 0
RTM_ROUTE_STATE_DELETING: UInt32 = 1
RTM_ROUTE_STATE_DELETED: UInt32 = 2
RTM_ROUTE_FLAGS_MARTIAN: UInt32 = 1
RTM_ROUTE_FLAGS_BLACKHOLE: UInt32 = 2
RTM_ROUTE_FLAGS_DISCARD: UInt32 = 4
RTM_ROUTE_FLAGS_INACTIVE: UInt32 = 8
RTM_ROUTE_FLAGS_LOCAL: UInt32 = 16
RTM_ROUTE_FLAGS_REMOTE: UInt32 = 32
RTM_ROUTE_FLAGS_MYSELF: UInt32 = 64
RTM_ROUTE_FLAGS_LOOPBACK: UInt32 = 128
RTM_ROUTE_FLAGS_MCAST: UInt32 = 256
RTM_ROUTE_FLAGS_LOCAL_MCAST: UInt32 = 512
RTM_ROUTE_FLAGS_LIMITED_BC: UInt32 = 1024
RTM_ROUTE_FLAGS_ZEROS_NETBC: UInt32 = 4096
RTM_ROUTE_FLAGS_ZEROS_SUBNETBC: UInt32 = 8192
RTM_ROUTE_FLAGS_ONES_NETBC: UInt32 = 16384
RTM_ROUTE_FLAGS_ONES_SUBNETBC: UInt32 = 32768
RTM_NEXTHOP_STATE_CREATED: UInt32 = 0
RTM_NEXTHOP_STATE_DELETED: UInt32 = 1
RTM_NEXTHOP_FLAGS_REMOTE: UInt32 = 1
RTM_NEXTHOP_FLAGS_DOWN: UInt32 = 2
METHOD_TYPE_ALL_METHODS: UInt32 = 4294967295
METHOD_RIP2_NEIGHBOUR_ADDR: UInt32 = 1
METHOD_RIP2_OUTBOUND_INTF: UInt32 = 2
METHOD_RIP2_ROUTE_TAG: UInt32 = 4
METHOD_RIP2_ROUTE_TIMESTAMP: UInt32 = 8
METHOD_BGP4_AS_PATH: UInt32 = 1
METHOD_BGP4_PEER_ID: UInt32 = 2
METHOD_BGP4_PA_ORIGIN: UInt32 = 4
METHOD_BGP4_NEXTHOP_ATTR: UInt32 = 8
RTM_RESUME_METHODS: UInt32 = 0
RTM_BLOCK_METHODS: UInt32 = 1
RTM_ROUTE_CHANGE_FIRST: UInt32 = 1
RTM_ROUTE_CHANGE_NEW: UInt32 = 2
RTM_ROUTE_CHANGE_BEST: UInt32 = 65536
RTM_NEXTHOP_CHANGE_NEW: UInt32 = 1
RTM_MATCH_NONE: UInt32 = 0
RTM_MATCH_OWNER: UInt32 = 1
RTM_MATCH_NEIGHBOUR: UInt32 = 2
RTM_MATCH_PREF: UInt32 = 4
RTM_MATCH_NEXTHOP: UInt32 = 8
RTM_MATCH_INTERFACE: UInt32 = 16
RTM_MATCH_FULL: UInt32 = 65535
RTM_ENUM_START: UInt32 = 0
RTM_ENUM_NEXT: UInt32 = 1
RTM_ENUM_RANGE: UInt32 = 2
RTM_ENUM_ALL_DESTS: UInt32 = 0
RTM_ENUM_OWN_DESTS: UInt32 = 16777216
RTM_ENUM_ALL_ROUTES: UInt32 = 0
RTM_ENUM_OWN_ROUTES: UInt32 = 65536
RTM_NUM_CHANGE_TYPES: UInt32 = 3
RTM_CHANGE_TYPE_ALL: UInt32 = 1
RTM_CHANGE_TYPE_BEST: UInt32 = 2
RTM_CHANGE_TYPE_FORWARDING: UInt32 = 4
RTM_NOTIFY_ONLY_MARKED_DESTS: UInt32 = 65536
RASBASE: UInt32 = 600
PENDING: UInt32 = 600
ERROR_INVALID_PORT_HANDLE: UInt32 = 601
ERROR_PORT_ALREADY_OPEN: UInt32 = 602
ERROR_BUFFER_TOO_SMALL: UInt32 = 603
ERROR_WRONG_INFO_SPECIFIED: UInt32 = 604
ERROR_CANNOT_SET_PORT_INFO: UInt32 = 605
ERROR_PORT_NOT_CONNECTED: UInt32 = 606
ERROR_EVENT_INVALID: UInt32 = 607
ERROR_DEVICE_DOES_NOT_EXIST: UInt32 = 608
ERROR_DEVICETYPE_DOES_NOT_EXIST: UInt32 = 609
ERROR_BUFFER_INVALID: UInt32 = 610
ERROR_ROUTE_NOT_AVAILABLE: UInt32 = 611
ERROR_ROUTE_NOT_ALLOCATED: UInt32 = 612
ERROR_INVALID_COMPRESSION_SPECIFIED: UInt32 = 613
ERROR_OUT_OF_BUFFERS: UInt32 = 614
ERROR_PORT_NOT_FOUND: UInt32 = 615
ERROR_ASYNC_REQUEST_PENDING: UInt32 = 616
ERROR_ALREADY_DISCONNECTING: UInt32 = 617
ERROR_PORT_NOT_OPEN: UInt32 = 618
ERROR_PORT_DISCONNECTED: UInt32 = 619
ERROR_NO_ENDPOINTS: UInt32 = 620
ERROR_CANNOT_OPEN_PHONEBOOK: UInt32 = 621
ERROR_CANNOT_LOAD_PHONEBOOK: UInt32 = 622
ERROR_CANNOT_FIND_PHONEBOOK_ENTRY: UInt32 = 623
ERROR_CANNOT_WRITE_PHONEBOOK: UInt32 = 624
ERROR_CORRUPT_PHONEBOOK: UInt32 = 625
ERROR_CANNOT_LOAD_STRING: UInt32 = 626
ERROR_KEY_NOT_FOUND: UInt32 = 627
ERROR_DISCONNECTION: UInt32 = 628
ERROR_REMOTE_DISCONNECTION: UInt32 = 629
ERROR_HARDWARE_FAILURE: UInt32 = 630
ERROR_USER_DISCONNECTION: UInt32 = 631
ERROR_INVALID_SIZE: UInt32 = 632
ERROR_PORT_NOT_AVAILABLE: UInt32 = 633
ERROR_CANNOT_PROJECT_CLIENT: UInt32 = 634
ERROR_UNKNOWN: UInt32 = 635
ERROR_WRONG_DEVICE_ATTACHED: UInt32 = 636
ERROR_BAD_STRING: UInt32 = 637
ERROR_REQUEST_TIMEOUT: UInt32 = 638
ERROR_CANNOT_GET_LANA: UInt32 = 639
ERROR_NETBIOS_ERROR: UInt32 = 640
ERROR_SERVER_OUT_OF_RESOURCES: UInt32 = 641
ERROR_NAME_EXISTS_ON_NET: UInt32 = 642
ERROR_SERVER_GENERAL_NET_FAILURE: UInt32 = 643
WARNING_MSG_ALIAS_NOT_ADDED: UInt32 = 644
ERROR_AUTH_INTERNAL: UInt32 = 645
ERROR_RESTRICTED_LOGON_HOURS: UInt32 = 646
ERROR_ACCT_DISABLED: UInt32 = 647
ERROR_PASSWD_EXPIRED: UInt32 = 648
ERROR_NO_DIALIN_PERMISSION: UInt32 = 649
ERROR_SERVER_NOT_RESPONDING: UInt32 = 650
ERROR_FROM_DEVICE: UInt32 = 651
ERROR_UNRECOGNIZED_RESPONSE: UInt32 = 652
ERROR_MACRO_NOT_FOUND: UInt32 = 653
ERROR_MACRO_NOT_DEFINED: UInt32 = 654
ERROR_MESSAGE_MACRO_NOT_FOUND: UInt32 = 655
ERROR_DEFAULTOFF_MACRO_NOT_FOUND: UInt32 = 656
ERROR_FILE_COULD_NOT_BE_OPENED: UInt32 = 657
ERROR_DEVICENAME_TOO_LONG: UInt32 = 658
ERROR_DEVICENAME_NOT_FOUND: UInt32 = 659
ERROR_NO_RESPONSES: UInt32 = 660
ERROR_NO_COMMAND_FOUND: UInt32 = 661
ERROR_WRONG_KEY_SPECIFIED: UInt32 = 662
ERROR_UNKNOWN_DEVICE_TYPE: UInt32 = 663
ERROR_ALLOCATING_MEMORY: UInt32 = 664
ERROR_PORT_NOT_CONFIGURED: UInt32 = 665
ERROR_DEVICE_NOT_READY: UInt32 = 666
ERROR_READING_INI_FILE: UInt32 = 667
ERROR_NO_CONNECTION: UInt32 = 668
ERROR_BAD_USAGE_IN_INI_FILE: UInt32 = 669
ERROR_READING_SECTIONNAME: UInt32 = 670
ERROR_READING_DEVICETYPE: UInt32 = 671
ERROR_READING_DEVICENAME: UInt32 = 672
ERROR_READING_USAGE: UInt32 = 673
ERROR_READING_MAXCONNECTBPS: UInt32 = 674
ERROR_READING_MAXCARRIERBPS: UInt32 = 675
ERROR_LINE_BUSY: UInt32 = 676
ERROR_VOICE_ANSWER: UInt32 = 677
ERROR_NO_ANSWER: UInt32 = 678
ERROR_NO_CARRIER: UInt32 = 679
ERROR_NO_DIALTONE: UInt32 = 680
ERROR_IN_COMMAND: UInt32 = 681
ERROR_WRITING_SECTIONNAME: UInt32 = 682
ERROR_WRITING_DEVICETYPE: UInt32 = 683
ERROR_WRITING_DEVICENAME: UInt32 = 684
ERROR_WRITING_MAXCONNECTBPS: UInt32 = 685
ERROR_WRITING_MAXCARRIERBPS: UInt32 = 686
ERROR_WRITING_USAGE: UInt32 = 687
ERROR_WRITING_DEFAULTOFF: UInt32 = 688
ERROR_READING_DEFAULTOFF: UInt32 = 689
ERROR_EMPTY_INI_FILE: UInt32 = 690
ERROR_AUTHENTICATION_FAILURE: UInt32 = 691
ERROR_PORT_OR_DEVICE: UInt32 = 692
ERROR_NOT_BINARY_MACRO: UInt32 = 693
ERROR_DCB_NOT_FOUND: UInt32 = 694
ERROR_STATE_MACHINES_NOT_STARTED: UInt32 = 695
ERROR_STATE_MACHINES_ALREADY_STARTED: UInt32 = 696
ERROR_PARTIAL_RESPONSE_LOOPING: UInt32 = 697
ERROR_UNKNOWN_RESPONSE_KEY: UInt32 = 698
ERROR_RECV_BUF_FULL: UInt32 = 699
ERROR_CMD_TOO_LONG: UInt32 = 700
ERROR_UNSUPPORTED_BPS: UInt32 = 701
ERROR_UNEXPECTED_RESPONSE: UInt32 = 702
ERROR_INTERACTIVE_MODE: UInt32 = 703
ERROR_BAD_CALLBACK_NUMBER: UInt32 = 704
ERROR_INVALID_AUTH_STATE: UInt32 = 705
ERROR_WRITING_INITBPS: UInt32 = 706
ERROR_X25_DIAGNOSTIC: UInt32 = 707
ERROR_ACCT_EXPIRED: UInt32 = 708
ERROR_CHANGING_PASSWORD: UInt32 = 709
ERROR_OVERRUN: UInt32 = 710
ERROR_RASMAN_CANNOT_INITIALIZE: UInt32 = 711
ERROR_BIPLEX_PORT_NOT_AVAILABLE: UInt32 = 712
ERROR_NO_ACTIVE_ISDN_LINES: UInt32 = 713
ERROR_NO_ISDN_CHANNELS_AVAILABLE: UInt32 = 714
ERROR_TOO_MANY_LINE_ERRORS: UInt32 = 715
ERROR_IP_CONFIGURATION: UInt32 = 716
ERROR_NO_IP_ADDRESSES: UInt32 = 717
ERROR_PPP_TIMEOUT: UInt32 = 718
ERROR_PPP_REMOTE_TERMINATED: UInt32 = 719
ERROR_PPP_NO_PROTOCOLS_CONFIGURED: UInt32 = 720
ERROR_PPP_NO_RESPONSE: UInt32 = 721
ERROR_PPP_INVALID_PACKET: UInt32 = 722
ERROR_PHONE_NUMBER_TOO_LONG: UInt32 = 723
ERROR_IPXCP_NO_DIALOUT_CONFIGURED: UInt32 = 724
ERROR_IPXCP_NO_DIALIN_CONFIGURED: UInt32 = 725
ERROR_IPXCP_DIALOUT_ALREADY_ACTIVE: UInt32 = 726
ERROR_ACCESSING_TCPCFGDLL: UInt32 = 727
ERROR_NO_IP_RAS_ADAPTER: UInt32 = 728
ERROR_SLIP_REQUIRES_IP: UInt32 = 729
ERROR_PROJECTION_NOT_COMPLETE: UInt32 = 730
ERROR_PROTOCOL_NOT_CONFIGURED: UInt32 = 731
ERROR_PPP_NOT_CONVERGING: UInt32 = 732
ERROR_PPP_CP_REJECTED: UInt32 = 733
ERROR_PPP_LCP_TERMINATED: UInt32 = 734
ERROR_PPP_REQUIRED_ADDRESS_REJECTED: UInt32 = 735
ERROR_PPP_NCP_TERMINATED: UInt32 = 736
ERROR_PPP_LOOPBACK_DETECTED: UInt32 = 737
ERROR_PPP_NO_ADDRESS_ASSIGNED: UInt32 = 738
ERROR_CANNOT_USE_LOGON_CREDENTIALS: UInt32 = 739
ERROR_TAPI_CONFIGURATION: UInt32 = 740
ERROR_NO_LOCAL_ENCRYPTION: UInt32 = 741
ERROR_NO_REMOTE_ENCRYPTION: UInt32 = 742
ERROR_REMOTE_REQUIRES_ENCRYPTION: UInt32 = 743
ERROR_IPXCP_NET_NUMBER_CONFLICT: UInt32 = 744
ERROR_INVALID_SMM: UInt32 = 745
ERROR_SMM_UNINITIALIZED: UInt32 = 746
ERROR_NO_MAC_FOR_PORT: UInt32 = 747
ERROR_SMM_TIMEOUT: UInt32 = 748
ERROR_BAD_PHONE_NUMBER: UInt32 = 749
ERROR_WRONG_MODULE: UInt32 = 750
ERROR_INVALID_CALLBACK_NUMBER: UInt32 = 751
ERROR_SCRIPT_SYNTAX: UInt32 = 752
ERROR_HANGUP_FAILED: UInt32 = 753
ERROR_BUNDLE_NOT_FOUND: UInt32 = 754
ERROR_CANNOT_DO_CUSTOMDIAL: UInt32 = 755
ERROR_DIAL_ALREADY_IN_PROGRESS: UInt32 = 756
ERROR_RASAUTO_CANNOT_INITIALIZE: UInt32 = 757
ERROR_CONNECTION_ALREADY_SHARED: UInt32 = 758
ERROR_SHARING_CHANGE_FAILED: UInt32 = 759
ERROR_SHARING_ROUTER_INSTALL: UInt32 = 760
ERROR_SHARE_CONNECTION_FAILED: UInt32 = 761
ERROR_SHARING_PRIVATE_INSTALL: UInt32 = 762
ERROR_CANNOT_SHARE_CONNECTION: UInt32 = 763
ERROR_NO_SMART_CARD_READER: UInt32 = 764
ERROR_SHARING_ADDRESS_EXISTS: UInt32 = 765
ERROR_NO_CERTIFICATE: UInt32 = 766
ERROR_SHARING_MULTIPLE_ADDRESSES: UInt32 = 767
ERROR_FAILED_TO_ENCRYPT: UInt32 = 768
ERROR_BAD_ADDRESS_SPECIFIED: UInt32 = 769
ERROR_CONNECTION_REJECT: UInt32 = 770
ERROR_CONGESTION: UInt32 = 771
ERROR_INCOMPATIBLE: UInt32 = 772
ERROR_NUMBERCHANGED: UInt32 = 773
ERROR_TEMPFAILURE: UInt32 = 774
ERROR_BLOCKED: UInt32 = 775
ERROR_DONOTDISTURB: UInt32 = 776
ERROR_OUTOFORDER: UInt32 = 777
ERROR_UNABLE_TO_AUTHENTICATE_SERVER: UInt32 = 778
ERROR_SMART_CARD_REQUIRED: UInt32 = 779
ERROR_INVALID_FUNCTION_FOR_ENTRY: UInt32 = 780
ERROR_CERT_FOR_ENCRYPTION_NOT_FOUND: UInt32 = 781
ERROR_SHARING_RRAS_CONFLICT: UInt32 = 782
ERROR_SHARING_NO_PRIVATE_LAN: UInt32 = 783
ERROR_NO_DIFF_USER_AT_LOGON: UInt32 = 784
ERROR_NO_REG_CERT_AT_LOGON: UInt32 = 785
ERROR_OAKLEY_NO_CERT: UInt32 = 786
ERROR_OAKLEY_AUTH_FAIL: UInt32 = 787
ERROR_OAKLEY_ATTRIB_FAIL: UInt32 = 788
ERROR_OAKLEY_GENERAL_PROCESSING: UInt32 = 789
ERROR_OAKLEY_NO_PEER_CERT: UInt32 = 790
ERROR_OAKLEY_NO_POLICY: UInt32 = 791
ERROR_OAKLEY_TIMED_OUT: UInt32 = 792
ERROR_OAKLEY_ERROR: UInt32 = 793
ERROR_UNKNOWN_FRAMED_PROTOCOL: UInt32 = 794
ERROR_WRONG_TUNNEL_TYPE: UInt32 = 795
ERROR_UNKNOWN_SERVICE_TYPE: UInt32 = 796
ERROR_CONNECTING_DEVICE_NOT_FOUND: UInt32 = 797
ERROR_NO_EAPTLS_CERTIFICATE: UInt32 = 798
ERROR_SHARING_HOST_ADDRESS_CONFLICT: UInt32 = 799
ERROR_AUTOMATIC_VPN_FAILED: UInt32 = 800
ERROR_VALIDATING_SERVER_CERT: UInt32 = 801
ERROR_READING_SCARD: UInt32 = 802
ERROR_INVALID_PEAP_COOKIE_CONFIG: UInt32 = 803
ERROR_INVALID_PEAP_COOKIE_USER: UInt32 = 804
ERROR_INVALID_MSCHAPV2_CONFIG: UInt32 = 805
ERROR_VPN_GRE_BLOCKED: UInt32 = 806
ERROR_VPN_DISCONNECT: UInt32 = 807
ERROR_VPN_REFUSED: UInt32 = 808
ERROR_VPN_TIMEOUT: UInt32 = 809
ERROR_VPN_BAD_CERT: UInt32 = 810
ERROR_VPN_BAD_PSK: UInt32 = 811
ERROR_SERVER_POLICY: UInt32 = 812
ERROR_BROADBAND_ACTIVE: UInt32 = 813
ERROR_BROADBAND_NO_NIC: UInt32 = 814
ERROR_BROADBAND_TIMEOUT: UInt32 = 815
ERROR_FEATURE_DEPRECATED: UInt32 = 816
ERROR_CANNOT_DELETE: UInt32 = 817
ERROR_RASQEC_RESOURCE_CREATION_FAILED: UInt32 = 818
ERROR_RASQEC_NAPAGENT_NOT_ENABLED: UInt32 = 819
ERROR_RASQEC_NAPAGENT_NOT_CONNECTED: UInt32 = 820
ERROR_RASQEC_CONN_DOESNOTEXIST: UInt32 = 821
ERROR_RASQEC_TIMEOUT: UInt32 = 822
ERROR_PEAP_CRYPTOBINDING_INVALID: UInt32 = 823
ERROR_PEAP_CRYPTOBINDING_NOTRECEIVED: UInt32 = 824
ERROR_INVALID_VPNSTRATEGY: UInt32 = 825
ERROR_EAPTLS_CACHE_CREDENTIALS_INVALID: UInt32 = 826
ERROR_IPSEC_SERVICE_STOPPED: UInt32 = 827
ERROR_IDLE_TIMEOUT: UInt32 = 828
ERROR_LINK_FAILURE: UInt32 = 829
ERROR_USER_LOGOFF: UInt32 = 830
ERROR_FAST_USER_SWITCH: UInt32 = 831
ERROR_HIBERNATION: UInt32 = 832
ERROR_SYSTEM_SUSPENDED: UInt32 = 833
ERROR_RASMAN_SERVICE_STOPPED: UInt32 = 834
ERROR_INVALID_SERVER_CERT: UInt32 = 835
ERROR_NOT_NAP_CAPABLE: UInt32 = 836
ERROR_INVALID_TUNNELID: UInt32 = 837
ERROR_UPDATECONNECTION_REQUEST_IN_PROCESS: UInt32 = 838
ERROR_PROTOCOL_ENGINE_DISABLED: UInt32 = 839
ERROR_INTERNAL_ADDRESS_FAILURE: UInt32 = 840
ERROR_FAILED_CP_REQUIRED: UInt32 = 841
ERROR_TS_UNACCEPTABLE: UInt32 = 842
ERROR_MOBIKE_DISABLED: UInt32 = 843
ERROR_CANNOT_INITIATE_MOBIKE_UPDATE: UInt32 = 844
ERROR_PEAP_SERVER_REJECTED_CLIENT_TLV: UInt32 = 845
ERROR_INVALID_PREFERENCES: UInt32 = 846
ERROR_EAPTLS_SCARD_CACHE_CREDENTIALS_INVALID: UInt32 = 847
ERROR_SSTP_COOKIE_SET_FAILURE: UInt32 = 848
ERROR_INVALID_PEAP_COOKIE_ATTRIBUTES: UInt32 = 849
ERROR_EAP_METHOD_NOT_INSTALLED: UInt32 = 850
ERROR_EAP_METHOD_DOES_NOT_SUPPORT_SSO: UInt32 = 851
ERROR_EAP_METHOD_OPERATION_NOT_SUPPORTED: UInt32 = 852
ERROR_EAP_USER_CERT_INVALID: UInt32 = 853
ERROR_EAP_USER_CERT_EXPIRED: UInt32 = 854
ERROR_EAP_USER_CERT_REVOKED: UInt32 = 855
ERROR_EAP_USER_CERT_OTHER_ERROR: UInt32 = 856
ERROR_EAP_SERVER_CERT_INVALID: UInt32 = 857
ERROR_EAP_SERVER_CERT_EXPIRED: UInt32 = 858
ERROR_EAP_SERVER_CERT_REVOKED: UInt32 = 859
ERROR_EAP_SERVER_CERT_OTHER_ERROR: UInt32 = 860
ERROR_EAP_USER_ROOT_CERT_NOT_FOUND: UInt32 = 861
ERROR_EAP_USER_ROOT_CERT_INVALID: UInt32 = 862
ERROR_EAP_USER_ROOT_CERT_EXPIRED: UInt32 = 863
ERROR_EAP_SERVER_ROOT_CERT_NOT_FOUND: UInt32 = 864
ERROR_EAP_SERVER_ROOT_CERT_INVALID: UInt32 = 865
ERROR_EAP_SERVER_ROOT_CERT_NAME_REQUIRED: UInt32 = 866
ERROR_PEAP_IDENTITY_MISMATCH: UInt32 = 867
ERROR_DNSNAME_NOT_RESOLVABLE: UInt32 = 868
ERROR_EAPTLS_PASSWD_INVALID: UInt32 = 869
ERROR_IKEV2_PSK_INTERFACE_ALREADY_EXISTS: UInt32 = 870
ERROR_INVALID_DESTINATION_IP: UInt32 = 871
ERROR_INVALID_INTERFACE_CONFIG: UInt32 = 872
ERROR_VPN_PLUGIN_GENERIC: UInt32 = 873
ERROR_SSO_CERT_MISSING: UInt32 = 874
ERROR_DEVICE_COMPLIANCE: UInt32 = 875
ERROR_PLUGIN_NOT_INSTALLED: UInt32 = 876
ERROR_ACTION_REQUIRED: UInt32 = 877
RASBASEEND: UInt32 = 877
@winfunctype('RASAPI32.dll')
def RasDialA(param0: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASDIALEXTENSIONS), param1: win32more.Windows.Win32.Foundation.PSTR, param2: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASDIALPARAMSA), param3: UInt32, param4: VoidPtr, param5: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.HRASCONN)) -> UInt32: ...
@winfunctype('RASAPI32.dll')
def RasDialW(param0: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASDIALEXTENSIONS), param1: win32more.Windows.Win32.Foundation.PWSTR, param2: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASDIALPARAMSW), param3: UInt32, param4: VoidPtr, param5: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.HRASCONN)) -> UInt32: ...
RasDial = UnicodeAlias('RasDialW')
@winfunctype('RASAPI32.dll')
def RasEnumConnectionsA(param0: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASCONNA), param1: POINTER(UInt32), param2: POINTER(UInt32)) -> UInt32: ...
@winfunctype('RASAPI32.dll')
def RasEnumConnectionsW(param0: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASCONNW), param1: POINTER(UInt32), param2: POINTER(UInt32)) -> UInt32: ...
RasEnumConnections = UnicodeAlias('RasEnumConnectionsW')
@winfunctype('RASAPI32.dll')
def RasEnumEntriesA(param0: win32more.Windows.Win32.Foundation.PSTR, param1: win32more.Windows.Win32.Foundation.PSTR, param2: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASENTRYNAMEA), param3: POINTER(UInt32), param4: POINTER(UInt32)) -> UInt32: ...
@winfunctype('RASAPI32.dll')
def RasEnumEntriesW(param0: win32more.Windows.Win32.Foundation.PWSTR, param1: win32more.Windows.Win32.Foundation.PWSTR, param2: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASENTRYNAMEW), param3: POINTER(UInt32), param4: POINTER(UInt32)) -> UInt32: ...
RasEnumEntries = UnicodeAlias('RasEnumEntriesW')
@winfunctype('RASAPI32.dll')
def RasGetConnectStatusA(param0: win32more.Windows.Win32.NetworkManagement.Rras.HRASCONN, param1: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASCONNSTATUSA)) -> UInt32: ...
@winfunctype('RASAPI32.dll')
def RasGetConnectStatusW(param0: win32more.Windows.Win32.NetworkManagement.Rras.HRASCONN, param1: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASCONNSTATUSW)) -> UInt32: ...
RasGetConnectStatus = UnicodeAlias('RasGetConnectStatusW')
@winfunctype('RASAPI32.dll')
def RasGetErrorStringA(ResourceId: UInt32, lpszString: win32more.Windows.Win32.Foundation.PSTR, InBufSize: UInt32) -> UInt32: ...
@winfunctype('RASAPI32.dll')
def RasGetErrorStringW(ResourceId: UInt32, lpszString: win32more.Windows.Win32.Foundation.PWSTR, InBufSize: UInt32) -> UInt32: ...
RasGetErrorString = UnicodeAlias('RasGetErrorStringW')
@winfunctype('RASAPI32.dll')
def RasHangUpA(param0: win32more.Windows.Win32.NetworkManagement.Rras.HRASCONN) -> UInt32: ...
@winfunctype('RASAPI32.dll')
def RasHangUpW(param0: win32more.Windows.Win32.NetworkManagement.Rras.HRASCONN) -> UInt32: ...
RasHangUp = UnicodeAlias('RasHangUpW')
@winfunctype('RASAPI32.dll')
def RasGetProjectionInfoA(param0: win32more.Windows.Win32.NetworkManagement.Rras.HRASCONN, param1: win32more.Windows.Win32.NetworkManagement.Rras.RASPROJECTION, param2: VoidPtr, param3: POINTER(UInt32)) -> UInt32: ...
@winfunctype('RASAPI32.dll')
def RasGetProjectionInfoW(param0: win32more.Windows.Win32.NetworkManagement.Rras.HRASCONN, param1: win32more.Windows.Win32.NetworkManagement.Rras.RASPROJECTION, param2: VoidPtr, param3: POINTER(UInt32)) -> UInt32: ...
RasGetProjectionInfo = UnicodeAlias('RasGetProjectionInfoW')
@winfunctype('RASAPI32.dll')
def RasCreatePhonebookEntryA(param0: win32more.Windows.Win32.Foundation.HWND, param1: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('RASAPI32.dll')
def RasCreatePhonebookEntryW(param0: win32more.Windows.Win32.Foundation.HWND, param1: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
RasCreatePhonebookEntry = UnicodeAlias('RasCreatePhonebookEntryW')
@winfunctype('RASAPI32.dll')
def RasEditPhonebookEntryA(param0: win32more.Windows.Win32.Foundation.HWND, param1: win32more.Windows.Win32.Foundation.PSTR, param2: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('RASAPI32.dll')
def RasEditPhonebookEntryW(param0: win32more.Windows.Win32.Foundation.HWND, param1: win32more.Windows.Win32.Foundation.PWSTR, param2: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
RasEditPhonebookEntry = UnicodeAlias('RasEditPhonebookEntryW')
@winfunctype('RASAPI32.dll')
def RasSetEntryDialParamsA(param0: win32more.Windows.Win32.Foundation.PSTR, param1: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASDIALPARAMSA), param2: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('RASAPI32.dll')
def RasSetEntryDialParamsW(param0: win32more.Windows.Win32.Foundation.PWSTR, param1: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASDIALPARAMSW), param2: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
RasSetEntryDialParams = UnicodeAlias('RasSetEntryDialParamsW')
@winfunctype('RASAPI32.dll')
def RasGetEntryDialParamsA(param0: win32more.Windows.Win32.Foundation.PSTR, param1: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASDIALPARAMSA), param2: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> UInt32: ...
@winfunctype('RASAPI32.dll')
def RasGetEntryDialParamsW(param0: win32more.Windows.Win32.Foundation.PWSTR, param1: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASDIALPARAMSW), param2: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> UInt32: ...
RasGetEntryDialParams = UnicodeAlias('RasGetEntryDialParamsW')
@winfunctype('RASAPI32.dll')
def RasEnumDevicesA(param0: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASDEVINFOA), param1: POINTER(UInt32), param2: POINTER(UInt32)) -> UInt32: ...
@winfunctype('RASAPI32.dll')
def RasEnumDevicesW(param0: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASDEVINFOW), param1: POINTER(UInt32), param2: POINTER(UInt32)) -> UInt32: ...
RasEnumDevices = UnicodeAlias('RasEnumDevicesW')
@winfunctype('RASAPI32.dll')
def RasGetCountryInfoA(param0: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASCTRYINFO), param1: POINTER(UInt32)) -> UInt32: ...
@winfunctype('RASAPI32.dll')
def RasGetCountryInfoW(param0: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASCTRYINFO), param1: POINTER(UInt32)) -> UInt32: ...
RasGetCountryInfo = UnicodeAlias('RasGetCountryInfoW')
@winfunctype('RASAPI32.dll')
def RasGetEntryPropertiesA(param0: win32more.Windows.Win32.Foundation.PSTR, param1: win32more.Windows.Win32.Foundation.PSTR, param2: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASENTRYA), param3: POINTER(UInt32), param4: POINTER(Byte), param5: POINTER(UInt32)) -> UInt32: ...
@winfunctype('RASAPI32.dll')
def RasGetEntryPropertiesW(param0: win32more.Windows.Win32.Foundation.PWSTR, param1: win32more.Windows.Win32.Foundation.PWSTR, param2: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASENTRYW), param3: POINTER(UInt32), param4: POINTER(Byte), param5: POINTER(UInt32)) -> UInt32: ...
RasGetEntryProperties = UnicodeAlias('RasGetEntryPropertiesW')
@winfunctype('RASAPI32.dll')
def RasSetEntryPropertiesA(param0: win32more.Windows.Win32.Foundation.PSTR, param1: win32more.Windows.Win32.Foundation.PSTR, param2: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASENTRYA), param3: UInt32, param4: POINTER(Byte), param5: UInt32) -> UInt32: ...
@winfunctype('RASAPI32.dll')
def RasSetEntryPropertiesW(param0: win32more.Windows.Win32.Foundation.PWSTR, param1: win32more.Windows.Win32.Foundation.PWSTR, param2: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASENTRYW), param3: UInt32, param4: POINTER(Byte), param5: UInt32) -> UInt32: ...
RasSetEntryProperties = UnicodeAlias('RasSetEntryPropertiesW')
@winfunctype('RASAPI32.dll')
def RasRenameEntryA(param0: win32more.Windows.Win32.Foundation.PSTR, param1: win32more.Windows.Win32.Foundation.PSTR, param2: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('RASAPI32.dll')
def RasRenameEntryW(param0: win32more.Windows.Win32.Foundation.PWSTR, param1: win32more.Windows.Win32.Foundation.PWSTR, param2: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
RasRenameEntry = UnicodeAlias('RasRenameEntryW')
@winfunctype('RASAPI32.dll')
def RasDeleteEntryA(param0: win32more.Windows.Win32.Foundation.PSTR, param1: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('RASAPI32.dll')
def RasDeleteEntryW(param0: win32more.Windows.Win32.Foundation.PWSTR, param1: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
RasDeleteEntry = UnicodeAlias('RasDeleteEntryW')
@winfunctype('RASAPI32.dll')
def RasValidateEntryNameA(param0: win32more.Windows.Win32.Foundation.PSTR, param1: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('RASAPI32.dll')
def RasValidateEntryNameW(param0: win32more.Windows.Win32.Foundation.PWSTR, param1: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
RasValidateEntryName = UnicodeAlias('RasValidateEntryNameW')
@winfunctype('RASAPI32.dll')
def RasConnectionNotificationA(param0: win32more.Windows.Win32.NetworkManagement.Rras.HRASCONN, param1: win32more.Windows.Win32.Foundation.HANDLE, param2: UInt32) -> UInt32: ...
@winfunctype('RASAPI32.dll')
def RasConnectionNotificationW(param0: win32more.Windows.Win32.NetworkManagement.Rras.HRASCONN, param1: win32more.Windows.Win32.Foundation.HANDLE, param2: UInt32) -> UInt32: ...
RasConnectionNotification = UnicodeAlias('RasConnectionNotificationW')
@winfunctype('RASAPI32.dll')
def RasGetSubEntryHandleA(param0: win32more.Windows.Win32.NetworkManagement.Rras.HRASCONN, param1: UInt32, param2: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.HRASCONN)) -> UInt32: ...
@winfunctype('RASAPI32.dll')
def RasGetSubEntryHandleW(param0: win32more.Windows.Win32.NetworkManagement.Rras.HRASCONN, param1: UInt32, param2: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.HRASCONN)) -> UInt32: ...
RasGetSubEntryHandle = UnicodeAlias('RasGetSubEntryHandleW')
@winfunctype('RASAPI32.dll')
def RasGetCredentialsA(param0: win32more.Windows.Win32.Foundation.PSTR, param1: win32more.Windows.Win32.Foundation.PSTR, param2: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASCREDENTIALSA)) -> UInt32: ...
@winfunctype('RASAPI32.dll')
def RasGetCredentialsW(param0: win32more.Windows.Win32.Foundation.PWSTR, param1: win32more.Windows.Win32.Foundation.PWSTR, param2: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASCREDENTIALSW)) -> UInt32: ...
RasGetCredentials = UnicodeAlias('RasGetCredentialsW')
@winfunctype('RASAPI32.dll')
def RasSetCredentialsA(param0: win32more.Windows.Win32.Foundation.PSTR, param1: win32more.Windows.Win32.Foundation.PSTR, param2: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASCREDENTIALSA), param3: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('RASAPI32.dll')
def RasSetCredentialsW(param0: win32more.Windows.Win32.Foundation.PWSTR, param1: win32more.Windows.Win32.Foundation.PWSTR, param2: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASCREDENTIALSW), param3: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
RasSetCredentials = UnicodeAlias('RasSetCredentialsW')
@winfunctype('RASAPI32.dll')
def RasGetSubEntryPropertiesA(param0: win32more.Windows.Win32.Foundation.PSTR, param1: win32more.Windows.Win32.Foundation.PSTR, param2: UInt32, param3: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASSUBENTRYA), param4: POINTER(UInt32), param5: POINTER(Byte), param6: POINTER(UInt32)) -> UInt32: ...
@winfunctype('RASAPI32.dll')
def RasGetSubEntryPropertiesW(param0: win32more.Windows.Win32.Foundation.PWSTR, param1: win32more.Windows.Win32.Foundation.PWSTR, param2: UInt32, param3: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASSUBENTRYW), param4: POINTER(UInt32), param5: POINTER(Byte), param6: POINTER(UInt32)) -> UInt32: ...
RasGetSubEntryProperties = UnicodeAlias('RasGetSubEntryPropertiesW')
@winfunctype('RASAPI32.dll')
def RasSetSubEntryPropertiesA(param0: win32more.Windows.Win32.Foundation.PSTR, param1: win32more.Windows.Win32.Foundation.PSTR, param2: UInt32, param3: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASSUBENTRYA), param4: UInt32, param5: POINTER(Byte), param6: UInt32) -> UInt32: ...
@winfunctype('RASAPI32.dll')
def RasSetSubEntryPropertiesW(param0: win32more.Windows.Win32.Foundation.PWSTR, param1: win32more.Windows.Win32.Foundation.PWSTR, param2: UInt32, param3: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASSUBENTRYW), param4: UInt32, param5: POINTER(Byte), param6: UInt32) -> UInt32: ...
RasSetSubEntryProperties = UnicodeAlias('RasSetSubEntryPropertiesW')
@winfunctype('RASAPI32.dll')
def RasGetAutodialAddressA(param0: win32more.Windows.Win32.Foundation.PSTR, param1: POINTER(UInt32), param2: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASAUTODIALENTRYA), param3: POINTER(UInt32), param4: POINTER(UInt32)) -> UInt32: ...
@winfunctype('RASAPI32.dll')
def RasGetAutodialAddressW(param0: win32more.Windows.Win32.Foundation.PWSTR, param1: POINTER(UInt32), param2: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASAUTODIALENTRYW), param3: POINTER(UInt32), param4: POINTER(UInt32)) -> UInt32: ...
RasGetAutodialAddress = UnicodeAlias('RasGetAutodialAddressW')
@winfunctype('RASAPI32.dll')
def RasSetAutodialAddressA(param0: win32more.Windows.Win32.Foundation.PSTR, param1: UInt32, param2: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASAUTODIALENTRYA), param3: UInt32, param4: UInt32) -> UInt32: ...
@winfunctype('RASAPI32.dll')
def RasSetAutodialAddressW(param0: win32more.Windows.Win32.Foundation.PWSTR, param1: UInt32, param2: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASAUTODIALENTRYW), param3: UInt32, param4: UInt32) -> UInt32: ...
RasSetAutodialAddress = UnicodeAlias('RasSetAutodialAddressW')
@winfunctype('RASAPI32.dll')
def RasEnumAutodialAddressesA(lppRasAutodialAddresses: POINTER(win32more.Windows.Win32.Foundation.PSTR), lpdwcbRasAutodialAddresses: POINTER(UInt32), lpdwcRasAutodialAddresses: POINTER(UInt32)) -> UInt32: ...
@winfunctype('RASAPI32.dll')
def RasEnumAutodialAddressesW(lppRasAutodialAddresses: POINTER(win32more.Windows.Win32.Foundation.PWSTR), lpdwcbRasAutodialAddresses: POINTER(UInt32), lpdwcRasAutodialAddresses: POINTER(UInt32)) -> UInt32: ...
RasEnumAutodialAddresses = UnicodeAlias('RasEnumAutodialAddressesW')
@winfunctype('RASAPI32.dll')
def RasGetAutodialEnableA(param0: UInt32, param1: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> UInt32: ...
@winfunctype('RASAPI32.dll')
def RasGetAutodialEnableW(param0: UInt32, param1: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> UInt32: ...
RasGetAutodialEnable = UnicodeAlias('RasGetAutodialEnableW')
@winfunctype('RASAPI32.dll')
def RasSetAutodialEnableA(param0: UInt32, param1: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('RASAPI32.dll')
def RasSetAutodialEnableW(param0: UInt32, param1: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
RasSetAutodialEnable = UnicodeAlias('RasSetAutodialEnableW')
@winfunctype('RASAPI32.dll')
def RasGetAutodialParamA(param0: UInt32, param1: VoidPtr, param2: POINTER(UInt32)) -> UInt32: ...
@winfunctype('RASAPI32.dll')
def RasGetAutodialParamW(param0: UInt32, param1: VoidPtr, param2: POINTER(UInt32)) -> UInt32: ...
RasGetAutodialParam = UnicodeAlias('RasGetAutodialParamW')
@winfunctype('RASAPI32.dll')
def RasSetAutodialParamA(param0: UInt32, param1: VoidPtr, param2: UInt32) -> UInt32: ...
@winfunctype('RASAPI32.dll')
def RasSetAutodialParamW(param0: UInt32, param1: VoidPtr, param2: UInt32) -> UInt32: ...
RasSetAutodialParam = UnicodeAlias('RasSetAutodialParamW')
@winfunctype('RASAPI32.dll')
def RasGetPCscf(lpszPCscf: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('RASAPI32.dll')
def RasInvokeEapUI(param0: win32more.Windows.Win32.NetworkManagement.Rras.HRASCONN, param1: UInt32, param2: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASDIALEXTENSIONS), param3: win32more.Windows.Win32.Foundation.HWND) -> UInt32: ...
@winfunctype('RASAPI32.dll')
def RasGetLinkStatistics(hRasConn: win32more.Windows.Win32.NetworkManagement.Rras.HRASCONN, dwSubEntry: UInt32, lpStatistics: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RAS_STATS)) -> UInt32: ...
@winfunctype('RASAPI32.dll')
def RasGetConnectionStatistics(hRasConn: win32more.Windows.Win32.NetworkManagement.Rras.HRASCONN, lpStatistics: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RAS_STATS)) -> UInt32: ...
@winfunctype('RASAPI32.dll')
def RasClearLinkStatistics(hRasConn: win32more.Windows.Win32.NetworkManagement.Rras.HRASCONN, dwSubEntry: UInt32) -> UInt32: ...
@winfunctype('RASAPI32.dll')
def RasClearConnectionStatistics(hRasConn: win32more.Windows.Win32.NetworkManagement.Rras.HRASCONN) -> UInt32: ...
@winfunctype('RASAPI32.dll')
def RasGetEapUserDataA(hToken: win32more.Windows.Win32.Foundation.HANDLE, pszPhonebook: win32more.Windows.Win32.Foundation.PSTR, pszEntry: win32more.Windows.Win32.Foundation.PSTR, pbEapData: POINTER(Byte), pdwSizeofEapData: POINTER(UInt32)) -> UInt32: ...
@winfunctype('RASAPI32.dll')
def RasGetEapUserDataW(hToken: win32more.Windows.Win32.Foundation.HANDLE, pszPhonebook: win32more.Windows.Win32.Foundation.PWSTR, pszEntry: win32more.Windows.Win32.Foundation.PWSTR, pbEapData: POINTER(Byte), pdwSizeofEapData: POINTER(UInt32)) -> UInt32: ...
RasGetEapUserData = UnicodeAlias('RasGetEapUserDataW')
@winfunctype('RASAPI32.dll')
def RasSetEapUserDataA(hToken: win32more.Windows.Win32.Foundation.HANDLE, pszPhonebook: win32more.Windows.Win32.Foundation.PSTR, pszEntry: win32more.Windows.Win32.Foundation.PSTR, pbEapData: POINTER(Byte), dwSizeofEapData: UInt32) -> UInt32: ...
@winfunctype('RASAPI32.dll')
def RasSetEapUserDataW(hToken: win32more.Windows.Win32.Foundation.HANDLE, pszPhonebook: win32more.Windows.Win32.Foundation.PWSTR, pszEntry: win32more.Windows.Win32.Foundation.PWSTR, pbEapData: POINTER(Byte), dwSizeofEapData: UInt32) -> UInt32: ...
RasSetEapUserData = UnicodeAlias('RasSetEapUserDataW')
@winfunctype('RASAPI32.dll')
def RasGetCustomAuthDataA(pszPhonebook: win32more.Windows.Win32.Foundation.PSTR, pszEntry: win32more.Windows.Win32.Foundation.PSTR, pbCustomAuthData: POINTER(Byte), pdwSizeofCustomAuthData: POINTER(UInt32)) -> UInt32: ...
@winfunctype('RASAPI32.dll')
def RasGetCustomAuthDataW(pszPhonebook: win32more.Windows.Win32.Foundation.PWSTR, pszEntry: win32more.Windows.Win32.Foundation.PWSTR, pbCustomAuthData: POINTER(Byte), pdwSizeofCustomAuthData: POINTER(UInt32)) -> UInt32: ...
RasGetCustomAuthData = UnicodeAlias('RasGetCustomAuthDataW')
@winfunctype('RASAPI32.dll')
def RasSetCustomAuthDataA(pszPhonebook: win32more.Windows.Win32.Foundation.PSTR, pszEntry: win32more.Windows.Win32.Foundation.PSTR, pbCustomAuthData: POINTER(Byte), dwSizeofCustomAuthData: UInt32) -> UInt32: ...
@winfunctype('RASAPI32.dll')
def RasSetCustomAuthDataW(pszPhonebook: win32more.Windows.Win32.Foundation.PWSTR, pszEntry: win32more.Windows.Win32.Foundation.PWSTR, pbCustomAuthData: POINTER(Byte), dwSizeofCustomAuthData: UInt32) -> UInt32: ...
RasSetCustomAuthData = UnicodeAlias('RasSetCustomAuthDataW')
@winfunctype('RASAPI32.dll')
def RasGetEapUserIdentityW(pszPhonebook: win32more.Windows.Win32.Foundation.PWSTR, pszEntry: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, hwnd: win32more.Windows.Win32.Foundation.HWND, ppRasEapUserIdentity: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASEAPUSERIDENTITYW))) -> UInt32: ...
RasGetEapUserIdentity = UnicodeAlias('RasGetEapUserIdentityW')
@winfunctype('RASAPI32.dll')
def RasGetEapUserIdentityA(pszPhonebook: win32more.Windows.Win32.Foundation.PSTR, pszEntry: win32more.Windows.Win32.Foundation.PSTR, dwFlags: UInt32, hwnd: win32more.Windows.Win32.Foundation.HWND, ppRasEapUserIdentity: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASEAPUSERIDENTITYA))) -> UInt32: ...
@winfunctype('RASAPI32.dll')
def RasFreeEapUserIdentityW(pRasEapUserIdentity: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASEAPUSERIDENTITYW)) -> Void: ...
RasFreeEapUserIdentity = UnicodeAlias('RasFreeEapUserIdentityW')
@winfunctype('RASAPI32.dll')
def RasFreeEapUserIdentityA(pRasEapUserIdentity: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASEAPUSERIDENTITYA)) -> Void: ...
@winfunctype('RASAPI32.dll')
def RasDeleteSubEntryA(pszPhonebook: win32more.Windows.Win32.Foundation.PSTR, pszEntry: win32more.Windows.Win32.Foundation.PSTR, dwSubentryId: UInt32) -> UInt32: ...
@winfunctype('RASAPI32.dll')
def RasDeleteSubEntryW(pszPhonebook: win32more.Windows.Win32.Foundation.PWSTR, pszEntry: win32more.Windows.Win32.Foundation.PWSTR, dwSubEntryId: UInt32) -> UInt32: ...
RasDeleteSubEntry = UnicodeAlias('RasDeleteSubEntryW')
@winfunctype('RASAPI32.dll')
def RasUpdateConnection(hrasconn: win32more.Windows.Win32.NetworkManagement.Rras.HRASCONN, lprasupdateconn: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASUPDATECONN)) -> UInt32: ...
@winfunctype('RASAPI32.dll')
def RasGetProjectionInfoEx(hrasconn: win32more.Windows.Win32.NetworkManagement.Rras.HRASCONN, pRasProjection: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RAS_PROJECTION_INFO), lpdwSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('RASDLG.dll')
def RasPhonebookDlgA(lpszPhonebook: win32more.Windows.Win32.Foundation.PSTR, lpszEntry: win32more.Windows.Win32.Foundation.PSTR, lpInfo: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASPBDLGA)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('RASDLG.dll')
def RasPhonebookDlgW(lpszPhonebook: win32more.Windows.Win32.Foundation.PWSTR, lpszEntry: win32more.Windows.Win32.Foundation.PWSTR, lpInfo: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASPBDLGW)) -> win32more.Windows.Win32.Foundation.BOOL: ...
RasPhonebookDlg = UnicodeAlias('RasPhonebookDlgW')
@winfunctype('RASDLG.dll')
def RasEntryDlgA(lpszPhonebook: win32more.Windows.Win32.Foundation.PSTR, lpszEntry: win32more.Windows.Win32.Foundation.PSTR, lpInfo: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASENTRYDLGA)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('RASDLG.dll')
def RasEntryDlgW(lpszPhonebook: win32more.Windows.Win32.Foundation.PWSTR, lpszEntry: win32more.Windows.Win32.Foundation.PWSTR, lpInfo: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASENTRYDLGW)) -> win32more.Windows.Win32.Foundation.BOOL: ...
RasEntryDlg = UnicodeAlias('RasEntryDlgW')
@winfunctype('RASDLG.dll')
def RasDialDlgA(lpszPhonebook: win32more.Windows.Win32.Foundation.PSTR, lpszEntry: win32more.Windows.Win32.Foundation.PSTR, lpszPhoneNumber: win32more.Windows.Win32.Foundation.PSTR, lpInfo: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASDIALDLG)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('RASDLG.dll')
def RasDialDlgW(lpszPhonebook: win32more.Windows.Win32.Foundation.PWSTR, lpszEntry: win32more.Windows.Win32.Foundation.PWSTR, lpszPhoneNumber: win32more.Windows.Win32.Foundation.PWSTR, lpInfo: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASDIALDLG)) -> win32more.Windows.Win32.Foundation.BOOL: ...
RasDialDlg = UnicodeAlias('RasDialDlgW')
@winfunctype('MPRAPI.dll')
def MprAdminConnectionEnumEx(hRasServer: IntPtr, pObjectHeader: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.MPRAPI_OBJECT_HEADER), dwPreferedMaxLen: UInt32, lpdwEntriesRead: POINTER(UInt32), lpdwTotalEntries: POINTER(UInt32), ppRasConn: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RAS_CONNECTION_EX)), lpdwResumeHandle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminConnectionGetInfoEx(hRasServer: IntPtr, hRasConnection: win32more.Windows.Win32.Foundation.HANDLE, pRasConnection: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RAS_CONNECTION_EX)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminServerGetInfoEx(hMprServer: IntPtr, pServerInfo: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.MPR_SERVER_EX1)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminServerSetInfoEx(hMprServer: IntPtr, pServerInfo: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.MPR_SERVER_SET_CONFIG_EX1)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprConfigServerGetInfoEx(hMprConfig: win32more.Windows.Win32.Foundation.HANDLE, pServerInfo: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.MPR_SERVER_EX1)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprConfigServerSetInfoEx(hMprConfig: win32more.Windows.Win32.Foundation.HANDLE, pSetServerConfig: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.MPR_SERVER_SET_CONFIG_EX1)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminUpdateConnection(hRasServer: IntPtr, hRasConnection: win32more.Windows.Win32.Foundation.HANDLE, pRasUpdateConnection: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RAS_UPDATE_CONNECTION)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminIsServiceInitialized(lpwsServerName: win32more.Windows.Win32.Foundation.PWSTR, fIsServiceInitialized: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminInterfaceSetCustomInfoEx(hMprServer: IntPtr, hInterface: win32more.Windows.Win32.Foundation.HANDLE, pCustomInfo: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.MPR_IF_CUSTOMINFOEX2)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminInterfaceGetCustomInfoEx(hMprServer: IntPtr, hInterface: win32more.Windows.Win32.Foundation.HANDLE, pCustomInfo: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.MPR_IF_CUSTOMINFOEX2)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprConfigInterfaceGetCustomInfoEx(hMprConfig: win32more.Windows.Win32.Foundation.HANDLE, hRouterInterface: win32more.Windows.Win32.Foundation.HANDLE, pCustomInfo: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.MPR_IF_CUSTOMINFOEX2)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprConfigInterfaceSetCustomInfoEx(hMprConfig: win32more.Windows.Win32.Foundation.HANDLE, hRouterInterface: win32more.Windows.Win32.Foundation.HANDLE, pCustomInfo: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.MPR_IF_CUSTOMINFOEX2)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminConnectionEnum(hRasServer: IntPtr, dwLevel: UInt32, lplpbBuffer: POINTER(POINTER(Byte)), dwPrefMaxLen: UInt32, lpdwEntriesRead: POINTER(UInt32), lpdwTotalEntries: POINTER(UInt32), lpdwResumeHandle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminPortEnum(hRasServer: IntPtr, dwLevel: UInt32, hRasConnection: win32more.Windows.Win32.Foundation.HANDLE, lplpbBuffer: POINTER(POINTER(Byte)), dwPrefMaxLen: UInt32, lpdwEntriesRead: POINTER(UInt32), lpdwTotalEntries: POINTER(UInt32), lpdwResumeHandle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminConnectionGetInfo(hRasServer: IntPtr, dwLevel: UInt32, hRasConnection: win32more.Windows.Win32.Foundation.HANDLE, lplpbBuffer: POINTER(POINTER(Byte))) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminPortGetInfo(hRasServer: IntPtr, dwLevel: UInt32, hPort: win32more.Windows.Win32.Foundation.HANDLE, lplpbBuffer: POINTER(POINTER(Byte))) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminConnectionClearStats(hRasServer: IntPtr, hRasConnection: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminPortClearStats(hRasServer: IntPtr, hPort: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminPortReset(hRasServer: IntPtr, hPort: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminPortDisconnect(hRasServer: IntPtr, hPort: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminConnectionRemoveQuarantine(hRasServer: win32more.Windows.Win32.Foundation.HANDLE, hRasConnection: win32more.Windows.Win32.Foundation.HANDLE, fIsIpAddress: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminUserGetInfo(lpszServer: win32more.Windows.Win32.Foundation.PWSTR, lpszUser: win32more.Windows.Win32.Foundation.PWSTR, dwLevel: UInt32, lpbBuffer: POINTER(Byte)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminUserSetInfo(lpszServer: win32more.Windows.Win32.Foundation.PWSTR, lpszUser: win32more.Windows.Win32.Foundation.PWSTR, dwLevel: UInt32, lpbBuffer: POINTER(Byte)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminSendUserMessage(hMprServer: IntPtr, hConnection: win32more.Windows.Win32.Foundation.HANDLE, lpwszMessage: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminGetPDCServer(lpszDomain: win32more.Windows.Win32.Foundation.PWSTR, lpszServer: win32more.Windows.Win32.Foundation.PWSTR, lpszPDCServer: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminIsServiceRunning(lpwsServerName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('MPRAPI.dll')
def MprAdminServerConnect(lpwsServerName: win32more.Windows.Win32.Foundation.PWSTR, phMprServer: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminServerDisconnect(hMprServer: IntPtr) -> Void: ...
@winfunctype('MPRAPI.dll')
def MprAdminServerGetCredentials(hMprServer: IntPtr, dwLevel: UInt32, lplpbBuffer: POINTER(POINTER(Byte))) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminServerSetCredentials(hMprServer: IntPtr, dwLevel: UInt32, lpbBuffer: POINTER(Byte)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminBufferFree(pBuffer: VoidPtr) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminGetErrorString(dwError: UInt32, lplpwsErrorString: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminServerGetInfo(hMprServer: IntPtr, dwLevel: UInt32, lplpbBuffer: POINTER(POINTER(Byte))) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminServerSetInfo(hMprServer: IntPtr, dwLevel: UInt32, lpbBuffer: POINTER(Byte)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminEstablishDomainRasServer(pszDomain: win32more.Windows.Win32.Foundation.PWSTR, pszMachine: win32more.Windows.Win32.Foundation.PWSTR, bEnable: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminIsDomainRasServer(pszDomain: win32more.Windows.Win32.Foundation.PWSTR, pszMachine: win32more.Windows.Win32.Foundation.PWSTR, pbIsRasServer: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminTransportCreate(hMprServer: IntPtr, dwTransportId: UInt32, lpwsTransportName: win32more.Windows.Win32.Foundation.PWSTR, pGlobalInfo: POINTER(Byte), dwGlobalInfoSize: UInt32, pClientInterfaceInfo: POINTER(Byte), dwClientInterfaceInfoSize: UInt32, lpwsDLLPath: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminTransportSetInfo(hMprServer: IntPtr, dwTransportId: UInt32, pGlobalInfo: POINTER(Byte), dwGlobalInfoSize: UInt32, pClientInterfaceInfo: POINTER(Byte), dwClientInterfaceInfoSize: UInt32) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminTransportGetInfo(hMprServer: IntPtr, dwTransportId: UInt32, ppGlobalInfo: POINTER(POINTER(Byte)), lpdwGlobalInfoSize: POINTER(UInt32), ppClientInterfaceInfo: POINTER(POINTER(Byte)), lpdwClientInterfaceInfoSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminDeviceEnum(hMprServer: IntPtr, dwLevel: UInt32, lplpbBuffer: POINTER(POINTER(Byte)), lpdwTotalEntries: POINTER(UInt32)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminInterfaceGetHandle(hMprServer: IntPtr, lpwsInterfaceName: win32more.Windows.Win32.Foundation.PWSTR, phInterface: POINTER(win32more.Windows.Win32.Foundation.HANDLE), fIncludeClientInterfaces: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminInterfaceCreate(hMprServer: IntPtr, dwLevel: UInt32, lpbBuffer: POINTER(Byte), phInterface: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminInterfaceGetInfo(hMprServer: IntPtr, hInterface: win32more.Windows.Win32.Foundation.HANDLE, dwLevel: UInt32, lplpbBuffer: POINTER(POINTER(Byte))) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminInterfaceSetInfo(hMprServer: IntPtr, hInterface: win32more.Windows.Win32.Foundation.HANDLE, dwLevel: UInt32, lpbBuffer: POINTER(Byte)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminInterfaceDelete(hMprServer: IntPtr, hInterface: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminInterfaceDeviceGetInfo(hMprServer: IntPtr, hInterface: win32more.Windows.Win32.Foundation.HANDLE, dwIndex: UInt32, dwLevel: UInt32, lplpBuffer: POINTER(POINTER(Byte))) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminInterfaceDeviceSetInfo(hMprServer: IntPtr, hInterface: win32more.Windows.Win32.Foundation.HANDLE, dwIndex: UInt32, dwLevel: UInt32, lpbBuffer: POINTER(Byte)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminInterfaceTransportRemove(hMprServer: IntPtr, hInterface: win32more.Windows.Win32.Foundation.HANDLE, dwTransportId: UInt32) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminInterfaceTransportAdd(hMprServer: IntPtr, hInterface: win32more.Windows.Win32.Foundation.HANDLE, dwTransportId: UInt32, pInterfaceInfo: POINTER(Byte), dwInterfaceInfoSize: UInt32) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminInterfaceTransportGetInfo(hMprServer: IntPtr, hInterface: win32more.Windows.Win32.Foundation.HANDLE, dwTransportId: UInt32, ppInterfaceInfo: POINTER(POINTER(Byte)), lpdwInterfaceInfoSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminInterfaceTransportSetInfo(hMprServer: IntPtr, hInterface: win32more.Windows.Win32.Foundation.HANDLE, dwTransportId: UInt32, pInterfaceInfo: POINTER(Byte), dwInterfaceInfoSize: UInt32) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminInterfaceEnum(hMprServer: IntPtr, dwLevel: UInt32, lplpbBuffer: POINTER(POINTER(Byte)), dwPrefMaxLen: UInt32, lpdwEntriesRead: POINTER(UInt32), lpdwTotalEntries: POINTER(UInt32), lpdwResumeHandle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminInterfaceSetCredentials(lpwsServer: win32more.Windows.Win32.Foundation.PWSTR, lpwsInterfaceName: win32more.Windows.Win32.Foundation.PWSTR, lpwsUserName: win32more.Windows.Win32.Foundation.PWSTR, lpwsDomainName: win32more.Windows.Win32.Foundation.PWSTR, lpwsPassword: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminInterfaceGetCredentials(lpwsServer: win32more.Windows.Win32.Foundation.PWSTR, lpwsInterfaceName: win32more.Windows.Win32.Foundation.PWSTR, lpwsUserName: win32more.Windows.Win32.Foundation.PWSTR, lpwsPassword: win32more.Windows.Win32.Foundation.PWSTR, lpwsDomainName: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminInterfaceSetCredentialsEx(hMprServer: IntPtr, hInterface: win32more.Windows.Win32.Foundation.HANDLE, dwLevel: UInt32, lpbBuffer: POINTER(Byte)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminInterfaceGetCredentialsEx(hMprServer: IntPtr, hInterface: win32more.Windows.Win32.Foundation.HANDLE, dwLevel: UInt32, lplpbBuffer: POINTER(POINTER(Byte))) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminInterfaceConnect(hMprServer: IntPtr, hInterface: win32more.Windows.Win32.Foundation.HANDLE, hEvent: win32more.Windows.Win32.Foundation.HANDLE, fSynchronous: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminInterfaceDisconnect(hMprServer: IntPtr, hInterface: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminInterfaceUpdateRoutes(hMprServer: IntPtr, hInterface: win32more.Windows.Win32.Foundation.HANDLE, dwProtocolId: UInt32, hEvent: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminInterfaceQueryUpdateResult(hMprServer: IntPtr, hInterface: win32more.Windows.Win32.Foundation.HANDLE, dwProtocolId: UInt32, lpdwUpdateResult: POINTER(UInt32)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminInterfaceUpdatePhonebookInfo(hMprServer: IntPtr, hInterface: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminRegisterConnectionNotification(hMprServer: IntPtr, hEventNotification: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminDeregisterConnectionNotification(hMprServer: IntPtr, hEventNotification: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminMIBServerConnect(lpwsServerName: win32more.Windows.Win32.Foundation.PWSTR, phMibServer: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminMIBServerDisconnect(hMibServer: IntPtr) -> Void: ...
@winfunctype('MPRAPI.dll')
def MprAdminMIBEntryCreate(hMibServer: IntPtr, dwPid: UInt32, dwRoutingPid: UInt32, lpEntry: VoidPtr, dwEntrySize: UInt32) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminMIBEntryDelete(hMibServer: IntPtr, dwProtocolId: UInt32, dwRoutingPid: UInt32, lpEntry: VoidPtr, dwEntrySize: UInt32) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminMIBEntrySet(hMibServer: IntPtr, dwProtocolId: UInt32, dwRoutingPid: UInt32, lpEntry: VoidPtr, dwEntrySize: UInt32) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminMIBEntryGet(hMibServer: IntPtr, dwProtocolId: UInt32, dwRoutingPid: UInt32, lpInEntry: VoidPtr, dwInEntrySize: UInt32, lplpOutEntry: POINTER(VoidPtr), lpOutEntrySize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminMIBEntryGetFirst(hMibServer: IntPtr, dwProtocolId: UInt32, dwRoutingPid: UInt32, lpInEntry: VoidPtr, dwInEntrySize: UInt32, lplpOutEntry: POINTER(VoidPtr), lpOutEntrySize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminMIBEntryGetNext(hMibServer: IntPtr, dwProtocolId: UInt32, dwRoutingPid: UInt32, lpInEntry: VoidPtr, dwInEntrySize: UInt32, lplpOutEntry: POINTER(VoidPtr), lpOutEntrySize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprAdminMIBBufferFree(pBuffer: VoidPtr) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprConfigServerInstall(dwLevel: UInt32, pBuffer: VoidPtr) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprConfigServerConnect(lpwsServerName: win32more.Windows.Win32.Foundation.PWSTR, phMprConfig: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprConfigServerDisconnect(hMprConfig: win32more.Windows.Win32.Foundation.HANDLE) -> Void: ...
@winfunctype('MPRAPI.dll')
def MprConfigServerRefresh(hMprConfig: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprConfigBufferFree(pBuffer: VoidPtr) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprConfigServerGetInfo(hMprConfig: win32more.Windows.Win32.Foundation.HANDLE, dwLevel: UInt32, lplpbBuffer: POINTER(POINTER(Byte))) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprConfigServerSetInfo(hMprServer: IntPtr, dwLevel: UInt32, lpbBuffer: POINTER(Byte)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprConfigServerBackup(hMprConfig: win32more.Windows.Win32.Foundation.HANDLE, lpwsPath: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprConfigServerRestore(hMprConfig: win32more.Windows.Win32.Foundation.HANDLE, lpwsPath: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprConfigTransportCreate(hMprConfig: win32more.Windows.Win32.Foundation.HANDLE, dwTransportId: UInt32, lpwsTransportName: win32more.Windows.Win32.Foundation.PWSTR, pGlobalInfo: POINTER(Byte), dwGlobalInfoSize: UInt32, pClientInterfaceInfo: POINTER(Byte), dwClientInterfaceInfoSize: UInt32, lpwsDLLPath: win32more.Windows.Win32.Foundation.PWSTR, phRouterTransport: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprConfigTransportDelete(hMprConfig: win32more.Windows.Win32.Foundation.HANDLE, hRouterTransport: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprConfigTransportGetHandle(hMprConfig: win32more.Windows.Win32.Foundation.HANDLE, dwTransportId: UInt32, phRouterTransport: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprConfigTransportSetInfo(hMprConfig: win32more.Windows.Win32.Foundation.HANDLE, hRouterTransport: win32more.Windows.Win32.Foundation.HANDLE, pGlobalInfo: POINTER(Byte), dwGlobalInfoSize: UInt32, pClientInterfaceInfo: POINTER(Byte), dwClientInterfaceInfoSize: UInt32, lpwsDLLPath: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprConfigTransportGetInfo(hMprConfig: win32more.Windows.Win32.Foundation.HANDLE, hRouterTransport: win32more.Windows.Win32.Foundation.HANDLE, ppGlobalInfo: POINTER(POINTER(Byte)), lpdwGlobalInfoSize: POINTER(UInt32), ppClientInterfaceInfo: POINTER(POINTER(Byte)), lpdwClientInterfaceInfoSize: POINTER(UInt32), lplpwsDLLPath: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprConfigTransportEnum(hMprConfig: win32more.Windows.Win32.Foundation.HANDLE, dwLevel: UInt32, lplpBuffer: POINTER(POINTER(Byte)), dwPrefMaxLen: UInt32, lpdwEntriesRead: POINTER(UInt32), lpdwTotalEntries: POINTER(UInt32), lpdwResumeHandle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprConfigInterfaceCreate(hMprConfig: win32more.Windows.Win32.Foundation.HANDLE, dwLevel: UInt32, lpbBuffer: POINTER(Byte), phRouterInterface: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprConfigInterfaceDelete(hMprConfig: win32more.Windows.Win32.Foundation.HANDLE, hRouterInterface: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprConfigInterfaceGetHandle(hMprConfig: win32more.Windows.Win32.Foundation.HANDLE, lpwsInterfaceName: win32more.Windows.Win32.Foundation.PWSTR, phRouterInterface: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprConfigInterfaceGetInfo(hMprConfig: win32more.Windows.Win32.Foundation.HANDLE, hRouterInterface: win32more.Windows.Win32.Foundation.HANDLE, dwLevel: UInt32, lplpBuffer: POINTER(POINTER(Byte)), lpdwBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprConfigInterfaceSetInfo(hMprConfig: win32more.Windows.Win32.Foundation.HANDLE, hRouterInterface: win32more.Windows.Win32.Foundation.HANDLE, dwLevel: UInt32, lpbBuffer: POINTER(Byte)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprConfigInterfaceEnum(hMprConfig: win32more.Windows.Win32.Foundation.HANDLE, dwLevel: UInt32, lplpBuffer: POINTER(POINTER(Byte)), dwPrefMaxLen: UInt32, lpdwEntriesRead: POINTER(UInt32), lpdwTotalEntries: POINTER(UInt32), lpdwResumeHandle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprConfigInterfaceTransportAdd(hMprConfig: win32more.Windows.Win32.Foundation.HANDLE, hRouterInterface: win32more.Windows.Win32.Foundation.HANDLE, dwTransportId: UInt32, lpwsTransportName: win32more.Windows.Win32.Foundation.PWSTR, pInterfaceInfo: POINTER(Byte), dwInterfaceInfoSize: UInt32, phRouterIfTransport: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprConfigInterfaceTransportRemove(hMprConfig: win32more.Windows.Win32.Foundation.HANDLE, hRouterInterface: win32more.Windows.Win32.Foundation.HANDLE, hRouterIfTransport: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprConfigInterfaceTransportGetHandle(hMprConfig: win32more.Windows.Win32.Foundation.HANDLE, hRouterInterface: win32more.Windows.Win32.Foundation.HANDLE, dwTransportId: UInt32, phRouterIfTransport: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprConfigInterfaceTransportGetInfo(hMprConfig: win32more.Windows.Win32.Foundation.HANDLE, hRouterInterface: win32more.Windows.Win32.Foundation.HANDLE, hRouterIfTransport: win32more.Windows.Win32.Foundation.HANDLE, ppInterfaceInfo: POINTER(POINTER(Byte)), lpdwInterfaceInfoSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprConfigInterfaceTransportSetInfo(hMprConfig: win32more.Windows.Win32.Foundation.HANDLE, hRouterInterface: win32more.Windows.Win32.Foundation.HANDLE, hRouterIfTransport: win32more.Windows.Win32.Foundation.HANDLE, pInterfaceInfo: POINTER(Byte), dwInterfaceInfoSize: UInt32) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprConfigInterfaceTransportEnum(hMprConfig: win32more.Windows.Win32.Foundation.HANDLE, hRouterInterface: win32more.Windows.Win32.Foundation.HANDLE, dwLevel: UInt32, lplpBuffer: POINTER(POINTER(Byte)), dwPrefMaxLen: UInt32, lpdwEntriesRead: POINTER(UInt32), lpdwTotalEntries: POINTER(UInt32), lpdwResumeHandle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprConfigGetFriendlyName(hMprConfig: win32more.Windows.Win32.Foundation.HANDLE, pszGuidName: win32more.Windows.Win32.Foundation.PWSTR, pszBuffer: win32more.Windows.Win32.Foundation.PWSTR, dwBufferSize: UInt32) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprConfigGetGuidName(hMprConfig: win32more.Windows.Win32.Foundation.HANDLE, pszFriendlyName: win32more.Windows.Win32.Foundation.PWSTR, pszBuffer: win32more.Windows.Win32.Foundation.PWSTR, dwBufferSize: UInt32) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprConfigFilterGetInfo(hMprConfig: win32more.Windows.Win32.Foundation.HANDLE, dwLevel: UInt32, dwTransportId: UInt32, lpBuffer: POINTER(Byte)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprConfigFilterSetInfo(hMprConfig: win32more.Windows.Win32.Foundation.HANDLE, dwLevel: UInt32, dwTransportId: UInt32, lpBuffer: POINTER(Byte)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprInfoCreate(dwVersion: UInt32, lplpNewHeader: POINTER(VoidPtr)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprInfoDelete(lpHeader: VoidPtr) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprInfoRemoveAll(lpHeader: VoidPtr, lplpNewHeader: POINTER(VoidPtr)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprInfoDuplicate(lpHeader: VoidPtr, lplpNewHeader: POINTER(VoidPtr)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprInfoBlockAdd(lpHeader: VoidPtr, dwInfoType: UInt32, dwItemSize: UInt32, dwItemCount: UInt32, lpItemData: POINTER(Byte), lplpNewHeader: POINTER(VoidPtr)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprInfoBlockRemove(lpHeader: VoidPtr, dwInfoType: UInt32, lplpNewHeader: POINTER(VoidPtr)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprInfoBlockSet(lpHeader: VoidPtr, dwInfoType: UInt32, dwItemSize: UInt32, dwItemCount: UInt32, lpItemData: POINTER(Byte), lplpNewHeader: POINTER(VoidPtr)) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprInfoBlockFind(lpHeader: VoidPtr, dwInfoType: UInt32, lpdwItemSize: POINTER(UInt32), lpdwItemCount: POINTER(UInt32), lplpItemData: POINTER(POINTER(Byte))) -> UInt32: ...
@winfunctype('MPRAPI.dll')
def MprInfoBlockQuerySize(lpHeader: VoidPtr) -> UInt32: ...
@winfunctype('rtm.dll')
def MgmRegisterMProtocol(prpiInfo: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.ROUTING_PROTOCOL_CONFIG), dwProtocolId: UInt32, dwComponentId: UInt32, phProtocol: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('rtm.dll')
def MgmDeRegisterMProtocol(hProtocol: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('rtm.dll')
def MgmTakeInterfaceOwnership(hProtocol: win32more.Windows.Win32.Foundation.HANDLE, dwIfIndex: UInt32, dwIfNextHopAddr: UInt32) -> UInt32: ...
@winfunctype('rtm.dll')
def MgmReleaseInterfaceOwnership(hProtocol: win32more.Windows.Win32.Foundation.HANDLE, dwIfIndex: UInt32, dwIfNextHopAddr: UInt32) -> UInt32: ...
@winfunctype('rtm.dll')
def MgmGetProtocolOnInterface(dwIfIndex: UInt32, dwIfNextHopAddr: UInt32, pdwIfProtocolId: POINTER(UInt32), pdwIfComponentId: POINTER(UInt32)) -> UInt32: ...
@winfunctype('rtm.dll')
def MgmAddGroupMembershipEntry(hProtocol: win32more.Windows.Win32.Foundation.HANDLE, dwSourceAddr: UInt32, dwSourceMask: UInt32, dwGroupAddr: UInt32, dwGroupMask: UInt32, dwIfIndex: UInt32, dwIfNextHopIPAddr: UInt32, dwFlags: UInt32) -> UInt32: ...
@winfunctype('rtm.dll')
def MgmDeleteGroupMembershipEntry(hProtocol: win32more.Windows.Win32.Foundation.HANDLE, dwSourceAddr: UInt32, dwSourceMask: UInt32, dwGroupAddr: UInt32, dwGroupMask: UInt32, dwIfIndex: UInt32, dwIfNextHopIPAddr: UInt32, dwFlags: UInt32) -> UInt32: ...
@winfunctype('rtm.dll')
def MgmGetMfe(pimm: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPMCAST_MFE), pdwBufferSize: POINTER(UInt32), pbBuffer: POINTER(Byte)) -> UInt32: ...
@winfunctype('rtm.dll')
def MgmGetFirstMfe(pdwBufferSize: POINTER(UInt32), pbBuffer: POINTER(Byte), pdwNumEntries: POINTER(UInt32)) -> UInt32: ...
@winfunctype('rtm.dll')
def MgmGetNextMfe(pimmStart: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPMCAST_MFE), pdwBufferSize: POINTER(UInt32), pbBuffer: POINTER(Byte), pdwNumEntries: POINTER(UInt32)) -> UInt32: ...
@winfunctype('rtm.dll')
def MgmGetMfeStats(pimm: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPMCAST_MFE), pdwBufferSize: POINTER(UInt32), pbBuffer: POINTER(Byte), dwFlags: UInt32) -> UInt32: ...
@winfunctype('rtm.dll')
def MgmGetFirstMfeStats(pdwBufferSize: POINTER(UInt32), pbBuffer: POINTER(Byte), pdwNumEntries: POINTER(UInt32), dwFlags: UInt32) -> UInt32: ...
@winfunctype('rtm.dll')
def MgmGetNextMfeStats(pimmStart: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPMCAST_MFE), pdwBufferSize: POINTER(UInt32), pbBuffer: POINTER(Byte), pdwNumEntries: POINTER(UInt32), dwFlags: UInt32) -> UInt32: ...
@winfunctype('rtm.dll')
def MgmGroupEnumerationStart(hProtocol: win32more.Windows.Win32.Foundation.HANDLE, metEnumType: win32more.Windows.Win32.NetworkManagement.Rras.MGM_ENUM_TYPES, phEnumHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('rtm.dll')
def MgmGroupEnumerationGetNext(hEnum: win32more.Windows.Win32.Foundation.HANDLE, pdwBufferSize: POINTER(UInt32), pbBuffer: POINTER(Byte), pdwNumEntries: POINTER(UInt32)) -> UInt32: ...
@winfunctype('rtm.dll')
def MgmGroupEnumerationEnd(hEnum: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmConvertNetAddressToIpv6AddressAndLength(pNetAddress: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RTM_NET_ADDRESS), pAddress: POINTER(win32more.Windows.Win32.Networking.WinSock.IN6_ADDR), pLength: POINTER(UInt32), dwAddressSize: UInt32) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmConvertIpv6AddressAndLengthToNetAddress(pNetAddress: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RTM_NET_ADDRESS), Address: win32more.Windows.Win32.Networking.WinSock.IN6_ADDR, dwLength: UInt32, dwAddressSize: UInt32) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmRegisterEntity(RtmEntityInfo: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RTM_ENTITY_INFO), ExportMethods: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RTM_ENTITY_EXPORT_METHODS), EventCallback: win32more.Windows.Win32.NetworkManagement.Rras.RTM_EVENT_CALLBACK, ReserveOpaquePointer: win32more.Windows.Win32.Foundation.BOOL, RtmRegProfile: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RTM_REGN_PROFILE), RtmRegHandle: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmDeregisterEntity(RtmRegHandle: IntPtr) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmGetRegisteredEntities(RtmRegHandle: IntPtr, NumEntities: POINTER(UInt32), EntityHandles: POINTER(IntPtr), EntityInfos: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RTM_ENTITY_INFO)) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmReleaseEntities(RtmRegHandle: IntPtr, NumEntities: UInt32, EntityHandles: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmLockDestination(RtmRegHandle: IntPtr, DestHandle: IntPtr, Exclusive: win32more.Windows.Win32.Foundation.BOOL, LockDest: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmGetOpaqueInformationPointer(RtmRegHandle: IntPtr, DestHandle: IntPtr, OpaqueInfoPointer: POINTER(VoidPtr)) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmGetEntityMethods(RtmRegHandle: IntPtr, EntityHandle: IntPtr, NumMethods: POINTER(UInt32), ExptMethods: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RTM_ENTITY_EXPORT_METHOD)) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmInvokeMethod(RtmRegHandle: IntPtr, EntityHandle: IntPtr, Input: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RTM_ENTITY_METHOD_INPUT), OutputSize: POINTER(UInt32), Output: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RTM_ENTITY_METHOD_OUTPUT)) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmBlockMethods(RtmRegHandle: IntPtr, TargetHandle: win32more.Windows.Win32.Foundation.HANDLE, TargetType: Byte, BlockingFlag: UInt32) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmGetEntityInfo(RtmRegHandle: IntPtr, EntityHandle: IntPtr, EntityInfo: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RTM_ENTITY_INFO)) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmGetDestInfo(RtmRegHandle: IntPtr, DestHandle: IntPtr, ProtocolId: UInt32, TargetViews: UInt32, DestInfo: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RTM_DEST_INFO)) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmGetRouteInfo(RtmRegHandle: IntPtr, RouteHandle: IntPtr, RouteInfo: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RTM_ROUTE_INFO), DestAddress: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RTM_NET_ADDRESS)) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmGetNextHopInfo(RtmRegHandle: IntPtr, NextHopHandle: IntPtr, NextHopInfo: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RTM_NEXTHOP_INFO)) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmReleaseEntityInfo(RtmRegHandle: IntPtr, EntityInfo: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RTM_ENTITY_INFO)) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmReleaseDestInfo(RtmRegHandle: IntPtr, DestInfo: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RTM_DEST_INFO)) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmReleaseRouteInfo(RtmRegHandle: IntPtr, RouteInfo: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RTM_ROUTE_INFO)) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmReleaseNextHopInfo(RtmRegHandle: IntPtr, NextHopInfo: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RTM_NEXTHOP_INFO)) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmAddRouteToDest(RtmRegHandle: IntPtr, RouteHandle: POINTER(IntPtr), DestAddress: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RTM_NET_ADDRESS), RouteInfo: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RTM_ROUTE_INFO), TimeToLive: UInt32, RouteListHandle: IntPtr, NotifyType: UInt32, NotifyHandle: IntPtr, ChangeFlags: POINTER(UInt32)) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmDeleteRouteToDest(RtmRegHandle: IntPtr, RouteHandle: IntPtr, ChangeFlags: POINTER(UInt32)) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmHoldDestination(RtmRegHandle: IntPtr, DestHandle: IntPtr, TargetViews: UInt32, HoldTime: UInt32) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmGetRoutePointer(RtmRegHandle: IntPtr, RouteHandle: IntPtr, RoutePointer: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RTM_ROUTE_INFO))) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmLockRoute(RtmRegHandle: IntPtr, RouteHandle: IntPtr, Exclusive: win32more.Windows.Win32.Foundation.BOOL, LockRoute: win32more.Windows.Win32.Foundation.BOOL, RoutePointer: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RTM_ROUTE_INFO))) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmUpdateAndUnlockRoute(RtmRegHandle: IntPtr, RouteHandle: IntPtr, TimeToLive: UInt32, RouteListHandle: IntPtr, NotifyType: UInt32, NotifyHandle: IntPtr, ChangeFlags: POINTER(UInt32)) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmGetExactMatchDestination(RtmRegHandle: IntPtr, DestAddress: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RTM_NET_ADDRESS), ProtocolId: UInt32, TargetViews: UInt32, DestInfo: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RTM_DEST_INFO)) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmGetMostSpecificDestination(RtmRegHandle: IntPtr, DestAddress: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RTM_NET_ADDRESS), ProtocolId: UInt32, TargetViews: UInt32, DestInfo: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RTM_DEST_INFO)) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmGetLessSpecificDestination(RtmRegHandle: IntPtr, DestHandle: IntPtr, ProtocolId: UInt32, TargetViews: UInt32, DestInfo: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RTM_DEST_INFO)) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmGetExactMatchRoute(RtmRegHandle: IntPtr, DestAddress: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RTM_NET_ADDRESS), MatchingFlags: UInt32, RouteInfo: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RTM_ROUTE_INFO), InterfaceIndex: UInt32, TargetViews: UInt32, RouteHandle: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmIsBestRoute(RtmRegHandle: IntPtr, RouteHandle: IntPtr, BestInViews: POINTER(UInt32)) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmAddNextHop(RtmRegHandle: IntPtr, NextHopInfo: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RTM_NEXTHOP_INFO), NextHopHandle: POINTER(IntPtr), ChangeFlags: POINTER(UInt32)) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmFindNextHop(RtmRegHandle: IntPtr, NextHopInfo: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RTM_NEXTHOP_INFO), NextHopHandle: POINTER(IntPtr), NextHopPointer: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RTM_NEXTHOP_INFO))) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmDeleteNextHop(RtmRegHandle: IntPtr, NextHopHandle: IntPtr, NextHopInfo: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RTM_NEXTHOP_INFO)) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmGetNextHopPointer(RtmRegHandle: IntPtr, NextHopHandle: IntPtr, NextHopPointer: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RTM_NEXTHOP_INFO))) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmLockNextHop(RtmRegHandle: IntPtr, NextHopHandle: IntPtr, Exclusive: win32more.Windows.Win32.Foundation.BOOL, LockNextHop: win32more.Windows.Win32.Foundation.BOOL, NextHopPointer: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RTM_NEXTHOP_INFO))) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmCreateDestEnum(RtmRegHandle: IntPtr, TargetViews: UInt32, EnumFlags: UInt32, NetAddress: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RTM_NET_ADDRESS), ProtocolId: UInt32, RtmEnumHandle: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmGetEnumDests(RtmRegHandle: IntPtr, EnumHandle: IntPtr, NumDests: POINTER(UInt32), DestInfos: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RTM_DEST_INFO)) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmReleaseDests(RtmRegHandle: IntPtr, NumDests: UInt32, DestInfos: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RTM_DEST_INFO)) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmCreateRouteEnum(RtmRegHandle: IntPtr, DestHandle: IntPtr, TargetViews: UInt32, EnumFlags: UInt32, StartDest: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RTM_NET_ADDRESS), MatchingFlags: UInt32, CriteriaRoute: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RTM_ROUTE_INFO), CriteriaInterface: UInt32, RtmEnumHandle: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmGetEnumRoutes(RtmRegHandle: IntPtr, EnumHandle: IntPtr, NumRoutes: POINTER(UInt32), RouteHandles: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmReleaseRoutes(RtmRegHandle: IntPtr, NumRoutes: UInt32, RouteHandles: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmCreateNextHopEnum(RtmRegHandle: IntPtr, EnumFlags: UInt32, NetAddress: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RTM_NET_ADDRESS), RtmEnumHandle: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmGetEnumNextHops(RtmRegHandle: IntPtr, EnumHandle: IntPtr, NumNextHops: POINTER(UInt32), NextHopHandles: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmReleaseNextHops(RtmRegHandle: IntPtr, NumNextHops: UInt32, NextHopHandles: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmDeleteEnumHandle(RtmRegHandle: IntPtr, EnumHandle: IntPtr) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmRegisterForChangeNotification(RtmRegHandle: IntPtr, TargetViews: UInt32, NotifyFlags: UInt32, NotifyContext: VoidPtr, NotifyHandle: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmGetChangedDests(RtmRegHandle: IntPtr, NotifyHandle: IntPtr, NumDests: POINTER(UInt32), ChangedDests: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RTM_DEST_INFO)) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmReleaseChangedDests(RtmRegHandle: IntPtr, NotifyHandle: IntPtr, NumDests: UInt32, ChangedDests: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RTM_DEST_INFO)) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmIgnoreChangedDests(RtmRegHandle: IntPtr, NotifyHandle: IntPtr, NumDests: UInt32, ChangedDests: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmGetChangeStatus(RtmRegHandle: IntPtr, NotifyHandle: IntPtr, DestHandle: IntPtr, ChangeStatus: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmMarkDestForChangeNotification(RtmRegHandle: IntPtr, NotifyHandle: IntPtr, DestHandle: IntPtr, MarkDest: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmIsMarkedForChangeNotification(RtmRegHandle: IntPtr, NotifyHandle: IntPtr, DestHandle: IntPtr, DestMarked: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmDeregisterFromChangeNotification(RtmRegHandle: IntPtr, NotifyHandle: IntPtr) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmCreateRouteList(RtmRegHandle: IntPtr, RouteListHandle: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmInsertInRouteList(RtmRegHandle: IntPtr, RouteListHandle: IntPtr, NumRoutes: UInt32, RouteHandles: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmCreateRouteListEnum(RtmRegHandle: IntPtr, RouteListHandle: IntPtr, RtmEnumHandle: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmGetListEnumRoutes(RtmRegHandle: IntPtr, EnumHandle: IntPtr, NumRoutes: POINTER(UInt32), RouteHandles: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmDeleteRouteList(RtmRegHandle: IntPtr, RouteListHandle: IntPtr) -> UInt32: ...
@winfunctype('rtm.dll')
def RtmReferenceHandles(RtmRegHandle: IntPtr, NumHandles: UInt32, RtmHandles: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
class GRE_CONFIG_PARAMS0(Structure):
    dwNumPorts: UInt32
    dwPortFlags: UInt32
HRASCONN = VoidPtr
class IKEV2_CONFIG_PARAMS(Structure):
    dwNumPorts: UInt32
    dwPortFlags: UInt32
    dwTunnelConfigParamFlags: UInt32
    TunnelConfigParams: win32more.Windows.Win32.NetworkManagement.Rras.IKEV2_TUNNEL_CONFIG_PARAMS4
IKEV2_ID_PAYLOAD_TYPE = Int32
IKEV2_ID_PAYLOAD_TYPE_INVALID: win32more.Windows.Win32.NetworkManagement.Rras.IKEV2_ID_PAYLOAD_TYPE = 0
IKEV2_ID_PAYLOAD_TYPE_IPV4_ADDR: win32more.Windows.Win32.NetworkManagement.Rras.IKEV2_ID_PAYLOAD_TYPE = 1
IKEV2_ID_PAYLOAD_TYPE_FQDN: win32more.Windows.Win32.NetworkManagement.Rras.IKEV2_ID_PAYLOAD_TYPE = 2
IKEV2_ID_PAYLOAD_TYPE_RFC822_ADDR: win32more.Windows.Win32.NetworkManagement.Rras.IKEV2_ID_PAYLOAD_TYPE = 3
IKEV2_ID_PAYLOAD_TYPE_RESERVED1: win32more.Windows.Win32.NetworkManagement.Rras.IKEV2_ID_PAYLOAD_TYPE = 4
IKEV2_ID_PAYLOAD_TYPE_ID_IPV6_ADDR: win32more.Windows.Win32.NetworkManagement.Rras.IKEV2_ID_PAYLOAD_TYPE = 5
IKEV2_ID_PAYLOAD_TYPE_RESERVED2: win32more.Windows.Win32.NetworkManagement.Rras.IKEV2_ID_PAYLOAD_TYPE = 6
IKEV2_ID_PAYLOAD_TYPE_RESERVED3: win32more.Windows.Win32.NetworkManagement.Rras.IKEV2_ID_PAYLOAD_TYPE = 7
IKEV2_ID_PAYLOAD_TYPE_RESERVED4: win32more.Windows.Win32.NetworkManagement.Rras.IKEV2_ID_PAYLOAD_TYPE = 8
IKEV2_ID_PAYLOAD_TYPE_DER_ASN1_DN: win32more.Windows.Win32.NetworkManagement.Rras.IKEV2_ID_PAYLOAD_TYPE = 9
IKEV2_ID_PAYLOAD_TYPE_DER_ASN1_GN: win32more.Windows.Win32.NetworkManagement.Rras.IKEV2_ID_PAYLOAD_TYPE = 10
IKEV2_ID_PAYLOAD_TYPE_KEY_ID: win32more.Windows.Win32.NetworkManagement.Rras.IKEV2_ID_PAYLOAD_TYPE = 11
IKEV2_ID_PAYLOAD_TYPE_MAX: win32more.Windows.Win32.NetworkManagement.Rras.IKEV2_ID_PAYLOAD_TYPE = 12
class IKEV2_PROJECTION_INFO(Structure):
    dwIPv4NegotiationError: UInt32
    wszAddress: Char * 16
    wszRemoteAddress: Char * 16
    IPv4SubInterfaceIndex: UInt64
    dwIPv6NegotiationError: UInt32
    bInterfaceIdentifier: Byte * 8
    bRemoteInterfaceIdentifier: Byte * 8
    bPrefix: Byte * 8
    dwPrefixLength: UInt32
    IPv6SubInterfaceIndex: UInt64
    dwOptions: UInt32
    dwAuthenticationProtocol: UInt32
    dwEapTypeId: UInt32
    dwCompressionAlgorithm: UInt32
    dwEncryptionMethod: UInt32
class IKEV2_PROJECTION_INFO2(Structure):
    dwIPv4NegotiationError: UInt32
    wszAddress: Char * 16
    wszRemoteAddress: Char * 16
    IPv4SubInterfaceIndex: UInt64
    dwIPv6NegotiationError: UInt32
    bInterfaceIdentifier: Byte * 8
    bRemoteInterfaceIdentifier: Byte * 8
    bPrefix: Byte * 8
    dwPrefixLength: UInt32
    IPv6SubInterfaceIndex: UInt64
    dwOptions: UInt32
    dwAuthenticationProtocol: UInt32
    dwEapTypeId: UInt32
    dwEmbeddedEAPTypeId: UInt32
    dwCompressionAlgorithm: UInt32
    dwEncryptionMethod: UInt32
class IKEV2_TUNNEL_CONFIG_PARAMS2(Structure):
    dwIdleTimeout: UInt32
    dwNetworkBlackoutTime: UInt32
    dwSaLifeTime: UInt32
    dwSaDataSizeForRenegotiation: UInt32
    dwConfigOptions: UInt32
    dwTotalCertificates: UInt32
    certificateNames: POINTER(win32more.Windows.Win32.Security.Cryptography.CRYPT_INTEGER_BLOB)
    machineCertificateName: win32more.Windows.Win32.Security.Cryptography.CRYPT_INTEGER_BLOB
    dwEncryptionType: UInt32
    customPolicy: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.ROUTER_CUSTOM_IKEv2_POLICY0)
class IKEV2_TUNNEL_CONFIG_PARAMS3(Structure):
    dwIdleTimeout: UInt32
    dwNetworkBlackoutTime: UInt32
    dwSaLifeTime: UInt32
    dwSaDataSizeForRenegotiation: UInt32
    dwConfigOptions: UInt32
    dwTotalCertificates: UInt32
    certificateNames: POINTER(win32more.Windows.Win32.Security.Cryptography.CRYPT_INTEGER_BLOB)
    machineCertificateName: win32more.Windows.Win32.Security.Cryptography.CRYPT_INTEGER_BLOB
    dwEncryptionType: UInt32
    customPolicy: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.ROUTER_CUSTOM_IKEv2_POLICY0)
    dwTotalEkus: UInt32
    certificateEKUs: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.MPR_CERT_EKU)
    machineCertificateHash: win32more.Windows.Win32.Security.Cryptography.CRYPT_INTEGER_BLOB
class IKEV2_TUNNEL_CONFIG_PARAMS4(Structure):
    dwIdleTimeout: UInt32
    dwNetworkBlackoutTime: UInt32
    dwSaLifeTime: UInt32
    dwSaDataSizeForRenegotiation: UInt32
    dwConfigOptions: UInt32
    dwTotalCertificates: UInt32
    certificateNames: POINTER(win32more.Windows.Win32.Security.Cryptography.CRYPT_INTEGER_BLOB)
    machineCertificateName: win32more.Windows.Win32.Security.Cryptography.CRYPT_INTEGER_BLOB
    dwEncryptionType: UInt32
    customPolicy: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.ROUTER_CUSTOM_IKEv2_POLICY0)
    dwTotalEkus: UInt32
    certificateEKUs: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.MPR_CERT_EKU)
    machineCertificateHash: win32more.Windows.Win32.Security.Cryptography.CRYPT_INTEGER_BLOB
    dwMmSaLifeTime: UInt32
class L2TP_CONFIG_PARAMS0(Structure):
    dwNumPorts: UInt32
    dwPortFlags: UInt32
class L2TP_CONFIG_PARAMS1(Structure):
    dwNumPorts: UInt32
    dwPortFlags: UInt32
    dwTunnelConfigParamFlags: UInt32
    TunnelConfigParams: win32more.Windows.Win32.NetworkManagement.Rras.L2TP_TUNNEL_CONFIG_PARAMS2
class L2TP_TUNNEL_CONFIG_PARAMS1(Structure):
    dwIdleTimeout: UInt32
    dwEncryptionType: UInt32
    dwSaLifeTime: UInt32
    dwSaDataSizeForRenegotiation: UInt32
    customPolicy: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.ROUTER_CUSTOM_IKEv2_POLICY0)
class L2TP_TUNNEL_CONFIG_PARAMS2(Structure):
    dwIdleTimeout: UInt32
    dwEncryptionType: UInt32
    dwSaLifeTime: UInt32
    dwSaDataSizeForRenegotiation: UInt32
    customPolicy: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.ROUTER_CUSTOM_IKEv2_POLICY0)
    dwMmSaLifeTime: UInt32
MGM_ENUM_TYPES = Int32
ANY_SOURCE: win32more.Windows.Win32.NetworkManagement.Rras.MGM_ENUM_TYPES = 0
ALL_SOURCES: win32more.Windows.Win32.NetworkManagement.Rras.MGM_ENUM_TYPES = 1
class MGM_IF_ENTRY(Structure):
    dwIfIndex: UInt32
    dwIfNextHopAddr: UInt32
    bIGMP: win32more.Windows.Win32.Foundation.BOOL
    bIsEnabled: win32more.Windows.Win32.Foundation.BOOL
class MPRAPI_ADMIN_DLL_CALLBACKS(Structure):
    revision: Byte
    lpfnMprAdminGetIpAddressForUser: win32more.Windows.Win32.NetworkManagement.Rras.PMPRADMINGETIPADDRESSFORUSER
    lpfnMprAdminReleaseIpAddress: win32more.Windows.Win32.NetworkManagement.Rras.PMPRADMINRELEASEIPADRESS
    lpfnMprAdminGetIpv6AddressForUser: win32more.Windows.Win32.NetworkManagement.Rras.PMPRADMINGETIPV6ADDRESSFORUSER
    lpfnMprAdminReleaseIpV6AddressForUser: win32more.Windows.Win32.NetworkManagement.Rras.PMPRADMINRELEASEIPV6ADDRESSFORUSER
    lpfnRasAdminAcceptNewLink: win32more.Windows.Win32.NetworkManagement.Rras.PMPRADMINACCEPTNEWLINK
    lpfnRasAdminLinkHangupNotification: win32more.Windows.Win32.NetworkManagement.Rras.PMPRADMINLINKHANGUPNOTIFICATION
    lpfnRasAdminTerminateDll: win32more.Windows.Win32.NetworkManagement.Rras.PMPRADMINTERMINATEDLL
    lpfnRasAdminAcceptNewConnectionEx: win32more.Windows.Win32.NetworkManagement.Rras.PMPRADMINACCEPTNEWCONNECTIONEX
    lpfnRasAdminAcceptEndpointChangeEx: win32more.Windows.Win32.NetworkManagement.Rras.PMPRADMINACCEPTTUNNELENDPOINTCHANGEEX
    lpfnRasAdminAcceptReauthenticationEx: win32more.Windows.Win32.NetworkManagement.Rras.PMPRADMINACCEPTREAUTHENTICATIONEX
    lpfnRasAdminConnectionHangupNotificationEx: win32more.Windows.Win32.NetworkManagement.Rras.PMPRADMINCONNECTIONHANGUPNOTIFICATIONEX
    lpfnRASValidatePreAuthenticatedConnectionEx: win32more.Windows.Win32.NetworkManagement.Rras.PMPRADMINRASVALIDATEPREAUTHENTICATEDCONNECTIONEX
class MPRAPI_OBJECT_HEADER(Structure):
    revision: Byte
    type: Byte
    size: UInt16
MPRAPI_OBJECT_TYPE = Int32
MPRAPI_OBJECT_TYPE_RAS_CONNECTION_OBJECT: win32more.Windows.Win32.NetworkManagement.Rras.MPRAPI_OBJECT_TYPE = 1
MPRAPI_OBJECT_TYPE_MPR_SERVER_OBJECT: win32more.Windows.Win32.NetworkManagement.Rras.MPRAPI_OBJECT_TYPE = 2
MPRAPI_OBJECT_TYPE_MPR_SERVER_SET_CONFIG_OBJECT: win32more.Windows.Win32.NetworkManagement.Rras.MPRAPI_OBJECT_TYPE = 3
MPRAPI_OBJECT_TYPE_AUTH_VALIDATION_OBJECT: win32more.Windows.Win32.NetworkManagement.Rras.MPRAPI_OBJECT_TYPE = 4
MPRAPI_OBJECT_TYPE_UPDATE_CONNECTION_OBJECT: win32more.Windows.Win32.NetworkManagement.Rras.MPRAPI_OBJECT_TYPE = 5
MPRAPI_OBJECT_TYPE_IF_CUSTOM_CONFIG_OBJECT: win32more.Windows.Win32.NetworkManagement.Rras.MPRAPI_OBJECT_TYPE = 6
class MPRAPI_TUNNEL_CONFIG_PARAMS0(Structure):
    IkeConfigParams: win32more.Windows.Win32.NetworkManagement.Rras.IKEV2_CONFIG_PARAMS
    PptpConfigParams: win32more.Windows.Win32.NetworkManagement.Rras.PPTP_CONFIG_PARAMS
    L2tpConfigParams: win32more.Windows.Win32.NetworkManagement.Rras.L2TP_CONFIG_PARAMS1
    SstpConfigParams: win32more.Windows.Win32.NetworkManagement.Rras.SSTP_CONFIG_PARAMS
class MPRAPI_TUNNEL_CONFIG_PARAMS1(Structure):
    IkeConfigParams: win32more.Windows.Win32.NetworkManagement.Rras.IKEV2_CONFIG_PARAMS
    PptpConfigParams: win32more.Windows.Win32.NetworkManagement.Rras.PPTP_CONFIG_PARAMS
    L2tpConfigParams: win32more.Windows.Win32.NetworkManagement.Rras.L2TP_CONFIG_PARAMS1
    SstpConfigParams: win32more.Windows.Win32.NetworkManagement.Rras.SSTP_CONFIG_PARAMS
    GREConfigParams: win32more.Windows.Win32.NetworkManagement.Rras.GRE_CONFIG_PARAMS0
class MPR_CERT_EKU(Structure):
    dwSize: UInt32
    IsEKUOID: win32more.Windows.Win32.Foundation.BOOL
    pwszEKU: win32more.Windows.Win32.Foundation.PWSTR
class MPR_CREDENTIALSEX_0(Structure):
    dwSize: UInt32
    lpbCredentialsInfo: POINTER(Byte)
class MPR_CREDENTIALSEX_1(Structure):
    dwSize: UInt32
    lpbCredentialsInfo: POINTER(Byte)
class MPR_DEVICE_0(Structure):
    szDeviceType: Char * 17
    szDeviceName: Char * 129
class MPR_DEVICE_1(Structure):
    szDeviceType: Char * 17
    szDeviceName: Char * 129
    szLocalPhoneNumber: Char * 129
    szAlternates: win32more.Windows.Win32.Foundation.PWSTR
MPR_ET = UInt32
MPR_ET_None: win32more.Windows.Win32.NetworkManagement.Rras.MPR_ET = 0
MPR_ET_Require: win32more.Windows.Win32.NetworkManagement.Rras.MPR_ET = 1
MPR_ET_RequireMax: win32more.Windows.Win32.NetworkManagement.Rras.MPR_ET = 2
MPR_ET_Optional: win32more.Windows.Win32.NetworkManagement.Rras.MPR_ET = 3
class MPR_FILTER_0(Structure):
    fEnable: win32more.Windows.Win32.Foundation.BOOL
class MPR_IFTRANSPORT_0(Structure):
    dwTransportId: UInt32
    hIfTransport: win32more.Windows.Win32.Foundation.HANDLE
    wszIfTransportName: Char * 41
class MPR_IF_CUSTOMINFOEX0(Structure):
    Header: win32more.Windows.Win32.NetworkManagement.Rras.MPRAPI_OBJECT_HEADER
    dwFlags: UInt32
    customIkev2Config: win32more.Windows.Win32.NetworkManagement.Rras.ROUTER_IKEv2_IF_CUSTOM_CONFIG0
class MPR_IF_CUSTOMINFOEX1(Structure):
    Header: win32more.Windows.Win32.NetworkManagement.Rras.MPRAPI_OBJECT_HEADER
    dwFlags: UInt32
    customIkev2Config: win32more.Windows.Win32.NetworkManagement.Rras.ROUTER_IKEv2_IF_CUSTOM_CONFIG1
class MPR_IF_CUSTOMINFOEX2(Structure):
    Header: win32more.Windows.Win32.NetworkManagement.Rras.MPRAPI_OBJECT_HEADER
    dwFlags: UInt32
    customIkev2Config: win32more.Windows.Win32.NetworkManagement.Rras.ROUTER_IKEv2_IF_CUSTOM_CONFIG2
class MPR_INTERFACE_0(Structure):
    wszInterfaceName: Char * 257
    hInterface: win32more.Windows.Win32.Foundation.HANDLE
    fEnabled: win32more.Windows.Win32.Foundation.BOOL
    dwIfType: win32more.Windows.Win32.NetworkManagement.Rras.ROUTER_INTERFACE_TYPE
    dwConnectionState: win32more.Windows.Win32.NetworkManagement.Rras.ROUTER_CONNECTION_STATE
    fUnReachabilityReasons: UInt32
    dwLastError: UInt32
class MPR_INTERFACE_1(Structure):
    wszInterfaceName: Char * 257
    hInterface: win32more.Windows.Win32.Foundation.HANDLE
    fEnabled: win32more.Windows.Win32.Foundation.BOOL
    dwIfType: win32more.Windows.Win32.NetworkManagement.Rras.ROUTER_INTERFACE_TYPE
    dwConnectionState: win32more.Windows.Win32.NetworkManagement.Rras.ROUTER_CONNECTION_STATE
    fUnReachabilityReasons: UInt32
    dwLastError: UInt32
    lpwsDialoutHoursRestriction: win32more.Windows.Win32.Foundation.PWSTR
class MPR_INTERFACE_2(Structure):
    wszInterfaceName: Char * 257
    hInterface: win32more.Windows.Win32.Foundation.HANDLE
    fEnabled: win32more.Windows.Win32.Foundation.BOOL
    dwIfType: win32more.Windows.Win32.NetworkManagement.Rras.ROUTER_INTERFACE_TYPE
    dwConnectionState: win32more.Windows.Win32.NetworkManagement.Rras.ROUTER_CONNECTION_STATE
    fUnReachabilityReasons: UInt32
    dwLastError: UInt32
    dwfOptions: UInt32
    szLocalPhoneNumber: Char * 129
    szAlternates: win32more.Windows.Win32.Foundation.PWSTR
    ipaddr: UInt32
    ipaddrDns: UInt32
    ipaddrDnsAlt: UInt32
    ipaddrWins: UInt32
    ipaddrWinsAlt: UInt32
    dwfNetProtocols: UInt32
    szDeviceType: Char * 17
    szDeviceName: Char * 129
    szX25PadType: Char * 33
    szX25Address: Char * 201
    szX25Facilities: Char * 201
    szX25UserData: Char * 201
    dwChannels: UInt32
    dwSubEntries: UInt32
    dwDialMode: win32more.Windows.Win32.NetworkManagement.Rras.MPR_INTERFACE_DIAL_MODE
    dwDialExtraPercent: UInt32
    dwDialExtraSampleSeconds: UInt32
    dwHangUpExtraPercent: UInt32
    dwHangUpExtraSampleSeconds: UInt32
    dwIdleDisconnectSeconds: UInt32
    dwType: UInt32
    dwEncryptionType: win32more.Windows.Win32.NetworkManagement.Rras.MPR_ET
    dwCustomAuthKey: UInt32
    dwCustomAuthDataSize: UInt32
    lpbCustomAuthData: POINTER(Byte)
    guidId: Guid
    dwVpnStrategy: win32more.Windows.Win32.NetworkManagement.Rras.MPR_VS
class MPR_INTERFACE_3(Structure):
    wszInterfaceName: Char * 257
    hInterface: win32more.Windows.Win32.Foundation.HANDLE
    fEnabled: win32more.Windows.Win32.Foundation.BOOL
    dwIfType: win32more.Windows.Win32.NetworkManagement.Rras.ROUTER_INTERFACE_TYPE
    dwConnectionState: win32more.Windows.Win32.NetworkManagement.Rras.ROUTER_CONNECTION_STATE
    fUnReachabilityReasons: UInt32
    dwLastError: UInt32
    dwfOptions: UInt32
    szLocalPhoneNumber: Char * 129
    szAlternates: win32more.Windows.Win32.Foundation.PWSTR
    ipaddr: UInt32
    ipaddrDns: UInt32
    ipaddrDnsAlt: UInt32
    ipaddrWins: UInt32
    ipaddrWinsAlt: UInt32
    dwfNetProtocols: UInt32
    szDeviceType: Char * 17
    szDeviceName: Char * 129
    szX25PadType: Char * 33
    szX25Address: Char * 201
    szX25Facilities: Char * 201
    szX25UserData: Char * 201
    dwChannels: UInt32
    dwSubEntries: UInt32
    dwDialMode: win32more.Windows.Win32.NetworkManagement.Rras.MPR_INTERFACE_DIAL_MODE
    dwDialExtraPercent: UInt32
    dwDialExtraSampleSeconds: UInt32
    dwHangUpExtraPercent: UInt32
    dwHangUpExtraSampleSeconds: UInt32
    dwIdleDisconnectSeconds: UInt32
    dwType: UInt32
    dwEncryptionType: win32more.Windows.Win32.NetworkManagement.Rras.MPR_ET
    dwCustomAuthKey: UInt32
    dwCustomAuthDataSize: UInt32
    lpbCustomAuthData: POINTER(Byte)
    guidId: Guid
    dwVpnStrategy: win32more.Windows.Win32.NetworkManagement.Rras.MPR_VS
    AddressCount: UInt32
    ipv6addrDns: win32more.Windows.Win32.Networking.WinSock.IN6_ADDR
    ipv6addrDnsAlt: win32more.Windows.Win32.Networking.WinSock.IN6_ADDR
    ipv6addr: POINTER(win32more.Windows.Win32.Networking.WinSock.IN6_ADDR)
MPR_INTERFACE_DIAL_MODE = UInt32
MPRDM_DialFirst: win32more.Windows.Win32.NetworkManagement.Rras.MPR_INTERFACE_DIAL_MODE = 0
MPRDM_DialAll: win32more.Windows.Win32.NetworkManagement.Rras.MPR_INTERFACE_DIAL_MODE = 1
MPRDM_DialAsNeeded: win32more.Windows.Win32.NetworkManagement.Rras.MPR_INTERFACE_DIAL_MODE = 2
class MPR_IPINIP_INTERFACE_0(Structure):
    wszFriendlyName: Char * 257
    Guid: Guid
class MPR_SERVER_0(Structure):
    fLanOnlyMode: win32more.Windows.Win32.Foundation.BOOL
    dwUpTime: UInt32
    dwTotalPorts: UInt32
    dwPortsInUse: UInt32
class MPR_SERVER_1(Structure):
    dwNumPptpPorts: UInt32
    dwPptpPortFlags: UInt32
    dwNumL2tpPorts: UInt32
    dwL2tpPortFlags: UInt32
class MPR_SERVER_2(Structure):
    dwNumPptpPorts: UInt32
    dwPptpPortFlags: UInt32
    dwNumL2tpPorts: UInt32
    dwL2tpPortFlags: UInt32
    dwNumSstpPorts: UInt32
    dwSstpPortFlags: UInt32
class MPR_SERVER_EX0(Structure):
    Header: win32more.Windows.Win32.NetworkManagement.Rras.MPRAPI_OBJECT_HEADER
    fLanOnlyMode: UInt32
    dwUpTime: UInt32
    dwTotalPorts: UInt32
    dwPortsInUse: UInt32
    Reserved: UInt32
    ConfigParams: win32more.Windows.Win32.NetworkManagement.Rras.MPRAPI_TUNNEL_CONFIG_PARAMS0
class MPR_SERVER_EX1(Structure):
    Header: win32more.Windows.Win32.NetworkManagement.Rras.MPRAPI_OBJECT_HEADER
    fLanOnlyMode: UInt32
    dwUpTime: UInt32
    dwTotalPorts: UInt32
    dwPortsInUse: UInt32
    Reserved: UInt32
    ConfigParams: win32more.Windows.Win32.NetworkManagement.Rras.MPRAPI_TUNNEL_CONFIG_PARAMS1
class MPR_SERVER_SET_CONFIG_EX0(Structure):
    Header: win32more.Windows.Win32.NetworkManagement.Rras.MPRAPI_OBJECT_HEADER
    setConfigForProtocols: UInt32
    ConfigParams: win32more.Windows.Win32.NetworkManagement.Rras.MPRAPI_TUNNEL_CONFIG_PARAMS0
class MPR_SERVER_SET_CONFIG_EX1(Structure):
    Header: win32more.Windows.Win32.NetworkManagement.Rras.MPRAPI_OBJECT_HEADER
    setConfigForProtocols: UInt32
    ConfigParams: win32more.Windows.Win32.NetworkManagement.Rras.MPRAPI_TUNNEL_CONFIG_PARAMS1
class MPR_TRANSPORT_0(Structure):
    dwTransportId: UInt32
    hTransport: win32more.Windows.Win32.Foundation.HANDLE
    wszTransportName: Char * 41
class MPR_VPN_TRAFFIC_SELECTOR(Structure):
    type: win32more.Windows.Win32.NetworkManagement.Rras.MPR_VPN_TS_TYPE
    protocolId: Byte
    portStart: UInt16
    portEnd: UInt16
    tsPayloadId: UInt16
    addrStart: win32more.Windows.Win32.NetworkManagement.Rras.VPN_TS_IP_ADDRESS
    addrEnd: win32more.Windows.Win32.NetworkManagement.Rras.VPN_TS_IP_ADDRESS
class MPR_VPN_TRAFFIC_SELECTORS(Structure):
    numTsi: UInt32
    numTsr: UInt32
    tsI: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.MPR_VPN_TRAFFIC_SELECTOR)
    tsR: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.MPR_VPN_TRAFFIC_SELECTOR)
MPR_VPN_TS_TYPE = Int32
MPR_VPN_TS_IPv4_ADDR_RANGE: win32more.Windows.Win32.NetworkManagement.Rras.MPR_VPN_TS_TYPE = 7
MPR_VPN_TS_IPv6_ADDR_RANGE: win32more.Windows.Win32.NetworkManagement.Rras.MPR_VPN_TS_TYPE = 8
MPR_VS = UInt32
MPR_VS_Default: win32more.Windows.Win32.NetworkManagement.Rras.MPR_VS = 0
MPR_VS_PptpOnly: win32more.Windows.Win32.NetworkManagement.Rras.MPR_VS = 1
MPR_VS_PptpFirst: win32more.Windows.Win32.NetworkManagement.Rras.MPR_VS = 2
MPR_VS_L2tpOnly: win32more.Windows.Win32.NetworkManagement.Rras.MPR_VS = 3
MPR_VS_L2tpFirst: win32more.Windows.Win32.NetworkManagement.Rras.MPR_VS = 4
@winfunctype_pointer
def ORASADFUNC(param0: win32more.Windows.Win32.Foundation.HWND, param1: win32more.Windows.Win32.Foundation.PSTR, param2: UInt32, param3: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFNRASFREEBUFFER(pBufer: POINTER(Byte)) -> UInt32: ...
@winfunctype_pointer
def PFNRASGETBUFFER(ppBuffer: POINTER(POINTER(Byte)), pdwSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype_pointer
def PFNRASRECEIVEBUFFER(hPort: win32more.Windows.Win32.Foundation.HANDLE, pBuffer: POINTER(Byte), pdwSize: POINTER(UInt32), dwTimeOut: UInt32, hEvent: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype_pointer
def PFNRASRETRIEVEBUFFER(hPort: win32more.Windows.Win32.Foundation.HANDLE, pBuffer: POINTER(Byte), pdwSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype_pointer
def PFNRASSENDBUFFER(hPort: win32more.Windows.Win32.Foundation.HANDLE, pBuffer: POINTER(Byte), dwSize: UInt32) -> UInt32: ...
@winfunctype_pointer
def PFNRASSETCOMMSETTINGS(hPort: win32more.Windows.Win32.Foundation.HANDLE, pRasCommSettings: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASCOMMSETTINGS), pvReserved: VoidPtr) -> UInt32: ...
@winfunctype_pointer
def PMGM_CREATION_ALERT_CALLBACK(dwSourceAddr: UInt32, dwSourceMask: UInt32, dwGroupAddr: UInt32, dwGroupMask: UInt32, dwInIfIndex: UInt32, dwInIfNextHopAddr: UInt32, dwIfCount: UInt32, pmieOutIfList: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.MGM_IF_ENTRY)) -> UInt32: ...
@winfunctype_pointer
def PMGM_DISABLE_IGMP_CALLBACK(dwIfIndex: UInt32, dwIfNextHopAddr: UInt32) -> UInt32: ...
@winfunctype_pointer
def PMGM_ENABLE_IGMP_CALLBACK(dwIfIndex: UInt32, dwIfNextHopAddr: UInt32) -> UInt32: ...
@winfunctype_pointer
def PMGM_JOIN_ALERT_CALLBACK(dwSourceAddr: UInt32, dwSourceMask: UInt32, dwGroupAddr: UInt32, dwGroupMask: UInt32, bMemberUpdate: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype_pointer
def PMGM_LOCAL_JOIN_CALLBACK(dwSourceAddr: UInt32, dwSourceMask: UInt32, dwGroupAddr: UInt32, dwGroupMask: UInt32, dwIfIndex: UInt32, dwIfNextHopAddr: UInt32) -> UInt32: ...
@winfunctype_pointer
def PMGM_LOCAL_LEAVE_CALLBACK(dwSourceAddr: UInt32, dwSourceMask: UInt32, dwGroupAddr: UInt32, dwGroupMask: UInt32, dwIfIndex: UInt32, dwIfNextHopAddr: UInt32) -> UInt32: ...
@winfunctype_pointer
def PMGM_PRUNE_ALERT_CALLBACK(dwSourceAddr: UInt32, dwSourceMask: UInt32, dwGroupAddr: UInt32, dwGroupMask: UInt32, dwIfIndex: UInt32, dwIfNextHopAddr: UInt32, bMemberDelete: win32more.Windows.Win32.Foundation.BOOL, pdwTimeout: POINTER(UInt32)) -> UInt32: ...
@winfunctype_pointer
def PMGM_RPF_CALLBACK(dwSourceAddr: UInt32, dwSourceMask: UInt32, dwGroupAddr: UInt32, dwGroupMask: UInt32, pdwInIfIndex: POINTER(UInt32), pdwInIfNextHopAddr: POINTER(UInt32), pdwUpStreamNbr: POINTER(UInt32), dwHdrSize: UInt32, pbPacketHdr: POINTER(Byte), pbRoute: POINTER(Byte)) -> UInt32: ...
@winfunctype_pointer
def PMGM_WRONG_IF_CALLBACK(dwSourceAddr: UInt32, dwGroupAddr: UInt32, dwIfIndex: UInt32, dwIfNextHopAddr: UInt32, dwHdrSize: UInt32, pbPacketHdr: POINTER(Byte)) -> UInt32: ...
@winfunctype_pointer
def PMPRADMINACCEPTNEWCONNECTION(param0: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RAS_CONNECTION_0), param1: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RAS_CONNECTION_1)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PMPRADMINACCEPTNEWCONNECTION2(param0: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RAS_CONNECTION_0), param1: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RAS_CONNECTION_1), param2: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RAS_CONNECTION_2)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PMPRADMINACCEPTNEWCONNECTION3(param0: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RAS_CONNECTION_0), param1: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RAS_CONNECTION_1), param2: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RAS_CONNECTION_2), param3: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RAS_CONNECTION_3)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PMPRADMINACCEPTNEWCONNECTIONEX(param0: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RAS_CONNECTION_EX)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PMPRADMINACCEPTNEWLINK(param0: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RAS_PORT_0), param1: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RAS_PORT_1)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PMPRADMINACCEPTREAUTHENTICATION(param0: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RAS_CONNECTION_0), param1: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RAS_CONNECTION_1), param2: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RAS_CONNECTION_2), param3: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RAS_CONNECTION_3)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PMPRADMINACCEPTREAUTHENTICATIONEX(param0: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RAS_CONNECTION_EX)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PMPRADMINACCEPTTUNNELENDPOINTCHANGEEX(param0: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RAS_CONNECTION_EX)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PMPRADMINCONNECTIONHANGUPNOTIFICATION(param0: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RAS_CONNECTION_0), param1: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RAS_CONNECTION_1)) -> Void: ...
@winfunctype_pointer
def PMPRADMINCONNECTIONHANGUPNOTIFICATION2(param0: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RAS_CONNECTION_0), param1: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RAS_CONNECTION_1), param2: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RAS_CONNECTION_2)) -> Void: ...
@winfunctype_pointer
def PMPRADMINCONNECTIONHANGUPNOTIFICATION3(param0: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RAS_CONNECTION_0), param1: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RAS_CONNECTION_1), param2: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RAS_CONNECTION_2), param3: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RAS_CONNECTION_3)) -> Void: ...
@winfunctype_pointer
def PMPRADMINCONNECTIONHANGUPNOTIFICATIONEX(param0: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RAS_CONNECTION_EX)) -> Void: ...
@winfunctype_pointer
def PMPRADMINGETIPADDRESSFORUSER(param0: win32more.Windows.Win32.Foundation.PWSTR, param1: win32more.Windows.Win32.Foundation.PWSTR, param2: POINTER(UInt32), param3: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> UInt32: ...
@winfunctype_pointer
def PMPRADMINGETIPV6ADDRESSFORUSER(param0: win32more.Windows.Win32.Foundation.PWSTR, param1: win32more.Windows.Win32.Foundation.PWSTR, param2: POINTER(win32more.Windows.Win32.Networking.WinSock.IN6_ADDR), param3: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> UInt32: ...
@winfunctype_pointer
def PMPRADMINLINKHANGUPNOTIFICATION(param0: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RAS_PORT_0), param1: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RAS_PORT_1)) -> Void: ...
@winfunctype_pointer
def PMPRADMINRASVALIDATEPREAUTHENTICATEDCONNECTIONEX(param0: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.AUTH_VALIDATION_EX)) -> UInt32: ...
@winfunctype_pointer
def PMPRADMINRELEASEIPADRESS(param0: win32more.Windows.Win32.Foundation.PWSTR, param1: win32more.Windows.Win32.Foundation.PWSTR, param2: POINTER(UInt32)) -> Void: ...
@winfunctype_pointer
def PMPRADMINRELEASEIPV6ADDRESSFORUSER(param0: win32more.Windows.Win32.Foundation.PWSTR, param1: win32more.Windows.Win32.Foundation.PWSTR, param2: POINTER(win32more.Windows.Win32.Networking.WinSock.IN6_ADDR)) -> Void: ...
@winfunctype_pointer
def PMPRADMINTERMINATEDLL() -> UInt32: ...
class PPP_ATCP_INFO(Structure):
    dwError: UInt32
    wszAddress: Char * 33
class PPP_CCP_INFO(Structure):
    dwError: UInt32
    dwCompressionAlgorithm: UInt32
    dwOptions: UInt32
    dwRemoteCompressionAlgorithm: UInt32
    dwRemoteOptions: UInt32
class PPP_INFO(Structure):
    nbf: win32more.Windows.Win32.NetworkManagement.Rras.PPP_NBFCP_INFO
    ip: win32more.Windows.Win32.NetworkManagement.Rras.PPP_IPCP_INFO
    ipx: win32more.Windows.Win32.NetworkManagement.Rras.PPP_IPXCP_INFO
    at: win32more.Windows.Win32.NetworkManagement.Rras.PPP_ATCP_INFO
class PPP_INFO_2(Structure):
    nbf: win32more.Windows.Win32.NetworkManagement.Rras.PPP_NBFCP_INFO
    ip: win32more.Windows.Win32.NetworkManagement.Rras.PPP_IPCP_INFO2
    ipx: win32more.Windows.Win32.NetworkManagement.Rras.PPP_IPXCP_INFO
    at: win32more.Windows.Win32.NetworkManagement.Rras.PPP_ATCP_INFO
    ccp: win32more.Windows.Win32.NetworkManagement.Rras.PPP_CCP_INFO
    lcp: win32more.Windows.Win32.NetworkManagement.Rras.PPP_LCP_INFO
class PPP_INFO_3(Structure):
    nbf: win32more.Windows.Win32.NetworkManagement.Rras.PPP_NBFCP_INFO
    ip: win32more.Windows.Win32.NetworkManagement.Rras.PPP_IPCP_INFO2
    ipv6: win32more.Windows.Win32.NetworkManagement.Rras.PPP_IPV6_CP_INFO
    ccp: win32more.Windows.Win32.NetworkManagement.Rras.PPP_CCP_INFO
    lcp: win32more.Windows.Win32.NetworkManagement.Rras.PPP_LCP_INFO
class PPP_IPCP_INFO(Structure):
    dwError: UInt32
    wszAddress: Char * 16
    wszRemoteAddress: Char * 16
class PPP_IPCP_INFO2(Structure):
    dwError: UInt32
    wszAddress: Char * 16
    wszRemoteAddress: Char * 16
    dwOptions: UInt32
    dwRemoteOptions: UInt32
class PPP_IPV6_CP_INFO(Structure):
    dwVersion: UInt32
    dwSize: UInt32
    dwError: UInt32
    bInterfaceIdentifier: Byte * 8
    bRemoteInterfaceIdentifier: Byte * 8
    dwOptions: UInt32
    dwRemoteOptions: UInt32
    bPrefix: Byte * 8
    dwPrefixLength: UInt32
class PPP_IPXCP_INFO(Structure):
    dwError: UInt32
    wszAddress: Char * 23
PPP_LCP = UInt32
PPP_LCP_PAP: win32more.Windows.Win32.NetworkManagement.Rras.PPP_LCP = 49187
PPP_LCP_CHAP: win32more.Windows.Win32.NetworkManagement.Rras.PPP_LCP = 49699
PPP_LCP_EAP: win32more.Windows.Win32.NetworkManagement.Rras.PPP_LCP = 49703
PPP_LCP_SPAP: win32more.Windows.Win32.NetworkManagement.Rras.PPP_LCP = 49191
class PPP_LCP_INFO(Structure):
    dwError: UInt32
    dwAuthenticationProtocol: win32more.Windows.Win32.NetworkManagement.Rras.PPP_LCP
    dwAuthenticationData: win32more.Windows.Win32.NetworkManagement.Rras.PPP_LCP_INFO_AUTH_DATA
    dwRemoteAuthenticationProtocol: UInt32
    dwRemoteAuthenticationData: UInt32
    dwTerminateReason: UInt32
    dwRemoteTerminateReason: UInt32
    dwOptions: UInt32
    dwRemoteOptions: UInt32
    dwEapTypeId: UInt32
    dwRemoteEapTypeId: UInt32
PPP_LCP_INFO_AUTH_DATA = UInt32
PPP_LCP_CHAP_MD5: win32more.Windows.Win32.NetworkManagement.Rras.PPP_LCP_INFO_AUTH_DATA = 5
PPP_LCP_CHAP_MS: win32more.Windows.Win32.NetworkManagement.Rras.PPP_LCP_INFO_AUTH_DATA = 128
PPP_LCP_CHAP_MSV2: win32more.Windows.Win32.NetworkManagement.Rras.PPP_LCP_INFO_AUTH_DATA = 129
class PPP_NBFCP_INFO(Structure):
    dwError: UInt32
    wszWksta: Char * 17
class PPP_PROJECTION_INFO(Structure):
    dwIPv4NegotiationError: UInt32
    wszAddress: Char * 16
    wszRemoteAddress: Char * 16
    dwIPv4Options: UInt32
    dwIPv4RemoteOptions: UInt32
    IPv4SubInterfaceIndex: UInt64
    dwIPv6NegotiationError: UInt32
    bInterfaceIdentifier: Byte * 8
    bRemoteInterfaceIdentifier: Byte * 8
    bPrefix: Byte * 8
    dwPrefixLength: UInt32
    IPv6SubInterfaceIndex: UInt64
    dwLcpError: UInt32
    dwAuthenticationProtocol: win32more.Windows.Win32.NetworkManagement.Rras.PPP_LCP
    dwAuthenticationData: win32more.Windows.Win32.NetworkManagement.Rras.PPP_LCP_INFO_AUTH_DATA
    dwRemoteAuthenticationProtocol: win32more.Windows.Win32.NetworkManagement.Rras.PPP_LCP
    dwRemoteAuthenticationData: win32more.Windows.Win32.NetworkManagement.Rras.PPP_LCP_INFO_AUTH_DATA
    dwLcpTerminateReason: UInt32
    dwLcpRemoteTerminateReason: UInt32
    dwLcpOptions: UInt32
    dwLcpRemoteOptions: UInt32
    dwEapTypeId: UInt32
    dwRemoteEapTypeId: UInt32
    dwCcpError: UInt32
    dwCompressionAlgorithm: UInt32
    dwCcpOptions: UInt32
    dwRemoteCompressionAlgorithm: UInt32
    dwCcpRemoteOptions: UInt32
class PPP_PROJECTION_INFO2(Structure):
    dwIPv4NegotiationError: UInt32
    wszAddress: Char * 16
    wszRemoteAddress: Char * 16
    dwIPv4Options: UInt32
    dwIPv4RemoteOptions: UInt32
    IPv4SubInterfaceIndex: UInt64
    dwIPv6NegotiationError: UInt32
    bInterfaceIdentifier: Byte * 8
    bRemoteInterfaceIdentifier: Byte * 8
    bPrefix: Byte * 8
    dwPrefixLength: UInt32
    IPv6SubInterfaceIndex: UInt64
    dwLcpError: UInt32
    dwAuthenticationProtocol: win32more.Windows.Win32.NetworkManagement.Rras.PPP_LCP
    dwAuthenticationData: win32more.Windows.Win32.NetworkManagement.Rras.PPP_LCP_INFO_AUTH_DATA
    dwRemoteAuthenticationProtocol: win32more.Windows.Win32.NetworkManagement.Rras.PPP_LCP
    dwRemoteAuthenticationData: win32more.Windows.Win32.NetworkManagement.Rras.PPP_LCP_INFO_AUTH_DATA
    dwLcpTerminateReason: UInt32
    dwLcpRemoteTerminateReason: UInt32
    dwLcpOptions: UInt32
    dwLcpRemoteOptions: UInt32
    dwEapTypeId: UInt32
    dwEmbeddedEAPTypeId: UInt32
    dwRemoteEapTypeId: UInt32
    dwCcpError: UInt32
    dwCompressionAlgorithm: UInt32
    dwCcpOptions: UInt32
    dwRemoteCompressionAlgorithm: UInt32
    dwCcpRemoteOptions: UInt32
class PPTP_CONFIG_PARAMS(Structure):
    dwNumPorts: UInt32
    dwPortFlags: UInt32
class PROJECTION_INFO(Structure):
    projectionInfoType: Byte
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        PppProjectionInfo: win32more.Windows.Win32.NetworkManagement.Rras.PPP_PROJECTION_INFO
        Ikev2ProjectionInfo: win32more.Windows.Win32.NetworkManagement.Rras.IKEV2_PROJECTION_INFO
class PROJECTION_INFO2(Structure):
    projectionInfoType: Byte
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        PppProjectionInfo: win32more.Windows.Win32.NetworkManagement.Rras.PPP_PROJECTION_INFO2
        Ikev2ProjectionInfo: win32more.Windows.Win32.NetworkManagement.Rras.IKEV2_PROJECTION_INFO2
@winfunctype_pointer
def RASADFUNCA(param0: win32more.Windows.Win32.Foundation.PSTR, param1: win32more.Windows.Win32.Foundation.PSTR, param2: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASADPARAMS), param3: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def RASADFUNCW(param0: win32more.Windows.Win32.Foundation.PWSTR, param1: win32more.Windows.Win32.Foundation.PWSTR, param2: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASADPARAMS), param3: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
RASADFUNC = UnicodeAlias('RASADFUNCW')
class RASADPARAMS(Structure):
    dwSize: UInt32
    hwndOwner: win32more.Windows.Win32.Foundation.HWND
    dwFlags: UInt32
    xDlg: Int32
    yDlg: Int32
    _pack_ = 4
class RASAMBA(Structure):
    dwSize: UInt32
    dwError: UInt32
    szNetBiosError: win32more.Windows.Win32.Foundation.CHAR * 17
    bLana: Byte
class RASAMBW(Structure):
    dwSize: UInt32
    dwError: UInt32
    szNetBiosError: Char * 17
    bLana: Byte
RASAMB = UnicodeAlias('RASAMBW')
RASAPIVERSION = Int32
RASAPIVERSION_500: win32more.Windows.Win32.NetworkManagement.Rras.RASAPIVERSION = 1
RASAPIVERSION_501: win32more.Windows.Win32.NetworkManagement.Rras.RASAPIVERSION = 2
RASAPIVERSION_600: win32more.Windows.Win32.NetworkManagement.Rras.RASAPIVERSION = 3
RASAPIVERSION_601: win32more.Windows.Win32.NetworkManagement.Rras.RASAPIVERSION = 4
class RASAUTODIALENTRYA(Structure):
    dwSize: UInt32
    dwFlags: UInt32
    dwDialingLocation: UInt32
    szEntry: win32more.Windows.Win32.Foundation.CHAR * 257
class RASAUTODIALENTRYW(Structure):
    dwSize: UInt32
    dwFlags: UInt32
    dwDialingLocation: UInt32
    szEntry: Char * 257
RASAUTODIALENTRY = UnicodeAlias('RASAUTODIALENTRYW')
class RASCOMMSETTINGS(Structure):
    dwSize: UInt32
    bParity: Byte
    bStop: Byte
    bByteSize: Byte
    bAlign: Byte
if ARCH in 'X64,ARM64':
    class RASCONNA(Structure):
        dwSize: UInt32
        hrasconn: win32more.Windows.Win32.NetworkManagement.Rras.HRASCONN
        szEntryName: win32more.Windows.Win32.Foundation.CHAR * 257
        szDeviceType: win32more.Windows.Win32.Foundation.CHAR * 17
        szDeviceName: win32more.Windows.Win32.Foundation.CHAR * 129
        szPhonebook: win32more.Windows.Win32.Foundation.CHAR * 260
        dwSubEntry: UInt32
        guidEntry: Guid
        dwFlags: UInt32
        luid: win32more.Windows.Win32.Foundation.LUID
        guidCorrelationId: Guid
        _pack_ = 4
elif ARCH in 'X86':
    class RASCONNA(Structure):
        dwSize: UInt32
        hrasconn: win32more.Windows.Win32.NetworkManagement.Rras.HRASCONN
        szEntryName: win32more.Windows.Win32.Foundation.CHAR * 257
        szDeviceType: win32more.Windows.Win32.Foundation.CHAR * 17
        szDeviceName: win32more.Windows.Win32.Foundation.CHAR * 129
        szPhonebook: win32more.Windows.Win32.Foundation.CHAR * 260
        dwSubEntry: UInt32
        guidEntry: Guid
        dwFlags: UInt32
        luid: win32more.Windows.Win32.Foundation.LUID
        guidCorrelationId: Guid
RASCONNSTATE = Int32
RASCS_OpenPort: win32more.Windows.Win32.NetworkManagement.Rras.RASCONNSTATE = 0
RASCS_PortOpened: win32more.Windows.Win32.NetworkManagement.Rras.RASCONNSTATE = 1
RASCS_ConnectDevice: win32more.Windows.Win32.NetworkManagement.Rras.RASCONNSTATE = 2
RASCS_DeviceConnected: win32more.Windows.Win32.NetworkManagement.Rras.RASCONNSTATE = 3
RASCS_AllDevicesConnected: win32more.Windows.Win32.NetworkManagement.Rras.RASCONNSTATE = 4
RASCS_Authenticate: win32more.Windows.Win32.NetworkManagement.Rras.RASCONNSTATE = 5
RASCS_AuthNotify: win32more.Windows.Win32.NetworkManagement.Rras.RASCONNSTATE = 6
RASCS_AuthRetry: win32more.Windows.Win32.NetworkManagement.Rras.RASCONNSTATE = 7
RASCS_AuthCallback: win32more.Windows.Win32.NetworkManagement.Rras.RASCONNSTATE = 8
RASCS_AuthChangePassword: win32more.Windows.Win32.NetworkManagement.Rras.RASCONNSTATE = 9
RASCS_AuthProject: win32more.Windows.Win32.NetworkManagement.Rras.RASCONNSTATE = 10
RASCS_AuthLinkSpeed: win32more.Windows.Win32.NetworkManagement.Rras.RASCONNSTATE = 11
RASCS_AuthAck: win32more.Windows.Win32.NetworkManagement.Rras.RASCONNSTATE = 12
RASCS_ReAuthenticate: win32more.Windows.Win32.NetworkManagement.Rras.RASCONNSTATE = 13
RASCS_Authenticated: win32more.Windows.Win32.NetworkManagement.Rras.RASCONNSTATE = 14
RASCS_PrepareForCallback: win32more.Windows.Win32.NetworkManagement.Rras.RASCONNSTATE = 15
RASCS_WaitForModemReset: win32more.Windows.Win32.NetworkManagement.Rras.RASCONNSTATE = 16
RASCS_WaitForCallback: win32more.Windows.Win32.NetworkManagement.Rras.RASCONNSTATE = 17
RASCS_Projected: win32more.Windows.Win32.NetworkManagement.Rras.RASCONNSTATE = 18
RASCS_StartAuthentication: win32more.Windows.Win32.NetworkManagement.Rras.RASCONNSTATE = 19
RASCS_CallbackComplete: win32more.Windows.Win32.NetworkManagement.Rras.RASCONNSTATE = 20
RASCS_LogonNetwork: win32more.Windows.Win32.NetworkManagement.Rras.RASCONNSTATE = 21
RASCS_SubEntryConnected: win32more.Windows.Win32.NetworkManagement.Rras.RASCONNSTATE = 22
RASCS_SubEntryDisconnected: win32more.Windows.Win32.NetworkManagement.Rras.RASCONNSTATE = 23
RASCS_ApplySettings: win32more.Windows.Win32.NetworkManagement.Rras.RASCONNSTATE = 24
RASCS_Interactive: win32more.Windows.Win32.NetworkManagement.Rras.RASCONNSTATE = 4096
RASCS_RetryAuthentication: win32more.Windows.Win32.NetworkManagement.Rras.RASCONNSTATE = 4097
RASCS_CallbackSetByCaller: win32more.Windows.Win32.NetworkManagement.Rras.RASCONNSTATE = 4098
RASCS_PasswordExpired: win32more.Windows.Win32.NetworkManagement.Rras.RASCONNSTATE = 4099
RASCS_InvokeEapUI: win32more.Windows.Win32.NetworkManagement.Rras.RASCONNSTATE = 4100
RASCS_Connected: win32more.Windows.Win32.NetworkManagement.Rras.RASCONNSTATE = 8192
RASCS_Disconnected: win32more.Windows.Win32.NetworkManagement.Rras.RASCONNSTATE = 8193
class RASCONNSTATUSA(Structure):
    dwSize: UInt32
    rasconnstate: win32more.Windows.Win32.NetworkManagement.Rras.RASCONNSTATE
    dwError: UInt32
    szDeviceType: win32more.Windows.Win32.Foundation.CHAR * 17
    szDeviceName: win32more.Windows.Win32.Foundation.CHAR * 129
    szPhoneNumber: win32more.Windows.Win32.Foundation.CHAR * 129
    localEndPoint: win32more.Windows.Win32.NetworkManagement.Rras.RASTUNNELENDPOINT
    remoteEndPoint: win32more.Windows.Win32.NetworkManagement.Rras.RASTUNNELENDPOINT
    rasconnsubstate: win32more.Windows.Win32.NetworkManagement.Rras.RASCONNSUBSTATE
class RASCONNSTATUSW(Structure):
    dwSize: UInt32
    rasconnstate: win32more.Windows.Win32.NetworkManagement.Rras.RASCONNSTATE
    dwError: UInt32
    szDeviceType: Char * 17
    szDeviceName: Char * 129
    szPhoneNumber: Char * 129
    localEndPoint: win32more.Windows.Win32.NetworkManagement.Rras.RASTUNNELENDPOINT
    remoteEndPoint: win32more.Windows.Win32.NetworkManagement.Rras.RASTUNNELENDPOINT
    rasconnsubstate: win32more.Windows.Win32.NetworkManagement.Rras.RASCONNSUBSTATE
RASCONNSTATUS = UnicodeAlias('RASCONNSTATUSW')
RASCONNSUBSTATE = Int32
RASCSS_None: win32more.Windows.Win32.NetworkManagement.Rras.RASCONNSUBSTATE = 0
RASCSS_Dormant: win32more.Windows.Win32.NetworkManagement.Rras.RASCONNSUBSTATE = 1
RASCSS_Reconnecting: win32more.Windows.Win32.NetworkManagement.Rras.RASCONNSUBSTATE = 2
RASCSS_Reconnected: win32more.Windows.Win32.NetworkManagement.Rras.RASCONNSUBSTATE = 8192
if ARCH in 'X64,ARM64':
    class RASCONNW(Structure):
        dwSize: UInt32
        hrasconn: win32more.Windows.Win32.NetworkManagement.Rras.HRASCONN
        szEntryName: Char * 257
        szDeviceType: Char * 17
        szDeviceName: Char * 129
        szPhonebook: Char * 260
        dwSubEntry: UInt32
        guidEntry: Guid
        dwFlags: UInt32
        luid: win32more.Windows.Win32.Foundation.LUID
        guidCorrelationId: Guid
        _pack_ = 4
elif ARCH in 'X86':
    class RASCONNW(Structure):
        dwSize: UInt32
        hrasconn: win32more.Windows.Win32.NetworkManagement.Rras.HRASCONN
        szEntryName: Char * 257
        szDeviceType: Char * 17
        szDeviceName: Char * 129
        szPhonebook: Char * 260
        dwSubEntry: UInt32
        guidEntry: Guid
        dwFlags: UInt32
        luid: win32more.Windows.Win32.Foundation.LUID
        guidCorrelationId: Guid
if ARCH in 'X64,ARM64':
    RASCONN = UnicodeAlias('RASCONNW')
elif ARCH in 'X86':
    RASCONN = UnicodeAlias('RASCONNW')
class RASCREDENTIALSA(Structure):
    dwSize: UInt32
    dwMask: UInt32
    szUserName: win32more.Windows.Win32.Foundation.CHAR * 257
    szPassword: win32more.Windows.Win32.Foundation.CHAR * 257
    szDomain: win32more.Windows.Win32.Foundation.CHAR * 16
class RASCREDENTIALSW(Structure):
    dwSize: UInt32
    dwMask: UInt32
    szUserName: Char * 257
    szPassword: Char * 257
    szDomain: Char * 16
RASCREDENTIALS = UnicodeAlias('RASCREDENTIALSW')
class RASCTRYINFO(Structure):
    dwSize: UInt32
    dwCountryID: UInt32
    dwNextCountryID: UInt32
    dwCountryCode: UInt32
    dwCountryNameOffset: UInt32
class RASCUSTOMSCRIPTEXTENSIONS(Structure):
    dwSize: UInt32
    pfnRasSetCommSettings: win32more.Windows.Win32.NetworkManagement.Rras.PFNRASSETCOMMSETTINGS
    _pack_ = 4
class RASDEVINFOA(Structure):
    dwSize: UInt32
    szDeviceType: win32more.Windows.Win32.Foundation.CHAR * 17
    szDeviceName: win32more.Windows.Win32.Foundation.CHAR * 129
class RASDEVINFOW(Structure):
    dwSize: UInt32
    szDeviceType: Char * 17
    szDeviceName: Char * 129
RASDEVINFO = UnicodeAlias('RASDEVINFOW')
if ARCH in 'X64,ARM64':
    class RASDEVSPECIFICINFO(Structure):
        dwSize: UInt32
        pbDevSpecificInfo: POINTER(Byte)
        _pack_ = 4
elif ARCH in 'X86':
    class RASDEVSPECIFICINFO(Structure):
        dwSize: UInt32
        pbDevSpecificInfo: POINTER(Byte)
class RASDIALDLG(Structure):
    dwSize: UInt32
    hwndOwner: win32more.Windows.Win32.Foundation.HWND
    dwFlags: UInt32
    xDlg: Int32
    yDlg: Int32
    dwSubEntry: UInt32
    dwError: UInt32
    reserved: UIntPtr
    reserved2: UIntPtr
    _pack_ = 4
class RASDIALEXTENSIONS(Structure):
    dwSize: UInt32
    dwfOptions: UInt32
    hwndParent: win32more.Windows.Win32.Foundation.HWND
    reserved: UIntPtr
    reserved1: UIntPtr
    RasEapInfo: win32more.Windows.Win32.NetworkManagement.Rras.RASEAPINFO
    fSkipPppAuth: win32more.Windows.Win32.Foundation.BOOL
    RasDevSpecificInfo: win32more.Windows.Win32.NetworkManagement.Rras.RASDEVSPECIFICINFO
    _pack_ = 4
@winfunctype_pointer
def RASDIALFUNC(param0: UInt32, param1: win32more.Windows.Win32.NetworkManagement.Rras.RASCONNSTATE, param2: UInt32) -> Void: ...
@winfunctype_pointer
def RASDIALFUNC1(param0: win32more.Windows.Win32.NetworkManagement.Rras.HRASCONN, param1: UInt32, param2: win32more.Windows.Win32.NetworkManagement.Rras.RASCONNSTATE, param3: UInt32, param4: UInt32) -> Void: ...
@winfunctype_pointer
def RASDIALFUNC2(param0: UIntPtr, param1: UInt32, param2: win32more.Windows.Win32.NetworkManagement.Rras.HRASCONN, param3: UInt32, param4: win32more.Windows.Win32.NetworkManagement.Rras.RASCONNSTATE, param5: UInt32, param6: UInt32) -> UInt32: ...
if ARCH in 'X64,ARM64':
    class RASDIALPARAMSA(Structure):
        dwSize: UInt32
        szEntryName: win32more.Windows.Win32.Foundation.CHAR * 257
        szPhoneNumber: win32more.Windows.Win32.Foundation.CHAR * 129
        szCallbackNumber: win32more.Windows.Win32.Foundation.CHAR * 129
        szUserName: win32more.Windows.Win32.Foundation.CHAR * 257
        szPassword: win32more.Windows.Win32.Foundation.CHAR * 257
        szDomain: win32more.Windows.Win32.Foundation.CHAR * 16
        dwSubEntry: UInt32
        dwCallbackId: UIntPtr
        dwIfIndex: UInt32
        szEncPassword: win32more.Windows.Win32.Foundation.PSTR
        _pack_ = 4
elif ARCH in 'X86':
    class RASDIALPARAMSA(Structure):
        dwSize: UInt32
        szEntryName: win32more.Windows.Win32.Foundation.CHAR * 257
        szPhoneNumber: win32more.Windows.Win32.Foundation.CHAR * 129
        szCallbackNumber: win32more.Windows.Win32.Foundation.CHAR * 129
        szUserName: win32more.Windows.Win32.Foundation.CHAR * 257
        szPassword: win32more.Windows.Win32.Foundation.CHAR * 257
        szDomain: win32more.Windows.Win32.Foundation.CHAR * 16
        dwSubEntry: UInt32
        dwCallbackId: UIntPtr
        dwIfIndex: UInt32
        szEncPassword: win32more.Windows.Win32.Foundation.PSTR
if ARCH in 'X64,ARM64':
    class RASDIALPARAMSW(Structure):
        dwSize: UInt32
        szEntryName: Char * 257
        szPhoneNumber: Char * 129
        szCallbackNumber: Char * 129
        szUserName: Char * 257
        szPassword: Char * 257
        szDomain: Char * 16
        dwSubEntry: UInt32
        dwCallbackId: UIntPtr
        dwIfIndex: UInt32
        szEncPassword: win32more.Windows.Win32.Foundation.PWSTR
        _pack_ = 4
elif ARCH in 'X86':
    class RASDIALPARAMSW(Structure):
        dwSize: UInt32
        szEntryName: Char * 257
        szPhoneNumber: Char * 129
        szCallbackNumber: Char * 129
        szUserName: Char * 257
        szPassword: Char * 257
        szDomain: Char * 16
        dwSubEntry: UInt32
        dwCallbackId: UIntPtr
        dwIfIndex: UInt32
        szEncPassword: win32more.Windows.Win32.Foundation.PWSTR
if ARCH in 'X64,ARM64':
    RASDIALPARAMS = UnicodeAlias('RASDIALPARAMSW')
elif ARCH in 'X86':
    RASDIALPARAMS = UnicodeAlias('RASDIALPARAMSW')
class RASEAPINFO(Structure):
    dwSizeofEapInfo: UInt32
    pbEapInfo: POINTER(Byte)
    _pack_ = 4
class RASEAPUSERIDENTITYA(Structure):
    szUserName: win32more.Windows.Win32.Foundation.CHAR * 257
    dwSizeofEapInfo: UInt32
    pbEapInfo: Byte * 1
class RASEAPUSERIDENTITYW(Structure):
    szUserName: Char * 257
    dwSizeofEapInfo: UInt32
    pbEapInfo: Byte * 1
RASEAPUSERIDENTITY = UnicodeAlias('RASEAPUSERIDENTITYW')
class RASENTRYA(Structure):
    dwSize: UInt32
    dwfOptions: UInt32
    dwCountryID: UInt32
    dwCountryCode: UInt32
    szAreaCode: win32more.Windows.Win32.Foundation.CHAR * 11
    szLocalPhoneNumber: win32more.Windows.Win32.Foundation.CHAR * 129
    dwAlternateOffset: UInt32
    ipaddr: win32more.Windows.Win32.NetworkManagement.Rras.RASIPADDR
    ipaddrDns: win32more.Windows.Win32.NetworkManagement.Rras.RASIPADDR
    ipaddrDnsAlt: win32more.Windows.Win32.NetworkManagement.Rras.RASIPADDR
    ipaddrWins: win32more.Windows.Win32.NetworkManagement.Rras.RASIPADDR
    ipaddrWinsAlt: win32more.Windows.Win32.NetworkManagement.Rras.RASIPADDR
    dwFrameSize: UInt32
    dwfNetProtocols: UInt32
    dwFramingProtocol: UInt32
    szScript: win32more.Windows.Win32.Foundation.CHAR * 260
    szAutodialDll: win32more.Windows.Win32.Foundation.CHAR * 260
    szAutodialFunc: win32more.Windows.Win32.Foundation.CHAR * 260
    szDeviceType: win32more.Windows.Win32.Foundation.CHAR * 17
    szDeviceName: win32more.Windows.Win32.Foundation.CHAR * 129
    szX25PadType: win32more.Windows.Win32.Foundation.CHAR * 33
    szX25Address: win32more.Windows.Win32.Foundation.CHAR * 201
    szX25Facilities: win32more.Windows.Win32.Foundation.CHAR * 201
    szX25UserData: win32more.Windows.Win32.Foundation.CHAR * 201
    dwChannels: UInt32
    dwReserved1: UInt32
    dwReserved2: UInt32
    dwSubEntries: UInt32
    dwDialMode: win32more.Windows.Win32.NetworkManagement.Rras.RASENTRY_DIAL_MODE
    dwDialExtraPercent: UInt32
    dwDialExtraSampleSeconds: UInt32
    dwHangUpExtraPercent: UInt32
    dwHangUpExtraSampleSeconds: UInt32
    dwIdleDisconnectSeconds: UInt32
    dwType: UInt32
    dwEncryptionType: UInt32
    dwCustomAuthKey: UInt32
    guidId: Guid
    szCustomDialDll: win32more.Windows.Win32.Foundation.CHAR * 260
    dwVpnStrategy: UInt32
    dwfOptions2: UInt32
    dwfOptions3: UInt32
    szDnsSuffix: win32more.Windows.Win32.Foundation.CHAR * 256
    dwTcpWindowSize: UInt32
    szPrerequisitePbk: win32more.Windows.Win32.Foundation.CHAR * 260
    szPrerequisiteEntry: win32more.Windows.Win32.Foundation.CHAR * 257
    dwRedialCount: UInt32
    dwRedialPause: UInt32
    ipv6addrDns: win32more.Windows.Win32.Networking.WinSock.IN6_ADDR
    ipv6addrDnsAlt: win32more.Windows.Win32.Networking.WinSock.IN6_ADDR
    dwIPv4InterfaceMetric: UInt32
    dwIPv6InterfaceMetric: UInt32
    ipv6addr: win32more.Windows.Win32.Networking.WinSock.IN6_ADDR
    dwIPv6PrefixLength: UInt32
    dwNetworkOutageTime: UInt32
    szIDi: win32more.Windows.Win32.Foundation.CHAR * 257
    szIDr: win32more.Windows.Win32.Foundation.CHAR * 257
    fIsImsConfig: win32more.Windows.Win32.Foundation.BOOL
    IdiType: win32more.Windows.Win32.NetworkManagement.Rras.IKEV2_ID_PAYLOAD_TYPE
    IdrType: win32more.Windows.Win32.NetworkManagement.Rras.IKEV2_ID_PAYLOAD_TYPE
    fDisableIKEv2Fragmentation: win32more.Windows.Win32.Foundation.BOOL
if ARCH in 'X64,ARM64':
    class RASENTRYDLGA(Structure):
        dwSize: UInt32
        hwndOwner: win32more.Windows.Win32.Foundation.HWND
        dwFlags: UInt32
        xDlg: Int32
        yDlg: Int32
        szEntry: win32more.Windows.Win32.Foundation.CHAR * 257
        dwError: UInt32
        reserved: UIntPtr
        reserved2: UIntPtr
        _pack_ = 4
elif ARCH in 'X86':
    class RASENTRYDLGA(Structure):
        dwSize: UInt32
        hwndOwner: win32more.Windows.Win32.Foundation.HWND
        dwFlags: UInt32
        xDlg: Int32
        yDlg: Int32
        szEntry: win32more.Windows.Win32.Foundation.CHAR * 257
        dwError: UInt32
        reserved: UIntPtr
        reserved2: UIntPtr
if ARCH in 'X64,ARM64':
    class RASENTRYDLGW(Structure):
        dwSize: UInt32
        hwndOwner: win32more.Windows.Win32.Foundation.HWND
        dwFlags: UInt32
        xDlg: Int32
        yDlg: Int32
        szEntry: Char * 257
        dwError: UInt32
        reserved: UIntPtr
        reserved2: UIntPtr
        _pack_ = 4
elif ARCH in 'X86':
    class RASENTRYDLGW(Structure):
        dwSize: UInt32
        hwndOwner: win32more.Windows.Win32.Foundation.HWND
        dwFlags: UInt32
        xDlg: Int32
        yDlg: Int32
        szEntry: Char * 257
        dwError: UInt32
        reserved: UIntPtr
        reserved2: UIntPtr
if ARCH in 'X64,ARM64':
    RASENTRYDLG = UnicodeAlias('RASENTRYDLGW')
elif ARCH in 'X86':
    RASENTRYDLG = UnicodeAlias('RASENTRYDLGW')
class RASENTRYNAMEA(Structure):
    dwSize: UInt32
    szEntryName: win32more.Windows.Win32.Foundation.CHAR * 257
    dwFlags: UInt32
    szPhonebookPath: win32more.Windows.Win32.Foundation.CHAR * 261
class RASENTRYNAMEW(Structure):
    dwSize: UInt32
    szEntryName: Char * 257
    dwFlags: UInt32
    szPhonebookPath: Char * 261
RASENTRYNAME = UnicodeAlias('RASENTRYNAMEW')
class RASENTRYW(Structure):
    dwSize: UInt32
    dwfOptions: UInt32
    dwCountryID: UInt32
    dwCountryCode: UInt32
    szAreaCode: Char * 11
    szLocalPhoneNumber: Char * 129
    dwAlternateOffset: UInt32
    ipaddr: win32more.Windows.Win32.NetworkManagement.Rras.RASIPADDR
    ipaddrDns: win32more.Windows.Win32.NetworkManagement.Rras.RASIPADDR
    ipaddrDnsAlt: win32more.Windows.Win32.NetworkManagement.Rras.RASIPADDR
    ipaddrWins: win32more.Windows.Win32.NetworkManagement.Rras.RASIPADDR
    ipaddrWinsAlt: win32more.Windows.Win32.NetworkManagement.Rras.RASIPADDR
    dwFrameSize: UInt32
    dwfNetProtocols: UInt32
    dwFramingProtocol: UInt32
    szScript: Char * 260
    szAutodialDll: Char * 260
    szAutodialFunc: Char * 260
    szDeviceType: Char * 17
    szDeviceName: Char * 129
    szX25PadType: Char * 33
    szX25Address: Char * 201
    szX25Facilities: Char * 201
    szX25UserData: Char * 201
    dwChannels: UInt32
    dwReserved1: UInt32
    dwReserved2: UInt32
    dwSubEntries: UInt32
    dwDialMode: win32more.Windows.Win32.NetworkManagement.Rras.RASENTRY_DIAL_MODE
    dwDialExtraPercent: UInt32
    dwDialExtraSampleSeconds: UInt32
    dwHangUpExtraPercent: UInt32
    dwHangUpExtraSampleSeconds: UInt32
    dwIdleDisconnectSeconds: UInt32
    dwType: UInt32
    dwEncryptionType: UInt32
    dwCustomAuthKey: UInt32
    guidId: Guid
    szCustomDialDll: Char * 260
    dwVpnStrategy: UInt32
    dwfOptions2: UInt32
    dwfOptions3: UInt32
    szDnsSuffix: Char * 256
    dwTcpWindowSize: UInt32
    szPrerequisitePbk: Char * 260
    szPrerequisiteEntry: Char * 257
    dwRedialCount: UInt32
    dwRedialPause: UInt32
    ipv6addrDns: win32more.Windows.Win32.Networking.WinSock.IN6_ADDR
    ipv6addrDnsAlt: win32more.Windows.Win32.Networking.WinSock.IN6_ADDR
    dwIPv4InterfaceMetric: UInt32
    dwIPv6InterfaceMetric: UInt32
    ipv6addr: win32more.Windows.Win32.Networking.WinSock.IN6_ADDR
    dwIPv6PrefixLength: UInt32
    dwNetworkOutageTime: UInt32
    szIDi: Char * 257
    szIDr: Char * 257
    fIsImsConfig: win32more.Windows.Win32.Foundation.BOOL
    IdiType: win32more.Windows.Win32.NetworkManagement.Rras.IKEV2_ID_PAYLOAD_TYPE
    IdrType: win32more.Windows.Win32.NetworkManagement.Rras.IKEV2_ID_PAYLOAD_TYPE
    fDisableIKEv2Fragmentation: win32more.Windows.Win32.Foundation.BOOL
RASENTRY = UnicodeAlias('RASENTRYW')
RASENTRY_DIAL_MODE = UInt32
RASEDM_DialAll: win32more.Windows.Win32.NetworkManagement.Rras.RASENTRY_DIAL_MODE = 1
RASEDM_DialAsNeeded: win32more.Windows.Win32.NetworkManagement.Rras.RASENTRY_DIAL_MODE = 2
if ARCH in 'X64,ARM64':
    class RASIKEV2_PROJECTION_INFO(Structure):
        dwIPv4NegotiationError: UInt32
        ipv4Address: win32more.Windows.Win32.Networking.WinSock.IN_ADDR
        ipv4ServerAddress: win32more.Windows.Win32.Networking.WinSock.IN_ADDR
        dwIPv6NegotiationError: UInt32
        ipv6Address: win32more.Windows.Win32.Networking.WinSock.IN6_ADDR
        ipv6ServerAddress: win32more.Windows.Win32.Networking.WinSock.IN6_ADDR
        dwPrefixLength: UInt32
        dwAuthenticationProtocol: UInt32
        dwEapTypeId: UInt32
        dwFlags: win32more.Windows.Win32.NetworkManagement.Rras.RASIKEV_PROJECTION_INFO_FLAGS
        dwEncryptionMethod: UInt32
        numIPv4ServerAddresses: UInt32
        ipv4ServerAddresses: POINTER(win32more.Windows.Win32.Networking.WinSock.IN_ADDR)
        numIPv6ServerAddresses: UInt32
        ipv6ServerAddresses: POINTER(win32more.Windows.Win32.Networking.WinSock.IN6_ADDR)
        _pack_ = 4
elif ARCH in 'X86':
    class RASIKEV2_PROJECTION_INFO(Structure):
        dwIPv4NegotiationError: UInt32
        ipv4Address: win32more.Windows.Win32.Networking.WinSock.IN_ADDR
        ipv4ServerAddress: win32more.Windows.Win32.Networking.WinSock.IN_ADDR
        dwIPv6NegotiationError: UInt32
        ipv6Address: win32more.Windows.Win32.Networking.WinSock.IN6_ADDR
        ipv6ServerAddress: win32more.Windows.Win32.Networking.WinSock.IN6_ADDR
        dwPrefixLength: UInt32
        dwAuthenticationProtocol: UInt32
        dwEapTypeId: UInt32
        dwFlags: win32more.Windows.Win32.NetworkManagement.Rras.RASIKEV_PROJECTION_INFO_FLAGS
        dwEncryptionMethod: UInt32
        numIPv4ServerAddresses: UInt32
        ipv4ServerAddresses: POINTER(win32more.Windows.Win32.Networking.WinSock.IN_ADDR)
        numIPv6ServerAddresses: UInt32
        ipv6ServerAddresses: POINTER(win32more.Windows.Win32.Networking.WinSock.IN6_ADDR)
RASIKEV_PROJECTION_INFO_FLAGS = UInt32
RASIKEv2_FLAGS_MOBIKESUPPORTED: win32more.Windows.Win32.NetworkManagement.Rras.RASIKEV_PROJECTION_INFO_FLAGS = 1
RASIKEv2_FLAGS_BEHIND_NAT: win32more.Windows.Win32.NetworkManagement.Rras.RASIKEV_PROJECTION_INFO_FLAGS = 2
RASIKEv2_FLAGS_SERVERBEHIND_NAT: win32more.Windows.Win32.NetworkManagement.Rras.RASIKEV_PROJECTION_INFO_FLAGS = 4
class RASIPADDR(Structure):
    a: Byte
    b: Byte
    c: Byte
    d: Byte
class RASIPXW(Structure):
    dwSize: UInt32
    dwError: UInt32
    szIpxAddress: Char * 22
class RASNOUSERA(Structure):
    dwSize: UInt32
    dwFlags: UInt32
    dwTimeoutMs: UInt32
    szUserName: win32more.Windows.Win32.Foundation.CHAR * 257
    szPassword: win32more.Windows.Win32.Foundation.CHAR * 257
    szDomain: win32more.Windows.Win32.Foundation.CHAR * 16
class RASNOUSERW(Structure):
    dwSize: UInt32
    dwFlags: UInt32
    dwTimeoutMs: UInt32
    szUserName: Char * 257
    szPassword: Char * 257
    szDomain: Char * 16
RASNOUSER = UnicodeAlias('RASNOUSERW')
if ARCH in 'X64,ARM64':
    class RASPBDLGA(Structure):
        dwSize: UInt32
        hwndOwner: win32more.Windows.Win32.Foundation.HWND
        dwFlags: UInt32
        xDlg: Int32
        yDlg: Int32
        dwCallbackId: UIntPtr
        pCallback: win32more.Windows.Win32.NetworkManagement.Rras.RASPBDLGFUNCA
        dwError: UInt32
        reserved: UIntPtr
        reserved2: UIntPtr
        _pack_ = 4
elif ARCH in 'X86':
    class RASPBDLGA(Structure):
        dwSize: UInt32
        hwndOwner: win32more.Windows.Win32.Foundation.HWND
        dwFlags: UInt32
        xDlg: Int32
        yDlg: Int32
        dwCallbackId: UIntPtr
        pCallback: win32more.Windows.Win32.NetworkManagement.Rras.RASPBDLGFUNCA
        dwError: UInt32
        reserved: UIntPtr
        reserved2: UIntPtr
@winfunctype_pointer
def RASPBDLGFUNCA(param0: UIntPtr, param1: UInt32, param2: win32more.Windows.Win32.Foundation.PSTR, param3: VoidPtr) -> Void: ...
@winfunctype_pointer
def RASPBDLGFUNCW(param0: UIntPtr, param1: UInt32, param2: win32more.Windows.Win32.Foundation.PWSTR, param3: VoidPtr) -> Void: ...
RASPBDLGFUNC = UnicodeAlias('RASPBDLGFUNCW')
if ARCH in 'X64,ARM64':
    class RASPBDLGW(Structure):
        dwSize: UInt32
        hwndOwner: win32more.Windows.Win32.Foundation.HWND
        dwFlags: UInt32
        xDlg: Int32
        yDlg: Int32
        dwCallbackId: UIntPtr
        pCallback: win32more.Windows.Win32.NetworkManagement.Rras.RASPBDLGFUNCW
        dwError: UInt32
        reserved: UIntPtr
        reserved2: UIntPtr
        _pack_ = 4
elif ARCH in 'X86':
    class RASPBDLGW(Structure):
        dwSize: UInt32
        hwndOwner: win32more.Windows.Win32.Foundation.HWND
        dwFlags: UInt32
        xDlg: Int32
        yDlg: Int32
        dwCallbackId: UIntPtr
        pCallback: win32more.Windows.Win32.NetworkManagement.Rras.RASPBDLGFUNCW
        dwError: UInt32
        reserved: UIntPtr
        reserved2: UIntPtr
if ARCH in 'X64,ARM64':
    RASPBDLG = UnicodeAlias('RASPBDLGW')
elif ARCH in 'X86':
    RASPBDLG = UnicodeAlias('RASPBDLGW')
class RASPPPCCP(Structure):
    dwSize: UInt32
    dwError: UInt32
    dwCompressionAlgorithm: UInt32
    dwOptions: UInt32
    dwServerCompressionAlgorithm: UInt32
    dwServerOptions: UInt32
class RASPPPIPA(Structure):
    dwSize: UInt32
    dwError: UInt32
    szIpAddress: win32more.Windows.Win32.Foundation.CHAR * 16
    szServerIpAddress: win32more.Windows.Win32.Foundation.CHAR * 16
    dwOptions: UInt32
    dwServerOptions: UInt32
class RASPPPIPV6(Structure):
    dwSize: UInt32
    dwError: UInt32
    bLocalInterfaceIdentifier: Byte * 8
    bPeerInterfaceIdentifier: Byte * 8
    bLocalCompressionProtocol: Byte * 2
    bPeerCompressionProtocol: Byte * 2
class RASPPPIPW(Structure):
    dwSize: UInt32
    dwError: UInt32
    szIpAddress: Char * 16
    szServerIpAddress: Char * 16
    dwOptions: UInt32
    dwServerOptions: UInt32
RASPPPIP = UnicodeAlias('RASPPPIPW')
class RASPPPIPXA(Structure):
    dwSize: UInt32
    dwError: UInt32
    szIpxAddress: win32more.Windows.Win32.Foundation.CHAR * 22
class RASPPPLCPA(Structure):
    dwSize: UInt32
    fBundled: win32more.Windows.Win32.Foundation.BOOL
    dwError: UInt32
    dwAuthenticationProtocol: UInt32
    dwAuthenticationData: UInt32
    dwEapTypeId: UInt32
    dwServerAuthenticationProtocol: UInt32
    dwServerAuthenticationData: UInt32
    dwServerEapTypeId: UInt32
    fMultilink: win32more.Windows.Win32.Foundation.BOOL
    dwTerminateReason: UInt32
    dwServerTerminateReason: UInt32
    szReplyMessage: win32more.Windows.Win32.Foundation.CHAR * 1024
    dwOptions: UInt32
    dwServerOptions: UInt32
class RASPPPLCPW(Structure):
    dwSize: UInt32
    fBundled: win32more.Windows.Win32.Foundation.BOOL
    dwError: UInt32
    dwAuthenticationProtocol: UInt32
    dwAuthenticationData: UInt32
    dwEapTypeId: UInt32
    dwServerAuthenticationProtocol: UInt32
    dwServerAuthenticationData: UInt32
    dwServerEapTypeId: UInt32
    fMultilink: win32more.Windows.Win32.Foundation.BOOL
    dwTerminateReason: UInt32
    dwServerTerminateReason: UInt32
    szReplyMessage: Char * 1024
    dwOptions: UInt32
    dwServerOptions: UInt32
RASPPPLCP = UnicodeAlias('RASPPPLCPW')
class RASPPPNBFA(Structure):
    dwSize: UInt32
    dwError: UInt32
    dwNetBiosError: UInt32
    szNetBiosError: win32more.Windows.Win32.Foundation.CHAR * 17
    szWorkstationName: win32more.Windows.Win32.Foundation.CHAR * 17
    bLana: Byte
class RASPPPNBFW(Structure):
    dwSize: UInt32
    dwError: UInt32
    dwNetBiosError: UInt32
    szNetBiosError: Char * 17
    szWorkstationName: Char * 17
    bLana: Byte
RASPPPNBF = UnicodeAlias('RASPPPNBFW')
class RASPPP_PROJECTION_INFO(Structure):
    dwIPv4NegotiationError: UInt32
    ipv4Address: win32more.Windows.Win32.Networking.WinSock.IN_ADDR
    ipv4ServerAddress: win32more.Windows.Win32.Networking.WinSock.IN_ADDR
    dwIPv4Options: UInt32
    dwIPv4ServerOptions: UInt32
    dwIPv6NegotiationError: UInt32
    bInterfaceIdentifier: Byte * 8
    bServerInterfaceIdentifier: Byte * 8
    fBundled: win32more.Windows.Win32.Foundation.BOOL
    fMultilink: win32more.Windows.Win32.Foundation.BOOL
    dwAuthenticationProtocol: win32more.Windows.Win32.NetworkManagement.Rras.RASPPP_PROJECTION_INFO_SERVER_AUTH_PROTOCOL
    dwAuthenticationData: win32more.Windows.Win32.NetworkManagement.Rras.RASPPP_PROJECTION_INFO_SERVER_AUTH_DATA
    dwServerAuthenticationProtocol: win32more.Windows.Win32.NetworkManagement.Rras.RASPPP_PROJECTION_INFO_SERVER_AUTH_PROTOCOL
    dwServerAuthenticationData: win32more.Windows.Win32.NetworkManagement.Rras.RASPPP_PROJECTION_INFO_SERVER_AUTH_DATA
    dwEapTypeId: UInt32
    dwServerEapTypeId: UInt32
    dwLcpOptions: UInt32
    dwLcpServerOptions: UInt32
    dwCcpError: UInt32
    dwCcpCompressionAlgorithm: UInt32
    dwCcpServerCompressionAlgorithm: UInt32
    dwCcpOptions: UInt32
    dwCcpServerOptions: UInt32
RASPPP_PROJECTION_INFO_SERVER_AUTH_DATA = UInt32
RASLCPAD_CHAP_MD5: win32more.Windows.Win32.NetworkManagement.Rras.RASPPP_PROJECTION_INFO_SERVER_AUTH_DATA = 5
RASLCPAD_CHAP_MS: win32more.Windows.Win32.NetworkManagement.Rras.RASPPP_PROJECTION_INFO_SERVER_AUTH_DATA = 128
RASLCPAD_CHAP_MSV2: win32more.Windows.Win32.NetworkManagement.Rras.RASPPP_PROJECTION_INFO_SERVER_AUTH_DATA = 129
RASPPP_PROJECTION_INFO_SERVER_AUTH_PROTOCOL = UInt32
RASLCPAP_PAP: win32more.Windows.Win32.NetworkManagement.Rras.RASPPP_PROJECTION_INFO_SERVER_AUTH_PROTOCOL = 49187
RASLCPAP_SPAP: win32more.Windows.Win32.NetworkManagement.Rras.RASPPP_PROJECTION_INFO_SERVER_AUTH_PROTOCOL = 49191
RASLCPAP_CHAP: win32more.Windows.Win32.NetworkManagement.Rras.RASPPP_PROJECTION_INFO_SERVER_AUTH_PROTOCOL = 49699
RASLCPAP_EAP: win32more.Windows.Win32.NetworkManagement.Rras.RASPPP_PROJECTION_INFO_SERVER_AUTH_PROTOCOL = 49703
RASPROJECTION = Int32
RASP_Amb: win32more.Windows.Win32.NetworkManagement.Rras.RASPROJECTION = 65536
RASP_PppNbf: win32more.Windows.Win32.NetworkManagement.Rras.RASPROJECTION = 32831
RASP_PppIpx: win32more.Windows.Win32.NetworkManagement.Rras.RASPROJECTION = 32811
RASP_PppIp: win32more.Windows.Win32.NetworkManagement.Rras.RASPROJECTION = 32801
RASP_PppCcp: win32more.Windows.Win32.NetworkManagement.Rras.RASPROJECTION = 33021
RASP_PppLcp: win32more.Windows.Win32.NetworkManagement.Rras.RASPROJECTION = 49185
RASP_PppIpv6: win32more.Windows.Win32.NetworkManagement.Rras.RASPROJECTION = 32855
RASPROJECTION_INFO_TYPE = Int32
PROJECTION_INFO_TYPE_PPP: win32more.Windows.Win32.NetworkManagement.Rras.RASPROJECTION_INFO_TYPE = 1
PROJECTION_INFO_TYPE_IKEv2: win32more.Windows.Win32.NetworkManagement.Rras.RASPROJECTION_INFO_TYPE = 2
@winfunctype_pointer
def RASSECURITYPROC() -> UInt32: ...
class RASSUBENTRYA(Structure):
    dwSize: UInt32
    dwfFlags: UInt32
    szDeviceType: win32more.Windows.Win32.Foundation.CHAR * 17
    szDeviceName: win32more.Windows.Win32.Foundation.CHAR * 129
    szLocalPhoneNumber: win32more.Windows.Win32.Foundation.CHAR * 129
    dwAlternateOffset: UInt32
class RASSUBENTRYW(Structure):
    dwSize: UInt32
    dwfFlags: UInt32
    szDeviceType: Char * 17
    szDeviceName: Char * 129
    szLocalPhoneNumber: Char * 129
    dwAlternateOffset: UInt32
RASSUBENTRY = UnicodeAlias('RASSUBENTRYW')
class RASTUNNELENDPOINT(Structure):
    dwType: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        ipv4: win32more.Windows.Win32.Networking.WinSock.IN_ADDR
        ipv6: win32more.Windows.Win32.Networking.WinSock.IN6_ADDR
class RASUPDATECONN(Structure):
    version: win32more.Windows.Win32.NetworkManagement.Rras.RASAPIVERSION
    dwSize: UInt32
    dwFlags: UInt32
    dwIfIndex: UInt32
    localEndPoint: win32more.Windows.Win32.NetworkManagement.Rras.RASTUNNELENDPOINT
    remoteEndPoint: win32more.Windows.Win32.NetworkManagement.Rras.RASTUNNELENDPOINT
class RAS_CONNECTION_0(Structure):
    hConnection: win32more.Windows.Win32.Foundation.HANDLE
    hInterface: win32more.Windows.Win32.Foundation.HANDLE
    dwConnectDuration: UInt32
    dwInterfaceType: win32more.Windows.Win32.NetworkManagement.Rras.ROUTER_INTERFACE_TYPE
    dwConnectionFlags: win32more.Windows.Win32.NetworkManagement.Rras.RAS_FLAGS
    wszInterfaceName: Char * 257
    wszUserName: Char * 257
    wszLogonDomain: Char * 16
    wszRemoteComputer: Char * 17
class RAS_CONNECTION_1(Structure):
    hConnection: win32more.Windows.Win32.Foundation.HANDLE
    hInterface: win32more.Windows.Win32.Foundation.HANDLE
    PppInfo: win32more.Windows.Win32.NetworkManagement.Rras.PPP_INFO
    dwBytesXmited: UInt32
    dwBytesRcved: UInt32
    dwFramesXmited: UInt32
    dwFramesRcved: UInt32
    dwCrcErr: UInt32
    dwTimeoutErr: UInt32
    dwAlignmentErr: UInt32
    dwHardwareOverrunErr: UInt32
    dwFramingErr: UInt32
    dwBufferOverrunErr: UInt32
    dwCompressionRatioIn: UInt32
    dwCompressionRatioOut: UInt32
class RAS_CONNECTION_2(Structure):
    hConnection: win32more.Windows.Win32.Foundation.HANDLE
    wszUserName: Char * 257
    dwInterfaceType: win32more.Windows.Win32.NetworkManagement.Rras.ROUTER_INTERFACE_TYPE
    guid: Guid
    PppInfo2: win32more.Windows.Win32.NetworkManagement.Rras.PPP_INFO_2
class RAS_CONNECTION_3(Structure):
    dwVersion: UInt32
    dwSize: UInt32
    hConnection: win32more.Windows.Win32.Foundation.HANDLE
    wszUserName: Char * 257
    dwInterfaceType: win32more.Windows.Win32.NetworkManagement.Rras.ROUTER_INTERFACE_TYPE
    guid: Guid
    PppInfo3: win32more.Windows.Win32.NetworkManagement.Rras.PPP_INFO_3
    rasQuarState: win32more.Windows.Win32.NetworkManagement.Rras.RAS_QUARANTINE_STATE
    timer: win32more.Windows.Win32.Foundation.FILETIME
class RAS_CONNECTION_4(Structure):
    dwConnectDuration: UInt32
    dwInterfaceType: win32more.Windows.Win32.NetworkManagement.Rras.ROUTER_INTERFACE_TYPE
    dwConnectionFlags: win32more.Windows.Win32.NetworkManagement.Rras.RAS_FLAGS
    wszInterfaceName: Char * 257
    wszUserName: Char * 257
    wszLogonDomain: Char * 16
    wszRemoteComputer: Char * 17
    guid: Guid
    rasQuarState: win32more.Windows.Win32.NetworkManagement.Rras.RAS_QUARANTINE_STATE
    probationTime: win32more.Windows.Win32.Foundation.FILETIME
    connectionStartTime: win32more.Windows.Win32.Foundation.FILETIME
    ullBytesXmited: UInt64
    ullBytesRcved: UInt64
    dwFramesXmited: UInt32
    dwFramesRcved: UInt32
    dwCrcErr: UInt32
    dwTimeoutErr: UInt32
    dwAlignmentErr: UInt32
    dwHardwareOverrunErr: UInt32
    dwFramingErr: UInt32
    dwBufferOverrunErr: UInt32
    dwCompressionRatioIn: UInt32
    dwCompressionRatioOut: UInt32
    dwNumSwitchOvers: UInt32
    wszRemoteEndpointAddress: Char * 65
    wszLocalEndpointAddress: Char * 65
    ProjectionInfo: win32more.Windows.Win32.NetworkManagement.Rras.PROJECTION_INFO2
    hConnection: win32more.Windows.Win32.Foundation.HANDLE
    hInterface: win32more.Windows.Win32.Foundation.HANDLE
    dwDeviceType: UInt32
class RAS_CONNECTION_EX(Structure):
    Header: win32more.Windows.Win32.NetworkManagement.Rras.MPRAPI_OBJECT_HEADER
    dwConnectDuration: UInt32
    dwInterfaceType: win32more.Windows.Win32.NetworkManagement.Rras.ROUTER_INTERFACE_TYPE
    dwConnectionFlags: win32more.Windows.Win32.NetworkManagement.Rras.RAS_FLAGS
    wszInterfaceName: Char * 257
    wszUserName: Char * 257
    wszLogonDomain: Char * 16
    wszRemoteComputer: Char * 17
    guid: Guid
    rasQuarState: win32more.Windows.Win32.NetworkManagement.Rras.RAS_QUARANTINE_STATE
    probationTime: win32more.Windows.Win32.Foundation.FILETIME
    dwBytesXmited: UInt32
    dwBytesRcved: UInt32
    dwFramesXmited: UInt32
    dwFramesRcved: UInt32
    dwCrcErr: UInt32
    dwTimeoutErr: UInt32
    dwAlignmentErr: UInt32
    dwHardwareOverrunErr: UInt32
    dwFramingErr: UInt32
    dwBufferOverrunErr: UInt32
    dwCompressionRatioIn: UInt32
    dwCompressionRatioOut: UInt32
    dwNumSwitchOvers: UInt32
    wszRemoteEndpointAddress: Char * 65
    wszLocalEndpointAddress: Char * 65
    ProjectionInfo: win32more.Windows.Win32.NetworkManagement.Rras.PROJECTION_INFO
    hConnection: win32more.Windows.Win32.Foundation.HANDLE
    hInterface: win32more.Windows.Win32.Foundation.HANDLE
RAS_FLAGS = UInt32
RAS_FLAGS_PPP_CONNECTION: win32more.Windows.Win32.NetworkManagement.Rras.RAS_FLAGS = 1
RAS_FLAGS_MESSENGER_PRESENT: win32more.Windows.Win32.NetworkManagement.Rras.RAS_FLAGS = 2
RAS_FLAGS_QUARANTINE_PRESENT: win32more.Windows.Win32.NetworkManagement.Rras.RAS_FLAGS = 8
RAS_FLAGS_ARAP_CONNECTION: win32more.Windows.Win32.NetworkManagement.Rras.RAS_FLAGS = 16
RAS_FLAGS_IKEV2_CONNECTION: win32more.Windows.Win32.NetworkManagement.Rras.RAS_FLAGS = 16
RAS_FLAGS_DORMANT: win32more.Windows.Win32.NetworkManagement.Rras.RAS_FLAGS = 32
RAS_HARDWARE_CONDITION = Int32
RAS_HARDWARE_OPERATIONAL: win32more.Windows.Win32.NetworkManagement.Rras.RAS_HARDWARE_CONDITION = 0
RAS_HARDWARE_FAILURE: win32more.Windows.Win32.NetworkManagement.Rras.RAS_HARDWARE_CONDITION = 1
class RAS_PORT_0(Structure):
    hPort: win32more.Windows.Win32.Foundation.HANDLE
    hConnection: win32more.Windows.Win32.Foundation.HANDLE
    dwPortCondition: win32more.Windows.Win32.NetworkManagement.Rras.RAS_PORT_CONDITION
    dwTotalNumberOfCalls: UInt32
    dwConnectDuration: UInt32
    wszPortName: Char * 17
    wszMediaName: Char * 17
    wszDeviceName: Char * 129
    wszDeviceType: Char * 17
class RAS_PORT_1(Structure):
    hPort: win32more.Windows.Win32.Foundation.HANDLE
    hConnection: win32more.Windows.Win32.Foundation.HANDLE
    dwHardwareCondition: win32more.Windows.Win32.NetworkManagement.Rras.RAS_HARDWARE_CONDITION
    dwLineSpeed: UInt32
    dwBytesXmited: UInt32
    dwBytesRcved: UInt32
    dwFramesXmited: UInt32
    dwFramesRcved: UInt32
    dwCrcErr: UInt32
    dwTimeoutErr: UInt32
    dwAlignmentErr: UInt32
    dwHardwareOverrunErr: UInt32
    dwFramingErr: UInt32
    dwBufferOverrunErr: UInt32
    dwCompressionRatioIn: UInt32
    dwCompressionRatioOut: UInt32
class RAS_PORT_2(Structure):
    hPort: win32more.Windows.Win32.Foundation.HANDLE
    hConnection: win32more.Windows.Win32.Foundation.HANDLE
    dwConn_State: UInt32
    wszPortName: Char * 17
    wszMediaName: Char * 17
    wszDeviceName: Char * 129
    wszDeviceType: Char * 17
    dwHardwareCondition: win32more.Windows.Win32.NetworkManagement.Rras.RAS_HARDWARE_CONDITION
    dwLineSpeed: UInt32
    dwCrcErr: UInt32
    dwSerialOverRunErrs: UInt32
    dwTimeoutErr: UInt32
    dwAlignmentErr: UInt32
    dwHardwareOverrunErr: UInt32
    dwFramingErr: UInt32
    dwBufferOverrunErr: UInt32
    dwCompressionRatioIn: UInt32
    dwCompressionRatioOut: UInt32
    dwTotalErrors: UInt32
    ullBytesXmited: UInt64
    ullBytesRcved: UInt64
    ullFramesXmited: UInt64
    ullFramesRcved: UInt64
    ullBytesTxUncompressed: UInt64
    ullBytesTxCompressed: UInt64
    ullBytesRcvUncompressed: UInt64
    ullBytesRcvCompressed: UInt64
RAS_PORT_CONDITION = Int32
RAS_PORT_NON_OPERATIONAL: win32more.Windows.Win32.NetworkManagement.Rras.RAS_PORT_CONDITION = 0
RAS_PORT_DISCONNECTED: win32more.Windows.Win32.NetworkManagement.Rras.RAS_PORT_CONDITION = 1
RAS_PORT_CALLING_BACK: win32more.Windows.Win32.NetworkManagement.Rras.RAS_PORT_CONDITION = 2
RAS_PORT_LISTENING: win32more.Windows.Win32.NetworkManagement.Rras.RAS_PORT_CONDITION = 3
RAS_PORT_AUTHENTICATING: win32more.Windows.Win32.NetworkManagement.Rras.RAS_PORT_CONDITION = 4
RAS_PORT_AUTHENTICATED: win32more.Windows.Win32.NetworkManagement.Rras.RAS_PORT_CONDITION = 5
RAS_PORT_INITIALIZING: win32more.Windows.Win32.NetworkManagement.Rras.RAS_PORT_CONDITION = 6
class RAS_PROJECTION_INFO(Structure):
    version: win32more.Windows.Win32.NetworkManagement.Rras.RASAPIVERSION
    type: win32more.Windows.Win32.NetworkManagement.Rras.RASPROJECTION_INFO_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        ppp: win32more.Windows.Win32.NetworkManagement.Rras.RASPPP_PROJECTION_INFO
        ikev2: win32more.Windows.Win32.NetworkManagement.Rras.RASIKEV2_PROJECTION_INFO
RAS_QUARANTINE_STATE = Int32
RAS_QUAR_STATE_NORMAL: win32more.Windows.Win32.NetworkManagement.Rras.RAS_QUARANTINE_STATE = 0
RAS_QUAR_STATE_QUARANTINE: win32more.Windows.Win32.NetworkManagement.Rras.RAS_QUARANTINE_STATE = 1
RAS_QUAR_STATE_PROBATION: win32more.Windows.Win32.NetworkManagement.Rras.RAS_QUARANTINE_STATE = 2
RAS_QUAR_STATE_NOT_CAPABLE: win32more.Windows.Win32.NetworkManagement.Rras.RAS_QUARANTINE_STATE = 3
class RAS_SECURITY_INFO(Structure):
    LastError: UInt32
    BytesReceived: UInt32
    DeviceName: win32more.Windows.Win32.Foundation.CHAR * 129
class RAS_STATS(Structure):
    dwSize: UInt32
    dwBytesXmited: UInt32
    dwBytesRcved: UInt32
    dwFramesXmited: UInt32
    dwFramesRcved: UInt32
    dwCrcErr: UInt32
    dwTimeoutErr: UInt32
    dwAlignmentErr: UInt32
    dwHardwareOverrunErr: UInt32
    dwFramingErr: UInt32
    dwBufferOverrunErr: UInt32
    dwCompressionRatioIn: UInt32
    dwCompressionRatioOut: UInt32
    dwBps: UInt32
    dwConnectDuration: UInt32
class RAS_UPDATE_CONNECTION(Structure):
    Header: win32more.Windows.Win32.NetworkManagement.Rras.MPRAPI_OBJECT_HEADER
    dwIfIndex: UInt32
    wszLocalEndpointAddress: Char * 65
    wszRemoteEndpointAddress: Char * 65
class RAS_USER_0(Structure):
    bfPrivilege: Byte
    wszPhoneNumber: Char * 129
class RAS_USER_1(Structure):
    bfPrivilege: Byte
    wszPhoneNumber: Char * 129
    bfPrivilege2: Byte
ROUTER_CONNECTION_STATE = Int32
ROUTER_IF_STATE_UNREACHABLE: win32more.Windows.Win32.NetworkManagement.Rras.ROUTER_CONNECTION_STATE = 0
ROUTER_IF_STATE_DISCONNECTED: win32more.Windows.Win32.NetworkManagement.Rras.ROUTER_CONNECTION_STATE = 1
ROUTER_IF_STATE_CONNECTING: win32more.Windows.Win32.NetworkManagement.Rras.ROUTER_CONNECTION_STATE = 2
ROUTER_IF_STATE_CONNECTED: win32more.Windows.Win32.NetworkManagement.Rras.ROUTER_CONNECTION_STATE = 3
class ROUTER_CUSTOM_IKEv2_POLICY0(Structure):
    dwIntegrityMethod: UInt32
    dwEncryptionMethod: UInt32
    dwCipherTransformConstant: UInt32
    dwAuthTransformConstant: UInt32
    dwPfsGroup: UInt32
    dwDhGroup: UInt32
class ROUTER_IKEv2_IF_CUSTOM_CONFIG0(Structure):
    dwSaLifeTime: UInt32
    dwSaDataSize: UInt32
    certificateName: win32more.Windows.Win32.Security.Cryptography.CRYPT_INTEGER_BLOB
    customPolicy: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.ROUTER_CUSTOM_IKEv2_POLICY0)
class ROUTER_IKEv2_IF_CUSTOM_CONFIG1(Structure):
    dwSaLifeTime: UInt32
    dwSaDataSize: UInt32
    certificateName: win32more.Windows.Win32.Security.Cryptography.CRYPT_INTEGER_BLOB
    customPolicy: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.ROUTER_CUSTOM_IKEv2_POLICY0)
    certificateHash: win32more.Windows.Win32.Security.Cryptography.CRYPT_INTEGER_BLOB
class ROUTER_IKEv2_IF_CUSTOM_CONFIG2(Structure):
    dwSaLifeTime: UInt32
    dwSaDataSize: UInt32
    certificateName: win32more.Windows.Win32.Security.Cryptography.CRYPT_INTEGER_BLOB
    customPolicy: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.ROUTER_CUSTOM_IKEv2_POLICY0)
    certificateHash: win32more.Windows.Win32.Security.Cryptography.CRYPT_INTEGER_BLOB
    dwMmSaLifeTime: UInt32
    vpnTrafficSelectors: win32more.Windows.Win32.NetworkManagement.Rras.MPR_VPN_TRAFFIC_SELECTORS
ROUTER_INTERFACE_TYPE = Int32
ROUTER_IF_TYPE_CLIENT: win32more.Windows.Win32.NetworkManagement.Rras.ROUTER_INTERFACE_TYPE = 0
ROUTER_IF_TYPE_HOME_ROUTER: win32more.Windows.Win32.NetworkManagement.Rras.ROUTER_INTERFACE_TYPE = 1
ROUTER_IF_TYPE_FULL_ROUTER: win32more.Windows.Win32.NetworkManagement.Rras.ROUTER_INTERFACE_TYPE = 2
ROUTER_IF_TYPE_DEDICATED: win32more.Windows.Win32.NetworkManagement.Rras.ROUTER_INTERFACE_TYPE = 3
ROUTER_IF_TYPE_INTERNAL: win32more.Windows.Win32.NetworkManagement.Rras.ROUTER_INTERFACE_TYPE = 4
ROUTER_IF_TYPE_LOOPBACK: win32more.Windows.Win32.NetworkManagement.Rras.ROUTER_INTERFACE_TYPE = 5
ROUTER_IF_TYPE_TUNNEL1: win32more.Windows.Win32.NetworkManagement.Rras.ROUTER_INTERFACE_TYPE = 6
ROUTER_IF_TYPE_DIALOUT: win32more.Windows.Win32.NetworkManagement.Rras.ROUTER_INTERFACE_TYPE = 7
ROUTER_IF_TYPE_MAX: win32more.Windows.Win32.NetworkManagement.Rras.ROUTER_INTERFACE_TYPE = 8
class ROUTING_PROTOCOL_CONFIG(Structure):
    dwCallbackFlags: UInt32
    pfnRpfCallback: win32more.Windows.Win32.NetworkManagement.Rras.PMGM_RPF_CALLBACK
    pfnCreationAlertCallback: win32more.Windows.Win32.NetworkManagement.Rras.PMGM_CREATION_ALERT_CALLBACK
    pfnPruneAlertCallback: win32more.Windows.Win32.NetworkManagement.Rras.PMGM_PRUNE_ALERT_CALLBACK
    pfnJoinAlertCallback: win32more.Windows.Win32.NetworkManagement.Rras.PMGM_JOIN_ALERT_CALLBACK
    pfnWrongIfCallback: win32more.Windows.Win32.NetworkManagement.Rras.PMGM_WRONG_IF_CALLBACK
    pfnLocalJoinCallback: win32more.Windows.Win32.NetworkManagement.Rras.PMGM_LOCAL_JOIN_CALLBACK
    pfnLocalLeaveCallback: win32more.Windows.Win32.NetworkManagement.Rras.PMGM_LOCAL_LEAVE_CALLBACK
    pfnDisableIgmpCallback: win32more.Windows.Win32.NetworkManagement.Rras.PMGM_DISABLE_IGMP_CALLBACK
    pfnEnableIgmpCallback: win32more.Windows.Win32.NetworkManagement.Rras.PMGM_ENABLE_IGMP_CALLBACK
class RTM_DEST_INFO(Structure):
    DestHandle: IntPtr
    DestAddress: win32more.Windows.Win32.NetworkManagement.Rras.RTM_NET_ADDRESS
    LastChanged: win32more.Windows.Win32.Foundation.FILETIME
    BelongsToViews: UInt32
    NumberOfViews: UInt32
    ViewInfo: _Anonymous_e__Struct * 1
    class _Anonymous_e__Struct(Structure):
        ViewId: Int32
        NumRoutes: UInt32
        Route: IntPtr
        Owner: IntPtr
        DestFlags: UInt32
        HoldRoute: IntPtr
@winfunctype_pointer
def RTM_ENTITY_EXPORT_METHOD(CallerHandle: IntPtr, CalleeHandle: IntPtr, Input: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RTM_ENTITY_METHOD_INPUT), Output: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RTM_ENTITY_METHOD_OUTPUT)) -> Void: ...
class RTM_ENTITY_EXPORT_METHODS(Structure):
    NumMethods: UInt32
    Methods: win32more.Windows.Win32.NetworkManagement.Rras.RTM_ENTITY_EXPORT_METHOD * 1
class RTM_ENTITY_ID(Structure):
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        EntityId: UInt64
        class _Anonymous_e__Struct(Structure):
            EntityProtocolId: UInt32
            EntityInstanceId: UInt32
class RTM_ENTITY_INFO(Structure):
    RtmInstanceId: UInt16
    AddressFamily: UInt16
    EntityId: win32more.Windows.Win32.NetworkManagement.Rras.RTM_ENTITY_ID
class RTM_ENTITY_METHOD_INPUT(Structure):
    MethodType: UInt32
    InputSize: UInt32
    InputData: Byte * 1
class RTM_ENTITY_METHOD_OUTPUT(Structure):
    MethodType: UInt32
    MethodStatus: UInt32
    OutputSize: UInt32
    OutputData: Byte * 1
@winfunctype_pointer
def RTM_EVENT_CALLBACK(RtmRegHandle: IntPtr, EventType: win32more.Windows.Win32.NetworkManagement.Rras.RTM_EVENT_TYPE, Context1: VoidPtr, Context2: VoidPtr) -> UInt32: ...
RTM_EVENT_TYPE = Int32
RTM_ENTITY_REGISTERED: win32more.Windows.Win32.NetworkManagement.Rras.RTM_EVENT_TYPE = 0
RTM_ENTITY_DEREGISTERED: win32more.Windows.Win32.NetworkManagement.Rras.RTM_EVENT_TYPE = 1
RTM_ROUTE_EXPIRED: win32more.Windows.Win32.NetworkManagement.Rras.RTM_EVENT_TYPE = 2
RTM_CHANGE_NOTIFICATION: win32more.Windows.Win32.NetworkManagement.Rras.RTM_EVENT_TYPE = 3
class RTM_NET_ADDRESS(Structure):
    AddressFamily: UInt16
    NumBits: UInt16
    AddrBits: Byte * 16
class RTM_NEXTHOP_INFO(Structure):
    NextHopAddress: win32more.Windows.Win32.NetworkManagement.Rras.RTM_NET_ADDRESS
    NextHopOwner: IntPtr
    InterfaceIndex: UInt32
    State: UInt16
    Flags: UInt16
    EntitySpecificInfo: VoidPtr
    RemoteNextHop: IntPtr
class RTM_NEXTHOP_LIST(Structure):
    NumNextHops: UInt16
    NextHops: IntPtr * 1
class RTM_PREF_INFO(Structure):
    Metric: UInt32
    Preference: UInt32
class RTM_REGN_PROFILE(Structure):
    MaxNextHopsInRoute: UInt32
    MaxHandlesInEnum: UInt32
    ViewsSupported: UInt32
    NumberOfViews: UInt32
class RTM_ROUTE_INFO(Structure):
    DestHandle: IntPtr
    RouteOwner: IntPtr
    Neighbour: IntPtr
    State: Byte
    Flags1: Byte
    Flags: UInt16
    PrefInfo: win32more.Windows.Win32.NetworkManagement.Rras.RTM_PREF_INFO
    BelongsToViews: UInt32
    EntitySpecificInfo: VoidPtr
    NextHopsList: win32more.Windows.Win32.NetworkManagement.Rras.RTM_NEXTHOP_LIST
@winfunctype_pointer
def RasCustomDeleteEntryNotifyFn(lpszPhonebook: win32more.Windows.Win32.Foundation.PWSTR, lpszEntry: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> UInt32: ...
@winfunctype_pointer
def RasCustomDialDlgFn(hInstDll: win32more.Windows.Win32.Foundation.HINSTANCE, dwFlags: UInt32, lpszPhonebook: win32more.Windows.Win32.Foundation.PWSTR, lpszEntry: win32more.Windows.Win32.Foundation.PWSTR, lpszPhoneNumber: win32more.Windows.Win32.Foundation.PWSTR, lpInfo: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASDIALDLG), pvInfo: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def RasCustomDialFn(hInstDll: win32more.Windows.Win32.Foundation.HINSTANCE, lpRasDialExtensions: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASDIALEXTENSIONS), lpszPhonebook: win32more.Windows.Win32.Foundation.PWSTR, lpRasDialParams: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASDIALPARAMSA), dwNotifierType: UInt32, lpvNotifier: VoidPtr, lphRasConn: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.HRASCONN), dwFlags: UInt32) -> UInt32: ...
@winfunctype_pointer
def RasCustomEntryDlgFn(hInstDll: win32more.Windows.Win32.Foundation.HINSTANCE, lpszPhonebook: win32more.Windows.Win32.Foundation.PWSTR, lpszEntry: win32more.Windows.Win32.Foundation.PWSTR, lpInfo: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASENTRYDLGA), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def RasCustomHangUpFn(hRasConn: win32more.Windows.Win32.NetworkManagement.Rras.HRASCONN) -> UInt32: ...
@winfunctype_pointer
def RasCustomScriptExecuteFn(hPort: win32more.Windows.Win32.Foundation.HANDLE, lpszPhonebook: win32more.Windows.Win32.Foundation.PWSTR, lpszEntryName: win32more.Windows.Win32.Foundation.PWSTR, pfnRasGetBuffer: win32more.Windows.Win32.NetworkManagement.Rras.PFNRASGETBUFFER, pfnRasFreeBuffer: win32more.Windows.Win32.NetworkManagement.Rras.PFNRASFREEBUFFER, pfnRasSendBuffer: win32more.Windows.Win32.NetworkManagement.Rras.PFNRASSENDBUFFER, pfnRasReceiveBuffer: win32more.Windows.Win32.NetworkManagement.Rras.PFNRASRECEIVEBUFFER, pfnRasRetrieveBuffer: win32more.Windows.Win32.NetworkManagement.Rras.PFNRASRETRIEVEBUFFER, hWnd: win32more.Windows.Win32.Foundation.HWND, pRasDialParams: POINTER(win32more.Windows.Win32.NetworkManagement.Rras.RASDIALPARAMSA), pvReserved: VoidPtr) -> UInt32: ...
class SECURITY_MESSAGE(Structure):
    dwMsgId: win32more.Windows.Win32.NetworkManagement.Rras.SECURITY_MESSAGE_MSG_ID
    hPort: IntPtr
    dwError: UInt32
    UserName: win32more.Windows.Win32.Foundation.CHAR * 257
    Domain: win32more.Windows.Win32.Foundation.CHAR * 16
SECURITY_MESSAGE_MSG_ID = UInt32
SECURITYMSG_SUCCESS: win32more.Windows.Win32.NetworkManagement.Rras.SECURITY_MESSAGE_MSG_ID = 1
SECURITYMSG_FAILURE: win32more.Windows.Win32.NetworkManagement.Rras.SECURITY_MESSAGE_MSG_ID = 2
SECURITYMSG_ERROR: win32more.Windows.Win32.NetworkManagement.Rras.SECURITY_MESSAGE_MSG_ID = 3
class SOURCE_GROUP_ENTRY(Structure):
    dwSourceAddr: UInt32
    dwSourceMask: UInt32
    dwGroupAddr: UInt32
    dwGroupMask: UInt32
class SSTP_CERT_INFO(Structure):
    isDefault: win32more.Windows.Win32.Foundation.BOOL
    certBlob: win32more.Windows.Win32.Security.Cryptography.CRYPT_INTEGER_BLOB
class SSTP_CONFIG_PARAMS(Structure):
    dwNumPorts: UInt32
    dwPortFlags: UInt32
    isUseHttps: win32more.Windows.Win32.Foundation.BOOL
    certAlgorithm: UInt32
    sstpCertDetails: win32more.Windows.Win32.NetworkManagement.Rras.SSTP_CERT_INFO
class VPN_TS_IP_ADDRESS(Structure):
    Type: UInt16
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        v4: win32more.Windows.Win32.Networking.WinSock.IN_ADDR
        v6: win32more.Windows.Win32.Networking.WinSock.IN6_ADDR


make_ready(__name__)
