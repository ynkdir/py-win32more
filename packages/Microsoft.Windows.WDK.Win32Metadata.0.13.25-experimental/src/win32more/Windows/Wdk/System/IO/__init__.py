from __future__ import annotations
from win32more._prelude import *
import win32more.Windows.Wdk.System.IO
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.IO
@winfunctype('ntdll.dll')
def NtDeviceIoControlFile(FileHandle: win32more.Windows.Win32.Foundation.HANDLE, Event: win32more.Windows.Win32.Foundation.HANDLE, ApcRoutine: win32more.Windows.Win32.System.IO.PIO_APC_ROUTINE, ApcContext: VoidPtr, IoStatusBlock: POINTER(win32more.Windows.Win32.System.IO.IO_STATUS_BLOCK), IoControlCode: UInt32, InputBuffer: VoidPtr, InputBufferLength: UInt32, OutputBuffer: VoidPtr, OutputBufferLength: UInt32) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...


make_ready(__name__)
