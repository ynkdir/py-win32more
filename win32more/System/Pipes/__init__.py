from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Security
import win32more.Storage.FileSystem
import win32more.System.IO
import win32more.System.Pipes
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
PIPE_UNLIMITED_INSTANCES: UInt32 = 255
NMPWAIT_WAIT_FOREVER: UInt32 = 4294967295
NMPWAIT_NOWAIT: UInt32 = 1
NMPWAIT_USE_DEFAULT_WAIT: UInt32 = 0
@winfunctype('KERNEL32.dll')
def CreatePipe(hReadPipe: POINTER(win32more.Foundation.HANDLE), hWritePipe: POINTER(win32more.Foundation.HANDLE), lpPipeAttributes: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), nSize: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ConnectNamedPipe(hNamedPipe: win32more.Foundation.HANDLE, lpOverlapped: POINTER(win32more.System.IO.OVERLAPPED_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DisconnectNamedPipe(hNamedPipe: win32more.Foundation.HANDLE) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetNamedPipeHandleState(hNamedPipe: win32more.Foundation.HANDLE, lpMode: POINTER(win32more.System.Pipes.NAMED_PIPE_MODE), lpMaxCollectionCount: POINTER(UInt32), lpCollectDataTimeout: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def PeekNamedPipe(hNamedPipe: win32more.Foundation.HANDLE, lpBuffer: c_void_p, nBufferSize: UInt32, lpBytesRead: POINTER(UInt32), lpTotalBytesAvail: POINTER(UInt32), lpBytesLeftThisMessage: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def TransactNamedPipe(hNamedPipe: win32more.Foundation.HANDLE, lpInBuffer: c_void_p, nInBufferSize: UInt32, lpOutBuffer: c_void_p, nOutBufferSize: UInt32, lpBytesRead: POINTER(UInt32), lpOverlapped: POINTER(win32more.System.IO.OVERLAPPED_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateNamedPipeW(lpName: win32more.Foundation.PWSTR, dwOpenMode: win32more.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES, dwPipeMode: win32more.System.Pipes.NAMED_PIPE_MODE, nMaxInstances: UInt32, nOutBufferSize: UInt32, nInBufferSize: UInt32, nDefaultTimeOut: UInt32, lpSecurityAttributes: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head)) -> win32more.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def WaitNamedPipeW(lpNamedPipeName: win32more.Foundation.PWSTR, nTimeOut: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetNamedPipeClientComputerNameW(Pipe: win32more.Foundation.HANDLE, ClientComputerName: win32more.Foundation.PWSTR, ClientComputerNameLength: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ImpersonateNamedPipeClient(hNamedPipe: win32more.Foundation.HANDLE) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetNamedPipeInfo(hNamedPipe: win32more.Foundation.HANDLE, lpFlags: POINTER(win32more.System.Pipes.NAMED_PIPE_MODE), lpOutBufferSize: POINTER(UInt32), lpInBufferSize: POINTER(UInt32), lpMaxInstances: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetNamedPipeHandleStateW(hNamedPipe: win32more.Foundation.HANDLE, lpState: POINTER(win32more.System.Pipes.NAMED_PIPE_MODE), lpCurInstances: POINTER(UInt32), lpMaxCollectionCount: POINTER(UInt32), lpCollectDataTimeout: POINTER(UInt32), lpUserName: win32more.Foundation.PWSTR, nMaxUserNameSize: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CallNamedPipeW(lpNamedPipeName: win32more.Foundation.PWSTR, lpInBuffer: c_void_p, nInBufferSize: UInt32, lpOutBuffer: c_void_p, nOutBufferSize: UInt32, lpBytesRead: POINTER(UInt32), nTimeOut: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateNamedPipeA(lpName: win32more.Foundation.PSTR, dwOpenMode: win32more.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES, dwPipeMode: win32more.System.Pipes.NAMED_PIPE_MODE, nMaxInstances: UInt32, nOutBufferSize: UInt32, nInBufferSize: UInt32, nDefaultTimeOut: UInt32, lpSecurityAttributes: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head)) -> win32more.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def GetNamedPipeHandleStateA(hNamedPipe: win32more.Foundation.HANDLE, lpState: POINTER(win32more.System.Pipes.NAMED_PIPE_MODE), lpCurInstances: POINTER(UInt32), lpMaxCollectionCount: POINTER(UInt32), lpCollectDataTimeout: POINTER(UInt32), lpUserName: win32more.Foundation.PSTR, nMaxUserNameSize: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CallNamedPipeA(lpNamedPipeName: win32more.Foundation.PSTR, lpInBuffer: c_void_p, nInBufferSize: UInt32, lpOutBuffer: c_void_p, nOutBufferSize: UInt32, lpBytesRead: POINTER(UInt32), nTimeOut: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WaitNamedPipeA(lpNamedPipeName: win32more.Foundation.PSTR, nTimeOut: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetNamedPipeClientComputerNameA(Pipe: win32more.Foundation.HANDLE, ClientComputerName: win32more.Foundation.PSTR, ClientComputerNameLength: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetNamedPipeClientProcessId(Pipe: win32more.Foundation.HANDLE, ClientProcessId: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetNamedPipeClientSessionId(Pipe: win32more.Foundation.HANDLE, ClientSessionId: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetNamedPipeServerProcessId(Pipe: win32more.Foundation.HANDLE, ServerProcessId: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetNamedPipeServerSessionId(Pipe: win32more.Foundation.HANDLE, ServerSessionId: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
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
__all__ = [
    "CallNamedPipeA",
    "CallNamedPipeW",
    "ConnectNamedPipe",
    "CreateNamedPipeA",
    "CreateNamedPipeW",
    "CreatePipe",
    "DisconnectNamedPipe",
    "GetNamedPipeClientComputerNameA",
    "GetNamedPipeClientComputerNameW",
    "GetNamedPipeClientProcessId",
    "GetNamedPipeClientSessionId",
    "GetNamedPipeHandleStateA",
    "GetNamedPipeHandleStateW",
    "GetNamedPipeInfo",
    "GetNamedPipeServerProcessId",
    "GetNamedPipeServerSessionId",
    "ImpersonateNamedPipeClient",
    "NAMED_PIPE_MODE",
    "NMPWAIT_NOWAIT",
    "NMPWAIT_USE_DEFAULT_WAIT",
    "NMPWAIT_WAIT_FOREVER",
    "PIPE_ACCEPT_REMOTE_CLIENTS",
    "PIPE_CLIENT_END",
    "PIPE_NOWAIT",
    "PIPE_READMODE_BYTE",
    "PIPE_READMODE_MESSAGE",
    "PIPE_REJECT_REMOTE_CLIENTS",
    "PIPE_SERVER_END",
    "PIPE_TYPE_BYTE",
    "PIPE_TYPE_MESSAGE",
    "PIPE_UNLIMITED_INSTANCES",
    "PIPE_WAIT",
    "PeekNamedPipe",
    "SetNamedPipeHandleState",
    "TransactNamedPipe",
    "WaitNamedPipeA",
    "WaitNamedPipeW",
]
_arch_optional = [
]
