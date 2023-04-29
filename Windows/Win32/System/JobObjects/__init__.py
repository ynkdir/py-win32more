from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.Security
import Windows.Win32.System.JobObjects
import Windows.Win32.System.Threading
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
def IsProcessInJob(ProcessHandle: Windows.Win32.Foundation.HANDLE, JobHandle: Windows.Win32.Foundation.HANDLE, Result: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateJobObjectW(lpJobAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head), lpName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def FreeMemoryJobObject(Buffer: c_void_p) -> Void: ...
@winfunctype('KERNEL32.dll')
def OpenJobObjectW(dwDesiredAccess: UInt32, bInheritHandle: Windows.Win32.Foundation.BOOL, lpName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def AssignProcessToJobObject(hJob: Windows.Win32.Foundation.HANDLE, hProcess: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def TerminateJobObject(hJob: Windows.Win32.Foundation.HANDLE, uExitCode: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetInformationJobObject(hJob: Windows.Win32.Foundation.HANDLE, JobObjectInformationClass: Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS, lpJobObjectInformation: c_void_p, cbJobObjectInformationLength: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetIoRateControlInformationJobObject(hJob: Windows.Win32.Foundation.HANDLE, IoRateControlInfo: POINTER(Windows.Win32.System.JobObjects.JOBOBJECT_IO_RATE_CONTROL_INFORMATION_head)) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def QueryInformationJobObject(hJob: Windows.Win32.Foundation.HANDLE, JobObjectInformationClass: Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS, lpJobObjectInformation: c_void_p, cbJobObjectInformationLength: UInt32, lpReturnLength: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def QueryIoRateControlInformationJobObject(hJob: Windows.Win32.Foundation.HANDLE, VolumeName: Windows.Win32.Foundation.PWSTR, InfoBlocks: POINTER(POINTER(Windows.Win32.System.JobObjects.JOBOBJECT_IO_RATE_CONTROL_INFORMATION_head)), InfoBlockCount: POINTER(UInt32)) -> UInt32: ...
@winfunctype('USER32.dll')
def UserHandleGrantAccess(hUserHandle: Windows.Win32.Foundation.HANDLE, hJob: Windows.Win32.Foundation.HANDLE, bGrant: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateJobObjectA(lpJobAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head), lpName: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def OpenJobObjectA(dwDesiredAccess: UInt32, bInheritHandle: Windows.Win32.Foundation.BOOL, lpName: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def CreateJobSet(NumJob: UInt32, UserJobSet: POINTER(Windows.Win32.System.JobObjects.JOB_SET_ARRAY_head), Flags: UInt32) -> Windows.Win32.Foundation.BOOL: ...
JOBOBJECTINFOCLASS = Int32
JOBOBJECTINFOCLASS_JobObjectBasicAccountingInformation: JOBOBJECTINFOCLASS = 1
JOBOBJECTINFOCLASS_JobObjectBasicLimitInformation: JOBOBJECTINFOCLASS = 2
JOBOBJECTINFOCLASS_JobObjectBasicProcessIdList: JOBOBJECTINFOCLASS = 3
JOBOBJECTINFOCLASS_JobObjectBasicUIRestrictions: JOBOBJECTINFOCLASS = 4
JOBOBJECTINFOCLASS_JobObjectSecurityLimitInformation: JOBOBJECTINFOCLASS = 5
JOBOBJECTINFOCLASS_JobObjectEndOfJobTimeInformation: JOBOBJECTINFOCLASS = 6
JOBOBJECTINFOCLASS_JobObjectAssociateCompletionPortInformation: JOBOBJECTINFOCLASS = 7
JOBOBJECTINFOCLASS_JobObjectBasicAndIoAccountingInformation: JOBOBJECTINFOCLASS = 8
JOBOBJECTINFOCLASS_JobObjectExtendedLimitInformation: JOBOBJECTINFOCLASS = 9
JOBOBJECTINFOCLASS_JobObjectJobSetInformation: JOBOBJECTINFOCLASS = 10
JOBOBJECTINFOCLASS_JobObjectGroupInformation: JOBOBJECTINFOCLASS = 11
JOBOBJECTINFOCLASS_JobObjectNotificationLimitInformation: JOBOBJECTINFOCLASS = 12
JOBOBJECTINFOCLASS_JobObjectLimitViolationInformation: JOBOBJECTINFOCLASS = 13
JOBOBJECTINFOCLASS_JobObjectGroupInformationEx: JOBOBJECTINFOCLASS = 14
JOBOBJECTINFOCLASS_JobObjectCpuRateControlInformation: JOBOBJECTINFOCLASS = 15
JOBOBJECTINFOCLASS_JobObjectCompletionFilter: JOBOBJECTINFOCLASS = 16
JOBOBJECTINFOCLASS_JobObjectCompletionCounter: JOBOBJECTINFOCLASS = 17
JOBOBJECTINFOCLASS_JobObjectReserved1Information: JOBOBJECTINFOCLASS = 18
JOBOBJECTINFOCLASS_JobObjectReserved2Information: JOBOBJECTINFOCLASS = 19
JOBOBJECTINFOCLASS_JobObjectReserved3Information: JOBOBJECTINFOCLASS = 20
JOBOBJECTINFOCLASS_JobObjectReserved4Information: JOBOBJECTINFOCLASS = 21
JOBOBJECTINFOCLASS_JobObjectReserved5Information: JOBOBJECTINFOCLASS = 22
JOBOBJECTINFOCLASS_JobObjectReserved6Information: JOBOBJECTINFOCLASS = 23
JOBOBJECTINFOCLASS_JobObjectReserved7Information: JOBOBJECTINFOCLASS = 24
JOBOBJECTINFOCLASS_JobObjectReserved8Information: JOBOBJECTINFOCLASS = 25
JOBOBJECTINFOCLASS_JobObjectReserved9Information: JOBOBJECTINFOCLASS = 26
JOBOBJECTINFOCLASS_JobObjectReserved10Information: JOBOBJECTINFOCLASS = 27
JOBOBJECTINFOCLASS_JobObjectReserved11Information: JOBOBJECTINFOCLASS = 28
JOBOBJECTINFOCLASS_JobObjectReserved12Information: JOBOBJECTINFOCLASS = 29
JOBOBJECTINFOCLASS_JobObjectReserved13Information: JOBOBJECTINFOCLASS = 30
JOBOBJECTINFOCLASS_JobObjectReserved14Information: JOBOBJECTINFOCLASS = 31
JOBOBJECTINFOCLASS_JobObjectNetRateControlInformation: JOBOBJECTINFOCLASS = 32
JOBOBJECTINFOCLASS_JobObjectNotificationLimitInformation2: JOBOBJECTINFOCLASS = 33
JOBOBJECTINFOCLASS_JobObjectLimitViolationInformation2: JOBOBJECTINFOCLASS = 34
JOBOBJECTINFOCLASS_JobObjectCreateSilo: JOBOBJECTINFOCLASS = 35
JOBOBJECTINFOCLASS_JobObjectSiloBasicInformation: JOBOBJECTINFOCLASS = 36
JOBOBJECTINFOCLASS_JobObjectReserved15Information: JOBOBJECTINFOCLASS = 37
JOBOBJECTINFOCLASS_JobObjectReserved16Information: JOBOBJECTINFOCLASS = 38
JOBOBJECTINFOCLASS_JobObjectReserved17Information: JOBOBJECTINFOCLASS = 39
JOBOBJECTINFOCLASS_JobObjectReserved18Information: JOBOBJECTINFOCLASS = 40
JOBOBJECTINFOCLASS_JobObjectReserved19Information: JOBOBJECTINFOCLASS = 41
JOBOBJECTINFOCLASS_JobObjectReserved20Information: JOBOBJECTINFOCLASS = 42
JOBOBJECTINFOCLASS_JobObjectReserved21Information: JOBOBJECTINFOCLASS = 43
JOBOBJECTINFOCLASS_JobObjectReserved22Information: JOBOBJECTINFOCLASS = 44
JOBOBJECTINFOCLASS_JobObjectReserved23Information: JOBOBJECTINFOCLASS = 45
JOBOBJECTINFOCLASS_JobObjectReserved24Information: JOBOBJECTINFOCLASS = 46
JOBOBJECTINFOCLASS_JobObjectReserved25Information: JOBOBJECTINFOCLASS = 47
JOBOBJECTINFOCLASS_JobObjectReserved26Information: JOBOBJECTINFOCLASS = 48
JOBOBJECTINFOCLASS_JobObjectReserved27Information: JOBOBJECTINFOCLASS = 49
JOBOBJECTINFOCLASS_MaxJobObjectInfoClass: JOBOBJECTINFOCLASS = 50
class JOBOBJECT_ASSOCIATE_COMPLETION_PORT(EasyCastStructure):
    CompletionKey: c_void_p
    CompletionPort: Windows.Win32.Foundation.HANDLE
class JOBOBJECT_BASIC_ACCOUNTING_INFORMATION(EasyCastStructure):
    TotalUserTime: Int64
    TotalKernelTime: Int64
    ThisPeriodTotalUserTime: Int64
    ThisPeriodTotalKernelTime: Int64
    TotalPageFaultCount: UInt32
    TotalProcesses: UInt32
    ActiveProcesses: UInt32
    TotalTerminatedProcesses: UInt32
class JOBOBJECT_BASIC_AND_IO_ACCOUNTING_INFORMATION(EasyCastStructure):
    BasicInfo: Windows.Win32.System.JobObjects.JOBOBJECT_BASIC_ACCOUNTING_INFORMATION
    IoInfo: Windows.Win32.System.Threading.IO_COUNTERS
class JOBOBJECT_BASIC_LIMIT_INFORMATION(EasyCastStructure):
    PerProcessUserTimeLimit: Int64
    PerJobUserTimeLimit: Int64
    LimitFlags: Windows.Win32.System.JobObjects.JOB_OBJECT_LIMIT
    MinimumWorkingSetSize: UIntPtr
    MaximumWorkingSetSize: UIntPtr
    ActiveProcessLimit: UInt32
    Affinity: UIntPtr
    PriorityClass: UInt32
    SchedulingClass: UInt32
class JOBOBJECT_BASIC_PROCESS_ID_LIST(EasyCastStructure):
    NumberOfAssignedProcesses: UInt32
    NumberOfProcessIdsInList: UInt32
    ProcessIdList: UIntPtr * 1
class JOBOBJECT_BASIC_UI_RESTRICTIONS(EasyCastStructure):
    UIRestrictionsClass: Windows.Win32.System.JobObjects.JOB_OBJECT_UILIMIT
class JOBOBJECT_CPU_RATE_CONTROL_INFORMATION(EasyCastStructure):
    ControlFlags: Windows.Win32.System.JobObjects.JOB_OBJECT_CPU_RATE_CONTROL
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        CpuRate: UInt32
        Weight: UInt32
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(EasyCastStructure):
            MinRate: UInt16
            MaxRate: UInt16
class JOBOBJECT_END_OF_JOB_TIME_INFORMATION(EasyCastStructure):
    EndOfJobTimeAction: Windows.Win32.System.JobObjects.JOB_OBJECT_TERMINATE_AT_END_ACTION
class JOBOBJECT_EXTENDED_LIMIT_INFORMATION(EasyCastStructure):
    BasicLimitInformation: Windows.Win32.System.JobObjects.JOBOBJECT_BASIC_LIMIT_INFORMATION
    IoInfo: Windows.Win32.System.Threading.IO_COUNTERS
    ProcessMemoryLimit: UIntPtr
    JobMemoryLimit: UIntPtr
    PeakProcessMemoryUsed: UIntPtr
    PeakJobMemoryUsed: UIntPtr
JOBOBJECT_IO_ATTRIBUTION_CONTROL_FLAGS = Int32
JOBOBJECT_IO_ATTRIBUTION_CONTROL_ENABLE: JOBOBJECT_IO_ATTRIBUTION_CONTROL_FLAGS = 1
JOBOBJECT_IO_ATTRIBUTION_CONTROL_DISABLE: JOBOBJECT_IO_ATTRIBUTION_CONTROL_FLAGS = 2
JOBOBJECT_IO_ATTRIBUTION_CONTROL_VALID_FLAGS: JOBOBJECT_IO_ATTRIBUTION_CONTROL_FLAGS = 3
class JOBOBJECT_IO_ATTRIBUTION_INFORMATION(EasyCastStructure):
    ControlFlags: UInt32
    ReadStats: Windows.Win32.System.JobObjects.JOBOBJECT_IO_ATTRIBUTION_STATS
    WriteStats: Windows.Win32.System.JobObjects.JOBOBJECT_IO_ATTRIBUTION_STATS
class JOBOBJECT_IO_ATTRIBUTION_STATS(EasyCastStructure):
    IoCount: UIntPtr
    TotalNonOverlappedQueueTime: UInt64
    TotalNonOverlappedServiceTime: UInt64
    TotalSize: UInt64
class JOBOBJECT_IO_RATE_CONTROL_INFORMATION(EasyCastStructure):
    MaxIops: Int64
    MaxBandwidth: Int64
    ReservationIops: Int64
    VolumeName: Windows.Win32.Foundation.PWSTR
    BaseIoSize: UInt32
    ControlFlags: Windows.Win32.System.JobObjects.JOB_OBJECT_IO_RATE_CONTROL_FLAGS
class JOBOBJECT_IO_RATE_CONTROL_INFORMATION_NATIVE_V1(EasyCastStructure):
    MaxIops: Int64
    MaxBandwidth: Int64
    ReservationIops: Int64
    VolumeName: Windows.Win32.Foundation.PWSTR
    BaseIoSize: UInt32
    ControlFlags: Windows.Win32.System.JobObjects.JOB_OBJECT_IO_RATE_CONTROL_FLAGS
    VolumeNameLength: UInt16
class JOBOBJECT_IO_RATE_CONTROL_INFORMATION_NATIVE_V2(EasyCastStructure):
    MaxIops: Int64
    MaxBandwidth: Int64
    ReservationIops: Int64
    VolumeName: Windows.Win32.Foundation.PWSTR
    BaseIoSize: UInt32
    ControlFlags: Windows.Win32.System.JobObjects.JOB_OBJECT_IO_RATE_CONTROL_FLAGS
    VolumeNameLength: UInt16
    CriticalReservationIops: Int64
    ReservationBandwidth: Int64
    CriticalReservationBandwidth: Int64
    MaxTimePercent: Int64
    ReservationTimePercent: Int64
    CriticalReservationTimePercent: Int64
class JOBOBJECT_IO_RATE_CONTROL_INFORMATION_NATIVE_V3(EasyCastStructure):
    MaxIops: Int64
    MaxBandwidth: Int64
    ReservationIops: Int64
    VolumeName: Windows.Win32.Foundation.PWSTR
    BaseIoSize: UInt32
    ControlFlags: Windows.Win32.System.JobObjects.JOB_OBJECT_IO_RATE_CONTROL_FLAGS
    VolumeNameLength: UInt16
    CriticalReservationIops: Int64
    ReservationBandwidth: Int64
    CriticalReservationBandwidth: Int64
    MaxTimePercent: Int64
    ReservationTimePercent: Int64
    CriticalReservationTimePercent: Int64
    SoftMaxIops: Int64
    SoftMaxBandwidth: Int64
    SoftMaxTimePercent: Int64
    LimitExcessNotifyIops: Int64
    LimitExcessNotifyBandwidth: Int64
    LimitExcessNotifyTimePercent: Int64
class JOBOBJECT_JOBSET_INFORMATION(EasyCastStructure):
    MemberLevel: UInt32
class JOBOBJECT_LIMIT_VIOLATION_INFORMATION(EasyCastStructure):
    LimitFlags: Windows.Win32.System.JobObjects.JOB_OBJECT_LIMIT
    ViolationLimitFlags: Windows.Win32.System.JobObjects.JOB_OBJECT_LIMIT
    IoReadBytes: UInt64
    IoReadBytesLimit: UInt64
    IoWriteBytes: UInt64
    IoWriteBytesLimit: UInt64
    PerJobUserTime: Int64
    PerJobUserTimeLimit: Int64
    JobMemory: UInt64
    JobMemoryLimit: UInt64
    RateControlTolerance: Windows.Win32.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE
    RateControlToleranceLimit: Windows.Win32.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE
class JOBOBJECT_LIMIT_VIOLATION_INFORMATION_2(EasyCastStructure):
    LimitFlags: Windows.Win32.System.JobObjects.JOB_OBJECT_LIMIT
    ViolationLimitFlags: Windows.Win32.System.JobObjects.JOB_OBJECT_LIMIT
    IoReadBytes: UInt64
    IoReadBytesLimit: UInt64
    IoWriteBytes: UInt64
    IoWriteBytesLimit: UInt64
    PerJobUserTime: Int64
    PerJobUserTimeLimit: Int64
    JobMemory: UInt64
    Anonymous1: _Anonymous1_e__Union
    Anonymous2: _Anonymous2_e__Union
    Anonymous3: _Anonymous3_e__Union
    JobLowMemoryLimit: UInt64
    IoRateControlTolerance: Windows.Win32.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE
    IoRateControlToleranceLimit: Windows.Win32.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE
    NetRateControlTolerance: Windows.Win32.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE
    NetRateControlToleranceLimit: Windows.Win32.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE
    class _Anonymous1_e__Union(EasyCastUnion):
        JobHighMemoryLimit: UInt64
        JobMemoryLimit: UInt64
    class _Anonymous2_e__Union(EasyCastUnion):
        RateControlTolerance: Windows.Win32.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE
        CpuRateControlTolerance: Windows.Win32.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE
    class _Anonymous3_e__Union(EasyCastUnion):
        RateControlToleranceLimit: Windows.Win32.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE
        CpuRateControlToleranceLimit: Windows.Win32.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE
class JOBOBJECT_NET_RATE_CONTROL_INFORMATION(EasyCastStructure):
    MaxBandwidth: UInt64
    ControlFlags: Windows.Win32.System.JobObjects.JOB_OBJECT_NET_RATE_CONTROL_FLAGS
    DscpTag: Byte
class JOBOBJECT_NOTIFICATION_LIMIT_INFORMATION(EasyCastStructure):
    IoReadBytesLimit: UInt64
    IoWriteBytesLimit: UInt64
    PerJobUserTimeLimit: Int64
    JobMemoryLimit: UInt64
    RateControlTolerance: Windows.Win32.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE
    RateControlToleranceInterval: Windows.Win32.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE_INTERVAL
    LimitFlags: Windows.Win32.System.JobObjects.JOB_OBJECT_LIMIT
class JOBOBJECT_NOTIFICATION_LIMIT_INFORMATION_2(EasyCastStructure):
    IoReadBytesLimit: UInt64
    IoWriteBytesLimit: UInt64
    PerJobUserTimeLimit: Int64
    Anonymous1: _Anonymous1_e__Union
    Anonymous2: _Anonymous2_e__Union
    Anonymous3: _Anonymous3_e__Union
    LimitFlags: Windows.Win32.System.JobObjects.JOB_OBJECT_LIMIT
    IoRateControlTolerance: Windows.Win32.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE
    JobLowMemoryLimit: UInt64
    IoRateControlToleranceInterval: Windows.Win32.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE_INTERVAL
    NetRateControlTolerance: Windows.Win32.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE
    NetRateControlToleranceInterval: Windows.Win32.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE_INTERVAL
    class _Anonymous1_e__Union(EasyCastUnion):
        JobHighMemoryLimit: UInt64
        JobMemoryLimit: UInt64
    class _Anonymous2_e__Union(EasyCastUnion):
        RateControlTolerance: Windows.Win32.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE
        CpuRateControlTolerance: Windows.Win32.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE
    class _Anonymous3_e__Union(EasyCastUnion):
        RateControlToleranceInterval: Windows.Win32.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE_INTERVAL
        CpuRateControlToleranceInterval: Windows.Win32.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE_INTERVAL
JOBOBJECT_RATE_CONTROL_TOLERANCE = Int32
JOBOBJECT_RATE_CONTROL_TOLERANCE_ToleranceLow: JOBOBJECT_RATE_CONTROL_TOLERANCE = 1
JOBOBJECT_RATE_CONTROL_TOLERANCE_ToleranceMedium: JOBOBJECT_RATE_CONTROL_TOLERANCE = 2
JOBOBJECT_RATE_CONTROL_TOLERANCE_ToleranceHigh: JOBOBJECT_RATE_CONTROL_TOLERANCE = 3
JOBOBJECT_RATE_CONTROL_TOLERANCE_INTERVAL = Int32
JOBOBJECT_RATE_CONTROL_TOLERANCE_INTERVAL_ToleranceIntervalShort: JOBOBJECT_RATE_CONTROL_TOLERANCE_INTERVAL = 1
JOBOBJECT_RATE_CONTROL_TOLERANCE_INTERVAL_ToleranceIntervalMedium: JOBOBJECT_RATE_CONTROL_TOLERANCE_INTERVAL = 2
JOBOBJECT_RATE_CONTROL_TOLERANCE_INTERVAL_ToleranceIntervalLong: JOBOBJECT_RATE_CONTROL_TOLERANCE_INTERVAL = 3
class JOBOBJECT_SECURITY_LIMIT_INFORMATION(EasyCastStructure):
    SecurityLimitFlags: Windows.Win32.System.JobObjects.JOB_OBJECT_SECURITY
    JobToken: Windows.Win32.Foundation.HANDLE
    SidsToDisable: POINTER(Windows.Win32.Security.TOKEN_GROUPS_head)
    PrivilegesToDelete: POINTER(Windows.Win32.Security.TOKEN_PRIVILEGES_head)
    RestrictedSids: POINTER(Windows.Win32.Security.TOKEN_GROUPS_head)
JOB_OBJECT_CPU_RATE_CONTROL = UInt32
JOB_OBJECT_CPU_RATE_CONTROL_ENABLE: JOB_OBJECT_CPU_RATE_CONTROL = 1
JOB_OBJECT_CPU_RATE_CONTROL_WEIGHT_BASED: JOB_OBJECT_CPU_RATE_CONTROL = 2
JOB_OBJECT_CPU_RATE_CONTROL_HARD_CAP: JOB_OBJECT_CPU_RATE_CONTROL = 4
JOB_OBJECT_CPU_RATE_CONTROL_NOTIFY: JOB_OBJECT_CPU_RATE_CONTROL = 8
JOB_OBJECT_CPU_RATE_CONTROL_MIN_MAX_RATE: JOB_OBJECT_CPU_RATE_CONTROL = 16
JOB_OBJECT_CPU_RATE_CONTROL_VALID_FLAGS: JOB_OBJECT_CPU_RATE_CONTROL = 31
JOB_OBJECT_IO_RATE_CONTROL_FLAGS = Int32
JOB_OBJECT_IO_RATE_CONTROL_ENABLE: JOB_OBJECT_IO_RATE_CONTROL_FLAGS = 1
JOB_OBJECT_IO_RATE_CONTROL_STANDALONE_VOLUME: JOB_OBJECT_IO_RATE_CONTROL_FLAGS = 2
JOB_OBJECT_IO_RATE_CONTROL_FORCE_UNIT_ACCESS_ALL: JOB_OBJECT_IO_RATE_CONTROL_FLAGS = 4
JOB_OBJECT_IO_RATE_CONTROL_FORCE_UNIT_ACCESS_ON_SOFT_CAP: JOB_OBJECT_IO_RATE_CONTROL_FLAGS = 8
JOB_OBJECT_IO_RATE_CONTROL_VALID_FLAGS: JOB_OBJECT_IO_RATE_CONTROL_FLAGS = 15
JOB_OBJECT_LIMIT = UInt32
JOB_OBJECT_LIMIT_WORKINGSET: JOB_OBJECT_LIMIT = 1
JOB_OBJECT_LIMIT_PROCESS_TIME: JOB_OBJECT_LIMIT = 2
JOB_OBJECT_LIMIT_JOB_TIME: JOB_OBJECT_LIMIT = 4
JOB_OBJECT_LIMIT_ACTIVE_PROCESS: JOB_OBJECT_LIMIT = 8
JOB_OBJECT_LIMIT_AFFINITY: JOB_OBJECT_LIMIT = 16
JOB_OBJECT_LIMIT_PRIORITY_CLASS: JOB_OBJECT_LIMIT = 32
JOB_OBJECT_LIMIT_PRESERVE_JOB_TIME: JOB_OBJECT_LIMIT = 64
JOB_OBJECT_LIMIT_SCHEDULING_CLASS: JOB_OBJECT_LIMIT = 128
JOB_OBJECT_LIMIT_PROCESS_MEMORY: JOB_OBJECT_LIMIT = 256
JOB_OBJECT_LIMIT_JOB_MEMORY: JOB_OBJECT_LIMIT = 512
JOB_OBJECT_LIMIT_JOB_MEMORY_HIGH: JOB_OBJECT_LIMIT = 512
JOB_OBJECT_LIMIT_DIE_ON_UNHANDLED_EXCEPTION: JOB_OBJECT_LIMIT = 1024
JOB_OBJECT_LIMIT_BREAKAWAY_OK: JOB_OBJECT_LIMIT = 2048
JOB_OBJECT_LIMIT_SILENT_BREAKAWAY_OK: JOB_OBJECT_LIMIT = 4096
JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE: JOB_OBJECT_LIMIT = 8192
JOB_OBJECT_LIMIT_SUBSET_AFFINITY: JOB_OBJECT_LIMIT = 16384
JOB_OBJECT_LIMIT_JOB_MEMORY_LOW: JOB_OBJECT_LIMIT = 32768
JOB_OBJECT_LIMIT_JOB_READ_BYTES: JOB_OBJECT_LIMIT = 65536
JOB_OBJECT_LIMIT_JOB_WRITE_BYTES: JOB_OBJECT_LIMIT = 131072
JOB_OBJECT_LIMIT_RATE_CONTROL: JOB_OBJECT_LIMIT = 262144
JOB_OBJECT_LIMIT_CPU_RATE_CONTROL: JOB_OBJECT_LIMIT = 262144
JOB_OBJECT_LIMIT_IO_RATE_CONTROL: JOB_OBJECT_LIMIT = 524288
JOB_OBJECT_LIMIT_NET_RATE_CONTROL: JOB_OBJECT_LIMIT = 1048576
JOB_OBJECT_LIMIT_VALID_FLAGS: JOB_OBJECT_LIMIT = 524287
JOB_OBJECT_BASIC_LIMIT_VALID_FLAGS: JOB_OBJECT_LIMIT = 255
JOB_OBJECT_EXTENDED_LIMIT_VALID_FLAGS: JOB_OBJECT_LIMIT = 32767
JOB_OBJECT_NOTIFICATION_LIMIT_VALID_FLAGS: JOB_OBJECT_LIMIT = 2064900
JOB_OBJECT_NET_RATE_CONTROL_FLAGS = Int32
JOB_OBJECT_NET_RATE_CONTROL_ENABLE: JOB_OBJECT_NET_RATE_CONTROL_FLAGS = 1
JOB_OBJECT_NET_RATE_CONTROL_MAX_BANDWIDTH: JOB_OBJECT_NET_RATE_CONTROL_FLAGS = 2
JOB_OBJECT_NET_RATE_CONTROL_DSCP_TAG: JOB_OBJECT_NET_RATE_CONTROL_FLAGS = 4
JOB_OBJECT_NET_RATE_CONTROL_VALID_FLAGS: JOB_OBJECT_NET_RATE_CONTROL_FLAGS = 7
JOB_OBJECT_SECURITY = UInt32
JOB_OBJECT_SECURITY_NO_ADMIN: JOB_OBJECT_SECURITY = 1
JOB_OBJECT_SECURITY_RESTRICTED_TOKEN: JOB_OBJECT_SECURITY = 2
JOB_OBJECT_SECURITY_ONLY_TOKEN: JOB_OBJECT_SECURITY = 4
JOB_OBJECT_SECURITY_FILTER_TOKENS: JOB_OBJECT_SECURITY = 8
JOB_OBJECT_SECURITY_VALID_FLAGS: JOB_OBJECT_SECURITY = 15
JOB_OBJECT_TERMINATE_AT_END_ACTION = UInt32
JOB_OBJECT_TERMINATE_AT_END_OF_JOB: JOB_OBJECT_TERMINATE_AT_END_ACTION = 0
JOB_OBJECT_POST_AT_END_OF_JOB: JOB_OBJECT_TERMINATE_AT_END_ACTION = 1
JOB_OBJECT_UILIMIT = UInt32
JOB_OBJECT_UILIMIT_NONE: JOB_OBJECT_UILIMIT = 0
JOB_OBJECT_UILIMIT_HANDLES: JOB_OBJECT_UILIMIT = 1
JOB_OBJECT_UILIMIT_READCLIPBOARD: JOB_OBJECT_UILIMIT = 2
JOB_OBJECT_UILIMIT_WRITECLIPBOARD: JOB_OBJECT_UILIMIT = 4
JOB_OBJECT_UILIMIT_SYSTEMPARAMETERS: JOB_OBJECT_UILIMIT = 8
JOB_OBJECT_UILIMIT_DISPLAYSETTINGS: JOB_OBJECT_UILIMIT = 16
JOB_OBJECT_UILIMIT_GLOBALATOMS: JOB_OBJECT_UILIMIT = 32
JOB_OBJECT_UILIMIT_DESKTOP: JOB_OBJECT_UILIMIT = 64
JOB_OBJECT_UILIMIT_EXITWINDOWS: JOB_OBJECT_UILIMIT = 128
class JOB_SET_ARRAY(EasyCastStructure):
    JobHandle: Windows.Win32.Foundation.HANDLE
    MemberLevel: UInt32
    Flags: UInt32
make_head(_module, 'JOBOBJECT_ASSOCIATE_COMPLETION_PORT')
make_head(_module, 'JOBOBJECT_BASIC_ACCOUNTING_INFORMATION')
make_head(_module, 'JOBOBJECT_BASIC_AND_IO_ACCOUNTING_INFORMATION')
make_head(_module, 'JOBOBJECT_BASIC_LIMIT_INFORMATION')
make_head(_module, 'JOBOBJECT_BASIC_PROCESS_ID_LIST')
make_head(_module, 'JOBOBJECT_BASIC_UI_RESTRICTIONS')
make_head(_module, 'JOBOBJECT_CPU_RATE_CONTROL_INFORMATION')
make_head(_module, 'JOBOBJECT_END_OF_JOB_TIME_INFORMATION')
make_head(_module, 'JOBOBJECT_EXTENDED_LIMIT_INFORMATION')
make_head(_module, 'JOBOBJECT_IO_ATTRIBUTION_INFORMATION')
make_head(_module, 'JOBOBJECT_IO_ATTRIBUTION_STATS')
make_head(_module, 'JOBOBJECT_IO_RATE_CONTROL_INFORMATION')
make_head(_module, 'JOBOBJECT_IO_RATE_CONTROL_INFORMATION_NATIVE_V1')
make_head(_module, 'JOBOBJECT_IO_RATE_CONTROL_INFORMATION_NATIVE_V2')
make_head(_module, 'JOBOBJECT_IO_RATE_CONTROL_INFORMATION_NATIVE_V3')
make_head(_module, 'JOBOBJECT_JOBSET_INFORMATION')
make_head(_module, 'JOBOBJECT_LIMIT_VIOLATION_INFORMATION')
make_head(_module, 'JOBOBJECT_LIMIT_VIOLATION_INFORMATION_2')
make_head(_module, 'JOBOBJECT_NET_RATE_CONTROL_INFORMATION')
make_head(_module, 'JOBOBJECT_NOTIFICATION_LIMIT_INFORMATION')
make_head(_module, 'JOBOBJECT_NOTIFICATION_LIMIT_INFORMATION_2')
make_head(_module, 'JOBOBJECT_SECURITY_LIMIT_INFORMATION')
make_head(_module, 'JOB_SET_ARRAY')
