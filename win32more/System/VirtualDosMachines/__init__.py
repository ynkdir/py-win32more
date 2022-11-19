from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, PROPERTYKEY, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.Diagnostics.Debug
import win32more.System.Kernel
import win32more.System.VirtualDosMachines

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
VDMCONTEXT_i386 = 65536
VDMCONTEXT_i486 = 65536
VDM_KGDT_R3_CODE = 24
VDM_MAXIMUM_SUPPORTED_EXTENSION = 512
V86FLAGS_CARRY = 1
V86FLAGS_PARITY = 4
V86FLAGS_AUXCARRY = 16
V86FLAGS_ZERO = 64
V86FLAGS_SIGN = 128
V86FLAGS_TRACE = 256
V86FLAGS_INTERRUPT = 512
V86FLAGS_DIRECTION = 1024
V86FLAGS_OVERFLOW = 2048
V86FLAGS_IOPL = 12288
V86FLAGS_IOPL_BITS = 18
V86FLAGS_RESUME = 65536
V86FLAGS_V86 = 131072
V86FLAGS_ALIGNMENT = 262144
STATUS_VDM_EVENT = 1073741829
DBG_SEGLOAD = 0
DBG_SEGMOVE = 1
DBG_SEGFREE = 2
DBG_MODLOAD = 3
DBG_MODFREE = 4
DBG_SINGLESTEP = 5
DBG_BREAK = 6
DBG_GPFAULT = 7
DBG_DIVOVERFLOW = 8
DBG_INSTRFAULT = 9
DBG_TASKSTART = 10
DBG_TASKSTOP = 11
DBG_DLLSTART = 12
DBG_DLLSTOP = 13
DBG_ATTACH = 14
DBG_TOOLHELP = 15
DBG_STACKFAULT = 16
DBG_WOWINIT = 17
DBG_TEMPBP = 18
DBG_MODMOVE = 19
DBG_INIT = 20
DBG_GPFAULT2 = 21
VDMEVENT_NEEDS_INTERACTIVE = 32768
VDMEVENT_VERBOSE = 16384
VDMEVENT_PE = 8192
VDMEVENT_ALLFLAGS = 57344
VDMEVENT_V86 = 1
VDMEVENT_PM16 = 2
MAX_MODULE_NAME = 9
MAX_PATH16 = 255
SN_CODE = 0
SN_DATA = 1
SN_V86 = 2
GLOBAL_ALL = 0
GLOBAL_LRU = 1
GLOBAL_FREE = 2
GT_UNKNOWN = 0
GT_DGROUP = 1
GT_DATA = 2
GT_CODE = 3
GT_TASK = 4
GT_RESOURCE = 5
GT_MODULE = 6
GT_FREE = 7
GT_INTERNAL = 8
GT_SENTINEL = 9
GT_BURGERMASTER = 10
GD_USERDEFINED = 0
GD_CURSORCOMPONENT = 1
GD_BITMAP = 2
GD_ICONCOMPONENT = 3
GD_MENU = 4
GD_DIALOG = 5
GD_STRING = 6
GD_FONTDIR = 7
GD_FONT = 8
GD_ACCELERATORS = 9
GD_RCDATA = 10
GD_ERRTABLE = 11
GD_CURSOR = 12
GD_ICON = 14
GD_NAMETABLE = 15
GD_MAX_RESOURCE = 15
VDMDBG_BREAK_DOSTASK = 1
VDMDBG_BREAK_WOWTASK = 2
VDMDBG_BREAK_LOADDLL = 4
VDMDBG_BREAK_EXCEPTIONS = 8
VDMDBG_BREAK_DEBUGGER = 16
VDMDBG_TRACE_HISTORY = 128
VDMDBG_BREAK_DIVIDEBYZERO = 256
VDMDBG_INITIAL_FLAGS = 256
VDMDBG_MAX_SYMBOL_BUFFER = 256
VDMADDR_V86 = 2
VDMADDR_PM16 = 4
VDMADDR_PM32 = 16
def _define_VDMCONTEXT_head():
    class VDMCONTEXT(Structure):
        pass
    return VDMCONTEXT
def _define_VDMCONTEXT():
    VDMCONTEXT = win32more.System.VirtualDosMachines.VDMCONTEXT_head
    VDMCONTEXT._fields_ = [
        ("ContextFlags", UInt32),
        ("Dr0", UInt32),
        ("Dr1", UInt32),
        ("Dr2", UInt32),
        ("Dr3", UInt32),
        ("Dr6", UInt32),
        ("Dr7", UInt32),
        ("FloatSave", win32more.System.Kernel.FLOATING_SAVE_AREA),
        ("SegGs", UInt32),
        ("SegFs", UInt32),
        ("SegEs", UInt32),
        ("SegDs", UInt32),
        ("Edi", UInt32),
        ("Esi", UInt32),
        ("Ebx", UInt32),
        ("Edx", UInt32),
        ("Ecx", UInt32),
        ("Eax", UInt32),
        ("Ebp", UInt32),
        ("Eip", UInt32),
        ("SegCs", UInt32),
        ("EFlags", UInt32),
        ("Esp", UInt32),
        ("SegSs", UInt32),
        ("ExtendedRegisters", Byte * 512),
    ]
    return VDMCONTEXT
def _define_VDMLDT_ENTRY_head():
    class VDMLDT_ENTRY(Structure):
        pass
    return VDMLDT_ENTRY
def _define_VDMLDT_ENTRY():
    VDMLDT_ENTRY = win32more.System.VirtualDosMachines.VDMLDT_ENTRY_head
    class VDMLDT_ENTRY__HighWord_e__Union(Union):
        pass
    class VDMLDT_ENTRY__HighWord_e__Union__Bits_e__Struct(Structure):
        pass
    VDMLDT_ENTRY__HighWord_e__Union__Bits_e__Struct._fields_ = [
        ("_bitfield", UInt32),
    ]
    class VDMLDT_ENTRY__HighWord_e__Union__Bytes_e__Struct(Structure):
        pass
    VDMLDT_ENTRY__HighWord_e__Union__Bytes_e__Struct._fields_ = [
        ("BaseMid", Byte),
        ("Flags1", Byte),
        ("Flags2", Byte),
        ("BaseHi", Byte),
    ]
    VDMLDT_ENTRY__HighWord_e__Union._fields_ = [
        ("Bytes", VDMLDT_ENTRY__HighWord_e__Union__Bytes_e__Struct),
        ("Bits", VDMLDT_ENTRY__HighWord_e__Union__Bits_e__Struct),
    ]
    VDMLDT_ENTRY._fields_ = [
        ("LimitLow", UInt16),
        ("BaseLow", UInt16),
        ("HighWord", VDMLDT_ENTRY__HighWord_e__Union),
    ]
    return VDMLDT_ENTRY
def _define_VDMCONTEXT_WITHOUT_XSAVE_head():
    class VDMCONTEXT_WITHOUT_XSAVE(Structure):
        pass
    return VDMCONTEXT_WITHOUT_XSAVE
def _define_VDMCONTEXT_WITHOUT_XSAVE():
    VDMCONTEXT_WITHOUT_XSAVE = win32more.System.VirtualDosMachines.VDMCONTEXT_WITHOUT_XSAVE_head
    VDMCONTEXT_WITHOUT_XSAVE._fields_ = [
        ("ContextFlags", UInt32),
        ("Dr0", UInt32),
        ("Dr1", UInt32),
        ("Dr2", UInt32),
        ("Dr3", UInt32),
        ("Dr6", UInt32),
        ("Dr7", UInt32),
        ("FloatSave", win32more.System.Kernel.FLOATING_SAVE_AREA),
        ("SegGs", UInt32),
        ("SegFs", UInt32),
        ("SegEs", UInt32),
        ("SegDs", UInt32),
        ("Edi", UInt32),
        ("Esi", UInt32),
        ("Ebx", UInt32),
        ("Edx", UInt32),
        ("Ecx", UInt32),
        ("Eax", UInt32),
        ("Ebp", UInt32),
        ("Eip", UInt32),
        ("SegCs", UInt32),
        ("EFlags", UInt32),
        ("Esp", UInt32),
        ("SegSs", UInt32),
    ]
    return VDMCONTEXT_WITHOUT_XSAVE
def _define_SEGMENT_NOTE_head():
    class SEGMENT_NOTE(Structure):
        pass
    return SEGMENT_NOTE
def _define_SEGMENT_NOTE():
    SEGMENT_NOTE = win32more.System.VirtualDosMachines.SEGMENT_NOTE_head
    SEGMENT_NOTE._fields_ = [
        ("Selector1", UInt16),
        ("Selector2", UInt16),
        ("Segment", UInt16),
        ("Module", win32more.Foundation.CHAR * 10),
        ("FileName", win32more.Foundation.CHAR * 256),
        ("Type", UInt16),
        ("Length", UInt32),
    ]
    return SEGMENT_NOTE
def _define_IMAGE_NOTE_head():
    class IMAGE_NOTE(Structure):
        pass
    return IMAGE_NOTE
def _define_IMAGE_NOTE():
    IMAGE_NOTE = win32more.System.VirtualDosMachines.IMAGE_NOTE_head
    IMAGE_NOTE._fields_ = [
        ("Module", win32more.Foundation.CHAR * 10),
        ("FileName", win32more.Foundation.CHAR * 256),
        ("hModule", UInt16),
        ("hTask", UInt16),
    ]
    return IMAGE_NOTE
def _define_MODULEENTRY_head():
    class MODULEENTRY(Structure):
        pass
    return MODULEENTRY
def _define_MODULEENTRY():
    MODULEENTRY = win32more.System.VirtualDosMachines.MODULEENTRY_head
    MODULEENTRY._pack_ = 4
    MODULEENTRY._fields_ = [
        ("dwSize", UInt32),
        ("szModule", win32more.Foundation.CHAR * 10),
        ("hModule", win32more.Foundation.HANDLE),
        ("wcUsage", UInt16),
        ("szExePath", win32more.Foundation.CHAR * 256),
        ("wNext", UInt16),
    ]
    return MODULEENTRY
def _define_TEMP_BP_NOTE_head():
    class TEMP_BP_NOTE(Structure):
        pass
    return TEMP_BP_NOTE
def _define_TEMP_BP_NOTE():
    TEMP_BP_NOTE = win32more.System.VirtualDosMachines.TEMP_BP_NOTE_head
    TEMP_BP_NOTE._fields_ = [
        ("Seg", UInt16),
        ("Offset", UInt32),
        ("bPM", win32more.Foundation.BOOL),
    ]
    return TEMP_BP_NOTE
def _define_VDM_SEGINFO_head():
    class VDM_SEGINFO(Structure):
        pass
    return VDM_SEGINFO
def _define_VDM_SEGINFO():
    VDM_SEGINFO = win32more.System.VirtualDosMachines.VDM_SEGINFO_head
    VDM_SEGINFO._fields_ = [
        ("Selector", UInt16),
        ("SegNumber", UInt16),
        ("Length", UInt32),
        ("Type", UInt16),
        ("ModuleName", win32more.Foundation.CHAR * 9),
        ("FileName", win32more.Foundation.CHAR * 255),
    ]
    return VDM_SEGINFO
def _define_GLOBALENTRY_head():
    class GLOBALENTRY(Structure):
        pass
    return GLOBALENTRY
def _define_GLOBALENTRY():
    GLOBALENTRY = win32more.System.VirtualDosMachines.GLOBALENTRY_head
    GLOBALENTRY._pack_ = 4
    GLOBALENTRY._fields_ = [
        ("dwSize", UInt32),
        ("dwAddress", UInt32),
        ("dwBlockSize", UInt32),
        ("hBlock", win32more.Foundation.HANDLE),
        ("wcLock", UInt16),
        ("wcPageLock", UInt16),
        ("wFlags", UInt16),
        ("wHeapPresent", win32more.Foundation.BOOL),
        ("hOwner", win32more.Foundation.HANDLE),
        ("wType", UInt16),
        ("wData", UInt16),
        ("dwNext", UInt32),
        ("dwNextAlt", UInt32),
    ]
    return GLOBALENTRY
def _define_DEBUGEVENTPROC():
    return CFUNCTYPE(UInt32,POINTER(win32more.System.Diagnostics.Debug.DEBUG_EVENT_head),c_void_p, use_last_error=False)
def _define_PROCESSENUMPROC():
    return CFUNCTYPE(win32more.Foundation.BOOL,UInt32,UInt32,win32more.Foundation.LPARAM, use_last_error=False)
def _define_TASKENUMPROC():
    return CFUNCTYPE(win32more.Foundation.BOOL,UInt32,UInt16,UInt16,win32more.Foundation.LPARAM, use_last_error=False)
def _define_TASKENUMPROCEX():
    return CFUNCTYPE(win32more.Foundation.BOOL,UInt32,UInt16,UInt16,POINTER(SByte),POINTER(SByte),win32more.Foundation.LPARAM, use_last_error=False)
def _define_VDMPROCESSEXCEPTIONPROC():
    return CFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Diagnostics.Debug.DEBUG_EVENT_head), use_last_error=False)
def _define_VDMGETTHREADSELECTORENTRYPROC():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,UInt32,POINTER(win32more.System.VirtualDosMachines.VDMLDT_ENTRY_head), use_last_error=False)
def _define_VDMGETPOINTERPROC():
    return CFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,UInt16,UInt32,win32more.Foundation.BOOL, use_last_error=False)
def _define_VDMGETCONTEXTPROC():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,POINTER(win32more.System.VirtualDosMachines.VDMCONTEXT_head), use_last_error=False)
def _define_VDMSETCONTEXTPROC():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,POINTER(win32more.System.VirtualDosMachines.VDMCONTEXT_head), use_last_error=False)
def _define_VDMKILLWOWPROC():
    return CFUNCTYPE(win32more.Foundation.BOOL, use_last_error=False)
def _define_VDMDETECTWOWPROC():
    return CFUNCTYPE(win32more.Foundation.BOOL, use_last_error=False)
def _define_VDMBREAKTHREADPROC():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE, use_last_error=False)
def _define_VDMGETSELECTORMODULEPROC():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,UInt16,POINTER(UInt32),win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,UInt32, use_last_error=False)
def _define_VDMGETMODULESELECTORPROC():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,UInt32,win32more.Foundation.PSTR,POINTER(UInt16), use_last_error=False)
def _define_VDMMODULEFIRSTPROC():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,POINTER(win32more.System.VirtualDosMachines.MODULEENTRY_head),win32more.System.VirtualDosMachines.DEBUGEVENTPROC,c_void_p, use_last_error=False)
def _define_VDMMODULENEXTPROC():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,POINTER(win32more.System.VirtualDosMachines.MODULEENTRY_head),win32more.System.VirtualDosMachines.DEBUGEVENTPROC,c_void_p, use_last_error=False)
def _define_VDMGLOBALFIRSTPROC():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,POINTER(win32more.System.VirtualDosMachines.GLOBALENTRY_head),UInt16,win32more.System.VirtualDosMachines.DEBUGEVENTPROC,c_void_p, use_last_error=False)
def _define_VDMGLOBALNEXTPROC():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,POINTER(win32more.System.VirtualDosMachines.GLOBALENTRY_head),UInt16,win32more.System.VirtualDosMachines.DEBUGEVENTPROC,c_void_p, use_last_error=False)
def _define_VDMENUMPROCESSWOWPROC():
    return CFUNCTYPE(Int32,win32more.System.VirtualDosMachines.PROCESSENUMPROC,win32more.Foundation.LPARAM, use_last_error=False)
def _define_VDMENUMTASKWOWPROC():
    return CFUNCTYPE(Int32,UInt32,win32more.System.VirtualDosMachines.TASKENUMPROC,win32more.Foundation.LPARAM, use_last_error=False)
def _define_VDMENUMTASKWOWEXPROC():
    return CFUNCTYPE(Int32,UInt32,win32more.System.VirtualDosMachines.TASKENUMPROCEX,win32more.Foundation.LPARAM, use_last_error=False)
def _define_VDMTERMINATETASKINWOWPROC():
    return CFUNCTYPE(win32more.Foundation.BOOL,UInt32,UInt16, use_last_error=False)
def _define_VDMSTARTTASKINWOWPROC():
    return CFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.Foundation.PSTR,UInt16, use_last_error=False)
def _define_VDMGETDBGFLAGSPROC():
    return CFUNCTYPE(UInt32,win32more.Foundation.HANDLE, use_last_error=False)
def _define_VDMSETDBGFLAGSPROC():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32, use_last_error=False)
def _define_VDMISMODULELOADEDPROC():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR, use_last_error=False)
def _define_VDMGETSEGMENTINFOPROC():
    return CFUNCTYPE(win32more.Foundation.BOOL,UInt16,UInt32,win32more.Foundation.BOOL,win32more.System.VirtualDosMachines.VDM_SEGINFO, use_last_error=False)
def _define_VDMGETSYMBOLPROC():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,UInt16,UInt32,win32more.Foundation.BOOL,win32more.Foundation.BOOL,POINTER(Byte),POINTER(UInt32), use_last_error=False)
def _define_VDMGETADDREXPRESSIONPROC():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(UInt16),POINTER(UInt32),POINTER(UInt16), use_last_error=False)
__all__ = [
    "VDMCONTEXT_i386",
    "VDMCONTEXT_i486",
    "VDM_KGDT_R3_CODE",
    "VDM_MAXIMUM_SUPPORTED_EXTENSION",
    "V86FLAGS_CARRY",
    "V86FLAGS_PARITY",
    "V86FLAGS_AUXCARRY",
    "V86FLAGS_ZERO",
    "V86FLAGS_SIGN",
    "V86FLAGS_TRACE",
    "V86FLAGS_INTERRUPT",
    "V86FLAGS_DIRECTION",
    "V86FLAGS_OVERFLOW",
    "V86FLAGS_IOPL",
    "V86FLAGS_IOPL_BITS",
    "V86FLAGS_RESUME",
    "V86FLAGS_V86",
    "V86FLAGS_ALIGNMENT",
    "STATUS_VDM_EVENT",
    "DBG_SEGLOAD",
    "DBG_SEGMOVE",
    "DBG_SEGFREE",
    "DBG_MODLOAD",
    "DBG_MODFREE",
    "DBG_SINGLESTEP",
    "DBG_BREAK",
    "DBG_GPFAULT",
    "DBG_DIVOVERFLOW",
    "DBG_INSTRFAULT",
    "DBG_TASKSTART",
    "DBG_TASKSTOP",
    "DBG_DLLSTART",
    "DBG_DLLSTOP",
    "DBG_ATTACH",
    "DBG_TOOLHELP",
    "DBG_STACKFAULT",
    "DBG_WOWINIT",
    "DBG_TEMPBP",
    "DBG_MODMOVE",
    "DBG_INIT",
    "DBG_GPFAULT2",
    "VDMEVENT_NEEDS_INTERACTIVE",
    "VDMEVENT_VERBOSE",
    "VDMEVENT_PE",
    "VDMEVENT_ALLFLAGS",
    "VDMEVENT_V86",
    "VDMEVENT_PM16",
    "MAX_MODULE_NAME",
    "MAX_PATH16",
    "SN_CODE",
    "SN_DATA",
    "SN_V86",
    "GLOBAL_ALL",
    "GLOBAL_LRU",
    "GLOBAL_FREE",
    "GT_UNKNOWN",
    "GT_DGROUP",
    "GT_DATA",
    "GT_CODE",
    "GT_TASK",
    "GT_RESOURCE",
    "GT_MODULE",
    "GT_FREE",
    "GT_INTERNAL",
    "GT_SENTINEL",
    "GT_BURGERMASTER",
    "GD_USERDEFINED",
    "GD_CURSORCOMPONENT",
    "GD_BITMAP",
    "GD_ICONCOMPONENT",
    "GD_MENU",
    "GD_DIALOG",
    "GD_STRING",
    "GD_FONTDIR",
    "GD_FONT",
    "GD_ACCELERATORS",
    "GD_RCDATA",
    "GD_ERRTABLE",
    "GD_CURSOR",
    "GD_ICON",
    "GD_NAMETABLE",
    "GD_MAX_RESOURCE",
    "VDMDBG_BREAK_DOSTASK",
    "VDMDBG_BREAK_WOWTASK",
    "VDMDBG_BREAK_LOADDLL",
    "VDMDBG_BREAK_EXCEPTIONS",
    "VDMDBG_BREAK_DEBUGGER",
    "VDMDBG_TRACE_HISTORY",
    "VDMDBG_BREAK_DIVIDEBYZERO",
    "VDMDBG_INITIAL_FLAGS",
    "VDMDBG_MAX_SYMBOL_BUFFER",
    "VDMADDR_V86",
    "VDMADDR_PM16",
    "VDMADDR_PM32",
    "VDMCONTEXT",
    "VDMLDT_ENTRY",
    "VDMCONTEXT_WITHOUT_XSAVE",
    "SEGMENT_NOTE",
    "IMAGE_NOTE",
    "MODULEENTRY",
    "TEMP_BP_NOTE",
    "VDM_SEGINFO",
    "GLOBALENTRY",
    "DEBUGEVENTPROC",
    "PROCESSENUMPROC",
    "TASKENUMPROC",
    "TASKENUMPROCEX",
    "VDMPROCESSEXCEPTIONPROC",
    "VDMGETTHREADSELECTORENTRYPROC",
    "VDMGETPOINTERPROC",
    "VDMGETCONTEXTPROC",
    "VDMSETCONTEXTPROC",
    "VDMKILLWOWPROC",
    "VDMDETECTWOWPROC",
    "VDMBREAKTHREADPROC",
    "VDMGETSELECTORMODULEPROC",
    "VDMGETMODULESELECTORPROC",
    "VDMMODULEFIRSTPROC",
    "VDMMODULENEXTPROC",
    "VDMGLOBALFIRSTPROC",
    "VDMGLOBALNEXTPROC",
    "VDMENUMPROCESSWOWPROC",
    "VDMENUMTASKWOWPROC",
    "VDMENUMTASKWOWEXPROC",
    "VDMTERMINATETASKINWOWPROC",
    "VDMSTARTTASKINWOWPROC",
    "VDMGETDBGFLAGSPROC",
    "VDMSETDBGFLAGSPROC",
    "VDMISMODULELOADEDPROC",
    "VDMGETSEGMENTINFOPROC",
    "VDMGETSYMBOLPROC",
    "VDMGETADDREXPRESSIONPROC",
]
