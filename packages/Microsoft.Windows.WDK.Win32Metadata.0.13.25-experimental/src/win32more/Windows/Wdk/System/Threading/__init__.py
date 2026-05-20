from __future__ import annotations
from win32more._prelude import *
import win32more.Windows.Wdk.Foundation
import win32more.Windows.Wdk.System.SystemServices
import win32more.Windows.Wdk.System.Threading
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Kernel
import win32more.Windows.Win32.System.WindowsProgramming
@winfunctype('ntdll.dll')
def NtQueryInformationProcess(ProcessHandle: win32more.Windows.Win32.Foundation.HANDLE, ProcessInformationClass: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS, ProcessInformation: VoidPtr, ProcessInformationLength: UInt32, ReturnLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def ZwQueryInformationProcess(ProcessHandle: win32more.Windows.Win32.Foundation.HANDLE, ProcessInformationClass: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS, ProcessInformation: VoidPtr, ProcessInformationLength: UInt32, ReturnLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtQueryInformationThread(ThreadHandle: win32more.Windows.Win32.Foundation.HANDLE, ThreadInformationClass: win32more.Windows.Wdk.System.Threading.THREADINFOCLASS, ThreadInformation: VoidPtr, ThreadInformationLength: UInt32, ReturnLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def ZwQueryInformationThread(ThreadHandle: win32more.Windows.Win32.Foundation.HANDLE, ThreadInformationClass: win32more.Windows.Wdk.System.Threading.THREADINFOCLASS, ThreadInformation: VoidPtr, ThreadInformationLength: UInt32, ReturnLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtSetInformationThread(ThreadHandle: win32more.Windows.Win32.Foundation.HANDLE, ThreadInformationClass: win32more.Windows.Wdk.System.Threading.THREADINFOCLASS, ThreadInformation: VoidPtr, ThreadInformationLength: UInt32) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtWaitForSingleObject(Handle: win32more.Windows.Win32.Foundation.HANDLE, Alertable: win32more.Windows.Win32.Foundation.BOOLEAN, Timeout: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtTerminateProcess(ProcessHandle: win32more.Windows.Win32.Foundation.HANDLE, ExitStatus: win32more.Windows.Win32.Foundation.NTSTATUS) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtCreateTimer(TimerHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE), DesiredAccess: UInt32, ObjectAttributes: POINTER(win32more.Windows.Wdk.Foundation.OBJECT_ATTRIBUTES), TimerType: win32more.Windows.Win32.System.Kernel.TIMER_TYPE) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtOpenTimer(TimerHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE), DesiredAccess: UInt32, ObjectAttributes: POINTER(win32more.Windows.Wdk.Foundation.OBJECT_ATTRIBUTES)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtCancelTimer(TimerHandle: win32more.Windows.Win32.Foundation.HANDLE, CurrentState: POINTER(win32more.Windows.Win32.Foundation.BOOLEAN)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtSetTimer(TimerHandle: win32more.Windows.Win32.Foundation.HANDLE, DueTime: POINTER(Int64), TimerApcRoutine: win32more.Windows.Wdk.System.SystemServices.PTIMER_APC_ROUTINE, TimerContext: VoidPtr, ResumeTimer: win32more.Windows.Win32.Foundation.BOOLEAN, Period: Int32, PreviousState: POINTER(win32more.Windows.Win32.Foundation.BOOLEAN)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtSetTimerEx(TimerHandle: win32more.Windows.Win32.Foundation.HANDLE, TimerSetInformationClass: win32more.Windows.Wdk.System.Threading.TIMER_SET_INFORMATION_CLASS, TimerSetInformation: VoidPtr, TimerSetInformationLength: UInt32) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtOpenEvent(EventHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE), DesiredAccess: UInt32, ObjectAttributes: POINTER(win32more.Windows.Wdk.Foundation.OBJECT_ATTRIBUTES)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def ZwWaitForSingleObject(Handle: win32more.Windows.Win32.Foundation.HANDLE, Alertable: win32more.Windows.Win32.Foundation.BOOLEAN, Timeout: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def ZwOpenEvent(EventHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE), DesiredAccess: UInt32, ObjectAttributes: POINTER(win32more.Windows.Wdk.Foundation.OBJECT_ATTRIBUTES)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtOpenProcess(ProcessHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE), DesiredAccess: UInt32, ObjectAttributes: POINTER(win32more.Windows.Wdk.Foundation.OBJECT_ATTRIBUTES), ClientId: POINTER(win32more.Windows.Win32.System.WindowsProgramming.CLIENT_ID)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def ZwSetInformationThread(ThreadHandle: win32more.Windows.Win32.Foundation.HANDLE, ThreadInformationClass: win32more.Windows.Wdk.System.Threading.THREADINFOCLASS, ThreadInformation: VoidPtr, ThreadInformationLength: UInt32) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def ZwCreateTimer(TimerHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE), DesiredAccess: UInt32, ObjectAttributes: POINTER(win32more.Windows.Wdk.Foundation.OBJECT_ATTRIBUTES), TimerType: win32more.Windows.Win32.System.Kernel.TIMER_TYPE) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def ZwOpenTimer(TimerHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE), DesiredAccess: UInt32, ObjectAttributes: POINTER(win32more.Windows.Wdk.Foundation.OBJECT_ATTRIBUTES)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def ZwCancelTimer(TimerHandle: win32more.Windows.Win32.Foundation.HANDLE, CurrentState: POINTER(win32more.Windows.Win32.Foundation.BOOLEAN)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def ZwSetTimer(TimerHandle: win32more.Windows.Win32.Foundation.HANDLE, DueTime: POINTER(Int64), TimerApcRoutine: win32more.Windows.Wdk.System.SystemServices.PTIMER_APC_ROUTINE, TimerContext: VoidPtr, ResumeTimer: win32more.Windows.Win32.Foundation.BOOLEAN, Period: Int32, PreviousState: POINTER(win32more.Windows.Win32.Foundation.BOOLEAN)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def ZwSetTimerEx(TimerHandle: win32more.Windows.Win32.Foundation.HANDLE, TimerSetInformationClass: win32more.Windows.Wdk.System.Threading.TIMER_SET_INFORMATION_CLASS, TimerSetInformation: VoidPtr, TimerSetInformationLength: UInt32) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def ZwTerminateProcess(ProcessHandle: win32more.Windows.Win32.Foundation.HANDLE, ExitStatus: win32more.Windows.Win32.Foundation.NTSTATUS) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def ZwOpenProcess(ProcessHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE), DesiredAccess: UInt32, ObjectAttributes: POINTER(win32more.Windows.Wdk.Foundation.OBJECT_ATTRIBUTES), ClientId: POINTER(win32more.Windows.Win32.System.WindowsProgramming.CLIENT_ID)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
PROCESSINFOCLASS = Int32
ProcessBasicInformation: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 0
ProcessQuotaLimits: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 1
ProcessIoCounters: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 2
ProcessVmCounters: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 3
ProcessTimes: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 4
ProcessBasePriority: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 5
ProcessRaisePriority: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 6
ProcessDebugPort: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 7
ProcessExceptionPort: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 8
ProcessAccessToken: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 9
ProcessLdtInformation: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 10
ProcessLdtSize: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 11
ProcessDefaultHardErrorMode: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 12
ProcessIoPortHandlers: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 13
ProcessPooledUsageAndLimits: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 14
ProcessWorkingSetWatch: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 15
ProcessUserModeIOPL: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 16
ProcessEnableAlignmentFaultFixup: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 17
ProcessPriorityClass: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 18
ProcessWx86Information: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 19
ProcessHandleCount: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 20
ProcessAffinityMask: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 21
ProcessPriorityBoost: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 22
ProcessDeviceMap: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 23
ProcessSessionInformation: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 24
ProcessForegroundInformation: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 25
ProcessWow64Information: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 26
ProcessImageFileName: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 27
ProcessLUIDDeviceMapsEnabled: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 28
ProcessBreakOnTermination: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 29
ProcessDebugObjectHandle: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 30
ProcessDebugFlags: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 31
ProcessHandleTracing: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 32
ProcessIoPriority: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 33
ProcessExecuteFlags: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 34
ProcessTlsInformation: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 35
ProcessCookie: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 36
ProcessImageInformation: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 37
ProcessCycleTime: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 38
ProcessPagePriority: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 39
ProcessInstrumentationCallback: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 40
ProcessThreadStackAllocation: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 41
ProcessWorkingSetWatchEx: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 42
ProcessImageFileNameWin32: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 43
ProcessImageFileMapping: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 44
ProcessAffinityUpdateMode: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 45
ProcessMemoryAllocationMode: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 46
ProcessGroupInformation: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 47
ProcessTokenVirtualizationEnabled: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 48
ProcessOwnerInformation: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 49
ProcessWindowInformation: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 50
ProcessHandleInformation: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 51
ProcessMitigationPolicy: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 52
ProcessDynamicFunctionTableInformation: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 53
ProcessHandleCheckingMode: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 54
ProcessKeepAliveCount: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 55
ProcessRevokeFileHandles: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 56
ProcessWorkingSetControl: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 57
ProcessHandleTable: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 58
ProcessCheckStackExtentsMode: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 59
ProcessCommandLineInformation: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 60
ProcessProtectionInformation: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 61
ProcessMemoryExhaustion: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 62
ProcessFaultInformation: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 63
ProcessTelemetryIdInformation: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 64
ProcessCommitReleaseInformation: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 65
ProcessReserved1Information: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 66
ProcessReserved2Information: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 67
ProcessSubsystemProcess: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 68
ProcessInPrivate: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 70
ProcessRaiseUMExceptionOnInvalidHandleClose: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 71
ProcessSubsystemInformation: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 75
ProcessWin32kSyscallFilterInformation: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 79
ProcessEnergyTrackingState: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 82
MaxProcessInfoClass: win32more.Windows.Wdk.System.Threading.PROCESSINFOCLASS = 83
THREADINFOCLASS = Int32
ThreadBasicInformation: win32more.Windows.Wdk.System.Threading.THREADINFOCLASS = 0
ThreadTimes: win32more.Windows.Wdk.System.Threading.THREADINFOCLASS = 1
ThreadPriority: win32more.Windows.Wdk.System.Threading.THREADINFOCLASS = 2
ThreadBasePriority: win32more.Windows.Wdk.System.Threading.THREADINFOCLASS = 3
ThreadAffinityMask: win32more.Windows.Wdk.System.Threading.THREADINFOCLASS = 4
ThreadImpersonationToken: win32more.Windows.Wdk.System.Threading.THREADINFOCLASS = 5
ThreadDescriptorTableEntry: win32more.Windows.Wdk.System.Threading.THREADINFOCLASS = 6
ThreadEnableAlignmentFaultFixup: win32more.Windows.Wdk.System.Threading.THREADINFOCLASS = 7
ThreadEventPair_Reusable: win32more.Windows.Wdk.System.Threading.THREADINFOCLASS = 8
ThreadQuerySetWin32StartAddress: win32more.Windows.Wdk.System.Threading.THREADINFOCLASS = 9
ThreadZeroTlsCell: win32more.Windows.Wdk.System.Threading.THREADINFOCLASS = 10
ThreadPerformanceCount: win32more.Windows.Wdk.System.Threading.THREADINFOCLASS = 11
ThreadAmILastThread: win32more.Windows.Wdk.System.Threading.THREADINFOCLASS = 12
ThreadIdealProcessor: win32more.Windows.Wdk.System.Threading.THREADINFOCLASS = 13
ThreadPriorityBoost: win32more.Windows.Wdk.System.Threading.THREADINFOCLASS = 14
ThreadSetTlsArrayAddress: win32more.Windows.Wdk.System.Threading.THREADINFOCLASS = 15
ThreadIsIoPending: win32more.Windows.Wdk.System.Threading.THREADINFOCLASS = 16
ThreadHideFromDebugger: win32more.Windows.Wdk.System.Threading.THREADINFOCLASS = 17
ThreadBreakOnTermination: win32more.Windows.Wdk.System.Threading.THREADINFOCLASS = 18
ThreadSwitchLegacyState: win32more.Windows.Wdk.System.Threading.THREADINFOCLASS = 19
ThreadIsTerminated: win32more.Windows.Wdk.System.Threading.THREADINFOCLASS = 20
ThreadLastSystemCall: win32more.Windows.Wdk.System.Threading.THREADINFOCLASS = 21
ThreadIoPriority: win32more.Windows.Wdk.System.Threading.THREADINFOCLASS = 22
ThreadCycleTime: win32more.Windows.Wdk.System.Threading.THREADINFOCLASS = 23
ThreadPagePriority: win32more.Windows.Wdk.System.Threading.THREADINFOCLASS = 24
ThreadActualBasePriority: win32more.Windows.Wdk.System.Threading.THREADINFOCLASS = 25
ThreadTebInformation: win32more.Windows.Wdk.System.Threading.THREADINFOCLASS = 26
ThreadCSwitchMon: win32more.Windows.Wdk.System.Threading.THREADINFOCLASS = 27
ThreadCSwitchPmu: win32more.Windows.Wdk.System.Threading.THREADINFOCLASS = 28
ThreadWow64Context: win32more.Windows.Wdk.System.Threading.THREADINFOCLASS = 29
ThreadGroupInformation: win32more.Windows.Wdk.System.Threading.THREADINFOCLASS = 30
ThreadUmsInformation: win32more.Windows.Wdk.System.Threading.THREADINFOCLASS = 31
ThreadCounterProfiling: win32more.Windows.Wdk.System.Threading.THREADINFOCLASS = 32
ThreadIdealProcessorEx: win32more.Windows.Wdk.System.Threading.THREADINFOCLASS = 33
ThreadCpuAccountingInformation: win32more.Windows.Wdk.System.Threading.THREADINFOCLASS = 34
ThreadSuspendCount: win32more.Windows.Wdk.System.Threading.THREADINFOCLASS = 35
ThreadActualGroupAffinity: win32more.Windows.Wdk.System.Threading.THREADINFOCLASS = 41
ThreadDynamicCodePolicyInfo: win32more.Windows.Wdk.System.Threading.THREADINFOCLASS = 42
ThreadSubsystemInformation: win32more.Windows.Wdk.System.Threading.THREADINFOCLASS = 45
MaxThreadInfoClass: win32more.Windows.Wdk.System.Threading.THREADINFOCLASS = 56
ThreadNameInformation: win32more.Windows.Wdk.System.Threading.THREADINFOCLASS = 38
TIMER_SET_INFORMATION_CLASS = Int32
TimerSetCoalescableTimer: win32more.Windows.Wdk.System.Threading.TIMER_SET_INFORMATION_CLASS = 0
MaxTimerInfoClass: win32more.Windows.Wdk.System.Threading.TIMER_SET_INFORMATION_CLASS = 1


make_ready(__name__)
