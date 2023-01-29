from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.System.Diagnostics.ToolHelp
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
MAX_MODULE_NAME32: UInt32 = 255
HF32_DEFAULT: UInt32 = 1
HF32_SHARED: UInt32 = 2
@winfunctype('KERNEL32.dll')
def CreateToolhelp32Snapshot(dwFlags: win32more.System.Diagnostics.ToolHelp.CREATE_TOOLHELP_SNAPSHOT_FLAGS, th32ProcessID: UInt32) -> win32more.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def Heap32ListFirst(hSnapshot: win32more.Foundation.HANDLE, lphl: POINTER(win32more.System.Diagnostics.ToolHelp.HEAPLIST32_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def Heap32ListNext(hSnapshot: win32more.Foundation.HANDLE, lphl: POINTER(win32more.System.Diagnostics.ToolHelp.HEAPLIST32_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def Heap32First(lphe: POINTER(win32more.System.Diagnostics.ToolHelp.HEAPENTRY32_head), th32ProcessID: UInt32, th32HeapID: UIntPtr) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def Heap32Next(lphe: POINTER(win32more.System.Diagnostics.ToolHelp.HEAPENTRY32_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def Toolhelp32ReadProcessMemory(th32ProcessID: UInt32, lpBaseAddress: c_void_p, lpBuffer: c_void_p, cbRead: UIntPtr, lpNumberOfBytesRead: POINTER(UIntPtr)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def Process32FirstW(hSnapshot: win32more.Foundation.HANDLE, lppe: POINTER(win32more.System.Diagnostics.ToolHelp.PROCESSENTRY32W_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def Process32NextW(hSnapshot: win32more.Foundation.HANDLE, lppe: POINTER(win32more.System.Diagnostics.ToolHelp.PROCESSENTRY32W_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def Process32First(hSnapshot: win32more.Foundation.HANDLE, lppe: POINTER(win32more.System.Diagnostics.ToolHelp.PROCESSENTRY32_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def Process32Next(hSnapshot: win32more.Foundation.HANDLE, lppe: POINTER(win32more.System.Diagnostics.ToolHelp.PROCESSENTRY32_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def Thread32First(hSnapshot: win32more.Foundation.HANDLE, lpte: POINTER(win32more.System.Diagnostics.ToolHelp.THREADENTRY32_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def Thread32Next(hSnapshot: win32more.Foundation.HANDLE, lpte: POINTER(win32more.System.Diagnostics.ToolHelp.THREADENTRY32_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def Module32FirstW(hSnapshot: win32more.Foundation.HANDLE, lpme: POINTER(win32more.System.Diagnostics.ToolHelp.MODULEENTRY32W_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def Module32NextW(hSnapshot: win32more.Foundation.HANDLE, lpme: POINTER(win32more.System.Diagnostics.ToolHelp.MODULEENTRY32W_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def Module32First(hSnapshot: win32more.Foundation.HANDLE, lpme: POINTER(win32more.System.Diagnostics.ToolHelp.MODULEENTRY32_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def Module32Next(hSnapshot: win32more.Foundation.HANDLE, lpme: POINTER(win32more.System.Diagnostics.ToolHelp.MODULEENTRY32_head)) -> win32more.Foundation.BOOL: ...
CREATE_TOOLHELP_SNAPSHOT_FLAGS = UInt32
TH32CS_INHERIT: CREATE_TOOLHELP_SNAPSHOT_FLAGS = 2147483648
TH32CS_SNAPALL: CREATE_TOOLHELP_SNAPSHOT_FLAGS = 15
TH32CS_SNAPHEAPLIST: CREATE_TOOLHELP_SNAPSHOT_FLAGS = 1
TH32CS_SNAPMODULE: CREATE_TOOLHELP_SNAPSHOT_FLAGS = 8
TH32CS_SNAPMODULE32: CREATE_TOOLHELP_SNAPSHOT_FLAGS = 16
TH32CS_SNAPPROCESS: CREATE_TOOLHELP_SNAPSHOT_FLAGS = 2
TH32CS_SNAPTHREAD: CREATE_TOOLHELP_SNAPSHOT_FLAGS = 4
class HEAPENTRY32(Structure):
    dwSize: UIntPtr
    hHandle: win32more.Foundation.HANDLE
    dwAddress: UIntPtr
    dwBlockSize: UIntPtr
    dwFlags: win32more.System.Diagnostics.ToolHelp.HEAPENTRY32_FLAGS
    dwLockCount: UInt32
    dwResvd: UInt32
    th32ProcessID: UInt32
    th32HeapID: UIntPtr
HEAPENTRY32_FLAGS = UInt32
LF32_FIXED: HEAPENTRY32_FLAGS = 1
LF32_FREE: HEAPENTRY32_FLAGS = 2
LF32_MOVEABLE: HEAPENTRY32_FLAGS = 4
class HEAPLIST32(Structure):
    dwSize: UIntPtr
    th32ProcessID: UInt32
    th32HeapID: UIntPtr
    dwFlags: UInt32
class MODULEENTRY32(Structure):
    dwSize: UInt32
    th32ModuleID: UInt32
    th32ProcessID: UInt32
    GlblcntUsage: UInt32
    ProccntUsage: UInt32
    modBaseAddr: c_char_p_no
    modBaseSize: UInt32
    hModule: win32more.Foundation.HINSTANCE
    szModule: win32more.Foundation.CHAR * 256
    szExePath: win32more.Foundation.CHAR * 260
class MODULEENTRY32W(Structure):
    dwSize: UInt32
    th32ModuleID: UInt32
    th32ProcessID: UInt32
    GlblcntUsage: UInt32
    ProccntUsage: UInt32
    modBaseAddr: c_char_p_no
    modBaseSize: UInt32
    hModule: win32more.Foundation.HINSTANCE
    szModule: Char * 256
    szExePath: Char * 260
class PROCESSENTRY32(Structure):
    dwSize: UInt32
    cntUsage: UInt32
    th32ProcessID: UInt32
    th32DefaultHeapID: UIntPtr
    th32ModuleID: UInt32
    cntThreads: UInt32
    th32ParentProcessID: UInt32
    pcPriClassBase: Int32
    dwFlags: UInt32
    szExeFile: win32more.Foundation.CHAR * 260
class PROCESSENTRY32W(Structure):
    dwSize: UInt32
    cntUsage: UInt32
    th32ProcessID: UInt32
    th32DefaultHeapID: UIntPtr
    th32ModuleID: UInt32
    cntThreads: UInt32
    th32ParentProcessID: UInt32
    pcPriClassBase: Int32
    dwFlags: UInt32
    szExeFile: Char * 260
class THREADENTRY32(Structure):
    dwSize: UInt32
    cntUsage: UInt32
    th32ThreadID: UInt32
    th32OwnerProcessID: UInt32
    tpBasePri: Int32
    tpDeltaPri: Int32
    dwFlags: UInt32
make_head(_module, 'HEAPENTRY32')
make_head(_module, 'HEAPLIST32')
make_head(_module, 'MODULEENTRY32')
make_head(_module, 'MODULEENTRY32W')
make_head(_module, 'PROCESSENTRY32')
make_head(_module, 'PROCESSENTRY32W')
make_head(_module, 'THREADENTRY32')
__all__ = [
    "CREATE_TOOLHELP_SNAPSHOT_FLAGS",
    "CreateToolhelp32Snapshot",
    "HEAPENTRY32",
    "HEAPENTRY32_FLAGS",
    "HEAPLIST32",
    "HF32_DEFAULT",
    "HF32_SHARED",
    "Heap32First",
    "Heap32ListFirst",
    "Heap32ListNext",
    "Heap32Next",
    "LF32_FIXED",
    "LF32_FREE",
    "LF32_MOVEABLE",
    "MAX_MODULE_NAME32",
    "MODULEENTRY32",
    "MODULEENTRY32W",
    "Module32First",
    "Module32FirstW",
    "Module32Next",
    "Module32NextW",
    "PROCESSENTRY32",
    "PROCESSENTRY32W",
    "Process32First",
    "Process32FirstW",
    "Process32Next",
    "Process32NextW",
    "TH32CS_INHERIT",
    "TH32CS_SNAPALL",
    "TH32CS_SNAPHEAPLIST",
    "TH32CS_SNAPMODULE",
    "TH32CS_SNAPMODULE32",
    "TH32CS_SNAPPROCESS",
    "TH32CS_SNAPTHREAD",
    "THREADENTRY32",
    "Thread32First",
    "Thread32Next",
    "Toolhelp32ReadProcessMemory",
]
_arch_optional = [
]
