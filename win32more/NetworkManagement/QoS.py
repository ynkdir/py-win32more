from win32more import *
import win32more.Foundation
import win32more.NetworkManagement.Ndis
import win32more.NetworkManagement.QoS
import win32more.Networking.WinSock
import win32more.System.IO

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
QOS_MAX_OBJECT_STRING_LENGTH = 256
QOS_TRAFFIC_GENERAL_ID_BASE = 4000
SERVICETYPE_NOTRAFFIC = 0
SERVICETYPE_BESTEFFORT = 1
SERVICETYPE_CONTROLLEDLOAD = 2
SERVICETYPE_GUARANTEED = 3
SERVICETYPE_NETWORK_UNAVAILABLE = 4
SERVICETYPE_GENERAL_INFORMATION = 5
SERVICETYPE_NOCHANGE = 6
SERVICETYPE_NONCONFORMING = 9
SERVICETYPE_NETWORK_CONTROL = 10
SERVICETYPE_QUALITATIVE = 13
SERVICE_BESTEFFORT = 2147549184
SERVICE_CONTROLLEDLOAD = 2147614720
SERVICE_GUARANTEED = 2147745792
SERVICE_QUALITATIVE = 2149580800
SERVICE_NO_TRAFFIC_CONTROL = 2164260864
SERVICE_NO_QOS_SIGNALING = 1073741824
QOS_NOT_SPECIFIED = 4294967295
POSITIVE_INFINITY_RATE = 4294967294
QOS_GENERAL_ID_BASE = 2000
TC_NONCONF_BORROW = 0
TC_NONCONF_SHAPE = 1
TC_NONCONF_DISCARD = 2
TC_NONCONF_BORROW_PLUS = 3
SESSFLG_E_Police = 1
Opt_Share_mask = 24
Opt_Distinct = 8
Opt_Shared = 16
Opt_SndSel_mask = 7
Opt_Wildcard = 1
Opt_Explicit = 2
ERROR_SPECF_InPlace = 1
ERROR_SPECF_NotGuilty = 2
ERR_FORWARD_OK = 32768
ERR_Usage_globl = 0
ERR_Usage_local = 16
ERR_Usage_serv = 17
ERR_global_mask = 4095
GENERAL_INFO = 1
GUARANTEED_SERV = 2
PREDICTIVE_SERV = 3
CONTROLLED_DELAY_SERV = 4
CONTROLLED_LOAD_SERV = 5
QUALITATIVE_SERV = 6
INTSERV_VERS_MASK = 240
INTSERV_VERSION0 = 0
ISSH_BREAK_BIT = 128
ISPH_FLG_INV = 128
RSVP_PATH = 1
RSVP_RESV = 2
RSVP_PATH_ERR = 3
RSVP_RESV_ERR = 4
RSVP_PATH_TEAR = 5
RSVP_RESV_TEAR = 6
RSVP_Err_NONE = 0
RSVP_Erv_Nonev = 0
RSVP_Err_ADMISSION = 1
RSVP_Erv_Other = 0
RSVP_Erv_DelayBnd = 1
RSVP_Erv_Bandwidth = 2
RSVP_Erv_MTU = 3
RSVP_Erv_Flow_Rate = 32769
RSVP_Erv_Bucket_szie = 32770
RSVP_Erv_Peak_Rate = 32771
RSVP_Erv_Min_Policied_size = 32772
RSVP_Err_POLICY = 2
POLICY_ERRV_NO_MORE_INFO = 1
POLICY_ERRV_UNSUPPORTED_CREDENTIAL_TYPE = 2
POLICY_ERRV_INSUFFICIENT_PRIVILEGES = 3
POLICY_ERRV_EXPIRED_CREDENTIALS = 4
POLICY_ERRV_IDENTITY_CHANGED = 5
POLICY_ERRV_UNKNOWN = 0
POLICY_ERRV_GLOBAL_DEF_FLOW_COUNT = 1
POLICY_ERRV_GLOBAL_GRP_FLOW_COUNT = 2
POLICY_ERRV_GLOBAL_USER_FLOW_COUNT = 3
POLICY_ERRV_GLOBAL_UNAUTH_USER_FLOW_COUNT = 4
POLICY_ERRV_SUBNET_DEF_FLOW_COUNT = 5
POLICY_ERRV_SUBNET_GRP_FLOW_COUNT = 6
POLICY_ERRV_SUBNET_USER_FLOW_COUNT = 7
POLICY_ERRV_SUBNET_UNAUTH_USER_FLOW_COUNT = 8
POLICY_ERRV_GLOBAL_DEF_FLOW_DURATION = 9
POLICY_ERRV_GLOBAL_GRP_FLOW_DURATION = 10
POLICY_ERRV_GLOBAL_USER_FLOW_DURATION = 11
POLICY_ERRV_GLOBAL_UNAUTH_USER_FLOW_DURATION = 12
POLICY_ERRV_SUBNET_DEF_FLOW_DURATION = 13
POLICY_ERRV_SUBNET_GRP_FLOW_DURATION = 14
POLICY_ERRV_SUBNET_USER_FLOW_DURATION = 15
POLICY_ERRV_SUBNET_UNAUTH_USER_FLOW_DURATION = 16
POLICY_ERRV_GLOBAL_DEF_FLOW_RATE = 17
POLICY_ERRV_GLOBAL_GRP_FLOW_RATE = 18
POLICY_ERRV_GLOBAL_USER_FLOW_RATE = 19
POLICY_ERRV_GLOBAL_UNAUTH_USER_FLOW_RATE = 20
POLICY_ERRV_SUBNET_DEF_FLOW_RATE = 21
POLICY_ERRV_SUBNET_GRP_FLOW_RATE = 22
POLICY_ERRV_SUBNET_USER_FLOW_RATE = 23
POLICY_ERRV_SUBNET_UNAUTH_USER_FLOW_RATE = 24
POLICY_ERRV_GLOBAL_DEF_PEAK_RATE = 25
POLICY_ERRV_GLOBAL_GRP_PEAK_RATE = 26
POLICY_ERRV_GLOBAL_USER_PEAK_RATE = 27
POLICY_ERRV_GLOBAL_UNAUTH_USER_PEAK_RATE = 28
POLICY_ERRV_SUBNET_DEF_PEAK_RATE = 29
POLICY_ERRV_SUBNET_GRP_PEAK_RATE = 30
POLICY_ERRV_SUBNET_USER_PEAK_RATE = 31
POLICY_ERRV_SUBNET_UNAUTH_USER_PEAK_RATE = 32
POLICY_ERRV_GLOBAL_DEF_SUM_FLOW_RATE = 33
POLICY_ERRV_GLOBAL_GRP_SUM_FLOW_RATE = 34
POLICY_ERRV_GLOBAL_USER_SUM_FLOW_RATE = 35
POLICY_ERRV_GLOBAL_UNAUTH_USER_SUM_FLOW_RATE = 36
POLICY_ERRV_SUBNET_DEF_SUM_FLOW_RATE = 37
POLICY_ERRV_SUBNET_GRP_SUM_FLOW_RATE = 38
POLICY_ERRV_SUBNET_USER_SUM_FLOW_RATE = 39
POLICY_ERRV_SUBNET_UNAUTH_USER_SUM_FLOW_RATE = 40
POLICY_ERRV_GLOBAL_DEF_SUM_PEAK_RATE = 41
POLICY_ERRV_GLOBAL_GRP_SUM_PEAK_RATE = 42
POLICY_ERRV_GLOBAL_USER_SUM_PEAK_RATE = 43
POLICY_ERRV_GLOBAL_UNAUTH_USER_SUM_PEAK_RATE = 44
POLICY_ERRV_SUBNET_DEF_SUM_PEAK_RATE = 45
POLICY_ERRV_SUBNET_GRP_SUM_PEAK_RATE = 46
POLICY_ERRV_SUBNET_USER_SUM_PEAK_RATE = 47
POLICY_ERRV_SUBNET_UNAUTH_USER_SUM_PEAK_RATE = 48
POLICY_ERRV_UNKNOWN_USER = 49
POLICY_ERRV_NO_PRIVILEGES = 50
POLICY_ERRV_EXPIRED_USER_TOKEN = 51
POLICY_ERRV_NO_RESOURCES = 52
POLICY_ERRV_PRE_EMPTED = 53
POLICY_ERRV_USER_CHANGED = 54
POLICY_ERRV_NO_ACCEPTS = 55
POLICY_ERRV_NO_MEMORY = 56
POLICY_ERRV_CRAZY_FLOWSPEC = 57
RSVP_Err_NO_PATH = 3
RSVP_Err_NO_SENDER = 4
RSVP_Err_BAD_STYLE = 5
RSVP_Err_UNKNOWN_STYLE = 6
RSVP_Err_BAD_DSTPORT = 7
RSVP_Err_BAD_SNDPORT = 8
RSVP_Err_AMBIG_FILTER = 9
RSVP_Err_PREEMPTED = 12
RSVP_Err_UNKN_OBJ_CLASS = 13
RSVP_Err_UNKNOWN_CTYPE = 14
RSVP_Err_API_ERROR = 20
RSVP_Err_TC_ERROR = 21
RSVP_Erv_Conflict_Serv = 1
RSVP_Erv_No_Serv = 2
RSVP_Erv_Crazy_Flowspec = 3
RSVP_Erv_Crazy_Tspec = 4
RSVP_Err_TC_SYS_ERROR = 22
RSVP_Err_RSVP_SYS_ERROR = 23
RSVP_Erv_MEMORY = 1
RSVP_Erv_API = 2
LPM_PE_USER_IDENTITY = 2
LPM_PE_APP_IDENTITY = 3
ERROR_NO_MORE_INFO = 1
UNSUPPORTED_CREDENTIAL_TYPE = 2
INSUFFICIENT_PRIVILEGES = 3
EXPIRED_CREDENTIAL = 4
IDENTITY_CHANGED = 5
LPM_OK = 0
INV_LPM_HANDLE = 1
LPM_TIME_OUT = 2
INV_REQ_HANDLE = 3
DUP_RESULTS = 4
INV_RESULTS = 5
LPM_PE_ALL_TYPES = 0
LPM_API_VERSION_1 = 1
PCM_VERSION_1 = 1
LPV_RESERVED = 0
LPV_MIN_PRIORITY = 1
LPV_MAX_PRIORITY = 65280
LPV_DROP_MSG = 65533
LPV_DONT_CARE = 65534
LPV_REJECT = 65535
FORCE_IMMEDIATE_REFRESH = 1
LPM_RESULT_READY = 0
LPM_RESULT_DEFER = 1
RCVD_PATH_TEAR = 1
RCVD_RESV_TEAR = 2
ADM_CTRL_FAILED = 3
STATE_TIMEOUT = 4
FLOW_DURATION = 5
RESOURCES_ALLOCATED = 1
RESOURCES_MODIFIED = 2
CURRENT_TCI_VERSION = 2
TC_NOTIFY_IFC_UP = 1
TC_NOTIFY_IFC_CLOSE = 2
TC_NOTIFY_IFC_CHANGE = 3
TC_NOTIFY_PARAM_CHANGED = 4
TC_NOTIFY_FLOW_CLOSE = 5
MAX_STRING_LENGTH = 256
QOS_OUTGOING_DEFAULT_MINIMUM_BANDWIDTH = 4294967295
QOS_QUERYFLOW_FRESH = 1
QOS_NON_ADAPTIVE_FLOW = 2
RSVP_OBJECT_ID_BASE = 1000
RSVP_DEFAULT_STYLE = 0
RSVP_WILDCARD_STYLE = 1
RSVP_FIXED_FILTER_STYLE = 2
RSVP_SHARED_EXPLICIT_STYLE = 3
AD_FLAG_BREAK_BIT = 1
QOSSPBASE = 50000
ALLOWED_TO_SEND_DATA = 50001
ABLE_TO_RECV_RSVP = 50002
LINE_RATE = 50003
LOCAL_TRAFFIC_CONTROL = 50004
LOCAL_QOSABILITY = 50005
END_TO_END_QOSABILITY = 50006
INFO_NOT_AVAILABLE = 4294967295
ANY_DEST_ADDR = 4294967295
MODERATELY_DELAY_SENSITIVE = 4294967293
HIGHLY_DELAY_SENSITIVE = 4294967294
QOSSP_ERR_BASE = 56000
GQOS_NO_ERRORCODE = 0
GQOS_NO_ERRORVALUE = 0
GQOS_ERRORCODE_UNKNOWN = 4294967295
GQOS_ERRORVALUE_UNKNOWN = 4294967295
GQOS_NET_ADMISSION = 56100
GQOS_NET_POLICY = 56200
GQOS_RSVP = 56300
GQOS_API = 56400
GQOS_KERNEL_TC_SYS = 56500
GQOS_RSVP_SYS = 56600
GQOS_KERNEL_TC = 56700
PE_TYPE_APPID = 3
PE_ATTRIB_TYPE_POLICY_LOCATOR = 1
POLICY_LOCATOR_SUB_TYPE_ASCII_DN = 1
POLICY_LOCATOR_SUB_TYPE_UNICODE_DN = 2
POLICY_LOCATOR_SUB_TYPE_ASCII_DN_ENC = 3
POLICY_LOCATOR_SUB_TYPE_UNICODE_DN_ENC = 4
PE_ATTRIB_TYPE_CREDENTIAL = 2
CREDENTIAL_SUB_TYPE_ASCII_ID = 1
CREDENTIAL_SUB_TYPE_UNICODE_ID = 2
CREDENTIAL_SUB_TYPE_KERBEROS_TKT = 3
CREDENTIAL_SUB_TYPE_X509_V3_CERT = 4
CREDENTIAL_SUB_TYPE_PGP_CERT = 5
TCBASE = 7500
ERROR_INCOMPATIBLE_TCI_VERSION = 7501
ERROR_INVALID_SERVICE_TYPE = 7502
ERROR_INVALID_TOKEN_RATE = 7503
ERROR_INVALID_PEAK_RATE = 7504
ERROR_INVALID_SD_MODE = 7505
ERROR_INVALID_QOS_PRIORITY = 7506
ERROR_INVALID_TRAFFIC_CLASS = 7507
ERROR_INVALID_ADDRESS_TYPE = 7508
ERROR_DUPLICATE_FILTER = 7509
ERROR_FILTER_CONFLICT = 7510
ERROR_ADDRESS_TYPE_NOT_SUPPORTED = 7511
ERROR_TC_SUPPORTED_OBJECTS_EXIST = 7512
ERROR_INCOMPATABLE_QOS = 7513
ERROR_TC_NOT_SUPPORTED = 7514
ERROR_TC_OBJECT_LENGTH_INVALID = 7515
ERROR_INVALID_FLOW_MODE = 7516
ERROR_INVALID_DIFFSERV_FLOW = 7517
ERROR_DS_MAPPING_EXISTS = 7518
ERROR_INVALID_SHAPE_RATE = 7519
ERROR_INVALID_DS_CLASS = 7520
ERROR_TOO_MANY_CLIENTS = 7521
GUID_QOS_REMAINING_BANDWIDTH = 'c4c51720-40ec-11d1-2c91-00aa00574915'
GUID_QOS_BESTEFFORT_BANDWIDTH = 'ed885290-40ec-11d1-2c91-00aa00574915'
GUID_QOS_LATENCY = 'fc408ef0-40ec-11d1-2c91-00aa00574915'
GUID_QOS_FLOW_COUNT = '1147f880-40ed-11d1-2c91-00aa00574915'
GUID_QOS_NON_BESTEFFORT_LIMIT = '185c44e0-40ed-11d1-2c91-00aa00574915'
GUID_QOS_MAX_OUTSTANDING_SENDS = '161ffa86-6120-11d1-2c91-00aa00574915'
GUID_QOS_STATISTICS_BUFFER = 'bb2c0980-e900-11d1-b07e-0080c71382bf'
GUID_QOS_FLOW_MODE = '5c82290a-515a-11d2-8e58-00c04fc9bfcb'
GUID_QOS_ISSLOW_FLOW = 'abf273a4-ee07-11d2-be1b-00a0c99ee63b'
GUID_QOS_TIMER_RESOLUTION = 'ba10cc88-f13e-11d2-be1b-00a0c99ee63b'
GUID_QOS_FLOW_IP_CONFORMING = '07f99a8b-fcd2-11d2-be1e-00a0c99ee63b'
GUID_QOS_FLOW_IP_NONCONFORMING = '087a5987-fcd2-11d2-be1e-00a0c99ee63b'
GUID_QOS_FLOW_8021P_CONFORMING = '08c1e013-fcd2-11d2-be1e-00a0c99ee63b'
GUID_QOS_FLOW_8021P_NONCONFORMING = '09023f91-fcd2-11d2-be1e-00a0c99ee63b'
GUID_QOS_ENABLE_AVG_STATS = 'bafb6d11-27c4-4801-a46f-ef8080c188c8'
GUID_QOS_ENABLE_WINDOW_ADJUSTMENT = 'aa966725-d3e9-4c55-b335-2a00279a1e64'
FSCTL_TCP_BASE = 18
IF_MIB_STATS_ID = 1
IP_MIB_STATS_ID = 1
IP_MIB_ADDRTABLE_ENTRY_ID = 258
IP_INTFC_INFO_ID = 259
MAX_PHYSADDR_SIZE = 8
SIPAEV_PREBOOT_CERT = 0
SIPAEV_POST_CODE = 1
SIPAEV_UNUSED = 2
SIPAEV_NO_ACTION = 3
SIPAEV_SEPARATOR = 4
SIPAEV_ACTION = 5
SIPAEV_EVENT_TAG = 6
SIPAEV_S_CRTM_CONTENTS = 7
SIPAEV_S_CRTM_VERSION = 8
SIPAEV_CPU_MICROCODE = 9
SIPAEV_PLATFORM_CONFIG_FLAGS = 10
SIPAEV_TABLE_OF_DEVICES = 11
SIPAEV_COMPACT_HASH = 12
SIPAEV_IPL = 13
SIPAEV_IPL_PARTITION_DATA = 14
SIPAEV_NONHOST_CODE = 15
SIPAEV_NONHOST_CONFIG = 16
SIPAEV_NONHOST_INFO = 17
SIPAEV_OMIT_BOOT_DEVICE_EVENTS = 18
SIPAEV_EFI_EVENT_BASE = 2147483648
SIPAEV_EFI_VARIABLE_DRIVER_CONFIG = 2147483649
SIPAEV_EFI_VARIABLE_BOOT = 2147483650
SIPAEV_EFI_BOOT_SERVICES_APPLICATION = 2147483651
SIPAEV_EFI_BOOT_SERVICES_DRIVER = 2147483652
SIPAEV_EFI_RUNTIME_SERVICES_DRIVER = 2147483653
SIPAEV_EFI_GPT_EVENT = 2147483654
SIPAEV_EFI_ACTION = 2147483655
SIPAEV_EFI_PLATFORM_FIRMWARE_BLOB = 2147483656
SIPAEV_EFI_HANDOFF_TABLES = 2147483657
SIPAEV_EFI_PLATFORM_FIRMWARE_BLOB2 = 2147483658
SIPAEV_EFI_HANDOFF_TABLES2 = 2147483659
SIPAEV_EFI_HCRTM_EVENT = 2147483664
SIPAEV_EFI_VARIABLE_AUTHORITY = 2147483872
SIPAEV_EFI_SPDM_FIRMWARE_BLOB = 2147483873
SIPAEV_EFI_SPDM_FIRMWARE_CONFIG = 2147483874
SIPAEV_TXT_EVENT_BASE = 1024
SIPAEV_TXT_PCR_MAPPING = 1025
SIPAEV_TXT_HASH_START = 1026
SIPAEV_TXT_COMBINED_HASH = 1027
SIPAEV_TXT_MLE_HASH = 1028
SIPAEV_TXT_BIOSAC_REG_DATA = 1034
SIPAEV_TXT_CPU_SCRTM_STAT = 1035
SIPAEV_TXT_LCP_CONTROL_HASH = 1036
SIPAEV_TXT_ELEMENTS_HASH = 1037
SIPAEV_TXT_STM_HASH = 1038
SIPAEV_TXT_OSSINITDATA_CAP_HASH = 1039
SIPAEV_TXT_SINIT_PUBKEY_HASH = 1040
SIPAEV_TXT_LCP_HASH = 1041
SIPAEV_TXT_LCP_DETAILS_HASH = 1042
SIPAEV_TXT_LCP_AUTHORITIES_HASH = 1043
SIPAEV_TXT_NV_INFO_HASH = 1044
SIPAEV_TXT_COLD_BOOT_BIOS_HASH = 1045
SIPAEV_TXT_KM_HASH = 1046
SIPAEV_TXT_BPM_HASH = 1047
SIPAEV_TXT_KM_INFO_HASH = 1048
SIPAEV_TXT_BPM_INFO_HASH = 1049
SIPAEV_TXT_BOOT_POL_HASH = 1050
SIPAEV_TXT_RANDOM_VALUE = 1278
SIPAEV_TXT_CAP_VALUE = 1279
SIPAEV_AMD_SL_EVENT_BASE = 32768
SIPAEV_AMD_SL_LOAD = 32769
SIPAEV_AMD_SL_PSP_FW_SPLT = 32770
SIPAEV_AMD_SL_TSME_RB_FUSE = 32771
SIPAEV_AMD_SL_PUB_KEY = 32772
SIPAEV_AMD_SL_SVN = 32773
SIPAEV_AMD_SL_LOAD_1 = 32774
SIPAEV_AMD_SL_SEPARATOR = 32775
SIPAEVENTTYPE_NONMEASURED = 2147483648
SIPAEVENTTYPE_AGGREGATION = 1073741824
SIPAEVENTTYPE_CONTAINER = 65536
SIPAEVENTTYPE_INFORMATION = 131072
SIPAEVENTTYPE_ERROR = 196608
SIPAEVENTTYPE_PREOSPARAMETER = 262144
SIPAEVENTTYPE_OSPARAMETER = 327680
SIPAEVENTTYPE_AUTHORITY = 393216
SIPAEVENTTYPE_LOADEDMODULE = 458752
SIPAEVENTTYPE_TRUSTPOINT = 524288
SIPAEVENTTYPE_ELAM = 589824
SIPAEVENTTYPE_VBS = 655360
SIPAEVENTTYPE_KSR = 720896
SIPAEVENTTYPE_DRTM = 786432
SIPAERROR_FIRMWAREFAILURE = 196609
SIPAERROR_INTERNALFAILURE = 196611
SIPAEVENT_INFORMATION = 131073
SIPAEVENT_BOOTCOUNTER = 131074
SIPAEVENT_TRANSFER_CONTROL = 131075
SIPAEVENT_APPLICATION_RETURN = 131076
SIPAEVENT_BITLOCKER_UNLOCK = 131077
SIPAEVENT_EVENTCOUNTER = 131078
SIPAEVENT_COUNTERID = 131079
SIPAEVENT_MORBIT_NOT_CANCELABLE = 131080
SIPAEVENT_APPLICATION_SVN = 131081
SIPAEVENT_SVN_CHAIN_STATUS = 131082
SIPAEVENT_MORBIT_API_STATUS = 131083
SIPAEVENT_BOOTDEBUGGING = 262145
SIPAEVENT_BOOT_REVOCATION_LIST = 262146
SIPAEVENT_OSKERNELDEBUG = 327681
SIPAEVENT_CODEINTEGRITY = 327682
SIPAEVENT_TESTSIGNING = 327683
SIPAEVENT_DATAEXECUTIONPREVENTION = 327684
SIPAEVENT_SAFEMODE = 327685
SIPAEVENT_WINPE = 327686
SIPAEVENT_PHYSICALADDRESSEXTENSION = 327687
SIPAEVENT_OSDEVICE = 327688
SIPAEVENT_SYSTEMROOT = 327689
SIPAEVENT_HYPERVISOR_LAUNCH_TYPE = 327690
SIPAEVENT_HYPERVISOR_PATH = 327691
SIPAEVENT_HYPERVISOR_IOMMU_POLICY = 327692
SIPAEVENT_HYPERVISOR_DEBUG = 327693
SIPAEVENT_DRIVER_LOAD_POLICY = 327694
SIPAEVENT_SI_POLICY = 327695
SIPAEVENT_HYPERVISOR_MMIO_NX_POLICY = 327696
SIPAEVENT_HYPERVISOR_MSR_FILTER_POLICY = 327697
SIPAEVENT_VSM_LAUNCH_TYPE = 327698
SIPAEVENT_OS_REVOCATION_LIST = 327699
SIPAEVENT_SMT_STATUS = 327700
SIPAEVENT_VSM_IDK_INFO = 327712
SIPAEVENT_FLIGHTSIGNING = 327713
SIPAEVENT_PAGEFILE_ENCRYPTION_ENABLED = 327714
SIPAEVENT_VSM_IDKS_INFO = 327715
SIPAEVENT_HIBERNATION_DISABLED = 327716
SIPAEVENT_DUMPS_DISABLED = 327717
SIPAEVENT_DUMP_ENCRYPTION_ENABLED = 327718
SIPAEVENT_DUMP_ENCRYPTION_KEY_DIGEST = 327719
SIPAEVENT_LSAISO_CONFIG = 327720
SIPAEVENT_SBCP_INFO = 327721
SIPAEVENT_HYPERVISOR_BOOT_DMA_PROTECTION = 327728
SIPAEVENT_NOAUTHORITY = 393217
SIPAEVENT_AUTHORITYPUBKEY = 393218
SIPAEVENT_FILEPATH = 458753
SIPAEVENT_IMAGESIZE = 458754
SIPAEVENT_HASHALGORITHMID = 458755
SIPAEVENT_AUTHENTICODEHASH = 458756
SIPAEVENT_AUTHORITYISSUER = 458757
SIPAEVENT_AUTHORITYSERIAL = 458758
SIPAEVENT_IMAGEBASE = 458759
SIPAEVENT_AUTHORITYPUBLISHER = 458760
SIPAEVENT_AUTHORITYSHA1THUMBPRINT = 458761
SIPAEVENT_IMAGEVALIDATED = 458762
SIPAEVENT_MODULE_SVN = 458763
SIPAEVENT_ELAM_KEYNAME = 589825
SIPAEVENT_ELAM_CONFIGURATION = 589826
SIPAEVENT_ELAM_POLICY = 589827
SIPAEVENT_ELAM_MEASURED = 589828
SIPAEVENT_VBS_VSM_REQUIRED = 655361
SIPAEVENT_VBS_SECUREBOOT_REQUIRED = 655362
SIPAEVENT_VBS_IOMMU_REQUIRED = 655363
SIPAEVENT_VBS_MMIO_NX_REQUIRED = 655364
SIPAEVENT_VBS_MSR_FILTERING_REQUIRED = 655365
SIPAEVENT_VBS_MANDATORY_ENFORCEMENT = 655366
SIPAEVENT_VBS_HVCI_POLICY = 655367
SIPAEVENT_VBS_MICROSOFT_BOOT_CHAIN_REQUIRED = 655368
SIPAEVENT_VBS_DUMP_USES_AMEROOT = 655369
SIPAEVENT_VBS_VSM_NOSECRETS_ENFORCED = 655370
SIPAEVENT_KSR_SIGNATURE = 720897
SIPAEVENT_DRTM_STATE_AUTH = 786433
SIPAEVENT_DRTM_SMM_LEVEL = 786434
SIPAEVENT_DRTM_AMD_SMM_HASH = 786435
SIPAEVENT_DRTM_AMD_SMM_SIGNER_KEY = 786436
FVEB_UNLOCK_FLAG_NONE = 0
FVEB_UNLOCK_FLAG_CACHED = 1
FVEB_UNLOCK_FLAG_MEDIA = 2
FVEB_UNLOCK_FLAG_TPM = 4
FVEB_UNLOCK_FLAG_PIN = 16
FVEB_UNLOCK_FLAG_EXTERNAL = 32
FVEB_UNLOCK_FLAG_RECOVERY = 64
FVEB_UNLOCK_FLAG_PASSPHRASE = 128
FVEB_UNLOCK_FLAG_NBP = 256
FVEB_UNLOCK_FLAG_AUK_OSFVEINFO = 512
OSDEVICE_TYPE_UNKNOWN = 0
OSDEVICE_TYPE_BLOCKIO_HARDDISK = 65537
OSDEVICE_TYPE_BLOCKIO_REMOVABLEDISK = 65538
OSDEVICE_TYPE_BLOCKIO_CDROM = 65539
OSDEVICE_TYPE_BLOCKIO_PARTITION = 65540
OSDEVICE_TYPE_BLOCKIO_FILE = 65541
OSDEVICE_TYPE_BLOCKIO_RAMDISK = 65542
OSDEVICE_TYPE_BLOCKIO_VIRTUALHARDDISK = 65543
OSDEVICE_TYPE_SERIAL = 131072
OSDEVICE_TYPE_UDP = 196608
OSDEVICE_TYPE_VMBUS = 262144
OSDEVICE_TYPE_COMPOSITE = 327680
SIPAHDRSIGNATURE = 1279476311
SIPALOGVERSION = 1
SIPAKSRHDRSIGNATURE = 1297240907
WBCL_DIGEST_ALG_ID_SHA_1 = 4
WBCL_DIGEST_ALG_ID_SHA_2_256 = 11
WBCL_DIGEST_ALG_ID_SHA_2_384 = 12
WBCL_DIGEST_ALG_ID_SHA_2_512 = 13
WBCL_DIGEST_ALG_ID_SM3_256 = 18
WBCL_DIGEST_ALG_ID_SHA3_256 = 39
WBCL_DIGEST_ALG_ID_SHA3_384 = 40
WBCL_DIGEST_ALG_ID_SHA3_512 = 41
WBCL_DIGEST_ALG_BITMAP_SHA_1 = 1
WBCL_DIGEST_ALG_BITMAP_SHA_2_256 = 2
WBCL_DIGEST_ALG_BITMAP_SHA_2_384 = 4
WBCL_DIGEST_ALG_BITMAP_SHA_2_512 = 8
WBCL_DIGEST_ALG_BITMAP_SM3_256 = 16
WBCL_DIGEST_ALG_BITMAP_SHA3_256 = 32
WBCL_DIGEST_ALG_BITMAP_SHA3_384 = 64
WBCL_DIGEST_ALG_BITMAP_SHA3_512 = 128
WBCL_HASH_LEN_SHA1 = 20
IS_GUAR_RSPEC = 130
GUAR_ADSPARM_C = 131
GUAR_ADSPARM_D = 132
GUAR_ADSPARM_Ctot = 133
GUAR_ADSPARM_Dtot = 134
GUAR_ADSPARM_Csum = 135
GUAR_ADSPARM_Dsum = 136
LPM_HANDLE = IntPtr
RHANDLE = IntPtr
def _define_FLOWSPEC_head():
    class FLOWSPEC(Structure):
        pass
    return FLOWSPEC
def _define_FLOWSPEC():
    FLOWSPEC = win32more.NetworkManagement.QoS.FLOWSPEC_head
    FLOWSPEC._fields_ = [
        ("TokenRate", UInt32),
        ("TokenBucketSize", UInt32),
        ("PeakBandwidth", UInt32),
        ("Latency", UInt32),
        ("DelayVariation", UInt32),
        ("ServiceType", UInt32),
        ("MaxSduSize", UInt32),
        ("MinimumPolicedSize", UInt32),
    ]
    return FLOWSPEC
def _define_QOS_OBJECT_HDR_head():
    class QOS_OBJECT_HDR(Structure):
        pass
    return QOS_OBJECT_HDR
def _define_QOS_OBJECT_HDR():
    QOS_OBJECT_HDR = win32more.NetworkManagement.QoS.QOS_OBJECT_HDR_head
    QOS_OBJECT_HDR._fields_ = [
        ("ObjectType", UInt32),
        ("ObjectLength", UInt32),
    ]
    return QOS_OBJECT_HDR
def _define_QOS_SD_MODE_head():
    class QOS_SD_MODE(Structure):
        pass
    return QOS_SD_MODE
def _define_QOS_SD_MODE():
    QOS_SD_MODE = win32more.NetworkManagement.QoS.QOS_SD_MODE_head
    QOS_SD_MODE._fields_ = [
        ("ObjectHdr", win32more.NetworkManagement.QoS.QOS_OBJECT_HDR),
        ("ShapeDiscardMode", UInt32),
    ]
    return QOS_SD_MODE
def _define_QOS_SHAPING_RATE_head():
    class QOS_SHAPING_RATE(Structure):
        pass
    return QOS_SHAPING_RATE
def _define_QOS_SHAPING_RATE():
    QOS_SHAPING_RATE = win32more.NetworkManagement.QoS.QOS_SHAPING_RATE_head
    QOS_SHAPING_RATE._fields_ = [
        ("ObjectHdr", win32more.NetworkManagement.QoS.QOS_OBJECT_HDR),
        ("ShapingRate", UInt32),
    ]
    return QOS_SHAPING_RATE
def _define_RsvpObjHdr_head():
    class RsvpObjHdr(Structure):
        pass
    return RsvpObjHdr
def _define_RsvpObjHdr():
    RsvpObjHdr = win32more.NetworkManagement.QoS.RsvpObjHdr_head
    RsvpObjHdr._fields_ = [
        ("obj_length", UInt16),
        ("obj_class", Byte),
        ("obj_ctype", Byte),
    ]
    return RsvpObjHdr
def _define_Session_IPv4_head():
    class Session_IPv4(Structure):
        pass
    return Session_IPv4
def _define_Session_IPv4():
    Session_IPv4 = win32more.NetworkManagement.QoS.Session_IPv4_head
    Session_IPv4._fields_ = [
        ("sess_destaddr", win32more.Networking.WinSock.IN_ADDR),
        ("sess_protid", Byte),
        ("sess_flags", Byte),
        ("sess_destport", UInt16),
    ]
    return Session_IPv4
def _define_RSVP_SESSION_head():
    class RSVP_SESSION(Structure):
        pass
    return RSVP_SESSION
def _define_RSVP_SESSION():
    RSVP_SESSION = win32more.NetworkManagement.QoS.RSVP_SESSION_head
    class RSVP_SESSION__sess_u_e__Union(Union):
        pass
    RSVP_SESSION__sess_u_e__Union._fields_ = [
        ("sess_ipv4", win32more.NetworkManagement.QoS.Session_IPv4),
    ]
    RSVP_SESSION._fields_ = [
        ("sess_header", win32more.NetworkManagement.QoS.RsvpObjHdr),
        ("sess_u", RSVP_SESSION__sess_u_e__Union),
    ]
    return RSVP_SESSION
def _define_Rsvp_Hop_IPv4_head():
    class Rsvp_Hop_IPv4(Structure):
        pass
    return Rsvp_Hop_IPv4
def _define_Rsvp_Hop_IPv4():
    Rsvp_Hop_IPv4 = win32more.NetworkManagement.QoS.Rsvp_Hop_IPv4_head
    Rsvp_Hop_IPv4._fields_ = [
        ("hop_ipaddr", win32more.Networking.WinSock.IN_ADDR),
        ("hop_LIH", UInt32),
    ]
    return Rsvp_Hop_IPv4
def _define_RSVP_HOP_head():
    class RSVP_HOP(Structure):
        pass
    return RSVP_HOP
def _define_RSVP_HOP():
    RSVP_HOP = win32more.NetworkManagement.QoS.RSVP_HOP_head
    class RSVP_HOP__hop_u_e__Union(Union):
        pass
    RSVP_HOP__hop_u_e__Union._fields_ = [
        ("hop_ipv4", win32more.NetworkManagement.QoS.Rsvp_Hop_IPv4),
    ]
    RSVP_HOP._fields_ = [
        ("hop_header", win32more.NetworkManagement.QoS.RsvpObjHdr),
        ("hop_u", RSVP_HOP__hop_u_e__Union),
    ]
    return RSVP_HOP
def _define_RESV_STYLE_head():
    class RESV_STYLE(Structure):
        pass
    return RESV_STYLE
def _define_RESV_STYLE():
    RESV_STYLE = win32more.NetworkManagement.QoS.RESV_STYLE_head
    RESV_STYLE._fields_ = [
        ("style_header", win32more.NetworkManagement.QoS.RsvpObjHdr),
        ("style_word", UInt32),
    ]
    return RESV_STYLE
def _define_Filter_Spec_IPv4_head():
    class Filter_Spec_IPv4(Structure):
        pass
    return Filter_Spec_IPv4
def _define_Filter_Spec_IPv4():
    Filter_Spec_IPv4 = win32more.NetworkManagement.QoS.Filter_Spec_IPv4_head
    Filter_Spec_IPv4._fields_ = [
        ("filt_ipaddr", win32more.Networking.WinSock.IN_ADDR),
        ("filt_unused", UInt16),
        ("filt_port", UInt16),
    ]
    return Filter_Spec_IPv4
def _define_Filter_Spec_IPv4GPI_head():
    class Filter_Spec_IPv4GPI(Structure):
        pass
    return Filter_Spec_IPv4GPI
def _define_Filter_Spec_IPv4GPI():
    Filter_Spec_IPv4GPI = win32more.NetworkManagement.QoS.Filter_Spec_IPv4GPI_head
    Filter_Spec_IPv4GPI._fields_ = [
        ("filt_ipaddr", win32more.Networking.WinSock.IN_ADDR),
        ("filt_gpi", UInt32),
    ]
    return Filter_Spec_IPv4GPI
def _define_FILTER_SPEC_head():
    class FILTER_SPEC(Structure):
        pass
    return FILTER_SPEC
def _define_FILTER_SPEC():
    FILTER_SPEC = win32more.NetworkManagement.QoS.FILTER_SPEC_head
    class FILTER_SPEC__filt_u_e__Union(Union):
        pass
    FILTER_SPEC__filt_u_e__Union._fields_ = [
        ("filt_ipv4", win32more.NetworkManagement.QoS.Filter_Spec_IPv4),
        ("filt_ipv4gpi", win32more.NetworkManagement.QoS.Filter_Spec_IPv4GPI),
    ]
    FILTER_SPEC._fields_ = [
        ("filt_header", win32more.NetworkManagement.QoS.RsvpObjHdr),
        ("filt_u", FILTER_SPEC__filt_u_e__Union),
    ]
    return FILTER_SPEC
def _define_Scope_list_ipv4_head():
    class Scope_list_ipv4(Structure):
        pass
    return Scope_list_ipv4
def _define_Scope_list_ipv4():
    Scope_list_ipv4 = win32more.NetworkManagement.QoS.Scope_list_ipv4_head
    Scope_list_ipv4._fields_ = [
        ("scopl_ipaddr", win32more.Networking.WinSock.IN_ADDR * 0),
    ]
    return Scope_list_ipv4
def _define_RSVP_SCOPE_head():
    class RSVP_SCOPE(Structure):
        pass
    return RSVP_SCOPE
def _define_RSVP_SCOPE():
    RSVP_SCOPE = win32more.NetworkManagement.QoS.RSVP_SCOPE_head
    class RSVP_SCOPE__scope_u_e__Union(Union):
        pass
    RSVP_SCOPE__scope_u_e__Union._fields_ = [
        ("scopl_ipv4", win32more.NetworkManagement.QoS.Scope_list_ipv4),
    ]
    RSVP_SCOPE._fields_ = [
        ("scopl_header", win32more.NetworkManagement.QoS.RsvpObjHdr),
        ("scope_u", RSVP_SCOPE__scope_u_e__Union),
    ]
    return RSVP_SCOPE
def _define_Error_Spec_IPv4_head():
    class Error_Spec_IPv4(Structure):
        pass
    return Error_Spec_IPv4
def _define_Error_Spec_IPv4():
    Error_Spec_IPv4 = win32more.NetworkManagement.QoS.Error_Spec_IPv4_head
    Error_Spec_IPv4._fields_ = [
        ("errs_errnode", win32more.Networking.WinSock.IN_ADDR),
        ("errs_flags", Byte),
        ("errs_code", Byte),
        ("errs_value", UInt16),
    ]
    return Error_Spec_IPv4
def _define_ERROR_SPEC_head():
    class ERROR_SPEC(Structure):
        pass
    return ERROR_SPEC
def _define_ERROR_SPEC():
    ERROR_SPEC = win32more.NetworkManagement.QoS.ERROR_SPEC_head
    class ERROR_SPEC__errs_u_e__Union(Union):
        pass
    ERROR_SPEC__errs_u_e__Union._fields_ = [
        ("errs_ipv4", win32more.NetworkManagement.QoS.Error_Spec_IPv4),
    ]
    ERROR_SPEC._fields_ = [
        ("errs_header", win32more.NetworkManagement.QoS.RsvpObjHdr),
        ("errs_u", ERROR_SPEC__errs_u_e__Union),
    ]
    return ERROR_SPEC
def _define_POLICY_DATA_head():
    class POLICY_DATA(Structure):
        pass
    return POLICY_DATA
def _define_POLICY_DATA():
    POLICY_DATA = win32more.NetworkManagement.QoS.POLICY_DATA_head
    POLICY_DATA._fields_ = [
        ("PolicyObjHdr", win32more.NetworkManagement.QoS.RsvpObjHdr),
        ("usPeOffset", UInt16),
        ("usReserved", UInt16),
    ]
    return POLICY_DATA
def _define_POLICY_ELEMENT_head():
    class POLICY_ELEMENT(Structure):
        pass
    return POLICY_ELEMENT
def _define_POLICY_ELEMENT():
    POLICY_ELEMENT = win32more.NetworkManagement.QoS.POLICY_ELEMENT_head
    POLICY_ELEMENT._fields_ = [
        ("usPeLength", UInt16),
        ("usPeType", UInt16),
        ("ucPeData", Byte * 4),
    ]
    return POLICY_ELEMENT
int_serv_wkp = Int32
IS_WKP_HOP_CNT = 4
IS_WKP_PATH_BW = 6
IS_WKP_MIN_LATENCY = 8
IS_WKP_COMPOSED_MTU = 10
IS_WKP_TB_TSPEC = 127
IS_WKP_Q_TSPEC = 128
def _define_IntServMainHdr_head():
    class IntServMainHdr(Structure):
        pass
    return IntServMainHdr
def _define_IntServMainHdr():
    IntServMainHdr = win32more.NetworkManagement.QoS.IntServMainHdr_head
    IntServMainHdr._fields_ = [
        ("ismh_version", Byte),
        ("ismh_unused", Byte),
        ("ismh_len32b", UInt16),
    ]
    return IntServMainHdr
def _define_IntServServiceHdr_head():
    class IntServServiceHdr(Structure):
        pass
    return IntServServiceHdr
def _define_IntServServiceHdr():
    IntServServiceHdr = win32more.NetworkManagement.QoS.IntServServiceHdr_head
    IntServServiceHdr._fields_ = [
        ("issh_service", Byte),
        ("issh_flags", Byte),
        ("issh_len32b", UInt16),
    ]
    return IntServServiceHdr
def _define_IntServParmHdr_head():
    class IntServParmHdr(Structure):
        pass
    return IntServParmHdr
def _define_IntServParmHdr():
    IntServParmHdr = win32more.NetworkManagement.QoS.IntServParmHdr_head
    IntServParmHdr._fields_ = [
        ("isph_parm_num", Byte),
        ("isph_flags", Byte),
        ("isph_len32b", UInt16),
    ]
    return IntServParmHdr
def _define_GenTspecParms_head():
    class GenTspecParms(Structure):
        pass
    return GenTspecParms
def _define_GenTspecParms():
    GenTspecParms = win32more.NetworkManagement.QoS.GenTspecParms_head
    GenTspecParms._fields_ = [
        ("TB_Tspec_r", Single),
        ("TB_Tspec_b", Single),
        ("TB_Tspec_p", Single),
        ("TB_Tspec_m", UInt32),
        ("TB_Tspec_M", UInt32),
    ]
    return GenTspecParms
def _define_GenTspec_head():
    class GenTspec(Structure):
        pass
    return GenTspec
def _define_GenTspec():
    GenTspec = win32more.NetworkManagement.QoS.GenTspec_head
    GenTspec._fields_ = [
        ("gen_Tspec_serv_hdr", win32more.NetworkManagement.QoS.IntServServiceHdr),
        ("gen_Tspec_parm_hdr", win32more.NetworkManagement.QoS.IntServParmHdr),
        ("gen_Tspec_parms", win32more.NetworkManagement.QoS.GenTspecParms),
    ]
    return GenTspec
def _define_QualTspecParms_head():
    class QualTspecParms(Structure):
        pass
    return QualTspecParms
def _define_QualTspecParms():
    QualTspecParms = win32more.NetworkManagement.QoS.QualTspecParms_head
    QualTspecParms._fields_ = [
        ("TB_Tspec_M", UInt32),
    ]
    return QualTspecParms
def _define_QualTspec_head():
    class QualTspec(Structure):
        pass
    return QualTspec
def _define_QualTspec():
    QualTspec = win32more.NetworkManagement.QoS.QualTspec_head
    QualTspec._fields_ = [
        ("qual_Tspec_serv_hdr", win32more.NetworkManagement.QoS.IntServServiceHdr),
        ("qual_Tspec_parm_hdr", win32more.NetworkManagement.QoS.IntServParmHdr),
        ("qual_Tspec_parms", win32more.NetworkManagement.QoS.QualTspecParms),
    ]
    return QualTspec
def _define_QualAppFlowSpec_head():
    class QualAppFlowSpec(Structure):
        pass
    return QualAppFlowSpec
def _define_QualAppFlowSpec():
    QualAppFlowSpec = win32more.NetworkManagement.QoS.QualAppFlowSpec_head
    QualAppFlowSpec._fields_ = [
        ("Q_spec_serv_hdr", win32more.NetworkManagement.QoS.IntServServiceHdr),
        ("Q_spec_parm_hdr", win32more.NetworkManagement.QoS.IntServParmHdr),
        ("Q_spec_parms", win32more.NetworkManagement.QoS.QualTspecParms),
    ]
    return QualAppFlowSpec
def _define_IntServTspecBody_head():
    class IntServTspecBody(Structure):
        pass
    return IntServTspecBody
def _define_IntServTspecBody():
    IntServTspecBody = win32more.NetworkManagement.QoS.IntServTspecBody_head
    class IntServTspecBody__tspec_u_e__Union(Union):
        pass
    IntServTspecBody__tspec_u_e__Union._fields_ = [
        ("gen_stspec", win32more.NetworkManagement.QoS.GenTspec),
        ("qual_stspec", win32more.NetworkManagement.QoS.QualTspec),
    ]
    IntServTspecBody._fields_ = [
        ("st_mh", win32more.NetworkManagement.QoS.IntServMainHdr),
        ("tspec_u", IntServTspecBody__tspec_u_e__Union),
    ]
    return IntServTspecBody
def _define_SENDER_TSPEC_head():
    class SENDER_TSPEC(Structure):
        pass
    return SENDER_TSPEC
def _define_SENDER_TSPEC():
    SENDER_TSPEC = win32more.NetworkManagement.QoS.SENDER_TSPEC_head
    SENDER_TSPEC._fields_ = [
        ("stspec_header", win32more.NetworkManagement.QoS.RsvpObjHdr),
        ("stspec_body", win32more.NetworkManagement.QoS.IntServTspecBody),
    ]
    return SENDER_TSPEC
def _define_CtrlLoadFlowspec_head():
    class CtrlLoadFlowspec(Structure):
        pass
    return CtrlLoadFlowspec
def _define_CtrlLoadFlowspec():
    CtrlLoadFlowspec = win32more.NetworkManagement.QoS.CtrlLoadFlowspec_head
    CtrlLoadFlowspec._fields_ = [
        ("CL_spec_serv_hdr", win32more.NetworkManagement.QoS.IntServServiceHdr),
        ("CL_spec_parm_hdr", win32more.NetworkManagement.QoS.IntServParmHdr),
        ("CL_spec_parms", win32more.NetworkManagement.QoS.GenTspecParms),
    ]
    return CtrlLoadFlowspec
def _define_GuarRspec_head():
    class GuarRspec(Structure):
        pass
    return GuarRspec
def _define_GuarRspec():
    GuarRspec = win32more.NetworkManagement.QoS.GuarRspec_head
    GuarRspec._fields_ = [
        ("Guar_R", Single),
        ("Guar_S", UInt32),
    ]
    return GuarRspec
def _define_GuarFlowSpec_head():
    class GuarFlowSpec(Structure):
        pass
    return GuarFlowSpec
def _define_GuarFlowSpec():
    GuarFlowSpec = win32more.NetworkManagement.QoS.GuarFlowSpec_head
    GuarFlowSpec._fields_ = [
        ("Guar_serv_hdr", win32more.NetworkManagement.QoS.IntServServiceHdr),
        ("Guar_Tspec_hdr", win32more.NetworkManagement.QoS.IntServParmHdr),
        ("Guar_Tspec_parms", win32more.NetworkManagement.QoS.GenTspecParms),
        ("Guar_Rspec_hdr", win32more.NetworkManagement.QoS.IntServParmHdr),
        ("Guar_Rspec", win32more.NetworkManagement.QoS.GuarRspec),
    ]
    return GuarFlowSpec
def _define_IntServFlowSpec_head():
    class IntServFlowSpec(Structure):
        pass
    return IntServFlowSpec
def _define_IntServFlowSpec():
    IntServFlowSpec = win32more.NetworkManagement.QoS.IntServFlowSpec_head
    class IntServFlowSpec__spec_u_e__Union(Union):
        pass
    IntServFlowSpec__spec_u_e__Union._fields_ = [
        ("CL_spec", win32more.NetworkManagement.QoS.CtrlLoadFlowspec),
        ("G_spec", win32more.NetworkManagement.QoS.GuarFlowSpec),
        ("Q_spec", win32more.NetworkManagement.QoS.QualAppFlowSpec),
    ]
    IntServFlowSpec._fields_ = [
        ("spec_mh", win32more.NetworkManagement.QoS.IntServMainHdr),
        ("spec_u", IntServFlowSpec__spec_u_e__Union),
    ]
    return IntServFlowSpec
def _define_IS_FLOWSPEC_head():
    class IS_FLOWSPEC(Structure):
        pass
    return IS_FLOWSPEC
def _define_IS_FLOWSPEC():
    IS_FLOWSPEC = win32more.NetworkManagement.QoS.IS_FLOWSPEC_head
    IS_FLOWSPEC._fields_ = [
        ("flow_header", win32more.NetworkManagement.QoS.RsvpObjHdr),
        ("flow_body", win32more.NetworkManagement.QoS.IntServFlowSpec),
    ]
    return IS_FLOWSPEC
def _define_flow_desc_head():
    class flow_desc(Structure):
        pass
    return flow_desc
def _define_flow_desc():
    flow_desc = win32more.NetworkManagement.QoS.flow_desc_head
    class flow_desc__u1_e__Union(Union):
        pass
    flow_desc__u1_e__Union._fields_ = [
        ("stspec", POINTER(win32more.NetworkManagement.QoS.SENDER_TSPEC_head)),
        ("isflow", POINTER(win32more.NetworkManagement.QoS.IS_FLOWSPEC_head)),
    ]
    class flow_desc__u2_e__Union(Union):
        pass
    flow_desc__u2_e__Union._fields_ = [
        ("stemp", POINTER(win32more.NetworkManagement.QoS.FILTER_SPEC_head)),
        ("fspec", POINTER(win32more.NetworkManagement.QoS.FILTER_SPEC_head)),
    ]
    flow_desc._fields_ = [
        ("u1", flow_desc__u1_e__Union),
        ("u2", flow_desc__u2_e__Union),
    ]
    return flow_desc
def _define_Gads_parms_t_head():
    class Gads_parms_t(Structure):
        pass
    return Gads_parms_t
def _define_Gads_parms_t():
    Gads_parms_t = win32more.NetworkManagement.QoS.Gads_parms_t_head
    Gads_parms_t._fields_ = [
        ("Gads_serv_hdr", win32more.NetworkManagement.QoS.IntServServiceHdr),
        ("Gads_Ctot_hdr", win32more.NetworkManagement.QoS.IntServParmHdr),
        ("Gads_Ctot", UInt32),
        ("Gads_Dtot_hdr", win32more.NetworkManagement.QoS.IntServParmHdr),
        ("Gads_Dtot", UInt32),
        ("Gads_Csum_hdr", win32more.NetworkManagement.QoS.IntServParmHdr),
        ("Gads_Csum", UInt32),
        ("Gads_Dsum_hdr", win32more.NetworkManagement.QoS.IntServParmHdr),
        ("Gads_Dsum", UInt32),
    ]
    return Gads_parms_t
def _define_GenAdspecParams_head():
    class GenAdspecParams(Structure):
        pass
    return GenAdspecParams
def _define_GenAdspecParams():
    GenAdspecParams = win32more.NetworkManagement.QoS.GenAdspecParams_head
    GenAdspecParams._fields_ = [
        ("gen_parm_hdr", win32more.NetworkManagement.QoS.IntServServiceHdr),
        ("gen_parm_hopcnt_hdr", win32more.NetworkManagement.QoS.IntServParmHdr),
        ("gen_parm_hopcnt", UInt32),
        ("gen_parm_pathbw_hdr", win32more.NetworkManagement.QoS.IntServParmHdr),
        ("gen_parm_path_bw", Single),
        ("gen_parm_minlat_hdr", win32more.NetworkManagement.QoS.IntServParmHdr),
        ("gen_parm_min_latency", UInt32),
        ("gen_parm_compmtu_hdr", win32more.NetworkManagement.QoS.IntServParmHdr),
        ("gen_parm_composed_MTU", UInt32),
    ]
    return GenAdspecParams
def _define_IS_ADSPEC_BODY_head():
    class IS_ADSPEC_BODY(Structure):
        pass
    return IS_ADSPEC_BODY
def _define_IS_ADSPEC_BODY():
    IS_ADSPEC_BODY = win32more.NetworkManagement.QoS.IS_ADSPEC_BODY_head
    IS_ADSPEC_BODY._fields_ = [
        ("adspec_mh", win32more.NetworkManagement.QoS.IntServMainHdr),
        ("adspec_genparms", win32more.NetworkManagement.QoS.GenAdspecParams),
    ]
    return IS_ADSPEC_BODY
def _define_ADSPEC_head():
    class ADSPEC(Structure):
        pass
    return ADSPEC
def _define_ADSPEC():
    ADSPEC = win32more.NetworkManagement.QoS.ADSPEC_head
    ADSPEC._fields_ = [
        ("adspec_header", win32more.NetworkManagement.QoS.RsvpObjHdr),
        ("adspec_body", win32more.NetworkManagement.QoS.IS_ADSPEC_BODY),
    ]
    return ADSPEC
def _define_ID_ERROR_OBJECT_head():
    class ID_ERROR_OBJECT(Structure):
        pass
    return ID_ERROR_OBJECT
def _define_ID_ERROR_OBJECT():
    ID_ERROR_OBJECT = win32more.NetworkManagement.QoS.ID_ERROR_OBJECT_head
    ID_ERROR_OBJECT._fields_ = [
        ("usIdErrLength", UInt16),
        ("ucAType", Byte),
        ("ucSubType", Byte),
        ("usReserved", UInt16),
        ("usIdErrorValue", UInt16),
        ("ucIdErrData", Byte * 4),
    ]
    return ID_ERROR_OBJECT
def _define_RSVP_MSG_OBJS_head():
    class RSVP_MSG_OBJS(Structure):
        pass
    return RSVP_MSG_OBJS
def _define_RSVP_MSG_OBJS():
    RSVP_MSG_OBJS = win32more.NetworkManagement.QoS.RSVP_MSG_OBJS_head
    RSVP_MSG_OBJS._fields_ = [
        ("RsvpMsgType", Int32),
        ("pRsvpSession", POINTER(win32more.NetworkManagement.QoS.RSVP_SESSION_head)),
        ("pRsvpFromHop", POINTER(win32more.NetworkManagement.QoS.RSVP_HOP_head)),
        ("pRsvpToHop", POINTER(win32more.NetworkManagement.QoS.RSVP_HOP_head)),
        ("pResvStyle", POINTER(win32more.NetworkManagement.QoS.RESV_STYLE_head)),
        ("pRsvpScope", POINTER(win32more.NetworkManagement.QoS.RSVP_SCOPE_head)),
        ("FlowDescCount", Int32),
        ("pFlowDescs", POINTER(win32more.NetworkManagement.QoS.flow_desc_head)),
        ("PdObjectCount", Int32),
        ("ppPdObjects", POINTER(POINTER(win32more.NetworkManagement.QoS.POLICY_DATA_head))),
        ("pErrorSpec", POINTER(win32more.NetworkManagement.QoS.ERROR_SPEC_head)),
        ("pAdspec", POINTER(win32more.NetworkManagement.QoS.ADSPEC_head)),
    ]
    return RSVP_MSG_OBJS
def _define_PALLOCMEM():
    return CFUNCTYPE(c_void_p,UInt32, use_last_error=False)
def _define_PFREEMEM():
    return CFUNCTYPE(Void,c_void_p, use_last_error=False)
def _define_policy_decision_head():
    class policy_decision(Structure):
        pass
    return policy_decision
def _define_policy_decision():
    policy_decision = win32more.NetworkManagement.QoS.policy_decision_head
    policy_decision._fields_ = [
        ("lpvResult", UInt32),
        ("wPolicyErrCode", UInt16),
        ("wPolicyErrValue", UInt16),
    ]
    return policy_decision
def _define_CBADMITRESULT():
    return CFUNCTYPE(POINTER(UInt32),win32more.NetworkManagement.QoS.LPM_HANDLE,win32more.NetworkManagement.QoS.RHANDLE,UInt32,Int32,Int32,POINTER(win32more.NetworkManagement.QoS.policy_decision_head), use_last_error=False)
def _define_CBGETRSVPOBJECTS():
    return CFUNCTYPE(POINTER(UInt32),win32more.NetworkManagement.QoS.LPM_HANDLE,win32more.NetworkManagement.QoS.RHANDLE,Int32,Int32,POINTER(POINTER(win32more.NetworkManagement.QoS.RsvpObjHdr_head)), use_last_error=False)
def _define_LPM_INIT_INFO_head():
    class LPM_INIT_INFO(Structure):
        pass
    return LPM_INIT_INFO
def _define_LPM_INIT_INFO():
    LPM_INIT_INFO = win32more.NetworkManagement.QoS.LPM_INIT_INFO_head
    LPM_INIT_INFO._fields_ = [
        ("PcmVersionNumber", UInt32),
        ("ResultTimeLimit", UInt32),
        ("ConfiguredLpmCount", Int32),
        ("AllocMemory", win32more.NetworkManagement.QoS.PALLOCMEM),
        ("FreeMemory", win32more.NetworkManagement.QoS.PFREEMEM),
        ("PcmAdmitResultCallback", win32more.NetworkManagement.QoS.CBADMITRESULT),
        ("GetRsvpObjectsCallback", win32more.NetworkManagement.QoS.CBGETRSVPOBJECTS),
    ]
    return LPM_INIT_INFO
def _define_lpmiptable_head():
    class lpmiptable(Structure):
        pass
    return lpmiptable
def _define_lpmiptable():
    lpmiptable = win32more.NetworkManagement.QoS.lpmiptable_head
    lpmiptable._fields_ = [
        ("ulIfIndex", UInt32),
        ("MediaType", UInt32),
        ("IfIpAddr", win32more.Networking.WinSock.IN_ADDR),
        ("IfNetMask", win32more.Networking.WinSock.IN_ADDR),
    ]
    return lpmiptable
QOS_TRAFFIC_TYPE = Int32
QOS_TRAFFIC_TYPE_QOSTrafficTypeBestEffort = 0
QOS_TRAFFIC_TYPE_QOSTrafficTypeBackground = 1
QOS_TRAFFIC_TYPE_QOSTrafficTypeExcellentEffort = 2
QOS_TRAFFIC_TYPE_QOSTrafficTypeAudioVideo = 3
QOS_TRAFFIC_TYPE_QOSTrafficTypeVoice = 4
QOS_TRAFFIC_TYPE_QOSTrafficTypeControl = 5
QOS_SET_FLOW = Int32
QOS_SET_FLOW_QOSSetTrafficType = 0
QOS_SET_FLOW_QOSSetOutgoingRate = 1
QOS_SET_FLOW_QOSSetOutgoingDSCPValue = 2
def _define_QOS_PACKET_PRIORITY_head():
    class QOS_PACKET_PRIORITY(Structure):
        pass
    return QOS_PACKET_PRIORITY
def _define_QOS_PACKET_PRIORITY():
    QOS_PACKET_PRIORITY = win32more.NetworkManagement.QoS.QOS_PACKET_PRIORITY_head
    QOS_PACKET_PRIORITY._fields_ = [
        ("ConformantDSCPValue", UInt32),
        ("NonConformantDSCPValue", UInt32),
        ("ConformantL2Value", UInt32),
        ("NonConformantL2Value", UInt32),
    ]
    return QOS_PACKET_PRIORITY
def _define_QOS_FLOW_FUNDAMENTALS_head():
    class QOS_FLOW_FUNDAMENTALS(Structure):
        pass
    return QOS_FLOW_FUNDAMENTALS
def _define_QOS_FLOW_FUNDAMENTALS():
    QOS_FLOW_FUNDAMENTALS = win32more.NetworkManagement.QoS.QOS_FLOW_FUNDAMENTALS_head
    QOS_FLOW_FUNDAMENTALS._fields_ = [
        ("BottleneckBandwidthSet", win32more.Foundation.BOOL),
        ("BottleneckBandwidth", UInt64),
        ("AvailableBandwidthSet", win32more.Foundation.BOOL),
        ("AvailableBandwidth", UInt64),
        ("RTTSet", win32more.Foundation.BOOL),
        ("RTT", UInt32),
    ]
    return QOS_FLOW_FUNDAMENTALS
QOS_FLOWRATE_REASON = Int32
QOS_FLOWRATE_REASON_QOSFlowRateNotApplicable = 0
QOS_FLOWRATE_REASON_QOSFlowRateContentChange = 1
QOS_FLOWRATE_REASON_QOSFlowRateCongestion = 2
QOS_FLOWRATE_REASON_QOSFlowRateHigherContentEncoding = 3
QOS_FLOWRATE_REASON_QOSFlowRateUserCaused = 4
QOS_SHAPING = Int32
QOS_SHAPING_QOSShapeOnly = 0
QOS_SHAPING_QOSShapeAndMark = 1
QOS_SHAPING_QOSUseNonConformantMarkings = 2
def _define_QOS_FLOWRATE_OUTGOING_head():
    class QOS_FLOWRATE_OUTGOING(Structure):
        pass
    return QOS_FLOWRATE_OUTGOING
def _define_QOS_FLOWRATE_OUTGOING():
    QOS_FLOWRATE_OUTGOING = win32more.NetworkManagement.QoS.QOS_FLOWRATE_OUTGOING_head
    QOS_FLOWRATE_OUTGOING._fields_ = [
        ("Bandwidth", UInt64),
        ("ShapingBehavior", win32more.NetworkManagement.QoS.QOS_SHAPING),
        ("Reason", win32more.NetworkManagement.QoS.QOS_FLOWRATE_REASON),
    ]
    return QOS_FLOWRATE_OUTGOING
QOS_QUERY_FLOW = Int32
QOS_QUERY_FLOW_QOSQueryFlowFundamentals = 0
QOS_QUERY_FLOW_QOSQueryPacketPriority = 1
QOS_QUERY_FLOW_QOSQueryOutgoingRate = 2
QOS_NOTIFY_FLOW = Int32
QOS_NOTIFY_FLOW_QOSNotifyCongested = 0
QOS_NOTIFY_FLOW_QOSNotifyUncongested = 1
QOS_NOTIFY_FLOW_QOSNotifyAvailable = 2
def _define_QOS_VERSION_head():
    class QOS_VERSION(Structure):
        pass
    return QOS_VERSION
def _define_QOS_VERSION():
    QOS_VERSION = win32more.NetworkManagement.QoS.QOS_VERSION_head
    QOS_VERSION._fields_ = [
        ("MajorVersion", UInt16),
        ("MinorVersion", UInt16),
    ]
    return QOS_VERSION
def _define_QOS_FRIENDLY_NAME_head():
    class QOS_FRIENDLY_NAME(Structure):
        pass
    return QOS_FRIENDLY_NAME
def _define_QOS_FRIENDLY_NAME():
    QOS_FRIENDLY_NAME = win32more.NetworkManagement.QoS.QOS_FRIENDLY_NAME_head
    QOS_FRIENDLY_NAME._fields_ = [
        ("ObjectHdr", win32more.NetworkManagement.QoS.QOS_OBJECT_HDR),
        ("FriendlyName", Char * 256),
    ]
    return QOS_FRIENDLY_NAME
def _define_QOS_TRAFFIC_CLASS_head():
    class QOS_TRAFFIC_CLASS(Structure):
        pass
    return QOS_TRAFFIC_CLASS
def _define_QOS_TRAFFIC_CLASS():
    QOS_TRAFFIC_CLASS = win32more.NetworkManagement.QoS.QOS_TRAFFIC_CLASS_head
    QOS_TRAFFIC_CLASS._fields_ = [
        ("ObjectHdr", win32more.NetworkManagement.QoS.QOS_OBJECT_HDR),
        ("TrafficClass", UInt32),
    ]
    return QOS_TRAFFIC_CLASS
def _define_QOS_DS_CLASS_head():
    class QOS_DS_CLASS(Structure):
        pass
    return QOS_DS_CLASS
def _define_QOS_DS_CLASS():
    QOS_DS_CLASS = win32more.NetworkManagement.QoS.QOS_DS_CLASS_head
    QOS_DS_CLASS._fields_ = [
        ("ObjectHdr", win32more.NetworkManagement.QoS.QOS_OBJECT_HDR),
        ("DSField", UInt32),
    ]
    return QOS_DS_CLASS
def _define_QOS_DIFFSERV_head():
    class QOS_DIFFSERV(Structure):
        pass
    return QOS_DIFFSERV
def _define_QOS_DIFFSERV():
    QOS_DIFFSERV = win32more.NetworkManagement.QoS.QOS_DIFFSERV_head
    QOS_DIFFSERV._fields_ = [
        ("ObjectHdr", win32more.NetworkManagement.QoS.QOS_OBJECT_HDR),
        ("DSFieldCount", UInt32),
        ("DiffservRule", Byte * 0),
    ]
    return QOS_DIFFSERV
def _define_QOS_DIFFSERV_RULE_head():
    class QOS_DIFFSERV_RULE(Structure):
        pass
    return QOS_DIFFSERV_RULE
def _define_QOS_DIFFSERV_RULE():
    QOS_DIFFSERV_RULE = win32more.NetworkManagement.QoS.QOS_DIFFSERV_RULE_head
    QOS_DIFFSERV_RULE._fields_ = [
        ("InboundDSField", Byte),
        ("ConformingOutboundDSField", Byte),
        ("NonConformingOutboundDSField", Byte),
        ("ConformingUserPriority", Byte),
        ("NonConformingUserPriority", Byte),
    ]
    return QOS_DIFFSERV_RULE
def _define_QOS_TCP_TRAFFIC_head():
    class QOS_TCP_TRAFFIC(Structure):
        pass
    return QOS_TCP_TRAFFIC
def _define_QOS_TCP_TRAFFIC():
    QOS_TCP_TRAFFIC = win32more.NetworkManagement.QoS.QOS_TCP_TRAFFIC_head
    QOS_TCP_TRAFFIC._fields_ = [
        ("ObjectHdr", win32more.NetworkManagement.QoS.QOS_OBJECT_HDR),
    ]
    return QOS_TCP_TRAFFIC
def _define_TCI_NOTIFY_HANDLER():
    return CFUNCTYPE(Void,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,UInt32,win32more.Foundation.HANDLE,UInt32,c_void_p, use_last_error=False)
def _define_TCI_ADD_FLOW_COMPLETE_HANDLER():
    return CFUNCTYPE(Void,win32more.Foundation.HANDLE,UInt32, use_last_error=False)
def _define_TCI_MOD_FLOW_COMPLETE_HANDLER():
    return CFUNCTYPE(Void,win32more.Foundation.HANDLE,UInt32, use_last_error=False)
def _define_TCI_DEL_FLOW_COMPLETE_HANDLER():
    return CFUNCTYPE(Void,win32more.Foundation.HANDLE,UInt32, use_last_error=False)
def _define_TCI_CLIENT_FUNC_LIST_head():
    class TCI_CLIENT_FUNC_LIST(Structure):
        pass
    return TCI_CLIENT_FUNC_LIST
def _define_TCI_CLIENT_FUNC_LIST():
    TCI_CLIENT_FUNC_LIST = win32more.NetworkManagement.QoS.TCI_CLIENT_FUNC_LIST_head
    TCI_CLIENT_FUNC_LIST._fields_ = [
        ("ClNotifyHandler", win32more.NetworkManagement.QoS.TCI_NOTIFY_HANDLER),
        ("ClAddFlowCompleteHandler", win32more.NetworkManagement.QoS.TCI_ADD_FLOW_COMPLETE_HANDLER),
        ("ClModifyFlowCompleteHandler", win32more.NetworkManagement.QoS.TCI_MOD_FLOW_COMPLETE_HANDLER),
        ("ClDeleteFlowCompleteHandler", win32more.NetworkManagement.QoS.TCI_DEL_FLOW_COMPLETE_HANDLER),
    ]
    return TCI_CLIENT_FUNC_LIST
def _define_ADDRESS_LIST_DESCRIPTOR_head():
    class ADDRESS_LIST_DESCRIPTOR(Structure):
        pass
    return ADDRESS_LIST_DESCRIPTOR
def _define_ADDRESS_LIST_DESCRIPTOR():
    ADDRESS_LIST_DESCRIPTOR = win32more.NetworkManagement.QoS.ADDRESS_LIST_DESCRIPTOR_head
    ADDRESS_LIST_DESCRIPTOR._fields_ = [
        ("MediaType", UInt32),
        ("AddressList", win32more.NetworkManagement.Ndis.NETWORK_ADDRESS_LIST),
    ]
    return ADDRESS_LIST_DESCRIPTOR
def _define_TC_IFC_DESCRIPTOR_head():
    class TC_IFC_DESCRIPTOR(Structure):
        pass
    return TC_IFC_DESCRIPTOR
def _define_TC_IFC_DESCRIPTOR():
    TC_IFC_DESCRIPTOR = win32more.NetworkManagement.QoS.TC_IFC_DESCRIPTOR_head
    TC_IFC_DESCRIPTOR._fields_ = [
        ("Length", UInt32),
        ("pInterfaceName", win32more.Foundation.PWSTR),
        ("pInterfaceID", win32more.Foundation.PWSTR),
        ("AddressListDesc", win32more.NetworkManagement.QoS.ADDRESS_LIST_DESCRIPTOR),
    ]
    return TC_IFC_DESCRIPTOR
def _define_TC_SUPPORTED_INFO_BUFFER_head():
    class TC_SUPPORTED_INFO_BUFFER(Structure):
        pass
    return TC_SUPPORTED_INFO_BUFFER
def _define_TC_SUPPORTED_INFO_BUFFER():
    TC_SUPPORTED_INFO_BUFFER = win32more.NetworkManagement.QoS.TC_SUPPORTED_INFO_BUFFER_head
    TC_SUPPORTED_INFO_BUFFER._fields_ = [
        ("InstanceIDLength", UInt16),
        ("InstanceID", Char * 256),
        ("InterfaceLuid", UInt64),
        ("AddrListDesc", win32more.NetworkManagement.QoS.ADDRESS_LIST_DESCRIPTOR),
    ]
    return TC_SUPPORTED_INFO_BUFFER
def _define_TC_GEN_FILTER_head():
    class TC_GEN_FILTER(Structure):
        pass
    return TC_GEN_FILTER
def _define_TC_GEN_FILTER():
    TC_GEN_FILTER = win32more.NetworkManagement.QoS.TC_GEN_FILTER_head
    TC_GEN_FILTER._fields_ = [
        ("AddressType", UInt16),
        ("PatternSize", UInt32),
        ("Pattern", c_void_p),
        ("Mask", c_void_p),
    ]
    return TC_GEN_FILTER
def _define_TC_GEN_FLOW_head():
    class TC_GEN_FLOW(Structure):
        pass
    return TC_GEN_FLOW
def _define_TC_GEN_FLOW():
    TC_GEN_FLOW = win32more.NetworkManagement.QoS.TC_GEN_FLOW_head
    TC_GEN_FLOW._fields_ = [
        ("SendingFlowspec", win32more.NetworkManagement.QoS.FLOWSPEC),
        ("ReceivingFlowspec", win32more.NetworkManagement.QoS.FLOWSPEC),
        ("TcObjectsLength", UInt32),
        ("TcObjects", win32more.NetworkManagement.QoS.QOS_OBJECT_HDR * 0),
    ]
    return TC_GEN_FLOW
def _define_IP_PATTERN_head():
    class IP_PATTERN(Structure):
        pass
    return IP_PATTERN
def _define_IP_PATTERN():
    IP_PATTERN = win32more.NetworkManagement.QoS.IP_PATTERN_head
    class IP_PATTERN__S_un_e__Union(Union):
        pass
    class IP_PATTERN__S_un_e__Union__S_un_icmp_e__Struct(Structure):
        pass
    IP_PATTERN__S_un_e__Union__S_un_icmp_e__Struct._fields_ = [
        ("s_type", Byte),
        ("s_code", Byte),
        ("filler", UInt16),
    ]
    class IP_PATTERN__S_un_e__Union__S_un_ports_e__Struct(Structure):
        pass
    IP_PATTERN__S_un_e__Union__S_un_ports_e__Struct._fields_ = [
        ("s_srcport", UInt16),
        ("s_dstport", UInt16),
    ]
    IP_PATTERN__S_un_e__Union._fields_ = [
        ("S_un_ports", IP_PATTERN__S_un_e__Union__S_un_ports_e__Struct),
        ("S_un_icmp", IP_PATTERN__S_un_e__Union__S_un_icmp_e__Struct),
        ("S_Spi", UInt32),
    ]
    IP_PATTERN._fields_ = [
        ("Reserved1", UInt32),
        ("Reserved2", UInt32),
        ("SrcAddr", UInt32),
        ("DstAddr", UInt32),
        ("S_un", IP_PATTERN__S_un_e__Union),
        ("ProtocolId", Byte),
        ("Reserved3", Byte * 3),
    ]
    return IP_PATTERN
def _define_IPX_PATTERN_head():
    class IPX_PATTERN(Structure):
        pass
    return IPX_PATTERN
def _define_IPX_PATTERN():
    IPX_PATTERN = win32more.NetworkManagement.QoS.IPX_PATTERN_head
    class IPX_PATTERN__Src_e__Struct(Structure):
        pass
    IPX_PATTERN__Src_e__Struct._fields_ = [
        ("NetworkAddress", UInt32),
        ("NodeAddress", Byte * 6),
        ("Socket", UInt16),
    ]
    IPX_PATTERN._fields_ = [
        ("Src", IPX_PATTERN__Src_e__Struct),
        ("Dest", IPX_PATTERN__Src_e__Struct),
    ]
    return IPX_PATTERN
def _define_ENUMERATION_BUFFER_head():
    class ENUMERATION_BUFFER(Structure):
        pass
    return ENUMERATION_BUFFER
def _define_ENUMERATION_BUFFER():
    ENUMERATION_BUFFER = win32more.NetworkManagement.QoS.ENUMERATION_BUFFER_head
    ENUMERATION_BUFFER._fields_ = [
        ("Length", UInt32),
        ("OwnerProcessId", UInt32),
        ("FlowNameLength", UInt16),
        ("FlowName", Char * 256),
        ("pFlow", POINTER(win32more.NetworkManagement.QoS.TC_GEN_FLOW_head)),
        ("NumberOfFilters", UInt32),
        ("GenericFilter", win32more.NetworkManagement.QoS.TC_GEN_FILTER * 0),
    ]
    return ENUMERATION_BUFFER
def _define_IN_ADDR_IPV4_head():
    class IN_ADDR_IPV4(Union):
        pass
    return IN_ADDR_IPV4
def _define_IN_ADDR_IPV4():
    IN_ADDR_IPV4 = win32more.NetworkManagement.QoS.IN_ADDR_IPV4_head
    IN_ADDR_IPV4._fields_ = [
        ("Addr", UInt32),
        ("AddrBytes", Byte * 4),
    ]
    return IN_ADDR_IPV4
def _define_IN_ADDR_IPV6_head():
    class IN_ADDR_IPV6(Structure):
        pass
    return IN_ADDR_IPV6
def _define_IN_ADDR_IPV6():
    IN_ADDR_IPV6 = win32more.NetworkManagement.QoS.IN_ADDR_IPV6_head
    IN_ADDR_IPV6._fields_ = [
        ("Addr", Byte * 16),
    ]
    return IN_ADDR_IPV6
def _define_RSVP_FILTERSPEC_V4_head():
    class RSVP_FILTERSPEC_V4(Structure):
        pass
    return RSVP_FILTERSPEC_V4
def _define_RSVP_FILTERSPEC_V4():
    RSVP_FILTERSPEC_V4 = win32more.NetworkManagement.QoS.RSVP_FILTERSPEC_V4_head
    RSVP_FILTERSPEC_V4._fields_ = [
        ("Address", win32more.NetworkManagement.QoS.IN_ADDR_IPV4),
        ("Unused", UInt16),
        ("Port", UInt16),
    ]
    return RSVP_FILTERSPEC_V4
def _define_RSVP_FILTERSPEC_V6_head():
    class RSVP_FILTERSPEC_V6(Structure):
        pass
    return RSVP_FILTERSPEC_V6
def _define_RSVP_FILTERSPEC_V6():
    RSVP_FILTERSPEC_V6 = win32more.NetworkManagement.QoS.RSVP_FILTERSPEC_V6_head
    RSVP_FILTERSPEC_V6._fields_ = [
        ("Address", win32more.NetworkManagement.QoS.IN_ADDR_IPV6),
        ("UnUsed", UInt16),
        ("Port", UInt16),
    ]
    return RSVP_FILTERSPEC_V6
def _define_RSVP_FILTERSPEC_V6_FLOW_head():
    class RSVP_FILTERSPEC_V6_FLOW(Structure):
        pass
    return RSVP_FILTERSPEC_V6_FLOW
def _define_RSVP_FILTERSPEC_V6_FLOW():
    RSVP_FILTERSPEC_V6_FLOW = win32more.NetworkManagement.QoS.RSVP_FILTERSPEC_V6_FLOW_head
    RSVP_FILTERSPEC_V6_FLOW._fields_ = [
        ("Address", win32more.NetworkManagement.QoS.IN_ADDR_IPV6),
        ("UnUsed", Byte),
        ("FlowLabel", Byte * 3),
    ]
    return RSVP_FILTERSPEC_V6_FLOW
def _define_RSVP_FILTERSPEC_V4_GPI_head():
    class RSVP_FILTERSPEC_V4_GPI(Structure):
        pass
    return RSVP_FILTERSPEC_V4_GPI
def _define_RSVP_FILTERSPEC_V4_GPI():
    RSVP_FILTERSPEC_V4_GPI = win32more.NetworkManagement.QoS.RSVP_FILTERSPEC_V4_GPI_head
    RSVP_FILTERSPEC_V4_GPI._fields_ = [
        ("Address", win32more.NetworkManagement.QoS.IN_ADDR_IPV4),
        ("GeneralPortId", UInt32),
    ]
    return RSVP_FILTERSPEC_V4_GPI
def _define_RSVP_FILTERSPEC_V6_GPI_head():
    class RSVP_FILTERSPEC_V6_GPI(Structure):
        pass
    return RSVP_FILTERSPEC_V6_GPI
def _define_RSVP_FILTERSPEC_V6_GPI():
    RSVP_FILTERSPEC_V6_GPI = win32more.NetworkManagement.QoS.RSVP_FILTERSPEC_V6_GPI_head
    RSVP_FILTERSPEC_V6_GPI._fields_ = [
        ("Address", win32more.NetworkManagement.QoS.IN_ADDR_IPV6),
        ("GeneralPortId", UInt32),
    ]
    return RSVP_FILTERSPEC_V6_GPI
FilterType = Int32
FILTERSPECV4 = 1
FILTERSPECV6 = 2
FILTERSPECV6_FLOW = 3
FILTERSPECV4_GPI = 4
FILTERSPECV6_GPI = 5
FILTERSPEC_END = 6
def _define_RSVP_FILTERSPEC_head():
    class RSVP_FILTERSPEC(Structure):
        pass
    return RSVP_FILTERSPEC
def _define_RSVP_FILTERSPEC():
    RSVP_FILTERSPEC = win32more.NetworkManagement.QoS.RSVP_FILTERSPEC_head
    class RSVP_FILTERSPEC__Anonymous_e__Union(Union):
        pass
    RSVP_FILTERSPEC__Anonymous_e__Union._fields_ = [
        ("FilterSpecV4", win32more.NetworkManagement.QoS.RSVP_FILTERSPEC_V4),
        ("FilterSpecV6", win32more.NetworkManagement.QoS.RSVP_FILTERSPEC_V6),
        ("FilterSpecV6Flow", win32more.NetworkManagement.QoS.RSVP_FILTERSPEC_V6_FLOW),
        ("FilterSpecV4Gpi", win32more.NetworkManagement.QoS.RSVP_FILTERSPEC_V4_GPI),
        ("FilterSpecV6Gpi", win32more.NetworkManagement.QoS.RSVP_FILTERSPEC_V6_GPI),
    ]
    RSVP_FILTERSPEC._anonymous_ = [
        'Anonymous',
    ]
    RSVP_FILTERSPEC._fields_ = [
        ("Type", win32more.NetworkManagement.QoS.FilterType),
        ("Anonymous", RSVP_FILTERSPEC__Anonymous_e__Union),
    ]
    return RSVP_FILTERSPEC
def _define_FLOWDESCRIPTOR_head():
    class FLOWDESCRIPTOR(Structure):
        pass
    return FLOWDESCRIPTOR
def _define_FLOWDESCRIPTOR():
    FLOWDESCRIPTOR = win32more.NetworkManagement.QoS.FLOWDESCRIPTOR_head
    FLOWDESCRIPTOR._fields_ = [
        ("FlowSpec", win32more.NetworkManagement.QoS.FLOWSPEC),
        ("NumFilters", UInt32),
        ("FilterList", POINTER(win32more.NetworkManagement.QoS.RSVP_FILTERSPEC_head)),
    ]
    return FLOWDESCRIPTOR
def _define_RSVP_POLICY_head():
    class RSVP_POLICY(Structure):
        pass
    return RSVP_POLICY
def _define_RSVP_POLICY():
    RSVP_POLICY = win32more.NetworkManagement.QoS.RSVP_POLICY_head
    RSVP_POLICY._fields_ = [
        ("Len", UInt16),
        ("Type", UInt16),
        ("Info", Byte * 4),
    ]
    return RSVP_POLICY
def _define_RSVP_POLICY_INFO_head():
    class RSVP_POLICY_INFO(Structure):
        pass
    return RSVP_POLICY_INFO
def _define_RSVP_POLICY_INFO():
    RSVP_POLICY_INFO = win32more.NetworkManagement.QoS.RSVP_POLICY_INFO_head
    RSVP_POLICY_INFO._fields_ = [
        ("ObjectHdr", win32more.NetworkManagement.QoS.QOS_OBJECT_HDR),
        ("NumPolicyElement", UInt32),
        ("PolicyElement", win32more.NetworkManagement.QoS.RSVP_POLICY * 0),
    ]
    return RSVP_POLICY_INFO
def _define_RSVP_RESERVE_INFO_head():
    class RSVP_RESERVE_INFO(Structure):
        pass
    return RSVP_RESERVE_INFO
def _define_RSVP_RESERVE_INFO():
    RSVP_RESERVE_INFO = win32more.NetworkManagement.QoS.RSVP_RESERVE_INFO_head
    RSVP_RESERVE_INFO._fields_ = [
        ("ObjectHdr", win32more.NetworkManagement.QoS.QOS_OBJECT_HDR),
        ("Style", UInt32),
        ("ConfirmRequest", UInt32),
        ("PolicyElementList", POINTER(win32more.NetworkManagement.QoS.RSVP_POLICY_INFO_head)),
        ("NumFlowDesc", UInt32),
        ("FlowDescList", POINTER(win32more.NetworkManagement.QoS.FLOWDESCRIPTOR_head)),
    ]
    return RSVP_RESERVE_INFO
def _define_RSVP_STATUS_INFO_head():
    class RSVP_STATUS_INFO(Structure):
        pass
    return RSVP_STATUS_INFO
def _define_RSVP_STATUS_INFO():
    RSVP_STATUS_INFO = win32more.NetworkManagement.QoS.RSVP_STATUS_INFO_head
    RSVP_STATUS_INFO._fields_ = [
        ("ObjectHdr", win32more.NetworkManagement.QoS.QOS_OBJECT_HDR),
        ("StatusCode", UInt32),
        ("ExtendedStatus1", UInt32),
        ("ExtendedStatus2", UInt32),
    ]
    return RSVP_STATUS_INFO
def _define_QOS_DESTADDR_head():
    class QOS_DESTADDR(Structure):
        pass
    return QOS_DESTADDR
def _define_QOS_DESTADDR():
    QOS_DESTADDR = win32more.NetworkManagement.QoS.QOS_DESTADDR_head
    QOS_DESTADDR._fields_ = [
        ("ObjectHdr", win32more.NetworkManagement.QoS.QOS_OBJECT_HDR),
        ("SocketAddress", POINTER(win32more.Networking.WinSock.SOCKADDR_head)),
        ("SocketAddressLength", UInt32),
    ]
    return QOS_DESTADDR
def _define_AD_GENERAL_PARAMS_head():
    class AD_GENERAL_PARAMS(Structure):
        pass
    return AD_GENERAL_PARAMS
def _define_AD_GENERAL_PARAMS():
    AD_GENERAL_PARAMS = win32more.NetworkManagement.QoS.AD_GENERAL_PARAMS_head
    AD_GENERAL_PARAMS._fields_ = [
        ("IntServAwareHopCount", UInt32),
        ("PathBandwidthEstimate", UInt32),
        ("MinimumLatency", UInt32),
        ("PathMTU", UInt32),
        ("Flags", UInt32),
    ]
    return AD_GENERAL_PARAMS
def _define_AD_GUARANTEED_head():
    class AD_GUARANTEED(Structure):
        pass
    return AD_GUARANTEED
def _define_AD_GUARANTEED():
    AD_GUARANTEED = win32more.NetworkManagement.QoS.AD_GUARANTEED_head
    AD_GUARANTEED._fields_ = [
        ("CTotal", UInt32),
        ("DTotal", UInt32),
        ("CSum", UInt32),
        ("DSum", UInt32),
    ]
    return AD_GUARANTEED
def _define_PARAM_BUFFER_head():
    class PARAM_BUFFER(Structure):
        pass
    return PARAM_BUFFER
def _define_PARAM_BUFFER():
    PARAM_BUFFER = win32more.NetworkManagement.QoS.PARAM_BUFFER_head
    PARAM_BUFFER._fields_ = [
        ("ParameterId", UInt32),
        ("Length", UInt32),
        ("Buffer", Byte * 0),
    ]
    return PARAM_BUFFER
def _define_CONTROL_SERVICE_head():
    class CONTROL_SERVICE(Structure):
        pass
    return CONTROL_SERVICE
def _define_CONTROL_SERVICE():
    CONTROL_SERVICE = win32more.NetworkManagement.QoS.CONTROL_SERVICE_head
    class CONTROL_SERVICE__Anonymous_e__Union(Union):
        pass
    CONTROL_SERVICE__Anonymous_e__Union._fields_ = [
        ("Guaranteed", win32more.NetworkManagement.QoS.AD_GUARANTEED),
        ("ParamBuffer", win32more.NetworkManagement.QoS.PARAM_BUFFER * 0),
    ]
    CONTROL_SERVICE._anonymous_ = [
        'Anonymous',
    ]
    CONTROL_SERVICE._fields_ = [
        ("Length", UInt32),
        ("Service", UInt32),
        ("Overrides", win32more.NetworkManagement.QoS.AD_GENERAL_PARAMS),
        ("Anonymous", CONTROL_SERVICE__Anonymous_e__Union),
    ]
    return CONTROL_SERVICE
def _define_RSVP_ADSPEC_head():
    class RSVP_ADSPEC(Structure):
        pass
    return RSVP_ADSPEC
def _define_RSVP_ADSPEC():
    RSVP_ADSPEC = win32more.NetworkManagement.QoS.RSVP_ADSPEC_head
    RSVP_ADSPEC._fields_ = [
        ("ObjectHdr", win32more.NetworkManagement.QoS.QOS_OBJECT_HDR),
        ("GeneralParams", win32more.NetworkManagement.QoS.AD_GENERAL_PARAMS),
        ("NumberOfServices", UInt32),
        ("Services", win32more.NetworkManagement.QoS.CONTROL_SERVICE * 0),
    ]
    return RSVP_ADSPEC
def _define_IDPE_ATTR_head():
    class IDPE_ATTR(Structure):
        pass
    return IDPE_ATTR
def _define_IDPE_ATTR():
    IDPE_ATTR = win32more.NetworkManagement.QoS.IDPE_ATTR_head
    IDPE_ATTR._fields_ = [
        ("PeAttribLength", UInt16),
        ("PeAttribType", Byte),
        ("PeAttribSubType", Byte),
        ("PeAttribValue", Byte * 4),
    ]
    return IDPE_ATTR
def _define_WBCL_Iterator_head():
    class WBCL_Iterator(Structure):
        pass
    return WBCL_Iterator
def _define_WBCL_Iterator():
    WBCL_Iterator = win32more.NetworkManagement.QoS.WBCL_Iterator_head
    WBCL_Iterator._pack_ = 1
    WBCL_Iterator._fields_ = [
        ("firstElementPtr", c_void_p),
        ("logSize", UInt32),
        ("currentElementPtr", c_void_p),
        ("currentElementSize", UInt32),
        ("digestSize", UInt16),
        ("logFormat", UInt16),
        ("numberOfDigests", UInt32),
        ("digestSizes", c_void_p),
        ("supportedAlgorithms", UInt32),
        ("hashAlgorithm", UInt16),
    ]
    return WBCL_Iterator
def _define_TCG_PCClientPCREventStruct_head():
    class TCG_PCClientPCREventStruct(Structure):
        pass
    return TCG_PCClientPCREventStruct
def _define_TCG_PCClientPCREventStruct():
    TCG_PCClientPCREventStruct = win32more.NetworkManagement.QoS.TCG_PCClientPCREventStruct_head
    TCG_PCClientPCREventStruct._pack_ = 1
    TCG_PCClientPCREventStruct._fields_ = [
        ("pcrIndex", UInt32),
        ("eventType", UInt32),
        ("digest", Byte * 20),
        ("eventDataSize", UInt32),
        ("event", Byte * 0),
    ]
    return TCG_PCClientPCREventStruct
def _define_TCG_PCClientTaggedEventStruct_head():
    class TCG_PCClientTaggedEventStruct(Structure):
        pass
    return TCG_PCClientTaggedEventStruct
def _define_TCG_PCClientTaggedEventStruct():
    TCG_PCClientTaggedEventStruct = win32more.NetworkManagement.QoS.TCG_PCClientTaggedEventStruct_head
    TCG_PCClientTaggedEventStruct._pack_ = 1
    TCG_PCClientTaggedEventStruct._fields_ = [
        ("EventID", UInt32),
        ("EventDataSize", UInt32),
        ("EventData", Byte * 0),
    ]
    return TCG_PCClientTaggedEventStruct
def _define_WBCL_LogHdr_head():
    class WBCL_LogHdr(Structure):
        pass
    return WBCL_LogHdr
def _define_WBCL_LogHdr():
    WBCL_LogHdr = win32more.NetworkManagement.QoS.WBCL_LogHdr_head
    WBCL_LogHdr._pack_ = 1
    WBCL_LogHdr._fields_ = [
        ("signature", UInt32),
        ("version", UInt32),
        ("entries", UInt32),
        ("length", UInt32),
    ]
    return WBCL_LogHdr
def _define_tag_SIPAEVENT_VSM_IDK_RSA_INFO_head():
    class tag_SIPAEVENT_VSM_IDK_RSA_INFO(Structure):
        pass
    return tag_SIPAEVENT_VSM_IDK_RSA_INFO
def _define_tag_SIPAEVENT_VSM_IDK_RSA_INFO():
    tag_SIPAEVENT_VSM_IDK_RSA_INFO = win32more.NetworkManagement.QoS.tag_SIPAEVENT_VSM_IDK_RSA_INFO_head
    tag_SIPAEVENT_VSM_IDK_RSA_INFO._pack_ = 1
    tag_SIPAEVENT_VSM_IDK_RSA_INFO._fields_ = [
        ("KeyBitLength", UInt32),
        ("PublicExpLengthBytes", UInt32),
        ("ModulusSizeBytes", UInt32),
        ("PublicKeyData", Byte * 0),
    ]
    return tag_SIPAEVENT_VSM_IDK_RSA_INFO
def _define_tag_SIPAEVENT_VSM_IDK_INFO_PAYLOAD_head():
    class tag_SIPAEVENT_VSM_IDK_INFO_PAYLOAD(Structure):
        pass
    return tag_SIPAEVENT_VSM_IDK_INFO_PAYLOAD
def _define_tag_SIPAEVENT_VSM_IDK_INFO_PAYLOAD():
    tag_SIPAEVENT_VSM_IDK_INFO_PAYLOAD = win32more.NetworkManagement.QoS.tag_SIPAEVENT_VSM_IDK_INFO_PAYLOAD_head
    class tag_SIPAEVENT_VSM_IDK_INFO_PAYLOAD__Anonymous_e__Union(Union):
        pass
    tag_SIPAEVENT_VSM_IDK_INFO_PAYLOAD__Anonymous_e__Union._fields_ = [
        ("RsaKeyInfo", win32more.NetworkManagement.QoS.tag_SIPAEVENT_VSM_IDK_RSA_INFO),
    ]
    tag_SIPAEVENT_VSM_IDK_INFO_PAYLOAD._pack_ = 1
    tag_SIPAEVENT_VSM_IDK_INFO_PAYLOAD._anonymous_ = [
        'Anonymous',
    ]
    tag_SIPAEVENT_VSM_IDK_INFO_PAYLOAD._fields_ = [
        ("KeyAlgID", UInt32),
        ("Anonymous", tag_SIPAEVENT_VSM_IDK_INFO_PAYLOAD__Anonymous_e__Union),
    ]
    return tag_SIPAEVENT_VSM_IDK_INFO_PAYLOAD
def _define_tag_SIPAEVENT_SI_POLICY_PAYLOAD_head():
    class tag_SIPAEVENT_SI_POLICY_PAYLOAD(Structure):
        pass
    return tag_SIPAEVENT_SI_POLICY_PAYLOAD
def _define_tag_SIPAEVENT_SI_POLICY_PAYLOAD():
    tag_SIPAEVENT_SI_POLICY_PAYLOAD = win32more.NetworkManagement.QoS.tag_SIPAEVENT_SI_POLICY_PAYLOAD_head
    tag_SIPAEVENT_SI_POLICY_PAYLOAD._pack_ = 1
    tag_SIPAEVENT_SI_POLICY_PAYLOAD._fields_ = [
        ("PolicyVersion", UInt64),
        ("PolicyNameLength", UInt16),
        ("HashAlgID", UInt16),
        ("DigestLength", UInt32),
        ("VarLengthData", Byte * 0),
    ]
    return tag_SIPAEVENT_SI_POLICY_PAYLOAD
def _define_tag_SIPAEVENT_REVOCATION_LIST_PAYLOAD_head():
    class tag_SIPAEVENT_REVOCATION_LIST_PAYLOAD(Structure):
        pass
    return tag_SIPAEVENT_REVOCATION_LIST_PAYLOAD
def _define_tag_SIPAEVENT_REVOCATION_LIST_PAYLOAD():
    tag_SIPAEVENT_REVOCATION_LIST_PAYLOAD = win32more.NetworkManagement.QoS.tag_SIPAEVENT_REVOCATION_LIST_PAYLOAD_head
    tag_SIPAEVENT_REVOCATION_LIST_PAYLOAD._pack_ = 1
    tag_SIPAEVENT_REVOCATION_LIST_PAYLOAD._fields_ = [
        ("CreationTime", Int64),
        ("DigestLength", UInt32),
        ("HashAlgID", UInt16),
        ("Digest", Byte * 0),
    ]
    return tag_SIPAEVENT_REVOCATION_LIST_PAYLOAD
def _define_tag_SIPAEVENT_KSR_SIGNATURE_PAYLOAD_head():
    class tag_SIPAEVENT_KSR_SIGNATURE_PAYLOAD(Structure):
        pass
    return tag_SIPAEVENT_KSR_SIGNATURE_PAYLOAD
def _define_tag_SIPAEVENT_KSR_SIGNATURE_PAYLOAD():
    tag_SIPAEVENT_KSR_SIGNATURE_PAYLOAD = win32more.NetworkManagement.QoS.tag_SIPAEVENT_KSR_SIGNATURE_PAYLOAD_head
    tag_SIPAEVENT_KSR_SIGNATURE_PAYLOAD._pack_ = 1
    tag_SIPAEVENT_KSR_SIGNATURE_PAYLOAD._fields_ = [
        ("SignAlgID", UInt32),
        ("SignatureLength", UInt32),
        ("Signature", Byte * 0),
    ]
    return tag_SIPAEVENT_KSR_SIGNATURE_PAYLOAD
def _define_tag_SIPAEVENT_SBCP_INFO_PAYLOAD_V1_head():
    class tag_SIPAEVENT_SBCP_INFO_PAYLOAD_V1(Structure):
        pass
    return tag_SIPAEVENT_SBCP_INFO_PAYLOAD_V1
def _define_tag_SIPAEVENT_SBCP_INFO_PAYLOAD_V1():
    tag_SIPAEVENT_SBCP_INFO_PAYLOAD_V1 = win32more.NetworkManagement.QoS.tag_SIPAEVENT_SBCP_INFO_PAYLOAD_V1_head
    tag_SIPAEVENT_SBCP_INFO_PAYLOAD_V1._pack_ = 1
    tag_SIPAEVENT_SBCP_INFO_PAYLOAD_V1._fields_ = [
        ("PayloadVersion", UInt32),
        ("VarDataOffset", UInt32),
        ("HashAlgID", UInt16),
        ("DigestLength", UInt16),
        ("Options", UInt32),
        ("SignersCount", UInt32),
        ("VarData", Byte * 0),
    ]
    return tag_SIPAEVENT_SBCP_INFO_PAYLOAD_V1
def _define_QOS_head():
    class QOS(Structure):
        pass
    return QOS
def _define_QOS():
    QOS = win32more.NetworkManagement.QoS.QOS_head
    QOS._fields_ = [
        ("SendingFlowspec", win32more.NetworkManagement.QoS.FLOWSPEC),
        ("ReceivingFlowspec", win32more.NetworkManagement.QoS.FLOWSPEC),
        ("ProviderSpecific", win32more.Networking.WinSock.WSABUF),
    ]
    return QOS
def _define_QOSCreateHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.NetworkManagement.QoS.QOS_VERSION_head),POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("QOSCreateHandle", windll["qwave"]), ((1, 'Version'),(1, 'QOSHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QOSCloseHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE, use_last_error=False)(("QOSCloseHandle", windll["qwave"]), ((1, 'QOSHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QOSStartTrackingClient():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Networking.WinSock.SOCKADDR_head),UInt32, use_last_error=False)(("QOSStartTrackingClient", windll["qwave"]), ((1, 'QOSHandle'),(1, 'DestAddr'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QOSStopTrackingClient():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Networking.WinSock.SOCKADDR_head),UInt32, use_last_error=False)(("QOSStopTrackingClient", windll["qwave"]), ((1, 'QOSHandle'),(1, 'DestAddr'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QOSEnumerateFlows():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(UInt32),c_void_p, use_last_error=False)(("QOSEnumerateFlows", windll["qwave"]), ((1, 'QOSHandle'),(1, 'Size'),(1, 'Buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QOSAddSocketToFlow():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Networking.WinSock.SOCKET,POINTER(win32more.Networking.WinSock.SOCKADDR_head),win32more.NetworkManagement.QoS.QOS_TRAFFIC_TYPE,UInt32,POINTER(UInt32), use_last_error=False)(("QOSAddSocketToFlow", windll["qwave"]), ((1, 'QOSHandle'),(1, 'Socket'),(1, 'DestAddr'),(1, 'TrafficType'),(1, 'Flags'),(1, 'FlowId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QOSRemoveSocketFromFlow():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Networking.WinSock.SOCKET,UInt32,UInt32, use_last_error=False)(("QOSRemoveSocketFromFlow", windll["qwave"]), ((1, 'QOSHandle'),(1, 'Socket'),(1, 'FlowId'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QOSSetFlow():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,win32more.NetworkManagement.QoS.QOS_SET_FLOW,UInt32,c_void_p,UInt32,POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(("QOSSetFlow", windll["qwave"]), ((1, 'QOSHandle'),(1, 'FlowId'),(1, 'Operation'),(1, 'Size'),(1, 'Buffer'),(1, 'Flags'),(1, 'Overlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QOSQueryFlow():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,win32more.NetworkManagement.QoS.QOS_QUERY_FLOW,POINTER(UInt32),c_void_p,UInt32,POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(("QOSQueryFlow", windll["qwave"]), ((1, 'QOSHandle'),(1, 'FlowId'),(1, 'Operation'),(1, 'Size'),(1, 'Buffer'),(1, 'Flags'),(1, 'Overlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QOSNotifyFlow():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,win32more.NetworkManagement.QoS.QOS_NOTIFY_FLOW,POINTER(UInt32),c_void_p,UInt32,POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(("QOSNotifyFlow", windll["qwave"]), ((1, 'QOSHandle'),(1, 'FlowId'),(1, 'Operation'),(1, 'Size'),(1, 'Buffer'),(1, 'Flags'),(1, 'Overlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QOSCancel():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(("QOSCancel", windll["qwave"]), ((1, 'QOSHandle'),(1, 'Overlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TcRegisterClient():
    try:
        return WINFUNCTYPE(UInt32,UInt32,win32more.Foundation.HANDLE,POINTER(win32more.NetworkManagement.QoS.TCI_CLIENT_FUNC_LIST_head),POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("TcRegisterClient", windll["TRAFFIC"]), ((1, 'TciVersion'),(1, 'ClRegCtx'),(1, 'ClientHandlerList'),(1, 'pClientHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TcEnumerateInterfaces():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(UInt32),POINTER(win32more.NetworkManagement.QoS.TC_IFC_DESCRIPTOR_head), use_last_error=False)(("TcEnumerateInterfaces", windll["TRAFFIC"]), ((1, 'ClientHandle'),(1, 'pBufferSize'),(1, 'InterfaceBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TcOpenInterfaceA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("TcOpenInterfaceA", windll["TRAFFIC"]), ((1, 'pInterfaceName'),(1, 'ClientHandle'),(1, 'ClIfcCtx'),(1, 'pIfcHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TcOpenInterfaceW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("TcOpenInterfaceW", windll["TRAFFIC"]), ((1, 'pInterfaceName'),(1, 'ClientHandle'),(1, 'ClIfcCtx'),(1, 'pIfcHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TcOpenInterface():
    return win32more.NetworkManagement.QoS.TcOpenInterfaceW
def _define_TcCloseInterface():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE, use_last_error=False)(("TcCloseInterface", windll["TRAFFIC"]), ((1, 'IfcHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TcQueryInterface():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(Guid),win32more.Foundation.BOOLEAN,POINTER(UInt32),c_void_p, use_last_error=False)(("TcQueryInterface", windll["TRAFFIC"]), ((1, 'IfcHandle'),(1, 'pGuidParam'),(1, 'NotifyChange'),(1, 'pBufferSize'),(1, 'Buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TcSetInterface():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(Guid),UInt32,c_void_p, use_last_error=False)(("TcSetInterface", windll["TRAFFIC"]), ((1, 'IfcHandle'),(1, 'pGuidParam'),(1, 'BufferSize'),(1, 'Buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TcQueryFlowA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,POINTER(Guid),POINTER(UInt32),c_void_p, use_last_error=False)(("TcQueryFlowA", windll["TRAFFIC"]), ((1, 'pFlowName'),(1, 'pGuidParam'),(1, 'pBufferSize'),(1, 'Buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TcQueryFlowW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(Guid),POINTER(UInt32),c_void_p, use_last_error=False)(("TcQueryFlowW", windll["TRAFFIC"]), ((1, 'pFlowName'),(1, 'pGuidParam'),(1, 'pBufferSize'),(1, 'Buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TcQueryFlow():
    return win32more.NetworkManagement.QoS.TcQueryFlowW
def _define_TcSetFlowA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,POINTER(Guid),UInt32,c_void_p, use_last_error=False)(("TcSetFlowA", windll["TRAFFIC"]), ((1, 'pFlowName'),(1, 'pGuidParam'),(1, 'BufferSize'),(1, 'Buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TcSetFlowW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(Guid),UInt32,c_void_p, use_last_error=False)(("TcSetFlowW", windll["TRAFFIC"]), ((1, 'pFlowName'),(1, 'pGuidParam'),(1, 'BufferSize'),(1, 'Buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TcSetFlow():
    return win32more.NetworkManagement.QoS.TcSetFlowW
def _define_TcAddFlow():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,UInt32,POINTER(win32more.NetworkManagement.QoS.TC_GEN_FLOW_head),POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("TcAddFlow", windll["TRAFFIC"]), ((1, 'IfcHandle'),(1, 'ClFlowCtx'),(1, 'Flags'),(1, 'pGenericFlow'),(1, 'pFlowHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TcGetFlowNameA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt32,POINTER(Byte), use_last_error=False)(("TcGetFlowNameA", windll["TRAFFIC"]), ((1, 'FlowHandle'),(1, 'StrSize'),(1, 'pFlowName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TcGetFlowNameW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt32,POINTER(Char), use_last_error=False)(("TcGetFlowNameW", windll["TRAFFIC"]), ((1, 'FlowHandle'),(1, 'StrSize'),(1, 'pFlowName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TcGetFlowName():
    return win32more.NetworkManagement.QoS.TcGetFlowNameW
def _define_TcModifyFlow():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(win32more.NetworkManagement.QoS.TC_GEN_FLOW_head), use_last_error=False)(("TcModifyFlow", windll["TRAFFIC"]), ((1, 'FlowHandle'),(1, 'pGenericFlow'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TcAddFilter():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(win32more.NetworkManagement.QoS.TC_GEN_FILTER_head),POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("TcAddFilter", windll["TRAFFIC"]), ((1, 'FlowHandle'),(1, 'pGenericFilter'),(1, 'pFilterHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TcDeregisterClient():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE, use_last_error=False)(("TcDeregisterClient", windll["TRAFFIC"]), ((1, 'ClientHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TcDeleteFlow():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE, use_last_error=False)(("TcDeleteFlow", windll["TRAFFIC"]), ((1, 'FlowHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TcDeleteFilter():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE, use_last_error=False)(("TcDeleteFilter", windll["TRAFFIC"]), ((1, 'FilterHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TcEnumerateFlows():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.HANDLE),POINTER(UInt32),POINTER(UInt32),POINTER(win32more.NetworkManagement.QoS.ENUMERATION_BUFFER_head), use_last_error=False)(("TcEnumerateFlows", windll["TRAFFIC"]), ((1, 'IfcHandle'),(1, 'pEnumHandle'),(1, 'pFlowCount'),(1, 'pBufSize'),(1, 'Buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "QOS_MAX_OBJECT_STRING_LENGTH",
    "QOS_TRAFFIC_GENERAL_ID_BASE",
    "SERVICETYPE_NOTRAFFIC",
    "SERVICETYPE_BESTEFFORT",
    "SERVICETYPE_CONTROLLEDLOAD",
    "SERVICETYPE_GUARANTEED",
    "SERVICETYPE_NETWORK_UNAVAILABLE",
    "SERVICETYPE_GENERAL_INFORMATION",
    "SERVICETYPE_NOCHANGE",
    "SERVICETYPE_NONCONFORMING",
    "SERVICETYPE_NETWORK_CONTROL",
    "SERVICETYPE_QUALITATIVE",
    "SERVICE_BESTEFFORT",
    "SERVICE_CONTROLLEDLOAD",
    "SERVICE_GUARANTEED",
    "SERVICE_QUALITATIVE",
    "SERVICE_NO_TRAFFIC_CONTROL",
    "SERVICE_NO_QOS_SIGNALING",
    "QOS_NOT_SPECIFIED",
    "POSITIVE_INFINITY_RATE",
    "QOS_GENERAL_ID_BASE",
    "TC_NONCONF_BORROW",
    "TC_NONCONF_SHAPE",
    "TC_NONCONF_DISCARD",
    "TC_NONCONF_BORROW_PLUS",
    "SESSFLG_E_Police",
    "Opt_Share_mask",
    "Opt_Distinct",
    "Opt_Shared",
    "Opt_SndSel_mask",
    "Opt_Wildcard",
    "Opt_Explicit",
    "ERROR_SPECF_InPlace",
    "ERROR_SPECF_NotGuilty",
    "ERR_FORWARD_OK",
    "ERR_Usage_globl",
    "ERR_Usage_local",
    "ERR_Usage_serv",
    "ERR_global_mask",
    "GENERAL_INFO",
    "GUARANTEED_SERV",
    "PREDICTIVE_SERV",
    "CONTROLLED_DELAY_SERV",
    "CONTROLLED_LOAD_SERV",
    "QUALITATIVE_SERV",
    "INTSERV_VERS_MASK",
    "INTSERV_VERSION0",
    "ISSH_BREAK_BIT",
    "ISPH_FLG_INV",
    "RSVP_PATH",
    "RSVP_RESV",
    "RSVP_PATH_ERR",
    "RSVP_RESV_ERR",
    "RSVP_PATH_TEAR",
    "RSVP_RESV_TEAR",
    "RSVP_Err_NONE",
    "RSVP_Erv_Nonev",
    "RSVP_Err_ADMISSION",
    "RSVP_Erv_Other",
    "RSVP_Erv_DelayBnd",
    "RSVP_Erv_Bandwidth",
    "RSVP_Erv_MTU",
    "RSVP_Erv_Flow_Rate",
    "RSVP_Erv_Bucket_szie",
    "RSVP_Erv_Peak_Rate",
    "RSVP_Erv_Min_Policied_size",
    "RSVP_Err_POLICY",
    "POLICY_ERRV_NO_MORE_INFO",
    "POLICY_ERRV_UNSUPPORTED_CREDENTIAL_TYPE",
    "POLICY_ERRV_INSUFFICIENT_PRIVILEGES",
    "POLICY_ERRV_EXPIRED_CREDENTIALS",
    "POLICY_ERRV_IDENTITY_CHANGED",
    "POLICY_ERRV_UNKNOWN",
    "POLICY_ERRV_GLOBAL_DEF_FLOW_COUNT",
    "POLICY_ERRV_GLOBAL_GRP_FLOW_COUNT",
    "POLICY_ERRV_GLOBAL_USER_FLOW_COUNT",
    "POLICY_ERRV_GLOBAL_UNAUTH_USER_FLOW_COUNT",
    "POLICY_ERRV_SUBNET_DEF_FLOW_COUNT",
    "POLICY_ERRV_SUBNET_GRP_FLOW_COUNT",
    "POLICY_ERRV_SUBNET_USER_FLOW_COUNT",
    "POLICY_ERRV_SUBNET_UNAUTH_USER_FLOW_COUNT",
    "POLICY_ERRV_GLOBAL_DEF_FLOW_DURATION",
    "POLICY_ERRV_GLOBAL_GRP_FLOW_DURATION",
    "POLICY_ERRV_GLOBAL_USER_FLOW_DURATION",
    "POLICY_ERRV_GLOBAL_UNAUTH_USER_FLOW_DURATION",
    "POLICY_ERRV_SUBNET_DEF_FLOW_DURATION",
    "POLICY_ERRV_SUBNET_GRP_FLOW_DURATION",
    "POLICY_ERRV_SUBNET_USER_FLOW_DURATION",
    "POLICY_ERRV_SUBNET_UNAUTH_USER_FLOW_DURATION",
    "POLICY_ERRV_GLOBAL_DEF_FLOW_RATE",
    "POLICY_ERRV_GLOBAL_GRP_FLOW_RATE",
    "POLICY_ERRV_GLOBAL_USER_FLOW_RATE",
    "POLICY_ERRV_GLOBAL_UNAUTH_USER_FLOW_RATE",
    "POLICY_ERRV_SUBNET_DEF_FLOW_RATE",
    "POLICY_ERRV_SUBNET_GRP_FLOW_RATE",
    "POLICY_ERRV_SUBNET_USER_FLOW_RATE",
    "POLICY_ERRV_SUBNET_UNAUTH_USER_FLOW_RATE",
    "POLICY_ERRV_GLOBAL_DEF_PEAK_RATE",
    "POLICY_ERRV_GLOBAL_GRP_PEAK_RATE",
    "POLICY_ERRV_GLOBAL_USER_PEAK_RATE",
    "POLICY_ERRV_GLOBAL_UNAUTH_USER_PEAK_RATE",
    "POLICY_ERRV_SUBNET_DEF_PEAK_RATE",
    "POLICY_ERRV_SUBNET_GRP_PEAK_RATE",
    "POLICY_ERRV_SUBNET_USER_PEAK_RATE",
    "POLICY_ERRV_SUBNET_UNAUTH_USER_PEAK_RATE",
    "POLICY_ERRV_GLOBAL_DEF_SUM_FLOW_RATE",
    "POLICY_ERRV_GLOBAL_GRP_SUM_FLOW_RATE",
    "POLICY_ERRV_GLOBAL_USER_SUM_FLOW_RATE",
    "POLICY_ERRV_GLOBAL_UNAUTH_USER_SUM_FLOW_RATE",
    "POLICY_ERRV_SUBNET_DEF_SUM_FLOW_RATE",
    "POLICY_ERRV_SUBNET_GRP_SUM_FLOW_RATE",
    "POLICY_ERRV_SUBNET_USER_SUM_FLOW_RATE",
    "POLICY_ERRV_SUBNET_UNAUTH_USER_SUM_FLOW_RATE",
    "POLICY_ERRV_GLOBAL_DEF_SUM_PEAK_RATE",
    "POLICY_ERRV_GLOBAL_GRP_SUM_PEAK_RATE",
    "POLICY_ERRV_GLOBAL_USER_SUM_PEAK_RATE",
    "POLICY_ERRV_GLOBAL_UNAUTH_USER_SUM_PEAK_RATE",
    "POLICY_ERRV_SUBNET_DEF_SUM_PEAK_RATE",
    "POLICY_ERRV_SUBNET_GRP_SUM_PEAK_RATE",
    "POLICY_ERRV_SUBNET_USER_SUM_PEAK_RATE",
    "POLICY_ERRV_SUBNET_UNAUTH_USER_SUM_PEAK_RATE",
    "POLICY_ERRV_UNKNOWN_USER",
    "POLICY_ERRV_NO_PRIVILEGES",
    "POLICY_ERRV_EXPIRED_USER_TOKEN",
    "POLICY_ERRV_NO_RESOURCES",
    "POLICY_ERRV_PRE_EMPTED",
    "POLICY_ERRV_USER_CHANGED",
    "POLICY_ERRV_NO_ACCEPTS",
    "POLICY_ERRV_NO_MEMORY",
    "POLICY_ERRV_CRAZY_FLOWSPEC",
    "RSVP_Err_NO_PATH",
    "RSVP_Err_NO_SENDER",
    "RSVP_Err_BAD_STYLE",
    "RSVP_Err_UNKNOWN_STYLE",
    "RSVP_Err_BAD_DSTPORT",
    "RSVP_Err_BAD_SNDPORT",
    "RSVP_Err_AMBIG_FILTER",
    "RSVP_Err_PREEMPTED",
    "RSVP_Err_UNKN_OBJ_CLASS",
    "RSVP_Err_UNKNOWN_CTYPE",
    "RSVP_Err_API_ERROR",
    "RSVP_Err_TC_ERROR",
    "RSVP_Erv_Conflict_Serv",
    "RSVP_Erv_No_Serv",
    "RSVP_Erv_Crazy_Flowspec",
    "RSVP_Erv_Crazy_Tspec",
    "RSVP_Err_TC_SYS_ERROR",
    "RSVP_Err_RSVP_SYS_ERROR",
    "RSVP_Erv_MEMORY",
    "RSVP_Erv_API",
    "LPM_PE_USER_IDENTITY",
    "LPM_PE_APP_IDENTITY",
    "ERROR_NO_MORE_INFO",
    "UNSUPPORTED_CREDENTIAL_TYPE",
    "INSUFFICIENT_PRIVILEGES",
    "EXPIRED_CREDENTIAL",
    "IDENTITY_CHANGED",
    "LPM_OK",
    "INV_LPM_HANDLE",
    "LPM_TIME_OUT",
    "INV_REQ_HANDLE",
    "DUP_RESULTS",
    "INV_RESULTS",
    "LPM_PE_ALL_TYPES",
    "LPM_API_VERSION_1",
    "PCM_VERSION_1",
    "LPV_RESERVED",
    "LPV_MIN_PRIORITY",
    "LPV_MAX_PRIORITY",
    "LPV_DROP_MSG",
    "LPV_DONT_CARE",
    "LPV_REJECT",
    "FORCE_IMMEDIATE_REFRESH",
    "LPM_RESULT_READY",
    "LPM_RESULT_DEFER",
    "RCVD_PATH_TEAR",
    "RCVD_RESV_TEAR",
    "ADM_CTRL_FAILED",
    "STATE_TIMEOUT",
    "FLOW_DURATION",
    "RESOURCES_ALLOCATED",
    "RESOURCES_MODIFIED",
    "CURRENT_TCI_VERSION",
    "TC_NOTIFY_IFC_UP",
    "TC_NOTIFY_IFC_CLOSE",
    "TC_NOTIFY_IFC_CHANGE",
    "TC_NOTIFY_PARAM_CHANGED",
    "TC_NOTIFY_FLOW_CLOSE",
    "MAX_STRING_LENGTH",
    "QOS_OUTGOING_DEFAULT_MINIMUM_BANDWIDTH",
    "QOS_QUERYFLOW_FRESH",
    "QOS_NON_ADAPTIVE_FLOW",
    "RSVP_OBJECT_ID_BASE",
    "RSVP_DEFAULT_STYLE",
    "RSVP_WILDCARD_STYLE",
    "RSVP_FIXED_FILTER_STYLE",
    "RSVP_SHARED_EXPLICIT_STYLE",
    "AD_FLAG_BREAK_BIT",
    "QOSSPBASE",
    "ALLOWED_TO_SEND_DATA",
    "ABLE_TO_RECV_RSVP",
    "LINE_RATE",
    "LOCAL_TRAFFIC_CONTROL",
    "LOCAL_QOSABILITY",
    "END_TO_END_QOSABILITY",
    "INFO_NOT_AVAILABLE",
    "ANY_DEST_ADDR",
    "MODERATELY_DELAY_SENSITIVE",
    "HIGHLY_DELAY_SENSITIVE",
    "QOSSP_ERR_BASE",
    "GQOS_NO_ERRORCODE",
    "GQOS_NO_ERRORVALUE",
    "GQOS_ERRORCODE_UNKNOWN",
    "GQOS_ERRORVALUE_UNKNOWN",
    "GQOS_NET_ADMISSION",
    "GQOS_NET_POLICY",
    "GQOS_RSVP",
    "GQOS_API",
    "GQOS_KERNEL_TC_SYS",
    "GQOS_RSVP_SYS",
    "GQOS_KERNEL_TC",
    "PE_TYPE_APPID",
    "PE_ATTRIB_TYPE_POLICY_LOCATOR",
    "POLICY_LOCATOR_SUB_TYPE_ASCII_DN",
    "POLICY_LOCATOR_SUB_TYPE_UNICODE_DN",
    "POLICY_LOCATOR_SUB_TYPE_ASCII_DN_ENC",
    "POLICY_LOCATOR_SUB_TYPE_UNICODE_DN_ENC",
    "PE_ATTRIB_TYPE_CREDENTIAL",
    "CREDENTIAL_SUB_TYPE_ASCII_ID",
    "CREDENTIAL_SUB_TYPE_UNICODE_ID",
    "CREDENTIAL_SUB_TYPE_KERBEROS_TKT",
    "CREDENTIAL_SUB_TYPE_X509_V3_CERT",
    "CREDENTIAL_SUB_TYPE_PGP_CERT",
    "TCBASE",
    "ERROR_INCOMPATIBLE_TCI_VERSION",
    "ERROR_INVALID_SERVICE_TYPE",
    "ERROR_INVALID_TOKEN_RATE",
    "ERROR_INVALID_PEAK_RATE",
    "ERROR_INVALID_SD_MODE",
    "ERROR_INVALID_QOS_PRIORITY",
    "ERROR_INVALID_TRAFFIC_CLASS",
    "ERROR_INVALID_ADDRESS_TYPE",
    "ERROR_DUPLICATE_FILTER",
    "ERROR_FILTER_CONFLICT",
    "ERROR_ADDRESS_TYPE_NOT_SUPPORTED",
    "ERROR_TC_SUPPORTED_OBJECTS_EXIST",
    "ERROR_INCOMPATABLE_QOS",
    "ERROR_TC_NOT_SUPPORTED",
    "ERROR_TC_OBJECT_LENGTH_INVALID",
    "ERROR_INVALID_FLOW_MODE",
    "ERROR_INVALID_DIFFSERV_FLOW",
    "ERROR_DS_MAPPING_EXISTS",
    "ERROR_INVALID_SHAPE_RATE",
    "ERROR_INVALID_DS_CLASS",
    "ERROR_TOO_MANY_CLIENTS",
    "GUID_QOS_REMAINING_BANDWIDTH",
    "GUID_QOS_BESTEFFORT_BANDWIDTH",
    "GUID_QOS_LATENCY",
    "GUID_QOS_FLOW_COUNT",
    "GUID_QOS_NON_BESTEFFORT_LIMIT",
    "GUID_QOS_MAX_OUTSTANDING_SENDS",
    "GUID_QOS_STATISTICS_BUFFER",
    "GUID_QOS_FLOW_MODE",
    "GUID_QOS_ISSLOW_FLOW",
    "GUID_QOS_TIMER_RESOLUTION",
    "GUID_QOS_FLOW_IP_CONFORMING",
    "GUID_QOS_FLOW_IP_NONCONFORMING",
    "GUID_QOS_FLOW_8021P_CONFORMING",
    "GUID_QOS_FLOW_8021P_NONCONFORMING",
    "GUID_QOS_ENABLE_AVG_STATS",
    "GUID_QOS_ENABLE_WINDOW_ADJUSTMENT",
    "FSCTL_TCP_BASE",
    "IF_MIB_STATS_ID",
    "IP_MIB_STATS_ID",
    "IP_MIB_ADDRTABLE_ENTRY_ID",
    "IP_INTFC_INFO_ID",
    "MAX_PHYSADDR_SIZE",
    "SIPAEV_PREBOOT_CERT",
    "SIPAEV_POST_CODE",
    "SIPAEV_UNUSED",
    "SIPAEV_NO_ACTION",
    "SIPAEV_SEPARATOR",
    "SIPAEV_ACTION",
    "SIPAEV_EVENT_TAG",
    "SIPAEV_S_CRTM_CONTENTS",
    "SIPAEV_S_CRTM_VERSION",
    "SIPAEV_CPU_MICROCODE",
    "SIPAEV_PLATFORM_CONFIG_FLAGS",
    "SIPAEV_TABLE_OF_DEVICES",
    "SIPAEV_COMPACT_HASH",
    "SIPAEV_IPL",
    "SIPAEV_IPL_PARTITION_DATA",
    "SIPAEV_NONHOST_CODE",
    "SIPAEV_NONHOST_CONFIG",
    "SIPAEV_NONHOST_INFO",
    "SIPAEV_OMIT_BOOT_DEVICE_EVENTS",
    "SIPAEV_EFI_EVENT_BASE",
    "SIPAEV_EFI_VARIABLE_DRIVER_CONFIG",
    "SIPAEV_EFI_VARIABLE_BOOT",
    "SIPAEV_EFI_BOOT_SERVICES_APPLICATION",
    "SIPAEV_EFI_BOOT_SERVICES_DRIVER",
    "SIPAEV_EFI_RUNTIME_SERVICES_DRIVER",
    "SIPAEV_EFI_GPT_EVENT",
    "SIPAEV_EFI_ACTION",
    "SIPAEV_EFI_PLATFORM_FIRMWARE_BLOB",
    "SIPAEV_EFI_HANDOFF_TABLES",
    "SIPAEV_EFI_PLATFORM_FIRMWARE_BLOB2",
    "SIPAEV_EFI_HANDOFF_TABLES2",
    "SIPAEV_EFI_HCRTM_EVENT",
    "SIPAEV_EFI_VARIABLE_AUTHORITY",
    "SIPAEV_EFI_SPDM_FIRMWARE_BLOB",
    "SIPAEV_EFI_SPDM_FIRMWARE_CONFIG",
    "SIPAEV_TXT_EVENT_BASE",
    "SIPAEV_TXT_PCR_MAPPING",
    "SIPAEV_TXT_HASH_START",
    "SIPAEV_TXT_COMBINED_HASH",
    "SIPAEV_TXT_MLE_HASH",
    "SIPAEV_TXT_BIOSAC_REG_DATA",
    "SIPAEV_TXT_CPU_SCRTM_STAT",
    "SIPAEV_TXT_LCP_CONTROL_HASH",
    "SIPAEV_TXT_ELEMENTS_HASH",
    "SIPAEV_TXT_STM_HASH",
    "SIPAEV_TXT_OSSINITDATA_CAP_HASH",
    "SIPAEV_TXT_SINIT_PUBKEY_HASH",
    "SIPAEV_TXT_LCP_HASH",
    "SIPAEV_TXT_LCP_DETAILS_HASH",
    "SIPAEV_TXT_LCP_AUTHORITIES_HASH",
    "SIPAEV_TXT_NV_INFO_HASH",
    "SIPAEV_TXT_COLD_BOOT_BIOS_HASH",
    "SIPAEV_TXT_KM_HASH",
    "SIPAEV_TXT_BPM_HASH",
    "SIPAEV_TXT_KM_INFO_HASH",
    "SIPAEV_TXT_BPM_INFO_HASH",
    "SIPAEV_TXT_BOOT_POL_HASH",
    "SIPAEV_TXT_RANDOM_VALUE",
    "SIPAEV_TXT_CAP_VALUE",
    "SIPAEV_AMD_SL_EVENT_BASE",
    "SIPAEV_AMD_SL_LOAD",
    "SIPAEV_AMD_SL_PSP_FW_SPLT",
    "SIPAEV_AMD_SL_TSME_RB_FUSE",
    "SIPAEV_AMD_SL_PUB_KEY",
    "SIPAEV_AMD_SL_SVN",
    "SIPAEV_AMD_SL_LOAD_1",
    "SIPAEV_AMD_SL_SEPARATOR",
    "SIPAEVENTTYPE_NONMEASURED",
    "SIPAEVENTTYPE_AGGREGATION",
    "SIPAEVENTTYPE_CONTAINER",
    "SIPAEVENTTYPE_INFORMATION",
    "SIPAEVENTTYPE_ERROR",
    "SIPAEVENTTYPE_PREOSPARAMETER",
    "SIPAEVENTTYPE_OSPARAMETER",
    "SIPAEVENTTYPE_AUTHORITY",
    "SIPAEVENTTYPE_LOADEDMODULE",
    "SIPAEVENTTYPE_TRUSTPOINT",
    "SIPAEVENTTYPE_ELAM",
    "SIPAEVENTTYPE_VBS",
    "SIPAEVENTTYPE_KSR",
    "SIPAEVENTTYPE_DRTM",
    "SIPAERROR_FIRMWAREFAILURE",
    "SIPAERROR_INTERNALFAILURE",
    "SIPAEVENT_INFORMATION",
    "SIPAEVENT_BOOTCOUNTER",
    "SIPAEVENT_TRANSFER_CONTROL",
    "SIPAEVENT_APPLICATION_RETURN",
    "SIPAEVENT_BITLOCKER_UNLOCK",
    "SIPAEVENT_EVENTCOUNTER",
    "SIPAEVENT_COUNTERID",
    "SIPAEVENT_MORBIT_NOT_CANCELABLE",
    "SIPAEVENT_APPLICATION_SVN",
    "SIPAEVENT_SVN_CHAIN_STATUS",
    "SIPAEVENT_MORBIT_API_STATUS",
    "SIPAEVENT_BOOTDEBUGGING",
    "SIPAEVENT_BOOT_REVOCATION_LIST",
    "SIPAEVENT_OSKERNELDEBUG",
    "SIPAEVENT_CODEINTEGRITY",
    "SIPAEVENT_TESTSIGNING",
    "SIPAEVENT_DATAEXECUTIONPREVENTION",
    "SIPAEVENT_SAFEMODE",
    "SIPAEVENT_WINPE",
    "SIPAEVENT_PHYSICALADDRESSEXTENSION",
    "SIPAEVENT_OSDEVICE",
    "SIPAEVENT_SYSTEMROOT",
    "SIPAEVENT_HYPERVISOR_LAUNCH_TYPE",
    "SIPAEVENT_HYPERVISOR_PATH",
    "SIPAEVENT_HYPERVISOR_IOMMU_POLICY",
    "SIPAEVENT_HYPERVISOR_DEBUG",
    "SIPAEVENT_DRIVER_LOAD_POLICY",
    "SIPAEVENT_SI_POLICY",
    "SIPAEVENT_HYPERVISOR_MMIO_NX_POLICY",
    "SIPAEVENT_HYPERVISOR_MSR_FILTER_POLICY",
    "SIPAEVENT_VSM_LAUNCH_TYPE",
    "SIPAEVENT_OS_REVOCATION_LIST",
    "SIPAEVENT_SMT_STATUS",
    "SIPAEVENT_VSM_IDK_INFO",
    "SIPAEVENT_FLIGHTSIGNING",
    "SIPAEVENT_PAGEFILE_ENCRYPTION_ENABLED",
    "SIPAEVENT_VSM_IDKS_INFO",
    "SIPAEVENT_HIBERNATION_DISABLED",
    "SIPAEVENT_DUMPS_DISABLED",
    "SIPAEVENT_DUMP_ENCRYPTION_ENABLED",
    "SIPAEVENT_DUMP_ENCRYPTION_KEY_DIGEST",
    "SIPAEVENT_LSAISO_CONFIG",
    "SIPAEVENT_SBCP_INFO",
    "SIPAEVENT_HYPERVISOR_BOOT_DMA_PROTECTION",
    "SIPAEVENT_NOAUTHORITY",
    "SIPAEVENT_AUTHORITYPUBKEY",
    "SIPAEVENT_FILEPATH",
    "SIPAEVENT_IMAGESIZE",
    "SIPAEVENT_HASHALGORITHMID",
    "SIPAEVENT_AUTHENTICODEHASH",
    "SIPAEVENT_AUTHORITYISSUER",
    "SIPAEVENT_AUTHORITYSERIAL",
    "SIPAEVENT_IMAGEBASE",
    "SIPAEVENT_AUTHORITYPUBLISHER",
    "SIPAEVENT_AUTHORITYSHA1THUMBPRINT",
    "SIPAEVENT_IMAGEVALIDATED",
    "SIPAEVENT_MODULE_SVN",
    "SIPAEVENT_ELAM_KEYNAME",
    "SIPAEVENT_ELAM_CONFIGURATION",
    "SIPAEVENT_ELAM_POLICY",
    "SIPAEVENT_ELAM_MEASURED",
    "SIPAEVENT_VBS_VSM_REQUIRED",
    "SIPAEVENT_VBS_SECUREBOOT_REQUIRED",
    "SIPAEVENT_VBS_IOMMU_REQUIRED",
    "SIPAEVENT_VBS_MMIO_NX_REQUIRED",
    "SIPAEVENT_VBS_MSR_FILTERING_REQUIRED",
    "SIPAEVENT_VBS_MANDATORY_ENFORCEMENT",
    "SIPAEVENT_VBS_HVCI_POLICY",
    "SIPAEVENT_VBS_MICROSOFT_BOOT_CHAIN_REQUIRED",
    "SIPAEVENT_VBS_DUMP_USES_AMEROOT",
    "SIPAEVENT_VBS_VSM_NOSECRETS_ENFORCED",
    "SIPAEVENT_KSR_SIGNATURE",
    "SIPAEVENT_DRTM_STATE_AUTH",
    "SIPAEVENT_DRTM_SMM_LEVEL",
    "SIPAEVENT_DRTM_AMD_SMM_HASH",
    "SIPAEVENT_DRTM_AMD_SMM_SIGNER_KEY",
    "FVEB_UNLOCK_FLAG_NONE",
    "FVEB_UNLOCK_FLAG_CACHED",
    "FVEB_UNLOCK_FLAG_MEDIA",
    "FVEB_UNLOCK_FLAG_TPM",
    "FVEB_UNLOCK_FLAG_PIN",
    "FVEB_UNLOCK_FLAG_EXTERNAL",
    "FVEB_UNLOCK_FLAG_RECOVERY",
    "FVEB_UNLOCK_FLAG_PASSPHRASE",
    "FVEB_UNLOCK_FLAG_NBP",
    "FVEB_UNLOCK_FLAG_AUK_OSFVEINFO",
    "OSDEVICE_TYPE_UNKNOWN",
    "OSDEVICE_TYPE_BLOCKIO_HARDDISK",
    "OSDEVICE_TYPE_BLOCKIO_REMOVABLEDISK",
    "OSDEVICE_TYPE_BLOCKIO_CDROM",
    "OSDEVICE_TYPE_BLOCKIO_PARTITION",
    "OSDEVICE_TYPE_BLOCKIO_FILE",
    "OSDEVICE_TYPE_BLOCKIO_RAMDISK",
    "OSDEVICE_TYPE_BLOCKIO_VIRTUALHARDDISK",
    "OSDEVICE_TYPE_SERIAL",
    "OSDEVICE_TYPE_UDP",
    "OSDEVICE_TYPE_VMBUS",
    "OSDEVICE_TYPE_COMPOSITE",
    "SIPAHDRSIGNATURE",
    "SIPALOGVERSION",
    "SIPAKSRHDRSIGNATURE",
    "WBCL_DIGEST_ALG_ID_SHA_1",
    "WBCL_DIGEST_ALG_ID_SHA_2_256",
    "WBCL_DIGEST_ALG_ID_SHA_2_384",
    "WBCL_DIGEST_ALG_ID_SHA_2_512",
    "WBCL_DIGEST_ALG_ID_SM3_256",
    "WBCL_DIGEST_ALG_ID_SHA3_256",
    "WBCL_DIGEST_ALG_ID_SHA3_384",
    "WBCL_DIGEST_ALG_ID_SHA3_512",
    "WBCL_DIGEST_ALG_BITMAP_SHA_1",
    "WBCL_DIGEST_ALG_BITMAP_SHA_2_256",
    "WBCL_DIGEST_ALG_BITMAP_SHA_2_384",
    "WBCL_DIGEST_ALG_BITMAP_SHA_2_512",
    "WBCL_DIGEST_ALG_BITMAP_SM3_256",
    "WBCL_DIGEST_ALG_BITMAP_SHA3_256",
    "WBCL_DIGEST_ALG_BITMAP_SHA3_384",
    "WBCL_DIGEST_ALG_BITMAP_SHA3_512",
    "WBCL_HASH_LEN_SHA1",
    "IS_GUAR_RSPEC",
    "GUAR_ADSPARM_C",
    "GUAR_ADSPARM_D",
    "GUAR_ADSPARM_Ctot",
    "GUAR_ADSPARM_Dtot",
    "GUAR_ADSPARM_Csum",
    "GUAR_ADSPARM_Dsum",
    "LPM_HANDLE",
    "RHANDLE",
    "FLOWSPEC",
    "QOS_OBJECT_HDR",
    "QOS_SD_MODE",
    "QOS_SHAPING_RATE",
    "RsvpObjHdr",
    "Session_IPv4",
    "RSVP_SESSION",
    "Rsvp_Hop_IPv4",
    "RSVP_HOP",
    "RESV_STYLE",
    "Filter_Spec_IPv4",
    "Filter_Spec_IPv4GPI",
    "FILTER_SPEC",
    "Scope_list_ipv4",
    "RSVP_SCOPE",
    "Error_Spec_IPv4",
    "ERROR_SPEC",
    "POLICY_DATA",
    "POLICY_ELEMENT",
    "int_serv_wkp",
    "IS_WKP_HOP_CNT",
    "IS_WKP_PATH_BW",
    "IS_WKP_MIN_LATENCY",
    "IS_WKP_COMPOSED_MTU",
    "IS_WKP_TB_TSPEC",
    "IS_WKP_Q_TSPEC",
    "IntServMainHdr",
    "IntServServiceHdr",
    "IntServParmHdr",
    "GenTspecParms",
    "GenTspec",
    "QualTspecParms",
    "QualTspec",
    "QualAppFlowSpec",
    "IntServTspecBody",
    "SENDER_TSPEC",
    "CtrlLoadFlowspec",
    "GuarRspec",
    "GuarFlowSpec",
    "IntServFlowSpec",
    "IS_FLOWSPEC",
    "flow_desc",
    "Gads_parms_t",
    "GenAdspecParams",
    "IS_ADSPEC_BODY",
    "ADSPEC",
    "ID_ERROR_OBJECT",
    "RSVP_MSG_OBJS",
    "PALLOCMEM",
    "PFREEMEM",
    "policy_decision",
    "CBADMITRESULT",
    "CBGETRSVPOBJECTS",
    "LPM_INIT_INFO",
    "lpmiptable",
    "QOS_TRAFFIC_TYPE",
    "QOS_TRAFFIC_TYPE_QOSTrafficTypeBestEffort",
    "QOS_TRAFFIC_TYPE_QOSTrafficTypeBackground",
    "QOS_TRAFFIC_TYPE_QOSTrafficTypeExcellentEffort",
    "QOS_TRAFFIC_TYPE_QOSTrafficTypeAudioVideo",
    "QOS_TRAFFIC_TYPE_QOSTrafficTypeVoice",
    "QOS_TRAFFIC_TYPE_QOSTrafficTypeControl",
    "QOS_SET_FLOW",
    "QOS_SET_FLOW_QOSSetTrafficType",
    "QOS_SET_FLOW_QOSSetOutgoingRate",
    "QOS_SET_FLOW_QOSSetOutgoingDSCPValue",
    "QOS_PACKET_PRIORITY",
    "QOS_FLOW_FUNDAMENTALS",
    "QOS_FLOWRATE_REASON",
    "QOS_FLOWRATE_REASON_QOSFlowRateNotApplicable",
    "QOS_FLOWRATE_REASON_QOSFlowRateContentChange",
    "QOS_FLOWRATE_REASON_QOSFlowRateCongestion",
    "QOS_FLOWRATE_REASON_QOSFlowRateHigherContentEncoding",
    "QOS_FLOWRATE_REASON_QOSFlowRateUserCaused",
    "QOS_SHAPING",
    "QOS_SHAPING_QOSShapeOnly",
    "QOS_SHAPING_QOSShapeAndMark",
    "QOS_SHAPING_QOSUseNonConformantMarkings",
    "QOS_FLOWRATE_OUTGOING",
    "QOS_QUERY_FLOW",
    "QOS_QUERY_FLOW_QOSQueryFlowFundamentals",
    "QOS_QUERY_FLOW_QOSQueryPacketPriority",
    "QOS_QUERY_FLOW_QOSQueryOutgoingRate",
    "QOS_NOTIFY_FLOW",
    "QOS_NOTIFY_FLOW_QOSNotifyCongested",
    "QOS_NOTIFY_FLOW_QOSNotifyUncongested",
    "QOS_NOTIFY_FLOW_QOSNotifyAvailable",
    "QOS_VERSION",
    "QOS_FRIENDLY_NAME",
    "QOS_TRAFFIC_CLASS",
    "QOS_DS_CLASS",
    "QOS_DIFFSERV",
    "QOS_DIFFSERV_RULE",
    "QOS_TCP_TRAFFIC",
    "TCI_NOTIFY_HANDLER",
    "TCI_ADD_FLOW_COMPLETE_HANDLER",
    "TCI_MOD_FLOW_COMPLETE_HANDLER",
    "TCI_DEL_FLOW_COMPLETE_HANDLER",
    "TCI_CLIENT_FUNC_LIST",
    "ADDRESS_LIST_DESCRIPTOR",
    "TC_IFC_DESCRIPTOR",
    "TC_SUPPORTED_INFO_BUFFER",
    "TC_GEN_FILTER",
    "TC_GEN_FLOW",
    "IP_PATTERN",
    "IPX_PATTERN",
    "ENUMERATION_BUFFER",
    "IN_ADDR_IPV4",
    "IN_ADDR_IPV6",
    "RSVP_FILTERSPEC_V4",
    "RSVP_FILTERSPEC_V6",
    "RSVP_FILTERSPEC_V6_FLOW",
    "RSVP_FILTERSPEC_V4_GPI",
    "RSVP_FILTERSPEC_V6_GPI",
    "FilterType",
    "FILTERSPECV4",
    "FILTERSPECV6",
    "FILTERSPECV6_FLOW",
    "FILTERSPECV4_GPI",
    "FILTERSPECV6_GPI",
    "FILTERSPEC_END",
    "RSVP_FILTERSPEC",
    "FLOWDESCRIPTOR",
    "RSVP_POLICY",
    "RSVP_POLICY_INFO",
    "RSVP_RESERVE_INFO",
    "RSVP_STATUS_INFO",
    "QOS_DESTADDR",
    "AD_GENERAL_PARAMS",
    "AD_GUARANTEED",
    "PARAM_BUFFER",
    "CONTROL_SERVICE",
    "RSVP_ADSPEC",
    "IDPE_ATTR",
    "WBCL_Iterator",
    "TCG_PCClientPCREventStruct",
    "TCG_PCClientTaggedEventStruct",
    "WBCL_LogHdr",
    "tag_SIPAEVENT_VSM_IDK_RSA_INFO",
    "tag_SIPAEVENT_VSM_IDK_INFO_PAYLOAD",
    "tag_SIPAEVENT_SI_POLICY_PAYLOAD",
    "tag_SIPAEVENT_REVOCATION_LIST_PAYLOAD",
    "tag_SIPAEVENT_KSR_SIGNATURE_PAYLOAD",
    "tag_SIPAEVENT_SBCP_INFO_PAYLOAD_V1",
    "QOS",
    "QOSCreateHandle",
    "QOSCloseHandle",
    "QOSStartTrackingClient",
    "QOSStopTrackingClient",
    "QOSEnumerateFlows",
    "QOSAddSocketToFlow",
    "QOSRemoveSocketFromFlow",
    "QOSSetFlow",
    "QOSQueryFlow",
    "QOSNotifyFlow",
    "QOSCancel",
    "TcRegisterClient",
    "TcEnumerateInterfaces",
    "TcOpenInterfaceA",
    "TcOpenInterfaceW",
    "TcOpenInterface",
    "TcCloseInterface",
    "TcQueryInterface",
    "TcSetInterface",
    "TcQueryFlowA",
    "TcQueryFlowW",
    "TcQueryFlow",
    "TcSetFlowA",
    "TcSetFlowW",
    "TcSetFlow",
    "TcAddFlow",
    "TcGetFlowNameA",
    "TcGetFlowNameW",
    "TcGetFlowName",
    "TcModifyFlow",
    "TcAddFilter",
    "TcDeregisterClient",
    "TcDeleteFlow",
    "TcDeleteFilter",
    "TcEnumerateFlows",
]
