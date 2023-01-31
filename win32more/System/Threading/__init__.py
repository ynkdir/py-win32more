from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Security
import win32more.System.Kernel
import win32more.System.SystemInformation
import win32more.System.SystemServices
import win32more.System.Threading
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
class APP_MEMORY_INFORMATION(Structure):
    AvailableCommit: UInt64
    PrivateCommitUsage: UInt64
    PeakPrivateCommitUsage: UInt64
    TotalCommitUsage: UInt64
AVRT_PRIORITY = Int32
AVRT_PRIORITY_VERYLOW: AVRT_PRIORITY = -2
AVRT_PRIORITY_LOW: AVRT_PRIORITY = -1
AVRT_PRIORITY_NORMAL: AVRT_PRIORITY = 0
AVRT_PRIORITY_HIGH: AVRT_PRIORITY = 1
AVRT_PRIORITY_CRITICAL: AVRT_PRIORITY = 2
FLS_OUT_OF_INDEXES: UInt32 = 4294967295
PRIVATE_NAMESPACE_FLAG_DESTROY: UInt32 = 1
TLS_OUT_OF_INDEXES: UInt32 = 4294967295
PROC_THREAD_ATTRIBUTE_REPLACE_VALUE: UInt32 = 1
THREAD_POWER_THROTTLING_CURRENT_VERSION: UInt32 = 1
THREAD_POWER_THROTTLING_EXECUTION_SPEED: UInt32 = 1
THREAD_POWER_THROTTLING_VALID_FLAGS: UInt32 = 1
PME_CURRENT_VERSION: UInt32 = 1
PME_FAILFAST_ON_COMMIT_FAIL_DISABLE: UInt32 = 0
PME_FAILFAST_ON_COMMIT_FAIL_ENABLE: UInt32 = 1
PROCESS_POWER_THROTTLING_CURRENT_VERSION: UInt32 = 1
PROCESS_POWER_THROTTLING_EXECUTION_SPEED: UInt32 = 1
PROCESS_POWER_THROTTLING_IGNORE_TIMER_RESOLUTION: UInt32 = 4
PROCESS_LEAP_SECOND_INFO_FLAG_ENABLE_SIXTY_SECOND: UInt32 = 1
PROCESS_LEAP_SECOND_INFO_VALID_FLAGS: UInt32 = 1
INIT_ONCE_CHECK_ONLY: UInt32 = 1
INIT_ONCE_ASYNC: UInt32 = 2
INIT_ONCE_INIT_FAILED: UInt32 = 4
INIT_ONCE_CTX_RESERVED_BITS: UInt32 = 2
CONDITION_VARIABLE_LOCKMODE_SHARED: UInt32 = 1
CREATE_MUTEX_INITIAL_OWNER: UInt32 = 1
CREATE_WAITABLE_TIMER_MANUAL_RESET: UInt32 = 1
CREATE_WAITABLE_TIMER_HIGH_RESOLUTION: UInt32 = 2
SYNCHRONIZATION_BARRIER_FLAGS_SPIN_ONLY: UInt32 = 1
SYNCHRONIZATION_BARRIER_FLAGS_BLOCK_ONLY: UInt32 = 2
SYNCHRONIZATION_BARRIER_FLAGS_NO_DELETE: UInt32 = 4
PROC_THREAD_ATTRIBUTE_PARENT_PROCESS: UInt32 = 131072
PROC_THREAD_ATTRIBUTE_HANDLE_LIST: UInt32 = 131074
PROC_THREAD_ATTRIBUTE_GROUP_AFFINITY: UInt32 = 196611
PROC_THREAD_ATTRIBUTE_PREFERRED_NODE: UInt32 = 131076
PROC_THREAD_ATTRIBUTE_IDEAL_PROCESSOR: UInt32 = 196613
PROC_THREAD_ATTRIBUTE_UMS_THREAD: UInt32 = 196614
PROC_THREAD_ATTRIBUTE_MITIGATION_POLICY: UInt32 = 131079
PROC_THREAD_ATTRIBUTE_SECURITY_CAPABILITIES: UInt32 = 131081
PROC_THREAD_ATTRIBUTE_PROTECTION_LEVEL: UInt32 = 131083
PROC_THREAD_ATTRIBUTE_PSEUDOCONSOLE: UInt32 = 131094
PROC_THREAD_ATTRIBUTE_MACHINE_TYPE: UInt32 = 131097
PROC_THREAD_ATTRIBUTE_ENABLE_OPTIONAL_XSTATE_FEATURES: UInt32 = 196635
PROC_THREAD_ATTRIBUTE_WIN32K_FILTER: UInt32 = 131088
PROC_THREAD_ATTRIBUTE_JOB_LIST: UInt32 = 131085
PROC_THREAD_ATTRIBUTE_CHILD_PROCESS_POLICY: UInt32 = 131086
PROC_THREAD_ATTRIBUTE_ALL_APPLICATION_PACKAGES_POLICY: UInt32 = 131087
PROC_THREAD_ATTRIBUTE_DESKTOP_APP_POLICY: UInt32 = 131090
PROC_THREAD_ATTRIBUTE_MITIGATION_AUDIT_POLICY: UInt32 = 131096
PROC_THREAD_ATTRIBUTE_COMPONENT_FILTER: UInt32 = 131098
@winfunctype('KERNEL32.dll')
def GetProcessWorkingSetSize(hProcess: win32more.Foundation.HANDLE, lpMinimumWorkingSetSize: POINTER(UIntPtr), lpMaximumWorkingSetSize: POINTER(UIntPtr)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetProcessWorkingSetSize(hProcess: win32more.Foundation.HANDLE, dwMinimumWorkingSetSize: UIntPtr, dwMaximumWorkingSetSize: UIntPtr) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FlsAlloc(lpCallback: win32more.System.Threading.PFLS_CALLBACK_FUNCTION) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def FlsGetValue(dwFlsIndex: UInt32) -> c_void_p: ...
@winfunctype('KERNEL32.dll')
def FlsSetValue(dwFlsIndex: UInt32, lpFlsData: c_void_p) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FlsFree(dwFlsIndex: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def IsThreadAFiber() -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def InitializeSRWLock(SRWLock: POINTER(win32more.System.Threading.RTL_SRWLOCK_head)) -> Void: ...
@winfunctype('KERNEL32.dll')
def ReleaseSRWLockExclusive(SRWLock: POINTER(win32more.System.Threading.RTL_SRWLOCK_head)) -> Void: ...
@winfunctype('KERNEL32.dll')
def ReleaseSRWLockShared(SRWLock: POINTER(win32more.System.Threading.RTL_SRWLOCK_head)) -> Void: ...
@winfunctype('KERNEL32.dll')
def AcquireSRWLockExclusive(SRWLock: POINTER(win32more.System.Threading.RTL_SRWLOCK_head)) -> Void: ...
@winfunctype('KERNEL32.dll')
def AcquireSRWLockShared(SRWLock: POINTER(win32more.System.Threading.RTL_SRWLOCK_head)) -> Void: ...
@winfunctype('KERNEL32.dll')
def TryAcquireSRWLockExclusive(SRWLock: POINTER(win32more.System.Threading.RTL_SRWLOCK_head)) -> win32more.Foundation.BOOLEAN: ...
@winfunctype('KERNEL32.dll')
def TryAcquireSRWLockShared(SRWLock: POINTER(win32more.System.Threading.RTL_SRWLOCK_head)) -> win32more.Foundation.BOOLEAN: ...
@winfunctype('KERNEL32.dll')
def InitializeCriticalSection(lpCriticalSection: POINTER(win32more.System.Threading.RTL_CRITICAL_SECTION_head)) -> Void: ...
@winfunctype('KERNEL32.dll')
def EnterCriticalSection(lpCriticalSection: POINTER(win32more.System.Threading.RTL_CRITICAL_SECTION_head)) -> Void: ...
@winfunctype('KERNEL32.dll')
def LeaveCriticalSection(lpCriticalSection: POINTER(win32more.System.Threading.RTL_CRITICAL_SECTION_head)) -> Void: ...
@winfunctype('KERNEL32.dll')
def InitializeCriticalSectionAndSpinCount(lpCriticalSection: POINTER(win32more.System.Threading.RTL_CRITICAL_SECTION_head), dwSpinCount: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def InitializeCriticalSectionEx(lpCriticalSection: POINTER(win32more.System.Threading.RTL_CRITICAL_SECTION_head), dwSpinCount: UInt32, Flags: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetCriticalSectionSpinCount(lpCriticalSection: POINTER(win32more.System.Threading.RTL_CRITICAL_SECTION_head), dwSpinCount: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def TryEnterCriticalSection(lpCriticalSection: POINTER(win32more.System.Threading.RTL_CRITICAL_SECTION_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DeleteCriticalSection(lpCriticalSection: POINTER(win32more.System.Threading.RTL_CRITICAL_SECTION_head)) -> Void: ...
@winfunctype('KERNEL32.dll')
def InitOnceInitialize(InitOnce: POINTER(win32more.System.Threading.RTL_RUN_ONCE_head)) -> Void: ...
@winfunctype('KERNEL32.dll')
def InitOnceExecuteOnce(InitOnce: POINTER(win32more.System.Threading.RTL_RUN_ONCE_head), InitFn: win32more.System.Threading.PINIT_ONCE_FN, Parameter: c_void_p, Context: POINTER(c_void_p)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def InitOnceBeginInitialize(lpInitOnce: POINTER(win32more.System.Threading.RTL_RUN_ONCE_head), dwFlags: UInt32, fPending: POINTER(win32more.Foundation.BOOL), lpContext: POINTER(c_void_p)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def InitOnceComplete(lpInitOnce: POINTER(win32more.System.Threading.RTL_RUN_ONCE_head), dwFlags: UInt32, lpContext: c_void_p) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def InitializeConditionVariable(ConditionVariable: POINTER(win32more.System.Threading.RTL_CONDITION_VARIABLE_head)) -> Void: ...
@winfunctype('KERNEL32.dll')
def WakeConditionVariable(ConditionVariable: POINTER(win32more.System.Threading.RTL_CONDITION_VARIABLE_head)) -> Void: ...
@winfunctype('KERNEL32.dll')
def WakeAllConditionVariable(ConditionVariable: POINTER(win32more.System.Threading.RTL_CONDITION_VARIABLE_head)) -> Void: ...
@winfunctype('KERNEL32.dll')
def SleepConditionVariableCS(ConditionVariable: POINTER(win32more.System.Threading.RTL_CONDITION_VARIABLE_head), CriticalSection: POINTER(win32more.System.Threading.RTL_CRITICAL_SECTION_head), dwMilliseconds: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SleepConditionVariableSRW(ConditionVariable: POINTER(win32more.System.Threading.RTL_CONDITION_VARIABLE_head), SRWLock: POINTER(win32more.System.Threading.RTL_SRWLOCK_head), dwMilliseconds: UInt32, Flags: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetEvent(hEvent: win32more.Foundation.HANDLE) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ResetEvent(hEvent: win32more.Foundation.HANDLE) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ReleaseSemaphore(hSemaphore: win32more.Foundation.HANDLE, lReleaseCount: Int32, lpPreviousCount: POINTER(Int32)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ReleaseMutex(hMutex: win32more.Foundation.HANDLE) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WaitForSingleObject(hHandle: win32more.Foundation.HANDLE, dwMilliseconds: UInt32) -> win32more.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def SleepEx(dwMilliseconds: UInt32, bAlertable: win32more.Foundation.BOOL) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def WaitForSingleObjectEx(hHandle: win32more.Foundation.HANDLE, dwMilliseconds: UInt32, bAlertable: win32more.Foundation.BOOL) -> win32more.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def WaitForMultipleObjectsEx(nCount: UInt32, lpHandles: POINTER(win32more.Foundation.HANDLE), bWaitAll: win32more.Foundation.BOOL, dwMilliseconds: UInt32, bAlertable: win32more.Foundation.BOOL) -> win32more.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def CreateMutexA(lpMutexAttributes: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), bInitialOwner: win32more.Foundation.BOOL, lpName: win32more.Foundation.PSTR) -> win32more.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def CreateMutexW(lpMutexAttributes: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), bInitialOwner: win32more.Foundation.BOOL, lpName: win32more.Foundation.PWSTR) -> win32more.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def OpenMutexW(dwDesiredAccess: win32more.System.Threading.SYNCHRONIZATION_ACCESS_RIGHTS, bInheritHandle: win32more.Foundation.BOOL, lpName: win32more.Foundation.PWSTR) -> win32more.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def CreateEventA(lpEventAttributes: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), bManualReset: win32more.Foundation.BOOL, bInitialState: win32more.Foundation.BOOL, lpName: win32more.Foundation.PSTR) -> win32more.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def CreateEventW(lpEventAttributes: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), bManualReset: win32more.Foundation.BOOL, bInitialState: win32more.Foundation.BOOL, lpName: win32more.Foundation.PWSTR) -> win32more.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def OpenEventA(dwDesiredAccess: win32more.System.Threading.SYNCHRONIZATION_ACCESS_RIGHTS, bInheritHandle: win32more.Foundation.BOOL, lpName: win32more.Foundation.PSTR) -> win32more.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def OpenEventW(dwDesiredAccess: win32more.System.Threading.SYNCHRONIZATION_ACCESS_RIGHTS, bInheritHandle: win32more.Foundation.BOOL, lpName: win32more.Foundation.PWSTR) -> win32more.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def OpenSemaphoreW(dwDesiredAccess: win32more.System.Threading.SYNCHRONIZATION_ACCESS_RIGHTS, bInheritHandle: win32more.Foundation.BOOL, lpName: win32more.Foundation.PWSTR) -> win32more.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def OpenWaitableTimerW(dwDesiredAccess: win32more.System.Threading.SYNCHRONIZATION_ACCESS_RIGHTS, bInheritHandle: win32more.Foundation.BOOL, lpTimerName: win32more.Foundation.PWSTR) -> win32more.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def SetWaitableTimerEx(hTimer: win32more.Foundation.HANDLE, lpDueTime: POINTER(win32more.Foundation.LARGE_INTEGER_head), lPeriod: Int32, pfnCompletionRoutine: win32more.System.Threading.PTIMERAPCROUTINE, lpArgToCompletionRoutine: c_void_p, WakeContext: POINTER(win32more.System.Threading.REASON_CONTEXT_head), TolerableDelay: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetWaitableTimer(hTimer: win32more.Foundation.HANDLE, lpDueTime: POINTER(win32more.Foundation.LARGE_INTEGER_head), lPeriod: Int32, pfnCompletionRoutine: win32more.System.Threading.PTIMERAPCROUTINE, lpArgToCompletionRoutine: c_void_p, fResume: win32more.Foundation.BOOL) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CancelWaitableTimer(hTimer: win32more.Foundation.HANDLE) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateMutexExA(lpMutexAttributes: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), lpName: win32more.Foundation.PSTR, dwFlags: UInt32, dwDesiredAccess: UInt32) -> win32more.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def CreateMutexExW(lpMutexAttributes: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), lpName: win32more.Foundation.PWSTR, dwFlags: UInt32, dwDesiredAccess: UInt32) -> win32more.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def CreateEventExA(lpEventAttributes: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), lpName: win32more.Foundation.PSTR, dwFlags: win32more.System.Threading.CREATE_EVENT, dwDesiredAccess: UInt32) -> win32more.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def CreateEventExW(lpEventAttributes: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), lpName: win32more.Foundation.PWSTR, dwFlags: win32more.System.Threading.CREATE_EVENT, dwDesiredAccess: UInt32) -> win32more.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def CreateSemaphoreExW(lpSemaphoreAttributes: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), lInitialCount: Int32, lMaximumCount: Int32, lpName: win32more.Foundation.PWSTR, dwFlags: UInt32, dwDesiredAccess: UInt32) -> win32more.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def CreateWaitableTimerExW(lpTimerAttributes: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), lpTimerName: win32more.Foundation.PWSTR, dwFlags: UInt32, dwDesiredAccess: UInt32) -> win32more.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def EnterSynchronizationBarrier(lpBarrier: POINTER(win32more.System.Threading.RTL_BARRIER_head), dwFlags: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def InitializeSynchronizationBarrier(lpBarrier: POINTER(win32more.System.Threading.RTL_BARRIER_head), lTotalThreads: Int32, lSpinCount: Int32) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DeleteSynchronizationBarrier(lpBarrier: POINTER(win32more.System.Threading.RTL_BARRIER_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def Sleep(dwMilliseconds: UInt32) -> Void: ...
@winfunctype('api-ms-win-core-synch-l1-2-0.dll')
def WaitOnAddress(Address: c_void_p, CompareAddress: c_void_p, AddressSize: UIntPtr, dwMilliseconds: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-synch-l1-2-0.dll')
def WakeByAddressSingle(Address: c_void_p) -> Void: ...
@winfunctype('api-ms-win-core-synch-l1-2-0.dll')
def WakeByAddressAll(Address: c_void_p) -> Void: ...
@winfunctype('KERNEL32.dll')
def WaitForMultipleObjects(nCount: UInt32, lpHandles: POINTER(win32more.Foundation.HANDLE), bWaitAll: win32more.Foundation.BOOL, dwMilliseconds: UInt32) -> win32more.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def CreateSemaphoreW(lpSemaphoreAttributes: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), lInitialCount: Int32, lMaximumCount: Int32, lpName: win32more.Foundation.PWSTR) -> win32more.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def CreateWaitableTimerW(lpTimerAttributes: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), bManualReset: win32more.Foundation.BOOL, lpTimerName: win32more.Foundation.PWSTR) -> win32more.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def InitializeSListHead(ListHead: POINTER(win32more.System.Kernel.SLIST_HEADER_head)) -> Void: ...
@winfunctype('KERNEL32.dll')
def InterlockedPopEntrySList(ListHead: POINTER(win32more.System.Kernel.SLIST_HEADER_head)) -> POINTER(win32more.System.Kernel.SLIST_ENTRY_head): ...
@winfunctype('KERNEL32.dll')
def InterlockedPushEntrySList(ListHead: POINTER(win32more.System.Kernel.SLIST_HEADER_head), ListEntry: POINTER(win32more.System.Kernel.SLIST_ENTRY_head)) -> POINTER(win32more.System.Kernel.SLIST_ENTRY_head): ...
@winfunctype('KERNEL32.dll')
def InterlockedPushListSListEx(ListHead: POINTER(win32more.System.Kernel.SLIST_HEADER_head), List: POINTER(win32more.System.Kernel.SLIST_ENTRY_head), ListEnd: POINTER(win32more.System.Kernel.SLIST_ENTRY_head), Count: UInt32) -> POINTER(win32more.System.Kernel.SLIST_ENTRY_head): ...
@winfunctype('KERNEL32.dll')
def InterlockedFlushSList(ListHead: POINTER(win32more.System.Kernel.SLIST_HEADER_head)) -> POINTER(win32more.System.Kernel.SLIST_ENTRY_head): ...
@winfunctype('KERNEL32.dll')
def QueryDepthSList(ListHead: POINTER(win32more.System.Kernel.SLIST_HEADER_head)) -> UInt16: ...
@winfunctype('KERNEL32.dll')
def QueueUserAPC(pfnAPC: win32more.Foundation.PAPCFUNC, hThread: win32more.Foundation.HANDLE, dwData: UIntPtr) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def QueueUserAPC2(ApcRoutine: win32more.Foundation.PAPCFUNC, Thread: win32more.Foundation.HANDLE, Data: UIntPtr, Flags: win32more.System.Threading.QUEUE_USER_APC_FLAGS) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetProcessTimes(hProcess: win32more.Foundation.HANDLE, lpCreationTime: POINTER(win32more.Foundation.FILETIME_head), lpExitTime: POINTER(win32more.Foundation.FILETIME_head), lpKernelTime: POINTER(win32more.Foundation.FILETIME_head), lpUserTime: POINTER(win32more.Foundation.FILETIME_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetCurrentProcess() -> win32more.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def GetCurrentProcessId() -> UInt32: ...
@winfunctype('KERNEL32.dll')
def ExitProcess(uExitCode: UInt32) -> Void: ...
@winfunctype('KERNEL32.dll')
def TerminateProcess(hProcess: win32more.Foundation.HANDLE, uExitCode: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetExitCodeProcess(hProcess: win32more.Foundation.HANDLE, lpExitCode: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SwitchToThread() -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateThread(lpThreadAttributes: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), dwStackSize: UIntPtr, lpStartAddress: win32more.System.Threading.LPTHREAD_START_ROUTINE, lpParameter: c_void_p, dwCreationFlags: win32more.System.Threading.THREAD_CREATION_FLAGS, lpThreadId: POINTER(UInt32)) -> win32more.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def CreateRemoteThread(hProcess: win32more.Foundation.HANDLE, lpThreadAttributes: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), dwStackSize: UIntPtr, lpStartAddress: win32more.System.Threading.LPTHREAD_START_ROUTINE, lpParameter: c_void_p, dwCreationFlags: UInt32, lpThreadId: POINTER(UInt32)) -> win32more.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def GetCurrentThread() -> win32more.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def GetCurrentThreadId() -> UInt32: ...
@winfunctype('KERNEL32.dll')
def OpenThread(dwDesiredAccess: win32more.System.Threading.THREAD_ACCESS_RIGHTS, bInheritHandle: win32more.Foundation.BOOL, dwThreadId: UInt32) -> win32more.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def SetThreadPriority(hThread: win32more.Foundation.HANDLE, nPriority: win32more.System.Threading.THREAD_PRIORITY) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetThreadPriorityBoost(hThread: win32more.Foundation.HANDLE, bDisablePriorityBoost: win32more.Foundation.BOOL) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetThreadPriorityBoost(hThread: win32more.Foundation.HANDLE, pDisablePriorityBoost: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetThreadPriority(hThread: win32more.Foundation.HANDLE) -> Int32: ...
@winfunctype('KERNEL32.dll')
def ExitThread(dwExitCode: UInt32) -> Void: ...
@winfunctype('KERNEL32.dll')
def TerminateThread(hThread: win32more.Foundation.HANDLE, dwExitCode: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetExitCodeThread(hThread: win32more.Foundation.HANDLE, lpExitCode: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SuspendThread(hThread: win32more.Foundation.HANDLE) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def ResumeThread(hThread: win32more.Foundation.HANDLE) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def TlsAlloc() -> UInt32: ...
@winfunctype('KERNEL32.dll')
def TlsGetValue(dwTlsIndex: UInt32) -> c_void_p: ...
@winfunctype('KERNEL32.dll')
def TlsSetValue(dwTlsIndex: UInt32, lpTlsValue: c_void_p) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def TlsFree(dwTlsIndex: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateProcessA(lpApplicationName: win32more.Foundation.PSTR, lpCommandLine: win32more.Foundation.PSTR, lpProcessAttributes: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), lpThreadAttributes: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), bInheritHandles: win32more.Foundation.BOOL, dwCreationFlags: win32more.System.Threading.PROCESS_CREATION_FLAGS, lpEnvironment: c_void_p, lpCurrentDirectory: win32more.Foundation.PSTR, lpStartupInfo: POINTER(win32more.System.Threading.STARTUPINFOA_head), lpProcessInformation: POINTER(win32more.System.Threading.PROCESS_INFORMATION_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateProcessW(lpApplicationName: win32more.Foundation.PWSTR, lpCommandLine: win32more.Foundation.PWSTR, lpProcessAttributes: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), lpThreadAttributes: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), bInheritHandles: win32more.Foundation.BOOL, dwCreationFlags: win32more.System.Threading.PROCESS_CREATION_FLAGS, lpEnvironment: c_void_p, lpCurrentDirectory: win32more.Foundation.PWSTR, lpStartupInfo: POINTER(win32more.System.Threading.STARTUPINFOW_head), lpProcessInformation: POINTER(win32more.System.Threading.PROCESS_INFORMATION_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetProcessShutdownParameters(dwLevel: UInt32, dwFlags: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetProcessVersion(ProcessId: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetStartupInfoW(lpStartupInfo: POINTER(win32more.System.Threading.STARTUPINFOW_head)) -> Void: ...
@winfunctype('ADVAPI32.dll')
def CreateProcessAsUserW(hToken: win32more.Foundation.HANDLE, lpApplicationName: win32more.Foundation.PWSTR, lpCommandLine: win32more.Foundation.PWSTR, lpProcessAttributes: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), lpThreadAttributes: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), bInheritHandles: win32more.Foundation.BOOL, dwCreationFlags: win32more.System.Threading.PROCESS_CREATION_FLAGS, lpEnvironment: c_void_p, lpCurrentDirectory: win32more.Foundation.PWSTR, lpStartupInfo: POINTER(win32more.System.Threading.STARTUPINFOW_head), lpProcessInformation: POINTER(win32more.System.Threading.PROCESS_INFORMATION_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def SetThreadToken(Thread: POINTER(win32more.Foundation.HANDLE), Token: win32more.Foundation.HANDLE) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def OpenProcessToken(ProcessHandle: win32more.Foundation.HANDLE, DesiredAccess: win32more.Security.TOKEN_ACCESS_MASK, TokenHandle: POINTER(win32more.Foundation.HANDLE)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def OpenThreadToken(ThreadHandle: win32more.Foundation.HANDLE, DesiredAccess: win32more.Security.TOKEN_ACCESS_MASK, OpenAsSelf: win32more.Foundation.BOOL, TokenHandle: POINTER(win32more.Foundation.HANDLE)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetPriorityClass(hProcess: win32more.Foundation.HANDLE, dwPriorityClass: win32more.System.Threading.PROCESS_CREATION_FLAGS) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetPriorityClass(hProcess: win32more.Foundation.HANDLE) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def SetThreadStackGuarantee(StackSizeInBytes: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetProcessId(Process: win32more.Foundation.HANDLE) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetThreadId(Thread: win32more.Foundation.HANDLE) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def FlushProcessWriteBuffers() -> Void: ...
@winfunctype('KERNEL32.dll')
def GetProcessIdOfThread(Thread: win32more.Foundation.HANDLE) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def InitializeProcThreadAttributeList(lpAttributeList: win32more.System.Threading.LPPROC_THREAD_ATTRIBUTE_LIST, dwAttributeCount: UInt32, dwFlags: UInt32, lpSize: POINTER(UIntPtr)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DeleteProcThreadAttributeList(lpAttributeList: win32more.System.Threading.LPPROC_THREAD_ATTRIBUTE_LIST) -> Void: ...
@winfunctype('KERNEL32.dll')
def UpdateProcThreadAttribute(lpAttributeList: win32more.System.Threading.LPPROC_THREAD_ATTRIBUTE_LIST, dwFlags: UInt32, Attribute: UIntPtr, lpValue: c_void_p, cbSize: UIntPtr, lpPreviousValue: c_void_p, lpReturnSize: POINTER(UIntPtr)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetProcessDynamicEHContinuationTargets(Process: win32more.Foundation.HANDLE, NumberOfTargets: UInt16, Targets: POINTER(win32more.System.Threading.PROCESS_DYNAMIC_EH_CONTINUATION_TARGET_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetProcessDynamicEnforcedCetCompatibleRanges(Process: win32more.Foundation.HANDLE, NumberOfRanges: UInt16, Ranges: POINTER(win32more.System.Threading.PROCESS_DYNAMIC_ENFORCED_ADDRESS_RANGE_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetProcessAffinityUpdateMode(hProcess: win32more.Foundation.HANDLE, dwFlags: win32more.System.Threading.PROCESS_AFFINITY_AUTO_UPDATE_FLAGS) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def QueryProcessAffinityUpdateMode(hProcess: win32more.Foundation.HANDLE, lpdwFlags: POINTER(win32more.System.Threading.PROCESS_AFFINITY_AUTO_UPDATE_FLAGS)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateRemoteThreadEx(hProcess: win32more.Foundation.HANDLE, lpThreadAttributes: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), dwStackSize: UIntPtr, lpStartAddress: win32more.System.Threading.LPTHREAD_START_ROUTINE, lpParameter: c_void_p, dwCreationFlags: UInt32, lpAttributeList: win32more.System.Threading.LPPROC_THREAD_ATTRIBUTE_LIST, lpThreadId: POINTER(UInt32)) -> win32more.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def GetCurrentThreadStackLimits(LowLimit: POINTER(UIntPtr), HighLimit: POINTER(UIntPtr)) -> Void: ...
@winfunctype('KERNEL32.dll')
def GetProcessMitigationPolicy(hProcess: win32more.Foundation.HANDLE, MitigationPolicy: win32more.System.Threading.PROCESS_MITIGATION_POLICY, lpBuffer: c_void_p, dwLength: UIntPtr) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetProcessMitigationPolicy(MitigationPolicy: win32more.System.Threading.PROCESS_MITIGATION_POLICY, lpBuffer: c_void_p, dwLength: UIntPtr) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetThreadTimes(hThread: win32more.Foundation.HANDLE, lpCreationTime: POINTER(win32more.Foundation.FILETIME_head), lpExitTime: POINTER(win32more.Foundation.FILETIME_head), lpKernelTime: POINTER(win32more.Foundation.FILETIME_head), lpUserTime: POINTER(win32more.Foundation.FILETIME_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def OpenProcess(dwDesiredAccess: win32more.System.Threading.PROCESS_ACCESS_RIGHTS, bInheritHandle: win32more.Foundation.BOOL, dwProcessId: UInt32) -> win32more.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def IsProcessorFeaturePresent(ProcessorFeature: win32more.System.Threading.PROCESSOR_FEATURE_ID) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetProcessHandleCount(hProcess: win32more.Foundation.HANDLE, pdwHandleCount: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetCurrentProcessorNumber() -> UInt32: ...
@winfunctype('KERNEL32.dll')
def SetThreadIdealProcessorEx(hThread: win32more.Foundation.HANDLE, lpIdealProcessor: POINTER(win32more.System.Kernel.PROCESSOR_NUMBER_head), lpPreviousIdealProcessor: POINTER(win32more.System.Kernel.PROCESSOR_NUMBER_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetThreadIdealProcessorEx(hThread: win32more.Foundation.HANDLE, lpIdealProcessor: POINTER(win32more.System.Kernel.PROCESSOR_NUMBER_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetCurrentProcessorNumberEx(ProcNumber: POINTER(win32more.System.Kernel.PROCESSOR_NUMBER_head)) -> Void: ...
@winfunctype('KERNEL32.dll')
def GetProcessPriorityBoost(hProcess: win32more.Foundation.HANDLE, pDisablePriorityBoost: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetProcessPriorityBoost(hProcess: win32more.Foundation.HANDLE, bDisablePriorityBoost: win32more.Foundation.BOOL) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetThreadIOPendingFlag(hThread: win32more.Foundation.HANDLE, lpIOIsPending: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetSystemTimes(lpIdleTime: POINTER(win32more.Foundation.FILETIME_head), lpKernelTime: POINTER(win32more.Foundation.FILETIME_head), lpUserTime: POINTER(win32more.Foundation.FILETIME_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetThreadInformation(hThread: win32more.Foundation.HANDLE, ThreadInformationClass: win32more.System.Threading.THREAD_INFORMATION_CLASS, ThreadInformation: c_void_p, ThreadInformationSize: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetThreadInformation(hThread: win32more.Foundation.HANDLE, ThreadInformationClass: win32more.System.Threading.THREAD_INFORMATION_CLASS, ThreadInformation: c_void_p, ThreadInformationSize: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def IsProcessCritical(hProcess: win32more.Foundation.HANDLE, Critical: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetProtectedPolicy(PolicyGuid: POINTER(Guid), PolicyValue: UIntPtr, OldPolicyValue: POINTER(UIntPtr)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def QueryProtectedPolicy(PolicyGuid: POINTER(Guid), PolicyValue: POINTER(UIntPtr)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetThreadIdealProcessor(hThread: win32more.Foundation.HANDLE, dwIdealProcessor: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def SetProcessInformation(hProcess: win32more.Foundation.HANDLE, ProcessInformationClass: win32more.System.Threading.PROCESS_INFORMATION_CLASS, ProcessInformation: c_void_p, ProcessInformationSize: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetProcessInformation(hProcess: win32more.Foundation.HANDLE, ProcessInformationClass: win32more.System.Threading.PROCESS_INFORMATION_CLASS, ProcessInformation: c_void_p, ProcessInformationSize: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetProcessDefaultCpuSets(Process: win32more.Foundation.HANDLE, CpuSetIds: POINTER(UInt32), CpuSetIdCount: UInt32, RequiredIdCount: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetProcessDefaultCpuSets(Process: win32more.Foundation.HANDLE, CpuSetIds: POINTER(UInt32), CpuSetIdCount: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetThreadSelectedCpuSets(Thread: win32more.Foundation.HANDLE, CpuSetIds: POINTER(UInt32), CpuSetIdCount: UInt32, RequiredIdCount: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetThreadSelectedCpuSets(Thread: win32more.Foundation.HANDLE, CpuSetIds: POINTER(UInt32), CpuSetIdCount: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CreateProcessAsUserA(hToken: win32more.Foundation.HANDLE, lpApplicationName: win32more.Foundation.PSTR, lpCommandLine: win32more.Foundation.PSTR, lpProcessAttributes: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), lpThreadAttributes: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), bInheritHandles: win32more.Foundation.BOOL, dwCreationFlags: win32more.System.Threading.PROCESS_CREATION_FLAGS, lpEnvironment: c_void_p, lpCurrentDirectory: win32more.Foundation.PSTR, lpStartupInfo: POINTER(win32more.System.Threading.STARTUPINFOA_head), lpProcessInformation: POINTER(win32more.System.Threading.PROCESS_INFORMATION_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetProcessShutdownParameters(lpdwLevel: POINTER(UInt32), lpdwFlags: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetProcessDefaultCpuSetMasks(Process: win32more.Foundation.HANDLE, CpuSetMasks: POINTER(win32more.System.SystemInformation.GROUP_AFFINITY_head), CpuSetMaskCount: UInt16, RequiredMaskCount: POINTER(UInt16)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetProcessDefaultCpuSetMasks(Process: win32more.Foundation.HANDLE, CpuSetMasks: POINTER(win32more.System.SystemInformation.GROUP_AFFINITY_head), CpuSetMaskCount: UInt16) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetThreadSelectedCpuSetMasks(Thread: win32more.Foundation.HANDLE, CpuSetMasks: POINTER(win32more.System.SystemInformation.GROUP_AFFINITY_head), CpuSetMaskCount: UInt16, RequiredMaskCount: POINTER(UInt16)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetThreadSelectedCpuSetMasks(Thread: win32more.Foundation.HANDLE, CpuSetMasks: POINTER(win32more.System.SystemInformation.GROUP_AFFINITY_head), CpuSetMaskCount: UInt16) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetMachineTypeAttributes(Machine: UInt16, MachineTypeAttributes: POINTER(win32more.System.Threading.MACHINE_ATTRIBUTES)) -> win32more.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def SetThreadDescription(hThread: win32more.Foundation.HANDLE, lpThreadDescription: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def GetThreadDescription(hThread: win32more.Foundation.HANDLE, ppszThreadDescription: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def QueueUserWorkItem(Function: win32more.System.Threading.LPTHREAD_START_ROUTINE, Context: c_void_p, Flags: win32more.System.Threading.WORKER_THREAD_FLAGS) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def UnregisterWaitEx(WaitHandle: win32more.Foundation.HANDLE, CompletionEvent: win32more.Foundation.HANDLE) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateTimerQueue() -> win32more.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def CreateTimerQueueTimer(phNewTimer: POINTER(win32more.Foundation.HANDLE), TimerQueue: win32more.Foundation.HANDLE, Callback: win32more.System.Threading.WAITORTIMERCALLBACK, Parameter: c_void_p, DueTime: UInt32, Period: UInt32, Flags: win32more.System.Threading.WORKER_THREAD_FLAGS) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ChangeTimerQueueTimer(TimerQueue: win32more.Foundation.HANDLE, Timer: win32more.Foundation.HANDLE, DueTime: UInt32, Period: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DeleteTimerQueueTimer(TimerQueue: win32more.Foundation.HANDLE, Timer: win32more.Foundation.HANDLE, CompletionEvent: win32more.Foundation.HANDLE) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DeleteTimerQueue(TimerQueue: win32more.Foundation.HANDLE) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DeleteTimerQueueEx(TimerQueue: win32more.Foundation.HANDLE, CompletionEvent: win32more.Foundation.HANDLE) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateThreadpool(reserved: c_void_p) -> win32more.System.Threading.PTP_POOL: ...
@winfunctype('KERNEL32.dll')
def SetThreadpoolThreadMaximum(ptpp: win32more.System.Threading.PTP_POOL, cthrdMost: UInt32) -> Void: ...
@winfunctype('KERNEL32.dll')
def SetThreadpoolThreadMinimum(ptpp: win32more.System.Threading.PTP_POOL, cthrdMic: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetThreadpoolStackInformation(ptpp: win32more.System.Threading.PTP_POOL, ptpsi: POINTER(win32more.System.Threading.TP_POOL_STACK_INFORMATION_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def QueryThreadpoolStackInformation(ptpp: win32more.System.Threading.PTP_POOL, ptpsi: POINTER(win32more.System.Threading.TP_POOL_STACK_INFORMATION_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CloseThreadpool(ptpp: win32more.System.Threading.PTP_POOL) -> Void: ...
@winfunctype('KERNEL32.dll')
def CreateThreadpoolCleanupGroup() -> IntPtr: ...
@winfunctype('KERNEL32.dll')
def CloseThreadpoolCleanupGroupMembers(ptpcg: IntPtr, fCancelPendingCallbacks: win32more.Foundation.BOOL, pvCleanupContext: c_void_p) -> Void: ...
@winfunctype('KERNEL32.dll')
def CloseThreadpoolCleanupGroup(ptpcg: IntPtr) -> Void: ...
@winfunctype('KERNEL32.dll')
def SetEventWhenCallbackReturns(pci: POINTER(win32more.System.Threading.TP_CALLBACK_INSTANCE_head), evt: win32more.Foundation.HANDLE) -> Void: ...
@winfunctype('KERNEL32.dll')
def ReleaseSemaphoreWhenCallbackReturns(pci: POINTER(win32more.System.Threading.TP_CALLBACK_INSTANCE_head), sem: win32more.Foundation.HANDLE, crel: UInt32) -> Void: ...
@winfunctype('KERNEL32.dll')
def ReleaseMutexWhenCallbackReturns(pci: POINTER(win32more.System.Threading.TP_CALLBACK_INSTANCE_head), mut: win32more.Foundation.HANDLE) -> Void: ...
@winfunctype('KERNEL32.dll')
def LeaveCriticalSectionWhenCallbackReturns(pci: POINTER(win32more.System.Threading.TP_CALLBACK_INSTANCE_head), pcs: POINTER(win32more.System.Threading.RTL_CRITICAL_SECTION_head)) -> Void: ...
@winfunctype('KERNEL32.dll')
def FreeLibraryWhenCallbackReturns(pci: POINTER(win32more.System.Threading.TP_CALLBACK_INSTANCE_head), mod: win32more.Foundation.HINSTANCE) -> Void: ...
@winfunctype('KERNEL32.dll')
def CallbackMayRunLong(pci: POINTER(win32more.System.Threading.TP_CALLBACK_INSTANCE_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DisassociateCurrentThreadFromCallback(pci: POINTER(win32more.System.Threading.TP_CALLBACK_INSTANCE_head)) -> Void: ...
@winfunctype('KERNEL32.dll')
def TrySubmitThreadpoolCallback(pfns: win32more.System.Threading.PTP_SIMPLE_CALLBACK, pv: c_void_p, pcbe: POINTER(win32more.System.Threading.TP_CALLBACK_ENVIRON_V3_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateThreadpoolWork(pfnwk: win32more.System.Threading.PTP_WORK_CALLBACK, pv: c_void_p, pcbe: POINTER(win32more.System.Threading.TP_CALLBACK_ENVIRON_V3_head)) -> POINTER(win32more.System.Threading.TP_WORK_head): ...
@winfunctype('KERNEL32.dll')
def SubmitThreadpoolWork(pwk: POINTER(win32more.System.Threading.TP_WORK_head)) -> Void: ...
@winfunctype('KERNEL32.dll')
def WaitForThreadpoolWorkCallbacks(pwk: POINTER(win32more.System.Threading.TP_WORK_head), fCancelPendingCallbacks: win32more.Foundation.BOOL) -> Void: ...
@winfunctype('KERNEL32.dll')
def CloseThreadpoolWork(pwk: POINTER(win32more.System.Threading.TP_WORK_head)) -> Void: ...
@winfunctype('KERNEL32.dll')
def CreateThreadpoolTimer(pfnti: win32more.System.Threading.PTP_TIMER_CALLBACK, pv: c_void_p, pcbe: POINTER(win32more.System.Threading.TP_CALLBACK_ENVIRON_V3_head)) -> POINTER(win32more.System.Threading.TP_TIMER_head): ...
@winfunctype('KERNEL32.dll')
def SetThreadpoolTimer(pti: POINTER(win32more.System.Threading.TP_TIMER_head), pftDueTime: POINTER(win32more.Foundation.FILETIME_head), msPeriod: UInt32, msWindowLength: UInt32) -> Void: ...
@winfunctype('KERNEL32.dll')
def IsThreadpoolTimerSet(pti: POINTER(win32more.System.Threading.TP_TIMER_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WaitForThreadpoolTimerCallbacks(pti: POINTER(win32more.System.Threading.TP_TIMER_head), fCancelPendingCallbacks: win32more.Foundation.BOOL) -> Void: ...
@winfunctype('KERNEL32.dll')
def CloseThreadpoolTimer(pti: POINTER(win32more.System.Threading.TP_TIMER_head)) -> Void: ...
@winfunctype('KERNEL32.dll')
def CreateThreadpoolWait(pfnwa: win32more.System.Threading.PTP_WAIT_CALLBACK, pv: c_void_p, pcbe: POINTER(win32more.System.Threading.TP_CALLBACK_ENVIRON_V3_head)) -> POINTER(win32more.System.Threading.TP_WAIT_head): ...
@winfunctype('KERNEL32.dll')
def SetThreadpoolWait(pwa: POINTER(win32more.System.Threading.TP_WAIT_head), h: win32more.Foundation.HANDLE, pftTimeout: POINTER(win32more.Foundation.FILETIME_head)) -> Void: ...
@winfunctype('KERNEL32.dll')
def WaitForThreadpoolWaitCallbacks(pwa: POINTER(win32more.System.Threading.TP_WAIT_head), fCancelPendingCallbacks: win32more.Foundation.BOOL) -> Void: ...
@winfunctype('KERNEL32.dll')
def CloseThreadpoolWait(pwa: POINTER(win32more.System.Threading.TP_WAIT_head)) -> Void: ...
@winfunctype('KERNEL32.dll')
def CreateThreadpoolIo(fl: win32more.Foundation.HANDLE, pfnio: win32more.System.Threading.PTP_WIN32_IO_CALLBACK, pv: c_void_p, pcbe: POINTER(win32more.System.Threading.TP_CALLBACK_ENVIRON_V3_head)) -> POINTER(win32more.System.Threading.TP_IO_head): ...
@winfunctype('KERNEL32.dll')
def StartThreadpoolIo(pio: POINTER(win32more.System.Threading.TP_IO_head)) -> Void: ...
@winfunctype('KERNEL32.dll')
def CancelThreadpoolIo(pio: POINTER(win32more.System.Threading.TP_IO_head)) -> Void: ...
@winfunctype('KERNEL32.dll')
def WaitForThreadpoolIoCallbacks(pio: POINTER(win32more.System.Threading.TP_IO_head), fCancelPendingCallbacks: win32more.Foundation.BOOL) -> Void: ...
@winfunctype('KERNEL32.dll')
def CloseThreadpoolIo(pio: POINTER(win32more.System.Threading.TP_IO_head)) -> Void: ...
@winfunctype('KERNEL32.dll')
def SetThreadpoolTimerEx(pti: POINTER(win32more.System.Threading.TP_TIMER_head), pftDueTime: POINTER(win32more.Foundation.FILETIME_head), msPeriod: UInt32, msWindowLength: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetThreadpoolWaitEx(pwa: POINTER(win32more.System.Threading.TP_WAIT_head), h: win32more.Foundation.HANDLE, pftTimeout: POINTER(win32more.Foundation.FILETIME_head), Reserved: c_void_p) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def IsWow64Process(hProcess: win32more.Foundation.HANDLE, Wow64Process: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-wow64-l1-1-1.dll')
def Wow64SetThreadDefaultGuestMachine(Machine: UInt16) -> UInt16: ...
@winfunctype('KERNEL32.dll')
def IsWow64Process2(hProcess: win32more.Foundation.HANDLE, pProcessMachine: POINTER(win32more.System.SystemInformation.IMAGE_FILE_MACHINE), pNativeMachine: POINTER(win32more.System.SystemInformation.IMAGE_FILE_MACHINE)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def Wow64SuspendThread(hThread: win32more.Foundation.HANDLE) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def CreatePrivateNamespaceW(lpPrivateNamespaceAttributes: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), lpBoundaryDescriptor: c_void_p, lpAliasPrefix: win32more.Foundation.PWSTR) -> win32more.System.Threading.NamespaceHandle: ...
@winfunctype('KERNEL32.dll')
def OpenPrivateNamespaceW(lpBoundaryDescriptor: c_void_p, lpAliasPrefix: win32more.Foundation.PWSTR) -> win32more.System.Threading.NamespaceHandle: ...
@winfunctype('KERNEL32.dll')
def ClosePrivateNamespace(Handle: win32more.System.Threading.NamespaceHandle, Flags: UInt32) -> win32more.Foundation.BOOLEAN: ...
@winfunctype('KERNEL32.dll')
def CreateBoundaryDescriptorW(Name: win32more.Foundation.PWSTR, Flags: UInt32) -> win32more.System.Threading.BoundaryDescriptorHandle: ...
@winfunctype('KERNEL32.dll')
def AddSIDToBoundaryDescriptor(BoundaryDescriptor: POINTER(win32more.Foundation.HANDLE), RequiredSid: win32more.Foundation.PSID) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DeleteBoundaryDescriptor(BoundaryDescriptor: win32more.System.Threading.BoundaryDescriptorHandle) -> Void: ...
@winfunctype('KERNEL32.dll')
def GetNumaHighestNodeNumber(HighestNodeNumber: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetNumaNodeProcessorMaskEx(Node: UInt16, ProcessorMask: POINTER(win32more.System.SystemInformation.GROUP_AFFINITY_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetNumaNodeProcessorMask2(NodeNumber: UInt16, ProcessorMasks: POINTER(win32more.System.SystemInformation.GROUP_AFFINITY_head), ProcessorMaskCount: UInt16, RequiredMaskCount: POINTER(UInt16)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetNumaProximityNodeEx(ProximityId: UInt32, NodeNumber: POINTER(UInt16)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetProcessGroupAffinity(hProcess: win32more.Foundation.HANDLE, GroupCount: POINTER(UInt16), GroupArray: POINTER(UInt16)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetThreadGroupAffinity(hThread: win32more.Foundation.HANDLE, GroupAffinity: POINTER(win32more.System.SystemInformation.GROUP_AFFINITY_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetThreadGroupAffinity(hThread: win32more.Foundation.HANDLE, GroupAffinity: POINTER(win32more.System.SystemInformation.GROUP_AFFINITY_head), PreviousGroupAffinity: POINTER(win32more.System.SystemInformation.GROUP_AFFINITY_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('AVRT.dll')
def AvSetMmThreadCharacteristicsA(TaskName: win32more.Foundation.PSTR, TaskIndex: POINTER(UInt32)) -> win32more.Foundation.HANDLE: ...
@winfunctype('AVRT.dll')
def AvSetMmThreadCharacteristicsW(TaskName: win32more.Foundation.PWSTR, TaskIndex: POINTER(UInt32)) -> win32more.Foundation.HANDLE: ...
@winfunctype('AVRT.dll')
def AvSetMmMaxThreadCharacteristicsA(FirstTask: win32more.Foundation.PSTR, SecondTask: win32more.Foundation.PSTR, TaskIndex: POINTER(UInt32)) -> win32more.Foundation.HANDLE: ...
@winfunctype('AVRT.dll')
def AvSetMmMaxThreadCharacteristicsW(FirstTask: win32more.Foundation.PWSTR, SecondTask: win32more.Foundation.PWSTR, TaskIndex: POINTER(UInt32)) -> win32more.Foundation.HANDLE: ...
@winfunctype('AVRT.dll')
def AvRevertMmThreadCharacteristics(AvrtHandle: win32more.Foundation.HANDLE) -> win32more.Foundation.BOOL: ...
@winfunctype('AVRT.dll')
def AvSetMmThreadPriority(AvrtHandle: win32more.Foundation.HANDLE, Priority: win32more.System.Threading.AVRT_PRIORITY) -> win32more.Foundation.BOOL: ...
@winfunctype('AVRT.dll')
def AvRtCreateThreadOrderingGroup(Context: POINTER(win32more.Foundation.HANDLE), Period: POINTER(win32more.Foundation.LARGE_INTEGER_head), ThreadOrderingGuid: POINTER(Guid), Timeout: POINTER(win32more.Foundation.LARGE_INTEGER_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('AVRT.dll')
def AvRtCreateThreadOrderingGroupExA(Context: POINTER(win32more.Foundation.HANDLE), Period: POINTER(win32more.Foundation.LARGE_INTEGER_head), ThreadOrderingGuid: POINTER(Guid), Timeout: POINTER(win32more.Foundation.LARGE_INTEGER_head), TaskName: win32more.Foundation.PSTR) -> win32more.Foundation.BOOL: ...
@winfunctype('AVRT.dll')
def AvRtCreateThreadOrderingGroupExW(Context: POINTER(win32more.Foundation.HANDLE), Period: POINTER(win32more.Foundation.LARGE_INTEGER_head), ThreadOrderingGuid: POINTER(Guid), Timeout: POINTER(win32more.Foundation.LARGE_INTEGER_head), TaskName: win32more.Foundation.PWSTR) -> win32more.Foundation.BOOL: ...
@winfunctype('AVRT.dll')
def AvRtJoinThreadOrderingGroup(Context: POINTER(win32more.Foundation.HANDLE), ThreadOrderingGuid: POINTER(Guid), Before: win32more.Foundation.BOOL) -> win32more.Foundation.BOOL: ...
@winfunctype('AVRT.dll')
def AvRtWaitOnThreadOrderingGroup(Context: win32more.Foundation.HANDLE) -> win32more.Foundation.BOOL: ...
@winfunctype('AVRT.dll')
def AvRtLeaveThreadOrderingGroup(Context: win32more.Foundation.HANDLE) -> win32more.Foundation.BOOL: ...
@winfunctype('AVRT.dll')
def AvRtDeleteThreadOrderingGroup(Context: win32more.Foundation.HANDLE) -> win32more.Foundation.BOOL: ...
@winfunctype('AVRT.dll')
def AvQuerySystemResponsiveness(AvrtHandle: win32more.Foundation.HANDLE, SystemResponsivenessValue: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def AttachThreadInput(idAttach: UInt32, idAttachTo: UInt32, fAttach: win32more.Foundation.BOOL) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def WaitForInputIdle(hProcess: win32more.Foundation.HANDLE, dwMilliseconds: UInt32) -> UInt32: ...
@winfunctype('USER32.dll')
def GetGuiResources(hProcess: win32more.Foundation.HANDLE, uiFlags: win32more.System.Threading.GET_GUI_RESOURCES_FLAGS) -> UInt32: ...
@winfunctype('USER32.dll')
def IsImmersiveProcess(hProcess: win32more.Foundation.HANDLE) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def SetProcessRestrictionExemption(fEnableExemption: win32more.Foundation.BOOL) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetProcessAffinityMask(hProcess: win32more.Foundation.HANDLE, lpProcessAffinityMask: POINTER(UIntPtr), lpSystemAffinityMask: POINTER(UIntPtr)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetProcessAffinityMask(hProcess: win32more.Foundation.HANDLE, dwProcessAffinityMask: UIntPtr) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetProcessIoCounters(hProcess: win32more.Foundation.HANDLE, lpIoCounters: POINTER(win32more.System.Threading.IO_COUNTERS_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SwitchToFiber(lpFiber: c_void_p) -> Void: ...
@winfunctype('KERNEL32.dll')
def DeleteFiber(lpFiber: c_void_p) -> Void: ...
@winfunctype('KERNEL32.dll')
def ConvertFiberToThread() -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateFiberEx(dwStackCommitSize: UIntPtr, dwStackReserveSize: UIntPtr, dwFlags: UInt32, lpStartAddress: win32more.System.Threading.LPFIBER_START_ROUTINE, lpParameter: c_void_p) -> c_void_p: ...
@winfunctype('KERNEL32.dll')
def ConvertThreadToFiberEx(lpParameter: c_void_p, dwFlags: UInt32) -> c_void_p: ...
@winfunctype('KERNEL32.dll')
def CreateFiber(dwStackSize: UIntPtr, lpStartAddress: win32more.System.Threading.LPFIBER_START_ROUTINE, lpParameter: c_void_p) -> c_void_p: ...
@winfunctype('KERNEL32.dll')
def ConvertThreadToFiber(lpParameter: c_void_p) -> c_void_p: ...
@winfunctype('KERNEL32.dll')
def CreateUmsCompletionList(UmsCompletionList: POINTER(c_void_p)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DequeueUmsCompletionListItems(UmsCompletionList: c_void_p, WaitTimeOut: UInt32, UmsThreadList: POINTER(c_void_p)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetUmsCompletionListEvent(UmsCompletionList: c_void_p, UmsCompletionEvent: POINTER(win32more.Foundation.HANDLE)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ExecuteUmsThread(UmsThread: c_void_p) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def UmsThreadYield(SchedulerParam: c_void_p) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DeleteUmsCompletionList(UmsCompletionList: c_void_p) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetCurrentUmsThread() -> c_void_p: ...
@winfunctype('KERNEL32.dll')
def GetNextUmsListItem(UmsContext: c_void_p) -> c_void_p: ...
@winfunctype('KERNEL32.dll')
def QueryUmsThreadInformation(UmsThread: c_void_p, UmsThreadInfoClass: win32more.System.Threading.RTL_UMS_THREAD_INFO_CLASS, UmsThreadInformation: c_void_p, UmsThreadInformationLength: UInt32, ReturnLength: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetUmsThreadInformation(UmsThread: c_void_p, UmsThreadInfoClass: win32more.System.Threading.RTL_UMS_THREAD_INFO_CLASS, UmsThreadInformation: c_void_p, UmsThreadInformationLength: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DeleteUmsThreadContext(UmsThread: c_void_p) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateUmsThreadContext(lpUmsThread: POINTER(c_void_p)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def EnterUmsSchedulingMode(SchedulerStartupInfo: POINTER(win32more.System.Threading.UMS_SCHEDULER_STARTUP_INFO_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetUmsSystemThreadInformation(ThreadHandle: win32more.Foundation.HANDLE, SystemThreadInfo: POINTER(win32more.System.Threading.UMS_SYSTEM_THREAD_INFORMATION_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetThreadAffinityMask(hThread: win32more.Foundation.HANDLE, dwThreadAffinityMask: UIntPtr) -> UIntPtr: ...
@winfunctype('KERNEL32.dll')
def SetProcessDEPPolicy(dwFlags: win32more.System.Threading.PROCESS_DEP_FLAGS) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetProcessDEPPolicy(hProcess: win32more.Foundation.HANDLE, lpFlags: POINTER(UInt32), lpPermanent: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def PulseEvent(hEvent: win32more.Foundation.HANDLE) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WinExec(lpCmdLine: win32more.Foundation.PSTR, uCmdShow: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def CreateSemaphoreA(lpSemaphoreAttributes: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), lInitialCount: Int32, lMaximumCount: Int32, lpName: win32more.Foundation.PSTR) -> win32more.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def CreateSemaphoreExA(lpSemaphoreAttributes: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), lInitialCount: Int32, lMaximumCount: Int32, lpName: win32more.Foundation.PSTR, dwFlags: UInt32, dwDesiredAccess: UInt32) -> win32more.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def QueryFullProcessImageNameA(hProcess: win32more.Foundation.HANDLE, dwFlags: win32more.System.Threading.PROCESS_NAME_FORMAT, lpExeName: win32more.Foundation.PSTR, lpdwSize: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def QueryFullProcessImageNameW(hProcess: win32more.Foundation.HANDLE, dwFlags: win32more.System.Threading.PROCESS_NAME_FORMAT, lpExeName: win32more.Foundation.PWSTR, lpdwSize: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetStartupInfoA(lpStartupInfo: POINTER(win32more.System.Threading.STARTUPINFOA_head)) -> Void: ...
@winfunctype('ADVAPI32.dll')
def CreateProcessWithLogonW(lpUsername: win32more.Foundation.PWSTR, lpDomain: win32more.Foundation.PWSTR, lpPassword: win32more.Foundation.PWSTR, dwLogonFlags: win32more.System.Threading.CREATE_PROCESS_LOGON_FLAGS, lpApplicationName: win32more.Foundation.PWSTR, lpCommandLine: win32more.Foundation.PWSTR, dwCreationFlags: win32more.System.Threading.PROCESS_CREATION_FLAGS, lpEnvironment: c_void_p, lpCurrentDirectory: win32more.Foundation.PWSTR, lpStartupInfo: POINTER(win32more.System.Threading.STARTUPINFOW_head), lpProcessInformation: POINTER(win32more.System.Threading.PROCESS_INFORMATION_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CreateProcessWithTokenW(hToken: win32more.Foundation.HANDLE, dwLogonFlags: win32more.System.Threading.CREATE_PROCESS_LOGON_FLAGS, lpApplicationName: win32more.Foundation.PWSTR, lpCommandLine: win32more.Foundation.PWSTR, dwCreationFlags: win32more.System.Threading.PROCESS_CREATION_FLAGS, lpEnvironment: c_void_p, lpCurrentDirectory: win32more.Foundation.PWSTR, lpStartupInfo: POINTER(win32more.System.Threading.STARTUPINFOW_head), lpProcessInformation: POINTER(win32more.System.Threading.PROCESS_INFORMATION_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def RegisterWaitForSingleObject(phNewWaitObject: POINTER(win32more.Foundation.HANDLE), hObject: win32more.Foundation.HANDLE, Callback: win32more.System.Threading.WAITORTIMERCALLBACK, Context: c_void_p, dwMilliseconds: UInt32, dwFlags: win32more.System.Threading.WORKER_THREAD_FLAGS) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def UnregisterWait(WaitHandle: win32more.Foundation.HANDLE) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetTimerQueueTimer(TimerQueue: win32more.Foundation.HANDLE, Callback: win32more.System.Threading.WAITORTIMERCALLBACK, Parameter: c_void_p, DueTime: UInt32, Period: UInt32, PreferIo: win32more.Foundation.BOOL) -> win32more.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def CreatePrivateNamespaceA(lpPrivateNamespaceAttributes: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), lpBoundaryDescriptor: c_void_p, lpAliasPrefix: win32more.Foundation.PSTR) -> win32more.System.Threading.NamespaceHandle: ...
@winfunctype('KERNEL32.dll')
def OpenPrivateNamespaceA(lpBoundaryDescriptor: c_void_p, lpAliasPrefix: win32more.Foundation.PSTR) -> win32more.System.Threading.NamespaceHandle: ...
@winfunctype('KERNEL32.dll')
def CreateBoundaryDescriptorA(Name: win32more.Foundation.PSTR, Flags: UInt32) -> win32more.System.Threading.BoundaryDescriptorHandle: ...
@winfunctype('KERNEL32.dll')
def AddIntegrityLabelToBoundaryDescriptor(BoundaryDescriptor: POINTER(win32more.Foundation.HANDLE), IntegrityLabel: win32more.Foundation.PSID) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetActiveProcessorGroupCount() -> UInt16: ...
@winfunctype('KERNEL32.dll')
def GetMaximumProcessorGroupCount() -> UInt16: ...
@winfunctype('KERNEL32.dll')
def GetActiveProcessorCount(GroupNumber: UInt16) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetMaximumProcessorCount(GroupNumber: UInt16) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetNumaProcessorNode(Processor: Byte, NodeNumber: c_char_p_no) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetNumaNodeNumberFromHandle(hFile: win32more.Foundation.HANDLE, NodeNumber: POINTER(UInt16)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetNumaProcessorNodeEx(Processor: POINTER(win32more.System.Kernel.PROCESSOR_NUMBER_head), NodeNumber: POINTER(UInt16)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetNumaNodeProcessorMask(Node: Byte, ProcessorMask: POINTER(UInt64)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetNumaAvailableMemoryNode(Node: Byte, AvailableBytes: POINTER(UInt64)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetNumaAvailableMemoryNodeEx(Node: UInt16, AvailableBytes: POINTER(UInt64)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetNumaProximityNode(ProximityId: UInt32, NodeNumber: c_char_p_no) -> win32more.Foundation.BOOL: ...
@winfunctype('ntdll.dll')
def NtQueryInformationProcess(ProcessHandle: win32more.Foundation.HANDLE, ProcessInformationClass: win32more.System.Threading.PROCESSINFOCLASS, ProcessInformation: c_void_p, ProcessInformationLength: UInt32, ReturnLength: POINTER(UInt32)) -> win32more.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtQueryInformationThread(ThreadHandle: win32more.Foundation.HANDLE, ThreadInformationClass: win32more.System.Threading.THREADINFOCLASS, ThreadInformation: c_void_p, ThreadInformationLength: UInt32, ReturnLength: POINTER(UInt32)) -> win32more.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtSetInformationThread(ThreadHandle: win32more.Foundation.HANDLE, ThreadInformationClass: win32more.System.Threading.THREADINFOCLASS, ThreadInformation: c_void_p, ThreadInformationLength: UInt32) -> win32more.Foundation.NTSTATUS: ...
BoundaryDescriptorHandle = IntPtr
CREATE_EVENT = UInt32
CREATE_EVENT_INITIAL_SET: CREATE_EVENT = 2
CREATE_EVENT_MANUAL_RESET: CREATE_EVENT = 1
CREATE_PROCESS_LOGON_FLAGS = UInt32
LOGON_WITH_PROFILE: CREATE_PROCESS_LOGON_FLAGS = 1
LOGON_NETCREDENTIALS_ONLY: CREATE_PROCESS_LOGON_FLAGS = 2
GET_GUI_RESOURCES_FLAGS = UInt32
GR_GDIOBJECTS: GET_GUI_RESOURCES_FLAGS = 0
GR_GDIOBJECTS_PEAK: GET_GUI_RESOURCES_FLAGS = 2
GR_USEROBJECTS: GET_GUI_RESOURCES_FLAGS = 1
GR_USEROBJECTS_PEAK: GET_GUI_RESOURCES_FLAGS = 4
class IO_COUNTERS(Structure):
    ReadOperationCount: UInt64
    WriteOperationCount: UInt64
    OtherOperationCount: UInt64
    ReadTransferCount: UInt64
    WriteTransferCount: UInt64
    OtherTransferCount: UInt64
@winfunctype_pointer
def LPFIBER_START_ROUTINE(lpFiberParameter: c_void_p) -> Void: ...
LPPROC_THREAD_ATTRIBUTE_LIST = c_void_p
@winfunctype_pointer
def LPTHREAD_START_ROUTINE(lpThreadParameter: c_void_p) -> UInt32: ...
MACHINE_ATTRIBUTES = UInt32
MACHINE_ATTRIBUTES_UserEnabled: MACHINE_ATTRIBUTES = 1
MACHINE_ATTRIBUTES_KernelEnabled: MACHINE_ATTRIBUTES = 2
MACHINE_ATTRIBUTES_Wow64Container: MACHINE_ATTRIBUTES = 4
MEMORY_PRIORITY = UInt32
MEMORY_PRIORITY_VERY_LOW: MEMORY_PRIORITY = 1
MEMORY_PRIORITY_LOW: MEMORY_PRIORITY = 2
MEMORY_PRIORITY_MEDIUM: MEMORY_PRIORITY = 3
MEMORY_PRIORITY_BELOW_NORMAL: MEMORY_PRIORITY = 4
MEMORY_PRIORITY_NORMAL: MEMORY_PRIORITY = 5
class MEMORY_PRIORITY_INFORMATION(Structure):
    MemoryPriority: win32more.System.Threading.MEMORY_PRIORITY
NamespaceHandle = IntPtr
class PEB(Structure):
    Reserved1: Byte * 2
    BeingDebugged: Byte
    Reserved2: Byte * 1
    Reserved3: c_void_p * 2
    Ldr: POINTER(win32more.System.Threading.PEB_LDR_DATA_head)
    ProcessParameters: POINTER(win32more.System.Threading.RTL_USER_PROCESS_PARAMETERS_head)
    Reserved4: c_void_p * 3
    AtlThunkSListPtr: c_void_p
    Reserved5: c_void_p
    Reserved6: UInt32
    Reserved7: c_void_p
    Reserved8: UInt32
    AtlThunkSListPtr32: UInt32
    Reserved9: c_void_p * 45
    Reserved10: Byte * 96
    PostProcessInitRoutine: win32more.System.Threading.PPS_POST_PROCESS_INIT_ROUTINE
    Reserved11: Byte * 128
    Reserved12: c_void_p * 1
    SessionId: UInt32
class PEB_LDR_DATA(Structure):
    Reserved1: Byte * 8
    Reserved2: c_void_p * 3
    InMemoryOrderModuleList: win32more.System.Kernel.LIST_ENTRY
@winfunctype_pointer
def PFLS_CALLBACK_FUNCTION(lpFlsData: c_void_p) -> Void: ...
@winfunctype_pointer
def PINIT_ONCE_FN(InitOnce: POINTER(win32more.System.Threading.RTL_RUN_ONCE_head), Parameter: c_void_p, Context: POINTER(c_void_p)) -> win32more.Foundation.BOOL: ...
POWER_REQUEST_CONTEXT_FLAGS = UInt32
POWER_REQUEST_CONTEXT_DETAILED_STRING: POWER_REQUEST_CONTEXT_FLAGS = 2
POWER_REQUEST_CONTEXT_SIMPLE_STRING: POWER_REQUEST_CONTEXT_FLAGS = 1
@winfunctype_pointer
def PPS_POST_PROCESS_INIT_ROUTINE() -> Void: ...
PROCESSINFOCLASS = Int32
PROCESSINFOCLASS_ProcessBasicInformation: PROCESSINFOCLASS = 0
PROCESSINFOCLASS_ProcessDebugPort: PROCESSINFOCLASS = 7
PROCESSINFOCLASS_ProcessWow64Information: PROCESSINFOCLASS = 26
PROCESSINFOCLASS_ProcessImageFileName: PROCESSINFOCLASS = 27
PROCESSINFOCLASS_ProcessBreakOnTermination: PROCESSINFOCLASS = 29
PROCESSOR_FEATURE_ID = UInt32
PF_ARM_64BIT_LOADSTORE_ATOMIC: PROCESSOR_FEATURE_ID = 25
PF_ARM_DIVIDE_INSTRUCTION_AVAILABLE: PROCESSOR_FEATURE_ID = 24
PF_ARM_EXTERNAL_CACHE_AVAILABLE: PROCESSOR_FEATURE_ID = 26
PF_ARM_FMAC_INSTRUCTIONS_AVAILABLE: PROCESSOR_FEATURE_ID = 27
PF_ARM_VFP_32_REGISTERS_AVAILABLE: PROCESSOR_FEATURE_ID = 18
PF_3DNOW_INSTRUCTIONS_AVAILABLE: PROCESSOR_FEATURE_ID = 7
PF_CHANNELS_ENABLED: PROCESSOR_FEATURE_ID = 16
PF_COMPARE_EXCHANGE_DOUBLE: PROCESSOR_FEATURE_ID = 2
PF_COMPARE_EXCHANGE128: PROCESSOR_FEATURE_ID = 14
PF_COMPARE64_EXCHANGE128: PROCESSOR_FEATURE_ID = 15
PF_FASTFAIL_AVAILABLE: PROCESSOR_FEATURE_ID = 23
PF_FLOATING_POINT_EMULATED: PROCESSOR_FEATURE_ID = 1
PF_FLOATING_POINT_PRECISION_ERRATA: PROCESSOR_FEATURE_ID = 0
PF_MMX_INSTRUCTIONS_AVAILABLE: PROCESSOR_FEATURE_ID = 3
PF_NX_ENABLED: PROCESSOR_FEATURE_ID = 12
PF_PAE_ENABLED: PROCESSOR_FEATURE_ID = 9
PF_RDTSC_INSTRUCTION_AVAILABLE: PROCESSOR_FEATURE_ID = 8
PF_RDWRFSGSBASE_AVAILABLE: PROCESSOR_FEATURE_ID = 22
PF_SECOND_LEVEL_ADDRESS_TRANSLATION: PROCESSOR_FEATURE_ID = 20
PF_SSE3_INSTRUCTIONS_AVAILABLE: PROCESSOR_FEATURE_ID = 13
PF_VIRT_FIRMWARE_ENABLED: PROCESSOR_FEATURE_ID = 21
PF_XMMI_INSTRUCTIONS_AVAILABLE: PROCESSOR_FEATURE_ID = 6
PF_XMMI64_INSTRUCTIONS_AVAILABLE: PROCESSOR_FEATURE_ID = 10
PF_XSAVE_ENABLED: PROCESSOR_FEATURE_ID = 17
PF_ARM_V8_INSTRUCTIONS_AVAILABLE: PROCESSOR_FEATURE_ID = 29
PF_ARM_V8_CRYPTO_INSTRUCTIONS_AVAILABLE: PROCESSOR_FEATURE_ID = 30
PF_ARM_V8_CRC32_INSTRUCTIONS_AVAILABLE: PROCESSOR_FEATURE_ID = 31
PF_ARM_V81_ATOMIC_INSTRUCTIONS_AVAILABLE: PROCESSOR_FEATURE_ID = 34
PROCESS_ACCESS_RIGHTS = UInt32
PROCESS_TERMINATE: PROCESS_ACCESS_RIGHTS = 1
PROCESS_CREATE_THREAD: PROCESS_ACCESS_RIGHTS = 2
PROCESS_SET_SESSIONID: PROCESS_ACCESS_RIGHTS = 4
PROCESS_VM_OPERATION: PROCESS_ACCESS_RIGHTS = 8
PROCESS_VM_READ: PROCESS_ACCESS_RIGHTS = 16
PROCESS_VM_WRITE: PROCESS_ACCESS_RIGHTS = 32
PROCESS_DUP_HANDLE: PROCESS_ACCESS_RIGHTS = 64
PROCESS_CREATE_PROCESS: PROCESS_ACCESS_RIGHTS = 128
PROCESS_SET_QUOTA: PROCESS_ACCESS_RIGHTS = 256
PROCESS_SET_INFORMATION: PROCESS_ACCESS_RIGHTS = 512
PROCESS_QUERY_INFORMATION: PROCESS_ACCESS_RIGHTS = 1024
PROCESS_SUSPEND_RESUME: PROCESS_ACCESS_RIGHTS = 2048
PROCESS_QUERY_LIMITED_INFORMATION: PROCESS_ACCESS_RIGHTS = 4096
PROCESS_SET_LIMITED_INFORMATION: PROCESS_ACCESS_RIGHTS = 8192
PROCESS_ALL_ACCESS: PROCESS_ACCESS_RIGHTS = 2097151
PROCESS_DELETE: PROCESS_ACCESS_RIGHTS = 65536
PROCESS_READ_CONTROL: PROCESS_ACCESS_RIGHTS = 131072
PROCESS_WRITE_DAC: PROCESS_ACCESS_RIGHTS = 262144
PROCESS_WRITE_OWNER: PROCESS_ACCESS_RIGHTS = 524288
PROCESS_SYNCHRONIZE: PROCESS_ACCESS_RIGHTS = 1048576
PROCESS_STANDARD_RIGHTS_REQUIRED: PROCESS_ACCESS_RIGHTS = 983040
PROCESS_AFFINITY_AUTO_UPDATE_FLAGS = UInt32
PROCESS_AFFINITY_DISABLE_AUTO_UPDATE: PROCESS_AFFINITY_AUTO_UPDATE_FLAGS = 0
PROCESS_AFFINITY_ENABLE_AUTO_UPDATE: PROCESS_AFFINITY_AUTO_UPDATE_FLAGS = 1
class PROCESS_BASIC_INFORMATION(Structure):
    Reserved1: c_void_p
    PebBaseAddress: POINTER(win32more.System.Threading.PEB_head)
    Reserved2: c_void_p * 2
    UniqueProcessId: UIntPtr
    Reserved3: c_void_p
PROCESS_CREATION_FLAGS = UInt32
DEBUG_PROCESS: PROCESS_CREATION_FLAGS = 1
DEBUG_ONLY_THIS_PROCESS: PROCESS_CREATION_FLAGS = 2
CREATE_SUSPENDED: PROCESS_CREATION_FLAGS = 4
DETACHED_PROCESS: PROCESS_CREATION_FLAGS = 8
CREATE_NEW_CONSOLE: PROCESS_CREATION_FLAGS = 16
NORMAL_PRIORITY_CLASS: PROCESS_CREATION_FLAGS = 32
IDLE_PRIORITY_CLASS: PROCESS_CREATION_FLAGS = 64
HIGH_PRIORITY_CLASS: PROCESS_CREATION_FLAGS = 128
REALTIME_PRIORITY_CLASS: PROCESS_CREATION_FLAGS = 256
CREATE_NEW_PROCESS_GROUP: PROCESS_CREATION_FLAGS = 512
CREATE_UNICODE_ENVIRONMENT: PROCESS_CREATION_FLAGS = 1024
CREATE_SEPARATE_WOW_VDM: PROCESS_CREATION_FLAGS = 2048
CREATE_SHARED_WOW_VDM: PROCESS_CREATION_FLAGS = 4096
CREATE_FORCEDOS: PROCESS_CREATION_FLAGS = 8192
BELOW_NORMAL_PRIORITY_CLASS: PROCESS_CREATION_FLAGS = 16384
ABOVE_NORMAL_PRIORITY_CLASS: PROCESS_CREATION_FLAGS = 32768
INHERIT_PARENT_AFFINITY: PROCESS_CREATION_FLAGS = 65536
INHERIT_CALLER_PRIORITY: PROCESS_CREATION_FLAGS = 131072
CREATE_PROTECTED_PROCESS: PROCESS_CREATION_FLAGS = 262144
EXTENDED_STARTUPINFO_PRESENT: PROCESS_CREATION_FLAGS = 524288
PROCESS_MODE_BACKGROUND_BEGIN: PROCESS_CREATION_FLAGS = 1048576
PROCESS_MODE_BACKGROUND_END: PROCESS_CREATION_FLAGS = 2097152
CREATE_SECURE_PROCESS: PROCESS_CREATION_FLAGS = 4194304
CREATE_BREAKAWAY_FROM_JOB: PROCESS_CREATION_FLAGS = 16777216
CREATE_PRESERVE_CODE_AUTHZ_LEVEL: PROCESS_CREATION_FLAGS = 33554432
CREATE_DEFAULT_ERROR_MODE: PROCESS_CREATION_FLAGS = 67108864
CREATE_NO_WINDOW: PROCESS_CREATION_FLAGS = 134217728
PROFILE_USER: PROCESS_CREATION_FLAGS = 268435456
PROFILE_KERNEL: PROCESS_CREATION_FLAGS = 536870912
PROFILE_SERVER: PROCESS_CREATION_FLAGS = 1073741824
CREATE_IGNORE_SYSTEM_DEFAULT: PROCESS_CREATION_FLAGS = 2147483648
PROCESS_DEP_FLAGS = UInt32
PROCESS_DEP_ENABLE: PROCESS_DEP_FLAGS = 1
PROCESS_DEP_DISABLE_ATL_THUNK_EMULATION: PROCESS_DEP_FLAGS = 2
PROCESS_DEP_NONE: PROCESS_DEP_FLAGS = 0
class PROCESS_DYNAMIC_EH_CONTINUATION_TARGET(Structure):
    TargetAddress: UIntPtr
    Flags: UIntPtr
class PROCESS_DYNAMIC_EH_CONTINUATION_TARGETS_INFORMATION(Structure):
    NumberOfTargets: UInt16
    Reserved: UInt16
    Reserved2: UInt32
    Targets: POINTER(win32more.System.Threading.PROCESS_DYNAMIC_EH_CONTINUATION_TARGET_head)
class PROCESS_DYNAMIC_ENFORCED_ADDRESS_RANGE(Structure):
    BaseAddress: UIntPtr
    Size: UIntPtr
    Flags: UInt32
class PROCESS_DYNAMIC_ENFORCED_ADDRESS_RANGES_INFORMATION(Structure):
    NumberOfRanges: UInt16
    Reserved: UInt16
    Reserved2: UInt32
    Ranges: POINTER(win32more.System.Threading.PROCESS_DYNAMIC_ENFORCED_ADDRESS_RANGE_head)
class PROCESS_INFORMATION(Structure):
    hProcess: win32more.Foundation.HANDLE
    hThread: win32more.Foundation.HANDLE
    dwProcessId: UInt32
    dwThreadId: UInt32
PROCESS_INFORMATION_CLASS = Int32
PROCESS_INFORMATION_CLASS_ProcessMemoryPriority: PROCESS_INFORMATION_CLASS = 0
PROCESS_INFORMATION_CLASS_ProcessMemoryExhaustionInfo: PROCESS_INFORMATION_CLASS = 1
PROCESS_INFORMATION_CLASS_ProcessAppMemoryInfo: PROCESS_INFORMATION_CLASS = 2
PROCESS_INFORMATION_CLASS_ProcessInPrivateInfo: PROCESS_INFORMATION_CLASS = 3
PROCESS_INFORMATION_CLASS_ProcessPowerThrottling: PROCESS_INFORMATION_CLASS = 4
PROCESS_INFORMATION_CLASS_ProcessReservedValue1: PROCESS_INFORMATION_CLASS = 5
PROCESS_INFORMATION_CLASS_ProcessTelemetryCoverageInfo: PROCESS_INFORMATION_CLASS = 6
PROCESS_INFORMATION_CLASS_ProcessProtectionLevelInfo: PROCESS_INFORMATION_CLASS = 7
PROCESS_INFORMATION_CLASS_ProcessLeapSecondInfo: PROCESS_INFORMATION_CLASS = 8
PROCESS_INFORMATION_CLASS_ProcessMachineTypeInfo: PROCESS_INFORMATION_CLASS = 9
PROCESS_INFORMATION_CLASS_ProcessInformationClassMax: PROCESS_INFORMATION_CLASS = 10
class PROCESS_LEAP_SECOND_INFO(Structure):
    Flags: UInt32
    Reserved: UInt32
class PROCESS_MACHINE_INFORMATION(Structure):
    ProcessMachine: win32more.System.SystemInformation.IMAGE_FILE_MACHINE
    Res0: UInt16
    MachineAttributes: win32more.System.Threading.MACHINE_ATTRIBUTES
class PROCESS_MEMORY_EXHAUSTION_INFO(Structure):
    Version: UInt16
    Reserved: UInt16
    Type: win32more.System.Threading.PROCESS_MEMORY_EXHAUSTION_TYPE
    Value: UIntPtr
PROCESS_MEMORY_EXHAUSTION_TYPE = Int32
PROCESS_MEMORY_EXHAUSTION_TYPE_PMETypeFailFastOnCommitFailure: PROCESS_MEMORY_EXHAUSTION_TYPE = 0
PROCESS_MEMORY_EXHAUSTION_TYPE_PMETypeMax: PROCESS_MEMORY_EXHAUSTION_TYPE = 1
PROCESS_MITIGATION_POLICY = Int32
PROCESS_MITIGATION_POLICY_ProcessDEPPolicy: PROCESS_MITIGATION_POLICY = 0
PROCESS_MITIGATION_POLICY_ProcessASLRPolicy: PROCESS_MITIGATION_POLICY = 1
PROCESS_MITIGATION_POLICY_ProcessDynamicCodePolicy: PROCESS_MITIGATION_POLICY = 2
PROCESS_MITIGATION_POLICY_ProcessStrictHandleCheckPolicy: PROCESS_MITIGATION_POLICY = 3
PROCESS_MITIGATION_POLICY_ProcessSystemCallDisablePolicy: PROCESS_MITIGATION_POLICY = 4
PROCESS_MITIGATION_POLICY_ProcessMitigationOptionsMask: PROCESS_MITIGATION_POLICY = 5
PROCESS_MITIGATION_POLICY_ProcessExtensionPointDisablePolicy: PROCESS_MITIGATION_POLICY = 6
PROCESS_MITIGATION_POLICY_ProcessControlFlowGuardPolicy: PROCESS_MITIGATION_POLICY = 7
PROCESS_MITIGATION_POLICY_ProcessSignaturePolicy: PROCESS_MITIGATION_POLICY = 8
PROCESS_MITIGATION_POLICY_ProcessFontDisablePolicy: PROCESS_MITIGATION_POLICY = 9
PROCESS_MITIGATION_POLICY_ProcessImageLoadPolicy: PROCESS_MITIGATION_POLICY = 10
PROCESS_MITIGATION_POLICY_ProcessSystemCallFilterPolicy: PROCESS_MITIGATION_POLICY = 11
PROCESS_MITIGATION_POLICY_ProcessPayloadRestrictionPolicy: PROCESS_MITIGATION_POLICY = 12
PROCESS_MITIGATION_POLICY_ProcessChildProcessPolicy: PROCESS_MITIGATION_POLICY = 13
PROCESS_MITIGATION_POLICY_ProcessSideChannelIsolationPolicy: PROCESS_MITIGATION_POLICY = 14
PROCESS_MITIGATION_POLICY_ProcessUserShadowStackPolicy: PROCESS_MITIGATION_POLICY = 15
PROCESS_MITIGATION_POLICY_ProcessRedirectionTrustPolicy: PROCESS_MITIGATION_POLICY = 16
PROCESS_MITIGATION_POLICY_MaxProcessMitigationPolicy: PROCESS_MITIGATION_POLICY = 17
PROCESS_NAME_FORMAT = UInt32
PROCESS_NAME_WIN32: PROCESS_NAME_FORMAT = 0
PROCESS_NAME_NATIVE: PROCESS_NAME_FORMAT = 1
class PROCESS_POWER_THROTTLING_STATE(Structure):
    Version: UInt32
    ControlMask: UInt32
    StateMask: UInt32
PROCESS_PROTECTION_LEVEL = UInt32
PROTECTION_LEVEL_WINTCB_LIGHT: PROCESS_PROTECTION_LEVEL = 0
PROTECTION_LEVEL_WINDOWS: PROCESS_PROTECTION_LEVEL = 1
PROTECTION_LEVEL_WINDOWS_LIGHT: PROCESS_PROTECTION_LEVEL = 2
PROTECTION_LEVEL_ANTIMALWARE_LIGHT: PROCESS_PROTECTION_LEVEL = 3
PROTECTION_LEVEL_LSA_LIGHT: PROCESS_PROTECTION_LEVEL = 4
PROTECTION_LEVEL_WINTCB: PROCESS_PROTECTION_LEVEL = 5
PROTECTION_LEVEL_CODEGEN_LIGHT: PROCESS_PROTECTION_LEVEL = 6
PROTECTION_LEVEL_AUTHENTICODE: PROCESS_PROTECTION_LEVEL = 7
PROTECTION_LEVEL_PPL_APP: PROCESS_PROTECTION_LEVEL = 8
PROTECTION_LEVEL_NONE: PROCESS_PROTECTION_LEVEL = 4294967294
class PROCESS_PROTECTION_LEVEL_INFORMATION(Structure):
    ProtectionLevel: win32more.System.Threading.PROCESS_PROTECTION_LEVEL
PROC_THREAD_ATTRIBUTE_NUM = UInt32
PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeParentProcess: PROC_THREAD_ATTRIBUTE_NUM = 0
PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeHandleList: PROC_THREAD_ATTRIBUTE_NUM = 2
PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeGroupAffinity: PROC_THREAD_ATTRIBUTE_NUM = 3
PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributePreferredNode: PROC_THREAD_ATTRIBUTE_NUM = 4
PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeIdealProcessor: PROC_THREAD_ATTRIBUTE_NUM = 5
PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeUmsThread: PROC_THREAD_ATTRIBUTE_NUM = 6
PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeMitigationPolicy: PROC_THREAD_ATTRIBUTE_NUM = 7
PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeSecurityCapabilities: PROC_THREAD_ATTRIBUTE_NUM = 9
PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeProtectionLevel: PROC_THREAD_ATTRIBUTE_NUM = 11
PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeJobList: PROC_THREAD_ATTRIBUTE_NUM = 13
PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeChildProcessPolicy: PROC_THREAD_ATTRIBUTE_NUM = 14
PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeAllApplicationPackagesPolicy: PROC_THREAD_ATTRIBUTE_NUM = 15
PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeWin32kFilter: PROC_THREAD_ATTRIBUTE_NUM = 16
PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeSafeOpenPromptOriginClaim: PROC_THREAD_ATTRIBUTE_NUM = 17
PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeDesktopAppPolicy: PROC_THREAD_ATTRIBUTE_NUM = 18
PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributePseudoConsole: PROC_THREAD_ATTRIBUTE_NUM = 22
PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeMitigationAuditPolicy: PROC_THREAD_ATTRIBUTE_NUM = 24
PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeMachineType: PROC_THREAD_ATTRIBUTE_NUM = 25
PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeComponentFilter: PROC_THREAD_ATTRIBUTE_NUM = 26
PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeEnableOptionalXStateFeatures: PROC_THREAD_ATTRIBUTE_NUM = 27
@winfunctype_pointer
def PRTL_UMS_SCHEDULER_ENTRY_POINT(Reason: win32more.System.SystemServices.RTL_UMS_SCHEDULER_REASON, ActivationPayload: UIntPtr, SchedulerParam: c_void_p) -> Void: ...
@winfunctype_pointer
def PTIMERAPCROUTINE(lpArgToCompletionRoutine: c_void_p, dwTimerLowValue: UInt32, dwTimerHighValue: UInt32) -> Void: ...
@winfunctype_pointer
def PTP_CLEANUP_GROUP_CANCEL_CALLBACK(ObjectContext: c_void_p, CleanupContext: c_void_p) -> Void: ...
PTP_POOL = IntPtr
@winfunctype_pointer
def PTP_SIMPLE_CALLBACK(Instance: POINTER(win32more.System.Threading.TP_CALLBACK_INSTANCE_head), Context: c_void_p) -> Void: ...
@winfunctype_pointer
def PTP_TIMER_CALLBACK(Instance: POINTER(win32more.System.Threading.TP_CALLBACK_INSTANCE_head), Context: c_void_p, Timer: POINTER(win32more.System.Threading.TP_TIMER_head)) -> Void: ...
@winfunctype_pointer
def PTP_WAIT_CALLBACK(Instance: POINTER(win32more.System.Threading.TP_CALLBACK_INSTANCE_head), Context: c_void_p, Wait: POINTER(win32more.System.Threading.TP_WAIT_head), WaitResult: UInt32) -> Void: ...
@winfunctype_pointer
def PTP_WIN32_IO_CALLBACK(Instance: POINTER(win32more.System.Threading.TP_CALLBACK_INSTANCE_head), Context: c_void_p, Overlapped: c_void_p, IoResult: UInt32, NumberOfBytesTransferred: UIntPtr, Io: POINTER(win32more.System.Threading.TP_IO_head)) -> Void: ...
@winfunctype_pointer
def PTP_WORK_CALLBACK(Instance: POINTER(win32more.System.Threading.TP_CALLBACK_INSTANCE_head), Context: c_void_p, Work: POINTER(win32more.System.Threading.TP_WORK_head)) -> Void: ...
QUEUE_USER_APC_FLAGS = Int32
QUEUE_USER_APC_FLAGS_NONE: QUEUE_USER_APC_FLAGS = 0
QUEUE_USER_APC_FLAGS_SPECIAL_USER_APC: QUEUE_USER_APC_FLAGS = 1
class REASON_CONTEXT(Structure):
    Version: UInt32
    Flags: win32more.System.Threading.POWER_REQUEST_CONTEXT_FLAGS
    Reason: _Reason_e__Union
    class _Reason_e__Union(Union):
        Detailed: _Detailed_e__Struct
        SimpleReasonString: win32more.Foundation.PWSTR
        class _Detailed_e__Struct(Structure):
            LocalizedReasonModule: win32more.Foundation.HINSTANCE
            LocalizedReasonId: UInt32
            ReasonStringCount: UInt32
            ReasonStrings: POINTER(win32more.Foundation.PWSTR)
class RTL_BARRIER(Structure):
    Reserved1: UInt32
    Reserved2: UInt32
    Reserved3: UIntPtr * 2
    Reserved4: UInt32
    Reserved5: UInt32
class RTL_CONDITION_VARIABLE(Structure):
    Ptr: c_void_p
class RTL_CRITICAL_SECTION(Structure):
    DebugInfo: POINTER(win32more.System.Threading.RTL_CRITICAL_SECTION_DEBUG_head)
    LockCount: Int32
    RecursionCount: Int32
    OwningThread: win32more.Foundation.HANDLE
    LockSemaphore: win32more.Foundation.HANDLE
    SpinCount: UIntPtr
class RTL_CRITICAL_SECTION_DEBUG(Structure):
    Type: UInt16
    CreatorBackTraceIndex: UInt16
    CriticalSection: POINTER(win32more.System.Threading.RTL_CRITICAL_SECTION_head)
    ProcessLocksList: win32more.System.Kernel.LIST_ENTRY
    EntryCount: UInt32
    ContentionCount: UInt32
    Flags: UInt32
    CreatorBackTraceIndexHigh: UInt16
    SpareWORD: UInt16
class RTL_RUN_ONCE(Union):
    Ptr: c_void_p
class RTL_SRWLOCK(Structure):
    Ptr: c_void_p
RTL_UMS_THREAD_INFO_CLASS = Int32
RTL_UMS_THREAD_INFO_CLASS_UmsThreadInvalidInfoClass: RTL_UMS_THREAD_INFO_CLASS = 0
RTL_UMS_THREAD_INFO_CLASS_UmsThreadUserContext: RTL_UMS_THREAD_INFO_CLASS = 1
RTL_UMS_THREAD_INFO_CLASS_UmsThreadPriority: RTL_UMS_THREAD_INFO_CLASS = 2
RTL_UMS_THREAD_INFO_CLASS_UmsThreadAffinity: RTL_UMS_THREAD_INFO_CLASS = 3
RTL_UMS_THREAD_INFO_CLASS_UmsThreadTeb: RTL_UMS_THREAD_INFO_CLASS = 4
RTL_UMS_THREAD_INFO_CLASS_UmsThreadIsSuspended: RTL_UMS_THREAD_INFO_CLASS = 5
RTL_UMS_THREAD_INFO_CLASS_UmsThreadIsTerminated: RTL_UMS_THREAD_INFO_CLASS = 6
RTL_UMS_THREAD_INFO_CLASS_UmsThreadMaxInfoClass: RTL_UMS_THREAD_INFO_CLASS = 7
class RTL_USER_PROCESS_PARAMETERS(Structure):
    Reserved1: Byte * 16
    Reserved2: c_void_p * 10
    ImagePathName: win32more.Foundation.UNICODE_STRING
    CommandLine: win32more.Foundation.UNICODE_STRING
class STARTUPINFOA(Structure):
    cb: UInt32
    lpReserved: win32more.Foundation.PSTR
    lpDesktop: win32more.Foundation.PSTR
    lpTitle: win32more.Foundation.PSTR
    dwX: UInt32
    dwY: UInt32
    dwXSize: UInt32
    dwYSize: UInt32
    dwXCountChars: UInt32
    dwYCountChars: UInt32
    dwFillAttribute: UInt32
    dwFlags: win32more.System.Threading.STARTUPINFOW_FLAGS
    wShowWindow: UInt16
    cbReserved2: UInt16
    lpReserved2: c_char_p_no
    hStdInput: win32more.Foundation.HANDLE
    hStdOutput: win32more.Foundation.HANDLE
    hStdError: win32more.Foundation.HANDLE
class STARTUPINFOEXA(Structure):
    StartupInfo: win32more.System.Threading.STARTUPINFOA
    lpAttributeList: win32more.System.Threading.LPPROC_THREAD_ATTRIBUTE_LIST
class STARTUPINFOEXW(Structure):
    StartupInfo: win32more.System.Threading.STARTUPINFOW
    lpAttributeList: win32more.System.Threading.LPPROC_THREAD_ATTRIBUTE_LIST
class STARTUPINFOW(Structure):
    cb: UInt32
    lpReserved: win32more.Foundation.PWSTR
    lpDesktop: win32more.Foundation.PWSTR
    lpTitle: win32more.Foundation.PWSTR
    dwX: UInt32
    dwY: UInt32
    dwXSize: UInt32
    dwYSize: UInt32
    dwXCountChars: UInt32
    dwYCountChars: UInt32
    dwFillAttribute: UInt32
    dwFlags: win32more.System.Threading.STARTUPINFOW_FLAGS
    wShowWindow: UInt16
    cbReserved2: UInt16
    lpReserved2: c_char_p_no
    hStdInput: win32more.Foundation.HANDLE
    hStdOutput: win32more.Foundation.HANDLE
    hStdError: win32more.Foundation.HANDLE
STARTUPINFOW_FLAGS = UInt32
STARTF_FORCEONFEEDBACK: STARTUPINFOW_FLAGS = 64
STARTF_FORCEOFFFEEDBACK: STARTUPINFOW_FLAGS = 128
STARTF_PREVENTPINNING: STARTUPINFOW_FLAGS = 8192
STARTF_RUNFULLSCREEN: STARTUPINFOW_FLAGS = 32
STARTF_TITLEISAPPID: STARTUPINFOW_FLAGS = 4096
STARTF_TITLEISLINKNAME: STARTUPINFOW_FLAGS = 2048
STARTF_UNTRUSTEDSOURCE: STARTUPINFOW_FLAGS = 32768
STARTF_USECOUNTCHARS: STARTUPINFOW_FLAGS = 8
STARTF_USEFILLATTRIBUTE: STARTUPINFOW_FLAGS = 16
STARTF_USEHOTKEY: STARTUPINFOW_FLAGS = 512
STARTF_USEPOSITION: STARTUPINFOW_FLAGS = 4
STARTF_USESHOWWINDOW: STARTUPINFOW_FLAGS = 1
STARTF_USESIZE: STARTUPINFOW_FLAGS = 2
STARTF_USESTDHANDLES: STARTUPINFOW_FLAGS = 256
SYNCHRONIZATION_ACCESS_RIGHTS = UInt32
EVENT_ALL_ACCESS: SYNCHRONIZATION_ACCESS_RIGHTS = 2031619
EVENT_MODIFY_STATE: SYNCHRONIZATION_ACCESS_RIGHTS = 2
MUTEX_ALL_ACCESS: SYNCHRONIZATION_ACCESS_RIGHTS = 2031617
MUTEX_MODIFY_STATE: SYNCHRONIZATION_ACCESS_RIGHTS = 1
SEMAPHORE_ALL_ACCESS: SYNCHRONIZATION_ACCESS_RIGHTS = 2031619
SEMAPHORE_MODIFY_STATE: SYNCHRONIZATION_ACCESS_RIGHTS = 2
TIMER_ALL_ACCESS: SYNCHRONIZATION_ACCESS_RIGHTS = 2031619
TIMER_MODIFY_STATE: SYNCHRONIZATION_ACCESS_RIGHTS = 2
TIMER_QUERY_STATE: SYNCHRONIZATION_ACCESS_RIGHTS = 1
SYNCHRONIZATION_DELETE: SYNCHRONIZATION_ACCESS_RIGHTS = 65536
SYNCHRONIZATION_READ_CONTROL: SYNCHRONIZATION_ACCESS_RIGHTS = 131072
SYNCHRONIZATION_WRITE_DAC: SYNCHRONIZATION_ACCESS_RIGHTS = 262144
SYNCHRONIZATION_WRITE_OWNER: SYNCHRONIZATION_ACCESS_RIGHTS = 524288
SYNCHRONIZATION_SYNCHRONIZE: SYNCHRONIZATION_ACCESS_RIGHTS = 1048576
THREADINFOCLASS = Int32
THREADINFOCLASS_ThreadIsIoPending: THREADINFOCLASS = 16
THREADINFOCLASS_ThreadNameInformation: THREADINFOCLASS = 38
THREAD_ACCESS_RIGHTS = UInt32
THREAD_TERMINATE: THREAD_ACCESS_RIGHTS = 1
THREAD_SUSPEND_RESUME: THREAD_ACCESS_RIGHTS = 2
THREAD_GET_CONTEXT: THREAD_ACCESS_RIGHTS = 8
THREAD_SET_CONTEXT: THREAD_ACCESS_RIGHTS = 16
THREAD_SET_INFORMATION: THREAD_ACCESS_RIGHTS = 32
THREAD_QUERY_INFORMATION: THREAD_ACCESS_RIGHTS = 64
THREAD_SET_THREAD_TOKEN: THREAD_ACCESS_RIGHTS = 128
THREAD_IMPERSONATE: THREAD_ACCESS_RIGHTS = 256
THREAD_DIRECT_IMPERSONATION: THREAD_ACCESS_RIGHTS = 512
THREAD_SET_LIMITED_INFORMATION: THREAD_ACCESS_RIGHTS = 1024
THREAD_QUERY_LIMITED_INFORMATION: THREAD_ACCESS_RIGHTS = 2048
THREAD_RESUME: THREAD_ACCESS_RIGHTS = 4096
THREAD_ALL_ACCESS: THREAD_ACCESS_RIGHTS = 2097151
THREAD_DELETE: THREAD_ACCESS_RIGHTS = 65536
THREAD_READ_CONTROL: THREAD_ACCESS_RIGHTS = 131072
THREAD_WRITE_DAC: THREAD_ACCESS_RIGHTS = 262144
THREAD_WRITE_OWNER: THREAD_ACCESS_RIGHTS = 524288
THREAD_SYNCHRONIZE: THREAD_ACCESS_RIGHTS = 1048576
THREAD_STANDARD_RIGHTS_REQUIRED: THREAD_ACCESS_RIGHTS = 983040
THREAD_CREATION_FLAGS = UInt32
THREAD_CREATE_RUN_IMMEDIATELY: THREAD_CREATION_FLAGS = 0
THREAD_CREATE_SUSPENDED: THREAD_CREATION_FLAGS = 4
STACK_SIZE_PARAM_IS_A_RESERVATION: THREAD_CREATION_FLAGS = 65536
THREAD_INFORMATION_CLASS = Int32
THREAD_INFORMATION_CLASS_ThreadMemoryPriority: THREAD_INFORMATION_CLASS = 0
THREAD_INFORMATION_CLASS_ThreadAbsoluteCpuPriority: THREAD_INFORMATION_CLASS = 1
THREAD_INFORMATION_CLASS_ThreadDynamicCodePolicy: THREAD_INFORMATION_CLASS = 2
THREAD_INFORMATION_CLASS_ThreadPowerThrottling: THREAD_INFORMATION_CLASS = 3
THREAD_INFORMATION_CLASS_ThreadInformationClassMax: THREAD_INFORMATION_CLASS = 4
class THREAD_POWER_THROTTLING_STATE(Structure):
    Version: UInt32
    ControlMask: UInt32
    StateMask: UInt32
THREAD_PRIORITY = Int32
THREAD_MODE_BACKGROUND_BEGIN: THREAD_PRIORITY = 65536
THREAD_MODE_BACKGROUND_END: THREAD_PRIORITY = 131072
THREAD_PRIORITY_ABOVE_NORMAL: THREAD_PRIORITY = 1
THREAD_PRIORITY_BELOW_NORMAL: THREAD_PRIORITY = -1
THREAD_PRIORITY_HIGHEST: THREAD_PRIORITY = 2
THREAD_PRIORITY_IDLE: THREAD_PRIORITY = -15
THREAD_PRIORITY_MIN: THREAD_PRIORITY = -2
THREAD_PRIORITY_LOWEST: THREAD_PRIORITY = -2
THREAD_PRIORITY_NORMAL: THREAD_PRIORITY = 0
THREAD_PRIORITY_TIME_CRITICAL: THREAD_PRIORITY = 15
class TP_CALLBACK_ENVIRON_V3(Structure):
    Version: UInt32
    Pool: win32more.System.Threading.PTP_POOL
    CleanupGroup: IntPtr
    CleanupGroupCancelCallback: win32more.System.Threading.PTP_CLEANUP_GROUP_CANCEL_CALLBACK
    RaceDll: c_void_p
    ActivationContext: IntPtr
    FinalizationCallback: win32more.System.Threading.PTP_SIMPLE_CALLBACK
    u: _u_e__Union
    CallbackPriority: win32more.System.Threading.TP_CALLBACK_PRIORITY
    Size: UInt32
    class _ACTIVATION_CONTEXT(Structure):
        pass
    class _u_e__Union(Union):
        Flags: UInt32
        s: _s_e__Struct
        class _s_e__Struct(Structure):
            _bitfield: UInt32
class TP_CALLBACK_INSTANCE(Structure):
    pass
TP_CALLBACK_PRIORITY = Int32
TP_CALLBACK_PRIORITY_HIGH: TP_CALLBACK_PRIORITY = 0
TP_CALLBACK_PRIORITY_NORMAL: TP_CALLBACK_PRIORITY = 1
TP_CALLBACK_PRIORITY_LOW: TP_CALLBACK_PRIORITY = 2
TP_CALLBACK_PRIORITY_INVALID: TP_CALLBACK_PRIORITY = 3
TP_CALLBACK_PRIORITY_COUNT: TP_CALLBACK_PRIORITY = 3
class TP_IO(Structure):
    pass
class TP_POOL_STACK_INFORMATION(Structure):
    StackReserve: UIntPtr
    StackCommit: UIntPtr
class TP_TIMER(Structure):
    pass
class TP_WAIT(Structure):
    pass
class TP_WORK(Structure):
    pass
TimerQueueHandle = IntPtr
class UMS_SCHEDULER_STARTUP_INFO(Structure):
    UmsVersion: UInt32
    CompletionList: c_void_p
    SchedulerProc: win32more.System.Threading.PRTL_UMS_SCHEDULER_ENTRY_POINT
    SchedulerParam: c_void_p
class UMS_SYSTEM_THREAD_INFORMATION(Structure):
    UmsVersion: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        ThreadUmsFlags: UInt32
        class _Anonymous_e__Struct(Structure):
            _bitfield: UInt32
@winfunctype_pointer
def WAITORTIMERCALLBACK(param0: c_void_p, param1: win32more.Foundation.BOOLEAN) -> Void: ...
WORKER_THREAD_FLAGS = UInt32
WT_EXECUTEDEFAULT: WORKER_THREAD_FLAGS = 0
WT_EXECUTEINIOTHREAD: WORKER_THREAD_FLAGS = 1
WT_EXECUTEINPERSISTENTTHREAD: WORKER_THREAD_FLAGS = 128
WT_EXECUTEINWAITTHREAD: WORKER_THREAD_FLAGS = 4
WT_EXECUTELONGFUNCTION: WORKER_THREAD_FLAGS = 16
WT_EXECUTEONLYONCE: WORKER_THREAD_FLAGS = 8
WT_TRANSFER_IMPERSONATION: WORKER_THREAD_FLAGS = 256
WT_EXECUTEINTIMERTHREAD: WORKER_THREAD_FLAGS = 32
make_head(_module, 'APP_MEMORY_INFORMATION')
make_head(_module, 'IO_COUNTERS')
make_head(_module, 'LPFIBER_START_ROUTINE')
make_head(_module, 'LPTHREAD_START_ROUTINE')
make_head(_module, 'MEMORY_PRIORITY_INFORMATION')
make_head(_module, 'PEB')
make_head(_module, 'PEB_LDR_DATA')
make_head(_module, 'PFLS_CALLBACK_FUNCTION')
make_head(_module, 'PINIT_ONCE_FN')
make_head(_module, 'PPS_POST_PROCESS_INIT_ROUTINE')
make_head(_module, 'PROCESS_BASIC_INFORMATION')
make_head(_module, 'PROCESS_DYNAMIC_EH_CONTINUATION_TARGET')
make_head(_module, 'PROCESS_DYNAMIC_EH_CONTINUATION_TARGETS_INFORMATION')
make_head(_module, 'PROCESS_DYNAMIC_ENFORCED_ADDRESS_RANGE')
make_head(_module, 'PROCESS_DYNAMIC_ENFORCED_ADDRESS_RANGES_INFORMATION')
make_head(_module, 'PROCESS_INFORMATION')
make_head(_module, 'PROCESS_LEAP_SECOND_INFO')
make_head(_module, 'PROCESS_MACHINE_INFORMATION')
make_head(_module, 'PROCESS_MEMORY_EXHAUSTION_INFO')
make_head(_module, 'PROCESS_POWER_THROTTLING_STATE')
make_head(_module, 'PROCESS_PROTECTION_LEVEL_INFORMATION')
make_head(_module, 'PRTL_UMS_SCHEDULER_ENTRY_POINT')
make_head(_module, 'PTIMERAPCROUTINE')
make_head(_module, 'PTP_CLEANUP_GROUP_CANCEL_CALLBACK')
make_head(_module, 'PTP_SIMPLE_CALLBACK')
make_head(_module, 'PTP_TIMER_CALLBACK')
make_head(_module, 'PTP_WAIT_CALLBACK')
make_head(_module, 'PTP_WIN32_IO_CALLBACK')
make_head(_module, 'PTP_WORK_CALLBACK')
make_head(_module, 'REASON_CONTEXT')
make_head(_module, 'RTL_BARRIER')
make_head(_module, 'RTL_CONDITION_VARIABLE')
make_head(_module, 'RTL_CRITICAL_SECTION')
make_head(_module, 'RTL_CRITICAL_SECTION_DEBUG')
make_head(_module, 'RTL_RUN_ONCE')
make_head(_module, 'RTL_SRWLOCK')
make_head(_module, 'RTL_USER_PROCESS_PARAMETERS')
make_head(_module, 'STARTUPINFOA')
make_head(_module, 'STARTUPINFOEXA')
make_head(_module, 'STARTUPINFOEXW')
make_head(_module, 'STARTUPINFOW')
make_head(_module, 'THREAD_POWER_THROTTLING_STATE')
make_head(_module, 'TP_CALLBACK_ENVIRON_V3')
make_head(_module, 'TP_CALLBACK_INSTANCE')
make_head(_module, 'TP_IO')
make_head(_module, 'TP_POOL_STACK_INFORMATION')
make_head(_module, 'TP_TIMER')
make_head(_module, 'TP_WAIT')
make_head(_module, 'TP_WORK')
make_head(_module, 'UMS_SCHEDULER_STARTUP_INFO')
make_head(_module, 'UMS_SYSTEM_THREAD_INFORMATION')
make_head(_module, 'WAITORTIMERCALLBACK')
__all__ = [
    "ABOVE_NORMAL_PRIORITY_CLASS",
    "APP_MEMORY_INFORMATION",
    "AVRT_PRIORITY",
    "AVRT_PRIORITY_CRITICAL",
    "AVRT_PRIORITY_HIGH",
    "AVRT_PRIORITY_LOW",
    "AVRT_PRIORITY_NORMAL",
    "AVRT_PRIORITY_VERYLOW",
    "AcquireSRWLockExclusive",
    "AcquireSRWLockShared",
    "AddIntegrityLabelToBoundaryDescriptor",
    "AddSIDToBoundaryDescriptor",
    "AttachThreadInput",
    "AvQuerySystemResponsiveness",
    "AvRevertMmThreadCharacteristics",
    "AvRtCreateThreadOrderingGroup",
    "AvRtCreateThreadOrderingGroupExA",
    "AvRtCreateThreadOrderingGroupExW",
    "AvRtDeleteThreadOrderingGroup",
    "AvRtJoinThreadOrderingGroup",
    "AvRtLeaveThreadOrderingGroup",
    "AvRtWaitOnThreadOrderingGroup",
    "AvSetMmMaxThreadCharacteristicsA",
    "AvSetMmMaxThreadCharacteristicsW",
    "AvSetMmThreadCharacteristicsA",
    "AvSetMmThreadCharacteristicsW",
    "AvSetMmThreadPriority",
    "BELOW_NORMAL_PRIORITY_CLASS",
    "BoundaryDescriptorHandle",
    "CONDITION_VARIABLE_LOCKMODE_SHARED",
    "CREATE_BREAKAWAY_FROM_JOB",
    "CREATE_DEFAULT_ERROR_MODE",
    "CREATE_EVENT",
    "CREATE_EVENT_INITIAL_SET",
    "CREATE_EVENT_MANUAL_RESET",
    "CREATE_FORCEDOS",
    "CREATE_IGNORE_SYSTEM_DEFAULT",
    "CREATE_MUTEX_INITIAL_OWNER",
    "CREATE_NEW_CONSOLE",
    "CREATE_NEW_PROCESS_GROUP",
    "CREATE_NO_WINDOW",
    "CREATE_PRESERVE_CODE_AUTHZ_LEVEL",
    "CREATE_PROCESS_LOGON_FLAGS",
    "CREATE_PROTECTED_PROCESS",
    "CREATE_SECURE_PROCESS",
    "CREATE_SEPARATE_WOW_VDM",
    "CREATE_SHARED_WOW_VDM",
    "CREATE_SUSPENDED",
    "CREATE_UNICODE_ENVIRONMENT",
    "CREATE_WAITABLE_TIMER_HIGH_RESOLUTION",
    "CREATE_WAITABLE_TIMER_MANUAL_RESET",
    "CallbackMayRunLong",
    "CancelThreadpoolIo",
    "CancelWaitableTimer",
    "ChangeTimerQueueTimer",
    "ClosePrivateNamespace",
    "CloseThreadpool",
    "CloseThreadpoolCleanupGroup",
    "CloseThreadpoolCleanupGroupMembers",
    "CloseThreadpoolIo",
    "CloseThreadpoolTimer",
    "CloseThreadpoolWait",
    "CloseThreadpoolWork",
    "ConvertFiberToThread",
    "ConvertThreadToFiber",
    "ConvertThreadToFiberEx",
    "CreateBoundaryDescriptorA",
    "CreateBoundaryDescriptorW",
    "CreateEventA",
    "CreateEventExA",
    "CreateEventExW",
    "CreateEventW",
    "CreateFiber",
    "CreateFiberEx",
    "CreateMutexA",
    "CreateMutexExA",
    "CreateMutexExW",
    "CreateMutexW",
    "CreatePrivateNamespaceA",
    "CreatePrivateNamespaceW",
    "CreateProcessA",
    "CreateProcessAsUserA",
    "CreateProcessAsUserW",
    "CreateProcessW",
    "CreateProcessWithLogonW",
    "CreateProcessWithTokenW",
    "CreateRemoteThread",
    "CreateRemoteThreadEx",
    "CreateSemaphoreA",
    "CreateSemaphoreExA",
    "CreateSemaphoreExW",
    "CreateSemaphoreW",
    "CreateThread",
    "CreateThreadpool",
    "CreateThreadpoolCleanupGroup",
    "CreateThreadpoolIo",
    "CreateThreadpoolTimer",
    "CreateThreadpoolWait",
    "CreateThreadpoolWork",
    "CreateTimerQueue",
    "CreateTimerQueueTimer",
    "CreateUmsCompletionList",
    "CreateUmsThreadContext",
    "CreateWaitableTimerExW",
    "CreateWaitableTimerW",
    "DEBUG_ONLY_THIS_PROCESS",
    "DEBUG_PROCESS",
    "DETACHED_PROCESS",
    "DeleteBoundaryDescriptor",
    "DeleteCriticalSection",
    "DeleteFiber",
    "DeleteProcThreadAttributeList",
    "DeleteSynchronizationBarrier",
    "DeleteTimerQueue",
    "DeleteTimerQueueEx",
    "DeleteTimerQueueTimer",
    "DeleteUmsCompletionList",
    "DeleteUmsThreadContext",
    "DequeueUmsCompletionListItems",
    "DisassociateCurrentThreadFromCallback",
    "EVENT_ALL_ACCESS",
    "EVENT_MODIFY_STATE",
    "EXTENDED_STARTUPINFO_PRESENT",
    "EnterCriticalSection",
    "EnterSynchronizationBarrier",
    "EnterUmsSchedulingMode",
    "ExecuteUmsThread",
    "ExitProcess",
    "ExitThread",
    "FLS_OUT_OF_INDEXES",
    "FlsAlloc",
    "FlsFree",
    "FlsGetValue",
    "FlsSetValue",
    "FlushProcessWriteBuffers",
    "FreeLibraryWhenCallbackReturns",
    "GET_GUI_RESOURCES_FLAGS",
    "GR_GDIOBJECTS",
    "GR_GDIOBJECTS_PEAK",
    "GR_USEROBJECTS",
    "GR_USEROBJECTS_PEAK",
    "GetActiveProcessorCount",
    "GetActiveProcessorGroupCount",
    "GetCurrentProcess",
    "GetCurrentProcessId",
    "GetCurrentProcessorNumber",
    "GetCurrentProcessorNumberEx",
    "GetCurrentThread",
    "GetCurrentThreadId",
    "GetCurrentThreadStackLimits",
    "GetCurrentUmsThread",
    "GetExitCodeProcess",
    "GetExitCodeThread",
    "GetGuiResources",
    "GetMachineTypeAttributes",
    "GetMaximumProcessorCount",
    "GetMaximumProcessorGroupCount",
    "GetNextUmsListItem",
    "GetNumaAvailableMemoryNode",
    "GetNumaAvailableMemoryNodeEx",
    "GetNumaHighestNodeNumber",
    "GetNumaNodeNumberFromHandle",
    "GetNumaNodeProcessorMask",
    "GetNumaNodeProcessorMask2",
    "GetNumaNodeProcessorMaskEx",
    "GetNumaProcessorNode",
    "GetNumaProcessorNodeEx",
    "GetNumaProximityNode",
    "GetNumaProximityNodeEx",
    "GetPriorityClass",
    "GetProcessAffinityMask",
    "GetProcessDEPPolicy",
    "GetProcessDefaultCpuSetMasks",
    "GetProcessDefaultCpuSets",
    "GetProcessGroupAffinity",
    "GetProcessHandleCount",
    "GetProcessId",
    "GetProcessIdOfThread",
    "GetProcessInformation",
    "GetProcessIoCounters",
    "GetProcessMitigationPolicy",
    "GetProcessPriorityBoost",
    "GetProcessShutdownParameters",
    "GetProcessTimes",
    "GetProcessVersion",
    "GetProcessWorkingSetSize",
    "GetStartupInfoA",
    "GetStartupInfoW",
    "GetSystemTimes",
    "GetThreadDescription",
    "GetThreadGroupAffinity",
    "GetThreadIOPendingFlag",
    "GetThreadId",
    "GetThreadIdealProcessorEx",
    "GetThreadInformation",
    "GetThreadPriority",
    "GetThreadPriorityBoost",
    "GetThreadSelectedCpuSetMasks",
    "GetThreadSelectedCpuSets",
    "GetThreadTimes",
    "GetUmsCompletionListEvent",
    "GetUmsSystemThreadInformation",
    "HIGH_PRIORITY_CLASS",
    "IDLE_PRIORITY_CLASS",
    "INHERIT_CALLER_PRIORITY",
    "INHERIT_PARENT_AFFINITY",
    "INIT_ONCE_ASYNC",
    "INIT_ONCE_CHECK_ONLY",
    "INIT_ONCE_CTX_RESERVED_BITS",
    "INIT_ONCE_INIT_FAILED",
    "IO_COUNTERS",
    "InitOnceBeginInitialize",
    "InitOnceComplete",
    "InitOnceExecuteOnce",
    "InitOnceInitialize",
    "InitializeConditionVariable",
    "InitializeCriticalSection",
    "InitializeCriticalSectionAndSpinCount",
    "InitializeCriticalSectionEx",
    "InitializeProcThreadAttributeList",
    "InitializeSListHead",
    "InitializeSRWLock",
    "InitializeSynchronizationBarrier",
    "InterlockedFlushSList",
    "InterlockedPopEntrySList",
    "InterlockedPushEntrySList",
    "InterlockedPushListSListEx",
    "IsImmersiveProcess",
    "IsProcessCritical",
    "IsProcessorFeaturePresent",
    "IsThreadAFiber",
    "IsThreadpoolTimerSet",
    "IsWow64Process",
    "IsWow64Process2",
    "LOGON_NETCREDENTIALS_ONLY",
    "LOGON_WITH_PROFILE",
    "LPFIBER_START_ROUTINE",
    "LPPROC_THREAD_ATTRIBUTE_LIST",
    "LPTHREAD_START_ROUTINE",
    "LeaveCriticalSection",
    "LeaveCriticalSectionWhenCallbackReturns",
    "MACHINE_ATTRIBUTES",
    "MACHINE_ATTRIBUTES_KernelEnabled",
    "MACHINE_ATTRIBUTES_UserEnabled",
    "MACHINE_ATTRIBUTES_Wow64Container",
    "MEMORY_PRIORITY",
    "MEMORY_PRIORITY_BELOW_NORMAL",
    "MEMORY_PRIORITY_INFORMATION",
    "MEMORY_PRIORITY_LOW",
    "MEMORY_PRIORITY_MEDIUM",
    "MEMORY_PRIORITY_NORMAL",
    "MEMORY_PRIORITY_VERY_LOW",
    "MUTEX_ALL_ACCESS",
    "MUTEX_MODIFY_STATE",
    "NORMAL_PRIORITY_CLASS",
    "NamespaceHandle",
    "NtQueryInformationProcess",
    "NtQueryInformationThread",
    "NtSetInformationThread",
    "OpenEventA",
    "OpenEventW",
    "OpenMutexW",
    "OpenPrivateNamespaceA",
    "OpenPrivateNamespaceW",
    "OpenProcess",
    "OpenProcessToken",
    "OpenSemaphoreW",
    "OpenThread",
    "OpenThreadToken",
    "OpenWaitableTimerW",
    "PEB",
    "PEB_LDR_DATA",
    "PFLS_CALLBACK_FUNCTION",
    "PF_3DNOW_INSTRUCTIONS_AVAILABLE",
    "PF_ARM_64BIT_LOADSTORE_ATOMIC",
    "PF_ARM_DIVIDE_INSTRUCTION_AVAILABLE",
    "PF_ARM_EXTERNAL_CACHE_AVAILABLE",
    "PF_ARM_FMAC_INSTRUCTIONS_AVAILABLE",
    "PF_ARM_V81_ATOMIC_INSTRUCTIONS_AVAILABLE",
    "PF_ARM_V8_CRC32_INSTRUCTIONS_AVAILABLE",
    "PF_ARM_V8_CRYPTO_INSTRUCTIONS_AVAILABLE",
    "PF_ARM_V8_INSTRUCTIONS_AVAILABLE",
    "PF_ARM_VFP_32_REGISTERS_AVAILABLE",
    "PF_CHANNELS_ENABLED",
    "PF_COMPARE64_EXCHANGE128",
    "PF_COMPARE_EXCHANGE128",
    "PF_COMPARE_EXCHANGE_DOUBLE",
    "PF_FASTFAIL_AVAILABLE",
    "PF_FLOATING_POINT_EMULATED",
    "PF_FLOATING_POINT_PRECISION_ERRATA",
    "PF_MMX_INSTRUCTIONS_AVAILABLE",
    "PF_NX_ENABLED",
    "PF_PAE_ENABLED",
    "PF_RDTSC_INSTRUCTION_AVAILABLE",
    "PF_RDWRFSGSBASE_AVAILABLE",
    "PF_SECOND_LEVEL_ADDRESS_TRANSLATION",
    "PF_SSE3_INSTRUCTIONS_AVAILABLE",
    "PF_VIRT_FIRMWARE_ENABLED",
    "PF_XMMI64_INSTRUCTIONS_AVAILABLE",
    "PF_XMMI_INSTRUCTIONS_AVAILABLE",
    "PF_XSAVE_ENABLED",
    "PINIT_ONCE_FN",
    "PME_CURRENT_VERSION",
    "PME_FAILFAST_ON_COMMIT_FAIL_DISABLE",
    "PME_FAILFAST_ON_COMMIT_FAIL_ENABLE",
    "POWER_REQUEST_CONTEXT_DETAILED_STRING",
    "POWER_REQUEST_CONTEXT_FLAGS",
    "POWER_REQUEST_CONTEXT_SIMPLE_STRING",
    "PPS_POST_PROCESS_INIT_ROUTINE",
    "PRIVATE_NAMESPACE_FLAG_DESTROY",
    "PROCESSINFOCLASS",
    "PROCESSINFOCLASS_ProcessBasicInformation",
    "PROCESSINFOCLASS_ProcessBreakOnTermination",
    "PROCESSINFOCLASS_ProcessDebugPort",
    "PROCESSINFOCLASS_ProcessImageFileName",
    "PROCESSINFOCLASS_ProcessWow64Information",
    "PROCESSOR_FEATURE_ID",
    "PROCESS_ACCESS_RIGHTS",
    "PROCESS_AFFINITY_AUTO_UPDATE_FLAGS",
    "PROCESS_AFFINITY_DISABLE_AUTO_UPDATE",
    "PROCESS_AFFINITY_ENABLE_AUTO_UPDATE",
    "PROCESS_ALL_ACCESS",
    "PROCESS_BASIC_INFORMATION",
    "PROCESS_CREATE_PROCESS",
    "PROCESS_CREATE_THREAD",
    "PROCESS_CREATION_FLAGS",
    "PROCESS_DELETE",
    "PROCESS_DEP_DISABLE_ATL_THUNK_EMULATION",
    "PROCESS_DEP_ENABLE",
    "PROCESS_DEP_FLAGS",
    "PROCESS_DEP_NONE",
    "PROCESS_DUP_HANDLE",
    "PROCESS_DYNAMIC_EH_CONTINUATION_TARGET",
    "PROCESS_DYNAMIC_EH_CONTINUATION_TARGETS_INFORMATION",
    "PROCESS_DYNAMIC_ENFORCED_ADDRESS_RANGE",
    "PROCESS_DYNAMIC_ENFORCED_ADDRESS_RANGES_INFORMATION",
    "PROCESS_INFORMATION",
    "PROCESS_INFORMATION_CLASS",
    "PROCESS_INFORMATION_CLASS_ProcessAppMemoryInfo",
    "PROCESS_INFORMATION_CLASS_ProcessInPrivateInfo",
    "PROCESS_INFORMATION_CLASS_ProcessInformationClassMax",
    "PROCESS_INFORMATION_CLASS_ProcessLeapSecondInfo",
    "PROCESS_INFORMATION_CLASS_ProcessMachineTypeInfo",
    "PROCESS_INFORMATION_CLASS_ProcessMemoryExhaustionInfo",
    "PROCESS_INFORMATION_CLASS_ProcessMemoryPriority",
    "PROCESS_INFORMATION_CLASS_ProcessPowerThrottling",
    "PROCESS_INFORMATION_CLASS_ProcessProtectionLevelInfo",
    "PROCESS_INFORMATION_CLASS_ProcessReservedValue1",
    "PROCESS_INFORMATION_CLASS_ProcessTelemetryCoverageInfo",
    "PROCESS_LEAP_SECOND_INFO",
    "PROCESS_LEAP_SECOND_INFO_FLAG_ENABLE_SIXTY_SECOND",
    "PROCESS_LEAP_SECOND_INFO_VALID_FLAGS",
    "PROCESS_MACHINE_INFORMATION",
    "PROCESS_MEMORY_EXHAUSTION_INFO",
    "PROCESS_MEMORY_EXHAUSTION_TYPE",
    "PROCESS_MEMORY_EXHAUSTION_TYPE_PMETypeFailFastOnCommitFailure",
    "PROCESS_MEMORY_EXHAUSTION_TYPE_PMETypeMax",
    "PROCESS_MITIGATION_POLICY",
    "PROCESS_MITIGATION_POLICY_MaxProcessMitigationPolicy",
    "PROCESS_MITIGATION_POLICY_ProcessASLRPolicy",
    "PROCESS_MITIGATION_POLICY_ProcessChildProcessPolicy",
    "PROCESS_MITIGATION_POLICY_ProcessControlFlowGuardPolicy",
    "PROCESS_MITIGATION_POLICY_ProcessDEPPolicy",
    "PROCESS_MITIGATION_POLICY_ProcessDynamicCodePolicy",
    "PROCESS_MITIGATION_POLICY_ProcessExtensionPointDisablePolicy",
    "PROCESS_MITIGATION_POLICY_ProcessFontDisablePolicy",
    "PROCESS_MITIGATION_POLICY_ProcessImageLoadPolicy",
    "PROCESS_MITIGATION_POLICY_ProcessMitigationOptionsMask",
    "PROCESS_MITIGATION_POLICY_ProcessPayloadRestrictionPolicy",
    "PROCESS_MITIGATION_POLICY_ProcessRedirectionTrustPolicy",
    "PROCESS_MITIGATION_POLICY_ProcessSideChannelIsolationPolicy",
    "PROCESS_MITIGATION_POLICY_ProcessSignaturePolicy",
    "PROCESS_MITIGATION_POLICY_ProcessStrictHandleCheckPolicy",
    "PROCESS_MITIGATION_POLICY_ProcessSystemCallDisablePolicy",
    "PROCESS_MITIGATION_POLICY_ProcessSystemCallFilterPolicy",
    "PROCESS_MITIGATION_POLICY_ProcessUserShadowStackPolicy",
    "PROCESS_MODE_BACKGROUND_BEGIN",
    "PROCESS_MODE_BACKGROUND_END",
    "PROCESS_NAME_FORMAT",
    "PROCESS_NAME_NATIVE",
    "PROCESS_NAME_WIN32",
    "PROCESS_POWER_THROTTLING_CURRENT_VERSION",
    "PROCESS_POWER_THROTTLING_EXECUTION_SPEED",
    "PROCESS_POWER_THROTTLING_IGNORE_TIMER_RESOLUTION",
    "PROCESS_POWER_THROTTLING_STATE",
    "PROCESS_PROTECTION_LEVEL",
    "PROCESS_PROTECTION_LEVEL_INFORMATION",
    "PROCESS_QUERY_INFORMATION",
    "PROCESS_QUERY_LIMITED_INFORMATION",
    "PROCESS_READ_CONTROL",
    "PROCESS_SET_INFORMATION",
    "PROCESS_SET_LIMITED_INFORMATION",
    "PROCESS_SET_QUOTA",
    "PROCESS_SET_SESSIONID",
    "PROCESS_STANDARD_RIGHTS_REQUIRED",
    "PROCESS_SUSPEND_RESUME",
    "PROCESS_SYNCHRONIZE",
    "PROCESS_TERMINATE",
    "PROCESS_VM_OPERATION",
    "PROCESS_VM_READ",
    "PROCESS_VM_WRITE",
    "PROCESS_WRITE_DAC",
    "PROCESS_WRITE_OWNER",
    "PROC_THREAD_ATTRIBUTE_ALL_APPLICATION_PACKAGES_POLICY",
    "PROC_THREAD_ATTRIBUTE_CHILD_PROCESS_POLICY",
    "PROC_THREAD_ATTRIBUTE_COMPONENT_FILTER",
    "PROC_THREAD_ATTRIBUTE_DESKTOP_APP_POLICY",
    "PROC_THREAD_ATTRIBUTE_ENABLE_OPTIONAL_XSTATE_FEATURES",
    "PROC_THREAD_ATTRIBUTE_GROUP_AFFINITY",
    "PROC_THREAD_ATTRIBUTE_HANDLE_LIST",
    "PROC_THREAD_ATTRIBUTE_IDEAL_PROCESSOR",
    "PROC_THREAD_ATTRIBUTE_JOB_LIST",
    "PROC_THREAD_ATTRIBUTE_MACHINE_TYPE",
    "PROC_THREAD_ATTRIBUTE_MITIGATION_AUDIT_POLICY",
    "PROC_THREAD_ATTRIBUTE_MITIGATION_POLICY",
    "PROC_THREAD_ATTRIBUTE_NUM",
    "PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeAllApplicationPackagesPolicy",
    "PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeChildProcessPolicy",
    "PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeComponentFilter",
    "PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeDesktopAppPolicy",
    "PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeEnableOptionalXStateFeatures",
    "PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeGroupAffinity",
    "PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeHandleList",
    "PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeIdealProcessor",
    "PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeJobList",
    "PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeMachineType",
    "PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeMitigationAuditPolicy",
    "PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeMitigationPolicy",
    "PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeParentProcess",
    "PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributePreferredNode",
    "PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeProtectionLevel",
    "PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributePseudoConsole",
    "PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeSafeOpenPromptOriginClaim",
    "PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeSecurityCapabilities",
    "PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeUmsThread",
    "PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeWin32kFilter",
    "PROC_THREAD_ATTRIBUTE_PARENT_PROCESS",
    "PROC_THREAD_ATTRIBUTE_PREFERRED_NODE",
    "PROC_THREAD_ATTRIBUTE_PROTECTION_LEVEL",
    "PROC_THREAD_ATTRIBUTE_PSEUDOCONSOLE",
    "PROC_THREAD_ATTRIBUTE_REPLACE_VALUE",
    "PROC_THREAD_ATTRIBUTE_SECURITY_CAPABILITIES",
    "PROC_THREAD_ATTRIBUTE_UMS_THREAD",
    "PROC_THREAD_ATTRIBUTE_WIN32K_FILTER",
    "PROFILE_KERNEL",
    "PROFILE_SERVER",
    "PROFILE_USER",
    "PROTECTION_LEVEL_ANTIMALWARE_LIGHT",
    "PROTECTION_LEVEL_AUTHENTICODE",
    "PROTECTION_LEVEL_CODEGEN_LIGHT",
    "PROTECTION_LEVEL_LSA_LIGHT",
    "PROTECTION_LEVEL_NONE",
    "PROTECTION_LEVEL_PPL_APP",
    "PROTECTION_LEVEL_WINDOWS",
    "PROTECTION_LEVEL_WINDOWS_LIGHT",
    "PROTECTION_LEVEL_WINTCB",
    "PROTECTION_LEVEL_WINTCB_LIGHT",
    "PRTL_UMS_SCHEDULER_ENTRY_POINT",
    "PTIMERAPCROUTINE",
    "PTP_CLEANUP_GROUP_CANCEL_CALLBACK",
    "PTP_POOL",
    "PTP_SIMPLE_CALLBACK",
    "PTP_TIMER_CALLBACK",
    "PTP_WAIT_CALLBACK",
    "PTP_WIN32_IO_CALLBACK",
    "PTP_WORK_CALLBACK",
    "PulseEvent",
    "QUEUE_USER_APC_FLAGS",
    "QUEUE_USER_APC_FLAGS_NONE",
    "QUEUE_USER_APC_FLAGS_SPECIAL_USER_APC",
    "QueryDepthSList",
    "QueryFullProcessImageNameA",
    "QueryFullProcessImageNameW",
    "QueryProcessAffinityUpdateMode",
    "QueryProtectedPolicy",
    "QueryThreadpoolStackInformation",
    "QueryUmsThreadInformation",
    "QueueUserAPC",
    "QueueUserAPC2",
    "QueueUserWorkItem",
    "REALTIME_PRIORITY_CLASS",
    "REASON_CONTEXT",
    "RTL_BARRIER",
    "RTL_CONDITION_VARIABLE",
    "RTL_CRITICAL_SECTION",
    "RTL_CRITICAL_SECTION_DEBUG",
    "RTL_RUN_ONCE",
    "RTL_SRWLOCK",
    "RTL_UMS_THREAD_INFO_CLASS",
    "RTL_UMS_THREAD_INFO_CLASS_UmsThreadAffinity",
    "RTL_UMS_THREAD_INFO_CLASS_UmsThreadInvalidInfoClass",
    "RTL_UMS_THREAD_INFO_CLASS_UmsThreadIsSuspended",
    "RTL_UMS_THREAD_INFO_CLASS_UmsThreadIsTerminated",
    "RTL_UMS_THREAD_INFO_CLASS_UmsThreadMaxInfoClass",
    "RTL_UMS_THREAD_INFO_CLASS_UmsThreadPriority",
    "RTL_UMS_THREAD_INFO_CLASS_UmsThreadTeb",
    "RTL_UMS_THREAD_INFO_CLASS_UmsThreadUserContext",
    "RTL_USER_PROCESS_PARAMETERS",
    "RegisterWaitForSingleObject",
    "ReleaseMutex",
    "ReleaseMutexWhenCallbackReturns",
    "ReleaseSRWLockExclusive",
    "ReleaseSRWLockShared",
    "ReleaseSemaphore",
    "ReleaseSemaphoreWhenCallbackReturns",
    "ResetEvent",
    "ResumeThread",
    "SEMAPHORE_ALL_ACCESS",
    "SEMAPHORE_MODIFY_STATE",
    "STACK_SIZE_PARAM_IS_A_RESERVATION",
    "STARTF_FORCEOFFFEEDBACK",
    "STARTF_FORCEONFEEDBACK",
    "STARTF_PREVENTPINNING",
    "STARTF_RUNFULLSCREEN",
    "STARTF_TITLEISAPPID",
    "STARTF_TITLEISLINKNAME",
    "STARTF_UNTRUSTEDSOURCE",
    "STARTF_USECOUNTCHARS",
    "STARTF_USEFILLATTRIBUTE",
    "STARTF_USEHOTKEY",
    "STARTF_USEPOSITION",
    "STARTF_USESHOWWINDOW",
    "STARTF_USESIZE",
    "STARTF_USESTDHANDLES",
    "STARTUPINFOA",
    "STARTUPINFOEXA",
    "STARTUPINFOEXW",
    "STARTUPINFOW",
    "STARTUPINFOW_FLAGS",
    "SYNCHRONIZATION_ACCESS_RIGHTS",
    "SYNCHRONIZATION_BARRIER_FLAGS_BLOCK_ONLY",
    "SYNCHRONIZATION_BARRIER_FLAGS_NO_DELETE",
    "SYNCHRONIZATION_BARRIER_FLAGS_SPIN_ONLY",
    "SYNCHRONIZATION_DELETE",
    "SYNCHRONIZATION_READ_CONTROL",
    "SYNCHRONIZATION_SYNCHRONIZE",
    "SYNCHRONIZATION_WRITE_DAC",
    "SYNCHRONIZATION_WRITE_OWNER",
    "SetCriticalSectionSpinCount",
    "SetEvent",
    "SetEventWhenCallbackReturns",
    "SetPriorityClass",
    "SetProcessAffinityMask",
    "SetProcessAffinityUpdateMode",
    "SetProcessDEPPolicy",
    "SetProcessDefaultCpuSetMasks",
    "SetProcessDefaultCpuSets",
    "SetProcessDynamicEHContinuationTargets",
    "SetProcessDynamicEnforcedCetCompatibleRanges",
    "SetProcessInformation",
    "SetProcessMitigationPolicy",
    "SetProcessPriorityBoost",
    "SetProcessRestrictionExemption",
    "SetProcessShutdownParameters",
    "SetProcessWorkingSetSize",
    "SetProtectedPolicy",
    "SetThreadAffinityMask",
    "SetThreadDescription",
    "SetThreadGroupAffinity",
    "SetThreadIdealProcessor",
    "SetThreadIdealProcessorEx",
    "SetThreadInformation",
    "SetThreadPriority",
    "SetThreadPriorityBoost",
    "SetThreadSelectedCpuSetMasks",
    "SetThreadSelectedCpuSets",
    "SetThreadStackGuarantee",
    "SetThreadToken",
    "SetThreadpoolStackInformation",
    "SetThreadpoolThreadMaximum",
    "SetThreadpoolThreadMinimum",
    "SetThreadpoolTimer",
    "SetThreadpoolTimerEx",
    "SetThreadpoolWait",
    "SetThreadpoolWaitEx",
    "SetTimerQueueTimer",
    "SetUmsThreadInformation",
    "SetWaitableTimer",
    "SetWaitableTimerEx",
    "Sleep",
    "SleepConditionVariableCS",
    "SleepConditionVariableSRW",
    "SleepEx",
    "StartThreadpoolIo",
    "SubmitThreadpoolWork",
    "SuspendThread",
    "SwitchToFiber",
    "SwitchToThread",
    "THREADINFOCLASS",
    "THREADINFOCLASS_ThreadIsIoPending",
    "THREADINFOCLASS_ThreadNameInformation",
    "THREAD_ACCESS_RIGHTS",
    "THREAD_ALL_ACCESS",
    "THREAD_CREATE_RUN_IMMEDIATELY",
    "THREAD_CREATE_SUSPENDED",
    "THREAD_CREATION_FLAGS",
    "THREAD_DELETE",
    "THREAD_DIRECT_IMPERSONATION",
    "THREAD_GET_CONTEXT",
    "THREAD_IMPERSONATE",
    "THREAD_INFORMATION_CLASS",
    "THREAD_INFORMATION_CLASS_ThreadAbsoluteCpuPriority",
    "THREAD_INFORMATION_CLASS_ThreadDynamicCodePolicy",
    "THREAD_INFORMATION_CLASS_ThreadInformationClassMax",
    "THREAD_INFORMATION_CLASS_ThreadMemoryPriority",
    "THREAD_INFORMATION_CLASS_ThreadPowerThrottling",
    "THREAD_MODE_BACKGROUND_BEGIN",
    "THREAD_MODE_BACKGROUND_END",
    "THREAD_POWER_THROTTLING_CURRENT_VERSION",
    "THREAD_POWER_THROTTLING_EXECUTION_SPEED",
    "THREAD_POWER_THROTTLING_STATE",
    "THREAD_POWER_THROTTLING_VALID_FLAGS",
    "THREAD_PRIORITY",
    "THREAD_PRIORITY_ABOVE_NORMAL",
    "THREAD_PRIORITY_BELOW_NORMAL",
    "THREAD_PRIORITY_HIGHEST",
    "THREAD_PRIORITY_IDLE",
    "THREAD_PRIORITY_LOWEST",
    "THREAD_PRIORITY_MIN",
    "THREAD_PRIORITY_NORMAL",
    "THREAD_PRIORITY_TIME_CRITICAL",
    "THREAD_QUERY_INFORMATION",
    "THREAD_QUERY_LIMITED_INFORMATION",
    "THREAD_READ_CONTROL",
    "THREAD_RESUME",
    "THREAD_SET_CONTEXT",
    "THREAD_SET_INFORMATION",
    "THREAD_SET_LIMITED_INFORMATION",
    "THREAD_SET_THREAD_TOKEN",
    "THREAD_STANDARD_RIGHTS_REQUIRED",
    "THREAD_SUSPEND_RESUME",
    "THREAD_SYNCHRONIZE",
    "THREAD_TERMINATE",
    "THREAD_WRITE_DAC",
    "THREAD_WRITE_OWNER",
    "TIMER_ALL_ACCESS",
    "TIMER_MODIFY_STATE",
    "TIMER_QUERY_STATE",
    "TLS_OUT_OF_INDEXES",
    "TP_CALLBACK_ENVIRON_V3",
    "TP_CALLBACK_INSTANCE",
    "TP_CALLBACK_PRIORITY",
    "TP_CALLBACK_PRIORITY_COUNT",
    "TP_CALLBACK_PRIORITY_HIGH",
    "TP_CALLBACK_PRIORITY_INVALID",
    "TP_CALLBACK_PRIORITY_LOW",
    "TP_CALLBACK_PRIORITY_NORMAL",
    "TP_IO",
    "TP_POOL_STACK_INFORMATION",
    "TP_TIMER",
    "TP_WAIT",
    "TP_WORK",
    "TerminateProcess",
    "TerminateThread",
    "TimerQueueHandle",
    "TlsAlloc",
    "TlsFree",
    "TlsGetValue",
    "TlsSetValue",
    "TryAcquireSRWLockExclusive",
    "TryAcquireSRWLockShared",
    "TryEnterCriticalSection",
    "TrySubmitThreadpoolCallback",
    "UMS_SCHEDULER_STARTUP_INFO",
    "UMS_SYSTEM_THREAD_INFORMATION",
    "UmsThreadYield",
    "UnregisterWait",
    "UnregisterWaitEx",
    "UpdateProcThreadAttribute",
    "WAITORTIMERCALLBACK",
    "WORKER_THREAD_FLAGS",
    "WT_EXECUTEDEFAULT",
    "WT_EXECUTEINIOTHREAD",
    "WT_EXECUTEINPERSISTENTTHREAD",
    "WT_EXECUTEINTIMERTHREAD",
    "WT_EXECUTEINWAITTHREAD",
    "WT_EXECUTELONGFUNCTION",
    "WT_EXECUTEONLYONCE",
    "WT_TRANSFER_IMPERSONATION",
    "WaitForInputIdle",
    "WaitForMultipleObjects",
    "WaitForMultipleObjectsEx",
    "WaitForSingleObject",
    "WaitForSingleObjectEx",
    "WaitForThreadpoolIoCallbacks",
    "WaitForThreadpoolTimerCallbacks",
    "WaitForThreadpoolWaitCallbacks",
    "WaitForThreadpoolWorkCallbacks",
    "WaitOnAddress",
    "WakeAllConditionVariable",
    "WakeByAddressAll",
    "WakeByAddressSingle",
    "WakeConditionVariable",
    "WinExec",
    "Wow64SetThreadDefaultGuestMachine",
    "Wow64SuspendThread",
]
_arch_optional = [
]
