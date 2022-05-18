from win32more import *
import win32more.Foundation
import win32more.System.IO

def __getattr__(name):
    module = globals()
    try:
        f = module[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    module[name] = f()
    return module[name]
def __dir__():
    return __all__
def _define_OVERLAPPED_head():
    class OVERLAPPED(Structure):
        pass
    return OVERLAPPED
def _define_OVERLAPPED():
    OVERLAPPED = win32more.System.IO.OVERLAPPED_head
    class OVERLAPPED__Anonymous_e__Union(Union):
        pass
    class OVERLAPPED__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    OVERLAPPED__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ("Offset", UInt32),
        ("OffsetHigh", UInt32),
    ]
    OVERLAPPED__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    OVERLAPPED__Anonymous_e__Union._fields_ = [
        ("Anonymous", OVERLAPPED__Anonymous_e__Union__Anonymous_e__Struct),
        ("Pointer", c_void_p),
    ]
    OVERLAPPED._anonymous_ = [
        'Anonymous',
    ]
    OVERLAPPED._fields_ = [
        ("Internal", UIntPtr),
        ("InternalHigh", UIntPtr),
        ("Anonymous", OVERLAPPED__Anonymous_e__Union),
        ("hEvent", win32more.Foundation.HANDLE),
    ]
    return OVERLAPPED
def _define_OVERLAPPED_ENTRY_head():
    class OVERLAPPED_ENTRY(Structure):
        pass
    return OVERLAPPED_ENTRY
def _define_OVERLAPPED_ENTRY():
    OVERLAPPED_ENTRY = win32more.System.IO.OVERLAPPED_ENTRY_head
    OVERLAPPED_ENTRY._fields_ = [
        ("lpCompletionKey", UIntPtr),
        ("lpOverlapped", POINTER(win32more.System.IO.OVERLAPPED_head)),
        ("Internal", UIntPtr),
        ("dwNumberOfBytesTransferred", UInt32),
    ]
    return OVERLAPPED_ENTRY
def _define_LPOVERLAPPED_COMPLETION_ROUTINE():
    return CFUNCTYPE(Void,UInt32,UInt32,POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)
def _define_CreateIoCompletionPort():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,UIntPtr,UInt32, use_last_error=True)(("CreateIoCompletionPort", windll["KERNEL32"]), ((1, 'FileHandle'),(1, 'ExistingCompletionPort'),(1, 'CompletionKey'),(1, 'NumberOfConcurrentThreads'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetQueuedCompletionStatus():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(UInt32),POINTER(UIntPtr),POINTER(POINTER(win32more.System.IO.OVERLAPPED_head)),UInt32, use_last_error=True)(("GetQueuedCompletionStatus", windll["KERNEL32"]), ((1, 'CompletionPort'),(1, 'lpNumberOfBytesTransferred'),(1, 'lpCompletionKey'),(1, 'lpOverlapped'),(1, 'dwMilliseconds'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetQueuedCompletionStatusEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.IO.OVERLAPPED_ENTRY),UInt32,POINTER(UInt32),UInt32,win32more.Foundation.BOOL, use_last_error=True)(("GetQueuedCompletionStatusEx", windll["KERNEL32"]), ((1, 'CompletionPort'),(1, 'lpCompletionPortEntries'),(1, 'ulCount'),(1, 'ulNumEntriesRemoved'),(1, 'dwMilliseconds'),(1, 'fAlertable'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PostQueuedCompletionStatus():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,UIntPtr,POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=True)(("PostQueuedCompletionStatus", windll["KERNEL32"]), ((1, 'CompletionPort'),(1, 'dwNumberOfBytesTransferred'),(1, 'dwCompletionKey'),(1, 'lpOverlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeviceIoControl():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,c_void_p,UInt32,c_void_p,UInt32,POINTER(UInt32),POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=True)(("DeviceIoControl", windll["KERNEL32"]), ((1, 'hDevice'),(1, 'dwIoControlCode'),(1, 'lpInBuffer'),(1, 'nInBufferSize'),(1, 'lpOutBuffer'),(1, 'nOutBufferSize'),(1, 'lpBytesReturned'),(1, 'lpOverlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetOverlappedResult():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.IO.OVERLAPPED_head),POINTER(UInt32),win32more.Foundation.BOOL, use_last_error=True)(("GetOverlappedResult", windll["KERNEL32"]), ((1, 'hFile'),(1, 'lpOverlapped'),(1, 'lpNumberOfBytesTransferred'),(1, 'bWait'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CancelIoEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=True)(("CancelIoEx", windll["KERNEL32"]), ((1, 'hFile'),(1, 'lpOverlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CancelIo():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE, use_last_error=True)(("CancelIo", windll["KERNEL32"]), ((1, 'hFile'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetOverlappedResultEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.IO.OVERLAPPED_head),POINTER(UInt32),UInt32,win32more.Foundation.BOOL, use_last_error=True)(("GetOverlappedResultEx", windll["KERNEL32"]), ((1, 'hFile'),(1, 'lpOverlapped'),(1, 'lpNumberOfBytesTransferred'),(1, 'dwMilliseconds'),(1, 'bAlertable'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CancelSynchronousIo():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE, use_last_error=True)(("CancelSynchronousIo", windll["KERNEL32"]), ((1, 'hThread'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BindIoCompletionCallback():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.System.IO.LPOVERLAPPED_COMPLETION_ROUTINE,UInt32, use_last_error=True)(("BindIoCompletionCallback", windll["KERNEL32"]), ((1, 'FileHandle'),(1, 'Function'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "OVERLAPPED",
    "OVERLAPPED_ENTRY",
    "LPOVERLAPPED_COMPLETION_ROUTINE",
    "CreateIoCompletionPort",
    "GetQueuedCompletionStatus",
    "GetQueuedCompletionStatusEx",
    "PostQueuedCompletionStatus",
    "DeviceIoControl",
    "GetOverlappedResult",
    "CancelIoEx",
    "CancelIo",
    "GetOverlappedResultEx",
    "CancelSynchronousIo",
    "BindIoCompletionCallback",
]
