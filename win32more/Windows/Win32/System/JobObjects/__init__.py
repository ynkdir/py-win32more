from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Security
import win32more.Windows.Win32.System.JobObjects
import win32more.Windows.Win32.System.Threading
@winfunctype('KERNEL32.dll')
def IsProcessInJob(ProcessHandle: win32more.Windows.Win32.Foundation.HANDLE, JobHandle: win32more.Windows.Win32.Foundation.HANDLE, Result: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateJobObjectW(lpJobAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), lpName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
CreateJobObject = UnicodeAlias('CreateJobObjectW')
@winfunctype('KERNEL32.dll')
def FreeMemoryJobObject(Buffer: VoidPtr) -> Void: ...
@winfunctype('KERNEL32.dll')
def OpenJobObjectW(dwDesiredAccess: UInt32, bInheritHandle: win32more.Windows.Win32.Foundation.BOOL, lpName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
OpenJobObject = UnicodeAlias('OpenJobObjectW')
@winfunctype('KERNEL32.dll')
def AssignProcessToJobObject(hJob: win32more.Windows.Win32.Foundation.HANDLE, hProcess: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def TerminateJobObject(hJob: win32more.Windows.Win32.Foundation.HANDLE, uExitCode: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetInformationJobObject(hJob: win32more.Windows.Win32.Foundation.HANDLE, JobObjectInformationClass: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS, lpJobObjectInformation: VoidPtr, cbJobObjectInformationLength: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetIoRateControlInformationJobObject(hJob: win32more.Windows.Win32.Foundation.HANDLE, IoRateControlInfo: POINTER(win32more.Windows.Win32.System.JobObjects.JOBOBJECT_IO_RATE_CONTROL_INFORMATION)) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def QueryInformationJobObject(hJob: win32more.Windows.Win32.Foundation.HANDLE, JobObjectInformationClass: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS, lpJobObjectInformation: VoidPtr, cbJobObjectInformationLength: UInt32, lpReturnLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def QueryIoRateControlInformationJobObject(hJob: win32more.Windows.Win32.Foundation.HANDLE, VolumeName: win32more.Windows.Win32.Foundation.PWSTR, InfoBlocks: POINTER(POINTER(win32more.Windows.Win32.System.JobObjects.JOBOBJECT_IO_RATE_CONTROL_INFORMATION)), InfoBlockCount: POINTER(UInt32)) -> UInt32: ...
@winfunctype('USER32.dll')
def UserHandleGrantAccess(hUserHandle: win32more.Windows.Win32.Foundation.HANDLE, hJob: win32more.Windows.Win32.Foundation.HANDLE, bGrant: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateJobObjectA(lpJobAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), lpName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def OpenJobObjectA(dwDesiredAccess: UInt32, bInheritHandle: win32more.Windows.Win32.Foundation.BOOL, lpName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def CreateJobSet(NumJob: UInt32, UserJobSet: POINTER(win32more.Windows.Win32.System.JobObjects.JOB_SET_ARRAY), Flags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
JOBOBJECTINFOCLASS = Int32
JobObjectBasicAccountingInformation: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 1
JobObjectBasicLimitInformation: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 2
JobObjectBasicProcessIdList: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 3
JobObjectBasicUIRestrictions: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 4
JobObjectSecurityLimitInformation: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 5
JobObjectEndOfJobTimeInformation: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 6
JobObjectAssociateCompletionPortInformation: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 7
JobObjectBasicAndIoAccountingInformation: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 8
JobObjectExtendedLimitInformation: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 9
JobObjectJobSetInformation: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 10
JobObjectGroupInformation: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 11
JobObjectNotificationLimitInformation: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 12
JobObjectLimitViolationInformation: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 13
JobObjectGroupInformationEx: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 14
JobObjectCpuRateControlInformation: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 15
JobObjectCompletionFilter: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 16
JobObjectCompletionCounter: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 17
JobObjectReserved1Information: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 18
JobObjectReserved2Information: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 19
JobObjectReserved3Information: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 20
JobObjectReserved4Information: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 21
JobObjectReserved5Information: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 22
JobObjectReserved6Information: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 23
JobObjectReserved7Information: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 24
JobObjectReserved8Information: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 25
JobObjectReserved9Information: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 26
JobObjectReserved10Information: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 27
JobObjectReserved11Information: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 28
JobObjectReserved12Information: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 29
JobObjectReserved13Information: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 30
JobObjectReserved14Information: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 31
JobObjectNetRateControlInformation: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 32
JobObjectNotificationLimitInformation2: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 33
JobObjectLimitViolationInformation2: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 34
JobObjectCreateSilo: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 35
JobObjectSiloBasicInformation: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 36
JobObjectReserved15Information: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 37
JobObjectReserved16Information: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 38
JobObjectReserved17Information: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 39
JobObjectReserved18Information: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 40
JobObjectReserved19Information: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 41
JobObjectReserved20Information: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 42
JobObjectReserved21Information: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 43
JobObjectReserved22Information: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 44
JobObjectReserved23Information: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 45
JobObjectReserved24Information: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 46
JobObjectReserved25Information: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 47
JobObjectReserved26Information: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 48
JobObjectReserved27Information: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 49
MaxJobObjectInfoClass: win32more.Windows.Win32.System.JobObjects.JOBOBJECTINFOCLASS = 50
class JOBOBJECT_ASSOCIATE_COMPLETION_PORT(Structure):
    CompletionKey: VoidPtr
    CompletionPort: win32more.Windows.Win32.Foundation.HANDLE
class JOBOBJECT_BASIC_ACCOUNTING_INFORMATION(Structure):
    TotalUserTime: Int64
    TotalKernelTime: Int64
    ThisPeriodTotalUserTime: Int64
    ThisPeriodTotalKernelTime: Int64
    TotalPageFaultCount: UInt32
    TotalProcesses: UInt32
    ActiveProcesses: UInt32
    TotalTerminatedProcesses: UInt32
class JOBOBJECT_BASIC_AND_IO_ACCOUNTING_INFORMATION(Structure):
    BasicInfo: win32more.Windows.Win32.System.JobObjects.JOBOBJECT_BASIC_ACCOUNTING_INFORMATION
    IoInfo: win32more.Windows.Win32.System.Threading.IO_COUNTERS
class JOBOBJECT_BASIC_LIMIT_INFORMATION(Structure):
    PerProcessUserTimeLimit: Int64
    PerJobUserTimeLimit: Int64
    LimitFlags: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_LIMIT
    MinimumWorkingSetSize: UIntPtr
    MaximumWorkingSetSize: UIntPtr
    ActiveProcessLimit: UInt32
    Affinity: UIntPtr
    PriorityClass: UInt32
    SchedulingClass: UInt32
class JOBOBJECT_BASIC_PROCESS_ID_LIST(Structure):
    NumberOfAssignedProcesses: UInt32
    NumberOfProcessIdsInList: UInt32
    ProcessIdList: UIntPtr * 1
class JOBOBJECT_BASIC_UI_RESTRICTIONS(Structure):
    UIRestrictionsClass: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_UILIMIT
class JOBOBJECT_CPU_RATE_CONTROL_INFORMATION(Structure):
    ControlFlags: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_CPU_RATE_CONTROL
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        CpuRate: UInt32
        Weight: UInt32
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            MinRate: UInt16
            MaxRate: UInt16
class JOBOBJECT_END_OF_JOB_TIME_INFORMATION(Structure):
    EndOfJobTimeAction: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_TERMINATE_AT_END_ACTION
class JOBOBJECT_EXTENDED_LIMIT_INFORMATION(Structure):
    BasicLimitInformation: win32more.Windows.Win32.System.JobObjects.JOBOBJECT_BASIC_LIMIT_INFORMATION
    IoInfo: win32more.Windows.Win32.System.Threading.IO_COUNTERS
    ProcessMemoryLimit: UIntPtr
    JobMemoryLimit: UIntPtr
    PeakProcessMemoryUsed: UIntPtr
    PeakJobMemoryUsed: UIntPtr
JOBOBJECT_IO_ATTRIBUTION_CONTROL_FLAGS = Int32
JOBOBJECT_IO_ATTRIBUTION_CONTROL_ENABLE: win32more.Windows.Win32.System.JobObjects.JOBOBJECT_IO_ATTRIBUTION_CONTROL_FLAGS = 1
JOBOBJECT_IO_ATTRIBUTION_CONTROL_DISABLE: win32more.Windows.Win32.System.JobObjects.JOBOBJECT_IO_ATTRIBUTION_CONTROL_FLAGS = 2
JOBOBJECT_IO_ATTRIBUTION_CONTROL_VALID_FLAGS: win32more.Windows.Win32.System.JobObjects.JOBOBJECT_IO_ATTRIBUTION_CONTROL_FLAGS = 3
class JOBOBJECT_IO_ATTRIBUTION_INFORMATION(Structure):
    ControlFlags: UInt32
    ReadStats: win32more.Windows.Win32.System.JobObjects.JOBOBJECT_IO_ATTRIBUTION_STATS
    WriteStats: win32more.Windows.Win32.System.JobObjects.JOBOBJECT_IO_ATTRIBUTION_STATS
class JOBOBJECT_IO_ATTRIBUTION_STATS(Structure):
    IoCount: UIntPtr
    TotalNonOverlappedQueueTime: UInt64
    TotalNonOverlappedServiceTime: UInt64
    TotalSize: UInt64
class JOBOBJECT_IO_RATE_CONTROL_INFORMATION(Structure):
    MaxIops: Int64
    MaxBandwidth: Int64
    ReservationIops: Int64
    VolumeName: win32more.Windows.Win32.Foundation.PWSTR
    BaseIoSize: UInt32
    ControlFlags: UInt32
class JOBOBJECT_IO_RATE_CONTROL_INFORMATION_NATIVE_V1(Structure):
    MaxIops: Int64
    MaxBandwidth: Int64
    ReservationIops: Int64
    VolumeName: win32more.Windows.Win32.Foundation.PWSTR
    BaseIoSize: UInt32
    ControlFlags: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_IO_RATE_CONTROL_FLAGS
    VolumeNameLength: UInt16
class JOBOBJECT_IO_RATE_CONTROL_INFORMATION_NATIVE_V2(Structure):
    MaxIops: Int64
    MaxBandwidth: Int64
    ReservationIops: Int64
    VolumeName: win32more.Windows.Win32.Foundation.PWSTR
    BaseIoSize: UInt32
    ControlFlags: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_IO_RATE_CONTROL_FLAGS
    VolumeNameLength: UInt16
    CriticalReservationIops: Int64
    ReservationBandwidth: Int64
    CriticalReservationBandwidth: Int64
    MaxTimePercent: Int64
    ReservationTimePercent: Int64
    CriticalReservationTimePercent: Int64
class JOBOBJECT_IO_RATE_CONTROL_INFORMATION_NATIVE_V3(Structure):
    MaxIops: Int64
    MaxBandwidth: Int64
    ReservationIops: Int64
    VolumeName: win32more.Windows.Win32.Foundation.PWSTR
    BaseIoSize: UInt32
    ControlFlags: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_IO_RATE_CONTROL_FLAGS
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
class JOBOBJECT_JOBSET_INFORMATION(Structure):
    MemberLevel: UInt32
class JOBOBJECT_LIMIT_VIOLATION_INFORMATION(Structure):
    LimitFlags: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_LIMIT
    ViolationLimitFlags: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_LIMIT
    IoReadBytes: UInt64
    IoReadBytesLimit: UInt64
    IoWriteBytes: UInt64
    IoWriteBytesLimit: UInt64
    PerJobUserTime: Int64
    PerJobUserTimeLimit: Int64
    JobMemory: UInt64
    JobMemoryLimit: UInt64
    RateControlTolerance: win32more.Windows.Win32.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE
    RateControlToleranceLimit: win32more.Windows.Win32.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE
class JOBOBJECT_LIMIT_VIOLATION_INFORMATION_2(Structure):
    LimitFlags: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_LIMIT
    ViolationLimitFlags: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_LIMIT
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
    IoRateControlTolerance: win32more.Windows.Win32.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE
    IoRateControlToleranceLimit: win32more.Windows.Win32.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE
    NetRateControlTolerance: win32more.Windows.Win32.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE
    NetRateControlToleranceLimit: win32more.Windows.Win32.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE
    class _Anonymous1_e__Union(Union):
        JobHighMemoryLimit: UInt64
        JobMemoryLimit: UInt64
    class _Anonymous2_e__Union(Union):
        RateControlTolerance: win32more.Windows.Win32.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE
        CpuRateControlTolerance: win32more.Windows.Win32.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE
    class _Anonymous3_e__Union(Union):
        RateControlToleranceLimit: win32more.Windows.Win32.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE
        CpuRateControlToleranceLimit: win32more.Windows.Win32.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE
class JOBOBJECT_NET_RATE_CONTROL_INFORMATION(Structure):
    MaxBandwidth: UInt64
    ControlFlags: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_NET_RATE_CONTROL_FLAGS
    DscpTag: Byte
class JOBOBJECT_NOTIFICATION_LIMIT_INFORMATION(Structure):
    IoReadBytesLimit: UInt64
    IoWriteBytesLimit: UInt64
    PerJobUserTimeLimit: Int64
    JobMemoryLimit: UInt64
    RateControlTolerance: win32more.Windows.Win32.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE
    RateControlToleranceInterval: win32more.Windows.Win32.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE_INTERVAL
    LimitFlags: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_LIMIT
class JOBOBJECT_NOTIFICATION_LIMIT_INFORMATION_2(Structure):
    IoReadBytesLimit: UInt64
    IoWriteBytesLimit: UInt64
    PerJobUserTimeLimit: Int64
    Anonymous1: _Anonymous1_e__Union
    Anonymous2: _Anonymous2_e__Union
    Anonymous3: _Anonymous3_e__Union
    LimitFlags: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_LIMIT
    IoRateControlTolerance: win32more.Windows.Win32.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE
    JobLowMemoryLimit: UInt64
    IoRateControlToleranceInterval: win32more.Windows.Win32.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE_INTERVAL
    NetRateControlTolerance: win32more.Windows.Win32.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE
    NetRateControlToleranceInterval: win32more.Windows.Win32.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE_INTERVAL
    class _Anonymous1_e__Union(Union):
        JobHighMemoryLimit: UInt64
        JobMemoryLimit: UInt64
    class _Anonymous2_e__Union(Union):
        RateControlTolerance: win32more.Windows.Win32.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE
        CpuRateControlTolerance: win32more.Windows.Win32.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE
    class _Anonymous3_e__Union(Union):
        RateControlToleranceInterval: win32more.Windows.Win32.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE_INTERVAL
        CpuRateControlToleranceInterval: win32more.Windows.Win32.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE_INTERVAL
JOBOBJECT_RATE_CONTROL_TOLERANCE = Int32
ToleranceLow: win32more.Windows.Win32.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE = 1
ToleranceMedium: win32more.Windows.Win32.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE = 2
ToleranceHigh: win32more.Windows.Win32.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE = 3
JOBOBJECT_RATE_CONTROL_TOLERANCE_INTERVAL = Int32
ToleranceIntervalShort: win32more.Windows.Win32.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE_INTERVAL = 1
ToleranceIntervalMedium: win32more.Windows.Win32.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE_INTERVAL = 2
ToleranceIntervalLong: win32more.Windows.Win32.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE_INTERVAL = 3
class JOBOBJECT_SECURITY_LIMIT_INFORMATION(Structure):
    SecurityLimitFlags: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_SECURITY
    JobToken: win32more.Windows.Win32.Foundation.HANDLE
    SidsToDisable: POINTER(win32more.Windows.Win32.Security.TOKEN_GROUPS)
    PrivilegesToDelete: POINTER(win32more.Windows.Win32.Security.TOKEN_PRIVILEGES)
    RestrictedSids: POINTER(win32more.Windows.Win32.Security.TOKEN_GROUPS)
JOB_OBJECT_CPU_RATE_CONTROL = UInt32
JOB_OBJECT_CPU_RATE_CONTROL_ENABLE: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_CPU_RATE_CONTROL = 1
JOB_OBJECT_CPU_RATE_CONTROL_WEIGHT_BASED: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_CPU_RATE_CONTROL = 2
JOB_OBJECT_CPU_RATE_CONTROL_HARD_CAP: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_CPU_RATE_CONTROL = 4
JOB_OBJECT_CPU_RATE_CONTROL_NOTIFY: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_CPU_RATE_CONTROL = 8
JOB_OBJECT_CPU_RATE_CONTROL_MIN_MAX_RATE: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_CPU_RATE_CONTROL = 16
JOB_OBJECT_CPU_RATE_CONTROL_VALID_FLAGS: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_CPU_RATE_CONTROL = 31
JOB_OBJECT_IO_RATE_CONTROL_FLAGS = Int32
JOB_OBJECT_IO_RATE_CONTROL_ENABLE: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_IO_RATE_CONTROL_FLAGS = 1
JOB_OBJECT_IO_RATE_CONTROL_STANDALONE_VOLUME: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_IO_RATE_CONTROL_FLAGS = 2
JOB_OBJECT_IO_RATE_CONTROL_FORCE_UNIT_ACCESS_ALL: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_IO_RATE_CONTROL_FLAGS = 4
JOB_OBJECT_IO_RATE_CONTROL_FORCE_UNIT_ACCESS_ON_SOFT_CAP: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_IO_RATE_CONTROL_FLAGS = 8
JOB_OBJECT_IO_RATE_CONTROL_VALID_FLAGS: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_IO_RATE_CONTROL_FLAGS = 15
JOB_OBJECT_LIMIT = UInt32
JOB_OBJECT_LIMIT_WORKINGSET: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_LIMIT = 1
JOB_OBJECT_LIMIT_PROCESS_TIME: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_LIMIT = 2
JOB_OBJECT_LIMIT_JOB_TIME: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_LIMIT = 4
JOB_OBJECT_LIMIT_ACTIVE_PROCESS: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_LIMIT = 8
JOB_OBJECT_LIMIT_AFFINITY: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_LIMIT = 16
JOB_OBJECT_LIMIT_PRIORITY_CLASS: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_LIMIT = 32
JOB_OBJECT_LIMIT_PRESERVE_JOB_TIME: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_LIMIT = 64
JOB_OBJECT_LIMIT_SCHEDULING_CLASS: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_LIMIT = 128
JOB_OBJECT_LIMIT_PROCESS_MEMORY: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_LIMIT = 256
JOB_OBJECT_LIMIT_JOB_MEMORY: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_LIMIT = 512
JOB_OBJECT_LIMIT_JOB_MEMORY_HIGH: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_LIMIT = 512
JOB_OBJECT_LIMIT_DIE_ON_UNHANDLED_EXCEPTION: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_LIMIT = 1024
JOB_OBJECT_LIMIT_BREAKAWAY_OK: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_LIMIT = 2048
JOB_OBJECT_LIMIT_SILENT_BREAKAWAY_OK: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_LIMIT = 4096
JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_LIMIT = 8192
JOB_OBJECT_LIMIT_SUBSET_AFFINITY: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_LIMIT = 16384
JOB_OBJECT_LIMIT_JOB_MEMORY_LOW: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_LIMIT = 32768
JOB_OBJECT_LIMIT_JOB_READ_BYTES: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_LIMIT = 65536
JOB_OBJECT_LIMIT_JOB_WRITE_BYTES: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_LIMIT = 131072
JOB_OBJECT_LIMIT_RATE_CONTROL: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_LIMIT = 262144
JOB_OBJECT_LIMIT_CPU_RATE_CONTROL: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_LIMIT = 262144
JOB_OBJECT_LIMIT_IO_RATE_CONTROL: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_LIMIT = 524288
JOB_OBJECT_LIMIT_NET_RATE_CONTROL: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_LIMIT = 1048576
JOB_OBJECT_LIMIT_VALID_FLAGS: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_LIMIT = 524287
JOB_OBJECT_BASIC_LIMIT_VALID_FLAGS: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_LIMIT = 255
JOB_OBJECT_EXTENDED_LIMIT_VALID_FLAGS: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_LIMIT = 32767
JOB_OBJECT_NOTIFICATION_LIMIT_VALID_FLAGS: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_LIMIT = 2064900
JOB_OBJECT_NET_RATE_CONTROL_FLAGS = Int32
JOB_OBJECT_NET_RATE_CONTROL_ENABLE: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_NET_RATE_CONTROL_FLAGS = 1
JOB_OBJECT_NET_RATE_CONTROL_MAX_BANDWIDTH: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_NET_RATE_CONTROL_FLAGS = 2
JOB_OBJECT_NET_RATE_CONTROL_DSCP_TAG: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_NET_RATE_CONTROL_FLAGS = 4
JOB_OBJECT_NET_RATE_CONTROL_VALID_FLAGS: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_NET_RATE_CONTROL_FLAGS = 7
JOB_OBJECT_SECURITY = UInt32
JOB_OBJECT_SECURITY_NO_ADMIN: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_SECURITY = 1
JOB_OBJECT_SECURITY_RESTRICTED_TOKEN: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_SECURITY = 2
JOB_OBJECT_SECURITY_ONLY_TOKEN: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_SECURITY = 4
JOB_OBJECT_SECURITY_FILTER_TOKENS: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_SECURITY = 8
JOB_OBJECT_SECURITY_VALID_FLAGS: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_SECURITY = 15
JOB_OBJECT_TERMINATE_AT_END_ACTION = UInt32
JOB_OBJECT_TERMINATE_AT_END_OF_JOB: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_TERMINATE_AT_END_ACTION = 0
JOB_OBJECT_POST_AT_END_OF_JOB: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_TERMINATE_AT_END_ACTION = 1
JOB_OBJECT_UILIMIT = UInt32
JOB_OBJECT_UILIMIT_NONE: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_UILIMIT = 0
JOB_OBJECT_UILIMIT_HANDLES: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_UILIMIT = 1
JOB_OBJECT_UILIMIT_READCLIPBOARD: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_UILIMIT = 2
JOB_OBJECT_UILIMIT_WRITECLIPBOARD: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_UILIMIT = 4
JOB_OBJECT_UILIMIT_SYSTEMPARAMETERS: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_UILIMIT = 8
JOB_OBJECT_UILIMIT_DISPLAYSETTINGS: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_UILIMIT = 16
JOB_OBJECT_UILIMIT_GLOBALATOMS: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_UILIMIT = 32
JOB_OBJECT_UILIMIT_DESKTOP: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_UILIMIT = 64
JOB_OBJECT_UILIMIT_EXITWINDOWS: win32more.Windows.Win32.System.JobObjects.JOB_OBJECT_UILIMIT = 128
class JOB_SET_ARRAY(Structure):
    JobHandle: win32more.Windows.Win32.Foundation.HANDLE
    MemberLevel: UInt32
    Flags: UInt32


make_ready(__name__)
