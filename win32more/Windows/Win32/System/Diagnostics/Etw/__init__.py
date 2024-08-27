from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Security
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Diagnostics.Etw
import win32more.Windows.Win32.System.Time
ALPCGuid: Guid = Guid('{45d8cccd-539f-4b72-a8b7-5c683142609a}')
DiskIoGuid: Guid = Guid('{3d6fa8d4-fe05-11d0-9dda-00c04fd7ba7c}')
EventTraceConfigGuid: Guid = Guid('{01853a65-418f-4f36-aefc-dc0f1d2fd235}')
FileIoGuid: Guid = Guid('{90cbdc39-4a3e-11d1-84f4-0000f80464e3}')
ImageLoadGuid: Guid = Guid('{2cb15d1d-5fc1-11d2-abe1-00a0c911f518}')
PageFaultGuid: Guid = Guid('{3d6fa8d3-fe05-11d0-9dda-00c04fd7ba7c}')
PerfInfoGuid: Guid = Guid('{ce1dbfb4-137e-4da6-87b0-3f59aa102cbc}')
ProcessGuid: Guid = Guid('{3d6fa8d0-fe05-11d0-9dda-00c04fd7ba7c}')
RegistryGuid: Guid = Guid('{ae53722e-c863-11d2-8659-00c04fa321a1}')
SplitIoGuid: Guid = Guid('{d837ca92-12b9-44a5-ad6a-3a65b3578aa8}')
TcpIpGuid: Guid = Guid('{9a280ac0-c8e0-11d1-84e2-00c04fb998a2}')
ThreadGuid: Guid = Guid('{3d6fa8d1-fe05-11d0-9dda-00c04fd7ba7c}')
UdpIpGuid: Guid = Guid('{bf3a50c5-a9c9-4988-a005-2df0b7c80f80}')
WNODE_FLAG_ALL_DATA: UInt32 = 1
WNODE_FLAG_SINGLE_INSTANCE: UInt32 = 2
WNODE_FLAG_SINGLE_ITEM: UInt32 = 4
WNODE_FLAG_EVENT_ITEM: UInt32 = 8
WNODE_FLAG_FIXED_INSTANCE_SIZE: UInt32 = 16
WNODE_FLAG_TOO_SMALL: UInt32 = 32
WNODE_FLAG_INSTANCES_SAME: UInt32 = 64
WNODE_FLAG_STATIC_INSTANCE_NAMES: UInt32 = 128
WNODE_FLAG_INTERNAL: UInt32 = 256
WNODE_FLAG_USE_TIMESTAMP: UInt32 = 512
WNODE_FLAG_PERSIST_EVENT: UInt32 = 1024
WNODE_FLAG_EVENT_REFERENCE: UInt32 = 8192
WNODE_FLAG_ANSI_INSTANCENAMES: UInt32 = 16384
WNODE_FLAG_METHOD_ITEM: UInt32 = 32768
WNODE_FLAG_PDO_INSTANCE_NAMES: UInt32 = 65536
WNODE_FLAG_TRACED_GUID: UInt32 = 131072
WNODE_FLAG_LOG_WNODE: UInt32 = 262144
WNODE_FLAG_USE_GUID_PTR: UInt32 = 524288
WNODE_FLAG_USE_MOF_PTR: UInt32 = 1048576
WNODE_FLAG_NO_HEADER: UInt32 = 2097152
WNODE_FLAG_SEND_DATA_BLOCK: UInt32 = 4194304
WNODE_FLAG_VERSIONED_PROPERTIES: UInt32 = 8388608
WNODE_FLAG_SEVERITY_MASK: UInt32 = 4278190080
WMIREG_FLAG_EXPENSIVE: UInt32 = 1
WMIREG_FLAG_INSTANCE_LIST: UInt32 = 4
WMIREG_FLAG_INSTANCE_BASENAME: UInt32 = 8
WMIREG_FLAG_INSTANCE_PDO: UInt32 = 32
WMIREG_FLAG_REMOVE_GUID: UInt32 = 65536
WMIREG_FLAG_RESERVED1: UInt32 = 131072
WMIREG_FLAG_RESERVED2: UInt32 = 262144
WMIREG_FLAG_TRACED_GUID: UInt32 = 524288
WMIREG_FLAG_TRACE_CONTROL_GUID: UInt32 = 4096
WMIREG_FLAG_EVENT_ONLY_GUID: UInt32 = 64
WMI_GUIDTYPE_TRACECONTROL: UInt32 = 0
WMI_GUIDTYPE_TRACE: UInt32 = 1
WMI_GUIDTYPE_DATA: UInt32 = 2
WMI_GUIDTYPE_EVENT: UInt32 = 3
WMIGUID_QUERY: UInt32 = 1
WMIGUID_SET: UInt32 = 2
WMIGUID_NOTIFICATION: UInt32 = 4
WMIGUID_READ_DESCRIPTION: UInt32 = 8
WMIGUID_EXECUTE: UInt32 = 16
TRACELOG_CREATE_REALTIME: UInt32 = 32
TRACELOG_CREATE_ONDISK: UInt32 = 64
TRACELOG_GUID_ENABLE: UInt32 = 128
TRACELOG_ACCESS_KERNEL_LOGGER: UInt32 = 256
TRACELOG_LOG_EVENT: UInt32 = 512
TRACELOG_CREATE_INPROC: UInt32 = 512
TRACELOG_ACCESS_REALTIME: UInt32 = 1024
TRACELOG_REGISTER_GUIDS: UInt32 = 2048
TRACELOG_JOIN_GROUP: UInt32 = 4096
WMI_GLOBAL_LOGGER_ID: UInt32 = 1
MAX_PAYLOAD_PREDICATES: UInt32 = 8
EventTraceGuid: Guid = Guid('{68fdd900-4a3e-11d1-84f4-0000f80464e3}')
SystemTraceControlGuid: Guid = Guid('{9e814aad-3204-11d2-9a82-006008a86939}')
DefaultTraceSecurityGuid: Guid = Guid('{0811c1af-7a07-4a06-82ed-869455cdf713}')
PrivateLoggerNotificationGuid: Guid = Guid('{3595ab5c-042a-4c8e-b942-2d059bfeb1b1}')
SystemIoFilterProviderGuid: Guid = Guid('{fbd09363-9e22-4661-b8bf-e7a34b535b8c}')
SystemObjectProviderGuid: Guid = Guid('{febd7460-3d1d-47eb-af49-c9eeb1e146f2}')
SystemPowerProviderGuid: Guid = Guid('{c134884a-32d5-4488-80e5-14ed7abb8269}')
SystemHypervisorProviderGuid: Guid = Guid('{bafa072a-918a-4bed-b622-bc152097098f}')
SystemLockProviderGuid: Guid = Guid('{721ddfd3-dacc-4e1e-b26a-a2cb31d4705a}')
SystemConfigProviderGuid: Guid = Guid('{fef3a8b6-318d-4b67-a96a-3b0f6b8f18fe}')
SystemCpuProviderGuid: Guid = Guid('{c6c5265f-eae8-4650-aae4-9d48603d8510}')
SystemSchedulerProviderGuid: Guid = Guid('{599a2a76-4d91-4910-9ac7-7d33f2e97a6c}')
SystemProfileProviderGuid: Guid = Guid('{bfeb0324-1cee-496f-a409-2ac2b48a6322}')
SystemIoProviderGuid: Guid = Guid('{3d5c43e3-0f1c-4202-b817-174c0070dc79}')
SystemMemoryProviderGuid: Guid = Guid('{82958ca9-b6cd-47f8-a3a8-03ae85a4bc24}')
SystemRegistryProviderGuid: Guid = Guid('{16156bd9-fab4-4cfa-a232-89d1099058e3}')
SystemProcessProviderGuid: Guid = Guid('{151f55dc-467d-471f-83b5-5f889d46ff66}')
SystemAlpcProviderGuid: Guid = Guid('{fcb9baaf-e529-4980-92e9-ced1a6aadfdf}')
SystemSyscallProviderGuid: Guid = Guid('{434286f7-6f1b-45bb-b37e-95f623046c7c}')
SystemInterruptProviderGuid: Guid = Guid('{d4bbee17-b545-4888-858b-744169015b25}')
SystemTimerProviderGuid: Guid = Guid('{4f061568-e215-499f-ab2e-eda0ae890a5b}')
KERNEL_LOGGER_NAMEW: String = 'NT Kernel Logger'
GLOBAL_LOGGER_NAMEW: String = 'GlobalLogger'
EVENT_LOGGER_NAMEW: String = 'EventLog'
DIAG_LOGGER_NAMEW: String = 'DiagLog'
KERNEL_LOGGER_NAMEA: String = 'NT Kernel Logger'
GLOBAL_LOGGER_NAMEA: String = 'GlobalLogger'
EVENT_LOGGER_NAMEA: String = 'EventLog'
DIAG_LOGGER_NAMEA: String = 'DiagLog'
MAX_MOF_FIELDS: UInt32 = 16
SYSTEM_EVENT_TYPE: UInt32 = 1
EVENT_TRACE_TYPE_INFO: UInt32 = 0
EVENT_TRACE_TYPE_START: UInt32 = 1
EVENT_TRACE_TYPE_END: UInt32 = 2
EVENT_TRACE_TYPE_STOP: UInt32 = 2
EVENT_TRACE_TYPE_DC_START: UInt32 = 3
EVENT_TRACE_TYPE_DC_END: UInt32 = 4
EVENT_TRACE_TYPE_EXTENSION: UInt32 = 5
EVENT_TRACE_TYPE_REPLY: UInt32 = 6
EVENT_TRACE_TYPE_DEQUEUE: UInt32 = 7
EVENT_TRACE_TYPE_RESUME: UInt32 = 7
EVENT_TRACE_TYPE_CHECKPOINT: UInt32 = 8
EVENT_TRACE_TYPE_SUSPEND: UInt32 = 8
EVENT_TRACE_TYPE_WINEVT_SEND: UInt32 = 9
EVENT_TRACE_TYPE_WINEVT_RECEIVE: UInt32 = 240
TRACE_LEVEL_NONE: UInt32 = 0
TRACE_LEVEL_CRITICAL: UInt32 = 1
TRACE_LEVEL_FATAL: UInt32 = 1
TRACE_LEVEL_ERROR: UInt32 = 2
TRACE_LEVEL_WARNING: UInt32 = 3
TRACE_LEVEL_INFORMATION: UInt32 = 4
TRACE_LEVEL_VERBOSE: UInt32 = 5
TRACE_LEVEL_RESERVED6: UInt32 = 6
TRACE_LEVEL_RESERVED7: UInt32 = 7
TRACE_LEVEL_RESERVED8: UInt32 = 8
TRACE_LEVEL_RESERVED9: UInt32 = 9
EVENT_TRACE_TYPE_LOAD: UInt32 = 10
EVENT_TRACE_TYPE_TERMINATE: UInt32 = 11
EVENT_TRACE_TYPE_IO_READ: UInt32 = 10
EVENT_TRACE_TYPE_IO_WRITE: UInt32 = 11
EVENT_TRACE_TYPE_IO_READ_INIT: UInt32 = 12
EVENT_TRACE_TYPE_IO_WRITE_INIT: UInt32 = 13
EVENT_TRACE_TYPE_IO_FLUSH: UInt32 = 14
EVENT_TRACE_TYPE_IO_FLUSH_INIT: UInt32 = 15
EVENT_TRACE_TYPE_IO_REDIRECTED_INIT: UInt32 = 16
EVENT_TRACE_TYPE_MM_TF: UInt32 = 10
EVENT_TRACE_TYPE_MM_DZF: UInt32 = 11
EVENT_TRACE_TYPE_MM_COW: UInt32 = 12
EVENT_TRACE_TYPE_MM_GPF: UInt32 = 13
EVENT_TRACE_TYPE_MM_HPF: UInt32 = 14
EVENT_TRACE_TYPE_MM_AV: UInt32 = 15
EVENT_TRACE_TYPE_SEND: UInt32 = 10
EVENT_TRACE_TYPE_RECEIVE: UInt32 = 11
EVENT_TRACE_TYPE_CONNECT: UInt32 = 12
EVENT_TRACE_TYPE_DISCONNECT: UInt32 = 13
EVENT_TRACE_TYPE_RETRANSMIT: UInt32 = 14
EVENT_TRACE_TYPE_ACCEPT: UInt32 = 15
EVENT_TRACE_TYPE_RECONNECT: UInt32 = 16
EVENT_TRACE_TYPE_CONNFAIL: UInt32 = 17
EVENT_TRACE_TYPE_COPY_TCP: UInt32 = 18
EVENT_TRACE_TYPE_COPY_ARP: UInt32 = 19
EVENT_TRACE_TYPE_ACKFULL: UInt32 = 20
EVENT_TRACE_TYPE_ACKPART: UInt32 = 21
EVENT_TRACE_TYPE_ACKDUP: UInt32 = 22
EVENT_TRACE_TYPE_GUIDMAP: UInt32 = 10
EVENT_TRACE_TYPE_CONFIG: UInt32 = 11
EVENT_TRACE_TYPE_SIDINFO: UInt32 = 12
EVENT_TRACE_TYPE_SECURITY: UInt32 = 13
EVENT_TRACE_TYPE_DBGID_RSDS: UInt32 = 64
EVENT_TRACE_TYPE_REGCREATE: UInt32 = 10
EVENT_TRACE_TYPE_REGOPEN: UInt32 = 11
EVENT_TRACE_TYPE_REGDELETE: UInt32 = 12
EVENT_TRACE_TYPE_REGQUERY: UInt32 = 13
EVENT_TRACE_TYPE_REGSETVALUE: UInt32 = 14
EVENT_TRACE_TYPE_REGDELETEVALUE: UInt32 = 15
EVENT_TRACE_TYPE_REGQUERYVALUE: UInt32 = 16
EVENT_TRACE_TYPE_REGENUMERATEKEY: UInt32 = 17
EVENT_TRACE_TYPE_REGENUMERATEVALUEKEY: UInt32 = 18
EVENT_TRACE_TYPE_REGQUERYMULTIPLEVALUE: UInt32 = 19
EVENT_TRACE_TYPE_REGSETINFORMATION: UInt32 = 20
EVENT_TRACE_TYPE_REGFLUSH: UInt32 = 21
EVENT_TRACE_TYPE_REGKCBCREATE: UInt32 = 22
EVENT_TRACE_TYPE_REGKCBDELETE: UInt32 = 23
EVENT_TRACE_TYPE_REGKCBRUNDOWNBEGIN: UInt32 = 24
EVENT_TRACE_TYPE_REGKCBRUNDOWNEND: UInt32 = 25
EVENT_TRACE_TYPE_REGVIRTUALIZE: UInt32 = 26
EVENT_TRACE_TYPE_REGCLOSE: UInt32 = 27
EVENT_TRACE_TYPE_REGSETSECURITY: UInt32 = 28
EVENT_TRACE_TYPE_REGQUERYSECURITY: UInt32 = 29
EVENT_TRACE_TYPE_REGCOMMIT: UInt32 = 30
EVENT_TRACE_TYPE_REGPREPARE: UInt32 = 31
EVENT_TRACE_TYPE_REGROLLBACK: UInt32 = 32
EVENT_TRACE_TYPE_REGMOUNTHIVE: UInt32 = 33
EVENT_TRACE_TYPE_CONFIG_CPU: UInt32 = 10
EVENT_TRACE_TYPE_CONFIG_PHYSICALDISK: UInt32 = 11
EVENT_TRACE_TYPE_CONFIG_LOGICALDISK: UInt32 = 12
EVENT_TRACE_TYPE_CONFIG_NIC: UInt32 = 13
EVENT_TRACE_TYPE_CONFIG_VIDEO: UInt32 = 14
EVENT_TRACE_TYPE_CONFIG_SERVICES: UInt32 = 15
EVENT_TRACE_TYPE_CONFIG_POWER: UInt32 = 16
EVENT_TRACE_TYPE_CONFIG_NETINFO: UInt32 = 17
EVENT_TRACE_TYPE_CONFIG_OPTICALMEDIA: UInt32 = 18
EVENT_TRACE_TYPE_CONFIG_PHYSICALDISK_EX: UInt32 = 19
EVENT_TRACE_TYPE_CONFIG_IRQ: UInt32 = 21
EVENT_TRACE_TYPE_CONFIG_PNP: UInt32 = 22
EVENT_TRACE_TYPE_CONFIG_IDECHANNEL: UInt32 = 23
EVENT_TRACE_TYPE_CONFIG_NUMANODE: UInt32 = 24
EVENT_TRACE_TYPE_CONFIG_PLATFORM: UInt32 = 25
EVENT_TRACE_TYPE_CONFIG_PROCESSORGROUP: UInt32 = 26
EVENT_TRACE_TYPE_CONFIG_PROCESSORNUMBER: UInt32 = 27
EVENT_TRACE_TYPE_CONFIG_DPI: UInt32 = 28
EVENT_TRACE_TYPE_CONFIG_CI_INFO: UInt32 = 29
EVENT_TRACE_TYPE_CONFIG_MACHINEID: UInt32 = 30
EVENT_TRACE_TYPE_CONFIG_DEFRAG: UInt32 = 31
EVENT_TRACE_TYPE_CONFIG_MOBILEPLATFORM: UInt32 = 32
EVENT_TRACE_TYPE_CONFIG_DEVICEFAMILY: UInt32 = 33
EVENT_TRACE_TYPE_CONFIG_FLIGHTID: UInt32 = 34
EVENT_TRACE_TYPE_CONFIG_PROCESSOR: UInt32 = 35
EVENT_TRACE_TYPE_CONFIG_VIRTUALIZATION: UInt32 = 36
EVENT_TRACE_TYPE_CONFIG_BOOT: UInt32 = 37
EVENT_TRACE_TYPE_OPTICAL_IO_READ: UInt32 = 55
EVENT_TRACE_TYPE_OPTICAL_IO_WRITE: UInt32 = 56
EVENT_TRACE_TYPE_OPTICAL_IO_FLUSH: UInt32 = 57
EVENT_TRACE_TYPE_OPTICAL_IO_READ_INIT: UInt32 = 58
EVENT_TRACE_TYPE_OPTICAL_IO_WRITE_INIT: UInt32 = 59
EVENT_TRACE_TYPE_OPTICAL_IO_FLUSH_INIT: UInt32 = 60
EVENT_TRACE_TYPE_FLT_PREOP_INIT: UInt32 = 96
EVENT_TRACE_TYPE_FLT_POSTOP_INIT: UInt32 = 97
EVENT_TRACE_TYPE_FLT_PREOP_COMPLETION: UInt32 = 98
EVENT_TRACE_TYPE_FLT_POSTOP_COMPLETION: UInt32 = 99
EVENT_TRACE_TYPE_FLT_PREOP_FAILURE: UInt32 = 100
EVENT_TRACE_TYPE_FLT_POSTOP_FAILURE: UInt32 = 101
EVENT_TRACE_FLAG_DEBUG_EVENTS: UInt32 = 4194304
EVENT_TRACE_FLAG_EXTENSION: UInt32 = 2147483648
EVENT_TRACE_FLAG_FORWARD_WMI: UInt32 = 1073741824
EVENT_TRACE_FLAG_ENABLE_RESERVE: UInt32 = 536870912
EVENT_TRACE_FILE_MODE_NONE: UInt32 = 0
EVENT_TRACE_FILE_MODE_SEQUENTIAL: UInt32 = 1
EVENT_TRACE_FILE_MODE_CIRCULAR: UInt32 = 2
EVENT_TRACE_FILE_MODE_APPEND: UInt32 = 4
EVENT_TRACE_REAL_TIME_MODE: UInt32 = 256
EVENT_TRACE_DELAY_OPEN_FILE_MODE: UInt32 = 512
EVENT_TRACE_BUFFERING_MODE: UInt32 = 1024
EVENT_TRACE_PRIVATE_LOGGER_MODE: UInt32 = 2048
EVENT_TRACE_ADD_HEADER_MODE: UInt32 = 4096
EVENT_TRACE_USE_GLOBAL_SEQUENCE: UInt32 = 16384
EVENT_TRACE_USE_LOCAL_SEQUENCE: UInt32 = 32768
EVENT_TRACE_RELOG_MODE: UInt32 = 65536
EVENT_TRACE_USE_PAGED_MEMORY: UInt32 = 16777216
EVENT_TRACE_FILE_MODE_NEWFILE: UInt32 = 8
EVENT_TRACE_FILE_MODE_PREALLOCATE: UInt32 = 32
EVENT_TRACE_NONSTOPPABLE_MODE: UInt32 = 64
EVENT_TRACE_SECURE_MODE: UInt32 = 128
EVENT_TRACE_USE_KBYTES_FOR_SIZE: UInt32 = 8192
EVENT_TRACE_PRIVATE_IN_PROC: UInt32 = 131072
EVENT_TRACE_MODE_RESERVED: UInt32 = 1048576
EVENT_TRACE_NO_PER_PROCESSOR_BUFFERING: UInt32 = 268435456
EVENT_TRACE_SYSTEM_LOGGER_MODE: UInt32 = 33554432
EVENT_TRACE_ADDTO_TRIAGE_DUMP: UInt32 = 2147483648
EVENT_TRACE_STOP_ON_HYBRID_SHUTDOWN: UInt32 = 4194304
EVENT_TRACE_PERSIST_ON_HYBRID_SHUTDOWN: UInt32 = 8388608
EVENT_TRACE_INDEPENDENT_SESSION_MODE: UInt32 = 134217728
EVENT_TRACE_COMPRESSED_MODE: UInt32 = 67108864
EVENT_TRACE_CONTROL_INCREMENT_FILE: UInt32 = 4
EVENT_TRACE_CONTROL_CONVERT_TO_REALTIME: UInt32 = 5
TRACE_MESSAGE_PERFORMANCE_TIMESTAMP: UInt32 = 16
TRACE_MESSAGE_POINTER32: UInt32 = 64
TRACE_MESSAGE_POINTER64: UInt32 = 128
TRACE_MESSAGE_FLAG_MASK: UInt32 = 65535
EVENT_TRACE_USE_PROCTIME: UInt32 = 1
EVENT_TRACE_USE_NOCPUTIME: UInt32 = 2
TRACE_HEADER_FLAG_USE_TIMESTAMP: UInt32 = 512
TRACE_HEADER_FLAG_TRACED_GUID: UInt32 = 131072
TRACE_HEADER_FLAG_LOG_WNODE: UInt32 = 262144
TRACE_HEADER_FLAG_USE_GUID_PTR: UInt32 = 524288
TRACE_HEADER_FLAG_USE_MOF_PTR: UInt32 = 1048576
SYSTEM_ALPC_KW_GENERAL: UInt64 = 1
SYSTEM_CONFIG_KW_SYSTEM: UInt64 = 1
SYSTEM_CONFIG_KW_GRAPHICS: UInt64 = 2
SYSTEM_CONFIG_KW_STORAGE: UInt64 = 4
SYSTEM_CONFIG_KW_NETWORK: UInt64 = 8
SYSTEM_CONFIG_KW_SERVICES: UInt64 = 16
SYSTEM_CONFIG_KW_PNP: UInt64 = 32
SYSTEM_CONFIG_KW_OPTICAL: UInt64 = 64
SYSTEM_CPU_KW_CONFIG: UInt64 = 1
SYSTEM_CPU_KW_CACHE_FLUSH: UInt64 = 2
SYSTEM_CPU_KW_SPEC_CONTROL: UInt64 = 4
SYSTEM_HYPERVISOR_KW_PROFILE: UInt64 = 1
SYSTEM_HYPERVISOR_KW_CALLOUTS: UInt64 = 2
SYSTEM_HYPERVISOR_KW_VTL_CHANGE: UInt64 = 4
SYSTEM_INTERRUPT_KW_GENERAL: UInt64 = 1
SYSTEM_INTERRUPT_KW_CLOCK_INTERRUPT: UInt64 = 2
SYSTEM_INTERRUPT_KW_DPC: UInt64 = 4
SYSTEM_INTERRUPT_KW_DPC_QUEUE: UInt64 = 8
SYSTEM_INTERRUPT_KW_WDF_DPC: UInt64 = 16
SYSTEM_INTERRUPT_KW_WDF_INTERRUPT: UInt64 = 32
SYSTEM_INTERRUPT_KW_IPI: UInt64 = 64
SYSTEM_IO_KW_DISK: UInt64 = 1
SYSTEM_IO_KW_DISK_INIT: UInt64 = 2
SYSTEM_IO_KW_FILENAME: UInt64 = 4
SYSTEM_IO_KW_SPLIT: UInt64 = 8
SYSTEM_IO_KW_FILE: UInt64 = 16
SYSTEM_IO_KW_OPTICAL: UInt64 = 32
SYSTEM_IO_KW_OPTICAL_INIT: UInt64 = 64
SYSTEM_IO_KW_DRIVERS: UInt64 = 128
SYSTEM_IO_KW_CC: UInt64 = 256
SYSTEM_IO_KW_NETWORK: UInt64 = 512
SYSTEM_IOFILTER_KW_GENERAL: UInt64 = 1
SYSTEM_IOFILTER_KW_INIT: UInt64 = 2
SYSTEM_IOFILTER_KW_FASTIO: UInt64 = 4
SYSTEM_IOFILTER_KW_FAILURE: UInt64 = 8
SYSTEM_LOCK_KW_SPINLOCK: UInt64 = 1
SYSTEM_LOCK_KW_SPINLOCK_COUNTERS: UInt64 = 2
SYSTEM_LOCK_KW_SYNC_OBJECTS: UInt64 = 4
SYSTEM_MEMORY_KW_GENERAL: UInt64 = 1
SYSTEM_MEMORY_KW_HARD_FAULTS: UInt64 = 2
SYSTEM_MEMORY_KW_ALL_FAULTS: UInt64 = 4
SYSTEM_MEMORY_KW_POOL: UInt64 = 8
SYSTEM_MEMORY_KW_MEMINFO: UInt64 = 16
SYSTEM_MEMORY_KW_PFSECTION: UInt64 = 32
SYSTEM_MEMORY_KW_MEMINFO_WS: UInt64 = 64
SYSTEM_MEMORY_KW_HEAP: UInt64 = 128
SYSTEM_MEMORY_KW_WS: UInt64 = 256
SYSTEM_MEMORY_KW_CONTMEM_GEN: UInt64 = 512
SYSTEM_MEMORY_KW_VIRTUAL_ALLOC: UInt64 = 1024
SYSTEM_MEMORY_KW_FOOTPRINT: UInt64 = 2048
SYSTEM_MEMORY_KW_SESSION: UInt64 = 4096
SYSTEM_MEMORY_KW_REFSET: UInt64 = 8192
SYSTEM_MEMORY_KW_VAMAP: UInt64 = 16384
SYSTEM_MEMORY_KW_NONTRADEABLE: UInt64 = 32768
SYSTEM_OBJECT_KW_GENERAL: UInt64 = 1
SYSTEM_OBJECT_KW_HANDLE: UInt64 = 2
SYSTEM_POWER_KW_GENERAL: UInt64 = 1
SYSTEM_POWER_KW_HIBER_RUNDOWN: UInt64 = 2
SYSTEM_POWER_KW_PROCESSOR_IDLE: UInt64 = 4
SYSTEM_POWER_KW_IDLE_SELECTION: UInt64 = 8
SYSTEM_POWER_KW_PPM_EXIT_LATENCY: UInt64 = 16
SYSTEM_PROCESS_KW_GENERAL: UInt64 = 1
SYSTEM_PROCESS_KW_INSWAP: UInt64 = 2
SYSTEM_PROCESS_KW_FREEZE: UInt64 = 4
SYSTEM_PROCESS_KW_PERF_COUNTER: UInt64 = 8
SYSTEM_PROCESS_KW_WAKE_COUNTER: UInt64 = 16
SYSTEM_PROCESS_KW_WAKE_DROP: UInt64 = 32
SYSTEM_PROCESS_KW_WAKE_EVENT: UInt64 = 64
SYSTEM_PROCESS_KW_DEBUG_EVENTS: UInt64 = 128
SYSTEM_PROCESS_KW_DBGPRINT: UInt64 = 256
SYSTEM_PROCESS_KW_JOB: UInt64 = 512
SYSTEM_PROCESS_KW_WORKER_THREAD: UInt64 = 1024
SYSTEM_PROCESS_KW_THREAD: UInt64 = 2048
SYSTEM_PROCESS_KW_LOADER: UInt64 = 4096
SYSTEM_PROFILE_KW_GENERAL: UInt64 = 1
SYSTEM_PROFILE_KW_PMC_PROFILE: UInt64 = 2
SYSTEM_REGISTRY_KW_GENERAL: UInt64 = 1
SYSTEM_REGISTRY_KW_HIVE: UInt64 = 2
SYSTEM_REGISTRY_KW_NOTIFICATION: UInt64 = 4
SYSTEM_SCHEDULER_KW_XSCHEDULER: UInt64 = 1
SYSTEM_SCHEDULER_KW_DISPATCHER: UInt64 = 2
SYSTEM_SCHEDULER_KW_KERNEL_QUEUE: UInt64 = 4
SYSTEM_SCHEDULER_KW_SHOULD_YIELD: UInt64 = 8
SYSTEM_SCHEDULER_KW_ANTI_STARVATION: UInt64 = 16
SYSTEM_SCHEDULER_KW_LOAD_BALANCER: UInt64 = 32
SYSTEM_SCHEDULER_KW_AFFINITY: UInt64 = 64
SYSTEM_SCHEDULER_KW_PRIORITY: UInt64 = 128
SYSTEM_SCHEDULER_KW_IDEAL_PROCESSOR: UInt64 = 256
SYSTEM_SCHEDULER_KW_CONTEXT_SWITCH: UInt64 = 512
SYSTEM_SCHEDULER_KW_COMPACT_CSWITCH: UInt64 = 1024
SYSTEM_SYSCALL_KW_GENERAL: UInt64 = 1
SYSTEM_TIMER_KW_GENERAL: UInt64 = 1
SYSTEM_TIMER_KW_CLOCK_TIMER: UInt64 = 2
SYSTEM_MEMORY_POOL_FILTER_ID: UInt32 = 1
ETW_NULL_TYPE_VALUE: UInt32 = 0
ETW_OBJECT_TYPE_VALUE: UInt32 = 1
ETW_STRING_TYPE_VALUE: UInt32 = 2
ETW_SBYTE_TYPE_VALUE: UInt32 = 3
ETW_BYTE_TYPE_VALUE: UInt32 = 4
ETW_INT16_TYPE_VALUE: UInt32 = 5
ETW_UINT16_TYPE_VALUE: UInt32 = 6
ETW_INT32_TYPE_VALUE: UInt32 = 7
ETW_UINT32_TYPE_VALUE: UInt32 = 8
ETW_INT64_TYPE_VALUE: UInt32 = 9
ETW_UINT64_TYPE_VALUE: UInt32 = 10
ETW_CHAR_TYPE_VALUE: UInt32 = 11
ETW_SINGLE_TYPE_VALUE: UInt32 = 12
ETW_DOUBLE_TYPE_VALUE: UInt32 = 13
ETW_BOOLEAN_TYPE_VALUE: UInt32 = 14
ETW_DECIMAL_TYPE_VALUE: UInt32 = 15
ETW_GUID_TYPE_VALUE: UInt32 = 101
ETW_ASCIICHAR_TYPE_VALUE: UInt32 = 102
ETW_ASCIISTRING_TYPE_VALUE: UInt32 = 103
ETW_COUNTED_STRING_TYPE_VALUE: UInt32 = 104
ETW_POINTER_TYPE_VALUE: UInt32 = 105
ETW_SIZET_TYPE_VALUE: UInt32 = 106
ETW_HIDDEN_TYPE_VALUE: UInt32 = 107
ETW_BOOL_TYPE_VALUE: UInt32 = 108
ETW_COUNTED_ANSISTRING_TYPE_VALUE: UInt32 = 109
ETW_REVERSED_COUNTED_STRING_TYPE_VALUE: UInt32 = 110
ETW_REVERSED_COUNTED_ANSISTRING_TYPE_VALUE: UInt32 = 111
ETW_NON_NULL_TERMINATED_STRING_TYPE_VALUE: UInt32 = 112
ETW_REDUCED_ANSISTRING_TYPE_VALUE: UInt32 = 113
ETW_REDUCED_STRING_TYPE_VALUE: UInt32 = 114
ETW_SID_TYPE_VALUE: UInt32 = 115
ETW_VARIANT_TYPE_VALUE: UInt32 = 116
ETW_PTVECTOR_TYPE_VALUE: UInt32 = 117
ETW_WMITIME_TYPE_VALUE: UInt32 = 118
ETW_DATETIME_TYPE_VALUE: UInt32 = 119
ETW_REFRENCE_TYPE_VALUE: UInt32 = 120
TRACE_PROVIDER_FLAG_LEGACY: UInt32 = 1
TRACE_PROVIDER_FLAG_PRE_ENABLE: UInt32 = 2
KERNEL_LOGGER_NAME: String = 'NT Kernel Logger'
GLOBAL_LOGGER_NAME: String = 'GlobalLogger'
EVENT_LOGGER_NAME: String = 'EventLog'
ENABLE_TRACE_PARAMETERS_VERSION: UInt32 = 1
ENABLE_TRACE_PARAMETERS_VERSION_2: UInt32 = 2
EVENT_MIN_LEVEL: UInt32 = 0
EVENT_MAX_LEVEL: UInt32 = 255
EVENT_ACTIVITY_CTRL_GET_ID: UInt32 = 1
EVENT_ACTIVITY_CTRL_SET_ID: UInt32 = 2
EVENT_ACTIVITY_CTRL_CREATE_ID: UInt32 = 3
EVENT_ACTIVITY_CTRL_GET_SET_ID: UInt32 = 4
EVENT_ACTIVITY_CTRL_CREATE_SET_ID: UInt32 = 5
MAX_EVENT_DATA_DESCRIPTORS: UInt32 = 128
MAX_EVENT_FILTER_DATA_SIZE: UInt32 = 1024
MAX_EVENT_FILTER_PAYLOAD_SIZE: UInt32 = 4096
MAX_EVENT_FILTER_EVENT_NAME_SIZE: UInt32 = 4096
MAX_EVENT_FILTERS_COUNT: UInt32 = 13
MAX_EVENT_FILTER_PID_COUNT: UInt32 = 8
MAX_EVENT_FILTER_EVENT_ID_COUNT: UInt32 = 64
EVENT_FILTER_TYPE_NONE: UInt32 = 0
EVENT_FILTER_TYPE_SCHEMATIZED: UInt32 = 2147483648
EVENT_FILTER_TYPE_SYSTEM_FLAGS: UInt32 = 2147483649
EVENT_FILTER_TYPE_TRACEHANDLE: UInt32 = 2147483650
EVENT_FILTER_TYPE_PID: UInt32 = 2147483652
EVENT_FILTER_TYPE_EXECUTABLE_NAME: UInt32 = 2147483656
EVENT_FILTER_TYPE_PACKAGE_ID: UInt32 = 2147483664
EVENT_FILTER_TYPE_PACKAGE_APP_ID: UInt32 = 2147483680
EVENT_FILTER_TYPE_PAYLOAD: UInt32 = 2147483904
EVENT_FILTER_TYPE_EVENT_ID: UInt32 = 2147484160
EVENT_FILTER_TYPE_EVENT_NAME: UInt32 = 2147484672
EVENT_FILTER_TYPE_STACKWALK: UInt32 = 2147487744
EVENT_FILTER_TYPE_STACKWALK_NAME: UInt32 = 2147491840
EVENT_FILTER_TYPE_STACKWALK_LEVEL_KW: UInt32 = 2147500032
EVENT_FILTER_TYPE_CONTAINER: UInt32 = 2147516416
EVENT_DATA_DESCRIPTOR_TYPE_NONE: UInt32 = 0
EVENT_DATA_DESCRIPTOR_TYPE_EVENT_METADATA: UInt32 = 1
EVENT_DATA_DESCRIPTOR_TYPE_PROVIDER_METADATA: UInt32 = 2
EVENT_DATA_DESCRIPTOR_TYPE_TIMESTAMP_OVERRIDE: UInt32 = 3
EVENT_WRITE_FLAG_NO_FAULTING: UInt32 = 1
EVENT_WRITE_FLAG_INPRIVATE: UInt32 = 2
EVENT_HEADER_EXT_TYPE_RELATED_ACTIVITYID: UInt32 = 1
EVENT_HEADER_EXT_TYPE_SID: UInt32 = 2
EVENT_HEADER_EXT_TYPE_TS_ID: UInt32 = 3
EVENT_HEADER_EXT_TYPE_INSTANCE_INFO: UInt32 = 4
EVENT_HEADER_EXT_TYPE_STACK_TRACE32: UInt32 = 5
EVENT_HEADER_EXT_TYPE_STACK_TRACE64: UInt32 = 6
EVENT_HEADER_EXT_TYPE_PEBS_INDEX: UInt32 = 7
EVENT_HEADER_EXT_TYPE_PMC_COUNTERS: UInt32 = 8
EVENT_HEADER_EXT_TYPE_PSM_KEY: UInt32 = 9
EVENT_HEADER_EXT_TYPE_EVENT_KEY: UInt32 = 10
EVENT_HEADER_EXT_TYPE_EVENT_SCHEMA_TL: UInt32 = 11
EVENT_HEADER_EXT_TYPE_PROV_TRAITS: UInt32 = 12
EVENT_HEADER_EXT_TYPE_PROCESS_START_KEY: UInt32 = 13
EVENT_HEADER_EXT_TYPE_CONTROL_GUID: UInt32 = 14
EVENT_HEADER_EXT_TYPE_QPC_DELTA: UInt32 = 15
EVENT_HEADER_EXT_TYPE_CONTAINER_ID: UInt32 = 16
EVENT_HEADER_EXT_TYPE_STACK_KEY32: UInt32 = 17
EVENT_HEADER_EXT_TYPE_STACK_KEY64: UInt32 = 18
EVENT_HEADER_EXT_TYPE_MAX: UInt32 = 19
EVENT_HEADER_PROPERTY_XML: UInt32 = 1
EVENT_HEADER_PROPERTY_FORWARDED_XML: UInt32 = 2
EVENT_HEADER_PROPERTY_LEGACY_EVENTLOG: UInt32 = 4
EVENT_HEADER_PROPERTY_RELOGGABLE: UInt32 = 8
EVENT_HEADER_FLAG_EXTENDED_INFO: UInt32 = 1
EVENT_HEADER_FLAG_PRIVATE_SESSION: UInt32 = 2
EVENT_HEADER_FLAG_STRING_ONLY: UInt32 = 4
EVENT_HEADER_FLAG_TRACE_MESSAGE: UInt32 = 8
EVENT_HEADER_FLAG_NO_CPUTIME: UInt32 = 16
EVENT_HEADER_FLAG_32_BIT_HEADER: UInt32 = 32
EVENT_HEADER_FLAG_64_BIT_HEADER: UInt32 = 64
EVENT_HEADER_FLAG_DECODE_GUID: UInt32 = 128
EVENT_HEADER_FLAG_CLASSIC_HEADER: UInt32 = 256
EVENT_HEADER_FLAG_PROCESSOR_INDEX: UInt32 = 512
EVENT_ENABLE_PROPERTY_SID: UInt32 = 1
EVENT_ENABLE_PROPERTY_TS_ID: UInt32 = 2
EVENT_ENABLE_PROPERTY_STACK_TRACE: UInt32 = 4
EVENT_ENABLE_PROPERTY_PSM_KEY: UInt32 = 8
EVENT_ENABLE_PROPERTY_IGNORE_KEYWORD_0: UInt32 = 16
EVENT_ENABLE_PROPERTY_PROVIDER_GROUP: UInt32 = 32
EVENT_ENABLE_PROPERTY_ENABLE_KEYWORD_0: UInt32 = 64
EVENT_ENABLE_PROPERTY_PROCESS_START_KEY: UInt32 = 128
EVENT_ENABLE_PROPERTY_EVENT_KEY: UInt32 = 256
EVENT_ENABLE_PROPERTY_EXCLUDE_INPRIVATE: UInt32 = 512
EVENT_ENABLE_PROPERTY_ENABLE_SILOS: UInt32 = 1024
EVENT_ENABLE_PROPERTY_SOURCE_CONTAINER_TRACKING: UInt32 = 2048
PROCESS_TRACE_MODE_REAL_TIME: UInt32 = 256
PROCESS_TRACE_MODE_RAW_TIMESTAMP: UInt32 = 4096
PROCESS_TRACE_MODE_EVENT_RECORD: UInt32 = 268435456
CLSID_TraceRelogger: Guid = Guid('{7b40792d-05ff-44c4-9058-f440c71f17d4}')
@winfunctype('ADVAPI32.dll')
def StartTraceW(TraceHandle: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.CONTROLTRACE_HANDLE), InstanceName: win32more.Windows.Win32.Foundation.PWSTR, Properties: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_PROPERTIES)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
StartTrace = UnicodeAlias('StartTraceW')
@winfunctype('ADVAPI32.dll')
def StartTraceA(TraceHandle: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.CONTROLTRACE_HANDLE), InstanceName: win32more.Windows.Win32.Foundation.PSTR, Properties: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_PROPERTIES)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def StopTraceW(TraceHandle: win32more.Windows.Win32.System.Diagnostics.Etw.CONTROLTRACE_HANDLE, InstanceName: win32more.Windows.Win32.Foundation.PWSTR, Properties: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_PROPERTIES)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
StopTrace = UnicodeAlias('StopTraceW')
@winfunctype('ADVAPI32.dll')
def StopTraceA(TraceHandle: win32more.Windows.Win32.System.Diagnostics.Etw.CONTROLTRACE_HANDLE, InstanceName: win32more.Windows.Win32.Foundation.PSTR, Properties: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_PROPERTIES)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def QueryTraceW(TraceHandle: win32more.Windows.Win32.System.Diagnostics.Etw.CONTROLTRACE_HANDLE, InstanceName: win32more.Windows.Win32.Foundation.PWSTR, Properties: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_PROPERTIES)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
QueryTrace = UnicodeAlias('QueryTraceW')
@winfunctype('ADVAPI32.dll')
def QueryTraceA(TraceHandle: win32more.Windows.Win32.System.Diagnostics.Etw.CONTROLTRACE_HANDLE, InstanceName: win32more.Windows.Win32.Foundation.PSTR, Properties: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_PROPERTIES)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def UpdateTraceW(TraceHandle: win32more.Windows.Win32.System.Diagnostics.Etw.CONTROLTRACE_HANDLE, InstanceName: win32more.Windows.Win32.Foundation.PWSTR, Properties: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_PROPERTIES)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
UpdateTrace = UnicodeAlias('UpdateTraceW')
@winfunctype('ADVAPI32.dll')
def UpdateTraceA(TraceHandle: win32more.Windows.Win32.System.Diagnostics.Etw.CONTROLTRACE_HANDLE, InstanceName: win32more.Windows.Win32.Foundation.PSTR, Properties: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_PROPERTIES)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def FlushTraceW(TraceHandle: win32more.Windows.Win32.System.Diagnostics.Etw.CONTROLTRACE_HANDLE, InstanceName: win32more.Windows.Win32.Foundation.PWSTR, Properties: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_PROPERTIES)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
FlushTrace = UnicodeAlias('FlushTraceW')
@winfunctype('ADVAPI32.dll')
def FlushTraceA(TraceHandle: win32more.Windows.Win32.System.Diagnostics.Etw.CONTROLTRACE_HANDLE, InstanceName: win32more.Windows.Win32.Foundation.PSTR, Properties: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_PROPERTIES)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def ControlTraceW(TraceHandle: win32more.Windows.Win32.System.Diagnostics.Etw.CONTROLTRACE_HANDLE, InstanceName: win32more.Windows.Win32.Foundation.PWSTR, Properties: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_PROPERTIES), ControlCode: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_CONTROL) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
ControlTrace = UnicodeAlias('ControlTraceW')
@winfunctype('ADVAPI32.dll')
def ControlTraceA(TraceHandle: win32more.Windows.Win32.System.Diagnostics.Etw.CONTROLTRACE_HANDLE, InstanceName: win32more.Windows.Win32.Foundation.PSTR, Properties: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_PROPERTIES), ControlCode: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_CONTROL) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def QueryAllTracesW(PropertyArray: POINTER(POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_PROPERTIES)), PropertyArrayCount: UInt32, LoggerCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
QueryAllTraces = UnicodeAlias('QueryAllTracesW')
@winfunctype('ADVAPI32.dll')
def QueryAllTracesA(PropertyArray: POINTER(POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_PROPERTIES)), PropertyArrayCount: UInt32, LoggerCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def EnableTrace(Enable: UInt32, EnableFlag: UInt32, EnableLevel: UInt32, ControlGuid: POINTER(Guid), TraceHandle: win32more.Windows.Win32.System.Diagnostics.Etw.CONTROLTRACE_HANDLE) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def EnableTraceEx(ProviderId: POINTER(Guid), SourceId: POINTER(Guid), TraceHandle: win32more.Windows.Win32.System.Diagnostics.Etw.CONTROLTRACE_HANDLE, IsEnabled: UInt32, Level: Byte, MatchAnyKeyword: UInt64, MatchAllKeyword: UInt64, EnableProperty: UInt32, EnableFilterDesc: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_FILTER_DESCRIPTOR)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def EnableTraceEx2(TraceHandle: win32more.Windows.Win32.System.Diagnostics.Etw.CONTROLTRACE_HANDLE, ProviderId: POINTER(Guid), ControlCode: UInt32, Level: Byte, MatchAnyKeyword: UInt64, MatchAllKeyword: UInt64, Timeout: UInt32, EnableParameters: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.ENABLE_TRACE_PARAMETERS)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def EnumerateTraceGuidsEx(TraceQueryInfoClass: win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_QUERY_INFO_CLASS, InBuffer: VoidPtr, InBufferSize: UInt32, OutBuffer: VoidPtr, OutBufferSize: UInt32, ReturnLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def TraceSetInformation(SessionHandle: win32more.Windows.Win32.System.Diagnostics.Etw.CONTROLTRACE_HANDLE, InformationClass: win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_QUERY_INFO_CLASS, TraceInformation: VoidPtr, InformationLength: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def TraceQueryInformation(SessionHandle: win32more.Windows.Win32.System.Diagnostics.Etw.CONTROLTRACE_HANDLE, InformationClass: win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_QUERY_INFO_CLASS, TraceInformation: VoidPtr, InformationLength: UInt32, ReturnLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def CreateTraceInstanceId(RegHandle: win32more.Windows.Win32.Foundation.HANDLE, InstInfo: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_INSTANCE_INFO)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def TraceEvent(TraceHandle: UInt64, EventTrace: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_HEADER)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def TraceEventInstance(TraceHandle: UInt64, EventTrace: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_INSTANCE_HEADER), InstInfo: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_INSTANCE_INFO), ParentInstInfo: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_INSTANCE_INFO)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def RegisterTraceGuidsW(RequestAddress: win32more.Windows.Win32.System.Diagnostics.Etw.WMIDPREQUEST, RequestContext: VoidPtr, ControlGuid: POINTER(Guid), GuidCount: UInt32, TraceGuidReg: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_GUID_REGISTRATION), MofImagePath: win32more.Windows.Win32.Foundation.PWSTR, MofResourceName: win32more.Windows.Win32.Foundation.PWSTR, RegistrationHandle: POINTER(UInt64)) -> UInt32: ...
RegisterTraceGuids = UnicodeAlias('RegisterTraceGuidsW')
@winfunctype('ADVAPI32.dll')
def RegisterTraceGuidsA(RequestAddress: win32more.Windows.Win32.System.Diagnostics.Etw.WMIDPREQUEST, RequestContext: VoidPtr, ControlGuid: POINTER(Guid), GuidCount: UInt32, TraceGuidReg: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_GUID_REGISTRATION), MofImagePath: win32more.Windows.Win32.Foundation.PSTR, MofResourceName: win32more.Windows.Win32.Foundation.PSTR, RegistrationHandle: POINTER(UInt64)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def EnumerateTraceGuids(GuidPropertiesArray: POINTER(POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_GUID_PROPERTIES)), PropertyArrayCount: UInt32, GuidCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def UnregisterTraceGuids(RegistrationHandle: UInt64) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def GetTraceLoggerHandle(Buffer: VoidPtr) -> UInt64: ...
@winfunctype('ADVAPI32.dll')
def GetTraceEnableLevel(TraceHandle: UInt64) -> Byte: ...
@winfunctype('ADVAPI32.dll')
def GetTraceEnableFlags(TraceHandle: UInt64) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def OpenTraceW(Logfile: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_LOGFILEW)) -> win32more.Windows.Win32.System.Diagnostics.Etw.PROCESSTRACE_HANDLE: ...
OpenTrace = UnicodeAlias('OpenTraceW')
@winfunctype('ADVAPI32.dll')
def ProcessTrace(HandleArray: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.PROCESSTRACE_HANDLE), HandleCount: UInt32, StartTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME), EndTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def CloseTrace(TraceHandle: win32more.Windows.Win32.System.Diagnostics.Etw.PROCESSTRACE_HANDLE) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def OpenTraceFromBufferStream(Options: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.ETW_OPEN_TRACE_OPTIONS), BufferCompletionCallback: win32more.Windows.Win32.System.Diagnostics.Etw.PETW_BUFFER_COMPLETION_CALLBACK, BufferCompletionContext: VoidPtr) -> UInt64: ...
@winfunctype('ADVAPI32.dll')
def OpenTraceFromRealTimeLogger(LoggerName: win32more.Windows.Win32.Foundation.PWSTR, Options: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.ETW_OPEN_TRACE_OPTIONS), LogFileHeader: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_LOGFILE_HEADER)) -> UInt64: ...
@winfunctype('ADVAPI32.dll')
def OpenTraceFromRealTimeLoggerWithAllocationOptions(LoggerName: win32more.Windows.Win32.Foundation.PWSTR, Options: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.ETW_OPEN_TRACE_OPTIONS), AllocationSize: UIntPtr, MemoryPartitionHandle: win32more.Windows.Win32.Foundation.HANDLE, LogFileHeader: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_LOGFILE_HEADER)) -> UInt64: ...
@winfunctype('ADVAPI32.dll')
def OpenTraceFromFile(LogFileName: win32more.Windows.Win32.Foundation.PWSTR, Options: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.ETW_OPEN_TRACE_OPTIONS), LogFileHeader: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_LOGFILE_HEADER)) -> UInt64: ...
@winfunctype('ADVAPI32.dll')
def ProcessTraceBufferIncrementReference(TraceHandle: UInt64, Buffer: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.ETW_BUFFER_HEADER)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def ProcessTraceBufferDecrementReference(Buffer: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.ETW_BUFFER_HEADER)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def ProcessTraceAddBufferToBufferStream(TraceHandle: UInt64, Buffer: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.ETW_BUFFER_HEADER), BufferSize: UInt32) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def QueryTraceProcessingHandle(ProcessingHandle: win32more.Windows.Win32.System.Diagnostics.Etw.PROCESSTRACE_HANDLE, InformationClass: win32more.Windows.Win32.System.Diagnostics.Etw.ETW_PROCESS_HANDLE_INFO_TYPE, InBuffer: VoidPtr, InBufferSize: UInt32, OutBuffer: VoidPtr, OutBufferSize: UInt32, ReturnLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def OpenTraceA(Logfile: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_LOGFILEA)) -> win32more.Windows.Win32.System.Diagnostics.Etw.PROCESSTRACE_HANDLE: ...
@winfunctype('ADVAPI32.dll')
def SetTraceCallback(pGuid: POINTER(Guid), EventCallback: win32more.Windows.Win32.System.Diagnostics.Etw.PEVENT_CALLBACK) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def RemoveTraceCallback(pGuid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@cfunctype('ADVAPI32.dll', variadic=True)
def TraceMessage(LoggerHandle: UInt64, MessageFlags: win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_MESSAGE_FLAGS, MessageGuid: POINTER(Guid), MessageNumber: UInt16, *__arglist) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def TraceMessageVa(LoggerHandle: UInt64, MessageFlags: win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_MESSAGE_FLAGS, MessageGuid: POINTER(Guid), MessageNumber: UInt16, MessageArgList: POINTER(SByte)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def EventRegister(ProviderId: POINTER(Guid), EnableCallback: win32more.Windows.Win32.System.Diagnostics.Etw.PENABLECALLBACK, CallbackContext: VoidPtr, RegHandle: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.REGHANDLE)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def EventUnregister(RegHandle: win32more.Windows.Win32.System.Diagnostics.Etw.REGHANDLE) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def EventSetInformation(RegHandle: win32more.Windows.Win32.System.Diagnostics.Etw.REGHANDLE, InformationClass: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_INFO_CLASS, EventInformation: VoidPtr, InformationLength: UInt32) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def EventEnabled(RegHandle: win32more.Windows.Win32.System.Diagnostics.Etw.REGHANDLE, EventDescriptor: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_DESCRIPTOR)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('ADVAPI32.dll')
def EventProviderEnabled(RegHandle: win32more.Windows.Win32.System.Diagnostics.Etw.REGHANDLE, Level: Byte, Keyword: UInt64) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('ADVAPI32.dll')
def EventWrite(RegHandle: win32more.Windows.Win32.System.Diagnostics.Etw.REGHANDLE, EventDescriptor: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_DESCRIPTOR), UserDataCount: UInt32, UserData: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_DATA_DESCRIPTOR)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def EventWriteTransfer(RegHandle: win32more.Windows.Win32.System.Diagnostics.Etw.REGHANDLE, EventDescriptor: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_DESCRIPTOR), ActivityId: POINTER(Guid), RelatedActivityId: POINTER(Guid), UserDataCount: UInt32, UserData: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_DATA_DESCRIPTOR)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def EventWriteEx(RegHandle: win32more.Windows.Win32.System.Diagnostics.Etw.REGHANDLE, EventDescriptor: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_DESCRIPTOR), Filter: UInt64, Flags: UInt32, ActivityId: POINTER(Guid), RelatedActivityId: POINTER(Guid), UserDataCount: UInt32, UserData: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_DATA_DESCRIPTOR)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def EventWriteString(RegHandle: win32more.Windows.Win32.System.Diagnostics.Etw.REGHANDLE, Level: Byte, Keyword: UInt64, String: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def EventActivityIdControl(ControlCode: UInt32, ActivityId: POINTER(Guid)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def EventAccessControl(Guid: POINTER(Guid), Operation: UInt32, Sid: win32more.Windows.Win32.Security.PSID, Rights: UInt32, AllowOrDeny: win32more.Windows.Win32.Foundation.BOOLEAN) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def EventAccessQuery(Guid: POINTER(Guid), Buffer: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, BufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def EventAccessRemove(Guid: POINTER(Guid)) -> UInt32: ...
@winfunctype('tdh.dll')
def TdhCreatePayloadFilter(ProviderGuid: POINTER(Guid), EventDescriptor: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_DESCRIPTOR), EventMatchANY: win32more.Windows.Win32.Foundation.BOOLEAN, PayloadPredicateCount: UInt32, PayloadPredicates: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.PAYLOAD_FILTER_PREDICATE), PayloadFilter: POINTER(VoidPtr)) -> UInt32: ...
@winfunctype('tdh.dll')
def TdhDeletePayloadFilter(PayloadFilter: POINTER(VoidPtr)) -> UInt32: ...
@winfunctype('tdh.dll')
def TdhAggregatePayloadFilters(PayloadFilterCount: UInt32, PayloadFilterPtrs: POINTER(VoidPtr), EventMatchALLFlags: POINTER(win32more.Windows.Win32.Foundation.BOOLEAN), EventFilterDescriptor: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_FILTER_DESCRIPTOR)) -> UInt32: ...
@winfunctype('tdh.dll')
def TdhCleanupPayloadEventFilterDescriptor(EventFilterDescriptor: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_FILTER_DESCRIPTOR)) -> UInt32: ...
@winfunctype('TDH.dll')
def TdhGetEventInformation(Event: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_RECORD), TdhContextCount: UInt32, TdhContext: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.TDH_CONTEXT), Buffer: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_EVENT_INFO), BufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('TDH.dll')
def TdhGetEventMapInformation(pEvent: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_RECORD), pMapName: win32more.Windows.Win32.Foundation.PWSTR, pBuffer: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_MAP_INFO), pBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('TDH.dll')
def TdhGetPropertySize(pEvent: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_RECORD), TdhContextCount: UInt32, pTdhContext: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.TDH_CONTEXT), PropertyDataCount: UInt32, pPropertyData: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.PROPERTY_DATA_DESCRIPTOR), pPropertySize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('TDH.dll')
def TdhGetProperty(pEvent: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_RECORD), TdhContextCount: UInt32, pTdhContext: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.TDH_CONTEXT), PropertyDataCount: UInt32, pPropertyData: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.PROPERTY_DATA_DESCRIPTOR), BufferSize: UInt32, pBuffer: POINTER(Byte)) -> UInt32: ...
@winfunctype('TDH.dll')
def TdhEnumerateProviders(pBuffer: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.PROVIDER_ENUMERATION_INFO), pBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('tdh.dll')
def TdhEnumerateProvidersForDecodingSource(filter: win32more.Windows.Win32.System.Diagnostics.Etw.DECODING_SOURCE, buffer: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.PROVIDER_ENUMERATION_INFO), bufferSize: UInt32, bufferRequired: POINTER(UInt32)) -> UInt32: ...
@winfunctype('TDH.dll')
def TdhQueryProviderFieldInformation(pGuid: POINTER(Guid), EventFieldValue: UInt64, EventFieldType: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_FIELD_TYPE, pBuffer: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.PROVIDER_FIELD_INFOARRAY), pBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('TDH.dll')
def TdhEnumerateProviderFieldInformation(pGuid: POINTER(Guid), EventFieldType: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_FIELD_TYPE, pBuffer: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.PROVIDER_FIELD_INFOARRAY), pBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('tdh.dll')
def TdhEnumerateProviderFilters(Guid: POINTER(Guid), TdhContextCount: UInt32, TdhContext: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.TDH_CONTEXT), FilterCount: POINTER(UInt32), Buffer: POINTER(POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.PROVIDER_FILTER_INFO)), BufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('TDH.dll')
def TdhLoadManifest(Manifest: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('TDH.dll')
def TdhLoadManifestFromMemory(pData: VoidPtr, cbData: UInt32) -> UInt32: ...
@winfunctype('TDH.dll')
def TdhUnloadManifest(Manifest: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('TDH.dll')
def TdhUnloadManifestFromMemory(pData: VoidPtr, cbData: UInt32) -> UInt32: ...
@winfunctype('TDH.dll')
def TdhFormatProperty(EventInfo: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_EVENT_INFO), MapInfo: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_MAP_INFO), PointerSize: UInt32, PropertyInType: UInt16, PropertyOutType: UInt16, PropertyLength: UInt16, UserDataLength: UInt16, UserData: POINTER(Byte), BufferSize: POINTER(UInt32), Buffer: win32more.Windows.Win32.Foundation.PWSTR, UserDataConsumed: POINTER(UInt16)) -> UInt32: ...
@winfunctype('tdh.dll')
def TdhOpenDecodingHandle(Handle: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.TDH_HANDLE)) -> UInt32: ...
@winfunctype('tdh.dll')
def TdhSetDecodingParameter(Handle: win32more.Windows.Win32.System.Diagnostics.Etw.TDH_HANDLE, TdhContext: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.TDH_CONTEXT)) -> UInt32: ...
@winfunctype('tdh.dll')
def TdhGetDecodingParameter(Handle: win32more.Windows.Win32.System.Diagnostics.Etw.TDH_HANDLE, TdhContext: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.TDH_CONTEXT)) -> UInt32: ...
@winfunctype('tdh.dll')
def TdhGetWppProperty(Handle: win32more.Windows.Win32.System.Diagnostics.Etw.TDH_HANDLE, EventRecord: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_RECORD), PropertyName: win32more.Windows.Win32.Foundation.PWSTR, BufferSize: POINTER(UInt32), Buffer: POINTER(Byte)) -> UInt32: ...
@winfunctype('tdh.dll')
def TdhGetWppMessage(Handle: win32more.Windows.Win32.System.Diagnostics.Etw.TDH_HANDLE, EventRecord: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_RECORD), BufferSize: POINTER(UInt32), Buffer: POINTER(Byte)) -> UInt32: ...
@winfunctype('tdh.dll')
def TdhCloseDecodingHandle(Handle: win32more.Windows.Win32.System.Diagnostics.Etw.TDH_HANDLE) -> UInt32: ...
@winfunctype('tdh.dll')
def TdhLoadManifestFromBinary(BinaryPath: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('TDH.dll')
def TdhEnumerateManifestProviderEvents(ProviderGuid: POINTER(Guid), Buffer: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.PROVIDER_EVENT_INFO), BufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('TDH.dll')
def TdhGetManifestEventInformation(ProviderGuid: POINTER(Guid), EventDescriptor: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_DESCRIPTOR), Buffer: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_EVENT_INFO), BufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def CveEventWrite(CveId: win32more.Windows.Win32.Foundation.PWSTR, AdditionalDetails: win32more.Windows.Win32.Foundation.PWSTR) -> Int32: ...
class CLASSIC_EVENT_ID(Structure):
    EventGuid: Guid
    Type: Byte
    Reserved: Byte * 7
class CONTROLTRACE_HANDLE(Structure):
    Value: UInt64
CTraceRelogger = Guid('{7b40792d-05ff-44c4-9058-f440c71f17d4}')
DECODING_SOURCE = Int32
DecodingSourceXMLFile: win32more.Windows.Win32.System.Diagnostics.Etw.DECODING_SOURCE = 0
DecodingSourceWbem: win32more.Windows.Win32.System.Diagnostics.Etw.DECODING_SOURCE = 1
DecodingSourceWPP: win32more.Windows.Win32.System.Diagnostics.Etw.DECODING_SOURCE = 2
DecodingSourceTlg: win32more.Windows.Win32.System.Diagnostics.Etw.DECODING_SOURCE = 3
DecodingSourceMax: win32more.Windows.Win32.System.Diagnostics.Etw.DECODING_SOURCE = 4
ENABLECALLBACK_ENABLED_STATE = UInt32
EVENT_CONTROL_CODE_DISABLE_PROVIDER: win32more.Windows.Win32.System.Diagnostics.Etw.ENABLECALLBACK_ENABLED_STATE = 0
EVENT_CONTROL_CODE_ENABLE_PROVIDER: win32more.Windows.Win32.System.Diagnostics.Etw.ENABLECALLBACK_ENABLED_STATE = 1
EVENT_CONTROL_CODE_CAPTURE_STATE: win32more.Windows.Win32.System.Diagnostics.Etw.ENABLECALLBACK_ENABLED_STATE = 2
class ENABLE_TRACE_PARAMETERS(Structure):
    Version: UInt32
    EnableProperty: UInt32
    ControlFlags: UInt32
    SourceId: Guid
    EnableFilterDesc: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_FILTER_DESCRIPTOR)
    FilterDescCount: UInt32
class ENABLE_TRACE_PARAMETERS_V1(Structure):
    Version: UInt32
    EnableProperty: UInt32
    ControlFlags: UInt32
    SourceId: Guid
    EnableFilterDesc: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_FILTER_DESCRIPTOR)
class ETW_BUFFER_CALLBACK_INFORMATION(Structure):
    TraceHandle: UInt64
    LogfileHeader: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_LOGFILE_HEADER)
    BuffersRead: UInt32
class ETW_BUFFER_CONTEXT(Structure):
    Anonymous: _Anonymous_e__Union
    LoggerId: UInt16
    class _Anonymous_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        ProcessorIndex: UInt16
        class _Anonymous_e__Struct(Structure):
            ProcessorNumber: Byte
            Alignment: Byte
class ETW_BUFFER_HEADER(Structure):
    Reserved1: UInt32 * 4
    TimeStamp: Int64
    Reserved2: UInt32 * 4
    ClientContext: win32more.Windows.Win32.System.Diagnostics.Etw.ETW_BUFFER_CONTEXT
    Reserved3: UInt32
    FilledBytes: UInt32
    Reserved4: UInt32 * 5
ETW_COMPRESSION_RESUMPTION_MODE = Int32
EtwCompressionModeRestart: win32more.Windows.Win32.System.Diagnostics.Etw.ETW_COMPRESSION_RESUMPTION_MODE = 0
EtwCompressionModeNoDisable: win32more.Windows.Win32.System.Diagnostics.Etw.ETW_COMPRESSION_RESUMPTION_MODE = 1
EtwCompressionModeNoRestart: win32more.Windows.Win32.System.Diagnostics.Etw.ETW_COMPRESSION_RESUMPTION_MODE = 2
class ETW_OPEN_TRACE_OPTIONS(Structure):
    ProcessTraceModes: win32more.Windows.Win32.System.Diagnostics.Etw.ETW_PROCESS_TRACE_MODES
    EventCallback: win32more.Windows.Win32.System.Diagnostics.Etw.PEVENT_RECORD_CALLBACK
    EventCallbackContext: VoidPtr
    BufferCallback: win32more.Windows.Win32.System.Diagnostics.Etw.PETW_BUFFER_CALLBACK
    BufferCallbackContext: VoidPtr
class ETW_PMC_COUNTER_OWNER(Structure):
    OwnerType: win32more.Windows.Win32.System.Diagnostics.Etw.ETW_PMC_COUNTER_OWNER_TYPE
    ProfileSource: UInt32
    OwnerTag: UInt32
class ETW_PMC_COUNTER_OWNERSHIP_STATUS(Structure):
    ProcessorNumber: UInt32
    NumberOfCounters: UInt32
    CounterOwners: win32more.Windows.Win32.System.Diagnostics.Etw.ETW_PMC_COUNTER_OWNER * 1
ETW_PMC_COUNTER_OWNER_TYPE = Int32
EtwPmcOwnerFree: win32more.Windows.Win32.System.Diagnostics.Etw.ETW_PMC_COUNTER_OWNER_TYPE = 0
EtwPmcOwnerUntagged: win32more.Windows.Win32.System.Diagnostics.Etw.ETW_PMC_COUNTER_OWNER_TYPE = 1
EtwPmcOwnerTagged: win32more.Windows.Win32.System.Diagnostics.Etw.ETW_PMC_COUNTER_OWNER_TYPE = 2
EtwPmcOwnerTaggedWithSource: win32more.Windows.Win32.System.Diagnostics.Etw.ETW_PMC_COUNTER_OWNER_TYPE = 3
class ETW_PMC_SESSION_INFO(Structure):
    NextEntryOffset: UInt32
    LoggerId: UInt16
    Reserved: UInt16
    ProfileSourceCount: UInt32
    HookIdCount: UInt32
ETW_PROCESS_HANDLE_INFO_TYPE = Int32
EtwQueryPartitionInformation: win32more.Windows.Win32.System.Diagnostics.Etw.ETW_PROCESS_HANDLE_INFO_TYPE = 1
EtwQueryPartitionInformationV2: win32more.Windows.Win32.System.Diagnostics.Etw.ETW_PROCESS_HANDLE_INFO_TYPE = 2
EtwQueryLastDroppedTimes: win32more.Windows.Win32.System.Diagnostics.Etw.ETW_PROCESS_HANDLE_INFO_TYPE = 3
EtwQueryLogFileHeader: win32more.Windows.Win32.System.Diagnostics.Etw.ETW_PROCESS_HANDLE_INFO_TYPE = 4
EtwQueryProcessHandleInfoMax: win32more.Windows.Win32.System.Diagnostics.Etw.ETW_PROCESS_HANDLE_INFO_TYPE = 5
ETW_PROCESS_TRACE_MODES = Int32
ETW_PROCESS_TRACE_MODE_NONE: win32more.Windows.Win32.System.Diagnostics.Etw.ETW_PROCESS_TRACE_MODES = 0
ETW_PROCESS_TRACE_MODE_RAW_TIMESTAMP: win32more.Windows.Win32.System.Diagnostics.Etw.ETW_PROCESS_TRACE_MODES = 1
ETW_PROVIDER_TRAIT_TYPE = Int32
EtwProviderTraitTypeGroup: win32more.Windows.Win32.System.Diagnostics.Etw.ETW_PROVIDER_TRAIT_TYPE = 1
EtwProviderTraitDecodeGuid: win32more.Windows.Win32.System.Diagnostics.Etw.ETW_PROVIDER_TRAIT_TYPE = 2
EtwProviderTraitTypeMax: win32more.Windows.Win32.System.Diagnostics.Etw.ETW_PROVIDER_TRAIT_TYPE = 3
class ETW_TRACE_PARTITION_INFORMATION(Structure):
    PartitionId: Guid
    ParentId: Guid
    QpcOffsetFromRoot: Int64
    PartitionType: UInt32
class ETW_TRACE_PARTITION_INFORMATION_V2(Structure):
    QpcOffsetFromRoot: Int64
    PartitionType: UInt32
    PartitionId: win32more.Windows.Win32.Foundation.PWSTR
    ParentId: win32more.Windows.Win32.Foundation.PWSTR
EVENTSECURITYOPERATION = Int32
EventSecuritySetDACL: win32more.Windows.Win32.System.Diagnostics.Etw.EVENTSECURITYOPERATION = 0
EventSecuritySetSACL: win32more.Windows.Win32.System.Diagnostics.Etw.EVENTSECURITYOPERATION = 1
EventSecurityAddDACL: win32more.Windows.Win32.System.Diagnostics.Etw.EVENTSECURITYOPERATION = 2
EventSecurityAddSACL: win32more.Windows.Win32.System.Diagnostics.Etw.EVENTSECURITYOPERATION = 3
EventSecurityMax: win32more.Windows.Win32.System.Diagnostics.Etw.EVENTSECURITYOPERATION = 4
class EVENT_DATA_DESCRIPTOR(Structure):
    Ptr: UInt64
    Size: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Reserved: UInt32
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            Type: Byte
            Reserved1: Byte
            Reserved2: UInt16
class EVENT_DESCRIPTOR(Structure):
    Id: UInt16
    Version: Byte
    Channel: Byte
    Level: Byte
    Opcode: Byte
    Task: UInt16
    Keyword: UInt64
class EVENT_EXTENDED_ITEM_EVENT_KEY(Structure):
    Key: UInt64
class EVENT_EXTENDED_ITEM_INSTANCE(Structure):
    InstanceId: UInt32
    ParentInstanceId: UInt32
    ParentGuid: Guid
class EVENT_EXTENDED_ITEM_PEBS_INDEX(Structure):
    PebsIndex: UInt64
class EVENT_EXTENDED_ITEM_PMC_COUNTERS(Structure):
    Counter: UInt64 * 1
class EVENT_EXTENDED_ITEM_PROCESS_START_KEY(Structure):
    ProcessStartKey: UInt64
class EVENT_EXTENDED_ITEM_RELATED_ACTIVITYID(Structure):
    RelatedActivityId: Guid
class EVENT_EXTENDED_ITEM_STACK_KEY32(Structure):
    MatchId: UInt64
    StackKey: UInt32
    Padding: UInt32
class EVENT_EXTENDED_ITEM_STACK_KEY64(Structure):
    MatchId: UInt64
    StackKey: UInt64
class EVENT_EXTENDED_ITEM_STACK_TRACE32(Structure):
    MatchId: UInt64
    Address: UInt32 * 1
class EVENT_EXTENDED_ITEM_STACK_TRACE64(Structure):
    MatchId: UInt64
    Address: UInt64 * 1
class EVENT_EXTENDED_ITEM_TS_ID(Structure):
    SessionId: UInt32
EVENT_FIELD_TYPE = Int32
EventKeywordInformation: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_FIELD_TYPE = 0
EventLevelInformation: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_FIELD_TYPE = 1
EventChannelInformation: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_FIELD_TYPE = 2
EventTaskInformation: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_FIELD_TYPE = 3
EventOpcodeInformation: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_FIELD_TYPE = 4
EventInformationMax: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_FIELD_TYPE = 5
class EVENT_FILTER_DESCRIPTOR(Structure):
    Ptr: UInt64
    Size: UInt32
    Type: UInt32
class EVENT_FILTER_EVENT_ID(Structure):
    FilterIn: win32more.Windows.Win32.Foundation.BOOLEAN
    Reserved: Byte
    Count: UInt16
    Events: UInt16 * 1
class EVENT_FILTER_EVENT_NAME(Structure):
    MatchAnyKeyword: UInt64
    MatchAllKeyword: UInt64
    Level: Byte
    FilterIn: win32more.Windows.Win32.Foundation.BOOLEAN
    NameCount: UInt16
    Names: Byte * 1
class EVENT_FILTER_HEADER(Structure):
    Id: UInt16
    Version: Byte
    Reserved: Byte * 5
    InstanceId: UInt64
    Size: UInt32
    NextOffset: UInt32
class EVENT_FILTER_LEVEL_KW(Structure):
    MatchAnyKeyword: UInt64
    MatchAllKeyword: UInt64
    Level: Byte
    FilterIn: win32more.Windows.Win32.Foundation.BOOLEAN
class EVENT_HEADER(Structure):
    Size: UInt16
    HeaderType: UInt16
    Flags: UInt16
    EventProperty: UInt16
    ThreadId: UInt32
    ProcessId: UInt32
    TimeStamp: Int64
    ProviderId: Guid
    EventDescriptor: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_DESCRIPTOR
    Anonymous: _Anonymous_e__Union
    ActivityId: Guid
    class _Anonymous_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        ProcessorTime: UInt64
        class _Anonymous_e__Struct(Structure):
            KernelTime: UInt32
            UserTime: UInt32
class EVENT_HEADER_EXTENDED_DATA_ITEM(Structure):
    Reserved1: UInt16
    ExtType: UInt16
    Anonymous: _Anonymous_e__Struct
    DataSize: UInt16
    DataPtr: UInt64
    class _Anonymous_e__Struct(Structure):
        Linkage: Annotated[UInt16, 1]
        Reserved2: Annotated[UInt16, 15]
EVENT_INFO_CLASS = Int32
EventProviderBinaryTrackInfo: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_INFO_CLASS = 0
EventProviderSetReserved1: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_INFO_CLASS = 1
EventProviderSetTraits: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_INFO_CLASS = 2
EventProviderUseDescriptorType: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_INFO_CLASS = 3
MaxEventInfo: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_INFO_CLASS = 4
class EVENT_INSTANCE_HEADER(Structure):
    Size: UInt16
    Anonymous1: _Anonymous1_e__Union
    Anonymous2: _Anonymous2_e__Union
    ThreadId: UInt32
    ProcessId: UInt32
    TimeStamp: Int64
    RegHandle: UInt64
    InstanceId: UInt32
    ParentInstanceId: UInt32
    Anonymous3: _Anonymous3_e__Union
    ParentRegHandle: UInt64
    class _Anonymous1_e__Union(Union):
        FieldTypeFlags: UInt16
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            HeaderType: Byte
            MarkerFlags: Byte
    class _Anonymous2_e__Union(Union):
        Version: UInt32
        Class: _Class_e__Struct
        class _Class_e__Struct(Structure):
            Type: Byte
            Level: Byte
            Version: UInt16
    class _Anonymous3_e__Union(Union):
        Anonymous1: _Anonymous1_e__Struct
        ProcessorTime: UInt64
        Anonymous2: _Anonymous2_e__Struct
        class _Anonymous1_e__Struct(Structure):
            KernelTime: UInt32
            UserTime: UInt32
        class _Anonymous2_e__Struct(Structure):
            EventId: UInt32
            Flags: UInt32
class EVENT_INSTANCE_INFO(Structure):
    RegHandle: win32more.Windows.Win32.Foundation.HANDLE
    InstanceId: UInt32
class EVENT_MAP_ENTRY(Structure):
    OutputOffset: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Value: UInt32
        InputOffset: UInt32
class EVENT_MAP_INFO(Structure):
    NameOffset: UInt32
    Flag: win32more.Windows.Win32.System.Diagnostics.Etw.MAP_FLAGS
    EntryCount: UInt32
    Anonymous: _Anonymous_e__Union
    MapEntryArray: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_MAP_ENTRY * 1
    class _Anonymous_e__Union(Union):
        MapEntryValueType: win32more.Windows.Win32.System.Diagnostics.Etw.MAP_VALUETYPE
        FormatStringOffset: UInt32
class EVENT_PROPERTY_INFO(Structure):
    Flags: win32more.Windows.Win32.System.Diagnostics.Etw.PROPERTY_FLAGS
    NameOffset: UInt32
    Anonymous1: _Anonymous1_e__Union
    Anonymous2: _Anonymous2_e__Union
    Anonymous3: _Anonymous3_e__Union
    Anonymous4: _Anonymous4_e__Union
    class _Anonymous1_e__Union(Union):
        nonStructType: _nonStructType
        structType: _structType
        customSchemaType: _customSchemaType
        class _nonStructType(Structure):
            InType: UInt16
            OutType: UInt16
            MapNameOffset: UInt32
        class _structType(Structure):
            StructStartIndex: UInt16
            NumOfStructMembers: UInt16
            padding: UInt32
        class _customSchemaType(Structure):
            InType: UInt16
            OutType: UInt16
            CustomSchemaOffset: UInt32
    class _Anonymous2_e__Union(Union):
        count: UInt16
        countPropertyIndex: UInt16
    class _Anonymous3_e__Union(Union):
        length: UInt16
        lengthPropertyIndex: UInt16
    class _Anonymous4_e__Union(Union):
        Reserved: UInt32
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            Tags: Annotated[UInt32, 28]
class EVENT_RECORD(Structure):
    EventHeader: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_HEADER
    BufferContext: win32more.Windows.Win32.System.Diagnostics.Etw.ETW_BUFFER_CONTEXT
    ExtendedDataCount: UInt16
    UserDataLength: UInt16
    ExtendedData: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_HEADER_EXTENDED_DATA_ITEM)
    UserData: VoidPtr
    UserContext: VoidPtr
class EVENT_TRACE(Structure):
    Header: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_HEADER
    InstanceId: UInt32
    ParentInstanceId: UInt32
    ParentGuid: Guid
    MofData: VoidPtr
    MofLength: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        ClientContext: UInt32
        BufferContext: win32more.Windows.Win32.System.Diagnostics.Etw.ETW_BUFFER_CONTEXT
EVENT_TRACE_CONTROL = UInt32
EVENT_TRACE_CONTROL_FLUSH: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_CONTROL = 3
EVENT_TRACE_CONTROL_QUERY: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_CONTROL = 0
EVENT_TRACE_CONTROL_STOP: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_CONTROL = 1
EVENT_TRACE_CONTROL_UPDATE: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_CONTROL = 2
EVENT_TRACE_FLAG = UInt32
EVENT_TRACE_FLAG_ALPC: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_FLAG = 1048576
EVENT_TRACE_FLAG_CSWITCH: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_FLAG = 16
EVENT_TRACE_FLAG_DBGPRINT: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_FLAG = 262144
EVENT_TRACE_FLAG_DISK_FILE_IO: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_FLAG = 512
EVENT_TRACE_FLAG_DISK_IO: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_FLAG = 256
EVENT_TRACE_FLAG_DISK_IO_INIT: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_FLAG = 1024
EVENT_TRACE_FLAG_DISPATCHER: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_FLAG = 2048
EVENT_TRACE_FLAG_DPC: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_FLAG = 32
EVENT_TRACE_FLAG_DRIVER: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_FLAG = 8388608
EVENT_TRACE_FLAG_FILE_IO: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_FLAG = 33554432
EVENT_TRACE_FLAG_FILE_IO_INIT: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_FLAG = 67108864
EVENT_TRACE_FLAG_IMAGE_LOAD: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_FLAG = 4
EVENT_TRACE_FLAG_INTERRUPT: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_FLAG = 64
EVENT_TRACE_FLAG_JOB: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_FLAG = 524288
EVENT_TRACE_FLAG_MEMORY_HARD_FAULTS: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_FLAG = 8192
EVENT_TRACE_FLAG_MEMORY_PAGE_FAULTS: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_FLAG = 4096
EVENT_TRACE_FLAG_NETWORK_TCPIP: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_FLAG = 65536
EVENT_TRACE_FLAG_NO_SYSCONFIG: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_FLAG = 268435456
EVENT_TRACE_FLAG_PROCESS: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_FLAG = 1
EVENT_TRACE_FLAG_PROCESS_COUNTERS: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_FLAG = 8
EVENT_TRACE_FLAG_PROFILE: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_FLAG = 16777216
EVENT_TRACE_FLAG_REGISTRY: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_FLAG = 131072
EVENT_TRACE_FLAG_SPLIT_IO: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_FLAG = 2097152
EVENT_TRACE_FLAG_SYSTEMCALL: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_FLAG = 128
EVENT_TRACE_FLAG_THREAD: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_FLAG = 2
EVENT_TRACE_FLAG_VAMAP: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_FLAG = 32768
EVENT_TRACE_FLAG_VIRTUAL_ALLOC: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_FLAG = 16384
class EVENT_TRACE_HEADER(Structure):
    Size: UInt16
    Anonymous1: _Anonymous1_e__Union
    Anonymous2: _Anonymous2_e__Union
    ThreadId: UInt32
    ProcessId: UInt32
    TimeStamp: Int64
    Anonymous3: _Anonymous3_e__Union
    Anonymous4: _Anonymous4_e__Union
    class _Anonymous1_e__Union(Union):
        FieldTypeFlags: UInt16
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            HeaderType: Byte
            MarkerFlags: Byte
    class _Anonymous2_e__Union(Union):
        Version: UInt32
        Class: _Class_e__Struct
        class _Class_e__Struct(Structure):
            Type: Byte
            Level: Byte
            Version: UInt16
    class _Anonymous3_e__Union(Union):
        Guid: Guid
        GuidPtr: UInt64
    class _Anonymous4_e__Union(Union):
        Anonymous1: _Anonymous1_e__Struct
        ProcessorTime: UInt64
        Anonymous2: _Anonymous2_e__Struct
        class _Anonymous1_e__Struct(Structure):
            KernelTime: UInt32
            UserTime: UInt32
        class _Anonymous2_e__Struct(Structure):
            ClientContext: UInt32
            Flags: UInt32
class EVENT_TRACE_LOGFILEA(Structure):
    LogFileName: win32more.Windows.Win32.Foundation.PSTR
    LoggerName: win32more.Windows.Win32.Foundation.PSTR
    CurrentTime: Int64
    BuffersRead: UInt32
    Anonymous1: _Anonymous1_e__Union
    CurrentEvent: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE
    LogfileHeader: win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_LOGFILE_HEADER
    BufferCallback: win32more.Windows.Win32.System.Diagnostics.Etw.PEVENT_TRACE_BUFFER_CALLBACKA
    BufferSize: UInt32
    Filled: UInt32
    EventsLost: UInt32
    Anonymous2: _Anonymous2_e__Union
    IsKernelTrace: UInt32
    Context: VoidPtr
    class _Anonymous1_e__Union(Union):
        LogFileMode: UInt32
        ProcessTraceMode: UInt32
    class _Anonymous2_e__Union(Union):
        EventCallback: win32more.Windows.Win32.System.Diagnostics.Etw.PEVENT_CALLBACK
        EventRecordCallback: win32more.Windows.Win32.System.Diagnostics.Etw.PEVENT_RECORD_CALLBACK
class EVENT_TRACE_LOGFILEW(Structure):
    LogFileName: win32more.Windows.Win32.Foundation.PWSTR
    LoggerName: win32more.Windows.Win32.Foundation.PWSTR
    CurrentTime: Int64
    BuffersRead: UInt32
    Anonymous1: _Anonymous1_e__Union
    CurrentEvent: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE
    LogfileHeader: win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_LOGFILE_HEADER
    BufferCallback: win32more.Windows.Win32.System.Diagnostics.Etw.PEVENT_TRACE_BUFFER_CALLBACKW
    BufferSize: UInt32
    Filled: UInt32
    EventsLost: UInt32
    Anonymous2: _Anonymous2_e__Union
    IsKernelTrace: UInt32
    Context: VoidPtr
    class _Anonymous1_e__Union(Union):
        LogFileMode: UInt32
        ProcessTraceMode: UInt32
    class _Anonymous2_e__Union(Union):
        EventCallback: win32more.Windows.Win32.System.Diagnostics.Etw.PEVENT_CALLBACK
        EventRecordCallback: win32more.Windows.Win32.System.Diagnostics.Etw.PEVENT_RECORD_CALLBACK
EVENT_TRACE_LOGFILE = UnicodeAlias('EVENT_TRACE_LOGFILEW')
class EVENT_TRACE_PROPERTIES(Structure):
    Wnode: win32more.Windows.Win32.System.Diagnostics.Etw.WNODE_HEADER
    BufferSize: UInt32
    MinimumBuffers: UInt32
    MaximumBuffers: UInt32
    MaximumFileSize: UInt32
    LogFileMode: UInt32
    FlushTimer: UInt32
    EnableFlags: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_FLAG
    Anonymous: _Anonymous_e__Union
    NumberOfBuffers: UInt32
    FreeBuffers: UInt32
    EventsLost: UInt32
    BuffersWritten: UInt32
    LogBuffersLost: UInt32
    RealTimeBuffersLost: UInt32
    LoggerThreadId: win32more.Windows.Win32.Foundation.HANDLE
    LogFileNameOffset: UInt32
    LoggerNameOffset: UInt32
    class _Anonymous_e__Union(Union):
        AgeLimit: Int32
        FlushThreshold: Int32
class EVENT_TRACE_PROPERTIES_V2(Structure):
    Wnode: win32more.Windows.Win32.System.Diagnostics.Etw.WNODE_HEADER
    BufferSize: UInt32
    MinimumBuffers: UInt32
    MaximumBuffers: UInt32
    MaximumFileSize: UInt32
    LogFileMode: UInt32
    FlushTimer: UInt32
    EnableFlags: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_FLAG
    Anonymous1: _Anonymous1_e__Union
    NumberOfBuffers: UInt32
    FreeBuffers: UInt32
    EventsLost: UInt32
    BuffersWritten: UInt32
    LogBuffersLost: UInt32
    RealTimeBuffersLost: UInt32
    LoggerThreadId: win32more.Windows.Win32.Foundation.HANDLE
    LogFileNameOffset: UInt32
    LoggerNameOffset: UInt32
    Anonymous2: _Anonymous2_e__Union
    FilterDescCount: UInt32
    FilterDesc: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_FILTER_DESCRIPTOR)
    Anonymous3: _Anonymous3_e__Union
    class _Anonymous1_e__Union(Union):
        AgeLimit: Int32
        FlushThreshold: Int32
    class _Anonymous2_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        V2Control: UInt32
        class _Anonymous_e__Struct(Structure):
            VersionNumber: Annotated[UInt32, 8]
    class _Anonymous3_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        V2Options: UInt64
        class _Anonymous_e__Struct(Structure):
            Wow: Annotated[UInt32, 1]
            QpcDeltaTracking: Annotated[UInt32, 1]
            LargeMdlPages: Annotated[UInt32, 1]
            ExcludeKernelStack: Annotated[UInt32, 1]
class ITraceEvent(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8cc97f40-9028-4ff3-9b62-7d1f79ca7bcb}')
    @commethod(3)
    def Clone(self, NewEvent: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.ITraceEvent)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetUserContext(self, UserContext: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetEventRecord(self, EventRecord: POINTER(POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_RECORD))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetPayload(self, Payload: POINTER(Byte), PayloadSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetEventDescriptor(self, EventDescriptor: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_DESCRIPTOR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetProcessId(self, ProcessId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetProcessorIndex(self, ProcessorIndex: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetThreadId(self, ThreadId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetThreadTimes(self, KernelTime: UInt32, UserTime: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetActivityId(self, ActivityId: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetTimeStamp(self, TimeStamp: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetProviderId(self, ProviderId: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITraceEventCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3ed25501-593f-43e9-8f38-3ab46f5a4a52}')
    @commethod(3)
    def OnBeginProcessTrace(self, HeaderEvent: win32more.Windows.Win32.System.Diagnostics.Etw.ITraceEvent, Relogger: win32more.Windows.Win32.System.Diagnostics.Etw.ITraceRelogger) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnFinalizeProcessTrace(self, Relogger: win32more.Windows.Win32.System.Diagnostics.Etw.ITraceRelogger) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnEvent(self, Event: win32more.Windows.Win32.System.Diagnostics.Etw.ITraceEvent, Relogger: win32more.Windows.Win32.System.Diagnostics.Etw.ITraceRelogger) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITraceRelogger(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f754ad43-3bcc-4286-8009-9c5da214e84e}')
    @commethod(3)
    def AddLogfileTraceStream(self, LogfileName: win32more.Windows.Win32.Foundation.BSTR, UserContext: VoidPtr, TraceHandle: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.RELOGSTREAM_HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddRealtimeTraceStream(self, LoggerName: win32more.Windows.Win32.Foundation.BSTR, UserContext: VoidPtr, TraceHandle: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.RELOGSTREAM_HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RegisterCallback(self, Callback: win32more.Windows.Win32.System.Diagnostics.Etw.ITraceEventCallback) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Inject(self, Event: win32more.Windows.Win32.System.Diagnostics.Etw.ITraceEvent) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateEventInstance(self, TraceHandle: win32more.Windows.Win32.System.Diagnostics.Etw.RELOGSTREAM_HANDLE, Flags: UInt32, Event: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.ITraceEvent)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ProcessTrace(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetOutputFilename(self, LogfileName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetCompressionMode(self, CompressionMode: win32more.Windows.Win32.Foundation.BOOLEAN) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Cancel(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
MAP_FLAGS = Int32
EVENTMAP_INFO_FLAG_MANIFEST_VALUEMAP: win32more.Windows.Win32.System.Diagnostics.Etw.MAP_FLAGS = 1
EVENTMAP_INFO_FLAG_MANIFEST_BITMAP: win32more.Windows.Win32.System.Diagnostics.Etw.MAP_FLAGS = 2
EVENTMAP_INFO_FLAG_MANIFEST_PATTERNMAP: win32more.Windows.Win32.System.Diagnostics.Etw.MAP_FLAGS = 4
EVENTMAP_INFO_FLAG_WBEM_VALUEMAP: win32more.Windows.Win32.System.Diagnostics.Etw.MAP_FLAGS = 8
EVENTMAP_INFO_FLAG_WBEM_BITMAP: win32more.Windows.Win32.System.Diagnostics.Etw.MAP_FLAGS = 16
EVENTMAP_INFO_FLAG_WBEM_FLAG: win32more.Windows.Win32.System.Diagnostics.Etw.MAP_FLAGS = 32
EVENTMAP_INFO_FLAG_WBEM_NO_MAP: win32more.Windows.Win32.System.Diagnostics.Etw.MAP_FLAGS = 64
MAP_VALUETYPE = Int32
EVENTMAP_ENTRY_VALUETYPE_ULONG: win32more.Windows.Win32.System.Diagnostics.Etw.MAP_VALUETYPE = 0
EVENTMAP_ENTRY_VALUETYPE_STRING: win32more.Windows.Win32.System.Diagnostics.Etw.MAP_VALUETYPE = 1
class MOF_FIELD(Structure):
    DataPtr: UInt64
    Length: UInt32
    DataType: UInt32
class OFFSETINSTANCEDATAANDLENGTH(Structure):
    OffsetInstanceData: UInt32
    LengthInstanceData: UInt32
class PAYLOAD_FILTER_PREDICATE(Structure):
    FieldName: win32more.Windows.Win32.Foundation.PWSTR
    CompareOp: UInt16
    Value: win32more.Windows.Win32.Foundation.PWSTR
PAYLOAD_OPERATOR = Int32
PAYLOADFIELD_EQ: win32more.Windows.Win32.System.Diagnostics.Etw.PAYLOAD_OPERATOR = 0
PAYLOADFIELD_NE: win32more.Windows.Win32.System.Diagnostics.Etw.PAYLOAD_OPERATOR = 1
PAYLOADFIELD_LE: win32more.Windows.Win32.System.Diagnostics.Etw.PAYLOAD_OPERATOR = 2
PAYLOADFIELD_GT: win32more.Windows.Win32.System.Diagnostics.Etw.PAYLOAD_OPERATOR = 3
PAYLOADFIELD_LT: win32more.Windows.Win32.System.Diagnostics.Etw.PAYLOAD_OPERATOR = 4
PAYLOADFIELD_GE: win32more.Windows.Win32.System.Diagnostics.Etw.PAYLOAD_OPERATOR = 5
PAYLOADFIELD_BETWEEN: win32more.Windows.Win32.System.Diagnostics.Etw.PAYLOAD_OPERATOR = 6
PAYLOADFIELD_NOTBETWEEN: win32more.Windows.Win32.System.Diagnostics.Etw.PAYLOAD_OPERATOR = 7
PAYLOADFIELD_MODULO: win32more.Windows.Win32.System.Diagnostics.Etw.PAYLOAD_OPERATOR = 8
PAYLOADFIELD_CONTAINS: win32more.Windows.Win32.System.Diagnostics.Etw.PAYLOAD_OPERATOR = 20
PAYLOADFIELD_DOESNTCONTAIN: win32more.Windows.Win32.System.Diagnostics.Etw.PAYLOAD_OPERATOR = 21
PAYLOADFIELD_IS: win32more.Windows.Win32.System.Diagnostics.Etw.PAYLOAD_OPERATOR = 30
PAYLOADFIELD_ISNOT: win32more.Windows.Win32.System.Diagnostics.Etw.PAYLOAD_OPERATOR = 31
PAYLOADFIELD_INVALID: win32more.Windows.Win32.System.Diagnostics.Etw.PAYLOAD_OPERATOR = 32
@winfunctype_pointer
def PENABLECALLBACK(SourceId: POINTER(Guid), IsEnabled: win32more.Windows.Win32.System.Diagnostics.Etw.ENABLECALLBACK_ENABLED_STATE, Level: Byte, MatchAnyKeyword: UInt64, MatchAllKeyword: UInt64, FilterData: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_FILTER_DESCRIPTOR), CallbackContext: VoidPtr) -> Void: ...
@winfunctype_pointer
def PETW_BUFFER_CALLBACK(Buffer: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.ETW_BUFFER_HEADER), BufferSize: UInt32, ConsumerInfo: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.ETW_BUFFER_CALLBACK_INFORMATION), CallbackContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PETW_BUFFER_COMPLETION_CALLBACK(Buffer: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.ETW_BUFFER_HEADER), CallbackContext: VoidPtr) -> Void: ...
@winfunctype_pointer
def PEVENT_CALLBACK(pEvent: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE)) -> Void: ...
@winfunctype_pointer
def PEVENT_RECORD_CALLBACK(EventRecord: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_RECORD)) -> Void: ...
@winfunctype_pointer
def PEVENT_TRACE_BUFFER_CALLBACKA(Logfile: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_LOGFILEA)) -> UInt32: ...
@winfunctype_pointer
def PEVENT_TRACE_BUFFER_CALLBACKW(Logfile: POINTER(win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_LOGFILEW)) -> UInt32: ...
PEVENT_TRACE_BUFFER_CALLBACK = UnicodeAlias('PEVENT_TRACE_BUFFER_CALLBACKW')
class PROCESSTRACE_HANDLE(Structure):
    Value: UInt64
class PROFILE_SOURCE_INFO(Structure):
    NextEntryOffset: UInt32
    Source: UInt32
    MinInterval: UInt32
    MaxInterval: UInt32
    Reserved: UInt64
    Description: Char * 1
class PROPERTY_DATA_DESCRIPTOR(Structure):
    PropertyName: UInt64
    ArrayIndex: UInt32
    Reserved: UInt32
PROPERTY_FLAGS = Int32
PropertyStruct: win32more.Windows.Win32.System.Diagnostics.Etw.PROPERTY_FLAGS = 1
PropertyParamLength: win32more.Windows.Win32.System.Diagnostics.Etw.PROPERTY_FLAGS = 2
PropertyParamCount: win32more.Windows.Win32.System.Diagnostics.Etw.PROPERTY_FLAGS = 4
PropertyWBEMXmlFragment: win32more.Windows.Win32.System.Diagnostics.Etw.PROPERTY_FLAGS = 8
PropertyParamFixedLength: win32more.Windows.Win32.System.Diagnostics.Etw.PROPERTY_FLAGS = 16
PropertyParamFixedCount: win32more.Windows.Win32.System.Diagnostics.Etw.PROPERTY_FLAGS = 32
PropertyHasTags: win32more.Windows.Win32.System.Diagnostics.Etw.PROPERTY_FLAGS = 64
PropertyHasCustomSchema: win32more.Windows.Win32.System.Diagnostics.Etw.PROPERTY_FLAGS = 128
class PROVIDER_ENUMERATION_INFO(Structure):
    NumberOfProviders: UInt32
    Reserved: UInt32
    TraceProviderInfoArray: win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_PROVIDER_INFO * 1
class PROVIDER_EVENT_INFO(Structure):
    NumberOfEvents: UInt32
    Reserved: UInt32
    EventDescriptorsArray: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_DESCRIPTOR * 1
class PROVIDER_FIELD_INFO(Structure):
    NameOffset: UInt32
    DescriptionOffset: UInt32
    Value: UInt64
class PROVIDER_FIELD_INFOARRAY(Structure):
    NumberOfElements: UInt32
    FieldType: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_FIELD_TYPE
    FieldInfoArray: win32more.Windows.Win32.System.Diagnostics.Etw.PROVIDER_FIELD_INFO * 1
class PROVIDER_FILTER_INFO(Structure):
    Id: Byte
    Version: Byte
    MessageOffset: UInt32
    Reserved: UInt32
    PropertyCount: UInt32
    EventPropertyInfoArray: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_PROPERTY_INFO * 1
REGHANDLE = Int64
class RELOGSTREAM_HANDLE(Structure):
    Value: UInt64
class TDH_CONTEXT(Structure):
    ParameterValue: UInt64
    ParameterType: win32more.Windows.Win32.System.Diagnostics.Etw.TDH_CONTEXT_TYPE
    ParameterSize: UInt32
TDH_CONTEXT_TYPE = Int32
TDH_CONTEXT_WPP_TMFFILE: win32more.Windows.Win32.System.Diagnostics.Etw.TDH_CONTEXT_TYPE = 0
TDH_CONTEXT_WPP_TMFSEARCHPATH: win32more.Windows.Win32.System.Diagnostics.Etw.TDH_CONTEXT_TYPE = 1
TDH_CONTEXT_WPP_GMT: win32more.Windows.Win32.System.Diagnostics.Etw.TDH_CONTEXT_TYPE = 2
TDH_CONTEXT_POINTERSIZE: win32more.Windows.Win32.System.Diagnostics.Etw.TDH_CONTEXT_TYPE = 3
TDH_CONTEXT_PDB_PATH: win32more.Windows.Win32.System.Diagnostics.Etw.TDH_CONTEXT_TYPE = 4
TDH_CONTEXT_MAXIMUM: win32more.Windows.Win32.System.Diagnostics.Etw.TDH_CONTEXT_TYPE = 5
TDH_HANDLE = IntPtr
TEMPLATE_FLAGS = Int32
TEMPLATE_EVENT_DATA: win32more.Windows.Win32.System.Diagnostics.Etw.TEMPLATE_FLAGS = 1
TEMPLATE_USER_DATA: win32more.Windows.Win32.System.Diagnostics.Etw.TEMPLATE_FLAGS = 2
TEMPLATE_CONTROL_GUID: win32more.Windows.Win32.System.Diagnostics.Etw.TEMPLATE_FLAGS = 4
class TRACE_ENABLE_INFO(Structure):
    IsEnabled: UInt32
    Level: Byte
    Reserved1: Byte
    LoggerId: UInt16
    EnableProperty: UInt32
    Reserved2: UInt32
    MatchAnyKeyword: UInt64
    MatchAllKeyword: UInt64
class TRACE_EVENT_INFO(Structure):
    ProviderGuid: Guid
    EventGuid: Guid
    EventDescriptor: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_DESCRIPTOR
    DecodingSource: win32more.Windows.Win32.System.Diagnostics.Etw.DECODING_SOURCE
    ProviderNameOffset: UInt32
    LevelNameOffset: UInt32
    ChannelNameOffset: UInt32
    KeywordsNameOffset: UInt32
    TaskNameOffset: UInt32
    OpcodeNameOffset: UInt32
    EventMessageOffset: UInt32
    ProviderMessageOffset: UInt32
    BinaryXMLOffset: UInt32
    BinaryXMLSize: UInt32
    Anonymous1: _Anonymous1_e__Union
    Anonymous2: _Anonymous2_e__Union
    PropertyCount: UInt32
    TopLevelPropertyCount: UInt32
    Anonymous3: _Anonymous3_e__Union
    EventPropertyInfoArray: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_PROPERTY_INFO * 1
    class _Anonymous1_e__Union(Union):
        EventNameOffset: UInt32
        ActivityIDNameOffset: UInt32
    class _Anonymous2_e__Union(Union):
        EventAttributesOffset: UInt32
        RelatedActivityIDNameOffset: UInt32
    class _Anonymous3_e__Union(Union):
        Flags: win32more.Windows.Win32.System.Diagnostics.Etw.TEMPLATE_FLAGS
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            Reserved: Annotated[UInt32, 4]
            Tags: Annotated[UInt32, 28]
class TRACE_GUID_INFO(Structure):
    InstanceCount: UInt32
    Reserved: UInt32
class TRACE_GUID_PROPERTIES(Structure):
    Guid: Guid
    GuidType: UInt32
    LoggerId: UInt32
    EnableLevel: UInt32
    EnableFlags: UInt32
    IsEnable: win32more.Windows.Win32.Foundation.BOOLEAN
class TRACE_GUID_REGISTRATION(Structure):
    Guid: POINTER(Guid)
    RegHandle: win32more.Windows.Win32.Foundation.HANDLE
class TRACE_LOGFILE_HEADER(Structure):
    BufferSize: UInt32
    Anonymous1: _Anonymous1_e__Union
    ProviderVersion: UInt32
    NumberOfProcessors: UInt32
    EndTime: Int64
    TimerResolution: UInt32
    MaximumFileSize: UInt32
    LogFileMode: UInt32
    BuffersWritten: UInt32
    Anonymous2: _Anonymous2_e__Union
    LoggerName: win32more.Windows.Win32.Foundation.PWSTR
    LogFileName: win32more.Windows.Win32.Foundation.PWSTR
    TimeZone: win32more.Windows.Win32.System.Time.TIME_ZONE_INFORMATION
    BootTime: Int64
    PerfFreq: Int64
    StartTime: Int64
    ReservedFlags: UInt32
    BuffersLost: UInt32
    class _Anonymous1_e__Union(Union):
        Version: UInt32
        VersionDetail: _VersionDetail_e__Struct
        class _VersionDetail_e__Struct(Structure):
            MajorVersion: Byte
            MinorVersion: Byte
            SubVersion: Byte
            SubMinorVersion: Byte
    class _Anonymous2_e__Union(Union):
        LogInstanceGuid: Guid
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            StartBuffers: UInt32
            PointerSize: UInt32
            EventsLost: UInt32
            CpuSpeedInMHz: UInt32
class TRACE_LOGFILE_HEADER32(Structure):
    BufferSize: UInt32
    Anonymous1: _Anonymous1_e__Union
    ProviderVersion: UInt32
    NumberOfProcessors: UInt32
    EndTime: Int64
    TimerResolution: UInt32
    MaximumFileSize: UInt32
    LogFileMode: UInt32
    BuffersWritten: UInt32
    Anonymous2: _Anonymous2_e__Union
    LoggerName: UInt32
    LogFileName: UInt32
    TimeZone: win32more.Windows.Win32.System.Time.TIME_ZONE_INFORMATION
    BootTime: Int64
    PerfFreq: Int64
    StartTime: Int64
    ReservedFlags: UInt32
    BuffersLost: UInt32
    class _Anonymous1_e__Union(Union):
        Version: UInt32
        VersionDetail: _VersionDetail_e__Struct
        class _VersionDetail_e__Struct(Structure):
            MajorVersion: Byte
            MinorVersion: Byte
            SubVersion: Byte
            SubMinorVersion: Byte
    class _Anonymous2_e__Union(Union):
        LogInstanceGuid: Guid
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            StartBuffers: UInt32
            PointerSize: UInt32
            EventsLost: UInt32
            CpuSpeedInMHz: UInt32
class TRACE_LOGFILE_HEADER64(Structure):
    BufferSize: UInt32
    Anonymous1: _Anonymous1_e__Union
    ProviderVersion: UInt32
    NumberOfProcessors: UInt32
    EndTime: Int64
    TimerResolution: UInt32
    MaximumFileSize: UInt32
    LogFileMode: UInt32
    BuffersWritten: UInt32
    Anonymous2: _Anonymous2_e__Union
    LoggerName: UInt64
    LogFileName: UInt64
    TimeZone: win32more.Windows.Win32.System.Time.TIME_ZONE_INFORMATION
    BootTime: Int64
    PerfFreq: Int64
    StartTime: Int64
    ReservedFlags: UInt32
    BuffersLost: UInt32
    class _Anonymous1_e__Union(Union):
        Version: UInt32
        VersionDetail: _VersionDetail_e__Struct
        class _VersionDetail_e__Struct(Structure):
            MajorVersion: Byte
            MinorVersion: Byte
            SubVersion: Byte
            SubMinorVersion: Byte
    class _Anonymous2_e__Union(Union):
        LogInstanceGuid: Guid
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            StartBuffers: UInt32
            PointerSize: UInt32
            EventsLost: UInt32
            CpuSpeedInMHz: UInt32
TRACE_MESSAGE_FLAGS = UInt32
TRACE_MESSAGE_COMPONENTID: win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_MESSAGE_FLAGS = 4
TRACE_MESSAGE_GUID: win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_MESSAGE_FLAGS = 2
TRACE_MESSAGE_SEQUENCE: win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_MESSAGE_FLAGS = 1
TRACE_MESSAGE_SYSTEMINFO: win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_MESSAGE_FLAGS = 32
TRACE_MESSAGE_TIMESTAMP: win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_MESSAGE_FLAGS = 8
class TRACE_PERIODIC_CAPTURE_STATE_INFO(Structure):
    CaptureStateFrequencyInSeconds: UInt32
    ProviderCount: UInt16
    Reserved: UInt16
class TRACE_PROFILE_INTERVAL(Structure):
    Source: UInt32
    Interval: UInt32
class TRACE_PROVIDER_INFO(Structure):
    ProviderGuid: Guid
    SchemaSource: UInt32
    ProviderNameOffset: UInt32
class TRACE_PROVIDER_INSTANCE_INFO(Structure):
    NextOffset: UInt32
    EnableCount: UInt32
    Pid: UInt32
    Flags: UInt32
TRACE_QUERY_INFO_CLASS = Int32
TraceGuidQueryList: win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_QUERY_INFO_CLASS = 0
TraceGuidQueryInfo: win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_QUERY_INFO_CLASS = 1
TraceGuidQueryProcess: win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_QUERY_INFO_CLASS = 2
TraceStackTracingInfo: win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_QUERY_INFO_CLASS = 3
TraceSystemTraceEnableFlagsInfo: win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_QUERY_INFO_CLASS = 4
TraceSampledProfileIntervalInfo: win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_QUERY_INFO_CLASS = 5
TraceProfileSourceConfigInfo: win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_QUERY_INFO_CLASS = 6
TraceProfileSourceListInfo: win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_QUERY_INFO_CLASS = 7
TracePmcEventListInfo: win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_QUERY_INFO_CLASS = 8
TracePmcCounterListInfo: win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_QUERY_INFO_CLASS = 9
TraceSetDisallowList: win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_QUERY_INFO_CLASS = 10
TraceVersionInfo: win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_QUERY_INFO_CLASS = 11
TraceGroupQueryList: win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_QUERY_INFO_CLASS = 12
TraceGroupQueryInfo: win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_QUERY_INFO_CLASS = 13
TraceDisallowListQuery: win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_QUERY_INFO_CLASS = 14
TraceInfoReserved15: win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_QUERY_INFO_CLASS = 15
TracePeriodicCaptureStateListInfo: win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_QUERY_INFO_CLASS = 16
TracePeriodicCaptureStateInfo: win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_QUERY_INFO_CLASS = 17
TraceProviderBinaryTracking: win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_QUERY_INFO_CLASS = 18
TraceMaxLoggersQuery: win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_QUERY_INFO_CLASS = 19
TraceLbrConfigurationInfo: win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_QUERY_INFO_CLASS = 20
TraceLbrEventListInfo: win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_QUERY_INFO_CLASS = 21
TraceMaxPmcCounterQuery: win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_QUERY_INFO_CLASS = 22
TraceStreamCount: win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_QUERY_INFO_CLASS = 23
TraceStackCachingInfo: win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_QUERY_INFO_CLASS = 24
TracePmcCounterOwners: win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_QUERY_INFO_CLASS = 25
TraceUnifiedStackCachingInfo: win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_QUERY_INFO_CLASS = 26
TracePmcSessionInformation: win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_QUERY_INFO_CLASS = 27
MaxTraceSetInfoClass: win32more.Windows.Win32.System.Diagnostics.Etw.TRACE_QUERY_INFO_CLASS = 28
class TRACE_STACK_CACHING_INFO(Structure):
    Enabled: win32more.Windows.Win32.Foundation.BOOLEAN
    CacheSize: UInt32
    BucketCount: UInt32
class TRACE_VERSION_INFO(Structure):
    EtwTraceProcessingVersion: UInt32
    Reserved: UInt32
@winfunctype_pointer
def WMIDPREQUEST(RequestCode: win32more.Windows.Win32.System.Diagnostics.Etw.WMIDPREQUESTCODE, RequestContext: VoidPtr, BufferSize: POINTER(UInt32), Buffer: VoidPtr) -> UInt32: ...
WMIDPREQUESTCODE = Int32
WMI_GET_ALL_DATA: win32more.Windows.Win32.System.Diagnostics.Etw.WMIDPREQUESTCODE = 0
WMI_GET_SINGLE_INSTANCE: win32more.Windows.Win32.System.Diagnostics.Etw.WMIDPREQUESTCODE = 1
WMI_SET_SINGLE_INSTANCE: win32more.Windows.Win32.System.Diagnostics.Etw.WMIDPREQUESTCODE = 2
WMI_SET_SINGLE_ITEM: win32more.Windows.Win32.System.Diagnostics.Etw.WMIDPREQUESTCODE = 3
WMI_ENABLE_EVENTS: win32more.Windows.Win32.System.Diagnostics.Etw.WMIDPREQUESTCODE = 4
WMI_DISABLE_EVENTS: win32more.Windows.Win32.System.Diagnostics.Etw.WMIDPREQUESTCODE = 5
WMI_ENABLE_COLLECTION: win32more.Windows.Win32.System.Diagnostics.Etw.WMIDPREQUESTCODE = 6
WMI_DISABLE_COLLECTION: win32more.Windows.Win32.System.Diagnostics.Etw.WMIDPREQUESTCODE = 7
WMI_REGINFO: win32more.Windows.Win32.System.Diagnostics.Etw.WMIDPREQUESTCODE = 8
WMI_EXECUTE_METHOD: win32more.Windows.Win32.System.Diagnostics.Etw.WMIDPREQUESTCODE = 9
WMI_CAPTURE_STATE: win32more.Windows.Win32.System.Diagnostics.Etw.WMIDPREQUESTCODE = 10
class WMIREGGUIDW(Structure):
    Guid: Guid
    Flags: UInt32
    InstanceCount: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        InstanceNameList: UInt32
        BaseNameOffset: UInt32
        Pdo: UIntPtr
        InstanceInfo: UIntPtr
class WMIREGINFOW(Structure):
    BufferSize: UInt32
    NextWmiRegInfo: UInt32
    RegistryPath: UInt32
    MofResourceName: UInt32
    GuidCount: UInt32
    WmiRegGuid: win32more.Windows.Win32.System.Diagnostics.Etw.WMIREGGUIDW * 1
class WNODE_ALL_DATA(Structure):
    WnodeHeader: win32more.Windows.Win32.System.Diagnostics.Etw.WNODE_HEADER
    DataBlockOffset: UInt32
    InstanceCount: UInt32
    OffsetInstanceNameOffsets: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        FixedInstanceSize: UInt32
        OffsetInstanceDataAndLength: win32more.Windows.Win32.System.Diagnostics.Etw.OFFSETINSTANCEDATAANDLENGTH * 1
class WNODE_EVENT_ITEM(Structure):
    WnodeHeader: win32more.Windows.Win32.System.Diagnostics.Etw.WNODE_HEADER
class WNODE_EVENT_REFERENCE(Structure):
    WnodeHeader: win32more.Windows.Win32.System.Diagnostics.Etw.WNODE_HEADER
    TargetGuid: Guid
    TargetDataBlockSize: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        TargetInstanceIndex: UInt32
        TargetInstanceName: Char * 1
class WNODE_HEADER(Structure):
    BufferSize: UInt32
    ProviderId: UInt32
    Anonymous1: _Anonymous1_e__Union
    Anonymous2: _Anonymous2_e__Union
    Guid: Guid
    ClientContext: UInt32
    Flags: UInt32
    class _Anonymous1_e__Union(Union):
        HistoricalContext: UInt64
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            Version: UInt32
            Linkage: UInt32
    class _Anonymous2_e__Union(Union):
        CountLost: UInt32
        KernelHandle: win32more.Windows.Win32.Foundation.HANDLE
        TimeStamp: Int64
class WNODE_METHOD_ITEM(Structure):
    WnodeHeader: win32more.Windows.Win32.System.Diagnostics.Etw.WNODE_HEADER
    OffsetInstanceName: UInt32
    InstanceIndex: UInt32
    MethodId: UInt32
    DataBlockOffset: UInt32
    SizeDataBlock: UInt32
    VariableData: Byte * 1
class WNODE_SINGLE_INSTANCE(Structure):
    WnodeHeader: win32more.Windows.Win32.System.Diagnostics.Etw.WNODE_HEADER
    OffsetInstanceName: UInt32
    InstanceIndex: UInt32
    DataBlockOffset: UInt32
    SizeDataBlock: UInt32
    VariableData: Byte * 1
class WNODE_SINGLE_ITEM(Structure):
    WnodeHeader: win32more.Windows.Win32.System.Diagnostics.Etw.WNODE_HEADER
    OffsetInstanceName: UInt32
    InstanceIndex: UInt32
    ItemId: UInt32
    DataBlockOffset: UInt32
    SizeDataItem: UInt32
    VariableData: Byte * 1
class WNODE_TOO_SMALL(Structure):
    WnodeHeader: win32more.Windows.Win32.System.Diagnostics.Etw.WNODE_HEADER
    SizeNeeded: UInt32
_TDH_IN_TYPE = Int32
TDH_INTYPE_NULL: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_IN_TYPE = 0
TDH_INTYPE_UNICODESTRING: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_IN_TYPE = 1
TDH_INTYPE_ANSISTRING: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_IN_TYPE = 2
TDH_INTYPE_INT8: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_IN_TYPE = 3
TDH_INTYPE_UINT8: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_IN_TYPE = 4
TDH_INTYPE_INT16: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_IN_TYPE = 5
TDH_INTYPE_UINT16: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_IN_TYPE = 6
TDH_INTYPE_INT32: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_IN_TYPE = 7
TDH_INTYPE_UINT32: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_IN_TYPE = 8
TDH_INTYPE_INT64: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_IN_TYPE = 9
TDH_INTYPE_UINT64: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_IN_TYPE = 10
TDH_INTYPE_FLOAT: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_IN_TYPE = 11
TDH_INTYPE_DOUBLE: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_IN_TYPE = 12
TDH_INTYPE_BOOLEAN: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_IN_TYPE = 13
TDH_INTYPE_BINARY: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_IN_TYPE = 14
TDH_INTYPE_GUID: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_IN_TYPE = 15
TDH_INTYPE_POINTER: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_IN_TYPE = 16
TDH_INTYPE_FILETIME: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_IN_TYPE = 17
TDH_INTYPE_SYSTEMTIME: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_IN_TYPE = 18
TDH_INTYPE_SID: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_IN_TYPE = 19
TDH_INTYPE_HEXINT32: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_IN_TYPE = 20
TDH_INTYPE_HEXINT64: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_IN_TYPE = 21
TDH_INTYPE_MANIFEST_COUNTEDSTRING: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_IN_TYPE = 22
TDH_INTYPE_MANIFEST_COUNTEDANSISTRING: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_IN_TYPE = 23
TDH_INTYPE_RESERVED24: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_IN_TYPE = 24
TDH_INTYPE_MANIFEST_COUNTEDBINARY: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_IN_TYPE = 25
TDH_INTYPE_COUNTEDSTRING: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_IN_TYPE = 300
TDH_INTYPE_COUNTEDANSISTRING: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_IN_TYPE = 301
TDH_INTYPE_REVERSEDCOUNTEDSTRING: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_IN_TYPE = 302
TDH_INTYPE_REVERSEDCOUNTEDANSISTRING: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_IN_TYPE = 303
TDH_INTYPE_NONNULLTERMINATEDSTRING: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_IN_TYPE = 304
TDH_INTYPE_NONNULLTERMINATEDANSISTRING: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_IN_TYPE = 305
TDH_INTYPE_UNICODECHAR: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_IN_TYPE = 306
TDH_INTYPE_ANSICHAR: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_IN_TYPE = 307
TDH_INTYPE_SIZET: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_IN_TYPE = 308
TDH_INTYPE_HEXDUMP: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_IN_TYPE = 309
TDH_INTYPE_WBEMSID: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_IN_TYPE = 310
_TDH_OUT_TYPE = Int32
TDH_OUTTYPE_NULL: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_OUT_TYPE = 0
TDH_OUTTYPE_STRING: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_OUT_TYPE = 1
TDH_OUTTYPE_DATETIME: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_OUT_TYPE = 2
TDH_OUTTYPE_BYTE: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_OUT_TYPE = 3
TDH_OUTTYPE_UNSIGNEDBYTE: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_OUT_TYPE = 4
TDH_OUTTYPE_SHORT: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_OUT_TYPE = 5
TDH_OUTTYPE_UNSIGNEDSHORT: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_OUT_TYPE = 6
TDH_OUTTYPE_INT: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_OUT_TYPE = 7
TDH_OUTTYPE_UNSIGNEDINT: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_OUT_TYPE = 8
TDH_OUTTYPE_LONG: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_OUT_TYPE = 9
TDH_OUTTYPE_UNSIGNEDLONG: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_OUT_TYPE = 10
TDH_OUTTYPE_FLOAT: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_OUT_TYPE = 11
TDH_OUTTYPE_DOUBLE: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_OUT_TYPE = 12
TDH_OUTTYPE_BOOLEAN: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_OUT_TYPE = 13
TDH_OUTTYPE_GUID: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_OUT_TYPE = 14
TDH_OUTTYPE_HEXBINARY: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_OUT_TYPE = 15
TDH_OUTTYPE_HEXINT8: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_OUT_TYPE = 16
TDH_OUTTYPE_HEXINT16: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_OUT_TYPE = 17
TDH_OUTTYPE_HEXINT32: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_OUT_TYPE = 18
TDH_OUTTYPE_HEXINT64: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_OUT_TYPE = 19
TDH_OUTTYPE_PID: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_OUT_TYPE = 20
TDH_OUTTYPE_TID: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_OUT_TYPE = 21
TDH_OUTTYPE_PORT: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_OUT_TYPE = 22
TDH_OUTTYPE_IPV4: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_OUT_TYPE = 23
TDH_OUTTYPE_IPV6: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_OUT_TYPE = 24
TDH_OUTTYPE_SOCKETADDRESS: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_OUT_TYPE = 25
TDH_OUTTYPE_CIMDATETIME: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_OUT_TYPE = 26
TDH_OUTTYPE_ETWTIME: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_OUT_TYPE = 27
TDH_OUTTYPE_XML: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_OUT_TYPE = 28
TDH_OUTTYPE_ERRORCODE: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_OUT_TYPE = 29
TDH_OUTTYPE_WIN32ERROR: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_OUT_TYPE = 30
TDH_OUTTYPE_NTSTATUS: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_OUT_TYPE = 31
TDH_OUTTYPE_HRESULT: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_OUT_TYPE = 32
TDH_OUTTYPE_CULTURE_INSENSITIVE_DATETIME: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_OUT_TYPE = 33
TDH_OUTTYPE_JSON: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_OUT_TYPE = 34
TDH_OUTTYPE_UTF8: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_OUT_TYPE = 35
TDH_OUTTYPE_PKCS7_WITH_TYPE_INFO: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_OUT_TYPE = 36
TDH_OUTTYPE_CODE_POINTER: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_OUT_TYPE = 37
TDH_OUTTYPE_DATETIME_UTC: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_OUT_TYPE = 38
TDH_OUTTYPE_REDUCEDSTRING: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_OUT_TYPE = 300
TDH_OUTTYPE_NOPRINT: win32more.Windows.Win32.System.Diagnostics.Etw._TDH_OUT_TYPE = 301


make_ready(__name__)
