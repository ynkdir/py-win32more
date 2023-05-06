from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.System.IO
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
@winfunctype('KERNEL32.dll')
def CreateIoCompletionPort(FileHandle: Windows.Win32.Foundation.HANDLE, ExistingCompletionPort: Windows.Win32.Foundation.HANDLE, CompletionKey: UIntPtr, NumberOfConcurrentThreads: UInt32) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def GetQueuedCompletionStatus(CompletionPort: Windows.Win32.Foundation.HANDLE, lpNumberOfBytesTransferred: POINTER(UInt32), lpCompletionKey: POINTER(UIntPtr), lpOverlapped: POINTER(POINTER(Windows.Win32.System.IO.OVERLAPPED_head)), dwMilliseconds: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetQueuedCompletionStatusEx(CompletionPort: Windows.Win32.Foundation.HANDLE, lpCompletionPortEntries: POINTER(Windows.Win32.System.IO.OVERLAPPED_ENTRY_head), ulCount: UInt32, ulNumEntriesRemoved: POINTER(UInt32), dwMilliseconds: UInt32, fAlertable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def PostQueuedCompletionStatus(CompletionPort: Windows.Win32.Foundation.HANDLE, dwNumberOfBytesTransferred: UInt32, dwCompletionKey: UIntPtr, lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DeviceIoControl(hDevice: Windows.Win32.Foundation.HANDLE, dwIoControlCode: UInt32, lpInBuffer: c_void_p, nInBufferSize: UInt32, lpOutBuffer: c_void_p, nOutBufferSize: UInt32, lpBytesReturned: POINTER(UInt32), lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetOverlappedResult(hFile: Windows.Win32.Foundation.HANDLE, lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head), lpNumberOfBytesTransferred: POINTER(UInt32), bWait: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CancelIoEx(hFile: Windows.Win32.Foundation.HANDLE, lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CancelIo(hFile: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetOverlappedResultEx(hFile: Windows.Win32.Foundation.HANDLE, lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head), lpNumberOfBytesTransferred: POINTER(UInt32), dwMilliseconds: UInt32, bAlertable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CancelSynchronousIo(hThread: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def BindIoCompletionCallback(FileHandle: Windows.Win32.Foundation.HANDLE, Function: Windows.Win32.System.IO.LPOVERLAPPED_COMPLETION_ROUTINE, Flags: UInt32) -> Windows.Win32.Foundation.BOOL: ...
class IO_STATUS_BLOCK(EasyCastStructure):
    Anonymous: _Anonymous_e__Union
    Information: UIntPtr
    class _Anonymous_e__Union(EasyCastUnion):
        Status: Windows.Win32.Foundation.NTSTATUS
        Pointer: c_void_p
@winfunctype_pointer
def LPOVERLAPPED_COMPLETION_ROUTINE(dwErrorCode: UInt32, dwNumberOfBytesTransfered: UInt32, lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Void: ...
class OVERLAPPED(EasyCastStructure):
    Internal: UIntPtr
    InternalHigh: UIntPtr
    Anonymous: _Anonymous_e__Union
    hEvent: Windows.Win32.Foundation.HANDLE
    class _Anonymous_e__Union(EasyCastUnion):
        Anonymous: _Anonymous_e__Struct
        Pointer: c_void_p
        class _Anonymous_e__Struct(EasyCastStructure):
            Offset: UInt32
            OffsetHigh: UInt32
class OVERLAPPED_ENTRY(EasyCastStructure):
    lpCompletionKey: UIntPtr
    lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)
    Internal: UIntPtr
    dwNumberOfBytesTransferred: UInt32
@winfunctype_pointer
def PIO_APC_ROUTINE(ApcContext: c_void_p, IoStatusBlock: POINTER(Windows.Win32.System.IO.IO_STATUS_BLOCK_head), Reserved: UInt32) -> Void: ...
make_head(_module, 'IO_STATUS_BLOCK')
make_head(_module, 'LPOVERLAPPED_COMPLETION_ROUTINE')
make_head(_module, 'OVERLAPPED')
make_head(_module, 'OVERLAPPED_ENTRY')
make_head(_module, 'PIO_APC_ROUTINE')
