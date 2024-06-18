from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Diagnostics.ToolHelp
MAX_MODULE_NAME32: UInt32 = 255
HF32_DEFAULT: UInt32 = 1
HF32_SHARED: UInt32 = 2
@winfunctype('KERNEL32.dll')
def CreateToolhelp32Snapshot(dwFlags: win32more.Windows.Win32.System.Diagnostics.ToolHelp.CREATE_TOOLHELP_SNAPSHOT_FLAGS, th32ProcessID: UInt32) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def Heap32ListFirst(hSnapshot: win32more.Windows.Win32.Foundation.HANDLE, lphl: POINTER(win32more.Windows.Win32.System.Diagnostics.ToolHelp.HEAPLIST32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def Heap32ListNext(hSnapshot: win32more.Windows.Win32.Foundation.HANDLE, lphl: POINTER(win32more.Windows.Win32.System.Diagnostics.ToolHelp.HEAPLIST32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def Heap32First(lphe: POINTER(win32more.Windows.Win32.System.Diagnostics.ToolHelp.HEAPENTRY32), th32ProcessID: UInt32, th32HeapID: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def Heap32Next(lphe: POINTER(win32more.Windows.Win32.System.Diagnostics.ToolHelp.HEAPENTRY32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def Toolhelp32ReadProcessMemory(th32ProcessID: UInt32, lpBaseAddress: VoidPtr, lpBuffer: VoidPtr, cbRead: UIntPtr, lpNumberOfBytesRead: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def Process32FirstW(hSnapshot: win32more.Windows.Win32.Foundation.HANDLE, lppe: POINTER(win32more.Windows.Win32.System.Diagnostics.ToolHelp.PROCESSENTRY32W)) -> win32more.Windows.Win32.Foundation.BOOL: ...
Process32First = UnicodeAlias('Process32FirstW')
@winfunctype('KERNEL32.dll')
def Process32NextW(hSnapshot: win32more.Windows.Win32.Foundation.HANDLE, lppe: POINTER(win32more.Windows.Win32.System.Diagnostics.ToolHelp.PROCESSENTRY32W)) -> win32more.Windows.Win32.Foundation.BOOL: ...
Process32Next = UnicodeAlias('Process32NextW')
@winfunctype('KERNEL32.dll')
def Thread32First(hSnapshot: win32more.Windows.Win32.Foundation.HANDLE, lpte: POINTER(win32more.Windows.Win32.System.Diagnostics.ToolHelp.THREADENTRY32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def Thread32Next(hSnapshot: win32more.Windows.Win32.Foundation.HANDLE, lpte: POINTER(win32more.Windows.Win32.System.Diagnostics.ToolHelp.THREADENTRY32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def Module32FirstW(hSnapshot: win32more.Windows.Win32.Foundation.HANDLE, lpme: POINTER(win32more.Windows.Win32.System.Diagnostics.ToolHelp.MODULEENTRY32W)) -> win32more.Windows.Win32.Foundation.BOOL: ...
Module32First = UnicodeAlias('Module32FirstW')
@winfunctype('KERNEL32.dll')
def Module32NextW(hSnapshot: win32more.Windows.Win32.Foundation.HANDLE, lpme: POINTER(win32more.Windows.Win32.System.Diagnostics.ToolHelp.MODULEENTRY32W)) -> win32more.Windows.Win32.Foundation.BOOL: ...
Module32Next = UnicodeAlias('Module32NextW')
CREATE_TOOLHELP_SNAPSHOT_FLAGS = UInt32
TH32CS_INHERIT: win32more.Windows.Win32.System.Diagnostics.ToolHelp.CREATE_TOOLHELP_SNAPSHOT_FLAGS = 2147483648
TH32CS_SNAPALL: win32more.Windows.Win32.System.Diagnostics.ToolHelp.CREATE_TOOLHELP_SNAPSHOT_FLAGS = 15
TH32CS_SNAPHEAPLIST: win32more.Windows.Win32.System.Diagnostics.ToolHelp.CREATE_TOOLHELP_SNAPSHOT_FLAGS = 1
TH32CS_SNAPMODULE: win32more.Windows.Win32.System.Diagnostics.ToolHelp.CREATE_TOOLHELP_SNAPSHOT_FLAGS = 8
TH32CS_SNAPMODULE32: win32more.Windows.Win32.System.Diagnostics.ToolHelp.CREATE_TOOLHELP_SNAPSHOT_FLAGS = 16
TH32CS_SNAPPROCESS: win32more.Windows.Win32.System.Diagnostics.ToolHelp.CREATE_TOOLHELP_SNAPSHOT_FLAGS = 2
TH32CS_SNAPTHREAD: win32more.Windows.Win32.System.Diagnostics.ToolHelp.CREATE_TOOLHELP_SNAPSHOT_FLAGS = 4
class HEAPENTRY32(Structure):
    dwSize: UIntPtr
    hHandle: win32more.Windows.Win32.Foundation.HANDLE
    dwAddress: UIntPtr
    dwBlockSize: UIntPtr
    dwFlags: win32more.Windows.Win32.System.Diagnostics.ToolHelp.HEAPENTRY32_FLAGS
    dwLockCount: UInt32
    dwResvd: UInt32
    th32ProcessID: UInt32
    th32HeapID: UIntPtr
HEAPENTRY32_FLAGS = UInt32
LF32_FIXED: win32more.Windows.Win32.System.Diagnostics.ToolHelp.HEAPENTRY32_FLAGS = 1
LF32_FREE: win32more.Windows.Win32.System.Diagnostics.ToolHelp.HEAPENTRY32_FLAGS = 2
LF32_MOVEABLE: win32more.Windows.Win32.System.Diagnostics.ToolHelp.HEAPENTRY32_FLAGS = 4
class HEAPLIST32(Structure):
    dwSize: UIntPtr
    th32ProcessID: UInt32
    th32HeapID: UIntPtr
    dwFlags: UInt32
class MODULEENTRY32W(Structure):
    dwSize: UInt32
    th32ModuleID: UInt32
    th32ProcessID: UInt32
    GlblcntUsage: UInt32
    ProccntUsage: UInt32
    modBaseAddr: POINTER(Byte)
    modBaseSize: UInt32
    hModule: win32more.Windows.Win32.Foundation.HMODULE
    szModule: Char * 256
    szExePath: Char * 260
MODULEENTRY32 = UnicodeAlias('MODULEENTRY32W')
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
PROCESSENTRY32 = UnicodeAlias('PROCESSENTRY32W')
class THREADENTRY32(Structure):
    dwSize: UInt32
    cntUsage: UInt32
    th32ThreadID: UInt32
    th32OwnerProcessID: UInt32
    tpBasePri: Int32
    tpDeltaPri: Int32
    dwFlags: UInt32


make_ready(__name__)
