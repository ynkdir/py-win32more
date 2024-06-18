from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
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
if ARCH in 'X86':
    class ADDRESS(Structure):
        Offset: UInt32
        Segment: UInt16
        Mode: win32more.Windows.Win32.System.Diagnostics.Debug.ADDRESS_MODE
class ADDRESS64(Structure):
    Offset: UInt64
    Segment: UInt16
    Mode: win32more.Windows.Win32.System.Diagnostics.Debug.ADDRESS_MODE
ADDRESS_MODE = Int32
AddrMode1616: win32more.Windows.Win32.System.Diagnostics.Debug.ADDRESS_MODE = 0
AddrMode1632: win32more.Windows.Win32.System.Diagnostics.Debug.ADDRESS_MODE = 1
AddrModeReal: win32more.Windows.Win32.System.Diagnostics.Debug.ADDRESS_MODE = 2
AddrModeFlat: win32more.Windows.Win32.System.Diagnostics.Debug.ADDRESS_MODE = 3
class AER_BRIDGE_DESCRIPTOR_FLAGS(Union):
    Anonymous: _Anonymous_e__Struct
    AsUSHORT: UInt16
    _pack_ = 1
    class _Anonymous_e__Struct(Structure):
        UncorrectableErrorMaskRW: Annotated[UInt16, 1]
        UncorrectableErrorSeverityRW: Annotated[UInt16, 1]
        CorrectableErrorMaskRW: Annotated[UInt16, 1]
        AdvancedCapsAndControlRW: Annotated[UInt16, 1]
        SecondaryUncorrectableErrorMaskRW: Annotated[UInt16, 1]
        SecondaryUncorrectableErrorSevRW: Annotated[UInt16, 1]
        SecondaryCapsAndControlRW: Annotated[UInt16, 1]
        Reserved: Annotated[UInt16, 9]
        _pack_ = 1
class AER_ENDPOINT_DESCRIPTOR_FLAGS(Union):
    Anonymous: _Anonymous_e__Struct
    AsUSHORT: UInt16
    _pack_ = 1
    class _Anonymous_e__Struct(Structure):
        UncorrectableErrorMaskRW: Annotated[UInt16, 1]
        UncorrectableErrorSeverityRW: Annotated[UInt16, 1]
        CorrectableErrorMaskRW: Annotated[UInt16, 1]
        AdvancedCapsAndControlRW: Annotated[UInt16, 1]
        Reserved: Annotated[UInt16, 12]
        _pack_ = 1
class AER_ROOTPORT_DESCRIPTOR_FLAGS(Union):
    Anonymous: _Anonymous_e__Struct
    AsUSHORT: UInt16
    _pack_ = 1
    class _Anonymous_e__Struct(Structure):
        UncorrectableErrorMaskRW: Annotated[UInt16, 1]
        UncorrectableErrorSeverityRW: Annotated[UInt16, 1]
        CorrectableErrorMaskRW: Annotated[UInt16, 1]
        AdvancedCapsAndControlRW: Annotated[UInt16, 1]
        RootErrorCommandRW: Annotated[UInt16, 1]
        Reserved: Annotated[UInt16, 11]
        _pack_ = 1
class APC_CALLBACK_DATA(Structure):
    Parameter: UIntPtr
    ContextRecord: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT)
    Reserved0: UIntPtr
    Reserved1: UIntPtr
class API_VERSION(Structure):
    MajorVersion: UInt16
    MinorVersion: UInt16
    Revision: UInt16
    Reserved: UInt16
if ARCH in 'X86,X64':
    class ARM64_NT_CONTEXT(Structure):
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
        class _Anonymous_e__Union(Union):
            Anonymous: _Anonymous_e__Struct
            X: UInt64 * 31
            class _Anonymous_e__Struct(Structure):
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
class ARM64_NT_NEON128(Union):
    Anonymous: _Anonymous_e__Struct
    D: Double * 2
    S: Single * 4
    H: UInt16 * 8
    B: Byte * 16
    class _Anonymous_e__Struct(Structure):
        Low: UInt64
        High: Int64
EXCEPTION_EXECUTE_HANDLER: Int32 = 1
EXCEPTION_CONTINUE_SEARCH: Int32 = 0
EXCEPTION_CONTINUE_EXECUTION: Int32 = -1
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
    def RtlAddFunctionTable(FunctionTable: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_ARM64_RUNTIME_FUNCTION_ENTRY), EntryCount: UInt32, BaseAddress: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
elif ARCH in 'X64':
    @winfunctype('KERNEL32.dll')
    def RtlAddFunctionTable(FunctionTable: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_RUNTIME_FUNCTION_ENTRY), EntryCount: UInt32, BaseAddress: UInt64) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
if ARCH in 'ARM64':
    @winfunctype('KERNEL32.dll')
    def RtlDeleteFunctionTable(FunctionTable: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_ARM64_RUNTIME_FUNCTION_ENTRY)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
elif ARCH in 'X64':
    @winfunctype('KERNEL32.dll')
    def RtlDeleteFunctionTable(FunctionTable: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_RUNTIME_FUNCTION_ENTRY)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
if ARCH in 'ARM64':
    @winfunctype('KERNEL32.dll')
    def RtlInstallFunctionTableCallback(TableIdentifier: UInt64, BaseAddress: UInt64, Length: UInt32, Callback: win32more.Windows.Win32.System.Diagnostics.Debug.PGET_RUNTIME_FUNCTION_CALLBACK, Context: VoidPtr, OutOfProcessCallbackDll: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
elif ARCH in 'X64':
    @winfunctype('KERNEL32.dll')
    def RtlInstallFunctionTableCallback(TableIdentifier: UInt64, BaseAddress: UInt64, Length: UInt32, Callback: win32more.Windows.Win32.System.Diagnostics.Debug.PGET_RUNTIME_FUNCTION_CALLBACK, Context: VoidPtr, OutOfProcessCallbackDll: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
if ARCH in 'ARM64':
    @winfunctype('ntdll.dll')
    def RtlAddGrowableFunctionTable(DynamicTable: POINTER(VoidPtr), FunctionTable: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_ARM64_RUNTIME_FUNCTION_ENTRY), EntryCount: UInt32, MaximumEntryCount: UInt32, RangeBase: UIntPtr, RangeEnd: UIntPtr) -> UInt32: ...
elif ARCH in 'X64':
    @winfunctype('ntdll.dll')
    def RtlAddGrowableFunctionTable(DynamicTable: POINTER(VoidPtr), FunctionTable: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_RUNTIME_FUNCTION_ENTRY), EntryCount: UInt32, MaximumEntryCount: UInt32, RangeBase: UIntPtr, RangeEnd: UIntPtr) -> UInt32: ...
if ARCH in 'ARM64':
    @winfunctype('KERNEL32.dll')
    def RtlLookupFunctionEntry(ControlPc: UIntPtr, ImageBase: POINTER(UIntPtr), HistoryTable: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.UNWIND_HISTORY_TABLE)) -> POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_ARM64_RUNTIME_FUNCTION_ENTRY): ...
elif ARCH in 'X64':
    @winfunctype('KERNEL32.dll')
    def RtlLookupFunctionEntry(ControlPc: UInt64, ImageBase: POINTER(UInt64), HistoryTable: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.UNWIND_HISTORY_TABLE)) -> POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_RUNTIME_FUNCTION_ENTRY): ...
if ARCH in 'ARM64':
    @winfunctype('KERNEL32.dll')
    def RtlVirtualUnwind(HandlerType: win32more.Windows.Win32.System.Diagnostics.Debug.RTL_VIRTUAL_UNWIND_HANDLER_TYPE, ImageBase: UIntPtr, ControlPc: UIntPtr, FunctionEntry: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_ARM64_RUNTIME_FUNCTION_ENTRY), ContextRecord: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT), HandlerData: POINTER(VoidPtr), EstablisherFrame: POINTER(UIntPtr), ContextPointers: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.KNONVOLATILE_CONTEXT_POINTERS)) -> win32more.Windows.Win32.System.Kernel.EXCEPTION_ROUTINE: ...
elif ARCH in 'X64':
    @winfunctype('KERNEL32.dll')
    def RtlVirtualUnwind(HandlerType: win32more.Windows.Win32.System.Diagnostics.Debug.RTL_VIRTUAL_UNWIND_HANDLER_TYPE, ImageBase: UInt64, ControlPc: UInt64, FunctionEntry: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_RUNTIME_FUNCTION_ENTRY), ContextRecord: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT), HandlerData: POINTER(VoidPtr), EstablisherFrame: POINTER(UInt64), ContextPointers: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.KNONVOLATILE_CONTEXT_POINTERS)) -> win32more.Windows.Win32.System.Kernel.EXCEPTION_ROUTINE: ...
@winfunctype('KERNEL32.dll')
def ReadProcessMemory(hProcess: win32more.Windows.Win32.Foundation.HANDLE, lpBaseAddress: VoidPtr, lpBuffer: VoidPtr, nSize: UIntPtr, lpNumberOfBytesRead: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WriteProcessMemory(hProcess: win32more.Windows.Win32.Foundation.HANDLE, lpBaseAddress: VoidPtr, lpBuffer: VoidPtr, nSize: UIntPtr, lpNumberOfBytesWritten: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetThreadContext(hThread: win32more.Windows.Win32.Foundation.HANDLE, lpContext: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetThreadContext(hThread: win32more.Windows.Win32.Foundation.HANDLE, lpContext: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FlushInstructionCache(hProcess: win32more.Windows.Win32.Foundation.HANDLE, lpBaseAddress: VoidPtr, dwSize: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def Wow64GetThreadContext(hThread: win32more.Windows.Win32.Foundation.HANDLE, lpContext: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.WOW64_CONTEXT)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def Wow64SetThreadContext(hThread: win32more.Windows.Win32.Foundation.HANDLE, lpContext: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.WOW64_CONTEXT)) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X64':
    @winfunctype('KERNEL32.dll')
    def RtlCaptureContext2(ContextRecord: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT)) -> Void: ...
if ARCH in 'X64,ARM64':
    @winfunctype('ntdll.dll')
    def RtlGrowFunctionTable(DynamicTable: VoidPtr, NewEntryCount: UInt32) -> Void: ...
if ARCH in 'X64,ARM64':
    @winfunctype('ntdll.dll')
    def RtlDeleteGrowableFunctionTable(DynamicTable: VoidPtr) -> Void: ...
if ARCH in 'X64,ARM64':
    @winfunctype('KERNEL32.dll')
    def RtlUnwindEx(TargetFrame: VoidPtr, TargetIp: VoidPtr, ExceptionRecord: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.EXCEPTION_RECORD), ReturnValue: VoidPtr, ContextRecord: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT), HistoryTable: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.UNWIND_HISTORY_TABLE)) -> Void: ...
if ARCH in 'X64,ARM64':
    @winfunctype('imagehlp.dll')
    def CheckSumMappedFile(BaseAddress: VoidPtr, FileLength: UInt32, HeaderSum: POINTER(UInt32), CheckSum: POINTER(UInt32)) -> POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_NT_HEADERS64): ...
elif ARCH in 'X86':
    @winfunctype('imagehlp.dll')
    def CheckSumMappedFile(BaseAddress: VoidPtr, FileLength: UInt32, HeaderSum: POINTER(UInt32), CheckSum: POINTER(UInt32)) -> POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_NT_HEADERS32): ...
if ARCH in 'X64,ARM64':
    @winfunctype('imagehlp.dll')
    def GetImageConfigInformation(LoadedImage: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.LOADED_IMAGE), ImageConfigInformation: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_LOAD_CONFIG_DIRECTORY64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
elif ARCH in 'X86':
    @winfunctype('imagehlp.dll')
    def GetImageConfigInformation(LoadedImage: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.LOADED_IMAGE), ImageConfigInformation: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_LOAD_CONFIG_DIRECTORY32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X64,ARM64':
    @winfunctype('imagehlp.dll')
    def SetImageConfigInformation(LoadedImage: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.LOADED_IMAGE), ImageConfigInformation: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_LOAD_CONFIG_DIRECTORY64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
elif ARCH in 'X86':
    @winfunctype('imagehlp.dll')
    def SetImageConfigInformation(LoadedImage: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.LOADED_IMAGE), ImageConfigInformation: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_LOAD_CONFIG_DIRECTORY32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X64,ARM64':
    @winfunctype('dbghelp.dll')
    def ImageNtHeader(Base: VoidPtr) -> POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_NT_HEADERS64): ...
elif ARCH in 'X86':
    @winfunctype('dbghelp.dll')
    def ImageNtHeader(Base: VoidPtr) -> POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_NT_HEADERS32): ...
if ARCH in 'X64,ARM64':
    @winfunctype('dbghelp.dll')
    def ImageRvaToSection(NtHeaders: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_NT_HEADERS64), Base: VoidPtr, Rva: UInt32) -> POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_HEADER): ...
elif ARCH in 'X86':
    @winfunctype('dbghelp.dll')
    def ImageRvaToSection(NtHeaders: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_NT_HEADERS32), Base: VoidPtr, Rva: UInt32) -> POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_HEADER): ...
if ARCH in 'X64,ARM64':
    @winfunctype('dbghelp.dll')
    def ImageRvaToVa(NtHeaders: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_NT_HEADERS64), Base: VoidPtr, Rva: UInt32, LastRvaSection: POINTER(POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_HEADER))) -> VoidPtr: ...
elif ARCH in 'X86':
    @winfunctype('dbghelp.dll')
    def ImageRvaToVa(NtHeaders: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_NT_HEADERS32), Base: VoidPtr, Rva: UInt32, LastRvaSection: POINTER(POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_HEADER))) -> VoidPtr: ...
@winfunctype('KERNEL32.dll')
def RtlCaptureStackBackTrace(FramesToSkip: UInt32, FramesToCapture: UInt32, BackTrace: POINTER(VoidPtr), BackTraceHash: POINTER(UInt32)) -> UInt16: ...
@winfunctype('KERNEL32.dll')
def RtlCaptureContext(ContextRecord: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT)) -> Void: ...
@winfunctype('KERNEL32.dll')
def RtlUnwind(TargetFrame: VoidPtr, TargetIp: VoidPtr, ExceptionRecord: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.EXCEPTION_RECORD), ReturnValue: VoidPtr) -> Void: ...
@cfunctype('KERNEL32.dll')
def RtlRestoreContext(ContextRecord: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT), ExceptionRecord: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.EXCEPTION_RECORD)) -> Void: ...
@winfunctype('KERNEL32.dll')
def RtlRaiseException(ExceptionRecord: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.EXCEPTION_RECORD)) -> Void: ...
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
OutputDebugString = UnicodeAlias('OutputDebugStringW')
@winfunctype('KERNEL32.dll')
def ContinueDebugEvent(dwProcessId: UInt32, dwThreadId: UInt32, dwContinueStatus: win32more.Windows.Win32.Foundation.NTSTATUS) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WaitForDebugEvent(lpDebugEvent: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.DEBUG_EVENT), dwMilliseconds: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DebugActiveProcess(dwProcessId: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DebugActiveProcessStop(dwProcessId: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CheckRemoteDebuggerPresent(hProcess: win32more.Windows.Win32.Foundation.HANDLE, pbDebuggerPresent: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WaitForDebugEventEx(lpDebugEvent: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.DEBUG_EVENT), dwMilliseconds: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
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
def UnhandledExceptionFilter(ExceptionInfo: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.EXCEPTION_POINTERS)) -> Int32: ...
@winfunctype('KERNEL32.dll')
def SetUnhandledExceptionFilter(lpTopLevelExceptionFilter: win32more.Windows.Win32.System.Diagnostics.Debug.LPTOP_LEVEL_EXCEPTION_FILTER) -> win32more.Windows.Win32.System.Diagnostics.Debug.LPTOP_LEVEL_EXCEPTION_FILTER: ...
@winfunctype('KERNEL32.dll')
def GetErrorMode() -> UInt32: ...
@winfunctype('KERNEL32.dll')
def SetErrorMode(uMode: win32more.Windows.Win32.System.Diagnostics.Debug.THREAD_ERROR_MODE) -> win32more.Windows.Win32.System.Diagnostics.Debug.THREAD_ERROR_MODE: ...
@winfunctype('KERNEL32.dll')
def AddVectoredExceptionHandler(First: UInt32, Handler: win32more.Windows.Win32.System.Diagnostics.Debug.PVECTORED_EXCEPTION_HANDLER) -> VoidPtr: ...
@winfunctype('KERNEL32.dll')
def RemoveVectoredExceptionHandler(Handle: VoidPtr) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def AddVectoredContinueHandler(First: UInt32, Handler: win32more.Windows.Win32.System.Diagnostics.Debug.PVECTORED_EXCEPTION_HANDLER) -> VoidPtr: ...
@winfunctype('KERNEL32.dll')
def RemoveVectoredContinueHandler(Handle: VoidPtr) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def RaiseFailFastException(pExceptionRecord: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.EXCEPTION_RECORD), pContextRecord: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT), dwFlags: UInt32) -> Void: ...
@winfunctype('KERNEL32.dll')
def FatalAppExitA(uAction: UInt32, lpMessageText: win32more.Windows.Win32.Foundation.PSTR) -> Void: ...
@winfunctype('KERNEL32.dll')
def FatalAppExitW(uAction: UInt32, lpMessageText: win32more.Windows.Win32.Foundation.PWSTR) -> Void: ...
FatalAppExit = UnicodeAlias('FatalAppExitW')
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
def GetThreadWaitChain(WctHandle: VoidPtr, Context: UIntPtr, Flags: win32more.Windows.Win32.System.Diagnostics.Debug.WAIT_CHAIN_THREAD_OPTIONS, ThreadId: UInt32, NodeCount: POINTER(UInt32), NodeInfoArray: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.WAITCHAIN_NODE_INFO), IsCycle: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def RegisterWaitChainCOMCallback(CallStateCallback: win32more.Windows.Win32.System.Diagnostics.Debug.PCOGETCALLSTATE, ActivationStateCallback: win32more.Windows.Win32.System.Diagnostics.Debug.PCOGETACTIVATIONSTATE) -> Void: ...
@winfunctype('dbghelp.dll')
def MiniDumpWriteDump(hProcess: win32more.Windows.Win32.Foundation.HANDLE, ProcessId: UInt32, hFile: win32more.Windows.Win32.Foundation.HANDLE, DumpType: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_TYPE, ExceptionParam: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_EXCEPTION_INFORMATION), UserStreamParam: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_USER_STREAM_INFORMATION), CallbackParam: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_CALLBACK_INFORMATION)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def MiniDumpReadDumpStream(BaseOfDump: VoidPtr, StreamNumber: UInt32, Dir: POINTER(POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_DIRECTORY)), StreamPointer: POINTER(VoidPtr), StreamSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('imagehlp.dll')
def BindImage(ImageName: win32more.Windows.Win32.Foundation.PSTR, DllPath: win32more.Windows.Win32.Foundation.PSTR, SymbolPath: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('imagehlp.dll')
def BindImageEx(Flags: UInt32, ImageName: win32more.Windows.Win32.Foundation.PSTR, DllPath: win32more.Windows.Win32.Foundation.PSTR, SymbolPath: win32more.Windows.Win32.Foundation.PSTR, StatusRoutine: win32more.Windows.Win32.System.Diagnostics.Debug.PIMAGEHLP_STATUS_ROUTINE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('imagehlp.dll')
def ReBaseImage(CurrentImageName: win32more.Windows.Win32.Foundation.PSTR, SymbolPath: win32more.Windows.Win32.Foundation.PSTR, fReBase: win32more.Windows.Win32.Foundation.BOOL, fRebaseSysfileOk: win32more.Windows.Win32.Foundation.BOOL, fGoingDown: win32more.Windows.Win32.Foundation.BOOL, CheckImageSize: UInt32, OldImageSize: POINTER(UInt32), OldImageBase: POINTER(UIntPtr), NewImageSize: POINTER(UInt32), NewImageBase: POINTER(UIntPtr), TimeStamp: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('imagehlp.dll')
def ReBaseImage64(CurrentImageName: win32more.Windows.Win32.Foundation.PSTR, SymbolPath: win32more.Windows.Win32.Foundation.PSTR, fReBase: win32more.Windows.Win32.Foundation.BOOL, fRebaseSysfileOk: win32more.Windows.Win32.Foundation.BOOL, fGoingDown: win32more.Windows.Win32.Foundation.BOOL, CheckImageSize: UInt32, OldImageSize: POINTER(UInt32), OldImageBase: POINTER(UInt64), NewImageSize: POINTER(UInt32), NewImageBase: POINTER(UInt64), TimeStamp: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('imagehlp.dll')
def MapFileAndCheckSumA(Filename: win32more.Windows.Win32.Foundation.PSTR, HeaderSum: POINTER(UInt32), CheckSum: POINTER(UInt32)) -> UInt32: ...
@winfunctype('imagehlp.dll')
def MapFileAndCheckSumW(Filename: win32more.Windows.Win32.Foundation.PWSTR, HeaderSum: POINTER(UInt32), CheckSum: POINTER(UInt32)) -> UInt32: ...
MapFileAndCheckSum = UnicodeAlias('MapFileAndCheckSumW')
@winfunctype('imagehlp.dll')
def GetImageUnusedHeaderBytes(LoadedImage: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.LOADED_IMAGE), SizeUnusedHeaderBytes: POINTER(UInt32)) -> UInt32: ...
@winfunctype('imagehlp.dll')
def ImageGetDigestStream(FileHandle: win32more.Windows.Win32.Foundation.HANDLE, DigestLevel: UInt32, DigestFunction: win32more.Windows.Win32.System.Diagnostics.Debug.DIGEST_FUNCTION, DigestHandle: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('imagehlp.dll')
def ImageAddCertificate(FileHandle: win32more.Windows.Win32.Foundation.HANDLE, Certificate: POINTER(win32more.Windows.Win32.Security.WinTrust.WIN_CERTIFICATE), Index: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('imagehlp.dll')
def ImageRemoveCertificate(FileHandle: win32more.Windows.Win32.Foundation.HANDLE, Index: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('imagehlp.dll')
def ImageEnumerateCertificates(FileHandle: win32more.Windows.Win32.Foundation.HANDLE, TypeFilter: UInt16, CertificateCount: POINTER(UInt32), Indices: POINTER(UInt32), IndexCount: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('imagehlp.dll')
def ImageGetCertificateData(FileHandle: win32more.Windows.Win32.Foundation.HANDLE, CertificateIndex: UInt32, Certificate: POINTER(win32more.Windows.Win32.Security.WinTrust.WIN_CERTIFICATE), RequiredLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('imagehlp.dll')
def ImageGetCertificateHeader(FileHandle: win32more.Windows.Win32.Foundation.HANDLE, CertificateIndex: UInt32, Certificateheader: POINTER(win32more.Windows.Win32.Security.WinTrust.WIN_CERTIFICATE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('imagehlp.dll')
def ImageLoad(DllName: win32more.Windows.Win32.Foundation.PSTR, DllPath: win32more.Windows.Win32.Foundation.PSTR) -> POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.LOADED_IMAGE): ...
@winfunctype('imagehlp.dll')
def ImageUnload(LoadedImage: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.LOADED_IMAGE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('imagehlp.dll')
def MapAndLoad(ImageName: win32more.Windows.Win32.Foundation.PSTR, DllPath: win32more.Windows.Win32.Foundation.PSTR, LoadedImage: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.LOADED_IMAGE), DotDll: win32more.Windows.Win32.Foundation.BOOL, ReadOnly: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('imagehlp.dll')
def UnMapAndLoad(LoadedImage: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.LOADED_IMAGE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('imagehlp.dll')
def TouchFileTimes(FileHandle: win32more.Windows.Win32.Foundation.HANDLE, pSystemTime: POINTER(win32more.Windows.Win32.Foundation.SYSTEMTIME)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('imagehlp.dll')
def UpdateDebugInfoFile(ImageFileName: win32more.Windows.Win32.Foundation.PSTR, SymbolPath: win32more.Windows.Win32.Foundation.PSTR, DebugFilePath: win32more.Windows.Win32.Foundation.PSTR, NtHeaders: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_NT_HEADERS32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('imagehlp.dll')
def UpdateDebugInfoFileEx(ImageFileName: win32more.Windows.Win32.Foundation.PSTR, SymbolPath: win32more.Windows.Win32.Foundation.PSTR, DebugFilePath: win32more.Windows.Win32.Foundation.PSTR, NtHeaders: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_NT_HEADERS32), OldCheckSum: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymFindDebugInfoFileW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, FileName: win32more.Windows.Win32.Foundation.PWSTR, DebugFilePath: win32more.Windows.Win32.Foundation.PWSTR, Callback: win32more.Windows.Win32.System.Diagnostics.Debug.PFIND_DEBUG_FILE_CALLBACKW, CallerData: VoidPtr) -> win32more.Windows.Win32.Foundation.HANDLE: ...
SymFindDebugInfoFile = UnicodeAlias('SymFindDebugInfoFileW')
@winfunctype('dbghelp.dll')
def FindDebugInfoFile(FileName: win32more.Windows.Win32.Foundation.PSTR, SymbolPath: win32more.Windows.Win32.Foundation.PSTR, DebugFilePath: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('dbghelp.dll')
def FindDebugInfoFileExW(FileName: win32more.Windows.Win32.Foundation.PWSTR, SymbolPath: win32more.Windows.Win32.Foundation.PWSTR, DebugFilePath: win32more.Windows.Win32.Foundation.PWSTR, Callback: win32more.Windows.Win32.System.Diagnostics.Debug.PFIND_DEBUG_FILE_CALLBACKW, CallerData: VoidPtr) -> win32more.Windows.Win32.Foundation.HANDLE: ...
FindDebugInfoFileEx = UnicodeAlias('FindDebugInfoFileExW')
@winfunctype('dbghelp.dll')
def SymFindFileInPathW(hprocess: win32more.Windows.Win32.Foundation.HANDLE, SearchPathA: win32more.Windows.Win32.Foundation.PWSTR, FileName: win32more.Windows.Win32.Foundation.PWSTR, id: VoidPtr, two: UInt32, three: UInt32, flags: win32more.Windows.Win32.System.Diagnostics.Debug.SYM_FIND_ID_OPTION, FoundFile: win32more.Windows.Win32.Foundation.PWSTR, callback: win32more.Windows.Win32.System.Diagnostics.Debug.PFINDFILEINPATHCALLBACKW, context: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
SymFindFileInPath = UnicodeAlias('SymFindFileInPathW')
@winfunctype('dbghelp.dll')
def SymFindExecutableImageW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, FileName: win32more.Windows.Win32.Foundation.PWSTR, ImageFilePath: win32more.Windows.Win32.Foundation.PWSTR, Callback: win32more.Windows.Win32.System.Diagnostics.Debug.PFIND_EXE_FILE_CALLBACKW, CallerData: VoidPtr) -> win32more.Windows.Win32.Foundation.HANDLE: ...
SymFindExecutableImage = UnicodeAlias('SymFindExecutableImageW')
@winfunctype('dbghelp.dll')
def FindExecutableImage(FileName: win32more.Windows.Win32.Foundation.PSTR, SymbolPath: win32more.Windows.Win32.Foundation.PSTR, ImageFilePath: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('dbghelp.dll')
def FindExecutableImageExW(FileName: win32more.Windows.Win32.Foundation.PWSTR, SymbolPath: win32more.Windows.Win32.Foundation.PWSTR, ImageFilePath: win32more.Windows.Win32.Foundation.PWSTR, Callback: win32more.Windows.Win32.System.Diagnostics.Debug.PFIND_EXE_FILE_CALLBACKW, CallerData: VoidPtr) -> win32more.Windows.Win32.Foundation.HANDLE: ...
FindExecutableImageEx = UnicodeAlias('FindExecutableImageExW')
@winfunctype('dbghelp.dll')
def ImageDirectoryEntryToDataEx(Base: VoidPtr, MappedAsImage: win32more.Windows.Win32.Foundation.BOOLEAN, DirectoryEntry: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DIRECTORY_ENTRY, Size: POINTER(UInt32), FoundHeader: POINTER(POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_HEADER))) -> VoidPtr: ...
@winfunctype('dbghelp.dll')
def ImageDirectoryEntryToData(Base: VoidPtr, MappedAsImage: win32more.Windows.Win32.Foundation.BOOLEAN, DirectoryEntry: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DIRECTORY_ENTRY, Size: POINTER(UInt32)) -> VoidPtr: ...
@winfunctype('dbghelp.dll')
def SearchTreeForFileW(RootPath: win32more.Windows.Win32.Foundation.PWSTR, InputPathName: win32more.Windows.Win32.Foundation.PWSTR, OutputPathBuffer: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
SearchTreeForFile = UnicodeAlias('SearchTreeForFileW')
@winfunctype('dbghelp.dll')
def EnumDirTreeW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, RootPath: win32more.Windows.Win32.Foundation.PWSTR, InputPathName: win32more.Windows.Win32.Foundation.PWSTR, OutputPathBuffer: win32more.Windows.Win32.Foundation.PWSTR, cb: win32more.Windows.Win32.System.Diagnostics.Debug.PENUMDIRTREE_CALLBACKW, data: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
EnumDirTree = UnicodeAlias('EnumDirTreeW')
@winfunctype('dbghelp.dll')
def MakeSureDirectoryPathExists(DirPath: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def UnDecorateSymbolNameW(name: win32more.Windows.Win32.Foundation.PWSTR, outputString: win32more.Windows.Win32.Foundation.PWSTR, maxStringLength: UInt32, flags: UInt32) -> UInt32: ...
UnDecorateSymbolName = UnicodeAlias('UnDecorateSymbolNameW')
@winfunctype('dbghelp.dll')
def StackWalk64(MachineType: UInt32, hProcess: win32more.Windows.Win32.Foundation.HANDLE, hThread: win32more.Windows.Win32.Foundation.HANDLE, StackFrame: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.STACKFRAME64), ContextRecord: VoidPtr, ReadMemoryRoutine: win32more.Windows.Win32.System.Diagnostics.Debug.PREAD_PROCESS_MEMORY_ROUTINE64, FunctionTableAccessRoutine: win32more.Windows.Win32.System.Diagnostics.Debug.PFUNCTION_TABLE_ACCESS_ROUTINE64, GetModuleBaseRoutine: win32more.Windows.Win32.System.Diagnostics.Debug.PGET_MODULE_BASE_ROUTINE64, TranslateAddress: win32more.Windows.Win32.System.Diagnostics.Debug.PTRANSLATE_ADDRESS_ROUTINE64) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def StackWalkEx(MachineType: UInt32, hProcess: win32more.Windows.Win32.Foundation.HANDLE, hThread: win32more.Windows.Win32.Foundation.HANDLE, StackFrame: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.STACKFRAME_EX), ContextRecord: VoidPtr, ReadMemoryRoutine: win32more.Windows.Win32.System.Diagnostics.Debug.PREAD_PROCESS_MEMORY_ROUTINE64, FunctionTableAccessRoutine: win32more.Windows.Win32.System.Diagnostics.Debug.PFUNCTION_TABLE_ACCESS_ROUTINE64, GetModuleBaseRoutine: win32more.Windows.Win32.System.Diagnostics.Debug.PGET_MODULE_BASE_ROUTINE64, TranslateAddress: win32more.Windows.Win32.System.Diagnostics.Debug.PTRANSLATE_ADDRESS_ROUTINE64, Flags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def StackWalk2(MachineType: UInt32, hProcess: win32more.Windows.Win32.Foundation.HANDLE, hThread: win32more.Windows.Win32.Foundation.HANDLE, StackFrame: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.STACKFRAME_EX), ContextRecord: VoidPtr, ReadMemoryRoutine: win32more.Windows.Win32.System.Diagnostics.Debug.PREAD_PROCESS_MEMORY_ROUTINE64, FunctionTableAccessRoutine: win32more.Windows.Win32.System.Diagnostics.Debug.PFUNCTION_TABLE_ACCESS_ROUTINE64, GetModuleBaseRoutine: win32more.Windows.Win32.System.Diagnostics.Debug.PGET_MODULE_BASE_ROUTINE64, TranslateAddress: win32more.Windows.Win32.System.Diagnostics.Debug.PTRANSLATE_ADDRESS_ROUTINE64, GetTargetAttributeValue: win32more.Windows.Win32.System.Diagnostics.Debug.PGET_TARGET_ATTRIBUTE_VALUE64, Flags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X86':
    @winfunctype('dbghelp.dll')
    def StackWalk(MachineType: UInt32, hProcess: win32more.Windows.Win32.Foundation.HANDLE, hThread: win32more.Windows.Win32.Foundation.HANDLE, StackFrame: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.STACKFRAME), ContextRecord: VoidPtr, ReadMemoryRoutine: win32more.Windows.Win32.System.Diagnostics.Debug.PREAD_PROCESS_MEMORY_ROUTINE, FunctionTableAccessRoutine: win32more.Windows.Win32.System.Diagnostics.Debug.PFUNCTION_TABLE_ACCESS_ROUTINE, GetModuleBaseRoutine: win32more.Windows.Win32.System.Diagnostics.Debug.PGET_MODULE_BASE_ROUTINE, TranslateAddress: win32more.Windows.Win32.System.Diagnostics.Debug.PTRANSLATE_ADDRESS_ROUTINE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def ImagehlpApiVersion() -> POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.API_VERSION): ...
@winfunctype('dbghelp.dll')
def ImagehlpApiVersionEx(AppVersion: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.API_VERSION)) -> POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.API_VERSION): ...
@winfunctype('dbghelp.dll')
def GetTimestampForLoadedLibrary(Module: win32more.Windows.Win32.Foundation.HMODULE) -> UInt32: ...
@winfunctype('dbghelp.dll')
def SymSetParentWindow(hwnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymSetHomeDirectoryW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, dir: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.PWSTR: ...
SymSetHomeDirectory = UnicodeAlias('SymSetHomeDirectoryW')
@winfunctype('dbghelp.dll')
def SymGetHomeDirectoryW(type: UInt32, dir: win32more.Windows.Win32.Foundation.PWSTR, size: UIntPtr) -> win32more.Windows.Win32.Foundation.PWSTR: ...
SymGetHomeDirectory = UnicodeAlias('SymGetHomeDirectoryW')
@winfunctype('dbghelp.dll')
def SymGetOmaps(hProcess: win32more.Windows.Win32.Foundation.HANDLE, BaseOfDll: UInt64, OmapTo: POINTER(POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.OMAP)), cOmapTo: POINTER(UInt64), OmapFrom: POINTER(POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.OMAP)), cOmapFrom: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
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
def SymMatchStringA(string: win32more.Windows.Win32.Foundation.PSTR, expression: win32more.Windows.Win32.Foundation.PSTR, fCase: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymMatchStringW(string: win32more.Windows.Win32.Foundation.PWSTR, expression: win32more.Windows.Win32.Foundation.PWSTR, fCase: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
SymMatchString = UnicodeAlias('SymMatchStringW')
@winfunctype('dbghelp.dll')
def SymEnumSourceFilesW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, ModBase: UInt64, Mask: win32more.Windows.Win32.Foundation.PWSTR, cbSrcFiles: win32more.Windows.Win32.System.Diagnostics.Debug.PSYM_ENUMSOURCEFILES_CALLBACKW, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
SymEnumSourceFiles = UnicodeAlias('SymEnumSourceFilesW')
@winfunctype('dbghelp.dll')
def SymEnumerateModules64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, EnumModulesCallback: win32more.Windows.Win32.System.Diagnostics.Debug.PSYM_ENUMMODULES_CALLBACK64, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymEnumerateModulesW64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, EnumModulesCallback: win32more.Windows.Win32.System.Diagnostics.Debug.PSYM_ENUMMODULES_CALLBACKW64, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X86':
    @winfunctype('dbghelp.dll')
    def SymEnumerateModules(hProcess: win32more.Windows.Win32.Foundation.HANDLE, EnumModulesCallback: win32more.Windows.Win32.System.Diagnostics.Debug.PSYM_ENUMMODULES_CALLBACK, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def EnumerateLoadedModulesExW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, EnumLoadedModulesCallback: win32more.Windows.Win32.System.Diagnostics.Debug.PENUMLOADED_MODULES_CALLBACKW64, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
EnumerateLoadedModulesEx = UnicodeAlias('EnumerateLoadedModulesExW')
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
def SymGetModuleInfo64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, qwAddr: UInt64, ModuleInfo: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_MODULE64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetModuleInfoW64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, qwAddr: UInt64, ModuleInfo: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_MODULEW64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X86':
    @winfunctype('dbghelp.dll')
    def SymGetModuleInfoW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, dwAddr: UInt32, ModuleInfo: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_MODULEW)) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X86':
    SymGetModuleInfo = UnicodeAlias('SymGetModuleInfoW')
@winfunctype('dbghelp.dll')
def SymGetModuleBase64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, qwAddr: UInt64) -> UInt64: ...
if ARCH in 'X86':
    @winfunctype('dbghelp.dll')
    def SymGetModuleBase(hProcess: win32more.Windows.Win32.Foundation.HANDLE, dwAddr: UInt32) -> UInt32: ...
@winfunctype('dbghelp.dll')
def SymEnumLinesW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Base: UInt64, Obj: win32more.Windows.Win32.Foundation.PWSTR, File: win32more.Windows.Win32.Foundation.PWSTR, EnumLinesCallback: win32more.Windows.Win32.System.Diagnostics.Debug.PSYM_ENUMLINES_CALLBACKW, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
SymEnumLines = UnicodeAlias('SymEnumLinesW')
@winfunctype('dbghelp.dll')
def SymGetLineFromAddr64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, qwAddr: UInt64, pdwDisplacement: POINTER(UInt32), Line64: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_LINE64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetLineFromAddrW64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, dwAddr: UInt64, pdwDisplacement: POINTER(UInt32), Line: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_LINEW64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetLineFromInlineContextW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, dwAddr: UInt64, InlineContext: UInt32, qwModuleBaseAddress: UInt64, pdwDisplacement: POINTER(UInt32), Line: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_LINEW64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
SymGetLineFromInlineContext = UnicodeAlias('SymGetLineFromInlineContextW')
@winfunctype('dbghelp.dll')
def SymEnumSourceLinesW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Base: UInt64, Obj: win32more.Windows.Win32.Foundation.PWSTR, File: win32more.Windows.Win32.Foundation.PWSTR, Line: UInt32, Flags: UInt32, EnumLinesCallback: win32more.Windows.Win32.System.Diagnostics.Debug.PSYM_ENUMLINES_CALLBACKW, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
SymEnumSourceLines = UnicodeAlias('SymEnumSourceLinesW')
@winfunctype('dbghelp.dll')
def SymAddrIncludeInlineTrace(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Address: UInt64) -> UInt32: ...
@winfunctype('dbghelp.dll')
def SymCompareInlineTrace(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Address1: UInt64, InlineContext1: UInt32, RetAddress1: UInt64, Address2: UInt64, RetAddress2: UInt64) -> UInt32: ...
@winfunctype('dbghelp.dll')
def SymQueryInlineTrace(hProcess: win32more.Windows.Win32.Foundation.HANDLE, StartAddress: UInt64, StartContext: UInt32, StartRetAddress: UInt64, CurAddress: UInt64, CurContext: POINTER(UInt32), CurFrameIndex: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X86':
    @winfunctype('dbghelp.dll')
    def SymGetLineFromAddr(hProcess: win32more.Windows.Win32.Foundation.HANDLE, dwAddr: UInt32, pdwDisplacement: POINTER(UInt32), Line: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_LINE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetLineFromName64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, ModuleName: win32more.Windows.Win32.Foundation.PSTR, FileName: win32more.Windows.Win32.Foundation.PSTR, dwLineNumber: UInt32, plDisplacement: POINTER(Int32), Line: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_LINE64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetLineFromNameW64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, ModuleName: win32more.Windows.Win32.Foundation.PWSTR, FileName: win32more.Windows.Win32.Foundation.PWSTR, dwLineNumber: UInt32, plDisplacement: POINTER(Int32), Line: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_LINEW64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X86':
    @winfunctype('dbghelp.dll')
    def SymGetLineFromName(hProcess: win32more.Windows.Win32.Foundation.HANDLE, ModuleName: win32more.Windows.Win32.Foundation.PSTR, FileName: win32more.Windows.Win32.Foundation.PSTR, dwLineNumber: UInt32, plDisplacement: POINTER(Int32), Line: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_LINE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetLineNext64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Line: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_LINE64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetLineNextW64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Line: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_LINEW64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X86':
    @winfunctype('dbghelp.dll')
    def SymGetLineNext(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Line: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_LINE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetLinePrev64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Line: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_LINE64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetLinePrevW64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Line: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_LINEW64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X86':
    @winfunctype('dbghelp.dll')
    def SymGetLinePrev(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Line: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_LINE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetFileLineOffsets64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, ModuleName: win32more.Windows.Win32.Foundation.PSTR, FileName: win32more.Windows.Win32.Foundation.PSTR, Buffer: POINTER(UInt64), BufferLines: UInt32) -> UInt32: ...
@winfunctype('dbghelp.dll')
def SymMatchFileNameW(FileName: win32more.Windows.Win32.Foundation.PWSTR, Match: win32more.Windows.Win32.Foundation.PWSTR, FileNameStop: POINTER(win32more.Windows.Win32.Foundation.PWSTR), MatchStop: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.BOOL: ...
SymMatchFileName = UnicodeAlias('SymMatchFileNameW')
@winfunctype('dbghelp.dll')
def SymGetSourceFileW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Base: UInt64, Params: win32more.Windows.Win32.Foundation.PWSTR, FileSpec: win32more.Windows.Win32.Foundation.PWSTR, FilePath: win32more.Windows.Win32.Foundation.PWSTR, Size: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
SymGetSourceFile = UnicodeAlias('SymGetSourceFileW')
@winfunctype('dbghelp.dll')
def SymGetSourceFileChecksumW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Base: UInt64, FileSpec: win32more.Windows.Win32.Foundation.PWSTR, pCheckSumType: POINTER(UInt32), pChecksum: POINTER(Byte), checksumSize: UInt32, pActualBytesWritten: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
SymGetSourceFileChecksum = UnicodeAlias('SymGetSourceFileChecksumW')
@winfunctype('dbghelp.dll')
def SymGetSourceFileTokenW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Base: UInt64, FileSpec: win32more.Windows.Win32.Foundation.PWSTR, Token: POINTER(VoidPtr), Size: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
SymGetSourceFileToken = UnicodeAlias('SymGetSourceFileTokenW')
@winfunctype('dbghelp.dll')
def SymGetSourceFileTokenByTokenNameW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Base: UInt64, FileSpec: win32more.Windows.Win32.Foundation.PWSTR, TokenName: win32more.Windows.Win32.Foundation.PWSTR, TokenParameters: win32more.Windows.Win32.Foundation.PWSTR, Token: POINTER(VoidPtr), Size: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
SymGetSourceFileTokenByTokenName = UnicodeAlias('SymGetSourceFileTokenByTokenNameW')
@winfunctype('dbghelp.dll')
def SymGetSourceFileFromTokenW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Token: VoidPtr, Params: win32more.Windows.Win32.Foundation.PWSTR, FilePath: win32more.Windows.Win32.Foundation.PWSTR, Size: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
SymGetSourceFileFromToken = UnicodeAlias('SymGetSourceFileFromTokenW')
@winfunctype('dbghelp.dll')
def SymGetSourceFileFromTokenByTokenNameW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Token: VoidPtr, TokenName: win32more.Windows.Win32.Foundation.PWSTR, Params: win32more.Windows.Win32.Foundation.PWSTR, FilePath: win32more.Windows.Win32.Foundation.PWSTR, Size: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
SymGetSourceFileFromTokenByTokenName = UnicodeAlias('SymGetSourceFileFromTokenByTokenNameW')
@winfunctype('dbghelp.dll')
def SymGetSourceVarFromTokenW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Token: VoidPtr, Params: win32more.Windows.Win32.Foundation.PWSTR, VarName: win32more.Windows.Win32.Foundation.PWSTR, Value: win32more.Windows.Win32.Foundation.PWSTR, Size: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
SymGetSourceVarFromToken = UnicodeAlias('SymGetSourceVarFromTokenW')
@winfunctype('dbghelp.dll')
def SymEnumSourceFileTokens(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Base: UInt64, Callback: win32more.Windows.Win32.System.Diagnostics.Debug.PENUMSOURCEFILETOKENSCALLBACK) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymInitializeW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, UserSearchPath: win32more.Windows.Win32.Foundation.PWSTR, fInvadeProcess: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
SymInitialize = UnicodeAlias('SymInitializeW')
@winfunctype('dbghelp.dll')
def SymGetSearchPathW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, SearchPathA: win32more.Windows.Win32.Foundation.PWSTR, SearchPathLength: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
SymGetSearchPath = UnicodeAlias('SymGetSearchPathW')
@winfunctype('dbghelp.dll')
def SymSetSearchPathW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, SearchPathA: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
SymSetSearchPath = UnicodeAlias('SymSetSearchPathW')
@winfunctype('dbghelp.dll')
def SymLoadModuleExW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, hFile: win32more.Windows.Win32.Foundation.HANDLE, ImageName: win32more.Windows.Win32.Foundation.PWSTR, ModuleName: win32more.Windows.Win32.Foundation.PWSTR, BaseOfDll: UInt64, DllSize: UInt32, Data: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.MODLOAD_DATA), Flags: win32more.Windows.Win32.System.Diagnostics.Debug.SYM_LOAD_FLAGS) -> UInt64: ...
SymLoadModuleEx = UnicodeAlias('SymLoadModuleExW')
@winfunctype('dbghelp.dll')
def SymUnloadModule64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, BaseOfDll: UInt64) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X86':
    @winfunctype('dbghelp.dll')
    def SymUnloadModule(hProcess: win32more.Windows.Win32.Foundation.HANDLE, BaseOfDll: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymUnDName64(sym: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL64), UnDecName: win32more.Windows.Win32.Foundation.PSTR, UnDecNameLength: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X86':
    @winfunctype('dbghelp.dll')
    def SymUnDName(sym: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL), UnDecName: win32more.Windows.Win32.Foundation.PSTR, UnDecNameLength: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
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
def SymSetContext(hProcess: win32more.Windows.Win32.Foundation.HANDLE, StackFrame: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_STACK_FRAME), Context: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymSetScopeFromAddr(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Address: UInt64) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymSetScopeFromInlineContext(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Address: UInt64, InlineContext: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymSetScopeFromIndex(hProcess: win32more.Windows.Win32.Foundation.HANDLE, BaseOfDll: UInt64, Index: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymEnumProcesses(EnumProcessesCallback: win32more.Windows.Win32.System.Diagnostics.Debug.PSYM_ENUMPROCESSES_CALLBACK, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymFromAddrW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Address: UInt64, Displacement: POINTER(UInt64), Symbol: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFOW)) -> win32more.Windows.Win32.Foundation.BOOL: ...
SymFromAddr = UnicodeAlias('SymFromAddrW')
@winfunctype('dbghelp.dll')
def SymFromInlineContextW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Address: UInt64, InlineContext: UInt32, Displacement: POINTER(UInt64), Symbol: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFOW)) -> win32more.Windows.Win32.Foundation.BOOL: ...
SymFromInlineContext = UnicodeAlias('SymFromInlineContextW')
@winfunctype('dbghelp.dll')
def SymFromTokenW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Base: UInt64, Token: UInt32, Symbol: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFOW)) -> win32more.Windows.Win32.Foundation.BOOL: ...
SymFromToken = UnicodeAlias('SymFromTokenW')
@winfunctype('dbghelp.dll')
def SymNextW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, siw: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFOW)) -> win32more.Windows.Win32.Foundation.BOOL: ...
SymNext = UnicodeAlias('SymNextW')
@winfunctype('dbghelp.dll')
def SymPrevW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, siw: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFOW)) -> win32more.Windows.Win32.Foundation.BOOL: ...
SymPrev = UnicodeAlias('SymPrevW')
@winfunctype('dbghelp.dll')
def SymFromNameW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Name: win32more.Windows.Win32.Foundation.PWSTR, Symbol: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFOW)) -> win32more.Windows.Win32.Foundation.BOOL: ...
SymFromName = UnicodeAlias('SymFromNameW')
@winfunctype('dbghelp.dll')
def SymEnumSymbolsW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, BaseOfDll: UInt64, Mask: win32more.Windows.Win32.Foundation.PWSTR, EnumSymbolsCallback: win32more.Windows.Win32.System.Diagnostics.Debug.PSYM_ENUMERATESYMBOLS_CALLBACKW, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
SymEnumSymbols = UnicodeAlias('SymEnumSymbolsW')
@winfunctype('dbghelp.dll')
def SymEnumSymbolsExW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, BaseOfDll: UInt64, Mask: win32more.Windows.Win32.Foundation.PWSTR, EnumSymbolsCallback: win32more.Windows.Win32.System.Diagnostics.Debug.PSYM_ENUMERATESYMBOLS_CALLBACKW, UserContext: VoidPtr, Options: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
SymEnumSymbolsEx = UnicodeAlias('SymEnumSymbolsExW')
@winfunctype('dbghelp.dll')
def SymEnumSymbolsForAddrW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Address: UInt64, EnumSymbolsCallback: win32more.Windows.Win32.System.Diagnostics.Debug.PSYM_ENUMERATESYMBOLS_CALLBACKW, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
SymEnumSymbolsForAddr = UnicodeAlias('SymEnumSymbolsForAddrW')
@winfunctype('dbghelp.dll')
def SymSearchW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, BaseOfDll: UInt64, Index: UInt32, SymTag: UInt32, Mask: win32more.Windows.Win32.Foundation.PWSTR, Address: UInt64, EnumSymbolsCallback: win32more.Windows.Win32.System.Diagnostics.Debug.PSYM_ENUMERATESYMBOLS_CALLBACKW, UserContext: VoidPtr, Options: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
SymSearch = UnicodeAlias('SymSearchW')
@winfunctype('dbghelp.dll')
def SymGetScopeW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, BaseOfDll: UInt64, Index: UInt32, Symbol: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFOW)) -> win32more.Windows.Win32.Foundation.BOOL: ...
SymGetScope = UnicodeAlias('SymGetScopeW')
@winfunctype('dbghelp.dll')
def SymFromIndexW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, BaseOfDll: UInt64, Index: UInt32, Symbol: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFOW)) -> win32more.Windows.Win32.Foundation.BOOL: ...
SymFromIndex = UnicodeAlias('SymFromIndexW')
@winfunctype('dbghelp.dll')
def SymGetTypeInfo(hProcess: win32more.Windows.Win32.Foundation.HANDLE, ModBase: UInt64, TypeId: UInt32, GetType: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL_TYPE_INFO, pInfo: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetTypeInfoEx(hProcess: win32more.Windows.Win32.Foundation.HANDLE, ModBase: UInt64, Params: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_GET_TYPE_INFO_PARAMS)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymEnumTypesW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, BaseOfDll: UInt64, EnumSymbolsCallback: win32more.Windows.Win32.System.Diagnostics.Debug.PSYM_ENUMERATESYMBOLS_CALLBACKW, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
SymEnumTypes = UnicodeAlias('SymEnumTypesW')
@winfunctype('dbghelp.dll')
def SymEnumTypesByNameW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, BaseOfDll: UInt64, mask: win32more.Windows.Win32.Foundation.PWSTR, EnumSymbolsCallback: win32more.Windows.Win32.System.Diagnostics.Debug.PSYM_ENUMERATESYMBOLS_CALLBACKW, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
SymEnumTypesByName = UnicodeAlias('SymEnumTypesByNameW')
@winfunctype('dbghelp.dll')
def SymGetTypeFromNameW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, BaseOfDll: UInt64, Name: win32more.Windows.Win32.Foundation.PWSTR, Symbol: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFOW)) -> win32more.Windows.Win32.Foundation.BOOL: ...
SymGetTypeFromName = UnicodeAlias('SymGetTypeFromNameW')
@winfunctype('dbghelp.dll')
def SymAddSymbolW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, BaseOfDll: UInt64, Name: win32more.Windows.Win32.Foundation.PWSTR, Address: UInt64, Size: UInt32, Flags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
SymAddSymbol = UnicodeAlias('SymAddSymbolW')
@winfunctype('dbghelp.dll')
def SymDeleteSymbolW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, BaseOfDll: UInt64, Name: win32more.Windows.Win32.Foundation.PWSTR, Address: UInt64, Flags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
SymDeleteSymbol = UnicodeAlias('SymDeleteSymbolW')
@winfunctype('dbghelp.dll')
def SymRefreshModuleList(hProcess: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymAddSourceStreamA(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Base: UInt64, StreamFile: win32more.Windows.Win32.Foundation.PSTR, Buffer: POINTER(Byte), Size: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymAddSourceStreamW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Base: UInt64, FileSpec: win32more.Windows.Win32.Foundation.PWSTR, Buffer: POINTER(Byte), Size: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
SymAddSourceStream = UnicodeAlias('SymAddSourceStreamW')
@winfunctype('dbghelp.dll')
def SymSrvIsStoreW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, path: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
SymSrvIsStore = UnicodeAlias('SymSrvIsStoreW')
@winfunctype('dbghelp.dll')
def SymSrvDeltaNameW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, SymPath: win32more.Windows.Win32.Foundation.PWSTR, Type: win32more.Windows.Win32.Foundation.PWSTR, File1: win32more.Windows.Win32.Foundation.PWSTR, File2: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.PWSTR: ...
SymSrvDeltaName = UnicodeAlias('SymSrvDeltaNameW')
@winfunctype('dbghelp.dll')
def SymSrvGetSupplementW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, SymPath: win32more.Windows.Win32.Foundation.PWSTR, Node: win32more.Windows.Win32.Foundation.PWSTR, File: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.PWSTR: ...
SymSrvGetSupplement = UnicodeAlias('SymSrvGetSupplementW')
@winfunctype('dbghelp.dll')
def SymSrvGetFileIndexesW(File: win32more.Windows.Win32.Foundation.PWSTR, Id: POINTER(Guid), Val1: POINTER(UInt32), Val2: POINTER(UInt32), Flags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
SymSrvGetFileIndexes = UnicodeAlias('SymSrvGetFileIndexesW')
@winfunctype('dbghelp.dll')
def SymSrvGetFileIndexStringW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, SrvPath: win32more.Windows.Win32.Foundation.PWSTR, File: win32more.Windows.Win32.Foundation.PWSTR, Index: win32more.Windows.Win32.Foundation.PWSTR, Size: UIntPtr, Flags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
SymSrvGetFileIndexString = UnicodeAlias('SymSrvGetFileIndexStringW')
@winfunctype('dbghelp.dll')
def SymSrvGetFileIndexInfoW(File: win32more.Windows.Win32.Foundation.PWSTR, Info: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.SYMSRV_INDEX_INFOW), Flags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
SymSrvGetFileIndexInfo = UnicodeAlias('SymSrvGetFileIndexInfoW')
@winfunctype('dbghelp.dll')
def SymSrvStoreSupplementW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, SymPath: win32more.Windows.Win32.Foundation.PWSTR, Node: win32more.Windows.Win32.Foundation.PWSTR, File: win32more.Windows.Win32.Foundation.PWSTR, Flags: UInt32) -> win32more.Windows.Win32.Foundation.PWSTR: ...
SymSrvStoreSupplement = UnicodeAlias('SymSrvStoreSupplementW')
@winfunctype('dbghelp.dll')
def SymSrvStoreFileW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, SrvPath: win32more.Windows.Win32.Foundation.PWSTR, File: win32more.Windows.Win32.Foundation.PWSTR, Flags: win32more.Windows.Win32.System.Diagnostics.Debug.SYM_SRV_STORE_FILE_FLAGS) -> win32more.Windows.Win32.Foundation.PWSTR: ...
SymSrvStoreFile = UnicodeAlias('SymSrvStoreFileW')
@winfunctype('dbghelp.dll')
def SymGetSymbolFileW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, SymPath: win32more.Windows.Win32.Foundation.PWSTR, ImageFile: win32more.Windows.Win32.Foundation.PWSTR, Type: UInt32, SymbolFile: win32more.Windows.Win32.Foundation.PWSTR, cSymbolFile: UIntPtr, DbgFile: win32more.Windows.Win32.Foundation.PWSTR, cDbgFile: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
SymGetSymbolFile = UnicodeAlias('SymGetSymbolFileW')
@winfunctype('dbghelp.dll')
def DbgHelpCreateUserDumpW(FileName: win32more.Windows.Win32.Foundation.PWSTR, Callback: win32more.Windows.Win32.System.Diagnostics.Debug.PDBGHELP_CREATE_USER_DUMP_CALLBACK, UserData: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
DbgHelpCreateUserDump = UnicodeAlias('DbgHelpCreateUserDumpW')
@winfunctype('dbghelp.dll')
def SymGetSymFromAddr64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, qwAddr: UInt64, pdwDisplacement: POINTER(UInt64), Symbol: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X86':
    @winfunctype('dbghelp.dll')
    def SymGetSymFromAddr(hProcess: win32more.Windows.Win32.Foundation.HANDLE, dwAddr: UInt32, pdwDisplacement: POINTER(UInt32), Symbol: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetSymFromName64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Name: win32more.Windows.Win32.Foundation.PSTR, Symbol: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X86':
    @winfunctype('dbghelp.dll')
    def SymGetSymFromName(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Name: win32more.Windows.Win32.Foundation.PSTR, Symbol: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
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
    def SymEnumerateSymbolsW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, BaseOfDll: UInt32, EnumSymbolsCallback: win32more.Windows.Win32.System.Diagnostics.Debug.PSYM_ENUMSYMBOLS_CALLBACKW, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X86':
    SymEnumerateSymbols = UnicodeAlias('SymEnumerateSymbolsW')
@winfunctype('dbghelp.dll')
def SymLoadModule64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, hFile: win32more.Windows.Win32.Foundation.HANDLE, ImageName: win32more.Windows.Win32.Foundation.PSTR, ModuleName: win32more.Windows.Win32.Foundation.PSTR, BaseOfDll: UInt64, SizeOfDll: UInt32) -> UInt64: ...
if ARCH in 'X86':
    @winfunctype('dbghelp.dll')
    def SymLoadModule(hProcess: win32more.Windows.Win32.Foundation.HANDLE, hFile: win32more.Windows.Win32.Foundation.HANDLE, ImageName: win32more.Windows.Win32.Foundation.PSTR, ModuleName: win32more.Windows.Win32.Foundation.PSTR, BaseOfDll: UInt32, SizeOfDll: UInt32) -> UInt32: ...
@winfunctype('dbghelp.dll')
def SymGetSymNext64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Symbol: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X86':
    @winfunctype('dbghelp.dll')
    def SymGetSymNext(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Symbol: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SymGetSymPrev64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Symbol: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X86':
    @winfunctype('dbghelp.dll')
    def SymGetSymPrev(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Symbol: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dbghelp.dll')
def SetCheckUserInterruptShared(lpStartAddress: win32more.Windows.Win32.System.Diagnostics.Debug.LPCALL_BACK_USER_INTERRUPT_ROUTINE) -> Void: ...
@winfunctype('dbghelp.dll')
def GetSymLoadError() -> UInt32: ...
@winfunctype('dbghelp.dll')
def SetSymLoadError(error: UInt32) -> Void: ...
@winfunctype('dbghelp.dll')
def ReportSymbolLoadSummary(hProcess: win32more.Windows.Win32.Foundation.HANDLE, pLoadModule: win32more.Windows.Win32.Foundation.PWSTR, pSymbolData: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.DBGHELP_DATA_REPORT_STRUCT)) -> win32more.Windows.Win32.Foundation.BOOL: ...
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
def GetThreadSelectorEntry(hThread: win32more.Windows.Win32.Foundation.HANDLE, dwSelector: UInt32, lpSelectorEntry: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.LDT_ENTRY)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def Wow64GetThreadSelectorEntry(hThread: win32more.Windows.Win32.Foundation.HANDLE, dwSelector: UInt32, lpSelectorEntry: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.WOW64_LDT_ENTRY)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DebugSetProcessKillOnExit(KillOnExit: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DebugBreakProcess(Process: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FormatMessageA(dwFlags: win32more.Windows.Win32.System.Diagnostics.Debug.FORMAT_MESSAGE_OPTIONS, lpSource: VoidPtr, dwMessageId: UInt32, dwLanguageId: UInt32, lpBuffer: win32more.Windows.Win32.Foundation.PSTR, nSize: UInt32, Arguments: POINTER(POINTER(SByte))) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def FormatMessageW(dwFlags: win32more.Windows.Win32.System.Diagnostics.Debug.FORMAT_MESSAGE_OPTIONS, lpSource: VoidPtr, dwMessageId: UInt32, dwLanguageId: UInt32, lpBuffer: win32more.Windows.Win32.Foundation.PWSTR, nSize: UInt32, Arguments: POINTER(POINTER(SByte))) -> UInt32: ...
FormatMessage = UnicodeAlias('FormatMessageW')
@winfunctype('KERNEL32.dll')
def CopyContext(Destination: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT), ContextFlags: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS, Source: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def InitializeContext(Buffer: VoidPtr, ContextFlags: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS, Context: POINTER(POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT)), ContextLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def InitializeContext2(Buffer: VoidPtr, ContextFlags: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS, Context: POINTER(POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT)), ContextLength: POINTER(UInt32), XStateCompactionMask: UInt64) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X86,X64':
    @winfunctype('KERNEL32.dll')
    def GetEnabledXStateFeatures() -> UInt64: ...
if ARCH in 'X86,X64':
    @winfunctype('KERNEL32.dll')
    def GetXStateFeaturesMask(Context: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT), FeatureMask: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X86,X64':
    @winfunctype('KERNEL32.dll')
    def LocateXStateFeature(Context: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT), FeatureId: UInt32, Length: POINTER(UInt32)) -> VoidPtr: ...
if ARCH in 'X86,X64':
    @winfunctype('KERNEL32.dll')
    def SetXStateFeaturesMask(Context: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT), FeatureMask: UInt64) -> win32more.Windows.Win32.Foundation.BOOL: ...
BUGCHECK_ERROR = UInt32
HARDWARE_PROFILE_UNDOCKED_STRING: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 1073807361
HARDWARE_PROFILE_DOCKED_STRING: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 1073807362
HARDWARE_PROFILE_UNKNOWN_STRING: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 1073807363
WINDOWS_NT_BANNER: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 1073741950
WINDOWS_NT_CSD_STRING: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 1073741959
WINDOWS_NT_INFO_STRING: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 1073741960
WINDOWS_NT_MP_STRING: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 1073741961
THREAD_TERMINATE_HELD_MUTEX: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 1073741962
WINDOWS_NT_INFO_STRING_PLURAL: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 1073741981
WINDOWS_NT_RC_STRING: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 1073741982
APC_INDEX_MISMATCH: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 1
DEVICE_QUEUE_NOT_BUSY: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 2
INVALID_AFFINITY_SET: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 3
INVALID_DATA_ACCESS_TRAP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 4
INVALID_PROCESS_ATTACH_ATTEMPT: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 5
INVALID_PROCESS_DETACH_ATTEMPT: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 6
INVALID_SOFTWARE_INTERRUPT: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 7
IRQL_NOT_DISPATCH_LEVEL: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 8
IRQL_NOT_GREATER_OR_EQUAL: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 9
IRQL_NOT_LESS_OR_EQUAL: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 10
NO_EXCEPTION_HANDLING_SUPPORT: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 11
MAXIMUM_WAIT_OBJECTS_EXCEEDED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 12
MUTEX_LEVEL_NUMBER_VIOLATION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 13
NO_USER_MODE_CONTEXT: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 14
SPIN_LOCK_ALREADY_OWNED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 15
SPIN_LOCK_NOT_OWNED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 16
THREAD_NOT_MUTEX_OWNER: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 17
TRAP_CAUSE_UNKNOWN: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 18
EMPTY_THREAD_REAPER_LIST: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 19
CREATE_DELETE_LOCK_NOT_LOCKED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 20
LAST_CHANCE_CALLED_FROM_KMODE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 21
CID_HANDLE_CREATION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 22
CID_HANDLE_DELETION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 23
REFERENCE_BY_POINTER: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 24
BAD_POOL_HEADER: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 25
MEMORY_MANAGEMENT: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 26
PFN_SHARE_COUNT: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 27
PFN_REFERENCE_COUNT: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 28
NO_SPIN_LOCK_AVAILABLE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 29
KMODE_EXCEPTION_NOT_HANDLED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 30
SHARED_RESOURCE_CONV_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 31
KERNEL_APC_PENDING_DURING_EXIT: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 32
QUOTA_UNDERFLOW: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 33
FILE_SYSTEM: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 34
FAT_FILE_SYSTEM: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 35
NTFS_FILE_SYSTEM: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 36
NPFS_FILE_SYSTEM: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 37
CDFS_FILE_SYSTEM: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 38
RDR_FILE_SYSTEM: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 39
CORRUPT_ACCESS_TOKEN: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 40
SECURITY_SYSTEM: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 41
INCONSISTENT_IRP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 42
PANIC_STACK_SWITCH: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 43
PORT_DRIVER_INTERNAL: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 44
SCSI_DISK_DRIVER_INTERNAL: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 45
DATA_BUS_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 46
INSTRUCTION_BUS_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 47
SET_OF_INVALID_CONTEXT: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 48
PHASE0_INITIALIZATION_FAILED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 49
PHASE1_INITIALIZATION_FAILED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 50
UNEXPECTED_INITIALIZATION_CALL: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 51
CACHE_MANAGER: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 52
NO_MORE_IRP_STACK_LOCATIONS: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 53
DEVICE_REFERENCE_COUNT_NOT_ZERO: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 54
FLOPPY_INTERNAL_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 55
SERIAL_DRIVER_INTERNAL: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 56
SYSTEM_EXIT_OWNED_MUTEX: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 57
SYSTEM_UNWIND_PREVIOUS_USER: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 58
SYSTEM_SERVICE_EXCEPTION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 59
INTERRUPT_UNWIND_ATTEMPTED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 60
INTERRUPT_EXCEPTION_NOT_HANDLED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 61
MULTIPROCESSOR_CONFIGURATION_NOT_SUPPORTED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 62
NO_MORE_SYSTEM_PTES: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 63
TARGET_MDL_TOO_SMALL: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 64
MUST_SUCCEED_POOL_EMPTY: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 65
ATDISK_DRIVER_INTERNAL: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 66
NO_SUCH_PARTITION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 67
MULTIPLE_IRP_COMPLETE_REQUESTS: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 68
INSUFFICIENT_SYSTEM_MAP_REGS: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 69
DEREF_UNKNOWN_LOGON_SESSION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 70
REF_UNKNOWN_LOGON_SESSION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 71
CANCEL_STATE_IN_COMPLETED_IRP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 72
PAGE_FAULT_WITH_INTERRUPTS_OFF: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 73
IRQL_GT_ZERO_AT_SYSTEM_SERVICE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 74
STREAMS_INTERNAL_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 75
FATAL_UNHANDLED_HARD_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 76
NO_PAGES_AVAILABLE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 77
PFN_LIST_CORRUPT: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 78
NDIS_INTERNAL_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 79
PAGE_FAULT_IN_NONPAGED_AREA: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 80
PAGE_FAULT_IN_NONPAGED_AREA_M: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 268435536
REGISTRY_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 81
MAILSLOT_FILE_SYSTEM: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 82
NO_BOOT_DEVICE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 83
LM_SERVER_INTERNAL_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 84
DATA_COHERENCY_EXCEPTION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 85
INSTRUCTION_COHERENCY_EXCEPTION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 86
XNS_INTERNAL_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 87
VOLMGRX_INTERNAL_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 88
PINBALL_FILE_SYSTEM: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 89
CRITICAL_SERVICE_FAILED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 90
SET_ENV_VAR_FAILED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 91
HAL_INITIALIZATION_FAILED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 92
UNSUPPORTED_PROCESSOR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 93
OBJECT_INITIALIZATION_FAILED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 94
SECURITY_INITIALIZATION_FAILED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 95
PROCESS_INITIALIZATION_FAILED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 96
HAL1_INITIALIZATION_FAILED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 97
OBJECT1_INITIALIZATION_FAILED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 98
SECURITY1_INITIALIZATION_FAILED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 99
SYMBOLIC_INITIALIZATION_FAILED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 100
MEMORY1_INITIALIZATION_FAILED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 101
CACHE_INITIALIZATION_FAILED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 102
CONFIG_INITIALIZATION_FAILED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 103
FILE_INITIALIZATION_FAILED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 104
IO1_INITIALIZATION_FAILED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 105
LPC_INITIALIZATION_FAILED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 106
PROCESS1_INITIALIZATION_FAILED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 107
REFMON_INITIALIZATION_FAILED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 108
SESSION1_INITIALIZATION_FAILED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 109
BOOTPROC_INITIALIZATION_FAILED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 110
VSL_INITIALIZATION_FAILED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 111
SOFT_RESTART_FATAL_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 112
ASSIGN_DRIVE_LETTERS_FAILED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 114
CONFIG_LIST_FAILED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 115
BAD_SYSTEM_CONFIG_INFO: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 116
CANNOT_WRITE_CONFIGURATION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 117
PROCESS_HAS_LOCKED_PAGES: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 118
KERNEL_STACK_INPAGE_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 119
PHASE0_EXCEPTION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 120
MISMATCHED_HAL: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 121
KERNEL_DATA_INPAGE_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 122
INACCESSIBLE_BOOT_DEVICE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 123
BUGCODE_NDIS_DRIVER: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 124
INSTALL_MORE_MEMORY: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 125
SYSTEM_THREAD_EXCEPTION_NOT_HANDLED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 126
SYSTEM_THREAD_EXCEPTION_NOT_HANDLED_M: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 268435582
UNEXPECTED_KERNEL_MODE_TRAP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 127
UNEXPECTED_KERNEL_MODE_TRAP_M: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 268435583
NMI_HARDWARE_FAILURE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 128
SPIN_LOCK_INIT_FAILURE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 129
DFS_FILE_SYSTEM: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 130
OFS_FILE_SYSTEM: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 131
RECOM_DRIVER: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 132
SETUP_FAILURE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 133
AUDIT_FAILURE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 134
MBR_CHECKSUM_MISMATCH: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 139
KERNEL_MODE_EXCEPTION_NOT_HANDLED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 142
KERNEL_MODE_EXCEPTION_NOT_HANDLED_M: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 268435598
PP0_INITIALIZATION_FAILED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 143
PP1_INITIALIZATION_FAILED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 144
WIN32K_INIT_OR_RIT_FAILURE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 145
UP_DRIVER_ON_MP_SYSTEM: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 146
INVALID_KERNEL_HANDLE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 147
KERNEL_STACK_LOCKED_AT_EXIT: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 148
PNP_INTERNAL_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 149
INVALID_WORK_QUEUE_ITEM: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 150
BOUND_IMAGE_UNSUPPORTED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 151
END_OF_NT_EVALUATION_PERIOD: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 152
INVALID_REGION_OR_SEGMENT: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 153
SYSTEM_LICENSE_VIOLATION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 154
UDFS_FILE_SYSTEM: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 155
MACHINE_CHECK_EXCEPTION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 156
USER_MODE_HEALTH_MONITOR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 158
DRIVER_POWER_STATE_FAILURE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 159
INTERNAL_POWER_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 160
PCI_BUS_DRIVER_INTERNAL: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 161
MEMORY_IMAGE_CORRUPT: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 162
ACPI_DRIVER_INTERNAL: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 163
CNSS_FILE_SYSTEM_FILTER: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 164
ACPI_BIOS_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 165
FP_EMULATION_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 166
BAD_EXHANDLE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 167
BOOTING_IN_SAFEMODE_MINIMAL: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 168
BOOTING_IN_SAFEMODE_NETWORK: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 169
BOOTING_IN_SAFEMODE_DSREPAIR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 170
SESSION_HAS_VALID_POOL_ON_EXIT: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 171
HAL_MEMORY_ALLOCATION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 172
VIDEO_DRIVER_DEBUG_REPORT_REQUEST: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 1073741997
BGI_DETECTED_VIOLATION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 177
VIDEO_DRIVER_INIT_FAILURE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 180
BOOTLOG_LOADED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 181
BOOTLOG_NOT_LOADED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 182
BOOTLOG_ENABLED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 183
ATTEMPTED_SWITCH_FROM_DPC: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 184
CHIPSET_DETECTED_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 185
SESSION_HAS_VALID_VIEWS_ON_EXIT: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 186
NETWORK_BOOT_INITIALIZATION_FAILED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 187
NETWORK_BOOT_DUPLICATE_ADDRESS: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 188
INVALID_HIBERNATED_STATE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 189
ATTEMPTED_WRITE_TO_READONLY_MEMORY: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 190
MUTEX_ALREADY_OWNED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 191
PCI_CONFIG_SPACE_ACCESS_FAILURE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 192
SPECIAL_POOL_DETECTED_MEMORY_CORRUPTION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 193
BAD_POOL_CALLER: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 194
SYSTEM_IMAGE_BAD_SIGNATURE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 195
DRIVER_VERIFIER_DETECTED_VIOLATION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 196
DRIVER_CORRUPTED_EXPOOL: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 197
DRIVER_CAUGHT_MODIFYING_FREED_POOL: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 198
TIMER_OR_DPC_INVALID: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 199
IRQL_UNEXPECTED_VALUE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 200
DRIVER_VERIFIER_IOMANAGER_VIOLATION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 201
PNP_DETECTED_FATAL_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 202
DRIVER_LEFT_LOCKED_PAGES_IN_PROCESS: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 203
PAGE_FAULT_IN_FREED_SPECIAL_POOL: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 204
PAGE_FAULT_BEYOND_END_OF_ALLOCATION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 205
DRIVER_UNLOADED_WITHOUT_CANCELLING_PENDING_OPERATIONS: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 206
TERMINAL_SERVER_DRIVER_MADE_INCORRECT_MEMORY_REFERENCE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 207
DRIVER_CORRUPTED_MMPOOL: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 208
DRIVER_IRQL_NOT_LESS_OR_EQUAL: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 209
BUGCODE_ID_DRIVER: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 210
DRIVER_PORTION_MUST_BE_NONPAGED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 211
SYSTEM_SCAN_AT_RAISED_IRQL_CAUGHT_IMPROPER_DRIVER_UNLOAD: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 212
DRIVER_PAGE_FAULT_IN_FREED_SPECIAL_POOL: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 213
DRIVER_PAGE_FAULT_BEYOND_END_OF_ALLOCATION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 214
DRIVER_PAGE_FAULT_BEYOND_END_OF_ALLOCATION_M: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 268435670
DRIVER_UNMAPPING_INVALID_VIEW: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 215
DRIVER_USED_EXCESSIVE_PTES: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 216
LOCKED_PAGES_TRACKER_CORRUPTION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 217
SYSTEM_PTE_MISUSE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 218
DRIVER_CORRUPTED_SYSPTES: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 219
DRIVER_INVALID_STACK_ACCESS: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 220
POOL_CORRUPTION_IN_FILE_AREA: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 222
IMPERSONATING_WORKER_THREAD: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 223
ACPI_BIOS_FATAL_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 224
WORKER_THREAD_RETURNED_AT_BAD_IRQL: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 225
MANUALLY_INITIATED_CRASH: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 226
RESOURCE_NOT_OWNED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 227
WORKER_INVALID: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 228
POWER_FAILURE_SIMULATE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 229
DRIVER_VERIFIER_DMA_VIOLATION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 230
INVALID_FLOATING_POINT_STATE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 231
INVALID_CANCEL_OF_FILE_OPEN: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 232
ACTIVE_EX_WORKER_THREAD_TERMINATION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 233
SAVER_UNSPECIFIED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 61440
SAVER_BLANKSCREEN: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 61442
SAVER_INPUT: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 61443
SAVER_WATCHDOG: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 61444
SAVER_STARTNOTVISIBLE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 61445
SAVER_NAVIGATIONMODEL: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 61446
SAVER_OUTOFMEMORY: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 61447
SAVER_GRAPHICS: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 61448
SAVER_NAVSERVERTIMEOUT: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 61449
SAVER_CHROMEPROCESSCRASH: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 61450
SAVER_NOTIFICATIONDISMISSAL: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 61451
SAVER_SPEECHDISMISSAL: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 61452
SAVER_CALLDISMISSAL: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 61453
SAVER_APPBARDISMISSAL: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 61454
SAVER_RILADAPTATIONCRASH: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 61455
SAVER_APPLISTUNREACHABLE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 61456
SAVER_REPORTNOTIFICATIONFAILURE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 61457
SAVER_UNEXPECTEDSHUTDOWN: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 61458
SAVER_RPCFAILURE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 61459
SAVER_AUXILIARYFULLDUMP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 61460
SAVER_ACCOUNTPROVSVCINITFAILURE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 61461
SAVER_MTBFCOMMANDTIMEOUT: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 789
SAVER_MTBFCOMMANDHANG: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 61697
SAVER_MTBFPASSBUGCHECK: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 61698
SAVER_MTBFIOERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 61699
SAVER_RENDERTHREADHANG: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 61952
SAVER_RENDERMOBILEUIOOM: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 61953
SAVER_DEVICEUPDATEUNSPECIFIED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 62208
SAVER_AUDIODRIVERHANG: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 62464
SAVER_BATTERYPULLOUT: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 62720
SAVER_MEDIACORETESTHANG: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 62976
SAVER_RESOURCEMANAGEMENT: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 63232
SAVER_CAPTURESERVICE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 63488
SAVER_WAITFORSHELLREADY: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 63744
SAVER_NONRESPONSIVEPROCESS: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 404
SAVER_SICKAPPLICATION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 34918
THREAD_STUCK_IN_DEVICE_DRIVER: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 234
THREAD_STUCK_IN_DEVICE_DRIVER_M: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 268435690
DIRTY_MAPPED_PAGES_CONGESTION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 235
SESSION_HAS_VALID_SPECIAL_POOL_ON_EXIT: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 236
UNMOUNTABLE_BOOT_VOLUME: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 237
CRITICAL_PROCESS_DIED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 239
STORAGE_MINIPORT_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 240
SCSI_VERIFIER_DETECTED_VIOLATION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 241
HARDWARE_INTERRUPT_STORM: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 242
DISORDERLY_SHUTDOWN: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 243
CRITICAL_OBJECT_TERMINATION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 244
FLTMGR_FILE_SYSTEM: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 245
PCI_VERIFIER_DETECTED_VIOLATION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 246
DRIVER_OVERRAN_STACK_BUFFER: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 247
RAMDISK_BOOT_INITIALIZATION_FAILED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 248
DRIVER_RETURNED_STATUS_REPARSE_FOR_VOLUME_OPEN: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 249
HTTP_DRIVER_CORRUPTED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 250
RECURSIVE_MACHINE_CHECK: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 251
ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 252
DIRTY_NOWRITE_PAGES_CONGESTION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 253
BUGCODE_USB_DRIVER: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 254
BC_BLUETOOTH_VERIFIER_FAULT: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 3070
BC_BTHMINI_VERIFIER_FAULT: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 3071
RESERVE_QUEUE_OVERFLOW: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 255
LOADER_BLOCK_MISMATCH: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 256
CLOCK_WATCHDOG_TIMEOUT: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 257
DPC_WATCHDOG_TIMEOUT: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 258
MUP_FILE_SYSTEM: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 259
AGP_INVALID_ACCESS: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 260
AGP_GART_CORRUPTION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 261
AGP_ILLEGALLY_REPROGRAMMED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 262
KERNEL_EXPAND_STACK_ACTIVE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 263
THIRD_PARTY_FILE_SYSTEM_FAILURE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 264
CRITICAL_STRUCTURE_CORRUPTION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 265
APP_TAGGING_INITIALIZATION_FAILED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 266
DFSC_FILE_SYSTEM: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 267
FSRTL_EXTRA_CREATE_PARAMETER_VIOLATION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 268
WDF_VIOLATION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 269
VIDEO_MEMORY_MANAGEMENT_INTERNAL: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 270
DRIVER_INVALID_CRUNTIME_PARAMETER: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 272
RECURSIVE_NMI: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 273
MSRPC_STATE_VIOLATION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 274
VIDEO_DXGKRNL_FATAL_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 275
VIDEO_SHADOW_DRIVER_FATAL_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 276
AGP_INTERNAL: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 277
VIDEO_TDR_FAILURE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 278
VIDEO_TDR_TIMEOUT_DETECTED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 279
NTHV_GUEST_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 280
VIDEO_SCHEDULER_INTERNAL_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 281
EM_INITIALIZATION_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 282
DRIVER_RETURNED_HOLDING_CANCEL_LOCK: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 283
ATTEMPTED_WRITE_TO_CM_PROTECTED_STORAGE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 284
EVENT_TRACING_FATAL_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 285
TOO_MANY_RECURSIVE_FAULTS: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 286
INVALID_DRIVER_HANDLE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 287
BITLOCKER_FATAL_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 288
DRIVER_VIOLATION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 289
WHEA_INTERNAL_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 290
CRYPTO_SELF_TEST_FAILURE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 291
WHEA_UNCORRECTABLE_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 292
NMR_INVALID_STATE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 293
NETIO_INVALID_POOL_CALLER: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 294
PAGE_NOT_ZERO: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 295
WORKER_THREAD_RETURNED_WITH_BAD_IO_PRIORITY: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 296
WORKER_THREAD_RETURNED_WITH_BAD_PAGING_IO_PRIORITY: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 297
MUI_NO_VALID_SYSTEM_LANGUAGE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 298
FAULTY_HARDWARE_CORRUPTED_PAGE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 299
EXFAT_FILE_SYSTEM: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 300
VOLSNAP_OVERLAPPED_TABLE_ACCESS: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 301
INVALID_MDL_RANGE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 302
VHD_BOOT_INITIALIZATION_FAILED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 303
DYNAMIC_ADD_PROCESSOR_MISMATCH: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 304
INVALID_EXTENDED_PROCESSOR_STATE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 305
RESOURCE_OWNER_POINTER_INVALID: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 306
DPC_WATCHDOG_VIOLATION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 307
DRIVE_EXTENDER: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 308
REGISTRY_FILTER_DRIVER_EXCEPTION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 309
VHD_BOOT_HOST_VOLUME_NOT_ENOUGH_SPACE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 310
WIN32K_HANDLE_MANAGER: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 311
GPIO_CONTROLLER_DRIVER_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 312
KERNEL_SECURITY_CHECK_FAILURE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 313
KERNEL_MODE_HEAP_CORRUPTION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 314
PASSIVE_INTERRUPT_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 315
INVALID_IO_BOOST_STATE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 316
CRITICAL_INITIALIZATION_FAILURE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 317
ERRATA_WORKAROUND_UNSUCCESSFUL: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 318
REGISTRY_CALLBACK_DRIVER_EXCEPTION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 319
STORAGE_DEVICE_ABNORMALITY_DETECTED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 320
VIDEO_ENGINE_TIMEOUT_DETECTED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 321
VIDEO_TDR_APPLICATION_BLOCKED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 322
PROCESSOR_DRIVER_INTERNAL: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 323
BUGCODE_USB3_DRIVER: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 324
SECURE_BOOT_VIOLATION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 325
NDIS_NET_BUFFER_LIST_INFO_ILLEGALLY_TRANSFERRED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 326
ABNORMAL_RESET_DETECTED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 327
IO_OBJECT_INVALID: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 328
REFS_FILE_SYSTEM: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 329
KERNEL_WMI_INTERNAL: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 330
SOC_SUBSYSTEM_FAILURE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 331
FATAL_ABNORMAL_RESET_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 332
EXCEPTION_SCOPE_INVALID: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 333
SOC_CRITICAL_DEVICE_REMOVED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 334
PDC_WATCHDOG_TIMEOUT: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 335
TCPIP_AOAC_NIC_ACTIVE_REFERENCE_LEAK: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 336
UNSUPPORTED_INSTRUCTION_MODE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 337
INVALID_PUSH_LOCK_FLAGS: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 338
KERNEL_LOCK_ENTRY_LEAKED_ON_THREAD_TERMINATION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 339
UNEXPECTED_STORE_EXCEPTION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 340
OS_DATA_TAMPERING: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 341
WINSOCK_DETECTED_HUNG_CLOSESOCKET_LIVEDUMP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 342
KERNEL_THREAD_PRIORITY_FLOOR_VIOLATION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 343
ILLEGAL_IOMMU_PAGE_FAULT: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 344
HAL_ILLEGAL_IOMMU_PAGE_FAULT: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 345
SDBUS_INTERNAL_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 346
WORKER_THREAD_RETURNED_WITH_SYSTEM_PAGE_PRIORITY_ACTIVE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 347
PDC_WATCHDOG_TIMEOUT_LIVEDUMP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 348
SOC_SUBSYSTEM_FAILURE_LIVEDUMP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 349
BUGCODE_NDIS_DRIVER_LIVE_DUMP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 350
CONNECTED_STANDBY_WATCHDOG_TIMEOUT_LIVEDUMP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 351
WIN32K_ATOMIC_CHECK_FAILURE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 352
LIVE_SYSTEM_DUMP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 353
KERNEL_AUTO_BOOST_INVALID_LOCK_RELEASE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 354
WORKER_THREAD_TEST_CONDITION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 355
WIN32K_CRITICAL_FAILURE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 356
CLUSTER_CSV_STATUS_IO_TIMEOUT_LIVEDUMP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 357
CLUSTER_RESOURCE_CALL_TIMEOUT_LIVEDUMP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 358
CLUSTER_CSV_SNAPSHOT_DEVICE_INFO_TIMEOUT_LIVEDUMP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 359
CLUSTER_CSV_STATE_TRANSITION_TIMEOUT_LIVEDUMP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 360
CLUSTER_CSV_VOLUME_ARRIVAL_LIVEDUMP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 361
CLUSTER_CSV_VOLUME_REMOVAL_LIVEDUMP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 362
CLUSTER_CSV_CLUSTER_WATCHDOG_LIVEDUMP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 363
INVALID_RUNDOWN_PROTECTION_FLAGS: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 364
INVALID_SLOT_ALLOCATOR_FLAGS: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 365
ERESOURCE_INVALID_RELEASE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 366
CLUSTER_CSV_STATE_TRANSITION_INTERVAL_TIMEOUT_LIVEDUMP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 367
CLUSTER_CSV_CLUSSVC_DISCONNECT_WATCHDOG: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 368
CRYPTO_LIBRARY_INTERNAL_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 369
COREMSGCALL_INTERNAL_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 371
COREMSG_INTERNAL_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 372
PREVIOUS_FATAL_ABNORMAL_RESET_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 373
ELAM_DRIVER_DETECTED_FATAL_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 376
CLUSTER_CLUSPORT_STATUS_IO_TIMEOUT_LIVEDUMP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 377
PROFILER_CONFIGURATION_ILLEGAL: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 379
PDC_LOCK_WATCHDOG_LIVEDUMP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 380
PDC_UNEXPECTED_REVOCATION_LIVEDUMP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 381
MICROCODE_REVISION_MISMATCH: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 382
HYPERGUARD_INITIALIZATION_FAILURE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 383
WVR_LIVEDUMP_REPLICATION_IOCONTEXT_TIMEOUT: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 384
WVR_LIVEDUMP_STATE_TRANSITION_TIMEOUT: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 385
WVR_LIVEDUMP_RECOVERY_IOCONTEXT_TIMEOUT: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 386
WVR_LIVEDUMP_APP_IO_TIMEOUT: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 387
WVR_LIVEDUMP_MANUALLY_INITIATED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 388
WVR_LIVEDUMP_STATE_FAILURE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 389
WVR_LIVEDUMP_CRITICAL_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 390
VIDEO_DWMINIT_TIMEOUT_FALLBACK_BDD: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 391
CLUSTER_CSVFS_LIVEDUMP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 392
BAD_OBJECT_HEADER: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 393
SILO_CORRUPT: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 394
SECURE_KERNEL_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 395
HYPERGUARD_VIOLATION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 396
SECURE_FAULT_UNHANDLED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 397
KERNEL_PARTITION_REFERENCE_VIOLATION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 398
SYNTHETIC_EXCEPTION_UNHANDLED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 399
WIN32K_CRITICAL_FAILURE_LIVEDUMP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 400
PF_DETECTED_CORRUPTION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 401
KERNEL_AUTO_BOOST_LOCK_ACQUISITION_WITH_RAISED_IRQL: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 402
VIDEO_DXGKRNL_LIVEDUMP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 403
KERNEL_STORAGE_SLOT_IN_USE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 409
SMB_SERVER_LIVEDUMP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 405
LOADER_ROLLBACK_DETECTED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 406
WIN32K_SECURITY_FAILURE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 407
UFX_LIVEDUMP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 408
WORKER_THREAD_RETURNED_WHILE_ATTACHED_TO_SILO: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 410
TTM_FATAL_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 411
WIN32K_POWER_WATCHDOG_TIMEOUT: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 412
CLUSTER_SVHDX_LIVEDUMP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 413
BUGCODE_NETADAPTER_DRIVER: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 414
PDC_PRIVILEGE_CHECK_LIVEDUMP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 415
TTM_WATCHDOG_TIMEOUT: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 416
WIN32K_CALLOUT_WATCHDOG_LIVEDUMP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 417
WIN32K_CALLOUT_WATCHDOG_BUGCHECK: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 418
CALL_HAS_NOT_RETURNED_WATCHDOG_TIMEOUT_LIVEDUMP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 419
DRIPS_SW_HW_DIVERGENCE_LIVEDUMP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 420
USB_DRIPS_BLOCKER_SURPRISE_REMOVAL_LIVEDUMP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 421
BLUETOOTH_ERROR_RECOVERY_LIVEDUMP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 422
SMB_REDIRECTOR_LIVEDUMP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 423
VIDEO_DXGKRNL_BLACK_SCREEN_LIVEDUMP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 424
DIRECTED_FX_TRANSITION_LIVEDUMP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 425
EXCEPTION_ON_INVALID_STACK: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 426
UNWIND_ON_INVALID_STACK: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 427
VIDEO_MINIPORT_FAILED_LIVEDUMP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 432
VIDEO_MINIPORT_BLACK_SCREEN_LIVEDUMP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 440
DRIVER_VERIFIER_DETECTED_VIOLATION_LIVEDUMP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 452
IO_THREADPOOL_DEADLOCK_LIVEDUMP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 453
FAST_ERESOURCE_PRECONDITION_VIOLATION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 454
STORE_DATA_STRUCTURE_CORRUPTION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 455
MANUALLY_INITIATED_POWER_BUTTON_HOLD: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 456
USER_MODE_HEALTH_MONITOR_LIVEDUMP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 457
SYNTHETIC_WATCHDOG_TIMEOUT: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 458
INVALID_SILO_DETACH: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 459
EXRESOURCE_TIMEOUT_LIVEDUMP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 460
INVALID_CALLBACK_STACK_ADDRESS: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 461
INVALID_KERNEL_STACK_ADDRESS: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 462
HARDWARE_WATCHDOG_TIMEOUT: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 463
ACPI_FIRMWARE_WATCHDOG_TIMEOUT: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 464
TELEMETRY_ASSERTS_LIVEDUMP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 465
WORKER_THREAD_INVALID_STATE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 466
WFP_INVALID_OPERATION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 467
UCMUCSI_LIVEDUMP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 468
DRIVER_PNP_WATCHDOG: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 469
WORKER_THREAD_RETURNED_WITH_NON_DEFAULT_WORKLOAD_CLASS: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 470
EFS_FATAL_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 471
UCMUCSI_FAILURE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 472
HAL_IOMMU_INTERNAL_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 473
HAL_BLOCKED_PROCESSOR_INTERNAL_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 474
IPI_WATCHDOG_TIMEOUT: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 475
DMA_COMMON_BUFFER_VECTOR_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 476
BUGCODE_MBBADAPTER_DRIVER: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 477
BUGCODE_WIFIADAPTER_DRIVER: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 478
PROCESSOR_START_TIMEOUT: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 479
INVALID_ALTERNATE_SYSTEM_CALL_HANDLER_REGISTRATION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 480
DEVICE_DIAGNOSTIC_LOG_LIVEDUMP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 481
AZURE_DEVICE_FW_DUMP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 482
BREAKAWAY_CABLE_TRANSITION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 483
VIDEO_DXGKRNL_SYSMM_FATAL_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 484
DRIVER_VERIFIER_TRACKING_LIVE_DUMP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 485
CRASHDUMP_WATCHDOG_TIMEOUT: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 486
REGISTRY_LIVE_DUMP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 487
INVALID_THREAD_AFFINITY_STATE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 488
ILLEGAL_ATS_INITIALIZATION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 489
SECURE_PCI_CONFIG_SPACE_ACCESS_VIOLATION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 490
DAM_WATCHDOG_TIMEOUT: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 491
HANDLE_LIVE_DUMP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 492
HANDLE_ERROR_ON_CRITICAL_THREAD: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 493
MPSDRV_QUERY_USER: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 1073742318
VMBUS_LIVEDUMP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 1073742319
USB4_HARDWARE_VIOLATION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 496
KASAN_ENLIGHTENMENT_VIOLATION: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 497
KASAN_ILLEGAL_ACCESS: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 498
IORING: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 499
MDL_CACHE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 500
MISALIGNED_POINTER_PARAMETER: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 502
MSSECCORE_ASSERTION_FAILURE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 503
XBOX_VMCTRL_CS_TIMEOUT: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 854
XBOX_CORRUPTED_IMAGE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 855
XBOX_INVERTED_FUNCTION_TABLE_OVERFLOW: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 856
XBOX_CORRUPTED_IMAGE_BASE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 857
XBOX_XDS_WATCHDOG_TIMEOUT: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 858
XBOX_SHUTDOWN_WATCHDOG_TIMEOUT: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 859
XBOX_360_SYSTEM_CRASH: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 864
XBOX_360_SYSTEM_CRASH_RESERVED: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 1056
XBOX_SECURITY_FAILUE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 1057
KERNEL_CFG_INIT_FAILURE: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 1058
MANUALLY_INITIATED_POWER_BUTTON_HOLD_LIVE_DUMP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 4552
HYPERVISOR_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 131073
XBOX_MANUALLY_INITIATED_CRASH: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 196614
MANUALLY_INITIATED_BLACKSCREEN_HOTKEY_LIVE_DUMP: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 8648
WINLOGON_FATAL_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 3221226010
MANUALLY_INITIATED_CRASH1: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 3735936685
BUGCHECK_CONTEXT_MODIFIER: win32more.Windows.Win32.System.Diagnostics.Debug.BUGCHECK_ERROR = 2147483648
if ARCH in 'ARM64':
    class CONTEXT(Structure):
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
        class _Anonymous_e__Union(Union):
            Anonymous: _Anonymous_e__Struct
            X: UInt64 * 31
            class _Anonymous_e__Struct(Structure):
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
elif ARCH in 'X64':
    class CONTEXT(Structure):
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
        class _Anonymous_e__Union(Union):
            FltSave: win32more.Windows.Win32.System.Diagnostics.Debug.XSAVE_FORMAT
            Anonymous: _Anonymous_e__Struct
            class _Anonymous_e__Struct(Structure):
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
elif ARCH in 'X86':
    class CONTEXT(Structure):
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
CONTEXT_AMD64: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 1048576
CONTEXT_CONTROL_AMD64: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 1048577
CONTEXT_INTEGER_AMD64: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 1048578
CONTEXT_SEGMENTS_AMD64: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 1048580
CONTEXT_FLOATING_POINT_AMD64: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 1048584
CONTEXT_DEBUG_REGISTERS_AMD64: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 1048592
CONTEXT_FULL_AMD64: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 1048587
CONTEXT_ALL_AMD64: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 1048607
CONTEXT_XSTATE_AMD64: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 1048640
CONTEXT_KERNEL_CET_AMD64: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 1048704
CONTEXT_KERNEL_DEBUGGER_AMD64: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 67108864
CONTEXT_EXCEPTION_ACTIVE_AMD64: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 134217728
CONTEXT_SERVICE_ACTIVE_AMD64: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 268435456
CONTEXT_EXCEPTION_REQUEST_AMD64: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 1073741824
CONTEXT_EXCEPTION_REPORTING_AMD64: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 2147483648
CONTEXT_UNWOUND_TO_CALL_AMD64: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 536870912
CONTEXT_X86: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 65536
CONTEXT_CONTROL_X86: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 65537
CONTEXT_INTEGER_X86: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 65538
CONTEXT_SEGMENTS_X86: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 65540
CONTEXT_FLOATING_POINT_X86: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 65544
CONTEXT_DEBUG_REGISTERS_X86: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 65552
CONTEXT_EXTENDED_REGISTERS_X86: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 65568
CONTEXT_FULL_X86: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 65543
CONTEXT_ALL_X86: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 65599
CONTEXT_XSTATE_X86: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 65600
CONTEXT_EXCEPTION_ACTIVE_X86: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 134217728
CONTEXT_SERVICE_ACTIVE_X86: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 268435456
CONTEXT_EXCEPTION_REQUEST_X86: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 1073741824
CONTEXT_EXCEPTION_REPORTING_X86: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 2147483648
CONTEXT_ARM64: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 4194304
CONTEXT_CONTROL_ARM64: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 4194305
CONTEXT_INTEGER_ARM64: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 4194306
CONTEXT_FLOATING_POINT_ARM64: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 4194308
CONTEXT_DEBUG_REGISTERS_ARM64: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 4194312
CONTEXT_X18_ARM64: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 4194320
CONTEXT_FULL_ARM64: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 4194311
CONTEXT_ALL_ARM64: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 4194335
CONTEXT_EXCEPTION_ACTIVE_ARM64: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 134217728
CONTEXT_SERVICE_ACTIVE_ARM64: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 268435456
CONTEXT_EXCEPTION_REQUEST_ARM64: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 1073741824
CONTEXT_EXCEPTION_REPORTING_ARM64: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 2147483648
CONTEXT_UNWOUND_TO_CALL_ARM64: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 536870912
CONTEXT_RET_TO_GUEST_ARM64: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 1073741824
CONTEXT_ARM: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 2097152
CONTEXT_CONTROL_ARM: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 2097153
CONTEXT_INTEGER_ARM: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 2097154
CONTEXT_FLOATING_POINT_ARM: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 2097156
CONTEXT_DEBUG_REGISTERS_ARM: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 2097160
CONTEXT_FULL_ARM: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 2097159
CONTEXT_ALL_ARM: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 2097167
CONTEXT_EXCEPTION_ACTIVE_ARM: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 134217728
CONTEXT_SERVICE_ACTIVE_ARM: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 268435456
CONTEXT_EXCEPTION_REQUEST_ARM: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 1073741824
CONTEXT_EXCEPTION_REPORTING_ARM: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 2147483648
CONTEXT_UNWOUND_TO_CALL_ARM: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT_FLAGS = 536870912
class CPU_INFORMATION(Union):
    X86CpuInfo: _X86CpuInfo_e__Struct
    OtherCpuInfo: _OtherCpuInfo_e__Struct
    class _X86CpuInfo_e__Struct(Structure):
        VendorId: UInt32 * 3
        VersionInformation: UInt32
        FeatureInformation: UInt32
        AMDExtendedCpuFeatures: UInt32
    class _OtherCpuInfo_e__Struct(Structure):
        ProcessorFeatures: UInt64 * 2
        _pack_ = 4
class CREATE_PROCESS_DEBUG_INFO(Structure):
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
class CREATE_THREAD_DEBUG_INFO(Structure):
    hThread: win32more.Windows.Win32.Foundation.HANDLE
    lpThreadLocalBase: VoidPtr
    lpStartAddress: win32more.Windows.Win32.System.Threading.LPTHREAD_START_ROUTINE
class DBGHELP_DATA_REPORT_STRUCT(Structure):
    pBinPathNonExist: win32more.Windows.Win32.Foundation.PWSTR
    pSymbolPathNonExist: win32more.Windows.Win32.Foundation.PWSTR
DBGPROP_ATTRIB_FLAGS = Int32
DBGPROP_ATTRIB_NO_ATTRIB: win32more.Windows.Win32.System.Diagnostics.Debug.DBGPROP_ATTRIB_FLAGS = 0
DBGPROP_ATTRIB_VALUE_IS_INVALID: win32more.Windows.Win32.System.Diagnostics.Debug.DBGPROP_ATTRIB_FLAGS = 8
DBGPROP_ATTRIB_VALUE_IS_EXPANDABLE: win32more.Windows.Win32.System.Diagnostics.Debug.DBGPROP_ATTRIB_FLAGS = 16
DBGPROP_ATTRIB_VALUE_IS_FAKE: win32more.Windows.Win32.System.Diagnostics.Debug.DBGPROP_ATTRIB_FLAGS = 32
DBGPROP_ATTRIB_VALUE_IS_METHOD: win32more.Windows.Win32.System.Diagnostics.Debug.DBGPROP_ATTRIB_FLAGS = 256
DBGPROP_ATTRIB_VALUE_IS_EVENT: win32more.Windows.Win32.System.Diagnostics.Debug.DBGPROP_ATTRIB_FLAGS = 512
DBGPROP_ATTRIB_VALUE_IS_RAW_STRING: win32more.Windows.Win32.System.Diagnostics.Debug.DBGPROP_ATTRIB_FLAGS = 1024
DBGPROP_ATTRIB_VALUE_READONLY: win32more.Windows.Win32.System.Diagnostics.Debug.DBGPROP_ATTRIB_FLAGS = 2048
DBGPROP_ATTRIB_ACCESS_PUBLIC: win32more.Windows.Win32.System.Diagnostics.Debug.DBGPROP_ATTRIB_FLAGS = 4096
DBGPROP_ATTRIB_ACCESS_PRIVATE: win32more.Windows.Win32.System.Diagnostics.Debug.DBGPROP_ATTRIB_FLAGS = 8192
DBGPROP_ATTRIB_ACCESS_PROTECTED: win32more.Windows.Win32.System.Diagnostics.Debug.DBGPROP_ATTRIB_FLAGS = 16384
DBGPROP_ATTRIB_ACCESS_FINAL: win32more.Windows.Win32.System.Diagnostics.Debug.DBGPROP_ATTRIB_FLAGS = 32768
DBGPROP_ATTRIB_STORAGE_GLOBAL: win32more.Windows.Win32.System.Diagnostics.Debug.DBGPROP_ATTRIB_FLAGS = 65536
DBGPROP_ATTRIB_STORAGE_STATIC: win32more.Windows.Win32.System.Diagnostics.Debug.DBGPROP_ATTRIB_FLAGS = 131072
DBGPROP_ATTRIB_STORAGE_FIELD: win32more.Windows.Win32.System.Diagnostics.Debug.DBGPROP_ATTRIB_FLAGS = 262144
DBGPROP_ATTRIB_STORAGE_VIRTUAL: win32more.Windows.Win32.System.Diagnostics.Debug.DBGPROP_ATTRIB_FLAGS = 524288
DBGPROP_ATTRIB_TYPE_IS_CONSTANT: win32more.Windows.Win32.System.Diagnostics.Debug.DBGPROP_ATTRIB_FLAGS = 1048576
DBGPROP_ATTRIB_TYPE_IS_SYNCHRONIZED: win32more.Windows.Win32.System.Diagnostics.Debug.DBGPROP_ATTRIB_FLAGS = 2097152
DBGPROP_ATTRIB_TYPE_IS_VOLATILE: win32more.Windows.Win32.System.Diagnostics.Debug.DBGPROP_ATTRIB_FLAGS = 4194304
DBGPROP_ATTRIB_HAS_EXTENDED_ATTRIBS: win32more.Windows.Win32.System.Diagnostics.Debug.DBGPROP_ATTRIB_FLAGS = 8388608
DBGPROP_ATTRIB_FRAME_INTRYBLOCK: win32more.Windows.Win32.System.Diagnostics.Debug.DBGPROP_ATTRIB_FLAGS = 16777216
DBGPROP_ATTRIB_FRAME_INCATCHBLOCK: win32more.Windows.Win32.System.Diagnostics.Debug.DBGPROP_ATTRIB_FLAGS = 33554432
DBGPROP_ATTRIB_FRAME_INFINALLYBLOCK: win32more.Windows.Win32.System.Diagnostics.Debug.DBGPROP_ATTRIB_FLAGS = 67108864
DBGPROP_ATTRIB_VALUE_IS_RETURN_VALUE: win32more.Windows.Win32.System.Diagnostics.Debug.DBGPROP_ATTRIB_FLAGS = 134217728
DBGPROP_ATTRIB_VALUE_PENDING_MUTATION: win32more.Windows.Win32.System.Diagnostics.Debug.DBGPROP_ATTRIB_FLAGS = 268435456
DBGPROP_INFO = Int32
DBGPROP_INFO_NAME: win32more.Windows.Win32.System.Diagnostics.Debug.DBGPROP_INFO = 1
DBGPROP_INFO_TYPE: win32more.Windows.Win32.System.Diagnostics.Debug.DBGPROP_INFO = 2
DBGPROP_INFO_VALUE: win32more.Windows.Win32.System.Diagnostics.Debug.DBGPROP_INFO = 4
DBGPROP_INFO_FULLNAME: win32more.Windows.Win32.System.Diagnostics.Debug.DBGPROP_INFO = 32
DBGPROP_INFO_ATTRIBUTES: win32more.Windows.Win32.System.Diagnostics.Debug.DBGPROP_INFO = 8
DBGPROP_INFO_DEBUGPROP: win32more.Windows.Win32.System.Diagnostics.Debug.DBGPROP_INFO = 16
DBGPROP_INFO_BEAUTIFY: win32more.Windows.Win32.System.Diagnostics.Debug.DBGPROP_INFO = 33554432
DBGPROP_INFO_CALLTOSTRING: win32more.Windows.Win32.System.Diagnostics.Debug.DBGPROP_INFO = 67108864
DBGPROP_INFO_AUTOEXPAND: win32more.Windows.Win32.System.Diagnostics.Debug.DBGPROP_INFO = 134217728
class DEBUG_EVENT(Structure):
    dwDebugEventCode: win32more.Windows.Win32.System.Diagnostics.Debug.DEBUG_EVENT_CODE
    dwProcessId: UInt32
    dwThreadId: UInt32
    u: _u_e__Union
    class _u_e__Union(Union):
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
CREATE_PROCESS_DEBUG_EVENT: win32more.Windows.Win32.System.Diagnostics.Debug.DEBUG_EVENT_CODE = 3
CREATE_THREAD_DEBUG_EVENT: win32more.Windows.Win32.System.Diagnostics.Debug.DEBUG_EVENT_CODE = 2
EXCEPTION_DEBUG_EVENT: win32more.Windows.Win32.System.Diagnostics.Debug.DEBUG_EVENT_CODE = 1
EXIT_PROCESS_DEBUG_EVENT: win32more.Windows.Win32.System.Diagnostics.Debug.DEBUG_EVENT_CODE = 5
EXIT_THREAD_DEBUG_EVENT: win32more.Windows.Win32.System.Diagnostics.Debug.DEBUG_EVENT_CODE = 4
LOAD_DLL_DEBUG_EVENT: win32more.Windows.Win32.System.Diagnostics.Debug.DEBUG_EVENT_CODE = 6
OUTPUT_DEBUG_STRING_EVENT: win32more.Windows.Win32.System.Diagnostics.Debug.DEBUG_EVENT_CODE = 8
RIP_EVENT: win32more.Windows.Win32.System.Diagnostics.Debug.DEBUG_EVENT_CODE = 9
UNLOAD_DLL_DEBUG_EVENT: win32more.Windows.Win32.System.Diagnostics.Debug.DEBUG_EVENT_CODE = 7
@winfunctype_pointer
def DIGEST_FUNCTION(refdata: VoidPtr, pData: POINTER(Byte), dwLength: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'ARM64':
    class DISPATCHER_CONTEXT(Structure):
        ControlPc: UIntPtr
        ImageBase: UIntPtr
        FunctionEntry: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_ARM64_RUNTIME_FUNCTION_ENTRY)
        EstablisherFrame: UIntPtr
        TargetPc: UIntPtr
        ContextRecord: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT)
        LanguageHandler: win32more.Windows.Win32.System.Kernel.EXCEPTION_ROUTINE
        HandlerData: VoidPtr
        HistoryTable: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.UNWIND_HISTORY_TABLE)
        ScopeIndex: UInt32
        ControlPcIsUnwound: win32more.Windows.Win32.Foundation.BOOLEAN
        NonVolatileRegisters: POINTER(Byte)
elif ARCH in 'X64':
    class DISPATCHER_CONTEXT(Structure):
        ControlPc: UInt64
        ImageBase: UInt64
        FunctionEntry: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_RUNTIME_FUNCTION_ENTRY)
        EstablisherFrame: UInt64
        TargetIp: UInt64
        ContextRecord: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT)
        LanguageHandler: win32more.Windows.Win32.System.Kernel.EXCEPTION_ROUTINE
        HandlerData: VoidPtr
        HistoryTable: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.UNWIND_HISTORY_TABLE)
        ScopeIndex: UInt32
        Fill0: UInt32
class DUMP_FILE_ATTRIBUTES(Union):
    Anonymous: _Anonymous_e__Struct
    Attributes: UInt32
    class _Anonymous_e__Struct(Structure):
        HiberCrash: Annotated[UInt32, 1]
        DumpDevicePowerOff: Annotated[UInt32, 1]
        InsufficientDumpfileSize: Annotated[UInt32, 1]
        KernelGeneratedTriageDump: Annotated[UInt32, 1]
        LiveDumpGeneratedDump: Annotated[UInt32, 1]
        DumpIsGeneratedOffline: Annotated[UInt32, 1]
        FilterDumpFile: Annotated[UInt32, 1]
        EarlyBootCrash: Annotated[UInt32, 1]
        EncryptedDumpData: Annotated[UInt32, 1]
        DecryptedDump: Annotated[UInt32, 1]
        ReservedFlags: Annotated[UInt32, 22]
class DUMP_HEADER32(Structure):
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
    class _Anonymous_e__Union(Union):
        PhysicalMemoryBlock: win32more.Windows.Win32.System.Diagnostics.Debug.PHYSICAL_MEMORY_DESCRIPTOR32
        PhysicalMemoryBlockBuffer: Byte * 700
class DUMP_HEADER64(Structure):
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
    class _Anonymous_e__Union(Union):
        PhysicalMemoryBlock: win32more.Windows.Win32.System.Diagnostics.Debug.PHYSICAL_MEMORY_DESCRIPTOR64
        PhysicalMemoryBlockBuffer: Byte * 700
DUMP_TYPE = Int32
DUMP_TYPE_INVALID: win32more.Windows.Win32.System.Diagnostics.Debug.DUMP_TYPE = -1
DUMP_TYPE_UNKNOWN: win32more.Windows.Win32.System.Diagnostics.Debug.DUMP_TYPE = 0
DUMP_TYPE_FULL: win32more.Windows.Win32.System.Diagnostics.Debug.DUMP_TYPE = 1
DUMP_TYPE_SUMMARY: win32more.Windows.Win32.System.Diagnostics.Debug.DUMP_TYPE = 2
DUMP_TYPE_HEADER: win32more.Windows.Win32.System.Diagnostics.Debug.DUMP_TYPE = 3
DUMP_TYPE_TRIAGE: win32more.Windows.Win32.System.Diagnostics.Debug.DUMP_TYPE = 4
DUMP_TYPE_BITMAP_FULL: win32more.Windows.Win32.System.Diagnostics.Debug.DUMP_TYPE = 5
DUMP_TYPE_BITMAP_KERNEL: win32more.Windows.Win32.System.Diagnostics.Debug.DUMP_TYPE = 6
DUMP_TYPE_AUTOMATIC: win32more.Windows.Win32.System.Diagnostics.Debug.DUMP_TYPE = 7
class DebugPropertyInfo(Structure):
    m_dwValidFields: UInt32
    m_bstrName: win32more.Windows.Win32.Foundation.BSTR
    m_bstrType: win32more.Windows.Win32.Foundation.BSTR
    m_bstrValue: win32more.Windows.Win32.Foundation.BSTR
    m_bstrFullName: win32more.Windows.Win32.Foundation.BSTR
    m_dwAttrib: UInt32
    m_pDebugProp: win32more.Windows.Win32.System.Diagnostics.Debug.IDebugProperty
class EXCEPTION_DEBUG_INFO(Structure):
    ExceptionRecord: win32more.Windows.Win32.System.Diagnostics.Debug.EXCEPTION_RECORD
    dwFirstChance: UInt32
class EXCEPTION_POINTERS(Structure):
    ExceptionRecord: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.EXCEPTION_RECORD)
    ContextRecord: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT)
class EXCEPTION_RECORD(Structure):
    ExceptionCode: win32more.Windows.Win32.Foundation.NTSTATUS
    ExceptionFlags: UInt32
    ExceptionRecord: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.EXCEPTION_RECORD)
    ExceptionAddress: VoidPtr
    NumberParameters: UInt32
    ExceptionInformation: UIntPtr * 15
class EXCEPTION_RECORD32(Structure):
    ExceptionCode: win32more.Windows.Win32.Foundation.NTSTATUS
    ExceptionFlags: UInt32
    ExceptionRecord: UInt32
    ExceptionAddress: UInt32
    NumberParameters: UInt32
    ExceptionInformation: UInt32 * 15
class EXCEPTION_RECORD64(Structure):
    ExceptionCode: win32more.Windows.Win32.Foundation.NTSTATUS
    ExceptionFlags: UInt32
    ExceptionRecord: UInt64
    ExceptionAddress: UInt64
    NumberParameters: UInt32
    __unusedAlignment: UInt32
    ExceptionInformation: UInt64 * 15
class EXIT_PROCESS_DEBUG_INFO(Structure):
    dwExitCode: UInt32
class EXIT_THREAD_DEBUG_INFO(Structure):
    dwExitCode: UInt32
EX_PROP_INFO_FLAGS = Int32
EX_PROP_INFO_ID: win32more.Windows.Win32.System.Diagnostics.Debug.EX_PROP_INFO_FLAGS = 256
EX_PROP_INFO_NTYPE: win32more.Windows.Win32.System.Diagnostics.Debug.EX_PROP_INFO_FLAGS = 512
EX_PROP_INFO_NVALUE: win32more.Windows.Win32.System.Diagnostics.Debug.EX_PROP_INFO_FLAGS = 1024
EX_PROP_INFO_LOCKBYTES: win32more.Windows.Win32.System.Diagnostics.Debug.EX_PROP_INFO_FLAGS = 2048
EX_PROP_INFO_DEBUGEXTPROP: win32more.Windows.Win32.System.Diagnostics.Debug.EX_PROP_INFO_FLAGS = 4096
class ExtendedDebugPropertyInfo(Structure):
    dwValidFields: UInt32
    pszName: win32more.Windows.Win32.Foundation.PWSTR
    pszType: win32more.Windows.Win32.Foundation.PWSTR
    pszValue: win32more.Windows.Win32.Foundation.PWSTR
    pszFullName: win32more.Windows.Win32.Foundation.PWSTR
    dwAttrib: UInt32
    pDebugProp: win32more.Windows.Win32.System.Diagnostics.Debug.IDebugProperty
    nDISPID: UInt32
    nType: UInt32
    varValue: win32more.Windows.Win32.System.Variant.VARIANT
    plbValue: win32more.Windows.Win32.System.Com.StructuredStorage.ILockBytes
    pDebugExtProp: win32more.Windows.Win32.System.Diagnostics.Debug.IDebugExtendedProperty
FACILITY_CODE = UInt32
FACILITY_NULL: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 0
FACILITY_RPC: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 1
FACILITY_DISPATCH: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 2
FACILITY_STORAGE: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 3
FACILITY_ITF: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 4
FACILITY_WIN32: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 7
FACILITY_WINDOWS: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 8
FACILITY_SSPI: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 9
FACILITY_SECURITY: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 9
FACILITY_CONTROL: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 10
FACILITY_CERT: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 11
FACILITY_INTERNET: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 12
FACILITY_MEDIASERVER: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 13
FACILITY_MSMQ: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 14
FACILITY_SETUPAPI: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 15
FACILITY_SCARD: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 16
FACILITY_COMPLUS: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 17
FACILITY_AAF: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 18
FACILITY_URT: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 19
FACILITY_ACS: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 20
FACILITY_DPLAY: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 21
FACILITY_UMI: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 22
FACILITY_SXS: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 23
FACILITY_WINDOWS_CE: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 24
FACILITY_HTTP: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 25
FACILITY_USERMODE_COMMONLOG: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 26
FACILITY_WER: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 27
FACILITY_USERMODE_FILTER_MANAGER: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 31
FACILITY_BACKGROUNDCOPY: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 32
FACILITY_CONFIGURATION: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 33
FACILITY_WIA: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 33
FACILITY_STATE_MANAGEMENT: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 34
FACILITY_METADIRECTORY: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 35
FACILITY_WINDOWSUPDATE: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 36
FACILITY_DIRECTORYSERVICE: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 37
FACILITY_GRAPHICS: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 38
FACILITY_SHELL: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 39
FACILITY_NAP: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 39
FACILITY_TPM_SERVICES: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 40
FACILITY_TPM_SOFTWARE: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 41
FACILITY_UI: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 42
FACILITY_XAML: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 43
FACILITY_ACTION_QUEUE: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 44
FACILITY_PLA: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 48
FACILITY_WINDOWS_SETUP: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 48
FACILITY_FVE: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 49
FACILITY_FWP: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 50
FACILITY_WINRM: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 51
FACILITY_NDIS: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 52
FACILITY_USERMODE_HYPERVISOR: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 53
FACILITY_CMI: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 54
FACILITY_USERMODE_VIRTUALIZATION: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 55
FACILITY_USERMODE_VOLMGR: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 56
FACILITY_BCD: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 57
FACILITY_USERMODE_VHD: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 58
FACILITY_USERMODE_HNS: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 59
FACILITY_SDIAG: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 60
FACILITY_WEBSERVICES: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 61
FACILITY_WINPE: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 61
FACILITY_WPN: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 62
FACILITY_WINDOWS_STORE: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 63
FACILITY_INPUT: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 64
FACILITY_QUIC: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 65
FACILITY_EAP: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 66
FACILITY_IORING: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 70
FACILITY_WINDOWS_DEFENDER: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 80
FACILITY_OPC: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 81
FACILITY_XPS: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 82
FACILITY_MBN: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 84
FACILITY_POWERSHELL: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 84
FACILITY_RAS: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 83
FACILITY_P2P_INT: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 98
FACILITY_P2P: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 99
FACILITY_DAF: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 100
FACILITY_BLUETOOTH_ATT: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 101
FACILITY_AUDIO: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 102
FACILITY_STATEREPOSITORY: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 103
FACILITY_VISUALCPP: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 109
FACILITY_SCRIPT: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 112
FACILITY_PARSE: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 113
FACILITY_BLB: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 120
FACILITY_BLB_CLI: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 121
FACILITY_WSBAPP: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 122
FACILITY_BLBUI: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 128
FACILITY_USN: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 129
FACILITY_USERMODE_VOLSNAP: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 130
FACILITY_TIERING: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 131
FACILITY_WSB_ONLINE: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 133
FACILITY_ONLINE_ID: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 134
FACILITY_DEVICE_UPDATE_AGENT: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 135
FACILITY_DRVSERVICING: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 136
FACILITY_DLS: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 153
FACILITY_DELIVERY_OPTIMIZATION: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 208
FACILITY_USERMODE_SPACES: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 231
FACILITY_USER_MODE_SECURITY_CORE: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 232
FACILITY_USERMODE_LICENSING: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 234
FACILITY_SOS: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 160
FACILITY_OCP_UPDATE_AGENT: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 173
FACILITY_DEBUGGERS: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 176
FACILITY_SPP: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 256
FACILITY_RESTORE: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 256
FACILITY_DMSERVER: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 256
FACILITY_DEPLOYMENT_SERVICES_SERVER: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 257
FACILITY_DEPLOYMENT_SERVICES_IMAGING: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 258
FACILITY_DEPLOYMENT_SERVICES_MANAGEMENT: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 259
FACILITY_DEPLOYMENT_SERVICES_UTIL: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 260
FACILITY_DEPLOYMENT_SERVICES_BINLSVC: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 261
FACILITY_DEPLOYMENT_SERVICES_PXE: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 263
FACILITY_DEPLOYMENT_SERVICES_TFTP: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 264
FACILITY_DEPLOYMENT_SERVICES_TRANSPORT_MANAGEMENT: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 272
FACILITY_DEPLOYMENT_SERVICES_DRIVER_PROVISIONING: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 278
FACILITY_DEPLOYMENT_SERVICES_MULTICAST_SERVER: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 289
FACILITY_DEPLOYMENT_SERVICES_MULTICAST_CLIENT: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 290
FACILITY_DEPLOYMENT_SERVICES_CONTENT_PROVIDER: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 293
FACILITY_HSP_SERVICES: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 296
FACILITY_HSP_SOFTWARE: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 297
FACILITY_LINGUISTIC_SERVICES: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 305
FACILITY_AUDIOSTREAMING: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 1094
FACILITY_TTD: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 1490
FACILITY_ACCELERATOR: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 1536
FACILITY_WMAAECMA: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 1996
FACILITY_DIRECTMUSIC: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 2168
FACILITY_DIRECT3D10: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 2169
FACILITY_DXGI: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 2170
FACILITY_DXGI_DDI: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 2171
FACILITY_DIRECT3D11: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 2172
FACILITY_DIRECT3D11_DEBUG: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 2173
FACILITY_DIRECT3D12: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 2174
FACILITY_DIRECT3D12_DEBUG: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 2175
FACILITY_DXCORE: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 2176
FACILITY_PRESENTATION: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 2177
FACILITY_LEAP: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 2184
FACILITY_AUDCLNT: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 2185
FACILITY_WINCODEC_DWRITE_DWM: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 2200
FACILITY_WINML: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 2192
FACILITY_DIRECT2D: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 2201
FACILITY_DEFRAG: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 2304
FACILITY_USERMODE_SDBUS: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 2305
FACILITY_JSCRIPT: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 2306
FACILITY_PIDGENX: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 2561
FACILITY_EAS: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 85
FACILITY_WEB: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 885
FACILITY_WEB_SOCKET: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 886
FACILITY_MOBILE: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 1793
FACILITY_SQLITE: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 1967
FACILITY_SERVICE_FABRIC: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 1968
FACILITY_UTC: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 1989
FACILITY_WEP: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 2049
FACILITY_SYNCENGINE: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 2050
FACILITY_XBOX: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 2339
FACILITY_GAME: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 2340
FACILITY_PIX: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 2748
FACILITY_NT_BIT: win32more.Windows.Win32.System.Diagnostics.Debug.FACILITY_CODE = 268435456
FORMAT_MESSAGE_OPTIONS = UInt32
FORMAT_MESSAGE_ALLOCATE_BUFFER: win32more.Windows.Win32.System.Diagnostics.Debug.FORMAT_MESSAGE_OPTIONS = 256
FORMAT_MESSAGE_ARGUMENT_ARRAY: win32more.Windows.Win32.System.Diagnostics.Debug.FORMAT_MESSAGE_OPTIONS = 8192
FORMAT_MESSAGE_FROM_HMODULE: win32more.Windows.Win32.System.Diagnostics.Debug.FORMAT_MESSAGE_OPTIONS = 2048
FORMAT_MESSAGE_FROM_STRING: win32more.Windows.Win32.System.Diagnostics.Debug.FORMAT_MESSAGE_OPTIONS = 1024
FORMAT_MESSAGE_FROM_SYSTEM: win32more.Windows.Win32.System.Diagnostics.Debug.FORMAT_MESSAGE_OPTIONS = 4096
FORMAT_MESSAGE_IGNORE_INSERTS: win32more.Windows.Win32.System.Diagnostics.Debug.FORMAT_MESSAGE_OPTIONS = 512
class FPO_DATA(Structure):
    ulOffStart: UInt32
    cbProcSize: UInt32
    cdwLocals: UInt32
    cdwParams: UInt16
    cbProlog: Annotated[UInt16, 8]
    cbRegs: Annotated[UInt16, 3]
    fHasSEH: Annotated[UInt16, 1]
    fUseBP: Annotated[UInt16, 1]
    reserved: Annotated[UInt16, 1]
    cbFrame: Annotated[UInt16, 2]
class IDebugExtendedProperty(ComPtr):
    extends: win32more.Windows.Win32.System.Diagnostics.Debug.IDebugProperty
    _iid_ = Guid('{51973c52-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(8)
    def GetExtendedPropertyInfo(self, dwFieldSpec: UInt32, nRadix: UInt32, pExtendedPropertyInfo: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ExtendedDebugPropertyInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def EnumExtendedMembers(self, dwFieldSpec: UInt32, nRadix: UInt32, ppeepi: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IEnumDebugExtendedPropertyInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDebugProperty(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51973c50-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(3)
    def GetPropertyInfo(self, dwFieldSpec: UInt32, nRadix: UInt32, pPropertyInfo: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.DebugPropertyInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetExtendedInfo(self, cInfos: UInt32, rgguidExtendedInfo: POINTER(Guid), rgvar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetValueAsString(self, pszValue: win32more.Windows.Win32.Foundation.PWSTR, nRadix: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EnumMembers(self, dwFieldSpec: UInt32, nRadix: UInt32, refiid: POINTER(Guid), ppepi: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IEnumDebugPropertyInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetParent(self, ppDebugProp: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IDebugProperty)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
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
    def Next(self, celt: UInt32, rgExtendedPropertyInfo: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ExtendedDebugPropertyInfo), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, pedpe: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IEnumDebugExtendedPropertyInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCount(self, pcelt: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumDebugPropertyInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51973c51-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(3)
    def Next(self, celt: UInt32, pi: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.DebugPropertyInfo), pcEltsfetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppepi: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IEnumDebugPropertyInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCount(self, pcelt: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMAGEHLP_CBA_EVENTW(Structure):
    severity: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_CBA_EVENT_SEVERITY
    code: UInt32
    desc: win32more.Windows.Win32.Foundation.PWSTR
    object: VoidPtr
IMAGEHLP_CBA_EVENT = UnicodeAlias('IMAGEHLP_CBA_EVENTW')
IMAGEHLP_CBA_EVENT_SEVERITY = UInt32
sevInfo: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_CBA_EVENT_SEVERITY = 0
sevProblem: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_CBA_EVENT_SEVERITY = 1
sevAttn: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_CBA_EVENT_SEVERITY = 2
sevFatal: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_CBA_EVENT_SEVERITY = 3
class IMAGEHLP_CBA_READ_MEMORY(Structure):
    addr: UInt64
    buf: VoidPtr
    bytes: UInt32
    bytesread: POINTER(UInt32)
if ARCH in 'X86':
    class IMAGEHLP_DEFERRED_SYMBOL_LOAD(Structure):
        SizeOfStruct: UInt32
        BaseOfImage: UInt32
        CheckSum: UInt32
        TimeDateStamp: UInt32
        FileName: win32more.Windows.Win32.Foundation.CHAR * 260
        Reparse: win32more.Windows.Win32.Foundation.BOOLEAN
        hFile: win32more.Windows.Win32.Foundation.HANDLE
class IMAGEHLP_DEFERRED_SYMBOL_LOAD64(Structure):
    SizeOfStruct: UInt32
    BaseOfImage: UInt64
    CheckSum: UInt32
    TimeDateStamp: UInt32
    FileName: win32more.Windows.Win32.Foundation.CHAR * 260
    Reparse: win32more.Windows.Win32.Foundation.BOOLEAN
    hFile: win32more.Windows.Win32.Foundation.HANDLE
    Flags: UInt32
class IMAGEHLP_DEFERRED_SYMBOL_LOADW64(Structure):
    SizeOfStruct: UInt32
    BaseOfImage: UInt64
    CheckSum: UInt32
    TimeDateStamp: UInt32
    FileName: Char * 261
    Reparse: win32more.Windows.Win32.Foundation.BOOLEAN
    hFile: win32more.Windows.Win32.Foundation.HANDLE
    Flags: UInt32
if ARCH in 'X86':
    class IMAGEHLP_DUPLICATE_SYMBOL(Structure):
        SizeOfStruct: UInt32
        NumberOfDups: UInt32
        Symbol: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL)
        SelectedSymbol: UInt32
class IMAGEHLP_DUPLICATE_SYMBOL64(Structure):
    SizeOfStruct: UInt32
    NumberOfDups: UInt32
    Symbol: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL64)
    SelectedSymbol: UInt32
IMAGEHLP_EXTENDED_OPTIONS = Int32
SYMOPT_EX_DISABLEACCESSTIMEUPDATE: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_EXTENDED_OPTIONS = 0
SYMOPT_EX_LASTVALIDDEBUGDIRECTORY: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_EXTENDED_OPTIONS = 1
SYMOPT_EX_NOIMPLICITPATTERNSEARCH: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_EXTENDED_OPTIONS = 2
SYMOPT_EX_NEVERLOADSYMBOLS: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_EXTENDED_OPTIONS = 3
SYMOPT_EX_MAX: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_EXTENDED_OPTIONS = 4
IMAGEHLP_GET_TYPE_INFO_FLAGS = UInt32
IMAGEHLP_GET_TYPE_INFO_CHILDREN: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_GET_TYPE_INFO_FLAGS = 2
IMAGEHLP_GET_TYPE_INFO_UNCACHED: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_GET_TYPE_INFO_FLAGS = 1
class IMAGEHLP_GET_TYPE_INFO_PARAMS(Structure):
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
hdBase: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_HD_TYPE = 0
hdSym: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_HD_TYPE = 1
hdSrc: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_HD_TYPE = 2
hdMax: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_HD_TYPE = 3
class IMAGEHLP_JIT_SYMBOLMAP(Structure):
    SizeOfStruct: UInt32
    Address: UInt64
    BaseOfImage: UInt64
class IMAGEHLP_LINE64(Structure):
    SizeOfStruct: UInt32
    Key: VoidPtr
    LineNumber: UInt32
    FileName: win32more.Windows.Win32.Foundation.PSTR
    Address: UInt64
if ARCH in 'X86':
    class IMAGEHLP_LINEW(Structure):
        SizeOfStruct: UInt32
        Key: VoidPtr
        LineNumber: UInt32
        FileName: win32more.Windows.Win32.Foundation.PSTR
        Address: UInt64
if ARCH in 'X86':
    IMAGEHLP_LINE = UnicodeAlias('IMAGEHLP_LINEW')
class IMAGEHLP_LINEW64(Structure):
    SizeOfStruct: UInt32
    Key: VoidPtr
    LineNumber: UInt32
    FileName: win32more.Windows.Win32.Foundation.PWSTR
    Address: UInt64
class IMAGEHLP_MODULE64(Structure):
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
class IMAGEHLP_MODULE64_EX(Structure):
    Module: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_MODULE64
    RegionFlags: UInt32
if ARCH in 'X86':
    class IMAGEHLP_MODULEW(Structure):
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
if ARCH in 'X86':
    IMAGEHLP_MODULE = UnicodeAlias('IMAGEHLP_MODULEW')
class IMAGEHLP_MODULEW64(Structure):
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
class IMAGEHLP_MODULEW64_EX(Structure):
    Module: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_MODULEW64
    RegionFlags: UInt32
IMAGEHLP_SF_TYPE = Int32
sfImage: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SF_TYPE = 0
sfDbg: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SF_TYPE = 1
sfPdb: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SF_TYPE = 2
sfMpd: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SF_TYPE = 3
sfMax: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SF_TYPE = 4
class IMAGEHLP_STACK_FRAME(Structure):
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
BindOutOfMemory: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_STATUS_REASON = 0
BindRvaToVaFailed: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_STATUS_REASON = 1
BindNoRoomInImage: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_STATUS_REASON = 2
BindImportModuleFailed: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_STATUS_REASON = 3
BindImportProcedureFailed: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_STATUS_REASON = 4
BindImportModule: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_STATUS_REASON = 5
BindImportProcedure: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_STATUS_REASON = 6
BindForwarder: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_STATUS_REASON = 7
BindForwarderNOT: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_STATUS_REASON = 8
BindImageModified: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_STATUS_REASON = 9
BindExpandFileHeaders: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_STATUS_REASON = 10
BindImageComplete: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_STATUS_REASON = 11
BindMismatchedSymbols: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_STATUS_REASON = 12
BindSymbolsNotUpdated: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_STATUS_REASON = 13
BindImportProcedure32: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_STATUS_REASON = 14
BindImportProcedure64: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_STATUS_REASON = 15
BindForwarder32: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_STATUS_REASON = 16
BindForwarder64: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_STATUS_REASON = 17
BindForwarderNOT32: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_STATUS_REASON = 18
BindForwarderNOT64: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_STATUS_REASON = 19
class IMAGEHLP_SYMBOL64(Structure):
    SizeOfStruct: UInt32
    Address: UInt64
    Size: UInt32
    Flags: UInt32
    MaxNameLength: UInt32
    Name: win32more.Windows.Win32.Foundation.CHAR * 1
class IMAGEHLP_SYMBOL64_PACKAGE(Structure):
    sym: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL64
    name: win32more.Windows.Win32.Foundation.CHAR * 2001
if ARCH in 'X86':
    class IMAGEHLP_SYMBOLW(Structure):
        SizeOfStruct: UInt32
        Address: UInt32
        Size: UInt32
        Flags: UInt32
        MaxNameLength: UInt32
        Name: Char * 1
if ARCH in 'X86':
    IMAGEHLP_SYMBOL = UnicodeAlias('IMAGEHLP_SYMBOLW')
class IMAGEHLP_SYMBOLW64(Structure):
    SizeOfStruct: UInt32
    Address: UInt64
    Size: UInt32
    Flags: UInt32
    MaxNameLength: UInt32
    Name: Char * 1
class IMAGEHLP_SYMBOLW64_PACKAGE(Structure):
    sym: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOLW64
    name: Char * 2001
if ARCH in 'X86':
    class IMAGEHLP_SYMBOLW_PACKAGE(Structure):
        sym: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOLW
        name: Char * 2001
if ARCH in 'X86':
    class IMAGEHLP_SYMBOL_PACKAGE(Structure):
        sym: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL
        name: win32more.Windows.Win32.Foundation.CHAR * 2001
class IMAGEHLP_SYMBOL_SRC(Structure):
    sizeofstruct: UInt32
    type: UInt32
    file: win32more.Windows.Win32.Foundation.CHAR * 260
IMAGEHLP_SYMBOL_TYPE_INFO = Int32
TI_GET_SYMTAG: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL_TYPE_INFO = 0
TI_GET_SYMNAME: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL_TYPE_INFO = 1
TI_GET_LENGTH: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL_TYPE_INFO = 2
TI_GET_TYPE: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL_TYPE_INFO = 3
TI_GET_TYPEID: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL_TYPE_INFO = 4
TI_GET_BASETYPE: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL_TYPE_INFO = 5
TI_GET_ARRAYINDEXTYPEID: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL_TYPE_INFO = 6
TI_FINDCHILDREN: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL_TYPE_INFO = 7
TI_GET_DATAKIND: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL_TYPE_INFO = 8
TI_GET_ADDRESSOFFSET: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL_TYPE_INFO = 9
TI_GET_OFFSET: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL_TYPE_INFO = 10
TI_GET_VALUE: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL_TYPE_INFO = 11
TI_GET_COUNT: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL_TYPE_INFO = 12
TI_GET_CHILDRENCOUNT: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL_TYPE_INFO = 13
TI_GET_BITPOSITION: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL_TYPE_INFO = 14
TI_GET_VIRTUALBASECLASS: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL_TYPE_INFO = 15
TI_GET_VIRTUALTABLESHAPEID: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL_TYPE_INFO = 16
TI_GET_VIRTUALBASEPOINTEROFFSET: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL_TYPE_INFO = 17
TI_GET_CLASSPARENTID: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL_TYPE_INFO = 18
TI_GET_NESTED: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL_TYPE_INFO = 19
TI_GET_SYMINDEX: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL_TYPE_INFO = 20
TI_GET_LEXICALPARENT: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL_TYPE_INFO = 21
TI_GET_ADDRESS: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL_TYPE_INFO = 22
TI_GET_THISADJUST: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL_TYPE_INFO = 23
TI_GET_UDTKIND: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL_TYPE_INFO = 24
TI_IS_EQUIV_TO: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL_TYPE_INFO = 25
TI_GET_CALLING_CONVENTION: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL_TYPE_INFO = 26
TI_IS_CLOSE_EQUIV_TO: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL_TYPE_INFO = 27
TI_GTIEX_REQS_VALID: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL_TYPE_INFO = 28
TI_GET_VIRTUALBASEOFFSET: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL_TYPE_INFO = 29
TI_GET_VIRTUALBASEDISPINDEX: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL_TYPE_INFO = 30
TI_GET_IS_REFERENCE: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL_TYPE_INFO = 31
TI_GET_INDIRECTVIRTUALBASECLASS: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL_TYPE_INFO = 32
TI_GET_VIRTUALBASETABLETYPE: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL_TYPE_INFO = 33
TI_GET_OBJECTPOINTERTYPE: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL_TYPE_INFO = 34
IMAGEHLP_SYMBOL_TYPE_INFO_MAX: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGEHLP_SYMBOL_TYPE_INFO = 35
class IMAGE_ARM64_RUNTIME_FUNCTION_ENTRY(Structure):
    BeginAddress: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        UnwindData: UInt32
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            Flag: Annotated[UInt32, 2]
            FunctionLength: Annotated[UInt32, 11]
            RegF: Annotated[UInt32, 3]
            RegI: Annotated[UInt32, 4]
            H: Annotated[UInt32, 1]
            CR: Annotated[UInt32, 2]
            FrameSize: Annotated[UInt32, 9]
class IMAGE_COFF_SYMBOLS_HEADER(Structure):
    NumberOfSymbols: UInt32
    LvaToFirstSymbol: UInt32
    NumberOfLinenumbers: UInt32
    LvaToFirstLinenumber: UInt32
    RvaToFirstByteOfCode: UInt32
    RvaToLastByteOfCode: UInt32
    RvaToFirstByteOfData: UInt32
    RvaToLastByteOfData: UInt32
class IMAGE_COR20_HEADER(Structure):
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
    class _Anonymous_e__Union(Union):
        EntryPointToken: UInt32
        EntryPointRVA: UInt32
class IMAGE_DATA_DIRECTORY(Structure):
    VirtualAddress: UInt32
    Size: UInt32
class IMAGE_DEBUG_DIRECTORY(Structure):
    Characteristics: UInt32
    TimeDateStamp: UInt32
    MajorVersion: UInt16
    MinorVersion: UInt16
    Type: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DEBUG_TYPE
    SizeOfData: UInt32
    AddressOfRawData: UInt32
    PointerToRawData: UInt32
if ARCH in 'X86':
    class IMAGE_DEBUG_INFORMATION(Structure):
        List: win32more.Windows.Win32.System.Kernel.LIST_ENTRY
        ReservedSize: UInt32
        ReservedMappedBase: VoidPtr
        ReservedMachine: UInt16
        ReservedCharacteristics: UInt16
        ReservedCheckSum: UInt32
        ImageBase: UInt32
        SizeOfImage: UInt32
        ReservedNumberOfSections: UInt32
        ReservedSections: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_HEADER)
        ReservedExportedNamesSize: UInt32
        ReservedExportedNames: win32more.Windows.Win32.Foundation.PSTR
        ReservedNumberOfFunctionTableEntries: UInt32
        ReservedFunctionTableEntries: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_FUNCTION_ENTRY)
        ReservedLowestFunctionStartingAddress: UInt32
        ReservedHighestFunctionEndingAddress: UInt32
        ReservedNumberOfFpoTableEntries: UInt32
        ReservedFpoTableEntries: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.FPO_DATA)
        SizeOfCoffSymbols: UInt32
        CoffSymbols: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_COFF_SYMBOLS_HEADER)
        ReservedSizeOfCodeViewSymbols: UInt32
        ReservedCodeViewSymbols: VoidPtr
        ImageFilePath: win32more.Windows.Win32.Foundation.PSTR
        ImageFileName: win32more.Windows.Win32.Foundation.PSTR
        ReservedDebugFilePath: win32more.Windows.Win32.Foundation.PSTR
        ReservedTimeDateStamp: UInt32
        ReservedRomImage: win32more.Windows.Win32.Foundation.BOOL
        ReservedDebugDirectory: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DEBUG_DIRECTORY)
        ReservedNumberOfDebugDirectories: UInt32
        ReservedOriginalFunctionTableBaseAddress: UInt32
        Reserved: UInt32 * 2
IMAGE_DEBUG_TYPE = UInt32
IMAGE_DEBUG_TYPE_UNKNOWN: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DEBUG_TYPE = 0
IMAGE_DEBUG_TYPE_COFF: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DEBUG_TYPE = 1
IMAGE_DEBUG_TYPE_CODEVIEW: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DEBUG_TYPE = 2
IMAGE_DEBUG_TYPE_FPO: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DEBUG_TYPE = 3
IMAGE_DEBUG_TYPE_MISC: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DEBUG_TYPE = 4
IMAGE_DEBUG_TYPE_EXCEPTION: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DEBUG_TYPE = 5
IMAGE_DEBUG_TYPE_FIXUP: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DEBUG_TYPE = 6
IMAGE_DEBUG_TYPE_BORLAND: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DEBUG_TYPE = 9
IMAGE_DIRECTORY_ENTRY = UInt16
IMAGE_DIRECTORY_ENTRY_ARCHITECTURE: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DIRECTORY_ENTRY = 7
IMAGE_DIRECTORY_ENTRY_BASERELOC: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DIRECTORY_ENTRY = 5
IMAGE_DIRECTORY_ENTRY_BOUND_IMPORT: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DIRECTORY_ENTRY = 11
IMAGE_DIRECTORY_ENTRY_COM_DESCRIPTOR: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DIRECTORY_ENTRY = 14
IMAGE_DIRECTORY_ENTRY_DEBUG: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DIRECTORY_ENTRY = 6
IMAGE_DIRECTORY_ENTRY_DELAY_IMPORT: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DIRECTORY_ENTRY = 13
IMAGE_DIRECTORY_ENTRY_EXCEPTION: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DIRECTORY_ENTRY = 3
IMAGE_DIRECTORY_ENTRY_EXPORT: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DIRECTORY_ENTRY = 0
IMAGE_DIRECTORY_ENTRY_GLOBALPTR: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DIRECTORY_ENTRY = 8
IMAGE_DIRECTORY_ENTRY_IAT: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DIRECTORY_ENTRY = 12
IMAGE_DIRECTORY_ENTRY_IMPORT: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DIRECTORY_ENTRY = 1
IMAGE_DIRECTORY_ENTRY_LOAD_CONFIG: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DIRECTORY_ENTRY = 10
IMAGE_DIRECTORY_ENTRY_RESOURCE: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DIRECTORY_ENTRY = 2
IMAGE_DIRECTORY_ENTRY_SECURITY: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DIRECTORY_ENTRY = 4
IMAGE_DIRECTORY_ENTRY_TLS: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DIRECTORY_ENTRY = 9
IMAGE_DLL_CHARACTERISTICS = UInt16
IMAGE_DLLCHARACTERISTICS_HIGH_ENTROPY_VA: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DLL_CHARACTERISTICS = 32
IMAGE_DLLCHARACTERISTICS_DYNAMIC_BASE: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DLL_CHARACTERISTICS = 64
IMAGE_DLLCHARACTERISTICS_FORCE_INTEGRITY: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DLL_CHARACTERISTICS = 128
IMAGE_DLLCHARACTERISTICS_NX_COMPAT: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DLL_CHARACTERISTICS = 256
IMAGE_DLLCHARACTERISTICS_NO_ISOLATION: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DLL_CHARACTERISTICS = 512
IMAGE_DLLCHARACTERISTICS_NO_SEH: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DLL_CHARACTERISTICS = 1024
IMAGE_DLLCHARACTERISTICS_NO_BIND: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DLL_CHARACTERISTICS = 2048
IMAGE_DLLCHARACTERISTICS_APPCONTAINER: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DLL_CHARACTERISTICS = 4096
IMAGE_DLLCHARACTERISTICS_WDM_DRIVER: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DLL_CHARACTERISTICS = 8192
IMAGE_DLLCHARACTERISTICS_GUARD_CF: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DLL_CHARACTERISTICS = 16384
IMAGE_DLLCHARACTERISTICS_TERMINAL_SERVER_AWARE: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DLL_CHARACTERISTICS = 32768
IMAGE_DLLCHARACTERISTICS_EX_CET_COMPAT: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DLL_CHARACTERISTICS = 1
IMAGE_DLLCHARACTERISTICS_EX_CET_COMPAT_STRICT_MODE: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DLL_CHARACTERISTICS = 2
IMAGE_DLLCHARACTERISTICS_EX_CET_SET_CONTEXT_IP_VALIDATION_RELAXED_MODE: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DLL_CHARACTERISTICS = 4
IMAGE_DLLCHARACTERISTICS_EX_CET_DYNAMIC_APIS_ALLOW_IN_PROC: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DLL_CHARACTERISTICS = 8
IMAGE_DLLCHARACTERISTICS_EX_CET_RESERVED_1: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DLL_CHARACTERISTICS = 16
IMAGE_DLLCHARACTERISTICS_EX_CET_RESERVED_2: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_DLL_CHARACTERISTICS = 32
IMAGE_FILE_CHARACTERISTICS = UInt16
IMAGE_FILE_RELOCS_STRIPPED: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_FILE_CHARACTERISTICS = 1
IMAGE_FILE_EXECUTABLE_IMAGE: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_FILE_CHARACTERISTICS = 2
IMAGE_FILE_LINE_NUMS_STRIPPED: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_FILE_CHARACTERISTICS = 4
IMAGE_FILE_LOCAL_SYMS_STRIPPED: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_FILE_CHARACTERISTICS = 8
IMAGE_FILE_AGGRESIVE_WS_TRIM: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_FILE_CHARACTERISTICS = 16
IMAGE_FILE_LARGE_ADDRESS_AWARE: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_FILE_CHARACTERISTICS = 32
IMAGE_FILE_BYTES_REVERSED_LO: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_FILE_CHARACTERISTICS = 128
IMAGE_FILE_32BIT_MACHINE: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_FILE_CHARACTERISTICS = 256
IMAGE_FILE_DEBUG_STRIPPED: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_FILE_CHARACTERISTICS = 512
IMAGE_FILE_REMOVABLE_RUN_FROM_SWAP: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_FILE_CHARACTERISTICS = 1024
IMAGE_FILE_NET_RUN_FROM_SWAP: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_FILE_CHARACTERISTICS = 2048
IMAGE_FILE_SYSTEM: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_FILE_CHARACTERISTICS = 4096
IMAGE_FILE_DLL: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_FILE_CHARACTERISTICS = 8192
IMAGE_FILE_UP_SYSTEM_ONLY: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_FILE_CHARACTERISTICS = 16384
IMAGE_FILE_BYTES_REVERSED_HI: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_FILE_CHARACTERISTICS = 32768
IMAGE_FILE_CHARACTERISTICS2 = UInt32
IMAGE_FILE_RELOCS_STRIPPED2: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_FILE_CHARACTERISTICS2 = 1
IMAGE_FILE_EXECUTABLE_IMAGE2: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_FILE_CHARACTERISTICS2 = 2
IMAGE_FILE_LINE_NUMS_STRIPPED2: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_FILE_CHARACTERISTICS2 = 4
IMAGE_FILE_LOCAL_SYMS_STRIPPED2: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_FILE_CHARACTERISTICS2 = 8
IMAGE_FILE_AGGRESIVE_WS_TRIM2: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_FILE_CHARACTERISTICS2 = 16
IMAGE_FILE_LARGE_ADDRESS_AWARE2: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_FILE_CHARACTERISTICS2 = 32
IMAGE_FILE_BYTES_REVERSED_LO2: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_FILE_CHARACTERISTICS2 = 128
IMAGE_FILE_32BIT_MACHINE2: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_FILE_CHARACTERISTICS2 = 256
IMAGE_FILE_DEBUG_STRIPPED2: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_FILE_CHARACTERISTICS2 = 512
IMAGE_FILE_REMOVABLE_RUN_FROM_SWAP2: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_FILE_CHARACTERISTICS2 = 1024
IMAGE_FILE_NET_RUN_FROM_SWAP2: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_FILE_CHARACTERISTICS2 = 2048
IMAGE_FILE_SYSTEM_2: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_FILE_CHARACTERISTICS2 = 4096
IMAGE_FILE_DLL_2: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_FILE_CHARACTERISTICS2 = 8192
IMAGE_FILE_UP_SYSTEM_ONLY_2: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_FILE_CHARACTERISTICS2 = 16384
IMAGE_FILE_BYTES_REVERSED_HI_2: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_FILE_CHARACTERISTICS2 = 32768
class IMAGE_FILE_HEADER(Structure):
    Machine: win32more.Windows.Win32.System.SystemInformation.IMAGE_FILE_MACHINE
    NumberOfSections: UInt16
    TimeDateStamp: UInt32
    PointerToSymbolTable: UInt32
    NumberOfSymbols: UInt32
    SizeOfOptionalHeader: UInt16
    Characteristics: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_FILE_CHARACTERISTICS
class IMAGE_FUNCTION_ENTRY(Structure):
    StartingAddress: UInt32
    EndingAddress: UInt32
    EndOfPrologue: UInt32
class IMAGE_FUNCTION_ENTRY64(Structure):
    StartingAddress: UInt64
    EndingAddress: UInt64
    Anonymous: _Anonymous_e__Union
    _pack_ = 4
    class _Anonymous_e__Union(Union):
        EndOfPrologue: UInt64
        UnwindInfoAddress: UInt64
        _pack_ = 4
class IMAGE_LOAD_CONFIG_CODE_INTEGRITY(Structure):
    Flags: UInt16
    Catalog: UInt16
    CatalogOffset: UInt32
    Reserved: UInt32
class IMAGE_LOAD_CONFIG_DIRECTORY32(Structure):
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
class IMAGE_LOAD_CONFIG_DIRECTORY64(Structure):
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
class IMAGE_NT_HEADERS32(Structure):
    Signature: UInt32
    FileHeader: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_FILE_HEADER
    OptionalHeader: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_OPTIONAL_HEADER32
class IMAGE_NT_HEADERS64(Structure):
    Signature: UInt32
    FileHeader: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_FILE_HEADER
    OptionalHeader: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_OPTIONAL_HEADER64
class IMAGE_OPTIONAL_HEADER32(Structure):
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
class IMAGE_OPTIONAL_HEADER64(Structure):
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
IMAGE_NT_OPTIONAL_HDR_MAGIC: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_OPTIONAL_HEADER_MAGIC = 523
IMAGE_NT_OPTIONAL_HDR32_MAGIC: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_OPTIONAL_HEADER_MAGIC = 267
IMAGE_NT_OPTIONAL_HDR64_MAGIC: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_OPTIONAL_HEADER_MAGIC = 523
IMAGE_ROM_OPTIONAL_HDR_MAGIC: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_OPTIONAL_HEADER_MAGIC = 263
class IMAGE_ROM_HEADERS(Structure):
    FileHeader: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_FILE_HEADER
    OptionalHeader: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_ROM_OPTIONAL_HEADER
class IMAGE_ROM_OPTIONAL_HEADER(Structure):
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
class IMAGE_RUNTIME_FUNCTION_ENTRY(Structure):
    BeginAddress: UInt32
    EndAddress: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        UnwindInfoAddress: UInt32
        UnwindData: UInt32
IMAGE_SECTION_CHARACTERISTICS = UInt32
IMAGE_SCN_TYPE_NO_PAD: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_CHARACTERISTICS = 8
IMAGE_SCN_CNT_CODE: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_CHARACTERISTICS = 32
IMAGE_SCN_CNT_INITIALIZED_DATA: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_CHARACTERISTICS = 64
IMAGE_SCN_CNT_UNINITIALIZED_DATA: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_CHARACTERISTICS = 128
IMAGE_SCN_LNK_OTHER: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_CHARACTERISTICS = 256
IMAGE_SCN_LNK_INFO: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_CHARACTERISTICS = 512
IMAGE_SCN_LNK_REMOVE: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_CHARACTERISTICS = 2048
IMAGE_SCN_LNK_COMDAT: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_CHARACTERISTICS = 4096
IMAGE_SCN_NO_DEFER_SPEC_EXC: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_CHARACTERISTICS = 16384
IMAGE_SCN_GPREL: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_CHARACTERISTICS = 32768
IMAGE_SCN_MEM_FARDATA: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_CHARACTERISTICS = 32768
IMAGE_SCN_MEM_PURGEABLE: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_CHARACTERISTICS = 131072
IMAGE_SCN_MEM_16BIT: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_CHARACTERISTICS = 131072
IMAGE_SCN_MEM_LOCKED: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_CHARACTERISTICS = 262144
IMAGE_SCN_MEM_PRELOAD: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_CHARACTERISTICS = 524288
IMAGE_SCN_ALIGN_1BYTES: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_CHARACTERISTICS = 1048576
IMAGE_SCN_ALIGN_2BYTES: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_CHARACTERISTICS = 2097152
IMAGE_SCN_ALIGN_4BYTES: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_CHARACTERISTICS = 3145728
IMAGE_SCN_ALIGN_8BYTES: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_CHARACTERISTICS = 4194304
IMAGE_SCN_ALIGN_16BYTES: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_CHARACTERISTICS = 5242880
IMAGE_SCN_ALIGN_32BYTES: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_CHARACTERISTICS = 6291456
IMAGE_SCN_ALIGN_64BYTES: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_CHARACTERISTICS = 7340032
IMAGE_SCN_ALIGN_128BYTES: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_CHARACTERISTICS = 8388608
IMAGE_SCN_ALIGN_256BYTES: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_CHARACTERISTICS = 9437184
IMAGE_SCN_ALIGN_512BYTES: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_CHARACTERISTICS = 10485760
IMAGE_SCN_ALIGN_1024BYTES: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_CHARACTERISTICS = 11534336
IMAGE_SCN_ALIGN_2048BYTES: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_CHARACTERISTICS = 12582912
IMAGE_SCN_ALIGN_4096BYTES: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_CHARACTERISTICS = 13631488
IMAGE_SCN_ALIGN_8192BYTES: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_CHARACTERISTICS = 14680064
IMAGE_SCN_ALIGN_MASK: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_CHARACTERISTICS = 15728640
IMAGE_SCN_LNK_NRELOC_OVFL: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_CHARACTERISTICS = 16777216
IMAGE_SCN_MEM_DISCARDABLE: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_CHARACTERISTICS = 33554432
IMAGE_SCN_MEM_NOT_CACHED: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_CHARACTERISTICS = 67108864
IMAGE_SCN_MEM_NOT_PAGED: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_CHARACTERISTICS = 134217728
IMAGE_SCN_MEM_SHARED: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_CHARACTERISTICS = 268435456
IMAGE_SCN_MEM_EXECUTE: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_CHARACTERISTICS = 536870912
IMAGE_SCN_MEM_READ: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_CHARACTERISTICS = 1073741824
IMAGE_SCN_MEM_WRITE: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_CHARACTERISTICS = 2147483648
IMAGE_SCN_SCALE_INDEX: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_CHARACTERISTICS = 1
class IMAGE_SECTION_HEADER(Structure):
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
    class _Misc_e__Union(Union):
        PhysicalAddress: UInt32
        VirtualSize: UInt32
IMAGE_SUBSYSTEM = UInt16
IMAGE_SUBSYSTEM_UNKNOWN: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SUBSYSTEM = 0
IMAGE_SUBSYSTEM_NATIVE: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SUBSYSTEM = 1
IMAGE_SUBSYSTEM_WINDOWS_GUI: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SUBSYSTEM = 2
IMAGE_SUBSYSTEM_WINDOWS_CUI: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SUBSYSTEM = 3
IMAGE_SUBSYSTEM_OS2_CUI: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SUBSYSTEM = 5
IMAGE_SUBSYSTEM_POSIX_CUI: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SUBSYSTEM = 7
IMAGE_SUBSYSTEM_NATIVE_WINDOWS: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SUBSYSTEM = 8
IMAGE_SUBSYSTEM_WINDOWS_CE_GUI: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SUBSYSTEM = 9
IMAGE_SUBSYSTEM_EFI_APPLICATION: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SUBSYSTEM = 10
IMAGE_SUBSYSTEM_EFI_BOOT_SERVICE_DRIVER: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SUBSYSTEM = 11
IMAGE_SUBSYSTEM_EFI_RUNTIME_DRIVER: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SUBSYSTEM = 12
IMAGE_SUBSYSTEM_EFI_ROM: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SUBSYSTEM = 13
IMAGE_SUBSYSTEM_XBOX: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SUBSYSTEM = 14
IMAGE_SUBSYSTEM_WINDOWS_BOOT_APPLICATION: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SUBSYSTEM = 16
IMAGE_SUBSYSTEM_XBOX_CODE_CATALOG: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SUBSYSTEM = 17
class IObjectSafety(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{cb5bdc81-93c1-11cf-8f20-00805f2cd064}')
    @commethod(3)
    def GetInterfaceSafetyOptions(self, riid: POINTER(Guid), pdwSupportedOptions: POINTER(UInt32), pdwEnabledOptions: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetInterfaceSafetyOptions(self, riid: POINTER(Guid), dwOptionSetMask: UInt32, dwEnabledOptions: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPMI_OS_SEL_RECORD(Structure):
    Signature: UInt32
    Version: UInt32
    Length: UInt32
    RecordType: win32more.Windows.Win32.System.Diagnostics.Debug.IPMI_OS_SEL_RECORD_TYPE
    DataLength: UInt32
    Data: Byte * 1
    _pack_ = 1
IPMI_OS_SEL_RECORD_TYPE = Int32
IpmiOsSelRecordTypeWhea: win32more.Windows.Win32.System.Diagnostics.Debug.IPMI_OS_SEL_RECORD_TYPE = 0
IpmiOsSelRecordTypeOther: win32more.Windows.Win32.System.Diagnostics.Debug.IPMI_OS_SEL_RECORD_TYPE = 1
IpmiOsSelRecordTypeWheaErrorXpfMca: win32more.Windows.Win32.System.Diagnostics.Debug.IPMI_OS_SEL_RECORD_TYPE = 2
IpmiOsSelRecordTypeWheaErrorPci: win32more.Windows.Win32.System.Diagnostics.Debug.IPMI_OS_SEL_RECORD_TYPE = 3
IpmiOsSelRecordTypeWheaErrorNmi: win32more.Windows.Win32.System.Diagnostics.Debug.IPMI_OS_SEL_RECORD_TYPE = 4
IpmiOsSelRecordTypeWheaErrorOther: win32more.Windows.Win32.System.Diagnostics.Debug.IPMI_OS_SEL_RECORD_TYPE = 5
IpmiOsSelRecordTypeRaw: win32more.Windows.Win32.System.Diagnostics.Debug.IPMI_OS_SEL_RECORD_TYPE = 6
IpmiOsSelRecordTypeDriver: win32more.Windows.Win32.System.Diagnostics.Debug.IPMI_OS_SEL_RECORD_TYPE = 7
IpmiOsSelRecordTypeBugcheckRecovery: win32more.Windows.Win32.System.Diagnostics.Debug.IPMI_OS_SEL_RECORD_TYPE = 8
IpmiOsSelRecordTypeBugcheckData: win32more.Windows.Win32.System.Diagnostics.Debug.IPMI_OS_SEL_RECORD_TYPE = 9
IpmiOsSelRecordTypeMax: win32more.Windows.Win32.System.Diagnostics.Debug.IPMI_OS_SEL_RECORD_TYPE = 10
class IPerPropertyBrowsing2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51973c54-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(3)
    def GetDisplayString(self, dispid: Int32, pBstr: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def MapPropertyToPage(self, dispid: Int32, pClsidPropPage: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPredefinedStrings(self, dispid: Int32, pCaStrings: POINTER(win32more.Windows.Win32.System.Ole.CALPOLESTR), pCaCookies: POINTER(win32more.Windows.Win32.System.Ole.CADWORD)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetPredefinedValue(self, dispid: Int32, dwCookie: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X86':
    class KDHELP(Structure):
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
class KDHELP64(Structure):
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
if ARCH in 'ARM64':
    class KNONVOLATILE_CONTEXT_POINTERS(Structure):
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
elif ARCH in 'X64':
    class KNONVOLATILE_CONTEXT_POINTERS(Structure):
        Anonymous1: _Anonymous1_e__Union
        Anonymous2: _Anonymous2_e__Union
        class _Anonymous1_e__Union(Union):
            FloatingContext: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.M128A) * 16
            Anonymous: _Anonymous_e__Struct
            class _Anonymous_e__Struct(Structure):
                Xmm0: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.M128A)
                Xmm1: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.M128A)
                Xmm2: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.M128A)
                Xmm3: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.M128A)
                Xmm4: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.M128A)
                Xmm5: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.M128A)
                Xmm6: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.M128A)
                Xmm7: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.M128A)
                Xmm8: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.M128A)
                Xmm9: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.M128A)
                Xmm10: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.M128A)
                Xmm11: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.M128A)
                Xmm12: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.M128A)
                Xmm13: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.M128A)
                Xmm14: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.M128A)
                Xmm15: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.M128A)
        class _Anonymous2_e__Union(Union):
            IntegerContext: POINTER(UInt64) * 16
            Anonymous: _Anonymous_e__Struct
            class _Anonymous_e__Struct(Structure):
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
elif ARCH in 'X86':
    class KNONVOLATILE_CONTEXT_POINTERS(Structure):
        Dummy: UInt32
class LDT_ENTRY(Structure):
    LimitLow: UInt16
    BaseLow: UInt16
    HighWord: _HighWord_e__Union
    class _HighWord_e__Union(Union):
        Bytes: _Bytes_e__Struct
        Bits: _Bits_e__Struct
        class _Bytes_e__Struct(Structure):
            BaseMid: Byte
            Flags1: Byte
            Flags2: Byte
            BaseHi: Byte
        class _Bits_e__Struct(Structure):
            BaseMid: Annotated[UInt32, 8]
            Type: Annotated[UInt32, 5]
            Dpl: Annotated[UInt32, 2]
            Pres: Annotated[UInt32, 1]
            LimitHi: Annotated[UInt32, 4]
            Sys: Annotated[UInt32, 1]
            Reserved_0: Annotated[UInt32, 1]
            Default_Big: Annotated[UInt32, 1]
            Granularity: Annotated[UInt32, 1]
            BaseHi: Annotated[UInt32, 8]
if ARCH in 'X64,ARM64':
    class LOADED_IMAGE(Structure):
        ModuleName: win32more.Windows.Win32.Foundation.PSTR
        hFile: win32more.Windows.Win32.Foundation.HANDLE
        MappedAddress: POINTER(Byte)
        FileHeader: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_NT_HEADERS64)
        LastRvaSection: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_HEADER)
        NumberOfSections: UInt32
        Sections: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_HEADER)
        Characteristics: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_FILE_CHARACTERISTICS2
        fSystemImage: win32more.Windows.Win32.Foundation.BOOLEAN
        fDOSImage: win32more.Windows.Win32.Foundation.BOOLEAN
        fReadOnly: win32more.Windows.Win32.Foundation.BOOLEAN
        Version: Byte
        Links: win32more.Windows.Win32.System.Kernel.LIST_ENTRY
        SizeOfImage: UInt32
elif ARCH in 'X86':
    class LOADED_IMAGE(Structure):
        ModuleName: win32more.Windows.Win32.Foundation.PSTR
        hFile: win32more.Windows.Win32.Foundation.HANDLE
        MappedAddress: POINTER(Byte)
        FileHeader: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_NT_HEADERS32)
        LastRvaSection: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_HEADER)
        NumberOfSections: UInt32
        Sections: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_SECTION_HEADER)
        Characteristics: win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_FILE_CHARACTERISTICS2
        fSystemImage: win32more.Windows.Win32.Foundation.BOOLEAN
        fDOSImage: win32more.Windows.Win32.Foundation.BOOLEAN
        fReadOnly: win32more.Windows.Win32.Foundation.BOOLEAN
        Version: Byte
        Links: win32more.Windows.Win32.System.Kernel.LIST_ENTRY
        SizeOfImage: UInt32
class LOAD_DLL_DEBUG_INFO(Structure):
    hFile: win32more.Windows.Win32.Foundation.HANDLE
    lpBaseOfDll: VoidPtr
    dwDebugInfoFileOffset: UInt32
    nDebugInfoSize: UInt32
    lpImageName: VoidPtr
    fUnicode: UInt16
@winfunctype_pointer
def LPCALL_BACK_USER_INTERRUPT_ROUTINE() -> UInt32: ...
@winfunctype_pointer
def LPTOP_LEVEL_EXCEPTION_FILTER(ExceptionInfo: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.EXCEPTION_POINTERS)) -> Int32: ...
class M128A(Structure):
    Low: UInt64
    High: Int64
if ARCH in 'X64,ARM64':
    class MINIDUMP_CALLBACK_INFORMATION(Structure):
        CallbackRoutine: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_CALLBACK_ROUTINE
        CallbackParam: VoidPtr
        _pack_ = 4
elif ARCH in 'X86':
    class MINIDUMP_CALLBACK_INFORMATION(Structure):
        CallbackRoutine: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_CALLBACK_ROUTINE
        CallbackParam: VoidPtr
class MINIDUMP_CALLBACK_INPUT(Structure):
    ProcessId: UInt32
    ProcessHandle: win32more.Windows.Win32.Foundation.HANDLE
    CallbackType: UInt32
    Anonymous: _Anonymous_e__Union
    _pack_ = 4
    class _Anonymous_e__Union(Union):
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
class MINIDUMP_CALLBACK_OUTPUT(Structure):
    Anonymous: _Anonymous_e__Union
    _pack_ = 4
    class _Anonymous_e__Union(Union):
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
        class _Anonymous1_e__Struct(Structure):
            MemoryBase: UInt64
            MemorySize: UInt32
            _pack_ = 4
        class _Anonymous2_e__Struct(Structure):
            CheckCancel: win32more.Windows.Win32.Foundation.BOOL
            Cancel: win32more.Windows.Win32.Foundation.BOOL
        class _Anonymous3_e__Struct(Structure):
            VmRegion: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_MEMORY_INFO
            Continue: win32more.Windows.Win32.Foundation.BOOL
        class _Anonymous4_e__Struct(Structure):
            VmQueryStatus: win32more.Windows.Win32.Foundation.HRESULT
            VmQueryResult: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_MEMORY_INFO
        class _Anonymous5_e__Struct(Structure):
            VmReadStatus: win32more.Windows.Win32.Foundation.HRESULT
            VmReadBytesCompleted: UInt32
@winfunctype_pointer
def MINIDUMP_CALLBACK_ROUTINE(CallbackParam: VoidPtr, CallbackInput: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_CALLBACK_INPUT), CallbackOutput: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_CALLBACK_OUTPUT)) -> win32more.Windows.Win32.Foundation.BOOL: ...
MINIDUMP_CALLBACK_TYPE = Int32
ModuleCallback: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_CALLBACK_TYPE = 0
ThreadCallback: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_CALLBACK_TYPE = 1
ThreadExCallback: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_CALLBACK_TYPE = 2
IncludeThreadCallback: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_CALLBACK_TYPE = 3
IncludeModuleCallback: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_CALLBACK_TYPE = 4
MemoryCallback: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_CALLBACK_TYPE = 5
CancelCallback: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_CALLBACK_TYPE = 6
WriteKernelMinidumpCallback: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_CALLBACK_TYPE = 7
KernelMinidumpStatusCallback: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_CALLBACK_TYPE = 8
RemoveMemoryCallback: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_CALLBACK_TYPE = 9
IncludeVmRegionCallback: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_CALLBACK_TYPE = 10
IoStartCallback: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_CALLBACK_TYPE = 11
IoWriteAllCallback: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_CALLBACK_TYPE = 12
IoFinishCallback: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_CALLBACK_TYPE = 13
ReadMemoryFailureCallback: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_CALLBACK_TYPE = 14
SecondaryFlagsCallback: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_CALLBACK_TYPE = 15
IsProcessSnapshotCallback: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_CALLBACK_TYPE = 16
VmStartCallback: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_CALLBACK_TYPE = 17
VmQueryCallback: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_CALLBACK_TYPE = 18
VmPreReadCallback: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_CALLBACK_TYPE = 19
VmPostReadCallback: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_CALLBACK_TYPE = 20
class MINIDUMP_DIRECTORY(Structure):
    StreamType: UInt32
    Location: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_LOCATION_DESCRIPTOR
    _pack_ = 4
class MINIDUMP_EXCEPTION(Structure):
    ExceptionCode: UInt32
    ExceptionFlags: UInt32
    ExceptionRecord: UInt64
    ExceptionAddress: UInt64
    NumberParameters: UInt32
    __unusedAlignment: UInt32
    ExceptionInformation: UInt64 * 15
    _pack_ = 4
if ARCH in 'X64,ARM64':
    class MINIDUMP_EXCEPTION_INFORMATION(Structure):
        ThreadId: UInt32
        ExceptionPointers: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.EXCEPTION_POINTERS)
        ClientPointers: win32more.Windows.Win32.Foundation.BOOL
        _pack_ = 4
elif ARCH in 'X86':
    class MINIDUMP_EXCEPTION_INFORMATION(Structure):
        ThreadId: UInt32
        ExceptionPointers: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.EXCEPTION_POINTERS)
        ClientPointers: win32more.Windows.Win32.Foundation.BOOL
class MINIDUMP_EXCEPTION_INFORMATION64(Structure):
    ThreadId: UInt32
    ExceptionRecord: UInt64
    ContextRecord: UInt64
    ClientPointers: win32more.Windows.Win32.Foundation.BOOL
    _pack_ = 4
class MINIDUMP_EXCEPTION_STREAM(Structure):
    ThreadId: UInt32
    __alignment: UInt32
    ExceptionRecord: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_EXCEPTION
    ThreadContext: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_LOCATION_DESCRIPTOR
    _pack_ = 4
class MINIDUMP_FUNCTION_TABLE_DESCRIPTOR(Structure):
    MinimumAddress: UInt64
    MaximumAddress: UInt64
    BaseAddress: UInt64
    EntryCount: UInt32
    SizeOfAlignPad: UInt32
    _pack_ = 4
class MINIDUMP_FUNCTION_TABLE_STREAM(Structure):
    SizeOfHeader: UInt32
    SizeOfDescriptor: UInt32
    SizeOfNativeDescriptor: UInt32
    SizeOfFunctionEntry: UInt32
    NumberOfDescriptors: UInt32
    SizeOfAlignPad: UInt32
    _pack_ = 4
class MINIDUMP_HANDLE_DATA_STREAM(Structure):
    SizeOfHeader: UInt32
    SizeOfDescriptor: UInt32
    NumberOfDescriptors: UInt32
    Reserved: UInt32
    _pack_ = 4
class MINIDUMP_HANDLE_DESCRIPTOR(Structure):
    Handle: UInt64
    TypeNameRva: UInt32
    ObjectNameRva: UInt32
    Attributes: UInt32
    GrantedAccess: UInt32
    HandleCount: UInt32
    PointerCount: UInt32
    _pack_ = 4
class MINIDUMP_HANDLE_DESCRIPTOR_2(Structure):
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
class MINIDUMP_HANDLE_OBJECT_INFORMATION(Structure):
    NextInfoRva: UInt32
    InfoType: UInt32
    SizeOfInfo: UInt32
    _pack_ = 4
MINIDUMP_HANDLE_OBJECT_INFORMATION_TYPE = Int32
MiniHandleObjectInformationNone: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_HANDLE_OBJECT_INFORMATION_TYPE = 0
MiniThreadInformation1: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_HANDLE_OBJECT_INFORMATION_TYPE = 1
MiniMutantInformation1: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_HANDLE_OBJECT_INFORMATION_TYPE = 2
MiniMutantInformation2: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_HANDLE_OBJECT_INFORMATION_TYPE = 3
MiniProcessInformation1: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_HANDLE_OBJECT_INFORMATION_TYPE = 4
MiniProcessInformation2: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_HANDLE_OBJECT_INFORMATION_TYPE = 5
MiniEventInformation1: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_HANDLE_OBJECT_INFORMATION_TYPE = 6
MiniSectionInformation1: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_HANDLE_OBJECT_INFORMATION_TYPE = 7
MiniSemaphoreInformation1: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_HANDLE_OBJECT_INFORMATION_TYPE = 8
MiniHandleObjectInformationTypeMax: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_HANDLE_OBJECT_INFORMATION_TYPE = 9
class MINIDUMP_HANDLE_OPERATION_LIST(Structure):
    SizeOfHeader: UInt32
    SizeOfEntry: UInt32
    NumberOfEntries: UInt32
    Reserved: UInt32
    _pack_ = 4
class MINIDUMP_HEADER(Structure):
    Signature: UInt32
    Version: UInt32
    NumberOfStreams: UInt32
    StreamDirectoryRva: UInt32
    CheckSum: UInt32
    Anonymous: _Anonymous_e__Union
    Flags: UInt64
    _pack_ = 4
    class _Anonymous_e__Union(Union):
        Reserved: UInt32
        TimeDateStamp: UInt32
class MINIDUMP_INCLUDE_MODULE_CALLBACK(Structure):
    BaseOfImage: UInt64
    _pack_ = 4
class MINIDUMP_INCLUDE_THREAD_CALLBACK(Structure):
    ThreadId: UInt32
    _pack_ = 4
class MINIDUMP_IO_CALLBACK(Structure):
    Handle: win32more.Windows.Win32.Foundation.HANDLE
    Offset: UInt64
    Buffer: VoidPtr
    BufferBytes: UInt32
    _pack_ = 4
class MINIDUMP_LOCATION_DESCRIPTOR(Structure):
    DataSize: UInt32
    Rva: UInt32
    _pack_ = 4
class MINIDUMP_LOCATION_DESCRIPTOR64(Structure):
    DataSize: UInt64
    Rva: UInt64
    _pack_ = 4
class MINIDUMP_MEMORY64_LIST(Structure):
    NumberOfMemoryRanges: UInt64
    BaseRva: UInt64
    MemoryRanges: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_MEMORY_DESCRIPTOR64 * 1
    _pack_ = 4
class MINIDUMP_MEMORY_DESCRIPTOR(Structure):
    StartOfMemoryRange: UInt64
    Memory: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_LOCATION_DESCRIPTOR
    _pack_ = 4
class MINIDUMP_MEMORY_DESCRIPTOR64(Structure):
    StartOfMemoryRange: UInt64
    DataSize: UInt64
    _pack_ = 4
class MINIDUMP_MEMORY_INFO(Structure):
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
class MINIDUMP_MEMORY_INFO_LIST(Structure):
    SizeOfHeader: UInt32
    SizeOfEntry: UInt32
    NumberOfEntries: UInt64
    _pack_ = 4
class MINIDUMP_MEMORY_LIST(Structure):
    NumberOfMemoryRanges: UInt32
    MemoryRanges: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_MEMORY_DESCRIPTOR * 1
    _pack_ = 4
class MINIDUMP_MISC_INFO(Structure):
    SizeOfInfo: UInt32
    Flags1: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_MISC_INFO_FLAGS
    ProcessId: UInt32
    ProcessCreateTime: UInt32
    ProcessUserTime: UInt32
    ProcessKernelTime: UInt32
    _pack_ = 4
class MINIDUMP_MISC_INFO_2(Structure):
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
class MINIDUMP_MISC_INFO_3(Structure):
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
class MINIDUMP_MISC_INFO_4(Structure):
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
class MINIDUMP_MISC_INFO_5(Structure):
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
MINIDUMP_MISC1_PROCESS_ID: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_MISC_INFO_FLAGS = 1
MINIDUMP_MISC1_PROCESS_TIMES: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_MISC_INFO_FLAGS = 2
class MINIDUMP_MODULE(Structure):
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
class MINIDUMP_MODULE_CALLBACK(Structure):
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
class MINIDUMP_MODULE_LIST(Structure):
    NumberOfModules: UInt32
    Modules: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_MODULE * 1
    _pack_ = 4
class MINIDUMP_PROCESS_VM_COUNTERS_1(Structure):
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
class MINIDUMP_PROCESS_VM_COUNTERS_2(Structure):
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
class MINIDUMP_READ_MEMORY_FAILURE_CALLBACK(Structure):
    Offset: UInt64
    Bytes: UInt32
    FailureStatus: win32more.Windows.Win32.Foundation.HRESULT
    _pack_ = 4
MINIDUMP_SECONDARY_FLAGS = Int32
MiniSecondaryWithoutPowerInfo: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_SECONDARY_FLAGS = 1
MiniSecondaryValidFlags: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_SECONDARY_FLAGS = 1
MINIDUMP_STREAM_TYPE = Int32
UnusedStream: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_STREAM_TYPE = 0
ReservedStream0: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_STREAM_TYPE = 1
ReservedStream1: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_STREAM_TYPE = 2
ThreadListStream: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_STREAM_TYPE = 3
ModuleListStream: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_STREAM_TYPE = 4
MemoryListStream: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_STREAM_TYPE = 5
ExceptionStream: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_STREAM_TYPE = 6
SystemInfoStream: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_STREAM_TYPE = 7
ThreadExListStream: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_STREAM_TYPE = 8
Memory64ListStream: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_STREAM_TYPE = 9
CommentStreamA: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_STREAM_TYPE = 10
CommentStreamW: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_STREAM_TYPE = 11
HandleDataStream: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_STREAM_TYPE = 12
FunctionTableStream: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_STREAM_TYPE = 13
UnloadedModuleListStream: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_STREAM_TYPE = 14
MiscInfoStream: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_STREAM_TYPE = 15
MemoryInfoListStream: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_STREAM_TYPE = 16
ThreadInfoListStream: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_STREAM_TYPE = 17
HandleOperationListStream: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_STREAM_TYPE = 18
TokenStream: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_STREAM_TYPE = 19
JavaScriptDataStream: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_STREAM_TYPE = 20
SystemMemoryInfoStream: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_STREAM_TYPE = 21
ProcessVmCountersStream: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_STREAM_TYPE = 22
IptTraceStream: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_STREAM_TYPE = 23
ThreadNamesStream: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_STREAM_TYPE = 24
ceStreamNull: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_STREAM_TYPE = 32768
ceStreamSystemInfo: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_STREAM_TYPE = 32769
ceStreamException: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_STREAM_TYPE = 32770
ceStreamModuleList: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_STREAM_TYPE = 32771
ceStreamProcessList: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_STREAM_TYPE = 32772
ceStreamThreadList: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_STREAM_TYPE = 32773
ceStreamThreadContextList: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_STREAM_TYPE = 32774
ceStreamThreadCallStackList: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_STREAM_TYPE = 32775
ceStreamMemoryVirtualList: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_STREAM_TYPE = 32776
ceStreamMemoryPhysicalList: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_STREAM_TYPE = 32777
ceStreamBucketParameters: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_STREAM_TYPE = 32778
ceStreamProcessModuleMap: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_STREAM_TYPE = 32779
ceStreamDiagnosisList: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_STREAM_TYPE = 32780
LastReservedStream: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_STREAM_TYPE = 65535
class MINIDUMP_STRING(Structure):
    Length: UInt32
    Buffer: Char * 1
    _pack_ = 4
class MINIDUMP_SYSTEM_BASIC_INFORMATION(Structure):
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
class MINIDUMP_SYSTEM_BASIC_PERFORMANCE_INFORMATION(Structure):
    AvailablePages: UInt64
    CommittedPages: UInt64
    CommitLimit: UInt64
    PeakCommitment: UInt64
    _pack_ = 4
class MINIDUMP_SYSTEM_FILECACHE_INFORMATION(Structure):
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
class MINIDUMP_SYSTEM_INFO(Structure):
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
    class _Anonymous1_e__Union(Union):
        Reserved0: UInt16
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            NumberOfProcessors: Byte
            ProductType: Byte
    class _Anonymous2_e__Union(Union):
        Reserved1: UInt32
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            SuiteMask: UInt16
            Reserved2: UInt16
class MINIDUMP_SYSTEM_MEMORY_INFO_1(Structure):
    Revision: UInt16
    Flags: UInt16
    BasicInfo: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_SYSTEM_BASIC_INFORMATION
    FileCacheInfo: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_SYSTEM_FILECACHE_INFORMATION
    BasicPerfInfo: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_SYSTEM_BASIC_PERFORMANCE_INFORMATION
    PerfInfo: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_SYSTEM_PERFORMANCE_INFORMATION
    _pack_ = 4
class MINIDUMP_SYSTEM_PERFORMANCE_INFORMATION(Structure):
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
class MINIDUMP_THREAD(Structure):
    ThreadId: UInt32
    SuspendCount: UInt32
    PriorityClass: UInt32
    Priority: UInt32
    Teb: UInt64
    Stack: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_MEMORY_DESCRIPTOR
    ThreadContext: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_LOCATION_DESCRIPTOR
    _pack_ = 4
if ARCH in 'ARM64':
    class MINIDUMP_THREAD_CALLBACK(Structure):
        ThreadId: UInt32
        ThreadHandle: win32more.Windows.Win32.Foundation.HANDLE
        Pad: UInt32
        Context: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT
        SizeOfContext: UInt32
        StackBase: UInt64
        StackEnd: UInt64
        _pack_ = 4
elif ARCH in 'X86,X64':
    class MINIDUMP_THREAD_CALLBACK(Structure):
        ThreadId: UInt32
        ThreadHandle: win32more.Windows.Win32.Foundation.HANDLE
        Context: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT
        SizeOfContext: UInt32
        StackBase: UInt64
        StackEnd: UInt64
        _pack_ = 4
class MINIDUMP_THREAD_EX(Structure):
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
    class MINIDUMP_THREAD_EX_CALLBACK(Structure):
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
elif ARCH in 'X86,X64':
    class MINIDUMP_THREAD_EX_CALLBACK(Structure):
        ThreadId: UInt32
        ThreadHandle: win32more.Windows.Win32.Foundation.HANDLE
        Context: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT
        SizeOfContext: UInt32
        StackBase: UInt64
        StackEnd: UInt64
        BackingStoreBase: UInt64
        BackingStoreEnd: UInt64
        _pack_ = 4
class MINIDUMP_THREAD_EX_LIST(Structure):
    NumberOfThreads: UInt32
    Threads: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_THREAD_EX * 1
    _pack_ = 4
class MINIDUMP_THREAD_INFO(Structure):
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
MINIDUMP_THREAD_INFO_ERROR_THREAD: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_THREAD_INFO_DUMP_FLAGS = 1
MINIDUMP_THREAD_INFO_EXITED_THREAD: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_THREAD_INFO_DUMP_FLAGS = 4
MINIDUMP_THREAD_INFO_INVALID_CONTEXT: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_THREAD_INFO_DUMP_FLAGS = 16
MINIDUMP_THREAD_INFO_INVALID_INFO: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_THREAD_INFO_DUMP_FLAGS = 8
MINIDUMP_THREAD_INFO_INVALID_TEB: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_THREAD_INFO_DUMP_FLAGS = 32
MINIDUMP_THREAD_INFO_WRITING_THREAD: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_THREAD_INFO_DUMP_FLAGS = 2
class MINIDUMP_THREAD_INFO_LIST(Structure):
    SizeOfHeader: UInt32
    SizeOfEntry: UInt32
    NumberOfEntries: UInt32
    _pack_ = 4
class MINIDUMP_THREAD_LIST(Structure):
    NumberOfThreads: UInt32
    Threads: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_THREAD * 1
    _pack_ = 4
class MINIDUMP_THREAD_NAME(Structure):
    ThreadId: UInt32
    RvaOfThreadName: UInt64
    _pack_ = 4
class MINIDUMP_THREAD_NAME_LIST(Structure):
    NumberOfThreadNames: UInt32
    ThreadNames: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_THREAD_NAME * 1
    _pack_ = 4
class MINIDUMP_TOKEN_INFO_HEADER(Structure):
    TokenSize: UInt32
    TokenId: UInt32
    TokenHandle: UInt64
    _pack_ = 4
class MINIDUMP_TOKEN_INFO_LIST(Structure):
    TokenListSize: UInt32
    TokenListEntries: UInt32
    ListHeaderSize: UInt32
    ElementHeaderSize: UInt32
    _pack_ = 4
MINIDUMP_TYPE = Int32
MiniDumpNormal: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_TYPE = 0
MiniDumpWithDataSegs: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_TYPE = 1
MiniDumpWithFullMemory: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_TYPE = 2
MiniDumpWithHandleData: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_TYPE = 4
MiniDumpFilterMemory: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_TYPE = 8
MiniDumpScanMemory: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_TYPE = 16
MiniDumpWithUnloadedModules: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_TYPE = 32
MiniDumpWithIndirectlyReferencedMemory: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_TYPE = 64
MiniDumpFilterModulePaths: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_TYPE = 128
MiniDumpWithProcessThreadData: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_TYPE = 256
MiniDumpWithPrivateReadWriteMemory: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_TYPE = 512
MiniDumpWithoutOptionalData: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_TYPE = 1024
MiniDumpWithFullMemoryInfo: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_TYPE = 2048
MiniDumpWithThreadInfo: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_TYPE = 4096
MiniDumpWithCodeSegs: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_TYPE = 8192
MiniDumpWithoutAuxiliaryState: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_TYPE = 16384
MiniDumpWithFullAuxiliaryState: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_TYPE = 32768
MiniDumpWithPrivateWriteCopyMemory: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_TYPE = 65536
MiniDumpIgnoreInaccessibleMemory: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_TYPE = 131072
MiniDumpWithTokenInformation: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_TYPE = 262144
MiniDumpWithModuleHeaders: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_TYPE = 524288
MiniDumpFilterTriage: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_TYPE = 1048576
MiniDumpWithAvxXStateContext: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_TYPE = 2097152
MiniDumpWithIptTrace: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_TYPE = 4194304
MiniDumpScanInaccessiblePartialPages: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_TYPE = 8388608
MiniDumpFilterWriteCombinedMemory: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_TYPE = 16777216
MiniDumpValidTypeFlags: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_TYPE = 33554431
class MINIDUMP_UNLOADED_MODULE(Structure):
    BaseOfImage: UInt64
    SizeOfImage: UInt32
    CheckSum: UInt32
    TimeDateStamp: UInt32
    ModuleNameRva: UInt32
    _pack_ = 4
class MINIDUMP_UNLOADED_MODULE_LIST(Structure):
    SizeOfHeader: UInt32
    SizeOfEntry: UInt32
    NumberOfEntries: UInt32
    _pack_ = 4
class MINIDUMP_USER_RECORD(Structure):
    Type: UInt32
    Memory: win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_LOCATION_DESCRIPTOR
    _pack_ = 4
if ARCH in 'X64,ARM64':
    class MINIDUMP_USER_STREAM(Structure):
        Type: UInt32
        BufferSize: UInt32
        Buffer: VoidPtr
        _pack_ = 4
elif ARCH in 'X86':
    class MINIDUMP_USER_STREAM(Structure):
        Type: UInt32
        BufferSize: UInt32
        Buffer: VoidPtr
if ARCH in 'X64,ARM64':
    class MINIDUMP_USER_STREAM_INFORMATION(Structure):
        UserStreamCount: UInt32
        UserStreamArray: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_USER_STREAM)
        _pack_ = 4
elif ARCH in 'X86':
    class MINIDUMP_USER_STREAM_INFORMATION(Structure):
        UserStreamCount: UInt32
        UserStreamArray: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.MINIDUMP_USER_STREAM)
class MINIDUMP_VM_POST_READ_CALLBACK(Structure):
    Offset: UInt64
    Buffer: VoidPtr
    Size: UInt32
    Completed: UInt32
    Status: win32more.Windows.Win32.Foundation.HRESULT
    _pack_ = 4
class MINIDUMP_VM_PRE_READ_CALLBACK(Structure):
    Offset: UInt64
    Buffer: VoidPtr
    Size: UInt32
    _pack_ = 4
class MINIDUMP_VM_QUERY_CALLBACK(Structure):
    Offset: UInt64
    _pack_ = 4
class MODLOAD_CVMISC(Structure):
    oCV: UInt32
    cCV: UIntPtr
    oMisc: UInt32
    cMisc: UIntPtr
    dtImage: UInt32
    cImage: UInt32
class MODLOAD_DATA(Structure):
    ssize: UInt32
    ssig: win32more.Windows.Win32.System.Diagnostics.Debug.MODLOAD_DATA_TYPE
    data: VoidPtr
    size: UInt32
    flags: UInt32
MODLOAD_DATA_TYPE = UInt32
DBHHEADER_DEBUGDIRS: win32more.Windows.Win32.System.Diagnostics.Debug.MODLOAD_DATA_TYPE = 1
DBHHEADER_CVMISC: win32more.Windows.Win32.System.Diagnostics.Debug.MODLOAD_DATA_TYPE = 2
class MODLOAD_PDBGUID_PDBAGE(Structure):
    PdbGuid: Guid
    PdbAge: UInt32
class MODULE_TYPE_INFO(Structure):
    dataLength: UInt16
    leaf: UInt16
    data: Byte * 1
MODULE_WRITE_FLAGS = Int32
ModuleWriteModule: win32more.Windows.Win32.System.Diagnostics.Debug.MODULE_WRITE_FLAGS = 1
ModuleWriteDataSeg: win32more.Windows.Win32.System.Diagnostics.Debug.MODULE_WRITE_FLAGS = 2
ModuleWriteMiscRecord: win32more.Windows.Win32.System.Diagnostics.Debug.MODULE_WRITE_FLAGS = 4
ModuleWriteCvRecord: win32more.Windows.Win32.System.Diagnostics.Debug.MODULE_WRITE_FLAGS = 8
ModuleReferencedByMemory: win32more.Windows.Win32.System.Diagnostics.Debug.MODULE_WRITE_FLAGS = 16
ModuleWriteTlsData: win32more.Windows.Win32.System.Diagnostics.Debug.MODULE_WRITE_FLAGS = 32
ModuleWriteCodeSegs: win32more.Windows.Win32.System.Diagnostics.Debug.MODULE_WRITE_FLAGS = 64
OBJECT_ATTRIB_FLAGS = Int32
OBJECT_ATTRIB_NO_ATTRIB: win32more.Windows.Win32.System.Diagnostics.Debug.OBJECT_ATTRIB_FLAGS = 0
OBJECT_ATTRIB_NO_NAME: win32more.Windows.Win32.System.Diagnostics.Debug.OBJECT_ATTRIB_FLAGS = 1
OBJECT_ATTRIB_NO_TYPE: win32more.Windows.Win32.System.Diagnostics.Debug.OBJECT_ATTRIB_FLAGS = 2
OBJECT_ATTRIB_NO_VALUE: win32more.Windows.Win32.System.Diagnostics.Debug.OBJECT_ATTRIB_FLAGS = 4
OBJECT_ATTRIB_VALUE_IS_INVALID: win32more.Windows.Win32.System.Diagnostics.Debug.OBJECT_ATTRIB_FLAGS = 8
OBJECT_ATTRIB_VALUE_IS_OBJECT: win32more.Windows.Win32.System.Diagnostics.Debug.OBJECT_ATTRIB_FLAGS = 16
OBJECT_ATTRIB_VALUE_IS_ENUM: win32more.Windows.Win32.System.Diagnostics.Debug.OBJECT_ATTRIB_FLAGS = 32
OBJECT_ATTRIB_VALUE_IS_CUSTOM: win32more.Windows.Win32.System.Diagnostics.Debug.OBJECT_ATTRIB_FLAGS = 64
OBJECT_ATTRIB_OBJECT_IS_EXPANDABLE: win32more.Windows.Win32.System.Diagnostics.Debug.OBJECT_ATTRIB_FLAGS = 112
OBJECT_ATTRIB_VALUE_HAS_CODE: win32more.Windows.Win32.System.Diagnostics.Debug.OBJECT_ATTRIB_FLAGS = 128
OBJECT_ATTRIB_TYPE_IS_OBJECT: win32more.Windows.Win32.System.Diagnostics.Debug.OBJECT_ATTRIB_FLAGS = 256
OBJECT_ATTRIB_TYPE_HAS_CODE: win32more.Windows.Win32.System.Diagnostics.Debug.OBJECT_ATTRIB_FLAGS = 512
OBJECT_ATTRIB_TYPE_IS_EXPANDABLE: win32more.Windows.Win32.System.Diagnostics.Debug.OBJECT_ATTRIB_FLAGS = 256
OBJECT_ATTRIB_SLOT_IS_CATEGORY: win32more.Windows.Win32.System.Diagnostics.Debug.OBJECT_ATTRIB_FLAGS = 1024
OBJECT_ATTRIB_VALUE_READONLY: win32more.Windows.Win32.System.Diagnostics.Debug.OBJECT_ATTRIB_FLAGS = 2048
OBJECT_ATTRIB_ACCESS_PUBLIC: win32more.Windows.Win32.System.Diagnostics.Debug.OBJECT_ATTRIB_FLAGS = 4096
OBJECT_ATTRIB_ACCESS_PRIVATE: win32more.Windows.Win32.System.Diagnostics.Debug.OBJECT_ATTRIB_FLAGS = 8192
OBJECT_ATTRIB_ACCESS_PROTECTED: win32more.Windows.Win32.System.Diagnostics.Debug.OBJECT_ATTRIB_FLAGS = 16384
OBJECT_ATTRIB_ACCESS_FINAL: win32more.Windows.Win32.System.Diagnostics.Debug.OBJECT_ATTRIB_FLAGS = 32768
OBJECT_ATTRIB_STORAGE_GLOBAL: win32more.Windows.Win32.System.Diagnostics.Debug.OBJECT_ATTRIB_FLAGS = 65536
OBJECT_ATTRIB_STORAGE_STATIC: win32more.Windows.Win32.System.Diagnostics.Debug.OBJECT_ATTRIB_FLAGS = 131072
OBJECT_ATTRIB_STORAGE_FIELD: win32more.Windows.Win32.System.Diagnostics.Debug.OBJECT_ATTRIB_FLAGS = 262144
OBJECT_ATTRIB_STORAGE_VIRTUAL: win32more.Windows.Win32.System.Diagnostics.Debug.OBJECT_ATTRIB_FLAGS = 524288
OBJECT_ATTRIB_TYPE_IS_CONSTANT: win32more.Windows.Win32.System.Diagnostics.Debug.OBJECT_ATTRIB_FLAGS = 1048576
OBJECT_ATTRIB_TYPE_IS_SYNCHRONIZED: win32more.Windows.Win32.System.Diagnostics.Debug.OBJECT_ATTRIB_FLAGS = 2097152
OBJECT_ATTRIB_TYPE_IS_VOLATILE: win32more.Windows.Win32.System.Diagnostics.Debug.OBJECT_ATTRIB_FLAGS = 4194304
OBJECT_ATTRIB_HAS_EXTENDED_ATTRIBS: win32more.Windows.Win32.System.Diagnostics.Debug.OBJECT_ATTRIB_FLAGS = 8388608
OBJECT_ATTRIB_IS_CLASS: win32more.Windows.Win32.System.Diagnostics.Debug.OBJECT_ATTRIB_FLAGS = 16777216
OBJECT_ATTRIB_IS_FUNCTION: win32more.Windows.Win32.System.Diagnostics.Debug.OBJECT_ATTRIB_FLAGS = 33554432
OBJECT_ATTRIB_IS_VARIABLE: win32more.Windows.Win32.System.Diagnostics.Debug.OBJECT_ATTRIB_FLAGS = 67108864
OBJECT_ATTRIB_IS_PROPERTY: win32more.Windows.Win32.System.Diagnostics.Debug.OBJECT_ATTRIB_FLAGS = 134217728
OBJECT_ATTRIB_IS_MACRO: win32more.Windows.Win32.System.Diagnostics.Debug.OBJECT_ATTRIB_FLAGS = 268435456
OBJECT_ATTRIB_IS_TYPE: win32more.Windows.Win32.System.Diagnostics.Debug.OBJECT_ATTRIB_FLAGS = 536870912
OBJECT_ATTRIB_IS_INHERITED: win32more.Windows.Win32.System.Diagnostics.Debug.OBJECT_ATTRIB_FLAGS = 1073741824
OBJECT_ATTRIB_IS_INTERFACE: win32more.Windows.Win32.System.Diagnostics.Debug.OBJECT_ATTRIB_FLAGS = -2147483648
class OMAP(Structure):
    rva: UInt32
    rvaTo: UInt32
OPEN_THREAD_WAIT_CHAIN_SESSION_FLAGS = UInt32
WCT_ASYNC_OPEN_FLAG: win32more.Windows.Win32.System.Diagnostics.Debug.OPEN_THREAD_WAIT_CHAIN_SESSION_FLAGS = 1
class OUTPUT_DEBUG_STRING_INFO(Structure):
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
def PENUMDIRTREE_CALLBACKW(FilePath: win32more.Windows.Win32.Foundation.PWSTR, CallerData: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
PENUMDIRTREE_CALLBACK = UnicodeAlias('PENUMDIRTREE_CALLBACKW')
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
def PFINDFILEINPATHCALLBACKW(filename: win32more.Windows.Win32.Foundation.PWSTR, context: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
PFINDFILEINPATHCALLBACK = UnicodeAlias('PFINDFILEINPATHCALLBACKW')
@winfunctype_pointer
def PFIND_DEBUG_FILE_CALLBACKW(FileHandle: win32more.Windows.Win32.Foundation.HANDLE, FileName: win32more.Windows.Win32.Foundation.PWSTR, CallerData: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
PFIND_DEBUG_FILE_CALLBACK = UnicodeAlias('PFIND_DEBUG_FILE_CALLBACKW')
@winfunctype_pointer
def PFIND_EXE_FILE_CALLBACKW(FileHandle: win32more.Windows.Win32.Foundation.HANDLE, FileName: win32more.Windows.Win32.Foundation.PWSTR, CallerData: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
PFIND_EXE_FILE_CALLBACK = UnicodeAlias('PFIND_EXE_FILE_CALLBACKW')
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
    def PGET_RUNTIME_FUNCTION_CALLBACK(ControlPc: UInt64, Context: VoidPtr) -> POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_ARM64_RUNTIME_FUNCTION_ENTRY): ...
elif ARCH in 'X64':
    @winfunctype_pointer
    def PGET_RUNTIME_FUNCTION_CALLBACK(ControlPc: UInt64, Context: VoidPtr) -> POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_RUNTIME_FUNCTION_ENTRY): ...
@winfunctype_pointer
def PGET_TARGET_ATTRIBUTE_VALUE64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Attribute: UInt32, AttributeData: UInt64, AttributeValue: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
class PHYSICAL_MEMORY_DESCRIPTOR32(Structure):
    NumberOfRuns: UInt32
    NumberOfPages: UInt32
    Run: win32more.Windows.Win32.System.Diagnostics.Debug.PHYSICAL_MEMORY_RUN32 * 1
class PHYSICAL_MEMORY_DESCRIPTOR64(Structure):
    NumberOfRuns: UInt32
    NumberOfPages: UInt64
    Run: win32more.Windows.Win32.System.Diagnostics.Debug.PHYSICAL_MEMORY_RUN64 * 1
class PHYSICAL_MEMORY_RUN32(Structure):
    BasePage: UInt32
    PageCount: UInt32
class PHYSICAL_MEMORY_RUN64(Structure):
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
PROP_INFO_NAME: win32more.Windows.Win32.System.Diagnostics.Debug.PROP_INFO_FLAGS = 1
PROP_INFO_TYPE: win32more.Windows.Win32.System.Diagnostics.Debug.PROP_INFO_FLAGS = 2
PROP_INFO_VALUE: win32more.Windows.Win32.System.Diagnostics.Debug.PROP_INFO_FLAGS = 4
PROP_INFO_FULLNAME: win32more.Windows.Win32.System.Diagnostics.Debug.PROP_INFO_FLAGS = 32
PROP_INFO_ATTRIBUTES: win32more.Windows.Win32.System.Diagnostics.Debug.PROP_INFO_FLAGS = 8
PROP_INFO_DEBUGPROP: win32more.Windows.Win32.System.Diagnostics.Debug.PROP_INFO_FLAGS = 16
PROP_INFO_AUTOEXPAND: win32more.Windows.Win32.System.Diagnostics.Debug.PROP_INFO_FLAGS = 134217728
@winfunctype_pointer
def PSYMBOLSERVERBYINDEXPROCA(param0: win32more.Windows.Win32.Foundation.PSTR, param1: win32more.Windows.Win32.Foundation.PSTR, param2: win32more.Windows.Win32.Foundation.PSTR, param3: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYMBOLSERVERBYINDEXPROCW(param0: win32more.Windows.Win32.Foundation.PWSTR, param1: win32more.Windows.Win32.Foundation.PWSTR, param2: win32more.Windows.Win32.Foundation.PWSTR, param3: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
PSYMBOLSERVERBYINDEXPROC = UnicodeAlias('PSYMBOLSERVERBYINDEXPROCW')
@winfunctype_pointer
def PSYMBOLSERVERCALLBACKPROC(action: UIntPtr, data: UInt64, context: UInt64) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYMBOLSERVERCLOSEPROC() -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYMBOLSERVERDELTANAMEW(param0: win32more.Windows.Win32.Foundation.PWSTR, param1: VoidPtr, param2: UInt32, param3: UInt32, param4: VoidPtr, param5: UInt32, param6: UInt32, param7: win32more.Windows.Win32.Foundation.PWSTR, param8: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
PSYMBOLSERVERDELTANAME = UnicodeAlias('PSYMBOLSERVERDELTANAMEW')
@winfunctype_pointer
def PSYMBOLSERVERGETINDEXSTRINGW(param0: VoidPtr, param1: UInt32, param2: UInt32, param3: win32more.Windows.Win32.Foundation.PWSTR, param4: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
PSYMBOLSERVERGETINDEXSTRING = UnicodeAlias('PSYMBOLSERVERGETINDEXSTRINGW')
@winfunctype_pointer
def PSYMBOLSERVERGETOPTIONDATAPROC(param0: UIntPtr, param1: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYMBOLSERVERGETOPTIONSPROC() -> UIntPtr: ...
@winfunctype_pointer
def PSYMBOLSERVERGETSUPPLEMENTW(param0: win32more.Windows.Win32.Foundation.PWSTR, param1: win32more.Windows.Win32.Foundation.PWSTR, param2: win32more.Windows.Win32.Foundation.PWSTR, param3: win32more.Windows.Win32.Foundation.PWSTR, param4: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
PSYMBOLSERVERGETSUPPLEMENT = UnicodeAlias('PSYMBOLSERVERGETSUPPLEMENTW')
@winfunctype_pointer
def PSYMBOLSERVERGETVERSION(param0: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.API_VERSION)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYMBOLSERVERISSTOREW(param0: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
PSYMBOLSERVERISSTORE = UnicodeAlias('PSYMBOLSERVERISSTOREW')
@winfunctype_pointer
def PSYMBOLSERVERMESSAGEPROC(action: UIntPtr, data: UInt64, context: UInt64) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYMBOLSERVEROPENPROC() -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYMBOLSERVERPINGPROCA(param0: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYMBOLSERVERPINGPROCW(param0: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
PSYMBOLSERVERPINGPROC = UnicodeAlias('PSYMBOLSERVERPINGPROCW')
@winfunctype_pointer
def PSYMBOLSERVERPINGPROCWEX(param0: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYMBOLSERVERPROCA(param0: win32more.Windows.Win32.Foundation.PSTR, param1: win32more.Windows.Win32.Foundation.PSTR, param2: VoidPtr, param3: UInt32, param4: UInt32, param5: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYMBOLSERVERPROCW(param0: win32more.Windows.Win32.Foundation.PWSTR, param1: win32more.Windows.Win32.Foundation.PWSTR, param2: VoidPtr, param3: UInt32, param4: UInt32, param5: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
PSYMBOLSERVERPROC = UnicodeAlias('PSYMBOLSERVERPROCW')
@winfunctype_pointer
def PSYMBOLSERVERSETHTTPAUTHHEADER(pszAuthHeader: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYMBOLSERVERSETOPTIONSPROC(param0: UIntPtr, param1: UInt64) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYMBOLSERVERSETOPTIONSWPROC(param0: UIntPtr, param1: UInt64) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PSYMBOLSERVERSTOREFILEW(param0: win32more.Windows.Win32.Foundation.PWSTR, param1: win32more.Windows.Win32.Foundation.PWSTR, param2: VoidPtr, param3: UInt32, param4: UInt32, param5: win32more.Windows.Win32.Foundation.PWSTR, param6: UIntPtr, param7: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
PSYMBOLSERVERSTOREFILE = UnicodeAlias('PSYMBOLSERVERSTOREFILEW')
@winfunctype_pointer
def PSYMBOLSERVERSTORESUPPLEMENTW(param0: win32more.Windows.Win32.Foundation.PWSTR, param1: win32more.Windows.Win32.Foundation.PWSTR, param2: win32more.Windows.Win32.Foundation.PWSTR, param3: win32more.Windows.Win32.Foundation.PWSTR, param4: UIntPtr, param5: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
PSYMBOLSERVERSTORESUPPLEMENT = UnicodeAlias('PSYMBOLSERVERSTORESUPPLEMENTW')
@winfunctype_pointer
def PSYMBOLSERVERVERSION() -> UInt32: ...
@winfunctype_pointer
def PSYMBOLSERVERWEXPROC(param0: win32more.Windows.Win32.Foundation.PWSTR, param1: win32more.Windows.Win32.Foundation.PWSTR, param2: VoidPtr, param3: UInt32, param4: UInt32, param5: win32more.Windows.Win32.Foundation.PWSTR, param6: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.SYMSRV_EXTENDED_OUTPUT_DATA)) -> win32more.Windows.Win32.Foundation.BOOL: ...
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
def PSYM_ENUMERATESYMBOLS_CALLBACKW(pSymInfo: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFOW), SymbolSize: UInt32, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
PSYM_ENUMERATESYMBOLS_CALLBACK = UnicodeAlias('PSYM_ENUMERATESYMBOLS_CALLBACKW')
@winfunctype_pointer
def PSYM_ENUMLINES_CALLBACKW(LineInfo: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.SRCCODEINFOW), UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
PSYM_ENUMLINES_CALLBACK = UnicodeAlias('PSYM_ENUMLINES_CALLBACKW')
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
def PSYM_ENUMSOURCEFILES_CALLBACKW(pSourceFile: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.SOURCEFILEW), UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
PSYM_ENUMSOURCEFILES_CALLBACK = UnicodeAlias('PSYM_ENUMSOURCEFILES_CALLBACKW')
@winfunctype_pointer
def PSYM_ENUMSYMBOLS_CALLBACK64W(SymbolName: win32more.Windows.Win32.Foundation.PWSTR, SymbolAddress: UInt64, SymbolSize: UInt32, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
PSYM_ENUMSYMBOLS_CALLBACK64 = UnicodeAlias('PSYM_ENUMSYMBOLS_CALLBACK64W')
if ARCH in 'X86':
    @winfunctype_pointer
    def PSYM_ENUMSYMBOLS_CALLBACKW(SymbolName: win32more.Windows.Win32.Foundation.PWSTR, SymbolAddress: UInt32, SymbolSize: UInt32, UserContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X86':
    PSYM_ENUMSYMBOLS_CALLBACK = UnicodeAlias('PSYM_ENUMSYMBOLS_CALLBACKW')
if ARCH in 'X86':
    @winfunctype_pointer
    def PTRANSLATE_ADDRESS_ROUTINE(hProcess: win32more.Windows.Win32.Foundation.HANDLE, hThread: win32more.Windows.Win32.Foundation.HANDLE, lpaddr: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ADDRESS)) -> UInt32: ...
@winfunctype_pointer
def PTRANSLATE_ADDRESS_ROUTINE64(hProcess: win32more.Windows.Win32.Foundation.HANDLE, hThread: win32more.Windows.Win32.Foundation.HANDLE, lpaddr: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ADDRESS64)) -> UInt64: ...
@winfunctype_pointer
def PVECTORED_EXCEPTION_HANDLER(ExceptionInfo: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.EXCEPTION_POINTERS)) -> Int32: ...
@winfunctype_pointer
def PWAITCHAINCALLBACK(WctHandle: VoidPtr, Context: UIntPtr, CallbackStatus: UInt32, NodeCount: POINTER(UInt32), NodeInfoArray: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.WAITCHAIN_NODE_INFO), IsCycle: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> Void: ...
class RIP_INFO(Structure):
    dwError: UInt32
    dwType: win32more.Windows.Win32.System.Diagnostics.Debug.RIP_INFO_TYPE
RIP_INFO_TYPE = UInt32
SLE_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.RIP_INFO_TYPE = 1
SLE_MINORERROR: win32more.Windows.Win32.System.Diagnostics.Debug.RIP_INFO_TYPE = 2
SLE_WARNING: win32more.Windows.Win32.System.Diagnostics.Debug.RIP_INFO_TYPE = 3
RTL_VIRTUAL_UNWIND_HANDLER_TYPE = UInt32
UNW_FLAG_NHANDLER: win32more.Windows.Win32.System.Diagnostics.Debug.RTL_VIRTUAL_UNWIND_HANDLER_TYPE = 0
UNW_FLAG_EHANDLER: win32more.Windows.Win32.System.Diagnostics.Debug.RTL_VIRTUAL_UNWIND_HANDLER_TYPE = 1
UNW_FLAG_UHANDLER: win32more.Windows.Win32.System.Diagnostics.Debug.RTL_VIRTUAL_UNWIND_HANDLER_TYPE = 2
UNW_FLAG_CHAININFO: win32more.Windows.Win32.System.Diagnostics.Debug.RTL_VIRTUAL_UNWIND_HANDLER_TYPE = 4
class SOURCEFILEW(Structure):
    ModBase: UInt64
    FileName: win32more.Windows.Win32.Foundation.PWSTR
SOURCEFILE = UnicodeAlias('SOURCEFILEW')
class SRCCODEINFOW(Structure):
    SizeOfStruct: UInt32
    Key: VoidPtr
    ModBase: UInt64
    Obj: Char * 261
    FileName: Char * 261
    LineNumber: UInt32
    Address: UInt64
SRCCODEINFO = UnicodeAlias('SRCCODEINFOW')
if ARCH in 'X86':
    class STACKFRAME(Structure):
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
class STACKFRAME64(Structure):
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
class STACKFRAME_EX(Structure):
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
class SYMBOL_INFOW(Structure):
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
SYMBOL_INFO = UnicodeAlias('SYMBOL_INFOW')
SYMBOL_INFO_FLAGS = UInt32
SYMFLAG_CLR_TOKEN: win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFO_FLAGS = 262144
SYMFLAG_CONSTANT: win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFO_FLAGS = 256
SYMFLAG_EXPORT: win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFO_FLAGS = 512
SYMFLAG_FORWARDER: win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFO_FLAGS = 1024
SYMFLAG_FRAMEREL: win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFO_FLAGS = 32
SYMFLAG_FUNCTION: win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFO_FLAGS = 2048
SYMFLAG_ILREL: win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFO_FLAGS = 65536
SYMFLAG_LOCAL: win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFO_FLAGS = 128
SYMFLAG_METADATA: win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFO_FLAGS = 131072
SYMFLAG_PARAMETER: win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFO_FLAGS = 64
SYMFLAG_REGISTER: win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFO_FLAGS = 8
SYMFLAG_REGREL: win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFO_FLAGS = 16
SYMFLAG_SLOT: win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFO_FLAGS = 32768
SYMFLAG_THUNK: win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFO_FLAGS = 8192
SYMFLAG_TLSREL: win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFO_FLAGS = 16384
SYMFLAG_VALUEPRESENT: win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFO_FLAGS = 1
SYMFLAG_VIRTUAL: win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFO_FLAGS = 4096
class SYMBOL_INFO_PACKAGEW(Structure):
    si: win32more.Windows.Win32.System.Diagnostics.Debug.SYMBOL_INFOW
    name: Char * 2001
SYMBOL_INFO_PACKAGE = UnicodeAlias('SYMBOL_INFO_PACKAGEW')
class SYMSRV_EXTENDED_OUTPUT_DATA(Structure):
    sizeOfStruct: UInt32
    version: UInt32
    filePtrMsg: Char * 261
class SYMSRV_INDEX_INFOW(Structure):
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
SYMSRV_INDEX_INFO = UnicodeAlias('SYMSRV_INDEX_INFOW')
SYM_FIND_ID_OPTION = UInt32
SSRVOPT_DWORD: win32more.Windows.Win32.System.Diagnostics.Debug.SYM_FIND_ID_OPTION = 2
SSRVOPT_DWORDPTR: win32more.Windows.Win32.System.Diagnostics.Debug.SYM_FIND_ID_OPTION = 4
SSRVOPT_GUIDPTR: win32more.Windows.Win32.System.Diagnostics.Debug.SYM_FIND_ID_OPTION = 8
SYM_LOAD_FLAGS = UInt32
SLMFLAG_NONE: win32more.Windows.Win32.System.Diagnostics.Debug.SYM_LOAD_FLAGS = 0
SLMFLAG_VIRTUAL: win32more.Windows.Win32.System.Diagnostics.Debug.SYM_LOAD_FLAGS = 1
SLMFLAG_ALT_INDEX: win32more.Windows.Win32.System.Diagnostics.Debug.SYM_LOAD_FLAGS = 2
SLMFLAG_NO_SYMBOLS: win32more.Windows.Win32.System.Diagnostics.Debug.SYM_LOAD_FLAGS = 4
SYM_SRV_STORE_FILE_FLAGS = UInt32
SYMSTOREOPT_COMPRESS: win32more.Windows.Win32.System.Diagnostics.Debug.SYM_SRV_STORE_FILE_FLAGS = 1
SYMSTOREOPT_OVERWRITE: win32more.Windows.Win32.System.Diagnostics.Debug.SYM_SRV_STORE_FILE_FLAGS = 2
SYMSTOREOPT_PASS_IF_EXISTS: win32more.Windows.Win32.System.Diagnostics.Debug.SYM_SRV_STORE_FILE_FLAGS = 64
SYMSTOREOPT_POINTER: win32more.Windows.Win32.System.Diagnostics.Debug.SYM_SRV_STORE_FILE_FLAGS = 8
SYMSTOREOPT_RETURNINDEX: win32more.Windows.Win32.System.Diagnostics.Debug.SYM_SRV_STORE_FILE_FLAGS = 4
SYM_TYPE = Int32
SymNone: win32more.Windows.Win32.System.Diagnostics.Debug.SYM_TYPE = 0
SymCoff: win32more.Windows.Win32.System.Diagnostics.Debug.SYM_TYPE = 1
SymCv: win32more.Windows.Win32.System.Diagnostics.Debug.SYM_TYPE = 2
SymPdb: win32more.Windows.Win32.System.Diagnostics.Debug.SYM_TYPE = 3
SymExport: win32more.Windows.Win32.System.Diagnostics.Debug.SYM_TYPE = 4
SymDeferred: win32more.Windows.Win32.System.Diagnostics.Debug.SYM_TYPE = 5
SymSym: win32more.Windows.Win32.System.Diagnostics.Debug.SYM_TYPE = 6
SymDia: win32more.Windows.Win32.System.Diagnostics.Debug.SYM_TYPE = 7
SymVirtual: win32more.Windows.Win32.System.Diagnostics.Debug.SYM_TYPE = 8
NumSymTypes: win32more.Windows.Win32.System.Diagnostics.Debug.SYM_TYPE = 9
THREAD_ERROR_MODE = UInt32
SEM_ALL_ERRORS: win32more.Windows.Win32.System.Diagnostics.Debug.THREAD_ERROR_MODE = 0
SEM_FAILCRITICALERRORS: win32more.Windows.Win32.System.Diagnostics.Debug.THREAD_ERROR_MODE = 1
SEM_NOGPFAULTERRORBOX: win32more.Windows.Win32.System.Diagnostics.Debug.THREAD_ERROR_MODE = 2
SEM_NOOPENFILEERRORBOX: win32more.Windows.Win32.System.Diagnostics.Debug.THREAD_ERROR_MODE = 32768
SEM_NOALIGNMENTFAULTEXCEPT: win32more.Windows.Win32.System.Diagnostics.Debug.THREAD_ERROR_MODE = 4
THREAD_WRITE_FLAGS = Int32
ThreadWriteThread: win32more.Windows.Win32.System.Diagnostics.Debug.THREAD_WRITE_FLAGS = 1
ThreadWriteStack: win32more.Windows.Win32.System.Diagnostics.Debug.THREAD_WRITE_FLAGS = 2
ThreadWriteContext: win32more.Windows.Win32.System.Diagnostics.Debug.THREAD_WRITE_FLAGS = 4
ThreadWriteBackingStore: win32more.Windows.Win32.System.Diagnostics.Debug.THREAD_WRITE_FLAGS = 8
ThreadWriteInstructionWindow: win32more.Windows.Win32.System.Diagnostics.Debug.THREAD_WRITE_FLAGS = 16
ThreadWriteThreadData: win32more.Windows.Win32.System.Diagnostics.Debug.THREAD_WRITE_FLAGS = 32
ThreadWriteThreadInfo: win32more.Windows.Win32.System.Diagnostics.Debug.THREAD_WRITE_FLAGS = 64
class TI_FINDCHILDREN_PARAMS(Structure):
    Count: UInt32
    Start: UInt32
    ChildId: UInt32 * 1
class UNLOAD_DLL_DEBUG_INFO(Structure):
    lpBaseOfDll: VoidPtr
if ARCH in 'X64,ARM64':
    class UNWIND_HISTORY_TABLE(Structure):
        Count: UInt32
        LocalHint: Byte
        GlobalHint: Byte
        Search: Byte
        Once: Byte
        LowAddress: UIntPtr
        HighAddress: UIntPtr
        Entry: win32more.Windows.Win32.System.Diagnostics.Debug.UNWIND_HISTORY_TABLE_ENTRY * 12
if ARCH in 'ARM64':
    class UNWIND_HISTORY_TABLE_ENTRY(Structure):
        ImageBase: UIntPtr
        FunctionEntry: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_ARM64_RUNTIME_FUNCTION_ENTRY)
elif ARCH in 'X64':
    class UNWIND_HISTORY_TABLE_ENTRY(Structure):
        ImageBase: UIntPtr
        FunctionEntry: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IMAGE_RUNTIME_FUNCTION_ENTRY)
VER_PLATFORM = UInt32
VER_PLATFORM_WIN32s: win32more.Windows.Win32.System.Diagnostics.Debug.VER_PLATFORM = 0
VER_PLATFORM_WIN32_WINDOWS: win32more.Windows.Win32.System.Diagnostics.Debug.VER_PLATFORM = 1
VER_PLATFORM_WIN32_NT: win32more.Windows.Win32.System.Diagnostics.Debug.VER_PLATFORM = 2
class WAITCHAIN_NODE_INFO(Structure):
    ObjectType: win32more.Windows.Win32.System.Diagnostics.Debug.WCT_OBJECT_TYPE
    ObjectStatus: win32more.Windows.Win32.System.Diagnostics.Debug.WCT_OBJECT_STATUS
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        LockObject: _LockObject_e__Struct
        ThreadObject: _ThreadObject_e__Struct
        class _LockObject_e__Struct(Structure):
            ObjectName: Char * 128
            Timeout: Int64
            Alertable: win32more.Windows.Win32.Foundation.BOOL
        class _ThreadObject_e__Struct(Structure):
            ProcessId: UInt32
            ThreadId: UInt32
            WaitTime: UInt32
            ContextSwitches: UInt32
WAIT_CHAIN_THREAD_OPTIONS = UInt32
WCT_OUT_OF_PROC_COM_FLAG: win32more.Windows.Win32.System.Diagnostics.Debug.WAIT_CHAIN_THREAD_OPTIONS = 2
WCT_OUT_OF_PROC_CS_FLAG: win32more.Windows.Win32.System.Diagnostics.Debug.WAIT_CHAIN_THREAD_OPTIONS = 4
WCT_OUT_OF_PROC_FLAG: win32more.Windows.Win32.System.Diagnostics.Debug.WAIT_CHAIN_THREAD_OPTIONS = 1
WCT_OBJECT_STATUS = Int32
WctStatusNoAccess: win32more.Windows.Win32.System.Diagnostics.Debug.WCT_OBJECT_STATUS = 1
WctStatusRunning: win32more.Windows.Win32.System.Diagnostics.Debug.WCT_OBJECT_STATUS = 2
WctStatusBlocked: win32more.Windows.Win32.System.Diagnostics.Debug.WCT_OBJECT_STATUS = 3
WctStatusPidOnly: win32more.Windows.Win32.System.Diagnostics.Debug.WCT_OBJECT_STATUS = 4
WctStatusPidOnlyRpcss: win32more.Windows.Win32.System.Diagnostics.Debug.WCT_OBJECT_STATUS = 5
WctStatusOwned: win32more.Windows.Win32.System.Diagnostics.Debug.WCT_OBJECT_STATUS = 6
WctStatusNotOwned: win32more.Windows.Win32.System.Diagnostics.Debug.WCT_OBJECT_STATUS = 7
WctStatusAbandoned: win32more.Windows.Win32.System.Diagnostics.Debug.WCT_OBJECT_STATUS = 8
WctStatusUnknown: win32more.Windows.Win32.System.Diagnostics.Debug.WCT_OBJECT_STATUS = 9
WctStatusError: win32more.Windows.Win32.System.Diagnostics.Debug.WCT_OBJECT_STATUS = 10
WctStatusMax: win32more.Windows.Win32.System.Diagnostics.Debug.WCT_OBJECT_STATUS = 11
WCT_OBJECT_TYPE = Int32
WctCriticalSectionType: win32more.Windows.Win32.System.Diagnostics.Debug.WCT_OBJECT_TYPE = 1
WctSendMessageType: win32more.Windows.Win32.System.Diagnostics.Debug.WCT_OBJECT_TYPE = 2
WctMutexType: win32more.Windows.Win32.System.Diagnostics.Debug.WCT_OBJECT_TYPE = 3
WctAlpcType: win32more.Windows.Win32.System.Diagnostics.Debug.WCT_OBJECT_TYPE = 4
WctComType: win32more.Windows.Win32.System.Diagnostics.Debug.WCT_OBJECT_TYPE = 5
WctThreadWaitType: win32more.Windows.Win32.System.Diagnostics.Debug.WCT_OBJECT_TYPE = 6
WctProcessWaitType: win32more.Windows.Win32.System.Diagnostics.Debug.WCT_OBJECT_TYPE = 7
WctThreadType: win32more.Windows.Win32.System.Diagnostics.Debug.WCT_OBJECT_TYPE = 8
WctComActivationType: win32more.Windows.Win32.System.Diagnostics.Debug.WCT_OBJECT_TYPE = 9
WctUnknownType: win32more.Windows.Win32.System.Diagnostics.Debug.WCT_OBJECT_TYPE = 10
WctSocketIoType: win32more.Windows.Win32.System.Diagnostics.Debug.WCT_OBJECT_TYPE = 11
WctSmbIoType: win32more.Windows.Win32.System.Diagnostics.Debug.WCT_OBJECT_TYPE = 12
WctMaxType: win32more.Windows.Win32.System.Diagnostics.Debug.WCT_OBJECT_TYPE = 13
class WHEA_AER_BRIDGE_DESCRIPTOR(Structure):
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
class WHEA_AER_ENDPOINT_DESCRIPTOR(Structure):
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
class WHEA_AER_ROOTPORT_DESCRIPTOR(Structure):
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
class WHEA_DEVICE_DRIVER_DESCRIPTOR(Structure):
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
class WHEA_DRIVER_BUFFER_SET(Structure):
    Version: UInt32
    Data: POINTER(Byte)
    DataSize: UInt32
    SectionTypeGuid: POINTER(Guid)
    SectionFriendlyName: POINTER(Byte)
    Flags: POINTER(Byte)
    _pack_ = 1
class WHEA_ERROR_SOURCE_CONFIGURATION_DD(Structure):
    Initialize: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_ERROR_SOURCE_INITIALIZE_DEVICE_DRIVER
    Uninitialize: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_ERROR_SOURCE_UNINITIALIZE_DEVICE_DRIVER
    Correct: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_ERROR_SOURCE_CORRECT_DEVICE_DRIVER
    _pack_ = 1
class WHEA_ERROR_SOURCE_CONFIGURATION_DEVICE_DRIVER(Structure):
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
class WHEA_ERROR_SOURCE_CONFIGURATION_DEVICE_DRIVER_V1(Structure):
    Version: UInt32
    SourceGuid: Guid
    LogTag: UInt16
    Reserved: Byte * 6
    Initialize: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_ERROR_SOURCE_INITIALIZE_DEVICE_DRIVER
    Uninitialize: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_ERROR_SOURCE_UNINITIALIZE_DEVICE_DRIVER
    _pack_ = 1
@winfunctype_pointer
def WHEA_ERROR_SOURCE_CORRECT_DEVICE_DRIVER(ErrorSourceDesc: VoidPtr, MaximumSectionLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
class WHEA_ERROR_SOURCE_DESCRIPTOR(Structure):
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
    class _Info_e__Union(Union):
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
WheaErrSrcStateStopped: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_ERROR_SOURCE_STATE = 1
WheaErrSrcStateStarted: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_ERROR_SOURCE_STATE = 2
WheaErrSrcStateRemoved: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_ERROR_SOURCE_STATE = 3
WheaErrSrcStateRemovePending: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_ERROR_SOURCE_STATE = 4
WHEA_ERROR_SOURCE_TYPE = Int32
WheaErrSrcTypeMCE: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_ERROR_SOURCE_TYPE = 0
WheaErrSrcTypeCMC: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_ERROR_SOURCE_TYPE = 1
WheaErrSrcTypeCPE: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_ERROR_SOURCE_TYPE = 2
WheaErrSrcTypeNMI: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_ERROR_SOURCE_TYPE = 3
WheaErrSrcTypePCIe: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_ERROR_SOURCE_TYPE = 4
WheaErrSrcTypeGeneric: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_ERROR_SOURCE_TYPE = 5
WheaErrSrcTypeINIT: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_ERROR_SOURCE_TYPE = 6
WheaErrSrcTypeBOOT: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_ERROR_SOURCE_TYPE = 7
WheaErrSrcTypeSCIGeneric: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_ERROR_SOURCE_TYPE = 8
WheaErrSrcTypeIPFMCA: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_ERROR_SOURCE_TYPE = 9
WheaErrSrcTypeIPFCMC: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_ERROR_SOURCE_TYPE = 10
WheaErrSrcTypeIPFCPE: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_ERROR_SOURCE_TYPE = 11
WheaErrSrcTypeGenericV2: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_ERROR_SOURCE_TYPE = 12
WheaErrSrcTypeSCIGenericV2: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_ERROR_SOURCE_TYPE = 13
WheaErrSrcTypeBMC: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_ERROR_SOURCE_TYPE = 14
WheaErrSrcTypePMEM: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_ERROR_SOURCE_TYPE = 15
WheaErrSrcTypeDeviceDriver: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_ERROR_SOURCE_TYPE = 16
WheaErrSrcTypeSea: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_ERROR_SOURCE_TYPE = 17
WheaErrSrcTypeSei: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_ERROR_SOURCE_TYPE = 18
WheaErrSrcTypeMax: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_ERROR_SOURCE_TYPE = 19
@winfunctype_pointer
def WHEA_ERROR_SOURCE_UNINITIALIZE_DEVICE_DRIVER(Context: VoidPtr) -> Void: ...
class WHEA_GENERIC_ERROR_DESCRIPTOR(Structure):
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
class WHEA_GENERIC_ERROR_DESCRIPTOR_V2(Structure):
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
class WHEA_IPF_CMC_DESCRIPTOR(Structure):
    Type: UInt16
    Enabled: Byte
    Reserved: Byte
    _pack_ = 1
class WHEA_IPF_CPE_DESCRIPTOR(Structure):
    Type: UInt16
    Enabled: Byte
    Reserved: Byte
    _pack_ = 1
class WHEA_IPF_MCA_DESCRIPTOR(Structure):
    Type: UInt16
    Enabled: Byte
    Reserved: Byte
    _pack_ = 1
class WHEA_NOTIFICATION_DESCRIPTOR(Structure):
    Type: Byte
    Length: Byte
    Flags: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_NOTIFICATION_FLAGS
    u: _u_e__Union
    class _u_e__Union(Union):
        Polled: _Polled_e__Struct
        Interrupt: _Interrupt_e__Struct
        LocalInterrupt: _LocalInterrupt_e__Struct
        Sci: _Sci_e__Struct
        Nmi: _Nmi_e__Struct
        Sea: _Sea_e__Struct
        Sei: _Sei_e__Struct
        Gsiv: _Gsiv_e__Struct
        class _Polled_e__Struct(Structure):
            PollInterval: UInt32
            _pack_ = 1
        class _Interrupt_e__Struct(Structure):
            PollInterval: UInt32
            Vector: UInt32
            SwitchToPollingThreshold: UInt32
            SwitchToPollingWindow: UInt32
            ErrorThreshold: UInt32
            ErrorThresholdWindow: UInt32
            _pack_ = 1
        class _LocalInterrupt_e__Struct(Structure):
            PollInterval: UInt32
            Vector: UInt32
            SwitchToPollingThreshold: UInt32
            SwitchToPollingWindow: UInt32
            ErrorThreshold: UInt32
            ErrorThresholdWindow: UInt32
            _pack_ = 1
        class _Sci_e__Struct(Structure):
            PollInterval: UInt32
            Vector: UInt32
            SwitchToPollingThreshold: UInt32
            SwitchToPollingWindow: UInt32
            ErrorThreshold: UInt32
            ErrorThresholdWindow: UInt32
            _pack_ = 1
        class _Nmi_e__Struct(Structure):
            PollInterval: UInt32
            Vector: UInt32
            SwitchToPollingThreshold: UInt32
            SwitchToPollingWindow: UInt32
            ErrorThreshold: UInt32
            ErrorThresholdWindow: UInt32
            _pack_ = 1
        class _Sea_e__Struct(Structure):
            PollInterval: UInt32
            Vector: UInt32
            SwitchToPollingThreshold: UInt32
            SwitchToPollingWindow: UInt32
            ErrorThreshold: UInt32
            ErrorThresholdWindow: UInt32
            _pack_ = 1
        class _Sei_e__Struct(Structure):
            PollInterval: UInt32
            Vector: UInt32
            SwitchToPollingThreshold: UInt32
            SwitchToPollingWindow: UInt32
            ErrorThreshold: UInt32
            ErrorThresholdWindow: UInt32
            _pack_ = 1
        class _Gsiv_e__Struct(Structure):
            PollInterval: UInt32
            Vector: UInt32
            SwitchToPollingThreshold: UInt32
            SwitchToPollingWindow: UInt32
            ErrorThreshold: UInt32
            ErrorThresholdWindow: UInt32
            _pack_ = 1
class WHEA_NOTIFICATION_FLAGS(Union):
    Anonymous: _Anonymous_e__Struct
    AsUSHORT: UInt16
    _pack_ = 1
    class _Anonymous_e__Struct(Structure):
        PollIntervalRW: Annotated[UInt16, 1]
        SwitchToPollingThresholdRW: Annotated[UInt16, 1]
        SwitchToPollingWindowRW: Annotated[UInt16, 1]
        ErrorThresholdRW: Annotated[UInt16, 1]
        ErrorThresholdWindowRW: Annotated[UInt16, 1]
        Reserved: Annotated[UInt16, 11]
        _pack_ = 1
class WHEA_PCI_SLOT_NUMBER(Structure):
    u: _u_e__Union
    class _u_e__Union(Union):
        bits: _bits_e__Struct
        AsULONG: UInt32
        _pack_ = 1
        class _bits_e__Struct(Structure):
            DeviceNumber: Annotated[UInt32, 5]
            FunctionNumber: Annotated[UInt32, 3]
            Reserved: Annotated[UInt32, 24]
            _pack_ = 1
class WHEA_XPF_CMC_DESCRIPTOR(Structure):
    Type: UInt16
    Enabled: win32more.Windows.Win32.Foundation.BOOLEAN
    NumberOfBanks: Byte
    Reserved: UInt32
    Notify: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_NOTIFICATION_DESCRIPTOR
    Banks: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_XPF_MC_BANK_DESCRIPTOR * 32
    _pack_ = 1
class WHEA_XPF_MCE_DESCRIPTOR(Structure):
    Type: UInt16
    Enabled: Byte
    NumberOfBanks: Byte
    Flags: win32more.Windows.Win32.System.Diagnostics.Debug.XPF_MCE_FLAGS
    MCG_Capability: UInt64
    MCG_GlobalControl: UInt64
    Banks: win32more.Windows.Win32.System.Diagnostics.Debug.WHEA_XPF_MC_BANK_DESCRIPTOR * 32
    _pack_ = 1
class WHEA_XPF_MC_BANK_DESCRIPTOR(Structure):
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
class WHEA_XPF_NMI_DESCRIPTOR(Structure):
    Type: UInt16
    Enabled: win32more.Windows.Win32.Foundation.BOOLEAN
    _pack_ = 1
class WOW64_CONTEXT(Structure):
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
WOW64_CONTEXT_X86: win32more.Windows.Win32.System.Diagnostics.Debug.WOW64_CONTEXT_FLAGS = 65536
WOW64_CONTEXT_CONTROL: win32more.Windows.Win32.System.Diagnostics.Debug.WOW64_CONTEXT_FLAGS = 65537
WOW64_CONTEXT_INTEGER: win32more.Windows.Win32.System.Diagnostics.Debug.WOW64_CONTEXT_FLAGS = 65538
WOW64_CONTEXT_SEGMENTS: win32more.Windows.Win32.System.Diagnostics.Debug.WOW64_CONTEXT_FLAGS = 65540
WOW64_CONTEXT_FLOATING_POINT: win32more.Windows.Win32.System.Diagnostics.Debug.WOW64_CONTEXT_FLAGS = 65544
WOW64_CONTEXT_DEBUG_REGISTERS: win32more.Windows.Win32.System.Diagnostics.Debug.WOW64_CONTEXT_FLAGS = 65552
WOW64_CONTEXT_EXTENDED_REGISTERS: win32more.Windows.Win32.System.Diagnostics.Debug.WOW64_CONTEXT_FLAGS = 65568
WOW64_CONTEXT_FULL: win32more.Windows.Win32.System.Diagnostics.Debug.WOW64_CONTEXT_FLAGS = 65543
WOW64_CONTEXT_ALL: win32more.Windows.Win32.System.Diagnostics.Debug.WOW64_CONTEXT_FLAGS = 65599
WOW64_CONTEXT_XSTATE: win32more.Windows.Win32.System.Diagnostics.Debug.WOW64_CONTEXT_FLAGS = 65600
WOW64_CONTEXT_EXCEPTION_ACTIVE: win32more.Windows.Win32.System.Diagnostics.Debug.WOW64_CONTEXT_FLAGS = 134217728
WOW64_CONTEXT_SERVICE_ACTIVE: win32more.Windows.Win32.System.Diagnostics.Debug.WOW64_CONTEXT_FLAGS = 268435456
WOW64_CONTEXT_EXCEPTION_REQUEST: win32more.Windows.Win32.System.Diagnostics.Debug.WOW64_CONTEXT_FLAGS = 1073741824
WOW64_CONTEXT_EXCEPTION_REPORTING: win32more.Windows.Win32.System.Diagnostics.Debug.WOW64_CONTEXT_FLAGS = 2147483648
class WOW64_DESCRIPTOR_TABLE_ENTRY(Structure):
    Selector: UInt32
    Descriptor: win32more.Windows.Win32.System.Diagnostics.Debug.WOW64_LDT_ENTRY
class WOW64_FLOATING_SAVE_AREA(Structure):
    ControlWord: UInt32
    StatusWord: UInt32
    TagWord: UInt32
    ErrorOffset: UInt32
    ErrorSelector: UInt32
    DataOffset: UInt32
    DataSelector: UInt32
    RegisterArea: Byte * 80
    Cr0NpxState: UInt32
class WOW64_LDT_ENTRY(Structure):
    LimitLow: UInt16
    BaseLow: UInt16
    HighWord: _HighWord_e__Union
    class _HighWord_e__Union(Union):
        Bytes: _Bytes_e__Struct
        Bits: _Bits_e__Struct
        class _Bytes_e__Struct(Structure):
            BaseMid: Byte
            Flags1: Byte
            Flags2: Byte
            BaseHi: Byte
        class _Bits_e__Struct(Structure):
            BaseMid: Annotated[UInt32, 8]
            Type: Annotated[UInt32, 5]
            Dpl: Annotated[UInt32, 2]
            Pres: Annotated[UInt32, 1]
            LimitHi: Annotated[UInt32, 4]
            Sys: Annotated[UInt32, 1]
            Reserved_0: Annotated[UInt32, 1]
            Default_Big: Annotated[UInt32, 1]
            Granularity: Annotated[UInt32, 1]
            BaseHi: Annotated[UInt32, 8]
class XPF_MCE_FLAGS(Union):
    Anonymous: _Anonymous_e__Struct
    AsULONG: UInt32
    _pack_ = 1
    class _Anonymous_e__Struct(Structure):
        MCG_CapabilityRW: Annotated[UInt32, 1]
        MCG_GlobalControlRW: Annotated[UInt32, 1]
        Reserved: Annotated[UInt32, 30]
        _pack_ = 1
class XPF_MC_BANK_FLAGS(Union):
    Anonymous: _Anonymous_e__Struct
    AsUCHAR: Byte
    class _Anonymous_e__Struct(Structure):
        ClearOnInitializationRW: Annotated[Byte, 1]
        ControlDataRW: Annotated[Byte, 1]
        Reserved: Annotated[Byte, 6]
class XSAVE_AREA(Structure):
    LegacyState: win32more.Windows.Win32.System.Diagnostics.Debug.XSAVE_FORMAT
    Header: win32more.Windows.Win32.System.Diagnostics.Debug.XSAVE_AREA_HEADER
class XSAVE_AREA_HEADER(Structure):
    Mask: UInt64
    CompactionMask: UInt64
    Reserved2: UInt64 * 6
if ARCH in 'X64,ARM64':
    class XSAVE_FORMAT(Structure):
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
elif ARCH in 'X86':
    class XSAVE_FORMAT(Structure):
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
class XSTATE_CONFIGURATION(Structure):
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
    class _Anonymous_e__Union(Union):
        ControlFlags: UInt32
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            OptimizedSave: Annotated[UInt32, 1]
            CompactionEnabled: Annotated[UInt32, 1]
            ExtendedFeatureDisable: Annotated[UInt32, 1]
class XSTATE_CONFIG_FEATURE_MSC_INFO(Structure):
    SizeOfInfo: UInt32
    ContextSize: UInt32
    EnabledFeatures: UInt64
    Features: win32more.Windows.Win32.System.Diagnostics.Debug.XSTATE_FEATURE * 64
    _pack_ = 4
if ARCH in 'X64,ARM64':
    class XSTATE_CONTEXT(Structure):
        Mask: UInt64
        Length: UInt32
        Reserved1: UInt32
        Area: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.XSAVE_AREA)
        Buffer: VoidPtr
elif ARCH in 'X86':
    class XSTATE_CONTEXT(Structure):
        Mask: UInt64
        Length: UInt32
        Reserved1: UInt32
        Area: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.XSAVE_AREA)
        Reserved2: UInt32
        Buffer: VoidPtr
        Reserved3: UInt32
class XSTATE_FEATURE(Structure):
    Offset: UInt32
    Size: UInt32


make_ready(__name__)
