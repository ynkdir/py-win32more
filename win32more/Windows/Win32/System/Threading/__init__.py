from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Security
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Kernel
import win32more.Windows.Win32.System.SystemInformation
import win32more.Windows.Win32.System.SystemServices
import win32more.Windows.Win32.System.Threading
@winfunctype_pointer
def APC_CALLBACK_FUNCTION(param0: UInt32, param1: VoidPtr, param2: VoidPtr) -> Void: ...
class APP_MEMORY_INFORMATION(Structure):
    AvailableCommit: UInt64
    PrivateCommitUsage: UInt64
    PeakPrivateCommitUsage: UInt64
    TotalCommitUsage: UInt64
AVRT_PRIORITY = Int32
AVRT_PRIORITY_VERYLOW: win32more.Windows.Win32.System.Threading.AVRT_PRIORITY = -2
AVRT_PRIORITY_LOW: win32more.Windows.Win32.System.Threading.AVRT_PRIORITY = -1
AVRT_PRIORITY_NORMAL: win32more.Windows.Win32.System.Threading.AVRT_PRIORITY = 0
AVRT_PRIORITY_HIGH: win32more.Windows.Win32.System.Threading.AVRT_PRIORITY = 1
AVRT_PRIORITY_CRITICAL: win32more.Windows.Win32.System.Threading.AVRT_PRIORITY = 2
CONDITION_VARIABLE_LOCKMODE_SHARED: UInt32 = 1
INIT_ONCE_CHECK_ONLY: UInt32 = 1
INIT_ONCE_ASYNC: UInt32 = 2
INIT_ONCE_INIT_FAILED: UInt32 = 4
INIT_ONCE_CTX_RESERVED_BITS: UInt32 = 2
CONDITION_VARIABLE_INIT: win32more.Windows.Win32.System.Threading.CONDITION_VARIABLE = ConstantLazyLoader(0)
SRWLOCK_INIT: win32more.Windows.Win32.System.Threading.SRWLOCK = ConstantLazyLoader(0)
INIT_ONCE_STATIC_INIT: win32more.Windows.Win32.System.Threading.INIT_ONCE = ConstantLazyLoader(0)
ALL_PROCESSOR_GROUPS: UInt16 = 65535
RTL_CRITICAL_SECTION_FLAG_NO_DEBUG_INFO: UInt32 = 16777216
RTL_CRITICAL_SECTION_FLAG_DYNAMIC_SPIN: UInt32 = 33554432
RTL_CRITICAL_SECTION_FLAG_STATIC_INIT: UInt32 = 67108864
RTL_CRITICAL_SECTION_FLAG_RESOURCE_TYPE: UInt32 = 134217728
RTL_CRITICAL_SECTION_FLAG_FORCE_DEBUG_INFO: UInt32 = 268435456
RTL_CRITICAL_SECTION_ALL_FLAG_BITS: UInt32 = 4278190080
RTL_CRITICAL_SECTION_DEBUG_FLAG_STATIC_INIT: UInt32 = 1
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
CREATE_MUTEX_INITIAL_OWNER: UInt32 = 1
CREATE_WAITABLE_TIMER_MANUAL_RESET: UInt32 = 1
CREATE_WAITABLE_TIMER_HIGH_RESOLUTION: UInt32 = 2
SYNCHRONIZATION_BARRIER_FLAGS_SPIN_ONLY: UInt32 = 1
SYNCHRONIZATION_BARRIER_FLAGS_BLOCK_ONLY: UInt32 = 2
SYNCHRONIZATION_BARRIER_FLAGS_NO_DELETE: UInt32 = 4
INFINITE: UInt32 = 4294967295
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
def GetCurrentProcessToken() -> win32more.Windows.Win32.Foundation.HANDLE:
    return -4
def GetCurrentThreadToken() -> win32more.Windows.Win32.Foundation.HANDLE:
    return -5
def GetCurrentThreadEffectiveToken() -> win32more.Windows.Win32.Foundation.HANDLE:
    return -6
@winfunctype('KERNEL32.dll')
def GetProcessWorkingSetSize(hProcess: win32more.Windows.Win32.Foundation.HANDLE, lpMinimumWorkingSetSize: POINTER(UIntPtr), lpMaximumWorkingSetSize: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetProcessWorkingSetSize(hProcess: win32more.Windows.Win32.Foundation.HANDLE, dwMinimumWorkingSetSize: UIntPtr, dwMaximumWorkingSetSize: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FlsAlloc(lpCallback: win32more.Windows.Win32.System.Threading.PFLS_CALLBACK_FUNCTION) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def FlsGetValue(dwFlsIndex: UInt32) -> VoidPtr: ...
@winfunctype('KERNEL32.dll')
def FlsSetValue(dwFlsIndex: UInt32, lpFlsData: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FlsFree(dwFlsIndex: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def IsThreadAFiber() -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def InitializeSRWLock(SRWLock: POINTER(win32more.Windows.Win32.System.Threading.SRWLOCK)) -> Void: ...
@winfunctype('KERNEL32.dll')
def ReleaseSRWLockExclusive(SRWLock: POINTER(win32more.Windows.Win32.System.Threading.SRWLOCK)) -> Void: ...
@winfunctype('KERNEL32.dll')
def ReleaseSRWLockShared(SRWLock: POINTER(win32more.Windows.Win32.System.Threading.SRWLOCK)) -> Void: ...
@winfunctype('KERNEL32.dll')
def AcquireSRWLockExclusive(SRWLock: POINTER(win32more.Windows.Win32.System.Threading.SRWLOCK)) -> Void: ...
@winfunctype('KERNEL32.dll')
def AcquireSRWLockShared(SRWLock: POINTER(win32more.Windows.Win32.System.Threading.SRWLOCK)) -> Void: ...
@winfunctype('KERNEL32.dll')
def TryAcquireSRWLockExclusive(SRWLock: POINTER(win32more.Windows.Win32.System.Threading.SRWLOCK)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('KERNEL32.dll')
def TryAcquireSRWLockShared(SRWLock: POINTER(win32more.Windows.Win32.System.Threading.SRWLOCK)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('KERNEL32.dll')
def InitializeCriticalSection(lpCriticalSection: POINTER(win32more.Windows.Win32.System.Threading.CRITICAL_SECTION)) -> Void: ...
@winfunctype('KERNEL32.dll')
def EnterCriticalSection(lpCriticalSection: POINTER(win32more.Windows.Win32.System.Threading.CRITICAL_SECTION)) -> Void: ...
@winfunctype('KERNEL32.dll')
def LeaveCriticalSection(lpCriticalSection: POINTER(win32more.Windows.Win32.System.Threading.CRITICAL_SECTION)) -> Void: ...
@winfunctype('KERNEL32.dll')
def InitializeCriticalSectionAndSpinCount(lpCriticalSection: POINTER(win32more.Windows.Win32.System.Threading.CRITICAL_SECTION), dwSpinCount: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def InitializeCriticalSectionEx(lpCriticalSection: POINTER(win32more.Windows.Win32.System.Threading.CRITICAL_SECTION), dwSpinCount: UInt32, Flags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetCriticalSectionSpinCount(lpCriticalSection: POINTER(win32more.Windows.Win32.System.Threading.CRITICAL_SECTION), dwSpinCount: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def TryEnterCriticalSection(lpCriticalSection: POINTER(win32more.Windows.Win32.System.Threading.CRITICAL_SECTION)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DeleteCriticalSection(lpCriticalSection: POINTER(win32more.Windows.Win32.System.Threading.CRITICAL_SECTION)) -> Void: ...
@winfunctype('KERNEL32.dll')
def InitOnceInitialize(InitOnce: POINTER(win32more.Windows.Win32.System.Threading.INIT_ONCE)) -> Void: ...
@winfunctype('KERNEL32.dll')
def InitOnceExecuteOnce(InitOnce: POINTER(win32more.Windows.Win32.System.Threading.INIT_ONCE), InitFn: win32more.Windows.Win32.System.Threading.PINIT_ONCE_FN, Parameter: VoidPtr, Context: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def InitOnceBeginInitialize(lpInitOnce: POINTER(win32more.Windows.Win32.System.Threading.INIT_ONCE), dwFlags: UInt32, fPending: POINTER(win32more.Windows.Win32.Foundation.BOOL), lpContext: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def InitOnceComplete(lpInitOnce: POINTER(win32more.Windows.Win32.System.Threading.INIT_ONCE), dwFlags: UInt32, lpContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def InitializeConditionVariable(ConditionVariable: POINTER(win32more.Windows.Win32.System.Threading.CONDITION_VARIABLE)) -> Void: ...
@winfunctype('KERNEL32.dll')
def WakeConditionVariable(ConditionVariable: POINTER(win32more.Windows.Win32.System.Threading.CONDITION_VARIABLE)) -> Void: ...
@winfunctype('KERNEL32.dll')
def WakeAllConditionVariable(ConditionVariable: POINTER(win32more.Windows.Win32.System.Threading.CONDITION_VARIABLE)) -> Void: ...
@winfunctype('KERNEL32.dll')
def SleepConditionVariableCS(ConditionVariable: POINTER(win32more.Windows.Win32.System.Threading.CONDITION_VARIABLE), CriticalSection: POINTER(win32more.Windows.Win32.System.Threading.CRITICAL_SECTION), dwMilliseconds: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SleepConditionVariableSRW(ConditionVariable: POINTER(win32more.Windows.Win32.System.Threading.CONDITION_VARIABLE), SRWLock: POINTER(win32more.Windows.Win32.System.Threading.SRWLOCK), dwMilliseconds: UInt32, Flags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetEvent(hEvent: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ResetEvent(hEvent: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ReleaseSemaphore(hSemaphore: win32more.Windows.Win32.Foundation.HANDLE, lReleaseCount: Int32, lpPreviousCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ReleaseMutex(hMutex: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WaitForSingleObject(hHandle: win32more.Windows.Win32.Foundation.HANDLE, dwMilliseconds: UInt32) -> win32more.Windows.Win32.Foundation.WAIT_EVENT: ...
@winfunctype('KERNEL32.dll')
def SleepEx(dwMilliseconds: UInt32, bAlertable: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def WaitForSingleObjectEx(hHandle: win32more.Windows.Win32.Foundation.HANDLE, dwMilliseconds: UInt32, bAlertable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.WAIT_EVENT: ...
@winfunctype('KERNEL32.dll')
def WaitForMultipleObjectsEx(nCount: UInt32, lpHandles: POINTER(win32more.Windows.Win32.Foundation.HANDLE), bWaitAll: win32more.Windows.Win32.Foundation.BOOL, dwMilliseconds: UInt32, bAlertable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.WAIT_EVENT: ...
@winfunctype('KERNEL32.dll')
def CreateMutexA(lpMutexAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), bInitialOwner: win32more.Windows.Win32.Foundation.BOOL, lpName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def CreateMutexW(lpMutexAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), bInitialOwner: win32more.Windows.Win32.Foundation.BOOL, lpName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
CreateMutex = UnicodeAlias('CreateMutexW')
@winfunctype('KERNEL32.dll')
def OpenMutexW(dwDesiredAccess: win32more.Windows.Win32.System.Threading.SYNCHRONIZATION_ACCESS_RIGHTS, bInheritHandle: win32more.Windows.Win32.Foundation.BOOL, lpName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
OpenMutex = UnicodeAlias('OpenMutexW')
@winfunctype('KERNEL32.dll')
def CreateEventA(lpEventAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), bManualReset: win32more.Windows.Win32.Foundation.BOOL, bInitialState: win32more.Windows.Win32.Foundation.BOOL, lpName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def CreateEventW(lpEventAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), bManualReset: win32more.Windows.Win32.Foundation.BOOL, bInitialState: win32more.Windows.Win32.Foundation.BOOL, lpName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
CreateEvent = UnicodeAlias('CreateEventW')
@winfunctype('KERNEL32.dll')
def OpenEventA(dwDesiredAccess: win32more.Windows.Win32.System.Threading.SYNCHRONIZATION_ACCESS_RIGHTS, bInheritHandle: win32more.Windows.Win32.Foundation.BOOL, lpName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def OpenEventW(dwDesiredAccess: win32more.Windows.Win32.System.Threading.SYNCHRONIZATION_ACCESS_RIGHTS, bInheritHandle: win32more.Windows.Win32.Foundation.BOOL, lpName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
OpenEvent = UnicodeAlias('OpenEventW')
@winfunctype('KERNEL32.dll')
def OpenSemaphoreW(dwDesiredAccess: win32more.Windows.Win32.System.Threading.SYNCHRONIZATION_ACCESS_RIGHTS, bInheritHandle: win32more.Windows.Win32.Foundation.BOOL, lpName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
OpenSemaphore = UnicodeAlias('OpenSemaphoreW')
@winfunctype('KERNEL32.dll')
def OpenWaitableTimerW(dwDesiredAccess: win32more.Windows.Win32.System.Threading.SYNCHRONIZATION_ACCESS_RIGHTS, bInheritHandle: win32more.Windows.Win32.Foundation.BOOL, lpTimerName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
OpenWaitableTimer = UnicodeAlias('OpenWaitableTimerW')
@winfunctype('KERNEL32.dll')
def SetWaitableTimerEx(hTimer: win32more.Windows.Win32.Foundation.HANDLE, lpDueTime: POINTER(Int64), lPeriod: Int32, pfnCompletionRoutine: win32more.Windows.Win32.System.Threading.PTIMERAPCROUTINE, lpArgToCompletionRoutine: VoidPtr, WakeContext: POINTER(win32more.Windows.Win32.System.Threading.REASON_CONTEXT), TolerableDelay: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetWaitableTimer(hTimer: win32more.Windows.Win32.Foundation.HANDLE, lpDueTime: POINTER(Int64), lPeriod: Int32, pfnCompletionRoutine: win32more.Windows.Win32.System.Threading.PTIMERAPCROUTINE, lpArgToCompletionRoutine: VoidPtr, fResume: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CancelWaitableTimer(hTimer: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateMutexExA(lpMutexAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), lpName: win32more.Windows.Win32.Foundation.PSTR, dwFlags: UInt32, dwDesiredAccess: UInt32) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def CreateMutexExW(lpMutexAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), lpName: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, dwDesiredAccess: UInt32) -> win32more.Windows.Win32.Foundation.HANDLE: ...
CreateMutexEx = UnicodeAlias('CreateMutexExW')
@winfunctype('KERNEL32.dll')
def CreateEventExA(lpEventAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), lpName: win32more.Windows.Win32.Foundation.PSTR, dwFlags: win32more.Windows.Win32.System.Threading.CREATE_EVENT, dwDesiredAccess: UInt32) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def CreateEventExW(lpEventAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), lpName: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: win32more.Windows.Win32.System.Threading.CREATE_EVENT, dwDesiredAccess: UInt32) -> win32more.Windows.Win32.Foundation.HANDLE: ...
CreateEventEx = UnicodeAlias('CreateEventExW')
@winfunctype('KERNEL32.dll')
def CreateSemaphoreExW(lpSemaphoreAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), lInitialCount: Int32, lMaximumCount: Int32, lpName: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, dwDesiredAccess: UInt32) -> win32more.Windows.Win32.Foundation.HANDLE: ...
CreateSemaphoreEx = UnicodeAlias('CreateSemaphoreExW')
@winfunctype('KERNEL32.dll')
def CreateWaitableTimerExW(lpTimerAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), lpTimerName: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, dwDesiredAccess: UInt32) -> win32more.Windows.Win32.Foundation.HANDLE: ...
CreateWaitableTimerEx = UnicodeAlias('CreateWaitableTimerExW')
@winfunctype('KERNEL32.dll')
def EnterSynchronizationBarrier(lpBarrier: POINTER(win32more.Windows.Win32.System.Threading.SYNCHRONIZATION_BARRIER), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def InitializeSynchronizationBarrier(lpBarrier: POINTER(win32more.Windows.Win32.System.Threading.SYNCHRONIZATION_BARRIER), lTotalThreads: Int32, lSpinCount: Int32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DeleteSynchronizationBarrier(lpBarrier: POINTER(win32more.Windows.Win32.System.Threading.SYNCHRONIZATION_BARRIER)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def Sleep(dwMilliseconds: UInt32) -> Void: ...
@winfunctype('api-ms-win-core-synch-l1-2-0.dll')
def WaitOnAddress(Address: VoidPtr, CompareAddress: VoidPtr, AddressSize: UIntPtr, dwMilliseconds: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-synch-l1-2-0.dll')
def WakeByAddressSingle(Address: VoidPtr) -> Void: ...
@winfunctype('api-ms-win-core-synch-l1-2-0.dll')
def WakeByAddressAll(Address: VoidPtr) -> Void: ...
@winfunctype('KERNEL32.dll')
def WaitForMultipleObjects(nCount: UInt32, lpHandles: POINTER(win32more.Windows.Win32.Foundation.HANDLE), bWaitAll: win32more.Windows.Win32.Foundation.BOOL, dwMilliseconds: UInt32) -> win32more.Windows.Win32.Foundation.WAIT_EVENT: ...
@winfunctype('KERNEL32.dll')
def CreateSemaphoreW(lpSemaphoreAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), lInitialCount: Int32, lMaximumCount: Int32, lpName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
CreateSemaphore = UnicodeAlias('CreateSemaphoreW')
@winfunctype('KERNEL32.dll')
def CreateWaitableTimerW(lpTimerAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), bManualReset: win32more.Windows.Win32.Foundation.BOOL, lpTimerName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
CreateWaitableTimer = UnicodeAlias('CreateWaitableTimerW')
@winfunctype('KERNEL32.dll')
def InitializeSListHead(ListHead: POINTER(win32more.Windows.Win32.System.Kernel.SLIST_HEADER)) -> Void: ...
@winfunctype('KERNEL32.dll')
def InterlockedPopEntrySList(ListHead: POINTER(win32more.Windows.Win32.System.Kernel.SLIST_HEADER)) -> POINTER(win32more.Windows.Win32.System.Kernel.SLIST_ENTRY): ...
@winfunctype('KERNEL32.dll')
def InterlockedPushEntrySList(ListHead: POINTER(win32more.Windows.Win32.System.Kernel.SLIST_HEADER), ListEntry: POINTER(win32more.Windows.Win32.System.Kernel.SLIST_ENTRY)) -> POINTER(win32more.Windows.Win32.System.Kernel.SLIST_ENTRY): ...
@winfunctype('KERNEL32.dll')
def InterlockedPushListSListEx(ListHead: POINTER(win32more.Windows.Win32.System.Kernel.SLIST_HEADER), List: POINTER(win32more.Windows.Win32.System.Kernel.SLIST_ENTRY), ListEnd: POINTER(win32more.Windows.Win32.System.Kernel.SLIST_ENTRY), Count: UInt32) -> POINTER(win32more.Windows.Win32.System.Kernel.SLIST_ENTRY): ...
@winfunctype('KERNEL32.dll')
def InterlockedFlushSList(ListHead: POINTER(win32more.Windows.Win32.System.Kernel.SLIST_HEADER)) -> POINTER(win32more.Windows.Win32.System.Kernel.SLIST_ENTRY): ...
@winfunctype('KERNEL32.dll')
def QueryDepthSList(ListHead: POINTER(win32more.Windows.Win32.System.Kernel.SLIST_HEADER)) -> UInt16: ...
@winfunctype('KERNEL32.dll')
def QueueUserAPC(pfnAPC: win32more.Windows.Win32.Foundation.PAPCFUNC, hThread: win32more.Windows.Win32.Foundation.HANDLE, dwData: UIntPtr) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def QueueUserAPC2(ApcRoutine: win32more.Windows.Win32.Foundation.PAPCFUNC, Thread: win32more.Windows.Win32.Foundation.HANDLE, Data: UIntPtr, Flags: win32more.Windows.Win32.System.Threading.QUEUE_USER_APC_FLAGS) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetProcessTimes(hProcess: win32more.Windows.Win32.Foundation.HANDLE, lpCreationTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME), lpExitTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME), lpKernelTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME), lpUserTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetCurrentProcess() -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def GetCurrentProcessId() -> UInt32: ...
@winfunctype('KERNEL32.dll')
def ExitProcess(uExitCode: UInt32) -> Void: ...
@winfunctype('KERNEL32.dll')
def TerminateProcess(hProcess: win32more.Windows.Win32.Foundation.HANDLE, uExitCode: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetExitCodeProcess(hProcess: win32more.Windows.Win32.Foundation.HANDLE, lpExitCode: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SwitchToThread() -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateThread(lpThreadAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), dwStackSize: UIntPtr, lpStartAddress: win32more.Windows.Win32.System.Threading.LPTHREAD_START_ROUTINE, lpParameter: VoidPtr, dwCreationFlags: win32more.Windows.Win32.System.Threading.THREAD_CREATION_FLAGS, lpThreadId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def CreateRemoteThread(hProcess: win32more.Windows.Win32.Foundation.HANDLE, lpThreadAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), dwStackSize: UIntPtr, lpStartAddress: win32more.Windows.Win32.System.Threading.LPTHREAD_START_ROUTINE, lpParameter: VoidPtr, dwCreationFlags: UInt32, lpThreadId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def GetCurrentThread() -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def GetCurrentThreadId() -> UInt32: ...
@winfunctype('KERNEL32.dll')
def OpenThread(dwDesiredAccess: win32more.Windows.Win32.System.Threading.THREAD_ACCESS_RIGHTS, bInheritHandle: win32more.Windows.Win32.Foundation.BOOL, dwThreadId: UInt32) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def SetThreadPriority(hThread: win32more.Windows.Win32.Foundation.HANDLE, nPriority: win32more.Windows.Win32.System.Threading.THREAD_PRIORITY) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetThreadPriorityBoost(hThread: win32more.Windows.Win32.Foundation.HANDLE, bDisablePriorityBoost: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetThreadPriorityBoost(hThread: win32more.Windows.Win32.Foundation.HANDLE, pDisablePriorityBoost: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetThreadPriority(hThread: win32more.Windows.Win32.Foundation.HANDLE) -> Int32: ...
@winfunctype('KERNEL32.dll')
def ExitThread(dwExitCode: UInt32) -> Void: ...
@winfunctype('KERNEL32.dll')
def TerminateThread(hThread: win32more.Windows.Win32.Foundation.HANDLE, dwExitCode: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetExitCodeThread(hThread: win32more.Windows.Win32.Foundation.HANDLE, lpExitCode: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SuspendThread(hThread: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def ResumeThread(hThread: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def TlsAlloc() -> UInt32: ...
@winfunctype('KERNEL32.dll')
def TlsGetValue(dwTlsIndex: UInt32) -> VoidPtr: ...
@winfunctype('KERNEL32.dll')
def TlsSetValue(dwTlsIndex: UInt32, lpTlsValue: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def TlsFree(dwTlsIndex: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateProcessA(lpApplicationName: win32more.Windows.Win32.Foundation.PSTR, lpCommandLine: win32more.Windows.Win32.Foundation.PSTR, lpProcessAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), lpThreadAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), bInheritHandles: win32more.Windows.Win32.Foundation.BOOL, dwCreationFlags: win32more.Windows.Win32.System.Threading.PROCESS_CREATION_FLAGS, lpEnvironment: VoidPtr, lpCurrentDirectory: win32more.Windows.Win32.Foundation.PSTR, lpStartupInfo: POINTER(win32more.Windows.Win32.System.Threading.STARTUPINFOA), lpProcessInformation: POINTER(win32more.Windows.Win32.System.Threading.PROCESS_INFORMATION)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateProcessW(lpApplicationName: win32more.Windows.Win32.Foundation.PWSTR, lpCommandLine: win32more.Windows.Win32.Foundation.PWSTR, lpProcessAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), lpThreadAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), bInheritHandles: win32more.Windows.Win32.Foundation.BOOL, dwCreationFlags: win32more.Windows.Win32.System.Threading.PROCESS_CREATION_FLAGS, lpEnvironment: VoidPtr, lpCurrentDirectory: win32more.Windows.Win32.Foundation.PWSTR, lpStartupInfo: POINTER(win32more.Windows.Win32.System.Threading.STARTUPINFOW), lpProcessInformation: POINTER(win32more.Windows.Win32.System.Threading.PROCESS_INFORMATION)) -> win32more.Windows.Win32.Foundation.BOOL: ...
CreateProcess = UnicodeAlias('CreateProcessW')
@winfunctype('KERNEL32.dll')
def SetProcessShutdownParameters(dwLevel: UInt32, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetProcessVersion(ProcessId: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetStartupInfoW(lpStartupInfo: POINTER(win32more.Windows.Win32.System.Threading.STARTUPINFOW)) -> Void: ...
GetStartupInfo = UnicodeAlias('GetStartupInfoW')
@winfunctype('ADVAPI32.dll')
def CreateProcessAsUserW(hToken: win32more.Windows.Win32.Foundation.HANDLE, lpApplicationName: win32more.Windows.Win32.Foundation.PWSTR, lpCommandLine: win32more.Windows.Win32.Foundation.PWSTR, lpProcessAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), lpThreadAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), bInheritHandles: win32more.Windows.Win32.Foundation.BOOL, dwCreationFlags: win32more.Windows.Win32.System.Threading.PROCESS_CREATION_FLAGS, lpEnvironment: VoidPtr, lpCurrentDirectory: win32more.Windows.Win32.Foundation.PWSTR, lpStartupInfo: POINTER(win32more.Windows.Win32.System.Threading.STARTUPINFOW), lpProcessInformation: POINTER(win32more.Windows.Win32.System.Threading.PROCESS_INFORMATION)) -> win32more.Windows.Win32.Foundation.BOOL: ...
CreateProcessAsUser = UnicodeAlias('CreateProcessAsUserW')
@winfunctype('ADVAPI32.dll')
def SetThreadToken(Thread: POINTER(win32more.Windows.Win32.Foundation.HANDLE), Token: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def OpenProcessToken(ProcessHandle: win32more.Windows.Win32.Foundation.HANDLE, DesiredAccess: win32more.Windows.Win32.Security.TOKEN_ACCESS_MASK, TokenHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def OpenThreadToken(ThreadHandle: win32more.Windows.Win32.Foundation.HANDLE, DesiredAccess: win32more.Windows.Win32.Security.TOKEN_ACCESS_MASK, OpenAsSelf: win32more.Windows.Win32.Foundation.BOOL, TokenHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetPriorityClass(hProcess: win32more.Windows.Win32.Foundation.HANDLE, dwPriorityClass: win32more.Windows.Win32.System.Threading.PROCESS_CREATION_FLAGS) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetPriorityClass(hProcess: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def SetThreadStackGuarantee(StackSizeInBytes: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetProcessId(Process: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetThreadId(Thread: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def FlushProcessWriteBuffers() -> Void: ...
@winfunctype('KERNEL32.dll')
def GetProcessIdOfThread(Thread: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def InitializeProcThreadAttributeList(lpAttributeList: win32more.Windows.Win32.System.Threading.LPPROC_THREAD_ATTRIBUTE_LIST, dwAttributeCount: UInt32, dwFlags: UInt32, lpSize: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DeleteProcThreadAttributeList(lpAttributeList: win32more.Windows.Win32.System.Threading.LPPROC_THREAD_ATTRIBUTE_LIST) -> Void: ...
@winfunctype('KERNEL32.dll')
def UpdateProcThreadAttribute(lpAttributeList: win32more.Windows.Win32.System.Threading.LPPROC_THREAD_ATTRIBUTE_LIST, dwFlags: UInt32, Attribute: UIntPtr, lpValue: VoidPtr, cbSize: UIntPtr, lpPreviousValue: VoidPtr, lpReturnSize: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetProcessDynamicEHContinuationTargets(Process: win32more.Windows.Win32.Foundation.HANDLE, NumberOfTargets: UInt16, Targets: POINTER(win32more.Windows.Win32.System.Threading.PROCESS_DYNAMIC_EH_CONTINUATION_TARGET)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetProcessDynamicEnforcedCetCompatibleRanges(Process: win32more.Windows.Win32.Foundation.HANDLE, NumberOfRanges: UInt16, Ranges: POINTER(win32more.Windows.Win32.System.Threading.PROCESS_DYNAMIC_ENFORCED_ADDRESS_RANGE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetProcessAffinityUpdateMode(hProcess: win32more.Windows.Win32.Foundation.HANDLE, dwFlags: win32more.Windows.Win32.System.Threading.PROCESS_AFFINITY_AUTO_UPDATE_FLAGS) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def QueryProcessAffinityUpdateMode(hProcess: win32more.Windows.Win32.Foundation.HANDLE, lpdwFlags: POINTER(win32more.Windows.Win32.System.Threading.PROCESS_AFFINITY_AUTO_UPDATE_FLAGS)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateRemoteThreadEx(hProcess: win32more.Windows.Win32.Foundation.HANDLE, lpThreadAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), dwStackSize: UIntPtr, lpStartAddress: win32more.Windows.Win32.System.Threading.LPTHREAD_START_ROUTINE, lpParameter: VoidPtr, dwCreationFlags: UInt32, lpAttributeList: win32more.Windows.Win32.System.Threading.LPPROC_THREAD_ATTRIBUTE_LIST, lpThreadId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def GetCurrentThreadStackLimits(LowLimit: POINTER(UIntPtr), HighLimit: POINTER(UIntPtr)) -> Void: ...
@winfunctype('KERNEL32.dll')
def GetProcessMitigationPolicy(hProcess: win32more.Windows.Win32.Foundation.HANDLE, MitigationPolicy: win32more.Windows.Win32.System.Threading.PROCESS_MITIGATION_POLICY, lpBuffer: VoidPtr, dwLength: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetProcessMitigationPolicy(MitigationPolicy: win32more.Windows.Win32.System.Threading.PROCESS_MITIGATION_POLICY, lpBuffer: VoidPtr, dwLength: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetThreadTimes(hThread: win32more.Windows.Win32.Foundation.HANDLE, lpCreationTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME), lpExitTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME), lpKernelTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME), lpUserTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def OpenProcess(dwDesiredAccess: win32more.Windows.Win32.System.Threading.PROCESS_ACCESS_RIGHTS, bInheritHandle: win32more.Windows.Win32.Foundation.BOOL, dwProcessId: UInt32) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def IsProcessorFeaturePresent(ProcessorFeature: win32more.Windows.Win32.System.Threading.PROCESSOR_FEATURE_ID) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetProcessHandleCount(hProcess: win32more.Windows.Win32.Foundation.HANDLE, pdwHandleCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetCurrentProcessorNumber() -> UInt32: ...
@winfunctype('KERNEL32.dll')
def SetThreadIdealProcessorEx(hThread: win32more.Windows.Win32.Foundation.HANDLE, lpIdealProcessor: POINTER(win32more.Windows.Win32.System.Kernel.PROCESSOR_NUMBER), lpPreviousIdealProcessor: POINTER(win32more.Windows.Win32.System.Kernel.PROCESSOR_NUMBER)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetThreadIdealProcessorEx(hThread: win32more.Windows.Win32.Foundation.HANDLE, lpIdealProcessor: POINTER(win32more.Windows.Win32.System.Kernel.PROCESSOR_NUMBER)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetCurrentProcessorNumberEx(ProcNumber: POINTER(win32more.Windows.Win32.System.Kernel.PROCESSOR_NUMBER)) -> Void: ...
@winfunctype('KERNEL32.dll')
def GetProcessPriorityBoost(hProcess: win32more.Windows.Win32.Foundation.HANDLE, pDisablePriorityBoost: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetProcessPriorityBoost(hProcess: win32more.Windows.Win32.Foundation.HANDLE, bDisablePriorityBoost: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetThreadIOPendingFlag(hThread: win32more.Windows.Win32.Foundation.HANDLE, lpIOIsPending: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetSystemTimes(lpIdleTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME), lpKernelTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME), lpUserTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetThreadInformation(hThread: win32more.Windows.Win32.Foundation.HANDLE, ThreadInformationClass: win32more.Windows.Win32.System.Threading.THREAD_INFORMATION_CLASS, ThreadInformation: VoidPtr, ThreadInformationSize: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetThreadInformation(hThread: win32more.Windows.Win32.Foundation.HANDLE, ThreadInformationClass: win32more.Windows.Win32.System.Threading.THREAD_INFORMATION_CLASS, ThreadInformation: VoidPtr, ThreadInformationSize: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def IsProcessCritical(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Critical: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetProtectedPolicy(PolicyGuid: POINTER(Guid), PolicyValue: UIntPtr, OldPolicyValue: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def QueryProtectedPolicy(PolicyGuid: POINTER(Guid), PolicyValue: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetThreadIdealProcessor(hThread: win32more.Windows.Win32.Foundation.HANDLE, dwIdealProcessor: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def SetProcessInformation(hProcess: win32more.Windows.Win32.Foundation.HANDLE, ProcessInformationClass: win32more.Windows.Win32.System.Threading.PROCESS_INFORMATION_CLASS, ProcessInformation: VoidPtr, ProcessInformationSize: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetProcessInformation(hProcess: win32more.Windows.Win32.Foundation.HANDLE, ProcessInformationClass: win32more.Windows.Win32.System.Threading.PROCESS_INFORMATION_CLASS, ProcessInformation: VoidPtr, ProcessInformationSize: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetProcessDefaultCpuSets(Process: win32more.Windows.Win32.Foundation.HANDLE, CpuSetIds: POINTER(UInt32), CpuSetIdCount: UInt32, RequiredIdCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetProcessDefaultCpuSets(Process: win32more.Windows.Win32.Foundation.HANDLE, CpuSetIds: POINTER(UInt32), CpuSetIdCount: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetThreadSelectedCpuSets(Thread: win32more.Windows.Win32.Foundation.HANDLE, CpuSetIds: POINTER(UInt32), CpuSetIdCount: UInt32, RequiredIdCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetThreadSelectedCpuSets(Thread: win32more.Windows.Win32.Foundation.HANDLE, CpuSetIds: POINTER(UInt32), CpuSetIdCount: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CreateProcessAsUserA(hToken: win32more.Windows.Win32.Foundation.HANDLE, lpApplicationName: win32more.Windows.Win32.Foundation.PSTR, lpCommandLine: win32more.Windows.Win32.Foundation.PSTR, lpProcessAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), lpThreadAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), bInheritHandles: win32more.Windows.Win32.Foundation.BOOL, dwCreationFlags: win32more.Windows.Win32.System.Threading.PROCESS_CREATION_FLAGS, lpEnvironment: VoidPtr, lpCurrentDirectory: win32more.Windows.Win32.Foundation.PSTR, lpStartupInfo: POINTER(win32more.Windows.Win32.System.Threading.STARTUPINFOA), lpProcessInformation: POINTER(win32more.Windows.Win32.System.Threading.PROCESS_INFORMATION)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetProcessShutdownParameters(lpdwLevel: POINTER(UInt32), lpdwFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetProcessDefaultCpuSetMasks(Process: win32more.Windows.Win32.Foundation.HANDLE, CpuSetMasks: POINTER(win32more.Windows.Win32.System.SystemInformation.GROUP_AFFINITY), CpuSetMaskCount: UInt16, RequiredMaskCount: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetProcessDefaultCpuSetMasks(Process: win32more.Windows.Win32.Foundation.HANDLE, CpuSetMasks: POINTER(win32more.Windows.Win32.System.SystemInformation.GROUP_AFFINITY), CpuSetMaskCount: UInt16) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetThreadSelectedCpuSetMasks(Thread: win32more.Windows.Win32.Foundation.HANDLE, CpuSetMasks: POINTER(win32more.Windows.Win32.System.SystemInformation.GROUP_AFFINITY), CpuSetMaskCount: UInt16, RequiredMaskCount: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetThreadSelectedCpuSetMasks(Thread: win32more.Windows.Win32.Foundation.HANDLE, CpuSetMasks: POINTER(win32more.Windows.Win32.System.SystemInformation.GROUP_AFFINITY), CpuSetMaskCount: UInt16) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetMachineTypeAttributes(Machine: UInt16, MachineTypeAttributes: POINTER(win32more.Windows.Win32.System.Threading.MACHINE_ATTRIBUTES)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def SetThreadDescription(hThread: win32more.Windows.Win32.Foundation.HANDLE, lpThreadDescription: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def GetThreadDescription(hThread: win32more.Windows.Win32.Foundation.HANDLE, ppszThreadDescription: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def QueueUserWorkItem(Function: win32more.Windows.Win32.System.Threading.LPTHREAD_START_ROUTINE, Context: VoidPtr, Flags: win32more.Windows.Win32.System.Threading.WORKER_THREAD_FLAGS) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def UnregisterWaitEx(WaitHandle: win32more.Windows.Win32.Foundation.HANDLE, CompletionEvent: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateTimerQueue() -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def CreateTimerQueueTimer(phNewTimer: POINTER(win32more.Windows.Win32.Foundation.HANDLE), TimerQueue: win32more.Windows.Win32.Foundation.HANDLE, Callback: win32more.Windows.Win32.System.Threading.WAITORTIMERCALLBACK, Parameter: VoidPtr, DueTime: UInt32, Period: UInt32, Flags: win32more.Windows.Win32.System.Threading.WORKER_THREAD_FLAGS) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ChangeTimerQueueTimer(TimerQueue: win32more.Windows.Win32.Foundation.HANDLE, Timer: win32more.Windows.Win32.Foundation.HANDLE, DueTime: UInt32, Period: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DeleteTimerQueueTimer(TimerQueue: win32more.Windows.Win32.Foundation.HANDLE, Timer: win32more.Windows.Win32.Foundation.HANDLE, CompletionEvent: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DeleteTimerQueue(TimerQueue: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DeleteTimerQueueEx(TimerQueue: win32more.Windows.Win32.Foundation.HANDLE, CompletionEvent: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateThreadpool(reserved: VoidPtr) -> win32more.Windows.Win32.System.Threading.PTP_POOL: ...
@winfunctype('KERNEL32.dll')
def SetThreadpoolThreadMaximum(ptpp: win32more.Windows.Win32.System.Threading.PTP_POOL, cthrdMost: UInt32) -> Void: ...
@winfunctype('KERNEL32.dll')
def SetThreadpoolThreadMinimum(ptpp: win32more.Windows.Win32.System.Threading.PTP_POOL, cthrdMic: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetThreadpoolStackInformation(ptpp: win32more.Windows.Win32.System.Threading.PTP_POOL, ptpsi: POINTER(win32more.Windows.Win32.System.Threading.TP_POOL_STACK_INFORMATION)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def QueryThreadpoolStackInformation(ptpp: win32more.Windows.Win32.System.Threading.PTP_POOL, ptpsi: POINTER(win32more.Windows.Win32.System.Threading.TP_POOL_STACK_INFORMATION)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CloseThreadpool(ptpp: win32more.Windows.Win32.System.Threading.PTP_POOL) -> Void: ...
@winfunctype('KERNEL32.dll')
def CreateThreadpoolCleanupGroup() -> win32more.Windows.Win32.System.Threading.PTP_CLEANUP_GROUP: ...
@winfunctype('KERNEL32.dll')
def CloseThreadpoolCleanupGroupMembers(ptpcg: win32more.Windows.Win32.System.Threading.PTP_CLEANUP_GROUP, fCancelPendingCallbacks: win32more.Windows.Win32.Foundation.BOOL, pvCleanupContext: VoidPtr) -> Void: ...
@winfunctype('KERNEL32.dll')
def CloseThreadpoolCleanupGroup(ptpcg: win32more.Windows.Win32.System.Threading.PTP_CLEANUP_GROUP) -> Void: ...
@winfunctype('KERNEL32.dll')
def SetEventWhenCallbackReturns(pci: win32more.Windows.Win32.System.Threading.PTP_CALLBACK_INSTANCE, evt: win32more.Windows.Win32.Foundation.HANDLE) -> Void: ...
@winfunctype('KERNEL32.dll')
def ReleaseSemaphoreWhenCallbackReturns(pci: win32more.Windows.Win32.System.Threading.PTP_CALLBACK_INSTANCE, sem: win32more.Windows.Win32.Foundation.HANDLE, crel: UInt32) -> Void: ...
@winfunctype('KERNEL32.dll')
def ReleaseMutexWhenCallbackReturns(pci: win32more.Windows.Win32.System.Threading.PTP_CALLBACK_INSTANCE, mut: win32more.Windows.Win32.Foundation.HANDLE) -> Void: ...
@winfunctype('KERNEL32.dll')
def LeaveCriticalSectionWhenCallbackReturns(pci: win32more.Windows.Win32.System.Threading.PTP_CALLBACK_INSTANCE, pcs: POINTER(win32more.Windows.Win32.System.Threading.CRITICAL_SECTION)) -> Void: ...
@winfunctype('KERNEL32.dll')
def FreeLibraryWhenCallbackReturns(pci: win32more.Windows.Win32.System.Threading.PTP_CALLBACK_INSTANCE, mod: win32more.Windows.Win32.Foundation.HMODULE) -> Void: ...
@winfunctype('KERNEL32.dll')
def CallbackMayRunLong(pci: win32more.Windows.Win32.System.Threading.PTP_CALLBACK_INSTANCE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DisassociateCurrentThreadFromCallback(pci: win32more.Windows.Win32.System.Threading.PTP_CALLBACK_INSTANCE) -> Void: ...
@winfunctype('KERNEL32.dll')
def TrySubmitThreadpoolCallback(pfns: win32more.Windows.Win32.System.Threading.PTP_SIMPLE_CALLBACK, pv: VoidPtr, pcbe: POINTER(win32more.Windows.Win32.System.Threading.TP_CALLBACK_ENVIRON_V3)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateThreadpoolWork(pfnwk: win32more.Windows.Win32.System.Threading.PTP_WORK_CALLBACK, pv: VoidPtr, pcbe: POINTER(win32more.Windows.Win32.System.Threading.TP_CALLBACK_ENVIRON_V3)) -> win32more.Windows.Win32.System.Threading.PTP_WORK: ...
@winfunctype('KERNEL32.dll')
def SubmitThreadpoolWork(pwk: win32more.Windows.Win32.System.Threading.PTP_WORK) -> Void: ...
@winfunctype('KERNEL32.dll')
def WaitForThreadpoolWorkCallbacks(pwk: win32more.Windows.Win32.System.Threading.PTP_WORK, fCancelPendingCallbacks: win32more.Windows.Win32.Foundation.BOOL) -> Void: ...
@winfunctype('KERNEL32.dll')
def CloseThreadpoolWork(pwk: win32more.Windows.Win32.System.Threading.PTP_WORK) -> Void: ...
@winfunctype('KERNEL32.dll')
def CreateThreadpoolTimer(pfnti: win32more.Windows.Win32.System.Threading.PTP_TIMER_CALLBACK, pv: VoidPtr, pcbe: POINTER(win32more.Windows.Win32.System.Threading.TP_CALLBACK_ENVIRON_V3)) -> win32more.Windows.Win32.System.Threading.PTP_TIMER: ...
@winfunctype('KERNEL32.dll')
def SetThreadpoolTimer(pti: win32more.Windows.Win32.System.Threading.PTP_TIMER, pftDueTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME), msPeriod: UInt32, msWindowLength: UInt32) -> Void: ...
@winfunctype('KERNEL32.dll')
def IsThreadpoolTimerSet(pti: win32more.Windows.Win32.System.Threading.PTP_TIMER) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WaitForThreadpoolTimerCallbacks(pti: win32more.Windows.Win32.System.Threading.PTP_TIMER, fCancelPendingCallbacks: win32more.Windows.Win32.Foundation.BOOL) -> Void: ...
@winfunctype('KERNEL32.dll')
def CloseThreadpoolTimer(pti: win32more.Windows.Win32.System.Threading.PTP_TIMER) -> Void: ...
@winfunctype('KERNEL32.dll')
def CreateThreadpoolWait(pfnwa: win32more.Windows.Win32.System.Threading.PTP_WAIT_CALLBACK, pv: VoidPtr, pcbe: POINTER(win32more.Windows.Win32.System.Threading.TP_CALLBACK_ENVIRON_V3)) -> win32more.Windows.Win32.System.Threading.PTP_WAIT: ...
@winfunctype('KERNEL32.dll')
def SetThreadpoolWait(pwa: win32more.Windows.Win32.System.Threading.PTP_WAIT, h: win32more.Windows.Win32.Foundation.HANDLE, pftTimeout: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> Void: ...
@winfunctype('KERNEL32.dll')
def WaitForThreadpoolWaitCallbacks(pwa: win32more.Windows.Win32.System.Threading.PTP_WAIT, fCancelPendingCallbacks: win32more.Windows.Win32.Foundation.BOOL) -> Void: ...
@winfunctype('KERNEL32.dll')
def CloseThreadpoolWait(pwa: win32more.Windows.Win32.System.Threading.PTP_WAIT) -> Void: ...
@winfunctype('KERNEL32.dll')
def CreateThreadpoolIo(fl: win32more.Windows.Win32.Foundation.HANDLE, pfnio: win32more.Windows.Win32.System.Threading.PTP_WIN32_IO_CALLBACK, pv: VoidPtr, pcbe: POINTER(win32more.Windows.Win32.System.Threading.TP_CALLBACK_ENVIRON_V3)) -> win32more.Windows.Win32.System.Threading.PTP_IO: ...
@winfunctype('KERNEL32.dll')
def StartThreadpoolIo(pio: win32more.Windows.Win32.System.Threading.PTP_IO) -> Void: ...
@winfunctype('KERNEL32.dll')
def CancelThreadpoolIo(pio: win32more.Windows.Win32.System.Threading.PTP_IO) -> Void: ...
@winfunctype('KERNEL32.dll')
def WaitForThreadpoolIoCallbacks(pio: win32more.Windows.Win32.System.Threading.PTP_IO, fCancelPendingCallbacks: win32more.Windows.Win32.Foundation.BOOL) -> Void: ...
@winfunctype('KERNEL32.dll')
def CloseThreadpoolIo(pio: win32more.Windows.Win32.System.Threading.PTP_IO) -> Void: ...
@winfunctype('KERNEL32.dll')
def SetThreadpoolTimerEx(pti: win32more.Windows.Win32.System.Threading.PTP_TIMER, pftDueTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME), msPeriod: UInt32, msWindowLength: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetThreadpoolWaitEx(pwa: win32more.Windows.Win32.System.Threading.PTP_WAIT, h: win32more.Windows.Win32.Foundation.HANDLE, pftTimeout: POINTER(win32more.Windows.Win32.Foundation.FILETIME), Reserved: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def IsWow64Process(hProcess: win32more.Windows.Win32.Foundation.HANDLE, Wow64Process: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-wow64-l1-1-1.dll')
def Wow64SetThreadDefaultGuestMachine(Machine: UInt16) -> UInt16: ...
@winfunctype('KERNEL32.dll')
def IsWow64Process2(hProcess: win32more.Windows.Win32.Foundation.HANDLE, pProcessMachine: POINTER(win32more.Windows.Win32.System.SystemInformation.IMAGE_FILE_MACHINE), pNativeMachine: POINTER(win32more.Windows.Win32.System.SystemInformation.IMAGE_FILE_MACHINE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def Wow64SuspendThread(hThread: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def CreatePrivateNamespaceW(lpPrivateNamespaceAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), lpBoundaryDescriptor: VoidPtr, lpAliasPrefix: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
CreatePrivateNamespace = UnicodeAlias('CreatePrivateNamespaceW')
@winfunctype('KERNEL32.dll')
def OpenPrivateNamespaceW(lpBoundaryDescriptor: VoidPtr, lpAliasPrefix: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
OpenPrivateNamespace = UnicodeAlias('OpenPrivateNamespaceW')
@winfunctype('KERNEL32.dll')
def ClosePrivateNamespace(Handle: win32more.Windows.Win32.Foundation.HANDLE, Flags: UInt32) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('KERNEL32.dll')
def CreateBoundaryDescriptorW(Name: win32more.Windows.Win32.Foundation.PWSTR, Flags: UInt32) -> win32more.Windows.Win32.Foundation.HANDLE: ...
CreateBoundaryDescriptor = UnicodeAlias('CreateBoundaryDescriptorW')
@winfunctype('KERNEL32.dll')
def AddSIDToBoundaryDescriptor(BoundaryDescriptor: POINTER(win32more.Windows.Win32.Foundation.HANDLE), RequiredSid: win32more.Windows.Win32.Security.PSID) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DeleteBoundaryDescriptor(BoundaryDescriptor: win32more.Windows.Win32.Foundation.HANDLE) -> Void: ...
@winfunctype('KERNEL32.dll')
def GetNumaHighestNodeNumber(HighestNodeNumber: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetNumaNodeProcessorMaskEx(Node: UInt16, ProcessorMask: POINTER(win32more.Windows.Win32.System.SystemInformation.GROUP_AFFINITY)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetNumaNodeProcessorMask2(NodeNumber: UInt16, ProcessorMasks: POINTER(win32more.Windows.Win32.System.SystemInformation.GROUP_AFFINITY), ProcessorMaskCount: UInt16, RequiredMaskCount: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetNumaProximityNodeEx(ProximityId: UInt32, NodeNumber: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetProcessGroupAffinity(hProcess: win32more.Windows.Win32.Foundation.HANDLE, GroupCount: POINTER(UInt16), GroupArray: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetThreadGroupAffinity(hThread: win32more.Windows.Win32.Foundation.HANDLE, GroupAffinity: POINTER(win32more.Windows.Win32.System.SystemInformation.GROUP_AFFINITY)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetThreadGroupAffinity(hThread: win32more.Windows.Win32.Foundation.HANDLE, GroupAffinity: POINTER(win32more.Windows.Win32.System.SystemInformation.GROUP_AFFINITY), PreviousGroupAffinity: POINTER(win32more.Windows.Win32.System.SystemInformation.GROUP_AFFINITY)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('AVRT.dll')
def AvSetMmThreadCharacteristicsA(TaskName: win32more.Windows.Win32.Foundation.PSTR, TaskIndex: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('AVRT.dll')
def AvSetMmThreadCharacteristicsW(TaskName: win32more.Windows.Win32.Foundation.PWSTR, TaskIndex: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HANDLE: ...
AvSetMmThreadCharacteristics = UnicodeAlias('AvSetMmThreadCharacteristicsW')
@winfunctype('AVRT.dll')
def AvSetMmMaxThreadCharacteristicsA(FirstTask: win32more.Windows.Win32.Foundation.PSTR, SecondTask: win32more.Windows.Win32.Foundation.PSTR, TaskIndex: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('AVRT.dll')
def AvSetMmMaxThreadCharacteristicsW(FirstTask: win32more.Windows.Win32.Foundation.PWSTR, SecondTask: win32more.Windows.Win32.Foundation.PWSTR, TaskIndex: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HANDLE: ...
AvSetMmMaxThreadCharacteristics = UnicodeAlias('AvSetMmMaxThreadCharacteristicsW')
@winfunctype('AVRT.dll')
def AvRevertMmThreadCharacteristics(AvrtHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('AVRT.dll')
def AvSetMmThreadPriority(AvrtHandle: win32more.Windows.Win32.Foundation.HANDLE, Priority: win32more.Windows.Win32.System.Threading.AVRT_PRIORITY) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('AVRT.dll')
def AvRtCreateThreadOrderingGroup(Context: POINTER(win32more.Windows.Win32.Foundation.HANDLE), Period: POINTER(Int64), ThreadOrderingGuid: POINTER(Guid), Timeout: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('AVRT.dll')
def AvRtCreateThreadOrderingGroupExA(Context: POINTER(win32more.Windows.Win32.Foundation.HANDLE), Period: POINTER(Int64), ThreadOrderingGuid: POINTER(Guid), Timeout: POINTER(Int64), TaskName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('AVRT.dll')
def AvRtCreateThreadOrderingGroupExW(Context: POINTER(win32more.Windows.Win32.Foundation.HANDLE), Period: POINTER(Int64), ThreadOrderingGuid: POINTER(Guid), Timeout: POINTER(Int64), TaskName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
AvRtCreateThreadOrderingGroupEx = UnicodeAlias('AvRtCreateThreadOrderingGroupExW')
@winfunctype('AVRT.dll')
def AvRtJoinThreadOrderingGroup(Context: POINTER(win32more.Windows.Win32.Foundation.HANDLE), ThreadOrderingGuid: POINTER(Guid), Before: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('AVRT.dll')
def AvRtWaitOnThreadOrderingGroup(Context: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('AVRT.dll')
def AvRtLeaveThreadOrderingGroup(Context: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('AVRT.dll')
def AvRtDeleteThreadOrderingGroup(Context: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('AVRT.dll')
def AvQuerySystemResponsiveness(AvrtHandle: win32more.Windows.Win32.Foundation.HANDLE, SystemResponsivenessValue: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('RTWorkQ.dll')
def RtwqStartup() -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('RTWorkQ.dll')
def RtwqShutdown() -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('RTWorkQ.dll')
def RtwqLockWorkQueue(workQueueId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('RTWorkQ.dll')
def RtwqUnlockWorkQueue(workQueueId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('RTWorkQ.dll')
def RtwqLockSharedWorkQueue(usageClass: win32more.Windows.Win32.Foundation.PWSTR, basePriority: Int32, taskId: POINTER(UInt32), id: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('RTWorkQ.dll')
def RtwqJoinWorkQueue(workQueueId: UInt32, hFile: win32more.Windows.Win32.Foundation.HANDLE, out: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('RTWorkQ.dll')
def RtwqUnjoinWorkQueue(workQueueId: UInt32, hFile: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('RTWorkQ.dll')
def RtwqCreateAsyncResult(appObject: win32more.Windows.Win32.System.Com.IUnknown, callback: win32more.Windows.Win32.System.Threading.IRtwqAsyncCallback, appState: win32more.Windows.Win32.System.Com.IUnknown, asyncResult: POINTER(win32more.Windows.Win32.System.Threading.IRtwqAsyncResult)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('RTWorkQ.dll')
def RtwqInvokeCallback(result: win32more.Windows.Win32.System.Threading.IRtwqAsyncResult) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('RTWorkQ.dll')
def RtwqLockPlatform() -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('RTWorkQ.dll')
def RtwqUnlockPlatform() -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('RTWorkQ.dll')
def RtwqRegisterPlatformWithMMCSS(usageClass: win32more.Windows.Win32.Foundation.PWSTR, taskId: POINTER(UInt32), lPriority: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('RTWorkQ.dll')
def RtwqUnregisterPlatformFromMMCSS() -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('RTWorkQ.dll')
def RtwqPutWorkItem(dwQueue: UInt32, lPriority: Int32, result: win32more.Windows.Win32.System.Threading.IRtwqAsyncResult) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('RTWorkQ.dll')
def RtwqPutWaitingWorkItem(hEvent: win32more.Windows.Win32.Foundation.HANDLE, lPriority: Int32, result: win32more.Windows.Win32.System.Threading.IRtwqAsyncResult, key: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('RTWorkQ.dll')
def RtwqAllocateSerialWorkQueue(workQueueIdIn: UInt32, workQueueIdOut: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('RTWorkQ.dll')
def RtwqScheduleWorkItem(result: win32more.Windows.Win32.System.Threading.IRtwqAsyncResult, Timeout: Int64, key: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('RTWorkQ.dll')
def RtwqAddPeriodicCallback(Callback: win32more.Windows.Win32.System.Threading.RTWQPERIODICCALLBACK, context: win32more.Windows.Win32.System.Com.IUnknown, key: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('RTWorkQ.dll')
def RtwqRemovePeriodicCallback(dwKey: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('RTWorkQ.dll')
def RtwqCancelWorkItem(Key: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('RTWorkQ.dll')
def RtwqAllocateWorkQueue(WorkQueueType: win32more.Windows.Win32.System.Threading.RTWQ_WORKQUEUE_TYPE, workQueueId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('RTWorkQ.dll')
def RtwqBeginRegisterWorkQueueWithMMCSS(workQueueId: UInt32, usageClass: win32more.Windows.Win32.Foundation.PWSTR, dwTaskId: UInt32, lPriority: Int32, doneCallback: win32more.Windows.Win32.System.Threading.IRtwqAsyncCallback, doneState: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('RTWorkQ.dll')
def RtwqBeginUnregisterWorkQueueWithMMCSS(workQueueId: UInt32, doneCallback: win32more.Windows.Win32.System.Threading.IRtwqAsyncCallback, doneState: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('RTWorkQ.dll')
def RtwqEndRegisterWorkQueueWithMMCSS(result: win32more.Windows.Win32.System.Threading.IRtwqAsyncResult, taskId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('RTWorkQ.dll')
def RtwqGetWorkQueueMMCSSClass(workQueueId: UInt32, usageClass: win32more.Windows.Win32.Foundation.PWSTR, usageClassLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('RTWorkQ.dll')
def RtwqGetWorkQueueMMCSSTaskId(workQueueId: UInt32, taskId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('RTWorkQ.dll')
def RtwqGetWorkQueueMMCSSPriority(workQueueId: UInt32, priority: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('RTWorkQ.dll')
def RtwqRegisterPlatformEvents(platformEvents: win32more.Windows.Win32.System.Threading.IRtwqPlatformEvents) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('RTWorkQ.dll')
def RtwqUnregisterPlatformEvents(platformEvents: win32more.Windows.Win32.System.Threading.IRtwqPlatformEvents) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('RTWorkQ.dll')
def RtwqSetLongRunning(workQueueId: UInt32, enable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('RTWorkQ.dll')
def RtwqSetDeadline(workQueueId: UInt32, deadlineInHNS: Int64, pRequest: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('RTWorkQ.dll')
def RtwqSetDeadline2(workQueueId: UInt32, deadlineInHNS: Int64, preDeadlineInHNS: Int64, pRequest: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('RTWorkQ.dll')
def RtwqCancelDeadline(pRequest: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEACC.dll')
def GetProcessHandleFromHwnd(hwnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('USER32.dll')
def AttachThreadInput(idAttach: UInt32, idAttachTo: UInt32, fAttach: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def WaitForInputIdle(hProcess: win32more.Windows.Win32.Foundation.HANDLE, dwMilliseconds: UInt32) -> UInt32: ...
@winfunctype('USER32.dll')
def GetGuiResources(hProcess: win32more.Windows.Win32.Foundation.HANDLE, uiFlags: win32more.Windows.Win32.System.Threading.GET_GUI_RESOURCES_FLAGS) -> UInt32: ...
@winfunctype('USER32.dll')
def IsImmersiveProcess(hProcess: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def SetProcessRestrictionExemption(fEnableExemption: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetProcessAffinityMask(hProcess: win32more.Windows.Win32.Foundation.HANDLE, lpProcessAffinityMask: POINTER(UIntPtr), lpSystemAffinityMask: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetProcessAffinityMask(hProcess: win32more.Windows.Win32.Foundation.HANDLE, dwProcessAffinityMask: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetProcessIoCounters(hProcess: win32more.Windows.Win32.Foundation.HANDLE, lpIoCounters: POINTER(win32more.Windows.Win32.System.Threading.IO_COUNTERS)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SwitchToFiber(lpFiber: VoidPtr) -> Void: ...
@winfunctype('KERNEL32.dll')
def DeleteFiber(lpFiber: VoidPtr) -> Void: ...
@winfunctype('KERNEL32.dll')
def ConvertFiberToThread() -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateFiberEx(dwStackCommitSize: UIntPtr, dwStackReserveSize: UIntPtr, dwFlags: UInt32, lpStartAddress: win32more.Windows.Win32.System.Threading.LPFIBER_START_ROUTINE, lpParameter: VoidPtr) -> VoidPtr: ...
@winfunctype('KERNEL32.dll')
def ConvertThreadToFiberEx(lpParameter: VoidPtr, dwFlags: UInt32) -> VoidPtr: ...
@winfunctype('KERNEL32.dll')
def CreateFiber(dwStackSize: UIntPtr, lpStartAddress: win32more.Windows.Win32.System.Threading.LPFIBER_START_ROUTINE, lpParameter: VoidPtr) -> VoidPtr: ...
@winfunctype('KERNEL32.dll')
def ConvertThreadToFiber(lpParameter: VoidPtr) -> VoidPtr: ...
@winfunctype('KERNEL32.dll')
def CreateUmsCompletionList(UmsCompletionList: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DequeueUmsCompletionListItems(UmsCompletionList: VoidPtr, WaitTimeOut: UInt32, UmsThreadList: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetUmsCompletionListEvent(UmsCompletionList: VoidPtr, UmsCompletionEvent: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ExecuteUmsThread(UmsThread: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def UmsThreadYield(SchedulerParam: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DeleteUmsCompletionList(UmsCompletionList: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetCurrentUmsThread() -> VoidPtr: ...
@winfunctype('KERNEL32.dll')
def GetNextUmsListItem(UmsContext: VoidPtr) -> VoidPtr: ...
@winfunctype('KERNEL32.dll')
def QueryUmsThreadInformation(UmsThread: VoidPtr, UmsThreadInfoClass: win32more.Windows.Win32.System.Threading.UMS_THREAD_INFO_CLASS, UmsThreadInformation: VoidPtr, UmsThreadInformationLength: UInt32, ReturnLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetUmsThreadInformation(UmsThread: VoidPtr, UmsThreadInfoClass: win32more.Windows.Win32.System.Threading.UMS_THREAD_INFO_CLASS, UmsThreadInformation: VoidPtr, UmsThreadInformationLength: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DeleteUmsThreadContext(UmsThread: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateUmsThreadContext(lpUmsThread: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def EnterUmsSchedulingMode(SchedulerStartupInfo: POINTER(win32more.Windows.Win32.System.Threading.UMS_SCHEDULER_STARTUP_INFO)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetUmsSystemThreadInformation(ThreadHandle: win32more.Windows.Win32.Foundation.HANDLE, SystemThreadInfo: POINTER(win32more.Windows.Win32.System.Threading.UMS_SYSTEM_THREAD_INFORMATION)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetThreadAffinityMask(hThread: win32more.Windows.Win32.Foundation.HANDLE, dwThreadAffinityMask: UIntPtr) -> UIntPtr: ...
@winfunctype('KERNEL32.dll')
def SetProcessDEPPolicy(dwFlags: win32more.Windows.Win32.System.Threading.PROCESS_DEP_FLAGS) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetProcessDEPPolicy(hProcess: win32more.Windows.Win32.Foundation.HANDLE, lpFlags: POINTER(UInt32), lpPermanent: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def PulseEvent(hEvent: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WinExec(lpCmdLine: win32more.Windows.Win32.Foundation.PSTR, uCmdShow: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def SignalObjectAndWait(hObjectToSignal: win32more.Windows.Win32.Foundation.HANDLE, hObjectToWaitOn: win32more.Windows.Win32.Foundation.HANDLE, dwMilliseconds: UInt32, bAlertable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.WAIT_EVENT: ...
@winfunctype('KERNEL32.dll')
def CreateSemaphoreA(lpSemaphoreAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), lInitialCount: Int32, lMaximumCount: Int32, lpName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def CreateWaitableTimerA(lpTimerAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), bManualReset: win32more.Windows.Win32.Foundation.BOOL, lpTimerName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def OpenWaitableTimerA(dwDesiredAccess: UInt32, bInheritHandle: win32more.Windows.Win32.Foundation.BOOL, lpTimerName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def CreateSemaphoreExA(lpSemaphoreAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), lInitialCount: Int32, lMaximumCount: Int32, lpName: win32more.Windows.Win32.Foundation.PSTR, dwFlags: UInt32, dwDesiredAccess: UInt32) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def CreateWaitableTimerExA(lpTimerAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), lpTimerName: win32more.Windows.Win32.Foundation.PSTR, dwFlags: UInt32, dwDesiredAccess: UInt32) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def QueryFullProcessImageNameA(hProcess: win32more.Windows.Win32.Foundation.HANDLE, dwFlags: win32more.Windows.Win32.System.Threading.PROCESS_NAME_FORMAT, lpExeName: win32more.Windows.Win32.Foundation.PSTR, lpdwSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def QueryFullProcessImageNameW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, dwFlags: win32more.Windows.Win32.System.Threading.PROCESS_NAME_FORMAT, lpExeName: win32more.Windows.Win32.Foundation.PWSTR, lpdwSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
QueryFullProcessImageName = UnicodeAlias('QueryFullProcessImageNameW')
@winfunctype('KERNEL32.dll')
def GetStartupInfoA(lpStartupInfo: POINTER(win32more.Windows.Win32.System.Threading.STARTUPINFOA)) -> Void: ...
@winfunctype('ADVAPI32.dll')
def CreateProcessWithLogonW(lpUsername: win32more.Windows.Win32.Foundation.PWSTR, lpDomain: win32more.Windows.Win32.Foundation.PWSTR, lpPassword: win32more.Windows.Win32.Foundation.PWSTR, dwLogonFlags: win32more.Windows.Win32.System.Threading.CREATE_PROCESS_LOGON_FLAGS, lpApplicationName: win32more.Windows.Win32.Foundation.PWSTR, lpCommandLine: win32more.Windows.Win32.Foundation.PWSTR, dwCreationFlags: win32more.Windows.Win32.System.Threading.PROCESS_CREATION_FLAGS, lpEnvironment: VoidPtr, lpCurrentDirectory: win32more.Windows.Win32.Foundation.PWSTR, lpStartupInfo: POINTER(win32more.Windows.Win32.System.Threading.STARTUPINFOW), lpProcessInformation: POINTER(win32more.Windows.Win32.System.Threading.PROCESS_INFORMATION)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CreateProcessWithTokenW(hToken: win32more.Windows.Win32.Foundation.HANDLE, dwLogonFlags: win32more.Windows.Win32.System.Threading.CREATE_PROCESS_LOGON_FLAGS, lpApplicationName: win32more.Windows.Win32.Foundation.PWSTR, lpCommandLine: win32more.Windows.Win32.Foundation.PWSTR, dwCreationFlags: win32more.Windows.Win32.System.Threading.PROCESS_CREATION_FLAGS, lpEnvironment: VoidPtr, lpCurrentDirectory: win32more.Windows.Win32.Foundation.PWSTR, lpStartupInfo: POINTER(win32more.Windows.Win32.System.Threading.STARTUPINFOW), lpProcessInformation: POINTER(win32more.Windows.Win32.System.Threading.PROCESS_INFORMATION)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def RegisterWaitForSingleObject(phNewWaitObject: POINTER(win32more.Windows.Win32.Foundation.HANDLE), hObject: win32more.Windows.Win32.Foundation.HANDLE, Callback: win32more.Windows.Win32.System.Threading.WAITORTIMERCALLBACK, Context: VoidPtr, dwMilliseconds: UInt32, dwFlags: win32more.Windows.Win32.System.Threading.WORKER_THREAD_FLAGS) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def UnregisterWait(WaitHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetTimerQueueTimer(TimerQueue: win32more.Windows.Win32.Foundation.HANDLE, Callback: win32more.Windows.Win32.System.Threading.WAITORTIMERCALLBACK, Parameter: VoidPtr, DueTime: UInt32, Period: UInt32, PreferIo: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def CancelTimerQueueTimer(TimerQueue: win32more.Windows.Win32.Foundation.HANDLE, Timer: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreatePrivateNamespaceA(lpPrivateNamespaceAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), lpBoundaryDescriptor: VoidPtr, lpAliasPrefix: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def OpenPrivateNamespaceA(lpBoundaryDescriptor: VoidPtr, lpAliasPrefix: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def CreateBoundaryDescriptorA(Name: win32more.Windows.Win32.Foundation.PSTR, Flags: UInt32) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def AddIntegrityLabelToBoundaryDescriptor(BoundaryDescriptor: POINTER(win32more.Windows.Win32.Foundation.HANDLE), IntegrityLabel: win32more.Windows.Win32.Security.PSID) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetActiveProcessorGroupCount() -> UInt16: ...
@winfunctype('KERNEL32.dll')
def GetMaximumProcessorGroupCount() -> UInt16: ...
@winfunctype('KERNEL32.dll')
def GetActiveProcessorCount(GroupNumber: UInt16) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetMaximumProcessorCount(GroupNumber: UInt16) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetNumaProcessorNode(Processor: Byte, NodeNumber: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetNumaNodeNumberFromHandle(hFile: win32more.Windows.Win32.Foundation.HANDLE, NodeNumber: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetNumaProcessorNodeEx(Processor: POINTER(win32more.Windows.Win32.System.Kernel.PROCESSOR_NUMBER), NodeNumber: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetNumaNodeProcessorMask(Node: Byte, ProcessorMask: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetNumaAvailableMemoryNode(Node: Byte, AvailableBytes: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetNumaAvailableMemoryNodeEx(Node: UInt16, AvailableBytes: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetNumaProximityNode(ProximityId: UInt32, NodeNumber: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.BOOL: ...
class CONDITION_VARIABLE(Structure):
    Ptr: VoidPtr
CREATE_EVENT = UInt32
CREATE_EVENT_INITIAL_SET: win32more.Windows.Win32.System.Threading.CREATE_EVENT = 2
CREATE_EVENT_MANUAL_RESET: win32more.Windows.Win32.System.Threading.CREATE_EVENT = 1
CREATE_PROCESS_LOGON_FLAGS = UInt32
LOGON_WITH_PROFILE: win32more.Windows.Win32.System.Threading.CREATE_PROCESS_LOGON_FLAGS = 1
LOGON_NETCREDENTIALS_ONLY: win32more.Windows.Win32.System.Threading.CREATE_PROCESS_LOGON_FLAGS = 2
class CRITICAL_SECTION(Structure):
    DebugInfo: POINTER(win32more.Windows.Win32.System.Threading.CRITICAL_SECTION_DEBUG)
    LockCount: Int32
    RecursionCount: Int32
    OwningThread: win32more.Windows.Win32.Foundation.HANDLE
    LockSemaphore: win32more.Windows.Win32.Foundation.HANDLE
    SpinCount: UIntPtr
class CRITICAL_SECTION_DEBUG(Structure):
    Type: UInt16
    CreatorBackTraceIndex: UInt16
    CriticalSection: POINTER(win32more.Windows.Win32.System.Threading.CRITICAL_SECTION)
    ProcessLocksList: win32more.Windows.Win32.System.Kernel.LIST_ENTRY
    EntryCount: UInt32
    ContentionCount: UInt32
    Flags: UInt32
    CreatorBackTraceIndexHigh: UInt16
    Identifier: UInt16
GET_GUI_RESOURCES_FLAGS = UInt32
GR_GLOBAL: win32more.Windows.Win32.System.Threading.GET_GUI_RESOURCES_FLAGS = 4294967294
GR_GDIOBJECTS: win32more.Windows.Win32.System.Threading.GET_GUI_RESOURCES_FLAGS = 0
GR_GDIOBJECTS_PEAK: win32more.Windows.Win32.System.Threading.GET_GUI_RESOURCES_FLAGS = 2
GR_USEROBJECTS: win32more.Windows.Win32.System.Threading.GET_GUI_RESOURCES_FLAGS = 1
GR_USEROBJECTS_PEAK: win32more.Windows.Win32.System.Threading.GET_GUI_RESOURCES_FLAGS = 4
class INIT_ONCE(Union):
    Ptr: VoidPtr
class IO_COUNTERS(Structure):
    ReadOperationCount: UInt64
    WriteOperationCount: UInt64
    OtherOperationCount: UInt64
    ReadTransferCount: UInt64
    WriteTransferCount: UInt64
    OtherTransferCount: UInt64
class IRtwqAsyncCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a27003cf-2354-4f2a-8d6a-ab7cff15437e}')
    @commethod(3)
    def GetParameters(self, pdwFlags: POINTER(UInt32), pdwQueue: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Invoke(self, pAsyncResult: win32more.Windows.Win32.System.Threading.IRtwqAsyncResult) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRtwqAsyncResult(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ac6b7889-0740-4d51-8619-905994a55cc6}')
    @commethod(3)
    def GetState(self, ppunkState: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetStatus(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetStatus(self, hrStatus: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetObject(self, ppObject: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetStateNoAddRef(self) -> win32more.Windows.Win32.System.Com.IUnknown: ...
class IRtwqPlatformEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{63d9255a-7ff1-4b61-8faf-ed6460dacf2b}')
    @commethod(3)
    def InitializationComplete(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ShutdownStart(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ShutdownComplete(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def LPFIBER_START_ROUTINE(lpFiberParameter: VoidPtr) -> Void: ...
LPPROC_THREAD_ATTRIBUTE_LIST = VoidPtr
@winfunctype_pointer
def LPTHREAD_START_ROUTINE(lpThreadParameter: VoidPtr) -> UInt32: ...
MACHINE_ATTRIBUTES = Int32
UserEnabled: win32more.Windows.Win32.System.Threading.MACHINE_ATTRIBUTES = 1
KernelEnabled: win32more.Windows.Win32.System.Threading.MACHINE_ATTRIBUTES = 2
Wow64Container: win32more.Windows.Win32.System.Threading.MACHINE_ATTRIBUTES = 4
MEMORY_PRIORITY = UInt32
MEMORY_PRIORITY_VERY_LOW: win32more.Windows.Win32.System.Threading.MEMORY_PRIORITY = 1
MEMORY_PRIORITY_LOW: win32more.Windows.Win32.System.Threading.MEMORY_PRIORITY = 2
MEMORY_PRIORITY_MEDIUM: win32more.Windows.Win32.System.Threading.MEMORY_PRIORITY = 3
MEMORY_PRIORITY_BELOW_NORMAL: win32more.Windows.Win32.System.Threading.MEMORY_PRIORITY = 4
MEMORY_PRIORITY_NORMAL: win32more.Windows.Win32.System.Threading.MEMORY_PRIORITY = 5
class MEMORY_PRIORITY_INFORMATION(Structure):
    MemoryPriority: win32more.Windows.Win32.System.Threading.MEMORY_PRIORITY
class OVERRIDE_PREFETCH_PARAMETER(Structure):
    Value: UInt32
class PEB(Structure):
    Reserved1: Byte * 2
    BeingDebugged: Byte
    Reserved2: Byte * 1
    Reserved3: VoidPtr * 2
    Ldr: POINTER(win32more.Windows.Win32.System.Threading.PEB_LDR_DATA)
    ProcessParameters: POINTER(win32more.Windows.Win32.System.Threading.RTL_USER_PROCESS_PARAMETERS)
    Reserved4: VoidPtr * 3
    AtlThunkSListPtr: VoidPtr
    Reserved5: VoidPtr
    Reserved6: UInt32
    Reserved7: VoidPtr
    Reserved8: UInt32
    AtlThunkSListPtr32: UInt32
    Reserved9: VoidPtr * 45
    Reserved10: Byte * 96
    PostProcessInitRoutine: win32more.Windows.Win32.System.Threading.PPS_POST_PROCESS_INIT_ROUTINE
    Reserved11: Byte * 128
    Reserved12: VoidPtr * 1
    SessionId: UInt32
class PEB_LDR_DATA(Structure):
    Reserved1: Byte * 8
    Reserved2: VoidPtr * 3
    InMemoryOrderModuleList: win32more.Windows.Win32.System.Kernel.LIST_ENTRY
@winfunctype_pointer
def PFLS_CALLBACK_FUNCTION(lpFlsData: VoidPtr) -> Void: ...
@winfunctype_pointer
def PINIT_ONCE_FN(InitOnce: POINTER(win32more.Windows.Win32.System.Threading.INIT_ONCE), Parameter: VoidPtr, Context: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
POWER_REQUEST_CONTEXT_FLAGS = UInt32
POWER_REQUEST_CONTEXT_DETAILED_STRING: win32more.Windows.Win32.System.Threading.POWER_REQUEST_CONTEXT_FLAGS = 2
POWER_REQUEST_CONTEXT_SIMPLE_STRING: win32more.Windows.Win32.System.Threading.POWER_REQUEST_CONTEXT_FLAGS = 1
@winfunctype_pointer
def PPS_POST_PROCESS_INIT_ROUTINE() -> Void: ...
PROCESSOR_FEATURE_ID = UInt32
PF_FLOATING_POINT_PRECISION_ERRATA: win32more.Windows.Win32.System.Threading.PROCESSOR_FEATURE_ID = 0
PF_FLOATING_POINT_EMULATED: win32more.Windows.Win32.System.Threading.PROCESSOR_FEATURE_ID = 1
PF_COMPARE_EXCHANGE_DOUBLE: win32more.Windows.Win32.System.Threading.PROCESSOR_FEATURE_ID = 2
PF_MMX_INSTRUCTIONS_AVAILABLE: win32more.Windows.Win32.System.Threading.PROCESSOR_FEATURE_ID = 3
PF_PPC_MOVEMEM_64BIT_OK: win32more.Windows.Win32.System.Threading.PROCESSOR_FEATURE_ID = 4
PF_ALPHA_BYTE_INSTRUCTIONS: win32more.Windows.Win32.System.Threading.PROCESSOR_FEATURE_ID = 5
PF_XMMI_INSTRUCTIONS_AVAILABLE: win32more.Windows.Win32.System.Threading.PROCESSOR_FEATURE_ID = 6
PF_3DNOW_INSTRUCTIONS_AVAILABLE: win32more.Windows.Win32.System.Threading.PROCESSOR_FEATURE_ID = 7
PF_RDTSC_INSTRUCTION_AVAILABLE: win32more.Windows.Win32.System.Threading.PROCESSOR_FEATURE_ID = 8
PF_PAE_ENABLED: win32more.Windows.Win32.System.Threading.PROCESSOR_FEATURE_ID = 9
PF_XMMI64_INSTRUCTIONS_AVAILABLE: win32more.Windows.Win32.System.Threading.PROCESSOR_FEATURE_ID = 10
PF_SSE_DAZ_MODE_AVAILABLE: win32more.Windows.Win32.System.Threading.PROCESSOR_FEATURE_ID = 11
PF_NX_ENABLED: win32more.Windows.Win32.System.Threading.PROCESSOR_FEATURE_ID = 12
PF_SSE3_INSTRUCTIONS_AVAILABLE: win32more.Windows.Win32.System.Threading.PROCESSOR_FEATURE_ID = 13
PF_COMPARE_EXCHANGE128: win32more.Windows.Win32.System.Threading.PROCESSOR_FEATURE_ID = 14
PF_COMPARE64_EXCHANGE128: win32more.Windows.Win32.System.Threading.PROCESSOR_FEATURE_ID = 15
PF_CHANNELS_ENABLED: win32more.Windows.Win32.System.Threading.PROCESSOR_FEATURE_ID = 16
PF_XSAVE_ENABLED: win32more.Windows.Win32.System.Threading.PROCESSOR_FEATURE_ID = 17
PF_ARM_VFP_32_REGISTERS_AVAILABLE: win32more.Windows.Win32.System.Threading.PROCESSOR_FEATURE_ID = 18
PF_ARM_NEON_INSTRUCTIONS_AVAILABLE: win32more.Windows.Win32.System.Threading.PROCESSOR_FEATURE_ID = 19
PF_SECOND_LEVEL_ADDRESS_TRANSLATION: win32more.Windows.Win32.System.Threading.PROCESSOR_FEATURE_ID = 20
PF_VIRT_FIRMWARE_ENABLED: win32more.Windows.Win32.System.Threading.PROCESSOR_FEATURE_ID = 21
PF_RDWRFSGSBASE_AVAILABLE: win32more.Windows.Win32.System.Threading.PROCESSOR_FEATURE_ID = 22
PF_FASTFAIL_AVAILABLE: win32more.Windows.Win32.System.Threading.PROCESSOR_FEATURE_ID = 23
PF_ARM_DIVIDE_INSTRUCTION_AVAILABLE: win32more.Windows.Win32.System.Threading.PROCESSOR_FEATURE_ID = 24
PF_ARM_64BIT_LOADSTORE_ATOMIC: win32more.Windows.Win32.System.Threading.PROCESSOR_FEATURE_ID = 25
PF_ARM_EXTERNAL_CACHE_AVAILABLE: win32more.Windows.Win32.System.Threading.PROCESSOR_FEATURE_ID = 26
PF_ARM_FMAC_INSTRUCTIONS_AVAILABLE: win32more.Windows.Win32.System.Threading.PROCESSOR_FEATURE_ID = 27
PF_RDRAND_INSTRUCTION_AVAILABLE: win32more.Windows.Win32.System.Threading.PROCESSOR_FEATURE_ID = 28
PF_ARM_V8_INSTRUCTIONS_AVAILABLE: win32more.Windows.Win32.System.Threading.PROCESSOR_FEATURE_ID = 29
PF_ARM_V8_CRYPTO_INSTRUCTIONS_AVAILABLE: win32more.Windows.Win32.System.Threading.PROCESSOR_FEATURE_ID = 30
PF_ARM_V8_CRC32_INSTRUCTIONS_AVAILABLE: win32more.Windows.Win32.System.Threading.PROCESSOR_FEATURE_ID = 31
PF_RDTSCP_INSTRUCTION_AVAILABLE: win32more.Windows.Win32.System.Threading.PROCESSOR_FEATURE_ID = 32
PF_RDPID_INSTRUCTION_AVAILABLE: win32more.Windows.Win32.System.Threading.PROCESSOR_FEATURE_ID = 33
PF_ARM_V81_ATOMIC_INSTRUCTIONS_AVAILABLE: win32more.Windows.Win32.System.Threading.PROCESSOR_FEATURE_ID = 34
PF_MONITORX_INSTRUCTION_AVAILABLE: win32more.Windows.Win32.System.Threading.PROCESSOR_FEATURE_ID = 35
PF_SSSE3_INSTRUCTIONS_AVAILABLE: win32more.Windows.Win32.System.Threading.PROCESSOR_FEATURE_ID = 36
PF_SSE4_1_INSTRUCTIONS_AVAILABLE: win32more.Windows.Win32.System.Threading.PROCESSOR_FEATURE_ID = 37
PF_SSE4_2_INSTRUCTIONS_AVAILABLE: win32more.Windows.Win32.System.Threading.PROCESSOR_FEATURE_ID = 38
PF_AVX_INSTRUCTIONS_AVAILABLE: win32more.Windows.Win32.System.Threading.PROCESSOR_FEATURE_ID = 39
PF_AVX2_INSTRUCTIONS_AVAILABLE: win32more.Windows.Win32.System.Threading.PROCESSOR_FEATURE_ID = 40
PF_AVX512F_INSTRUCTIONS_AVAILABLE: win32more.Windows.Win32.System.Threading.PROCESSOR_FEATURE_ID = 41
PF_ERMS_AVAILABLE: win32more.Windows.Win32.System.Threading.PROCESSOR_FEATURE_ID = 42
PF_ARM_V82_DP_INSTRUCTIONS_AVAILABLE: win32more.Windows.Win32.System.Threading.PROCESSOR_FEATURE_ID = 43
PF_ARM_V83_JSCVT_INSTRUCTIONS_AVAILABLE: win32more.Windows.Win32.System.Threading.PROCESSOR_FEATURE_ID = 44
PF_ARM_V83_LRCPC_INSTRUCTIONS_AVAILABLE: win32more.Windows.Win32.System.Threading.PROCESSOR_FEATURE_ID = 45
PROCESS_ACCESS_RIGHTS = UInt32
PROCESS_TERMINATE: win32more.Windows.Win32.System.Threading.PROCESS_ACCESS_RIGHTS = 1
PROCESS_CREATE_THREAD: win32more.Windows.Win32.System.Threading.PROCESS_ACCESS_RIGHTS = 2
PROCESS_SET_SESSIONID: win32more.Windows.Win32.System.Threading.PROCESS_ACCESS_RIGHTS = 4
PROCESS_VM_OPERATION: win32more.Windows.Win32.System.Threading.PROCESS_ACCESS_RIGHTS = 8
PROCESS_VM_READ: win32more.Windows.Win32.System.Threading.PROCESS_ACCESS_RIGHTS = 16
PROCESS_VM_WRITE: win32more.Windows.Win32.System.Threading.PROCESS_ACCESS_RIGHTS = 32
PROCESS_DUP_HANDLE: win32more.Windows.Win32.System.Threading.PROCESS_ACCESS_RIGHTS = 64
PROCESS_CREATE_PROCESS: win32more.Windows.Win32.System.Threading.PROCESS_ACCESS_RIGHTS = 128
PROCESS_SET_QUOTA: win32more.Windows.Win32.System.Threading.PROCESS_ACCESS_RIGHTS = 256
PROCESS_SET_INFORMATION: win32more.Windows.Win32.System.Threading.PROCESS_ACCESS_RIGHTS = 512
PROCESS_QUERY_INFORMATION: win32more.Windows.Win32.System.Threading.PROCESS_ACCESS_RIGHTS = 1024
PROCESS_SUSPEND_RESUME: win32more.Windows.Win32.System.Threading.PROCESS_ACCESS_RIGHTS = 2048
PROCESS_QUERY_LIMITED_INFORMATION: win32more.Windows.Win32.System.Threading.PROCESS_ACCESS_RIGHTS = 4096
PROCESS_SET_LIMITED_INFORMATION: win32more.Windows.Win32.System.Threading.PROCESS_ACCESS_RIGHTS = 8192
PROCESS_ALL_ACCESS: win32more.Windows.Win32.System.Threading.PROCESS_ACCESS_RIGHTS = 2097151
PROCESS_DELETE: win32more.Windows.Win32.System.Threading.PROCESS_ACCESS_RIGHTS = 65536
PROCESS_READ_CONTROL: win32more.Windows.Win32.System.Threading.PROCESS_ACCESS_RIGHTS = 131072
PROCESS_WRITE_DAC: win32more.Windows.Win32.System.Threading.PROCESS_ACCESS_RIGHTS = 262144
PROCESS_WRITE_OWNER: win32more.Windows.Win32.System.Threading.PROCESS_ACCESS_RIGHTS = 524288
PROCESS_SYNCHRONIZE: win32more.Windows.Win32.System.Threading.PROCESS_ACCESS_RIGHTS = 1048576
PROCESS_STANDARD_RIGHTS_REQUIRED: win32more.Windows.Win32.System.Threading.PROCESS_ACCESS_RIGHTS = 983040
PROCESS_AFFINITY_AUTO_UPDATE_FLAGS = UInt32
PROCESS_AFFINITY_DISABLE_AUTO_UPDATE: win32more.Windows.Win32.System.Threading.PROCESS_AFFINITY_AUTO_UPDATE_FLAGS = 0
PROCESS_AFFINITY_ENABLE_AUTO_UPDATE: win32more.Windows.Win32.System.Threading.PROCESS_AFFINITY_AUTO_UPDATE_FLAGS = 1
class PROCESS_BASIC_INFORMATION(Structure):
    ExitStatus: win32more.Windows.Win32.Foundation.NTSTATUS
    PebBaseAddress: POINTER(win32more.Windows.Win32.System.Threading.PEB)
    AffinityMask: UIntPtr
    BasePriority: Int32
    UniqueProcessId: UIntPtr
    InheritedFromUniqueProcessId: UIntPtr
PROCESS_CREATION_FLAGS = UInt32
DEBUG_PROCESS: win32more.Windows.Win32.System.Threading.PROCESS_CREATION_FLAGS = 1
DEBUG_ONLY_THIS_PROCESS: win32more.Windows.Win32.System.Threading.PROCESS_CREATION_FLAGS = 2
CREATE_SUSPENDED: win32more.Windows.Win32.System.Threading.PROCESS_CREATION_FLAGS = 4
DETACHED_PROCESS: win32more.Windows.Win32.System.Threading.PROCESS_CREATION_FLAGS = 8
CREATE_NEW_CONSOLE: win32more.Windows.Win32.System.Threading.PROCESS_CREATION_FLAGS = 16
NORMAL_PRIORITY_CLASS: win32more.Windows.Win32.System.Threading.PROCESS_CREATION_FLAGS = 32
IDLE_PRIORITY_CLASS: win32more.Windows.Win32.System.Threading.PROCESS_CREATION_FLAGS = 64
HIGH_PRIORITY_CLASS: win32more.Windows.Win32.System.Threading.PROCESS_CREATION_FLAGS = 128
REALTIME_PRIORITY_CLASS: win32more.Windows.Win32.System.Threading.PROCESS_CREATION_FLAGS = 256
CREATE_NEW_PROCESS_GROUP: win32more.Windows.Win32.System.Threading.PROCESS_CREATION_FLAGS = 512
CREATE_UNICODE_ENVIRONMENT: win32more.Windows.Win32.System.Threading.PROCESS_CREATION_FLAGS = 1024
CREATE_SEPARATE_WOW_VDM: win32more.Windows.Win32.System.Threading.PROCESS_CREATION_FLAGS = 2048
CREATE_SHARED_WOW_VDM: win32more.Windows.Win32.System.Threading.PROCESS_CREATION_FLAGS = 4096
CREATE_FORCEDOS: win32more.Windows.Win32.System.Threading.PROCESS_CREATION_FLAGS = 8192
BELOW_NORMAL_PRIORITY_CLASS: win32more.Windows.Win32.System.Threading.PROCESS_CREATION_FLAGS = 16384
ABOVE_NORMAL_PRIORITY_CLASS: win32more.Windows.Win32.System.Threading.PROCESS_CREATION_FLAGS = 32768
INHERIT_PARENT_AFFINITY: win32more.Windows.Win32.System.Threading.PROCESS_CREATION_FLAGS = 65536
INHERIT_CALLER_PRIORITY: win32more.Windows.Win32.System.Threading.PROCESS_CREATION_FLAGS = 131072
CREATE_PROTECTED_PROCESS: win32more.Windows.Win32.System.Threading.PROCESS_CREATION_FLAGS = 262144
EXTENDED_STARTUPINFO_PRESENT: win32more.Windows.Win32.System.Threading.PROCESS_CREATION_FLAGS = 524288
PROCESS_MODE_BACKGROUND_BEGIN: win32more.Windows.Win32.System.Threading.PROCESS_CREATION_FLAGS = 1048576
PROCESS_MODE_BACKGROUND_END: win32more.Windows.Win32.System.Threading.PROCESS_CREATION_FLAGS = 2097152
CREATE_SECURE_PROCESS: win32more.Windows.Win32.System.Threading.PROCESS_CREATION_FLAGS = 4194304
CREATE_BREAKAWAY_FROM_JOB: win32more.Windows.Win32.System.Threading.PROCESS_CREATION_FLAGS = 16777216
CREATE_PRESERVE_CODE_AUTHZ_LEVEL: win32more.Windows.Win32.System.Threading.PROCESS_CREATION_FLAGS = 33554432
CREATE_DEFAULT_ERROR_MODE: win32more.Windows.Win32.System.Threading.PROCESS_CREATION_FLAGS = 67108864
CREATE_NO_WINDOW: win32more.Windows.Win32.System.Threading.PROCESS_CREATION_FLAGS = 134217728
PROFILE_USER: win32more.Windows.Win32.System.Threading.PROCESS_CREATION_FLAGS = 268435456
PROFILE_KERNEL: win32more.Windows.Win32.System.Threading.PROCESS_CREATION_FLAGS = 536870912
PROFILE_SERVER: win32more.Windows.Win32.System.Threading.PROCESS_CREATION_FLAGS = 1073741824
CREATE_IGNORE_SYSTEM_DEFAULT: win32more.Windows.Win32.System.Threading.PROCESS_CREATION_FLAGS = 2147483648
PROCESS_DEP_FLAGS = UInt32
PROCESS_DEP_ENABLE: win32more.Windows.Win32.System.Threading.PROCESS_DEP_FLAGS = 1
PROCESS_DEP_DISABLE_ATL_THUNK_EMULATION: win32more.Windows.Win32.System.Threading.PROCESS_DEP_FLAGS = 2
PROCESS_DEP_NONE: win32more.Windows.Win32.System.Threading.PROCESS_DEP_FLAGS = 0
class PROCESS_DYNAMIC_EH_CONTINUATION_TARGET(Structure):
    TargetAddress: UIntPtr
    Flags: UIntPtr
class PROCESS_DYNAMIC_EH_CONTINUATION_TARGETS_INFORMATION(Structure):
    NumberOfTargets: UInt16
    Reserved: UInt16
    Reserved2: UInt32
    Targets: POINTER(win32more.Windows.Win32.System.Threading.PROCESS_DYNAMIC_EH_CONTINUATION_TARGET)
class PROCESS_DYNAMIC_ENFORCED_ADDRESS_RANGE(Structure):
    BaseAddress: UIntPtr
    Size: UIntPtr
    Flags: UInt32
class PROCESS_DYNAMIC_ENFORCED_ADDRESS_RANGES_INFORMATION(Structure):
    NumberOfRanges: UInt16
    Reserved: UInt16
    Reserved2: UInt32
    Ranges: POINTER(win32more.Windows.Win32.System.Threading.PROCESS_DYNAMIC_ENFORCED_ADDRESS_RANGE)
class PROCESS_INFORMATION(Structure):
    hProcess: win32more.Windows.Win32.Foundation.HANDLE
    hThread: win32more.Windows.Win32.Foundation.HANDLE
    dwProcessId: UInt32
    dwThreadId: UInt32
PROCESS_INFORMATION_CLASS = Int32
ProcessMemoryPriority: win32more.Windows.Win32.System.Threading.PROCESS_INFORMATION_CLASS = 0
ProcessMemoryExhaustionInfo: win32more.Windows.Win32.System.Threading.PROCESS_INFORMATION_CLASS = 1
ProcessAppMemoryInfo: win32more.Windows.Win32.System.Threading.PROCESS_INFORMATION_CLASS = 2
ProcessInPrivateInfo: win32more.Windows.Win32.System.Threading.PROCESS_INFORMATION_CLASS = 3
ProcessPowerThrottling: win32more.Windows.Win32.System.Threading.PROCESS_INFORMATION_CLASS = 4
ProcessReservedValue1: win32more.Windows.Win32.System.Threading.PROCESS_INFORMATION_CLASS = 5
ProcessTelemetryCoverageInfo: win32more.Windows.Win32.System.Threading.PROCESS_INFORMATION_CLASS = 6
ProcessProtectionLevelInfo: win32more.Windows.Win32.System.Threading.PROCESS_INFORMATION_CLASS = 7
ProcessLeapSecondInfo: win32more.Windows.Win32.System.Threading.PROCESS_INFORMATION_CLASS = 8
ProcessMachineTypeInfo: win32more.Windows.Win32.System.Threading.PROCESS_INFORMATION_CLASS = 9
ProcessOverrideSubsequentPrefetchParameter: win32more.Windows.Win32.System.Threading.PROCESS_INFORMATION_CLASS = 10
ProcessMaxOverridePrefetchParameter: win32more.Windows.Win32.System.Threading.PROCESS_INFORMATION_CLASS = 11
ProcessInformationClassMax: win32more.Windows.Win32.System.Threading.PROCESS_INFORMATION_CLASS = 12
class PROCESS_LEAP_SECOND_INFO(Structure):
    Flags: UInt32
    Reserved: UInt32
class PROCESS_MACHINE_INFORMATION(Structure):
    ProcessMachine: win32more.Windows.Win32.System.SystemInformation.IMAGE_FILE_MACHINE
    Res0: UInt16
    MachineAttributes: win32more.Windows.Win32.System.Threading.MACHINE_ATTRIBUTES
class PROCESS_MEMORY_EXHAUSTION_INFO(Structure):
    Version: UInt16
    Reserved: UInt16
    Type: win32more.Windows.Win32.System.Threading.PROCESS_MEMORY_EXHAUSTION_TYPE
    Value: UIntPtr
PROCESS_MEMORY_EXHAUSTION_TYPE = Int32
PMETypeFailFastOnCommitFailure: win32more.Windows.Win32.System.Threading.PROCESS_MEMORY_EXHAUSTION_TYPE = 0
PMETypeMax: win32more.Windows.Win32.System.Threading.PROCESS_MEMORY_EXHAUSTION_TYPE = 1
PROCESS_MITIGATION_POLICY = Int32
ProcessDEPPolicy: win32more.Windows.Win32.System.Threading.PROCESS_MITIGATION_POLICY = 0
ProcessASLRPolicy: win32more.Windows.Win32.System.Threading.PROCESS_MITIGATION_POLICY = 1
ProcessDynamicCodePolicy: win32more.Windows.Win32.System.Threading.PROCESS_MITIGATION_POLICY = 2
ProcessStrictHandleCheckPolicy: win32more.Windows.Win32.System.Threading.PROCESS_MITIGATION_POLICY = 3
ProcessSystemCallDisablePolicy: win32more.Windows.Win32.System.Threading.PROCESS_MITIGATION_POLICY = 4
ProcessMitigationOptionsMask: win32more.Windows.Win32.System.Threading.PROCESS_MITIGATION_POLICY = 5
ProcessExtensionPointDisablePolicy: win32more.Windows.Win32.System.Threading.PROCESS_MITIGATION_POLICY = 6
ProcessControlFlowGuardPolicy: win32more.Windows.Win32.System.Threading.PROCESS_MITIGATION_POLICY = 7
ProcessSignaturePolicy: win32more.Windows.Win32.System.Threading.PROCESS_MITIGATION_POLICY = 8
ProcessFontDisablePolicy: win32more.Windows.Win32.System.Threading.PROCESS_MITIGATION_POLICY = 9
ProcessImageLoadPolicy: win32more.Windows.Win32.System.Threading.PROCESS_MITIGATION_POLICY = 10
ProcessSystemCallFilterPolicy: win32more.Windows.Win32.System.Threading.PROCESS_MITIGATION_POLICY = 11
ProcessPayloadRestrictionPolicy: win32more.Windows.Win32.System.Threading.PROCESS_MITIGATION_POLICY = 12
ProcessChildProcessPolicy: win32more.Windows.Win32.System.Threading.PROCESS_MITIGATION_POLICY = 13
ProcessSideChannelIsolationPolicy: win32more.Windows.Win32.System.Threading.PROCESS_MITIGATION_POLICY = 14
ProcessUserShadowStackPolicy: win32more.Windows.Win32.System.Threading.PROCESS_MITIGATION_POLICY = 15
ProcessRedirectionTrustPolicy: win32more.Windows.Win32.System.Threading.PROCESS_MITIGATION_POLICY = 16
ProcessUserPointerAuthPolicy: win32more.Windows.Win32.System.Threading.PROCESS_MITIGATION_POLICY = 17
ProcessSEHOPPolicy: win32more.Windows.Win32.System.Threading.PROCESS_MITIGATION_POLICY = 18
ProcessActivationContextTrustPolicy: win32more.Windows.Win32.System.Threading.PROCESS_MITIGATION_POLICY = 19
MaxProcessMitigationPolicy: win32more.Windows.Win32.System.Threading.PROCESS_MITIGATION_POLICY = 20
PROCESS_NAME_FORMAT = UInt32
PROCESS_NAME_WIN32: win32more.Windows.Win32.System.Threading.PROCESS_NAME_FORMAT = 0
PROCESS_NAME_NATIVE: win32more.Windows.Win32.System.Threading.PROCESS_NAME_FORMAT = 1
class PROCESS_POWER_THROTTLING_STATE(Structure):
    Version: UInt32
    ControlMask: UInt32
    StateMask: UInt32
PROCESS_PROTECTION_LEVEL = UInt32
PROTECTION_LEVEL_WINTCB_LIGHT: win32more.Windows.Win32.System.Threading.PROCESS_PROTECTION_LEVEL = 0
PROTECTION_LEVEL_WINDOWS: win32more.Windows.Win32.System.Threading.PROCESS_PROTECTION_LEVEL = 1
PROTECTION_LEVEL_WINDOWS_LIGHT: win32more.Windows.Win32.System.Threading.PROCESS_PROTECTION_LEVEL = 2
PROTECTION_LEVEL_ANTIMALWARE_LIGHT: win32more.Windows.Win32.System.Threading.PROCESS_PROTECTION_LEVEL = 3
PROTECTION_LEVEL_LSA_LIGHT: win32more.Windows.Win32.System.Threading.PROCESS_PROTECTION_LEVEL = 4
PROTECTION_LEVEL_WINTCB: win32more.Windows.Win32.System.Threading.PROCESS_PROTECTION_LEVEL = 5
PROTECTION_LEVEL_CODEGEN_LIGHT: win32more.Windows.Win32.System.Threading.PROCESS_PROTECTION_LEVEL = 6
PROTECTION_LEVEL_AUTHENTICODE: win32more.Windows.Win32.System.Threading.PROCESS_PROTECTION_LEVEL = 7
PROTECTION_LEVEL_PPL_APP: win32more.Windows.Win32.System.Threading.PROCESS_PROTECTION_LEVEL = 8
PROTECTION_LEVEL_NONE: win32more.Windows.Win32.System.Threading.PROCESS_PROTECTION_LEVEL = 4294967294
class PROCESS_PROTECTION_LEVEL_INFORMATION(Structure):
    ProtectionLevel: win32more.Windows.Win32.System.Threading.PROCESS_PROTECTION_LEVEL
PROC_THREAD_ATTRIBUTE_NUM = UInt32
ProcThreadAttributeParentProcess: win32more.Windows.Win32.System.Threading.PROC_THREAD_ATTRIBUTE_NUM = 0
ProcThreadAttributeHandleList: win32more.Windows.Win32.System.Threading.PROC_THREAD_ATTRIBUTE_NUM = 2
ProcThreadAttributeGroupAffinity: win32more.Windows.Win32.System.Threading.PROC_THREAD_ATTRIBUTE_NUM = 3
ProcThreadAttributePreferredNode: win32more.Windows.Win32.System.Threading.PROC_THREAD_ATTRIBUTE_NUM = 4
ProcThreadAttributeIdealProcessor: win32more.Windows.Win32.System.Threading.PROC_THREAD_ATTRIBUTE_NUM = 5
ProcThreadAttributeUmsThread: win32more.Windows.Win32.System.Threading.PROC_THREAD_ATTRIBUTE_NUM = 6
ProcThreadAttributeMitigationPolicy: win32more.Windows.Win32.System.Threading.PROC_THREAD_ATTRIBUTE_NUM = 7
ProcThreadAttributeSecurityCapabilities: win32more.Windows.Win32.System.Threading.PROC_THREAD_ATTRIBUTE_NUM = 9
ProcThreadAttributeProtectionLevel: win32more.Windows.Win32.System.Threading.PROC_THREAD_ATTRIBUTE_NUM = 11
ProcThreadAttributeJobList: win32more.Windows.Win32.System.Threading.PROC_THREAD_ATTRIBUTE_NUM = 13
ProcThreadAttributeChildProcessPolicy: win32more.Windows.Win32.System.Threading.PROC_THREAD_ATTRIBUTE_NUM = 14
ProcThreadAttributeAllApplicationPackagesPolicy: win32more.Windows.Win32.System.Threading.PROC_THREAD_ATTRIBUTE_NUM = 15
ProcThreadAttributeWin32kFilter: win32more.Windows.Win32.System.Threading.PROC_THREAD_ATTRIBUTE_NUM = 16
ProcThreadAttributeSafeOpenPromptOriginClaim: win32more.Windows.Win32.System.Threading.PROC_THREAD_ATTRIBUTE_NUM = 17
ProcThreadAttributeDesktopAppPolicy: win32more.Windows.Win32.System.Threading.PROC_THREAD_ATTRIBUTE_NUM = 18
ProcThreadAttributePseudoConsole: win32more.Windows.Win32.System.Threading.PROC_THREAD_ATTRIBUTE_NUM = 22
ProcThreadAttributeMitigationAuditPolicy: win32more.Windows.Win32.System.Threading.PROC_THREAD_ATTRIBUTE_NUM = 24
ProcThreadAttributeMachineType: win32more.Windows.Win32.System.Threading.PROC_THREAD_ATTRIBUTE_NUM = 25
ProcThreadAttributeComponentFilter: win32more.Windows.Win32.System.Threading.PROC_THREAD_ATTRIBUTE_NUM = 26
ProcThreadAttributeEnableOptionalXStateFeatures: win32more.Windows.Win32.System.Threading.PROC_THREAD_ATTRIBUTE_NUM = 27
ProcThreadAttributeTrustedApp: win32more.Windows.Win32.System.Threading.PROC_THREAD_ATTRIBUTE_NUM = 29
@winfunctype_pointer
def PRTL_UMS_SCHEDULER_ENTRY_POINT(Reason: win32more.Windows.Win32.System.SystemServices.RTL_UMS_SCHEDULER_REASON, ActivationPayload: UIntPtr, SchedulerParam: VoidPtr) -> Void: ...
@winfunctype_pointer
def PTIMERAPCROUTINE(lpArgToCompletionRoutine: VoidPtr, dwTimerLowValue: UInt32, dwTimerHighValue: UInt32) -> Void: ...
PTP_CALLBACK_INSTANCE = IntPtr
PTP_CLEANUP_GROUP = IntPtr
@winfunctype_pointer
def PTP_CLEANUP_GROUP_CANCEL_CALLBACK(ObjectContext: VoidPtr, CleanupContext: VoidPtr) -> Void: ...
PTP_IO = IntPtr
PTP_POOL = IntPtr
@winfunctype_pointer
def PTP_SIMPLE_CALLBACK(Instance: win32more.Windows.Win32.System.Threading.PTP_CALLBACK_INSTANCE, Context: VoidPtr) -> Void: ...
PTP_TIMER = IntPtr
@winfunctype_pointer
def PTP_TIMER_CALLBACK(Instance: win32more.Windows.Win32.System.Threading.PTP_CALLBACK_INSTANCE, Context: VoidPtr, Timer: win32more.Windows.Win32.System.Threading.PTP_TIMER) -> Void: ...
PTP_WAIT = IntPtr
@winfunctype_pointer
def PTP_WAIT_CALLBACK(Instance: win32more.Windows.Win32.System.Threading.PTP_CALLBACK_INSTANCE, Context: VoidPtr, Wait: win32more.Windows.Win32.System.Threading.PTP_WAIT, WaitResult: UInt32) -> Void: ...
@winfunctype_pointer
def PTP_WIN32_IO_CALLBACK(Instance: win32more.Windows.Win32.System.Threading.PTP_CALLBACK_INSTANCE, Context: VoidPtr, Overlapped: VoidPtr, IoResult: UInt32, NumberOfBytesTransferred: UIntPtr, Io: win32more.Windows.Win32.System.Threading.PTP_IO) -> Void: ...
PTP_WORK = IntPtr
@winfunctype_pointer
def PTP_WORK_CALLBACK(Instance: win32more.Windows.Win32.System.Threading.PTP_CALLBACK_INSTANCE, Context: VoidPtr, Work: win32more.Windows.Win32.System.Threading.PTP_WORK) -> Void: ...
QUEUE_USER_APC_FLAGS = Int32
QUEUE_USER_APC_FLAGS_NONE: win32more.Windows.Win32.System.Threading.QUEUE_USER_APC_FLAGS = 0
QUEUE_USER_APC_FLAGS_SPECIAL_USER_APC: win32more.Windows.Win32.System.Threading.QUEUE_USER_APC_FLAGS = 1
QUEUE_USER_APC_CALLBACK_DATA_CONTEXT: win32more.Windows.Win32.System.Threading.QUEUE_USER_APC_FLAGS = 65536
class REASON_CONTEXT(Structure):
    Version: UInt32
    Flags: win32more.Windows.Win32.System.Threading.POWER_REQUEST_CONTEXT_FLAGS
    Reason: _Reason_e__Union
    class _Reason_e__Union(Union):
        Detailed: _Detailed_e__Struct
        SimpleReasonString: win32more.Windows.Win32.Foundation.PWSTR
        class _Detailed_e__Struct(Structure):
            LocalizedReasonModule: win32more.Windows.Win32.Foundation.HMODULE
            LocalizedReasonId: UInt32
            ReasonStringCount: UInt32
            ReasonStrings: POINTER(win32more.Windows.Win32.Foundation.PWSTR)
class RTL_USER_PROCESS_PARAMETERS(Structure):
    Reserved1: Byte * 16
    Reserved2: VoidPtr * 10
    ImagePathName: win32more.Windows.Win32.Foundation.UNICODE_STRING
    CommandLine: win32more.Windows.Win32.Foundation.UNICODE_STRING
class RTWQASYNCRESULT(ComPtr):
    extends: win32more.Windows.Win32.System.Threading.IRtwqAsyncResult
@winfunctype_pointer
def RTWQPERIODICCALLBACK(context: win32more.Windows.Win32.System.Com.IUnknown) -> Void: ...
RTWQ_WORKQUEUE_TYPE = Int32
RTWQ_STANDARD_WORKQUEUE: win32more.Windows.Win32.System.Threading.RTWQ_WORKQUEUE_TYPE = 0
RTWQ_WINDOW_WORKQUEUE: win32more.Windows.Win32.System.Threading.RTWQ_WORKQUEUE_TYPE = 1
RTWQ_MULTITHREADED_WORKQUEUE: win32more.Windows.Win32.System.Threading.RTWQ_WORKQUEUE_TYPE = 2
class SRWLOCK(Structure):
    Ptr: VoidPtr
class STARTUPINFOA(Structure):
    cb: UInt32
    lpReserved: win32more.Windows.Win32.Foundation.PSTR
    lpDesktop: win32more.Windows.Win32.Foundation.PSTR
    lpTitle: win32more.Windows.Win32.Foundation.PSTR
    dwX: UInt32
    dwY: UInt32
    dwXSize: UInt32
    dwYSize: UInt32
    dwXCountChars: UInt32
    dwYCountChars: UInt32
    dwFillAttribute: UInt32
    dwFlags: win32more.Windows.Win32.System.Threading.STARTUPINFOW_FLAGS
    wShowWindow: UInt16
    cbReserved2: UInt16
    lpReserved2: POINTER(Byte)
    hStdInput: win32more.Windows.Win32.Foundation.HANDLE
    hStdOutput: win32more.Windows.Win32.Foundation.HANDLE
    hStdError: win32more.Windows.Win32.Foundation.HANDLE
class STARTUPINFOEXA(Structure):
    StartupInfo: win32more.Windows.Win32.System.Threading.STARTUPINFOA
    lpAttributeList: win32more.Windows.Win32.System.Threading.LPPROC_THREAD_ATTRIBUTE_LIST
class STARTUPINFOEXW(Structure):
    StartupInfo: win32more.Windows.Win32.System.Threading.STARTUPINFOW
    lpAttributeList: win32more.Windows.Win32.System.Threading.LPPROC_THREAD_ATTRIBUTE_LIST
STARTUPINFOEX = UnicodeAlias('STARTUPINFOEXW')
class STARTUPINFOW(Structure):
    cb: UInt32
    lpReserved: win32more.Windows.Win32.Foundation.PWSTR
    lpDesktop: win32more.Windows.Win32.Foundation.PWSTR
    lpTitle: win32more.Windows.Win32.Foundation.PWSTR
    dwX: UInt32
    dwY: UInt32
    dwXSize: UInt32
    dwYSize: UInt32
    dwXCountChars: UInt32
    dwYCountChars: UInt32
    dwFillAttribute: UInt32
    dwFlags: win32more.Windows.Win32.System.Threading.STARTUPINFOW_FLAGS
    wShowWindow: UInt16
    cbReserved2: UInt16
    lpReserved2: POINTER(Byte)
    hStdInput: win32more.Windows.Win32.Foundation.HANDLE
    hStdOutput: win32more.Windows.Win32.Foundation.HANDLE
    hStdError: win32more.Windows.Win32.Foundation.HANDLE
STARTUPINFO = UnicodeAlias('STARTUPINFOW')
STARTUPINFOW_FLAGS = UInt32
STARTF_FORCEONFEEDBACK: win32more.Windows.Win32.System.Threading.STARTUPINFOW_FLAGS = 64
STARTF_FORCEOFFFEEDBACK: win32more.Windows.Win32.System.Threading.STARTUPINFOW_FLAGS = 128
STARTF_PREVENTPINNING: win32more.Windows.Win32.System.Threading.STARTUPINFOW_FLAGS = 8192
STARTF_RUNFULLSCREEN: win32more.Windows.Win32.System.Threading.STARTUPINFOW_FLAGS = 32
STARTF_TITLEISAPPID: win32more.Windows.Win32.System.Threading.STARTUPINFOW_FLAGS = 4096
STARTF_TITLEISLINKNAME: win32more.Windows.Win32.System.Threading.STARTUPINFOW_FLAGS = 2048
STARTF_UNTRUSTEDSOURCE: win32more.Windows.Win32.System.Threading.STARTUPINFOW_FLAGS = 32768
STARTF_USECOUNTCHARS: win32more.Windows.Win32.System.Threading.STARTUPINFOW_FLAGS = 8
STARTF_USEFILLATTRIBUTE: win32more.Windows.Win32.System.Threading.STARTUPINFOW_FLAGS = 16
STARTF_USEHOTKEY: win32more.Windows.Win32.System.Threading.STARTUPINFOW_FLAGS = 512
STARTF_USEPOSITION: win32more.Windows.Win32.System.Threading.STARTUPINFOW_FLAGS = 4
STARTF_USESHOWWINDOW: win32more.Windows.Win32.System.Threading.STARTUPINFOW_FLAGS = 1
STARTF_USESIZE: win32more.Windows.Win32.System.Threading.STARTUPINFOW_FLAGS = 2
STARTF_USESTDHANDLES: win32more.Windows.Win32.System.Threading.STARTUPINFOW_FLAGS = 256
SYNCHRONIZATION_ACCESS_RIGHTS = UInt32
EVENT_ALL_ACCESS: win32more.Windows.Win32.System.Threading.SYNCHRONIZATION_ACCESS_RIGHTS = 2031619
EVENT_MODIFY_STATE: win32more.Windows.Win32.System.Threading.SYNCHRONIZATION_ACCESS_RIGHTS = 2
MUTEX_ALL_ACCESS: win32more.Windows.Win32.System.Threading.SYNCHRONIZATION_ACCESS_RIGHTS = 2031617
MUTEX_MODIFY_STATE: win32more.Windows.Win32.System.Threading.SYNCHRONIZATION_ACCESS_RIGHTS = 1
SEMAPHORE_ALL_ACCESS: win32more.Windows.Win32.System.Threading.SYNCHRONIZATION_ACCESS_RIGHTS = 2031619
SEMAPHORE_MODIFY_STATE: win32more.Windows.Win32.System.Threading.SYNCHRONIZATION_ACCESS_RIGHTS = 2
TIMER_ALL_ACCESS: win32more.Windows.Win32.System.Threading.SYNCHRONIZATION_ACCESS_RIGHTS = 2031619
TIMER_MODIFY_STATE: win32more.Windows.Win32.System.Threading.SYNCHRONIZATION_ACCESS_RIGHTS = 2
TIMER_QUERY_STATE: win32more.Windows.Win32.System.Threading.SYNCHRONIZATION_ACCESS_RIGHTS = 1
SYNCHRONIZATION_DELETE: win32more.Windows.Win32.System.Threading.SYNCHRONIZATION_ACCESS_RIGHTS = 65536
SYNCHRONIZATION_READ_CONTROL: win32more.Windows.Win32.System.Threading.SYNCHRONIZATION_ACCESS_RIGHTS = 131072
SYNCHRONIZATION_WRITE_DAC: win32more.Windows.Win32.System.Threading.SYNCHRONIZATION_ACCESS_RIGHTS = 262144
SYNCHRONIZATION_WRITE_OWNER: win32more.Windows.Win32.System.Threading.SYNCHRONIZATION_ACCESS_RIGHTS = 524288
SYNCHRONIZATION_SYNCHRONIZE: win32more.Windows.Win32.System.Threading.SYNCHRONIZATION_ACCESS_RIGHTS = 1048576
class SYNCHRONIZATION_BARRIER(Structure):
    Reserved1: UInt32
    Reserved2: UInt32
    Reserved3: UIntPtr * 2
    Reserved4: UInt32
    Reserved5: UInt32
class TEB(Structure):
    Reserved1: VoidPtr * 12
    ProcessEnvironmentBlock: POINTER(win32more.Windows.Win32.System.Threading.PEB)
    Reserved2: VoidPtr * 399
    Reserved3: Byte * 1952
    TlsSlots: VoidPtr * 64
    Reserved4: Byte * 8
    Reserved5: VoidPtr * 26
    ReservedForOle: VoidPtr
    Reserved6: VoidPtr * 4
    TlsExpansionSlots: VoidPtr
THREAD_ACCESS_RIGHTS = UInt32
THREAD_TERMINATE: win32more.Windows.Win32.System.Threading.THREAD_ACCESS_RIGHTS = 1
THREAD_SUSPEND_RESUME: win32more.Windows.Win32.System.Threading.THREAD_ACCESS_RIGHTS = 2
THREAD_GET_CONTEXT: win32more.Windows.Win32.System.Threading.THREAD_ACCESS_RIGHTS = 8
THREAD_SET_CONTEXT: win32more.Windows.Win32.System.Threading.THREAD_ACCESS_RIGHTS = 16
THREAD_SET_INFORMATION: win32more.Windows.Win32.System.Threading.THREAD_ACCESS_RIGHTS = 32
THREAD_QUERY_INFORMATION: win32more.Windows.Win32.System.Threading.THREAD_ACCESS_RIGHTS = 64
THREAD_SET_THREAD_TOKEN: win32more.Windows.Win32.System.Threading.THREAD_ACCESS_RIGHTS = 128
THREAD_IMPERSONATE: win32more.Windows.Win32.System.Threading.THREAD_ACCESS_RIGHTS = 256
THREAD_DIRECT_IMPERSONATION: win32more.Windows.Win32.System.Threading.THREAD_ACCESS_RIGHTS = 512
THREAD_SET_LIMITED_INFORMATION: win32more.Windows.Win32.System.Threading.THREAD_ACCESS_RIGHTS = 1024
THREAD_QUERY_LIMITED_INFORMATION: win32more.Windows.Win32.System.Threading.THREAD_ACCESS_RIGHTS = 2048
THREAD_RESUME: win32more.Windows.Win32.System.Threading.THREAD_ACCESS_RIGHTS = 4096
THREAD_ALL_ACCESS: win32more.Windows.Win32.System.Threading.THREAD_ACCESS_RIGHTS = 2097151
THREAD_DELETE: win32more.Windows.Win32.System.Threading.THREAD_ACCESS_RIGHTS = 65536
THREAD_READ_CONTROL: win32more.Windows.Win32.System.Threading.THREAD_ACCESS_RIGHTS = 131072
THREAD_WRITE_DAC: win32more.Windows.Win32.System.Threading.THREAD_ACCESS_RIGHTS = 262144
THREAD_WRITE_OWNER: win32more.Windows.Win32.System.Threading.THREAD_ACCESS_RIGHTS = 524288
THREAD_SYNCHRONIZE: win32more.Windows.Win32.System.Threading.THREAD_ACCESS_RIGHTS = 1048576
THREAD_STANDARD_RIGHTS_REQUIRED: win32more.Windows.Win32.System.Threading.THREAD_ACCESS_RIGHTS = 983040
THREAD_CREATION_FLAGS = UInt32
THREAD_CREATE_RUN_IMMEDIATELY: win32more.Windows.Win32.System.Threading.THREAD_CREATION_FLAGS = 0
THREAD_CREATE_SUSPENDED: win32more.Windows.Win32.System.Threading.THREAD_CREATION_FLAGS = 4
STACK_SIZE_PARAM_IS_A_RESERVATION: win32more.Windows.Win32.System.Threading.THREAD_CREATION_FLAGS = 65536
THREAD_INFORMATION_CLASS = Int32
ThreadMemoryPriority: win32more.Windows.Win32.System.Threading.THREAD_INFORMATION_CLASS = 0
ThreadAbsoluteCpuPriority: win32more.Windows.Win32.System.Threading.THREAD_INFORMATION_CLASS = 1
ThreadDynamicCodePolicy: win32more.Windows.Win32.System.Threading.THREAD_INFORMATION_CLASS = 2
ThreadPowerThrottling: win32more.Windows.Win32.System.Threading.THREAD_INFORMATION_CLASS = 3
ThreadInformationClassMax: win32more.Windows.Win32.System.Threading.THREAD_INFORMATION_CLASS = 4
class THREAD_POWER_THROTTLING_STATE(Structure):
    Version: UInt32
    ControlMask: UInt32
    StateMask: UInt32
THREAD_PRIORITY = Int32
THREAD_MODE_BACKGROUND_BEGIN: win32more.Windows.Win32.System.Threading.THREAD_PRIORITY = 65536
THREAD_MODE_BACKGROUND_END: win32more.Windows.Win32.System.Threading.THREAD_PRIORITY = 131072
THREAD_PRIORITY_ABOVE_NORMAL: win32more.Windows.Win32.System.Threading.THREAD_PRIORITY = 1
THREAD_PRIORITY_BELOW_NORMAL: win32more.Windows.Win32.System.Threading.THREAD_PRIORITY = -1
THREAD_PRIORITY_HIGHEST: win32more.Windows.Win32.System.Threading.THREAD_PRIORITY = 2
THREAD_PRIORITY_IDLE: win32more.Windows.Win32.System.Threading.THREAD_PRIORITY = -15
THREAD_PRIORITY_MIN: win32more.Windows.Win32.System.Threading.THREAD_PRIORITY = -2
THREAD_PRIORITY_LOWEST: win32more.Windows.Win32.System.Threading.THREAD_PRIORITY = -2
THREAD_PRIORITY_NORMAL: win32more.Windows.Win32.System.Threading.THREAD_PRIORITY = 0
THREAD_PRIORITY_TIME_CRITICAL: win32more.Windows.Win32.System.Threading.THREAD_PRIORITY = 15
class TP_CALLBACK_ENVIRON_V3(Structure):
    Version: UInt32
    Pool: win32more.Windows.Win32.System.Threading.PTP_POOL
    CleanupGroup: win32more.Windows.Win32.System.Threading.PTP_CLEANUP_GROUP
    CleanupGroupCancelCallback: win32more.Windows.Win32.System.Threading.PTP_CLEANUP_GROUP_CANCEL_CALLBACK
    RaceDll: VoidPtr
    ActivationContext: IntPtr
    FinalizationCallback: win32more.Windows.Win32.System.Threading.PTP_SIMPLE_CALLBACK
    u: _u_e__Union
    CallbackPriority: win32more.Windows.Win32.System.Threading.TP_CALLBACK_PRIORITY
    Size: UInt32
    class _u_e__Union(Union):
        Flags: UInt32
        s: _s_e__Struct
        class _s_e__Struct(Structure):
            LongFunction: Annotated[UInt32, 1]
            Persistent: Annotated[UInt32, 1]
            Private: Annotated[UInt32, 30]
TP_CALLBACK_PRIORITY = Int32
TP_CALLBACK_PRIORITY_HIGH: win32more.Windows.Win32.System.Threading.TP_CALLBACK_PRIORITY = 0
TP_CALLBACK_PRIORITY_NORMAL: win32more.Windows.Win32.System.Threading.TP_CALLBACK_PRIORITY = 1
TP_CALLBACK_PRIORITY_LOW: win32more.Windows.Win32.System.Threading.TP_CALLBACK_PRIORITY = 2
TP_CALLBACK_PRIORITY_INVALID: win32more.Windows.Win32.System.Threading.TP_CALLBACK_PRIORITY = 3
TP_CALLBACK_PRIORITY_COUNT: win32more.Windows.Win32.System.Threading.TP_CALLBACK_PRIORITY = 3
class TP_POOL_STACK_INFORMATION(Structure):
    StackReserve: UIntPtr
    StackCommit: UIntPtr
class UMS_SCHEDULER_STARTUP_INFO(Structure):
    UmsVersion: UInt32
    CompletionList: VoidPtr
    SchedulerProc: win32more.Windows.Win32.System.Threading.PRTL_UMS_SCHEDULER_ENTRY_POINT
    SchedulerParam: VoidPtr
class UMS_SYSTEM_THREAD_INFORMATION(Structure):
    UmsVersion: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        ThreadUmsFlags: UInt32
        class _Anonymous_e__Struct(Structure):
            IsUmsSchedulerThread: Annotated[UInt32, 1]
            IsUmsWorkerThread: Annotated[UInt32, 1]
UMS_THREAD_INFO_CLASS = Int32
UmsThreadInvalidInfoClass: win32more.Windows.Win32.System.Threading.UMS_THREAD_INFO_CLASS = 0
UmsThreadUserContext: win32more.Windows.Win32.System.Threading.UMS_THREAD_INFO_CLASS = 1
UmsThreadPriority: win32more.Windows.Win32.System.Threading.UMS_THREAD_INFO_CLASS = 2
UmsThreadAffinity: win32more.Windows.Win32.System.Threading.UMS_THREAD_INFO_CLASS = 3
UmsThreadTeb: win32more.Windows.Win32.System.Threading.UMS_THREAD_INFO_CLASS = 4
UmsThreadIsSuspended: win32more.Windows.Win32.System.Threading.UMS_THREAD_INFO_CLASS = 5
UmsThreadIsTerminated: win32more.Windows.Win32.System.Threading.UMS_THREAD_INFO_CLASS = 6
UmsThreadMaxInfoClass: win32more.Windows.Win32.System.Threading.UMS_THREAD_INFO_CLASS = 7
@winfunctype_pointer
def WAITORTIMERCALLBACK(param0: VoidPtr, param1: win32more.Windows.Win32.Foundation.BOOLEAN) -> Void: ...
@winfunctype_pointer
def WORKERCALLBACKFUNC(param0: VoidPtr) -> Void: ...
WORKER_THREAD_FLAGS = UInt32
WT_EXECUTEDEFAULT: win32more.Windows.Win32.System.Threading.WORKER_THREAD_FLAGS = 0
WT_EXECUTEINIOTHREAD: win32more.Windows.Win32.System.Threading.WORKER_THREAD_FLAGS = 1
WT_EXECUTEINPERSISTENTTHREAD: win32more.Windows.Win32.System.Threading.WORKER_THREAD_FLAGS = 128
WT_EXECUTEINWAITTHREAD: win32more.Windows.Win32.System.Threading.WORKER_THREAD_FLAGS = 4
WT_EXECUTELONGFUNCTION: win32more.Windows.Win32.System.Threading.WORKER_THREAD_FLAGS = 16
WT_EXECUTEONLYONCE: win32more.Windows.Win32.System.Threading.WORKER_THREAD_FLAGS = 8
WT_TRANSFER_IMPERSONATION: win32more.Windows.Win32.System.Threading.WORKER_THREAD_FLAGS = 256
WT_EXECUTEINTIMERTHREAD: win32more.Windows.Win32.System.Threading.WORKER_THREAD_FLAGS = 32


make_ready(__name__)
