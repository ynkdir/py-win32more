from win32more import *
import win32more.Foundation
import win32more.Security
import win32more.System.Registry

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
HKEY_CLASSES_ROOT = -2147483648
HKEY_CURRENT_USER = -2147483647
HKEY_LOCAL_MACHINE = -2147483646
HKEY_USERS = -2147483645
HKEY_PERFORMANCE_DATA = -2147483644
HKEY_PERFORMANCE_TEXT = -2147483568
HKEY_PERFORMANCE_NLSTEXT = -2147483552
HKEY_CURRENT_CONFIG = -2147483643
HKEY_DYN_DATA = -2147483642
HKEY_CURRENT_USER_LOCAL_SETTINGS = -2147483641
RRF_SUBKEY_WOW6464KEY = 65536
RRF_SUBKEY_WOW6432KEY = 131072
RRF_WOW64_MASK = 196608
RRF_NOEXPAND = 268435456
RRF_ZEROONFAILURE = 536870912
REG_PROCESS_APPKEY = 1
REG_USE_CURRENT_SECURITY_CONTEXT = 2
PROVIDER_KEEPS_VALUE_LENGTH = 1
REG_MUI_STRING_TRUNCATE = 1
REG_SECURE_CONNECTION = 1
REGSTR_MAX_VALUE_LENGTH = 256
IT_COMPACT = 0
IT_TYPICAL = 1
IT_PORTABLE = 2
IT_CUSTOM = 3
DRIVERSIGN_NONE = 0
DRIVERSIGN_WARNING = 1
DRIVERSIGN_BLOCKING = 2
DOSOPTGF_DEFCLEAN = 1
DOSOPTF_DEFAULT = 1
DOSOPTF_SUPPORTED = 2
DOSOPTF_ALWAYSUSE = 4
DOSOPTF_USESPMODE = 8
DOSOPTF_PROVIDESUMB = 16
DOSOPTF_NEEDSETUP = 32
DOSOPTF_INDOSSTART = 64
DOSOPTF_MULTIPLE = 128
SUF_FIRSTTIME = 1
SUF_EXPRESS = 2
SUF_BATCHINF = 4
SUF_CLEAN = 8
SUF_INSETUP = 16
SUF_NETSETUP = 32
SUF_NETHDBOOT = 64
SUF_NETRPLBOOT = 128
SUF_SBSCOPYOK = 256
VPDF_DISABLEPWRMGMT = 1
VPDF_FORCEAPM10MODE = 2
VPDF_SKIPINTELSLCHECK = 4
VPDF_DISABLEPWRSTATUSPOLL = 8
VPDF_DISABLERINGRESUME = 16
VPDF_SHOWMULTIBATT = 32
BIF_SHOWSIMILARDRIVERS = 1
BIF_RAWDEVICENEEDSDRIVER = 2
PCMCIA_OPT_HAVE_SOCKET = 1
PCMCIA_OPT_AUTOMEM = 4
PCMCIA_OPT_NO_SOUND = 8
PCMCIA_OPT_NO_AUDIO = 16
PCMCIA_OPT_NO_APMREMOVE = 32
PCMCIA_DEF_MEMBEGIN = 786432
PCMCIA_DEF_MEMEND = 16777215
PCMCIA_DEF_MEMLEN = 4096
PCMCIA_DEF_MIN_REGION = 65536
PCI_OPTIONS_USE_BIOS = 1
PCI_OPTIONS_USE_IRQ_STEERING = 2
AGP_FLAG_NO_1X_RATE = 1
AGP_FLAG_NO_2X_RATE = 2
AGP_FLAG_NO_4X_RATE = 4
AGP_FLAG_NO_8X_RATE = 8
AGP_FLAG_REVERSE_INITIALIZATION = 128
AGP_FLAG_NO_SBA_ENABLE = 256
AGP_FLAG_NO_FW_ENABLE = 512
AGP_FLAG_SPECIAL_TARGET = 1048575
AGP_FLAG_SPECIAL_RESERVE = 1015808
REGSTR_VAL_MAX_HCID_LEN = 1024
REGDF_NOTDETIO = 1
REGDF_NOTDETMEM = 2
REGDF_NOTDETIRQ = 4
REGDF_NOTDETDMA = 8
REGDF_NEEDFULLCONFIG = 16
REGDF_GENFORCEDCONFIG = 32
REGDF_NODETCONFIG = 32768
REGDF_CONFLICTIO = 65536
REGDF_CONFLICTMEM = 131072
REGDF_CONFLICTIRQ = 262144
REGDF_CONFLICTDMA = 524288
REGDF_MAPIRQ2TO9 = 1048576
REGDF_NOTVERIFIED = 2147483648
APMMENUSUSPEND_DISABLED = 0
APMMENUSUSPEND_ENABLED = 1
APMMENUSUSPEND_UNDOCKED = 2
APMMENUSUSPEND_NOCHANGE = 128
APMTIMEOUT_DISABLED = 0
CONFIGFLAG_DISABLED = 1
CONFIGFLAG_REMOVED = 2
CONFIGFLAG_MANUAL_INSTALL = 4
CONFIGFLAG_IGNORE_BOOT_LC = 8
CONFIGFLAG_NET_BOOT = 16
CONFIGFLAG_REINSTALL = 32
CONFIGFLAG_FAILEDINSTALL = 64
CONFIGFLAG_CANTSTOPACHILD = 128
CONFIGFLAG_OKREMOVEROM = 256
CONFIGFLAG_NOREMOVEEXIT = 512
CONFIGFLAG_FINISH_INSTALL = 1024
CONFIGFLAG_NEEDS_FORCED_CONFIG = 2048
CONFIGFLAG_NETBOOT_CARD = 4096
CONFIGFLAG_PARTIAL_LOG_CONF = 8192
CONFIGFLAG_SUPPRESS_SURPRISE = 16384
CONFIGFLAG_VERIFY_HARDWARE = 32768
CONFIGFLAG_FINISHINSTALL_UI = 65536
CONFIGFLAG_FINISHINSTALL_ACTION = 131072
CONFIGFLAG_BOOT_DEVICE = 262144
CONFIGFLAG_NEEDS_CLASS_CONFIG = 524288
CSCONFIGFLAG_BITS = 7
CSCONFIGFLAG_DISABLED = 1
CSCONFIGFLAG_DO_NOT_CREATE = 2
CSCONFIGFLAG_DO_NOT_START = 4
DMSTATEFLAG_APPLYTOALL = 1
NUM_RESOURCE_MAP = 256
MF_FLAGS_EVEN_IF_NO_RESOURCE = 1
MF_FLAGS_NO_CREATE_IF_NO_RESOURCE = 2
MF_FLAGS_FILL_IN_UNKNOWN_RESOURCE = 4
MF_FLAGS_CREATE_BUT_NO_SHOW_DISABLED = 8
EISAFLAG_NO_IO_MERGE = 1
EISAFLAG_SLOT_IO_FIRST = 2
EISA_NO_MAX_FUNCTION = 255
NUM_EISA_RANGES = 4
PCIC_DEFAULT_IRQMASK = 20152
PCIC_DEFAULT_NUMSOCKETS = 0
DTRESULTOK = 0
DTRESULTFIX = 1
DTRESULTPROB = 2
DTRESULTPART = 3
PIR_OPTION_ENABLED = 1
PIR_OPTION_REGISTRY = 2
PIR_OPTION_MSSPEC = 4
PIR_OPTION_REALMODE = 8
PIR_OPTION_DEFAULT = 15
PIR_STATUS_ERROR = 0
PIR_STATUS_ENABLED = 1
PIR_STATUS_DISABLED = 2
PIR_STATUS_MAX = 3
PIR_STATUS_TABLE_REGISTRY = 0
PIR_STATUS_TABLE_MSSPEC = 1
PIR_STATUS_TABLE_REALMODE = 2
PIR_STATUS_TABLE_NONE = 3
PIR_STATUS_TABLE_ERROR = 4
PIR_STATUS_TABLE_BAD = 5
PIR_STATUS_TABLE_SUCCESS = 6
PIR_STATUS_TABLE_MAX = 7
PIR_STATUS_MINIPORT_NORMAL = 0
PIR_STATUS_MINIPORT_COMPATIBLE = 1
PIR_STATUS_MINIPORT_OVERRIDE = 2
PIR_STATUS_MINIPORT_NONE = 3
PIR_STATUS_MINIPORT_ERROR = 4
PIR_STATUS_MINIPORT_NOKEY = 5
PIR_STATUS_MINIPORT_SUCCESS = 6
PIR_STATUS_MINIPORT_INVALID = 7
PIR_STATUS_MINIPORT_MAX = 8
LASTGOOD_OPERATION = 255
LASTGOOD_OPERATION_NOPOSTPROC = 0
LASTGOOD_OPERATION_DELETE = 1
REG_VALUE_TYPE = UInt32
REG_NONE = 0
REG_SZ = 1
REG_EXPAND_SZ = 2
REG_BINARY = 3
REG_DWORD = 4
REG_DWORD_LITTLE_ENDIAN = 4
REG_DWORD_BIG_ENDIAN = 5
REG_LINK = 6
REG_MULTI_SZ = 7
REG_RESOURCE_LIST = 8
REG_FULL_RESOURCE_DESCRIPTOR = 9
REG_RESOURCE_REQUIREMENTS_LIST = 10
REG_QWORD = 11
REG_QWORD_LITTLE_ENDIAN = 11
REG_SAM_FLAGS = UInt32
KEY_QUERY_VALUE = 1
KEY_SET_VALUE = 2
KEY_CREATE_SUB_KEY = 4
KEY_ENUMERATE_SUB_KEYS = 8
KEY_NOTIFY = 16
KEY_CREATE_LINK = 32
KEY_WOW64_32KEY = 512
KEY_WOW64_64KEY = 256
KEY_WOW64_RES = 768
KEY_READ = 131097
KEY_WRITE = 131078
KEY_EXECUTE = 131097
KEY_ALL_ACCESS = 983103
REG_OPEN_CREATE_OPTIONS = UInt32
REG_OPTION_RESERVED = 0
REG_OPTION_NON_VOLATILE = 0
REG_OPTION_VOLATILE = 1
REG_OPTION_CREATE_LINK = 2
REG_OPTION_BACKUP_RESTORE = 4
REG_OPTION_OPEN_LINK = 8
REG_OPTION_DONT_VIRTUALIZE = 16
REG_CREATE_KEY_DISPOSITION = UInt32
REG_CREATED_NEW_KEY = 1
REG_OPENED_EXISTING_KEY = 2
REG_SAVE_FORMAT = UInt32
REG_STANDARD_FORMAT = 1
REG_LATEST_FORMAT = 2
REG_NO_COMPRESSION = 4
REG_RESTORE_KEY_FLAGS = Int32
REG_FORCE_RESTORE = 8
REG_WHOLE_HIVE_VOLATILE = 1
REG_NOTIFY_FILTER = UInt32
REG_NOTIFY_CHANGE_NAME = 1
REG_NOTIFY_CHANGE_ATTRIBUTES = 2
REG_NOTIFY_CHANGE_LAST_SET = 4
REG_NOTIFY_CHANGE_SECURITY = 8
REG_NOTIFY_THREAD_AGNOSTIC = 268435456
RRF_RT = UInt32
RRF_RT_ANY = 65535
RRF_RT_DWORD = 24
RRF_RT_QWORD = 72
RRF_RT_REG_BINARY = 8
RRF_RT_REG_DWORD = 16
RRF_RT_REG_EXPAND_SZ = 4
RRF_RT_REG_MULTI_SZ = 32
RRF_RT_REG_NONE = 1
RRF_RT_REG_QWORD = 64
RRF_RT_REG_SZ = 2
HKEY = IntPtr
def _define_val_context_head():
    class val_context(Structure):
        pass
    return val_context
def _define_val_context():
    val_context = win32more.System.Registry.val_context_head
    val_context._fields_ = [
        ("valuelen", Int32),
        ("value_context", c_void_p),
        ("val_buff_ptr", c_void_p),
    ]
    return val_context
def _define_pvalueA_head():
    class pvalueA(Structure):
        pass
    return pvalueA
def _define_pvalueA():
    pvalueA = win32more.System.Registry.pvalueA_head
    pvalueA._fields_ = [
        ("pv_valuename", win32more.Foundation.PSTR),
        ("pv_valuelen", Int32),
        ("pv_value_context", c_void_p),
        ("pv_type", UInt32),
    ]
    return pvalueA
def _define_pvalueW_head():
    class pvalueW(Structure):
        pass
    return pvalueW
def _define_pvalueW():
    pvalueW = win32more.System.Registry.pvalueW_head
    pvalueW._fields_ = [
        ("pv_valuename", win32more.Foundation.PWSTR),
        ("pv_valuelen", Int32),
        ("pv_value_context", c_void_p),
        ("pv_type", UInt32),
    ]
    return pvalueW
def _define_PQUERYHANDLER():
    return CFUNCTYPE(UInt32,c_void_p,POINTER(win32more.System.Registry.val_context_head),UInt32,c_void_p,POINTER(UInt32),UInt32, use_last_error=False)
def _define_provider_info_head():
    class provider_info(Structure):
        pass
    return provider_info
def _define_provider_info():
    provider_info = win32more.System.Registry.provider_info_head
    provider_info._fields_ = [
        ("pi_R0_1val", win32more.System.Registry.PQUERYHANDLER),
        ("pi_R0_allvals", win32more.System.Registry.PQUERYHANDLER),
        ("pi_R3_1val", win32more.System.Registry.PQUERYHANDLER),
        ("pi_R3_allvals", win32more.System.Registry.PQUERYHANDLER),
        ("pi_flags", UInt32),
        ("pi_key_context", c_void_p),
    ]
    return provider_info
def _define_VALENTA_head():
    class VALENTA(Structure):
        pass
    return VALENTA
def _define_VALENTA():
    VALENTA = win32more.System.Registry.VALENTA_head
    VALENTA._fields_ = [
        ("ve_valuename", win32more.Foundation.PSTR),
        ("ve_valuelen", UInt32),
        ("ve_valueptr", UIntPtr),
        ("ve_type", win32more.System.Registry.REG_VALUE_TYPE),
    ]
    return VALENTA
def _define_VALENTW_head():
    class VALENTW(Structure):
        pass
    return VALENTW
def _define_VALENTW():
    VALENTW = win32more.System.Registry.VALENTW_head
    VALENTW._fields_ = [
        ("ve_valuename", win32more.Foundation.PWSTR),
        ("ve_valuelen", UInt32),
        ("ve_valueptr", UIntPtr),
        ("ve_type", win32more.System.Registry.REG_VALUE_TYPE),
    ]
    return VALENTW
def _define_DSKTLSYSTEMTIME_head():
    class DSKTLSYSTEMTIME(Structure):
        pass
    return DSKTLSYSTEMTIME
def _define_DSKTLSYSTEMTIME():
    DSKTLSYSTEMTIME = win32more.System.Registry.DSKTLSYSTEMTIME_head
    DSKTLSYSTEMTIME._fields_ = [
        ("wYear", UInt16),
        ("wMonth", UInt16),
        ("wDayOfWeek", UInt16),
        ("wDay", UInt16),
        ("wHour", UInt16),
        ("wMinute", UInt16),
        ("wSecond", UInt16),
        ("wMilliseconds", UInt16),
        ("wResult", UInt16),
    ]
    return DSKTLSYSTEMTIME
def _define_RegCloseKey():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY, use_last_error=False)(("RegCloseKey", windll["ADVAPI32"]), ((1, 'hKey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegOverridePredefKey():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.System.Registry.HKEY, use_last_error=False)(("RegOverridePredefKey", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'hNewHKey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegOpenUserClassesRoot():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.Foundation.HANDLE,UInt32,UInt32,POINTER(win32more.System.Registry.HKEY), use_last_error=False)(("RegOpenUserClassesRoot", windll["ADVAPI32"]), ((1, 'hToken'),(1, 'dwOptions'),(1, 'samDesired'),(1, 'phkResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegOpenCurrentUser():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,UInt32,POINTER(win32more.System.Registry.HKEY), use_last_error=False)(("RegOpenCurrentUser", windll["ADVAPI32"]), ((1, 'samDesired'),(1, 'phkResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegDisablePredefinedCache():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS, use_last_error=False)(("RegDisablePredefinedCache", windll["ADVAPI32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegDisablePredefinedCacheEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS, use_last_error=False)(("RegDisablePredefinedCacheEx", windll["ADVAPI32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegConnectRegistryA():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.Foundation.PSTR,win32more.System.Registry.HKEY,POINTER(win32more.System.Registry.HKEY), use_last_error=False)(("RegConnectRegistryA", windll["ADVAPI32"]), ((1, 'lpMachineName'),(1, 'hKey'),(1, 'phkResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegConnectRegistryW():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.Foundation.PWSTR,win32more.System.Registry.HKEY,POINTER(win32more.System.Registry.HKEY), use_last_error=False)(("RegConnectRegistryW", windll["ADVAPI32"]), ((1, 'lpMachineName'),(1, 'hKey'),(1, 'phkResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegConnectRegistry():
    return win32more.System.Registry.RegConnectRegistryW
def _define_RegConnectRegistryExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.Foundation.PSTR,win32more.System.Registry.HKEY,UInt32,POINTER(win32more.System.Registry.HKEY), use_last_error=False)(("RegConnectRegistryExA", windll["ADVAPI32"]), ((1, 'lpMachineName'),(1, 'hKey'),(1, 'Flags'),(1, 'phkResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegConnectRegistryExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.Foundation.PWSTR,win32more.System.Registry.HKEY,UInt32,POINTER(win32more.System.Registry.HKEY), use_last_error=False)(("RegConnectRegistryExW", windll["ADVAPI32"]), ((1, 'lpMachineName'),(1, 'hKey'),(1, 'Flags'),(1, 'phkResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegConnectRegistryEx():
    return win32more.System.Registry.RegConnectRegistryExW
def _define_RegCreateKeyA():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PSTR,POINTER(win32more.System.Registry.HKEY), use_last_error=False)(("RegCreateKeyA", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'lpSubKey'),(1, 'phkResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegCreateKeyW():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PWSTR,POINTER(win32more.System.Registry.HKEY), use_last_error=False)(("RegCreateKeyW", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'lpSubKey'),(1, 'phkResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegCreateKey():
    return win32more.System.Registry.RegCreateKeyW
def _define_RegCreateKeyExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,win32more.System.Registry.REG_OPEN_CREATE_OPTIONS,win32more.System.Registry.REG_SAM_FLAGS,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),POINTER(win32more.System.Registry.HKEY),POINTER(win32more.System.Registry.REG_CREATE_KEY_DISPOSITION), use_last_error=False)(("RegCreateKeyExA", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'lpSubKey'),(1, 'Reserved'),(1, 'lpClass'),(1, 'dwOptions'),(1, 'samDesired'),(1, 'lpSecurityAttributes'),(1, 'phkResult'),(1, 'lpdwDisposition'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegCreateKeyExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,win32more.System.Registry.REG_OPEN_CREATE_OPTIONS,win32more.System.Registry.REG_SAM_FLAGS,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),POINTER(win32more.System.Registry.HKEY),POINTER(win32more.System.Registry.REG_CREATE_KEY_DISPOSITION), use_last_error=False)(("RegCreateKeyExW", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'lpSubKey'),(1, 'Reserved'),(1, 'lpClass'),(1, 'dwOptions'),(1, 'samDesired'),(1, 'lpSecurityAttributes'),(1, 'phkResult'),(1, 'lpdwDisposition'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegCreateKeyEx():
    return win32more.System.Registry.RegCreateKeyExW
def _define_RegCreateKeyTransactedA():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,win32more.System.Registry.REG_OPEN_CREATE_OPTIONS,win32more.System.Registry.REG_SAM_FLAGS,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),POINTER(win32more.System.Registry.HKEY),POINTER(win32more.System.Registry.REG_CREATE_KEY_DISPOSITION),win32more.Foundation.HANDLE,c_void_p, use_last_error=False)(("RegCreateKeyTransactedA", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'lpSubKey'),(1, 'Reserved'),(1, 'lpClass'),(1, 'dwOptions'),(1, 'samDesired'),(1, 'lpSecurityAttributes'),(1, 'phkResult'),(1, 'lpdwDisposition'),(1, 'hTransaction'),(1, 'pExtendedParemeter'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegCreateKeyTransactedW():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,win32more.System.Registry.REG_OPEN_CREATE_OPTIONS,win32more.System.Registry.REG_SAM_FLAGS,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),POINTER(win32more.System.Registry.HKEY),POINTER(win32more.System.Registry.REG_CREATE_KEY_DISPOSITION),win32more.Foundation.HANDLE,c_void_p, use_last_error=False)(("RegCreateKeyTransactedW", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'lpSubKey'),(1, 'Reserved'),(1, 'lpClass'),(1, 'dwOptions'),(1, 'samDesired'),(1, 'lpSecurityAttributes'),(1, 'phkResult'),(1, 'lpdwDisposition'),(1, 'hTransaction'),(1, 'pExtendedParemeter'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegCreateKeyTransacted():
    return win32more.System.Registry.RegCreateKeyTransactedW
def _define_RegDeleteKeyA():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PSTR, use_last_error=False)(("RegDeleteKeyA", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'lpSubKey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegDeleteKeyW():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PWSTR, use_last_error=False)(("RegDeleteKeyW", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'lpSubKey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegDeleteKey():
    return win32more.System.Registry.RegDeleteKeyW
def _define_RegDeleteKeyExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PSTR,UInt32,UInt32, use_last_error=False)(("RegDeleteKeyExA", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'lpSubKey'),(1, 'samDesired'),(1, 'Reserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegDeleteKeyExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PWSTR,UInt32,UInt32, use_last_error=False)(("RegDeleteKeyExW", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'lpSubKey'),(1, 'samDesired'),(1, 'Reserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegDeleteKeyEx():
    return win32more.System.Registry.RegDeleteKeyExW
def _define_RegDeleteKeyTransactedA():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PSTR,UInt32,UInt32,win32more.Foundation.HANDLE,c_void_p, use_last_error=False)(("RegDeleteKeyTransactedA", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'lpSubKey'),(1, 'samDesired'),(1, 'Reserved'),(1, 'hTransaction'),(1, 'pExtendedParameter'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegDeleteKeyTransactedW():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PWSTR,UInt32,UInt32,win32more.Foundation.HANDLE,c_void_p, use_last_error=False)(("RegDeleteKeyTransactedW", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'lpSubKey'),(1, 'samDesired'),(1, 'Reserved'),(1, 'hTransaction'),(1, 'pExtendedParameter'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegDeleteKeyTransacted():
    return win32more.System.Registry.RegDeleteKeyTransactedW
def _define_RegDisableReflectionKey():
    try:
        return WINFUNCTYPE(Int32,win32more.System.Registry.HKEY, use_last_error=False)(("RegDisableReflectionKey", windll["ADVAPI32"]), ((1, 'hBase'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegEnableReflectionKey():
    try:
        return WINFUNCTYPE(Int32,win32more.System.Registry.HKEY, use_last_error=False)(("RegEnableReflectionKey", windll["ADVAPI32"]), ((1, 'hBase'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegQueryReflectionKey():
    try:
        return WINFUNCTYPE(Int32,win32more.System.Registry.HKEY,POINTER(win32more.Foundation.BOOL), use_last_error=False)(("RegQueryReflectionKey", windll["ADVAPI32"]), ((1, 'hBase'),(1, 'bIsReflectionDisabled'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegDeleteValueA():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PSTR, use_last_error=False)(("RegDeleteValueA", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'lpValueName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegDeleteValueW():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PWSTR, use_last_error=False)(("RegDeleteValueW", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'lpValueName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegDeleteValue():
    return win32more.System.Registry.RegDeleteValueW
def _define_RegEnumKeyA():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,UInt32,POINTER(Byte),UInt32, use_last_error=False)(("RegEnumKeyA", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'dwIndex'),(1, 'lpName'),(1, 'cchName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegEnumKeyW():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,UInt32,POINTER(Char),UInt32, use_last_error=False)(("RegEnumKeyW", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'dwIndex'),(1, 'lpName'),(1, 'cchName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegEnumKey():
    return win32more.System.Registry.RegEnumKeyW
def _define_RegEnumKeyExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,UInt32,POINTER(Byte),POINTER(UInt32),POINTER(UInt32),POINTER(Byte),POINTER(UInt32),POINTER(win32more.Foundation.FILETIME_head), use_last_error=False)(("RegEnumKeyExA", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'dwIndex'),(1, 'lpName'),(1, 'lpcchName'),(1, 'lpReserved'),(1, 'lpClass'),(1, 'lpcchClass'),(1, 'lpftLastWriteTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegEnumKeyExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,UInt32,POINTER(Char),POINTER(UInt32),POINTER(UInt32),POINTER(Char),POINTER(UInt32),POINTER(win32more.Foundation.FILETIME_head), use_last_error=False)(("RegEnumKeyExW", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'dwIndex'),(1, 'lpName'),(1, 'lpcchName'),(1, 'lpReserved'),(1, 'lpClass'),(1, 'lpcchClass'),(1, 'lpftLastWriteTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegEnumKeyEx():
    return win32more.System.Registry.RegEnumKeyExW
def _define_RegEnumValueA():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,UInt32,POINTER(Byte),POINTER(UInt32),POINTER(UInt32),POINTER(UInt32),c_char_p_no,POINTER(UInt32), use_last_error=False)(("RegEnumValueA", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'dwIndex'),(1, 'lpValueName'),(1, 'lpcchValueName'),(1, 'lpReserved'),(1, 'lpType'),(1, 'lpData'),(1, 'lpcbData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegEnumValueW():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,UInt32,POINTER(Char),POINTER(UInt32),POINTER(UInt32),POINTER(UInt32),c_char_p_no,POINTER(UInt32), use_last_error=False)(("RegEnumValueW", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'dwIndex'),(1, 'lpValueName'),(1, 'lpcchValueName'),(1, 'lpReserved'),(1, 'lpType'),(1, 'lpData'),(1, 'lpcbData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegEnumValue():
    return win32more.System.Registry.RegEnumValueW
def _define_RegFlushKey():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY, use_last_error=False)(("RegFlushKey", windll["ADVAPI32"]), ((1, 'hKey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegGetKeySecurity():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,UInt32,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),POINTER(UInt32), use_last_error=False)(("RegGetKeySecurity", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'SecurityInformation'),(1, 'pSecurityDescriptor'),(1, 'lpcbSecurityDescriptor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegLoadKeyA():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("RegLoadKeyA", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'lpSubKey'),(1, 'lpFile'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegLoadKeyW():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("RegLoadKeyW", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'lpSubKey'),(1, 'lpFile'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegLoadKey():
    return win32more.System.Registry.RegLoadKeyW
def _define_RegNotifyChangeKeyValue():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.BOOL,win32more.System.Registry.REG_NOTIFY_FILTER,win32more.Foundation.HANDLE,win32more.Foundation.BOOL, use_last_error=False)(("RegNotifyChangeKeyValue", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'bWatchSubtree'),(1, 'dwNotifyFilter'),(1, 'hEvent'),(1, 'fAsynchronous'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegOpenKeyA():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PSTR,POINTER(win32more.System.Registry.HKEY), use_last_error=False)(("RegOpenKeyA", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'lpSubKey'),(1, 'phkResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegOpenKeyW():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PWSTR,POINTER(win32more.System.Registry.HKEY), use_last_error=False)(("RegOpenKeyW", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'lpSubKey'),(1, 'phkResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegOpenKey():
    return win32more.System.Registry.RegOpenKeyW
def _define_RegOpenKeyExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PSTR,UInt32,win32more.System.Registry.REG_SAM_FLAGS,POINTER(win32more.System.Registry.HKEY), use_last_error=False)(("RegOpenKeyExA", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'lpSubKey'),(1, 'ulOptions'),(1, 'samDesired'),(1, 'phkResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegOpenKeyExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PWSTR,UInt32,win32more.System.Registry.REG_SAM_FLAGS,POINTER(win32more.System.Registry.HKEY), use_last_error=False)(("RegOpenKeyExW", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'lpSubKey'),(1, 'ulOptions'),(1, 'samDesired'),(1, 'phkResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegOpenKeyEx():
    return win32more.System.Registry.RegOpenKeyExW
def _define_RegOpenKeyTransactedA():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PSTR,UInt32,win32more.System.Registry.REG_SAM_FLAGS,POINTER(win32more.System.Registry.HKEY),win32more.Foundation.HANDLE,c_void_p, use_last_error=False)(("RegOpenKeyTransactedA", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'lpSubKey'),(1, 'ulOptions'),(1, 'samDesired'),(1, 'phkResult'),(1, 'hTransaction'),(1, 'pExtendedParemeter'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegOpenKeyTransactedW():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PWSTR,UInt32,win32more.System.Registry.REG_SAM_FLAGS,POINTER(win32more.System.Registry.HKEY),win32more.Foundation.HANDLE,c_void_p, use_last_error=False)(("RegOpenKeyTransactedW", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'lpSubKey'),(1, 'ulOptions'),(1, 'samDesired'),(1, 'phkResult'),(1, 'hTransaction'),(1, 'pExtendedParemeter'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegOpenKeyTransacted():
    return win32more.System.Registry.RegOpenKeyTransactedW
def _define_RegQueryInfoKeyA():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,POINTER(Byte),POINTER(UInt32),POINTER(UInt32),POINTER(UInt32),POINTER(UInt32),POINTER(UInt32),POINTER(UInt32),POINTER(UInt32),POINTER(UInt32),POINTER(UInt32),POINTER(win32more.Foundation.FILETIME_head), use_last_error=False)(("RegQueryInfoKeyA", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'lpClass'),(1, 'lpcchClass'),(1, 'lpReserved'),(1, 'lpcSubKeys'),(1, 'lpcbMaxSubKeyLen'),(1, 'lpcbMaxClassLen'),(1, 'lpcValues'),(1, 'lpcbMaxValueNameLen'),(1, 'lpcbMaxValueLen'),(1, 'lpcbSecurityDescriptor'),(1, 'lpftLastWriteTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegQueryInfoKeyW():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,POINTER(Char),POINTER(UInt32),POINTER(UInt32),POINTER(UInt32),POINTER(UInt32),POINTER(UInt32),POINTER(UInt32),POINTER(UInt32),POINTER(UInt32),POINTER(UInt32),POINTER(win32more.Foundation.FILETIME_head), use_last_error=False)(("RegQueryInfoKeyW", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'lpClass'),(1, 'lpcchClass'),(1, 'lpReserved'),(1, 'lpcSubKeys'),(1, 'lpcbMaxSubKeyLen'),(1, 'lpcbMaxClassLen'),(1, 'lpcValues'),(1, 'lpcbMaxValueNameLen'),(1, 'lpcbMaxValueLen'),(1, 'lpcbSecurityDescriptor'),(1, 'lpftLastWriteTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegQueryInfoKey():
    return win32more.System.Registry.RegQueryInfoKeyW
def _define_RegQueryValueA():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(Int32), use_last_error=False)(("RegQueryValueA", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'lpSubKey'),(1, 'lpData'),(1, 'lpcbData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegQueryValueW():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(Int32), use_last_error=False)(("RegQueryValueW", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'lpSubKey'),(1, 'lpData'),(1, 'lpcbData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegQueryValue():
    return win32more.System.Registry.RegQueryValueW
def _define_RegQueryMultipleValuesA():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,POINTER(win32more.System.Registry.VALENTA),UInt32,win32more.Foundation.PSTR,POINTER(UInt32), use_last_error=False)(("RegQueryMultipleValuesA", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'val_list'),(1, 'num_vals'),(1, 'lpValueBuf'),(1, 'ldwTotsize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegQueryMultipleValuesW():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,POINTER(win32more.System.Registry.VALENTW),UInt32,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(("RegQueryMultipleValuesW", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'val_list'),(1, 'num_vals'),(1, 'lpValueBuf'),(1, 'ldwTotsize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegQueryMultipleValues():
    return win32more.System.Registry.RegQueryMultipleValuesW
def _define_RegQueryValueExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PSTR,POINTER(UInt32),POINTER(win32more.System.Registry.REG_VALUE_TYPE),c_char_p_no,POINTER(UInt32), use_last_error=False)(("RegQueryValueExA", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'lpValueName'),(1, 'lpReserved'),(1, 'lpType'),(1, 'lpData'),(1, 'lpcbData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegQueryValueExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(win32more.System.Registry.REG_VALUE_TYPE),c_char_p_no,POINTER(UInt32), use_last_error=False)(("RegQueryValueExW", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'lpValueName'),(1, 'lpReserved'),(1, 'lpType'),(1, 'lpData'),(1, 'lpcbData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegQueryValueEx():
    return win32more.System.Registry.RegQueryValueExW
def _define_RegReplaceKeyA():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("RegReplaceKeyA", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'lpSubKey'),(1, 'lpNewFile'),(1, 'lpOldFile'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegReplaceKeyW():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("RegReplaceKeyW", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'lpSubKey'),(1, 'lpNewFile'),(1, 'lpOldFile'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegReplaceKey():
    return win32more.System.Registry.RegReplaceKeyW
def _define_RegRestoreKeyA():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PSTR,win32more.System.Registry.REG_RESTORE_KEY_FLAGS, use_last_error=False)(("RegRestoreKeyA", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'lpFile'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegRestoreKeyW():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PWSTR,win32more.System.Registry.REG_RESTORE_KEY_FLAGS, use_last_error=False)(("RegRestoreKeyW", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'lpFile'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegRestoreKey():
    return win32more.System.Registry.RegRestoreKeyW
def _define_RegRenameKey():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("RegRenameKey", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'lpSubKeyName'),(1, 'lpNewKeyName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegSaveKeyA():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PSTR,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), use_last_error=False)(("RegSaveKeyA", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'lpFile'),(1, 'lpSecurityAttributes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegSaveKeyW():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PWSTR,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), use_last_error=False)(("RegSaveKeyW", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'lpFile'),(1, 'lpSecurityAttributes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegSaveKey():
    return win32more.System.Registry.RegSaveKeyW
def _define_RegSetKeySecurity():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,UInt32,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head), use_last_error=False)(("RegSetKeySecurity", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'SecurityInformation'),(1, 'pSecurityDescriptor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegSetValueA():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PSTR,win32more.System.Registry.REG_VALUE_TYPE,win32more.Foundation.PSTR,UInt32, use_last_error=False)(("RegSetValueA", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'lpSubKey'),(1, 'dwType'),(1, 'lpData'),(1, 'cbData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegSetValueW():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PWSTR,win32more.System.Registry.REG_VALUE_TYPE,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(("RegSetValueW", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'lpSubKey'),(1, 'dwType'),(1, 'lpData'),(1, 'cbData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegSetValue():
    return win32more.System.Registry.RegSetValueW
def _define_RegSetValueExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PSTR,UInt32,win32more.System.Registry.REG_VALUE_TYPE,c_char_p_no,UInt32, use_last_error=False)(("RegSetValueExA", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'lpValueName'),(1, 'Reserved'),(1, 'dwType'),(1, 'lpData'),(1, 'cbData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegSetValueExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PWSTR,UInt32,win32more.System.Registry.REG_VALUE_TYPE,c_char_p_no,UInt32, use_last_error=False)(("RegSetValueExW", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'lpValueName'),(1, 'Reserved'),(1, 'dwType'),(1, 'lpData'),(1, 'cbData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegSetValueEx():
    return win32more.System.Registry.RegSetValueExW
def _define_RegUnLoadKeyA():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PSTR, use_last_error=False)(("RegUnLoadKeyA", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'lpSubKey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegUnLoadKeyW():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PWSTR, use_last_error=False)(("RegUnLoadKeyW", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'lpSubKey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegUnLoadKey():
    return win32more.System.Registry.RegUnLoadKeyW
def _define_RegDeleteKeyValueA():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("RegDeleteKeyValueA", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'lpSubKey'),(1, 'lpValueName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegDeleteKeyValueW():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("RegDeleteKeyValueW", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'lpSubKey'),(1, 'lpValueName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegDeleteKeyValue():
    return win32more.System.Registry.RegDeleteKeyValueW
def _define_RegSetKeyValueA():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32,c_void_p,UInt32, use_last_error=False)(("RegSetKeyValueA", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'lpSubKey'),(1, 'lpValueName'),(1, 'dwType'),(1, 'lpData'),(1, 'cbData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegSetKeyValueW():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,c_void_p,UInt32, use_last_error=False)(("RegSetKeyValueW", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'lpSubKey'),(1, 'lpValueName'),(1, 'dwType'),(1, 'lpData'),(1, 'cbData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegSetKeyValue():
    return win32more.System.Registry.RegSetKeyValueW
def _define_RegDeleteTreeA():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PSTR, use_last_error=False)(("RegDeleteTreeA", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'lpSubKey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegDeleteTreeW():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PWSTR, use_last_error=False)(("RegDeleteTreeW", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'lpSubKey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegDeleteTree():
    return win32more.System.Registry.RegDeleteTreeW
def _define_RegCopyTreeA():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PSTR,win32more.System.Registry.HKEY, use_last_error=False)(("RegCopyTreeA", windll["ADVAPI32"]), ((1, 'hKeySrc'),(1, 'lpSubKey'),(1, 'hKeyDest'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegGetValueA():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.System.Registry.RRF_RT,POINTER(UInt32),c_void_p,POINTER(UInt32), use_last_error=False)(("RegGetValueA", windll["ADVAPI32"]), ((1, 'hkey'),(1, 'lpSubKey'),(1, 'lpValue'),(1, 'dwFlags'),(1, 'pdwType'),(1, 'pvData'),(1, 'pcbData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegGetValueW():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.System.Registry.RRF_RT,POINTER(UInt32),c_void_p,POINTER(UInt32), use_last_error=False)(("RegGetValueW", windll["ADVAPI32"]), ((1, 'hkey'),(1, 'lpSubKey'),(1, 'lpValue'),(1, 'dwFlags'),(1, 'pdwType'),(1, 'pvData'),(1, 'pcbData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegGetValue():
    return win32more.System.Registry.RegGetValueW
def _define_RegCopyTreeW():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PWSTR,win32more.System.Registry.HKEY, use_last_error=False)(("RegCopyTreeW", windll["ADVAPI32"]), ((1, 'hKeySrc'),(1, 'lpSubKey'),(1, 'hKeyDest'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegCopyTree():
    return win32more.System.Registry.RegCopyTreeW
def _define_RegLoadMUIStringA():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32,POINTER(UInt32),UInt32,win32more.Foundation.PSTR, use_last_error=False)(("RegLoadMUIStringA", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'pszValue'),(1, 'pszOutBuf'),(1, 'cbOutBuf'),(1, 'pcbData'),(1, 'Flags'),(1, 'pszDirectory'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegLoadMUIStringW():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32),UInt32,win32more.Foundation.PWSTR, use_last_error=False)(("RegLoadMUIStringW", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'pszValue'),(1, 'pszOutBuf'),(1, 'cbOutBuf'),(1, 'pcbData'),(1, 'Flags'),(1, 'pszDirectory'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegLoadMUIString():
    return win32more.System.Registry.RegLoadMUIStringW
def _define_RegLoadAppKeyA():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.Foundation.PSTR,POINTER(win32more.System.Registry.HKEY),UInt32,UInt32,UInt32, use_last_error=False)(("RegLoadAppKeyA", windll["ADVAPI32"]), ((1, 'lpFile'),(1, 'phkResult'),(1, 'samDesired'),(1, 'dwOptions'),(1, 'Reserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegLoadAppKeyW():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.Foundation.PWSTR,POINTER(win32more.System.Registry.HKEY),UInt32,UInt32,UInt32, use_last_error=False)(("RegLoadAppKeyW", windll["ADVAPI32"]), ((1, 'lpFile'),(1, 'phkResult'),(1, 'samDesired'),(1, 'dwOptions'),(1, 'Reserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegLoadAppKey():
    return win32more.System.Registry.RegLoadAppKeyW
def _define_RegSaveKeyExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PSTR,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),win32more.System.Registry.REG_SAVE_FORMAT, use_last_error=False)(("RegSaveKeyExA", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'lpFile'),(1, 'lpSecurityAttributes'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegSaveKeyExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PWSTR,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),win32more.System.Registry.REG_SAVE_FORMAT, use_last_error=False)(("RegSaveKeyExW", windll["ADVAPI32"]), ((1, 'hKey'),(1, 'lpFile'),(1, 'lpSecurityAttributes'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegSaveKeyEx():
    return win32more.System.Registry.RegSaveKeyExW
def _define_GetRegistryValueWithFallbackW():
    try:
        return WINFUNCTYPE(win32more.Foundation.LSTATUS,win32more.System.Registry.HKEY,win32more.Foundation.PWSTR,win32more.System.Registry.HKEY,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32),c_void_p,UInt32,POINTER(UInt32), use_last_error=False)(("GetRegistryValueWithFallbackW", windll["api-ms-win-core-state-helpers-l1-1-0"]), ((1, 'hkeyPrimary'),(1, 'pwszPrimarySubKey'),(1, 'hkeyFallback'),(1, 'pwszFallbackSubKey'),(1, 'pwszValue'),(1, 'dwFlags'),(1, 'pdwType'),(1, 'pvData'),(1, 'cbDataIn'),(1, 'pcbDataOut'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "HKEY_CLASSES_ROOT",
    "HKEY_CURRENT_USER",
    "HKEY_LOCAL_MACHINE",
    "HKEY_USERS",
    "HKEY_PERFORMANCE_DATA",
    "HKEY_PERFORMANCE_TEXT",
    "HKEY_PERFORMANCE_NLSTEXT",
    "HKEY_CURRENT_CONFIG",
    "HKEY_DYN_DATA",
    "HKEY_CURRENT_USER_LOCAL_SETTINGS",
    "RRF_SUBKEY_WOW6464KEY",
    "RRF_SUBKEY_WOW6432KEY",
    "RRF_WOW64_MASK",
    "RRF_NOEXPAND",
    "RRF_ZEROONFAILURE",
    "REG_PROCESS_APPKEY",
    "REG_USE_CURRENT_SECURITY_CONTEXT",
    "PROVIDER_KEEPS_VALUE_LENGTH",
    "REG_MUI_STRING_TRUNCATE",
    "REG_SECURE_CONNECTION",
    "REGSTR_MAX_VALUE_LENGTH",
    "IT_COMPACT",
    "IT_TYPICAL",
    "IT_PORTABLE",
    "IT_CUSTOM",
    "DRIVERSIGN_NONE",
    "DRIVERSIGN_WARNING",
    "DRIVERSIGN_BLOCKING",
    "DOSOPTGF_DEFCLEAN",
    "DOSOPTF_DEFAULT",
    "DOSOPTF_SUPPORTED",
    "DOSOPTF_ALWAYSUSE",
    "DOSOPTF_USESPMODE",
    "DOSOPTF_PROVIDESUMB",
    "DOSOPTF_NEEDSETUP",
    "DOSOPTF_INDOSSTART",
    "DOSOPTF_MULTIPLE",
    "SUF_FIRSTTIME",
    "SUF_EXPRESS",
    "SUF_BATCHINF",
    "SUF_CLEAN",
    "SUF_INSETUP",
    "SUF_NETSETUP",
    "SUF_NETHDBOOT",
    "SUF_NETRPLBOOT",
    "SUF_SBSCOPYOK",
    "VPDF_DISABLEPWRMGMT",
    "VPDF_FORCEAPM10MODE",
    "VPDF_SKIPINTELSLCHECK",
    "VPDF_DISABLEPWRSTATUSPOLL",
    "VPDF_DISABLERINGRESUME",
    "VPDF_SHOWMULTIBATT",
    "BIF_SHOWSIMILARDRIVERS",
    "BIF_RAWDEVICENEEDSDRIVER",
    "PCMCIA_OPT_HAVE_SOCKET",
    "PCMCIA_OPT_AUTOMEM",
    "PCMCIA_OPT_NO_SOUND",
    "PCMCIA_OPT_NO_AUDIO",
    "PCMCIA_OPT_NO_APMREMOVE",
    "PCMCIA_DEF_MEMBEGIN",
    "PCMCIA_DEF_MEMEND",
    "PCMCIA_DEF_MEMLEN",
    "PCMCIA_DEF_MIN_REGION",
    "PCI_OPTIONS_USE_BIOS",
    "PCI_OPTIONS_USE_IRQ_STEERING",
    "AGP_FLAG_NO_1X_RATE",
    "AGP_FLAG_NO_2X_RATE",
    "AGP_FLAG_NO_4X_RATE",
    "AGP_FLAG_NO_8X_RATE",
    "AGP_FLAG_REVERSE_INITIALIZATION",
    "AGP_FLAG_NO_SBA_ENABLE",
    "AGP_FLAG_NO_FW_ENABLE",
    "AGP_FLAG_SPECIAL_TARGET",
    "AGP_FLAG_SPECIAL_RESERVE",
    "REGSTR_VAL_MAX_HCID_LEN",
    "REGDF_NOTDETIO",
    "REGDF_NOTDETMEM",
    "REGDF_NOTDETIRQ",
    "REGDF_NOTDETDMA",
    "REGDF_NEEDFULLCONFIG",
    "REGDF_GENFORCEDCONFIG",
    "REGDF_NODETCONFIG",
    "REGDF_CONFLICTIO",
    "REGDF_CONFLICTMEM",
    "REGDF_CONFLICTIRQ",
    "REGDF_CONFLICTDMA",
    "REGDF_MAPIRQ2TO9",
    "REGDF_NOTVERIFIED",
    "APMMENUSUSPEND_DISABLED",
    "APMMENUSUSPEND_ENABLED",
    "APMMENUSUSPEND_UNDOCKED",
    "APMMENUSUSPEND_NOCHANGE",
    "APMTIMEOUT_DISABLED",
    "CONFIGFLAG_DISABLED",
    "CONFIGFLAG_REMOVED",
    "CONFIGFLAG_MANUAL_INSTALL",
    "CONFIGFLAG_IGNORE_BOOT_LC",
    "CONFIGFLAG_NET_BOOT",
    "CONFIGFLAG_REINSTALL",
    "CONFIGFLAG_FAILEDINSTALL",
    "CONFIGFLAG_CANTSTOPACHILD",
    "CONFIGFLAG_OKREMOVEROM",
    "CONFIGFLAG_NOREMOVEEXIT",
    "CONFIGFLAG_FINISH_INSTALL",
    "CONFIGFLAG_NEEDS_FORCED_CONFIG",
    "CONFIGFLAG_NETBOOT_CARD",
    "CONFIGFLAG_PARTIAL_LOG_CONF",
    "CONFIGFLAG_SUPPRESS_SURPRISE",
    "CONFIGFLAG_VERIFY_HARDWARE",
    "CONFIGFLAG_FINISHINSTALL_UI",
    "CONFIGFLAG_FINISHINSTALL_ACTION",
    "CONFIGFLAG_BOOT_DEVICE",
    "CONFIGFLAG_NEEDS_CLASS_CONFIG",
    "CSCONFIGFLAG_BITS",
    "CSCONFIGFLAG_DISABLED",
    "CSCONFIGFLAG_DO_NOT_CREATE",
    "CSCONFIGFLAG_DO_NOT_START",
    "DMSTATEFLAG_APPLYTOALL",
    "NUM_RESOURCE_MAP",
    "MF_FLAGS_EVEN_IF_NO_RESOURCE",
    "MF_FLAGS_NO_CREATE_IF_NO_RESOURCE",
    "MF_FLAGS_FILL_IN_UNKNOWN_RESOURCE",
    "MF_FLAGS_CREATE_BUT_NO_SHOW_DISABLED",
    "EISAFLAG_NO_IO_MERGE",
    "EISAFLAG_SLOT_IO_FIRST",
    "EISA_NO_MAX_FUNCTION",
    "NUM_EISA_RANGES",
    "PCIC_DEFAULT_IRQMASK",
    "PCIC_DEFAULT_NUMSOCKETS",
    "DTRESULTOK",
    "DTRESULTFIX",
    "DTRESULTPROB",
    "DTRESULTPART",
    "PIR_OPTION_ENABLED",
    "PIR_OPTION_REGISTRY",
    "PIR_OPTION_MSSPEC",
    "PIR_OPTION_REALMODE",
    "PIR_OPTION_DEFAULT",
    "PIR_STATUS_ERROR",
    "PIR_STATUS_ENABLED",
    "PIR_STATUS_DISABLED",
    "PIR_STATUS_MAX",
    "PIR_STATUS_TABLE_REGISTRY",
    "PIR_STATUS_TABLE_MSSPEC",
    "PIR_STATUS_TABLE_REALMODE",
    "PIR_STATUS_TABLE_NONE",
    "PIR_STATUS_TABLE_ERROR",
    "PIR_STATUS_TABLE_BAD",
    "PIR_STATUS_TABLE_SUCCESS",
    "PIR_STATUS_TABLE_MAX",
    "PIR_STATUS_MINIPORT_NORMAL",
    "PIR_STATUS_MINIPORT_COMPATIBLE",
    "PIR_STATUS_MINIPORT_OVERRIDE",
    "PIR_STATUS_MINIPORT_NONE",
    "PIR_STATUS_MINIPORT_ERROR",
    "PIR_STATUS_MINIPORT_NOKEY",
    "PIR_STATUS_MINIPORT_SUCCESS",
    "PIR_STATUS_MINIPORT_INVALID",
    "PIR_STATUS_MINIPORT_MAX",
    "LASTGOOD_OPERATION",
    "LASTGOOD_OPERATION_NOPOSTPROC",
    "LASTGOOD_OPERATION_DELETE",
    "REG_VALUE_TYPE",
    "REG_NONE",
    "REG_SZ",
    "REG_EXPAND_SZ",
    "REG_BINARY",
    "REG_DWORD",
    "REG_DWORD_LITTLE_ENDIAN",
    "REG_DWORD_BIG_ENDIAN",
    "REG_LINK",
    "REG_MULTI_SZ",
    "REG_RESOURCE_LIST",
    "REG_FULL_RESOURCE_DESCRIPTOR",
    "REG_RESOURCE_REQUIREMENTS_LIST",
    "REG_QWORD",
    "REG_QWORD_LITTLE_ENDIAN",
    "REG_SAM_FLAGS",
    "KEY_QUERY_VALUE",
    "KEY_SET_VALUE",
    "KEY_CREATE_SUB_KEY",
    "KEY_ENUMERATE_SUB_KEYS",
    "KEY_NOTIFY",
    "KEY_CREATE_LINK",
    "KEY_WOW64_32KEY",
    "KEY_WOW64_64KEY",
    "KEY_WOW64_RES",
    "KEY_READ",
    "KEY_WRITE",
    "KEY_EXECUTE",
    "KEY_ALL_ACCESS",
    "REG_OPEN_CREATE_OPTIONS",
    "REG_OPTION_RESERVED",
    "REG_OPTION_NON_VOLATILE",
    "REG_OPTION_VOLATILE",
    "REG_OPTION_CREATE_LINK",
    "REG_OPTION_BACKUP_RESTORE",
    "REG_OPTION_OPEN_LINK",
    "REG_OPTION_DONT_VIRTUALIZE",
    "REG_CREATE_KEY_DISPOSITION",
    "REG_CREATED_NEW_KEY",
    "REG_OPENED_EXISTING_KEY",
    "REG_SAVE_FORMAT",
    "REG_STANDARD_FORMAT",
    "REG_LATEST_FORMAT",
    "REG_NO_COMPRESSION",
    "REG_RESTORE_KEY_FLAGS",
    "REG_FORCE_RESTORE",
    "REG_WHOLE_HIVE_VOLATILE",
    "REG_NOTIFY_FILTER",
    "REG_NOTIFY_CHANGE_NAME",
    "REG_NOTIFY_CHANGE_ATTRIBUTES",
    "REG_NOTIFY_CHANGE_LAST_SET",
    "REG_NOTIFY_CHANGE_SECURITY",
    "REG_NOTIFY_THREAD_AGNOSTIC",
    "RRF_RT",
    "RRF_RT_ANY",
    "RRF_RT_DWORD",
    "RRF_RT_QWORD",
    "RRF_RT_REG_BINARY",
    "RRF_RT_REG_DWORD",
    "RRF_RT_REG_EXPAND_SZ",
    "RRF_RT_REG_MULTI_SZ",
    "RRF_RT_REG_NONE",
    "RRF_RT_REG_QWORD",
    "RRF_RT_REG_SZ",
    "HKEY",
    "val_context",
    "pvalueA",
    "pvalueW",
    "PQUERYHANDLER",
    "provider_info",
    "VALENTA",
    "VALENTW",
    "DSKTLSYSTEMTIME",
    "RegCloseKey",
    "RegOverridePredefKey",
    "RegOpenUserClassesRoot",
    "RegOpenCurrentUser",
    "RegDisablePredefinedCache",
    "RegDisablePredefinedCacheEx",
    "RegConnectRegistryA",
    "RegConnectRegistryW",
    "RegConnectRegistry",
    "RegConnectRegistryExA",
    "RegConnectRegistryExW",
    "RegConnectRegistryEx",
    "RegCreateKeyA",
    "RegCreateKeyW",
    "RegCreateKey",
    "RegCreateKeyExA",
    "RegCreateKeyExW",
    "RegCreateKeyEx",
    "RegCreateKeyTransactedA",
    "RegCreateKeyTransactedW",
    "RegCreateKeyTransacted",
    "RegDeleteKeyA",
    "RegDeleteKeyW",
    "RegDeleteKey",
    "RegDeleteKeyExA",
    "RegDeleteKeyExW",
    "RegDeleteKeyEx",
    "RegDeleteKeyTransactedA",
    "RegDeleteKeyTransactedW",
    "RegDeleteKeyTransacted",
    "RegDisableReflectionKey",
    "RegEnableReflectionKey",
    "RegQueryReflectionKey",
    "RegDeleteValueA",
    "RegDeleteValueW",
    "RegDeleteValue",
    "RegEnumKeyA",
    "RegEnumKeyW",
    "RegEnumKey",
    "RegEnumKeyExA",
    "RegEnumKeyExW",
    "RegEnumKeyEx",
    "RegEnumValueA",
    "RegEnumValueW",
    "RegEnumValue",
    "RegFlushKey",
    "RegGetKeySecurity",
    "RegLoadKeyA",
    "RegLoadKeyW",
    "RegLoadKey",
    "RegNotifyChangeKeyValue",
    "RegOpenKeyA",
    "RegOpenKeyW",
    "RegOpenKey",
    "RegOpenKeyExA",
    "RegOpenKeyExW",
    "RegOpenKeyEx",
    "RegOpenKeyTransactedA",
    "RegOpenKeyTransactedW",
    "RegOpenKeyTransacted",
    "RegQueryInfoKeyA",
    "RegQueryInfoKeyW",
    "RegQueryInfoKey",
    "RegQueryValueA",
    "RegQueryValueW",
    "RegQueryValue",
    "RegQueryMultipleValuesA",
    "RegQueryMultipleValuesW",
    "RegQueryMultipleValues",
    "RegQueryValueExA",
    "RegQueryValueExW",
    "RegQueryValueEx",
    "RegReplaceKeyA",
    "RegReplaceKeyW",
    "RegReplaceKey",
    "RegRestoreKeyA",
    "RegRestoreKeyW",
    "RegRestoreKey",
    "RegRenameKey",
    "RegSaveKeyA",
    "RegSaveKeyW",
    "RegSaveKey",
    "RegSetKeySecurity",
    "RegSetValueA",
    "RegSetValueW",
    "RegSetValue",
    "RegSetValueExA",
    "RegSetValueExW",
    "RegSetValueEx",
    "RegUnLoadKeyA",
    "RegUnLoadKeyW",
    "RegUnLoadKey",
    "RegDeleteKeyValueA",
    "RegDeleteKeyValueW",
    "RegDeleteKeyValue",
    "RegSetKeyValueA",
    "RegSetKeyValueW",
    "RegSetKeyValue",
    "RegDeleteTreeA",
    "RegDeleteTreeW",
    "RegDeleteTree",
    "RegCopyTreeA",
    "RegGetValueA",
    "RegGetValueW",
    "RegGetValue",
    "RegCopyTreeW",
    "RegCopyTree",
    "RegLoadMUIStringA",
    "RegLoadMUIStringW",
    "RegLoadMUIString",
    "RegLoadAppKeyA",
    "RegLoadAppKeyW",
    "RegLoadAppKey",
    "RegSaveKeyExA",
    "RegSaveKeyExW",
    "RegSaveKeyEx",
    "GetRegistryValueWithFallbackW",
]
