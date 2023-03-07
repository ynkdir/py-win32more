from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.Graphics.Gdi
import Windows.Win32.Security
import Windows.Win32.System.Com
import Windows.Win32.System.Kernel
import Windows.Win32.System.Ole
import Windows.Win32.System.Registry
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
class ACTCTX_SECTION_KEYED_DATA_2600(Structure):
    cbSize: UInt32
    ulDataFormatVersion: UInt32
    lpData: c_void_p
    ulLength: UInt32
    lpSectionGlobalData: c_void_p
    ulSectionGlobalDataLength: UInt32
    lpSectionBase: c_void_p
    ulSectionTotalLength: UInt32
    hActCtx: Windows.Win32.Foundation.HANDLE
    ulAssemblyRosterIndex: UInt32
class ACTCTX_SECTION_KEYED_DATA_ASSEMBLY_METADATA(Structure):
    lpInformation: c_void_p
    lpSectionBase: c_void_p
    ulSectionLength: UInt32
    lpSectionGlobalDataBase: c_void_p
    ulSectionGlobalDataLength: UInt32
class ACTIVATION_CONTEXT_BASIC_INFORMATION(Structure):
    hActCtx: Windows.Win32.Foundation.HANDLE
    dwFlags: UInt32
@winfunctype_pointer
def APPLICATION_RECOVERY_CALLBACK(pvParameter: c_void_p) -> UInt32: ...
WLDP_DLL: String = 'WLDP.DLL'
WLDP_GETLOCKDOWNPOLICY_FN: String = 'WldpGetLockdownPolicy'
WLDP_ISCLASSINAPPROVEDLIST_FN: String = 'WldpIsClassInApprovedList'
WLDP_SETDYNAMICCODETRUST_FN: String = 'WldpSetDynamicCodeTrust'
WLDP_ISDYNAMICCODEPOLICYENABLED_FN: String = 'WldpIsDynamicCodePolicyEnabled'
WLDP_QUERYDANAMICCODETRUST_FN: String = 'WldpQueryDynamicCodeTrust'
WLDP_QUERYDYNAMICCODETRUST_FN: String = 'WldpQueryDynamicCodeTrust'
WLDP_QUERYWINDOWSLOCKDOWNMODE_FN: String = 'WldpQueryWindowsLockdownMode'
WLDP_SETWINDOWSLOCKDOWNRESTRICTION_FN: String = 'WldpSetWindowsLockdownRestriction'
WLDP_QUERYDEVICESECURITYINFORMATION_FN: String = 'WldpQueryDeviceSecurityInformation'
WLDP_QUERYWINDOWSLOCKDOWNRESTRICTION_FN: String = 'WldpQueryWindowsLockdownRestriction'
WLDP_ISAPPAPPROVEDBYPOLICY_FN: String = 'WldpIsAppApprovedByPolicy'
WLDP_QUERYPOLICYSETTINGENABLED_FN: String = 'WldpQueryPolicySettingEnabled'
WLDP_QUERYPOLICYSETTINGENABLED2_FN: String = 'WldpQueryPolicySettingEnabled2'
WLDP_ISWCOSPRODUCTIONCONFIGURATION_FN: String = 'WldpIsWcosProductionConfiguration'
WLDP_RESETWCOSPRODUCTIONCONFIGURATION_FN: String = 'WldpResetWcosProductionConfiguration'
WLDP_ISPRODUCTIONCONFIGURATION_FN: String = 'WldpIsProductionConfiguration'
WLDP_RESETPRODUCTIONCONFIGURATION_FN: String = 'WldpResetProductionConfiguration'
WLDP_LOCKDOWN_UNDEFINED: UInt32 = 0
WLDP_LOCKDOWN_DEFINED_FLAG: UInt32 = 2147483648
WLDP_LOCKDOWN_CONFIG_CI_FLAG: UInt32 = 1
WLDP_LOCKDOWN_CONFIG_CI_AUDIT_FLAG: UInt32 = 2
WLDP_LOCKDOWN_UMCIENFORCE_FLAG: UInt32 = 4
WLDP_LOCKDOWN_AUDIT_FLAG: UInt32 = 8
WLDP_LOCKDOWN_EXCLUSION_FLAG: UInt32 = 16
WLDP_LOCKDOWN_OFF: UInt32 = 2147483648
WLDP_HOST_INFORMATION_REVISION: UInt32 = 1
WLDP_FLAGS_SKIPSIGNATUREVALIDATION: UInt32 = 256
MAX_TDI_ENTITIES: UInt32 = 4096
INFO_CLASS_GENERIC: UInt32 = 256
INFO_CLASS_PROTOCOL: UInt32 = 512
INFO_CLASS_IMPLEMENTATION: UInt32 = 768
INFO_TYPE_PROVIDER: UInt32 = 256
INFO_TYPE_ADDRESS_OBJECT: UInt32 = 512
INFO_TYPE_CONNECTION: UInt32 = 768
ENTITY_LIST_ID: UInt32 = 0
INVALID_ENTITY_INSTANCE: Int32 = -1
CONTEXT_SIZE: UInt32 = 16
ENTITY_TYPE_ID: UInt32 = 1
CO_TL_NBF: UInt32 = 1024
CO_TL_SPX: UInt32 = 1026
CO_TL_TCP: UInt32 = 1028
CO_TL_SPP: UInt32 = 1030
CL_TL_NBF: UInt32 = 1025
CL_TL_UDP: UInt32 = 1027
ER_ICMP: UInt32 = 896
CL_NL_IPX: UInt32 = 769
CL_NL_IP: UInt32 = 771
AT_ARP: UInt32 = 640
AT_NULL: UInt32 = 642
IF_GENERIC: UInt32 = 512
IF_MIB: UInt32 = 514
IOCTL_TDI_TL_IO_CONTROL_ENDPOINT: UInt32 = 2162744
DCI_VERSION: UInt32 = 256
DCICREATEPRIMARYSURFACE: UInt32 = 1
DCICREATEOFFSCREENSURFACE: UInt32 = 2
DCICREATEOVERLAYSURFACE: UInt32 = 3
DCIENUMSURFACE: UInt32 = 4
DCIESCAPE: UInt32 = 5
DCI_OK: UInt32 = 0
DCI_FAIL_GENERIC: Int32 = -1
DCI_FAIL_UNSUPPORTEDVERSION: Int32 = -2
DCI_FAIL_INVALIDSURFACE: Int32 = -3
DCI_FAIL_UNSUPPORTED: Int32 = -4
DCI_ERR_CURRENTLYNOTAVAIL: Int32 = -5
DCI_ERR_INVALIDRECT: Int32 = -6
DCI_ERR_UNSUPPORTEDFORMAT: Int32 = -7
DCI_ERR_UNSUPPORTEDMASK: Int32 = -8
DCI_ERR_TOOBIGHEIGHT: Int32 = -9
DCI_ERR_TOOBIGWIDTH: Int32 = -10
DCI_ERR_TOOBIGSIZE: Int32 = -11
DCI_ERR_OUTOFMEMORY: Int32 = -12
DCI_ERR_INVALIDPOSITION: Int32 = -13
DCI_ERR_INVALIDSTRETCH: Int32 = -14
DCI_ERR_INVALIDCLIPLIST: Int32 = -15
DCI_ERR_SURFACEISOBSCURED: Int32 = -16
DCI_ERR_XALIGN: Int32 = -17
DCI_ERR_YALIGN: Int32 = -18
DCI_ERR_XYALIGN: Int32 = -19
DCI_ERR_WIDTHALIGN: Int32 = -20
DCI_ERR_HEIGHTALIGN: Int32 = -21
DCI_STATUS_POINTERCHANGED: UInt32 = 1
DCI_STATUS_STRIDECHANGED: UInt32 = 2
DCI_STATUS_FORMATCHANGED: UInt32 = 4
DCI_STATUS_SURFACEINFOCHANGED: UInt32 = 8
DCI_STATUS_CHROMAKEYCHANGED: UInt32 = 16
DCI_STATUS_WASSTILLDRAWING: UInt32 = 32
DCI_SURFACE_TYPE: UInt32 = 15
DCI_PRIMARY: UInt32 = 0
DCI_OFFSCREEN: UInt32 = 1
DCI_OVERLAY: UInt32 = 2
DCI_VISIBLE: UInt32 = 16
DCI_CHROMAKEY: UInt32 = 32
DCI_1632_ACCESS: UInt32 = 64
DCI_DWORDSIZE: UInt32 = 128
DCI_DWORDALIGN: UInt32 = 256
DCI_WRITEONLY: UInt32 = 512
DCI_ASYNC: UInt32 = 1024
DCI_CAN_STRETCHX: UInt32 = 4096
DCI_CAN_STRETCHY: UInt32 = 8192
DCI_CAN_STRETCHXN: UInt32 = 16384
DCI_CAN_STRETCHYN: UInt32 = 32768
DCI_CANOVERLAY: UInt32 = 65536
FILE_FLAG_OPEN_REQUIRING_OPLOCK: UInt32 = 262144
PROGRESS_CONTINUE: UInt32 = 0
PROGRESS_CANCEL: UInt32 = 1
PROGRESS_STOP: UInt32 = 2
PROGRESS_QUIET: UInt32 = 3
COPY_FILE_FAIL_IF_EXISTS: UInt32 = 1
COPY_FILE_RESTARTABLE: UInt32 = 2
COPY_FILE_OPEN_SOURCE_FOR_WRITE: UInt32 = 4
COPY_FILE_ALLOW_DECRYPTED_DESTINATION: UInt32 = 8
COPY_FILE_COPY_SYMLINK: UInt32 = 2048
COPY_FILE_NO_BUFFERING: UInt32 = 4096
COPY_FILE_REQUEST_SECURITY_PRIVILEGES: UInt32 = 8192
COPY_FILE_RESUME_FROM_PAUSE: UInt32 = 16384
COPY_FILE_NO_OFFLOAD: UInt32 = 262144
COPY_FILE_IGNORE_EDP_BLOCK: UInt32 = 4194304
COPY_FILE_IGNORE_SOURCE_ENCRYPTION: UInt32 = 8388608
COPY_FILE_DONT_REQUEST_DEST_WRITE_DAC: UInt32 = 33554432
COPY_FILE_REQUEST_COMPRESSED_TRAFFIC: UInt32 = 268435456
COPY_FILE_OPEN_AND_COPY_REPARSE_POINT: UInt32 = 2097152
COPY_FILE_DIRECTORY: UInt32 = 128
COPY_FILE_SKIP_ALTERNATE_STREAMS: UInt32 = 32768
COPY_FILE_DISABLE_PRE_ALLOCATION: UInt32 = 67108864
COPY_FILE_ENABLE_LOW_FREE_SPACE_MODE: UInt32 = 134217728
FAIL_FAST_GENERATE_EXCEPTION_ADDRESS: UInt32 = 1
FAIL_FAST_NO_HARD_ERROR_DLG: UInt32 = 2
SP_SERIALCOMM: UInt32 = 1
PST_UNSPECIFIED: UInt32 = 0
PST_RS232: UInt32 = 1
PST_PARALLELPORT: UInt32 = 2
PST_RS422: UInt32 = 3
PST_RS423: UInt32 = 4
PST_RS449: UInt32 = 5
PST_MODEM: UInt32 = 6
PST_FAX: UInt32 = 33
PST_SCANNER: UInt32 = 34
PST_NETWORK_BRIDGE: UInt32 = 256
PST_LAT: UInt32 = 257
PST_TCPIP_TELNET: UInt32 = 258
PST_X25: UInt32 = 259
PCF_DTRDSR: UInt32 = 1
PCF_RTSCTS: UInt32 = 2
PCF_RLSD: UInt32 = 4
PCF_PARITY_CHECK: UInt32 = 8
PCF_XONXOFF: UInt32 = 16
PCF_SETXCHAR: UInt32 = 32
PCF_TOTALTIMEOUTS: UInt32 = 64
PCF_INTTIMEOUTS: UInt32 = 128
PCF_SPECIALCHARS: UInt32 = 256
PCF_16BITMODE: UInt32 = 512
SP_PARITY: UInt32 = 1
SP_BAUD: UInt32 = 2
SP_DATABITS: UInt32 = 4
SP_STOPBITS: UInt32 = 8
SP_HANDSHAKING: UInt32 = 16
SP_PARITY_CHECK: UInt32 = 32
SP_RLSD: UInt32 = 64
BAUD_075: UInt32 = 1
BAUD_110: UInt32 = 2
BAUD_134_5: UInt32 = 4
BAUD_150: UInt32 = 8
BAUD_300: UInt32 = 16
BAUD_600: UInt32 = 32
BAUD_1200: UInt32 = 64
BAUD_1800: UInt32 = 128
BAUD_2400: UInt32 = 256
BAUD_4800: UInt32 = 512
BAUD_7200: UInt32 = 1024
BAUD_9600: UInt32 = 2048
BAUD_14400: UInt32 = 4096
BAUD_19200: UInt32 = 8192
BAUD_38400: UInt32 = 16384
BAUD_56K: UInt32 = 32768
BAUD_128K: UInt32 = 65536
BAUD_115200: UInt32 = 131072
BAUD_57600: UInt32 = 262144
BAUD_USER: UInt32 = 268435456
COMMPROP_INITIALIZED: UInt32 = 3879531822
DTR_CONTROL_DISABLE: UInt32 = 0
DTR_CONTROL_ENABLE: UInt32 = 1
DTR_CONTROL_HANDSHAKE: UInt32 = 2
RTS_CONTROL_DISABLE: UInt32 = 0
RTS_CONTROL_ENABLE: UInt32 = 1
RTS_CONTROL_HANDSHAKE: UInt32 = 2
RTS_CONTROL_TOGGLE: UInt32 = 3
GMEM_NOCOMPACT: UInt32 = 16
GMEM_NODISCARD: UInt32 = 32
GMEM_MODIFY: UInt32 = 128
GMEM_DISCARDABLE: UInt32 = 256
GMEM_NOT_BANKED: UInt32 = 4096
GMEM_SHARE: UInt32 = 8192
GMEM_DDESHARE: UInt32 = 8192
GMEM_NOTIFY: UInt32 = 16384
GMEM_LOWER: UInt32 = 4096
GMEM_VALID_FLAGS: UInt32 = 32626
GMEM_INVALID_HANDLE: UInt32 = 32768
GMEM_DISCARDED: UInt32 = 16384
GMEM_LOCKCOUNT: UInt32 = 255
THREAD_PRIORITY_ERROR_RETURN: UInt32 = 2147483647
VOLUME_NAME_DOS: UInt32 = 0
VOLUME_NAME_GUID: UInt32 = 1
VOLUME_NAME_NT: UInt32 = 2
VOLUME_NAME_NONE: UInt32 = 4
DRIVE_UNKNOWN: UInt32 = 0
DRIVE_NO_ROOT_DIR: UInt32 = 1
DRIVE_REMOVABLE: UInt32 = 2
DRIVE_FIXED: UInt32 = 3
DRIVE_REMOTE: UInt32 = 4
DRIVE_CDROM: UInt32 = 5
DRIVE_RAMDISK: UInt32 = 6
IGNORE: UInt32 = 0
INFINITE: UInt32 = 4294967295
CBR_110: UInt32 = 110
CBR_300: UInt32 = 300
CBR_600: UInt32 = 600
CBR_1200: UInt32 = 1200
CBR_2400: UInt32 = 2400
CBR_4800: UInt32 = 4800
CBR_9600: UInt32 = 9600
CBR_14400: UInt32 = 14400
CBR_19200: UInt32 = 19200
CBR_38400: UInt32 = 38400
CBR_56000: UInt32 = 56000
CBR_57600: UInt32 = 57600
CBR_115200: UInt32 = 115200
CBR_128000: UInt32 = 128000
CBR_256000: UInt32 = 256000
CE_TXFULL: UInt32 = 256
CE_PTO: UInt32 = 512
CE_IOE: UInt32 = 1024
CE_DNS: UInt32 = 2048
CE_OOP: UInt32 = 4096
CE_MODE: UInt32 = 32768
IE_BADID: Int32 = -1
IE_OPEN: Int32 = -2
IE_NOPEN: Int32 = -3
IE_MEMORY: Int32 = -4
IE_DEFAULT: Int32 = -5
IE_HARDWARE: Int32 = -10
IE_BYTESIZE: Int32 = -11
IE_BAUDRATE: Int32 = -12
RESETDEV: UInt32 = 7
LPTx: UInt32 = 128
S_QUEUEEMPTY: UInt32 = 0
S_THRESHOLD: UInt32 = 1
S_ALLTHRESHOLD: UInt32 = 2
S_NORMAL: UInt32 = 0
S_LEGATO: UInt32 = 1
S_STACCATO: UInt32 = 2
S_PERIOD512: UInt32 = 0
S_PERIOD1024: UInt32 = 1
S_PERIOD2048: UInt32 = 2
S_PERIODVOICE: UInt32 = 3
S_WHITE512: UInt32 = 4
S_WHITE1024: UInt32 = 5
S_WHITE2048: UInt32 = 6
S_WHITEVOICE: UInt32 = 7
S_SERDVNA: Int32 = -1
S_SEROFM: Int32 = -2
S_SERMACT: Int32 = -3
S_SERQFUL: Int32 = -4
S_SERBDNT: Int32 = -5
S_SERDLN: Int32 = -6
S_SERDCC: Int32 = -7
S_SERDTP: Int32 = -8
S_SERDVL: Int32 = -9
S_SERDMD: Int32 = -10
S_SERDSH: Int32 = -11
S_SERDPT: Int32 = -12
S_SERDFQ: Int32 = -13
S_SERDDR: Int32 = -14
S_SERDSR: Int32 = -15
S_SERDST: Int32 = -16
FS_CASE_IS_PRESERVED: UInt32 = 2
FS_CASE_SENSITIVE: UInt32 = 1
FS_UNICODE_STORED_ON_DISK: UInt32 = 4
FS_PERSISTENT_ACLS: UInt32 = 8
FS_VOL_IS_COMPRESSED: UInt32 = 32768
FS_FILE_COMPRESSION: UInt32 = 16
FS_FILE_ENCRYPTION: UInt32 = 131072
OFS_MAXPATHNAME: UInt32 = 128
MAXINTATOM: UInt32 = 49152
SCS_32BIT_BINARY: UInt32 = 0
SCS_DOS_BINARY: UInt32 = 1
SCS_WOW_BINARY: UInt32 = 2
SCS_PIF_BINARY: UInt32 = 3
SCS_POSIX_BINARY: UInt32 = 4
SCS_OS216_BINARY: UInt32 = 5
SCS_64BIT_BINARY: UInt32 = 6
SCS_THIS_PLATFORM_BINARY: UInt32 = 6
FIBER_FLAG_FLOAT_SWITCH: UInt32 = 1
UMS_VERSION: UInt32 = 256
FILE_SKIP_COMPLETION_PORT_ON_SUCCESS: UInt32 = 1
FILE_SKIP_SET_EVENT_ON_HANDLE: UInt32 = 2
CRITICAL_SECTION_NO_DEBUG_INFO: UInt32 = 16777216
HINSTANCE_ERROR: UInt32 = 32
FORMAT_MESSAGE_MAX_WIDTH_MASK: UInt32 = 255
FILE_ENCRYPTABLE: UInt32 = 0
FILE_IS_ENCRYPTED: UInt32 = 1
FILE_SYSTEM_ATTR: UInt32 = 2
FILE_ROOT_DIR: UInt32 = 3
FILE_SYSTEM_DIR: UInt32 = 4
FILE_UNKNOWN: UInt32 = 5
FILE_SYSTEM_NOT_SUPPORT: UInt32 = 6
FILE_USER_DISALLOWED: UInt32 = 7
FILE_READ_ONLY: UInt32 = 8
FILE_DIR_DISALLOWED: UInt32 = 9
EFS_USE_RECOVERY_KEYS: UInt32 = 1
CREATE_FOR_IMPORT: UInt32 = 1
CREATE_FOR_DIR: UInt32 = 2
OVERWRITE_HIDDEN: UInt32 = 4
EFSRPC_SECURE_ONLY: UInt32 = 8
EFS_DROP_ALTERNATE_STREAMS: UInt32 = 16
BACKUP_INVALID: UInt32 = 0
BACKUP_GHOSTED_FILE_EXTENTS: UInt32 = 11
STREAM_NORMAL_ATTRIBUTE: UInt32 = 0
STREAM_MODIFIED_WHEN_READ: UInt32 = 1
STREAM_CONTAINS_SECURITY: UInt32 = 2
STREAM_CONTAINS_PROPERTIES: UInt32 = 4
STREAM_SPARSE_ATTRIBUTE: UInt32 = 8
STREAM_CONTAINS_GHOSTED_FILE_EXTENTS: UInt32 = 16
STARTF_HOLOGRAPHIC: UInt32 = 262144
SHUTDOWN_NORETRY: UInt32 = 1
PROTECTION_LEVEL_SAME: UInt32 = 4294967295
PROC_THREAD_ATTRIBUTE_NUMBER: UInt32 = 65535
PROC_THREAD_ATTRIBUTE_THREAD: UInt32 = 65536
PROC_THREAD_ATTRIBUTE_INPUT: UInt32 = 131072
PROC_THREAD_ATTRIBUTE_ADDITIVE: UInt32 = 262144
PROCESS_CREATION_MITIGATION_POLICY_DEP_ENABLE: UInt32 = 1
PROCESS_CREATION_MITIGATION_POLICY_DEP_ATL_THUNK_ENABLE: UInt32 = 2
PROCESS_CREATION_MITIGATION_POLICY_SEHOP_ENABLE: UInt32 = 4
PROCESS_CREATION_CHILD_PROCESS_RESTRICTED: UInt32 = 1
PROCESS_CREATION_CHILD_PROCESS_OVERRIDE: UInt32 = 2
PROCESS_CREATION_CHILD_PROCESS_RESTRICTED_UNLESS_SECURE: UInt32 = 4
PROCESS_CREATION_ALL_APPLICATION_PACKAGES_OPT_OUT: UInt32 = 1
PROCESS_CREATION_DESKTOP_APP_BREAKAWAY_ENABLE_PROCESS_TREE: UInt32 = 1
PROCESS_CREATION_DESKTOP_APP_BREAKAWAY_DISABLE_PROCESS_TREE: UInt32 = 2
PROCESS_CREATION_DESKTOP_APP_BREAKAWAY_OVERRIDE: UInt32 = 4
ATOM_FLAG_GLOBAL: UInt32 = 2
GET_SYSTEM_WOW64_DIRECTORY_NAME_A_A: String = 'GetSystemWow64DirectoryA'
GET_SYSTEM_WOW64_DIRECTORY_NAME_A_W: String = 'GetSystemWow64DirectoryA'
GET_SYSTEM_WOW64_DIRECTORY_NAME_A_T: String = 'GetSystemWow64DirectoryA'
GET_SYSTEM_WOW64_DIRECTORY_NAME_W_A: String = 'GetSystemWow64DirectoryW'
GET_SYSTEM_WOW64_DIRECTORY_NAME_W_W: String = 'GetSystemWow64DirectoryW'
GET_SYSTEM_WOW64_DIRECTORY_NAME_W_T: String = 'GetSystemWow64DirectoryW'
GET_SYSTEM_WOW64_DIRECTORY_NAME_T_A: String = 'GetSystemWow64DirectoryW'
GET_SYSTEM_WOW64_DIRECTORY_NAME_T_W: String = 'GetSystemWow64DirectoryW'
GET_SYSTEM_WOW64_DIRECTORY_NAME_T_T: String = 'GetSystemWow64DirectoryW'
BASE_SEARCH_PATH_ENABLE_SAFE_SEARCHMODE: UInt32 = 1
BASE_SEARCH_PATH_DISABLE_SAFE_SEARCHMODE: UInt32 = 65536
BASE_SEARCH_PATH_PERMANENT: UInt32 = 32768
COPYFILE2_MESSAGE_COPY_OFFLOAD: Int32 = 1
COPYFILE2_IO_CYCLE_SIZE_MIN: UInt32 = 4096
COPYFILE2_IO_CYCLE_SIZE_MAX: UInt32 = 1073741824
COPYFILE2_IO_RATE_MIN: UInt32 = 512
EVENTLOG_FULL_INFO: UInt32 = 0
OPERATION_API_VERSION: UInt32 = 1
MAX_COMPUTERNAME_LENGTH: UInt32 = 15
LOGON32_PROVIDER_WINNT35: UInt32 = 1
LOGON32_PROVIDER_VIRTUAL: UInt32 = 4
LOGON_ZERO_PASSWORD_BUFFER: UInt32 = 2147483648
HW_PROFILE_GUIDLEN: UInt32 = 39
DOCKINFO_UNDOCKED: UInt32 = 1
DOCKINFO_DOCKED: UInt32 = 2
DOCKINFO_USER_SUPPLIED: UInt32 = 4
TC_NORMAL: UInt32 = 0
TC_HARDERR: UInt32 = 1
TC_GP_TRAP: UInt32 = 2
TC_SIGNAL: UInt32 = 3
AC_LINE_OFFLINE: UInt32 = 0
AC_LINE_ONLINE: UInt32 = 1
AC_LINE_BACKUP_POWER: UInt32 = 2
AC_LINE_UNKNOWN: UInt32 = 255
BATTERY_FLAG_HIGH: UInt32 = 1
BATTERY_FLAG_LOW: UInt32 = 2
BATTERY_FLAG_CRITICAL: UInt32 = 4
BATTERY_FLAG_CHARGING: UInt32 = 8
BATTERY_FLAG_NO_BATTERY: UInt32 = 128
BATTERY_FLAG_UNKNOWN: UInt32 = 255
BATTERY_PERCENTAGE_UNKNOWN: UInt32 = 255
SYSTEM_STATUS_FLAG_POWER_SAVING_ON: UInt32 = 1
BATTERY_LIFE_UNKNOWN: UInt32 = 4294967295
ACTCTX_FLAG_PROCESSOR_ARCHITECTURE_VALID: UInt32 = 1
ACTCTX_FLAG_LANGID_VALID: UInt32 = 2
ACTCTX_FLAG_ASSEMBLY_DIRECTORY_VALID: UInt32 = 4
ACTCTX_FLAG_RESOURCE_NAME_VALID: UInt32 = 8
ACTCTX_FLAG_SET_PROCESS_DEFAULT: UInt32 = 16
ACTCTX_FLAG_APPLICATION_NAME_VALID: UInt32 = 32
ACTCTX_FLAG_SOURCE_IS_ASSEMBLYREF: UInt32 = 64
ACTCTX_FLAG_HMODULE_VALID: UInt32 = 128
DEACTIVATE_ACTCTX_FLAG_FORCE_EARLY_DEACTIVATION: UInt32 = 1
FIND_ACTCTX_SECTION_KEY_RETURN_HACTCTX: UInt32 = 1
FIND_ACTCTX_SECTION_KEY_RETURN_FLAGS: UInt32 = 2
FIND_ACTCTX_SECTION_KEY_RETURN_ASSEMBLY_METADATA: UInt32 = 4
ACTIVATION_CONTEXT_BASIC_INFORMATION_DEFINED: UInt32 = 1
QUERY_ACTCTX_FLAG_USE_ACTIVE_ACTCTX: UInt32 = 4
QUERY_ACTCTX_FLAG_ACTCTX_IS_HMODULE: UInt32 = 8
QUERY_ACTCTX_FLAG_ACTCTX_IS_ADDRESS: UInt32 = 16
QUERY_ACTCTX_FLAG_NO_ADDREF: UInt32 = 2147483648
RESTART_MAX_CMD_LINE: UInt32 = 1024
RECOVERY_DEFAULT_PING_INTERVAL: UInt32 = 5000
FILE_RENAME_FLAG_REPLACE_IF_EXISTS: UInt32 = 1
FILE_RENAME_FLAG_POSIX_SEMANTICS: UInt32 = 2
FILE_RENAME_FLAG_SUPPRESS_PIN_STATE_INHERITANCE: UInt32 = 4
FILE_DISPOSITION_FLAG_DO_NOT_DELETE: UInt32 = 0
FILE_DISPOSITION_FLAG_DELETE: UInt32 = 1
FILE_DISPOSITION_FLAG_POSIX_SEMANTICS: UInt32 = 2
FILE_DISPOSITION_FLAG_FORCE_IMAGE_SECTION_CHECK: UInt32 = 4
FILE_DISPOSITION_FLAG_ON_CLOSE: UInt32 = 8
FILE_DISPOSITION_FLAG_IGNORE_READONLY_ATTRIBUTE: UInt32 = 16
STORAGE_INFO_FLAGS_ALIGNED_DEVICE: UInt32 = 1
STORAGE_INFO_FLAGS_PARTITION_ALIGNED_ON_DEVICE: UInt32 = 2
STORAGE_INFO_OFFSET_UNKNOWN: UInt32 = 4294967295
REMOTE_PROTOCOL_INFO_FLAG_LOOPBACK: UInt32 = 1
REMOTE_PROTOCOL_INFO_FLAG_OFFLINE: UInt32 = 2
REMOTE_PROTOCOL_INFO_FLAG_PERSISTENT_HANDLE: UInt32 = 4
RPI_FLAG_SMB2_SHARECAP_TIMEWARP: UInt32 = 2
RPI_FLAG_SMB2_SHARECAP_DFS: UInt32 = 8
RPI_FLAG_SMB2_SHARECAP_CONTINUOUS_AVAILABILITY: UInt32 = 16
RPI_FLAG_SMB2_SHARECAP_SCALEOUT: UInt32 = 32
RPI_FLAG_SMB2_SHARECAP_CLUSTER: UInt32 = 64
RPI_SMB2_FLAG_SERVERCAP_DFS: UInt32 = 1
RPI_SMB2_FLAG_SERVERCAP_LEASING: UInt32 = 2
RPI_SMB2_FLAG_SERVERCAP_LARGEMTU: UInt32 = 4
RPI_SMB2_FLAG_SERVERCAP_MULTICHANNEL: UInt32 = 8
RPI_SMB2_FLAG_SERVERCAP_PERSISTENT_HANDLES: UInt32 = 16
RPI_SMB2_FLAG_SERVERCAP_DIRECTORY_LEASING: UInt32 = 32
MICROSOFT_WINDOWS_WINBASE_H_DEFINE_INTERLOCKED_CPLUSPLUS_OVERLOADS: UInt32 = 0
MICROSOFT_WINBASE_H_DEFINE_INTERLOCKED_CPLUSPLUS_OVERLOADS: UInt32 = 0
CODEINTEGRITY_OPTION_ENABLED: UInt32 = 1
CODEINTEGRITY_OPTION_TESTSIGN: UInt32 = 2
CODEINTEGRITY_OPTION_UMCI_ENABLED: UInt32 = 4
CODEINTEGRITY_OPTION_UMCI_AUDITMODE_ENABLED: UInt32 = 8
CODEINTEGRITY_OPTION_UMCI_EXCLUSIONPATHS_ENABLED: UInt32 = 16
CODEINTEGRITY_OPTION_TEST_BUILD: UInt32 = 32
CODEINTEGRITY_OPTION_PREPRODUCTION_BUILD: UInt32 = 64
CODEINTEGRITY_OPTION_DEBUGMODE_ENABLED: UInt32 = 128
CODEINTEGRITY_OPTION_FLIGHT_BUILD: UInt32 = 256
CODEINTEGRITY_OPTION_FLIGHTING_ENABLED: UInt32 = 512
CODEINTEGRITY_OPTION_HVCI_KMCI_ENABLED: UInt32 = 1024
CODEINTEGRITY_OPTION_HVCI_KMCI_AUDITMODE_ENABLED: UInt32 = 2048
CODEINTEGRITY_OPTION_HVCI_KMCI_STRICTMODE_ENABLED: UInt32 = 4096
CODEINTEGRITY_OPTION_HVCI_IUM_ENABLED: UInt32 = 8192
FILE_MAXIMUM_DISPOSITION: UInt32 = 5
FILE_DIRECTORY_FILE: UInt32 = 1
FILE_WRITE_THROUGH: UInt32 = 2
FILE_SEQUENTIAL_ONLY: UInt32 = 4
FILE_NO_INTERMEDIATE_BUFFERING: UInt32 = 8
FILE_SYNCHRONOUS_IO_ALERT: UInt32 = 16
FILE_SYNCHRONOUS_IO_NONALERT: UInt32 = 32
FILE_NON_DIRECTORY_FILE: UInt32 = 64
FILE_CREATE_TREE_CONNECTION: UInt32 = 128
FILE_COMPLETE_IF_OPLOCKED: UInt32 = 256
FILE_NO_EA_KNOWLEDGE: UInt32 = 512
FILE_OPEN_REMOTE_INSTANCE: UInt32 = 1024
FILE_RANDOM_ACCESS: UInt32 = 2048
FILE_DELETE_ON_CLOSE: UInt32 = 4096
FILE_OPEN_BY_FILE_ID: UInt32 = 8192
FILE_OPEN_FOR_BACKUP_INTENT: UInt32 = 16384
FILE_NO_COMPRESSION: UInt32 = 32768
FILE_OPEN_REQUIRING_OPLOCK: UInt32 = 65536
FILE_RESERVE_OPFILTER: UInt32 = 1048576
FILE_OPEN_REPARSE_POINT: UInt32 = 2097152
FILE_OPEN_NO_RECALL: UInt32 = 4194304
FILE_OPEN_FOR_FREE_SPACE_QUERY: UInt32 = 8388608
FILE_VALID_OPTION_FLAGS: UInt32 = 16777215
FILE_VALID_PIPE_OPTION_FLAGS: UInt32 = 50
FILE_VALID_MAILSLOT_OPTION_FLAGS: UInt32 = 50
FILE_VALID_SET_FLAGS: UInt32 = 54
FILE_SUPERSEDED: UInt32 = 0
FILE_OPENED: UInt32 = 1
FILE_CREATED: UInt32 = 2
FILE_OVERWRITTEN: UInt32 = 3
FILE_EXISTS: UInt32 = 4
FILE_DOES_NOT_EXIST: UInt32 = 5
WINWATCHNOTIFY_START: UInt32 = 0
WINWATCHNOTIFY_STOP: UInt32 = 1
WINWATCHNOTIFY_DESTROY: UInt32 = 2
WINWATCHNOTIFY_CHANGING: UInt32 = 3
WINWATCHNOTIFY_CHANGED: UInt32 = 4
RSC_FLAG_INF: UInt32 = 1
RSC_FLAG_SKIPDISKSPACECHECK: UInt32 = 2
RSC_FLAG_QUIET: UInt32 = 4
RSC_FLAG_NGCONV: UInt32 = 8
RSC_FLAG_UPDHLPDLLS: UInt32 = 16
RSC_FLAG_DELAYREGISTEROCX: UInt32 = 512
RSC_FLAG_SETUPAPI: UInt32 = 1024
ALINF_QUIET: UInt32 = 4
ALINF_NGCONV: UInt32 = 8
ALINF_UPDHLPDLLS: UInt32 = 16
ALINF_BKINSTALL: UInt32 = 32
ALINF_ROLLBACK: UInt32 = 64
ALINF_CHECKBKDATA: UInt32 = 128
ALINF_ROLLBKDOALL: UInt32 = 256
ALINF_DELAYREGISTEROCX: UInt32 = 512
AIF_WARNIFSKIP: UInt32 = 1
AIF_NOSKIP: UInt32 = 2
AIF_NOVERSIONCHECK: UInt32 = 4
AIF_FORCE_FILE_IN_USE: UInt32 = 8
AIF_NOOVERWRITE: UInt32 = 16
AIF_NO_VERSION_DIALOG: UInt32 = 32
AIF_REPLACEONLY: UInt32 = 1024
AIF_NOLANGUAGECHECK: UInt32 = 268435456
AIF_QUIET: UInt32 = 536870912
IE4_RESTORE: UInt32 = 1
IE4_BACKNEW: UInt32 = 2
IE4_NODELETENEW: UInt32 = 4
IE4_NOMESSAGES: UInt32 = 8
IE4_NOPROGRESS: UInt32 = 16
IE4_NOENUMKEY: UInt32 = 32
IE4_NO_CRC_MAPPING: UInt32 = 64
IE4_REGSECTION: UInt32 = 128
IE4_FRDOALL: UInt32 = 256
IE4_UPDREFCNT: UInt32 = 512
IE4_USEREFCNT: UInt32 = 1024
IE4_EXTRAINCREFCNT: UInt32 = 2048
IE4_REMOVREGBKDATA: UInt32 = 4096
ARSR_RESTORE: UInt32 = 1
ARSR_NOMESSAGES: UInt32 = 8
ARSR_REGSECTION: UInt32 = 128
ARSR_REMOVREGBKDATA: UInt32 = 4096
REG_SAVE_LOG_KEY: String = 'RegSaveLogFile'
REG_RESTORE_LOG_KEY: String = 'RegRestoreLogFile'
AFSR_RESTORE: UInt32 = 1
AFSR_BACKNEW: UInt32 = 2
AFSR_NODELETENEW: UInt32 = 4
AFSR_NOMESSAGES: UInt32 = 8
AFSR_NOPROGRESS: UInt32 = 16
AFSR_UPDREFCNT: UInt32 = 512
AFSR_USEREFCNT: UInt32 = 1024
AFSR_EXTRAINCREFCNT: UInt32 = 2048
AADBE_ADD_ENTRY: UInt32 = 1
AADBE_DEL_ENTRY: UInt32 = 2
ADN_DEL_IF_EMPTY: UInt32 = 1
ADN_DONT_DEL_SUBDIRS: UInt32 = 2
ADN_DONT_DEL_DIR: UInt32 = 4
ADN_DEL_UNC_PATHS: UInt32 = 8
LIS_QUIET: UInt32 = 1
LIS_NOGRPCONV: UInt32 = 2
RUNCMDS_QUIET: UInt32 = 1
RUNCMDS_NOWAIT: UInt32 = 2
RUNCMDS_DELAYPOSTCMD: UInt32 = 4
IME_MAXPROCESS: UInt32 = 32
CP_HWND: UInt32 = 0
CP_OPEN: UInt32 = 1
CP_DIRECT: UInt32 = 2
CP_LEVEL: UInt32 = 3
MCW_DEFAULT: UInt32 = 0
MCW_RECT: UInt32 = 1
MCW_WINDOW: UInt32 = 2
MCW_SCREEN: UInt32 = 4
MCW_VERTICAL: UInt32 = 8
MCW_HIDDEN: UInt32 = 16
IME_MODE_ALPHANUMERIC: UInt32 = 1
IME_MODE_SBCSCHAR: UInt32 = 2
IME_MODE_KATAKANA: UInt32 = 2
IME_MODE_HIRAGANA: UInt32 = 4
IME_MODE_HANJACONVERT: UInt32 = 4
IME_MODE_DBCSCHAR: UInt32 = 16
IME_MODE_ROMAN: UInt32 = 32
IME_MODE_NOROMAN: UInt32 = 64
IME_MODE_CODEINPUT: UInt32 = 128
IME_MODE_NOCODEINPUT: UInt32 = 256
IME_GETIMECAPS: UInt32 = 3
IME_SETOPEN: UInt32 = 4
IME_GETOPEN: UInt32 = 5
IME_GETVERSION: UInt32 = 7
IME_SETCONVERSIONWINDOW: UInt32 = 8
IME_MOVEIMEWINDOW: UInt32 = 8
IME_SETCONVERSIONMODE: UInt32 = 16
IME_GETCONVERSIONMODE: UInt32 = 17
IME_SET_MODE: UInt32 = 18
IME_SENDVKEY: UInt32 = 19
IME_ENTERWORDREGISTERMODE: UInt32 = 24
IME_SETCONVERSIONFONTEX: UInt32 = 25
IME_BANJAtoJUNJA: UInt32 = 19
IME_JUNJAtoBANJA: UInt32 = 20
IME_JOHABtoKS: UInt32 = 21
IME_KStoJOHAB: UInt32 = 22
IMEA_INIT: UInt32 = 1
IMEA_NEXT: UInt32 = 2
IMEA_PREV: UInt32 = 3
IME_REQUEST_CONVERT: UInt32 = 1
IME_ENABLE_CONVERT: UInt32 = 2
INTERIM_WINDOW: UInt32 = 0
MODE_WINDOW: UInt32 = 1
HANJA_WINDOW: UInt32 = 2
IME_RS_ERROR: UInt32 = 1
IME_RS_NOIME: UInt32 = 2
IME_RS_TOOLONG: UInt32 = 5
IME_RS_ILLEGAL: UInt32 = 6
IME_RS_NOTFOUND: UInt32 = 7
IME_RS_NOROOM: UInt32 = 10
IME_RS_DISKERROR: UInt32 = 14
IME_RS_INVALID: UInt32 = 17
IME_RS_NEST: UInt32 = 18
IME_RS_SYSTEMMODAL: UInt32 = 19
WM_IME_REPORT: UInt32 = 640
IR_STRINGSTART: UInt32 = 256
IR_STRINGEND: UInt32 = 257
IR_OPENCONVERT: UInt32 = 288
IR_CHANGECONVERT: UInt32 = 289
IR_CLOSECONVERT: UInt32 = 290
IR_FULLCONVERT: UInt32 = 291
IR_IMESELECT: UInt32 = 304
IR_STRING: UInt32 = 320
IR_DBCSCHAR: UInt32 = 352
IR_UNDETERMINE: UInt32 = 368
IR_STRINGEX: UInt32 = 384
IR_MODEINFO: UInt32 = 400
WM_WNT_CONVERTREQUESTEX: UInt32 = 265
WM_CONVERTREQUEST: UInt32 = 266
WM_CONVERTRESULT: UInt32 = 267
WM_INTERIM: UInt32 = 268
WM_IMEKEYDOWN: UInt32 = 656
WM_IMEKEYUP: UInt32 = 657
DELAYLOAD_GPA_FAILURE: UInt32 = 4
CATID_DeleteBrowsingHistory: Guid = Guid('31caf6e4-d6aa-4090-a0-50-a5-ac-89-72-e9-ef')
DELETE_BROWSING_HISTORY_HISTORY: UInt32 = 1
DELETE_BROWSING_HISTORY_COOKIES: UInt32 = 2
DELETE_BROWSING_HISTORY_TIF: UInt32 = 4
DELETE_BROWSING_HISTORY_FORMDATA: UInt32 = 8
DELETE_BROWSING_HISTORY_PASSWORDS: UInt32 = 16
DELETE_BROWSING_HISTORY_PRESERVEFAVORITES: UInt32 = 32
DELETE_BROWSING_HISTORY_DOWNLOADHISTORY: UInt32 = 64
if ARCH in 'X64,ARM64':
    @winfunctype('KERNEL32.dll')
    def uaw_lstrcmpW(String1: POINTER(UInt16), String2: POINTER(UInt16)) -> Int32: ...
if ARCH in 'X64,ARM64':
    @winfunctype('KERNEL32.dll')
    def uaw_lstrcmpiW(String1: POINTER(UInt16), String2: POINTER(UInt16)) -> Int32: ...
if ARCH in 'X64,ARM64':
    @winfunctype('KERNEL32.dll')
    def uaw_lstrlenW(String: POINTER(UInt16)) -> Int32: ...
if ARCH in 'X64,ARM64':
    @winfunctype('KERNEL32.dll')
    def uaw_wcschr(String: POINTER(UInt16), Character: Char) -> POINTER(UInt16): ...
if ARCH in 'X64,ARM64':
    @winfunctype('KERNEL32.dll')
    def uaw_wcscpy(Destination: POINTER(UInt16), Source: POINTER(UInt16)) -> POINTER(UInt16): ...
if ARCH in 'X64,ARM64':
    @winfunctype('KERNEL32.dll')
    def uaw_wcsicmp(String1: POINTER(UInt16), String2: POINTER(UInt16)) -> Int32: ...
if ARCH in 'X64,ARM64':
    @winfunctype('KERNEL32.dll')
    def uaw_wcslen(String: POINTER(UInt16)) -> UIntPtr: ...
if ARCH in 'X64,ARM64':
    @winfunctype('KERNEL32.dll')
    def uaw_wcsrchr(String: POINTER(UInt16), Character: Char) -> POINTER(UInt16): ...
@winfunctype('ntdll.dll')
def RtlGetReturnAddressHijackTarget() -> UIntPtr: ...
@winfunctype('ntdll.dll')
def RtlRaiseCustomSystemEventTrigger(TriggerConfig: POINTER(Windows.Win32.System.WindowsProgramming.CUSTOM_SYSTEM_EVENT_TRIGGER_CONFIG_head)) -> UInt32: ...
@winfunctype('api-ms-win-core-apiquery-l2-1-0.dll')
def IsApiSetImplemented(Contract: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def QueryThreadCycleTime(ThreadHandle: Windows.Win32.Foundation.HANDLE, CycleTime: POINTER(UInt64)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def QueryProcessCycleTime(ProcessHandle: Windows.Win32.Foundation.HANDLE, CycleTime: POINTER(UInt64)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def QueryIdleProcessorCycleTime(BufferLength: POINTER(UInt32), ProcessorIdleCycleTime: POINTER(UInt64)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def QueryIdleProcessorCycleTimeEx(Group: UInt16, BufferLength: POINTER(UInt32), ProcessorIdleCycleTime: POINTER(UInt64)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-realtime-l1-1-1.dll')
def QueryInterruptTimePrecise(lpInterruptTimePrecise: POINTER(UInt64)) -> Void: ...
@winfunctype('api-ms-win-core-realtime-l1-1-1.dll')
def QueryUnbiasedInterruptTimePrecise(lpUnbiasedInterruptTimePrecise: POINTER(UInt64)) -> Void: ...
@winfunctype('api-ms-win-core-realtime-l1-1-1.dll')
def QueryInterruptTime(lpInterruptTime: POINTER(UInt64)) -> Void: ...
@winfunctype('KERNEL32.dll')
def QueryUnbiasedInterruptTime(UnbiasedTime: POINTER(UInt64)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-realtime-l1-1-2.dll')
def QueryAuxiliaryCounterFrequency(lpAuxiliaryCounterFrequency: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-realtime-l1-1-2.dll')
def ConvertAuxiliaryCounterToPerformanceCounter(ullAuxiliaryCounterValue: UInt64, lpPerformanceCounterValue: POINTER(UInt64), lpConversionError: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-realtime-l1-1-2.dll')
def ConvertPerformanceCounterToAuxiliaryCounter(ullPerformanceCounterValue: UInt64, lpAuxiliaryCounterValue: POINTER(UInt64), lpConversionError: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def GlobalCompact(dwMinFree: UInt32) -> UIntPtr: ...
@winfunctype('KERNEL32.dll')
def GlobalFix(hMem: Windows.Win32.Foundation.HGLOBAL) -> Void: ...
@winfunctype('KERNEL32.dll')
def GlobalUnfix(hMem: Windows.Win32.Foundation.HGLOBAL) -> Void: ...
@winfunctype('KERNEL32.dll')
def GlobalWire(hMem: Windows.Win32.Foundation.HGLOBAL) -> c_void_p: ...
@winfunctype('KERNEL32.dll')
def GlobalUnWire(hMem: Windows.Win32.Foundation.HGLOBAL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def LocalShrink(hMem: Windows.Win32.Foundation.HLOCAL, cbNewSize: UInt32) -> UIntPtr: ...
@winfunctype('KERNEL32.dll')
def LocalCompact(uMinFree: UInt32) -> UIntPtr: ...
@winfunctype('KERNEL32.dll')
def SetEnvironmentStringsA(NewEnvironment: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetHandleCount(uNumber: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def RequestDeviceWakeup(hDevice: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CancelDeviceWakeupRequest(hDevice: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetMessageWaitingIndicator(hMsgIndicator: Windows.Win32.Foundation.HANDLE, ulMsgCount: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def MulDiv(nNumber: Int32, nNumerator: Int32, nDenominator: Int32) -> Int32: ...
@winfunctype('KERNEL32.dll')
def GetSystemRegistryQuota(pdwQuotaAllowed: POINTER(UInt32), pdwQuotaUsed: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FileTimeToDosDateTime(lpFileTime: POINTER(Windows.Win32.Foundation.FILETIME_head), lpFatDate: POINTER(UInt16), lpFatTime: POINTER(UInt16)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DosDateTimeToFileTime(wFatDate: UInt16, wFatTime: UInt16, lpFileTime: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def _lopen(lpPathName: Windows.Win32.Foundation.PSTR, iReadWrite: Int32) -> Int32: ...
@winfunctype('KERNEL32.dll')
def _lcreat(lpPathName: Windows.Win32.Foundation.PSTR, iAttribute: Int32) -> Int32: ...
@winfunctype('KERNEL32.dll')
def _lread(hFile: Int32, lpBuffer: c_void_p, uBytes: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def _lwrite(hFile: Int32, lpBuffer: Windows.Win32.Foundation.PSTR, uBytes: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def _hread(hFile: Int32, lpBuffer: c_void_p, lBytes: Int32) -> Int32: ...
@winfunctype('KERNEL32.dll')
def _hwrite(hFile: Int32, lpBuffer: Windows.Win32.Foundation.PSTR, lBytes: Int32) -> Int32: ...
@winfunctype('KERNEL32.dll')
def _lclose(hFile: Int32) -> Int32: ...
@winfunctype('KERNEL32.dll')
def _llseek(hFile: Int32, lOffset: Int32, iOrigin: Int32) -> Int32: ...
@winfunctype('KERNEL32.dll')
def SignalObjectAndWait(hObjectToSignal: Windows.Win32.Foundation.HANDLE, hObjectToWaitOn: Windows.Win32.Foundation.HANDLE, dwMilliseconds: UInt32, bAlertable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def OpenMutexA(dwDesiredAccess: UInt32, bInheritHandle: Windows.Win32.Foundation.BOOL, lpName: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def OpenSemaphoreA(dwDesiredAccess: UInt32, bInheritHandle: Windows.Win32.Foundation.BOOL, lpName: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def CreateWaitableTimerA(lpTimerAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head), bManualReset: Windows.Win32.Foundation.BOOL, lpTimerName: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def OpenWaitableTimerA(dwDesiredAccess: UInt32, bInheritHandle: Windows.Win32.Foundation.BOOL, lpTimerName: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def CreateWaitableTimerExA(lpTimerAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head), lpTimerName: Windows.Win32.Foundation.PSTR, dwFlags: UInt32, dwDesiredAccess: UInt32) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def GetFirmwareEnvironmentVariableA(lpName: Windows.Win32.Foundation.PSTR, lpGuid: Windows.Win32.Foundation.PSTR, pBuffer: c_void_p, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetFirmwareEnvironmentVariableW(lpName: Windows.Win32.Foundation.PWSTR, lpGuid: Windows.Win32.Foundation.PWSTR, pBuffer: c_void_p, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetFirmwareEnvironmentVariableExA(lpName: Windows.Win32.Foundation.PSTR, lpGuid: Windows.Win32.Foundation.PSTR, pBuffer: c_void_p, nSize: UInt32, pdwAttribubutes: POINTER(UInt32)) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetFirmwareEnvironmentVariableExW(lpName: Windows.Win32.Foundation.PWSTR, lpGuid: Windows.Win32.Foundation.PWSTR, pBuffer: c_void_p, nSize: UInt32, pdwAttribubutes: POINTER(UInt32)) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def SetFirmwareEnvironmentVariableA(lpName: Windows.Win32.Foundation.PSTR, lpGuid: Windows.Win32.Foundation.PSTR, pValue: c_void_p, nSize: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetFirmwareEnvironmentVariableW(lpName: Windows.Win32.Foundation.PWSTR, lpGuid: Windows.Win32.Foundation.PWSTR, pValue: c_void_p, nSize: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetFirmwareEnvironmentVariableExA(lpName: Windows.Win32.Foundation.PSTR, lpGuid: Windows.Win32.Foundation.PSTR, pValue: c_void_p, nSize: UInt32, dwAttributes: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetFirmwareEnvironmentVariableExW(lpName: Windows.Win32.Foundation.PWSTR, lpGuid: Windows.Win32.Foundation.PWSTR, pValue: c_void_p, nSize: UInt32, dwAttributes: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def IsNativeVhdBoot(NativeVhdBoot: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetProfileIntA(lpAppName: Windows.Win32.Foundation.PSTR, lpKeyName: Windows.Win32.Foundation.PSTR, nDefault: Int32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetProfileIntW(lpAppName: Windows.Win32.Foundation.PWSTR, lpKeyName: Windows.Win32.Foundation.PWSTR, nDefault: Int32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetProfileStringA(lpAppName: Windows.Win32.Foundation.PSTR, lpKeyName: Windows.Win32.Foundation.PSTR, lpDefault: Windows.Win32.Foundation.PSTR, lpReturnedString: Windows.Win32.Foundation.PSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetProfileStringW(lpAppName: Windows.Win32.Foundation.PWSTR, lpKeyName: Windows.Win32.Foundation.PWSTR, lpDefault: Windows.Win32.Foundation.PWSTR, lpReturnedString: Windows.Win32.Foundation.PWSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def WriteProfileStringA(lpAppName: Windows.Win32.Foundation.PSTR, lpKeyName: Windows.Win32.Foundation.PSTR, lpString: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WriteProfileStringW(lpAppName: Windows.Win32.Foundation.PWSTR, lpKeyName: Windows.Win32.Foundation.PWSTR, lpString: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetProfileSectionA(lpAppName: Windows.Win32.Foundation.PSTR, lpReturnedString: Windows.Win32.Foundation.PSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetProfileSectionW(lpAppName: Windows.Win32.Foundation.PWSTR, lpReturnedString: Windows.Win32.Foundation.PWSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def WriteProfileSectionA(lpAppName: Windows.Win32.Foundation.PSTR, lpString: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WriteProfileSectionW(lpAppName: Windows.Win32.Foundation.PWSTR, lpString: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetPrivateProfileIntA(lpAppName: Windows.Win32.Foundation.PSTR, lpKeyName: Windows.Win32.Foundation.PSTR, nDefault: Int32, lpFileName: Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetPrivateProfileIntW(lpAppName: Windows.Win32.Foundation.PWSTR, lpKeyName: Windows.Win32.Foundation.PWSTR, nDefault: Int32, lpFileName: Windows.Win32.Foundation.PWSTR) -> Int32: ...
@winfunctype('KERNEL32.dll')
def GetPrivateProfileStringA(lpAppName: Windows.Win32.Foundation.PSTR, lpKeyName: Windows.Win32.Foundation.PSTR, lpDefault: Windows.Win32.Foundation.PSTR, lpReturnedString: Windows.Win32.Foundation.PSTR, nSize: UInt32, lpFileName: Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetPrivateProfileStringW(lpAppName: Windows.Win32.Foundation.PWSTR, lpKeyName: Windows.Win32.Foundation.PWSTR, lpDefault: Windows.Win32.Foundation.PWSTR, lpReturnedString: Windows.Win32.Foundation.PWSTR, nSize: UInt32, lpFileName: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def WritePrivateProfileStringA(lpAppName: Windows.Win32.Foundation.PSTR, lpKeyName: Windows.Win32.Foundation.PSTR, lpString: Windows.Win32.Foundation.PSTR, lpFileName: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WritePrivateProfileStringW(lpAppName: Windows.Win32.Foundation.PWSTR, lpKeyName: Windows.Win32.Foundation.PWSTR, lpString: Windows.Win32.Foundation.PWSTR, lpFileName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetPrivateProfileSectionA(lpAppName: Windows.Win32.Foundation.PSTR, lpReturnedString: Windows.Win32.Foundation.PSTR, nSize: UInt32, lpFileName: Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetPrivateProfileSectionW(lpAppName: Windows.Win32.Foundation.PWSTR, lpReturnedString: Windows.Win32.Foundation.PWSTR, nSize: UInt32, lpFileName: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def WritePrivateProfileSectionA(lpAppName: Windows.Win32.Foundation.PSTR, lpString: Windows.Win32.Foundation.PSTR, lpFileName: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WritePrivateProfileSectionW(lpAppName: Windows.Win32.Foundation.PWSTR, lpString: Windows.Win32.Foundation.PWSTR, lpFileName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetPrivateProfileSectionNamesA(lpszReturnBuffer: Windows.Win32.Foundation.PSTR, nSize: UInt32, lpFileName: Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetPrivateProfileSectionNamesW(lpszReturnBuffer: Windows.Win32.Foundation.PWSTR, nSize: UInt32, lpFileName: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetPrivateProfileStructA(lpszSection: Windows.Win32.Foundation.PSTR, lpszKey: Windows.Win32.Foundation.PSTR, lpStruct: c_void_p, uSizeStruct: UInt32, szFile: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetPrivateProfileStructW(lpszSection: Windows.Win32.Foundation.PWSTR, lpszKey: Windows.Win32.Foundation.PWSTR, lpStruct: c_void_p, uSizeStruct: UInt32, szFile: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WritePrivateProfileStructA(lpszSection: Windows.Win32.Foundation.PSTR, lpszKey: Windows.Win32.Foundation.PSTR, lpStruct: c_void_p, uSizeStruct: UInt32, szFile: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WritePrivateProfileStructW(lpszSection: Windows.Win32.Foundation.PWSTR, lpszKey: Windows.Win32.Foundation.PWSTR, lpStruct: c_void_p, uSizeStruct: UInt32, szFile: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def IsBadHugeReadPtr(lp: c_void_p, ucb: UIntPtr) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def IsBadHugeWritePtr(lp: c_void_p, ucb: UIntPtr) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetComputerNameA(lpBuffer: Windows.Win32.Foundation.PSTR, nSize: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetComputerNameW(lpBuffer: Windows.Win32.Foundation.PWSTR, nSize: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DnsHostnameToComputerNameA(Hostname: Windows.Win32.Foundation.PSTR, ComputerName: Windows.Win32.Foundation.PSTR, nSize: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DnsHostnameToComputerNameW(Hostname: Windows.Win32.Foundation.PWSTR, ComputerName: Windows.Win32.Foundation.PWSTR, nSize: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def GetUserNameA(lpBuffer: Windows.Win32.Foundation.PSTR, pcbBuffer: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def GetUserNameW(lpBuffer: Windows.Win32.Foundation.PWSTR, pcbBuffer: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def IsTokenUntrusted(TokenHandle: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CancelTimerQueueTimer(TimerQueue: Windows.Win32.Foundation.HANDLE, Timer: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def GetCurrentHwProfileA(lpHwProfileInfo: POINTER(Windows.Win32.System.WindowsProgramming.HW_PROFILE_INFOA_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def GetCurrentHwProfileW(lpHwProfileInfo: POINTER(Windows.Win32.System.WindowsProgramming.HW_PROFILE_INFOW_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ReplacePartitionUnit(TargetPartition: Windows.Win32.Foundation.PWSTR, SparePartition: Windows.Win32.Foundation.PWSTR, Flags: UInt32) -> Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X86,X64':
    @winfunctype('KERNEL32.dll')
    def GetThreadEnabledXStateFeatures() -> UInt64: ...
if ARCH in 'X86,X64':
    @winfunctype('KERNEL32.dll')
    def EnableProcessOptionalXStateFeatures(Features: UInt64) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-backgroundtask-l1-1-0.dll')
def RaiseCustomSystemEventTrigger(CustomSystemEventTriggerConfig: POINTER(Windows.Win32.System.WindowsProgramming.CUSTOM_SYSTEM_EVENT_TRIGGER_CONFIG_head)) -> UInt32: ...
@winfunctype('ntdll.dll')
def NtClose(Handle: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtOpenFile(FileHandle: POINTER(Windows.Win32.Foundation.HANDLE), DesiredAccess: UInt32, ObjectAttributes: POINTER(Windows.Win32.System.WindowsProgramming.OBJECT_ATTRIBUTES_head), IoStatusBlock: POINTER(Windows.Win32.System.WindowsProgramming.IO_STATUS_BLOCK_head), ShareAccess: UInt32, OpenOptions: UInt32) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtRenameKey(KeyHandle: Windows.Win32.Foundation.HANDLE, NewName: POINTER(Windows.Win32.Foundation.UNICODE_STRING_head)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtNotifyChangeMultipleKeys(MasterKeyHandle: Windows.Win32.Foundation.HANDLE, Count: UInt32, SubordinateObjects: POINTER(Windows.Win32.System.WindowsProgramming.OBJECT_ATTRIBUTES_head), Event: Windows.Win32.Foundation.HANDLE, ApcRoutine: Windows.Win32.System.WindowsProgramming.PIO_APC_ROUTINE, ApcContext: c_void_p, IoStatusBlock: POINTER(Windows.Win32.System.WindowsProgramming.IO_STATUS_BLOCK_head), CompletionFilter: UInt32, WatchTree: Windows.Win32.Foundation.BOOLEAN, Buffer: c_void_p, BufferSize: UInt32, Asynchronous: Windows.Win32.Foundation.BOOLEAN) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtQueryMultipleValueKey(KeyHandle: Windows.Win32.Foundation.HANDLE, ValueEntries: POINTER(Windows.Win32.System.WindowsProgramming.KEY_VALUE_ENTRY_head), EntryCount: UInt32, ValueBuffer: c_void_p, BufferLength: POINTER(UInt32), RequiredBufferLength: POINTER(UInt32)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtSetInformationKey(KeyHandle: Windows.Win32.Foundation.HANDLE, KeySetInformationClass: Windows.Win32.System.WindowsProgramming.KEY_SET_INFORMATION_CLASS, KeySetInformation: c_void_p, KeySetInformationLength: UInt32) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtDeviceIoControlFile(FileHandle: Windows.Win32.Foundation.HANDLE, Event: Windows.Win32.Foundation.HANDLE, ApcRoutine: Windows.Win32.System.WindowsProgramming.PIO_APC_ROUTINE, ApcContext: c_void_p, IoStatusBlock: POINTER(Windows.Win32.System.WindowsProgramming.IO_STATUS_BLOCK_head), IoControlCode: UInt32, InputBuffer: c_void_p, InputBufferLength: UInt32, OutputBuffer: c_void_p, OutputBufferLength: UInt32) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtWaitForSingleObject(Handle: Windows.Win32.Foundation.HANDLE, Alertable: Windows.Win32.Foundation.BOOLEAN, Timeout: POINTER(Windows.Win32.Foundation.LARGE_INTEGER_head)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def RtlIsNameLegalDOS8Dot3(Name: POINTER(Windows.Win32.Foundation.UNICODE_STRING_head), OemName: POINTER(Windows.Win32.System.Kernel.STRING_head), NameContainsSpaces: POINTER(Windows.Win32.Foundation.BOOLEAN)) -> Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('ntdll.dll')
def NtQueryObject(Handle: Windows.Win32.Foundation.HANDLE, ObjectInformationClass: Windows.Win32.System.WindowsProgramming.OBJECT_INFORMATION_CLASS, ObjectInformation: c_void_p, ObjectInformationLength: UInt32, ReturnLength: POINTER(UInt32)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtQuerySystemInformation(SystemInformationClass: Windows.Win32.System.WindowsProgramming.SYSTEM_INFORMATION_CLASS, SystemInformation: c_void_p, SystemInformationLength: UInt32, ReturnLength: POINTER(UInt32)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtQuerySystemTime(SystemTime: POINTER(Windows.Win32.Foundation.LARGE_INTEGER_head)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtQueryTimerResolution(MaximumTime: POINTER(UInt32), MinimumTime: POINTER(UInt32), CurrentTime: POINTER(UInt32)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def RtlLocalTimeToSystemTime(LocalTime: POINTER(Windows.Win32.Foundation.LARGE_INTEGER_head), SystemTime: POINTER(Windows.Win32.Foundation.LARGE_INTEGER_head)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def RtlTimeToSecondsSince1970(Time: POINTER(Windows.Win32.Foundation.LARGE_INTEGER_head), ElapsedSeconds: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('ntdll.dll')
def RtlFreeAnsiString(AnsiString: POINTER(Windows.Win32.System.Kernel.STRING_head)) -> Void: ...
@winfunctype('ntdll.dll')
def RtlFreeUnicodeString(UnicodeString: POINTER(Windows.Win32.Foundation.UNICODE_STRING_head)) -> Void: ...
@winfunctype('ntdll.dll')
def RtlFreeOemString(OemString: POINTER(Windows.Win32.System.Kernel.STRING_head)) -> Void: ...
@winfunctype('ntdll.dll')
def RtlInitString(DestinationString: POINTER(Windows.Win32.System.Kernel.STRING_head), SourceString: POINTER(SByte)) -> Void: ...
@winfunctype('ntdll.dll')
def RtlInitStringEx(DestinationString: POINTER(Windows.Win32.System.Kernel.STRING_head), SourceString: POINTER(SByte)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def RtlInitAnsiString(DestinationString: POINTER(Windows.Win32.System.Kernel.STRING_head), SourceString: POINTER(SByte)) -> Void: ...
@winfunctype('ntdll.dll')
def RtlInitAnsiStringEx(DestinationString: POINTER(Windows.Win32.System.Kernel.STRING_head), SourceString: POINTER(SByte)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def RtlInitUnicodeString(DestinationString: POINTER(Windows.Win32.Foundation.UNICODE_STRING_head), SourceString: Windows.Win32.Foundation.PWSTR) -> Void: ...
@winfunctype('ntdll.dll')
def RtlAnsiStringToUnicodeString(DestinationString: POINTER(Windows.Win32.Foundation.UNICODE_STRING_head), SourceString: POINTER(Windows.Win32.System.Kernel.STRING_head), AllocateDestinationString: Windows.Win32.Foundation.BOOLEAN) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def RtlUnicodeStringToAnsiString(DestinationString: POINTER(Windows.Win32.System.Kernel.STRING_head), SourceString: POINTER(Windows.Win32.Foundation.UNICODE_STRING_head), AllocateDestinationString: Windows.Win32.Foundation.BOOLEAN) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def RtlUnicodeStringToOemString(DestinationString: POINTER(Windows.Win32.System.Kernel.STRING_head), SourceString: POINTER(Windows.Win32.Foundation.UNICODE_STRING_head), AllocateDestinationString: Windows.Win32.Foundation.BOOLEAN) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def RtlUnicodeToMultiByteSize(BytesInMultiByteString: POINTER(UInt32), UnicodeString: Windows.Win32.Foundation.PWSTR, BytesInUnicodeString: UInt32) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def RtlCharToInteger(String: POINTER(SByte), Base: UInt32, Value: POINTER(UInt32)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def RtlUniform(Seed: POINTER(UInt32)) -> UInt32: ...
@winfunctype('api-ms-win-core-featurestaging-l1-1-0.dll')
def GetFeatureEnabledState(featureId: UInt32, changeTime: Windows.Win32.System.WindowsProgramming.FEATURE_CHANGE_TIME) -> Windows.Win32.System.WindowsProgramming.FEATURE_ENABLED_STATE: ...
@winfunctype('api-ms-win-core-featurestaging-l1-1-0.dll')
def RecordFeatureUsage(featureId: UInt32, kind: UInt32, addend: UInt32, originName: Windows.Win32.Foundation.PSTR) -> Void: ...
@winfunctype('api-ms-win-core-featurestaging-l1-1-0.dll')
def RecordFeatureError(featureId: UInt32, error: POINTER(Windows.Win32.System.WindowsProgramming.FEATURE_ERROR_head)) -> Void: ...
@winfunctype('api-ms-win-core-featurestaging-l1-1-0.dll')
def SubscribeFeatureStateChangeNotification(subscription: POINTER(Windows.Win32.System.WindowsProgramming.FEATURE_STATE_CHANGE_SUBSCRIPTION), callback: Windows.Win32.System.WindowsProgramming.PFEATURE_STATE_CHANGE_CALLBACK, context: c_void_p) -> Void: ...
@winfunctype('api-ms-win-core-featurestaging-l1-1-0.dll')
def UnsubscribeFeatureStateChangeNotification(subscription: Windows.Win32.System.WindowsProgramming.FEATURE_STATE_CHANGE_SUBSCRIPTION) -> Void: ...
@winfunctype('api-ms-win-core-featurestaging-l1-1-1.dll')
def GetFeatureVariant(featureId: UInt32, changeTime: Windows.Win32.System.WindowsProgramming.FEATURE_CHANGE_TIME, payloadId: POINTER(UInt32), hasNotification: POINTER(Windows.Win32.Foundation.BOOL)) -> UInt32: ...
@winfunctype('DCIMAN32.dll')
def DCIOpenProvider() -> Windows.Win32.Graphics.Gdi.HDC: ...
@winfunctype('DCIMAN32.dll')
def DCICloseProvider(hdc: Windows.Win32.Graphics.Gdi.HDC) -> Void: ...
@winfunctype('DCIMAN32.dll')
def DCICreatePrimary(hdc: Windows.Win32.Graphics.Gdi.HDC, lplpSurface: POINTER(POINTER(Windows.Win32.System.WindowsProgramming.DCISURFACEINFO_head))) -> Int32: ...
@winfunctype('DCIMAN32.dll')
def DCICreateOffscreen(hdc: Windows.Win32.Graphics.Gdi.HDC, dwCompression: UInt32, dwRedMask: UInt32, dwGreenMask: UInt32, dwBlueMask: UInt32, dwWidth: UInt32, dwHeight: UInt32, dwDCICaps: UInt32, dwBitCount: UInt32, lplpSurface: POINTER(POINTER(Windows.Win32.System.WindowsProgramming.DCIOFFSCREEN_head))) -> Int32: ...
@winfunctype('DCIMAN32.dll')
def DCICreateOverlay(hdc: Windows.Win32.Graphics.Gdi.HDC, lpOffscreenSurf: c_void_p, lplpSurface: POINTER(POINTER(Windows.Win32.System.WindowsProgramming.DCIOVERLAY_head))) -> Int32: ...
@winfunctype('DCIMAN32.dll')
def DCIEnum(hdc: Windows.Win32.Graphics.Gdi.HDC, lprDst: POINTER(Windows.Win32.Foundation.RECT_head), lprSrc: POINTER(Windows.Win32.Foundation.RECT_head), lpFnCallback: c_void_p, lpContext: c_void_p) -> Int32: ...
@winfunctype('DCIMAN32.dll')
def DCISetSrcDestClip(pdci: POINTER(Windows.Win32.System.WindowsProgramming.DCIOFFSCREEN_head), srcrc: POINTER(Windows.Win32.Foundation.RECT_head), destrc: POINTER(Windows.Win32.Foundation.RECT_head), prd: POINTER(Windows.Win32.Graphics.Gdi.RGNDATA_head)) -> Int32: ...
@winfunctype('DCIMAN32.dll')
def WinWatchOpen(hwnd: Windows.Win32.Foundation.HWND) -> Windows.Win32.System.WindowsProgramming.HWINWATCH: ...
@winfunctype('DCIMAN32.dll')
def WinWatchClose(hWW: Windows.Win32.System.WindowsProgramming.HWINWATCH) -> Void: ...
@winfunctype('DCIMAN32.dll')
def WinWatchGetClipList(hWW: Windows.Win32.System.WindowsProgramming.HWINWATCH, prc: POINTER(Windows.Win32.Foundation.RECT_head), size: UInt32, prd: POINTER(Windows.Win32.Graphics.Gdi.RGNDATA_head)) -> UInt32: ...
@winfunctype('DCIMAN32.dll')
def WinWatchDidStatusChange(hWW: Windows.Win32.System.WindowsProgramming.HWINWATCH) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('DCIMAN32.dll')
def GetWindowRegionData(hwnd: Windows.Win32.Foundation.HWND, size: UInt32, prd: POINTER(Windows.Win32.Graphics.Gdi.RGNDATA_head)) -> UInt32: ...
@winfunctype('DCIMAN32.dll')
def GetDCRegionData(hdc: Windows.Win32.Graphics.Gdi.HDC, size: UInt32, prd: POINTER(Windows.Win32.Graphics.Gdi.RGNDATA_head)) -> UInt32: ...
@winfunctype('DCIMAN32.dll')
def WinWatchNotify(hWW: Windows.Win32.System.WindowsProgramming.HWINWATCH, NotifyCallback: Windows.Win32.System.WindowsProgramming.WINWATCHNOTIFYPROC, NotifyParam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('DCIMAN32.dll')
def DCIEndAccess(pdci: POINTER(Windows.Win32.System.WindowsProgramming.DCISURFACEINFO_head)) -> Void: ...
@winfunctype('DCIMAN32.dll')
def DCIBeginAccess(pdci: POINTER(Windows.Win32.System.WindowsProgramming.DCISURFACEINFO_head), x: Int32, y: Int32, dx: Int32, dy: Int32) -> Int32: ...
@winfunctype('DCIMAN32.dll')
def DCIDestroy(pdci: POINTER(Windows.Win32.System.WindowsProgramming.DCISURFACEINFO_head)) -> Void: ...
@winfunctype('DCIMAN32.dll')
def DCIDraw(pdci: POINTER(Windows.Win32.System.WindowsProgramming.DCIOFFSCREEN_head)) -> Int32: ...
@winfunctype('DCIMAN32.dll')
def DCISetClipList(pdci: POINTER(Windows.Win32.System.WindowsProgramming.DCIOFFSCREEN_head), prd: POINTER(Windows.Win32.Graphics.Gdi.RGNDATA_head)) -> Int32: ...
@winfunctype('DCIMAN32.dll')
def DCISetDestination(pdci: POINTER(Windows.Win32.System.WindowsProgramming.DCIOFFSCREEN_head), dst: POINTER(Windows.Win32.Foundation.RECT_head), src: POINTER(Windows.Win32.Foundation.RECT_head)) -> Int32: ...
@winfunctype('api-ms-win-dx-d3dkmt-l1-1-0.dll')
def GdiEntry13() -> UInt32: ...
@winfunctype('ADVPACK.dll')
def RunSetupCommandA(hWnd: Windows.Win32.Foundation.HWND, szCmdName: Windows.Win32.Foundation.PSTR, szInfSection: Windows.Win32.Foundation.PSTR, szDir: Windows.Win32.Foundation.PSTR, lpszTitle: Windows.Win32.Foundation.PSTR, phEXE: POINTER(Windows.Win32.Foundation.HANDLE), dwFlags: UInt32, pvReserved: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ADVPACK.dll')
def RunSetupCommandW(hWnd: Windows.Win32.Foundation.HWND, szCmdName: Windows.Win32.Foundation.PWSTR, szInfSection: Windows.Win32.Foundation.PWSTR, szDir: Windows.Win32.Foundation.PWSTR, lpszTitle: Windows.Win32.Foundation.PWSTR, phEXE: POINTER(Windows.Win32.Foundation.HANDLE), dwFlags: UInt32, pvReserved: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ADVPACK.dll')
def NeedRebootInit() -> UInt32: ...
@winfunctype('ADVPACK.dll')
def NeedReboot(dwRebootCheck: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVPACK.dll')
def RebootCheckOnInstallA(hwnd: Windows.Win32.Foundation.HWND, pszINF: Windows.Win32.Foundation.PSTR, pszSec: Windows.Win32.Foundation.PSTR, dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ADVPACK.dll')
def RebootCheckOnInstallW(hwnd: Windows.Win32.Foundation.HWND, pszINF: Windows.Win32.Foundation.PWSTR, pszSec: Windows.Win32.Foundation.PWSTR, dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ADVPACK.dll')
def TranslateInfStringA(pszInfFilename: Windows.Win32.Foundation.PSTR, pszInstallSection: Windows.Win32.Foundation.PSTR, pszTranslateSection: Windows.Win32.Foundation.PSTR, pszTranslateKey: Windows.Win32.Foundation.PSTR, pszBuffer: Windows.Win32.Foundation.PSTR, cchBuffer: UInt32, pdwRequiredSize: POINTER(UInt32), pvReserved: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ADVPACK.dll')
def TranslateInfStringW(pszInfFilename: Windows.Win32.Foundation.PWSTR, pszInstallSection: Windows.Win32.Foundation.PWSTR, pszTranslateSection: Windows.Win32.Foundation.PWSTR, pszTranslateKey: Windows.Win32.Foundation.PWSTR, pszBuffer: Windows.Win32.Foundation.PWSTR, cchBuffer: UInt32, pdwRequiredSize: POINTER(UInt32), pvReserved: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ADVPACK.dll')
def RegInstallA(hmod: Windows.Win32.Foundation.HINSTANCE, pszSection: Windows.Win32.Foundation.PSTR, pstTable: POINTER(Windows.Win32.System.WindowsProgramming.STRTABLEA_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ADVPACK.dll')
def RegInstallW(hmod: Windows.Win32.Foundation.HINSTANCE, pszSection: Windows.Win32.Foundation.PWSTR, pstTable: POINTER(Windows.Win32.System.WindowsProgramming.STRTABLEW_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ADVPACK.dll')
def LaunchINFSectionExW(hwnd: Windows.Win32.Foundation.HWND, hInstance: Windows.Win32.Foundation.HINSTANCE, pszParms: Windows.Win32.Foundation.PWSTR, nShow: Int32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ADVPACK.dll')
def ExecuteCabA(hwnd: Windows.Win32.Foundation.HWND, pCab: POINTER(Windows.Win32.System.WindowsProgramming.CABINFOA_head), pReserved: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ADVPACK.dll')
def ExecuteCabW(hwnd: Windows.Win32.Foundation.HWND, pCab: POINTER(Windows.Win32.System.WindowsProgramming.CABINFOW_head), pReserved: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ADVPACK.dll')
def AdvInstallFileA(hwnd: Windows.Win32.Foundation.HWND, lpszSourceDir: Windows.Win32.Foundation.PSTR, lpszSourceFile: Windows.Win32.Foundation.PSTR, lpszDestDir: Windows.Win32.Foundation.PSTR, lpszDestFile: Windows.Win32.Foundation.PSTR, dwFlags: UInt32, dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ADVPACK.dll')
def AdvInstallFileW(hwnd: Windows.Win32.Foundation.HWND, lpszSourceDir: Windows.Win32.Foundation.PWSTR, lpszSourceFile: Windows.Win32.Foundation.PWSTR, lpszDestDir: Windows.Win32.Foundation.PWSTR, lpszDestFile: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ADVPACK.dll')
def RegSaveRestoreA(hWnd: Windows.Win32.Foundation.HWND, pszTitleString: Windows.Win32.Foundation.PSTR, hkBckupKey: Windows.Win32.System.Registry.HKEY, pcszRootKey: Windows.Win32.Foundation.PSTR, pcszSubKey: Windows.Win32.Foundation.PSTR, pcszValueName: Windows.Win32.Foundation.PSTR, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ADVPACK.dll')
def RegSaveRestoreW(hWnd: Windows.Win32.Foundation.HWND, pszTitleString: Windows.Win32.Foundation.PWSTR, hkBckupKey: Windows.Win32.System.Registry.HKEY, pcszRootKey: Windows.Win32.Foundation.PWSTR, pcszSubKey: Windows.Win32.Foundation.PWSTR, pcszValueName: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ADVPACK.dll')
def RegSaveRestoreOnINFA(hWnd: Windows.Win32.Foundation.HWND, pszTitle: Windows.Win32.Foundation.PSTR, pszINF: Windows.Win32.Foundation.PSTR, pszSection: Windows.Win32.Foundation.PSTR, hHKLMBackKey: Windows.Win32.System.Registry.HKEY, hHKCUBackKey: Windows.Win32.System.Registry.HKEY, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ADVPACK.dll')
def RegSaveRestoreOnINFW(hWnd: Windows.Win32.Foundation.HWND, pszTitle: Windows.Win32.Foundation.PWSTR, pszINF: Windows.Win32.Foundation.PWSTR, pszSection: Windows.Win32.Foundation.PWSTR, hHKLMBackKey: Windows.Win32.System.Registry.HKEY, hHKCUBackKey: Windows.Win32.System.Registry.HKEY, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ADVPACK.dll')
def RegRestoreAllA(hWnd: Windows.Win32.Foundation.HWND, pszTitleString: Windows.Win32.Foundation.PSTR, hkBckupKey: Windows.Win32.System.Registry.HKEY) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ADVPACK.dll')
def RegRestoreAllW(hWnd: Windows.Win32.Foundation.HWND, pszTitleString: Windows.Win32.Foundation.PWSTR, hkBckupKey: Windows.Win32.System.Registry.HKEY) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ADVPACK.dll')
def FileSaveRestoreW(hDlg: Windows.Win32.Foundation.HWND, lpFileList: Windows.Win32.Foundation.PWSTR, lpDir: Windows.Win32.Foundation.PWSTR, lpBaseName: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ADVPACK.dll')
def FileSaveRestoreOnINFA(hWnd: Windows.Win32.Foundation.HWND, pszTitle: Windows.Win32.Foundation.PSTR, pszINF: Windows.Win32.Foundation.PSTR, pszSection: Windows.Win32.Foundation.PSTR, pszBackupDir: Windows.Win32.Foundation.PSTR, pszBaseBackupFile: Windows.Win32.Foundation.PSTR, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ADVPACK.dll')
def FileSaveRestoreOnINFW(hWnd: Windows.Win32.Foundation.HWND, pszTitle: Windows.Win32.Foundation.PWSTR, pszINF: Windows.Win32.Foundation.PWSTR, pszSection: Windows.Win32.Foundation.PWSTR, pszBackupDir: Windows.Win32.Foundation.PWSTR, pszBaseBackupFile: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ADVPACK.dll')
def AddDelBackupEntryA(lpcszFileList: Windows.Win32.Foundation.PSTR, lpcszBackupDir: Windows.Win32.Foundation.PSTR, lpcszBaseName: Windows.Win32.Foundation.PSTR, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ADVPACK.dll')
def AddDelBackupEntryW(lpcszFileList: Windows.Win32.Foundation.PWSTR, lpcszBackupDir: Windows.Win32.Foundation.PWSTR, lpcszBaseName: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ADVPACK.dll')
def FileSaveMarkNotExistA(lpFileList: Windows.Win32.Foundation.PSTR, lpDir: Windows.Win32.Foundation.PSTR, lpBaseName: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ADVPACK.dll')
def FileSaveMarkNotExistW(lpFileList: Windows.Win32.Foundation.PWSTR, lpDir: Windows.Win32.Foundation.PWSTR, lpBaseName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ADVPACK.dll')
def GetVersionFromFileA(lpszFilename: Windows.Win32.Foundation.PSTR, pdwMSVer: POINTER(UInt32), pdwLSVer: POINTER(UInt32), bVersion: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ADVPACK.dll')
def GetVersionFromFileW(lpszFilename: Windows.Win32.Foundation.PWSTR, pdwMSVer: POINTER(UInt32), pdwLSVer: POINTER(UInt32), bVersion: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ADVPACK.dll')
def GetVersionFromFileExA(lpszFilename: Windows.Win32.Foundation.PSTR, pdwMSVer: POINTER(UInt32), pdwLSVer: POINTER(UInt32), bVersion: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ADVPACK.dll')
def GetVersionFromFileExW(lpszFilename: Windows.Win32.Foundation.PWSTR, pdwMSVer: POINTER(UInt32), pdwLSVer: POINTER(UInt32), bVersion: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ADVPACK.dll')
def IsNTAdmin(dwReserved: UInt32, lpdwReserved: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVPACK.dll')
def DelNodeA(pszFileOrDirName: Windows.Win32.Foundation.PSTR, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ADVPACK.dll')
def DelNodeW(pszFileOrDirName: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ADVPACK.dll')
def DelNodeRunDLL32W(hwnd: Windows.Win32.Foundation.HWND, hInstance: Windows.Win32.Foundation.HINSTANCE, pszParms: Windows.Win32.Foundation.PWSTR, nShow: Int32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ADVPACK.dll')
def OpenINFEngineA(pszInfFilename: Windows.Win32.Foundation.PSTR, pszInstallSection: Windows.Win32.Foundation.PSTR, dwFlags: UInt32, phInf: POINTER(c_void_p), pvReserved: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ADVPACK.dll')
def OpenINFEngineW(pszInfFilename: Windows.Win32.Foundation.PWSTR, pszInstallSection: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, phInf: POINTER(c_void_p), pvReserved: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ADVPACK.dll')
def TranslateInfStringExA(hInf: c_void_p, pszInfFilename: Windows.Win32.Foundation.PSTR, pszTranslateSection: Windows.Win32.Foundation.PSTR, pszTranslateKey: Windows.Win32.Foundation.PSTR, pszBuffer: Windows.Win32.Foundation.PSTR, dwBufferSize: UInt32, pdwRequiredSize: POINTER(UInt32), pvReserved: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ADVPACK.dll')
def TranslateInfStringExW(hInf: c_void_p, pszInfFilename: Windows.Win32.Foundation.PWSTR, pszTranslateSection: Windows.Win32.Foundation.PWSTR, pszTranslateKey: Windows.Win32.Foundation.PWSTR, pszBuffer: Windows.Win32.Foundation.PWSTR, dwBufferSize: UInt32, pdwRequiredSize: POINTER(UInt32), pvReserved: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ADVPACK.dll')
def CloseINFEngine(hInf: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ADVPACK.dll')
def ExtractFilesA(pszCabName: Windows.Win32.Foundation.PSTR, pszExpandDir: Windows.Win32.Foundation.PSTR, dwFlags: UInt32, pszFileList: Windows.Win32.Foundation.PSTR, lpReserved: c_void_p, dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ADVPACK.dll')
def ExtractFilesW(pszCabName: Windows.Win32.Foundation.PWSTR, pszExpandDir: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, pszFileList: Windows.Win32.Foundation.PWSTR, lpReserved: c_void_p, dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ADVPACK.dll')
def LaunchINFSectionW(hwndOwner: Windows.Win32.Foundation.HWND, hInstance: Windows.Win32.Foundation.HINSTANCE, pszParams: Windows.Win32.Foundation.PWSTR, nShow: Int32) -> Int32: ...
@winfunctype('ADVPACK.dll')
def UserInstStubWrapperA(hwnd: Windows.Win32.Foundation.HWND, hInstance: Windows.Win32.Foundation.HINSTANCE, pszParms: Windows.Win32.Foundation.PSTR, nShow: Int32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ADVPACK.dll')
def UserInstStubWrapperW(hwnd: Windows.Win32.Foundation.HWND, hInstance: Windows.Win32.Foundation.HINSTANCE, pszParms: Windows.Win32.Foundation.PWSTR, nShow: Int32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ADVPACK.dll')
def UserUnInstStubWrapperA(hwnd: Windows.Win32.Foundation.HWND, hInstance: Windows.Win32.Foundation.HINSTANCE, pszParms: Windows.Win32.Foundation.PSTR, nShow: Int32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ADVPACK.dll')
def UserUnInstStubWrapperW(hwnd: Windows.Win32.Foundation.HWND, hInstance: Windows.Win32.Foundation.HINSTANCE, pszParms: Windows.Win32.Foundation.PWSTR, nShow: Int32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ADVPACK.dll')
def SetPerUserSecValuesA(pPerUser: POINTER(Windows.Win32.System.WindowsProgramming.PERUSERSECTIONA_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ADVPACK.dll')
def SetPerUserSecValuesW(pPerUser: POINTER(Windows.Win32.System.WindowsProgramming.PERUSERSECTIONW_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('USER32.dll')
def SendIMEMessageExA(param0: Windows.Win32.Foundation.HWND, param1: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.LRESULT: ...
@winfunctype('USER32.dll')
def SendIMEMessageExW(param0: Windows.Win32.Foundation.HWND, param1: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.LRESULT: ...
@winfunctype('USER32.dll')
def IMPGetIMEA(param0: Windows.Win32.Foundation.HWND, param1: POINTER(Windows.Win32.System.WindowsProgramming.IMEPROA_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def IMPGetIMEW(param0: Windows.Win32.Foundation.HWND, param1: POINTER(Windows.Win32.System.WindowsProgramming.IMEPROW_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def IMPQueryIMEA(param0: POINTER(Windows.Win32.System.WindowsProgramming.IMEPROA_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def IMPQueryIMEW(param0: POINTER(Windows.Win32.System.WindowsProgramming.IMEPROW_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def IMPSetIMEA(param0: Windows.Win32.Foundation.HWND, param1: POINTER(Windows.Win32.System.WindowsProgramming.IMEPROA_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def IMPSetIMEW(param0: Windows.Win32.Foundation.HWND, param1: POINTER(Windows.Win32.System.WindowsProgramming.IMEPROW_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def WINNLSGetIMEHotkey(param0: Windows.Win32.Foundation.HWND) -> UInt32: ...
@winfunctype('USER32.dll')
def WINNLSEnableIME(param0: Windows.Win32.Foundation.HWND, param1: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def WINNLSGetEnableStatus(param0: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('APPHELP.dll')
def ApphelpCheckShellObject(ObjectCLSID: POINTER(Guid), bShimIfNecessary: Windows.Win32.Foundation.BOOL, pullFlags: POINTER(UInt64)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('Wldp.dll')
def WldpGetLockdownPolicy(hostInformation: POINTER(Windows.Win32.System.WindowsProgramming.WLDP_HOST_INFORMATION_head), lockdownState: POINTER(UInt32), lockdownFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Wldp.dll')
def WldpIsClassInApprovedList(classID: POINTER(Guid), hostInformation: POINTER(Windows.Win32.System.WindowsProgramming.WLDP_HOST_INFORMATION_head), isApproved: POINTER(Windows.Win32.Foundation.BOOL), optionalFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Wldp.dll')
def WldpSetDynamicCodeTrust(fileHandle: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Wldp.dll')
def WldpIsDynamicCodePolicyEnabled(isEnabled: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Wldp.dll')
def WldpQueryDynamicCodeTrust(fileHandle: Windows.Win32.Foundation.HANDLE, baseImage: c_void_p, imageSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Wldp.dll')
def WldpQueryDeviceSecurityInformation(information: POINTER(Windows.Win32.System.WindowsProgramming.WLDP_DEVICE_SECURITY_INFORMATION_head), informationLength: UInt32, returnLength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class CABINFOA(Structure):
    pszCab: Windows.Win32.Foundation.PSTR
    pszInf: Windows.Win32.Foundation.PSTR
    pszSection: Windows.Win32.Foundation.PSTR
    szSrcPath: Windows.Win32.Foundation.CHAR * 260
    dwFlags: UInt32
class CABINFOW(Structure):
    pszCab: Windows.Win32.Foundation.PWSTR
    pszInf: Windows.Win32.Foundation.PWSTR
    pszSection: Windows.Win32.Foundation.PWSTR
    szSrcPath: Char * 260
    dwFlags: UInt32
class CLIENT_ID(Structure):
    UniqueProcess: Windows.Win32.Foundation.HANDLE
    UniqueThread: Windows.Win32.Foundation.HANDLE
class CUSTOM_SYSTEM_EVENT_TRIGGER_CONFIG(Structure):
    Size: UInt32
    TriggerId: Windows.Win32.Foundation.PWSTR
CameraUIControl = Guid('16d5a2be-b1c5-47b3-8e-ae-cc-bc-f4-52-c7-e8')
CameraUIControlCaptureMode = Int32
CameraUIControlCaptureMode_PhotoOrVideo: CameraUIControlCaptureMode = 0
CameraUIControlCaptureMode_Photo: CameraUIControlCaptureMode = 1
CameraUIControlCaptureMode_Video: CameraUIControlCaptureMode = 2
CameraUIControlLinearSelectionMode = Int32
CameraUIControlLinearSelectionMode_Single: CameraUIControlLinearSelectionMode = 0
CameraUIControlLinearSelectionMode_Multiple: CameraUIControlLinearSelectionMode = 1
CameraUIControlMode = Int32
CameraUIControlMode_Browse: CameraUIControlMode = 0
CameraUIControlMode_Linear: CameraUIControlMode = 1
CameraUIControlPhotoFormat = Int32
CameraUIControlPhotoFormat_Jpeg: CameraUIControlPhotoFormat = 0
CameraUIControlPhotoFormat_Png: CameraUIControlPhotoFormat = 1
CameraUIControlPhotoFormat_JpegXR: CameraUIControlPhotoFormat = 2
CameraUIControlVideoFormat = Int32
CameraUIControlVideoFormat_Mp4: CameraUIControlVideoFormat = 0
CameraUIControlVideoFormat_Wmv: CameraUIControlVideoFormat = 1
CameraUIControlViewType = Int32
CameraUIControlViewType_SingleItem: CameraUIControlViewType = 0
CameraUIControlViewType_ItemList: CameraUIControlViewType = 1
class DATETIME(Structure):
    year: UInt16
    month: UInt16
    day: UInt16
    hour: UInt16
    min: UInt16
    sec: UInt16
class DCICMD(Structure):
    dwCommand: UInt32
    dwParam1: UInt32
    dwParam2: UInt32
    dwVersion: UInt32
    dwReserved: UInt32
class DCICREATEINPUT(Structure):
    cmd: Windows.Win32.System.WindowsProgramming.DCICMD
    dwCompression: UInt32
    dwMask: UInt32 * 3
    dwWidth: UInt32
    dwHeight: UInt32
    dwDCICaps: UInt32
    dwBitCount: UInt32
    lpSurface: c_void_p
class DCIENUMINPUT(Structure):
    cmd: Windows.Win32.System.WindowsProgramming.DCICMD
    rSrc: Windows.Win32.Foundation.RECT
    rDst: Windows.Win32.Foundation.RECT
    EnumCallback: IntPtr
    lpContext: c_void_p
class DCIOFFSCREEN(Structure):
    dciInfo: Windows.Win32.System.WindowsProgramming.DCISURFACEINFO
    Draw: IntPtr
    SetClipList: IntPtr
    SetDestination: IntPtr
class DCIOVERLAY(Structure):
    dciInfo: Windows.Win32.System.WindowsProgramming.DCISURFACEINFO
    dwChromakeyValue: UInt32
    dwChromakeyMask: UInt32
class DCISURFACEINFO(Structure):
    dwSize: UInt32
    dwDCICaps: UInt32
    dwCompression: UInt32
    dwMask: UInt32 * 3
    dwWidth: UInt32
    dwHeight: UInt32
    lStride: Int32
    dwBitCount: UInt32
    dwOffSurface: UIntPtr
    wSelSurface: UInt16
    wReserved: UInt16
    dwReserved1: UInt32
    dwReserved2: UInt32
    dwReserved3: UInt32
    BeginAccess: IntPtr
    EndAccess: IntPtr
    DestroySurface: IntPtr
DECISION_LOCATION = Int32
DECISION_LOCATION_REFRESH_GLOBAL_DATA: DECISION_LOCATION = 0
DECISION_LOCATION_PARAMETER_VALIDATION: DECISION_LOCATION = 1
DECISION_LOCATION_AUDIT: DECISION_LOCATION = 2
DECISION_LOCATION_FAILED_CONVERT_GUID: DECISION_LOCATION = 3
DECISION_LOCATION_ENTERPRISE_DEFINED_CLASS_ID: DECISION_LOCATION = 4
DECISION_LOCATION_GLOBAL_BUILT_IN_LIST: DECISION_LOCATION = 5
DECISION_LOCATION_PROVIDER_BUILT_IN_LIST: DECISION_LOCATION = 6
DECISION_LOCATION_ENFORCE_STATE_LIST: DECISION_LOCATION = 7
DECISION_LOCATION_NOT_FOUND: DECISION_LOCATION = 8
DECISION_LOCATION_UNKNOWN: DECISION_LOCATION = 9
if ARCH in 'X64,ARM64':
    class DELAYLOAD_INFO(Structure):
        Size: UInt32
        DelayloadDescriptor: POINTER(Windows.Win32.System.WindowsProgramming.IMAGE_DELAYLOAD_DESCRIPTOR_head)
        ThunkAddress: POINTER(Windows.Win32.System.WindowsProgramming.IMAGE_THUNK_DATA64_head)
        TargetDllName: Windows.Win32.Foundation.PSTR
        TargetApiDescriptor: Windows.Win32.System.WindowsProgramming.DELAYLOAD_PROC_DESCRIPTOR
        TargetModuleBase: c_void_p
        Unused: c_void_p
        LastError: UInt32
if ARCH in 'X86':
    class DELAYLOAD_INFO(Structure):
        Size: UInt32
        DelayloadDescriptor: POINTER(Windows.Win32.System.WindowsProgramming.IMAGE_DELAYLOAD_DESCRIPTOR_head)
        ThunkAddress: POINTER(Windows.Win32.System.WindowsProgramming.IMAGE_THUNK_DATA32_head)
        TargetDllName: Windows.Win32.Foundation.PSTR
        TargetApiDescriptor: Windows.Win32.System.WindowsProgramming.DELAYLOAD_PROC_DESCRIPTOR
        TargetModuleBase: c_void_p
        Unused: c_void_p
        LastError: UInt32
class DELAYLOAD_PROC_DESCRIPTOR(Structure):
    ImportDescribedByName: UInt32
    Description: _Description_e__Union
    class _Description_e__Union(Union):
        Name: Windows.Win32.Foundation.PSTR
        Ordinal: UInt32
DefaultBrowserSyncSettings = Guid('3ac83423-3112-4aa6-9b-5b-1f-eb-23-d0-c5-f9')
@winfunctype_pointer
def ENUM_CALLBACK(lpSurfaceInfo: POINTER(Windows.Win32.System.WindowsProgramming.DCISURFACEINFO_head), lpContext: c_void_p) -> Void: ...
EditionUpgradeBroker = Guid('c4270827-4f39-45df-92-88-12-ff-6b-85-a9-21')
EditionUpgradeHelper = Guid('01776df3-b9af-4e50-9b-1c-56-e9-31-16-d7-04')
FEATURE_CHANGE_TIME = Int32
FEATURE_CHANGE_TIME_READ: FEATURE_CHANGE_TIME = 0
FEATURE_CHANGE_TIME_MODULE_RELOAD: FEATURE_CHANGE_TIME = 1
FEATURE_CHANGE_TIME_SESSION: FEATURE_CHANGE_TIME = 2
FEATURE_CHANGE_TIME_REBOOT: FEATURE_CHANGE_TIME = 3
FEATURE_ENABLED_STATE = Int32
FEATURE_ENABLED_STATE_DEFAULT: FEATURE_ENABLED_STATE = 0
FEATURE_ENABLED_STATE_DISABLED: FEATURE_ENABLED_STATE = 1
FEATURE_ENABLED_STATE_ENABLED: FEATURE_ENABLED_STATE = 2
class FEATURE_ERROR(Structure):
    hr: Windows.Win32.Foundation.HRESULT
    lineNumber: UInt16
    file: Windows.Win32.Foundation.PSTR
    process: Windows.Win32.Foundation.PSTR
    module: Windows.Win32.Foundation.PSTR
    callerReturnAddressOffset: UInt32
    callerModule: Windows.Win32.Foundation.PSTR
    message: Windows.Win32.Foundation.PSTR
    originLineNumber: UInt16
    originFile: Windows.Win32.Foundation.PSTR
    originModule: Windows.Win32.Foundation.PSTR
    originCallerReturnAddressOffset: UInt32
    originCallerModule: Windows.Win32.Foundation.PSTR
    originName: Windows.Win32.Foundation.PSTR
FEATURE_STATE_CHANGE_SUBSCRIPTION = IntPtr
FH_SERVICE_PIPE_HANDLE = IntPtr
class FILE_CASE_SENSITIVE_INFO(Structure):
    Flags: UInt32
class FILE_DISPOSITION_INFO_EX(Structure):
    Flags: UInt32
FILE_INFORMATION_CLASS = Int32
FILE_INFORMATION_CLASS_FileDirectoryInformation: FILE_INFORMATION_CLASS = 1
HWINWATCH = IntPtr
class HW_PROFILE_INFOA(Structure):
    dwDockInfo: UInt32
    szHwProfileGuid: Windows.Win32.Foundation.CHAR * 39
    szHwProfileName: Windows.Win32.Foundation.CHAR * 80
class HW_PROFILE_INFOW(Structure):
    dwDockInfo: UInt32
    szHwProfileGuid: Char * 39
    szHwProfileName: Char * 80
class ICameraUIControl(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b8733adf-3d68-4b8f-bb-08-e2-8a-0b-ed-03-76')
    @commethod(3)
    def Show(pWindow: Windows.Win32.System.Com.IUnknown_head, mode: Windows.Win32.System.WindowsProgramming.CameraUIControlMode, selectionMode: Windows.Win32.System.WindowsProgramming.CameraUIControlLinearSelectionMode, captureMode: Windows.Win32.System.WindowsProgramming.CameraUIControlCaptureMode, photoFormat: Windows.Win32.System.WindowsProgramming.CameraUIControlPhotoFormat, videoFormat: Windows.Win32.System.WindowsProgramming.CameraUIControlVideoFormat, bHasCloseButton: Windows.Win32.Foundation.BOOL, pEventCallback: Windows.Win32.System.WindowsProgramming.ICameraUIControlEventCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Close() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Suspend(pbDeferralRequired: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Resume() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCurrentViewType(pViewType: POINTER(Windows.Win32.System.WindowsProgramming.CameraUIControlViewType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetActiveItem(pbstrActiveItemPath: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetSelectedItems(ppSelectedItemPaths: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def RemoveCapturedItem(pszPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class ICameraUIControlEventCallback(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1bfa0c2c-fbcd-4776-bd-a4-88-bf-97-4e-74-f4')
    @commethod(3)
    def OnStartupComplete() -> Void: ...
    @commethod(4)
    def OnSuspendComplete() -> Void: ...
    @commethod(5)
    def OnItemCaptured(pszPath: Windows.Win32.Foundation.PWSTR) -> Void: ...
    @commethod(6)
    def OnItemDeleted(pszPath: Windows.Win32.Foundation.PWSTR) -> Void: ...
    @commethod(7)
    def OnClosed() -> Void: ...
class IClipServiceNotificationHelper(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c39948f0-6142-44fd-98-ca-e1-68-1a-8d-68-b5')
    @commethod(3)
    def ShowToast(titleText: Windows.Win32.Foundation.BSTR, bodyText: Windows.Win32.Foundation.BSTR, packageName: Windows.Win32.Foundation.BSTR, appId: Windows.Win32.Foundation.BSTR, launchCommand: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IContainerActivationHelper(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b524f93f-80d5-4ec7-ae-9e-d6-6e-93-ad-e1-fa')
    @commethod(3)
    def CanActivateClientVM(isAllowed: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IDefaultBrowserSyncSettings(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('7a27faad-5ae6-4255-90-30-c5-30-93-62-92-e3')
    @commethod(3)
    def IsEnabled() -> Windows.Win32.Foundation.BOOL: ...
class IDeleteBrowsingHistory(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('cf38ed4b-2be7-4461-8b-5e-9a-46-6d-c8-2a-e3')
    @commethod(3)
    def DeleteBrowsingHistory(dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IEditionUpgradeBroker(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('ff19cbcf-9455-4937-b8-72-6b-79-29-a4-60-af')
    @commethod(3)
    def InitializeParentWindow(parentHandle: Windows.Win32.System.Ole.OLE_HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UpdateOperatingSystem(parameter: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ShowProductKeyUI() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CanUpgrade() -> Windows.Win32.Foundation.HRESULT: ...
class IEditionUpgradeHelper(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d3e9e342-5deb-43b6-84-9e-69-13-b8-5d-50-3a')
    @commethod(3)
    def CanUpgrade(isAllowed: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UpdateOperatingSystem(contentId: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ShowProductKeyUI() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetOsProductContentId(contentId: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetGenuineLocalStatus(isGenuine: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IMAGE_DELAYLOAD_DESCRIPTOR(Structure):
    Attributes: _Attributes_e__Union
    DllNameRVA: UInt32
    ModuleHandleRVA: UInt32
    ImportAddressTableRVA: UInt32
    ImportNameTableRVA: UInt32
    BoundImportAddressTableRVA: UInt32
    UnloadInformationTableRVA: UInt32
    TimeDateStamp: UInt32
    class _Attributes_e__Union(Union):
        AllAttributes: UInt32
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            _bitfield: UInt32
class IMAGE_THUNK_DATA32(Structure):
    u1: _u1_e__Union
    class _u1_e__Union(Union):
        ForwarderString: UInt32
        Function: UInt32
        Ordinal: UInt32
        AddressOfData: UInt32
class IMAGE_THUNK_DATA64(Structure):
    u1: _u1_e__Union
    class _u1_e__Union(Union):
        ForwarderString: UInt64
        Function: UInt64
        Ordinal: UInt64
        AddressOfData: UInt64
class IMEPROA(Structure):
    hWnd: Windows.Win32.Foundation.HWND
    InstDate: Windows.Win32.System.WindowsProgramming.DATETIME
    wVersion: UInt32
    szDescription: Byte * 50
    szName: Byte * 80
    szOptions: Byte * 30
class IMEPROW(Structure):
    hWnd: Windows.Win32.Foundation.HWND
    InstDate: Windows.Win32.System.WindowsProgramming.DATETIME
    wVersion: UInt32
    szDescription: Char * 50
    szName: Char * 80
    szOptions: Char * 30
class IMESTRUCT(Structure):
    fnc: UInt32
    wParam: Windows.Win32.Foundation.WPARAM
    wCount: UInt32
    dchSource: UInt32
    dchDest: UInt32
    lParam1: Windows.Win32.Foundation.LPARAM
    lParam2: Windows.Win32.Foundation.LPARAM
    lParam3: Windows.Win32.Foundation.LPARAM
class IO_STATUS_BLOCK(Structure):
    Anonymous: _Anonymous_e__Union
    Information: UIntPtr
    class _Anonymous_e__Union(Union):
        Status: Windows.Win32.Foundation.NTSTATUS
        Pointer: c_void_p
class IWindowsLockModeHelper(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f342d19e-cc22-4648-bb-5d-03-cc-f7-5b-47-c5')
    @commethod(3)
    def GetSMode(isSmode: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class JAVA_TRUST(Structure):
    cbSize: UInt32
    flag: UInt32
    fAllActiveXPermissions: Windows.Win32.Foundation.BOOL
    fAllPermissions: Windows.Win32.Foundation.BOOL
    dwEncodingType: UInt32
    pbJavaPermissions: c_char_p_no
    cbJavaPermissions: UInt32
    pbSigner: c_char_p_no
    cbSigner: UInt32
    pwszZone: Windows.Win32.Foundation.PWSTR
    guidZone: Guid
    hVerify: Windows.Win32.Foundation.HRESULT
class JIT_DEBUG_INFO(Structure):
    dwSize: UInt32
    dwProcessorArchitecture: UInt32
    dwThreadID: UInt32
    dwReserved0: UInt32
    lpExceptionAddress: UInt64
    lpExceptionRecord: UInt64
    lpContextRecord: UInt64
KEY_SET_INFORMATION_CLASS = Int32
KEY_SET_INFORMATION_CLASS_KeyWriteTimeInformation: KEY_SET_INFORMATION_CLASS = 0
KEY_SET_INFORMATION_CLASS_KeyWow64FlagsInformation: KEY_SET_INFORMATION_CLASS = 1
KEY_SET_INFORMATION_CLASS_KeyControlFlagsInformation: KEY_SET_INFORMATION_CLASS = 2
KEY_SET_INFORMATION_CLASS_KeySetVirtualizationInformation: KEY_SET_INFORMATION_CLASS = 3
KEY_SET_INFORMATION_CLASS_KeySetDebugInformation: KEY_SET_INFORMATION_CLASS = 4
KEY_SET_INFORMATION_CLASS_KeySetHandleTagsInformation: KEY_SET_INFORMATION_CLASS = 5
KEY_SET_INFORMATION_CLASS_MaxKeySetInfoClass: KEY_SET_INFORMATION_CLASS = 6
class KEY_VALUE_ENTRY(Structure):
    ValueName: POINTER(Windows.Win32.Foundation.UNICODE_STRING_head)
    DataLength: UInt32
    DataOffset: UInt32
    Type: UInt32
class LDR_DATA_TABLE_ENTRY(Structure):
    Reserved1: c_void_p * 2
    InMemoryOrderLinks: Windows.Win32.System.Kernel.LIST_ENTRY
    Reserved2: c_void_p * 2
    DllBase: c_void_p
    Reserved3: c_void_p * 2
    FullDllName: Windows.Win32.Foundation.UNICODE_STRING
    Reserved4: Byte * 8
    Reserved5: c_void_p * 3
    Anonymous: _Anonymous_e__Union
    TimeDateStamp: UInt32
    class _Anonymous_e__Union(Union):
        CheckSum: UInt32
        Reserved6: c_void_p
class OBJECT_ATTRIBUTES(Structure):
    Length: UInt32
    RootDirectory: Windows.Win32.Foundation.HANDLE
    ObjectName: POINTER(Windows.Win32.Foundation.UNICODE_STRING_head)
    Attributes: UInt32
    SecurityDescriptor: c_void_p
    SecurityQualityOfService: c_void_p
OBJECT_INFORMATION_CLASS = Int32
OBJECT_INFORMATION_CLASS_ObjectBasicInformation: OBJECT_INFORMATION_CLASS = 0
OBJECT_INFORMATION_CLASS_ObjectTypeInformation: OBJECT_INFORMATION_CLASS = 2
@winfunctype_pointer
def PDELAYLOAD_FAILURE_DLL_CALLBACK(NotificationReason: UInt32, DelayloadInfo: POINTER(Windows.Win32.System.WindowsProgramming.DELAYLOAD_INFO_head)) -> c_void_p: ...
class PERUSERSECTIONA(Structure):
    szGUID: Windows.Win32.Foundation.CHAR * 59
    szDispName: Windows.Win32.Foundation.CHAR * 128
    szLocale: Windows.Win32.Foundation.CHAR * 10
    szStub: Windows.Win32.Foundation.CHAR * 1040
    szVersion: Windows.Win32.Foundation.CHAR * 32
    szCompID: Windows.Win32.Foundation.CHAR * 128
    dwIsInstalled: UInt32
    bRollback: Windows.Win32.Foundation.BOOL
class PERUSERSECTIONW(Structure):
    szGUID: Char * 59
    szDispName: Char * 128
    szLocale: Char * 10
    szStub: Char * 1040
    szVersion: Char * 32
    szCompID: Char * 128
    dwIsInstalled: UInt32
    bRollback: Windows.Win32.Foundation.BOOL
@winfunctype_pointer
def PFEATURE_STATE_CHANGE_CALLBACK(context: c_void_p) -> Void: ...
@winfunctype_pointer
def PFIBER_CALLOUT_ROUTINE(lpParameter: c_void_p) -> c_void_p: ...
@winfunctype_pointer
def PIO_APC_ROUTINE(ApcContext: c_void_p, IoStatusBlock: POINTER(Windows.Win32.System.WindowsProgramming.IO_STATUS_BLOCK_head), Reserved: UInt32) -> Void: ...
@winfunctype_pointer
def PQUERYACTCTXW_FUNC(dwFlags: UInt32, hActCtx: Windows.Win32.Foundation.HANDLE, pvSubInstance: c_void_p, ulInfoClass: UInt32, pvBuffer: c_void_p, cbBuffer: UIntPtr, pcbWrittenOrRequired: POINTER(UIntPtr)) -> Windows.Win32.Foundation.BOOL: ...
class PUBLIC_OBJECT_BASIC_INFORMATION(Structure):
    Attributes: UInt32
    GrantedAccess: UInt32
    HandleCount: UInt32
    PointerCount: UInt32
    Reserved: UInt32 * 10
class PUBLIC_OBJECT_TYPE_INFORMATION(Structure):
    TypeName: Windows.Win32.Foundation.UNICODE_STRING
    Reserved: UInt32 * 22
@winfunctype_pointer
def PWINSTATIONQUERYINFORMATIONW(param0: Windows.Win32.Foundation.HANDLE, param1: UInt32, param2: Windows.Win32.System.WindowsProgramming.WINSTATIONINFOCLASS, param3: c_void_p, param4: UInt32, param5: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype_pointer
def PWLDP_ISAPPAPPROVEDBYPOLICY_API(PackageFamilyName: Windows.Win32.Foundation.PWSTR, PackageVersion: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PWLDP_ISDYNAMICCODEPOLICYENABLED_API(pbEnabled: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PWLDP_ISPRODUCTIONCONFIGURATION_API(IsProductionConfiguration: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PWLDP_ISWCOSPRODUCTIONCONFIGURATION_API(IsProductionConfiguration: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PWLDP_QUERYDEVICESECURITYINFORMATION_API(information: POINTER(Windows.Win32.System.WindowsProgramming.WLDP_DEVICE_SECURITY_INFORMATION_head), informationLength: UInt32, returnLength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PWLDP_QUERYDYNAMICODETRUST_API(fileHandle: Windows.Win32.Foundation.HANDLE, baseImage: c_void_p, imageSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PWLDP_QUERYPOLICYSETTINGENABLED2_API(Setting: Windows.Win32.Foundation.PWSTR, Enabled: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PWLDP_QUERYPOLICYSETTINGENABLED_API(Setting: Windows.Win32.System.WindowsProgramming.WLDP_POLICY_SETTING, Enabled: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PWLDP_QUERYWINDOWSLOCKDOWNMODE_API(lockdownMode: POINTER(Windows.Win32.System.WindowsProgramming.WLDP_WINDOWS_LOCKDOWN_MODE)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PWLDP_QUERYWINDOWSLOCKDOWNRESTRICTION_API(LockdownRestriction: POINTER(Windows.Win32.System.WindowsProgramming.WLDP_WINDOWS_LOCKDOWN_RESTRICTION)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PWLDP_RESETPRODUCTIONCONFIGURATION_API() -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PWLDP_RESETWCOSPRODUCTIONCONFIGURATION_API() -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PWLDP_SETDYNAMICCODETRUST_API(hFileHandle: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PWLDP_SETWINDOWSLOCKDOWNRESTRICTION_API(LockdownRestriction: Windows.Win32.System.WindowsProgramming.WLDP_WINDOWS_LOCKDOWN_RESTRICTION) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def REGINSTALLA(hm: Windows.Win32.Foundation.HINSTANCE, pszSection: Windows.Win32.Foundation.PSTR, pstTable: POINTER(Windows.Win32.System.WindowsProgramming.STRTABLEA_head)) -> Windows.Win32.Foundation.HRESULT: ...
class STRENTRYA(Structure):
    pszName: Windows.Win32.Foundation.PSTR
    pszValue: Windows.Win32.Foundation.PSTR
class STRENTRYW(Structure):
    pszName: Windows.Win32.Foundation.PWSTR
    pszValue: Windows.Win32.Foundation.PWSTR
class STRINGEXSTRUCT(Structure):
    dwSize: UInt32
    uDeterminePos: UInt32
    uDetermineDelimPos: UInt32
    uYomiPos: UInt32
    uYomiDelimPos: UInt32
class STRTABLEA(Structure):
    cEntries: UInt32
    pse: POINTER(Windows.Win32.System.WindowsProgramming.STRENTRYA_head)
class STRTABLEW(Structure):
    cEntries: UInt32
    pse: POINTER(Windows.Win32.System.WindowsProgramming.STRENTRYW_head)
class SYSTEM_BASIC_INFORMATION(Structure):
    Reserved1: Byte * 24
    Reserved2: c_void_p * 4
    NumberOfProcessors: SByte
class SYSTEM_CODEINTEGRITY_INFORMATION(Structure):
    Length: UInt32
    CodeIntegrityOptions: UInt32
class SYSTEM_EXCEPTION_INFORMATION(Structure):
    Reserved1: Byte * 16
SYSTEM_INFORMATION_CLASS = Int32
SYSTEM_INFORMATION_CLASS_SystemBasicInformation: SYSTEM_INFORMATION_CLASS = 0
SYSTEM_INFORMATION_CLASS_SystemPerformanceInformation: SYSTEM_INFORMATION_CLASS = 2
SYSTEM_INFORMATION_CLASS_SystemTimeOfDayInformation: SYSTEM_INFORMATION_CLASS = 3
SYSTEM_INFORMATION_CLASS_SystemProcessInformation: SYSTEM_INFORMATION_CLASS = 5
SYSTEM_INFORMATION_CLASS_SystemProcessorPerformanceInformation: SYSTEM_INFORMATION_CLASS = 8
SYSTEM_INFORMATION_CLASS_SystemInterruptInformation: SYSTEM_INFORMATION_CLASS = 23
SYSTEM_INFORMATION_CLASS_SystemExceptionInformation: SYSTEM_INFORMATION_CLASS = 33
SYSTEM_INFORMATION_CLASS_SystemRegistryQuotaInformation: SYSTEM_INFORMATION_CLASS = 37
SYSTEM_INFORMATION_CLASS_SystemLookasideInformation: SYSTEM_INFORMATION_CLASS = 45
SYSTEM_INFORMATION_CLASS_SystemCodeIntegrityInformation: SYSTEM_INFORMATION_CLASS = 103
SYSTEM_INFORMATION_CLASS_SystemPolicyInformation: SYSTEM_INFORMATION_CLASS = 134
class SYSTEM_INTERRUPT_INFORMATION(Structure):
    Reserved1: Byte * 24
class SYSTEM_LOOKASIDE_INFORMATION(Structure):
    Reserved1: Byte * 32
class SYSTEM_PERFORMANCE_INFORMATION(Structure):
    Reserved1: Byte * 312
class SYSTEM_POLICY_INFORMATION(Structure):
    Reserved1: c_void_p * 2
    Reserved2: UInt32 * 3
class SYSTEM_PROCESSOR_PERFORMANCE_INFORMATION(Structure):
    IdleTime: Windows.Win32.Foundation.LARGE_INTEGER
    KernelTime: Windows.Win32.Foundation.LARGE_INTEGER
    UserTime: Windows.Win32.Foundation.LARGE_INTEGER
    Reserved1: Windows.Win32.Foundation.LARGE_INTEGER * 2
    Reserved2: UInt32
class SYSTEM_PROCESS_INFORMATION(Structure):
    NextEntryOffset: UInt32
    NumberOfThreads: UInt32
    Reserved1: Byte * 48
    ImageName: Windows.Win32.Foundation.UNICODE_STRING
    BasePriority: Int32
    UniqueProcessId: Windows.Win32.Foundation.HANDLE
    Reserved2: c_void_p
    HandleCount: UInt32
    SessionId: UInt32
    Reserved3: c_void_p
    PeakVirtualSize: UIntPtr
    VirtualSize: UIntPtr
    Reserved4: UInt32
    PeakWorkingSetSize: UIntPtr
    WorkingSetSize: UIntPtr
    Reserved5: c_void_p
    QuotaPagedPoolUsage: UIntPtr
    Reserved6: c_void_p
    QuotaNonPagedPoolUsage: UIntPtr
    PagefileUsage: UIntPtr
    PeakPagefileUsage: UIntPtr
    PrivatePageCount: UIntPtr
    Reserved7: Windows.Win32.Foundation.LARGE_INTEGER * 6
class SYSTEM_REGISTRY_QUOTA_INFORMATION(Structure):
    RegistryQuotaAllowed: UInt32
    RegistryQuotaUsed: UInt32
    Reserved1: c_void_p
class SYSTEM_THREAD_INFORMATION(Structure):
    Reserved1: Windows.Win32.Foundation.LARGE_INTEGER * 3
    Reserved2: UInt32
    StartAddress: c_void_p
    ClientId: Windows.Win32.System.WindowsProgramming.CLIENT_ID
    Priority: Int32
    BasePriority: Int32
    Reserved3: UInt32
    ThreadState: UInt32
    WaitReason: UInt32
class SYSTEM_TIMEOFDAY_INFORMATION(Structure):
    Reserved1: Byte * 48
if ARCH in 'X64,ARM64':
    class TCP_REQUEST_QUERY_INFORMATION_EX32_XP(Structure):
        ID: Windows.Win32.System.WindowsProgramming.TDIObjectID
        Context: UInt32 * 4
class TCP_REQUEST_QUERY_INFORMATION_EX_W2K(Structure):
    ID: Windows.Win32.System.WindowsProgramming.TDIObjectID
    Context: Byte * 16
class TCP_REQUEST_QUERY_INFORMATION_EX_XP(Structure):
    ID: Windows.Win32.System.WindowsProgramming.TDIObjectID
    Context: UIntPtr * 4
class TCP_REQUEST_SET_INFORMATION_EX(Structure):
    ID: Windows.Win32.System.WindowsProgramming.TDIObjectID
    BufferSize: UInt32
    Buffer: Byte * 1
TDIENTITY_ENTITY_TYPE = UInt32
GENERIC_ENTITY: TDIENTITY_ENTITY_TYPE = 0
AT_ENTITY: TDIENTITY_ENTITY_TYPE = 640
CL_NL_ENTITY: TDIENTITY_ENTITY_TYPE = 769
CO_NL_ENTITY: TDIENTITY_ENTITY_TYPE = 768
CL_TL_ENTITY: TDIENTITY_ENTITY_TYPE = 1025
CO_TL_ENTITY: TDIENTITY_ENTITY_TYPE = 1024
ER_ENTITY: TDIENTITY_ENTITY_TYPE = 896
IF_ENTITY: TDIENTITY_ENTITY_TYPE = 512
class TDIEntityID(Structure):
    tei_entity: Windows.Win32.System.WindowsProgramming.TDIENTITY_ENTITY_TYPE
    tei_instance: UInt32
class TDIObjectID(Structure):
    toi_entity: Windows.Win32.System.WindowsProgramming.TDIEntityID
    toi_class: UInt32
    toi_type: UInt32
    toi_id: UInt32
class TDI_TL_IO_CONTROL_ENDPOINT(Structure):
    Type: Windows.Win32.System.WindowsProgramming.TDI_TL_IO_CONTROL_TYPE
    Level: UInt32
    Anonymous: _Anonymous_e__Union
    InputBuffer: c_void_p
    InputBufferLength: UInt32
    OutputBuffer: c_void_p
    OutputBufferLength: UInt32
    class _Anonymous_e__Union(Union):
        IoControlCode: UInt32
        OptionName: UInt32
TDI_TL_IO_CONTROL_TYPE = Int32
TDI_TL_IO_CONTROL_TYPE_EndpointIoControlType: TDI_TL_IO_CONTROL_TYPE = 0
TDI_TL_IO_CONTROL_TYPE_SetSockOptIoControlType: TDI_TL_IO_CONTROL_TYPE = 1
TDI_TL_IO_CONTROL_TYPE_GetSockOptIoControlType: TDI_TL_IO_CONTROL_TYPE = 2
TDI_TL_IO_CONTROL_TYPE_SocketIoControlType: TDI_TL_IO_CONTROL_TYPE = 3
class THREAD_NAME_INFORMATION(Structure):
    ThreadName: Windows.Win32.Foundation.UNICODE_STRING
class UNDETERMINESTRUCT(Structure):
    dwSize: UInt32
    uDefIMESize: UInt32
    uDefIMEPos: UInt32
    uUndetTextLen: UInt32
    uUndetTextPos: UInt32
    uUndetAttrPos: UInt32
    uCursorPos: UInt32
    uDeltaStart: UInt32
    uDetermineTextLen: UInt32
    uDetermineTextPos: UInt32
    uDetermineDelimPos: UInt32
    uYomiTextLen: UInt32
    uYomiTextPos: UInt32
    uYomiDelimPos: UInt32
VALUENAME = Int32
VALUENAME_UNKNOWN: VALUENAME = 0
VALUENAME_ENTERPRISE_DEFINED_CLASS_ID: VALUENAME = 1
VALUENAME_BUILT_IN_LIST: VALUENAME = 2
WINSTATIONINFOCLASS = Int32
WINSTATIONINFOCLASS_WinStationInformation: WINSTATIONINFOCLASS = 8
class WINSTATIONINFORMATIONW(Structure):
    Reserved2: Byte * 70
    LogonId: UInt32
    Reserved3: Byte * 1140
@winfunctype_pointer
def WINWATCHNOTIFYPROC(hww: Windows.Win32.System.WindowsProgramming.HWINWATCH, hwnd: Windows.Win32.Foundation.HWND, code: UInt32, lParam: Windows.Win32.Foundation.LPARAM) -> Void: ...
class WLDP_DEVICE_SECURITY_INFORMATION(Structure):
    UnlockIdSize: UInt32
    UnlockId: c_char_p_no
    ManufacturerIDLength: UInt32
    ManufacturerID: Windows.Win32.Foundation.PWSTR
WLDP_HOST = Int32
WLDP_HOST_RUNDLL32: WLDP_HOST = 0
WLDP_HOST_SVCHOST: WLDP_HOST = 1
WLDP_HOST_MAX: WLDP_HOST = 2
WLDP_HOST_ID = Int32
WLDP_HOST_ID_UNKNOWN: WLDP_HOST_ID = 0
WLDP_HOST_ID_GLOBAL: WLDP_HOST_ID = 1
WLDP_HOST_ID_VBA: WLDP_HOST_ID = 2
WLDP_HOST_ID_WSH: WLDP_HOST_ID = 3
WLDP_HOST_ID_POWERSHELL: WLDP_HOST_ID = 4
WLDP_HOST_ID_IE: WLDP_HOST_ID = 5
WLDP_HOST_ID_MSI: WLDP_HOST_ID = 6
WLDP_HOST_ID_ALL: WLDP_HOST_ID = 7
WLDP_HOST_ID_MAX: WLDP_HOST_ID = 8
class WLDP_HOST_INFORMATION(Structure):
    dwRevision: UInt32
    dwHostId: Windows.Win32.System.WindowsProgramming.WLDP_HOST_ID
    szSource: Windows.Win32.Foundation.PWSTR
    hSource: Windows.Win32.Foundation.HANDLE
WLDP_KEY = Int32
KEY_UNKNOWN: WLDP_KEY = 0
KEY_OVERRIDE: WLDP_KEY = 1
KEY_ALL_KEYS: WLDP_KEY = 2
WLDP_POLICY_SETTING = Int32
WLDP_POLICY_SETTING_AV_PERF_MODE: WLDP_POLICY_SETTING = 1000
WLDP_WINDOWS_LOCKDOWN_MODE = Int32
WLDP_WINDOWS_LOCKDOWN_MODE_UNLOCKED: WLDP_WINDOWS_LOCKDOWN_MODE = 0
WLDP_WINDOWS_LOCKDOWN_MODE_TRIAL: WLDP_WINDOWS_LOCKDOWN_MODE = 1
WLDP_WINDOWS_LOCKDOWN_MODE_LOCKED: WLDP_WINDOWS_LOCKDOWN_MODE = 2
WLDP_WINDOWS_LOCKDOWN_MODE_MAX: WLDP_WINDOWS_LOCKDOWN_MODE = 3
WLDP_WINDOWS_LOCKDOWN_RESTRICTION = Int32
WLDP_WINDOWS_LOCKDOWN_RESTRICTION_NONE: WLDP_WINDOWS_LOCKDOWN_RESTRICTION = 0
WLDP_WINDOWS_LOCKDOWN_RESTRICTION_NOUNLOCK: WLDP_WINDOWS_LOCKDOWN_RESTRICTION = 1
WLDP_WINDOWS_LOCKDOWN_RESTRICTION_NOUNLOCK_PERMANENT: WLDP_WINDOWS_LOCKDOWN_RESTRICTION = 2
WLDP_WINDOWS_LOCKDOWN_RESTRICTION_MAX: WLDP_WINDOWS_LOCKDOWN_RESTRICTION = 3
class _D3DHAL_CALLBACKS(Structure):
    pass
class _D3DHAL_GLOBALDRIVERDATA(Structure):
    pass
make_head(_module, 'ACTCTX_SECTION_KEYED_DATA_2600')
make_head(_module, 'ACTCTX_SECTION_KEYED_DATA_ASSEMBLY_METADATA')
make_head(_module, 'ACTIVATION_CONTEXT_BASIC_INFORMATION')
make_head(_module, 'APPLICATION_RECOVERY_CALLBACK')
make_head(_module, 'CABINFOA')
make_head(_module, 'CABINFOW')
make_head(_module, 'CLIENT_ID')
make_head(_module, 'CUSTOM_SYSTEM_EVENT_TRIGGER_CONFIG')
make_head(_module, 'DATETIME')
make_head(_module, 'DCICMD')
make_head(_module, 'DCICREATEINPUT')
make_head(_module, 'DCIENUMINPUT')
make_head(_module, 'DCIOFFSCREEN')
make_head(_module, 'DCIOVERLAY')
make_head(_module, 'DCISURFACEINFO')
if ARCH in 'X64,ARM64':
    make_head(_module, 'DELAYLOAD_INFO')
if ARCH in 'X86':
    make_head(_module, 'DELAYLOAD_INFO')
make_head(_module, 'DELAYLOAD_PROC_DESCRIPTOR')
make_head(_module, 'ENUM_CALLBACK')
make_head(_module, 'FEATURE_ERROR')
make_head(_module, 'FILE_CASE_SENSITIVE_INFO')
make_head(_module, 'FILE_DISPOSITION_INFO_EX')
make_head(_module, 'HW_PROFILE_INFOA')
make_head(_module, 'HW_PROFILE_INFOW')
make_head(_module, 'ICameraUIControl')
make_head(_module, 'ICameraUIControlEventCallback')
make_head(_module, 'IClipServiceNotificationHelper')
make_head(_module, 'IContainerActivationHelper')
make_head(_module, 'IDefaultBrowserSyncSettings')
make_head(_module, 'IDeleteBrowsingHistory')
make_head(_module, 'IEditionUpgradeBroker')
make_head(_module, 'IEditionUpgradeHelper')
make_head(_module, 'IMAGE_DELAYLOAD_DESCRIPTOR')
make_head(_module, 'IMAGE_THUNK_DATA32')
make_head(_module, 'IMAGE_THUNK_DATA64')
make_head(_module, 'IMEPROA')
make_head(_module, 'IMEPROW')
make_head(_module, 'IMESTRUCT')
make_head(_module, 'IO_STATUS_BLOCK')
make_head(_module, 'IWindowsLockModeHelper')
make_head(_module, 'JAVA_TRUST')
make_head(_module, 'JIT_DEBUG_INFO')
make_head(_module, 'KEY_VALUE_ENTRY')
make_head(_module, 'LDR_DATA_TABLE_ENTRY')
make_head(_module, 'OBJECT_ATTRIBUTES')
make_head(_module, 'PDELAYLOAD_FAILURE_DLL_CALLBACK')
make_head(_module, 'PERUSERSECTIONA')
make_head(_module, 'PERUSERSECTIONW')
make_head(_module, 'PFEATURE_STATE_CHANGE_CALLBACK')
make_head(_module, 'PFIBER_CALLOUT_ROUTINE')
make_head(_module, 'PIO_APC_ROUTINE')
make_head(_module, 'PQUERYACTCTXW_FUNC')
make_head(_module, 'PUBLIC_OBJECT_BASIC_INFORMATION')
make_head(_module, 'PUBLIC_OBJECT_TYPE_INFORMATION')
make_head(_module, 'PWINSTATIONQUERYINFORMATIONW')
make_head(_module, 'PWLDP_ISAPPAPPROVEDBYPOLICY_API')
make_head(_module, 'PWLDP_ISDYNAMICCODEPOLICYENABLED_API')
make_head(_module, 'PWLDP_ISPRODUCTIONCONFIGURATION_API')
make_head(_module, 'PWLDP_ISWCOSPRODUCTIONCONFIGURATION_API')
make_head(_module, 'PWLDP_QUERYDEVICESECURITYINFORMATION_API')
make_head(_module, 'PWLDP_QUERYDYNAMICODETRUST_API')
make_head(_module, 'PWLDP_QUERYPOLICYSETTINGENABLED2_API')
make_head(_module, 'PWLDP_QUERYPOLICYSETTINGENABLED_API')
make_head(_module, 'PWLDP_QUERYWINDOWSLOCKDOWNMODE_API')
make_head(_module, 'PWLDP_QUERYWINDOWSLOCKDOWNRESTRICTION_API')
make_head(_module, 'PWLDP_RESETPRODUCTIONCONFIGURATION_API')
make_head(_module, 'PWLDP_RESETWCOSPRODUCTIONCONFIGURATION_API')
make_head(_module, 'PWLDP_SETDYNAMICCODETRUST_API')
make_head(_module, 'PWLDP_SETWINDOWSLOCKDOWNRESTRICTION_API')
make_head(_module, 'REGINSTALLA')
make_head(_module, 'STRENTRYA')
make_head(_module, 'STRENTRYW')
make_head(_module, 'STRINGEXSTRUCT')
make_head(_module, 'STRTABLEA')
make_head(_module, 'STRTABLEW')
make_head(_module, 'SYSTEM_BASIC_INFORMATION')
make_head(_module, 'SYSTEM_CODEINTEGRITY_INFORMATION')
make_head(_module, 'SYSTEM_EXCEPTION_INFORMATION')
make_head(_module, 'SYSTEM_INTERRUPT_INFORMATION')
make_head(_module, 'SYSTEM_LOOKASIDE_INFORMATION')
make_head(_module, 'SYSTEM_PERFORMANCE_INFORMATION')
make_head(_module, 'SYSTEM_POLICY_INFORMATION')
make_head(_module, 'SYSTEM_PROCESSOR_PERFORMANCE_INFORMATION')
make_head(_module, 'SYSTEM_PROCESS_INFORMATION')
make_head(_module, 'SYSTEM_REGISTRY_QUOTA_INFORMATION')
make_head(_module, 'SYSTEM_THREAD_INFORMATION')
make_head(_module, 'SYSTEM_TIMEOFDAY_INFORMATION')
if ARCH in 'X64,ARM64':
    make_head(_module, 'TCP_REQUEST_QUERY_INFORMATION_EX32_XP')
make_head(_module, 'TCP_REQUEST_QUERY_INFORMATION_EX_W2K')
make_head(_module, 'TCP_REQUEST_QUERY_INFORMATION_EX_XP')
make_head(_module, 'TCP_REQUEST_SET_INFORMATION_EX')
make_head(_module, 'TDIEntityID')
make_head(_module, 'TDIObjectID')
make_head(_module, 'TDI_TL_IO_CONTROL_ENDPOINT')
make_head(_module, 'THREAD_NAME_INFORMATION')
make_head(_module, 'UNDETERMINESTRUCT')
make_head(_module, 'WINSTATIONINFORMATIONW')
make_head(_module, 'WINWATCHNOTIFYPROC')
make_head(_module, 'WLDP_DEVICE_SECURITY_INFORMATION')
make_head(_module, 'WLDP_HOST_INFORMATION')
make_head(_module, '_D3DHAL_CALLBACKS')
make_head(_module, '_D3DHAL_GLOBALDRIVERDATA')
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
    "BAUD_075",
    "BAUD_110",
    "BAUD_115200",
    "BAUD_1200",
    "BAUD_128K",
    "BAUD_134_5",
    "BAUD_14400",
    "BAUD_150",
    "BAUD_1800",
    "BAUD_19200",
    "BAUD_2400",
    "BAUD_300",
    "BAUD_38400",
    "BAUD_4800",
    "BAUD_56K",
    "BAUD_57600",
    "BAUD_600",
    "BAUD_7200",
    "BAUD_9600",
    "BAUD_USER",
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
    "COMMPROP_INITIALIZED",
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
    "PCF_16BITMODE",
    "PCF_DTRDSR",
    "PCF_INTTIMEOUTS",
    "PCF_PARITY_CHECK",
    "PCF_RLSD",
    "PCF_RTSCTS",
    "PCF_SETXCHAR",
    "PCF_SPECIALCHARS",
    "PCF_TOTALTIMEOUTS",
    "PCF_XONXOFF",
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
    "PST_FAX",
    "PST_LAT",
    "PST_MODEM",
    "PST_NETWORK_BRIDGE",
    "PST_PARALLELPORT",
    "PST_RS232",
    "PST_RS422",
    "PST_RS423",
    "PST_RS449",
    "PST_SCANNER",
    "PST_TCPIP_TELNET",
    "PST_UNSPECIFIED",
    "PST_X25",
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
    "SP_BAUD",
    "SP_DATABITS",
    "SP_HANDSHAKING",
    "SP_PARITY",
    "SP_PARITY_CHECK",
    "SP_RLSD",
    "SP_SERIALCOMM",
    "SP_STOPBITS",
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
_arch_optional = [
    "EnableProcessOptionalXStateFeatures",
    "GetThreadEnabledXStateFeatures",
    "TCP_REQUEST_QUERY_INFORMATION_EX32_XP",
    "uaw_lstrcmpW",
    "uaw_lstrcmpiW",
    "uaw_lstrlenW",
    "uaw_wcschr",
    "uaw_wcscpy",
    "uaw_wcsicmp",
    "uaw_wcslen",
    "uaw_wcsrchr",
]