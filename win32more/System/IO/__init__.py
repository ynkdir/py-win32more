from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.IO
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f'_define_{name}']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
def _define_CreateIoCompletionPort():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,UIntPtr,UInt32)(('CreateIoCompletionPort', windll['KERNEL32.dll']), ((1, 'FileHandle'),(1, 'ExistingCompletionPort'),(1, 'CompletionKey'),(1, 'NumberOfConcurrentThreads'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetQueuedCompletionStatus():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(UInt32),POINTER(UIntPtr),POINTER(POINTER(win32more.System.IO.OVERLAPPED_head)),UInt32)(('GetQueuedCompletionStatus', windll['KERNEL32.dll']), ((1, 'CompletionPort'),(1, 'lpNumberOfBytesTransferred'),(1, 'lpCompletionKey'),(1, 'lpOverlapped'),(1, 'dwMilliseconds'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetQueuedCompletionStatusEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.IO.OVERLAPPED_ENTRY_head),UInt32,POINTER(UInt32),UInt32,win32more.Foundation.BOOL)(('GetQueuedCompletionStatusEx', windll['KERNEL32.dll']), ((1, 'CompletionPort'),(1, 'lpCompletionPortEntries'),(1, 'ulCount'),(1, 'ulNumEntriesRemoved'),(1, 'dwMilliseconds'),(1, 'fAlertable'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PostQueuedCompletionStatus():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,UIntPtr,POINTER(win32more.System.IO.OVERLAPPED_head))(('PostQueuedCompletionStatus', windll['KERNEL32.dll']), ((1, 'CompletionPort'),(1, 'dwNumberOfBytesTransferred'),(1, 'dwCompletionKey'),(1, 'lpOverlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeviceIoControl():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,c_void_p,UInt32,c_void_p,UInt32,POINTER(UInt32),POINTER(win32more.System.IO.OVERLAPPED_head))(('DeviceIoControl', windll['KERNEL32.dll']), ((1, 'hDevice'),(1, 'dwIoControlCode'),(1, 'lpInBuffer'),(1, 'nInBufferSize'),(1, 'lpOutBuffer'),(1, 'nOutBufferSize'),(1, 'lpBytesReturned'),(1, 'lpOverlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetOverlappedResult():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.IO.OVERLAPPED_head),POINTER(UInt32),win32more.Foundation.BOOL)(('GetOverlappedResult', windll['KERNEL32.dll']), ((1, 'hFile'),(1, 'lpOverlapped'),(1, 'lpNumberOfBytesTransferred'),(1, 'bWait'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CancelIoEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.IO.OVERLAPPED_head))(('CancelIoEx', windll['KERNEL32.dll']), ((1, 'hFile'),(1, 'lpOverlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CancelIo():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE)(('CancelIo', windll['KERNEL32.dll']), ((1, 'hFile'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetOverlappedResultEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.IO.OVERLAPPED_head),POINTER(UInt32),UInt32,win32more.Foundation.BOOL)(('GetOverlappedResultEx', windll['KERNEL32.dll']), ((1, 'hFile'),(1, 'lpOverlapped'),(1, 'lpNumberOfBytesTransferred'),(1, 'dwMilliseconds'),(1, 'bAlertable'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CancelSynchronousIo():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE)(('CancelSynchronousIo', windll['KERNEL32.dll']), ((1, 'hThread'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BindIoCompletionCallback():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.System.IO.LPOVERLAPPED_COMPLETION_ROUTINE,UInt32)(('BindIoCompletionCallback', windll['KERNEL32.dll']), ((1, 'FileHandle'),(1, 'Function'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LPOVERLAPPED_COMPLETION_ROUTINE():
    return WINFUNCTYPE(Void,UInt32,UInt32,POINTER(win32more.System.IO.OVERLAPPED_head))
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
        ('Offset', UInt32),
        ('OffsetHigh', UInt32),
    ]
    OVERLAPPED__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    OVERLAPPED__Anonymous_e__Union._fields_ = [
        ('Anonymous', OVERLAPPED__Anonymous_e__Union__Anonymous_e__Struct),
        ('Pointer', c_void_p),
    ]
    OVERLAPPED._anonymous_ = [
        'Anonymous',
    ]
    OVERLAPPED._fields_ = [
        ('Internal', UIntPtr),
        ('InternalHigh', UIntPtr),
        ('Anonymous', OVERLAPPED__Anonymous_e__Union),
        ('hEvent', win32more.Foundation.HANDLE),
    ]
    return OVERLAPPED
def _define_OVERLAPPED_ENTRY_head():
    class OVERLAPPED_ENTRY(Structure):
        pass
    return OVERLAPPED_ENTRY
def _define_OVERLAPPED_ENTRY():
    OVERLAPPED_ENTRY = win32more.System.IO.OVERLAPPED_ENTRY_head
    OVERLAPPED_ENTRY._fields_ = [
        ('lpCompletionKey', UIntPtr),
        ('lpOverlapped', POINTER(win32more.System.IO.OVERLAPPED_head)),
        ('Internal', UIntPtr),
        ('dwNumberOfBytesTransferred', UInt32),
    ]
    return OVERLAPPED_ENTRY
__all__ = [
    "BindIoCompletionCallback",
    "CancelIo",
    "CancelIoEx",
    "CancelSynchronousIo",
    "CreateIoCompletionPort",
    "DeviceIoControl",
    "GetOverlappedResult",
    "GetOverlappedResultEx",
    "GetQueuedCompletionStatus",
    "GetQueuedCompletionStatusEx",
    "LPOVERLAPPED_COMPLETION_ROUTINE",
    "OVERLAPPED",
    "OVERLAPPED_ENTRY",
    "PostQueuedCompletionStatus",
]
