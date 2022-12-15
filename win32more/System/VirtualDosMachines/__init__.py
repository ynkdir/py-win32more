from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.System.Diagnostics.Debug
import win32more.System.Kernel
import win32more.System.VirtualDosMachines
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
VDMCONTEXT_i386: UInt32 = 65536
VDMCONTEXT_i486: UInt32 = 65536
VDM_KGDT_R3_CODE: UInt32 = 24
VDM_MAXIMUM_SUPPORTED_EXTENSION: UInt32 = 512
V86FLAGS_CARRY: UInt32 = 1
V86FLAGS_PARITY: UInt32 = 4
V86FLAGS_AUXCARRY: UInt32 = 16
V86FLAGS_ZERO: UInt32 = 64
V86FLAGS_SIGN: UInt32 = 128
V86FLAGS_TRACE: UInt32 = 256
V86FLAGS_INTERRUPT: UInt32 = 512
V86FLAGS_DIRECTION: UInt32 = 1024
V86FLAGS_OVERFLOW: UInt32 = 2048
V86FLAGS_IOPL: UInt32 = 12288
V86FLAGS_IOPL_BITS: UInt32 = 18
V86FLAGS_RESUME: UInt32 = 65536
V86FLAGS_V86: UInt32 = 131072
V86FLAGS_ALIGNMENT: UInt32 = 262144
STATUS_VDM_EVENT: Int32 = 1073741829
DBG_SEGLOAD: UInt32 = 0
DBG_SEGMOVE: UInt32 = 1
DBG_SEGFREE: UInt32 = 2
DBG_MODLOAD: UInt32 = 3
DBG_MODFREE: UInt32 = 4
DBG_SINGLESTEP: UInt32 = 5
DBG_BREAK: UInt32 = 6
DBG_GPFAULT: UInt32 = 7
DBG_DIVOVERFLOW: UInt32 = 8
DBG_INSTRFAULT: UInt32 = 9
DBG_TASKSTART: UInt32 = 10
DBG_TASKSTOP: UInt32 = 11
DBG_DLLSTART: UInt32 = 12
DBG_DLLSTOP: UInt32 = 13
DBG_ATTACH: UInt32 = 14
DBG_TOOLHELP: UInt32 = 15
DBG_STACKFAULT: UInt32 = 16
DBG_WOWINIT: UInt32 = 17
DBG_TEMPBP: UInt32 = 18
DBG_MODMOVE: UInt32 = 19
DBG_INIT: UInt32 = 20
DBG_GPFAULT2: UInt32 = 21
VDMEVENT_NEEDS_INTERACTIVE: UInt32 = 32768
VDMEVENT_VERBOSE: UInt32 = 16384
VDMEVENT_PE: UInt32 = 8192
VDMEVENT_ALLFLAGS: UInt32 = 57344
VDMEVENT_V86: UInt32 = 1
VDMEVENT_PM16: UInt32 = 2
MAX_MODULE_NAME: UInt32 = 9
MAX_PATH16: UInt32 = 255
SN_CODE: UInt32 = 0
SN_DATA: UInt32 = 1
SN_V86: UInt32 = 2
GLOBAL_ALL: UInt32 = 0
GLOBAL_LRU: UInt32 = 1
GLOBAL_FREE: UInt32 = 2
GT_UNKNOWN: UInt32 = 0
GT_DGROUP: UInt32 = 1
GT_DATA: UInt32 = 2
GT_CODE: UInt32 = 3
GT_TASK: UInt32 = 4
GT_RESOURCE: UInt32 = 5
GT_MODULE: UInt32 = 6
GT_FREE: UInt32 = 7
GT_INTERNAL: UInt32 = 8
GT_SENTINEL: UInt32 = 9
GT_BURGERMASTER: UInt32 = 10
GD_USERDEFINED: UInt32 = 0
GD_CURSORCOMPONENT: UInt32 = 1
GD_BITMAP: UInt32 = 2
GD_ICONCOMPONENT: UInt32 = 3
GD_MENU: UInt32 = 4
GD_DIALOG: UInt32 = 5
GD_STRING: UInt32 = 6
GD_FONTDIR: UInt32 = 7
GD_FONT: UInt32 = 8
GD_ACCELERATORS: UInt32 = 9
GD_RCDATA: UInt32 = 10
GD_ERRTABLE: UInt32 = 11
GD_CURSOR: UInt32 = 12
GD_ICON: UInt32 = 14
GD_NAMETABLE: UInt32 = 15
GD_MAX_RESOURCE: UInt32 = 15
WOW_SYSTEM: UInt32 = 1
VDMDBG_BREAK_DOSTASK: UInt32 = 1
VDMDBG_BREAK_WOWTASK: UInt32 = 2
VDMDBG_BREAK_LOADDLL: UInt32 = 4
VDMDBG_BREAK_EXCEPTIONS: UInt32 = 8
VDMDBG_BREAK_DEBUGGER: UInt32 = 16
VDMDBG_TRACE_HISTORY: UInt32 = 128
VDMDBG_BREAK_DIVIDEBYZERO: UInt32 = 256
VDMDBG_INITIAL_FLAGS: UInt32 = 256
VDMDBG_MAX_SYMBOL_BUFFER: UInt32 = 256
VDMADDR_V86: UInt32 = 2
VDMADDR_PM16: UInt32 = 4
VDMADDR_PM32: UInt32 = 16
@winfunctype_pointer
def DEBUGEVENTPROC(param0: POINTER(win32more.System.Diagnostics.Debug.DEBUG_EVENT_head), param1: c_void_p) -> UInt32: ...
class GLOBALENTRY(Structure):
    dwSize: UInt32
    dwAddress: UInt32
    dwBlockSize: UInt32
    hBlock: win32more.Foundation.HANDLE
    wcLock: UInt16
    wcPageLock: UInt16
    wFlags: UInt16
    wHeapPresent: win32more.Foundation.BOOL
    hOwner: win32more.Foundation.HANDLE
    wType: UInt16
    wData: UInt16
    dwNext: UInt32
    dwNextAlt: UInt32
    _pack_ = 4
class IMAGE_NOTE(Structure):
    Module: win32more.Foundation.CHAR * 10
    FileName: win32more.Foundation.CHAR * 256
    hModule: UInt16
    hTask: UInt16
class MODULEENTRY(Structure):
    dwSize: UInt32
    szModule: win32more.Foundation.CHAR * 10
    hModule: win32more.Foundation.HANDLE
    wcUsage: UInt16
    szExePath: win32more.Foundation.CHAR * 256
    wNext: UInt16
    _pack_ = 4
@winfunctype_pointer
def PROCESSENUMPROC(dwProcessId: UInt32, dwAttributes: UInt32, lpUserDefined: win32more.Foundation.LPARAM) -> win32more.Foundation.BOOL: ...
class SEGMENT_NOTE(Structure):
    Selector1: UInt16
    Selector2: UInt16
    Segment: UInt16
    Module: win32more.Foundation.CHAR * 10
    FileName: win32more.Foundation.CHAR * 256
    Type: UInt16
    Length: UInt32
@winfunctype_pointer
def TASKENUMPROC(dwThreadId: UInt32, hMod16: UInt16, hTask16: UInt16, lpUserDefined: win32more.Foundation.LPARAM) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def TASKENUMPROCEX(dwThreadId: UInt32, hMod16: UInt16, hTask16: UInt16, pszModName: POINTER(SByte), pszFileName: POINTER(SByte), lpUserDefined: win32more.Foundation.LPARAM) -> win32more.Foundation.BOOL: ...
class TEMP_BP_NOTE(Structure):
    Seg: UInt16
    Offset: UInt32
    bPM: win32more.Foundation.BOOL
class VDM_SEGINFO(Structure):
    Selector: UInt16
    SegNumber: UInt16
    Length: UInt32
    Type: UInt16
    ModuleName: win32more.Foundation.CHAR * 9
    FileName: win32more.Foundation.CHAR * 255
@winfunctype_pointer
def VDMBREAKTHREADPROC(param0: win32more.Foundation.HANDLE) -> win32more.Foundation.BOOL: ...
class VDMCONTEXT(Structure):
    ContextFlags: UInt32
    Dr0: UInt32
    Dr1: UInt32
    Dr2: UInt32
    Dr3: UInt32
    Dr6: UInt32
    Dr7: UInt32
    FloatSave: win32more.System.Kernel.FLOATING_SAVE_AREA
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
class VDMCONTEXT_WITHOUT_XSAVE(Structure):
    ContextFlags: UInt32
    Dr0: UInt32
    Dr1: UInt32
    Dr2: UInt32
    Dr3: UInt32
    Dr6: UInt32
    Dr7: UInt32
    FloatSave: win32more.System.Kernel.FLOATING_SAVE_AREA
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
@winfunctype_pointer
def VDMDETECTWOWPROC() -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def VDMENUMPROCESSWOWPROC(param0: win32more.System.VirtualDosMachines.PROCESSENUMPROC, param1: win32more.Foundation.LPARAM) -> Int32: ...
@winfunctype_pointer
def VDMENUMTASKWOWEXPROC(param0: UInt32, param1: win32more.System.VirtualDosMachines.TASKENUMPROCEX, param2: win32more.Foundation.LPARAM) -> Int32: ...
@winfunctype_pointer
def VDMENUMTASKWOWPROC(param0: UInt32, param1: win32more.System.VirtualDosMachines.TASKENUMPROC, param2: win32more.Foundation.LPARAM) -> Int32: ...
@winfunctype_pointer
def VDMGETADDREXPRESSIONPROC(param0: win32more.Foundation.PSTR, param1: win32more.Foundation.PSTR, param2: POINTER(UInt16), param3: POINTER(UInt32), param4: POINTER(UInt16)) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def VDMGETCONTEXTPROC(param0: win32more.Foundation.HANDLE, param1: win32more.Foundation.HANDLE, param2: POINTER(win32more.System.VirtualDosMachines.VDMCONTEXT_head)) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def VDMGETDBGFLAGSPROC(param0: win32more.Foundation.HANDLE) -> UInt32: ...
@winfunctype_pointer
def VDMGETMODULESELECTORPROC(param0: win32more.Foundation.HANDLE, param1: win32more.Foundation.HANDLE, param2: UInt32, param3: win32more.Foundation.PSTR, param4: POINTER(UInt16)) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def VDMGETPOINTERPROC(param0: win32more.Foundation.HANDLE, param1: win32more.Foundation.HANDLE, param2: UInt16, param3: UInt32, param4: win32more.Foundation.BOOL) -> UInt32: ...
@winfunctype_pointer
def VDMGETSEGMENTINFOPROC(param0: UInt16, param1: UInt32, param2: win32more.Foundation.BOOL, param3: win32more.System.VirtualDosMachines.VDM_SEGINFO) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def VDMGETSELECTORMODULEPROC(param0: win32more.Foundation.HANDLE, param1: win32more.Foundation.HANDLE, param2: UInt16, param3: POINTER(UInt32), param4: win32more.Foundation.PSTR, param5: UInt32, param6: win32more.Foundation.PSTR, param7: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def VDMGETSYMBOLPROC(param0: win32more.Foundation.PSTR, param1: UInt16, param2: UInt32, param3: win32more.Foundation.BOOL, param4: win32more.Foundation.BOOL, param5: win32more.Foundation.PSTR, param6: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def VDMGETTHREADSELECTORENTRYPROC(param0: win32more.Foundation.HANDLE, param1: win32more.Foundation.HANDLE, param2: UInt32, param3: POINTER(win32more.System.VirtualDosMachines.VDMLDT_ENTRY_head)) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def VDMGLOBALFIRSTPROC(param0: win32more.Foundation.HANDLE, param1: win32more.Foundation.HANDLE, param2: POINTER(win32more.System.VirtualDosMachines.GLOBALENTRY_head), param3: UInt16, param4: win32more.System.VirtualDosMachines.DEBUGEVENTPROC, param5: c_void_p) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def VDMGLOBALNEXTPROC(param0: win32more.Foundation.HANDLE, param1: win32more.Foundation.HANDLE, param2: POINTER(win32more.System.VirtualDosMachines.GLOBALENTRY_head), param3: UInt16, param4: win32more.System.VirtualDosMachines.DEBUGEVENTPROC, param5: c_void_p) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def VDMISMODULELOADEDPROC(param0: win32more.Foundation.PSTR) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def VDMKILLWOWPROC() -> win32more.Foundation.BOOL: ...
class VDMLDT_ENTRY(Structure):
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
            _bitfield: UInt32
@winfunctype_pointer
def VDMMODULEFIRSTPROC(param0: win32more.Foundation.HANDLE, param1: win32more.Foundation.HANDLE, param2: POINTER(win32more.System.VirtualDosMachines.MODULEENTRY_head), param3: win32more.System.VirtualDosMachines.DEBUGEVENTPROC, param4: c_void_p) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def VDMMODULENEXTPROC(param0: win32more.Foundation.HANDLE, param1: win32more.Foundation.HANDLE, param2: POINTER(win32more.System.VirtualDosMachines.MODULEENTRY_head), param3: win32more.System.VirtualDosMachines.DEBUGEVENTPROC, param4: c_void_p) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def VDMPROCESSEXCEPTIONPROC(param0: POINTER(win32more.System.Diagnostics.Debug.DEBUG_EVENT_head)) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def VDMSETCONTEXTPROC(param0: win32more.Foundation.HANDLE, param1: win32more.Foundation.HANDLE, param2: POINTER(win32more.System.VirtualDosMachines.VDMCONTEXT_head)) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def VDMSETDBGFLAGSPROC(param0: win32more.Foundation.HANDLE, param1: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def VDMSTARTTASKINWOWPROC(param0: UInt32, param1: win32more.Foundation.PSTR, param2: UInt16) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def VDMTERMINATETASKINWOWPROC(param0: UInt32, param1: UInt16) -> win32more.Foundation.BOOL: ...
make_head(_module, 'DEBUGEVENTPROC')
make_head(_module, 'GLOBALENTRY')
make_head(_module, 'IMAGE_NOTE')
make_head(_module, 'MODULEENTRY')
make_head(_module, 'PROCESSENUMPROC')
make_head(_module, 'SEGMENT_NOTE')
make_head(_module, 'TASKENUMPROC')
make_head(_module, 'TASKENUMPROCEX')
make_head(_module, 'TEMP_BP_NOTE')
make_head(_module, 'VDM_SEGINFO')
make_head(_module, 'VDMBREAKTHREADPROC')
make_head(_module, 'VDMCONTEXT')
make_head(_module, 'VDMCONTEXT_WITHOUT_XSAVE')
make_head(_module, 'VDMDETECTWOWPROC')
make_head(_module, 'VDMENUMPROCESSWOWPROC')
make_head(_module, 'VDMENUMTASKWOWEXPROC')
make_head(_module, 'VDMENUMTASKWOWPROC')
make_head(_module, 'VDMGETADDREXPRESSIONPROC')
make_head(_module, 'VDMGETCONTEXTPROC')
make_head(_module, 'VDMGETDBGFLAGSPROC')
make_head(_module, 'VDMGETMODULESELECTORPROC')
make_head(_module, 'VDMGETPOINTERPROC')
make_head(_module, 'VDMGETSEGMENTINFOPROC')
make_head(_module, 'VDMGETSELECTORMODULEPROC')
make_head(_module, 'VDMGETSYMBOLPROC')
make_head(_module, 'VDMGETTHREADSELECTORENTRYPROC')
make_head(_module, 'VDMGLOBALFIRSTPROC')
make_head(_module, 'VDMGLOBALNEXTPROC')
make_head(_module, 'VDMISMODULELOADEDPROC')
make_head(_module, 'VDMKILLWOWPROC')
make_head(_module, 'VDMLDT_ENTRY')
make_head(_module, 'VDMMODULEFIRSTPROC')
make_head(_module, 'VDMMODULENEXTPROC')
make_head(_module, 'VDMPROCESSEXCEPTIONPROC')
make_head(_module, 'VDMSETCONTEXTPROC')
make_head(_module, 'VDMSETDBGFLAGSPROC')
make_head(_module, 'VDMSTARTTASKINWOWPROC')
make_head(_module, 'VDMTERMINATETASKINWOWPROC')
__all__ = [
    "DBG_ATTACH",
    "DBG_BREAK",
    "DBG_DIVOVERFLOW",
    "DBG_DLLSTART",
    "DBG_DLLSTOP",
    "DBG_GPFAULT",
    "DBG_GPFAULT2",
    "DBG_INIT",
    "DBG_INSTRFAULT",
    "DBG_MODFREE",
    "DBG_MODLOAD",
    "DBG_MODMOVE",
    "DBG_SEGFREE",
    "DBG_SEGLOAD",
    "DBG_SEGMOVE",
    "DBG_SINGLESTEP",
    "DBG_STACKFAULT",
    "DBG_TASKSTART",
    "DBG_TASKSTOP",
    "DBG_TEMPBP",
    "DBG_TOOLHELP",
    "DBG_WOWINIT",
    "DEBUGEVENTPROC",
    "GD_ACCELERATORS",
    "GD_BITMAP",
    "GD_CURSOR",
    "GD_CURSORCOMPONENT",
    "GD_DIALOG",
    "GD_ERRTABLE",
    "GD_FONT",
    "GD_FONTDIR",
    "GD_ICON",
    "GD_ICONCOMPONENT",
    "GD_MAX_RESOURCE",
    "GD_MENU",
    "GD_NAMETABLE",
    "GD_RCDATA",
    "GD_STRING",
    "GD_USERDEFINED",
    "GLOBALENTRY",
    "GLOBAL_ALL",
    "GLOBAL_FREE",
    "GLOBAL_LRU",
    "GT_BURGERMASTER",
    "GT_CODE",
    "GT_DATA",
    "GT_DGROUP",
    "GT_FREE",
    "GT_INTERNAL",
    "GT_MODULE",
    "GT_RESOURCE",
    "GT_SENTINEL",
    "GT_TASK",
    "GT_UNKNOWN",
    "IMAGE_NOTE",
    "MAX_MODULE_NAME",
    "MAX_PATH16",
    "MODULEENTRY",
    "PROCESSENUMPROC",
    "SEGMENT_NOTE",
    "SN_CODE",
    "SN_DATA",
    "SN_V86",
    "STATUS_VDM_EVENT",
    "TASKENUMPROC",
    "TASKENUMPROCEX",
    "TEMP_BP_NOTE",
    "V86FLAGS_ALIGNMENT",
    "V86FLAGS_AUXCARRY",
    "V86FLAGS_CARRY",
    "V86FLAGS_DIRECTION",
    "V86FLAGS_INTERRUPT",
    "V86FLAGS_IOPL",
    "V86FLAGS_IOPL_BITS",
    "V86FLAGS_OVERFLOW",
    "V86FLAGS_PARITY",
    "V86FLAGS_RESUME",
    "V86FLAGS_SIGN",
    "V86FLAGS_TRACE",
    "V86FLAGS_V86",
    "V86FLAGS_ZERO",
    "VDMADDR_PM16",
    "VDMADDR_PM32",
    "VDMADDR_V86",
    "VDMBREAKTHREADPROC",
    "VDMCONTEXT",
    "VDMCONTEXT_WITHOUT_XSAVE",
    "VDMCONTEXT_i386",
    "VDMCONTEXT_i486",
    "VDMDBG_BREAK_DEBUGGER",
    "VDMDBG_BREAK_DIVIDEBYZERO",
    "VDMDBG_BREAK_DOSTASK",
    "VDMDBG_BREAK_EXCEPTIONS",
    "VDMDBG_BREAK_LOADDLL",
    "VDMDBG_BREAK_WOWTASK",
    "VDMDBG_INITIAL_FLAGS",
    "VDMDBG_MAX_SYMBOL_BUFFER",
    "VDMDBG_TRACE_HISTORY",
    "VDMDETECTWOWPROC",
    "VDMENUMPROCESSWOWPROC",
    "VDMENUMTASKWOWEXPROC",
    "VDMENUMTASKWOWPROC",
    "VDMEVENT_ALLFLAGS",
    "VDMEVENT_NEEDS_INTERACTIVE",
    "VDMEVENT_PE",
    "VDMEVENT_PM16",
    "VDMEVENT_V86",
    "VDMEVENT_VERBOSE",
    "VDMGETADDREXPRESSIONPROC",
    "VDMGETCONTEXTPROC",
    "VDMGETDBGFLAGSPROC",
    "VDMGETMODULESELECTORPROC",
    "VDMGETPOINTERPROC",
    "VDMGETSEGMENTINFOPROC",
    "VDMGETSELECTORMODULEPROC",
    "VDMGETSYMBOLPROC",
    "VDMGETTHREADSELECTORENTRYPROC",
    "VDMGLOBALFIRSTPROC",
    "VDMGLOBALNEXTPROC",
    "VDMISMODULELOADEDPROC",
    "VDMKILLWOWPROC",
    "VDMLDT_ENTRY",
    "VDMMODULEFIRSTPROC",
    "VDMMODULENEXTPROC",
    "VDMPROCESSEXCEPTIONPROC",
    "VDMSETCONTEXTPROC",
    "VDMSETDBGFLAGSPROC",
    "VDMSTARTTASKINWOWPROC",
    "VDMTERMINATETASKINWOWPROC",
    "VDM_KGDT_R3_CODE",
    "VDM_MAXIMUM_SUPPORTED_EXTENSION",
    "VDM_SEGINFO",
    "WOW_SYSTEM",
]
