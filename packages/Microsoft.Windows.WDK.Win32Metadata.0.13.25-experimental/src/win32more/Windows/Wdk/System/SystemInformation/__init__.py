from __future__ import annotations
from win32more._prelude import *
import win32more.Windows.Wdk.System.SystemInformation
import win32more.Windows.Win32.Foundation
@winfunctype('ntdll.dll')
def NtQuerySystemInformation(SystemInformationClass: win32more.Windows.Wdk.System.SystemInformation.SYSTEM_INFORMATION_CLASS, SystemInformation: VoidPtr, SystemInformationLength: UInt32, ReturnLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def ZwQuerySystemInformation(SystemInformationClass: win32more.Windows.Wdk.System.SystemInformation.SYSTEM_INFORMATION_CLASS, SystemInformation: VoidPtr, SystemInformationLength: UInt32, ReturnLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtQuerySystemTime(SystemTime: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def ZwQuerySystemTime(SystemTime: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtQueryTimerResolution(MaximumTime: POINTER(UInt32), MinimumTime: POINTER(UInt32), CurrentTime: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def ZwQueryTimerResolution(MaximumTime: POINTER(UInt32), MinimumTime: POINTER(UInt32), CurrentTime: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
SYSTEM_INFORMATION_CLASS = Int32
SystemBasicInformation: win32more.Windows.Wdk.System.SystemInformation.SYSTEM_INFORMATION_CLASS = 0
SystemPerformanceInformation: win32more.Windows.Wdk.System.SystemInformation.SYSTEM_INFORMATION_CLASS = 2
SystemTimeOfDayInformation: win32more.Windows.Wdk.System.SystemInformation.SYSTEM_INFORMATION_CLASS = 3
SystemProcessInformation: win32more.Windows.Wdk.System.SystemInformation.SYSTEM_INFORMATION_CLASS = 5
SystemProcessorPerformanceInformation: win32more.Windows.Wdk.System.SystemInformation.SYSTEM_INFORMATION_CLASS = 8
SystemInterruptInformation: win32more.Windows.Wdk.System.SystemInformation.SYSTEM_INFORMATION_CLASS = 23
SystemExceptionInformation: win32more.Windows.Wdk.System.SystemInformation.SYSTEM_INFORMATION_CLASS = 33
SystemRegistryQuotaInformation: win32more.Windows.Wdk.System.SystemInformation.SYSTEM_INFORMATION_CLASS = 37
SystemLookasideInformation: win32more.Windows.Wdk.System.SystemInformation.SYSTEM_INFORMATION_CLASS = 45
SystemCodeIntegrityInformation: win32more.Windows.Wdk.System.SystemInformation.SYSTEM_INFORMATION_CLASS = 103
SystemPolicyInformation: win32more.Windows.Wdk.System.SystemInformation.SYSTEM_INFORMATION_CLASS = 134


make_ready(__name__)
