from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
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
        f = globals()[f'_define_{name}']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
PRIVATE_NAMESPACE_FLAG_DESTROY = 1
PROC_THREAD_ATTRIBUTE_REPLACE_VALUE = 1
THREAD_POWER_THROTTLING_CURRENT_VERSION = 1
THREAD_POWER_THROTTLING_EXECUTION_SPEED = 1
THREAD_POWER_THROTTLING_VALID_FLAGS = 1
PME_CURRENT_VERSION = 1
PME_FAILFAST_ON_COMMIT_FAIL_DISABLE = 0
PME_FAILFAST_ON_COMMIT_FAIL_ENABLE = 1
PROCESS_POWER_THROTTLING_CURRENT_VERSION = 1
PROCESS_POWER_THROTTLING_EXECUTION_SPEED = 1
PROCESS_POWER_THROTTLING_IGNORE_TIMER_RESOLUTION = 4
PROCESS_LEAP_SECOND_INFO_FLAG_ENABLE_SIXTY_SECOND = 1
PROCESS_LEAP_SECOND_INFO_VALID_FLAGS = 1
INIT_ONCE_CHECK_ONLY = 1
INIT_ONCE_ASYNC = 2
INIT_ONCE_INIT_FAILED = 4
INIT_ONCE_CTX_RESERVED_BITS = 2
CONDITION_VARIABLE_LOCKMODE_SHARED = 1
CREATE_MUTEX_INITIAL_OWNER = 1
CREATE_WAITABLE_TIMER_MANUAL_RESET = 1
CREATE_WAITABLE_TIMER_HIGH_RESOLUTION = 2
SYNCHRONIZATION_BARRIER_FLAGS_SPIN_ONLY = 1
SYNCHRONIZATION_BARRIER_FLAGS_BLOCK_ONLY = 2
SYNCHRONIZATION_BARRIER_FLAGS_NO_DELETE = 4
PROC_THREAD_ATTRIBUTE_PARENT_PROCESS = 131072
PROC_THREAD_ATTRIBUTE_HANDLE_LIST = 131074
PROC_THREAD_ATTRIBUTE_GROUP_AFFINITY = 196611
PROC_THREAD_ATTRIBUTE_PREFERRED_NODE = 131076
PROC_THREAD_ATTRIBUTE_IDEAL_PROCESSOR = 196613
PROC_THREAD_ATTRIBUTE_UMS_THREAD = 196614
PROC_THREAD_ATTRIBUTE_MITIGATION_POLICY = 131079
PROC_THREAD_ATTRIBUTE_SECURITY_CAPABILITIES = 131081
PROC_THREAD_ATTRIBUTE_PROTECTION_LEVEL = 131083
PROC_THREAD_ATTRIBUTE_PSEUDOCONSOLE = 131094
PROC_THREAD_ATTRIBUTE_MACHINE_TYPE = 131097
PROC_THREAD_ATTRIBUTE_ENABLE_OPTIONAL_XSTATE_FEATURES = 196635
PROC_THREAD_ATTRIBUTE_WIN32K_FILTER = 131088
PROC_THREAD_ATTRIBUTE_JOB_LIST = 131085
PROC_THREAD_ATTRIBUTE_CHILD_PROCESS_POLICY = 131086
PROC_THREAD_ATTRIBUTE_ALL_APPLICATION_PACKAGES_POLICY = 131087
PROC_THREAD_ATTRIBUTE_DESKTOP_APP_POLICY = 131090
PROC_THREAD_ATTRIBUTE_MITIGATION_AUDIT_POLICY = 131096
PROC_THREAD_ATTRIBUTE_COMPONENT_FILTER = 131098
def _define_GetProcessWorkingSetSize():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(UIntPtr),POINTER(UIntPtr))(('GetProcessWorkingSetSize', windll['KERNEL32.dll']), ((1, 'hProcess'),(1, 'lpMinimumWorkingSetSize'),(1, 'lpMaximumWorkingSetSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetProcessWorkingSetSize():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UIntPtr,UIntPtr)(('SetProcessWorkingSetSize', windll['KERNEL32.dll']), ((1, 'hProcess'),(1, 'dwMinimumWorkingSetSize'),(1, 'dwMaximumWorkingSetSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FlsAlloc():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Threading.PFLS_CALLBACK_FUNCTION)(('FlsAlloc', windll['KERNEL32.dll']), ((1, 'lpCallback'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FlsGetValue():
    try:
        return WINFUNCTYPE(c_void_p,UInt32)(('FlsGetValue', windll['KERNEL32.dll']), ((1, 'dwFlsIndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FlsSetValue():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,c_void_p)(('FlsSetValue', windll['KERNEL32.dll']), ((1, 'dwFlsIndex'),(1, 'lpFlsData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FlsFree():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32)(('FlsFree', windll['KERNEL32.dll']), ((1, 'dwFlsIndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsThreadAFiber():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,)(('IsThreadAFiber', windll['KERNEL32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitializeSRWLock():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Threading.RTL_SRWLOCK_head))(('InitializeSRWLock', windll['KERNEL32.dll']), ((1, 'SRWLock'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReleaseSRWLockExclusive():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Threading.RTL_SRWLOCK_head))(('ReleaseSRWLockExclusive', windll['KERNEL32.dll']), ((1, 'SRWLock'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReleaseSRWLockShared():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Threading.RTL_SRWLOCK_head))(('ReleaseSRWLockShared', windll['KERNEL32.dll']), ((1, 'SRWLock'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AcquireSRWLockExclusive():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Threading.RTL_SRWLOCK_head))(('AcquireSRWLockExclusive', windll['KERNEL32.dll']), ((1, 'SRWLock'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AcquireSRWLockShared():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Threading.RTL_SRWLOCK_head))(('AcquireSRWLockShared', windll['KERNEL32.dll']), ((1, 'SRWLock'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TryAcquireSRWLockExclusive():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,POINTER(win32more.System.Threading.RTL_SRWLOCK_head))(('TryAcquireSRWLockExclusive', windll['KERNEL32.dll']), ((1, 'SRWLock'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TryAcquireSRWLockShared():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,POINTER(win32more.System.Threading.RTL_SRWLOCK_head))(('TryAcquireSRWLockShared', windll['KERNEL32.dll']), ((1, 'SRWLock'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitializeCriticalSection():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Threading.RTL_CRITICAL_SECTION_head))(('InitializeCriticalSection', windll['KERNEL32.dll']), ((1, 'lpCriticalSection'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnterCriticalSection():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Threading.RTL_CRITICAL_SECTION_head))(('EnterCriticalSection', windll['KERNEL32.dll']), ((1, 'lpCriticalSection'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LeaveCriticalSection():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Threading.RTL_CRITICAL_SECTION_head))(('LeaveCriticalSection', windll['KERNEL32.dll']), ((1, 'lpCriticalSection'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitializeCriticalSectionAndSpinCount():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Threading.RTL_CRITICAL_SECTION_head),UInt32)(('InitializeCriticalSectionAndSpinCount', windll['KERNEL32.dll']), ((1, 'lpCriticalSection'),(1, 'dwSpinCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitializeCriticalSectionEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Threading.RTL_CRITICAL_SECTION_head),UInt32,UInt32)(('InitializeCriticalSectionEx', windll['KERNEL32.dll']), ((1, 'lpCriticalSection'),(1, 'dwSpinCount'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetCriticalSectionSpinCount():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Threading.RTL_CRITICAL_SECTION_head),UInt32)(('SetCriticalSectionSpinCount', windll['KERNEL32.dll']), ((1, 'lpCriticalSection'),(1, 'dwSpinCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TryEnterCriticalSection():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Threading.RTL_CRITICAL_SECTION_head))(('TryEnterCriticalSection', windll['KERNEL32.dll']), ((1, 'lpCriticalSection'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeleteCriticalSection():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Threading.RTL_CRITICAL_SECTION_head))(('DeleteCriticalSection', windll['KERNEL32.dll']), ((1, 'lpCriticalSection'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitOnceInitialize():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Threading.RTL_RUN_ONCE_head))(('InitOnceInitialize', windll['KERNEL32.dll']), ((1, 'InitOnce'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitOnceExecuteOnce():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Threading.RTL_RUN_ONCE_head),win32more.System.Threading.PINIT_ONCE_FN,c_void_p,POINTER(c_void_p))(('InitOnceExecuteOnce', windll['KERNEL32.dll']), ((1, 'InitOnce'),(1, 'InitFn'),(1, 'Parameter'),(1, 'Context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitOnceBeginInitialize():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Threading.RTL_RUN_ONCE_head),UInt32,POINTER(win32more.Foundation.BOOL),POINTER(c_void_p))(('InitOnceBeginInitialize', windll['KERNEL32.dll']), ((1, 'lpInitOnce'),(1, 'dwFlags'),(1, 'fPending'),(1, 'lpContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitOnceComplete():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Threading.RTL_RUN_ONCE_head),UInt32,c_void_p)(('InitOnceComplete', windll['KERNEL32.dll']), ((1, 'lpInitOnce'),(1, 'dwFlags'),(1, 'lpContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitializeConditionVariable():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Threading.RTL_CONDITION_VARIABLE_head))(('InitializeConditionVariable', windll['KERNEL32.dll']), ((1, 'ConditionVariable'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WakeConditionVariable():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Threading.RTL_CONDITION_VARIABLE_head))(('WakeConditionVariable', windll['KERNEL32.dll']), ((1, 'ConditionVariable'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WakeAllConditionVariable():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Threading.RTL_CONDITION_VARIABLE_head))(('WakeAllConditionVariable', windll['KERNEL32.dll']), ((1, 'ConditionVariable'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SleepConditionVariableCS():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Threading.RTL_CONDITION_VARIABLE_head),POINTER(win32more.System.Threading.RTL_CRITICAL_SECTION_head),UInt32)(('SleepConditionVariableCS', windll['KERNEL32.dll']), ((1, 'ConditionVariable'),(1, 'CriticalSection'),(1, 'dwMilliseconds'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SleepConditionVariableSRW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Threading.RTL_CONDITION_VARIABLE_head),POINTER(win32more.System.Threading.RTL_SRWLOCK_head),UInt32,UInt32)(('SleepConditionVariableSRW', windll['KERNEL32.dll']), ((1, 'ConditionVariable'),(1, 'SRWLock'),(1, 'dwMilliseconds'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetEvent():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE)(('SetEvent', windll['KERNEL32.dll']), ((1, 'hEvent'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ResetEvent():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE)(('ResetEvent', windll['KERNEL32.dll']), ((1, 'hEvent'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReleaseSemaphore():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,Int32,POINTER(Int32))(('ReleaseSemaphore', windll['KERNEL32.dll']), ((1, 'hSemaphore'),(1, 'lReleaseCount'),(1, 'lpPreviousCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReleaseMutex():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE)(('ReleaseMutex', windll['KERNEL32.dll']), ((1, 'hMutex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WaitForSingleObject():
    try:
        return WINFUNCTYPE(win32more.Foundation.WIN32_ERROR,win32more.Foundation.HANDLE,UInt32)(('WaitForSingleObject', windll['KERNEL32.dll']), ((1, 'hHandle'),(1, 'dwMilliseconds'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SleepEx():
    try:
        return WINFUNCTYPE(UInt32,UInt32,win32more.Foundation.BOOL)(('SleepEx', windll['KERNEL32.dll']), ((1, 'dwMilliseconds'),(1, 'bAlertable'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WaitForSingleObjectEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.WIN32_ERROR,win32more.Foundation.HANDLE,UInt32,win32more.Foundation.BOOL)(('WaitForSingleObjectEx', windll['KERNEL32.dll']), ((1, 'hHandle'),(1, 'dwMilliseconds'),(1, 'bAlertable'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WaitForMultipleObjectsEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.WIN32_ERROR,UInt32,POINTER(win32more.Foundation.HANDLE),win32more.Foundation.BOOL,UInt32,win32more.Foundation.BOOL)(('WaitForMultipleObjectsEx', windll['KERNEL32.dll']), ((1, 'nCount'),(1, 'lpHandles'),(1, 'bWaitAll'),(1, 'dwMilliseconds'),(1, 'bAlertable'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateMutexA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),win32more.Foundation.BOOL,win32more.Foundation.PSTR)(('CreateMutexA', windll['KERNEL32.dll']), ((1, 'lpMutexAttributes'),(1, 'bInitialOwner'),(1, 'lpName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateMutexW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),win32more.Foundation.BOOL,win32more.Foundation.PWSTR)(('CreateMutexW', windll['KERNEL32.dll']), ((1, 'lpMutexAttributes'),(1, 'bInitialOwner'),(1, 'lpName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenMutexW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.System.Threading.SYNCHRONIZATION_ACCESS_RIGHTS,win32more.Foundation.BOOL,win32more.Foundation.PWSTR)(('OpenMutexW', windll['KERNEL32.dll']), ((1, 'dwDesiredAccess'),(1, 'bInheritHandle'),(1, 'lpName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateEventA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),win32more.Foundation.BOOL,win32more.Foundation.BOOL,win32more.Foundation.PSTR)(('CreateEventA', windll['KERNEL32.dll']), ((1, 'lpEventAttributes'),(1, 'bManualReset'),(1, 'bInitialState'),(1, 'lpName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateEventW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),win32more.Foundation.BOOL,win32more.Foundation.BOOL,win32more.Foundation.PWSTR)(('CreateEventW', windll['KERNEL32.dll']), ((1, 'lpEventAttributes'),(1, 'bManualReset'),(1, 'bInitialState'),(1, 'lpName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenEventA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.System.Threading.SYNCHRONIZATION_ACCESS_RIGHTS,win32more.Foundation.BOOL,win32more.Foundation.PSTR)(('OpenEventA', windll['KERNEL32.dll']), ((1, 'dwDesiredAccess'),(1, 'bInheritHandle'),(1, 'lpName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenEventW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.System.Threading.SYNCHRONIZATION_ACCESS_RIGHTS,win32more.Foundation.BOOL,win32more.Foundation.PWSTR)(('OpenEventW', windll['KERNEL32.dll']), ((1, 'dwDesiredAccess'),(1, 'bInheritHandle'),(1, 'lpName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenSemaphoreW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.System.Threading.SYNCHRONIZATION_ACCESS_RIGHTS,win32more.Foundation.BOOL,win32more.Foundation.PWSTR)(('OpenSemaphoreW', windll['KERNEL32.dll']), ((1, 'dwDesiredAccess'),(1, 'bInheritHandle'),(1, 'lpName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenWaitableTimerW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.System.Threading.SYNCHRONIZATION_ACCESS_RIGHTS,win32more.Foundation.BOOL,win32more.Foundation.PWSTR)(('OpenWaitableTimerW', windll['KERNEL32.dll']), ((1, 'dwDesiredAccess'),(1, 'bInheritHandle'),(1, 'lpTimerName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetWaitableTimerEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.LARGE_INTEGER_head),Int32,win32more.System.Threading.PTIMERAPCROUTINE,c_void_p,POINTER(win32more.System.Threading.REASON_CONTEXT_head),UInt32)(('SetWaitableTimerEx', windll['KERNEL32.dll']), ((1, 'hTimer'),(1, 'lpDueTime'),(1, 'lPeriod'),(1, 'pfnCompletionRoutine'),(1, 'lpArgToCompletionRoutine'),(1, 'WakeContext'),(1, 'TolerableDelay'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetWaitableTimer():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.LARGE_INTEGER_head),Int32,win32more.System.Threading.PTIMERAPCROUTINE,c_void_p,win32more.Foundation.BOOL)(('SetWaitableTimer', windll['KERNEL32.dll']), ((1, 'hTimer'),(1, 'lpDueTime'),(1, 'lPeriod'),(1, 'pfnCompletionRoutine'),(1, 'lpArgToCompletionRoutine'),(1, 'fResume'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CancelWaitableTimer():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE)(('CancelWaitableTimer', windll['KERNEL32.dll']), ((1, 'hTimer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateMutexExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),win32more.Foundation.PSTR,UInt32,UInt32)(('CreateMutexExA', windll['KERNEL32.dll']), ((1, 'lpMutexAttributes'),(1, 'lpName'),(1, 'dwFlags'),(1, 'dwDesiredAccess'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateMutexExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),win32more.Foundation.PWSTR,UInt32,UInt32)(('CreateMutexExW', windll['KERNEL32.dll']), ((1, 'lpMutexAttributes'),(1, 'lpName'),(1, 'dwFlags'),(1, 'dwDesiredAccess'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateEventExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),win32more.Foundation.PSTR,win32more.System.Threading.CREATE_EVENT,UInt32)(('CreateEventExA', windll['KERNEL32.dll']), ((1, 'lpEventAttributes'),(1, 'lpName'),(1, 'dwFlags'),(1, 'dwDesiredAccess'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateEventExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),win32more.Foundation.PWSTR,win32more.System.Threading.CREATE_EVENT,UInt32)(('CreateEventExW', windll['KERNEL32.dll']), ((1, 'lpEventAttributes'),(1, 'lpName'),(1, 'dwFlags'),(1, 'dwDesiredAccess'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateSemaphoreExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),Int32,Int32,win32more.Foundation.PWSTR,UInt32,UInt32)(('CreateSemaphoreExW', windll['KERNEL32.dll']), ((1, 'lpSemaphoreAttributes'),(1, 'lInitialCount'),(1, 'lMaximumCount'),(1, 'lpName'),(1, 'dwFlags'),(1, 'dwDesiredAccess'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateWaitableTimerExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),win32more.Foundation.PWSTR,UInt32,UInt32)(('CreateWaitableTimerExW', windll['KERNEL32.dll']), ((1, 'lpTimerAttributes'),(1, 'lpTimerName'),(1, 'dwFlags'),(1, 'dwDesiredAccess'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnterSynchronizationBarrier():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Threading.RTL_BARRIER_head),UInt32)(('EnterSynchronizationBarrier', windll['KERNEL32.dll']), ((1, 'lpBarrier'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitializeSynchronizationBarrier():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Threading.RTL_BARRIER_head),Int32,Int32)(('InitializeSynchronizationBarrier', windll['KERNEL32.dll']), ((1, 'lpBarrier'),(1, 'lTotalThreads'),(1, 'lSpinCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeleteSynchronizationBarrier():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Threading.RTL_BARRIER_head))(('DeleteSynchronizationBarrier', windll['KERNEL32.dll']), ((1, 'lpBarrier'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Sleep():
    try:
        return WINFUNCTYPE(Void,UInt32)(('Sleep', windll['KERNEL32.dll']), ((1, 'dwMilliseconds'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WaitOnAddress():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,c_void_p,UIntPtr,UInt32)(('WaitOnAddress', windll['api-ms-win-core-synch-l1-2-0.dll']), ((1, 'Address'),(1, 'CompareAddress'),(1, 'AddressSize'),(1, 'dwMilliseconds'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WakeByAddressSingle():
    try:
        return WINFUNCTYPE(Void,c_void_p)(('WakeByAddressSingle', windll['api-ms-win-core-synch-l1-2-0.dll']), ((1, 'Address'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WakeByAddressAll():
    try:
        return WINFUNCTYPE(Void,c_void_p)(('WakeByAddressAll', windll['api-ms-win-core-synch-l1-2-0.dll']), ((1, 'Address'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WaitForMultipleObjects():
    try:
        return WINFUNCTYPE(win32more.Foundation.WIN32_ERROR,UInt32,POINTER(win32more.Foundation.HANDLE),win32more.Foundation.BOOL,UInt32)(('WaitForMultipleObjects', windll['KERNEL32.dll']), ((1, 'nCount'),(1, 'lpHandles'),(1, 'bWaitAll'),(1, 'dwMilliseconds'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateSemaphoreW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),Int32,Int32,win32more.Foundation.PWSTR)(('CreateSemaphoreW', windll['KERNEL32.dll']), ((1, 'lpSemaphoreAttributes'),(1, 'lInitialCount'),(1, 'lMaximumCount'),(1, 'lpName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateWaitableTimerW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),win32more.Foundation.BOOL,win32more.Foundation.PWSTR)(('CreateWaitableTimerW', windll['KERNEL32.dll']), ((1, 'lpTimerAttributes'),(1, 'bManualReset'),(1, 'lpTimerName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitializeSListHead():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Kernel.SLIST_HEADER_head))(('InitializeSListHead', windll['KERNEL32.dll']), ((1, 'ListHead'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InterlockedPopEntrySList():
    try:
        return WINFUNCTYPE(POINTER(win32more.System.Kernel.SLIST_ENTRY_head),POINTER(win32more.System.Kernel.SLIST_HEADER_head))(('InterlockedPopEntrySList', windll['KERNEL32.dll']), ((1, 'ListHead'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InterlockedPushEntrySList():
    try:
        return WINFUNCTYPE(POINTER(win32more.System.Kernel.SLIST_ENTRY_head),POINTER(win32more.System.Kernel.SLIST_HEADER_head),POINTER(win32more.System.Kernel.SLIST_ENTRY_head))(('InterlockedPushEntrySList', windll['KERNEL32.dll']), ((1, 'ListHead'),(1, 'ListEntry'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InterlockedPushListSListEx():
    try:
        return WINFUNCTYPE(POINTER(win32more.System.Kernel.SLIST_ENTRY_head),POINTER(win32more.System.Kernel.SLIST_HEADER_head),POINTER(win32more.System.Kernel.SLIST_ENTRY_head),POINTER(win32more.System.Kernel.SLIST_ENTRY_head),UInt32)(('InterlockedPushListSListEx', windll['KERNEL32.dll']), ((1, 'ListHead'),(1, 'List'),(1, 'ListEnd'),(1, 'Count'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InterlockedFlushSList():
    try:
        return WINFUNCTYPE(POINTER(win32more.System.Kernel.SLIST_ENTRY_head),POINTER(win32more.System.Kernel.SLIST_HEADER_head))(('InterlockedFlushSList', windll['KERNEL32.dll']), ((1, 'ListHead'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryDepthSList():
    try:
        return WINFUNCTYPE(UInt16,POINTER(win32more.System.Kernel.SLIST_HEADER_head))(('QueryDepthSList', windll['KERNEL32.dll']), ((1, 'ListHead'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueueUserAPC():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PAPCFUNC,win32more.Foundation.HANDLE,UIntPtr)(('QueueUserAPC', windll['KERNEL32.dll']), ((1, 'pfnAPC'),(1, 'hThread'),(1, 'dwData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueueUserAPC2():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PAPCFUNC,win32more.Foundation.HANDLE,UIntPtr,win32more.System.Threading.QUEUE_USER_APC_FLAGS)(('QueueUserAPC2', windll['KERNEL32.dll']), ((1, 'ApcRoutine'),(1, 'Thread'),(1, 'Data'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetProcessTimes():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.FILETIME_head),POINTER(win32more.Foundation.FILETIME_head),POINTER(win32more.Foundation.FILETIME_head),POINTER(win32more.Foundation.FILETIME_head))(('GetProcessTimes', windll['KERNEL32.dll']), ((1, 'hProcess'),(1, 'lpCreationTime'),(1, 'lpExitTime'),(1, 'lpKernelTime'),(1, 'lpUserTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCurrentProcess():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,)(('GetCurrentProcess', windll['KERNEL32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCurrentProcessId():
    try:
        return WINFUNCTYPE(UInt32,)(('GetCurrentProcessId', windll['KERNEL32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_ExitProcess():
    try:
        return WINFUNCTYPE(Void,UInt32)(('ExitProcess', windll['KERNEL32.dll']), ((1, 'uExitCode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TerminateProcess():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32)(('TerminateProcess', windll['KERNEL32.dll']), ((1, 'hProcess'),(1, 'uExitCode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetExitCodeProcess():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(UInt32))(('GetExitCodeProcess', windll['KERNEL32.dll']), ((1, 'hProcess'),(1, 'lpExitCode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SwitchToThread():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,)(('SwitchToThread', windll['KERNEL32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateThread():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),UIntPtr,win32more.System.Threading.LPTHREAD_START_ROUTINE,c_void_p,win32more.System.Threading.THREAD_CREATION_FLAGS,POINTER(UInt32))(('CreateThread', windll['KERNEL32.dll']), ((1, 'lpThreadAttributes'),(1, 'dwStackSize'),(1, 'lpStartAddress'),(1, 'lpParameter'),(1, 'dwCreationFlags'),(1, 'lpThreadId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateRemoteThread():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),UIntPtr,win32more.System.Threading.LPTHREAD_START_ROUTINE,c_void_p,UInt32,POINTER(UInt32))(('CreateRemoteThread', windll['KERNEL32.dll']), ((1, 'hProcess'),(1, 'lpThreadAttributes'),(1, 'dwStackSize'),(1, 'lpStartAddress'),(1, 'lpParameter'),(1, 'dwCreationFlags'),(1, 'lpThreadId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCurrentThread():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,)(('GetCurrentThread', windll['KERNEL32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCurrentThreadId():
    try:
        return WINFUNCTYPE(UInt32,)(('GetCurrentThreadId', windll['KERNEL32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenThread():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.System.Threading.THREAD_ACCESS_RIGHTS,win32more.Foundation.BOOL,UInt32)(('OpenThread', windll['KERNEL32.dll']), ((1, 'dwDesiredAccess'),(1, 'bInheritHandle'),(1, 'dwThreadId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetThreadPriority():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.System.Threading.THREAD_PRIORITY)(('SetThreadPriority', windll['KERNEL32.dll']), ((1, 'hThread'),(1, 'nPriority'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetThreadPriorityBoost():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.BOOL)(('SetThreadPriorityBoost', windll['KERNEL32.dll']), ((1, 'hThread'),(1, 'bDisablePriorityBoost'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetThreadPriorityBoost():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.BOOL))(('GetThreadPriorityBoost', windll['KERNEL32.dll']), ((1, 'hThread'),(1, 'pDisablePriorityBoost'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetThreadPriority():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE)(('GetThreadPriority', windll['KERNEL32.dll']), ((1, 'hThread'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ExitThread():
    try:
        return WINFUNCTYPE(Void,UInt32)(('ExitThread', windll['KERNEL32.dll']), ((1, 'dwExitCode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TerminateThread():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32)(('TerminateThread', windll['KERNEL32.dll']), ((1, 'hThread'),(1, 'dwExitCode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetExitCodeThread():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(UInt32))(('GetExitCodeThread', windll['KERNEL32.dll']), ((1, 'hThread'),(1, 'lpExitCode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SuspendThread():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE)(('SuspendThread', windll['KERNEL32.dll']), ((1, 'hThread'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ResumeThread():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE)(('ResumeThread', windll['KERNEL32.dll']), ((1, 'hThread'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TlsAlloc():
    try:
        return WINFUNCTYPE(UInt32,)(('TlsAlloc', windll['KERNEL32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_TlsGetValue():
    try:
        return WINFUNCTYPE(c_void_p,UInt32)(('TlsGetValue', windll['KERNEL32.dll']), ((1, 'dwTlsIndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TlsSetValue():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,c_void_p)(('TlsSetValue', windll['KERNEL32.dll']), ((1, 'dwTlsIndex'),(1, 'lpTlsValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TlsFree():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32)(('TlsFree', windll['KERNEL32.dll']), ((1, 'dwTlsIndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateProcessA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),win32more.Foundation.BOOL,win32more.System.Threading.PROCESS_CREATION_FLAGS,c_void_p,win32more.Foundation.PSTR,POINTER(win32more.System.Threading.STARTUPINFOA_head),POINTER(win32more.System.Threading.PROCESS_INFORMATION_head))(('CreateProcessA', windll['KERNEL32.dll']), ((1, 'lpApplicationName'),(1, 'lpCommandLine'),(1, 'lpProcessAttributes'),(1, 'lpThreadAttributes'),(1, 'bInheritHandles'),(1, 'dwCreationFlags'),(1, 'lpEnvironment'),(1, 'lpCurrentDirectory'),(1, 'lpStartupInfo'),(1, 'lpProcessInformation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateProcessW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),win32more.Foundation.BOOL,win32more.System.Threading.PROCESS_CREATION_FLAGS,c_void_p,win32more.Foundation.PWSTR,POINTER(win32more.System.Threading.STARTUPINFOW_head),POINTER(win32more.System.Threading.PROCESS_INFORMATION_head))(('CreateProcessW', windll['KERNEL32.dll']), ((1, 'lpApplicationName'),(1, 'lpCommandLine'),(1, 'lpProcessAttributes'),(1, 'lpThreadAttributes'),(1, 'bInheritHandles'),(1, 'dwCreationFlags'),(1, 'lpEnvironment'),(1, 'lpCurrentDirectory'),(1, 'lpStartupInfo'),(1, 'lpProcessInformation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetProcessShutdownParameters():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,UInt32)(('SetProcessShutdownParameters', windll['KERNEL32.dll']), ((1, 'dwLevel'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetProcessVersion():
    try:
        return WINFUNCTYPE(UInt32,UInt32)(('GetProcessVersion', windll['KERNEL32.dll']), ((1, 'ProcessId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetStartupInfoW():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Threading.STARTUPINFOW_head))(('GetStartupInfoW', windll['KERNEL32.dll']), ((1, 'lpStartupInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateProcessAsUserW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),win32more.Foundation.BOOL,UInt32,c_void_p,win32more.Foundation.PWSTR,POINTER(win32more.System.Threading.STARTUPINFOW_head),POINTER(win32more.System.Threading.PROCESS_INFORMATION_head))(('CreateProcessAsUserW', windll['ADVAPI32.dll']), ((1, 'hToken'),(1, 'lpApplicationName'),(1, 'lpCommandLine'),(1, 'lpProcessAttributes'),(1, 'lpThreadAttributes'),(1, 'bInheritHandles'),(1, 'dwCreationFlags'),(1, 'lpEnvironment'),(1, 'lpCurrentDirectory'),(1, 'lpStartupInfo'),(1, 'lpProcessInformation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetThreadToken():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.HANDLE),win32more.Foundation.HANDLE)(('SetThreadToken', windll['ADVAPI32.dll']), ((1, 'Thread'),(1, 'Token'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenProcessToken():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Security.TOKEN_ACCESS_MASK,POINTER(win32more.Foundation.HANDLE))(('OpenProcessToken', windll['ADVAPI32.dll']), ((1, 'ProcessHandle'),(1, 'DesiredAccess'),(1, 'TokenHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenThreadToken():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Security.TOKEN_ACCESS_MASK,win32more.Foundation.BOOL,POINTER(win32more.Foundation.HANDLE))(('OpenThreadToken', windll['ADVAPI32.dll']), ((1, 'ThreadHandle'),(1, 'DesiredAccess'),(1, 'OpenAsSelf'),(1, 'TokenHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetPriorityClass():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.System.Threading.PROCESS_CREATION_FLAGS)(('SetPriorityClass', windll['KERNEL32.dll']), ((1, 'hProcess'),(1, 'dwPriorityClass'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPriorityClass():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE)(('GetPriorityClass', windll['KERNEL32.dll']), ((1, 'hProcess'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetThreadStackGuarantee():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(UInt32))(('SetThreadStackGuarantee', windll['KERNEL32.dll']), ((1, 'StackSizeInBytes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetProcessId():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE)(('GetProcessId', windll['KERNEL32.dll']), ((1, 'Process'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetThreadId():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE)(('GetThreadId', windll['KERNEL32.dll']), ((1, 'Thread'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FlushProcessWriteBuffers():
    try:
        return WINFUNCTYPE(Void,)(('FlushProcessWriteBuffers', windll['KERNEL32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetProcessIdOfThread():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE)(('GetProcessIdOfThread', windll['KERNEL32.dll']), ((1, 'Thread'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitializeProcThreadAttributeList():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.Threading.LPPROC_THREAD_ATTRIBUTE_LIST,UInt32,UInt32,POINTER(UIntPtr))(('InitializeProcThreadAttributeList', windll['KERNEL32.dll']), ((1, 'lpAttributeList'),(1, 'dwAttributeCount'),(1, 'dwFlags'),(1, 'lpSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeleteProcThreadAttributeList():
    try:
        return WINFUNCTYPE(Void,win32more.System.Threading.LPPROC_THREAD_ATTRIBUTE_LIST)(('DeleteProcThreadAttributeList', windll['KERNEL32.dll']), ((1, 'lpAttributeList'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UpdateProcThreadAttribute():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.Threading.LPPROC_THREAD_ATTRIBUTE_LIST,UInt32,UIntPtr,c_void_p,UIntPtr,c_void_p,POINTER(UIntPtr))(('UpdateProcThreadAttribute', windll['KERNEL32.dll']), ((1, 'lpAttributeList'),(1, 'dwFlags'),(1, 'Attribute'),(1, 'lpValue'),(1, 'cbSize'),(1, 'lpPreviousValue'),(1, 'lpReturnSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetProcessDynamicEHContinuationTargets():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt16,POINTER(win32more.System.Threading.PROCESS_DYNAMIC_EH_CONTINUATION_TARGET_head))(('SetProcessDynamicEHContinuationTargets', windll['KERNEL32.dll']), ((1, 'Process'),(1, 'NumberOfTargets'),(1, 'Targets'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetProcessDynamicEnforcedCetCompatibleRanges():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt16,POINTER(win32more.System.Threading.PROCESS_DYNAMIC_ENFORCED_ADDRESS_RANGE_head))(('SetProcessDynamicEnforcedCetCompatibleRanges', windll['KERNEL32.dll']), ((1, 'Process'),(1, 'NumberOfRanges'),(1, 'Ranges'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetProcessAffinityUpdateMode():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.System.Threading.PROCESS_AFFINITY_AUTO_UPDATE_FLAGS)(('SetProcessAffinityUpdateMode', windll['KERNEL32.dll']), ((1, 'hProcess'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryProcessAffinityUpdateMode():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.Threading.PROCESS_AFFINITY_AUTO_UPDATE_FLAGS))(('QueryProcessAffinityUpdateMode', windll['KERNEL32.dll']), ((1, 'hProcess'),(1, 'lpdwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateRemoteThreadEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),UIntPtr,win32more.System.Threading.LPTHREAD_START_ROUTINE,c_void_p,UInt32,win32more.System.Threading.LPPROC_THREAD_ATTRIBUTE_LIST,POINTER(UInt32))(('CreateRemoteThreadEx', windll['KERNEL32.dll']), ((1, 'hProcess'),(1, 'lpThreadAttributes'),(1, 'dwStackSize'),(1, 'lpStartAddress'),(1, 'lpParameter'),(1, 'dwCreationFlags'),(1, 'lpAttributeList'),(1, 'lpThreadId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCurrentThreadStackLimits():
    try:
        return WINFUNCTYPE(Void,POINTER(UIntPtr),POINTER(UIntPtr))(('GetCurrentThreadStackLimits', windll['KERNEL32.dll']), ((1, 'LowLimit'),(1, 'HighLimit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetProcessMitigationPolicy():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.System.Threading.PROCESS_MITIGATION_POLICY,c_void_p,UIntPtr)(('GetProcessMitigationPolicy', windll['KERNEL32.dll']), ((1, 'hProcess'),(1, 'MitigationPolicy'),(1, 'lpBuffer'),(1, 'dwLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetProcessMitigationPolicy():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.Threading.PROCESS_MITIGATION_POLICY,c_void_p,UIntPtr)(('SetProcessMitigationPolicy', windll['KERNEL32.dll']), ((1, 'MitigationPolicy'),(1, 'lpBuffer'),(1, 'dwLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetThreadTimes():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.FILETIME_head),POINTER(win32more.Foundation.FILETIME_head),POINTER(win32more.Foundation.FILETIME_head),POINTER(win32more.Foundation.FILETIME_head))(('GetThreadTimes', windll['KERNEL32.dll']), ((1, 'hThread'),(1, 'lpCreationTime'),(1, 'lpExitTime'),(1, 'lpKernelTime'),(1, 'lpUserTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenProcess():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.System.Threading.PROCESS_ACCESS_RIGHTS,win32more.Foundation.BOOL,UInt32)(('OpenProcess', windll['KERNEL32.dll']), ((1, 'dwDesiredAccess'),(1, 'bInheritHandle'),(1, 'dwProcessId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsProcessorFeaturePresent():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.Threading.PROCESSOR_FEATURE_ID)(('IsProcessorFeaturePresent', windll['KERNEL32.dll']), ((1, 'ProcessorFeature'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetProcessHandleCount():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(UInt32))(('GetProcessHandleCount', windll['KERNEL32.dll']), ((1, 'hProcess'),(1, 'pdwHandleCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCurrentProcessorNumber():
    try:
        return WINFUNCTYPE(UInt32,)(('GetCurrentProcessorNumber', windll['KERNEL32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetThreadIdealProcessorEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.Kernel.PROCESSOR_NUMBER_head),POINTER(win32more.System.Kernel.PROCESSOR_NUMBER_head))(('SetThreadIdealProcessorEx', windll['KERNEL32.dll']), ((1, 'hThread'),(1, 'lpIdealProcessor'),(1, 'lpPreviousIdealProcessor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetThreadIdealProcessorEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.Kernel.PROCESSOR_NUMBER_head))(('GetThreadIdealProcessorEx', windll['KERNEL32.dll']), ((1, 'hThread'),(1, 'lpIdealProcessor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCurrentProcessorNumberEx():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Kernel.PROCESSOR_NUMBER_head))(('GetCurrentProcessorNumberEx', windll['KERNEL32.dll']), ((1, 'ProcNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetProcessPriorityBoost():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.BOOL))(('GetProcessPriorityBoost', windll['KERNEL32.dll']), ((1, 'hProcess'),(1, 'pDisablePriorityBoost'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetProcessPriorityBoost():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.BOOL)(('SetProcessPriorityBoost', windll['KERNEL32.dll']), ((1, 'hProcess'),(1, 'bDisablePriorityBoost'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetThreadIOPendingFlag():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.BOOL))(('GetThreadIOPendingFlag', windll['KERNEL32.dll']), ((1, 'hThread'),(1, 'lpIOIsPending'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSystemTimes():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.FILETIME_head),POINTER(win32more.Foundation.FILETIME_head),POINTER(win32more.Foundation.FILETIME_head))(('GetSystemTimes', windll['KERNEL32.dll']), ((1, 'lpIdleTime'),(1, 'lpKernelTime'),(1, 'lpUserTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetThreadInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.System.Threading.THREAD_INFORMATION_CLASS,c_void_p,UInt32)(('GetThreadInformation', windll['KERNEL32.dll']), ((1, 'hThread'),(1, 'ThreadInformationClass'),(1, 'ThreadInformation'),(1, 'ThreadInformationSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetThreadInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.System.Threading.THREAD_INFORMATION_CLASS,c_void_p,UInt32)(('SetThreadInformation', windll['KERNEL32.dll']), ((1, 'hThread'),(1, 'ThreadInformationClass'),(1, 'ThreadInformation'),(1, 'ThreadInformationSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsProcessCritical():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.BOOL))(('IsProcessCritical', windll['KERNEL32.dll']), ((1, 'hProcess'),(1, 'Critical'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetProtectedPolicy():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(Guid),UIntPtr,POINTER(UIntPtr))(('SetProtectedPolicy', windll['KERNEL32.dll']), ((1, 'PolicyGuid'),(1, 'PolicyValue'),(1, 'OldPolicyValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryProtectedPolicy():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(Guid),POINTER(UIntPtr))(('QueryProtectedPolicy', windll['KERNEL32.dll']), ((1, 'PolicyGuid'),(1, 'PolicyValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetThreadIdealProcessor():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt32)(('SetThreadIdealProcessor', windll['KERNEL32.dll']), ((1, 'hThread'),(1, 'dwIdealProcessor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetProcessInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.System.Threading.PROCESS_INFORMATION_CLASS,c_void_p,UInt32)(('SetProcessInformation', windll['KERNEL32.dll']), ((1, 'hProcess'),(1, 'ProcessInformationClass'),(1, 'ProcessInformation'),(1, 'ProcessInformationSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetProcessInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.System.Threading.PROCESS_INFORMATION_CLASS,c_void_p,UInt32)(('GetProcessInformation', windll['KERNEL32.dll']), ((1, 'hProcess'),(1, 'ProcessInformationClass'),(1, 'ProcessInformation'),(1, 'ProcessInformationSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetProcessDefaultCpuSets():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(UInt32),UInt32,POINTER(UInt32))(('GetProcessDefaultCpuSets', windll['KERNEL32.dll']), ((1, 'Process'),(1, 'CpuSetIds'),(1, 'CpuSetIdCount'),(1, 'RequiredIdCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetProcessDefaultCpuSets():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(UInt32),UInt32)(('SetProcessDefaultCpuSets', windll['KERNEL32.dll']), ((1, 'Process'),(1, 'CpuSetIds'),(1, 'CpuSetIdCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetThreadSelectedCpuSets():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(UInt32),UInt32,POINTER(UInt32))(('GetThreadSelectedCpuSets', windll['KERNEL32.dll']), ((1, 'Thread'),(1, 'CpuSetIds'),(1, 'CpuSetIdCount'),(1, 'RequiredIdCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetThreadSelectedCpuSets():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(UInt32),UInt32)(('SetThreadSelectedCpuSets', windll['KERNEL32.dll']), ((1, 'Thread'),(1, 'CpuSetIds'),(1, 'CpuSetIdCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateProcessAsUserA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),win32more.Foundation.BOOL,UInt32,c_void_p,win32more.Foundation.PSTR,POINTER(win32more.System.Threading.STARTUPINFOA_head),POINTER(win32more.System.Threading.PROCESS_INFORMATION_head))(('CreateProcessAsUserA', windll['ADVAPI32.dll']), ((1, 'hToken'),(1, 'lpApplicationName'),(1, 'lpCommandLine'),(1, 'lpProcessAttributes'),(1, 'lpThreadAttributes'),(1, 'bInheritHandles'),(1, 'dwCreationFlags'),(1, 'lpEnvironment'),(1, 'lpCurrentDirectory'),(1, 'lpStartupInfo'),(1, 'lpProcessInformation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetProcessShutdownParameters():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(UInt32),POINTER(UInt32))(('GetProcessShutdownParameters', windll['KERNEL32.dll']), ((1, 'lpdwLevel'),(1, 'lpdwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetProcessDefaultCpuSetMasks():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.SystemInformation.GROUP_AFFINITY_head),UInt16,POINTER(UInt16))(('GetProcessDefaultCpuSetMasks', windll['KERNEL32.dll']), ((1, 'Process'),(1, 'CpuSetMasks'),(1, 'CpuSetMaskCount'),(1, 'RequiredMaskCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetProcessDefaultCpuSetMasks():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.SystemInformation.GROUP_AFFINITY_head),UInt16)(('SetProcessDefaultCpuSetMasks', windll['KERNEL32.dll']), ((1, 'Process'),(1, 'CpuSetMasks'),(1, 'CpuSetMaskCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetThreadSelectedCpuSetMasks():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.SystemInformation.GROUP_AFFINITY_head),UInt16,POINTER(UInt16))(('GetThreadSelectedCpuSetMasks', windll['KERNEL32.dll']), ((1, 'Thread'),(1, 'CpuSetMasks'),(1, 'CpuSetMaskCount'),(1, 'RequiredMaskCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetThreadSelectedCpuSetMasks():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.SystemInformation.GROUP_AFFINITY_head),UInt16)(('SetThreadSelectedCpuSetMasks', windll['KERNEL32.dll']), ((1, 'Thread'),(1, 'CpuSetMasks'),(1, 'CpuSetMaskCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetMachineTypeAttributes():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(win32more.System.Threading.MACHINE_ATTRIBUTES))(('GetMachineTypeAttributes', windll['KERNEL32.dll']), ((1, 'Machine'),(1, 'MachineTypeAttributes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetThreadDescription():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR)(('SetThreadDescription', windll['KERNEL32.dll']), ((1, 'hThread'),(1, 'lpThreadDescription'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetThreadDescription():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.PWSTR))(('GetThreadDescription', windll['KERNEL32.dll']), ((1, 'hThread'),(1, 'ppszThreadDescription'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueueUserWorkItem():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.Threading.LPTHREAD_START_ROUTINE,c_void_p,win32more.System.Threading.WORKER_THREAD_FLAGS)(('QueueUserWorkItem', windll['KERNEL32.dll']), ((1, 'Function'),(1, 'Context'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UnregisterWaitEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE)(('UnregisterWaitEx', windll['KERNEL32.dll']), ((1, 'WaitHandle'),(1, 'CompletionEvent'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateTimerQueue():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,)(('CreateTimerQueue', windll['KERNEL32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateTimerQueueTimer():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.HANDLE),win32more.Foundation.HANDLE,win32more.System.Threading.WAITORTIMERCALLBACK,c_void_p,UInt32,UInt32,win32more.System.Threading.WORKER_THREAD_FLAGS)(('CreateTimerQueueTimer', windll['KERNEL32.dll']), ((1, 'phNewTimer'),(1, 'TimerQueue'),(1, 'Callback'),(1, 'Parameter'),(1, 'DueTime'),(1, 'Period'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ChangeTimerQueueTimer():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,UInt32,UInt32)(('ChangeTimerQueueTimer', windll['KERNEL32.dll']), ((1, 'TimerQueue'),(1, 'Timer'),(1, 'DueTime'),(1, 'Period'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeleteTimerQueueTimer():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE)(('DeleteTimerQueueTimer', windll['KERNEL32.dll']), ((1, 'TimerQueue'),(1, 'Timer'),(1, 'CompletionEvent'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeleteTimerQueue():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE)(('DeleteTimerQueue', windll['KERNEL32.dll']), ((1, 'TimerQueue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeleteTimerQueueEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE)(('DeleteTimerQueueEx', windll['KERNEL32.dll']), ((1, 'TimerQueue'),(1, 'CompletionEvent'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateThreadpool():
    try:
        return WINFUNCTYPE(win32more.System.Threading.PTP_POOL,c_void_p)(('CreateThreadpool', windll['KERNEL32.dll']), ((1, 'reserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetThreadpoolThreadMaximum():
    try:
        return WINFUNCTYPE(Void,win32more.System.Threading.PTP_POOL,UInt32)(('SetThreadpoolThreadMaximum', windll['KERNEL32.dll']), ((1, 'ptpp'),(1, 'cthrdMost'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetThreadpoolThreadMinimum():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.Threading.PTP_POOL,UInt32)(('SetThreadpoolThreadMinimum', windll['KERNEL32.dll']), ((1, 'ptpp'),(1, 'cthrdMic'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetThreadpoolStackInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.Threading.PTP_POOL,POINTER(win32more.System.Threading.TP_POOL_STACK_INFORMATION_head))(('SetThreadpoolStackInformation', windll['KERNEL32.dll']), ((1, 'ptpp'),(1, 'ptpsi'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryThreadpoolStackInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.Threading.PTP_POOL,POINTER(win32more.System.Threading.TP_POOL_STACK_INFORMATION_head))(('QueryThreadpoolStackInformation', windll['KERNEL32.dll']), ((1, 'ptpp'),(1, 'ptpsi'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CloseThreadpool():
    try:
        return WINFUNCTYPE(Void,win32more.System.Threading.PTP_POOL)(('CloseThreadpool', windll['KERNEL32.dll']), ((1, 'ptpp'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateThreadpoolCleanupGroup():
    try:
        return WINFUNCTYPE(IntPtr,)(('CreateThreadpoolCleanupGroup', windll['KERNEL32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_CloseThreadpoolCleanupGroupMembers():
    try:
        return WINFUNCTYPE(Void,IntPtr,win32more.Foundation.BOOL,c_void_p)(('CloseThreadpoolCleanupGroupMembers', windll['KERNEL32.dll']), ((1, 'ptpcg'),(1, 'fCancelPendingCallbacks'),(1, 'pvCleanupContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CloseThreadpoolCleanupGroup():
    try:
        return WINFUNCTYPE(Void,IntPtr)(('CloseThreadpoolCleanupGroup', windll['KERNEL32.dll']), ((1, 'ptpcg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetEventWhenCallbackReturns():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Threading.TP_CALLBACK_INSTANCE_head),win32more.Foundation.HANDLE)(('SetEventWhenCallbackReturns', windll['KERNEL32.dll']), ((1, 'pci'),(1, 'evt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReleaseSemaphoreWhenCallbackReturns():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Threading.TP_CALLBACK_INSTANCE_head),win32more.Foundation.HANDLE,UInt32)(('ReleaseSemaphoreWhenCallbackReturns', windll['KERNEL32.dll']), ((1, 'pci'),(1, 'sem'),(1, 'crel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReleaseMutexWhenCallbackReturns():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Threading.TP_CALLBACK_INSTANCE_head),win32more.Foundation.HANDLE)(('ReleaseMutexWhenCallbackReturns', windll['KERNEL32.dll']), ((1, 'pci'),(1, 'mut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LeaveCriticalSectionWhenCallbackReturns():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Threading.TP_CALLBACK_INSTANCE_head),POINTER(win32more.System.Threading.RTL_CRITICAL_SECTION_head))(('LeaveCriticalSectionWhenCallbackReturns', windll['KERNEL32.dll']), ((1, 'pci'),(1, 'pcs'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FreeLibraryWhenCallbackReturns():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Threading.TP_CALLBACK_INSTANCE_head),win32more.Foundation.HINSTANCE)(('FreeLibraryWhenCallbackReturns', windll['KERNEL32.dll']), ((1, 'pci'),(1, 'mod'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CallbackMayRunLong():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Threading.TP_CALLBACK_INSTANCE_head))(('CallbackMayRunLong', windll['KERNEL32.dll']), ((1, 'pci'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DisassociateCurrentThreadFromCallback():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Threading.TP_CALLBACK_INSTANCE_head))(('DisassociateCurrentThreadFromCallback', windll['KERNEL32.dll']), ((1, 'pci'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TrySubmitThreadpoolCallback():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.Threading.PTP_SIMPLE_CALLBACK,c_void_p,POINTER(win32more.System.Threading.TP_CALLBACK_ENVIRON_V3_head))(('TrySubmitThreadpoolCallback', windll['KERNEL32.dll']), ((1, 'pfns'),(1, 'pv'),(1, 'pcbe'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateThreadpoolWork():
    try:
        return WINFUNCTYPE(POINTER(win32more.System.Threading.TP_WORK_head),win32more.System.Threading.PTP_WORK_CALLBACK,c_void_p,POINTER(win32more.System.Threading.TP_CALLBACK_ENVIRON_V3_head))(('CreateThreadpoolWork', windll['KERNEL32.dll']), ((1, 'pfnwk'),(1, 'pv'),(1, 'pcbe'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SubmitThreadpoolWork():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Threading.TP_WORK_head))(('SubmitThreadpoolWork', windll['KERNEL32.dll']), ((1, 'pwk'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WaitForThreadpoolWorkCallbacks():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Threading.TP_WORK_head),win32more.Foundation.BOOL)(('WaitForThreadpoolWorkCallbacks', windll['KERNEL32.dll']), ((1, 'pwk'),(1, 'fCancelPendingCallbacks'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CloseThreadpoolWork():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Threading.TP_WORK_head))(('CloseThreadpoolWork', windll['KERNEL32.dll']), ((1, 'pwk'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateThreadpoolTimer():
    try:
        return WINFUNCTYPE(POINTER(win32more.System.Threading.TP_TIMER_head),win32more.System.Threading.PTP_TIMER_CALLBACK,c_void_p,POINTER(win32more.System.Threading.TP_CALLBACK_ENVIRON_V3_head))(('CreateThreadpoolTimer', windll['KERNEL32.dll']), ((1, 'pfnti'),(1, 'pv'),(1, 'pcbe'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetThreadpoolTimer():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Threading.TP_TIMER_head),POINTER(win32more.Foundation.FILETIME_head),UInt32,UInt32)(('SetThreadpoolTimer', windll['KERNEL32.dll']), ((1, 'pti'),(1, 'pftDueTime'),(1, 'msPeriod'),(1, 'msWindowLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsThreadpoolTimerSet():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Threading.TP_TIMER_head))(('IsThreadpoolTimerSet', windll['KERNEL32.dll']), ((1, 'pti'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WaitForThreadpoolTimerCallbacks():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Threading.TP_TIMER_head),win32more.Foundation.BOOL)(('WaitForThreadpoolTimerCallbacks', windll['KERNEL32.dll']), ((1, 'pti'),(1, 'fCancelPendingCallbacks'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CloseThreadpoolTimer():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Threading.TP_TIMER_head))(('CloseThreadpoolTimer', windll['KERNEL32.dll']), ((1, 'pti'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateThreadpoolWait():
    try:
        return WINFUNCTYPE(POINTER(win32more.System.Threading.TP_WAIT_head),win32more.System.Threading.PTP_WAIT_CALLBACK,c_void_p,POINTER(win32more.System.Threading.TP_CALLBACK_ENVIRON_V3_head))(('CreateThreadpoolWait', windll['KERNEL32.dll']), ((1, 'pfnwa'),(1, 'pv'),(1, 'pcbe'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetThreadpoolWait():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Threading.TP_WAIT_head),win32more.Foundation.HANDLE,POINTER(win32more.Foundation.FILETIME_head))(('SetThreadpoolWait', windll['KERNEL32.dll']), ((1, 'pwa'),(1, 'h'),(1, 'pftTimeout'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WaitForThreadpoolWaitCallbacks():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Threading.TP_WAIT_head),win32more.Foundation.BOOL)(('WaitForThreadpoolWaitCallbacks', windll['KERNEL32.dll']), ((1, 'pwa'),(1, 'fCancelPendingCallbacks'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CloseThreadpoolWait():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Threading.TP_WAIT_head))(('CloseThreadpoolWait', windll['KERNEL32.dll']), ((1, 'pwa'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateThreadpoolIo():
    try:
        return WINFUNCTYPE(POINTER(win32more.System.Threading.TP_IO_head),win32more.Foundation.HANDLE,win32more.System.Threading.PTP_WIN32_IO_CALLBACK,c_void_p,POINTER(win32more.System.Threading.TP_CALLBACK_ENVIRON_V3_head))(('CreateThreadpoolIo', windll['KERNEL32.dll']), ((1, 'fl'),(1, 'pfnio'),(1, 'pv'),(1, 'pcbe'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_StartThreadpoolIo():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Threading.TP_IO_head))(('StartThreadpoolIo', windll['KERNEL32.dll']), ((1, 'pio'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CancelThreadpoolIo():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Threading.TP_IO_head))(('CancelThreadpoolIo', windll['KERNEL32.dll']), ((1, 'pio'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WaitForThreadpoolIoCallbacks():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Threading.TP_IO_head),win32more.Foundation.BOOL)(('WaitForThreadpoolIoCallbacks', windll['KERNEL32.dll']), ((1, 'pio'),(1, 'fCancelPendingCallbacks'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CloseThreadpoolIo():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Threading.TP_IO_head))(('CloseThreadpoolIo', windll['KERNEL32.dll']), ((1, 'pio'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetThreadpoolTimerEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Threading.TP_TIMER_head),POINTER(win32more.Foundation.FILETIME_head),UInt32,UInt32)(('SetThreadpoolTimerEx', windll['KERNEL32.dll']), ((1, 'pti'),(1, 'pftDueTime'),(1, 'msPeriod'),(1, 'msWindowLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetThreadpoolWaitEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Threading.TP_WAIT_head),win32more.Foundation.HANDLE,POINTER(win32more.Foundation.FILETIME_head),c_void_p)(('SetThreadpoolWaitEx', windll['KERNEL32.dll']), ((1, 'pwa'),(1, 'h'),(1, 'pftTimeout'),(1, 'Reserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsWow64Process():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.BOOL))(('IsWow64Process', windll['KERNEL32.dll']), ((1, 'hProcess'),(1, 'Wow64Process'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Wow64SetThreadDefaultGuestMachine():
    try:
        return WINFUNCTYPE(UInt16,UInt16)(('Wow64SetThreadDefaultGuestMachine', windll['api-ms-win-core-wow64-l1-1-1.dll']), ((1, 'Machine'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsWow64Process2():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.SystemInformation.IMAGE_FILE_MACHINE),POINTER(win32more.System.SystemInformation.IMAGE_FILE_MACHINE))(('IsWow64Process2', windll['KERNEL32.dll']), ((1, 'hProcess'),(1, 'pProcessMachine'),(1, 'pNativeMachine'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Wow64SuspendThread():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE)(('Wow64SuspendThread', windll['KERNEL32.dll']), ((1, 'hThread'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreatePrivateNamespaceW():
    try:
        return WINFUNCTYPE(win32more.System.Threading.NamespaceHandle,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),c_void_p,win32more.Foundation.PWSTR)(('CreatePrivateNamespaceW', windll['KERNEL32.dll']), ((1, 'lpPrivateNamespaceAttributes'),(1, 'lpBoundaryDescriptor'),(1, 'lpAliasPrefix'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenPrivateNamespaceW():
    try:
        return WINFUNCTYPE(win32more.System.Threading.NamespaceHandle,c_void_p,win32more.Foundation.PWSTR)(('OpenPrivateNamespaceW', windll['KERNEL32.dll']), ((1, 'lpBoundaryDescriptor'),(1, 'lpAliasPrefix'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ClosePrivateNamespace():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,win32more.System.Threading.NamespaceHandle,UInt32)(('ClosePrivateNamespace', windll['KERNEL32.dll']), ((1, 'Handle'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateBoundaryDescriptorW():
    try:
        return WINFUNCTYPE(win32more.System.Threading.BoundaryDescriptorHandle,win32more.Foundation.PWSTR,UInt32)(('CreateBoundaryDescriptorW', windll['KERNEL32.dll']), ((1, 'Name'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddSIDToBoundaryDescriptor():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.HANDLE),win32more.Foundation.PSID)(('AddSIDToBoundaryDescriptor', windll['KERNEL32.dll']), ((1, 'BoundaryDescriptor'),(1, 'RequiredSid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeleteBoundaryDescriptor():
    try:
        return WINFUNCTYPE(Void,win32more.System.Threading.BoundaryDescriptorHandle)(('DeleteBoundaryDescriptor', windll['KERNEL32.dll']), ((1, 'BoundaryDescriptor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetNumaHighestNodeNumber():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(UInt32))(('GetNumaHighestNodeNumber', windll['KERNEL32.dll']), ((1, 'HighestNodeNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetNumaNodeProcessorMaskEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt16,POINTER(win32more.System.SystemInformation.GROUP_AFFINITY_head))(('GetNumaNodeProcessorMaskEx', windll['KERNEL32.dll']), ((1, 'Node'),(1, 'ProcessorMask'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetNumaNodeProcessorMask2():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt16,POINTER(win32more.System.SystemInformation.GROUP_AFFINITY_head),UInt16,POINTER(UInt16))(('GetNumaNodeProcessorMask2', windll['KERNEL32.dll']), ((1, 'NodeNumber'),(1, 'ProcessorMasks'),(1, 'ProcessorMaskCount'),(1, 'RequiredMaskCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetNumaProximityNodeEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,POINTER(UInt16))(('GetNumaProximityNodeEx', windll['KERNEL32.dll']), ((1, 'ProximityId'),(1, 'NodeNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetProcessGroupAffinity():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(UInt16),POINTER(UInt16))(('GetProcessGroupAffinity', windll['KERNEL32.dll']), ((1, 'hProcess'),(1, 'GroupCount'),(1, 'GroupArray'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetThreadGroupAffinity():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.SystemInformation.GROUP_AFFINITY_head))(('GetThreadGroupAffinity', windll['KERNEL32.dll']), ((1, 'hThread'),(1, 'GroupAffinity'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetThreadGroupAffinity():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.SystemInformation.GROUP_AFFINITY_head),POINTER(win32more.System.SystemInformation.GROUP_AFFINITY_head))(('SetThreadGroupAffinity', windll['KERNEL32.dll']), ((1, 'hThread'),(1, 'GroupAffinity'),(1, 'PreviousGroupAffinity'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AvSetMmThreadCharacteristicsA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.PSTR,POINTER(UInt32))(('AvSetMmThreadCharacteristicsA', windll['AVRT.dll']), ((1, 'TaskName'),(1, 'TaskIndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AvSetMmThreadCharacteristicsW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,POINTER(UInt32))(('AvSetMmThreadCharacteristicsW', windll['AVRT.dll']), ((1, 'TaskName'),(1, 'TaskIndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AvSetMmMaxThreadCharacteristicsA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(UInt32))(('AvSetMmMaxThreadCharacteristicsA', windll['AVRT.dll']), ((1, 'FirstTask'),(1, 'SecondTask'),(1, 'TaskIndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AvSetMmMaxThreadCharacteristicsW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32))(('AvSetMmMaxThreadCharacteristicsW', windll['AVRT.dll']), ((1, 'FirstTask'),(1, 'SecondTask'),(1, 'TaskIndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AvRevertMmThreadCharacteristics():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE)(('AvRevertMmThreadCharacteristics', windll['AVRT.dll']), ((1, 'AvrtHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AvSetMmThreadPriority():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.System.Threading.AVRT_PRIORITY)(('AvSetMmThreadPriority', windll['AVRT.dll']), ((1, 'AvrtHandle'),(1, 'Priority'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AvRtCreateThreadOrderingGroup():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.HANDLE),POINTER(win32more.Foundation.LARGE_INTEGER_head),POINTER(Guid),POINTER(win32more.Foundation.LARGE_INTEGER_head))(('AvRtCreateThreadOrderingGroup', windll['AVRT.dll']), ((1, 'Context'),(1, 'Period'),(1, 'ThreadOrderingGuid'),(1, 'Timeout'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AvRtCreateThreadOrderingGroupExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.HANDLE),POINTER(win32more.Foundation.LARGE_INTEGER_head),POINTER(Guid),POINTER(win32more.Foundation.LARGE_INTEGER_head),win32more.Foundation.PSTR)(('AvRtCreateThreadOrderingGroupExA', windll['AVRT.dll']), ((1, 'Context'),(1, 'Period'),(1, 'ThreadOrderingGuid'),(1, 'Timeout'),(1, 'TaskName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AvRtCreateThreadOrderingGroupExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.HANDLE),POINTER(win32more.Foundation.LARGE_INTEGER_head),POINTER(Guid),POINTER(win32more.Foundation.LARGE_INTEGER_head),win32more.Foundation.PWSTR)(('AvRtCreateThreadOrderingGroupExW', windll['AVRT.dll']), ((1, 'Context'),(1, 'Period'),(1, 'ThreadOrderingGuid'),(1, 'Timeout'),(1, 'TaskName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AvRtJoinThreadOrderingGroup():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.HANDLE),POINTER(Guid),win32more.Foundation.BOOL)(('AvRtJoinThreadOrderingGroup', windll['AVRT.dll']), ((1, 'Context'),(1, 'ThreadOrderingGuid'),(1, 'Before'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AvRtWaitOnThreadOrderingGroup():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE)(('AvRtWaitOnThreadOrderingGroup', windll['AVRT.dll']), ((1, 'Context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AvRtLeaveThreadOrderingGroup():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE)(('AvRtLeaveThreadOrderingGroup', windll['AVRT.dll']), ((1, 'Context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AvRtDeleteThreadOrderingGroup():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE)(('AvRtDeleteThreadOrderingGroup', windll['AVRT.dll']), ((1, 'Context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AvQuerySystemResponsiveness():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(UInt32))(('AvQuerySystemResponsiveness', windll['AVRT.dll']), ((1, 'AvrtHandle'),(1, 'SystemResponsivenessValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AttachThreadInput():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,UInt32,win32more.Foundation.BOOL)(('AttachThreadInput', windll['USER32.dll']), ((1, 'idAttach'),(1, 'idAttachTo'),(1, 'fAttach'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WaitForInputIdle():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt32)(('WaitForInputIdle', windll['USER32.dll']), ((1, 'hProcess'),(1, 'dwMilliseconds'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetGuiResources():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.System.Threading.GET_GUI_RESOURCES_FLAGS)(('GetGuiResources', windll['USER32.dll']), ((1, 'hProcess'),(1, 'uiFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsImmersiveProcess():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE)(('IsImmersiveProcess', windll['USER32.dll']), ((1, 'hProcess'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetProcessRestrictionExemption():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.BOOL)(('SetProcessRestrictionExemption', windll['USER32.dll']), ((1, 'fEnableExemption'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetProcessAffinityMask():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(UIntPtr),POINTER(UIntPtr))(('GetProcessAffinityMask', windll['KERNEL32.dll']), ((1, 'hProcess'),(1, 'lpProcessAffinityMask'),(1, 'lpSystemAffinityMask'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetProcessAffinityMask():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UIntPtr)(('SetProcessAffinityMask', windll['KERNEL32.dll']), ((1, 'hProcess'),(1, 'dwProcessAffinityMask'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetProcessIoCounters():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.Threading.IO_COUNTERS_head))(('GetProcessIoCounters', windll['KERNEL32.dll']), ((1, 'hProcess'),(1, 'lpIoCounters'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SwitchToFiber():
    try:
        return WINFUNCTYPE(Void,c_void_p)(('SwitchToFiber', windll['KERNEL32.dll']), ((1, 'lpFiber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeleteFiber():
    try:
        return WINFUNCTYPE(Void,c_void_p)(('DeleteFiber', windll['KERNEL32.dll']), ((1, 'lpFiber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ConvertFiberToThread():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,)(('ConvertFiberToThread', windll['KERNEL32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateFiberEx():
    try:
        return WINFUNCTYPE(c_void_p,UIntPtr,UIntPtr,UInt32,win32more.System.Threading.LPFIBER_START_ROUTINE,c_void_p)(('CreateFiberEx', windll['KERNEL32.dll']), ((1, 'dwStackCommitSize'),(1, 'dwStackReserveSize'),(1, 'dwFlags'),(1, 'lpStartAddress'),(1, 'lpParameter'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ConvertThreadToFiberEx():
    try:
        return WINFUNCTYPE(c_void_p,c_void_p,UInt32)(('ConvertThreadToFiberEx', windll['KERNEL32.dll']), ((1, 'lpParameter'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateFiber():
    try:
        return WINFUNCTYPE(c_void_p,UIntPtr,win32more.System.Threading.LPFIBER_START_ROUTINE,c_void_p)(('CreateFiber', windll['KERNEL32.dll']), ((1, 'dwStackSize'),(1, 'lpStartAddress'),(1, 'lpParameter'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ConvertThreadToFiber():
    try:
        return WINFUNCTYPE(c_void_p,c_void_p)(('ConvertThreadToFiber', windll['KERNEL32.dll']), ((1, 'lpParameter'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateUmsCompletionList():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(c_void_p))(('CreateUmsCompletionList', windll['KERNEL32.dll']), ((1, 'UmsCompletionList'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DequeueUmsCompletionListItems():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,UInt32,POINTER(c_void_p))(('DequeueUmsCompletionListItems', windll['KERNEL32.dll']), ((1, 'UmsCompletionList'),(1, 'WaitTimeOut'),(1, 'UmsThreadList'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetUmsCompletionListEvent():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,POINTER(win32more.Foundation.HANDLE))(('GetUmsCompletionListEvent', windll['KERNEL32.dll']), ((1, 'UmsCompletionList'),(1, 'UmsCompletionEvent'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ExecuteUmsThread():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p)(('ExecuteUmsThread', windll['KERNEL32.dll']), ((1, 'UmsThread'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UmsThreadYield():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p)(('UmsThreadYield', windll['KERNEL32.dll']), ((1, 'SchedulerParam'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeleteUmsCompletionList():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p)(('DeleteUmsCompletionList', windll['KERNEL32.dll']), ((1, 'UmsCompletionList'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCurrentUmsThread():
    try:
        return WINFUNCTYPE(c_void_p,)(('GetCurrentUmsThread', windll['KERNEL32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetNextUmsListItem():
    try:
        return WINFUNCTYPE(c_void_p,c_void_p)(('GetNextUmsListItem', windll['KERNEL32.dll']), ((1, 'UmsContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryUmsThreadInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,win32more.System.Threading.RTL_UMS_THREAD_INFO_CLASS,c_void_p,UInt32,POINTER(UInt32))(('QueryUmsThreadInformation', windll['KERNEL32.dll']), ((1, 'UmsThread'),(1, 'UmsThreadInfoClass'),(1, 'UmsThreadInformation'),(1, 'UmsThreadInformationLength'),(1, 'ReturnLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetUmsThreadInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,win32more.System.Threading.RTL_UMS_THREAD_INFO_CLASS,c_void_p,UInt32)(('SetUmsThreadInformation', windll['KERNEL32.dll']), ((1, 'UmsThread'),(1, 'UmsThreadInfoClass'),(1, 'UmsThreadInformation'),(1, 'UmsThreadInformationLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeleteUmsThreadContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p)(('DeleteUmsThreadContext', windll['KERNEL32.dll']), ((1, 'UmsThread'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateUmsThreadContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(c_void_p))(('CreateUmsThreadContext', windll['KERNEL32.dll']), ((1, 'lpUmsThread'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnterUmsSchedulingMode():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Threading.UMS_SCHEDULER_STARTUP_INFO_head))(('EnterUmsSchedulingMode', windll['KERNEL32.dll']), ((1, 'SchedulerStartupInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetUmsSystemThreadInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.Threading.UMS_SYSTEM_THREAD_INFORMATION_head))(('GetUmsSystemThreadInformation', windll['KERNEL32.dll']), ((1, 'ThreadHandle'),(1, 'SystemThreadInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetThreadAffinityMask():
    try:
        return WINFUNCTYPE(UIntPtr,win32more.Foundation.HANDLE,UIntPtr)(('SetThreadAffinityMask', windll['KERNEL32.dll']), ((1, 'hThread'),(1, 'dwThreadAffinityMask'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetProcessDEPPolicy():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.Threading.PROCESS_DEP_FLAGS)(('SetProcessDEPPolicy', windll['KERNEL32.dll']), ((1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetProcessDEPPolicy():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(UInt32),POINTER(win32more.Foundation.BOOL))(('GetProcessDEPPolicy', windll['KERNEL32.dll']), ((1, 'hProcess'),(1, 'lpFlags'),(1, 'lpPermanent'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PulseEvent():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE)(('PulseEvent', windll['KERNEL32.dll']), ((1, 'hEvent'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinExec():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,UInt32)(('WinExec', windll['KERNEL32.dll']), ((1, 'lpCmdLine'),(1, 'uCmdShow'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateSemaphoreA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),Int32,Int32,win32more.Foundation.PSTR)(('CreateSemaphoreA', windll['KERNEL32.dll']), ((1, 'lpSemaphoreAttributes'),(1, 'lInitialCount'),(1, 'lMaximumCount'),(1, 'lpName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateSemaphoreExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),Int32,Int32,win32more.Foundation.PSTR,UInt32,UInt32)(('CreateSemaphoreExA', windll['KERNEL32.dll']), ((1, 'lpSemaphoreAttributes'),(1, 'lInitialCount'),(1, 'lMaximumCount'),(1, 'lpName'),(1, 'dwFlags'),(1, 'dwDesiredAccess'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryFullProcessImageNameA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.System.Threading.PROCESS_NAME_FORMAT,win32more.Foundation.PSTR,POINTER(UInt32))(('QueryFullProcessImageNameA', windll['KERNEL32.dll']), ((1, 'hProcess'),(1, 'dwFlags'),(1, 'lpExeName'),(1, 'lpdwSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryFullProcessImageNameW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.System.Threading.PROCESS_NAME_FORMAT,win32more.Foundation.PWSTR,POINTER(UInt32))(('QueryFullProcessImageNameW', windll['KERNEL32.dll']), ((1, 'hProcess'),(1, 'dwFlags'),(1, 'lpExeName'),(1, 'lpdwSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetStartupInfoA():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Threading.STARTUPINFOA_head))(('GetStartupInfoA', windll['KERNEL32.dll']), ((1, 'lpStartupInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateProcessWithLogonW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.System.Threading.CREATE_PROCESS_LOGON_FLAGS,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,c_void_p,win32more.Foundation.PWSTR,POINTER(win32more.System.Threading.STARTUPINFOW_head),POINTER(win32more.System.Threading.PROCESS_INFORMATION_head))(('CreateProcessWithLogonW', windll['ADVAPI32.dll']), ((1, 'lpUsername'),(1, 'lpDomain'),(1, 'lpPassword'),(1, 'dwLogonFlags'),(1, 'lpApplicationName'),(1, 'lpCommandLine'),(1, 'dwCreationFlags'),(1, 'lpEnvironment'),(1, 'lpCurrentDirectory'),(1, 'lpStartupInfo'),(1, 'lpProcessInformation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateProcessWithTokenW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.System.Threading.CREATE_PROCESS_LOGON_FLAGS,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,c_void_p,win32more.Foundation.PWSTR,POINTER(win32more.System.Threading.STARTUPINFOW_head),POINTER(win32more.System.Threading.PROCESS_INFORMATION_head))(('CreateProcessWithTokenW', windll['ADVAPI32.dll']), ((1, 'hToken'),(1, 'dwLogonFlags'),(1, 'lpApplicationName'),(1, 'lpCommandLine'),(1, 'dwCreationFlags'),(1, 'lpEnvironment'),(1, 'lpCurrentDirectory'),(1, 'lpStartupInfo'),(1, 'lpProcessInformation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterWaitForSingleObject():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.HANDLE),win32more.Foundation.HANDLE,win32more.System.Threading.WAITORTIMERCALLBACK,c_void_p,UInt32,win32more.System.Threading.WORKER_THREAD_FLAGS)(('RegisterWaitForSingleObject', windll['KERNEL32.dll']), ((1, 'phNewWaitObject'),(1, 'hObject'),(1, 'Callback'),(1, 'Context'),(1, 'dwMilliseconds'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UnregisterWait():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE)(('UnregisterWait', windll['KERNEL32.dll']), ((1, 'WaitHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetTimerQueueTimer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,win32more.System.Threading.WAITORTIMERCALLBACK,c_void_p,UInt32,UInt32,win32more.Foundation.BOOL)(('SetTimerQueueTimer', windll['KERNEL32.dll']), ((1, 'TimerQueue'),(1, 'Callback'),(1, 'Parameter'),(1, 'DueTime'),(1, 'Period'),(1, 'PreferIo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreatePrivateNamespaceA():
    try:
        return WINFUNCTYPE(win32more.System.Threading.NamespaceHandle,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),c_void_p,win32more.Foundation.PSTR)(('CreatePrivateNamespaceA', windll['KERNEL32.dll']), ((1, 'lpPrivateNamespaceAttributes'),(1, 'lpBoundaryDescriptor'),(1, 'lpAliasPrefix'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenPrivateNamespaceA():
    try:
        return WINFUNCTYPE(win32more.System.Threading.NamespaceHandle,c_void_p,win32more.Foundation.PSTR)(('OpenPrivateNamespaceA', windll['KERNEL32.dll']), ((1, 'lpBoundaryDescriptor'),(1, 'lpAliasPrefix'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateBoundaryDescriptorA():
    try:
        return WINFUNCTYPE(win32more.System.Threading.BoundaryDescriptorHandle,win32more.Foundation.PSTR,UInt32)(('CreateBoundaryDescriptorA', windll['KERNEL32.dll']), ((1, 'Name'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddIntegrityLabelToBoundaryDescriptor():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.HANDLE),win32more.Foundation.PSID)(('AddIntegrityLabelToBoundaryDescriptor', windll['KERNEL32.dll']), ((1, 'BoundaryDescriptor'),(1, 'IntegrityLabel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetActiveProcessorGroupCount():
    try:
        return WINFUNCTYPE(UInt16,)(('GetActiveProcessorGroupCount', windll['KERNEL32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetMaximumProcessorGroupCount():
    try:
        return WINFUNCTYPE(UInt16,)(('GetMaximumProcessorGroupCount', windll['KERNEL32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetActiveProcessorCount():
    try:
        return WINFUNCTYPE(UInt32,UInt16)(('GetActiveProcessorCount', windll['KERNEL32.dll']), ((1, 'GroupNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetMaximumProcessorCount():
    try:
        return WINFUNCTYPE(UInt32,UInt16)(('GetMaximumProcessorCount', windll['KERNEL32.dll']), ((1, 'GroupNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetNumaProcessorNode():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,Byte,c_char_p_no)(('GetNumaProcessorNode', windll['KERNEL32.dll']), ((1, 'Processor'),(1, 'NodeNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetNumaNodeNumberFromHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(UInt16))(('GetNumaNodeNumberFromHandle', windll['KERNEL32.dll']), ((1, 'hFile'),(1, 'NodeNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetNumaProcessorNodeEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Kernel.PROCESSOR_NUMBER_head),POINTER(UInt16))(('GetNumaProcessorNodeEx', windll['KERNEL32.dll']), ((1, 'Processor'),(1, 'NodeNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetNumaNodeProcessorMask():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,Byte,POINTER(UInt64))(('GetNumaNodeProcessorMask', windll['KERNEL32.dll']), ((1, 'Node'),(1, 'ProcessorMask'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetNumaAvailableMemoryNode():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,Byte,POINTER(UInt64))(('GetNumaAvailableMemoryNode', windll['KERNEL32.dll']), ((1, 'Node'),(1, 'AvailableBytes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetNumaAvailableMemoryNodeEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt16,POINTER(UInt64))(('GetNumaAvailableMemoryNodeEx', windll['KERNEL32.dll']), ((1, 'Node'),(1, 'AvailableBytes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetNumaProximityNode():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,c_char_p_no)(('GetNumaProximityNode', windll['KERNEL32.dll']), ((1, 'ProximityId'),(1, 'NodeNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NtQueryInformationProcess():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,win32more.Foundation.HANDLE,win32more.System.Threading.PROCESSINFOCLASS,c_void_p,UInt32,POINTER(UInt32))(('NtQueryInformationProcess', windll['ntdll.dll']), ((1, 'ProcessHandle'),(1, 'ProcessInformationClass'),(1, 'ProcessInformation'),(1, 'ProcessInformationLength'),(1, 'ReturnLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NtQueryInformationThread():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,win32more.Foundation.HANDLE,win32more.System.Threading.THREADINFOCLASS,c_void_p,UInt32,POINTER(UInt32))(('NtQueryInformationThread', windll['ntdll.dll']), ((1, 'ThreadHandle'),(1, 'ThreadInformationClass'),(1, 'ThreadInformation'),(1, 'ThreadInformationLength'),(1, 'ReturnLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NtSetInformationThread():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,win32more.Foundation.HANDLE,win32more.System.Threading.THREADINFOCLASS,c_void_p,UInt32)(('NtSetInformationThread', windll['ntdll.dll']), ((1, 'ThreadHandle'),(1, 'ThreadInformationClass'),(1, 'ThreadInformation'),(1, 'ThreadInformationLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_APP_MEMORY_INFORMATION_head():
    class APP_MEMORY_INFORMATION(Structure):
        pass
    return APP_MEMORY_INFORMATION
def _define_APP_MEMORY_INFORMATION():
    APP_MEMORY_INFORMATION = win32more.System.Threading.APP_MEMORY_INFORMATION_head
    APP_MEMORY_INFORMATION._fields_ = [
        ('AvailableCommit', UInt64),
        ('PrivateCommitUsage', UInt64),
        ('PeakPrivateCommitUsage', UInt64),
        ('TotalCommitUsage', UInt64),
    ]
    return APP_MEMORY_INFORMATION
AVRT_PRIORITY = Int32
AVRT_PRIORITY_VERYLOW = -2
AVRT_PRIORITY_LOW = -1
AVRT_PRIORITY_NORMAL = 0
AVRT_PRIORITY_HIGH = 1
AVRT_PRIORITY_CRITICAL = 2
BoundaryDescriptorHandle = IntPtr
CREATE_EVENT = UInt32
CREATE_EVENT_INITIAL_SET = 2
CREATE_EVENT_MANUAL_RESET = 1
CREATE_PROCESS_LOGON_FLAGS = UInt32
LOGON_WITH_PROFILE = 1
LOGON_NETCREDENTIALS_ONLY = 2
GET_GUI_RESOURCES_FLAGS = UInt32
GR_GDIOBJECTS = 0
GR_GDIOBJECTS_PEAK = 2
GR_USEROBJECTS = 1
GR_USEROBJECTS_PEAK = 4
def _define_IO_COUNTERS_head():
    class IO_COUNTERS(Structure):
        pass
    return IO_COUNTERS
def _define_IO_COUNTERS():
    IO_COUNTERS = win32more.System.Threading.IO_COUNTERS_head
    IO_COUNTERS._fields_ = [
        ('ReadOperationCount', UInt64),
        ('WriteOperationCount', UInt64),
        ('OtherOperationCount', UInt64),
        ('ReadTransferCount', UInt64),
        ('WriteTransferCount', UInt64),
        ('OtherTransferCount', UInt64),
    ]
    return IO_COUNTERS
def _define_LPFIBER_START_ROUTINE():
    return WINFUNCTYPE(Void,c_void_p)
LPPROC_THREAD_ATTRIBUTE_LIST = c_void_p
def _define_LPTHREAD_START_ROUTINE():
    return WINFUNCTYPE(UInt32,c_void_p)
MACHINE_ATTRIBUTES = UInt32
MACHINE_ATTRIBUTES_UserEnabled = 1
MACHINE_ATTRIBUTES_KernelEnabled = 2
MACHINE_ATTRIBUTES_Wow64Container = 4
MEMORY_PRIORITY = UInt32
MEMORY_PRIORITY_VERY_LOW = 1
MEMORY_PRIORITY_LOW = 2
MEMORY_PRIORITY_MEDIUM = 3
MEMORY_PRIORITY_BELOW_NORMAL = 4
MEMORY_PRIORITY_NORMAL = 5
def _define_MEMORY_PRIORITY_INFORMATION_head():
    class MEMORY_PRIORITY_INFORMATION(Structure):
        pass
    return MEMORY_PRIORITY_INFORMATION
def _define_MEMORY_PRIORITY_INFORMATION():
    MEMORY_PRIORITY_INFORMATION = win32more.System.Threading.MEMORY_PRIORITY_INFORMATION_head
    MEMORY_PRIORITY_INFORMATION._fields_ = [
        ('MemoryPriority', win32more.System.Threading.MEMORY_PRIORITY),
    ]
    return MEMORY_PRIORITY_INFORMATION
NamespaceHandle = IntPtr
def _define_PEB_head():
    class PEB(Structure):
        pass
    return PEB
def _define_PEB():
    PEB = win32more.System.Threading.PEB_head
    PEB._fields_ = [
        ('Reserved1', Byte * 2),
        ('BeingDebugged', Byte),
        ('Reserved2', Byte * 1),
        ('Reserved3', c_void_p * 2),
        ('Ldr', POINTER(win32more.System.Threading.PEB_LDR_DATA_head)),
        ('ProcessParameters', POINTER(win32more.System.Threading.RTL_USER_PROCESS_PARAMETERS_head)),
        ('Reserved4', c_void_p * 3),
        ('AtlThunkSListPtr', c_void_p),
        ('Reserved5', c_void_p),
        ('Reserved6', UInt32),
        ('Reserved7', c_void_p),
        ('Reserved8', UInt32),
        ('AtlThunkSListPtr32', UInt32),
        ('Reserved9', c_void_p * 45),
        ('Reserved10', Byte * 96),
        ('PostProcessInitRoutine', win32more.System.Threading.PPS_POST_PROCESS_INIT_ROUTINE),
        ('Reserved11', Byte * 128),
        ('Reserved12', c_void_p * 1),
        ('SessionId', UInt32),
    ]
    return PEB
def _define_PEB_LDR_DATA_head():
    class PEB_LDR_DATA(Structure):
        pass
    return PEB_LDR_DATA
def _define_PEB_LDR_DATA():
    PEB_LDR_DATA = win32more.System.Threading.PEB_LDR_DATA_head
    PEB_LDR_DATA._fields_ = [
        ('Reserved1', Byte * 8),
        ('Reserved2', c_void_p * 3),
        ('InMemoryOrderModuleList', win32more.System.Kernel.LIST_ENTRY),
    ]
    return PEB_LDR_DATA
def _define_PFLS_CALLBACK_FUNCTION():
    return WINFUNCTYPE(Void,c_void_p)
def _define_PINIT_ONCE_FN():
    return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Threading.RTL_RUN_ONCE_head),c_void_p,POINTER(c_void_p))
POWER_REQUEST_CONTEXT_FLAGS = UInt32
POWER_REQUEST_CONTEXT_DETAILED_STRING = 2
POWER_REQUEST_CONTEXT_SIMPLE_STRING = 1
def _define_PPS_POST_PROCESS_INIT_ROUTINE():
    return WINFUNCTYPE(Void,)
PROC_THREAD_ATTRIBUTE_NUM = UInt32
PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeParentProcess = 0
PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeHandleList = 2
PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeGroupAffinity = 3
PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributePreferredNode = 4
PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeIdealProcessor = 5
PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeUmsThread = 6
PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeMitigationPolicy = 7
PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeSecurityCapabilities = 9
PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeProtectionLevel = 11
PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeJobList = 13
PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeChildProcessPolicy = 14
PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeAllApplicationPackagesPolicy = 15
PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeWin32kFilter = 16
PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeSafeOpenPromptOriginClaim = 17
PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeDesktopAppPolicy = 18
PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributePseudoConsole = 22
PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeMitigationAuditPolicy = 24
PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeMachineType = 25
PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeComponentFilter = 26
PROC_THREAD_ATTRIBUTE_NUM_ProcThreadAttributeEnableOptionalXStateFeatures = 27
PROCESS_ACCESS_RIGHTS = UInt32
PROCESS_TERMINATE = 1
PROCESS_CREATE_THREAD = 2
PROCESS_SET_SESSIONID = 4
PROCESS_VM_OPERATION = 8
PROCESS_VM_READ = 16
PROCESS_VM_WRITE = 32
PROCESS_DUP_HANDLE = 64
PROCESS_CREATE_PROCESS = 128
PROCESS_SET_QUOTA = 256
PROCESS_SET_INFORMATION = 512
PROCESS_QUERY_INFORMATION = 1024
PROCESS_SUSPEND_RESUME = 2048
PROCESS_QUERY_LIMITED_INFORMATION = 4096
PROCESS_SET_LIMITED_INFORMATION = 8192
PROCESS_ALL_ACCESS = 2097151
PROCESS_DELETE = 65536
PROCESS_READ_CONTROL = 131072
PROCESS_WRITE_DAC = 262144
PROCESS_WRITE_OWNER = 524288
PROCESS_SYNCHRONIZE = 1048576
PROCESS_STANDARD_RIGHTS_REQUIRED = 983040
PROCESS_AFFINITY_AUTO_UPDATE_FLAGS = UInt32
PROCESS_AFFINITY_DISABLE_AUTO_UPDATE = 0
PROCESS_AFFINITY_ENABLE_AUTO_UPDATE = 1
def _define_PROCESS_BASIC_INFORMATION_head():
    class PROCESS_BASIC_INFORMATION(Structure):
        pass
    return PROCESS_BASIC_INFORMATION
def _define_PROCESS_BASIC_INFORMATION():
    PROCESS_BASIC_INFORMATION = win32more.System.Threading.PROCESS_BASIC_INFORMATION_head
    PROCESS_BASIC_INFORMATION._fields_ = [
        ('Reserved1', c_void_p),
        ('PebBaseAddress', POINTER(win32more.System.Threading.PEB_head)),
        ('Reserved2', c_void_p * 2),
        ('UniqueProcessId', UIntPtr),
        ('Reserved3', c_void_p),
    ]
    return PROCESS_BASIC_INFORMATION
PROCESS_CREATION_FLAGS = UInt32
DEBUG_PROCESS = 1
DEBUG_ONLY_THIS_PROCESS = 2
CREATE_SUSPENDED = 4
DETACHED_PROCESS = 8
CREATE_NEW_CONSOLE = 16
NORMAL_PRIORITY_CLASS = 32
IDLE_PRIORITY_CLASS = 64
HIGH_PRIORITY_CLASS = 128
REALTIME_PRIORITY_CLASS = 256
CREATE_NEW_PROCESS_GROUP = 512
CREATE_UNICODE_ENVIRONMENT = 1024
CREATE_SEPARATE_WOW_VDM = 2048
CREATE_SHARED_WOW_VDM = 4096
CREATE_FORCEDOS = 8192
BELOW_NORMAL_PRIORITY_CLASS = 16384
ABOVE_NORMAL_PRIORITY_CLASS = 32768
INHERIT_PARENT_AFFINITY = 65536
INHERIT_CALLER_PRIORITY = 131072
CREATE_PROTECTED_PROCESS = 262144
EXTENDED_STARTUPINFO_PRESENT = 524288
PROCESS_MODE_BACKGROUND_BEGIN = 1048576
PROCESS_MODE_BACKGROUND_END = 2097152
CREATE_SECURE_PROCESS = 4194304
CREATE_BREAKAWAY_FROM_JOB = 16777216
CREATE_PRESERVE_CODE_AUTHZ_LEVEL = 33554432
CREATE_DEFAULT_ERROR_MODE = 67108864
CREATE_NO_WINDOW = 134217728
PROFILE_USER = 268435456
PROFILE_KERNEL = 536870912
PROFILE_SERVER = 1073741824
CREATE_IGNORE_SYSTEM_DEFAULT = 2147483648
PROCESS_DEP_FLAGS = UInt32
PROCESS_DEP_ENABLE = 1
PROCESS_DEP_DISABLE_ATL_THUNK_EMULATION = 2
PROCESS_DEP_NONE = 0
def _define_PROCESS_DYNAMIC_EH_CONTINUATION_TARGET_head():
    class PROCESS_DYNAMIC_EH_CONTINUATION_TARGET(Structure):
        pass
    return PROCESS_DYNAMIC_EH_CONTINUATION_TARGET
def _define_PROCESS_DYNAMIC_EH_CONTINUATION_TARGET():
    PROCESS_DYNAMIC_EH_CONTINUATION_TARGET = win32more.System.Threading.PROCESS_DYNAMIC_EH_CONTINUATION_TARGET_head
    PROCESS_DYNAMIC_EH_CONTINUATION_TARGET._fields_ = [
        ('TargetAddress', UIntPtr),
        ('Flags', UIntPtr),
    ]
    return PROCESS_DYNAMIC_EH_CONTINUATION_TARGET
def _define_PROCESS_DYNAMIC_EH_CONTINUATION_TARGETS_INFORMATION_head():
    class PROCESS_DYNAMIC_EH_CONTINUATION_TARGETS_INFORMATION(Structure):
        pass
    return PROCESS_DYNAMIC_EH_CONTINUATION_TARGETS_INFORMATION
def _define_PROCESS_DYNAMIC_EH_CONTINUATION_TARGETS_INFORMATION():
    PROCESS_DYNAMIC_EH_CONTINUATION_TARGETS_INFORMATION = win32more.System.Threading.PROCESS_DYNAMIC_EH_CONTINUATION_TARGETS_INFORMATION_head
    PROCESS_DYNAMIC_EH_CONTINUATION_TARGETS_INFORMATION._fields_ = [
        ('NumberOfTargets', UInt16),
        ('Reserved', UInt16),
        ('Reserved2', UInt32),
        ('Targets', POINTER(win32more.System.Threading.PROCESS_DYNAMIC_EH_CONTINUATION_TARGET_head)),
    ]
    return PROCESS_DYNAMIC_EH_CONTINUATION_TARGETS_INFORMATION
def _define_PROCESS_DYNAMIC_ENFORCED_ADDRESS_RANGE_head():
    class PROCESS_DYNAMIC_ENFORCED_ADDRESS_RANGE(Structure):
        pass
    return PROCESS_DYNAMIC_ENFORCED_ADDRESS_RANGE
def _define_PROCESS_DYNAMIC_ENFORCED_ADDRESS_RANGE():
    PROCESS_DYNAMIC_ENFORCED_ADDRESS_RANGE = win32more.System.Threading.PROCESS_DYNAMIC_ENFORCED_ADDRESS_RANGE_head
    PROCESS_DYNAMIC_ENFORCED_ADDRESS_RANGE._fields_ = [
        ('BaseAddress', UIntPtr),
        ('Size', UIntPtr),
        ('Flags', UInt32),
    ]
    return PROCESS_DYNAMIC_ENFORCED_ADDRESS_RANGE
def _define_PROCESS_DYNAMIC_ENFORCED_ADDRESS_RANGES_INFORMATION_head():
    class PROCESS_DYNAMIC_ENFORCED_ADDRESS_RANGES_INFORMATION(Structure):
        pass
    return PROCESS_DYNAMIC_ENFORCED_ADDRESS_RANGES_INFORMATION
def _define_PROCESS_DYNAMIC_ENFORCED_ADDRESS_RANGES_INFORMATION():
    PROCESS_DYNAMIC_ENFORCED_ADDRESS_RANGES_INFORMATION = win32more.System.Threading.PROCESS_DYNAMIC_ENFORCED_ADDRESS_RANGES_INFORMATION_head
    PROCESS_DYNAMIC_ENFORCED_ADDRESS_RANGES_INFORMATION._fields_ = [
        ('NumberOfRanges', UInt16),
        ('Reserved', UInt16),
        ('Reserved2', UInt32),
        ('Ranges', POINTER(win32more.System.Threading.PROCESS_DYNAMIC_ENFORCED_ADDRESS_RANGE_head)),
    ]
    return PROCESS_DYNAMIC_ENFORCED_ADDRESS_RANGES_INFORMATION
def _define_PROCESS_INFORMATION_head():
    class PROCESS_INFORMATION(Structure):
        pass
    return PROCESS_INFORMATION
def _define_PROCESS_INFORMATION():
    PROCESS_INFORMATION = win32more.System.Threading.PROCESS_INFORMATION_head
    PROCESS_INFORMATION._fields_ = [
        ('hProcess', win32more.Foundation.HANDLE),
        ('hThread', win32more.Foundation.HANDLE),
        ('dwProcessId', UInt32),
        ('dwThreadId', UInt32),
    ]
    return PROCESS_INFORMATION
PROCESS_INFORMATION_CLASS = Int32
PROCESS_INFORMATION_CLASS_ProcessMemoryPriority = 0
PROCESS_INFORMATION_CLASS_ProcessMemoryExhaustionInfo = 1
PROCESS_INFORMATION_CLASS_ProcessAppMemoryInfo = 2
PROCESS_INFORMATION_CLASS_ProcessInPrivateInfo = 3
PROCESS_INFORMATION_CLASS_ProcessPowerThrottling = 4
PROCESS_INFORMATION_CLASS_ProcessReservedValue1 = 5
PROCESS_INFORMATION_CLASS_ProcessTelemetryCoverageInfo = 6
PROCESS_INFORMATION_CLASS_ProcessProtectionLevelInfo = 7
PROCESS_INFORMATION_CLASS_ProcessLeapSecondInfo = 8
PROCESS_INFORMATION_CLASS_ProcessMachineTypeInfo = 9
PROCESS_INFORMATION_CLASS_ProcessInformationClassMax = 10
def _define_PROCESS_LEAP_SECOND_INFO_head():
    class PROCESS_LEAP_SECOND_INFO(Structure):
        pass
    return PROCESS_LEAP_SECOND_INFO
def _define_PROCESS_LEAP_SECOND_INFO():
    PROCESS_LEAP_SECOND_INFO = win32more.System.Threading.PROCESS_LEAP_SECOND_INFO_head
    PROCESS_LEAP_SECOND_INFO._fields_ = [
        ('Flags', UInt32),
        ('Reserved', UInt32),
    ]
    return PROCESS_LEAP_SECOND_INFO
def _define_PROCESS_MACHINE_INFORMATION_head():
    class PROCESS_MACHINE_INFORMATION(Structure):
        pass
    return PROCESS_MACHINE_INFORMATION
def _define_PROCESS_MACHINE_INFORMATION():
    PROCESS_MACHINE_INFORMATION = win32more.System.Threading.PROCESS_MACHINE_INFORMATION_head
    PROCESS_MACHINE_INFORMATION._fields_ = [
        ('ProcessMachine', win32more.System.SystemInformation.IMAGE_FILE_MACHINE),
        ('Res0', UInt16),
        ('MachineAttributes', win32more.System.Threading.MACHINE_ATTRIBUTES),
    ]
    return PROCESS_MACHINE_INFORMATION
def _define_PROCESS_MEMORY_EXHAUSTION_INFO_head():
    class PROCESS_MEMORY_EXHAUSTION_INFO(Structure):
        pass
    return PROCESS_MEMORY_EXHAUSTION_INFO
def _define_PROCESS_MEMORY_EXHAUSTION_INFO():
    PROCESS_MEMORY_EXHAUSTION_INFO = win32more.System.Threading.PROCESS_MEMORY_EXHAUSTION_INFO_head
    PROCESS_MEMORY_EXHAUSTION_INFO._fields_ = [
        ('Version', UInt16),
        ('Reserved', UInt16),
        ('Type', win32more.System.Threading.PROCESS_MEMORY_EXHAUSTION_TYPE),
        ('Value', UIntPtr),
    ]
    return PROCESS_MEMORY_EXHAUSTION_INFO
PROCESS_MEMORY_EXHAUSTION_TYPE = Int32
PROCESS_MEMORY_EXHAUSTION_TYPE_PMETypeFailFastOnCommitFailure = 0
PROCESS_MEMORY_EXHAUSTION_TYPE_PMETypeMax = 1
PROCESS_MITIGATION_POLICY = Int32
PROCESS_MITIGATION_POLICY_ProcessDEPPolicy = 0
PROCESS_MITIGATION_POLICY_ProcessASLRPolicy = 1
PROCESS_MITIGATION_POLICY_ProcessDynamicCodePolicy = 2
PROCESS_MITIGATION_POLICY_ProcessStrictHandleCheckPolicy = 3
PROCESS_MITIGATION_POLICY_ProcessSystemCallDisablePolicy = 4
PROCESS_MITIGATION_POLICY_ProcessMitigationOptionsMask = 5
PROCESS_MITIGATION_POLICY_ProcessExtensionPointDisablePolicy = 6
PROCESS_MITIGATION_POLICY_ProcessControlFlowGuardPolicy = 7
PROCESS_MITIGATION_POLICY_ProcessSignaturePolicy = 8
PROCESS_MITIGATION_POLICY_ProcessFontDisablePolicy = 9
PROCESS_MITIGATION_POLICY_ProcessImageLoadPolicy = 10
PROCESS_MITIGATION_POLICY_ProcessSystemCallFilterPolicy = 11
PROCESS_MITIGATION_POLICY_ProcessPayloadRestrictionPolicy = 12
PROCESS_MITIGATION_POLICY_ProcessChildProcessPolicy = 13
PROCESS_MITIGATION_POLICY_ProcessSideChannelIsolationPolicy = 14
PROCESS_MITIGATION_POLICY_ProcessUserShadowStackPolicy = 15
PROCESS_MITIGATION_POLICY_ProcessRedirectionTrustPolicy = 16
PROCESS_MITIGATION_POLICY_MaxProcessMitigationPolicy = 17
PROCESS_NAME_FORMAT = UInt32
PROCESS_NAME_WIN32 = 0
PROCESS_NAME_NATIVE = 1
def _define_PROCESS_POWER_THROTTLING_STATE_head():
    class PROCESS_POWER_THROTTLING_STATE(Structure):
        pass
    return PROCESS_POWER_THROTTLING_STATE
def _define_PROCESS_POWER_THROTTLING_STATE():
    PROCESS_POWER_THROTTLING_STATE = win32more.System.Threading.PROCESS_POWER_THROTTLING_STATE_head
    PROCESS_POWER_THROTTLING_STATE._fields_ = [
        ('Version', UInt32),
        ('ControlMask', UInt32),
        ('StateMask', UInt32),
    ]
    return PROCESS_POWER_THROTTLING_STATE
PROCESS_PROTECTION_LEVEL = UInt32
PROTECTION_LEVEL_WINTCB_LIGHT = 0
PROTECTION_LEVEL_WINDOWS = 1
PROTECTION_LEVEL_WINDOWS_LIGHT = 2
PROTECTION_LEVEL_ANTIMALWARE_LIGHT = 3
PROTECTION_LEVEL_LSA_LIGHT = 4
PROTECTION_LEVEL_WINTCB = 5
PROTECTION_LEVEL_CODEGEN_LIGHT = 6
PROTECTION_LEVEL_AUTHENTICODE = 7
PROTECTION_LEVEL_PPL_APP = 8
PROTECTION_LEVEL_NONE = 4294967294
def _define_PROCESS_PROTECTION_LEVEL_INFORMATION_head():
    class PROCESS_PROTECTION_LEVEL_INFORMATION(Structure):
        pass
    return PROCESS_PROTECTION_LEVEL_INFORMATION
def _define_PROCESS_PROTECTION_LEVEL_INFORMATION():
    PROCESS_PROTECTION_LEVEL_INFORMATION = win32more.System.Threading.PROCESS_PROTECTION_LEVEL_INFORMATION_head
    PROCESS_PROTECTION_LEVEL_INFORMATION._fields_ = [
        ('ProtectionLevel', win32more.System.Threading.PROCESS_PROTECTION_LEVEL),
    ]
    return PROCESS_PROTECTION_LEVEL_INFORMATION
PROCESSINFOCLASS = Int32
PROCESSINFOCLASS_ProcessBasicInformation = 0
PROCESSINFOCLASS_ProcessDebugPort = 7
PROCESSINFOCLASS_ProcessWow64Information = 26
PROCESSINFOCLASS_ProcessImageFileName = 27
PROCESSINFOCLASS_ProcessBreakOnTermination = 29
PROCESSOR_FEATURE_ID = UInt32
PF_ARM_64BIT_LOADSTORE_ATOMIC = 25
PF_ARM_DIVIDE_INSTRUCTION_AVAILABLE = 24
PF_ARM_EXTERNAL_CACHE_AVAILABLE = 26
PF_ARM_FMAC_INSTRUCTIONS_AVAILABLE = 27
PF_ARM_VFP_32_REGISTERS_AVAILABLE = 18
PF_3DNOW_INSTRUCTIONS_AVAILABLE = 7
PF_CHANNELS_ENABLED = 16
PF_COMPARE_EXCHANGE_DOUBLE = 2
PF_COMPARE_EXCHANGE128 = 14
PF_COMPARE64_EXCHANGE128 = 15
PF_FASTFAIL_AVAILABLE = 23
PF_FLOATING_POINT_EMULATED = 1
PF_FLOATING_POINT_PRECISION_ERRATA = 0
PF_MMX_INSTRUCTIONS_AVAILABLE = 3
PF_NX_ENABLED = 12
PF_PAE_ENABLED = 9
PF_RDTSC_INSTRUCTION_AVAILABLE = 8
PF_RDWRFSGSBASE_AVAILABLE = 22
PF_SECOND_LEVEL_ADDRESS_TRANSLATION = 20
PF_SSE3_INSTRUCTIONS_AVAILABLE = 13
PF_VIRT_FIRMWARE_ENABLED = 21
PF_XMMI_INSTRUCTIONS_AVAILABLE = 6
PF_XMMI64_INSTRUCTIONS_AVAILABLE = 10
PF_XSAVE_ENABLED = 17
PF_ARM_V8_INSTRUCTIONS_AVAILABLE = 29
PF_ARM_V8_CRYPTO_INSTRUCTIONS_AVAILABLE = 30
PF_ARM_V8_CRC32_INSTRUCTIONS_AVAILABLE = 31
PF_ARM_V81_ATOMIC_INSTRUCTIONS_AVAILABLE = 34
def _define_PRTL_UMS_SCHEDULER_ENTRY_POINT():
    return WINFUNCTYPE(Void,win32more.System.SystemServices.RTL_UMS_SCHEDULER_REASON,UIntPtr,c_void_p)
def _define_PTIMERAPCROUTINE():
    return WINFUNCTYPE(Void,c_void_p,UInt32,UInt32)
def _define_PTP_CLEANUP_GROUP_CANCEL_CALLBACK():
    return WINFUNCTYPE(Void,c_void_p,c_void_p)
PTP_POOL = IntPtr
def _define_PTP_SIMPLE_CALLBACK():
    return WINFUNCTYPE(Void,POINTER(win32more.System.Threading.TP_CALLBACK_INSTANCE_head),c_void_p)
def _define_PTP_TIMER_CALLBACK():
    return WINFUNCTYPE(Void,POINTER(win32more.System.Threading.TP_CALLBACK_INSTANCE_head),c_void_p,POINTER(win32more.System.Threading.TP_TIMER_head))
def _define_PTP_WAIT_CALLBACK():
    return WINFUNCTYPE(Void,POINTER(win32more.System.Threading.TP_CALLBACK_INSTANCE_head),c_void_p,POINTER(win32more.System.Threading.TP_WAIT_head),UInt32)
def _define_PTP_WIN32_IO_CALLBACK():
    return WINFUNCTYPE(Void,POINTER(win32more.System.Threading.TP_CALLBACK_INSTANCE_head),c_void_p,c_void_p,UInt32,UIntPtr,POINTER(win32more.System.Threading.TP_IO_head))
def _define_PTP_WORK_CALLBACK():
    return WINFUNCTYPE(Void,POINTER(win32more.System.Threading.TP_CALLBACK_INSTANCE_head),c_void_p,POINTER(win32more.System.Threading.TP_WORK_head))
QUEUE_USER_APC_FLAGS = Int32
QUEUE_USER_APC_FLAGS_NONE = 0
QUEUE_USER_APC_FLAGS_SPECIAL_USER_APC = 1
def _define_REASON_CONTEXT_head():
    class REASON_CONTEXT(Structure):
        pass
    return REASON_CONTEXT
def _define_REASON_CONTEXT():
    REASON_CONTEXT = win32more.System.Threading.REASON_CONTEXT_head
    class REASON_CONTEXT__Reason_e__Union(Union):
        pass
    class REASON_CONTEXT__Reason_e__Union__Detailed_e__Struct(Structure):
        pass
    REASON_CONTEXT__Reason_e__Union__Detailed_e__Struct._fields_ = [
        ('LocalizedReasonModule', win32more.Foundation.HINSTANCE),
        ('LocalizedReasonId', UInt32),
        ('ReasonStringCount', UInt32),
        ('ReasonStrings', POINTER(win32more.Foundation.PWSTR)),
    ]
    REASON_CONTEXT__Reason_e__Union._fields_ = [
        ('Detailed', REASON_CONTEXT__Reason_e__Union__Detailed_e__Struct),
        ('SimpleReasonString', win32more.Foundation.PWSTR),
    ]
    REASON_CONTEXT._fields_ = [
        ('Version', UInt32),
        ('Flags', win32more.System.Threading.POWER_REQUEST_CONTEXT_FLAGS),
        ('Reason', REASON_CONTEXT__Reason_e__Union),
    ]
    return REASON_CONTEXT
def _define_RTL_BARRIER_head():
    class RTL_BARRIER(Structure):
        pass
    return RTL_BARRIER
def _define_RTL_BARRIER():
    RTL_BARRIER = win32more.System.Threading.RTL_BARRIER_head
    RTL_BARRIER._fields_ = [
        ('Reserved1', UInt32),
        ('Reserved2', UInt32),
        ('Reserved3', UIntPtr * 2),
        ('Reserved4', UInt32),
        ('Reserved5', UInt32),
    ]
    return RTL_BARRIER
def _define_RTL_CONDITION_VARIABLE_head():
    class RTL_CONDITION_VARIABLE(Structure):
        pass
    return RTL_CONDITION_VARIABLE
def _define_RTL_CONDITION_VARIABLE():
    RTL_CONDITION_VARIABLE = win32more.System.Threading.RTL_CONDITION_VARIABLE_head
    RTL_CONDITION_VARIABLE._fields_ = [
        ('Ptr', c_void_p),
    ]
    return RTL_CONDITION_VARIABLE
def _define_RTL_CRITICAL_SECTION_head():
    class RTL_CRITICAL_SECTION(Structure):
        pass
    return RTL_CRITICAL_SECTION
def _define_RTL_CRITICAL_SECTION():
    RTL_CRITICAL_SECTION = win32more.System.Threading.RTL_CRITICAL_SECTION_head
    RTL_CRITICAL_SECTION._fields_ = [
        ('DebugInfo', POINTER(win32more.System.Threading.RTL_CRITICAL_SECTION_DEBUG_head)),
        ('LockCount', Int32),
        ('RecursionCount', Int32),
        ('OwningThread', win32more.Foundation.HANDLE),
        ('LockSemaphore', win32more.Foundation.HANDLE),
        ('SpinCount', UIntPtr),
    ]
    return RTL_CRITICAL_SECTION
def _define_RTL_CRITICAL_SECTION_DEBUG_head():
    class RTL_CRITICAL_SECTION_DEBUG(Structure):
        pass
    return RTL_CRITICAL_SECTION_DEBUG
def _define_RTL_CRITICAL_SECTION_DEBUG():
    RTL_CRITICAL_SECTION_DEBUG = win32more.System.Threading.RTL_CRITICAL_SECTION_DEBUG_head
    RTL_CRITICAL_SECTION_DEBUG._fields_ = [
        ('Type', UInt16),
        ('CreatorBackTraceIndex', UInt16),
        ('CriticalSection', POINTER(win32more.System.Threading.RTL_CRITICAL_SECTION_head)),
        ('ProcessLocksList', win32more.System.Kernel.LIST_ENTRY),
        ('EntryCount', UInt32),
        ('ContentionCount', UInt32),
        ('Flags', UInt32),
        ('CreatorBackTraceIndexHigh', UInt16),
        ('SpareWORD', UInt16),
    ]
    return RTL_CRITICAL_SECTION_DEBUG
def _define_RTL_RUN_ONCE_head():
    class RTL_RUN_ONCE(Union):
        pass
    return RTL_RUN_ONCE
def _define_RTL_RUN_ONCE():
    RTL_RUN_ONCE = win32more.System.Threading.RTL_RUN_ONCE_head
    RTL_RUN_ONCE._fields_ = [
        ('Ptr', c_void_p),
    ]
    return RTL_RUN_ONCE
def _define_RTL_SRWLOCK_head():
    class RTL_SRWLOCK(Structure):
        pass
    return RTL_SRWLOCK
def _define_RTL_SRWLOCK():
    RTL_SRWLOCK = win32more.System.Threading.RTL_SRWLOCK_head
    RTL_SRWLOCK._fields_ = [
        ('Ptr', c_void_p),
    ]
    return RTL_SRWLOCK
RTL_UMS_THREAD_INFO_CLASS = Int32
RTL_UMS_THREAD_INFO_CLASS_UmsThreadInvalidInfoClass = 0
RTL_UMS_THREAD_INFO_CLASS_UmsThreadUserContext = 1
RTL_UMS_THREAD_INFO_CLASS_UmsThreadPriority = 2
RTL_UMS_THREAD_INFO_CLASS_UmsThreadAffinity = 3
RTL_UMS_THREAD_INFO_CLASS_UmsThreadTeb = 4
RTL_UMS_THREAD_INFO_CLASS_UmsThreadIsSuspended = 5
RTL_UMS_THREAD_INFO_CLASS_UmsThreadIsTerminated = 6
RTL_UMS_THREAD_INFO_CLASS_UmsThreadMaxInfoClass = 7
def _define_RTL_USER_PROCESS_PARAMETERS_head():
    class RTL_USER_PROCESS_PARAMETERS(Structure):
        pass
    return RTL_USER_PROCESS_PARAMETERS
def _define_RTL_USER_PROCESS_PARAMETERS():
    RTL_USER_PROCESS_PARAMETERS = win32more.System.Threading.RTL_USER_PROCESS_PARAMETERS_head
    RTL_USER_PROCESS_PARAMETERS._fields_ = [
        ('Reserved1', Byte * 16),
        ('Reserved2', c_void_p * 10),
        ('ImagePathName', win32more.Foundation.UNICODE_STRING),
        ('CommandLine', win32more.Foundation.UNICODE_STRING),
    ]
    return RTL_USER_PROCESS_PARAMETERS
def _define_STARTUPINFOA_head():
    class STARTUPINFOA(Structure):
        pass
    return STARTUPINFOA
def _define_STARTUPINFOA():
    STARTUPINFOA = win32more.System.Threading.STARTUPINFOA_head
    STARTUPINFOA._fields_ = [
        ('cb', UInt32),
        ('lpReserved', win32more.Foundation.PSTR),
        ('lpDesktop', win32more.Foundation.PSTR),
        ('lpTitle', win32more.Foundation.PSTR),
        ('dwX', UInt32),
        ('dwY', UInt32),
        ('dwXSize', UInt32),
        ('dwYSize', UInt32),
        ('dwXCountChars', UInt32),
        ('dwYCountChars', UInt32),
        ('dwFillAttribute', UInt32),
        ('dwFlags', win32more.System.Threading.STARTUPINFOW_FLAGS),
        ('wShowWindow', UInt16),
        ('cbReserved2', UInt16),
        ('lpReserved2', c_char_p_no),
        ('hStdInput', win32more.Foundation.HANDLE),
        ('hStdOutput', win32more.Foundation.HANDLE),
        ('hStdError', win32more.Foundation.HANDLE),
    ]
    return STARTUPINFOA
def _define_STARTUPINFOEXA_head():
    class STARTUPINFOEXA(Structure):
        pass
    return STARTUPINFOEXA
def _define_STARTUPINFOEXA():
    STARTUPINFOEXA = win32more.System.Threading.STARTUPINFOEXA_head
    STARTUPINFOEXA._fields_ = [
        ('StartupInfo', win32more.System.Threading.STARTUPINFOA),
        ('lpAttributeList', win32more.System.Threading.LPPROC_THREAD_ATTRIBUTE_LIST),
    ]
    return STARTUPINFOEXA
def _define_STARTUPINFOEXW_head():
    class STARTUPINFOEXW(Structure):
        pass
    return STARTUPINFOEXW
def _define_STARTUPINFOEXW():
    STARTUPINFOEXW = win32more.System.Threading.STARTUPINFOEXW_head
    STARTUPINFOEXW._fields_ = [
        ('StartupInfo', win32more.System.Threading.STARTUPINFOW),
        ('lpAttributeList', win32more.System.Threading.LPPROC_THREAD_ATTRIBUTE_LIST),
    ]
    return STARTUPINFOEXW
def _define_STARTUPINFOW_head():
    class STARTUPINFOW(Structure):
        pass
    return STARTUPINFOW
def _define_STARTUPINFOW():
    STARTUPINFOW = win32more.System.Threading.STARTUPINFOW_head
    STARTUPINFOW._fields_ = [
        ('cb', UInt32),
        ('lpReserved', win32more.Foundation.PWSTR),
        ('lpDesktop', win32more.Foundation.PWSTR),
        ('lpTitle', win32more.Foundation.PWSTR),
        ('dwX', UInt32),
        ('dwY', UInt32),
        ('dwXSize', UInt32),
        ('dwYSize', UInt32),
        ('dwXCountChars', UInt32),
        ('dwYCountChars', UInt32),
        ('dwFillAttribute', UInt32),
        ('dwFlags', win32more.System.Threading.STARTUPINFOW_FLAGS),
        ('wShowWindow', UInt16),
        ('cbReserved2', UInt16),
        ('lpReserved2', c_char_p_no),
        ('hStdInput', win32more.Foundation.HANDLE),
        ('hStdOutput', win32more.Foundation.HANDLE),
        ('hStdError', win32more.Foundation.HANDLE),
    ]
    return STARTUPINFOW
STARTUPINFOW_FLAGS = UInt32
STARTF_FORCEONFEEDBACK = 64
STARTF_FORCEOFFFEEDBACK = 128
STARTF_PREVENTPINNING = 8192
STARTF_RUNFULLSCREEN = 32
STARTF_TITLEISAPPID = 4096
STARTF_TITLEISLINKNAME = 2048
STARTF_UNTRUSTEDSOURCE = 32768
STARTF_USECOUNTCHARS = 8
STARTF_USEFILLATTRIBUTE = 16
STARTF_USEHOTKEY = 512
STARTF_USEPOSITION = 4
STARTF_USESHOWWINDOW = 1
STARTF_USESIZE = 2
STARTF_USESTDHANDLES = 256
SYNCHRONIZATION_ACCESS_RIGHTS = UInt32
EVENT_ALL_ACCESS = 2031619
EVENT_MODIFY_STATE = 2
MUTEX_ALL_ACCESS = 2031617
MUTEX_MODIFY_STATE = 1
SEMAPHORE_ALL_ACCESS = 2031619
SEMAPHORE_MODIFY_STATE = 2
TIMER_ALL_ACCESS = 2031619
TIMER_MODIFY_STATE = 2
TIMER_QUERY_STATE = 1
SYNCHRONIZATION_DELETE = 65536
SYNCHRONIZATION_READ_CONTROL = 131072
SYNCHRONIZATION_WRITE_DAC = 262144
SYNCHRONIZATION_WRITE_OWNER = 524288
SYNCHRONIZATION_SYNCHRONIZE = 1048576
THREAD_ACCESS_RIGHTS = UInt32
THREAD_TERMINATE = 1
THREAD_SUSPEND_RESUME = 2
THREAD_GET_CONTEXT = 8
THREAD_SET_CONTEXT = 16
THREAD_SET_INFORMATION = 32
THREAD_QUERY_INFORMATION = 64
THREAD_SET_THREAD_TOKEN = 128
THREAD_IMPERSONATE = 256
THREAD_DIRECT_IMPERSONATION = 512
THREAD_SET_LIMITED_INFORMATION = 1024
THREAD_QUERY_LIMITED_INFORMATION = 2048
THREAD_RESUME = 4096
THREAD_ALL_ACCESS = 2097151
THREAD_DELETE = 65536
THREAD_READ_CONTROL = 131072
THREAD_WRITE_DAC = 262144
THREAD_WRITE_OWNER = 524288
THREAD_SYNCHRONIZE = 1048576
THREAD_STANDARD_RIGHTS_REQUIRED = 983040
THREAD_CREATION_FLAGS = UInt32
THREAD_CREATE_RUN_IMMEDIATELY = 0
THREAD_CREATE_SUSPENDED = 4
STACK_SIZE_PARAM_IS_A_RESERVATION = 65536
THREAD_INFORMATION_CLASS = Int32
THREAD_INFORMATION_CLASS_ThreadMemoryPriority = 0
THREAD_INFORMATION_CLASS_ThreadAbsoluteCpuPriority = 1
THREAD_INFORMATION_CLASS_ThreadDynamicCodePolicy = 2
THREAD_INFORMATION_CLASS_ThreadPowerThrottling = 3
THREAD_INFORMATION_CLASS_ThreadInformationClassMax = 4
def _define_THREAD_POWER_THROTTLING_STATE_head():
    class THREAD_POWER_THROTTLING_STATE(Structure):
        pass
    return THREAD_POWER_THROTTLING_STATE
def _define_THREAD_POWER_THROTTLING_STATE():
    THREAD_POWER_THROTTLING_STATE = win32more.System.Threading.THREAD_POWER_THROTTLING_STATE_head
    THREAD_POWER_THROTTLING_STATE._fields_ = [
        ('Version', UInt32),
        ('ControlMask', UInt32),
        ('StateMask', UInt32),
    ]
    return THREAD_POWER_THROTTLING_STATE
THREAD_PRIORITY = Int32
THREAD_MODE_BACKGROUND_BEGIN = 65536
THREAD_MODE_BACKGROUND_END = 131072
THREAD_PRIORITY_ABOVE_NORMAL = 1
THREAD_PRIORITY_BELOW_NORMAL = -1
THREAD_PRIORITY_HIGHEST = 2
THREAD_PRIORITY_IDLE = -15
THREAD_PRIORITY_MIN = -2
THREAD_PRIORITY_LOWEST = -2
THREAD_PRIORITY_NORMAL = 0
THREAD_PRIORITY_TIME_CRITICAL = 15
THREADINFOCLASS = Int32
THREADINFOCLASS_ThreadIsIoPending = 16
THREADINFOCLASS_ThreadNameInformation = 38
TimerQueueHandle = IntPtr
def _define_TP_CALLBACK_ENVIRON_V3_head():
    class TP_CALLBACK_ENVIRON_V3(Structure):
        pass
    return TP_CALLBACK_ENVIRON_V3
def _define_TP_CALLBACK_ENVIRON_V3():
    TP_CALLBACK_ENVIRON_V3 = win32more.System.Threading.TP_CALLBACK_ENVIRON_V3_head
    class TP_CALLBACK_ENVIRON_V3__ACTIVATION_CONTEXT(Structure):
        pass
    class TP_CALLBACK_ENVIRON_V3__u_e__Union(Union):
        pass
    class TP_CALLBACK_ENVIRON_V3__u_e__Union__s_e__Struct(Structure):
        pass
    TP_CALLBACK_ENVIRON_V3__u_e__Union__s_e__Struct._fields_ = [
        ('_bitfield', UInt32),
    ]
    TP_CALLBACK_ENVIRON_V3__u_e__Union._fields_ = [
        ('Flags', UInt32),
        ('s', TP_CALLBACK_ENVIRON_V3__u_e__Union__s_e__Struct),
    ]
    TP_CALLBACK_ENVIRON_V3._fields_ = [
        ('Version', UInt32),
        ('Pool', win32more.System.Threading.PTP_POOL),
        ('CleanupGroup', IntPtr),
        ('CleanupGroupCancelCallback', win32more.System.Threading.PTP_CLEANUP_GROUP_CANCEL_CALLBACK),
        ('RaceDll', c_void_p),
        ('ActivationContext', IntPtr),
        ('FinalizationCallback', win32more.System.Threading.PTP_SIMPLE_CALLBACK),
        ('u', TP_CALLBACK_ENVIRON_V3__u_e__Union),
        ('CallbackPriority', win32more.System.Threading.TP_CALLBACK_PRIORITY),
        ('Size', UInt32),
    ]
    return TP_CALLBACK_ENVIRON_V3
def _define_TP_CALLBACK_INSTANCE_head():
    class TP_CALLBACK_INSTANCE(Structure):
        pass
    return TP_CALLBACK_INSTANCE
def _define_TP_CALLBACK_INSTANCE():
    TP_CALLBACK_INSTANCE = win32more.System.Threading.TP_CALLBACK_INSTANCE_head
    return TP_CALLBACK_INSTANCE
TP_CALLBACK_PRIORITY = Int32
TP_CALLBACK_PRIORITY_HIGH = 0
TP_CALLBACK_PRIORITY_NORMAL = 1
TP_CALLBACK_PRIORITY_LOW = 2
TP_CALLBACK_PRIORITY_INVALID = 3
TP_CALLBACK_PRIORITY_COUNT = 3
def _define_TP_IO_head():
    class TP_IO(Structure):
        pass
    return TP_IO
def _define_TP_IO():
    TP_IO = win32more.System.Threading.TP_IO_head
    return TP_IO
def _define_TP_POOL_STACK_INFORMATION_head():
    class TP_POOL_STACK_INFORMATION(Structure):
        pass
    return TP_POOL_STACK_INFORMATION
def _define_TP_POOL_STACK_INFORMATION():
    TP_POOL_STACK_INFORMATION = win32more.System.Threading.TP_POOL_STACK_INFORMATION_head
    TP_POOL_STACK_INFORMATION._fields_ = [
        ('StackReserve', UIntPtr),
        ('StackCommit', UIntPtr),
    ]
    return TP_POOL_STACK_INFORMATION
def _define_TP_TIMER_head():
    class TP_TIMER(Structure):
        pass
    return TP_TIMER
def _define_TP_TIMER():
    TP_TIMER = win32more.System.Threading.TP_TIMER_head
    return TP_TIMER
def _define_TP_WAIT_head():
    class TP_WAIT(Structure):
        pass
    return TP_WAIT
def _define_TP_WAIT():
    TP_WAIT = win32more.System.Threading.TP_WAIT_head
    return TP_WAIT
def _define_TP_WORK_head():
    class TP_WORK(Structure):
        pass
    return TP_WORK
def _define_TP_WORK():
    TP_WORK = win32more.System.Threading.TP_WORK_head
    return TP_WORK
def _define_UMS_SCHEDULER_STARTUP_INFO_head():
    class UMS_SCHEDULER_STARTUP_INFO(Structure):
        pass
    return UMS_SCHEDULER_STARTUP_INFO
def _define_UMS_SCHEDULER_STARTUP_INFO():
    UMS_SCHEDULER_STARTUP_INFO = win32more.System.Threading.UMS_SCHEDULER_STARTUP_INFO_head
    UMS_SCHEDULER_STARTUP_INFO._fields_ = [
        ('UmsVersion', UInt32),
        ('CompletionList', c_void_p),
        ('SchedulerProc', win32more.System.Threading.PRTL_UMS_SCHEDULER_ENTRY_POINT),
        ('SchedulerParam', c_void_p),
    ]
    return UMS_SCHEDULER_STARTUP_INFO
def _define_UMS_SYSTEM_THREAD_INFORMATION_head():
    class UMS_SYSTEM_THREAD_INFORMATION(Structure):
        pass
    return UMS_SYSTEM_THREAD_INFORMATION
def _define_UMS_SYSTEM_THREAD_INFORMATION():
    UMS_SYSTEM_THREAD_INFORMATION = win32more.System.Threading.UMS_SYSTEM_THREAD_INFORMATION_head
    class UMS_SYSTEM_THREAD_INFORMATION__Anonymous_e__Union(Union):
        pass
    class UMS_SYSTEM_THREAD_INFORMATION__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    UMS_SYSTEM_THREAD_INFORMATION__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ('_bitfield', UInt32),
    ]
    UMS_SYSTEM_THREAD_INFORMATION__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    UMS_SYSTEM_THREAD_INFORMATION__Anonymous_e__Union._fields_ = [
        ('Anonymous', UMS_SYSTEM_THREAD_INFORMATION__Anonymous_e__Union__Anonymous_e__Struct),
        ('ThreadUmsFlags', UInt32),
    ]
    UMS_SYSTEM_THREAD_INFORMATION._anonymous_ = [
        'Anonymous',
    ]
    UMS_SYSTEM_THREAD_INFORMATION._fields_ = [
        ('UmsVersion', UInt32),
        ('Anonymous', UMS_SYSTEM_THREAD_INFORMATION__Anonymous_e__Union),
    ]
    return UMS_SYSTEM_THREAD_INFORMATION
def _define_WAITORTIMERCALLBACK():
    return WINFUNCTYPE(Void,c_void_p,win32more.Foundation.BOOLEAN)
WORKER_THREAD_FLAGS = UInt32
WT_EXECUTEDEFAULT = 0
WT_EXECUTEINIOTHREAD = 1
WT_EXECUTEINPERSISTENTTHREAD = 128
WT_EXECUTEINWAITTHREAD = 4
WT_EXECUTELONGFUNCTION = 16
WT_EXECUTEONLYONCE = 8
WT_TRANSFER_IMPERSONATION = 256
WT_EXECUTEINTIMERTHREAD = 32
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
