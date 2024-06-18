from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.IO
@winfunctype('KERNEL32.dll')
def CreateIoCompletionPort(FileHandle: win32more.Windows.Win32.Foundation.HANDLE, ExistingCompletionPort: win32more.Windows.Win32.Foundation.HANDLE, CompletionKey: UIntPtr, NumberOfConcurrentThreads: UInt32) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def GetQueuedCompletionStatus(CompletionPort: win32more.Windows.Win32.Foundation.HANDLE, lpNumberOfBytesTransferred: POINTER(UInt32), lpCompletionKey: POINTER(UIntPtr), lpOverlapped: POINTER(POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)), dwMilliseconds: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetQueuedCompletionStatusEx(CompletionPort: win32more.Windows.Win32.Foundation.HANDLE, lpCompletionPortEntries: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED_ENTRY), ulCount: UInt32, ulNumEntriesRemoved: POINTER(UInt32), dwMilliseconds: UInt32, fAlertable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def PostQueuedCompletionStatus(CompletionPort: win32more.Windows.Win32.Foundation.HANDLE, dwNumberOfBytesTransferred: UInt32, dwCompletionKey: UIntPtr, lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DeviceIoControl(hDevice: win32more.Windows.Win32.Foundation.HANDLE, dwIoControlCode: UInt32, lpInBuffer: VoidPtr, nInBufferSize: UInt32, lpOutBuffer: VoidPtr, nOutBufferSize: UInt32, lpBytesReturned: POINTER(UInt32), lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetOverlappedResult(hFile: win32more.Windows.Win32.Foundation.HANDLE, lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED), lpNumberOfBytesTransferred: POINTER(UInt32), bWait: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CancelIoEx(hFile: win32more.Windows.Win32.Foundation.HANDLE, lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CancelIo(hFile: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetOverlappedResultEx(hFile: win32more.Windows.Win32.Foundation.HANDLE, lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED), lpNumberOfBytesTransferred: POINTER(UInt32), dwMilliseconds: UInt32, bAlertable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CancelSynchronousIo(hThread: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def BindIoCompletionCallback(FileHandle: win32more.Windows.Win32.Foundation.HANDLE, Function: win32more.Windows.Win32.System.IO.LPOVERLAPPED_COMPLETION_ROUTINE, Flags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
class IO_STATUS_BLOCK(Structure):
    Anonymous: _Anonymous_e__Union
    Information: UIntPtr
    class _Anonymous_e__Union(Union):
        Status: win32more.Windows.Win32.Foundation.NTSTATUS
        Pointer: VoidPtr
@winfunctype_pointer
def LPOVERLAPPED_COMPLETION_ROUTINE(dwErrorCode: UInt32, dwNumberOfBytesTransfered: UInt32, lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> Void: ...
class OVERLAPPED(Structure):
    Internal: UIntPtr
    InternalHigh: UIntPtr
    Anonymous: _Anonymous_e__Union
    hEvent: win32more.Windows.Win32.Foundation.HANDLE
    class _Anonymous_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        Pointer: VoidPtr
        class _Anonymous_e__Struct(Structure):
            Offset: UInt32
            OffsetHigh: UInt32
class OVERLAPPED_ENTRY(Structure):
    lpCompletionKey: UIntPtr
    lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)
    Internal: UIntPtr
    dwNumberOfBytesTransferred: UInt32
@winfunctype_pointer
def PIO_APC_ROUTINE(ApcContext: VoidPtr, IoStatusBlock: POINTER(win32more.Windows.Win32.System.IO.IO_STATUS_BLOCK), Reserved: UInt32) -> Void: ...


make_ready(__name__)
