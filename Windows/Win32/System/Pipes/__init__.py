from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.Foundation
import Windows.Win32.Security
import Windows.Win32.Storage.FileSystem
import Windows.Win32.System.IO
import Windows.Win32.System.Pipes
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
PIPE_UNLIMITED_INSTANCES: UInt32 = 255
NMPWAIT_WAIT_FOREVER: UInt32 = 4294967295
NMPWAIT_NOWAIT: UInt32 = 1
NMPWAIT_USE_DEFAULT_WAIT: UInt32 = 0
@winfunctype('KERNEL32.dll')
def CreatePipe(hReadPipe: POINTER(Windows.Win32.Foundation.HANDLE), hWritePipe: POINTER(Windows.Win32.Foundation.HANDLE), lpPipeAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head), nSize: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ConnectNamedPipe(hNamedPipe: Windows.Win32.Foundation.HANDLE, lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DisconnectNamedPipe(hNamedPipe: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetNamedPipeHandleState(hNamedPipe: Windows.Win32.Foundation.HANDLE, lpMode: POINTER(Windows.Win32.System.Pipes.NAMED_PIPE_MODE), lpMaxCollectionCount: POINTER(UInt32), lpCollectDataTimeout: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def PeekNamedPipe(hNamedPipe: Windows.Win32.Foundation.HANDLE, lpBuffer: c_void_p, nBufferSize: UInt32, lpBytesRead: POINTER(UInt32), lpTotalBytesAvail: POINTER(UInt32), lpBytesLeftThisMessage: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def TransactNamedPipe(hNamedPipe: Windows.Win32.Foundation.HANDLE, lpInBuffer: c_void_p, nInBufferSize: UInt32, lpOutBuffer: c_void_p, nOutBufferSize: UInt32, lpBytesRead: POINTER(UInt32), lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateNamedPipeW(lpName: Windows.Win32.Foundation.PWSTR, dwOpenMode: Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES, dwPipeMode: Windows.Win32.System.Pipes.NAMED_PIPE_MODE, nMaxInstances: UInt32, nOutBufferSize: UInt32, nInBufferSize: UInt32, nDefaultTimeOut: UInt32, lpSecurityAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head)) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def WaitNamedPipeW(lpNamedPipeName: Windows.Win32.Foundation.PWSTR, nTimeOut: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetNamedPipeClientComputerNameW(Pipe: Windows.Win32.Foundation.HANDLE, ClientComputerName: Windows.Win32.Foundation.PWSTR, ClientComputerNameLength: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ImpersonateNamedPipeClient(hNamedPipe: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetNamedPipeInfo(hNamedPipe: Windows.Win32.Foundation.HANDLE, lpFlags: POINTER(Windows.Win32.System.Pipes.NAMED_PIPE_MODE), lpOutBufferSize: POINTER(UInt32), lpInBufferSize: POINTER(UInt32), lpMaxInstances: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetNamedPipeHandleStateW(hNamedPipe: Windows.Win32.Foundation.HANDLE, lpState: POINTER(Windows.Win32.System.Pipes.NAMED_PIPE_MODE), lpCurInstances: POINTER(UInt32), lpMaxCollectionCount: POINTER(UInt32), lpCollectDataTimeout: POINTER(UInt32), lpUserName: Windows.Win32.Foundation.PWSTR, nMaxUserNameSize: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CallNamedPipeW(lpNamedPipeName: Windows.Win32.Foundation.PWSTR, lpInBuffer: c_void_p, nInBufferSize: UInt32, lpOutBuffer: c_void_p, nOutBufferSize: UInt32, lpBytesRead: POINTER(UInt32), nTimeOut: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateNamedPipeA(lpName: Windows.Win32.Foundation.PSTR, dwOpenMode: Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES, dwPipeMode: Windows.Win32.System.Pipes.NAMED_PIPE_MODE, nMaxInstances: UInt32, nOutBufferSize: UInt32, nInBufferSize: UInt32, nDefaultTimeOut: UInt32, lpSecurityAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head)) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def GetNamedPipeHandleStateA(hNamedPipe: Windows.Win32.Foundation.HANDLE, lpState: POINTER(Windows.Win32.System.Pipes.NAMED_PIPE_MODE), lpCurInstances: POINTER(UInt32), lpMaxCollectionCount: POINTER(UInt32), lpCollectDataTimeout: POINTER(UInt32), lpUserName: Windows.Win32.Foundation.PSTR, nMaxUserNameSize: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CallNamedPipeA(lpNamedPipeName: Windows.Win32.Foundation.PSTR, lpInBuffer: c_void_p, nInBufferSize: UInt32, lpOutBuffer: c_void_p, nOutBufferSize: UInt32, lpBytesRead: POINTER(UInt32), nTimeOut: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WaitNamedPipeA(lpNamedPipeName: Windows.Win32.Foundation.PSTR, nTimeOut: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetNamedPipeClientComputerNameA(Pipe: Windows.Win32.Foundation.HANDLE, ClientComputerName: Windows.Win32.Foundation.PSTR, ClientComputerNameLength: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetNamedPipeClientProcessId(Pipe: Windows.Win32.Foundation.HANDLE, ClientProcessId: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetNamedPipeClientSessionId(Pipe: Windows.Win32.Foundation.HANDLE, ClientSessionId: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetNamedPipeServerProcessId(Pipe: Windows.Win32.Foundation.HANDLE, ServerProcessId: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetNamedPipeServerSessionId(Pipe: Windows.Win32.Foundation.HANDLE, ServerSessionId: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
NAMED_PIPE_MODE = UInt32
PIPE_WAIT: NAMED_PIPE_MODE = 0
PIPE_NOWAIT: NAMED_PIPE_MODE = 1
PIPE_READMODE_BYTE: NAMED_PIPE_MODE = 0
PIPE_READMODE_MESSAGE: NAMED_PIPE_MODE = 2
PIPE_CLIENT_END: NAMED_PIPE_MODE = 0
PIPE_SERVER_END: NAMED_PIPE_MODE = 1
PIPE_TYPE_BYTE: NAMED_PIPE_MODE = 0
PIPE_TYPE_MESSAGE: NAMED_PIPE_MODE = 4
PIPE_ACCEPT_REMOTE_CLIENTS: NAMED_PIPE_MODE = 0
PIPE_REJECT_REMOTE_CLIENTS: NAMED_PIPE_MODE = 8
