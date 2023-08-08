from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Security.WinTrust
import win32more.Windows.Win32.Storage.FileSystem
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Com.StructuredStorage
import win32more.Windows.Win32.System.Diagnostics.Debug
import win32more.Windows.Win32.System.Kernel
import win32more.Windows.Win32.System.Memory
import win32more.Windows.Win32.System.Ole
import win32more.Windows.Win32.System.SystemInformation
import win32more.Windows.Win32.System.Threading
import win32more.Windows.Win32.System.Time
import win32more.Windows.Win32.System.Variant
import win32more.Windows.Win32.UI.WindowsAndMessaging
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
if ARCH in 'X86':
    class ADDRESS(EasyCastStructure):
        Offset: UInt32
        Segment: UInt16
        Mode: win32more.Windows.Win32.System.Diagnostics.Debug.ADDRESS_MODE
class ADDRESS64(EasyCastStructure):
    Offset: UInt64
    Segment: UInt16
    Mode: win32more.Windows.Win32.System.Diagnostics.Debug.ADDRESS_MODE
ADDRESS_MODE = Int32
ADDRESS_MODE_AddrMode1616: ADDRESS_MODE = 0
ADDRESS_MODE_AddrMode1632: ADDRESS_MODE = 1
ADDRESS_MODE_AddrModeReal: ADDRESS_MODE = 2
ADDRESS_MODE_AddrModeFlat: ADDRESS_MODE = 3
class AER_BRIDGE_DESCRIPTOR_FLAGS(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUSHORT: UInt16
    _pack_ = 1
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt16
        _pack_ = 1
class AER_ENDPOINT_DESCRIPTOR_FLAGS(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUSHORT: UInt16
    _pack_ = 1
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt16
        _pack_ = 1
class AER_ROOTPORT_DESCRIPTOR_FLAGS(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUSHORT: UInt16
    _pack_ = 1
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt16
        _pack_ = 1
class APC_CALLBACK_DATA(EasyCastStructure):
    Parameter: UIntPtr
    ContextRecord: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_head)
    Reserved0: UIntPtr
    Reserved1: UIntPtr
class API_VERSION(EasyCastStructure):
    MajorVersion: UInt16
    MinorVersion: UInt16
    Revision: UInt16
    Reserved: UInt16
if ARCH in 'X86,X64':
    class ARM64_NT_CONTEXT(EasyCastStructure):
        ContextFlags: UInt32
        Cpsr: UInt32
        Anonymous: _Anonymous_e__Union
        Sp: UInt64
        Pc: UInt64
        V: win32more.Windows.Win32.System.Diagnostics.Debug.ARM64_NT_NEON128 * 32
        Fpcr: UInt32
        Fpsr: UInt32
        Bcr: UInt32 * 8
        Bvr: UInt64 * 8
        Wcr: UInt32 * 2
        Wvr: UInt64 * 2
        class _Anonymous_e__Union(EasyCastUnion):
            Anonymous: _Anonymous_e__Struct
            X: UInt64 * 31
            class _Anonymous_e__Struct(EasyCastStructure):
                X0: UInt64
                X1: UInt64
                X2: UInt64
                X3: UInt64
                X4: UInt64
                X5: UInt64
                X6: UInt64
                X7: UInt64
                X8: UInt64
                X9: UInt64
                X10: UInt64
                X11: UInt64
                X12: UInt64
                X13: UInt64
                X14: UInt64
                X15: UInt64
                X16: UInt64
                X17: UInt64
                X18: UInt64
                X19: UInt64
                X20: UInt64
                X21: UInt64
                X22: UInt64
                X23: UInt64
                X24: UInt64
                X25: UInt64
                X26: UInt64
                X27: UInt64
                X28: UInt64
                Fp: UInt64
                Lr: UInt64
class ARM64_NT_NEON128(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    D: Double * 2
    S: Single * 4
    H: UInt16 * 8
    B: Byte * 16
    class _Anonymous_e__Struct(EasyCastStructure):
        Low: UInt64
        High: Int64
WOW64_SIZE_OF_80387_REGISTERS: UInt32 = 80
WOW64_MAXIMUM_SUPPORTED_EXTENSION: UInt32 = 512
RESTORE_LAST_ERROR_NAME_A: String = 'RestoreLastError'
RESTORE_LAST_ERROR_NAME_W: String = 'RestoreLastError'
RESTORE_LAST_ERROR_NAME: String = 'RestoreLastError'
MAX_SYM_NAME: UInt32 = 2000
BIND_NO_BOUND_IMPORTS: UInt32 = 1
BIND_NO_UPDATE: UInt32 = 2
BIND_ALL_IMAGES: UInt32 = 4
BIND_CACHE_IMPORT_DLLS: UInt32 = 8
BIND_REPORT_64BIT_VA: UInt32 = 16
CHECKSUM_SUCCESS: UInt32 = 0
CHECKSUM_OPEN_FAILURE: UInt32 = 1
CHECKSUM_MAP_FAILURE: UInt32 = 2
CHECKSUM_MAPVIEW_FAILURE: UInt32 = 3
CHECKSUM_UNICODE_FAILURE: UInt32 = 4
SPLITSYM_REMOVE_PRIVATE: UInt32 = 1
SPLITSYM_EXTRACT_ALL: UInt32 = 2
SPLITSYM_SYMBOLPATH_IS_SRC: UInt32 = 4
CERT_PE_IMAGE_DIGEST_DEBUG_INFO: UInt32 = 1
CERT_PE_IMAGE_DIGEST_RESOURCES: UInt32 = 2
CERT_PE_IMAGE_DIGEST_ALL_IMPORT_INFO: UInt32 = 4
CERT_PE_IMAGE_DIGEST_NON_PE_INFO: UInt32 = 8
CERT_SECTION_TYPE_ANY: UInt32 = 255
ERROR_IMAGE_NOT_STRIPPED: UInt32 = 34816
ERROR_NO_DBG_POINTER: UInt32 = 34817
ERROR_NO_PDB_POINTER: UInt32 = 34818
UNDNAME_COMPLETE: UInt32 = 0
UNDNAME_NO_LEADING_UNDERSCORES: UInt32 = 1
UNDNAME_NO_MS_KEYWORDS: UInt32 = 2
UNDNAME_NO_FUNCTION_RETURNS: UInt32 = 4
UNDNAME_NO_ALLOCATION_MODEL: UInt32 = 8
UNDNAME_NO_ALLOCATION_LANGUAGE: UInt32 = 16
UNDNAME_NO_MS_THISTYPE: UInt32 = 32
UNDNAME_NO_CV_THISTYPE: UInt32 = 64
UNDNAME_NO_THISTYPE: UInt32 = 96
UNDNAME_NO_ACCESS_SPECIFIERS: UInt32 = 128
UNDNAME_NO_THROW_SIGNATURES: UInt32 = 256
UNDNAME_NO_MEMBER_TYPE: UInt32 = 512
UNDNAME_NO_RETURN_UDT_MODEL: UInt32 = 1024
UNDNAME_32_BIT_DECODE: UInt32 = 2048
UNDNAME_NAME_ONLY: UInt32 = 4096
UNDNAME_NO_ARGUMENTS: UInt32 = 8192
UNDNAME_NO_SPECIAL_SYMS: UInt32 = 16384
DBHHEADER_PDBGUID: UInt32 = 3
INLINE_FRAME_CONTEXT_INIT: UInt32 = 0
INLINE_FRAME_CONTEXT_IGNORE: UInt32 = 4294967295
TARGET_ATTRIBUTE_PACMASK: UInt32 = 1
SYM_STKWALK_DEFAULT: UInt32 = 0
SYM_STKWALK_FORCE_FRAMEPTR: UInt32 = 1
SYM_STKWALK_ZEROEXTEND_PTRS: UInt32 = 2
API_VERSION_NUMBER: UInt32 = 12
SYMFLAG_NULL: UInt32 = 524288
SYMFLAG_FUNC_NO_RETURN: UInt32 = 1048576
SYMFLAG_SYNTHETIC_ZEROBASE: UInt32 = 2097152
SYMFLAG_PUBLIC_CODE: UInt32 = 4194304
SYMFLAG_REGREL_ALIASINDIR: UInt32 = 8388608
SYMFLAG_FIXUP_ARM64X: UInt32 = 16777216
SYMFLAG_GLOBAL: UInt32 = 33554432
SYMFLAG_RESET: UInt32 = 2147483648
IMAGEHLP_MODULE_REGION_DLLBASE: UInt32 = 1
IMAGEHLP_MODULE_REGION_DLLRANGE: UInt32 = 2
IMAGEHLP_MODULE_REGION_ADDITIONAL: UInt32 = 4
IMAGEHLP_MODULE_REGION_JIT: UInt32 = 8
IMAGEHLP_MODULE_REGION_ALL: UInt32 = 255
CBA_DEFERRED_SYMBOL_LOAD_START: UInt32 = 1
CBA_DEFERRED_SYMBOL_LOAD_COMPLETE: UInt32 = 2
CBA_DEFERRED_SYMBOL_LOAD_FAILURE: UInt32 = 3
CBA_SYMBOLS_UNLOADED: UInt32 = 4
CBA_DUPLICATE_SYMBOL: UInt32 = 5
CBA_READ_MEMORY: UInt32 = 6
CBA_DEFERRED_SYMBOL_LOAD_CANCEL: UInt32 = 7
CBA_SET_OPTIONS: UInt32 = 8
CBA_EVENT: UInt32 = 16
CBA_DEFERRED_SYMBOL_LOAD_PARTIAL: UInt32 = 32
CBA_DEBUG_INFO: UInt32 = 268435456
CBA_SRCSRV_INFO: UInt32 = 536870912
CBA_SRCSRV_EVENT: UInt32 = 1073741824
CBA_UPDATE_STATUS_BAR: UInt32 = 1342177280
CBA_ENGINE_PRESENT: UInt32 = 1610612736
CBA_CHECK_ENGOPT_DISALLOW_NETWORK_PATHS: UInt32 = 1879048192
CBA_CHECK_ARM_MACHINE_THUMB_TYPE_OVERRIDE: UInt32 = 2147483648
CBA_XML_LOG: UInt32 = 2415919104
CBA_MAP_JIT_SYMBOL: UInt32 = 2684354560
EVENT_SRCSPEW_START: UInt32 = 100
EVENT_SRCSPEW: UInt32 = 100
EVENT_SRCSPEW_END: UInt32 = 199
DSLFLAG_MISMATCHED_PDB: UInt32 = 1
DSLFLAG_MISMATCHED_DBG: UInt32 = 2
FLAG_ENGINE_PRESENT: UInt32 = 4
FLAG_ENGOPT_DISALLOW_NETWORK_PATHS: UInt32 = 8
FLAG_OVERRIDE_ARM_MACHINE_TYPE: UInt32 = 16
SYMOPT_CASE_INSENSITIVE: UInt32 = 1
SYMOPT_UNDNAME: UInt32 = 2
SYMOPT_DEFERRED_LOADS: UInt32 = 4
SYMOPT_NO_CPP: UInt32 = 8
SYMOPT_LOAD_LINES: UInt32 = 16
SYMOPT_OMAP_FIND_NEAREST: UInt32 = 32
SYMOPT_LOAD_ANYTHING: UInt32 = 64
SYMOPT_IGNORE_CVREC: UInt32 = 128
SYMOPT_NO_UNQUALIFIED_LOADS: UInt32 = 256
SYMOPT_FAIL_CRITICAL_ERRORS: UInt32 = 512
SYMOPT_EXACT_SYMBOLS: UInt32 = 1024
SYMOPT_ALLOW_ABSOLUTE_SYMBOLS: UInt32 = 2048
SYMOPT_IGNORE_NT_SYMPATH: UInt32 = 4096
SYMOPT_INCLUDE_32BIT_MODULES: UInt32 = 8192
SYMOPT_PUBLICS_ONLY: UInt32 = 16384
SYMOPT_NO_PUBLICS: UInt32 = 32768
SYMOPT_AUTO_PUBLICS: UInt32 = 65536
SYMOPT_NO_IMAGE_SEARCH: UInt32 = 131072
SYMOPT_SECURE: UInt32 = 262144
SYMOPT_NO_PROMPTS: UInt32 = 524288
SYMOPT_OVERWRITE: UInt32 = 1048576
SYMOPT_IGNORE_IMAGEDIR: UInt32 = 2097152
SYMOPT_FLAT_DIRECTORY: UInt32 = 4194304
SYMOPT_FAVOR_COMPRESSED: UInt32 = 8388608
SYMOPT_ALLOW_ZERO_ADDRESS: UInt32 = 16777216
SYMOPT_DISABLE_SYMSRV_AUTODETECT: UInt32 = 33554432
SYMOPT_READONLY_CACHE: UInt32 = 67108864
SYMOPT_SYMPATH_LAST: UInt32 = 134217728
SYMOPT_DISABLE_FAST_SYMBOLS: UInt32 = 268435456
SYMOPT_DISABLE_SYMSRV_TIMEOUT: UInt32 = 536870912
SYMOPT_DISABLE_SRVSTAR_ON_STARTUP: UInt32 = 1073741824
SYMOPT_DEBUG: UInt32 = 2147483648
SYM_INLINE_COMP_ERROR: UInt32 = 0
SYM_INLINE_COMP_IDENTICAL: UInt32 = 1
SYM_INLINE_COMP_STEPIN: UInt32 = 2
SYM_INLINE_COMP_STEPOUT: UInt32 = 3
SYM_INLINE_COMP_STEPOVER: UInt32 = 4
SYM_INLINE_COMP_DIFFERENT: UInt32 = 5
ESLFLAG_FULLPATH: UInt32 = 1
ESLFLAG_NEAREST: UInt32 = 2
ESLFLAG_PREV: UInt32 = 4
ESLFLAG_NEXT: UInt32 = 8
ESLFLAG_INLINE_SITE: UInt32 = 16
SYMENUM_OPTIONS_DEFAULT: UInt32 = 1
SYMENUM_OPTIONS_INLINE: UInt32 = 2
SYMSEARCH_MASKOBJS: UInt32 = 1
SYMSEARCH_RECURSE: UInt32 = 2
SYMSEARCH_GLOBALSONLY: UInt32 = 4
SYMSEARCH_ALLITEMS: UInt32 = 8
EXT_OUTPUT_VER: UInt32 = 1
SYMSRV_VERSION: UInt32 = 2
SSRVOPT_CALLBACK: UInt32 = 1
SSRVOPT_OLDGUIDPTR: UInt32 = 16
SSRVOPT_UNATTENDED: UInt32 = 32
SSRVOPT_NOCOPY: UInt32 = 64
SSRVOPT_GETPATH: UInt32 = 64
SSRVOPT_PARENTWIN: UInt32 = 128
SSRVOPT_PARAMTYPE: UInt32 = 256
SSRVOPT_SECURE: UInt32 = 512
SSRVOPT_TRACE: UInt32 = 1024
SSRVOPT_SETCONTEXT: UInt32 = 2048
SSRVOPT_PROXY: UInt32 = 4096
SSRVOPT_DOWNSTREAM_STORE: UInt32 = 8192
SSRVOPT_OVERWRITE: UInt32 = 16384
SSRVOPT_RESETTOU: UInt32 = 32768
SSRVOPT_CALLBACKW: UInt32 = 65536
SSRVOPT_FLAT_DEFAULT_STORE: UInt32 = 131072
SSRVOPT_PROXYW: UInt32 = 262144
SSRVOPT_MESSAGE: UInt32 = 524288
SSRVOPT_SERVICE: UInt32 = 1048576
SSRVOPT_FAVOR_COMPRESSED: UInt32 = 2097152
SSRVOPT_STRING: UInt32 = 4194304
SSRVOPT_WINHTTP: UInt32 = 8388608
SSRVOPT_WININET: UInt32 = 16777216
SSRVOPT_DONT_UNCOMPRESS: UInt32 = 33554432
SSRVOPT_DISABLE_PING_HOST: UInt32 = 67108864
SSRVOPT_DISABLE_TIMEOUT: UInt32 = 134217728
SSRVOPT_ENABLE_COMM_MSG: UInt32 = 268435456
SSRVOPT_URI_FILTER: UInt32 = 536870912
SSRVOPT_URI_TIERS: UInt32 = 1073741824
SSRVOPT_RETRY_APP_HANG: UInt32 = 2147483648
SSRVOPT_MAX: UInt32 = 2147483648
NUM_SSRVOPTS: UInt32 = 32
SSRVURI_HTTP_NORMAL: UInt32 = 1
SSRVURI_HTTP_COMPRESSED: UInt32 = 2
SSRVURI_HTTP_FILEPTR: UInt32 = 4
SSRVURI_UNC_NORMAL: UInt32 = 16
SSRVURI_UNC_COMPRESSED: UInt32 = 32
SSRVURI_UNC_FILEPTR: UInt32 = 64
SSRVURI_HTTP_MASK: UInt32 = 15
SSRVURI_UNC_MASK: UInt32 = 240
SSRVURI_ALL: UInt32 = 255
SSRVURI_NORMAL: UInt32 = 1
SSRVURI_COMPRESSED: UInt32 = 2
SSRVURI_FILEPTR: UInt32 = 4
SSRVACTION_TRACE: UInt32 = 1
SSRVACTION_QUERYCANCEL: UInt32 = 2
SSRVACTION_EVENT: UInt32 = 3
SSRVACTION_EVENTW: UInt32 = 4
SSRVACTION_SIZE: UInt32 = 5
SSRVACTION_HTTPSTATUS: UInt32 = 6
SSRVACTION_XMLOUTPUT: UInt32 = 7
SSRVACTION_CHECKSUMSTATUS: UInt32 = 8
SYMSTOREOPT_ALT_INDEX: UInt32 = 16
SYMSTOREOPT_UNICODE: UInt32 = 32
SYMF_OMAP_GENERATED: UInt32 = 1
SYMF_OMAP_MODIFIED: UInt32 = 2
SYMF_REGISTER: UInt32 = 8
SYMF_REGREL: UInt32 = 16
SYMF_FRAMEREL: UInt32 = 32
SYMF_PARAMETER: UInt32 = 64
SYMF_LOCAL: UInt32 = 128
SYMF_CONSTANT: UInt32 = 256
SYMF_EXPORT: UInt32 = 512
SYMF_FORWARDER: UInt32 = 1024
SYMF_FUNCTION: UInt32 = 2048
SYMF_VIRTUAL: UInt32 = 4096
SYMF_THUNK: UInt32 = 8192
SYMF_TLSREL: UInt32 = 16384
IMAGEHLP_SYMBOL_INFO_VALUEPRESENT: UInt32 = 1
IMAGEHLP_SYMBOL_INFO_REGISTER: UInt32 = 8
IMAGEHLP_SYMBOL_INFO_REGRELATIVE: UInt32 = 16
IMAGEHLP_SYMBOL_INFO_FRAMERELATIVE: UInt32 = 32
IMAGEHLP_SYMBOL_INFO_PARAMETER: UInt32 = 64
IMAGEHLP_SYMBOL_INFO_LOCAL: UInt32 = 128
IMAGEHLP_SYMBOL_INFO_CONSTANT: UInt32 = 256
IMAGEHLP_SYMBOL_FUNCTION: UInt32 = 2048
IMAGEHLP_SYMBOL_VIRTUAL: UInt32 = 4096
IMAGEHLP_SYMBOL_THUNK: UInt32 = 8192
IMAGEHLP_SYMBOL_INFO_TLSRELATIVE: UInt32 = 16384
IMAGEHLP_RMAP_MAPPED_FLAT: UInt32 = 1
IMAGEHLP_RMAP_BIG_ENDIAN: UInt32 = 2
IMAGEHLP_RMAP_IGNORE_MISCOMPARE: UInt32 = 4
IMAGEHLP_RMAP_FIXUP_ARM64X: UInt32 = 268435456
IMAGEHLP_RMAP_LOAD_RW_DATA_SECTIONS: UInt32 = 536870912
IMAGEHLP_RMAP_OMIT_SHARED_RW_DATA_SECTIONS: UInt32 = 1073741824
IMAGEHLP_RMAP_FIXUP_IMAGEBASE: UInt32 = 2147483648
DMP_PHYSICAL_MEMORY_BLOCK_SIZE_32: UInt32 = 700
DMP_CONTEXT_RECORD_SIZE_32: UInt32 = 1200
DMP_RESERVED_0_SIZE_32: UInt32 = 1760
DMP_RESERVED_2_SIZE_32: UInt32 = 16
DMP_RESERVED_3_SIZE_32: UInt32 = 56
DMP_PHYSICAL_MEMORY_BLOCK_SIZE_64: UInt32 = 700
DMP_CONTEXT_RECORD_SIZE_64: UInt32 = 3000
DMP_RESERVED_0_SIZE_64: UInt32 = 4008
DMP_HEADER_COMMENT_SIZE: UInt32 = 128
DUMP_SUMMARY_VALID_KERNEL_VA: UInt32 = 1
DUMP_SUMMARY_VALID_CURRENT_USER_VA: UInt32 = 2
MINIDUMP_VERSION: UInt32 = 42899
MINIDUMP_MISC1_PROCESSOR_POWER_INFO: UInt32 = 4
MINIDUMP_MISC3_PROCESS_INTEGRITY: UInt32 = 16
MINIDUMP_MISC3_PROCESS_EXECUTE_FLAGS: UInt32 = 32
MINIDUMP_MISC3_TIMEZONE: UInt32 = 64
MINIDUMP_MISC3_PROTECTED_PROCESS: UInt32 = 128
MINIDUMP_MISC4_BUILDSTRING: UInt32 = 256
MINIDUMP_MISC5_PROCESS_COOKIE: UInt32 = 512
MINIDUMP_SYSMEMINFO1_FILECACHE_TRANSITIONREPURPOSECOUNT_FLAGS: UInt32 = 1
MINIDUMP_SYSMEMINFO1_BASICPERF: UInt32 = 2
MINIDUMP_SYSMEMINFO1_PERF_CCTOTALDIRTYPAGES_CCDIRTYPAGETHRESHOLD: UInt32 = 4
MINIDUMP_SYSMEMINFO1_PERF_RESIDENTAVAILABLEPAGES_SHAREDCOMMITPAGES: UInt32 = 8
MINIDUMP_PROCESS_VM_COUNTERS: UInt32 = 1
MINIDUMP_PROCESS_VM_COUNTERS_VIRTUALSIZE: UInt32 = 2
MINIDUMP_PROCESS_VM_COUNTERS_EX: UInt32 = 4
MINIDUMP_PROCESS_VM_COUNTERS_EX2: UInt32 = 8
MINIDUMP_PROCESS_VM_COUNTERS_JOB: UInt32 = 16
INTERFACESAFE_FOR_UNTRUSTED_CALLER: UInt32 = 1
INTERFACESAFE_FOR_UNTRUSTED_DATA: UInt32 = 2
INTERFACE_USES_DISPEX: UInt32 = 4
INTERFACE_USES_SECURITY_MANAGER: UInt32 = 8
WCT_MAX_NODE_COUNT: UInt32 = 16
WCT_OBJNAME_LENGTH: UInt32 = 128
WCT_NETWORK_IO_FLAG: UInt32 = 8
WHEA_ERROR_SOURCE_DESCRIPTOR_VERSION_10: UInt32 = 10
WHEA_ERROR_SOURCE_DESCRIPTOR_VERSION_11: UInt32 = 11
WHEA_MAX_MC_BANKS: UInt32 = 32
WHEA_ERROR_SOURCE_FLAG_FIRMWAREFIRST: UInt32 = 1
WHEA_ERROR_SOURCE_FLAG_GLOBAL: UInt32 = 2
WHEA_ERROR_SOURCE_FLAG_GHES_ASSIST: UInt32 = 4
WHEA_ERROR_SOURCE_FLAG_DEFAULTSOURCE: UInt32 = 2147483648
WHEA_ERROR_SOURCE_INVALID_RELATED_SOURCE: UInt32 = 65535
WHEA_ERROR_SOURCE_DESCRIPTOR_TYPE_XPFMCE: UInt32 = 0
WHEA_ERROR_SOURCE_DESCRIPTOR_TYPE_XPFCMC: UInt32 = 1
WHEA_ERROR_SOURCE_DESCRIPTOR_TYPE_XPFNMI: UInt32 = 2
WHEA_ERROR_SOURCE_DESCRIPTOR_TYPE_IPFMCA: UInt32 = 3
WHEA_ERROR_SOURCE_DESCRIPTOR_TYPE_IPFCMC: UInt32 = 4
WHEA_ERROR_SOURCE_DESCRIPTOR_TYPE_IPFCPE: UInt32 = 5
WHEA_ERROR_SOURCE_DESCRIPTOR_TYPE_AERROOTPORT: UInt32 = 6
WHEA_ERROR_SOURCE_DESCRIPTOR_TYPE_AERENDPOINT: UInt32 = 7
WHEA_ERROR_SOURCE_DESCRIPTOR_TYPE_AERBRIDGE: UInt32 = 8
WHEA_ERROR_SOURCE_DESCRIPTOR_TYPE_GENERIC: UInt32 = 9
WHEA_ERROR_SOURCE_DESCRIPTOR_TYPE_GENERIC_V2: UInt32 = 10
WHEA_XPF_MC_BANK_STATUSFORMAT_IA32MCA: UInt32 = 0
WHEA_XPF_MC_BANK_STATUSFORMAT_Intel64MCA: UInt32 = 1
WHEA_XPF_MC_BANK_STATUSFORMAT_AMD64MCA: UInt32 = 2
WHEA_NOTIFICATION_TYPE_POLLED: UInt32 = 0
WHEA_NOTIFICATION_TYPE_EXTERNALINTERRUPT: UInt32 = 1
WHEA_NOTIFICATION_TYPE_LOCALINTERRUPT: UInt32 = 2
WHEA_NOTIFICATION_TYPE_SCI: UInt32 = 3
WHEA_NOTIFICATION_TYPE_NMI: UInt32 = 4
WHEA_NOTIFICATION_TYPE_CMCI: UInt32 = 5
WHEA_NOTIFICATION_TYPE_MCE: UInt32 = 6
WHEA_NOTIFICATION_TYPE_GPIO_SIGNAL: UInt32 = 7
WHEA_NOTIFICATION_TYPE_ARMV8_SEA: UInt32 = 8
WHEA_NOTIFICATION_TYPE_ARMV8_SEI: UInt32 = 9
WHEA_NOTIFICATION_TYPE_EXTERNALINTERRUPT_GSIV: UInt32 = 10
WHEA_NOTIFICATION_TYPE_SDEI: UInt32 = 11
WHEA_DEVICE_DRIVER_CONFIG_V1: UInt32 = 1
WHEA_DEVICE_DRIVER_CONFIG_V2: UInt32 = 2
WHEA_DEVICE_DRIVER_CONFIG_MIN: UInt32 = 1
WHEA_DEVICE_DRIVER_CONFIG_MAX: UInt32 = 2
WHEA_DEVICE_DRIVER_BUFFER_SET_V1: UInt32 = 1
WHEA_DEVICE_DRIVER_BUFFER_SET_MIN: UInt32 = 1
WHEA_DEVICE_DRIVER_BUFFER_SET_MAX: UInt32 = 1
WHEA_DISABLE_OFFLINE: UInt32 = 0
WHEA_MEM_PERSISTOFFLINE: UInt32 = 1
WHEA_MEM_PFA_DISABLE: UInt32 = 2
WHEA_MEM_PFA_PAGECOUNT: UInt32 = 3
WHEA_MEM_PFA_THRESHOLD: UInt32 = 4
WHEA_MEM_PFA_TIMEOUT: UInt32 = 5
WHEA_DISABLE_DUMMY_WRITE: UInt32 = 6
WHEA_RESTORE_CMCI_ENABLED: UInt32 = 7
WHEA_RESTORE_CMCI_ATTEMPTS: UInt32 = 8
WHEA_RESTORE_CMCI_ERR_LIMIT: UInt32 = 9
WHEA_CMCI_THRESHOLD_COUNT: UInt32 = 10
WHEA_CMCI_THRESHOLD_TIME: UInt32 = 11
WHEA_CMCI_THRESHOLD_POLL_COUNT: UInt32 = 12
WHEA_PENDING_PAGE_LIST_SZ: UInt32 = 13
WHEA_BAD_PAGE_LIST_MAX_SIZE: UInt32 = 14
WHEA_BAD_PAGE_LIST_LOCATION: UInt32 = 15
WHEA_NOTIFY_ALL_OFFLINES: UInt32 = 16
WHEA_ROW_FAIL_CHECK_EXTENT: UInt32 = 17
WHEA_ROW_FAIL_CHECK_ENABLE: UInt32 = 18
WHEA_ROW_FAIL_CHECK_THRESHOLD: UInt32 = 19
IPMI_OS_SEL_RECORD_VERSION_1: UInt32 = 1
IPMI_OS_SEL_RECORD_VERSION: UInt32 = 1
IPMI_IOCTL_INDEX: UInt32 = 1024
IOCTL_IPMI_INTERNAL_RECORD_SEL_EVENT: UInt32 = 2232320
IPMI_OS_SEL_RECORD_MASK: UInt32 = 65535
sevMax: Int32 = 4
if ARCH in 'ARM64':
    @winfunctype('KERNEL32.dll')
    def RtlAddFunctionTable(FunctionTable: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_ARM64_RUNTIME_FUNCTION_ENTRY_head), EntryCount: UInt32, BaseAddress: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
if ARCH in 'ARM64':
    @winfunctype('KERNEL32.dll')
    def RtlDeleteFunctionTable(FunctionTable: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_ARM64_RUNTIME_FUNCTION_ENTRY_head)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
if ARCH in 'ARM64':
    @winfunctype('KERNEL32.dll')
    def RtlInstallFunctionTableCallback(TableIdentifier: UInt64, BaseAddress: UInt64, Length: UInt32, Callback: win32more.Windows.Win32.System.Diagnostics.Debug.PGET_RUNTIME_FUNCTION_CALLBACK, Context: VoidPtr, OutOfProcessCallbackDll: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
if ARCH in 'ARM64':
    @winfunctype('ntdll.dll')
    def RtlAddGrowableFunctionTable(DynamicTable: POINTER(VoidPtr), FunctionTable: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_ARM64_RUNTIME_FUNCTION_ENTRY_head), EntryCount: UInt32, MaximumEntryCount: UInt32, RangeBase: UIntPtr, RangeEnd: UIntPtr) -> UInt32: ...
if ARCH in 'ARM64':
    @winfunctype('KERNEL32.dll')
    def RtlLookupFunctionEntry(ControlPc: UIntPtr, ImageBase: POINTER(UIntPtr), HistoryTable: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.UNWIND_HISTORY_TABLE_head)) -> POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_ARM64_RUNTIME_FUNCTION_ENTRY_head): ...
if ARCH in 'ARM64':
    @winfunctype('KERNEL32.dll')
    def RtlVirtualUnwind(HandlerType: win32more.Windows.Win32.System.Diagnostics.Debug.RTL_VIRTUAL_UNWIND_HANDLER_TYPE, ImageBase: UIntPtr, ControlPc: UIntPtr, FunctionEntry: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_ARM64_RUNTIME_FUNCTION_ENTRY_head), ContextRecord: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_head), HandlerData: POINTER(VoidPtr), EstablisherFrame: POINTER(UIntPtr), ContextPointers: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.KNONVOLATILE_CONTEXT_POINTERS_ARM64_head)) -> win32more.Windows.Win32.System.Kernel.EXCEPTION_ROUTINE: ...
@winfunctype('KERNEL32.dll')
def ReadProcessMemory(hProcess: win32more.Windows.Win32.Foundation.HANDLE, lpBaseAddress: VoidPtr, lpBuffer: VoidPtr, nSize: UIntPtr, lpNumberOfBytesRead: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WriteProcessMemory(hProcess: win32more.Windows.Win32.Foundation.HANDLE, lpBaseAddress: VoidPtr, lpBuffer: VoidPtr, nSize: UIntPtr, lpNumberOfBytesWritten: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetThreadContext(hThread: win32more.Windows.Win32.Foundation.HANDLE, lpContext: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetThreadContext(hThread: win32more.Windows.Win32.Foundation.HANDLE, lpContext: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FlushInstructionCache(hProcess: win32more.Windows.Win32.Foundation.HANDLE, lpBaseAddress: VoidPtr, dwSize: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def Wow64GetThreadContext(hThread: win32more.Windows.Win32.Foundation.HANDLE, lpContext: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.WOW64_CONTEXT_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def Wow64SetThreadContext(hThread: win32more.Windows.Win32.Foundation.HANDLE, lpContext: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.WOW64_CONTEXT_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X64':
    @winfunctype('KERNEL32.dll')
    def RtlCaptureContext2(ContextRecord: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_head)) -> Void: ...
if ARCH in 'X64':
    @winfunctype('KERNEL32.dll')
    def RtlAddFunctionTable(FunctionTable: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_RUNTIME_FUNCTION_ENTRY_head), EntryCount: UInt32, BaseAddress: UInt64) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
if ARCH in 'X64':
    @winfunctype('KERNEL32.dll')
    def RtlDeleteFunctionTable(FunctionTable: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_RUNTIME_FUNCTION_ENTRY_head)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
if ARCH in 'X64':
    @winfunctype('KERNEL32.dll')
    def RtlInstallFunctionTableCallback(TableIdentifier: UInt64, BaseAddress: UInt64, Length: UInt32, Callback: win32more.Windows.Win32.System.Diagnostics.Debug.PGET_RUNTIME_FUNCTION_CALLBACK, Context: VoidPtr, OutOfProcessCallbackDll: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
if ARCH in 'X64':
    @winfunctype('ntdll.dll')
    def RtlAddGrowableFunctionTable(DynamicTable: POINTER(VoidPtr), FunctionTable: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_RUNTIME_FUNCTION_ENTRY_head), EntryCount: UInt32, MaximumEntryCount: UInt32, RangeBase: UIntPtr, RangeEnd: UIntPtr) -> UInt32: ...
if ARCH in 'X64,ARM64':
    @winfunctype('ntdll.dll')
    def RtlGrowFunctionTable(DynamicTable: VoidPtr, NewEntryCount: UInt32) -> Void: ...
if ARCH in 'X64,ARM64':
    @winfunctype('ntdll.dll')
    def RtlDeleteGrowableFunctionTable(DynamicTable: VoidPtr) -> Void: ...
if ARCH in 'X64':
    @winfunctype('KERNEL32.dll')
    def RtlLookupFunctionEntry(ControlPc: UInt64, ImageBase: POINTER(UInt64), HistoryTable: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.UNWIND_HISTORY_TABLE_head)) -> POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_RUNTIME_FUNCTION_ENTRY_head): ...
if ARCH in 'X64,ARM64':
    @winfunctype('KERNEL32.dll')
    def RtlUnwindEx(TargetFrame: VoidPtr, TargetIp: VoidPtr, ExceptionRecord: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.EXCEPTION_RECORD_head), ReturnValue: VoidPtr, ContextRecord: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_head), HistoryTable: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.UNWIND_HISTORY_TABLE_head)) -> Void: ...
if ARCH in 'X64':
    @winfunctype('KERNEL32.dll')
    def RtlVirtualUnwind(HandlerType: win32more.Windows.Win32.System.Diagnostics.Debug.RTL_VIRTUAL_UNWIND_HANDLER_TYPE, ImageBase: UInt64, ControlPc: UInt64, FunctionEntry: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_RUNTIME_FUNCTION_ENTRY_head), ContextRecord: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_head), HandlerData: POINTER(VoidPtr), EstablisherFrame: POINTER(UInt64), ContextPointers: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.KNONVOLATILE_CONTEXT_POINTERS_head)) -> win32more.Windows.Win32.System.Kernel.EXCEPTION_ROUTINE: ...
if ARCH in 'X64,ARM64':
    @winfunctype('imagehlp.dll')
    def CheckSumMappedFile(BaseAddress: VoidPtr, FileLength: UInt32, HeaderSum: POINTER(UInt32), CheckSum: POINTER(UInt32)) -> POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_NT_HEADERS64_head): ...
if ARCH in 'X64,ARM64':
    @winfunctype('imagehlp.dll')
    def GetImageConfigInformation(LoadedImage: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.LOADED_IMAGE_head), ImageConfigInformation: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_LOAD_CONFIG_DIRECTORY64_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X64,ARM64':
    @winfunctype('imagehlp.dll')
    def SetImageConfigInformation(LoadedImage: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.LOADED_IMAGE_head), ImageConfigInformation: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_LOAD_CONFIG_DIRECTORY64_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X64,ARM64':
    @winfunctype('dbghelp.dll')
    def ImageNtHeader(Base: VoidPtr) -> POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_NT_HEADERS64_head): ...
if ARCH in 'X64,ARM64':
    @winfunctype('dbghelp.dll')
    def ImageRvaToSection(NtHeaders: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_NT_HEADERS64_head), Base: VoidPtr, Rva: UInt32) -> POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_HEADER_head): ...
if ARCH in 'X64,ARM64':
    @winfunctype('dbghelp.dll')
    def ImageRvaToVa(NtHeaders: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_NT_HEADERS64_head), Base: VoidPtr, Rva: UInt32, LastRvaSection: POINTER(POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_HEADER_head))) -> VoidPtr: ...
@winfunctype('KERNEL32.dll')
def RtlCaptureStackBackTrace(FramesToSkip: UInt32, FramesToCapture: UInt32, BackTrace: POINTER(VoidPtr), BackTraceHash: POINTER(UInt32)) -> UInt16: ...
@winfunctype('KERNEL32.dll')
def RtlCaptureContext(ContextRecord: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_head)) -> Void: ...
@winfunctype('KERNEL32.dll')
def RtlUnwind(TargetFrame: VoidPtr, TargetIp: VoidPtr, ExceptionRecord: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.EXCEPTION_RECORD_head), ReturnValue: VoidPtr) -> Void: ...
@cfunctype('KERNEL32.dll')
def RtlRestoreContext(ContextRecord: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_head), ExceptionRecord: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.EXCEPTION_RECORD_head)) -> Void: ...
@winfunctype('KERNEL32.dll')
def RtlRaiseException(ExceptionRecord: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.EXCEPTION_RECORD_head)) -> Void: ...
@winfunctype('KERNEL32.dll')
def RtlPcToFileHeader(PcValue: VoidPtr, BaseOfImage: POINTER(VoidPtr)) -> VoidPtr: ...
@winfunctype('KERNEL32.dll')
def IsDebuggerPresent() -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DebugBreak() -> Void: ...
@winfunctype('KERNEL32.dll')
def OutputDebugStringA(lpOutputString: win32more.Windows.Win32.Foundation.PSTR) -> Void: ...
@winfunctype('KERNEL32.dll')
def OutputDebugStringW(lpOutputString: win32more.Windows.Win32.Foundation.PWSTR) -> Void: ...
@winfunctype('KERNEL32.dll')
def ContinueDebugEvent(dwProcessId: UInt32, dwThreadId: UInt32, dwContinueStatus: win32more.Windows.Win32.Foundation.NTSTATUS) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WaitForDebugEvent(lpDebugEvent: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.DEBUG_EVENT_head), dwMilliseconds: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DebugActiveProcess(dwProcessId: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DebugActiveProcessStop(dwProcessId: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CheckRemoteDebuggerPresent(hProcess: win32more.Windows.Win32.Foundation.HANDLE, pbDebuggerPresent: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WaitForDebugEventEx(lpDebugEvent: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.DEBUG_EVENT_head), dwMilliseconds: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def EncodePointer(Ptr: VoidPtr) -> VoidPtr: ...
@winfunctype('KERNEL32.dll')
def DecodePointer(Ptr: VoidPtr) -> VoidPtr: ...
@winfunctype('KERNEL32.dll')
def EncodeSystemPointer(Ptr: VoidPtr) -> VoidPtr: ...
@winfunctype('KERNEL32.dll')
def DecodeSystemPointer(Ptr: VoidPtr) -> VoidPtr: ...
@winfunctype('api-ms-win-core-util-l1-1-1.dll')
def EncodeRemotePointer(ProcessHandle: win32more.Windows.Win32.Foundation.HANDLE, Ptr: VoidPtr, EncodedPtr: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-util-l1-1-1.dll')
def DecodeRemotePointer(ProcessHandle: win32more.Windows.Win32.Foundation.HANDLE, Ptr: VoidPtr, DecodedPtr: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def Beep(dwFreq: UInt32, dwDuration: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def RaiseException(dwExceptionCode: UInt32, dwExceptionFlags: UInt32, nNumberOfArguments: UInt32, lpArguments: POINTER(UIntPtr)) -> Void: ...
@winfunctype('KERNEL32.dll')
def UnhandledExceptionFilter(ExceptionInfo: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.EXCEPTION_POINTERS_head)) -> Int32: ...
@winfunctype('KERNEL32.dll')
def SetUnhandledExceptionFilter(lpTopLevelExceptionFilter: win32more.Windows.Win32.System.Diagnostics.Debug.LPTOP_LEVEL_EXCEPTION_FILTER) -> win32more.Windows.Win32.System.Diagnostics.Debug.LPTOP_LEVEL_EXCEPTION_FILTER: ...
@winfunctype('KERNEL32.dll')
def GetErrorMode() -> UInt32: ...
@winfunctype('KERNEL32.dll')
def SetErrorMode(uMode: win32more.Windows.Win32.System.Diagnostics.Debug.THREAD_ERROR_MODE) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def AddVectoredExceptionHandler(First: UInt32, Handler: win32more.Windows.Win32.System.Diagnostics.Debug.PVECTORED_EXCEPTION_HANDLER) -> VoidPtr: ...
@winfunctype('KERNEL32.dll')
def RemoveVectoredExceptionHandler(Handle: VoidPtr) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def AddVectoredContinueHandler(First: UInt32, Handler: win32more.Windows.Win32.System.Diagnostics.Debug.PVECTORED_EXCEPTION_HANDLER) -> VoidPtr: ...
@winfunctype('KERNEL32.dll')
def RemoveVectoredContinueHandler(Handle: VoidPtr) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def RaiseFailFastException(pExceptionRecord: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.EXCEPTION_RECORD_head), pContextRecord: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_head), dwFlags: UInt32) -> Void: ...
@winfunctype('KERNEL32.dll')
def FatalAppExitA(uAction: UInt32, lpMessageText: win32more.Windows.Win32.Foundation.PSTR) -> Void: ...
@winfunctype('KERNEL32.dll')
def FatalAppExitW(uAction: UInt32, lpMessageText: win32more.Windows.Win32.Foundation.PWSTR) -> Void: ...
@winfunctype('KERNEL32.dll')
def GetThreadErrorMode() -> UInt32: ...
@winfunctype('KERNEL32.dll')
def SetThreadErrorMode(dwNewMode: win32more.Windows.Win32.System.Diagnostics.Debug.THREAD_ERROR_MODE, lpOldMode: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.THREAD_ERROR_MODE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-errorhandling-l1-1-3.dll')
def TerminateProcessOnMemoryExhaustion(FailedAllocationSize: UIntPtr) -> Void: ...
@winfunctype('ADVAPI32.dll')
def OpenThreadWaitChainSession(Flags: win32more.Windows.Win32.System.Diagnostics.Debug.OPEN_THREAD_WAIT_CHAIN_SESSION_FLAGS, callback: win32more.Windows.Win32.System.Diagnostics.Debug.PWAITCHAINCALLBACK) -> VoidPtr: ...
@winfunctype('ADVAPI32.dll')
def CloseThreadWaitChainSession(WctHandle: VoidPtr) -> Void: ...
@winfunctype('ADVAPI32.dll')
def GetThreadWaitChain(WctHandle: VoidPtr, Context: UIntPtr, Flags: win32more.Windows.Win32.System.Diagnostics.Debug.WAIT_CHAIN_THREAD_OPTIONS, ThreadId: UInt32, NodeCount: POINTER(UInt32), NodeInfoArray: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.WAITCHAIN_NODE_INFO_head), IsCycle: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def RegisterWaitChainCOMCallback(CallStateCallback: win32more.Windows.Win32.System.Diagnostics.Debug.PCOGETCALLSTATE, ActivationStateCallback: win32more.Windows.Win32.System.Diagnostics.Debug.PCOGETACTIVATIONSTATE) -> Void: ...
@winfunctype('dbghelp.dll')
def MiniDumpWriteDump(hProcess: win32more.Windows.Win32.Foundation.HANDLE, ProcessId: UInt32, hFile: win32more.Windows.Win32.Foundation.HANDLE, DumpType: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_TYPE, ExceptionParam: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_EXCEPTION_INFORMATION_head), UserStreamParam: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_USER_STREAM_INFORMATION_head), CallbackParam: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_CALLBACK_INFORMATION_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def MiniDumpReadDumpStream(BaseOfDump: VoidPtr, StreamNumber: UInt32, Dir: POINTER(POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_DIRECTORY_head)), StreamPointer: POINTER(VoidPtr), StreamSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('imagehlp.dll')
def BindImage(ImageName: win32more.Windows.Win32.Foundation.PSTR, DllPath: win32more.Windows.Win32.Foundation.PSTR, SymbolPath: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('imagehlp.dll')
def BindImageEx(Flags: UInt32, ImageName: win32more.Windows.Win32.Foundation.PSTR, DllPath: win32more.Windows.Win32.Foundation.PSTR, SymbolPath: win32more.Windows.Win32.Foundation.PSTR, StatusRoutine: win32more.Windows.Win32.System.Diagnostics.Debug.PIMAGEHLP_STATUS_ROUTINE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('imagehlp.dll')
def ReBaseImage(CurrentImageName: win32more.Windows.Win32.Foundation.PSTR, SymbolPath: win32more.Windows.Win32.Foundation.PSTR, fReBase: win32more.Windows.Win32.Foundation.BOOL, fRebaseSysfileOk: win32more.Windows.Win32.Foundation.BOOL, fGoingDown: win32more.Windows.Win32.Foundation.BOOL, CheckImageSize: UInt32, OldImageSize: POINTER(UInt32), OldImageBase: POINTER(UIntPtr), NewImageSize: POINTER(UInt32), NewImageBase: POINTER(UIntPtr), TimeStamp: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('imagehlp.dll')
def ReBaseImage64(CurrentImageName: win32more.Windows.Win32.Foundation.PSTR, SymbolPath: win32more.Windows.Win32.Foundation.PSTR, fReBase: win32more.Windows.Win32.Foundation.BOOL, fRebaseSysfileOk: win32more.Windows.Win32.Foundation.BOOL, fGoingDown: win32more.Windows.Win32.Foundation.BOOL, CheckImageSize: UInt32, OldImageSize: POINTER(UInt32), OldImageBase: POINTER(UInt64), NewImageSize: POINTER(UInt32), NewImageBase: POINTER(UInt64), TimeStamp: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X86':
    @winfunctype('imagehlp.dll')
    def CheckSumMappedFile(BaseAddress: VoidPtr, FileLength: UInt32, HeaderSum: POINTER(UInt32), CheckSum: POINTER(UInt32)) -> POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_NT_HEADERS32_head): ...
@winfunctype('imagehlp.dll')
def MapFileAndCheckSumA(Filename: win32more.Windows.Win32.Foundation.PSTR, HeaderSum: POINTER(UInt32), CheckSum: POINTER(UInt32)) -> UInt32: ...
@winfunctype('imagehlp.dll')
def MapFileAndCheckSumW(Filename: win32more.Windows.Win32.Foundation.PWSTR, HeaderSum: POINTER(UInt32), CheckSum: POINTER(UInt32)) -> UInt32: ...
if ARCH in 'X86':
    @winfunctype('imagehlp.dll')
    def GetImageConfigInformation(LoadedImage: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.LOADED_IMAGE_head), ImageConfigInformation: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_LOAD_CONFIG_DIRECTORY32_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('imagehlp.dll')
def GetImageUnusedHeaderBytes(LoadedImage: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.LOADED_IMAGE_head), SizeUnusedHeaderBytes: POINTER(UInt32)) -> UInt32: ...
if ARCH in 'X86':
    @winfunctype('imagehlp.dll')
    def SetImageConfigInformation(LoadedImage: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.LOADED_IMAGE_head), ImageConfigInformation: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_LOAD_CONFIG_DIRECTORY32_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('imagehlp.dll')
def ImageGetDigestStream(FileHandle: win32more.Windows.Win32.Foundation.HANDLE, DigestLevel: UInt32, DigestFunction: win32more.Windows.Win32.System.Diagnostics.Debug.DIGEST_FUNCTION, DigestHandle: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('imagehlp.dll')
def ImageAddCertificate(FileHandle: win32more.Windows.Win32.Foundation.HANDLE, Certificate: POINTER(win32more.Windows.Win32.Security.WinTrust.WIN_CERTIFICATE_head), Index: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('imagehlp.dll')
def ImageRemoveCertificate(FileHandle: win32more.Windows.Win32.Foundation.HANDLE, Index: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('imagehlp.dll')
def ImageEnumerateCertificates(FileHandle: win32more.Windows.Win32.Foundation.HANDLE, TypeFilter: UInt16, CertificateCount: POINTER(UInt32), Indices: POINTER(UInt32), IndexCount: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('imagehlp.dll')
def ImageGetCertificateData(FileHandle: win32more.Windows.Win32.Foundation.HANDLE, CertificateIndex: UInt32, Certificate: POINTER(win32more.Windows.Win32.Security.WinTrust.WIN_CERTIFICATE_head), RequiredLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('imagehlp.dll')
def ImageGetCertificateHeader(FileHandle: win32more.Windows.Win32.Foundation.HANDLE, CertificateIndex: UInt32, Certificateheader: POINTER(win32more.Windows.Win32.Security.WinTrust.WIN_CERTIFICATE_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('imagehlp.dll')
def ImageLoad(DllName: win32more.Windows.Win32.Foundation.PSTR, DllPath: win32more.Windows.Win32.Foundation.PSTR) -> POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.LOADED_IMAGE_head): ...
@winfunctype('imagehlp.dll')
def ImageUnload(LoadedImage: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.LOADED_IMAGE_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('imagehlp.dll')
def MapAndLoad(ImageName: win32more.Windows.Win32.Foundation.PSTR, DllPath: win32more.Windows.Win32.Foundation.PSTR, LoadedImage: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.LOADED_IMAGE_head), DotDll: win32more.Windows.Win32.Foundation.BOOL, ReadOnly: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('imagehlp.dll')
def UnMapAndLoad(LoadedImage: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.LOADED_IMAGE_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('imagehlp.dll')
def TouchFileTimes(FileHandle: win32more.Windows.Win32.Foundation.HANDLE, pSystemTime: POINTER(win32more.Windows.Win32.Foundation.SYSTEMTIME_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('imagehlp.dll')
def UpdateDebugInfoFile(ImageFileName: win32more.Windows.Win32.Foundation.PSTR, SymbolPath: win32more.Windows.Win32.Foundation.PSTR, DebugFilePath: win32more.Windows.Win32.Foundation.PSTR, NtHeaders: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_NT_HEADERS32_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('imagehlp.dll')
def UpdateDebugInfoFileEx(ImageFileName: win32more.Windows.Win32.Foundation.PSTR, SymbolPath: win32more.Windows.Win32.Foundation.PSTR, DebugFilePath: win32more.Windows.Win32.Foundation.PSTR, NtHeaders: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_NT_HEADERS32_head), OldCheckSum: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymFindDebugInfoFile(hProcess: win32more.Windows.Win32.Foundation.HANDLE, FileName: win32more.Windows.Win32.Foundation.PSTR, DebugFilePath: win32more.Windows.Win32.Foundation.PSTR, Callback: win32more.Windows.Win32.System.Diagnostics.Debug.PFIND_DEBUG_FILE_CALLBACK, CallerData: VoidPtr) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('dbghelp.dll')
def SymFindDebugInfoFileW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, FileName: win32more.Windows.Win32.Foundation.PWSTR, DebugFilePath: win32more.Windows.Win32.Foundation.PWSTR, Callback: win32more.Windows.Win32.System.Diagnostics.Debug.PFIND_DEBUG_FILE_CALLBACKW, CallerData: VoidPtr) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('dbghelp.dll')
def FindDebugInfoFile(FileName: win32more.Windows.Win32.Foundation.PSTR, SymbolPath: win32more.Windows.Win32.Foundation.PSTR, DebugFilePath: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('dbghelp.dll')
def FindDebugInfoFileEx(FileName: win32more.Windows.Win32.Foundation.PSTR, SymbolPath: win32more.Windows.Win32.Foundation.PSTR, DebugFilePath: win32more.Windows.Win32.Foundation.PSTR, Callback: win32more.Windows.Win32.System.Diagnostics.Debug.PFIND_DEBUG_FILE_CALLBACK, CallerData: VoidPtr) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('dbghelp.dll')
def FindDebugInfoFileExW(FileName: win32more.Windows.Win32.Foundation.PWSTR, SymbolPath: win32more.Windows.Win32.Foundation.PWSTR, DebugFilePath: win32more.Windows.Win32.Foundation.PWSTR, Callback: win32more.Windows.Win32.System.Diagnostics.Debug.PFIND_DEBUG_FILE_CALLBACKW, CallerData: VoidPtr) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('dbghelp.dll')
def SymFindFileInPath(hprocess: win32more.Windows.Win32.Foundation.HANDLE, SearchPathA: win32more.Windows.Win32.Foundation.PSTR, FileName: win32more.Windows.Win32.Foundation.PSTR, id: VoidPtr, two: UInt32, three: UInt32, flags: win32more.Windows.Win32.System.Diagnostics.Debug.SYM_FIND_ID_OPTION, FoundFile: win32more.Windows.Win32.Foundation.PSTR, callback: win32more.Windows.Win32.System.Diagnostics.Debug.PFINDFILEINPATHCALLBACK, context: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymFindFileInPathW(hprocess: win32more.Windows.Win32.Foundation.HANDLE, SearchPathA: win32more.Windows.Win32.Foundation.PWSTR, FileName: win32more.Windows.Win32.Foundation.PWSTR, id: VoidPtr, two: UInt32, three: UInt32, flags: win32more.Windows.Win32.System.Diagnostics.Debug.SYM_FIND_ID_OPTION, FoundFile: win32more.Windows.Win32.Foundation.PWSTR, callback: win32more.Windows.Win32.System.Diagnostics.Debug.PFINDFILEINPATHCALLBACKW, context: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymFindExecutableImage(hProcess: win32more.Windows.Win32.Foundation.HANDLE, FileName: win32more.Windows.Win32.Foundation.PSTR, ImageFilePath: win32more.Windows.Win32.Foundation.PSTR, Callback: win32more.Windows.Win32.System.Diagnostics.Debug.PFIND_EXE_FILE_CALLBACK, CallerData: VoidPtr) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('dbghelp.dll')
def SymFindExecutableImageW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, FileName: win32more.Windows.Win32.Foundation.PWSTR, ImageFilePath: win32more.Windows.Win32.Foundation.PWSTR, Callback: win32more.Windows.Win32.System.Diagnostics.Debug.PFIND_EXE_FILE_CALLBACKW, CallerData: VoidPtr) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('dbghelp.dll')
def FindExecutableImage(FileName: win32more.Windows.Win32.Foundation.PSTR, SymbolPath: win32more.Windows.Win32.Foundation.PSTR, ImageFilePath: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('dbghelp.dll')
def FindExecutableImageEx(FileName: win32more.Windows.Win32.Foundation.PSTR, SymbolPath: win32more.Windows.Win32.Foundation.PSTR, ImageFilePath: win32more.Windows.Win32.Foundation.PSTR, Callback: win32more.Windows.Win32.System.Diagnostics.Debug.PFIND_EXE_FILE_CALLBACK, CallerData: VoidPtr) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('dbghelp.dll')
def FindExecutableImageExW(FileName: win32more.Windows.Win32.Foundation.PWSTR, SymbolPath: win32more.Windows.Win32.Foundation.PWSTR, ImageFilePath: win32more.Windows.Win32.Foundation.PWSTR, Callback: win32more.Windows.Win32.System.Diagnostics.Debug.PFIND_EXE_FILE_CALLBACKW, CallerData: VoidPtr) -> win32more.Windows.Win32.Foundation.HANDLE: ...
if ARCH in 'X86':
    @winfunctype('dbghelp.dll')
    def ImageNtHeader(Base: VoidPtr) -> POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_NT_HEADERS32_head): ...
@winfunctype('dbghelp.dll')
def ImageDirectoryEntryToDataEx(Base: VoidPtr, MappedAsImage: win32more.Windows.Win32.Foundation.BOOLEAN, DirectoryEntry: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DIRECTORY_ENTRY, Size: POINTER(UInt32), FoundHeader: POINTER(POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_HEADER_head))) -> VoidPtr: ...
@winfunctype('dbghelp.dll')
def ImageDirectoryEntryToData(Base: VoidPtr, MappedAsImage: win32more.Windows.Win32.Foundation.BOOLEAN, DirectoryEntry: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DIRECTORY_ENTRY, Size: POINTER(UInt32)) -> VoidPtr: ...
if ARCH in 'X86':
    @winfunctype('dbghelp.dll')
    def ImageRvaToSection(NtHeaders: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_NT_HEADERS32_head), Base: VoidPtr, Rva: UInt32) -> POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_HEADER_head): ...
if ARCH in 'X86':
    @winfunctype('dbghelp.dll')
    def ImageRvaToVa(NtHeaders: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_NT_HEADERS32_head), Base: VoidPtr, Rva: UInt32, LastRvaSection: POINTER(POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_HEADER_head))) -> VoidPtr: ...
@winfunctype('dbghelp.dll')
def SearchTreeForFile(RootPath: win32more.Windows.Win32.Foundation.PSTR, InputPathName: win32more.Windows.Win32.Foundation.PSTR, OutputPathBuffer: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SearchTreeForFileW(RootPath: win32more.Windows.Win32.Foundation.PWSTR, InputPathName: win32more.Windows.Win32.Foundation.PWSTR, OutputPathBuffer: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def EnumDirTree(hProcess: win32more.Windows.Win32.Foundation.HANDLE, RootPath: win32more.Windows.Win32.Foundation.PSTR, InputPathName: win32more.Windows.Win32.Foundation.PSTR, OutputPathBuffer: win32more.Windows.Win32.Foundation.PSTR, cb: win32more.Windows.Win32.System.Diagnostics.Debug.PENUMDIRTREE_CALLBACK, data: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def EnumDirTreeW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, RootPath: win32more.Windows.Win32.Foundation.PWSTR, InputPathName: win32more.Windows.Win32.Foundation.PWSTR, OutputPathBuffer: win32more.Windows.Win32.Foundation.PWSTR, cb: win32more.Windows.Win32.System.Diagnostics.Debug.PENUMDIRTREE_CALLBACKW, data: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def MakeSureDirectoryPathExists(DirPath: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def UnDecorateSymbolName(name: win32more.Windows.Win32.Foundation.PSTR, outputString: win32more.Windows.Win32.Foundation.PSTR, maxStringLength: UInt32, flags: UInt32) -> UInt32: ...
@winfunctype('dbghelp.dll')
def UnDecorateSymbolNameW(name: win32more.Windows.Win32.Foundation.PWSTR, outputString: win32more.Windows.Win32.Foundation.PWSTR, maxStringLength: UInt32, flags: UInt32) -> UInt32: ...
@winfunctype('dbghelp.dll')
def StackWalk64(MachineType: UInt32, hProcess: win32more.Windows.Win32.Foundation.HANDLE, hThread: win32more.Windows.Win32.Foundation.HANDLE, StackFrame: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.STACKFRAME64_head), ContextRecord: VoidPtr, ReadMemoryRoutine: win32more.Windows.Win32.System.Diagnostics.Debug.PREAD_PROCESS_MEMORY_ROUTINE64, FunctionTableAccessRoutine: win32more.Windows.Win32.System.Diagnostics.Debug.PFUNCTION_TABLE_ACCESS_ROUTINE64, GetModuleBaseRoutine: win32more.Windows.Win32.System.Diagnostics.Debug.PGET_MODULE_BASE_ROUTINE64, TranslateAddress: win32more.Windows.Win32.System.Diagnostics.Debug.PTRANSLATE_ADDRESS_ROUTINE64) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def StackWalkEx(MachineType: UInt32, hProcess: win32more.Windows.Win32.Foundation.HANDLE, hThread: win32more.Windows.Win32.Foundation.HANDLE, StackFrame: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.STACKFRAME_EX_head), ContextRecord: VoidPtr, ReadMemoryRoutine: win32more.Windows.Win32.System.Diagnostics.Debug.PREAD_PROCESS_MEMORY_ROUTINE64, FunctionTableAccessRoutine: win32more.Windows.Win32.System.Diagnostics.Debug.PFUNCTION_TABLE_ACCESS_ROUTINE64, GetModuleBaseRoutine: win32more.Windows.Win32.System.Diagnostics.Debug.PGET_MODULE_BASE_ROUTINE64, TranslateAddress: win32more.Windows.Win32.System.Diagnostics.Debug.PTRANSLATE_ADDRESS_ROUTINE64, Flags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def StackWalk2(MachineType: UInt32, hProcess: win32more.Windows.Win32.Foundation.HANDLE, hThread: win32more.Windows.Win32.Foundation.HANDLE, StackFrame: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.STACKFRAME_EX_head), ContextRecord: VoidPtr, ReadMemoryRoutine: win32more.Windows.Win32.System.Diagnostics.Debug.PREAD_PROCESS_MEMORY_ROUTINE64, FunctionTableAccessRoutine: win32more.Windows.Win32.System.Diagnostics.Debug.PFUNCTION_TABLE_ACCESS_ROUTINE64, GetModuleBaseRoutine: win32more.Windows.Win32.System.Diagnostics.Debug.PGET_MODULE_BASE_ROUTINE64, TranslateAddress: win32more.Windows.Win32.System.Diagnostics.Debug.PTRANSLATE_ADDRESS_ROUTINE64, GetTargetAttributeValue: win32more.Windows.Win32.System.Diagnostics.Debug.PGET_TARGET_ATTRIBUTE_VALUE64, Flags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X86':
    @winfunctype('dbghelp.dll')
    def StackWalk(MachineType: UInt32, hProcess: win32more.Windows.Win32.Foundation.HANDLE, hThread: win32more.Windows.Win32.Foundation.HANDLE, StackFrame: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.STACKFRAME_head), ContextRecord: VoidPtr, ReadMemoryRoutine: win32more.Windows.Win32.System.Diagnostics.Debug.PREAD_PROCESS_MEMORY_ROUTINE, FunctionTableAccessRoutine: win32more.Windows.Win32.System.Diagnostics.Debug.PFUNCTION_TABLE_ACCESS_ROUTINE, GetModuleBaseRoutine: win32more.Windows.Win32.System.Diagnostics.Debug.PGET_MODULE_BASE_ROUTINE, TranslateAddress: win32more.Windows.Win32.System.Diagnostics.Debug.PTRANSLATE_ADDRESS_ROUTINE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def ImagehlpApiVersion() -> POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.API_VERSION_head): ...
@winfunctype('dbghelp.dll')
def ImagehlpApiVersionEx(AppVersion: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.API_VERSION_head)) -> POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.API_VERSION_head): ...
@winfunctype('dbghelp.dll')
def GetTimestampForLoadedLibrary(Module: win32more.Windows.Win32.Foundation.HMODULE) -> UInt32: ...
@winfunctype('dbghelp.dll')
def SymSetParentWindow(hwnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymSetHomeDirectory(hProcess: win32more.Windows.Win32.Foundation.HANDLE, dir: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.PSTR: ...
@winfunctype('dbghelp.dll')
def SymSetHomeDirectoryW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, dir: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.PWSTR: ...
@winfunctype('dbghelp.dll')
def SymGetHomeDirectory(type: UInt32, dir: win32more.Windows.Win32.Foundation.PSTR, size: UIntPtr) -> win32more.Windows.Win32.Foundation.PSTR: ...
@winfunctype('dbghelp.dll')
def SymGetHomeDirectoryW(type: UInt32, dir: win32more.Windows.Win32.Foundation.PWSTR, size: UIntPtr) -> win32more.Windows.Win32.Foundation.PWSTR: ...
@winfunctype('dbghelp.dll')
def SymGetOmaps(hProcess: win32more.Windows.Win32.Foundation.HANDLE, BaseOfDll: UInt64, OmapTo: POINTER(POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.OMAP_head)), cOmapTo: POINTER(UInt64), OmapFrom: POINTER(POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.OMAP_head)), cOmapFrom: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymSetOptions(SymOptions: UInt32) -> UInt32: ...
@winfunctype('dbghelp.dll')
def SymGetOptions() -> UInt32: ...
@winfunctype('dbghelp.dll')
def SymCleanup(hProcess: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetExtendedOption(option: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_EXTENDED_OPTIONS) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymSetExtendedOption(option: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_EXTENDED_OPTIONS, value: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymMatchString(string: win32more.Windows.Win32.Foundation.PSTR, expression: win32more.Windows.Win32.Foundation.PSTR, fCase: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymMatchStringA(string: win32more.Windows.Win32.Foundation.PSTR, expression: win32more.Windows.Win32.Foundation.PSTR, fCase: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymMatchStringW(string: win32more.Windows.Win32.Foundation.PWSTR, expression: win32more.Windows.Win32.Foundation.PWSTR, fCase: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymEnumSourceFiles(hProcess: win32more.Windows.Win32.Foundation.HANDLE, ModBase: UInt64, Mask: win32more.Windows.Win32.Foundation.PSTR, cbSrcFiles: win32more.Windows.Win32.System.Diagnostics.Debug.PSYM_ENUMSOURCEFILES_CALLBACK, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymEnumSourceFilesW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, ModBase: UInt64, Mask: win32more.Windows.Win32.Foundation.PWSTR, cbSrcFiles: win32more.Windows.Win32.System.Diagnostics.Debug.PSYM_ENUMSOURCEFILES_CALLBACKW, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymEnumerateModules64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, EnumModulesCallback: win32more.Windows.Win32.System.Diagnostics.Debug.PSYM_ENUMMODULES_CALLBACK64, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymEnumerateModulesW64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, EnumModulesCallback: win32more.Windows.Win32.System.Diagnostics.Debug.PSYM_ENUMMODULES_CALLBACKW64, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X86':
    @winfunctype('dbghelp.dll')
    def SymEnumerateModules(hProcess: win32more.Windows.Win32.Foundation.HANDLE, EnumModulesCallback: win32more.Windows.Win32.System.Diagnostics.Debug.PSYM_ENUMMODULES_CALLBACK, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def EnumerateLoadedModulesEx(hProcess: win32more.Windows.Win32.Foundation.HANDLE, EnumLoadedModulesCallback: win32more.Windows.Win32.System.Diagnostics.Debug.PENUMLOADED_MODULES_CALLBACK64, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def EnumerateLoadedModulesExW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, EnumLoadedModulesCallback: win32more.Windows.Win32.System.Diagnostics.Debug.PENUMLOADED_MODULES_CALLBACKW64, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def EnumerateLoadedModules64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, EnumLoadedModulesCallback: win32more.Windows.Win32.System.Diagnostics.Debug.PENUMLOADED_MODULES_CALLBACK64, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def EnumerateLoadedModulesW64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, EnumLoadedModulesCallback: win32more.Windows.Win32.System.Diagnostics.Debug.PENUMLOADED_MODULES_CALLBACKW64, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X86':
    @winfunctype('dbghelp.dll')
    def EnumerateLoadedModules(hProcess: win32more.Windows.Win32.Foundation.HANDLE, EnumLoadedModulesCallback: win32more.Windows.Win32.System.Diagnostics.Debug.PENUMLOADED_MODULES_CALLBACK, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymFunctionTableAccess64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, AddrBase: UInt64) -> VoidPtr: ...
@winfunctype('dbghelp.dll')
def SymFunctionTableAccess64AccessRoutines(hProcess: win32more.Windows.Win32.Foundation.HANDLE, AddrBase: UInt64, ReadMemoryRoutine: win32more.Windows.Win32.System.Diagnostics.Debug.PREAD_PROCESS_MEMORY_ROUTINE64, GetModuleBaseRoutine: win32more.Windows.Win32.System.Diagnostics.Debug.PGET_MODULE_BASE_ROUTINE64) -> VoidPtr: ...
if ARCH in 'X86':
    @winfunctype('dbghelp.dll')
    def SymFunctionTableAccess(hProcess: win32more.Windows.Win32.Foundation.HANDLE, AddrBase: UInt32) -> VoidPtr: ...
@winfunctype('dbghelp.dll')
def SymGetUnwindInfo(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Address: UInt64, Buffer: VoidPtr, Size: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetModuleInfo64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, qwAddr: UInt64, ModuleInfo: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_MODULE64_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetModuleInfoW64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, qwAddr: UInt64, ModuleInfo: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_MODULEW64_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X86':
    @winfunctype('dbghelp.dll')
    def SymGetModuleInfo(hProcess: win32more.Windows.Win32.Foundation.HANDLE, dwAddr: UInt32, ModuleInfo: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_MODULE_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X86':
    @winfunctype('dbghelp.dll')
    def SymGetModuleInfoW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, dwAddr: UInt32, ModuleInfo: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_MODULEW_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetModuleBase64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, qwAddr: UInt64) -> UInt64: ...
if ARCH in 'X86':
    @winfunctype('dbghelp.dll')
    def SymGetModuleBase(hProcess: win32more.Windows.Win32.Foundation.HANDLE, dwAddr: UInt32) -> UInt32: ...
@winfunctype('dbghelp.dll')
def SymEnumLines(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Base: UInt64, Obj: win32more.Windows.Win32.Foundation.PSTR, File: win32more.Windows.Win32.Foundation.PSTR, EnumLinesCallback: win32more.Windows.Win32.System.Diagnostics.Debug.PSYM_ENUMLINES_CALLBACK, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymEnumLinesW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Base: UInt64, Obj: win32more.Windows.Win32.Foundation.PWSTR, File: win32more.Windows.Win32.Foundation.PWSTR, EnumLinesCallback: win32more.Windows.Win32.System.Diagnostics.Debug.PSYM_ENUMLINES_CALLBACKW, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetLineFromAddr64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, qwAddr: UInt64, pdwDisplacement: POINTER(UInt32), Line64: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_LINE64_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetLineFromAddrW64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, dwAddr: UInt64, pdwDisplacement: POINTER(UInt32), Line: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_LINEW64_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetLineFromInlineContext(hProcess: win32more.Windows.Win32.Foundation.HANDLE, qwAddr: UInt64, InlineContext: UInt32, qwModuleBaseAddress: UInt64, pdwDisplacement: POINTER(UInt32), Line64: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_LINE64_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetLineFromInlineContextW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, dwAddr: UInt64, InlineContext: UInt32, qwModuleBaseAddress: UInt64, pdwDisplacement: POINTER(UInt32), Line: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_LINEW64_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymEnumSourceLines(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Base: UInt64, Obj: win32more.Windows.Win32.Foundation.PSTR, File: win32more.Windows.Win32.Foundation.PSTR, Line: UInt32, Flags: UInt32, EnumLinesCallback: win32more.Windows.Win32.System.Diagnostics.Debug.PSYM_ENUMLINES_CALLBACK, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymEnumSourceLinesW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Base: UInt64, Obj: win32more.Windows.Win32.Foundation.PWSTR, File: win32more.Windows.Win32.Foundation.PWSTR, Line: UInt32, Flags: UInt32, EnumLinesCallback: win32more.Windows.Win32.System.Diagnostics.Debug.PSYM_ENUMLINES_CALLBACKW, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymAddrIncludeInlineTrace(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Address: UInt64) -> UInt32: ...
@winfunctype('dbghelp.dll')
def SymCompareInlineTrace(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Address1: UInt64, InlineContext1: UInt32, RetAddress1: UInt64, Address2: UInt64, RetAddress2: UInt64) -> UInt32: ...
@winfunctype('dbghelp.dll')
def SymQueryInlineTrace(hProcess: win32more.Windows.Win32.Foundation.HANDLE, StartAddress: UInt64, StartContext: UInt32, StartRetAddress: UInt64, CurAddress: UInt64, CurContext: POINTER(UInt32), CurFrameIndex: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X86':
    @winfunctype('dbghelp.dll')
    def SymGetLineFromAddr(hProcess: win32more.Windows.Win32.Foundation.HANDLE, dwAddr: UInt32, pdwDisplacement: POINTER(UInt32), Line: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_LINE_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetLineFromName64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, ModuleName: win32more.Windows.Win32.Foundation.PSTR, FileName: win32more.Windows.Win32.Foundation.PSTR, dwLineNumber: UInt32, plDisplacement: POINTER(Int32), Line: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_LINE64_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetLineFromNameW64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, ModuleName: win32more.Windows.Win32.Foundation.PWSTR, FileName: win32more.Windows.Win32.Foundation.PWSTR, dwLineNumber: UInt32, plDisplacement: POINTER(Int32), Line: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_LINEW64_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X86':
    @winfunctype('dbghelp.dll')
    def SymGetLineFromName(hProcess: win32more.Windows.Win32.Foundation.HANDLE, ModuleName: win32more.Windows.Win32.Foundation.PSTR, FileName: win32more.Windows.Win32.Foundation.PSTR, dwLineNumber: UInt32, plDisplacement: POINTER(Int32), Line: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_LINE_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetLineNext64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Line: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_LINE64_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetLineNextW64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Line: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_LINEW64_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X86':
    @winfunctype('dbghelp.dll')
    def SymGetLineNext(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Line: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_LINE_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetLinePrev64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Line: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_LINE64_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetLinePrevW64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Line: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_LINEW64_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X86':
    @winfunctype('dbghelp.dll')
    def SymGetLinePrev(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Line: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_LINE_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetFileLineOffsets64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, ModuleName: win32more.Windows.Win32.Foundation.PSTR, FileName: win32more.Windows.Win32.Foundation.PSTR, Buffer: POINTER(UInt64), BufferLines: UInt32) -> UInt32: ...
@winfunctype('dbghelp.dll')
def SymMatchFileName(FileName: win32more.Windows.Win32.Foundation.PSTR, Match: win32more.Windows.Win32.Foundation.PSTR, FileNameStop: POINTER(win32more.Windows.Win32.Foundation.PSTR), MatchStop: POINTER(win32more.Windows.Win32.Foundation.PSTR)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymMatchFileNameW(FileName: win32more.Windows.Win32.Foundation.PWSTR, Match: win32more.Windows.Win32.Foundation.PWSTR, FileNameStop: POINTER(win32more.Windows.Win32.Foundation.PWSTR), MatchStop: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetSourceFile(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Base: UInt64, Params: win32more.Windows.Win32.Foundation.PSTR, FileSpec: win32more.Windows.Win32.Foundation.PSTR, FilePath: win32more.Windows.Win32.Foundation.PSTR, Size: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetSourceFileW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Base: UInt64, Params: win32more.Windows.Win32.Foundation.PWSTR, FileSpec: win32more.Windows.Win32.Foundation.PWSTR, FilePath: win32more.Windows.Win32.Foundation.PWSTR, Size: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetSourceFileToken(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Base: UInt64, FileSpec: win32more.Windows.Win32.Foundation.PSTR, Token: POINTER(VoidPtr), Size: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetSourceFileTokenByTokenName(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Base: UInt64, FileSpec: win32more.Windows.Win32.Foundation.PSTR, TokenName: win32more.Windows.Win32.Foundation.PSTR, TokenParameters: win32more.Windows.Win32.Foundation.PSTR, Token: POINTER(VoidPtr), Size: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetSourceFileChecksumW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Base: UInt64, FileSpec: win32more.Windows.Win32.Foundation.PWSTR, pCheckSumType: POINTER(UInt32), pChecksum: POINTER(Byte), checksumSize: UInt32, pActualBytesWritten: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetSourceFileChecksum(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Base: UInt64, FileSpec: win32more.Windows.Win32.Foundation.PSTR, pCheckSumType: POINTER(UInt32), pChecksum: POINTER(Byte), checksumSize: UInt32, pActualBytesWritten: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetSourceFileTokenW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Base: UInt64, FileSpec: win32more.Windows.Win32.Foundation.PWSTR, Token: POINTER(VoidPtr), Size: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetSourceFileTokenByTokenNameW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Base: UInt64, FileSpec: win32more.Windows.Win32.Foundation.PWSTR, TokenName: win32more.Windows.Win32.Foundation.PWSTR, TokenParameters: win32more.Windows.Win32.Foundation.PWSTR, Token: POINTER(VoidPtr), Size: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetSourceFileFromToken(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Token: VoidPtr, Params: win32more.Windows.Win32.Foundation.PSTR, FilePath: win32more.Windows.Win32.Foundation.PSTR, Size: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetSourceFileFromTokenByTokenName(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Token: VoidPtr, TokenName: win32more.Windows.Win32.Foundation.PSTR, Params: win32more.Windows.Win32.Foundation.PSTR, FilePath: win32more.Windows.Win32.Foundation.PSTR, Size: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetSourceFileFromTokenW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Token: VoidPtr, Params: win32more.Windows.Win32.Foundation.PWSTR, FilePath: win32more.Windows.Win32.Foundation.PWSTR, Size: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetSourceFileFromTokenByTokenNameW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Token: VoidPtr, TokenName: win32more.Windows.Win32.Foundation.PWSTR, Params: win32more.Windows.Win32.Foundation.PWSTR, FilePath: win32more.Windows.Win32.Foundation.PWSTR, Size: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetSourceVarFromToken(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Token: VoidPtr, Params: win32more.Windows.Win32.Foundation.PSTR, VarName: win32more.Windows.Win32.Foundation.PSTR, Value: win32more.Windows.Win32.Foundation.PSTR, Size: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetSourceVarFromTokenW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Token: VoidPtr, Params: win32more.Windows.Win32.Foundation.PWSTR, VarName: win32more.Windows.Win32.Foundation.PWSTR, Value: win32more.Windows.Win32.Foundation.PWSTR, Size: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymEnumSourceFileTokens(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Base: UInt64, Callback: win32more.Windows.Win32.System.Diagnostics.Debug.PENUMSOURCEFILETOKENSCALLBACK) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymInitialize(hProcess: win32more.Windows.Win32.Foundation.HANDLE, UserSearchPath: win32more.Windows.Win32.Foundation.PSTR, fInvadeProcess: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymInitializeW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, UserSearchPath: win32more.Windows.Win32.Foundation.PWSTR, fInvadeProcess: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetSearchPath(hProcess: win32more.Windows.Win32.Foundation.HANDLE, SearchPathA: win32more.Windows.Win32.Foundation.PSTR, SearchPathLength: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetSearchPathW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, SearchPathA: win32more.Windows.Win32.Foundation.PWSTR, SearchPathLength: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymSetSearchPath(hProcess: win32more.Windows.Win32.Foundation.HANDLE, SearchPathA: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymSetSearchPathW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, SearchPathA: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymLoadModuleEx(hProcess: win32more.Windows.Win32.Foundation.HANDLE, hFile: win32more.Windows.Win32.Foundation.HANDLE, ImageName: win32more.Windows.Win32.Foundation.PSTR, ModuleName: win32more.Windows.Win32.Foundation.PSTR, BaseOfDll: UInt64, DllSize: UInt32, Data: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.MODLOAD_DATA_head), Flags: win32more.Windows.Win32.System.Diagnostics.Debug.SYM_LOAD_FLAGS) -> UInt64: ...
@winfunctype('dbghelp.dll')
def SymLoadModuleExW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, hFile: win32more.Windows.Win32.Foundation.HANDLE, ImageName: win32more.Windows.Win32.Foundation.PWSTR, ModuleName: win32more.Windows.Win32.Foundation.PWSTR, BaseOfDll: UInt64, DllSize: UInt32, Data: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.MODLOAD_DATA_head), Flags: win32more.Windows.Win32.System.Diagnostics.Debug.SYM_LOAD_FLAGS) -> UInt64: ...
@winfunctype('dbghelp.dll')
def SymUnloadModule64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, BaseOfDll: UInt64) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X86':
    @winfunctype('dbghelp.dll')
    def SymUnloadModule(hProcess: win32more.Windows.Win32.Foundation.HANDLE, BaseOfDll: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymUnDName64(sym: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL64_head), UnDecName: win32more.Windows.Win32.Foundation.PSTR, UnDecNameLength: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X86':
    @winfunctype('dbghelp.dll')
    def SymUnDName(sym: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL_head), UnDecName: win32more.Windows.Win32.Foundation.PSTR, UnDecNameLength: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymRegisterCallback64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, CallbackFunction: win32more.Windows.Win32.System.Diagnostics.Debug.PSYMBOL_REGISTERED_CALLBACK64, UserContext: UInt64) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymRegisterCallbackW64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, CallbackFunction: win32more.Windows.Win32.System.Diagnostics.Debug.PSYMBOL_REGISTERED_CALLBACK64, UserContext: UInt64) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymRegisterFunctionEntryCallback64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, CallbackFunction: win32more.Windows.Win32.System.Diagnostics.Debug.PSYMBOL_FUNCENTRY_CALLBACK64, UserContext: UInt64) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X86':
    @winfunctype('dbghelp.dll')
    def SymRegisterCallback(hProcess: win32more.Windows.Win32.Foundation.HANDLE, CallbackFunction: win32more.Windows.Win32.System.Diagnostics.Debug.PSYMBOL_REGISTERED_CALLBACK, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X86':
    @winfunctype('dbghelp.dll')
    def SymRegisterFunctionEntryCallback(hProcess: win32more.Windows.Win32.Foundation.HANDLE, CallbackFunction: win32more.Windows.Win32.System.Diagnostics.Debug.PSYMBOL_FUNCENTRY_CALLBACK, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymSetContext(hProcess: win32more.Windows.Win32.Foundation.HANDLE, StackFrame: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_STACK_FRAME_head), Context: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymSetScopeFromAddr(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Address: UInt64) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymSetScopeFromInlineContext(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Address: UInt64, InlineContext: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymSetScopeFromIndex(hProcess: win32more.Windows.Win32.Foundation.HANDLE, BaseOfDll: UInt64, Index: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymEnumProcesses(EnumProcessesCallback: win32more.Windows.Win32.System.Diagnostics.Debug.PSYM_ENUMPROCESSES_CALLBACK, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymFromAddr(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Address: UInt64, Displacement: POINTER(UInt64), Symbol: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFO_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymFromAddrW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Address: UInt64, Displacement: POINTER(UInt64), Symbol: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFOW_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymFromInlineContext(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Address: UInt64, InlineContext: UInt32, Displacement: POINTER(UInt64), Symbol: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFO_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymFromInlineContextW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Address: UInt64, InlineContext: UInt32, Displacement: POINTER(UInt64), Symbol: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFOW_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymFromToken(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Base: UInt64, Token: UInt32, Symbol: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFO_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymFromTokenW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Base: UInt64, Token: UInt32, Symbol: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFOW_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymNext(hProcess: win32more.Windows.Win32.Foundation.HANDLE, si: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFO_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymNextW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, siw: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFOW_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymPrev(hProcess: win32more.Windows.Win32.Foundation.HANDLE, si: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFO_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymPrevW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, siw: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFOW_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymFromName(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Name: win32more.Windows.Win32.Foundation.PSTR, Symbol: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFO_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymFromNameW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Name: win32more.Windows.Win32.Foundation.PWSTR, Symbol: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFOW_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymEnumSymbols(hProcess: win32more.Windows.Win32.Foundation.HANDLE, BaseOfDll: UInt64, Mask: win32more.Windows.Win32.Foundation.PSTR, EnumSymbolsCallback: win32more.Windows.Win32.System.Diagnostics.Debug.PSYM_ENUMERATESYMBOLS_CALLBACK, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymEnumSymbolsEx(hProcess: win32more.Windows.Win32.Foundation.HANDLE, BaseOfDll: UInt64, Mask: win32more.Windows.Win32.Foundation.PSTR, EnumSymbolsCallback: win32more.Windows.Win32.System.Diagnostics.Debug.PSYM_ENUMERATESYMBOLS_CALLBACK, UserContext: VoidPtr, Options: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymEnumSymbolsW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, BaseOfDll: UInt64, Mask: win32more.Windows.Win32.Foundation.PWSTR, EnumSymbolsCallback: win32more.Windows.Win32.System.Diagnostics.Debug.PSYM_ENUMERATESYMBOLS_CALLBACKW, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymEnumSymbolsExW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, BaseOfDll: UInt64, Mask: win32more.Windows.Win32.Foundation.PWSTR, EnumSymbolsCallback: win32more.Windows.Win32.System.Diagnostics.Debug.PSYM_ENUMERATESYMBOLS_CALLBACKW, UserContext: VoidPtr, Options: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymEnumSymbolsForAddr(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Address: UInt64, EnumSymbolsCallback: win32more.Windows.Win32.System.Diagnostics.Debug.PSYM_ENUMERATESYMBOLS_CALLBACK, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymEnumSymbolsForAddrW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Address: UInt64, EnumSymbolsCallback: win32more.Windows.Win32.System.Diagnostics.Debug.PSYM_ENUMERATESYMBOLS_CALLBACKW, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymSearch(hProcess: win32more.Windows.Win32.Foundation.HANDLE, BaseOfDll: UInt64, Index: UInt32, SymTag: UInt32, Mask: win32more.Windows.Win32.Foundation.PSTR, Address: UInt64, EnumSymbolsCallback: win32more.Windows.Win32.System.Diagnostics.Debug.PSYM_ENUMERATESYMBOLS_CALLBACK, UserContext: VoidPtr, Options: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymSearchW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, BaseOfDll: UInt64, Index: UInt32, SymTag: UInt32, Mask: win32more.Windows.Win32.Foundation.PWSTR, Address: UInt64, EnumSymbolsCallback: win32more.Windows.Win32.System.Diagnostics.Debug.PSYM_ENUMERATESYMBOLS_CALLBACKW, UserContext: VoidPtr, Options: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetScope(hProcess: win32more.Windows.Win32.Foundation.HANDLE, BaseOfDll: UInt64, Index: UInt32, Symbol: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFO_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetScopeW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, BaseOfDll: UInt64, Index: UInt32, Symbol: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFOW_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymFromIndex(hProcess: win32more.Windows.Win32.Foundation.HANDLE, BaseOfDll: UInt64, Index: UInt32, Symbol: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFO_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymFromIndexW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, BaseOfDll: UInt64, Index: UInt32, Symbol: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFOW_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetTypeInfo(hProcess: win32more.Windows.Win32.Foundation.HANDLE, ModBase: UInt64, TypeId: UInt32, GetType: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL_TYPE_INFO, pInfo: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetTypeInfoEx(hProcess: win32more.Windows.Win32.Foundation.HANDLE, ModBase: UInt64, Params: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_GET_TYPE_INFO_PARAMS_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymEnumTypes(hProcess: win32more.Windows.Win32.Foundation.HANDLE, BaseOfDll: UInt64, EnumSymbolsCallback: win32more.Windows.Win32.System.Diagnostics.Debug.PSYM_ENUMERATESYMBOLS_CALLBACK, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymEnumTypesW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, BaseOfDll: UInt64, EnumSymbolsCallback: win32more.Windows.Win32.System.Diagnostics.Debug.PSYM_ENUMERATESYMBOLS_CALLBACKW, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymEnumTypesByName(hProcess: win32more.Windows.Win32.Foundation.HANDLE, BaseOfDll: UInt64, mask: win32more.Windows.Win32.Foundation.PSTR, EnumSymbolsCallback: win32more.Windows.Win32.System.Diagnostics.Debug.PSYM_ENUMERATESYMBOLS_CALLBACK, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymEnumTypesByNameW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, BaseOfDll: UInt64, mask: win32more.Windows.Win32.Foundation.PWSTR, EnumSymbolsCallback: win32more.Windows.Win32.System.Diagnostics.Debug.PSYM_ENUMERATESYMBOLS_CALLBACKW, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetTypeFromName(hProcess: win32more.Windows.Win32.Foundation.HANDLE, BaseOfDll: UInt64, Name: win32more.Windows.Win32.Foundation.PSTR, Symbol: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFO_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetTypeFromNameW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, BaseOfDll: UInt64, Name: win32more.Windows.Win32.Foundation.PWSTR, Symbol: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFOW_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymAddSymbol(hProcess: win32more.Windows.Win32.Foundation.HANDLE, BaseOfDll: UInt64, Name: win32more.Windows.Win32.Foundation.PSTR, Address: UInt64, Size: UInt32, Flags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymAddSymbolW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, BaseOfDll: UInt64, Name: win32more.Windows.Win32.Foundation.PWSTR, Address: UInt64, Size: UInt32, Flags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymDeleteSymbol(hProcess: win32more.Windows.Win32.Foundation.HANDLE, BaseOfDll: UInt64, Name: win32more.Windows.Win32.Foundation.PSTR, Address: UInt64, Flags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymDeleteSymbolW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, BaseOfDll: UInt64, Name: win32more.Windows.Win32.Foundation.PWSTR, Address: UInt64, Flags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymRefreshModuleList(hProcess: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymAddSourceStream(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Base: UInt64, StreamFile: win32more.Windows.Win32.Foundation.PSTR, Buffer: POINTER(Byte), Size: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymAddSourceStreamA(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Base: UInt64, StreamFile: win32more.Windows.Win32.Foundation.PSTR, Buffer: POINTER(Byte), Size: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymAddSourceStreamW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Base: UInt64, FileSpec: win32more.Windows.Win32.Foundation.PWSTR, Buffer: POINTER(Byte), Size: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymSrvIsStoreW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, path: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymSrvIsStore(hProcess: win32more.Windows.Win32.Foundation.HANDLE, path: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymSrvDeltaName(hProcess: win32more.Windows.Win32.Foundation.HANDLE, SymPath: win32more.Windows.Win32.Foundation.PSTR, Type: win32more.Windows.Win32.Foundation.PSTR, File1: win32more.Windows.Win32.Foundation.PSTR, File2: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.PSTR: ...
@winfunctype('dbghelp.dll')
def SymSrvDeltaNameW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, SymPath: win32more.Windows.Win32.Foundation.PWSTR, Type: win32more.Windows.Win32.Foundation.PWSTR, File1: win32more.Windows.Win32.Foundation.PWSTR, File2: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.PWSTR: ...
@winfunctype('dbghelp.dll')
def SymSrvGetSupplement(hProcess: win32more.Windows.Win32.Foundation.HANDLE, SymPath: win32more.Windows.Win32.Foundation.PSTR, Node: win32more.Windows.Win32.Foundation.PSTR, File: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.PSTR: ...
@winfunctype('dbghelp.dll')
def SymSrvGetSupplementW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, SymPath: win32more.Windows.Win32.Foundation.PWSTR, Node: win32more.Windows.Win32.Foundation.PWSTR, File: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.PWSTR: ...
@winfunctype('dbghelp.dll')
def SymSrvGetFileIndexes(File: win32more.Windows.Win32.Foundation.PSTR, Id: POINTER(Guid), Val1: POINTER(UInt32), Val2: POINTER(UInt32), Flags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymSrvGetFileIndexesW(File: win32more.Windows.Win32.Foundation.PWSTR, Id: POINTER(Guid), Val1: POINTER(UInt32), Val2: POINTER(UInt32), Flags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymSrvGetFileIndexStringW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, SrvPath: win32more.Windows.Win32.Foundation.PWSTR, File: win32more.Windows.Win32.Foundation.PWSTR, Index: win32more.Windows.Win32.Foundation.PWSTR, Size: UIntPtr, Flags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymSrvGetFileIndexString(hProcess: win32more.Windows.Win32.Foundation.HANDLE, SrvPath: win32more.Windows.Win32.Foundation.PSTR, File: win32more.Windows.Win32.Foundation.PSTR, Index: win32more.Windows.Win32.Foundation.PSTR, Size: UIntPtr, Flags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymSrvGetFileIndexInfo(File: win32more.Windows.Win32.Foundation.PSTR, Info: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.SYMSRV_INDEX_INFO_head), Flags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymSrvGetFileIndexInfoW(File: win32more.Windows.Win32.Foundation.PWSTR, Info: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.SYMSRV_INDEX_INFOW_head), Flags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymSrvStoreSupplement(hProcess: win32more.Windows.Win32.Foundation.HANDLE, SrvPath: win32more.Windows.Win32.Foundation.PSTR, Node: win32more.Windows.Win32.Foundation.PSTR, File: win32more.Windows.Win32.Foundation.PSTR, Flags: UInt32) -> win32more.Windows.Win32.Foundation.PSTR: ...
@winfunctype('dbghelp.dll')
def SymSrvStoreSupplementW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, SymPath: win32more.Windows.Win32.Foundation.PWSTR, Node: win32more.Windows.Win32.Foundation.PWSTR, File: win32more.Windows.Win32.Foundation.PWSTR, Flags: UInt32) -> win32more.Windows.Win32.Foundation.PWSTR: ...
@winfunctype('dbghelp.dll')
def SymSrvStoreFile(hProcess: win32more.Windows.Win32.Foundation.HANDLE, SrvPath: win32more.Windows.Win32.Foundation.PSTR, File: win32more.Windows.Win32.Foundation.PSTR, Flags: win32more.Windows.Win32.System.Diagnostics.Debug.SYM_SRV_STORE_FILE_FLAGS) -> win32more.Windows.Win32.Foundation.PSTR: ...
@winfunctype('dbghelp.dll')
def SymSrvStoreFileW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, SrvPath: win32more.Windows.Win32.Foundation.PWSTR, File: win32more.Windows.Win32.Foundation.PWSTR, Flags: win32more.Windows.Win32.System.Diagnostics.Debug.SYM_SRV_STORE_FILE_FLAGS) -> win32more.Windows.Win32.Foundation.PWSTR: ...
@winfunctype('dbghelp.dll')
def SymGetSymbolFile(hProcess: win32more.Windows.Win32.Foundation.HANDLE, SymPath: win32more.Windows.Win32.Foundation.PSTR, ImageFile: win32more.Windows.Win32.Foundation.PSTR, Type: UInt32, SymbolFile: win32more.Windows.Win32.Foundation.PSTR, cSymbolFile: UIntPtr, DbgFile: win32more.Windows.Win32.Foundation.PSTR, cDbgFile: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetSymbolFileW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, SymPath: win32more.Windows.Win32.Foundation.PWSTR, ImageFile: win32more.Windows.Win32.Foundation.PWSTR, Type: UInt32, SymbolFile: win32more.Windows.Win32.Foundation.PWSTR, cSymbolFile: UIntPtr, DbgFile: win32more.Windows.Win32.Foundation.PWSTR, cDbgFile: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def DbgHelpCreateUserDump(FileName: win32more.Windows.Win32.Foundation.PSTR, Callback: win32more.Windows.Win32.System.Diagnostics.Debug.PDBGHELP_CREATE_USER_DUMP_CALLBACK, UserData: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def DbgHelpCreateUserDumpW(FileName: win32more.Windows.Win32.Foundation.PWSTR, Callback: win32more.Windows.Win32.System.Diagnostics.Debug.PDBGHELP_CREATE_USER_DUMP_CALLBACK, UserData: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetSymFromAddr64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, qwAddr: UInt64, pdwDisplacement: POINTER(UInt64), Symbol: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL64_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X86':
    @winfunctype('dbghelp.dll')
    def SymGetSymFromAddr(hProcess: win32more.Windows.Win32.Foundation.HANDLE, dwAddr: UInt32, pdwDisplacement: POINTER(UInt32), Symbol: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetSymFromName64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Name: win32more.Windows.Win32.Foundation.PSTR, Symbol: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL64_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X86':
    @winfunctype('dbghelp.dll')
    def SymGetSymFromName(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Name: win32more.Windows.Win32.Foundation.PSTR, Symbol: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def FindFileInPath(hprocess: win32more.Windows.Win32.Foundation.HANDLE, SearchPathA: win32more.Windows.Win32.Foundation.PSTR, FileName: win32more.Windows.Win32.Foundation.PSTR, id: VoidPtr, two: UInt32, three: UInt32, flags: UInt32, FilePath: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def FindFileInSearchPath(hprocess: win32more.Windows.Win32.Foundation.HANDLE, SearchPathA: win32more.Windows.Win32.Foundation.PSTR, FileName: win32more.Windows.Win32.Foundation.PSTR, one: UInt32, two: UInt32, three: UInt32, FilePath: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymEnumSym(hProcess: win32more.Windows.Win32.Foundation.HANDLE, BaseOfDll: UInt64, EnumSymbolsCallback: win32more.Windows.Win32.System.Diagnostics.Debug.PSYM_ENUMERATESYMBOLS_CALLBACK, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymEnumerateSymbols64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, BaseOfDll: UInt64, EnumSymbolsCallback: win32more.Windows.Win32.System.Diagnostics.Debug.PSYM_ENUMSYMBOLS_CALLBACK64, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymEnumerateSymbolsW64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, BaseOfDll: UInt64, EnumSymbolsCallback: win32more.Windows.Win32.System.Diagnostics.Debug.PSYM_ENUMSYMBOLS_CALLBACK64W, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X86':
    @winfunctype('dbghelp.dll')
    def SymEnumerateSymbols(hProcess: win32more.Windows.Win32.Foundation.HANDLE, BaseOfDll: UInt32, EnumSymbolsCallback: win32more.Windows.Win32.System.Diagnostics.Debug.PSYM_ENUMSYMBOLS_CALLBACK, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X86':
    @winfunctype('dbghelp.dll')
    def SymEnumerateSymbolsW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, BaseOfDll: UInt32, EnumSymbolsCallback: win32more.Windows.Win32.System.Diagnostics.Debug.PSYM_ENUMSYMBOLS_CALLBACKW, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymLoadModule64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, hFile: win32more.Windows.Win32.Foundation.HANDLE, ImageName: win32more.Windows.Win32.Foundation.PSTR, ModuleName: win32more.Windows.Win32.Foundation.PSTR, BaseOfDll: UInt64, SizeOfDll: UInt32) -> UInt64: ...
if ARCH in 'X86':
    @winfunctype('dbghelp.dll')
    def SymLoadModule(hProcess: win32more.Windows.Win32.Foundation.HANDLE, hFile: win32more.Windows.Win32.Foundation.HANDLE, ImageName: win32more.Windows.Win32.Foundation.PSTR, ModuleName: win32more.Windows.Win32.Foundation.PSTR, BaseOfDll: UInt32, SizeOfDll: UInt32) -> UInt32: ...
@winfunctype('dbghelp.dll')
def SymGetSymNext64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Symbol: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL64_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X86':
    @winfunctype('dbghelp.dll')
    def SymGetSymNext(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Symbol: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetSymPrev64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Symbol: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL64_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X86':
    @winfunctype('dbghelp.dll')
    def SymGetSymPrev(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Symbol: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SetCheckUserInterruptShared(lpStartAddress: win32more.Windows.Win32.System.Diagnostics.Debug.LPCALL_BACK_USER_INTERRUPT_ROUTINE) -> Void: ...
@winfunctype('dbghelp.dll')
def GetSymLoadError() -> UInt32: ...
@winfunctype('dbghelp.dll')
def SetSymLoadError(error: UInt32) -> Void: ...
@winfunctype('dbghelp.dll')
def ReportSymbolLoadSummary(hProcess: win32more.Windows.Win32.Foundation.HANDLE, pLoadModule: win32more.Windows.Win32.Foundation.PWSTR, pSymbolData: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.DBGHELP_DATA_REPORT_STRUCT_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def RemoveInvalidModuleList(hProcess: win32more.Windows.Win32.Foundation.HANDLE) -> Void: ...
@winfunctype('dbghelp.dll')
def RangeMapCreate() -> VoidPtr: ...
@winfunctype('dbghelp.dll')
def RangeMapFree(RmapHandle: VoidPtr) -> Void: ...
@winfunctype('dbghelp.dll')
def RangeMapAddPeImageSections(RmapHandle: VoidPtr, ImageName: win32more.Windows.Win32.Foundation.PWSTR, MappedImage: VoidPtr, MappingBytes: UInt32, ImageBase: UInt64, UserTag: UInt64, MappingFlags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def RangeMapRemove(RmapHandle: VoidPtr, UserTag: UInt64) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def RangeMapRead(RmapHandle: VoidPtr, Offset: UInt64, Buffer: VoidPtr, RequestBytes: UInt32, Flags: UInt32, DoneBytes: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def RangeMapWrite(RmapHandle: VoidPtr, Offset: UInt64, Buffer: VoidPtr, RequestBytes: UInt32, Flags: UInt32, DoneBytes: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def MessageBeep(uType: win32more.Windows.Win32.UI.WindowsAndMessaging.MESSAGEBOX_STYLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FatalExit(ExitCode: Int32) -> Void: ...
@winfunctype('KERNEL32.dll')
def GetThreadSelectorEntry(hThread: win32more.Windows.Win32.Foundation.HANDLE, dwSelector: UInt32, lpSelectorEntry: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.LDT_ENTRY_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def Wow64GetThreadSelectorEntry(hThread: win32more.Windows.Win32.Foundation.HANDLE, dwSelector: UInt32, lpSelectorEntry: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.WOW64_LDT_ENTRY_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DebugSetProcessKillOnExit(KillOnExit: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DebugBreakProcess(Process: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FormatMessageA(dwFlags: win32more.Windows.Win32.System.Diagnostics.Debug.FORMAT_MESSAGE_OPTIONS, lpSource: VoidPtr, dwMessageId: UInt32, dwLanguageId: UInt32, lpBuffer: win32more.Windows.Win32.Foundation.PSTR, nSize: UInt32, Arguments: POINTER(POINTER(SByte))) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def FormatMessageW(dwFlags: win32more.Windows.Win32.System.Diagnostics.Debug.FORMAT_MESSAGE_OPTIONS, lpSource: VoidPtr, dwMessageId: UInt32, dwLanguageId: UInt32, lpBuffer: win32more.Windows.Win32.Foundation.PWSTR, nSize: UInt32, Arguments: POINTER(POINTER(SByte))) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def CopyContext(Destination: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_head), ContextFlags: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS, Source: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def InitializeContext(Buffer: VoidPtr, ContextFlags: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS, Context: POINTER(POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_head)), ContextLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def InitializeContext2(Buffer: VoidPtr, ContextFlags: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS, Context: POINTER(POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_head)), ContextLength: POINTER(UInt32), XStateCompactionMask: UInt64) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X86,X64':
    @winfunctype('KERNEL32.dll')
    def GetEnabledXStateFeatures() -> UInt64: ...
if ARCH in 'X86,X64':
    @winfunctype('KERNEL32.dll')
    def GetXStateFeaturesMask(Context: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_head), FeatureMask: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X86,X64':
    @winfunctype('KERNEL32.dll')
    def LocateXStateFeature(Context: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_head), FeatureId: UInt32, Length: POINTER(UInt32)) -> VoidPtr: ...
if ARCH in 'X86,X64':
    @winfunctype('KERNEL32.dll')
    def SetXStateFeaturesMask(Context: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_head), FeatureMask: UInt64) -> win32more.Windows.Win32.Foundation.BOOL: ...
BUGCHECK_ERROR = UInt32
HARDWARE_PROFILE_UNDOCKED_STRING: BUGCHECK_ERROR = 1073807361
HARDWARE_PROFILE_DOCKED_STRING: BUGCHECK_ERROR = 1073807362
HARDWARE_PROFILE_UNKNOWN_STRING: BUGCHECK_ERROR = 1073807363
WINDOWS_NT_BANNER: BUGCHECK_ERROR = 1073741950
WINDOWS_NT_CSD_STRING: BUGCHECK_ERROR = 1073741959
WINDOWS_NT_INFO_STRING: BUGCHECK_ERROR = 1073741960
WINDOWS_NT_MP_STRING: BUGCHECK_ERROR = 1073741961
THREAD_TERMINATE_HELD_MUTEX: BUGCHECK_ERROR = 1073741962
WINDOWS_NT_INFO_STRING_PLURAL: BUGCHECK_ERROR = 1073741981
WINDOWS_NT_RC_STRING: BUGCHECK_ERROR = 1073741982
APC_INDEX_MISMATCH: BUGCHECK_ERROR = 1
DEVICE_QUEUE_NOT_BUSY: BUGCHECK_ERROR = 2
INVALID_AFFINITY_SET: BUGCHECK_ERROR = 3
INVALID_DATA_ACCESS_TRAP: BUGCHECK_ERROR = 4
INVALID_PROCESS_ATTACH_ATTEMPT: BUGCHECK_ERROR = 5
INVALID_PROCESS_DETACH_ATTEMPT: BUGCHECK_ERROR = 6
INVALID_SOFTWARE_INTERRUPT: BUGCHECK_ERROR = 7
IRQL_NOT_DISPATCH_LEVEL: BUGCHECK_ERROR = 8
IRQL_NOT_GREATER_OR_EQUAL: BUGCHECK_ERROR = 9
IRQL_NOT_LESS_OR_EQUAL: BUGCHECK_ERROR = 10
NO_EXCEPTION_HANDLING_SUPPORT: BUGCHECK_ERROR = 11
MAXIMUM_WAIT_OBJECTS_EXCEEDED: BUGCHECK_ERROR = 12
MUTEX_LEVEL_NUMBER_VIOLATION: BUGCHECK_ERROR = 13
NO_USER_MODE_CONTEXT: BUGCHECK_ERROR = 14
SPIN_LOCK_ALREADY_OWNED: BUGCHECK_ERROR = 15
SPIN_LOCK_NOT_OWNED: BUGCHECK_ERROR = 16
THREAD_NOT_MUTEX_OWNER: BUGCHECK_ERROR = 17
TRAP_CAUSE_UNKNOWN: BUGCHECK_ERROR = 18
EMPTY_THREAD_REAPER_LIST: BUGCHECK_ERROR = 19
CREATE_DELETE_LOCK_NOT_LOCKED: BUGCHECK_ERROR = 20
LAST_CHANCE_CALLED_FROM_KMODE: BUGCHECK_ERROR = 21
CID_HANDLE_CREATION: BUGCHECK_ERROR = 22
CID_HANDLE_DELETION: BUGCHECK_ERROR = 23
REFERENCE_BY_POINTER: BUGCHECK_ERROR = 24
BAD_POOL_HEADER: BUGCHECK_ERROR = 25
MEMORY_MANAGEMENT: BUGCHECK_ERROR = 26
PFN_SHARE_COUNT: BUGCHECK_ERROR = 27
PFN_REFERENCE_COUNT: BUGCHECK_ERROR = 28
NO_SPIN_LOCK_AVAILABLE: BUGCHECK_ERROR = 29
KMODE_EXCEPTION_NOT_HANDLED: BUGCHECK_ERROR = 30
SHARED_RESOURCE_CONV_ERROR: BUGCHECK_ERROR = 31
KERNEL_APC_PENDING_DURING_EXIT: BUGCHECK_ERROR = 32
QUOTA_UNDERFLOW: BUGCHECK_ERROR = 33
FILE_SYSTEM: BUGCHECK_ERROR = 34
FAT_FILE_SYSTEM: BUGCHECK_ERROR = 35
NTFS_FILE_SYSTEM: BUGCHECK_ERROR = 36
NPFS_FILE_SYSTEM: BUGCHECK_ERROR = 37
CDFS_FILE_SYSTEM: BUGCHECK_ERROR = 38
RDR_FILE_SYSTEM: BUGCHECK_ERROR = 39
CORRUPT_ACCESS_TOKEN: BUGCHECK_ERROR = 40
SECURITY_SYSTEM: BUGCHECK_ERROR = 41
INCONSISTENT_IRP: BUGCHECK_ERROR = 42
PANIC_STACK_SWITCH: BUGCHECK_ERROR = 43
PORT_DRIVER_INTERNAL: BUGCHECK_ERROR = 44
SCSI_DISK_DRIVER_INTERNAL: BUGCHECK_ERROR = 45
DATA_BUS_ERROR: BUGCHECK_ERROR = 46
INSTRUCTION_BUS_ERROR: BUGCHECK_ERROR = 47
SET_OF_INVALID_CONTEXT: BUGCHECK_ERROR = 48
PHASE0_INITIALIZATION_FAILED: BUGCHECK_ERROR = 49
PHASE1_INITIALIZATION_FAILED: BUGCHECK_ERROR = 50
UNEXPECTED_INITIALIZATION_CALL: BUGCHECK_ERROR = 51
CACHE_MANAGER: BUGCHECK_ERROR = 52
NO_MORE_IRP_STACK_LOCATIONS: BUGCHECK_ERROR = 53
DEVICE_REFERENCE_COUNT_NOT_ZERO: BUGCHECK_ERROR = 54
FLOPPY_INTERNAL_ERROR: BUGCHECK_ERROR = 55
SERIAL_DRIVER_INTERNAL: BUGCHECK_ERROR = 56
SYSTEM_EXIT_OWNED_MUTEX: BUGCHECK_ERROR = 57
SYSTEM_UNWIND_PREVIOUS_USER: BUGCHECK_ERROR = 58
SYSTEM_SERVICE_EXCEPTION: BUGCHECK_ERROR = 59
INTERRUPT_UNWIND_ATTEMPTED: BUGCHECK_ERROR = 60
INTERRUPT_EXCEPTION_NOT_HANDLED: BUGCHECK_ERROR = 61
MULTIPROCESSOR_CONFIGURATION_NOT_SUPPORTED: BUGCHECK_ERROR = 62
NO_MORE_SYSTEM_PTES: BUGCHECK_ERROR = 63
TARGET_MDL_TOO_SMALL: BUGCHECK_ERROR = 64
MUST_SUCCEED_POOL_EMPTY: BUGCHECK_ERROR = 65
ATDISK_DRIVER_INTERNAL: BUGCHECK_ERROR = 66
NO_SUCH_PARTITION: BUGCHECK_ERROR = 67
MULTIPLE_IRP_COMPLETE_REQUESTS: BUGCHECK_ERROR = 68
INSUFFICIENT_SYSTEM_MAP_REGS: BUGCHECK_ERROR = 69
DEREF_UNKNOWN_LOGON_SESSION: BUGCHECK_ERROR = 70
REF_UNKNOWN_LOGON_SESSION: BUGCHECK_ERROR = 71
CANCEL_STATE_IN_COMPLETED_IRP: BUGCHECK_ERROR = 72
PAGE_FAULT_WITH_INTERRUPTS_OFF: BUGCHECK_ERROR = 73
IRQL_GT_ZERO_AT_SYSTEM_SERVICE: BUGCHECK_ERROR = 74
STREAMS_INTERNAL_ERROR: BUGCHECK_ERROR = 75
FATAL_UNHANDLED_HARD_ERROR: BUGCHECK_ERROR = 76
NO_PAGES_AVAILABLE: BUGCHECK_ERROR = 77
PFN_LIST_CORRUPT: BUGCHECK_ERROR = 78
NDIS_INTERNAL_ERROR: BUGCHECK_ERROR = 79
PAGE_FAULT_IN_NONPAGED_AREA: BUGCHECK_ERROR = 80
PAGE_FAULT_IN_NONPAGED_AREA_M: BUGCHECK_ERROR = 268435536
REGISTRY_ERROR: BUGCHECK_ERROR = 81
MAILSLOT_FILE_SYSTEM: BUGCHECK_ERROR = 82
NO_BOOT_DEVICE: BUGCHECK_ERROR = 83
LM_SERVER_INTERNAL_ERROR: BUGCHECK_ERROR = 84
DATA_COHERENCY_EXCEPTION: BUGCHECK_ERROR = 85
INSTRUCTION_COHERENCY_EXCEPTION: BUGCHECK_ERROR = 86
XNS_INTERNAL_ERROR: BUGCHECK_ERROR = 87
VOLMGRX_INTERNAL_ERROR: BUGCHECK_ERROR = 88
PINBALL_FILE_SYSTEM: BUGCHECK_ERROR = 89
CRITICAL_SERVICE_FAILED: BUGCHECK_ERROR = 90
SET_ENV_VAR_FAILED: BUGCHECK_ERROR = 91
HAL_INITIALIZATION_FAILED: BUGCHECK_ERROR = 92
UNSUPPORTED_PROCESSOR: BUGCHECK_ERROR = 93
OBJECT_INITIALIZATION_FAILED: BUGCHECK_ERROR = 94
SECURITY_INITIALIZATION_FAILED: BUGCHECK_ERROR = 95
PROCESS_INITIALIZATION_FAILED: BUGCHECK_ERROR = 96
HAL1_INITIALIZATION_FAILED: BUGCHECK_ERROR = 97
OBJECT1_INITIALIZATION_FAILED: BUGCHECK_ERROR = 98
SECURITY1_INITIALIZATION_FAILED: BUGCHECK_ERROR = 99
SYMBOLIC_INITIALIZATION_FAILED: BUGCHECK_ERROR = 100
MEMORY1_INITIALIZATION_FAILED: BUGCHECK_ERROR = 101
CACHE_INITIALIZATION_FAILED: BUGCHECK_ERROR = 102
CONFIG_INITIALIZATION_FAILED: BUGCHECK_ERROR = 103
FILE_INITIALIZATION_FAILED: BUGCHECK_ERROR = 104
IO1_INITIALIZATION_FAILED: BUGCHECK_ERROR = 105
LPC_INITIALIZATION_FAILED: BUGCHECK_ERROR = 106
PROCESS1_INITIALIZATION_FAILED: BUGCHECK_ERROR = 107
REFMON_INITIALIZATION_FAILED: BUGCHECK_ERROR = 108
SESSION1_INITIALIZATION_FAILED: BUGCHECK_ERROR = 109
BOOTPROC_INITIALIZATION_FAILED: BUGCHECK_ERROR = 110
VSL_INITIALIZATION_FAILED: BUGCHECK_ERROR = 111
SOFT_RESTART_FATAL_ERROR: BUGCHECK_ERROR = 112
ASSIGN_DRIVE_LETTERS_FAILED: BUGCHECK_ERROR = 114
CONFIG_LIST_FAILED: BUGCHECK_ERROR = 115
BAD_SYSTEM_CONFIG_INFO: BUGCHECK_ERROR = 116
CANNOT_WRITE_CONFIGURATION: BUGCHECK_ERROR = 117
PROCESS_HAS_LOCKED_PAGES: BUGCHECK_ERROR = 118
KERNEL_STACK_INPAGE_ERROR: BUGCHECK_ERROR = 119
PHASE0_EXCEPTION: BUGCHECK_ERROR = 120
MISMATCHED_HAL: BUGCHECK_ERROR = 121
KERNEL_DATA_INPAGE_ERROR: BUGCHECK_ERROR = 122
INACCESSIBLE_BOOT_DEVICE: BUGCHECK_ERROR = 123
BUGCODE_NDIS_DRIVER: BUGCHECK_ERROR = 124
INSTALL_MORE_MEMORY: BUGCHECK_ERROR = 125
SYSTEM_THREAD_EXCEPTION_NOT_HANDLED: BUGCHECK_ERROR = 126
SYSTEM_THREAD_EXCEPTION_NOT_HANDLED_M: BUGCHECK_ERROR = 268435582
UNEXPECTED_KERNEL_MODE_TRAP: BUGCHECK_ERROR = 127
UNEXPECTED_KERNEL_MODE_TRAP_M: BUGCHECK_ERROR = 268435583
NMI_HARDWARE_FAILURE: BUGCHECK_ERROR = 128
SPIN_LOCK_INIT_FAILURE: BUGCHECK_ERROR = 129
DFS_FILE_SYSTEM: BUGCHECK_ERROR = 130
OFS_FILE_SYSTEM: BUGCHECK_ERROR = 131
RECOM_DRIVER: BUGCHECK_ERROR = 132
SETUP_FAILURE: BUGCHECK_ERROR = 133
AUDIT_FAILURE: BUGCHECK_ERROR = 134
MBR_CHECKSUM_MISMATCH: BUGCHECK_ERROR = 139
KERNEL_MODE_EXCEPTION_NOT_HANDLED: BUGCHECK_ERROR = 142
KERNEL_MODE_EXCEPTION_NOT_HANDLED_M: BUGCHECK_ERROR = 268435598
PP0_INITIALIZATION_FAILED: BUGCHECK_ERROR = 143
PP1_INITIALIZATION_FAILED: BUGCHECK_ERROR = 144
WIN32K_INIT_OR_RIT_FAILURE: BUGCHECK_ERROR = 145
UP_DRIVER_ON_MP_SYSTEM: BUGCHECK_ERROR = 146
INVALID_KERNEL_HANDLE: BUGCHECK_ERROR = 147
KERNEL_STACK_LOCKED_AT_EXIT: BUGCHECK_ERROR = 148
PNP_INTERNAL_ERROR: BUGCHECK_ERROR = 149
INVALID_WORK_QUEUE_ITEM: BUGCHECK_ERROR = 150
BOUND_IMAGE_UNSUPPORTED: BUGCHECK_ERROR = 151
END_OF_NT_EVALUATION_PERIOD: BUGCHECK_ERROR = 152
INVALID_REGION_OR_SEGMENT: BUGCHECK_ERROR = 153
SYSTEM_LICENSE_VIOLATION: BUGCHECK_ERROR = 154
UDFS_FILE_SYSTEM: BUGCHECK_ERROR = 155
MACHINE_CHECK_EXCEPTION: BUGCHECK_ERROR = 156
USER_MODE_HEALTH_MONITOR: BUGCHECK_ERROR = 158
DRIVER_POWER_STATE_FAILURE: BUGCHECK_ERROR = 159
INTERNAL_POWER_ERROR: BUGCHECK_ERROR = 160
PCI_BUS_DRIVER_INTERNAL: BUGCHECK_ERROR = 161
MEMORY_IMAGE_CORRUPT: BUGCHECK_ERROR = 162
ACPI_DRIVER_INTERNAL: BUGCHECK_ERROR = 163
CNSS_FILE_SYSTEM_FILTER: BUGCHECK_ERROR = 164
ACPI_BIOS_ERROR: BUGCHECK_ERROR = 165
FP_EMULATION_ERROR: BUGCHECK_ERROR = 166
BAD_EXHANDLE: BUGCHECK_ERROR = 167
BOOTING_IN_SAFEMODE_MINIMAL: BUGCHECK_ERROR = 168
BOOTING_IN_SAFEMODE_NETWORK: BUGCHECK_ERROR = 169
BOOTING_IN_SAFEMODE_DSREPAIR: BUGCHECK_ERROR = 170
SESSION_HAS_VALID_POOL_ON_EXIT: BUGCHECK_ERROR = 171
HAL_MEMORY_ALLOCATION: BUGCHECK_ERROR = 172
VIDEO_DRIVER_DEBUG_REPORT_REQUEST: BUGCHECK_ERROR = 1073741997
BGI_DETECTED_VIOLATION: BUGCHECK_ERROR = 177
VIDEO_DRIVER_INIT_FAILURE: BUGCHECK_ERROR = 180
BOOTLOG_LOADED: BUGCHECK_ERROR = 181
BOOTLOG_NOT_LOADED: BUGCHECK_ERROR = 182
BOOTLOG_ENABLED: BUGCHECK_ERROR = 183
ATTEMPTED_SWITCH_FROM_DPC: BUGCHECK_ERROR = 184
CHIPSET_DETECTED_ERROR: BUGCHECK_ERROR = 185
SESSION_HAS_VALID_VIEWS_ON_EXIT: BUGCHECK_ERROR = 186
NETWORK_BOOT_INITIALIZATION_FAILED: BUGCHECK_ERROR = 187
NETWORK_BOOT_DUPLICATE_ADDRESS: BUGCHECK_ERROR = 188
INVALID_HIBERNATED_STATE: BUGCHECK_ERROR = 189
ATTEMPTED_WRITE_TO_READONLY_MEMORY: BUGCHECK_ERROR = 190
MUTEX_ALREADY_OWNED: BUGCHECK_ERROR = 191
PCI_CONFIG_SPACE_ACCESS_FAILURE: BUGCHECK_ERROR = 192
SPECIAL_POOL_DETECTED_MEMORY_CORRUPTION: BUGCHECK_ERROR = 193
BAD_POOL_CALLER: BUGCHECK_ERROR = 194
SYSTEM_IMAGE_BAD_SIGNATURE: BUGCHECK_ERROR = 195
DRIVER_VERIFIER_DETECTED_VIOLATION: BUGCHECK_ERROR = 196
DRIVER_CORRUPTED_EXPOOL: BUGCHECK_ERROR = 197
DRIVER_CAUGHT_MODIFYING_FREED_POOL: BUGCHECK_ERROR = 198
TIMER_OR_DPC_INVALID: BUGCHECK_ERROR = 199
IRQL_UNEXPECTED_VALUE: BUGCHECK_ERROR = 200
DRIVER_VERIFIER_IOMANAGER_VIOLATION: BUGCHECK_ERROR = 201
PNP_DETECTED_FATAL_ERROR: BUGCHECK_ERROR = 202
DRIVER_LEFT_LOCKED_PAGES_IN_PROCESS: BUGCHECK_ERROR = 203
PAGE_FAULT_IN_FREED_SPECIAL_POOL: BUGCHECK_ERROR = 204
PAGE_FAULT_BEYOND_END_OF_ALLOCATION: BUGCHECK_ERROR = 205
DRIVER_UNLOADED_WITHOUT_CANCELLING_PENDING_OPERATIONS: BUGCHECK_ERROR = 206
TERMINAL_SERVER_DRIVER_MADE_INCORRECT_MEMORY_REFERENCE: BUGCHECK_ERROR = 207
DRIVER_CORRUPTED_MMPOOL: BUGCHECK_ERROR = 208
DRIVER_IRQL_NOT_LESS_OR_EQUAL: BUGCHECK_ERROR = 209
BUGCODE_ID_DRIVER: BUGCHECK_ERROR = 210
DRIVER_PORTION_MUST_BE_NONPAGED: BUGCHECK_ERROR = 211
SYSTEM_SCAN_AT_RAISED_IRQL_CAUGHT_IMPROPER_DRIVER_UNLOAD: BUGCHECK_ERROR = 212
DRIVER_PAGE_FAULT_IN_FREED_SPECIAL_POOL: BUGCHECK_ERROR = 213
DRIVER_PAGE_FAULT_BEYOND_END_OF_ALLOCATION: BUGCHECK_ERROR = 214
DRIVER_PAGE_FAULT_BEYOND_END_OF_ALLOCATION_M: BUGCHECK_ERROR = 268435670
DRIVER_UNMAPPING_INVALID_VIEW: BUGCHECK_ERROR = 215
DRIVER_USED_EXCESSIVE_PTES: BUGCHECK_ERROR = 216
LOCKED_PAGES_TRACKER_CORRUPTION: BUGCHECK_ERROR = 217
SYSTEM_PTE_MISUSE: BUGCHECK_ERROR = 218
DRIVER_CORRUPTED_SYSPTES: BUGCHECK_ERROR = 219
DRIVER_INVALID_STACK_ACCESS: BUGCHECK_ERROR = 220
POOL_CORRUPTION_IN_FILE_AREA: BUGCHECK_ERROR = 222
IMPERSONATING_WORKER_THREAD: BUGCHECK_ERROR = 223
ACPI_BIOS_FATAL_ERROR: BUGCHECK_ERROR = 224
WORKER_THREAD_RETURNED_AT_BAD_IRQL: BUGCHECK_ERROR = 225
MANUALLY_INITIATED_CRASH: BUGCHECK_ERROR = 226
RESOURCE_NOT_OWNED: BUGCHECK_ERROR = 227
WORKER_INVALID: BUGCHECK_ERROR = 228
POWER_FAILURE_SIMULATE: BUGCHECK_ERROR = 229
DRIVER_VERIFIER_DMA_VIOLATION: BUGCHECK_ERROR = 230
INVALID_FLOATING_POINT_STATE: BUGCHECK_ERROR = 231
INVALID_CANCEL_OF_FILE_OPEN: BUGCHECK_ERROR = 232
ACTIVE_EX_WORKER_THREAD_TERMINATION: BUGCHECK_ERROR = 233
SAVER_UNSPECIFIED: BUGCHECK_ERROR = 61440
SAVER_BLANKSCREEN: BUGCHECK_ERROR = 61442
SAVER_INPUT: BUGCHECK_ERROR = 61443
SAVER_WATCHDOG: BUGCHECK_ERROR = 61444
SAVER_STARTNOTVISIBLE: BUGCHECK_ERROR = 61445
SAVER_NAVIGATIONMODEL: BUGCHECK_ERROR = 61446
SAVER_OUTOFMEMORY: BUGCHECK_ERROR = 61447
SAVER_GRAPHICS: BUGCHECK_ERROR = 61448
SAVER_NAVSERVERTIMEOUT: BUGCHECK_ERROR = 61449
SAVER_CHROMEPROCESSCRASH: BUGCHECK_ERROR = 61450
SAVER_NOTIFICATIONDISMISSAL: BUGCHECK_ERROR = 61451
SAVER_SPEECHDISMISSAL: BUGCHECK_ERROR = 61452
SAVER_CALLDISMISSAL: BUGCHECK_ERROR = 61453
SAVER_APPBARDISMISSAL: BUGCHECK_ERROR = 61454
SAVER_RILADAPTATIONCRASH: BUGCHECK_ERROR = 61455
SAVER_APPLISTUNREACHABLE: BUGCHECK_ERROR = 61456
SAVER_REPORTNOTIFICATIONFAILURE: BUGCHECK_ERROR = 61457
SAVER_UNEXPECTEDSHUTDOWN: BUGCHECK_ERROR = 61458
SAVER_RPCFAILURE: BUGCHECK_ERROR = 61459
SAVER_AUXILIARYFULLDUMP: BUGCHECK_ERROR = 61460
SAVER_ACCOUNTPROVSVCINITFAILURE: BUGCHECK_ERROR = 61461
SAVER_MTBFCOMMANDTIMEOUT: BUGCHECK_ERROR = 789
SAVER_MTBFCOMMANDHANG: BUGCHECK_ERROR = 61697
SAVER_MTBFPASSBUGCHECK: BUGCHECK_ERROR = 61698
SAVER_MTBFIOERROR: BUGCHECK_ERROR = 61699
SAVER_RENDERTHREADHANG: BUGCHECK_ERROR = 61952
SAVER_RENDERMOBILEUIOOM: BUGCHECK_ERROR = 61953
SAVER_DEVICEUPDATEUNSPECIFIED: BUGCHECK_ERROR = 62208
SAVER_AUDIODRIVERHANG: BUGCHECK_ERROR = 62464
SAVER_BATTERYPULLOUT: BUGCHECK_ERROR = 62720
SAVER_MEDIACORETESTHANG: BUGCHECK_ERROR = 62976
SAVER_RESOURCEMANAGEMENT: BUGCHECK_ERROR = 63232
SAVER_CAPTURESERVICE: BUGCHECK_ERROR = 63488
SAVER_WAITFORSHELLREADY: BUGCHECK_ERROR = 63744
SAVER_NONRESPONSIVEPROCESS: BUGCHECK_ERROR = 404
SAVER_SICKAPPLICATION: BUGCHECK_ERROR = 34918
THREAD_STUCK_IN_DEVICE_DRIVER: BUGCHECK_ERROR = 234
THREAD_STUCK_IN_DEVICE_DRIVER_M: BUGCHECK_ERROR = 268435690
DIRTY_MAPPED_PAGES_CONGESTION: BUGCHECK_ERROR = 235
SESSION_HAS_VALID_SPECIAL_POOL_ON_EXIT: BUGCHECK_ERROR = 236
UNMOUNTABLE_BOOT_VOLUME: BUGCHECK_ERROR = 237
CRITICAL_PROCESS_DIED: BUGCHECK_ERROR = 239
STORAGE_MINIPORT_ERROR: BUGCHECK_ERROR = 240
SCSI_VERIFIER_DETECTED_VIOLATION: BUGCHECK_ERROR = 241
HARDWARE_INTERRUPT_STORM: BUGCHECK_ERROR = 242
DISORDERLY_SHUTDOWN: BUGCHECK_ERROR = 243
CRITICAL_OBJECT_TERMINATION: BUGCHECK_ERROR = 244
FLTMGR_FILE_SYSTEM: BUGCHECK_ERROR = 245
PCI_VERIFIER_DETECTED_VIOLATION: BUGCHECK_ERROR = 246
DRIVER_OVERRAN_STACK_BUFFER: BUGCHECK_ERROR = 247
RAMDISK_BOOT_INITIALIZATION_FAILED: BUGCHECK_ERROR = 248
DRIVER_RETURNED_STATUS_REPARSE_FOR_VOLUME_OPEN: BUGCHECK_ERROR = 249
HTTP_DRIVER_CORRUPTED: BUGCHECK_ERROR = 250
RECURSIVE_MACHINE_CHECK: BUGCHECK_ERROR = 251
ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY: BUGCHECK_ERROR = 252
DIRTY_NOWRITE_PAGES_CONGESTION: BUGCHECK_ERROR = 253
BUGCODE_USB_DRIVER: BUGCHECK_ERROR = 254
BC_BLUETOOTH_VERIFIER_FAULT: BUGCHECK_ERROR = 3070
BC_BTHMINI_VERIFIER_FAULT: BUGCHECK_ERROR = 3071
RESERVE_QUEUE_OVERFLOW: BUGCHECK_ERROR = 255
LOADER_BLOCK_MISMATCH: BUGCHECK_ERROR = 256
CLOCK_WATCHDOG_TIMEOUT: BUGCHECK_ERROR = 257
DPC_WATCHDOG_TIMEOUT: BUGCHECK_ERROR = 258
MUP_FILE_SYSTEM: BUGCHECK_ERROR = 259
AGP_INVALID_ACCESS: BUGCHECK_ERROR = 260
AGP_GART_CORRUPTION: BUGCHECK_ERROR = 261
AGP_ILLEGALLY_REPROGRAMMED: BUGCHECK_ERROR = 262
KERNEL_EXPAND_STACK_ACTIVE: BUGCHECK_ERROR = 263
THIRD_PARTY_FILE_SYSTEM_FAILURE: BUGCHECK_ERROR = 264
CRITICAL_STRUCTURE_CORRUPTION: BUGCHECK_ERROR = 265
APP_TAGGING_INITIALIZATION_FAILED: BUGCHECK_ERROR = 266
DFSC_FILE_SYSTEM: BUGCHECK_ERROR = 267
FSRTL_EXTRA_CREATE_PARAMETER_VIOLATION: BUGCHECK_ERROR = 268
WDF_VIOLATION: BUGCHECK_ERROR = 269
VIDEO_MEMORY_MANAGEMENT_INTERNAL: BUGCHECK_ERROR = 270
DRIVER_INVALID_CRUNTIME_PARAMETER: BUGCHECK_ERROR = 272
RECURSIVE_NMI: BUGCHECK_ERROR = 273
MSRPC_STATE_VIOLATION: BUGCHECK_ERROR = 274
VIDEO_DXGKRNL_FATAL_ERROR: BUGCHECK_ERROR = 275
VIDEO_SHADOW_DRIVER_FATAL_ERROR: BUGCHECK_ERROR = 276
AGP_INTERNAL: BUGCHECK_ERROR = 277
VIDEO_TDR_FAILURE: BUGCHECK_ERROR = 278
VIDEO_TDR_TIMEOUT_DETECTED: BUGCHECK_ERROR = 279
NTHV_GUEST_ERROR: BUGCHECK_ERROR = 280
VIDEO_SCHEDULER_INTERNAL_ERROR: BUGCHECK_ERROR = 281
EM_INITIALIZATION_ERROR: BUGCHECK_ERROR = 282
DRIVER_RETURNED_HOLDING_CANCEL_LOCK: BUGCHECK_ERROR = 283
ATTEMPTED_WRITE_TO_CM_PROTECTED_STORAGE: BUGCHECK_ERROR = 284
EVENT_TRACING_FATAL_ERROR: BUGCHECK_ERROR = 285
TOO_MANY_RECURSIVE_FAULTS: BUGCHECK_ERROR = 286
INVALID_DRIVER_HANDLE: BUGCHECK_ERROR = 287
BITLOCKER_FATAL_ERROR: BUGCHECK_ERROR = 288
DRIVER_VIOLATION: BUGCHECK_ERROR = 289
WHEA_INTERNAL_ERROR: BUGCHECK_ERROR = 290
CRYPTO_SELF_TEST_FAILURE: BUGCHECK_ERROR = 291
WHEA_UNCORRECTABLE_ERROR: BUGCHECK_ERROR = 292
NMR_INVALID_STATE: BUGCHECK_ERROR = 293
NETIO_INVALID_POOL_CALLER: BUGCHECK_ERROR = 294
PAGE_NOT_ZERO: BUGCHECK_ERROR = 295
WORKER_THREAD_RETURNED_WITH_BAD_IO_PRIORITY: BUGCHECK_ERROR = 296
WORKER_THREAD_RETURNED_WITH_BAD_PAGING_IO_PRIORITY: BUGCHECK_ERROR = 297
MUI_NO_VALID_SYSTEM_LANGUAGE: BUGCHECK_ERROR = 298
FAULTY_HARDWARE_CORRUPTED_PAGE: BUGCHECK_ERROR = 299
EXFAT_FILE_SYSTEM: BUGCHECK_ERROR = 300
VOLSNAP_OVERLAPPED_TABLE_ACCESS: BUGCHECK_ERROR = 301
INVALID_MDL_RANGE: BUGCHECK_ERROR = 302
VHD_BOOT_INITIALIZATION_FAILED: BUGCHECK_ERROR = 303
DYNAMIC_ADD_PROCESSOR_MISMATCH: BUGCHECK_ERROR = 304
INVALID_EXTENDED_PROCESSOR_STATE: BUGCHECK_ERROR = 305
RESOURCE_OWNER_POINTER_INVALID: BUGCHECK_ERROR = 306
DPC_WATCHDOG_VIOLATION: BUGCHECK_ERROR = 307
DRIVE_EXTENDER: BUGCHECK_ERROR = 308
REGISTRY_FILTER_DRIVER_EXCEPTION: BUGCHECK_ERROR = 309
VHD_BOOT_HOST_VOLUME_NOT_ENOUGH_SPACE: BUGCHECK_ERROR = 310
WIN32K_HANDLE_MANAGER: BUGCHECK_ERROR = 311
GPIO_CONTROLLER_DRIVER_ERROR: BUGCHECK_ERROR = 312
KERNEL_SECURITY_CHECK_FAILURE: BUGCHECK_ERROR = 313
KERNEL_MODE_HEAP_CORRUPTION: BUGCHECK_ERROR = 314
PASSIVE_INTERRUPT_ERROR: BUGCHECK_ERROR = 315
INVALID_IO_BOOST_STATE: BUGCHECK_ERROR = 316
CRITICAL_INITIALIZATION_FAILURE: BUGCHECK_ERROR = 317
ERRATA_WORKAROUND_UNSUCCESSFUL: BUGCHECK_ERROR = 318
REGISTRY_CALLBACK_DRIVER_EXCEPTION: BUGCHECK_ERROR = 319
STORAGE_DEVICE_ABNORMALITY_DETECTED: BUGCHECK_ERROR = 320
VIDEO_ENGINE_TIMEOUT_DETECTED: BUGCHECK_ERROR = 321
VIDEO_TDR_APPLICATION_BLOCKED: BUGCHECK_ERROR = 322
PROCESSOR_DRIVER_INTERNAL: BUGCHECK_ERROR = 323
BUGCODE_USB3_DRIVER: BUGCHECK_ERROR = 324
SECURE_BOOT_VIOLATION: BUGCHECK_ERROR = 325
NDIS_NET_BUFFER_LIST_INFO_ILLEGALLY_TRANSFERRED: BUGCHECK_ERROR = 326
ABNORMAL_RESET_DETECTED: BUGCHECK_ERROR = 327
IO_OBJECT_INVALID: BUGCHECK_ERROR = 328
REFS_FILE_SYSTEM: BUGCHECK_ERROR = 329
KERNEL_WMI_INTERNAL: BUGCHECK_ERROR = 330
SOC_SUBSYSTEM_FAILURE: BUGCHECK_ERROR = 331
FATAL_ABNORMAL_RESET_ERROR: BUGCHECK_ERROR = 332
EXCEPTION_SCOPE_INVALID: BUGCHECK_ERROR = 333
SOC_CRITICAL_DEVICE_REMOVED: BUGCHECK_ERROR = 334
PDC_WATCHDOG_TIMEOUT: BUGCHECK_ERROR = 335
TCPIP_AOAC_NIC_ACTIVE_REFERENCE_LEAK: BUGCHECK_ERROR = 336
UNSUPPORTED_INSTRUCTION_MODE: BUGCHECK_ERROR = 337
INVALID_PUSH_LOCK_FLAGS: BUGCHECK_ERROR = 338
KERNEL_LOCK_ENTRY_LEAKED_ON_THREAD_TERMINATION: BUGCHECK_ERROR = 339
UNEXPECTED_STORE_EXCEPTION: BUGCHECK_ERROR = 340
OS_DATA_TAMPERING: BUGCHECK_ERROR = 341
WINSOCK_DETECTED_HUNG_CLOSESOCKET_LIVEDUMP: BUGCHECK_ERROR = 342
KERNEL_THREAD_PRIORITY_FLOOR_VIOLATION: BUGCHECK_ERROR = 343
ILLEGAL_IOMMU_PAGE_FAULT: BUGCHECK_ERROR = 344
HAL_ILLEGAL_IOMMU_PAGE_FAULT: BUGCHECK_ERROR = 345
SDBUS_INTERNAL_ERROR: BUGCHECK_ERROR = 346
WORKER_THREAD_RETURNED_WITH_SYSTEM_PAGE_PRIORITY_ACTIVE: BUGCHECK_ERROR = 347
PDC_WATCHDOG_TIMEOUT_LIVEDUMP: BUGCHECK_ERROR = 348
SOC_SUBSYSTEM_FAILURE_LIVEDUMP: BUGCHECK_ERROR = 349
BUGCODE_NDIS_DRIVER_LIVE_DUMP: BUGCHECK_ERROR = 350
CONNECTED_STANDBY_WATCHDOG_TIMEOUT_LIVEDUMP: BUGCHECK_ERROR = 351
WIN32K_ATOMIC_CHECK_FAILURE: BUGCHECK_ERROR = 352
LIVE_SYSTEM_DUMP: BUGCHECK_ERROR = 353
KERNEL_AUTO_BOOST_INVALID_LOCK_RELEASE: BUGCHECK_ERROR = 354
WORKER_THREAD_TEST_CONDITION: BUGCHECK_ERROR = 355
WIN32K_CRITICAL_FAILURE: BUGCHECK_ERROR = 356
CLUSTER_CSV_STATUS_IO_TIMEOUT_LIVEDUMP: BUGCHECK_ERROR = 357
CLUSTER_RESOURCE_CALL_TIMEOUT_LIVEDUMP: BUGCHECK_ERROR = 358
CLUSTER_CSV_SNAPSHOT_DEVICE_INFO_TIMEOUT_LIVEDUMP: BUGCHECK_ERROR = 359
CLUSTER_CSV_STATE_TRANSITION_TIMEOUT_LIVEDUMP: BUGCHECK_ERROR = 360
CLUSTER_CSV_VOLUME_ARRIVAL_LIVEDUMP: BUGCHECK_ERROR = 361
CLUSTER_CSV_VOLUME_REMOVAL_LIVEDUMP: BUGCHECK_ERROR = 362
CLUSTER_CSV_CLUSTER_WATCHDOG_LIVEDUMP: BUGCHECK_ERROR = 363
INVALID_RUNDOWN_PROTECTION_FLAGS: BUGCHECK_ERROR = 364
INVALID_SLOT_ALLOCATOR_FLAGS: BUGCHECK_ERROR = 365
ERESOURCE_INVALID_RELEASE: BUGCHECK_ERROR = 366
CLUSTER_CSV_STATE_TRANSITION_INTERVAL_TIMEOUT_LIVEDUMP: BUGCHECK_ERROR = 367
CLUSTER_CSV_CLUSSVC_DISCONNECT_WATCHDOG: BUGCHECK_ERROR = 368
CRYPTO_LIBRARY_INTERNAL_ERROR: BUGCHECK_ERROR = 369
COREMSGCALL_INTERNAL_ERROR: BUGCHECK_ERROR = 371
COREMSG_INTERNAL_ERROR: BUGCHECK_ERROR = 372
PREVIOUS_FATAL_ABNORMAL_RESET_ERROR: BUGCHECK_ERROR = 373
ELAM_DRIVER_DETECTED_FATAL_ERROR: BUGCHECK_ERROR = 376
CLUSTER_CLUSPORT_STATUS_IO_TIMEOUT_LIVEDUMP: BUGCHECK_ERROR = 377
PROFILER_CONFIGURATION_ILLEGAL: BUGCHECK_ERROR = 379
PDC_LOCK_WATCHDOG_LIVEDUMP: BUGCHECK_ERROR = 380
PDC_UNEXPECTED_REVOCATION_LIVEDUMP: BUGCHECK_ERROR = 381
MICROCODE_REVISION_MISMATCH: BUGCHECK_ERROR = 382
HYPERGUARD_INITIALIZATION_FAILURE: BUGCHECK_ERROR = 383
WVR_LIVEDUMP_REPLICATION_IOCONTEXT_TIMEOUT: BUGCHECK_ERROR = 384
WVR_LIVEDUMP_STATE_TRANSITION_TIMEOUT: BUGCHECK_ERROR = 385
WVR_LIVEDUMP_RECOVERY_IOCONTEXT_TIMEOUT: BUGCHECK_ERROR = 386
WVR_LIVEDUMP_APP_IO_TIMEOUT: BUGCHECK_ERROR = 387
WVR_LIVEDUMP_MANUALLY_INITIATED: BUGCHECK_ERROR = 388
WVR_LIVEDUMP_STATE_FAILURE: BUGCHECK_ERROR = 389
WVR_LIVEDUMP_CRITICAL_ERROR: BUGCHECK_ERROR = 390
VIDEO_DWMINIT_TIMEOUT_FALLBACK_BDD: BUGCHECK_ERROR = 391
CLUSTER_CSVFS_LIVEDUMP: BUGCHECK_ERROR = 392
BAD_OBJECT_HEADER: BUGCHECK_ERROR = 393
SILO_CORRUPT: BUGCHECK_ERROR = 394
SECURE_KERNEL_ERROR: BUGCHECK_ERROR = 395
HYPERGUARD_VIOLATION: BUGCHECK_ERROR = 396
SECURE_FAULT_UNHANDLED: BUGCHECK_ERROR = 397
KERNEL_PARTITION_REFERENCE_VIOLATION: BUGCHECK_ERROR = 398
SYNTHETIC_EXCEPTION_UNHANDLED: BUGCHECK_ERROR = 399
WIN32K_CRITICAL_FAILURE_LIVEDUMP: BUGCHECK_ERROR = 400
PF_DETECTED_CORRUPTION: BUGCHECK_ERROR = 401
KERNEL_AUTO_BOOST_LOCK_ACQUISITION_WITH_RAISED_IRQL: BUGCHECK_ERROR = 402
VIDEO_DXGKRNL_LIVEDUMP: BUGCHECK_ERROR = 403
KERNEL_STORAGE_SLOT_IN_USE: BUGCHECK_ERROR = 409
SMB_SERVER_LIVEDUMP: BUGCHECK_ERROR = 405
LOADER_ROLLBACK_DETECTED: BUGCHECK_ERROR = 406
WIN32K_SECURITY_FAILURE: BUGCHECK_ERROR = 407
UFX_LIVEDUMP: BUGCHECK_ERROR = 408
WORKER_THREAD_RETURNED_WHILE_ATTACHED_TO_SILO: BUGCHECK_ERROR = 410
TTM_FATAL_ERROR: BUGCHECK_ERROR = 411
WIN32K_POWER_WATCHDOG_TIMEOUT: BUGCHECK_ERROR = 412
CLUSTER_SVHDX_LIVEDUMP: BUGCHECK_ERROR = 413
BUGCODE_NETADAPTER_DRIVER: BUGCHECK_ERROR = 414
PDC_PRIVILEGE_CHECK_LIVEDUMP: BUGCHECK_ERROR = 415
TTM_WATCHDOG_TIMEOUT: BUGCHECK_ERROR = 416
WIN32K_CALLOUT_WATCHDOG_LIVEDUMP: BUGCHECK_ERROR = 417
WIN32K_CALLOUT_WATCHDOG_BUGCHECK: BUGCHECK_ERROR = 418
CALL_HAS_NOT_RETURNED_WATCHDOG_TIMEOUT_LIVEDUMP: BUGCHECK_ERROR = 419
DRIPS_SW_HW_DIVERGENCE_LIVEDUMP: BUGCHECK_ERROR = 420
USB_DRIPS_BLOCKER_SURPRISE_REMOVAL_LIVEDUMP: BUGCHECK_ERROR = 421
BLUETOOTH_ERROR_RECOVERY_LIVEDUMP: BUGCHECK_ERROR = 422
SMB_REDIRECTOR_LIVEDUMP: BUGCHECK_ERROR = 423
VIDEO_DXGKRNL_BLACK_SCREEN_LIVEDUMP: BUGCHECK_ERROR = 424
DIRECTED_FX_TRANSITION_LIVEDUMP: BUGCHECK_ERROR = 425
EXCEPTION_ON_INVALID_STACK: BUGCHECK_ERROR = 426
UNWIND_ON_INVALID_STACK: BUGCHECK_ERROR = 427
VIDEO_MINIPORT_FAILED_LIVEDUMP: BUGCHECK_ERROR = 432
VIDEO_MINIPORT_BLACK_SCREEN_LIVEDUMP: BUGCHECK_ERROR = 440
DRIVER_VERIFIER_DETECTED_VIOLATION_LIVEDUMP: BUGCHECK_ERROR = 452
IO_THREADPOOL_DEADLOCK_LIVEDUMP: BUGCHECK_ERROR = 453
FAST_ERESOURCE_PRECONDITION_VIOLATION: BUGCHECK_ERROR = 454
STORE_DATA_STRUCTURE_CORRUPTION: BUGCHECK_ERROR = 455
MANUALLY_INITIATED_POWER_BUTTON_HOLD: BUGCHECK_ERROR = 456
USER_MODE_HEALTH_MONITOR_LIVEDUMP: BUGCHECK_ERROR = 457
SYNTHETIC_WATCHDOG_TIMEOUT: BUGCHECK_ERROR = 458
INVALID_SILO_DETACH: BUGCHECK_ERROR = 459
EXRESOURCE_TIMEOUT_LIVEDUMP: BUGCHECK_ERROR = 460
INVALID_CALLBACK_STACK_ADDRESS: BUGCHECK_ERROR = 461
INVALID_KERNEL_STACK_ADDRESS: BUGCHECK_ERROR = 462
HARDWARE_WATCHDOG_TIMEOUT: BUGCHECK_ERROR = 463
ACPI_FIRMWARE_WATCHDOG_TIMEOUT: BUGCHECK_ERROR = 464
TELEMETRY_ASSERTS_LIVEDUMP: BUGCHECK_ERROR = 465
WORKER_THREAD_INVALID_STATE: BUGCHECK_ERROR = 466
WFP_INVALID_OPERATION: BUGCHECK_ERROR = 467
UCMUCSI_LIVEDUMP: BUGCHECK_ERROR = 468
DRIVER_PNP_WATCHDOG: BUGCHECK_ERROR = 469
WORKER_THREAD_RETURNED_WITH_NON_DEFAULT_WORKLOAD_CLASS: BUGCHECK_ERROR = 470
EFS_FATAL_ERROR: BUGCHECK_ERROR = 471
UCMUCSI_FAILURE: BUGCHECK_ERROR = 472
HAL_IOMMU_INTERNAL_ERROR: BUGCHECK_ERROR = 473
HAL_BLOCKED_PROCESSOR_INTERNAL_ERROR: BUGCHECK_ERROR = 474
IPI_WATCHDOG_TIMEOUT: BUGCHECK_ERROR = 475
DMA_COMMON_BUFFER_VECTOR_ERROR: BUGCHECK_ERROR = 476
BUGCODE_MBBADAPTER_DRIVER: BUGCHECK_ERROR = 477
BUGCODE_WIFIADAPTER_DRIVER: BUGCHECK_ERROR = 478
PROCESSOR_START_TIMEOUT: BUGCHECK_ERROR = 479
INVALID_ALTERNATE_SYSTEM_CALL_HANDLER_REGISTRATION: BUGCHECK_ERROR = 480
DEVICE_DIAGNOSTIC_LOG_LIVEDUMP: BUGCHECK_ERROR = 481
AZURE_DEVICE_FW_DUMP: BUGCHECK_ERROR = 482
BREAKAWAY_CABLE_TRANSITION: BUGCHECK_ERROR = 483
VIDEO_DXGKRNL_SYSMM_FATAL_ERROR: BUGCHECK_ERROR = 484
DRIVER_VERIFIER_TRACKING_LIVE_DUMP: BUGCHECK_ERROR = 485
CRASHDUMP_WATCHDOG_TIMEOUT: BUGCHECK_ERROR = 486
REGISTRY_LIVE_DUMP: BUGCHECK_ERROR = 487
INVALID_THREAD_AFFINITY_STATE: BUGCHECK_ERROR = 488
ILLEGAL_ATS_INITIALIZATION: BUGCHECK_ERROR = 489
SECURE_PCI_CONFIG_SPACE_ACCESS_VIOLATION: BUGCHECK_ERROR = 490
DAM_WATCHDOG_TIMEOUT: BUGCHECK_ERROR = 491
HANDLE_LIVE_DUMP: BUGCHECK_ERROR = 492
HANDLE_ERROR_ON_CRITICAL_THREAD: BUGCHECK_ERROR = 493
MPSDRV_QUERY_USER: BUGCHECK_ERROR = 1073742318
VMBUS_LIVEDUMP: BUGCHECK_ERROR = 1073742319
USB4_HARDWARE_VIOLATION: BUGCHECK_ERROR = 496
KASAN_ENLIGHTENMENT_VIOLATION: BUGCHECK_ERROR = 497
KASAN_ILLEGAL_ACCESS: BUGCHECK_ERROR = 498
IORING: BUGCHECK_ERROR = 499
MDL_CACHE: BUGCHECK_ERROR = 500
MISALIGNED_POINTER_PARAMETER: BUGCHECK_ERROR = 502
XBOX_VMCTRL_CS_TIMEOUT: BUGCHECK_ERROR = 854
XBOX_CORRUPTED_IMAGE: BUGCHECK_ERROR = 855
XBOX_INVERTED_FUNCTION_TABLE_OVERFLOW: BUGCHECK_ERROR = 856
XBOX_CORRUPTED_IMAGE_BASE: BUGCHECK_ERROR = 857
XBOX_XDS_WATCHDOG_TIMEOUT: BUGCHECK_ERROR = 858
XBOX_SHUTDOWN_WATCHDOG_TIMEOUT: BUGCHECK_ERROR = 859
XBOX_360_SYSTEM_CRASH: BUGCHECK_ERROR = 864
XBOX_360_SYSTEM_CRASH_RESERVED: BUGCHECK_ERROR = 1056
XBOX_SECURITY_FAILUE: BUGCHECK_ERROR = 1057
KERNEL_CFG_INIT_FAILURE: BUGCHECK_ERROR = 1058
MANUALLY_INITIATED_POWER_BUTTON_HOLD_LIVE_DUMP: BUGCHECK_ERROR = 4552
HYPERVISOR_ERROR: BUGCHECK_ERROR = 131073
XBOX_MANUALLY_INITIATED_CRASH: BUGCHECK_ERROR = 196614
MANUALLY_INITIATED_BLACKSCREEN_HOTKEY_LIVE_DUMP: BUGCHECK_ERROR = 8648
WINLOGON_FATAL_ERROR: BUGCHECK_ERROR = 3221226010
MANUALLY_INITIATED_CRASH1: BUGCHECK_ERROR = 3735936685
BUGCHECK_CONTEXT_MODIFIER: BUGCHECK_ERROR = 2147483648
if ARCH in 'ARM64':
    class CONTEXT(EasyCastStructure):
        ContextFlags: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS
        Cpsr: UInt32
        Anonymous: _Anonymous_e__Union
        Sp: UInt64
        Pc: UInt64
        V: win32more.Windows.Win32.System.Diagnostics.Debug.ARM64_NT_NEON128 * 32
        Fpcr: UInt32
        Fpsr: UInt32
        Bcr: UInt32 * 8
        Bvr: UInt64 * 8
        Wcr: UInt32 * 2
        Wvr: UInt64 * 2
        class _Anonymous_e__Union(EasyCastUnion):
            Anonymous: _Anonymous_e__Struct
            X: UInt64 * 31
            class _Anonymous_e__Struct(EasyCastStructure):
                X0: UInt64
                X1: UInt64
                X2: UInt64
                X3: UInt64
                X4: UInt64
                X5: UInt64
                X6: UInt64
                X7: UInt64
                X8: UInt64
                X9: UInt64
                X10: UInt64
                X11: UInt64
                X12: UInt64
                X13: UInt64
                X14: UInt64
                X15: UInt64
                X16: UInt64
                X17: UInt64
                X18: UInt64
                X19: UInt64
                X20: UInt64
                X21: UInt64
                X22: UInt64
                X23: UInt64
                X24: UInt64
                X25: UInt64
                X26: UInt64
                X27: UInt64
                X28: UInt64
                Fp: UInt64
                Lr: UInt64
if ARCH in 'X64':
    class CONTEXT(EasyCastStructure):
        P1Home: UInt64
        P2Home: UInt64
        P3Home: UInt64
        P4Home: UInt64
        P5Home: UInt64
        P6Home: UInt64
        ContextFlags: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS
        MxCsr: UInt32
        SegCs: UInt16
        SegDs: UInt16
        SegEs: UInt16
        SegFs: UInt16
        SegGs: UInt16
        SegSs: UInt16
        EFlags: UInt32
        Dr0: UInt64
        Dr1: UInt64
        Dr2: UInt64
        Dr3: UInt64
        Dr6: UInt64
        Dr7: UInt64
        Rax: UInt64
        Rcx: UInt64
        Rdx: UInt64
        Rbx: UInt64
        Rsp: UInt64
        Rbp: UInt64
        Rsi: UInt64
        Rdi: UInt64
        R8: UInt64
        R9: UInt64
        R10: UInt64
        R11: UInt64
        R12: UInt64
        R13: UInt64
        R14: UInt64
        R15: UInt64
        Rip: UInt64
        Anonymous: _Anonymous_e__Union
        VectorRegister: win32more.Windows.Win32.System.Diagnostics.Debug.M128A * 26
        VectorControl: UInt64
        DebugControl: UInt64
        LastBranchToRip: UInt64
        LastBranchFromRip: UInt64
        LastExceptionToRip: UInt64
        LastExceptionFromRip: UInt64
        class _Anonymous_e__Union(EasyCastUnion):
            FltSave: win32more.Windows.Win32.System.Diagnostics.Debug.XSAVE_FORMAT
            Anonymous: _Anonymous_e__Struct
            class _Anonymous_e__Struct(EasyCastStructure):
                Header: win32more.Windows.Win32.System.Diagnostics.Debug.M128A * 2
                Legacy: win32more.Windows.Win32.System.Diagnostics.Debug.M128A * 8
                Xmm0: win32more.Windows.Win32.System.Diagnostics.Debug.M128A
                Xmm1: win32more.Windows.Win32.System.Diagnostics.Debug.M128A
                Xmm2: win32more.Windows.Win32.System.Diagnostics.Debug.M128A
                Xmm3: win32more.Windows.Win32.System.Diagnostics.Debug.M128A
                Xmm4: win32more.Windows.Win32.System.Diagnostics.Debug.M128A
                Xmm5: win32more.Windows.Win32.System.Diagnostics.Debug.M128A
                Xmm6: win32more.Windows.Win32.System.Diagnostics.Debug.M128A
                Xmm7: win32more.Windows.Win32.System.Diagnostics.Debug.M128A
                Xmm8: win32more.Windows.Win32.System.Diagnostics.Debug.M128A
                Xmm9: win32more.Windows.Win32.System.Diagnostics.Debug.M128A
                Xmm10: win32more.Windows.Win32.System.Diagnostics.Debug.M128A
                Xmm11: win32more.Windows.Win32.System.Diagnostics.Debug.M128A
                Xmm12: win32more.Windows.Win32.System.Diagnostics.Debug.M128A
                Xmm13: win32more.Windows.Win32.System.Diagnostics.Debug.M128A
                Xmm14: win32more.Windows.Win32.System.Diagnostics.Debug.M128A
                Xmm15: win32more.Windows.Win32.System.Diagnostics.Debug.M128A
if ARCH in 'X86':
    class CONTEXT(EasyCastStructure):
        ContextFlags: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS
        Dr0: UInt32
        Dr1: UInt32
        Dr2: UInt32
        Dr3: UInt32
        Dr6: UInt32
        Dr7: UInt32
        FloatSave: win32more.Windows.Win32.System.Kernel.FLOATING_SAVE_AREA
        SegGs: UInt32
        SegFs: UInt32
        SegEs: UInt32
        SegDs: UInt32
        Edi: UInt32
        Esi: UInt32
        Ebx: UInt32
        Edx: UInt32
        Ecx: UInt32
        Eax: UInt32
        Ebp: UInt32
        Eip: UInt32
        SegCs: UInt32
        EFlags: UInt32
        Esp: UInt32
        SegSs: UInt32
        ExtendedRegisters: Byte * 512
CONTEXT_FLAGS = UInt32
CONTEXT_AMD64: CONTEXT_FLAGS = 1048576
CONTEXT_CONTROL_AMD64: CONTEXT_FLAGS = 1048577
CONTEXT_INTEGER_AMD64: CONTEXT_FLAGS = 1048578
CONTEXT_SEGMENTS_AMD64: CONTEXT_FLAGS = 1048580
CONTEXT_FLOATING_POINT_AMD64: CONTEXT_FLAGS = 1048584
CONTEXT_DEBUG_REGISTERS_AMD64: CONTEXT_FLAGS = 1048592
CONTEXT_FULL_AMD64: CONTEXT_FLAGS = 1048587
CONTEXT_ALL_AMD64: CONTEXT_FLAGS = 1048607
CONTEXT_XSTATE_AMD64: CONTEXT_FLAGS = 1048640
CONTEXT_KERNEL_CET_AMD64: CONTEXT_FLAGS = 1048704
CONTEXT_KERNEL_DEBUGGER_AMD64: CONTEXT_FLAGS = 67108864
CONTEXT_EXCEPTION_ACTIVE_AMD64: CONTEXT_FLAGS = 134217728
CONTEXT_SERVICE_ACTIVE_AMD64: CONTEXT_FLAGS = 268435456
CONTEXT_EXCEPTION_REQUEST_AMD64: CONTEXT_FLAGS = 1073741824
CONTEXT_EXCEPTION_REPORTING_AMD64: CONTEXT_FLAGS = 2147483648
CONTEXT_UNWOUND_TO_CALL_AMD64: CONTEXT_FLAGS = 536870912
CONTEXT_X86: CONTEXT_FLAGS = 65536
CONTEXT_CONTROL_X86: CONTEXT_FLAGS = 65537
CONTEXT_INTEGER_X86: CONTEXT_FLAGS = 65538
CONTEXT_SEGMENTS_X86: CONTEXT_FLAGS = 65540
CONTEXT_FLOATING_POINT_X86: CONTEXT_FLAGS = 65544
CONTEXT_DEBUG_REGISTERS_X86: CONTEXT_FLAGS = 65552
CONTEXT_EXTENDED_REGISTERS_X86: CONTEXT_FLAGS = 65568
CONTEXT_FULL_X86: CONTEXT_FLAGS = 65543
CONTEXT_ALL_X86: CONTEXT_FLAGS = 65599
CONTEXT_XSTATE_X86: CONTEXT_FLAGS = 65600
CONTEXT_EXCEPTION_ACTIVE_X86: CONTEXT_FLAGS = 134217728
CONTEXT_SERVICE_ACTIVE_X86: CONTEXT_FLAGS = 268435456
CONTEXT_EXCEPTION_REQUEST_X86: CONTEXT_FLAGS = 1073741824
CONTEXT_EXCEPTION_REPORTING_X86: CONTEXT_FLAGS = 2147483648
CONTEXT_ARM64: CONTEXT_FLAGS = 4194304
CONTEXT_CONTROL_ARM64: CONTEXT_FLAGS = 4194305
CONTEXT_INTEGER_ARM64: CONTEXT_FLAGS = 4194306
CONTEXT_FLOATING_POINT_ARM64: CONTEXT_FLAGS = 4194308
CONTEXT_DEBUG_REGISTERS_ARM64: CONTEXT_FLAGS = 4194312
CONTEXT_X18_ARM64: CONTEXT_FLAGS = 4194320
CONTEXT_FULL_ARM64: CONTEXT_FLAGS = 4194311
CONTEXT_ALL_ARM64: CONTEXT_FLAGS = 4194335
CONTEXT_EXCEPTION_ACTIVE_ARM64: CONTEXT_FLAGS = 134217728
CONTEXT_SERVICE_ACTIVE_ARM64: CONTEXT_FLAGS = 268435456
CONTEXT_EXCEPTION_REQUEST_ARM64: CONTEXT_FLAGS = 1073741824
CONTEXT_EXCEPTION_REPORTING_ARM64: CONTEXT_FLAGS = 2147483648
CONTEXT_UNWOUND_TO_CALL_ARM64: CONTEXT_FLAGS = 536870912
CONTEXT_RET_TO_GUEST_ARM64: CONTEXT_FLAGS = 1073741824
CONTEXT_ARM: CONTEXT_FLAGS = 2097152
CONTEXT_CONTROL_ARM: CONTEXT_FLAGS = 2097153
CONTEXT_INTEGER_ARM: CONTEXT_FLAGS = 2097154
CONTEXT_FLOATING_POINT_ARM: CONTEXT_FLAGS = 2097156
CONTEXT_DEBUG_REGISTERS_ARM: CONTEXT_FLAGS = 2097160
CONTEXT_FULL_ARM: CONTEXT_FLAGS = 2097159
CONTEXT_ALL_ARM: CONTEXT_FLAGS = 2097167
CONTEXT_EXCEPTION_ACTIVE_ARM: CONTEXT_FLAGS = 134217728
CONTEXT_SERVICE_ACTIVE_ARM: CONTEXT_FLAGS = 268435456
CONTEXT_EXCEPTION_REQUEST_ARM: CONTEXT_FLAGS = 1073741824
CONTEXT_EXCEPTION_REPORTING_ARM: CONTEXT_FLAGS = 2147483648
CONTEXT_UNWOUND_TO_CALL_ARM: CONTEXT_FLAGS = 536870912
class CPU_INFORMATION(EasyCastUnion):
    X86CpuInfo: _X86CpuInfo_e__Struct
    OtherCpuInfo: _OtherCpuInfo_e__Struct
    class _X86CpuInfo_e__Struct(EasyCastStructure):
        VendorId: UInt32 * 3
        VersionInformation: UInt32
        FeatureInformation: UInt32
        AMDExtendedCpuFeatures: UInt32
    class _OtherCpuInfo_e__Struct(EasyCastStructure):
        ProcessorFeatures: UInt64 * 2
        _pack_ = 4
class CREATE_PROCESS_DEBUG_INFO(EasyCastStructure):
    hFile: win32more.Windows.Win32.Foundation.HANDLE
    hProcess: win32more.Windows.Win32.Foundation.HANDLE
    hThread: win32more.Windows.Win32.Foundation.HANDLE
    lpBaseOfImage: VoidPtr
    dwDebugInfoFileOffset: UInt32
    nDebugInfoSize: UInt32
    lpThreadLocalBase: VoidPtr
    lpStartAddress: win32more.Windows.Win32.System.Threading.LPTHREAD_START_ROUTINE
    lpImageName: VoidPtr
    fUnicode: UInt16
class CREATE_THREAD_DEBUG_INFO(EasyCastStructure):
    hThread: win32more.Windows.Win32.Foundation.HANDLE
    lpThreadLocalBase: VoidPtr
    lpStartAddress: win32more.Windows.Win32.System.Threading.LPTHREAD_START_ROUTINE
class DBGHELP_DATA_REPORT_STRUCT(EasyCastStructure):
    pBinPathNonExist: win32more.Windows.Win32.Foundation.PWSTR
    pSymbolPathNonExist: win32more.Windows.Win32.Foundation.PWSTR
DBGPROP_ATTRIB_FLAGS = Int32
DBGPROP_ATTRIB_NO_ATTRIB: DBGPROP_ATTRIB_FLAGS = 0
DBGPROP_ATTRIB_VALUE_IS_INVALID: DBGPROP_ATTRIB_FLAGS = 8
DBGPROP_ATTRIB_VALUE_IS_EXPANDABLE: DBGPROP_ATTRIB_FLAGS = 16
DBGPROP_ATTRIB_VALUE_IS_FAKE: DBGPROP_ATTRIB_FLAGS = 32
DBGPROP_ATTRIB_VALUE_IS_METHOD: DBGPROP_ATTRIB_FLAGS = 256
DBGPROP_ATTRIB_VALUE_IS_EVENT: DBGPROP_ATTRIB_FLAGS = 512
DBGPROP_ATTRIB_VALUE_IS_RAW_STRING: DBGPROP_ATTRIB_FLAGS = 1024
DBGPROP_ATTRIB_VALUE_READONLY: DBGPROP_ATTRIB_FLAGS = 2048
DBGPROP_ATTRIB_ACCESS_PUBLIC: DBGPROP_ATTRIB_FLAGS = 4096
DBGPROP_ATTRIB_ACCESS_PRIVATE: DBGPROP_ATTRIB_FLAGS = 8192
DBGPROP_ATTRIB_ACCESS_PROTECTED: DBGPROP_ATTRIB_FLAGS = 16384
DBGPROP_ATTRIB_ACCESS_FINAL: DBGPROP_ATTRIB_FLAGS = 32768
DBGPROP_ATTRIB_STORAGE_GLOBAL: DBGPROP_ATTRIB_FLAGS = 65536
DBGPROP_ATTRIB_STORAGE_STATIC: DBGPROP_ATTRIB_FLAGS = 131072
DBGPROP_ATTRIB_STORAGE_FIELD: DBGPROP_ATTRIB_FLAGS = 262144
DBGPROP_ATTRIB_STORAGE_VIRTUAL: DBGPROP_ATTRIB_FLAGS = 524288
DBGPROP_ATTRIB_TYPE_IS_CONSTANT: DBGPROP_ATTRIB_FLAGS = 1048576
DBGPROP_ATTRIB_TYPE_IS_SYNCHRONIZED: DBGPROP_ATTRIB_FLAGS = 2097152
DBGPROP_ATTRIB_TYPE_IS_VOLATILE: DBGPROP_ATTRIB_FLAGS = 4194304
DBGPROP_ATTRIB_HAS_EXTENDED_ATTRIBS: DBGPROP_ATTRIB_FLAGS = 8388608
DBGPROP_ATTRIB_FRAME_INTRYBLOCK: DBGPROP_ATTRIB_FLAGS = 16777216
DBGPROP_ATTRIB_FRAME_INCATCHBLOCK: DBGPROP_ATTRIB_FLAGS = 33554432
DBGPROP_ATTRIB_FRAME_INFINALLYBLOCK: DBGPROP_ATTRIB_FLAGS = 67108864
DBGPROP_ATTRIB_VALUE_IS_RETURN_VALUE: DBGPROP_ATTRIB_FLAGS = 134217728
DBGPROP_ATTRIB_VALUE_PENDING_MUTATION: DBGPROP_ATTRIB_FLAGS = 268435456
DBGPROP_INFO = Int32
DBGPROP_INFO_NAME: DBGPROP_INFO = 1
DBGPROP_INFO_TYPE: DBGPROP_INFO = 2
DBGPROP_INFO_VALUE: DBGPROP_INFO = 4
DBGPROP_INFO_FULLNAME: DBGPROP_INFO = 32
DBGPROP_INFO_ATTRIBUTES: DBGPROP_INFO = 8
DBGPROP_INFO_DEBUGPROP: DBGPROP_INFO = 16
DBGPROP_INFO_BEAUTIFY: DBGPROP_INFO = 33554432
DBGPROP_INFO_CALLTOSTRING: DBGPROP_INFO = 67108864
DBGPROP_INFO_AUTOEXPAND: DBGPROP_INFO = 134217728
class DEBUG_EVENT(EasyCastStructure):
    dwDebugEventCode: win32more.Windows.Win32.System.Diagnostics.Debug.DEBUG_EVENT_CODE
    dwProcessId: UInt32
    dwThreadId: UInt32
    u: _u_e__Union
    class _u_e__Union(EasyCastUnion):
        Exception: win32more.Windows.Win32.System.Diagnostics.Debug.EXCEPTION_DEBUG_INFO
        CreateThread: win32more.Windows.Win32.System.Diagnostics.Debug.CREATE_THREAD_DEBUG_INFO
        CreateProcessInfo: win32more.Windows.Win32.System.Diagnostics.Debug.CREATE_PROCESS_DEBUG_INFO
        ExitThread: win32more.Windows.Win32.System.Diagnostics.Debug.EXIT_THREAD_DEBUG_INFO
        ExitProcess: win32more.Windows.Win32.System.Diagnostics.Debug.EXIT_PROCESS_DEBUG_INFO
        LoadDll: win32more.Windows.Win32.System.Diagnostics.Debug.LOAD_DLL_DEBUG_INFO
        UnloadDll: win32more.Windows.Win32.System.Diagnostics.Debug.UNLOAD_DLL_DEBUG_INFO
        DebugString: win32more.Windows.Win32.System.Diagnostics.Debug.OUTPUT_DEBUG_STRING_INFO
        RipInfo: win32more.Windows.Win32.System.Diagnostics.Debug.RIP_INFO
DEBUG_EVENT_CODE = UInt32
CREATE_PROCESS_DEBUG_EVENT: DEBUG_EVENT_CODE = 3
CREATE_THREAD_DEBUG_EVENT: DEBUG_EVENT_CODE = 2
EXCEPTION_DEBUG_EVENT: DEBUG_EVENT_CODE = 1
EXIT_PROCESS_DEBUG_EVENT: DEBUG_EVENT_CODE = 5
EXIT_THREAD_DEBUG_EVENT: DEBUG_EVENT_CODE = 4
LOAD_DLL_DEBUG_EVENT: DEBUG_EVENT_CODE = 6
OUTPUT_DEBUG_STRING_EVENT: DEBUG_EVENT_CODE = 8
RIP_EVENT: DEBUG_EVENT_CODE = 9
UNLOAD_DLL_DEBUG_EVENT: DEBUG_EVENT_CODE = 7
@winfunctype_pointer
def DIGEST_FUNCTION(refdata: VoidPtr, pData: POINTER(Byte), dwLength: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'ARM64':
    class DISPATCHER_CONTEXT(EasyCastStructure):
        ControlPc: UIntPtr
        ImageBase: UIntPtr
        FunctionEntry: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_ARM64_RUNTIME_FUNCTION_ENTRY_head)
        EstablisherFrame: UIntPtr
        TargetPc: UIntPtr
        ContextRecord: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_head)
        LanguageHandler: win32more.Windows.Win32.System.Kernel.EXCEPTION_ROUTINE
        HandlerData: VoidPtr
        HistoryTable: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.UNWIND_HISTORY_TABLE_head)
        ScopeIndex: UInt32
        ControlPcIsUnwound: win32more.Windows.Win32.Foundation.BOOLEAN
        NonVolatileRegisters: POINTER(Byte)
if ARCH in 'X64':
    class DISPATCHER_CONTEXT(EasyCastStructure):
        ControlPc: UInt64
        ImageBase: UInt64
        FunctionEntry: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_RUNTIME_FUNCTION_ENTRY_head)
        EstablisherFrame: UInt64
        TargetIp: UInt64
        ContextRecord: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_head)
        LanguageHandler: win32more.Windows.Win32.System.Kernel.EXCEPTION_ROUTINE
        HandlerData: VoidPtr
        HistoryTable: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.UNWIND_HISTORY_TABLE_head)
        ScopeIndex: UInt32
        Fill0: UInt32
class DUMP_FILE_ATTRIBUTES(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    Attributes: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class DUMP_HEADER32(EasyCastStructure):
    Signature: UInt32
    ValidDump: UInt32
    MajorVersion: UInt32
    MinorVersion: UInt32
    DirectoryTableBase: UInt32
    PfnDataBase: UInt32
    PsLoadedModuleList: UInt32
    PsActiveProcessHead: UInt32
    MachineImageType: UInt32
    NumberProcessors: UInt32
    BugCheckCode: UInt32
    BugCheckParameter1: UInt32
    BugCheckParameter2: UInt32
    BugCheckParameter3: UInt32
    BugCheckParameter4: UInt32
    VersionUser: win32more.Windows.Win32.Foundation.CHAR * 32
    PaeEnabled: Byte
    KdSecondaryVersion: Byte
    Spare3: Byte * 2
    KdDebuggerDataBlock: UInt32
    Anonymous: _Anonymous_e__Union
    ContextRecord: Byte * 1200
    Exception: win32more.Windows.Win32.System.Diagnostics.Debug.EXCEPTION_RECORD32
    Comment: win32more.Windows.Win32.Foundation.CHAR * 128
    Attributes: win32more.Windows.Win32.System.Diagnostics.Debug.DUMP_FILE_ATTRIBUTES
    BootId: UInt32
    _reserved0: Byte * 1760
    DumpType: UInt32
    MiniDumpFields: UInt32
    SecondaryDataState: UInt32
    ProductType: UInt32
    SuiteMask: UInt32
    WriterStatus: UInt32
    RequiredDumpSpace: Int64
    _reserved2: Byte * 16
    SystemUpTime: Int64
    SystemTime: Int64
    _reserved3: Byte * 56
    class _Anonymous_e__Union(EasyCastUnion):
        PhysicalMemoryBlock: win32more.Windows.Win32.System.Diagnostics.Debug.PHYSICAL_MEMORY_DESCRIPTOR32
        PhysicalMemoryBlockBuffer: Byte * 700
class DUMP_HEADER64(EasyCastStructure):
    Signature: UInt32
    ValidDump: UInt32
    MajorVersion: UInt32
    MinorVersion: UInt32
    DirectoryTableBase: UInt64
    PfnDataBase: UInt64
    PsLoadedModuleList: UInt64
    PsActiveProcessHead: UInt64
    MachineImageType: UInt32
    NumberProcessors: UInt32
    BugCheckCode: UInt32
    BugCheckParameter1: UInt64
    BugCheckParameter2: UInt64
    BugCheckParameter3: UInt64
    BugCheckParameter4: UInt64
    VersionUser: win32more.Windows.Win32.Foundation.CHAR * 32
    KdDebuggerDataBlock: UInt64
    Anonymous: _Anonymous_e__Union
    ContextRecord: Byte * 3000
    Exception: win32more.Windows.Win32.System.Diagnostics.Debug.EXCEPTION_RECORD64
    DumpType: UInt32
    RequiredDumpSpace: Int64
    SystemTime: Int64
    Comment: win32more.Windows.Win32.Foundation.CHAR * 128
    SystemUpTime: Int64
    MiniDumpFields: UInt32
    SecondaryDataState: UInt32
    ProductType: UInt32
    SuiteMask: UInt32
    WriterStatus: UInt32
    Unused1: Byte
    KdSecondaryVersion: Byte
    Unused: Byte * 2
    Attributes: win32more.Windows.Win32.System.Diagnostics.Debug.DUMP_FILE_ATTRIBUTES
    BootId: UInt32
    _reserved0: Byte * 4008
    class _Anonymous_e__Union(EasyCastUnion):
        PhysicalMemoryBlock: win32more.Windows.Win32.System.Diagnostics.Debug.PHYSICAL_MEMORY_DESCRIPTOR64
        PhysicalMemoryBlockBuffer: Byte * 700
DUMP_TYPE = Int32
DUMP_TYPE_INVALID: DUMP_TYPE = -1
DUMP_TYPE_UNKNOWN: DUMP_TYPE = 0
DUMP_TYPE_FULL: DUMP_TYPE = 1
DUMP_TYPE_SUMMARY: DUMP_TYPE = 2
DUMP_TYPE_HEADER: DUMP_TYPE = 3
DUMP_TYPE_TRIAGE: DUMP_TYPE = 4
DUMP_TYPE_BITMAP_FULL: DUMP_TYPE = 5
DUMP_TYPE_BITMAP_KERNEL: DUMP_TYPE = 6
DUMP_TYPE_AUTOMATIC: DUMP_TYPE = 7
class DebugPropertyInfo(EasyCastStructure):
    m_dwValidFields: UInt32
    m_bstrName: win32more.Windows.Win32.Foundation.BSTR
    m_bstrType: win32more.Windows.Win32.Foundation.BSTR
    m_bstrValue: win32more.Windows.Win32.Foundation.BSTR
    m_bstrFullName: win32more.Windows.Win32.Foundation.BSTR
    m_dwAttrib: UInt32
    m_pDebugProp: win32more.Windows.Win32.System.Diagnostics.Debug.IDebugProperty_head
class EXCEPTION_DEBUG_INFO(EasyCastStructure):
    ExceptionRecord: win32more.Windows.Win32.System.Diagnostics.Debug.EXCEPTION_RECORD
    dwFirstChance: UInt32
class EXCEPTION_POINTERS(EasyCastStructure):
    ExceptionRecord: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.EXCEPTION_RECORD_head)
    ContextRecord: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_head)
class EXCEPTION_RECORD(EasyCastStructure):
    ExceptionCode: win32more.Windows.Win32.Foundation.NTSTATUS
    ExceptionFlags: UInt32
    ExceptionRecord: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.EXCEPTION_RECORD_head)
    ExceptionAddress: VoidPtr
    NumberParameters: UInt32
    ExceptionInformation: UIntPtr * 15
class EXCEPTION_RECORD32(EasyCastStructure):
    ExceptionCode: win32more.Windows.Win32.Foundation.NTSTATUS
    ExceptionFlags: UInt32
    ExceptionRecord: UInt32
    ExceptionAddress: UInt32
    NumberParameters: UInt32
    ExceptionInformation: UInt32 * 15
class EXCEPTION_RECORD64(EasyCastStructure):
    ExceptionCode: win32more.Windows.Win32.Foundation.NTSTATUS
    ExceptionFlags: UInt32
    ExceptionRecord: UInt64
    ExceptionAddress: UInt64
    NumberParameters: UInt32
    __unusedAlignment: UInt32
    ExceptionInformation: UInt64 * 15
class EXIT_PROCESS_DEBUG_INFO(EasyCastStructure):
    dwExitCode: UInt32
class EXIT_THREAD_DEBUG_INFO(EasyCastStructure):
    dwExitCode: UInt32
EX_PROP_INFO_FLAGS = Int32
EX_PROP_INFO_ID: EX_PROP_INFO_FLAGS = 256
EX_PROP_INFO_NTYPE: EX_PROP_INFO_FLAGS = 512
EX_PROP_INFO_NVALUE: EX_PROP_INFO_FLAGS = 1024
EX_PROP_INFO_LOCKBYTES: EX_PROP_INFO_FLAGS = 2048
EX_PROP_INFO_DEBUGEXTPROP: EX_PROP_INFO_FLAGS = 4096
class ExtendedDebugPropertyInfo(EasyCastStructure):
    dwValidFields: UInt32
    pszName: win32more.Windows.Win32.Foundation.PWSTR
    pszType: win32more.Windows.Win32.Foundation.PWSTR
    pszValue: win32more.Windows.Win32.Foundation.PWSTR
    pszFullName: win32more.Windows.Win32.Foundation.PWSTR
    dwAttrib: UInt32
    pDebugProp: win32more.Windows.Win32.System.Diagnostics.Debug.IDebugProperty_head
    nDISPID: UInt32
    nType: UInt32
    varValue: win32more.Windows.Win32.System.Variant.VARIANT
    plbValue: win32more.Windows.Win32.System.Com.StructuredStorage.ILockBytes_head
    pDebugExtProp: win32more.Windows.Win32.System.Diagnostics.Debug.IDebugExtendedProperty_head
FACILITY_CODE = UInt32
FACILITY_NULL: FACILITY_CODE = 0
FACILITY_RPC: FACILITY_CODE = 1
FACILITY_DISPATCH: FACILITY_CODE = 2
FACILITY_STORAGE: FACILITY_CODE = 3
FACILITY_ITF: FACILITY_CODE = 4
FACILITY_WIN32: FACILITY_CODE = 7
FACILITY_WINDOWS: FACILITY_CODE = 8
FACILITY_SSPI: FACILITY_CODE = 9
FACILITY_SECURITY: FACILITY_CODE = 9
FACILITY_CONTROL: FACILITY_CODE = 10
FACILITY_CERT: FACILITY_CODE = 11
FACILITY_INTERNET: FACILITY_CODE = 12
FACILITY_MEDIASERVER: FACILITY_CODE = 13
FACILITY_MSMQ: FACILITY_CODE = 14
FACILITY_SETUPAPI: FACILITY_CODE = 15
FACILITY_SCARD: FACILITY_CODE = 16
FACILITY_COMPLUS: FACILITY_CODE = 17
FACILITY_AAF: FACILITY_CODE = 18
FACILITY_URT: FACILITY_CODE = 19
FACILITY_ACS: FACILITY_CODE = 20
FACILITY_DPLAY: FACILITY_CODE = 21
FACILITY_UMI: FACILITY_CODE = 22
FACILITY_SXS: FACILITY_CODE = 23
FACILITY_WINDOWS_CE: FACILITY_CODE = 24
FACILITY_HTTP: FACILITY_CODE = 25
FACILITY_USERMODE_COMMONLOG: FACILITY_CODE = 26
FACILITY_WER: FACILITY_CODE = 27
FACILITY_USERMODE_FILTER_MANAGER: FACILITY_CODE = 31
FACILITY_BACKGROUNDCOPY: FACILITY_CODE = 32
FACILITY_CONFIGURATION: FACILITY_CODE = 33
FACILITY_WIA: FACILITY_CODE = 33
FACILITY_STATE_MANAGEMENT: FACILITY_CODE = 34
FACILITY_METADIRECTORY: FACILITY_CODE = 35
FACILITY_WINDOWSUPDATE: FACILITY_CODE = 36
FACILITY_DIRECTORYSERVICE: FACILITY_CODE = 37
FACILITY_GRAPHICS: FACILITY_CODE = 38
FACILITY_SHELL: FACILITY_CODE = 39
FACILITY_NAP: FACILITY_CODE = 39
FACILITY_TPM_SERVICES: FACILITY_CODE = 40
FACILITY_TPM_SOFTWARE: FACILITY_CODE = 41
FACILITY_UI: FACILITY_CODE = 42
FACILITY_XAML: FACILITY_CODE = 43
FACILITY_ACTION_QUEUE: FACILITY_CODE = 44
FACILITY_PLA: FACILITY_CODE = 48
FACILITY_WINDOWS_SETUP: FACILITY_CODE = 48
FACILITY_FVE: FACILITY_CODE = 49
FACILITY_FWP: FACILITY_CODE = 50
FACILITY_WINRM: FACILITY_CODE = 51
FACILITY_NDIS: FACILITY_CODE = 52
FACILITY_USERMODE_HYPERVISOR: FACILITY_CODE = 53
FACILITY_CMI: FACILITY_CODE = 54
FACILITY_USERMODE_VIRTUALIZATION: FACILITY_CODE = 55
FACILITY_USERMODE_VOLMGR: FACILITY_CODE = 56
FACILITY_BCD: FACILITY_CODE = 57
FACILITY_USERMODE_VHD: FACILITY_CODE = 58
FACILITY_USERMODE_HNS: FACILITY_CODE = 59
FACILITY_SDIAG: FACILITY_CODE = 60
FACILITY_WEBSERVICES: FACILITY_CODE = 61
FACILITY_WINPE: FACILITY_CODE = 61
FACILITY_WPN: FACILITY_CODE = 62
FACILITY_WINDOWS_STORE: FACILITY_CODE = 63
FACILITY_INPUT: FACILITY_CODE = 64
FACILITY_QUIC: FACILITY_CODE = 65
FACILITY_EAP: FACILITY_CODE = 66
FACILITY_IORING: FACILITY_CODE = 70
FACILITY_WINDOWS_DEFENDER: FACILITY_CODE = 80
FACILITY_OPC: FACILITY_CODE = 81
FACILITY_XPS: FACILITY_CODE = 82
FACILITY_MBN: FACILITY_CODE = 84
FACILITY_POWERSHELL: FACILITY_CODE = 84
FACILITY_RAS: FACILITY_CODE = 83
FACILITY_P2P_INT: FACILITY_CODE = 98
FACILITY_P2P: FACILITY_CODE = 99
FACILITY_DAF: FACILITY_CODE = 100
FACILITY_BLUETOOTH_ATT: FACILITY_CODE = 101
FACILITY_AUDIO: FACILITY_CODE = 102
FACILITY_STATEREPOSITORY: FACILITY_CODE = 103
FACILITY_VISUALCPP: FACILITY_CODE = 109
FACILITY_SCRIPT: FACILITY_CODE = 112
FACILITY_PARSE: FACILITY_CODE = 113
FACILITY_BLB: FACILITY_CODE = 120
FACILITY_BLB_CLI: FACILITY_CODE = 121
FACILITY_WSBAPP: FACILITY_CODE = 122
FACILITY_BLBUI: FACILITY_CODE = 128
FACILITY_USN: FACILITY_CODE = 129
FACILITY_USERMODE_VOLSNAP: FACILITY_CODE = 130
FACILITY_TIERING: FACILITY_CODE = 131
FACILITY_WSB_ONLINE: FACILITY_CODE = 133
FACILITY_ONLINE_ID: FACILITY_CODE = 134
FACILITY_DEVICE_UPDATE_AGENT: FACILITY_CODE = 135
FACILITY_DRVSERVICING: FACILITY_CODE = 136
FACILITY_DLS: FACILITY_CODE = 153
FACILITY_DELIVERY_OPTIMIZATION: FACILITY_CODE = 208
FACILITY_USERMODE_SPACES: FACILITY_CODE = 231
FACILITY_USER_MODE_SECURITY_CORE: FACILITY_CODE = 232
FACILITY_USERMODE_LICENSING: FACILITY_CODE = 234
FACILITY_SOS: FACILITY_CODE = 160
FACILITY_OCP_UPDATE_AGENT: FACILITY_CODE = 173
FACILITY_DEBUGGERS: FACILITY_CODE = 176
FACILITY_SPP: FACILITY_CODE = 256
FACILITY_RESTORE: FACILITY_CODE = 256
FACILITY_DMSERVER: FACILITY_CODE = 256
FACILITY_DEPLOYMENT_SERVICES_SERVER: FACILITY_CODE = 257
FACILITY_DEPLOYMENT_SERVICES_IMAGING: FACILITY_CODE = 258
FACILITY_DEPLOYMENT_SERVICES_MANAGEMENT: FACILITY_CODE = 259
FACILITY_DEPLOYMENT_SERVICES_UTIL: FACILITY_CODE = 260
FACILITY_DEPLOYMENT_SERVICES_BINLSVC: FACILITY_CODE = 261
FACILITY_DEPLOYMENT_SERVICES_PXE: FACILITY_CODE = 263
FACILITY_DEPLOYMENT_SERVICES_TFTP: FACILITY_CODE = 264
FACILITY_DEPLOYMENT_SERVICES_TRANSPORT_MANAGEMENT: FACILITY_CODE = 272
FACILITY_DEPLOYMENT_SERVICES_DRIVER_PROVISIONING: FACILITY_CODE = 278
FACILITY_DEPLOYMENT_SERVICES_MULTICAST_SERVER: FACILITY_CODE = 289
FACILITY_DEPLOYMENT_SERVICES_MULTICAST_CLIENT: FACILITY_CODE = 290
FACILITY_DEPLOYMENT_SERVICES_CONTENT_PROVIDER: FACILITY_CODE = 293
FACILITY_HSP_SERVICES: FACILITY_CODE = 296
FACILITY_HSP_SOFTWARE: FACILITY_CODE = 297
FACILITY_LINGUISTIC_SERVICES: FACILITY_CODE = 305
FACILITY_AUDIOSTREAMING: FACILITY_CODE = 1094
FACILITY_TTD: FACILITY_CODE = 1490
FACILITY_ACCELERATOR: FACILITY_CODE = 1536
FACILITY_WMAAECMA: FACILITY_CODE = 1996
FACILITY_DIRECTMUSIC: FACILITY_CODE = 2168
FACILITY_DIRECT3D10: FACILITY_CODE = 2169
FACILITY_DXGI: FACILITY_CODE = 2170
FACILITY_DXGI_DDI: FACILITY_CODE = 2171
FACILITY_DIRECT3D11: FACILITY_CODE = 2172
FACILITY_DIRECT3D11_DEBUG: FACILITY_CODE = 2173
FACILITY_DIRECT3D12: FACILITY_CODE = 2174
FACILITY_DIRECT3D12_DEBUG: FACILITY_CODE = 2175
FACILITY_DXCORE: FACILITY_CODE = 2176
FACILITY_PRESENTATION: FACILITY_CODE = 2177
FACILITY_LEAP: FACILITY_CODE = 2184
FACILITY_AUDCLNT: FACILITY_CODE = 2185
FACILITY_WINCODEC_DWRITE_DWM: FACILITY_CODE = 2200
FACILITY_WINML: FACILITY_CODE = 2192
FACILITY_DIRECT2D: FACILITY_CODE = 2201
FACILITY_DEFRAG: FACILITY_CODE = 2304
FACILITY_USERMODE_SDBUS: FACILITY_CODE = 2305
FACILITY_JSCRIPT: FACILITY_CODE = 2306
FACILITY_PIDGENX: FACILITY_CODE = 2561
FACILITY_EAS: FACILITY_CODE = 85
FACILITY_WEB: FACILITY_CODE = 885
FACILITY_WEB_SOCKET: FACILITY_CODE = 886
FACILITY_MOBILE: FACILITY_CODE = 1793
FACILITY_SQLITE: FACILITY_CODE = 1967
FACILITY_SERVICE_FABRIC: FACILITY_CODE = 1968
FACILITY_UTC: FACILITY_CODE = 1989
FACILITY_WEP: FACILITY_CODE = 2049
FACILITY_SYNCENGINE: FACILITY_CODE = 2050
FACILITY_XBOX: FACILITY_CODE = 2339
FACILITY_GAME: FACILITY_CODE = 2340
FACILITY_PIX: FACILITY_CODE = 2748
FACILITY_NT_BIT: FACILITY_CODE = 268435456
FORMAT_MESSAGE_OPTIONS = UInt32
FORMAT_MESSAGE_ALLOCATE_BUFFER: FORMAT_MESSAGE_OPTIONS = 256
FORMAT_MESSAGE_ARGUMENT_ARRAY: FORMAT_MESSAGE_OPTIONS = 8192
FORMAT_MESSAGE_FROM_HMODULE: FORMAT_MESSAGE_OPTIONS = 2048
FORMAT_MESSAGE_FROM_STRING: FORMAT_MESSAGE_OPTIONS = 1024
FORMAT_MESSAGE_FROM_SYSTEM: FORMAT_MESSAGE_OPTIONS = 4096
FORMAT_MESSAGE_IGNORE_INSERTS: FORMAT_MESSAGE_OPTIONS = 512
class FPO_DATA(EasyCastStructure):
    ulOffStart: UInt32
    cbProcSize: UInt32
    cdwLocals: UInt32
    cdwParams: UInt16
    _bitfield: UInt16
class IDebugExtendedProperty(ComPtr):
    extends: win32more.Windows.Win32.System.Diagnostics.Debug.IDebugProperty
    _iid_ = Guid('{51973c52-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(8)
    def GetExtendedPropertyInfo(self, dwFieldSpec: UInt32, nRadix: UInt32, pExtendedPropertyInfo: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ExtendedDebugPropertyInfo_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def EnumExtendedMembers(self, dwFieldSpec: UInt32, nRadix: UInt32, ppeepi: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IEnumDebugExtendedPropertyInfo_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDebugProperty(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51973c50-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(3)
    def GetPropertyInfo(self, dwFieldSpec: UInt32, nRadix: UInt32, pPropertyInfo: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.DebugPropertyInfo_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetExtendedInfo(self, cInfos: UInt32, rgguidExtendedInfo: POINTER(Guid), rgvar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetValueAsString(self, pszValue: win32more.Windows.Win32.Foundation.PWSTR, nRadix: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EnumMembers(self, dwFieldSpec: UInt32, nRadix: UInt32, refiid: POINTER(Guid), ppepi: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IEnumDebugPropertyInfo_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetParent(self, ppDebugProp: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IDebugProperty_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDebugPropertyEnumType_All(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51973c55-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(3)
    def GetName(self, __MIDL__IDebugPropertyEnumType_All0000: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDebugPropertyEnumType_Arguments(ComPtr):
    extends: win32more.Windows.Win32.System.Diagnostics.Debug.IDebugPropertyEnumType_All
    _iid_ = Guid('{51973c57-cb0c-11d0-b5c9-00a0244a0e7a}')
class IDebugPropertyEnumType_Locals(ComPtr):
    extends: win32more.Windows.Win32.System.Diagnostics.Debug.IDebugPropertyEnumType_All
    _iid_ = Guid('{51973c56-cb0c-11d0-b5c9-00a0244a0e7a}')
class IDebugPropertyEnumType_LocalsPlusArgs(ComPtr):
    extends: win32more.Windows.Win32.System.Diagnostics.Debug.IDebugPropertyEnumType_All
    _iid_ = Guid('{51973c58-cb0c-11d0-b5c9-00a0244a0e7a}')
class IDebugPropertyEnumType_Registers(ComPtr):
    extends: win32more.Windows.Win32.System.Diagnostics.Debug.IDebugPropertyEnumType_All
    _iid_ = Guid('{51973c59-cb0c-11d0-b5c9-00a0244a0e7a}')
class IEnumDebugExtendedPropertyInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51973c53-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(3)
    def Next(self, celt: UInt32, rgExtendedPropertyInfo: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ExtendedDebugPropertyInfo_head), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, pedpe: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IEnumDebugExtendedPropertyInfo_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCount(self, pcelt: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumDebugPropertyInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51973c51-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(3)
    def Next(self, celt: UInt32, pi: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.DebugPropertyInfo_head), pcEltsfetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppepi: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IEnumDebugPropertyInfo_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCount(self, pcelt: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMAGEHLP_CBA_EVENT(EasyCastStructure):
    severity: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_CBA_EVENT_SEVERITY
    code: UInt32
    desc: win32more.Windows.Win32.Foundation.PSTR
    object: VoidPtr
class IMAGEHLP_CBA_EVENTW(EasyCastStructure):
    severity: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_CBA_EVENT_SEVERITY
    code: UInt32
    desc: win32more.Windows.Win32.Foundation.PWSTR
    object: VoidPtr
IMAGEHLP_CBA_EVENT_SEVERITY = UInt32
IMAGEHLP_CBA_EVENT_SEVERITY_sevInfo: IMAGEHLP_CBA_EVENT_SEVERITY = 0
IMAGEHLP_CBA_EVENT_SEVERITY_sevProblem: IMAGEHLP_CBA_EVENT_SEVERITY = 1
IMAGEHLP_CBA_EVENT_SEVERITY_sevAttn: IMAGEHLP_CBA_EVENT_SEVERITY = 2
IMAGEHLP_CBA_EVENT_SEVERITY_sevFatal: IMAGEHLP_CBA_EVENT_SEVERITY = 3
class IMAGEHLP_CBA_READ_MEMORY(EasyCastStructure):
    addr: UInt64
    buf: VoidPtr
    bytes: UInt32
    bytesread: POINTER(UInt32)
if ARCH in 'X86':
    class IMAGEHLP_DEFERRED_SYMBOL_LOAD(EasyCastStructure):
        SizeOfStruct: UInt32
        BaseOfImage: UInt32
        CheckSum: UInt32
        TimeDateStamp: UInt32
        FileName: win32more.Windows.Win32.Foundation.CHAR * 260
        Reparse: win32more.Windows.Win32.Foundation.BOOLEAN
        hFile: win32more.Windows.Win32.Foundation.HANDLE
class IMAGEHLP_DEFERRED_SYMBOL_LOAD64(EasyCastStructure):
    SizeOfStruct: UInt32
    BaseOfImage: UInt64
    CheckSum: UInt32
    TimeDateStamp: UInt32
    FileName: win32more.Windows.Win32.Foundation.CHAR * 260
    Reparse: win32more.Windows.Win32.Foundation.BOOLEAN
    hFile: win32more.Windows.Win32.Foundation.HANDLE
    Flags: UInt32
class IMAGEHLP_DEFERRED_SYMBOL_LOADW64(EasyCastStructure):
    SizeOfStruct: UInt32
    BaseOfImage: UInt64
    CheckSum: UInt32
    TimeDateStamp: UInt32
    FileName: Char * 261
    Reparse: win32more.Windows.Win32.Foundation.BOOLEAN
    hFile: win32more.Windows.Win32.Foundation.HANDLE
    Flags: UInt32
if ARCH in 'X86':
    class IMAGEHLP_DUPLICATE_SYMBOL(EasyCastStructure):
        SizeOfStruct: UInt32
        NumberOfDups: UInt32
        Symbol: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL_head)
        SelectedSymbol: UInt32
class IMAGEHLP_DUPLICATE_SYMBOL64(EasyCastStructure):
    SizeOfStruct: UInt32
    NumberOfDups: UInt32
    Symbol: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL64_head)
    SelectedSymbol: UInt32
IMAGEHLP_EXTENDED_OPTIONS = Int32
SYMOPT_EX_DISABLEACCESSTIMEUPDATE: IMAGEHLP_EXTENDED_OPTIONS = 0
SYMOPT_EX_LASTVALIDDEBUGDIRECTORY: IMAGEHLP_EXTENDED_OPTIONS = 1
SYMOPT_EX_NOIMPLICITPATTERNSEARCH: IMAGEHLP_EXTENDED_OPTIONS = 2
SYMOPT_EX_NEVERLOADSYMBOLS: IMAGEHLP_EXTENDED_OPTIONS = 3
SYMOPT_EX_MAX: IMAGEHLP_EXTENDED_OPTIONS = 4
IMAGEHLP_GET_TYPE_INFO_FLAGS = UInt32
IMAGEHLP_GET_TYPE_INFO_CHILDREN: IMAGEHLP_GET_TYPE_INFO_FLAGS = 2
IMAGEHLP_GET_TYPE_INFO_UNCACHED: IMAGEHLP_GET_TYPE_INFO_FLAGS = 1
class IMAGEHLP_GET_TYPE_INFO_PARAMS(EasyCastStructure):
    SizeOfStruct: UInt32
    Flags: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_GET_TYPE_INFO_FLAGS
    NumIds: UInt32
    TypeIds: POINTER(UInt32)
    TagFilter: UInt64
    NumReqs: UInt32
    ReqKinds: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL_TYPE_INFO)
    ReqOffsets: POINTER(UIntPtr)
    ReqSizes: POINTER(UInt32)
    ReqStride: UIntPtr
    BufferSize: UIntPtr
    Buffer: VoidPtr
    EntriesMatched: UInt32
    EntriesFilled: UInt32
    TagsFound: UInt64
    AllReqsValid: UInt64
    NumReqsValid: UInt32
    ReqsValid: POINTER(UInt64)
IMAGEHLP_HD_TYPE = Int32
IMAGEHLP_HD_TYPE_hdBase: IMAGEHLP_HD_TYPE = 0
IMAGEHLP_HD_TYPE_hdSym: IMAGEHLP_HD_TYPE = 1
IMAGEHLP_HD_TYPE_hdSrc: IMAGEHLP_HD_TYPE = 2
IMAGEHLP_HD_TYPE_hdMax: IMAGEHLP_HD_TYPE = 3
class IMAGEHLP_JIT_SYMBOLMAP(EasyCastStructure):
    SizeOfStruct: UInt32
    Address: UInt64
    BaseOfImage: UInt64
if ARCH in 'X86':
    class IMAGEHLP_LINE(EasyCastStructure):
        SizeOfStruct: UInt32
        Key: VoidPtr
        LineNumber: UInt32
        FileName: win32more.Windows.Win32.Foundation.PSTR
        Address: UInt32
class IMAGEHLP_LINE64(EasyCastStructure):
    SizeOfStruct: UInt32
    Key: VoidPtr
    LineNumber: UInt32
    FileName: win32more.Windows.Win32.Foundation.PSTR
    Address: UInt64
if ARCH in 'X86':
    class IMAGEHLP_LINEW(EasyCastStructure):
        SizeOfStruct: UInt32
        Key: VoidPtr
        LineNumber: UInt32
        FileName: win32more.Windows.Win32.Foundation.PSTR
        Address: UInt64
class IMAGEHLP_LINEW64(EasyCastStructure):
    SizeOfStruct: UInt32
    Key: VoidPtr
    LineNumber: UInt32
    FileName: win32more.Windows.Win32.Foundation.PWSTR
    Address: UInt64
if ARCH in 'X86':
    class IMAGEHLP_MODULE(EasyCastStructure):
        SizeOfStruct: UInt32
        BaseOfImage: UInt32
        ImageSize: UInt32
        TimeDateStamp: UInt32
        CheckSum: UInt32
        NumSyms: UInt32
        SymType: win32more.Windows.Win32.System.Diagnostics.Debug.SYM_TYPE
        ModuleName: win32more.Windows.Win32.Foundation.CHAR * 32
        ImageName: win32more.Windows.Win32.Foundation.CHAR * 256
        LoadedImageName: win32more.Windows.Win32.Foundation.CHAR * 256
class IMAGEHLP_MODULE64(EasyCastStructure):
    SizeOfStruct: UInt32
    BaseOfImage: UInt64
    ImageSize: UInt32
    TimeDateStamp: UInt32
    CheckSum: UInt32
    NumSyms: UInt32
    SymType: win32more.Windows.Win32.System.Diagnostics.Debug.SYM_TYPE
    ModuleName: win32more.Windows.Win32.Foundation.CHAR * 32
    ImageName: win32more.Windows.Win32.Foundation.CHAR * 256
    LoadedImageName: win32more.Windows.Win32.Foundation.CHAR * 256
    LoadedPdbName: win32more.Windows.Win32.Foundation.CHAR * 256
    CVSig: UInt32
    CVData: win32more.Windows.Win32.Foundation.CHAR * 780
    PdbSig: UInt32
    PdbSig70: Guid
    PdbAge: UInt32
    PdbUnmatched: win32more.Windows.Win32.Foundation.BOOL
    DbgUnmatched: win32more.Windows.Win32.Foundation.BOOL
    LineNumbers: win32more.Windows.Win32.Foundation.BOOL
    GlobalSymbols: win32more.Windows.Win32.Foundation.BOOL
    TypeInfo: win32more.Windows.Win32.Foundation.BOOL
    SourceIndexed: win32more.Windows.Win32.Foundation.BOOL
    Publics: win32more.Windows.Win32.Foundation.BOOL
    MachineType: UInt32
    Reserved: UInt32
class IMAGEHLP_MODULE64_EX(EasyCastStructure):
    Module: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_MODULE64
    RegionFlags: UInt32
if ARCH in 'X86':
    class IMAGEHLP_MODULEW(EasyCastStructure):
        SizeOfStruct: UInt32
        BaseOfImage: UInt32
        ImageSize: UInt32
        TimeDateStamp: UInt32
        CheckSum: UInt32
        NumSyms: UInt32
        SymType: win32more.Windows.Win32.System.Diagnostics.Debug.SYM_TYPE
        ModuleName: Char * 32
        ImageName: Char * 256
        LoadedImageName: Char * 256
class IMAGEHLP_MODULEW64(EasyCastStructure):
    SizeOfStruct: UInt32
    BaseOfImage: UInt64
    ImageSize: UInt32
    TimeDateStamp: UInt32
    CheckSum: UInt32
    NumSyms: UInt32
    SymType: win32more.Windows.Win32.System.Diagnostics.Debug.SYM_TYPE
    ModuleName: Char * 32
    ImageName: Char * 256
    LoadedImageName: Char * 256
    LoadedPdbName: Char * 256
    CVSig: UInt32
    CVData: Char * 780
    PdbSig: UInt32
    PdbSig70: Guid
    PdbAge: UInt32
    PdbUnmatched: win32more.Windows.Win32.Foundation.BOOL
    DbgUnmatched: win32more.Windows.Win32.Foundation.BOOL
    LineNumbers: win32more.Windows.Win32.Foundation.BOOL
    GlobalSymbols: win32more.Windows.Win32.Foundation.BOOL
    TypeInfo: win32more.Windows.Win32.Foundation.BOOL
    SourceIndexed: win32more.Windows.Win32.Foundation.BOOL
    Publics: win32more.Windows.Win32.Foundation.BOOL
    MachineType: UInt32
    Reserved: UInt32
class IMAGEHLP_MODULEW64_EX(EasyCastStructure):
    Module: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_MODULEW64
    RegionFlags: UInt32
IMAGEHLP_SF_TYPE = Int32
IMAGEHLP_SF_TYPE_sfImage: IMAGEHLP_SF_TYPE = 0
IMAGEHLP_SF_TYPE_sfDbg: IMAGEHLP_SF_TYPE = 1
IMAGEHLP_SF_TYPE_sfPdb: IMAGEHLP_SF_TYPE = 2
IMAGEHLP_SF_TYPE_sfMpd: IMAGEHLP_SF_TYPE = 3
IMAGEHLP_SF_TYPE_sfMax: IMAGEHLP_SF_TYPE = 4
class IMAGEHLP_STACK_FRAME(EasyCastStructure):
    InstructionOffset: UInt64
    ReturnOffset: UInt64
    FrameOffset: UInt64
    StackOffset: UInt64
    BackingStoreOffset: UInt64
    FuncTableEntry: UInt64
    Params: UInt64 * 4
    Reserved: UInt64 * 5
    Virtual: win32more.Windows.Win32.Foundation.BOOL
    Reserved2: UInt32
IMAGEHLP_STATUS_REASON = Int32
IMAGEHLP_STATUS_REASON_BindOutOfMemory: IMAGEHLP_STATUS_REASON = 0
IMAGEHLP_STATUS_REASON_BindRvaToVaFailed: IMAGEHLP_STATUS_REASON = 1
IMAGEHLP_STATUS_REASON_BindNoRoomInImage: IMAGEHLP_STATUS_REASON = 2
IMAGEHLP_STATUS_REASON_BindImportModuleFailed: IMAGEHLP_STATUS_REASON = 3
IMAGEHLP_STATUS_REASON_BindImportProcedureFailed: IMAGEHLP_STATUS_REASON = 4
IMAGEHLP_STATUS_REASON_BindImportModule: IMAGEHLP_STATUS_REASON = 5
IMAGEHLP_STATUS_REASON_BindImportProcedure: IMAGEHLP_STATUS_REASON = 6
IMAGEHLP_STATUS_REASON_BindForwarder: IMAGEHLP_STATUS_REASON = 7
IMAGEHLP_STATUS_REASON_BindForwarderNOT: IMAGEHLP_STATUS_REASON = 8
IMAGEHLP_STATUS_REASON_BindImageModified: IMAGEHLP_STATUS_REASON = 9
IMAGEHLP_STATUS_REASON_BindExpandFileHeaders: IMAGEHLP_STATUS_REASON = 10
IMAGEHLP_STATUS_REASON_BindImageComplete: IMAGEHLP_STATUS_REASON = 11
IMAGEHLP_STATUS_REASON_BindMismatchedSymbols: IMAGEHLP_STATUS_REASON = 12
IMAGEHLP_STATUS_REASON_BindSymbolsNotUpdated: IMAGEHLP_STATUS_REASON = 13
IMAGEHLP_STATUS_REASON_BindImportProcedure32: IMAGEHLP_STATUS_REASON = 14
IMAGEHLP_STATUS_REASON_BindImportProcedure64: IMAGEHLP_STATUS_REASON = 15
IMAGEHLP_STATUS_REASON_BindForwarder32: IMAGEHLP_STATUS_REASON = 16
IMAGEHLP_STATUS_REASON_BindForwarder64: IMAGEHLP_STATUS_REASON = 17
IMAGEHLP_STATUS_REASON_BindForwarderNOT32: IMAGEHLP_STATUS_REASON = 18
IMAGEHLP_STATUS_REASON_BindForwarderNOT64: IMAGEHLP_STATUS_REASON = 19
if ARCH in 'X86':
    class IMAGEHLP_SYMBOL(EasyCastStructure):
        SizeOfStruct: UInt32
        Address: UInt32
        Size: UInt32
        Flags: UInt32
        MaxNameLength: UInt32
        Name: win32more.Windows.Win32.Foundation.CHAR * 1
class IMAGEHLP_SYMBOL64(EasyCastStructure):
    SizeOfStruct: UInt32
    Address: UInt64
    Size: UInt32
    Flags: UInt32
    MaxNameLength: UInt32
    Name: win32more.Windows.Win32.Foundation.CHAR * 1
class IMAGEHLP_SYMBOL64_PACKAGE(EasyCastStructure):
    sym: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL64
    name: win32more.Windows.Win32.Foundation.CHAR * 2001
if ARCH in 'X86':
    class IMAGEHLP_SYMBOLW(EasyCastStructure):
        SizeOfStruct: UInt32
        Address: UInt32
        Size: UInt32
        Flags: UInt32
        MaxNameLength: UInt32
        Name: Char * 1
class IMAGEHLP_SYMBOLW64(EasyCastStructure):
    SizeOfStruct: UInt32
    Address: UInt64
    Size: UInt32
    Flags: UInt32
    MaxNameLength: UInt32
    Name: Char * 1
class IMAGEHLP_SYMBOLW64_PACKAGE(EasyCastStructure):
    sym: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOLW64
    name: Char * 2001
if ARCH in 'X86':
    class IMAGEHLP_SYMBOLW_PACKAGE(EasyCastStructure):
        sym: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOLW
        name: Char * 2001
if ARCH in 'X86':
    class IMAGEHLP_SYMBOL_PACKAGE(EasyCastStructure):
        sym: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL
        name: win32more.Windows.Win32.Foundation.CHAR * 2001
class IMAGEHLP_SYMBOL_SRC(EasyCastStructure):
    sizeofstruct: UInt32
    type: UInt32
    file: win32more.Windows.Win32.Foundation.CHAR * 260
IMAGEHLP_SYMBOL_TYPE_INFO = Int32
TI_GET_SYMTAG: IMAGEHLP_SYMBOL_TYPE_INFO = 0
TI_GET_SYMNAME: IMAGEHLP_SYMBOL_TYPE_INFO = 1
TI_GET_LENGTH: IMAGEHLP_SYMBOL_TYPE_INFO = 2
TI_GET_TYPE: IMAGEHLP_SYMBOL_TYPE_INFO = 3
TI_GET_TYPEID: IMAGEHLP_SYMBOL_TYPE_INFO = 4
TI_GET_BASETYPE: IMAGEHLP_SYMBOL_TYPE_INFO = 5
TI_GET_ARRAYINDEXTYPEID: IMAGEHLP_SYMBOL_TYPE_INFO = 6
TI_FINDCHILDREN: IMAGEHLP_SYMBOL_TYPE_INFO = 7
TI_GET_DATAKIND: IMAGEHLP_SYMBOL_TYPE_INFO = 8
TI_GET_ADDRESSOFFSET: IMAGEHLP_SYMBOL_TYPE_INFO = 9
TI_GET_OFFSET: IMAGEHLP_SYMBOL_TYPE_INFO = 10
TI_GET_VALUE: IMAGEHLP_SYMBOL_TYPE_INFO = 11
TI_GET_COUNT: IMAGEHLP_SYMBOL_TYPE_INFO = 12
TI_GET_CHILDRENCOUNT: IMAGEHLP_SYMBOL_TYPE_INFO = 13
TI_GET_BITPOSITION: IMAGEHLP_SYMBOL_TYPE_INFO = 14
TI_GET_VIRTUALBASECLASS: IMAGEHLP_SYMBOL_TYPE_INFO = 15
TI_GET_VIRTUALTABLESHAPEID: IMAGEHLP_SYMBOL_TYPE_INFO = 16
TI_GET_VIRTUALBASEPOINTEROFFSET: IMAGEHLP_SYMBOL_TYPE_INFO = 17
TI_GET_CLASSPARENTID: IMAGEHLP_SYMBOL_TYPE_INFO = 18
TI_GET_NESTED: IMAGEHLP_SYMBOL_TYPE_INFO = 19
TI_GET_SYMINDEX: IMAGEHLP_SYMBOL_TYPE_INFO = 20
TI_GET_LEXICALPARENT: IMAGEHLP_SYMBOL_TYPE_INFO = 21
TI_GET_ADDRESS: IMAGEHLP_SYMBOL_TYPE_INFO = 22
TI_GET_THISADJUST: IMAGEHLP_SYMBOL_TYPE_INFO = 23
TI_GET_UDTKIND: IMAGEHLP_SYMBOL_TYPE_INFO = 24
TI_IS_EQUIV_TO: IMAGEHLP_SYMBOL_TYPE_INFO = 25
TI_GET_CALLING_CONVENTION: IMAGEHLP_SYMBOL_TYPE_INFO = 26
TI_IS_CLOSE_EQUIV_TO: IMAGEHLP_SYMBOL_TYPE_INFO = 27
TI_GTIEX_REQS_VALID: IMAGEHLP_SYMBOL_TYPE_INFO = 28
TI_GET_VIRTUALBASEOFFSET: IMAGEHLP_SYMBOL_TYPE_INFO = 29
TI_GET_VIRTUALBASEDISPINDEX: IMAGEHLP_SYMBOL_TYPE_INFO = 30
TI_GET_IS_REFERENCE: IMAGEHLP_SYMBOL_TYPE_INFO = 31
TI_GET_INDIRECTVIRTUALBASECLASS: IMAGEHLP_SYMBOL_TYPE_INFO = 32
TI_GET_VIRTUALBASETABLETYPE: IMAGEHLP_SYMBOL_TYPE_INFO = 33
TI_GET_OBJECTPOINTERTYPE: IMAGEHLP_SYMBOL_TYPE_INFO = 34
IMAGEHLP_SYMBOL_TYPE_INFO_MAX: IMAGEHLP_SYMBOL_TYPE_INFO = 35
class IMAGE_ARM64_RUNTIME_FUNCTION_ENTRY(EasyCastStructure):
    BeginAddress: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        UnwindData: UInt32
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(EasyCastStructure):
            _bitfield: UInt32
class IMAGE_COFF_SYMBOLS_HEADER(EasyCastStructure):
    NumberOfSymbols: UInt32
    LvaToFirstSymbol: UInt32
    NumberOfLinenumbers: UInt32
    LvaToFirstLinenumber: UInt32
    RvaToFirstByteOfCode: UInt32
    RvaToLastByteOfCode: UInt32
    RvaToFirstByteOfData: UInt32
    RvaToLastByteOfData: UInt32
class IMAGE_COR20_HEADER(EasyCastStructure):
    cb: UInt32
    MajorRuntimeVersion: UInt16
    MinorRuntimeVersion: UInt16
    MetaData: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DATA_DIRECTORY
    Flags: UInt32
    Anonymous: _Anonymous_e__Union
    Resources: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DATA_DIRECTORY
    StrongNameSignature: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DATA_DIRECTORY
    CodeManagerTable: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DATA_DIRECTORY
    VTableFixups: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DATA_DIRECTORY
    ExportAddressTableJumps: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DATA_DIRECTORY
    ManagedNativeHeader: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DATA_DIRECTORY
    class _Anonymous_e__Union(EasyCastUnion):
        EntryPointToken: UInt32
        EntryPointRVA: UInt32
class IMAGE_DATA_DIRECTORY(EasyCastStructure):
    VirtualAddress: UInt32
    Size: UInt32
class IMAGE_DEBUG_DIRECTORY(EasyCastStructure):
    Characteristics: UInt32
    TimeDateStamp: UInt32
    MajorVersion: UInt16
    MinorVersion: UInt16
    Type: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DEBUG_TYPE
    SizeOfData: UInt32
    AddressOfRawData: UInt32
    PointerToRawData: UInt32
if ARCH in 'X86':
    class IMAGE_DEBUG_INFORMATION(EasyCastStructure):
        List: win32more.Windows.Win32.System.Kernel.LIST_ENTRY
        ReservedSize: UInt32
        ReservedMappedBase: VoidPtr
        ReservedMachine: UInt16
        ReservedCharacteristics: UInt16
        ReservedCheckSum: UInt32
        ImageBase: UInt32
        SizeOfImage: UInt32
        ReservedNumberOfSections: UInt32
        ReservedSections: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_HEADER_head)
        ReservedExportedNamesSize: UInt32
        ReservedExportedNames: win32more.Windows.Win32.Foundation.PSTR
        ReservedNumberOfFunctionTableEntries: UInt32
        ReservedFunctionTableEntries: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_FUNCTION_ENTRY_head)
        ReservedLowestFunctionStartingAddress: UInt32
        ReservedHighestFunctionEndingAddress: UInt32
        ReservedNumberOfFpoTableEntries: UInt32
        ReservedFpoTableEntries: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.FPO_DATA_head)
        SizeOfCoffSymbols: UInt32
        CoffSymbols: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_COFF_SYMBOLS_HEADER_head)
        ReservedSizeOfCodeViewSymbols: UInt32
        ReservedCodeViewSymbols: VoidPtr
        ImageFilePath: win32more.Windows.Win32.Foundation.PSTR
        ImageFileName: win32more.Windows.Win32.Foundation.PSTR
        ReservedDebugFilePath: win32more.Windows.Win32.Foundation.PSTR
        ReservedTimeDateStamp: UInt32
        ReservedRomImage: win32more.Windows.Win32.Foundation.BOOL
        ReservedDebugDirectory: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DEBUG_DIRECTORY_head)
        ReservedNumberOfDebugDirectories: UInt32
        ReservedOriginalFunctionTableBaseAddress: UInt32
        Reserved: UInt32 * 2
IMAGE_DEBUG_TYPE = UInt32
IMAGE_DEBUG_TYPE_UNKNOWN: IMAGE_DEBUG_TYPE = 0
IMAGE_DEBUG_TYPE_COFF: IMAGE_DEBUG_TYPE = 1
IMAGE_DEBUG_TYPE_CODEVIEW: IMAGE_DEBUG_TYPE = 2
IMAGE_DEBUG_TYPE_FPO: IMAGE_DEBUG_TYPE = 3
IMAGE_DEBUG_TYPE_MISC: IMAGE_DEBUG_TYPE = 4
IMAGE_DEBUG_TYPE_EXCEPTION: IMAGE_DEBUG_TYPE = 5
IMAGE_DEBUG_TYPE_FIXUP: IMAGE_DEBUG_TYPE = 6
IMAGE_DEBUG_TYPE_BORLAND: IMAGE_DEBUG_TYPE = 9
IMAGE_DIRECTORY_ENTRY = UInt16
IMAGE_DIRECTORY_ENTRY_ARCHITECTURE: IMAGE_DIRECTORY_ENTRY = 7
IMAGE_DIRECTORY_ENTRY_BASERELOC: IMAGE_DIRECTORY_ENTRY = 5
IMAGE_DIRECTORY_ENTRY_BOUND_IMPORT: IMAGE_DIRECTORY_ENTRY = 11
IMAGE_DIRECTORY_ENTRY_COM_DESCRIPTOR: IMAGE_DIRECTORY_ENTRY = 14
IMAGE_DIRECTORY_ENTRY_DEBUG: IMAGE_DIRECTORY_ENTRY = 6
IMAGE_DIRECTORY_ENTRY_DELAY_IMPORT: IMAGE_DIRECTORY_ENTRY = 13
IMAGE_DIRECTORY_ENTRY_EXCEPTION: IMAGE_DIRECTORY_ENTRY = 3
IMAGE_DIRECTORY_ENTRY_EXPORT: IMAGE_DIRECTORY_ENTRY = 0
IMAGE_DIRECTORY_ENTRY_GLOBALPTR: IMAGE_DIRECTORY_ENTRY = 8
IMAGE_DIRECTORY_ENTRY_IAT: IMAGE_DIRECTORY_ENTRY = 12
IMAGE_DIRECTORY_ENTRY_IMPORT: IMAGE_DIRECTORY_ENTRY = 1
IMAGE_DIRECTORY_ENTRY_LOAD_CONFIG: IMAGE_DIRECTORY_ENTRY = 10
IMAGE_DIRECTORY_ENTRY_RESOURCE: IMAGE_DIRECTORY_ENTRY = 2
IMAGE_DIRECTORY_ENTRY_SECURITY: IMAGE_DIRECTORY_ENTRY = 4
IMAGE_DIRECTORY_ENTRY_TLS: IMAGE_DIRECTORY_ENTRY = 9
IMAGE_DLL_CHARACTERISTICS = UInt16
IMAGE_DLLCHARACTERISTICS_HIGH_ENTROPY_VA: IMAGE_DLL_CHARACTERISTICS = 32
IMAGE_DLLCHARACTERISTICS_DYNAMIC_BASE: IMAGE_DLL_CHARACTERISTICS = 64
IMAGE_DLLCHARACTERISTICS_FORCE_INTEGRITY: IMAGE_DLL_CHARACTERISTICS = 128
IMAGE_DLLCHARACTERISTICS_NX_COMPAT: IMAGE_DLL_CHARACTERISTICS = 256
IMAGE_DLLCHARACTERISTICS_NO_ISOLATION: IMAGE_DLL_CHARACTERISTICS = 512
IMAGE_DLLCHARACTERISTICS_NO_SEH: IMAGE_DLL_CHARACTERISTICS = 1024
IMAGE_DLLCHARACTERISTICS_NO_BIND: IMAGE_DLL_CHARACTERISTICS = 2048
IMAGE_DLLCHARACTERISTICS_APPCONTAINER: IMAGE_DLL_CHARACTERISTICS = 4096
IMAGE_DLLCHARACTERISTICS_WDM_DRIVER: IMAGE_DLL_CHARACTERISTICS = 8192
IMAGE_DLLCHARACTERISTICS_GUARD_CF: IMAGE_DLL_CHARACTERISTICS = 16384
IMAGE_DLLCHARACTERISTICS_TERMINAL_SERVER_AWARE: IMAGE_DLL_CHARACTERISTICS = 32768
IMAGE_DLLCHARACTERISTICS_EX_CET_COMPAT: IMAGE_DLL_CHARACTERISTICS = 1
IMAGE_DLLCHARACTERISTICS_EX_CET_COMPAT_STRICT_MODE: IMAGE_DLL_CHARACTERISTICS = 2
IMAGE_DLLCHARACTERISTICS_EX_CET_SET_CONTEXT_IP_VALIDATION_RELAXED_MODE: IMAGE_DLL_CHARACTERISTICS = 4
IMAGE_DLLCHARACTERISTICS_EX_CET_DYNAMIC_APIS_ALLOW_IN_PROC: IMAGE_DLL_CHARACTERISTICS = 8
IMAGE_DLLCHARACTERISTICS_EX_CET_RESERVED_1: IMAGE_DLL_CHARACTERISTICS = 16
IMAGE_DLLCHARACTERISTICS_EX_CET_RESERVED_2: IMAGE_DLL_CHARACTERISTICS = 32
IMAGE_FILE_CHARACTERISTICS = UInt16
IMAGE_FILE_RELOCS_STRIPPED: IMAGE_FILE_CHARACTERISTICS = 1
IMAGE_FILE_EXECUTABLE_IMAGE: IMAGE_FILE_CHARACTERISTICS = 2
IMAGE_FILE_LINE_NUMS_STRIPPED: IMAGE_FILE_CHARACTERISTICS = 4
IMAGE_FILE_LOCAL_SYMS_STRIPPED: IMAGE_FILE_CHARACTERISTICS = 8
IMAGE_FILE_AGGRESIVE_WS_TRIM: IMAGE_FILE_CHARACTERISTICS = 16
IMAGE_FILE_LARGE_ADDRESS_AWARE: IMAGE_FILE_CHARACTERISTICS = 32
IMAGE_FILE_BYTES_REVERSED_LO: IMAGE_FILE_CHARACTERISTICS = 128
IMAGE_FILE_32BIT_MACHINE: IMAGE_FILE_CHARACTERISTICS = 256
IMAGE_FILE_DEBUG_STRIPPED: IMAGE_FILE_CHARACTERISTICS = 512
IMAGE_FILE_REMOVABLE_RUN_FROM_SWAP: IMAGE_FILE_CHARACTERISTICS = 1024
IMAGE_FILE_NET_RUN_FROM_SWAP: IMAGE_FILE_CHARACTERISTICS = 2048
IMAGE_FILE_SYSTEM: IMAGE_FILE_CHARACTERISTICS = 4096
IMAGE_FILE_DLL: IMAGE_FILE_CHARACTERISTICS = 8192
IMAGE_FILE_UP_SYSTEM_ONLY: IMAGE_FILE_CHARACTERISTICS = 16384
IMAGE_FILE_BYTES_REVERSED_HI: IMAGE_FILE_CHARACTERISTICS = 32768
IMAGE_FILE_CHARACTERISTICS2 = UInt32
IMAGE_FILE_RELOCS_STRIPPED2: IMAGE_FILE_CHARACTERISTICS2 = 1
IMAGE_FILE_EXECUTABLE_IMAGE2: IMAGE_FILE_CHARACTERISTICS2 = 2
IMAGE_FILE_LINE_NUMS_STRIPPED2: IMAGE_FILE_CHARACTERISTICS2 = 4
IMAGE_FILE_LOCAL_SYMS_STRIPPED2: IMAGE_FILE_CHARACTERISTICS2 = 8
IMAGE_FILE_AGGRESIVE_WS_TRIM2: IMAGE_FILE_CHARACTERISTICS2 = 16
IMAGE_FILE_LARGE_ADDRESS_AWARE2: IMAGE_FILE_CHARACTERISTICS2 = 32
IMAGE_FILE_BYTES_REVERSED_LO2: IMAGE_FILE_CHARACTERISTICS2 = 128
IMAGE_FILE_32BIT_MACHINE2: IMAGE_FILE_CHARACTERISTICS2 = 256
IMAGE_FILE_DEBUG_STRIPPED2: IMAGE_FILE_CHARACTERISTICS2 = 512
IMAGE_FILE_REMOVABLE_RUN_FROM_SWAP2: IMAGE_FILE_CHARACTERISTICS2 = 1024
IMAGE_FILE_NET_RUN_FROM_SWAP2: IMAGE_FILE_CHARACTERISTICS2 = 2048
IMAGE_FILE_SYSTEM_2: IMAGE_FILE_CHARACTERISTICS2 = 4096
IMAGE_FILE_DLL_2: IMAGE_FILE_CHARACTERISTICS2 = 8192
IMAGE_FILE_UP_SYSTEM_ONLY_2: IMAGE_FILE_CHARACTERISTICS2 = 16384
IMAGE_FILE_BYTES_REVERSED_HI_2: IMAGE_FILE_CHARACTERISTICS2 = 32768
class IMAGE_FILE_HEADER(EasyCastStructure):
    Machine: win32more.Windows.Win32.System.SystemInformation.IMAGE_FILE_MACHINE
    NumberOfSections: UInt16
    TimeDateStamp: UInt32
    PointerToSymbolTable: UInt32
    NumberOfSymbols: UInt32
    SizeOfOptionalHeader: UInt16
    Characteristics: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_FILE_CHARACTERISTICS
class IMAGE_FUNCTION_ENTRY(EasyCastStructure):
    StartingAddress: UInt32
    EndingAddress: UInt32
    EndOfPrologue: UInt32
class IMAGE_FUNCTION_ENTRY64(EasyCastStructure):
    StartingAddress: UInt64
    EndingAddress: UInt64
    Anonymous: _Anonymous_e__Union
    _pack_ = 4
    class _Anonymous_e__Union(EasyCastUnion):
        EndOfPrologue: UInt64
        UnwindInfoAddress: UInt64
        _pack_ = 4
class IMAGE_LOAD_CONFIG_CODE_INTEGRITY(EasyCastStructure):
    Flags: UInt16
    Catalog: UInt16
    CatalogOffset: UInt32
    Reserved: UInt32
class IMAGE_LOAD_CONFIG_DIRECTORY32(EasyCastStructure):
    Size: UInt32
    TimeDateStamp: UInt32
    MajorVersion: UInt16
    MinorVersion: UInt16
    GlobalFlagsClear: UInt32
    GlobalFlagsSet: UInt32
    CriticalSectionDefaultTimeout: UInt32
    DeCommitFreeBlockThreshold: UInt32
    DeCommitTotalFreeThreshold: UInt32
    LockPrefixTable: UInt32
    MaximumAllocationSize: UInt32
    VirtualMemoryThreshold: UInt32
    ProcessHeapFlags: UInt32
    ProcessAffinityMask: UInt32
    CSDVersion: UInt16
    DependentLoadFlags: UInt16
    EditList: UInt32
    SecurityCookie: UInt32
    SEHandlerTable: UInt32
    SEHandlerCount: UInt32
    GuardCFCheckFunctionPointer: UInt32
    GuardCFDispatchFunctionPointer: UInt32
    GuardCFFunctionTable: UInt32
    GuardCFFunctionCount: UInt32
    GuardFlags: UInt32
    CodeIntegrity: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_LOAD_CONFIG_CODE_INTEGRITY
    GuardAddressTakenIatEntryTable: UInt32
    GuardAddressTakenIatEntryCount: UInt32
    GuardLongJumpTargetTable: UInt32
    GuardLongJumpTargetCount: UInt32
    DynamicValueRelocTable: UInt32
    CHPEMetadataPointer: UInt32
    GuardRFFailureRoutine: UInt32
    GuardRFFailureRoutineFunctionPointer: UInt32
    DynamicValueRelocTableOffset: UInt32
    DynamicValueRelocTableSection: UInt16
    Reserved2: UInt16
    GuardRFVerifyStackPointerFunctionPointer: UInt32
    HotPatchTableOffset: UInt32
    Reserved3: UInt32
    EnclaveConfigurationPointer: UInt32
    VolatileMetadataPointer: UInt32
    GuardEHContinuationTable: UInt32
    GuardEHContinuationCount: UInt32
    GuardXFGCheckFunctionPointer: UInt32
    GuardXFGDispatchFunctionPointer: UInt32
    GuardXFGTableDispatchFunctionPointer: UInt32
    CastGuardOsDeterminedFailureMode: UInt32
    GuardMemcpyFunctionPointer: UInt32
class IMAGE_LOAD_CONFIG_DIRECTORY64(EasyCastStructure):
    Size: UInt32
    TimeDateStamp: UInt32
    MajorVersion: UInt16
    MinorVersion: UInt16
    GlobalFlagsClear: UInt32
    GlobalFlagsSet: UInt32
    CriticalSectionDefaultTimeout: UInt32
    DeCommitFreeBlockThreshold: UInt64
    DeCommitTotalFreeThreshold: UInt64
    LockPrefixTable: UInt64
    MaximumAllocationSize: UInt64
    VirtualMemoryThreshold: UInt64
    ProcessAffinityMask: UInt64
    ProcessHeapFlags: UInt32
    CSDVersion: UInt16
    DependentLoadFlags: UInt16
    EditList: UInt64
    SecurityCookie: UInt64
    SEHandlerTable: UInt64
    SEHandlerCount: UInt64
    GuardCFCheckFunctionPointer: UInt64
    GuardCFDispatchFunctionPointer: UInt64
    GuardCFFunctionTable: UInt64
    GuardCFFunctionCount: UInt64
    GuardFlags: UInt32
    CodeIntegrity: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_LOAD_CONFIG_CODE_INTEGRITY
    GuardAddressTakenIatEntryTable: UInt64
    GuardAddressTakenIatEntryCount: UInt64
    GuardLongJumpTargetTable: UInt64
    GuardLongJumpTargetCount: UInt64
    DynamicValueRelocTable: UInt64
    CHPEMetadataPointer: UInt64
    GuardRFFailureRoutine: UInt64
    GuardRFFailureRoutineFunctionPointer: UInt64
    DynamicValueRelocTableOffset: UInt32
    DynamicValueRelocTableSection: UInt16
    Reserved2: UInt16
    GuardRFVerifyStackPointerFunctionPointer: UInt64
    HotPatchTableOffset: UInt32
    Reserved3: UInt32
    EnclaveConfigurationPointer: UInt64
    VolatileMetadataPointer: UInt64
    GuardEHContinuationTable: UInt64
    GuardEHContinuationCount: UInt64
    GuardXFGCheckFunctionPointer: UInt64
    GuardXFGDispatchFunctionPointer: UInt64
    GuardXFGTableDispatchFunctionPointer: UInt64
    CastGuardOsDeterminedFailureMode: UInt64
    GuardMemcpyFunctionPointer: UInt64
    _pack_ = 4
class IMAGE_NT_HEADERS32(EasyCastStructure):
    Signature: UInt32
    FileHeader: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_FILE_HEADER
    OptionalHeader: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_OPTIONAL_HEADER32
class IMAGE_NT_HEADERS64(EasyCastStructure):
    Signature: UInt32
    FileHeader: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_FILE_HEADER
    OptionalHeader: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_OPTIONAL_HEADER64
class IMAGE_OPTIONAL_HEADER32(EasyCastStructure):
    Magic: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_OPTIONAL_HEADER_MAGIC
    MajorLinkerVersion: Byte
    MinorLinkerVersion: Byte
    SizeOfCode: UInt32
    SizeOfInitializedData: UInt32
    SizeOfUninitializedData: UInt32
    AddressOfEntryPoint: UInt32
    BaseOfCode: UInt32
    BaseOfData: UInt32
    ImageBase: UInt32
    SectionAlignment: UInt32
    FileAlignment: UInt32
    MajorOperatingSystemVersion: UInt16
    MinorOperatingSystemVersion: UInt16
    MajorImageVersion: UInt16
    MinorImageVersion: UInt16
    MajorSubsystemVersion: UInt16
    MinorSubsystemVersion: UInt16
    Win32VersionValue: UInt32
    SizeOfImage: UInt32
    SizeOfHeaders: UInt32
    CheckSum: UInt32
    Subsystem: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SUBSYSTEM
    DllCharacteristics: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DLL_CHARACTERISTICS
    SizeOfStackReserve: UInt32
    SizeOfStackCommit: UInt32
    SizeOfHeapReserve: UInt32
    SizeOfHeapCommit: UInt32
    LoaderFlags: UInt32
    NumberOfRvaAndSizes: UInt32
    DataDirectory: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DATA_DIRECTORY * 16
class IMAGE_OPTIONAL_HEADER64(EasyCastStructure):
    Magic: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_OPTIONAL_HEADER_MAGIC
    MajorLinkerVersion: Byte
    MinorLinkerVersion: Byte
    SizeOfCode: UInt32
    SizeOfInitializedData: UInt32
    SizeOfUninitializedData: UInt32
    AddressOfEntryPoint: UInt32
    BaseOfCode: UInt32
    ImageBase: UInt64
    SectionAlignment: UInt32
    FileAlignment: UInt32
    MajorOperatingSystemVersion: UInt16
    MinorOperatingSystemVersion: UInt16
    MajorImageVersion: UInt16
    MinorImageVersion: UInt16
    MajorSubsystemVersion: UInt16
    MinorSubsystemVersion: UInt16
    Win32VersionValue: UInt32
    SizeOfImage: UInt32
    SizeOfHeaders: UInt32
    CheckSum: UInt32
    Subsystem: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SUBSYSTEM
    DllCharacteristics: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DLL_CHARACTERISTICS
    SizeOfStackReserve: UInt64
    SizeOfStackCommit: UInt64
    SizeOfHeapReserve: UInt64
    SizeOfHeapCommit: UInt64
    LoaderFlags: UInt32
    NumberOfRvaAndSizes: UInt32
    DataDirectory: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DATA_DIRECTORY * 16
    _pack_ = 4
IMAGE_OPTIONAL_HEADER_MAGIC = UInt16
IMAGE_NT_OPTIONAL_HDR_MAGIC: IMAGE_OPTIONAL_HEADER_MAGIC = 523
IMAGE_NT_OPTIONAL_HDR32_MAGIC: IMAGE_OPTIONAL_HEADER_MAGIC = 267
IMAGE_NT_OPTIONAL_HDR64_MAGIC: IMAGE_OPTIONAL_HEADER_MAGIC = 523
IMAGE_ROM_OPTIONAL_HDR_MAGIC: IMAGE_OPTIONAL_HEADER_MAGIC = 263
class IMAGE_ROM_HEADERS(EasyCastStructure):
    FileHeader: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_FILE_HEADER
    OptionalHeader: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_ROM_OPTIONAL_HEADER
class IMAGE_ROM_OPTIONAL_HEADER(EasyCastStructure):
    Magic: UInt16
    MajorLinkerVersion: Byte
    MinorLinkerVersion: Byte
    SizeOfCode: UInt32
    SizeOfInitializedData: UInt32
    SizeOfUninitializedData: UInt32
    AddressOfEntryPoint: UInt32
    BaseOfCode: UInt32
    BaseOfData: UInt32
    BaseOfBss: UInt32
    GprMask: UInt32
    CprMask: UInt32 * 4
    GpValue: UInt32
class IMAGE_RUNTIME_FUNCTION_ENTRY(EasyCastStructure):
    BeginAddress: UInt32
    EndAddress: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        UnwindInfoAddress: UInt32
        UnwindData: UInt32
IMAGE_SECTION_CHARACTERISTICS = UInt32
IMAGE_SCN_TYPE_NO_PAD: IMAGE_SECTION_CHARACTERISTICS = 8
IMAGE_SCN_CNT_CODE: IMAGE_SECTION_CHARACTERISTICS = 32
IMAGE_SCN_CNT_INITIALIZED_DATA: IMAGE_SECTION_CHARACTERISTICS = 64
IMAGE_SCN_CNT_UNINITIALIZED_DATA: IMAGE_SECTION_CHARACTERISTICS = 128
IMAGE_SCN_LNK_OTHER: IMAGE_SECTION_CHARACTERISTICS = 256
IMAGE_SCN_LNK_INFO: IMAGE_SECTION_CHARACTERISTICS = 512
IMAGE_SCN_LNK_REMOVE: IMAGE_SECTION_CHARACTERISTICS = 2048
IMAGE_SCN_LNK_COMDAT: IMAGE_SECTION_CHARACTERISTICS = 4096
IMAGE_SCN_NO_DEFER_SPEC_EXC: IMAGE_SECTION_CHARACTERISTICS = 16384
IMAGE_SCN_GPREL: IMAGE_SECTION_CHARACTERISTICS = 32768
IMAGE_SCN_MEM_FARDATA: IMAGE_SECTION_CHARACTERISTICS = 32768
IMAGE_SCN_MEM_PURGEABLE: IMAGE_SECTION_CHARACTERISTICS = 131072
IMAGE_SCN_MEM_16BIT: IMAGE_SECTION_CHARACTERISTICS = 131072
IMAGE_SCN_MEM_LOCKED: IMAGE_SECTION_CHARACTERISTICS = 262144
IMAGE_SCN_MEM_PRELOAD: IMAGE_SECTION_CHARACTERISTICS = 524288
IMAGE_SCN_ALIGN_1BYTES: IMAGE_SECTION_CHARACTERISTICS = 1048576
IMAGE_SCN_ALIGN_2BYTES: IMAGE_SECTION_CHARACTERISTICS = 2097152
IMAGE_SCN_ALIGN_4BYTES: IMAGE_SECTION_CHARACTERISTICS = 3145728
IMAGE_SCN_ALIGN_8BYTES: IMAGE_SECTION_CHARACTERISTICS = 4194304
IMAGE_SCN_ALIGN_16BYTES: IMAGE_SECTION_CHARACTERISTICS = 5242880
IMAGE_SCN_ALIGN_32BYTES: IMAGE_SECTION_CHARACTERISTICS = 6291456
IMAGE_SCN_ALIGN_64BYTES: IMAGE_SECTION_CHARACTERISTICS = 7340032
IMAGE_SCN_ALIGN_128BYTES: IMAGE_SECTION_CHARACTERISTICS = 8388608
IMAGE_SCN_ALIGN_256BYTES: IMAGE_SECTION_CHARACTERISTICS = 9437184
IMAGE_SCN_ALIGN_512BYTES: IMAGE_SECTION_CHARACTERISTICS = 10485760
IMAGE_SCN_ALIGN_1024BYTES: IMAGE_SECTION_CHARACTERISTICS = 11534336
IMAGE_SCN_ALIGN_2048BYTES: IMAGE_SECTION_CHARACTERISTICS = 12582912
IMAGE_SCN_ALIGN_4096BYTES: IMAGE_SECTION_CHARACTERISTICS = 13631488
IMAGE_SCN_ALIGN_8192BYTES: IMAGE_SECTION_CHARACTERISTICS = 14680064
IMAGE_SCN_ALIGN_MASK: IMAGE_SECTION_CHARACTERISTICS = 15728640
IMAGE_SCN_LNK_NRELOC_OVFL: IMAGE_SECTION_CHARACTERISTICS = 16777216
IMAGE_SCN_MEM_DISCARDABLE: IMAGE_SECTION_CHARACTERISTICS = 33554432
IMAGE_SCN_MEM_NOT_CACHED: IMAGE_SECTION_CHARACTERISTICS = 67108864
IMAGE_SCN_MEM_NOT_PAGED: IMAGE_SECTION_CHARACTERISTICS = 134217728
IMAGE_SCN_MEM_SHARED: IMAGE_SECTION_CHARACTERISTICS = 268435456
IMAGE_SCN_MEM_EXECUTE: IMAGE_SECTION_CHARACTERISTICS = 536870912
IMAGE_SCN_MEM_READ: IMAGE_SECTION_CHARACTERISTICS = 1073741824
IMAGE_SCN_MEM_WRITE: IMAGE_SECTION_CHARACTERISTICS = 2147483648
IMAGE_SCN_SCALE_INDEX: IMAGE_SECTION_CHARACTERISTICS = 1
class IMAGE_SECTION_HEADER(EasyCastStructure):
    Name: Byte * 8
    Misc: _Misc_e__Union
    VirtualAddress: UInt32
    SizeOfRawData: UInt32
    PointerToRawData: UInt32
    PointerToRelocations: UInt32
    PointerToLinenumbers: UInt32
    NumberOfRelocations: UInt16
    NumberOfLinenumbers: UInt16
    Characteristics: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_CHARACTERISTICS
    class _Misc_e__Union(EasyCastUnion):
        PhysicalAddress: UInt32
        VirtualSize: UInt32
IMAGE_SUBSYSTEM = UInt16
IMAGE_SUBSYSTEM_UNKNOWN: IMAGE_SUBSYSTEM = 0
IMAGE_SUBSYSTEM_NATIVE: IMAGE_SUBSYSTEM = 1
IMAGE_SUBSYSTEM_WINDOWS_GUI: IMAGE_SUBSYSTEM = 2
IMAGE_SUBSYSTEM_WINDOWS_CUI: IMAGE_SUBSYSTEM = 3
IMAGE_SUBSYSTEM_OS2_CUI: IMAGE_SUBSYSTEM = 5
IMAGE_SUBSYSTEM_POSIX_CUI: IMAGE_SUBSYSTEM = 7
IMAGE_SUBSYSTEM_NATIVE_WINDOWS: IMAGE_SUBSYSTEM = 8
IMAGE_SUBSYSTEM_WINDOWS_CE_GUI: IMAGE_SUBSYSTEM = 9
IMAGE_SUBSYSTEM_EFI_APPLICATION: IMAGE_SUBSYSTEM = 10
IMAGE_SUBSYSTEM_EFI_BOOT_SERVICE_DRIVER: IMAGE_SUBSYSTEM = 11
IMAGE_SUBSYSTEM_EFI_RUNTIME_DRIVER: IMAGE_SUBSYSTEM = 12
IMAGE_SUBSYSTEM_EFI_ROM: IMAGE_SUBSYSTEM = 13
IMAGE_SUBSYSTEM_XBOX: IMAGE_SUBSYSTEM = 14
IMAGE_SUBSYSTEM_WINDOWS_BOOT_APPLICATION: IMAGE_SUBSYSTEM = 16
IMAGE_SUBSYSTEM_XBOX_CODE_CATALOG: IMAGE_SUBSYSTEM = 17
class IObjectSafety(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{cb5bdc81-93c1-11cf-8f20-00805f2cd064}')
    @commethod(3)
    def GetInterfaceSafetyOptions(self, riid: POINTER(Guid), pdwSupportedOptions: POINTER(UInt32), pdwEnabledOptions: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetInterfaceSafetyOptions(self, riid: POINTER(Guid), dwOptionSetMask: UInt32, dwEnabledOptions: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPMI_OS_SEL_RECORD(EasyCastStructure):
    Signature: UInt32
    Version: UInt32
    Length: UInt32
    RecordType: win32more.Windows.Win32.System.Diagnostics.Debug.IPMI_OS_SEL_RECORD_TYPE
    DataLength: UInt32
    Data: Byte * 1
    _pack_ = 1
IPMI_OS_SEL_RECORD_TYPE = Int32
IPMI_OS_SEL_RECORD_TYPE_IpmiOsSelRecordTypeWhea: IPMI_OS_SEL_RECORD_TYPE = 0
IPMI_OS_SEL_RECORD_TYPE_IpmiOsSelRecordTypeOther: IPMI_OS_SEL_RECORD_TYPE = 1
IPMI_OS_SEL_RECORD_TYPE_IpmiOsSelRecordTypeWheaErrorXpfMca: IPMI_OS_SEL_RECORD_TYPE = 2
IPMI_OS_SEL_RECORD_TYPE_IpmiOsSelRecordTypeWheaErrorPci: IPMI_OS_SEL_RECORD_TYPE = 3
IPMI_OS_SEL_RECORD_TYPE_IpmiOsSelRecordTypeWheaErrorNmi: IPMI_OS_SEL_RECORD_TYPE = 4
IPMI_OS_SEL_RECORD_TYPE_IpmiOsSelRecordTypeWheaErrorOther: IPMI_OS_SEL_RECORD_TYPE = 5
IPMI_OS_SEL_RECORD_TYPE_IpmiOsSelRecordTypeRaw: IPMI_OS_SEL_RECORD_TYPE = 6
IPMI_OS_SEL_RECORD_TYPE_IpmiOsSelRecordTypeDriver: IPMI_OS_SEL_RECORD_TYPE = 7
IPMI_OS_SEL_RECORD_TYPE_IpmiOsSelRecordTypeBugcheckRecovery: IPMI_OS_SEL_RECORD_TYPE = 8
IPMI_OS_SEL_RECORD_TYPE_IpmiOsSelRecordTypeBugcheckData: IPMI_OS_SEL_RECORD_TYPE = 9
IPMI_OS_SEL_RECORD_TYPE_IpmiOsSelRecordTypeMax: IPMI_OS_SEL_RECORD_TYPE = 10
class IPerPropertyBrowsing2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51973c54-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(3)
    def GetDisplayString(self, dispid: Int32, pBstr: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def MapPropertyToPage(self, dispid: Int32, pClsidPropPage: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPredefinedStrings(self, dispid: Int32, pCaStrings: POINTER(win32more.Windows.Win32.System.Ole.CALPOLESTR_head), pCaCookies: POINTER(win32more.Windows.Win32.System.Ole.CADWORD_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetPredefinedValue(self, dispid: Int32, dwCookie: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X86':
    class KDHELP(EasyCastStructure):
        Thread: UInt32
        ThCallbackStack: UInt32
        NextCallback: UInt32
        FramePointer: UInt32
        KiCallUserMode: UInt32
        KeUserCallbackDispatcher: UInt32
        SystemRangeStart: UInt32
        ThCallbackBStore: UInt32
        KiUserExceptionDispatcher: UInt32
        StackBase: UInt32
        StackLimit: UInt32
        Reserved: UInt32 * 5
class KDHELP64(EasyCastStructure):
    Thread: UInt64
    ThCallbackStack: UInt32
    ThCallbackBStore: UInt32
    NextCallback: UInt32
    FramePointer: UInt32
    KiCallUserMode: UInt64
    KeUserCallbackDispatcher: UInt64
    SystemRangeStart: UInt64
    KiUserExceptionDispatcher: UInt64
    StackBase: UInt64
    StackLimit: UInt64
    BuildVersion: UInt32
    RetpolineStubFunctionTableSize: UInt32
    RetpolineStubFunctionTable: UInt64
    RetpolineStubOffset: UInt32
    RetpolineStubSize: UInt32
    Reserved0: UInt64 * 2
if ARCH in 'X64':
    class KNONVOLATILE_CONTEXT_POINTERS(EasyCastStructure):
        Anonymous1: _Anonymous1_e__Union
        Anonymous2: _Anonymous2_e__Union
        class _Anonymous1_e__Union(EasyCastUnion):
            FloatingContext: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.M128A_head) * 16
            Anonymous: _Anonymous_e__Struct
            class _Anonymous_e__Struct(EasyCastStructure):
                Xmm0: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.M128A_head)
                Xmm1: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.M128A_head)
                Xmm2: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.M128A_head)
                Xmm3: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.M128A_head)
                Xmm4: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.M128A_head)
                Xmm5: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.M128A_head)
                Xmm6: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.M128A_head)
                Xmm7: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.M128A_head)
                Xmm8: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.M128A_head)
                Xmm9: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.M128A_head)
                Xmm10: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.M128A_head)
                Xmm11: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.M128A_head)
                Xmm12: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.M128A_head)
                Xmm13: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.M128A_head)
                Xmm14: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.M128A_head)
                Xmm15: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.M128A_head)
        class _Anonymous2_e__Union(EasyCastUnion):
            IntegerContext: POINTER(UInt64) * 16
            Anonymous: _Anonymous_e__Struct
            class _Anonymous_e__Struct(EasyCastStructure):
                Rax: POINTER(UInt64)
                Rcx: POINTER(UInt64)
                Rdx: POINTER(UInt64)
                Rbx: POINTER(UInt64)
                Rsp: POINTER(UInt64)
                Rbp: POINTER(UInt64)
                Rsi: POINTER(UInt64)
                Rdi: POINTER(UInt64)
                R8: POINTER(UInt64)
                R9: POINTER(UInt64)
                R10: POINTER(UInt64)
                R11: POINTER(UInt64)
                R12: POINTER(UInt64)
                R13: POINTER(UInt64)
                R14: POINTER(UInt64)
                R15: POINTER(UInt64)
if ARCH in 'X86':
    class KNONVOLATILE_CONTEXT_POINTERS(EasyCastStructure):
        Dummy: UInt32
if ARCH in 'ARM64':
    class KNONVOLATILE_CONTEXT_POINTERS_ARM64(EasyCastStructure):
        X19: POINTER(UInt64)
        X20: POINTER(UInt64)
        X21: POINTER(UInt64)
        X22: POINTER(UInt64)
        X23: POINTER(UInt64)
        X24: POINTER(UInt64)
        X25: POINTER(UInt64)
        X26: POINTER(UInt64)
        X27: POINTER(UInt64)
        X28: POINTER(UInt64)
        Fp: POINTER(UInt64)
        Lr: POINTER(UInt64)
        D8: POINTER(UInt64)
        D9: POINTER(UInt64)
        D10: POINTER(UInt64)
        D11: POINTER(UInt64)
        D12: POINTER(UInt64)
        D13: POINTER(UInt64)
        D14: POINTER(UInt64)
        D15: POINTER(UInt64)
class LDT_ENTRY(EasyCastStructure):
    LimitLow: UInt16
    BaseLow: UInt16
    HighWord: _HighWord_e__Union
    class _HighWord_e__Union(EasyCastUnion):
        Bytes: _Bytes_e__Struct
        Bits: _Bits_e__Struct
        class _Bytes_e__Struct(EasyCastStructure):
            BaseMid: Byte
            Flags1: Byte
            Flags2: Byte
            BaseHi: Byte
        class _Bits_e__Struct(EasyCastStructure):
            _bitfield: UInt32
if ARCH in 'X64,ARM64':
    class LOADED_IMAGE(EasyCastStructure):
        ModuleName: win32more.Windows.Win32.Foundation.PSTR
        hFile: win32more.Windows.Win32.Foundation.HANDLE
        MappedAddress: POINTER(Byte)
        FileHeader: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_NT_HEADERS64_head)
        LastRvaSection: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_HEADER_head)
        NumberOfSections: UInt32
        Sections: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_HEADER_head)
        Characteristics: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_FILE_CHARACTERISTICS2
        fSystemImage: win32more.Windows.Win32.Foundation.BOOLEAN
        fDOSImage: win32more.Windows.Win32.Foundation.BOOLEAN
        fReadOnly: win32more.Windows.Win32.Foundation.BOOLEAN
        Version: Byte
        Links: win32more.Windows.Win32.System.Kernel.LIST_ENTRY
        SizeOfImage: UInt32
if ARCH in 'X86':
    class LOADED_IMAGE(EasyCastStructure):
        ModuleName: win32more.Windows.Win32.Foundation.PSTR
        hFile: win32more.Windows.Win32.Foundation.HANDLE
        MappedAddress: POINTER(Byte)
        FileHeader: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_NT_HEADERS32_head)
        LastRvaSection: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_HEADER_head)
        NumberOfSections: UInt32
        Sections: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_HEADER_head)
        Characteristics: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_FILE_CHARACTERISTICS2
        fSystemImage: win32more.Windows.Win32.Foundation.BOOLEAN
        fDOSImage: win32more.Windows.Win32.Foundation.BOOLEAN
        fReadOnly: win32more.Windows.Win32.Foundation.BOOLEAN
        Version: Byte
        Links: win32more.Windows.Win32.System.Kernel.LIST_ENTRY
        SizeOfImage: UInt32
class LOAD_DLL_DEBUG_INFO(EasyCastStructure):
    hFile: win32more.Windows.Win32.Foundation.HANDLE
    lpBaseOfDll: VoidPtr
    dwDebugInfoFileOffset: UInt32
    nDebugInfoSize: UInt32
    lpImageName: VoidPtr
    fUnicode: UInt16
@winfunctype_pointer
def LPCALL_BACK_USER_INTERRUPT_ROUTINE() -> UInt32: ...
@winfunctype_pointer
def LPTOP_LEVEL_EXCEPTION_FILTER(ExceptionInfo: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.EXCEPTION_POINTERS_head)) -> Int32: ...
class M128A(EasyCastStructure):
    Low: UInt64
    High: Int64
if ARCH in 'X64,ARM64':
    class MINIDUMP_CALLBACK_INFORMATION(EasyCastStructure):
        CallbackRoutine: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_CALLBACK_ROUTINE
        CallbackParam: VoidPtr
        _pack_ = 4
if ARCH in 'X86':
    class MINIDUMP_CALLBACK_INFORMATION(EasyCastStructure):
        CallbackRoutine: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_CALLBACK_ROUTINE
        CallbackParam: VoidPtr
class MINIDUMP_CALLBACK_INPUT(EasyCastStructure):
    ProcessId: UInt32
    ProcessHandle: win32more.Windows.Win32.Foundation.HANDLE
    CallbackType: UInt32
    Anonymous: _Anonymous_e__Union
    _pack_ = 4
    class _Anonymous_e__Union(EasyCastUnion):
        Status: win32more.Windows.Win32.Foundation.HRESULT
        Thread: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_THREAD_CALLBACK
        ThreadEx: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_THREAD_EX_CALLBACK
        Module: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_MODULE_CALLBACK
        IncludeThread: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_INCLUDE_THREAD_CALLBACK
        IncludeModule: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_INCLUDE_MODULE_CALLBACK
        Io: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_IO_CALLBACK
        ReadMemoryFailure: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_READ_MEMORY_FAILURE_CALLBACK
        SecondaryFlags: UInt32
        VmQuery: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_VM_QUERY_CALLBACK
        VmPreRead: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_VM_PRE_READ_CALLBACK
        VmPostRead: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_VM_POST_READ_CALLBACK
class MINIDUMP_CALLBACK_OUTPUT(EasyCastStructure):
    Anonymous: _Anonymous_e__Union
    _pack_ = 4
    class _Anonymous_e__Union(EasyCastUnion):
        ModuleWriteFlags: UInt32
        ThreadWriteFlags: UInt32
        SecondaryFlags: UInt32
        Anonymous1: _Anonymous1_e__Struct
        Anonymous2: _Anonymous2_e__Struct
        Handle: win32more.Windows.Win32.Foundation.HANDLE
        Anonymous3: _Anonymous3_e__Struct
        Anonymous4: _Anonymous4_e__Struct
        Anonymous5: _Anonymous5_e__Struct
        Status: win32more.Windows.Win32.Foundation.HRESULT
        class _Anonymous1_e__Struct(EasyCastStructure):
            MemoryBase: UInt64
            MemorySize: UInt32
            _pack_ = 4
        class _Anonymous2_e__Struct(EasyCastStructure):
            CheckCancel: win32more.Windows.Win32.Foundation.BOOL
            Cancel: win32more.Windows.Win32.Foundation.BOOL
        class _Anonymous3_e__Struct(EasyCastStructure):
            VmRegion: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_MEMORY_INFO
            Continue: win32more.Windows.Win32.Foundation.BOOL
        class _Anonymous4_e__Struct(EasyCastStructure):
            VmQueryStatus: win32more.Windows.Win32.Foundation.HRESULT
            VmQueryResult: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_MEMORY_INFO
        class _Anonymous5_e__Struct(EasyCastStructure):
            VmReadStatus: win32more.Windows.Win32.Foundation.HRESULT
            VmReadBytesCompleted: UInt32
@winfunctype_pointer
def MINIDUMP_CALLBACK_ROUTINE(CallbackParam: VoidPtr, CallbackInput: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_CALLBACK_INPUT_head), CallbackOutput: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_CALLBACK_OUTPUT_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
MINIDUMP_CALLBACK_TYPE = Int32
MINIDUMP_CALLBACK_TYPE_ModuleCallback: MINIDUMP_CALLBACK_TYPE = 0
MINIDUMP_CALLBACK_TYPE_ThreadCallback: MINIDUMP_CALLBACK_TYPE = 1
MINIDUMP_CALLBACK_TYPE_ThreadExCallback: MINIDUMP_CALLBACK_TYPE = 2
MINIDUMP_CALLBACK_TYPE_IncludeThreadCallback: MINIDUMP_CALLBACK_TYPE = 3
MINIDUMP_CALLBACK_TYPE_IncludeModuleCallback: MINIDUMP_CALLBACK_TYPE = 4
MINIDUMP_CALLBACK_TYPE_MemoryCallback: MINIDUMP_CALLBACK_TYPE = 5
MINIDUMP_CALLBACK_TYPE_CancelCallback: MINIDUMP_CALLBACK_TYPE = 6
MINIDUMP_CALLBACK_TYPE_WriteKernelMinidumpCallback: MINIDUMP_CALLBACK_TYPE = 7
MINIDUMP_CALLBACK_TYPE_KernelMinidumpStatusCallback: MINIDUMP_CALLBACK_TYPE = 8
MINIDUMP_CALLBACK_TYPE_RemoveMemoryCallback: MINIDUMP_CALLBACK_TYPE = 9
MINIDUMP_CALLBACK_TYPE_IncludeVmRegionCallback: MINIDUMP_CALLBACK_TYPE = 10
MINIDUMP_CALLBACK_TYPE_IoStartCallback: MINIDUMP_CALLBACK_TYPE = 11
MINIDUMP_CALLBACK_TYPE_IoWriteAllCallback: MINIDUMP_CALLBACK_TYPE = 12
MINIDUMP_CALLBACK_TYPE_IoFinishCallback: MINIDUMP_CALLBACK_TYPE = 13
MINIDUMP_CALLBACK_TYPE_ReadMemoryFailureCallback: MINIDUMP_CALLBACK_TYPE = 14
MINIDUMP_CALLBACK_TYPE_SecondaryFlagsCallback: MINIDUMP_CALLBACK_TYPE = 15
MINIDUMP_CALLBACK_TYPE_IsProcessSnapshotCallback: MINIDUMP_CALLBACK_TYPE = 16
MINIDUMP_CALLBACK_TYPE_VmStartCallback: MINIDUMP_CALLBACK_TYPE = 17
MINIDUMP_CALLBACK_TYPE_VmQueryCallback: MINIDUMP_CALLBACK_TYPE = 18
MINIDUMP_CALLBACK_TYPE_VmPreReadCallback: MINIDUMP_CALLBACK_TYPE = 19
MINIDUMP_CALLBACK_TYPE_VmPostReadCallback: MINIDUMP_CALLBACK_TYPE = 20
class MINIDUMP_DIRECTORY(EasyCastStructure):
    StreamType: UInt32
    Location: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_LOCATION_DESCRIPTOR
    _pack_ = 4
class MINIDUMP_EXCEPTION(EasyCastStructure):
    ExceptionCode: UInt32
    ExceptionFlags: UInt32
    ExceptionRecord: UInt64
    ExceptionAddress: UInt64
    NumberParameters: UInt32
    __unusedAlignment: UInt32
    ExceptionInformation: UInt64 * 15
    _pack_ = 4
if ARCH in 'X64,ARM64':
    class MINIDUMP_EXCEPTION_INFORMATION(EasyCastStructure):
        ThreadId: UInt32
        ExceptionPointers: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.EXCEPTION_POINTERS_head)
        ClientPointers: win32more.Windows.Win32.Foundation.BOOL
        _pack_ = 4
if ARCH in 'X86':
    class MINIDUMP_EXCEPTION_INFORMATION(EasyCastStructure):
        ThreadId: UInt32
        ExceptionPointers: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.EXCEPTION_POINTERS_head)
        ClientPointers: win32more.Windows.Win32.Foundation.BOOL
class MINIDUMP_EXCEPTION_INFORMATION64(EasyCastStructure):
    ThreadId: UInt32
    ExceptionRecord: UInt64
    ContextRecord: UInt64
    ClientPointers: win32more.Windows.Win32.Foundation.BOOL
    _pack_ = 4
class MINIDUMP_EXCEPTION_STREAM(EasyCastStructure):
    ThreadId: UInt32
    __alignment: UInt32
    ExceptionRecord: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_EXCEPTION
    ThreadContext: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_LOCATION_DESCRIPTOR
    _pack_ = 4
class MINIDUMP_FUNCTION_TABLE_DESCRIPTOR(EasyCastStructure):
    MinimumAddress: UInt64
    MaximumAddress: UInt64
    BaseAddress: UInt64
    EntryCount: UInt32
    SizeOfAlignPad: UInt32
    _pack_ = 4
class MINIDUMP_FUNCTION_TABLE_STREAM(EasyCastStructure):
    SizeOfHeader: UInt32
    SizeOfDescriptor: UInt32
    SizeOfNativeDescriptor: UInt32
    SizeOfFunctionEntry: UInt32
    NumberOfDescriptors: UInt32
    SizeOfAlignPad: UInt32
    _pack_ = 4
class MINIDUMP_HANDLE_DATA_STREAM(EasyCastStructure):
    SizeOfHeader: UInt32
    SizeOfDescriptor: UInt32
    NumberOfDescriptors: UInt32
    Reserved: UInt32
    _pack_ = 4
class MINIDUMP_HANDLE_DESCRIPTOR(EasyCastStructure):
    Handle: UInt64
    TypeNameRva: UInt32
    ObjectNameRva: UInt32
    Attributes: UInt32
    GrantedAccess: UInt32
    HandleCount: UInt32
    PointerCount: UInt32
    _pack_ = 4
class MINIDUMP_HANDLE_DESCRIPTOR_2(EasyCastStructure):
    Handle: UInt64
    TypeNameRva: UInt32
    ObjectNameRva: UInt32
    Attributes: UInt32
    GrantedAccess: UInt32
    HandleCount: UInt32
    PointerCount: UInt32
    ObjectInfoRva: UInt32
    Reserved0: UInt32
    _pack_ = 4
class MINIDUMP_HANDLE_OBJECT_INFORMATION(EasyCastStructure):
    NextInfoRva: UInt32
    InfoType: UInt32
    SizeOfInfo: UInt32
    _pack_ = 4
MINIDUMP_HANDLE_OBJECT_INFORMATION_TYPE = Int32
MINIDUMP_HANDLE_OBJECT_INFORMATION_TYPE_MiniHandleObjectInformationNone: MINIDUMP_HANDLE_OBJECT_INFORMATION_TYPE = 0
MINIDUMP_HANDLE_OBJECT_INFORMATION_TYPE_MiniThreadInformation1: MINIDUMP_HANDLE_OBJECT_INFORMATION_TYPE = 1
MINIDUMP_HANDLE_OBJECT_INFORMATION_TYPE_MiniMutantInformation1: MINIDUMP_HANDLE_OBJECT_INFORMATION_TYPE = 2
MINIDUMP_HANDLE_OBJECT_INFORMATION_TYPE_MiniMutantInformation2: MINIDUMP_HANDLE_OBJECT_INFORMATION_TYPE = 3
MINIDUMP_HANDLE_OBJECT_INFORMATION_TYPE_MiniProcessInformation1: MINIDUMP_HANDLE_OBJECT_INFORMATION_TYPE = 4
MINIDUMP_HANDLE_OBJECT_INFORMATION_TYPE_MiniProcessInformation2: MINIDUMP_HANDLE_OBJECT_INFORMATION_TYPE = 5
MINIDUMP_HANDLE_OBJECT_INFORMATION_TYPE_MiniEventInformation1: MINIDUMP_HANDLE_OBJECT_INFORMATION_TYPE = 6
MINIDUMP_HANDLE_OBJECT_INFORMATION_TYPE_MiniSectionInformation1: MINIDUMP_HANDLE_OBJECT_INFORMATION_TYPE = 7
MINIDUMP_HANDLE_OBJECT_INFORMATION_TYPE_MiniSemaphoreInformation1: MINIDUMP_HANDLE_OBJECT_INFORMATION_TYPE = 8
MINIDUMP_HANDLE_OBJECT_INFORMATION_TYPE_MiniHandleObjectInformationTypeMax: MINIDUMP_HANDLE_OBJECT_INFORMATION_TYPE = 9
class MINIDUMP_HANDLE_OPERATION_LIST(EasyCastStructure):
    SizeOfHeader: UInt32
    SizeOfEntry: UInt32
    NumberOfEntries: UInt32
    Reserved: UInt32
    _pack_ = 4
class MINIDUMP_HEADER(EasyCastStructure):
    Signature: UInt32
    Version: UInt32
    NumberOfStreams: UInt32
    StreamDirectoryRva: UInt32
    CheckSum: UInt32
    Anonymous: _Anonymous_e__Union
    Flags: UInt64
    _pack_ = 4
    class _Anonymous_e__Union(EasyCastUnion):
        Reserved: UInt32
        TimeDateStamp: UInt32
class MINIDUMP_INCLUDE_MODULE_CALLBACK(EasyCastStructure):
    BaseOfImage: UInt64
    _pack_ = 4
class MINIDUMP_INCLUDE_THREAD_CALLBACK(EasyCastStructure):
    ThreadId: UInt32
    _pack_ = 4
class MINIDUMP_IO_CALLBACK(EasyCastStructure):
    Handle: win32more.Windows.Win32.Foundation.HANDLE
    Offset: UInt64
    Buffer: VoidPtr
    BufferBytes: UInt32
    _pack_ = 4
class MINIDUMP_LOCATION_DESCRIPTOR(EasyCastStructure):
    DataSize: UInt32
    Rva: UInt32
    _pack_ = 4
class MINIDUMP_LOCATION_DESCRIPTOR64(EasyCastStructure):
    DataSize: UInt64
    Rva: UInt64
    _pack_ = 4
class MINIDUMP_MEMORY64_LIST(EasyCastStructure):
    NumberOfMemoryRanges: UInt64
    BaseRva: UInt64
    MemoryRanges: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_MEMORY_DESCRIPTOR64 * 1
    _pack_ = 4
class MINIDUMP_MEMORY_DESCRIPTOR(EasyCastStructure):
    StartOfMemoryRange: UInt64
    Memory: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_LOCATION_DESCRIPTOR
    _pack_ = 4
class MINIDUMP_MEMORY_DESCRIPTOR64(EasyCastStructure):
    StartOfMemoryRange: UInt64
    DataSize: UInt64
    _pack_ = 4
class MINIDUMP_MEMORY_INFO(EasyCastStructure):
    BaseAddress: UInt64
    AllocationBase: UInt64
    AllocationProtect: UInt32
    __alignment1: UInt32
    RegionSize: UInt64
    State: win32more.Windows.Win32.System.Memory.VIRTUAL_ALLOCATION_TYPE
    Protect: UInt32
    Type: UInt32
    __alignment2: UInt32
    _pack_ = 4
class MINIDUMP_MEMORY_INFO_LIST(EasyCastStructure):
    SizeOfHeader: UInt32
    SizeOfEntry: UInt32
    NumberOfEntries: UInt64
    _pack_ = 4
class MINIDUMP_MEMORY_LIST(EasyCastStructure):
    NumberOfMemoryRanges: UInt32
    MemoryRanges: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_MEMORY_DESCRIPTOR * 1
    _pack_ = 4
class MINIDUMP_MISC_INFO(EasyCastStructure):
    SizeOfInfo: UInt32
    Flags1: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_MISC_INFO_FLAGS
    ProcessId: UInt32
    ProcessCreateTime: UInt32
    ProcessUserTime: UInt32
    ProcessKernelTime: UInt32
    _pack_ = 4
class MINIDUMP_MISC_INFO_2(EasyCastStructure):
    SizeOfInfo: UInt32
    Flags1: UInt32
    ProcessId: UInt32
    ProcessCreateTime: UInt32
    ProcessUserTime: UInt32
    ProcessKernelTime: UInt32
    ProcessorMaxMhz: UInt32
    ProcessorCurrentMhz: UInt32
    ProcessorMhzLimit: UInt32
    ProcessorMaxIdleState: UInt32
    ProcessorCurrentIdleState: UInt32
    _pack_ = 4
class MINIDUMP_MISC_INFO_3(EasyCastStructure):
    SizeOfInfo: UInt32
    Flags1: UInt32
    ProcessId: UInt32
    ProcessCreateTime: UInt32
    ProcessUserTime: UInt32
    ProcessKernelTime: UInt32
    ProcessorMaxMhz: UInt32
    ProcessorCurrentMhz: UInt32
    ProcessorMhzLimit: UInt32
    ProcessorMaxIdleState: UInt32
    ProcessorCurrentIdleState: UInt32
    ProcessIntegrityLevel: UInt32
    ProcessExecuteFlags: UInt32
    ProtectedProcess: UInt32
    TimeZoneId: UInt32
    TimeZone: win32more.Windows.Win32.System.Time.TIME_ZONE_INFORMATION
    _pack_ = 4
class MINIDUMP_MISC_INFO_4(EasyCastStructure):
    SizeOfInfo: UInt32
    Flags1: UInt32
    ProcessId: UInt32
    ProcessCreateTime: UInt32
    ProcessUserTime: UInt32
    ProcessKernelTime: UInt32
    ProcessorMaxMhz: UInt32
    ProcessorCurrentMhz: UInt32
    ProcessorMhzLimit: UInt32
    ProcessorMaxIdleState: UInt32
    ProcessorCurrentIdleState: UInt32
    ProcessIntegrityLevel: UInt32
    ProcessExecuteFlags: UInt32
    ProtectedProcess: UInt32
    TimeZoneId: UInt32
    TimeZone: win32more.Windows.Win32.System.Time.TIME_ZONE_INFORMATION
    BuildString: Char * 260
    DbgBldStr: Char * 40
    _pack_ = 4
class MINIDUMP_MISC_INFO_5(EasyCastStructure):
    SizeOfInfo: UInt32
    Flags1: UInt32
    ProcessId: UInt32
    ProcessCreateTime: UInt32
    ProcessUserTime: UInt32
    ProcessKernelTime: UInt32
    ProcessorMaxMhz: UInt32
    ProcessorCurrentMhz: UInt32
    ProcessorMhzLimit: UInt32
    ProcessorMaxIdleState: UInt32
    ProcessorCurrentIdleState: UInt32
    ProcessIntegrityLevel: UInt32
    ProcessExecuteFlags: UInt32
    ProtectedProcess: UInt32
    TimeZoneId: UInt32
    TimeZone: win32more.Windows.Win32.System.Time.TIME_ZONE_INFORMATION
    BuildString: Char * 260
    DbgBldStr: Char * 40
    XStateData: win32more.Windows.Win32.System.Diagnostics.Debug.XSTATE_CONFIG_FEATURE_MSC_INFO
    ProcessCookie: UInt32
    _pack_ = 4
MINIDUMP_MISC_INFO_FLAGS = UInt32
MINIDUMP_MISC1_PROCESS_ID: MINIDUMP_MISC_INFO_FLAGS = 1
MINIDUMP_MISC1_PROCESS_TIMES: MINIDUMP_MISC_INFO_FLAGS = 2
class MINIDUMP_MODULE(EasyCastStructure):
    BaseOfImage: UInt64
    SizeOfImage: UInt32
    CheckSum: UInt32
    TimeDateStamp: UInt32
    ModuleNameRva: UInt32
    VersionInfo: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO
    CvRecord: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_LOCATION_DESCRIPTOR
    MiscRecord: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_LOCATION_DESCRIPTOR
    Reserved0: UInt64
    Reserved1: UInt64
    _pack_ = 4
class MINIDUMP_MODULE_CALLBACK(EasyCastStructure):
    FullPath: win32more.Windows.Win32.Foundation.PWSTR
    BaseOfImage: UInt64
    SizeOfImage: UInt32
    CheckSum: UInt32
    TimeDateStamp: UInt32
    VersionInfo: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO
    CvRecord: VoidPtr
    SizeOfCvRecord: UInt32
    MiscRecord: VoidPtr
    SizeOfMiscRecord: UInt32
    _pack_ = 4
class MINIDUMP_MODULE_LIST(EasyCastStructure):
    NumberOfModules: UInt32
    Modules: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_MODULE * 1
    _pack_ = 4
class MINIDUMP_PROCESS_VM_COUNTERS_1(EasyCastStructure):
    Revision: UInt16
    PageFaultCount: UInt32
    PeakWorkingSetSize: UInt64
    WorkingSetSize: UInt64
    QuotaPeakPagedPoolUsage: UInt64
    QuotaPagedPoolUsage: UInt64
    QuotaPeakNonPagedPoolUsage: UInt64
    QuotaNonPagedPoolUsage: UInt64
    PagefileUsage: UInt64
    PeakPagefileUsage: UInt64
    PrivateUsage: UInt64
    _pack_ = 4
class MINIDUMP_PROCESS_VM_COUNTERS_2(EasyCastStructure):
    Revision: UInt16
    Flags: UInt16
    PageFaultCount: UInt32
    PeakWorkingSetSize: UInt64
    WorkingSetSize: UInt64
    QuotaPeakPagedPoolUsage: UInt64
    QuotaPagedPoolUsage: UInt64
    QuotaPeakNonPagedPoolUsage: UInt64
    QuotaNonPagedPoolUsage: UInt64
    PagefileUsage: UInt64
    PeakPagefileUsage: UInt64
    PeakVirtualSize: UInt64
    VirtualSize: UInt64
    PrivateUsage: UInt64
    PrivateWorkingSetSize: UInt64
    SharedCommitUsage: UInt64
    JobSharedCommitUsage: UInt64
    JobPrivateCommitUsage: UInt64
    JobPeakPrivateCommitUsage: UInt64
    JobPrivateCommitLimit: UInt64
    JobTotalCommitLimit: UInt64
    _pack_ = 4
class MINIDUMP_READ_MEMORY_FAILURE_CALLBACK(EasyCastStructure):
    Offset: UInt64
    Bytes: UInt32
    FailureStatus: win32more.Windows.Win32.Foundation.HRESULT
    _pack_ = 4
MINIDUMP_SECONDARY_FLAGS = Int32
MINIDUMP_SECONDARY_FLAGS_MiniSecondaryWithoutPowerInfo: MINIDUMP_SECONDARY_FLAGS = 1
MINIDUMP_SECONDARY_FLAGS_MiniSecondaryValidFlags: MINIDUMP_SECONDARY_FLAGS = 1
MINIDUMP_STREAM_TYPE = Int32
MINIDUMP_STREAM_TYPE_UnusedStream: MINIDUMP_STREAM_TYPE = 0
MINIDUMP_STREAM_TYPE_ReservedStream0: MINIDUMP_STREAM_TYPE = 1
MINIDUMP_STREAM_TYPE_ReservedStream1: MINIDUMP_STREAM_TYPE = 2
MINIDUMP_STREAM_TYPE_ThreadListStream: MINIDUMP_STREAM_TYPE = 3
MINIDUMP_STREAM_TYPE_ModuleListStream: MINIDUMP_STREAM_TYPE = 4
MINIDUMP_STREAM_TYPE_MemoryListStream: MINIDUMP_STREAM_TYPE = 5
MINIDUMP_STREAM_TYPE_ExceptionStream: MINIDUMP_STREAM_TYPE = 6
MINIDUMP_STREAM_TYPE_SystemInfoStream: MINIDUMP_STREAM_TYPE = 7
MINIDUMP_STREAM_TYPE_ThreadExListStream: MINIDUMP_STREAM_TYPE = 8
MINIDUMP_STREAM_TYPE_Memory64ListStream: MINIDUMP_STREAM_TYPE = 9
MINIDUMP_STREAM_TYPE_CommentStreamA: MINIDUMP_STREAM_TYPE = 10
MINIDUMP_STREAM_TYPE_CommentStreamW: MINIDUMP_STREAM_TYPE = 11
MINIDUMP_STREAM_TYPE_HandleDataStream: MINIDUMP_STREAM_TYPE = 12
MINIDUMP_STREAM_TYPE_FunctionTableStream: MINIDUMP_STREAM_TYPE = 13
MINIDUMP_STREAM_TYPE_UnloadedModuleListStream: MINIDUMP_STREAM_TYPE = 14
MINIDUMP_STREAM_TYPE_MiscInfoStream: MINIDUMP_STREAM_TYPE = 15
MINIDUMP_STREAM_TYPE_MemoryInfoListStream: MINIDUMP_STREAM_TYPE = 16
MINIDUMP_STREAM_TYPE_ThreadInfoListStream: MINIDUMP_STREAM_TYPE = 17
MINIDUMP_STREAM_TYPE_HandleOperationListStream: MINIDUMP_STREAM_TYPE = 18
MINIDUMP_STREAM_TYPE_TokenStream: MINIDUMP_STREAM_TYPE = 19
MINIDUMP_STREAM_TYPE_JavaScriptDataStream: MINIDUMP_STREAM_TYPE = 20
MINIDUMP_STREAM_TYPE_SystemMemoryInfoStream: MINIDUMP_STREAM_TYPE = 21
MINIDUMP_STREAM_TYPE_ProcessVmCountersStream: MINIDUMP_STREAM_TYPE = 22
MINIDUMP_STREAM_TYPE_IptTraceStream: MINIDUMP_STREAM_TYPE = 23
MINIDUMP_STREAM_TYPE_ThreadNamesStream: MINIDUMP_STREAM_TYPE = 24
MINIDUMP_STREAM_TYPE_ceStreamNull: MINIDUMP_STREAM_TYPE = 32768
MINIDUMP_STREAM_TYPE_ceStreamSystemInfo: MINIDUMP_STREAM_TYPE = 32769
MINIDUMP_STREAM_TYPE_ceStreamException: MINIDUMP_STREAM_TYPE = 32770
MINIDUMP_STREAM_TYPE_ceStreamModuleList: MINIDUMP_STREAM_TYPE = 32771
MINIDUMP_STREAM_TYPE_ceStreamProcessList: MINIDUMP_STREAM_TYPE = 32772
MINIDUMP_STREAM_TYPE_ceStreamThreadList: MINIDUMP_STREAM_TYPE = 32773
MINIDUMP_STREAM_TYPE_ceStreamThreadContextList: MINIDUMP_STREAM_TYPE = 32774
MINIDUMP_STREAM_TYPE_ceStreamThreadCallStackList: MINIDUMP_STREAM_TYPE = 32775
MINIDUMP_STREAM_TYPE_ceStreamMemoryVirtualList: MINIDUMP_STREAM_TYPE = 32776
MINIDUMP_STREAM_TYPE_ceStreamMemoryPhysicalList: MINIDUMP_STREAM_TYPE = 32777
MINIDUMP_STREAM_TYPE_ceStreamBucketParameters: MINIDUMP_STREAM_TYPE = 32778
MINIDUMP_STREAM_TYPE_ceStreamProcessModuleMap: MINIDUMP_STREAM_TYPE = 32779
MINIDUMP_STREAM_TYPE_ceStreamDiagnosisList: MINIDUMP_STREAM_TYPE = 32780
MINIDUMP_STREAM_TYPE_LastReservedStream: MINIDUMP_STREAM_TYPE = 65535
class MINIDUMP_STRING(EasyCastStructure):
    Length: UInt32
    Buffer: Char * 1
    _pack_ = 4
class MINIDUMP_SYSTEM_BASIC_INFORMATION(EasyCastStructure):
    TimerResolution: UInt32
    PageSize: UInt32
    NumberOfPhysicalPages: UInt32
    LowestPhysicalPageNumber: UInt32
    HighestPhysicalPageNumber: UInt32
    AllocationGranularity: UInt32
    MinimumUserModeAddress: UInt64
    MaximumUserModeAddress: UInt64
    ActiveProcessorsAffinityMask: UInt64
    NumberOfProcessors: UInt32
    _pack_ = 4
class MINIDUMP_SYSTEM_BASIC_PERFORMANCE_INFORMATION(EasyCastStructure):
    AvailablePages: UInt64
    CommittedPages: UInt64
    CommitLimit: UInt64
    PeakCommitment: UInt64
    _pack_ = 4
class MINIDUMP_SYSTEM_FILECACHE_INFORMATION(EasyCastStructure):
    CurrentSize: UInt64
    PeakSize: UInt64
    PageFaultCount: UInt32
    MinimumWorkingSet: UInt64
    MaximumWorkingSet: UInt64
    CurrentSizeIncludingTransitionInPages: UInt64
    PeakSizeIncludingTransitionInPages: UInt64
    TransitionRePurposeCount: UInt32
    Flags: UInt32
    _pack_ = 4
class MINIDUMP_SYSTEM_INFO(EasyCastStructure):
    ProcessorArchitecture: win32more.Windows.Win32.System.SystemInformation.PROCESSOR_ARCHITECTURE
    ProcessorLevel: UInt16
    ProcessorRevision: UInt16
    Anonymous1: _Anonymous1_e__Union
    MajorVersion: UInt32
    MinorVersion: UInt32
    BuildNumber: UInt32
    PlatformId: win32more.Windows.Win32.System.Diagnostics.Debug.VER_PLATFORM
    CSDVersionRva: UInt32
    Anonymous2: _Anonymous2_e__Union
    Cpu: win32more.Windows.Win32.System.Diagnostics.Debug.CPU_INFORMATION
    _pack_ = 4
    class _Anonymous1_e__Union(EasyCastUnion):
        Reserved0: UInt16
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(EasyCastStructure):
            NumberOfProcessors: Byte
            ProductType: Byte
    class _Anonymous2_e__Union(EasyCastUnion):
        Reserved1: UInt32
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(EasyCastStructure):
            SuiteMask: UInt16
            Reserved2: UInt16
class MINIDUMP_SYSTEM_MEMORY_INFO_1(EasyCastStructure):
    Revision: UInt16
    Flags: UInt16
    BasicInfo: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_SYSTEM_BASIC_INFORMATION
    FileCacheInfo: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_SYSTEM_FILECACHE_INFORMATION
    BasicPerfInfo: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_SYSTEM_BASIC_PERFORMANCE_INFORMATION
    PerfInfo: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_SYSTEM_PERFORMANCE_INFORMATION
    _pack_ = 4
class MINIDUMP_SYSTEM_PERFORMANCE_INFORMATION(EasyCastStructure):
    IdleProcessTime: UInt64
    IoReadTransferCount: UInt64
    IoWriteTransferCount: UInt64
    IoOtherTransferCount: UInt64
    IoReadOperationCount: UInt32
    IoWriteOperationCount: UInt32
    IoOtherOperationCount: UInt32
    AvailablePages: UInt32
    CommittedPages: UInt32
    CommitLimit: UInt32
    PeakCommitment: UInt32
    PageFaultCount: UInt32
    CopyOnWriteCount: UInt32
    TransitionCount: UInt32
    CacheTransitionCount: UInt32
    DemandZeroCount: UInt32
    PageReadCount: UInt32
    PageReadIoCount: UInt32
    CacheReadCount: UInt32
    CacheIoCount: UInt32
    DirtyPagesWriteCount: UInt32
    DirtyWriteIoCount: UInt32
    MappedPagesWriteCount: UInt32
    MappedWriteIoCount: UInt32
    PagedPoolPages: UInt32
    NonPagedPoolPages: UInt32
    PagedPoolAllocs: UInt32
    PagedPoolFrees: UInt32
    NonPagedPoolAllocs: UInt32
    NonPagedPoolFrees: UInt32
    FreeSystemPtes: UInt32
    ResidentSystemCodePage: UInt32
    TotalSystemDriverPages: UInt32
    TotalSystemCodePages: UInt32
    NonPagedPoolLookasideHits: UInt32
    PagedPoolLookasideHits: UInt32
    AvailablePagedPoolPages: UInt32
    ResidentSystemCachePage: UInt32
    ResidentPagedPoolPage: UInt32
    ResidentSystemDriverPage: UInt32
    CcFastReadNoWait: UInt32
    CcFastReadWait: UInt32
    CcFastReadResourceMiss: UInt32
    CcFastReadNotPossible: UInt32
    CcFastMdlReadNoWait: UInt32
    CcFastMdlReadWait: UInt32
    CcFastMdlReadResourceMiss: UInt32
    CcFastMdlReadNotPossible: UInt32
    CcMapDataNoWait: UInt32
    CcMapDataWait: UInt32
    CcMapDataNoWaitMiss: UInt32
    CcMapDataWaitMiss: UInt32
    CcPinMappedDataCount: UInt32
    CcPinReadNoWait: UInt32
    CcPinReadWait: UInt32
    CcPinReadNoWaitMiss: UInt32
    CcPinReadWaitMiss: UInt32
    CcCopyReadNoWait: UInt32
    CcCopyReadWait: UInt32
    CcCopyReadNoWaitMiss: UInt32
    CcCopyReadWaitMiss: UInt32
    CcMdlReadNoWait: UInt32
    CcMdlReadWait: UInt32
    CcMdlReadNoWaitMiss: UInt32
    CcMdlReadWaitMiss: UInt32
    CcReadAheadIos: UInt32
    CcLazyWriteIos: UInt32
    CcLazyWritePages: UInt32
    CcDataFlushes: UInt32
    CcDataPages: UInt32
    ContextSwitches: UInt32
    FirstLevelTbFills: UInt32
    SecondLevelTbFills: UInt32
    SystemCalls: UInt32
    CcTotalDirtyPages: UInt64
    CcDirtyPageThreshold: UInt64
    ResidentAvailablePages: Int64
    SharedCommittedPages: UInt64
    _pack_ = 4
class MINIDUMP_THREAD(EasyCastStructure):
    ThreadId: UInt32
    SuspendCount: UInt32
    PriorityClass: UInt32
    Priority: UInt32
    Teb: UInt64
    Stack: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_MEMORY_DESCRIPTOR
    ThreadContext: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_LOCATION_DESCRIPTOR
    _pack_ = 4
if ARCH in 'ARM64':
    class MINIDUMP_THREAD_CALLBACK(EasyCastStructure):
        ThreadId: UInt32
        ThreadHandle: win32more.Windows.Win32.Foundation.HANDLE
        Pad: UInt32
        Context: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT
        SizeOfContext: UInt32
        StackBase: UInt64
        StackEnd: UInt64
        _pack_ = 4
if ARCH in 'X86,X64':
    class MINIDUMP_THREAD_CALLBACK(EasyCastStructure):
        ThreadId: UInt32
        ThreadHandle: win32more.Windows.Win32.Foundation.HANDLE
        Context: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT
        SizeOfContext: UInt32
        StackBase: UInt64
        StackEnd: UInt64
        _pack_ = 4
class MINIDUMP_THREAD_EX(EasyCastStructure):
    ThreadId: UInt32
    SuspendCount: UInt32
    PriorityClass: UInt32
    Priority: UInt32
    Teb: UInt64
    Stack: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_MEMORY_DESCRIPTOR
    ThreadContext: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_LOCATION_DESCRIPTOR
    BackingStore: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_MEMORY_DESCRIPTOR
    _pack_ = 4
if ARCH in 'ARM64':
    class MINIDUMP_THREAD_EX_CALLBACK(EasyCastStructure):
        ThreadId: UInt32
        ThreadHandle: win32more.Windows.Win32.Foundation.HANDLE
        Pad: UInt32
        Context: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT
        SizeOfContext: UInt32
        StackBase: UInt64
        StackEnd: UInt64
        BackingStoreBase: UInt64
        BackingStoreEnd: UInt64
        _pack_ = 4
if ARCH in 'X86,X64':
    class MINIDUMP_THREAD_EX_CALLBACK(EasyCastStructure):
        ThreadId: UInt32
        ThreadHandle: win32more.Windows.Win32.Foundation.HANDLE
        Context: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT
        SizeOfContext: UInt32
        StackBase: UInt64
        StackEnd: UInt64
        BackingStoreBase: UInt64
        BackingStoreEnd: UInt64
        _pack_ = 4
class MINIDUMP_THREAD_EX_LIST(EasyCastStructure):
    NumberOfThreads: UInt32
    Threads: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_THREAD_EX * 1
    _pack_ = 4
class MINIDUMP_THREAD_INFO(EasyCastStructure):
    ThreadId: UInt32
    DumpFlags: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_THREAD_INFO_DUMP_FLAGS
    DumpError: UInt32
    ExitStatus: UInt32
    CreateTime: UInt64
    ExitTime: UInt64
    KernelTime: UInt64
    UserTime: UInt64
    StartAddress: UInt64
    Affinity: UInt64
    _pack_ = 4
MINIDUMP_THREAD_INFO_DUMP_FLAGS = UInt32
MINIDUMP_THREAD_INFO_ERROR_THREAD: MINIDUMP_THREAD_INFO_DUMP_FLAGS = 1
MINIDUMP_THREAD_INFO_EXITED_THREAD: MINIDUMP_THREAD_INFO_DUMP_FLAGS = 4
MINIDUMP_THREAD_INFO_INVALID_CONTEXT: MINIDUMP_THREAD_INFO_DUMP_FLAGS = 16
MINIDUMP_THREAD_INFO_INVALID_INFO: MINIDUMP_THREAD_INFO_DUMP_FLAGS = 8
MINIDUMP_THREAD_INFO_INVALID_TEB: MINIDUMP_THREAD_INFO_DUMP_FLAGS = 32
MINIDUMP_THREAD_INFO_WRITING_THREAD: MINIDUMP_THREAD_INFO_DUMP_FLAGS = 2
class MINIDUMP_THREAD_INFO_LIST(EasyCastStructure):
    SizeOfHeader: UInt32
    SizeOfEntry: UInt32
    NumberOfEntries: UInt32
    _pack_ = 4
class MINIDUMP_THREAD_LIST(EasyCastStructure):
    NumberOfThreads: UInt32
    Threads: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_THREAD * 1
    _pack_ = 4
class MINIDUMP_THREAD_NAME(EasyCastStructure):
    ThreadId: UInt32
    RvaOfThreadName: UInt64
    _pack_ = 4
class MINIDUMP_THREAD_NAME_LIST(EasyCastStructure):
    NumberOfThreadNames: UInt32
    ThreadNames: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_THREAD_NAME * 1
    _pack_ = 4
class MINIDUMP_TOKEN_INFO_HEADER(EasyCastStructure):
    TokenSize: UInt32
    TokenId: UInt32
    TokenHandle: UInt64
    _pack_ = 4
class MINIDUMP_TOKEN_INFO_LIST(EasyCastStructure):
    TokenListSize: UInt32
    TokenListEntries: UInt32
    ListHeaderSize: UInt32
    ElementHeaderSize: UInt32
    _pack_ = 4
MINIDUMP_TYPE = Int32
MINIDUMP_TYPE_MiniDumpNormal: MINIDUMP_TYPE = 0
MINIDUMP_TYPE_MiniDumpWithDataSegs: MINIDUMP_TYPE = 1
MINIDUMP_TYPE_MiniDumpWithFullMemory: MINIDUMP_TYPE = 2
MINIDUMP_TYPE_MiniDumpWithHandleData: MINIDUMP_TYPE = 4
MINIDUMP_TYPE_MiniDumpFilterMemory: MINIDUMP_TYPE = 8
MINIDUMP_TYPE_MiniDumpScanMemory: MINIDUMP_TYPE = 16
MINIDUMP_TYPE_MiniDumpWithUnloadedModules: MINIDUMP_TYPE = 32
MINIDUMP_TYPE_MiniDumpWithIndirectlyReferencedMemory: MINIDUMP_TYPE = 64
MINIDUMP_TYPE_MiniDumpFilterModulePaths: MINIDUMP_TYPE = 128
MINIDUMP_TYPE_MiniDumpWithProcessThreadData: MINIDUMP_TYPE = 256
MINIDUMP_TYPE_MiniDumpWithPrivateReadWriteMemory: MINIDUMP_TYPE = 512
MINIDUMP_TYPE_MiniDumpWithoutOptionalData: MINIDUMP_TYPE = 1024
MINIDUMP_TYPE_MiniDumpWithFullMemoryInfo: MINIDUMP_TYPE = 2048
MINIDUMP_TYPE_MiniDumpWithThreadInfo: MINIDUMP_TYPE = 4096
MINIDUMP_TYPE_MiniDumpWithCodeSegs: MINIDUMP_TYPE = 8192
MINIDUMP_TYPE_MiniDumpWithoutAuxiliaryState: MINIDUMP_TYPE = 16384
MINIDUMP_TYPE_MiniDumpWithFullAuxiliaryState: MINIDUMP_TYPE = 32768
MINIDUMP_TYPE_MiniDumpWithPrivateWriteCopyMemory: MINIDUMP_TYPE = 65536
MINIDUMP_TYPE_MiniDumpIgnoreInaccessibleMemory: MINIDUMP_TYPE = 131072
MINIDUMP_TYPE_MiniDumpWithTokenInformation: MINIDUMP_TYPE = 262144
MINIDUMP_TYPE_MiniDumpWithModuleHeaders: MINIDUMP_TYPE = 524288
MINIDUMP_TYPE_MiniDumpFilterTriage: MINIDUMP_TYPE = 1048576
MINIDUMP_TYPE_MiniDumpWithAvxXStateContext: MINIDUMP_TYPE = 2097152
MINIDUMP_TYPE_MiniDumpWithIptTrace: MINIDUMP_TYPE = 4194304
MINIDUMP_TYPE_MiniDumpScanInaccessiblePartialPages: MINIDUMP_TYPE = 8388608
MINIDUMP_TYPE_MiniDumpFilterWriteCombinedMemory: MINIDUMP_TYPE = 16777216
MINIDUMP_TYPE_MiniDumpValidTypeFlags: MINIDUMP_TYPE = 33554431
class MINIDUMP_UNLOADED_MODULE(EasyCastStructure):
    BaseOfImage: UInt64
    SizeOfImage: UInt32
    CheckSum: UInt32
    TimeDateStamp: UInt32
    ModuleNameRva: UInt32
    _pack_ = 4
class MINIDUMP_UNLOADED_MODULE_LIST(EasyCastStructure):
    SizeOfHeader: UInt32
    SizeOfEntry: UInt32
    NumberOfEntries: UInt32
    _pack_ = 4
class MINIDUMP_USER_RECORD(EasyCastStructure):
    Type: UInt32
    Memory: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_LOCATION_DESCRIPTOR
    _pack_ = 4
if ARCH in 'X64,ARM64':
    class MINIDUMP_USER_STREAM(EasyCastStructure):
        Type: UInt32
        BufferSize: UInt32
        Buffer: VoidPtr
        _pack_ = 4
if ARCH in 'X86':
    class MINIDUMP_USER_STREAM(EasyCastStructure):
        Type: UInt32
        BufferSize: UInt32
        Buffer: VoidPtr
if ARCH in 'X64,ARM64':
    class MINIDUMP_USER_STREAM_INFORMATION(EasyCastStructure):
        UserStreamCount: UInt32
        UserStreamArray: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_USER_STREAM_head)
        _pack_ = 4
if ARCH in 'X86':
    class MINIDUMP_USER_STREAM_INFORMATION(EasyCastStructure):
        UserStreamCount: UInt32
        UserStreamArray: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_USER_STREAM_head)
class MINIDUMP_VM_POST_READ_CALLBACK(EasyCastStructure):
    Offset: UInt64
    Buffer: VoidPtr
    Size: UInt32
    Completed: UInt32
    Status: win32more.Windows.Win32.Foundation.HRESULT
    _pack_ = 4
class MINIDUMP_VM_PRE_READ_CALLBACK(EasyCastStructure):
    Offset: UInt64
    Buffer: VoidPtr
    Size: UInt32
    _pack_ = 4
class MINIDUMP_VM_QUERY_CALLBACK(EasyCastStructure):
    Offset: UInt64
    _pack_ = 4
class MODLOAD_CVMISC(EasyCastStructure):
    oCV: UInt32
    cCV: UIntPtr
    oMisc: UInt32
    cMisc: UIntPtr
    dtImage: UInt32
    cImage: UInt32
class MODLOAD_DATA(EasyCastStructure):
    ssize: UInt32
    ssig: win32more.Windows.Win32.System.Diagnostics.Debug.MODLOAD_DATA_TYPE
    data: VoidPtr
    size: UInt32
    flags: UInt32
MODLOAD_DATA_TYPE = UInt32
DBHHEADER_DEBUGDIRS: MODLOAD_DATA_TYPE = 1
DBHHEADER_CVMISC: MODLOAD_DATA_TYPE = 2
class MODLOAD_PDBGUID_PDBAGE(EasyCastStructure):
    PdbGuid: Guid
    PdbAge: UInt32
class MODULE_TYPE_INFO(EasyCastStructure):
    dataLength: UInt16
    leaf: UInt16
    data: Byte * 1
MODULE_WRITE_FLAGS = Int32
MODULE_WRITE_FLAGS_ModuleWriteModule: MODULE_WRITE_FLAGS = 1
MODULE_WRITE_FLAGS_ModuleWriteDataSeg: MODULE_WRITE_FLAGS = 2
MODULE_WRITE_FLAGS_ModuleWriteMiscRecord: MODULE_WRITE_FLAGS = 4
MODULE_WRITE_FLAGS_ModuleWriteCvRecord: MODULE_WRITE_FLAGS = 8
MODULE_WRITE_FLAGS_ModuleReferencedByMemory: MODULE_WRITE_FLAGS = 16
MODULE_WRITE_FLAGS_ModuleWriteTlsData: MODULE_WRITE_FLAGS = 32
MODULE_WRITE_FLAGS_ModuleWriteCodeSegs: MODULE_WRITE_FLAGS = 64
OBJECT_ATTRIB_FLAGS = Int32
OBJECT_ATTRIB_NO_ATTRIB: OBJECT_ATTRIB_FLAGS = 0
OBJECT_ATTRIB_NO_NAME: OBJECT_ATTRIB_FLAGS = 1
OBJECT_ATTRIB_NO_TYPE: OBJECT_ATTRIB_FLAGS = 2
OBJECT_ATTRIB_NO_VALUE: OBJECT_ATTRIB_FLAGS = 4
OBJECT_ATTRIB_VALUE_IS_INVALID: OBJECT_ATTRIB_FLAGS = 8
OBJECT_ATTRIB_VALUE_IS_OBJECT: OBJECT_ATTRIB_FLAGS = 16
OBJECT_ATTRIB_VALUE_IS_ENUM: OBJECT_ATTRIB_FLAGS = 32
OBJECT_ATTRIB_VALUE_IS_CUSTOM: OBJECT_ATTRIB_FLAGS = 64
OBJECT_ATTRIB_OBJECT_IS_EXPANDABLE: OBJECT_ATTRIB_FLAGS = 112
OBJECT_ATTRIB_VALUE_HAS_CODE: OBJECT_ATTRIB_FLAGS = 128
OBJECT_ATTRIB_TYPE_IS_OBJECT: OBJECT_ATTRIB_FLAGS = 256
OBJECT_ATTRIB_TYPE_HAS_CODE: OBJECT_ATTRIB_FLAGS = 512
OBJECT_ATTRIB_TYPE_IS_EXPANDABLE: OBJECT_ATTRIB_FLAGS = 256
OBJECT_ATTRIB_SLOT_IS_CATEGORY: OBJECT_ATTRIB_FLAGS = 1024
OBJECT_ATTRIB_VALUE_READONLY: OBJECT_ATTRIB_FLAGS = 2048
OBJECT_ATTRIB_ACCESS_PUBLIC: OBJECT_ATTRIB_FLAGS = 4096
OBJECT_ATTRIB_ACCESS_PRIVATE: OBJECT_ATTRIB_FLAGS = 8192
OBJECT_ATTRIB_ACCESS_PROTECTED: OBJECT_ATTRIB_FLAGS = 16384
OBJECT_ATTRIB_ACCESS_FINAL: OBJECT_ATTRIB_FLAGS = 32768
OBJECT_ATTRIB_STORAGE_GLOBAL: OBJECT_ATTRIB_FLAGS = 65536
OBJECT_ATTRIB_STORAGE_STATIC: OBJECT_ATTRIB_FLAGS = 131072
OBJECT_ATTRIB_STORAGE_FIELD: OBJECT_ATTRIB_FLAGS = 262144
OBJECT_ATTRIB_STORAGE_VIRTUAL: OBJECT_ATTRIB_FLAGS = 524288
OBJECT_ATTRIB_TYPE_IS_CONSTANT: OBJECT_ATTRIB_FLAGS = 1048576
OBJECT_ATTRIB_TYPE_IS_SYNCHRONIZED: OBJECT_ATTRIB_FLAGS = 2097152
OBJECT_ATTRIB_TYPE_IS_VOLATILE: OBJECT_ATTRIB_FLAGS = 4194304
OBJECT_ATTRIB_HAS_EXTENDED_ATTRIBS: OBJECT_ATTRIB_FLAGS = 8388608
OBJECT_ATTRIB_IS_CLASS: OBJECT_ATTRIB_FLAGS = 16777216
OBJECT_ATTRIB_IS_FUNCTION: OBJECT_ATTRIB_FLAGS = 33554432
OBJECT_ATTRIB_IS_VARIABLE: OBJECT_ATTRIB_FLAGS = 67108864
OBJECT_ATTRIB_IS_PROPERTY: OBJECT_ATTRIB_FLAGS = 134217728
OBJECT_ATTRIB_IS_MACRO: OBJECT_ATTRIB_FLAGS = 268435456
OBJECT_ATTRIB_IS_TYPE: OBJECT_ATTRIB_FLAGS = 536870912
OBJECT_ATTRIB_IS_INHERITED: OBJECT_ATTRIB_FLAGS = 1073741824
OBJECT_ATTRIB_IS_INTERFACE: OBJECT_ATTRIB_FLAGS = -2147483648
class OMAP(EasyCastStructure):
    rva: UInt32
    rvaTo: UInt32
OPEN_THREAD_WAIT_CHAIN_SESSION_FLAGS = UInt32
WCT_ASYNC_OPEN_FLAG: OPEN_THREAD_WAIT_CHAIN_SESSION_FLAGS = 1
class OUTPUT_DEBUG_STRING_INFO(EasyCastStructure):
    lpDebugStringData: win32more.Windows.Win32.Foundation.PSTR
    fUnicode: UInt16
    nDebugStringLength: UInt16
@winfunctype_pointer
def PCOGETACTIVATIONSTATE(param0: Guid, param1: UInt32, param2: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PCOGETCALLSTATE(param0: Int32, param1: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PDBGHELP_CREATE_USER_DUMP_CALLBACK(DataType: UInt32, Data: POINTER(VoidPtr), DataLength: POINTER(UInt32), UserData: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PENUMDIRTREE_CALLBACK(FilePath: win32more.Windows.Win32.Foundation.PSTR, CallerData: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PENUMDIRTREE_CALLBACKW(FilePath: win32more.Windows.Win32.Foundation.PWSTR, CallerData: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X86':
    @winfunctype_pointer
    def PENUMLOADED_MODULES_CALLBACK(ModuleName: win32more.Windows.Win32.Foundation.PSTR, ModuleBase: UInt32, ModuleSize: UInt32, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PENUMLOADED_MODULES_CALLBACK64(ModuleName: win32more.Windows.Win32.Foundation.PSTR, ModuleBase: UInt64, ModuleSize: UInt32, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PENUMLOADED_MODULES_CALLBACKW64(ModuleName: win32more.Windows.Win32.Foundation.PWSTR, ModuleBase: UInt64, ModuleSize: UInt32, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PENUMSOURCEFILETOKENSCALLBACK(token: VoidPtr, size: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFINDFILEINPATHCALLBACK(filename: win32more.Windows.Win32.Foundation.PSTR, context: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFINDFILEINPATHCALLBACKW(filename: win32more.Windows.Win32.Foundation.PWSTR, context: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFIND_DEBUG_FILE_CALLBACK(FileHandle: win32more.Windows.Win32.Foundation.HANDLE, FileName: win32more.Windows.Win32.Foundation.PSTR, CallerData: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFIND_DEBUG_FILE_CALLBACKW(FileHandle: win32more.Windows.Win32.Foundation.HANDLE, FileName: win32more.Windows.Win32.Foundation.PWSTR, CallerData: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFIND_EXE_FILE_CALLBACK(FileHandle: win32more.Windows.Win32.Foundation.HANDLE, FileName: win32more.Windows.Win32.Foundation.PSTR, CallerData: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFIND_EXE_FILE_CALLBACKW(FileHandle: win32more.Windows.Win32.Foundation.HANDLE, FileName: win32more.Windows.Win32.Foundation.PWSTR, CallerData: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X86':
    @winfunctype_pointer
    def PFUNCTION_TABLE_ACCESS_ROUTINE(hProcess: win32more.Windows.Win32.Foundation.HANDLE, AddrBase: UInt32) -> VoidPtr: ...
@winfunctype_pointer
def PFUNCTION_TABLE_ACCESS_ROUTINE64(ahProcess: win32more.Windows.Win32.Foundation.HANDLE, AddrBase: UInt64) -> VoidPtr: ...
if ARCH in 'X86':
    @winfunctype_pointer
    def PGET_MODULE_BASE_ROUTINE(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Address: UInt32) -> UInt32: ...
@winfunctype_pointer
def PGET_MODULE_BASE_ROUTINE64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Address: UInt64) -> UInt64: ...
if ARCH in 'ARM64':
    @winfunctype_pointer
    def PGET_RUNTIME_FUNCTION_CALLBACK(ControlPc: UInt64, Context: VoidPtr) -> POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_ARM64_RUNTIME_FUNCTION_ENTRY_head): ...
if ARCH in 'X64':
    @winfunctype_pointer
    def PGET_RUNTIME_FUNCTION_CALLBACK(ControlPc: UInt64, Context: VoidPtr) -> POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_RUNTIME_FUNCTION_ENTRY_head): ...
@winfunctype_pointer
def PGET_TARGET_ATTRIBUTE_VALUE64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Attribute: UInt32, AttributeData: UInt64, AttributeValue: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
class PHYSICAL_MEMORY_DESCRIPTOR32(EasyCastStructure):
    NumberOfRuns: UInt32
    NumberOfPages: UInt32
    Run: win32more.Windows.Win32.System.Diagnostics.Debug.PHYSICAL_MEMORY_RUN32 * 1
class PHYSICAL_MEMORY_DESCRIPTOR64(EasyCastStructure):
    NumberOfRuns: UInt32
    NumberOfPages: UInt64
    Run: win32more.Windows.Win32.System.Diagnostics.Debug.PHYSICAL_MEMORY_RUN64 * 1
class PHYSICAL_MEMORY_RUN32(EasyCastStructure):
    BasePage: UInt32
    PageCount: UInt32
class PHYSICAL_MEMORY_RUN64(EasyCastStructure):
    BasePage: UInt64
    PageCount: UInt64
@winfunctype_pointer
def PIMAGEHLP_STATUS_ROUTINE(Reason: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_STATUS_REASON, ImageName: win32more.Windows.Win32.Foundation.PSTR, DllName: win32more.Windows.Win32.Foundation.PSTR, Va: UIntPtr, Parameter: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PIMAGEHLP_STATUS_ROUTINE32(Reason: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_STATUS_REASON, ImageName: win32more.Windows.Win32.Foundation.PSTR, DllName: win32more.Windows.Win32.Foundation.PSTR, Va: UInt32, Parameter: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PIMAGEHLP_STATUS_ROUTINE64(Reason: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_STATUS_REASON, ImageName: win32more.Windows.Win32.Foundation.PSTR, DllName: win32more.Windows.Win32.Foundation.PSTR, Va: UInt64, Parameter: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X86':
    @winfunctype_pointer
    def PREAD_PROCESS_MEMORY_ROUTINE(hProcess: win32more.Windows.Win32.Foundation.HANDLE, lpBaseAddress: UInt32, lpBuffer: VoidPtr, nSize: UInt32, lpNumberOfBytesRead: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PREAD_PROCESS_MEMORY_ROUTINE64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, qwBaseAddress: UInt64, lpBuffer: VoidPtr, nSize: UInt32, lpNumberOfBytesRead: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
PROP_INFO_FLAGS = Int32
PROP_INFO_NAME: PROP_INFO_FLAGS = 1
PROP_INFO_TYPE: PROP_INFO_FLAGS = 2
PROP_INFO_VALUE: PROP_INFO_FLAGS = 4
PROP_INFO_FULLNAME: PROP_INFO_FLAGS = 32
PROP_INFO_ATTRIBUTES: PROP_INFO_FLAGS = 8
PROP_INFO_DEBUGPROP: PROP_INFO_FLAGS = 16
PROP_INFO_AUTOEXPAND: PROP_INFO_FLAGS = 134217728
@winfunctype_pointer
def PSYMBOLSERVERBYINDEXPROC(param0: win32more.Windows.Win32.Foundation.PSTR, param1: win32more.Windows.Win32.Foundation.PSTR, param2: win32more.Windows.Win32.Foundation.PSTR, param3: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYMBOLSERVERBYINDEXPROCA(param0: win32more.Windows.Win32.Foundation.PSTR, param1: win32more.Windows.Win32.Foundation.PSTR, param2: win32more.Windows.Win32.Foundation.PSTR, param3: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYMBOLSERVERBYINDEXPROCW(param0: win32more.Windows.Win32.Foundation.PWSTR, param1: win32more.Windows.Win32.Foundation.PWSTR, param2: win32more.Windows.Win32.Foundation.PWSTR, param3: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYMBOLSERVERCALLBACKPROC(action: UIntPtr, data: UInt64, context: UInt64) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYMBOLSERVERCLOSEPROC() -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYMBOLSERVERDELTANAME(param0: win32more.Windows.Win32.Foundation.PSTR, param1: VoidPtr, param2: UInt32, param3: UInt32, param4: VoidPtr, param5: UInt32, param6: UInt32, param7: win32more.Windows.Win32.Foundation.PSTR, param8: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYMBOLSERVERDELTANAMEW(param0: win32more.Windows.Win32.Foundation.PWSTR, param1: VoidPtr, param2: UInt32, param3: UInt32, param4: VoidPtr, param5: UInt32, param6: UInt32, param7: win32more.Windows.Win32.Foundation.PWSTR, param8: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYMBOLSERVERGETINDEXSTRING(param0: VoidPtr, param1: UInt32, param2: UInt32, param3: win32more.Windows.Win32.Foundation.PSTR, param4: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYMBOLSERVERGETINDEXSTRINGW(param0: VoidPtr, param1: UInt32, param2: UInt32, param3: win32more.Windows.Win32.Foundation.PWSTR, param4: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYMBOLSERVERGETOPTIONDATAPROC(param0: UIntPtr, param1: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYMBOLSERVERGETOPTIONSPROC() -> UIntPtr: ...
@winfunctype_pointer
def PSYMBOLSERVERGETSUPPLEMENT(param0: win32more.Windows.Win32.Foundation.PSTR, param1: win32more.Windows.Win32.Foundation.PSTR, param2: win32more.Windows.Win32.Foundation.PSTR, param3: win32more.Windows.Win32.Foundation.PSTR, param4: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYMBOLSERVERGETSUPPLEMENTW(param0: win32more.Windows.Win32.Foundation.PWSTR, param1: win32more.Windows.Win32.Foundation.PWSTR, param2: win32more.Windows.Win32.Foundation.PWSTR, param3: win32more.Windows.Win32.Foundation.PWSTR, param4: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYMBOLSERVERGETVERSION(param0: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.API_VERSION_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYMBOLSERVERISSTORE(param0: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYMBOLSERVERISSTOREW(param0: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYMBOLSERVERMESSAGEPROC(action: UIntPtr, data: UInt64, context: UInt64) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYMBOLSERVEROPENPROC() -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYMBOLSERVERPINGPROC(param0: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYMBOLSERVERPINGPROCA(param0: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYMBOLSERVERPINGPROCW(param0: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYMBOLSERVERPINGPROCWEX(param0: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYMBOLSERVERPROC(param0: win32more.Windows.Win32.Foundation.PSTR, param1: win32more.Windows.Win32.Foundation.PSTR, param2: VoidPtr, param3: UInt32, param4: UInt32, param5: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYMBOLSERVERPROCA(param0: win32more.Windows.Win32.Foundation.PSTR, param1: win32more.Windows.Win32.Foundation.PSTR, param2: VoidPtr, param3: UInt32, param4: UInt32, param5: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYMBOLSERVERPROCW(param0: win32more.Windows.Win32.Foundation.PWSTR, param1: win32more.Windows.Win32.Foundation.PWSTR, param2: VoidPtr, param3: UInt32, param4: UInt32, param5: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYMBOLSERVERSETHTTPAUTHHEADER(pszAuthHeader: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYMBOLSERVERSETOPTIONSPROC(param0: UIntPtr, param1: UInt64) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYMBOLSERVERSETOPTIONSWPROC(param0: UIntPtr, param1: UInt64) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYMBOLSERVERSTOREFILE(param0: win32more.Windows.Win32.Foundation.PSTR, param1: win32more.Windows.Win32.Foundation.PSTR, param2: VoidPtr, param3: UInt32, param4: UInt32, param5: win32more.Windows.Win32.Foundation.PSTR, param6: UIntPtr, param7: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYMBOLSERVERSTOREFILEW(param0: win32more.Windows.Win32.Foundation.PWSTR, param1: win32more.Windows.Win32.Foundation.PWSTR, param2: VoidPtr, param3: UInt32, param4: UInt32, param5: win32more.Windows.Win32.Foundation.PWSTR, param6: UIntPtr, param7: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYMBOLSERVERSTORESUPPLEMENT(param0: win32more.Windows.Win32.Foundation.PSTR, param1: win32more.Windows.Win32.Foundation.PSTR, param2: win32more.Windows.Win32.Foundation.PSTR, param3: win32more.Windows.Win32.Foundation.PSTR, param4: UIntPtr, param5: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYMBOLSERVERSTORESUPPLEMENTW(param0: win32more.Windows.Win32.Foundation.PWSTR, param1: win32more.Windows.Win32.Foundation.PWSTR, param2: win32more.Windows.Win32.Foundation.PWSTR, param3: win32more.Windows.Win32.Foundation.PWSTR, param4: UIntPtr, param5: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYMBOLSERVERVERSION() -> UInt32: ...
@winfunctype_pointer
def PSYMBOLSERVERWEXPROC(param0: win32more.Windows.Win32.Foundation.PWSTR, param1: win32more.Windows.Win32.Foundation.PWSTR, param2: VoidPtr, param3: UInt32, param4: UInt32, param5: win32more.Windows.Win32.Foundation.PWSTR, param6: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.SYMSRV_EXTENDED_OUTPUT_DATA_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYMBOL_FUNCENTRY_CALLBACK(hProcess: win32more.Windows.Win32.Foundation.HANDLE, AddrBase: UInt32, UserContext: VoidPtr) -> VoidPtr: ...
@winfunctype_pointer
def PSYMBOL_FUNCENTRY_CALLBACK64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, AddrBase: UInt64, UserContext: UInt64) -> VoidPtr: ...
if ARCH in 'X86':
    @winfunctype_pointer
    def PSYMBOL_REGISTERED_CALLBACK(hProcess: win32more.Windows.Win32.Foundation.HANDLE, ActionCode: UInt32, CallbackData: VoidPtr, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYMBOL_REGISTERED_CALLBACK64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, ActionCode: UInt32, CallbackData: UInt64, UserContext: UInt64) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYM_ENUMERATESYMBOLS_CALLBACK(pSymInfo: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFO_head), SymbolSize: UInt32, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYM_ENUMERATESYMBOLS_CALLBACKW(pSymInfo: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFOW_head), SymbolSize: UInt32, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYM_ENUMLINES_CALLBACK(LineInfo: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.SRCCODEINFO_head), UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYM_ENUMLINES_CALLBACKW(LineInfo: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.SRCCODEINFOW_head), UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X86':
    @winfunctype_pointer
    def PSYM_ENUMMODULES_CALLBACK(ModuleName: win32more.Windows.Win32.Foundation.PSTR, BaseOfDll: UInt32, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYM_ENUMMODULES_CALLBACK64(ModuleName: win32more.Windows.Win32.Foundation.PSTR, BaseOfDll: UInt64, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYM_ENUMMODULES_CALLBACKW64(ModuleName: win32more.Windows.Win32.Foundation.PWSTR, BaseOfDll: UInt64, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYM_ENUMPROCESSES_CALLBACK(hProcess: win32more.Windows.Win32.Foundation.HANDLE, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYM_ENUMSOURCEFILES_CALLBACK(pSourceFile: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.SOURCEFILE_head), UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYM_ENUMSOURCEFILES_CALLBACKW(pSourceFile: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.SOURCEFILEW_head), UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X86':
    @winfunctype_pointer
    def PSYM_ENUMSYMBOLS_CALLBACK(SymbolName: win32more.Windows.Win32.Foundation.PSTR, SymbolAddress: UInt32, SymbolSize: UInt32, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYM_ENUMSYMBOLS_CALLBACK64(SymbolName: win32more.Windows.Win32.Foundation.PSTR, SymbolAddress: UInt64, SymbolSize: UInt32, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYM_ENUMSYMBOLS_CALLBACK64W(SymbolName: win32more.Windows.Win32.Foundation.PWSTR, SymbolAddress: UInt64, SymbolSize: UInt32, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X86':
    @winfunctype_pointer
    def PSYM_ENUMSYMBOLS_CALLBACKW(SymbolName: win32more.Windows.Win32.Foundation.PWSTR, SymbolAddress: UInt32, SymbolSize: UInt32, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X86':
    @winfunctype_pointer
    def PTRANSLATE_ADDRESS_ROUTINE(hProcess: win32more.Windows.Win32.Foundation.HANDLE, hThread: win32more.Windows.Win32.Foundation.HANDLE, lpaddr: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ADDRESS_head)) -> UInt32: ...
@winfunctype_pointer
def PTRANSLATE_ADDRESS_ROUTINE64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, hThread: win32more.Windows.Win32.Foundation.HANDLE, lpaddr: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ADDRESS64_head)) -> UInt64: ...
@winfunctype_pointer
def PVECTORED_EXCEPTION_HANDLER(ExceptionInfo: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.EXCEPTION_POINTERS_head)) -> Int32: ...
@winfunctype_pointer
def PWAITCHAINCALLBACK(WctHandle: VoidPtr, Context: UIntPtr, CallbackStatus: UInt32, NodeCount: POINTER(UInt32), NodeInfoArray: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.WAITCHAIN_NODE_INFO_head), IsCycle: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> Void: ...
class RIP_INFO(EasyCastStructure):
    dwError: UInt32
    dwType: win32more.Windows.Win32.System.Diagnostics.Debug.RIP_INFO_TYPE
RIP_INFO_TYPE = UInt32
SLE_ERROR: RIP_INFO_TYPE = 1
SLE_MINORERROR: RIP_INFO_TYPE = 2
SLE_WARNING: RIP_INFO_TYPE = 3
RTL_VIRTUAL_UNWIND_HANDLER_TYPE = UInt32
UNW_FLAG_NHANDLER: RTL_VIRTUAL_UNWIND_HANDLER_TYPE = 0
UNW_FLAG_EHANDLER: RTL_VIRTUAL_UNWIND_HANDLER_TYPE = 1
UNW_FLAG_UHANDLER: RTL_VIRTUAL_UNWIND_HANDLER_TYPE = 2
UNW_FLAG_CHAININFO: RTL_VIRTUAL_UNWIND_HANDLER_TYPE = 4
class SOURCEFILE(EasyCastStructure):
    ModBase: UInt64
    FileName: win32more.Windows.Win32.Foundation.PSTR
class SOURCEFILEW(EasyCastStructure):
    ModBase: UInt64
    FileName: win32more.Windows.Win32.Foundation.PWSTR
class SRCCODEINFO(EasyCastStructure):
    SizeOfStruct: UInt32
    Key: VoidPtr
    ModBase: UInt64
    Obj: win32more.Windows.Win32.Foundation.CHAR * 261
    FileName: win32more.Windows.Win32.Foundation.CHAR * 261
    LineNumber: UInt32
    Address: UInt64
class SRCCODEINFOW(EasyCastStructure):
    SizeOfStruct: UInt32
    Key: VoidPtr
    ModBase: UInt64
    Obj: Char * 261
    FileName: Char * 261
    LineNumber: UInt32
    Address: UInt64
if ARCH in 'X86':
    class STACKFRAME(EasyCastStructure):
        AddrPC: win32more.Windows.Win32.System.Diagnostics.Debug.ADDRESS
        AddrReturn: win32more.Windows.Win32.System.Diagnostics.Debug.ADDRESS
        AddrFrame: win32more.Windows.Win32.System.Diagnostics.Debug.ADDRESS
        AddrStack: win32more.Windows.Win32.System.Diagnostics.Debug.ADDRESS
        FuncTableEntry: VoidPtr
        Params: UInt32 * 4
        Far: win32more.Windows.Win32.Foundation.BOOL
        Virtual: win32more.Windows.Win32.Foundation.BOOL
        Reserved: UInt32 * 3
        KdHelp: win32more.Windows.Win32.System.Diagnostics.Debug.KDHELP
        AddrBStore: win32more.Windows.Win32.System.Diagnostics.Debug.ADDRESS
class STACKFRAME64(EasyCastStructure):
    AddrPC: win32more.Windows.Win32.System.Diagnostics.Debug.ADDRESS64
    AddrReturn: win32more.Windows.Win32.System.Diagnostics.Debug.ADDRESS64
    AddrFrame: win32more.Windows.Win32.System.Diagnostics.Debug.ADDRESS64
    AddrStack: win32more.Windows.Win32.System.Diagnostics.Debug.ADDRESS64
    AddrBStore: win32more.Windows.Win32.System.Diagnostics.Debug.ADDRESS64
    FuncTableEntry: VoidPtr
    Params: UInt64 * 4
    Far: win32more.Windows.Win32.Foundation.BOOL
    Virtual: win32more.Windows.Win32.Foundation.BOOL
    Reserved: UInt64 * 3
    KdHelp: win32more.Windows.Win32.System.Diagnostics.Debug.KDHELP64
class STACKFRAME_EX(EasyCastStructure):
    AddrPC: win32more.Windows.Win32.System.Diagnostics.Debug.ADDRESS64
    AddrReturn: win32more.Windows.Win32.System.Diagnostics.Debug.ADDRESS64
    AddrFrame: win32more.Windows.Win32.System.Diagnostics.Debug.ADDRESS64
    AddrStack: win32more.Windows.Win32.System.Diagnostics.Debug.ADDRESS64
    AddrBStore: win32more.Windows.Win32.System.Diagnostics.Debug.ADDRESS64
    FuncTableEntry: VoidPtr
    Params: UInt64 * 4
    Far: win32more.Windows.Win32.Foundation.BOOL
    Virtual: win32more.Windows.Win32.Foundation.BOOL
    Reserved: UInt64 * 3
    KdHelp: win32more.Windows.Win32.System.Diagnostics.Debug.KDHELP64
    StackFrameSize: UInt32
    InlineFrameContext: UInt32
@winfunctype_pointer
def SYMADDSOURCESTREAM(param0: win32more.Windows.Win32.Foundation.HANDLE, param1: UInt64, param2: win32more.Windows.Win32.Foundation.PSTR, param3: POINTER(Byte), param4: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def SYMADDSOURCESTREAMA(param0: win32more.Windows.Win32.Foundation.HANDLE, param1: UInt64, param2: win32more.Windows.Win32.Foundation.PSTR, param3: POINTER(Byte), param4: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
class SYMBOL_INFO(EasyCastStructure):
    SizeOfStruct: UInt32
    TypeIndex: UInt32
    Reserved: UInt64 * 2
    Index: UInt32
    Size: UInt32
    ModBase: UInt64
    Flags: win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFO_FLAGS
    Value: UInt64
    Address: UInt64
    Register: UInt32
    Scope: UInt32
    Tag: UInt32
    NameLen: UInt32
    MaxNameLen: UInt32
    Name: win32more.Windows.Win32.Foundation.CHAR * 1
class SYMBOL_INFOW(EasyCastStructure):
    SizeOfStruct: UInt32
    TypeIndex: UInt32
    Reserved: UInt64 * 2
    Index: UInt32
    Size: UInt32
    ModBase: UInt64
    Flags: win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFO_FLAGS
    Value: UInt64
    Address: UInt64
    Register: UInt32
    Scope: UInt32
    Tag: UInt32
    NameLen: UInt32
    MaxNameLen: UInt32
    Name: Char * 1
SYMBOL_INFO_FLAGS = UInt32
SYMFLAG_CLR_TOKEN: SYMBOL_INFO_FLAGS = 262144
SYMFLAG_CONSTANT: SYMBOL_INFO_FLAGS = 256
SYMFLAG_EXPORT: SYMBOL_INFO_FLAGS = 512
SYMFLAG_FORWARDER: SYMBOL_INFO_FLAGS = 1024
SYMFLAG_FRAMEREL: SYMBOL_INFO_FLAGS = 32
SYMFLAG_FUNCTION: SYMBOL_INFO_FLAGS = 2048
SYMFLAG_ILREL: SYMBOL_INFO_FLAGS = 65536
SYMFLAG_LOCAL: SYMBOL_INFO_FLAGS = 128
SYMFLAG_METADATA: SYMBOL_INFO_FLAGS = 131072
SYMFLAG_PARAMETER: SYMBOL_INFO_FLAGS = 64
SYMFLAG_REGISTER: SYMBOL_INFO_FLAGS = 8
SYMFLAG_REGREL: SYMBOL_INFO_FLAGS = 16
SYMFLAG_SLOT: SYMBOL_INFO_FLAGS = 32768
SYMFLAG_THUNK: SYMBOL_INFO_FLAGS = 8192
SYMFLAG_TLSREL: SYMBOL_INFO_FLAGS = 16384
SYMFLAG_VALUEPRESENT: SYMBOL_INFO_FLAGS = 1
SYMFLAG_VIRTUAL: SYMBOL_INFO_FLAGS = 4096
class SYMBOL_INFO_PACKAGE(EasyCastStructure):
    si: win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFO
    name: win32more.Windows.Win32.Foundation.CHAR * 2001
class SYMBOL_INFO_PACKAGEW(EasyCastStructure):
    si: win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFOW
    name: Char * 2001
class SYMSRV_EXTENDED_OUTPUT_DATA(EasyCastStructure):
    sizeOfStruct: UInt32
    version: UInt32
    filePtrMsg: Char * 261
class SYMSRV_INDEX_INFO(EasyCastStructure):
    sizeofstruct: UInt32
    file: win32more.Windows.Win32.Foundation.CHAR * 261
    stripped: win32more.Windows.Win32.Foundation.BOOL
    timestamp: UInt32
    size: UInt32
    dbgfile: win32more.Windows.Win32.Foundation.CHAR * 261
    pdbfile: win32more.Windows.Win32.Foundation.CHAR * 261
    guid: Guid
    sig: UInt32
    age: UInt32
class SYMSRV_INDEX_INFOW(EasyCastStructure):
    sizeofstruct: UInt32
    file: Char * 261
    stripped: win32more.Windows.Win32.Foundation.BOOL
    timestamp: UInt32
    size: UInt32
    dbgfile: Char * 261
    pdbfile: Char * 261
    guid: Guid
    sig: UInt32
    age: UInt32
SYM_FIND_ID_OPTION = UInt32
SSRVOPT_DWORD: SYM_FIND_ID_OPTION = 2
SSRVOPT_DWORDPTR: SYM_FIND_ID_OPTION = 4
SSRVOPT_GUIDPTR: SYM_FIND_ID_OPTION = 8
SYM_LOAD_FLAGS = UInt32
SLMFLAG_NONE: SYM_LOAD_FLAGS = 0
SLMFLAG_VIRTUAL: SYM_LOAD_FLAGS = 1
SLMFLAG_ALT_INDEX: SYM_LOAD_FLAGS = 2
SLMFLAG_NO_SYMBOLS: SYM_LOAD_FLAGS = 4
SYM_SRV_STORE_FILE_FLAGS = UInt32
SYMSTOREOPT_COMPRESS: SYM_SRV_STORE_FILE_FLAGS = 1
SYMSTOREOPT_OVERWRITE: SYM_SRV_STORE_FILE_FLAGS = 2
SYMSTOREOPT_PASS_IF_EXISTS: SYM_SRV_STORE_FILE_FLAGS = 64
SYMSTOREOPT_POINTER: SYM_SRV_STORE_FILE_FLAGS = 8
SYMSTOREOPT_RETURNINDEX: SYM_SRV_STORE_FILE_FLAGS = 4
SYM_TYPE = Int32
SYM_TYPE_SymNone: SYM_TYPE = 0
SYM_TYPE_SymCoff: SYM_TYPE = 1
SYM_TYPE_SymCv: SYM_TYPE = 2
SYM_TYPE_SymPdb: SYM_TYPE = 3
SYM_TYPE_SymExport: SYM_TYPE = 4
SYM_TYPE_SymDeferred: SYM_TYPE = 5
SYM_TYPE_SymSym: SYM_TYPE = 6
SYM_TYPE_SymDia: SYM_TYPE = 7
SYM_TYPE_SymVirtual: SYM_TYPE = 8
SYM_TYPE_NumSymTypes: SYM_TYPE = 9
THREAD_ERROR_MODE = UInt32
SEM_ALL_ERRORS: THREAD_ERROR_MODE = 0
SEM_FAILCRITICALERRORS: THREAD_ERROR_MODE = 1
SEM_NOGPFAULTERRORBOX: THREAD_ERROR_MODE = 2
SEM_NOOPENFILEERRORBOX: THREAD_ERROR_MODE = 32768
SEM_NOALIGNMENTFAULTEXCEPT: THREAD_ERROR_MODE = 4
THREAD_WRITE_FLAGS = Int32
THREAD_WRITE_FLAGS_ThreadWriteThread: THREAD_WRITE_FLAGS = 1
THREAD_WRITE_FLAGS_ThreadWriteStack: THREAD_WRITE_FLAGS = 2
THREAD_WRITE_FLAGS_ThreadWriteContext: THREAD_WRITE_FLAGS = 4
THREAD_WRITE_FLAGS_ThreadWriteBackingStore: THREAD_WRITE_FLAGS = 8
THREAD_WRITE_FLAGS_ThreadWriteInstructionWindow: THREAD_WRITE_FLAGS = 16
THREAD_WRITE_FLAGS_ThreadWriteThreadData: THREAD_WRITE_FLAGS = 32
THREAD_WRITE_FLAGS_ThreadWriteThreadInfo: THREAD_WRITE_FLAGS = 64
class TI_FINDCHILDREN_PARAMS(EasyCastStructure):
    Count: UInt32
    Start: UInt32
    ChildId: UInt32 * 1
class UNLOAD_DLL_DEBUG_INFO(EasyCastStructure):
    lpBaseOfDll: VoidPtr
if ARCH in 'X64,ARM64':
    class UNWIND_HISTORY_TABLE(EasyCastStructure):
        Count: UInt32
        LocalHint: Byte
        GlobalHint: Byte
        Search: Byte
        Once: Byte
        LowAddress: UIntPtr
        HighAddress: UIntPtr
        Entry: win32more.Windows.Win32.System.Diagnostics.Debug.UNWIND_HISTORY_TABLE_ENTRY * 12
if ARCH in 'ARM64':
    class UNWIND_HISTORY_TABLE_ENTRY(EasyCastStructure):
        ImageBase: UIntPtr
        FunctionEntry: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_ARM64_RUNTIME_FUNCTION_ENTRY_head)
if ARCH in 'X64':
    class UNWIND_HISTORY_TABLE_ENTRY(EasyCastStructure):
        ImageBase: UIntPtr
        FunctionEntry: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_RUNTIME_FUNCTION_ENTRY_head)
VER_PLATFORM = UInt32
VER_PLATFORM_WIN32s: VER_PLATFORM = 0
VER_PLATFORM_WIN32_WINDOWS: VER_PLATFORM = 1
VER_PLATFORM_WIN32_NT: VER_PLATFORM = 2
class WAITCHAIN_NODE_INFO(EasyCastStructure):
    ObjectType: win32more.Windows.Win32.System.Diagnostics.Debug.WCT_OBJECT_TYPE
    ObjectStatus: win32more.Windows.Win32.System.Diagnostics.Debug.WCT_OBJECT_STATUS
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        LockObject: _LockObject_e__Struct
        ThreadObject: _ThreadObject_e__Struct
        class _LockObject_e__Struct(EasyCastStructure):
            ObjectName: Char * 128
            Timeout: Int64
            Alertable: win32more.Windows.Win32.Foundation.BOOL
        class _ThreadObject_e__Struct(EasyCastStructure):
            ProcessId: UInt32
            ThreadId: UInt32
            WaitTime: UInt32
            ContextSwitches: UInt32
WAIT_CHAIN_THREAD_OPTIONS = UInt32
WCT_OUT_OF_PROC_COM_FLAG: WAIT_CHAIN_THREAD_OPTIONS = 2
WCT_OUT_OF_PROC_CS_FLAG: WAIT_CHAIN_THREAD_OPTIONS = 4
WCT_OUT_OF_PROC_FLAG: WAIT_CHAIN_THREAD_OPTIONS = 1
WCT_OBJECT_STATUS = Int32
WCT_OBJECT_STATUS_WctStatusNoAccess: WCT_OBJECT_STATUS = 1
WCT_OBJECT_STATUS_WctStatusRunning: WCT_OBJECT_STATUS = 2
WCT_OBJECT_STATUS_WctStatusBlocked: WCT_OBJECT_STATUS = 3
WCT_OBJECT_STATUS_WctStatusPidOnly: WCT_OBJECT_STATUS = 4
WCT_OBJECT_STATUS_WctStatusPidOnlyRpcss: WCT_OBJECT_STATUS = 5
WCT_OBJECT_STATUS_WctStatusOwned: WCT_OBJECT_STATUS = 6
WCT_OBJECT_STATUS_WctStatusNotOwned: WCT_OBJECT_STATUS = 7
WCT_OBJECT_STATUS_WctStatusAbandoned: WCT_OBJECT_STATUS = 8
WCT_OBJECT_STATUS_WctStatusUnknown: WCT_OBJECT_STATUS = 9
WCT_OBJECT_STATUS_WctStatusError: WCT_OBJECT_STATUS = 10
WCT_OBJECT_STATUS_WctStatusMax: WCT_OBJECT_STATUS = 11
WCT_OBJECT_TYPE = Int32
WCT_OBJECT_TYPE_WctCriticalSectionType: WCT_OBJECT_TYPE = 1
WCT_OBJECT_TYPE_WctSendMessageType: WCT_OBJECT_TYPE = 2
WCT_OBJECT_TYPE_WctMutexType: WCT_OBJECT_TYPE = 3
WCT_OBJECT_TYPE_WctAlpcType: WCT_OBJECT_TYPE = 4
WCT_OBJECT_TYPE_WctComType: WCT_OBJECT_TYPE = 5
WCT_OBJECT_TYPE_WctThreadWaitType: WCT_OBJECT_TYPE = 6
WCT_OBJECT_TYPE_WctProcessWaitType: WCT_OBJECT_TYPE = 7
WCT_OBJECT_TYPE_WctThreadType: WCT_OBJECT_TYPE = 8
WCT_OBJECT_TYPE_WctComActivationType: WCT_OBJECT_TYPE = 9
WCT_OBJECT_TYPE_WctUnknownType: WCT_OBJECT_TYPE = 10
WCT_OBJECT_TYPE_WctSocketIoType: WCT_OBJECT_TYPE = 11
WCT_OBJECT_TYPE_WctSmbIoType: WCT_OBJECT_TYPE = 12
WCT_OBJECT_TYPE_WctMaxType: WCT_OBJECT_TYPE = 13
class WHEA_AER_BRIDGE_DESCRIPTOR(EasyCastStructure):
    Type: UInt16
    Enabled: win32more.Windows.Win32.Foundation.BOOLEAN
    Reserved: Byte
    BusNumber: UInt32
    Slot: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_PCI_SLOT_NUMBER
    DeviceControl: UInt16
    Flags: win32more.Windows.Win32.System.Diagnostics.Debug.AER_BRIDGE_DESCRIPTOR_FLAGS
    UncorrectableErrorMask: UInt32
    UncorrectableErrorSeverity: UInt32
    CorrectableErrorMask: UInt32
    AdvancedCapsAndControl: UInt32
    SecondaryUncorrectableErrorMask: UInt32
    SecondaryUncorrectableErrorSev: UInt32
    SecondaryCapsAndControl: UInt32
    _pack_ = 1
class WHEA_AER_ENDPOINT_DESCRIPTOR(EasyCastStructure):
    Type: UInt16
    Enabled: win32more.Windows.Win32.Foundation.BOOLEAN
    Reserved: Byte
    BusNumber: UInt32
    Slot: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_PCI_SLOT_NUMBER
    DeviceControl: UInt16
    Flags: win32more.Windows.Win32.System.Diagnostics.Debug.AER_ENDPOINT_DESCRIPTOR_FLAGS
    UncorrectableErrorMask: UInt32
    UncorrectableErrorSeverity: UInt32
    CorrectableErrorMask: UInt32
    AdvancedCapsAndControl: UInt32
    _pack_ = 1
class WHEA_AER_ROOTPORT_DESCRIPTOR(EasyCastStructure):
    Type: UInt16
    Enabled: win32more.Windows.Win32.Foundation.BOOLEAN
    Reserved: Byte
    BusNumber: UInt32
    Slot: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_PCI_SLOT_NUMBER
    DeviceControl: UInt16
    Flags: win32more.Windows.Win32.System.Diagnostics.Debug.AER_ROOTPORT_DESCRIPTOR_FLAGS
    UncorrectableErrorMask: UInt32
    UncorrectableErrorSeverity: UInt32
    CorrectableErrorMask: UInt32
    AdvancedCapsAndControl: UInt32
    RootErrorCommand: UInt32
    _pack_ = 1
class WHEA_DEVICE_DRIVER_DESCRIPTOR(EasyCastStructure):
    Type: UInt16
    Enabled: win32more.Windows.Win32.Foundation.BOOLEAN
    Reserved: Byte
    SourceGuid: Guid
    LogTag: UInt16
    Reserved2: UInt16
    PacketLength: UInt32
    PacketCount: UInt32
    PacketBuffer: POINTER(Byte)
    Config: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_ERROR_SOURCE_CONFIGURATION_DD
    CreatorId: Guid
    PartitionId: Guid
    MaxSectionDataLength: UInt32
    MaxSectionsPerRecord: UInt32
    PacketStateBuffer: POINTER(Byte)
    OpenHandles: Int32
    _pack_ = 1
class WHEA_DRIVER_BUFFER_SET(EasyCastStructure):
    Version: UInt32
    Data: POINTER(Byte)
    DataSize: UInt32
    SectionTypeGuid: POINTER(Guid)
    SectionFriendlyName: POINTER(Byte)
    Flags: POINTER(Byte)
    _pack_ = 1
class WHEA_ERROR_SOURCE_CONFIGURATION_DD(EasyCastStructure):
    Initialize: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_ERROR_SOURCE_INITIALIZE_DEVICE_DRIVER
    Uninitialize: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_ERROR_SOURCE_UNINITIALIZE_DEVICE_DRIVER
    Correct: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_ERROR_SOURCE_CORRECT_DEVICE_DRIVER
    _pack_ = 1
class WHEA_ERROR_SOURCE_CONFIGURATION_DEVICE_DRIVER(EasyCastStructure):
    Version: UInt32
    SourceGuid: Guid
    LogTag: UInt16
    Reserved: Byte * 6
    Initialize: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_ERROR_SOURCE_INITIALIZE_DEVICE_DRIVER
    Uninitialize: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_ERROR_SOURCE_UNINITIALIZE_DEVICE_DRIVER
    MaxSectionDataLength: UInt32
    MaxSectionsPerReport: UInt32
    CreatorId: Guid
    PartitionId: Guid
    _pack_ = 1
class WHEA_ERROR_SOURCE_CONFIGURATION_DEVICE_DRIVER_V1(EasyCastStructure):
    Version: UInt32
    SourceGuid: Guid
    LogTag: UInt16
    Reserved: Byte * 6
    Initialize: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_ERROR_SOURCE_INITIALIZE_DEVICE_DRIVER
    Uninitialize: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_ERROR_SOURCE_UNINITIALIZE_DEVICE_DRIVER
    _pack_ = 1
@winfunctype_pointer
def WHEA_ERROR_SOURCE_CORRECT_DEVICE_DRIVER(ErrorSourceDesc: VoidPtr, MaximumSectionLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
class WHEA_ERROR_SOURCE_DESCRIPTOR(EasyCastStructure):
    Length: UInt32
    Version: UInt32
    Type: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_ERROR_SOURCE_TYPE
    State: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_ERROR_SOURCE_STATE
    MaxRawDataLength: UInt32
    NumRecordsToPreallocate: UInt32
    MaxSectionsPerRecord: UInt32
    ErrorSourceId: UInt32
    PlatformErrorSourceId: UInt32
    Flags: UInt32
    Info: _Info_e__Union
    _pack_ = 1
    class _Info_e__Union(EasyCastUnion):
        XpfMceDescriptor: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_XPF_MCE_DESCRIPTOR
        XpfCmcDescriptor: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_XPF_CMC_DESCRIPTOR
        XpfNmiDescriptor: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_XPF_NMI_DESCRIPTOR
        IpfMcaDescriptor: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_IPF_MCA_DESCRIPTOR
        IpfCmcDescriptor: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_IPF_CMC_DESCRIPTOR
        IpfCpeDescriptor: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_IPF_CPE_DESCRIPTOR
        AerRootportDescriptor: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_AER_ROOTPORT_DESCRIPTOR
        AerEndpointDescriptor: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_AER_ENDPOINT_DESCRIPTOR
        AerBridgeDescriptor: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_AER_BRIDGE_DESCRIPTOR
        GenErrDescriptor: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_GENERIC_ERROR_DESCRIPTOR
        GenErrDescriptorV2: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_GENERIC_ERROR_DESCRIPTOR_V2
        DeviceDriverDescriptor: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_DEVICE_DRIVER_DESCRIPTOR
@winfunctype_pointer
def WHEA_ERROR_SOURCE_INITIALIZE_DEVICE_DRIVER(Context: VoidPtr, ErrorSourceId: UInt32) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
WHEA_ERROR_SOURCE_STATE = Int32
WHEA_ERROR_SOURCE_STATE_WheaErrSrcStateStopped: WHEA_ERROR_SOURCE_STATE = 1
WHEA_ERROR_SOURCE_STATE_WheaErrSrcStateStarted: WHEA_ERROR_SOURCE_STATE = 2
WHEA_ERROR_SOURCE_STATE_WheaErrSrcStateRemoved: WHEA_ERROR_SOURCE_STATE = 3
WHEA_ERROR_SOURCE_STATE_WheaErrSrcStateRemovePending: WHEA_ERROR_SOURCE_STATE = 4
WHEA_ERROR_SOURCE_TYPE = Int32
WHEA_ERROR_SOURCE_TYPE_WheaErrSrcTypeMCE: WHEA_ERROR_SOURCE_TYPE = 0
WHEA_ERROR_SOURCE_TYPE_WheaErrSrcTypeCMC: WHEA_ERROR_SOURCE_TYPE = 1
WHEA_ERROR_SOURCE_TYPE_WheaErrSrcTypeCPE: WHEA_ERROR_SOURCE_TYPE = 2
WHEA_ERROR_SOURCE_TYPE_WheaErrSrcTypeNMI: WHEA_ERROR_SOURCE_TYPE = 3
WHEA_ERROR_SOURCE_TYPE_WheaErrSrcTypePCIe: WHEA_ERROR_SOURCE_TYPE = 4
WHEA_ERROR_SOURCE_TYPE_WheaErrSrcTypeGeneric: WHEA_ERROR_SOURCE_TYPE = 5
WHEA_ERROR_SOURCE_TYPE_WheaErrSrcTypeINIT: WHEA_ERROR_SOURCE_TYPE = 6
WHEA_ERROR_SOURCE_TYPE_WheaErrSrcTypeBOOT: WHEA_ERROR_SOURCE_TYPE = 7
WHEA_ERROR_SOURCE_TYPE_WheaErrSrcTypeSCIGeneric: WHEA_ERROR_SOURCE_TYPE = 8
WHEA_ERROR_SOURCE_TYPE_WheaErrSrcTypeIPFMCA: WHEA_ERROR_SOURCE_TYPE = 9
WHEA_ERROR_SOURCE_TYPE_WheaErrSrcTypeIPFCMC: WHEA_ERROR_SOURCE_TYPE = 10
WHEA_ERROR_SOURCE_TYPE_WheaErrSrcTypeIPFCPE: WHEA_ERROR_SOURCE_TYPE = 11
WHEA_ERROR_SOURCE_TYPE_WheaErrSrcTypeGenericV2: WHEA_ERROR_SOURCE_TYPE = 12
WHEA_ERROR_SOURCE_TYPE_WheaErrSrcTypeSCIGenericV2: WHEA_ERROR_SOURCE_TYPE = 13
WHEA_ERROR_SOURCE_TYPE_WheaErrSrcTypeBMC: WHEA_ERROR_SOURCE_TYPE = 14
WHEA_ERROR_SOURCE_TYPE_WheaErrSrcTypePMEM: WHEA_ERROR_SOURCE_TYPE = 15
WHEA_ERROR_SOURCE_TYPE_WheaErrSrcTypeDeviceDriver: WHEA_ERROR_SOURCE_TYPE = 16
WHEA_ERROR_SOURCE_TYPE_WheaErrSrcTypeSea: WHEA_ERROR_SOURCE_TYPE = 17
WHEA_ERROR_SOURCE_TYPE_WheaErrSrcTypeSei: WHEA_ERROR_SOURCE_TYPE = 18
WHEA_ERROR_SOURCE_TYPE_WheaErrSrcTypeMax: WHEA_ERROR_SOURCE_TYPE = 19
@winfunctype_pointer
def WHEA_ERROR_SOURCE_UNINITIALIZE_DEVICE_DRIVER(Context: VoidPtr) -> Void: ...
class WHEA_GENERIC_ERROR_DESCRIPTOR(EasyCastStructure):
    Type: UInt16
    Reserved: Byte
    Enabled: Byte
    ErrStatusBlockLength: UInt32
    RelatedErrorSourceId: UInt32
    ErrStatusAddressSpaceID: Byte
    ErrStatusAddressBitWidth: Byte
    ErrStatusAddressBitOffset: Byte
    ErrStatusAddressAccessSize: Byte
    ErrStatusAddress: Int64
    Notify: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_NOTIFICATION_DESCRIPTOR
    _pack_ = 1
class WHEA_GENERIC_ERROR_DESCRIPTOR_V2(EasyCastStructure):
    Type: UInt16
    Reserved: Byte
    Enabled: Byte
    ErrStatusBlockLength: UInt32
    RelatedErrorSourceId: UInt32
    ErrStatusAddressSpaceID: Byte
    ErrStatusAddressBitWidth: Byte
    ErrStatusAddressBitOffset: Byte
    ErrStatusAddressAccessSize: Byte
    ErrStatusAddress: Int64
    Notify: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_NOTIFICATION_DESCRIPTOR
    ReadAckAddressSpaceID: Byte
    ReadAckAddressBitWidth: Byte
    ReadAckAddressBitOffset: Byte
    ReadAckAddressAccessSize: Byte
    ReadAckAddress: Int64
    ReadAckPreserveMask: UInt64
    ReadAckWriteMask: UInt64
    _pack_ = 1
class WHEA_IPF_CMC_DESCRIPTOR(EasyCastStructure):
    Type: UInt16
    Enabled: Byte
    Reserved: Byte
    _pack_ = 1
class WHEA_IPF_CPE_DESCRIPTOR(EasyCastStructure):
    Type: UInt16
    Enabled: Byte
    Reserved: Byte
    _pack_ = 1
class WHEA_IPF_MCA_DESCRIPTOR(EasyCastStructure):
    Type: UInt16
    Enabled: Byte
    Reserved: Byte
    _pack_ = 1
class WHEA_NOTIFICATION_DESCRIPTOR(EasyCastStructure):
    Type: Byte
    Length: Byte
    Flags: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_NOTIFICATION_FLAGS
    u: _u_e__Union
    class _u_e__Union(EasyCastUnion):
        Polled: _Polled_e__Struct
        Interrupt: _Interrupt_e__Struct
        LocalInterrupt: _LocalInterrupt_e__Struct
        Sci: _Sci_e__Struct
        Nmi: _Nmi_e__Struct
        Sea: _Sea_e__Struct
        Sei: _Sei_e__Struct
        Gsiv: _Gsiv_e__Struct
        class _Polled_e__Struct(EasyCastStructure):
            PollInterval: UInt32
            _pack_ = 1
        class _Interrupt_e__Struct(EasyCastStructure):
            PollInterval: UInt32
            Vector: UInt32
            SwitchToPollingThreshold: UInt32
            SwitchToPollingWindow: UInt32
            ErrorThreshold: UInt32
            ErrorThresholdWindow: UInt32
            _pack_ = 1
        class _LocalInterrupt_e__Struct(EasyCastStructure):
            PollInterval: UInt32
            Vector: UInt32
            SwitchToPollingThreshold: UInt32
            SwitchToPollingWindow: UInt32
            ErrorThreshold: UInt32
            ErrorThresholdWindow: UInt32
            _pack_ = 1
        class _Sci_e__Struct(EasyCastStructure):
            PollInterval: UInt32
            Vector: UInt32
            SwitchToPollingThreshold: UInt32
            SwitchToPollingWindow: UInt32
            ErrorThreshold: UInt32
            ErrorThresholdWindow: UInt32
            _pack_ = 1
        class _Nmi_e__Struct(EasyCastStructure):
            PollInterval: UInt32
            Vector: UInt32
            SwitchToPollingThreshold: UInt32
            SwitchToPollingWindow: UInt32
            ErrorThreshold: UInt32
            ErrorThresholdWindow: UInt32
            _pack_ = 1
        class _Sea_e__Struct(EasyCastStructure):
            PollInterval: UInt32
            Vector: UInt32
            SwitchToPollingThreshold: UInt32
            SwitchToPollingWindow: UInt32
            ErrorThreshold: UInt32
            ErrorThresholdWindow: UInt32
            _pack_ = 1
        class _Sei_e__Struct(EasyCastStructure):
            PollInterval: UInt32
            Vector: UInt32
            SwitchToPollingThreshold: UInt32
            SwitchToPollingWindow: UInt32
            ErrorThreshold: UInt32
            ErrorThresholdWindow: UInt32
            _pack_ = 1
        class _Gsiv_e__Struct(EasyCastStructure):
            PollInterval: UInt32
            Vector: UInt32
            SwitchToPollingThreshold: UInt32
            SwitchToPollingWindow: UInt32
            ErrorThreshold: UInt32
            ErrorThresholdWindow: UInt32
            _pack_ = 1
class WHEA_NOTIFICATION_FLAGS(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUSHORT: UInt16
    _pack_ = 1
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt16
        _pack_ = 1
class WHEA_PCI_SLOT_NUMBER(EasyCastStructure):
    u: _u_e__Union
    class _u_e__Union(EasyCastUnion):
        bits: _bits_e__Struct
        AsULONG: UInt32
        _pack_ = 1
        class _bits_e__Struct(EasyCastStructure):
            _bitfield: UInt32
            _pack_ = 1
class WHEA_XPF_CMC_DESCRIPTOR(EasyCastStructure):
    Type: UInt16
    Enabled: win32more.Windows.Win32.Foundation.BOOLEAN
    NumberOfBanks: Byte
    Reserved: UInt32
    Notify: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_NOTIFICATION_DESCRIPTOR
    Banks: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_XPF_MC_BANK_DESCRIPTOR * 32
    _pack_ = 1
class WHEA_XPF_MCE_DESCRIPTOR(EasyCastStructure):
    Type: UInt16
    Enabled: Byte
    NumberOfBanks: Byte
    Flags: win32more.Windows.Win32.System.Diagnostics.Debug.XPF_MCE_FLAGS
    MCG_Capability: UInt64
    MCG_GlobalControl: UInt64
    Banks: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_XPF_MC_BANK_DESCRIPTOR * 32
    _pack_ = 1
class WHEA_XPF_MC_BANK_DESCRIPTOR(EasyCastStructure):
    BankNumber: Byte
    ClearOnInitialization: win32more.Windows.Win32.Foundation.BOOLEAN
    StatusDataFormat: Byte
    Flags: win32more.Windows.Win32.System.Diagnostics.Debug.XPF_MC_BANK_FLAGS
    ControlMsr: UInt32
    StatusMsr: UInt32
    AddressMsr: UInt32
    MiscMsr: UInt32
    ControlData: UInt64
    _pack_ = 1
class WHEA_XPF_NMI_DESCRIPTOR(EasyCastStructure):
    Type: UInt16
    Enabled: win32more.Windows.Win32.Foundation.BOOLEAN
    _pack_ = 1
class WOW64_CONTEXT(EasyCastStructure):
    ContextFlags: win32more.Windows.Win32.System.Diagnostics.Debug.WOW64_CONTEXT_FLAGS
    Dr0: UInt32
    Dr1: UInt32
    Dr2: UInt32
    Dr3: UInt32
    Dr6: UInt32
    Dr7: UInt32
    FloatSave: win32more.Windows.Win32.System.Diagnostics.Debug.WOW64_FLOATING_SAVE_AREA
    SegGs: UInt32
    SegFs: UInt32
    SegEs: UInt32
    SegDs: UInt32
    Edi: UInt32
    Esi: UInt32
    Ebx: UInt32
    Edx: UInt32
    Ecx: UInt32
    Eax: UInt32
    Ebp: UInt32
    Eip: UInt32
    SegCs: UInt32
    EFlags: UInt32
    Esp: UInt32
    SegSs: UInt32
    ExtendedRegisters: Byte * 512
WOW64_CONTEXT_FLAGS = UInt32
WOW64_CONTEXT_X86: WOW64_CONTEXT_FLAGS = 65536
WOW64_CONTEXT_CONTROL: WOW64_CONTEXT_FLAGS = 65537
WOW64_CONTEXT_INTEGER: WOW64_CONTEXT_FLAGS = 65538
WOW64_CONTEXT_SEGMENTS: WOW64_CONTEXT_FLAGS = 65540
WOW64_CONTEXT_FLOATING_POINT: WOW64_CONTEXT_FLAGS = 65544
WOW64_CONTEXT_DEBUG_REGISTERS: WOW64_CONTEXT_FLAGS = 65552
WOW64_CONTEXT_EXTENDED_REGISTERS: WOW64_CONTEXT_FLAGS = 65568
WOW64_CONTEXT_FULL: WOW64_CONTEXT_FLAGS = 65543
WOW64_CONTEXT_ALL: WOW64_CONTEXT_FLAGS = 65599
WOW64_CONTEXT_XSTATE: WOW64_CONTEXT_FLAGS = 65600
WOW64_CONTEXT_EXCEPTION_ACTIVE: WOW64_CONTEXT_FLAGS = 134217728
WOW64_CONTEXT_SERVICE_ACTIVE: WOW64_CONTEXT_FLAGS = 268435456
WOW64_CONTEXT_EXCEPTION_REQUEST: WOW64_CONTEXT_FLAGS = 1073741824
WOW64_CONTEXT_EXCEPTION_REPORTING: WOW64_CONTEXT_FLAGS = 2147483648
class WOW64_DESCRIPTOR_TABLE_ENTRY(EasyCastStructure):
    Selector: UInt32
    Descriptor: win32more.Windows.Win32.System.Diagnostics.Debug.WOW64_LDT_ENTRY
class WOW64_FLOATING_SAVE_AREA(EasyCastStructure):
    ControlWord: UInt32
    StatusWord: UInt32
    TagWord: UInt32
    ErrorOffset: UInt32
    ErrorSelector: UInt32
    DataOffset: UInt32
    DataSelector: UInt32
    RegisterArea: Byte * 80
    Cr0NpxState: UInt32
class WOW64_LDT_ENTRY(EasyCastStructure):
    LimitLow: UInt16
    BaseLow: UInt16
    HighWord: _HighWord_e__Union
    class _HighWord_e__Union(EasyCastUnion):
        Bytes: _Bytes_e__Struct
        Bits: _Bits_e__Struct
        class _Bytes_e__Struct(EasyCastStructure):
            BaseMid: Byte
            Flags1: Byte
            Flags2: Byte
            BaseHi: Byte
        class _Bits_e__Struct(EasyCastStructure):
            _bitfield: UInt32
class XPF_MCE_FLAGS(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsULONG: UInt32
    _pack_ = 1
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
        _pack_ = 1
class XPF_MC_BANK_FLAGS(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUCHAR: Byte
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: Byte
class XSAVE_AREA(EasyCastStructure):
    LegacyState: win32more.Windows.Win32.System.Diagnostics.Debug.XSAVE_FORMAT
    Header: win32more.Windows.Win32.System.Diagnostics.Debug.XSAVE_AREA_HEADER
class XSAVE_AREA_HEADER(EasyCastStructure):
    Mask: UInt64
    CompactionMask: UInt64
    Reserved2: UInt64 * 6
if ARCH in 'X64,ARM64':
    class XSAVE_FORMAT(EasyCastStructure):
        ControlWord: UInt16
        StatusWord: UInt16
        TagWord: Byte
        Reserved1: Byte
        ErrorOpcode: UInt16
        ErrorOffset: UInt32
        ErrorSelector: UInt16
        Reserved2: UInt16
        DataOffset: UInt32
        DataSelector: UInt16
        Reserved3: UInt16
        MxCsr: UInt32
        MxCsr_Mask: UInt32
        FloatRegisters: win32more.Windows.Win32.System.Diagnostics.Debug.M128A * 8
        XmmRegisters: win32more.Windows.Win32.System.Diagnostics.Debug.M128A * 16
        Reserved4: Byte * 96
if ARCH in 'X86':
    class XSAVE_FORMAT(EasyCastStructure):
        ControlWord: UInt16
        StatusWord: UInt16
        TagWord: Byte
        Reserved1: Byte
        ErrorOpcode: UInt16
        ErrorOffset: UInt32
        ErrorSelector: UInt16
        Reserved2: UInt16
        DataOffset: UInt32
        DataSelector: UInt16
        Reserved3: UInt16
        MxCsr: UInt32
        MxCsr_Mask: UInt32
        FloatRegisters: win32more.Windows.Win32.System.Diagnostics.Debug.M128A * 8
        XmmRegisters: win32more.Windows.Win32.System.Diagnostics.Debug.M128A * 8
        Reserved4: Byte * 224
class XSTATE_CONFIGURATION(EasyCastStructure):
    EnabledFeatures: UInt64
    EnabledVolatileFeatures: UInt64
    Size: UInt32
    Anonymous: _Anonymous_e__Union
    Features: win32more.Windows.Win32.System.Diagnostics.Debug.XSTATE_FEATURE * 64
    EnabledSupervisorFeatures: UInt64
    AlignedFeatures: UInt64
    AllFeatureSize: UInt32
    AllFeatures: UInt32 * 64
    EnabledUserVisibleSupervisorFeatures: UInt64
    ExtendedFeatureDisableFeatures: UInt64
    AllNonLargeFeatureSize: UInt32
    Spare: UInt32
    class _Anonymous_e__Union(EasyCastUnion):
        ControlFlags: UInt32
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(EasyCastStructure):
            _bitfield: UInt32
class XSTATE_CONFIG_FEATURE_MSC_INFO(EasyCastStructure):
    SizeOfInfo: UInt32
    ContextSize: UInt32
    EnabledFeatures: UInt64
    Features: win32more.Windows.Win32.System.Diagnostics.Debug.XSTATE_FEATURE * 64
    _pack_ = 4
if ARCH in 'X64,ARM64':
    class XSTATE_CONTEXT(EasyCastStructure):
        Mask: UInt64
        Length: UInt32
        Reserved1: UInt32
        Area: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.XSAVE_AREA_head)
        Buffer: VoidPtr
if ARCH in 'X86':
    class XSTATE_CONTEXT(EasyCastStructure):
        Mask: UInt64
        Length: UInt32
        Reserved1: UInt32
        Area: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.XSAVE_AREA_head)
        Reserved2: UInt32
        Buffer: VoidPtr
        Reserved3: UInt32
class XSTATE_FEATURE(EasyCastStructure):
    Offset: UInt32
    Size: UInt32
if ARCH in 'X86':
    make_head(_module, 'ADDRESS')
make_head(_module, 'ADDRESS64')
make_head(_module, 'AER_BRIDGE_DESCRIPTOR_FLAGS')
make_head(_module, 'AER_ENDPOINT_DESCRIPTOR_FLAGS')
make_head(_module, 'AER_ROOTPORT_DESCRIPTOR_FLAGS')
make_head(_module, 'APC_CALLBACK_DATA')
make_head(_module, 'API_VERSION')
if ARCH in 'X86,X64':
    make_head(_module, 'ARM64_NT_CONTEXT')
make_head(_module, 'ARM64_NT_NEON128')
if ARCH in 'ARM64':
    make_head(_module, 'CONTEXT')
if ARCH in 'X64':
    make_head(_module, 'CONTEXT')
if ARCH in 'X86':
    make_head(_module, 'CONTEXT')
make_head(_module, 'CPU_INFORMATION')
make_head(_module, 'CREATE_PROCESS_DEBUG_INFO')
make_head(_module, 'CREATE_THREAD_DEBUG_INFO')
make_head(_module, 'DBGHELP_DATA_REPORT_STRUCT')
make_head(_module, 'DEBUG_EVENT')
make_head(_module, 'DIGEST_FUNCTION')
if ARCH in 'ARM64':
    make_head(_module, 'DISPATCHER_CONTEXT')
if ARCH in 'X64':
    make_head(_module, 'DISPATCHER_CONTEXT')
make_head(_module, 'DUMP_FILE_ATTRIBUTES')
make_head(_module, 'DUMP_HEADER32')
make_head(_module, 'DUMP_HEADER64')
make_head(_module, 'DebugPropertyInfo')
make_head(_module, 'EXCEPTION_DEBUG_INFO')
make_head(_module, 'EXCEPTION_POINTERS')
make_head(_module, 'EXCEPTION_RECORD')
make_head(_module, 'EXCEPTION_RECORD32')
make_head(_module, 'EXCEPTION_RECORD64')
make_head(_module, 'EXIT_PROCESS_DEBUG_INFO')
make_head(_module, 'EXIT_THREAD_DEBUG_INFO')
make_head(_module, 'ExtendedDebugPropertyInfo')
make_head(_module, 'FPO_DATA')
make_head(_module, 'IDebugExtendedProperty')
make_head(_module, 'IDebugProperty')
make_head(_module, 'IDebugPropertyEnumType_All')
make_head(_module, 'IDebugPropertyEnumType_Arguments')
make_head(_module, 'IDebugPropertyEnumType_Locals')
make_head(_module, 'IDebugPropertyEnumType_LocalsPlusArgs')
make_head(_module, 'IDebugPropertyEnumType_Registers')
make_head(_module, 'IEnumDebugExtendedPropertyInfo')
make_head(_module, 'IEnumDebugPropertyInfo')
make_head(_module, 'IMAGEHLP_CBA_EVENT')
make_head(_module, 'IMAGEHLP_CBA_EVENTW')
make_head(_module, 'IMAGEHLP_CBA_READ_MEMORY')
if ARCH in 'X86':
    make_head(_module, 'IMAGEHLP_DEFERRED_SYMBOL_LOAD')
make_head(_module, 'IMAGEHLP_DEFERRED_SYMBOL_LOAD64')
make_head(_module, 'IMAGEHLP_DEFERRED_SYMBOL_LOADW64')
if ARCH in 'X86':
    make_head(_module, 'IMAGEHLP_DUPLICATE_SYMBOL')
make_head(_module, 'IMAGEHLP_DUPLICATE_SYMBOL64')
make_head(_module, 'IMAGEHLP_GET_TYPE_INFO_PARAMS')
make_head(_module, 'IMAGEHLP_JIT_SYMBOLMAP')
if ARCH in 'X86':
    make_head(_module, 'IMAGEHLP_LINE')
make_head(_module, 'IMAGEHLP_LINE64')
if ARCH in 'X86':
    make_head(_module, 'IMAGEHLP_LINEW')
make_head(_module, 'IMAGEHLP_LINEW64')
if ARCH in 'X86':
    make_head(_module, 'IMAGEHLP_MODULE')
make_head(_module, 'IMAGEHLP_MODULE64')
make_head(_module, 'IMAGEHLP_MODULE64_EX')
if ARCH in 'X86':
    make_head(_module, 'IMAGEHLP_MODULEW')
make_head(_module, 'IMAGEHLP_MODULEW64')
make_head(_module, 'IMAGEHLP_MODULEW64_EX')
make_head(_module, 'IMAGEHLP_STACK_FRAME')
if ARCH in 'X86':
    make_head(_module, 'IMAGEHLP_SYMBOL')
make_head(_module, 'IMAGEHLP_SYMBOL64')
make_head(_module, 'IMAGEHLP_SYMBOL64_PACKAGE')
if ARCH in 'X86':
    make_head(_module, 'IMAGEHLP_SYMBOLW')
make_head(_module, 'IMAGEHLP_SYMBOLW64')
make_head(_module, 'IMAGEHLP_SYMBOLW64_PACKAGE')
if ARCH in 'X86':
    make_head(_module, 'IMAGEHLP_SYMBOLW_PACKAGE')
if ARCH in 'X86':
    make_head(_module, 'IMAGEHLP_SYMBOL_PACKAGE')
make_head(_module, 'IMAGEHLP_SYMBOL_SRC')
make_head(_module, 'IMAGE_ARM64_RUNTIME_FUNCTION_ENTRY')
make_head(_module, 'IMAGE_COFF_SYMBOLS_HEADER')
make_head(_module, 'IMAGE_COR20_HEADER')
make_head(_module, 'IMAGE_DATA_DIRECTORY')
make_head(_module, 'IMAGE_DEBUG_DIRECTORY')
if ARCH in 'X86':
    make_head(_module, 'IMAGE_DEBUG_INFORMATION')
make_head(_module, 'IMAGE_FILE_HEADER')
make_head(_module, 'IMAGE_FUNCTION_ENTRY')
make_head(_module, 'IMAGE_FUNCTION_ENTRY64')
make_head(_module, 'IMAGE_LOAD_CONFIG_CODE_INTEGRITY')
make_head(_module, 'IMAGE_LOAD_CONFIG_DIRECTORY32')
make_head(_module, 'IMAGE_LOAD_CONFIG_DIRECTORY64')
make_head(_module, 'IMAGE_NT_HEADERS32')
make_head(_module, 'IMAGE_NT_HEADERS64')
make_head(_module, 'IMAGE_OPTIONAL_HEADER32')
make_head(_module, 'IMAGE_OPTIONAL_HEADER64')
make_head(_module, 'IMAGE_ROM_HEADERS')
make_head(_module, 'IMAGE_ROM_OPTIONAL_HEADER')
make_head(_module, 'IMAGE_RUNTIME_FUNCTION_ENTRY')
make_head(_module, 'IMAGE_SECTION_HEADER')
make_head(_module, 'IObjectSafety')
make_head(_module, 'IPMI_OS_SEL_RECORD')
make_head(_module, 'IPerPropertyBrowsing2')
if ARCH in 'X86':
    make_head(_module, 'KDHELP')
make_head(_module, 'KDHELP64')
if ARCH in 'X64':
    make_head(_module, 'KNONVOLATILE_CONTEXT_POINTERS')
if ARCH in 'X86':
    make_head(_module, 'KNONVOLATILE_CONTEXT_POINTERS')
if ARCH in 'ARM64':
    make_head(_module, 'KNONVOLATILE_CONTEXT_POINTERS_ARM64')
make_head(_module, 'LDT_ENTRY')
if ARCH in 'X64,ARM64':
    make_head(_module, 'LOADED_IMAGE')
if ARCH in 'X86':
    make_head(_module, 'LOADED_IMAGE')
make_head(_module, 'LOAD_DLL_DEBUG_INFO')
make_head(_module, 'LPCALL_BACK_USER_INTERRUPT_ROUTINE')
make_head(_module, 'LPTOP_LEVEL_EXCEPTION_FILTER')
make_head(_module, 'M128A')
if ARCH in 'X64,ARM64':
    make_head(_module, 'MINIDUMP_CALLBACK_INFORMATION')
if ARCH in 'X86':
    make_head(_module, 'MINIDUMP_CALLBACK_INFORMATION')
make_head(_module, 'MINIDUMP_CALLBACK_INPUT')
make_head(_module, 'MINIDUMP_CALLBACK_OUTPUT')
make_head(_module, 'MINIDUMP_CALLBACK_ROUTINE')
make_head(_module, 'MINIDUMP_DIRECTORY')
make_head(_module, 'MINIDUMP_EXCEPTION')
if ARCH in 'X64,ARM64':
    make_head(_module, 'MINIDUMP_EXCEPTION_INFORMATION')
if ARCH in 'X86':
    make_head(_module, 'MINIDUMP_EXCEPTION_INFORMATION')
make_head(_module, 'MINIDUMP_EXCEPTION_INFORMATION64')
make_head(_module, 'MINIDUMP_EXCEPTION_STREAM')
make_head(_module, 'MINIDUMP_FUNCTION_TABLE_DESCRIPTOR')
make_head(_module, 'MINIDUMP_FUNCTION_TABLE_STREAM')
make_head(_module, 'MINIDUMP_HANDLE_DATA_STREAM')
make_head(_module, 'MINIDUMP_HANDLE_DESCRIPTOR')
make_head(_module, 'MINIDUMP_HANDLE_DESCRIPTOR_2')
make_head(_module, 'MINIDUMP_HANDLE_OBJECT_INFORMATION')
make_head(_module, 'MINIDUMP_HANDLE_OPERATION_LIST')
make_head(_module, 'MINIDUMP_HEADER')
make_head(_module, 'MINIDUMP_INCLUDE_MODULE_CALLBACK')
make_head(_module, 'MINIDUMP_INCLUDE_THREAD_CALLBACK')
make_head(_module, 'MINIDUMP_IO_CALLBACK')
make_head(_module, 'MINIDUMP_LOCATION_DESCRIPTOR')
make_head(_module, 'MINIDUMP_LOCATION_DESCRIPTOR64')
make_head(_module, 'MINIDUMP_MEMORY64_LIST')
make_head(_module, 'MINIDUMP_MEMORY_DESCRIPTOR')
make_head(_module, 'MINIDUMP_MEMORY_DESCRIPTOR64')
make_head(_module, 'MINIDUMP_MEMORY_INFO')
make_head(_module, 'MINIDUMP_MEMORY_INFO_LIST')
make_head(_module, 'MINIDUMP_MEMORY_LIST')
make_head(_module, 'MINIDUMP_MISC_INFO')
make_head(_module, 'MINIDUMP_MISC_INFO_2')
make_head(_module, 'MINIDUMP_MISC_INFO_3')
make_head(_module, 'MINIDUMP_MISC_INFO_4')
make_head(_module, 'MINIDUMP_MISC_INFO_5')
make_head(_module, 'MINIDUMP_MODULE')
make_head(_module, 'MINIDUMP_MODULE_CALLBACK')
make_head(_module, 'MINIDUMP_MODULE_LIST')
make_head(_module, 'MINIDUMP_PROCESS_VM_COUNTERS_1')
make_head(_module, 'MINIDUMP_PROCESS_VM_COUNTERS_2')
make_head(_module, 'MINIDUMP_READ_MEMORY_FAILURE_CALLBACK')
make_head(_module, 'MINIDUMP_STRING')
make_head(_module, 'MINIDUMP_SYSTEM_BASIC_INFORMATION')
make_head(_module, 'MINIDUMP_SYSTEM_BASIC_PERFORMANCE_INFORMATION')
make_head(_module, 'MINIDUMP_SYSTEM_FILECACHE_INFORMATION')
make_head(_module, 'MINIDUMP_SYSTEM_INFO')
make_head(_module, 'MINIDUMP_SYSTEM_MEMORY_INFO_1')
make_head(_module, 'MINIDUMP_SYSTEM_PERFORMANCE_INFORMATION')
make_head(_module, 'MINIDUMP_THREAD')
if ARCH in 'ARM64':
    make_head(_module, 'MINIDUMP_THREAD_CALLBACK')
if ARCH in 'X86,X64':
    make_head(_module, 'MINIDUMP_THREAD_CALLBACK')
make_head(_module, 'MINIDUMP_THREAD_EX')
if ARCH in 'ARM64':
    make_head(_module, 'MINIDUMP_THREAD_EX_CALLBACK')
if ARCH in 'X86,X64':
    make_head(_module, 'MINIDUMP_THREAD_EX_CALLBACK')
make_head(_module, 'MINIDUMP_THREAD_EX_LIST')
make_head(_module, 'MINIDUMP_THREAD_INFO')
make_head(_module, 'MINIDUMP_THREAD_INFO_LIST')
make_head(_module, 'MINIDUMP_THREAD_LIST')
make_head(_module, 'MINIDUMP_THREAD_NAME')
make_head(_module, 'MINIDUMP_THREAD_NAME_LIST')
make_head(_module, 'MINIDUMP_TOKEN_INFO_HEADER')
make_head(_module, 'MINIDUMP_TOKEN_INFO_LIST')
make_head(_module, 'MINIDUMP_UNLOADED_MODULE')
make_head(_module, 'MINIDUMP_UNLOADED_MODULE_LIST')
make_head(_module, 'MINIDUMP_USER_RECORD')
if ARCH in 'X64,ARM64':
    make_head(_module, 'MINIDUMP_USER_STREAM')
if ARCH in 'X86':
    make_head(_module, 'MINIDUMP_USER_STREAM')
if ARCH in 'X64,ARM64':
    make_head(_module, 'MINIDUMP_USER_STREAM_INFORMATION')
if ARCH in 'X86':
    make_head(_module, 'MINIDUMP_USER_STREAM_INFORMATION')
make_head(_module, 'MINIDUMP_VM_POST_READ_CALLBACK')
make_head(_module, 'MINIDUMP_VM_PRE_READ_CALLBACK')
make_head(_module, 'MINIDUMP_VM_QUERY_CALLBACK')
make_head(_module, 'MODLOAD_CVMISC')
make_head(_module, 'MODLOAD_DATA')
make_head(_module, 'MODLOAD_PDBGUID_PDBAGE')
make_head(_module, 'MODULE_TYPE_INFO')
make_head(_module, 'OMAP')
make_head(_module, 'OUTPUT_DEBUG_STRING_INFO')
make_head(_module, 'PCOGETACTIVATIONSTATE')
make_head(_module, 'PCOGETCALLSTATE')
make_head(_module, 'PDBGHELP_CREATE_USER_DUMP_CALLBACK')
make_head(_module, 'PENUMDIRTREE_CALLBACK')
make_head(_module, 'PENUMDIRTREE_CALLBACKW')
if ARCH in 'X86':
    make_head(_module, 'PENUMLOADED_MODULES_CALLBACK')
make_head(_module, 'PENUMLOADED_MODULES_CALLBACK64')
make_head(_module, 'PENUMLOADED_MODULES_CALLBACKW64')
make_head(_module, 'PENUMSOURCEFILETOKENSCALLBACK')
make_head(_module, 'PFINDFILEINPATHCALLBACK')
make_head(_module, 'PFINDFILEINPATHCALLBACKW')
make_head(_module, 'PFIND_DEBUG_FILE_CALLBACK')
make_head(_module, 'PFIND_DEBUG_FILE_CALLBACKW')
make_head(_module, 'PFIND_EXE_FILE_CALLBACK')
make_head(_module, 'PFIND_EXE_FILE_CALLBACKW')
if ARCH in 'X86':
    make_head(_module, 'PFUNCTION_TABLE_ACCESS_ROUTINE')
make_head(_module, 'PFUNCTION_TABLE_ACCESS_ROUTINE64')
if ARCH in 'X86':
    make_head(_module, 'PGET_MODULE_BASE_ROUTINE')
make_head(_module, 'PGET_MODULE_BASE_ROUTINE64')
if ARCH in 'ARM64':
    make_head(_module, 'PGET_RUNTIME_FUNCTION_CALLBACK')
if ARCH in 'X64':
    make_head(_module, 'PGET_RUNTIME_FUNCTION_CALLBACK')
make_head(_module, 'PGET_TARGET_ATTRIBUTE_VALUE64')
make_head(_module, 'PHYSICAL_MEMORY_DESCRIPTOR32')
make_head(_module, 'PHYSICAL_MEMORY_DESCRIPTOR64')
make_head(_module, 'PHYSICAL_MEMORY_RUN32')
make_head(_module, 'PHYSICAL_MEMORY_RUN64')
make_head(_module, 'PIMAGEHLP_STATUS_ROUTINE')
make_head(_module, 'PIMAGEHLP_STATUS_ROUTINE32')
make_head(_module, 'PIMAGEHLP_STATUS_ROUTINE64')
if ARCH in 'X86':
    make_head(_module, 'PREAD_PROCESS_MEMORY_ROUTINE')
make_head(_module, 'PREAD_PROCESS_MEMORY_ROUTINE64')
make_head(_module, 'PSYMBOLSERVERBYINDEXPROC')
make_head(_module, 'PSYMBOLSERVERBYINDEXPROCA')
make_head(_module, 'PSYMBOLSERVERBYINDEXPROCW')
make_head(_module, 'PSYMBOLSERVERCALLBACKPROC')
make_head(_module, 'PSYMBOLSERVERCLOSEPROC')
make_head(_module, 'PSYMBOLSERVERDELTANAME')
make_head(_module, 'PSYMBOLSERVERDELTANAMEW')
make_head(_module, 'PSYMBOLSERVERGETINDEXSTRING')
make_head(_module, 'PSYMBOLSERVERGETINDEXSTRINGW')
make_head(_module, 'PSYMBOLSERVERGETOPTIONDATAPROC')
make_head(_module, 'PSYMBOLSERVERGETOPTIONSPROC')
make_head(_module, 'PSYMBOLSERVERGETSUPPLEMENT')
make_head(_module, 'PSYMBOLSERVERGETSUPPLEMENTW')
make_head(_module, 'PSYMBOLSERVERGETVERSION')
make_head(_module, 'PSYMBOLSERVERISSTORE')
make_head(_module, 'PSYMBOLSERVERISSTOREW')
make_head(_module, 'PSYMBOLSERVERMESSAGEPROC')
make_head(_module, 'PSYMBOLSERVEROPENPROC')
make_head(_module, 'PSYMBOLSERVERPINGPROC')
make_head(_module, 'PSYMBOLSERVERPINGPROCA')
make_head(_module, 'PSYMBOLSERVERPINGPROCW')
make_head(_module, 'PSYMBOLSERVERPINGPROCWEX')
make_head(_module, 'PSYMBOLSERVERPROC')
make_head(_module, 'PSYMBOLSERVERPROCA')
make_head(_module, 'PSYMBOLSERVERPROCW')
make_head(_module, 'PSYMBOLSERVERSETHTTPAUTHHEADER')
make_head(_module, 'PSYMBOLSERVERSETOPTIONSPROC')
make_head(_module, 'PSYMBOLSERVERSETOPTIONSWPROC')
make_head(_module, 'PSYMBOLSERVERSTOREFILE')
make_head(_module, 'PSYMBOLSERVERSTOREFILEW')
make_head(_module, 'PSYMBOLSERVERSTORESUPPLEMENT')
make_head(_module, 'PSYMBOLSERVERSTORESUPPLEMENTW')
make_head(_module, 'PSYMBOLSERVERVERSION')
make_head(_module, 'PSYMBOLSERVERWEXPROC')
make_head(_module, 'PSYMBOL_FUNCENTRY_CALLBACK')
make_head(_module, 'PSYMBOL_FUNCENTRY_CALLBACK64')
if ARCH in 'X86':
    make_head(_module, 'PSYMBOL_REGISTERED_CALLBACK')
make_head(_module, 'PSYMBOL_REGISTERED_CALLBACK64')
make_head(_module, 'PSYM_ENUMERATESYMBOLS_CALLBACK')
make_head(_module, 'PSYM_ENUMERATESYMBOLS_CALLBACKW')
make_head(_module, 'PSYM_ENUMLINES_CALLBACK')
make_head(_module, 'PSYM_ENUMLINES_CALLBACKW')
if ARCH in 'X86':
    make_head(_module, 'PSYM_ENUMMODULES_CALLBACK')
make_head(_module, 'PSYM_ENUMMODULES_CALLBACK64')
make_head(_module, 'PSYM_ENUMMODULES_CALLBACKW64')
make_head(_module, 'PSYM_ENUMPROCESSES_CALLBACK')
make_head(_module, 'PSYM_ENUMSOURCEFILES_CALLBACK')
make_head(_module, 'PSYM_ENUMSOURCEFILES_CALLBACKW')
if ARCH in 'X86':
    make_head(_module, 'PSYM_ENUMSYMBOLS_CALLBACK')
make_head(_module, 'PSYM_ENUMSYMBOLS_CALLBACK64')
make_head(_module, 'PSYM_ENUMSYMBOLS_CALLBACK64W')
if ARCH in 'X86':
    make_head(_module, 'PSYM_ENUMSYMBOLS_CALLBACKW')
if ARCH in 'X86':
    make_head(_module, 'PTRANSLATE_ADDRESS_ROUTINE')
make_head(_module, 'PTRANSLATE_ADDRESS_ROUTINE64')
make_head(_module, 'PVECTORED_EXCEPTION_HANDLER')
make_head(_module, 'PWAITCHAINCALLBACK')
make_head(_module, 'RIP_INFO')
make_head(_module, 'SOURCEFILE')
make_head(_module, 'SOURCEFILEW')
make_head(_module, 'SRCCODEINFO')
make_head(_module, 'SRCCODEINFOW')
if ARCH in 'X86':
    make_head(_module, 'STACKFRAME')
make_head(_module, 'STACKFRAME64')
make_head(_module, 'STACKFRAME_EX')
make_head(_module, 'SYMADDSOURCESTREAM')
make_head(_module, 'SYMADDSOURCESTREAMA')
make_head(_module, 'SYMBOL_INFO')
make_head(_module, 'SYMBOL_INFOW')
make_head(_module, 'SYMBOL_INFO_PACKAGE')
make_head(_module, 'SYMBOL_INFO_PACKAGEW')
make_head(_module, 'SYMSRV_EXTENDED_OUTPUT_DATA')
make_head(_module, 'SYMSRV_INDEX_INFO')
make_head(_module, 'SYMSRV_INDEX_INFOW')
make_head(_module, 'TI_FINDCHILDREN_PARAMS')
make_head(_module, 'UNLOAD_DLL_DEBUG_INFO')
if ARCH in 'X64,ARM64':
    make_head(_module, 'UNWIND_HISTORY_TABLE')
if ARCH in 'ARM64':
    make_head(_module, 'UNWIND_HISTORY_TABLE_ENTRY')
if ARCH in 'X64':
    make_head(_module, 'UNWIND_HISTORY_TABLE_ENTRY')
make_head(_module, 'WAITCHAIN_NODE_INFO')
make_head(_module, 'WHEA_AER_BRIDGE_DESCRIPTOR')
make_head(_module, 'WHEA_AER_ENDPOINT_DESCRIPTOR')
make_head(_module, 'WHEA_AER_ROOTPORT_DESCRIPTOR')
make_head(_module, 'WHEA_DEVICE_DRIVER_DESCRIPTOR')
make_head(_module, 'WHEA_DRIVER_BUFFER_SET')
make_head(_module, 'WHEA_ERROR_SOURCE_CONFIGURATION_DD')
make_head(_module, 'WHEA_ERROR_SOURCE_CONFIGURATION_DEVICE_DRIVER')
make_head(_module, 'WHEA_ERROR_SOURCE_CONFIGURATION_DEVICE_DRIVER_V1')
make_head(_module, 'WHEA_ERROR_SOURCE_CORRECT_DEVICE_DRIVER')
make_head(_module, 'WHEA_ERROR_SOURCE_DESCRIPTOR')
make_head(_module, 'WHEA_ERROR_SOURCE_INITIALIZE_DEVICE_DRIVER')
make_head(_module, 'WHEA_ERROR_SOURCE_UNINITIALIZE_DEVICE_DRIVER')
make_head(_module, 'WHEA_GENERIC_ERROR_DESCRIPTOR')
make_head(_module, 'WHEA_GENERIC_ERROR_DESCRIPTOR_V2')
make_head(_module, 'WHEA_IPF_CMC_DESCRIPTOR')
make_head(_module, 'WHEA_IPF_CPE_DESCRIPTOR')
make_head(_module, 'WHEA_IPF_MCA_DESCRIPTOR')
make_head(_module, 'WHEA_NOTIFICATION_DESCRIPTOR')
make_head(_module, 'WHEA_NOTIFICATION_FLAGS')
make_head(_module, 'WHEA_PCI_SLOT_NUMBER')
make_head(_module, 'WHEA_XPF_CMC_DESCRIPTOR')
make_head(_module, 'WHEA_XPF_MCE_DESCRIPTOR')
make_head(_module, 'WHEA_XPF_MC_BANK_DESCRIPTOR')
make_head(_module, 'WHEA_XPF_NMI_DESCRIPTOR')
make_head(_module, 'WOW64_CONTEXT')
make_head(_module, 'WOW64_DESCRIPTOR_TABLE_ENTRY')
make_head(_module, 'WOW64_FLOATING_SAVE_AREA')
make_head(_module, 'WOW64_LDT_ENTRY')
make_head(_module, 'XPF_MCE_FLAGS')
make_head(_module, 'XPF_MC_BANK_FLAGS')
make_head(_module, 'XSAVE_AREA')
make_head(_module, 'XSAVE_AREA_HEADER')
if ARCH in 'X64,ARM64':
    make_head(_module, 'XSAVE_FORMAT')
if ARCH in 'X86':
    make_head(_module, 'XSAVE_FORMAT')
make_head(_module, 'XSTATE_CONFIGURATION')
make_head(_module, 'XSTATE_CONFIG_FEATURE_MSC_INFO')
if ARCH in 'X64,ARM64':
    make_head(_module, 'XSTATE_CONTEXT')
if ARCH in 'X86':
    make_head(_module, 'XSTATE_CONTEXT')
make_head(_module, 'XSTATE_FEATURE')
