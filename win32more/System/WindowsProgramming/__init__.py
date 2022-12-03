from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Graphics.Gdi
import win32more.Security
import win32more.System.Com
import win32more.System.Kernel
import win32more.System.Ole
import win32more.System.Registry
import win32more.System.WindowsProgramming
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f'_define_{name}']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
def _define__D3DHAL_CALLBACKS_head():
    class _D3DHAL_CALLBACKS(Structure):
        pass
    return _D3DHAL_CALLBACKS
def _define__D3DHAL_CALLBACKS():
    _D3DHAL_CALLBACKS = win32more.System.WindowsProgramming._D3DHAL_CALLBACKS_head
    return _D3DHAL_CALLBACKS
def _define__D3DHAL_GLOBALDRIVERDATA_head():
    class _D3DHAL_GLOBALDRIVERDATA(Structure):
        pass
    return _D3DHAL_GLOBALDRIVERDATA
def _define__D3DHAL_GLOBALDRIVERDATA():
    _D3DHAL_GLOBALDRIVERDATA = win32more.System.WindowsProgramming._D3DHAL_GLOBALDRIVERDATA_head
    return _D3DHAL_GLOBALDRIVERDATA
def _define_ACTCTX_SECTION_KEYED_DATA_2600_head():
    class ACTCTX_SECTION_KEYED_DATA_2600(Structure):
        pass
    return ACTCTX_SECTION_KEYED_DATA_2600
def _define_ACTCTX_SECTION_KEYED_DATA_2600():
    ACTCTX_SECTION_KEYED_DATA_2600 = win32more.System.WindowsProgramming.ACTCTX_SECTION_KEYED_DATA_2600_head
    ACTCTX_SECTION_KEYED_DATA_2600._fields_ = [
        ('cbSize', UInt32),
        ('ulDataFormatVersion', UInt32),
        ('lpData', c_void_p),
        ('ulLength', UInt32),
        ('lpSectionGlobalData', c_void_p),
        ('ulSectionGlobalDataLength', UInt32),
        ('lpSectionBase', c_void_p),
        ('ulSectionTotalLength', UInt32),
        ('hActCtx', win32more.Foundation.HANDLE),
        ('ulAssemblyRosterIndex', UInt32),
    ]
    return ACTCTX_SECTION_KEYED_DATA_2600
def _define_ACTCTX_SECTION_KEYED_DATA_ASSEMBLY_METADATA_head():
    class ACTCTX_SECTION_KEYED_DATA_ASSEMBLY_METADATA(Structure):
        pass
    return ACTCTX_SECTION_KEYED_DATA_ASSEMBLY_METADATA
def _define_ACTCTX_SECTION_KEYED_DATA_ASSEMBLY_METADATA():
    ACTCTX_SECTION_KEYED_DATA_ASSEMBLY_METADATA = win32more.System.WindowsProgramming.ACTCTX_SECTION_KEYED_DATA_ASSEMBLY_METADATA_head
    ACTCTX_SECTION_KEYED_DATA_ASSEMBLY_METADATA._fields_ = [
        ('lpInformation', c_void_p),
        ('lpSectionBase', c_void_p),
        ('ulSectionLength', UInt32),
        ('lpSectionGlobalDataBase', c_void_p),
        ('ulSectionGlobalDataLength', UInt32),
    ]
    return ACTCTX_SECTION_KEYED_DATA_ASSEMBLY_METADATA
def _define_ACTIVATION_CONTEXT_BASIC_INFORMATION_head():
    class ACTIVATION_CONTEXT_BASIC_INFORMATION(Structure):
        pass
    return ACTIVATION_CONTEXT_BASIC_INFORMATION
def _define_ACTIVATION_CONTEXT_BASIC_INFORMATION():
    ACTIVATION_CONTEXT_BASIC_INFORMATION = win32more.System.WindowsProgramming.ACTIVATION_CONTEXT_BASIC_INFORMATION_head
    ACTIVATION_CONTEXT_BASIC_INFORMATION._fields_ = [
        ('hActCtx', win32more.Foundation.HANDLE),
        ('dwFlags', UInt32),
    ]
    return ACTIVATION_CONTEXT_BASIC_INFORMATION
WLDP_DLL = 'WLDP.DLL'
WLDP_GETLOCKDOWNPOLICY_FN = 'WldpGetLockdownPolicy'
WLDP_ISCLASSINAPPROVEDLIST_FN = 'WldpIsClassInApprovedList'
WLDP_SETDYNAMICCODETRUST_FN = 'WldpSetDynamicCodeTrust'
WLDP_ISDYNAMICCODEPOLICYENABLED_FN = 'WldpIsDynamicCodePolicyEnabled'
WLDP_QUERYDANAMICCODETRUST_FN = 'WldpQueryDynamicCodeTrust'
WLDP_QUERYDYNAMICCODETRUST_FN = 'WldpQueryDynamicCodeTrust'
WLDP_QUERYWINDOWSLOCKDOWNMODE_FN = 'WldpQueryWindowsLockdownMode'
WLDP_SETWINDOWSLOCKDOWNRESTRICTION_FN = 'WldpSetWindowsLockdownRestriction'
WLDP_QUERYDEVICESECURITYINFORMATION_FN = 'WldpQueryDeviceSecurityInformation'
WLDP_QUERYWINDOWSLOCKDOWNRESTRICTION_FN = 'WldpQueryWindowsLockdownRestriction'
WLDP_ISAPPAPPROVEDBYPOLICY_FN = 'WldpIsAppApprovedByPolicy'
WLDP_QUERYPOLICYSETTINGENABLED_FN = 'WldpQueryPolicySettingEnabled'
WLDP_QUERYPOLICYSETTINGENABLED2_FN = 'WldpQueryPolicySettingEnabled2'
WLDP_ISWCOSPRODUCTIONCONFIGURATION_FN = 'WldpIsWcosProductionConfiguration'
WLDP_RESETWCOSPRODUCTIONCONFIGURATION_FN = 'WldpResetWcosProductionConfiguration'
WLDP_ISPRODUCTIONCONFIGURATION_FN = 'WldpIsProductionConfiguration'
WLDP_RESETPRODUCTIONCONFIGURATION_FN = 'WldpResetProductionConfiguration'
WLDP_LOCKDOWN_UNDEFINED = 0
WLDP_LOCKDOWN_DEFINED_FLAG = 2147483648
WLDP_LOCKDOWN_CONFIG_CI_FLAG = 1
WLDP_LOCKDOWN_CONFIG_CI_AUDIT_FLAG = 2
WLDP_LOCKDOWN_UMCIENFORCE_FLAG = 4
WLDP_LOCKDOWN_AUDIT_FLAG = 8
WLDP_LOCKDOWN_EXCLUSION_FLAG = 16
WLDP_LOCKDOWN_OFF = 2147483648
WLDP_HOST_INFORMATION_REVISION = 1
WLDP_FLAGS_SKIPSIGNATUREVALIDATION = 256
MAX_TDI_ENTITIES = 4096
INFO_CLASS_GENERIC = 256
INFO_CLASS_PROTOCOL = 512
INFO_CLASS_IMPLEMENTATION = 768
INFO_TYPE_PROVIDER = 256
INFO_TYPE_ADDRESS_OBJECT = 512
INFO_TYPE_CONNECTION = 768
ENTITY_LIST_ID = 0
INVALID_ENTITY_INSTANCE = -1
CONTEXT_SIZE = 16
ENTITY_TYPE_ID = 1
CO_TL_NBF = 1024
CO_TL_SPX = 1026
CO_TL_TCP = 1028
CO_TL_SPP = 1030
CL_TL_NBF = 1025
CL_TL_UDP = 1027
ER_ICMP = 896
CL_NL_IPX = 769
CL_NL_IP = 771
AT_ARP = 640
AT_NULL = 642
IF_GENERIC = 512
IF_MIB = 514
IOCTL_TDI_TL_IO_CONTROL_ENDPOINT = 2162744
DCI_VERSION = 256
DCICREATEPRIMARYSURFACE = 1
DCICREATEOFFSCREENSURFACE = 2
DCICREATEOVERLAYSURFACE = 3
DCIENUMSURFACE = 4
DCIESCAPE = 5
DCI_OK = 0
DCI_FAIL_GENERIC = -1
DCI_FAIL_UNSUPPORTEDVERSION = -2
DCI_FAIL_INVALIDSURFACE = -3
DCI_FAIL_UNSUPPORTED = -4
DCI_ERR_CURRENTLYNOTAVAIL = -5
DCI_ERR_INVALIDRECT = -6
DCI_ERR_UNSUPPORTEDFORMAT = -7
DCI_ERR_UNSUPPORTEDMASK = -8
DCI_ERR_TOOBIGHEIGHT = -9
DCI_ERR_TOOBIGWIDTH = -10
DCI_ERR_TOOBIGSIZE = -11
DCI_ERR_OUTOFMEMORY = -12
DCI_ERR_INVALIDPOSITION = -13
DCI_ERR_INVALIDSTRETCH = -14
DCI_ERR_INVALIDCLIPLIST = -15
DCI_ERR_SURFACEISOBSCURED = -16
DCI_ERR_XALIGN = -17
DCI_ERR_YALIGN = -18
DCI_ERR_XYALIGN = -19
DCI_ERR_WIDTHALIGN = -20
DCI_ERR_HEIGHTALIGN = -21
DCI_STATUS_POINTERCHANGED = 1
DCI_STATUS_STRIDECHANGED = 2
DCI_STATUS_FORMATCHANGED = 4
DCI_STATUS_SURFACEINFOCHANGED = 8
DCI_STATUS_CHROMAKEYCHANGED = 16
DCI_STATUS_WASSTILLDRAWING = 32
DCI_SURFACE_TYPE = 15
DCI_PRIMARY = 0
DCI_OFFSCREEN = 1
DCI_OVERLAY = 2
DCI_VISIBLE = 16
DCI_CHROMAKEY = 32
DCI_1632_ACCESS = 64
DCI_DWORDSIZE = 128
DCI_DWORDALIGN = 256
DCI_WRITEONLY = 512
DCI_ASYNC = 1024
DCI_CAN_STRETCHX = 4096
DCI_CAN_STRETCHY = 8192
DCI_CAN_STRETCHXN = 16384
DCI_CAN_STRETCHYN = 32768
DCI_CANOVERLAY = 65536
FILE_FLAG_OPEN_REQUIRING_OPLOCK = 262144
PROGRESS_CONTINUE = 0
PROGRESS_CANCEL = 1
PROGRESS_STOP = 2
PROGRESS_QUIET = 3
COPY_FILE_FAIL_IF_EXISTS = 1
COPY_FILE_RESTARTABLE = 2
COPY_FILE_OPEN_SOURCE_FOR_WRITE = 4
COPY_FILE_ALLOW_DECRYPTED_DESTINATION = 8
COPY_FILE_COPY_SYMLINK = 2048
COPY_FILE_NO_BUFFERING = 4096
COPY_FILE_REQUEST_SECURITY_PRIVILEGES = 8192
COPY_FILE_RESUME_FROM_PAUSE = 16384
COPY_FILE_NO_OFFLOAD = 262144
COPY_FILE_IGNORE_EDP_BLOCK = 4194304
COPY_FILE_IGNORE_SOURCE_ENCRYPTION = 8388608
COPY_FILE_DONT_REQUEST_DEST_WRITE_DAC = 33554432
COPY_FILE_REQUEST_COMPRESSED_TRAFFIC = 268435456
COPY_FILE_OPEN_AND_COPY_REPARSE_POINT = 2097152
COPY_FILE_DIRECTORY = 128
COPY_FILE_SKIP_ALTERNATE_STREAMS = 32768
COPY_FILE_DISABLE_PRE_ALLOCATION = 67108864
COPY_FILE_ENABLE_LOW_FREE_SPACE_MODE = 134217728
FAIL_FAST_GENERATE_EXCEPTION_ADDRESS = 1
FAIL_FAST_NO_HARD_ERROR_DLG = 2
DTR_CONTROL_DISABLE = 0
DTR_CONTROL_ENABLE = 1
DTR_CONTROL_HANDSHAKE = 2
RTS_CONTROL_DISABLE = 0
RTS_CONTROL_ENABLE = 1
RTS_CONTROL_HANDSHAKE = 2
RTS_CONTROL_TOGGLE = 3
GMEM_NOCOMPACT = 16
GMEM_NODISCARD = 32
GMEM_MODIFY = 128
GMEM_DISCARDABLE = 256
GMEM_NOT_BANKED = 4096
GMEM_SHARE = 8192
GMEM_DDESHARE = 8192
GMEM_NOTIFY = 16384
GMEM_LOWER = 4096
GMEM_VALID_FLAGS = 32626
GMEM_INVALID_HANDLE = 32768
GMEM_DISCARDED = 16384
GMEM_LOCKCOUNT = 255
THREAD_PRIORITY_ERROR_RETURN = 2147483647
VOLUME_NAME_DOS = 0
VOLUME_NAME_GUID = 1
VOLUME_NAME_NT = 2
VOLUME_NAME_NONE = 4
DRIVE_UNKNOWN = 0
DRIVE_NO_ROOT_DIR = 1
DRIVE_REMOVABLE = 2
DRIVE_FIXED = 3
DRIVE_REMOTE = 4
DRIVE_CDROM = 5
DRIVE_RAMDISK = 6
IGNORE = 0
INFINITE = 4294967295
CBR_110 = 110
CBR_300 = 300
CBR_600 = 600
CBR_1200 = 1200
CBR_2400 = 2400
CBR_4800 = 4800
CBR_9600 = 9600
CBR_14400 = 14400
CBR_19200 = 19200
CBR_38400 = 38400
CBR_56000 = 56000
CBR_57600 = 57600
CBR_115200 = 115200
CBR_128000 = 128000
CBR_256000 = 256000
CE_TXFULL = 256
CE_PTO = 512
CE_IOE = 1024
CE_DNS = 2048
CE_OOP = 4096
CE_MODE = 32768
IE_BADID = -1
IE_OPEN = -2
IE_NOPEN = -3
IE_MEMORY = -4
IE_DEFAULT = -5
IE_HARDWARE = -10
IE_BYTESIZE = -11
IE_BAUDRATE = -12
RESETDEV = 7
LPTx = 128
S_QUEUEEMPTY = 0
S_THRESHOLD = 1
S_ALLTHRESHOLD = 2
S_NORMAL = 0
S_LEGATO = 1
S_STACCATO = 2
S_PERIOD512 = 0
S_PERIOD1024 = 1
S_PERIOD2048 = 2
S_PERIODVOICE = 3
S_WHITE512 = 4
S_WHITE1024 = 5
S_WHITE2048 = 6
S_WHITEVOICE = 7
S_SERDVNA = -1
S_SEROFM = -2
S_SERMACT = -3
S_SERQFUL = -4
S_SERBDNT = -5
S_SERDLN = -6
S_SERDCC = -7
S_SERDTP = -8
S_SERDVL = -9
S_SERDMD = -10
S_SERDSH = -11
S_SERDPT = -12
S_SERDFQ = -13
S_SERDDR = -14
S_SERDSR = -15
S_SERDST = -16
FS_CASE_IS_PRESERVED = 2
FS_CASE_SENSITIVE = 1
FS_UNICODE_STORED_ON_DISK = 4
FS_PERSISTENT_ACLS = 8
FS_VOL_IS_COMPRESSED = 32768
FS_FILE_COMPRESSION = 16
FS_FILE_ENCRYPTION = 131072
OFS_MAXPATHNAME = 128
MAXINTATOM = 49152
SCS_32BIT_BINARY = 0
SCS_DOS_BINARY = 1
SCS_WOW_BINARY = 2
SCS_PIF_BINARY = 3
SCS_POSIX_BINARY = 4
SCS_OS216_BINARY = 5
SCS_64BIT_BINARY = 6
SCS_THIS_PLATFORM_BINARY = 6
FIBER_FLAG_FLOAT_SWITCH = 1
UMS_VERSION = 256
FILE_SKIP_COMPLETION_PORT_ON_SUCCESS = 1
FILE_SKIP_SET_EVENT_ON_HANDLE = 2
CRITICAL_SECTION_NO_DEBUG_INFO = 16777216
HINSTANCE_ERROR = 32
FORMAT_MESSAGE_MAX_WIDTH_MASK = 255
FILE_ENCRYPTABLE = 0
FILE_IS_ENCRYPTED = 1
FILE_SYSTEM_ATTR = 2
FILE_ROOT_DIR = 3
FILE_SYSTEM_DIR = 4
FILE_UNKNOWN = 5
FILE_SYSTEM_NOT_SUPPORT = 6
FILE_USER_DISALLOWED = 7
FILE_READ_ONLY = 8
FILE_DIR_DISALLOWED = 9
EFS_USE_RECOVERY_KEYS = 1
CREATE_FOR_IMPORT = 1
CREATE_FOR_DIR = 2
OVERWRITE_HIDDEN = 4
EFSRPC_SECURE_ONLY = 8
EFS_DROP_ALTERNATE_STREAMS = 16
BACKUP_INVALID = 0
BACKUP_GHOSTED_FILE_EXTENTS = 11
STREAM_NORMAL_ATTRIBUTE = 0
STREAM_MODIFIED_WHEN_READ = 1
STREAM_CONTAINS_SECURITY = 2
STREAM_CONTAINS_PROPERTIES = 4
STREAM_SPARSE_ATTRIBUTE = 8
STREAM_CONTAINS_GHOSTED_FILE_EXTENTS = 16
STARTF_HOLOGRAPHIC = 262144
SHUTDOWN_NORETRY = 1
PROTECTION_LEVEL_SAME = 4294967295
PROC_THREAD_ATTRIBUTE_NUMBER = 65535
PROC_THREAD_ATTRIBUTE_THREAD = 65536
PROC_THREAD_ATTRIBUTE_INPUT = 131072
PROC_THREAD_ATTRIBUTE_ADDITIVE = 262144
PROCESS_CREATION_MITIGATION_POLICY_DEP_ENABLE = 1
PROCESS_CREATION_MITIGATION_POLICY_DEP_ATL_THUNK_ENABLE = 2
PROCESS_CREATION_MITIGATION_POLICY_SEHOP_ENABLE = 4
PROCESS_CREATION_CHILD_PROCESS_RESTRICTED = 1
PROCESS_CREATION_CHILD_PROCESS_OVERRIDE = 2
PROCESS_CREATION_CHILD_PROCESS_RESTRICTED_UNLESS_SECURE = 4
PROCESS_CREATION_ALL_APPLICATION_PACKAGES_OPT_OUT = 1
PROCESS_CREATION_DESKTOP_APP_BREAKAWAY_ENABLE_PROCESS_TREE = 1
PROCESS_CREATION_DESKTOP_APP_BREAKAWAY_DISABLE_PROCESS_TREE = 2
PROCESS_CREATION_DESKTOP_APP_BREAKAWAY_OVERRIDE = 4
ATOM_FLAG_GLOBAL = 2
GET_SYSTEM_WOW64_DIRECTORY_NAME_A_A = 'GetSystemWow64DirectoryA'
GET_SYSTEM_WOW64_DIRECTORY_NAME_A_W = 'GetSystemWow64DirectoryA'
GET_SYSTEM_WOW64_DIRECTORY_NAME_A_T = 'GetSystemWow64DirectoryA'
GET_SYSTEM_WOW64_DIRECTORY_NAME_W_A = 'GetSystemWow64DirectoryW'
GET_SYSTEM_WOW64_DIRECTORY_NAME_W_W = 'GetSystemWow64DirectoryW'
GET_SYSTEM_WOW64_DIRECTORY_NAME_W_T = 'GetSystemWow64DirectoryW'
GET_SYSTEM_WOW64_DIRECTORY_NAME_T_A = 'GetSystemWow64DirectoryW'
GET_SYSTEM_WOW64_DIRECTORY_NAME_T_W = 'GetSystemWow64DirectoryW'
GET_SYSTEM_WOW64_DIRECTORY_NAME_T_T = 'GetSystemWow64DirectoryW'
BASE_SEARCH_PATH_ENABLE_SAFE_SEARCHMODE = 1
BASE_SEARCH_PATH_DISABLE_SAFE_SEARCHMODE = 65536
BASE_SEARCH_PATH_PERMANENT = 32768
COPYFILE2_MESSAGE_COPY_OFFLOAD = 1
COPYFILE2_IO_CYCLE_SIZE_MIN = 4096
COPYFILE2_IO_CYCLE_SIZE_MAX = 1073741824
COPYFILE2_IO_RATE_MIN = 512
EVENTLOG_FULL_INFO = 0
OPERATION_API_VERSION = 1
MAX_COMPUTERNAME_LENGTH = 15
LOGON32_PROVIDER_WINNT35 = 1
LOGON32_PROVIDER_VIRTUAL = 4
LOGON_ZERO_PASSWORD_BUFFER = 2147483648
HW_PROFILE_GUIDLEN = 39
DOCKINFO_UNDOCKED = 1
DOCKINFO_DOCKED = 2
DOCKINFO_USER_SUPPLIED = 4
TC_NORMAL = 0
TC_HARDERR = 1
TC_GP_TRAP = 2
TC_SIGNAL = 3
AC_LINE_OFFLINE = 0
AC_LINE_ONLINE = 1
AC_LINE_BACKUP_POWER = 2
AC_LINE_UNKNOWN = 255
BATTERY_FLAG_HIGH = 1
BATTERY_FLAG_LOW = 2
BATTERY_FLAG_CRITICAL = 4
BATTERY_FLAG_CHARGING = 8
BATTERY_FLAG_NO_BATTERY = 128
BATTERY_FLAG_UNKNOWN = 255
BATTERY_PERCENTAGE_UNKNOWN = 255
SYSTEM_STATUS_FLAG_POWER_SAVING_ON = 1
BATTERY_LIFE_UNKNOWN = 4294967295
ACTCTX_FLAG_PROCESSOR_ARCHITECTURE_VALID = 1
ACTCTX_FLAG_LANGID_VALID = 2
ACTCTX_FLAG_ASSEMBLY_DIRECTORY_VALID = 4
ACTCTX_FLAG_RESOURCE_NAME_VALID = 8
ACTCTX_FLAG_SET_PROCESS_DEFAULT = 16
ACTCTX_FLAG_APPLICATION_NAME_VALID = 32
ACTCTX_FLAG_SOURCE_IS_ASSEMBLYREF = 64
ACTCTX_FLAG_HMODULE_VALID = 128
DEACTIVATE_ACTCTX_FLAG_FORCE_EARLY_DEACTIVATION = 1
FIND_ACTCTX_SECTION_KEY_RETURN_HACTCTX = 1
FIND_ACTCTX_SECTION_KEY_RETURN_FLAGS = 2
FIND_ACTCTX_SECTION_KEY_RETURN_ASSEMBLY_METADATA = 4
ACTIVATION_CONTEXT_BASIC_INFORMATION_DEFINED = 1
QUERY_ACTCTX_FLAG_USE_ACTIVE_ACTCTX = 4
QUERY_ACTCTX_FLAG_ACTCTX_IS_HMODULE = 8
QUERY_ACTCTX_FLAG_ACTCTX_IS_ADDRESS = 16
QUERY_ACTCTX_FLAG_NO_ADDREF = 2147483648
RESTART_MAX_CMD_LINE = 1024
RECOVERY_DEFAULT_PING_INTERVAL = 5000
FILE_RENAME_FLAG_REPLACE_IF_EXISTS = 1
FILE_RENAME_FLAG_POSIX_SEMANTICS = 2
FILE_RENAME_FLAG_SUPPRESS_PIN_STATE_INHERITANCE = 4
FILE_DISPOSITION_FLAG_DO_NOT_DELETE = 0
FILE_DISPOSITION_FLAG_DELETE = 1
FILE_DISPOSITION_FLAG_POSIX_SEMANTICS = 2
FILE_DISPOSITION_FLAG_FORCE_IMAGE_SECTION_CHECK = 4
FILE_DISPOSITION_FLAG_ON_CLOSE = 8
FILE_DISPOSITION_FLAG_IGNORE_READONLY_ATTRIBUTE = 16
STORAGE_INFO_FLAGS_ALIGNED_DEVICE = 1
STORAGE_INFO_FLAGS_PARTITION_ALIGNED_ON_DEVICE = 2
STORAGE_INFO_OFFSET_UNKNOWN = 4294967295
REMOTE_PROTOCOL_INFO_FLAG_LOOPBACK = 1
REMOTE_PROTOCOL_INFO_FLAG_OFFLINE = 2
REMOTE_PROTOCOL_INFO_FLAG_PERSISTENT_HANDLE = 4
RPI_FLAG_SMB2_SHARECAP_TIMEWARP = 2
RPI_FLAG_SMB2_SHARECAP_DFS = 8
RPI_FLAG_SMB2_SHARECAP_CONTINUOUS_AVAILABILITY = 16
RPI_FLAG_SMB2_SHARECAP_SCALEOUT = 32
RPI_FLAG_SMB2_SHARECAP_CLUSTER = 64
RPI_SMB2_FLAG_SERVERCAP_DFS = 1
RPI_SMB2_FLAG_SERVERCAP_LEASING = 2
RPI_SMB2_FLAG_SERVERCAP_LARGEMTU = 4
RPI_SMB2_FLAG_SERVERCAP_MULTICHANNEL = 8
RPI_SMB2_FLAG_SERVERCAP_PERSISTENT_HANDLES = 16
RPI_SMB2_FLAG_SERVERCAP_DIRECTORY_LEASING = 32
MICROSOFT_WINDOWS_WINBASE_H_DEFINE_INTERLOCKED_CPLUSPLUS_OVERLOADS = 0
MICROSOFT_WINBASE_H_DEFINE_INTERLOCKED_CPLUSPLUS_OVERLOADS = 0
CODEINTEGRITY_OPTION_ENABLED = 1
CODEINTEGRITY_OPTION_TESTSIGN = 2
CODEINTEGRITY_OPTION_UMCI_ENABLED = 4
CODEINTEGRITY_OPTION_UMCI_AUDITMODE_ENABLED = 8
CODEINTEGRITY_OPTION_UMCI_EXCLUSIONPATHS_ENABLED = 16
CODEINTEGRITY_OPTION_TEST_BUILD = 32
CODEINTEGRITY_OPTION_PREPRODUCTION_BUILD = 64
CODEINTEGRITY_OPTION_DEBUGMODE_ENABLED = 128
CODEINTEGRITY_OPTION_FLIGHT_BUILD = 256
CODEINTEGRITY_OPTION_FLIGHTING_ENABLED = 512
CODEINTEGRITY_OPTION_HVCI_KMCI_ENABLED = 1024
CODEINTEGRITY_OPTION_HVCI_KMCI_AUDITMODE_ENABLED = 2048
CODEINTEGRITY_OPTION_HVCI_KMCI_STRICTMODE_ENABLED = 4096
CODEINTEGRITY_OPTION_HVCI_IUM_ENABLED = 8192
FILE_MAXIMUM_DISPOSITION = 5
FILE_DIRECTORY_FILE = 1
FILE_WRITE_THROUGH = 2
FILE_SEQUENTIAL_ONLY = 4
FILE_NO_INTERMEDIATE_BUFFERING = 8
FILE_SYNCHRONOUS_IO_ALERT = 16
FILE_SYNCHRONOUS_IO_NONALERT = 32
FILE_NON_DIRECTORY_FILE = 64
FILE_CREATE_TREE_CONNECTION = 128
FILE_COMPLETE_IF_OPLOCKED = 256
FILE_NO_EA_KNOWLEDGE = 512
FILE_OPEN_REMOTE_INSTANCE = 1024
FILE_RANDOM_ACCESS = 2048
FILE_DELETE_ON_CLOSE = 4096
FILE_OPEN_BY_FILE_ID = 8192
FILE_OPEN_FOR_BACKUP_INTENT = 16384
FILE_NO_COMPRESSION = 32768
FILE_OPEN_REQUIRING_OPLOCK = 65536
FILE_RESERVE_OPFILTER = 1048576
FILE_OPEN_REPARSE_POINT = 2097152
FILE_OPEN_NO_RECALL = 4194304
FILE_OPEN_FOR_FREE_SPACE_QUERY = 8388608
FILE_VALID_OPTION_FLAGS = 16777215
FILE_VALID_PIPE_OPTION_FLAGS = 50
FILE_VALID_MAILSLOT_OPTION_FLAGS = 50
FILE_VALID_SET_FLAGS = 54
FILE_SUPERSEDED = 0
FILE_OPENED = 1
FILE_CREATED = 2
FILE_OVERWRITTEN = 3
FILE_EXISTS = 4
FILE_DOES_NOT_EXIST = 5
WINWATCHNOTIFY_START = 0
WINWATCHNOTIFY_STOP = 1
WINWATCHNOTIFY_DESTROY = 2
WINWATCHNOTIFY_CHANGING = 3
WINWATCHNOTIFY_CHANGED = 4
RSC_FLAG_INF = 1
RSC_FLAG_SKIPDISKSPACECHECK = 2
RSC_FLAG_QUIET = 4
RSC_FLAG_NGCONV = 8
RSC_FLAG_UPDHLPDLLS = 16
RSC_FLAG_DELAYREGISTEROCX = 512
RSC_FLAG_SETUPAPI = 1024
ALINF_QUIET = 4
ALINF_NGCONV = 8
ALINF_UPDHLPDLLS = 16
ALINF_BKINSTALL = 32
ALINF_ROLLBACK = 64
ALINF_CHECKBKDATA = 128
ALINF_ROLLBKDOALL = 256
ALINF_DELAYREGISTEROCX = 512
AIF_WARNIFSKIP = 1
AIF_NOSKIP = 2
AIF_NOVERSIONCHECK = 4
AIF_FORCE_FILE_IN_USE = 8
AIF_NOOVERWRITE = 16
AIF_NO_VERSION_DIALOG = 32
AIF_REPLACEONLY = 1024
AIF_NOLANGUAGECHECK = 268435456
AIF_QUIET = 536870912
IE4_RESTORE = 1
IE4_BACKNEW = 2
IE4_NODELETENEW = 4
IE4_NOMESSAGES = 8
IE4_NOPROGRESS = 16
IE4_NOENUMKEY = 32
IE4_NO_CRC_MAPPING = 64
IE4_REGSECTION = 128
IE4_FRDOALL = 256
IE4_UPDREFCNT = 512
IE4_USEREFCNT = 1024
IE4_EXTRAINCREFCNT = 2048
IE4_REMOVREGBKDATA = 4096
ARSR_RESTORE = 1
ARSR_NOMESSAGES = 8
ARSR_REGSECTION = 128
ARSR_REMOVREGBKDATA = 4096
REG_SAVE_LOG_KEY = 'RegSaveLogFile'
REG_RESTORE_LOG_KEY = 'RegRestoreLogFile'
AFSR_RESTORE = 1
AFSR_BACKNEW = 2
AFSR_NODELETENEW = 4
AFSR_NOMESSAGES = 8
AFSR_NOPROGRESS = 16
AFSR_UPDREFCNT = 512
AFSR_USEREFCNT = 1024
AFSR_EXTRAINCREFCNT = 2048
AADBE_ADD_ENTRY = 1
AADBE_DEL_ENTRY = 2
ADN_DEL_IF_EMPTY = 1
ADN_DONT_DEL_SUBDIRS = 2
ADN_DONT_DEL_DIR = 4
ADN_DEL_UNC_PATHS = 8
LIS_QUIET = 1
LIS_NOGRPCONV = 2
RUNCMDS_QUIET = 1
RUNCMDS_NOWAIT = 2
RUNCMDS_DELAYPOSTCMD = 4
IME_MAXPROCESS = 32
CP_HWND = 0
CP_OPEN = 1
CP_DIRECT = 2
CP_LEVEL = 3
MCW_DEFAULT = 0
MCW_RECT = 1
MCW_WINDOW = 2
MCW_SCREEN = 4
MCW_VERTICAL = 8
MCW_HIDDEN = 16
IME_MODE_ALPHANUMERIC = 1
IME_MODE_SBCSCHAR = 2
IME_MODE_KATAKANA = 2
IME_MODE_HIRAGANA = 4
IME_MODE_HANJACONVERT = 4
IME_MODE_DBCSCHAR = 16
IME_MODE_ROMAN = 32
IME_MODE_NOROMAN = 64
IME_MODE_CODEINPUT = 128
IME_MODE_NOCODEINPUT = 256
IME_GETIMECAPS = 3
IME_SETOPEN = 4
IME_GETOPEN = 5
IME_GETVERSION = 7
IME_SETCONVERSIONWINDOW = 8
IME_MOVEIMEWINDOW = 8
IME_SETCONVERSIONMODE = 16
IME_GETCONVERSIONMODE = 17
IME_SET_MODE = 18
IME_SENDVKEY = 19
IME_ENTERWORDREGISTERMODE = 24
IME_SETCONVERSIONFONTEX = 25
IME_BANJAtoJUNJA = 19
IME_JUNJAtoBANJA = 20
IME_JOHABtoKS = 21
IME_KStoJOHAB = 22
IMEA_INIT = 1
IMEA_NEXT = 2
IMEA_PREV = 3
IME_REQUEST_CONVERT = 1
IME_ENABLE_CONVERT = 2
INTERIM_WINDOW = 0
MODE_WINDOW = 1
HANJA_WINDOW = 2
IME_RS_ERROR = 1
IME_RS_NOIME = 2
IME_RS_TOOLONG = 5
IME_RS_ILLEGAL = 6
IME_RS_NOTFOUND = 7
IME_RS_NOROOM = 10
IME_RS_DISKERROR = 14
IME_RS_INVALID = 17
IME_RS_NEST = 18
IME_RS_SYSTEMMODAL = 19
WM_IME_REPORT = 640
IR_STRINGSTART = 256
IR_STRINGEND = 257
IR_OPENCONVERT = 288
IR_CHANGECONVERT = 289
IR_CLOSECONVERT = 290
IR_FULLCONVERT = 291
IR_IMESELECT = 304
IR_STRING = 320
IR_DBCSCHAR = 352
IR_UNDETERMINE = 368
IR_STRINGEX = 384
IR_MODEINFO = 400
WM_WNT_CONVERTREQUESTEX = 265
WM_CONVERTREQUEST = 266
WM_CONVERTRESULT = 267
WM_INTERIM = 268
WM_IMEKEYDOWN = 656
WM_IMEKEYUP = 657
DELAYLOAD_GPA_FAILURE = 4
def _define_CATID_DeleteBrowsingHistory():
    return Guid('31caf6e4-d6aa-4090-a0-50-a5-ac-89-72-e9-ef')
DELETE_BROWSING_HISTORY_HISTORY = 1
DELETE_BROWSING_HISTORY_COOKIES = 2
DELETE_BROWSING_HISTORY_TIF = 4
DELETE_BROWSING_HISTORY_FORMDATA = 8
DELETE_BROWSING_HISTORY_PASSWORDS = 16
DELETE_BROWSING_HISTORY_PRESERVEFAVORITES = 32
DELETE_BROWSING_HISTORY_DOWNLOADHISTORY = 64
def _define_uaw_lstrcmpW():
    try:
        return WINFUNCTYPE(Int32,POINTER(UInt16),POINTER(UInt16))(('uaw_lstrcmpW', windll['KERNEL32.dll']), ((1, 'String1'),(1, 'String2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_uaw_lstrcmpiW():
    try:
        return WINFUNCTYPE(Int32,POINTER(UInt16),POINTER(UInt16))(('uaw_lstrcmpiW', windll['KERNEL32.dll']), ((1, 'String1'),(1, 'String2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_uaw_lstrlenW():
    try:
        return WINFUNCTYPE(Int32,POINTER(UInt16))(('uaw_lstrlenW', windll['KERNEL32.dll']), ((1, 'String'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_uaw_wcschr():
    try:
        return WINFUNCTYPE(POINTER(UInt16),POINTER(UInt16),Char)(('uaw_wcschr', windll['KERNEL32.dll']), ((1, 'String'),(1, 'Character'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_uaw_wcscpy():
    try:
        return WINFUNCTYPE(POINTER(UInt16),POINTER(UInt16),POINTER(UInt16))(('uaw_wcscpy', windll['KERNEL32.dll']), ((1, 'Destination'),(1, 'Source'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_uaw_wcsicmp():
    try:
        return WINFUNCTYPE(Int32,POINTER(UInt16),POINTER(UInt16))(('uaw_wcsicmp', windll['KERNEL32.dll']), ((1, 'String1'),(1, 'String2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_uaw_wcslen():
    try:
        return WINFUNCTYPE(UIntPtr,POINTER(UInt16))(('uaw_wcslen', windll['KERNEL32.dll']), ((1, 'String'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_uaw_wcsrchr():
    try:
        return WINFUNCTYPE(POINTER(UInt16),POINTER(UInt16),Char)(('uaw_wcsrchr', windll['KERNEL32.dll']), ((1, 'String'),(1, 'Character'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlGetReturnAddressHijackTarget():
    try:
        return WINFUNCTYPE(UIntPtr,)(('RtlGetReturnAddressHijackTarget', windll['ntdll.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlRaiseCustomSystemEventTrigger():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.WindowsProgramming.CUSTOM_SYSTEM_EVENT_TRIGGER_CONFIG_head))(('RtlRaiseCustomSystemEventTrigger', windll['ntdll.dll']), ((1, 'TriggerConfig'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsApiSetImplemented():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR)(('IsApiSetImplemented', windll['api-ms-win-core-apiquery-l2-1-0.dll']), ((1, 'Contract'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryThreadCycleTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(UInt64))(('QueryThreadCycleTime', windll['KERNEL32.dll']), ((1, 'ThreadHandle'),(1, 'CycleTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryProcessCycleTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(UInt64))(('QueryProcessCycleTime', windll['KERNEL32.dll']), ((1, 'ProcessHandle'),(1, 'CycleTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryIdleProcessorCycleTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(UInt32),POINTER(UInt64))(('QueryIdleProcessorCycleTime', windll['KERNEL32.dll']), ((1, 'BufferLength'),(1, 'ProcessorIdleCycleTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryIdleProcessorCycleTimeEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt16,POINTER(UInt32),POINTER(UInt64))(('QueryIdleProcessorCycleTimeEx', windll['KERNEL32.dll']), ((1, 'Group'),(1, 'BufferLength'),(1, 'ProcessorIdleCycleTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryInterruptTimePrecise():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt64))(('QueryInterruptTimePrecise', windll['api-ms-win-core-realtime-l1-1-1.dll']), ((1, 'lpInterruptTimePrecise'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryUnbiasedInterruptTimePrecise():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt64))(('QueryUnbiasedInterruptTimePrecise', windll['api-ms-win-core-realtime-l1-1-1.dll']), ((1, 'lpUnbiasedInterruptTimePrecise'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryInterruptTime():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt64))(('QueryInterruptTime', windll['api-ms-win-core-realtime-l1-1-1.dll']), ((1, 'lpInterruptTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryUnbiasedInterruptTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(UInt64))(('QueryUnbiasedInterruptTime', windll['KERNEL32.dll']), ((1, 'UnbiasedTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryAuxiliaryCounterFrequency():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64))(('QueryAuxiliaryCounterFrequency', windll['api-ms-win-core-realtime-l1-1-2.dll']), ((1, 'lpAuxiliaryCounterFrequency'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ConvertAuxiliaryCounterToPerformanceCounter():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,POINTER(UInt64),POINTER(UInt64))(('ConvertAuxiliaryCounterToPerformanceCounter', windll['api-ms-win-core-realtime-l1-1-2.dll']), ((1, 'ullAuxiliaryCounterValue'),(1, 'lpPerformanceCounterValue'),(1, 'lpConversionError'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ConvertPerformanceCounterToAuxiliaryCounter():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,POINTER(UInt64),POINTER(UInt64))(('ConvertPerformanceCounterToAuxiliaryCounter', windll['api-ms-win-core-realtime-l1-1-2.dll']), ((1, 'ullPerformanceCounterValue'),(1, 'lpAuxiliaryCounterValue'),(1, 'lpConversionError'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GlobalCompact():
    try:
        return WINFUNCTYPE(UIntPtr,UInt32)(('GlobalCompact', windll['KERNEL32.dll']), ((1, 'dwMinFree'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GlobalFix():
    try:
        return WINFUNCTYPE(Void,IntPtr)(('GlobalFix', windll['KERNEL32.dll']), ((1, 'hMem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GlobalUnfix():
    try:
        return WINFUNCTYPE(Void,IntPtr)(('GlobalUnfix', windll['KERNEL32.dll']), ((1, 'hMem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GlobalWire():
    try:
        return WINFUNCTYPE(c_void_p,IntPtr)(('GlobalWire', windll['KERNEL32.dll']), ((1, 'hMem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GlobalUnWire():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr)(('GlobalUnWire', windll['KERNEL32.dll']), ((1, 'hMem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LocalShrink():
    try:
        return WINFUNCTYPE(UIntPtr,IntPtr,UInt32)(('LocalShrink', windll['KERNEL32.dll']), ((1, 'hMem'),(1, 'cbNewSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LocalCompact():
    try:
        return WINFUNCTYPE(UIntPtr,UInt32)(('LocalCompact', windll['KERNEL32.dll']), ((1, 'uMinFree'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetEnvironmentStringsA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR)(('SetEnvironmentStringsA', windll['KERNEL32.dll']), ((1, 'NewEnvironment'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetHandleCount():
    try:
        return WINFUNCTYPE(UInt32,UInt32)(('SetHandleCount', windll['KERNEL32.dll']), ((1, 'uNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RequestDeviceWakeup():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE)(('RequestDeviceWakeup', windll['KERNEL32.dll']), ((1, 'hDevice'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CancelDeviceWakeupRequest():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE)(('CancelDeviceWakeupRequest', windll['KERNEL32.dll']), ((1, 'hDevice'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetMessageWaitingIndicator():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32)(('SetMessageWaitingIndicator', windll['KERNEL32.dll']), ((1, 'hMsgIndicator'),(1, 'ulMsgCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MulDiv():
    try:
        return WINFUNCTYPE(Int32,Int32,Int32,Int32)(('MulDiv', windll['KERNEL32.dll']), ((1, 'nNumber'),(1, 'nNumerator'),(1, 'nDenominator'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSystemRegistryQuota():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(UInt32),POINTER(UInt32))(('GetSystemRegistryQuota', windll['KERNEL32.dll']), ((1, 'pdwQuotaAllowed'),(1, 'pdwQuotaUsed'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FileTimeToDosDateTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.FILETIME_head),POINTER(UInt16),POINTER(UInt16))(('FileTimeToDosDateTime', windll['KERNEL32.dll']), ((1, 'lpFileTime'),(1, 'lpFatDate'),(1, 'lpFatTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DosDateTimeToFileTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt16,UInt16,POINTER(win32more.Foundation.FILETIME_head))(('DosDateTimeToFileTime', windll['KERNEL32.dll']), ((1, 'wFatDate'),(1, 'wFatTime'),(1, 'lpFileTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define__lopen():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PSTR,Int32)(('_lopen', windll['KERNEL32.dll']), ((1, 'lpPathName'),(1, 'iReadWrite'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define__lcreat():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PSTR,Int32)(('_lcreat', windll['KERNEL32.dll']), ((1, 'lpPathName'),(1, 'iAttribute'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define__lread():
    try:
        return WINFUNCTYPE(UInt32,Int32,c_void_p,UInt32)(('_lread', windll['KERNEL32.dll']), ((1, 'hFile'),(1, 'lpBuffer'),(1, 'uBytes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define__lwrite():
    try:
        return WINFUNCTYPE(UInt32,Int32,win32more.Foundation.PSTR,UInt32)(('_lwrite', windll['KERNEL32.dll']), ((1, 'hFile'),(1, 'lpBuffer'),(1, 'uBytes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define__hread():
    try:
        return WINFUNCTYPE(Int32,Int32,c_void_p,Int32)(('_hread', windll['KERNEL32.dll']), ((1, 'hFile'),(1, 'lpBuffer'),(1, 'lBytes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define__hwrite():
    try:
        return WINFUNCTYPE(Int32,Int32,win32more.Foundation.PSTR,Int32)(('_hwrite', windll['KERNEL32.dll']), ((1, 'hFile'),(1, 'lpBuffer'),(1, 'lBytes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define__lclose():
    try:
        return WINFUNCTYPE(Int32,Int32)(('_lclose', windll['KERNEL32.dll']), ((1, 'hFile'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define__llseek():
    try:
        return WINFUNCTYPE(Int32,Int32,Int32,Int32)(('_llseek', windll['KERNEL32.dll']), ((1, 'hFile'),(1, 'lOffset'),(1, 'iOrigin'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SignalObjectAndWait():
    try:
        return WINFUNCTYPE(win32more.Foundation.WIN32_ERROR,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,UInt32,win32more.Foundation.BOOL)(('SignalObjectAndWait', windll['KERNEL32.dll']), ((1, 'hObjectToSignal'),(1, 'hObjectToWaitOn'),(1, 'dwMilliseconds'),(1, 'bAlertable'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenMutexA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,UInt32,win32more.Foundation.BOOL,win32more.Foundation.PSTR)(('OpenMutexA', windll['KERNEL32.dll']), ((1, 'dwDesiredAccess'),(1, 'bInheritHandle'),(1, 'lpName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenSemaphoreA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,UInt32,win32more.Foundation.BOOL,win32more.Foundation.PSTR)(('OpenSemaphoreA', windll['KERNEL32.dll']), ((1, 'dwDesiredAccess'),(1, 'bInheritHandle'),(1, 'lpName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateWaitableTimerA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),win32more.Foundation.BOOL,win32more.Foundation.PSTR)(('CreateWaitableTimerA', windll['KERNEL32.dll']), ((1, 'lpTimerAttributes'),(1, 'bManualReset'),(1, 'lpTimerName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenWaitableTimerA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,UInt32,win32more.Foundation.BOOL,win32more.Foundation.PSTR)(('OpenWaitableTimerA', windll['KERNEL32.dll']), ((1, 'dwDesiredAccess'),(1, 'bInheritHandle'),(1, 'lpTimerName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateWaitableTimerExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),win32more.Foundation.PSTR,UInt32,UInt32)(('CreateWaitableTimerExA', windll['KERNEL32.dll']), ((1, 'lpTimerAttributes'),(1, 'lpTimerName'),(1, 'dwFlags'),(1, 'dwDesiredAccess'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetFirmwareEnvironmentVariableA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,c_void_p,UInt32)(('GetFirmwareEnvironmentVariableA', windll['KERNEL32.dll']), ((1, 'lpName'),(1, 'lpGuid'),(1, 'pBuffer'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetFirmwareEnvironmentVariableW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,c_void_p,UInt32)(('GetFirmwareEnvironmentVariableW', windll['KERNEL32.dll']), ((1, 'lpName'),(1, 'lpGuid'),(1, 'pBuffer'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetFirmwareEnvironmentVariableExA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,c_void_p,UInt32,POINTER(UInt32))(('GetFirmwareEnvironmentVariableExA', windll['KERNEL32.dll']), ((1, 'lpName'),(1, 'lpGuid'),(1, 'pBuffer'),(1, 'nSize'),(1, 'pdwAttribubutes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetFirmwareEnvironmentVariableExW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,c_void_p,UInt32,POINTER(UInt32))(('GetFirmwareEnvironmentVariableExW', windll['KERNEL32.dll']), ((1, 'lpName'),(1, 'lpGuid'),(1, 'pBuffer'),(1, 'nSize'),(1, 'pdwAttribubutes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetFirmwareEnvironmentVariableA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR,c_void_p,UInt32)(('SetFirmwareEnvironmentVariableA', windll['KERNEL32.dll']), ((1, 'lpName'),(1, 'lpGuid'),(1, 'pValue'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetFirmwareEnvironmentVariableW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,c_void_p,UInt32)(('SetFirmwareEnvironmentVariableW', windll['KERNEL32.dll']), ((1, 'lpName'),(1, 'lpGuid'),(1, 'pValue'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetFirmwareEnvironmentVariableExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR,c_void_p,UInt32,UInt32)(('SetFirmwareEnvironmentVariableExA', windll['KERNEL32.dll']), ((1, 'lpName'),(1, 'lpGuid'),(1, 'pValue'),(1, 'nSize'),(1, 'dwAttributes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetFirmwareEnvironmentVariableExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,c_void_p,UInt32,UInt32)(('SetFirmwareEnvironmentVariableExW', windll['KERNEL32.dll']), ((1, 'lpName'),(1, 'lpGuid'),(1, 'pValue'),(1, 'nSize'),(1, 'dwAttributes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsNativeVhdBoot():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.BOOL))(('IsNativeVhdBoot', windll['KERNEL32.dll']), ((1, 'NativeVhdBoot'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetProfileIntA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,Int32)(('GetProfileIntA', windll['KERNEL32.dll']), ((1, 'lpAppName'),(1, 'lpKeyName'),(1, 'nDefault'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetProfileIntW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,Int32)(('GetProfileIntW', windll['KERNEL32.dll']), ((1, 'lpAppName'),(1, 'lpKeyName'),(1, 'nDefault'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetProfileStringA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32)(('GetProfileStringA', windll['KERNEL32.dll']), ((1, 'lpAppName'),(1, 'lpKeyName'),(1, 'lpDefault'),(1, 'lpReturnedString'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetProfileStringW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32)(('GetProfileStringW', windll['KERNEL32.dll']), ((1, 'lpAppName'),(1, 'lpKeyName'),(1, 'lpDefault'),(1, 'lpReturnedString'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WriteProfileStringA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR)(('WriteProfileStringA', windll['KERNEL32.dll']), ((1, 'lpAppName'),(1, 'lpKeyName'),(1, 'lpString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WriteProfileStringW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('WriteProfileStringW', windll['KERNEL32.dll']), ((1, 'lpAppName'),(1, 'lpKeyName'),(1, 'lpString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetProfileSectionA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32)(('GetProfileSectionA', windll['KERNEL32.dll']), ((1, 'lpAppName'),(1, 'lpReturnedString'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetProfileSectionW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32)(('GetProfileSectionW', windll['KERNEL32.dll']), ((1, 'lpAppName'),(1, 'lpReturnedString'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WriteProfileSectionA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR)(('WriteProfileSectionA', windll['KERNEL32.dll']), ((1, 'lpAppName'),(1, 'lpString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WriteProfileSectionW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('WriteProfileSectionW', windll['KERNEL32.dll']), ((1, 'lpAppName'),(1, 'lpString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPrivateProfileIntA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,Int32,win32more.Foundation.PSTR)(('GetPrivateProfileIntA', windll['KERNEL32.dll']), ((1, 'lpAppName'),(1, 'lpKeyName'),(1, 'nDefault'),(1, 'lpFileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPrivateProfileIntW():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,Int32,win32more.Foundation.PWSTR)(('GetPrivateProfileIntW', windll['KERNEL32.dll']), ((1, 'lpAppName'),(1, 'lpKeyName'),(1, 'nDefault'),(1, 'lpFileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPrivateProfileStringA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR)(('GetPrivateProfileStringA', windll['KERNEL32.dll']), ((1, 'lpAppName'),(1, 'lpKeyName'),(1, 'lpDefault'),(1, 'lpReturnedString'),(1, 'nSize'),(1, 'lpFileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPrivateProfileStringW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR)(('GetPrivateProfileStringW', windll['KERNEL32.dll']), ((1, 'lpAppName'),(1, 'lpKeyName'),(1, 'lpDefault'),(1, 'lpReturnedString'),(1, 'nSize'),(1, 'lpFileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WritePrivateProfileStringA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR)(('WritePrivateProfileStringA', windll['KERNEL32.dll']), ((1, 'lpAppName'),(1, 'lpKeyName'),(1, 'lpString'),(1, 'lpFileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WritePrivateProfileStringW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('WritePrivateProfileStringW', windll['KERNEL32.dll']), ((1, 'lpAppName'),(1, 'lpKeyName'),(1, 'lpString'),(1, 'lpFileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPrivateProfileSectionA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR)(('GetPrivateProfileSectionA', windll['KERNEL32.dll']), ((1, 'lpAppName'),(1, 'lpReturnedString'),(1, 'nSize'),(1, 'lpFileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPrivateProfileSectionW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR)(('GetPrivateProfileSectionW', windll['KERNEL32.dll']), ((1, 'lpAppName'),(1, 'lpReturnedString'),(1, 'nSize'),(1, 'lpFileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WritePrivateProfileSectionA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR)(('WritePrivateProfileSectionA', windll['KERNEL32.dll']), ((1, 'lpAppName'),(1, 'lpString'),(1, 'lpFileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WritePrivateProfileSectionW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('WritePrivateProfileSectionW', windll['KERNEL32.dll']), ((1, 'lpAppName'),(1, 'lpString'),(1, 'lpFileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPrivateProfileSectionNamesA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR)(('GetPrivateProfileSectionNamesA', windll['KERNEL32.dll']), ((1, 'lpszReturnBuffer'),(1, 'nSize'),(1, 'lpFileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPrivateProfileSectionNamesW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR)(('GetPrivateProfileSectionNamesW', windll['KERNEL32.dll']), ((1, 'lpszReturnBuffer'),(1, 'nSize'),(1, 'lpFileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPrivateProfileStructA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR,c_void_p,UInt32,win32more.Foundation.PSTR)(('GetPrivateProfileStructA', windll['KERNEL32.dll']), ((1, 'lpszSection'),(1, 'lpszKey'),(1, 'lpStruct'),(1, 'uSizeStruct'),(1, 'szFile'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPrivateProfileStructW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,c_void_p,UInt32,win32more.Foundation.PWSTR)(('GetPrivateProfileStructW', windll['KERNEL32.dll']), ((1, 'lpszSection'),(1, 'lpszKey'),(1, 'lpStruct'),(1, 'uSizeStruct'),(1, 'szFile'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WritePrivateProfileStructA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR,c_void_p,UInt32,win32more.Foundation.PSTR)(('WritePrivateProfileStructA', windll['KERNEL32.dll']), ((1, 'lpszSection'),(1, 'lpszKey'),(1, 'lpStruct'),(1, 'uSizeStruct'),(1, 'szFile'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WritePrivateProfileStructW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,c_void_p,UInt32,win32more.Foundation.PWSTR)(('WritePrivateProfileStructW', windll['KERNEL32.dll']), ((1, 'lpszSection'),(1, 'lpszKey'),(1, 'lpStruct'),(1, 'uSizeStruct'),(1, 'szFile'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsBadHugeReadPtr():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,UIntPtr)(('IsBadHugeReadPtr', windll['KERNEL32.dll']), ((1, 'lp'),(1, 'ucb'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsBadHugeWritePtr():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,UIntPtr)(('IsBadHugeWritePtr', windll['KERNEL32.dll']), ((1, 'lp'),(1, 'ucb'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetComputerNameA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,POINTER(UInt32))(('GetComputerNameA', windll['KERNEL32.dll']), ((1, 'lpBuffer'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetComputerNameW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,POINTER(UInt32))(('GetComputerNameW', windll['KERNEL32.dll']), ((1, 'lpBuffer'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsHostnameToComputerNameA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(UInt32))(('DnsHostnameToComputerNameA', windll['KERNEL32.dll']), ((1, 'Hostname'),(1, 'ComputerName'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsHostnameToComputerNameW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32))(('DnsHostnameToComputerNameW', windll['KERNEL32.dll']), ((1, 'Hostname'),(1, 'ComputerName'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetUserNameA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,POINTER(UInt32))(('GetUserNameA', windll['ADVAPI32.dll']), ((1, 'lpBuffer'),(1, 'pcbBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetUserNameW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,POINTER(UInt32))(('GetUserNameW', windll['ADVAPI32.dll']), ((1, 'lpBuffer'),(1, 'pcbBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsTokenUntrusted():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE)(('IsTokenUntrusted', windll['ADVAPI32.dll']), ((1, 'TokenHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CancelTimerQueueTimer():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE)(('CancelTimerQueueTimer', windll['KERNEL32.dll']), ((1, 'TimerQueue'),(1, 'Timer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCurrentHwProfileA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.WindowsProgramming.HW_PROFILE_INFOA_head))(('GetCurrentHwProfileA', windll['ADVAPI32.dll']), ((1, 'lpHwProfileInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCurrentHwProfileW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.WindowsProgramming.HW_PROFILE_INFOW_head))(('GetCurrentHwProfileW', windll['ADVAPI32.dll']), ((1, 'lpHwProfileInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReplacePartitionUnit():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32)(('ReplacePartitionUnit', windll['KERNEL32.dll']), ((1, 'TargetPartition'),(1, 'SparePartition'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetThreadEnabledXStateFeatures():
    try:
        return WINFUNCTYPE(UInt64,)(('GetThreadEnabledXStateFeatures', windll['KERNEL32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnableProcessOptionalXStateFeatures():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt64)(('EnableProcessOptionalXStateFeatures', windll['KERNEL32.dll']), ((1, 'Features'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RaiseCustomSystemEventTrigger():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.WindowsProgramming.CUSTOM_SYSTEM_EVENT_TRIGGER_CONFIG_head))(('RaiseCustomSystemEventTrigger', windll['api-ms-win-core-backgroundtask-l1-1-0.dll']), ((1, 'CustomSystemEventTriggerConfig'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NtClose():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,win32more.Foundation.HANDLE)(('NtClose', windll['ntdll.dll']), ((1, 'Handle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NtOpenFile():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Foundation.HANDLE),UInt32,POINTER(win32more.System.WindowsProgramming.OBJECT_ATTRIBUTES_head),POINTER(win32more.System.WindowsProgramming.IO_STATUS_BLOCK_head),UInt32,UInt32)(('NtOpenFile', windll['ntdll.dll']), ((1, 'FileHandle'),(1, 'DesiredAccess'),(1, 'ObjectAttributes'),(1, 'IoStatusBlock'),(1, 'ShareAccess'),(1, 'OpenOptions'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NtRenameKey():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.UNICODE_STRING_head))(('NtRenameKey', windll['ntdll.dll']), ((1, 'KeyHandle'),(1, 'NewName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NtNotifyChangeMultipleKeys():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,win32more.Foundation.HANDLE,UInt32,POINTER(win32more.System.WindowsProgramming.OBJECT_ATTRIBUTES_head),win32more.Foundation.HANDLE,win32more.System.WindowsProgramming.PIO_APC_ROUTINE,c_void_p,POINTER(win32more.System.WindowsProgramming.IO_STATUS_BLOCK_head),UInt32,win32more.Foundation.BOOLEAN,c_void_p,UInt32,win32more.Foundation.BOOLEAN)(('NtNotifyChangeMultipleKeys', windll['ntdll.dll']), ((1, 'MasterKeyHandle'),(1, 'Count'),(1, 'SubordinateObjects'),(1, 'Event'),(1, 'ApcRoutine'),(1, 'ApcContext'),(1, 'IoStatusBlock'),(1, 'CompletionFilter'),(1, 'WatchTree'),(1, 'Buffer'),(1, 'BufferSize'),(1, 'Asynchronous'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NtQueryMultipleValueKey():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,win32more.Foundation.HANDLE,POINTER(win32more.System.WindowsProgramming.KEY_VALUE_ENTRY_head),UInt32,c_void_p,POINTER(UInt32),POINTER(UInt32))(('NtQueryMultipleValueKey', windll['ntdll.dll']), ((1, 'KeyHandle'),(1, 'ValueEntries'),(1, 'EntryCount'),(1, 'ValueBuffer'),(1, 'BufferLength'),(1, 'RequiredBufferLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NtSetInformationKey():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,win32more.Foundation.HANDLE,win32more.System.WindowsProgramming.KEY_SET_INFORMATION_CLASS,c_void_p,UInt32)(('NtSetInformationKey', windll['ntdll.dll']), ((1, 'KeyHandle'),(1, 'KeySetInformationClass'),(1, 'KeySetInformation'),(1, 'KeySetInformationLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NtDeviceIoControlFile():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,win32more.System.WindowsProgramming.PIO_APC_ROUTINE,c_void_p,POINTER(win32more.System.WindowsProgramming.IO_STATUS_BLOCK_head),UInt32,c_void_p,UInt32,c_void_p,UInt32)(('NtDeviceIoControlFile', windll['ntdll.dll']), ((1, 'FileHandle'),(1, 'Event'),(1, 'ApcRoutine'),(1, 'ApcContext'),(1, 'IoStatusBlock'),(1, 'IoControlCode'),(1, 'InputBuffer'),(1, 'InputBufferLength'),(1, 'OutputBuffer'),(1, 'OutputBufferLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NtWaitForSingleObject():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,win32more.Foundation.HANDLE,win32more.Foundation.BOOLEAN,POINTER(win32more.Foundation.LARGE_INTEGER_head))(('NtWaitForSingleObject', windll['ntdll.dll']), ((1, 'Handle'),(1, 'Alertable'),(1, 'Timeout'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlIsNameLegalDOS8Dot3():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,POINTER(win32more.Foundation.UNICODE_STRING_head),POINTER(win32more.System.Kernel.STRING_head),POINTER(win32more.Foundation.BOOLEAN))(('RtlIsNameLegalDOS8Dot3', windll['ntdll.dll']), ((1, 'Name'),(1, 'OemName'),(1, 'NameContainsSpaces'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NtQueryObject():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,win32more.Foundation.HANDLE,win32more.System.WindowsProgramming.OBJECT_INFORMATION_CLASS,c_void_p,UInt32,POINTER(UInt32))(('NtQueryObject', windll['ntdll.dll']), ((1, 'Handle'),(1, 'ObjectInformationClass'),(1, 'ObjectInformation'),(1, 'ObjectInformationLength'),(1, 'ReturnLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NtQuerySystemInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,win32more.System.WindowsProgramming.SYSTEM_INFORMATION_CLASS,c_void_p,UInt32,POINTER(UInt32))(('NtQuerySystemInformation', windll['ntdll.dll']), ((1, 'SystemInformationClass'),(1, 'SystemInformation'),(1, 'SystemInformationLength'),(1, 'ReturnLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NtQuerySystemTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Foundation.LARGE_INTEGER_head))(('NtQuerySystemTime', windll['ntdll.dll']), ((1, 'SystemTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NtQueryTimerResolution():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32))(('NtQueryTimerResolution', windll['ntdll.dll']), ((1, 'MaximumTime'),(1, 'MinimumTime'),(1, 'CurrentTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlLocalTimeToSystemTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Foundation.LARGE_INTEGER_head),POINTER(win32more.Foundation.LARGE_INTEGER_head))(('RtlLocalTimeToSystemTime', windll['ntdll.dll']), ((1, 'LocalTime'),(1, 'SystemTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlTimeToSecondsSince1970():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,POINTER(win32more.Foundation.LARGE_INTEGER_head),POINTER(UInt32))(('RtlTimeToSecondsSince1970', windll['ntdll.dll']), ((1, 'Time'),(1, 'ElapsedSeconds'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlFreeAnsiString():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Kernel.STRING_head))(('RtlFreeAnsiString', windll['ntdll.dll']), ((1, 'AnsiString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlFreeUnicodeString():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Foundation.UNICODE_STRING_head))(('RtlFreeUnicodeString', windll['ntdll.dll']), ((1, 'UnicodeString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlFreeOemString():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Kernel.STRING_head))(('RtlFreeOemString', windll['ntdll.dll']), ((1, 'OemString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlInitString():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Kernel.STRING_head),POINTER(SByte))(('RtlInitString', windll['ntdll.dll']), ((1, 'DestinationString'),(1, 'SourceString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlInitStringEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.System.Kernel.STRING_head),POINTER(SByte))(('RtlInitStringEx', windll['ntdll.dll']), ((1, 'DestinationString'),(1, 'SourceString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlInitAnsiString():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Kernel.STRING_head),POINTER(SByte))(('RtlInitAnsiString', windll['ntdll.dll']), ((1, 'DestinationString'),(1, 'SourceString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlInitAnsiStringEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.System.Kernel.STRING_head),POINTER(SByte))(('RtlInitAnsiStringEx', windll['ntdll.dll']), ((1, 'DestinationString'),(1, 'SourceString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlInitUnicodeString():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Foundation.UNICODE_STRING_head),win32more.Foundation.PWSTR)(('RtlInitUnicodeString', windll['ntdll.dll']), ((1, 'DestinationString'),(1, 'SourceString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlAnsiStringToUnicodeString():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Foundation.UNICODE_STRING_head),POINTER(win32more.System.Kernel.STRING_head),win32more.Foundation.BOOLEAN)(('RtlAnsiStringToUnicodeString', windll['ntdll.dll']), ((1, 'DestinationString'),(1, 'SourceString'),(1, 'AllocateDestinationString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlUnicodeStringToAnsiString():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.System.Kernel.STRING_head),POINTER(win32more.Foundation.UNICODE_STRING_head),win32more.Foundation.BOOLEAN)(('RtlUnicodeStringToAnsiString', windll['ntdll.dll']), ((1, 'DestinationString'),(1, 'SourceString'),(1, 'AllocateDestinationString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlUnicodeStringToOemString():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.System.Kernel.STRING_head),POINTER(win32more.Foundation.UNICODE_STRING_head),win32more.Foundation.BOOLEAN)(('RtlUnicodeStringToOemString', windll['ntdll.dll']), ((1, 'DestinationString'),(1, 'SourceString'),(1, 'AllocateDestinationString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlUnicodeToMultiByteSize():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(UInt32),win32more.Foundation.PWSTR,UInt32)(('RtlUnicodeToMultiByteSize', windll['ntdll.dll']), ((1, 'BytesInMultiByteString'),(1, 'UnicodeString'),(1, 'BytesInUnicodeString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlCharToInteger():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(SByte),UInt32,POINTER(UInt32))(('RtlCharToInteger', windll['ntdll.dll']), ((1, 'String'),(1, 'Base'),(1, 'Value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlUniform():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32))(('RtlUniform', windll['ntdll.dll']), ((1, 'Seed'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetFeatureEnabledState():
    try:
        return WINFUNCTYPE(win32more.System.WindowsProgramming.FEATURE_ENABLED_STATE,UInt32,win32more.System.WindowsProgramming.FEATURE_CHANGE_TIME)(('GetFeatureEnabledState', windll['api-ms-win-core-featurestaging-l1-1-0.dll']), ((1, 'featureId'),(1, 'changeTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RecordFeatureUsage():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32,UInt32,win32more.Foundation.PSTR)(('RecordFeatureUsage', windll['api-ms-win-core-featurestaging-l1-1-0.dll']), ((1, 'featureId'),(1, 'kind'),(1, 'addend'),(1, 'originName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RecordFeatureError():
    try:
        return WINFUNCTYPE(Void,UInt32,POINTER(win32more.System.WindowsProgramming.FEATURE_ERROR_head))(('RecordFeatureError', windll['api-ms-win-core-featurestaging-l1-1-0.dll']), ((1, 'featureId'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SubscribeFeatureStateChangeNotification():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.WindowsProgramming.FEATURE_STATE_CHANGE_SUBSCRIPTION),win32more.System.WindowsProgramming.PFEATURE_STATE_CHANGE_CALLBACK,c_void_p)(('SubscribeFeatureStateChangeNotification', windll['api-ms-win-core-featurestaging-l1-1-0.dll']), ((1, 'subscription'),(1, 'callback'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UnsubscribeFeatureStateChangeNotification():
    try:
        return WINFUNCTYPE(Void,win32more.System.WindowsProgramming.FEATURE_STATE_CHANGE_SUBSCRIPTION)(('UnsubscribeFeatureStateChangeNotification', windll['api-ms-win-core-featurestaging-l1-1-0.dll']), ((1, 'subscription'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetFeatureVariant():
    try:
        return WINFUNCTYPE(UInt32,UInt32,win32more.System.WindowsProgramming.FEATURE_CHANGE_TIME,POINTER(UInt32),POINTER(win32more.Foundation.BOOL))(('GetFeatureVariant', windll['api-ms-win-core-featurestaging-l1-1-1.dll']), ((1, 'featureId'),(1, 'changeTime'),(1, 'payloadId'),(1, 'hasNotification'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DCIOpenProvider():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HDC,)(('DCIOpenProvider', windll['DCIMAN32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_DCICloseProvider():
    try:
        return WINFUNCTYPE(Void,win32more.Graphics.Gdi.HDC)(('DCICloseProvider', windll['DCIMAN32.dll']), ((1, 'hdc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DCICreatePrimary():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,POINTER(POINTER(win32more.System.WindowsProgramming.DCISURFACEINFO_head)))(('DCICreatePrimary', windll['DCIMAN32.dll']), ((1, 'hdc'),(1, 'lplpSurface'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DCICreateOffscreen():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,UInt32,UInt32,UInt32,UInt32,UInt32,UInt32,UInt32,UInt32,POINTER(POINTER(win32more.System.WindowsProgramming.DCIOFFSCREEN_head)))(('DCICreateOffscreen', windll['DCIMAN32.dll']), ((1, 'hdc'),(1, 'dwCompression'),(1, 'dwRedMask'),(1, 'dwGreenMask'),(1, 'dwBlueMask'),(1, 'dwWidth'),(1, 'dwHeight'),(1, 'dwDCICaps'),(1, 'dwBitCount'),(1, 'lplpSurface'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DCICreateOverlay():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,c_void_p,POINTER(POINTER(win32more.System.WindowsProgramming.DCIOVERLAY_head)))(('DCICreateOverlay', windll['DCIMAN32.dll']), ((1, 'hdc'),(1, 'lpOffscreenSurf'),(1, 'lplpSurface'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DCIEnum():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,POINTER(win32more.Foundation.RECT_head),POINTER(win32more.Foundation.RECT_head),c_void_p,c_void_p)(('DCIEnum', windll['DCIMAN32.dll']), ((1, 'hdc'),(1, 'lprDst'),(1, 'lprSrc'),(1, 'lpFnCallback'),(1, 'lpContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DCISetSrcDestClip():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.WindowsProgramming.DCIOFFSCREEN_head),POINTER(win32more.Foundation.RECT_head),POINTER(win32more.Foundation.RECT_head),POINTER(win32more.Graphics.Gdi.RGNDATA_head))(('DCISetSrcDestClip', windll['DCIMAN32.dll']), ((1, 'pdci'),(1, 'srcrc'),(1, 'destrc'),(1, 'prd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinWatchOpen():
    try:
        return WINFUNCTYPE(win32more.System.WindowsProgramming.HWINWATCH,win32more.Foundation.HWND)(('WinWatchOpen', windll['DCIMAN32.dll']), ((1, 'hwnd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinWatchClose():
    try:
        return WINFUNCTYPE(Void,win32more.System.WindowsProgramming.HWINWATCH)(('WinWatchClose', windll['DCIMAN32.dll']), ((1, 'hWW'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinWatchGetClipList():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.WindowsProgramming.HWINWATCH,POINTER(win32more.Foundation.RECT_head),UInt32,POINTER(win32more.Graphics.Gdi.RGNDATA_head))(('WinWatchGetClipList', windll['DCIMAN32.dll']), ((1, 'hWW'),(1, 'prc'),(1, 'size'),(1, 'prd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinWatchDidStatusChange():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.WindowsProgramming.HWINWATCH)(('WinWatchDidStatusChange', windll['DCIMAN32.dll']), ((1, 'hWW'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetWindowRegionData():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HWND,UInt32,POINTER(win32more.Graphics.Gdi.RGNDATA_head))(('GetWindowRegionData', windll['DCIMAN32.dll']), ((1, 'hwnd'),(1, 'size'),(1, 'prd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDCRegionData():
    try:
        return WINFUNCTYPE(UInt32,win32more.Graphics.Gdi.HDC,UInt32,POINTER(win32more.Graphics.Gdi.RGNDATA_head))(('GetDCRegionData', windll['DCIMAN32.dll']), ((1, 'hdc'),(1, 'size'),(1, 'prd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinWatchNotify():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.WindowsProgramming.HWINWATCH,win32more.System.WindowsProgramming.WINWATCHNOTIFYPROC,win32more.Foundation.LPARAM)(('WinWatchNotify', windll['DCIMAN32.dll']), ((1, 'hWW'),(1, 'NotifyCallback'),(1, 'NotifyParam'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DCIEndAccess():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.WindowsProgramming.DCISURFACEINFO_head))(('DCIEndAccess', windll['DCIMAN32.dll']), ((1, 'pdci'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DCIBeginAccess():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.WindowsProgramming.DCISURFACEINFO_head),Int32,Int32,Int32,Int32)(('DCIBeginAccess', windll['DCIMAN32.dll']), ((1, 'pdci'),(1, 'x'),(1, 'y'),(1, 'dx'),(1, 'dy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DCIDestroy():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.WindowsProgramming.DCISURFACEINFO_head))(('DCIDestroy', windll['DCIMAN32.dll']), ((1, 'pdci'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DCIDraw():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.WindowsProgramming.DCIOFFSCREEN_head))(('DCIDraw', windll['DCIMAN32.dll']), ((1, 'pdci'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DCISetClipList():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.WindowsProgramming.DCIOFFSCREEN_head),POINTER(win32more.Graphics.Gdi.RGNDATA_head))(('DCISetClipList', windll['DCIMAN32.dll']), ((1, 'pdci'),(1, 'prd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DCISetDestination():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.WindowsProgramming.DCIOFFSCREEN_head),POINTER(win32more.Foundation.RECT_head),POINTER(win32more.Foundation.RECT_head))(('DCISetDestination', windll['DCIMAN32.dll']), ((1, 'pdci'),(1, 'dst'),(1, 'src'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GdiEntry13():
    try:
        return WINFUNCTYPE(UInt32,)(('GdiEntry13', windll['api-ms-win-dx-d3dkmt-l1-1-0.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_RunSetupCommandA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(win32more.Foundation.HANDLE),UInt32,c_void_p)(('RunSetupCommandA', windll['ADVPACK.dll']), ((1, 'hWnd'),(1, 'szCmdName'),(1, 'szInfSection'),(1, 'szDir'),(1, 'lpszTitle'),(1, 'phEXE'),(1, 'dwFlags'),(1, 'pvReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RunSetupCommandW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.HANDLE),UInt32,c_void_p)(('RunSetupCommandW', windll['ADVPACK.dll']), ((1, 'hWnd'),(1, 'szCmdName'),(1, 'szInfSection'),(1, 'szDir'),(1, 'lpszTitle'),(1, 'phEXE'),(1, 'dwFlags'),(1, 'pvReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NeedRebootInit():
    try:
        return WINFUNCTYPE(UInt32,)(('NeedRebootInit', windll['ADVPACK.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_NeedReboot():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32)(('NeedReboot', windll['ADVPACK.dll']), ((1, 'dwRebootCheck'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RebootCheckOnInstallA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32)(('RebootCheckOnInstallA', windll['ADVPACK.dll']), ((1, 'hwnd'),(1, 'pszINF'),(1, 'pszSec'),(1, 'dwReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RebootCheckOnInstallW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32)(('RebootCheckOnInstallW', windll['ADVPACK.dll']), ((1, 'hwnd'),(1, 'pszINF'),(1, 'pszSec'),(1, 'dwReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TranslateInfStringA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32,POINTER(UInt32),c_void_p)(('TranslateInfStringA', windll['ADVPACK.dll']), ((1, 'pszInfFilename'),(1, 'pszInstallSection'),(1, 'pszTranslateSection'),(1, 'pszTranslateKey'),(1, 'pszBuffer'),(1, 'cchBuffer'),(1, 'pdwRequiredSize'),(1, 'pvReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TranslateInfStringW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32),c_void_p)(('TranslateInfStringW', windll['ADVPACK.dll']), ((1, 'pszInfFilename'),(1, 'pszInstallSection'),(1, 'pszTranslateSection'),(1, 'pszTranslateKey'),(1, 'pszBuffer'),(1, 'cchBuffer'),(1, 'pdwRequiredSize'),(1, 'pvReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegInstallA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HINSTANCE,win32more.Foundation.PSTR,POINTER(win32more.System.WindowsProgramming.STRTABLEA_head))(('RegInstallA', windll['ADVPACK.dll']), ((1, 'hmod'),(1, 'pszSection'),(1, 'pstTable'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegInstallW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HINSTANCE,win32more.Foundation.PWSTR,POINTER(win32more.System.WindowsProgramming.STRTABLEW_head))(('RegInstallW', windll['ADVPACK.dll']), ((1, 'hmod'),(1, 'pszSection'),(1, 'pstTable'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LaunchINFSectionExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.HINSTANCE,win32more.Foundation.PWSTR,Int32)(('LaunchINFSectionExW', windll['ADVPACK.dll']), ((1, 'hwnd'),(1, 'hInstance'),(1, 'pszParms'),(1, 'nShow'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ExecuteCabA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(win32more.System.WindowsProgramming.CABINFOA_head),c_void_p)(('ExecuteCabA', windll['ADVPACK.dll']), ((1, 'hwnd'),(1, 'pCab'),(1, 'pReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ExecuteCabW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(win32more.System.WindowsProgramming.CABINFOW_head),c_void_p)(('ExecuteCabW', windll['ADVPACK.dll']), ((1, 'hwnd'),(1, 'pCab'),(1, 'pReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AdvInstallFileA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32,UInt32)(('AdvInstallFileA', windll['ADVPACK.dll']), ((1, 'hwnd'),(1, 'lpszSourceDir'),(1, 'lpszSourceFile'),(1, 'lpszDestDir'),(1, 'lpszDestFile'),(1, 'dwFlags'),(1, 'dwReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AdvInstallFileW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,UInt32)(('AdvInstallFileW', windll['ADVPACK.dll']), ((1, 'hwnd'),(1, 'lpszSourceDir'),(1, 'lpszSourceFile'),(1, 'lpszDestDir'),(1, 'lpszDestFile'),(1, 'dwFlags'),(1, 'dwReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegSaveRestoreA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.PSTR,win32more.System.Registry.HKEY,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32)(('RegSaveRestoreA', windll['ADVPACK.dll']), ((1, 'hWnd'),(1, 'pszTitleString'),(1, 'hkBckupKey'),(1, 'pcszRootKey'),(1, 'pcszSubKey'),(1, 'pcszValueName'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegSaveRestoreW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.PWSTR,win32more.System.Registry.HKEY,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32)(('RegSaveRestoreW', windll['ADVPACK.dll']), ((1, 'hWnd'),(1, 'pszTitleString'),(1, 'hkBckupKey'),(1, 'pcszRootKey'),(1, 'pcszSubKey'),(1, 'pcszValueName'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegSaveRestoreOnINFA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.System.Registry.HKEY,win32more.System.Registry.HKEY,UInt32)(('RegSaveRestoreOnINFA', windll['ADVPACK.dll']), ((1, 'hWnd'),(1, 'pszTitle'),(1, 'pszINF'),(1, 'pszSection'),(1, 'hHKLMBackKey'),(1, 'hHKCUBackKey'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegSaveRestoreOnINFW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.System.Registry.HKEY,win32more.System.Registry.HKEY,UInt32)(('RegSaveRestoreOnINFW', windll['ADVPACK.dll']), ((1, 'hWnd'),(1, 'pszTitle'),(1, 'pszINF'),(1, 'pszSection'),(1, 'hHKLMBackKey'),(1, 'hHKCUBackKey'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegRestoreAllA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.PSTR,win32more.System.Registry.HKEY)(('RegRestoreAllA', windll['ADVPACK.dll']), ((1, 'hWnd'),(1, 'pszTitleString'),(1, 'hkBckupKey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegRestoreAllW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.PWSTR,win32more.System.Registry.HKEY)(('RegRestoreAllW', windll['ADVPACK.dll']), ((1, 'hWnd'),(1, 'pszTitleString'),(1, 'hkBckupKey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FileSaveRestoreW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32)(('FileSaveRestoreW', windll['ADVPACK.dll']), ((1, 'hDlg'),(1, 'lpFileList'),(1, 'lpDir'),(1, 'lpBaseName'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FileSaveRestoreOnINFA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32)(('FileSaveRestoreOnINFA', windll['ADVPACK.dll']), ((1, 'hWnd'),(1, 'pszTitle'),(1, 'pszINF'),(1, 'pszSection'),(1, 'pszBackupDir'),(1, 'pszBaseBackupFile'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FileSaveRestoreOnINFW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32)(('FileSaveRestoreOnINFW', windll['ADVPACK.dll']), ((1, 'hWnd'),(1, 'pszTitle'),(1, 'pszINF'),(1, 'pszSection'),(1, 'pszBackupDir'),(1, 'pszBaseBackupFile'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddDelBackupEntryA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32)(('AddDelBackupEntryA', windll['ADVPACK.dll']), ((1, 'lpcszFileList'),(1, 'lpcszBackupDir'),(1, 'lpcszBaseName'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddDelBackupEntryW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32)(('AddDelBackupEntryW', windll['ADVPACK.dll']), ((1, 'lpcszFileList'),(1, 'lpcszBackupDir'),(1, 'lpcszBaseName'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FileSaveMarkNotExistA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR)(('FileSaveMarkNotExistA', windll['ADVPACK.dll']), ((1, 'lpFileList'),(1, 'lpDir'),(1, 'lpBaseName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FileSaveMarkNotExistW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('FileSaveMarkNotExistW', windll['ADVPACK.dll']), ((1, 'lpFileList'),(1, 'lpDir'),(1, 'lpBaseName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetVersionFromFileA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSTR,POINTER(UInt32),POINTER(UInt32),win32more.Foundation.BOOL)(('GetVersionFromFileA', windll['ADVPACK.dll']), ((1, 'lpszFilename'),(1, 'pdwMSVer'),(1, 'pdwLSVer'),(1, 'bVersion'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetVersionFromFileW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(UInt32),win32more.Foundation.BOOL)(('GetVersionFromFileW', windll['ADVPACK.dll']), ((1, 'lpszFilename'),(1, 'pdwMSVer'),(1, 'pdwLSVer'),(1, 'bVersion'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetVersionFromFileExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSTR,POINTER(UInt32),POINTER(UInt32),win32more.Foundation.BOOL)(('GetVersionFromFileExA', windll['ADVPACK.dll']), ((1, 'lpszFilename'),(1, 'pdwMSVer'),(1, 'pdwLSVer'),(1, 'bVersion'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetVersionFromFileExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(UInt32),win32more.Foundation.BOOL)(('GetVersionFromFileExW', windll['ADVPACK.dll']), ((1, 'lpszFilename'),(1, 'pdwMSVer'),(1, 'pdwLSVer'),(1, 'bVersion'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsNTAdmin():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,POINTER(UInt32))(('IsNTAdmin', windll['ADVPACK.dll']), ((1, 'dwReserved'),(1, 'lpdwReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DelNodeA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSTR,UInt32)(('DelNodeA', windll['ADVPACK.dll']), ((1, 'pszFileOrDirName'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DelNodeW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32)(('DelNodeW', windll['ADVPACK.dll']), ((1, 'pszFileOrDirName'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DelNodeRunDLL32W():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.HINSTANCE,win32more.Foundation.PWSTR,Int32)(('DelNodeRunDLL32W', windll['ADVPACK.dll']), ((1, 'hwnd'),(1, 'hInstance'),(1, 'pszParms'),(1, 'nShow'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenINFEngineA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32,POINTER(c_void_p),c_void_p)(('OpenINFEngineA', windll['ADVPACK.dll']), ((1, 'pszInfFilename'),(1, 'pszInstallSection'),(1, 'dwFlags'),(1, 'phInf'),(1, 'pvReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenINFEngineW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(c_void_p),c_void_p)(('OpenINFEngineW', windll['ADVPACK.dll']), ((1, 'pszInfFilename'),(1, 'pszInstallSection'),(1, 'dwFlags'),(1, 'phInf'),(1, 'pvReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TranslateInfStringExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32,POINTER(UInt32),c_void_p)(('TranslateInfStringExA', windll['ADVPACK.dll']), ((1, 'hInf'),(1, 'pszInfFilename'),(1, 'pszTranslateSection'),(1, 'pszTranslateKey'),(1, 'pszBuffer'),(1, 'dwBufferSize'),(1, 'pdwRequiredSize'),(1, 'pvReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TranslateInfStringExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32),c_void_p)(('TranslateInfStringExW', windll['ADVPACK.dll']), ((1, 'hInf'),(1, 'pszInfFilename'),(1, 'pszTranslateSection'),(1, 'pszTranslateKey'),(1, 'pszBuffer'),(1, 'dwBufferSize'),(1, 'pdwRequiredSize'),(1, 'pvReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CloseINFEngine():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p)(('CloseINFEngine', windll['ADVPACK.dll']), ((1, 'hInf'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ExtractFilesA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,c_void_p,UInt32)(('ExtractFilesA', windll['ADVPACK.dll']), ((1, 'pszCabName'),(1, 'pszExpandDir'),(1, 'dwFlags'),(1, 'pszFileList'),(1, 'lpReserved'),(1, 'dwReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ExtractFilesW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,c_void_p,UInt32)(('ExtractFilesW', windll['ADVPACK.dll']), ((1, 'pszCabName'),(1, 'pszExpandDir'),(1, 'dwFlags'),(1, 'pszFileList'),(1, 'lpReserved'),(1, 'dwReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LaunchINFSectionW():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HWND,win32more.Foundation.HINSTANCE,win32more.Foundation.PWSTR,Int32)(('LaunchINFSectionW', windll['ADVPACK.dll']), ((1, 'hwndOwner'),(1, 'hInstance'),(1, 'pszParams'),(1, 'nShow'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UserInstStubWrapperA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.HINSTANCE,win32more.Foundation.PSTR,Int32)(('UserInstStubWrapperA', windll['ADVPACK.dll']), ((1, 'hwnd'),(1, 'hInstance'),(1, 'pszParms'),(1, 'nShow'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UserInstStubWrapperW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.HINSTANCE,win32more.Foundation.PWSTR,Int32)(('UserInstStubWrapperW', windll['ADVPACK.dll']), ((1, 'hwnd'),(1, 'hInstance'),(1, 'pszParms'),(1, 'nShow'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UserUnInstStubWrapperA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.HINSTANCE,win32more.Foundation.PSTR,Int32)(('UserUnInstStubWrapperA', windll['ADVPACK.dll']), ((1, 'hwnd'),(1, 'hInstance'),(1, 'pszParms'),(1, 'nShow'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UserUnInstStubWrapperW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.HINSTANCE,win32more.Foundation.PWSTR,Int32)(('UserUnInstStubWrapperW', windll['ADVPACK.dll']), ((1, 'hwnd'),(1, 'hInstance'),(1, 'pszParms'),(1, 'nShow'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetPerUserSecValuesA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsProgramming.PERUSERSECTIONA_head))(('SetPerUserSecValuesA', windll['ADVPACK.dll']), ((1, 'pPerUser'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetPerUserSecValuesW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsProgramming.PERUSERSECTIONW_head))(('SetPerUserSecValuesW', windll['ADVPACK.dll']), ((1, 'pPerUser'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SendIMEMessageExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.LRESULT,win32more.Foundation.HWND,win32more.Foundation.LPARAM)(('SendIMEMessageExA', windll['USER32.dll']), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SendIMEMessageExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.LRESULT,win32more.Foundation.HWND,win32more.Foundation.LPARAM)(('SendIMEMessageExW', windll['USER32.dll']), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IMPGetIMEA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,POINTER(win32more.System.WindowsProgramming.IMEPROA_head))(('IMPGetIMEA', windll['USER32.dll']), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IMPGetIMEW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,POINTER(win32more.System.WindowsProgramming.IMEPROW_head))(('IMPGetIMEW', windll['USER32.dll']), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IMPQueryIMEA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.WindowsProgramming.IMEPROA_head))(('IMPQueryIMEA', windll['USER32.dll']), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IMPQueryIMEW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.WindowsProgramming.IMEPROW_head))(('IMPQueryIMEW', windll['USER32.dll']), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IMPSetIMEA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,POINTER(win32more.System.WindowsProgramming.IMEPROA_head))(('IMPSetIMEA', windll['USER32.dll']), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IMPSetIMEW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,POINTER(win32more.System.WindowsProgramming.IMEPROW_head))(('IMPSetIMEW', windll['USER32.dll']), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WINNLSGetIMEHotkey():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HWND)(('WINNLSGetIMEHotkey', windll['USER32.dll']), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WINNLSEnableIME():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,win32more.Foundation.BOOL)(('WINNLSEnableIME', windll['USER32.dll']), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WINNLSGetEnableStatus():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND)(('WINNLSGetEnableStatus', windll['USER32.dll']), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ApphelpCheckShellObject():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(Guid),win32more.Foundation.BOOL,POINTER(UInt64))(('ApphelpCheckShellObject', windll['APPHELP.dll']), ((1, 'ObjectCLSID'),(1, 'bShimIfNecessary'),(1, 'pullFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WldpGetLockdownPolicy():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsProgramming.WLDP_HOST_INFORMATION_head),POINTER(UInt32),UInt32)(('WldpGetLockdownPolicy', windll['Wldp.dll']), ((1, 'hostInformation'),(1, 'lockdownState'),(1, 'lockdownFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WldpIsClassInApprovedList():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.System.WindowsProgramming.WLDP_HOST_INFORMATION_head),POINTER(win32more.Foundation.BOOL),UInt32)(('WldpIsClassInApprovedList', windll['Wldp.dll']), ((1, 'classID'),(1, 'hostInformation'),(1, 'isApproved'),(1, 'optionalFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WldpSetDynamicCodeTrust():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE)(('WldpSetDynamicCodeTrust', windll['Wldp.dll']), ((1, 'fileHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WldpIsDynamicCodePolicyEnabled():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(('WldpIsDynamicCodePolicyEnabled', windll['Wldp.dll']), ((1, 'isEnabled'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WldpQueryDynamicCodeTrust():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,c_void_p,UInt32)(('WldpQueryDynamicCodeTrust', windll['Wldp.dll']), ((1, 'fileHandle'),(1, 'baseImage'),(1, 'imageSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WldpQueryDeviceSecurityInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsProgramming.WLDP_DEVICE_SECURITY_INFORMATION_head),UInt32,POINTER(UInt32))(('WldpQueryDeviceSecurityInformation', windll['Wldp.dll']), ((1, 'information'),(1, 'informationLength'),(1, 'returnLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_APPLICATION_RECOVERY_CALLBACK():
    return WINFUNCTYPE(UInt32,c_void_p)
def _define_CABINFOA_head():
    class CABINFOA(Structure):
        pass
    return CABINFOA
def _define_CABINFOA():
    CABINFOA = win32more.System.WindowsProgramming.CABINFOA_head
    CABINFOA._fields_ = [
        ('pszCab', win32more.Foundation.PSTR),
        ('pszInf', win32more.Foundation.PSTR),
        ('pszSection', win32more.Foundation.PSTR),
        ('szSrcPath', win32more.Foundation.CHAR * 260),
        ('dwFlags', UInt32),
    ]
    return CABINFOA
def _define_CABINFOW_head():
    class CABINFOW(Structure):
        pass
    return CABINFOW
def _define_CABINFOW():
    CABINFOW = win32more.System.WindowsProgramming.CABINFOW_head
    CABINFOW._fields_ = [
        ('pszCab', win32more.Foundation.PWSTR),
        ('pszInf', win32more.Foundation.PWSTR),
        ('pszSection', win32more.Foundation.PWSTR),
        ('szSrcPath', Char * 260),
        ('dwFlags', UInt32),
    ]
    return CABINFOW
CameraUIControl = Guid('16d5a2be-b1c5-47b3-8e-ae-cc-bc-f4-52-c7-e8')
CameraUIControlCaptureMode = Int32
CameraUIControlCaptureMode_PhotoOrVideo = 0
CameraUIControlCaptureMode_Photo = 1
CameraUIControlCaptureMode_Video = 2
CameraUIControlLinearSelectionMode = Int32
CameraUIControlLinearSelectionMode_Single = 0
CameraUIControlLinearSelectionMode_Multiple = 1
CameraUIControlMode = Int32
CameraUIControlMode_Browse = 0
CameraUIControlMode_Linear = 1
CameraUIControlPhotoFormat = Int32
CameraUIControlPhotoFormat_Jpeg = 0
CameraUIControlPhotoFormat_Png = 1
CameraUIControlPhotoFormat_JpegXR = 2
CameraUIControlVideoFormat = Int32
CameraUIControlVideoFormat_Mp4 = 0
CameraUIControlVideoFormat_Wmv = 1
CameraUIControlViewType = Int32
CameraUIControlViewType_SingleItem = 0
CameraUIControlViewType_ItemList = 1
def _define_CLIENT_ID_head():
    class CLIENT_ID(Structure):
        pass
    return CLIENT_ID
def _define_CLIENT_ID():
    CLIENT_ID = win32more.System.WindowsProgramming.CLIENT_ID_head
    CLIENT_ID._fields_ = [
        ('UniqueProcess', win32more.Foundation.HANDLE),
        ('UniqueThread', win32more.Foundation.HANDLE),
    ]
    return CLIENT_ID
def _define_CUSTOM_SYSTEM_EVENT_TRIGGER_CONFIG_head():
    class CUSTOM_SYSTEM_EVENT_TRIGGER_CONFIG(Structure):
        pass
    return CUSTOM_SYSTEM_EVENT_TRIGGER_CONFIG
def _define_CUSTOM_SYSTEM_EVENT_TRIGGER_CONFIG():
    CUSTOM_SYSTEM_EVENT_TRIGGER_CONFIG = win32more.System.WindowsProgramming.CUSTOM_SYSTEM_EVENT_TRIGGER_CONFIG_head
    CUSTOM_SYSTEM_EVENT_TRIGGER_CONFIG._fields_ = [
        ('Size', UInt32),
        ('TriggerId', win32more.Foundation.PWSTR),
    ]
    return CUSTOM_SYSTEM_EVENT_TRIGGER_CONFIG
def _define_DATETIME_head():
    class DATETIME(Structure):
        pass
    return DATETIME
def _define_DATETIME():
    DATETIME = win32more.System.WindowsProgramming.DATETIME_head
    DATETIME._fields_ = [
        ('year', UInt16),
        ('month', UInt16),
        ('day', UInt16),
        ('hour', UInt16),
        ('min', UInt16),
        ('sec', UInt16),
    ]
    return DATETIME
def _define_DCICMD_head():
    class DCICMD(Structure):
        pass
    return DCICMD
def _define_DCICMD():
    DCICMD = win32more.System.WindowsProgramming.DCICMD_head
    DCICMD._fields_ = [
        ('dwCommand', UInt32),
        ('dwParam1', UInt32),
        ('dwParam2', UInt32),
        ('dwVersion', UInt32),
        ('dwReserved', UInt32),
    ]
    return DCICMD
def _define_DCICREATEINPUT_head():
    class DCICREATEINPUT(Structure):
        pass
    return DCICREATEINPUT
def _define_DCICREATEINPUT():
    DCICREATEINPUT = win32more.System.WindowsProgramming.DCICREATEINPUT_head
    DCICREATEINPUT._fields_ = [
        ('cmd', win32more.System.WindowsProgramming.DCICMD),
        ('dwCompression', UInt32),
        ('dwMask', UInt32 * 3),
        ('dwWidth', UInt32),
        ('dwHeight', UInt32),
        ('dwDCICaps', UInt32),
        ('dwBitCount', UInt32),
        ('lpSurface', c_void_p),
    ]
    return DCICREATEINPUT
def _define_DCIENUMINPUT_head():
    class DCIENUMINPUT(Structure):
        pass
    return DCIENUMINPUT
def _define_DCIENUMINPUT():
    DCIENUMINPUT = win32more.System.WindowsProgramming.DCIENUMINPUT_head
    DCIENUMINPUT._fields_ = [
        ('cmd', win32more.System.WindowsProgramming.DCICMD),
        ('rSrc', win32more.Foundation.RECT),
        ('rDst', win32more.Foundation.RECT),
        ('EnumCallback', IntPtr),
        ('lpContext', c_void_p),
    ]
    return DCIENUMINPUT
def _define_DCIOFFSCREEN_head():
    class DCIOFFSCREEN(Structure):
        pass
    return DCIOFFSCREEN
def _define_DCIOFFSCREEN():
    DCIOFFSCREEN = win32more.System.WindowsProgramming.DCIOFFSCREEN_head
    DCIOFFSCREEN._fields_ = [
        ('dciInfo', win32more.System.WindowsProgramming.DCISURFACEINFO),
        ('Draw', IntPtr),
        ('SetClipList', IntPtr),
        ('SetDestination', IntPtr),
    ]
    return DCIOFFSCREEN
def _define_DCIOVERLAY_head():
    class DCIOVERLAY(Structure):
        pass
    return DCIOVERLAY
def _define_DCIOVERLAY():
    DCIOVERLAY = win32more.System.WindowsProgramming.DCIOVERLAY_head
    DCIOVERLAY._fields_ = [
        ('dciInfo', win32more.System.WindowsProgramming.DCISURFACEINFO),
        ('dwChromakeyValue', UInt32),
        ('dwChromakeyMask', UInt32),
    ]
    return DCIOVERLAY
def _define_DCISURFACEINFO_head():
    class DCISURFACEINFO(Structure):
        pass
    return DCISURFACEINFO
def _define_DCISURFACEINFO():
    DCISURFACEINFO = win32more.System.WindowsProgramming.DCISURFACEINFO_head
    DCISURFACEINFO._fields_ = [
        ('dwSize', UInt32),
        ('dwDCICaps', UInt32),
        ('dwCompression', UInt32),
        ('dwMask', UInt32 * 3),
        ('dwWidth', UInt32),
        ('dwHeight', UInt32),
        ('lStride', Int32),
        ('dwBitCount', UInt32),
        ('dwOffSurface', UIntPtr),
        ('wSelSurface', UInt16),
        ('wReserved', UInt16),
        ('dwReserved1', UInt32),
        ('dwReserved2', UInt32),
        ('dwReserved3', UInt32),
        ('BeginAccess', IntPtr),
        ('EndAccess', IntPtr),
        ('DestroySurface', IntPtr),
    ]
    return DCISURFACEINFO
DECISION_LOCATION = Int32
DECISION_LOCATION_REFRESH_GLOBAL_DATA = 0
DECISION_LOCATION_PARAMETER_VALIDATION = 1
DECISION_LOCATION_AUDIT = 2
DECISION_LOCATION_FAILED_CONVERT_GUID = 3
DECISION_LOCATION_ENTERPRISE_DEFINED_CLASS_ID = 4
DECISION_LOCATION_GLOBAL_BUILT_IN_LIST = 5
DECISION_LOCATION_PROVIDER_BUILT_IN_LIST = 6
DECISION_LOCATION_ENFORCE_STATE_LIST = 7
DECISION_LOCATION_NOT_FOUND = 8
DECISION_LOCATION_UNKNOWN = 9
DefaultBrowserSyncSettings = Guid('3ac83423-3112-4aa6-9b-5b-1f-eb-23-d0-c5-f9')
def _define_DELAYLOAD_INFO_head():
    class DELAYLOAD_INFO(Structure):
        pass
    return DELAYLOAD_INFO
def _define_DELAYLOAD_INFO():
    DELAYLOAD_INFO = win32more.System.WindowsProgramming.DELAYLOAD_INFO_head
    DELAYLOAD_INFO._fields_ = [
        ('Size', UInt32),
        ('DelayloadDescriptor', POINTER(win32more.System.WindowsProgramming.IMAGE_DELAYLOAD_DESCRIPTOR_head)),
        ('ThunkAddress', POINTER(win32more.System.WindowsProgramming.IMAGE_THUNK_DATA64_head)),
        ('TargetDllName', win32more.Foundation.PSTR),
        ('TargetApiDescriptor', win32more.System.WindowsProgramming.DELAYLOAD_PROC_DESCRIPTOR),
        ('TargetModuleBase', c_void_p),
        ('Unused', c_void_p),
        ('LastError', UInt32),
    ]
    return DELAYLOAD_INFO
def _define_DELAYLOAD_PROC_DESCRIPTOR_head():
    class DELAYLOAD_PROC_DESCRIPTOR(Structure):
        pass
    return DELAYLOAD_PROC_DESCRIPTOR
def _define_DELAYLOAD_PROC_DESCRIPTOR():
    DELAYLOAD_PROC_DESCRIPTOR = win32more.System.WindowsProgramming.DELAYLOAD_PROC_DESCRIPTOR_head
    class DELAYLOAD_PROC_DESCRIPTOR__Description_e__Union(Union):
        pass
    DELAYLOAD_PROC_DESCRIPTOR__Description_e__Union._fields_ = [
        ('Name', win32more.Foundation.PSTR),
        ('Ordinal', UInt32),
    ]
    DELAYLOAD_PROC_DESCRIPTOR._fields_ = [
        ('ImportDescribedByName', UInt32),
        ('Description', DELAYLOAD_PROC_DESCRIPTOR__Description_e__Union),
    ]
    return DELAYLOAD_PROC_DESCRIPTOR
EditionUpgradeBroker = Guid('c4270827-4f39-45df-92-88-12-ff-6b-85-a9-21')
EditionUpgradeHelper = Guid('01776df3-b9af-4e50-9b-1c-56-e9-31-16-d7-04')
def _define_ENUM_CALLBACK():
    return WINFUNCTYPE(Void,POINTER(win32more.System.WindowsProgramming.DCISURFACEINFO_head),c_void_p)
FEATURE_CHANGE_TIME = Int32
FEATURE_CHANGE_TIME_READ = 0
FEATURE_CHANGE_TIME_MODULE_RELOAD = 1
FEATURE_CHANGE_TIME_SESSION = 2
FEATURE_CHANGE_TIME_REBOOT = 3
FEATURE_ENABLED_STATE = Int32
FEATURE_ENABLED_STATE_DEFAULT = 0
FEATURE_ENABLED_STATE_DISABLED = 1
FEATURE_ENABLED_STATE_ENABLED = 2
def _define_FEATURE_ERROR_head():
    class FEATURE_ERROR(Structure):
        pass
    return FEATURE_ERROR
def _define_FEATURE_ERROR():
    FEATURE_ERROR = win32more.System.WindowsProgramming.FEATURE_ERROR_head
    FEATURE_ERROR._fields_ = [
        ('hr', win32more.Foundation.HRESULT),
        ('lineNumber', UInt16),
        ('file', win32more.Foundation.PSTR),
        ('process', win32more.Foundation.PSTR),
        ('module', win32more.Foundation.PSTR),
        ('callerReturnAddressOffset', UInt32),
        ('callerModule', win32more.Foundation.PSTR),
        ('message', win32more.Foundation.PSTR),
        ('originLineNumber', UInt16),
        ('originFile', win32more.Foundation.PSTR),
        ('originModule', win32more.Foundation.PSTR),
        ('originCallerReturnAddressOffset', UInt32),
        ('originCallerModule', win32more.Foundation.PSTR),
        ('originName', win32more.Foundation.PSTR),
    ]
    return FEATURE_ERROR
FEATURE_STATE_CHANGE_SUBSCRIPTION = IntPtr
FH_SERVICE_PIPE_HANDLE = IntPtr
def _define_FILE_CASE_SENSITIVE_INFO_head():
    class FILE_CASE_SENSITIVE_INFO(Structure):
        pass
    return FILE_CASE_SENSITIVE_INFO
def _define_FILE_CASE_SENSITIVE_INFO():
    FILE_CASE_SENSITIVE_INFO = win32more.System.WindowsProgramming.FILE_CASE_SENSITIVE_INFO_head
    FILE_CASE_SENSITIVE_INFO._fields_ = [
        ('Flags', UInt32),
    ]
    return FILE_CASE_SENSITIVE_INFO
def _define_FILE_DISPOSITION_INFO_EX_head():
    class FILE_DISPOSITION_INFO_EX(Structure):
        pass
    return FILE_DISPOSITION_INFO_EX
def _define_FILE_DISPOSITION_INFO_EX():
    FILE_DISPOSITION_INFO_EX = win32more.System.WindowsProgramming.FILE_DISPOSITION_INFO_EX_head
    FILE_DISPOSITION_INFO_EX._fields_ = [
        ('Flags', UInt32),
    ]
    return FILE_DISPOSITION_INFO_EX
FILE_INFORMATION_CLASS = Int32
FILE_INFORMATION_CLASS_FileDirectoryInformation = 1
def _define_HW_PROFILE_INFOA_head():
    class HW_PROFILE_INFOA(Structure):
        pass
    return HW_PROFILE_INFOA
def _define_HW_PROFILE_INFOA():
    HW_PROFILE_INFOA = win32more.System.WindowsProgramming.HW_PROFILE_INFOA_head
    HW_PROFILE_INFOA._fields_ = [
        ('dwDockInfo', UInt32),
        ('szHwProfileGuid', win32more.Foundation.CHAR * 39),
        ('szHwProfileName', win32more.Foundation.CHAR * 80),
    ]
    return HW_PROFILE_INFOA
def _define_HW_PROFILE_INFOW_head():
    class HW_PROFILE_INFOW(Structure):
        pass
    return HW_PROFILE_INFOW
def _define_HW_PROFILE_INFOW():
    HW_PROFILE_INFOW = win32more.System.WindowsProgramming.HW_PROFILE_INFOW_head
    HW_PROFILE_INFOW._fields_ = [
        ('dwDockInfo', UInt32),
        ('szHwProfileGuid', Char * 39),
        ('szHwProfileName', Char * 80),
    ]
    return HW_PROFILE_INFOW
HWINWATCH = IntPtr
def _define_ICameraUIControl_head():
    class ICameraUIControl(win32more.System.Com.IUnknown_head):
        Guid = Guid('b8733adf-3d68-4b8f-bb-08-e2-8a-0b-ed-03-76')
    return ICameraUIControl
def _define_ICameraUIControl():
    ICameraUIControl = win32more.System.WindowsProgramming.ICameraUIControl_head
    ICameraUIControl.Show = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.System.WindowsProgramming.CameraUIControlMode,win32more.System.WindowsProgramming.CameraUIControlLinearSelectionMode,win32more.System.WindowsProgramming.CameraUIControlCaptureMode,win32more.System.WindowsProgramming.CameraUIControlPhotoFormat,win32more.System.WindowsProgramming.CameraUIControlVideoFormat,win32more.Foundation.BOOL,win32more.System.WindowsProgramming.ICameraUIControlEventCallback_head)(3, 'Show', ((1, 'pWindow'),(1, 'mode'),(1, 'selectionMode'),(1, 'captureMode'),(1, 'photoFormat'),(1, 'videoFormat'),(1, 'bHasCloseButton'),(1, 'pEventCallback'),)))
    ICameraUIControl.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'Close', ()))
    ICameraUIControl.Suspend = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(5, 'Suspend', ((1, 'pbDeferralRequired'),)))
    ICameraUIControl.Resume = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(6, 'Resume', ()))
    ICameraUIControl.GetCurrentViewType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsProgramming.CameraUIControlViewType))(7, 'GetCurrentViewType', ((1, 'pViewType'),)))
    ICameraUIControl.GetActiveItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(8, 'GetActiveItem', ((1, 'pbstrActiveItemPath'),)))
    ICameraUIControl.GetSelectedItems = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(9, 'GetSelectedItems', ((1, 'ppSelectedItemPaths'),)))
    ICameraUIControl.RemoveCapturedItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(10, 'RemoveCapturedItem', ((1, 'pszPath'),)))
    win32more.System.Com.IUnknown
    return ICameraUIControl
def _define_ICameraUIControlEventCallback_head():
    class ICameraUIControlEventCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('1bfa0c2c-fbcd-4776-bd-a4-88-bf-97-4e-74-f4')
    return ICameraUIControlEventCallback
def _define_ICameraUIControlEventCallback():
    ICameraUIControlEventCallback = win32more.System.WindowsProgramming.ICameraUIControlEventCallback_head
    ICameraUIControlEventCallback.OnStartupComplete = COMMETHOD(WINFUNCTYPE(Void,)(3, 'OnStartupComplete', ()))
    ICameraUIControlEventCallback.OnSuspendComplete = COMMETHOD(WINFUNCTYPE(Void,)(4, 'OnSuspendComplete', ()))
    ICameraUIControlEventCallback.OnItemCaptured = COMMETHOD(WINFUNCTYPE(Void,win32more.Foundation.PWSTR)(5, 'OnItemCaptured', ((1, 'pszPath'),)))
    ICameraUIControlEventCallback.OnItemDeleted = COMMETHOD(WINFUNCTYPE(Void,win32more.Foundation.PWSTR)(6, 'OnItemDeleted', ((1, 'pszPath'),)))
    ICameraUIControlEventCallback.OnClosed = COMMETHOD(WINFUNCTYPE(Void,)(7, 'OnClosed', ()))
    win32more.System.Com.IUnknown
    return ICameraUIControlEventCallback
def _define_IClipServiceNotificationHelper_head():
    class IClipServiceNotificationHelper(win32more.System.Com.IUnknown_head):
        Guid = Guid('c39948f0-6142-44fd-98-ca-e1-68-1a-8d-68-b5')
    return IClipServiceNotificationHelper
def _define_IClipServiceNotificationHelper():
    IClipServiceNotificationHelper = win32more.System.WindowsProgramming.IClipServiceNotificationHelper_head
    IClipServiceNotificationHelper.ShowToast = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR)(3, 'ShowToast', ((1, 'titleText'),(1, 'bodyText'),(1, 'packageName'),(1, 'appId'),(1, 'launchCommand'),)))
    win32more.System.Com.IUnknown
    return IClipServiceNotificationHelper
def _define_IContainerActivationHelper_head():
    class IContainerActivationHelper(win32more.System.Com.IUnknown_head):
        Guid = Guid('b524f93f-80d5-4ec7-ae-9e-d6-6e-93-ad-e1-fa')
    return IContainerActivationHelper
def _define_IContainerActivationHelper():
    IContainerActivationHelper = win32more.System.WindowsProgramming.IContainerActivationHelper_head
    IContainerActivationHelper.CanActivateClientVM = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(3, 'CanActivateClientVM', ((1, 'isAllowed'),)))
    win32more.System.Com.IUnknown
    return IContainerActivationHelper
def _define_IDefaultBrowserSyncSettings_head():
    class IDefaultBrowserSyncSettings(win32more.System.Com.IUnknown_head):
        Guid = Guid('7a27faad-5ae6-4255-90-30-c5-30-93-62-92-e3')
    return IDefaultBrowserSyncSettings
def _define_IDefaultBrowserSyncSettings():
    IDefaultBrowserSyncSettings = win32more.System.WindowsProgramming.IDefaultBrowserSyncSettings_head
    IDefaultBrowserSyncSettings.IsEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,)(3, 'IsEnabled', ()))
    win32more.System.Com.IUnknown
    return IDefaultBrowserSyncSettings
def _define_IDeleteBrowsingHistory_head():
    class IDeleteBrowsingHistory(win32more.System.Com.IUnknown_head):
        Guid = Guid('cf38ed4b-2be7-4461-8b-5e-9a-46-6d-c8-2a-e3')
    return IDeleteBrowsingHistory
def _define_IDeleteBrowsingHistory():
    IDeleteBrowsingHistory = win32more.System.WindowsProgramming.IDeleteBrowsingHistory_head
    IDeleteBrowsingHistory.DeleteBrowsingHistory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(3, 'DeleteBrowsingHistory', ((1, 'dwFlags'),)))
    win32more.System.Com.IUnknown
    return IDeleteBrowsingHistory
def _define_IEditionUpgradeBroker_head():
    class IEditionUpgradeBroker(win32more.System.Com.IUnknown_head):
        Guid = Guid('ff19cbcf-9455-4937-b8-72-6b-79-29-a4-60-af')
    return IEditionUpgradeBroker
def _define_IEditionUpgradeBroker():
    IEditionUpgradeBroker = win32more.System.WindowsProgramming.IEditionUpgradeBroker_head
    IEditionUpgradeBroker.InitializeParentWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Ole.OLE_HANDLE)(3, 'InitializeParentWindow', ((1, 'parentHandle'),)))
    IEditionUpgradeBroker.UpdateOperatingSystem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(4, 'UpdateOperatingSystem', ((1, 'parameter'),)))
    IEditionUpgradeBroker.ShowProductKeyUI = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'ShowProductKeyUI', ()))
    IEditionUpgradeBroker.CanUpgrade = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(6, 'CanUpgrade', ()))
    win32more.System.Com.IUnknown
    return IEditionUpgradeBroker
def _define_IEditionUpgradeHelper_head():
    class IEditionUpgradeHelper(win32more.System.Com.IUnknown_head):
        Guid = Guid('d3e9e342-5deb-43b6-84-9e-69-13-b8-5d-50-3a')
    return IEditionUpgradeHelper
def _define_IEditionUpgradeHelper():
    IEditionUpgradeHelper = win32more.System.WindowsProgramming.IEditionUpgradeHelper_head
    IEditionUpgradeHelper.CanUpgrade = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(3, 'CanUpgrade', ((1, 'isAllowed'),)))
    IEditionUpgradeHelper.UpdateOperatingSystem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(4, 'UpdateOperatingSystem', ((1, 'contentId'),)))
    IEditionUpgradeHelper.ShowProductKeyUI = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'ShowProductKeyUI', ()))
    IEditionUpgradeHelper.GetOsProductContentId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(6, 'GetOsProductContentId', ((1, 'contentId'),)))
    IEditionUpgradeHelper.GetGenuineLocalStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(7, 'GetGenuineLocalStatus', ((1, 'isGenuine'),)))
    win32more.System.Com.IUnknown
    return IEditionUpgradeHelper
def _define_IMAGE_DELAYLOAD_DESCRIPTOR_head():
    class IMAGE_DELAYLOAD_DESCRIPTOR(Structure):
        pass
    return IMAGE_DELAYLOAD_DESCRIPTOR
def _define_IMAGE_DELAYLOAD_DESCRIPTOR():
    IMAGE_DELAYLOAD_DESCRIPTOR = win32more.System.WindowsProgramming.IMAGE_DELAYLOAD_DESCRIPTOR_head
    class IMAGE_DELAYLOAD_DESCRIPTOR__Attributes_e__Union(Union):
        pass
    class IMAGE_DELAYLOAD_DESCRIPTOR__Attributes_e__Union__Anonymous_e__Struct(Structure):
        pass
    IMAGE_DELAYLOAD_DESCRIPTOR__Attributes_e__Union__Anonymous_e__Struct._fields_ = [
        ('_bitfield', UInt32),
    ]
    IMAGE_DELAYLOAD_DESCRIPTOR__Attributes_e__Union._anonymous_ = [
        'Anonymous',
    ]
    IMAGE_DELAYLOAD_DESCRIPTOR__Attributes_e__Union._fields_ = [
        ('AllAttributes', UInt32),
        ('Anonymous', IMAGE_DELAYLOAD_DESCRIPTOR__Attributes_e__Union__Anonymous_e__Struct),
    ]
    IMAGE_DELAYLOAD_DESCRIPTOR._fields_ = [
        ('Attributes', IMAGE_DELAYLOAD_DESCRIPTOR__Attributes_e__Union),
        ('DllNameRVA', UInt32),
        ('ModuleHandleRVA', UInt32),
        ('ImportAddressTableRVA', UInt32),
        ('ImportNameTableRVA', UInt32),
        ('BoundImportAddressTableRVA', UInt32),
        ('UnloadInformationTableRVA', UInt32),
        ('TimeDateStamp', UInt32),
    ]
    return IMAGE_DELAYLOAD_DESCRIPTOR
def _define_IMAGE_THUNK_DATA32_head():
    class IMAGE_THUNK_DATA32(Structure):
        pass
    return IMAGE_THUNK_DATA32
def _define_IMAGE_THUNK_DATA32():
    IMAGE_THUNK_DATA32 = win32more.System.WindowsProgramming.IMAGE_THUNK_DATA32_head
    class IMAGE_THUNK_DATA32__u1_e__Union(Union):
        pass
    IMAGE_THUNK_DATA32__u1_e__Union._fields_ = [
        ('ForwarderString', UInt32),
        ('Function', UInt32),
        ('Ordinal', UInt32),
        ('AddressOfData', UInt32),
    ]
    IMAGE_THUNK_DATA32._fields_ = [
        ('u1', IMAGE_THUNK_DATA32__u1_e__Union),
    ]
    return IMAGE_THUNK_DATA32
def _define_IMAGE_THUNK_DATA64_head():
    class IMAGE_THUNK_DATA64(Structure):
        pass
    return IMAGE_THUNK_DATA64
def _define_IMAGE_THUNK_DATA64():
    IMAGE_THUNK_DATA64 = win32more.System.WindowsProgramming.IMAGE_THUNK_DATA64_head
    class IMAGE_THUNK_DATA64__u1_e__Union(Union):
        pass
    IMAGE_THUNK_DATA64__u1_e__Union._fields_ = [
        ('ForwarderString', UInt64),
        ('Function', UInt64),
        ('Ordinal', UInt64),
        ('AddressOfData', UInt64),
    ]
    IMAGE_THUNK_DATA64._fields_ = [
        ('u1', IMAGE_THUNK_DATA64__u1_e__Union),
    ]
    return IMAGE_THUNK_DATA64
def _define_IMEPROA_head():
    class IMEPROA(Structure):
        pass
    return IMEPROA
def _define_IMEPROA():
    IMEPROA = win32more.System.WindowsProgramming.IMEPROA_head
    IMEPROA._fields_ = [
        ('hWnd', win32more.Foundation.HWND),
        ('InstDate', win32more.System.WindowsProgramming.DATETIME),
        ('wVersion', UInt32),
        ('szDescription', Byte * 50),
        ('szName', Byte * 80),
        ('szOptions', Byte * 30),
    ]
    return IMEPROA
def _define_IMEPROW_head():
    class IMEPROW(Structure):
        pass
    return IMEPROW
def _define_IMEPROW():
    IMEPROW = win32more.System.WindowsProgramming.IMEPROW_head
    IMEPROW._fields_ = [
        ('hWnd', win32more.Foundation.HWND),
        ('InstDate', win32more.System.WindowsProgramming.DATETIME),
        ('wVersion', UInt32),
        ('szDescription', Char * 50),
        ('szName', Char * 80),
        ('szOptions', Char * 30),
    ]
    return IMEPROW
def _define_IMESTRUCT_head():
    class IMESTRUCT(Structure):
        pass
    return IMESTRUCT
def _define_IMESTRUCT():
    IMESTRUCT = win32more.System.WindowsProgramming.IMESTRUCT_head
    IMESTRUCT._fields_ = [
        ('fnc', UInt32),
        ('wParam', win32more.Foundation.WPARAM),
        ('wCount', UInt32),
        ('dchSource', UInt32),
        ('dchDest', UInt32),
        ('lParam1', win32more.Foundation.LPARAM),
        ('lParam2', win32more.Foundation.LPARAM),
        ('lParam3', win32more.Foundation.LPARAM),
    ]
    return IMESTRUCT
def _define_IO_STATUS_BLOCK_head():
    class IO_STATUS_BLOCK(Structure):
        pass
    return IO_STATUS_BLOCK
def _define_IO_STATUS_BLOCK():
    IO_STATUS_BLOCK = win32more.System.WindowsProgramming.IO_STATUS_BLOCK_head
    class IO_STATUS_BLOCK__Anonymous_e__Union(Union):
        pass
    IO_STATUS_BLOCK__Anonymous_e__Union._fields_ = [
        ('Status', win32more.Foundation.NTSTATUS),
        ('Pointer', c_void_p),
    ]
    IO_STATUS_BLOCK._anonymous_ = [
        'Anonymous',
    ]
    IO_STATUS_BLOCK._fields_ = [
        ('Anonymous', IO_STATUS_BLOCK__Anonymous_e__Union),
        ('Information', UIntPtr),
    ]
    return IO_STATUS_BLOCK
def _define_IWindowsLockModeHelper_head():
    class IWindowsLockModeHelper(win32more.System.Com.IUnknown_head):
        Guid = Guid('f342d19e-cc22-4648-bb-5d-03-cc-f7-5b-47-c5')
    return IWindowsLockModeHelper
def _define_IWindowsLockModeHelper():
    IWindowsLockModeHelper = win32more.System.WindowsProgramming.IWindowsLockModeHelper_head
    IWindowsLockModeHelper.GetSMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(3, 'GetSMode', ((1, 'isSmode'),)))
    win32more.System.Com.IUnknown
    return IWindowsLockModeHelper
def _define_JAVA_TRUST_head():
    class JAVA_TRUST(Structure):
        pass
    return JAVA_TRUST
def _define_JAVA_TRUST():
    JAVA_TRUST = win32more.System.WindowsProgramming.JAVA_TRUST_head
    JAVA_TRUST._fields_ = [
        ('cbSize', UInt32),
        ('flag', UInt32),
        ('fAllActiveXPermissions', win32more.Foundation.BOOL),
        ('fAllPermissions', win32more.Foundation.BOOL),
        ('dwEncodingType', UInt32),
        ('pbJavaPermissions', c_char_p_no),
        ('cbJavaPermissions', UInt32),
        ('pbSigner', c_char_p_no),
        ('cbSigner', UInt32),
        ('pwszZone', win32more.Foundation.PWSTR),
        ('guidZone', Guid),
        ('hVerify', win32more.Foundation.HRESULT),
    ]
    return JAVA_TRUST
def _define_JIT_DEBUG_INFO_head():
    class JIT_DEBUG_INFO(Structure):
        pass
    return JIT_DEBUG_INFO
def _define_JIT_DEBUG_INFO():
    JIT_DEBUG_INFO = win32more.System.WindowsProgramming.JIT_DEBUG_INFO_head
    JIT_DEBUG_INFO._fields_ = [
        ('dwSize', UInt32),
        ('dwProcessorArchitecture', UInt32),
        ('dwThreadID', UInt32),
        ('dwReserved0', UInt32),
        ('lpExceptionAddress', UInt64),
        ('lpExceptionRecord', UInt64),
        ('lpContextRecord', UInt64),
    ]
    return JIT_DEBUG_INFO
KEY_SET_INFORMATION_CLASS = Int32
KEY_SET_INFORMATION_CLASS_KeyWriteTimeInformation = 0
KEY_SET_INFORMATION_CLASS_KeyWow64FlagsInformation = 1
KEY_SET_INFORMATION_CLASS_KeyControlFlagsInformation = 2
KEY_SET_INFORMATION_CLASS_KeySetVirtualizationInformation = 3
KEY_SET_INFORMATION_CLASS_KeySetDebugInformation = 4
KEY_SET_INFORMATION_CLASS_KeySetHandleTagsInformation = 5
KEY_SET_INFORMATION_CLASS_MaxKeySetInfoClass = 6
def _define_KEY_VALUE_ENTRY_head():
    class KEY_VALUE_ENTRY(Structure):
        pass
    return KEY_VALUE_ENTRY
def _define_KEY_VALUE_ENTRY():
    KEY_VALUE_ENTRY = win32more.System.WindowsProgramming.KEY_VALUE_ENTRY_head
    KEY_VALUE_ENTRY._fields_ = [
        ('ValueName', POINTER(win32more.Foundation.UNICODE_STRING_head)),
        ('DataLength', UInt32),
        ('DataOffset', UInt32),
        ('Type', UInt32),
    ]
    return KEY_VALUE_ENTRY
def _define_LDR_DATA_TABLE_ENTRY_head():
    class LDR_DATA_TABLE_ENTRY(Structure):
        pass
    return LDR_DATA_TABLE_ENTRY
def _define_LDR_DATA_TABLE_ENTRY():
    LDR_DATA_TABLE_ENTRY = win32more.System.WindowsProgramming.LDR_DATA_TABLE_ENTRY_head
    class LDR_DATA_TABLE_ENTRY__Anonymous_e__Union(Union):
        pass
    LDR_DATA_TABLE_ENTRY__Anonymous_e__Union._fields_ = [
        ('CheckSum', UInt32),
        ('Reserved6', c_void_p),
    ]
    LDR_DATA_TABLE_ENTRY._anonymous_ = [
        'Anonymous',
    ]
    LDR_DATA_TABLE_ENTRY._fields_ = [
        ('Reserved1', c_void_p * 2),
        ('InMemoryOrderLinks', win32more.System.Kernel.LIST_ENTRY),
        ('Reserved2', c_void_p * 2),
        ('DllBase', c_void_p),
        ('Reserved3', c_void_p * 2),
        ('FullDllName', win32more.Foundation.UNICODE_STRING),
        ('Reserved4', Byte * 8),
        ('Reserved5', c_void_p * 3),
        ('Anonymous', LDR_DATA_TABLE_ENTRY__Anonymous_e__Union),
        ('TimeDateStamp', UInt32),
    ]
    return LDR_DATA_TABLE_ENTRY
def _define_OBJECT_ATTRIBUTES_head():
    class OBJECT_ATTRIBUTES(Structure):
        pass
    return OBJECT_ATTRIBUTES
def _define_OBJECT_ATTRIBUTES():
    OBJECT_ATTRIBUTES = win32more.System.WindowsProgramming.OBJECT_ATTRIBUTES_head
    OBJECT_ATTRIBUTES._fields_ = [
        ('Length', UInt32),
        ('RootDirectory', win32more.Foundation.HANDLE),
        ('ObjectName', POINTER(win32more.Foundation.UNICODE_STRING_head)),
        ('Attributes', UInt32),
        ('SecurityDescriptor', c_void_p),
        ('SecurityQualityOfService', c_void_p),
    ]
    return OBJECT_ATTRIBUTES
OBJECT_INFORMATION_CLASS = Int32
OBJECT_INFORMATION_CLASS_ObjectBasicInformation = 0
OBJECT_INFORMATION_CLASS_ObjectTypeInformation = 2
def _define_PDELAYLOAD_FAILURE_DLL_CALLBACK():
    return WINFUNCTYPE(c_void_p,UInt32,POINTER(win32more.System.WindowsProgramming.DELAYLOAD_INFO_head))
def _define_PERUSERSECTIONA_head():
    class PERUSERSECTIONA(Structure):
        pass
    return PERUSERSECTIONA
def _define_PERUSERSECTIONA():
    PERUSERSECTIONA = win32more.System.WindowsProgramming.PERUSERSECTIONA_head
    PERUSERSECTIONA._fields_ = [
        ('szGUID', win32more.Foundation.CHAR * 59),
        ('szDispName', win32more.Foundation.CHAR * 128),
        ('szLocale', win32more.Foundation.CHAR * 10),
        ('szStub', win32more.Foundation.CHAR * 1040),
        ('szVersion', win32more.Foundation.CHAR * 32),
        ('szCompID', win32more.Foundation.CHAR * 128),
        ('dwIsInstalled', UInt32),
        ('bRollback', win32more.Foundation.BOOL),
    ]
    return PERUSERSECTIONA
def _define_PERUSERSECTIONW_head():
    class PERUSERSECTIONW(Structure):
        pass
    return PERUSERSECTIONW
def _define_PERUSERSECTIONW():
    PERUSERSECTIONW = win32more.System.WindowsProgramming.PERUSERSECTIONW_head
    PERUSERSECTIONW._fields_ = [
        ('szGUID', Char * 59),
        ('szDispName', Char * 128),
        ('szLocale', Char * 10),
        ('szStub', Char * 1040),
        ('szVersion', Char * 32),
        ('szCompID', Char * 128),
        ('dwIsInstalled', UInt32),
        ('bRollback', win32more.Foundation.BOOL),
    ]
    return PERUSERSECTIONW
def _define_PFEATURE_STATE_CHANGE_CALLBACK():
    return WINFUNCTYPE(Void,c_void_p)
def _define_PFIBER_CALLOUT_ROUTINE():
    return WINFUNCTYPE(c_void_p,c_void_p)
def _define_PIO_APC_ROUTINE():
    return WINFUNCTYPE(Void,c_void_p,POINTER(win32more.System.WindowsProgramming.IO_STATUS_BLOCK_head),UInt32)
def _define_PQUERYACTCTXW_FUNC():
    return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.Foundation.HANDLE,c_void_p,UInt32,c_void_p,UIntPtr,POINTER(UIntPtr))
def _define_PUBLIC_OBJECT_BASIC_INFORMATION_head():
    class PUBLIC_OBJECT_BASIC_INFORMATION(Structure):
        pass
    return PUBLIC_OBJECT_BASIC_INFORMATION
def _define_PUBLIC_OBJECT_BASIC_INFORMATION():
    PUBLIC_OBJECT_BASIC_INFORMATION = win32more.System.WindowsProgramming.PUBLIC_OBJECT_BASIC_INFORMATION_head
    PUBLIC_OBJECT_BASIC_INFORMATION._fields_ = [
        ('Attributes', UInt32),
        ('GrantedAccess', UInt32),
        ('HandleCount', UInt32),
        ('PointerCount', UInt32),
        ('Reserved', UInt32 * 10),
    ]
    return PUBLIC_OBJECT_BASIC_INFORMATION
def _define_PUBLIC_OBJECT_TYPE_INFORMATION_head():
    class PUBLIC_OBJECT_TYPE_INFORMATION(Structure):
        pass
    return PUBLIC_OBJECT_TYPE_INFORMATION
def _define_PUBLIC_OBJECT_TYPE_INFORMATION():
    PUBLIC_OBJECT_TYPE_INFORMATION = win32more.System.WindowsProgramming.PUBLIC_OBJECT_TYPE_INFORMATION_head
    PUBLIC_OBJECT_TYPE_INFORMATION._fields_ = [
        ('TypeName', win32more.Foundation.UNICODE_STRING),
        ('Reserved', UInt32 * 22),
    ]
    return PUBLIC_OBJECT_TYPE_INFORMATION
def _define_PWINSTATIONQUERYINFORMATIONW():
    return WINFUNCTYPE(win32more.Foundation.BOOLEAN,win32more.Foundation.HANDLE,UInt32,win32more.System.WindowsProgramming.WINSTATIONINFOCLASS,c_void_p,UInt32,POINTER(UInt32))
def _define_PWLDP_ISAPPAPPROVEDBYPOLICY_API():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt64)
def _define_PWLDP_ISDYNAMICCODEPOLICYENABLED_API():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))
def _define_PWLDP_ISPRODUCTIONCONFIGURATION_API():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))
def _define_PWLDP_ISWCOSPRODUCTIONCONFIGURATION_API():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))
def _define_PWLDP_QUERYDEVICESECURITYINFORMATION_API():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsProgramming.WLDP_DEVICE_SECURITY_INFORMATION_head),UInt32,POINTER(UInt32))
def _define_PWLDP_QUERYDYNAMICODETRUST_API():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,c_void_p,UInt32)
def _define_PWLDP_QUERYPOLICYSETTINGENABLED_API():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsProgramming.WLDP_POLICY_SETTING,POINTER(win32more.Foundation.BOOL))
def _define_PWLDP_QUERYPOLICYSETTINGENABLED2_API():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.BOOL))
def _define_PWLDP_QUERYWINDOWSLOCKDOWNMODE_API():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsProgramming.WLDP_WINDOWS_LOCKDOWN_MODE))
def _define_PWLDP_QUERYWINDOWSLOCKDOWNRESTRICTION_API():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WindowsProgramming.WLDP_WINDOWS_LOCKDOWN_RESTRICTION))
def _define_PWLDP_RESETPRODUCTIONCONFIGURATION_API():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,)
def _define_PWLDP_RESETWCOSPRODUCTIONCONFIGURATION_API():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,)
def _define_PWLDP_SETDYNAMICCODETRUST_API():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE)
def _define_PWLDP_SETWINDOWSLOCKDOWNRESTRICTION_API():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsProgramming.WLDP_WINDOWS_LOCKDOWN_RESTRICTION)
def _define_REGINSTALLA():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HINSTANCE,win32more.Foundation.PSTR,POINTER(win32more.System.WindowsProgramming.STRTABLEA_head))
def _define_STRENTRYA_head():
    class STRENTRYA(Structure):
        pass
    return STRENTRYA
def _define_STRENTRYA():
    STRENTRYA = win32more.System.WindowsProgramming.STRENTRYA_head
    STRENTRYA._fields_ = [
        ('pszName', win32more.Foundation.PSTR),
        ('pszValue', win32more.Foundation.PSTR),
    ]
    return STRENTRYA
def _define_STRENTRYW_head():
    class STRENTRYW(Structure):
        pass
    return STRENTRYW
def _define_STRENTRYW():
    STRENTRYW = win32more.System.WindowsProgramming.STRENTRYW_head
    STRENTRYW._fields_ = [
        ('pszName', win32more.Foundation.PWSTR),
        ('pszValue', win32more.Foundation.PWSTR),
    ]
    return STRENTRYW
def _define_STRINGEXSTRUCT_head():
    class STRINGEXSTRUCT(Structure):
        pass
    return STRINGEXSTRUCT
def _define_STRINGEXSTRUCT():
    STRINGEXSTRUCT = win32more.System.WindowsProgramming.STRINGEXSTRUCT_head
    STRINGEXSTRUCT._fields_ = [
        ('dwSize', UInt32),
        ('uDeterminePos', UInt32),
        ('uDetermineDelimPos', UInt32),
        ('uYomiPos', UInt32),
        ('uYomiDelimPos', UInt32),
    ]
    return STRINGEXSTRUCT
def _define_STRTABLEA_head():
    class STRTABLEA(Structure):
        pass
    return STRTABLEA
def _define_STRTABLEA():
    STRTABLEA = win32more.System.WindowsProgramming.STRTABLEA_head
    STRTABLEA._fields_ = [
        ('cEntries', UInt32),
        ('pse', POINTER(win32more.System.WindowsProgramming.STRENTRYA_head)),
    ]
    return STRTABLEA
def _define_STRTABLEW_head():
    class STRTABLEW(Structure):
        pass
    return STRTABLEW
def _define_STRTABLEW():
    STRTABLEW = win32more.System.WindowsProgramming.STRTABLEW_head
    STRTABLEW._fields_ = [
        ('cEntries', UInt32),
        ('pse', POINTER(win32more.System.WindowsProgramming.STRENTRYW_head)),
    ]
    return STRTABLEW
def _define_SYSTEM_BASIC_INFORMATION_head():
    class SYSTEM_BASIC_INFORMATION(Structure):
        pass
    return SYSTEM_BASIC_INFORMATION
def _define_SYSTEM_BASIC_INFORMATION():
    SYSTEM_BASIC_INFORMATION = win32more.System.WindowsProgramming.SYSTEM_BASIC_INFORMATION_head
    SYSTEM_BASIC_INFORMATION._fields_ = [
        ('Reserved1', Byte * 24),
        ('Reserved2', c_void_p * 4),
        ('NumberOfProcessors', SByte),
    ]
    return SYSTEM_BASIC_INFORMATION
def _define_SYSTEM_CODEINTEGRITY_INFORMATION_head():
    class SYSTEM_CODEINTEGRITY_INFORMATION(Structure):
        pass
    return SYSTEM_CODEINTEGRITY_INFORMATION
def _define_SYSTEM_CODEINTEGRITY_INFORMATION():
    SYSTEM_CODEINTEGRITY_INFORMATION = win32more.System.WindowsProgramming.SYSTEM_CODEINTEGRITY_INFORMATION_head
    SYSTEM_CODEINTEGRITY_INFORMATION._fields_ = [
        ('Length', UInt32),
        ('CodeIntegrityOptions', UInt32),
    ]
    return SYSTEM_CODEINTEGRITY_INFORMATION
def _define_SYSTEM_EXCEPTION_INFORMATION_head():
    class SYSTEM_EXCEPTION_INFORMATION(Structure):
        pass
    return SYSTEM_EXCEPTION_INFORMATION
def _define_SYSTEM_EXCEPTION_INFORMATION():
    SYSTEM_EXCEPTION_INFORMATION = win32more.System.WindowsProgramming.SYSTEM_EXCEPTION_INFORMATION_head
    SYSTEM_EXCEPTION_INFORMATION._fields_ = [
        ('Reserved1', Byte * 16),
    ]
    return SYSTEM_EXCEPTION_INFORMATION
SYSTEM_INFORMATION_CLASS = Int32
SYSTEM_INFORMATION_CLASS_SystemBasicInformation = 0
SYSTEM_INFORMATION_CLASS_SystemPerformanceInformation = 2
SYSTEM_INFORMATION_CLASS_SystemTimeOfDayInformation = 3
SYSTEM_INFORMATION_CLASS_SystemProcessInformation = 5
SYSTEM_INFORMATION_CLASS_SystemProcessorPerformanceInformation = 8
SYSTEM_INFORMATION_CLASS_SystemInterruptInformation = 23
SYSTEM_INFORMATION_CLASS_SystemExceptionInformation = 33
SYSTEM_INFORMATION_CLASS_SystemRegistryQuotaInformation = 37
SYSTEM_INFORMATION_CLASS_SystemLookasideInformation = 45
SYSTEM_INFORMATION_CLASS_SystemCodeIntegrityInformation = 103
SYSTEM_INFORMATION_CLASS_SystemPolicyInformation = 134
def _define_SYSTEM_INTERRUPT_INFORMATION_head():
    class SYSTEM_INTERRUPT_INFORMATION(Structure):
        pass
    return SYSTEM_INTERRUPT_INFORMATION
def _define_SYSTEM_INTERRUPT_INFORMATION():
    SYSTEM_INTERRUPT_INFORMATION = win32more.System.WindowsProgramming.SYSTEM_INTERRUPT_INFORMATION_head
    SYSTEM_INTERRUPT_INFORMATION._fields_ = [
        ('Reserved1', Byte * 24),
    ]
    return SYSTEM_INTERRUPT_INFORMATION
def _define_SYSTEM_LOOKASIDE_INFORMATION_head():
    class SYSTEM_LOOKASIDE_INFORMATION(Structure):
        pass
    return SYSTEM_LOOKASIDE_INFORMATION
def _define_SYSTEM_LOOKASIDE_INFORMATION():
    SYSTEM_LOOKASIDE_INFORMATION = win32more.System.WindowsProgramming.SYSTEM_LOOKASIDE_INFORMATION_head
    SYSTEM_LOOKASIDE_INFORMATION._fields_ = [
        ('Reserved1', Byte * 32),
    ]
    return SYSTEM_LOOKASIDE_INFORMATION
def _define_SYSTEM_PERFORMANCE_INFORMATION_head():
    class SYSTEM_PERFORMANCE_INFORMATION(Structure):
        pass
    return SYSTEM_PERFORMANCE_INFORMATION
def _define_SYSTEM_PERFORMANCE_INFORMATION():
    SYSTEM_PERFORMANCE_INFORMATION = win32more.System.WindowsProgramming.SYSTEM_PERFORMANCE_INFORMATION_head
    SYSTEM_PERFORMANCE_INFORMATION._fields_ = [
        ('Reserved1', Byte * 312),
    ]
    return SYSTEM_PERFORMANCE_INFORMATION
def _define_SYSTEM_POLICY_INFORMATION_head():
    class SYSTEM_POLICY_INFORMATION(Structure):
        pass
    return SYSTEM_POLICY_INFORMATION
def _define_SYSTEM_POLICY_INFORMATION():
    SYSTEM_POLICY_INFORMATION = win32more.System.WindowsProgramming.SYSTEM_POLICY_INFORMATION_head
    SYSTEM_POLICY_INFORMATION._fields_ = [
        ('Reserved1', c_void_p * 2),
        ('Reserved2', UInt32 * 3),
    ]
    return SYSTEM_POLICY_INFORMATION
def _define_SYSTEM_PROCESS_INFORMATION_head():
    class SYSTEM_PROCESS_INFORMATION(Structure):
        pass
    return SYSTEM_PROCESS_INFORMATION
def _define_SYSTEM_PROCESS_INFORMATION():
    SYSTEM_PROCESS_INFORMATION = win32more.System.WindowsProgramming.SYSTEM_PROCESS_INFORMATION_head
    SYSTEM_PROCESS_INFORMATION._fields_ = [
        ('NextEntryOffset', UInt32),
        ('NumberOfThreads', UInt32),
        ('Reserved1', Byte * 48),
        ('ImageName', win32more.Foundation.UNICODE_STRING),
        ('BasePriority', Int32),
        ('UniqueProcessId', win32more.Foundation.HANDLE),
        ('Reserved2', c_void_p),
        ('HandleCount', UInt32),
        ('SessionId', UInt32),
        ('Reserved3', c_void_p),
        ('PeakVirtualSize', UIntPtr),
        ('VirtualSize', UIntPtr),
        ('Reserved4', UInt32),
        ('PeakWorkingSetSize', UIntPtr),
        ('WorkingSetSize', UIntPtr),
        ('Reserved5', c_void_p),
        ('QuotaPagedPoolUsage', UIntPtr),
        ('Reserved6', c_void_p),
        ('QuotaNonPagedPoolUsage', UIntPtr),
        ('PagefileUsage', UIntPtr),
        ('PeakPagefileUsage', UIntPtr),
        ('PrivatePageCount', UIntPtr),
        ('Reserved7', win32more.Foundation.LARGE_INTEGER * 6),
    ]
    return SYSTEM_PROCESS_INFORMATION
def _define_SYSTEM_PROCESSOR_PERFORMANCE_INFORMATION_head():
    class SYSTEM_PROCESSOR_PERFORMANCE_INFORMATION(Structure):
        pass
    return SYSTEM_PROCESSOR_PERFORMANCE_INFORMATION
def _define_SYSTEM_PROCESSOR_PERFORMANCE_INFORMATION():
    SYSTEM_PROCESSOR_PERFORMANCE_INFORMATION = win32more.System.WindowsProgramming.SYSTEM_PROCESSOR_PERFORMANCE_INFORMATION_head
    SYSTEM_PROCESSOR_PERFORMANCE_INFORMATION._fields_ = [
        ('IdleTime', win32more.Foundation.LARGE_INTEGER),
        ('KernelTime', win32more.Foundation.LARGE_INTEGER),
        ('UserTime', win32more.Foundation.LARGE_INTEGER),
        ('Reserved1', win32more.Foundation.LARGE_INTEGER * 2),
        ('Reserved2', UInt32),
    ]
    return SYSTEM_PROCESSOR_PERFORMANCE_INFORMATION
def _define_SYSTEM_REGISTRY_QUOTA_INFORMATION_head():
    class SYSTEM_REGISTRY_QUOTA_INFORMATION(Structure):
        pass
    return SYSTEM_REGISTRY_QUOTA_INFORMATION
def _define_SYSTEM_REGISTRY_QUOTA_INFORMATION():
    SYSTEM_REGISTRY_QUOTA_INFORMATION = win32more.System.WindowsProgramming.SYSTEM_REGISTRY_QUOTA_INFORMATION_head
    SYSTEM_REGISTRY_QUOTA_INFORMATION._fields_ = [
        ('RegistryQuotaAllowed', UInt32),
        ('RegistryQuotaUsed', UInt32),
        ('Reserved1', c_void_p),
    ]
    return SYSTEM_REGISTRY_QUOTA_INFORMATION
def _define_SYSTEM_THREAD_INFORMATION_head():
    class SYSTEM_THREAD_INFORMATION(Structure):
        pass
    return SYSTEM_THREAD_INFORMATION
def _define_SYSTEM_THREAD_INFORMATION():
    SYSTEM_THREAD_INFORMATION = win32more.System.WindowsProgramming.SYSTEM_THREAD_INFORMATION_head
    SYSTEM_THREAD_INFORMATION._fields_ = [
        ('Reserved1', win32more.Foundation.LARGE_INTEGER * 3),
        ('Reserved2', UInt32),
        ('StartAddress', c_void_p),
        ('ClientId', win32more.System.WindowsProgramming.CLIENT_ID),
        ('Priority', Int32),
        ('BasePriority', Int32),
        ('Reserved3', UInt32),
        ('ThreadState', UInt32),
        ('WaitReason', UInt32),
    ]
    return SYSTEM_THREAD_INFORMATION
def _define_SYSTEM_TIMEOFDAY_INFORMATION_head():
    class SYSTEM_TIMEOFDAY_INFORMATION(Structure):
        pass
    return SYSTEM_TIMEOFDAY_INFORMATION
def _define_SYSTEM_TIMEOFDAY_INFORMATION():
    SYSTEM_TIMEOFDAY_INFORMATION = win32more.System.WindowsProgramming.SYSTEM_TIMEOFDAY_INFORMATION_head
    SYSTEM_TIMEOFDAY_INFORMATION._fields_ = [
        ('Reserved1', Byte * 48),
    ]
    return SYSTEM_TIMEOFDAY_INFORMATION
def _define_TCP_REQUEST_QUERY_INFORMATION_EX_W2K_head():
    class TCP_REQUEST_QUERY_INFORMATION_EX_W2K(Structure):
        pass
    return TCP_REQUEST_QUERY_INFORMATION_EX_W2K
def _define_TCP_REQUEST_QUERY_INFORMATION_EX_W2K():
    TCP_REQUEST_QUERY_INFORMATION_EX_W2K = win32more.System.WindowsProgramming.TCP_REQUEST_QUERY_INFORMATION_EX_W2K_head
    TCP_REQUEST_QUERY_INFORMATION_EX_W2K._fields_ = [
        ('ID', win32more.System.WindowsProgramming.TDIObjectID),
        ('Context', Byte * 16),
    ]
    return TCP_REQUEST_QUERY_INFORMATION_EX_W2K
def _define_TCP_REQUEST_QUERY_INFORMATION_EX_XP_head():
    class TCP_REQUEST_QUERY_INFORMATION_EX_XP(Structure):
        pass
    return TCP_REQUEST_QUERY_INFORMATION_EX_XP
def _define_TCP_REQUEST_QUERY_INFORMATION_EX_XP():
    TCP_REQUEST_QUERY_INFORMATION_EX_XP = win32more.System.WindowsProgramming.TCP_REQUEST_QUERY_INFORMATION_EX_XP_head
    TCP_REQUEST_QUERY_INFORMATION_EX_XP._fields_ = [
        ('ID', win32more.System.WindowsProgramming.TDIObjectID),
        ('Context', UIntPtr * 4),
    ]
    return TCP_REQUEST_QUERY_INFORMATION_EX_XP
def _define_TCP_REQUEST_QUERY_INFORMATION_EX32_XP_head():
    class TCP_REQUEST_QUERY_INFORMATION_EX32_XP(Structure):
        pass
    return TCP_REQUEST_QUERY_INFORMATION_EX32_XP
def _define_TCP_REQUEST_QUERY_INFORMATION_EX32_XP():
    TCP_REQUEST_QUERY_INFORMATION_EX32_XP = win32more.System.WindowsProgramming.TCP_REQUEST_QUERY_INFORMATION_EX32_XP_head
    TCP_REQUEST_QUERY_INFORMATION_EX32_XP._fields_ = [
        ('ID', win32more.System.WindowsProgramming.TDIObjectID),
        ('Context', UInt32 * 4),
    ]
    return TCP_REQUEST_QUERY_INFORMATION_EX32_XP
def _define_TCP_REQUEST_SET_INFORMATION_EX_head():
    class TCP_REQUEST_SET_INFORMATION_EX(Structure):
        pass
    return TCP_REQUEST_SET_INFORMATION_EX
def _define_TCP_REQUEST_SET_INFORMATION_EX():
    TCP_REQUEST_SET_INFORMATION_EX = win32more.System.WindowsProgramming.TCP_REQUEST_SET_INFORMATION_EX_head
    TCP_REQUEST_SET_INFORMATION_EX._fields_ = [
        ('ID', win32more.System.WindowsProgramming.TDIObjectID),
        ('BufferSize', UInt32),
        ('Buffer', Byte * 1),
    ]
    return TCP_REQUEST_SET_INFORMATION_EX
def _define_TDI_TL_IO_CONTROL_ENDPOINT_head():
    class TDI_TL_IO_CONTROL_ENDPOINT(Structure):
        pass
    return TDI_TL_IO_CONTROL_ENDPOINT
def _define_TDI_TL_IO_CONTROL_ENDPOINT():
    TDI_TL_IO_CONTROL_ENDPOINT = win32more.System.WindowsProgramming.TDI_TL_IO_CONTROL_ENDPOINT_head
    class TDI_TL_IO_CONTROL_ENDPOINT__Anonymous_e__Union(Union):
        pass
    TDI_TL_IO_CONTROL_ENDPOINT__Anonymous_e__Union._fields_ = [
        ('IoControlCode', UInt32),
        ('OptionName', UInt32),
    ]
    TDI_TL_IO_CONTROL_ENDPOINT._anonymous_ = [
        'Anonymous',
    ]
    TDI_TL_IO_CONTROL_ENDPOINT._fields_ = [
        ('Type', win32more.System.WindowsProgramming.TDI_TL_IO_CONTROL_TYPE),
        ('Level', UInt32),
        ('Anonymous', TDI_TL_IO_CONTROL_ENDPOINT__Anonymous_e__Union),
        ('InputBuffer', c_void_p),
        ('InputBufferLength', UInt32),
        ('OutputBuffer', c_void_p),
        ('OutputBufferLength', UInt32),
    ]
    return TDI_TL_IO_CONTROL_ENDPOINT
TDI_TL_IO_CONTROL_TYPE = Int32
TDI_TL_IO_CONTROL_TYPE_EndpointIoControlType = 0
TDI_TL_IO_CONTROL_TYPE_SetSockOptIoControlType = 1
TDI_TL_IO_CONTROL_TYPE_GetSockOptIoControlType = 2
TDI_TL_IO_CONTROL_TYPE_SocketIoControlType = 3
TDIENTITY_ENTITY_TYPE = UInt32
GENERIC_ENTITY = 0
AT_ENTITY = 640
CL_NL_ENTITY = 769
CO_NL_ENTITY = 768
CL_TL_ENTITY = 1025
CO_TL_ENTITY = 1024
ER_ENTITY = 896
IF_ENTITY = 512
def _define_TDIEntityID_head():
    class TDIEntityID(Structure):
        pass
    return TDIEntityID
def _define_TDIEntityID():
    TDIEntityID = win32more.System.WindowsProgramming.TDIEntityID_head
    TDIEntityID._fields_ = [
        ('tei_entity', win32more.System.WindowsProgramming.TDIENTITY_ENTITY_TYPE),
        ('tei_instance', UInt32),
    ]
    return TDIEntityID
def _define_TDIObjectID_head():
    class TDIObjectID(Structure):
        pass
    return TDIObjectID
def _define_TDIObjectID():
    TDIObjectID = win32more.System.WindowsProgramming.TDIObjectID_head
    TDIObjectID._fields_ = [
        ('toi_entity', win32more.System.WindowsProgramming.TDIEntityID),
        ('toi_class', UInt32),
        ('toi_type', UInt32),
        ('toi_id', UInt32),
    ]
    return TDIObjectID
def _define_THREAD_NAME_INFORMATION_head():
    class THREAD_NAME_INFORMATION(Structure):
        pass
    return THREAD_NAME_INFORMATION
def _define_THREAD_NAME_INFORMATION():
    THREAD_NAME_INFORMATION = win32more.System.WindowsProgramming.THREAD_NAME_INFORMATION_head
    THREAD_NAME_INFORMATION._fields_ = [
        ('ThreadName', win32more.Foundation.UNICODE_STRING),
    ]
    return THREAD_NAME_INFORMATION
def _define_UNDETERMINESTRUCT_head():
    class UNDETERMINESTRUCT(Structure):
        pass
    return UNDETERMINESTRUCT
def _define_UNDETERMINESTRUCT():
    UNDETERMINESTRUCT = win32more.System.WindowsProgramming.UNDETERMINESTRUCT_head
    UNDETERMINESTRUCT._fields_ = [
        ('dwSize', UInt32),
        ('uDefIMESize', UInt32),
        ('uDefIMEPos', UInt32),
        ('uUndetTextLen', UInt32),
        ('uUndetTextPos', UInt32),
        ('uUndetAttrPos', UInt32),
        ('uCursorPos', UInt32),
        ('uDeltaStart', UInt32),
        ('uDetermineTextLen', UInt32),
        ('uDetermineTextPos', UInt32),
        ('uDetermineDelimPos', UInt32),
        ('uYomiTextLen', UInt32),
        ('uYomiTextPos', UInt32),
        ('uYomiDelimPos', UInt32),
    ]
    return UNDETERMINESTRUCT
VALUENAME = Int32
VALUENAME_UNKNOWN = 0
VALUENAME_ENTERPRISE_DEFINED_CLASS_ID = 1
VALUENAME_BUILT_IN_LIST = 2
WINSTATIONINFOCLASS = Int32
WINSTATIONINFOCLASS_WinStationInformation = 8
def _define_WINSTATIONINFORMATIONW_head():
    class WINSTATIONINFORMATIONW(Structure):
        pass
    return WINSTATIONINFORMATIONW
def _define_WINSTATIONINFORMATIONW():
    WINSTATIONINFORMATIONW = win32more.System.WindowsProgramming.WINSTATIONINFORMATIONW_head
    WINSTATIONINFORMATIONW._fields_ = [
        ('Reserved2', Byte * 70),
        ('LogonId', UInt32),
        ('Reserved3', Byte * 1140),
    ]
    return WINSTATIONINFORMATIONW
def _define_WINWATCHNOTIFYPROC():
    return WINFUNCTYPE(Void,win32more.System.WindowsProgramming.HWINWATCH,win32more.Foundation.HWND,UInt32,win32more.Foundation.LPARAM)
def _define_WLDP_DEVICE_SECURITY_INFORMATION_head():
    class WLDP_DEVICE_SECURITY_INFORMATION(Structure):
        pass
    return WLDP_DEVICE_SECURITY_INFORMATION
def _define_WLDP_DEVICE_SECURITY_INFORMATION():
    WLDP_DEVICE_SECURITY_INFORMATION = win32more.System.WindowsProgramming.WLDP_DEVICE_SECURITY_INFORMATION_head
    WLDP_DEVICE_SECURITY_INFORMATION._fields_ = [
        ('UnlockIdSize', UInt32),
        ('UnlockId', c_char_p_no),
        ('ManufacturerIDLength', UInt32),
        ('ManufacturerID', win32more.Foundation.PWSTR),
    ]
    return WLDP_DEVICE_SECURITY_INFORMATION
WLDP_HOST = Int32
WLDP_HOST_RUNDLL32 = 0
WLDP_HOST_SVCHOST = 1
WLDP_HOST_MAX = 2
WLDP_HOST_ID = Int32
WLDP_HOST_ID_UNKNOWN = 0
WLDP_HOST_ID_GLOBAL = 1
WLDP_HOST_ID_VBA = 2
WLDP_HOST_ID_WSH = 3
WLDP_HOST_ID_POWERSHELL = 4
WLDP_HOST_ID_IE = 5
WLDP_HOST_ID_MSI = 6
WLDP_HOST_ID_ALL = 7
WLDP_HOST_ID_MAX = 8
def _define_WLDP_HOST_INFORMATION_head():
    class WLDP_HOST_INFORMATION(Structure):
        pass
    return WLDP_HOST_INFORMATION
def _define_WLDP_HOST_INFORMATION():
    WLDP_HOST_INFORMATION = win32more.System.WindowsProgramming.WLDP_HOST_INFORMATION_head
    WLDP_HOST_INFORMATION._fields_ = [
        ('dwRevision', UInt32),
        ('dwHostId', win32more.System.WindowsProgramming.WLDP_HOST_ID),
        ('szSource', win32more.Foundation.PWSTR),
        ('hSource', win32more.Foundation.HANDLE),
    ]
    return WLDP_HOST_INFORMATION
WLDP_KEY = Int32
KEY_UNKNOWN = 0
KEY_OVERRIDE = 1
KEY_ALL_KEYS = 2
WLDP_POLICY_SETTING = Int32
WLDP_POLICY_SETTING_AV_PERF_MODE = 1000
WLDP_WINDOWS_LOCKDOWN_MODE = Int32
WLDP_WINDOWS_LOCKDOWN_MODE_UNLOCKED = 0
WLDP_WINDOWS_LOCKDOWN_MODE_TRIAL = 1
WLDP_WINDOWS_LOCKDOWN_MODE_LOCKED = 2
WLDP_WINDOWS_LOCKDOWN_MODE_MAX = 3
WLDP_WINDOWS_LOCKDOWN_RESTRICTION = Int32
WLDP_WINDOWS_LOCKDOWN_RESTRICTION_NONE = 0
WLDP_WINDOWS_LOCKDOWN_RESTRICTION_NOUNLOCK = 1
WLDP_WINDOWS_LOCKDOWN_RESTRICTION_NOUNLOCK_PERMANENT = 2
WLDP_WINDOWS_LOCKDOWN_RESTRICTION_MAX = 3
__all__ = [
    "AADBE_ADD_ENTRY",
    "AADBE_DEL_ENTRY",
    "ACTCTX_FLAG_APPLICATION_NAME_VALID",
    "ACTCTX_FLAG_ASSEMBLY_DIRECTORY_VALID",
    "ACTCTX_FLAG_HMODULE_VALID",
    "ACTCTX_FLAG_LANGID_VALID",
    "ACTCTX_FLAG_PROCESSOR_ARCHITECTURE_VALID",
    "ACTCTX_FLAG_RESOURCE_NAME_VALID",
    "ACTCTX_FLAG_SET_PROCESS_DEFAULT",
    "ACTCTX_FLAG_SOURCE_IS_ASSEMBLYREF",
    "ACTCTX_SECTION_KEYED_DATA_2600",
    "ACTCTX_SECTION_KEYED_DATA_ASSEMBLY_METADATA",
    "ACTIVATION_CONTEXT_BASIC_INFORMATION",
    "ACTIVATION_CONTEXT_BASIC_INFORMATION_DEFINED",
    "AC_LINE_BACKUP_POWER",
    "AC_LINE_OFFLINE",
    "AC_LINE_ONLINE",
    "AC_LINE_UNKNOWN",
    "ADN_DEL_IF_EMPTY",
    "ADN_DEL_UNC_PATHS",
    "ADN_DONT_DEL_DIR",
    "ADN_DONT_DEL_SUBDIRS",
    "AFSR_BACKNEW",
    "AFSR_EXTRAINCREFCNT",
    "AFSR_NODELETENEW",
    "AFSR_NOMESSAGES",
    "AFSR_NOPROGRESS",
    "AFSR_RESTORE",
    "AFSR_UPDREFCNT",
    "AFSR_USEREFCNT",
    "AIF_FORCE_FILE_IN_USE",
    "AIF_NOLANGUAGECHECK",
    "AIF_NOOVERWRITE",
    "AIF_NOSKIP",
    "AIF_NOVERSIONCHECK",
    "AIF_NO_VERSION_DIALOG",
    "AIF_QUIET",
    "AIF_REPLACEONLY",
    "AIF_WARNIFSKIP",
    "ALINF_BKINSTALL",
    "ALINF_CHECKBKDATA",
    "ALINF_DELAYREGISTEROCX",
    "ALINF_NGCONV",
    "ALINF_QUIET",
    "ALINF_ROLLBACK",
    "ALINF_ROLLBKDOALL",
    "ALINF_UPDHLPDLLS",
    "APPLICATION_RECOVERY_CALLBACK",
    "ARSR_NOMESSAGES",
    "ARSR_REGSECTION",
    "ARSR_REMOVREGBKDATA",
    "ARSR_RESTORE",
    "ATOM_FLAG_GLOBAL",
    "AT_ARP",
    "AT_ENTITY",
    "AT_NULL",
    "AddDelBackupEntryA",
    "AddDelBackupEntryW",
    "AdvInstallFileA",
    "AdvInstallFileW",
    "ApphelpCheckShellObject",
    "BACKUP_GHOSTED_FILE_EXTENTS",
    "BACKUP_INVALID",
    "BASE_SEARCH_PATH_DISABLE_SAFE_SEARCHMODE",
    "BASE_SEARCH_PATH_ENABLE_SAFE_SEARCHMODE",
    "BASE_SEARCH_PATH_PERMANENT",
    "BATTERY_FLAG_CHARGING",
    "BATTERY_FLAG_CRITICAL",
    "BATTERY_FLAG_HIGH",
    "BATTERY_FLAG_LOW",
    "BATTERY_FLAG_NO_BATTERY",
    "BATTERY_FLAG_UNKNOWN",
    "BATTERY_LIFE_UNKNOWN",
    "BATTERY_PERCENTAGE_UNKNOWN",
    "CABINFOA",
    "CABINFOW",
    "CATID_DeleteBrowsingHistory",
    "CBR_110",
    "CBR_115200",
    "CBR_1200",
    "CBR_128000",
    "CBR_14400",
    "CBR_19200",
    "CBR_2400",
    "CBR_256000",
    "CBR_300",
    "CBR_38400",
    "CBR_4800",
    "CBR_56000",
    "CBR_57600",
    "CBR_600",
    "CBR_9600",
    "CE_DNS",
    "CE_IOE",
    "CE_MODE",
    "CE_OOP",
    "CE_PTO",
    "CE_TXFULL",
    "CLIENT_ID",
    "CL_NL_ENTITY",
    "CL_NL_IP",
    "CL_NL_IPX",
    "CL_TL_ENTITY",
    "CL_TL_NBF",
    "CL_TL_UDP",
    "CODEINTEGRITY_OPTION_DEBUGMODE_ENABLED",
    "CODEINTEGRITY_OPTION_ENABLED",
    "CODEINTEGRITY_OPTION_FLIGHTING_ENABLED",
    "CODEINTEGRITY_OPTION_FLIGHT_BUILD",
    "CODEINTEGRITY_OPTION_HVCI_IUM_ENABLED",
    "CODEINTEGRITY_OPTION_HVCI_KMCI_AUDITMODE_ENABLED",
    "CODEINTEGRITY_OPTION_HVCI_KMCI_ENABLED",
    "CODEINTEGRITY_OPTION_HVCI_KMCI_STRICTMODE_ENABLED",
    "CODEINTEGRITY_OPTION_PREPRODUCTION_BUILD",
    "CODEINTEGRITY_OPTION_TESTSIGN",
    "CODEINTEGRITY_OPTION_TEST_BUILD",
    "CODEINTEGRITY_OPTION_UMCI_AUDITMODE_ENABLED",
    "CODEINTEGRITY_OPTION_UMCI_ENABLED",
    "CODEINTEGRITY_OPTION_UMCI_EXCLUSIONPATHS_ENABLED",
    "CONTEXT_SIZE",
    "COPYFILE2_IO_CYCLE_SIZE_MAX",
    "COPYFILE2_IO_CYCLE_SIZE_MIN",
    "COPYFILE2_IO_RATE_MIN",
    "COPYFILE2_MESSAGE_COPY_OFFLOAD",
    "COPY_FILE_ALLOW_DECRYPTED_DESTINATION",
    "COPY_FILE_COPY_SYMLINK",
    "COPY_FILE_DIRECTORY",
    "COPY_FILE_DISABLE_PRE_ALLOCATION",
    "COPY_FILE_DONT_REQUEST_DEST_WRITE_DAC",
    "COPY_FILE_ENABLE_LOW_FREE_SPACE_MODE",
    "COPY_FILE_FAIL_IF_EXISTS",
    "COPY_FILE_IGNORE_EDP_BLOCK",
    "COPY_FILE_IGNORE_SOURCE_ENCRYPTION",
    "COPY_FILE_NO_BUFFERING",
    "COPY_FILE_NO_OFFLOAD",
    "COPY_FILE_OPEN_AND_COPY_REPARSE_POINT",
    "COPY_FILE_OPEN_SOURCE_FOR_WRITE",
    "COPY_FILE_REQUEST_COMPRESSED_TRAFFIC",
    "COPY_FILE_REQUEST_SECURITY_PRIVILEGES",
    "COPY_FILE_RESTARTABLE",
    "COPY_FILE_RESUME_FROM_PAUSE",
    "COPY_FILE_SKIP_ALTERNATE_STREAMS",
    "CO_NL_ENTITY",
    "CO_TL_ENTITY",
    "CO_TL_NBF",
    "CO_TL_SPP",
    "CO_TL_SPX",
    "CO_TL_TCP",
    "CP_DIRECT",
    "CP_HWND",
    "CP_LEVEL",
    "CP_OPEN",
    "CREATE_FOR_DIR",
    "CREATE_FOR_IMPORT",
    "CRITICAL_SECTION_NO_DEBUG_INFO",
    "CUSTOM_SYSTEM_EVENT_TRIGGER_CONFIG",
    "CameraUIControl",
    "CameraUIControlCaptureMode",
    "CameraUIControlCaptureMode_Photo",
    "CameraUIControlCaptureMode_PhotoOrVideo",
    "CameraUIControlCaptureMode_Video",
    "CameraUIControlLinearSelectionMode",
    "CameraUIControlLinearSelectionMode_Multiple",
    "CameraUIControlLinearSelectionMode_Single",
    "CameraUIControlMode",
    "CameraUIControlMode_Browse",
    "CameraUIControlMode_Linear",
    "CameraUIControlPhotoFormat",
    "CameraUIControlPhotoFormat_Jpeg",
    "CameraUIControlPhotoFormat_JpegXR",
    "CameraUIControlPhotoFormat_Png",
    "CameraUIControlVideoFormat",
    "CameraUIControlVideoFormat_Mp4",
    "CameraUIControlVideoFormat_Wmv",
    "CameraUIControlViewType",
    "CameraUIControlViewType_ItemList",
    "CameraUIControlViewType_SingleItem",
    "CancelDeviceWakeupRequest",
    "CancelTimerQueueTimer",
    "CloseINFEngine",
    "ConvertAuxiliaryCounterToPerformanceCounter",
    "ConvertPerformanceCounterToAuxiliaryCounter",
    "CreateWaitableTimerA",
    "CreateWaitableTimerExA",
    "DATETIME",
    "DCIBeginAccess",
    "DCICMD",
    "DCICREATEINPUT",
    "DCICREATEOFFSCREENSURFACE",
    "DCICREATEOVERLAYSURFACE",
    "DCICREATEPRIMARYSURFACE",
    "DCICloseProvider",
    "DCICreateOffscreen",
    "DCICreateOverlay",
    "DCICreatePrimary",
    "DCIDestroy",
    "DCIDraw",
    "DCIENUMINPUT",
    "DCIENUMSURFACE",
    "DCIESCAPE",
    "DCIEndAccess",
    "DCIEnum",
    "DCIOFFSCREEN",
    "DCIOVERLAY",
    "DCIOpenProvider",
    "DCISURFACEINFO",
    "DCISetClipList",
    "DCISetDestination",
    "DCISetSrcDestClip",
    "DCI_1632_ACCESS",
    "DCI_ASYNC",
    "DCI_CANOVERLAY",
    "DCI_CAN_STRETCHX",
    "DCI_CAN_STRETCHXN",
    "DCI_CAN_STRETCHY",
    "DCI_CAN_STRETCHYN",
    "DCI_CHROMAKEY",
    "DCI_DWORDALIGN",
    "DCI_DWORDSIZE",
    "DCI_ERR_CURRENTLYNOTAVAIL",
    "DCI_ERR_HEIGHTALIGN",
    "DCI_ERR_INVALIDCLIPLIST",
    "DCI_ERR_INVALIDPOSITION",
    "DCI_ERR_INVALIDRECT",
    "DCI_ERR_INVALIDSTRETCH",
    "DCI_ERR_OUTOFMEMORY",
    "DCI_ERR_SURFACEISOBSCURED",
    "DCI_ERR_TOOBIGHEIGHT",
    "DCI_ERR_TOOBIGSIZE",
    "DCI_ERR_TOOBIGWIDTH",
    "DCI_ERR_UNSUPPORTEDFORMAT",
    "DCI_ERR_UNSUPPORTEDMASK",
    "DCI_ERR_WIDTHALIGN",
    "DCI_ERR_XALIGN",
    "DCI_ERR_XYALIGN",
    "DCI_ERR_YALIGN",
    "DCI_FAIL_GENERIC",
    "DCI_FAIL_INVALIDSURFACE",
    "DCI_FAIL_UNSUPPORTED",
    "DCI_FAIL_UNSUPPORTEDVERSION",
    "DCI_OFFSCREEN",
    "DCI_OK",
    "DCI_OVERLAY",
    "DCI_PRIMARY",
    "DCI_STATUS_CHROMAKEYCHANGED",
    "DCI_STATUS_FORMATCHANGED",
    "DCI_STATUS_POINTERCHANGED",
    "DCI_STATUS_STRIDECHANGED",
    "DCI_STATUS_SURFACEINFOCHANGED",
    "DCI_STATUS_WASSTILLDRAWING",
    "DCI_SURFACE_TYPE",
    "DCI_VERSION",
    "DCI_VISIBLE",
    "DCI_WRITEONLY",
    "DEACTIVATE_ACTCTX_FLAG_FORCE_EARLY_DEACTIVATION",
    "DECISION_LOCATION",
    "DECISION_LOCATION_AUDIT",
    "DECISION_LOCATION_ENFORCE_STATE_LIST",
    "DECISION_LOCATION_ENTERPRISE_DEFINED_CLASS_ID",
    "DECISION_LOCATION_FAILED_CONVERT_GUID",
    "DECISION_LOCATION_GLOBAL_BUILT_IN_LIST",
    "DECISION_LOCATION_NOT_FOUND",
    "DECISION_LOCATION_PARAMETER_VALIDATION",
    "DECISION_LOCATION_PROVIDER_BUILT_IN_LIST",
    "DECISION_LOCATION_REFRESH_GLOBAL_DATA",
    "DECISION_LOCATION_UNKNOWN",
    "DELAYLOAD_GPA_FAILURE",
    "DELAYLOAD_INFO",
    "DELAYLOAD_PROC_DESCRIPTOR",
    "DELETE_BROWSING_HISTORY_COOKIES",
    "DELETE_BROWSING_HISTORY_DOWNLOADHISTORY",
    "DELETE_BROWSING_HISTORY_FORMDATA",
    "DELETE_BROWSING_HISTORY_HISTORY",
    "DELETE_BROWSING_HISTORY_PASSWORDS",
    "DELETE_BROWSING_HISTORY_PRESERVEFAVORITES",
    "DELETE_BROWSING_HISTORY_TIF",
    "DOCKINFO_DOCKED",
    "DOCKINFO_UNDOCKED",
    "DOCKINFO_USER_SUPPLIED",
    "DRIVE_CDROM",
    "DRIVE_FIXED",
    "DRIVE_NO_ROOT_DIR",
    "DRIVE_RAMDISK",
    "DRIVE_REMOTE",
    "DRIVE_REMOVABLE",
    "DRIVE_UNKNOWN",
    "DTR_CONTROL_DISABLE",
    "DTR_CONTROL_ENABLE",
    "DTR_CONTROL_HANDSHAKE",
    "DefaultBrowserSyncSettings",
    "DelNodeA",
    "DelNodeRunDLL32W",
    "DelNodeW",
    "DnsHostnameToComputerNameA",
    "DnsHostnameToComputerNameW",
    "DosDateTimeToFileTime",
    "EFSRPC_SECURE_ONLY",
    "EFS_DROP_ALTERNATE_STREAMS",
    "EFS_USE_RECOVERY_KEYS",
    "ENTITY_LIST_ID",
    "ENTITY_TYPE_ID",
    "ENUM_CALLBACK",
    "ER_ENTITY",
    "ER_ICMP",
    "EVENTLOG_FULL_INFO",
    "EditionUpgradeBroker",
    "EditionUpgradeHelper",
    "EnableProcessOptionalXStateFeatures",
    "ExecuteCabA",
    "ExecuteCabW",
    "ExtractFilesA",
    "ExtractFilesW",
    "FAIL_FAST_GENERATE_EXCEPTION_ADDRESS",
    "FAIL_FAST_NO_HARD_ERROR_DLG",
    "FEATURE_CHANGE_TIME",
    "FEATURE_CHANGE_TIME_MODULE_RELOAD",
    "FEATURE_CHANGE_TIME_READ",
    "FEATURE_CHANGE_TIME_REBOOT",
    "FEATURE_CHANGE_TIME_SESSION",
    "FEATURE_ENABLED_STATE",
    "FEATURE_ENABLED_STATE_DEFAULT",
    "FEATURE_ENABLED_STATE_DISABLED",
    "FEATURE_ENABLED_STATE_ENABLED",
    "FEATURE_ERROR",
    "FEATURE_STATE_CHANGE_SUBSCRIPTION",
    "FH_SERVICE_PIPE_HANDLE",
    "FIBER_FLAG_FLOAT_SWITCH",
    "FILE_CASE_SENSITIVE_INFO",
    "FILE_COMPLETE_IF_OPLOCKED",
    "FILE_CREATED",
    "FILE_CREATE_TREE_CONNECTION",
    "FILE_DELETE_ON_CLOSE",
    "FILE_DIRECTORY_FILE",
    "FILE_DIR_DISALLOWED",
    "FILE_DISPOSITION_FLAG_DELETE",
    "FILE_DISPOSITION_FLAG_DO_NOT_DELETE",
    "FILE_DISPOSITION_FLAG_FORCE_IMAGE_SECTION_CHECK",
    "FILE_DISPOSITION_FLAG_IGNORE_READONLY_ATTRIBUTE",
    "FILE_DISPOSITION_FLAG_ON_CLOSE",
    "FILE_DISPOSITION_FLAG_POSIX_SEMANTICS",
    "FILE_DISPOSITION_INFO_EX",
    "FILE_DOES_NOT_EXIST",
    "FILE_ENCRYPTABLE",
    "FILE_EXISTS",
    "FILE_FLAG_OPEN_REQUIRING_OPLOCK",
    "FILE_INFORMATION_CLASS",
    "FILE_INFORMATION_CLASS_FileDirectoryInformation",
    "FILE_IS_ENCRYPTED",
    "FILE_MAXIMUM_DISPOSITION",
    "FILE_NON_DIRECTORY_FILE",
    "FILE_NO_COMPRESSION",
    "FILE_NO_EA_KNOWLEDGE",
    "FILE_NO_INTERMEDIATE_BUFFERING",
    "FILE_OPENED",
    "FILE_OPEN_BY_FILE_ID",
    "FILE_OPEN_FOR_BACKUP_INTENT",
    "FILE_OPEN_FOR_FREE_SPACE_QUERY",
    "FILE_OPEN_NO_RECALL",
    "FILE_OPEN_REMOTE_INSTANCE",
    "FILE_OPEN_REPARSE_POINT",
    "FILE_OPEN_REQUIRING_OPLOCK",
    "FILE_OVERWRITTEN",
    "FILE_RANDOM_ACCESS",
    "FILE_READ_ONLY",
    "FILE_RENAME_FLAG_POSIX_SEMANTICS",
    "FILE_RENAME_FLAG_REPLACE_IF_EXISTS",
    "FILE_RENAME_FLAG_SUPPRESS_PIN_STATE_INHERITANCE",
    "FILE_RESERVE_OPFILTER",
    "FILE_ROOT_DIR",
    "FILE_SEQUENTIAL_ONLY",
    "FILE_SKIP_COMPLETION_PORT_ON_SUCCESS",
    "FILE_SKIP_SET_EVENT_ON_HANDLE",
    "FILE_SUPERSEDED",
    "FILE_SYNCHRONOUS_IO_ALERT",
    "FILE_SYNCHRONOUS_IO_NONALERT",
    "FILE_SYSTEM_ATTR",
    "FILE_SYSTEM_DIR",
    "FILE_SYSTEM_NOT_SUPPORT",
    "FILE_UNKNOWN",
    "FILE_USER_DISALLOWED",
    "FILE_VALID_MAILSLOT_OPTION_FLAGS",
    "FILE_VALID_OPTION_FLAGS",
    "FILE_VALID_PIPE_OPTION_FLAGS",
    "FILE_VALID_SET_FLAGS",
    "FILE_WRITE_THROUGH",
    "FIND_ACTCTX_SECTION_KEY_RETURN_ASSEMBLY_METADATA",
    "FIND_ACTCTX_SECTION_KEY_RETURN_FLAGS",
    "FIND_ACTCTX_SECTION_KEY_RETURN_HACTCTX",
    "FORMAT_MESSAGE_MAX_WIDTH_MASK",
    "FS_CASE_IS_PRESERVED",
    "FS_CASE_SENSITIVE",
    "FS_FILE_COMPRESSION",
    "FS_FILE_ENCRYPTION",
    "FS_PERSISTENT_ACLS",
    "FS_UNICODE_STORED_ON_DISK",
    "FS_VOL_IS_COMPRESSED",
    "FileSaveMarkNotExistA",
    "FileSaveMarkNotExistW",
    "FileSaveRestoreOnINFA",
    "FileSaveRestoreOnINFW",
    "FileSaveRestoreW",
    "FileTimeToDosDateTime",
    "GENERIC_ENTITY",
    "GET_SYSTEM_WOW64_DIRECTORY_NAME_A_A",
    "GET_SYSTEM_WOW64_DIRECTORY_NAME_A_T",
    "GET_SYSTEM_WOW64_DIRECTORY_NAME_A_W",
    "GET_SYSTEM_WOW64_DIRECTORY_NAME_T_A",
    "GET_SYSTEM_WOW64_DIRECTORY_NAME_T_T",
    "GET_SYSTEM_WOW64_DIRECTORY_NAME_T_W",
    "GET_SYSTEM_WOW64_DIRECTORY_NAME_W_A",
    "GET_SYSTEM_WOW64_DIRECTORY_NAME_W_T",
    "GET_SYSTEM_WOW64_DIRECTORY_NAME_W_W",
    "GMEM_DDESHARE",
    "GMEM_DISCARDABLE",
    "GMEM_DISCARDED",
    "GMEM_INVALID_HANDLE",
    "GMEM_LOCKCOUNT",
    "GMEM_LOWER",
    "GMEM_MODIFY",
    "GMEM_NOCOMPACT",
    "GMEM_NODISCARD",
    "GMEM_NOTIFY",
    "GMEM_NOT_BANKED",
    "GMEM_SHARE",
    "GMEM_VALID_FLAGS",
    "GdiEntry13",
    "GetComputerNameA",
    "GetComputerNameW",
    "GetCurrentHwProfileA",
    "GetCurrentHwProfileW",
    "GetDCRegionData",
    "GetFeatureEnabledState",
    "GetFeatureVariant",
    "GetFirmwareEnvironmentVariableA",
    "GetFirmwareEnvironmentVariableExA",
    "GetFirmwareEnvironmentVariableExW",
    "GetFirmwareEnvironmentVariableW",
    "GetPrivateProfileIntA",
    "GetPrivateProfileIntW",
    "GetPrivateProfileSectionA",
    "GetPrivateProfileSectionNamesA",
    "GetPrivateProfileSectionNamesW",
    "GetPrivateProfileSectionW",
    "GetPrivateProfileStringA",
    "GetPrivateProfileStringW",
    "GetPrivateProfileStructA",
    "GetPrivateProfileStructW",
    "GetProfileIntA",
    "GetProfileIntW",
    "GetProfileSectionA",
    "GetProfileSectionW",
    "GetProfileStringA",
    "GetProfileStringW",
    "GetSystemRegistryQuota",
    "GetThreadEnabledXStateFeatures",
    "GetUserNameA",
    "GetUserNameW",
    "GetVersionFromFileA",
    "GetVersionFromFileExA",
    "GetVersionFromFileExW",
    "GetVersionFromFileW",
    "GetWindowRegionData",
    "GlobalCompact",
    "GlobalFix",
    "GlobalUnWire",
    "GlobalUnfix",
    "GlobalWire",
    "HANJA_WINDOW",
    "HINSTANCE_ERROR",
    "HWINWATCH",
    "HW_PROFILE_GUIDLEN",
    "HW_PROFILE_INFOA",
    "HW_PROFILE_INFOW",
    "ICameraUIControl",
    "ICameraUIControlEventCallback",
    "IClipServiceNotificationHelper",
    "IContainerActivationHelper",
    "IDefaultBrowserSyncSettings",
    "IDeleteBrowsingHistory",
    "IE4_BACKNEW",
    "IE4_EXTRAINCREFCNT",
    "IE4_FRDOALL",
    "IE4_NODELETENEW",
    "IE4_NOENUMKEY",
    "IE4_NOMESSAGES",
    "IE4_NOPROGRESS",
    "IE4_NO_CRC_MAPPING",
    "IE4_REGSECTION",
    "IE4_REMOVREGBKDATA",
    "IE4_RESTORE",
    "IE4_UPDREFCNT",
    "IE4_USEREFCNT",
    "IE_BADID",
    "IE_BAUDRATE",
    "IE_BYTESIZE",
    "IE_DEFAULT",
    "IE_HARDWARE",
    "IE_MEMORY",
    "IE_NOPEN",
    "IE_OPEN",
    "IEditionUpgradeBroker",
    "IEditionUpgradeHelper",
    "IF_ENTITY",
    "IF_GENERIC",
    "IF_MIB",
    "IGNORE",
    "IMAGE_DELAYLOAD_DESCRIPTOR",
    "IMAGE_THUNK_DATA32",
    "IMAGE_THUNK_DATA64",
    "IMEA_INIT",
    "IMEA_NEXT",
    "IMEA_PREV",
    "IMEPROA",
    "IMEPROW",
    "IMESTRUCT",
    "IME_BANJAtoJUNJA",
    "IME_ENABLE_CONVERT",
    "IME_ENTERWORDREGISTERMODE",
    "IME_GETCONVERSIONMODE",
    "IME_GETIMECAPS",
    "IME_GETOPEN",
    "IME_GETVERSION",
    "IME_JOHABtoKS",
    "IME_JUNJAtoBANJA",
    "IME_KStoJOHAB",
    "IME_MAXPROCESS",
    "IME_MODE_ALPHANUMERIC",
    "IME_MODE_CODEINPUT",
    "IME_MODE_DBCSCHAR",
    "IME_MODE_HANJACONVERT",
    "IME_MODE_HIRAGANA",
    "IME_MODE_KATAKANA",
    "IME_MODE_NOCODEINPUT",
    "IME_MODE_NOROMAN",
    "IME_MODE_ROMAN",
    "IME_MODE_SBCSCHAR",
    "IME_MOVEIMEWINDOW",
    "IME_REQUEST_CONVERT",
    "IME_RS_DISKERROR",
    "IME_RS_ERROR",
    "IME_RS_ILLEGAL",
    "IME_RS_INVALID",
    "IME_RS_NEST",
    "IME_RS_NOIME",
    "IME_RS_NOROOM",
    "IME_RS_NOTFOUND",
    "IME_RS_SYSTEMMODAL",
    "IME_RS_TOOLONG",
    "IME_SENDVKEY",
    "IME_SETCONVERSIONFONTEX",
    "IME_SETCONVERSIONMODE",
    "IME_SETCONVERSIONWINDOW",
    "IME_SETOPEN",
    "IME_SET_MODE",
    "IMPGetIMEA",
    "IMPGetIMEW",
    "IMPQueryIMEA",
    "IMPQueryIMEW",
    "IMPSetIMEA",
    "IMPSetIMEW",
    "INFINITE",
    "INFO_CLASS_GENERIC",
    "INFO_CLASS_IMPLEMENTATION",
    "INFO_CLASS_PROTOCOL",
    "INFO_TYPE_ADDRESS_OBJECT",
    "INFO_TYPE_CONNECTION",
    "INFO_TYPE_PROVIDER",
    "INTERIM_WINDOW",
    "INVALID_ENTITY_INSTANCE",
    "IOCTL_TDI_TL_IO_CONTROL_ENDPOINT",
    "IO_STATUS_BLOCK",
    "IR_CHANGECONVERT",
    "IR_CLOSECONVERT",
    "IR_DBCSCHAR",
    "IR_FULLCONVERT",
    "IR_IMESELECT",
    "IR_MODEINFO",
    "IR_OPENCONVERT",
    "IR_STRING",
    "IR_STRINGEND",
    "IR_STRINGEX",
    "IR_STRINGSTART",
    "IR_UNDETERMINE",
    "IWindowsLockModeHelper",
    "IsApiSetImplemented",
    "IsBadHugeReadPtr",
    "IsBadHugeWritePtr",
    "IsNTAdmin",
    "IsNativeVhdBoot",
    "IsTokenUntrusted",
    "JAVA_TRUST",
    "JIT_DEBUG_INFO",
    "KEY_ALL_KEYS",
    "KEY_OVERRIDE",
    "KEY_SET_INFORMATION_CLASS",
    "KEY_SET_INFORMATION_CLASS_KeyControlFlagsInformation",
    "KEY_SET_INFORMATION_CLASS_KeySetDebugInformation",
    "KEY_SET_INFORMATION_CLASS_KeySetHandleTagsInformation",
    "KEY_SET_INFORMATION_CLASS_KeySetVirtualizationInformation",
    "KEY_SET_INFORMATION_CLASS_KeyWow64FlagsInformation",
    "KEY_SET_INFORMATION_CLASS_KeyWriteTimeInformation",
    "KEY_SET_INFORMATION_CLASS_MaxKeySetInfoClass",
    "KEY_UNKNOWN",
    "KEY_VALUE_ENTRY",
    "LDR_DATA_TABLE_ENTRY",
    "LIS_NOGRPCONV",
    "LIS_QUIET",
    "LOGON32_PROVIDER_VIRTUAL",
    "LOGON32_PROVIDER_WINNT35",
    "LOGON_ZERO_PASSWORD_BUFFER",
    "LPTx",
    "LaunchINFSectionExW",
    "LaunchINFSectionW",
    "LocalCompact",
    "LocalShrink",
    "MAXINTATOM",
    "MAX_COMPUTERNAME_LENGTH",
    "MAX_TDI_ENTITIES",
    "MCW_DEFAULT",
    "MCW_HIDDEN",
    "MCW_RECT",
    "MCW_SCREEN",
    "MCW_VERTICAL",
    "MCW_WINDOW",
    "MICROSOFT_WINBASE_H_DEFINE_INTERLOCKED_CPLUSPLUS_OVERLOADS",
    "MICROSOFT_WINDOWS_WINBASE_H_DEFINE_INTERLOCKED_CPLUSPLUS_OVERLOADS",
    "MODE_WINDOW",
    "MulDiv",
    "NeedReboot",
    "NeedRebootInit",
    "NtClose",
    "NtDeviceIoControlFile",
    "NtNotifyChangeMultipleKeys",
    "NtOpenFile",
    "NtQueryMultipleValueKey",
    "NtQueryObject",
    "NtQuerySystemInformation",
    "NtQuerySystemTime",
    "NtQueryTimerResolution",
    "NtRenameKey",
    "NtSetInformationKey",
    "NtWaitForSingleObject",
    "OBJECT_ATTRIBUTES",
    "OBJECT_INFORMATION_CLASS",
    "OBJECT_INFORMATION_CLASS_ObjectBasicInformation",
    "OBJECT_INFORMATION_CLASS_ObjectTypeInformation",
    "OFS_MAXPATHNAME",
    "OPERATION_API_VERSION",
    "OVERWRITE_HIDDEN",
    "OpenINFEngineA",
    "OpenINFEngineW",
    "OpenMutexA",
    "OpenSemaphoreA",
    "OpenWaitableTimerA",
    "PDELAYLOAD_FAILURE_DLL_CALLBACK",
    "PERUSERSECTIONA",
    "PERUSERSECTIONW",
    "PFEATURE_STATE_CHANGE_CALLBACK",
    "PFIBER_CALLOUT_ROUTINE",
    "PIO_APC_ROUTINE",
    "PQUERYACTCTXW_FUNC",
    "PROCESS_CREATION_ALL_APPLICATION_PACKAGES_OPT_OUT",
    "PROCESS_CREATION_CHILD_PROCESS_OVERRIDE",
    "PROCESS_CREATION_CHILD_PROCESS_RESTRICTED",
    "PROCESS_CREATION_CHILD_PROCESS_RESTRICTED_UNLESS_SECURE",
    "PROCESS_CREATION_DESKTOP_APP_BREAKAWAY_DISABLE_PROCESS_TREE",
    "PROCESS_CREATION_DESKTOP_APP_BREAKAWAY_ENABLE_PROCESS_TREE",
    "PROCESS_CREATION_DESKTOP_APP_BREAKAWAY_OVERRIDE",
    "PROCESS_CREATION_MITIGATION_POLICY_DEP_ATL_THUNK_ENABLE",
    "PROCESS_CREATION_MITIGATION_POLICY_DEP_ENABLE",
    "PROCESS_CREATION_MITIGATION_POLICY_SEHOP_ENABLE",
    "PROC_THREAD_ATTRIBUTE_ADDITIVE",
    "PROC_THREAD_ATTRIBUTE_INPUT",
    "PROC_THREAD_ATTRIBUTE_NUMBER",
    "PROC_THREAD_ATTRIBUTE_THREAD",
    "PROGRESS_CANCEL",
    "PROGRESS_CONTINUE",
    "PROGRESS_QUIET",
    "PROGRESS_STOP",
    "PROTECTION_LEVEL_SAME",
    "PUBLIC_OBJECT_BASIC_INFORMATION",
    "PUBLIC_OBJECT_TYPE_INFORMATION",
    "PWINSTATIONQUERYINFORMATIONW",
    "PWLDP_ISAPPAPPROVEDBYPOLICY_API",
    "PWLDP_ISDYNAMICCODEPOLICYENABLED_API",
    "PWLDP_ISPRODUCTIONCONFIGURATION_API",
    "PWLDP_ISWCOSPRODUCTIONCONFIGURATION_API",
    "PWLDP_QUERYDEVICESECURITYINFORMATION_API",
    "PWLDP_QUERYDYNAMICODETRUST_API",
    "PWLDP_QUERYPOLICYSETTINGENABLED2_API",
    "PWLDP_QUERYPOLICYSETTINGENABLED_API",
    "PWLDP_QUERYWINDOWSLOCKDOWNMODE_API",
    "PWLDP_QUERYWINDOWSLOCKDOWNRESTRICTION_API",
    "PWLDP_RESETPRODUCTIONCONFIGURATION_API",
    "PWLDP_RESETWCOSPRODUCTIONCONFIGURATION_API",
    "PWLDP_SETDYNAMICCODETRUST_API",
    "PWLDP_SETWINDOWSLOCKDOWNRESTRICTION_API",
    "QUERY_ACTCTX_FLAG_ACTCTX_IS_ADDRESS",
    "QUERY_ACTCTX_FLAG_ACTCTX_IS_HMODULE",
    "QUERY_ACTCTX_FLAG_NO_ADDREF",
    "QUERY_ACTCTX_FLAG_USE_ACTIVE_ACTCTX",
    "QueryAuxiliaryCounterFrequency",
    "QueryIdleProcessorCycleTime",
    "QueryIdleProcessorCycleTimeEx",
    "QueryInterruptTime",
    "QueryInterruptTimePrecise",
    "QueryProcessCycleTime",
    "QueryThreadCycleTime",
    "QueryUnbiasedInterruptTime",
    "QueryUnbiasedInterruptTimePrecise",
    "RECOVERY_DEFAULT_PING_INTERVAL",
    "REGINSTALLA",
    "REG_RESTORE_LOG_KEY",
    "REG_SAVE_LOG_KEY",
    "REMOTE_PROTOCOL_INFO_FLAG_LOOPBACK",
    "REMOTE_PROTOCOL_INFO_FLAG_OFFLINE",
    "REMOTE_PROTOCOL_INFO_FLAG_PERSISTENT_HANDLE",
    "RESETDEV",
    "RESTART_MAX_CMD_LINE",
    "RPI_FLAG_SMB2_SHARECAP_CLUSTER",
    "RPI_FLAG_SMB2_SHARECAP_CONTINUOUS_AVAILABILITY",
    "RPI_FLAG_SMB2_SHARECAP_DFS",
    "RPI_FLAG_SMB2_SHARECAP_SCALEOUT",
    "RPI_FLAG_SMB2_SHARECAP_TIMEWARP",
    "RPI_SMB2_FLAG_SERVERCAP_DFS",
    "RPI_SMB2_FLAG_SERVERCAP_DIRECTORY_LEASING",
    "RPI_SMB2_FLAG_SERVERCAP_LARGEMTU",
    "RPI_SMB2_FLAG_SERVERCAP_LEASING",
    "RPI_SMB2_FLAG_SERVERCAP_MULTICHANNEL",
    "RPI_SMB2_FLAG_SERVERCAP_PERSISTENT_HANDLES",
    "RSC_FLAG_DELAYREGISTEROCX",
    "RSC_FLAG_INF",
    "RSC_FLAG_NGCONV",
    "RSC_FLAG_QUIET",
    "RSC_FLAG_SETUPAPI",
    "RSC_FLAG_SKIPDISKSPACECHECK",
    "RSC_FLAG_UPDHLPDLLS",
    "RTS_CONTROL_DISABLE",
    "RTS_CONTROL_ENABLE",
    "RTS_CONTROL_HANDSHAKE",
    "RTS_CONTROL_TOGGLE",
    "RUNCMDS_DELAYPOSTCMD",
    "RUNCMDS_NOWAIT",
    "RUNCMDS_QUIET",
    "RaiseCustomSystemEventTrigger",
    "RebootCheckOnInstallA",
    "RebootCheckOnInstallW",
    "RecordFeatureError",
    "RecordFeatureUsage",
    "RegInstallA",
    "RegInstallW",
    "RegRestoreAllA",
    "RegRestoreAllW",
    "RegSaveRestoreA",
    "RegSaveRestoreOnINFA",
    "RegSaveRestoreOnINFW",
    "RegSaveRestoreW",
    "ReplacePartitionUnit",
    "RequestDeviceWakeup",
    "RtlAnsiStringToUnicodeString",
    "RtlCharToInteger",
    "RtlFreeAnsiString",
    "RtlFreeOemString",
    "RtlFreeUnicodeString",
    "RtlGetReturnAddressHijackTarget",
    "RtlInitAnsiString",
    "RtlInitAnsiStringEx",
    "RtlInitString",
    "RtlInitStringEx",
    "RtlInitUnicodeString",
    "RtlIsNameLegalDOS8Dot3",
    "RtlLocalTimeToSystemTime",
    "RtlRaiseCustomSystemEventTrigger",
    "RtlTimeToSecondsSince1970",
    "RtlUnicodeStringToAnsiString",
    "RtlUnicodeStringToOemString",
    "RtlUnicodeToMultiByteSize",
    "RtlUniform",
    "RunSetupCommandA",
    "RunSetupCommandW",
    "SCS_32BIT_BINARY",
    "SCS_64BIT_BINARY",
    "SCS_DOS_BINARY",
    "SCS_OS216_BINARY",
    "SCS_PIF_BINARY",
    "SCS_POSIX_BINARY",
    "SCS_THIS_PLATFORM_BINARY",
    "SCS_WOW_BINARY",
    "SHUTDOWN_NORETRY",
    "STARTF_HOLOGRAPHIC",
    "STORAGE_INFO_FLAGS_ALIGNED_DEVICE",
    "STORAGE_INFO_FLAGS_PARTITION_ALIGNED_ON_DEVICE",
    "STORAGE_INFO_OFFSET_UNKNOWN",
    "STREAM_CONTAINS_GHOSTED_FILE_EXTENTS",
    "STREAM_CONTAINS_PROPERTIES",
    "STREAM_CONTAINS_SECURITY",
    "STREAM_MODIFIED_WHEN_READ",
    "STREAM_NORMAL_ATTRIBUTE",
    "STREAM_SPARSE_ATTRIBUTE",
    "STRENTRYA",
    "STRENTRYW",
    "STRINGEXSTRUCT",
    "STRTABLEA",
    "STRTABLEW",
    "SYSTEM_BASIC_INFORMATION",
    "SYSTEM_CODEINTEGRITY_INFORMATION",
    "SYSTEM_EXCEPTION_INFORMATION",
    "SYSTEM_INFORMATION_CLASS",
    "SYSTEM_INFORMATION_CLASS_SystemBasicInformation",
    "SYSTEM_INFORMATION_CLASS_SystemCodeIntegrityInformation",
    "SYSTEM_INFORMATION_CLASS_SystemExceptionInformation",
    "SYSTEM_INFORMATION_CLASS_SystemInterruptInformation",
    "SYSTEM_INFORMATION_CLASS_SystemLookasideInformation",
    "SYSTEM_INFORMATION_CLASS_SystemPerformanceInformation",
    "SYSTEM_INFORMATION_CLASS_SystemPolicyInformation",
    "SYSTEM_INFORMATION_CLASS_SystemProcessInformation",
    "SYSTEM_INFORMATION_CLASS_SystemProcessorPerformanceInformation",
    "SYSTEM_INFORMATION_CLASS_SystemRegistryQuotaInformation",
    "SYSTEM_INFORMATION_CLASS_SystemTimeOfDayInformation",
    "SYSTEM_INTERRUPT_INFORMATION",
    "SYSTEM_LOOKASIDE_INFORMATION",
    "SYSTEM_PERFORMANCE_INFORMATION",
    "SYSTEM_POLICY_INFORMATION",
    "SYSTEM_PROCESSOR_PERFORMANCE_INFORMATION",
    "SYSTEM_PROCESS_INFORMATION",
    "SYSTEM_REGISTRY_QUOTA_INFORMATION",
    "SYSTEM_STATUS_FLAG_POWER_SAVING_ON",
    "SYSTEM_THREAD_INFORMATION",
    "SYSTEM_TIMEOFDAY_INFORMATION",
    "S_ALLTHRESHOLD",
    "S_LEGATO",
    "S_NORMAL",
    "S_PERIOD1024",
    "S_PERIOD2048",
    "S_PERIOD512",
    "S_PERIODVOICE",
    "S_QUEUEEMPTY",
    "S_SERBDNT",
    "S_SERDCC",
    "S_SERDDR",
    "S_SERDFQ",
    "S_SERDLN",
    "S_SERDMD",
    "S_SERDPT",
    "S_SERDSH",
    "S_SERDSR",
    "S_SERDST",
    "S_SERDTP",
    "S_SERDVL",
    "S_SERDVNA",
    "S_SERMACT",
    "S_SEROFM",
    "S_SERQFUL",
    "S_STACCATO",
    "S_THRESHOLD",
    "S_WHITE1024",
    "S_WHITE2048",
    "S_WHITE512",
    "S_WHITEVOICE",
    "SendIMEMessageExA",
    "SendIMEMessageExW",
    "SetEnvironmentStringsA",
    "SetFirmwareEnvironmentVariableA",
    "SetFirmwareEnvironmentVariableExA",
    "SetFirmwareEnvironmentVariableExW",
    "SetFirmwareEnvironmentVariableW",
    "SetHandleCount",
    "SetMessageWaitingIndicator",
    "SetPerUserSecValuesA",
    "SetPerUserSecValuesW",
    "SignalObjectAndWait",
    "SubscribeFeatureStateChangeNotification",
    "TCP_REQUEST_QUERY_INFORMATION_EX32_XP",
    "TCP_REQUEST_QUERY_INFORMATION_EX_W2K",
    "TCP_REQUEST_QUERY_INFORMATION_EX_XP",
    "TCP_REQUEST_SET_INFORMATION_EX",
    "TC_GP_TRAP",
    "TC_HARDERR",
    "TC_NORMAL",
    "TC_SIGNAL",
    "TDIENTITY_ENTITY_TYPE",
    "TDIEntityID",
    "TDIObjectID",
    "TDI_TL_IO_CONTROL_ENDPOINT",
    "TDI_TL_IO_CONTROL_TYPE",
    "TDI_TL_IO_CONTROL_TYPE_EndpointIoControlType",
    "TDI_TL_IO_CONTROL_TYPE_GetSockOptIoControlType",
    "TDI_TL_IO_CONTROL_TYPE_SetSockOptIoControlType",
    "TDI_TL_IO_CONTROL_TYPE_SocketIoControlType",
    "THREAD_NAME_INFORMATION",
    "THREAD_PRIORITY_ERROR_RETURN",
    "TranslateInfStringA",
    "TranslateInfStringExA",
    "TranslateInfStringExW",
    "TranslateInfStringW",
    "UMS_VERSION",
    "UNDETERMINESTRUCT",
    "UnsubscribeFeatureStateChangeNotification",
    "UserInstStubWrapperA",
    "UserInstStubWrapperW",
    "UserUnInstStubWrapperA",
    "UserUnInstStubWrapperW",
    "VALUENAME",
    "VALUENAME_BUILT_IN_LIST",
    "VALUENAME_ENTERPRISE_DEFINED_CLASS_ID",
    "VALUENAME_UNKNOWN",
    "VOLUME_NAME_DOS",
    "VOLUME_NAME_GUID",
    "VOLUME_NAME_NONE",
    "VOLUME_NAME_NT",
    "WINNLSEnableIME",
    "WINNLSGetEnableStatus",
    "WINNLSGetIMEHotkey",
    "WINSTATIONINFOCLASS",
    "WINSTATIONINFOCLASS_WinStationInformation",
    "WINSTATIONINFORMATIONW",
    "WINWATCHNOTIFYPROC",
    "WINWATCHNOTIFY_CHANGED",
    "WINWATCHNOTIFY_CHANGING",
    "WINWATCHNOTIFY_DESTROY",
    "WINWATCHNOTIFY_START",
    "WINWATCHNOTIFY_STOP",
    "WLDP_DEVICE_SECURITY_INFORMATION",
    "WLDP_DLL",
    "WLDP_FLAGS_SKIPSIGNATUREVALIDATION",
    "WLDP_GETLOCKDOWNPOLICY_FN",
    "WLDP_HOST",
    "WLDP_HOST_ID",
    "WLDP_HOST_ID_ALL",
    "WLDP_HOST_ID_GLOBAL",
    "WLDP_HOST_ID_IE",
    "WLDP_HOST_ID_MAX",
    "WLDP_HOST_ID_MSI",
    "WLDP_HOST_ID_POWERSHELL",
    "WLDP_HOST_ID_UNKNOWN",
    "WLDP_HOST_ID_VBA",
    "WLDP_HOST_ID_WSH",
    "WLDP_HOST_INFORMATION",
    "WLDP_HOST_INFORMATION_REVISION",
    "WLDP_HOST_MAX",
    "WLDP_HOST_RUNDLL32",
    "WLDP_HOST_SVCHOST",
    "WLDP_ISAPPAPPROVEDBYPOLICY_FN",
    "WLDP_ISCLASSINAPPROVEDLIST_FN",
    "WLDP_ISDYNAMICCODEPOLICYENABLED_FN",
    "WLDP_ISPRODUCTIONCONFIGURATION_FN",
    "WLDP_ISWCOSPRODUCTIONCONFIGURATION_FN",
    "WLDP_KEY",
    "WLDP_LOCKDOWN_AUDIT_FLAG",
    "WLDP_LOCKDOWN_CONFIG_CI_AUDIT_FLAG",
    "WLDP_LOCKDOWN_CONFIG_CI_FLAG",
    "WLDP_LOCKDOWN_DEFINED_FLAG",
    "WLDP_LOCKDOWN_EXCLUSION_FLAG",
    "WLDP_LOCKDOWN_OFF",
    "WLDP_LOCKDOWN_UMCIENFORCE_FLAG",
    "WLDP_LOCKDOWN_UNDEFINED",
    "WLDP_POLICY_SETTING",
    "WLDP_POLICY_SETTING_AV_PERF_MODE",
    "WLDP_QUERYDANAMICCODETRUST_FN",
    "WLDP_QUERYDEVICESECURITYINFORMATION_FN",
    "WLDP_QUERYDYNAMICCODETRUST_FN",
    "WLDP_QUERYPOLICYSETTINGENABLED2_FN",
    "WLDP_QUERYPOLICYSETTINGENABLED_FN",
    "WLDP_QUERYWINDOWSLOCKDOWNMODE_FN",
    "WLDP_QUERYWINDOWSLOCKDOWNRESTRICTION_FN",
    "WLDP_RESETPRODUCTIONCONFIGURATION_FN",
    "WLDP_RESETWCOSPRODUCTIONCONFIGURATION_FN",
    "WLDP_SETDYNAMICCODETRUST_FN",
    "WLDP_SETWINDOWSLOCKDOWNRESTRICTION_FN",
    "WLDP_WINDOWS_LOCKDOWN_MODE",
    "WLDP_WINDOWS_LOCKDOWN_MODE_LOCKED",
    "WLDP_WINDOWS_LOCKDOWN_MODE_MAX",
    "WLDP_WINDOWS_LOCKDOWN_MODE_TRIAL",
    "WLDP_WINDOWS_LOCKDOWN_MODE_UNLOCKED",
    "WLDP_WINDOWS_LOCKDOWN_RESTRICTION",
    "WLDP_WINDOWS_LOCKDOWN_RESTRICTION_MAX",
    "WLDP_WINDOWS_LOCKDOWN_RESTRICTION_NONE",
    "WLDP_WINDOWS_LOCKDOWN_RESTRICTION_NOUNLOCK",
    "WLDP_WINDOWS_LOCKDOWN_RESTRICTION_NOUNLOCK_PERMANENT",
    "WM_CONVERTREQUEST",
    "WM_CONVERTRESULT",
    "WM_IMEKEYDOWN",
    "WM_IMEKEYUP",
    "WM_IME_REPORT",
    "WM_INTERIM",
    "WM_WNT_CONVERTREQUESTEX",
    "WinWatchClose",
    "WinWatchDidStatusChange",
    "WinWatchGetClipList",
    "WinWatchNotify",
    "WinWatchOpen",
    "WldpGetLockdownPolicy",
    "WldpIsClassInApprovedList",
    "WldpIsDynamicCodePolicyEnabled",
    "WldpQueryDeviceSecurityInformation",
    "WldpQueryDynamicCodeTrust",
    "WldpSetDynamicCodeTrust",
    "WritePrivateProfileSectionA",
    "WritePrivateProfileSectionW",
    "WritePrivateProfileStringA",
    "WritePrivateProfileStringW",
    "WritePrivateProfileStructA",
    "WritePrivateProfileStructW",
    "WriteProfileSectionA",
    "WriteProfileSectionW",
    "WriteProfileStringA",
    "WriteProfileStringW",
    "_D3DHAL_CALLBACKS",
    "_D3DHAL_GLOBALDRIVERDATA",
    "_hread",
    "_hwrite",
    "_lclose",
    "_lcreat",
    "_llseek",
    "_lopen",
    "_lread",
    "_lwrite",
    "uaw_lstrcmpW",
    "uaw_lstrcmpiW",
    "uaw_lstrlenW",
    "uaw_wcschr",
    "uaw_wcscpy",
    "uaw_wcsicmp",
    "uaw_wcslen",
    "uaw_wcsrchr",
]
