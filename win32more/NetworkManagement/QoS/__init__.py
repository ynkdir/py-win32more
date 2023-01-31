from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.NetworkManagement.Ndis
import win32more.NetworkManagement.QoS
import win32more.Networking.WinSock
import win32more.System.IO
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
class ADDRESS_LIST_DESCRIPTOR(Structure):
    MediaType: UInt32
    AddressList: win32more.NetworkManagement.Ndis.NETWORK_ADDRESS_LIST
class ADSPEC(Structure):
    adspec_header: win32more.NetworkManagement.QoS.RsvpObjHdr
    adspec_body: win32more.NetworkManagement.QoS.IS_ADSPEC_BODY
class AD_GENERAL_PARAMS(Structure):
    IntServAwareHopCount: UInt32
    PathBandwidthEstimate: UInt32
    MinimumLatency: UInt32
    PathMTU: UInt32
    Flags: UInt32
class AD_GUARANTEED(Structure):
    CTotal: UInt32
    DTotal: UInt32
    CSum: UInt32
    DSum: UInt32
QOS_MAX_OBJECT_STRING_LENGTH: UInt32 = 256
QOS_TRAFFIC_GENERAL_ID_BASE: UInt32 = 4000
SERVICETYPE_NOTRAFFIC: UInt32 = 0
SERVICETYPE_BESTEFFORT: UInt32 = 1
SERVICETYPE_CONTROLLEDLOAD: UInt32 = 2
SERVICETYPE_GUARANTEED: UInt32 = 3
SERVICETYPE_NETWORK_UNAVAILABLE: UInt32 = 4
SERVICETYPE_GENERAL_INFORMATION: UInt32 = 5
SERVICETYPE_NOCHANGE: UInt32 = 6
SERVICETYPE_NONCONFORMING: UInt32 = 9
SERVICETYPE_NETWORK_CONTROL: UInt32 = 10
SERVICETYPE_QUALITATIVE: UInt32 = 13
SERVICE_BESTEFFORT: UInt32 = 2147549184
SERVICE_CONTROLLEDLOAD: UInt32 = 2147614720
SERVICE_GUARANTEED: UInt32 = 2147745792
SERVICE_QUALITATIVE: UInt32 = 2149580800
SERVICE_NO_TRAFFIC_CONTROL: UInt32 = 2164260864
SERVICE_NO_QOS_SIGNALING: UInt32 = 1073741824
QOS_NOT_SPECIFIED: UInt32 = 4294967295
POSITIVE_INFINITY_RATE: UInt32 = 4294967294
QOS_GENERAL_ID_BASE: UInt32 = 2000
TC_NONCONF_BORROW: UInt32 = 0
TC_NONCONF_SHAPE: UInt32 = 1
TC_NONCONF_DISCARD: UInt32 = 2
TC_NONCONF_BORROW_PLUS: UInt32 = 3
class_NULL: UInt32 = 0
class_SESSION: UInt32 = 1
class_SESSION_GROUP: UInt32 = 2
class_RSVP_HOP: UInt32 = 3
class_INTEGRITY: UInt32 = 4
class_TIME_VALUES: UInt32 = 5
class_ERROR_SPEC: UInt32 = 6
class_SCOPE: UInt32 = 7
class_STYLE: UInt32 = 8
class_FLOWSPEC: UInt32 = 9
class_IS_FLOWSPEC: UInt32 = 9
class_FILTER_SPEC: UInt32 = 10
class_SENDER_TEMPLATE: UInt32 = 11
class_SENDER_TSPEC: UInt32 = 12
class_ADSPEC: UInt32 = 13
class_POLICY_DATA: UInt32 = 14
class_CONFIRM: UInt32 = 15
class_MAX: UInt32 = 15
ctype_SESSION_ipv4: UInt32 = 1
ctype_SESSION_ipv4GPI: UInt32 = 3
SESSFLG_E_Police: UInt32 = 1
ctype_RSVP_HOP_ipv4: UInt32 = 1
Opt_Share_mask: UInt32 = 24
Opt_Distinct: UInt32 = 8
Opt_Shared: UInt32 = 16
Opt_SndSel_mask: UInt32 = 7
Opt_Wildcard: UInt32 = 1
Opt_Explicit: UInt32 = 2
ctype_STYLE: UInt32 = 1
ctype_FILTER_SPEC_ipv4: UInt32 = 1
ctype_FILTER_SPEC_ipv4GPI: UInt32 = 4
ctype_SENDER_TEMPLATE_ipv4: UInt32 = 1
ctype_SENDER_TEMPLATE_ipv4GPI: UInt32 = 4
ctype_SCOPE_list_ipv4: UInt32 = 1
ctype_ERROR_SPEC_ipv4: UInt32 = 1
ERROR_SPECF_InPlace: UInt32 = 1
ERROR_SPECF_NotGuilty: UInt32 = 2
ERR_FORWARD_OK: UInt32 = 32768
ERR_Usage_globl: UInt32 = 0
ERR_Usage_local: UInt32 = 16
ERR_Usage_serv: UInt32 = 17
ERR_global_mask: UInt32 = 4095
ctype_POLICY_DATA: UInt32 = 1
GENERAL_INFO: UInt32 = 1
GUARANTEED_SERV: UInt32 = 2
PREDICTIVE_SERV: UInt32 = 3
CONTROLLED_DELAY_SERV: UInt32 = 4
CONTROLLED_LOAD_SERV: UInt32 = 5
QUALITATIVE_SERV: UInt32 = 6
INTSERV_VERS_MASK: UInt32 = 240
INTSERV_VERSION0: UInt32 = 0
ISSH_BREAK_BIT: UInt32 = 128
ISPH_FLG_INV: UInt32 = 128
ctype_SENDER_TSPEC: UInt32 = 2
ctype_FLOWSPEC_Intserv0: UInt32 = 2
ctype_ADSPEC_INTSERV: UInt32 = 2
RSVP_PATH: UInt32 = 1
RSVP_RESV: UInt32 = 2
RSVP_PATH_ERR: UInt32 = 3
RSVP_RESV_ERR: UInt32 = 4
RSVP_PATH_TEAR: UInt32 = 5
RSVP_RESV_TEAR: UInt32 = 6
RSVP_Err_NONE: UInt32 = 0
RSVP_Erv_Nonev: UInt32 = 0
RSVP_Err_ADMISSION: UInt32 = 1
RSVP_Erv_Other: UInt32 = 0
RSVP_Erv_DelayBnd: UInt32 = 1
RSVP_Erv_Bandwidth: UInt32 = 2
RSVP_Erv_MTU: UInt32 = 3
RSVP_Erv_Flow_Rate: UInt32 = 32769
RSVP_Erv_Bucket_szie: UInt32 = 32770
RSVP_Erv_Peak_Rate: UInt32 = 32771
RSVP_Erv_Min_Policied_size: UInt32 = 32772
RSVP_Err_POLICY: UInt32 = 2
POLICY_ERRV_NO_MORE_INFO: UInt32 = 1
POLICY_ERRV_UNSUPPORTED_CREDENTIAL_TYPE: UInt32 = 2
POLICY_ERRV_INSUFFICIENT_PRIVILEGES: UInt32 = 3
POLICY_ERRV_EXPIRED_CREDENTIALS: UInt32 = 4
POLICY_ERRV_IDENTITY_CHANGED: UInt32 = 5
POLICY_ERRV_UNKNOWN: UInt32 = 0
POLICY_ERRV_GLOBAL_DEF_FLOW_COUNT: UInt32 = 1
POLICY_ERRV_GLOBAL_GRP_FLOW_COUNT: UInt32 = 2
POLICY_ERRV_GLOBAL_USER_FLOW_COUNT: UInt32 = 3
POLICY_ERRV_GLOBAL_UNAUTH_USER_FLOW_COUNT: UInt32 = 4
POLICY_ERRV_SUBNET_DEF_FLOW_COUNT: UInt32 = 5
POLICY_ERRV_SUBNET_GRP_FLOW_COUNT: UInt32 = 6
POLICY_ERRV_SUBNET_USER_FLOW_COUNT: UInt32 = 7
POLICY_ERRV_SUBNET_UNAUTH_USER_FLOW_COUNT: UInt32 = 8
POLICY_ERRV_GLOBAL_DEF_FLOW_DURATION: UInt32 = 9
POLICY_ERRV_GLOBAL_GRP_FLOW_DURATION: UInt32 = 10
POLICY_ERRV_GLOBAL_USER_FLOW_DURATION: UInt32 = 11
POLICY_ERRV_GLOBAL_UNAUTH_USER_FLOW_DURATION: UInt32 = 12
POLICY_ERRV_SUBNET_DEF_FLOW_DURATION: UInt32 = 13
POLICY_ERRV_SUBNET_GRP_FLOW_DURATION: UInt32 = 14
POLICY_ERRV_SUBNET_USER_FLOW_DURATION: UInt32 = 15
POLICY_ERRV_SUBNET_UNAUTH_USER_FLOW_DURATION: UInt32 = 16
POLICY_ERRV_GLOBAL_DEF_FLOW_RATE: UInt32 = 17
POLICY_ERRV_GLOBAL_GRP_FLOW_RATE: UInt32 = 18
POLICY_ERRV_GLOBAL_USER_FLOW_RATE: UInt32 = 19
POLICY_ERRV_GLOBAL_UNAUTH_USER_FLOW_RATE: UInt32 = 20
POLICY_ERRV_SUBNET_DEF_FLOW_RATE: UInt32 = 21
POLICY_ERRV_SUBNET_GRP_FLOW_RATE: UInt32 = 22
POLICY_ERRV_SUBNET_USER_FLOW_RATE: UInt32 = 23
POLICY_ERRV_SUBNET_UNAUTH_USER_FLOW_RATE: UInt32 = 24
POLICY_ERRV_GLOBAL_DEF_PEAK_RATE: UInt32 = 25
POLICY_ERRV_GLOBAL_GRP_PEAK_RATE: UInt32 = 26
POLICY_ERRV_GLOBAL_USER_PEAK_RATE: UInt32 = 27
POLICY_ERRV_GLOBAL_UNAUTH_USER_PEAK_RATE: UInt32 = 28
POLICY_ERRV_SUBNET_DEF_PEAK_RATE: UInt32 = 29
POLICY_ERRV_SUBNET_GRP_PEAK_RATE: UInt32 = 30
POLICY_ERRV_SUBNET_USER_PEAK_RATE: UInt32 = 31
POLICY_ERRV_SUBNET_UNAUTH_USER_PEAK_RATE: UInt32 = 32
POLICY_ERRV_GLOBAL_DEF_SUM_FLOW_RATE: UInt32 = 33
POLICY_ERRV_GLOBAL_GRP_SUM_FLOW_RATE: UInt32 = 34
POLICY_ERRV_GLOBAL_USER_SUM_FLOW_RATE: UInt32 = 35
POLICY_ERRV_GLOBAL_UNAUTH_USER_SUM_FLOW_RATE: UInt32 = 36
POLICY_ERRV_SUBNET_DEF_SUM_FLOW_RATE: UInt32 = 37
POLICY_ERRV_SUBNET_GRP_SUM_FLOW_RATE: UInt32 = 38
POLICY_ERRV_SUBNET_USER_SUM_FLOW_RATE: UInt32 = 39
POLICY_ERRV_SUBNET_UNAUTH_USER_SUM_FLOW_RATE: UInt32 = 40
POLICY_ERRV_GLOBAL_DEF_SUM_PEAK_RATE: UInt32 = 41
POLICY_ERRV_GLOBAL_GRP_SUM_PEAK_RATE: UInt32 = 42
POLICY_ERRV_GLOBAL_USER_SUM_PEAK_RATE: UInt32 = 43
POLICY_ERRV_GLOBAL_UNAUTH_USER_SUM_PEAK_RATE: UInt32 = 44
POLICY_ERRV_SUBNET_DEF_SUM_PEAK_RATE: UInt32 = 45
POLICY_ERRV_SUBNET_GRP_SUM_PEAK_RATE: UInt32 = 46
POLICY_ERRV_SUBNET_USER_SUM_PEAK_RATE: UInt32 = 47
POLICY_ERRV_SUBNET_UNAUTH_USER_SUM_PEAK_RATE: UInt32 = 48
POLICY_ERRV_UNKNOWN_USER: UInt32 = 49
POLICY_ERRV_NO_PRIVILEGES: UInt32 = 50
POLICY_ERRV_EXPIRED_USER_TOKEN: UInt32 = 51
POLICY_ERRV_NO_RESOURCES: UInt32 = 52
POLICY_ERRV_PRE_EMPTED: UInt32 = 53
POLICY_ERRV_USER_CHANGED: UInt32 = 54
POLICY_ERRV_NO_ACCEPTS: UInt32 = 55
POLICY_ERRV_NO_MEMORY: UInt32 = 56
POLICY_ERRV_CRAZY_FLOWSPEC: UInt32 = 57
RSVP_Err_NO_PATH: UInt32 = 3
RSVP_Err_NO_SENDER: UInt32 = 4
RSVP_Err_BAD_STYLE: UInt32 = 5
RSVP_Err_UNKNOWN_STYLE: UInt32 = 6
RSVP_Err_BAD_DSTPORT: UInt32 = 7
RSVP_Err_BAD_SNDPORT: UInt32 = 8
RSVP_Err_AMBIG_FILTER: UInt32 = 9
RSVP_Err_PREEMPTED: UInt32 = 12
RSVP_Err_UNKN_OBJ_CLASS: UInt32 = 13
RSVP_Err_UNKNOWN_CTYPE: UInt32 = 14
RSVP_Err_API_ERROR: UInt32 = 20
RSVP_Err_TC_ERROR: UInt32 = 21
RSVP_Erv_Conflict_Serv: UInt32 = 1
RSVP_Erv_No_Serv: UInt32 = 2
RSVP_Erv_Crazy_Flowspec: UInt32 = 3
RSVP_Erv_Crazy_Tspec: UInt32 = 4
RSVP_Err_TC_SYS_ERROR: UInt32 = 22
RSVP_Err_RSVP_SYS_ERROR: UInt32 = 23
RSVP_Erv_MEMORY: UInt32 = 1
RSVP_Erv_API: UInt32 = 2
LPM_PE_USER_IDENTITY: UInt32 = 2
LPM_PE_APP_IDENTITY: UInt32 = 3
ERROR_NO_MORE_INFO: UInt32 = 1
UNSUPPORTED_CREDENTIAL_TYPE: UInt32 = 2
INSUFFICIENT_PRIVILEGES: UInt32 = 3
EXPIRED_CREDENTIAL: UInt32 = 4
IDENTITY_CHANGED: UInt32 = 5
LPM_OK: UInt32 = 0
INV_LPM_HANDLE: UInt32 = 1
LPM_TIME_OUT: UInt32 = 2
INV_REQ_HANDLE: UInt32 = 3
DUP_RESULTS: UInt32 = 4
INV_RESULTS: UInt32 = 5
LPM_PE_ALL_TYPES: UInt32 = 0
LPM_API_VERSION_1: UInt32 = 1
PCM_VERSION_1: UInt32 = 1
LPV_RESERVED: UInt32 = 0
LPV_MIN_PRIORITY: UInt32 = 1
LPV_MAX_PRIORITY: UInt32 = 65280
LPV_DROP_MSG: UInt32 = 65533
LPV_DONT_CARE: UInt32 = 65534
LPV_REJECT: UInt32 = 65535
FORCE_IMMEDIATE_REFRESH: UInt32 = 1
LPM_RESULT_READY: UInt32 = 0
LPM_RESULT_DEFER: UInt32 = 1
RCVD_PATH_TEAR: UInt32 = 1
RCVD_RESV_TEAR: UInt32 = 2
ADM_CTRL_FAILED: UInt32 = 3
STATE_TIMEOUT: UInt32 = 4
FLOW_DURATION: UInt32 = 5
RESOURCES_ALLOCATED: UInt32 = 1
RESOURCES_MODIFIED: UInt32 = 2
CURRENT_TCI_VERSION: UInt32 = 2
TC_NOTIFY_IFC_UP: UInt32 = 1
TC_NOTIFY_IFC_CLOSE: UInt32 = 2
TC_NOTIFY_IFC_CHANGE: UInt32 = 3
TC_NOTIFY_PARAM_CHANGED: UInt32 = 4
TC_NOTIFY_FLOW_CLOSE: UInt32 = 5
MAX_STRING_LENGTH: UInt32 = 256
QOS_OUTGOING_DEFAULT_MINIMUM_BANDWIDTH: UInt32 = 4294967295
QOS_QUERYFLOW_FRESH: UInt32 = 1
QOS_NON_ADAPTIVE_FLOW: UInt32 = 2
RSVP_OBJECT_ID_BASE: UInt32 = 1000
RSVP_DEFAULT_STYLE: UInt32 = 0
RSVP_WILDCARD_STYLE: UInt32 = 1
RSVP_FIXED_FILTER_STYLE: UInt32 = 2
RSVP_SHARED_EXPLICIT_STYLE: UInt32 = 3
AD_FLAG_BREAK_BIT: UInt32 = 1
mIOC_IN: UInt32 = 2147483648
mIOC_OUT: UInt32 = 1073741824
mIOC_VENDOR: UInt32 = 67108864
mCOMPANY: UInt32 = 402653184
ioctl_code: UInt32 = 1
QOSSPBASE: UInt32 = 50000
ALLOWED_TO_SEND_DATA: UInt32 = 50001
ABLE_TO_RECV_RSVP: UInt32 = 50002
LINE_RATE: UInt32 = 50003
LOCAL_TRAFFIC_CONTROL: UInt32 = 50004
LOCAL_QOSABILITY: UInt32 = 50005
END_TO_END_QOSABILITY: UInt32 = 50006
INFO_NOT_AVAILABLE: UInt32 = 4294967295
ANY_DEST_ADDR: UInt32 = 4294967295
MODERATELY_DELAY_SENSITIVE: UInt32 = 4294967293
HIGHLY_DELAY_SENSITIVE: UInt32 = 4294967294
QOSSP_ERR_BASE: UInt32 = 56000
GQOS_NO_ERRORCODE: UInt32 = 0
GQOS_NO_ERRORVALUE: UInt32 = 0
GQOS_ERRORCODE_UNKNOWN: UInt32 = 4294967295
GQOS_ERRORVALUE_UNKNOWN: UInt32 = 4294967295
GQOS_NET_ADMISSION: UInt32 = 56100
GQOS_NET_POLICY: UInt32 = 56200
GQOS_RSVP: UInt32 = 56300
GQOS_API: UInt32 = 56400
GQOS_KERNEL_TC_SYS: UInt32 = 56500
GQOS_RSVP_SYS: UInt32 = 56600
GQOS_KERNEL_TC: UInt32 = 56700
PE_TYPE_APPID: UInt32 = 3
PE_ATTRIB_TYPE_POLICY_LOCATOR: UInt32 = 1
POLICY_LOCATOR_SUB_TYPE_ASCII_DN: UInt32 = 1
POLICY_LOCATOR_SUB_TYPE_UNICODE_DN: UInt32 = 2
POLICY_LOCATOR_SUB_TYPE_ASCII_DN_ENC: UInt32 = 3
POLICY_LOCATOR_SUB_TYPE_UNICODE_DN_ENC: UInt32 = 4
PE_ATTRIB_TYPE_CREDENTIAL: UInt32 = 2
CREDENTIAL_SUB_TYPE_ASCII_ID: UInt32 = 1
CREDENTIAL_SUB_TYPE_UNICODE_ID: UInt32 = 2
CREDENTIAL_SUB_TYPE_KERBEROS_TKT: UInt32 = 3
CREDENTIAL_SUB_TYPE_X509_V3_CERT: UInt32 = 4
CREDENTIAL_SUB_TYPE_PGP_CERT: UInt32 = 5
TCBASE: UInt32 = 7500
ERROR_INCOMPATIBLE_TCI_VERSION: UInt32 = 7501
ERROR_INVALID_SERVICE_TYPE: UInt32 = 7502
ERROR_INVALID_TOKEN_RATE: UInt32 = 7503
ERROR_INVALID_PEAK_RATE: UInt32 = 7504
ERROR_INVALID_SD_MODE: UInt32 = 7505
ERROR_INVALID_QOS_PRIORITY: UInt32 = 7506
ERROR_INVALID_TRAFFIC_CLASS: UInt32 = 7507
ERROR_INVALID_ADDRESS_TYPE: UInt32 = 7508
ERROR_DUPLICATE_FILTER: UInt32 = 7509
ERROR_FILTER_CONFLICT: UInt32 = 7510
ERROR_ADDRESS_TYPE_NOT_SUPPORTED: UInt32 = 7511
ERROR_TC_SUPPORTED_OBJECTS_EXIST: UInt32 = 7512
ERROR_INCOMPATABLE_QOS: UInt32 = 7513
ERROR_TC_NOT_SUPPORTED: UInt32 = 7514
ERROR_TC_OBJECT_LENGTH_INVALID: UInt32 = 7515
ERROR_INVALID_FLOW_MODE: UInt32 = 7516
ERROR_INVALID_DIFFSERV_FLOW: UInt32 = 7517
ERROR_DS_MAPPING_EXISTS: UInt32 = 7518
ERROR_INVALID_SHAPE_RATE: UInt32 = 7519
ERROR_INVALID_DS_CLASS: UInt32 = 7520
ERROR_TOO_MANY_CLIENTS: UInt32 = 7521
GUID_QOS_REMAINING_BANDWIDTH: Guid = Guid('c4c51720-40ec-11d1-2c-91-00-aa-00-57-49-15')
GUID_QOS_BESTEFFORT_BANDWIDTH: Guid = Guid('ed885290-40ec-11d1-2c-91-00-aa-00-57-49-15')
GUID_QOS_LATENCY: Guid = Guid('fc408ef0-40ec-11d1-2c-91-00-aa-00-57-49-15')
GUID_QOS_FLOW_COUNT: Guid = Guid('1147f880-40ed-11d1-2c-91-00-aa-00-57-49-15')
GUID_QOS_NON_BESTEFFORT_LIMIT: Guid = Guid('185c44e0-40ed-11d1-2c-91-00-aa-00-57-49-15')
GUID_QOS_MAX_OUTSTANDING_SENDS: Guid = Guid('161ffa86-6120-11d1-2c-91-00-aa-00-57-49-15')
GUID_QOS_STATISTICS_BUFFER: Guid = Guid('bb2c0980-e900-11d1-b0-7e-00-80-c7-13-82-bf')
GUID_QOS_FLOW_MODE: Guid = Guid('5c82290a-515a-11d2-8e-58-00-c0-4f-c9-bf-cb')
GUID_QOS_ISSLOW_FLOW: Guid = Guid('abf273a4-ee07-11d2-be-1b-00-a0-c9-9e-e6-3b')
GUID_QOS_TIMER_RESOLUTION: Guid = Guid('ba10cc88-f13e-11d2-be-1b-00-a0-c9-9e-e6-3b')
GUID_QOS_FLOW_IP_CONFORMING: Guid = Guid('07f99a8b-fcd2-11d2-be-1e-00-a0-c9-9e-e6-3b')
GUID_QOS_FLOW_IP_NONCONFORMING: Guid = Guid('087a5987-fcd2-11d2-be-1e-00-a0-c9-9e-e6-3b')
GUID_QOS_FLOW_8021P_CONFORMING: Guid = Guid('08c1e013-fcd2-11d2-be-1e-00-a0-c9-9e-e6-3b')
GUID_QOS_FLOW_8021P_NONCONFORMING: Guid = Guid('09023f91-fcd2-11d2-be-1e-00-a0-c9-9e-e6-3b')
GUID_QOS_ENABLE_AVG_STATS: Guid = Guid('bafb6d11-27c4-4801-a4-6f-ef-80-80-c1-88-c8')
GUID_QOS_ENABLE_WINDOW_ADJUSTMENT: Guid = Guid('aa966725-d3e9-4c55-b3-35-2a-00-27-9a-1e-64')
FSCTL_TCP_BASE: UInt32 = 18
DD_TCP_DEVICE_NAME: String = '\\Device\\Tcp'
IF_MIB_STATS_ID: UInt32 = 1
IP_MIB_STATS_ID: UInt32 = 1
IP_MIB_ADDRTABLE_ENTRY_ID: UInt32 = 258
IP_INTFC_INFO_ID: UInt32 = 259
MAX_PHYSADDR_SIZE: UInt32 = 8
SIPAEV_PREBOOT_CERT: UInt32 = 0
SIPAEV_POST_CODE: UInt32 = 1
SIPAEV_UNUSED: UInt32 = 2
SIPAEV_NO_ACTION: UInt32 = 3
SIPAEV_SEPARATOR: UInt32 = 4
SIPAEV_ACTION: UInt32 = 5
SIPAEV_EVENT_TAG: UInt32 = 6
SIPAEV_S_CRTM_CONTENTS: UInt32 = 7
SIPAEV_S_CRTM_VERSION: UInt32 = 8
SIPAEV_CPU_MICROCODE: UInt32 = 9
SIPAEV_PLATFORM_CONFIG_FLAGS: UInt32 = 10
SIPAEV_TABLE_OF_DEVICES: UInt32 = 11
SIPAEV_COMPACT_HASH: UInt32 = 12
SIPAEV_IPL: UInt32 = 13
SIPAEV_IPL_PARTITION_DATA: UInt32 = 14
SIPAEV_NONHOST_CODE: UInt32 = 15
SIPAEV_NONHOST_CONFIG: UInt32 = 16
SIPAEV_NONHOST_INFO: UInt32 = 17
SIPAEV_OMIT_BOOT_DEVICE_EVENTS: UInt32 = 18
SIPAEV_EFI_EVENT_BASE: UInt32 = 2147483648
SIPAEV_EFI_VARIABLE_DRIVER_CONFIG: UInt32 = 2147483649
SIPAEV_EFI_VARIABLE_BOOT: UInt32 = 2147483650
SIPAEV_EFI_BOOT_SERVICES_APPLICATION: UInt32 = 2147483651
SIPAEV_EFI_BOOT_SERVICES_DRIVER: UInt32 = 2147483652
SIPAEV_EFI_RUNTIME_SERVICES_DRIVER: UInt32 = 2147483653
SIPAEV_EFI_GPT_EVENT: UInt32 = 2147483654
SIPAEV_EFI_ACTION: UInt32 = 2147483655
SIPAEV_EFI_PLATFORM_FIRMWARE_BLOB: UInt32 = 2147483656
SIPAEV_EFI_HANDOFF_TABLES: UInt32 = 2147483657
SIPAEV_EFI_PLATFORM_FIRMWARE_BLOB2: UInt32 = 2147483658
SIPAEV_EFI_HANDOFF_TABLES2: UInt32 = 2147483659
SIPAEV_EFI_HCRTM_EVENT: UInt32 = 2147483664
SIPAEV_EFI_VARIABLE_AUTHORITY: UInt32 = 2147483872
SIPAEV_EFI_SPDM_FIRMWARE_BLOB: UInt32 = 2147483873
SIPAEV_EFI_SPDM_FIRMWARE_CONFIG: UInt32 = 2147483874
SIPAEV_TXT_EVENT_BASE: UInt32 = 1024
SIPAEV_TXT_PCR_MAPPING: UInt32 = 1025
SIPAEV_TXT_HASH_START: UInt32 = 1026
SIPAEV_TXT_COMBINED_HASH: UInt32 = 1027
SIPAEV_TXT_MLE_HASH: UInt32 = 1028
SIPAEV_TXT_BIOSAC_REG_DATA: UInt32 = 1034
SIPAEV_TXT_CPU_SCRTM_STAT: UInt32 = 1035
SIPAEV_TXT_LCP_CONTROL_HASH: UInt32 = 1036
SIPAEV_TXT_ELEMENTS_HASH: UInt32 = 1037
SIPAEV_TXT_STM_HASH: UInt32 = 1038
SIPAEV_TXT_OSSINITDATA_CAP_HASH: UInt32 = 1039
SIPAEV_TXT_SINIT_PUBKEY_HASH: UInt32 = 1040
SIPAEV_TXT_LCP_HASH: UInt32 = 1041
SIPAEV_TXT_LCP_DETAILS_HASH: UInt32 = 1042
SIPAEV_TXT_LCP_AUTHORITIES_HASH: UInt32 = 1043
SIPAEV_TXT_NV_INFO_HASH: UInt32 = 1044
SIPAEV_TXT_COLD_BOOT_BIOS_HASH: UInt32 = 1045
SIPAEV_TXT_KM_HASH: UInt32 = 1046
SIPAEV_TXT_BPM_HASH: UInt32 = 1047
SIPAEV_TXT_KM_INFO_HASH: UInt32 = 1048
SIPAEV_TXT_BPM_INFO_HASH: UInt32 = 1049
SIPAEV_TXT_BOOT_POL_HASH: UInt32 = 1050
SIPAEV_TXT_RANDOM_VALUE: UInt32 = 1278
SIPAEV_TXT_CAP_VALUE: UInt32 = 1279
SIPAEV_AMD_SL_EVENT_BASE: UInt32 = 32768
SIPAEV_AMD_SL_LOAD: UInt32 = 32769
SIPAEV_AMD_SL_PSP_FW_SPLT: UInt32 = 32770
SIPAEV_AMD_SL_TSME_RB_FUSE: UInt32 = 32771
SIPAEV_AMD_SL_PUB_KEY: UInt32 = 32772
SIPAEV_AMD_SL_SVN: UInt32 = 32773
SIPAEV_AMD_SL_LOAD_1: UInt32 = 32774
SIPAEV_AMD_SL_SEPARATOR: UInt32 = 32775
SIPAEVENTTYPE_NONMEASURED: UInt32 = 2147483648
SIPAEVENTTYPE_AGGREGATION: UInt32 = 1073741824
SIPAEVENTTYPE_CONTAINER: UInt32 = 65536
SIPAEVENTTYPE_INFORMATION: UInt32 = 131072
SIPAEVENTTYPE_ERROR: UInt32 = 196608
SIPAEVENTTYPE_PREOSPARAMETER: UInt32 = 262144
SIPAEVENTTYPE_OSPARAMETER: UInt32 = 327680
SIPAEVENTTYPE_AUTHORITY: UInt32 = 393216
SIPAEVENTTYPE_LOADEDMODULE: UInt32 = 458752
SIPAEVENTTYPE_TRUSTPOINT: UInt32 = 524288
SIPAEVENTTYPE_ELAM: UInt32 = 589824
SIPAEVENTTYPE_VBS: UInt32 = 655360
SIPAEVENTTYPE_KSR: UInt32 = 720896
SIPAEVENTTYPE_DRTM: UInt32 = 786432
SIPAERROR_FIRMWAREFAILURE: UInt32 = 196609
SIPAERROR_INTERNALFAILURE: UInt32 = 196611
SIPAEVENT_INFORMATION: UInt32 = 131073
SIPAEVENT_BOOTCOUNTER: UInt32 = 131074
SIPAEVENT_TRANSFER_CONTROL: UInt32 = 131075
SIPAEVENT_APPLICATION_RETURN: UInt32 = 131076
SIPAEVENT_BITLOCKER_UNLOCK: UInt32 = 131077
SIPAEVENT_EVENTCOUNTER: UInt32 = 131078
SIPAEVENT_COUNTERID: UInt32 = 131079
SIPAEVENT_MORBIT_NOT_CANCELABLE: UInt32 = 131080
SIPAEVENT_APPLICATION_SVN: UInt32 = 131081
SIPAEVENT_SVN_CHAIN_STATUS: UInt32 = 131082
SIPAEVENT_MORBIT_API_STATUS: UInt32 = 131083
SIPAEVENT_BOOTDEBUGGING: UInt32 = 262145
SIPAEVENT_BOOT_REVOCATION_LIST: UInt32 = 262146
SIPAEVENT_OSKERNELDEBUG: UInt32 = 327681
SIPAEVENT_CODEINTEGRITY: UInt32 = 327682
SIPAEVENT_TESTSIGNING: UInt32 = 327683
SIPAEVENT_DATAEXECUTIONPREVENTION: UInt32 = 327684
SIPAEVENT_SAFEMODE: UInt32 = 327685
SIPAEVENT_WINPE: UInt32 = 327686
SIPAEVENT_PHYSICALADDRESSEXTENSION: UInt32 = 327687
SIPAEVENT_OSDEVICE: UInt32 = 327688
SIPAEVENT_SYSTEMROOT: UInt32 = 327689
SIPAEVENT_HYPERVISOR_LAUNCH_TYPE: UInt32 = 327690
SIPAEVENT_HYPERVISOR_PATH: UInt32 = 327691
SIPAEVENT_HYPERVISOR_IOMMU_POLICY: UInt32 = 327692
SIPAEVENT_HYPERVISOR_DEBUG: UInt32 = 327693
SIPAEVENT_DRIVER_LOAD_POLICY: UInt32 = 327694
SIPAEVENT_SI_POLICY: UInt32 = 327695
SIPAEVENT_HYPERVISOR_MMIO_NX_POLICY: UInt32 = 327696
SIPAEVENT_HYPERVISOR_MSR_FILTER_POLICY: UInt32 = 327697
SIPAEVENT_VSM_LAUNCH_TYPE: UInt32 = 327698
SIPAEVENT_OS_REVOCATION_LIST: UInt32 = 327699
SIPAEVENT_SMT_STATUS: UInt32 = 327700
SIPAEVENT_VSM_IDK_INFO: UInt32 = 327712
SIPAEVENT_FLIGHTSIGNING: UInt32 = 327713
SIPAEVENT_PAGEFILE_ENCRYPTION_ENABLED: UInt32 = 327714
SIPAEVENT_VSM_IDKS_INFO: UInt32 = 327715
SIPAEVENT_HIBERNATION_DISABLED: UInt32 = 327716
SIPAEVENT_DUMPS_DISABLED: UInt32 = 327717
SIPAEVENT_DUMP_ENCRYPTION_ENABLED: UInt32 = 327718
SIPAEVENT_DUMP_ENCRYPTION_KEY_DIGEST: UInt32 = 327719
SIPAEVENT_LSAISO_CONFIG: UInt32 = 327720
SIPAEVENT_SBCP_INFO: UInt32 = 327721
SIPAEVENT_HYPERVISOR_BOOT_DMA_PROTECTION: UInt32 = 327728
SIPAEVENT_NOAUTHORITY: UInt32 = 393217
SIPAEVENT_AUTHORITYPUBKEY: UInt32 = 393218
SIPAEVENT_FILEPATH: UInt32 = 458753
SIPAEVENT_IMAGESIZE: UInt32 = 458754
SIPAEVENT_HASHALGORITHMID: UInt32 = 458755
SIPAEVENT_AUTHENTICODEHASH: UInt32 = 458756
SIPAEVENT_AUTHORITYISSUER: UInt32 = 458757
SIPAEVENT_AUTHORITYSERIAL: UInt32 = 458758
SIPAEVENT_IMAGEBASE: UInt32 = 458759
SIPAEVENT_AUTHORITYPUBLISHER: UInt32 = 458760
SIPAEVENT_AUTHORITYSHA1THUMBPRINT: UInt32 = 458761
SIPAEVENT_IMAGEVALIDATED: UInt32 = 458762
SIPAEVENT_MODULE_SVN: UInt32 = 458763
SIPAEVENT_ELAM_KEYNAME: UInt32 = 589825
SIPAEVENT_ELAM_CONFIGURATION: UInt32 = 589826
SIPAEVENT_ELAM_POLICY: UInt32 = 589827
SIPAEVENT_ELAM_MEASURED: UInt32 = 589828
SIPAEVENT_VBS_VSM_REQUIRED: UInt32 = 655361
SIPAEVENT_VBS_SECUREBOOT_REQUIRED: UInt32 = 655362
SIPAEVENT_VBS_IOMMU_REQUIRED: UInt32 = 655363
SIPAEVENT_VBS_MMIO_NX_REQUIRED: UInt32 = 655364
SIPAEVENT_VBS_MSR_FILTERING_REQUIRED: UInt32 = 655365
SIPAEVENT_VBS_MANDATORY_ENFORCEMENT: UInt32 = 655366
SIPAEVENT_VBS_HVCI_POLICY: UInt32 = 655367
SIPAEVENT_VBS_MICROSOFT_BOOT_CHAIN_REQUIRED: UInt32 = 655368
SIPAEVENT_VBS_DUMP_USES_AMEROOT: UInt32 = 655369
SIPAEVENT_VBS_VSM_NOSECRETS_ENFORCED: UInt32 = 655370
SIPAEVENT_KSR_SIGNATURE: UInt32 = 720897
SIPAEVENT_DRTM_STATE_AUTH: UInt32 = 786433
SIPAEVENT_DRTM_SMM_LEVEL: UInt32 = 786434
SIPAEVENT_DRTM_AMD_SMM_HASH: UInt32 = 786435
SIPAEVENT_DRTM_AMD_SMM_SIGNER_KEY: UInt32 = 786436
FVEB_UNLOCK_FLAG_NONE: UInt32 = 0
FVEB_UNLOCK_FLAG_CACHED: UInt32 = 1
FVEB_UNLOCK_FLAG_MEDIA: UInt32 = 2
FVEB_UNLOCK_FLAG_TPM: UInt32 = 4
FVEB_UNLOCK_FLAG_PIN: UInt32 = 16
FVEB_UNLOCK_FLAG_EXTERNAL: UInt32 = 32
FVEB_UNLOCK_FLAG_RECOVERY: UInt32 = 64
FVEB_UNLOCK_FLAG_PASSPHRASE: UInt32 = 128
FVEB_UNLOCK_FLAG_NBP: UInt32 = 256
FVEB_UNLOCK_FLAG_AUK_OSFVEINFO: UInt32 = 512
OSDEVICE_TYPE_UNKNOWN: UInt32 = 0
OSDEVICE_TYPE_BLOCKIO_HARDDISK: UInt32 = 65537
OSDEVICE_TYPE_BLOCKIO_REMOVABLEDISK: UInt32 = 65538
OSDEVICE_TYPE_BLOCKIO_CDROM: UInt32 = 65539
OSDEVICE_TYPE_BLOCKIO_PARTITION: UInt32 = 65540
OSDEVICE_TYPE_BLOCKIO_FILE: UInt32 = 65541
OSDEVICE_TYPE_BLOCKIO_RAMDISK: UInt32 = 65542
OSDEVICE_TYPE_BLOCKIO_VIRTUALHARDDISK: UInt32 = 65543
OSDEVICE_TYPE_SERIAL: UInt32 = 131072
OSDEVICE_TYPE_UDP: UInt32 = 196608
OSDEVICE_TYPE_VMBUS: UInt32 = 262144
OSDEVICE_TYPE_COMPOSITE: UInt32 = 327680
SIPAHDRSIGNATURE: UInt32 = 1279476311
SIPALOGVERSION: UInt32 = 1
SIPAKSRHDRSIGNATURE: UInt32 = 1297240907
WBCL_DIGEST_ALG_ID_SHA_1: UInt32 = 4
WBCL_DIGEST_ALG_ID_SHA_2_256: UInt32 = 11
WBCL_DIGEST_ALG_ID_SHA_2_384: UInt32 = 12
WBCL_DIGEST_ALG_ID_SHA_2_512: UInt32 = 13
WBCL_DIGEST_ALG_ID_SM3_256: UInt32 = 18
WBCL_DIGEST_ALG_ID_SHA3_256: UInt32 = 39
WBCL_DIGEST_ALG_ID_SHA3_384: UInt32 = 40
WBCL_DIGEST_ALG_ID_SHA3_512: UInt32 = 41
WBCL_DIGEST_ALG_BITMAP_SHA_1: UInt32 = 1
WBCL_DIGEST_ALG_BITMAP_SHA_2_256: UInt32 = 2
WBCL_DIGEST_ALG_BITMAP_SHA_2_384: UInt32 = 4
WBCL_DIGEST_ALG_BITMAP_SHA_2_512: UInt32 = 8
WBCL_DIGEST_ALG_BITMAP_SM3_256: UInt32 = 16
WBCL_DIGEST_ALG_BITMAP_SHA3_256: UInt32 = 32
WBCL_DIGEST_ALG_BITMAP_SHA3_384: UInt32 = 64
WBCL_DIGEST_ALG_BITMAP_SHA3_512: UInt32 = 128
WBCL_HASH_LEN_SHA1: UInt32 = 20
IS_GUAR_RSPEC: Int32 = 130
GUAR_ADSPARM_C: Int32 = 131
GUAR_ADSPARM_D: Int32 = 132
GUAR_ADSPARM_Ctot: Int32 = 133
GUAR_ADSPARM_Dtot: Int32 = 134
GUAR_ADSPARM_Csum: Int32 = 135
GUAR_ADSPARM_Dsum: Int32 = 136
@winfunctype('qwave.dll')
def QOSCreateHandle(Version: POINTER(win32more.NetworkManagement.QoS.QOS_VERSION_head), QOSHandle: POINTER(win32more.Foundation.HANDLE)) -> win32more.Foundation.BOOL: ...
@winfunctype('qwave.dll')
def QOSCloseHandle(QOSHandle: win32more.Foundation.HANDLE) -> win32more.Foundation.BOOL: ...
@winfunctype('qwave.dll')
def QOSStartTrackingClient(QOSHandle: win32more.Foundation.HANDLE, DestAddr: POINTER(win32more.Networking.WinSock.SOCKADDR_head), Flags: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('qwave.dll')
def QOSStopTrackingClient(QOSHandle: win32more.Foundation.HANDLE, DestAddr: POINTER(win32more.Networking.WinSock.SOCKADDR_head), Flags: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('qwave.dll')
def QOSEnumerateFlows(QOSHandle: win32more.Foundation.HANDLE, Size: POINTER(UInt32), Buffer: c_void_p) -> win32more.Foundation.BOOL: ...
@winfunctype('qwave.dll')
def QOSAddSocketToFlow(QOSHandle: win32more.Foundation.HANDLE, Socket: win32more.Networking.WinSock.SOCKET, DestAddr: POINTER(win32more.Networking.WinSock.SOCKADDR_head), TrafficType: win32more.NetworkManagement.QoS.QOS_TRAFFIC_TYPE, Flags: UInt32, FlowId: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('qwave.dll')
def QOSRemoveSocketFromFlow(QOSHandle: win32more.Foundation.HANDLE, Socket: win32more.Networking.WinSock.SOCKET, FlowId: UInt32, Flags: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('qwave.dll')
def QOSSetFlow(QOSHandle: win32more.Foundation.HANDLE, FlowId: UInt32, Operation: win32more.NetworkManagement.QoS.QOS_SET_FLOW, Size: UInt32, Buffer: c_void_p, Flags: UInt32, Overlapped: POINTER(win32more.System.IO.OVERLAPPED_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('qwave.dll')
def QOSQueryFlow(QOSHandle: win32more.Foundation.HANDLE, FlowId: UInt32, Operation: win32more.NetworkManagement.QoS.QOS_QUERY_FLOW, Size: POINTER(UInt32), Buffer: c_void_p, Flags: UInt32, Overlapped: POINTER(win32more.System.IO.OVERLAPPED_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('qwave.dll')
def QOSNotifyFlow(QOSHandle: win32more.Foundation.HANDLE, FlowId: UInt32, Operation: win32more.NetworkManagement.QoS.QOS_NOTIFY_FLOW, Size: POINTER(UInt32), Buffer: c_void_p, Flags: UInt32, Overlapped: POINTER(win32more.System.IO.OVERLAPPED_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('qwave.dll')
def QOSCancel(QOSHandle: win32more.Foundation.HANDLE, Overlapped: POINTER(win32more.System.IO.OVERLAPPED_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('TRAFFIC.dll')
def TcRegisterClient(TciVersion: UInt32, ClRegCtx: win32more.Foundation.HANDLE, ClientHandlerList: POINTER(win32more.NetworkManagement.QoS.TCI_CLIENT_FUNC_LIST_head), pClientHandle: POINTER(win32more.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('TRAFFIC.dll')
def TcEnumerateInterfaces(ClientHandle: win32more.Foundation.HANDLE, pBufferSize: POINTER(UInt32), InterfaceBuffer: POINTER(win32more.NetworkManagement.QoS.TC_IFC_DESCRIPTOR_head)) -> UInt32: ...
@winfunctype('TRAFFIC.dll')
def TcOpenInterfaceA(pInterfaceName: win32more.Foundation.PSTR, ClientHandle: win32more.Foundation.HANDLE, ClIfcCtx: win32more.Foundation.HANDLE, pIfcHandle: POINTER(win32more.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('TRAFFIC.dll')
def TcOpenInterfaceW(pInterfaceName: win32more.Foundation.PWSTR, ClientHandle: win32more.Foundation.HANDLE, ClIfcCtx: win32more.Foundation.HANDLE, pIfcHandle: POINTER(win32more.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('TRAFFIC.dll')
def TcCloseInterface(IfcHandle: win32more.Foundation.HANDLE) -> UInt32: ...
@winfunctype('TRAFFIC.dll')
def TcQueryInterface(IfcHandle: win32more.Foundation.HANDLE, pGuidParam: POINTER(Guid), NotifyChange: win32more.Foundation.BOOLEAN, pBufferSize: POINTER(UInt32), Buffer: c_void_p) -> UInt32: ...
@winfunctype('TRAFFIC.dll')
def TcSetInterface(IfcHandle: win32more.Foundation.HANDLE, pGuidParam: POINTER(Guid), BufferSize: UInt32, Buffer: c_void_p) -> UInt32: ...
@winfunctype('TRAFFIC.dll')
def TcQueryFlowA(pFlowName: win32more.Foundation.PSTR, pGuidParam: POINTER(Guid), pBufferSize: POINTER(UInt32), Buffer: c_void_p) -> UInt32: ...
@winfunctype('TRAFFIC.dll')
def TcQueryFlowW(pFlowName: win32more.Foundation.PWSTR, pGuidParam: POINTER(Guid), pBufferSize: POINTER(UInt32), Buffer: c_void_p) -> UInt32: ...
@winfunctype('TRAFFIC.dll')
def TcSetFlowA(pFlowName: win32more.Foundation.PSTR, pGuidParam: POINTER(Guid), BufferSize: UInt32, Buffer: c_void_p) -> UInt32: ...
@winfunctype('TRAFFIC.dll')
def TcSetFlowW(pFlowName: win32more.Foundation.PWSTR, pGuidParam: POINTER(Guid), BufferSize: UInt32, Buffer: c_void_p) -> UInt32: ...
@winfunctype('TRAFFIC.dll')
def TcAddFlow(IfcHandle: win32more.Foundation.HANDLE, ClFlowCtx: win32more.Foundation.HANDLE, Flags: UInt32, pGenericFlow: POINTER(win32more.NetworkManagement.QoS.TC_GEN_FLOW_head), pFlowHandle: POINTER(win32more.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('TRAFFIC.dll')
def TcGetFlowNameA(FlowHandle: win32more.Foundation.HANDLE, StrSize: UInt32, pFlowName: win32more.Foundation.PSTR) -> UInt32: ...
@winfunctype('TRAFFIC.dll')
def TcGetFlowNameW(FlowHandle: win32more.Foundation.HANDLE, StrSize: UInt32, pFlowName: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('TRAFFIC.dll')
def TcModifyFlow(FlowHandle: win32more.Foundation.HANDLE, pGenericFlow: POINTER(win32more.NetworkManagement.QoS.TC_GEN_FLOW_head)) -> UInt32: ...
@winfunctype('TRAFFIC.dll')
def TcAddFilter(FlowHandle: win32more.Foundation.HANDLE, pGenericFilter: POINTER(win32more.NetworkManagement.QoS.TC_GEN_FILTER_head), pFilterHandle: POINTER(win32more.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('TRAFFIC.dll')
def TcDeregisterClient(ClientHandle: win32more.Foundation.HANDLE) -> UInt32: ...
@winfunctype('TRAFFIC.dll')
def TcDeleteFlow(FlowHandle: win32more.Foundation.HANDLE) -> UInt32: ...
@winfunctype('TRAFFIC.dll')
def TcDeleteFilter(FilterHandle: win32more.Foundation.HANDLE) -> UInt32: ...
@winfunctype('TRAFFIC.dll')
def TcEnumerateFlows(IfcHandle: win32more.Foundation.HANDLE, pEnumHandle: POINTER(win32more.Foundation.HANDLE), pFlowCount: POINTER(UInt32), pBufSize: POINTER(UInt32), Buffer: POINTER(win32more.NetworkManagement.QoS.ENUMERATION_BUFFER_head)) -> UInt32: ...
@winfunctype_pointer
def CBADMITRESULT(LpmHandle: win32more.NetworkManagement.QoS.LPM_HANDLE, RequestHandle: win32more.NetworkManagement.QoS.RHANDLE, ulPcmActionFlags: UInt32, LpmError: Int32, PolicyDecisionsCount: Int32, pPolicyDecisions: POINTER(win32more.NetworkManagement.QoS.POLICY_DECISION_head)) -> POINTER(UInt32): ...
@winfunctype_pointer
def CBGETRSVPOBJECTS(LpmHandle: win32more.NetworkManagement.QoS.LPM_HANDLE, RequestHandle: win32more.NetworkManagement.QoS.RHANDLE, LpmError: Int32, RsvpObjectsCount: Int32, ppRsvpObjects: POINTER(POINTER(win32more.NetworkManagement.QoS.RsvpObjHdr_head))) -> POINTER(UInt32): ...
class CONTROL_SERVICE(Structure):
    Length: UInt32
    Service: UInt32
    Overrides: win32more.NetworkManagement.QoS.AD_GENERAL_PARAMS
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Guaranteed: win32more.NetworkManagement.QoS.AD_GUARANTEED
        ParamBuffer: win32more.NetworkManagement.QoS.PARAM_BUFFER * 1
class CtrlLoadFlowspec(Structure):
    CL_spec_serv_hdr: win32more.NetworkManagement.QoS.IntServServiceHdr
    CL_spec_parm_hdr: win32more.NetworkManagement.QoS.IntServParmHdr
    CL_spec_parms: win32more.NetworkManagement.QoS.GenTspecParms
class ENUMERATION_BUFFER(Structure):
    Length: UInt32
    OwnerProcessId: UInt32
    FlowNameLength: UInt16
    FlowName: Char * 256
    pFlow: POINTER(win32more.NetworkManagement.QoS.TC_GEN_FLOW_head)
    NumberOfFilters: UInt32
    GenericFilter: win32more.NetworkManagement.QoS.TC_GEN_FILTER * 1
class ERROR_SPEC(Structure):
    errs_header: win32more.NetworkManagement.QoS.RsvpObjHdr
    errs_u: _errs_u_e__Union
    class _errs_u_e__Union(Union):
        errs_ipv4: win32more.NetworkManagement.QoS.Error_Spec_IPv4
class Error_Spec_IPv4(Structure):
    errs_errnode: win32more.Networking.WinSock.IN_ADDR
    errs_flags: Byte
    errs_code: Byte
    errs_value: UInt16
class FILTER_SPEC(Structure):
    filt_header: win32more.NetworkManagement.QoS.RsvpObjHdr
    filt_u: _filt_u_e__Union
    class _filt_u_e__Union(Union):
        filt_ipv4: win32more.NetworkManagement.QoS.Filter_Spec_IPv4
        filt_ipv4gpi: win32more.NetworkManagement.QoS.Filter_Spec_IPv4GPI
class FLOWDESCRIPTOR(Structure):
    FlowSpec: win32more.Networking.WinSock.FLOWSPEC
    NumFilters: UInt32
    FilterList: POINTER(win32more.NetworkManagement.QoS.RSVP_FILTERSPEC_head)
class FLOW_DESC(Structure):
    u1: _u1_e__Union
    u2: _u2_e__Union
    class _u1_e__Union(Union):
        stspec: POINTER(win32more.NetworkManagement.QoS.SENDER_TSPEC_head)
        isflow: POINTER(win32more.NetworkManagement.QoS.IS_FLOWSPEC_head)
    class _u2_e__Union(Union):
        stemp: POINTER(win32more.NetworkManagement.QoS.FILTER_SPEC_head)
        fspec: POINTER(win32more.NetworkManagement.QoS.FILTER_SPEC_head)
FilterType = Int32
FILTERSPECV4: FilterType = 1
FILTERSPECV6: FilterType = 2
FILTERSPECV6_FLOW: FilterType = 3
FILTERSPECV4_GPI: FilterType = 4
FILTERSPECV6_GPI: FilterType = 5
FILTERSPEC_END: FilterType = 6
class Filter_Spec_IPv4(Structure):
    filt_ipaddr: win32more.Networking.WinSock.IN_ADDR
    filt_unused: UInt16
    filt_port: UInt16
class Filter_Spec_IPv4GPI(Structure):
    filt_ipaddr: win32more.Networking.WinSock.IN_ADDR
    filt_gpi: UInt32
class Gads_parms_t(Structure):
    Gads_serv_hdr: win32more.NetworkManagement.QoS.IntServServiceHdr
    Gads_Ctot_hdr: win32more.NetworkManagement.QoS.IntServParmHdr
    Gads_Ctot: UInt32
    Gads_Dtot_hdr: win32more.NetworkManagement.QoS.IntServParmHdr
    Gads_Dtot: UInt32
    Gads_Csum_hdr: win32more.NetworkManagement.QoS.IntServParmHdr
    Gads_Csum: UInt32
    Gads_Dsum_hdr: win32more.NetworkManagement.QoS.IntServParmHdr
    Gads_Dsum: UInt32
class GenAdspecParams(Structure):
    gen_parm_hdr: win32more.NetworkManagement.QoS.IntServServiceHdr
    gen_parm_hopcnt_hdr: win32more.NetworkManagement.QoS.IntServParmHdr
    gen_parm_hopcnt: UInt32
    gen_parm_pathbw_hdr: win32more.NetworkManagement.QoS.IntServParmHdr
    gen_parm_path_bw: Single
    gen_parm_minlat_hdr: win32more.NetworkManagement.QoS.IntServParmHdr
    gen_parm_min_latency: UInt32
    gen_parm_compmtu_hdr: win32more.NetworkManagement.QoS.IntServParmHdr
    gen_parm_composed_MTU: UInt32
class GenTspec(Structure):
    gen_Tspec_serv_hdr: win32more.NetworkManagement.QoS.IntServServiceHdr
    gen_Tspec_parm_hdr: win32more.NetworkManagement.QoS.IntServParmHdr
    gen_Tspec_parms: win32more.NetworkManagement.QoS.GenTspecParms
class GenTspecParms(Structure):
    TB_Tspec_r: Single
    TB_Tspec_b: Single
    TB_Tspec_p: Single
    TB_Tspec_m: UInt32
    TB_Tspec_M: UInt32
class GuarFlowSpec(Structure):
    Guar_serv_hdr: win32more.NetworkManagement.QoS.IntServServiceHdr
    Guar_Tspec_hdr: win32more.NetworkManagement.QoS.IntServParmHdr
    Guar_Tspec_parms: win32more.NetworkManagement.QoS.GenTspecParms
    Guar_Rspec_hdr: win32more.NetworkManagement.QoS.IntServParmHdr
    Guar_Rspec: win32more.NetworkManagement.QoS.GuarRspec
class GuarRspec(Structure):
    Guar_R: Single
    Guar_S: UInt32
class IDPE_ATTR(Structure):
    PeAttribLength: UInt16
    PeAttribType: Byte
    PeAttribSubType: Byte
    PeAttribValue: Byte * 4
class ID_ERROR_OBJECT(Structure):
    usIdErrLength: UInt16
    ucAType: Byte
    ucSubType: Byte
    usReserved: UInt16
    usIdErrorValue: UInt16
    ucIdErrData: Byte * 4
class IN_ADDR_IPV4(Union):
    Addr: UInt32
    AddrBytes: Byte * 4
class IN_ADDR_IPV6(Structure):
    Addr: Byte * 16
class IPX_PATTERN(Structure):
    Src: _Src_e__Struct
    Dest: _Src_e__Struct
    class _Src_e__Struct(Structure):
        NetworkAddress: UInt32
        NodeAddress: Byte * 6
        Socket: UInt16
class IP_PATTERN(Structure):
    Reserved1: UInt32
    Reserved2: UInt32
    SrcAddr: UInt32
    DstAddr: UInt32
    S_un: _S_un_e__Union
    ProtocolId: Byte
    Reserved3: Byte * 3
    class _S_un_e__Union(Union):
        S_un_ports: _S_un_ports_e__Struct
        S_un_icmp: _S_un_icmp_e__Struct
        S_Spi: UInt32
        class _S_un_ports_e__Struct(Structure):
            s_srcport: UInt16
            s_dstport: UInt16
        class _S_un_icmp_e__Struct(Structure):
            s_type: Byte
            s_code: Byte
            filler: UInt16
class IS_ADSPEC_BODY(Structure):
    adspec_mh: win32more.NetworkManagement.QoS.IntServMainHdr
    adspec_genparms: win32more.NetworkManagement.QoS.GenAdspecParams
class IS_FLOWSPEC(Structure):
    flow_header: win32more.NetworkManagement.QoS.RsvpObjHdr
    flow_body: win32more.NetworkManagement.QoS.IntServFlowSpec
class IntServFlowSpec(Structure):
    spec_mh: win32more.NetworkManagement.QoS.IntServMainHdr
    spec_u: _spec_u_e__Union
    class _spec_u_e__Union(Union):
        CL_spec: win32more.NetworkManagement.QoS.CtrlLoadFlowspec
        G_spec: win32more.NetworkManagement.QoS.GuarFlowSpec
        Q_spec: win32more.NetworkManagement.QoS.QualAppFlowSpec
class IntServMainHdr(Structure):
    ismh_version: Byte
    ismh_unused: Byte
    ismh_len32b: UInt16
class IntServParmHdr(Structure):
    isph_parm_num: Byte
    isph_flags: Byte
    isph_len32b: UInt16
class IntServServiceHdr(Structure):
    issh_service: Byte
    issh_flags: Byte
    issh_len32b: UInt16
class IntServTspecBody(Structure):
    st_mh: win32more.NetworkManagement.QoS.IntServMainHdr
    tspec_u: _tspec_u_e__Union
    class _tspec_u_e__Union(Union):
        gen_stspec: win32more.NetworkManagement.QoS.GenTspec
        qual_stspec: win32more.NetworkManagement.QoS.QualTspec
class LPMIPTABLE(Structure):
    ulIfIndex: UInt32
    MediaType: UInt32
    IfIpAddr: win32more.Networking.WinSock.IN_ADDR
    IfNetMask: win32more.Networking.WinSock.IN_ADDR
LPM_HANDLE = IntPtr
class LPM_INIT_INFO(Structure):
    PcmVersionNumber: UInt32
    ResultTimeLimit: UInt32
    ConfiguredLpmCount: Int32
    AllocMemory: win32more.NetworkManagement.QoS.PALLOCMEM
    FreeMemory: win32more.NetworkManagement.QoS.PFREEMEM
    PcmAdmitResultCallback: win32more.NetworkManagement.QoS.CBADMITRESULT
    GetRsvpObjectsCallback: win32more.NetworkManagement.QoS.CBGETRSVPOBJECTS
@winfunctype_pointer
def PALLOCMEM(Size: UInt32) -> c_void_p: ...
class PARAM_BUFFER(Structure):
    ParameterId: UInt32
    Length: UInt32
    Buffer: Byte * 1
@winfunctype_pointer
def PFREEMEM(pv: c_void_p) -> Void: ...
class POLICY_DATA(Structure):
    PolicyObjHdr: win32more.NetworkManagement.QoS.RsvpObjHdr
    usPeOffset: UInt16
    usReserved: UInt16
class POLICY_DECISION(Structure):
    lpvResult: UInt32
    wPolicyErrCode: UInt16
    wPolicyErrValue: UInt16
class POLICY_ELEMENT(Structure):
    usPeLength: UInt16
    usPeType: UInt16
    ucPeData: Byte * 4
class QOS_DESTADDR(Structure):
    ObjectHdr: win32more.NetworkManagement.QoS.QOS_OBJECT_HDR
    SocketAddress: POINTER(win32more.Networking.WinSock.SOCKADDR_head)
    SocketAddressLength: UInt32
class QOS_DIFFSERV(Structure):
    ObjectHdr: win32more.NetworkManagement.QoS.QOS_OBJECT_HDR
    DSFieldCount: UInt32
    DiffservRule: Byte * 1
class QOS_DIFFSERV_RULE(Structure):
    InboundDSField: Byte
    ConformingOutboundDSField: Byte
    NonConformingOutboundDSField: Byte
    ConformingUserPriority: Byte
    NonConformingUserPriority: Byte
class QOS_DS_CLASS(Structure):
    ObjectHdr: win32more.NetworkManagement.QoS.QOS_OBJECT_HDR
    DSField: UInt32
class QOS_FLOWRATE_OUTGOING(Structure):
    Bandwidth: UInt64
    ShapingBehavior: win32more.NetworkManagement.QoS.QOS_SHAPING
    Reason: win32more.NetworkManagement.QoS.QOS_FLOWRATE_REASON
QOS_FLOWRATE_REASON = Int32
QOS_FLOWRATE_REASON_QOSFlowRateNotApplicable: QOS_FLOWRATE_REASON = 0
QOS_FLOWRATE_REASON_QOSFlowRateContentChange: QOS_FLOWRATE_REASON = 1
QOS_FLOWRATE_REASON_QOSFlowRateCongestion: QOS_FLOWRATE_REASON = 2
QOS_FLOWRATE_REASON_QOSFlowRateHigherContentEncoding: QOS_FLOWRATE_REASON = 3
QOS_FLOWRATE_REASON_QOSFlowRateUserCaused: QOS_FLOWRATE_REASON = 4
class QOS_FLOW_FUNDAMENTALS(Structure):
    BottleneckBandwidthSet: win32more.Foundation.BOOL
    BottleneckBandwidth: UInt64
    AvailableBandwidthSet: win32more.Foundation.BOOL
    AvailableBandwidth: UInt64
    RTTSet: win32more.Foundation.BOOL
    RTT: UInt32
class QOS_FRIENDLY_NAME(Structure):
    ObjectHdr: win32more.NetworkManagement.QoS.QOS_OBJECT_HDR
    FriendlyName: Char * 256
QOS_NOTIFY_FLOW = Int32
QOS_NOTIFY_FLOW_QOSNotifyCongested: QOS_NOTIFY_FLOW = 0
QOS_NOTIFY_FLOW_QOSNotifyUncongested: QOS_NOTIFY_FLOW = 1
QOS_NOTIFY_FLOW_QOSNotifyAvailable: QOS_NOTIFY_FLOW = 2
class QOS_OBJECT_HDR(Structure):
    ObjectType: UInt32
    ObjectLength: UInt32
class QOS_PACKET_PRIORITY(Structure):
    ConformantDSCPValue: UInt32
    NonConformantDSCPValue: UInt32
    ConformantL2Value: UInt32
    NonConformantL2Value: UInt32
QOS_QUERY_FLOW = Int32
QOS_QUERY_FLOW_QOSQueryFlowFundamentals: QOS_QUERY_FLOW = 0
QOS_QUERY_FLOW_QOSQueryPacketPriority: QOS_QUERY_FLOW = 1
QOS_QUERY_FLOW_QOSQueryOutgoingRate: QOS_QUERY_FLOW = 2
class QOS_SD_MODE(Structure):
    ObjectHdr: win32more.NetworkManagement.QoS.QOS_OBJECT_HDR
    ShapeDiscardMode: UInt32
QOS_SET_FLOW = Int32
QOS_SET_FLOW_QOSSetTrafficType: QOS_SET_FLOW = 0
QOS_SET_FLOW_QOSSetOutgoingRate: QOS_SET_FLOW = 1
QOS_SET_FLOW_QOSSetOutgoingDSCPValue: QOS_SET_FLOW = 2
QOS_SHAPING = Int32
QOS_SHAPING_QOSShapeOnly: QOS_SHAPING = 0
QOS_SHAPING_QOSShapeAndMark: QOS_SHAPING = 1
QOS_SHAPING_QOSUseNonConformantMarkings: QOS_SHAPING = 2
class QOS_SHAPING_RATE(Structure):
    ObjectHdr: win32more.NetworkManagement.QoS.QOS_OBJECT_HDR
    ShapingRate: UInt32
class QOS_TCP_TRAFFIC(Structure):
    ObjectHdr: win32more.NetworkManagement.QoS.QOS_OBJECT_HDR
class QOS_TRAFFIC_CLASS(Structure):
    ObjectHdr: win32more.NetworkManagement.QoS.QOS_OBJECT_HDR
    TrafficClass: UInt32
QOS_TRAFFIC_TYPE = Int32
QOS_TRAFFIC_TYPE_QOSTrafficTypeBestEffort: QOS_TRAFFIC_TYPE = 0
QOS_TRAFFIC_TYPE_QOSTrafficTypeBackground: QOS_TRAFFIC_TYPE = 1
QOS_TRAFFIC_TYPE_QOSTrafficTypeExcellentEffort: QOS_TRAFFIC_TYPE = 2
QOS_TRAFFIC_TYPE_QOSTrafficTypeAudioVideo: QOS_TRAFFIC_TYPE = 3
QOS_TRAFFIC_TYPE_QOSTrafficTypeVoice: QOS_TRAFFIC_TYPE = 4
QOS_TRAFFIC_TYPE_QOSTrafficTypeControl: QOS_TRAFFIC_TYPE = 5
class QOS_VERSION(Structure):
    MajorVersion: UInt16
    MinorVersion: UInt16
class QualAppFlowSpec(Structure):
    Q_spec_serv_hdr: win32more.NetworkManagement.QoS.IntServServiceHdr
    Q_spec_parm_hdr: win32more.NetworkManagement.QoS.IntServParmHdr
    Q_spec_parms: win32more.NetworkManagement.QoS.QualTspecParms
class QualTspec(Structure):
    qual_Tspec_serv_hdr: win32more.NetworkManagement.QoS.IntServServiceHdr
    qual_Tspec_parm_hdr: win32more.NetworkManagement.QoS.IntServParmHdr
    qual_Tspec_parms: win32more.NetworkManagement.QoS.QualTspecParms
class QualTspecParms(Structure):
    TB_Tspec_M: UInt32
class RESV_STYLE(Structure):
    style_header: win32more.NetworkManagement.QoS.RsvpObjHdr
    style_word: UInt32
RHANDLE = IntPtr
class RSVP_ADSPEC(Structure):
    ObjectHdr: win32more.NetworkManagement.QoS.QOS_OBJECT_HDR
    GeneralParams: win32more.NetworkManagement.QoS.AD_GENERAL_PARAMS
    NumberOfServices: UInt32
    Services: win32more.NetworkManagement.QoS.CONTROL_SERVICE * 1
class RSVP_FILTERSPEC(Structure):
    Type: win32more.NetworkManagement.QoS.FilterType
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        FilterSpecV4: win32more.NetworkManagement.QoS.RSVP_FILTERSPEC_V4
        FilterSpecV6: win32more.NetworkManagement.QoS.RSVP_FILTERSPEC_V6
        FilterSpecV6Flow: win32more.NetworkManagement.QoS.RSVP_FILTERSPEC_V6_FLOW
        FilterSpecV4Gpi: win32more.NetworkManagement.QoS.RSVP_FILTERSPEC_V4_GPI
        FilterSpecV6Gpi: win32more.NetworkManagement.QoS.RSVP_FILTERSPEC_V6_GPI
class RSVP_FILTERSPEC_V4(Structure):
    Address: win32more.NetworkManagement.QoS.IN_ADDR_IPV4
    Unused: UInt16
    Port: UInt16
class RSVP_FILTERSPEC_V4_GPI(Structure):
    Address: win32more.NetworkManagement.QoS.IN_ADDR_IPV4
    GeneralPortId: UInt32
class RSVP_FILTERSPEC_V6(Structure):
    Address: win32more.NetworkManagement.QoS.IN_ADDR_IPV6
    UnUsed: UInt16
    Port: UInt16
class RSVP_FILTERSPEC_V6_FLOW(Structure):
    Address: win32more.NetworkManagement.QoS.IN_ADDR_IPV6
    UnUsed: Byte
    FlowLabel: Byte * 3
class RSVP_FILTERSPEC_V6_GPI(Structure):
    Address: win32more.NetworkManagement.QoS.IN_ADDR_IPV6
    GeneralPortId: UInt32
class RSVP_HOP(Structure):
    hop_header: win32more.NetworkManagement.QoS.RsvpObjHdr
    hop_u: _hop_u_e__Union
    class _hop_u_e__Union(Union):
        hop_ipv4: win32more.NetworkManagement.QoS.Rsvp_Hop_IPv4
class RSVP_MSG_OBJS(Structure):
    RsvpMsgType: Int32
    pRsvpSession: POINTER(win32more.NetworkManagement.QoS.RSVP_SESSION_head)
    pRsvpFromHop: POINTER(win32more.NetworkManagement.QoS.RSVP_HOP_head)
    pRsvpToHop: POINTER(win32more.NetworkManagement.QoS.RSVP_HOP_head)
    pResvStyle: POINTER(win32more.NetworkManagement.QoS.RESV_STYLE_head)
    pRsvpScope: POINTER(win32more.NetworkManagement.QoS.RSVP_SCOPE_head)
    FlowDescCount: Int32
    pFlowDescs: POINTER(win32more.NetworkManagement.QoS.FLOW_DESC_head)
    PdObjectCount: Int32
    ppPdObjects: POINTER(POINTER(win32more.NetworkManagement.QoS.POLICY_DATA_head))
    pErrorSpec: POINTER(win32more.NetworkManagement.QoS.ERROR_SPEC_head)
    pAdspec: POINTER(win32more.NetworkManagement.QoS.ADSPEC_head)
class RSVP_POLICY(Structure):
    Len: UInt16
    Type: UInt16
    Info: Byte * 4
class RSVP_POLICY_INFO(Structure):
    ObjectHdr: win32more.NetworkManagement.QoS.QOS_OBJECT_HDR
    NumPolicyElement: UInt32
    PolicyElement: win32more.NetworkManagement.QoS.RSVP_POLICY * 1
class RSVP_RESERVE_INFO(Structure):
    ObjectHdr: win32more.NetworkManagement.QoS.QOS_OBJECT_HDR
    Style: UInt32
    ConfirmRequest: UInt32
    PolicyElementList: POINTER(win32more.NetworkManagement.QoS.RSVP_POLICY_INFO_head)
    NumFlowDesc: UInt32
    FlowDescList: POINTER(win32more.NetworkManagement.QoS.FLOWDESCRIPTOR_head)
class RSVP_SCOPE(Structure):
    scopl_header: win32more.NetworkManagement.QoS.RsvpObjHdr
    scope_u: _scope_u_e__Union
    class _scope_u_e__Union(Union):
        scopl_ipv4: win32more.NetworkManagement.QoS.Scope_list_ipv4
class RSVP_SESSION(Structure):
    sess_header: win32more.NetworkManagement.QoS.RsvpObjHdr
    sess_u: _sess_u_e__Union
    class _sess_u_e__Union(Union):
        sess_ipv4: win32more.NetworkManagement.QoS.Session_IPv4
class RSVP_STATUS_INFO(Structure):
    ObjectHdr: win32more.NetworkManagement.QoS.QOS_OBJECT_HDR
    StatusCode: UInt32
    ExtendedStatus1: UInt32
    ExtendedStatus2: UInt32
class RsvpObjHdr(Structure):
    obj_length: UInt16
    obj_class: Byte
    obj_ctype: Byte
class Rsvp_Hop_IPv4(Structure):
    hop_ipaddr: win32more.Networking.WinSock.IN_ADDR
    hop_LIH: UInt32
class SENDER_TSPEC(Structure):
    stspec_header: win32more.NetworkManagement.QoS.RsvpObjHdr
    stspec_body: win32more.NetworkManagement.QoS.IntServTspecBody
class SIPAEVENT_KSR_SIGNATURE_PAYLOAD(Structure):
    SignAlgID: UInt32
    SignatureLength: UInt32
    Signature: Byte * 1
    _pack_ = 1
class SIPAEVENT_REVOCATION_LIST_PAYLOAD(Structure):
    CreationTime: Int64
    DigestLength: UInt32
    HashAlgID: UInt16
    Digest: Byte * 1
    _pack_ = 1
class SIPAEVENT_SBCP_INFO_PAYLOAD_V1(Structure):
    PayloadVersion: UInt32
    VarDataOffset: UInt32
    HashAlgID: UInt16
    DigestLength: UInt16
    Options: UInt32
    SignersCount: UInt32
    VarData: Byte * 1
    _pack_ = 1
class SIPAEVENT_SI_POLICY_PAYLOAD(Structure):
    PolicyVersion: UInt64
    PolicyNameLength: UInt16
    HashAlgID: UInt16
    DigestLength: UInt32
    VarLengthData: Byte * 1
    _pack_ = 1
class SIPAEVENT_VSM_IDK_INFO_PAYLOAD(Structure):
    KeyAlgID: UInt32
    Anonymous: _Anonymous_e__Union
    _pack_ = 1
    class _Anonymous_e__Union(Union):
        RsaKeyInfo: win32more.NetworkManagement.QoS.SIPAEVENT_VSM_IDK_RSA_INFO
class SIPAEVENT_VSM_IDK_RSA_INFO(Structure):
    KeyBitLength: UInt32
    PublicExpLengthBytes: UInt32
    ModulusSizeBytes: UInt32
    PublicKeyData: Byte * 1
    _pack_ = 1
class Scope_list_ipv4(Structure):
    scopl_ipaddr: win32more.Networking.WinSock.IN_ADDR * 1
class Session_IPv4(Structure):
    sess_destaddr: win32more.Networking.WinSock.IN_ADDR
    sess_protid: Byte
    sess_flags: Byte
    sess_destport: UInt16
class TCG_PCClientPCREventStruct(Structure):
    pcrIndex: UInt32
    eventType: UInt32
    digest: Byte * 20
    eventDataSize: UInt32
    event: Byte * 1
    _pack_ = 1
class TCG_PCClientTaggedEventStruct(Structure):
    EventID: UInt32
    EventDataSize: UInt32
    EventData: Byte * 1
    _pack_ = 1
@winfunctype_pointer
def TCI_ADD_FLOW_COMPLETE_HANDLER(ClFlowCtx: win32more.Foundation.HANDLE, Status: UInt32) -> Void: ...
class TCI_CLIENT_FUNC_LIST(Structure):
    ClNotifyHandler: win32more.NetworkManagement.QoS.TCI_NOTIFY_HANDLER
    ClAddFlowCompleteHandler: win32more.NetworkManagement.QoS.TCI_ADD_FLOW_COMPLETE_HANDLER
    ClModifyFlowCompleteHandler: win32more.NetworkManagement.QoS.TCI_MOD_FLOW_COMPLETE_HANDLER
    ClDeleteFlowCompleteHandler: win32more.NetworkManagement.QoS.TCI_DEL_FLOW_COMPLETE_HANDLER
@winfunctype_pointer
def TCI_DEL_FLOW_COMPLETE_HANDLER(ClFlowCtx: win32more.Foundation.HANDLE, Status: UInt32) -> Void: ...
@winfunctype_pointer
def TCI_MOD_FLOW_COMPLETE_HANDLER(ClFlowCtx: win32more.Foundation.HANDLE, Status: UInt32) -> Void: ...
@winfunctype_pointer
def TCI_NOTIFY_HANDLER(ClRegCtx: win32more.Foundation.HANDLE, ClIfcCtx: win32more.Foundation.HANDLE, Event: UInt32, SubCode: win32more.Foundation.HANDLE, BufSize: UInt32, Buffer: c_void_p) -> Void: ...
class TC_GEN_FILTER(Structure):
    AddressType: UInt16
    PatternSize: UInt32
    Pattern: c_void_p
    Mask: c_void_p
class TC_GEN_FLOW(Structure):
    SendingFlowspec: win32more.Networking.WinSock.FLOWSPEC
    ReceivingFlowspec: win32more.Networking.WinSock.FLOWSPEC
    TcObjectsLength: UInt32
    TcObjects: win32more.NetworkManagement.QoS.QOS_OBJECT_HDR * 1
class TC_IFC_DESCRIPTOR(Structure):
    Length: UInt32
    pInterfaceName: win32more.Foundation.PWSTR
    pInterfaceID: win32more.Foundation.PWSTR
    AddressListDesc: win32more.NetworkManagement.QoS.ADDRESS_LIST_DESCRIPTOR
class TC_SUPPORTED_INFO_BUFFER(Structure):
    InstanceIDLength: UInt16
    InstanceID: Char * 256
    InterfaceLuid: UInt64
    AddrListDesc: win32more.NetworkManagement.QoS.ADDRESS_LIST_DESCRIPTOR
class WBCL_Iterator(Structure):
    firstElementPtr: c_void_p
    logSize: UInt32
    currentElementPtr: c_void_p
    currentElementSize: UInt32
    digestSize: UInt16
    logFormat: UInt16
    numberOfDigests: UInt32
    digestSizes: c_void_p
    supportedAlgorithms: UInt32
    hashAlgorithm: UInt16
    _pack_ = 1
class WBCL_LogHdr(Structure):
    signature: UInt32
    version: UInt32
    entries: UInt32
    length: UInt32
    _pack_ = 1
int_serv_wkp = Int32
IS_WKP_HOP_CNT: int_serv_wkp = 4
IS_WKP_PATH_BW: int_serv_wkp = 6
IS_WKP_MIN_LATENCY: int_serv_wkp = 8
IS_WKP_COMPOSED_MTU: int_serv_wkp = 10
IS_WKP_TB_TSPEC: int_serv_wkp = 127
IS_WKP_Q_TSPEC: int_serv_wkp = 128
make_head(_module, 'ADDRESS_LIST_DESCRIPTOR')
make_head(_module, 'ADSPEC')
make_head(_module, 'AD_GENERAL_PARAMS')
make_head(_module, 'AD_GUARANTEED')
make_head(_module, 'CBADMITRESULT')
make_head(_module, 'CBGETRSVPOBJECTS')
make_head(_module, 'CONTROL_SERVICE')
make_head(_module, 'CtrlLoadFlowspec')
make_head(_module, 'ENUMERATION_BUFFER')
make_head(_module, 'ERROR_SPEC')
make_head(_module, 'Error_Spec_IPv4')
make_head(_module, 'FILTER_SPEC')
make_head(_module, 'FLOWDESCRIPTOR')
make_head(_module, 'FLOW_DESC')
make_head(_module, 'Filter_Spec_IPv4')
make_head(_module, 'Filter_Spec_IPv4GPI')
make_head(_module, 'Gads_parms_t')
make_head(_module, 'GenAdspecParams')
make_head(_module, 'GenTspec')
make_head(_module, 'GenTspecParms')
make_head(_module, 'GuarFlowSpec')
make_head(_module, 'GuarRspec')
make_head(_module, 'IDPE_ATTR')
make_head(_module, 'ID_ERROR_OBJECT')
make_head(_module, 'IN_ADDR_IPV4')
make_head(_module, 'IN_ADDR_IPV6')
make_head(_module, 'IPX_PATTERN')
make_head(_module, 'IP_PATTERN')
make_head(_module, 'IS_ADSPEC_BODY')
make_head(_module, 'IS_FLOWSPEC')
make_head(_module, 'IntServFlowSpec')
make_head(_module, 'IntServMainHdr')
make_head(_module, 'IntServParmHdr')
make_head(_module, 'IntServServiceHdr')
make_head(_module, 'IntServTspecBody')
make_head(_module, 'LPMIPTABLE')
make_head(_module, 'LPM_INIT_INFO')
make_head(_module, 'PALLOCMEM')
make_head(_module, 'PARAM_BUFFER')
make_head(_module, 'PFREEMEM')
make_head(_module, 'POLICY_DATA')
make_head(_module, 'POLICY_DECISION')
make_head(_module, 'POLICY_ELEMENT')
make_head(_module, 'QOS_DESTADDR')
make_head(_module, 'QOS_DIFFSERV')
make_head(_module, 'QOS_DIFFSERV_RULE')
make_head(_module, 'QOS_DS_CLASS')
make_head(_module, 'QOS_FLOWRATE_OUTGOING')
make_head(_module, 'QOS_FLOW_FUNDAMENTALS')
make_head(_module, 'QOS_FRIENDLY_NAME')
make_head(_module, 'QOS_OBJECT_HDR')
make_head(_module, 'QOS_PACKET_PRIORITY')
make_head(_module, 'QOS_SD_MODE')
make_head(_module, 'QOS_SHAPING_RATE')
make_head(_module, 'QOS_TCP_TRAFFIC')
make_head(_module, 'QOS_TRAFFIC_CLASS')
make_head(_module, 'QOS_VERSION')
make_head(_module, 'QualAppFlowSpec')
make_head(_module, 'QualTspec')
make_head(_module, 'QualTspecParms')
make_head(_module, 'RESV_STYLE')
make_head(_module, 'RSVP_ADSPEC')
make_head(_module, 'RSVP_FILTERSPEC')
make_head(_module, 'RSVP_FILTERSPEC_V4')
make_head(_module, 'RSVP_FILTERSPEC_V4_GPI')
make_head(_module, 'RSVP_FILTERSPEC_V6')
make_head(_module, 'RSVP_FILTERSPEC_V6_FLOW')
make_head(_module, 'RSVP_FILTERSPEC_V6_GPI')
make_head(_module, 'RSVP_HOP')
make_head(_module, 'RSVP_MSG_OBJS')
make_head(_module, 'RSVP_POLICY')
make_head(_module, 'RSVP_POLICY_INFO')
make_head(_module, 'RSVP_RESERVE_INFO')
make_head(_module, 'RSVP_SCOPE')
make_head(_module, 'RSVP_SESSION')
make_head(_module, 'RSVP_STATUS_INFO')
make_head(_module, 'RsvpObjHdr')
make_head(_module, 'Rsvp_Hop_IPv4')
make_head(_module, 'SENDER_TSPEC')
make_head(_module, 'SIPAEVENT_KSR_SIGNATURE_PAYLOAD')
make_head(_module, 'SIPAEVENT_REVOCATION_LIST_PAYLOAD')
make_head(_module, 'SIPAEVENT_SBCP_INFO_PAYLOAD_V1')
make_head(_module, 'SIPAEVENT_SI_POLICY_PAYLOAD')
make_head(_module, 'SIPAEVENT_VSM_IDK_INFO_PAYLOAD')
make_head(_module, 'SIPAEVENT_VSM_IDK_RSA_INFO')
make_head(_module, 'Scope_list_ipv4')
make_head(_module, 'Session_IPv4')
make_head(_module, 'TCG_PCClientPCREventStruct')
make_head(_module, 'TCG_PCClientTaggedEventStruct')
make_head(_module, 'TCI_ADD_FLOW_COMPLETE_HANDLER')
make_head(_module, 'TCI_CLIENT_FUNC_LIST')
make_head(_module, 'TCI_DEL_FLOW_COMPLETE_HANDLER')
make_head(_module, 'TCI_MOD_FLOW_COMPLETE_HANDLER')
make_head(_module, 'TCI_NOTIFY_HANDLER')
make_head(_module, 'TC_GEN_FILTER')
make_head(_module, 'TC_GEN_FLOW')
make_head(_module, 'TC_IFC_DESCRIPTOR')
make_head(_module, 'TC_SUPPORTED_INFO_BUFFER')
make_head(_module, 'WBCL_Iterator')
make_head(_module, 'WBCL_LogHdr')
__all__ = [
    "ABLE_TO_RECV_RSVP",
    "ADDRESS_LIST_DESCRIPTOR",
    "ADM_CTRL_FAILED",
    "ADSPEC",
    "AD_FLAG_BREAK_BIT",
    "AD_GENERAL_PARAMS",
    "AD_GUARANTEED",
    "ALLOWED_TO_SEND_DATA",
    "ANY_DEST_ADDR",
    "CBADMITRESULT",
    "CBGETRSVPOBJECTS",
    "CONTROLLED_DELAY_SERV",
    "CONTROLLED_LOAD_SERV",
    "CONTROL_SERVICE",
    "CREDENTIAL_SUB_TYPE_ASCII_ID",
    "CREDENTIAL_SUB_TYPE_KERBEROS_TKT",
    "CREDENTIAL_SUB_TYPE_PGP_CERT",
    "CREDENTIAL_SUB_TYPE_UNICODE_ID",
    "CREDENTIAL_SUB_TYPE_X509_V3_CERT",
    "CURRENT_TCI_VERSION",
    "CtrlLoadFlowspec",
    "DD_TCP_DEVICE_NAME",
    "DUP_RESULTS",
    "END_TO_END_QOSABILITY",
    "ENUMERATION_BUFFER",
    "ERROR_ADDRESS_TYPE_NOT_SUPPORTED",
    "ERROR_DS_MAPPING_EXISTS",
    "ERROR_DUPLICATE_FILTER",
    "ERROR_FILTER_CONFLICT",
    "ERROR_INCOMPATABLE_QOS",
    "ERROR_INCOMPATIBLE_TCI_VERSION",
    "ERROR_INVALID_ADDRESS_TYPE",
    "ERROR_INVALID_DIFFSERV_FLOW",
    "ERROR_INVALID_DS_CLASS",
    "ERROR_INVALID_FLOW_MODE",
    "ERROR_INVALID_PEAK_RATE",
    "ERROR_INVALID_QOS_PRIORITY",
    "ERROR_INVALID_SD_MODE",
    "ERROR_INVALID_SERVICE_TYPE",
    "ERROR_INVALID_SHAPE_RATE",
    "ERROR_INVALID_TOKEN_RATE",
    "ERROR_INVALID_TRAFFIC_CLASS",
    "ERROR_NO_MORE_INFO",
    "ERROR_SPEC",
    "ERROR_SPECF_InPlace",
    "ERROR_SPECF_NotGuilty",
    "ERROR_TC_NOT_SUPPORTED",
    "ERROR_TC_OBJECT_LENGTH_INVALID",
    "ERROR_TC_SUPPORTED_OBJECTS_EXIST",
    "ERROR_TOO_MANY_CLIENTS",
    "ERR_FORWARD_OK",
    "ERR_Usage_globl",
    "ERR_Usage_local",
    "ERR_Usage_serv",
    "ERR_global_mask",
    "EXPIRED_CREDENTIAL",
    "Error_Spec_IPv4",
    "FILTERSPECV4",
    "FILTERSPECV4_GPI",
    "FILTERSPECV6",
    "FILTERSPECV6_FLOW",
    "FILTERSPECV6_GPI",
    "FILTERSPEC_END",
    "FILTER_SPEC",
    "FLOWDESCRIPTOR",
    "FLOW_DESC",
    "FLOW_DURATION",
    "FORCE_IMMEDIATE_REFRESH",
    "FSCTL_TCP_BASE",
    "FVEB_UNLOCK_FLAG_AUK_OSFVEINFO",
    "FVEB_UNLOCK_FLAG_CACHED",
    "FVEB_UNLOCK_FLAG_EXTERNAL",
    "FVEB_UNLOCK_FLAG_MEDIA",
    "FVEB_UNLOCK_FLAG_NBP",
    "FVEB_UNLOCK_FLAG_NONE",
    "FVEB_UNLOCK_FLAG_PASSPHRASE",
    "FVEB_UNLOCK_FLAG_PIN",
    "FVEB_UNLOCK_FLAG_RECOVERY",
    "FVEB_UNLOCK_FLAG_TPM",
    "FilterType",
    "Filter_Spec_IPv4",
    "Filter_Spec_IPv4GPI",
    "GENERAL_INFO",
    "GQOS_API",
    "GQOS_ERRORCODE_UNKNOWN",
    "GQOS_ERRORVALUE_UNKNOWN",
    "GQOS_KERNEL_TC",
    "GQOS_KERNEL_TC_SYS",
    "GQOS_NET_ADMISSION",
    "GQOS_NET_POLICY",
    "GQOS_NO_ERRORCODE",
    "GQOS_NO_ERRORVALUE",
    "GQOS_RSVP",
    "GQOS_RSVP_SYS",
    "GUARANTEED_SERV",
    "GUAR_ADSPARM_C",
    "GUAR_ADSPARM_Csum",
    "GUAR_ADSPARM_Ctot",
    "GUAR_ADSPARM_D",
    "GUAR_ADSPARM_Dsum",
    "GUAR_ADSPARM_Dtot",
    "GUID_QOS_BESTEFFORT_BANDWIDTH",
    "GUID_QOS_ENABLE_AVG_STATS",
    "GUID_QOS_ENABLE_WINDOW_ADJUSTMENT",
    "GUID_QOS_FLOW_8021P_CONFORMING",
    "GUID_QOS_FLOW_8021P_NONCONFORMING",
    "GUID_QOS_FLOW_COUNT",
    "GUID_QOS_FLOW_IP_CONFORMING",
    "GUID_QOS_FLOW_IP_NONCONFORMING",
    "GUID_QOS_FLOW_MODE",
    "GUID_QOS_ISSLOW_FLOW",
    "GUID_QOS_LATENCY",
    "GUID_QOS_MAX_OUTSTANDING_SENDS",
    "GUID_QOS_NON_BESTEFFORT_LIMIT",
    "GUID_QOS_REMAINING_BANDWIDTH",
    "GUID_QOS_STATISTICS_BUFFER",
    "GUID_QOS_TIMER_RESOLUTION",
    "Gads_parms_t",
    "GenAdspecParams",
    "GenTspec",
    "GenTspecParms",
    "GuarFlowSpec",
    "GuarRspec",
    "HIGHLY_DELAY_SENSITIVE",
    "IDENTITY_CHANGED",
    "IDPE_ATTR",
    "ID_ERROR_OBJECT",
    "IF_MIB_STATS_ID",
    "INFO_NOT_AVAILABLE",
    "INSUFFICIENT_PRIVILEGES",
    "INTSERV_VERSION0",
    "INTSERV_VERS_MASK",
    "INV_LPM_HANDLE",
    "INV_REQ_HANDLE",
    "INV_RESULTS",
    "IN_ADDR_IPV4",
    "IN_ADDR_IPV6",
    "IPX_PATTERN",
    "IP_INTFC_INFO_ID",
    "IP_MIB_ADDRTABLE_ENTRY_ID",
    "IP_MIB_STATS_ID",
    "IP_PATTERN",
    "ISPH_FLG_INV",
    "ISSH_BREAK_BIT",
    "IS_ADSPEC_BODY",
    "IS_FLOWSPEC",
    "IS_GUAR_RSPEC",
    "IS_WKP_COMPOSED_MTU",
    "IS_WKP_HOP_CNT",
    "IS_WKP_MIN_LATENCY",
    "IS_WKP_PATH_BW",
    "IS_WKP_Q_TSPEC",
    "IS_WKP_TB_TSPEC",
    "IntServFlowSpec",
    "IntServMainHdr",
    "IntServParmHdr",
    "IntServServiceHdr",
    "IntServTspecBody",
    "LINE_RATE",
    "LOCAL_QOSABILITY",
    "LOCAL_TRAFFIC_CONTROL",
    "LPMIPTABLE",
    "LPM_API_VERSION_1",
    "LPM_HANDLE",
    "LPM_INIT_INFO",
    "LPM_OK",
    "LPM_PE_ALL_TYPES",
    "LPM_PE_APP_IDENTITY",
    "LPM_PE_USER_IDENTITY",
    "LPM_RESULT_DEFER",
    "LPM_RESULT_READY",
    "LPM_TIME_OUT",
    "LPV_DONT_CARE",
    "LPV_DROP_MSG",
    "LPV_MAX_PRIORITY",
    "LPV_MIN_PRIORITY",
    "LPV_REJECT",
    "LPV_RESERVED",
    "MAX_PHYSADDR_SIZE",
    "MAX_STRING_LENGTH",
    "MODERATELY_DELAY_SENSITIVE",
    "OSDEVICE_TYPE_BLOCKIO_CDROM",
    "OSDEVICE_TYPE_BLOCKIO_FILE",
    "OSDEVICE_TYPE_BLOCKIO_HARDDISK",
    "OSDEVICE_TYPE_BLOCKIO_PARTITION",
    "OSDEVICE_TYPE_BLOCKIO_RAMDISK",
    "OSDEVICE_TYPE_BLOCKIO_REMOVABLEDISK",
    "OSDEVICE_TYPE_BLOCKIO_VIRTUALHARDDISK",
    "OSDEVICE_TYPE_COMPOSITE",
    "OSDEVICE_TYPE_SERIAL",
    "OSDEVICE_TYPE_UDP",
    "OSDEVICE_TYPE_UNKNOWN",
    "OSDEVICE_TYPE_VMBUS",
    "Opt_Distinct",
    "Opt_Explicit",
    "Opt_Share_mask",
    "Opt_Shared",
    "Opt_SndSel_mask",
    "Opt_Wildcard",
    "PALLOCMEM",
    "PARAM_BUFFER",
    "PCM_VERSION_1",
    "PE_ATTRIB_TYPE_CREDENTIAL",
    "PE_ATTRIB_TYPE_POLICY_LOCATOR",
    "PE_TYPE_APPID",
    "PFREEMEM",
    "POLICY_DATA",
    "POLICY_DECISION",
    "POLICY_ELEMENT",
    "POLICY_ERRV_CRAZY_FLOWSPEC",
    "POLICY_ERRV_EXPIRED_CREDENTIALS",
    "POLICY_ERRV_EXPIRED_USER_TOKEN",
    "POLICY_ERRV_GLOBAL_DEF_FLOW_COUNT",
    "POLICY_ERRV_GLOBAL_DEF_FLOW_DURATION",
    "POLICY_ERRV_GLOBAL_DEF_FLOW_RATE",
    "POLICY_ERRV_GLOBAL_DEF_PEAK_RATE",
    "POLICY_ERRV_GLOBAL_DEF_SUM_FLOW_RATE",
    "POLICY_ERRV_GLOBAL_DEF_SUM_PEAK_RATE",
    "POLICY_ERRV_GLOBAL_GRP_FLOW_COUNT",
    "POLICY_ERRV_GLOBAL_GRP_FLOW_DURATION",
    "POLICY_ERRV_GLOBAL_GRP_FLOW_RATE",
    "POLICY_ERRV_GLOBAL_GRP_PEAK_RATE",
    "POLICY_ERRV_GLOBAL_GRP_SUM_FLOW_RATE",
    "POLICY_ERRV_GLOBAL_GRP_SUM_PEAK_RATE",
    "POLICY_ERRV_GLOBAL_UNAUTH_USER_FLOW_COUNT",
    "POLICY_ERRV_GLOBAL_UNAUTH_USER_FLOW_DURATION",
    "POLICY_ERRV_GLOBAL_UNAUTH_USER_FLOW_RATE",
    "POLICY_ERRV_GLOBAL_UNAUTH_USER_PEAK_RATE",
    "POLICY_ERRV_GLOBAL_UNAUTH_USER_SUM_FLOW_RATE",
    "POLICY_ERRV_GLOBAL_UNAUTH_USER_SUM_PEAK_RATE",
    "POLICY_ERRV_GLOBAL_USER_FLOW_COUNT",
    "POLICY_ERRV_GLOBAL_USER_FLOW_DURATION",
    "POLICY_ERRV_GLOBAL_USER_FLOW_RATE",
    "POLICY_ERRV_GLOBAL_USER_PEAK_RATE",
    "POLICY_ERRV_GLOBAL_USER_SUM_FLOW_RATE",
    "POLICY_ERRV_GLOBAL_USER_SUM_PEAK_RATE",
    "POLICY_ERRV_IDENTITY_CHANGED",
    "POLICY_ERRV_INSUFFICIENT_PRIVILEGES",
    "POLICY_ERRV_NO_ACCEPTS",
    "POLICY_ERRV_NO_MEMORY",
    "POLICY_ERRV_NO_MORE_INFO",
    "POLICY_ERRV_NO_PRIVILEGES",
    "POLICY_ERRV_NO_RESOURCES",
    "POLICY_ERRV_PRE_EMPTED",
    "POLICY_ERRV_SUBNET_DEF_FLOW_COUNT",
    "POLICY_ERRV_SUBNET_DEF_FLOW_DURATION",
    "POLICY_ERRV_SUBNET_DEF_FLOW_RATE",
    "POLICY_ERRV_SUBNET_DEF_PEAK_RATE",
    "POLICY_ERRV_SUBNET_DEF_SUM_FLOW_RATE",
    "POLICY_ERRV_SUBNET_DEF_SUM_PEAK_RATE",
    "POLICY_ERRV_SUBNET_GRP_FLOW_COUNT",
    "POLICY_ERRV_SUBNET_GRP_FLOW_DURATION",
    "POLICY_ERRV_SUBNET_GRP_FLOW_RATE",
    "POLICY_ERRV_SUBNET_GRP_PEAK_RATE",
    "POLICY_ERRV_SUBNET_GRP_SUM_FLOW_RATE",
    "POLICY_ERRV_SUBNET_GRP_SUM_PEAK_RATE",
    "POLICY_ERRV_SUBNET_UNAUTH_USER_FLOW_COUNT",
    "POLICY_ERRV_SUBNET_UNAUTH_USER_FLOW_DURATION",
    "POLICY_ERRV_SUBNET_UNAUTH_USER_FLOW_RATE",
    "POLICY_ERRV_SUBNET_UNAUTH_USER_PEAK_RATE",
    "POLICY_ERRV_SUBNET_UNAUTH_USER_SUM_FLOW_RATE",
    "POLICY_ERRV_SUBNET_UNAUTH_USER_SUM_PEAK_RATE",
    "POLICY_ERRV_SUBNET_USER_FLOW_COUNT",
    "POLICY_ERRV_SUBNET_USER_FLOW_DURATION",
    "POLICY_ERRV_SUBNET_USER_FLOW_RATE",
    "POLICY_ERRV_SUBNET_USER_PEAK_RATE",
    "POLICY_ERRV_SUBNET_USER_SUM_FLOW_RATE",
    "POLICY_ERRV_SUBNET_USER_SUM_PEAK_RATE",
    "POLICY_ERRV_UNKNOWN",
    "POLICY_ERRV_UNKNOWN_USER",
    "POLICY_ERRV_UNSUPPORTED_CREDENTIAL_TYPE",
    "POLICY_ERRV_USER_CHANGED",
    "POLICY_LOCATOR_SUB_TYPE_ASCII_DN",
    "POLICY_LOCATOR_SUB_TYPE_ASCII_DN_ENC",
    "POLICY_LOCATOR_SUB_TYPE_UNICODE_DN",
    "POLICY_LOCATOR_SUB_TYPE_UNICODE_DN_ENC",
    "POSITIVE_INFINITY_RATE",
    "PREDICTIVE_SERV",
    "QOSAddSocketToFlow",
    "QOSCancel",
    "QOSCloseHandle",
    "QOSCreateHandle",
    "QOSEnumerateFlows",
    "QOSNotifyFlow",
    "QOSQueryFlow",
    "QOSRemoveSocketFromFlow",
    "QOSSPBASE",
    "QOSSP_ERR_BASE",
    "QOSSetFlow",
    "QOSStartTrackingClient",
    "QOSStopTrackingClient",
    "QOS_DESTADDR",
    "QOS_DIFFSERV",
    "QOS_DIFFSERV_RULE",
    "QOS_DS_CLASS",
    "QOS_FLOWRATE_OUTGOING",
    "QOS_FLOWRATE_REASON",
    "QOS_FLOWRATE_REASON_QOSFlowRateCongestion",
    "QOS_FLOWRATE_REASON_QOSFlowRateContentChange",
    "QOS_FLOWRATE_REASON_QOSFlowRateHigherContentEncoding",
    "QOS_FLOWRATE_REASON_QOSFlowRateNotApplicable",
    "QOS_FLOWRATE_REASON_QOSFlowRateUserCaused",
    "QOS_FLOW_FUNDAMENTALS",
    "QOS_FRIENDLY_NAME",
    "QOS_GENERAL_ID_BASE",
    "QOS_MAX_OBJECT_STRING_LENGTH",
    "QOS_NON_ADAPTIVE_FLOW",
    "QOS_NOTIFY_FLOW",
    "QOS_NOTIFY_FLOW_QOSNotifyAvailable",
    "QOS_NOTIFY_FLOW_QOSNotifyCongested",
    "QOS_NOTIFY_FLOW_QOSNotifyUncongested",
    "QOS_NOT_SPECIFIED",
    "QOS_OBJECT_HDR",
    "QOS_OUTGOING_DEFAULT_MINIMUM_BANDWIDTH",
    "QOS_PACKET_PRIORITY",
    "QOS_QUERYFLOW_FRESH",
    "QOS_QUERY_FLOW",
    "QOS_QUERY_FLOW_QOSQueryFlowFundamentals",
    "QOS_QUERY_FLOW_QOSQueryOutgoingRate",
    "QOS_QUERY_FLOW_QOSQueryPacketPriority",
    "QOS_SD_MODE",
    "QOS_SET_FLOW",
    "QOS_SET_FLOW_QOSSetOutgoingDSCPValue",
    "QOS_SET_FLOW_QOSSetOutgoingRate",
    "QOS_SET_FLOW_QOSSetTrafficType",
    "QOS_SHAPING",
    "QOS_SHAPING_QOSShapeAndMark",
    "QOS_SHAPING_QOSShapeOnly",
    "QOS_SHAPING_QOSUseNonConformantMarkings",
    "QOS_SHAPING_RATE",
    "QOS_TCP_TRAFFIC",
    "QOS_TRAFFIC_CLASS",
    "QOS_TRAFFIC_GENERAL_ID_BASE",
    "QOS_TRAFFIC_TYPE",
    "QOS_TRAFFIC_TYPE_QOSTrafficTypeAudioVideo",
    "QOS_TRAFFIC_TYPE_QOSTrafficTypeBackground",
    "QOS_TRAFFIC_TYPE_QOSTrafficTypeBestEffort",
    "QOS_TRAFFIC_TYPE_QOSTrafficTypeControl",
    "QOS_TRAFFIC_TYPE_QOSTrafficTypeExcellentEffort",
    "QOS_TRAFFIC_TYPE_QOSTrafficTypeVoice",
    "QOS_VERSION",
    "QUALITATIVE_SERV",
    "QualAppFlowSpec",
    "QualTspec",
    "QualTspecParms",
    "RCVD_PATH_TEAR",
    "RCVD_RESV_TEAR",
    "RESOURCES_ALLOCATED",
    "RESOURCES_MODIFIED",
    "RESV_STYLE",
    "RHANDLE",
    "RSVP_ADSPEC",
    "RSVP_DEFAULT_STYLE",
    "RSVP_Err_ADMISSION",
    "RSVP_Err_AMBIG_FILTER",
    "RSVP_Err_API_ERROR",
    "RSVP_Err_BAD_DSTPORT",
    "RSVP_Err_BAD_SNDPORT",
    "RSVP_Err_BAD_STYLE",
    "RSVP_Err_NONE",
    "RSVP_Err_NO_PATH",
    "RSVP_Err_NO_SENDER",
    "RSVP_Err_POLICY",
    "RSVP_Err_PREEMPTED",
    "RSVP_Err_RSVP_SYS_ERROR",
    "RSVP_Err_TC_ERROR",
    "RSVP_Err_TC_SYS_ERROR",
    "RSVP_Err_UNKNOWN_CTYPE",
    "RSVP_Err_UNKNOWN_STYLE",
    "RSVP_Err_UNKN_OBJ_CLASS",
    "RSVP_Erv_API",
    "RSVP_Erv_Bandwidth",
    "RSVP_Erv_Bucket_szie",
    "RSVP_Erv_Conflict_Serv",
    "RSVP_Erv_Crazy_Flowspec",
    "RSVP_Erv_Crazy_Tspec",
    "RSVP_Erv_DelayBnd",
    "RSVP_Erv_Flow_Rate",
    "RSVP_Erv_MEMORY",
    "RSVP_Erv_MTU",
    "RSVP_Erv_Min_Policied_size",
    "RSVP_Erv_No_Serv",
    "RSVP_Erv_Nonev",
    "RSVP_Erv_Other",
    "RSVP_Erv_Peak_Rate",
    "RSVP_FILTERSPEC",
    "RSVP_FILTERSPEC_V4",
    "RSVP_FILTERSPEC_V4_GPI",
    "RSVP_FILTERSPEC_V6",
    "RSVP_FILTERSPEC_V6_FLOW",
    "RSVP_FILTERSPEC_V6_GPI",
    "RSVP_FIXED_FILTER_STYLE",
    "RSVP_HOP",
    "RSVP_MSG_OBJS",
    "RSVP_OBJECT_ID_BASE",
    "RSVP_PATH",
    "RSVP_PATH_ERR",
    "RSVP_PATH_TEAR",
    "RSVP_POLICY",
    "RSVP_POLICY_INFO",
    "RSVP_RESERVE_INFO",
    "RSVP_RESV",
    "RSVP_RESV_ERR",
    "RSVP_RESV_TEAR",
    "RSVP_SCOPE",
    "RSVP_SESSION",
    "RSVP_SHARED_EXPLICIT_STYLE",
    "RSVP_STATUS_INFO",
    "RSVP_WILDCARD_STYLE",
    "RsvpObjHdr",
    "Rsvp_Hop_IPv4",
    "SENDER_TSPEC",
    "SERVICETYPE_BESTEFFORT",
    "SERVICETYPE_CONTROLLEDLOAD",
    "SERVICETYPE_GENERAL_INFORMATION",
    "SERVICETYPE_GUARANTEED",
    "SERVICETYPE_NETWORK_CONTROL",
    "SERVICETYPE_NETWORK_UNAVAILABLE",
    "SERVICETYPE_NOCHANGE",
    "SERVICETYPE_NONCONFORMING",
    "SERVICETYPE_NOTRAFFIC",
    "SERVICETYPE_QUALITATIVE",
    "SERVICE_BESTEFFORT",
    "SERVICE_CONTROLLEDLOAD",
    "SERVICE_GUARANTEED",
    "SERVICE_NO_QOS_SIGNALING",
    "SERVICE_NO_TRAFFIC_CONTROL",
    "SERVICE_QUALITATIVE",
    "SESSFLG_E_Police",
    "SIPAERROR_FIRMWAREFAILURE",
    "SIPAERROR_INTERNALFAILURE",
    "SIPAEVENTTYPE_AGGREGATION",
    "SIPAEVENTTYPE_AUTHORITY",
    "SIPAEVENTTYPE_CONTAINER",
    "SIPAEVENTTYPE_DRTM",
    "SIPAEVENTTYPE_ELAM",
    "SIPAEVENTTYPE_ERROR",
    "SIPAEVENTTYPE_INFORMATION",
    "SIPAEVENTTYPE_KSR",
    "SIPAEVENTTYPE_LOADEDMODULE",
    "SIPAEVENTTYPE_NONMEASURED",
    "SIPAEVENTTYPE_OSPARAMETER",
    "SIPAEVENTTYPE_PREOSPARAMETER",
    "SIPAEVENTTYPE_TRUSTPOINT",
    "SIPAEVENTTYPE_VBS",
    "SIPAEVENT_APPLICATION_RETURN",
    "SIPAEVENT_APPLICATION_SVN",
    "SIPAEVENT_AUTHENTICODEHASH",
    "SIPAEVENT_AUTHORITYISSUER",
    "SIPAEVENT_AUTHORITYPUBKEY",
    "SIPAEVENT_AUTHORITYPUBLISHER",
    "SIPAEVENT_AUTHORITYSERIAL",
    "SIPAEVENT_AUTHORITYSHA1THUMBPRINT",
    "SIPAEVENT_BITLOCKER_UNLOCK",
    "SIPAEVENT_BOOTCOUNTER",
    "SIPAEVENT_BOOTDEBUGGING",
    "SIPAEVENT_BOOT_REVOCATION_LIST",
    "SIPAEVENT_CODEINTEGRITY",
    "SIPAEVENT_COUNTERID",
    "SIPAEVENT_DATAEXECUTIONPREVENTION",
    "SIPAEVENT_DRIVER_LOAD_POLICY",
    "SIPAEVENT_DRTM_AMD_SMM_HASH",
    "SIPAEVENT_DRTM_AMD_SMM_SIGNER_KEY",
    "SIPAEVENT_DRTM_SMM_LEVEL",
    "SIPAEVENT_DRTM_STATE_AUTH",
    "SIPAEVENT_DUMPS_DISABLED",
    "SIPAEVENT_DUMP_ENCRYPTION_ENABLED",
    "SIPAEVENT_DUMP_ENCRYPTION_KEY_DIGEST",
    "SIPAEVENT_ELAM_CONFIGURATION",
    "SIPAEVENT_ELAM_KEYNAME",
    "SIPAEVENT_ELAM_MEASURED",
    "SIPAEVENT_ELAM_POLICY",
    "SIPAEVENT_EVENTCOUNTER",
    "SIPAEVENT_FILEPATH",
    "SIPAEVENT_FLIGHTSIGNING",
    "SIPAEVENT_HASHALGORITHMID",
    "SIPAEVENT_HIBERNATION_DISABLED",
    "SIPAEVENT_HYPERVISOR_BOOT_DMA_PROTECTION",
    "SIPAEVENT_HYPERVISOR_DEBUG",
    "SIPAEVENT_HYPERVISOR_IOMMU_POLICY",
    "SIPAEVENT_HYPERVISOR_LAUNCH_TYPE",
    "SIPAEVENT_HYPERVISOR_MMIO_NX_POLICY",
    "SIPAEVENT_HYPERVISOR_MSR_FILTER_POLICY",
    "SIPAEVENT_HYPERVISOR_PATH",
    "SIPAEVENT_IMAGEBASE",
    "SIPAEVENT_IMAGESIZE",
    "SIPAEVENT_IMAGEVALIDATED",
    "SIPAEVENT_INFORMATION",
    "SIPAEVENT_KSR_SIGNATURE",
    "SIPAEVENT_KSR_SIGNATURE_PAYLOAD",
    "SIPAEVENT_LSAISO_CONFIG",
    "SIPAEVENT_MODULE_SVN",
    "SIPAEVENT_MORBIT_API_STATUS",
    "SIPAEVENT_MORBIT_NOT_CANCELABLE",
    "SIPAEVENT_NOAUTHORITY",
    "SIPAEVENT_OSDEVICE",
    "SIPAEVENT_OSKERNELDEBUG",
    "SIPAEVENT_OS_REVOCATION_LIST",
    "SIPAEVENT_PAGEFILE_ENCRYPTION_ENABLED",
    "SIPAEVENT_PHYSICALADDRESSEXTENSION",
    "SIPAEVENT_REVOCATION_LIST_PAYLOAD",
    "SIPAEVENT_SAFEMODE",
    "SIPAEVENT_SBCP_INFO",
    "SIPAEVENT_SBCP_INFO_PAYLOAD_V1",
    "SIPAEVENT_SI_POLICY",
    "SIPAEVENT_SI_POLICY_PAYLOAD",
    "SIPAEVENT_SMT_STATUS",
    "SIPAEVENT_SVN_CHAIN_STATUS",
    "SIPAEVENT_SYSTEMROOT",
    "SIPAEVENT_TESTSIGNING",
    "SIPAEVENT_TRANSFER_CONTROL",
    "SIPAEVENT_VBS_DUMP_USES_AMEROOT",
    "SIPAEVENT_VBS_HVCI_POLICY",
    "SIPAEVENT_VBS_IOMMU_REQUIRED",
    "SIPAEVENT_VBS_MANDATORY_ENFORCEMENT",
    "SIPAEVENT_VBS_MICROSOFT_BOOT_CHAIN_REQUIRED",
    "SIPAEVENT_VBS_MMIO_NX_REQUIRED",
    "SIPAEVENT_VBS_MSR_FILTERING_REQUIRED",
    "SIPAEVENT_VBS_SECUREBOOT_REQUIRED",
    "SIPAEVENT_VBS_VSM_NOSECRETS_ENFORCED",
    "SIPAEVENT_VBS_VSM_REQUIRED",
    "SIPAEVENT_VSM_IDKS_INFO",
    "SIPAEVENT_VSM_IDK_INFO",
    "SIPAEVENT_VSM_IDK_INFO_PAYLOAD",
    "SIPAEVENT_VSM_IDK_RSA_INFO",
    "SIPAEVENT_VSM_LAUNCH_TYPE",
    "SIPAEVENT_WINPE",
    "SIPAEV_ACTION",
    "SIPAEV_AMD_SL_EVENT_BASE",
    "SIPAEV_AMD_SL_LOAD",
    "SIPAEV_AMD_SL_LOAD_1",
    "SIPAEV_AMD_SL_PSP_FW_SPLT",
    "SIPAEV_AMD_SL_PUB_KEY",
    "SIPAEV_AMD_SL_SEPARATOR",
    "SIPAEV_AMD_SL_SVN",
    "SIPAEV_AMD_SL_TSME_RB_FUSE",
    "SIPAEV_COMPACT_HASH",
    "SIPAEV_CPU_MICROCODE",
    "SIPAEV_EFI_ACTION",
    "SIPAEV_EFI_BOOT_SERVICES_APPLICATION",
    "SIPAEV_EFI_BOOT_SERVICES_DRIVER",
    "SIPAEV_EFI_EVENT_BASE",
    "SIPAEV_EFI_GPT_EVENT",
    "SIPAEV_EFI_HANDOFF_TABLES",
    "SIPAEV_EFI_HANDOFF_TABLES2",
    "SIPAEV_EFI_HCRTM_EVENT",
    "SIPAEV_EFI_PLATFORM_FIRMWARE_BLOB",
    "SIPAEV_EFI_PLATFORM_FIRMWARE_BLOB2",
    "SIPAEV_EFI_RUNTIME_SERVICES_DRIVER",
    "SIPAEV_EFI_SPDM_FIRMWARE_BLOB",
    "SIPAEV_EFI_SPDM_FIRMWARE_CONFIG",
    "SIPAEV_EFI_VARIABLE_AUTHORITY",
    "SIPAEV_EFI_VARIABLE_BOOT",
    "SIPAEV_EFI_VARIABLE_DRIVER_CONFIG",
    "SIPAEV_EVENT_TAG",
    "SIPAEV_IPL",
    "SIPAEV_IPL_PARTITION_DATA",
    "SIPAEV_NONHOST_CODE",
    "SIPAEV_NONHOST_CONFIG",
    "SIPAEV_NONHOST_INFO",
    "SIPAEV_NO_ACTION",
    "SIPAEV_OMIT_BOOT_DEVICE_EVENTS",
    "SIPAEV_PLATFORM_CONFIG_FLAGS",
    "SIPAEV_POST_CODE",
    "SIPAEV_PREBOOT_CERT",
    "SIPAEV_SEPARATOR",
    "SIPAEV_S_CRTM_CONTENTS",
    "SIPAEV_S_CRTM_VERSION",
    "SIPAEV_TABLE_OF_DEVICES",
    "SIPAEV_TXT_BIOSAC_REG_DATA",
    "SIPAEV_TXT_BOOT_POL_HASH",
    "SIPAEV_TXT_BPM_HASH",
    "SIPAEV_TXT_BPM_INFO_HASH",
    "SIPAEV_TXT_CAP_VALUE",
    "SIPAEV_TXT_COLD_BOOT_BIOS_HASH",
    "SIPAEV_TXT_COMBINED_HASH",
    "SIPAEV_TXT_CPU_SCRTM_STAT",
    "SIPAEV_TXT_ELEMENTS_HASH",
    "SIPAEV_TXT_EVENT_BASE",
    "SIPAEV_TXT_HASH_START",
    "SIPAEV_TXT_KM_HASH",
    "SIPAEV_TXT_KM_INFO_HASH",
    "SIPAEV_TXT_LCP_AUTHORITIES_HASH",
    "SIPAEV_TXT_LCP_CONTROL_HASH",
    "SIPAEV_TXT_LCP_DETAILS_HASH",
    "SIPAEV_TXT_LCP_HASH",
    "SIPAEV_TXT_MLE_HASH",
    "SIPAEV_TXT_NV_INFO_HASH",
    "SIPAEV_TXT_OSSINITDATA_CAP_HASH",
    "SIPAEV_TXT_PCR_MAPPING",
    "SIPAEV_TXT_RANDOM_VALUE",
    "SIPAEV_TXT_SINIT_PUBKEY_HASH",
    "SIPAEV_TXT_STM_HASH",
    "SIPAEV_UNUSED",
    "SIPAHDRSIGNATURE",
    "SIPAKSRHDRSIGNATURE",
    "SIPALOGVERSION",
    "STATE_TIMEOUT",
    "Scope_list_ipv4",
    "Session_IPv4",
    "TCBASE",
    "TCG_PCClientPCREventStruct",
    "TCG_PCClientTaggedEventStruct",
    "TCI_ADD_FLOW_COMPLETE_HANDLER",
    "TCI_CLIENT_FUNC_LIST",
    "TCI_DEL_FLOW_COMPLETE_HANDLER",
    "TCI_MOD_FLOW_COMPLETE_HANDLER",
    "TCI_NOTIFY_HANDLER",
    "TC_GEN_FILTER",
    "TC_GEN_FLOW",
    "TC_IFC_DESCRIPTOR",
    "TC_NONCONF_BORROW",
    "TC_NONCONF_BORROW_PLUS",
    "TC_NONCONF_DISCARD",
    "TC_NONCONF_SHAPE",
    "TC_NOTIFY_FLOW_CLOSE",
    "TC_NOTIFY_IFC_CHANGE",
    "TC_NOTIFY_IFC_CLOSE",
    "TC_NOTIFY_IFC_UP",
    "TC_NOTIFY_PARAM_CHANGED",
    "TC_SUPPORTED_INFO_BUFFER",
    "TcAddFilter",
    "TcAddFlow",
    "TcCloseInterface",
    "TcDeleteFilter",
    "TcDeleteFlow",
    "TcDeregisterClient",
    "TcEnumerateFlows",
    "TcEnumerateInterfaces",
    "TcGetFlowNameA",
    "TcGetFlowNameW",
    "TcModifyFlow",
    "TcOpenInterfaceA",
    "TcOpenInterfaceW",
    "TcQueryFlowA",
    "TcQueryFlowW",
    "TcQueryInterface",
    "TcRegisterClient",
    "TcSetFlowA",
    "TcSetFlowW",
    "TcSetInterface",
    "UNSUPPORTED_CREDENTIAL_TYPE",
    "WBCL_DIGEST_ALG_BITMAP_SHA3_256",
    "WBCL_DIGEST_ALG_BITMAP_SHA3_384",
    "WBCL_DIGEST_ALG_BITMAP_SHA3_512",
    "WBCL_DIGEST_ALG_BITMAP_SHA_1",
    "WBCL_DIGEST_ALG_BITMAP_SHA_2_256",
    "WBCL_DIGEST_ALG_BITMAP_SHA_2_384",
    "WBCL_DIGEST_ALG_BITMAP_SHA_2_512",
    "WBCL_DIGEST_ALG_BITMAP_SM3_256",
    "WBCL_DIGEST_ALG_ID_SHA3_256",
    "WBCL_DIGEST_ALG_ID_SHA3_384",
    "WBCL_DIGEST_ALG_ID_SHA3_512",
    "WBCL_DIGEST_ALG_ID_SHA_1",
    "WBCL_DIGEST_ALG_ID_SHA_2_256",
    "WBCL_DIGEST_ALG_ID_SHA_2_384",
    "WBCL_DIGEST_ALG_ID_SHA_2_512",
    "WBCL_DIGEST_ALG_ID_SM3_256",
    "WBCL_HASH_LEN_SHA1",
    "WBCL_Iterator",
    "WBCL_LogHdr",
    "class_ADSPEC",
    "class_CONFIRM",
    "class_ERROR_SPEC",
    "class_FILTER_SPEC",
    "class_FLOWSPEC",
    "class_INTEGRITY",
    "class_IS_FLOWSPEC",
    "class_MAX",
    "class_NULL",
    "class_POLICY_DATA",
    "class_RSVP_HOP",
    "class_SCOPE",
    "class_SENDER_TEMPLATE",
    "class_SENDER_TSPEC",
    "class_SESSION",
    "class_SESSION_GROUP",
    "class_STYLE",
    "class_TIME_VALUES",
    "ctype_ADSPEC_INTSERV",
    "ctype_ERROR_SPEC_ipv4",
    "ctype_FILTER_SPEC_ipv4",
    "ctype_FILTER_SPEC_ipv4GPI",
    "ctype_FLOWSPEC_Intserv0",
    "ctype_POLICY_DATA",
    "ctype_RSVP_HOP_ipv4",
    "ctype_SCOPE_list_ipv4",
    "ctype_SENDER_TEMPLATE_ipv4",
    "ctype_SENDER_TEMPLATE_ipv4GPI",
    "ctype_SENDER_TSPEC",
    "ctype_SESSION_ipv4",
    "ctype_SESSION_ipv4GPI",
    "ctype_STYLE",
    "int_serv_wkp",
    "ioctl_code",
    "mCOMPANY",
    "mIOC_IN",
    "mIOC_OUT",
    "mIOC_VENDOR",
]
_arch_optional = [
]
