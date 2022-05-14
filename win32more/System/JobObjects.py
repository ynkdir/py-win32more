from win32more import *
import win32more.System.JobObjects
import win32more.Foundation
import win32more.Security
import win32more.System.Threading

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.System.JobObjects, name, eval(f"_define_{name}()"))
    return getattr(win32more.System.JobObjects, name)
JOB_OBJECT_LIMIT = UInt32
JOB_OBJECT_LIMIT_WORKINGSET = 1
JOB_OBJECT_LIMIT_PROCESS_TIME = 2
JOB_OBJECT_LIMIT_JOB_TIME = 4
JOB_OBJECT_LIMIT_ACTIVE_PROCESS = 8
JOB_OBJECT_LIMIT_AFFINITY = 16
JOB_OBJECT_LIMIT_PRIORITY_CLASS = 32
JOB_OBJECT_LIMIT_PRESERVE_JOB_TIME = 64
JOB_OBJECT_LIMIT_SCHEDULING_CLASS = 128
JOB_OBJECT_LIMIT_PROCESS_MEMORY = 256
JOB_OBJECT_LIMIT_JOB_MEMORY = 512
JOB_OBJECT_LIMIT_JOB_MEMORY_HIGH = 512
JOB_OBJECT_LIMIT_DIE_ON_UNHANDLED_EXCEPTION = 1024
JOB_OBJECT_LIMIT_BREAKAWAY_OK = 2048
JOB_OBJECT_LIMIT_SILENT_BREAKAWAY_OK = 4096
JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE = 8192
JOB_OBJECT_LIMIT_SUBSET_AFFINITY = 16384
JOB_OBJECT_LIMIT_JOB_MEMORY_LOW = 32768
JOB_OBJECT_LIMIT_JOB_READ_BYTES = 65536
JOB_OBJECT_LIMIT_JOB_WRITE_BYTES = 131072
JOB_OBJECT_LIMIT_RATE_CONTROL = 262144
JOB_OBJECT_LIMIT_CPU_RATE_CONTROL = 262144
JOB_OBJECT_LIMIT_IO_RATE_CONTROL = 524288
JOB_OBJECT_LIMIT_NET_RATE_CONTROL = 1048576
JOB_OBJECT_LIMIT_VALID_FLAGS = 524287
JOB_OBJECT_BASIC_LIMIT_VALID_FLAGS = 255
JOB_OBJECT_EXTENDED_LIMIT_VALID_FLAGS = 32767
JOB_OBJECT_NOTIFICATION_LIMIT_VALID_FLAGS = 2064900
JOB_OBJECT_UILIMIT = UInt32
JOB_OBJECT_UILIMIT_NONE = 0
JOB_OBJECT_UILIMIT_HANDLES = 1
JOB_OBJECT_UILIMIT_READCLIPBOARD = 2
JOB_OBJECT_UILIMIT_WRITECLIPBOARD = 4
JOB_OBJECT_UILIMIT_SYSTEMPARAMETERS = 8
JOB_OBJECT_UILIMIT_DISPLAYSETTINGS = 16
JOB_OBJECT_UILIMIT_GLOBALATOMS = 32
JOB_OBJECT_UILIMIT_DESKTOP = 64
JOB_OBJECT_UILIMIT_EXITWINDOWS = 128
JOB_OBJECT_SECURITY = UInt32
JOB_OBJECT_SECURITY_NO_ADMIN = 1
JOB_OBJECT_SECURITY_RESTRICTED_TOKEN = 2
JOB_OBJECT_SECURITY_ONLY_TOKEN = 4
JOB_OBJECT_SECURITY_FILTER_TOKENS = 8
JOB_OBJECT_SECURITY_VALID_FLAGS = 15
JOB_OBJECT_CPU_RATE_CONTROL = UInt32
JOB_OBJECT_CPU_RATE_CONTROL_ENABLE = 1
JOB_OBJECT_CPU_RATE_CONTROL_WEIGHT_BASED = 2
JOB_OBJECT_CPU_RATE_CONTROL_HARD_CAP = 4
JOB_OBJECT_CPU_RATE_CONTROL_NOTIFY = 8
JOB_OBJECT__CPU_RATE_CONTROL_MIN_MAX_RATE = 16
JOB_OBJECT_TERMINATE_AT_END_ACTION = UInt32
JOB_OBJECT_TERMINATE_AT_END_OF_JOB = 0
JOB_OBJECT_POST_AT_END_OF_JOB = 1
def _define_JOBOBJECT_IO_RATE_CONTROL_INFORMATION_head():
    class JOBOBJECT_IO_RATE_CONTROL_INFORMATION(Structure):
        pass
    return JOBOBJECT_IO_RATE_CONTROL_INFORMATION
def _define_JOBOBJECT_IO_RATE_CONTROL_INFORMATION():
    JOBOBJECT_IO_RATE_CONTROL_INFORMATION = win32more.System.JobObjects.JOBOBJECT_IO_RATE_CONTROL_INFORMATION_head
    JOBOBJECT_IO_RATE_CONTROL_INFORMATION._fields_ = [
        ("MaxIops", Int64),
        ("MaxBandwidth", Int64),
        ("ReservationIops", Int64),
        ("VolumeName", win32more.Foundation.PWSTR),
        ("BaseIoSize", UInt32),
        ("ControlFlags", win32more.System.JobObjects.JOB_OBJECT_IO_RATE_CONTROL_FLAGS),
    ]
    return JOBOBJECT_IO_RATE_CONTROL_INFORMATION
def _define_JOB_SET_ARRAY_head():
    class JOB_SET_ARRAY(Structure):
        pass
    return JOB_SET_ARRAY
def _define_JOB_SET_ARRAY():
    JOB_SET_ARRAY = win32more.System.JobObjects.JOB_SET_ARRAY_head
    JOB_SET_ARRAY._fields_ = [
        ("JobHandle", win32more.Foundation.HANDLE),
        ("MemberLevel", UInt32),
        ("Flags", UInt32),
    ]
    return JOB_SET_ARRAY
def _define_JOBOBJECT_BASIC_ACCOUNTING_INFORMATION_head():
    class JOBOBJECT_BASIC_ACCOUNTING_INFORMATION(Structure):
        pass
    return JOBOBJECT_BASIC_ACCOUNTING_INFORMATION
def _define_JOBOBJECT_BASIC_ACCOUNTING_INFORMATION():
    JOBOBJECT_BASIC_ACCOUNTING_INFORMATION = win32more.System.JobObjects.JOBOBJECT_BASIC_ACCOUNTING_INFORMATION_head
    JOBOBJECT_BASIC_ACCOUNTING_INFORMATION._fields_ = [
        ("TotalUserTime", win32more.Foundation.LARGE_INTEGER),
        ("TotalKernelTime", win32more.Foundation.LARGE_INTEGER),
        ("ThisPeriodTotalUserTime", win32more.Foundation.LARGE_INTEGER),
        ("ThisPeriodTotalKernelTime", win32more.Foundation.LARGE_INTEGER),
        ("TotalPageFaultCount", UInt32),
        ("TotalProcesses", UInt32),
        ("ActiveProcesses", UInt32),
        ("TotalTerminatedProcesses", UInt32),
    ]
    return JOBOBJECT_BASIC_ACCOUNTING_INFORMATION
def _define_JOBOBJECT_BASIC_LIMIT_INFORMATION_head():
    class JOBOBJECT_BASIC_LIMIT_INFORMATION(Structure):
        pass
    return JOBOBJECT_BASIC_LIMIT_INFORMATION
def _define_JOBOBJECT_BASIC_LIMIT_INFORMATION():
    JOBOBJECT_BASIC_LIMIT_INFORMATION = win32more.System.JobObjects.JOBOBJECT_BASIC_LIMIT_INFORMATION_head
    JOBOBJECT_BASIC_LIMIT_INFORMATION._fields_ = [
        ("PerProcessUserTimeLimit", win32more.Foundation.LARGE_INTEGER),
        ("PerJobUserTimeLimit", win32more.Foundation.LARGE_INTEGER),
        ("LimitFlags", win32more.System.JobObjects.JOB_OBJECT_LIMIT),
        ("MinimumWorkingSetSize", UIntPtr),
        ("MaximumWorkingSetSize", UIntPtr),
        ("ActiveProcessLimit", UInt32),
        ("Affinity", UIntPtr),
        ("PriorityClass", UInt32),
        ("SchedulingClass", UInt32),
    ]
    return JOBOBJECT_BASIC_LIMIT_INFORMATION
def _define_JOBOBJECT_EXTENDED_LIMIT_INFORMATION_head():
    class JOBOBJECT_EXTENDED_LIMIT_INFORMATION(Structure):
        pass
    return JOBOBJECT_EXTENDED_LIMIT_INFORMATION
def _define_JOBOBJECT_EXTENDED_LIMIT_INFORMATION():
    JOBOBJECT_EXTENDED_LIMIT_INFORMATION = win32more.System.JobObjects.JOBOBJECT_EXTENDED_LIMIT_INFORMATION_head
    JOBOBJECT_EXTENDED_LIMIT_INFORMATION._fields_ = [
        ("BasicLimitInformation", win32more.System.JobObjects.JOBOBJECT_BASIC_LIMIT_INFORMATION),
        ("IoInfo", win32more.System.Threading.IO_COUNTERS),
        ("ProcessMemoryLimit", UIntPtr),
        ("JobMemoryLimit", UIntPtr),
        ("PeakProcessMemoryUsed", UIntPtr),
        ("PeakJobMemoryUsed", UIntPtr),
    ]
    return JOBOBJECT_EXTENDED_LIMIT_INFORMATION
def _define_JOBOBJECT_BASIC_PROCESS_ID_LIST_head():
    class JOBOBJECT_BASIC_PROCESS_ID_LIST(Structure):
        pass
    return JOBOBJECT_BASIC_PROCESS_ID_LIST
def _define_JOBOBJECT_BASIC_PROCESS_ID_LIST():
    JOBOBJECT_BASIC_PROCESS_ID_LIST = win32more.System.JobObjects.JOBOBJECT_BASIC_PROCESS_ID_LIST_head
    JOBOBJECT_BASIC_PROCESS_ID_LIST._fields_ = [
        ("NumberOfAssignedProcesses", UInt32),
        ("NumberOfProcessIdsInList", UInt32),
        ("ProcessIdList", UIntPtr * 0),
    ]
    return JOBOBJECT_BASIC_PROCESS_ID_LIST
def _define_JOBOBJECT_BASIC_UI_RESTRICTIONS_head():
    class JOBOBJECT_BASIC_UI_RESTRICTIONS(Structure):
        pass
    return JOBOBJECT_BASIC_UI_RESTRICTIONS
def _define_JOBOBJECT_BASIC_UI_RESTRICTIONS():
    JOBOBJECT_BASIC_UI_RESTRICTIONS = win32more.System.JobObjects.JOBOBJECT_BASIC_UI_RESTRICTIONS_head
    JOBOBJECT_BASIC_UI_RESTRICTIONS._fields_ = [
        ("UIRestrictionsClass", win32more.System.JobObjects.JOB_OBJECT_UILIMIT),
    ]
    return JOBOBJECT_BASIC_UI_RESTRICTIONS
def _define_JOBOBJECT_SECURITY_LIMIT_INFORMATION_head():
    class JOBOBJECT_SECURITY_LIMIT_INFORMATION(Structure):
        pass
    return JOBOBJECT_SECURITY_LIMIT_INFORMATION
def _define_JOBOBJECT_SECURITY_LIMIT_INFORMATION():
    JOBOBJECT_SECURITY_LIMIT_INFORMATION = win32more.System.JobObjects.JOBOBJECT_SECURITY_LIMIT_INFORMATION_head
    JOBOBJECT_SECURITY_LIMIT_INFORMATION._fields_ = [
        ("SecurityLimitFlags", win32more.System.JobObjects.JOB_OBJECT_SECURITY),
        ("JobToken", win32more.Foundation.HANDLE),
        ("SidsToDisable", POINTER(win32more.Security.TOKEN_GROUPS_head)),
        ("PrivilegesToDelete", POINTER(win32more.Security.TOKEN_PRIVILEGES_head)),
        ("RestrictedSids", POINTER(win32more.Security.TOKEN_GROUPS_head)),
    ]
    return JOBOBJECT_SECURITY_LIMIT_INFORMATION
def _define_JOBOBJECT_END_OF_JOB_TIME_INFORMATION_head():
    class JOBOBJECT_END_OF_JOB_TIME_INFORMATION(Structure):
        pass
    return JOBOBJECT_END_OF_JOB_TIME_INFORMATION
def _define_JOBOBJECT_END_OF_JOB_TIME_INFORMATION():
    JOBOBJECT_END_OF_JOB_TIME_INFORMATION = win32more.System.JobObjects.JOBOBJECT_END_OF_JOB_TIME_INFORMATION_head
    JOBOBJECT_END_OF_JOB_TIME_INFORMATION._fields_ = [
        ("EndOfJobTimeAction", win32more.System.JobObjects.JOB_OBJECT_TERMINATE_AT_END_ACTION),
    ]
    return JOBOBJECT_END_OF_JOB_TIME_INFORMATION
def _define_JOBOBJECT_ASSOCIATE_COMPLETION_PORT_head():
    class JOBOBJECT_ASSOCIATE_COMPLETION_PORT(Structure):
        pass
    return JOBOBJECT_ASSOCIATE_COMPLETION_PORT
def _define_JOBOBJECT_ASSOCIATE_COMPLETION_PORT():
    JOBOBJECT_ASSOCIATE_COMPLETION_PORT = win32more.System.JobObjects.JOBOBJECT_ASSOCIATE_COMPLETION_PORT_head
    JOBOBJECT_ASSOCIATE_COMPLETION_PORT._fields_ = [
        ("CompletionKey", c_void_p),
        ("CompletionPort", win32more.Foundation.HANDLE),
    ]
    return JOBOBJECT_ASSOCIATE_COMPLETION_PORT
def _define_JOBOBJECT_BASIC_AND_IO_ACCOUNTING_INFORMATION_head():
    class JOBOBJECT_BASIC_AND_IO_ACCOUNTING_INFORMATION(Structure):
        pass
    return JOBOBJECT_BASIC_AND_IO_ACCOUNTING_INFORMATION
def _define_JOBOBJECT_BASIC_AND_IO_ACCOUNTING_INFORMATION():
    JOBOBJECT_BASIC_AND_IO_ACCOUNTING_INFORMATION = win32more.System.JobObjects.JOBOBJECT_BASIC_AND_IO_ACCOUNTING_INFORMATION_head
    JOBOBJECT_BASIC_AND_IO_ACCOUNTING_INFORMATION._fields_ = [
        ("BasicInfo", win32more.System.JobObjects.JOBOBJECT_BASIC_ACCOUNTING_INFORMATION),
        ("IoInfo", win32more.System.Threading.IO_COUNTERS),
    ]
    return JOBOBJECT_BASIC_AND_IO_ACCOUNTING_INFORMATION
def _define_JOBOBJECT_JOBSET_INFORMATION_head():
    class JOBOBJECT_JOBSET_INFORMATION(Structure):
        pass
    return JOBOBJECT_JOBSET_INFORMATION
def _define_JOBOBJECT_JOBSET_INFORMATION():
    JOBOBJECT_JOBSET_INFORMATION = win32more.System.JobObjects.JOBOBJECT_JOBSET_INFORMATION_head
    JOBOBJECT_JOBSET_INFORMATION._fields_ = [
        ("MemberLevel", UInt32),
    ]
    return JOBOBJECT_JOBSET_INFORMATION
JOBOBJECT_RATE_CONTROL_TOLERANCE = Int32
JOBOBJECT_RATE_CONTROL_TOLERANCE_ToleranceLow = 1
JOBOBJECT_RATE_CONTROL_TOLERANCE_ToleranceMedium = 2
JOBOBJECT_RATE_CONTROL_TOLERANCE_ToleranceHigh = 3
JOBOBJECT_RATE_CONTROL_TOLERANCE_INTERVAL = Int32
JOBOBJECT_RATE_CONTROL_TOLERANCE_INTERVAL_ToleranceIntervalShort = 1
JOBOBJECT_RATE_CONTROL_TOLERANCE_INTERVAL_ToleranceIntervalMedium = 2
JOBOBJECT_RATE_CONTROL_TOLERANCE_INTERVAL_ToleranceIntervalLong = 3
def _define_JOBOBJECT_NOTIFICATION_LIMIT_INFORMATION_head():
    class JOBOBJECT_NOTIFICATION_LIMIT_INFORMATION(Structure):
        pass
    return JOBOBJECT_NOTIFICATION_LIMIT_INFORMATION
def _define_JOBOBJECT_NOTIFICATION_LIMIT_INFORMATION():
    JOBOBJECT_NOTIFICATION_LIMIT_INFORMATION = win32more.System.JobObjects.JOBOBJECT_NOTIFICATION_LIMIT_INFORMATION_head
    JOBOBJECT_NOTIFICATION_LIMIT_INFORMATION._fields_ = [
        ("IoReadBytesLimit", UInt64),
        ("IoWriteBytesLimit", UInt64),
        ("PerJobUserTimeLimit", win32more.Foundation.LARGE_INTEGER),
        ("JobMemoryLimit", UInt64),
        ("RateControlTolerance", win32more.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE),
        ("RateControlToleranceInterval", win32more.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE_INTERVAL),
        ("LimitFlags", win32more.System.JobObjects.JOB_OBJECT_LIMIT),
    ]
    return JOBOBJECT_NOTIFICATION_LIMIT_INFORMATION
def _define_JOBOBJECT_NOTIFICATION_LIMIT_INFORMATION_2_head():
    class JOBOBJECT_NOTIFICATION_LIMIT_INFORMATION_2(Structure):
        pass
    return JOBOBJECT_NOTIFICATION_LIMIT_INFORMATION_2
def _define_JOBOBJECT_NOTIFICATION_LIMIT_INFORMATION_2():
    JOBOBJECT_NOTIFICATION_LIMIT_INFORMATION_2 = win32more.System.JobObjects.JOBOBJECT_NOTIFICATION_LIMIT_INFORMATION_2_head
    class JOBOBJECT_NOTIFICATION_LIMIT_INFORMATION_2__Anonymous3_e__Union(Union):
        pass
    JOBOBJECT_NOTIFICATION_LIMIT_INFORMATION_2__Anonymous3_e__Union._fields_ = [
        ("RateControlToleranceInterval", win32more.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE_INTERVAL),
        ("CpuRateControlToleranceInterval", win32more.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE_INTERVAL),
    ]
    class JOBOBJECT_NOTIFICATION_LIMIT_INFORMATION_2__Anonymous1_e__Union(Union):
        pass
    JOBOBJECT_NOTIFICATION_LIMIT_INFORMATION_2__Anonymous1_e__Union._fields_ = [
        ("JobHighMemoryLimit", UInt64),
        ("JobMemoryLimit", UInt64),
    ]
    class JOBOBJECT_NOTIFICATION_LIMIT_INFORMATION_2__Anonymous2_e__Union(Union):
        pass
    JOBOBJECT_NOTIFICATION_LIMIT_INFORMATION_2__Anonymous2_e__Union._fields_ = [
        ("RateControlTolerance", win32more.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE),
        ("CpuRateControlTolerance", win32more.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE),
    ]
    JOBOBJECT_NOTIFICATION_LIMIT_INFORMATION_2._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
        'Anonymous3',
    ]
    JOBOBJECT_NOTIFICATION_LIMIT_INFORMATION_2._fields_ = [
        ("IoReadBytesLimit", UInt64),
        ("IoWriteBytesLimit", UInt64),
        ("PerJobUserTimeLimit", win32more.Foundation.LARGE_INTEGER),
        ("Anonymous1", JOBOBJECT_NOTIFICATION_LIMIT_INFORMATION_2__Anonymous1_e__Union),
        ("Anonymous2", JOBOBJECT_NOTIFICATION_LIMIT_INFORMATION_2__Anonymous2_e__Union),
        ("Anonymous3", JOBOBJECT_NOTIFICATION_LIMIT_INFORMATION_2__Anonymous3_e__Union),
        ("LimitFlags", win32more.System.JobObjects.JOB_OBJECT_LIMIT),
        ("IoRateControlTolerance", win32more.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE),
        ("JobLowMemoryLimit", UInt64),
        ("IoRateControlToleranceInterval", win32more.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE_INTERVAL),
        ("NetRateControlTolerance", win32more.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE),
        ("NetRateControlToleranceInterval", win32more.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE_INTERVAL),
    ]
    return JOBOBJECT_NOTIFICATION_LIMIT_INFORMATION_2
def _define_JOBOBJECT_LIMIT_VIOLATION_INFORMATION_head():
    class JOBOBJECT_LIMIT_VIOLATION_INFORMATION(Structure):
        pass
    return JOBOBJECT_LIMIT_VIOLATION_INFORMATION
def _define_JOBOBJECT_LIMIT_VIOLATION_INFORMATION():
    JOBOBJECT_LIMIT_VIOLATION_INFORMATION = win32more.System.JobObjects.JOBOBJECT_LIMIT_VIOLATION_INFORMATION_head
    JOBOBJECT_LIMIT_VIOLATION_INFORMATION._fields_ = [
        ("LimitFlags", win32more.System.JobObjects.JOB_OBJECT_LIMIT),
        ("ViolationLimitFlags", win32more.System.JobObjects.JOB_OBJECT_LIMIT),
        ("IoReadBytes", UInt64),
        ("IoReadBytesLimit", UInt64),
        ("IoWriteBytes", UInt64),
        ("IoWriteBytesLimit", UInt64),
        ("PerJobUserTime", win32more.Foundation.LARGE_INTEGER),
        ("PerJobUserTimeLimit", win32more.Foundation.LARGE_INTEGER),
        ("JobMemory", UInt64),
        ("JobMemoryLimit", UInt64),
        ("RateControlTolerance", win32more.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE),
        ("RateControlToleranceLimit", win32more.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE),
    ]
    return JOBOBJECT_LIMIT_VIOLATION_INFORMATION
def _define_JOBOBJECT_LIMIT_VIOLATION_INFORMATION_2_head():
    class JOBOBJECT_LIMIT_VIOLATION_INFORMATION_2(Structure):
        pass
    return JOBOBJECT_LIMIT_VIOLATION_INFORMATION_2
def _define_JOBOBJECT_LIMIT_VIOLATION_INFORMATION_2():
    JOBOBJECT_LIMIT_VIOLATION_INFORMATION_2 = win32more.System.JobObjects.JOBOBJECT_LIMIT_VIOLATION_INFORMATION_2_head
    class JOBOBJECT_LIMIT_VIOLATION_INFORMATION_2__Anonymous2_e__Union(Union):
        pass
    JOBOBJECT_LIMIT_VIOLATION_INFORMATION_2__Anonymous2_e__Union._fields_ = [
        ("RateControlTolerance", win32more.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE),
        ("CpuRateControlTolerance", win32more.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE),
    ]
    class JOBOBJECT_LIMIT_VIOLATION_INFORMATION_2__Anonymous3_e__Union(Union):
        pass
    JOBOBJECT_LIMIT_VIOLATION_INFORMATION_2__Anonymous3_e__Union._fields_ = [
        ("RateControlToleranceLimit", win32more.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE),
        ("CpuRateControlToleranceLimit", win32more.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE),
    ]
    class JOBOBJECT_LIMIT_VIOLATION_INFORMATION_2__Anonymous1_e__Union(Union):
        pass
    JOBOBJECT_LIMIT_VIOLATION_INFORMATION_2__Anonymous1_e__Union._fields_ = [
        ("JobHighMemoryLimit", UInt64),
        ("JobMemoryLimit", UInt64),
    ]
    JOBOBJECT_LIMIT_VIOLATION_INFORMATION_2._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
        'Anonymous3',
    ]
    JOBOBJECT_LIMIT_VIOLATION_INFORMATION_2._fields_ = [
        ("LimitFlags", win32more.System.JobObjects.JOB_OBJECT_LIMIT),
        ("ViolationLimitFlags", win32more.System.JobObjects.JOB_OBJECT_LIMIT),
        ("IoReadBytes", UInt64),
        ("IoReadBytesLimit", UInt64),
        ("IoWriteBytes", UInt64),
        ("IoWriteBytesLimit", UInt64),
        ("PerJobUserTime", win32more.Foundation.LARGE_INTEGER),
        ("PerJobUserTimeLimit", win32more.Foundation.LARGE_INTEGER),
        ("JobMemory", UInt64),
        ("Anonymous1", JOBOBJECT_LIMIT_VIOLATION_INFORMATION_2__Anonymous1_e__Union),
        ("Anonymous2", JOBOBJECT_LIMIT_VIOLATION_INFORMATION_2__Anonymous2_e__Union),
        ("Anonymous3", JOBOBJECT_LIMIT_VIOLATION_INFORMATION_2__Anonymous3_e__Union),
        ("JobLowMemoryLimit", UInt64),
        ("IoRateControlTolerance", win32more.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE),
        ("IoRateControlToleranceLimit", win32more.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE),
        ("NetRateControlTolerance", win32more.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE),
        ("NetRateControlToleranceLimit", win32more.System.JobObjects.JOBOBJECT_RATE_CONTROL_TOLERANCE),
    ]
    return JOBOBJECT_LIMIT_VIOLATION_INFORMATION_2
def _define_JOBOBJECT_CPU_RATE_CONTROL_INFORMATION_head():
    class JOBOBJECT_CPU_RATE_CONTROL_INFORMATION(Structure):
        pass
    return JOBOBJECT_CPU_RATE_CONTROL_INFORMATION
def _define_JOBOBJECT_CPU_RATE_CONTROL_INFORMATION():
    JOBOBJECT_CPU_RATE_CONTROL_INFORMATION = win32more.System.JobObjects.JOBOBJECT_CPU_RATE_CONTROL_INFORMATION_head
    class JOBOBJECT_CPU_RATE_CONTROL_INFORMATION__Anonymous_e__Union(Union):
        pass
    class JOBOBJECT_CPU_RATE_CONTROL_INFORMATION__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    JOBOBJECT_CPU_RATE_CONTROL_INFORMATION__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ("MinRate", UInt16),
        ("MaxRate", UInt16),
    ]
    JOBOBJECT_CPU_RATE_CONTROL_INFORMATION__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    JOBOBJECT_CPU_RATE_CONTROL_INFORMATION__Anonymous_e__Union._fields_ = [
        ("CpuRate", UInt32),
        ("Weight", UInt32),
        ("Anonymous", JOBOBJECT_CPU_RATE_CONTROL_INFORMATION__Anonymous_e__Union__Anonymous_e__Struct),
    ]
    JOBOBJECT_CPU_RATE_CONTROL_INFORMATION._anonymous_ = [
        'Anonymous',
    ]
    JOBOBJECT_CPU_RATE_CONTROL_INFORMATION._fields_ = [
        ("ControlFlags", win32more.System.JobObjects.JOB_OBJECT_CPU_RATE_CONTROL),
        ("Anonymous", JOBOBJECT_CPU_RATE_CONTROL_INFORMATION__Anonymous_e__Union),
    ]
    return JOBOBJECT_CPU_RATE_CONTROL_INFORMATION
JOB_OBJECT_NET_RATE_CONTROL_FLAGS = Int32
JOB_OBJECT_NET_RATE_CONTROL_ENABLE = 1
JOB_OBJECT_NET_RATE_CONTROL_MAX_BANDWIDTH = 2
JOB_OBJECT_NET_RATE_CONTROL_DSCP_TAG = 4
JOB_OBJECT_NET_RATE_CONTROL_VALID_FLAGS = 7
def _define_JOBOBJECT_NET_RATE_CONTROL_INFORMATION_head():
    class JOBOBJECT_NET_RATE_CONTROL_INFORMATION(Structure):
        pass
    return JOBOBJECT_NET_RATE_CONTROL_INFORMATION
def _define_JOBOBJECT_NET_RATE_CONTROL_INFORMATION():
    JOBOBJECT_NET_RATE_CONTROL_INFORMATION = win32more.System.JobObjects.JOBOBJECT_NET_RATE_CONTROL_INFORMATION_head
    JOBOBJECT_NET_RATE_CONTROL_INFORMATION._fields_ = [
        ("MaxBandwidth", UInt64),
        ("ControlFlags", win32more.System.JobObjects.JOB_OBJECT_NET_RATE_CONTROL_FLAGS),
        ("DscpTag", Byte),
    ]
    return JOBOBJECT_NET_RATE_CONTROL_INFORMATION
JOB_OBJECT_IO_RATE_CONTROL_FLAGS = Int32
JOB_OBJECT_IO_RATE_CONTROL_ENABLE = 1
JOB_OBJECT_IO_RATE_CONTROL_STANDALONE_VOLUME = 2
JOB_OBJECT_IO_RATE_CONTROL_FORCE_UNIT_ACCESS_ALL = 4
JOB_OBJECT_IO_RATE_CONTROL_FORCE_UNIT_ACCESS_ON_SOFT_CAP = 8
JOB_OBJECT_IO_RATE_CONTROL_VALID_FLAGS = 15
def _define_JOBOBJECT_IO_RATE_CONTROL_INFORMATION_NATIVE_head():
    class JOBOBJECT_IO_RATE_CONTROL_INFORMATION_NATIVE(Structure):
        pass
    return JOBOBJECT_IO_RATE_CONTROL_INFORMATION_NATIVE
def _define_JOBOBJECT_IO_RATE_CONTROL_INFORMATION_NATIVE():
    JOBOBJECT_IO_RATE_CONTROL_INFORMATION_NATIVE = win32more.System.JobObjects.JOBOBJECT_IO_RATE_CONTROL_INFORMATION_NATIVE_head
    JOBOBJECT_IO_RATE_CONTROL_INFORMATION_NATIVE._fields_ = [
        ("MaxIops", Int64),
        ("MaxBandwidth", Int64),
        ("ReservationIops", Int64),
        ("VolumeName", win32more.Foundation.PWSTR),
        ("BaseIoSize", UInt32),
        ("ControlFlags", win32more.System.JobObjects.JOB_OBJECT_IO_RATE_CONTROL_FLAGS),
        ("VolumeNameLength", UInt16),
    ]
    return JOBOBJECT_IO_RATE_CONTROL_INFORMATION_NATIVE
def _define_JOBOBJECT_IO_RATE_CONTROL_INFORMATION_NATIVE_V2_head():
    class JOBOBJECT_IO_RATE_CONTROL_INFORMATION_NATIVE_V2(Structure):
        pass
    return JOBOBJECT_IO_RATE_CONTROL_INFORMATION_NATIVE_V2
def _define_JOBOBJECT_IO_RATE_CONTROL_INFORMATION_NATIVE_V2():
    JOBOBJECT_IO_RATE_CONTROL_INFORMATION_NATIVE_V2 = win32more.System.JobObjects.JOBOBJECT_IO_RATE_CONTROL_INFORMATION_NATIVE_V2_head
    JOBOBJECT_IO_RATE_CONTROL_INFORMATION_NATIVE_V2._fields_ = [
        ("MaxIops", Int64),
        ("MaxBandwidth", Int64),
        ("ReservationIops", Int64),
        ("VolumeName", win32more.Foundation.PWSTR),
        ("BaseIoSize", UInt32),
        ("ControlFlags", win32more.System.JobObjects.JOB_OBJECT_IO_RATE_CONTROL_FLAGS),
        ("VolumeNameLength", UInt16),
        ("CriticalReservationIops", Int64),
        ("ReservationBandwidth", Int64),
        ("CriticalReservationBandwidth", Int64),
        ("MaxTimePercent", Int64),
        ("ReservationTimePercent", Int64),
        ("CriticalReservationTimePercent", Int64),
    ]
    return JOBOBJECT_IO_RATE_CONTROL_INFORMATION_NATIVE_V2
def _define_JOBOBJECT_IO_RATE_CONTROL_INFORMATION_NATIVE_V3_head():
    class JOBOBJECT_IO_RATE_CONTROL_INFORMATION_NATIVE_V3(Structure):
        pass
    return JOBOBJECT_IO_RATE_CONTROL_INFORMATION_NATIVE_V3
def _define_JOBOBJECT_IO_RATE_CONTROL_INFORMATION_NATIVE_V3():
    JOBOBJECT_IO_RATE_CONTROL_INFORMATION_NATIVE_V3 = win32more.System.JobObjects.JOBOBJECT_IO_RATE_CONTROL_INFORMATION_NATIVE_V3_head
    JOBOBJECT_IO_RATE_CONTROL_INFORMATION_NATIVE_V3._fields_ = [
        ("MaxIops", Int64),
        ("MaxBandwidth", Int64),
        ("ReservationIops", Int64),
        ("VolumeName", win32more.Foundation.PWSTR),
        ("BaseIoSize", UInt32),
        ("ControlFlags", win32more.System.JobObjects.JOB_OBJECT_IO_RATE_CONTROL_FLAGS),
        ("VolumeNameLength", UInt16),
        ("CriticalReservationIops", Int64),
        ("ReservationBandwidth", Int64),
        ("CriticalReservationBandwidth", Int64),
        ("MaxTimePercent", Int64),
        ("ReservationTimePercent", Int64),
        ("CriticalReservationTimePercent", Int64),
        ("SoftMaxIops", Int64),
        ("SoftMaxBandwidth", Int64),
        ("SoftMaxTimePercent", Int64),
        ("LimitExcessNotifyIops", Int64),
        ("LimitExcessNotifyBandwidth", Int64),
        ("LimitExcessNotifyTimePercent", Int64),
    ]
    return JOBOBJECT_IO_RATE_CONTROL_INFORMATION_NATIVE_V3
JOBOBJECT_IO_ATTRIBUTION_CONTROL_FLAGS = Int32
JOBOBJECT_IO_ATTRIBUTION_CONTROL_ENABLE = 1
JOBOBJECT_IO_ATTRIBUTION_CONTROL_DISABLE = 2
JOBOBJECT_IO_ATTRIBUTION_CONTROL_VALID_FLAGS = 3
def _define_JOBOBJECT_IO_ATTRIBUTION_STATS_head():
    class JOBOBJECT_IO_ATTRIBUTION_STATS(Structure):
        pass
    return JOBOBJECT_IO_ATTRIBUTION_STATS
def _define_JOBOBJECT_IO_ATTRIBUTION_STATS():
    JOBOBJECT_IO_ATTRIBUTION_STATS = win32more.System.JobObjects.JOBOBJECT_IO_ATTRIBUTION_STATS_head
    JOBOBJECT_IO_ATTRIBUTION_STATS._fields_ = [
        ("IoCount", UIntPtr),
        ("TotalNonOverlappedQueueTime", UInt64),
        ("TotalNonOverlappedServiceTime", UInt64),
        ("TotalSize", UInt64),
    ]
    return JOBOBJECT_IO_ATTRIBUTION_STATS
def _define_JOBOBJECT_IO_ATTRIBUTION_INFORMATION_head():
    class JOBOBJECT_IO_ATTRIBUTION_INFORMATION(Structure):
        pass
    return JOBOBJECT_IO_ATTRIBUTION_INFORMATION
def _define_JOBOBJECT_IO_ATTRIBUTION_INFORMATION():
    JOBOBJECT_IO_ATTRIBUTION_INFORMATION = win32more.System.JobObjects.JOBOBJECT_IO_ATTRIBUTION_INFORMATION_head
    JOBOBJECT_IO_ATTRIBUTION_INFORMATION._fields_ = [
        ("ControlFlags", UInt32),
        ("ReadStats", win32more.System.JobObjects.JOBOBJECT_IO_ATTRIBUTION_STATS),
        ("WriteStats", win32more.System.JobObjects.JOBOBJECT_IO_ATTRIBUTION_STATS),
    ]
    return JOBOBJECT_IO_ATTRIBUTION_INFORMATION
JOBOBJECTINFOCLASS = Int32
JOBOBJECTINFOCLASS_JobObjectBasicAccountingInformation = 1
JOBOBJECTINFOCLASS_JobObjectBasicLimitInformation = 2
JOBOBJECTINFOCLASS_JobObjectBasicProcessIdList = 3
JOBOBJECTINFOCLASS_JobObjectBasicUIRestrictions = 4
JOBOBJECTINFOCLASS_JobObjectSecurityLimitInformation = 5
JOBOBJECTINFOCLASS_JobObjectEndOfJobTimeInformation = 6
JOBOBJECTINFOCLASS_JobObjectAssociateCompletionPortInformation = 7
JOBOBJECTINFOCLASS_JobObjectBasicAndIoAccountingInformation = 8
JOBOBJECTINFOCLASS_JobObjectExtendedLimitInformation = 9
JOBOBJECTINFOCLASS_JobObjectJobSetInformation = 10
JOBOBJECTINFOCLASS_JobObjectGroupInformation = 11
JOBOBJECTINFOCLASS_JobObjectNotificationLimitInformation = 12
JOBOBJECTINFOCLASS_JobObjectLimitViolationInformation = 13
JOBOBJECTINFOCLASS_JobObjectGroupInformationEx = 14
JOBOBJECTINFOCLASS_JobObjectCpuRateControlInformation = 15
JOBOBJECTINFOCLASS_JobObjectCompletionFilter = 16
JOBOBJECTINFOCLASS_JobObjectCompletionCounter = 17
JOBOBJECTINFOCLASS_JobObjectReserved1Information = 18
JOBOBJECTINFOCLASS_JobObjectReserved2Information = 19
JOBOBJECTINFOCLASS_JobObjectReserved3Information = 20
JOBOBJECTINFOCLASS_JobObjectReserved4Information = 21
JOBOBJECTINFOCLASS_JobObjectReserved5Information = 22
JOBOBJECTINFOCLASS_JobObjectReserved6Information = 23
JOBOBJECTINFOCLASS_JobObjectReserved7Information = 24
JOBOBJECTINFOCLASS_JobObjectReserved8Information = 25
JOBOBJECTINFOCLASS_JobObjectReserved9Information = 26
JOBOBJECTINFOCLASS_JobObjectReserved10Information = 27
JOBOBJECTINFOCLASS_JobObjectReserved11Information = 28
JOBOBJECTINFOCLASS_JobObjectReserved12Information = 29
JOBOBJECTINFOCLASS_JobObjectReserved13Information = 30
JOBOBJECTINFOCLASS_JobObjectReserved14Information = 31
JOBOBJECTINFOCLASS_JobObjectNetRateControlInformation = 32
JOBOBJECTINFOCLASS_JobObjectNotificationLimitInformation2 = 33
JOBOBJECTINFOCLASS_JobObjectLimitViolationInformation2 = 34
JOBOBJECTINFOCLASS_JobObjectCreateSilo = 35
JOBOBJECTINFOCLASS_JobObjectSiloBasicInformation = 36
JOBOBJECTINFOCLASS_JobObjectReserved15Information = 37
JOBOBJECTINFOCLASS_JobObjectReserved16Information = 38
JOBOBJECTINFOCLASS_JobObjectReserved17Information = 39
JOBOBJECTINFOCLASS_JobObjectReserved18Information = 40
JOBOBJECTINFOCLASS_JobObjectReserved19Information = 41
JOBOBJECTINFOCLASS_JobObjectReserved20Information = 42
JOBOBJECTINFOCLASS_JobObjectReserved21Information = 43
JOBOBJECTINFOCLASS_JobObjectReserved22Information = 44
JOBOBJECTINFOCLASS_JobObjectReserved23Information = 45
JOBOBJECTINFOCLASS_JobObjectReserved24Information = 46
JOBOBJECTINFOCLASS_JobObjectReserved25Information = 47
JOBOBJECTINFOCLASS_MaxJobObjectInfoClass = 48
def _define_IsProcessInJob():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.BOOL), use_last_error=True)(("IsProcessInJob", windll["KERNEL32"]), ((1, 'ProcessHandle'),(1, 'JobHandle'),(1, 'Result'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateJobObjectW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),win32more.Foundation.PWSTR, use_last_error=True)(("CreateJobObjectW", windll["KERNEL32"]), ((1, 'lpJobAttributes'),(1, 'lpName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateJobObject():
    return win32more.System.JobObjects.CreateJobObjectW
def _define_FreeMemoryJobObject():
    try:
        return WINFUNCTYPE(Void,c_void_p, use_last_error=False)(("FreeMemoryJobObject", windll["KERNEL32"]), ((1, 'Buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenJobObjectW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,UInt32,win32more.Foundation.BOOL,win32more.Foundation.PWSTR, use_last_error=True)(("OpenJobObjectW", windll["KERNEL32"]), ((1, 'dwDesiredAccess'),(1, 'bInheritHandle'),(1, 'lpName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenJobObject():
    return win32more.System.JobObjects.OpenJobObjectW
def _define_AssignProcessToJobObject():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE, use_last_error=True)(("AssignProcessToJobObject", windll["KERNEL32"]), ((1, 'hJob'),(1, 'hProcess'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TerminateJobObject():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32, use_last_error=True)(("TerminateJobObject", windll["KERNEL32"]), ((1, 'hJob'),(1, 'uExitCode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetInformationJobObject():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.System.JobObjects.JOBOBJECTINFOCLASS,c_void_p,UInt32, use_last_error=True)(("SetInformationJobObject", windll["KERNEL32"]), ((1, 'hJob'),(1, 'JobObjectInformationClass'),(1, 'lpJobObjectInformation'),(1, 'cbJobObjectInformationLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetIoRateControlInformationJobObject():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(win32more.System.JobObjects.JOBOBJECT_IO_RATE_CONTROL_INFORMATION_head), use_last_error=True)(("SetIoRateControlInformationJobObject", windll["KERNEL32"]), ((1, 'hJob'),(1, 'IoRateControlInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryInformationJobObject():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.System.JobObjects.JOBOBJECTINFOCLASS,c_void_p,UInt32,POINTER(UInt32), use_last_error=True)(("QueryInformationJobObject", windll["KERNEL32"]), ((1, 'hJob'),(1, 'JobObjectInformationClass'),(1, 'lpJobObjectInformation'),(1, 'cbJobObjectInformationLength'),(1, 'lpReturnLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryIoRateControlInformationJobObject():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,POINTER(POINTER(win32more.System.JobObjects.JOBOBJECT_IO_RATE_CONTROL_INFORMATION_head)),POINTER(UInt32), use_last_error=True)(("QueryIoRateControlInformationJobObject", windll["KERNEL32"]), ((1, 'hJob'),(1, 'VolumeName'),(1, 'InfoBlocks'),(1, 'InfoBlockCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UserHandleGrantAccess():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,win32more.Foundation.BOOL, use_last_error=True)(("UserHandleGrantAccess", windll["USER32"]), ((1, 'hUserHandle'),(1, 'hJob'),(1, 'bGrant'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateJobObjectA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),win32more.Foundation.PSTR, use_last_error=True)(("CreateJobObjectA", windll["KERNEL32"]), ((1, 'lpJobAttributes'),(1, 'lpName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenJobObjectA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,UInt32,win32more.Foundation.BOOL,win32more.Foundation.PSTR, use_last_error=True)(("OpenJobObjectA", windll["KERNEL32"]), ((1, 'dwDesiredAccess'),(1, 'bInheritHandle'),(1, 'lpName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateJobSet():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,POINTER(win32more.System.JobObjects.JOB_SET_ARRAY),UInt32, use_last_error=False)(("CreateJobSet", windll["KERNEL32"]), ((1, 'NumJob'),(1, 'UserJobSet'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "JOB_OBJECT_LIMIT",
    "JOB_OBJECT_LIMIT_WORKINGSET",
    "JOB_OBJECT_LIMIT_PROCESS_TIME",
    "JOB_OBJECT_LIMIT_JOB_TIME",
    "JOB_OBJECT_LIMIT_ACTIVE_PROCESS",
    "JOB_OBJECT_LIMIT_AFFINITY",
    "JOB_OBJECT_LIMIT_PRIORITY_CLASS",
    "JOB_OBJECT_LIMIT_PRESERVE_JOB_TIME",
    "JOB_OBJECT_LIMIT_SCHEDULING_CLASS",
    "JOB_OBJECT_LIMIT_PROCESS_MEMORY",
    "JOB_OBJECT_LIMIT_JOB_MEMORY",
    "JOB_OBJECT_LIMIT_JOB_MEMORY_HIGH",
    "JOB_OBJECT_LIMIT_DIE_ON_UNHANDLED_EXCEPTION",
    "JOB_OBJECT_LIMIT_BREAKAWAY_OK",
    "JOB_OBJECT_LIMIT_SILENT_BREAKAWAY_OK",
    "JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE",
    "JOB_OBJECT_LIMIT_SUBSET_AFFINITY",
    "JOB_OBJECT_LIMIT_JOB_MEMORY_LOW",
    "JOB_OBJECT_LIMIT_JOB_READ_BYTES",
    "JOB_OBJECT_LIMIT_JOB_WRITE_BYTES",
    "JOB_OBJECT_LIMIT_RATE_CONTROL",
    "JOB_OBJECT_LIMIT_CPU_RATE_CONTROL",
    "JOB_OBJECT_LIMIT_IO_RATE_CONTROL",
    "JOB_OBJECT_LIMIT_NET_RATE_CONTROL",
    "JOB_OBJECT_LIMIT_VALID_FLAGS",
    "JOB_OBJECT_BASIC_LIMIT_VALID_FLAGS",
    "JOB_OBJECT_EXTENDED_LIMIT_VALID_FLAGS",
    "JOB_OBJECT_NOTIFICATION_LIMIT_VALID_FLAGS",
    "JOB_OBJECT_UILIMIT",
    "JOB_OBJECT_UILIMIT_NONE",
    "JOB_OBJECT_UILIMIT_HANDLES",
    "JOB_OBJECT_UILIMIT_READCLIPBOARD",
    "JOB_OBJECT_UILIMIT_WRITECLIPBOARD",
    "JOB_OBJECT_UILIMIT_SYSTEMPARAMETERS",
    "JOB_OBJECT_UILIMIT_DISPLAYSETTINGS",
    "JOB_OBJECT_UILIMIT_GLOBALATOMS",
    "JOB_OBJECT_UILIMIT_DESKTOP",
    "JOB_OBJECT_UILIMIT_EXITWINDOWS",
    "JOB_OBJECT_SECURITY",
    "JOB_OBJECT_SECURITY_NO_ADMIN",
    "JOB_OBJECT_SECURITY_RESTRICTED_TOKEN",
    "JOB_OBJECT_SECURITY_ONLY_TOKEN",
    "JOB_OBJECT_SECURITY_FILTER_TOKENS",
    "JOB_OBJECT_SECURITY_VALID_FLAGS",
    "JOB_OBJECT_CPU_RATE_CONTROL",
    "JOB_OBJECT_CPU_RATE_CONTROL_ENABLE",
    "JOB_OBJECT_CPU_RATE_CONTROL_WEIGHT_BASED",
    "JOB_OBJECT_CPU_RATE_CONTROL_HARD_CAP",
    "JOB_OBJECT_CPU_RATE_CONTROL_NOTIFY",
    "JOB_OBJECT__CPU_RATE_CONTROL_MIN_MAX_RATE",
    "JOB_OBJECT_TERMINATE_AT_END_ACTION",
    "JOB_OBJECT_TERMINATE_AT_END_OF_JOB",
    "JOB_OBJECT_POST_AT_END_OF_JOB",
    "JOBOBJECT_IO_RATE_CONTROL_INFORMATION",
    "JOB_SET_ARRAY",
    "JOBOBJECT_BASIC_ACCOUNTING_INFORMATION",
    "JOBOBJECT_BASIC_LIMIT_INFORMATION",
    "JOBOBJECT_EXTENDED_LIMIT_INFORMATION",
    "JOBOBJECT_BASIC_PROCESS_ID_LIST",
    "JOBOBJECT_BASIC_UI_RESTRICTIONS",
    "JOBOBJECT_SECURITY_LIMIT_INFORMATION",
    "JOBOBJECT_END_OF_JOB_TIME_INFORMATION",
    "JOBOBJECT_ASSOCIATE_COMPLETION_PORT",
    "JOBOBJECT_BASIC_AND_IO_ACCOUNTING_INFORMATION",
    "JOBOBJECT_JOBSET_INFORMATION",
    "JOBOBJECT_RATE_CONTROL_TOLERANCE",
    "JOBOBJECT_RATE_CONTROL_TOLERANCE_ToleranceLow",
    "JOBOBJECT_RATE_CONTROL_TOLERANCE_ToleranceMedium",
    "JOBOBJECT_RATE_CONTROL_TOLERANCE_ToleranceHigh",
    "JOBOBJECT_RATE_CONTROL_TOLERANCE_INTERVAL",
    "JOBOBJECT_RATE_CONTROL_TOLERANCE_INTERVAL_ToleranceIntervalShort",
    "JOBOBJECT_RATE_CONTROL_TOLERANCE_INTERVAL_ToleranceIntervalMedium",
    "JOBOBJECT_RATE_CONTROL_TOLERANCE_INTERVAL_ToleranceIntervalLong",
    "JOBOBJECT_NOTIFICATION_LIMIT_INFORMATION",
    "JOBOBJECT_NOTIFICATION_LIMIT_INFORMATION_2",
    "JOBOBJECT_LIMIT_VIOLATION_INFORMATION",
    "JOBOBJECT_LIMIT_VIOLATION_INFORMATION_2",
    "JOBOBJECT_CPU_RATE_CONTROL_INFORMATION",
    "JOB_OBJECT_NET_RATE_CONTROL_FLAGS",
    "JOB_OBJECT_NET_RATE_CONTROL_ENABLE",
    "JOB_OBJECT_NET_RATE_CONTROL_MAX_BANDWIDTH",
    "JOB_OBJECT_NET_RATE_CONTROL_DSCP_TAG",
    "JOB_OBJECT_NET_RATE_CONTROL_VALID_FLAGS",
    "JOBOBJECT_NET_RATE_CONTROL_INFORMATION",
    "JOB_OBJECT_IO_RATE_CONTROL_FLAGS",
    "JOB_OBJECT_IO_RATE_CONTROL_ENABLE",
    "JOB_OBJECT_IO_RATE_CONTROL_STANDALONE_VOLUME",
    "JOB_OBJECT_IO_RATE_CONTROL_FORCE_UNIT_ACCESS_ALL",
    "JOB_OBJECT_IO_RATE_CONTROL_FORCE_UNIT_ACCESS_ON_SOFT_CAP",
    "JOB_OBJECT_IO_RATE_CONTROL_VALID_FLAGS",
    "JOBOBJECT_IO_RATE_CONTROL_INFORMATION_NATIVE",
    "JOBOBJECT_IO_RATE_CONTROL_INFORMATION_NATIVE_V2",
    "JOBOBJECT_IO_RATE_CONTROL_INFORMATION_NATIVE_V3",
    "JOBOBJECT_IO_ATTRIBUTION_CONTROL_FLAGS",
    "JOBOBJECT_IO_ATTRIBUTION_CONTROL_ENABLE",
    "JOBOBJECT_IO_ATTRIBUTION_CONTROL_DISABLE",
    "JOBOBJECT_IO_ATTRIBUTION_CONTROL_VALID_FLAGS",
    "JOBOBJECT_IO_ATTRIBUTION_STATS",
    "JOBOBJECT_IO_ATTRIBUTION_INFORMATION",
    "JOBOBJECTINFOCLASS",
    "JOBOBJECTINFOCLASS_JobObjectBasicAccountingInformation",
    "JOBOBJECTINFOCLASS_JobObjectBasicLimitInformation",
    "JOBOBJECTINFOCLASS_JobObjectBasicProcessIdList",
    "JOBOBJECTINFOCLASS_JobObjectBasicUIRestrictions",
    "JOBOBJECTINFOCLASS_JobObjectSecurityLimitInformation",
    "JOBOBJECTINFOCLASS_JobObjectEndOfJobTimeInformation",
    "JOBOBJECTINFOCLASS_JobObjectAssociateCompletionPortInformation",
    "JOBOBJECTINFOCLASS_JobObjectBasicAndIoAccountingInformation",
    "JOBOBJECTINFOCLASS_JobObjectExtendedLimitInformation",
    "JOBOBJECTINFOCLASS_JobObjectJobSetInformation",
    "JOBOBJECTINFOCLASS_JobObjectGroupInformation",
    "JOBOBJECTINFOCLASS_JobObjectNotificationLimitInformation",
    "JOBOBJECTINFOCLASS_JobObjectLimitViolationInformation",
    "JOBOBJECTINFOCLASS_JobObjectGroupInformationEx",
    "JOBOBJECTINFOCLASS_JobObjectCpuRateControlInformation",
    "JOBOBJECTINFOCLASS_JobObjectCompletionFilter",
    "JOBOBJECTINFOCLASS_JobObjectCompletionCounter",
    "JOBOBJECTINFOCLASS_JobObjectReserved1Information",
    "JOBOBJECTINFOCLASS_JobObjectReserved2Information",
    "JOBOBJECTINFOCLASS_JobObjectReserved3Information",
    "JOBOBJECTINFOCLASS_JobObjectReserved4Information",
    "JOBOBJECTINFOCLASS_JobObjectReserved5Information",
    "JOBOBJECTINFOCLASS_JobObjectReserved6Information",
    "JOBOBJECTINFOCLASS_JobObjectReserved7Information",
    "JOBOBJECTINFOCLASS_JobObjectReserved8Information",
    "JOBOBJECTINFOCLASS_JobObjectReserved9Information",
    "JOBOBJECTINFOCLASS_JobObjectReserved10Information",
    "JOBOBJECTINFOCLASS_JobObjectReserved11Information",
    "JOBOBJECTINFOCLASS_JobObjectReserved12Information",
    "JOBOBJECTINFOCLASS_JobObjectReserved13Information",
    "JOBOBJECTINFOCLASS_JobObjectReserved14Information",
    "JOBOBJECTINFOCLASS_JobObjectNetRateControlInformation",
    "JOBOBJECTINFOCLASS_JobObjectNotificationLimitInformation2",
    "JOBOBJECTINFOCLASS_JobObjectLimitViolationInformation2",
    "JOBOBJECTINFOCLASS_JobObjectCreateSilo",
    "JOBOBJECTINFOCLASS_JobObjectSiloBasicInformation",
    "JOBOBJECTINFOCLASS_JobObjectReserved15Information",
    "JOBOBJECTINFOCLASS_JobObjectReserved16Information",
    "JOBOBJECTINFOCLASS_JobObjectReserved17Information",
    "JOBOBJECTINFOCLASS_JobObjectReserved18Information",
    "JOBOBJECTINFOCLASS_JobObjectReserved19Information",
    "JOBOBJECTINFOCLASS_JobObjectReserved20Information",
    "JOBOBJECTINFOCLASS_JobObjectReserved21Information",
    "JOBOBJECTINFOCLASS_JobObjectReserved22Information",
    "JOBOBJECTINFOCLASS_JobObjectReserved23Information",
    "JOBOBJECTINFOCLASS_JobObjectReserved24Information",
    "JOBOBJECTINFOCLASS_JobObjectReserved25Information",
    "JOBOBJECTINFOCLASS_MaxJobObjectInfoClass",
    "IsProcessInJob",
    "CreateJobObjectW",
    "CreateJobObject",
    "FreeMemoryJobObject",
    "OpenJobObjectW",
    "OpenJobObject",
    "AssignProcessToJobObject",
    "TerminateJobObject",
    "SetInformationJobObject",
    "SetIoRateControlInformationJobObject",
    "QueryInformationJobObject",
    "QueryIoRateControlInformationJobObject",
    "UserHandleGrantAccess",
    "CreateJobObjectA",
    "OpenJobObjectA",
    "CreateJobSet",
]
