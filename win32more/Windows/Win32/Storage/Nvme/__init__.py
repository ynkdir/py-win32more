from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Storage.Nvme
class ACTIVE_LATENCY_CONFIGURATION(Structure):
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        AsUshort: UInt16
        _pack_ = 1
        class _Anonymous_e__Struct(Structure):
            Read0: Annotated[UInt16, 1]
            Write0: Annotated[UInt16, 1]
            Trim0: Annotated[UInt16, 1]
            Read1: Annotated[UInt16, 1]
            Write1: Annotated[UInt16, 1]
            Trim1: Annotated[UInt16, 1]
            Read2: Annotated[UInt16, 1]
            Write2: Annotated[UInt16, 1]
            Trim2: Annotated[UInt16, 1]
            Read3: Annotated[UInt16, 1]
            Write3: Annotated[UInt16, 1]
            Trim3: Annotated[UInt16, 1]
            Reserved: Annotated[UInt16, 4]
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
class BUCKET_COUNTER(Structure):
    Reserved: UInt32
    Trim: UInt32
    Write: UInt32
    Read: UInt32
    _pack_ = 1
class DEBUG_BIT_FIELD(Structure):
    Read0: Annotated[UInt16, 1]
    Write0: Annotated[UInt16, 1]
    Trim0: Annotated[UInt16, 1]
    Read1: Annotated[UInt16, 1]
    Write1: Annotated[UInt16, 1]
    Trim1: Annotated[UInt16, 1]
    Read2: Annotated[UInt16, 1]
    Write2: Annotated[UInt16, 1]
    Trim2: Annotated[UInt16, 1]
    Read3: Annotated[UInt16, 1]
    Write3: Annotated[UInt16, 1]
    Trim3: Annotated[UInt16, 1]
    Reserved: Annotated[UInt16, 4]
    _pack_ = 1
class DSSD_POWER_STATE_DESCRIPTOR(Structure):
    NvmePowerState: Annotated[Byte, 5]
    Reserved: Annotated[Byte, 2]
    ValidDSSDPowerState: Annotated[Byte, 1]
class FIRMWARE_ACTIVATION_HISTORY_ENTRY(Structure):
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
class LATENCY_MONITOR_FEATURE_STATUS(Structure):
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        AsUchar: Byte
        class _Anonymous_e__Struct(Structure):
            FeatureEnabled: Annotated[Byte, 1]
            ActiveLatencyMode: Annotated[Byte, 1]
            ActiveMeasuredLatency: Annotated[Byte, 1]
            Reserved: Annotated[Byte, 5]
class LATENCY_STAMP(Structure):
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
class LATENCY_STAMP_UNITS(Structure):
    Read0: Annotated[UInt16, 1]
    Write0: Annotated[UInt16, 1]
    Trim0: Annotated[UInt16, 1]
    Read1: Annotated[UInt16, 1]
    Write1: Annotated[UInt16, 1]
    Trim1: Annotated[UInt16, 1]
    Read2: Annotated[UInt16, 1]
    Write2: Annotated[UInt16, 1]
    Trim2: Annotated[UInt16, 1]
    Read3: Annotated[UInt16, 1]
    Write3: Annotated[UInt16, 1]
    Trim3: Annotated[UInt16, 1]
    Reserved: Annotated[UInt16, 4]
    _pack_ = 1
class MEASURED_LATENCY(Structure):
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
NVME_ACCESS_FREQUENCY_NONE: win32more.Windows.Win32.Storage.Nvme.NVME_ACCESS_FREQUENCIES = 0
NVME_ACCESS_FREQUENCY_TYPICAL: win32more.Windows.Win32.Storage.Nvme.NVME_ACCESS_FREQUENCIES = 1
NVME_ACCESS_FREQUENCY_INFR_WRITE_INFR_READ: win32more.Windows.Win32.Storage.Nvme.NVME_ACCESS_FREQUENCIES = 2
NVME_ACCESS_FREQUENCY_INFR_WRITE_FR_READ: win32more.Windows.Win32.Storage.Nvme.NVME_ACCESS_FREQUENCIES = 3
NVME_ACCESS_FREQUENCY_FR_WRITE_INFR_READ: win32more.Windows.Win32.Storage.Nvme.NVME_ACCESS_FREQUENCIES = 4
NVME_ACCESS_FREQUENCY_FR_WRITE_FR_READ: win32more.Windows.Win32.Storage.Nvme.NVME_ACCESS_FREQUENCIES = 5
NVME_ACCESS_FREQUENCY_ONE_TIME_READ: win32more.Windows.Win32.Storage.Nvme.NVME_ACCESS_FREQUENCIES = 6
NVME_ACCESS_FREQUENCY_SPECULATIVE_READ: win32more.Windows.Win32.Storage.Nvme.NVME_ACCESS_FREQUENCIES = 7
NVME_ACCESS_FREQUENCY_WILL_BE_OVERWRITTEN: win32more.Windows.Win32.Storage.Nvme.NVME_ACCESS_FREQUENCIES = 8
NVME_ACCESS_LATENCIES = Int32
NVME_ACCESS_LATENCY_NONE: win32more.Windows.Win32.Storage.Nvme.NVME_ACCESS_LATENCIES = 0
NVME_ACCESS_LATENCY_IDLE: win32more.Windows.Win32.Storage.Nvme.NVME_ACCESS_LATENCIES = 1
NVME_ACCESS_LATENCY_NORMAL: win32more.Windows.Win32.Storage.Nvme.NVME_ACCESS_LATENCIES = 2
NVME_ACCESS_LATENCY_LOW: win32more.Windows.Win32.Storage.Nvme.NVME_ACCESS_LATENCIES = 3
class NVME_ACTIVE_NAMESPACE_ID_LIST(Structure):
    NSID: UInt32 * 1024
NVME_ADMIN_COMMANDS = Int32
NVME_ADMIN_COMMAND_DELETE_IO_SQ: win32more.Windows.Win32.Storage.Nvme.NVME_ADMIN_COMMANDS = 0
NVME_ADMIN_COMMAND_CREATE_IO_SQ: win32more.Windows.Win32.Storage.Nvme.NVME_ADMIN_COMMANDS = 1
NVME_ADMIN_COMMAND_GET_LOG_PAGE: win32more.Windows.Win32.Storage.Nvme.NVME_ADMIN_COMMANDS = 2
NVME_ADMIN_COMMAND_DELETE_IO_CQ: win32more.Windows.Win32.Storage.Nvme.NVME_ADMIN_COMMANDS = 4
NVME_ADMIN_COMMAND_CREATE_IO_CQ: win32more.Windows.Win32.Storage.Nvme.NVME_ADMIN_COMMANDS = 5
NVME_ADMIN_COMMAND_IDENTIFY: win32more.Windows.Win32.Storage.Nvme.NVME_ADMIN_COMMANDS = 6
NVME_ADMIN_COMMAND_ABORT: win32more.Windows.Win32.Storage.Nvme.NVME_ADMIN_COMMANDS = 8
NVME_ADMIN_COMMAND_SET_FEATURES: win32more.Windows.Win32.Storage.Nvme.NVME_ADMIN_COMMANDS = 9
NVME_ADMIN_COMMAND_GET_FEATURES: win32more.Windows.Win32.Storage.Nvme.NVME_ADMIN_COMMANDS = 10
NVME_ADMIN_COMMAND_ASYNC_EVENT_REQUEST: win32more.Windows.Win32.Storage.Nvme.NVME_ADMIN_COMMANDS = 12
NVME_ADMIN_COMMAND_NAMESPACE_MANAGEMENT: win32more.Windows.Win32.Storage.Nvme.NVME_ADMIN_COMMANDS = 13
NVME_ADMIN_COMMAND_FIRMWARE_ACTIVATE: win32more.Windows.Win32.Storage.Nvme.NVME_ADMIN_COMMANDS = 16
NVME_ADMIN_COMMAND_FIRMWARE_COMMIT: win32more.Windows.Win32.Storage.Nvme.NVME_ADMIN_COMMANDS = 16
NVME_ADMIN_COMMAND_FIRMWARE_IMAGE_DOWNLOAD: win32more.Windows.Win32.Storage.Nvme.NVME_ADMIN_COMMANDS = 17
NVME_ADMIN_COMMAND_DEVICE_SELF_TEST: win32more.Windows.Win32.Storage.Nvme.NVME_ADMIN_COMMANDS = 20
NVME_ADMIN_COMMAND_NAMESPACE_ATTACHMENT: win32more.Windows.Win32.Storage.Nvme.NVME_ADMIN_COMMANDS = 21
NVME_ADMIN_COMMAND_DIRECTIVE_SEND: win32more.Windows.Win32.Storage.Nvme.NVME_ADMIN_COMMANDS = 25
NVME_ADMIN_COMMAND_DIRECTIVE_RECEIVE: win32more.Windows.Win32.Storage.Nvme.NVME_ADMIN_COMMANDS = 26
NVME_ADMIN_COMMAND_VIRTUALIZATION_MANAGEMENT: win32more.Windows.Win32.Storage.Nvme.NVME_ADMIN_COMMANDS = 28
NVME_ADMIN_COMMAND_NVME_MI_SEND: win32more.Windows.Win32.Storage.Nvme.NVME_ADMIN_COMMANDS = 29
NVME_ADMIN_COMMAND_NVME_MI_RECEIVE: win32more.Windows.Win32.Storage.Nvme.NVME_ADMIN_COMMANDS = 30
NVME_ADMIN_COMMAND_DOORBELL_BUFFER_CONFIG: win32more.Windows.Win32.Storage.Nvme.NVME_ADMIN_COMMANDS = 124
NVME_ADMIN_COMMAND_FORMAT_NVM: win32more.Windows.Win32.Storage.Nvme.NVME_ADMIN_COMMANDS = 128
NVME_ADMIN_COMMAND_SECURITY_SEND: win32more.Windows.Win32.Storage.Nvme.NVME_ADMIN_COMMANDS = 129
NVME_ADMIN_COMMAND_SECURITY_RECEIVE: win32more.Windows.Win32.Storage.Nvme.NVME_ADMIN_COMMANDS = 130
NVME_ADMIN_COMMAND_SANITIZE: win32more.Windows.Win32.Storage.Nvme.NVME_ADMIN_COMMANDS = 132
NVME_ADMIN_COMMAND_GET_LBA_STATUS: win32more.Windows.Win32.Storage.Nvme.NVME_ADMIN_COMMANDS = 134
class NVME_ADMIN_COMPLETION_QUEUE_BASE_ADDRESS(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlonglong: UInt64
    class _Anonymous_e__Struct(Structure):
        Reserved0: Annotated[UInt64, 12]
        ACQB: Annotated[UInt64, 52]
class NVME_ADMIN_QUEUE_ATTRIBUTES(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        ASQS: Annotated[UInt32, 12]
        Reserved0: Annotated[UInt32, 4]
        ACQS: Annotated[UInt32, 12]
        Reserved1: Annotated[UInt32, 4]
class NVME_ADMIN_SUBMISSION_QUEUE_BASE_ADDRESS(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlonglong: UInt64
    class _Anonymous_e__Struct(Structure):
        Reserved0: Annotated[UInt64, 12]
        ASQB: Annotated[UInt64, 52]
NVME_AMS_OPTION = Int32
NVME_AMS_ROUND_ROBIN: win32more.Windows.Win32.Storage.Nvme.NVME_AMS_OPTION = 0
NVME_AMS_WEIGHTED_ROUND_ROBIN_URGENT: win32more.Windows.Win32.Storage.Nvme.NVME_AMS_OPTION = 1
NVME_ASYNC_EVENT_ERROR_STATUS_CODES = Int32
NVME_ASYNC_ERROR_INVALID_SUBMISSION_QUEUE: win32more.Windows.Win32.Storage.Nvme.NVME_ASYNC_EVENT_ERROR_STATUS_CODES = 0
NVME_ASYNC_ERROR_INVALID_DOORBELL_WRITE_VALUE: win32more.Windows.Win32.Storage.Nvme.NVME_ASYNC_EVENT_ERROR_STATUS_CODES = 1
NVME_ASYNC_ERROR_DIAG_FAILURE: win32more.Windows.Win32.Storage.Nvme.NVME_ASYNC_EVENT_ERROR_STATUS_CODES = 2
NVME_ASYNC_ERROR_PERSISTENT_INTERNAL_DEVICE_ERROR: win32more.Windows.Win32.Storage.Nvme.NVME_ASYNC_EVENT_ERROR_STATUS_CODES = 3
NVME_ASYNC_ERROR_TRANSIENT_INTERNAL_DEVICE_ERROR: win32more.Windows.Win32.Storage.Nvme.NVME_ASYNC_EVENT_ERROR_STATUS_CODES = 4
NVME_ASYNC_ERROR_FIRMWARE_IMAGE_LOAD_ERROR: win32more.Windows.Win32.Storage.Nvme.NVME_ASYNC_EVENT_ERROR_STATUS_CODES = 5
NVME_ASYNC_EVENT_HEALTH_STATUS_CODES = Int32
NVME_ASYNC_HEALTH_NVM_SUBSYSTEM_RELIABILITY: win32more.Windows.Win32.Storage.Nvme.NVME_ASYNC_EVENT_HEALTH_STATUS_CODES = 0
NVME_ASYNC_HEALTH_TEMPERATURE_THRESHOLD: win32more.Windows.Win32.Storage.Nvme.NVME_ASYNC_EVENT_HEALTH_STATUS_CODES = 1
NVME_ASYNC_HEALTH_SPARE_BELOW_THRESHOLD: win32more.Windows.Win32.Storage.Nvme.NVME_ASYNC_EVENT_HEALTH_STATUS_CODES = 2
NVME_ASYNC_EVENT_IO_COMMAND_SET_STATUS_CODES = Int32
NVME_ASYNC_IO_CMD_SET_RESERVATION_LOG_PAGE_AVAILABLE: win32more.Windows.Win32.Storage.Nvme.NVME_ASYNC_EVENT_IO_COMMAND_SET_STATUS_CODES = 0
NVME_ASYNC_IO_CMD_SANITIZE_OPERATION_COMPLETED: win32more.Windows.Win32.Storage.Nvme.NVME_ASYNC_EVENT_IO_COMMAND_SET_STATUS_CODES = 1
NVME_ASYNC_IO_CMD_SANITIZE_OPERATION_COMPLETED_WITH_UNEXPECTED_DEALLOCATION: win32more.Windows.Win32.Storage.Nvme.NVME_ASYNC_EVENT_IO_COMMAND_SET_STATUS_CODES = 2
NVME_ASYNC_EVENT_NOTICE_CODES = Int32
NVME_ASYNC_NOTICE_NAMESPACE_ATTRIBUTE_CHANGED: win32more.Windows.Win32.Storage.Nvme.NVME_ASYNC_EVENT_NOTICE_CODES = 0
NVME_ASYNC_NOTICE_FIRMWARE_ACTIVATION_STARTING: win32more.Windows.Win32.Storage.Nvme.NVME_ASYNC_EVENT_NOTICE_CODES = 1
NVME_ASYNC_NOTICE_TELEMETRY_LOG_CHANGED: win32more.Windows.Win32.Storage.Nvme.NVME_ASYNC_EVENT_NOTICE_CODES = 2
NVME_ASYNC_NOTICE_ASYMMETRIC_ACCESS_CHANGE: win32more.Windows.Win32.Storage.Nvme.NVME_ASYNC_EVENT_NOTICE_CODES = 3
NVME_ASYNC_NOTICE_PREDICTABLE_LATENCY_EVENT_AGGREGATE_LOG_CHANGE: win32more.Windows.Win32.Storage.Nvme.NVME_ASYNC_EVENT_NOTICE_CODES = 4
NVME_ASYNC_NOTICE_LBA_STATUS_INFORMATION_ALERT: win32more.Windows.Win32.Storage.Nvme.NVME_ASYNC_EVENT_NOTICE_CODES = 5
NVME_ASYNC_NOTICE_ENDURANCE_GROUP_EVENT_AGGREGATE_LOG_CHANGE: win32more.Windows.Win32.Storage.Nvme.NVME_ASYNC_EVENT_NOTICE_CODES = 6
NVME_ASYNC_NOTICE_ZONE_DESCRIPTOR_CHANGED: win32more.Windows.Win32.Storage.Nvme.NVME_ASYNC_EVENT_NOTICE_CODES = 239
NVME_ASYNC_EVENT_TYPES = Int32
NVME_ASYNC_EVENT_TYPE_ERROR_STATUS: win32more.Windows.Win32.Storage.Nvme.NVME_ASYNC_EVENT_TYPES = 0
NVME_ASYNC_EVENT_TYPE_HEALTH_STATUS: win32more.Windows.Win32.Storage.Nvme.NVME_ASYNC_EVENT_TYPES = 1
NVME_ASYNC_EVENT_TYPE_NOTICE: win32more.Windows.Win32.Storage.Nvme.NVME_ASYNC_EVENT_TYPES = 2
NVME_ASYNC_EVENT_TYPE_IO_COMMAND_SET_STATUS: win32more.Windows.Win32.Storage.Nvme.NVME_ASYNC_EVENT_TYPES = 6
NVME_ASYNC_EVENT_TYPE_VENDOR_SPECIFIC: win32more.Windows.Win32.Storage.Nvme.NVME_ASYNC_EVENT_TYPES = 7
NVME_ASYNC_EVENT_TYPE_VENDOR_SPECIFIC_CODES = Int32
NVME_ASYNC_EVENT_TYPE_VENDOR_SPECIFIC_RESERVED: win32more.Windows.Win32.Storage.Nvme.NVME_ASYNC_EVENT_TYPE_VENDOR_SPECIFIC_CODES = 0
NVME_ASYNC_EVENT_TYPE_VENDOR_SPECIFIC_DEVICE_PANIC: win32more.Windows.Win32.Storage.Nvme.NVME_ASYNC_EVENT_TYPE_VENDOR_SPECIFIC_CODES = 1
class NVME_AUTO_POWER_STATE_TRANSITION_ENTRY(Structure):
    Reserved0: Annotated[UInt32, 3]
    IdleTransitionPowerState: Annotated[UInt32, 5]
    IdleTimePriorToTransition: Annotated[UInt32, 24]
    Reserved1: UInt32
NVME_CC_SHN_SHUTDOWN_NOTIFICATIONS = Int32
NVME_CC_SHN_NO_NOTIFICATION: win32more.Windows.Win32.Storage.Nvme.NVME_CC_SHN_SHUTDOWN_NOTIFICATIONS = 0
NVME_CC_SHN_NORMAL_SHUTDOWN: win32more.Windows.Win32.Storage.Nvme.NVME_CC_SHN_SHUTDOWN_NOTIFICATIONS = 1
NVME_CC_SHN_ABRUPT_SHUTDOWN: win32more.Windows.Win32.Storage.Nvme.NVME_CC_SHN_SHUTDOWN_NOTIFICATIONS = 2
class NVME_CDW0_FEATURE_ENABLE_IEEE1667_SILO(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        Enabled: Annotated[UInt32, 3]
        Reserved0: Annotated[UInt32, 29]
class NVME_CDW0_FEATURE_ERROR_INJECTION(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        NUM: Annotated[UInt32, 7]
        Reserved0: Annotated[UInt32, 25]
class NVME_CDW0_FEATURE_READONLY_WRITETHROUGH_MODE(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        EOLBehavior: Annotated[UInt32, 3]
        Reserved0: Annotated[UInt32, 29]
class NVME_CDW0_RESERVATION_PERSISTENCE(Structure):
    PTPL: Annotated[UInt32, 1]
    Reserved: Annotated[UInt32, 31]
class NVME_CDW10_ABORT(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        SQID: Annotated[UInt32, 8]
        CID: Annotated[UInt32, 16]
class NVME_CDW10_CREATE_IO_QUEUE(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        QID: Annotated[UInt32, 16]
        QSIZE: Annotated[UInt32, 16]
class NVME_CDW10_DATASET_MANAGEMENT(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        NR: Annotated[UInt32, 8]
        Reserved: Annotated[UInt32, 24]
class NVME_CDW10_DIRECTIVE_RECEIVE(Structure):
    NUMD: UInt32
class NVME_CDW10_DIRECTIVE_SEND(Structure):
    NUMD: UInt32
class NVME_CDW10_FIRMWARE_ACTIVATE(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        FS: Annotated[UInt32, 3]
        AA: Annotated[UInt32, 2]
        Reserved: Annotated[UInt32, 27]
class NVME_CDW10_FIRMWARE_DOWNLOAD(Structure):
    NUMD: UInt32
class NVME_CDW10_FORMAT_NVM(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        LBAF: Annotated[UInt32, 4]
        MS: Annotated[UInt32, 1]
        PI: Annotated[UInt32, 3]
        PIL: Annotated[UInt32, 1]
        SES: Annotated[UInt32, 3]
        ZF: Annotated[UInt32, 2]
        Reserved: Annotated[UInt32, 18]
class NVME_CDW10_GET_FEATURES(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        FID: Annotated[UInt32, 8]
        SEL: Annotated[UInt32, 3]
        Reserved0: Annotated[UInt32, 21]
class NVME_CDW10_GET_LOG_PAGE(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        LID: Annotated[UInt32, 8]
        Reserved0: Annotated[UInt32, 8]
        NUMD: Annotated[UInt32, 12]
        Reserved1: Annotated[UInt32, 4]
class NVME_CDW10_GET_LOG_PAGE_V13(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        LID: Annotated[UInt32, 8]
        LSP: Annotated[UInt32, 4]
        Reserved0: Annotated[UInt32, 3]
        RAE: Annotated[UInt32, 1]
        NUMDL: Annotated[UInt32, 16]
class NVME_CDW10_IDENTIFY(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        CNS: Annotated[UInt32, 8]
        Reserved: Annotated[UInt32, 8]
        CNTID: Annotated[UInt32, 16]
class NVME_CDW10_RESERVATION_ACQUIRE(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        RACQA: Annotated[UInt32, 3]
        IEKEY: Annotated[UInt32, 1]
        Reserved: Annotated[UInt32, 4]
        RTYPE: Annotated[UInt32, 8]
        Reserved1: Annotated[UInt32, 16]
class NVME_CDW10_RESERVATION_REGISTER(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        RREGA: Annotated[UInt32, 3]
        IEKEY: Annotated[UInt32, 1]
        Reserved: Annotated[UInt32, 26]
        CPTPL: Annotated[UInt32, 2]
class NVME_CDW10_RESERVATION_RELEASE(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        RRELA: Annotated[UInt32, 3]
        IEKEY: Annotated[UInt32, 1]
        Reserved: Annotated[UInt32, 4]
        RTYPE: Annotated[UInt32, 8]
        Reserved1: Annotated[UInt32, 16]
class NVME_CDW10_RESERVATION_REPORT(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        NUMD: UInt32
class NVME_CDW10_SANITIZE(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        SANACT: Annotated[UInt32, 3]
        AUSE: Annotated[UInt32, 1]
        OWPASS: Annotated[UInt32, 4]
        OIPBP: Annotated[UInt32, 1]
        NDAS: Annotated[UInt32, 1]
        Reserved: Annotated[UInt32, 22]
class NVME_CDW10_SECURITY_SEND_RECEIVE(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        Reserved0: Annotated[UInt32, 8]
        SPSP: Annotated[UInt32, 16]
        SECP: Annotated[UInt32, 8]
class NVME_CDW10_SET_FEATURES(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        FID: Annotated[UInt32, 8]
        Reserved0: Annotated[UInt32, 23]
        SV: Annotated[UInt32, 1]
class NVME_CDW10_ZONE_APPEND(Structure):
    SLBA: UInt64
class NVME_CDW10_ZONE_MANAGEMENT_RECEIVE(Structure):
    SLBA: UInt64
class NVME_CDW10_ZONE_MANAGEMENT_SEND(Structure):
    SLBA: UInt64
class NVME_CDW11_CREATE_IO_CQ(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        PC: Annotated[UInt32, 1]
        IEN: Annotated[UInt32, 1]
        Reserved0: Annotated[UInt32, 14]
        IV: Annotated[UInt32, 16]
class NVME_CDW11_CREATE_IO_SQ(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        PC: Annotated[UInt32, 1]
        QPRIO: Annotated[UInt32, 2]
        Reserved0: Annotated[UInt32, 13]
        CQID: Annotated[UInt32, 16]
class NVME_CDW11_DATASET_MANAGEMENT(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        IDR: Annotated[UInt32, 1]
        IDW: Annotated[UInt32, 1]
        AD: Annotated[UInt32, 1]
        Reserved: Annotated[UInt32, 29]
class NVME_CDW11_DIRECTIVE_RECEIVE(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        DOPER: Annotated[UInt32, 8]
        DTYPE: Annotated[UInt32, 8]
        DSPEC: Annotated[UInt32, 16]
class NVME_CDW11_DIRECTIVE_SEND(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        DOPER: Annotated[UInt32, 8]
        DTYPE: Annotated[UInt32, 8]
        DSPEC: Annotated[UInt32, 16]
class NVME_CDW11_FEATURES(Union):
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
class NVME_CDW11_FEATURE_ARBITRATION(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        AB: Annotated[UInt32, 3]
        Reserved0: Annotated[UInt32, 5]
        LPW: Annotated[UInt32, 8]
        MPW: Annotated[UInt32, 8]
        HPW: Annotated[UInt32, 8]
class NVME_CDW11_FEATURE_ASYNC_EVENT_CONFIG(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        CriticalWarnings: Annotated[UInt32, 8]
        NsAttributeNotices: Annotated[UInt32, 1]
        FwActivationNotices: Annotated[UInt32, 1]
        TelemetryLogNotices: Annotated[UInt32, 1]
        ANAChangeNotices: Annotated[UInt32, 1]
        PredictableLogChangeNotices: Annotated[UInt32, 1]
        LBAStatusNotices: Annotated[UInt32, 1]
        EnduranceEventNotices: Annotated[UInt32, 1]
        Reserved0: Annotated[UInt32, 12]
        ZoneDescriptorNotices: Annotated[UInt32, 1]
        Reserved1: Annotated[UInt32, 4]
class NVME_CDW11_FEATURE_AUTO_POWER_STATE_TRANSITION(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        APSTE: Annotated[UInt32, 1]
        Reserved0: Annotated[UInt32, 31]
class NVME_CDW11_FEATURE_CLEAR_FW_UPDATE_HISTORY(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        Reserved0: Annotated[UInt32, 31]
        Clear: Annotated[UInt32, 1]
class NVME_CDW11_FEATURE_CLEAR_PCIE_CORRECTABLE_ERROR_COUNTERS(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        Reserved0: Annotated[UInt32, 31]
        Clear: Annotated[UInt32, 1]
class NVME_CDW11_FEATURE_ENABLE_IEEE1667_SILO(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        Reserved0: Annotated[UInt32, 31]
        Enable: Annotated[UInt32, 1]
class NVME_CDW11_FEATURE_ERROR_RECOVERY(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        TLER: Annotated[UInt32, 16]
        DULBE: Annotated[UInt32, 1]
        Reserved0: Annotated[UInt32, 15]
class NVME_CDW11_FEATURE_GET_HOST_METADATA(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        GDHM: Annotated[UInt32, 1]
        Reserved: Annotated[UInt32, 31]
class NVME_CDW11_FEATURE_HOST_IDENTIFIER(Structure):
    EXHID: Annotated[UInt32, 1]
    Reserved: Annotated[UInt32, 31]
class NVME_CDW11_FEATURE_HOST_MEMORY_BUFFER(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        EHM: Annotated[UInt32, 1]
        MR: Annotated[UInt32, 1]
        Reserved: Annotated[UInt32, 30]
class NVME_CDW11_FEATURE_INTERRUPT_COALESCING(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        THR: Annotated[UInt32, 8]
        TIME: Annotated[UInt32, 8]
        Reserved0: Annotated[UInt32, 16]
class NVME_CDW11_FEATURE_INTERRUPT_VECTOR_CONFIG(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        IV: Annotated[UInt32, 16]
        CD: Annotated[UInt32, 1]
        Reserved0: Annotated[UInt32, 15]
class NVME_CDW11_FEATURE_IO_COMMAND_SET_PROFILE(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        IOCSCI: Annotated[UInt32, 8]
        Reserved: Annotated[UInt32, 24]
class NVME_CDW11_FEATURE_LBA_RANGE_TYPE(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        NUM: Annotated[UInt32, 6]
        Reserved0: Annotated[UInt32, 26]
class NVME_CDW11_FEATURE_NON_OPERATIONAL_POWER_STATE(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        NOPPME: Annotated[UInt32, 1]
        Reserved0: Annotated[UInt32, 31]
class NVME_CDW11_FEATURE_NUMBER_OF_QUEUES(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        NSQ: Annotated[UInt32, 16]
        NCQ: Annotated[UInt32, 16]
class NVME_CDW11_FEATURE_POWER_MANAGEMENT(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        PS: Annotated[UInt32, 5]
        Reserved0: Annotated[UInt32, 27]
class NVME_CDW11_FEATURE_READONLY_WRITETHROUGH_MODE(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        Reserved0: Annotated[UInt32, 30]
        EOLBehavior: Annotated[UInt32, 2]
class NVME_CDW11_FEATURE_RESERVATION_NOTIFICATION_MASK(Structure):
    Reserved: Annotated[UInt32, 1]
    REGPRE: Annotated[UInt32, 1]
    RESREL: Annotated[UInt32, 1]
    RESPRE: Annotated[UInt32, 1]
    Reserved1: Annotated[UInt32, 28]
class NVME_CDW11_FEATURE_RESERVATION_PERSISTENCE(Structure):
    PTPL: Annotated[UInt32, 1]
    Reserved: Annotated[UInt32, 31]
class NVME_CDW11_FEATURE_SET_HOST_METADATA(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        Reserved0: Annotated[UInt32, 13]
        EA: Annotated[UInt32, 2]
        Reserved1: Annotated[UInt32, 17]
class NVME_CDW11_FEATURE_SUPPORTED_CAPABILITY(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        SAVE: Annotated[UInt32, 1]
        NSS: Annotated[UInt32, 1]
        MOD: Annotated[UInt32, 1]
        Reserved0: Annotated[UInt32, 29]
class NVME_CDW11_FEATURE_TEMPERATURE_THRESHOLD(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        TMPTH: Annotated[UInt32, 16]
        TMPSEL: Annotated[UInt32, 4]
        THSEL: Annotated[UInt32, 2]
        Reserved0: Annotated[UInt32, 10]
class NVME_CDW11_FEATURE_VOLATILE_WRITE_CACHE(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        WCE: Annotated[UInt32, 1]
        Reserved0: Annotated[UInt32, 31]
class NVME_CDW11_FEATURE_WRITE_ATOMICITY_NORMAL(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        DN: Annotated[UInt32, 1]
        Reserved0: Annotated[UInt32, 31]
class NVME_CDW11_FIRMWARE_DOWNLOAD(Structure):
    OFST: UInt32
class NVME_CDW11_GET_LOG_PAGE(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        NUMDU: Annotated[UInt32, 16]
        LogSpecificIdentifier: Annotated[UInt32, 16]
class NVME_CDW11_IDENTIFY(Union):
    Anonymous1: _Anonymous1_e__Struct
    Anonymous2: _Anonymous2_e__Struct
    AsUlong: UInt32
    class _Anonymous1_e__Struct(Structure):
        NVMSETID: UInt16
        Reserved: UInt16
    class _Anonymous2_e__Struct(Structure):
        CNSID: Annotated[UInt32, 16]
        Reserved2: Annotated[UInt32, 8]
        CSI: Annotated[UInt32, 8]
class NVME_CDW11_RESERVATION_REPORT(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        EDS: Annotated[UInt32, 1]
        Reserved: Annotated[UInt32, 31]
class NVME_CDW11_SANITIZE(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        OVRPAT: UInt32
class NVME_CDW11_SECURITY_RECEIVE(Structure):
    AL: UInt32
class NVME_CDW11_SECURITY_SEND(Structure):
    TL: UInt32
class NVME_CDW12_DIRECTIVE_RECEIVE(Union):
    AllocateResources: win32more.Windows.Win32.Storage.Nvme.NVME_CDW12_DIRECTIVE_RECEIVE_STREAMS_ALLOCATE_RESOURCES
    AsUlong: UInt32
class NVME_CDW12_DIRECTIVE_RECEIVE_STREAMS_ALLOCATE_RESOURCES(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        NSR: Annotated[UInt32, 16]
        Reserved: Annotated[UInt32, 16]
class NVME_CDW12_DIRECTIVE_SEND(Union):
    EnableDirective: win32more.Windows.Win32.Storage.Nvme.NVME_CDW12_DIRECTIVE_SEND_IDENTIFY_ENABLE_DIRECTIVE
    AsUlong: UInt32
class NVME_CDW12_DIRECTIVE_SEND_IDENTIFY_ENABLE_DIRECTIVE(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        ENDIR: Annotated[UInt32, 1]
        Reserved0: Annotated[UInt32, 7]
        DTYPE: Annotated[UInt32, 8]
        Reserved1: Annotated[UInt32, 16]
class NVME_CDW12_FEATURES(Union):
    HostMemoryBuffer: win32more.Windows.Win32.Storage.Nvme.NVME_CDW12_FEATURE_HOST_MEMORY_BUFFER
    AsUlong: UInt32
class NVME_CDW12_FEATURE_HOST_MEMORY_BUFFER(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        HSIZE: UInt32
class NVME_CDW12_GET_LOG_PAGE(Structure):
    LPOL: UInt32
class NVME_CDW12_READ_WRITE(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        NLB: Annotated[UInt32, 16]
        Reserved0: Annotated[UInt32, 4]
        DTYPE: Annotated[UInt32, 4]
        Reserved1: Annotated[UInt32, 2]
        PRINFO: Annotated[UInt32, 4]
        FUA: Annotated[UInt32, 1]
        LR: Annotated[UInt32, 1]
class NVME_CDW12_ZONE_APPEND(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        NLB: Annotated[UInt32, 16]
        Reserved: Annotated[UInt32, 9]
        PIREMAP: Annotated[UInt32, 1]
        PRINFO: Annotated[UInt32, 4]
        FUA: Annotated[UInt32, 1]
        LR: Annotated[UInt32, 1]
class NVME_CDW13_FEATURES(Union):
    HostMemoryBuffer: win32more.Windows.Win32.Storage.Nvme.NVME_CDW13_FEATURE_HOST_MEMORY_BUFFER
    AsUlong: UInt32
class NVME_CDW13_FEATURE_HOST_MEMORY_BUFFER(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        Reserved: Annotated[UInt32, 4]
        HMDLLA: Annotated[UInt32, 28]
class NVME_CDW13_GET_LOG_PAGE(Structure):
    LPOU: UInt32
class NVME_CDW13_READ_WRITE(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        DSM: _DSM_e__Struct
        Reserved: Byte
        DSPEC: UInt16
        class _DSM_e__Struct(Structure):
            AccessFrequency: Annotated[Byte, 4]
            AccessLatency: Annotated[Byte, 2]
            SequentialRequest: Annotated[Byte, 1]
            Incompressible: Annotated[Byte, 1]
class NVME_CDW13_ZONE_MANAGEMENT_RECEIVE(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        ZRA: Annotated[UInt32, 8]
        ZRASpecific: Annotated[UInt32, 8]
        Partial: Annotated[UInt32, 1]
        Reserved: Annotated[UInt32, 15]
class NVME_CDW13_ZONE_MANAGEMENT_SEND(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        ZSA: Annotated[UInt32, 8]
        SelectAll: Annotated[UInt32, 1]
        Reserved: Annotated[UInt32, 23]
class NVME_CDW14_FEATURES(Union):
    HostMemoryBuffer: win32more.Windows.Win32.Storage.Nvme.NVME_CDW14_FEATURE_HOST_MEMORY_BUFFER
    AsUlong: UInt32
class NVME_CDW14_FEATURE_HOST_MEMORY_BUFFER(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        HMDLUA: UInt32
class NVME_CDW14_GET_LOG_PAGE(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        UUIDIndex: Annotated[UInt32, 7]
        Reserved: Annotated[UInt32, 17]
        CommandSetIdentifier: Annotated[UInt32, 8]
class NVME_CDW15_FEATURES(Union):
    HostMemoryBuffer: win32more.Windows.Win32.Storage.Nvme.NVME_CDW15_FEATURE_HOST_MEMORY_BUFFER
    AsUlong: UInt32
class NVME_CDW15_FEATURE_HOST_MEMORY_BUFFER(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        HMDLEC: UInt32
class NVME_CDW15_READ_WRITE(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        ELBAT: Annotated[UInt32, 16]
        ELBATM: Annotated[UInt32, 16]
class NVME_CDW15_ZONE_APPEND(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        LBAT: Annotated[UInt32, 16]
        LBATM: Annotated[UInt32, 16]
class NVME_CHANGED_NAMESPACE_LIST_LOG(Structure):
    NSID: UInt32 * 1024
class NVME_CHANGED_ZONE_LIST_LOG(Structure):
    ZoneIdentifiersCount: UInt16
    Reserved: Byte * 6
    ZoneIdentifier: UInt64 * 511
NVME_CMBSZ_SIZE_UNITS = Int32
NVME_CMBSZ_SIZE_UNITS_4KB: win32more.Windows.Win32.Storage.Nvme.NVME_CMBSZ_SIZE_UNITS = 0
NVME_CMBSZ_SIZE_UNITS_64KB: win32more.Windows.Win32.Storage.Nvme.NVME_CMBSZ_SIZE_UNITS = 1
NVME_CMBSZ_SIZE_UNITS_1MB: win32more.Windows.Win32.Storage.Nvme.NVME_CMBSZ_SIZE_UNITS = 2
NVME_CMBSZ_SIZE_UNITS_16MB: win32more.Windows.Win32.Storage.Nvme.NVME_CMBSZ_SIZE_UNITS = 3
NVME_CMBSZ_SIZE_UNITS_256MB: win32more.Windows.Win32.Storage.Nvme.NVME_CMBSZ_SIZE_UNITS = 4
NVME_CMBSZ_SIZE_UNITS_4GB: win32more.Windows.Win32.Storage.Nvme.NVME_CMBSZ_SIZE_UNITS = 5
NVME_CMBSZ_SIZE_UNITS_64GB: win32more.Windows.Win32.Storage.Nvme.NVME_CMBSZ_SIZE_UNITS = 6
class NVME_COMMAND(Structure):
    CDW0: win32more.Windows.Win32.Storage.Nvme.NVME_COMMAND_DWORD0
    NSID: UInt32
    Reserved0: UInt32 * 2
    MPTR: UInt64
    PRP1: UInt64
    PRP2: UInt64
    u: _u_e__Union
    class _u_e__Union(Union):
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
        class _GENERAL_e__Struct(Structure):
            CDW10: UInt32
            CDW11: UInt32
            CDW12: UInt32
            CDW13: UInt32
            CDW14: UInt32
            CDW15: UInt32
        class _IDENTIFY_e__Struct(Structure):
            CDW10: win32more.Windows.Win32.Storage.Nvme.NVME_CDW10_IDENTIFY
            CDW11: win32more.Windows.Win32.Storage.Nvme.NVME_CDW11_IDENTIFY
            CDW12: UInt32
            CDW13: UInt32
            CDW14: UInt32
            CDW15: UInt32
        class _ABORT_e__Struct(Structure):
            CDW10: win32more.Windows.Win32.Storage.Nvme.NVME_CDW10_ABORT
            CDW11: UInt32
            CDW12: UInt32
            CDW13: UInt32
            CDW14: UInt32
            CDW15: UInt32
        class _GETFEATURES_e__Struct(Structure):
            CDW10: win32more.Windows.Win32.Storage.Nvme.NVME_CDW10_GET_FEATURES
            CDW11: win32more.Windows.Win32.Storage.Nvme.NVME_CDW11_FEATURES
            CDW12: UInt32
            CDW13: UInt32
            CDW14: UInt32
            CDW15: UInt32
        class _SETFEATURES_e__Struct(Structure):
            CDW10: win32more.Windows.Win32.Storage.Nvme.NVME_CDW10_SET_FEATURES
            CDW11: win32more.Windows.Win32.Storage.Nvme.NVME_CDW11_FEATURES
            CDW12: win32more.Windows.Win32.Storage.Nvme.NVME_CDW12_FEATURES
            CDW13: win32more.Windows.Win32.Storage.Nvme.NVME_CDW13_FEATURES
            CDW14: win32more.Windows.Win32.Storage.Nvme.NVME_CDW14_FEATURES
            CDW15: win32more.Windows.Win32.Storage.Nvme.NVME_CDW15_FEATURES
        class _GETLOGPAGE_e__Struct(Structure):
            Anonymous: _Anonymous_e__Union
            CDW11: win32more.Windows.Win32.Storage.Nvme.NVME_CDW11_GET_LOG_PAGE
            CDW12: win32more.Windows.Win32.Storage.Nvme.NVME_CDW12_GET_LOG_PAGE
            CDW13: win32more.Windows.Win32.Storage.Nvme.NVME_CDW13_GET_LOG_PAGE
            CDW14: win32more.Windows.Win32.Storage.Nvme.NVME_CDW14_GET_LOG_PAGE
            CDW15: UInt32
            class _Anonymous_e__Union(Union):
                CDW10: win32more.Windows.Win32.Storage.Nvme.NVME_CDW10_GET_LOG_PAGE
                CDW10_V13: win32more.Windows.Win32.Storage.Nvme.NVME_CDW10_GET_LOG_PAGE_V13
        class _CREATEIOCQ_e__Struct(Structure):
            CDW10: win32more.Windows.Win32.Storage.Nvme.NVME_CDW10_CREATE_IO_QUEUE
            CDW11: win32more.Windows.Win32.Storage.Nvme.NVME_CDW11_CREATE_IO_CQ
            CDW12: UInt32
            CDW13: UInt32
            CDW14: UInt32
            CDW15: UInt32
        class _CREATEIOSQ_e__Struct(Structure):
            CDW10: win32more.Windows.Win32.Storage.Nvme.NVME_CDW10_CREATE_IO_QUEUE
            CDW11: win32more.Windows.Win32.Storage.Nvme.NVME_CDW11_CREATE_IO_SQ
            CDW12: UInt32
            CDW13: UInt32
            CDW14: UInt32
            CDW15: UInt32
        class _DATASETMANAGEMENT_e__Struct(Structure):
            CDW10: win32more.Windows.Win32.Storage.Nvme.NVME_CDW10_DATASET_MANAGEMENT
            CDW11: win32more.Windows.Win32.Storage.Nvme.NVME_CDW11_DATASET_MANAGEMENT
            CDW12: UInt32
            CDW13: UInt32
            CDW14: UInt32
            CDW15: UInt32
        class _SECURITYSEND_e__Struct(Structure):
            CDW10: win32more.Windows.Win32.Storage.Nvme.NVME_CDW10_SECURITY_SEND_RECEIVE
            CDW11: win32more.Windows.Win32.Storage.Nvme.NVME_CDW11_SECURITY_SEND
            CDW12: UInt32
            CDW13: UInt32
            CDW14: UInt32
            CDW15: UInt32
        class _SECURITYRECEIVE_e__Struct(Structure):
            CDW10: win32more.Windows.Win32.Storage.Nvme.NVME_CDW10_SECURITY_SEND_RECEIVE
            CDW11: win32more.Windows.Win32.Storage.Nvme.NVME_CDW11_SECURITY_RECEIVE
            CDW12: UInt32
            CDW13: UInt32
            CDW14: UInt32
            CDW15: UInt32
        class _FIRMWAREDOWNLOAD_e__Struct(Structure):
            CDW10: win32more.Windows.Win32.Storage.Nvme.NVME_CDW10_FIRMWARE_DOWNLOAD
            CDW11: win32more.Windows.Win32.Storage.Nvme.NVME_CDW11_FIRMWARE_DOWNLOAD
            CDW12: UInt32
            CDW13: UInt32
            CDW14: UInt32
            CDW15: UInt32
        class _FIRMWAREACTIVATE_e__Struct(Structure):
            CDW10: win32more.Windows.Win32.Storage.Nvme.NVME_CDW10_FIRMWARE_ACTIVATE
            CDW11: UInt32
            CDW12: UInt32
            CDW13: UInt32
            CDW14: UInt32
            CDW15: UInt32
        class _FORMATNVM_e__Struct(Structure):
            CDW10: win32more.Windows.Win32.Storage.Nvme.NVME_CDW10_FORMAT_NVM
            CDW11: UInt32
            CDW12: UInt32
            CDW13: UInt32
            CDW14: UInt32
            CDW15: UInt32
        class _DIRECTIVERECEIVE_e__Struct(Structure):
            CDW10: win32more.Windows.Win32.Storage.Nvme.NVME_CDW10_DIRECTIVE_RECEIVE
            CDW11: win32more.Windows.Win32.Storage.Nvme.NVME_CDW11_DIRECTIVE_RECEIVE
            CDW12: win32more.Windows.Win32.Storage.Nvme.NVME_CDW12_DIRECTIVE_RECEIVE
            CDW13: UInt32
            CDW14: UInt32
            CDW15: UInt32
        class _DIRECTIVESEND_e__Struct(Structure):
            CDW10: win32more.Windows.Win32.Storage.Nvme.NVME_CDW10_DIRECTIVE_SEND
            CDW11: win32more.Windows.Win32.Storage.Nvme.NVME_CDW11_DIRECTIVE_SEND
            CDW12: win32more.Windows.Win32.Storage.Nvme.NVME_CDW12_DIRECTIVE_SEND
            CDW13: UInt32
            CDW14: UInt32
            CDW15: UInt32
        class _SANITIZE_e__Struct(Structure):
            CDW10: win32more.Windows.Win32.Storage.Nvme.NVME_CDW10_SANITIZE
            CDW11: win32more.Windows.Win32.Storage.Nvme.NVME_CDW11_SANITIZE
            CDW12: UInt32
            CDW13: UInt32
            CDW14: UInt32
            CDW15: UInt32
        class _READWRITE_e__Struct(Structure):
            LBALOW: UInt32
            LBAHIGH: UInt32
            CDW12: win32more.Windows.Win32.Storage.Nvme.NVME_CDW12_READ_WRITE
            CDW13: win32more.Windows.Win32.Storage.Nvme.NVME_CDW13_READ_WRITE
            CDW14: UInt32
            CDW15: win32more.Windows.Win32.Storage.Nvme.NVME_CDW15_READ_WRITE
        class _RESERVATIONACQUIRE_e__Struct(Structure):
            CDW10: win32more.Windows.Win32.Storage.Nvme.NVME_CDW10_RESERVATION_ACQUIRE
            CDW11: UInt32
            CDW12: UInt32
            CDW13: UInt32
            CDW14: UInt32
            CDW15: UInt32
        class _RESERVATIONREGISTER_e__Struct(Structure):
            CDW10: win32more.Windows.Win32.Storage.Nvme.NVME_CDW10_RESERVATION_REGISTER
            CDW11: UInt32
            CDW12: UInt32
            CDW13: UInt32
            CDW14: UInt32
            CDW15: UInt32
        class _RESERVATIONRELEASE_e__Struct(Structure):
            CDW10: win32more.Windows.Win32.Storage.Nvme.NVME_CDW10_RESERVATION_RELEASE
            CDW11: UInt32
            CDW12: UInt32
            CDW13: UInt32
            CDW14: UInt32
            CDW15: UInt32
        class _RESERVATIONREPORT_e__Struct(Structure):
            CDW10: win32more.Windows.Win32.Storage.Nvme.NVME_CDW10_RESERVATION_REPORT
            CDW11: win32more.Windows.Win32.Storage.Nvme.NVME_CDW11_RESERVATION_REPORT
            CDW12: UInt32
            CDW13: UInt32
            CDW14: UInt32
            CDW15: UInt32
        class _ZONEMANAGEMENTSEND_e__Struct(Structure):
            CDW1011: win32more.Windows.Win32.Storage.Nvme.NVME_CDW10_ZONE_MANAGEMENT_SEND
            CDW12: UInt32
            CDW13: win32more.Windows.Win32.Storage.Nvme.NVME_CDW13_ZONE_MANAGEMENT_SEND
            CDW14: UInt32
            CDW15: UInt32
        class _ZONEMANAGEMENTRECEIVE_e__Struct(Structure):
            CDW1011: win32more.Windows.Win32.Storage.Nvme.NVME_CDW10_ZONE_MANAGEMENT_RECEIVE
            DWORDCOUNT: UInt32
            CDW13: win32more.Windows.Win32.Storage.Nvme.NVME_CDW13_ZONE_MANAGEMENT_RECEIVE
            CDW14: UInt32
            CDW15: UInt32
        class _ZONEAPPEND_e__Struct(Structure):
            CDW1011: win32more.Windows.Win32.Storage.Nvme.NVME_CDW10_ZONE_APPEND
            CDW12: win32more.Windows.Win32.Storage.Nvme.NVME_CDW12_ZONE_APPEND
            CDW13: UInt32
            ILBRT: UInt32
            CDW15: win32more.Windows.Win32.Storage.Nvme.NVME_CDW15_ZONE_APPEND
class NVME_COMMAND_DWORD0(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        OPC: Annotated[UInt32, 8]
        FUSE: Annotated[UInt32, 2]
        Reserved0: Annotated[UInt32, 5]
        PSDT: Annotated[UInt32, 1]
        CID: Annotated[UInt32, 16]
class NVME_COMMAND_EFFECTS_DATA(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        CSUPP: Annotated[UInt32, 1]
        LBCC: Annotated[UInt32, 1]
        NCC: Annotated[UInt32, 1]
        NIC: Annotated[UInt32, 1]
        CCC: Annotated[UInt32, 1]
        Reserved0: Annotated[UInt32, 11]
        CSE: Annotated[UInt32, 3]
        Reserved1: Annotated[UInt32, 13]
class NVME_COMMAND_EFFECTS_LOG(Structure):
    ACS: win32more.Windows.Win32.Storage.Nvme.NVME_COMMAND_EFFECTS_DATA * 256
    IOCS: win32more.Windows.Win32.Storage.Nvme.NVME_COMMAND_EFFECTS_DATA * 256
    Reserved: Byte * 2048
NVME_COMMAND_EFFECT_SBUMISSION_EXECUTION_LIMITS = Int32
NVME_COMMAND_EFFECT_SBUMISSION_EXECUTION_LIMIT_NONE: win32more.Windows.Win32.Storage.Nvme.NVME_COMMAND_EFFECT_SBUMISSION_EXECUTION_LIMITS = 0
NVME_COMMAND_EFFECT_SBUMISSION_EXECUTION_LIMIT_SINGLE_PER_NAMESPACE: win32more.Windows.Win32.Storage.Nvme.NVME_COMMAND_EFFECT_SBUMISSION_EXECUTION_LIMITS = 1
NVME_COMMAND_EFFECT_SBUMISSION_EXECUTION_LIMIT_SINGLE_PER_CONTROLLER: win32more.Windows.Win32.Storage.Nvme.NVME_COMMAND_EFFECT_SBUMISSION_EXECUTION_LIMITS = 2
NVME_COMMAND_SET_IDENTIFIERS = Int32
NVME_COMMAND_SET_NVM: win32more.Windows.Win32.Storage.Nvme.NVME_COMMAND_SET_IDENTIFIERS = 0
NVME_COMMAND_SET_KEY_VALUE: win32more.Windows.Win32.Storage.Nvme.NVME_COMMAND_SET_IDENTIFIERS = 1
NVME_COMMAND_SET_ZONED_NAMESPACE: win32more.Windows.Win32.Storage.Nvme.NVME_COMMAND_SET_IDENTIFIERS = 2
class NVME_COMMAND_STATUS(Union):
    Anonymous: _Anonymous_e__Struct
    AsUshort: UInt16
    class _Anonymous_e__Struct(Structure):
        P: Annotated[UInt16, 1]
        SC: Annotated[UInt16, 8]
        SCT: Annotated[UInt16, 3]
        Reserved: Annotated[UInt16, 2]
        M: Annotated[UInt16, 1]
        DNR: Annotated[UInt16, 1]
class NVME_COMPLETION_DW0_ASYNC_EVENT_REQUEST(Structure):
    AsyncEventType: Annotated[UInt32, 3]
    Reserved0: Annotated[UInt32, 5]
    AsyncEventInfo: Annotated[UInt32, 8]
    LogPage: Annotated[UInt32, 8]
    Reserved1: Annotated[UInt32, 8]
class NVME_COMPLETION_DW0_DIRECTIVE_RECEIVE_STREAMS_ALLOCATE_RESOURCES(Structure):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        NSA: Annotated[UInt32, 16]
        Reserved: Annotated[UInt32, 16]
class NVME_COMPLETION_ENTRY(Structure):
    DW0: UInt32
    DW1: UInt32
    DW2: _DW2_e__Union
    DW3: _DW3_e__Union
    class _DW2_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        AsUlong: UInt32
        class _Anonymous_e__Struct(Structure):
            SQHD: UInt16
            SQID: UInt16
    class _DW3_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        AsUlong: UInt32
        class _Anonymous_e__Struct(Structure):
            CID: UInt16
            Status: win32more.Windows.Win32.Storage.Nvme.NVME_COMMAND_STATUS
class NVME_COMPLETION_QUEUE_HEAD_DOORBELL(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        CQH: Annotated[UInt32, 16]
        Reserved0: Annotated[UInt32, 16]
class NVME_CONTEXT_ATTRIBUTES(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        AccessFrequency: Annotated[UInt32, 4]
        AccessLatency: Annotated[UInt32, 2]
        Reserved0: Annotated[UInt32, 2]
        SequentialReadRange: Annotated[UInt32, 1]
        SequentialWriteRange: Annotated[UInt32, 1]
        WritePrepare: Annotated[UInt32, 1]
        Reserved1: Annotated[UInt32, 13]
        CommandAccessSize: Annotated[UInt32, 8]
class NVME_CONTROLLER_CAPABILITIES(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlonglong: UInt64
    class _Anonymous_e__Struct(Structure):
        MQES: Annotated[UInt64, 16]
        CQR: Annotated[UInt64, 1]
        AMS_WeightedRoundRobinWithUrgent: Annotated[UInt64, 1]
        AMS_VendorSpecific: Annotated[UInt64, 1]
        Reserved0: Annotated[UInt64, 5]
        TO: Annotated[UInt64, 8]
        DSTRD: Annotated[UInt64, 4]
        NSSRS: Annotated[UInt64, 1]
        CSS_NVM: Annotated[UInt64, 1]
        CSS_Reserved0: Annotated[UInt64, 1]
        CSS_Reserved1: Annotated[UInt64, 1]
        CSS_Reserved2: Annotated[UInt64, 1]
        CSS_Reserved3: Annotated[UInt64, 1]
        CSS_Reserved4: Annotated[UInt64, 1]
        CSS_MultipleIo: Annotated[UInt64, 1]
        CSS_AdminOnly: Annotated[UInt64, 1]
        Reserved2: Annotated[UInt64, 3]
        MPSMIN: Annotated[UInt64, 4]
        MPSMAX: Annotated[UInt64, 4]
        Reserved3: Annotated[UInt64, 8]
class NVME_CONTROLLER_CONFIGURATION(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        EN: Annotated[UInt32, 1]
        Reserved0: Annotated[UInt32, 3]
        CSS: Annotated[UInt32, 3]
        MPS: Annotated[UInt32, 4]
        AMS: Annotated[UInt32, 3]
        SHN: Annotated[UInt32, 2]
        IOSQES: Annotated[UInt32, 4]
        IOCQES: Annotated[UInt32, 4]
        Reserved1: Annotated[UInt32, 8]
class NVME_CONTROLLER_LIST(Structure):
    NumberOfIdentifiers: UInt16
    ControllerID: UInt16 * 2047
class NVME_CONTROLLER_MEMORY_BUFFER_LOCATION(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        BIR: Annotated[UInt32, 3]
        Reserved: Annotated[UInt32, 9]
        OFST: Annotated[UInt32, 20]
class NVME_CONTROLLER_MEMORY_BUFFER_SIZE(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        SQS: Annotated[UInt32, 1]
        CQS: Annotated[UInt32, 1]
        LISTS: Annotated[UInt32, 1]
        RDS: Annotated[UInt32, 1]
        WDS: Annotated[UInt32, 1]
        Reserved: Annotated[UInt32, 3]
        SZU: Annotated[UInt32, 4]
        SZ: Annotated[UInt32, 20]
NVME_CONTROLLER_METADATA_ELEMENT_TYPES = Int32
NVME_CONTROLLER_METADATA_OPERATING_SYSTEM_CONTROLLER_NAME: win32more.Windows.Win32.Storage.Nvme.NVME_CONTROLLER_METADATA_ELEMENT_TYPES = 1
NVME_CONTROLLER_METADATA_OPERATING_SYSTEM_DRIVER_NAME: win32more.Windows.Win32.Storage.Nvme.NVME_CONTROLLER_METADATA_ELEMENT_TYPES = 2
NVME_CONTROLLER_METADATA_OPERATING_SYSTEM_DRIVER_VERSION: win32more.Windows.Win32.Storage.Nvme.NVME_CONTROLLER_METADATA_ELEMENT_TYPES = 3
NVME_CONTROLLER_METADATA_PREBOOT_CONTROLLER_NAME: win32more.Windows.Win32.Storage.Nvme.NVME_CONTROLLER_METADATA_ELEMENT_TYPES = 4
NVME_CONTROLLER_METADATA_PREBOOT_DRIVER_NAME: win32more.Windows.Win32.Storage.Nvme.NVME_CONTROLLER_METADATA_ELEMENT_TYPES = 5
NVME_CONTROLLER_METADATA_PREBOOT_DRIVER_VERSION: win32more.Windows.Win32.Storage.Nvme.NVME_CONTROLLER_METADATA_ELEMENT_TYPES = 6
NVME_CONTROLLER_METADATA_SYSTEM_PROCESSOR_MODEL: win32more.Windows.Win32.Storage.Nvme.NVME_CONTROLLER_METADATA_ELEMENT_TYPES = 7
NVME_CONTROLLER_METADATA_CHIPSET_DRIVER_NAME: win32more.Windows.Win32.Storage.Nvme.NVME_CONTROLLER_METADATA_ELEMENT_TYPES = 8
NVME_CONTROLLER_METADATA_CHIPSET_DRIVER_VERSION: win32more.Windows.Win32.Storage.Nvme.NVME_CONTROLLER_METADATA_ELEMENT_TYPES = 9
NVME_CONTROLLER_METADATA_OPERATING_SYSTEM_NAME_AND_BUILD: win32more.Windows.Win32.Storage.Nvme.NVME_CONTROLLER_METADATA_ELEMENT_TYPES = 10
NVME_CONTROLLER_METADATA_SYSTEM_PRODUCT_NAME: win32more.Windows.Win32.Storage.Nvme.NVME_CONTROLLER_METADATA_ELEMENT_TYPES = 11
NVME_CONTROLLER_METADATA_FIRMWARE_VERSION: win32more.Windows.Win32.Storage.Nvme.NVME_CONTROLLER_METADATA_ELEMENT_TYPES = 12
NVME_CONTROLLER_METADATA_OPERATING_SYSTEM_DRIVER_FILENAME: win32more.Windows.Win32.Storage.Nvme.NVME_CONTROLLER_METADATA_ELEMENT_TYPES = 13
NVME_CONTROLLER_METADATA_DISPLAY_DRIVER_NAME: win32more.Windows.Win32.Storage.Nvme.NVME_CONTROLLER_METADATA_ELEMENT_TYPES = 14
NVME_CONTROLLER_METADATA_DISPLAY_DRIVER_VERSION: win32more.Windows.Win32.Storage.Nvme.NVME_CONTROLLER_METADATA_ELEMENT_TYPES = 15
NVME_CONTROLLER_METADATA_HOST_DETERMINED_FAILURE_RECORD: win32more.Windows.Win32.Storage.Nvme.NVME_CONTROLLER_METADATA_ELEMENT_TYPES = 16
class NVME_CONTROLLER_REGISTERS(Structure):
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
class NVME_CONTROLLER_STATUS(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        RDY: Annotated[UInt32, 1]
        CFS: Annotated[UInt32, 1]
        SHST: Annotated[UInt32, 2]
        NSSRO: Annotated[UInt32, 1]
        PP: Annotated[UInt32, 1]
        Reserved0: Annotated[UInt32, 26]
NVME_CSS_COMMAND_SETS = Int32
NVME_CSS_NVM_COMMAND_SET: win32more.Windows.Win32.Storage.Nvme.NVME_CSS_COMMAND_SETS = 0
NVME_CSS_ALL_SUPPORTED_IO_COMMAND_SET: win32more.Windows.Win32.Storage.Nvme.NVME_CSS_COMMAND_SETS = 6
NVME_CSS_ADMIN_COMMAND_SET_ONLY: win32more.Windows.Win32.Storage.Nvme.NVME_CSS_COMMAND_SETS = 7
NVME_CSTS_SHST_SHUTDOWN_STATUS = Int32
NVME_CSTS_SHST_NO_SHUTDOWN: win32more.Windows.Win32.Storage.Nvme.NVME_CSTS_SHST_SHUTDOWN_STATUS = 0
NVME_CSTS_SHST_SHUTDOWN_IN_PROCESS: win32more.Windows.Win32.Storage.Nvme.NVME_CSTS_SHST_SHUTDOWN_STATUS = 1
NVME_CSTS_SHST_SHUTDOWN_COMPLETED: win32more.Windows.Win32.Storage.Nvme.NVME_CSTS_SHST_SHUTDOWN_STATUS = 2
class NVME_DEVICE_SELF_TEST_LOG(Structure):
    CurrentOperation: _CurrentOperation_e__Struct
    CurrentCompletion: _CurrentCompletion_e__Struct
    Reserved: Byte * 2
    ResultData: win32more.Windows.Win32.Storage.Nvme.NVME_DEVICE_SELF_TEST_RESULT_DATA * 20
    class _CurrentOperation_e__Struct(Structure):
        Status: Annotated[Byte, 4]
        Reserved: Annotated[Byte, 4]
    class _CurrentCompletion_e__Struct(Structure):
        CompletePercent: Annotated[Byte, 7]
        Reserved: Annotated[Byte, 1]
class NVME_DEVICE_SELF_TEST_RESULT_DATA(Structure):
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
    class _Status_e__Struct(Structure):
        Result: Annotated[Byte, 4]
        CodeValue: Annotated[Byte, 4]
    class _ValidDiagnostics_e__Struct(Structure):
        NSIDValid: Annotated[Byte, 1]
        FLBAValid: Annotated[Byte, 1]
        SCTValid: Annotated[Byte, 1]
        SCValid: Annotated[Byte, 1]
        Reserved: Annotated[Byte, 4]
    class _StatusCodeType_e__Struct(Structure):
        AdditionalInfo: Annotated[Byte, 3]
        Reserved: Annotated[Byte, 5]
class NVME_DIRECTIVE_IDENTIFY_RETURN_PARAMETERS(Structure):
    DirectivesSupported: win32more.Windows.Win32.Storage.Nvme.NVME_DIRECTIVE_IDENTIFY_RETURN_PARAMETERS_DESCRIPTOR
    DirectivesEnabled: win32more.Windows.Win32.Storage.Nvme.NVME_DIRECTIVE_IDENTIFY_RETURN_PARAMETERS_DESCRIPTOR
class NVME_DIRECTIVE_IDENTIFY_RETURN_PARAMETERS_DESCRIPTOR(Structure):
    Identify: Annotated[Byte, 1]
    Streams: Annotated[Byte, 1]
    Reserved0: Annotated[Byte, 6]
    Reserved1: Byte * 31
NVME_DIRECTIVE_RECEIVE_IDENTIFY_OPERATIONS = Int32
NVME_DIRECTIVE_RECEIVE_IDENTIFY_OPERATION_RETURN_PARAMETERS: win32more.Windows.Win32.Storage.Nvme.NVME_DIRECTIVE_RECEIVE_IDENTIFY_OPERATIONS = 1
NVME_DIRECTIVE_RECEIVE_STREAMS_OPERATIONS = Int32
NVME_DIRECTIVE_RECEIVE_STREAMS_OPERATION_RETURN_PARAMETERS: win32more.Windows.Win32.Storage.Nvme.NVME_DIRECTIVE_RECEIVE_STREAMS_OPERATIONS = 1
NVME_DIRECTIVE_RECEIVE_STREAMS_OPERATION_GET_STATUS: win32more.Windows.Win32.Storage.Nvme.NVME_DIRECTIVE_RECEIVE_STREAMS_OPERATIONS = 2
NVME_DIRECTIVE_RECEIVE_STREAMS_OPERATION_ALLOCATE_RESOURCES: win32more.Windows.Win32.Storage.Nvme.NVME_DIRECTIVE_RECEIVE_STREAMS_OPERATIONS = 3
NVME_DIRECTIVE_SEND_IDENTIFY_OPERATIONS = Int32
NVME_DIRECTIVE_SEND_IDENTIFY_OPERATION_ENABLE_DIRECTIVE: win32more.Windows.Win32.Storage.Nvme.NVME_DIRECTIVE_SEND_IDENTIFY_OPERATIONS = 1
NVME_DIRECTIVE_SEND_STREAMS_OPERATIONS = Int32
NVME_DIRECTIVE_SEND_STREAMS_OPERATION_RELEASE_IDENTIFIER: win32more.Windows.Win32.Storage.Nvme.NVME_DIRECTIVE_SEND_STREAMS_OPERATIONS = 1
NVME_DIRECTIVE_SEND_STREAMS_OPERATION_RELEASE_RESOURCES: win32more.Windows.Win32.Storage.Nvme.NVME_DIRECTIVE_SEND_STREAMS_OPERATIONS = 2
class NVME_DIRECTIVE_STREAMS_GET_STATUS_DATA(Structure):
    OpenStreamCount: UInt16
    StreamIdentifiers: UInt16 * 65535
class NVME_DIRECTIVE_STREAMS_RETURN_PARAMETERS(Structure):
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
NVME_DIRECTIVE_TYPE_IDENTIFY: win32more.Windows.Win32.Storage.Nvme.NVME_DIRECTIVE_TYPES = 0
NVME_DIRECTIVE_TYPE_STREAMS: win32more.Windows.Win32.Storage.Nvme.NVME_DIRECTIVE_TYPES = 1
class NVME_ENDURANCE_GROUP_LOG(Structure):
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
class NVME_ERROR_INFO_LOG(Structure):
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
    class _ParameterErrorLocation_e__Struct(Structure):
        Byte: Annotated[UInt16, 8]
        Bit: Annotated[UInt16, 3]
        Reserved: Annotated[UInt16, 5]
class NVME_ERROR_INJECTION_ENTRY(Structure):
    Flags: _Flags_e__Union
    Reserved1: Byte
    ErrorInjectionType: UInt16
    ErrorInjectionTypeSpecific: Byte * 28
    class _Flags_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        AsUchar: Byte
        class _Anonymous_e__Struct(Structure):
            Enable: Annotated[Byte, 1]
            SingleInstance: Annotated[Byte, 1]
            Reserved0: Annotated[Byte, 6]
NVME_ERROR_INJECTION_TYPES = Int32
NVME_ERROR_INJECTION_TYPE_RESERVED0: win32more.Windows.Win32.Storage.Nvme.NVME_ERROR_INJECTION_TYPES = 0
NVME_ERROR_INJECTION_TYPE_DEVICE_PANIC_CPU_CONTROLLER_HANG: win32more.Windows.Win32.Storage.Nvme.NVME_ERROR_INJECTION_TYPES = 1
NVME_ERROR_INJECTION_TYPE_DEVICE_PANIC_NAND_HANG: win32more.Windows.Win32.Storage.Nvme.NVME_ERROR_INJECTION_TYPES = 2
NVME_ERROR_INJECTION_TYPE_DEVICE_PANIC_PLP_DEFECT: win32more.Windows.Win32.Storage.Nvme.NVME_ERROR_INJECTION_TYPES = 3
NVME_ERROR_INJECTION_TYPE_DEVICE_PANIC_LOGICAL_FW_ERROR: win32more.Windows.Win32.Storage.Nvme.NVME_ERROR_INJECTION_TYPES = 4
NVME_ERROR_INJECTION_TYPE_DEVICE_PANIC_DRAM_CORRUPTION_CRITICAL: win32more.Windows.Win32.Storage.Nvme.NVME_ERROR_INJECTION_TYPES = 5
NVME_ERROR_INJECTION_TYPE_DEVICE_PANIC_DRAM_CORRUPTION_NONCRITICAL: win32more.Windows.Win32.Storage.Nvme.NVME_ERROR_INJECTION_TYPES = 6
NVME_ERROR_INJECTION_TYPE_DEVICE_PANIC_NAND_CORRUPTION: win32more.Windows.Win32.Storage.Nvme.NVME_ERROR_INJECTION_TYPES = 7
NVME_ERROR_INJECTION_TYPE_DEVICE_PANIC_SRAM_CORRUPTION: win32more.Windows.Win32.Storage.Nvme.NVME_ERROR_INJECTION_TYPES = 8
NVME_ERROR_INJECTION_TYPE_DEVICE_PANIC_HW_MALFUNCTION: win32more.Windows.Win32.Storage.Nvme.NVME_ERROR_INJECTION_TYPES = 9
NVME_ERROR_INJECTION_TYPE_RESERVED1: win32more.Windows.Win32.Storage.Nvme.NVME_ERROR_INJECTION_TYPES = 10
NVME_ERROR_INJECTION_TYPE_MAX: win32more.Windows.Win32.Storage.Nvme.NVME_ERROR_INJECTION_TYPES = 65535
class NVME_EXTENDED_REPORT_ZONE_INFO(Structure):
    ZoneCount: UInt64
    Reserved: UInt64 * 7
    Desc: win32more.Windows.Win32.Storage.Nvme.NVME_ZONE_EXTENDED_REPORT_ZONE_DESC * 1
NVME_FEATURES = Int32
NVME_FEATURE_ARBITRATION: win32more.Windows.Win32.Storage.Nvme.NVME_FEATURES = 1
NVME_FEATURE_POWER_MANAGEMENT: win32more.Windows.Win32.Storage.Nvme.NVME_FEATURES = 2
NVME_FEATURE_LBA_RANGE_TYPE: win32more.Windows.Win32.Storage.Nvme.NVME_FEATURES = 3
NVME_FEATURE_TEMPERATURE_THRESHOLD: win32more.Windows.Win32.Storage.Nvme.NVME_FEATURES = 4
NVME_FEATURE_ERROR_RECOVERY: win32more.Windows.Win32.Storage.Nvme.NVME_FEATURES = 5
NVME_FEATURE_VOLATILE_WRITE_CACHE: win32more.Windows.Win32.Storage.Nvme.NVME_FEATURES = 6
NVME_FEATURE_NUMBER_OF_QUEUES: win32more.Windows.Win32.Storage.Nvme.NVME_FEATURES = 7
NVME_FEATURE_INTERRUPT_COALESCING: win32more.Windows.Win32.Storage.Nvme.NVME_FEATURES = 8
NVME_FEATURE_INTERRUPT_VECTOR_CONFIG: win32more.Windows.Win32.Storage.Nvme.NVME_FEATURES = 9
NVME_FEATURE_WRITE_ATOMICITY: win32more.Windows.Win32.Storage.Nvme.NVME_FEATURES = 10
NVME_FEATURE_ASYNC_EVENT_CONFIG: win32more.Windows.Win32.Storage.Nvme.NVME_FEATURES = 11
NVME_FEATURE_AUTONOMOUS_POWER_STATE_TRANSITION: win32more.Windows.Win32.Storage.Nvme.NVME_FEATURES = 12
NVME_FEATURE_HOST_MEMORY_BUFFER: win32more.Windows.Win32.Storage.Nvme.NVME_FEATURES = 13
NVME_FEATURE_TIMESTAMP: win32more.Windows.Win32.Storage.Nvme.NVME_FEATURES = 14
NVME_FEATURE_KEEP_ALIVE: win32more.Windows.Win32.Storage.Nvme.NVME_FEATURES = 15
NVME_FEATURE_HOST_CONTROLLED_THERMAL_MANAGEMENT: win32more.Windows.Win32.Storage.Nvme.NVME_FEATURES = 16
NVME_FEATURE_NONOPERATIONAL_POWER_STATE: win32more.Windows.Win32.Storage.Nvme.NVME_FEATURES = 17
NVME_FEATURE_READ_RECOVERY_LEVEL_CONFIG: win32more.Windows.Win32.Storage.Nvme.NVME_FEATURES = 18
NVME_FEATURE_PREDICTABLE_LATENCY_MODE_CONFIG: win32more.Windows.Win32.Storage.Nvme.NVME_FEATURES = 19
NVME_FEATURE_PREDICTABLE_LATENCY_MODE_WINDOW: win32more.Windows.Win32.Storage.Nvme.NVME_FEATURES = 20
NVME_FEATURE_LBA_STATUS_INFORMATION_REPORT_INTERVAL: win32more.Windows.Win32.Storage.Nvme.NVME_FEATURES = 21
NVME_FEATURE_HOST_BEHAVIOR_SUPPORT: win32more.Windows.Win32.Storage.Nvme.NVME_FEATURES = 22
NVME_FEATURE_SANITIZE_CONFIG: win32more.Windows.Win32.Storage.Nvme.NVME_FEATURES = 23
NVME_FEATURE_ENDURANCE_GROUP_EVENT_CONFIG: win32more.Windows.Win32.Storage.Nvme.NVME_FEATURES = 24
NVME_FEATURE_IO_COMMAND_SET_PROFILE: win32more.Windows.Win32.Storage.Nvme.NVME_FEATURES = 25
NVME_FEATURE_ENHANCED_CONTROLLER_METADATA: win32more.Windows.Win32.Storage.Nvme.NVME_FEATURES = 125
NVME_FEATURE_CONTROLLER_METADATA: win32more.Windows.Win32.Storage.Nvme.NVME_FEATURES = 126
NVME_FEATURE_NAMESPACE_METADATA: win32more.Windows.Win32.Storage.Nvme.NVME_FEATURES = 127
NVME_FEATURE_NVM_SOFTWARE_PROGRESS_MARKER: win32more.Windows.Win32.Storage.Nvme.NVME_FEATURES = 128
NVME_FEATURE_NVM_HOST_IDENTIFIER: win32more.Windows.Win32.Storage.Nvme.NVME_FEATURES = 129
NVME_FEATURE_NVM_RESERVATION_NOTIFICATION_MASK: win32more.Windows.Win32.Storage.Nvme.NVME_FEATURES = 130
NVME_FEATURE_NVM_RESERVATION_PERSISTANCE: win32more.Windows.Win32.Storage.Nvme.NVME_FEATURES = 131
NVME_FEATURE_NVM_NAMESPACE_WRITE_PROTECTION_CONFIG: win32more.Windows.Win32.Storage.Nvme.NVME_FEATURES = 132
NVME_FEATURE_ERROR_INJECTION: win32more.Windows.Win32.Storage.Nvme.NVME_FEATURES = 192
NVME_FEATURE_CLEAR_FW_UPDATE_HISTORY: win32more.Windows.Win32.Storage.Nvme.NVME_FEATURES = 193
NVME_FEATURE_READONLY_WRITETHROUGH_MODE: win32more.Windows.Win32.Storage.Nvme.NVME_FEATURES = 194
NVME_FEATURE_CLEAR_PCIE_CORRECTABLE_ERROR_COUNTERS: win32more.Windows.Win32.Storage.Nvme.NVME_FEATURES = 195
NVME_FEATURE_ENABLE_IEEE1667_SILO: win32more.Windows.Win32.Storage.Nvme.NVME_FEATURES = 196
NVME_FEATURE_PLP_HEALTH_MONITOR: win32more.Windows.Win32.Storage.Nvme.NVME_FEATURES = 197
class NVME_FEATURE_HOST_IDENTIFIER_DATA(Structure):
    HOSTID: Byte * 16
class NVME_FEATURE_HOST_METADATA_DATA(Structure):
    NumberOfMetadataElementDescriptors: Byte
    Reserved0: Byte
    MetadataElementDescriptors: Byte * 4094
NVME_FEATURE_VALUE_CODES = Int32
NVME_FEATURE_VALUE_CURRENT: win32more.Windows.Win32.Storage.Nvme.NVME_FEATURE_VALUE_CODES = 0
NVME_FEATURE_VALUE_DEFAULT: win32more.Windows.Win32.Storage.Nvme.NVME_FEATURE_VALUE_CODES = 1
NVME_FEATURE_VALUE_SAVED: win32more.Windows.Win32.Storage.Nvme.NVME_FEATURE_VALUE_CODES = 2
NVME_FEATURE_VALUE_SUPPORTED_CAPABILITIES: win32more.Windows.Win32.Storage.Nvme.NVME_FEATURE_VALUE_CODES = 3
NVME_FIRMWARE_ACTIVATE_ACTIONS = Int32
NVME_FIRMWARE_ACTIVATE_ACTION_DOWNLOAD_TO_SLOT: win32more.Windows.Win32.Storage.Nvme.NVME_FIRMWARE_ACTIVATE_ACTIONS = 0
NVME_FIRMWARE_ACTIVATE_ACTION_DOWNLOAD_TO_SLOT_AND_ACTIVATE: win32more.Windows.Win32.Storage.Nvme.NVME_FIRMWARE_ACTIVATE_ACTIONS = 1
NVME_FIRMWARE_ACTIVATE_ACTION_ACTIVATE: win32more.Windows.Win32.Storage.Nvme.NVME_FIRMWARE_ACTIVATE_ACTIONS = 2
NVME_FIRMWARE_ACTIVATE_ACTION_DOWNLOAD_TO_SLOT_AND_ACTIVATE_IMMEDIATE: win32more.Windows.Win32.Storage.Nvme.NVME_FIRMWARE_ACTIVATE_ACTIONS = 3
class NVME_FIRMWARE_SLOT_INFO_LOG(Structure):
    AFI: _AFI_e__Struct
    Reserved0: Byte * 7
    FRS: UInt64 * 7
    Reserved1: Byte * 448
    class _AFI_e__Struct(Structure):
        ActiveSlot: Annotated[Byte, 3]
        Reserved0: Annotated[Byte, 1]
        PendingActivateSlot: Annotated[Byte, 3]
        Reserved1: Annotated[Byte, 1]
NVME_FUSED_OPERATION_CODES = Int32
NVME_FUSED_OPERATION_NORMAL: win32more.Windows.Win32.Storage.Nvme.NVME_FUSED_OPERATION_CODES = 0
NVME_FUSED_OPERATION_FIRST_CMD: win32more.Windows.Win32.Storage.Nvme.NVME_FUSED_OPERATION_CODES = 1
NVME_FUSED_OPERATION_SECOND_CMD: win32more.Windows.Win32.Storage.Nvme.NVME_FUSED_OPERATION_CODES = 2
class NVME_HEALTH_INFO_LOG(Structure):
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
    class _CriticalWarning_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        AsUchar: Byte
        class _Anonymous_e__Struct(Structure):
            AvailableSpaceLow: Annotated[Byte, 1]
            TemperatureThreshold: Annotated[Byte, 1]
            ReliabilityDegraded: Annotated[Byte, 1]
            ReadOnly: Annotated[Byte, 1]
            VolatileMemoryBackupDeviceFailed: Annotated[Byte, 1]
            Reserved: Annotated[Byte, 3]
class NVME_HOST_MEMORY_BUFFER_DESCRIPTOR_ENTRY(Structure):
    BADD: UInt64
    BSIZE: UInt32
    Reserved: UInt32
NVME_HOST_METADATA_ELEMENT_ACTIONS = Int32
NVME_HOST_METADATA_ADD_REPLACE_ENTRY: win32more.Windows.Win32.Storage.Nvme.NVME_HOST_METADATA_ELEMENT_ACTIONS = 0
NVME_HOST_METADATA_DELETE_ENTRY_MULTIPLE: win32more.Windows.Win32.Storage.Nvme.NVME_HOST_METADATA_ELEMENT_ACTIONS = 1
NVME_HOST_METADATA_ADD_ENTRY_MULTIPLE: win32more.Windows.Win32.Storage.Nvme.NVME_HOST_METADATA_ELEMENT_ACTIONS = 2
class NVME_HOST_METADATA_ELEMENT_DESCRIPTOR(Structure):
    ET: Annotated[UInt32, 6]
    Reserved0: Annotated[UInt32, 2]
    ER: Annotated[UInt32, 4]
    Reserved1: Annotated[UInt32, 4]
    ELEN: Annotated[UInt32, 16]
    EVAL: Byte * 1
NVME_IDENTIFIER_TYPE = Int32
NVME_IDENTIFIER_TYPE_EUI64: win32more.Windows.Win32.Storage.Nvme.NVME_IDENTIFIER_TYPE = 1
NVME_IDENTIFIER_TYPE_NGUID: win32more.Windows.Win32.Storage.Nvme.NVME_IDENTIFIER_TYPE = 2
NVME_IDENTIFIER_TYPE_UUID: win32more.Windows.Win32.Storage.Nvme.NVME_IDENTIFIER_TYPE = 3
NVME_IDENTIFIER_TYPE_CSI: win32more.Windows.Win32.Storage.Nvme.NVME_IDENTIFIER_TYPE = 4
NVME_IDENTIFIER_TYPE_LENGTH = Int32
NVME_IDENTIFIER_TYPE_EUI64_LENGTH: win32more.Windows.Win32.Storage.Nvme.NVME_IDENTIFIER_TYPE_LENGTH = 8
NVME_IDENTIFIER_TYPE_NGUID_LENGTH: win32more.Windows.Win32.Storage.Nvme.NVME_IDENTIFIER_TYPE_LENGTH = 16
NVME_IDENTIFIER_TYPE_UUID_LENGTH: win32more.Windows.Win32.Storage.Nvme.NVME_IDENTIFIER_TYPE_LENGTH = 16
NVME_IDENTIFIER_TYPE_CSI_LENGTH: win32more.Windows.Win32.Storage.Nvme.NVME_IDENTIFIER_TYPE_LENGTH = 1
NVME_IDENTIFY_CNS_CODES = Int32
NVME_IDENTIFY_CNS_SPECIFIC_NAMESPACE: win32more.Windows.Win32.Storage.Nvme.NVME_IDENTIFY_CNS_CODES = 0
NVME_IDENTIFY_CNS_CONTROLLER: win32more.Windows.Win32.Storage.Nvme.NVME_IDENTIFY_CNS_CODES = 1
NVME_IDENTIFY_CNS_ACTIVE_NAMESPACES: win32more.Windows.Win32.Storage.Nvme.NVME_IDENTIFY_CNS_CODES = 2
NVME_IDENTIFY_CNS_DESCRIPTOR_NAMESPACE: win32more.Windows.Win32.Storage.Nvme.NVME_IDENTIFY_CNS_CODES = 3
NVME_IDENTIFY_CNS_NVM_SET: win32more.Windows.Win32.Storage.Nvme.NVME_IDENTIFY_CNS_CODES = 4
NVME_IDENTIFY_CNS_SPECIFIC_NAMESPACE_IO_COMMAND_SET: win32more.Windows.Win32.Storage.Nvme.NVME_IDENTIFY_CNS_CODES = 5
NVME_IDENTIFY_CNS_SPECIFIC_CONTROLLER_IO_COMMAND_SET: win32more.Windows.Win32.Storage.Nvme.NVME_IDENTIFY_CNS_CODES = 6
NVME_IDENTIFY_CNS_ACTIVE_NAMESPACE_LIST_IO_COMMAND_SET: win32more.Windows.Win32.Storage.Nvme.NVME_IDENTIFY_CNS_CODES = 7
NVME_IDENTIFY_CNS_ALLOCATED_NAMESPACE_LIST: win32more.Windows.Win32.Storage.Nvme.NVME_IDENTIFY_CNS_CODES = 16
NVME_IDENTIFY_CNS_ALLOCATED_NAMESPACE: win32more.Windows.Win32.Storage.Nvme.NVME_IDENTIFY_CNS_CODES = 17
NVME_IDENTIFY_CNS_CONTROLLER_LIST_OF_NSID: win32more.Windows.Win32.Storage.Nvme.NVME_IDENTIFY_CNS_CODES = 18
NVME_IDENTIFY_CNS_CONTROLLER_LIST_OF_NVM_SUBSYSTEM: win32more.Windows.Win32.Storage.Nvme.NVME_IDENTIFY_CNS_CODES = 19
NVME_IDENTIFY_CNS_PRIMARY_CONTROLLER_CAPABILITIES: win32more.Windows.Win32.Storage.Nvme.NVME_IDENTIFY_CNS_CODES = 20
NVME_IDENTIFY_CNS_SECONDARY_CONTROLLER_LIST: win32more.Windows.Win32.Storage.Nvme.NVME_IDENTIFY_CNS_CODES = 21
NVME_IDENTIFY_CNS_NAMESPACE_GRANULARITY_LIST: win32more.Windows.Win32.Storage.Nvme.NVME_IDENTIFY_CNS_CODES = 22
NVME_IDENTIFY_CNS_UUID_LIST: win32more.Windows.Win32.Storage.Nvme.NVME_IDENTIFY_CNS_CODES = 23
NVME_IDENTIFY_CNS_DOMAIN_LIST: win32more.Windows.Win32.Storage.Nvme.NVME_IDENTIFY_CNS_CODES = 24
NVME_IDENTIFY_CNS_ENDURANCE_GROUP_LIST: win32more.Windows.Win32.Storage.Nvme.NVME_IDENTIFY_CNS_CODES = 25
NVME_IDENTIFY_CNS_ALLOCATED_NAMSPACE_LIST_IO_COMMAND_SET: win32more.Windows.Win32.Storage.Nvme.NVME_IDENTIFY_CNS_CODES = 26
NVME_IDENTIFY_CNS_ALLOCATED_NAMESPACE_IO_COMMAND_SET: win32more.Windows.Win32.Storage.Nvme.NVME_IDENTIFY_CNS_CODES = 27
NVME_IDENTIFY_CNS_IO_COMMAND_SET: win32more.Windows.Win32.Storage.Nvme.NVME_IDENTIFY_CNS_CODES = 28
class NVME_IDENTIFY_CONTROLLER_DATA(Structure):
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
    class _CMIC_e__Struct(Structure):
        MultiPCIePorts: Annotated[Byte, 1]
        MultiControllers: Annotated[Byte, 1]
        SRIOV: Annotated[Byte, 1]
        ANAR: Annotated[Byte, 1]
        Reserved: Annotated[Byte, 4]
    class _OAES_e__Struct(Structure):
        Reserved0: Annotated[UInt32, 8]
        NamespaceAttributeChanged: Annotated[UInt32, 1]
        FirmwareActivation: Annotated[UInt32, 1]
        Reserved1: Annotated[UInt32, 1]
        AsymmetricAccessChanged: Annotated[UInt32, 1]
        PredictableLatencyAggregateLogChanged: Annotated[UInt32, 1]
        LbaStatusChanged: Annotated[UInt32, 1]
        EnduranceGroupAggregateLogChanged: Annotated[UInt32, 1]
        Reserved2: Annotated[UInt32, 12]
        ZoneInformation: Annotated[UInt32, 1]
        Reserved3: Annotated[UInt32, 4]
    class _CTRATT_e__Struct(Structure):
        HostIdentifier128Bit: Annotated[UInt32, 1]
        NOPSPMode: Annotated[UInt32, 1]
        NVMSets: Annotated[UInt32, 1]
        ReadRecoveryLevels: Annotated[UInt32, 1]
        EnduranceGroups: Annotated[UInt32, 1]
        PredictableLatencyMode: Annotated[UInt32, 1]
        TBKAS: Annotated[UInt32, 1]
        NamespaceGranularity: Annotated[UInt32, 1]
        SQAssociations: Annotated[UInt32, 1]
        UUIDList: Annotated[UInt32, 1]
        Reserved0: Annotated[UInt32, 22]
    class _RRLS_e__Struct(Structure):
        ReadRecoveryLevel0: Annotated[UInt16, 1]
        ReadRecoveryLevel1: Annotated[UInt16, 1]
        ReadRecoveryLevel2: Annotated[UInt16, 1]
        ReadRecoveryLevel3: Annotated[UInt16, 1]
        ReadRecoveryLevel4: Annotated[UInt16, 1]
        ReadRecoveryLevel5: Annotated[UInt16, 1]
        ReadRecoveryLevel6: Annotated[UInt16, 1]
        ReadRecoveryLevel7: Annotated[UInt16, 1]
        ReadRecoveryLevel8: Annotated[UInt16, 1]
        ReadRecoveryLevel9: Annotated[UInt16, 1]
        ReadRecoveryLevel10: Annotated[UInt16, 1]
        ReadRecoveryLevel11: Annotated[UInt16, 1]
        ReadRecoveryLevel12: Annotated[UInt16, 1]
        ReadRecoveryLevel13: Annotated[UInt16, 1]
        ReadRecoveryLevel14: Annotated[UInt16, 1]
        ReadRecoveryLevel15: Annotated[UInt16, 1]
    class _OACS_e__Struct(Structure):
        SecurityCommands: Annotated[UInt16, 1]
        FormatNVM: Annotated[UInt16, 1]
        FirmwareCommands: Annotated[UInt16, 1]
        NamespaceCommands: Annotated[UInt16, 1]
        DeviceSelfTest: Annotated[UInt16, 1]
        Directives: Annotated[UInt16, 1]
        NVMeMICommands: Annotated[UInt16, 1]
        VirtualizationMgmt: Annotated[UInt16, 1]
        DoorBellBufferConfig: Annotated[UInt16, 1]
        GetLBAStatus: Annotated[UInt16, 1]
        Reserved: Annotated[UInt16, 6]
    class _FRMW_e__Struct(Structure):
        Slot1ReadOnly: Annotated[Byte, 1]
        SlotCount: Annotated[Byte, 3]
        ActivationWithoutReset: Annotated[Byte, 1]
        Reserved: Annotated[Byte, 3]
    class _LPA_e__Struct(Structure):
        SmartPagePerNamespace: Annotated[Byte, 1]
        CommandEffectsLog: Annotated[Byte, 1]
        LogPageExtendedData: Annotated[Byte, 1]
        TelemetrySupport: Annotated[Byte, 1]
        PersistentEventLog: Annotated[Byte, 1]
        Reserved0: Annotated[Byte, 1]
        TelemetryDataArea4: Annotated[Byte, 1]
        Reserved1: Annotated[Byte, 1]
    class _AVSCC_e__Struct(Structure):
        CommandFormatInSpec: Annotated[Byte, 1]
        Reserved: Annotated[Byte, 7]
    class _APSTA_e__Struct(Structure):
        Supported: Annotated[Byte, 1]
        Reserved: Annotated[Byte, 7]
    class _RPMBS_e__Struct(Structure):
        RPMBUnitCount: Annotated[UInt32, 3]
        AuthenticationMethod: Annotated[UInt32, 3]
        Reserved0: Annotated[UInt32, 10]
        TotalSize: Annotated[UInt32, 8]
        AccessSize: Annotated[UInt32, 8]
    class _HCTMA_e__Struct(Structure):
        Supported: Annotated[UInt16, 1]
        Reserved: Annotated[UInt16, 15]
    class _SANICAP_e__Struct(Structure):
        CryptoErase: Annotated[UInt32, 1]
        BlockErase: Annotated[UInt32, 1]
        Overwrite: Annotated[UInt32, 1]
        Reserved: Annotated[UInt32, 26]
        NDI: Annotated[UInt32, 1]
        NODMMAS: Annotated[UInt32, 2]
    class _ANACAP_e__Struct(Structure):
        OptimizedState: Annotated[Byte, 1]
        NonOptimizedState: Annotated[Byte, 1]
        InaccessibleState: Annotated[Byte, 1]
        PersistentLossState: Annotated[Byte, 1]
        ChangeState: Annotated[Byte, 1]
        Reserved: Annotated[Byte, 1]
        StaticANAGRPID: Annotated[Byte, 1]
        SupportNonZeroANAGRPID: Annotated[Byte, 1]
    class _SQES_e__Struct(Structure):
        RequiredEntrySize: Annotated[Byte, 4]
        MaxEntrySize: Annotated[Byte, 4]
    class _CQES_e__Struct(Structure):
        RequiredEntrySize: Annotated[Byte, 4]
        MaxEntrySize: Annotated[Byte, 4]
    class _ONCS_e__Struct(Structure):
        Compare: Annotated[UInt16, 1]
        WriteUncorrectable: Annotated[UInt16, 1]
        DatasetManagement: Annotated[UInt16, 1]
        WriteZeroes: Annotated[UInt16, 1]
        FeatureField: Annotated[UInt16, 1]
        Reservations: Annotated[UInt16, 1]
        Timestamp: Annotated[UInt16, 1]
        Verify: Annotated[UInt16, 1]
        Reserved: Annotated[UInt16, 8]
    class _FUSES_e__Struct(Structure):
        CompareAndWrite: Annotated[UInt16, 1]
        Reserved: Annotated[UInt16, 15]
    class _FNA_e__Struct(Structure):
        FormatApplyToAll: Annotated[Byte, 1]
        SecureEraseApplyToAll: Annotated[Byte, 1]
        CryptographicEraseSupported: Annotated[Byte, 1]
        FormatSupportNSIDAllF: Annotated[Byte, 1]
        Reserved: Annotated[Byte, 4]
    class _VWC_e__Struct(Structure):
        Present: Annotated[Byte, 1]
        FlushBehavior: Annotated[Byte, 2]
        Reserved: Annotated[Byte, 5]
    class _NVSCC_e__Struct(Structure):
        CommandFormatInSpec: Annotated[Byte, 1]
        Reserved: Annotated[Byte, 7]
    class _NWPC_e__Struct(Structure):
        WriteProtect: Annotated[Byte, 1]
        UntilPowerCycle: Annotated[Byte, 1]
        Permanent: Annotated[Byte, 1]
        Reserved: Annotated[Byte, 5]
    class _SGLS_e__Struct(Structure):
        SGLSupported: Annotated[UInt32, 2]
        KeyedSGLData: Annotated[UInt32, 1]
        Reserved0: Annotated[UInt32, 13]
        BitBucketDescrSupported: Annotated[UInt32, 1]
        ByteAlignedContiguousPhysicalBuffer: Annotated[UInt32, 1]
        SGLLengthLargerThanDataLength: Annotated[UInt32, 1]
        MPTRSGLDescriptor: Annotated[UInt32, 1]
        AddressFieldSGLDataBlock: Annotated[UInt32, 1]
        TransportSGLData: Annotated[UInt32, 1]
        Reserved1: Annotated[UInt32, 10]
class NVME_IDENTIFY_IO_COMMAND_SET(Structure):
    IOCommandSetVector: UInt64 * 512
class NVME_IDENTIFY_NAMESPACE_DATA(Structure):
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
    class _NSFEAT_e__Struct(Structure):
        ThinProvisioning: Annotated[Byte, 1]
        NameSpaceAtomicWriteUnit: Annotated[Byte, 1]
        DeallocatedOrUnwrittenError: Annotated[Byte, 1]
        SkipReuseUI: Annotated[Byte, 1]
        NameSpaceIoOptimization: Annotated[Byte, 1]
        Reserved: Annotated[Byte, 3]
    class _FLBAS_e__Struct(Structure):
        LbaFormatIndex: Annotated[Byte, 4]
        MetadataInExtendedDataLBA: Annotated[Byte, 1]
        Reserved: Annotated[Byte, 3]
    class _MC_e__Struct(Structure):
        MetadataInExtendedDataLBA: Annotated[Byte, 1]
        MetadataInSeparateBuffer: Annotated[Byte, 1]
        Reserved: Annotated[Byte, 6]
    class _DPC_e__Struct(Structure):
        ProtectionInfoType1: Annotated[Byte, 1]
        ProtectionInfoType2: Annotated[Byte, 1]
        ProtectionInfoType3: Annotated[Byte, 1]
        InfoAtBeginningOfMetadata: Annotated[Byte, 1]
        InfoAtEndOfMetadata: Annotated[Byte, 1]
        Reserved: Annotated[Byte, 3]
    class _DPS_e__Struct(Structure):
        ProtectionInfoTypeEnabled: Annotated[Byte, 3]
        InfoAtBeginningOfMetadata: Annotated[Byte, 1]
        Reserved: Annotated[Byte, 4]
    class _NMIC_e__Struct(Structure):
        SharedNameSpace: Annotated[Byte, 1]
        Reserved: Annotated[Byte, 7]
    class _FPI_e__Struct(Structure):
        PercentageRemained: Annotated[Byte, 7]
        Supported: Annotated[Byte, 1]
    class _DLFEAT_e__Struct(Structure):
        ReadBehavior: Annotated[Byte, 3]
        WriteZeroes: Annotated[Byte, 1]
        GuardFieldWithCRC: Annotated[Byte, 1]
        Reserved: Annotated[Byte, 3]
    class _NSATTR_e__Struct(Structure):
        WriteProtected: Annotated[Byte, 1]
        Reserved: Annotated[Byte, 7]
class NVME_IDENTIFY_NAMESPACE_DESCRIPTOR(Structure):
    NIDT: Byte
    NIDL: Byte
    Reserved: Byte * 2
    NID: Byte * 1
class NVME_IDENTIFY_NVM_SPECIFIC_CONTROLLER_IO_COMMAND_SET(Structure):
    VSL: Byte
    WZSL: Byte
    WUSL: Byte
    DMRL: Byte
    DMRSL: UInt32
    DMSL: UInt64
    Reserved: Byte * 4080
class NVME_IDENTIFY_SPECIFIC_NAMESPACE_IO_COMMAND_SET(Structure):
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
    class _ZOC_e__Struct(Structure):
        VariableZoneCapacity: Annotated[UInt16, 1]
        ZoneExcursions: Annotated[UInt16, 1]
        Reserved: Annotated[UInt16, 14]
    class _OZCS_e__Struct(Structure):
        ReadAcrossZoneBoundaries: Annotated[UInt16, 1]
        Reserved: Annotated[UInt16, 15]
class NVME_IDENTIFY_ZNS_SPECIFIC_CONTROLLER_IO_COMMAND_SET(Structure):
    ZASL: Byte
    Reserved: Byte * 4095
class NVME_LBA_FORMAT(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        MS: UInt16
        LBADS: Byte
        RP: Annotated[Byte, 2]
        Reserved0: Annotated[Byte, 6]
class NVME_LBA_RANGE(Structure):
    Attributes: win32more.Windows.Win32.Storage.Nvme.NVME_CONTEXT_ATTRIBUTES
    LogicalBlockCount: UInt32
    StartingLBA: UInt64
class NVME_LBA_RANGET_TYPE_ENTRY(Structure):
    Type: Byte
    Attributes: _Attributes_e__Struct
    Reserved0: Byte * 14
    SLBA: UInt64
    NLB: UInt64
    GUID: Byte * 16
    Reserved1: Byte * 16
    class _Attributes_e__Struct(Structure):
        MayOverwritten: Annotated[Byte, 1]
        Hidden: Annotated[Byte, 1]
        Reserved: Annotated[Byte, 6]
NVME_LBA_RANGE_TYPES = Int32
NVME_LBA_RANGE_TYPE_RESERVED: win32more.Windows.Win32.Storage.Nvme.NVME_LBA_RANGE_TYPES = 0
NVME_LBA_RANGE_TYPE_FILESYSTEM: win32more.Windows.Win32.Storage.Nvme.NVME_LBA_RANGE_TYPES = 1
NVME_LBA_RANGE_TYPE_RAID: win32more.Windows.Win32.Storage.Nvme.NVME_LBA_RANGE_TYPES = 2
NVME_LBA_RANGE_TYPE_CACHE: win32more.Windows.Win32.Storage.Nvme.NVME_LBA_RANGE_TYPES = 3
NVME_LBA_RANGE_TYPE_PAGE_SWAP_FILE: win32more.Windows.Win32.Storage.Nvme.NVME_LBA_RANGE_TYPES = 4
class NVME_LBA_ZONE_FORMAT(Structure):
    ZoneSize: UInt64
    ZDES: Byte
    Reserved: Byte * 7
NVME_LOG_PAGES = Int32
NVME_LOG_PAGE_ERROR_INFO: win32more.Windows.Win32.Storage.Nvme.NVME_LOG_PAGES = 1
NVME_LOG_PAGE_HEALTH_INFO: win32more.Windows.Win32.Storage.Nvme.NVME_LOG_PAGES = 2
NVME_LOG_PAGE_FIRMWARE_SLOT_INFO: win32more.Windows.Win32.Storage.Nvme.NVME_LOG_PAGES = 3
NVME_LOG_PAGE_CHANGED_NAMESPACE_LIST: win32more.Windows.Win32.Storage.Nvme.NVME_LOG_PAGES = 4
NVME_LOG_PAGE_COMMAND_EFFECTS: win32more.Windows.Win32.Storage.Nvme.NVME_LOG_PAGES = 5
NVME_LOG_PAGE_DEVICE_SELF_TEST: win32more.Windows.Win32.Storage.Nvme.NVME_LOG_PAGES = 6
NVME_LOG_PAGE_TELEMETRY_HOST_INITIATED: win32more.Windows.Win32.Storage.Nvme.NVME_LOG_PAGES = 7
NVME_LOG_PAGE_TELEMETRY_CTLR_INITIATED: win32more.Windows.Win32.Storage.Nvme.NVME_LOG_PAGES = 8
NVME_LOG_PAGE_ENDURANCE_GROUP_INFORMATION: win32more.Windows.Win32.Storage.Nvme.NVME_LOG_PAGES = 9
NVME_LOG_PAGE_PREDICTABLE_LATENCY_NVM_SET: win32more.Windows.Win32.Storage.Nvme.NVME_LOG_PAGES = 10
NVME_LOG_PAGE_PREDICTABLE_LATENCY_EVENT_AGGREGATE: win32more.Windows.Win32.Storage.Nvme.NVME_LOG_PAGES = 11
NVME_LOG_PAGE_ASYMMETRIC_NAMESPACE_ACCESS: win32more.Windows.Win32.Storage.Nvme.NVME_LOG_PAGES = 12
NVME_LOG_PAGE_PERSISTENT_EVENT_LOG: win32more.Windows.Win32.Storage.Nvme.NVME_LOG_PAGES = 13
NVME_LOG_PAGE_LBA_STATUS_INFORMATION: win32more.Windows.Win32.Storage.Nvme.NVME_LOG_PAGES = 14
NVME_LOG_PAGE_ENDURANCE_GROUP_EVENT_AGGREGATE: win32more.Windows.Win32.Storage.Nvme.NVME_LOG_PAGES = 15
NVME_LOG_PAGE_RESERVATION_NOTIFICATION: win32more.Windows.Win32.Storage.Nvme.NVME_LOG_PAGES = 128
NVME_LOG_PAGE_SANITIZE_STATUS: win32more.Windows.Win32.Storage.Nvme.NVME_LOG_PAGES = 129
NVME_LOG_PAGE_CHANGED_ZONE_LIST: win32more.Windows.Win32.Storage.Nvme.NVME_LOG_PAGES = 191
NVME_NAMESPACE_METADATA_ELEMENT_TYPES = Int32
NVME_NAMESPACE_METADATA_OPERATING_SYSTEM_NAMESPACE_NAME: win32more.Windows.Win32.Storage.Nvme.NVME_NAMESPACE_METADATA_ELEMENT_TYPES = 1
NVME_NAMESPACE_METADATA_PREBOOT_NAMESPACE_NAME: win32more.Windows.Win32.Storage.Nvme.NVME_NAMESPACE_METADATA_ELEMENT_TYPES = 2
NVME_NAMESPACE_METADATA_OPERATING_SYSTEM_NAMESPACE_NAME_QUALIFIER_1: win32more.Windows.Win32.Storage.Nvme.NVME_NAMESPACE_METADATA_ELEMENT_TYPES = 3
NVME_NAMESPACE_METADATA_OPERATING_SYSTEM_NAMESPACE_NAME_QUALIFIER_2: win32more.Windows.Win32.Storage.Nvme.NVME_NAMESPACE_METADATA_ELEMENT_TYPES = 4
NVME_NO_DEALLOCATE_MODIFIES_MEDIA_AFTER_SANITIZE = Int32
NVME_MEDIA_ADDITIONALLY_MODIFIED_AFTER_SANITIZE_NOT_DEFINED: win32more.Windows.Win32.Storage.Nvme.NVME_NO_DEALLOCATE_MODIFIES_MEDIA_AFTER_SANITIZE = 0
NVME_MEDIA_NOT_ADDITIONALLY_MODIFIED_AFTER_SANITIZE: win32more.Windows.Win32.Storage.Nvme.NVME_NO_DEALLOCATE_MODIFIES_MEDIA_AFTER_SANITIZE = 1
NVME_MEDIA_ADDITIONALLY_MOFIDIED_AFTER_SANITIZE: win32more.Windows.Win32.Storage.Nvme.NVME_NO_DEALLOCATE_MODIFIES_MEDIA_AFTER_SANITIZE = 2
NVME_NVM_COMMANDS = Int32
NVME_NVM_COMMAND_FLUSH: win32more.Windows.Win32.Storage.Nvme.NVME_NVM_COMMANDS = 0
NVME_NVM_COMMAND_WRITE: win32more.Windows.Win32.Storage.Nvme.NVME_NVM_COMMANDS = 1
NVME_NVM_COMMAND_READ: win32more.Windows.Win32.Storage.Nvme.NVME_NVM_COMMANDS = 2
NVME_NVM_COMMAND_WRITE_UNCORRECTABLE: win32more.Windows.Win32.Storage.Nvme.NVME_NVM_COMMANDS = 4
NVME_NVM_COMMAND_COMPARE: win32more.Windows.Win32.Storage.Nvme.NVME_NVM_COMMANDS = 5
NVME_NVM_COMMAND_WRITE_ZEROES: win32more.Windows.Win32.Storage.Nvme.NVME_NVM_COMMANDS = 8
NVME_NVM_COMMAND_DATASET_MANAGEMENT: win32more.Windows.Win32.Storage.Nvme.NVME_NVM_COMMANDS = 9
NVME_NVM_COMMAND_VERIFY: win32more.Windows.Win32.Storage.Nvme.NVME_NVM_COMMANDS = 12
NVME_NVM_COMMAND_RESERVATION_REGISTER: win32more.Windows.Win32.Storage.Nvme.NVME_NVM_COMMANDS = 13
NVME_NVM_COMMAND_RESERVATION_REPORT: win32more.Windows.Win32.Storage.Nvme.NVME_NVM_COMMANDS = 14
NVME_NVM_COMMAND_RESERVATION_ACQUIRE: win32more.Windows.Win32.Storage.Nvme.NVME_NVM_COMMANDS = 17
NVME_NVM_COMMAND_RESERVATION_RELEASE: win32more.Windows.Win32.Storage.Nvme.NVME_NVM_COMMANDS = 21
NVME_NVM_COMMAND_COPY: win32more.Windows.Win32.Storage.Nvme.NVME_NVM_COMMANDS = 25
NVME_NVM_COMMAND_ZONE_MANAGEMENT_SEND: win32more.Windows.Win32.Storage.Nvme.NVME_NVM_COMMANDS = 121
NVME_NVM_COMMAND_ZONE_MANAGEMENT_RECEIVE: win32more.Windows.Win32.Storage.Nvme.NVME_NVM_COMMANDS = 122
NVME_NVM_COMMAND_ZONE_APPEND: win32more.Windows.Win32.Storage.Nvme.NVME_NVM_COMMANDS = 125
NVME_NVM_QUEUE_PRIORITIES = Int32
NVME_NVM_QUEUE_PRIORITY_URGENT: win32more.Windows.Win32.Storage.Nvme.NVME_NVM_QUEUE_PRIORITIES = 0
NVME_NVM_QUEUE_PRIORITY_HIGH: win32more.Windows.Win32.Storage.Nvme.NVME_NVM_QUEUE_PRIORITIES = 1
NVME_NVM_QUEUE_PRIORITY_MEDIUM: win32more.Windows.Win32.Storage.Nvme.NVME_NVM_QUEUE_PRIORITIES = 2
NVME_NVM_QUEUE_PRIORITY_LOW: win32more.Windows.Win32.Storage.Nvme.NVME_NVM_QUEUE_PRIORITIES = 3
class NVME_NVM_SUBSYSTEM_RESET(Structure):
    NSSRC: UInt32
class NVME_OCP_DEVICE_CAPABILITIES_LOG(Structure):
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
    class _OobMgmtSupport_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        AsUshort: UInt16
        _pack_ = 1
        class _Anonymous_e__Struct(Structure):
            MctpOverSMBusSupported: Annotated[UInt16, 1]
            MctpOverPcieVDMSupported: Annotated[UInt16, 1]
            BasicMgmtCommandSupported: Annotated[UInt16, 1]
            Reserved: Annotated[UInt16, 12]
            CompliesWithSpec: Annotated[UInt16, 1]
            _pack_ = 1
    class _WriteZeroesCommand_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        AsUshort: UInt16
        _pack_ = 1
        class _Anonymous_e__Struct(Structure):
            Supported: Annotated[UInt16, 1]
            DEACBitSupported: Annotated[UInt16, 1]
            FUABitSupported: Annotated[UInt16, 1]
            NvmeIo5Met: Annotated[UInt16, 1]
            NvmeIo6Met: Annotated[UInt16, 1]
            Reserved: Annotated[UInt16, 10]
            CompliesWithSpec: Annotated[UInt16, 1]
            _pack_ = 1
    class _SanitizeCommand_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        AsUshort: UInt16
        _pack_ = 1
        class _Anonymous_e__Struct(Structure):
            Supported: Annotated[UInt16, 1]
            CryptoEraseSupported: Annotated[UInt16, 1]
            BlockEraseSupported: Annotated[UInt16, 1]
            OverwriteSupported: Annotated[UInt16, 1]
            DeallocateLbaSupported: Annotated[UInt16, 1]
            Reserved: Annotated[UInt16, 10]
            CompliesWithSpec: Annotated[UInt16, 1]
            _pack_ = 1
    class _DatasetMgmtCommand_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        AsUshort: UInt16
        _pack_ = 1
        class _Anonymous_e__Struct(Structure):
            Supported: Annotated[UInt16, 1]
            AttribDeallocateSupported: Annotated[UInt16, 1]
            Reserved: Annotated[UInt16, 13]
            CompliesWithSpec: Annotated[UInt16, 1]
            _pack_ = 1
    class _WriteUncorrectableCommand_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        AsUshort: UInt16
        _pack_ = 1
        class _Anonymous_e__Struct(Structure):
            Supported: Annotated[UInt16, 1]
            SingleLBASupported: Annotated[UInt16, 1]
            MaxLBASupported: Annotated[UInt16, 1]
            NvmeIo14Met: Annotated[UInt16, 1]
            Reserved: Annotated[UInt16, 11]
            CompliesWithSpec: Annotated[UInt16, 1]
            _pack_ = 1
    class _FusedCommand_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        AsUshort: UInt16
        _pack_ = 1
        class _Anonymous_e__Struct(Structure):
            CWFusedSupported: Annotated[UInt16, 1]
            Reserved: Annotated[UInt16, 14]
            CompliesWithSpec: Annotated[UInt16, 1]
            _pack_ = 1
class NVME_OCP_DEVICE_ERROR_RECOVERY_LOG_V2(Structure):
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
class NVME_OCP_DEVICE_FIRMWARE_ACTIVATION_HISTORY_LOG(Structure):
    LID: Byte
    Reserved0: Byte * 3
    ValidNumberOfEntries: UInt32
    Entries: win32more.Windows.Win32.Storage.Nvme.FIRMWARE_ACTIVATION_HISTORY_ENTRY * 20
    Reserved1: Byte * 2790
    LogPageVersionNumber: UInt16
    LogPageGUID: Guid
    _pack_ = 1
class NVME_OCP_DEVICE_LATENCY_MONITOR_LOG(Structure):
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
    class _DebugLogStampUnits_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        AsUchar: Byte
        class _Anonymous_e__Struct(Structure):
            BasedOnTimestamp: Annotated[Byte, 1]
            Reserved: Annotated[Byte, 7]
class NVME_OCP_DEVICE_SMART_INFORMATION_LOG_V3(Structure):
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
    class _BadUserNANDBlockCount_e__Struct(Structure):
        RawCount: Byte * 6
        Normalized: Byte * 2
    class _BadSystemNANDBlockCount_e__Struct(Structure):
        RawCount: Byte * 6
        Normalized: Byte * 2
    class _EndToEndCorrectionCounts_e__Struct(Structure):
        DetectedCounts: UInt32
        CorrectedCounts: UInt32
        _pack_ = 1
    class _UserDataEraseCounts_e__Struct(Structure):
        MaximumCount: UInt32
        MinimumCount: UInt32
        _pack_ = 1
    class _ThermalThrottling_e__Struct(Structure):
        EventCount: Byte
        Status: Byte
class NVME_OCP_DEVICE_TCG_CONFIGURATION_LOG(Structure):
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
    class _State_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        AsUchar: Byte
        class _Anonymous_e__Struct(Structure):
            CPINSIDValue: Annotated[Byte, 1]
            CPINSIDBlocked: Annotated[Byte, 1]
            LockingEnabled: Annotated[Byte, 1]
            SUMOwner: Annotated[Byte, 1]
            Reserved: Annotated[Byte, 4]
class NVME_OCP_DEVICE_TCG_HISTORY_LOG(Structure):
    LID: Byte
    Reserved0: Byte * 3
    HistoryEntryCount: UInt32
    HistoryEntries: win32more.Windows.Win32.Storage.Nvme.TCG_HISTORY_ENTRY * 84
    Reserved1: Byte * 38
    LogPageVersionNumber: UInt16
    LogPageGUID: Guid
    _pack_ = 1
class NVME_OCP_DEVICE_UNSUPPORTED_REQUIREMENTS_LOG(Structure):
    UnsupportedCount: UInt16
    Reserved0: Byte * 14
    UnsupportedReqList: win32more.Windows.Win32.Storage.Nvme.UNSUPPORTED_REQUIREMENT * 253
    Reserved1: Byte * 14
    LogPageVersionNumber: UInt16
    LogPageGUID: Guid
    _pack_ = 1
class NVME_PERSISTENT_EVENT_LOG_EVENT_HEADER(Structure):
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
NVME_PERSISTENT_EVENT_TYPE_RESERVED0: win32more.Windows.Win32.Storage.Nvme.NVME_PERSISTENT_EVENT_LOG_EVENT_TYPES = 0
NVME_PERSISTENT_EVENT_TYPE_SMART_HEALTH_LOG_SNAPSHOT: win32more.Windows.Win32.Storage.Nvme.NVME_PERSISTENT_EVENT_LOG_EVENT_TYPES = 1
NVME_PERSISTENT_EVENT_TYPE_FIRMWARE_COMMIT: win32more.Windows.Win32.Storage.Nvme.NVME_PERSISTENT_EVENT_LOG_EVENT_TYPES = 2
NVME_PERSISTENT_EVENT_TYPE_TIMESTAMP_CHANGE: win32more.Windows.Win32.Storage.Nvme.NVME_PERSISTENT_EVENT_LOG_EVENT_TYPES = 3
NVME_PERSISTENT_EVENT_TYPE_POWER_ON_OR_RESET: win32more.Windows.Win32.Storage.Nvme.NVME_PERSISTENT_EVENT_LOG_EVENT_TYPES = 4
NVME_PERSISTENT_EVENT_TYPE_NVM_SUBSYSTEM_HARDWARE_ERROR: win32more.Windows.Win32.Storage.Nvme.NVME_PERSISTENT_EVENT_LOG_EVENT_TYPES = 5
NVME_PERSISTENT_EVENT_TYPE_CHANGE_NAMESPACE: win32more.Windows.Win32.Storage.Nvme.NVME_PERSISTENT_EVENT_LOG_EVENT_TYPES = 6
NVME_PERSISTENT_EVENT_TYPE_FORMAT_NVM_START: win32more.Windows.Win32.Storage.Nvme.NVME_PERSISTENT_EVENT_LOG_EVENT_TYPES = 7
NVME_PERSISTENT_EVENT_TYPE_FORMAT_NVM_COMPLETION: win32more.Windows.Win32.Storage.Nvme.NVME_PERSISTENT_EVENT_LOG_EVENT_TYPES = 8
NVME_PERSISTENT_EVENT_TYPE_SANITIZE_START: win32more.Windows.Win32.Storage.Nvme.NVME_PERSISTENT_EVENT_LOG_EVENT_TYPES = 9
NVME_PERSISTENT_EVENT_TYPE_SANITIZE_COMPLETION: win32more.Windows.Win32.Storage.Nvme.NVME_PERSISTENT_EVENT_LOG_EVENT_TYPES = 10
NVME_PERSISTENT_EVENT_TYPE_SET_FEATURE: win32more.Windows.Win32.Storage.Nvme.NVME_PERSISTENT_EVENT_LOG_EVENT_TYPES = 11
NVME_PERSISTENT_EVENT_TYPE_TELEMETRY_LOG_CREATED: win32more.Windows.Win32.Storage.Nvme.NVME_PERSISTENT_EVENT_LOG_EVENT_TYPES = 12
NVME_PERSISTENT_EVENT_TYPE_THERMAL_EXCURSION: win32more.Windows.Win32.Storage.Nvme.NVME_PERSISTENT_EVENT_LOG_EVENT_TYPES = 13
NVME_PERSISTENT_EVENT_TYPE_RESERVED1_BEGIN: win32more.Windows.Win32.Storage.Nvme.NVME_PERSISTENT_EVENT_LOG_EVENT_TYPES = 14
NVME_PERSISTENT_EVENT_TYPE_RESERVED1_END: win32more.Windows.Win32.Storage.Nvme.NVME_PERSISTENT_EVENT_LOG_EVENT_TYPES = 221
NVME_PERSISTENT_EVENT_TYPE_VENDOR_SPECIFIC_EVENT: win32more.Windows.Win32.Storage.Nvme.NVME_PERSISTENT_EVENT_LOG_EVENT_TYPES = 222
NVME_PERSISTENT_EVENT_TYPE_TCG_DEFINED: win32more.Windows.Win32.Storage.Nvme.NVME_PERSISTENT_EVENT_LOG_EVENT_TYPES = 223
NVME_PERSISTENT_EVENT_TYPE_RESERVED2_BEGIN: win32more.Windows.Win32.Storage.Nvme.NVME_PERSISTENT_EVENT_LOG_EVENT_TYPES = 224
NVME_PERSISTENT_EVENT_TYPE_RESERVED2_END: win32more.Windows.Win32.Storage.Nvme.NVME_PERSISTENT_EVENT_LOG_EVENT_TYPES = 255
NVME_PERSISTENT_EVENT_TYPE_MAX: win32more.Windows.Win32.Storage.Nvme.NVME_PERSISTENT_EVENT_LOG_EVENT_TYPES = 255
class NVME_PERSISTENT_EVENT_LOG_HEADER(Structure):
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
class NVME_POWER_STATE_DESC(Structure):
    MP: UInt16
    Reserved0: Byte
    MPS: Annotated[Byte, 1]
    NOPS: Annotated[Byte, 1]
    Reserved1: Annotated[Byte, 6]
    ENLAT: UInt32
    EXLAT: UInt32
    RRT: Annotated[Byte, 5]
    Reserved2: Annotated[Byte, 3]
    RRL: Annotated[Byte, 5]
    Reserved3: Annotated[Byte, 3]
    RWT: Annotated[Byte, 5]
    Reserved4: Annotated[Byte, 3]
    RWL: Annotated[Byte, 5]
    Reserved5: Annotated[Byte, 3]
    IDLP: UInt16
    Reserved6: Annotated[Byte, 6]
    IPS: Annotated[Byte, 2]
    Reserved7: Byte
    ACTP: UInt16
    APW: Annotated[Byte, 3]
    Reserved8: Annotated[Byte, 3]
    APS: Annotated[Byte, 2]
    Reserved9: Byte * 9
NVME_PROTECTION_INFORMATION_TYPES = Int32
NVME_PROTECTION_INFORMATION_NOT_ENABLED: win32more.Windows.Win32.Storage.Nvme.NVME_PROTECTION_INFORMATION_TYPES = 0
NVME_PROTECTION_INFORMATION_TYPE1: win32more.Windows.Win32.Storage.Nvme.NVME_PROTECTION_INFORMATION_TYPES = 1
NVME_PROTECTION_INFORMATION_TYPE2: win32more.Windows.Win32.Storage.Nvme.NVME_PROTECTION_INFORMATION_TYPES = 2
NVME_PROTECTION_INFORMATION_TYPE3: win32more.Windows.Win32.Storage.Nvme.NVME_PROTECTION_INFORMATION_TYPES = 3
class NVME_PRP_ENTRY(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlonglong: UInt64
    class _Anonymous_e__Struct(Structure):
        Reserved0: Annotated[UInt64, 2]
        PBAO: Annotated[UInt64, 62]
class NVME_REGISTERED_CONTROLLER_DATA(Structure):
    CNTLID: UInt16
    RCSTS: _RCSTS_e__Struct
    Reserved: Byte * 5
    HOSTID: Byte * 8
    RKEY: UInt64
    class _RCSTS_e__Struct(Structure):
        HoldReservation: Annotated[Byte, 1]
        Reserved: Annotated[Byte, 7]
class NVME_REGISTERED_CONTROLLER_EXTENDED_DATA(Structure):
    CNTLID: UInt16
    RCSTS: _RCSTS_e__Struct
    Reserved: Byte * 5
    RKEY: UInt64
    HOSTID: Byte * 16
    Reserved1: Byte * 32
    class _RCSTS_e__Struct(Structure):
        HoldReservation: Annotated[Byte, 1]
        Reserved: Annotated[Byte, 7]
class NVME_REPORT_ZONE_INFO(Structure):
    ZoneCount: UInt64
    Reserved: UInt64 * 7
    ZoneDescriptor: win32more.Windows.Win32.Storage.Nvme.NVME_ZONE_DESCRIPTOR * 1
NVME_RESERVATION_ACQUIRE_ACTIONS = Int32
NVME_RESERVATION_ACQUIRE_ACTION_ACQUIRE: win32more.Windows.Win32.Storage.Nvme.NVME_RESERVATION_ACQUIRE_ACTIONS = 0
NVME_RESERVATION_ACQUIRE_ACTION_PREEMPT: win32more.Windows.Win32.Storage.Nvme.NVME_RESERVATION_ACQUIRE_ACTIONS = 1
NVME_RESERVATION_ACQUIRE_ACTION_PREEMPT_AND_ABORT: win32more.Windows.Win32.Storage.Nvme.NVME_RESERVATION_ACQUIRE_ACTIONS = 2
class NVME_RESERVATION_ACQUIRE_DATA_STRUCTURE(Structure):
    CRKEY: UInt64
    PRKEY: UInt64
class NVME_RESERVATION_NOTIFICATION_LOG(Structure):
    LogPageCount: UInt64
    LogPageType: Byte
    AvailableLogPageCount: Byte
    Reserved0: Byte * 2
    NameSpaceId: UInt32
    Reserved1: Byte * 48
NVME_RESERVATION_NOTIFICATION_TYPES = Int32
NVME_RESERVATION_NOTIFICATION_TYPE_EMPTY_LOG_PAGE: win32more.Windows.Win32.Storage.Nvme.NVME_RESERVATION_NOTIFICATION_TYPES = 0
NVME_RESERVATION_NOTIFICATION_TYPE_REGISTRATION_PREEMPTED: win32more.Windows.Win32.Storage.Nvme.NVME_RESERVATION_NOTIFICATION_TYPES = 1
NVME_RESERVATION_NOTIFICATION_TYPE_REGISTRATION_RELEASED: win32more.Windows.Win32.Storage.Nvme.NVME_RESERVATION_NOTIFICATION_TYPES = 2
NVME_RESERVATION_NOTIFICATION_TYPE_RESERVATION_PREEPMPTED: win32more.Windows.Win32.Storage.Nvme.NVME_RESERVATION_NOTIFICATION_TYPES = 3
NVME_RESERVATION_REGISTER_ACTIONS = Int32
NVME_RESERVATION_REGISTER_ACTION_REGISTER: win32more.Windows.Win32.Storage.Nvme.NVME_RESERVATION_REGISTER_ACTIONS = 0
NVME_RESERVATION_REGISTER_ACTION_UNREGISTER: win32more.Windows.Win32.Storage.Nvme.NVME_RESERVATION_REGISTER_ACTIONS = 1
NVME_RESERVATION_REGISTER_ACTION_REPLACE: win32more.Windows.Win32.Storage.Nvme.NVME_RESERVATION_REGISTER_ACTIONS = 2
class NVME_RESERVATION_REGISTER_DATA_STRUCTURE(Structure):
    CRKEY: UInt64
    NRKEY: UInt64
NVME_RESERVATION_REGISTER_PTPL_STATE_CHANGES = Int32
NVME_RESERVATION_REGISTER_PTPL_STATE_NO_CHANGE: win32more.Windows.Win32.Storage.Nvme.NVME_RESERVATION_REGISTER_PTPL_STATE_CHANGES = 0
NVME_RESERVATION_REGISTER_PTPL_STATE_RESERVED: win32more.Windows.Win32.Storage.Nvme.NVME_RESERVATION_REGISTER_PTPL_STATE_CHANGES = 1
NVME_RESERVATION_REGISTER_PTPL_STATE_SET_TO_0: win32more.Windows.Win32.Storage.Nvme.NVME_RESERVATION_REGISTER_PTPL_STATE_CHANGES = 2
NVME_RESERVATION_REGISTER_PTPL_STATE_SET_TO_1: win32more.Windows.Win32.Storage.Nvme.NVME_RESERVATION_REGISTER_PTPL_STATE_CHANGES = 3
NVME_RESERVATION_RELEASE_ACTIONS = Int32
NVME_RESERVATION_RELEASE_ACTION_RELEASE: win32more.Windows.Win32.Storage.Nvme.NVME_RESERVATION_RELEASE_ACTIONS = 0
NVME_RESERVATION_RELEASE_ACTION_CLEAR: win32more.Windows.Win32.Storage.Nvme.NVME_RESERVATION_RELEASE_ACTIONS = 1
class NVME_RESERVATION_RELEASE_DATA_STRUCTURE(Structure):
    CRKEY: UInt64
class NVME_RESERVATION_REPORT_STATUS_DATA_STRUCTURE(Structure):
    Header: win32more.Windows.Win32.Storage.Nvme.NVME_RESERVATION_REPORT_STATUS_HEADER
    RegisteredControllersData: win32more.Windows.Win32.Storage.Nvme.NVME_REGISTERED_CONTROLLER_DATA * 1
class NVME_RESERVATION_REPORT_STATUS_EXTENDED_DATA_STRUCTURE(Structure):
    Header: win32more.Windows.Win32.Storage.Nvme.NVME_RESERVATION_REPORT_STATUS_HEADER
    Reserved1: Byte * 40
    RegisteredControllersExtendedData: win32more.Windows.Win32.Storage.Nvme.NVME_REGISTERED_CONTROLLER_EXTENDED_DATA * 1
class NVME_RESERVATION_REPORT_STATUS_HEADER(Structure):
    GEN: UInt32
    RTYPE: Byte
    REGCTL: UInt16
    Reserved: Byte * 2
    PTPLS: Byte
    Reserved1: Byte * 14
    _pack_ = 1
NVME_RESERVATION_TYPES = Int32
NVME_RESERVATION_TYPE_RESERVED: win32more.Windows.Win32.Storage.Nvme.NVME_RESERVATION_TYPES = 0
NVME_RESERVATION_TYPE_WRITE_EXCLUSIVE: win32more.Windows.Win32.Storage.Nvme.NVME_RESERVATION_TYPES = 1
NVME_RESERVATION_TYPE_EXCLUSIVE_ACCESS: win32more.Windows.Win32.Storage.Nvme.NVME_RESERVATION_TYPES = 2
NVME_RESERVATION_TYPE_WRITE_EXCLUSIVE_REGISTRANTS_ONLY: win32more.Windows.Win32.Storage.Nvme.NVME_RESERVATION_TYPES = 3
NVME_RESERVATION_TYPE_EXCLUSIVE_ACCESS_REGISTRANTS_ONLY: win32more.Windows.Win32.Storage.Nvme.NVME_RESERVATION_TYPES = 4
NVME_RESERVATION_TYPE_WRITE_EXCLUSIVE_ALL_REGISTRANTS: win32more.Windows.Win32.Storage.Nvme.NVME_RESERVATION_TYPES = 5
NVME_RESERVATION_TYPE_EXCLUSIVE_ACCESS_ALL_REGISTRANTS: win32more.Windows.Win32.Storage.Nvme.NVME_RESERVATION_TYPES = 6
NVME_SANITIZE_ACTION = Int32
NVME_SANITIZE_ACTION_RESERVED: win32more.Windows.Win32.Storage.Nvme.NVME_SANITIZE_ACTION = 0
NVME_SANITIZE_ACTION_EXIT_FAILURE_MODE: win32more.Windows.Win32.Storage.Nvme.NVME_SANITIZE_ACTION = 1
NVME_SANITIZE_ACTION_START_BLOCK_ERASE_SANITIZE: win32more.Windows.Win32.Storage.Nvme.NVME_SANITIZE_ACTION = 2
NVME_SANITIZE_ACTION_START_OVERWRITE_SANITIZE: win32more.Windows.Win32.Storage.Nvme.NVME_SANITIZE_ACTION = 3
NVME_SANITIZE_ACTION_START_CRYPTO_ERASE_SANITIZE: win32more.Windows.Win32.Storage.Nvme.NVME_SANITIZE_ACTION = 4
NVME_SANITIZE_OPERATION_STATUS = Int32
NVME_SANITIZE_OPERATION_NONE: win32more.Windows.Win32.Storage.Nvme.NVME_SANITIZE_OPERATION_STATUS = 0
NVME_SANITIZE_OPERATION_SUCCEEDED: win32more.Windows.Win32.Storage.Nvme.NVME_SANITIZE_OPERATION_STATUS = 1
NVME_SANITIZE_OPERATION_IN_PROGRESS: win32more.Windows.Win32.Storage.Nvme.NVME_SANITIZE_OPERATION_STATUS = 2
NVME_SANITIZE_OPERATION_FAILED: win32more.Windows.Win32.Storage.Nvme.NVME_SANITIZE_OPERATION_STATUS = 3
NVME_SANITIZE_OPERATION_SUCCEEDED_WITH_FORCED_DEALLOCATION: win32more.Windows.Win32.Storage.Nvme.NVME_SANITIZE_OPERATION_STATUS = 4
class NVME_SANITIZE_STATUS(Structure):
    MostRecentSanitizeOperationStatus: Annotated[UInt16, 3]
    NumberCompletedPassesOfOverwrite: Annotated[UInt16, 4]
    GlobalDataErased: Annotated[UInt16, 1]
    Reserved: Annotated[UInt16, 8]
class NVME_SANITIZE_STATUS_LOG(Structure):
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
class NVME_SCSI_NAME_STRING(Structure):
    PCIVendorID: win32more.Windows.Win32.Foundation.CHAR * 4
    ModelNumber: win32more.Windows.Win32.Foundation.CHAR * 40
    NamespaceID: win32more.Windows.Win32.Foundation.CHAR * 4
    SerialNumber: win32more.Windows.Win32.Foundation.CHAR * 20
NVME_SECURE_ERASE_SETTINGS = Int32
NVME_SECURE_ERASE_NONE: win32more.Windows.Win32.Storage.Nvme.NVME_SECURE_ERASE_SETTINGS = 0
NVME_SECURE_ERASE_USER_DATA: win32more.Windows.Win32.Storage.Nvme.NVME_SECURE_ERASE_SETTINGS = 1
NVME_SECURE_ERASE_CRYPTOGRAPHIC: win32more.Windows.Win32.Storage.Nvme.NVME_SECURE_ERASE_SETTINGS = 2
class NVME_SET_ATTRIBUTES_ENTRY(Structure):
    Identifier: UInt16
    ENDGID: UInt16
    Reserved1: UInt32
    Random4KBReadTypical: UInt32
    OptimalWriteSize: UInt32
    TotalCapacity: Byte * 16
    UnallocatedCapacity: Byte * 16
    Reserved2: Byte * 80
NVME_STATUS_COMMAND_SPECIFIC_CODES = Int32
NVME_STATUS_COMPLETION_QUEUE_INVALID: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 0
NVME_STATUS_INVALID_QUEUE_IDENTIFIER: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 1
NVME_STATUS_MAX_QUEUE_SIZE_EXCEEDED: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 2
NVME_STATUS_ABORT_COMMAND_LIMIT_EXCEEDED: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 3
NVME_STATUS_ASYNC_EVENT_REQUEST_LIMIT_EXCEEDED: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 5
NVME_STATUS_INVALID_FIRMWARE_SLOT: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 6
NVME_STATUS_INVALID_FIRMWARE_IMAGE: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 7
NVME_STATUS_INVALID_INTERRUPT_VECTOR: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 8
NVME_STATUS_INVALID_LOG_PAGE: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 9
NVME_STATUS_INVALID_FORMAT: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 10
NVME_STATUS_FIRMWARE_ACTIVATION_REQUIRES_CONVENTIONAL_RESET: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 11
NVME_STATUS_INVALID_QUEUE_DELETION: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 12
NVME_STATUS_FEATURE_ID_NOT_SAVEABLE: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 13
NVME_STATUS_FEATURE_NOT_CHANGEABLE: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 14
NVME_STATUS_FEATURE_NOT_NAMESPACE_SPECIFIC: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 15
NVME_STATUS_FIRMWARE_ACTIVATION_REQUIRES_NVM_SUBSYSTEM_RESET: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 16
NVME_STATUS_FIRMWARE_ACTIVATION_REQUIRES_RESET: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 17
NVME_STATUS_FIRMWARE_ACTIVATION_REQUIRES_MAX_TIME_VIOLATION: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 18
NVME_STATUS_FIRMWARE_ACTIVATION_PROHIBITED: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 19
NVME_STATUS_OVERLAPPING_RANGE: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 20
NVME_STATUS_NAMESPACE_INSUFFICIENT_CAPACITY: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 21
NVME_STATUS_NAMESPACE_IDENTIFIER_UNAVAILABLE: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 22
NVME_STATUS_NAMESPACE_ALREADY_ATTACHED: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 24
NVME_STATUS_NAMESPACE_IS_PRIVATE: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 25
NVME_STATUS_NAMESPACE_NOT_ATTACHED: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 26
NVME_STATUS_NAMESPACE_THIN_PROVISIONING_NOT_SUPPORTED: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 27
NVME_STATUS_CONTROLLER_LIST_INVALID: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 28
NVME_STATUS_DEVICE_SELF_TEST_IN_PROGRESS: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 29
NVME_STATUS_BOOT_PARTITION_WRITE_PROHIBITED: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 30
NVME_STATUS_INVALID_CONTROLLER_IDENTIFIER: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 31
NVME_STATUS_INVALID_SECONDARY_CONTROLLER_STATE: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 32
NVME_STATUS_INVALID_NUMBER_OF_CONTROLLER_RESOURCES: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 33
NVME_STATUS_INVALID_RESOURCE_IDENTIFIER: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 34
NVME_STATUS_SANITIZE_PROHIBITED_ON_PERSISTENT_MEMORY: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 35
NVME_STATUS_INVALID_ANA_GROUP_IDENTIFIER: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 36
NVME_STATUS_ANA_ATTACH_FAILED: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 37
NVME_IO_COMMAND_SET_NOT_SUPPORTED: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 41
NVME_IO_COMMAND_SET_NOT_ENABLED: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 42
NVME_IO_COMMAND_SET_COMBINATION_REJECTED: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 43
NVME_IO_COMMAND_SET_INVALID: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 44
NVME_STATUS_STREAM_RESOURCE_ALLOCATION_FAILED: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 127
NVME_STATUS_ZONE_INVALID_FORMAT: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 127
NVME_STATUS_NVM_CONFLICTING_ATTRIBUTES: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 128
NVME_STATUS_NVM_INVALID_PROTECTION_INFORMATION: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 129
NVME_STATUS_NVM_ATTEMPTED_WRITE_TO_READ_ONLY_RANGE: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 130
NVME_STATUS_NVM_COMMAND_SIZE_LIMIT_EXCEEDED: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 131
NVME_STATUS_ZONE_BOUNDARY_ERROR: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 184
NVME_STATUS_ZONE_FULL: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 185
NVME_STATUS_ZONE_READ_ONLY: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 186
NVME_STATUS_ZONE_OFFLINE: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 187
NVME_STATUS_ZONE_INVALID_WRITE: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 188
NVME_STATUS_ZONE_TOO_MANY_ACTIVE: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 189
NVME_STATUS_ZONE_TOO_MANY_OPEN: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 190
NVME_STATUS_ZONE_INVALID_STATE_TRANSITION: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_COMMAND_SPECIFIC_CODES = 191
NVME_STATUS_GENERIC_COMMAND_CODES = Int32
NVME_STATUS_SUCCESS_COMPLETION: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_GENERIC_COMMAND_CODES = 0
NVME_STATUS_INVALID_COMMAND_OPCODE: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_GENERIC_COMMAND_CODES = 1
NVME_STATUS_INVALID_FIELD_IN_COMMAND: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_GENERIC_COMMAND_CODES = 2
NVME_STATUS_COMMAND_ID_CONFLICT: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_GENERIC_COMMAND_CODES = 3
NVME_STATUS_DATA_TRANSFER_ERROR: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_GENERIC_COMMAND_CODES = 4
NVME_STATUS_COMMAND_ABORTED_DUE_TO_POWER_LOSS_NOTIFICATION: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_GENERIC_COMMAND_CODES = 5
NVME_STATUS_INTERNAL_DEVICE_ERROR: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_GENERIC_COMMAND_CODES = 6
NVME_STATUS_COMMAND_ABORT_REQUESTED: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_GENERIC_COMMAND_CODES = 7
NVME_STATUS_COMMAND_ABORTED_DUE_TO_SQ_DELETION: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_GENERIC_COMMAND_CODES = 8
NVME_STATUS_COMMAND_ABORTED_DUE_TO_FAILED_FUSED_COMMAND: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_GENERIC_COMMAND_CODES = 9
NVME_STATUS_COMMAND_ABORTED_DUE_TO_FAILED_MISSING_COMMAND: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_GENERIC_COMMAND_CODES = 10
NVME_STATUS_INVALID_NAMESPACE_OR_FORMAT: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_GENERIC_COMMAND_CODES = 11
NVME_STATUS_COMMAND_SEQUENCE_ERROR: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_GENERIC_COMMAND_CODES = 12
NVME_STATUS_INVALID_SGL_LAST_SEGMENT_DESCR: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_GENERIC_COMMAND_CODES = 13
NVME_STATUS_INVALID_NUMBER_OF_SGL_DESCR: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_GENERIC_COMMAND_CODES = 14
NVME_STATUS_DATA_SGL_LENGTH_INVALID: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_GENERIC_COMMAND_CODES = 15
NVME_STATUS_METADATA_SGL_LENGTH_INVALID: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_GENERIC_COMMAND_CODES = 16
NVME_STATUS_SGL_DESCR_TYPE_INVALID: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_GENERIC_COMMAND_CODES = 17
NVME_STATUS_INVALID_USE_OF_CONTROLLER_MEMORY_BUFFER: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_GENERIC_COMMAND_CODES = 18
NVME_STATUS_PRP_OFFSET_INVALID: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_GENERIC_COMMAND_CODES = 19
NVME_STATUS_ATOMIC_WRITE_UNIT_EXCEEDED: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_GENERIC_COMMAND_CODES = 20
NVME_STATUS_OPERATION_DENIED: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_GENERIC_COMMAND_CODES = 21
NVME_STATUS_SGL_OFFSET_INVALID: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_GENERIC_COMMAND_CODES = 22
NVME_STATUS_RESERVED: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_GENERIC_COMMAND_CODES = 23
NVME_STATUS_HOST_IDENTIFIER_INCONSISTENT_FORMAT: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_GENERIC_COMMAND_CODES = 24
NVME_STATUS_KEEP_ALIVE_TIMEOUT_EXPIRED: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_GENERIC_COMMAND_CODES = 25
NVME_STATUS_KEEP_ALIVE_TIMEOUT_INVALID: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_GENERIC_COMMAND_CODES = 26
NVME_STATUS_COMMAND_ABORTED_DUE_TO_PREEMPT_ABORT: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_GENERIC_COMMAND_CODES = 27
NVME_STATUS_SANITIZE_FAILED: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_GENERIC_COMMAND_CODES = 28
NVME_STATUS_SANITIZE_IN_PROGRESS: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_GENERIC_COMMAND_CODES = 29
NVME_STATUS_SGL_DATA_BLOCK_GRANULARITY_INVALID: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_GENERIC_COMMAND_CODES = 30
NVME_STATUS_DIRECTIVE_TYPE_INVALID: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_GENERIC_COMMAND_CODES = 112
NVME_STATUS_DIRECTIVE_ID_INVALID: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_GENERIC_COMMAND_CODES = 113
NVME_STATUS_NVM_LBA_OUT_OF_RANGE: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_GENERIC_COMMAND_CODES = 128
NVME_STATUS_NVM_CAPACITY_EXCEEDED: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_GENERIC_COMMAND_CODES = 129
NVME_STATUS_NVM_NAMESPACE_NOT_READY: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_GENERIC_COMMAND_CODES = 130
NVME_STATUS_NVM_RESERVATION_CONFLICT: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_GENERIC_COMMAND_CODES = 131
NVME_STATUS_FORMAT_IN_PROGRESS: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_GENERIC_COMMAND_CODES = 132
NVME_STATUS_MEDIA_ERROR_CODES = Int32
NVME_STATUS_NVM_WRITE_FAULT: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_MEDIA_ERROR_CODES = 128
NVME_STATUS_NVM_UNRECOVERED_READ_ERROR: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_MEDIA_ERROR_CODES = 129
NVME_STATUS_NVM_END_TO_END_GUARD_CHECK_ERROR: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_MEDIA_ERROR_CODES = 130
NVME_STATUS_NVM_END_TO_END_APPLICATION_TAG_CHECK_ERROR: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_MEDIA_ERROR_CODES = 131
NVME_STATUS_NVM_END_TO_END_REFERENCE_TAG_CHECK_ERROR: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_MEDIA_ERROR_CODES = 132
NVME_STATUS_NVM_COMPARE_FAILURE: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_MEDIA_ERROR_CODES = 133
NVME_STATUS_NVM_ACCESS_DENIED: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_MEDIA_ERROR_CODES = 134
NVME_STATUS_NVM_DEALLOCATED_OR_UNWRITTEN_LOGICAL_BLOCK: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_MEDIA_ERROR_CODES = 135
NVME_STATUS_TYPES = Int32
NVME_STATUS_TYPE_GENERIC_COMMAND: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_TYPES = 0
NVME_STATUS_TYPE_COMMAND_SPECIFIC: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_TYPES = 1
NVME_STATUS_TYPE_MEDIA_ERROR: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_TYPES = 2
NVME_STATUS_TYPE_VENDOR_SPECIFIC: win32more.Windows.Win32.Storage.Nvme.NVME_STATUS_TYPES = 7
class NVME_SUBMISSION_QUEUE_TAIL_DOORBELL(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        SQT: Annotated[UInt32, 16]
        Reserved0: Annotated[UInt32, 16]
class NVME_TELEMETRY_CONTROLLER_INITIATED_LOG(Structure):
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
class NVME_TELEMETRY_HOST_INITIATED_LOG(Structure):
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
NVME_TEMPERATURE_OVER_THRESHOLD: win32more.Windows.Win32.Storage.Nvme.NVME_TEMPERATURE_THRESHOLD_TYPES = 0
NVME_TEMPERATURE_UNDER_THRESHOLD: win32more.Windows.Win32.Storage.Nvme.NVME_TEMPERATURE_THRESHOLD_TYPES = 1
NVME_VENDOR_LOG_PAGES = Int32
NVME_LOG_PAGE_OCP_DEVICE_SMART_INFORMATION: win32more.Windows.Win32.Storage.Nvme.NVME_VENDOR_LOG_PAGES = 192
NVME_LOG_PAGE_OCP_DEVICE_ERROR_RECOVERY: win32more.Windows.Win32.Storage.Nvme.NVME_VENDOR_LOG_PAGES = 193
NVME_LOG_PAGE_OCP_FIRMWARE_ACTIVATION_HISTORY: win32more.Windows.Win32.Storage.Nvme.NVME_VENDOR_LOG_PAGES = 194
NVME_LOG_PAGE_OCP_LATENCY_MONITOR: win32more.Windows.Win32.Storage.Nvme.NVME_VENDOR_LOG_PAGES = 195
NVME_LOG_PAGE_OCP_DEVICE_CAPABILITIES: win32more.Windows.Win32.Storage.Nvme.NVME_VENDOR_LOG_PAGES = 196
NVME_LOG_PAGE_OCP_UNSUPPORTED_REQUIREMENTS: win32more.Windows.Win32.Storage.Nvme.NVME_VENDOR_LOG_PAGES = 197
NVME_LOG_PAGE_OCP_TCG_CONFIGURATION: win32more.Windows.Win32.Storage.Nvme.NVME_VENDOR_LOG_PAGES = 200
NVME_LOG_PAGE_OCP_TCG_HISTORY: win32more.Windows.Win32.Storage.Nvme.NVME_VENDOR_LOG_PAGES = 201
class NVME_VERSION(Union):
    Anonymous: _Anonymous_e__Struct
    AsUlong: UInt32
    class _Anonymous_e__Struct(Structure):
        TER: Annotated[UInt32, 8]
        MNR: Annotated[UInt32, 8]
        MJR: Annotated[UInt32, 16]
class NVME_WCS_DEVICE_CAPABILITIES(Structure):
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        AsULONG: UInt32
        class _Anonymous_e__Struct(Structure):
            PanicAEN: Annotated[UInt32, 1]
            PanicCFS: Annotated[UInt32, 1]
            Reserved: Annotated[UInt32, 30]
class NVME_WCS_DEVICE_ERROR_RECOVERY_LOG(Structure):
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
NVMeDeviceRecoveryNoAction: win32more.Windows.Win32.Storage.Nvme.NVME_WCS_DEVICE_RECOVERY_ACTION1 = 0
NVMeDeviceRecoveryFormatNVM: win32more.Windows.Win32.Storage.Nvme.NVME_WCS_DEVICE_RECOVERY_ACTION1 = 1
NVMeDeviceRecoveryVendorSpecificCommand: win32more.Windows.Win32.Storage.Nvme.NVME_WCS_DEVICE_RECOVERY_ACTION1 = 2
NVMeDeviceRecoveryVendorAnalysis: win32more.Windows.Win32.Storage.Nvme.NVME_WCS_DEVICE_RECOVERY_ACTION1 = 3
NVMeDeviceRecoveryDeviceReplacement: win32more.Windows.Win32.Storage.Nvme.NVME_WCS_DEVICE_RECOVERY_ACTION1 = 4
NVMeDeviceRecoverySanitize: win32more.Windows.Win32.Storage.Nvme.NVME_WCS_DEVICE_RECOVERY_ACTION1 = 5
NVMeDeviceRecovery1Max: win32more.Windows.Win32.Storage.Nvme.NVME_WCS_DEVICE_RECOVERY_ACTION1 = 15
NVME_WCS_DEVICE_RECOVERY_ACTION2 = Int32
NVMeDeviceRecoveryControllerReset: win32more.Windows.Win32.Storage.Nvme.NVME_WCS_DEVICE_RECOVERY_ACTION2 = 0
NVMeDeviceRecoverySubsystemReset: win32more.Windows.Win32.Storage.Nvme.NVME_WCS_DEVICE_RECOVERY_ACTION2 = 1
NVMeDeviceRecoveryPcieFunctionReset: win32more.Windows.Win32.Storage.Nvme.NVME_WCS_DEVICE_RECOVERY_ACTION2 = 2
NVMeDeviceRecoveryPERST: win32more.Windows.Win32.Storage.Nvme.NVME_WCS_DEVICE_RECOVERY_ACTION2 = 3
NVMeDeviceRecoveryPowerCycle: win32more.Windows.Win32.Storage.Nvme.NVME_WCS_DEVICE_RECOVERY_ACTION2 = 4
NVMeDeviceRecoveryPcieHotReset: win32more.Windows.Win32.Storage.Nvme.NVME_WCS_DEVICE_RECOVERY_ACTION2 = 5
NVMeDeviceRecovery2Max: win32more.Windows.Win32.Storage.Nvme.NVME_WCS_DEVICE_RECOVERY_ACTION2 = 15
class NVME_WCS_DEVICE_RESET_ACTION(Structure):
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        AsUCHAR: Byte
        class _Anonymous_e__Struct(Structure):
            ControllerReset: Annotated[Byte, 1]
            NVMeSubsystemReset: Annotated[Byte, 1]
            PCIeFLR: Annotated[Byte, 1]
            PERST: Annotated[Byte, 1]
            PowerCycle: Annotated[Byte, 1]
            PCIeConventionalHotReset: Annotated[Byte, 1]
            Reserved: Annotated[Byte, 2]
class NVME_WCS_DEVICE_SMART_ATTRIBUTES_LOG(Structure):
    VersionSpecificData: Byte * 494
    LogPageVersionNumber: UInt16
    LogPageGUID: Guid
    _pack_ = 1
class NVME_WCS_DEVICE_SMART_ATTRIBUTES_LOG_V2(Structure):
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
    class _BadUserNANDBlockCount_e__Struct(Structure):
        RawCount: Byte * 6
        Normalized: Byte * 2
    class _BadSystemNANDBlockCount_e__Struct(Structure):
        RawCount: Byte * 6
        Normalized: Byte * 2
    class _EndToEndCorrectionCounts_e__Struct(Structure):
        DetectedCounts: UInt32
        CorrectedCounts: UInt32
        _pack_ = 1
    class _UserDataEraseCounts_e__Struct(Structure):
        MaximumCount: UInt32
        MinimumCount: UInt32
        _pack_ = 1
    class _ThermalThrottling_e__Struct(Structure):
        EventCount: Byte
        Status: Byte
class NVME_ZONE_DESCRIPTOR(Structure):
    Anonymous1: _Anonymous1_e__Struct
    Anonymous2: _Anonymous2_e__Struct
    ZA: _ZA_e__Struct
    Reserved3: Byte * 5
    ZCAP: UInt64
    ZSLBA: UInt64
    WritePointer: UInt64
    Reserved4: Byte * 32
    class _Anonymous1_e__Struct(Structure):
        ZT: Annotated[Byte, 4]
        Reserved1: Annotated[Byte, 4]
    class _Anonymous2_e__Struct(Structure):
        Reserved2: Annotated[Byte, 4]
        ZS: Annotated[Byte, 4]
    class _ZA_e__Struct(Structure):
        ZFC: Annotated[Byte, 1]
        FZR: Annotated[Byte, 1]
        RZR: Annotated[Byte, 1]
        Reserved: Annotated[Byte, 4]
        ZDEV: Annotated[Byte, 1]
class NVME_ZONE_DESCRIPTOR_EXTENSION(Structure):
    ZoneDescriptorExtensionInfo: Byte * 64
class NVME_ZONE_EXTENDED_REPORT_ZONE_DESC(Structure):
    ZoneDescriptor: win32more.Windows.Win32.Storage.Nvme.NVME_ZONE_DESCRIPTOR
    ZoneDescriptorExtension: win32more.Windows.Win32.Storage.Nvme.NVME_ZONE_DESCRIPTOR_EXTENSION * 1
NVME_ZONE_RECEIVE_ACTION = Int32
NVME_ZONE_RECEIVE_REPORT_ZONES: win32more.Windows.Win32.Storage.Nvme.NVME_ZONE_RECEIVE_ACTION = 0
NVME_ZONE_RECEIVE_EXTENDED_REPORT_ZONES: win32more.Windows.Win32.Storage.Nvme.NVME_ZONE_RECEIVE_ACTION = 1
NVME_ZONE_RECEIVE_ACTION_SPECIFIC = Int32
NVME_ZRA_ALL_ZONES: win32more.Windows.Win32.Storage.Nvme.NVME_ZONE_RECEIVE_ACTION_SPECIFIC = 0
NVME_ZRA_EMPTY_STATE_ZONES: win32more.Windows.Win32.Storage.Nvme.NVME_ZONE_RECEIVE_ACTION_SPECIFIC = 1
NVME_ZRA_IO_STATE_ZONES: win32more.Windows.Win32.Storage.Nvme.NVME_ZONE_RECEIVE_ACTION_SPECIFIC = 2
NVME_ZRA_EO_STATE_ZONES: win32more.Windows.Win32.Storage.Nvme.NVME_ZONE_RECEIVE_ACTION_SPECIFIC = 3
NVME_ZRA_CLOSED_STATE_ZONES: win32more.Windows.Win32.Storage.Nvme.NVME_ZONE_RECEIVE_ACTION_SPECIFIC = 4
NVME_ZRA_FULL_STATE_ZONES: win32more.Windows.Win32.Storage.Nvme.NVME_ZONE_RECEIVE_ACTION_SPECIFIC = 5
NVME_ZRA_RO_STATE_ZONES: win32more.Windows.Win32.Storage.Nvme.NVME_ZONE_RECEIVE_ACTION_SPECIFIC = 6
NVME_ZRA_OFFLINE_STATE_ZONES: win32more.Windows.Win32.Storage.Nvme.NVME_ZONE_RECEIVE_ACTION_SPECIFIC = 7
NVME_ZONE_SEND_ACTION = Int32
NVME_ZONE_SEND_CLOSE: win32more.Windows.Win32.Storage.Nvme.NVME_ZONE_SEND_ACTION = 1
NVME_ZONE_SEND_FINISH: win32more.Windows.Win32.Storage.Nvme.NVME_ZONE_SEND_ACTION = 2
NVME_ZONE_SEND_OPEN: win32more.Windows.Win32.Storage.Nvme.NVME_ZONE_SEND_ACTION = 3
NVME_ZONE_SEND_RESET: win32more.Windows.Win32.Storage.Nvme.NVME_ZONE_SEND_ACTION = 4
NVME_ZONE_SEND_OFFLINE: win32more.Windows.Win32.Storage.Nvme.NVME_ZONE_SEND_ACTION = 5
NVME_ZONE_SEND_SET_ZONE_DESCRIPTOR: win32more.Windows.Win32.Storage.Nvme.NVME_ZONE_SEND_ACTION = 16
class NVM_RESERVATION_CAPABILITIES(Union):
    Anonymous: _Anonymous_e__Struct
    AsUchar: Byte
    class _Anonymous_e__Struct(Structure):
        PersistThroughPowerLoss: Annotated[Byte, 1]
        WriteExclusiveReservation: Annotated[Byte, 1]
        ExclusiveAccessReservation: Annotated[Byte, 1]
        WriteExclusiveRegistrantsOnlyReservation: Annotated[Byte, 1]
        ExclusiveAccessRegistrantsOnlyReservation: Annotated[Byte, 1]
        WriteExclusiveAllRegistrantsReservation: Annotated[Byte, 1]
        ExclusiveAccessAllRegistrantsReservation: Annotated[Byte, 1]
        Reserved: Annotated[Byte, 1]
class NVM_SET_LIST(Structure):
    IdentifierCount: Byte
    Reserved: Byte * 127
    Entry: win32more.Windows.Win32.Storage.Nvme.NVME_SET_ATTRIBUTES_ENTRY * 1
class TCG_ACTIVATE_METHOD_SPECIFIC(Structure):
    RangeStartLengthPolicy: Byte
class TCG_ASSIGN_METHOD_SPECIFIC(Structure):
    NamespaceId: UInt32
    _pack_ = 1
class TCG_AUTH_METHOD_SPECIFIC(Structure):
    AuthorityId: UInt64
    TriesCount: Byte
    _pack_ = 1
class TCG_BLOCKSID_METHOD_SPECIFIC(Structure):
    ClearEvents: Byte
class TCG_HISTORY_ENTRY(Structure):
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
class TCG_REACTIVATE_METHOD_SPECIFIC(Structure):
    RangeStartLengthPolicy: Byte
class UNSUPPORTED_REQUIREMENT(Structure):
    ReqId: Byte * 16
ZONE_STATE = Int32
NVME_STATE_ZSE: win32more.Windows.Win32.Storage.Nvme.ZONE_STATE = 1
NVME_STATE_ZSIO: win32more.Windows.Win32.Storage.Nvme.ZONE_STATE = 2
NVME_STATE_ZSEO: win32more.Windows.Win32.Storage.Nvme.ZONE_STATE = 3
NVME_STATE_ZSC: win32more.Windows.Win32.Storage.Nvme.ZONE_STATE = 4
NVME_STATE_ZSRO: win32more.Windows.Win32.Storage.Nvme.ZONE_STATE = 13
NVME_STATE_ZSF: win32more.Windows.Win32.Storage.Nvme.ZONE_STATE = 14
NVME_STATE_ZSO: win32more.Windows.Win32.Storage.Nvme.ZONE_STATE = 15


make_ready(__name__)
