from win32more import *
import win32more.System.Pipes
import win32more.Foundation
import win32more.Security
import win32more.Storage.FileSystem
import win32more.System.IO

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.System.Pipes, name, eval(f"_define_{name}()"))
    return getattr(win32more.System.Pipes, name)
PIPE_UNLIMITED_INSTANCES = 255
NMPWAIT_WAIT_FOREVER = 4294967295
NMPWAIT_NOWAIT = 1
NMPWAIT_USE_DEFAULT_WAIT = 0
NAMED_PIPE_MODE = UInt32
PIPE_WAIT = 0
PIPE_NOWAIT = 1
PIPE_READMODE_BYTE = 0
PIPE_READMODE_MESSAGE = 2
PIPE_CLIENT_END = 0
PIPE_SERVER_END = 1
PIPE_TYPE_BYTE = 0
PIPE_TYPE_MESSAGE = 4
PIPE_ACCEPT_REMOTE_CLIENTS = 0
PIPE_REJECT_REMOTE_CLIENTS = 8
def _define_CreatePipe():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.HANDLE),POINTER(win32more.Foundation.HANDLE),POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),UInt32, use_last_error=True)(("CreatePipe", windll["KERNEL32"]), ((1, 'hReadPipe'),(1, 'hWritePipe'),(1, 'lpPipeAttributes'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ConnectNamedPipe():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=True)(("ConnectNamedPipe", windll["KERNEL32"]), ((1, 'hNamedPipe'),(1, 'lpOverlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DisconnectNamedPipe():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE, use_last_error=True)(("DisconnectNamedPipe", windll["KERNEL32"]), ((1, 'hNamedPipe'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetNamedPipeHandleState():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.Pipes.NAMED_PIPE_MODE),POINTER(UInt32),POINTER(UInt32), use_last_error=True)(("SetNamedPipeHandleState", windll["KERNEL32"]), ((1, 'hNamedPipe'),(1, 'lpMode'),(1, 'lpMaxCollectionCount'),(1, 'lpCollectDataTimeout'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeekNamedPipe():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,c_void_p,UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32), use_last_error=True)(("PeekNamedPipe", windll["KERNEL32"]), ((1, 'hNamedPipe'),(1, 'lpBuffer'),(1, 'nBufferSize'),(1, 'lpBytesRead'),(1, 'lpTotalBytesAvail'),(1, 'lpBytesLeftThisMessage'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TransactNamedPipe():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,c_void_p,UInt32,c_void_p,UInt32,POINTER(UInt32),POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=True)(("TransactNamedPipe", windll["KERNEL32"]), ((1, 'hNamedPipe'),(1, 'lpInBuffer'),(1, 'nInBufferSize'),(1, 'lpOutBuffer'),(1, 'nOutBufferSize'),(1, 'lpBytesRead'),(1, 'lpOverlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateNamedPipeW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,win32more.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES,win32more.System.Pipes.NAMED_PIPE_MODE,UInt32,UInt32,UInt32,UInt32,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), use_last_error=False)(("CreateNamedPipeW", windll["KERNEL32"]), ((1, 'lpName'),(1, 'dwOpenMode'),(1, 'dwPipeMode'),(1, 'nMaxInstances'),(1, 'nOutBufferSize'),(1, 'nInBufferSize'),(1, 'nDefaultTimeOut'),(1, 'lpSecurityAttributes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateNamedPipe():
    return win32more.System.Pipes.CreateNamedPipeW
def _define_WaitNamedPipeW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(("WaitNamedPipeW", windll["KERNEL32"]), ((1, 'lpNamedPipeName'),(1, 'nTimeOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WaitNamedPipe():
    return win32more.System.Pipes.WaitNamedPipeW
def _define_GetNamedPipeClientComputerNameW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(("GetNamedPipeClientComputerNameW", windll["KERNEL32"]), ((1, 'Pipe'),(1, 'ClientComputerName'),(1, 'ClientComputerNameLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetNamedPipeClientComputerName():
    return win32more.System.Pipes.GetNamedPipeClientComputerNameW
def _define_ImpersonateNamedPipeClient():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE, use_last_error=True)(("ImpersonateNamedPipeClient", windll["ADVAPI32"]), ((1, 'hNamedPipe'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetNamedPipeInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.Pipes.NAMED_PIPE_MODE),POINTER(UInt32),POINTER(UInt32),POINTER(UInt32), use_last_error=True)(("GetNamedPipeInfo", windll["KERNEL32"]), ((1, 'hNamedPipe'),(1, 'lpFlags'),(1, 'lpOutBufferSize'),(1, 'lpInBufferSize'),(1, 'lpMaxInstances'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetNamedPipeHandleStateW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.Pipes.NAMED_PIPE_MODE),POINTER(UInt32),POINTER(UInt32),POINTER(UInt32),POINTER(Char),UInt32, use_last_error=False)(("GetNamedPipeHandleStateW", windll["KERNEL32"]), ((1, 'hNamedPipe'),(1, 'lpState'),(1, 'lpCurInstances'),(1, 'lpMaxCollectionCount'),(1, 'lpCollectDataTimeout'),(1, 'lpUserName'),(1, 'nMaxUserNameSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetNamedPipeHandleState():
    return win32more.System.Pipes.GetNamedPipeHandleStateW
def _define_CallNamedPipeW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,c_void_p,UInt32,c_void_p,UInt32,POINTER(UInt32),UInt32, use_last_error=False)(("CallNamedPipeW", windll["KERNEL32"]), ((1, 'lpNamedPipeName'),(1, 'lpInBuffer'),(1, 'nInBufferSize'),(1, 'lpOutBuffer'),(1, 'nOutBufferSize'),(1, 'lpBytesRead'),(1, 'nTimeOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CallNamedPipe():
    return win32more.System.Pipes.CallNamedPipeW
def _define_CreateNamedPipeA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.PSTR,win32more.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES,win32more.System.Pipes.NAMED_PIPE_MODE,UInt32,UInt32,UInt32,UInt32,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), use_last_error=True)(("CreateNamedPipeA", windll["KERNEL32"]), ((1, 'lpName'),(1, 'dwOpenMode'),(1, 'dwPipeMode'),(1, 'nMaxInstances'),(1, 'nOutBufferSize'),(1, 'nInBufferSize'),(1, 'nDefaultTimeOut'),(1, 'lpSecurityAttributes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetNamedPipeHandleStateA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.Pipes.NAMED_PIPE_MODE),POINTER(UInt32),POINTER(UInt32),POINTER(UInt32),POINTER(Byte),UInt32, use_last_error=True)(("GetNamedPipeHandleStateA", windll["KERNEL32"]), ((1, 'hNamedPipe'),(1, 'lpState'),(1, 'lpCurInstances'),(1, 'lpMaxCollectionCount'),(1, 'lpCollectDataTimeout'),(1, 'lpUserName'),(1, 'nMaxUserNameSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CallNamedPipeA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,c_void_p,UInt32,c_void_p,UInt32,POINTER(UInt32),UInt32, use_last_error=True)(("CallNamedPipeA", windll["KERNEL32"]), ((1, 'lpNamedPipeName'),(1, 'lpInBuffer'),(1, 'nInBufferSize'),(1, 'lpOutBuffer'),(1, 'nOutBufferSize'),(1, 'lpBytesRead'),(1, 'nTimeOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WaitNamedPipeA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,UInt32, use_last_error=True)(("WaitNamedPipeA", windll["KERNEL32"]), ((1, 'lpNamedPipeName'),(1, 'nTimeOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetNamedPipeClientComputerNameA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,UInt32, use_last_error=True)(("GetNamedPipeClientComputerNameA", windll["KERNEL32"]), ((1, 'Pipe'),(1, 'ClientComputerName'),(1, 'ClientComputerNameLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetNamedPipeClientProcessId():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(UInt32), use_last_error=True)(("GetNamedPipeClientProcessId", windll["KERNEL32"]), ((1, 'Pipe'),(1, 'ClientProcessId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetNamedPipeClientSessionId():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(UInt32), use_last_error=True)(("GetNamedPipeClientSessionId", windll["KERNEL32"]), ((1, 'Pipe'),(1, 'ClientSessionId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetNamedPipeServerProcessId():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(UInt32), use_last_error=True)(("GetNamedPipeServerProcessId", windll["KERNEL32"]), ((1, 'Pipe'),(1, 'ServerProcessId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetNamedPipeServerSessionId():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(UInt32), use_last_error=True)(("GetNamedPipeServerSessionId", windll["KERNEL32"]), ((1, 'Pipe'),(1, 'ServerSessionId'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "PIPE_UNLIMITED_INSTANCES",
    "NMPWAIT_WAIT_FOREVER",
    "NMPWAIT_NOWAIT",
    "NMPWAIT_USE_DEFAULT_WAIT",
    "NAMED_PIPE_MODE",
    "PIPE_WAIT",
    "PIPE_NOWAIT",
    "PIPE_READMODE_BYTE",
    "PIPE_READMODE_MESSAGE",
    "PIPE_CLIENT_END",
    "PIPE_SERVER_END",
    "PIPE_TYPE_BYTE",
    "PIPE_TYPE_MESSAGE",
    "PIPE_ACCEPT_REMOTE_CLIENTS",
    "PIPE_REJECT_REMOTE_CLIENTS",
    "CreatePipe",
    "ConnectNamedPipe",
    "DisconnectNamedPipe",
    "SetNamedPipeHandleState",
    "PeekNamedPipe",
    "TransactNamedPipe",
    "CreateNamedPipeW",
    "CreateNamedPipe",
    "WaitNamedPipeW",
    "WaitNamedPipe",
    "GetNamedPipeClientComputerNameW",
    "GetNamedPipeClientComputerName",
    "ImpersonateNamedPipeClient",
    "GetNamedPipeInfo",
    "GetNamedPipeHandleStateW",
    "GetNamedPipeHandleState",
    "CallNamedPipeW",
    "CallNamedPipe",
    "CreateNamedPipeA",
    "GetNamedPipeHandleStateA",
    "CallNamedPipeA",
    "WaitNamedPipeA",
    "GetNamedPipeClientComputerNameA",
    "GetNamedPipeClientProcessId",
    "GetNamedPipeClientSessionId",
    "GetNamedPipeServerProcessId",
    "GetNamedPipeServerSessionId",
]
