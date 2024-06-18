from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Security
import win32more.Windows.Win32.Storage.FileSystem
import win32more.Windows.Win32.System.IO
import win32more.Windows.Win32.System.Pipes
PIPE_UNLIMITED_INSTANCES: UInt32 = 255
NMPWAIT_WAIT_FOREVER: UInt32 = 4294967295
NMPWAIT_NOWAIT: UInt32 = 1
NMPWAIT_USE_DEFAULT_WAIT: UInt32 = 0
@winfunctype('KERNEL32.dll')
def CreatePipe(hReadPipe: POINTER(win32more.Windows.Win32.Foundation.HANDLE), hWritePipe: POINTER(win32more.Windows.Win32.Foundation.HANDLE), lpPipeAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), nSize: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ConnectNamedPipe(hNamedPipe: win32more.Windows.Win32.Foundation.HANDLE, lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DisconnectNamedPipe(hNamedPipe: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetNamedPipeHandleState(hNamedPipe: win32more.Windows.Win32.Foundation.HANDLE, lpMode: POINTER(win32more.Windows.Win32.System.Pipes.NAMED_PIPE_MODE), lpMaxCollectionCount: POINTER(UInt32), lpCollectDataTimeout: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def PeekNamedPipe(hNamedPipe: win32more.Windows.Win32.Foundation.HANDLE, lpBuffer: VoidPtr, nBufferSize: UInt32, lpBytesRead: POINTER(UInt32), lpTotalBytesAvail: POINTER(UInt32), lpBytesLeftThisMessage: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def TransactNamedPipe(hNamedPipe: win32more.Windows.Win32.Foundation.HANDLE, lpInBuffer: VoidPtr, nInBufferSize: UInt32, lpOutBuffer: VoidPtr, nOutBufferSize: UInt32, lpBytesRead: POINTER(UInt32), lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateNamedPipeW(lpName: win32more.Windows.Win32.Foundation.PWSTR, dwOpenMode: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES, dwPipeMode: win32more.Windows.Win32.System.Pipes.NAMED_PIPE_MODE, nMaxInstances: UInt32, nOutBufferSize: UInt32, nInBufferSize: UInt32, nDefaultTimeOut: UInt32, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES)) -> win32more.Windows.Win32.Foundation.HANDLE: ...
CreateNamedPipe = UnicodeAlias('CreateNamedPipeW')
@winfunctype('KERNEL32.dll')
def WaitNamedPipeW(lpNamedPipeName: win32more.Windows.Win32.Foundation.PWSTR, nTimeOut: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
WaitNamedPipe = UnicodeAlias('WaitNamedPipeW')
@winfunctype('KERNEL32.dll')
def GetNamedPipeClientComputerNameW(Pipe: win32more.Windows.Win32.Foundation.HANDLE, ClientComputerName: win32more.Windows.Win32.Foundation.PWSTR, ClientComputerNameLength: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
GetNamedPipeClientComputerName = UnicodeAlias('GetNamedPipeClientComputerNameW')
@winfunctype('ADVAPI32.dll')
def ImpersonateNamedPipeClient(hNamedPipe: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetNamedPipeInfo(hNamedPipe: win32more.Windows.Win32.Foundation.HANDLE, lpFlags: POINTER(win32more.Windows.Win32.System.Pipes.NAMED_PIPE_MODE), lpOutBufferSize: POINTER(UInt32), lpInBufferSize: POINTER(UInt32), lpMaxInstances: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetNamedPipeHandleStateW(hNamedPipe: win32more.Windows.Win32.Foundation.HANDLE, lpState: POINTER(win32more.Windows.Win32.System.Pipes.NAMED_PIPE_MODE), lpCurInstances: POINTER(UInt32), lpMaxCollectionCount: POINTER(UInt32), lpCollectDataTimeout: POINTER(UInt32), lpUserName: win32more.Windows.Win32.Foundation.PWSTR, nMaxUserNameSize: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
GetNamedPipeHandleState = UnicodeAlias('GetNamedPipeHandleStateW')
@winfunctype('KERNEL32.dll')
def CallNamedPipeW(lpNamedPipeName: win32more.Windows.Win32.Foundation.PWSTR, lpInBuffer: VoidPtr, nInBufferSize: UInt32, lpOutBuffer: VoidPtr, nOutBufferSize: UInt32, lpBytesRead: POINTER(UInt32), nTimeOut: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
CallNamedPipe = UnicodeAlias('CallNamedPipeW')
@winfunctype('KERNEL32.dll')
def CreateNamedPipeA(lpName: win32more.Windows.Win32.Foundation.PSTR, dwOpenMode: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES, dwPipeMode: win32more.Windows.Win32.System.Pipes.NAMED_PIPE_MODE, nMaxInstances: UInt32, nOutBufferSize: UInt32, nInBufferSize: UInt32, nDefaultTimeOut: UInt32, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES)) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def GetNamedPipeHandleStateA(hNamedPipe: win32more.Windows.Win32.Foundation.HANDLE, lpState: POINTER(win32more.Windows.Win32.System.Pipes.NAMED_PIPE_MODE), lpCurInstances: POINTER(UInt32), lpMaxCollectionCount: POINTER(UInt32), lpCollectDataTimeout: POINTER(UInt32), lpUserName: win32more.Windows.Win32.Foundation.PSTR, nMaxUserNameSize: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CallNamedPipeA(lpNamedPipeName: win32more.Windows.Win32.Foundation.PSTR, lpInBuffer: VoidPtr, nInBufferSize: UInt32, lpOutBuffer: VoidPtr, nOutBufferSize: UInt32, lpBytesRead: POINTER(UInt32), nTimeOut: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WaitNamedPipeA(lpNamedPipeName: win32more.Windows.Win32.Foundation.PSTR, nTimeOut: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetNamedPipeClientComputerNameA(Pipe: win32more.Windows.Win32.Foundation.HANDLE, ClientComputerName: win32more.Windows.Win32.Foundation.PSTR, ClientComputerNameLength: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetNamedPipeClientProcessId(Pipe: win32more.Windows.Win32.Foundation.HANDLE, ClientProcessId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetNamedPipeClientSessionId(Pipe: win32more.Windows.Win32.Foundation.HANDLE, ClientSessionId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetNamedPipeServerProcessId(Pipe: win32more.Windows.Win32.Foundation.HANDLE, ServerProcessId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetNamedPipeServerSessionId(Pipe: win32more.Windows.Win32.Foundation.HANDLE, ServerSessionId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
NAMED_PIPE_MODE = UInt32
PIPE_WAIT: win32more.Windows.Win32.System.Pipes.NAMED_PIPE_MODE = 0
PIPE_NOWAIT: win32more.Windows.Win32.System.Pipes.NAMED_PIPE_MODE = 1
PIPE_READMODE_BYTE: win32more.Windows.Win32.System.Pipes.NAMED_PIPE_MODE = 0
PIPE_READMODE_MESSAGE: win32more.Windows.Win32.System.Pipes.NAMED_PIPE_MODE = 2
PIPE_CLIENT_END: win32more.Windows.Win32.System.Pipes.NAMED_PIPE_MODE = 0
PIPE_SERVER_END: win32more.Windows.Win32.System.Pipes.NAMED_PIPE_MODE = 1
PIPE_TYPE_BYTE: win32more.Windows.Win32.System.Pipes.NAMED_PIPE_MODE = 0
PIPE_TYPE_MESSAGE: win32more.Windows.Win32.System.Pipes.NAMED_PIPE_MODE = 4
PIPE_ACCEPT_REMOTE_CLIENTS: win32more.Windows.Win32.System.Pipes.NAMED_PIPE_MODE = 0
PIPE_REJECT_REMOTE_CLIENTS: win32more.Windows.Win32.System.Pipes.NAMED_PIPE_MODE = 8


make_ready(__name__)
