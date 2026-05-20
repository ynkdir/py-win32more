from __future__ import annotations
from win32more._prelude import *
import win32more.Windows.Wdk.Foundation
import win32more.Windows.Wdk.System.Memory
import win32more.Windows.Win32.Foundation
@winfunctype('ntdll.dll')
def NtOpenSection(SectionHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE), DesiredAccess: UInt32, ObjectAttributes: POINTER(win32more.Windows.Wdk.Foundation.OBJECT_ATTRIBUTES)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtMapViewOfSection(SectionHandle: win32more.Windows.Win32.Foundation.HANDLE, ProcessHandle: win32more.Windows.Win32.Foundation.HANDLE, BaseAddress: POINTER(VoidPtr), ZeroBits: UIntPtr, CommitSize: UIntPtr, SectionOffset: POINTER(Int64), ViewSize: POINTER(UIntPtr), InheritDisposition: win32more.Windows.Wdk.System.Memory.SECTION_INHERIT, AllocationType: UInt32, Win32Protect: UInt32) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtUnmapViewOfSection(ProcessHandle: win32more.Windows.Win32.Foundation.HANDLE, BaseAddress: VoidPtr) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def ZwOpenSection(SectionHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE), DesiredAccess: UInt32, ObjectAttributes: POINTER(win32more.Windows.Wdk.Foundation.OBJECT_ATTRIBUTES)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def ZwMapViewOfSection(SectionHandle: win32more.Windows.Win32.Foundation.HANDLE, ProcessHandle: win32more.Windows.Win32.Foundation.HANDLE, BaseAddress: POINTER(VoidPtr), ZeroBits: UIntPtr, CommitSize: UIntPtr, SectionOffset: POINTER(Int64), ViewSize: POINTER(UIntPtr), InheritDisposition: win32more.Windows.Wdk.System.Memory.SECTION_INHERIT, AllocationType: UInt32, Win32Protect: UInt32) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def ZwUnmapViewOfSection(ProcessHandle: win32more.Windows.Win32.Foundation.HANDLE, BaseAddress: VoidPtr) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
SECTION_INHERIT = Int32
ViewShare: win32more.Windows.Wdk.System.Memory.SECTION_INHERIT = 1
ViewUnmap: win32more.Windows.Wdk.System.Memory.SECTION_INHERIT = 2


make_ready(__name__)
