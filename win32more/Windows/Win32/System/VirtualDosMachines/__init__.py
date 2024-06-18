from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Diagnostics.Debug
import win32more.Windows.Win32.System.Kernel
import win32more.Windows.Win32.System.VirtualDosMachines
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
def DEBUGEVENTPROC(param0: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.DEBUG_EVENT), param1: VoidPtr) -> UInt32: ...
class GLOBALENTRY(Structure):
    dwSize: UInt32
    dwAddress: UInt32
    dwBlockSize: UInt32
    hBlock: win32more.Windows.Win32.Foundation.HANDLE
    wcLock: UInt16
    wcPageLock: UInt16
    wFlags: UInt16
    wHeapPresent: win32more.Windows.Win32.Foundation.BOOL
    hOwner: win32more.Windows.Win32.Foundation.HANDLE
    wType: UInt16
    wData: UInt16
    dwNext: UInt32
    dwNextAlt: UInt32
    _pack_ = 4
class IMAGE_NOTE(Structure):
    Module: win32more.Windows.Win32.Foundation.CHAR * 10
    FileName: win32more.Windows.Win32.Foundation.CHAR * 256
    hModule: UInt16
    hTask: UInt16
class MODULEENTRY(Structure):
    dwSize: UInt32
    szModule: win32more.Windows.Win32.Foundation.CHAR * 10
    hModule: win32more.Windows.Win32.Foundation.HANDLE
    wcUsage: UInt16
    szExePath: win32more.Windows.Win32.Foundation.CHAR * 256
    wNext: UInt16
    _pack_ = 4
@winfunctype_pointer
def PROCESSENUMPROC(dwProcessId: UInt32, dwAttributes: UInt32, lpUserDefined: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.BOOL: ...
class SEGMENT_NOTE(Structure):
    Selector1: UInt16
    Selector2: UInt16
    Segment: UInt16
    Module: win32more.Windows.Win32.Foundation.CHAR * 10
    FileName: win32more.Windows.Win32.Foundation.CHAR * 256
    Type: UInt16
    Length: UInt32
@winfunctype_pointer
def TASKENUMPROC(dwThreadId: UInt32, hMod16: UInt16, hTask16: UInt16, lpUserDefined: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def TASKENUMPROCEX(dwThreadId: UInt32, hMod16: UInt16, hTask16: UInt16, pszModName: POINTER(SByte), pszFileName: POINTER(SByte), lpUserDefined: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.BOOL: ...
class TEMP_BP_NOTE(Structure):
    Seg: UInt16
    Offset: UInt32
    bPM: win32more.Windows.Win32.Foundation.BOOL
@winfunctype_pointer
def VDMBREAKTHREADPROC(param0: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X64,ARM64':
    class VDMCONTEXT(Structure):
        ContextFlags: UInt32
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
class VDMCONTEXT_WITHOUT_XSAVE(Structure):
    ContextFlags: UInt32
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
@winfunctype_pointer
def VDMDETECTWOWPROC() -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def VDMENUMPROCESSWOWPROC(param0: win32more.Windows.Win32.System.VirtualDosMachines.PROCESSENUMPROC, param1: win32more.Windows.Win32.Foundation.LPARAM) -> Int32: ...
@winfunctype_pointer
def VDMENUMTASKWOWEXPROC(param0: UInt32, param1: win32more.Windows.Win32.System.VirtualDosMachines.TASKENUMPROCEX, param2: win32more.Windows.Win32.Foundation.LPARAM) -> Int32: ...
@winfunctype_pointer
def VDMENUMTASKWOWPROC(param0: UInt32, param1: win32more.Windows.Win32.System.VirtualDosMachines.TASKENUMPROC, param2: win32more.Windows.Win32.Foundation.LPARAM) -> Int32: ...
@winfunctype_pointer
def VDMGETADDREXPRESSIONPROC(param0: win32more.Windows.Win32.Foundation.PSTR, param1: win32more.Windows.Win32.Foundation.PSTR, param2: POINTER(UInt16), param3: POINTER(UInt32), param4: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X64,ARM64':
    @winfunctype_pointer
    def VDMGETCONTEXTPROC(param0: win32more.Windows.Win32.Foundation.HANDLE, param1: win32more.Windows.Win32.Foundation.HANDLE, param2: POINTER(win32more.Windows.Win32.System.VirtualDosMachines.VDMCONTEXT)) -> win32more.Windows.Win32.Foundation.BOOL: ...
elif ARCH in 'X86':
    @winfunctype_pointer
    def VDMGETCONTEXTPROC(param0: win32more.Windows.Win32.Foundation.HANDLE, param1: win32more.Windows.Win32.Foundation.HANDLE, param2: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def VDMGETDBGFLAGSPROC(param0: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype_pointer
def VDMGETMODULESELECTORPROC(param0: win32more.Windows.Win32.Foundation.HANDLE, param1: win32more.Windows.Win32.Foundation.HANDLE, param2: UInt32, param3: win32more.Windows.Win32.Foundation.PSTR, param4: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def VDMGETPOINTERPROC(param0: win32more.Windows.Win32.Foundation.HANDLE, param1: win32more.Windows.Win32.Foundation.HANDLE, param2: UInt16, param3: UInt32, param4: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype_pointer
def VDMGETSEGMENTINFOPROC(param0: UInt16, param1: UInt32, param2: win32more.Windows.Win32.Foundation.BOOL, param3: win32more.Windows.Win32.System.VirtualDosMachines.VDM_SEGINFO) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def VDMGETSELECTORMODULEPROC(param0: win32more.Windows.Win32.Foundation.HANDLE, param1: win32more.Windows.Win32.Foundation.HANDLE, param2: UInt16, param3: POINTER(UInt32), param4: win32more.Windows.Win32.Foundation.PSTR, param5: UInt32, param6: win32more.Windows.Win32.Foundation.PSTR, param7: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def VDMGETSYMBOLPROC(param0: win32more.Windows.Win32.Foundation.PSTR, param1: UInt16, param2: UInt32, param3: win32more.Windows.Win32.Foundation.BOOL, param4: win32more.Windows.Win32.Foundation.BOOL, param5: win32more.Windows.Win32.Foundation.PSTR, param6: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X64,ARM64':
    @winfunctype_pointer
    def VDMGETTHREADSELECTORENTRYPROC(param0: win32more.Windows.Win32.Foundation.HANDLE, param1: win32more.Windows.Win32.Foundation.HANDLE, param2: UInt32, param3: POINTER(win32more.Windows.Win32.System.VirtualDosMachines.VDMLDT_ENTRY)) -> win32more.Windows.Win32.Foundation.BOOL: ...
elif ARCH in 'X86':
    @winfunctype_pointer
    def VDMGETTHREADSELECTORENTRYPROC(param0: win32more.Windows.Win32.Foundation.HANDLE, param1: win32more.Windows.Win32.Foundation.HANDLE, param2: UInt32, param3: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.LDT_ENTRY)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def VDMGLOBALFIRSTPROC(param0: win32more.Windows.Win32.Foundation.HANDLE, param1: win32more.Windows.Win32.Foundation.HANDLE, param2: POINTER(win32more.Windows.Win32.System.VirtualDosMachines.GLOBALENTRY), param3: UInt16, param4: win32more.Windows.Win32.System.VirtualDosMachines.DEBUGEVENTPROC, param5: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def VDMGLOBALNEXTPROC(param0: win32more.Windows.Win32.Foundation.HANDLE, param1: win32more.Windows.Win32.Foundation.HANDLE, param2: POINTER(win32more.Windows.Win32.System.VirtualDosMachines.GLOBALENTRY), param3: UInt16, param4: win32more.Windows.Win32.System.VirtualDosMachines.DEBUGEVENTPROC, param5: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def VDMISMODULELOADEDPROC(param0: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def VDMKILLWOWPROC() -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X64,ARM64':
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
@winfunctype_pointer
def VDMMODULEFIRSTPROC(param0: win32more.Windows.Win32.Foundation.HANDLE, param1: win32more.Windows.Win32.Foundation.HANDLE, param2: POINTER(win32more.Windows.Win32.System.VirtualDosMachines.MODULEENTRY), param3: win32more.Windows.Win32.System.VirtualDosMachines.DEBUGEVENTPROC, param4: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def VDMMODULENEXTPROC(param0: win32more.Windows.Win32.Foundation.HANDLE, param1: win32more.Windows.Win32.Foundation.HANDLE, param2: POINTER(win32more.Windows.Win32.System.VirtualDosMachines.MODULEENTRY), param3: win32more.Windows.Win32.System.VirtualDosMachines.DEBUGEVENTPROC, param4: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def VDMPROCESSEXCEPTIONPROC(param0: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.DEBUG_EVENT)) -> win32more.Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X64,ARM64':
    @winfunctype_pointer
    def VDMSETCONTEXTPROC(param0: win32more.Windows.Win32.Foundation.HANDLE, param1: win32more.Windows.Win32.Foundation.HANDLE, param2: POINTER(win32more.Windows.Win32.System.VirtualDosMachines.VDMCONTEXT)) -> win32more.Windows.Win32.Foundation.BOOL: ...
elif ARCH in 'X86':
    @winfunctype_pointer
    def VDMSETCONTEXTPROC(param0: win32more.Windows.Win32.Foundation.HANDLE, param1: win32more.Windows.Win32.Foundation.HANDLE, param2: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def VDMSETDBGFLAGSPROC(param0: win32more.Windows.Win32.Foundation.HANDLE, param1: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def VDMSTARTTASKINWOWPROC(param0: UInt32, param1: win32more.Windows.Win32.Foundation.PSTR, param2: UInt16) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def VDMTERMINATETASKINWOWPROC(param0: UInt32, param1: UInt16) -> win32more.Windows.Win32.Foundation.BOOL: ...
class VDM_SEGINFO(Structure):
    Selector: UInt16
    SegNumber: UInt16
    Length: UInt32
    Type: UInt16
    ModuleName: win32more.Windows.Win32.Foundation.CHAR * 9
    FileName: win32more.Windows.Win32.Foundation.CHAR * 255


make_ready(__name__)
