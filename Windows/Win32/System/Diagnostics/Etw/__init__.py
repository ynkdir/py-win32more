from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.Security
import Windows.Win32.System.Com
import Windows.Win32.System.Diagnostics.Etw
import Windows.Win32.System.Time
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
ALPCGuid: Guid = Guid('45d8cccd-539f-4b72-a8-b7-5c-68-31-42-60-9a')
DiskIoGuid: Guid = Guid('3d6fa8d4-fe05-11d0-9d-da-00-c0-4f-d7-ba-7c')
EventTraceConfigGuid: Guid = Guid('01853a65-418f-4f36-ae-fc-dc-0f-1d-2f-d2-35')
FileIoGuid: Guid = Guid('90cbdc39-4a3e-11d1-84-f4-00-00-f8-04-64-e3')
ImageLoadGuid: Guid = Guid('2cb15d1d-5fc1-11d2-ab-e1-00-a0-c9-11-f5-18')
PageFaultGuid: Guid = Guid('3d6fa8d3-fe05-11d0-9d-da-00-c0-4f-d7-ba-7c')
PerfInfoGuid: Guid = Guid('ce1dbfb4-137e-4da6-87-b0-3f-59-aa-10-2c-bc')
ProcessGuid: Guid = Guid('3d6fa8d0-fe05-11d0-9d-da-00-c0-4f-d7-ba-7c')
RegistryGuid: Guid = Guid('ae53722e-c863-11d2-86-59-00-c0-4f-a3-21-a1')
SplitIoGuid: Guid = Guid('d837ca92-12b9-44a5-ad-6a-3a-65-b3-57-8a-a8')
TcpIpGuid: Guid = Guid('9a280ac0-c8e0-11d1-84-e2-00-c0-4f-b9-98-a2')
ThreadGuid: Guid = Guid('3d6fa8d1-fe05-11d0-9d-da-00-c0-4f-d7-ba-7c')
UdpIpGuid: Guid = Guid('bf3a50c5-a9c9-4988-a0-05-2d-f0-b7-c8-0f-80')
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
EventTraceGuid: Guid = Guid('68fdd900-4a3e-11d1-84-f4-00-00-f8-04-64-e3')
SystemTraceControlGuid: Guid = Guid('9e814aad-3204-11d2-9a-82-00-60-08-a8-69-39')
DefaultTraceSecurityGuid: Guid = Guid('0811c1af-7a07-4a06-82-ed-86-94-55-cd-f7-13')
PrivateLoggerNotificationGuid: Guid = Guid('3595ab5c-042a-4c8e-b9-42-2d-05-9b-fe-b1-b1')
SystemIoFilterProviderGuid: Guid = Guid('fbd09363-9e22-4661-b8-bf-e7-a3-4b-53-5b-8c')
SystemObjectProviderGuid: Guid = Guid('febd7460-3d1d-47eb-af-49-c9-ee-b1-e1-46-f2')
SystemPowerProviderGuid: Guid = Guid('c134884a-32d5-4488-80-e5-14-ed-7a-bb-82-69')
SystemHypervisorProviderGuid: Guid = Guid('bafa072a-918a-4bed-b6-22-bc-15-20-97-09-8f')
SystemLockProviderGuid: Guid = Guid('721ddfd3-dacc-4e1e-b2-6a-a2-cb-31-d4-70-5a')
SystemConfigProviderGuid: Guid = Guid('fef3a8b6-318d-4b67-a9-6a-3b-0f-6b-8f-18-fe')
SystemCpuProviderGuid: Guid = Guid('c6c5265f-eae8-4650-aa-e4-9d-48-60-3d-85-10')
SystemSchedulerProviderGuid: Guid = Guid('599a2a76-4d91-4910-9a-c7-7d-33-f2-e9-7a-6c')
SystemProfileProviderGuid: Guid = Guid('bfeb0324-1cee-496f-a4-09-2a-c2-b4-8a-63-22')
SystemIoProviderGuid: Guid = Guid('3d5c43e3-0f1c-4202-b8-17-17-4c-00-70-dc-79')
SystemMemoryProviderGuid: Guid = Guid('82958ca9-b6cd-47f8-a3-a8-03-ae-85-a4-bc-24')
SystemRegistryProviderGuid: Guid = Guid('16156bd9-fab4-4cfa-a2-32-89-d1-09-90-58-e3')
SystemProcessProviderGuid: Guid = Guid('151f55dc-467d-471f-83-b5-5f-88-9d-46-ff-66')
SystemAlpcProviderGuid: Guid = Guid('fcb9baaf-e529-4980-92-e9-ce-d1-a6-aa-df-df')
SystemSyscallProviderGuid: Guid = Guid('434286f7-6f1b-45bb-b3-7e-95-f6-23-04-6c-7c')
SystemInterruptProviderGuid: Guid = Guid('d4bbee17-b545-4888-85-8b-74-41-69-01-5b-25')
SystemTimerProviderGuid: Guid = Guid('4f061568-e215-499f-ab-2e-ed-a0-ae-89-0a-5b')
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
CLSID_TraceRelogger: Guid = Guid('7b40792d-05ff-44c4-90-58-f4-40-c7-1f-17-d4')
@winfunctype('ADVAPI32.dll')
def StartTraceW(TraceHandle: POINTER(Windows.Win32.System.Diagnostics.Etw.CONTROLTRACE_HANDLE), InstanceName: Windows.Win32.Foundation.PWSTR, Properties: POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_PROPERTIES_head)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def StartTraceA(TraceHandle: POINTER(Windows.Win32.System.Diagnostics.Etw.CONTROLTRACE_HANDLE), InstanceName: Windows.Win32.Foundation.PSTR, Properties: POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_PROPERTIES_head)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def StopTraceW(TraceHandle: Windows.Win32.System.Diagnostics.Etw.CONTROLTRACE_HANDLE, InstanceName: Windows.Win32.Foundation.PWSTR, Properties: POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_PROPERTIES_head)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def StopTraceA(TraceHandle: Windows.Win32.System.Diagnostics.Etw.CONTROLTRACE_HANDLE, InstanceName: Windows.Win32.Foundation.PSTR, Properties: POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_PROPERTIES_head)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def QueryTraceW(TraceHandle: Windows.Win32.System.Diagnostics.Etw.CONTROLTRACE_HANDLE, InstanceName: Windows.Win32.Foundation.PWSTR, Properties: POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_PROPERTIES_head)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def QueryTraceA(TraceHandle: Windows.Win32.System.Diagnostics.Etw.CONTROLTRACE_HANDLE, InstanceName: Windows.Win32.Foundation.PSTR, Properties: POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_PROPERTIES_head)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def UpdateTraceW(TraceHandle: Windows.Win32.System.Diagnostics.Etw.CONTROLTRACE_HANDLE, InstanceName: Windows.Win32.Foundation.PWSTR, Properties: POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_PROPERTIES_head)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def UpdateTraceA(TraceHandle: Windows.Win32.System.Diagnostics.Etw.CONTROLTRACE_HANDLE, InstanceName: Windows.Win32.Foundation.PSTR, Properties: POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_PROPERTIES_head)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def FlushTraceW(TraceHandle: Windows.Win32.System.Diagnostics.Etw.CONTROLTRACE_HANDLE, InstanceName: Windows.Win32.Foundation.PWSTR, Properties: POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_PROPERTIES_head)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def FlushTraceA(TraceHandle: Windows.Win32.System.Diagnostics.Etw.CONTROLTRACE_HANDLE, InstanceName: Windows.Win32.Foundation.PSTR, Properties: POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_PROPERTIES_head)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def ControlTraceW(TraceHandle: Windows.Win32.System.Diagnostics.Etw.CONTROLTRACE_HANDLE, InstanceName: Windows.Win32.Foundation.PWSTR, Properties: POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_PROPERTIES_head), ControlCode: Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_CONTROL) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def ControlTraceA(TraceHandle: Windows.Win32.System.Diagnostics.Etw.CONTROLTRACE_HANDLE, InstanceName: Windows.Win32.Foundation.PSTR, Properties: POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_PROPERTIES_head), ControlCode: Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_CONTROL) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def QueryAllTracesW(PropertyArray: POINTER(POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_PROPERTIES_head)), PropertyArrayCount: UInt32, LoggerCount: POINTER(UInt32)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def QueryAllTracesA(PropertyArray: POINTER(POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_PROPERTIES_head)), PropertyArrayCount: UInt32, LoggerCount: POINTER(UInt32)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def EnableTrace(Enable: UInt32, EnableFlag: UInt32, EnableLevel: UInt32, ControlGuid: POINTER(Guid), TraceHandle: Windows.Win32.System.Diagnostics.Etw.CONTROLTRACE_HANDLE) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def EnableTraceEx(ProviderId: POINTER(Guid), SourceId: POINTER(Guid), TraceHandle: Windows.Win32.System.Diagnostics.Etw.CONTROLTRACE_HANDLE, IsEnabled: UInt32, Level: Byte, MatchAnyKeyword: UInt64, MatchAllKeyword: UInt64, EnableProperty: UInt32, EnableFilterDesc: POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_FILTER_DESCRIPTOR_head)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def EnableTraceEx2(TraceHandle: Windows.Win32.System.Diagnostics.Etw.CONTROLTRACE_HANDLE, ProviderId: POINTER(Guid), ControlCode: UInt32, Level: Byte, MatchAnyKeyword: UInt64, MatchAllKeyword: UInt64, Timeout: UInt32, EnableParameters: POINTER(Windows.Win32.System.Diagnostics.Etw.ENABLE_TRACE_PARAMETERS_head)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def EnumerateTraceGuidsEx(TraceQueryInfoClass: Windows.Win32.System.Diagnostics.Etw.TRACE_QUERY_INFO_CLASS, InBuffer: c_void_p, InBufferSize: UInt32, OutBuffer: c_void_p, OutBufferSize: UInt32, ReturnLength: POINTER(UInt32)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def TraceSetInformation(SessionHandle: Windows.Win32.System.Diagnostics.Etw.CONTROLTRACE_HANDLE, InformationClass: Windows.Win32.System.Diagnostics.Etw.TRACE_QUERY_INFO_CLASS, TraceInformation: c_void_p, InformationLength: UInt32) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def TraceQueryInformation(SessionHandle: Windows.Win32.System.Diagnostics.Etw.CONTROLTRACE_HANDLE, InformationClass: Windows.Win32.System.Diagnostics.Etw.TRACE_QUERY_INFO_CLASS, TraceInformation: c_void_p, InformationLength: UInt32, ReturnLength: POINTER(UInt32)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def CreateTraceInstanceId(RegHandle: Windows.Win32.Foundation.HANDLE, InstInfo: POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_INSTANCE_INFO_head)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def TraceEvent(TraceHandle: UInt64, EventTrace: POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_HEADER_head)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def TraceEventInstance(TraceHandle: UInt64, EventTrace: POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_INSTANCE_HEADER_head), InstInfo: POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_INSTANCE_INFO_head), ParentInstInfo: POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_INSTANCE_INFO_head)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def RegisterTraceGuidsW(RequestAddress: Windows.Win32.System.Diagnostics.Etw.WMIDPREQUEST, RequestContext: c_void_p, ControlGuid: POINTER(Guid), GuidCount: UInt32, TraceGuidReg: POINTER(Windows.Win32.System.Diagnostics.Etw.TRACE_GUID_REGISTRATION_head), MofImagePath: Windows.Win32.Foundation.PWSTR, MofResourceName: Windows.Win32.Foundation.PWSTR, RegistrationHandle: POINTER(UInt64)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def RegisterTraceGuidsA(RequestAddress: Windows.Win32.System.Diagnostics.Etw.WMIDPREQUEST, RequestContext: c_void_p, ControlGuid: POINTER(Guid), GuidCount: UInt32, TraceGuidReg: POINTER(Windows.Win32.System.Diagnostics.Etw.TRACE_GUID_REGISTRATION_head), MofImagePath: Windows.Win32.Foundation.PSTR, MofResourceName: Windows.Win32.Foundation.PSTR, RegistrationHandle: POINTER(UInt64)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def EnumerateTraceGuids(GuidPropertiesArray: POINTER(POINTER(Windows.Win32.System.Diagnostics.Etw.TRACE_GUID_PROPERTIES_head)), PropertyArrayCount: UInt32, GuidCount: POINTER(UInt32)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def UnregisterTraceGuids(RegistrationHandle: UInt64) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def GetTraceLoggerHandle(Buffer: c_void_p) -> UInt64: ...
@winfunctype('ADVAPI32.dll')
def GetTraceEnableLevel(TraceHandle: UInt64) -> Byte: ...
@winfunctype('ADVAPI32.dll')
def GetTraceEnableFlags(TraceHandle: UInt64) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def OpenTraceW(Logfile: POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_LOGFILEW_head)) -> Windows.Win32.System.Diagnostics.Etw.PROCESSTRACE_HANDLE: ...
@winfunctype('ADVAPI32.dll')
def ProcessTrace(HandleArray: POINTER(Windows.Win32.System.Diagnostics.Etw.PROCESSTRACE_HANDLE), HandleCount: UInt32, StartTime: POINTER(Windows.Win32.Foundation.FILETIME_head), EndTime: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def CloseTrace(TraceHandle: Windows.Win32.System.Diagnostics.Etw.PROCESSTRACE_HANDLE) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def QueryTraceProcessingHandle(ProcessingHandle: Windows.Win32.System.Diagnostics.Etw.PROCESSTRACE_HANDLE, InformationClass: Windows.Win32.System.Diagnostics.Etw.ETW_PROCESS_HANDLE_INFO_TYPE, InBuffer: c_void_p, InBufferSize: UInt32, OutBuffer: c_void_p, OutBufferSize: UInt32, ReturnLength: POINTER(UInt32)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def OpenTraceA(Logfile: POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_LOGFILEA_head)) -> Windows.Win32.System.Diagnostics.Etw.PROCESSTRACE_HANDLE: ...
@winfunctype('ADVAPI32.dll')
def SetTraceCallback(pGuid: POINTER(Guid), EventCallback: Windows.Win32.System.Diagnostics.Etw.PEVENT_CALLBACK) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def RemoveTraceCallback(pGuid: POINTER(Guid)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@cfunctype('ADVAPI32.dll')
def TraceMessage(LoggerHandle: UInt64, MessageFlags: Windows.Win32.System.Diagnostics.Etw.TRACE_MESSAGE_FLAGS, MessageGuid: POINTER(Guid), MessageNumber: UInt16) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def TraceMessageVa(LoggerHandle: UInt64, MessageFlags: Windows.Win32.System.Diagnostics.Etw.TRACE_MESSAGE_FLAGS, MessageGuid: POINTER(Guid), MessageNumber: UInt16, MessageArgList: POINTER(SByte)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def EventRegister(ProviderId: POINTER(Guid), EnableCallback: Windows.Win32.System.Diagnostics.Etw.PENABLECALLBACK, CallbackContext: c_void_p, RegHandle: POINTER(UInt64)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def EventUnregister(RegHandle: UInt64) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def EventSetInformation(RegHandle: UInt64, InformationClass: Windows.Win32.System.Diagnostics.Etw.EVENT_INFO_CLASS, EventInformation: c_void_p, InformationLength: UInt32) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def EventEnabled(RegHandle: UInt64, EventDescriptor: POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_DESCRIPTOR_head)) -> Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('ADVAPI32.dll')
def EventProviderEnabled(RegHandle: UInt64, Level: Byte, Keyword: UInt64) -> Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('ADVAPI32.dll')
def EventWrite(RegHandle: UInt64, EventDescriptor: POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_DESCRIPTOR_head), UserDataCount: UInt32, UserData: POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_DATA_DESCRIPTOR_head)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def EventWriteTransfer(RegHandle: UInt64, EventDescriptor: POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_DESCRIPTOR_head), ActivityId: POINTER(Guid), RelatedActivityId: POINTER(Guid), UserDataCount: UInt32, UserData: POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_DATA_DESCRIPTOR_head)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def EventWriteEx(RegHandle: UInt64, EventDescriptor: POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_DESCRIPTOR_head), Filter: UInt64, Flags: UInt32, ActivityId: POINTER(Guid), RelatedActivityId: POINTER(Guid), UserDataCount: UInt32, UserData: POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_DATA_DESCRIPTOR_head)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def EventWriteString(RegHandle: UInt64, Level: Byte, Keyword: UInt64, String: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def EventActivityIdControl(ControlCode: UInt32, ActivityId: POINTER(Guid)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def EventAccessControl(Guid: POINTER(Guid), Operation: UInt32, Sid: Windows.Win32.Foundation.PSID, Rights: UInt32, AllowOrDeny: Windows.Win32.Foundation.BOOLEAN) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def EventAccessQuery(Guid: POINTER(Guid), Buffer: Windows.Win32.Security.PSECURITY_DESCRIPTOR, BufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def EventAccessRemove(Guid: POINTER(Guid)) -> UInt32: ...
@winfunctype('tdh.dll')
def TdhCreatePayloadFilter(ProviderGuid: POINTER(Guid), EventDescriptor: POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_DESCRIPTOR_head), EventMatchANY: Windows.Win32.Foundation.BOOLEAN, PayloadPredicateCount: UInt32, PayloadPredicates: POINTER(Windows.Win32.System.Diagnostics.Etw.PAYLOAD_FILTER_PREDICATE_head), PayloadFilter: POINTER(c_void_p)) -> UInt32: ...
@winfunctype('tdh.dll')
def TdhDeletePayloadFilter(PayloadFilter: POINTER(c_void_p)) -> UInt32: ...
@winfunctype('tdh.dll')
def TdhAggregatePayloadFilters(PayloadFilterCount: UInt32, PayloadFilterPtrs: POINTER(c_void_p), EventMatchALLFlags: POINTER(Windows.Win32.Foundation.BOOLEAN), EventFilterDescriptor: POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_FILTER_DESCRIPTOR_head)) -> UInt32: ...
@winfunctype('tdh.dll')
def TdhCleanupPayloadEventFilterDescriptor(EventFilterDescriptor: POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_FILTER_DESCRIPTOR_head)) -> UInt32: ...
@winfunctype('TDH.dll')
def TdhGetEventInformation(Event: POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_RECORD_head), TdhContextCount: UInt32, TdhContext: POINTER(Windows.Win32.System.Diagnostics.Etw.TDH_CONTEXT_head), Buffer: POINTER(Windows.Win32.System.Diagnostics.Etw.TRACE_EVENT_INFO_head), BufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('TDH.dll')
def TdhGetEventMapInformation(pEvent: POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_RECORD_head), pMapName: Windows.Win32.Foundation.PWSTR, pBuffer: POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_MAP_INFO_head), pBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('TDH.dll')
def TdhGetPropertySize(pEvent: POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_RECORD_head), TdhContextCount: UInt32, pTdhContext: POINTER(Windows.Win32.System.Diagnostics.Etw.TDH_CONTEXT_head), PropertyDataCount: UInt32, pPropertyData: POINTER(Windows.Win32.System.Diagnostics.Etw.PROPERTY_DATA_DESCRIPTOR_head), pPropertySize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('TDH.dll')
def TdhGetProperty(pEvent: POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_RECORD_head), TdhContextCount: UInt32, pTdhContext: POINTER(Windows.Win32.System.Diagnostics.Etw.TDH_CONTEXT_head), PropertyDataCount: UInt32, pPropertyData: POINTER(Windows.Win32.System.Diagnostics.Etw.PROPERTY_DATA_DESCRIPTOR_head), BufferSize: UInt32, pBuffer: c_char_p_no) -> UInt32: ...
@winfunctype('TDH.dll')
def TdhEnumerateProviders(pBuffer: POINTER(Windows.Win32.System.Diagnostics.Etw.PROVIDER_ENUMERATION_INFO_head), pBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('tdh.dll')
def TdhEnumerateProvidersForDecodingSource(filter: Windows.Win32.System.Diagnostics.Etw.DECODING_SOURCE, buffer: POINTER(Windows.Win32.System.Diagnostics.Etw.PROVIDER_ENUMERATION_INFO_head), bufferSize: UInt32, bufferRequired: POINTER(UInt32)) -> UInt32: ...
@winfunctype('TDH.dll')
def TdhQueryProviderFieldInformation(pGuid: POINTER(Guid), EventFieldValue: UInt64, EventFieldType: Windows.Win32.System.Diagnostics.Etw.EVENT_FIELD_TYPE, pBuffer: POINTER(Windows.Win32.System.Diagnostics.Etw.PROVIDER_FIELD_INFOARRAY_head), pBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('TDH.dll')
def TdhEnumerateProviderFieldInformation(pGuid: POINTER(Guid), EventFieldType: Windows.Win32.System.Diagnostics.Etw.EVENT_FIELD_TYPE, pBuffer: POINTER(Windows.Win32.System.Diagnostics.Etw.PROVIDER_FIELD_INFOARRAY_head), pBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('tdh.dll')
def TdhEnumerateProviderFilters(Guid: POINTER(Guid), TdhContextCount: UInt32, TdhContext: POINTER(Windows.Win32.System.Diagnostics.Etw.TDH_CONTEXT_head), FilterCount: POINTER(UInt32), Buffer: POINTER(POINTER(Windows.Win32.System.Diagnostics.Etw.PROVIDER_FILTER_INFO_head)), BufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('TDH.dll')
def TdhLoadManifest(Manifest: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('TDH.dll')
def TdhLoadManifestFromMemory(pData: c_void_p, cbData: UInt32) -> UInt32: ...
@winfunctype('TDH.dll')
def TdhUnloadManifest(Manifest: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('TDH.dll')
def TdhUnloadManifestFromMemory(pData: c_void_p, cbData: UInt32) -> UInt32: ...
@winfunctype('TDH.dll')
def TdhFormatProperty(EventInfo: POINTER(Windows.Win32.System.Diagnostics.Etw.TRACE_EVENT_INFO_head), MapInfo: POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_MAP_INFO_head), PointerSize: UInt32, PropertyInType: UInt16, PropertyOutType: UInt16, PropertyLength: UInt16, UserDataLength: UInt16, UserData: c_char_p_no, BufferSize: POINTER(UInt32), Buffer: Windows.Win32.Foundation.PWSTR, UserDataConsumed: POINTER(UInt16)) -> UInt32: ...
@winfunctype('tdh.dll')
def TdhOpenDecodingHandle(Handle: POINTER(Windows.Win32.System.Diagnostics.Etw.TDH_HANDLE)) -> UInt32: ...
@winfunctype('tdh.dll')
def TdhSetDecodingParameter(Handle: Windows.Win32.System.Diagnostics.Etw.TDH_HANDLE, TdhContext: POINTER(Windows.Win32.System.Diagnostics.Etw.TDH_CONTEXT_head)) -> UInt32: ...
@winfunctype('tdh.dll')
def TdhGetDecodingParameter(Handle: Windows.Win32.System.Diagnostics.Etw.TDH_HANDLE, TdhContext: POINTER(Windows.Win32.System.Diagnostics.Etw.TDH_CONTEXT_head)) -> UInt32: ...
@winfunctype('tdh.dll')
def TdhGetWppProperty(Handle: Windows.Win32.System.Diagnostics.Etw.TDH_HANDLE, EventRecord: POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_RECORD_head), PropertyName: Windows.Win32.Foundation.PWSTR, BufferSize: POINTER(UInt32), Buffer: c_char_p_no) -> UInt32: ...
@winfunctype('tdh.dll')
def TdhGetWppMessage(Handle: Windows.Win32.System.Diagnostics.Etw.TDH_HANDLE, EventRecord: POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_RECORD_head), BufferSize: POINTER(UInt32), Buffer: c_char_p_no) -> UInt32: ...
@winfunctype('tdh.dll')
def TdhCloseDecodingHandle(Handle: Windows.Win32.System.Diagnostics.Etw.TDH_HANDLE) -> UInt32: ...
@winfunctype('tdh.dll')
def TdhLoadManifestFromBinary(BinaryPath: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('TDH.dll')
def TdhEnumerateManifestProviderEvents(ProviderGuid: POINTER(Guid), Buffer: POINTER(Windows.Win32.System.Diagnostics.Etw.PROVIDER_EVENT_INFO_head), BufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('TDH.dll')
def TdhGetManifestEventInformation(ProviderGuid: POINTER(Guid), EventDescriptor: POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_DESCRIPTOR_head), Buffer: POINTER(Windows.Win32.System.Diagnostics.Etw.TRACE_EVENT_INFO_head), BufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def CveEventWrite(CveId: Windows.Win32.Foundation.PWSTR, AdditionalDetails: Windows.Win32.Foundation.PWSTR) -> Int32: ...
class CLASSIC_EVENT_ID(Structure):
    EventGuid: Guid
    Type: Byte
    Reserved: Byte * 7
CONTROLTRACE_HANDLE = UInt64
CTraceRelogger = Guid('7b40792d-05ff-44c4-90-58-f4-40-c7-1f-17-d4')
DECODING_SOURCE = Int32
DECODING_SOURCE_DecodingSourceXMLFile: DECODING_SOURCE = 0
DECODING_SOURCE_DecodingSourceWbem: DECODING_SOURCE = 1
DECODING_SOURCE_DecodingSourceWPP: DECODING_SOURCE = 2
DECODING_SOURCE_DecodingSourceTlg: DECODING_SOURCE = 3
DECODING_SOURCE_DecodingSourceMax: DECODING_SOURCE = 4
ENABLECALLBACK_ENABLED_STATE = UInt32
EVENT_CONTROL_CODE_DISABLE_PROVIDER: ENABLECALLBACK_ENABLED_STATE = 0
EVENT_CONTROL_CODE_ENABLE_PROVIDER: ENABLECALLBACK_ENABLED_STATE = 1
EVENT_CONTROL_CODE_CAPTURE_STATE: ENABLECALLBACK_ENABLED_STATE = 2
class ENABLE_TRACE_PARAMETERS(Structure):
    Version: UInt32
    EnableProperty: UInt32
    ControlFlags: UInt32
    SourceId: Guid
    EnableFilterDesc: POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_FILTER_DESCRIPTOR_head)
    FilterDescCount: UInt32
class ENABLE_TRACE_PARAMETERS_V1(Structure):
    Version: UInt32
    EnableProperty: UInt32
    ControlFlags: UInt32
    SourceId: Guid
    EnableFilterDesc: POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_FILTER_DESCRIPTOR_head)
class ETW_BUFFER_CONTEXT(Structure):
    Anonymous: _Anonymous_e__Union
    LoggerId: UInt16
    class _Anonymous_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        ProcessorIndex: UInt16
        class _Anonymous_e__Struct(Structure):
            ProcessorNumber: Byte
            Alignment: Byte
ETW_COMPRESSION_RESUMPTION_MODE = Int32
ETW_COMPRESSION_RESUMPTION_MODE_EtwCompressionModeRestart: ETW_COMPRESSION_RESUMPTION_MODE = 0
ETW_COMPRESSION_RESUMPTION_MODE_EtwCompressionModeNoDisable: ETW_COMPRESSION_RESUMPTION_MODE = 1
ETW_COMPRESSION_RESUMPTION_MODE_EtwCompressionModeNoRestart: ETW_COMPRESSION_RESUMPTION_MODE = 2
class ETW_PMC_COUNTER_OWNER(Structure):
    OwnerType: Windows.Win32.System.Diagnostics.Etw.ETW_PMC_COUNTER_OWNER_TYPE
    ProfileSource: UInt32
    OwnerTag: UInt32
class ETW_PMC_COUNTER_OWNERSHIP_STATUS(Structure):
    ProcessorNumber: UInt32
    NumberOfCounters: UInt32
    CounterOwners: Windows.Win32.System.Diagnostics.Etw.ETW_PMC_COUNTER_OWNER * 1
ETW_PMC_COUNTER_OWNER_TYPE = Int32
ETW_PMC_COUNTER_OWNER_TYPE_EtwPmcOwnerFree: ETW_PMC_COUNTER_OWNER_TYPE = 0
ETW_PMC_COUNTER_OWNER_TYPE_EtwPmcOwnerUntagged: ETW_PMC_COUNTER_OWNER_TYPE = 1
ETW_PMC_COUNTER_OWNER_TYPE_EtwPmcOwnerTagged: ETW_PMC_COUNTER_OWNER_TYPE = 2
ETW_PMC_COUNTER_OWNER_TYPE_EtwPmcOwnerTaggedWithSource: ETW_PMC_COUNTER_OWNER_TYPE = 3
ETW_PROCESS_HANDLE_INFO_TYPE = Int32
ETW_PROCESS_HANDLE_INFO_TYPE_EtwQueryPartitionInformation: ETW_PROCESS_HANDLE_INFO_TYPE = 1
ETW_PROCESS_HANDLE_INFO_TYPE_EtwQueryPartitionInformationV2: ETW_PROCESS_HANDLE_INFO_TYPE = 2
ETW_PROCESS_HANDLE_INFO_TYPE_EtwQueryLastDroppedTimes: ETW_PROCESS_HANDLE_INFO_TYPE = 3
ETW_PROCESS_HANDLE_INFO_TYPE_EtwQueryProcessHandleInfoMax: ETW_PROCESS_HANDLE_INFO_TYPE = 4
ETW_PROVIDER_TRAIT_TYPE = Int32
ETW_PROVIDER_TRAIT_TYPE_EtwProviderTraitTypeGroup: ETW_PROVIDER_TRAIT_TYPE = 1
ETW_PROVIDER_TRAIT_TYPE_EtwProviderTraitDecodeGuid: ETW_PROVIDER_TRAIT_TYPE = 2
ETW_PROVIDER_TRAIT_TYPE_EtwProviderTraitTypeMax: ETW_PROVIDER_TRAIT_TYPE = 3
class ETW_TRACE_PARTITION_INFORMATION(Structure):
    PartitionId: Guid
    ParentId: Guid
    QpcOffsetFromRoot: Int64
    PartitionType: UInt32
class ETW_TRACE_PARTITION_INFORMATION_V2(Structure):
    QpcOffsetFromRoot: Int64
    PartitionType: UInt32
    PartitionId: Windows.Win32.Foundation.PWSTR
    ParentId: Windows.Win32.Foundation.PWSTR
EVENTSECURITYOPERATION = Int32
EVENTSECURITYOPERATION_EventSecuritySetDACL: EVENTSECURITYOPERATION = 0
EVENTSECURITYOPERATION_EventSecuritySetSACL: EVENTSECURITYOPERATION = 1
EVENTSECURITYOPERATION_EventSecurityAddDACL: EVENTSECURITYOPERATION = 2
EVENTSECURITYOPERATION_EventSecurityAddSACL: EVENTSECURITYOPERATION = 3
EVENTSECURITYOPERATION_EventSecurityMax: EVENTSECURITYOPERATION = 4
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
EVENT_FIELD_TYPE_EventKeywordInformation: EVENT_FIELD_TYPE = 0
EVENT_FIELD_TYPE_EventLevelInformation: EVENT_FIELD_TYPE = 1
EVENT_FIELD_TYPE_EventChannelInformation: EVENT_FIELD_TYPE = 2
EVENT_FIELD_TYPE_EventTaskInformation: EVENT_FIELD_TYPE = 3
EVENT_FIELD_TYPE_EventOpcodeInformation: EVENT_FIELD_TYPE = 4
EVENT_FIELD_TYPE_EventInformationMax: EVENT_FIELD_TYPE = 5
class EVENT_FILTER_DESCRIPTOR(Structure):
    Ptr: UInt64
    Size: UInt32
    Type: UInt32
class EVENT_FILTER_EVENT_ID(Structure):
    FilterIn: Windows.Win32.Foundation.BOOLEAN
    Reserved: Byte
    Count: UInt16
    Events: UInt16 * 1
class EVENT_FILTER_EVENT_NAME(Structure):
    MatchAnyKeyword: UInt64
    MatchAllKeyword: UInt64
    Level: Byte
    FilterIn: Windows.Win32.Foundation.BOOLEAN
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
    FilterIn: Windows.Win32.Foundation.BOOLEAN
class EVENT_HEADER(Structure):
    Size: UInt16
    HeaderType: UInt16
    Flags: UInt16
    EventProperty: UInt16
    ThreadId: UInt32
    ProcessId: UInt32
    TimeStamp: Windows.Win32.Foundation.LARGE_INTEGER
    ProviderId: Guid
    EventDescriptor: Windows.Win32.System.Diagnostics.Etw.EVENT_DESCRIPTOR
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
        _bitfield: UInt16
EVENT_INFO_CLASS = Int32
EVENT_INFO_CLASS_EventProviderBinaryTrackInfo: EVENT_INFO_CLASS = 0
EVENT_INFO_CLASS_EventProviderSetReserved1: EVENT_INFO_CLASS = 1
EVENT_INFO_CLASS_EventProviderSetTraits: EVENT_INFO_CLASS = 2
EVENT_INFO_CLASS_EventProviderUseDescriptorType: EVENT_INFO_CLASS = 3
EVENT_INFO_CLASS_MaxEventInfo: EVENT_INFO_CLASS = 4
class EVENT_INSTANCE_HEADER(Structure):
    Size: UInt16
    Anonymous1: _Anonymous1_e__Union
    Anonymous2: _Anonymous2_e__Union
    ThreadId: UInt32
    ProcessId: UInt32
    TimeStamp: Windows.Win32.Foundation.LARGE_INTEGER
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
    RegHandle: Windows.Win32.Foundation.HANDLE
    InstanceId: UInt32
class EVENT_MAP_ENTRY(Structure):
    OutputOffset: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Value: UInt32
        InputOffset: UInt32
class EVENT_MAP_INFO(Structure):
    NameOffset: UInt32
    Flag: Windows.Win32.System.Diagnostics.Etw.MAP_FLAGS
    EntryCount: UInt32
    Anonymous: _Anonymous_e__Union
    MapEntryArray: Windows.Win32.System.Diagnostics.Etw.EVENT_MAP_ENTRY * 1
    class _Anonymous_e__Union(Union):
        MapEntryValueType: Windows.Win32.System.Diagnostics.Etw.MAP_VALUETYPE
        FormatStringOffset: UInt32
class EVENT_PROPERTY_INFO(Structure):
    Flags: Windows.Win32.System.Diagnostics.Etw.PROPERTY_FLAGS
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
            _bitfield: UInt32
class EVENT_RECORD(Structure):
    EventHeader: Windows.Win32.System.Diagnostics.Etw.EVENT_HEADER
    BufferContext: Windows.Win32.System.Diagnostics.Etw.ETW_BUFFER_CONTEXT
    ExtendedDataCount: UInt16
    UserDataLength: UInt16
    ExtendedData: POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_HEADER_EXTENDED_DATA_ITEM_head)
    UserData: c_void_p
    UserContext: c_void_p
class EVENT_TRACE(Structure):
    Header: Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_HEADER
    InstanceId: UInt32
    ParentInstanceId: UInt32
    ParentGuid: Guid
    MofData: c_void_p
    MofLength: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        ClientContext: UInt32
        BufferContext: Windows.Win32.System.Diagnostics.Etw.ETW_BUFFER_CONTEXT
EVENT_TRACE_CONTROL = UInt32
EVENT_TRACE_CONTROL_FLUSH: EVENT_TRACE_CONTROL = 3
EVENT_TRACE_CONTROL_QUERY: EVENT_TRACE_CONTROL = 0
EVENT_TRACE_CONTROL_STOP: EVENT_TRACE_CONTROL = 1
EVENT_TRACE_CONTROL_UPDATE: EVENT_TRACE_CONTROL = 2
EVENT_TRACE_FLAG = UInt32
EVENT_TRACE_FLAG_ALPC: EVENT_TRACE_FLAG = 1048576
EVENT_TRACE_FLAG_CSWITCH: EVENT_TRACE_FLAG = 16
EVENT_TRACE_FLAG_DBGPRINT: EVENT_TRACE_FLAG = 262144
EVENT_TRACE_FLAG_DISK_FILE_IO: EVENT_TRACE_FLAG = 512
EVENT_TRACE_FLAG_DISK_IO: EVENT_TRACE_FLAG = 256
EVENT_TRACE_FLAG_DISK_IO_INIT: EVENT_TRACE_FLAG = 1024
EVENT_TRACE_FLAG_DISPATCHER: EVENT_TRACE_FLAG = 2048
EVENT_TRACE_FLAG_DPC: EVENT_TRACE_FLAG = 32
EVENT_TRACE_FLAG_DRIVER: EVENT_TRACE_FLAG = 8388608
EVENT_TRACE_FLAG_FILE_IO: EVENT_TRACE_FLAG = 33554432
EVENT_TRACE_FLAG_FILE_IO_INIT: EVENT_TRACE_FLAG = 67108864
EVENT_TRACE_FLAG_IMAGE_LOAD: EVENT_TRACE_FLAG = 4
EVENT_TRACE_FLAG_INTERRUPT: EVENT_TRACE_FLAG = 64
EVENT_TRACE_FLAG_JOB: EVENT_TRACE_FLAG = 524288
EVENT_TRACE_FLAG_MEMORY_HARD_FAULTS: EVENT_TRACE_FLAG = 8192
EVENT_TRACE_FLAG_MEMORY_PAGE_FAULTS: EVENT_TRACE_FLAG = 4096
EVENT_TRACE_FLAG_NETWORK_TCPIP: EVENT_TRACE_FLAG = 65536
EVENT_TRACE_FLAG_NO_SYSCONFIG: EVENT_TRACE_FLAG = 268435456
EVENT_TRACE_FLAG_PROCESS: EVENT_TRACE_FLAG = 1
EVENT_TRACE_FLAG_PROCESS_COUNTERS: EVENT_TRACE_FLAG = 8
EVENT_TRACE_FLAG_PROFILE: EVENT_TRACE_FLAG = 16777216
EVENT_TRACE_FLAG_REGISTRY: EVENT_TRACE_FLAG = 131072
EVENT_TRACE_FLAG_SPLIT_IO: EVENT_TRACE_FLAG = 2097152
EVENT_TRACE_FLAG_SYSTEMCALL: EVENT_TRACE_FLAG = 128
EVENT_TRACE_FLAG_THREAD: EVENT_TRACE_FLAG = 2
EVENT_TRACE_FLAG_VAMAP: EVENT_TRACE_FLAG = 32768
EVENT_TRACE_FLAG_VIRTUAL_ALLOC: EVENT_TRACE_FLAG = 16384
class EVENT_TRACE_HEADER(Structure):
    Size: UInt16
    Anonymous1: _Anonymous1_e__Union
    Anonymous2: _Anonymous2_e__Union
    ThreadId: UInt32
    ProcessId: UInt32
    TimeStamp: Windows.Win32.Foundation.LARGE_INTEGER
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
    LogFileName: Windows.Win32.Foundation.PSTR
    LoggerName: Windows.Win32.Foundation.PSTR
    CurrentTime: Int64
    BuffersRead: UInt32
    Anonymous1: _Anonymous1_e__Union
    CurrentEvent: Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE
    LogfileHeader: Windows.Win32.System.Diagnostics.Etw.TRACE_LOGFILE_HEADER
    BufferCallback: Windows.Win32.System.Diagnostics.Etw.PEVENT_TRACE_BUFFER_CALLBACKA
    BufferSize: UInt32
    Filled: UInt32
    EventsLost: UInt32
    Anonymous2: _Anonymous2_e__Union
    IsKernelTrace: UInt32
    Context: c_void_p
    class _Anonymous1_e__Union(Union):
        LogFileMode: UInt32
        ProcessTraceMode: UInt32
    class _Anonymous2_e__Union(Union):
        EventCallback: Windows.Win32.System.Diagnostics.Etw.PEVENT_CALLBACK
        EventRecordCallback: Windows.Win32.System.Diagnostics.Etw.PEVENT_RECORD_CALLBACK
class EVENT_TRACE_LOGFILEW(Structure):
    LogFileName: Windows.Win32.Foundation.PWSTR
    LoggerName: Windows.Win32.Foundation.PWSTR
    CurrentTime: Int64
    BuffersRead: UInt32
    Anonymous1: _Anonymous1_e__Union
    CurrentEvent: Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE
    LogfileHeader: Windows.Win32.System.Diagnostics.Etw.TRACE_LOGFILE_HEADER
    BufferCallback: Windows.Win32.System.Diagnostics.Etw.PEVENT_TRACE_BUFFER_CALLBACKW
    BufferSize: UInt32
    Filled: UInt32
    EventsLost: UInt32
    Anonymous2: _Anonymous2_e__Union
    IsKernelTrace: UInt32
    Context: c_void_p
    class _Anonymous1_e__Union(Union):
        LogFileMode: UInt32
        ProcessTraceMode: UInt32
    class _Anonymous2_e__Union(Union):
        EventCallback: Windows.Win32.System.Diagnostics.Etw.PEVENT_CALLBACK
        EventRecordCallback: Windows.Win32.System.Diagnostics.Etw.PEVENT_RECORD_CALLBACK
class EVENT_TRACE_PROPERTIES(Structure):
    Wnode: Windows.Win32.System.Diagnostics.Etw.WNODE_HEADER
    BufferSize: UInt32
    MinimumBuffers: UInt32
    MaximumBuffers: UInt32
    MaximumFileSize: UInt32
    LogFileMode: UInt32
    FlushTimer: UInt32
    EnableFlags: Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_FLAG
    Anonymous: _Anonymous_e__Union
    NumberOfBuffers: UInt32
    FreeBuffers: UInt32
    EventsLost: UInt32
    BuffersWritten: UInt32
    LogBuffersLost: UInt32
    RealTimeBuffersLost: UInt32
    LoggerThreadId: Windows.Win32.Foundation.HANDLE
    LogFileNameOffset: UInt32
    LoggerNameOffset: UInt32
    class _Anonymous_e__Union(Union):
        AgeLimit: Int32
        FlushThreshold: Int32
class EVENT_TRACE_PROPERTIES_V2(Structure):
    Wnode: Windows.Win32.System.Diagnostics.Etw.WNODE_HEADER
    BufferSize: UInt32
    MinimumBuffers: UInt32
    MaximumBuffers: UInt32
    MaximumFileSize: UInt32
    LogFileMode: UInt32
    FlushTimer: UInt32
    EnableFlags: Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_FLAG
    Anonymous1: _Anonymous1_e__Union
    NumberOfBuffers: UInt32
    FreeBuffers: UInt32
    EventsLost: UInt32
    BuffersWritten: UInt32
    LogBuffersLost: UInt32
    RealTimeBuffersLost: UInt32
    LoggerThreadId: Windows.Win32.Foundation.HANDLE
    LogFileNameOffset: UInt32
    LoggerNameOffset: UInt32
    Anonymous2: _Anonymous2_e__Union
    FilterDescCount: UInt32
    FilterDesc: POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_FILTER_DESCRIPTOR_head)
    Anonymous3: _Anonymous3_e__Union
    class _Anonymous1_e__Union(Union):
        AgeLimit: Int32
        FlushThreshold: Int32
    class _Anonymous2_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        V2Control: UInt32
        class _Anonymous_e__Struct(Structure):
            _bitfield: UInt32
    class _Anonymous3_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        V2Options: UInt64
        class _Anonymous_e__Struct(Structure):
            _bitfield: UInt32
class ITraceEvent(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('8cc97f40-9028-4ff3-9b-62-7d-1f-79-ca-7b-cb')
    @commethod(3)
    def Clone(NewEvent: POINTER(Windows.Win32.System.Diagnostics.Etw.ITraceEvent_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetUserContext(UserContext: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetEventRecord(EventRecord: POINTER(POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_RECORD_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetPayload(Payload: c_char_p_no, PayloadSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetEventDescriptor(EventDescriptor: POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_DESCRIPTOR_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetProcessId(ProcessId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetProcessorIndex(ProcessorIndex: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetThreadId(ThreadId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetThreadTimes(KernelTime: UInt32, UserTime: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetActivityId(ActivityId: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetTimeStamp(TimeStamp: POINTER(Windows.Win32.Foundation.LARGE_INTEGER_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetProviderId(ProviderId: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class ITraceEventCallback(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('3ed25501-593f-43e9-8f-38-3a-b4-6f-5a-4a-52')
    @commethod(3)
    def OnBeginProcessTrace(HeaderEvent: Windows.Win32.System.Diagnostics.Etw.ITraceEvent_head, Relogger: Windows.Win32.System.Diagnostics.Etw.ITraceRelogger_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnFinalizeProcessTrace(Relogger: Windows.Win32.System.Diagnostics.Etw.ITraceRelogger_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnEvent(Event: Windows.Win32.System.Diagnostics.Etw.ITraceEvent_head, Relogger: Windows.Win32.System.Diagnostics.Etw.ITraceRelogger_head) -> Windows.Win32.Foundation.HRESULT: ...
class ITraceRelogger(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f754ad43-3bcc-4286-80-09-9c-5d-a2-14-e8-4e')
    @commethod(3)
    def AddLogfileTraceStream(LogfileName: Windows.Win32.Foundation.BSTR, UserContext: c_void_p, TraceHandle: POINTER(Windows.Win32.System.Diagnostics.Etw.RELOGSTREAM_HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddRealtimeTraceStream(LoggerName: Windows.Win32.Foundation.BSTR, UserContext: c_void_p, TraceHandle: POINTER(Windows.Win32.System.Diagnostics.Etw.RELOGSTREAM_HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RegisterCallback(Callback: Windows.Win32.System.Diagnostics.Etw.ITraceEventCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Inject(Event: Windows.Win32.System.Diagnostics.Etw.ITraceEvent_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateEventInstance(TraceHandle: Windows.Win32.System.Diagnostics.Etw.RELOGSTREAM_HANDLE, Flags: UInt32, Event: POINTER(Windows.Win32.System.Diagnostics.Etw.ITraceEvent_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ProcessTrace() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetOutputFilename(LogfileName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetCompressionMode(CompressionMode: Windows.Win32.Foundation.BOOLEAN) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Cancel() -> Windows.Win32.Foundation.HRESULT: ...
MAP_FLAGS = Int32
EVENTMAP_INFO_FLAG_MANIFEST_VALUEMAP: MAP_FLAGS = 1
EVENTMAP_INFO_FLAG_MANIFEST_BITMAP: MAP_FLAGS = 2
EVENTMAP_INFO_FLAG_MANIFEST_PATTERNMAP: MAP_FLAGS = 4
EVENTMAP_INFO_FLAG_WBEM_VALUEMAP: MAP_FLAGS = 8
EVENTMAP_INFO_FLAG_WBEM_BITMAP: MAP_FLAGS = 16
EVENTMAP_INFO_FLAG_WBEM_FLAG: MAP_FLAGS = 32
EVENTMAP_INFO_FLAG_WBEM_NO_MAP: MAP_FLAGS = 64
MAP_VALUETYPE = Int32
EVENTMAP_ENTRY_VALUETYPE_ULONG: MAP_VALUETYPE = 0
EVENTMAP_ENTRY_VALUETYPE_STRING: MAP_VALUETYPE = 1
class MOF_FIELD(Structure):
    DataPtr: UInt64
    Length: UInt32
    DataType: UInt32
class OFFSETINSTANCEDATAANDLENGTH(Structure):
    OffsetInstanceData: UInt32
    LengthInstanceData: UInt32
class PAYLOAD_FILTER_PREDICATE(Structure):
    FieldName: Windows.Win32.Foundation.PWSTR
    CompareOp: UInt16
    Value: Windows.Win32.Foundation.PWSTR
PAYLOAD_OPERATOR = Int32
PAYLOADFIELD_EQ: PAYLOAD_OPERATOR = 0
PAYLOADFIELD_NE: PAYLOAD_OPERATOR = 1
PAYLOADFIELD_LE: PAYLOAD_OPERATOR = 2
PAYLOADFIELD_GT: PAYLOAD_OPERATOR = 3
PAYLOADFIELD_LT: PAYLOAD_OPERATOR = 4
PAYLOADFIELD_GE: PAYLOAD_OPERATOR = 5
PAYLOADFIELD_BETWEEN: PAYLOAD_OPERATOR = 6
PAYLOADFIELD_NOTBETWEEN: PAYLOAD_OPERATOR = 7
PAYLOADFIELD_MODULO: PAYLOAD_OPERATOR = 8
PAYLOADFIELD_CONTAINS: PAYLOAD_OPERATOR = 20
PAYLOADFIELD_DOESNTCONTAIN: PAYLOAD_OPERATOR = 21
PAYLOADFIELD_IS: PAYLOAD_OPERATOR = 30
PAYLOADFIELD_ISNOT: PAYLOAD_OPERATOR = 31
PAYLOADFIELD_INVALID: PAYLOAD_OPERATOR = 32
@winfunctype_pointer
def PENABLECALLBACK(SourceId: POINTER(Guid), IsEnabled: Windows.Win32.System.Diagnostics.Etw.ENABLECALLBACK_ENABLED_STATE, Level: Byte, MatchAnyKeyword: UInt64, MatchAllKeyword: UInt64, FilterData: POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_FILTER_DESCRIPTOR_head), CallbackContext: c_void_p) -> Void: ...
@winfunctype_pointer
def PEVENT_CALLBACK(pEvent: POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_head)) -> Void: ...
@winfunctype_pointer
def PEVENT_RECORD_CALLBACK(EventRecord: POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_RECORD_head)) -> Void: ...
@winfunctype_pointer
def PEVENT_TRACE_BUFFER_CALLBACKA(Logfile: POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_LOGFILEA_head)) -> UInt32: ...
@winfunctype_pointer
def PEVENT_TRACE_BUFFER_CALLBACKW(Logfile: POINTER(Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_LOGFILEW_head)) -> UInt32: ...
PROCESSTRACE_HANDLE = UInt64
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
PROPERTY_FLAGS_PropertyStruct: PROPERTY_FLAGS = 1
PROPERTY_FLAGS_PropertyParamLength: PROPERTY_FLAGS = 2
PROPERTY_FLAGS_PropertyParamCount: PROPERTY_FLAGS = 4
PROPERTY_FLAGS_PropertyWBEMXmlFragment: PROPERTY_FLAGS = 8
PROPERTY_FLAGS_PropertyParamFixedLength: PROPERTY_FLAGS = 16
PROPERTY_FLAGS_PropertyParamFixedCount: PROPERTY_FLAGS = 32
PROPERTY_FLAGS_PropertyHasTags: PROPERTY_FLAGS = 64
PROPERTY_FLAGS_PropertyHasCustomSchema: PROPERTY_FLAGS = 128
class PROVIDER_ENUMERATION_INFO(Structure):
    NumberOfProviders: UInt32
    Reserved: UInt32
    TraceProviderInfoArray: Windows.Win32.System.Diagnostics.Etw.TRACE_PROVIDER_INFO * 1
class PROVIDER_EVENT_INFO(Structure):
    NumberOfEvents: UInt32
    Reserved: UInt32
    EventDescriptorsArray: Windows.Win32.System.Diagnostics.Etw.EVENT_DESCRIPTOR * 1
class PROVIDER_FIELD_INFO(Structure):
    NameOffset: UInt32
    DescriptionOffset: UInt32
    Value: UInt64
class PROVIDER_FIELD_INFOARRAY(Structure):
    NumberOfElements: UInt32
    FieldType: Windows.Win32.System.Diagnostics.Etw.EVENT_FIELD_TYPE
    FieldInfoArray: Windows.Win32.System.Diagnostics.Etw.PROVIDER_FIELD_INFO * 1
class PROVIDER_FILTER_INFO(Structure):
    Id: Byte
    Version: Byte
    MessageOffset: UInt32
    Reserved: UInt32
    PropertyCount: UInt32
    EventPropertyInfoArray: Windows.Win32.System.Diagnostics.Etw.EVENT_PROPERTY_INFO * 1
RELOGSTREAM_HANDLE = UInt64
class TDH_CONTEXT(Structure):
    ParameterValue: UInt64
    ParameterType: Windows.Win32.System.Diagnostics.Etw.TDH_CONTEXT_TYPE
    ParameterSize: UInt32
TDH_CONTEXT_TYPE = Int32
TDH_CONTEXT_WPP_TMFFILE: TDH_CONTEXT_TYPE = 0
TDH_CONTEXT_WPP_TMFSEARCHPATH: TDH_CONTEXT_TYPE = 1
TDH_CONTEXT_WPP_GMT: TDH_CONTEXT_TYPE = 2
TDH_CONTEXT_POINTERSIZE: TDH_CONTEXT_TYPE = 3
TDH_CONTEXT_PDB_PATH: TDH_CONTEXT_TYPE = 4
TDH_CONTEXT_MAXIMUM: TDH_CONTEXT_TYPE = 5
TDH_HANDLE = IntPtr
TEMPLATE_FLAGS = Int32
TEMPLATE_EVENT_DATA: TEMPLATE_FLAGS = 1
TEMPLATE_USER_DATA: TEMPLATE_FLAGS = 2
TEMPLATE_CONTROL_GUID: TEMPLATE_FLAGS = 4
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
    EventDescriptor: Windows.Win32.System.Diagnostics.Etw.EVENT_DESCRIPTOR
    DecodingSource: Windows.Win32.System.Diagnostics.Etw.DECODING_SOURCE
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
    EventPropertyInfoArray: Windows.Win32.System.Diagnostics.Etw.EVENT_PROPERTY_INFO * 1
    class _Anonymous1_e__Union(Union):
        EventNameOffset: UInt32
        ActivityIDNameOffset: UInt32
    class _Anonymous2_e__Union(Union):
        EventAttributesOffset: UInt32
        RelatedActivityIDNameOffset: UInt32
    class _Anonymous3_e__Union(Union):
        Flags: Windows.Win32.System.Diagnostics.Etw.TEMPLATE_FLAGS
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            _bitfield: UInt32
class TRACE_GUID_INFO(Structure):
    InstanceCount: UInt32
    Reserved: UInt32
class TRACE_GUID_PROPERTIES(Structure):
    Guid: Guid
    GuidType: UInt32
    LoggerId: UInt32
    EnableLevel: UInt32
    EnableFlags: UInt32
    IsEnable: Windows.Win32.Foundation.BOOLEAN
class TRACE_GUID_REGISTRATION(Structure):
    Guid: POINTER(Guid)
    RegHandle: Windows.Win32.Foundation.HANDLE
class TRACE_LOGFILE_HEADER(Structure):
    BufferSize: UInt32
    Anonymous1: _Anonymous1_e__Union
    ProviderVersion: UInt32
    NumberOfProcessors: UInt32
    EndTime: Windows.Win32.Foundation.LARGE_INTEGER
    TimerResolution: UInt32
    MaximumFileSize: UInt32
    LogFileMode: UInt32
    BuffersWritten: UInt32
    Anonymous2: _Anonymous2_e__Union
    LoggerName: Windows.Win32.Foundation.PWSTR
    LogFileName: Windows.Win32.Foundation.PWSTR
    TimeZone: Windows.Win32.System.Time.TIME_ZONE_INFORMATION
    BootTime: Windows.Win32.Foundation.LARGE_INTEGER
    PerfFreq: Windows.Win32.Foundation.LARGE_INTEGER
    StartTime: Windows.Win32.Foundation.LARGE_INTEGER
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
    EndTime: Windows.Win32.Foundation.LARGE_INTEGER
    TimerResolution: UInt32
    MaximumFileSize: UInt32
    LogFileMode: UInt32
    BuffersWritten: UInt32
    Anonymous2: _Anonymous2_e__Union
    LoggerName: UInt32
    LogFileName: UInt32
    TimeZone: Windows.Win32.System.Time.TIME_ZONE_INFORMATION
    BootTime: Windows.Win32.Foundation.LARGE_INTEGER
    PerfFreq: Windows.Win32.Foundation.LARGE_INTEGER
    StartTime: Windows.Win32.Foundation.LARGE_INTEGER
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
    EndTime: Windows.Win32.Foundation.LARGE_INTEGER
    TimerResolution: UInt32
    MaximumFileSize: UInt32
    LogFileMode: UInt32
    BuffersWritten: UInt32
    Anonymous2: _Anonymous2_e__Union
    LoggerName: UInt64
    LogFileName: UInt64
    TimeZone: Windows.Win32.System.Time.TIME_ZONE_INFORMATION
    BootTime: Windows.Win32.Foundation.LARGE_INTEGER
    PerfFreq: Windows.Win32.Foundation.LARGE_INTEGER
    StartTime: Windows.Win32.Foundation.LARGE_INTEGER
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
TRACE_MESSAGE_COMPONENTID: TRACE_MESSAGE_FLAGS = 4
TRACE_MESSAGE_GUID: TRACE_MESSAGE_FLAGS = 2
TRACE_MESSAGE_SEQUENCE: TRACE_MESSAGE_FLAGS = 1
TRACE_MESSAGE_SYSTEMINFO: TRACE_MESSAGE_FLAGS = 32
TRACE_MESSAGE_TIMESTAMP: TRACE_MESSAGE_FLAGS = 8
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
TRACE_QUERY_INFO_CLASS_TraceGuidQueryList: TRACE_QUERY_INFO_CLASS = 0
TRACE_QUERY_INFO_CLASS_TraceGuidQueryInfo: TRACE_QUERY_INFO_CLASS = 1
TRACE_QUERY_INFO_CLASS_TraceGuidQueryProcess: TRACE_QUERY_INFO_CLASS = 2
TRACE_QUERY_INFO_CLASS_TraceStackTracingInfo: TRACE_QUERY_INFO_CLASS = 3
TRACE_QUERY_INFO_CLASS_TraceSystemTraceEnableFlagsInfo: TRACE_QUERY_INFO_CLASS = 4
TRACE_QUERY_INFO_CLASS_TraceSampledProfileIntervalInfo: TRACE_QUERY_INFO_CLASS = 5
TRACE_QUERY_INFO_CLASS_TraceProfileSourceConfigInfo: TRACE_QUERY_INFO_CLASS = 6
TRACE_QUERY_INFO_CLASS_TraceProfileSourceListInfo: TRACE_QUERY_INFO_CLASS = 7
TRACE_QUERY_INFO_CLASS_TracePmcEventListInfo: TRACE_QUERY_INFO_CLASS = 8
TRACE_QUERY_INFO_CLASS_TracePmcCounterListInfo: TRACE_QUERY_INFO_CLASS = 9
TRACE_QUERY_INFO_CLASS_TraceSetDisallowList: TRACE_QUERY_INFO_CLASS = 10
TRACE_QUERY_INFO_CLASS_TraceVersionInfo: TRACE_QUERY_INFO_CLASS = 11
TRACE_QUERY_INFO_CLASS_TraceGroupQueryList: TRACE_QUERY_INFO_CLASS = 12
TRACE_QUERY_INFO_CLASS_TraceGroupQueryInfo: TRACE_QUERY_INFO_CLASS = 13
TRACE_QUERY_INFO_CLASS_TraceDisallowListQuery: TRACE_QUERY_INFO_CLASS = 14
TRACE_QUERY_INFO_CLASS_TraceInfoReserved15: TRACE_QUERY_INFO_CLASS = 15
TRACE_QUERY_INFO_CLASS_TracePeriodicCaptureStateListInfo: TRACE_QUERY_INFO_CLASS = 16
TRACE_QUERY_INFO_CLASS_TracePeriodicCaptureStateInfo: TRACE_QUERY_INFO_CLASS = 17
TRACE_QUERY_INFO_CLASS_TraceProviderBinaryTracking: TRACE_QUERY_INFO_CLASS = 18
TRACE_QUERY_INFO_CLASS_TraceMaxLoggersQuery: TRACE_QUERY_INFO_CLASS = 19
TRACE_QUERY_INFO_CLASS_TraceLbrConfigurationInfo: TRACE_QUERY_INFO_CLASS = 20
TRACE_QUERY_INFO_CLASS_TraceLbrEventListInfo: TRACE_QUERY_INFO_CLASS = 21
TRACE_QUERY_INFO_CLASS_TraceMaxPmcCounterQuery: TRACE_QUERY_INFO_CLASS = 22
TRACE_QUERY_INFO_CLASS_TraceStreamCount: TRACE_QUERY_INFO_CLASS = 23
TRACE_QUERY_INFO_CLASS_TraceStackCachingInfo: TRACE_QUERY_INFO_CLASS = 24
TRACE_QUERY_INFO_CLASS_TracePmcCounterOwners: TRACE_QUERY_INFO_CLASS = 25
TRACE_QUERY_INFO_CLASS_TraceUnifiedStackCachingInfo: TRACE_QUERY_INFO_CLASS = 26
TRACE_QUERY_INFO_CLASS_MaxTraceSetInfoClass: TRACE_QUERY_INFO_CLASS = 27
class TRACE_STACK_CACHING_INFO(Structure):
    Enabled: Windows.Win32.Foundation.BOOLEAN
    CacheSize: UInt32
    BucketCount: UInt32
class TRACE_VERSION_INFO(Structure):
    EtwTraceProcessingVersion: UInt32
    Reserved: UInt32
@winfunctype_pointer
def WMIDPREQUEST(RequestCode: Windows.Win32.System.Diagnostics.Etw.WMIDPREQUESTCODE, RequestContext: c_void_p, BufferSize: POINTER(UInt32), Buffer: c_void_p) -> UInt32: ...
WMIDPREQUESTCODE = Int32
WMI_GET_ALL_DATA: WMIDPREQUESTCODE = 0
WMI_GET_SINGLE_INSTANCE: WMIDPREQUESTCODE = 1
WMI_SET_SINGLE_INSTANCE: WMIDPREQUESTCODE = 2
WMI_SET_SINGLE_ITEM: WMIDPREQUESTCODE = 3
WMI_ENABLE_EVENTS: WMIDPREQUESTCODE = 4
WMI_DISABLE_EVENTS: WMIDPREQUESTCODE = 5
WMI_ENABLE_COLLECTION: WMIDPREQUESTCODE = 6
WMI_DISABLE_COLLECTION: WMIDPREQUESTCODE = 7
WMI_REGINFO: WMIDPREQUESTCODE = 8
WMI_EXECUTE_METHOD: WMIDPREQUESTCODE = 9
WMI_CAPTURE_STATE: WMIDPREQUESTCODE = 10
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
    WmiRegGuid: Windows.Win32.System.Diagnostics.Etw.WMIREGGUIDW * 1
class WNODE_ALL_DATA(Structure):
    WnodeHeader: Windows.Win32.System.Diagnostics.Etw.WNODE_HEADER
    DataBlockOffset: UInt32
    InstanceCount: UInt32
    OffsetInstanceNameOffsets: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        FixedInstanceSize: UInt32
        OffsetInstanceDataAndLength: Windows.Win32.System.Diagnostics.Etw.OFFSETINSTANCEDATAANDLENGTH * 1
class WNODE_EVENT_ITEM(Structure):
    WnodeHeader: Windows.Win32.System.Diagnostics.Etw.WNODE_HEADER
class WNODE_EVENT_REFERENCE(Structure):
    WnodeHeader: Windows.Win32.System.Diagnostics.Etw.WNODE_HEADER
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
        KernelHandle: Windows.Win32.Foundation.HANDLE
        TimeStamp: Windows.Win32.Foundation.LARGE_INTEGER
class WNODE_METHOD_ITEM(Structure):
    WnodeHeader: Windows.Win32.System.Diagnostics.Etw.WNODE_HEADER
    OffsetInstanceName: UInt32
    InstanceIndex: UInt32
    MethodId: UInt32
    DataBlockOffset: UInt32
    SizeDataBlock: UInt32
    VariableData: Byte * 1
class WNODE_SINGLE_INSTANCE(Structure):
    WnodeHeader: Windows.Win32.System.Diagnostics.Etw.WNODE_HEADER
    OffsetInstanceName: UInt32
    InstanceIndex: UInt32
    DataBlockOffset: UInt32
    SizeDataBlock: UInt32
    VariableData: Byte * 1
class WNODE_SINGLE_ITEM(Structure):
    WnodeHeader: Windows.Win32.System.Diagnostics.Etw.WNODE_HEADER
    OffsetInstanceName: UInt32
    InstanceIndex: UInt32
    ItemId: UInt32
    DataBlockOffset: UInt32
    SizeDataItem: UInt32
    VariableData: Byte * 1
class WNODE_TOO_SMALL(Structure):
    WnodeHeader: Windows.Win32.System.Diagnostics.Etw.WNODE_HEADER
    SizeNeeded: UInt32
_TDH_IN_TYPE = Int32
TDH_INTYPE_NULL: _TDH_IN_TYPE = 0
TDH_INTYPE_UNICODESTRING: _TDH_IN_TYPE = 1
TDH_INTYPE_ANSISTRING: _TDH_IN_TYPE = 2
TDH_INTYPE_INT8: _TDH_IN_TYPE = 3
TDH_INTYPE_UINT8: _TDH_IN_TYPE = 4
TDH_INTYPE_INT16: _TDH_IN_TYPE = 5
TDH_INTYPE_UINT16: _TDH_IN_TYPE = 6
TDH_INTYPE_INT32: _TDH_IN_TYPE = 7
TDH_INTYPE_UINT32: _TDH_IN_TYPE = 8
TDH_INTYPE_INT64: _TDH_IN_TYPE = 9
TDH_INTYPE_UINT64: _TDH_IN_TYPE = 10
TDH_INTYPE_FLOAT: _TDH_IN_TYPE = 11
TDH_INTYPE_DOUBLE: _TDH_IN_TYPE = 12
TDH_INTYPE_BOOLEAN: _TDH_IN_TYPE = 13
TDH_INTYPE_BINARY: _TDH_IN_TYPE = 14
TDH_INTYPE_GUID: _TDH_IN_TYPE = 15
TDH_INTYPE_POINTER: _TDH_IN_TYPE = 16
TDH_INTYPE_FILETIME: _TDH_IN_TYPE = 17
TDH_INTYPE_SYSTEMTIME: _TDH_IN_TYPE = 18
TDH_INTYPE_SID: _TDH_IN_TYPE = 19
TDH_INTYPE_HEXINT32: _TDH_IN_TYPE = 20
TDH_INTYPE_HEXINT64: _TDH_IN_TYPE = 21
TDH_INTYPE_MANIFEST_COUNTEDSTRING: _TDH_IN_TYPE = 22
TDH_INTYPE_MANIFEST_COUNTEDANSISTRING: _TDH_IN_TYPE = 23
TDH_INTYPE_RESERVED24: _TDH_IN_TYPE = 24
TDH_INTYPE_MANIFEST_COUNTEDBINARY: _TDH_IN_TYPE = 25
TDH_INTYPE_COUNTEDSTRING: _TDH_IN_TYPE = 300
TDH_INTYPE_COUNTEDANSISTRING: _TDH_IN_TYPE = 301
TDH_INTYPE_REVERSEDCOUNTEDSTRING: _TDH_IN_TYPE = 302
TDH_INTYPE_REVERSEDCOUNTEDANSISTRING: _TDH_IN_TYPE = 303
TDH_INTYPE_NONNULLTERMINATEDSTRING: _TDH_IN_TYPE = 304
TDH_INTYPE_NONNULLTERMINATEDANSISTRING: _TDH_IN_TYPE = 305
TDH_INTYPE_UNICODECHAR: _TDH_IN_TYPE = 306
TDH_INTYPE_ANSICHAR: _TDH_IN_TYPE = 307
TDH_INTYPE_SIZET: _TDH_IN_TYPE = 308
TDH_INTYPE_HEXDUMP: _TDH_IN_TYPE = 309
TDH_INTYPE_WBEMSID: _TDH_IN_TYPE = 310
_TDH_OUT_TYPE = Int32
TDH_OUTTYPE_NULL: _TDH_OUT_TYPE = 0
TDH_OUTTYPE_STRING: _TDH_OUT_TYPE = 1
TDH_OUTTYPE_DATETIME: _TDH_OUT_TYPE = 2
TDH_OUTTYPE_BYTE: _TDH_OUT_TYPE = 3
TDH_OUTTYPE_UNSIGNEDBYTE: _TDH_OUT_TYPE = 4
TDH_OUTTYPE_SHORT: _TDH_OUT_TYPE = 5
TDH_OUTTYPE_UNSIGNEDSHORT: _TDH_OUT_TYPE = 6
TDH_OUTTYPE_INT: _TDH_OUT_TYPE = 7
TDH_OUTTYPE_UNSIGNEDINT: _TDH_OUT_TYPE = 8
TDH_OUTTYPE_LONG: _TDH_OUT_TYPE = 9
TDH_OUTTYPE_UNSIGNEDLONG: _TDH_OUT_TYPE = 10
TDH_OUTTYPE_FLOAT: _TDH_OUT_TYPE = 11
TDH_OUTTYPE_DOUBLE: _TDH_OUT_TYPE = 12
TDH_OUTTYPE_BOOLEAN: _TDH_OUT_TYPE = 13
TDH_OUTTYPE_GUID: _TDH_OUT_TYPE = 14
TDH_OUTTYPE_HEXBINARY: _TDH_OUT_TYPE = 15
TDH_OUTTYPE_HEXINT8: _TDH_OUT_TYPE = 16
TDH_OUTTYPE_HEXINT16: _TDH_OUT_TYPE = 17
TDH_OUTTYPE_HEXINT32: _TDH_OUT_TYPE = 18
TDH_OUTTYPE_HEXINT64: _TDH_OUT_TYPE = 19
TDH_OUTTYPE_PID: _TDH_OUT_TYPE = 20
TDH_OUTTYPE_TID: _TDH_OUT_TYPE = 21
TDH_OUTTYPE_PORT: _TDH_OUT_TYPE = 22
TDH_OUTTYPE_IPV4: _TDH_OUT_TYPE = 23
TDH_OUTTYPE_IPV6: _TDH_OUT_TYPE = 24
TDH_OUTTYPE_SOCKETADDRESS: _TDH_OUT_TYPE = 25
TDH_OUTTYPE_CIMDATETIME: _TDH_OUT_TYPE = 26
TDH_OUTTYPE_ETWTIME: _TDH_OUT_TYPE = 27
TDH_OUTTYPE_XML: _TDH_OUT_TYPE = 28
TDH_OUTTYPE_ERRORCODE: _TDH_OUT_TYPE = 29
TDH_OUTTYPE_WIN32ERROR: _TDH_OUT_TYPE = 30
TDH_OUTTYPE_NTSTATUS: _TDH_OUT_TYPE = 31
TDH_OUTTYPE_HRESULT: _TDH_OUT_TYPE = 32
TDH_OUTTYPE_CULTURE_INSENSITIVE_DATETIME: _TDH_OUT_TYPE = 33
TDH_OUTTYPE_JSON: _TDH_OUT_TYPE = 34
TDH_OUTTYPE_UTF8: _TDH_OUT_TYPE = 35
TDH_OUTTYPE_PKCS7_WITH_TYPE_INFO: _TDH_OUT_TYPE = 36
TDH_OUTTYPE_CODE_POINTER: _TDH_OUT_TYPE = 37
TDH_OUTTYPE_DATETIME_UTC: _TDH_OUT_TYPE = 38
TDH_OUTTYPE_REDUCEDSTRING: _TDH_OUT_TYPE = 300
TDH_OUTTYPE_NOPRINT: _TDH_OUT_TYPE = 301
make_head(_module, 'CLASSIC_EVENT_ID')
make_head(_module, 'ENABLE_TRACE_PARAMETERS')
make_head(_module, 'ENABLE_TRACE_PARAMETERS_V1')
make_head(_module, 'ETW_BUFFER_CONTEXT')
make_head(_module, 'ETW_PMC_COUNTER_OWNER')
make_head(_module, 'ETW_PMC_COUNTER_OWNERSHIP_STATUS')
make_head(_module, 'ETW_TRACE_PARTITION_INFORMATION')
make_head(_module, 'ETW_TRACE_PARTITION_INFORMATION_V2')
make_head(_module, 'EVENT_DATA_DESCRIPTOR')
make_head(_module, 'EVENT_DESCRIPTOR')
make_head(_module, 'EVENT_EXTENDED_ITEM_EVENT_KEY')
make_head(_module, 'EVENT_EXTENDED_ITEM_INSTANCE')
make_head(_module, 'EVENT_EXTENDED_ITEM_PEBS_INDEX')
make_head(_module, 'EVENT_EXTENDED_ITEM_PMC_COUNTERS')
make_head(_module, 'EVENT_EXTENDED_ITEM_PROCESS_START_KEY')
make_head(_module, 'EVENT_EXTENDED_ITEM_RELATED_ACTIVITYID')
make_head(_module, 'EVENT_EXTENDED_ITEM_STACK_KEY32')
make_head(_module, 'EVENT_EXTENDED_ITEM_STACK_KEY64')
make_head(_module, 'EVENT_EXTENDED_ITEM_STACK_TRACE32')
make_head(_module, 'EVENT_EXTENDED_ITEM_STACK_TRACE64')
make_head(_module, 'EVENT_EXTENDED_ITEM_TS_ID')
make_head(_module, 'EVENT_FILTER_DESCRIPTOR')
make_head(_module, 'EVENT_FILTER_EVENT_ID')
make_head(_module, 'EVENT_FILTER_EVENT_NAME')
make_head(_module, 'EVENT_FILTER_HEADER')
make_head(_module, 'EVENT_FILTER_LEVEL_KW')
make_head(_module, 'EVENT_HEADER')
make_head(_module, 'EVENT_HEADER_EXTENDED_DATA_ITEM')
make_head(_module, 'EVENT_INSTANCE_HEADER')
make_head(_module, 'EVENT_INSTANCE_INFO')
make_head(_module, 'EVENT_MAP_ENTRY')
make_head(_module, 'EVENT_MAP_INFO')
make_head(_module, 'EVENT_PROPERTY_INFO')
make_head(_module, 'EVENT_RECORD')
make_head(_module, 'EVENT_TRACE')
make_head(_module, 'EVENT_TRACE_HEADER')
make_head(_module, 'EVENT_TRACE_LOGFILEA')
make_head(_module, 'EVENT_TRACE_LOGFILEW')
make_head(_module, 'EVENT_TRACE_PROPERTIES')
make_head(_module, 'EVENT_TRACE_PROPERTIES_V2')
make_head(_module, 'ITraceEvent')
make_head(_module, 'ITraceEventCallback')
make_head(_module, 'ITraceRelogger')
make_head(_module, 'MOF_FIELD')
make_head(_module, 'OFFSETINSTANCEDATAANDLENGTH')
make_head(_module, 'PAYLOAD_FILTER_PREDICATE')
make_head(_module, 'PENABLECALLBACK')
make_head(_module, 'PEVENT_CALLBACK')
make_head(_module, 'PEVENT_RECORD_CALLBACK')
make_head(_module, 'PEVENT_TRACE_BUFFER_CALLBACKA')
make_head(_module, 'PEVENT_TRACE_BUFFER_CALLBACKW')
make_head(_module, 'PROFILE_SOURCE_INFO')
make_head(_module, 'PROPERTY_DATA_DESCRIPTOR')
make_head(_module, 'PROVIDER_ENUMERATION_INFO')
make_head(_module, 'PROVIDER_EVENT_INFO')
make_head(_module, 'PROVIDER_FIELD_INFO')
make_head(_module, 'PROVIDER_FIELD_INFOARRAY')
make_head(_module, 'PROVIDER_FILTER_INFO')
make_head(_module, 'TDH_CONTEXT')
make_head(_module, 'TRACE_ENABLE_INFO')
make_head(_module, 'TRACE_EVENT_INFO')
make_head(_module, 'TRACE_GUID_INFO')
make_head(_module, 'TRACE_GUID_PROPERTIES')
make_head(_module, 'TRACE_GUID_REGISTRATION')
make_head(_module, 'TRACE_LOGFILE_HEADER')
make_head(_module, 'TRACE_LOGFILE_HEADER32')
make_head(_module, 'TRACE_LOGFILE_HEADER64')
make_head(_module, 'TRACE_PERIODIC_CAPTURE_STATE_INFO')
make_head(_module, 'TRACE_PROFILE_INTERVAL')
make_head(_module, 'TRACE_PROVIDER_INFO')
make_head(_module, 'TRACE_PROVIDER_INSTANCE_INFO')
make_head(_module, 'TRACE_STACK_CACHING_INFO')
make_head(_module, 'TRACE_VERSION_INFO')
make_head(_module, 'WMIDPREQUEST')
make_head(_module, 'WMIREGGUIDW')
make_head(_module, 'WMIREGINFOW')
make_head(_module, 'WNODE_ALL_DATA')
make_head(_module, 'WNODE_EVENT_ITEM')
make_head(_module, 'WNODE_EVENT_REFERENCE')
make_head(_module, 'WNODE_HEADER')
make_head(_module, 'WNODE_METHOD_ITEM')
make_head(_module, 'WNODE_SINGLE_INSTANCE')
make_head(_module, 'WNODE_SINGLE_ITEM')
make_head(_module, 'WNODE_TOO_SMALL')
__all__ = [
    "ALPCGuid",
    "CLASSIC_EVENT_ID",
    "CLSID_TraceRelogger",
    "CONTROLTRACE_HANDLE",
    "CTraceRelogger",
    "CloseTrace",
    "ControlTraceA",
    "ControlTraceW",
    "CreateTraceInstanceId",
    "CveEventWrite",
    "DECODING_SOURCE",
    "DECODING_SOURCE_DecodingSourceMax",
    "DECODING_SOURCE_DecodingSourceTlg",
    "DECODING_SOURCE_DecodingSourceWPP",
    "DECODING_SOURCE_DecodingSourceWbem",
    "DECODING_SOURCE_DecodingSourceXMLFile",
    "DIAG_LOGGER_NAMEA",
    "DIAG_LOGGER_NAMEW",
    "DefaultTraceSecurityGuid",
    "DiskIoGuid",
    "ENABLECALLBACK_ENABLED_STATE",
    "ENABLE_TRACE_PARAMETERS",
    "ENABLE_TRACE_PARAMETERS_V1",
    "ENABLE_TRACE_PARAMETERS_VERSION",
    "ENABLE_TRACE_PARAMETERS_VERSION_2",
    "ETW_ASCIICHAR_TYPE_VALUE",
    "ETW_ASCIISTRING_TYPE_VALUE",
    "ETW_BOOLEAN_TYPE_VALUE",
    "ETW_BOOL_TYPE_VALUE",
    "ETW_BUFFER_CONTEXT",
    "ETW_BYTE_TYPE_VALUE",
    "ETW_CHAR_TYPE_VALUE",
    "ETW_COMPRESSION_RESUMPTION_MODE",
    "ETW_COMPRESSION_RESUMPTION_MODE_EtwCompressionModeNoDisable",
    "ETW_COMPRESSION_RESUMPTION_MODE_EtwCompressionModeNoRestart",
    "ETW_COMPRESSION_RESUMPTION_MODE_EtwCompressionModeRestart",
    "ETW_COUNTED_ANSISTRING_TYPE_VALUE",
    "ETW_COUNTED_STRING_TYPE_VALUE",
    "ETW_DATETIME_TYPE_VALUE",
    "ETW_DECIMAL_TYPE_VALUE",
    "ETW_DOUBLE_TYPE_VALUE",
    "ETW_GUID_TYPE_VALUE",
    "ETW_HIDDEN_TYPE_VALUE",
    "ETW_INT16_TYPE_VALUE",
    "ETW_INT32_TYPE_VALUE",
    "ETW_INT64_TYPE_VALUE",
    "ETW_NON_NULL_TERMINATED_STRING_TYPE_VALUE",
    "ETW_NULL_TYPE_VALUE",
    "ETW_OBJECT_TYPE_VALUE",
    "ETW_PMC_COUNTER_OWNER",
    "ETW_PMC_COUNTER_OWNERSHIP_STATUS",
    "ETW_PMC_COUNTER_OWNER_TYPE",
    "ETW_PMC_COUNTER_OWNER_TYPE_EtwPmcOwnerFree",
    "ETW_PMC_COUNTER_OWNER_TYPE_EtwPmcOwnerTagged",
    "ETW_PMC_COUNTER_OWNER_TYPE_EtwPmcOwnerTaggedWithSource",
    "ETW_PMC_COUNTER_OWNER_TYPE_EtwPmcOwnerUntagged",
    "ETW_POINTER_TYPE_VALUE",
    "ETW_PROCESS_HANDLE_INFO_TYPE",
    "ETW_PROCESS_HANDLE_INFO_TYPE_EtwQueryLastDroppedTimes",
    "ETW_PROCESS_HANDLE_INFO_TYPE_EtwQueryPartitionInformation",
    "ETW_PROCESS_HANDLE_INFO_TYPE_EtwQueryPartitionInformationV2",
    "ETW_PROCESS_HANDLE_INFO_TYPE_EtwQueryProcessHandleInfoMax",
    "ETW_PROVIDER_TRAIT_TYPE",
    "ETW_PROVIDER_TRAIT_TYPE_EtwProviderTraitDecodeGuid",
    "ETW_PROVIDER_TRAIT_TYPE_EtwProviderTraitTypeGroup",
    "ETW_PROVIDER_TRAIT_TYPE_EtwProviderTraitTypeMax",
    "ETW_PTVECTOR_TYPE_VALUE",
    "ETW_REDUCED_ANSISTRING_TYPE_VALUE",
    "ETW_REDUCED_STRING_TYPE_VALUE",
    "ETW_REFRENCE_TYPE_VALUE",
    "ETW_REVERSED_COUNTED_ANSISTRING_TYPE_VALUE",
    "ETW_REVERSED_COUNTED_STRING_TYPE_VALUE",
    "ETW_SBYTE_TYPE_VALUE",
    "ETW_SID_TYPE_VALUE",
    "ETW_SINGLE_TYPE_VALUE",
    "ETW_SIZET_TYPE_VALUE",
    "ETW_STRING_TYPE_VALUE",
    "ETW_TRACE_PARTITION_INFORMATION",
    "ETW_TRACE_PARTITION_INFORMATION_V2",
    "ETW_UINT16_TYPE_VALUE",
    "ETW_UINT32_TYPE_VALUE",
    "ETW_UINT64_TYPE_VALUE",
    "ETW_VARIANT_TYPE_VALUE",
    "ETW_WMITIME_TYPE_VALUE",
    "EVENTMAP_ENTRY_VALUETYPE_STRING",
    "EVENTMAP_ENTRY_VALUETYPE_ULONG",
    "EVENTMAP_INFO_FLAG_MANIFEST_BITMAP",
    "EVENTMAP_INFO_FLAG_MANIFEST_PATTERNMAP",
    "EVENTMAP_INFO_FLAG_MANIFEST_VALUEMAP",
    "EVENTMAP_INFO_FLAG_WBEM_BITMAP",
    "EVENTMAP_INFO_FLAG_WBEM_FLAG",
    "EVENTMAP_INFO_FLAG_WBEM_NO_MAP",
    "EVENTMAP_INFO_FLAG_WBEM_VALUEMAP",
    "EVENTSECURITYOPERATION",
    "EVENTSECURITYOPERATION_EventSecurityAddDACL",
    "EVENTSECURITYOPERATION_EventSecurityAddSACL",
    "EVENTSECURITYOPERATION_EventSecurityMax",
    "EVENTSECURITYOPERATION_EventSecuritySetDACL",
    "EVENTSECURITYOPERATION_EventSecuritySetSACL",
    "EVENT_ACTIVITY_CTRL_CREATE_ID",
    "EVENT_ACTIVITY_CTRL_CREATE_SET_ID",
    "EVENT_ACTIVITY_CTRL_GET_ID",
    "EVENT_ACTIVITY_CTRL_GET_SET_ID",
    "EVENT_ACTIVITY_CTRL_SET_ID",
    "EVENT_CONTROL_CODE_CAPTURE_STATE",
    "EVENT_CONTROL_CODE_DISABLE_PROVIDER",
    "EVENT_CONTROL_CODE_ENABLE_PROVIDER",
    "EVENT_DATA_DESCRIPTOR",
    "EVENT_DATA_DESCRIPTOR_TYPE_EVENT_METADATA",
    "EVENT_DATA_DESCRIPTOR_TYPE_NONE",
    "EVENT_DATA_DESCRIPTOR_TYPE_PROVIDER_METADATA",
    "EVENT_DATA_DESCRIPTOR_TYPE_TIMESTAMP_OVERRIDE",
    "EVENT_DESCRIPTOR",
    "EVENT_ENABLE_PROPERTY_ENABLE_KEYWORD_0",
    "EVENT_ENABLE_PROPERTY_ENABLE_SILOS",
    "EVENT_ENABLE_PROPERTY_EVENT_KEY",
    "EVENT_ENABLE_PROPERTY_EXCLUDE_INPRIVATE",
    "EVENT_ENABLE_PROPERTY_IGNORE_KEYWORD_0",
    "EVENT_ENABLE_PROPERTY_PROCESS_START_KEY",
    "EVENT_ENABLE_PROPERTY_PROVIDER_GROUP",
    "EVENT_ENABLE_PROPERTY_PSM_KEY",
    "EVENT_ENABLE_PROPERTY_SID",
    "EVENT_ENABLE_PROPERTY_SOURCE_CONTAINER_TRACKING",
    "EVENT_ENABLE_PROPERTY_STACK_TRACE",
    "EVENT_ENABLE_PROPERTY_TS_ID",
    "EVENT_EXTENDED_ITEM_EVENT_KEY",
    "EVENT_EXTENDED_ITEM_INSTANCE",
    "EVENT_EXTENDED_ITEM_PEBS_INDEX",
    "EVENT_EXTENDED_ITEM_PMC_COUNTERS",
    "EVENT_EXTENDED_ITEM_PROCESS_START_KEY",
    "EVENT_EXTENDED_ITEM_RELATED_ACTIVITYID",
    "EVENT_EXTENDED_ITEM_STACK_KEY32",
    "EVENT_EXTENDED_ITEM_STACK_KEY64",
    "EVENT_EXTENDED_ITEM_STACK_TRACE32",
    "EVENT_EXTENDED_ITEM_STACK_TRACE64",
    "EVENT_EXTENDED_ITEM_TS_ID",
    "EVENT_FIELD_TYPE",
    "EVENT_FIELD_TYPE_EventChannelInformation",
    "EVENT_FIELD_TYPE_EventInformationMax",
    "EVENT_FIELD_TYPE_EventKeywordInformation",
    "EVENT_FIELD_TYPE_EventLevelInformation",
    "EVENT_FIELD_TYPE_EventOpcodeInformation",
    "EVENT_FIELD_TYPE_EventTaskInformation",
    "EVENT_FILTER_DESCRIPTOR",
    "EVENT_FILTER_EVENT_ID",
    "EVENT_FILTER_EVENT_NAME",
    "EVENT_FILTER_HEADER",
    "EVENT_FILTER_LEVEL_KW",
    "EVENT_FILTER_TYPE_CONTAINER",
    "EVENT_FILTER_TYPE_EVENT_ID",
    "EVENT_FILTER_TYPE_EVENT_NAME",
    "EVENT_FILTER_TYPE_EXECUTABLE_NAME",
    "EVENT_FILTER_TYPE_NONE",
    "EVENT_FILTER_TYPE_PACKAGE_APP_ID",
    "EVENT_FILTER_TYPE_PACKAGE_ID",
    "EVENT_FILTER_TYPE_PAYLOAD",
    "EVENT_FILTER_TYPE_PID",
    "EVENT_FILTER_TYPE_SCHEMATIZED",
    "EVENT_FILTER_TYPE_STACKWALK",
    "EVENT_FILTER_TYPE_STACKWALK_LEVEL_KW",
    "EVENT_FILTER_TYPE_STACKWALK_NAME",
    "EVENT_FILTER_TYPE_SYSTEM_FLAGS",
    "EVENT_FILTER_TYPE_TRACEHANDLE",
    "EVENT_HEADER",
    "EVENT_HEADER_EXTENDED_DATA_ITEM",
    "EVENT_HEADER_EXT_TYPE_CONTAINER_ID",
    "EVENT_HEADER_EXT_TYPE_CONTROL_GUID",
    "EVENT_HEADER_EXT_TYPE_EVENT_KEY",
    "EVENT_HEADER_EXT_TYPE_EVENT_SCHEMA_TL",
    "EVENT_HEADER_EXT_TYPE_INSTANCE_INFO",
    "EVENT_HEADER_EXT_TYPE_MAX",
    "EVENT_HEADER_EXT_TYPE_PEBS_INDEX",
    "EVENT_HEADER_EXT_TYPE_PMC_COUNTERS",
    "EVENT_HEADER_EXT_TYPE_PROCESS_START_KEY",
    "EVENT_HEADER_EXT_TYPE_PROV_TRAITS",
    "EVENT_HEADER_EXT_TYPE_PSM_KEY",
    "EVENT_HEADER_EXT_TYPE_QPC_DELTA",
    "EVENT_HEADER_EXT_TYPE_RELATED_ACTIVITYID",
    "EVENT_HEADER_EXT_TYPE_SID",
    "EVENT_HEADER_EXT_TYPE_STACK_KEY32",
    "EVENT_HEADER_EXT_TYPE_STACK_KEY64",
    "EVENT_HEADER_EXT_TYPE_STACK_TRACE32",
    "EVENT_HEADER_EXT_TYPE_STACK_TRACE64",
    "EVENT_HEADER_EXT_TYPE_TS_ID",
    "EVENT_HEADER_FLAG_32_BIT_HEADER",
    "EVENT_HEADER_FLAG_64_BIT_HEADER",
    "EVENT_HEADER_FLAG_CLASSIC_HEADER",
    "EVENT_HEADER_FLAG_DECODE_GUID",
    "EVENT_HEADER_FLAG_EXTENDED_INFO",
    "EVENT_HEADER_FLAG_NO_CPUTIME",
    "EVENT_HEADER_FLAG_PRIVATE_SESSION",
    "EVENT_HEADER_FLAG_PROCESSOR_INDEX",
    "EVENT_HEADER_FLAG_STRING_ONLY",
    "EVENT_HEADER_FLAG_TRACE_MESSAGE",
    "EVENT_HEADER_PROPERTY_FORWARDED_XML",
    "EVENT_HEADER_PROPERTY_LEGACY_EVENTLOG",
    "EVENT_HEADER_PROPERTY_RELOGGABLE",
    "EVENT_HEADER_PROPERTY_XML",
    "EVENT_INFO_CLASS",
    "EVENT_INFO_CLASS_EventProviderBinaryTrackInfo",
    "EVENT_INFO_CLASS_EventProviderSetReserved1",
    "EVENT_INFO_CLASS_EventProviderSetTraits",
    "EVENT_INFO_CLASS_EventProviderUseDescriptorType",
    "EVENT_INFO_CLASS_MaxEventInfo",
    "EVENT_INSTANCE_HEADER",
    "EVENT_INSTANCE_INFO",
    "EVENT_LOGGER_NAME",
    "EVENT_LOGGER_NAMEA",
    "EVENT_LOGGER_NAMEW",
    "EVENT_MAP_ENTRY",
    "EVENT_MAP_INFO",
    "EVENT_MAX_LEVEL",
    "EVENT_MIN_LEVEL",
    "EVENT_PROPERTY_INFO",
    "EVENT_RECORD",
    "EVENT_TRACE",
    "EVENT_TRACE_ADDTO_TRIAGE_DUMP",
    "EVENT_TRACE_ADD_HEADER_MODE",
    "EVENT_TRACE_BUFFERING_MODE",
    "EVENT_TRACE_COMPRESSED_MODE",
    "EVENT_TRACE_CONTROL",
    "EVENT_TRACE_CONTROL_CONVERT_TO_REALTIME",
    "EVENT_TRACE_CONTROL_FLUSH",
    "EVENT_TRACE_CONTROL_INCREMENT_FILE",
    "EVENT_TRACE_CONTROL_QUERY",
    "EVENT_TRACE_CONTROL_STOP",
    "EVENT_TRACE_CONTROL_UPDATE",
    "EVENT_TRACE_DELAY_OPEN_FILE_MODE",
    "EVENT_TRACE_FILE_MODE_APPEND",
    "EVENT_TRACE_FILE_MODE_CIRCULAR",
    "EVENT_TRACE_FILE_MODE_NEWFILE",
    "EVENT_TRACE_FILE_MODE_NONE",
    "EVENT_TRACE_FILE_MODE_PREALLOCATE",
    "EVENT_TRACE_FILE_MODE_SEQUENTIAL",
    "EVENT_TRACE_FLAG",
    "EVENT_TRACE_FLAG_ALPC",
    "EVENT_TRACE_FLAG_CSWITCH",
    "EVENT_TRACE_FLAG_DBGPRINT",
    "EVENT_TRACE_FLAG_DEBUG_EVENTS",
    "EVENT_TRACE_FLAG_DISK_FILE_IO",
    "EVENT_TRACE_FLAG_DISK_IO",
    "EVENT_TRACE_FLAG_DISK_IO_INIT",
    "EVENT_TRACE_FLAG_DISPATCHER",
    "EVENT_TRACE_FLAG_DPC",
    "EVENT_TRACE_FLAG_DRIVER",
    "EVENT_TRACE_FLAG_ENABLE_RESERVE",
    "EVENT_TRACE_FLAG_EXTENSION",
    "EVENT_TRACE_FLAG_FILE_IO",
    "EVENT_TRACE_FLAG_FILE_IO_INIT",
    "EVENT_TRACE_FLAG_FORWARD_WMI",
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
    "EVENT_TRACE_HEADER",
    "EVENT_TRACE_INDEPENDENT_SESSION_MODE",
    "EVENT_TRACE_LOGFILEA",
    "EVENT_TRACE_LOGFILEW",
    "EVENT_TRACE_MODE_RESERVED",
    "EVENT_TRACE_NONSTOPPABLE_MODE",
    "EVENT_TRACE_NO_PER_PROCESSOR_BUFFERING",
    "EVENT_TRACE_PERSIST_ON_HYBRID_SHUTDOWN",
    "EVENT_TRACE_PRIVATE_IN_PROC",
    "EVENT_TRACE_PRIVATE_LOGGER_MODE",
    "EVENT_TRACE_PROPERTIES",
    "EVENT_TRACE_PROPERTIES_V2",
    "EVENT_TRACE_REAL_TIME_MODE",
    "EVENT_TRACE_RELOG_MODE",
    "EVENT_TRACE_SECURE_MODE",
    "EVENT_TRACE_STOP_ON_HYBRID_SHUTDOWN",
    "EVENT_TRACE_SYSTEM_LOGGER_MODE",
    "EVENT_TRACE_TYPE_ACCEPT",
    "EVENT_TRACE_TYPE_ACKDUP",
    "EVENT_TRACE_TYPE_ACKFULL",
    "EVENT_TRACE_TYPE_ACKPART",
    "EVENT_TRACE_TYPE_CHECKPOINT",
    "EVENT_TRACE_TYPE_CONFIG",
    "EVENT_TRACE_TYPE_CONFIG_BOOT",
    "EVENT_TRACE_TYPE_CONFIG_CI_INFO",
    "EVENT_TRACE_TYPE_CONFIG_CPU",
    "EVENT_TRACE_TYPE_CONFIG_DEFRAG",
    "EVENT_TRACE_TYPE_CONFIG_DEVICEFAMILY",
    "EVENT_TRACE_TYPE_CONFIG_DPI",
    "EVENT_TRACE_TYPE_CONFIG_FLIGHTID",
    "EVENT_TRACE_TYPE_CONFIG_IDECHANNEL",
    "EVENT_TRACE_TYPE_CONFIG_IRQ",
    "EVENT_TRACE_TYPE_CONFIG_LOGICALDISK",
    "EVENT_TRACE_TYPE_CONFIG_MACHINEID",
    "EVENT_TRACE_TYPE_CONFIG_MOBILEPLATFORM",
    "EVENT_TRACE_TYPE_CONFIG_NETINFO",
    "EVENT_TRACE_TYPE_CONFIG_NIC",
    "EVENT_TRACE_TYPE_CONFIG_NUMANODE",
    "EVENT_TRACE_TYPE_CONFIG_OPTICALMEDIA",
    "EVENT_TRACE_TYPE_CONFIG_PHYSICALDISK",
    "EVENT_TRACE_TYPE_CONFIG_PLATFORM",
    "EVENT_TRACE_TYPE_CONFIG_PNP",
    "EVENT_TRACE_TYPE_CONFIG_POWER",
    "EVENT_TRACE_TYPE_CONFIG_PROCESSOR",
    "EVENT_TRACE_TYPE_CONFIG_PROCESSORGROUP",
    "EVENT_TRACE_TYPE_CONFIG_PROCESSORNUMBER",
    "EVENT_TRACE_TYPE_CONFIG_SERVICES",
    "EVENT_TRACE_TYPE_CONFIG_VIDEO",
    "EVENT_TRACE_TYPE_CONFIG_VIRTUALIZATION",
    "EVENT_TRACE_TYPE_CONNECT",
    "EVENT_TRACE_TYPE_CONNFAIL",
    "EVENT_TRACE_TYPE_COPY_ARP",
    "EVENT_TRACE_TYPE_COPY_TCP",
    "EVENT_TRACE_TYPE_DBGID_RSDS",
    "EVENT_TRACE_TYPE_DC_END",
    "EVENT_TRACE_TYPE_DC_START",
    "EVENT_TRACE_TYPE_DEQUEUE",
    "EVENT_TRACE_TYPE_DISCONNECT",
    "EVENT_TRACE_TYPE_END",
    "EVENT_TRACE_TYPE_EXTENSION",
    "EVENT_TRACE_TYPE_FLT_POSTOP_COMPLETION",
    "EVENT_TRACE_TYPE_FLT_POSTOP_FAILURE",
    "EVENT_TRACE_TYPE_FLT_POSTOP_INIT",
    "EVENT_TRACE_TYPE_FLT_PREOP_COMPLETION",
    "EVENT_TRACE_TYPE_FLT_PREOP_FAILURE",
    "EVENT_TRACE_TYPE_FLT_PREOP_INIT",
    "EVENT_TRACE_TYPE_GUIDMAP",
    "EVENT_TRACE_TYPE_INFO",
    "EVENT_TRACE_TYPE_IO_FLUSH",
    "EVENT_TRACE_TYPE_IO_FLUSH_INIT",
    "EVENT_TRACE_TYPE_IO_READ",
    "EVENT_TRACE_TYPE_IO_READ_INIT",
    "EVENT_TRACE_TYPE_IO_REDIRECTED_INIT",
    "EVENT_TRACE_TYPE_IO_WRITE",
    "EVENT_TRACE_TYPE_IO_WRITE_INIT",
    "EVENT_TRACE_TYPE_LOAD",
    "EVENT_TRACE_TYPE_MM_AV",
    "EVENT_TRACE_TYPE_MM_COW",
    "EVENT_TRACE_TYPE_MM_DZF",
    "EVENT_TRACE_TYPE_MM_GPF",
    "EVENT_TRACE_TYPE_MM_HPF",
    "EVENT_TRACE_TYPE_MM_TF",
    "EVENT_TRACE_TYPE_OPTICAL_IO_FLUSH",
    "EVENT_TRACE_TYPE_OPTICAL_IO_FLUSH_INIT",
    "EVENT_TRACE_TYPE_OPTICAL_IO_READ",
    "EVENT_TRACE_TYPE_OPTICAL_IO_READ_INIT",
    "EVENT_TRACE_TYPE_OPTICAL_IO_WRITE",
    "EVENT_TRACE_TYPE_OPTICAL_IO_WRITE_INIT",
    "EVENT_TRACE_TYPE_RECEIVE",
    "EVENT_TRACE_TYPE_RECONNECT",
    "EVENT_TRACE_TYPE_REGCLOSE",
    "EVENT_TRACE_TYPE_REGCOMMIT",
    "EVENT_TRACE_TYPE_REGCREATE",
    "EVENT_TRACE_TYPE_REGDELETE",
    "EVENT_TRACE_TYPE_REGDELETEVALUE",
    "EVENT_TRACE_TYPE_REGENUMERATEKEY",
    "EVENT_TRACE_TYPE_REGENUMERATEVALUEKEY",
    "EVENT_TRACE_TYPE_REGFLUSH",
    "EVENT_TRACE_TYPE_REGKCBCREATE",
    "EVENT_TRACE_TYPE_REGKCBDELETE",
    "EVENT_TRACE_TYPE_REGKCBRUNDOWNBEGIN",
    "EVENT_TRACE_TYPE_REGKCBRUNDOWNEND",
    "EVENT_TRACE_TYPE_REGMOUNTHIVE",
    "EVENT_TRACE_TYPE_REGOPEN",
    "EVENT_TRACE_TYPE_REGPREPARE",
    "EVENT_TRACE_TYPE_REGQUERY",
    "EVENT_TRACE_TYPE_REGQUERYMULTIPLEVALUE",
    "EVENT_TRACE_TYPE_REGQUERYSECURITY",
    "EVENT_TRACE_TYPE_REGQUERYVALUE",
    "EVENT_TRACE_TYPE_REGROLLBACK",
    "EVENT_TRACE_TYPE_REGSETINFORMATION",
    "EVENT_TRACE_TYPE_REGSETSECURITY",
    "EVENT_TRACE_TYPE_REGSETVALUE",
    "EVENT_TRACE_TYPE_REGVIRTUALIZE",
    "EVENT_TRACE_TYPE_REPLY",
    "EVENT_TRACE_TYPE_RESUME",
    "EVENT_TRACE_TYPE_RETRANSMIT",
    "EVENT_TRACE_TYPE_SECURITY",
    "EVENT_TRACE_TYPE_SEND",
    "EVENT_TRACE_TYPE_SIDINFO",
    "EVENT_TRACE_TYPE_START",
    "EVENT_TRACE_TYPE_STOP",
    "EVENT_TRACE_TYPE_SUSPEND",
    "EVENT_TRACE_TYPE_TERMINATE",
    "EVENT_TRACE_TYPE_WINEVT_RECEIVE",
    "EVENT_TRACE_TYPE_WINEVT_SEND",
    "EVENT_TRACE_USE_GLOBAL_SEQUENCE",
    "EVENT_TRACE_USE_KBYTES_FOR_SIZE",
    "EVENT_TRACE_USE_LOCAL_SEQUENCE",
    "EVENT_TRACE_USE_NOCPUTIME",
    "EVENT_TRACE_USE_PAGED_MEMORY",
    "EVENT_TRACE_USE_PROCTIME",
    "EVENT_WRITE_FLAG_INPRIVATE",
    "EVENT_WRITE_FLAG_NO_FAULTING",
    "EnableTrace",
    "EnableTraceEx",
    "EnableTraceEx2",
    "EnumerateTraceGuids",
    "EnumerateTraceGuidsEx",
    "EventAccessControl",
    "EventAccessQuery",
    "EventAccessRemove",
    "EventActivityIdControl",
    "EventEnabled",
    "EventProviderEnabled",
    "EventRegister",
    "EventSetInformation",
    "EventTraceConfigGuid",
    "EventTraceGuid",
    "EventUnregister",
    "EventWrite",
    "EventWriteEx",
    "EventWriteString",
    "EventWriteTransfer",
    "FileIoGuid",
    "FlushTraceA",
    "FlushTraceW",
    "GLOBAL_LOGGER_NAME",
    "GLOBAL_LOGGER_NAMEA",
    "GLOBAL_LOGGER_NAMEW",
    "GetTraceEnableFlags",
    "GetTraceEnableLevel",
    "GetTraceLoggerHandle",
    "ITraceEvent",
    "ITraceEventCallback",
    "ITraceRelogger",
    "ImageLoadGuid",
    "KERNEL_LOGGER_NAME",
    "KERNEL_LOGGER_NAMEA",
    "KERNEL_LOGGER_NAMEW",
    "MAP_FLAGS",
    "MAP_VALUETYPE",
    "MAX_EVENT_DATA_DESCRIPTORS",
    "MAX_EVENT_FILTERS_COUNT",
    "MAX_EVENT_FILTER_DATA_SIZE",
    "MAX_EVENT_FILTER_EVENT_ID_COUNT",
    "MAX_EVENT_FILTER_EVENT_NAME_SIZE",
    "MAX_EVENT_FILTER_PAYLOAD_SIZE",
    "MAX_EVENT_FILTER_PID_COUNT",
    "MAX_MOF_FIELDS",
    "MAX_PAYLOAD_PREDICATES",
    "MOF_FIELD",
    "OFFSETINSTANCEDATAANDLENGTH",
    "OpenTraceA",
    "OpenTraceW",
    "PAYLOADFIELD_BETWEEN",
    "PAYLOADFIELD_CONTAINS",
    "PAYLOADFIELD_DOESNTCONTAIN",
    "PAYLOADFIELD_EQ",
    "PAYLOADFIELD_GE",
    "PAYLOADFIELD_GT",
    "PAYLOADFIELD_INVALID",
    "PAYLOADFIELD_IS",
    "PAYLOADFIELD_ISNOT",
    "PAYLOADFIELD_LE",
    "PAYLOADFIELD_LT",
    "PAYLOADFIELD_MODULO",
    "PAYLOADFIELD_NE",
    "PAYLOADFIELD_NOTBETWEEN",
    "PAYLOAD_FILTER_PREDICATE",
    "PAYLOAD_OPERATOR",
    "PENABLECALLBACK",
    "PEVENT_CALLBACK",
    "PEVENT_RECORD_CALLBACK",
    "PEVENT_TRACE_BUFFER_CALLBACKA",
    "PEVENT_TRACE_BUFFER_CALLBACKW",
    "PROCESSTRACE_HANDLE",
    "PROCESS_TRACE_MODE_EVENT_RECORD",
    "PROCESS_TRACE_MODE_RAW_TIMESTAMP",
    "PROCESS_TRACE_MODE_REAL_TIME",
    "PROFILE_SOURCE_INFO",
    "PROPERTY_DATA_DESCRIPTOR",
    "PROPERTY_FLAGS",
    "PROPERTY_FLAGS_PropertyHasCustomSchema",
    "PROPERTY_FLAGS_PropertyHasTags",
    "PROPERTY_FLAGS_PropertyParamCount",
    "PROPERTY_FLAGS_PropertyParamFixedCount",
    "PROPERTY_FLAGS_PropertyParamFixedLength",
    "PROPERTY_FLAGS_PropertyParamLength",
    "PROPERTY_FLAGS_PropertyStruct",
    "PROPERTY_FLAGS_PropertyWBEMXmlFragment",
    "PROVIDER_ENUMERATION_INFO",
    "PROVIDER_EVENT_INFO",
    "PROVIDER_FIELD_INFO",
    "PROVIDER_FIELD_INFOARRAY",
    "PROVIDER_FILTER_INFO",
    "PageFaultGuid",
    "PerfInfoGuid",
    "PrivateLoggerNotificationGuid",
    "ProcessGuid",
    "ProcessTrace",
    "QueryAllTracesA",
    "QueryAllTracesW",
    "QueryTraceA",
    "QueryTraceProcessingHandle",
    "QueryTraceW",
    "RELOGSTREAM_HANDLE",
    "RegisterTraceGuidsA",
    "RegisterTraceGuidsW",
    "RegistryGuid",
    "RemoveTraceCallback",
    "SYSTEM_ALPC_KW_GENERAL",
    "SYSTEM_CONFIG_KW_GRAPHICS",
    "SYSTEM_CONFIG_KW_NETWORK",
    "SYSTEM_CONFIG_KW_OPTICAL",
    "SYSTEM_CONFIG_KW_PNP",
    "SYSTEM_CONFIG_KW_SERVICES",
    "SYSTEM_CONFIG_KW_STORAGE",
    "SYSTEM_CONFIG_KW_SYSTEM",
    "SYSTEM_CPU_KW_CACHE_FLUSH",
    "SYSTEM_CPU_KW_CONFIG",
    "SYSTEM_CPU_KW_SPEC_CONTROL",
    "SYSTEM_EVENT_TYPE",
    "SYSTEM_HYPERVISOR_KW_CALLOUTS",
    "SYSTEM_HYPERVISOR_KW_PROFILE",
    "SYSTEM_HYPERVISOR_KW_VTL_CHANGE",
    "SYSTEM_INTERRUPT_KW_CLOCK_INTERRUPT",
    "SYSTEM_INTERRUPT_KW_DPC",
    "SYSTEM_INTERRUPT_KW_DPC_QUEUE",
    "SYSTEM_INTERRUPT_KW_GENERAL",
    "SYSTEM_INTERRUPT_KW_IPI",
    "SYSTEM_INTERRUPT_KW_WDF_DPC",
    "SYSTEM_INTERRUPT_KW_WDF_INTERRUPT",
    "SYSTEM_IOFILTER_KW_FAILURE",
    "SYSTEM_IOFILTER_KW_FASTIO",
    "SYSTEM_IOFILTER_KW_GENERAL",
    "SYSTEM_IOFILTER_KW_INIT",
    "SYSTEM_IO_KW_CC",
    "SYSTEM_IO_KW_DISK",
    "SYSTEM_IO_KW_DISK_INIT",
    "SYSTEM_IO_KW_DRIVERS",
    "SYSTEM_IO_KW_FILE",
    "SYSTEM_IO_KW_FILENAME",
    "SYSTEM_IO_KW_NETWORK",
    "SYSTEM_IO_KW_OPTICAL",
    "SYSTEM_IO_KW_OPTICAL_INIT",
    "SYSTEM_IO_KW_SPLIT",
    "SYSTEM_LOCK_KW_SPINLOCK",
    "SYSTEM_LOCK_KW_SPINLOCK_COUNTERS",
    "SYSTEM_LOCK_KW_SYNC_OBJECTS",
    "SYSTEM_MEMORY_KW_ALL_FAULTS",
    "SYSTEM_MEMORY_KW_CONTMEM_GEN",
    "SYSTEM_MEMORY_KW_FOOTPRINT",
    "SYSTEM_MEMORY_KW_GENERAL",
    "SYSTEM_MEMORY_KW_HARD_FAULTS",
    "SYSTEM_MEMORY_KW_HEAP",
    "SYSTEM_MEMORY_KW_MEMINFO",
    "SYSTEM_MEMORY_KW_MEMINFO_WS",
    "SYSTEM_MEMORY_KW_NONTRADEABLE",
    "SYSTEM_MEMORY_KW_PFSECTION",
    "SYSTEM_MEMORY_KW_POOL",
    "SYSTEM_MEMORY_KW_REFSET",
    "SYSTEM_MEMORY_KW_SESSION",
    "SYSTEM_MEMORY_KW_VAMAP",
    "SYSTEM_MEMORY_KW_VIRTUAL_ALLOC",
    "SYSTEM_MEMORY_KW_WS",
    "SYSTEM_MEMORY_POOL_FILTER_ID",
    "SYSTEM_OBJECT_KW_GENERAL",
    "SYSTEM_OBJECT_KW_HANDLE",
    "SYSTEM_POWER_KW_GENERAL",
    "SYSTEM_POWER_KW_HIBER_RUNDOWN",
    "SYSTEM_POWER_KW_IDLE_SELECTION",
    "SYSTEM_POWER_KW_PPM_EXIT_LATENCY",
    "SYSTEM_POWER_KW_PROCESSOR_IDLE",
    "SYSTEM_PROCESS_KW_DBGPRINT",
    "SYSTEM_PROCESS_KW_DEBUG_EVENTS",
    "SYSTEM_PROCESS_KW_FREEZE",
    "SYSTEM_PROCESS_KW_GENERAL",
    "SYSTEM_PROCESS_KW_INSWAP",
    "SYSTEM_PROCESS_KW_JOB",
    "SYSTEM_PROCESS_KW_LOADER",
    "SYSTEM_PROCESS_KW_PERF_COUNTER",
    "SYSTEM_PROCESS_KW_THREAD",
    "SYSTEM_PROCESS_KW_WAKE_COUNTER",
    "SYSTEM_PROCESS_KW_WAKE_DROP",
    "SYSTEM_PROCESS_KW_WAKE_EVENT",
    "SYSTEM_PROCESS_KW_WORKER_THREAD",
    "SYSTEM_PROFILE_KW_GENERAL",
    "SYSTEM_PROFILE_KW_PMC_PROFILE",
    "SYSTEM_REGISTRY_KW_GENERAL",
    "SYSTEM_REGISTRY_KW_HIVE",
    "SYSTEM_REGISTRY_KW_NOTIFICATION",
    "SYSTEM_SCHEDULER_KW_AFFINITY",
    "SYSTEM_SCHEDULER_KW_ANTI_STARVATION",
    "SYSTEM_SCHEDULER_KW_COMPACT_CSWITCH",
    "SYSTEM_SCHEDULER_KW_CONTEXT_SWITCH",
    "SYSTEM_SCHEDULER_KW_DISPATCHER",
    "SYSTEM_SCHEDULER_KW_IDEAL_PROCESSOR",
    "SYSTEM_SCHEDULER_KW_KERNEL_QUEUE",
    "SYSTEM_SCHEDULER_KW_LOAD_BALANCER",
    "SYSTEM_SCHEDULER_KW_PRIORITY",
    "SYSTEM_SCHEDULER_KW_SHOULD_YIELD",
    "SYSTEM_SCHEDULER_KW_XSCHEDULER",
    "SYSTEM_SYSCALL_KW_GENERAL",
    "SYSTEM_TIMER_KW_CLOCK_TIMER",
    "SYSTEM_TIMER_KW_GENERAL",
    "SetTraceCallback",
    "SplitIoGuid",
    "StartTraceA",
    "StartTraceW",
    "StopTraceA",
    "StopTraceW",
    "SystemAlpcProviderGuid",
    "SystemConfigProviderGuid",
    "SystemCpuProviderGuid",
    "SystemHypervisorProviderGuid",
    "SystemInterruptProviderGuid",
    "SystemIoFilterProviderGuid",
    "SystemIoProviderGuid",
    "SystemLockProviderGuid",
    "SystemMemoryProviderGuid",
    "SystemObjectProviderGuid",
    "SystemPowerProviderGuid",
    "SystemProcessProviderGuid",
    "SystemProfileProviderGuid",
    "SystemRegistryProviderGuid",
    "SystemSchedulerProviderGuid",
    "SystemSyscallProviderGuid",
    "SystemTimerProviderGuid",
    "SystemTraceControlGuid",
    "TDH_CONTEXT",
    "TDH_CONTEXT_MAXIMUM",
    "TDH_CONTEXT_PDB_PATH",
    "TDH_CONTEXT_POINTERSIZE",
    "TDH_CONTEXT_TYPE",
    "TDH_CONTEXT_WPP_GMT",
    "TDH_CONTEXT_WPP_TMFFILE",
    "TDH_CONTEXT_WPP_TMFSEARCHPATH",
    "TDH_HANDLE",
    "TDH_INTYPE_ANSICHAR",
    "TDH_INTYPE_ANSISTRING",
    "TDH_INTYPE_BINARY",
    "TDH_INTYPE_BOOLEAN",
    "TDH_INTYPE_COUNTEDANSISTRING",
    "TDH_INTYPE_COUNTEDSTRING",
    "TDH_INTYPE_DOUBLE",
    "TDH_INTYPE_FILETIME",
    "TDH_INTYPE_FLOAT",
    "TDH_INTYPE_GUID",
    "TDH_INTYPE_HEXDUMP",
    "TDH_INTYPE_HEXINT32",
    "TDH_INTYPE_HEXINT64",
    "TDH_INTYPE_INT16",
    "TDH_INTYPE_INT32",
    "TDH_INTYPE_INT64",
    "TDH_INTYPE_INT8",
    "TDH_INTYPE_MANIFEST_COUNTEDANSISTRING",
    "TDH_INTYPE_MANIFEST_COUNTEDBINARY",
    "TDH_INTYPE_MANIFEST_COUNTEDSTRING",
    "TDH_INTYPE_NONNULLTERMINATEDANSISTRING",
    "TDH_INTYPE_NONNULLTERMINATEDSTRING",
    "TDH_INTYPE_NULL",
    "TDH_INTYPE_POINTER",
    "TDH_INTYPE_RESERVED24",
    "TDH_INTYPE_REVERSEDCOUNTEDANSISTRING",
    "TDH_INTYPE_REVERSEDCOUNTEDSTRING",
    "TDH_INTYPE_SID",
    "TDH_INTYPE_SIZET",
    "TDH_INTYPE_SYSTEMTIME",
    "TDH_INTYPE_UINT16",
    "TDH_INTYPE_UINT32",
    "TDH_INTYPE_UINT64",
    "TDH_INTYPE_UINT8",
    "TDH_INTYPE_UNICODECHAR",
    "TDH_INTYPE_UNICODESTRING",
    "TDH_INTYPE_WBEMSID",
    "TDH_OUTTYPE_BOOLEAN",
    "TDH_OUTTYPE_BYTE",
    "TDH_OUTTYPE_CIMDATETIME",
    "TDH_OUTTYPE_CODE_POINTER",
    "TDH_OUTTYPE_CULTURE_INSENSITIVE_DATETIME",
    "TDH_OUTTYPE_DATETIME",
    "TDH_OUTTYPE_DATETIME_UTC",
    "TDH_OUTTYPE_DOUBLE",
    "TDH_OUTTYPE_ERRORCODE",
    "TDH_OUTTYPE_ETWTIME",
    "TDH_OUTTYPE_FLOAT",
    "TDH_OUTTYPE_GUID",
    "TDH_OUTTYPE_HEXBINARY",
    "TDH_OUTTYPE_HEXINT16",
    "TDH_OUTTYPE_HEXINT32",
    "TDH_OUTTYPE_HEXINT64",
    "TDH_OUTTYPE_HEXINT8",
    "TDH_OUTTYPE_HRESULT",
    "TDH_OUTTYPE_INT",
    "TDH_OUTTYPE_IPV4",
    "TDH_OUTTYPE_IPV6",
    "TDH_OUTTYPE_JSON",
    "TDH_OUTTYPE_LONG",
    "TDH_OUTTYPE_NOPRINT",
    "TDH_OUTTYPE_NTSTATUS",
    "TDH_OUTTYPE_NULL",
    "TDH_OUTTYPE_PID",
    "TDH_OUTTYPE_PKCS7_WITH_TYPE_INFO",
    "TDH_OUTTYPE_PORT",
    "TDH_OUTTYPE_REDUCEDSTRING",
    "TDH_OUTTYPE_SHORT",
    "TDH_OUTTYPE_SOCKETADDRESS",
    "TDH_OUTTYPE_STRING",
    "TDH_OUTTYPE_TID",
    "TDH_OUTTYPE_UNSIGNEDBYTE",
    "TDH_OUTTYPE_UNSIGNEDINT",
    "TDH_OUTTYPE_UNSIGNEDLONG",
    "TDH_OUTTYPE_UNSIGNEDSHORT",
    "TDH_OUTTYPE_UTF8",
    "TDH_OUTTYPE_WIN32ERROR",
    "TDH_OUTTYPE_XML",
    "TEMPLATE_CONTROL_GUID",
    "TEMPLATE_EVENT_DATA",
    "TEMPLATE_FLAGS",
    "TEMPLATE_USER_DATA",
    "TRACELOG_ACCESS_KERNEL_LOGGER",
    "TRACELOG_ACCESS_REALTIME",
    "TRACELOG_CREATE_INPROC",
    "TRACELOG_CREATE_ONDISK",
    "TRACELOG_CREATE_REALTIME",
    "TRACELOG_GUID_ENABLE",
    "TRACELOG_JOIN_GROUP",
    "TRACELOG_LOG_EVENT",
    "TRACELOG_REGISTER_GUIDS",
    "TRACE_ENABLE_INFO",
    "TRACE_EVENT_INFO",
    "TRACE_GUID_INFO",
    "TRACE_GUID_PROPERTIES",
    "TRACE_GUID_REGISTRATION",
    "TRACE_HEADER_FLAG_LOG_WNODE",
    "TRACE_HEADER_FLAG_TRACED_GUID",
    "TRACE_HEADER_FLAG_USE_GUID_PTR",
    "TRACE_HEADER_FLAG_USE_MOF_PTR",
    "TRACE_HEADER_FLAG_USE_TIMESTAMP",
    "TRACE_LEVEL_CRITICAL",
    "TRACE_LEVEL_ERROR",
    "TRACE_LEVEL_FATAL",
    "TRACE_LEVEL_INFORMATION",
    "TRACE_LEVEL_NONE",
    "TRACE_LEVEL_RESERVED6",
    "TRACE_LEVEL_RESERVED7",
    "TRACE_LEVEL_RESERVED8",
    "TRACE_LEVEL_RESERVED9",
    "TRACE_LEVEL_VERBOSE",
    "TRACE_LEVEL_WARNING",
    "TRACE_LOGFILE_HEADER",
    "TRACE_LOGFILE_HEADER32",
    "TRACE_LOGFILE_HEADER64",
    "TRACE_MESSAGE_COMPONENTID",
    "TRACE_MESSAGE_FLAGS",
    "TRACE_MESSAGE_FLAG_MASK",
    "TRACE_MESSAGE_GUID",
    "TRACE_MESSAGE_PERFORMANCE_TIMESTAMP",
    "TRACE_MESSAGE_POINTER32",
    "TRACE_MESSAGE_POINTER64",
    "TRACE_MESSAGE_SEQUENCE",
    "TRACE_MESSAGE_SYSTEMINFO",
    "TRACE_MESSAGE_TIMESTAMP",
    "TRACE_PERIODIC_CAPTURE_STATE_INFO",
    "TRACE_PROFILE_INTERVAL",
    "TRACE_PROVIDER_FLAG_LEGACY",
    "TRACE_PROVIDER_FLAG_PRE_ENABLE",
    "TRACE_PROVIDER_INFO",
    "TRACE_PROVIDER_INSTANCE_INFO",
    "TRACE_QUERY_INFO_CLASS",
    "TRACE_QUERY_INFO_CLASS_MaxTraceSetInfoClass",
    "TRACE_QUERY_INFO_CLASS_TraceDisallowListQuery",
    "TRACE_QUERY_INFO_CLASS_TraceGroupQueryInfo",
    "TRACE_QUERY_INFO_CLASS_TraceGroupQueryList",
    "TRACE_QUERY_INFO_CLASS_TraceGuidQueryInfo",
    "TRACE_QUERY_INFO_CLASS_TraceGuidQueryList",
    "TRACE_QUERY_INFO_CLASS_TraceGuidQueryProcess",
    "TRACE_QUERY_INFO_CLASS_TraceInfoReserved15",
    "TRACE_QUERY_INFO_CLASS_TraceLbrConfigurationInfo",
    "TRACE_QUERY_INFO_CLASS_TraceLbrEventListInfo",
    "TRACE_QUERY_INFO_CLASS_TraceMaxLoggersQuery",
    "TRACE_QUERY_INFO_CLASS_TraceMaxPmcCounterQuery",
    "TRACE_QUERY_INFO_CLASS_TracePeriodicCaptureStateInfo",
    "TRACE_QUERY_INFO_CLASS_TracePeriodicCaptureStateListInfo",
    "TRACE_QUERY_INFO_CLASS_TracePmcCounterListInfo",
    "TRACE_QUERY_INFO_CLASS_TracePmcCounterOwners",
    "TRACE_QUERY_INFO_CLASS_TracePmcEventListInfo",
    "TRACE_QUERY_INFO_CLASS_TraceProfileSourceConfigInfo",
    "TRACE_QUERY_INFO_CLASS_TraceProfileSourceListInfo",
    "TRACE_QUERY_INFO_CLASS_TraceProviderBinaryTracking",
    "TRACE_QUERY_INFO_CLASS_TraceSampledProfileIntervalInfo",
    "TRACE_QUERY_INFO_CLASS_TraceSetDisallowList",
    "TRACE_QUERY_INFO_CLASS_TraceStackCachingInfo",
    "TRACE_QUERY_INFO_CLASS_TraceStackTracingInfo",
    "TRACE_QUERY_INFO_CLASS_TraceStreamCount",
    "TRACE_QUERY_INFO_CLASS_TraceSystemTraceEnableFlagsInfo",
    "TRACE_QUERY_INFO_CLASS_TraceUnifiedStackCachingInfo",
    "TRACE_QUERY_INFO_CLASS_TraceVersionInfo",
    "TRACE_STACK_CACHING_INFO",
    "TRACE_VERSION_INFO",
    "TcpIpGuid",
    "TdhAggregatePayloadFilters",
    "TdhCleanupPayloadEventFilterDescriptor",
    "TdhCloseDecodingHandle",
    "TdhCreatePayloadFilter",
    "TdhDeletePayloadFilter",
    "TdhEnumerateManifestProviderEvents",
    "TdhEnumerateProviderFieldInformation",
    "TdhEnumerateProviderFilters",
    "TdhEnumerateProviders",
    "TdhEnumerateProvidersForDecodingSource",
    "TdhFormatProperty",
    "TdhGetDecodingParameter",
    "TdhGetEventInformation",
    "TdhGetEventMapInformation",
    "TdhGetManifestEventInformation",
    "TdhGetProperty",
    "TdhGetPropertySize",
    "TdhGetWppMessage",
    "TdhGetWppProperty",
    "TdhLoadManifest",
    "TdhLoadManifestFromBinary",
    "TdhLoadManifestFromMemory",
    "TdhOpenDecodingHandle",
    "TdhQueryProviderFieldInformation",
    "TdhSetDecodingParameter",
    "TdhUnloadManifest",
    "TdhUnloadManifestFromMemory",
    "ThreadGuid",
    "TraceEvent",
    "TraceEventInstance",
    "TraceMessage",
    "TraceMessageVa",
    "TraceQueryInformation",
    "TraceSetInformation",
    "UdpIpGuid",
    "UnregisterTraceGuids",
    "UpdateTraceA",
    "UpdateTraceW",
    "WMIDPREQUEST",
    "WMIDPREQUESTCODE",
    "WMIGUID_EXECUTE",
    "WMIGUID_NOTIFICATION",
    "WMIGUID_QUERY",
    "WMIGUID_READ_DESCRIPTION",
    "WMIGUID_SET",
    "WMIREGGUIDW",
    "WMIREGINFOW",
    "WMIREG_FLAG_EVENT_ONLY_GUID",
    "WMIREG_FLAG_EXPENSIVE",
    "WMIREG_FLAG_INSTANCE_BASENAME",
    "WMIREG_FLAG_INSTANCE_LIST",
    "WMIREG_FLAG_INSTANCE_PDO",
    "WMIREG_FLAG_REMOVE_GUID",
    "WMIREG_FLAG_RESERVED1",
    "WMIREG_FLAG_RESERVED2",
    "WMIREG_FLAG_TRACED_GUID",
    "WMIREG_FLAG_TRACE_CONTROL_GUID",
    "WMI_CAPTURE_STATE",
    "WMI_DISABLE_COLLECTION",
    "WMI_DISABLE_EVENTS",
    "WMI_ENABLE_COLLECTION",
    "WMI_ENABLE_EVENTS",
    "WMI_EXECUTE_METHOD",
    "WMI_GET_ALL_DATA",
    "WMI_GET_SINGLE_INSTANCE",
    "WMI_GLOBAL_LOGGER_ID",
    "WMI_GUIDTYPE_DATA",
    "WMI_GUIDTYPE_EVENT",
    "WMI_GUIDTYPE_TRACE",
    "WMI_GUIDTYPE_TRACECONTROL",
    "WMI_REGINFO",
    "WMI_SET_SINGLE_INSTANCE",
    "WMI_SET_SINGLE_ITEM",
    "WNODE_ALL_DATA",
    "WNODE_EVENT_ITEM",
    "WNODE_EVENT_REFERENCE",
    "WNODE_FLAG_ALL_DATA",
    "WNODE_FLAG_ANSI_INSTANCENAMES",
    "WNODE_FLAG_EVENT_ITEM",
    "WNODE_FLAG_EVENT_REFERENCE",
    "WNODE_FLAG_FIXED_INSTANCE_SIZE",
    "WNODE_FLAG_INSTANCES_SAME",
    "WNODE_FLAG_INTERNAL",
    "WNODE_FLAG_LOG_WNODE",
    "WNODE_FLAG_METHOD_ITEM",
    "WNODE_FLAG_NO_HEADER",
    "WNODE_FLAG_PDO_INSTANCE_NAMES",
    "WNODE_FLAG_PERSIST_EVENT",
    "WNODE_FLAG_SEND_DATA_BLOCK",
    "WNODE_FLAG_SEVERITY_MASK",
    "WNODE_FLAG_SINGLE_INSTANCE",
    "WNODE_FLAG_SINGLE_ITEM",
    "WNODE_FLAG_STATIC_INSTANCE_NAMES",
    "WNODE_FLAG_TOO_SMALL",
    "WNODE_FLAG_TRACED_GUID",
    "WNODE_FLAG_USE_GUID_PTR",
    "WNODE_FLAG_USE_MOF_PTR",
    "WNODE_FLAG_USE_TIMESTAMP",
    "WNODE_FLAG_VERSIONED_PROPERTIES",
    "WNODE_HEADER",
    "WNODE_METHOD_ITEM",
    "WNODE_SINGLE_INSTANCE",
    "WNODE_SINGLE_ITEM",
    "WNODE_TOO_SMALL",
    "_TDH_IN_TYPE",
    "_TDH_OUT_TYPE",
]
_arch_optional = [
]
