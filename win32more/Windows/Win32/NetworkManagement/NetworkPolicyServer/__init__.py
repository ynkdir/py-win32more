from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Variant
ACCOUNTINGPROPERTIES = Int32
PROPERTY_ACCOUNTING_LOG_ACCOUNTING: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ACCOUNTINGPROPERTIES = 1026
PROPERTY_ACCOUNTING_LOG_ACCOUNTING_INTERIM: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ACCOUNTINGPROPERTIES = 1027
PROPERTY_ACCOUNTING_LOG_AUTHENTICATION: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ACCOUNTINGPROPERTIES = 1028
PROPERTY_ACCOUNTING_LOG_OPEN_NEW_FREQUENCY: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ACCOUNTINGPROPERTIES = 1029
PROPERTY_ACCOUNTING_LOG_OPEN_NEW_SIZE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ACCOUNTINGPROPERTIES = 1030
PROPERTY_ACCOUNTING_LOG_FILE_DIRECTORY: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ACCOUNTINGPROPERTIES = 1031
PROPERTY_ACCOUNTING_LOG_IAS1_FORMAT: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ACCOUNTINGPROPERTIES = 1032
PROPERTY_ACCOUNTING_LOG_ENABLE_LOGGING: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ACCOUNTINGPROPERTIES = 1033
PROPERTY_ACCOUNTING_LOG_DELETE_IF_FULL: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ACCOUNTINGPROPERTIES = 1034
PROPERTY_ACCOUNTING_SQL_MAX_SESSIONS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ACCOUNTINGPROPERTIES = 1035
PROPERTY_ACCOUNTING_LOG_AUTHENTICATION_INTERIM: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ACCOUNTINGPROPERTIES = 1036
PROPERTY_ACCOUNTING_LOG_FILE_IS_BACKUP: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ACCOUNTINGPROPERTIES = 1037
PROPERTY_ACCOUNTING_DISCARD_REQUEST_ON_FAILURE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ACCOUNTINGPROPERTIES = 1038
ATTRIBUTEFILTER = Int32
ATTRIBUTE_FILTER_NONE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEFILTER = 0
ATTRIBUTE_FILTER_VPN_DIALUP: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEFILTER = 1
ATTRIBUTE_FILTER_IEEE_802_1x: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEFILTER = 2
ATTRIBUTEID = UInt32
ATTRIBUTE_UNDEFINED: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 0
ATTRIBUTE_MIN_VALUE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 1
RADIUS_ATTRIBUTE_USER_NAME: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 1
RADIUS_ATTRIBUTE_USER_PASSWORD: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 2
RADIUS_ATTRIBUTE_CHAP_PASSWORD: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 3
RADIUS_ATTRIBUTE_NAS_IP_ADDRESS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4
RADIUS_ATTRIBUTE_NAS_PORT: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 5
RADIUS_ATTRIBUTE_SERVICE_TYPE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 6
RADIUS_ATTRIBUTE_FRAMED_PROTOCOL: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 7
RADIUS_ATTRIBUTE_FRAMED_IP_ADDRESS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8
RADIUS_ATTRIBUTE_FRAMED_IP_NETMASK: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 9
RADIUS_ATTRIBUTE_FRAMED_ROUTING: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 10
RADIUS_ATTRIBUTE_FILTER_ID: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 11
RADIUS_ATTRIBUTE_FRAMED_MTU: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 12
RADIUS_ATTRIBUTE_FRAMED_COMPRESSION: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 13
RADIUS_ATTRIBUTE_LOGIN_IP_HOST: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 14
RADIUS_ATTRIBUTE_LOGIN_SERVICE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 15
RADIUS_ATTRIBUTE_LOGIN_TCP_PORT: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 16
RADIUS_ATTRIBUTE_UNASSIGNED1: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 17
RADIUS_ATTRIBUTE_REPLY_MESSAGE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 18
RADIUS_ATTRIBUTE_CALLBACK_NUMBER: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 19
RADIUS_ATTRIBUTE_CALLBACK_ID: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 20
RADIUS_ATTRIBUTE_UNASSIGNED2: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 21
RADIUS_ATTRIBUTE_FRAMED_ROUTE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 22
RADIUS_ATTRIBUTE_FRAMED_IPX_NETWORK: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 23
RADIUS_ATTRIBUTE_STATE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 24
RADIUS_ATTRIBUTE_CLASS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 25
RADIUS_ATTRIBUTE_VENDOR_SPECIFIC: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 26
RADIUS_ATTRIBUTE_SESSION_TIMEOUT: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 27
RADIUS_ATTRIBUTE_IDLE_TIMEOUT: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 28
RADIUS_ATTRIBUTE_TERMINATION_ACTION: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 29
RADIUS_ATTRIBUTE_CALLED_STATION_ID: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 30
RADIUS_ATTRIBUTE_CALLING_STATION_ID: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 31
RADIUS_ATTRIBUTE_NAS_IDENTIFIER: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 32
RADIUS_ATTRIBUTE_PROXY_STATE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 33
RADIUS_ATTRIBUTE_LOGIN_LAT_SERVICE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 34
RADIUS_ATTRIBUTE_LOGIN_LAT_NODE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 35
RADIUS_ATTRIBUTE_LOGIN_LAT_GROUP: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 36
RADIUS_ATTRIBUTE_FRAMED_APPLETALK_LINK: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 37
RADIUS_ATTRIBUTE_FRAMED_APPLETALK_NET: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 38
RADIUS_ATTRIBUTE_FRAMED_APPLETALK_ZONE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 39
RADIUS_ATTRIBUTE_ACCT_STATUS_TYPE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 40
RADIUS_ATTRIBUTE_ACCT_DELAY_TIME: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 41
RADIUS_ATTRIBUTE_ACCT_INPUT_OCTETS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 42
RADIUS_ATTRIBUTE_ACCT_OUTPUT_OCTETS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 43
RADIUS_ATTRIBUTE_ACCT_SESSION_ID: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 44
RADIUS_ATTRIBUTE_ACCT_AUTHENTIC: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 45
RADIUS_ATTRIBUTE_ACCT_SESSION_TIME: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 46
RADIUS_ATTRIBUTE_ACCT_INPUT_PACKETS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 47
RADIUS_ATTRIBUTE_ACCT_OUTPUT_PACKETS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 48
RADIUS_ATTRIBUTE_ACCT_TERMINATE_CAUSE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 49
RADIUS_ATTRIBUTE_ACCT_MULTI_SSN_ID: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 50
RADIUS_ATTRIBUTE_ACCT_LINK_COUNT: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 51
RADIUS_ATTRIBUTE_CHAP_CHALLENGE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 60
RADIUS_ATTRIBUTE_NAS_PORT_TYPE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 61
RADIUS_ATTRIBUTE_PORT_LIMIT: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 62
RADIUS_ATTRIBUTE_LOGIN_LAT_PORT: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 63
RADIUS_ATTRIBUTE_TUNNEL_TYPE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 64
RADIUS_ATTRIBUTE_TUNNEL_MEDIUM_TYPE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 65
RADIUS_ATTRIBUTE_TUNNEL_CLIENT_ENDPT: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 66
RADIUS_ATTRIBUTE_TUNNEL_SERVER_ENDPT: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 67
RADIUS_ATTRIBUTE_ACCT_TUNNEL_CONN: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 68
RADIUS_ATTRIBUTE_TUNNEL_PASSWORD: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 69
RADIUS_ATTRIBUTE_ARAP_PASSWORD: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 70
RADIUS_ATTRIBUTE_ARAP_FEATURES: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 71
RADIUS_ATTRIBUTE_ARAP_ZONE_ACCESS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 72
RADIUS_ATTRIBUTE_ARAP_SECURITY: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 73
RADIUS_ATTRIBUTE_ARAP_SECURITY_DATA: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 74
RADIUS_ATTRIBUTE_PASSWORD_RETRY: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 75
RADIUS_ATTRIBUTE_PROMPT: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 76
RADIUS_ATTRIBUTE_CONNECT_INFO: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 77
RADIUS_ATTRIBUTE_CONFIGURATION_TOKEN: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 78
RADIUS_ATTRIBUTE_EAP_MESSAGE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 79
RADIUS_ATTRIBUTE_SIGNATURE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 80
RADIUS_ATTRIBUTE_TUNNEL_PVT_GROUP_ID: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 81
RADIUS_ATTRIBUTE_TUNNEL_ASSIGNMENT_ID: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 82
RADIUS_ATTRIBUTE_TUNNEL_PREFERENCE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 83
RADIUS_ATTRIBUTE_ARAP_CHALLENGE_RESPONSE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 84
RADIUS_ATTRIBUTE_ACCT_INTERIM_INTERVAL: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 85
RADIUS_ATTRIBUTE_NAS_IPv6_ADDRESS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 95
RADIUS_ATTRIBUTE_FRAMED_INTERFACE_ID: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 96
RADIUS_ATTRIBUTE_FRAMED_IPv6_PREFIX: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 97
RADIUS_ATTRIBUTE_LOGIN_IPv6_HOST: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 98
RADIUS_ATTRIBUTE_FRAMED_IPv6_ROUTE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 99
RADIUS_ATTRIBUTE_FRAMED_IPv6_POOL: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 100
IAS_ATTRIBUTE_SAVED_RADIUS_FRAMED_IP_ADDRESS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4096
IAS_ATTRIBUTE_SAVED_RADIUS_CALLBACK_NUMBER: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4097
IAS_ATTRIBUTE_NP_CALLING_STATION_ID: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4098
IAS_ATTRIBUTE_SAVED_NP_CALLING_STATION_ID: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4099
IAS_ATTRIBUTE_SAVED_RADIUS_FRAMED_ROUTE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4100
IAS_ATTRIBUTE_IGNORE_USER_DIALIN_PROPERTIES: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4101
IAS_ATTRIBUTE_NP_TIME_OF_DAY: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4102
IAS_ATTRIBUTE_NP_CALLED_STATION_ID: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4103
IAS_ATTRIBUTE_NP_ALLOWED_PORT_TYPES: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4104
IAS_ATTRIBUTE_NP_AUTHENTICATION_TYPE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4105
IAS_ATTRIBUTE_NP_ALLOWED_EAP_TYPE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4106
IAS_ATTRIBUTE_SHARED_SECRET: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4107
IAS_ATTRIBUTE_CLIENT_IP_ADDRESS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4108
IAS_ATTRIBUTE_CLIENT_PACKET_HEADER: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4109
IAS_ATTRIBUTE_TOKEN_GROUPS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4110
IAS_ATTRIBUTE_ALLOW_DIALIN: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4111
IAS_ATTRIBUTE_REQUEST_ID: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4112
IAS_ATTRIBUTE_MANIPULATION_TARGET: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4113
IAS_ATTRIBUTE_MANIPULATION_RULE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4114
IAS_ATTRIBUTE_ORIGINAL_USER_NAME: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4115
IAS_ATTRIBUTE_CLIENT_VENDOR_TYPE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4116
IAS_ATTRIBUTE_CLIENT_UDP_PORT: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4117
MS_ATTRIBUTE_CHAP_CHALLENGE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4118
MS_ATTRIBUTE_CHAP_RESPONSE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4119
MS_ATTRIBUTE_CHAP_DOMAIN: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4120
MS_ATTRIBUTE_CHAP_ERROR: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4121
MS_ATTRIBUTE_CHAP_CPW1: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4122
MS_ATTRIBUTE_CHAP_CPW2: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4123
MS_ATTRIBUTE_CHAP_LM_ENC_PW: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4124
MS_ATTRIBUTE_CHAP_NT_ENC_PW: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4125
MS_ATTRIBUTE_CHAP_MPPE_KEYS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4126
IAS_ATTRIBUTE_AUTHENTICATION_TYPE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4127
IAS_ATTRIBUTE_CLIENT_NAME: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4128
IAS_ATTRIBUTE_NT4_ACCOUNT_NAME: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4129
IAS_ATTRIBUTE_FULLY_QUALIFIED_USER_NAME: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4130
IAS_ATTRIBUTE_NTGROUPS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4131
IAS_ATTRIBUTE_EAP_FRIENDLY_NAME: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4132
IAS_ATTRIBUTE_AUTH_PROVIDER_TYPE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4133
MS_ATTRIBUTE_ACCT_AUTH_TYPE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4134
MS_ATTRIBUTE_ACCT_EAP_TYPE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4135
IAS_ATTRIBUTE_PACKET_TYPE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4136
IAS_ATTRIBUTE_AUTH_PROVIDER_NAME: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4137
IAS_ATTRIBUTE_ACCT_PROVIDER_TYPE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4138
IAS_ATTRIBUTE_ACCT_PROVIDER_NAME: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4139
MS_ATTRIBUTE_MPPE_SEND_KEY: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4140
MS_ATTRIBUTE_MPPE_RECV_KEY: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4141
IAS_ATTRIBUTE_REASON_CODE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4142
MS_ATTRIBUTE_FILTER: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4143
MS_ATTRIBUTE_CHAP2_RESPONSE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4144
MS_ATTRIBUTE_CHAP2_SUCCESS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4145
MS_ATTRIBUTE_CHAP2_CPW: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4146
MS_ATTRIBUTE_RAS_VENDOR: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4147
MS_ATTRIBUTE_RAS_VERSION: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4148
IAS_ATTRIBUTE_NP_NAME: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4149
MS_ATTRIBUTE_PRIMARY_DNS_SERVER: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4150
MS_ATTRIBUTE_SECONDARY_DNS_SERVER: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4151
MS_ATTRIBUTE_PRIMARY_NBNS_SERVER: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4152
MS_ATTRIBUTE_SECONDARY_NBNS_SERVER: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4153
IAS_ATTRIBUTE_PROXY_POLICY_NAME: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4154
IAS_ATTRIBUTE_PROVIDER_TYPE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4155
IAS_ATTRIBUTE_PROVIDER_NAME: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4156
IAS_ATTRIBUTE_REMOTE_SERVER_ADDRESS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4157
IAS_ATTRIBUTE_GENERATE_CLASS_ATTRIBUTE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4158
MS_ATTRIBUTE_RAS_CLIENT_NAME: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4159
MS_ATTRIBUTE_RAS_CLIENT_VERSION: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4160
IAS_ATTRIBUTE_ALLOWED_CERTIFICATE_EKU: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4161
IAS_ATTRIBUTE_EXTENSION_STATE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4162
IAS_ATTRIBUTE_GENERATE_SESSION_TIMEOUT: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4163
IAS_ATTRIBUTE_SESSION_TIMEOUT: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4164
MS_ATTRIBUTE_QUARANTINE_IPFILTER: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4165
MS_ATTRIBUTE_QUARANTINE_SESSION_TIMEOUT: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4166
MS_ATTRIBUTE_USER_SECURITY_IDENTITY: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4167
IAS_ATTRIBUTE_REMOTE_RADIUS_TO_WINDOWS_USER_MAPPING: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4168
IAS_ATTRIBUTE_PASSPORT_USER_MAPPING_UPN_SUFFIX: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4169
IAS_ATTRIBUTE_TUNNEL_TAG: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4170
IAS_ATTRIBUTE_NP_PEAPUPFRONT_ENABLED: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4171
IAS_ATTRIBUTE_CERTIFICATE_EKU: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8097
IAS_ATTRIBUTE_EAP_CONFIG: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8098
IAS_ATTRIBUTE_PEAP_EMBEDDED_EAP_TYPEID: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8099
IAS_ATTRIBUTE_PEAP_FAST_ROAMED_SESSION: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8100
IAS_ATTRIBUTE_EAP_TYPEID: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8101
MS_ATTRIBUTE_EAP_TLV: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8102
IAS_ATTRIBUTE_REJECT_REASON_CODE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8103
IAS_ATTRIBUTE_PROXY_EAP_CONFIG: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8104
IAS_ATTRIBUTE_EAP_SESSION: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8105
IAS_ATTRIBUTE_IS_REPLAY: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8106
IAS_ATTRIBUTE_CLEAR_TEXT_PASSWORD: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8107
MS_ATTRIBUTE_IDENTITY_TYPE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8108
MS_ATTRIBUTE_SERVICE_CLASS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8109
MS_ATTRIBUTE_QUARANTINE_USER_CLASS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8110
MS_ATTRIBUTE_QUARANTINE_STATE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8111
IAS_ATTRIBUTE_OVERRIDE_RAP_AUTH: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8112
IAS_ATTRIBUTE_PEAP_CHANNEL_UP: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8113
IAS_ATTRIBUTE_NAME_MAPPED: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8114
IAS_ATTRIBUTE_POLICY_ENFORCED: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8115
IAS_ATTRIBUTE_MACHINE_NTGROUPS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8116
IAS_ATTRIBUTE_USER_NTGROUPS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8117
IAS_ATTRIBUTE_MACHINE_TOKEN_GROUPS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8118
IAS_ATTRIBUTE_USER_TOKEN_GROUPS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8119
MS_ATTRIBUTE_QUARANTINE_GRACE_TIME: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8120
IAS_ATTRIBUTE_QUARANTINE_URL: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8121
IAS_ATTRIBUTE_QUARANTINE_FIXUP_SERVERS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8122
MS_ATTRIBUTE_NOT_QUARANTINE_CAPABLE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8123
IAS_ATTRIBUTE_QUARANTINE_SYSTEM_HEALTH_RESULT: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8124
IAS_ATTRIBUTE_QUARANTINE_SYSTEM_HEALTH_VALIDATORS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8125
IAS_ATTRIBUTE_MACHINE_NAME: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8126
IAS_ATTRIBUTE_NT4_MACHINE_NAME: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8127
IAS_ATTRIBUTE_QUARANTINE_SESSION_HANDLE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8128
IAS_ATTRIBUTE_FULLY_QUALIFIED_MACHINE_NAME: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8129
IAS_ATTRIBUTE_QUARANTINE_FIXUP_SERVERS_CONFIGURATION: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8130
IAS_ATTRIBUTE_CLIENT_QUARANTINE_COMPATIBLE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8131
MS_ATTRIBUTE_NETWORK_ACCESS_SERVER_TYPE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8132
IAS_ATTRIBUTE_QUARANTINE_SESSION_ID: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8133
MS_ATTRIBUTE_AFW_QUARANTINE_ZONE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8134
MS_ATTRIBUTE_AFW_PROTECTION_LEVEL: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8135
IAS_ATTRIBUTE_QUARANTINE_UPDATE_NON_COMPLIANT: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8136
IAS_ATTRIBUTE_REQUEST_START_TIME: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8137
MS_ATTRIBUTE_MACHINE_NAME: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8138
IAS_ATTRIBUTE_CLIENT_IPv6_ADDRESS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8139
IAS_ATTRIBUTE_SAVED_RADIUS_FRAMED_INTERFACE_ID: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8140
IAS_ATTRIBUTE_SAVED_RADIUS_FRAMED_IPv6_PREFIX: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8141
IAS_ATTRIBUTE_SAVED_RADIUS_FRAMED_IPv6_ROUTE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8142
MS_ATTRIBUTE_QUARANTINE_GRACE_TIME_CONFIGURATION: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8143
MS_ATTRIBUTE_IPv6_FILTER: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8144
MS_ATTRIBUTE_IPV4_REMEDIATION_SERVERS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8145
MS_ATTRIBUTE_IPV6_REMEDIATION_SERVERS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8146
IAS_ATTRIBUTE_PROXY_RETRY_COUNT: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8147
IAS_ATTRIBUTE_MACHINE_INVENTORY: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8148
IAS_ATTRIBUTE_ABSOLUTE_TIME: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8149
MS_ATTRIBUTE_QUARANTINE_SOH: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8150
IAS_ATTRIBUTE_EAP_TYPES_CONFIGURED_IN_PROXYPOLICY: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8151
MS_ATTRIBUTE_HCAP_LOCATION_GROUP_NAME: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8152
MS_ATTRIBUTE_EXTENDED_QUARANTINE_STATE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8153
IAS_ATTRIBUTE_SOH_CARRIER_EAPTLV: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8154
MS_ATTRIBUTE_HCAP_USER_GROUPS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8155
IAS_ATTRIBUTE_SAVED_MACHINE_HEALTHCHECK_ONLY: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8156
IAS_ATTRIBUTE_POLICY_EVALUATED_SHV: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8157
MS_ATTRIBUTE_RAS_CORRELATION_ID: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8158
MS_ATTRIBUTE_HCAP_USER_NAME: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8159
IAS_ATTRIBUTE_NT4_HCAP_ACCOUNT_NAME: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8160
IAS_ATTRIBUTE_USER_TOKEN_SID: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8161
IAS_ATTRIBUTE_MACHINE_TOKEN_SID: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8162
IAS_ATTRIBUTE_MACHINE_VALIDATED: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8163
MS_ATTRIBUTE_USER_IPv4_ADDRESS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8164
MS_ATTRIBUTE_USER_IPv6_ADDRESS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8165
MS_ATTRIBUTE_TSG_DEVICE_REDIRECTION: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8166
IAS_ATTRIBUTE_ACCEPT_REASON_CODE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8167
IAS_ATTRIBUTE_LOGGING_RESULT: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8168
IAS_ATTRIBUTE_SERVER_IP_ADDRESS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8169
IAS_ATTRIBUTE_SERVER_IPv6_ADDRESS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8170
IAS_ATTRIBUTE_RADIUS_USERNAME_ENCODING_ASCII: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8171
MS_ATTRIBUTE_RAS_ROUTING_DOMAIN_ID: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8172
MS_ATTRIBUTE_AZURE_POLICY_ID: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8173
IAS_ATTRIBUTE_CERTIFICATE_THUMBPRINT: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 8250
RAS_ATTRIBUTE_ENCRYPTION_TYPE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4294967206
RAS_ATTRIBUTE_ENCRYPTION_POLICY: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4294967207
RAS_ATTRIBUTE_BAP_REQUIRED: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4294967208
RAS_ATTRIBUTE_BAP_LINE_DOWN_TIME: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4294967209
RAS_ATTRIBUTE_BAP_LINE_DOWN_LIMIT: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID = 4294967210
ATTRIBUTEINFO = Int32
NAME: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEINFO = 1
SYNTAX: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEINFO = 2
RESTRICTIONS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEINFO = 3
DESCRIPTION: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEINFO = 4
VENDORID: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEINFO = 5
LDAPNAME: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEINFO = 6
VENDORTYPE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEINFO = 7
ATTRIBUTEPROPERTIES = Int32
PROPERTY_ATTRIBUTE_ID: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEPROPERTIES = 1024
PROPERTY_ATTRIBUTE_VENDOR_ID: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEPROPERTIES = 1025
PROPERTY_ATTRIBUTE_VENDOR_TYPE_ID: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEPROPERTIES = 1026
PROPERTY_ATTRIBUTE_IS_ENUMERABLE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEPROPERTIES = 1027
PROPERTY_ATTRIBUTE_ENUM_NAMES: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEPROPERTIES = 1028
PROPERTY_ATTRIBUTE_ENUM_VALUES: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEPROPERTIES = 1029
PROPERTY_ATTRIBUTE_SYNTAX: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEPROPERTIES = 1030
PROPERTY_ATTRIBUTE_ALLOW_MULTIPLE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEPROPERTIES = 1031
PROPERTY_ATTRIBUTE_ALLOW_LOG_ORDINAL: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEPROPERTIES = 1032
PROPERTY_ATTRIBUTE_ALLOW_IN_PROFILE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEPROPERTIES = 1033
PROPERTY_ATTRIBUTE_ALLOW_IN_CONDITION: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEPROPERTIES = 1034
PROPERTY_ATTRIBUTE_DISPLAY_NAME: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEPROPERTIES = 1035
PROPERTY_ATTRIBUTE_VALUE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEPROPERTIES = 1036
PROPERTY_ATTRIBUTE_ALLOW_IN_PROXY_PROFILE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEPROPERTIES = 1037
PROPERTY_ATTRIBUTE_ALLOW_IN_PROXY_CONDITION: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEPROPERTIES = 1038
PROPERTY_ATTRIBUTE_ALLOW_IN_VPNDIALUP: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEPROPERTIES = 1039
PROPERTY_ATTRIBUTE_ALLOW_IN_8021X: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEPROPERTIES = 1040
PROPERTY_ATTRIBUTE_ENUM_FILTERS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEPROPERTIES = 1041
ATTRIBUTERESTRICTIONS = Int32
MULTIVALUED: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTERESTRICTIONS = 1
ALLOWEDINPROFILE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTERESTRICTIONS = 2
ALLOWEDINCONDITION: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTERESTRICTIONS = 4
ALLOWEDINPROXYPROFILE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTERESTRICTIONS = 8
ALLOWEDINPROXYCONDITION: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTERESTRICTIONS = 16
ALLOWEDINVPNDIALUP: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTERESTRICTIONS = 32
ALLOWEDIN8021X: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTERESTRICTIONS = 64
ATTRIBUTESYNTAX = Int32
IAS_SYNTAX_BOOLEAN: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTESYNTAX = 1
IAS_SYNTAX_INTEGER: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTESYNTAX = 2
IAS_SYNTAX_ENUMERATOR: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTESYNTAX = 3
IAS_SYNTAX_INETADDR: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTESYNTAX = 4
IAS_SYNTAX_STRING: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTESYNTAX = 5
IAS_SYNTAX_OCTETSTRING: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTESYNTAX = 6
IAS_SYNTAX_UTCTIME: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTESYNTAX = 7
IAS_SYNTAX_PROVIDERSPECIFIC: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTESYNTAX = 8
IAS_SYNTAX_UNSIGNEDINTEGER: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTESYNTAX = 9
IAS_SYNTAX_INETADDR6: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTESYNTAX = 10
AUTHENTICATION_TYPE = Int32
IAS_AUTH_INVALID: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.AUTHENTICATION_TYPE = 0
IAS_AUTH_PAP: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.AUTHENTICATION_TYPE = 1
IAS_AUTH_MD5CHAP: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.AUTHENTICATION_TYPE = 2
IAS_AUTH_MSCHAP: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.AUTHENTICATION_TYPE = 3
IAS_AUTH_MSCHAP2: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.AUTHENTICATION_TYPE = 4
IAS_AUTH_EAP: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.AUTHENTICATION_TYPE = 5
IAS_AUTH_ARAP: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.AUTHENTICATION_TYPE = 6
IAS_AUTH_NONE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.AUTHENTICATION_TYPE = 7
IAS_AUTH_CUSTOM: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.AUTHENTICATION_TYPE = 8
IAS_AUTH_MSCHAP_CPW: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.AUTHENTICATION_TYPE = 9
IAS_AUTH_MSCHAP2_CPW: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.AUTHENTICATION_TYPE = 10
IAS_AUTH_PEAP: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.AUTHENTICATION_TYPE = 11
RADIUS_EXTENSION_INIT: String = 'RadiusExtensionInit'
RADIUS_EXTENSION_TERM: String = 'RadiusExtensionTerm'
RADIUS_EXTENSION_PROCESS: String = 'RadiusExtensionProcess'
RADIUS_EXTENSION_PROCESS_EX: String = 'RadiusExtensionProcessEx'
RADIUS_EXTENSION_FREE_ATTRIBUTES: String = 'RadiusExtensionFreeAttributes'
AUTHSRV_PARAMETERS_KEY_W: String = 'System\\CurrentControlSet\\Services\\AuthSrv\\Parameters'
AUTHSRV_EXTENSIONS_VALUE_W: String = 'ExtensionDLLs'
AUTHSRV_AUTHORIZATION_VALUE_W: String = 'AuthorizationDLLs'
AUTHSRV_ENFORCE_NP_FOR_PAP_CHALLENGE_RESPONSE_VALUE_W: String = 'EnforceNetworkPolicyForPAPBasedChallengeResponse'
RADIUS_EXTENSION_VERSION: UInt32 = 1
RADIUS_EXTENSION_PROCESS2: String = 'RadiusExtensionProcess2'
CLIENTPROPERTIES = Int32
PROPERTY_CLIENT_REQUIRE_SIGNATURE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.CLIENTPROPERTIES = 1024
PROPERTY_CLIENT_UNUSED: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.CLIENTPROPERTIES = 1025
PROPERTY_CLIENT_SHARED_SECRET: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.CLIENTPROPERTIES = 1026
PROPERTY_CLIENT_NAS_MANUFACTURER: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.CLIENTPROPERTIES = 1027
PROPERTY_CLIENT_ADDRESS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.CLIENTPROPERTIES = 1028
PROPERTY_CLIENT_QUARANTINE_COMPATIBLE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.CLIENTPROPERTIES = 1029
PROPERTY_CLIENT_ENABLED: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.CLIENTPROPERTIES = 1030
PROPERTY_CLIENT_SECRET_TEMPLATE_GUID: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.CLIENTPROPERTIES = 1031
CONDITIONPROPERTIES = Int32
PROPERTY_CONDITION_TEXT: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.CONDITIONPROPERTIES = 1024
DICTIONARYPROPERTIES = Int32
PROPERTY_DICTIONARY_ATTRIBUTES_COLLECTION: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.DICTIONARYPROPERTIES = 1024
PROPERTY_DICTIONARY_LOCATION: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.DICTIONARYPROPERTIES = 1025
IASCOMMONPROPERTIES = Int32
PROPERTY_SDO_RESERVED: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.IASCOMMONPROPERTIES = 0
PROPERTY_SDO_CLASS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.IASCOMMONPROPERTIES = 1
PROPERTY_SDO_NAME: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.IASCOMMONPROPERTIES = 2
PROPERTY_SDO_DESCRIPTION: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.IASCOMMONPROPERTIES = 3
PROPERTY_SDO_ID: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.IASCOMMONPROPERTIES = 4
PROPERTY_SDO_DATASTORE_NAME: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.IASCOMMONPROPERTIES = 5
PROPERTY_SDO_TEMPLATE_GUID: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.IASCOMMONPROPERTIES = 6
PROPERTY_SDO_OPAQUE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.IASCOMMONPROPERTIES = 7
PROPERTY_SDO_START: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.IASCOMMONPROPERTIES = 1024
IASCOMPONENTPROPERTIES = Int32
PROPERTY_COMPONENT_ID: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.IASCOMPONENTPROPERTIES = 1024
PROPERTY_COMPONENT_PROG_ID: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.IASCOMPONENTPROPERTIES = 1025
PROPERTY_COMPONENT_START: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.IASCOMPONENTPROPERTIES = 1026
IASDATASTORE = Int32
DATA_STORE_LOCAL: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.IASDATASTORE = 0
DATA_STORE_DIRECTORY: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.IASDATASTORE = 1
IASDOMAINTYPE = Int32
DOMAIN_TYPE_NONE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.IASDOMAINTYPE = 0
DOMAIN_TYPE_NT4: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.IASDOMAINTYPE = 1
DOMAIN_TYPE_NT5: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.IASDOMAINTYPE = 2
DOMAIN_TYPE_MIXED: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.IASDOMAINTYPE = 3
IASOSTYPE = Int32
SYSTEM_TYPE_NT4_WORKSTATION: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.IASOSTYPE = 0
SYSTEM_TYPE_NT5_WORKSTATION: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.IASOSTYPE = 1
SYSTEM_TYPE_NT6_WORKSTATION: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.IASOSTYPE = 2
SYSTEM_TYPE_NT6_1_WORKSTATION: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.IASOSTYPE = 3
SYSTEM_TYPE_NT6_2_WORKSTATION: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.IASOSTYPE = 4
SYSTEM_TYPE_NT6_3_WORKSTATION: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.IASOSTYPE = 5
SYSTEM_TYPE_NT10_0_WORKSTATION: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.IASOSTYPE = 6
SYSTEM_TYPE_NT4_SERVER: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.IASOSTYPE = 7
SYSTEM_TYPE_NT5_SERVER: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.IASOSTYPE = 8
SYSTEM_TYPE_NT6_SERVER: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.IASOSTYPE = 9
SYSTEM_TYPE_NT6_1_SERVER: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.IASOSTYPE = 10
SYSTEM_TYPE_NT6_2_SERVER: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.IASOSTYPE = 11
SYSTEM_TYPE_NT6_3_SERVER: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.IASOSTYPE = 12
SYSTEM_TYPE_NT10_0_SERVER: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.IASOSTYPE = 13
IASPROPERTIES = Int32
PROPERTY_IAS_RADIUSSERVERGROUPS_COLLECTION: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.IASPROPERTIES = 1024
PROPERTY_IAS_POLICIES_COLLECTION: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.IASPROPERTIES = 1025
PROPERTY_IAS_PROFILES_COLLECTION: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.IASPROPERTIES = 1026
PROPERTY_IAS_PROTOCOLS_COLLECTION: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.IASPROPERTIES = 1027
PROPERTY_IAS_AUDITORS_COLLECTION: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.IASPROPERTIES = 1028
PROPERTY_IAS_REQUESTHANDLERS_COLLECTION: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.IASPROPERTIES = 1029
PROPERTY_IAS_PROXYPOLICIES_COLLECTION: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.IASPROPERTIES = 1030
PROPERTY_IAS_PROXYPROFILES_COLLECTION: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.IASPROPERTIES = 1031
PROPERTY_IAS_REMEDIATIONSERVERGROUPS_COLLECTION: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.IASPROPERTIES = 1032
PROPERTY_IAS_SHVTEMPLATES_COLLECTION: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.IASPROPERTIES = 1033
IDENTITY_TYPE = Int32
IAS_IDENTITY_NO_DEFAULT: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.IDENTITY_TYPE = 1
IPFILTERPROPERTIES = Int32
PROPERTY_IPFILTER_ATTRIBUTES_COLLECTION: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.IPFILTERPROPERTIES = 1024
class ISdo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{56bc53de-96db-11d1-bf3f-000000000000}')
    @commethod(7)
    def GetPropertyInfo(self, Id: Int32, ppPropertyInfo: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetProperty(self, Id: Int32, pValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def PutProperty(self, Id: Int32, pValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def ResetProperty(self, Id: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Apply(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Restore(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get__NewEnum(self, ppEnumVARIANT: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISdoCollection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{56bc53e2-96db-11d1-bf3f-000000000000}')
    @commethod(7)
    def get_Count(self, pCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Add(self, bstrName: win32more.Windows.Win32.Foundation.BSTR, ppItem: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Remove(self, pItem: win32more.Windows.Win32.System.Com.IDispatch) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def RemoveAll(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Reload(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def IsNameUnique(self, bstrName: win32more.Windows.Win32.Foundation.BSTR, pBool: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Item(self, Name: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pItem: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get__NewEnum(self, ppEnumVARIANT: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISdoDictionaryOld(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{d432e5f4-53d8-11d2-9a3a-00c04fb998ac}')
    @commethod(7)
    def EnumAttributes(self, Id: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pValues: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetAttributeInfo(self, Id: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID, pInfoIDs: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pInfoValues: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def EnumAttributeValues(self, Id: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID, pValueIds: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pValuesDesc: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def CreateAttribute(self, Id: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID, ppAttributeObject: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetAttributeID(self, bstrAttributeName: win32more.Windows.Win32.Foundation.BSTR, pId: POINTER(win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ATTRIBUTEID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISdoMachine(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{479f6e75-49a2-11d2-8eca-00c04fc2f519}')
    @commethod(7)
    def Attach(self, bstrComputerName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetDictionarySDO(self, ppDictionarySDO: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetServiceSDO(self, eDataStore: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.IASDATASTORE, bstrServiceName: win32more.Windows.Win32.Foundation.BSTR, ppServiceSDO: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetUserSDO(self, eDataStore: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.IASDATASTORE, bstrUserName: win32more.Windows.Win32.Foundation.BSTR, ppUserSDO: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetOSType(self, eOSType: POINTER(win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.IASOSTYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetDomainType(self, eDomainType: POINTER(win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.IASDOMAINTYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def IsDirectoryAvailable(self, boolDirectoryAvailable: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetAttachedComputer(self, bstrComputerName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetSDOSchema(self, ppSDOSchema: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISdoMachine2(ComPtr):
    extends: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ISdoMachine
    _iid_ = Guid('{518e5ffe-d8ce-4f7e-a5db-b40a35419d3b}')
    @commethod(16)
    def GetTemplatesSDO(self, bstrServiceName: win32more.Windows.Win32.Foundation.BSTR, ppTemplatesSDO: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def EnableTemplates(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SyncConfigAgainstTemplates(self, bstrServiceName: win32more.Windows.Win32.Foundation.BSTR, ppConfigRoot: POINTER(win32more.Windows.Win32.System.Com.IUnknown), ppTemplatesRoot: POINTER(win32more.Windows.Win32.System.Com.IUnknown), bForcedSync: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def ImportRemoteTemplates(self, pLocalTemplatesRoot: win32more.Windows.Win32.System.Com.IUnknown, bstrRemoteMachineName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def Reload(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISdoServiceControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{479f6e74-49a2-11d2-8eca-00c04fc2f519}')
    @commethod(7)
    def StartService(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def StopService(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetServiceStatus(self, status: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def ResetService(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITemplateSdo(ComPtr):
    extends: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.ISdo
    _iid_ = Guid('{8aa85302-d2e2-4e20-8b1f-a571e437d6c9}')
    @commethod(14)
    def AddToCollection(self, bstrName: win32more.Windows.Win32.Foundation.BSTR, pCollection: win32more.Windows.Win32.System.Com.IDispatch, ppItem: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def AddToSdo(self, bstrName: win32more.Windows.Win32.Foundation.BSTR, pSdoTarget: win32more.Windows.Win32.System.Com.IDispatch, ppItem: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def AddToSdoAsProperty(self, pSdoTarget: win32more.Windows.Win32.System.Com.IDispatch, id: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
NAMESPROPERTIES = Int32
PROPERTY_NAMES_REALMS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.NAMESPROPERTIES = 1026
NAPPROPERTIES = Int32
PROPERTY_NAP_POLICIES_COLLECTION: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.NAPPROPERTIES = 1026
PROPERTY_SHV_TEMPLATES_COLLECTION: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.NAPPROPERTIES = 1027
NEW_LOG_FILE_FREQUENCY = Int32
IAS_LOGGING_UNLIMITED_SIZE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.NEW_LOG_FILE_FREQUENCY = 0
IAS_LOGGING_DAILY: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.NEW_LOG_FILE_FREQUENCY = 1
IAS_LOGGING_WEEKLY: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.NEW_LOG_FILE_FREQUENCY = 2
IAS_LOGGING_MONTHLY: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.NEW_LOG_FILE_FREQUENCY = 3
IAS_LOGGING_WHEN_FILE_SIZE_REACHES: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.NEW_LOG_FILE_FREQUENCY = 4
NTEVENTLOGPROPERTIES = Int32
PROPERTY_EVENTLOG_LOG_APPLICATION_EVENTS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.NTEVENTLOGPROPERTIES = 1026
PROPERTY_EVENTLOG_LOG_MALFORMED: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.NTEVENTLOGPROPERTIES = 1027
PROPERTY_EVENTLOG_LOG_DEBUG: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.NTEVENTLOGPROPERTIES = 1028
NTSAMPROPERTIES = Int32
PROPERTY_NTSAM_ALLOW_LM_AUTHENTICATION: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.NTSAMPROPERTIES = 1026
POLICYPROPERTIES = Int32
PROPERTY_POLICY_CONSTRAINT: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.POLICYPROPERTIES = 1024
PROPERTY_POLICY_MERIT: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.POLICYPROPERTIES = 1025
PROPERTY_POLICY_UNUSED0: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.POLICYPROPERTIES = 1026
PROPERTY_POLICY_UNUSED1: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.POLICYPROPERTIES = 1027
PROPERTY_POLICY_PROFILE_NAME: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.POLICYPROPERTIES = 1028
PROPERTY_POLICY_ACTION: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.POLICYPROPERTIES = 1029
PROPERTY_POLICY_CONDITIONS_COLLECTION: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.POLICYPROPERTIES = 1030
PROPERTY_POLICY_ENABLED: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.POLICYPROPERTIES = 1031
PROPERTY_POLICY_SOURCETAG: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.POLICYPROPERTIES = 1032
@winfunctype_pointer
def PRADIUS_EXTENSION_FREE_ATTRIBUTES(pAttrs: POINTER(win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE)) -> Void: ...
@winfunctype_pointer
def PRADIUS_EXTENSION_INIT() -> UInt32: ...
@winfunctype_pointer
def PRADIUS_EXTENSION_PROCESS(pAttrs: POINTER(win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE), pfAction: POINTER(win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ACTION)) -> UInt32: ...
@winfunctype_pointer
def PRADIUS_EXTENSION_PROCESS_2(pECB: POINTER(win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_EXTENSION_CONTROL_BLOCK)) -> UInt32: ...
@winfunctype_pointer
def PRADIUS_EXTENSION_PROCESS_EX(pInAttrs: POINTER(win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE), pOutAttrs: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE)), pfAction: POINTER(win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ACTION)) -> UInt32: ...
@winfunctype_pointer
def PRADIUS_EXTENSION_TERM() -> Void: ...
PROFILEPROPERTIES = Int32
PROPERTY_PROFILE_ATTRIBUTES_COLLECTION: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.PROFILEPROPERTIES = 1024
PROPERTY_PROFILE_IPFILTER_TEMPLATE_GUID: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.PROFILEPROPERTIES = 1025
PROTOCOLPROPERTIES = Int32
PROPERTY_PROTOCOL_REQUEST_HANDLER: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.PROTOCOLPROPERTIES = 1026
PROPERTY_PROTOCOL_START: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.PROTOCOLPROPERTIES = 1027
RADIUSPROPERTIES = Int32
PROPERTY_RADIUS_ACCOUNTING_PORT: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUSPROPERTIES = 1027
PROPERTY_RADIUS_AUTHENTICATION_PORT: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUSPROPERTIES = 1028
PROPERTY_RADIUS_CLIENTS_COLLECTION: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUSPROPERTIES = 1029
PROPERTY_RADIUS_VENDORS_COLLECTION: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUSPROPERTIES = 1030
RADIUSPROXYPROPERTIES = Int32
PROPERTY_RADIUSPROXY_SERVERGROUPS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUSPROXYPROPERTIES = 1026
RADIUSSERVERGROUPPROPERTIES = Int32
PROPERTY_RADIUSSERVERGROUP_SERVERS_COLLECTION: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUSSERVERGROUPPROPERTIES = 1024
RADIUSSERVERPROPERTIES = Int32
PROPERTY_RADIUSSERVER_AUTH_PORT: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUSSERVERPROPERTIES = 1024
PROPERTY_RADIUSSERVER_AUTH_SECRET: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUSSERVERPROPERTIES = 1025
PROPERTY_RADIUSSERVER_ACCT_PORT: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUSSERVERPROPERTIES = 1026
PROPERTY_RADIUSSERVER_ACCT_SECRET: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUSSERVERPROPERTIES = 1027
PROPERTY_RADIUSSERVER_ADDRESS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUSSERVERPROPERTIES = 1028
PROPERTY_RADIUSSERVER_FORWARD_ACCT_ONOFF: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUSSERVERPROPERTIES = 1029
PROPERTY_RADIUSSERVER_PRIORITY: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUSSERVERPROPERTIES = 1030
PROPERTY_RADIUSSERVER_WEIGHT: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUSSERVERPROPERTIES = 1031
PROPERTY_RADIUSSERVER_TIMEOUT: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUSSERVERPROPERTIES = 1032
PROPERTY_RADIUSSERVER_MAX_LOST: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUSSERVERPROPERTIES = 1033
PROPERTY_RADIUSSERVER_BLACKOUT: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUSSERVERPROPERTIES = 1034
PROPERTY_RADIUSSERVER_SEND_SIGNATURE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUSSERVERPROPERTIES = 1035
PROPERTY_RADIUSSERVER_AUTH_SECRET_TEMPLATE_GUID: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUSSERVERPROPERTIES = 1036
PROPERTY_RADIUSSERVER_ACCT_SECRET_TEMPLATE_GUID: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUSSERVERPROPERTIES = 1037
RADIUS_ACTION = Int32
raContinue: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ACTION = 0
raReject: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ACTION = 1
raAccept: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ACTION = 2
class RADIUS_ATTRIBUTE(Structure):
    dwAttrType: UInt32
    fDataType: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_DATA_TYPE
    cbDataLength: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        dwValue: UInt32
        lpValue: POINTER(Byte)
class RADIUS_ATTRIBUTE_ARRAY(Structure):
    cbSize: UInt32
    Add: IntPtr
    AttributeAt: IntPtr
    GetSize: IntPtr
    InsertAt: IntPtr
    RemoveAt: IntPtr
    SetAt: IntPtr
RADIUS_ATTRIBUTE_TYPE = Int32
ratMinimum: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 0
ratUserName: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 1
ratUserPassword: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 2
ratCHAPPassword: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 3
ratNASIPAddress: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 4
ratNASPort: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 5
ratServiceType: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 6
ratFramedProtocol: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 7
ratFramedIPAddress: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 8
ratFramedIPNetmask: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 9
ratFramedRouting: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 10
ratFilterId: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 11
ratFramedMTU: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 12
ratFramedCompression: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 13
ratLoginIPHost: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 14
ratLoginService: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 15
ratLoginPort: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 16
ratReplyMessage: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 18
ratCallbackNumber: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 19
ratCallbackId: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 20
ratFramedRoute: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 22
ratFramedIPXNetwork: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 23
ratState: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 24
ratClass: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 25
ratVendorSpecific: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 26
ratSessionTimeout: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 27
ratIdleTimeout: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 28
ratTerminationAction: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 29
ratCalledStationId: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 30
ratCallingStationId: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 31
ratNASIdentifier: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 32
ratProxyState: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 33
ratLoginLATService: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 34
ratLoginLATNode: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 35
ratLoginLATGroup: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 36
ratFramedAppleTalkLink: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 37
ratFramedAppleTalkNetwork: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 38
ratFramedAppleTalkZone: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 39
ratAcctStatusType: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 40
ratAcctDelayTime: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 41
ratAcctInputOctets: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 42
ratAcctOutputOctets: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 43
ratAcctSessionId: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 44
ratAcctAuthentic: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 45
ratAcctSessionTime: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 46
ratAcctInputPackets: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 47
ratAcctOutputPackets: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 48
ratAcctTerminationCause: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 49
ratCHAPChallenge: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 60
ratNASPortType: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 61
ratPortLimit: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 62
ratTunnelType: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 64
ratMediumType: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 65
ratTunnelPassword: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 69
ratTunnelPrivateGroupID: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 81
ratNASIPv6Address: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 95
ratFramedInterfaceId: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 96
ratFramedIPv6Prefix: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 97
ratLoginIPv6Host: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 98
ratFramedIPv6Route: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 99
ratFramedIPv6Pool: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 100
ratCode: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 262
ratIdentifier: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 263
ratAuthenticator: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 264
ratSrcIPAddress: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 265
ratSrcPort: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 266
ratProvider: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 267
ratStrippedUserName: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 268
ratFQUserName: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 269
ratPolicyName: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 270
ratUniqueId: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 271
ratExtensionState: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 272
ratEAPTLV: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 273
ratRejectReasonCode: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 274
ratCRPPolicyName: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 275
ratProviderName: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 276
ratClearTextPassword: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 277
ratSrcIPv6Address: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 278
ratCertificateThumbprint: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_ATTRIBUTE_TYPE = 279
RADIUS_AUTHENTICATION_PROVIDER = Int32
rapUnknown: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_AUTHENTICATION_PROVIDER = 0
rapUsersFile: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_AUTHENTICATION_PROVIDER = 1
rapProxy: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_AUTHENTICATION_PROVIDER = 2
rapWindowsNT: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_AUTHENTICATION_PROVIDER = 3
rapMCIS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_AUTHENTICATION_PROVIDER = 4
rapODBC: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_AUTHENTICATION_PROVIDER = 5
rapNone: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_AUTHENTICATION_PROVIDER = 6
RADIUS_CODE = Int32
rcUnknown: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_CODE = 0
rcAccessRequest: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_CODE = 1
rcAccessAccept: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_CODE = 2
rcAccessReject: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_CODE = 3
rcAccountingRequest: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_CODE = 4
rcAccountingResponse: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_CODE = 5
rcAccessChallenge: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_CODE = 11
rcDiscard: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_CODE = 256
RADIUS_DATA_TYPE = Int32
rdtUnknown: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_DATA_TYPE = 0
rdtString: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_DATA_TYPE = 1
rdtAddress: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_DATA_TYPE = 2
rdtInteger: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_DATA_TYPE = 3
rdtTime: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_DATA_TYPE = 4
rdtIpv6Address: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_DATA_TYPE = 5
class RADIUS_EXTENSION_CONTROL_BLOCK(Structure):
    cbSize: UInt32
    dwVersion: UInt32
    repPoint: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_EXTENSION_POINT
    rcRequestType: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_CODE
    rcResponseType: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_CODE
    GetRequest: IntPtr
    GetResponse: IntPtr
    SetResponseType: IntPtr
RADIUS_EXTENSION_POINT = Int32
repAuthentication: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_EXTENSION_POINT = 0
repAuthorization: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_EXTENSION_POINT = 1
RADIUS_REJECT_REASON_CODE = Int32
rrrcUndefined: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_REJECT_REASON_CODE = 0
rrrcAccountUnknown: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_REJECT_REASON_CODE = 1
rrrcAccountDisabled: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_REJECT_REASON_CODE = 2
rrrcAccountExpired: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_REJECT_REASON_CODE = 3
rrrcAuthenticationFailure: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.RADIUS_REJECT_REASON_CODE = 4
class RADIUS_VSA_FORMAT(Structure):
    VendorId: Byte * 4
    VendorType: Byte
    VendorLength: Byte
    AttributeSpecific: Byte * 1
REMEDIATIONSERVERGROUPPROPERTIES = Int32
PROPERTY_REMEDIATIONSERVERGROUP_SERVERS_COLLECTION: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.REMEDIATIONSERVERGROUPPROPERTIES = 1024
REMEDIATIONSERVERPROPERTIES = Int32
PROPERTY_REMEDIATIONSERVER_ADDRESS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.REMEDIATIONSERVERPROPERTIES = 1024
PROPERTY_REMEDIATIONSERVER_FRIENDLY_NAME: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.REMEDIATIONSERVERPROPERTIES = 1025
REMEDIATIONSERVERSPROPERTIES = Int32
PROPERTY_REMEDIATIONSERVERS_SERVERGROUPS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.REMEDIATIONSERVERSPROPERTIES = 1026
SERVICE_TYPE = Int32
SERVICE_TYPE_IAS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.SERVICE_TYPE = 0
SERVICE_TYPE_RAS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.SERVICE_TYPE = 1
SERVICE_TYPE_RAMGMTSVC: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.SERVICE_TYPE = 2
SERVICE_TYPE_MAX: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.SERVICE_TYPE = 3
SHAREDSECRETPROPERTIES = Int32
PROPERTY_SHAREDSECRET_STRING: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.SHAREDSECRETPROPERTIES = 1024
SHVTEMPLATEPROPERTIES = Int32
PROPERTY_SHV_COMBINATION_TYPE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.SHVTEMPLATEPROPERTIES = 1024
PROPERTY_SHV_LIST: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.SHVTEMPLATEPROPERTIES = 1025
PROPERTY_SHVCONFIG_LIST: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.SHVTEMPLATEPROPERTIES = 1026
SHV_COMBINATION_TYPE = Int32
SHV_COMBINATION_TYPE_ALL_PASS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.SHV_COMBINATION_TYPE = 0
SHV_COMBINATION_TYPE_ALL_FAIL: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.SHV_COMBINATION_TYPE = 1
SHV_COMBINATION_TYPE_ONE_OR_MORE_PASS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.SHV_COMBINATION_TYPE = 2
SHV_COMBINATION_TYPE_ONE_OR_MORE_FAIL: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.SHV_COMBINATION_TYPE = 3
SHV_COMBINATION_TYPE_ONE_OR_MORE_INFECTED: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.SHV_COMBINATION_TYPE = 4
SHV_COMBINATION_TYPE_ONE_OR_MORE_TRANSITIONAL: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.SHV_COMBINATION_TYPE = 5
SHV_COMBINATION_TYPE_ONE_OR_MORE_UNKNOWN: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.SHV_COMBINATION_TYPE = 6
SHV_COMBINATION_TYPE_MAX: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.SHV_COMBINATION_TYPE = 7
SdoMachine = Guid('{e9218ae7-9e91-11d1-bf60-0080c7846bc0}')
TEMPLATESPROPERTIES = Int32
PROPERTY_TEMPLATES_POLICIES_TEMPLATES: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.TEMPLATESPROPERTIES = 1024
PROPERTY_TEMPLATES_PROFILES_TEMPLATES: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.TEMPLATESPROPERTIES = 1025
PROPERTY_TEMPLATES_PROFILES_COLLECTION: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.TEMPLATESPROPERTIES = 1026
PROPERTY_TEMPLATES_PROXYPOLICIES_TEMPLATES: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.TEMPLATESPROPERTIES = 1027
PROPERTY_TEMPLATES_PROXYPROFILES_TEMPLATES: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.TEMPLATESPROPERTIES = 1028
PROPERTY_TEMPLATES_PROXYPROFILES_COLLECTION: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.TEMPLATESPROPERTIES = 1029
PROPERTY_TEMPLATES_REMEDIATIONSERVERGROUPS_TEMPLATES: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.TEMPLATESPROPERTIES = 1030
PROPERTY_TEMPLATES_SHVTEMPLATES_TEMPLATES: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.TEMPLATESPROPERTIES = 1031
PROPERTY_TEMPLATES_CLIENTS_TEMPLATES: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.TEMPLATESPROPERTIES = 1032
PROPERTY_TEMPLATES_RADIUSSERVERS_TEMPLATES: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.TEMPLATESPROPERTIES = 1033
PROPERTY_TEMPLATES_SHAREDSECRETS_TEMPLATES: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.TEMPLATESPROPERTIES = 1034
PROPERTY_TEMPLATES_IPFILTERS_TEMPLATES: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.TEMPLATESPROPERTIES = 1035
USERPROPERTIES = Int32
PROPERTY_USER_CALLING_STATION_ID: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.USERPROPERTIES = 1024
PROPERTY_USER_SAVED_CALLING_STATION_ID: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.USERPROPERTIES = 1025
PROPERTY_USER_RADIUS_CALLBACK_NUMBER: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.USERPROPERTIES = 1026
PROPERTY_USER_RADIUS_FRAMED_ROUTE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.USERPROPERTIES = 1027
PROPERTY_USER_RADIUS_FRAMED_IP_ADDRESS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.USERPROPERTIES = 1028
PROPERTY_USER_SAVED_RADIUS_CALLBACK_NUMBER: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.USERPROPERTIES = 1029
PROPERTY_USER_SAVED_RADIUS_FRAMED_ROUTE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.USERPROPERTIES = 1030
PROPERTY_USER_SAVED_RADIUS_FRAMED_IP_ADDRESS: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.USERPROPERTIES = 1031
PROPERTY_USER_ALLOW_DIALIN: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.USERPROPERTIES = 1032
PROPERTY_USER_SERVICE_TYPE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.USERPROPERTIES = 1033
PROPERTY_USER_RADIUS_FRAMED_IPV6_ROUTE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.USERPROPERTIES = 1034
PROPERTY_USER_SAVED_RADIUS_FRAMED_IPV6_ROUTE: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.USERPROPERTIES = 1035
PROPERTY_USER_RADIUS_FRAMED_INTERFACE_ID: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.USERPROPERTIES = 1036
PROPERTY_USER_SAVED_RADIUS_FRAMED_INTERFACE_ID: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.USERPROPERTIES = 1037
PROPERTY_USER_RADIUS_FRAMED_IPV6_PREFIX: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.USERPROPERTIES = 1038
PROPERTY_USER_SAVED_RADIUS_FRAMED_IPV6_PREFIX: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.USERPROPERTIES = 1039
VENDORPROPERTIES = Int32
PROPERTY_NAS_VENDOR_ID: win32more.Windows.Win32.NetworkManagement.NetworkPolicyServer.VENDORPROPERTIES = 1024


make_ready(__name__)
