from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, winfunctype, winfunctype_pointer, make_ready
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Storage.Nvme
class ACTIVE_LATENCY_CONFIGURATION(EasyCastStructure):
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Anonymous: _Anonymous_e__Struct
        AsUshort: UInt16
        _pack_ = 1
        class _Anonymous_e__Struct(EasyCastStructure):
            _bitfield: UInt16
            _pack_ = 1
NVME_IDENTIFY_CNS_DESCRIPTOR_NAMESPACE_SIZE: UInt32 = 4096
GUID_OCP_DEVICE_SMART_INFORMATIONGuid: Guid = Guid('{2810afc5-bfea-a4f2-9c4f-6f7cc914d5af}')
GUID_OCP_DEVICE_SMART_INFORMATION: Guid = Guid('{2810afc5-bfea-a4f2-9c4f-6f7cc914d5af}')
GUID_WCS_DEVICE_SMART_ATTRIBUTESGuid: Guid = Guid('{2810afc5-bfea-a4f2-9c4f-6f7cc914d5af}')
GUID_WCS_DEVICE_SMART_ATTRIBUTES: Guid = Guid('{2810afc5-bfea-a4f2-9c4f-6f7cc914d5af}')
GUID_OCP_DEVICE_ERROR_RECOVERYGuid: Guid = Guid('{2131d944-30fe-ae34-ab4d-fd3dba83195a}')
GUID_OCP_DEVICE_ERROR_RECOVERY: Guid = Guid('{2131d944-30fe-ae34-ab4d-fd3dba83195a}')
GUID_WCS_DEVICE_ERROR_RECOVERYGuid: Guid = Guid('{2131d944-30fe-ae34-ab4d-fd3dba83195a}')
GUID_WCS_DEVICE_ERROR_RECOVERY: Guid = Guid('{2131d944-30fe-ae34-ab4d-fd3dba83195a}')
GUID_OCP_DEVICE_FIRMWARE_ACTIVATION_HISTORYGuid: Guid = Guid('{769a796d-dab4-a3f6-e24d-b28aacf31cd1}')
GUID_OCP_DEVICE_FIRMWARE_ACTIVATION_HISTORY: Guid = Guid('{769a796d-dab4-a3f6-e24d-b28aacf31cd1}')
GUID_OCP_DEVICE_LATENCY_MONITORGuid: Guid = Guid('{8cc07a92-84d0-9c6c-7043-e6d4585ed485}')
GUID_OCP_DEVICE_LATENCY_MONITOR: Guid = Guid('{8cc07a92-84d0-9c6c-7043-e6d4585ed485}')
GUID_OCP_DEVICE_DEVICE_CAPABILITIESGuid: Guid = Guid('{0d054297-e1d1-98c9-5d49-584b913c05b7}')
GUID_OCP_DEVICE_DEVICE_CAPABILITIES: Guid = Guid('{0d054297-e1d1-98c9-5d49-584b913c05b7}')
GUID_OCP_DEVICE_UNSUPPORTED_REQUIREMENTSGuid: Guid = Guid('{0e9c722f-2399-bb2c-6348-32d0b798bbc7}')
GUID_OCP_DEVICE_UNSUPPORTED_REQUIREMENTS: Guid = Guid('{0e9c722f-2399-bb2c-6348-32d0b798bbc7}')
GUID_OCP_DEVICE_TCG_CONFIGURATIONGuid: Guid = Guid('{bd244006-e07e-83e6-c047-54fa9d2ae054}')
GUID_OCP_DEVICE_TCG_CONFIGURATION: Guid = Guid('{bd244006-e07e-83e6-c047-54fa9d2ae054}')
GUID_OCP_DEVICE_TCG_HISTORYGuid: Guid = Guid('{704b513e-09c6-9490-274e-d0969690d788}')
GUID_OCP_DEVICE_TCG_HISTORY: Guid = Guid('{704b513e-09c6-9490-274e-d0969690d788}')
GUID_MFND_CHILD_CONTROLLER_EVENT_LOG_PAGEGuid: Guid = Guid('{98bcce18-a5f0-bf35-a544-d97f259d669c}')
GUID_MFND_CHILD_CONTROLLER_EVENT_LOG_PAGE: Guid = Guid('{98bcce18-a5f0-bf35-a544-d97f259d669c}')
NVME_WCS_DEVICE_SMART_ATTRIBUTES_LOG_VERSION_2: UInt32 = 2
NVME_OCP_DEVICE_SMART_INFORMATION_LOG_VERSION_3: UInt32 = 3
NVME_WCS_DEVICE_ERROR_RECOVERY_LOG_VERSION_1: UInt32 = 1
NVME_OCP_DEVICE_ERROR_RECOVERY_LOG_VERSION_2: UInt32 = 2
FIRMWARE_ACTIVATION_HISTORY_ENTRY_VERSION_1: UInt32 = 1
NVME_OCP_DEVICE_FIRMWARE_ACTIVATION_HISTORY_LOG_VERSION_1: UInt32 = 1
NVME_OCP_DEVICE_LATENCY_MONITOR_LOG_VERSION_1: UInt32 = 1
NVME_OCP_DEVICE_CAPABILITIES_LOG_VERSION_1: UInt32 = 1
NVME_OCP_DEVICE_UNSUPPORTED_REQUIREMENTS_LOG_VERSION_1: UInt32 = 1
NVME_OCP_DEVICE_TCG_CONFIGURATION_LOG_VERSION_1: UInt32 = 1
TCG_HISTORY_ENTRY_VERSION_1: UInt32 = 1
NVME_OCP_DEVICE_TCG_HISTORY_LOG_VERSION_1: UInt32 = 1
NVME_MAX_HOST_IDENTIFIER_SIZE: UInt32 = 16
NVME_HOST_IDENTIFIER_SIZE: UInt32 = 8
NVME_EXTENDED_HOST_IDENTIFIER_SIZE: UInt32 = 16
NVME_MAX_LOG_SIZE: UInt32 = 4096
NVME_TELEMETRY_DATA_BLOCK_SIZE: UInt32 = 512
NVME_STREAMS_ID_MIN: UInt32 = 1
NVME_STREAMS_ID_MAX: UInt32 = 65535
NVME_STREAMS_GET_STATUS_MAX_IDS: UInt32 = 65535
NVME_NAMESPACE_ALL: UInt32 = 4294967295
class BUCKET_COUNTER(EasyCastStructure):
    Reserved: UInt32
    Trim: UInt32
    Write: UInt32
    Read: UInt32
    _pack_ = 1
class DEBUG_BIT_FIELD(EasyCastStructure):
    _bitfield: UInt16
    _pack_ = 1
class DSSD_POWER_STATE_DESCRIPTOR(EasyCastStructure):
    _bitfield: Byte
class FIRMWARE_ACTIVATION_HISTORY_ENTRY(EasyCastStructure):
    VersionNumber: Byte
    Length: Byte
    Reserved0: UInt16
    ActivationCount: UInt16
    Timestamp: UInt64
    Reserved1: UInt64
    PowerCycleCount: UInt64
    PreviousFirmware: UInt64
    NewFirmware: UInt64
    SlotNumber: Byte
    CommitActionType: Byte
    Result: UInt16
    Reserved2: Byte * 14
    _pack_ = 1
class LATENCY_MONITOR_FEATURE_STATUS(EasyCastStructure):
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Anonymous: _Anonymous_e__Struct
        AsUchar: Byte
        class _Anonymous_e__Struct(EasyCastStructure):
            _bitfield: Byte
class LATENCY_STAMP(EasyCastStructure):
    Trim3: UInt64
    Write3: UInt64
    Read3: UInt64
    Trim2: UInt64
    Write2: UInt64
    Read2: UInt64
    Trim1: UInt64
    Write1: UInt64
    Read1: UInt64
    Trim0: UInt64
    Write0: UInt64
    Read0: UInt64
    _pack_ = 1
class LATENCY_STAMP_UNITS(EasyCastStructure):
    _bitfield: UInt16
    _pack_ = 1
class MEASURED_LATENCY(EasyCastStructure):
    Trim3: UInt16
    Write3: UInt16
    Read3: UInt16
    Trim2: UInt16
    Write2: UInt16
    Read2: UInt16
    Trim1: UInt16
    Write1: UInt16
    Read1: UInt16
    Trim0: UInt16
    Write0: UInt16
    Read0: UInt16
    _pack_ = 1
NVME_ACCESS_FREQUENCIES = Int32
NVME_ACCESS_FREQUENCY_NONE: NVME_ACCESS_FREQUENCIES = 0
NVME_ACCESS_FREQUENCY_TYPICAL: NVME_ACCESS_FREQUENCIES = 1
NVME_ACCESS_FREQUENCY_INFR_WRITE_INFR_READ: NVME_ACCESS_FREQUENCIES = 2
NVME_ACCESS_FREQUENCY_INFR_WRITE_FR_READ: NVME_ACCESS_FREQUENCIES = 3
NVME_ACCESS_FREQUENCY_FR_WRITE_INFR_READ: NVME_ACCESS_FREQUENCIES = 4
NVME_ACCESS_FREQUENCY_FR_WRITE_FR_READ: NVME_ACCESS_FREQUENCIES = 5
NVME_ACCESS_FREQUENCY_ONE_TIME_READ: NVME_ACCESS_FREQUENCIES = 6
NVME_ACCESS_FREQUENCY_SPECULATIVE_READ: NVME_ACCESS_FREQUENCIES = 7
NVME_ACCESS_FREQUENCY_WILL_BE_OVERWRITTEN: NVME_ACCESS_FREQUENCIES = 8
NVME_ACCESS_LATENCIES = Int32
NVME_ACCESS_LATENCY_NONE: NVME_ACCESS_LATENCIES = 0
NVME_ACCESS_LATENCY_IDLE: NVME_ACCESS_LATENCIES = 1
NVME_ACCESS_LATENCY_NORMAL: NVME_ACCESS_LATENCIES = 2
NVME_ACCESS_LATENCY_LOW: NVME_ACCESS_LATENCIES = 3
class NVME_ACTIVE_NAMESPACE_ID_LIST(EasyCastStructure):
    NSID: UInt32 * 1024
NVME_ADMIN_COMMANDS = Int32
NVME_ADMIN_COMMAND_DELETE_IO_SQ: NVME_ADMIN_COMMANDS = 0
NVME_ADMIN_COMMAND_CREATE_IO_SQ: NVME_ADMIN_COMMANDS = 1
NVME_ADMIN_COMMAND_GET_LOG_PAGE: NVME_ADMIN_COMMANDS = 2
NVME_ADMIN_COMMAND_DELETE_IO_CQ: NVME_ADMIN_COMMANDS = 4
NVME_ADMIN_COMMAND_CREATE_IO_CQ: NVME_ADMIN_COMMANDS = 5
NVME_ADMIN_COMMAND_IDENTIFY: NVME_ADMIN_COMMANDS = 6
NVME_ADMIN_COMMAND_ABORT: NVME_ADMIN_COMMANDS = 8
NVME_ADMIN_COMMAND_SET_FEATURES: NVME_ADMIN_COMMANDS = 9
NVME_ADMIN_COMMAND_GET_FEATURES: NVME_ADMIN_COMMANDS = 10
NVME_ADMIN_COMMAND_ASYNC_EVENT_REQUEST: NVME_ADMIN_COMMANDS = 12
NVME_ADMIN_COMMAND_NAMESPACE_MANAGEMENT: NVME_ADMIN_COMMANDS = 13
NVME_ADMIN_COMMAND_FIRMWARE_ACTIVATE: NVME_ADMIN_COMMANDS = 16
NVME_ADMIN_COMMAND_FIRMWARE_COMMIT: NVME_ADMIN_COMMANDS = 16
NVME_ADMIN_COMMAND_FIRMWARE_IMAGE_DOWNLOAD: NVME_ADMIN_COMMANDS = 17
NVME_ADMIN_COMMAND_DEVICE_SELF_TEST: NVME_ADMIN_COMMANDS = 20
NVME_ADMIN_COMMAND_NAMESPACE_ATTACHMENT: NVME_ADMIN_COMMANDS = 21
NVME_ADMIN_COMMAND_DIRECTIVE_SEND: NVME_ADMIN_COMMANDS = 25
NVME_ADMIN_COMMAND_DIRECTIVE_RECEIVE: NVME_ADMIN_COMMANDS = 26
NVME_ADMIN_COMMAND_VIRTUALIZATION_MANAGEMENT: NVME_ADMIN_COMMANDS = 28
NVME_ADMIN_COMMAND_NVME_MI_SEND: NVME_ADMIN_COMMANDS = 29
NVME_ADMIN_COMMAND_NVME_MI_RECEIVE: NVME_ADMIN_COMMANDS = 30
NVME_ADMIN_COMMAND_DOORBELL_BUFFER_CONFIG: NVME_ADMIN_COMMANDS = 124
NVME_ADMIN_COMMAND_FORMAT_NVM: NVME_ADMIN_COMMANDS = 128
NVME_ADMIN_COMMAND_SECURITY_SEND: NVME_ADMIN_COMMANDS = 129
NVME_ADMIN_COMMAND_SECURITY_RECEIVE: NVME_ADMIN_COMMANDS = 130
NVME_ADMIN_COMMAND_SANITIZE: NVME_ADMIN_COMMANDS = 132
NVME_ADMIN_COMMAND_GET_LBA_STATUS: NVME_ADMIN_COMMANDS = 134
class NVME_ADMIN_COMPLETION_QUEUE_BASE_ADDRESS(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlonglong: UInt64
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt64
class NVME_ADMIN_QUEUE_ATTRIBUTES(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_ADMIN_SUBMISSION_QUEUE_BASE_ADDRESS(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlonglong: UInt64
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt64
NVME_AMS_OPTION = Int32
NVME_AMS_ROUND_ROBIN: NVME_AMS_OPTION = 0
NVME_AMS_WEIGHTED_ROUND_ROBIN_URGENT: NVME_AMS_OPTION = 1
NVME_ASYNC_EVENT_ERROR_STATUS_CODES = Int32
NVME_ASYNC_ERROR_INVALID_SUBMISSION_QUEUE: NVME_ASYNC_EVENT_ERROR_STATUS_CODES = 0
NVME_ASYNC_ERROR_INVALID_DOORBELL_WRITE_VALUE: NVME_ASYNC_EVENT_ERROR_STATUS_CODES = 1
NVME_ASYNC_ERROR_DIAG_FAILURE: NVME_ASYNC_EVENT_ERROR_STATUS_CODES = 2
NVME_ASYNC_ERROR_PERSISTENT_INTERNAL_DEVICE_ERROR: NVME_ASYNC_EVENT_ERROR_STATUS_CODES = 3
NVME_ASYNC_ERROR_TRANSIENT_INTERNAL_DEVICE_ERROR: NVME_ASYNC_EVENT_ERROR_STATUS_CODES = 4
NVME_ASYNC_ERROR_FIRMWARE_IMAGE_LOAD_ERROR: NVME_ASYNC_EVENT_ERROR_STATUS_CODES = 5
NVME_ASYNC_EVENT_HEALTH_STATUS_CODES = Int32
NVME_ASYNC_HEALTH_NVM_SUBSYSTEM_RELIABILITY: NVME_ASYNC_EVENT_HEALTH_STATUS_CODES = 0
NVME_ASYNC_HEALTH_TEMPERATURE_THRESHOLD: NVME_ASYNC_EVENT_HEALTH_STATUS_CODES = 1
NVME_ASYNC_HEALTH_SPARE_BELOW_THRESHOLD: NVME_ASYNC_EVENT_HEALTH_STATUS_CODES = 2
NVME_ASYNC_EVENT_IO_COMMAND_SET_STATUS_CODES = Int32
NVME_ASYNC_IO_CMD_SET_RESERVATION_LOG_PAGE_AVAILABLE: NVME_ASYNC_EVENT_IO_COMMAND_SET_STATUS_CODES = 0
NVME_ASYNC_IO_CMD_SANITIZE_OPERATION_COMPLETED: NVME_ASYNC_EVENT_IO_COMMAND_SET_STATUS_CODES = 1
NVME_ASYNC_IO_CMD_SANITIZE_OPERATION_COMPLETED_WITH_UNEXPECTED_DEALLOCATION: NVME_ASYNC_EVENT_IO_COMMAND_SET_STATUS_CODES = 2
NVME_ASYNC_EVENT_NOTICE_CODES = Int32
NVME_ASYNC_NOTICE_NAMESPACE_ATTRIBUTE_CHANGED: NVME_ASYNC_EVENT_NOTICE_CODES = 0
NVME_ASYNC_NOTICE_FIRMWARE_ACTIVATION_STARTING: NVME_ASYNC_EVENT_NOTICE_CODES = 1
NVME_ASYNC_NOTICE_TELEMETRY_LOG_CHANGED: NVME_ASYNC_EVENT_NOTICE_CODES = 2
NVME_ASYNC_NOTICE_ASYMMETRIC_ACCESS_CHANGE: NVME_ASYNC_EVENT_NOTICE_CODES = 3
NVME_ASYNC_NOTICE_PREDICTABLE_LATENCY_EVENT_AGGREGATE_LOG_CHANGE: NVME_ASYNC_EVENT_NOTICE_CODES = 4
NVME_ASYNC_NOTICE_LBA_STATUS_INFORMATION_ALERT: NVME_ASYNC_EVENT_NOTICE_CODES = 5
NVME_ASYNC_NOTICE_ENDURANCE_GROUP_EVENT_AGGREGATE_LOG_CHANGE: NVME_ASYNC_EVENT_NOTICE_CODES = 6
NVME_ASYNC_NOTICE_ZONE_DESCRIPTOR_CHANGED: NVME_ASYNC_EVENT_NOTICE_CODES = 239
NVME_ASYNC_EVENT_TYPES = Int32
NVME_ASYNC_EVENT_TYPE_ERROR_STATUS: NVME_ASYNC_EVENT_TYPES = 0
NVME_ASYNC_EVENT_TYPE_HEALTH_STATUS: NVME_ASYNC_EVENT_TYPES = 1
NVME_ASYNC_EVENT_TYPE_NOTICE: NVME_ASYNC_EVENT_TYPES = 2
NVME_ASYNC_EVENT_TYPE_IO_COMMAND_SET_STATUS: NVME_ASYNC_EVENT_TYPES = 6
NVME_ASYNC_EVENT_TYPE_VENDOR_SPECIFIC: NVME_ASYNC_EVENT_TYPES = 7
NVME_ASYNC_EVENT_TYPE_VENDOR_SPECIFIC_CODES = Int32
NVME_ASYNC_EVENT_TYPE_VENDOR_SPECIFIC_RESERVED: NVME_ASYNC_EVENT_TYPE_VENDOR_SPECIFIC_CODES = 0
NVME_ASYNC_EVENT_TYPE_VENDOR_SPECIFIC_DEVICE_PANIC: NVME_ASYNC_EVENT_TYPE_VENDOR_SPECIFIC_CODES = 1
class NVME_AUTO_POWER_STATE_TRANSITION_ENTRY(EasyCastStructure):
    _bitfield: UInt32
    Reserved1: UInt32
NVME_CC_SHN_SHUTDOWN_NOTIFICATIONS = Int32
NVME_CC_SHN_NO_NOTIFICATION: NVME_CC_SHN_SHUTDOWN_NOTIFICATIONS = 0
NVME_CC_SHN_NORMAL_SHUTDOWN: NVME_CC_SHN_SHUTDOWN_NOTIFICATIONS = 1
NVME_CC_SHN_ABRUPT_SHUTDOWN: NVME_CC_SHN_SHUTDOWN_NOTIFICATIONS = 2
class NVME_CDW0_FEATURE_ENABLE_IEEE1667_SILO(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW0_FEATURE_ERROR_INJECTION(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW0_FEATURE_READONLY_WRITETHROUGH_MODE(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW0_RESERVATION_PERSISTENCE(EasyCastStructure):
    _bitfield: UInt32
class NVME_CDW10_ABORT(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW10_CREATE_IO_QUEUE(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW10_DATASET_MANAGEMENT(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW10_DIRECTIVE_RECEIVE(EasyCastStructure):
    NUMD: UInt32
class NVME_CDW10_DIRECTIVE_SEND(EasyCastStructure):
    NUMD: UInt32
class NVME_CDW10_FIRMWARE_ACTIVATE(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW10_FIRMWARE_DOWNLOAD(EasyCastStructure):
    NUMD: UInt32
class NVME_CDW10_FORMAT_NVM(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW10_GET_FEATURES(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW10_GET_LOG_PAGE(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW10_GET_LOG_PAGE_V13(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW10_IDENTIFY(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW10_RESERVATION_ACQUIRE(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW10_RESERVATION_REGISTER(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW10_RESERVATION_RELEASE(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW10_RESERVATION_REPORT(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        NUMD: UInt32
class NVME_CDW10_SANITIZE(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW10_SECURITY_SEND_RECEIVE(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW10_SET_FEATURES(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW10_ZONE_APPEND(EasyCastStructure):
    SLBA: UInt64
class NVME_CDW10_ZONE_MANAGEMENT_RECEIVE(EasyCastStructure):
    SLBA: UInt64
class NVME_CDW10_ZONE_MANAGEMENT_SEND(EasyCastStructure):
    SLBA: UInt64
class NVME_CDW11_CREATE_IO_CQ(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW11_CREATE_IO_SQ(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW11_DATASET_MANAGEMENT(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW11_DIRECTIVE_RECEIVE(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW11_DIRECTIVE_SEND(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW11_FEATURES(EasyCastUnion):
    NumberOfQueues: win32more.Windows.Win32.Storage.Nvme.NVME_CDW11_FEATURE_NUMBER_OF_QUEUES
    InterruptCoalescing: win32more.Windows.Win32.Storage.Nvme.NVME_CDW11_FEATURE_INTERRUPT_COALESCING
    InterruptVectorConfig: win32more.Windows.Win32.Storage.Nvme.NVME_CDW11_FEATURE_INTERRUPT_VECTOR_CONFIG
    LbaRangeType: win32more.Windows.Win32.Storage.Nvme.NVME_CDW11_FEATURE_LBA_RANGE_TYPE
    Arbitration: win32more.Windows.Win32.Storage.Nvme.NVME_CDW11_FEATURE_ARBITRATION
    VolatileWriteCache: win32more.Windows.Win32.Storage.Nvme.NVME_CDW11_FEATURE_VOLATILE_WRITE_CACHE
    AsyncEventConfig: win32more.Windows.Win32.Storage.Nvme.NVME_CDW11_FEATURE_ASYNC_EVENT_CONFIG
    PowerManagement: win32more.Windows.Win32.Storage.Nvme.NVME_CDW11_FEATURE_POWER_MANAGEMENT
    AutoPowerStateTransition: win32more.Windows.Win32.Storage.Nvme.NVME_CDW11_FEATURE_AUTO_POWER_STATE_TRANSITION
    TemperatureThreshold: win32more.Windows.Win32.Storage.Nvme.NVME_CDW11_FEATURE_TEMPERATURE_THRESHOLD
    ErrorRecovery: win32more.Windows.Win32.Storage.Nvme.NVME_CDW11_FEATURE_ERROR_RECOVERY
    HostMemoryBuffer: win32more.Windows.Win32.Storage.Nvme.NVME_CDW11_FEATURE_HOST_MEMORY_BUFFER
    WriteAtomicityNormal: win32more.Windows.Win32.Storage.Nvme.NVME_CDW11_FEATURE_WRITE_ATOMICITY_NORMAL
    NonOperationalPowerState: win32more.Windows.Win32.Storage.Nvme.NVME_CDW11_FEATURE_NON_OPERATIONAL_POWER_STATE
    IoCommandSetProfile: win32more.Windows.Win32.Storage.Nvme.NVME_CDW11_FEATURE_IO_COMMAND_SET_PROFILE
    ErrorInjection: win32more.Windows.Win32.Storage.Nvme.NVME_CDW0_FEATURE_ERROR_INJECTION
    HostIdentifier: win32more.Windows.Win32.Storage.Nvme.NVME_CDW11_FEATURE_HOST_IDENTIFIER
    ReservationPersistence: win32more.Windows.Win32.Storage.Nvme.NVME_CDW11_FEATURE_RESERVATION_PERSISTENCE
    ReservationNotificationMask: win32more.Windows.Win32.Storage.Nvme.NVME_CDW11_FEATURE_RESERVATION_NOTIFICATION_MASK
    GetHostMetadata: win32more.Windows.Win32.Storage.Nvme.NVME_CDW11_FEATURE_GET_HOST_METADATA
    SetHostMetadata: win32more.Windows.Win32.Storage.Nvme.NVME_CDW11_FEATURE_SET_HOST_METADATA
    AsUlong: UInt32
class NVME_CDW11_FEATURE_ARBITRATION(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW11_FEATURE_ASYNC_EVENT_CONFIG(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW11_FEATURE_AUTO_POWER_STATE_TRANSITION(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW11_FEATURE_CLEAR_FW_UPDATE_HISTORY(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW11_FEATURE_CLEAR_PCIE_CORRECTABLE_ERROR_COUNTERS(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW11_FEATURE_ENABLE_IEEE1667_SILO(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW11_FEATURE_ERROR_RECOVERY(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW11_FEATURE_GET_HOST_METADATA(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW11_FEATURE_HOST_IDENTIFIER(EasyCastStructure):
    _bitfield: UInt32
class NVME_CDW11_FEATURE_HOST_MEMORY_BUFFER(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW11_FEATURE_INTERRUPT_COALESCING(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW11_FEATURE_INTERRUPT_VECTOR_CONFIG(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW11_FEATURE_IO_COMMAND_SET_PROFILE(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW11_FEATURE_LBA_RANGE_TYPE(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW11_FEATURE_NON_OPERATIONAL_POWER_STATE(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW11_FEATURE_NUMBER_OF_QUEUES(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW11_FEATURE_POWER_MANAGEMENT(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW11_FEATURE_READONLY_WRITETHROUGH_MODE(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW11_FEATURE_RESERVATION_NOTIFICATION_MASK(EasyCastStructure):
    _bitfield: UInt32
class NVME_CDW11_FEATURE_RESERVATION_PERSISTENCE(EasyCastStructure):
    _bitfield: UInt32
class NVME_CDW11_FEATURE_SET_HOST_METADATA(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW11_FEATURE_SUPPORTED_CAPABILITY(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW11_FEATURE_TEMPERATURE_THRESHOLD(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW11_FEATURE_VOLATILE_WRITE_CACHE(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW11_FEATURE_WRITE_ATOMICITY_NORMAL(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW11_FIRMWARE_DOWNLOAD(EasyCastStructure):
    OFST: UInt32
class NVME_CDW11_GET_LOG_PAGE(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW11_IDENTIFY(EasyCastUnion):
    Anonymous1: _Anonymous1_e__Struct
    Anonymous2: _Anonymous2_e__Struct
    AsUlong: UInt32
    class _Anonymous1_e__Struct(EasyCastStructure):
        NVMSETID: UInt16
        Reserved: UInt16
    class _Anonymous2_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW11_RESERVATION_REPORT(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW11_SANITIZE(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        OVRPAT: UInt32
class NVME_CDW11_SECURITY_RECEIVE(EasyCastStructure):
    AL: UInt32
class NVME_CDW11_SECURITY_SEND(EasyCastStructure):
    TL: UInt32
class NVME_CDW12_DIRECTIVE_RECEIVE(EasyCastUnion):
    AllocateResources: win32more.Windows.Win32.Storage.Nvme.NVME_CDW12_DIRECTIVE_RECEIVE_STREAMS_ALLOCATE_RESOURCES
    AsUlong: UInt32
class NVME_CDW12_DIRECTIVE_RECEIVE_STREAMS_ALLOCATE_RESOURCES(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW12_DIRECTIVE_SEND(EasyCastUnion):
    EnableDirective: win32more.Windows.Win32.Storage.Nvme.NVME_CDW12_DIRECTIVE_SEND_IDENTIFY_ENABLE_DIRECTIVE
    AsUlong: UInt32
class NVME_CDW12_DIRECTIVE_SEND_IDENTIFY_ENABLE_DIRECTIVE(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW12_FEATURES(EasyCastUnion):
    HostMemoryBuffer: win32more.Windows.Win32.Storage.Nvme.NVME_CDW12_FEATURE_HOST_MEMORY_BUFFER
    AsUlong: UInt32
class NVME_CDW12_FEATURE_HOST_MEMORY_BUFFER(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        HSIZE: UInt32
class NVME_CDW12_GET_LOG_PAGE(EasyCastStructure):
    LPOL: UInt32
class NVME_CDW12_READ_WRITE(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW12_ZONE_APPEND(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW13_FEATURES(EasyCastUnion):
    HostMemoryBuffer: win32more.Windows.Win32.Storage.Nvme.NVME_CDW13_FEATURE_HOST_MEMORY_BUFFER
    AsUlong: UInt32
class NVME_CDW13_FEATURE_HOST_MEMORY_BUFFER(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW13_GET_LOG_PAGE(EasyCastStructure):
    LPOU: UInt32
class NVME_CDW13_READ_WRITE(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        DSM: _DSM_e__Struct
        Reserved: Byte
        DSPEC: UInt16
        class _DSM_e__Struct(EasyCastStructure):
            _bitfield: Byte
class NVME_CDW13_ZONE_MANAGEMENT_RECEIVE(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW13_ZONE_MANAGEMENT_SEND(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW14_FEATURES(EasyCastUnion):
    HostMemoryBuffer: win32more.Windows.Win32.Storage.Nvme.NVME_CDW14_FEATURE_HOST_MEMORY_BUFFER
    AsUlong: UInt32
class NVME_CDW14_FEATURE_HOST_MEMORY_BUFFER(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        HMDLUA: UInt32
class NVME_CDW14_GET_LOG_PAGE(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW15_FEATURES(EasyCastUnion):
    HostMemoryBuffer: win32more.Windows.Win32.Storage.Nvme.NVME_CDW15_FEATURE_HOST_MEMORY_BUFFER
    AsUlong: UInt32
class NVME_CDW15_FEATURE_HOST_MEMORY_BUFFER(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        HMDLEC: UInt32
class NVME_CDW15_READ_WRITE(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CDW15_ZONE_APPEND(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CHANGED_NAMESPACE_LIST_LOG(EasyCastStructure):
    NSID: UInt32 * 1024
class NVME_CHANGED_ZONE_LIST_LOG(EasyCastStructure):
    ZoneIdentifiersCount: UInt16
    Reserved: Byte * 6
    ZoneIdentifier: UInt64 * 511
NVME_CMBSZ_SIZE_UNITS = Int32
NVME_CMBSZ_SIZE_UNITS_4KB: NVME_CMBSZ_SIZE_UNITS = 0
NVME_CMBSZ_SIZE_UNITS_64KB: NVME_CMBSZ_SIZE_UNITS = 1
NVME_CMBSZ_SIZE_UNITS_1MB: NVME_CMBSZ_SIZE_UNITS = 2
NVME_CMBSZ_SIZE_UNITS_16MB: NVME_CMBSZ_SIZE_UNITS = 3
NVME_CMBSZ_SIZE_UNITS_256MB: NVME_CMBSZ_SIZE_UNITS = 4
NVME_CMBSZ_SIZE_UNITS_4GB: NVME_CMBSZ_SIZE_UNITS = 5
NVME_CMBSZ_SIZE_UNITS_64GB: NVME_CMBSZ_SIZE_UNITS = 6
class NVME_COMMAND(EasyCastStructure):
    CDW0: win32more.Windows.Win32.Storage.Nvme.NVME_COMMAND_DWORD0
    NSID: UInt32
    Reserved0: UInt32 * 2
    MPTR: UInt64
    PRP1: UInt64
    PRP2: UInt64
    u: _u_e__Union
    class _u_e__Union(EasyCastUnion):
        GENERAL: _GENERAL_e__Struct
        IDENTIFY: _IDENTIFY_e__Struct
        ABORT: _ABORT_e__Struct
        GETFEATURES: _GETFEATURES_e__Struct
        SETFEATURES: _SETFEATURES_e__Struct
        GETLOGPAGE: _GETLOGPAGE_e__Struct
        CREATEIOCQ: _CREATEIOCQ_e__Struct
        CREATEIOSQ: _CREATEIOSQ_e__Struct
        DATASETMANAGEMENT: _DATASETMANAGEMENT_e__Struct
        SECURITYSEND: _SECURITYSEND_e__Struct
        SECURITYRECEIVE: _SECURITYRECEIVE_e__Struct
        FIRMWAREDOWNLOAD: _FIRMWAREDOWNLOAD_e__Struct
        FIRMWAREACTIVATE: _FIRMWAREACTIVATE_e__Struct
        FORMATNVM: _FORMATNVM_e__Struct
        DIRECTIVERECEIVE: _DIRECTIVERECEIVE_e__Struct
        DIRECTIVESEND: _DIRECTIVESEND_e__Struct
        SANITIZE: _SANITIZE_e__Struct
        READWRITE: _READWRITE_e__Struct
        RESERVATIONACQUIRE: _RESERVATIONACQUIRE_e__Struct
        RESERVATIONREGISTER: _RESERVATIONREGISTER_e__Struct
        RESERVATIONRELEASE: _RESERVATIONRELEASE_e__Struct
        RESERVATIONREPORT: _RESERVATIONREPORT_e__Struct
        ZONEMANAGEMENTSEND: _ZONEMANAGEMENTSEND_e__Struct
        ZONEMANAGEMENTRECEIVE: _ZONEMANAGEMENTRECEIVE_e__Struct
        ZONEAPPEND: _ZONEAPPEND_e__Struct
        class _GENERAL_e__Struct(EasyCastStructure):
            CDW10: UInt32
            CDW11: UInt32
            CDW12: UInt32
            CDW13: UInt32
            CDW14: UInt32
            CDW15: UInt32
        class _IDENTIFY_e__Struct(EasyCastStructure):
            CDW10: win32more.Windows.Win32.Storage.Nvme.NVME_CDW10_IDENTIFY
            CDW11: win32more.Windows.Win32.Storage.Nvme.NVME_CDW11_IDENTIFY
            CDW12: UInt32
            CDW13: UInt32
            CDW14: UInt32
            CDW15: UInt32
        class _ABORT_e__Struct(EasyCastStructure):
            CDW10: win32more.Windows.Win32.Storage.Nvme.NVME_CDW10_ABORT
            CDW11: UInt32
            CDW12: UInt32
            CDW13: UInt32
            CDW14: UInt32
            CDW15: UInt32
        class _GETFEATURES_e__Struct(EasyCastStructure):
            CDW10: win32more.Windows.Win32.Storage.Nvme.NVME_CDW10_GET_FEATURES
            CDW11: win32more.Windows.Win32.Storage.Nvme.NVME_CDW11_FEATURES
            CDW12: UInt32
            CDW13: UInt32
            CDW14: UInt32
            CDW15: UInt32
        class _SETFEATURES_e__Struct(EasyCastStructure):
            CDW10: win32more.Windows.Win32.Storage.Nvme.NVME_CDW10_SET_FEATURES
            CDW11: win32more.Windows.Win32.Storage.Nvme.NVME_CDW11_FEATURES
            CDW12: win32more.Windows.Win32.Storage.Nvme.NVME_CDW12_FEATURES
            CDW13: win32more.Windows.Win32.Storage.Nvme.NVME_CDW13_FEATURES
            CDW14: win32more.Windows.Win32.Storage.Nvme.NVME_CDW14_FEATURES
            CDW15: win32more.Windows.Win32.Storage.Nvme.NVME_CDW15_FEATURES
        class _GETLOGPAGE_e__Struct(EasyCastStructure):
            Anonymous: _Anonymous_e__Union
            CDW11: win32more.Windows.Win32.Storage.Nvme.NVME_CDW11_GET_LOG_PAGE
            CDW12: win32more.Windows.Win32.Storage.Nvme.NVME_CDW12_GET_LOG_PAGE
            CDW13: win32more.Windows.Win32.Storage.Nvme.NVME_CDW13_GET_LOG_PAGE
            CDW14: win32more.Windows.Win32.Storage.Nvme.NVME_CDW14_GET_LOG_PAGE
            CDW15: UInt32
            class _Anonymous_e__Union(EasyCastUnion):
                CDW10: win32more.Windows.Win32.Storage.Nvme.NVME_CDW10_GET_LOG_PAGE
                CDW10_V13: win32more.Windows.Win32.Storage.Nvme.NVME_CDW10_GET_LOG_PAGE_V13
        class _CREATEIOCQ_e__Struct(EasyCastStructure):
            CDW10: win32more.Windows.Win32.Storage.Nvme.NVME_CDW10_CREATE_IO_QUEUE
            CDW11: win32more.Windows.Win32.Storage.Nvme.NVME_CDW11_CREATE_IO_CQ
            CDW12: UInt32
            CDW13: UInt32
            CDW14: UInt32
            CDW15: UInt32
        class _CREATEIOSQ_e__Struct(EasyCastStructure):
            CDW10: win32more.Windows.Win32.Storage.Nvme.NVME_CDW10_CREATE_IO_QUEUE
            CDW11: win32more.Windows.Win32.Storage.Nvme.NVME_CDW11_CREATE_IO_SQ
            CDW12: UInt32
            CDW13: UInt32
            CDW14: UInt32
            CDW15: UInt32
        class _DATASETMANAGEMENT_e__Struct(EasyCastStructure):
            CDW10: win32more.Windows.Win32.Storage.Nvme.NVME_CDW10_DATASET_MANAGEMENT
            CDW11: win32more.Windows.Win32.Storage.Nvme.NVME_CDW11_DATASET_MANAGEMENT
            CDW12: UInt32
            CDW13: UInt32
            CDW14: UInt32
            CDW15: UInt32
        class _SECURITYSEND_e__Struct(EasyCastStructure):
            CDW10: win32more.Windows.Win32.Storage.Nvme.NVME_CDW10_SECURITY_SEND_RECEIVE
            CDW11: win32more.Windows.Win32.Storage.Nvme.NVME_CDW11_SECURITY_SEND
            CDW12: UInt32
            CDW13: UInt32
            CDW14: UInt32
            CDW15: UInt32
        class _SECURITYRECEIVE_e__Struct(EasyCastStructure):
            CDW10: win32more.Windows.Win32.Storage.Nvme.NVME_CDW10_SECURITY_SEND_RECEIVE
            CDW11: win32more.Windows.Win32.Storage.Nvme.NVME_CDW11_SECURITY_RECEIVE
            CDW12: UInt32
            CDW13: UInt32
            CDW14: UInt32
            CDW15: UInt32
        class _FIRMWAREDOWNLOAD_e__Struct(EasyCastStructure):
            CDW10: win32more.Windows.Win32.Storage.Nvme.NVME_CDW10_FIRMWARE_DOWNLOAD
            CDW11: win32more.Windows.Win32.Storage.Nvme.NVME_CDW11_FIRMWARE_DOWNLOAD
            CDW12: UInt32
            CDW13: UInt32
            CDW14: UInt32
            CDW15: UInt32
        class _FIRMWAREACTIVATE_e__Struct(EasyCastStructure):
            CDW10: win32more.Windows.Win32.Storage.Nvme.NVME_CDW10_FIRMWARE_ACTIVATE
            CDW11: UInt32
            CDW12: UInt32
            CDW13: UInt32
            CDW14: UInt32
            CDW15: UInt32
        class _FORMATNVM_e__Struct(EasyCastStructure):
            CDW10: win32more.Windows.Win32.Storage.Nvme.NVME_CDW10_FORMAT_NVM
            CDW11: UInt32
            CDW12: UInt32
            CDW13: UInt32
            CDW14: UInt32
            CDW15: UInt32
        class _DIRECTIVERECEIVE_e__Struct(EasyCastStructure):
            CDW10: win32more.Windows.Win32.Storage.Nvme.NVME_CDW10_DIRECTIVE_RECEIVE
            CDW11: win32more.Windows.Win32.Storage.Nvme.NVME_CDW11_DIRECTIVE_RECEIVE
            CDW12: win32more.Windows.Win32.Storage.Nvme.NVME_CDW12_DIRECTIVE_RECEIVE
            CDW13: UInt32
            CDW14: UInt32
            CDW15: UInt32
        class _DIRECTIVESEND_e__Struct(EasyCastStructure):
            CDW10: win32more.Windows.Win32.Storage.Nvme.NVME_CDW10_DIRECTIVE_SEND
            CDW11: win32more.Windows.Win32.Storage.Nvme.NVME_CDW11_DIRECTIVE_SEND
            CDW12: win32more.Windows.Win32.Storage.Nvme.NVME_CDW12_DIRECTIVE_SEND
            CDW13: UInt32
            CDW14: UInt32
            CDW15: UInt32
        class _SANITIZE_e__Struct(EasyCastStructure):
            CDW10: win32more.Windows.Win32.Storage.Nvme.NVME_CDW10_SANITIZE
            CDW11: win32more.Windows.Win32.Storage.Nvme.NVME_CDW11_SANITIZE
            CDW12: UInt32
            CDW13: UInt32
            CDW14: UInt32
            CDW15: UInt32
        class _READWRITE_e__Struct(EasyCastStructure):
            LBALOW: UInt32
            LBAHIGH: UInt32
            CDW12: win32more.Windows.Win32.Storage.Nvme.NVME_CDW12_READ_WRITE
            CDW13: win32more.Windows.Win32.Storage.Nvme.NVME_CDW13_READ_WRITE
            CDW14: UInt32
            CDW15: win32more.Windows.Win32.Storage.Nvme.NVME_CDW15_READ_WRITE
        class _RESERVATIONACQUIRE_e__Struct(EasyCastStructure):
            CDW10: win32more.Windows.Win32.Storage.Nvme.NVME_CDW10_RESERVATION_ACQUIRE
            CDW11: UInt32
            CDW12: UInt32
            CDW13: UInt32
            CDW14: UInt32
            CDW15: UInt32
        class _RESERVATIONREGISTER_e__Struct(EasyCastStructure):
            CDW10: win32more.Windows.Win32.Storage.Nvme.NVME_CDW10_RESERVATION_REGISTER
            CDW11: UInt32
            CDW12: UInt32
            CDW13: UInt32
            CDW14: UInt32
            CDW15: UInt32
        class _RESERVATIONRELEASE_e__Struct(EasyCastStructure):
            CDW10: win32more.Windows.Win32.Storage.Nvme.NVME_CDW10_RESERVATION_RELEASE
            CDW11: UInt32
            CDW12: UInt32
            CDW13: UInt32
            CDW14: UInt32
            CDW15: UInt32
        class _RESERVATIONREPORT_e__Struct(EasyCastStructure):
            CDW10: win32more.Windows.Win32.Storage.Nvme.NVME_CDW10_RESERVATION_REPORT
            CDW11: win32more.Windows.Win32.Storage.Nvme.NVME_CDW11_RESERVATION_REPORT
            CDW12: UInt32
            CDW13: UInt32
            CDW14: UInt32
            CDW15: UInt32
        class _ZONEMANAGEMENTSEND_e__Struct(EasyCastStructure):
            CDW1011: win32more.Windows.Win32.Storage.Nvme.NVME_CDW10_ZONE_MANAGEMENT_SEND
            CDW12: UInt32
            CDW13: win32more.Windows.Win32.Storage.Nvme.NVME_CDW13_ZONE_MANAGEMENT_SEND
            CDW14: UInt32
            CDW15: UInt32
        class _ZONEMANAGEMENTRECEIVE_e__Struct(EasyCastStructure):
            CDW1011: win32more.Windows.Win32.Storage.Nvme.NVME_CDW10_ZONE_MANAGEMENT_RECEIVE
            DWORDCOUNT: UInt32
            CDW13: win32more.Windows.Win32.Storage.Nvme.NVME_CDW13_ZONE_MANAGEMENT_RECEIVE
            CDW14: UInt32
            CDW15: UInt32
        class _ZONEAPPEND_e__Struct(EasyCastStructure):
            CDW1011: win32more.Windows.Win32.Storage.Nvme.NVME_CDW10_ZONE_APPEND
            CDW12: win32more.Windows.Win32.Storage.Nvme.NVME_CDW12_ZONE_APPEND
            CDW13: UInt32
            ILBRT: UInt32
            CDW15: win32more.Windows.Win32.Storage.Nvme.NVME_CDW15_ZONE_APPEND
class NVME_COMMAND_DWORD0(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_COMMAND_EFFECTS_DATA(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_COMMAND_EFFECTS_LOG(EasyCastStructure):
    ACS: win32more.Windows.Win32.Storage.Nvme.NVME_COMMAND_EFFECTS_DATA * 256
    IOCS: win32more.Windows.Win32.Storage.Nvme.NVME_COMMAND_EFFECTS_DATA * 256
    Reserved: Byte * 2048
NVME_COMMAND_EFFECT_SBUMISSION_EXECUTION_LIMITS = Int32
NVME_COMMAND_EFFECT_SBUMISSION_EXECUTION_LIMIT_NONE: NVME_COMMAND_EFFECT_SBUMISSION_EXECUTION_LIMITS = 0
NVME_COMMAND_EFFECT_SBUMISSION_EXECUTION_LIMIT_SINGLE_PER_NAMESPACE: NVME_COMMAND_EFFECT_SBUMISSION_EXECUTION_LIMITS = 1
NVME_COMMAND_EFFECT_SBUMISSION_EXECUTION_LIMIT_SINGLE_PER_CONTROLLER: NVME_COMMAND_EFFECT_SBUMISSION_EXECUTION_LIMITS = 2
NVME_COMMAND_SET_IDENTIFIERS = Int32
NVME_COMMAND_SET_NVM: NVME_COMMAND_SET_IDENTIFIERS = 0
NVME_COMMAND_SET_KEY_VALUE: NVME_COMMAND_SET_IDENTIFIERS = 1
NVME_COMMAND_SET_ZONED_NAMESPACE: NVME_COMMAND_SET_IDENTIFIERS = 2
class NVME_COMMAND_STATUS(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUshort: UInt16
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt16
class NVME_COMPLETION_DW0_ASYNC_EVENT_REQUEST(EasyCastStructure):
    _bitfield: UInt32
class NVME_COMPLETION_DW0_DIRECTIVE_RECEIVE_STREAMS_ALLOCATE_RESOURCES(EasyCastStructure):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_COMPLETION_ENTRY(EasyCastStructure):
    DW0: UInt32
    DW1: UInt32
    DW2: _DW2_e__Union
    DW3: _DW3_e__Union
    class _DW2_e__Union(EasyCastUnion):
        Anonymous: _Anonymous_e__Struct
        AsUlong: UInt32
        class _Anonymous_e__Struct(EasyCastStructure):
            SQHD: UInt16
            SQID: UInt16
    class _DW3_e__Union(EasyCastUnion):
        Anonymous: _Anonymous_e__Struct
        AsUlong: UInt32
        class _Anonymous_e__Struct(EasyCastStructure):
            CID: UInt16
            Status: win32more.Windows.Win32.Storage.Nvme.NVME_COMMAND_STATUS
class NVME_COMPLETION_QUEUE_HEAD_DOORBELL(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CONTEXT_ATTRIBUTES(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CONTROLLER_CAPABILITIES(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlonglong: UInt64
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt64
class NVME_CONTROLLER_CONFIGURATION(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CONTROLLER_LIST(EasyCastStructure):
    NumberOfIdentifiers: UInt16
    ControllerID: UInt16 * 2047
class NVME_CONTROLLER_MEMORY_BUFFER_LOCATION(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_CONTROLLER_MEMORY_BUFFER_SIZE(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
NVME_CONTROLLER_METADATA_ELEMENT_TYPES = Int32
NVME_CONTROLLER_METADATA_OPERATING_SYSTEM_CONTROLLER_NAME: NVME_CONTROLLER_METADATA_ELEMENT_TYPES = 1
NVME_CONTROLLER_METADATA_OPERATING_SYSTEM_DRIVER_NAME: NVME_CONTROLLER_METADATA_ELEMENT_TYPES = 2
NVME_CONTROLLER_METADATA_OPERATING_SYSTEM_DRIVER_VERSION: NVME_CONTROLLER_METADATA_ELEMENT_TYPES = 3
NVME_CONTROLLER_METADATA_PREBOOT_CONTROLLER_NAME: NVME_CONTROLLER_METADATA_ELEMENT_TYPES = 4
NVME_CONTROLLER_METADATA_PREBOOT_DRIVER_NAME: NVME_CONTROLLER_METADATA_ELEMENT_TYPES = 5
NVME_CONTROLLER_METADATA_PREBOOT_DRIVER_VERSION: NVME_CONTROLLER_METADATA_ELEMENT_TYPES = 6
NVME_CONTROLLER_METADATA_SYSTEM_PROCESSOR_MODEL: NVME_CONTROLLER_METADATA_ELEMENT_TYPES = 7
NVME_CONTROLLER_METADATA_CHIPSET_DRIVER_NAME: NVME_CONTROLLER_METADATA_ELEMENT_TYPES = 8
NVME_CONTROLLER_METADATA_CHIPSET_DRIVER_VERSION: NVME_CONTROLLER_METADATA_ELEMENT_TYPES = 9
NVME_CONTROLLER_METADATA_OPERATING_SYSTEM_NAME_AND_BUILD: NVME_CONTROLLER_METADATA_ELEMENT_TYPES = 10
NVME_CONTROLLER_METADATA_SYSTEM_PRODUCT_NAME: NVME_CONTROLLER_METADATA_ELEMENT_TYPES = 11
NVME_CONTROLLER_METADATA_FIRMWARE_VERSION: NVME_CONTROLLER_METADATA_ELEMENT_TYPES = 12
NVME_CONTROLLER_METADATA_OPERATING_SYSTEM_DRIVER_FILENAME: NVME_CONTROLLER_METADATA_ELEMENT_TYPES = 13
NVME_CONTROLLER_METADATA_DISPLAY_DRIVER_NAME: NVME_CONTROLLER_METADATA_ELEMENT_TYPES = 14
NVME_CONTROLLER_METADATA_DISPLAY_DRIVER_VERSION: NVME_CONTROLLER_METADATA_ELEMENT_TYPES = 15
NVME_CONTROLLER_METADATA_HOST_DETERMINED_FAILURE_RECORD: NVME_CONTROLLER_METADATA_ELEMENT_TYPES = 16
class NVME_CONTROLLER_REGISTERS(EasyCastStructure):
    CAP: win32more.Windows.Win32.Storage.Nvme.NVME_CONTROLLER_CAPABILITIES
    VS: win32more.Windows.Win32.Storage.Nvme.NVME_VERSION
    INTMS: UInt32
    INTMC: UInt32
    CC: win32more.Windows.Win32.Storage.Nvme.NVME_CONTROLLER_CONFIGURATION
    Reserved0: UInt32
    CSTS: win32more.Windows.Win32.Storage.Nvme.NVME_CONTROLLER_STATUS
    NSSR: win32more.Windows.Win32.Storage.Nvme.NVME_NVM_SUBSYSTEM_RESET
    AQA: win32more.Windows.Win32.Storage.Nvme.NVME_ADMIN_QUEUE_ATTRIBUTES
    ASQ: win32more.Windows.Win32.Storage.Nvme.NVME_ADMIN_SUBMISSION_QUEUE_BASE_ADDRESS
    ACQ: win32more.Windows.Win32.Storage.Nvme.NVME_ADMIN_COMPLETION_QUEUE_BASE_ADDRESS
    CMBLOC: win32more.Windows.Win32.Storage.Nvme.NVME_CONTROLLER_MEMORY_BUFFER_LOCATION
    CMBSZ: win32more.Windows.Win32.Storage.Nvme.NVME_CONTROLLER_MEMORY_BUFFER_SIZE
    Reserved2: UInt32 * 944
    Reserved3: UInt32 * 64
    Doorbells: UInt32 * 1
class NVME_CONTROLLER_STATUS(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
NVME_CSS_COMMAND_SETS = Int32
NVME_CSS_NVM_COMMAND_SET: NVME_CSS_COMMAND_SETS = 0
NVME_CSS_ALL_SUPPORTED_IO_COMMAND_SET: NVME_CSS_COMMAND_SETS = 6
NVME_CSS_ADMIN_COMMAND_SET_ONLY: NVME_CSS_COMMAND_SETS = 7
NVME_CSTS_SHST_SHUTDOWN_STATUS = Int32
NVME_CSTS_SHST_NO_SHUTDOWN: NVME_CSTS_SHST_SHUTDOWN_STATUS = 0
NVME_CSTS_SHST_SHUTDOWN_IN_PROCESS: NVME_CSTS_SHST_SHUTDOWN_STATUS = 1
NVME_CSTS_SHST_SHUTDOWN_COMPLETED: NVME_CSTS_SHST_SHUTDOWN_STATUS = 2
class NVME_DEVICE_SELF_TEST_LOG(EasyCastStructure):
    CurrentOperation: _CurrentOperation_e__Struct
    CurrentCompletion: _CurrentCompletion_e__Struct
    Reserved: Byte * 2
    ResultData: win32more.Windows.Win32.Storage.Nvme.NVME_DEVICE_SELF_TEST_RESULT_DATA * 20
    class _CurrentOperation_e__Struct(EasyCastStructure):
        _bitfield: Byte
    class _CurrentCompletion_e__Struct(EasyCastStructure):
        _bitfield: Byte
class NVME_DEVICE_SELF_TEST_RESULT_DATA(EasyCastStructure):
    Status: _Status_e__Struct
    SegmentNumber: Byte
    ValidDiagnostics: _ValidDiagnostics_e__Struct
    Reserved: Byte
    POH: UInt64
    NSID: UInt32
    FailingLBA: UInt64
    StatusCodeType: _StatusCodeType_e__Struct
    StatusCode: Byte
    VendorSpecific: UInt16
    _pack_ = 1
    class _Status_e__Struct(EasyCastStructure):
        _bitfield: Byte
    class _ValidDiagnostics_e__Struct(EasyCastStructure):
        _bitfield: Byte
    class _StatusCodeType_e__Struct(EasyCastStructure):
        _bitfield: Byte
class NVME_DIRECTIVE_IDENTIFY_RETURN_PARAMETERS(EasyCastStructure):
    DirectivesSupported: win32more.Windows.Win32.Storage.Nvme.NVME_DIRECTIVE_IDENTIFY_RETURN_PARAMETERS_DESCRIPTOR
    DirectivesEnabled: win32more.Windows.Win32.Storage.Nvme.NVME_DIRECTIVE_IDENTIFY_RETURN_PARAMETERS_DESCRIPTOR
class NVME_DIRECTIVE_IDENTIFY_RETURN_PARAMETERS_DESCRIPTOR(EasyCastStructure):
    _bitfield: Byte
    Reserved1: Byte * 31
NVME_DIRECTIVE_RECEIVE_IDENTIFY_OPERATIONS = Int32
NVME_DIRECTIVE_RECEIVE_IDENTIFY_OPERATION_RETURN_PARAMETERS: NVME_DIRECTIVE_RECEIVE_IDENTIFY_OPERATIONS = 1
NVME_DIRECTIVE_RECEIVE_STREAMS_OPERATIONS = Int32
NVME_DIRECTIVE_RECEIVE_STREAMS_OPERATION_RETURN_PARAMETERS: NVME_DIRECTIVE_RECEIVE_STREAMS_OPERATIONS = 1
NVME_DIRECTIVE_RECEIVE_STREAMS_OPERATION_GET_STATUS: NVME_DIRECTIVE_RECEIVE_STREAMS_OPERATIONS = 2
NVME_DIRECTIVE_RECEIVE_STREAMS_OPERATION_ALLOCATE_RESOURCES: NVME_DIRECTIVE_RECEIVE_STREAMS_OPERATIONS = 3
NVME_DIRECTIVE_SEND_IDENTIFY_OPERATIONS = Int32
NVME_DIRECTIVE_SEND_IDENTIFY_OPERATION_ENABLE_DIRECTIVE: NVME_DIRECTIVE_SEND_IDENTIFY_OPERATIONS = 1
NVME_DIRECTIVE_SEND_STREAMS_OPERATIONS = Int32
NVME_DIRECTIVE_SEND_STREAMS_OPERATION_RELEASE_IDENTIFIER: NVME_DIRECTIVE_SEND_STREAMS_OPERATIONS = 1
NVME_DIRECTIVE_SEND_STREAMS_OPERATION_RELEASE_RESOURCES: NVME_DIRECTIVE_SEND_STREAMS_OPERATIONS = 2
class NVME_DIRECTIVE_STREAMS_GET_STATUS_DATA(EasyCastStructure):
    OpenStreamCount: UInt16
    StreamIdentifiers: UInt16 * 65535
class NVME_DIRECTIVE_STREAMS_RETURN_PARAMETERS(EasyCastStructure):
    MSL: UInt16
    NSSA: UInt16
    NSSO: UInt16
    Reserved0: Byte * 10
    SWS: UInt32
    SGS: UInt16
    NSA: UInt16
    NSO: UInt16
    Reserved1: Byte * 6
NVME_DIRECTIVE_TYPES = Int32
NVME_DIRECTIVE_TYPE_IDENTIFY: NVME_DIRECTIVE_TYPES = 0
NVME_DIRECTIVE_TYPE_STREAMS: NVME_DIRECTIVE_TYPES = 1
class NVME_ENDURANCE_GROUP_LOG(EasyCastStructure):
    Reserved0: UInt32
    AvailableSpareThreshold: Byte
    PercentageUsed: Byte
    Reserved1: Byte * 26
    EnduranceEstimate: Byte * 16
    DataUnitsRead: Byte * 16
    DataUnitsWritten: Byte * 16
    MediaUnitsWritten: Byte * 16
    Reserved2: Byte * 416
    _pack_ = 1
class NVME_ERROR_INFO_LOG(EasyCastStructure):
    ErrorCount: UInt64
    SQID: UInt16
    CMDID: UInt16
    Status: win32more.Windows.Win32.Storage.Nvme.NVME_COMMAND_STATUS
    ParameterErrorLocation: _ParameterErrorLocation_e__Struct
    Lba: UInt64
    NameSpace: UInt32
    VendorInfoAvailable: Byte
    Reserved0: Byte * 3
    CommandSpecificInfo: UInt64
    Reserved1: Byte * 24
    class _ParameterErrorLocation_e__Struct(EasyCastStructure):
        _bitfield: UInt16
class NVME_ERROR_INJECTION_ENTRY(EasyCastStructure):
    Flags: _Flags_e__Union
    Reserved1: Byte
    ErrorInjectionType: UInt16
    ErrorInjectionTypeSpecific: Byte * 28
    class _Flags_e__Union(EasyCastUnion):
        Anonymous: _Anonymous_e__Struct
        AsUchar: Byte
        class _Anonymous_e__Struct(EasyCastStructure):
            _bitfield: Byte
NVME_ERROR_INJECTION_TYPES = Int32
NVME_ERROR_INJECTION_TYPE_RESERVED0: NVME_ERROR_INJECTION_TYPES = 0
NVME_ERROR_INJECTION_TYPE_DEVICE_PANIC_CPU_CONTROLLER_HANG: NVME_ERROR_INJECTION_TYPES = 1
NVME_ERROR_INJECTION_TYPE_DEVICE_PANIC_NAND_HANG: NVME_ERROR_INJECTION_TYPES = 2
NVME_ERROR_INJECTION_TYPE_DEVICE_PANIC_PLP_DEFECT: NVME_ERROR_INJECTION_TYPES = 3
NVME_ERROR_INJECTION_TYPE_DEVICE_PANIC_LOGICAL_FW_ERROR: NVME_ERROR_INJECTION_TYPES = 4
NVME_ERROR_INJECTION_TYPE_DEVICE_PANIC_DRAM_CORRUPTION_CRITICAL: NVME_ERROR_INJECTION_TYPES = 5
NVME_ERROR_INJECTION_TYPE_DEVICE_PANIC_DRAM_CORRUPTION_NONCRITICAL: NVME_ERROR_INJECTION_TYPES = 6
NVME_ERROR_INJECTION_TYPE_DEVICE_PANIC_NAND_CORRUPTION: NVME_ERROR_INJECTION_TYPES = 7
NVME_ERROR_INJECTION_TYPE_DEVICE_PANIC_SRAM_CORRUPTION: NVME_ERROR_INJECTION_TYPES = 8
NVME_ERROR_INJECTION_TYPE_DEVICE_PANIC_HW_MALFUNCTION: NVME_ERROR_INJECTION_TYPES = 9
NVME_ERROR_INJECTION_TYPE_RESERVED1: NVME_ERROR_INJECTION_TYPES = 10
NVME_ERROR_INJECTION_TYPE_MAX: NVME_ERROR_INJECTION_TYPES = 65535
class NVME_EXTENDED_REPORT_ZONE_INFO(EasyCastStructure):
    ZoneCount: UInt64
    Reserved: UInt64 * 7
    Desc: win32more.Windows.Win32.Storage.Nvme.NVME_ZONE_EXTENDED_REPORT_ZONE_DESC * 1
NVME_FEATURES = Int32
NVME_FEATURE_ARBITRATION: NVME_FEATURES = 1
NVME_FEATURE_POWER_MANAGEMENT: NVME_FEATURES = 2
NVME_FEATURE_LBA_RANGE_TYPE: NVME_FEATURES = 3
NVME_FEATURE_TEMPERATURE_THRESHOLD: NVME_FEATURES = 4
NVME_FEATURE_ERROR_RECOVERY: NVME_FEATURES = 5
NVME_FEATURE_VOLATILE_WRITE_CACHE: NVME_FEATURES = 6
NVME_FEATURE_NUMBER_OF_QUEUES: NVME_FEATURES = 7
NVME_FEATURE_INTERRUPT_COALESCING: NVME_FEATURES = 8
NVME_FEATURE_INTERRUPT_VECTOR_CONFIG: NVME_FEATURES = 9
NVME_FEATURE_WRITE_ATOMICITY: NVME_FEATURES = 10
NVME_FEATURE_ASYNC_EVENT_CONFIG: NVME_FEATURES = 11
NVME_FEATURE_AUTONOMOUS_POWER_STATE_TRANSITION: NVME_FEATURES = 12
NVME_FEATURE_HOST_MEMORY_BUFFER: NVME_FEATURES = 13
NVME_FEATURE_TIMESTAMP: NVME_FEATURES = 14
NVME_FEATURE_KEEP_ALIVE: NVME_FEATURES = 15
NVME_FEATURE_HOST_CONTROLLED_THERMAL_MANAGEMENT: NVME_FEATURES = 16
NVME_FEATURE_NONOPERATIONAL_POWER_STATE: NVME_FEATURES = 17
NVME_FEATURE_READ_RECOVERY_LEVEL_CONFIG: NVME_FEATURES = 18
NVME_FEATURE_PREDICTABLE_LATENCY_MODE_CONFIG: NVME_FEATURES = 19
NVME_FEATURE_PREDICTABLE_LATENCY_MODE_WINDOW: NVME_FEATURES = 20
NVME_FEATURE_LBA_STATUS_INFORMATION_REPORT_INTERVAL: NVME_FEATURES = 21
NVME_FEATURE_HOST_BEHAVIOR_SUPPORT: NVME_FEATURES = 22
NVME_FEATURE_SANITIZE_CONFIG: NVME_FEATURES = 23
NVME_FEATURE_ENDURANCE_GROUP_EVENT_CONFIG: NVME_FEATURES = 24
NVME_FEATURE_IO_COMMAND_SET_PROFILE: NVME_FEATURES = 25
NVME_FEATURE_ENHANCED_CONTROLLER_METADATA: NVME_FEATURES = 125
NVME_FEATURE_CONTROLLER_METADATA: NVME_FEATURES = 126
NVME_FEATURE_NAMESPACE_METADATA: NVME_FEATURES = 127
NVME_FEATURE_NVM_SOFTWARE_PROGRESS_MARKER: NVME_FEATURES = 128
NVME_FEATURE_NVM_HOST_IDENTIFIER: NVME_FEATURES = 129
NVME_FEATURE_NVM_RESERVATION_NOTIFICATION_MASK: NVME_FEATURES = 130
NVME_FEATURE_NVM_RESERVATION_PERSISTANCE: NVME_FEATURES = 131
NVME_FEATURE_NVM_NAMESPACE_WRITE_PROTECTION_CONFIG: NVME_FEATURES = 132
NVME_FEATURE_ERROR_INJECTION: NVME_FEATURES = 192
NVME_FEATURE_CLEAR_FW_UPDATE_HISTORY: NVME_FEATURES = 193
NVME_FEATURE_READONLY_WRITETHROUGH_MODE: NVME_FEATURES = 194
NVME_FEATURE_CLEAR_PCIE_CORRECTABLE_ERROR_COUNTERS: NVME_FEATURES = 195
NVME_FEATURE_ENABLE_IEEE1667_SILO: NVME_FEATURES = 196
NVME_FEATURE_PLP_HEALTH_MONITOR: NVME_FEATURES = 197
class NVME_FEATURE_HOST_IDENTIFIER_DATA(EasyCastStructure):
    HOSTID: Byte * 16
class NVME_FEATURE_HOST_METADATA_DATA(EasyCastStructure):
    NumberOfMetadataElementDescriptors: Byte
    Reserved0: Byte
    MetadataElementDescriptors: Byte * 4094
NVME_FEATURE_VALUE_CODES = Int32
NVME_FEATURE_VALUE_CURRENT: NVME_FEATURE_VALUE_CODES = 0
NVME_FEATURE_VALUE_DEFAULT: NVME_FEATURE_VALUE_CODES = 1
NVME_FEATURE_VALUE_SAVED: NVME_FEATURE_VALUE_CODES = 2
NVME_FEATURE_VALUE_SUPPORTED_CAPABILITIES: NVME_FEATURE_VALUE_CODES = 3
NVME_FIRMWARE_ACTIVATE_ACTIONS = Int32
NVME_FIRMWARE_ACTIVATE_ACTION_DOWNLOAD_TO_SLOT: NVME_FIRMWARE_ACTIVATE_ACTIONS = 0
NVME_FIRMWARE_ACTIVATE_ACTION_DOWNLOAD_TO_SLOT_AND_ACTIVATE: NVME_FIRMWARE_ACTIVATE_ACTIONS = 1
NVME_FIRMWARE_ACTIVATE_ACTION_ACTIVATE: NVME_FIRMWARE_ACTIVATE_ACTIONS = 2
NVME_FIRMWARE_ACTIVATE_ACTION_DOWNLOAD_TO_SLOT_AND_ACTIVATE_IMMEDIATE: NVME_FIRMWARE_ACTIVATE_ACTIONS = 3
class NVME_FIRMWARE_SLOT_INFO_LOG(EasyCastStructure):
    AFI: _AFI_e__Struct
    Reserved0: Byte * 7
    FRS: UInt64 * 7
    Reserved1: Byte * 448
    class _AFI_e__Struct(EasyCastStructure):
        _bitfield: Byte
NVME_FUSED_OPERATION_CODES = Int32
NVME_FUSED_OPERATION_NORMAL: NVME_FUSED_OPERATION_CODES = 0
NVME_FUSED_OPERATION_FIRST_CMD: NVME_FUSED_OPERATION_CODES = 1
NVME_FUSED_OPERATION_SECOND_CMD: NVME_FUSED_OPERATION_CODES = 2
class NVME_HEALTH_INFO_LOG(EasyCastStructure):
    CriticalWarning: _CriticalWarning_e__Union
    Temperature: Byte * 2
    AvailableSpare: Byte
    AvailableSpareThreshold: Byte
    PercentageUsed: Byte
    Reserved0: Byte * 26
    DataUnitRead: Byte * 16
    DataUnitWritten: Byte * 16
    HostReadCommands: Byte * 16
    HostWrittenCommands: Byte * 16
    ControllerBusyTime: Byte * 16
    PowerCycle: Byte * 16
    PowerOnHours: Byte * 16
    UnsafeShutdowns: Byte * 16
    MediaErrors: Byte * 16
    ErrorInfoLogEntryCount: Byte * 16
    WarningCompositeTemperatureTime: UInt32
    CriticalCompositeTemperatureTime: UInt32
    TemperatureSensor1: UInt16
    TemperatureSensor2: UInt16
    TemperatureSensor3: UInt16
    TemperatureSensor4: UInt16
    TemperatureSensor5: UInt16
    TemperatureSensor6: UInt16
    TemperatureSensor7: UInt16
    TemperatureSensor8: UInt16
    Reserved1: Byte * 296
    class _CriticalWarning_e__Union(EasyCastUnion):
        Anonymous: _Anonymous_e__Struct
        AsUchar: Byte
        class _Anonymous_e__Struct(EasyCastStructure):
            _bitfield: Byte
class NVME_HOST_MEMORY_BUFFER_DESCRIPTOR_ENTRY(EasyCastStructure):
    BADD: UInt64
    BSIZE: UInt32
    Reserved: UInt32
NVME_HOST_METADATA_ELEMENT_ACTIONS = Int32
NVME_HOST_METADATA_ADD_REPLACE_ENTRY: NVME_HOST_METADATA_ELEMENT_ACTIONS = 0
NVME_HOST_METADATA_DELETE_ENTRY_MULTIPLE: NVME_HOST_METADATA_ELEMENT_ACTIONS = 1
NVME_HOST_METADATA_ADD_ENTRY_MULTIPLE: NVME_HOST_METADATA_ELEMENT_ACTIONS = 2
class NVME_HOST_METADATA_ELEMENT_DESCRIPTOR(EasyCastStructure):
    _bitfield: UInt32
    EVAL: Byte * 1
NVME_IDENTIFIER_TYPE = Int32
NVME_IDENTIFIER_TYPE_EUI64: NVME_IDENTIFIER_TYPE = 1
NVME_IDENTIFIER_TYPE_NGUID: NVME_IDENTIFIER_TYPE = 2
NVME_IDENTIFIER_TYPE_UUID: NVME_IDENTIFIER_TYPE = 3
NVME_IDENTIFIER_TYPE_CSI: NVME_IDENTIFIER_TYPE = 4
NVME_IDENTIFIER_TYPE_LENGTH = Int32
NVME_IDENTIFIER_TYPE_EUI64_LENGTH: NVME_IDENTIFIER_TYPE_LENGTH = 8
NVME_IDENTIFIER_TYPE_NGUID_LENGTH: NVME_IDENTIFIER_TYPE_LENGTH = 16
NVME_IDENTIFIER_TYPE_UUID_LENGTH: NVME_IDENTIFIER_TYPE_LENGTH = 16
NVME_IDENTIFIER_TYPE_CSI_LENGTH: NVME_IDENTIFIER_TYPE_LENGTH = 1
NVME_IDENTIFY_CNS_CODES = Int32
NVME_IDENTIFY_CNS_SPECIFIC_NAMESPACE: NVME_IDENTIFY_CNS_CODES = 0
NVME_IDENTIFY_CNS_CONTROLLER: NVME_IDENTIFY_CNS_CODES = 1
NVME_IDENTIFY_CNS_ACTIVE_NAMESPACES: NVME_IDENTIFY_CNS_CODES = 2
NVME_IDENTIFY_CNS_DESCRIPTOR_NAMESPACE: NVME_IDENTIFY_CNS_CODES = 3
NVME_IDENTIFY_CNS_NVM_SET: NVME_IDENTIFY_CNS_CODES = 4
NVME_IDENTIFY_CNS_SPECIFIC_NAMESPACE_IO_COMMAND_SET: NVME_IDENTIFY_CNS_CODES = 5
NVME_IDENTIFY_CNS_SPECIFIC_CONTROLLER_IO_COMMAND_SET: NVME_IDENTIFY_CNS_CODES = 6
NVME_IDENTIFY_CNS_ACTIVE_NAMESPACE_LIST_IO_COMMAND_SET: NVME_IDENTIFY_CNS_CODES = 7
NVME_IDENTIFY_CNS_ALLOCATED_NAMESPACE_LIST: NVME_IDENTIFY_CNS_CODES = 16
NVME_IDENTIFY_CNS_ALLOCATED_NAMESPACE: NVME_IDENTIFY_CNS_CODES = 17
NVME_IDENTIFY_CNS_CONTROLLER_LIST_OF_NSID: NVME_IDENTIFY_CNS_CODES = 18
NVME_IDENTIFY_CNS_CONTROLLER_LIST_OF_NVM_SUBSYSTEM: NVME_IDENTIFY_CNS_CODES = 19
NVME_IDENTIFY_CNS_PRIMARY_CONTROLLER_CAPABILITIES: NVME_IDENTIFY_CNS_CODES = 20
NVME_IDENTIFY_CNS_SECONDARY_CONTROLLER_LIST: NVME_IDENTIFY_CNS_CODES = 21
NVME_IDENTIFY_CNS_NAMESPACE_GRANULARITY_LIST: NVME_IDENTIFY_CNS_CODES = 22
NVME_IDENTIFY_CNS_UUID_LIST: NVME_IDENTIFY_CNS_CODES = 23
NVME_IDENTIFY_CNS_DOMAIN_LIST: NVME_IDENTIFY_CNS_CODES = 24
NVME_IDENTIFY_CNS_ENDURANCE_GROUP_LIST: NVME_IDENTIFY_CNS_CODES = 25
NVME_IDENTIFY_CNS_ALLOCATED_NAMSPACE_LIST_IO_COMMAND_SET: NVME_IDENTIFY_CNS_CODES = 26
NVME_IDENTIFY_CNS_ALLOCATED_NAMESPACE_IO_COMMAND_SET: NVME_IDENTIFY_CNS_CODES = 27
NVME_IDENTIFY_CNS_IO_COMMAND_SET: NVME_IDENTIFY_CNS_CODES = 28
class NVME_IDENTIFY_CONTROLLER_DATA(EasyCastStructure):
    VID: UInt16
    SSVID: UInt16
    SN: Byte * 20
    MN: Byte * 40
    FR: Byte * 8
    RAB: Byte
    IEEE: Byte * 3
    CMIC: _CMIC_e__Struct
    MDTS: Byte
    CNTLID: UInt16
    VER: UInt32
    RTD3R: UInt32
    RTD3E: UInt32
    OAES: _OAES_e__Struct
    CTRATT: _CTRATT_e__Struct
    RRLS: _RRLS_e__Struct
    Reserved0: Byte * 9
    CNTRLTYPE: Byte
    FGUID: Byte * 16
    CRDT1: UInt16
    CRDT2: UInt16
    CRDT3: UInt16
    Reserved0_1: Byte * 106
    ReservedForManagement: Byte * 16
    OACS: _OACS_e__Struct
    ACL: Byte
    AERL: Byte
    FRMW: _FRMW_e__Struct
    LPA: _LPA_e__Struct
    ELPE: Byte
    NPSS: Byte
    AVSCC: _AVSCC_e__Struct
    APSTA: _APSTA_e__Struct
    WCTEMP: UInt16
    CCTEMP: UInt16
    MTFA: UInt16
    HMPRE: UInt32
    HMMIN: UInt32
    TNVMCAP: Byte * 16
    UNVMCAP: Byte * 16
    RPMBS: _RPMBS_e__Struct
    EDSTT: UInt16
    DSTO: Byte
    FWUG: Byte
    KAS: UInt16
    HCTMA: _HCTMA_e__Struct
    MNTMT: UInt16
    MXTMT: UInt16
    SANICAP: _SANICAP_e__Struct
    HMMINDS: UInt32
    HMMAXD: UInt16
    NSETIDMAX: UInt16
    ENDGIDMAX: UInt16
    ANATT: Byte
    ANACAP: _ANACAP_e__Struct
    ANAGRPMAX: UInt32
    NANAGRPID: UInt32
    PELS: UInt32
    Reserved1: Byte * 156
    SQES: _SQES_e__Struct
    CQES: _CQES_e__Struct
    MAXCMD: UInt16
    NN: UInt32
    ONCS: _ONCS_e__Struct
    FUSES: _FUSES_e__Struct
    FNA: _FNA_e__Struct
    VWC: _VWC_e__Struct
    AWUN: UInt16
    AWUPF: UInt16
    NVSCC: _NVSCC_e__Struct
    NWPC: _NWPC_e__Struct
    ACWU: UInt16
    Reserved4: Byte * 2
    SGLS: _SGLS_e__Struct
    MNAN: UInt32
    Reserved6: Byte * 224
    SUBNQN: Byte * 256
    Reserved7: Byte * 768
    Reserved8: Byte * 256
    PDS: win32more.Windows.Win32.Storage.Nvme.NVME_POWER_STATE_DESC * 32
    VS: Byte * 1024
    class _CMIC_e__Struct(EasyCastStructure):
        _bitfield: Byte
    class _OAES_e__Struct(EasyCastStructure):
        _bitfield: UInt32
    class _CTRATT_e__Struct(EasyCastStructure):
        _bitfield: UInt32
    class _RRLS_e__Struct(EasyCastStructure):
        _bitfield: UInt16
    class _OACS_e__Struct(EasyCastStructure):
        _bitfield: UInt16
    class _FRMW_e__Struct(EasyCastStructure):
        _bitfield: Byte
    class _LPA_e__Struct(EasyCastStructure):
        _bitfield: Byte
    class _AVSCC_e__Struct(EasyCastStructure):
        _bitfield: Byte
    class _APSTA_e__Struct(EasyCastStructure):
        _bitfield: Byte
    class _RPMBS_e__Struct(EasyCastStructure):
        _bitfield: UInt32
    class _HCTMA_e__Struct(EasyCastStructure):
        _bitfield: UInt16
    class _SANICAP_e__Struct(EasyCastStructure):
        _bitfield: UInt32
    class _ANACAP_e__Struct(EasyCastStructure):
        _bitfield: Byte
    class _SQES_e__Struct(EasyCastStructure):
        _bitfield: Byte
    class _CQES_e__Struct(EasyCastStructure):
        _bitfield: Byte
    class _ONCS_e__Struct(EasyCastStructure):
        _bitfield: UInt16
    class _FUSES_e__Struct(EasyCastStructure):
        _bitfield: UInt16
    class _FNA_e__Struct(EasyCastStructure):
        _bitfield: Byte
    class _VWC_e__Struct(EasyCastStructure):
        _bitfield: Byte
    class _NVSCC_e__Struct(EasyCastStructure):
        _bitfield: Byte
    class _NWPC_e__Struct(EasyCastStructure):
        _bitfield: Byte
    class _SGLS_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_IDENTIFY_IO_COMMAND_SET(EasyCastStructure):
    IOCommandSetVector: UInt64 * 512
class NVME_IDENTIFY_NAMESPACE_DATA(EasyCastStructure):
    NSZE: UInt64
    NCAP: UInt64
    NUSE: UInt64
    NSFEAT: _NSFEAT_e__Struct
    NLBAF: Byte
    FLBAS: _FLBAS_e__Struct
    MC: _MC_e__Struct
    DPC: _DPC_e__Struct
    DPS: _DPS_e__Struct
    NMIC: _NMIC_e__Struct
    RESCAP: win32more.Windows.Win32.Storage.Nvme.NVM_RESERVATION_CAPABILITIES
    FPI: _FPI_e__Struct
    DLFEAT: _DLFEAT_e__Struct
    NAWUN: UInt16
    NAWUPF: UInt16
    NACWU: UInt16
    NABSN: UInt16
    NABO: UInt16
    NABSPF: UInt16
    NOIOB: UInt16
    NVMCAP: Byte * 16
    NPWG: UInt16
    NPWA: UInt16
    NPDG: UInt16
    NPDA: UInt16
    NOWS: UInt16
    MSSRL: UInt16
    MCL: UInt32
    MSRC: Byte
    Reserved2: Byte * 11
    ANAGRPID: UInt32
    Reserved3: Byte * 3
    NSATTR: _NSATTR_e__Struct
    NVMSETID: UInt16
    ENDGID: UInt16
    NGUID: Byte * 16
    EUI64: Byte * 8
    LBAF: win32more.Windows.Win32.Storage.Nvme.NVME_LBA_FORMAT * 16
    Reserved4: Byte * 192
    VS: Byte * 3712
    class _NSFEAT_e__Struct(EasyCastStructure):
        _bitfield: Byte
    class _FLBAS_e__Struct(EasyCastStructure):
        _bitfield: Byte
    class _MC_e__Struct(EasyCastStructure):
        _bitfield: Byte
    class _DPC_e__Struct(EasyCastStructure):
        _bitfield: Byte
    class _DPS_e__Struct(EasyCastStructure):
        _bitfield: Byte
    class _NMIC_e__Struct(EasyCastStructure):
        _bitfield: Byte
    class _FPI_e__Struct(EasyCastStructure):
        _bitfield: Byte
    class _DLFEAT_e__Struct(EasyCastStructure):
        _bitfield: Byte
    class _NSATTR_e__Struct(EasyCastStructure):
        _bitfield: Byte
class NVME_IDENTIFY_NAMESPACE_DESCRIPTOR(EasyCastStructure):
    NIDT: Byte
    NIDL: Byte
    Reserved: Byte * 2
    NID: Byte * 1
class NVME_IDENTIFY_NVM_SPECIFIC_CONTROLLER_IO_COMMAND_SET(EasyCastStructure):
    VSL: Byte
    WZSL: Byte
    WUSL: Byte
    DMRL: Byte
    DMRSL: UInt32
    DMSL: UInt64
    Reserved: Byte * 4080
class NVME_IDENTIFY_SPECIFIC_NAMESPACE_IO_COMMAND_SET(EasyCastStructure):
    ZOC: _ZOC_e__Struct
    OZCS: _OZCS_e__Struct
    MAR: UInt32
    MOR: UInt32
    RRL: UInt32
    FRL: UInt32
    Reserved0: Byte * 2796
    LBAEF: win32more.Windows.Win32.Storage.Nvme.NVME_LBA_ZONE_FORMAT * 16
    Reserved1: Byte * 768
    VS: Byte * 256
    class _ZOC_e__Struct(EasyCastStructure):
        _bitfield: UInt16
    class _OZCS_e__Struct(EasyCastStructure):
        _bitfield: UInt16
class NVME_IDENTIFY_ZNS_SPECIFIC_CONTROLLER_IO_COMMAND_SET(EasyCastStructure):
    ZASL: Byte
    Reserved: Byte * 4095
class NVME_LBA_FORMAT(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        MS: UInt16
        LBADS: Byte
        _bitfield: Byte
class NVME_LBA_RANGE(EasyCastStructure):
    Attributes: win32more.Windows.Win32.Storage.Nvme.NVME_CONTEXT_ATTRIBUTES
    LogicalBlockCount: UInt32
    StartingLBA: UInt64
class NVME_LBA_RANGET_TYPE_ENTRY(EasyCastStructure):
    Type: Byte
    Attributes: _Attributes_e__Struct
    Reserved0: Byte * 14
    SLBA: UInt64
    NLB: UInt64
    GUID: Byte * 16
    Reserved1: Byte * 16
    class _Attributes_e__Struct(EasyCastStructure):
        _bitfield: Byte
NVME_LBA_RANGE_TYPES = Int32
NVME_LBA_RANGE_TYPE_RESERVED: NVME_LBA_RANGE_TYPES = 0
NVME_LBA_RANGE_TYPE_FILESYSTEM: NVME_LBA_RANGE_TYPES = 1
NVME_LBA_RANGE_TYPE_RAID: NVME_LBA_RANGE_TYPES = 2
NVME_LBA_RANGE_TYPE_CACHE: NVME_LBA_RANGE_TYPES = 3
NVME_LBA_RANGE_TYPE_PAGE_SWAP_FILE: NVME_LBA_RANGE_TYPES = 4
class NVME_LBA_ZONE_FORMAT(EasyCastStructure):
    ZoneSize: UInt64
    ZDES: Byte
    Reserved: Byte * 7
NVME_LOG_PAGES = Int32
NVME_LOG_PAGE_ERROR_INFO: NVME_LOG_PAGES = 1
NVME_LOG_PAGE_HEALTH_INFO: NVME_LOG_PAGES = 2
NVME_LOG_PAGE_FIRMWARE_SLOT_INFO: NVME_LOG_PAGES = 3
NVME_LOG_PAGE_CHANGED_NAMESPACE_LIST: NVME_LOG_PAGES = 4
NVME_LOG_PAGE_COMMAND_EFFECTS: NVME_LOG_PAGES = 5
NVME_LOG_PAGE_DEVICE_SELF_TEST: NVME_LOG_PAGES = 6
NVME_LOG_PAGE_TELEMETRY_HOST_INITIATED: NVME_LOG_PAGES = 7
NVME_LOG_PAGE_TELEMETRY_CTLR_INITIATED: NVME_LOG_PAGES = 8
NVME_LOG_PAGE_ENDURANCE_GROUP_INFORMATION: NVME_LOG_PAGES = 9
NVME_LOG_PAGE_PREDICTABLE_LATENCY_NVM_SET: NVME_LOG_PAGES = 10
NVME_LOG_PAGE_PREDICTABLE_LATENCY_EVENT_AGGREGATE: NVME_LOG_PAGES = 11
NVME_LOG_PAGE_ASYMMETRIC_NAMESPACE_ACCESS: NVME_LOG_PAGES = 12
NVME_LOG_PAGE_PERSISTENT_EVENT_LOG: NVME_LOG_PAGES = 13
NVME_LOG_PAGE_LBA_STATUS_INFORMATION: NVME_LOG_PAGES = 14
NVME_LOG_PAGE_ENDURANCE_GROUP_EVENT_AGGREGATE: NVME_LOG_PAGES = 15
NVME_LOG_PAGE_RESERVATION_NOTIFICATION: NVME_LOG_PAGES = 128
NVME_LOG_PAGE_SANITIZE_STATUS: NVME_LOG_PAGES = 129
NVME_LOG_PAGE_CHANGED_ZONE_LIST: NVME_LOG_PAGES = 191
NVME_NAMESPACE_METADATA_ELEMENT_TYPES = Int32
NVME_NAMESPACE_METADATA_OPERATING_SYSTEM_NAMESPACE_NAME: NVME_NAMESPACE_METADATA_ELEMENT_TYPES = 1
NVME_NAMESPACE_METADATA_PREBOOT_NAMESPACE_NAME: NVME_NAMESPACE_METADATA_ELEMENT_TYPES = 2
NVME_NAMESPACE_METADATA_OPERATING_SYSTEM_NAMESPACE_NAME_QUALIFIER_1: NVME_NAMESPACE_METADATA_ELEMENT_TYPES = 3
NVME_NAMESPACE_METADATA_OPERATING_SYSTEM_NAMESPACE_NAME_QUALIFIER_2: NVME_NAMESPACE_METADATA_ELEMENT_TYPES = 4
NVME_NO_DEALLOCATE_MODIFIES_MEDIA_AFTER_SANITIZE = Int32
NVME_MEDIA_ADDITIONALLY_MODIFIED_AFTER_SANITIZE_NOT_DEFINED: NVME_NO_DEALLOCATE_MODIFIES_MEDIA_AFTER_SANITIZE = 0
NVME_MEDIA_NOT_ADDITIONALLY_MODIFIED_AFTER_SANITIZE: NVME_NO_DEALLOCATE_MODIFIES_MEDIA_AFTER_SANITIZE = 1
NVME_MEDIA_ADDITIONALLY_MOFIDIED_AFTER_SANITIZE: NVME_NO_DEALLOCATE_MODIFIES_MEDIA_AFTER_SANITIZE = 2
NVME_NVM_COMMANDS = Int32
NVME_NVM_COMMAND_FLUSH: NVME_NVM_COMMANDS = 0
NVME_NVM_COMMAND_WRITE: NVME_NVM_COMMANDS = 1
NVME_NVM_COMMAND_READ: NVME_NVM_COMMANDS = 2
NVME_NVM_COMMAND_WRITE_UNCORRECTABLE: NVME_NVM_COMMANDS = 4
NVME_NVM_COMMAND_COMPARE: NVME_NVM_COMMANDS = 5
NVME_NVM_COMMAND_WRITE_ZEROES: NVME_NVM_COMMANDS = 8
NVME_NVM_COMMAND_DATASET_MANAGEMENT: NVME_NVM_COMMANDS = 9
NVME_NVM_COMMAND_VERIFY: NVME_NVM_COMMANDS = 12
NVME_NVM_COMMAND_RESERVATION_REGISTER: NVME_NVM_COMMANDS = 13
NVME_NVM_COMMAND_RESERVATION_REPORT: NVME_NVM_COMMANDS = 14
NVME_NVM_COMMAND_RESERVATION_ACQUIRE: NVME_NVM_COMMANDS = 17
NVME_NVM_COMMAND_RESERVATION_RELEASE: NVME_NVM_COMMANDS = 21
NVME_NVM_COMMAND_COPY: NVME_NVM_COMMANDS = 25
NVME_NVM_COMMAND_ZONE_MANAGEMENT_SEND: NVME_NVM_COMMANDS = 121
NVME_NVM_COMMAND_ZONE_MANAGEMENT_RECEIVE: NVME_NVM_COMMANDS = 122
NVME_NVM_COMMAND_ZONE_APPEND: NVME_NVM_COMMANDS = 125
NVME_NVM_QUEUE_PRIORITIES = Int32
NVME_NVM_QUEUE_PRIORITY_URGENT: NVME_NVM_QUEUE_PRIORITIES = 0
NVME_NVM_QUEUE_PRIORITY_HIGH: NVME_NVM_QUEUE_PRIORITIES = 1
NVME_NVM_QUEUE_PRIORITY_MEDIUM: NVME_NVM_QUEUE_PRIORITIES = 2
NVME_NVM_QUEUE_PRIORITY_LOW: NVME_NVM_QUEUE_PRIORITIES = 3
class NVME_NVM_SUBSYSTEM_RESET(EasyCastStructure):
    NSSRC: UInt32
class NVME_OCP_DEVICE_CAPABILITIES_LOG(EasyCastStructure):
    PciePorts: UInt16
    OobMgmtSupport: _OobMgmtSupport_e__Union
    WriteZeroesCommand: _WriteZeroesCommand_e__Union
    SanitizeCommand: _SanitizeCommand_e__Union
    DatasetMgmtCommand: _DatasetMgmtCommand_e__Union
    WriteUncorrectableCommand: _WriteUncorrectableCommand_e__Union
    FusedCommand: _FusedCommand_e__Union
    MinimumValidDSSDPowerState: UInt16
    Reserved0: Byte
    DssdDescriptors: win32more.Windows.Win32.Storage.Nvme.DSSD_POWER_STATE_DESCRIPTOR * 127
    Reserved1: Byte * 3934
    LogPageVersionNumber: UInt16
    LogPageGUID: Guid
    _pack_ = 1
    class _OobMgmtSupport_e__Union(EasyCastUnion):
        Anonymous: _Anonymous_e__Struct
        AsUshort: UInt16
        _pack_ = 1
        class _Anonymous_e__Struct(EasyCastStructure):
            _bitfield: UInt16
            _pack_ = 1
    class _WriteZeroesCommand_e__Union(EasyCastUnion):
        Anonymous: _Anonymous_e__Struct
        AsUshort: UInt16
        _pack_ = 1
        class _Anonymous_e__Struct(EasyCastStructure):
            _bitfield: UInt16
            _pack_ = 1
    class _SanitizeCommand_e__Union(EasyCastUnion):
        Anonymous: _Anonymous_e__Struct
        AsUshort: UInt16
        _pack_ = 1
        class _Anonymous_e__Struct(EasyCastStructure):
            _bitfield: UInt16
            _pack_ = 1
    class _DatasetMgmtCommand_e__Union(EasyCastUnion):
        Anonymous: _Anonymous_e__Struct
        AsUshort: UInt16
        _pack_ = 1
        class _Anonymous_e__Struct(EasyCastStructure):
            _bitfield: UInt16
            _pack_ = 1
    class _WriteUncorrectableCommand_e__Union(EasyCastUnion):
        Anonymous: _Anonymous_e__Struct
        AsUshort: UInt16
        _pack_ = 1
        class _Anonymous_e__Struct(EasyCastStructure):
            _bitfield: UInt16
            _pack_ = 1
    class _FusedCommand_e__Union(EasyCastUnion):
        Anonymous: _Anonymous_e__Struct
        AsUshort: UInt16
        _pack_ = 1
        class _Anonymous_e__Struct(EasyCastStructure):
            _bitfield: UInt16
            _pack_ = 1
class NVME_OCP_DEVICE_ERROR_RECOVERY_LOG_V2(EasyCastStructure):
    PanicResetWaitTime: UInt16
    PanicResetAction: win32more.Windows.Win32.Storage.Nvme.NVME_WCS_DEVICE_RESET_ACTION
    DeviceRecoveryAction1: Byte
    PanicId: UInt64
    DeviceCapabilitiesA: win32more.Windows.Win32.Storage.Nvme.NVME_WCS_DEVICE_CAPABILITIES
    VendorSpecificRecoveryCode: Byte
    Reserved0: Byte * 3
    VendorSpecificCommandCDW12: UInt32
    VendorSpecificCommandCDW13: UInt32
    VendorSpecificCommandTimeout: Byte
    DeviceRecoveryAction2: Byte
    DeviceRecoveryAction2Timeout: Byte
    Reserved1: Byte * 463
    LogPageVersionNumber: UInt16
    LogPageGUID: Guid
    _pack_ = 1
class NVME_OCP_DEVICE_FIRMWARE_ACTIVATION_HISTORY_LOG(EasyCastStructure):
    LID: Byte
    Reserved0: Byte * 3
    ValidNumberOfEntries: UInt32
    Entries: win32more.Windows.Win32.Storage.Nvme.FIRMWARE_ACTIVATION_HISTORY_ENTRY * 20
    Reserved1: Byte * 2790
    LogPageVersionNumber: UInt16
    LogPageGUID: Guid
    _pack_ = 1
class NVME_OCP_DEVICE_LATENCY_MONITOR_LOG(EasyCastStructure):
    FeatureStatus: win32more.Windows.Win32.Storage.Nvme.LATENCY_MONITOR_FEATURE_STATUS
    Reserved0: Byte
    ActiveBucketTimer: UInt16
    ActiveBucketTimerThreshold: UInt16
    ActiveThresholdA: Byte
    ActiveThresholdB: Byte
    ActiveThresholdC: Byte
    ActiveThresholdD: Byte
    ActiveLatencyConfig: win32more.Windows.Win32.Storage.Nvme.ACTIVE_LATENCY_CONFIGURATION
    ActiveLatencyMinimumWindow: Byte
    Reserved1: Byte * 19
    ActiveBucketCounter0: win32more.Windows.Win32.Storage.Nvme.BUCKET_COUNTER
    ActiveBucketCounter1: win32more.Windows.Win32.Storage.Nvme.BUCKET_COUNTER
    ActiveBucketCounter2: win32more.Windows.Win32.Storage.Nvme.BUCKET_COUNTER
    ActiveBucketCounter3: win32more.Windows.Win32.Storage.Nvme.BUCKET_COUNTER
    ActiveLatencyStamp: win32more.Windows.Win32.Storage.Nvme.LATENCY_STAMP
    ActiveMeasuredLatency: win32more.Windows.Win32.Storage.Nvme.MEASURED_LATENCY
    ActiveLatencyStampUnits: win32more.Windows.Win32.Storage.Nvme.LATENCY_STAMP_UNITS
    Reserved2: Byte * 22
    StaticBucketCounter0: win32more.Windows.Win32.Storage.Nvme.BUCKET_COUNTER
    StaticBucketCounter1: win32more.Windows.Win32.Storage.Nvme.BUCKET_COUNTER
    StaticBucketCounter2: win32more.Windows.Win32.Storage.Nvme.BUCKET_COUNTER
    StaticBucketCounter3: win32more.Windows.Win32.Storage.Nvme.BUCKET_COUNTER
    StaticLatencyStamp: win32more.Windows.Win32.Storage.Nvme.LATENCY_STAMP
    StaticMeasuredLatency: win32more.Windows.Win32.Storage.Nvme.MEASURED_LATENCY
    StaticLatencyStampUnits: win32more.Windows.Win32.Storage.Nvme.LATENCY_STAMP_UNITS
    Reserved3: Byte * 22
    DebugLogTriggerEnable: win32more.Windows.Win32.Storage.Nvme.DEBUG_BIT_FIELD
    DebugLogMeasuredLatency: UInt16
    DebugLogLatencyStamp: UInt64
    DebugLogPointer: UInt16
    DebugCounterTriggerSource: win32more.Windows.Win32.Storage.Nvme.DEBUG_BIT_FIELD
    DebugLogStampUnits: _DebugLogStampUnits_e__Union
    Reserved4: Byte * 29
    LogPageVersionNumber: UInt16
    LogPageGUID: Guid
    _pack_ = 1
    class _DebugLogStampUnits_e__Union(EasyCastUnion):
        Anonymous: _Anonymous_e__Struct
        AsUchar: Byte
        class _Anonymous_e__Struct(EasyCastStructure):
            _bitfield: Byte
class NVME_OCP_DEVICE_SMART_INFORMATION_LOG_V3(EasyCastStructure):
    MediaUnitsWritten: Byte * 16
    MediaUnitsRead: Byte * 16
    BadUserNANDBlockCount: _BadUserNANDBlockCount_e__Struct
    BadSystemNANDBlockCount: _BadSystemNANDBlockCount_e__Struct
    XORRecoveryCount: UInt64
    UnrecoverableReadErrorCount: UInt64
    SoftECCErrorCount: UInt64
    EndToEndCorrectionCounts: _EndToEndCorrectionCounts_e__Struct
    PercentageSystemDataUsed: Byte
    RefreshCount: Byte * 7
    UserDataEraseCounts: _UserDataEraseCounts_e__Struct
    ThermalThrottling: _ThermalThrottling_e__Struct
    DSSDSpecVersion: Byte * 6
    PCIeCorrectableErrorCount: UInt64
    IncompleteShutdownCount: UInt32
    Reserved1: UInt32
    PercentageFreeBlocks: Byte
    Reserved2: Byte * 7
    CapacitorHealth: UInt16
    NvmeErrata: Byte
    Reserved3: Byte * 5
    UnalignedIOCount: UInt64
    SecurityVersionNumber: UInt64
    NUSE: UInt64
    PLPStartCount: Byte * 16
    EnduranceEstimate: Byte * 16
    PCIeLinkRetrainingCount: UInt64
    PowerStateChangeCount: UInt64
    Reserved4: Byte * 286
    LogPageVersionNumber: UInt16
    LogPageGUID: Guid
    _pack_ = 1
    class _BadUserNANDBlockCount_e__Struct(EasyCastStructure):
        RawCount: Byte * 6
        Normalized: Byte * 2
    class _BadSystemNANDBlockCount_e__Struct(EasyCastStructure):
        RawCount: Byte * 6
        Normalized: Byte * 2
    class _EndToEndCorrectionCounts_e__Struct(EasyCastStructure):
        DetectedCounts: UInt32
        CorrectedCounts: UInt32
        _pack_ = 1
    class _UserDataEraseCounts_e__Struct(EasyCastStructure):
        MaximumCount: UInt32
        MinimumCount: UInt32
        _pack_ = 1
    class _ThermalThrottling_e__Struct(EasyCastStructure):
        EventCount: Byte
        Status: Byte
class NVME_OCP_DEVICE_TCG_CONFIGURATION_LOG(EasyCastStructure):
    State: _State_e__Union
    Reserved0: Byte * 3
    LSPActivationCount: Byte
    TPRevertCount: Byte
    LSPRevertCount: Byte
    LOCount: Byte
    SUMLOCount: Byte
    RPLOCount: Byte
    NPLOCount: Byte
    RLLOCount: Byte
    WLLOCount: Byte
    RULOCount: Byte
    WULOCount: Byte
    Reserved1: Byte
    SIDAuthTryCount: UInt32
    SIDAuthTryLimit: UInt32
    ResetCount: UInt32
    ResetLockCount: UInt32
    Reserved2: Byte * 462
    LogPageVersionNumber: UInt16
    LogPageGUID: Guid
    _pack_ = 1
    class _State_e__Union(EasyCastUnion):
        Anonymous: _Anonymous_e__Struct
        AsUchar: Byte
        class _Anonymous_e__Struct(EasyCastStructure):
            _bitfield: Byte
class NVME_OCP_DEVICE_TCG_HISTORY_LOG(EasyCastStructure):
    LID: Byte
    Reserved0: Byte * 3
    HistoryEntryCount: UInt32
    HistoryEntries: win32more.Windows.Win32.Storage.Nvme.TCG_HISTORY_ENTRY * 84
    Reserved1: Byte * 38
    LogPageVersionNumber: UInt16
    LogPageGUID: Guid
    _pack_ = 1
class NVME_OCP_DEVICE_UNSUPPORTED_REQUIREMENTS_LOG(EasyCastStructure):
    UnsupportedCount: UInt16
    Reserved0: Byte * 14
    UnsupportedReqList: win32more.Windows.Win32.Storage.Nvme.UNSUPPORTED_REQUIREMENT * 253
    Reserved1: Byte * 14
    LogPageVersionNumber: UInt16
    LogPageGUID: Guid
    _pack_ = 1
class NVME_PERSISTENT_EVENT_LOG_EVENT_HEADER(EasyCastStructure):
    EventType: Byte
    EventTypeRevision: Byte
    EventHeaderLength: Byte
    Reserved0: Byte
    ControllerIdentifier: UInt16
    EventTimestamp: UInt64
    Reserved1: Byte * 6
    VendorSpecificInformationLength: UInt16
    EventLength: UInt16
    _pack_ = 1
NVME_PERSISTENT_EVENT_LOG_EVENT_TYPES = Int32
NVME_PERSISTENT_EVENT_TYPE_RESERVED0: NVME_PERSISTENT_EVENT_LOG_EVENT_TYPES = 0
NVME_PERSISTENT_EVENT_TYPE_SMART_HEALTH_LOG_SNAPSHOT: NVME_PERSISTENT_EVENT_LOG_EVENT_TYPES = 1
NVME_PERSISTENT_EVENT_TYPE_FIRMWARE_COMMIT: NVME_PERSISTENT_EVENT_LOG_EVENT_TYPES = 2
NVME_PERSISTENT_EVENT_TYPE_TIMESTAMP_CHANGE: NVME_PERSISTENT_EVENT_LOG_EVENT_TYPES = 3
NVME_PERSISTENT_EVENT_TYPE_POWER_ON_OR_RESET: NVME_PERSISTENT_EVENT_LOG_EVENT_TYPES = 4
NVME_PERSISTENT_EVENT_TYPE_NVM_SUBSYSTEM_HARDWARE_ERROR: NVME_PERSISTENT_EVENT_LOG_EVENT_TYPES = 5
NVME_PERSISTENT_EVENT_TYPE_CHANGE_NAMESPACE: NVME_PERSISTENT_EVENT_LOG_EVENT_TYPES = 6
NVME_PERSISTENT_EVENT_TYPE_FORMAT_NVM_START: NVME_PERSISTENT_EVENT_LOG_EVENT_TYPES = 7
NVME_PERSISTENT_EVENT_TYPE_FORMAT_NVM_COMPLETION: NVME_PERSISTENT_EVENT_LOG_EVENT_TYPES = 8
NVME_PERSISTENT_EVENT_TYPE_SANITIZE_START: NVME_PERSISTENT_EVENT_LOG_EVENT_TYPES = 9
NVME_PERSISTENT_EVENT_TYPE_SANITIZE_COMPLETION: NVME_PERSISTENT_EVENT_LOG_EVENT_TYPES = 10
NVME_PERSISTENT_EVENT_TYPE_SET_FEATURE: NVME_PERSISTENT_EVENT_LOG_EVENT_TYPES = 11
NVME_PERSISTENT_EVENT_TYPE_TELEMETRY_LOG_CREATED: NVME_PERSISTENT_EVENT_LOG_EVENT_TYPES = 12
NVME_PERSISTENT_EVENT_TYPE_THERMAL_EXCURSION: NVME_PERSISTENT_EVENT_LOG_EVENT_TYPES = 13
NVME_PERSISTENT_EVENT_TYPE_RESERVED1_BEGIN: NVME_PERSISTENT_EVENT_LOG_EVENT_TYPES = 14
NVME_PERSISTENT_EVENT_TYPE_RESERVED1_END: NVME_PERSISTENT_EVENT_LOG_EVENT_TYPES = 221
NVME_PERSISTENT_EVENT_TYPE_VENDOR_SPECIFIC_EVENT: NVME_PERSISTENT_EVENT_LOG_EVENT_TYPES = 222
NVME_PERSISTENT_EVENT_TYPE_TCG_DEFINED: NVME_PERSISTENT_EVENT_LOG_EVENT_TYPES = 223
NVME_PERSISTENT_EVENT_TYPE_RESERVED2_BEGIN: NVME_PERSISTENT_EVENT_LOG_EVENT_TYPES = 224
NVME_PERSISTENT_EVENT_TYPE_RESERVED2_END: NVME_PERSISTENT_EVENT_LOG_EVENT_TYPES = 255
NVME_PERSISTENT_EVENT_TYPE_MAX: NVME_PERSISTENT_EVENT_LOG_EVENT_TYPES = 255
class NVME_PERSISTENT_EVENT_LOG_HEADER(EasyCastStructure):
    LogIdentifier: Byte
    Reserved0: Byte * 3
    TotalNumberOfEvents: UInt32
    TotalLogLength: UInt64
    LogRevision: Byte
    Reserved1: Byte
    LogHeaderLength: UInt16
    Timestamp: UInt64
    PowerOnHours: Byte * 16
    PowerCycleCount: UInt64
    PciVendorId: UInt16
    PciSubsystemVendorId: UInt16
    SerialNumber: Byte * 20
    ModelNumber: Byte * 40
    NVMSubsystemNVMeQualifiedName: Byte * 256
    Reserved: Byte * 108
    SupportedEventsBitmap: Byte * 32
    _pack_ = 1
class NVME_POWER_STATE_DESC(EasyCastStructure):
    MP: UInt16
    Reserved0: Byte
    _bitfield1: Byte
    ENLAT: UInt32
    EXLAT: UInt32
    _bitfield2: Byte
    _bitfield3: Byte
    _bitfield4: Byte
    _bitfield5: Byte
    IDLP: UInt16
    _bitfield6: Byte
    Reserved7: Byte
    ACTP: UInt16
    _bitfield7: Byte
    Reserved9: Byte * 9
NVME_PROTECTION_INFORMATION_TYPES = Int32
NVME_PROTECTION_INFORMATION_NOT_ENABLED: NVME_PROTECTION_INFORMATION_TYPES = 0
NVME_PROTECTION_INFORMATION_TYPE1: NVME_PROTECTION_INFORMATION_TYPES = 1
NVME_PROTECTION_INFORMATION_TYPE2: NVME_PROTECTION_INFORMATION_TYPES = 2
NVME_PROTECTION_INFORMATION_TYPE3: NVME_PROTECTION_INFORMATION_TYPES = 3
class NVME_PRP_ENTRY(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlonglong: UInt64
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt64
class NVME_REGISTERED_CONTROLLER_DATA(EasyCastStructure):
    CNTLID: UInt16
    RCSTS: _RCSTS_e__Struct
    Reserved: Byte * 5
    HOSTID: Byte * 8
    RKEY: UInt64
    class _RCSTS_e__Struct(EasyCastStructure):
        _bitfield: Byte
class NVME_REGISTERED_CONTROLLER_EXTENDED_DATA(EasyCastStructure):
    CNTLID: UInt16
    RCSTS: _RCSTS_e__Struct
    Reserved: Byte * 5
    RKEY: UInt64
    HOSTID: Byte * 16
    Reserved1: Byte * 32
    class _RCSTS_e__Struct(EasyCastStructure):
        _bitfield: Byte
class NVME_REPORT_ZONE_INFO(EasyCastStructure):
    ZoneCount: UInt64
    Reserved: UInt64 * 7
    ZoneDescriptor: win32more.Windows.Win32.Storage.Nvme.NVME_ZONE_DESCRIPTOR * 1
NVME_RESERVATION_ACQUIRE_ACTIONS = Int32
NVME_RESERVATION_ACQUIRE_ACTION_ACQUIRE: NVME_RESERVATION_ACQUIRE_ACTIONS = 0
NVME_RESERVATION_ACQUIRE_ACTION_PREEMPT: NVME_RESERVATION_ACQUIRE_ACTIONS = 1
NVME_RESERVATION_ACQUIRE_ACTION_PREEMPT_AND_ABORT: NVME_RESERVATION_ACQUIRE_ACTIONS = 2
class NVME_RESERVATION_ACQUIRE_DATA_STRUCTURE(EasyCastStructure):
    CRKEY: UInt64
    PRKEY: UInt64
class NVME_RESERVATION_NOTIFICATION_LOG(EasyCastStructure):
    LogPageCount: UInt64
    LogPageType: Byte
    AvailableLogPageCount: Byte
    Reserved0: Byte * 2
    NameSpaceId: UInt32
    Reserved1: Byte * 48
NVME_RESERVATION_NOTIFICATION_TYPES = Int32
NVME_RESERVATION_NOTIFICATION_TYPE_EMPTY_LOG_PAGE: NVME_RESERVATION_NOTIFICATION_TYPES = 0
NVME_RESERVATION_NOTIFICATION_TYPE_REGISTRATION_PREEMPTED: NVME_RESERVATION_NOTIFICATION_TYPES = 1
NVME_RESERVATION_NOTIFICATION_TYPE_REGISTRATION_RELEASED: NVME_RESERVATION_NOTIFICATION_TYPES = 2
NVME_RESERVATION_NOTIFICATION_TYPE_RESERVATION_PREEPMPTED: NVME_RESERVATION_NOTIFICATION_TYPES = 3
NVME_RESERVATION_REGISTER_ACTIONS = Int32
NVME_RESERVATION_REGISTER_ACTION_REGISTER: NVME_RESERVATION_REGISTER_ACTIONS = 0
NVME_RESERVATION_REGISTER_ACTION_UNREGISTER: NVME_RESERVATION_REGISTER_ACTIONS = 1
NVME_RESERVATION_REGISTER_ACTION_REPLACE: NVME_RESERVATION_REGISTER_ACTIONS = 2
class NVME_RESERVATION_REGISTER_DATA_STRUCTURE(EasyCastStructure):
    CRKEY: UInt64
    NRKEY: UInt64
NVME_RESERVATION_REGISTER_PTPL_STATE_CHANGES = Int32
NVME_RESERVATION_REGISTER_PTPL_STATE_NO_CHANGE: NVME_RESERVATION_REGISTER_PTPL_STATE_CHANGES = 0
NVME_RESERVATION_REGISTER_PTPL_STATE_RESERVED: NVME_RESERVATION_REGISTER_PTPL_STATE_CHANGES = 1
NVME_RESERVATION_REGISTER_PTPL_STATE_SET_TO_0: NVME_RESERVATION_REGISTER_PTPL_STATE_CHANGES = 2
NVME_RESERVATION_REGISTER_PTPL_STATE_SET_TO_1: NVME_RESERVATION_REGISTER_PTPL_STATE_CHANGES = 3
NVME_RESERVATION_RELEASE_ACTIONS = Int32
NVME_RESERVATION_RELEASE_ACTION_RELEASE: NVME_RESERVATION_RELEASE_ACTIONS = 0
NVME_RESERVATION_RELEASE_ACTION_CLEAR: NVME_RESERVATION_RELEASE_ACTIONS = 1
class NVME_RESERVATION_RELEASE_DATA_STRUCTURE(EasyCastStructure):
    CRKEY: UInt64
class NVME_RESERVATION_REPORT_STATUS_DATA_STRUCTURE(EasyCastStructure):
    Header: win32more.Windows.Win32.Storage.Nvme.NVME_RESERVATION_REPORT_STATUS_HEADER
    RegisteredControllersData: win32more.Windows.Win32.Storage.Nvme.NVME_REGISTERED_CONTROLLER_DATA * 1
class NVME_RESERVATION_REPORT_STATUS_EXTENDED_DATA_STRUCTURE(EasyCastStructure):
    Header: win32more.Windows.Win32.Storage.Nvme.NVME_RESERVATION_REPORT_STATUS_HEADER
    Reserved1: Byte * 40
    RegisteredControllersExtendedData: win32more.Windows.Win32.Storage.Nvme.NVME_REGISTERED_CONTROLLER_EXTENDED_DATA * 1
class NVME_RESERVATION_REPORT_STATUS_HEADER(EasyCastStructure):
    GEN: UInt32
    RTYPE: Byte
    REGCTL: UInt16
    Reserved: Byte * 2
    PTPLS: Byte
    Reserved1: Byte * 14
    _pack_ = 1
NVME_RESERVATION_TYPES = Int32
NVME_RESERVATION_TYPE_RESERVED: NVME_RESERVATION_TYPES = 0
NVME_RESERVATION_TYPE_WRITE_EXCLUSIVE: NVME_RESERVATION_TYPES = 1
NVME_RESERVATION_TYPE_EXCLUSIVE_ACCESS: NVME_RESERVATION_TYPES = 2
NVME_RESERVATION_TYPE_WRITE_EXCLUSIVE_REGISTRANTS_ONLY: NVME_RESERVATION_TYPES = 3
NVME_RESERVATION_TYPE_EXCLUSIVE_ACCESS_REGISTRANTS_ONLY: NVME_RESERVATION_TYPES = 4
NVME_RESERVATION_TYPE_WRITE_EXCLUSIVE_ALL_REGISTRANTS: NVME_RESERVATION_TYPES = 5
NVME_RESERVATION_TYPE_EXCLUSIVE_ACCESS_ALL_REGISTRANTS: NVME_RESERVATION_TYPES = 6
NVME_SANITIZE_ACTION = Int32
NVME_SANITIZE_ACTION_RESERVED: NVME_SANITIZE_ACTION = 0
NVME_SANITIZE_ACTION_EXIT_FAILURE_MODE: NVME_SANITIZE_ACTION = 1
NVME_SANITIZE_ACTION_START_BLOCK_ERASE_SANITIZE: NVME_SANITIZE_ACTION = 2
NVME_SANITIZE_ACTION_START_OVERWRITE_SANITIZE: NVME_SANITIZE_ACTION = 3
NVME_SANITIZE_ACTION_START_CRYPTO_ERASE_SANITIZE: NVME_SANITIZE_ACTION = 4
NVME_SANITIZE_OPERATION_STATUS = Int32
NVME_SANITIZE_OPERATION_NONE: NVME_SANITIZE_OPERATION_STATUS = 0
NVME_SANITIZE_OPERATION_SUCCEEDED: NVME_SANITIZE_OPERATION_STATUS = 1
NVME_SANITIZE_OPERATION_IN_PROGRESS: NVME_SANITIZE_OPERATION_STATUS = 2
NVME_SANITIZE_OPERATION_FAILED: NVME_SANITIZE_OPERATION_STATUS = 3
NVME_SANITIZE_OPERATION_SUCCEEDED_WITH_FORCED_DEALLOCATION: NVME_SANITIZE_OPERATION_STATUS = 4
class NVME_SANITIZE_STATUS(EasyCastStructure):
    _bitfield: UInt16
class NVME_SANITIZE_STATUS_LOG(EasyCastStructure):
    SPROG: UInt16
    SSTAT: win32more.Windows.Win32.Storage.Nvme.NVME_SANITIZE_STATUS
    SCDW10: UInt32
    EstimatedTimeForOverwrite: UInt32
    EstimatedTimeForBlockErase: UInt32
    EstimatedTimeForCryptoErase: UInt32
    EstimatedTimeForOverwriteWithNoDeallocateMediaModification: UInt32
    EstimatedTimeForBlockEraseWithNoDeallocateMediaModification: UInt32
    EstimatedTimeForCryptoEraseWithNoDeallocateMediaModification: UInt32
    Reserved: Byte * 480
class NVME_SCSI_NAME_STRING(EasyCastStructure):
    PCIVendorID: win32more.Windows.Win32.Foundation.CHAR * 4
    ModelNumber: win32more.Windows.Win32.Foundation.CHAR * 40
    NamespaceID: win32more.Windows.Win32.Foundation.CHAR * 4
    SerialNumber: win32more.Windows.Win32.Foundation.CHAR * 20
NVME_SECURE_ERASE_SETTINGS = Int32
NVME_SECURE_ERASE_NONE: NVME_SECURE_ERASE_SETTINGS = 0
NVME_SECURE_ERASE_USER_DATA: NVME_SECURE_ERASE_SETTINGS = 1
NVME_SECURE_ERASE_CRYPTOGRAPHIC: NVME_SECURE_ERASE_SETTINGS = 2
class NVME_SET_ATTRIBUTES_ENTRY(EasyCastStructure):
    Identifier: UInt16
    ENDGID: UInt16
    Reserved1: UInt32
    Random4KBReadTypical: UInt32
    OptimalWriteSize: UInt32
    TotalCapacity: Byte * 16
    UnallocatedCapacity: Byte * 16
    Reserved2: Byte * 80
NVME_STATUS_COMMAND_SPECIFIC_CODES = Int32
NVME_STATUS_COMPLETION_QUEUE_INVALID: NVME_STATUS_COMMAND_SPECIFIC_CODES = 0
NVME_STATUS_INVALID_QUEUE_IDENTIFIER: NVME_STATUS_COMMAND_SPECIFIC_CODES = 1
NVME_STATUS_MAX_QUEUE_SIZE_EXCEEDED: NVME_STATUS_COMMAND_SPECIFIC_CODES = 2
NVME_STATUS_ABORT_COMMAND_LIMIT_EXCEEDED: NVME_STATUS_COMMAND_SPECIFIC_CODES = 3
NVME_STATUS_ASYNC_EVENT_REQUEST_LIMIT_EXCEEDED: NVME_STATUS_COMMAND_SPECIFIC_CODES = 5
NVME_STATUS_INVALID_FIRMWARE_SLOT: NVME_STATUS_COMMAND_SPECIFIC_CODES = 6
NVME_STATUS_INVALID_FIRMWARE_IMAGE: NVME_STATUS_COMMAND_SPECIFIC_CODES = 7
NVME_STATUS_INVALID_INTERRUPT_VECTOR: NVME_STATUS_COMMAND_SPECIFIC_CODES = 8
NVME_STATUS_INVALID_LOG_PAGE: NVME_STATUS_COMMAND_SPECIFIC_CODES = 9
NVME_STATUS_INVALID_FORMAT: NVME_STATUS_COMMAND_SPECIFIC_CODES = 10
NVME_STATUS_FIRMWARE_ACTIVATION_REQUIRES_CONVENTIONAL_RESET: NVME_STATUS_COMMAND_SPECIFIC_CODES = 11
NVME_STATUS_INVALID_QUEUE_DELETION: NVME_STATUS_COMMAND_SPECIFIC_CODES = 12
NVME_STATUS_FEATURE_ID_NOT_SAVEABLE: NVME_STATUS_COMMAND_SPECIFIC_CODES = 13
NVME_STATUS_FEATURE_NOT_CHANGEABLE: NVME_STATUS_COMMAND_SPECIFIC_CODES = 14
NVME_STATUS_FEATURE_NOT_NAMESPACE_SPECIFIC: NVME_STATUS_COMMAND_SPECIFIC_CODES = 15
NVME_STATUS_FIRMWARE_ACTIVATION_REQUIRES_NVM_SUBSYSTEM_RESET: NVME_STATUS_COMMAND_SPECIFIC_CODES = 16
NVME_STATUS_FIRMWARE_ACTIVATION_REQUIRES_RESET: NVME_STATUS_COMMAND_SPECIFIC_CODES = 17
NVME_STATUS_FIRMWARE_ACTIVATION_REQUIRES_MAX_TIME_VIOLATION: NVME_STATUS_COMMAND_SPECIFIC_CODES = 18
NVME_STATUS_FIRMWARE_ACTIVATION_PROHIBITED: NVME_STATUS_COMMAND_SPECIFIC_CODES = 19
NVME_STATUS_OVERLAPPING_RANGE: NVME_STATUS_COMMAND_SPECIFIC_CODES = 20
NVME_STATUS_NAMESPACE_INSUFFICIENT_CAPACITY: NVME_STATUS_COMMAND_SPECIFIC_CODES = 21
NVME_STATUS_NAMESPACE_IDENTIFIER_UNAVAILABLE: NVME_STATUS_COMMAND_SPECIFIC_CODES = 22
NVME_STATUS_NAMESPACE_ALREADY_ATTACHED: NVME_STATUS_COMMAND_SPECIFIC_CODES = 24
NVME_STATUS_NAMESPACE_IS_PRIVATE: NVME_STATUS_COMMAND_SPECIFIC_CODES = 25
NVME_STATUS_NAMESPACE_NOT_ATTACHED: NVME_STATUS_COMMAND_SPECIFIC_CODES = 26
NVME_STATUS_NAMESPACE_THIN_PROVISIONING_NOT_SUPPORTED: NVME_STATUS_COMMAND_SPECIFIC_CODES = 27
NVME_STATUS_CONTROLLER_LIST_INVALID: NVME_STATUS_COMMAND_SPECIFIC_CODES = 28
NVME_STATUS_DEVICE_SELF_TEST_IN_PROGRESS: NVME_STATUS_COMMAND_SPECIFIC_CODES = 29
NVME_STATUS_BOOT_PARTITION_WRITE_PROHIBITED: NVME_STATUS_COMMAND_SPECIFIC_CODES = 30
NVME_STATUS_INVALID_CONTROLLER_IDENTIFIER: NVME_STATUS_COMMAND_SPECIFIC_CODES = 31
NVME_STATUS_INVALID_SECONDARY_CONTROLLER_STATE: NVME_STATUS_COMMAND_SPECIFIC_CODES = 32
NVME_STATUS_INVALID_NUMBER_OF_CONTROLLER_RESOURCES: NVME_STATUS_COMMAND_SPECIFIC_CODES = 33
NVME_STATUS_INVALID_RESOURCE_IDENTIFIER: NVME_STATUS_COMMAND_SPECIFIC_CODES = 34
NVME_STATUS_SANITIZE_PROHIBITED_ON_PERSISTENT_MEMORY: NVME_STATUS_COMMAND_SPECIFIC_CODES = 35
NVME_STATUS_INVALID_ANA_GROUP_IDENTIFIER: NVME_STATUS_COMMAND_SPECIFIC_CODES = 36
NVME_STATUS_ANA_ATTACH_FAILED: NVME_STATUS_COMMAND_SPECIFIC_CODES = 37
NVME_IO_COMMAND_SET_NOT_SUPPORTED: NVME_STATUS_COMMAND_SPECIFIC_CODES = 41
NVME_IO_COMMAND_SET_NOT_ENABLED: NVME_STATUS_COMMAND_SPECIFIC_CODES = 42
NVME_IO_COMMAND_SET_COMBINATION_REJECTED: NVME_STATUS_COMMAND_SPECIFIC_CODES = 43
NVME_IO_COMMAND_SET_INVALID: NVME_STATUS_COMMAND_SPECIFIC_CODES = 44
NVME_STATUS_STREAM_RESOURCE_ALLOCATION_FAILED: NVME_STATUS_COMMAND_SPECIFIC_CODES = 127
NVME_STATUS_ZONE_INVALID_FORMAT: NVME_STATUS_COMMAND_SPECIFIC_CODES = 127
NVME_STATUS_NVM_CONFLICTING_ATTRIBUTES: NVME_STATUS_COMMAND_SPECIFIC_CODES = 128
NVME_STATUS_NVM_INVALID_PROTECTION_INFORMATION: NVME_STATUS_COMMAND_SPECIFIC_CODES = 129
NVME_STATUS_NVM_ATTEMPTED_WRITE_TO_READ_ONLY_RANGE: NVME_STATUS_COMMAND_SPECIFIC_CODES = 130
NVME_STATUS_NVM_COMMAND_SIZE_LIMIT_EXCEEDED: NVME_STATUS_COMMAND_SPECIFIC_CODES = 131
NVME_STATUS_ZONE_BOUNDARY_ERROR: NVME_STATUS_COMMAND_SPECIFIC_CODES = 184
NVME_STATUS_ZONE_FULL: NVME_STATUS_COMMAND_SPECIFIC_CODES = 185
NVME_STATUS_ZONE_READ_ONLY: NVME_STATUS_COMMAND_SPECIFIC_CODES = 186
NVME_STATUS_ZONE_OFFLINE: NVME_STATUS_COMMAND_SPECIFIC_CODES = 187
NVME_STATUS_ZONE_INVALID_WRITE: NVME_STATUS_COMMAND_SPECIFIC_CODES = 188
NVME_STATUS_ZONE_TOO_MANY_ACTIVE: NVME_STATUS_COMMAND_SPECIFIC_CODES = 189
NVME_STATUS_ZONE_TOO_MANY_OPEN: NVME_STATUS_COMMAND_SPECIFIC_CODES = 190
NVME_STATUS_ZONE_INVALID_STATE_TRANSITION: NVME_STATUS_COMMAND_SPECIFIC_CODES = 191
NVME_STATUS_GENERIC_COMMAND_CODES = Int32
NVME_STATUS_SUCCESS_COMPLETION: NVME_STATUS_GENERIC_COMMAND_CODES = 0
NVME_STATUS_INVALID_COMMAND_OPCODE: NVME_STATUS_GENERIC_COMMAND_CODES = 1
NVME_STATUS_INVALID_FIELD_IN_COMMAND: NVME_STATUS_GENERIC_COMMAND_CODES = 2
NVME_STATUS_COMMAND_ID_CONFLICT: NVME_STATUS_GENERIC_COMMAND_CODES = 3
NVME_STATUS_DATA_TRANSFER_ERROR: NVME_STATUS_GENERIC_COMMAND_CODES = 4
NVME_STATUS_COMMAND_ABORTED_DUE_TO_POWER_LOSS_NOTIFICATION: NVME_STATUS_GENERIC_COMMAND_CODES = 5
NVME_STATUS_INTERNAL_DEVICE_ERROR: NVME_STATUS_GENERIC_COMMAND_CODES = 6
NVME_STATUS_COMMAND_ABORT_REQUESTED: NVME_STATUS_GENERIC_COMMAND_CODES = 7
NVME_STATUS_COMMAND_ABORTED_DUE_TO_SQ_DELETION: NVME_STATUS_GENERIC_COMMAND_CODES = 8
NVME_STATUS_COMMAND_ABORTED_DUE_TO_FAILED_FUSED_COMMAND: NVME_STATUS_GENERIC_COMMAND_CODES = 9
NVME_STATUS_COMMAND_ABORTED_DUE_TO_FAILED_MISSING_COMMAND: NVME_STATUS_GENERIC_COMMAND_CODES = 10
NVME_STATUS_INVALID_NAMESPACE_OR_FORMAT: NVME_STATUS_GENERIC_COMMAND_CODES = 11
NVME_STATUS_COMMAND_SEQUENCE_ERROR: NVME_STATUS_GENERIC_COMMAND_CODES = 12
NVME_STATUS_INVALID_SGL_LAST_SEGMENT_DESCR: NVME_STATUS_GENERIC_COMMAND_CODES = 13
NVME_STATUS_INVALID_NUMBER_OF_SGL_DESCR: NVME_STATUS_GENERIC_COMMAND_CODES = 14
NVME_STATUS_DATA_SGL_LENGTH_INVALID: NVME_STATUS_GENERIC_COMMAND_CODES = 15
NVME_STATUS_METADATA_SGL_LENGTH_INVALID: NVME_STATUS_GENERIC_COMMAND_CODES = 16
NVME_STATUS_SGL_DESCR_TYPE_INVALID: NVME_STATUS_GENERIC_COMMAND_CODES = 17
NVME_STATUS_INVALID_USE_OF_CONTROLLER_MEMORY_BUFFER: NVME_STATUS_GENERIC_COMMAND_CODES = 18
NVME_STATUS_PRP_OFFSET_INVALID: NVME_STATUS_GENERIC_COMMAND_CODES = 19
NVME_STATUS_ATOMIC_WRITE_UNIT_EXCEEDED: NVME_STATUS_GENERIC_COMMAND_CODES = 20
NVME_STATUS_OPERATION_DENIED: NVME_STATUS_GENERIC_COMMAND_CODES = 21
NVME_STATUS_SGL_OFFSET_INVALID: NVME_STATUS_GENERIC_COMMAND_CODES = 22
NVME_STATUS_RESERVED: NVME_STATUS_GENERIC_COMMAND_CODES = 23
NVME_STATUS_HOST_IDENTIFIER_INCONSISTENT_FORMAT: NVME_STATUS_GENERIC_COMMAND_CODES = 24
NVME_STATUS_KEEP_ALIVE_TIMEOUT_EXPIRED: NVME_STATUS_GENERIC_COMMAND_CODES = 25
NVME_STATUS_KEEP_ALIVE_TIMEOUT_INVALID: NVME_STATUS_GENERIC_COMMAND_CODES = 26
NVME_STATUS_COMMAND_ABORTED_DUE_TO_PREEMPT_ABORT: NVME_STATUS_GENERIC_COMMAND_CODES = 27
NVME_STATUS_SANITIZE_FAILED: NVME_STATUS_GENERIC_COMMAND_CODES = 28
NVME_STATUS_SANITIZE_IN_PROGRESS: NVME_STATUS_GENERIC_COMMAND_CODES = 29
NVME_STATUS_SGL_DATA_BLOCK_GRANULARITY_INVALID: NVME_STATUS_GENERIC_COMMAND_CODES = 30
NVME_STATUS_DIRECTIVE_TYPE_INVALID: NVME_STATUS_GENERIC_COMMAND_CODES = 112
NVME_STATUS_DIRECTIVE_ID_INVALID: NVME_STATUS_GENERIC_COMMAND_CODES = 113
NVME_STATUS_NVM_LBA_OUT_OF_RANGE: NVME_STATUS_GENERIC_COMMAND_CODES = 128
NVME_STATUS_NVM_CAPACITY_EXCEEDED: NVME_STATUS_GENERIC_COMMAND_CODES = 129
NVME_STATUS_NVM_NAMESPACE_NOT_READY: NVME_STATUS_GENERIC_COMMAND_CODES = 130
NVME_STATUS_NVM_RESERVATION_CONFLICT: NVME_STATUS_GENERIC_COMMAND_CODES = 131
NVME_STATUS_FORMAT_IN_PROGRESS: NVME_STATUS_GENERIC_COMMAND_CODES = 132
NVME_STATUS_MEDIA_ERROR_CODES = Int32
NVME_STATUS_NVM_WRITE_FAULT: NVME_STATUS_MEDIA_ERROR_CODES = 128
NVME_STATUS_NVM_UNRECOVERED_READ_ERROR: NVME_STATUS_MEDIA_ERROR_CODES = 129
NVME_STATUS_NVM_END_TO_END_GUARD_CHECK_ERROR: NVME_STATUS_MEDIA_ERROR_CODES = 130
NVME_STATUS_NVM_END_TO_END_APPLICATION_TAG_CHECK_ERROR: NVME_STATUS_MEDIA_ERROR_CODES = 131
NVME_STATUS_NVM_END_TO_END_REFERENCE_TAG_CHECK_ERROR: NVME_STATUS_MEDIA_ERROR_CODES = 132
NVME_STATUS_NVM_COMPARE_FAILURE: NVME_STATUS_MEDIA_ERROR_CODES = 133
NVME_STATUS_NVM_ACCESS_DENIED: NVME_STATUS_MEDIA_ERROR_CODES = 134
NVME_STATUS_NVM_DEALLOCATED_OR_UNWRITTEN_LOGICAL_BLOCK: NVME_STATUS_MEDIA_ERROR_CODES = 135
NVME_STATUS_TYPES = Int32
NVME_STATUS_TYPE_GENERIC_COMMAND: NVME_STATUS_TYPES = 0
NVME_STATUS_TYPE_COMMAND_SPECIFIC: NVME_STATUS_TYPES = 1
NVME_STATUS_TYPE_MEDIA_ERROR: NVME_STATUS_TYPES = 2
NVME_STATUS_TYPE_VENDOR_SPECIFIC: NVME_STATUS_TYPES = 7
class NVME_SUBMISSION_QUEUE_TAIL_DOORBELL(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_TELEMETRY_CONTROLLER_INITIATED_LOG(EasyCastStructure):
    LogIdentifier: Byte
    Reserved0: Byte * 4
    OrganizationID: Byte * 3
    Area1LastBlock: UInt16
    Area2LastBlock: UInt16
    Area3LastBlock: UInt16
    Reserved1: Byte * 2
    Area4LastBlock: UInt32
    Reserved2: Byte * 362
    ControllerInitiatedDataAvailable: Byte
    ControllerInitiatedDataGenerationNumber: Byte
    ReasonIdentifier: Byte * 128
class NVME_TELEMETRY_HOST_INITIATED_LOG(EasyCastStructure):
    LogIdentifier: Byte
    Reserved0: Byte * 4
    OrganizationID: Byte * 3
    Area1LastBlock: UInt16
    Area2LastBlock: UInt16
    Area3LastBlock: UInt16
    Reserved1: Byte * 2
    Area4LastBlock: UInt32
    Reserved2: Byte * 361
    HostInitiatedDataGenerationNumber: Byte
    ControllerInitiatedDataAvailable: Byte
    ControllerInitiatedDataGenerationNumber: Byte
    ReasonIdentifier: Byte * 128
NVME_TEMPERATURE_THRESHOLD_TYPES = Int32
NVME_TEMPERATURE_OVER_THRESHOLD: NVME_TEMPERATURE_THRESHOLD_TYPES = 0
NVME_TEMPERATURE_UNDER_THRESHOLD: NVME_TEMPERATURE_THRESHOLD_TYPES = 1
NVME_VENDOR_LOG_PAGES = Int32
NVME_LOG_PAGE_OCP_DEVICE_SMART_INFORMATION: NVME_VENDOR_LOG_PAGES = 192
NVME_LOG_PAGE_OCP_DEVICE_ERROR_RECOVERY: NVME_VENDOR_LOG_PAGES = 193
NVME_LOG_PAGE_OCP_FIRMWARE_ACTIVATION_HISTORY: NVME_VENDOR_LOG_PAGES = 194
NVME_LOG_PAGE_OCP_LATENCY_MONITOR: NVME_VENDOR_LOG_PAGES = 195
NVME_LOG_PAGE_OCP_DEVICE_CAPABILITIES: NVME_VENDOR_LOG_PAGES = 196
NVME_LOG_PAGE_OCP_UNSUPPORTED_REQUIREMENTS: NVME_VENDOR_LOG_PAGES = 197
NVME_LOG_PAGE_OCP_TCG_CONFIGURATION: NVME_VENDOR_LOG_PAGES = 200
NVME_LOG_PAGE_OCP_TCG_HISTORY: NVME_VENDOR_LOG_PAGES = 201
class NVME_VERSION(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class NVME_WCS_DEVICE_CAPABILITIES(EasyCastStructure):
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Anonymous: _Anonymous_e__Struct
        AsULONG: UInt32
        class _Anonymous_e__Struct(EasyCastStructure):
            _bitfield: UInt32
class NVME_WCS_DEVICE_ERROR_RECOVERY_LOG(EasyCastStructure):
    PanicResetWaitTime: UInt16
    PanicResetAction: win32more.Windows.Win32.Storage.Nvme.NVME_WCS_DEVICE_RESET_ACTION
    DriveRecoveryAction: Byte
    PanicId: UInt64
    DeviceCapabilitiesA: win32more.Windows.Win32.Storage.Nvme.NVME_WCS_DEVICE_CAPABILITIES
    VendorSpecificRecoveryCode: Byte
    Reserved0: Byte * 3
    VendorSpecificCommandCDW12: UInt32
    VendorSpecificCommandCDW13: UInt32
    Reserved1: Byte * 466
    LogPageVersionNumber: UInt16
    LogPageGUID: Guid
    _pack_ = 1
NVME_WCS_DEVICE_RECOVERY_ACTION1 = Int32
NVME_WCS_DEVICE_RECOVERY_ACTION1_NVMeDeviceRecoveryNoAction: NVME_WCS_DEVICE_RECOVERY_ACTION1 = 0
NVME_WCS_DEVICE_RECOVERY_ACTION1_NVMeDeviceRecoveryFormatNVM: NVME_WCS_DEVICE_RECOVERY_ACTION1 = 1
NVME_WCS_DEVICE_RECOVERY_ACTION1_NVMeDeviceRecoveryVendorSpecificCommand: NVME_WCS_DEVICE_RECOVERY_ACTION1 = 2
NVME_WCS_DEVICE_RECOVERY_ACTION1_NVMeDeviceRecoveryVendorAnalysis: NVME_WCS_DEVICE_RECOVERY_ACTION1 = 3
NVME_WCS_DEVICE_RECOVERY_ACTION1_NVMeDeviceRecoveryDeviceReplacement: NVME_WCS_DEVICE_RECOVERY_ACTION1 = 4
NVME_WCS_DEVICE_RECOVERY_ACTION1_NVMeDeviceRecoverySanitize: NVME_WCS_DEVICE_RECOVERY_ACTION1 = 5
NVME_WCS_DEVICE_RECOVERY_ACTION1_NVMeDeviceRecovery1Max: NVME_WCS_DEVICE_RECOVERY_ACTION1 = 15
NVME_WCS_DEVICE_RECOVERY_ACTION2 = Int32
NVME_WCS_DEVICE_RECOVERY_ACTION2_NVMeDeviceRecoveryControllerReset: NVME_WCS_DEVICE_RECOVERY_ACTION2 = 0
NVME_WCS_DEVICE_RECOVERY_ACTION2_NVMeDeviceRecoverySubsystemReset: NVME_WCS_DEVICE_RECOVERY_ACTION2 = 1
NVME_WCS_DEVICE_RECOVERY_ACTION2_NVMeDeviceRecoveryPcieFunctionReset: NVME_WCS_DEVICE_RECOVERY_ACTION2 = 2
NVME_WCS_DEVICE_RECOVERY_ACTION2_NVMeDeviceRecoveryPERST: NVME_WCS_DEVICE_RECOVERY_ACTION2 = 3
NVME_WCS_DEVICE_RECOVERY_ACTION2_NVMeDeviceRecoveryPowerCycle: NVME_WCS_DEVICE_RECOVERY_ACTION2 = 4
NVME_WCS_DEVICE_RECOVERY_ACTION2_NVMeDeviceRecoveryPcieHotReset: NVME_WCS_DEVICE_RECOVERY_ACTION2 = 5
NVME_WCS_DEVICE_RECOVERY_ACTION2_NVMeDeviceRecovery2Max: NVME_WCS_DEVICE_RECOVERY_ACTION2 = 15
class NVME_WCS_DEVICE_RESET_ACTION(EasyCastStructure):
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Anonymous: _Anonymous_e__Struct
        AsUCHAR: Byte
        class _Anonymous_e__Struct(EasyCastStructure):
            _bitfield: Byte
class NVME_WCS_DEVICE_SMART_ATTRIBUTES_LOG(EasyCastStructure):
    VersionSpecificData: Byte * 494
    LogPageVersionNumber: UInt16
    LogPageGUID: Guid
    _pack_ = 1
class NVME_WCS_DEVICE_SMART_ATTRIBUTES_LOG_V2(EasyCastStructure):
    MediaUnitsWritten: Byte * 16
    MediaUnitsRead: Byte * 16
    BadUserNANDBlockCount: _BadUserNANDBlockCount_e__Struct
    BadSystemNANDBlockCount: _BadSystemNANDBlockCount_e__Struct
    XORRecoveryCount: UInt64
    UnrecoverableReadErrorCount: UInt64
    SoftECCErrorCount: UInt64
    EndToEndCorrectionCounts: _EndToEndCorrectionCounts_e__Struct
    PercentageSystemDataUsed: Byte
    RefreshCount: Byte * 7
    UserDataEraseCounts: _UserDataEraseCounts_e__Struct
    ThermalThrottling: _ThermalThrottling_e__Struct
    Reserved0: Byte * 6
    PCIeCorrectableErrorCount: UInt64
    IncompleteShutdownCount: UInt32
    Reserved1: UInt32
    PercentageFreeBlocks: Byte
    Reserved2: Byte * 7
    CapacitorHealth: UInt16
    Reserved3: Byte * 6
    UnalignedIOCount: UInt64
    SecurityVersionNumber: UInt64
    NUSE: UInt64
    PLPStartCount: Byte * 16
    EnduranceEstimate: Byte * 16
    Reserved4: Byte * 302
    LogPageVersionNumber: UInt16
    LogPageGUID: Guid
    _pack_ = 1
    class _BadUserNANDBlockCount_e__Struct(EasyCastStructure):
        RawCount: Byte * 6
        Normalized: Byte * 2
    class _BadSystemNANDBlockCount_e__Struct(EasyCastStructure):
        RawCount: Byte * 6
        Normalized: Byte * 2
    class _EndToEndCorrectionCounts_e__Struct(EasyCastStructure):
        DetectedCounts: UInt32
        CorrectedCounts: UInt32
        _pack_ = 1
    class _UserDataEraseCounts_e__Struct(EasyCastStructure):
        MaximumCount: UInt32
        MinimumCount: UInt32
        _pack_ = 1
    class _ThermalThrottling_e__Struct(EasyCastStructure):
        EventCount: Byte
        Status: Byte
class NVME_ZONE_DESCRIPTOR(EasyCastStructure):
    Anonymous1: _Anonymous1_e__Struct
    Anonymous2: _Anonymous2_e__Struct
    ZA: _ZA_e__Struct
    Reserved3: Byte * 5
    ZCAP: UInt64
    ZSLBA: UInt64
    WritePointer: UInt64
    Reserved4: Byte * 32
    class _Anonymous1_e__Struct(EasyCastStructure):
        _bitfield: Byte
    class _Anonymous2_e__Struct(EasyCastStructure):
        _bitfield: Byte
    class _ZA_e__Struct(EasyCastStructure):
        _bitfield: Byte
class NVME_ZONE_DESCRIPTOR_EXTENSION(EasyCastStructure):
    ZoneDescriptorExtensionInfo: Byte * 64
class NVME_ZONE_EXTENDED_REPORT_ZONE_DESC(EasyCastStructure):
    ZoneDescriptor: win32more.Windows.Win32.Storage.Nvme.NVME_ZONE_DESCRIPTOR
    ZoneDescriptorExtension: win32more.Windows.Win32.Storage.Nvme.NVME_ZONE_DESCRIPTOR_EXTENSION * 1
NVME_ZONE_RECEIVE_ACTION = Int32
NVME_ZONE_RECEIVE_REPORT_ZONES: NVME_ZONE_RECEIVE_ACTION = 0
NVME_ZONE_RECEIVE_EXTENDED_REPORT_ZONES: NVME_ZONE_RECEIVE_ACTION = 1
NVME_ZONE_RECEIVE_ACTION_SPECIFIC = Int32
NVME_ZRA_ALL_ZONES: NVME_ZONE_RECEIVE_ACTION_SPECIFIC = 0
NVME_ZRA_EMPTY_STATE_ZONES: NVME_ZONE_RECEIVE_ACTION_SPECIFIC = 1
NVME_ZRA_IO_STATE_ZONES: NVME_ZONE_RECEIVE_ACTION_SPECIFIC = 2
NVME_ZRA_EO_STATE_ZONES: NVME_ZONE_RECEIVE_ACTION_SPECIFIC = 3
NVME_ZRA_CLOSED_STATE_ZONES: NVME_ZONE_RECEIVE_ACTION_SPECIFIC = 4
NVME_ZRA_FULL_STATE_ZONES: NVME_ZONE_RECEIVE_ACTION_SPECIFIC = 5
NVME_ZRA_RO_STATE_ZONES: NVME_ZONE_RECEIVE_ACTION_SPECIFIC = 6
NVME_ZRA_OFFLINE_STATE_ZONES: NVME_ZONE_RECEIVE_ACTION_SPECIFIC = 7
NVME_ZONE_SEND_ACTION = Int32
NVME_ZONE_SEND_CLOSE: NVME_ZONE_SEND_ACTION = 1
NVME_ZONE_SEND_FINISH: NVME_ZONE_SEND_ACTION = 2
NVME_ZONE_SEND_OPEN: NVME_ZONE_SEND_ACTION = 3
NVME_ZONE_SEND_RESET: NVME_ZONE_SEND_ACTION = 4
NVME_ZONE_SEND_OFFLINE: NVME_ZONE_SEND_ACTION = 5
NVME_ZONE_SEND_SET_ZONE_DESCRIPTOR: NVME_ZONE_SEND_ACTION = 16
class NVM_RESERVATION_CAPABILITIES(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUchar: Byte
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: Byte
class NVM_SET_LIST(EasyCastStructure):
    IdentifierCount: Byte
    Reserved: Byte * 127
    Entry: win32more.Windows.Win32.Storage.Nvme.NVME_SET_ATTRIBUTES_ENTRY * 1
class TCG_ACTIVATE_METHOD_SPECIFIC(EasyCastStructure):
    RangeStartLengthPolicy: Byte
class TCG_ASSIGN_METHOD_SPECIFIC(EasyCastStructure):
    NamespaceId: UInt32
    _pack_ = 1
class TCG_AUTH_METHOD_SPECIFIC(EasyCastStructure):
    AuthorityId: UInt64
    TriesCount: Byte
    _pack_ = 1
class TCG_BLOCKSID_METHOD_SPECIFIC(EasyCastStructure):
    ClearEvents: Byte
class TCG_HISTORY_ENTRY(EasyCastStructure):
    VersionNumber: Byte
    EntryLength: Byte
    PowerCycleCount: UInt16
    TcgCommandCount: UInt32
    TcgCommandCompletionTS: UInt64
    InvokingId: UInt64
    MethodId: UInt64
    ComId: UInt16
    ProtocolId: Byte
    TcgStatus: Byte
    ProcessTime: UInt16
    CommandSpecific: Byte * 10
    _pack_ = 1
class TCG_REACTIVATE_METHOD_SPECIFIC(EasyCastStructure):
    RangeStartLengthPolicy: Byte
class UNSUPPORTED_REQUIREMENT(EasyCastStructure):
    ReqId: Byte * 16
ZONE_STATE = Int32
NVME_STATE_ZSE: ZONE_STATE = 1
NVME_STATE_ZSIO: ZONE_STATE = 2
NVME_STATE_ZSEO: ZONE_STATE = 3
NVME_STATE_ZSC: ZONE_STATE = 4
NVME_STATE_ZSRO: ZONE_STATE = 13
NVME_STATE_ZSF: ZONE_STATE = 14
NVME_STATE_ZSO: ZONE_STATE = 15
make_ready(__name__)
