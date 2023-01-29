from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.System.IO
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
@winfunctype('KERNEL32.dll')
def CreateIoCompletionPort(FileHandle: win32more.Foundation.HANDLE, ExistingCompletionPort: win32more.Foundation.HANDLE, CompletionKey: UIntPtr, NumberOfConcurrentThreads: UInt32) -> win32more.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def GetQueuedCompletionStatus(CompletionPort: win32more.Foundation.HANDLE, lpNumberOfBytesTransferred: POINTER(UInt32), lpCompletionKey: POINTER(UIntPtr), lpOverlapped: POINTER(POINTER(win32more.System.IO.OVERLAPPED_head)), dwMilliseconds: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetQueuedCompletionStatusEx(CompletionPort: win32more.Foundation.HANDLE, lpCompletionPortEntries: POINTER(win32more.System.IO.OVERLAPPED_ENTRY_head), ulCount: UInt32, ulNumEntriesRemoved: POINTER(UInt32), dwMilliseconds: UInt32, fAlertable: win32more.Foundation.BOOL) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def PostQueuedCompletionStatus(CompletionPort: win32more.Foundation.HANDLE, dwNumberOfBytesTransferred: UInt32, dwCompletionKey: UIntPtr, lpOverlapped: POINTER(win32more.System.IO.OVERLAPPED_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DeviceIoControl(hDevice: win32more.Foundation.HANDLE, dwIoControlCode: UInt32, lpInBuffer: c_void_p, nInBufferSize: UInt32, lpOutBuffer: c_void_p, nOutBufferSize: UInt32, lpBytesReturned: POINTER(UInt32), lpOverlapped: POINTER(win32more.System.IO.OVERLAPPED_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetOverlappedResult(hFile: win32more.Foundation.HANDLE, lpOverlapped: POINTER(win32more.System.IO.OVERLAPPED_head), lpNumberOfBytesTransferred: POINTER(UInt32), bWait: win32more.Foundation.BOOL) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CancelIoEx(hFile: win32more.Foundation.HANDLE, lpOverlapped: POINTER(win32more.System.IO.OVERLAPPED_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CancelIo(hFile: win32more.Foundation.HANDLE) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetOverlappedResultEx(hFile: win32more.Foundation.HANDLE, lpOverlapped: POINTER(win32more.System.IO.OVERLAPPED_head), lpNumberOfBytesTransferred: POINTER(UInt32), dwMilliseconds: UInt32, bAlertable: win32more.Foundation.BOOL) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CancelSynchronousIo(hThread: win32more.Foundation.HANDLE) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def BindIoCompletionCallback(FileHandle: win32more.Foundation.HANDLE, Function: win32more.System.IO.LPOVERLAPPED_COMPLETION_ROUTINE, Flags: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def LPOVERLAPPED_COMPLETION_ROUTINE(dwErrorCode: UInt32, dwNumberOfBytesTransfered: UInt32, lpOverlapped: POINTER(win32more.System.IO.OVERLAPPED_head)) -> Void: ...
class OVERLAPPED(Structure):
    Internal: UIntPtr
    InternalHigh: UIntPtr
    Anonymous: _Anonymous_e__Union
    hEvent: win32more.Foundation.HANDLE
    class _Anonymous_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        Pointer: c_void_p
        class _Anonymous_e__Struct(Structure):
            Offset: UInt32
            OffsetHigh: UInt32
class OVERLAPPED_ENTRY(Structure):
    lpCompletionKey: UIntPtr
    lpOverlapped: POINTER(win32more.System.IO.OVERLAPPED_head)
    Internal: UIntPtr
    dwNumberOfBytesTransferred: UInt32
make_head(_module, 'LPOVERLAPPED_COMPLETION_ROUTINE')
make_head(_module, 'OVERLAPPED')
make_head(_module, 'OVERLAPPED_ENTRY')
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
_arch_optional = [
]
