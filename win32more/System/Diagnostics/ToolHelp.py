from win32more import *
import win32more.System.Diagnostics.ToolHelp
import win32more.Foundation

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.System.Diagnostics.ToolHelp, name, eval(f"_define_{name}()"))
    return getattr(win32more.System.Diagnostics.ToolHelp, name)
MAX_MODULE_NAME32 = 255
HF32_DEFAULT = 1
HF32_SHARED = 2
CREATE_TOOLHELP_SNAPSHOT_FLAGS = UInt32
TH32CS_INHERIT = 2147483648
TH32CS_SNAPALL = 15
TH32CS_SNAPHEAPLIST = 1
TH32CS_SNAPMODULE = 8
TH32CS_SNAPMODULE32 = 16
TH32CS_SNAPPROCESS = 2
TH32CS_SNAPTHREAD = 4
HEAPENTRY32_FLAGS = UInt32
LF32_FIXED = 1
LF32_FREE = 2
LF32_MOVEABLE = 4
def _define_HEAPLIST32_head():
    class HEAPLIST32(Structure):
        pass
    return HEAPLIST32
def _define_HEAPLIST32():
    HEAPLIST32 = win32more.System.Diagnostics.ToolHelp.HEAPLIST32_head
    HEAPLIST32._fields_ = [
        ("dwSize", UIntPtr),
        ("th32ProcessID", UInt32),
        ("th32HeapID", UIntPtr),
        ("dwFlags", UInt32),
    ]
    return HEAPLIST32
def _define_HEAPENTRY32_head():
    class HEAPENTRY32(Structure):
        pass
    return HEAPENTRY32
def _define_HEAPENTRY32():
    HEAPENTRY32 = win32more.System.Diagnostics.ToolHelp.HEAPENTRY32_head
    HEAPENTRY32._fields_ = [
        ("dwSize", UIntPtr),
        ("hHandle", win32more.Foundation.HANDLE),
        ("dwAddress", UIntPtr),
        ("dwBlockSize", UIntPtr),
        ("dwFlags", win32more.System.Diagnostics.ToolHelp.HEAPENTRY32_FLAGS),
        ("dwLockCount", UInt32),
        ("dwResvd", UInt32),
        ("th32ProcessID", UInt32),
        ("th32HeapID", UIntPtr),
    ]
    return HEAPENTRY32
def _define_PROCESSENTRY32W_head():
    class PROCESSENTRY32W(Structure):
        pass
    return PROCESSENTRY32W
def _define_PROCESSENTRY32W():
    PROCESSENTRY32W = win32more.System.Diagnostics.ToolHelp.PROCESSENTRY32W_head
    PROCESSENTRY32W._fields_ = [
        ("dwSize", UInt32),
        ("cntUsage", UInt32),
        ("th32ProcessID", UInt32),
        ("th32DefaultHeapID", UIntPtr),
        ("th32ModuleID", UInt32),
        ("cntThreads", UInt32),
        ("th32ParentProcessID", UInt32),
        ("pcPriClassBase", Int32),
        ("dwFlags", UInt32),
        ("szExeFile", Char * 260),
    ]
    return PROCESSENTRY32W
def _define_PROCESSENTRY32_head():
    class PROCESSENTRY32(Structure):
        pass
    return PROCESSENTRY32
def _define_PROCESSENTRY32():
    PROCESSENTRY32 = win32more.System.Diagnostics.ToolHelp.PROCESSENTRY32_head
    PROCESSENTRY32._fields_ = [
        ("dwSize", UInt32),
        ("cntUsage", UInt32),
        ("th32ProcessID", UInt32),
        ("th32DefaultHeapID", UIntPtr),
        ("th32ModuleID", UInt32),
        ("cntThreads", UInt32),
        ("th32ParentProcessID", UInt32),
        ("pcPriClassBase", Int32),
        ("dwFlags", UInt32),
        ("szExeFile", win32more.Foundation.CHAR * 260),
    ]
    return PROCESSENTRY32
def _define_THREADENTRY32_head():
    class THREADENTRY32(Structure):
        pass
    return THREADENTRY32
def _define_THREADENTRY32():
    THREADENTRY32 = win32more.System.Diagnostics.ToolHelp.THREADENTRY32_head
    THREADENTRY32._fields_ = [
        ("dwSize", UInt32),
        ("cntUsage", UInt32),
        ("th32ThreadID", UInt32),
        ("th32OwnerProcessID", UInt32),
        ("tpBasePri", Int32),
        ("tpDeltaPri", Int32),
        ("dwFlags", UInt32),
    ]
    return THREADENTRY32
def _define_MODULEENTRY32W_head():
    class MODULEENTRY32W(Structure):
        pass
    return MODULEENTRY32W
def _define_MODULEENTRY32W():
    MODULEENTRY32W = win32more.System.Diagnostics.ToolHelp.MODULEENTRY32W_head
    MODULEENTRY32W._fields_ = [
        ("dwSize", UInt32),
        ("th32ModuleID", UInt32),
        ("th32ProcessID", UInt32),
        ("GlblcntUsage", UInt32),
        ("ProccntUsage", UInt32),
        ("modBaseAddr", c_char_p_no),
        ("modBaseSize", UInt32),
        ("hModule", win32more.Foundation.HINSTANCE),
        ("szModule", Char * 256),
        ("szExePath", Char * 260),
    ]
    return MODULEENTRY32W
def _define_MODULEENTRY32_head():
    class MODULEENTRY32(Structure):
        pass
    return MODULEENTRY32
def _define_MODULEENTRY32():
    MODULEENTRY32 = win32more.System.Diagnostics.ToolHelp.MODULEENTRY32_head
    MODULEENTRY32._fields_ = [
        ("dwSize", UInt32),
        ("th32ModuleID", UInt32),
        ("th32ProcessID", UInt32),
        ("GlblcntUsage", UInt32),
        ("ProccntUsage", UInt32),
        ("modBaseAddr", c_char_p_no),
        ("modBaseSize", UInt32),
        ("hModule", win32more.Foundation.HINSTANCE),
        ("szModule", win32more.Foundation.CHAR * 256),
        ("szExePath", win32more.Foundation.CHAR * 260),
    ]
    return MODULEENTRY32
def _define_CreateToolhelp32Snapshot():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.System.Diagnostics.ToolHelp.CREATE_TOOLHELP_SNAPSHOT_FLAGS,UInt32, use_last_error=True)(("CreateToolhelp32Snapshot", windll["KERNEL32"]), ((1, 'dwFlags'),(1, 'th32ProcessID'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Heap32ListFirst():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.Diagnostics.ToolHelp.HEAPLIST32_head), use_last_error=True)(("Heap32ListFirst", windll["KERNEL32"]), ((1, 'hSnapshot'),(1, 'lphl'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Heap32ListNext():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.Diagnostics.ToolHelp.HEAPLIST32_head), use_last_error=True)(("Heap32ListNext", windll["KERNEL32"]), ((1, 'hSnapshot'),(1, 'lphl'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Heap32First():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Diagnostics.ToolHelp.HEAPENTRY32_head),UInt32,UIntPtr, use_last_error=True)(("Heap32First", windll["KERNEL32"]), ((1, 'lphe'),(1, 'th32ProcessID'),(1, 'th32HeapID'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Heap32Next():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Diagnostics.ToolHelp.HEAPENTRY32_head), use_last_error=True)(("Heap32Next", windll["KERNEL32"]), ((1, 'lphe'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Toolhelp32ReadProcessMemory():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,c_void_p,c_void_p,UIntPtr,POINTER(UIntPtr), use_last_error=False)(("Toolhelp32ReadProcessMemory", windll["KERNEL32"]), ((1, 'th32ProcessID'),(1, 'lpBaseAddress'),(1, 'lpBuffer'),(1, 'cbRead'),(1, 'lpNumberOfBytesRead'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Process32FirstW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.Diagnostics.ToolHelp.PROCESSENTRY32W_head), use_last_error=True)(("Process32FirstW", windll["KERNEL32"]), ((1, 'hSnapshot'),(1, 'lppe'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Process32NextW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.Diagnostics.ToolHelp.PROCESSENTRY32W_head), use_last_error=True)(("Process32NextW", windll["KERNEL32"]), ((1, 'hSnapshot'),(1, 'lppe'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Process32First():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.Diagnostics.ToolHelp.PROCESSENTRY32_head), use_last_error=True)(("Process32First", windll["KERNEL32"]), ((1, 'hSnapshot'),(1, 'lppe'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Process32Next():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.Diagnostics.ToolHelp.PROCESSENTRY32_head), use_last_error=True)(("Process32Next", windll["KERNEL32"]), ((1, 'hSnapshot'),(1, 'lppe'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Thread32First():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.Diagnostics.ToolHelp.THREADENTRY32_head), use_last_error=True)(("Thread32First", windll["KERNEL32"]), ((1, 'hSnapshot'),(1, 'lpte'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Thread32Next():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.Diagnostics.ToolHelp.THREADENTRY32_head), use_last_error=True)(("Thread32Next", windll["KERNEL32"]), ((1, 'hSnapshot'),(1, 'lpte'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Module32FirstW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.Diagnostics.ToolHelp.MODULEENTRY32W_head), use_last_error=True)(("Module32FirstW", windll["KERNEL32"]), ((1, 'hSnapshot'),(1, 'lpme'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Module32NextW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.Diagnostics.ToolHelp.MODULEENTRY32W_head), use_last_error=True)(("Module32NextW", windll["KERNEL32"]), ((1, 'hSnapshot'),(1, 'lpme'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Module32First():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.Diagnostics.ToolHelp.MODULEENTRY32_head), use_last_error=True)(("Module32First", windll["KERNEL32"]), ((1, 'hSnapshot'),(1, 'lpme'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Module32Next():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.Diagnostics.ToolHelp.MODULEENTRY32_head), use_last_error=True)(("Module32Next", windll["KERNEL32"]), ((1, 'hSnapshot'),(1, 'lpme'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "MAX_MODULE_NAME32",
    "HF32_DEFAULT",
    "HF32_SHARED",
    "CREATE_TOOLHELP_SNAPSHOT_FLAGS",
    "TH32CS_INHERIT",
    "TH32CS_SNAPALL",
    "TH32CS_SNAPHEAPLIST",
    "TH32CS_SNAPMODULE",
    "TH32CS_SNAPMODULE32",
    "TH32CS_SNAPPROCESS",
    "TH32CS_SNAPTHREAD",
    "HEAPENTRY32_FLAGS",
    "LF32_FIXED",
    "LF32_FREE",
    "LF32_MOVEABLE",
    "HEAPLIST32",
    "HEAPENTRY32",
    "PROCESSENTRY32W",
    "PROCESSENTRY32",
    "THREADENTRY32",
    "MODULEENTRY32W",
    "MODULEENTRY32",
    "CreateToolhelp32Snapshot",
    "Heap32ListFirst",
    "Heap32ListNext",
    "Heap32First",
    "Heap32Next",
    "Toolhelp32ReadProcessMemory",
    "Process32FirstW",
    "Process32NextW",
    "Process32First",
    "Process32Next",
    "Thread32First",
    "Thread32Next",
    "Module32FirstW",
    "Module32NextW",
    "Module32First",
    "Module32Next",
]
