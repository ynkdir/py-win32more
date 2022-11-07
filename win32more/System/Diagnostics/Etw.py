from win32more import *
import win32more.Foundation
import win32more.Security
import win32more.System.Com
import win32more.System.Diagnostics.Etw
import win32more.System.Time

import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
WNODE_FLAG_ALL_DATA = 1
WNODE_FLAG_SINGLE_INSTANCE = 2
WNODE_FLAG_SINGLE_ITEM = 4
WNODE_FLAG_EVENT_ITEM = 8
WNODE_FLAG_FIXED_INSTANCE_SIZE = 16
WNODE_FLAG_TOO_SMALL = 32
WNODE_FLAG_INSTANCES_SAME = 64
WNODE_FLAG_STATIC_INSTANCE_NAMES = 128
WNODE_FLAG_INTERNAL = 256
WNODE_FLAG_USE_TIMESTAMP = 512
WNODE_FLAG_PERSIST_EVENT = 1024
WNODE_FLAG_EVENT_REFERENCE = 8192
WNODE_FLAG_ANSI_INSTANCENAMES = 16384
WNODE_FLAG_METHOD_ITEM = 32768
WNODE_FLAG_PDO_INSTANCE_NAMES = 65536
WNODE_FLAG_TRACED_GUID = 131072
WNODE_FLAG_LOG_WNODE = 262144
WNODE_FLAG_USE_GUID_PTR = 524288
WNODE_FLAG_USE_MOF_PTR = 1048576
WNODE_FLAG_NO_HEADER = 2097152
WNODE_FLAG_SEND_DATA_BLOCK = 4194304
WNODE_FLAG_VERSIONED_PROPERTIES = 8388608
WNODE_FLAG_SEVERITY_MASK = 4278190080
WMIREG_FLAG_EXPENSIVE = 1
WMIREG_FLAG_INSTANCE_LIST = 4
WMIREG_FLAG_INSTANCE_BASENAME = 8
WMIREG_FLAG_INSTANCE_PDO = 32
WMIREG_FLAG_REMOVE_GUID = 65536
WMIREG_FLAG_RESERVED1 = 131072
WMIREG_FLAG_RESERVED2 = 262144
WMIREG_FLAG_TRACED_GUID = 524288
WMIREG_FLAG_TRACE_CONTROL_GUID = 4096
WMIREG_FLAG_EVENT_ONLY_GUID = 64
WMI_GUIDTYPE_TRACECONTROL = 0
WMI_GUIDTYPE_TRACE = 1
WMI_GUIDTYPE_DATA = 2
WMI_GUIDTYPE_EVENT = 3
WMIGUID_QUERY = 1
WMIGUID_SET = 2
WMIGUID_NOTIFICATION = 4
WMIGUID_READ_DESCRIPTION = 8
WMIGUID_EXECUTE = 16
TRACELOG_CREATE_REALTIME = 32
TRACELOG_CREATE_ONDISK = 64
TRACELOG_GUID_ENABLE = 128
TRACELOG_ACCESS_KERNEL_LOGGER = 256
TRACELOG_LOG_EVENT = 512
TRACELOG_CREATE_INPROC = 512
TRACELOG_ACCESS_REALTIME = 1024
TRACELOG_REGISTER_GUIDS = 2048
TRACELOG_JOIN_GROUP = 4096
WMI_GLOBAL_LOGGER_ID = 1
MAX_PAYLOAD_PREDICATES = 8
EventTraceGuid = '68fdd900-4a3e-11d1-84f4-0000f80464e3'
SystemTraceControlGuid = '9e814aad-3204-11d2-9a82-006008a86939'
EventTraceConfigGuid = '01853a65-418f-4f36-aefc-dc0f1d2fd235'
DefaultTraceSecurityGuid = '0811c1af-7a07-4a06-82ed-869455cdf713'
PrivateLoggerNotificationGuid = '3595ab5c-042a-4c8e-b942-2d059bfeb1b1'
SystemIoFilterProviderGuid = 'fbd09363-9e22-4661-b8bf-e7a34b535b8c'
SystemObjectProviderGuid = 'febd7460-3d1d-47eb-af49-c9eeb1e146f2'
SystemPowerProviderGuid = 'c134884a-32d5-4488-80e5-14ed7abb8269'
SystemHypervisorProviderGuid = 'bafa072a-918a-4bed-b622-bc152097098f'
SystemLockProviderGuid = '721ddfd3-dacc-4e1e-b26a-a2cb31d4705a'
SystemConfigProviderGuid = 'fef3a8b6-318d-4b67-a96a-3b0f6b8f18fe'
SystemCpuProviderGuid = 'c6c5265f-eae8-4650-aae4-9d48603d8510'
SystemSchedulerProviderGuid = '599a2a76-4d91-4910-9ac7-7d33f2e97a6c'
SystemProfileProviderGuid = 'bfeb0324-1cee-496f-a409-2ac2b48a6322'
SystemIoProviderGuid = '3d5c43e3-0f1c-4202-b817-174c0070dc79'
SystemMemoryProviderGuid = '82958ca9-b6cd-47f8-a3a8-03ae85a4bc24'
SystemRegistryProviderGuid = '16156bd9-fab4-4cfa-a232-89d1099058e3'
SystemProcessProviderGuid = '151f55dc-467d-471f-83b5-5f889d46ff66'
SystemAlpcProviderGuid = 'fcb9baaf-e529-4980-92e9-ced1a6aadfdf'
SystemSyscallProviderGuid = '434286f7-6f1b-45bb-b37e-95f623046c7c'
SystemInterruptProviderGuid = 'd4bbee17-b545-4888-858b-744169015b25'
SystemTimerProviderGuid = '4f061568-e215-499f-ab2e-eda0ae890a5b'
MAX_MOF_FIELDS = 16
SYSTEM_EVENT_TYPE = 1
EVENT_TRACE_TYPE_INFO = 0
EVENT_TRACE_TYPE_START = 1
EVENT_TRACE_TYPE_END = 2
EVENT_TRACE_TYPE_STOP = 2
EVENT_TRACE_TYPE_DC_START = 3
EVENT_TRACE_TYPE_DC_END = 4
EVENT_TRACE_TYPE_EXTENSION = 5
EVENT_TRACE_TYPE_REPLY = 6
EVENT_TRACE_TYPE_DEQUEUE = 7
EVENT_TRACE_TYPE_RESUME = 7
EVENT_TRACE_TYPE_CHECKPOINT = 8
EVENT_TRACE_TYPE_SUSPEND = 8
EVENT_TRACE_TYPE_WINEVT_SEND = 9
EVENT_TRACE_TYPE_WINEVT_RECEIVE = 240
TRACE_LEVEL_NONE = 0
TRACE_LEVEL_CRITICAL = 1
TRACE_LEVEL_FATAL = 1
TRACE_LEVEL_ERROR = 2
TRACE_LEVEL_WARNING = 3
TRACE_LEVEL_INFORMATION = 4
TRACE_LEVEL_VERBOSE = 5
TRACE_LEVEL_RESERVED6 = 6
TRACE_LEVEL_RESERVED7 = 7
TRACE_LEVEL_RESERVED8 = 8
TRACE_LEVEL_RESERVED9 = 9
EVENT_TRACE_TYPE_LOAD = 10
EVENT_TRACE_TYPE_TERMINATE = 11
EVENT_TRACE_TYPE_IO_READ = 10
EVENT_TRACE_TYPE_IO_WRITE = 11
EVENT_TRACE_TYPE_IO_READ_INIT = 12
EVENT_TRACE_TYPE_IO_WRITE_INIT = 13
EVENT_TRACE_TYPE_IO_FLUSH = 14
EVENT_TRACE_TYPE_IO_FLUSH_INIT = 15
EVENT_TRACE_TYPE_IO_REDIRECTED_INIT = 16
EVENT_TRACE_TYPE_MM_TF = 10
EVENT_TRACE_TYPE_MM_DZF = 11
EVENT_TRACE_TYPE_MM_COW = 12
EVENT_TRACE_TYPE_MM_GPF = 13
EVENT_TRACE_TYPE_MM_HPF = 14
EVENT_TRACE_TYPE_MM_AV = 15
EVENT_TRACE_TYPE_SEND = 10
EVENT_TRACE_TYPE_RECEIVE = 11
EVENT_TRACE_TYPE_CONNECT = 12
EVENT_TRACE_TYPE_DISCONNECT = 13
EVENT_TRACE_TYPE_RETRANSMIT = 14
EVENT_TRACE_TYPE_ACCEPT = 15
EVENT_TRACE_TYPE_RECONNECT = 16
EVENT_TRACE_TYPE_CONNFAIL = 17
EVENT_TRACE_TYPE_COPY_TCP = 18
EVENT_TRACE_TYPE_COPY_ARP = 19
EVENT_TRACE_TYPE_ACKFULL = 20
EVENT_TRACE_TYPE_ACKPART = 21
EVENT_TRACE_TYPE_ACKDUP = 22
EVENT_TRACE_TYPE_GUIDMAP = 10
EVENT_TRACE_TYPE_CONFIG = 11
EVENT_TRACE_TYPE_SIDINFO = 12
EVENT_TRACE_TYPE_SECURITY = 13
EVENT_TRACE_TYPE_DBGID_RSDS = 64
EVENT_TRACE_TYPE_REGCREATE = 10
EVENT_TRACE_TYPE_REGOPEN = 11
EVENT_TRACE_TYPE_REGDELETE = 12
EVENT_TRACE_TYPE_REGQUERY = 13
EVENT_TRACE_TYPE_REGSETVALUE = 14
EVENT_TRACE_TYPE_REGDELETEVALUE = 15
EVENT_TRACE_TYPE_REGQUERYVALUE = 16
EVENT_TRACE_TYPE_REGENUMERATEKEY = 17
EVENT_TRACE_TYPE_REGENUMERATEVALUEKEY = 18
EVENT_TRACE_TYPE_REGQUERYMULTIPLEVALUE = 19
EVENT_TRACE_TYPE_REGSETINFORMATION = 20
EVENT_TRACE_TYPE_REGFLUSH = 21
EVENT_TRACE_TYPE_REGKCBCREATE = 22
EVENT_TRACE_TYPE_REGKCBDELETE = 23
EVENT_TRACE_TYPE_REGKCBRUNDOWNBEGIN = 24
EVENT_TRACE_TYPE_REGKCBRUNDOWNEND = 25
EVENT_TRACE_TYPE_REGVIRTUALIZE = 26
EVENT_TRACE_TYPE_REGCLOSE = 27
EVENT_TRACE_TYPE_REGSETSECURITY = 28
EVENT_TRACE_TYPE_REGQUERYSECURITY = 29
EVENT_TRACE_TYPE_REGCOMMIT = 30
EVENT_TRACE_TYPE_REGPREPARE = 31
EVENT_TRACE_TYPE_REGROLLBACK = 32
EVENT_TRACE_TYPE_REGMOUNTHIVE = 33
EVENT_TRACE_TYPE_CONFIG_CPU = 10
EVENT_TRACE_TYPE_CONFIG_PHYSICALDISK = 11
EVENT_TRACE_TYPE_CONFIG_LOGICALDISK = 12
EVENT_TRACE_TYPE_CONFIG_NIC = 13
EVENT_TRACE_TYPE_CONFIG_VIDEO = 14
EVENT_TRACE_TYPE_CONFIG_SERVICES = 15
EVENT_TRACE_TYPE_CONFIG_POWER = 16
EVENT_TRACE_TYPE_CONFIG_NETINFO = 17
EVENT_TRACE_TYPE_CONFIG_OPTICALMEDIA = 18
EVENT_TRACE_TYPE_CONFIG_IRQ = 21
EVENT_TRACE_TYPE_CONFIG_PNP = 22
EVENT_TRACE_TYPE_CONFIG_IDECHANNEL = 23
EVENT_TRACE_TYPE_CONFIG_NUMANODE = 24
EVENT_TRACE_TYPE_CONFIG_PLATFORM = 25
EVENT_TRACE_TYPE_CONFIG_PROCESSORGROUP = 26
EVENT_TRACE_TYPE_CONFIG_PROCESSORNUMBER = 27
EVENT_TRACE_TYPE_CONFIG_DPI = 28
EVENT_TRACE_TYPE_CONFIG_CI_INFO = 29
EVENT_TRACE_TYPE_CONFIG_MACHINEID = 30
EVENT_TRACE_TYPE_CONFIG_DEFRAG = 31
EVENT_TRACE_TYPE_CONFIG_MOBILEPLATFORM = 32
EVENT_TRACE_TYPE_CONFIG_DEVICEFAMILY = 33
EVENT_TRACE_TYPE_CONFIG_FLIGHTID = 34
EVENT_TRACE_TYPE_CONFIG_PROCESSOR = 35
EVENT_TRACE_TYPE_CONFIG_VIRTUALIZATION = 36
EVENT_TRACE_TYPE_CONFIG_BOOT = 37
EVENT_TRACE_TYPE_OPTICAL_IO_READ = 55
EVENT_TRACE_TYPE_OPTICAL_IO_WRITE = 56
EVENT_TRACE_TYPE_OPTICAL_IO_FLUSH = 57
EVENT_TRACE_TYPE_OPTICAL_IO_READ_INIT = 58
EVENT_TRACE_TYPE_OPTICAL_IO_WRITE_INIT = 59
EVENT_TRACE_TYPE_OPTICAL_IO_FLUSH_INIT = 60
EVENT_TRACE_TYPE_FLT_PREOP_INIT = 96
EVENT_TRACE_TYPE_FLT_POSTOP_INIT = 97
EVENT_TRACE_TYPE_FLT_PREOP_COMPLETION = 98
EVENT_TRACE_TYPE_FLT_POSTOP_COMPLETION = 99
EVENT_TRACE_TYPE_FLT_PREOP_FAILURE = 100
EVENT_TRACE_TYPE_FLT_POSTOP_FAILURE = 101
EVENT_TRACE_FLAG_DEBUG_EVENTS = 4194304
EVENT_TRACE_FLAG_EXTENSION = 2147483648
EVENT_TRACE_FLAG_FORWARD_WMI = 1073741824
EVENT_TRACE_FLAG_ENABLE_RESERVE = 536870912
EVENT_TRACE_FILE_MODE_NONE = 0
EVENT_TRACE_FILE_MODE_SEQUENTIAL = 1
EVENT_TRACE_FILE_MODE_CIRCULAR = 2
EVENT_TRACE_FILE_MODE_APPEND = 4
EVENT_TRACE_REAL_TIME_MODE = 256
EVENT_TRACE_DELAY_OPEN_FILE_MODE = 512
EVENT_TRACE_BUFFERING_MODE = 1024
EVENT_TRACE_PRIVATE_LOGGER_MODE = 2048
EVENT_TRACE_ADD_HEADER_MODE = 4096
EVENT_TRACE_USE_GLOBAL_SEQUENCE = 16384
EVENT_TRACE_USE_LOCAL_SEQUENCE = 32768
EVENT_TRACE_RELOG_MODE = 65536
EVENT_TRACE_USE_PAGED_MEMORY = 16777216
EVENT_TRACE_FILE_MODE_NEWFILE = 8
EVENT_TRACE_FILE_MODE_PREALLOCATE = 32
EVENT_TRACE_NONSTOPPABLE_MODE = 64
EVENT_TRACE_SECURE_MODE = 128
EVENT_TRACE_USE_KBYTES_FOR_SIZE = 8192
EVENT_TRACE_PRIVATE_IN_PROC = 131072
EVENT_TRACE_MODE_RESERVED = 1048576
EVENT_TRACE_NO_PER_PROCESSOR_BUFFERING = 268435456
EVENT_TRACE_SYSTEM_LOGGER_MODE = 33554432
EVENT_TRACE_ADDTO_TRIAGE_DUMP = 2147483648
EVENT_TRACE_STOP_ON_HYBRID_SHUTDOWN = 4194304
EVENT_TRACE_PERSIST_ON_HYBRID_SHUTDOWN = 8388608
EVENT_TRACE_INDEPENDENT_SESSION_MODE = 134217728
EVENT_TRACE_COMPRESSED_MODE = 67108864
EVENT_TRACE_CONTROL_INCREMENT_FILE = 4
EVENT_TRACE_CONTROL_CONVERT_TO_REALTIME = 5
TRACE_MESSAGE_PERFORMANCE_TIMESTAMP = 16
TRACE_MESSAGE_POINTER32 = 64
TRACE_MESSAGE_POINTER64 = 128
TRACE_MESSAGE_FLAG_MASK = 65535
EVENT_TRACE_USE_PROCTIME = 1
EVENT_TRACE_USE_NOCPUTIME = 2
TRACE_HEADER_FLAG_USE_TIMESTAMP = 512
TRACE_HEADER_FLAG_TRACED_GUID = 131072
TRACE_HEADER_FLAG_LOG_WNODE = 262144
TRACE_HEADER_FLAG_USE_GUID_PTR = 524288
TRACE_HEADER_FLAG_USE_MOF_PTR = 1048576
SYSTEM_ALPC_KW_GENERAL = 1
SYSTEM_CONFIG_KW_SYSTEM = 1
SYSTEM_CONFIG_KW_GRAPHICS = 2
SYSTEM_CONFIG_KW_STORAGE = 4
SYSTEM_CONFIG_KW_NETWORK = 8
SYSTEM_CONFIG_KW_SERVICES = 16
SYSTEM_CONFIG_KW_PNP = 32
SYSTEM_CONFIG_KW_OPTICAL = 64
SYSTEM_CPU_KW_CONFIG = 1
SYSTEM_CPU_KW_CACHE_FLUSH = 2
SYSTEM_CPU_KW_SPEC_CONTROL = 4
SYSTEM_HYPERVISOR_KW_PROFILE = 1
SYSTEM_HYPERVISOR_KW_CALLOUTS = 2
SYSTEM_HYPERVISOR_KW_VTL_CHANGE = 4
SYSTEM_INTERRUPT_KW_GENERAL = 1
SYSTEM_INTERRUPT_KW_CLOCK_INTERRUPT = 2
SYSTEM_INTERRUPT_KW_DPC = 4
SYSTEM_INTERRUPT_KW_DPC_QUEUE = 8
SYSTEM_INTERRUPT_KW_WDF_DPC = 16
SYSTEM_INTERRUPT_KW_WDF_INTERRUPT = 32
SYSTEM_INTERRUPT_KW_IPI = 64
SYSTEM_IO_KW_DISK = 1
SYSTEM_IO_KW_DISK_INIT = 2
SYSTEM_IO_KW_FILENAME = 4
SYSTEM_IO_KW_SPLIT = 8
SYSTEM_IO_KW_FILE = 16
SYSTEM_IO_KW_OPTICAL = 32
SYSTEM_IO_KW_OPTICAL_INIT = 64
SYSTEM_IO_KW_DRIVERS = 128
SYSTEM_IO_KW_CC = 256
SYSTEM_IO_KW_NETWORK = 512
SYSTEM_IOFILTER_KW_GENERAL = 1
SYSTEM_IOFILTER_KW_INIT = 2
SYSTEM_IOFILTER_KW_FASTIO = 4
SYSTEM_IOFILTER_KW_FAILURE = 8
SYSTEM_LOCK_KW_SPINLOCK = 1
SYSTEM_LOCK_KW_SPINLOCK_COUNTERS = 2
SYSTEM_LOCK_KW_SYNC_OBJECTS = 4
SYSTEM_MEMORY_KW_GENERAL = 1
SYSTEM_MEMORY_KW_HARD_FAULTS = 2
SYSTEM_MEMORY_KW_ALL_FAULTS = 4
SYSTEM_MEMORY_KW_POOL = 8
SYSTEM_MEMORY_KW_MEMINFO = 16
SYSTEM_MEMORY_KW_PFSECTION = 32
SYSTEM_MEMORY_KW_MEMINFO_WS = 64
SYSTEM_MEMORY_KW_HEAP = 128
SYSTEM_MEMORY_KW_WS = 256
SYSTEM_MEMORY_KW_CONTMEM_GEN = 512
SYSTEM_MEMORY_KW_VIRTUAL_ALLOC = 1024
SYSTEM_MEMORY_KW_FOOTPRINT = 2048
SYSTEM_MEMORY_KW_SESSION = 4096
SYSTEM_MEMORY_KW_REFSET = 8192
SYSTEM_MEMORY_KW_VAMAP = 16384
SYSTEM_MEMORY_KW_NONTRADEABLE = 32768
SYSTEM_OBJECT_KW_GENERAL = 1
SYSTEM_OBJECT_KW_HANDLE = 2
SYSTEM_POWER_KW_GENERAL = 1
SYSTEM_POWER_KW_HIBER_RUNDOWN = 2
SYSTEM_POWER_KW_PROCESSOR_IDLE = 4
SYSTEM_POWER_KW_IDLE_SELECTION = 8
SYSTEM_POWER_KW_PPM_EXIT_LATENCY = 16
SYSTEM_PROCESS_KW_GENERAL = 1
SYSTEM_PROCESS_KW_INSWAP = 2
SYSTEM_PROCESS_KW_FREEZE = 4
SYSTEM_PROCESS_KW_PERF_COUNTER = 8
SYSTEM_PROCESS_KW_WAKE_COUNTER = 16
SYSTEM_PROCESS_KW_WAKE_DROP = 32
SYSTEM_PROCESS_KW_WAKE_EVENT = 64
SYSTEM_PROCESS_KW_DEBUG_EVENTS = 128
SYSTEM_PROCESS_KW_DBGPRINT = 256
SYSTEM_PROCESS_KW_JOB = 512
SYSTEM_PROCESS_KW_WORKER_THREAD = 1024
SYSTEM_PROCESS_KW_THREAD = 2048
SYSTEM_PROCESS_KW_LOADER = 4096
SYSTEM_PROFILE_KW_GENERAL = 1
SYSTEM_PROFILE_KW_PMC_PROFILE = 2
SYSTEM_REGISTRY_KW_GENERAL = 1
SYSTEM_REGISTRY_KW_HIVE = 2
SYSTEM_REGISTRY_KW_NOTIFICATION = 4
SYSTEM_SCHEDULER_KW_XSCHEDULER = 1
SYSTEM_SCHEDULER_KW_DISPATCHER = 2
SYSTEM_SCHEDULER_KW_KERNEL_QUEUE = 4
SYSTEM_SCHEDULER_KW_SHOULD_YIELD = 8
SYSTEM_SCHEDULER_KW_ANTI_STARVATION = 16
SYSTEM_SCHEDULER_KW_LOAD_BALANCER = 32
SYSTEM_SCHEDULER_KW_AFFINITY = 64
SYSTEM_SCHEDULER_KW_PRIORITY = 128
SYSTEM_SCHEDULER_KW_IDEAL_PROCESSOR = 256
SYSTEM_SCHEDULER_KW_CONTEXT_SWITCH = 512
SYSTEM_SCHEDULER_KW_COMPACT_CSWITCH = 1024
SYSTEM_SYSCALL_KW_GENERAL = 1
SYSTEM_TIMER_KW_GENERAL = 1
SYSTEM_TIMER_KW_CLOCK_TIMER = 2
SYSTEM_MEMORY_POOL_FILTER_ID = 1
ETW_NULL_TYPE_VALUE = 0
ETW_OBJECT_TYPE_VALUE = 1
ETW_STRING_TYPE_VALUE = 2
ETW_SBYTE_TYPE_VALUE = 3
ETW_BYTE_TYPE_VALUE = 4
ETW_INT16_TYPE_VALUE = 5
ETW_UINT16_TYPE_VALUE = 6
ETW_INT32_TYPE_VALUE = 7
ETW_UINT32_TYPE_VALUE = 8
ETW_INT64_TYPE_VALUE = 9
ETW_UINT64_TYPE_VALUE = 10
ETW_CHAR_TYPE_VALUE = 11
ETW_SINGLE_TYPE_VALUE = 12
ETW_DOUBLE_TYPE_VALUE = 13
ETW_BOOLEAN_TYPE_VALUE = 14
ETW_DECIMAL_TYPE_VALUE = 15
ETW_GUID_TYPE_VALUE = 101
ETW_ASCIICHAR_TYPE_VALUE = 102
ETW_ASCIISTRING_TYPE_VALUE = 103
ETW_COUNTED_STRING_TYPE_VALUE = 104
ETW_POINTER_TYPE_VALUE = 105
ETW_SIZET_TYPE_VALUE = 106
ETW_HIDDEN_TYPE_VALUE = 107
ETW_BOOL_TYPE_VALUE = 108
ETW_COUNTED_ANSISTRING_TYPE_VALUE = 109
ETW_REVERSED_COUNTED_STRING_TYPE_VALUE = 110
ETW_REVERSED_COUNTED_ANSISTRING_TYPE_VALUE = 111
ETW_NON_NULL_TERMINATED_STRING_TYPE_VALUE = 112
ETW_REDUCED_ANSISTRING_TYPE_VALUE = 113
ETW_REDUCED_STRING_TYPE_VALUE = 114
ETW_SID_TYPE_VALUE = 115
ETW_VARIANT_TYPE_VALUE = 116
ETW_PTVECTOR_TYPE_VALUE = 117
ETW_WMITIME_TYPE_VALUE = 118
ETW_DATETIME_TYPE_VALUE = 119
ETW_REFRENCE_TYPE_VALUE = 120
TRACE_PROVIDER_FLAG_LEGACY = 1
TRACE_PROVIDER_FLAG_PRE_ENABLE = 2
ENABLE_TRACE_PARAMETERS_VERSION = 1
ENABLE_TRACE_PARAMETERS_VERSION_2 = 2
EVENT_MIN_LEVEL = 0
EVENT_MAX_LEVEL = 255
EVENT_ACTIVITY_CTRL_GET_ID = 1
EVENT_ACTIVITY_CTRL_SET_ID = 2
EVENT_ACTIVITY_CTRL_CREATE_ID = 3
EVENT_ACTIVITY_CTRL_GET_SET_ID = 4
EVENT_ACTIVITY_CTRL_CREATE_SET_ID = 5
MAX_EVENT_DATA_DESCRIPTORS = 128
MAX_EVENT_FILTER_DATA_SIZE = 1024
MAX_EVENT_FILTER_PAYLOAD_SIZE = 4096
MAX_EVENT_FILTER_EVENT_NAME_SIZE = 4096
MAX_EVENT_FILTERS_COUNT = 13
MAX_EVENT_FILTER_PID_COUNT = 8
MAX_EVENT_FILTER_EVENT_ID_COUNT = 64
EVENT_FILTER_TYPE_NONE = 0
EVENT_FILTER_TYPE_SCHEMATIZED = 2147483648
EVENT_FILTER_TYPE_SYSTEM_FLAGS = 2147483649
EVENT_FILTER_TYPE_TRACEHANDLE = 2147483650
EVENT_FILTER_TYPE_PID = 2147483652
EVENT_FILTER_TYPE_EXECUTABLE_NAME = 2147483656
EVENT_FILTER_TYPE_PACKAGE_ID = 2147483664
EVENT_FILTER_TYPE_PACKAGE_APP_ID = 2147483680
EVENT_FILTER_TYPE_PAYLOAD = 2147483904
EVENT_FILTER_TYPE_EVENT_ID = 2147484160
EVENT_FILTER_TYPE_EVENT_NAME = 2147484672
EVENT_FILTER_TYPE_STACKWALK = 2147487744
EVENT_FILTER_TYPE_STACKWALK_NAME = 2147491840
EVENT_FILTER_TYPE_STACKWALK_LEVEL_KW = 2147500032
EVENT_FILTER_TYPE_CONTAINER = 2147516416
EVENT_DATA_DESCRIPTOR_TYPE_NONE = 0
EVENT_DATA_DESCRIPTOR_TYPE_EVENT_METADATA = 1
EVENT_DATA_DESCRIPTOR_TYPE_PROVIDER_METADATA = 2
EVENT_DATA_DESCRIPTOR_TYPE_TIMESTAMP_OVERRIDE = 3
EVENT_WRITE_FLAG_NO_FAULTING = 1
EVENT_WRITE_FLAG_INPRIVATE = 2
EVENT_HEADER_EXT_TYPE_RELATED_ACTIVITYID = 1
EVENT_HEADER_EXT_TYPE_SID = 2
EVENT_HEADER_EXT_TYPE_TS_ID = 3
EVENT_HEADER_EXT_TYPE_INSTANCE_INFO = 4
EVENT_HEADER_EXT_TYPE_STACK_TRACE32 = 5
EVENT_HEADER_EXT_TYPE_STACK_TRACE64 = 6
EVENT_HEADER_EXT_TYPE_PEBS_INDEX = 7
EVENT_HEADER_EXT_TYPE_PMC_COUNTERS = 8
EVENT_HEADER_EXT_TYPE_PSM_KEY = 9
EVENT_HEADER_EXT_TYPE_EVENT_KEY = 10
EVENT_HEADER_EXT_TYPE_EVENT_SCHEMA_TL = 11
EVENT_HEADER_EXT_TYPE_PROV_TRAITS = 12
EVENT_HEADER_EXT_TYPE_PROCESS_START_KEY = 13
EVENT_HEADER_EXT_TYPE_CONTROL_GUID = 14
EVENT_HEADER_EXT_TYPE_QPC_DELTA = 15
EVENT_HEADER_EXT_TYPE_CONTAINER_ID = 16
EVENT_HEADER_EXT_TYPE_STACK_KEY32 = 17
EVENT_HEADER_EXT_TYPE_STACK_KEY64 = 18
EVENT_HEADER_EXT_TYPE_MAX = 19
EVENT_HEADER_PROPERTY_XML = 1
EVENT_HEADER_PROPERTY_FORWARDED_XML = 2
EVENT_HEADER_PROPERTY_LEGACY_EVENTLOG = 4
EVENT_HEADER_PROPERTY_RELOGGABLE = 8
EVENT_HEADER_FLAG_EXTENDED_INFO = 1
EVENT_HEADER_FLAG_PRIVATE_SESSION = 2
EVENT_HEADER_FLAG_STRING_ONLY = 4
EVENT_HEADER_FLAG_TRACE_MESSAGE = 8
EVENT_HEADER_FLAG_NO_CPUTIME = 16
EVENT_HEADER_FLAG_32_BIT_HEADER = 32
EVENT_HEADER_FLAG_64_BIT_HEADER = 64
EVENT_HEADER_FLAG_DECODE_GUID = 128
EVENT_HEADER_FLAG_CLASSIC_HEADER = 256
EVENT_HEADER_FLAG_PROCESSOR_INDEX = 512
EVENT_ENABLE_PROPERTY_SID = 1
EVENT_ENABLE_PROPERTY_TS_ID = 2
EVENT_ENABLE_PROPERTY_STACK_TRACE = 4
EVENT_ENABLE_PROPERTY_PSM_KEY = 8
EVENT_ENABLE_PROPERTY_IGNORE_KEYWORD_0 = 16
EVENT_ENABLE_PROPERTY_PROVIDER_GROUP = 32
EVENT_ENABLE_PROPERTY_ENABLE_KEYWORD_0 = 64
EVENT_ENABLE_PROPERTY_PROCESS_START_KEY = 128
EVENT_ENABLE_PROPERTY_EVENT_KEY = 256
EVENT_ENABLE_PROPERTY_EXCLUDE_INPRIVATE = 512
EVENT_ENABLE_PROPERTY_ENABLE_SILOS = 1024
EVENT_ENABLE_PROPERTY_SOURCE_CONTAINER_TRACKING = 2048
PROCESS_TRACE_MODE_REAL_TIME = 256
PROCESS_TRACE_MODE_RAW_TIMESTAMP = 4096
PROCESS_TRACE_MODE_EVENT_RECORD = 268435456
CLSID_TraceRelogger = '7b40792d-05ff-44c4-9058-f440c71f17d4'
TRACE_MESSAGE_FLAGS = UInt32
TRACE_MESSAGE_COMPONENTID = 4
TRACE_MESSAGE_GUID = 2
TRACE_MESSAGE_SEQUENCE = 1
TRACE_MESSAGE_SYSTEMINFO = 32
TRACE_MESSAGE_TIMESTAMP = 8
ENABLECALLBACK_ENABLED_STATE = UInt32
EVENT_CONTROL_CODE_DISABLE_PROVIDER = 0
EVENT_CONTROL_CODE_ENABLE_PROVIDER = 1
EVENT_CONTROL_CODE_CAPTURE_STATE = 2
EVENT_TRACE_CONTROL = UInt32
EVENT_TRACE_CONTROL_FLUSH = 3
EVENT_TRACE_CONTROL_QUERY = 0
EVENT_TRACE_CONTROL_STOP = 1
EVENT_TRACE_CONTROL_UPDATE = 2
EVENT_TRACE_FLAG = UInt32
EVENT_TRACE_FLAG_ALPC = 1048576
EVENT_TRACE_FLAG_CSWITCH = 16
EVENT_TRACE_FLAG_DBGPRINT = 262144
EVENT_TRACE_FLAG_DISK_FILE_IO = 512
EVENT_TRACE_FLAG_DISK_IO = 256
EVENT_TRACE_FLAG_DISK_IO_INIT = 1024
EVENT_TRACE_FLAG_DISPATCHER = 2048
EVENT_TRACE_FLAG_DPC = 32
EVENT_TRACE_FLAG_DRIVER = 8388608
EVENT_TRACE_FLAG_FILE_IO = 33554432
EVENT_TRACE_FLAG_FILE_IO_INIT = 67108864
EVENT_TRACE_FLAG_IMAGE_LOAD = 4
EVENT_TRACE_FLAG_INTERRUPT = 64
EVENT_TRACE_FLAG_JOB = 524288
EVENT_TRACE_FLAG_MEMORY_HARD_FAULTS = 8192
EVENT_TRACE_FLAG_MEMORY_PAGE_FAULTS = 4096
EVENT_TRACE_FLAG_NETWORK_TCPIP = 65536
EVENT_TRACE_FLAG_NO_SYSCONFIG = 268435456
EVENT_TRACE_FLAG_PROCESS = 1
EVENT_TRACE_FLAG_PROCESS_COUNTERS = 8
EVENT_TRACE_FLAG_PROFILE = 16777216
EVENT_TRACE_FLAG_REGISTRY = 131072
EVENT_TRACE_FLAG_SPLIT_IO = 2097152
EVENT_TRACE_FLAG_SYSTEMCALL = 128
EVENT_TRACE_FLAG_THREAD = 2
EVENT_TRACE_FLAG_VAMAP = 32768
EVENT_TRACE_FLAG_VIRTUAL_ALLOC = 16384
TDH_HANDLE = IntPtr
def _define_WNODE_HEADER_head():
    class WNODE_HEADER(Structure):
        pass
    return WNODE_HEADER
def _define_WNODE_HEADER():
    WNODE_HEADER = win32more.System.Diagnostics.Etw.WNODE_HEADER_head
    class WNODE_HEADER__Anonymous2_e__Union(Union):
        pass
    WNODE_HEADER__Anonymous2_e__Union._fields_ = [
        ("CountLost", UInt32),
        ("KernelHandle", win32more.Foundation.HANDLE),
        ("TimeStamp", win32more.Foundation.LARGE_INTEGER),
    ]
    class WNODE_HEADER__Anonymous1_e__Union(Union):
        pass
    class WNODE_HEADER__Anonymous1_e__Union__Anonymous_e__Struct(Structure):
        pass
    WNODE_HEADER__Anonymous1_e__Union__Anonymous_e__Struct._fields_ = [
        ("Version", UInt32),
        ("Linkage", UInt32),
    ]
    WNODE_HEADER__Anonymous1_e__Union._anonymous_ = [
        'Anonymous',
    ]
    WNODE_HEADER__Anonymous1_e__Union._fields_ = [
        ("HistoricalContext", UInt64),
        ("Anonymous", WNODE_HEADER__Anonymous1_e__Union__Anonymous_e__Struct),
    ]
    WNODE_HEADER._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
    ]
    WNODE_HEADER._fields_ = [
        ("BufferSize", UInt32),
        ("ProviderId", UInt32),
        ("Anonymous1", WNODE_HEADER__Anonymous1_e__Union),
        ("Anonymous2", WNODE_HEADER__Anonymous2_e__Union),
        ("Guid", Guid),
        ("ClientContext", UInt32),
        ("Flags", UInt32),
    ]
    return WNODE_HEADER
def _define_OFFSETINSTANCEDATAANDLENGTH_head():
    class OFFSETINSTANCEDATAANDLENGTH(Structure):
        pass
    return OFFSETINSTANCEDATAANDLENGTH
def _define_OFFSETINSTANCEDATAANDLENGTH():
    OFFSETINSTANCEDATAANDLENGTH = win32more.System.Diagnostics.Etw.OFFSETINSTANCEDATAANDLENGTH_head
    OFFSETINSTANCEDATAANDLENGTH._fields_ = [
        ("OffsetInstanceData", UInt32),
        ("LengthInstanceData", UInt32),
    ]
    return OFFSETINSTANCEDATAANDLENGTH
def _define_WNODE_ALL_DATA_head():
    class WNODE_ALL_DATA(Structure):
        pass
    return WNODE_ALL_DATA
def _define_WNODE_ALL_DATA():
    WNODE_ALL_DATA = win32more.System.Diagnostics.Etw.WNODE_ALL_DATA_head
    class WNODE_ALL_DATA__Anonymous_e__Union(Union):
        pass
    WNODE_ALL_DATA__Anonymous_e__Union._fields_ = [
        ("FixedInstanceSize", UInt32),
        ("OffsetInstanceDataAndLength", win32more.System.Diagnostics.Etw.OFFSETINSTANCEDATAANDLENGTH * 0),
    ]
    WNODE_ALL_DATA._anonymous_ = [
        'Anonymous',
    ]
    WNODE_ALL_DATA._fields_ = [
        ("WnodeHeader", win32more.System.Diagnostics.Etw.WNODE_HEADER),
        ("DataBlockOffset", UInt32),
        ("InstanceCount", UInt32),
        ("OffsetInstanceNameOffsets", UInt32),
        ("Anonymous", WNODE_ALL_DATA__Anonymous_e__Union),
    ]
    return WNODE_ALL_DATA
def _define_WNODE_SINGLE_INSTANCE_head():
    class WNODE_SINGLE_INSTANCE(Structure):
        pass
    return WNODE_SINGLE_INSTANCE
def _define_WNODE_SINGLE_INSTANCE():
    WNODE_SINGLE_INSTANCE = win32more.System.Diagnostics.Etw.WNODE_SINGLE_INSTANCE_head
    WNODE_SINGLE_INSTANCE._fields_ = [
        ("WnodeHeader", win32more.System.Diagnostics.Etw.WNODE_HEADER),
        ("OffsetInstanceName", UInt32),
        ("InstanceIndex", UInt32),
        ("DataBlockOffset", UInt32),
        ("SizeDataBlock", UInt32),
        ("VariableData", Byte * 0),
    ]
    return WNODE_SINGLE_INSTANCE
def _define_WNODE_SINGLE_ITEM_head():
    class WNODE_SINGLE_ITEM(Structure):
        pass
    return WNODE_SINGLE_ITEM
def _define_WNODE_SINGLE_ITEM():
    WNODE_SINGLE_ITEM = win32more.System.Diagnostics.Etw.WNODE_SINGLE_ITEM_head
    WNODE_SINGLE_ITEM._fields_ = [
        ("WnodeHeader", win32more.System.Diagnostics.Etw.WNODE_HEADER),
        ("OffsetInstanceName", UInt32),
        ("InstanceIndex", UInt32),
        ("ItemId", UInt32),
        ("DataBlockOffset", UInt32),
        ("SizeDataItem", UInt32),
        ("VariableData", Byte * 0),
    ]
    return WNODE_SINGLE_ITEM
def _define_WNODE_METHOD_ITEM_head():
    class WNODE_METHOD_ITEM(Structure):
        pass
    return WNODE_METHOD_ITEM
def _define_WNODE_METHOD_ITEM():
    WNODE_METHOD_ITEM = win32more.System.Diagnostics.Etw.WNODE_METHOD_ITEM_head
    WNODE_METHOD_ITEM._fields_ = [
        ("WnodeHeader", win32more.System.Diagnostics.Etw.WNODE_HEADER),
        ("OffsetInstanceName", UInt32),
        ("InstanceIndex", UInt32),
        ("MethodId", UInt32),
        ("DataBlockOffset", UInt32),
        ("SizeDataBlock", UInt32),
        ("VariableData", Byte * 0),
    ]
    return WNODE_METHOD_ITEM
def _define_WNODE_EVENT_ITEM_head():
    class WNODE_EVENT_ITEM(Structure):
        pass
    return WNODE_EVENT_ITEM
def _define_WNODE_EVENT_ITEM():
    WNODE_EVENT_ITEM = win32more.System.Diagnostics.Etw.WNODE_EVENT_ITEM_head
    WNODE_EVENT_ITEM._fields_ = [
        ("WnodeHeader", win32more.System.Diagnostics.Etw.WNODE_HEADER),
    ]
    return WNODE_EVENT_ITEM
def _define_WNODE_EVENT_REFERENCE_head():
    class WNODE_EVENT_REFERENCE(Structure):
        pass
    return WNODE_EVENT_REFERENCE
def _define_WNODE_EVENT_REFERENCE():
    WNODE_EVENT_REFERENCE = win32more.System.Diagnostics.Etw.WNODE_EVENT_REFERENCE_head
    class WNODE_EVENT_REFERENCE__Anonymous_e__Union(Union):
        pass
    WNODE_EVENT_REFERENCE__Anonymous_e__Union._fields_ = [
        ("TargetInstanceIndex", UInt32),
        ("TargetInstanceName", Char * 0),
    ]
    WNODE_EVENT_REFERENCE._anonymous_ = [
        'Anonymous',
    ]
    WNODE_EVENT_REFERENCE._fields_ = [
        ("WnodeHeader", win32more.System.Diagnostics.Etw.WNODE_HEADER),
        ("TargetGuid", Guid),
        ("TargetDataBlockSize", UInt32),
        ("Anonymous", WNODE_EVENT_REFERENCE__Anonymous_e__Union),
    ]
    return WNODE_EVENT_REFERENCE
def _define_WNODE_TOO_SMALL_head():
    class WNODE_TOO_SMALL(Structure):
        pass
    return WNODE_TOO_SMALL
def _define_WNODE_TOO_SMALL():
    WNODE_TOO_SMALL = win32more.System.Diagnostics.Etw.WNODE_TOO_SMALL_head
    WNODE_TOO_SMALL._fields_ = [
        ("WnodeHeader", win32more.System.Diagnostics.Etw.WNODE_HEADER),
        ("SizeNeeded", UInt32),
    ]
    return WNODE_TOO_SMALL
def _define_WMIREGGUIDW_head():
    class WMIREGGUIDW(Structure):
        pass
    return WMIREGGUIDW
def _define_WMIREGGUIDW():
    WMIREGGUIDW = win32more.System.Diagnostics.Etw.WMIREGGUIDW_head
    class WMIREGGUIDW__Anonymous_e__Union(Union):
        pass
    WMIREGGUIDW__Anonymous_e__Union._fields_ = [
        ("InstanceNameList", UInt32),
        ("BaseNameOffset", UInt32),
        ("Pdo", UIntPtr),
        ("InstanceInfo", UIntPtr),
    ]
    WMIREGGUIDW._anonymous_ = [
        'Anonymous',
    ]
    WMIREGGUIDW._fields_ = [
        ("Guid", Guid),
        ("Flags", UInt32),
        ("InstanceCount", UInt32),
        ("Anonymous", WMIREGGUIDW__Anonymous_e__Union),
    ]
    return WMIREGGUIDW
def _define_WMIREGINFOW_head():
    class WMIREGINFOW(Structure):
        pass
    return WMIREGINFOW
def _define_WMIREGINFOW():
    WMIREGINFOW = win32more.System.Diagnostics.Etw.WMIREGINFOW_head
    WMIREGINFOW._fields_ = [
        ("BufferSize", UInt32),
        ("NextWmiRegInfo", UInt32),
        ("RegistryPath", UInt32),
        ("MofResourceName", UInt32),
        ("GuidCount", UInt32),
        ("WmiRegGuid", win32more.System.Diagnostics.Etw.WMIREGGUIDW * 0),
    ]
    return WMIREGINFOW
WMIDPREQUESTCODE = Int32
WMI_GET_ALL_DATA = 0
WMI_GET_SINGLE_INSTANCE = 1
WMI_SET_SINGLE_INSTANCE = 2
WMI_SET_SINGLE_ITEM = 3
WMI_ENABLE_EVENTS = 4
WMI_DISABLE_EVENTS = 5
WMI_ENABLE_COLLECTION = 6
WMI_DISABLE_COLLECTION = 7
WMI_REGINFO = 8
WMI_EXECUTE_METHOD = 9
WMI_CAPTURE_STATE = 10
ETW_COMPRESSION_RESUMPTION_MODE = Int32
ETW_COMPRESSION_RESUMPTION_MODE_EtwCompressionModeRestart = 0
ETW_COMPRESSION_RESUMPTION_MODE_EtwCompressionModeNoDisable = 1
ETW_COMPRESSION_RESUMPTION_MODE_EtwCompressionModeNoRestart = 2
def _define_EVENT_TRACE_HEADER_head():
    class EVENT_TRACE_HEADER(Structure):
        pass
    return EVENT_TRACE_HEADER
def _define_EVENT_TRACE_HEADER():
    EVENT_TRACE_HEADER = win32more.System.Diagnostics.Etw.EVENT_TRACE_HEADER_head
    class EVENT_TRACE_HEADER__Anonymous4_e__Union(Union):
        pass
    class EVENT_TRACE_HEADER__Anonymous4_e__Union__Anonymous2_e__Struct(Structure):
        pass
    EVENT_TRACE_HEADER__Anonymous4_e__Union__Anonymous2_e__Struct._fields_ = [
        ("ClientContext", UInt32),
        ("Flags", UInt32),
    ]
    class EVENT_TRACE_HEADER__Anonymous4_e__Union__Anonymous1_e__Struct(Structure):
        pass
    EVENT_TRACE_HEADER__Anonymous4_e__Union__Anonymous1_e__Struct._fields_ = [
        ("KernelTime", UInt32),
        ("UserTime", UInt32),
    ]
    EVENT_TRACE_HEADER__Anonymous4_e__Union._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
    ]
    EVENT_TRACE_HEADER__Anonymous4_e__Union._fields_ = [
        ("Anonymous1", EVENT_TRACE_HEADER__Anonymous4_e__Union__Anonymous1_e__Struct),
        ("ProcessorTime", UInt64),
        ("Anonymous2", EVENT_TRACE_HEADER__Anonymous4_e__Union__Anonymous2_e__Struct),
    ]
    class EVENT_TRACE_HEADER__Anonymous2_e__Union(Union):
        pass
    class EVENT_TRACE_HEADER__Anonymous2_e__Union__Class_e__Struct(Structure):
        pass
    EVENT_TRACE_HEADER__Anonymous2_e__Union__Class_e__Struct._fields_ = [
        ("Type", Byte),
        ("Level", Byte),
        ("Version", UInt16),
    ]
    EVENT_TRACE_HEADER__Anonymous2_e__Union._fields_ = [
        ("Version", UInt32),
        ("Class", EVENT_TRACE_HEADER__Anonymous2_e__Union__Class_e__Struct),
    ]
    class EVENT_TRACE_HEADER__Anonymous1_e__Union(Union):
        pass
    class EVENT_TRACE_HEADER__Anonymous1_e__Union__Anonymous_e__Struct(Structure):
        pass
    EVENT_TRACE_HEADER__Anonymous1_e__Union__Anonymous_e__Struct._fields_ = [
        ("HeaderType", Byte),
        ("MarkerFlags", Byte),
    ]
    EVENT_TRACE_HEADER__Anonymous1_e__Union._anonymous_ = [
        'Anonymous',
    ]
    EVENT_TRACE_HEADER__Anonymous1_e__Union._fields_ = [
        ("FieldTypeFlags", UInt16),
        ("Anonymous", EVENT_TRACE_HEADER__Anonymous1_e__Union__Anonymous_e__Struct),
    ]
    class EVENT_TRACE_HEADER__Anonymous3_e__Union(Union):
        pass
    EVENT_TRACE_HEADER__Anonymous3_e__Union._fields_ = [
        ("Guid", Guid),
        ("GuidPtr", UInt64),
    ]
    EVENT_TRACE_HEADER._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
        'Anonymous3',
        'Anonymous4',
    ]
    EVENT_TRACE_HEADER._fields_ = [
        ("Size", UInt16),
        ("Anonymous1", EVENT_TRACE_HEADER__Anonymous1_e__Union),
        ("Anonymous2", EVENT_TRACE_HEADER__Anonymous2_e__Union),
        ("ThreadId", UInt32),
        ("ProcessId", UInt32),
        ("TimeStamp", win32more.Foundation.LARGE_INTEGER),
        ("Anonymous3", EVENT_TRACE_HEADER__Anonymous3_e__Union),
        ("Anonymous4", EVENT_TRACE_HEADER__Anonymous4_e__Union),
    ]
    return EVENT_TRACE_HEADER
def _define_EVENT_INSTANCE_HEADER_head():
    class EVENT_INSTANCE_HEADER(Structure):
        pass
    return EVENT_INSTANCE_HEADER
def _define_EVENT_INSTANCE_HEADER():
    EVENT_INSTANCE_HEADER = win32more.System.Diagnostics.Etw.EVENT_INSTANCE_HEADER_head
    class EVENT_INSTANCE_HEADER__Anonymous3_e__Union(Union):
        pass
    class EVENT_INSTANCE_HEADER__Anonymous3_e__Union__Anonymous2_e__Struct(Structure):
        pass
    EVENT_INSTANCE_HEADER__Anonymous3_e__Union__Anonymous2_e__Struct._fields_ = [
        ("EventId", UInt32),
        ("Flags", UInt32),
    ]
    class EVENT_INSTANCE_HEADER__Anonymous3_e__Union__Anonymous1_e__Struct(Structure):
        pass
    EVENT_INSTANCE_HEADER__Anonymous3_e__Union__Anonymous1_e__Struct._fields_ = [
        ("KernelTime", UInt32),
        ("UserTime", UInt32),
    ]
    EVENT_INSTANCE_HEADER__Anonymous3_e__Union._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
    ]
    EVENT_INSTANCE_HEADER__Anonymous3_e__Union._fields_ = [
        ("Anonymous1", EVENT_INSTANCE_HEADER__Anonymous3_e__Union__Anonymous1_e__Struct),
        ("ProcessorTime", UInt64),
        ("Anonymous2", EVENT_INSTANCE_HEADER__Anonymous3_e__Union__Anonymous2_e__Struct),
    ]
    class EVENT_INSTANCE_HEADER__Anonymous2_e__Union(Union):
        pass
    class EVENT_INSTANCE_HEADER__Anonymous2_e__Union__Class_e__Struct(Structure):
        pass
    EVENT_INSTANCE_HEADER__Anonymous2_e__Union__Class_e__Struct._fields_ = [
        ("Type", Byte),
        ("Level", Byte),
        ("Version", UInt16),
    ]
    EVENT_INSTANCE_HEADER__Anonymous2_e__Union._fields_ = [
        ("Version", UInt32),
        ("Class", EVENT_INSTANCE_HEADER__Anonymous2_e__Union__Class_e__Struct),
    ]
    class EVENT_INSTANCE_HEADER__Anonymous1_e__Union(Union):
        pass
    class EVENT_INSTANCE_HEADER__Anonymous1_e__Union__Anonymous_e__Struct(Structure):
        pass
    EVENT_INSTANCE_HEADER__Anonymous1_e__Union__Anonymous_e__Struct._fields_ = [
        ("HeaderType", Byte),
        ("MarkerFlags", Byte),
    ]
    EVENT_INSTANCE_HEADER__Anonymous1_e__Union._anonymous_ = [
        'Anonymous',
    ]
    EVENT_INSTANCE_HEADER__Anonymous1_e__Union._fields_ = [
        ("FieldTypeFlags", UInt16),
        ("Anonymous", EVENT_INSTANCE_HEADER__Anonymous1_e__Union__Anonymous_e__Struct),
    ]
    EVENT_INSTANCE_HEADER._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
        'Anonymous3',
    ]
    EVENT_INSTANCE_HEADER._fields_ = [
        ("Size", UInt16),
        ("Anonymous1", EVENT_INSTANCE_HEADER__Anonymous1_e__Union),
        ("Anonymous2", EVENT_INSTANCE_HEADER__Anonymous2_e__Union),
        ("ThreadId", UInt32),
        ("ProcessId", UInt32),
        ("TimeStamp", win32more.Foundation.LARGE_INTEGER),
        ("RegHandle", UInt64),
        ("InstanceId", UInt32),
        ("ParentInstanceId", UInt32),
        ("Anonymous3", EVENT_INSTANCE_HEADER__Anonymous3_e__Union),
        ("ParentRegHandle", UInt64),
    ]
    return EVENT_INSTANCE_HEADER
def _define_MOF_FIELD_head():
    class MOF_FIELD(Structure):
        pass
    return MOF_FIELD
def _define_MOF_FIELD():
    MOF_FIELD = win32more.System.Diagnostics.Etw.MOF_FIELD_head
    MOF_FIELD._fields_ = [
        ("DataPtr", UInt64),
        ("Length", UInt32),
        ("DataType", UInt32),
    ]
    return MOF_FIELD
def _define_TRACE_LOGFILE_HEADER_head():
    class TRACE_LOGFILE_HEADER(Structure):
        pass
    return TRACE_LOGFILE_HEADER
def _define_TRACE_LOGFILE_HEADER():
    TRACE_LOGFILE_HEADER = win32more.System.Diagnostics.Etw.TRACE_LOGFILE_HEADER_head
    class TRACE_LOGFILE_HEADER__Anonymous2_e__Union(Union):
        pass
    class TRACE_LOGFILE_HEADER__Anonymous2_e__Union__Anonymous_e__Struct(Structure):
        pass
    TRACE_LOGFILE_HEADER__Anonymous2_e__Union__Anonymous_e__Struct._fields_ = [
        ("StartBuffers", UInt32),
        ("PointerSize", UInt32),
        ("EventsLost", UInt32),
        ("CpuSpeedInMHz", UInt32),
    ]
    TRACE_LOGFILE_HEADER__Anonymous2_e__Union._anonymous_ = [
        'Anonymous',
    ]
    TRACE_LOGFILE_HEADER__Anonymous2_e__Union._fields_ = [
        ("LogInstanceGuid", Guid),
        ("Anonymous", TRACE_LOGFILE_HEADER__Anonymous2_e__Union__Anonymous_e__Struct),
    ]
    class TRACE_LOGFILE_HEADER__Anonymous1_e__Union(Union):
        pass
    class TRACE_LOGFILE_HEADER__Anonymous1_e__Union__VersionDetail_e__Struct(Structure):
        pass
    TRACE_LOGFILE_HEADER__Anonymous1_e__Union__VersionDetail_e__Struct._fields_ = [
        ("MajorVersion", Byte),
        ("MinorVersion", Byte),
        ("SubVersion", Byte),
        ("SubMinorVersion", Byte),
    ]
    TRACE_LOGFILE_HEADER__Anonymous1_e__Union._fields_ = [
        ("Version", UInt32),
        ("VersionDetail", TRACE_LOGFILE_HEADER__Anonymous1_e__Union__VersionDetail_e__Struct),
    ]
    TRACE_LOGFILE_HEADER._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
    ]
    TRACE_LOGFILE_HEADER._fields_ = [
        ("BufferSize", UInt32),
        ("Anonymous1", TRACE_LOGFILE_HEADER__Anonymous1_e__Union),
        ("ProviderVersion", UInt32),
        ("NumberOfProcessors", UInt32),
        ("EndTime", win32more.Foundation.LARGE_INTEGER),
        ("TimerResolution", UInt32),
        ("MaximumFileSize", UInt32),
        ("LogFileMode", UInt32),
        ("BuffersWritten", UInt32),
        ("Anonymous2", TRACE_LOGFILE_HEADER__Anonymous2_e__Union),
        ("LoggerName", win32more.Foundation.PWSTR),
        ("LogFileName", win32more.Foundation.PWSTR),
        ("TimeZone", win32more.System.Time.TIME_ZONE_INFORMATION),
        ("BootTime", win32more.Foundation.LARGE_INTEGER),
        ("PerfFreq", win32more.Foundation.LARGE_INTEGER),
        ("StartTime", win32more.Foundation.LARGE_INTEGER),
        ("ReservedFlags", UInt32),
        ("BuffersLost", UInt32),
    ]
    return TRACE_LOGFILE_HEADER
def _define_TRACE_LOGFILE_HEADER32_head():
    class TRACE_LOGFILE_HEADER32(Structure):
        pass
    return TRACE_LOGFILE_HEADER32
def _define_TRACE_LOGFILE_HEADER32():
    TRACE_LOGFILE_HEADER32 = win32more.System.Diagnostics.Etw.TRACE_LOGFILE_HEADER32_head
    class TRACE_LOGFILE_HEADER32__Anonymous2_e__Union(Union):
        pass
    class TRACE_LOGFILE_HEADER32__Anonymous2_e__Union__Anonymous_e__Struct(Structure):
        pass
    TRACE_LOGFILE_HEADER32__Anonymous2_e__Union__Anonymous_e__Struct._fields_ = [
        ("StartBuffers", UInt32),
        ("PointerSize", UInt32),
        ("EventsLost", UInt32),
        ("CpuSpeedInMHz", UInt32),
    ]
    TRACE_LOGFILE_HEADER32__Anonymous2_e__Union._anonymous_ = [
        'Anonymous',
    ]
    TRACE_LOGFILE_HEADER32__Anonymous2_e__Union._fields_ = [
        ("LogInstanceGuid", Guid),
        ("Anonymous", TRACE_LOGFILE_HEADER32__Anonymous2_e__Union__Anonymous_e__Struct),
    ]
    class TRACE_LOGFILE_HEADER32__Anonymous1_e__Union(Union):
        pass
    class TRACE_LOGFILE_HEADER32__Anonymous1_e__Union__VersionDetail_e__Struct(Structure):
        pass
    TRACE_LOGFILE_HEADER32__Anonymous1_e__Union__VersionDetail_e__Struct._fields_ = [
        ("MajorVersion", Byte),
        ("MinorVersion", Byte),
        ("SubVersion", Byte),
        ("SubMinorVersion", Byte),
    ]
    TRACE_LOGFILE_HEADER32__Anonymous1_e__Union._fields_ = [
        ("Version", UInt32),
        ("VersionDetail", TRACE_LOGFILE_HEADER32__Anonymous1_e__Union__VersionDetail_e__Struct),
    ]
    TRACE_LOGFILE_HEADER32._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
    ]
    TRACE_LOGFILE_HEADER32._fields_ = [
        ("BufferSize", UInt32),
        ("Anonymous1", TRACE_LOGFILE_HEADER32__Anonymous1_e__Union),
        ("ProviderVersion", UInt32),
        ("NumberOfProcessors", UInt32),
        ("EndTime", win32more.Foundation.LARGE_INTEGER),
        ("TimerResolution", UInt32),
        ("MaximumFileSize", UInt32),
        ("LogFileMode", UInt32),
        ("BuffersWritten", UInt32),
        ("Anonymous2", TRACE_LOGFILE_HEADER32__Anonymous2_e__Union),
        ("LoggerName", UInt32),
        ("LogFileName", UInt32),
        ("TimeZone", win32more.System.Time.TIME_ZONE_INFORMATION),
        ("BootTime", win32more.Foundation.LARGE_INTEGER),
        ("PerfFreq", win32more.Foundation.LARGE_INTEGER),
        ("StartTime", win32more.Foundation.LARGE_INTEGER),
        ("ReservedFlags", UInt32),
        ("BuffersLost", UInt32),
    ]
    return TRACE_LOGFILE_HEADER32
def _define_TRACE_LOGFILE_HEADER64_head():
    class TRACE_LOGFILE_HEADER64(Structure):
        pass
    return TRACE_LOGFILE_HEADER64
def _define_TRACE_LOGFILE_HEADER64():
    TRACE_LOGFILE_HEADER64 = win32more.System.Diagnostics.Etw.TRACE_LOGFILE_HEADER64_head
    class TRACE_LOGFILE_HEADER64__Anonymous2_e__Union(Union):
        pass
    class TRACE_LOGFILE_HEADER64__Anonymous2_e__Union__Anonymous_e__Struct(Structure):
        pass
    TRACE_LOGFILE_HEADER64__Anonymous2_e__Union__Anonymous_e__Struct._fields_ = [
        ("StartBuffers", UInt32),
        ("PointerSize", UInt32),
        ("EventsLost", UInt32),
        ("CpuSpeedInMHz", UInt32),
    ]
    TRACE_LOGFILE_HEADER64__Anonymous2_e__Union._anonymous_ = [
        'Anonymous',
    ]
    TRACE_LOGFILE_HEADER64__Anonymous2_e__Union._fields_ = [
        ("LogInstanceGuid", Guid),
        ("Anonymous", TRACE_LOGFILE_HEADER64__Anonymous2_e__Union__Anonymous_e__Struct),
    ]
    class TRACE_LOGFILE_HEADER64__Anonymous1_e__Union(Union):
        pass
    class TRACE_LOGFILE_HEADER64__Anonymous1_e__Union__VersionDetail_e__Struct(Structure):
        pass
    TRACE_LOGFILE_HEADER64__Anonymous1_e__Union__VersionDetail_e__Struct._fields_ = [
        ("MajorVersion", Byte),
        ("MinorVersion", Byte),
        ("SubVersion", Byte),
        ("SubMinorVersion", Byte),
    ]
    TRACE_LOGFILE_HEADER64__Anonymous1_e__Union._fields_ = [
        ("Version", UInt32),
        ("VersionDetail", TRACE_LOGFILE_HEADER64__Anonymous1_e__Union__VersionDetail_e__Struct),
    ]
    TRACE_LOGFILE_HEADER64._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
    ]
    TRACE_LOGFILE_HEADER64._fields_ = [
        ("BufferSize", UInt32),
        ("Anonymous1", TRACE_LOGFILE_HEADER64__Anonymous1_e__Union),
        ("ProviderVersion", UInt32),
        ("NumberOfProcessors", UInt32),
        ("EndTime", win32more.Foundation.LARGE_INTEGER),
        ("TimerResolution", UInt32),
        ("MaximumFileSize", UInt32),
        ("LogFileMode", UInt32),
        ("BuffersWritten", UInt32),
        ("Anonymous2", TRACE_LOGFILE_HEADER64__Anonymous2_e__Union),
        ("LoggerName", UInt64),
        ("LogFileName", UInt64),
        ("TimeZone", win32more.System.Time.TIME_ZONE_INFORMATION),
        ("BootTime", win32more.Foundation.LARGE_INTEGER),
        ("PerfFreq", win32more.Foundation.LARGE_INTEGER),
        ("StartTime", win32more.Foundation.LARGE_INTEGER),
        ("ReservedFlags", UInt32),
        ("BuffersLost", UInt32),
    ]
    return TRACE_LOGFILE_HEADER64
def _define_EVENT_INSTANCE_INFO_head():
    class EVENT_INSTANCE_INFO(Structure):
        pass
    return EVENT_INSTANCE_INFO
def _define_EVENT_INSTANCE_INFO():
    EVENT_INSTANCE_INFO = win32more.System.Diagnostics.Etw.EVENT_INSTANCE_INFO_head
    EVENT_INSTANCE_INFO._fields_ = [
        ("RegHandle", win32more.Foundation.HANDLE),
        ("InstanceId", UInt32),
    ]
    return EVENT_INSTANCE_INFO
def _define_EVENT_TRACE_PROPERTIES_head():
    class EVENT_TRACE_PROPERTIES(Structure):
        pass
    return EVENT_TRACE_PROPERTIES
def _define_EVENT_TRACE_PROPERTIES():
    EVENT_TRACE_PROPERTIES = win32more.System.Diagnostics.Etw.EVENT_TRACE_PROPERTIES_head
    class EVENT_TRACE_PROPERTIES__Anonymous_e__Union(Union):
        pass
    EVENT_TRACE_PROPERTIES__Anonymous_e__Union._fields_ = [
        ("AgeLimit", Int32),
        ("FlushThreshold", Int32),
    ]
    EVENT_TRACE_PROPERTIES._anonymous_ = [
        'Anonymous',
    ]
    EVENT_TRACE_PROPERTIES._fields_ = [
        ("Wnode", win32more.System.Diagnostics.Etw.WNODE_HEADER),
        ("BufferSize", UInt32),
        ("MinimumBuffers", UInt32),
        ("MaximumBuffers", UInt32),
        ("MaximumFileSize", UInt32),
        ("LogFileMode", UInt32),
        ("FlushTimer", UInt32),
        ("EnableFlags", win32more.System.Diagnostics.Etw.EVENT_TRACE_FLAG),
        ("Anonymous", EVENT_TRACE_PROPERTIES__Anonymous_e__Union),
        ("NumberOfBuffers", UInt32),
        ("FreeBuffers", UInt32),
        ("EventsLost", UInt32),
        ("BuffersWritten", UInt32),
        ("LogBuffersLost", UInt32),
        ("RealTimeBuffersLost", UInt32),
        ("LoggerThreadId", win32more.Foundation.HANDLE),
        ("LogFileNameOffset", UInt32),
        ("LoggerNameOffset", UInt32),
    ]
    return EVENT_TRACE_PROPERTIES
def _define_EVENT_TRACE_PROPERTIES_V2_head():
    class EVENT_TRACE_PROPERTIES_V2(Structure):
        pass
    return EVENT_TRACE_PROPERTIES_V2
def _define_EVENT_TRACE_PROPERTIES_V2():
    EVENT_TRACE_PROPERTIES_V2 = win32more.System.Diagnostics.Etw.EVENT_TRACE_PROPERTIES_V2_head
    class EVENT_TRACE_PROPERTIES_V2__Anonymous3_e__Union(Union):
        pass
    class EVENT_TRACE_PROPERTIES_V2__Anonymous3_e__Union__Anonymous_e__Struct(Structure):
        pass
    EVENT_TRACE_PROPERTIES_V2__Anonymous3_e__Union__Anonymous_e__Struct._fields_ = [
        ("_bitfield", UInt32),
    ]
    EVENT_TRACE_PROPERTIES_V2__Anonymous3_e__Union._anonymous_ = [
        'Anonymous',
    ]
    EVENT_TRACE_PROPERTIES_V2__Anonymous3_e__Union._fields_ = [
        ("Anonymous", EVENT_TRACE_PROPERTIES_V2__Anonymous3_e__Union__Anonymous_e__Struct),
        ("V2Options", UInt64),
    ]
    class EVENT_TRACE_PROPERTIES_V2__Anonymous2_e__Union(Union):
        pass
    class EVENT_TRACE_PROPERTIES_V2__Anonymous2_e__Union__Anonymous_e__Struct(Structure):
        pass
    EVENT_TRACE_PROPERTIES_V2__Anonymous2_e__Union__Anonymous_e__Struct._fields_ = [
        ("_bitfield", UInt32),
    ]
    EVENT_TRACE_PROPERTIES_V2__Anonymous2_e__Union._anonymous_ = [
        'Anonymous',
    ]
    EVENT_TRACE_PROPERTIES_V2__Anonymous2_e__Union._fields_ = [
        ("Anonymous", EVENT_TRACE_PROPERTIES_V2__Anonymous2_e__Union__Anonymous_e__Struct),
        ("V2Control", UInt32),
    ]
    class EVENT_TRACE_PROPERTIES_V2__Anonymous1_e__Union(Union):
        pass
    EVENT_TRACE_PROPERTIES_V2__Anonymous1_e__Union._fields_ = [
        ("AgeLimit", Int32),
        ("FlushThreshold", Int32),
    ]
    EVENT_TRACE_PROPERTIES_V2._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
        'Anonymous3',
    ]
    EVENT_TRACE_PROPERTIES_V2._fields_ = [
        ("Wnode", win32more.System.Diagnostics.Etw.WNODE_HEADER),
        ("BufferSize", UInt32),
        ("MinimumBuffers", UInt32),
        ("MaximumBuffers", UInt32),
        ("MaximumFileSize", UInt32),
        ("LogFileMode", UInt32),
        ("FlushTimer", UInt32),
        ("EnableFlags", win32more.System.Diagnostics.Etw.EVENT_TRACE_FLAG),
        ("Anonymous1", EVENT_TRACE_PROPERTIES_V2__Anonymous1_e__Union),
        ("NumberOfBuffers", UInt32),
        ("FreeBuffers", UInt32),
        ("EventsLost", UInt32),
        ("BuffersWritten", UInt32),
        ("LogBuffersLost", UInt32),
        ("RealTimeBuffersLost", UInt32),
        ("LoggerThreadId", win32more.Foundation.HANDLE),
        ("LogFileNameOffset", UInt32),
        ("LoggerNameOffset", UInt32),
        ("Anonymous2", EVENT_TRACE_PROPERTIES_V2__Anonymous2_e__Union),
        ("FilterDescCount", UInt32),
        ("FilterDesc", POINTER(win32more.System.Diagnostics.Etw.EVENT_FILTER_DESCRIPTOR_head)),
        ("Anonymous3", EVENT_TRACE_PROPERTIES_V2__Anonymous3_e__Union),
    ]
    return EVENT_TRACE_PROPERTIES_V2
def _define_TRACE_GUID_REGISTRATION_head():
    class TRACE_GUID_REGISTRATION(Structure):
        pass
    return TRACE_GUID_REGISTRATION
def _define_TRACE_GUID_REGISTRATION():
    TRACE_GUID_REGISTRATION = win32more.System.Diagnostics.Etw.TRACE_GUID_REGISTRATION_head
    TRACE_GUID_REGISTRATION._fields_ = [
        ("Guid", POINTER(Guid)),
        ("RegHandle", win32more.Foundation.HANDLE),
    ]
    return TRACE_GUID_REGISTRATION
def _define_TRACE_GUID_PROPERTIES_head():
    class TRACE_GUID_PROPERTIES(Structure):
        pass
    return TRACE_GUID_PROPERTIES
def _define_TRACE_GUID_PROPERTIES():
    TRACE_GUID_PROPERTIES = win32more.System.Diagnostics.Etw.TRACE_GUID_PROPERTIES_head
    TRACE_GUID_PROPERTIES._fields_ = [
        ("Guid", Guid),
        ("GuidType", UInt32),
        ("LoggerId", UInt32),
        ("EnableLevel", UInt32),
        ("EnableFlags", UInt32),
        ("IsEnable", win32more.Foundation.BOOLEAN),
    ]
    return TRACE_GUID_PROPERTIES
def _define_ETW_BUFFER_CONTEXT_head():
    class ETW_BUFFER_CONTEXT(Structure):
        pass
    return ETW_BUFFER_CONTEXT
def _define_ETW_BUFFER_CONTEXT():
    ETW_BUFFER_CONTEXT = win32more.System.Diagnostics.Etw.ETW_BUFFER_CONTEXT_head
    class ETW_BUFFER_CONTEXT__Anonymous_e__Union(Union):
        pass
    class ETW_BUFFER_CONTEXT__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    ETW_BUFFER_CONTEXT__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ("ProcessorNumber", Byte),
        ("Alignment", Byte),
    ]
    ETW_BUFFER_CONTEXT__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    ETW_BUFFER_CONTEXT__Anonymous_e__Union._fields_ = [
        ("Anonymous", ETW_BUFFER_CONTEXT__Anonymous_e__Union__Anonymous_e__Struct),
        ("ProcessorIndex", UInt16),
    ]
    ETW_BUFFER_CONTEXT._anonymous_ = [
        'Anonymous',
    ]
    ETW_BUFFER_CONTEXT._fields_ = [
        ("Anonymous", ETW_BUFFER_CONTEXT__Anonymous_e__Union),
        ("LoggerId", UInt16),
    ]
    return ETW_BUFFER_CONTEXT
def _define_TRACE_ENABLE_INFO_head():
    class TRACE_ENABLE_INFO(Structure):
        pass
    return TRACE_ENABLE_INFO
def _define_TRACE_ENABLE_INFO():
    TRACE_ENABLE_INFO = win32more.System.Diagnostics.Etw.TRACE_ENABLE_INFO_head
    TRACE_ENABLE_INFO._fields_ = [
        ("IsEnabled", UInt32),
        ("Level", Byte),
        ("Reserved1", Byte),
        ("LoggerId", UInt16),
        ("EnableProperty", UInt32),
        ("Reserved2", UInt32),
        ("MatchAnyKeyword", UInt64),
        ("MatchAllKeyword", UInt64),
    ]
    return TRACE_ENABLE_INFO
def _define_TRACE_PROVIDER_INSTANCE_INFO_head():
    class TRACE_PROVIDER_INSTANCE_INFO(Structure):
        pass
    return TRACE_PROVIDER_INSTANCE_INFO
def _define_TRACE_PROVIDER_INSTANCE_INFO():
    TRACE_PROVIDER_INSTANCE_INFO = win32more.System.Diagnostics.Etw.TRACE_PROVIDER_INSTANCE_INFO_head
    TRACE_PROVIDER_INSTANCE_INFO._fields_ = [
        ("NextOffset", UInt32),
        ("EnableCount", UInt32),
        ("Pid", UInt32),
        ("Flags", UInt32),
    ]
    return TRACE_PROVIDER_INSTANCE_INFO
def _define_TRACE_GUID_INFO_head():
    class TRACE_GUID_INFO(Structure):
        pass
    return TRACE_GUID_INFO
def _define_TRACE_GUID_INFO():
    TRACE_GUID_INFO = win32more.System.Diagnostics.Etw.TRACE_GUID_INFO_head
    TRACE_GUID_INFO._fields_ = [
        ("InstanceCount", UInt32),
        ("Reserved", UInt32),
    ]
    return TRACE_GUID_INFO
def _define_PROFILE_SOURCE_INFO_head():
    class PROFILE_SOURCE_INFO(Structure):
        pass
    return PROFILE_SOURCE_INFO
def _define_PROFILE_SOURCE_INFO():
    PROFILE_SOURCE_INFO = win32more.System.Diagnostics.Etw.PROFILE_SOURCE_INFO_head
    PROFILE_SOURCE_INFO._fields_ = [
        ("NextEntryOffset", UInt32),
        ("Source", UInt32),
        ("MinInterval", UInt32),
        ("MaxInterval", UInt32),
        ("Reserved", UInt64),
        ("Description", Char * 0),
    ]
    return PROFILE_SOURCE_INFO
ETW_PMC_COUNTER_OWNER_TYPE = Int32
ETW_PMC_COUNTER_OWNER_TYPE_EtwPmcOwnerFree = 0
ETW_PMC_COUNTER_OWNER_TYPE_EtwPmcOwnerUntagged = 1
ETW_PMC_COUNTER_OWNER_TYPE_EtwPmcOwnerTagged = 2
ETW_PMC_COUNTER_OWNER_TYPE_EtwPmcOwnerTaggedWithSource = 3
def _define_ETW_PMC_COUNTER_OWNER_head():
    class ETW_PMC_COUNTER_OWNER(Structure):
        pass
    return ETW_PMC_COUNTER_OWNER
def _define_ETW_PMC_COUNTER_OWNER():
    ETW_PMC_COUNTER_OWNER = win32more.System.Diagnostics.Etw.ETW_PMC_COUNTER_OWNER_head
    ETW_PMC_COUNTER_OWNER._fields_ = [
        ("OwnerType", win32more.System.Diagnostics.Etw.ETW_PMC_COUNTER_OWNER_TYPE),
        ("ProfileSource", UInt32),
        ("OwnerTag", UInt32),
    ]
    return ETW_PMC_COUNTER_OWNER
def _define_ETW_PMC_COUNTER_OWNERSHIP_STATUS_head():
    class ETW_PMC_COUNTER_OWNERSHIP_STATUS(Structure):
        pass
    return ETW_PMC_COUNTER_OWNERSHIP_STATUS
def _define_ETW_PMC_COUNTER_OWNERSHIP_STATUS():
    ETW_PMC_COUNTER_OWNERSHIP_STATUS = win32more.System.Diagnostics.Etw.ETW_PMC_COUNTER_OWNERSHIP_STATUS_head
    ETW_PMC_COUNTER_OWNERSHIP_STATUS._fields_ = [
        ("ProcessorNumber", UInt32),
        ("NumberOfCounters", UInt32),
        ("CounterOwners", win32more.System.Diagnostics.Etw.ETW_PMC_COUNTER_OWNER * 0),
    ]
    return ETW_PMC_COUNTER_OWNERSHIP_STATUS
def _define_EVENT_TRACE_head():
    class EVENT_TRACE(Structure):
        pass
    return EVENT_TRACE
def _define_EVENT_TRACE():
    EVENT_TRACE = win32more.System.Diagnostics.Etw.EVENT_TRACE_head
    class EVENT_TRACE__Anonymous_e__Union(Union):
        pass
    EVENT_TRACE__Anonymous_e__Union._fields_ = [
        ("ClientContext", UInt32),
        ("BufferContext", win32more.System.Diagnostics.Etw.ETW_BUFFER_CONTEXT),
    ]
    EVENT_TRACE._anonymous_ = [
        'Anonymous',
    ]
    EVENT_TRACE._fields_ = [
        ("Header", win32more.System.Diagnostics.Etw.EVENT_TRACE_HEADER),
        ("InstanceId", UInt32),
        ("ParentInstanceId", UInt32),
        ("ParentGuid", Guid),
        ("MofData", c_void_p),
        ("MofLength", UInt32),
        ("Anonymous", EVENT_TRACE__Anonymous_e__Union),
    ]
    return EVENT_TRACE
def _define_PEVENT_TRACE_BUFFER_CALLBACKW():
    return CFUNCTYPE(UInt32,POINTER(win32more.System.Diagnostics.Etw.EVENT_TRACE_LOGFILEW_head), use_last_error=False)
def _define_PEVENT_TRACE_BUFFER_CALLBACKA():
    return CFUNCTYPE(UInt32,POINTER(win32more.System.Diagnostics.Etw.EVENT_TRACE_LOGFILEA_head), use_last_error=False)
def _define_PEVENT_CALLBACK():
    return CFUNCTYPE(Void,POINTER(win32more.System.Diagnostics.Etw.EVENT_TRACE_head), use_last_error=False)
def _define_PEVENT_RECORD_CALLBACK():
    return CFUNCTYPE(Void,POINTER(win32more.System.Diagnostics.Etw.EVENT_RECORD_head), use_last_error=False)
def _define_WMIDPREQUEST():
    return CFUNCTYPE(UInt32,win32more.System.Diagnostics.Etw.WMIDPREQUESTCODE,c_void_p,POINTER(UInt32),c_void_p, use_last_error=False)
def _define_EVENT_TRACE_LOGFILEW_head():
    class EVENT_TRACE_LOGFILEW(Structure):
        pass
    return EVENT_TRACE_LOGFILEW
def _define_EVENT_TRACE_LOGFILEW():
    EVENT_TRACE_LOGFILEW = win32more.System.Diagnostics.Etw.EVENT_TRACE_LOGFILEW_head
    class EVENT_TRACE_LOGFILEW__Anonymous1_e__Union(Union):
        pass
    EVENT_TRACE_LOGFILEW__Anonymous1_e__Union._fields_ = [
        ("LogFileMode", UInt32),
        ("ProcessTraceMode", UInt32),
    ]
    class EVENT_TRACE_LOGFILEW__Anonymous2_e__Union(Union):
        pass
    EVENT_TRACE_LOGFILEW__Anonymous2_e__Union._fields_ = [
        ("EventCallback", win32more.System.Diagnostics.Etw.PEVENT_CALLBACK),
        ("EventRecordCallback", win32more.System.Diagnostics.Etw.PEVENT_RECORD_CALLBACK),
    ]
    EVENT_TRACE_LOGFILEW._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
    ]
    EVENT_TRACE_LOGFILEW._fields_ = [
        ("LogFileName", win32more.Foundation.PWSTR),
        ("LoggerName", win32more.Foundation.PWSTR),
        ("CurrentTime", Int64),
        ("BuffersRead", UInt32),
        ("Anonymous1", EVENT_TRACE_LOGFILEW__Anonymous1_e__Union),
        ("CurrentEvent", win32more.System.Diagnostics.Etw.EVENT_TRACE),
        ("LogfileHeader", win32more.System.Diagnostics.Etw.TRACE_LOGFILE_HEADER),
        ("BufferCallback", win32more.System.Diagnostics.Etw.PEVENT_TRACE_BUFFER_CALLBACKW),
        ("BufferSize", UInt32),
        ("Filled", UInt32),
        ("EventsLost", UInt32),
        ("Anonymous2", EVENT_TRACE_LOGFILEW__Anonymous2_e__Union),
        ("IsKernelTrace", UInt32),
        ("Context", c_void_p),
    ]
    return EVENT_TRACE_LOGFILEW
def _define_EVENT_TRACE_LOGFILEA_head():
    class EVENT_TRACE_LOGFILEA(Structure):
        pass
    return EVENT_TRACE_LOGFILEA
def _define_EVENT_TRACE_LOGFILEA():
    EVENT_TRACE_LOGFILEA = win32more.System.Diagnostics.Etw.EVENT_TRACE_LOGFILEA_head
    class EVENT_TRACE_LOGFILEA__Anonymous1_e__Union(Union):
        pass
    EVENT_TRACE_LOGFILEA__Anonymous1_e__Union._fields_ = [
        ("LogFileMode", UInt32),
        ("ProcessTraceMode", UInt32),
    ]
    class EVENT_TRACE_LOGFILEA__Anonymous2_e__Union(Union):
        pass
    EVENT_TRACE_LOGFILEA__Anonymous2_e__Union._fields_ = [
        ("EventCallback", win32more.System.Diagnostics.Etw.PEVENT_CALLBACK),
        ("EventRecordCallback", win32more.System.Diagnostics.Etw.PEVENT_RECORD_CALLBACK),
    ]
    EVENT_TRACE_LOGFILEA._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
    ]
    EVENT_TRACE_LOGFILEA._fields_ = [
        ("LogFileName", win32more.Foundation.PSTR),
        ("LoggerName", win32more.Foundation.PSTR),
        ("CurrentTime", Int64),
        ("BuffersRead", UInt32),
        ("Anonymous1", EVENT_TRACE_LOGFILEA__Anonymous1_e__Union),
        ("CurrentEvent", win32more.System.Diagnostics.Etw.EVENT_TRACE),
        ("LogfileHeader", win32more.System.Diagnostics.Etw.TRACE_LOGFILE_HEADER),
        ("BufferCallback", win32more.System.Diagnostics.Etw.PEVENT_TRACE_BUFFER_CALLBACKA),
        ("BufferSize", UInt32),
        ("Filled", UInt32),
        ("EventsLost", UInt32),
        ("Anonymous2", EVENT_TRACE_LOGFILEA__Anonymous2_e__Union),
        ("IsKernelTrace", UInt32),
        ("Context", c_void_p),
    ]
    return EVENT_TRACE_LOGFILEA
def _define_ENABLE_TRACE_PARAMETERS_V1_head():
    class ENABLE_TRACE_PARAMETERS_V1(Structure):
        pass
    return ENABLE_TRACE_PARAMETERS_V1
def _define_ENABLE_TRACE_PARAMETERS_V1():
    ENABLE_TRACE_PARAMETERS_V1 = win32more.System.Diagnostics.Etw.ENABLE_TRACE_PARAMETERS_V1_head
    ENABLE_TRACE_PARAMETERS_V1._fields_ = [
        ("Version", UInt32),
        ("EnableProperty", UInt32),
        ("ControlFlags", UInt32),
        ("SourceId", Guid),
        ("EnableFilterDesc", POINTER(win32more.System.Diagnostics.Etw.EVENT_FILTER_DESCRIPTOR_head)),
    ]
    return ENABLE_TRACE_PARAMETERS_V1
def _define_ENABLE_TRACE_PARAMETERS_head():
    class ENABLE_TRACE_PARAMETERS(Structure):
        pass
    return ENABLE_TRACE_PARAMETERS
def _define_ENABLE_TRACE_PARAMETERS():
    ENABLE_TRACE_PARAMETERS = win32more.System.Diagnostics.Etw.ENABLE_TRACE_PARAMETERS_head
    ENABLE_TRACE_PARAMETERS._fields_ = [
        ("Version", UInt32),
        ("EnableProperty", UInt32),
        ("ControlFlags", UInt32),
        ("SourceId", Guid),
        ("EnableFilterDesc", POINTER(win32more.System.Diagnostics.Etw.EVENT_FILTER_DESCRIPTOR_head)),
        ("FilterDescCount", UInt32),
    ]
    return ENABLE_TRACE_PARAMETERS
TRACE_QUERY_INFO_CLASS = Int32
TRACE_QUERY_INFO_CLASS_TraceGuidQueryList = 0
TRACE_QUERY_INFO_CLASS_TraceGuidQueryInfo = 1
TRACE_QUERY_INFO_CLASS_TraceGuidQueryProcess = 2
TRACE_QUERY_INFO_CLASS_TraceStackTracingInfo = 3
TRACE_QUERY_INFO_CLASS_TraceSystemTraceEnableFlagsInfo = 4
TRACE_QUERY_INFO_CLASS_TraceSampledProfileIntervalInfo = 5
TRACE_QUERY_INFO_CLASS_TraceProfileSourceConfigInfo = 6
TRACE_QUERY_INFO_CLASS_TraceProfileSourceListInfo = 7
TRACE_QUERY_INFO_CLASS_TracePmcEventListInfo = 8
TRACE_QUERY_INFO_CLASS_TracePmcCounterListInfo = 9
TRACE_QUERY_INFO_CLASS_TraceSetDisallowList = 10
TRACE_QUERY_INFO_CLASS_TraceVersionInfo = 11
TRACE_QUERY_INFO_CLASS_TraceGroupQueryList = 12
TRACE_QUERY_INFO_CLASS_TraceGroupQueryInfo = 13
TRACE_QUERY_INFO_CLASS_TraceDisallowListQuery = 14
TRACE_QUERY_INFO_CLASS_TraceInfoReserved15 = 15
TRACE_QUERY_INFO_CLASS_TracePeriodicCaptureStateListInfo = 16
TRACE_QUERY_INFO_CLASS_TracePeriodicCaptureStateInfo = 17
TRACE_QUERY_INFO_CLASS_TraceProviderBinaryTracking = 18
TRACE_QUERY_INFO_CLASS_TraceMaxLoggersQuery = 19
TRACE_QUERY_INFO_CLASS_TraceLbrConfigurationInfo = 20
TRACE_QUERY_INFO_CLASS_TraceLbrEventListInfo = 21
TRACE_QUERY_INFO_CLASS_TraceMaxPmcCounterQuery = 22
TRACE_QUERY_INFO_CLASS_TraceStreamCount = 23
TRACE_QUERY_INFO_CLASS_TraceStackCachingInfo = 24
TRACE_QUERY_INFO_CLASS_TracePmcCounterOwners = 25
TRACE_QUERY_INFO_CLASS_TraceUnifiedStackCachingInfo = 26
TRACE_QUERY_INFO_CLASS_MaxTraceSetInfoClass = 27
def _define_CLASSIC_EVENT_ID_head():
    class CLASSIC_EVENT_ID(Structure):
        pass
    return CLASSIC_EVENT_ID
def _define_CLASSIC_EVENT_ID():
    CLASSIC_EVENT_ID = win32more.System.Diagnostics.Etw.CLASSIC_EVENT_ID_head
    CLASSIC_EVENT_ID._fields_ = [
        ("EventGuid", Guid),
        ("Type", Byte),
        ("Reserved", Byte * 7),
    ]
    return CLASSIC_EVENT_ID
def _define_TRACE_STACK_CACHING_INFO_head():
    class TRACE_STACK_CACHING_INFO(Structure):
        pass
    return TRACE_STACK_CACHING_INFO
def _define_TRACE_STACK_CACHING_INFO():
    TRACE_STACK_CACHING_INFO = win32more.System.Diagnostics.Etw.TRACE_STACK_CACHING_INFO_head
    TRACE_STACK_CACHING_INFO._fields_ = [
        ("Enabled", win32more.Foundation.BOOLEAN),
        ("CacheSize", UInt32),
        ("BucketCount", UInt32),
    ]
    return TRACE_STACK_CACHING_INFO
def _define_TRACE_PROFILE_INTERVAL_head():
    class TRACE_PROFILE_INTERVAL(Structure):
        pass
    return TRACE_PROFILE_INTERVAL
def _define_TRACE_PROFILE_INTERVAL():
    TRACE_PROFILE_INTERVAL = win32more.System.Diagnostics.Etw.TRACE_PROFILE_INTERVAL_head
    TRACE_PROFILE_INTERVAL._fields_ = [
        ("Source", UInt32),
        ("Interval", UInt32),
    ]
    return TRACE_PROFILE_INTERVAL
def _define_TRACE_VERSION_INFO_head():
    class TRACE_VERSION_INFO(Structure):
        pass
    return TRACE_VERSION_INFO
def _define_TRACE_VERSION_INFO():
    TRACE_VERSION_INFO = win32more.System.Diagnostics.Etw.TRACE_VERSION_INFO_head
    TRACE_VERSION_INFO._fields_ = [
        ("EtwTraceProcessingVersion", UInt32),
        ("Reserved", UInt32),
    ]
    return TRACE_VERSION_INFO
def _define_TRACE_PERIODIC_CAPTURE_STATE_INFO_head():
    class TRACE_PERIODIC_CAPTURE_STATE_INFO(Structure):
        pass
    return TRACE_PERIODIC_CAPTURE_STATE_INFO
def _define_TRACE_PERIODIC_CAPTURE_STATE_INFO():
    TRACE_PERIODIC_CAPTURE_STATE_INFO = win32more.System.Diagnostics.Etw.TRACE_PERIODIC_CAPTURE_STATE_INFO_head
    TRACE_PERIODIC_CAPTURE_STATE_INFO._fields_ = [
        ("CaptureStateFrequencyInSeconds", UInt32),
        ("ProviderCount", UInt16),
        ("Reserved", UInt16),
    ]
    return TRACE_PERIODIC_CAPTURE_STATE_INFO
ETW_PROCESS_HANDLE_INFO_TYPE = Int32
ETW_PROCESS_HANDLE_INFO_TYPE_EtwQueryPartitionInformation = 1
ETW_PROCESS_HANDLE_INFO_TYPE_EtwQueryPartitionInformationV2 = 2
ETW_PROCESS_HANDLE_INFO_TYPE_EtwQueryLastDroppedTimes = 3
ETW_PROCESS_HANDLE_INFO_TYPE_EtwQueryProcessHandleInfoMax = 4
def _define_ETW_TRACE_PARTITION_INFORMATION_head():
    class ETW_TRACE_PARTITION_INFORMATION(Structure):
        pass
    return ETW_TRACE_PARTITION_INFORMATION
def _define_ETW_TRACE_PARTITION_INFORMATION():
    ETW_TRACE_PARTITION_INFORMATION = win32more.System.Diagnostics.Etw.ETW_TRACE_PARTITION_INFORMATION_head
    ETW_TRACE_PARTITION_INFORMATION._fields_ = [
        ("PartitionId", Guid),
        ("ParentId", Guid),
        ("QpcOffsetFromRoot", Int64),
        ("PartitionType", UInt32),
    ]
    return ETW_TRACE_PARTITION_INFORMATION
def _define_ETW_TRACE_PARTITION_INFORMATION_V2_head():
    class ETW_TRACE_PARTITION_INFORMATION_V2(Structure):
        pass
    return ETW_TRACE_PARTITION_INFORMATION_V2
def _define_ETW_TRACE_PARTITION_INFORMATION_V2():
    ETW_TRACE_PARTITION_INFORMATION_V2 = win32more.System.Diagnostics.Etw.ETW_TRACE_PARTITION_INFORMATION_V2_head
    ETW_TRACE_PARTITION_INFORMATION_V2._fields_ = [
        ("QpcOffsetFromRoot", Int64),
        ("PartitionType", UInt32),
        ("PartitionId", win32more.Foundation.PWSTR),
        ("ParentId", win32more.Foundation.PWSTR),
    ]
    return ETW_TRACE_PARTITION_INFORMATION_V2
def _define_EVENT_DATA_DESCRIPTOR_head():
    class EVENT_DATA_DESCRIPTOR(Structure):
        pass
    return EVENT_DATA_DESCRIPTOR
def _define_EVENT_DATA_DESCRIPTOR():
    EVENT_DATA_DESCRIPTOR = win32more.System.Diagnostics.Etw.EVENT_DATA_DESCRIPTOR_head
    class EVENT_DATA_DESCRIPTOR__Anonymous_e__Union(Union):
        pass
    class EVENT_DATA_DESCRIPTOR__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    EVENT_DATA_DESCRIPTOR__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ("Type", Byte),
        ("Reserved1", Byte),
        ("Reserved2", UInt16),
    ]
    EVENT_DATA_DESCRIPTOR__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    EVENT_DATA_DESCRIPTOR__Anonymous_e__Union._fields_ = [
        ("Reserved", UInt32),
        ("Anonymous", EVENT_DATA_DESCRIPTOR__Anonymous_e__Union__Anonymous_e__Struct),
    ]
    EVENT_DATA_DESCRIPTOR._anonymous_ = [
        'Anonymous',
    ]
    EVENT_DATA_DESCRIPTOR._fields_ = [
        ("Ptr", UInt64),
        ("Size", UInt32),
        ("Anonymous", EVENT_DATA_DESCRIPTOR__Anonymous_e__Union),
    ]
    return EVENT_DATA_DESCRIPTOR
def _define_EVENT_DESCRIPTOR_head():
    class EVENT_DESCRIPTOR(Structure):
        pass
    return EVENT_DESCRIPTOR
def _define_EVENT_DESCRIPTOR():
    EVENT_DESCRIPTOR = win32more.System.Diagnostics.Etw.EVENT_DESCRIPTOR_head
    EVENT_DESCRIPTOR._fields_ = [
        ("Id", UInt16),
        ("Version", Byte),
        ("Channel", Byte),
        ("Level", Byte),
        ("Opcode", Byte),
        ("Task", UInt16),
        ("Keyword", UInt64),
    ]
    return EVENT_DESCRIPTOR
def _define_EVENT_FILTER_DESCRIPTOR_head():
    class EVENT_FILTER_DESCRIPTOR(Structure):
        pass
    return EVENT_FILTER_DESCRIPTOR
def _define_EVENT_FILTER_DESCRIPTOR():
    EVENT_FILTER_DESCRIPTOR = win32more.System.Diagnostics.Etw.EVENT_FILTER_DESCRIPTOR_head
    EVENT_FILTER_DESCRIPTOR._fields_ = [
        ("Ptr", UInt64),
        ("Size", UInt32),
        ("Type", UInt32),
    ]
    return EVENT_FILTER_DESCRIPTOR
def _define_EVENT_FILTER_HEADER_head():
    class EVENT_FILTER_HEADER(Structure):
        pass
    return EVENT_FILTER_HEADER
def _define_EVENT_FILTER_HEADER():
    EVENT_FILTER_HEADER = win32more.System.Diagnostics.Etw.EVENT_FILTER_HEADER_head
    EVENT_FILTER_HEADER._fields_ = [
        ("Id", UInt16),
        ("Version", Byte),
        ("Reserved", Byte * 5),
        ("InstanceId", UInt64),
        ("Size", UInt32),
        ("NextOffset", UInt32),
    ]
    return EVENT_FILTER_HEADER
def _define_EVENT_FILTER_EVENT_ID_head():
    class EVENT_FILTER_EVENT_ID(Structure):
        pass
    return EVENT_FILTER_EVENT_ID
def _define_EVENT_FILTER_EVENT_ID():
    EVENT_FILTER_EVENT_ID = win32more.System.Diagnostics.Etw.EVENT_FILTER_EVENT_ID_head
    EVENT_FILTER_EVENT_ID._fields_ = [
        ("FilterIn", win32more.Foundation.BOOLEAN),
        ("Reserved", Byte),
        ("Count", UInt16),
        ("Events", UInt16 * 0),
    ]
    return EVENT_FILTER_EVENT_ID
def _define_EVENT_FILTER_EVENT_NAME_head():
    class EVENT_FILTER_EVENT_NAME(Structure):
        pass
    return EVENT_FILTER_EVENT_NAME
def _define_EVENT_FILTER_EVENT_NAME():
    EVENT_FILTER_EVENT_NAME = win32more.System.Diagnostics.Etw.EVENT_FILTER_EVENT_NAME_head
    EVENT_FILTER_EVENT_NAME._fields_ = [
        ("MatchAnyKeyword", UInt64),
        ("MatchAllKeyword", UInt64),
        ("Level", Byte),
        ("FilterIn", win32more.Foundation.BOOLEAN),
        ("NameCount", UInt16),
        ("Names", Byte * 0),
    ]
    return EVENT_FILTER_EVENT_NAME
def _define_EVENT_FILTER_LEVEL_KW_head():
    class EVENT_FILTER_LEVEL_KW(Structure):
        pass
    return EVENT_FILTER_LEVEL_KW
def _define_EVENT_FILTER_LEVEL_KW():
    EVENT_FILTER_LEVEL_KW = win32more.System.Diagnostics.Etw.EVENT_FILTER_LEVEL_KW_head
    EVENT_FILTER_LEVEL_KW._fields_ = [
        ("MatchAnyKeyword", UInt64),
        ("MatchAllKeyword", UInt64),
        ("Level", Byte),
        ("FilterIn", win32more.Foundation.BOOLEAN),
    ]
    return EVENT_FILTER_LEVEL_KW
EVENT_INFO_CLASS = Int32
EVENT_INFO_CLASS_EventProviderBinaryTrackInfo = 0
EVENT_INFO_CLASS_EventProviderSetReserved1 = 1
EVENT_INFO_CLASS_EventProviderSetTraits = 2
EVENT_INFO_CLASS_EventProviderUseDescriptorType = 3
EVENT_INFO_CLASS_MaxEventInfo = 4
def _define_PENABLECALLBACK():
    return CFUNCTYPE(Void,POINTER(Guid),win32more.System.Diagnostics.Etw.ENABLECALLBACK_ENABLED_STATE,Byte,UInt64,UInt64,POINTER(win32more.System.Diagnostics.Etw.EVENT_FILTER_DESCRIPTOR_head),c_void_p, use_last_error=False)
def _define_EVENT_HEADER_EXTENDED_DATA_ITEM_head():
    class EVENT_HEADER_EXTENDED_DATA_ITEM(Structure):
        pass
    return EVENT_HEADER_EXTENDED_DATA_ITEM
def _define_EVENT_HEADER_EXTENDED_DATA_ITEM():
    EVENT_HEADER_EXTENDED_DATA_ITEM = win32more.System.Diagnostics.Etw.EVENT_HEADER_EXTENDED_DATA_ITEM_head
    class EVENT_HEADER_EXTENDED_DATA_ITEM__Anonymous_e__Struct(Structure):
        pass
    EVENT_HEADER_EXTENDED_DATA_ITEM__Anonymous_e__Struct._fields_ = [
        ("_bitfield", UInt16),
    ]
    EVENT_HEADER_EXTENDED_DATA_ITEM._anonymous_ = [
        'Anonymous',
    ]
    EVENT_HEADER_EXTENDED_DATA_ITEM._fields_ = [
        ("Reserved1", UInt16),
        ("ExtType", UInt16),
        ("Anonymous", EVENT_HEADER_EXTENDED_DATA_ITEM__Anonymous_e__Struct),
        ("DataSize", UInt16),
        ("DataPtr", UInt64),
    ]
    return EVENT_HEADER_EXTENDED_DATA_ITEM
def _define_EVENT_EXTENDED_ITEM_INSTANCE_head():
    class EVENT_EXTENDED_ITEM_INSTANCE(Structure):
        pass
    return EVENT_EXTENDED_ITEM_INSTANCE
def _define_EVENT_EXTENDED_ITEM_INSTANCE():
    EVENT_EXTENDED_ITEM_INSTANCE = win32more.System.Diagnostics.Etw.EVENT_EXTENDED_ITEM_INSTANCE_head
    EVENT_EXTENDED_ITEM_INSTANCE._fields_ = [
        ("InstanceId", UInt32),
        ("ParentInstanceId", UInt32),
        ("ParentGuid", Guid),
    ]
    return EVENT_EXTENDED_ITEM_INSTANCE
def _define_EVENT_EXTENDED_ITEM_RELATED_ACTIVITYID_head():
    class EVENT_EXTENDED_ITEM_RELATED_ACTIVITYID(Structure):
        pass
    return EVENT_EXTENDED_ITEM_RELATED_ACTIVITYID
def _define_EVENT_EXTENDED_ITEM_RELATED_ACTIVITYID():
    EVENT_EXTENDED_ITEM_RELATED_ACTIVITYID = win32more.System.Diagnostics.Etw.EVENT_EXTENDED_ITEM_RELATED_ACTIVITYID_head
    EVENT_EXTENDED_ITEM_RELATED_ACTIVITYID._fields_ = [
        ("RelatedActivityId", Guid),
    ]
    return EVENT_EXTENDED_ITEM_RELATED_ACTIVITYID
def _define_EVENT_EXTENDED_ITEM_TS_ID_head():
    class EVENT_EXTENDED_ITEM_TS_ID(Structure):
        pass
    return EVENT_EXTENDED_ITEM_TS_ID
def _define_EVENT_EXTENDED_ITEM_TS_ID():
    EVENT_EXTENDED_ITEM_TS_ID = win32more.System.Diagnostics.Etw.EVENT_EXTENDED_ITEM_TS_ID_head
    EVENT_EXTENDED_ITEM_TS_ID._fields_ = [
        ("SessionId", UInt32),
    ]
    return EVENT_EXTENDED_ITEM_TS_ID
def _define_EVENT_EXTENDED_ITEM_STACK_TRACE32_head():
    class EVENT_EXTENDED_ITEM_STACK_TRACE32(Structure):
        pass
    return EVENT_EXTENDED_ITEM_STACK_TRACE32
def _define_EVENT_EXTENDED_ITEM_STACK_TRACE32():
    EVENT_EXTENDED_ITEM_STACK_TRACE32 = win32more.System.Diagnostics.Etw.EVENT_EXTENDED_ITEM_STACK_TRACE32_head
    EVENT_EXTENDED_ITEM_STACK_TRACE32._fields_ = [
        ("MatchId", UInt64),
        ("Address", UInt32 * 0),
    ]
    return EVENT_EXTENDED_ITEM_STACK_TRACE32
def _define_EVENT_EXTENDED_ITEM_STACK_TRACE64_head():
    class EVENT_EXTENDED_ITEM_STACK_TRACE64(Structure):
        pass
    return EVENT_EXTENDED_ITEM_STACK_TRACE64
def _define_EVENT_EXTENDED_ITEM_STACK_TRACE64():
    EVENT_EXTENDED_ITEM_STACK_TRACE64 = win32more.System.Diagnostics.Etw.EVENT_EXTENDED_ITEM_STACK_TRACE64_head
    EVENT_EXTENDED_ITEM_STACK_TRACE64._fields_ = [
        ("MatchId", UInt64),
        ("Address", UInt64 * 0),
    ]
    return EVENT_EXTENDED_ITEM_STACK_TRACE64
def _define_EVENT_EXTENDED_ITEM_STACK_KEY32_head():
    class EVENT_EXTENDED_ITEM_STACK_KEY32(Structure):
        pass
    return EVENT_EXTENDED_ITEM_STACK_KEY32
def _define_EVENT_EXTENDED_ITEM_STACK_KEY32():
    EVENT_EXTENDED_ITEM_STACK_KEY32 = win32more.System.Diagnostics.Etw.EVENT_EXTENDED_ITEM_STACK_KEY32_head
    EVENT_EXTENDED_ITEM_STACK_KEY32._fields_ = [
        ("MatchId", UInt64),
        ("StackKey", UInt32),
        ("Padding", UInt32),
    ]
    return EVENT_EXTENDED_ITEM_STACK_KEY32
def _define_EVENT_EXTENDED_ITEM_STACK_KEY64_head():
    class EVENT_EXTENDED_ITEM_STACK_KEY64(Structure):
        pass
    return EVENT_EXTENDED_ITEM_STACK_KEY64
def _define_EVENT_EXTENDED_ITEM_STACK_KEY64():
    EVENT_EXTENDED_ITEM_STACK_KEY64 = win32more.System.Diagnostics.Etw.EVENT_EXTENDED_ITEM_STACK_KEY64_head
    EVENT_EXTENDED_ITEM_STACK_KEY64._fields_ = [
        ("MatchId", UInt64),
        ("StackKey", UInt64),
    ]
    return EVENT_EXTENDED_ITEM_STACK_KEY64
def _define_EVENT_EXTENDED_ITEM_PEBS_INDEX_head():
    class EVENT_EXTENDED_ITEM_PEBS_INDEX(Structure):
        pass
    return EVENT_EXTENDED_ITEM_PEBS_INDEX
def _define_EVENT_EXTENDED_ITEM_PEBS_INDEX():
    EVENT_EXTENDED_ITEM_PEBS_INDEX = win32more.System.Diagnostics.Etw.EVENT_EXTENDED_ITEM_PEBS_INDEX_head
    EVENT_EXTENDED_ITEM_PEBS_INDEX._fields_ = [
        ("PebsIndex", UInt64),
    ]
    return EVENT_EXTENDED_ITEM_PEBS_INDEX
def _define_EVENT_EXTENDED_ITEM_PMC_COUNTERS_head():
    class EVENT_EXTENDED_ITEM_PMC_COUNTERS(Structure):
        pass
    return EVENT_EXTENDED_ITEM_PMC_COUNTERS
def _define_EVENT_EXTENDED_ITEM_PMC_COUNTERS():
    EVENT_EXTENDED_ITEM_PMC_COUNTERS = win32more.System.Diagnostics.Etw.EVENT_EXTENDED_ITEM_PMC_COUNTERS_head
    EVENT_EXTENDED_ITEM_PMC_COUNTERS._fields_ = [
        ("Counter", UInt64 * 0),
    ]
    return EVENT_EXTENDED_ITEM_PMC_COUNTERS
def _define_EVENT_EXTENDED_ITEM_PROCESS_START_KEY_head():
    class EVENT_EXTENDED_ITEM_PROCESS_START_KEY(Structure):
        pass
    return EVENT_EXTENDED_ITEM_PROCESS_START_KEY
def _define_EVENT_EXTENDED_ITEM_PROCESS_START_KEY():
    EVENT_EXTENDED_ITEM_PROCESS_START_KEY = win32more.System.Diagnostics.Etw.EVENT_EXTENDED_ITEM_PROCESS_START_KEY_head
    EVENT_EXTENDED_ITEM_PROCESS_START_KEY._fields_ = [
        ("ProcessStartKey", UInt64),
    ]
    return EVENT_EXTENDED_ITEM_PROCESS_START_KEY
def _define_EVENT_EXTENDED_ITEM_EVENT_KEY_head():
    class EVENT_EXTENDED_ITEM_EVENT_KEY(Structure):
        pass
    return EVENT_EXTENDED_ITEM_EVENT_KEY
def _define_EVENT_EXTENDED_ITEM_EVENT_KEY():
    EVENT_EXTENDED_ITEM_EVENT_KEY = win32more.System.Diagnostics.Etw.EVENT_EXTENDED_ITEM_EVENT_KEY_head
    EVENT_EXTENDED_ITEM_EVENT_KEY._fields_ = [
        ("Key", UInt64),
    ]
    return EVENT_EXTENDED_ITEM_EVENT_KEY
def _define_EVENT_HEADER_head():
    class EVENT_HEADER(Structure):
        pass
    return EVENT_HEADER
def _define_EVENT_HEADER():
    EVENT_HEADER = win32more.System.Diagnostics.Etw.EVENT_HEADER_head
    class EVENT_HEADER__Anonymous_e__Union(Union):
        pass
    class EVENT_HEADER__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    EVENT_HEADER__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ("KernelTime", UInt32),
        ("UserTime", UInt32),
    ]
    EVENT_HEADER__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    EVENT_HEADER__Anonymous_e__Union._fields_ = [
        ("Anonymous", EVENT_HEADER__Anonymous_e__Union__Anonymous_e__Struct),
        ("ProcessorTime", UInt64),
    ]
    EVENT_HEADER._anonymous_ = [
        'Anonymous',
    ]
    EVENT_HEADER._fields_ = [
        ("Size", UInt16),
        ("HeaderType", UInt16),
        ("Flags", UInt16),
        ("EventProperty", UInt16),
        ("ThreadId", UInt32),
        ("ProcessId", UInt32),
        ("TimeStamp", win32more.Foundation.LARGE_INTEGER),
        ("ProviderId", Guid),
        ("EventDescriptor", win32more.System.Diagnostics.Etw.EVENT_DESCRIPTOR),
        ("Anonymous", EVENT_HEADER__Anonymous_e__Union),
        ("ActivityId", Guid),
    ]
    return EVENT_HEADER
def _define_EVENT_RECORD_head():
    class EVENT_RECORD(Structure):
        pass
    return EVENT_RECORD
def _define_EVENT_RECORD():
    EVENT_RECORD = win32more.System.Diagnostics.Etw.EVENT_RECORD_head
    EVENT_RECORD._fields_ = [
        ("EventHeader", win32more.System.Diagnostics.Etw.EVENT_HEADER),
        ("BufferContext", win32more.System.Diagnostics.Etw.ETW_BUFFER_CONTEXT),
        ("ExtendedDataCount", UInt16),
        ("UserDataLength", UInt16),
        ("ExtendedData", POINTER(win32more.System.Diagnostics.Etw.EVENT_HEADER_EXTENDED_DATA_ITEM_head)),
        ("UserData", c_void_p),
        ("UserContext", c_void_p),
    ]
    return EVENT_RECORD
ETW_PROVIDER_TRAIT_TYPE = Int32
ETW_PROVIDER_TRAIT_TYPE_EtwProviderTraitTypeGroup = 1
ETW_PROVIDER_TRAIT_TYPE_EtwProviderTraitDecodeGuid = 2
ETW_PROVIDER_TRAIT_TYPE_EtwProviderTraitTypeMax = 3
EVENTSECURITYOPERATION = Int32
EVENTSECURITYOPERATION_EventSecuritySetDACL = 0
EVENTSECURITYOPERATION_EventSecuritySetSACL = 1
EVENTSECURITYOPERATION_EventSecurityAddDACL = 2
EVENTSECURITYOPERATION_EventSecurityAddSACL = 3
EVENTSECURITYOPERATION_EventSecurityMax = 4
def _define_EVENT_MAP_ENTRY_head():
    class EVENT_MAP_ENTRY(Structure):
        pass
    return EVENT_MAP_ENTRY
def _define_EVENT_MAP_ENTRY():
    EVENT_MAP_ENTRY = win32more.System.Diagnostics.Etw.EVENT_MAP_ENTRY_head
    class EVENT_MAP_ENTRY__Anonymous_e__Union(Union):
        pass
    EVENT_MAP_ENTRY__Anonymous_e__Union._fields_ = [
        ("Value", UInt32),
        ("InputOffset", UInt32),
    ]
    EVENT_MAP_ENTRY._anonymous_ = [
        'Anonymous',
    ]
    EVENT_MAP_ENTRY._fields_ = [
        ("OutputOffset", UInt32),
        ("Anonymous", EVENT_MAP_ENTRY__Anonymous_e__Union),
    ]
    return EVENT_MAP_ENTRY
MAP_FLAGS = Int32
EVENTMAP_INFO_FLAG_MANIFEST_VALUEMAP = 1
EVENTMAP_INFO_FLAG_MANIFEST_BITMAP = 2
EVENTMAP_INFO_FLAG_MANIFEST_PATTERNMAP = 4
EVENTMAP_INFO_FLAG_WBEM_VALUEMAP = 8
EVENTMAP_INFO_FLAG_WBEM_BITMAP = 16
EVENTMAP_INFO_FLAG_WBEM_FLAG = 32
EVENTMAP_INFO_FLAG_WBEM_NO_MAP = 64
MAP_VALUETYPE = Int32
EVENTMAP_ENTRY_VALUETYPE_ULONG = 0
EVENTMAP_ENTRY_VALUETYPE_STRING = 1
def _define_EVENT_MAP_INFO_head():
    class EVENT_MAP_INFO(Structure):
        pass
    return EVENT_MAP_INFO
def _define_EVENT_MAP_INFO():
    EVENT_MAP_INFO = win32more.System.Diagnostics.Etw.EVENT_MAP_INFO_head
    class EVENT_MAP_INFO__Anonymous_e__Union(Union):
        pass
    EVENT_MAP_INFO__Anonymous_e__Union._fields_ = [
        ("MapEntryValueType", win32more.System.Diagnostics.Etw.MAP_VALUETYPE),
        ("FormatStringOffset", UInt32),
    ]
    EVENT_MAP_INFO._anonymous_ = [
        'Anonymous',
    ]
    EVENT_MAP_INFO._fields_ = [
        ("NameOffset", UInt32),
        ("Flag", win32more.System.Diagnostics.Etw.MAP_FLAGS),
        ("EntryCount", UInt32),
        ("Anonymous", EVENT_MAP_INFO__Anonymous_e__Union),
        ("MapEntryArray", win32more.System.Diagnostics.Etw.EVENT_MAP_ENTRY * 0),
    ]
    return EVENT_MAP_INFO
_TDH_IN_TYPE = Int32
TDH_INTYPE_NULL = 0
TDH_INTYPE_UNICODESTRING = 1
TDH_INTYPE_ANSISTRING = 2
TDH_INTYPE_INT8 = 3
TDH_INTYPE_UINT8 = 4
TDH_INTYPE_INT16 = 5
TDH_INTYPE_UINT16 = 6
TDH_INTYPE_INT32 = 7
TDH_INTYPE_UINT32 = 8
TDH_INTYPE_INT64 = 9
TDH_INTYPE_UINT64 = 10
TDH_INTYPE_FLOAT = 11
TDH_INTYPE_DOUBLE = 12
TDH_INTYPE_BOOLEAN = 13
TDH_INTYPE_BINARY = 14
TDH_INTYPE_GUID = 15
TDH_INTYPE_POINTER = 16
TDH_INTYPE_FILETIME = 17
TDH_INTYPE_SYSTEMTIME = 18
TDH_INTYPE_SID = 19
TDH_INTYPE_HEXINT32 = 20
TDH_INTYPE_HEXINT64 = 21
TDH_INTYPE_MANIFEST_COUNTEDSTRING = 22
TDH_INTYPE_MANIFEST_COUNTEDANSISTRING = 23
TDH_INTYPE_RESERVED24 = 24
TDH_INTYPE_MANIFEST_COUNTEDBINARY = 25
TDH_INTYPE_COUNTEDSTRING = 300
TDH_INTYPE_COUNTEDANSISTRING = 301
TDH_INTYPE_REVERSEDCOUNTEDSTRING = 302
TDH_INTYPE_REVERSEDCOUNTEDANSISTRING = 303
TDH_INTYPE_NONNULLTERMINATEDSTRING = 304
TDH_INTYPE_NONNULLTERMINATEDANSISTRING = 305
TDH_INTYPE_UNICODECHAR = 306
TDH_INTYPE_ANSICHAR = 307
TDH_INTYPE_SIZET = 308
TDH_INTYPE_HEXDUMP = 309
TDH_INTYPE_WBEMSID = 310
_TDH_OUT_TYPE = Int32
TDH_OUTTYPE_NULL = 0
TDH_OUTTYPE_STRING = 1
TDH_OUTTYPE_DATETIME = 2
TDH_OUTTYPE_BYTE = 3
TDH_OUTTYPE_UNSIGNEDBYTE = 4
TDH_OUTTYPE_SHORT = 5
TDH_OUTTYPE_UNSIGNEDSHORT = 6
TDH_OUTTYPE_INT = 7
TDH_OUTTYPE_UNSIGNEDINT = 8
TDH_OUTTYPE_LONG = 9
TDH_OUTTYPE_UNSIGNEDLONG = 10
TDH_OUTTYPE_FLOAT = 11
TDH_OUTTYPE_DOUBLE = 12
TDH_OUTTYPE_BOOLEAN = 13
TDH_OUTTYPE_GUID = 14
TDH_OUTTYPE_HEXBINARY = 15
TDH_OUTTYPE_HEXINT8 = 16
TDH_OUTTYPE_HEXINT16 = 17
TDH_OUTTYPE_HEXINT32 = 18
TDH_OUTTYPE_HEXINT64 = 19
TDH_OUTTYPE_PID = 20
TDH_OUTTYPE_TID = 21
TDH_OUTTYPE_PORT = 22
TDH_OUTTYPE_IPV4 = 23
TDH_OUTTYPE_IPV6 = 24
TDH_OUTTYPE_SOCKETADDRESS = 25
TDH_OUTTYPE_CIMDATETIME = 26
TDH_OUTTYPE_ETWTIME = 27
TDH_OUTTYPE_XML = 28
TDH_OUTTYPE_ERRORCODE = 29
TDH_OUTTYPE_WIN32ERROR = 30
TDH_OUTTYPE_NTSTATUS = 31
TDH_OUTTYPE_HRESULT = 32
TDH_OUTTYPE_CULTURE_INSENSITIVE_DATETIME = 33
TDH_OUTTYPE_JSON = 34
TDH_OUTTYPE_UTF8 = 35
TDH_OUTTYPE_PKCS7_WITH_TYPE_INFO = 36
TDH_OUTTYPE_CODE_POINTER = 37
TDH_OUTTYPE_DATETIME_UTC = 38
TDH_OUTTYPE_REDUCEDSTRING = 300
TDH_OUTTYPE_NOPRINT = 301
PROPERTY_FLAGS = Int32
PROPERTY_FLAGS_PropertyStruct = 1
PROPERTY_FLAGS_PropertyParamLength = 2
PROPERTY_FLAGS_PropertyParamCount = 4
PROPERTY_FLAGS_PropertyWBEMXmlFragment = 8
PROPERTY_FLAGS_PropertyParamFixedLength = 16
PROPERTY_FLAGS_PropertyParamFixedCount = 32
PROPERTY_FLAGS_PropertyHasTags = 64
PROPERTY_FLAGS_PropertyHasCustomSchema = 128
def _define_EVENT_PROPERTY_INFO_head():
    class EVENT_PROPERTY_INFO(Structure):
        pass
    return EVENT_PROPERTY_INFO
def _define_EVENT_PROPERTY_INFO():
    EVENT_PROPERTY_INFO = win32more.System.Diagnostics.Etw.EVENT_PROPERTY_INFO_head
    class EVENT_PROPERTY_INFO__Anonymous4_e__Union(Union):
        pass
    class EVENT_PROPERTY_INFO__Anonymous4_e__Union__Anonymous_e__Struct(Structure):
        pass
    EVENT_PROPERTY_INFO__Anonymous4_e__Union__Anonymous_e__Struct._fields_ = [
        ("_bitfield", UInt32),
    ]
    EVENT_PROPERTY_INFO__Anonymous4_e__Union._anonymous_ = [
        'Anonymous',
    ]
    EVENT_PROPERTY_INFO__Anonymous4_e__Union._fields_ = [
        ("Reserved", UInt32),
        ("Anonymous", EVENT_PROPERTY_INFO__Anonymous4_e__Union__Anonymous_e__Struct),
    ]
    class EVENT_PROPERTY_INFO__Anonymous2_e__Union(Union):
        pass
    EVENT_PROPERTY_INFO__Anonymous2_e__Union._fields_ = [
        ("count", UInt16),
        ("countPropertyIndex", UInt16),
    ]
    class EVENT_PROPERTY_INFO__Anonymous1_e__Union(Union):
        pass
    class EVENT_PROPERTY_INFO__Anonymous1_e__Union__customSchemaType(Structure):
        pass
    EVENT_PROPERTY_INFO__Anonymous1_e__Union__customSchemaType._fields_ = [
        ("InType", UInt16),
        ("OutType", UInt16),
        ("CustomSchemaOffset", UInt32),
    ]
    class EVENT_PROPERTY_INFO__Anonymous1_e__Union__nonStructType(Structure):
        pass
    EVENT_PROPERTY_INFO__Anonymous1_e__Union__nonStructType._fields_ = [
        ("InType", UInt16),
        ("OutType", UInt16),
        ("MapNameOffset", UInt32),
    ]
    class EVENT_PROPERTY_INFO__Anonymous1_e__Union__structType(Structure):
        pass
    EVENT_PROPERTY_INFO__Anonymous1_e__Union__structType._fields_ = [
        ("StructStartIndex", UInt16),
        ("NumOfStructMembers", UInt16),
        ("padding", UInt32),
    ]
    EVENT_PROPERTY_INFO__Anonymous1_e__Union._fields_ = [
        ("nonStructType", EVENT_PROPERTY_INFO__Anonymous1_e__Union__nonStructType),
        ("structType", EVENT_PROPERTY_INFO__Anonymous1_e__Union__structType),
        ("customSchemaType", EVENT_PROPERTY_INFO__Anonymous1_e__Union__customSchemaType),
    ]
    class EVENT_PROPERTY_INFO__Anonymous3_e__Union(Union):
        pass
    EVENT_PROPERTY_INFO__Anonymous3_e__Union._fields_ = [
        ("length", UInt16),
        ("lengthPropertyIndex", UInt16),
    ]
    EVENT_PROPERTY_INFO._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
        'Anonymous3',
        'Anonymous4',
    ]
    EVENT_PROPERTY_INFO._fields_ = [
        ("Flags", win32more.System.Diagnostics.Etw.PROPERTY_FLAGS),
        ("NameOffset", UInt32),
        ("Anonymous1", EVENT_PROPERTY_INFO__Anonymous1_e__Union),
        ("Anonymous2", EVENT_PROPERTY_INFO__Anonymous2_e__Union),
        ("Anonymous3", EVENT_PROPERTY_INFO__Anonymous3_e__Union),
        ("Anonymous4", EVENT_PROPERTY_INFO__Anonymous4_e__Union),
    ]
    return EVENT_PROPERTY_INFO
DECODING_SOURCE = Int32
DECODING_SOURCE_DecodingSourceXMLFile = 0
DECODING_SOURCE_DecodingSourceWbem = 1
DECODING_SOURCE_DecodingSourceWPP = 2
DECODING_SOURCE_DecodingSourceTlg = 3
DECODING_SOURCE_DecodingSourceMax = 4
TEMPLATE_FLAGS = Int32
TEMPLATE_EVENT_DATA = 1
TEMPLATE_USER_DATA = 2
TEMPLATE_CONTROL_GUID = 4
def _define_TRACE_EVENT_INFO_head():
    class TRACE_EVENT_INFO(Structure):
        pass
    return TRACE_EVENT_INFO
def _define_TRACE_EVENT_INFO():
    TRACE_EVENT_INFO = win32more.System.Diagnostics.Etw.TRACE_EVENT_INFO_head
    class TRACE_EVENT_INFO__Anonymous3_e__Union(Union):
        pass
    class TRACE_EVENT_INFO__Anonymous3_e__Union__Anonymous_e__Struct(Structure):
        pass
    TRACE_EVENT_INFO__Anonymous3_e__Union__Anonymous_e__Struct._fields_ = [
        ("_bitfield", UInt32),
    ]
    TRACE_EVENT_INFO__Anonymous3_e__Union._anonymous_ = [
        'Anonymous',
    ]
    TRACE_EVENT_INFO__Anonymous3_e__Union._fields_ = [
        ("Flags", win32more.System.Diagnostics.Etw.TEMPLATE_FLAGS),
        ("Anonymous", TRACE_EVENT_INFO__Anonymous3_e__Union__Anonymous_e__Struct),
    ]
    class TRACE_EVENT_INFO__Anonymous1_e__Union(Union):
        pass
    TRACE_EVENT_INFO__Anonymous1_e__Union._fields_ = [
        ("EventNameOffset", UInt32),
        ("ActivityIDNameOffset", UInt32),
    ]
    class TRACE_EVENT_INFO__Anonymous2_e__Union(Union):
        pass
    TRACE_EVENT_INFO__Anonymous2_e__Union._fields_ = [
        ("EventAttributesOffset", UInt32),
        ("RelatedActivityIDNameOffset", UInt32),
    ]
    TRACE_EVENT_INFO._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
        'Anonymous3',
    ]
    TRACE_EVENT_INFO._fields_ = [
        ("ProviderGuid", Guid),
        ("EventGuid", Guid),
        ("EventDescriptor", win32more.System.Diagnostics.Etw.EVENT_DESCRIPTOR),
        ("DecodingSource", win32more.System.Diagnostics.Etw.DECODING_SOURCE),
        ("ProviderNameOffset", UInt32),
        ("LevelNameOffset", UInt32),
        ("ChannelNameOffset", UInt32),
        ("KeywordsNameOffset", UInt32),
        ("TaskNameOffset", UInt32),
        ("OpcodeNameOffset", UInt32),
        ("EventMessageOffset", UInt32),
        ("ProviderMessageOffset", UInt32),
        ("BinaryXMLOffset", UInt32),
        ("BinaryXMLSize", UInt32),
        ("Anonymous1", TRACE_EVENT_INFO__Anonymous1_e__Union),
        ("Anonymous2", TRACE_EVENT_INFO__Anonymous2_e__Union),
        ("PropertyCount", UInt32),
        ("TopLevelPropertyCount", UInt32),
        ("Anonymous3", TRACE_EVENT_INFO__Anonymous3_e__Union),
        ("EventPropertyInfoArray", win32more.System.Diagnostics.Etw.EVENT_PROPERTY_INFO * 0),
    ]
    return TRACE_EVENT_INFO
def _define_PROPERTY_DATA_DESCRIPTOR_head():
    class PROPERTY_DATA_DESCRIPTOR(Structure):
        pass
    return PROPERTY_DATA_DESCRIPTOR
def _define_PROPERTY_DATA_DESCRIPTOR():
    PROPERTY_DATA_DESCRIPTOR = win32more.System.Diagnostics.Etw.PROPERTY_DATA_DESCRIPTOR_head
    PROPERTY_DATA_DESCRIPTOR._fields_ = [
        ("PropertyName", UInt64),
        ("ArrayIndex", UInt32),
        ("Reserved", UInt32),
    ]
    return PROPERTY_DATA_DESCRIPTOR
PAYLOAD_OPERATOR = Int32
PAYLOADFIELD_EQ = 0
PAYLOADFIELD_NE = 1
PAYLOADFIELD_LE = 2
PAYLOADFIELD_GT = 3
PAYLOADFIELD_LT = 4
PAYLOADFIELD_GE = 5
PAYLOADFIELD_BETWEEN = 6
PAYLOADFIELD_NOTBETWEEN = 7
PAYLOADFIELD_MODULO = 8
PAYLOADFIELD_CONTAINS = 20
PAYLOADFIELD_DOESNTCONTAIN = 21
PAYLOADFIELD_IS = 30
PAYLOADFIELD_ISNOT = 31
PAYLOADFIELD_INVALID = 32
def _define_PAYLOAD_FILTER_PREDICATE_head():
    class PAYLOAD_FILTER_PREDICATE(Structure):
        pass
    return PAYLOAD_FILTER_PREDICATE
def _define_PAYLOAD_FILTER_PREDICATE():
    PAYLOAD_FILTER_PREDICATE = win32more.System.Diagnostics.Etw.PAYLOAD_FILTER_PREDICATE_head
    PAYLOAD_FILTER_PREDICATE._fields_ = [
        ("FieldName", win32more.Foundation.PWSTR),
        ("CompareOp", UInt16),
        ("Value", win32more.Foundation.PWSTR),
    ]
    return PAYLOAD_FILTER_PREDICATE
def _define_PROVIDER_FILTER_INFO_head():
    class PROVIDER_FILTER_INFO(Structure):
        pass
    return PROVIDER_FILTER_INFO
def _define_PROVIDER_FILTER_INFO():
    PROVIDER_FILTER_INFO = win32more.System.Diagnostics.Etw.PROVIDER_FILTER_INFO_head
    PROVIDER_FILTER_INFO._fields_ = [
        ("Id", Byte),
        ("Version", Byte),
        ("MessageOffset", UInt32),
        ("Reserved", UInt32),
        ("PropertyCount", UInt32),
        ("EventPropertyInfoArray", win32more.System.Diagnostics.Etw.EVENT_PROPERTY_INFO * 0),
    ]
    return PROVIDER_FILTER_INFO
EVENT_FIELD_TYPE = Int32
EVENT_FIELD_TYPE_EventKeywordInformation = 0
EVENT_FIELD_TYPE_EventLevelInformation = 1
EVENT_FIELD_TYPE_EventChannelInformation = 2
EVENT_FIELD_TYPE_EventTaskInformation = 3
EVENT_FIELD_TYPE_EventOpcodeInformation = 4
EVENT_FIELD_TYPE_EventInformationMax = 5
def _define_PROVIDER_FIELD_INFO_head():
    class PROVIDER_FIELD_INFO(Structure):
        pass
    return PROVIDER_FIELD_INFO
def _define_PROVIDER_FIELD_INFO():
    PROVIDER_FIELD_INFO = win32more.System.Diagnostics.Etw.PROVIDER_FIELD_INFO_head
    PROVIDER_FIELD_INFO._fields_ = [
        ("NameOffset", UInt32),
        ("DescriptionOffset", UInt32),
        ("Value", UInt64),
    ]
    return PROVIDER_FIELD_INFO
def _define_PROVIDER_FIELD_INFOARRAY_head():
    class PROVIDER_FIELD_INFOARRAY(Structure):
        pass
    return PROVIDER_FIELD_INFOARRAY
def _define_PROVIDER_FIELD_INFOARRAY():
    PROVIDER_FIELD_INFOARRAY = win32more.System.Diagnostics.Etw.PROVIDER_FIELD_INFOARRAY_head
    PROVIDER_FIELD_INFOARRAY._fields_ = [
        ("NumberOfElements", UInt32),
        ("FieldType", win32more.System.Diagnostics.Etw.EVENT_FIELD_TYPE),
        ("FieldInfoArray", win32more.System.Diagnostics.Etw.PROVIDER_FIELD_INFO * 0),
    ]
    return PROVIDER_FIELD_INFOARRAY
def _define_TRACE_PROVIDER_INFO_head():
    class TRACE_PROVIDER_INFO(Structure):
        pass
    return TRACE_PROVIDER_INFO
def _define_TRACE_PROVIDER_INFO():
    TRACE_PROVIDER_INFO = win32more.System.Diagnostics.Etw.TRACE_PROVIDER_INFO_head
    TRACE_PROVIDER_INFO._fields_ = [
        ("ProviderGuid", Guid),
        ("SchemaSource", UInt32),
        ("ProviderNameOffset", UInt32),
    ]
    return TRACE_PROVIDER_INFO
def _define_PROVIDER_ENUMERATION_INFO_head():
    class PROVIDER_ENUMERATION_INFO(Structure):
        pass
    return PROVIDER_ENUMERATION_INFO
def _define_PROVIDER_ENUMERATION_INFO():
    PROVIDER_ENUMERATION_INFO = win32more.System.Diagnostics.Etw.PROVIDER_ENUMERATION_INFO_head
    PROVIDER_ENUMERATION_INFO._fields_ = [
        ("NumberOfProviders", UInt32),
        ("Reserved", UInt32),
        ("TraceProviderInfoArray", win32more.System.Diagnostics.Etw.TRACE_PROVIDER_INFO * 0),
    ]
    return PROVIDER_ENUMERATION_INFO
def _define_PROVIDER_EVENT_INFO_head():
    class PROVIDER_EVENT_INFO(Structure):
        pass
    return PROVIDER_EVENT_INFO
def _define_PROVIDER_EVENT_INFO():
    PROVIDER_EVENT_INFO = win32more.System.Diagnostics.Etw.PROVIDER_EVENT_INFO_head
    PROVIDER_EVENT_INFO._fields_ = [
        ("NumberOfEvents", UInt32),
        ("Reserved", UInt32),
        ("EventDescriptorsArray", win32more.System.Diagnostics.Etw.EVENT_DESCRIPTOR * 0),
    ]
    return PROVIDER_EVENT_INFO
TDH_CONTEXT_TYPE = Int32
TDH_CONTEXT_WPP_TMFFILE = 0
TDH_CONTEXT_WPP_TMFSEARCHPATH = 1
TDH_CONTEXT_WPP_GMT = 2
TDH_CONTEXT_POINTERSIZE = 3
TDH_CONTEXT_PDB_PATH = 4
TDH_CONTEXT_MAXIMUM = 5
def _define_TDH_CONTEXT_head():
    class TDH_CONTEXT(Structure):
        pass
    return TDH_CONTEXT
def _define_TDH_CONTEXT():
    TDH_CONTEXT = win32more.System.Diagnostics.Etw.TDH_CONTEXT_head
    TDH_CONTEXT._fields_ = [
        ("ParameterValue", UInt64),
        ("ParameterType", win32more.System.Diagnostics.Etw.TDH_CONTEXT_TYPE),
        ("ParameterSize", UInt32),
    ]
    return TDH_CONTEXT
CTraceRelogger = Guid('7b40792d-05ff-44c4-9058-f440c71f17d4')
def _define_ITraceEvent_head():
    class ITraceEvent(win32more.System.Com.IUnknown_head):
        Guid = Guid('8cc97f40-9028-4ff3-9b62-7d1f79ca7bcb')
    return ITraceEvent
def _define_ITraceEvent():
    ITraceEvent = win32more.System.Diagnostics.Etw.ITraceEvent_head
    ITraceEvent.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Diagnostics.Etw.ITraceEvent_head), use_last_error=False)(3, 'Clone', ((1, 'NewEvent'),)))
    ITraceEvent.GetUserContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(c_void_p), use_last_error=False)(4, 'GetUserContext', ((1, 'UserContext'),)))
    ITraceEvent.GetEventRecord = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Diagnostics.Etw.EVENT_RECORD_head)), use_last_error=False)(5, 'GetEventRecord', ((1, 'EventRecord'),)))
    ITraceEvent.SetPayload = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),UInt32, use_last_error=False)(6, 'SetPayload', ((1, 'Payload'),(1, 'PayloadSize'),)))
    ITraceEvent.SetEventDescriptor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Diagnostics.Etw.EVENT_DESCRIPTOR_head), use_last_error=False)(7, 'SetEventDescriptor', ((1, 'EventDescriptor'),)))
    ITraceEvent.SetProcessId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(8, 'SetProcessId', ((1, 'ProcessId'),)))
    ITraceEvent.SetProcessorIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(9, 'SetProcessorIndex', ((1, 'ProcessorIndex'),)))
    ITraceEvent.SetThreadId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(10, 'SetThreadId', ((1, 'ThreadId'),)))
    ITraceEvent.SetThreadTimes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(11, 'SetThreadTimes', ((1, 'KernelTime'),(1, 'UserTime'),)))
    ITraceEvent.SetActivityId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(12, 'SetActivityId', ((1, 'ActivityId'),)))
    ITraceEvent.SetTimeStamp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.LARGE_INTEGER_head), use_last_error=False)(13, 'SetTimeStamp', ((1, 'TimeStamp'),)))
    ITraceEvent.SetProviderId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(14, 'SetProviderId', ((1, 'ProviderId'),)))
    win32more.System.Com.IUnknown
    return ITraceEvent
def _define_ITraceEventCallback_head():
    class ITraceEventCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('3ed25501-593f-43e9-8f38-3ab46f5a4a52')
    return ITraceEventCallback
def _define_ITraceEventCallback():
    ITraceEventCallback = win32more.System.Diagnostics.Etw.ITraceEventCallback_head
    ITraceEventCallback.OnBeginProcessTrace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Diagnostics.Etw.ITraceEvent_head,win32more.System.Diagnostics.Etw.ITraceRelogger_head, use_last_error=False)(3, 'OnBeginProcessTrace', ((1, 'HeaderEvent'),(1, 'Relogger'),)))
    ITraceEventCallback.OnFinalizeProcessTrace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Diagnostics.Etw.ITraceRelogger_head, use_last_error=False)(4, 'OnFinalizeProcessTrace', ((1, 'Relogger'),)))
    ITraceEventCallback.OnEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Diagnostics.Etw.ITraceEvent_head,win32more.System.Diagnostics.Etw.ITraceRelogger_head, use_last_error=False)(5, 'OnEvent', ((1, 'Event'),(1, 'Relogger'),)))
    win32more.System.Com.IUnknown
    return ITraceEventCallback
def _define_ITraceRelogger_head():
    class ITraceRelogger(win32more.System.Com.IUnknown_head):
        Guid = Guid('f754ad43-3bcc-4286-8009-9c5da214e84e')
    return ITraceRelogger
def _define_ITraceRelogger():
    ITraceRelogger = win32more.System.Diagnostics.Etw.ITraceRelogger_head
    ITraceRelogger.AddLogfileTraceStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,c_void_p,POINTER(UInt64), use_last_error=False)(3, 'AddLogfileTraceStream', ((1, 'LogfileName'),(1, 'UserContext'),(1, 'TraceHandle'),)))
    ITraceRelogger.AddRealtimeTraceStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,c_void_p,POINTER(UInt64), use_last_error=False)(4, 'AddRealtimeTraceStream', ((1, 'LoggerName'),(1, 'UserContext'),(1, 'TraceHandle'),)))
    ITraceRelogger.RegisterCallback = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Diagnostics.Etw.ITraceEventCallback_head, use_last_error=False)(5, 'RegisterCallback', ((1, 'Callback'),)))
    ITraceRelogger.Inject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Diagnostics.Etw.ITraceEvent_head, use_last_error=False)(6, 'Inject', ((1, 'Event'),)))
    ITraceRelogger.CreateEventInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,UInt32,POINTER(win32more.System.Diagnostics.Etw.ITraceEvent_head), use_last_error=False)(7, 'CreateEventInstance', ((1, 'TraceHandle'),(1, 'Flags'),(1, 'Event'),)))
    ITraceRelogger.ProcessTrace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'ProcessTrace', ()))
    ITraceRelogger.SetOutputFilename = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(9, 'SetOutputFilename', ((1, 'LogfileName'),)))
    ITraceRelogger.SetCompressionMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOLEAN, use_last_error=False)(10, 'SetCompressionMode', ((1, 'CompressionMode'),)))
    ITraceRelogger.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(11, 'Cancel', ()))
    win32more.System.Com.IUnknown
    return ITraceRelogger
def _define_StartTraceW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt64),win32more.Foundation.PWSTR,POINTER(win32more.System.Diagnostics.Etw.EVENT_TRACE_PROPERTIES_head), use_last_error=False)(("StartTraceW", windll["ADVAPI32"]), ((1, 'TraceHandle'),(1, 'InstanceName'),(1, 'Properties'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_StartTrace():
    return win32more.System.Diagnostics.Etw.StartTraceW
def _define_StartTraceA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt64),win32more.Foundation.PSTR,POINTER(win32more.System.Diagnostics.Etw.EVENT_TRACE_PROPERTIES_head), use_last_error=False)(("StartTraceA", windll["ADVAPI32"]), ((1, 'TraceHandle'),(1, 'InstanceName'),(1, 'Properties'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_StopTraceW():
    try:
        return WINFUNCTYPE(UInt32,UInt64,win32more.Foundation.PWSTR,POINTER(win32more.System.Diagnostics.Etw.EVENT_TRACE_PROPERTIES_head), use_last_error=False)(("StopTraceW", windll["ADVAPI32"]), ((1, 'TraceHandle'),(1, 'InstanceName'),(1, 'Properties'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_StopTrace():
    return win32more.System.Diagnostics.Etw.StopTraceW
def _define_StopTraceA():
    try:
        return WINFUNCTYPE(UInt32,UInt64,win32more.Foundation.PSTR,POINTER(win32more.System.Diagnostics.Etw.EVENT_TRACE_PROPERTIES_head), use_last_error=False)(("StopTraceA", windll["ADVAPI32"]), ((1, 'TraceHandle'),(1, 'InstanceName'),(1, 'Properties'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryTraceW():
    try:
        return WINFUNCTYPE(UInt32,UInt64,win32more.Foundation.PWSTR,POINTER(win32more.System.Diagnostics.Etw.EVENT_TRACE_PROPERTIES_head), use_last_error=False)(("QueryTraceW", windll["ADVAPI32"]), ((1, 'TraceHandle'),(1, 'InstanceName'),(1, 'Properties'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryTrace():
    return win32more.System.Diagnostics.Etw.QueryTraceW
def _define_QueryTraceA():
    try:
        return WINFUNCTYPE(UInt32,UInt64,win32more.Foundation.PSTR,POINTER(win32more.System.Diagnostics.Etw.EVENT_TRACE_PROPERTIES_head), use_last_error=False)(("QueryTraceA", windll["ADVAPI32"]), ((1, 'TraceHandle'),(1, 'InstanceName'),(1, 'Properties'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UpdateTraceW():
    try:
        return WINFUNCTYPE(UInt32,UInt64,win32more.Foundation.PWSTR,POINTER(win32more.System.Diagnostics.Etw.EVENT_TRACE_PROPERTIES_head), use_last_error=False)(("UpdateTraceW", windll["ADVAPI32"]), ((1, 'TraceHandle'),(1, 'InstanceName'),(1, 'Properties'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UpdateTrace():
    return win32more.System.Diagnostics.Etw.UpdateTraceW
def _define_UpdateTraceA():
    try:
        return WINFUNCTYPE(UInt32,UInt64,win32more.Foundation.PSTR,POINTER(win32more.System.Diagnostics.Etw.EVENT_TRACE_PROPERTIES_head), use_last_error=False)(("UpdateTraceA", windll["ADVAPI32"]), ((1, 'TraceHandle'),(1, 'InstanceName'),(1, 'Properties'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FlushTraceW():
    try:
        return WINFUNCTYPE(UInt32,UInt64,win32more.Foundation.PWSTR,POINTER(win32more.System.Diagnostics.Etw.EVENT_TRACE_PROPERTIES_head), use_last_error=False)(("FlushTraceW", windll["ADVAPI32"]), ((1, 'TraceHandle'),(1, 'InstanceName'),(1, 'Properties'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FlushTrace():
    return win32more.System.Diagnostics.Etw.FlushTraceW
def _define_FlushTraceA():
    try:
        return WINFUNCTYPE(UInt32,UInt64,win32more.Foundation.PSTR,POINTER(win32more.System.Diagnostics.Etw.EVENT_TRACE_PROPERTIES_head), use_last_error=False)(("FlushTraceA", windll["ADVAPI32"]), ((1, 'TraceHandle'),(1, 'InstanceName'),(1, 'Properties'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ControlTraceW():
    try:
        return WINFUNCTYPE(UInt32,UInt64,win32more.Foundation.PWSTR,POINTER(win32more.System.Diagnostics.Etw.EVENT_TRACE_PROPERTIES_head),win32more.System.Diagnostics.Etw.EVENT_TRACE_CONTROL, use_last_error=False)(("ControlTraceW", windll["ADVAPI32"]), ((1, 'TraceHandle'),(1, 'InstanceName'),(1, 'Properties'),(1, 'ControlCode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ControlTrace():
    return win32more.System.Diagnostics.Etw.ControlTraceW
def _define_ControlTraceA():
    try:
        return WINFUNCTYPE(UInt32,UInt64,win32more.Foundation.PSTR,POINTER(win32more.System.Diagnostics.Etw.EVENT_TRACE_PROPERTIES_head),win32more.System.Diagnostics.Etw.EVENT_TRACE_CONTROL, use_last_error=False)(("ControlTraceA", windll["ADVAPI32"]), ((1, 'TraceHandle'),(1, 'InstanceName'),(1, 'Properties'),(1, 'ControlCode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryAllTracesW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(POINTER(win32more.System.Diagnostics.Etw.EVENT_TRACE_PROPERTIES_head)),UInt32,POINTER(UInt32), use_last_error=False)(("QueryAllTracesW", windll["ADVAPI32"]), ((1, 'PropertyArray'),(1, 'PropertyArrayCount'),(1, 'LoggerCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryAllTraces():
    return win32more.System.Diagnostics.Etw.QueryAllTracesW
def _define_QueryAllTracesA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(POINTER(win32more.System.Diagnostics.Etw.EVENT_TRACE_PROPERTIES_head)),UInt32,POINTER(UInt32), use_last_error=False)(("QueryAllTracesA", windll["ADVAPI32"]), ((1, 'PropertyArray'),(1, 'PropertyArrayCount'),(1, 'LoggerCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnableTrace():
    try:
        return WINFUNCTYPE(UInt32,UInt32,UInt32,UInt32,POINTER(Guid),UInt64, use_last_error=False)(("EnableTrace", windll["ADVAPI32"]), ((1, 'Enable'),(1, 'EnableFlag'),(1, 'EnableLevel'),(1, 'ControlGuid'),(1, 'TraceHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnableTraceEx():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Guid),POINTER(Guid),UInt64,UInt32,Byte,UInt64,UInt64,UInt32,POINTER(win32more.System.Diagnostics.Etw.EVENT_FILTER_DESCRIPTOR_head), use_last_error=False)(("EnableTraceEx", windll["ADVAPI32"]), ((1, 'ProviderId'),(1, 'SourceId'),(1, 'TraceHandle'),(1, 'IsEnabled'),(1, 'Level'),(1, 'MatchAnyKeyword'),(1, 'MatchAllKeyword'),(1, 'EnableProperty'),(1, 'EnableFilterDesc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnableTraceEx2():
    try:
        return WINFUNCTYPE(UInt32,UInt64,POINTER(Guid),UInt32,Byte,UInt64,UInt64,UInt32,POINTER(win32more.System.Diagnostics.Etw.ENABLE_TRACE_PARAMETERS_head), use_last_error=False)(("EnableTraceEx2", windll["ADVAPI32"]), ((1, 'TraceHandle'),(1, 'ProviderId'),(1, 'ControlCode'),(1, 'Level'),(1, 'MatchAnyKeyword'),(1, 'MatchAllKeyword'),(1, 'Timeout'),(1, 'EnableParameters'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumerateTraceGuidsEx():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Diagnostics.Etw.TRACE_QUERY_INFO_CLASS,c_void_p,UInt32,c_void_p,UInt32,POINTER(UInt32), use_last_error=False)(("EnumerateTraceGuidsEx", windll["ADVAPI32"]), ((1, 'TraceQueryInfoClass'),(1, 'InBuffer'),(1, 'InBufferSize'),(1, 'OutBuffer'),(1, 'OutBufferSize'),(1, 'ReturnLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TraceSetInformation():
    try:
        return WINFUNCTYPE(UInt32,UInt64,win32more.System.Diagnostics.Etw.TRACE_QUERY_INFO_CLASS,c_void_p,UInt32, use_last_error=False)(("TraceSetInformation", windll["ADVAPI32"]), ((1, 'SessionHandle'),(1, 'InformationClass'),(1, 'TraceInformation'),(1, 'InformationLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TraceQueryInformation():
    try:
        return WINFUNCTYPE(UInt32,UInt64,win32more.System.Diagnostics.Etw.TRACE_QUERY_INFO_CLASS,c_void_p,UInt32,POINTER(UInt32), use_last_error=False)(("TraceQueryInformation", windll["ADVAPI32"]), ((1, 'SessionHandle'),(1, 'InformationClass'),(1, 'TraceInformation'),(1, 'InformationLength'),(1, 'ReturnLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateTraceInstanceId():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(win32more.System.Diagnostics.Etw.EVENT_INSTANCE_INFO_head), use_last_error=False)(("CreateTraceInstanceId", windll["ADVAPI32"]), ((1, 'RegHandle'),(1, 'InstInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TraceEvent():
    try:
        return WINFUNCTYPE(UInt32,UInt64,POINTER(win32more.System.Diagnostics.Etw.EVENT_TRACE_HEADER_head), use_last_error=False)(("TraceEvent", windll["ADVAPI32"]), ((1, 'TraceHandle'),(1, 'EventTrace'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TraceEventInstance():
    try:
        return WINFUNCTYPE(UInt32,UInt64,POINTER(win32more.System.Diagnostics.Etw.EVENT_INSTANCE_HEADER_head),POINTER(win32more.System.Diagnostics.Etw.EVENT_INSTANCE_INFO_head),POINTER(win32more.System.Diagnostics.Etw.EVENT_INSTANCE_INFO_head), use_last_error=False)(("TraceEventInstance", windll["ADVAPI32"]), ((1, 'TraceHandle'),(1, 'EventTrace'),(1, 'InstInfo'),(1, 'ParentInstInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterTraceGuidsW():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Diagnostics.Etw.WMIDPREQUEST,c_void_p,POINTER(Guid),UInt32,POINTER(win32more.System.Diagnostics.Etw.TRACE_GUID_REGISTRATION),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt64), use_last_error=False)(("RegisterTraceGuidsW", windll["ADVAPI32"]), ((1, 'RequestAddress'),(1, 'RequestContext'),(1, 'ControlGuid'),(1, 'GuidCount'),(1, 'TraceGuidReg'),(1, 'MofImagePath'),(1, 'MofResourceName'),(1, 'RegistrationHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterTraceGuids():
    return win32more.System.Diagnostics.Etw.RegisterTraceGuidsW
def _define_RegisterTraceGuidsA():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Diagnostics.Etw.WMIDPREQUEST,c_void_p,POINTER(Guid),UInt32,POINTER(win32more.System.Diagnostics.Etw.TRACE_GUID_REGISTRATION),win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(UInt64), use_last_error=False)(("RegisterTraceGuidsA", windll["ADVAPI32"]), ((1, 'RequestAddress'),(1, 'RequestContext'),(1, 'ControlGuid'),(1, 'GuidCount'),(1, 'TraceGuidReg'),(1, 'MofImagePath'),(1, 'MofResourceName'),(1, 'RegistrationHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumerateTraceGuids():
    try:
        return WINFUNCTYPE(UInt32,POINTER(POINTER(win32more.System.Diagnostics.Etw.TRACE_GUID_PROPERTIES_head)),UInt32,POINTER(UInt32), use_last_error=False)(("EnumerateTraceGuids", windll["ADVAPI32"]), ((1, 'GuidPropertiesArray'),(1, 'PropertyArrayCount'),(1, 'GuidCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UnregisterTraceGuids():
    try:
        return WINFUNCTYPE(UInt32,UInt64, use_last_error=False)(("UnregisterTraceGuids", windll["ADVAPI32"]), ((1, 'RegistrationHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTraceLoggerHandle():
    try:
        return WINFUNCTYPE(UInt64,c_void_p, use_last_error=True)(("GetTraceLoggerHandle", windll["ADVAPI32"]), ((1, 'Buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTraceEnableLevel():
    try:
        return WINFUNCTYPE(Byte,UInt64, use_last_error=True)(("GetTraceEnableLevel", windll["ADVAPI32"]), ((1, 'TraceHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTraceEnableFlags():
    try:
        return WINFUNCTYPE(UInt32,UInt64, use_last_error=True)(("GetTraceEnableFlags", windll["ADVAPI32"]), ((1, 'TraceHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenTraceW():
    try:
        return WINFUNCTYPE(UInt64,POINTER(win32more.System.Diagnostics.Etw.EVENT_TRACE_LOGFILEW_head), use_last_error=True)(("OpenTraceW", windll["ADVAPI32"]), ((1, 'Logfile'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenTrace():
    return win32more.System.Diagnostics.Etw.OpenTraceW
def _define_ProcessTrace():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt64),UInt32,POINTER(win32more.Foundation.FILETIME_head),POINTER(win32more.Foundation.FILETIME_head), use_last_error=False)(("ProcessTrace", windll["ADVAPI32"]), ((1, 'HandleArray'),(1, 'HandleCount'),(1, 'StartTime'),(1, 'EndTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CloseTrace():
    try:
        return WINFUNCTYPE(UInt32,UInt64, use_last_error=False)(("CloseTrace", windll["ADVAPI32"]), ((1, 'TraceHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryTraceProcessingHandle():
    try:
        return WINFUNCTYPE(UInt32,UInt64,win32more.System.Diagnostics.Etw.ETW_PROCESS_HANDLE_INFO_TYPE,c_void_p,UInt32,c_void_p,UInt32,POINTER(UInt32), use_last_error=False)(("QueryTraceProcessingHandle", windll["ADVAPI32"]), ((1, 'ProcessingHandle'),(1, 'InformationClass'),(1, 'InBuffer'),(1, 'InBufferSize'),(1, 'OutBuffer'),(1, 'OutBufferSize'),(1, 'ReturnLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenTraceA():
    try:
        return WINFUNCTYPE(UInt64,POINTER(win32more.System.Diagnostics.Etw.EVENT_TRACE_LOGFILEA_head), use_last_error=True)(("OpenTraceA", windll["ADVAPI32"]), ((1, 'Logfile'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetTraceCallback():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Guid),win32more.System.Diagnostics.Etw.PEVENT_CALLBACK, use_last_error=False)(("SetTraceCallback", windll["ADVAPI32"]), ((1, 'pGuid'),(1, 'EventCallback'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RemoveTraceCallback():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Guid), use_last_error=False)(("RemoveTraceCallback", windll["ADVAPI32"]), ((1, 'pGuid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TraceMessage():
    try:
        return WINFUNCTYPE(UInt32,UInt64,win32more.System.Diagnostics.Etw.TRACE_MESSAGE_FLAGS,POINTER(Guid),UInt16, use_last_error=False)(("TraceMessage", windll["ADVAPI32"]), ((1, 'LoggerHandle'),(1, 'MessageFlags'),(1, 'MessageGuid'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TraceMessageVa():
    try:
        return WINFUNCTYPE(UInt32,UInt64,win32more.System.Diagnostics.Etw.TRACE_MESSAGE_FLAGS,POINTER(Guid),UInt16,POINTER(SByte), use_last_error=False)(("TraceMessageVa", windll["ADVAPI32"]), ((1, 'LoggerHandle'),(1, 'MessageFlags'),(1, 'MessageGuid'),(1, 'MessageNumber'),(1, 'MessageArgList'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EventRegister():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Guid),win32more.System.Diagnostics.Etw.PENABLECALLBACK,c_void_p,POINTER(UInt64), use_last_error=False)(("EventRegister", windll["ADVAPI32"]), ((1, 'ProviderId'),(1, 'EnableCallback'),(1, 'CallbackContext'),(1, 'RegHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EventUnregister():
    try:
        return WINFUNCTYPE(UInt32,UInt64, use_last_error=False)(("EventUnregister", windll["ADVAPI32"]), ((1, 'RegHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EventSetInformation():
    try:
        return WINFUNCTYPE(UInt32,UInt64,win32more.System.Diagnostics.Etw.EVENT_INFO_CLASS,c_void_p,UInt32, use_last_error=False)(("EventSetInformation", windll["ADVAPI32"]), ((1, 'RegHandle'),(1, 'InformationClass'),(1, 'EventInformation'),(1, 'InformationLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EventEnabled():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,UInt64,POINTER(win32more.System.Diagnostics.Etw.EVENT_DESCRIPTOR_head), use_last_error=False)(("EventEnabled", windll["ADVAPI32"]), ((1, 'RegHandle'),(1, 'EventDescriptor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EventProviderEnabled():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,UInt64,Byte,UInt64, use_last_error=False)(("EventProviderEnabled", windll["ADVAPI32"]), ((1, 'RegHandle'),(1, 'Level'),(1, 'Keyword'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EventWrite():
    try:
        return WINFUNCTYPE(UInt32,UInt64,POINTER(win32more.System.Diagnostics.Etw.EVENT_DESCRIPTOR_head),UInt32,POINTER(win32more.System.Diagnostics.Etw.EVENT_DATA_DESCRIPTOR), use_last_error=False)(("EventWrite", windll["ADVAPI32"]), ((1, 'RegHandle'),(1, 'EventDescriptor'),(1, 'UserDataCount'),(1, 'UserData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EventWriteTransfer():
    try:
        return WINFUNCTYPE(UInt32,UInt64,POINTER(win32more.System.Diagnostics.Etw.EVENT_DESCRIPTOR_head),POINTER(Guid),POINTER(Guid),UInt32,POINTER(win32more.System.Diagnostics.Etw.EVENT_DATA_DESCRIPTOR), use_last_error=False)(("EventWriteTransfer", windll["ADVAPI32"]), ((1, 'RegHandle'),(1, 'EventDescriptor'),(1, 'ActivityId'),(1, 'RelatedActivityId'),(1, 'UserDataCount'),(1, 'UserData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EventWriteEx():
    try:
        return WINFUNCTYPE(UInt32,UInt64,POINTER(win32more.System.Diagnostics.Etw.EVENT_DESCRIPTOR_head),UInt64,UInt32,POINTER(Guid),POINTER(Guid),UInt32,POINTER(win32more.System.Diagnostics.Etw.EVENT_DATA_DESCRIPTOR), use_last_error=False)(("EventWriteEx", windll["ADVAPI32"]), ((1, 'RegHandle'),(1, 'EventDescriptor'),(1, 'Filter'),(1, 'Flags'),(1, 'ActivityId'),(1, 'RelatedActivityId'),(1, 'UserDataCount'),(1, 'UserData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EventWriteString():
    try:
        return WINFUNCTYPE(UInt32,UInt64,Byte,UInt64,win32more.Foundation.PWSTR, use_last_error=False)(("EventWriteString", windll["ADVAPI32"]), ((1, 'RegHandle'),(1, 'Level'),(1, 'Keyword'),(1, 'String'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EventActivityIdControl():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(Guid), use_last_error=False)(("EventActivityIdControl", windll["ADVAPI32"]), ((1, 'ControlCode'),(1, 'ActivityId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EventAccessControl():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Guid),UInt32,win32more.Foundation.PSID,UInt32,win32more.Foundation.BOOLEAN, use_last_error=False)(("EventAccessControl", windll["ADVAPI32"]), ((1, 'Guid'),(1, 'Operation'),(1, 'Sid'),(1, 'Rights'),(1, 'AllowOrDeny'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EventAccessQuery():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Guid),POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),POINTER(UInt32), use_last_error=False)(("EventAccessQuery", windll["ADVAPI32"]), ((1, 'Guid'),(1, 'Buffer'),(1, 'BufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EventAccessRemove():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Guid), use_last_error=False)(("EventAccessRemove", windll["ADVAPI32"]), ((1, 'Guid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TdhCreatePayloadFilter():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Guid),POINTER(win32more.System.Diagnostics.Etw.EVENT_DESCRIPTOR_head),win32more.Foundation.BOOLEAN,UInt32,POINTER(win32more.System.Diagnostics.Etw.PAYLOAD_FILTER_PREDICATE),POINTER(c_void_p), use_last_error=False)(("TdhCreatePayloadFilter", windll["tdh"]), ((1, 'ProviderGuid'),(1, 'EventDescriptor'),(1, 'EventMatchANY'),(1, 'PayloadPredicateCount'),(1, 'PayloadPredicates'),(1, 'PayloadFilter'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TdhDeletePayloadFilter():
    try:
        return WINFUNCTYPE(UInt32,POINTER(c_void_p), use_last_error=False)(("TdhDeletePayloadFilter", windll["tdh"]), ((1, 'PayloadFilter'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TdhAggregatePayloadFilters():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(c_void_p),POINTER(win32more.Foundation.BOOLEAN),POINTER(win32more.System.Diagnostics.Etw.EVENT_FILTER_DESCRIPTOR_head), use_last_error=False)(("TdhAggregatePayloadFilters", windll["tdh"]), ((1, 'PayloadFilterCount'),(1, 'PayloadFilterPtrs'),(1, 'EventMatchALLFlags'),(1, 'EventFilterDescriptor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TdhCleanupPayloadEventFilterDescriptor():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Diagnostics.Etw.EVENT_FILTER_DESCRIPTOR_head), use_last_error=False)(("TdhCleanupPayloadEventFilterDescriptor", windll["tdh"]), ((1, 'EventFilterDescriptor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TdhGetEventInformation():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Diagnostics.Etw.EVENT_RECORD_head),UInt32,POINTER(win32more.System.Diagnostics.Etw.TDH_CONTEXT),POINTER(win32more.System.Diagnostics.Etw.TRACE_EVENT_INFO_head),POINTER(UInt32), use_last_error=False)(("TdhGetEventInformation", windll["TDH"]), ((1, 'Event'),(1, 'TdhContextCount'),(1, 'TdhContext'),(1, 'Buffer'),(1, 'BufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TdhGetEventMapInformation():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Diagnostics.Etw.EVENT_RECORD_head),win32more.Foundation.PWSTR,POINTER(win32more.System.Diagnostics.Etw.EVENT_MAP_INFO_head),POINTER(UInt32), use_last_error=False)(("TdhGetEventMapInformation", windll["TDH"]), ((1, 'pEvent'),(1, 'pMapName'),(1, 'pBuffer'),(1, 'pBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TdhGetPropertySize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Diagnostics.Etw.EVENT_RECORD_head),UInt32,POINTER(win32more.System.Diagnostics.Etw.TDH_CONTEXT),UInt32,POINTER(win32more.System.Diagnostics.Etw.PROPERTY_DATA_DESCRIPTOR),POINTER(UInt32), use_last_error=False)(("TdhGetPropertySize", windll["TDH"]), ((1, 'pEvent'),(1, 'TdhContextCount'),(1, 'pTdhContext'),(1, 'PropertyDataCount'),(1, 'pPropertyData'),(1, 'pPropertySize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TdhGetProperty():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Diagnostics.Etw.EVENT_RECORD_head),UInt32,POINTER(win32more.System.Diagnostics.Etw.TDH_CONTEXT),UInt32,POINTER(win32more.System.Diagnostics.Etw.PROPERTY_DATA_DESCRIPTOR),UInt32,c_char_p_no, use_last_error=False)(("TdhGetProperty", windll["TDH"]), ((1, 'pEvent'),(1, 'TdhContextCount'),(1, 'pTdhContext'),(1, 'PropertyDataCount'),(1, 'pPropertyData'),(1, 'BufferSize'),(1, 'pBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TdhEnumerateProviders():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Diagnostics.Etw.PROVIDER_ENUMERATION_INFO_head),POINTER(UInt32), use_last_error=False)(("TdhEnumerateProviders", windll["TDH"]), ((1, 'pBuffer'),(1, 'pBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TdhEnumerateProvidersForDecodingSource():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Diagnostics.Etw.DECODING_SOURCE,POINTER(win32more.System.Diagnostics.Etw.PROVIDER_ENUMERATION_INFO_head),UInt32,POINTER(UInt32), use_last_error=False)(("TdhEnumerateProvidersForDecodingSource", windll["tdh"]), ((1, 'filter'),(1, 'buffer'),(1, 'bufferSize'),(1, 'bufferRequired'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TdhQueryProviderFieldInformation():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Guid),UInt64,win32more.System.Diagnostics.Etw.EVENT_FIELD_TYPE,POINTER(win32more.System.Diagnostics.Etw.PROVIDER_FIELD_INFOARRAY_head),POINTER(UInt32), use_last_error=False)(("TdhQueryProviderFieldInformation", windll["TDH"]), ((1, 'pGuid'),(1, 'EventFieldValue'),(1, 'EventFieldType'),(1, 'pBuffer'),(1, 'pBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TdhEnumerateProviderFieldInformation():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Guid),win32more.System.Diagnostics.Etw.EVENT_FIELD_TYPE,POINTER(win32more.System.Diagnostics.Etw.PROVIDER_FIELD_INFOARRAY_head),POINTER(UInt32), use_last_error=False)(("TdhEnumerateProviderFieldInformation", windll["TDH"]), ((1, 'pGuid'),(1, 'EventFieldType'),(1, 'pBuffer'),(1, 'pBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TdhEnumerateProviderFilters():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Guid),UInt32,POINTER(win32more.System.Diagnostics.Etw.TDH_CONTEXT),POINTER(UInt32),POINTER(POINTER(win32more.System.Diagnostics.Etw.PROVIDER_FILTER_INFO_head)),POINTER(UInt32), use_last_error=False)(("TdhEnumerateProviderFilters", windll["tdh"]), ((1, 'Guid'),(1, 'TdhContextCount'),(1, 'TdhContext'),(1, 'FilterCount'),(1, 'Buffer'),(1, 'BufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TdhLoadManifest():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR, use_last_error=False)(("TdhLoadManifest", windll["TDH"]), ((1, 'Manifest'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TdhLoadManifestFromMemory():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,UInt32, use_last_error=False)(("TdhLoadManifestFromMemory", windll["TDH"]), ((1, 'pData'),(1, 'cbData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TdhUnloadManifest():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR, use_last_error=False)(("TdhUnloadManifest", windll["TDH"]), ((1, 'Manifest'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TdhUnloadManifestFromMemory():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,UInt32, use_last_error=False)(("TdhUnloadManifestFromMemory", windll["TDH"]), ((1, 'pData'),(1, 'cbData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TdhFormatProperty():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Diagnostics.Etw.TRACE_EVENT_INFO_head),POINTER(win32more.System.Diagnostics.Etw.EVENT_MAP_INFO_head),UInt32,UInt16,UInt16,UInt16,UInt16,c_char_p_no,POINTER(UInt32),win32more.Foundation.PWSTR,POINTER(UInt16), use_last_error=False)(("TdhFormatProperty", windll["TDH"]), ((1, 'EventInfo'),(1, 'MapInfo'),(1, 'PointerSize'),(1, 'PropertyInType'),(1, 'PropertyOutType'),(1, 'PropertyLength'),(1, 'UserDataLength'),(1, 'UserData'),(1, 'BufferSize'),(1, 'Buffer'),(1, 'UserDataConsumed'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TdhOpenDecodingHandle():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Diagnostics.Etw.TDH_HANDLE), use_last_error=False)(("TdhOpenDecodingHandle", windll["tdh"]), ((1, 'Handle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TdhSetDecodingParameter():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Diagnostics.Etw.TDH_HANDLE,POINTER(win32more.System.Diagnostics.Etw.TDH_CONTEXT_head), use_last_error=False)(("TdhSetDecodingParameter", windll["tdh"]), ((1, 'Handle'),(1, 'TdhContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TdhGetDecodingParameter():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Diagnostics.Etw.TDH_HANDLE,POINTER(win32more.System.Diagnostics.Etw.TDH_CONTEXT_head), use_last_error=False)(("TdhGetDecodingParameter", windll["tdh"]), ((1, 'Handle'),(1, 'TdhContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TdhGetWppProperty():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Diagnostics.Etw.TDH_HANDLE,POINTER(win32more.System.Diagnostics.Etw.EVENT_RECORD_head),win32more.Foundation.PWSTR,POINTER(UInt32),c_char_p_no, use_last_error=False)(("TdhGetWppProperty", windll["tdh"]), ((1, 'Handle'),(1, 'EventRecord'),(1, 'PropertyName'),(1, 'BufferSize'),(1, 'Buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TdhGetWppMessage():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Diagnostics.Etw.TDH_HANDLE,POINTER(win32more.System.Diagnostics.Etw.EVENT_RECORD_head),POINTER(UInt32),c_char_p_no, use_last_error=False)(("TdhGetWppMessage", windll["tdh"]), ((1, 'Handle'),(1, 'EventRecord'),(1, 'BufferSize'),(1, 'Buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TdhCloseDecodingHandle():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Diagnostics.Etw.TDH_HANDLE, use_last_error=False)(("TdhCloseDecodingHandle", windll["tdh"]), ((1, 'Handle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TdhLoadManifestFromBinary():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR, use_last_error=False)(("TdhLoadManifestFromBinary", windll["tdh"]), ((1, 'BinaryPath'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TdhEnumerateManifestProviderEvents():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Guid),POINTER(win32more.System.Diagnostics.Etw.PROVIDER_EVENT_INFO_head),POINTER(UInt32), use_last_error=False)(("TdhEnumerateManifestProviderEvents", windll["TDH"]), ((1, 'ProviderGuid'),(1, 'Buffer'),(1, 'BufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TdhGetManifestEventInformation():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Guid),POINTER(win32more.System.Diagnostics.Etw.EVENT_DESCRIPTOR_head),POINTER(win32more.System.Diagnostics.Etw.TRACE_EVENT_INFO_head),POINTER(UInt32), use_last_error=False)(("TdhGetManifestEventInformation", windll["TDH"]), ((1, 'ProviderGuid'),(1, 'EventDescriptor'),(1, 'Buffer'),(1, 'BufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CveEventWrite():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("CveEventWrite", windll["ADVAPI32"]), ((1, 'CveId'),(1, 'AdditionalDetails'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "WNODE_FLAG_ALL_DATA",
    "WNODE_FLAG_SINGLE_INSTANCE",
    "WNODE_FLAG_SINGLE_ITEM",
    "WNODE_FLAG_EVENT_ITEM",
    "WNODE_FLAG_FIXED_INSTANCE_SIZE",
    "WNODE_FLAG_TOO_SMALL",
    "WNODE_FLAG_INSTANCES_SAME",
    "WNODE_FLAG_STATIC_INSTANCE_NAMES",
    "WNODE_FLAG_INTERNAL",
    "WNODE_FLAG_USE_TIMESTAMP",
    "WNODE_FLAG_PERSIST_EVENT",
    "WNODE_FLAG_EVENT_REFERENCE",
    "WNODE_FLAG_ANSI_INSTANCENAMES",
    "WNODE_FLAG_METHOD_ITEM",
    "WNODE_FLAG_PDO_INSTANCE_NAMES",
    "WNODE_FLAG_TRACED_GUID",
    "WNODE_FLAG_LOG_WNODE",
    "WNODE_FLAG_USE_GUID_PTR",
    "WNODE_FLAG_USE_MOF_PTR",
    "WNODE_FLAG_NO_HEADER",
    "WNODE_FLAG_SEND_DATA_BLOCK",
    "WNODE_FLAG_VERSIONED_PROPERTIES",
    "WNODE_FLAG_SEVERITY_MASK",
    "WMIREG_FLAG_EXPENSIVE",
    "WMIREG_FLAG_INSTANCE_LIST",
    "WMIREG_FLAG_INSTANCE_BASENAME",
    "WMIREG_FLAG_INSTANCE_PDO",
    "WMIREG_FLAG_REMOVE_GUID",
    "WMIREG_FLAG_RESERVED1",
    "WMIREG_FLAG_RESERVED2",
    "WMIREG_FLAG_TRACED_GUID",
    "WMIREG_FLAG_TRACE_CONTROL_GUID",
    "WMIREG_FLAG_EVENT_ONLY_GUID",
    "WMI_GUIDTYPE_TRACECONTROL",
    "WMI_GUIDTYPE_TRACE",
    "WMI_GUIDTYPE_DATA",
    "WMI_GUIDTYPE_EVENT",
    "WMIGUID_QUERY",
    "WMIGUID_SET",
    "WMIGUID_NOTIFICATION",
    "WMIGUID_READ_DESCRIPTION",
    "WMIGUID_EXECUTE",
    "TRACELOG_CREATE_REALTIME",
    "TRACELOG_CREATE_ONDISK",
    "TRACELOG_GUID_ENABLE",
    "TRACELOG_ACCESS_KERNEL_LOGGER",
    "TRACELOG_LOG_EVENT",
    "TRACELOG_CREATE_INPROC",
    "TRACELOG_ACCESS_REALTIME",
    "TRACELOG_REGISTER_GUIDS",
    "TRACELOG_JOIN_GROUP",
    "WMI_GLOBAL_LOGGER_ID",
    "MAX_PAYLOAD_PREDICATES",
    "EventTraceGuid",
    "SystemTraceControlGuid",
    "EventTraceConfigGuid",
    "DefaultTraceSecurityGuid",
    "PrivateLoggerNotificationGuid",
    "SystemIoFilterProviderGuid",
    "SystemObjectProviderGuid",
    "SystemPowerProviderGuid",
    "SystemHypervisorProviderGuid",
    "SystemLockProviderGuid",
    "SystemConfigProviderGuid",
    "SystemCpuProviderGuid",
    "SystemSchedulerProviderGuid",
    "SystemProfileProviderGuid",
    "SystemIoProviderGuid",
    "SystemMemoryProviderGuid",
    "SystemRegistryProviderGuid",
    "SystemProcessProviderGuid",
    "SystemAlpcProviderGuid",
    "SystemSyscallProviderGuid",
    "SystemInterruptProviderGuid",
    "SystemTimerProviderGuid",
    "MAX_MOF_FIELDS",
    "SYSTEM_EVENT_TYPE",
    "EVENT_TRACE_TYPE_INFO",
    "EVENT_TRACE_TYPE_START",
    "EVENT_TRACE_TYPE_END",
    "EVENT_TRACE_TYPE_STOP",
    "EVENT_TRACE_TYPE_DC_START",
    "EVENT_TRACE_TYPE_DC_END",
    "EVENT_TRACE_TYPE_EXTENSION",
    "EVENT_TRACE_TYPE_REPLY",
    "EVENT_TRACE_TYPE_DEQUEUE",
    "EVENT_TRACE_TYPE_RESUME",
    "EVENT_TRACE_TYPE_CHECKPOINT",
    "EVENT_TRACE_TYPE_SUSPEND",
    "EVENT_TRACE_TYPE_WINEVT_SEND",
    "EVENT_TRACE_TYPE_WINEVT_RECEIVE",
    "TRACE_LEVEL_NONE",
    "TRACE_LEVEL_CRITICAL",
    "TRACE_LEVEL_FATAL",
    "TRACE_LEVEL_ERROR",
    "TRACE_LEVEL_WARNING",
    "TRACE_LEVEL_INFORMATION",
    "TRACE_LEVEL_VERBOSE",
    "TRACE_LEVEL_RESERVED6",
    "TRACE_LEVEL_RESERVED7",
    "TRACE_LEVEL_RESERVED8",
    "TRACE_LEVEL_RESERVED9",
    "EVENT_TRACE_TYPE_LOAD",
    "EVENT_TRACE_TYPE_TERMINATE",
    "EVENT_TRACE_TYPE_IO_READ",
    "EVENT_TRACE_TYPE_IO_WRITE",
    "EVENT_TRACE_TYPE_IO_READ_INIT",
    "EVENT_TRACE_TYPE_IO_WRITE_INIT",
    "EVENT_TRACE_TYPE_IO_FLUSH",
    "EVENT_TRACE_TYPE_IO_FLUSH_INIT",
    "EVENT_TRACE_TYPE_IO_REDIRECTED_INIT",
    "EVENT_TRACE_TYPE_MM_TF",
    "EVENT_TRACE_TYPE_MM_DZF",
    "EVENT_TRACE_TYPE_MM_COW",
    "EVENT_TRACE_TYPE_MM_GPF",
    "EVENT_TRACE_TYPE_MM_HPF",
    "EVENT_TRACE_TYPE_MM_AV",
    "EVENT_TRACE_TYPE_SEND",
    "EVENT_TRACE_TYPE_RECEIVE",
    "EVENT_TRACE_TYPE_CONNECT",
    "EVENT_TRACE_TYPE_DISCONNECT",
    "EVENT_TRACE_TYPE_RETRANSMIT",
    "EVENT_TRACE_TYPE_ACCEPT",
    "EVENT_TRACE_TYPE_RECONNECT",
    "EVENT_TRACE_TYPE_CONNFAIL",
    "EVENT_TRACE_TYPE_COPY_TCP",
    "EVENT_TRACE_TYPE_COPY_ARP",
    "EVENT_TRACE_TYPE_ACKFULL",
    "EVENT_TRACE_TYPE_ACKPART",
    "EVENT_TRACE_TYPE_ACKDUP",
    "EVENT_TRACE_TYPE_GUIDMAP",
    "EVENT_TRACE_TYPE_CONFIG",
    "EVENT_TRACE_TYPE_SIDINFO",
    "EVENT_TRACE_TYPE_SECURITY",
    "EVENT_TRACE_TYPE_DBGID_RSDS",
    "EVENT_TRACE_TYPE_REGCREATE",
    "EVENT_TRACE_TYPE_REGOPEN",
    "EVENT_TRACE_TYPE_REGDELETE",
    "EVENT_TRACE_TYPE_REGQUERY",
    "EVENT_TRACE_TYPE_REGSETVALUE",
    "EVENT_TRACE_TYPE_REGDELETEVALUE",
    "EVENT_TRACE_TYPE_REGQUERYVALUE",
    "EVENT_TRACE_TYPE_REGENUMERATEKEY",
    "EVENT_TRACE_TYPE_REGENUMERATEVALUEKEY",
    "EVENT_TRACE_TYPE_REGQUERYMULTIPLEVALUE",
    "EVENT_TRACE_TYPE_REGSETINFORMATION",
    "EVENT_TRACE_TYPE_REGFLUSH",
    "EVENT_TRACE_TYPE_REGKCBCREATE",
    "EVENT_TRACE_TYPE_REGKCBDELETE",
    "EVENT_TRACE_TYPE_REGKCBRUNDOWNBEGIN",
    "EVENT_TRACE_TYPE_REGKCBRUNDOWNEND",
    "EVENT_TRACE_TYPE_REGVIRTUALIZE",
    "EVENT_TRACE_TYPE_REGCLOSE",
    "EVENT_TRACE_TYPE_REGSETSECURITY",
    "EVENT_TRACE_TYPE_REGQUERYSECURITY",
    "EVENT_TRACE_TYPE_REGCOMMIT",
    "EVENT_TRACE_TYPE_REGPREPARE",
    "EVENT_TRACE_TYPE_REGROLLBACK",
    "EVENT_TRACE_TYPE_REGMOUNTHIVE",
    "EVENT_TRACE_TYPE_CONFIG_CPU",
    "EVENT_TRACE_TYPE_CONFIG_PHYSICALDISK",
    "EVENT_TRACE_TYPE_CONFIG_LOGICALDISK",
    "EVENT_TRACE_TYPE_CONFIG_NIC",
    "EVENT_TRACE_TYPE_CONFIG_VIDEO",
    "EVENT_TRACE_TYPE_CONFIG_SERVICES",
    "EVENT_TRACE_TYPE_CONFIG_POWER",
    "EVENT_TRACE_TYPE_CONFIG_NETINFO",
    "EVENT_TRACE_TYPE_CONFIG_OPTICALMEDIA",
    "EVENT_TRACE_TYPE_CONFIG_IRQ",
    "EVENT_TRACE_TYPE_CONFIG_PNP",
    "EVENT_TRACE_TYPE_CONFIG_IDECHANNEL",
    "EVENT_TRACE_TYPE_CONFIG_NUMANODE",
    "EVENT_TRACE_TYPE_CONFIG_PLATFORM",
    "EVENT_TRACE_TYPE_CONFIG_PROCESSORGROUP",
    "EVENT_TRACE_TYPE_CONFIG_PROCESSORNUMBER",
    "EVENT_TRACE_TYPE_CONFIG_DPI",
    "EVENT_TRACE_TYPE_CONFIG_CI_INFO",
    "EVENT_TRACE_TYPE_CONFIG_MACHINEID",
    "EVENT_TRACE_TYPE_CONFIG_DEFRAG",
    "EVENT_TRACE_TYPE_CONFIG_MOBILEPLATFORM",
    "EVENT_TRACE_TYPE_CONFIG_DEVICEFAMILY",
    "EVENT_TRACE_TYPE_CONFIG_FLIGHTID",
    "EVENT_TRACE_TYPE_CONFIG_PROCESSOR",
    "EVENT_TRACE_TYPE_CONFIG_VIRTUALIZATION",
    "EVENT_TRACE_TYPE_CONFIG_BOOT",
    "EVENT_TRACE_TYPE_OPTICAL_IO_READ",
    "EVENT_TRACE_TYPE_OPTICAL_IO_WRITE",
    "EVENT_TRACE_TYPE_OPTICAL_IO_FLUSH",
    "EVENT_TRACE_TYPE_OPTICAL_IO_READ_INIT",
    "EVENT_TRACE_TYPE_OPTICAL_IO_WRITE_INIT",
    "EVENT_TRACE_TYPE_OPTICAL_IO_FLUSH_INIT",
    "EVENT_TRACE_TYPE_FLT_PREOP_INIT",
    "EVENT_TRACE_TYPE_FLT_POSTOP_INIT",
    "EVENT_TRACE_TYPE_FLT_PREOP_COMPLETION",
    "EVENT_TRACE_TYPE_FLT_POSTOP_COMPLETION",
    "EVENT_TRACE_TYPE_FLT_PREOP_FAILURE",
    "EVENT_TRACE_TYPE_FLT_POSTOP_FAILURE",
    "EVENT_TRACE_FLAG_DEBUG_EVENTS",
    "EVENT_TRACE_FLAG_EXTENSION",
    "EVENT_TRACE_FLAG_FORWARD_WMI",
    "EVENT_TRACE_FLAG_ENABLE_RESERVE",
    "EVENT_TRACE_FILE_MODE_NONE",
    "EVENT_TRACE_FILE_MODE_SEQUENTIAL",
    "EVENT_TRACE_FILE_MODE_CIRCULAR",
    "EVENT_TRACE_FILE_MODE_APPEND",
    "EVENT_TRACE_REAL_TIME_MODE",
    "EVENT_TRACE_DELAY_OPEN_FILE_MODE",
    "EVENT_TRACE_BUFFERING_MODE",
    "EVENT_TRACE_PRIVATE_LOGGER_MODE",
    "EVENT_TRACE_ADD_HEADER_MODE",
    "EVENT_TRACE_USE_GLOBAL_SEQUENCE",
    "EVENT_TRACE_USE_LOCAL_SEQUENCE",
    "EVENT_TRACE_RELOG_MODE",
    "EVENT_TRACE_USE_PAGED_MEMORY",
    "EVENT_TRACE_FILE_MODE_NEWFILE",
    "EVENT_TRACE_FILE_MODE_PREALLOCATE",
    "EVENT_TRACE_NONSTOPPABLE_MODE",
    "EVENT_TRACE_SECURE_MODE",
    "EVENT_TRACE_USE_KBYTES_FOR_SIZE",
    "EVENT_TRACE_PRIVATE_IN_PROC",
    "EVENT_TRACE_MODE_RESERVED",
    "EVENT_TRACE_NO_PER_PROCESSOR_BUFFERING",
    "EVENT_TRACE_SYSTEM_LOGGER_MODE",
    "EVENT_TRACE_ADDTO_TRIAGE_DUMP",
    "EVENT_TRACE_STOP_ON_HYBRID_SHUTDOWN",
    "EVENT_TRACE_PERSIST_ON_HYBRID_SHUTDOWN",
    "EVENT_TRACE_INDEPENDENT_SESSION_MODE",
    "EVENT_TRACE_COMPRESSED_MODE",
    "EVENT_TRACE_CONTROL_INCREMENT_FILE",
    "EVENT_TRACE_CONTROL_CONVERT_TO_REALTIME",
    "TRACE_MESSAGE_PERFORMANCE_TIMESTAMP",
    "TRACE_MESSAGE_POINTER32",
    "TRACE_MESSAGE_POINTER64",
    "TRACE_MESSAGE_FLAG_MASK",
    "EVENT_TRACE_USE_PROCTIME",
    "EVENT_TRACE_USE_NOCPUTIME",
    "TRACE_HEADER_FLAG_USE_TIMESTAMP",
    "TRACE_HEADER_FLAG_TRACED_GUID",
    "TRACE_HEADER_FLAG_LOG_WNODE",
    "TRACE_HEADER_FLAG_USE_GUID_PTR",
    "TRACE_HEADER_FLAG_USE_MOF_PTR",
    "SYSTEM_ALPC_KW_GENERAL",
    "SYSTEM_CONFIG_KW_SYSTEM",
    "SYSTEM_CONFIG_KW_GRAPHICS",
    "SYSTEM_CONFIG_KW_STORAGE",
    "SYSTEM_CONFIG_KW_NETWORK",
    "SYSTEM_CONFIG_KW_SERVICES",
    "SYSTEM_CONFIG_KW_PNP",
    "SYSTEM_CONFIG_KW_OPTICAL",
    "SYSTEM_CPU_KW_CONFIG",
    "SYSTEM_CPU_KW_CACHE_FLUSH",
    "SYSTEM_CPU_KW_SPEC_CONTROL",
    "SYSTEM_HYPERVISOR_KW_PROFILE",
    "SYSTEM_HYPERVISOR_KW_CALLOUTS",
    "SYSTEM_HYPERVISOR_KW_VTL_CHANGE",
    "SYSTEM_INTERRUPT_KW_GENERAL",
    "SYSTEM_INTERRUPT_KW_CLOCK_INTERRUPT",
    "SYSTEM_INTERRUPT_KW_DPC",
    "SYSTEM_INTERRUPT_KW_DPC_QUEUE",
    "SYSTEM_INTERRUPT_KW_WDF_DPC",
    "SYSTEM_INTERRUPT_KW_WDF_INTERRUPT",
    "SYSTEM_INTERRUPT_KW_IPI",
    "SYSTEM_IO_KW_DISK",
    "SYSTEM_IO_KW_DISK_INIT",
    "SYSTEM_IO_KW_FILENAME",
    "SYSTEM_IO_KW_SPLIT",
    "SYSTEM_IO_KW_FILE",
    "SYSTEM_IO_KW_OPTICAL",
    "SYSTEM_IO_KW_OPTICAL_INIT",
    "SYSTEM_IO_KW_DRIVERS",
    "SYSTEM_IO_KW_CC",
    "SYSTEM_IO_KW_NETWORK",
    "SYSTEM_IOFILTER_KW_GENERAL",
    "SYSTEM_IOFILTER_KW_INIT",
    "SYSTEM_IOFILTER_KW_FASTIO",
    "SYSTEM_IOFILTER_KW_FAILURE",
    "SYSTEM_LOCK_KW_SPINLOCK",
    "SYSTEM_LOCK_KW_SPINLOCK_COUNTERS",
    "SYSTEM_LOCK_KW_SYNC_OBJECTS",
    "SYSTEM_MEMORY_KW_GENERAL",
    "SYSTEM_MEMORY_KW_HARD_FAULTS",
    "SYSTEM_MEMORY_KW_ALL_FAULTS",
    "SYSTEM_MEMORY_KW_POOL",
    "SYSTEM_MEMORY_KW_MEMINFO",
    "SYSTEM_MEMORY_KW_PFSECTION",
    "SYSTEM_MEMORY_KW_MEMINFO_WS",
    "SYSTEM_MEMORY_KW_HEAP",
    "SYSTEM_MEMORY_KW_WS",
    "SYSTEM_MEMORY_KW_CONTMEM_GEN",
    "SYSTEM_MEMORY_KW_VIRTUAL_ALLOC",
    "SYSTEM_MEMORY_KW_FOOTPRINT",
    "SYSTEM_MEMORY_KW_SESSION",
    "SYSTEM_MEMORY_KW_REFSET",
    "SYSTEM_MEMORY_KW_VAMAP",
    "SYSTEM_MEMORY_KW_NONTRADEABLE",
    "SYSTEM_OBJECT_KW_GENERAL",
    "SYSTEM_OBJECT_KW_HANDLE",
    "SYSTEM_POWER_KW_GENERAL",
    "SYSTEM_POWER_KW_HIBER_RUNDOWN",
    "SYSTEM_POWER_KW_PROCESSOR_IDLE",
    "SYSTEM_POWER_KW_IDLE_SELECTION",
    "SYSTEM_POWER_KW_PPM_EXIT_LATENCY",
    "SYSTEM_PROCESS_KW_GENERAL",
    "SYSTEM_PROCESS_KW_INSWAP",
    "SYSTEM_PROCESS_KW_FREEZE",
    "SYSTEM_PROCESS_KW_PERF_COUNTER",
    "SYSTEM_PROCESS_KW_WAKE_COUNTER",
    "SYSTEM_PROCESS_KW_WAKE_DROP",
    "SYSTEM_PROCESS_KW_WAKE_EVENT",
    "SYSTEM_PROCESS_KW_DEBUG_EVENTS",
    "SYSTEM_PROCESS_KW_DBGPRINT",
    "SYSTEM_PROCESS_KW_JOB",
    "SYSTEM_PROCESS_KW_WORKER_THREAD",
    "SYSTEM_PROCESS_KW_THREAD",
    "SYSTEM_PROCESS_KW_LOADER",
    "SYSTEM_PROFILE_KW_GENERAL",
    "SYSTEM_PROFILE_KW_PMC_PROFILE",
    "SYSTEM_REGISTRY_KW_GENERAL",
    "SYSTEM_REGISTRY_KW_HIVE",
    "SYSTEM_REGISTRY_KW_NOTIFICATION",
    "SYSTEM_SCHEDULER_KW_XSCHEDULER",
    "SYSTEM_SCHEDULER_KW_DISPATCHER",
    "SYSTEM_SCHEDULER_KW_KERNEL_QUEUE",
    "SYSTEM_SCHEDULER_KW_SHOULD_YIELD",
    "SYSTEM_SCHEDULER_KW_ANTI_STARVATION",
    "SYSTEM_SCHEDULER_KW_LOAD_BALANCER",
    "SYSTEM_SCHEDULER_KW_AFFINITY",
    "SYSTEM_SCHEDULER_KW_PRIORITY",
    "SYSTEM_SCHEDULER_KW_IDEAL_PROCESSOR",
    "SYSTEM_SCHEDULER_KW_CONTEXT_SWITCH",
    "SYSTEM_SCHEDULER_KW_COMPACT_CSWITCH",
    "SYSTEM_SYSCALL_KW_GENERAL",
    "SYSTEM_TIMER_KW_GENERAL",
    "SYSTEM_TIMER_KW_CLOCK_TIMER",
    "SYSTEM_MEMORY_POOL_FILTER_ID",
    "ETW_NULL_TYPE_VALUE",
    "ETW_OBJECT_TYPE_VALUE",
    "ETW_STRING_TYPE_VALUE",
    "ETW_SBYTE_TYPE_VALUE",
    "ETW_BYTE_TYPE_VALUE",
    "ETW_INT16_TYPE_VALUE",
    "ETW_UINT16_TYPE_VALUE",
    "ETW_INT32_TYPE_VALUE",
    "ETW_UINT32_TYPE_VALUE",
    "ETW_INT64_TYPE_VALUE",
    "ETW_UINT64_TYPE_VALUE",
    "ETW_CHAR_TYPE_VALUE",
    "ETW_SINGLE_TYPE_VALUE",
    "ETW_DOUBLE_TYPE_VALUE",
    "ETW_BOOLEAN_TYPE_VALUE",
    "ETW_DECIMAL_TYPE_VALUE",
    "ETW_GUID_TYPE_VALUE",
    "ETW_ASCIICHAR_TYPE_VALUE",
    "ETW_ASCIISTRING_TYPE_VALUE",
    "ETW_COUNTED_STRING_TYPE_VALUE",
    "ETW_POINTER_TYPE_VALUE",
    "ETW_SIZET_TYPE_VALUE",
    "ETW_HIDDEN_TYPE_VALUE",
    "ETW_BOOL_TYPE_VALUE",
    "ETW_COUNTED_ANSISTRING_TYPE_VALUE",
    "ETW_REVERSED_COUNTED_STRING_TYPE_VALUE",
    "ETW_REVERSED_COUNTED_ANSISTRING_TYPE_VALUE",
    "ETW_NON_NULL_TERMINATED_STRING_TYPE_VALUE",
    "ETW_REDUCED_ANSISTRING_TYPE_VALUE",
    "ETW_REDUCED_STRING_TYPE_VALUE",
    "ETW_SID_TYPE_VALUE",
    "ETW_VARIANT_TYPE_VALUE",
    "ETW_PTVECTOR_TYPE_VALUE",
    "ETW_WMITIME_TYPE_VALUE",
    "ETW_DATETIME_TYPE_VALUE",
    "ETW_REFRENCE_TYPE_VALUE",
    "TRACE_PROVIDER_FLAG_LEGACY",
    "TRACE_PROVIDER_FLAG_PRE_ENABLE",
    "ENABLE_TRACE_PARAMETERS_VERSION",
    "ENABLE_TRACE_PARAMETERS_VERSION_2",
    "EVENT_MIN_LEVEL",
    "EVENT_MAX_LEVEL",
    "EVENT_ACTIVITY_CTRL_GET_ID",
    "EVENT_ACTIVITY_CTRL_SET_ID",
    "EVENT_ACTIVITY_CTRL_CREATE_ID",
    "EVENT_ACTIVITY_CTRL_GET_SET_ID",
    "EVENT_ACTIVITY_CTRL_CREATE_SET_ID",
    "MAX_EVENT_DATA_DESCRIPTORS",
    "MAX_EVENT_FILTER_DATA_SIZE",
    "MAX_EVENT_FILTER_PAYLOAD_SIZE",
    "MAX_EVENT_FILTER_EVENT_NAME_SIZE",
    "MAX_EVENT_FILTERS_COUNT",
    "MAX_EVENT_FILTER_PID_COUNT",
    "MAX_EVENT_FILTER_EVENT_ID_COUNT",
    "EVENT_FILTER_TYPE_NONE",
    "EVENT_FILTER_TYPE_SCHEMATIZED",
    "EVENT_FILTER_TYPE_SYSTEM_FLAGS",
    "EVENT_FILTER_TYPE_TRACEHANDLE",
    "EVENT_FILTER_TYPE_PID",
    "EVENT_FILTER_TYPE_EXECUTABLE_NAME",
    "EVENT_FILTER_TYPE_PACKAGE_ID",
    "EVENT_FILTER_TYPE_PACKAGE_APP_ID",
    "EVENT_FILTER_TYPE_PAYLOAD",
    "EVENT_FILTER_TYPE_EVENT_ID",
    "EVENT_FILTER_TYPE_EVENT_NAME",
    "EVENT_FILTER_TYPE_STACKWALK",
    "EVENT_FILTER_TYPE_STACKWALK_NAME",
    "EVENT_FILTER_TYPE_STACKWALK_LEVEL_KW",
    "EVENT_FILTER_TYPE_CONTAINER",
    "EVENT_DATA_DESCRIPTOR_TYPE_NONE",
    "EVENT_DATA_DESCRIPTOR_TYPE_EVENT_METADATA",
    "EVENT_DATA_DESCRIPTOR_TYPE_PROVIDER_METADATA",
    "EVENT_DATA_DESCRIPTOR_TYPE_TIMESTAMP_OVERRIDE",
    "EVENT_WRITE_FLAG_NO_FAULTING",
    "EVENT_WRITE_FLAG_INPRIVATE",
    "EVENT_HEADER_EXT_TYPE_RELATED_ACTIVITYID",
    "EVENT_HEADER_EXT_TYPE_SID",
    "EVENT_HEADER_EXT_TYPE_TS_ID",
    "EVENT_HEADER_EXT_TYPE_INSTANCE_INFO",
    "EVENT_HEADER_EXT_TYPE_STACK_TRACE32",
    "EVENT_HEADER_EXT_TYPE_STACK_TRACE64",
    "EVENT_HEADER_EXT_TYPE_PEBS_INDEX",
    "EVENT_HEADER_EXT_TYPE_PMC_COUNTERS",
    "EVENT_HEADER_EXT_TYPE_PSM_KEY",
    "EVENT_HEADER_EXT_TYPE_EVENT_KEY",
    "EVENT_HEADER_EXT_TYPE_EVENT_SCHEMA_TL",
    "EVENT_HEADER_EXT_TYPE_PROV_TRAITS",
    "EVENT_HEADER_EXT_TYPE_PROCESS_START_KEY",
    "EVENT_HEADER_EXT_TYPE_CONTROL_GUID",
    "EVENT_HEADER_EXT_TYPE_QPC_DELTA",
    "EVENT_HEADER_EXT_TYPE_CONTAINER_ID",
    "EVENT_HEADER_EXT_TYPE_STACK_KEY32",
    "EVENT_HEADER_EXT_TYPE_STACK_KEY64",
    "EVENT_HEADER_EXT_TYPE_MAX",
    "EVENT_HEADER_PROPERTY_XML",
    "EVENT_HEADER_PROPERTY_FORWARDED_XML",
    "EVENT_HEADER_PROPERTY_LEGACY_EVENTLOG",
    "EVENT_HEADER_PROPERTY_RELOGGABLE",
    "EVENT_HEADER_FLAG_EXTENDED_INFO",
    "EVENT_HEADER_FLAG_PRIVATE_SESSION",
    "EVENT_HEADER_FLAG_STRING_ONLY",
    "EVENT_HEADER_FLAG_TRACE_MESSAGE",
    "EVENT_HEADER_FLAG_NO_CPUTIME",
    "EVENT_HEADER_FLAG_32_BIT_HEADER",
    "EVENT_HEADER_FLAG_64_BIT_HEADER",
    "EVENT_HEADER_FLAG_DECODE_GUID",
    "EVENT_HEADER_FLAG_CLASSIC_HEADER",
    "EVENT_HEADER_FLAG_PROCESSOR_INDEX",
    "EVENT_ENABLE_PROPERTY_SID",
    "EVENT_ENABLE_PROPERTY_TS_ID",
    "EVENT_ENABLE_PROPERTY_STACK_TRACE",
    "EVENT_ENABLE_PROPERTY_PSM_KEY",
    "EVENT_ENABLE_PROPERTY_IGNORE_KEYWORD_0",
    "EVENT_ENABLE_PROPERTY_PROVIDER_GROUP",
    "EVENT_ENABLE_PROPERTY_ENABLE_KEYWORD_0",
    "EVENT_ENABLE_PROPERTY_PROCESS_START_KEY",
    "EVENT_ENABLE_PROPERTY_EVENT_KEY",
    "EVENT_ENABLE_PROPERTY_EXCLUDE_INPRIVATE",
    "EVENT_ENABLE_PROPERTY_ENABLE_SILOS",
    "EVENT_ENABLE_PROPERTY_SOURCE_CONTAINER_TRACKING",
    "PROCESS_TRACE_MODE_REAL_TIME",
    "PROCESS_TRACE_MODE_RAW_TIMESTAMP",
    "PROCESS_TRACE_MODE_EVENT_RECORD",
    "CLSID_TraceRelogger",
    "TRACE_MESSAGE_FLAGS",
    "TRACE_MESSAGE_COMPONENTID",
    "TRACE_MESSAGE_GUID",
    "TRACE_MESSAGE_SEQUENCE",
    "TRACE_MESSAGE_SYSTEMINFO",
    "TRACE_MESSAGE_TIMESTAMP",
    "ENABLECALLBACK_ENABLED_STATE",
    "EVENT_CONTROL_CODE_DISABLE_PROVIDER",
    "EVENT_CONTROL_CODE_ENABLE_PROVIDER",
    "EVENT_CONTROL_CODE_CAPTURE_STATE",
    "EVENT_TRACE_CONTROL",
    "EVENT_TRACE_CONTROL_FLUSH",
    "EVENT_TRACE_CONTROL_QUERY",
    "EVENT_TRACE_CONTROL_STOP",
    "EVENT_TRACE_CONTROL_UPDATE",
    "EVENT_TRACE_FLAG",
    "EVENT_TRACE_FLAG_ALPC",
    "EVENT_TRACE_FLAG_CSWITCH",
    "EVENT_TRACE_FLAG_DBGPRINT",
    "EVENT_TRACE_FLAG_DISK_FILE_IO",
    "EVENT_TRACE_FLAG_DISK_IO",
    "EVENT_TRACE_FLAG_DISK_IO_INIT",
    "EVENT_TRACE_FLAG_DISPATCHER",
    "EVENT_TRACE_FLAG_DPC",
    "EVENT_TRACE_FLAG_DRIVER",
    "EVENT_TRACE_FLAG_FILE_IO",
    "EVENT_TRACE_FLAG_FILE_IO_INIT",
    "EVENT_TRACE_FLAG_IMAGE_LOAD",
    "EVENT_TRACE_FLAG_INTERRUPT",
    "EVENT_TRACE_FLAG_JOB",
    "EVENT_TRACE_FLAG_MEMORY_HARD_FAULTS",
    "EVENT_TRACE_FLAG_MEMORY_PAGE_FAULTS",
    "EVENT_TRACE_FLAG_NETWORK_TCPIP",
    "EVENT_TRACE_FLAG_NO_SYSCONFIG",
    "EVENT_TRACE_FLAG_PROCESS",
    "EVENT_TRACE_FLAG_PROCESS_COUNTERS",
    "EVENT_TRACE_FLAG_PROFILE",
    "EVENT_TRACE_FLAG_REGISTRY",
    "EVENT_TRACE_FLAG_SPLIT_IO",
    "EVENT_TRACE_FLAG_SYSTEMCALL",
    "EVENT_TRACE_FLAG_THREAD",
    "EVENT_TRACE_FLAG_VAMAP",
    "EVENT_TRACE_FLAG_VIRTUAL_ALLOC",
    "TDH_HANDLE",
    "WNODE_HEADER",
    "OFFSETINSTANCEDATAANDLENGTH",
    "WNODE_ALL_DATA",
    "WNODE_SINGLE_INSTANCE",
    "WNODE_SINGLE_ITEM",
    "WNODE_METHOD_ITEM",
    "WNODE_EVENT_ITEM",
    "WNODE_EVENT_REFERENCE",
    "WNODE_TOO_SMALL",
    "WMIREGGUIDW",
    "WMIREGINFOW",
    "WMIDPREQUESTCODE",
    "WMI_GET_ALL_DATA",
    "WMI_GET_SINGLE_INSTANCE",
    "WMI_SET_SINGLE_INSTANCE",
    "WMI_SET_SINGLE_ITEM",
    "WMI_ENABLE_EVENTS",
    "WMI_DISABLE_EVENTS",
    "WMI_ENABLE_COLLECTION",
    "WMI_DISABLE_COLLECTION",
    "WMI_REGINFO",
    "WMI_EXECUTE_METHOD",
    "WMI_CAPTURE_STATE",
    "ETW_COMPRESSION_RESUMPTION_MODE",
    "ETW_COMPRESSION_RESUMPTION_MODE_EtwCompressionModeRestart",
    "ETW_COMPRESSION_RESUMPTION_MODE_EtwCompressionModeNoDisable",
    "ETW_COMPRESSION_RESUMPTION_MODE_EtwCompressionModeNoRestart",
    "EVENT_TRACE_HEADER",
    "EVENT_INSTANCE_HEADER",
    "MOF_FIELD",
    "TRACE_LOGFILE_HEADER",
    "TRACE_LOGFILE_HEADER32",
    "TRACE_LOGFILE_HEADER64",
    "EVENT_INSTANCE_INFO",
    "EVENT_TRACE_PROPERTIES",
    "EVENT_TRACE_PROPERTIES_V2",
    "TRACE_GUID_REGISTRATION",
    "TRACE_GUID_PROPERTIES",
    "ETW_BUFFER_CONTEXT",
    "TRACE_ENABLE_INFO",
    "TRACE_PROVIDER_INSTANCE_INFO",
    "TRACE_GUID_INFO",
    "PROFILE_SOURCE_INFO",
    "ETW_PMC_COUNTER_OWNER_TYPE",
    "ETW_PMC_COUNTER_OWNER_TYPE_EtwPmcOwnerFree",
    "ETW_PMC_COUNTER_OWNER_TYPE_EtwPmcOwnerUntagged",
    "ETW_PMC_COUNTER_OWNER_TYPE_EtwPmcOwnerTagged",
    "ETW_PMC_COUNTER_OWNER_TYPE_EtwPmcOwnerTaggedWithSource",
    "ETW_PMC_COUNTER_OWNER",
    "ETW_PMC_COUNTER_OWNERSHIP_STATUS",
    "EVENT_TRACE",
    "PEVENT_TRACE_BUFFER_CALLBACKW",
    "PEVENT_TRACE_BUFFER_CALLBACKA",
    "PEVENT_CALLBACK",
    "PEVENT_RECORD_CALLBACK",
    "WMIDPREQUEST",
    "EVENT_TRACE_LOGFILEW",
    "EVENT_TRACE_LOGFILEA",
    "ENABLE_TRACE_PARAMETERS_V1",
    "ENABLE_TRACE_PARAMETERS",
    "TRACE_QUERY_INFO_CLASS",
    "TRACE_QUERY_INFO_CLASS_TraceGuidQueryList",
    "TRACE_QUERY_INFO_CLASS_TraceGuidQueryInfo",
    "TRACE_QUERY_INFO_CLASS_TraceGuidQueryProcess",
    "TRACE_QUERY_INFO_CLASS_TraceStackTracingInfo",
    "TRACE_QUERY_INFO_CLASS_TraceSystemTraceEnableFlagsInfo",
    "TRACE_QUERY_INFO_CLASS_TraceSampledProfileIntervalInfo",
    "TRACE_QUERY_INFO_CLASS_TraceProfileSourceConfigInfo",
    "TRACE_QUERY_INFO_CLASS_TraceProfileSourceListInfo",
    "TRACE_QUERY_INFO_CLASS_TracePmcEventListInfo",
    "TRACE_QUERY_INFO_CLASS_TracePmcCounterListInfo",
    "TRACE_QUERY_INFO_CLASS_TraceSetDisallowList",
    "TRACE_QUERY_INFO_CLASS_TraceVersionInfo",
    "TRACE_QUERY_INFO_CLASS_TraceGroupQueryList",
    "TRACE_QUERY_INFO_CLASS_TraceGroupQueryInfo",
    "TRACE_QUERY_INFO_CLASS_TraceDisallowListQuery",
    "TRACE_QUERY_INFO_CLASS_TraceInfoReserved15",
    "TRACE_QUERY_INFO_CLASS_TracePeriodicCaptureStateListInfo",
    "TRACE_QUERY_INFO_CLASS_TracePeriodicCaptureStateInfo",
    "TRACE_QUERY_INFO_CLASS_TraceProviderBinaryTracking",
    "TRACE_QUERY_INFO_CLASS_TraceMaxLoggersQuery",
    "TRACE_QUERY_INFO_CLASS_TraceLbrConfigurationInfo",
    "TRACE_QUERY_INFO_CLASS_TraceLbrEventListInfo",
    "TRACE_QUERY_INFO_CLASS_TraceMaxPmcCounterQuery",
    "TRACE_QUERY_INFO_CLASS_TraceStreamCount",
    "TRACE_QUERY_INFO_CLASS_TraceStackCachingInfo",
    "TRACE_QUERY_INFO_CLASS_TracePmcCounterOwners",
    "TRACE_QUERY_INFO_CLASS_TraceUnifiedStackCachingInfo",
    "TRACE_QUERY_INFO_CLASS_MaxTraceSetInfoClass",
    "CLASSIC_EVENT_ID",
    "TRACE_STACK_CACHING_INFO",
    "TRACE_PROFILE_INTERVAL",
    "TRACE_VERSION_INFO",
    "TRACE_PERIODIC_CAPTURE_STATE_INFO",
    "ETW_PROCESS_HANDLE_INFO_TYPE",
    "ETW_PROCESS_HANDLE_INFO_TYPE_EtwQueryPartitionInformation",
    "ETW_PROCESS_HANDLE_INFO_TYPE_EtwQueryPartitionInformationV2",
    "ETW_PROCESS_HANDLE_INFO_TYPE_EtwQueryLastDroppedTimes",
    "ETW_PROCESS_HANDLE_INFO_TYPE_EtwQueryProcessHandleInfoMax",
    "ETW_TRACE_PARTITION_INFORMATION",
    "ETW_TRACE_PARTITION_INFORMATION_V2",
    "EVENT_DATA_DESCRIPTOR",
    "EVENT_DESCRIPTOR",
    "EVENT_FILTER_DESCRIPTOR",
    "EVENT_FILTER_HEADER",
    "EVENT_FILTER_EVENT_ID",
    "EVENT_FILTER_EVENT_NAME",
    "EVENT_FILTER_LEVEL_KW",
    "EVENT_INFO_CLASS",
    "EVENT_INFO_CLASS_EventProviderBinaryTrackInfo",
    "EVENT_INFO_CLASS_EventProviderSetReserved1",
    "EVENT_INFO_CLASS_EventProviderSetTraits",
    "EVENT_INFO_CLASS_EventProviderUseDescriptorType",
    "EVENT_INFO_CLASS_MaxEventInfo",
    "PENABLECALLBACK",
    "EVENT_HEADER_EXTENDED_DATA_ITEM",
    "EVENT_EXTENDED_ITEM_INSTANCE",
    "EVENT_EXTENDED_ITEM_RELATED_ACTIVITYID",
    "EVENT_EXTENDED_ITEM_TS_ID",
    "EVENT_EXTENDED_ITEM_STACK_TRACE32",
    "EVENT_EXTENDED_ITEM_STACK_TRACE64",
    "EVENT_EXTENDED_ITEM_STACK_KEY32",
    "EVENT_EXTENDED_ITEM_STACK_KEY64",
    "EVENT_EXTENDED_ITEM_PEBS_INDEX",
    "EVENT_EXTENDED_ITEM_PMC_COUNTERS",
    "EVENT_EXTENDED_ITEM_PROCESS_START_KEY",
    "EVENT_EXTENDED_ITEM_EVENT_KEY",
    "EVENT_HEADER",
    "EVENT_RECORD",
    "ETW_PROVIDER_TRAIT_TYPE",
    "ETW_PROVIDER_TRAIT_TYPE_EtwProviderTraitTypeGroup",
    "ETW_PROVIDER_TRAIT_TYPE_EtwProviderTraitDecodeGuid",
    "ETW_PROVIDER_TRAIT_TYPE_EtwProviderTraitTypeMax",
    "EVENTSECURITYOPERATION",
    "EVENTSECURITYOPERATION_EventSecuritySetDACL",
    "EVENTSECURITYOPERATION_EventSecuritySetSACL",
    "EVENTSECURITYOPERATION_EventSecurityAddDACL",
    "EVENTSECURITYOPERATION_EventSecurityAddSACL",
    "EVENTSECURITYOPERATION_EventSecurityMax",
    "EVENT_MAP_ENTRY",
    "MAP_FLAGS",
    "EVENTMAP_INFO_FLAG_MANIFEST_VALUEMAP",
    "EVENTMAP_INFO_FLAG_MANIFEST_BITMAP",
    "EVENTMAP_INFO_FLAG_MANIFEST_PATTERNMAP",
    "EVENTMAP_INFO_FLAG_WBEM_VALUEMAP",
    "EVENTMAP_INFO_FLAG_WBEM_BITMAP",
    "EVENTMAP_INFO_FLAG_WBEM_FLAG",
    "EVENTMAP_INFO_FLAG_WBEM_NO_MAP",
    "MAP_VALUETYPE",
    "EVENTMAP_ENTRY_VALUETYPE_ULONG",
    "EVENTMAP_ENTRY_VALUETYPE_STRING",
    "EVENT_MAP_INFO",
    "_TDH_IN_TYPE",
    "TDH_INTYPE_NULL",
    "TDH_INTYPE_UNICODESTRING",
    "TDH_INTYPE_ANSISTRING",
    "TDH_INTYPE_INT8",
    "TDH_INTYPE_UINT8",
    "TDH_INTYPE_INT16",
    "TDH_INTYPE_UINT16",
    "TDH_INTYPE_INT32",
    "TDH_INTYPE_UINT32",
    "TDH_INTYPE_INT64",
    "TDH_INTYPE_UINT64",
    "TDH_INTYPE_FLOAT",
    "TDH_INTYPE_DOUBLE",
    "TDH_INTYPE_BOOLEAN",
    "TDH_INTYPE_BINARY",
    "TDH_INTYPE_GUID",
    "TDH_INTYPE_POINTER",
    "TDH_INTYPE_FILETIME",
    "TDH_INTYPE_SYSTEMTIME",
    "TDH_INTYPE_SID",
    "TDH_INTYPE_HEXINT32",
    "TDH_INTYPE_HEXINT64",
    "TDH_INTYPE_MANIFEST_COUNTEDSTRING",
    "TDH_INTYPE_MANIFEST_COUNTEDANSISTRING",
    "TDH_INTYPE_RESERVED24",
    "TDH_INTYPE_MANIFEST_COUNTEDBINARY",
    "TDH_INTYPE_COUNTEDSTRING",
    "TDH_INTYPE_COUNTEDANSISTRING",
    "TDH_INTYPE_REVERSEDCOUNTEDSTRING",
    "TDH_INTYPE_REVERSEDCOUNTEDANSISTRING",
    "TDH_INTYPE_NONNULLTERMINATEDSTRING",
    "TDH_INTYPE_NONNULLTERMINATEDANSISTRING",
    "TDH_INTYPE_UNICODECHAR",
    "TDH_INTYPE_ANSICHAR",
    "TDH_INTYPE_SIZET",
    "TDH_INTYPE_HEXDUMP",
    "TDH_INTYPE_WBEMSID",
    "_TDH_OUT_TYPE",
    "TDH_OUTTYPE_NULL",
    "TDH_OUTTYPE_STRING",
    "TDH_OUTTYPE_DATETIME",
    "TDH_OUTTYPE_BYTE",
    "TDH_OUTTYPE_UNSIGNEDBYTE",
    "TDH_OUTTYPE_SHORT",
    "TDH_OUTTYPE_UNSIGNEDSHORT",
    "TDH_OUTTYPE_INT",
    "TDH_OUTTYPE_UNSIGNEDINT",
    "TDH_OUTTYPE_LONG",
    "TDH_OUTTYPE_UNSIGNEDLONG",
    "TDH_OUTTYPE_FLOAT",
    "TDH_OUTTYPE_DOUBLE",
    "TDH_OUTTYPE_BOOLEAN",
    "TDH_OUTTYPE_GUID",
    "TDH_OUTTYPE_HEXBINARY",
    "TDH_OUTTYPE_HEXINT8",
    "TDH_OUTTYPE_HEXINT16",
    "TDH_OUTTYPE_HEXINT32",
    "TDH_OUTTYPE_HEXINT64",
    "TDH_OUTTYPE_PID",
    "TDH_OUTTYPE_TID",
    "TDH_OUTTYPE_PORT",
    "TDH_OUTTYPE_IPV4",
    "TDH_OUTTYPE_IPV6",
    "TDH_OUTTYPE_SOCKETADDRESS",
    "TDH_OUTTYPE_CIMDATETIME",
    "TDH_OUTTYPE_ETWTIME",
    "TDH_OUTTYPE_XML",
    "TDH_OUTTYPE_ERRORCODE",
    "TDH_OUTTYPE_WIN32ERROR",
    "TDH_OUTTYPE_NTSTATUS",
    "TDH_OUTTYPE_HRESULT",
    "TDH_OUTTYPE_CULTURE_INSENSITIVE_DATETIME",
    "TDH_OUTTYPE_JSON",
    "TDH_OUTTYPE_UTF8",
    "TDH_OUTTYPE_PKCS7_WITH_TYPE_INFO",
    "TDH_OUTTYPE_CODE_POINTER",
    "TDH_OUTTYPE_DATETIME_UTC",
    "TDH_OUTTYPE_REDUCEDSTRING",
    "TDH_OUTTYPE_NOPRINT",
    "PROPERTY_FLAGS",
    "PROPERTY_FLAGS_PropertyStruct",
    "PROPERTY_FLAGS_PropertyParamLength",
    "PROPERTY_FLAGS_PropertyParamCount",
    "PROPERTY_FLAGS_PropertyWBEMXmlFragment",
    "PROPERTY_FLAGS_PropertyParamFixedLength",
    "PROPERTY_FLAGS_PropertyParamFixedCount",
    "PROPERTY_FLAGS_PropertyHasTags",
    "PROPERTY_FLAGS_PropertyHasCustomSchema",
    "EVENT_PROPERTY_INFO",
    "DECODING_SOURCE",
    "DECODING_SOURCE_DecodingSourceXMLFile",
    "DECODING_SOURCE_DecodingSourceWbem",
    "DECODING_SOURCE_DecodingSourceWPP",
    "DECODING_SOURCE_DecodingSourceTlg",
    "DECODING_SOURCE_DecodingSourceMax",
    "TEMPLATE_FLAGS",
    "TEMPLATE_EVENT_DATA",
    "TEMPLATE_USER_DATA",
    "TEMPLATE_CONTROL_GUID",
    "TRACE_EVENT_INFO",
    "PROPERTY_DATA_DESCRIPTOR",
    "PAYLOAD_OPERATOR",
    "PAYLOADFIELD_EQ",
    "PAYLOADFIELD_NE",
    "PAYLOADFIELD_LE",
    "PAYLOADFIELD_GT",
    "PAYLOADFIELD_LT",
    "PAYLOADFIELD_GE",
    "PAYLOADFIELD_BETWEEN",
    "PAYLOADFIELD_NOTBETWEEN",
    "PAYLOADFIELD_MODULO",
    "PAYLOADFIELD_CONTAINS",
    "PAYLOADFIELD_DOESNTCONTAIN",
    "PAYLOADFIELD_IS",
    "PAYLOADFIELD_ISNOT",
    "PAYLOADFIELD_INVALID",
    "PAYLOAD_FILTER_PREDICATE",
    "PROVIDER_FILTER_INFO",
    "EVENT_FIELD_TYPE",
    "EVENT_FIELD_TYPE_EventKeywordInformation",
    "EVENT_FIELD_TYPE_EventLevelInformation",
    "EVENT_FIELD_TYPE_EventChannelInformation",
    "EVENT_FIELD_TYPE_EventTaskInformation",
    "EVENT_FIELD_TYPE_EventOpcodeInformation",
    "EVENT_FIELD_TYPE_EventInformationMax",
    "PROVIDER_FIELD_INFO",
    "PROVIDER_FIELD_INFOARRAY",
    "TRACE_PROVIDER_INFO",
    "PROVIDER_ENUMERATION_INFO",
    "PROVIDER_EVENT_INFO",
    "TDH_CONTEXT_TYPE",
    "TDH_CONTEXT_WPP_TMFFILE",
    "TDH_CONTEXT_WPP_TMFSEARCHPATH",
    "TDH_CONTEXT_WPP_GMT",
    "TDH_CONTEXT_POINTERSIZE",
    "TDH_CONTEXT_PDB_PATH",
    "TDH_CONTEXT_MAXIMUM",
    "TDH_CONTEXT",
    "CTraceRelogger",
    "ITraceEvent",
    "ITraceEventCallback",
    "ITraceRelogger",
    "StartTraceW",
    "StartTrace",
    "StartTraceA",
    "StopTraceW",
    "StopTrace",
    "StopTraceA",
    "QueryTraceW",
    "QueryTrace",
    "QueryTraceA",
    "UpdateTraceW",
    "UpdateTrace",
    "UpdateTraceA",
    "FlushTraceW",
    "FlushTrace",
    "FlushTraceA",
    "ControlTraceW",
    "ControlTrace",
    "ControlTraceA",
    "QueryAllTracesW",
    "QueryAllTraces",
    "QueryAllTracesA",
    "EnableTrace",
    "EnableTraceEx",
    "EnableTraceEx2",
    "EnumerateTraceGuidsEx",
    "TraceSetInformation",
    "TraceQueryInformation",
    "CreateTraceInstanceId",
    "TraceEvent",
    "TraceEventInstance",
    "RegisterTraceGuidsW",
    "RegisterTraceGuids",
    "RegisterTraceGuidsA",
    "EnumerateTraceGuids",
    "UnregisterTraceGuids",
    "GetTraceLoggerHandle",
    "GetTraceEnableLevel",
    "GetTraceEnableFlags",
    "OpenTraceW",
    "OpenTrace",
    "ProcessTrace",
    "CloseTrace",
    "QueryTraceProcessingHandle",
    "OpenTraceA",
    "SetTraceCallback",
    "RemoveTraceCallback",
    "TraceMessage",
    "TraceMessageVa",
    "EventRegister",
    "EventUnregister",
    "EventSetInformation",
    "EventEnabled",
    "EventProviderEnabled",
    "EventWrite",
    "EventWriteTransfer",
    "EventWriteEx",
    "EventWriteString",
    "EventActivityIdControl",
    "EventAccessControl",
    "EventAccessQuery",
    "EventAccessRemove",
    "TdhCreatePayloadFilter",
    "TdhDeletePayloadFilter",
    "TdhAggregatePayloadFilters",
    "TdhCleanupPayloadEventFilterDescriptor",
    "TdhGetEventInformation",
    "TdhGetEventMapInformation",
    "TdhGetPropertySize",
    "TdhGetProperty",
    "TdhEnumerateProviders",
    "TdhEnumerateProvidersForDecodingSource",
    "TdhQueryProviderFieldInformation",
    "TdhEnumerateProviderFieldInformation",
    "TdhEnumerateProviderFilters",
    "TdhLoadManifest",
    "TdhLoadManifestFromMemory",
    "TdhUnloadManifest",
    "TdhUnloadManifestFromMemory",
    "TdhFormatProperty",
    "TdhOpenDecodingHandle",
    "TdhSetDecodingParameter",
    "TdhGetDecodingParameter",
    "TdhGetWppProperty",
    "TdhGetWppMessage",
    "TdhCloseDecodingHandle",
    "TdhLoadManifestFromBinary",
    "TdhEnumerateManifestProviderEvents",
    "TdhGetManifestEventInformation",
    "CveEventWrite",
]
