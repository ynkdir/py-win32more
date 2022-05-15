from win32more import *
import win32more.Storage.IscsiDisc
import win32more.Foundation
import win32more.System.Ioctl

def __getattr__(name):
    if f"_define_{name}" not in globals():
        raise AttributeError()
    setattr(win32more.Storage.IscsiDisc, name, globals()[f"_define_{name}"]())
    return getattr(win32more.Storage.IscsiDisc, name)
def __dir__():
    return __all__
IOCTL_SCSI_BASE = 4
ScsiRawInterfaceGuid = '53f56309-b6bf-11d0-94f2-00a0c91efb8b'
WmiScsiAddressGuid = '53f5630f-b6bf-11d0-94f2-00a0c91efb8b'
FILE_DEVICE_SCSI = 27
IOCTL_SCSI_PASS_THROUGH = 315396
IOCTL_SCSI_MINIPORT = 315400
IOCTL_SCSI_GET_INQUIRY_DATA = 266252
IOCTL_SCSI_GET_CAPABILITIES = 266256
IOCTL_SCSI_PASS_THROUGH_DIRECT = 315412
IOCTL_SCSI_GET_ADDRESS = 266264
IOCTL_SCSI_RESCAN_BUS = 266268
IOCTL_SCSI_GET_DUMP_POINTERS = 266272
IOCTL_SCSI_FREE_DUMP_POINTERS = 266276
IOCTL_IDE_PASS_THROUGH = 315432
IOCTL_ATA_PASS_THROUGH = 315436
IOCTL_ATA_PASS_THROUGH_DIRECT = 315440
IOCTL_ATA_MINIPORT = 315444
IOCTL_MINIPORT_PROCESS_SERVICE_IRP = 315448
IOCTL_MPIO_PASS_THROUGH_PATH = 315452
IOCTL_MPIO_PASS_THROUGH_PATH_DIRECT = 315456
IOCTL_SCSI_PASS_THROUGH_EX = 315460
IOCTL_SCSI_PASS_THROUGH_DIRECT_EX = 315464
IOCTL_MPIO_PASS_THROUGH_PATH_EX = 315468
IOCTL_MPIO_PASS_THROUGH_PATH_DIRECT_EX = 315472
ATA_FLAGS_DRDY_REQUIRED = 1
ATA_FLAGS_DATA_IN = 2
ATA_FLAGS_DATA_OUT = 4
ATA_FLAGS_48BIT_COMMAND = 8
ATA_FLAGS_USE_DMA = 16
ATA_FLAGS_NO_MULTIPLE = 32
NRB_FUNCTION_NVCACHE_INFO = 236
NRB_FUNCTION_SPINDLE_STATUS = 229
NRB_FUNCTION_NVCACHE_POWER_MODE_SET = 0
NRB_FUNCTION_NVCACHE_POWER_MODE_RETURN = 1
NRB_FUNCTION_FLUSH_NVCACHE = 20
NRB_FUNCTION_QUERY_PINNED_SET = 18
NRB_FUNCTION_QUERY_CACHE_MISS = 19
NRB_FUNCTION_ADD_LBAS_PINNED_SET = 16
NRB_FUNCTION_REMOVE_LBAS_PINNED_SET = 17
NRB_FUNCTION_QUERY_ASCENDER_STATUS = 208
NRB_FUNCTION_QUERY_HYBRID_DISK_STATUS = 209
NRB_FUNCTION_PASS_HINT_PAYLOAD = 224
NRB_FUNCTION_NVSEPARATED_INFO = 192
NRB_FUNCTION_NVSEPARATED_FLUSH = 193
NRB_FUNCTION_NVSEPARATED_WB_DISABLE = 194
NRB_FUNCTION_NVSEPARATED_WB_REVERT_DEFAULT = 195
NRB_SUCCESS = 0
NRB_ILLEGAL_REQUEST = 1
NRB_INVALID_PARAMETER = 2
NRB_INPUT_DATA_OVERRUN = 3
NRB_INPUT_DATA_UNDERRUN = 4
NRB_OUTPUT_DATA_OVERRUN = 5
NRB_OUTPUT_DATA_UNDERRUN = 6
NV_SEP_CACHE_PARAMETER_VERSION_1 = 1
NV_SEP_CACHE_PARAMETER_VERSION = 1
STORAGE_DIAGNOSTIC_STATUS_SUCCESS = 0
STORAGE_DIAGNOSTIC_STATUS_BUFFER_TOO_SMALL = 1
STORAGE_DIAGNOSTIC_STATUS_UNSUPPORTED_VERSION = 2
STORAGE_DIAGNOSTIC_STATUS_INVALID_PARAMETER = 3
STORAGE_DIAGNOSTIC_STATUS_INVALID_SIGNATURE = 4
STORAGE_DIAGNOSTIC_STATUS_INVALID_TARGET_TYPE = 5
STORAGE_DIAGNOSTIC_STATUS_MORE_DATA = 6
MINIPORT_DSM_NOTIFICATION_VERSION_1 = 1
MINIPORT_DSM_NOTIFICATION_VERSION = 1
MINIPORT_DSM_PROFILE_UNKNOWN = 0
MINIPORT_DSM_PROFILE_PAGE_FILE = 1
MINIPORT_DSM_PROFILE_HIBERNATION_FILE = 2
MINIPORT_DSM_PROFILE_CRASHDUMP_FILE = 3
MINIPORT_DSM_NOTIFY_FLAG_BEGIN = 1
MINIPORT_DSM_NOTIFY_FLAG_END = 2
HYBRID_FUNCTION_GET_INFO = 1
HYBRID_FUNCTION_DISABLE_CACHING_MEDIUM = 16
HYBRID_FUNCTION_ENABLE_CACHING_MEDIUM = 17
HYBRID_FUNCTION_SET_DIRTY_THRESHOLD = 18
HYBRID_FUNCTION_DEMOTE_BY_SIZE = 19
HYBRID_STATUS_SUCCESS = 0
HYBRID_STATUS_ILLEGAL_REQUEST = 1
HYBRID_STATUS_INVALID_PARAMETER = 2
HYBRID_STATUS_OUTPUT_BUFFER_TOO_SMALL = 3
HYBRID_STATUS_ENABLE_REFCOUNT_HOLD = 16
HYBRID_REQUEST_BLOCK_STRUCTURE_VERSION = 1
HYBRID_REQUEST_INFO_STRUCTURE_VERSION = 1
FIRMWARE_FUNCTION_GET_INFO = 1
FIRMWARE_FUNCTION_DOWNLOAD = 2
FIRMWARE_FUNCTION_ACTIVATE = 3
FIRMWARE_STATUS_SUCCESS = 0
FIRMWARE_STATUS_ERROR = 1
FIRMWARE_STATUS_ILLEGAL_REQUEST = 2
FIRMWARE_STATUS_INVALID_PARAMETER = 3
FIRMWARE_STATUS_INPUT_BUFFER_TOO_BIG = 4
FIRMWARE_STATUS_OUTPUT_BUFFER_TOO_SMALL = 5
FIRMWARE_STATUS_INVALID_SLOT = 6
FIRMWARE_STATUS_INVALID_IMAGE = 7
FIRMWARE_STATUS_CONTROLLER_ERROR = 16
FIRMWARE_STATUS_POWER_CYCLE_REQUIRED = 32
FIRMWARE_STATUS_DEVICE_ERROR = 64
FIRMWARE_STATUS_INTERFACE_CRC_ERROR = 128
FIRMWARE_STATUS_UNCORRECTABLE_DATA_ERROR = 129
FIRMWARE_STATUS_MEDIA_CHANGE = 130
FIRMWARE_STATUS_ID_NOT_FOUND = 131
FIRMWARE_STATUS_MEDIA_CHANGE_REQUEST = 132
FIRMWARE_STATUS_COMMAND_ABORT = 133
FIRMWARE_STATUS_END_OF_MEDIA = 134
FIRMWARE_STATUS_ILLEGAL_LENGTH = 135
FIRMWARE_REQUEST_BLOCK_STRUCTURE_VERSION = 1
FIRMWARE_REQUEST_FLAG_CONTROLLER = 1
FIRMWARE_REQUEST_FLAG_LAST_SEGMENT = 2
FIRMWARE_REQUEST_FLAG_FIRST_SEGMENT = 4
FIRMWARE_REQUEST_FLAG_SWITCH_TO_EXISTING_FIRMWARE = 2147483648
STORAGE_FIRMWARE_INFO_STRUCTURE_VERSION = 1
STORAGE_FIRMWARE_INFO_STRUCTURE_VERSION_V2 = 2
STORAGE_FIRMWARE_INFO_INVALID_SLOT = 255
STORAGE_FIRMWARE_SLOT_INFO_V2_REVISION_LENGTH = 16
STORAGE_FIRMWARE_DOWNLOAD_STRUCTURE_VERSION = 1
STORAGE_FIRMWARE_DOWNLOAD_STRUCTURE_VERSION_V2 = 2
STORAGE_FIRMWARE_ACTIVATE_STRUCTURE_VERSION = 1
DUMP_POINTERS_VERSION_1 = 1
DUMP_POINTERS_VERSION_2 = 2
DUMP_POINTERS_VERSION_3 = 3
DUMP_POINTERS_VERSION_4 = 4
DUMP_DRIVER_NAME_LENGTH = 15
DUMP_EX_FLAG_SUPPORT_64BITMEMORY = 1
DUMP_EX_FLAG_SUPPORT_DD_TELEMETRY = 2
DUMP_EX_FLAG_RESUME_SUPPORT = 4
DUMP_EX_FLAG_DRIVER_FULL_PATH_SUPPORT = 8
SCSI_IOCTL_DATA_OUT = 0
SCSI_IOCTL_DATA_IN = 1
SCSI_IOCTL_DATA_UNSPECIFIED = 2
SCSI_IOCTL_DATA_BIDIRECTIONAL = 3
MPIO_IOCTL_FLAG_USE_PATHID = 1
MPIO_IOCTL_FLAG_USE_SCSIADDRESS = 2
MPIO_IOCTL_FLAG_INVOLVE_DSM = 4
MAX_ISCSI_HBANAME_LEN = 256
MAX_ISCSI_NAME_LEN = 223
MAX_ISCSI_ALIAS_LEN = 255
MAX_ISCSI_PORTAL_NAME_LEN = 256
MAX_ISCSI_PORTAL_ALIAS_LEN = 256
MAX_ISCSI_TEXT_ADDRESS_LEN = 256
MAX_ISCSI_PORTAL_ADDRESS_LEN = 256
MAX_ISCSI_DISCOVERY_DOMAIN_LEN = 256
MAX_RADIUS_ADDRESS_LEN = 41
ISCSI_SECURITY_FLAG_TUNNEL_MODE_PREFERRED = 64
ISCSI_SECURITY_FLAG_TRANSPORT_MODE_PREFERRED = 32
ISCSI_SECURITY_FLAG_PFS_ENABLED = 16
ISCSI_SECURITY_FLAG_AGGRESSIVE_MODE_ENABLED = 8
ISCSI_SECURITY_FLAG_MAIN_MODE_ENABLED = 4
ISCSI_SECURITY_FLAG_IKE_IPSEC_ENABLED = 2
ISCSI_SECURITY_FLAG_VALID = 1
ISCSI_LOGIN_FLAG_REQUIRE_IPSEC = 1
ISCSI_LOGIN_FLAG_MULTIPATH_ENABLED = 2
ISCSI_LOGIN_FLAG_RESERVED1 = 4
ISCSI_LOGIN_FLAG_ALLOW_PORTAL_HOPPING = 8
ISCSI_LOGIN_FLAG_USE_RADIUS_RESPONSE = 16
ISCSI_LOGIN_FLAG_USE_RADIUS_VERIFICATION = 32
ISCSI_LOGIN_OPTIONS_HEADER_DIGEST = 1
ISCSI_LOGIN_OPTIONS_DATA_DIGEST = 2
ISCSI_LOGIN_OPTIONS_MAXIMUM_CONNECTIONS = 4
ISCSI_LOGIN_OPTIONS_DEFAULT_TIME_2_WAIT = 8
ISCSI_LOGIN_OPTIONS_DEFAULT_TIME_2_RETAIN = 16
ISCSI_LOGIN_OPTIONS_USERNAME = 32
ISCSI_LOGIN_OPTIONS_PASSWORD = 64
ISCSI_LOGIN_OPTIONS_AUTH_TYPE = 128
ISCSI_LOGIN_OPTIONS_VERSION = 0
ISCSI_TARGET_FLAG_HIDE_STATIC_TARGET = 2
ISCSI_TARGET_FLAG_MERGE_TARGET_INFORMATION = 4
ID_IPV4_ADDR = 1
ID_FQDN = 2
ID_USER_FQDN = 3
ID_IPV6_ADDR = 5
def _define__ADAPTER_OBJECT_head():
    class _ADAPTER_OBJECT(Structure):
        pass
    return _ADAPTER_OBJECT
def _define__ADAPTER_OBJECT():
    _ADAPTER_OBJECT = win32more.Storage.IscsiDisc._ADAPTER_OBJECT_head
    return _ADAPTER_OBJECT
def _define_SCSI_PASS_THROUGH_head():
    class SCSI_PASS_THROUGH(Structure):
        pass
    return SCSI_PASS_THROUGH
def _define_SCSI_PASS_THROUGH():
    SCSI_PASS_THROUGH = win32more.Storage.IscsiDisc.SCSI_PASS_THROUGH_head
    SCSI_PASS_THROUGH._fields_ = [
        ("Length", UInt16),
        ("ScsiStatus", Byte),
        ("PathId", Byte),
        ("TargetId", Byte),
        ("Lun", Byte),
        ("CdbLength", Byte),
        ("SenseInfoLength", Byte),
        ("DataIn", Byte),
        ("DataTransferLength", UInt32),
        ("TimeOutValue", UInt32),
        ("DataBufferOffset", UIntPtr),
        ("SenseInfoOffset", UInt32),
        ("Cdb", Byte * 16),
    ]
    return SCSI_PASS_THROUGH
def _define_SCSI_PASS_THROUGH_DIRECT_head():
    class SCSI_PASS_THROUGH_DIRECT(Structure):
        pass
    return SCSI_PASS_THROUGH_DIRECT
def _define_SCSI_PASS_THROUGH_DIRECT():
    SCSI_PASS_THROUGH_DIRECT = win32more.Storage.IscsiDisc.SCSI_PASS_THROUGH_DIRECT_head
    SCSI_PASS_THROUGH_DIRECT._fields_ = [
        ("Length", UInt16),
        ("ScsiStatus", Byte),
        ("PathId", Byte),
        ("TargetId", Byte),
        ("Lun", Byte),
        ("CdbLength", Byte),
        ("SenseInfoLength", Byte),
        ("DataIn", Byte),
        ("DataTransferLength", UInt32),
        ("TimeOutValue", UInt32),
        ("DataBuffer", c_void_p),
        ("SenseInfoOffset", UInt32),
        ("Cdb", Byte * 16),
    ]
    return SCSI_PASS_THROUGH_DIRECT
def _define_SCSI_PASS_THROUGH32_head():
    class SCSI_PASS_THROUGH32(Structure):
        pass
    return SCSI_PASS_THROUGH32
def _define_SCSI_PASS_THROUGH32():
    SCSI_PASS_THROUGH32 = win32more.Storage.IscsiDisc.SCSI_PASS_THROUGH32_head
    SCSI_PASS_THROUGH32._fields_ = [
        ("Length", UInt16),
        ("ScsiStatus", Byte),
        ("PathId", Byte),
        ("TargetId", Byte),
        ("Lun", Byte),
        ("CdbLength", Byte),
        ("SenseInfoLength", Byte),
        ("DataIn", Byte),
        ("DataTransferLength", UInt32),
        ("TimeOutValue", UInt32),
        ("DataBufferOffset", UInt32),
        ("SenseInfoOffset", UInt32),
        ("Cdb", Byte * 16),
    ]
    return SCSI_PASS_THROUGH32
def _define_SCSI_PASS_THROUGH_DIRECT32_head():
    class SCSI_PASS_THROUGH_DIRECT32(Structure):
        pass
    return SCSI_PASS_THROUGH_DIRECT32
def _define_SCSI_PASS_THROUGH_DIRECT32():
    SCSI_PASS_THROUGH_DIRECT32 = win32more.Storage.IscsiDisc.SCSI_PASS_THROUGH_DIRECT32_head
    SCSI_PASS_THROUGH_DIRECT32._fields_ = [
        ("Length", UInt16),
        ("ScsiStatus", Byte),
        ("PathId", Byte),
        ("TargetId", Byte),
        ("Lun", Byte),
        ("CdbLength", Byte),
        ("SenseInfoLength", Byte),
        ("DataIn", Byte),
        ("DataTransferLength", UInt32),
        ("TimeOutValue", UInt32),
        ("DataBuffer", c_void_p),
        ("SenseInfoOffset", UInt32),
        ("Cdb", Byte * 16),
    ]
    return SCSI_PASS_THROUGH_DIRECT32
def _define_SCSI_PASS_THROUGH_EX_head():
    class SCSI_PASS_THROUGH_EX(Structure):
        pass
    return SCSI_PASS_THROUGH_EX
def _define_SCSI_PASS_THROUGH_EX():
    SCSI_PASS_THROUGH_EX = win32more.Storage.IscsiDisc.SCSI_PASS_THROUGH_EX_head
    SCSI_PASS_THROUGH_EX._fields_ = [
        ("Version", UInt32),
        ("Length", UInt32),
        ("CdbLength", UInt32),
        ("StorAddressLength", UInt32),
        ("ScsiStatus", Byte),
        ("SenseInfoLength", Byte),
        ("DataDirection", Byte),
        ("Reserved", Byte),
        ("TimeOutValue", UInt32),
        ("StorAddressOffset", UInt32),
        ("SenseInfoOffset", UInt32),
        ("DataOutTransferLength", UInt32),
        ("DataInTransferLength", UInt32),
        ("DataOutBufferOffset", UIntPtr),
        ("DataInBufferOffset", UIntPtr),
        ("Cdb", Byte * 0),
    ]
    return SCSI_PASS_THROUGH_EX
def _define_SCSI_PASS_THROUGH_DIRECT_EX_head():
    class SCSI_PASS_THROUGH_DIRECT_EX(Structure):
        pass
    return SCSI_PASS_THROUGH_DIRECT_EX
def _define_SCSI_PASS_THROUGH_DIRECT_EX():
    SCSI_PASS_THROUGH_DIRECT_EX = win32more.Storage.IscsiDisc.SCSI_PASS_THROUGH_DIRECT_EX_head
    SCSI_PASS_THROUGH_DIRECT_EX._fields_ = [
        ("Version", UInt32),
        ("Length", UInt32),
        ("CdbLength", UInt32),
        ("StorAddressLength", UInt32),
        ("ScsiStatus", Byte),
        ("SenseInfoLength", Byte),
        ("DataDirection", Byte),
        ("Reserved", Byte),
        ("TimeOutValue", UInt32),
        ("StorAddressOffset", UInt32),
        ("SenseInfoOffset", UInt32),
        ("DataOutTransferLength", UInt32),
        ("DataInTransferLength", UInt32),
        ("DataOutBuffer", c_void_p),
        ("DataInBuffer", c_void_p),
        ("Cdb", Byte * 0),
    ]
    return SCSI_PASS_THROUGH_DIRECT_EX
def _define_SCSI_PASS_THROUGH32_EX_head():
    class SCSI_PASS_THROUGH32_EX(Structure):
        pass
    return SCSI_PASS_THROUGH32_EX
def _define_SCSI_PASS_THROUGH32_EX():
    SCSI_PASS_THROUGH32_EX = win32more.Storage.IscsiDisc.SCSI_PASS_THROUGH32_EX_head
    SCSI_PASS_THROUGH32_EX._fields_ = [
        ("Version", UInt32),
        ("Length", UInt32),
        ("CdbLength", UInt32),
        ("StorAddressLength", UInt32),
        ("ScsiStatus", Byte),
        ("SenseInfoLength", Byte),
        ("DataDirection", Byte),
        ("Reserved", Byte),
        ("TimeOutValue", UInt32),
        ("StorAddressOffset", UInt32),
        ("SenseInfoOffset", UInt32),
        ("DataOutTransferLength", UInt32),
        ("DataInTransferLength", UInt32),
        ("DataOutBufferOffset", UInt32),
        ("DataInBufferOffset", UInt32),
        ("Cdb", Byte * 0),
    ]
    return SCSI_PASS_THROUGH32_EX
def _define_SCSI_PASS_THROUGH_DIRECT32_EX_head():
    class SCSI_PASS_THROUGH_DIRECT32_EX(Structure):
        pass
    return SCSI_PASS_THROUGH_DIRECT32_EX
def _define_SCSI_PASS_THROUGH_DIRECT32_EX():
    SCSI_PASS_THROUGH_DIRECT32_EX = win32more.Storage.IscsiDisc.SCSI_PASS_THROUGH_DIRECT32_EX_head
    SCSI_PASS_THROUGH_DIRECT32_EX._fields_ = [
        ("Version", UInt32),
        ("Length", UInt32),
        ("CdbLength", UInt32),
        ("StorAddressLength", UInt32),
        ("ScsiStatus", Byte),
        ("SenseInfoLength", Byte),
        ("DataDirection", Byte),
        ("Reserved", Byte),
        ("TimeOutValue", UInt32),
        ("StorAddressOffset", UInt32),
        ("SenseInfoOffset", UInt32),
        ("DataOutTransferLength", UInt32),
        ("DataInTransferLength", UInt32),
        ("DataOutBuffer", c_void_p),
        ("DataInBuffer", c_void_p),
        ("Cdb", Byte * 0),
    ]
    return SCSI_PASS_THROUGH_DIRECT32_EX
def _define_ATA_PASS_THROUGH_EX_head():
    class ATA_PASS_THROUGH_EX(Structure):
        pass
    return ATA_PASS_THROUGH_EX
def _define_ATA_PASS_THROUGH_EX():
    ATA_PASS_THROUGH_EX = win32more.Storage.IscsiDisc.ATA_PASS_THROUGH_EX_head
    ATA_PASS_THROUGH_EX._fields_ = [
        ("Length", UInt16),
        ("AtaFlags", UInt16),
        ("PathId", Byte),
        ("TargetId", Byte),
        ("Lun", Byte),
        ("ReservedAsUchar", Byte),
        ("DataTransferLength", UInt32),
        ("TimeOutValue", UInt32),
        ("ReservedAsUlong", UInt32),
        ("DataBufferOffset", UIntPtr),
        ("PreviousTaskFile", Byte * 8),
        ("CurrentTaskFile", Byte * 8),
    ]
    return ATA_PASS_THROUGH_EX
def _define_ATA_PASS_THROUGH_DIRECT_head():
    class ATA_PASS_THROUGH_DIRECT(Structure):
        pass
    return ATA_PASS_THROUGH_DIRECT
def _define_ATA_PASS_THROUGH_DIRECT():
    ATA_PASS_THROUGH_DIRECT = win32more.Storage.IscsiDisc.ATA_PASS_THROUGH_DIRECT_head
    ATA_PASS_THROUGH_DIRECT._fields_ = [
        ("Length", UInt16),
        ("AtaFlags", UInt16),
        ("PathId", Byte),
        ("TargetId", Byte),
        ("Lun", Byte),
        ("ReservedAsUchar", Byte),
        ("DataTransferLength", UInt32),
        ("TimeOutValue", UInt32),
        ("ReservedAsUlong", UInt32),
        ("DataBuffer", c_void_p),
        ("PreviousTaskFile", Byte * 8),
        ("CurrentTaskFile", Byte * 8),
    ]
    return ATA_PASS_THROUGH_DIRECT
def _define_ATA_PASS_THROUGH_EX32_head():
    class ATA_PASS_THROUGH_EX32(Structure):
        pass
    return ATA_PASS_THROUGH_EX32
def _define_ATA_PASS_THROUGH_EX32():
    ATA_PASS_THROUGH_EX32 = win32more.Storage.IscsiDisc.ATA_PASS_THROUGH_EX32_head
    ATA_PASS_THROUGH_EX32._fields_ = [
        ("Length", UInt16),
        ("AtaFlags", UInt16),
        ("PathId", Byte),
        ("TargetId", Byte),
        ("Lun", Byte),
        ("ReservedAsUchar", Byte),
        ("DataTransferLength", UInt32),
        ("TimeOutValue", UInt32),
        ("ReservedAsUlong", UInt32),
        ("DataBufferOffset", UInt32),
        ("PreviousTaskFile", Byte * 8),
        ("CurrentTaskFile", Byte * 8),
    ]
    return ATA_PASS_THROUGH_EX32
def _define_ATA_PASS_THROUGH_DIRECT32_head():
    class ATA_PASS_THROUGH_DIRECT32(Structure):
        pass
    return ATA_PASS_THROUGH_DIRECT32
def _define_ATA_PASS_THROUGH_DIRECT32():
    ATA_PASS_THROUGH_DIRECT32 = win32more.Storage.IscsiDisc.ATA_PASS_THROUGH_DIRECT32_head
    ATA_PASS_THROUGH_DIRECT32._fields_ = [
        ("Length", UInt16),
        ("AtaFlags", UInt16),
        ("PathId", Byte),
        ("TargetId", Byte),
        ("Lun", Byte),
        ("ReservedAsUchar", Byte),
        ("DataTransferLength", UInt32),
        ("TimeOutValue", UInt32),
        ("ReservedAsUlong", UInt32),
        ("DataBuffer", c_void_p),
        ("PreviousTaskFile", Byte * 8),
        ("CurrentTaskFile", Byte * 8),
    ]
    return ATA_PASS_THROUGH_DIRECT32
def _define_IDE_IO_CONTROL_head():
    class IDE_IO_CONTROL(Structure):
        pass
    return IDE_IO_CONTROL
def _define_IDE_IO_CONTROL():
    IDE_IO_CONTROL = win32more.Storage.IscsiDisc.IDE_IO_CONTROL_head
    IDE_IO_CONTROL._fields_ = [
        ("HeaderLength", UInt32),
        ("Signature", Byte * 8),
        ("Timeout", UInt32),
        ("ControlCode", UInt32),
        ("ReturnStatus", UInt32),
        ("DataLength", UInt32),
    ]
    return IDE_IO_CONTROL
def _define_MPIO_PASS_THROUGH_PATH_head():
    class MPIO_PASS_THROUGH_PATH(Structure):
        pass
    return MPIO_PASS_THROUGH_PATH
def _define_MPIO_PASS_THROUGH_PATH():
    MPIO_PASS_THROUGH_PATH = win32more.Storage.IscsiDisc.MPIO_PASS_THROUGH_PATH_head
    MPIO_PASS_THROUGH_PATH._fields_ = [
        ("PassThrough", win32more.Storage.IscsiDisc.SCSI_PASS_THROUGH),
        ("Version", UInt32),
        ("Length", UInt16),
        ("Flags", Byte),
        ("PortNumber", Byte),
        ("MpioPathId", UInt64),
    ]
    return MPIO_PASS_THROUGH_PATH
def _define_MPIO_PASS_THROUGH_PATH_DIRECT_head():
    class MPIO_PASS_THROUGH_PATH_DIRECT(Structure):
        pass
    return MPIO_PASS_THROUGH_PATH_DIRECT
def _define_MPIO_PASS_THROUGH_PATH_DIRECT():
    MPIO_PASS_THROUGH_PATH_DIRECT = win32more.Storage.IscsiDisc.MPIO_PASS_THROUGH_PATH_DIRECT_head
    MPIO_PASS_THROUGH_PATH_DIRECT._fields_ = [
        ("PassThrough", win32more.Storage.IscsiDisc.SCSI_PASS_THROUGH_DIRECT),
        ("Version", UInt32),
        ("Length", UInt16),
        ("Flags", Byte),
        ("PortNumber", Byte),
        ("MpioPathId", UInt64),
    ]
    return MPIO_PASS_THROUGH_PATH_DIRECT
def _define_MPIO_PASS_THROUGH_PATH_EX_head():
    class MPIO_PASS_THROUGH_PATH_EX(Structure):
        pass
    return MPIO_PASS_THROUGH_PATH_EX
def _define_MPIO_PASS_THROUGH_PATH_EX():
    MPIO_PASS_THROUGH_PATH_EX = win32more.Storage.IscsiDisc.MPIO_PASS_THROUGH_PATH_EX_head
    MPIO_PASS_THROUGH_PATH_EX._fields_ = [
        ("PassThroughOffset", UInt32),
        ("Version", UInt32),
        ("Length", UInt16),
        ("Flags", Byte),
        ("PortNumber", Byte),
        ("MpioPathId", UInt64),
    ]
    return MPIO_PASS_THROUGH_PATH_EX
def _define_MPIO_PASS_THROUGH_PATH_DIRECT_EX_head():
    class MPIO_PASS_THROUGH_PATH_DIRECT_EX(Structure):
        pass
    return MPIO_PASS_THROUGH_PATH_DIRECT_EX
def _define_MPIO_PASS_THROUGH_PATH_DIRECT_EX():
    MPIO_PASS_THROUGH_PATH_DIRECT_EX = win32more.Storage.IscsiDisc.MPIO_PASS_THROUGH_PATH_DIRECT_EX_head
    MPIO_PASS_THROUGH_PATH_DIRECT_EX._fields_ = [
        ("PassThroughOffset", UInt32),
        ("Version", UInt32),
        ("Length", UInt16),
        ("Flags", Byte),
        ("PortNumber", Byte),
        ("MpioPathId", UInt64),
    ]
    return MPIO_PASS_THROUGH_PATH_DIRECT_EX
def _define_MPIO_PASS_THROUGH_PATH32_head():
    class MPIO_PASS_THROUGH_PATH32(Structure):
        pass
    return MPIO_PASS_THROUGH_PATH32
def _define_MPIO_PASS_THROUGH_PATH32():
    MPIO_PASS_THROUGH_PATH32 = win32more.Storage.IscsiDisc.MPIO_PASS_THROUGH_PATH32_head
    MPIO_PASS_THROUGH_PATH32._fields_ = [
        ("PassThrough", win32more.Storage.IscsiDisc.SCSI_PASS_THROUGH32),
        ("Version", UInt32),
        ("Length", UInt16),
        ("Flags", Byte),
        ("PortNumber", Byte),
        ("MpioPathId", UInt64),
    ]
    return MPIO_PASS_THROUGH_PATH32
def _define_MPIO_PASS_THROUGH_PATH_DIRECT32_head():
    class MPIO_PASS_THROUGH_PATH_DIRECT32(Structure):
        pass
    return MPIO_PASS_THROUGH_PATH_DIRECT32
def _define_MPIO_PASS_THROUGH_PATH_DIRECT32():
    MPIO_PASS_THROUGH_PATH_DIRECT32 = win32more.Storage.IscsiDisc.MPIO_PASS_THROUGH_PATH_DIRECT32_head
    MPIO_PASS_THROUGH_PATH_DIRECT32._fields_ = [
        ("PassThrough", win32more.Storage.IscsiDisc.SCSI_PASS_THROUGH_DIRECT32),
        ("Version", UInt32),
        ("Length", UInt16),
        ("Flags", Byte),
        ("PortNumber", Byte),
        ("MpioPathId", UInt64),
    ]
    return MPIO_PASS_THROUGH_PATH_DIRECT32
def _define_MPIO_PASS_THROUGH_PATH32_EX_head():
    class MPIO_PASS_THROUGH_PATH32_EX(Structure):
        pass
    return MPIO_PASS_THROUGH_PATH32_EX
def _define_MPIO_PASS_THROUGH_PATH32_EX():
    MPIO_PASS_THROUGH_PATH32_EX = win32more.Storage.IscsiDisc.MPIO_PASS_THROUGH_PATH32_EX_head
    MPIO_PASS_THROUGH_PATH32_EX._fields_ = [
        ("PassThroughOffset", UInt32),
        ("Version", UInt32),
        ("Length", UInt16),
        ("Flags", Byte),
        ("PortNumber", Byte),
        ("MpioPathId", UInt64),
    ]
    return MPIO_PASS_THROUGH_PATH32_EX
def _define_MPIO_PASS_THROUGH_PATH_DIRECT32_EX_head():
    class MPIO_PASS_THROUGH_PATH_DIRECT32_EX(Structure):
        pass
    return MPIO_PASS_THROUGH_PATH_DIRECT32_EX
def _define_MPIO_PASS_THROUGH_PATH_DIRECT32_EX():
    MPIO_PASS_THROUGH_PATH_DIRECT32_EX = win32more.Storage.IscsiDisc.MPIO_PASS_THROUGH_PATH_DIRECT32_EX_head
    MPIO_PASS_THROUGH_PATH_DIRECT32_EX._fields_ = [
        ("PassThroughOffset", UInt32),
        ("Version", UInt32),
        ("Length", UInt16),
        ("Flags", Byte),
        ("PortNumber", Byte),
        ("MpioPathId", UInt64),
    ]
    return MPIO_PASS_THROUGH_PATH_DIRECT32_EX
def _define_SCSI_BUS_DATA_head():
    class SCSI_BUS_DATA(Structure):
        pass
    return SCSI_BUS_DATA
def _define_SCSI_BUS_DATA():
    SCSI_BUS_DATA = win32more.Storage.IscsiDisc.SCSI_BUS_DATA_head
    SCSI_BUS_DATA._fields_ = [
        ("NumberOfLogicalUnits", Byte),
        ("InitiatorBusId", Byte),
        ("InquiryDataOffset", UInt32),
    ]
    return SCSI_BUS_DATA
def _define_SCSI_ADAPTER_BUS_INFO_head():
    class SCSI_ADAPTER_BUS_INFO(Structure):
        pass
    return SCSI_ADAPTER_BUS_INFO
def _define_SCSI_ADAPTER_BUS_INFO():
    SCSI_ADAPTER_BUS_INFO = win32more.Storage.IscsiDisc.SCSI_ADAPTER_BUS_INFO_head
    SCSI_ADAPTER_BUS_INFO._fields_ = [
        ("NumberOfBuses", Byte),
        ("BusData", win32more.Storage.IscsiDisc.SCSI_BUS_DATA * 0),
    ]
    return SCSI_ADAPTER_BUS_INFO
def _define_SCSI_INQUIRY_DATA_head():
    class SCSI_INQUIRY_DATA(Structure):
        pass
    return SCSI_INQUIRY_DATA
def _define_SCSI_INQUIRY_DATA():
    SCSI_INQUIRY_DATA = win32more.Storage.IscsiDisc.SCSI_INQUIRY_DATA_head
    SCSI_INQUIRY_DATA._fields_ = [
        ("PathId", Byte),
        ("TargetId", Byte),
        ("Lun", Byte),
        ("DeviceClaimed", win32more.Foundation.BOOLEAN),
        ("InquiryDataLength", UInt32),
        ("NextInquiryDataOffset", UInt32),
        ("InquiryData", Byte * 0),
    ]
    return SCSI_INQUIRY_DATA
def _define_SRB_IO_CONTROL_head():
    class SRB_IO_CONTROL(Structure):
        pass
    return SRB_IO_CONTROL
def _define_SRB_IO_CONTROL():
    SRB_IO_CONTROL = win32more.Storage.IscsiDisc.SRB_IO_CONTROL_head
    SRB_IO_CONTROL._fields_ = [
        ("HeaderLength", UInt32),
        ("Signature", Byte * 8),
        ("Timeout", UInt32),
        ("ControlCode", UInt32),
        ("ReturnCode", UInt32),
        ("Length", UInt32),
    ]
    return SRB_IO_CONTROL
def _define_NVCACHE_REQUEST_BLOCK_head():
    class NVCACHE_REQUEST_BLOCK(Structure):
        pass
    return NVCACHE_REQUEST_BLOCK
def _define_NVCACHE_REQUEST_BLOCK():
    NVCACHE_REQUEST_BLOCK = win32more.Storage.IscsiDisc.NVCACHE_REQUEST_BLOCK_head
    NVCACHE_REQUEST_BLOCK._fields_ = [
        ("NRBSize", UInt32),
        ("Function", UInt16),
        ("NRBFlags", UInt32),
        ("NRBStatus", UInt32),
        ("Count", UInt32),
        ("LBA", UInt64),
        ("DataBufSize", UInt32),
        ("NVCacheStatus", UInt32),
        ("NVCacheSubStatus", UInt32),
    ]
    return NVCACHE_REQUEST_BLOCK
def _define_NV_FEATURE_PARAMETER_head():
    class NV_FEATURE_PARAMETER(Structure):
        pass
    return NV_FEATURE_PARAMETER
def _define_NV_FEATURE_PARAMETER():
    NV_FEATURE_PARAMETER = win32more.Storage.IscsiDisc.NV_FEATURE_PARAMETER_head
    NV_FEATURE_PARAMETER._fields_ = [
        ("NVPowerModeEnabled", UInt16),
        ("NVParameterReserv1", UInt16),
        ("NVCmdEnabled", UInt16),
        ("NVParameterReserv2", UInt16),
        ("NVPowerModeVer", UInt16),
        ("NVCmdVer", UInt16),
        ("NVSize", UInt32),
        ("NVReadSpeed", UInt16),
        ("NVWrtSpeed", UInt16),
        ("DeviceSpinUpTime", UInt32),
    ]
    return NV_FEATURE_PARAMETER
def _define_NVCACHE_HINT_PAYLOAD_head():
    class NVCACHE_HINT_PAYLOAD(Structure):
        pass
    return NVCACHE_HINT_PAYLOAD
def _define_NVCACHE_HINT_PAYLOAD():
    NVCACHE_HINT_PAYLOAD = win32more.Storage.IscsiDisc.NVCACHE_HINT_PAYLOAD_head
    NVCACHE_HINT_PAYLOAD._fields_ = [
        ("Command", Byte),
        ("Feature7_0", Byte),
        ("Feature15_8", Byte),
        ("Count15_8", Byte),
        ("LBA7_0", Byte),
        ("LBA15_8", Byte),
        ("LBA23_16", Byte),
        ("LBA31_24", Byte),
        ("LBA39_32", Byte),
        ("LBA47_40", Byte),
        ("Auxiliary7_0", Byte),
        ("Auxiliary23_16", Byte),
        ("Reserved", Byte * 4),
    ]
    return NVCACHE_HINT_PAYLOAD
def _define_NV_SEP_CACHE_PARAMETER_head():
    class NV_SEP_CACHE_PARAMETER(Structure):
        pass
    return NV_SEP_CACHE_PARAMETER
def _define_NV_SEP_CACHE_PARAMETER():
    NV_SEP_CACHE_PARAMETER = win32more.Storage.IscsiDisc.NV_SEP_CACHE_PARAMETER_head
    class NV_SEP_CACHE_PARAMETER__Flags_e__Union(Union):
        pass
    class NV_SEP_CACHE_PARAMETER__Flags_e__Union__CacheFlags_e__Struct(Structure):
        pass
    NV_SEP_CACHE_PARAMETER__Flags_e__Union__CacheFlags_e__Struct._fields_ = [
        ("_bitfield", Byte),
    ]
    NV_SEP_CACHE_PARAMETER__Flags_e__Union._fields_ = [
        ("CacheFlags", NV_SEP_CACHE_PARAMETER__Flags_e__Union__CacheFlags_e__Struct),
        ("CacheFlagsSet", Byte),
    ]
    NV_SEP_CACHE_PARAMETER._fields_ = [
        ("Version", UInt32),
        ("Size", UInt32),
        ("Flags", NV_SEP_CACHE_PARAMETER__Flags_e__Union),
        ("WriteCacheType", Byte),
        ("WriteCacheTypeEffective", Byte),
        ("ParameterReserve1", Byte * 3),
    ]
    return NV_SEP_CACHE_PARAMETER
NV_SEP_WRITE_CACHE_TYPE = Int32
NV_SEP_WRITE_CACHE_TYPE_NVSEPWriteCacheTypeUnknown = 0
NV_SEP_WRITE_CACHE_TYPE_NVSEPWriteCacheTypeNone = 1
NV_SEP_WRITE_CACHE_TYPE_NVSEPWriteCacheTypeWriteBack = 2
NV_SEP_WRITE_CACHE_TYPE_NVSEPWriteCacheTypeWriteThrough = 3
MP_STORAGE_DIAGNOSTIC_LEVEL = Int32
MP_STORAGE_DIAGNOSTIC_LEVEL_MpStorageDiagnosticLevelDefault = 0
MP_STORAGE_DIAGNOSTIC_LEVEL_MpStorageDiagnosticLevelMax = 1
MP_STORAGE_DIAGNOSTIC_TARGET_TYPE = Int32
MP_STORAGE_DIAGNOSTIC_TARGET_TYPE_MpStorageDiagnosticTargetTypeUndefined = 0
MP_STORAGE_DIAGNOSTIC_TARGET_TYPE_MpStorageDiagnosticTargetTypeMiniport = 2
MP_STORAGE_DIAGNOSTIC_TARGET_TYPE_MpStorageDiagnosticTargetTypeHbaFirmware = 3
MP_STORAGE_DIAGNOSTIC_TARGET_TYPE_MpStorageDiagnosticTargetTypeMax = 4
def _define_STORAGE_DIAGNOSTIC_MP_REQUEST_head():
    class STORAGE_DIAGNOSTIC_MP_REQUEST(Structure):
        pass
    return STORAGE_DIAGNOSTIC_MP_REQUEST
def _define_STORAGE_DIAGNOSTIC_MP_REQUEST():
    STORAGE_DIAGNOSTIC_MP_REQUEST = win32more.Storage.IscsiDisc.STORAGE_DIAGNOSTIC_MP_REQUEST_head
    STORAGE_DIAGNOSTIC_MP_REQUEST._fields_ = [
        ("Version", UInt32),
        ("Size", UInt32),
        ("TargetType", win32more.Storage.IscsiDisc.MP_STORAGE_DIAGNOSTIC_TARGET_TYPE),
        ("Level", win32more.Storage.IscsiDisc.MP_STORAGE_DIAGNOSTIC_LEVEL),
        ("ProviderId", Guid),
        ("BufferSize", UInt32),
        ("Reserved", UInt32),
        ("DataBuffer", Byte * 0),
    ]
    return STORAGE_DIAGNOSTIC_MP_REQUEST
def _define_MP_DEVICE_DATA_SET_RANGE_head():
    class MP_DEVICE_DATA_SET_RANGE(Structure):
        pass
    return MP_DEVICE_DATA_SET_RANGE
def _define_MP_DEVICE_DATA_SET_RANGE():
    MP_DEVICE_DATA_SET_RANGE = win32more.Storage.IscsiDisc.MP_DEVICE_DATA_SET_RANGE_head
    MP_DEVICE_DATA_SET_RANGE._fields_ = [
        ("StartingOffset", Int64),
        ("LengthInBytes", UInt64),
    ]
    return MP_DEVICE_DATA_SET_RANGE
def _define_DSM_NOTIFICATION_REQUEST_BLOCK_head():
    class DSM_NOTIFICATION_REQUEST_BLOCK(Structure):
        pass
    return DSM_NOTIFICATION_REQUEST_BLOCK
def _define_DSM_NOTIFICATION_REQUEST_BLOCK():
    DSM_NOTIFICATION_REQUEST_BLOCK = win32more.Storage.IscsiDisc.DSM_NOTIFICATION_REQUEST_BLOCK_head
    DSM_NOTIFICATION_REQUEST_BLOCK._fields_ = [
        ("Size", UInt32),
        ("Version", UInt32),
        ("NotifyFlags", UInt32),
        ("DataSetProfile", UInt32),
        ("Reserved", UInt32 * 3),
        ("DataSetRangesCount", UInt32),
        ("DataSetRanges", win32more.Storage.IscsiDisc.MP_DEVICE_DATA_SET_RANGE * 0),
    ]
    return DSM_NOTIFICATION_REQUEST_BLOCK
def _define_HYBRID_REQUEST_BLOCK_head():
    class HYBRID_REQUEST_BLOCK(Structure):
        pass
    return HYBRID_REQUEST_BLOCK
def _define_HYBRID_REQUEST_BLOCK():
    HYBRID_REQUEST_BLOCK = win32more.Storage.IscsiDisc.HYBRID_REQUEST_BLOCK_head
    HYBRID_REQUEST_BLOCK._fields_ = [
        ("Version", UInt32),
        ("Size", UInt32),
        ("Function", UInt32),
        ("Flags", UInt32),
        ("DataBufferOffset", UInt32),
        ("DataBufferLength", UInt32),
    ]
    return HYBRID_REQUEST_BLOCK
NVCACHE_TYPE = Int32
NVCACHE_TYPE_NvCacheTypeUnknown = 0
NVCACHE_TYPE_NvCacheTypeNone = 1
NVCACHE_TYPE_NvCacheTypeWriteBack = 2
NVCACHE_TYPE_NvCacheTypeWriteThrough = 3
NVCACHE_STATUS = Int32
NVCACHE_STATUS_NvCacheStatusUnknown = 0
NVCACHE_STATUS_NvCacheStatusDisabling = 1
NVCACHE_STATUS_NvCacheStatusDisabled = 2
NVCACHE_STATUS_NvCacheStatusEnabled = 3
def _define_NVCACHE_PRIORITY_LEVEL_DESCRIPTOR_head():
    class NVCACHE_PRIORITY_LEVEL_DESCRIPTOR(Structure):
        pass
    return NVCACHE_PRIORITY_LEVEL_DESCRIPTOR
def _define_NVCACHE_PRIORITY_LEVEL_DESCRIPTOR():
    NVCACHE_PRIORITY_LEVEL_DESCRIPTOR = win32more.Storage.IscsiDisc.NVCACHE_PRIORITY_LEVEL_DESCRIPTOR_head
    NVCACHE_PRIORITY_LEVEL_DESCRIPTOR._fields_ = [
        ("PriorityLevel", Byte),
        ("Reserved0", Byte * 3),
        ("ConsumedNVMSizeFraction", UInt32),
        ("ConsumedMappingResourcesFraction", UInt32),
        ("ConsumedNVMSizeForDirtyDataFraction", UInt32),
        ("ConsumedMappingResourcesForDirtyDataFraction", UInt32),
        ("Reserved1", UInt32),
    ]
    return NVCACHE_PRIORITY_LEVEL_DESCRIPTOR
def _define_HYBRID_INFORMATION_head():
    class HYBRID_INFORMATION(Structure):
        pass
    return HYBRID_INFORMATION
def _define_HYBRID_INFORMATION():
    HYBRID_INFORMATION = win32more.Storage.IscsiDisc.HYBRID_INFORMATION_head
    class HYBRID_INFORMATION__Priorities_e__Struct(Structure):
        pass
    class HYBRID_INFORMATION__Priorities_e__Struct__SupportedCommands_e__Struct(Structure):
        pass
    HYBRID_INFORMATION__Priorities_e__Struct__SupportedCommands_e__Struct._fields_ = [
        ("_bitfield", UInt32),
        ("MaxEvictCommands", UInt32),
        ("MaxLbaRangeCountForEvict", UInt32),
        ("MaxLbaRangeCountForChangeLba", UInt32),
    ]
    HYBRID_INFORMATION__Priorities_e__Struct._fields_ = [
        ("PriorityLevelCount", Byte),
        ("MaxPriorityBehavior", win32more.Foundation.BOOLEAN),
        ("OptimalWriteGranularity", Byte),
        ("Reserved", Byte),
        ("DirtyThresholdLow", UInt32),
        ("DirtyThresholdHigh", UInt32),
        ("SupportedCommands", HYBRID_INFORMATION__Priorities_e__Struct__SupportedCommands_e__Struct),
        ("Priority", win32more.Storage.IscsiDisc.NVCACHE_PRIORITY_LEVEL_DESCRIPTOR * 0),
    ]
    class HYBRID_INFORMATION__Attributes_e__Struct(Structure):
        pass
    HYBRID_INFORMATION__Attributes_e__Struct._fields_ = [
        ("_bitfield", UInt32),
    ]
    HYBRID_INFORMATION._fields_ = [
        ("Version", UInt32),
        ("Size", UInt32),
        ("HybridSupported", win32more.Foundation.BOOLEAN),
        ("Status", win32more.Storage.IscsiDisc.NVCACHE_STATUS),
        ("CacheTypeEffective", win32more.Storage.IscsiDisc.NVCACHE_TYPE),
        ("CacheTypeDefault", win32more.Storage.IscsiDisc.NVCACHE_TYPE),
        ("FractionBase", UInt32),
        ("CacheSize", UInt64),
        ("Attributes", HYBRID_INFORMATION__Attributes_e__Struct),
        ("Priorities", HYBRID_INFORMATION__Priorities_e__Struct),
    ]
    return HYBRID_INFORMATION
def _define_HYBRID_DIRTY_THRESHOLDS_head():
    class HYBRID_DIRTY_THRESHOLDS(Structure):
        pass
    return HYBRID_DIRTY_THRESHOLDS
def _define_HYBRID_DIRTY_THRESHOLDS():
    HYBRID_DIRTY_THRESHOLDS = win32more.Storage.IscsiDisc.HYBRID_DIRTY_THRESHOLDS_head
    HYBRID_DIRTY_THRESHOLDS._fields_ = [
        ("Version", UInt32),
        ("Size", UInt32),
        ("DirtyLowThreshold", UInt32),
        ("DirtyHighThreshold", UInt32),
    ]
    return HYBRID_DIRTY_THRESHOLDS
def _define_HYBRID_DEMOTE_BY_SIZE_head():
    class HYBRID_DEMOTE_BY_SIZE(Structure):
        pass
    return HYBRID_DEMOTE_BY_SIZE
def _define_HYBRID_DEMOTE_BY_SIZE():
    HYBRID_DEMOTE_BY_SIZE = win32more.Storage.IscsiDisc.HYBRID_DEMOTE_BY_SIZE_head
    HYBRID_DEMOTE_BY_SIZE._fields_ = [
        ("Version", UInt32),
        ("Size", UInt32),
        ("SourcePriority", Byte),
        ("TargetPriority", Byte),
        ("Reserved0", UInt16),
        ("Reserved1", UInt32),
        ("LbaCount", UInt64),
    ]
    return HYBRID_DEMOTE_BY_SIZE
def _define_FIRMWARE_REQUEST_BLOCK_head():
    class FIRMWARE_REQUEST_BLOCK(Structure):
        pass
    return FIRMWARE_REQUEST_BLOCK
def _define_FIRMWARE_REQUEST_BLOCK():
    FIRMWARE_REQUEST_BLOCK = win32more.Storage.IscsiDisc.FIRMWARE_REQUEST_BLOCK_head
    FIRMWARE_REQUEST_BLOCK._fields_ = [
        ("Version", UInt32),
        ("Size", UInt32),
        ("Function", UInt32),
        ("Flags", UInt32),
        ("DataBufferOffset", UInt32),
        ("DataBufferLength", UInt32),
    ]
    return FIRMWARE_REQUEST_BLOCK
def _define_STORAGE_FIRMWARE_SLOT_INFO_head():
    class STORAGE_FIRMWARE_SLOT_INFO(Structure):
        pass
    return STORAGE_FIRMWARE_SLOT_INFO
def _define_STORAGE_FIRMWARE_SLOT_INFO():
    STORAGE_FIRMWARE_SLOT_INFO = win32more.Storage.IscsiDisc.STORAGE_FIRMWARE_SLOT_INFO_head
    class STORAGE_FIRMWARE_SLOT_INFO__Revision_e__Union(Union):
        pass
    STORAGE_FIRMWARE_SLOT_INFO__Revision_e__Union._fields_ = [
        ("Info", Byte * 8),
        ("AsUlonglong", UInt64),
    ]
    STORAGE_FIRMWARE_SLOT_INFO._fields_ = [
        ("SlotNumber", Byte),
        ("ReadOnly", win32more.Foundation.BOOLEAN),
        ("Reserved", Byte * 6),
        ("Revision", STORAGE_FIRMWARE_SLOT_INFO__Revision_e__Union),
    ]
    return STORAGE_FIRMWARE_SLOT_INFO
def _define_STORAGE_FIRMWARE_SLOT_INFO_V2_head():
    class STORAGE_FIRMWARE_SLOT_INFO_V2(Structure):
        pass
    return STORAGE_FIRMWARE_SLOT_INFO_V2
def _define_STORAGE_FIRMWARE_SLOT_INFO_V2():
    STORAGE_FIRMWARE_SLOT_INFO_V2 = win32more.Storage.IscsiDisc.STORAGE_FIRMWARE_SLOT_INFO_V2_head
    STORAGE_FIRMWARE_SLOT_INFO_V2._fields_ = [
        ("SlotNumber", Byte),
        ("ReadOnly", win32more.Foundation.BOOLEAN),
        ("Reserved", Byte * 6),
        ("Revision", Byte * 16),
    ]
    return STORAGE_FIRMWARE_SLOT_INFO_V2
def _define_STORAGE_FIRMWARE_INFO_head():
    class STORAGE_FIRMWARE_INFO(Structure):
        pass
    return STORAGE_FIRMWARE_INFO
def _define_STORAGE_FIRMWARE_INFO():
    STORAGE_FIRMWARE_INFO = win32more.Storage.IscsiDisc.STORAGE_FIRMWARE_INFO_head
    STORAGE_FIRMWARE_INFO._fields_ = [
        ("Version", UInt32),
        ("Size", UInt32),
        ("UpgradeSupport", win32more.Foundation.BOOLEAN),
        ("SlotCount", Byte),
        ("ActiveSlot", Byte),
        ("PendingActivateSlot", Byte),
        ("Reserved", UInt32),
        ("Slot", win32more.Storage.IscsiDisc.STORAGE_FIRMWARE_SLOT_INFO * 0),
    ]
    return STORAGE_FIRMWARE_INFO
def _define_STORAGE_FIRMWARE_INFO_V2_head():
    class STORAGE_FIRMWARE_INFO_V2(Structure):
        pass
    return STORAGE_FIRMWARE_INFO_V2
def _define_STORAGE_FIRMWARE_INFO_V2():
    STORAGE_FIRMWARE_INFO_V2 = win32more.Storage.IscsiDisc.STORAGE_FIRMWARE_INFO_V2_head
    STORAGE_FIRMWARE_INFO_V2._fields_ = [
        ("Version", UInt32),
        ("Size", UInt32),
        ("UpgradeSupport", win32more.Foundation.BOOLEAN),
        ("SlotCount", Byte),
        ("ActiveSlot", Byte),
        ("PendingActivateSlot", Byte),
        ("FirmwareShared", win32more.Foundation.BOOLEAN),
        ("Reserved", Byte * 3),
        ("ImagePayloadAlignment", UInt32),
        ("ImagePayloadMaxSize", UInt32),
        ("Slot", win32more.Storage.IscsiDisc.STORAGE_FIRMWARE_SLOT_INFO_V2 * 0),
    ]
    return STORAGE_FIRMWARE_INFO_V2
def _define_STORAGE_FIRMWARE_DOWNLOAD_head():
    class STORAGE_FIRMWARE_DOWNLOAD(Structure):
        pass
    return STORAGE_FIRMWARE_DOWNLOAD
def _define_STORAGE_FIRMWARE_DOWNLOAD():
    STORAGE_FIRMWARE_DOWNLOAD = win32more.Storage.IscsiDisc.STORAGE_FIRMWARE_DOWNLOAD_head
    STORAGE_FIRMWARE_DOWNLOAD._fields_ = [
        ("Version", UInt32),
        ("Size", UInt32),
        ("Offset", UInt64),
        ("BufferSize", UInt64),
        ("ImageBuffer", Byte * 0),
    ]
    return STORAGE_FIRMWARE_DOWNLOAD
def _define_STORAGE_FIRMWARE_DOWNLOAD_V2_head():
    class STORAGE_FIRMWARE_DOWNLOAD_V2(Structure):
        pass
    return STORAGE_FIRMWARE_DOWNLOAD_V2
def _define_STORAGE_FIRMWARE_DOWNLOAD_V2():
    STORAGE_FIRMWARE_DOWNLOAD_V2 = win32more.Storage.IscsiDisc.STORAGE_FIRMWARE_DOWNLOAD_V2_head
    STORAGE_FIRMWARE_DOWNLOAD_V2._fields_ = [
        ("Version", UInt32),
        ("Size", UInt32),
        ("Offset", UInt64),
        ("BufferSize", UInt64),
        ("Slot", Byte),
        ("Reserved", Byte * 3),
        ("ImageSize", UInt32),
        ("ImageBuffer", Byte * 0),
    ]
    return STORAGE_FIRMWARE_DOWNLOAD_V2
def _define_STORAGE_FIRMWARE_ACTIVATE_head():
    class STORAGE_FIRMWARE_ACTIVATE(Structure):
        pass
    return STORAGE_FIRMWARE_ACTIVATE
def _define_STORAGE_FIRMWARE_ACTIVATE():
    STORAGE_FIRMWARE_ACTIVATE = win32more.Storage.IscsiDisc.STORAGE_FIRMWARE_ACTIVATE_head
    STORAGE_FIRMWARE_ACTIVATE._fields_ = [
        ("Version", UInt32),
        ("Size", UInt32),
        ("SlotToActivate", Byte),
        ("Reserved0", Byte * 3),
    ]
    return STORAGE_FIRMWARE_ACTIVATE
def _define_IO_SCSI_CAPABILITIES_head():
    class IO_SCSI_CAPABILITIES(Structure):
        pass
    return IO_SCSI_CAPABILITIES
def _define_IO_SCSI_CAPABILITIES():
    IO_SCSI_CAPABILITIES = win32more.Storage.IscsiDisc.IO_SCSI_CAPABILITIES_head
    IO_SCSI_CAPABILITIES._fields_ = [
        ("Length", UInt32),
        ("MaximumTransferLength", UInt32),
        ("MaximumPhysicalPages", UInt32),
        ("SupportedAsynchronousEvents", UInt32),
        ("AlignmentMask", UInt32),
        ("TaggedQueuing", win32more.Foundation.BOOLEAN),
        ("AdapterScansDown", win32more.Foundation.BOOLEAN),
        ("AdapterUsesPio", win32more.Foundation.BOOLEAN),
    ]
    return IO_SCSI_CAPABILITIES
def _define_SCSI_ADDRESS_head():
    class SCSI_ADDRESS(Structure):
        pass
    return SCSI_ADDRESS
def _define_SCSI_ADDRESS():
    SCSI_ADDRESS = win32more.Storage.IscsiDisc.SCSI_ADDRESS_head
    SCSI_ADDRESS._fields_ = [
        ("Length", UInt32),
        ("PortNumber", Byte),
        ("PathId", Byte),
        ("TargetId", Byte),
        ("Lun", Byte),
    ]
    return SCSI_ADDRESS
def _define_DUMP_DEVICE_POWERON_ROUTINE():
    return CFUNCTYPE(Int32,c_void_p, use_last_error=False)
def _define_PDUMP_DEVICE_POWERON_ROUTINE():
    return CFUNCTYPE(Int32, use_last_error=False)
def _define_DUMP_POINTERS_VERSION_head():
    class DUMP_POINTERS_VERSION(Structure):
        pass
    return DUMP_POINTERS_VERSION
def _define_DUMP_POINTERS_VERSION():
    DUMP_POINTERS_VERSION = win32more.Storage.IscsiDisc.DUMP_POINTERS_VERSION_head
    DUMP_POINTERS_VERSION._fields_ = [
        ("Version", UInt32),
        ("Size", UInt32),
    ]
    return DUMP_POINTERS_VERSION
def _define_DUMP_POINTERS_head():
    class DUMP_POINTERS(Structure):
        pass
    return DUMP_POINTERS
def _define_DUMP_POINTERS():
    DUMP_POINTERS = win32more.Storage.IscsiDisc.DUMP_POINTERS_head
    DUMP_POINTERS._fields_ = [
        ("AdapterObject", POINTER(win32more.Storage.IscsiDisc._ADAPTER_OBJECT_head)),
        ("MappedRegisterBase", c_void_p),
        ("DumpData", c_void_p),
        ("CommonBufferVa", c_void_p),
        ("CommonBufferPa", win32more.Foundation.LARGE_INTEGER),
        ("CommonBufferSize", UInt32),
        ("AllocateCommonBuffers", win32more.Foundation.BOOLEAN),
        ("UseDiskDump", win32more.Foundation.BOOLEAN),
        ("Spare1", Byte * 2),
        ("DeviceObject", c_void_p),
    ]
    return DUMP_POINTERS
def _define_DUMP_POINTERS_EX_head():
    class DUMP_POINTERS_EX(Structure):
        pass
    return DUMP_POINTERS_EX
def _define_DUMP_POINTERS_EX():
    DUMP_POINTERS_EX = win32more.Storage.IscsiDisc.DUMP_POINTERS_EX_head
    DUMP_POINTERS_EX._fields_ = [
        ("Header", win32more.Storage.IscsiDisc.DUMP_POINTERS_VERSION),
        ("DumpData", c_void_p),
        ("CommonBufferVa", c_void_p),
        ("CommonBufferSize", UInt32),
        ("AllocateCommonBuffers", win32more.Foundation.BOOLEAN),
        ("DeviceObject", c_void_p),
        ("DriverList", c_void_p),
        ("dwPortFlags", UInt32),
        ("MaxDeviceDumpSectionSize", UInt32),
        ("MaxDeviceDumpLevel", UInt32),
        ("MaxTransferSize", UInt32),
        ("AdapterObject", c_void_p),
        ("MappedRegisterBase", c_void_p),
        ("DeviceReady", POINTER(win32more.Foundation.BOOLEAN)),
        ("DumpDevicePowerOn", win32more.Storage.IscsiDisc.PDUMP_DEVICE_POWERON_ROUTINE),
        ("DumpDevicePowerOnContext", c_void_p),
    ]
    return DUMP_POINTERS_EX
def _define_DUMP_DRIVER_head():
    class DUMP_DRIVER(Structure):
        pass
    return DUMP_DRIVER
def _define_DUMP_DRIVER():
    DUMP_DRIVER = win32more.Storage.IscsiDisc.DUMP_DRIVER_head
    DUMP_DRIVER._fields_ = [
        ("DumpDriverList", c_void_p),
        ("DriverName", Char * 15),
        ("BaseName", Char * 15),
    ]
    return DUMP_DRIVER
def _define_NTSCSI_UNICODE_STRING_head():
    class NTSCSI_UNICODE_STRING(Structure):
        pass
    return NTSCSI_UNICODE_STRING
def _define_NTSCSI_UNICODE_STRING():
    NTSCSI_UNICODE_STRING = win32more.Storage.IscsiDisc.NTSCSI_UNICODE_STRING_head
    NTSCSI_UNICODE_STRING._fields_ = [
        ("Length", UInt16),
        ("MaximumLength", UInt16),
        ("Buffer", win32more.Foundation.PWSTR),
    ]
    return NTSCSI_UNICODE_STRING
def _define_DUMP_DRIVER_EX_head():
    class DUMP_DRIVER_EX(Structure):
        pass
    return DUMP_DRIVER_EX
def _define_DUMP_DRIVER_EX():
    DUMP_DRIVER_EX = win32more.Storage.IscsiDisc.DUMP_DRIVER_EX_head
    DUMP_DRIVER_EX._fields_ = [
        ("DumpDriverList", c_void_p),
        ("DriverName", Char * 15),
        ("BaseName", Char * 15),
        ("DriverFullPath", win32more.Storage.IscsiDisc.NTSCSI_UNICODE_STRING),
    ]
    return DUMP_DRIVER_EX
def _define_STORAGE_ENDURANCE_INFO_head():
    class STORAGE_ENDURANCE_INFO(Structure):
        pass
    return STORAGE_ENDURANCE_INFO
def _define_STORAGE_ENDURANCE_INFO():
    STORAGE_ENDURANCE_INFO = win32more.Storage.IscsiDisc.STORAGE_ENDURANCE_INFO_head
    class STORAGE_ENDURANCE_INFO__Flags_e__Struct(Structure):
        pass
    STORAGE_ENDURANCE_INFO__Flags_e__Struct._fields_ = [
        ("_bitfield", UInt32),
    ]
    STORAGE_ENDURANCE_INFO._fields_ = [
        ("ValidFields", UInt32),
        ("GroupId", UInt32),
        ("Flags", STORAGE_ENDURANCE_INFO__Flags_e__Struct),
        ("LifePercentage", UInt32),
        ("BytesReadCount", Byte * 16),
        ("ByteWriteCount", Byte * 16),
    ]
    return STORAGE_ENDURANCE_INFO
def _define_STORAGE_ENDURANCE_DATA_DESCRIPTOR_head():
    class STORAGE_ENDURANCE_DATA_DESCRIPTOR(Structure):
        pass
    return STORAGE_ENDURANCE_DATA_DESCRIPTOR
def _define_STORAGE_ENDURANCE_DATA_DESCRIPTOR():
    STORAGE_ENDURANCE_DATA_DESCRIPTOR = win32more.Storage.IscsiDisc.STORAGE_ENDURANCE_DATA_DESCRIPTOR_head
    STORAGE_ENDURANCE_DATA_DESCRIPTOR._fields_ = [
        ("Version", UInt32),
        ("Size", UInt32),
        ("EnduranceInfo", win32more.Storage.IscsiDisc.STORAGE_ENDURANCE_INFO),
    ]
    return STORAGE_ENDURANCE_DATA_DESCRIPTOR
ISCSI_DIGEST_TYPES = Int32
ISCSI_DIGEST_TYPE_NONE = 0
ISCSI_DIGEST_TYPE_CRC32C = 1
ISCSI_AUTH_TYPES = Int32
ISCSI_NO_AUTH_TYPE = 0
ISCSI_CHAP_AUTH_TYPE = 1
ISCSI_MUTUAL_CHAP_AUTH_TYPE = 2
def _define_ISCSI_LOGIN_OPTIONS_head():
    class ISCSI_LOGIN_OPTIONS(Structure):
        pass
    return ISCSI_LOGIN_OPTIONS
def _define_ISCSI_LOGIN_OPTIONS():
    ISCSI_LOGIN_OPTIONS = win32more.Storage.IscsiDisc.ISCSI_LOGIN_OPTIONS_head
    ISCSI_LOGIN_OPTIONS._fields_ = [
        ("Version", UInt32),
        ("InformationSpecified", UInt32),
        ("LoginFlags", UInt32),
        ("AuthType", win32more.Storage.IscsiDisc.ISCSI_AUTH_TYPES),
        ("HeaderDigest", win32more.Storage.IscsiDisc.ISCSI_DIGEST_TYPES),
        ("DataDigest", win32more.Storage.IscsiDisc.ISCSI_DIGEST_TYPES),
        ("MaximumConnections", UInt32),
        ("DefaultTime2Wait", UInt32),
        ("DefaultTime2Retain", UInt32),
        ("UsernameLength", UInt32),
        ("PasswordLength", UInt32),
        ("Username", c_char_p_no),
        ("Password", c_char_p_no),
    ]
    return ISCSI_LOGIN_OPTIONS
IKE_AUTHENTICATION_METHOD = Int32
IKE_AUTHENTICATION_PRESHARED_KEY_METHOD = 1
def _define_IKE_AUTHENTICATION_PRESHARED_KEY_head():
    class IKE_AUTHENTICATION_PRESHARED_KEY(Structure):
        pass
    return IKE_AUTHENTICATION_PRESHARED_KEY
def _define_IKE_AUTHENTICATION_PRESHARED_KEY():
    IKE_AUTHENTICATION_PRESHARED_KEY = win32more.Storage.IscsiDisc.IKE_AUTHENTICATION_PRESHARED_KEY_head
    IKE_AUTHENTICATION_PRESHARED_KEY._fields_ = [
        ("SecurityFlags", UInt64),
        ("IdType", Byte),
        ("IdLengthInBytes", UInt32),
        ("Id", c_char_p_no),
        ("KeyLengthInBytes", UInt32),
        ("Key", c_char_p_no),
    ]
    return IKE_AUTHENTICATION_PRESHARED_KEY
def _define_IKE_AUTHENTICATION_INFORMATION_head():
    class IKE_AUTHENTICATION_INFORMATION(Structure):
        pass
    return IKE_AUTHENTICATION_INFORMATION
def _define_IKE_AUTHENTICATION_INFORMATION():
    IKE_AUTHENTICATION_INFORMATION = win32more.Storage.IscsiDisc.IKE_AUTHENTICATION_INFORMATION_head
    class IKE_AUTHENTICATION_INFORMATION__Anonymous_e__Union(Union):
        pass
    IKE_AUTHENTICATION_INFORMATION__Anonymous_e__Union._fields_ = [
        ("PsKey", win32more.Storage.IscsiDisc.IKE_AUTHENTICATION_PRESHARED_KEY),
    ]
    IKE_AUTHENTICATION_INFORMATION._anonymous_ = [
        'Anonymous',
    ]
    IKE_AUTHENTICATION_INFORMATION._fields_ = [
        ("AuthMethod", win32more.Storage.IscsiDisc.IKE_AUTHENTICATION_METHOD),
        ("Anonymous", IKE_AUTHENTICATION_INFORMATION__Anonymous_e__Union),
    ]
    return IKE_AUTHENTICATION_INFORMATION
def _define_ISCSI_UNIQUE_SESSION_ID_head():
    class ISCSI_UNIQUE_SESSION_ID(Structure):
        pass
    return ISCSI_UNIQUE_SESSION_ID
def _define_ISCSI_UNIQUE_SESSION_ID():
    ISCSI_UNIQUE_SESSION_ID = win32more.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID_head
    ISCSI_UNIQUE_SESSION_ID._fields_ = [
        ("AdapterUnique", UInt64),
        ("AdapterSpecific", UInt64),
    ]
    return ISCSI_UNIQUE_SESSION_ID
def _define_SCSI_LUN_LIST_head():
    class SCSI_LUN_LIST(Structure):
        pass
    return SCSI_LUN_LIST
def _define_SCSI_LUN_LIST():
    SCSI_LUN_LIST = win32more.Storage.IscsiDisc.SCSI_LUN_LIST_head
    SCSI_LUN_LIST._fields_ = [
        ("OSLUN", UInt32),
        ("TargetLUN", UInt64),
    ]
    return SCSI_LUN_LIST
def _define_ISCSI_TARGET_MAPPINGW_head():
    class ISCSI_TARGET_MAPPINGW(Structure):
        pass
    return ISCSI_TARGET_MAPPINGW
def _define_ISCSI_TARGET_MAPPINGW():
    ISCSI_TARGET_MAPPINGW = win32more.Storage.IscsiDisc.ISCSI_TARGET_MAPPINGW_head
    ISCSI_TARGET_MAPPINGW._fields_ = [
        ("InitiatorName", Char * 256),
        ("TargetName", Char * 224),
        ("OSDeviceName", Char * 260),
        ("SessionId", win32more.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID),
        ("OSBusNumber", UInt32),
        ("OSTargetNumber", UInt32),
        ("LUNCount", UInt32),
        ("LUNList", POINTER(win32more.Storage.IscsiDisc.SCSI_LUN_LIST_head)),
    ]
    return ISCSI_TARGET_MAPPINGW
def _define_ISCSI_TARGET_MAPPINGA_head():
    class ISCSI_TARGET_MAPPINGA(Structure):
        pass
    return ISCSI_TARGET_MAPPINGA
def _define_ISCSI_TARGET_MAPPINGA():
    ISCSI_TARGET_MAPPINGA = win32more.Storage.IscsiDisc.ISCSI_TARGET_MAPPINGA_head
    ISCSI_TARGET_MAPPINGA._fields_ = [
        ("InitiatorName", win32more.Foundation.CHAR * 256),
        ("TargetName", win32more.Foundation.CHAR * 224),
        ("OSDeviceName", win32more.Foundation.CHAR * 260),
        ("SessionId", win32more.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID),
        ("OSBusNumber", UInt32),
        ("OSTargetNumber", UInt32),
        ("LUNCount", UInt32),
        ("LUNList", POINTER(win32more.Storage.IscsiDisc.SCSI_LUN_LIST_head)),
    ]
    return ISCSI_TARGET_MAPPINGA
def _define_ISCSI_TARGET_PORTALW_head():
    class ISCSI_TARGET_PORTALW(Structure):
        pass
    return ISCSI_TARGET_PORTALW
def _define_ISCSI_TARGET_PORTALW():
    ISCSI_TARGET_PORTALW = win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTALW_head
    ISCSI_TARGET_PORTALW._fields_ = [
        ("SymbolicName", Char * 256),
        ("Address", Char * 256),
        ("Socket", UInt16),
    ]
    return ISCSI_TARGET_PORTALW
def _define_ISCSI_TARGET_PORTALA_head():
    class ISCSI_TARGET_PORTALA(Structure):
        pass
    return ISCSI_TARGET_PORTALA
def _define_ISCSI_TARGET_PORTALA():
    ISCSI_TARGET_PORTALA = win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTALA_head
    ISCSI_TARGET_PORTALA._fields_ = [
        ("SymbolicName", win32more.Foundation.CHAR * 256),
        ("Address", win32more.Foundation.CHAR * 256),
        ("Socket", UInt16),
    ]
    return ISCSI_TARGET_PORTALA
def _define_ISCSI_TARGET_PORTAL_INFOW_head():
    class ISCSI_TARGET_PORTAL_INFOW(Structure):
        pass
    return ISCSI_TARGET_PORTAL_INFOW
def _define_ISCSI_TARGET_PORTAL_INFOW():
    ISCSI_TARGET_PORTAL_INFOW = win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTAL_INFOW_head
    ISCSI_TARGET_PORTAL_INFOW._fields_ = [
        ("InitiatorName", Char * 256),
        ("InitiatorPortNumber", UInt32),
        ("SymbolicName", Char * 256),
        ("Address", Char * 256),
        ("Socket", UInt16),
    ]
    return ISCSI_TARGET_PORTAL_INFOW
def _define_ISCSI_TARGET_PORTAL_INFOA_head():
    class ISCSI_TARGET_PORTAL_INFOA(Structure):
        pass
    return ISCSI_TARGET_PORTAL_INFOA
def _define_ISCSI_TARGET_PORTAL_INFOA():
    ISCSI_TARGET_PORTAL_INFOA = win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTAL_INFOA_head
    ISCSI_TARGET_PORTAL_INFOA._fields_ = [
        ("InitiatorName", win32more.Foundation.CHAR * 256),
        ("InitiatorPortNumber", UInt32),
        ("SymbolicName", win32more.Foundation.CHAR * 256),
        ("Address", win32more.Foundation.CHAR * 256),
        ("Socket", UInt16),
    ]
    return ISCSI_TARGET_PORTAL_INFOA
def _define_ISCSI_TARGET_PORTAL_INFO_EXW_head():
    class ISCSI_TARGET_PORTAL_INFO_EXW(Structure):
        pass
    return ISCSI_TARGET_PORTAL_INFO_EXW
def _define_ISCSI_TARGET_PORTAL_INFO_EXW():
    ISCSI_TARGET_PORTAL_INFO_EXW = win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTAL_INFO_EXW_head
    ISCSI_TARGET_PORTAL_INFO_EXW._fields_ = [
        ("InitiatorName", Char * 256),
        ("InitiatorPortNumber", UInt32),
        ("SymbolicName", Char * 256),
        ("Address", Char * 256),
        ("Socket", UInt16),
        ("SecurityFlags", UInt64),
        ("LoginOptions", win32more.Storage.IscsiDisc.ISCSI_LOGIN_OPTIONS),
    ]
    return ISCSI_TARGET_PORTAL_INFO_EXW
def _define_ISCSI_TARGET_PORTAL_INFO_EXA_head():
    class ISCSI_TARGET_PORTAL_INFO_EXA(Structure):
        pass
    return ISCSI_TARGET_PORTAL_INFO_EXA
def _define_ISCSI_TARGET_PORTAL_INFO_EXA():
    ISCSI_TARGET_PORTAL_INFO_EXA = win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTAL_INFO_EXA_head
    ISCSI_TARGET_PORTAL_INFO_EXA._fields_ = [
        ("InitiatorName", win32more.Foundation.CHAR * 256),
        ("InitiatorPortNumber", UInt32),
        ("SymbolicName", win32more.Foundation.CHAR * 256),
        ("Address", win32more.Foundation.CHAR * 256),
        ("Socket", UInt16),
        ("SecurityFlags", UInt64),
        ("LoginOptions", win32more.Storage.IscsiDisc.ISCSI_LOGIN_OPTIONS),
    ]
    return ISCSI_TARGET_PORTAL_INFO_EXA
def _define_ISCSI_TARGET_PORTAL_GROUPW_head():
    class ISCSI_TARGET_PORTAL_GROUPW(Structure):
        pass
    return ISCSI_TARGET_PORTAL_GROUPW
def _define_ISCSI_TARGET_PORTAL_GROUPW():
    ISCSI_TARGET_PORTAL_GROUPW = win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTAL_GROUPW_head
    ISCSI_TARGET_PORTAL_GROUPW._fields_ = [
        ("Count", UInt32),
        ("Portals", win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTALW * 0),
    ]
    return ISCSI_TARGET_PORTAL_GROUPW
def _define_ISCSI_TARGET_PORTAL_GROUPA_head():
    class ISCSI_TARGET_PORTAL_GROUPA(Structure):
        pass
    return ISCSI_TARGET_PORTAL_GROUPA
def _define_ISCSI_TARGET_PORTAL_GROUPA():
    ISCSI_TARGET_PORTAL_GROUPA = win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTAL_GROUPA_head
    ISCSI_TARGET_PORTAL_GROUPA._fields_ = [
        ("Count", UInt32),
        ("Portals", win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTALA * 0),
    ]
    return ISCSI_TARGET_PORTAL_GROUPA
def _define_ISCSI_CONNECTION_INFOW_head():
    class ISCSI_CONNECTION_INFOW(Structure):
        pass
    return ISCSI_CONNECTION_INFOW
def _define_ISCSI_CONNECTION_INFOW():
    ISCSI_CONNECTION_INFOW = win32more.Storage.IscsiDisc.ISCSI_CONNECTION_INFOW_head
    ISCSI_CONNECTION_INFOW._fields_ = [
        ("ConnectionId", win32more.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID),
        ("InitiatorAddress", win32more.Foundation.PWSTR),
        ("TargetAddress", win32more.Foundation.PWSTR),
        ("InitiatorSocket", UInt16),
        ("TargetSocket", UInt16),
        ("CID", Byte * 2),
    ]
    return ISCSI_CONNECTION_INFOW
def _define_ISCSI_SESSION_INFOW_head():
    class ISCSI_SESSION_INFOW(Structure):
        pass
    return ISCSI_SESSION_INFOW
def _define_ISCSI_SESSION_INFOW():
    ISCSI_SESSION_INFOW = win32more.Storage.IscsiDisc.ISCSI_SESSION_INFOW_head
    ISCSI_SESSION_INFOW._fields_ = [
        ("SessionId", win32more.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID),
        ("InitiatorName", win32more.Foundation.PWSTR),
        ("TargetNodeName", win32more.Foundation.PWSTR),
        ("TargetName", win32more.Foundation.PWSTR),
        ("ISID", Byte * 6),
        ("TSID", Byte * 2),
        ("ConnectionCount", UInt32),
        ("Connections", POINTER(win32more.Storage.IscsiDisc.ISCSI_CONNECTION_INFOW_head)),
    ]
    return ISCSI_SESSION_INFOW
def _define_ISCSI_CONNECTION_INFOA_head():
    class ISCSI_CONNECTION_INFOA(Structure):
        pass
    return ISCSI_CONNECTION_INFOA
def _define_ISCSI_CONNECTION_INFOA():
    ISCSI_CONNECTION_INFOA = win32more.Storage.IscsiDisc.ISCSI_CONNECTION_INFOA_head
    ISCSI_CONNECTION_INFOA._fields_ = [
        ("ConnectionId", win32more.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID),
        ("InitiatorAddress", win32more.Foundation.PSTR),
        ("TargetAddress", win32more.Foundation.PSTR),
        ("InitiatorSocket", UInt16),
        ("TargetSocket", UInt16),
        ("CID", Byte * 2),
    ]
    return ISCSI_CONNECTION_INFOA
def _define_ISCSI_SESSION_INFOA_head():
    class ISCSI_SESSION_INFOA(Structure):
        pass
    return ISCSI_SESSION_INFOA
def _define_ISCSI_SESSION_INFOA():
    ISCSI_SESSION_INFOA = win32more.Storage.IscsiDisc.ISCSI_SESSION_INFOA_head
    ISCSI_SESSION_INFOA._fields_ = [
        ("SessionId", win32more.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID),
        ("InitiatorName", win32more.Foundation.PSTR),
        ("TargetNodeName", win32more.Foundation.PSTR),
        ("TargetName", win32more.Foundation.PSTR),
        ("ISID", Byte * 6),
        ("TSID", Byte * 2),
        ("ConnectionCount", UInt32),
        ("Connections", POINTER(win32more.Storage.IscsiDisc.ISCSI_CONNECTION_INFOA_head)),
    ]
    return ISCSI_SESSION_INFOA
def _define_ISCSI_CONNECTION_INFO_EX_head():
    class ISCSI_CONNECTION_INFO_EX(Structure):
        pass
    return ISCSI_CONNECTION_INFO_EX
def _define_ISCSI_CONNECTION_INFO_EX():
    ISCSI_CONNECTION_INFO_EX = win32more.Storage.IscsiDisc.ISCSI_CONNECTION_INFO_EX_head
    ISCSI_CONNECTION_INFO_EX._fields_ = [
        ("ConnectionId", win32more.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID),
        ("State", Byte),
        ("Protocol", Byte),
        ("HeaderDigest", Byte),
        ("DataDigest", Byte),
        ("MaxRecvDataSegmentLength", UInt32),
        ("AuthType", win32more.Storage.IscsiDisc.ISCSI_AUTH_TYPES),
        ("EstimatedThroughput", UInt64),
        ("MaxDatagramSize", UInt32),
    ]
    return ISCSI_CONNECTION_INFO_EX
def _define_ISCSI_SESSION_INFO_EX_head():
    class ISCSI_SESSION_INFO_EX(Structure):
        pass
    return ISCSI_SESSION_INFO_EX
def _define_ISCSI_SESSION_INFO_EX():
    ISCSI_SESSION_INFO_EX = win32more.Storage.IscsiDisc.ISCSI_SESSION_INFO_EX_head
    ISCSI_SESSION_INFO_EX._fields_ = [
        ("SessionId", win32more.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID),
        ("InitialR2t", win32more.Foundation.BOOLEAN),
        ("ImmediateData", win32more.Foundation.BOOLEAN),
        ("Type", Byte),
        ("DataSequenceInOrder", win32more.Foundation.BOOLEAN),
        ("DataPduInOrder", win32more.Foundation.BOOLEAN),
        ("ErrorRecoveryLevel", Byte),
        ("MaxOutstandingR2t", UInt32),
        ("FirstBurstLength", UInt32),
        ("MaxBurstLength", UInt32),
        ("MaximumConnections", UInt32),
        ("ConnectionCount", UInt32),
        ("Connections", POINTER(win32more.Storage.IscsiDisc.ISCSI_CONNECTION_INFO_EX_head)),
    ]
    return ISCSI_SESSION_INFO_EX
def _define_ISCSI_DEVICE_ON_SESSIONW_head():
    class ISCSI_DEVICE_ON_SESSIONW(Structure):
        pass
    return ISCSI_DEVICE_ON_SESSIONW
def _define_ISCSI_DEVICE_ON_SESSIONW():
    ISCSI_DEVICE_ON_SESSIONW = win32more.Storage.IscsiDisc.ISCSI_DEVICE_ON_SESSIONW_head
    ISCSI_DEVICE_ON_SESSIONW._fields_ = [
        ("InitiatorName", Char * 256),
        ("TargetName", Char * 224),
        ("ScsiAddress", win32more.Storage.IscsiDisc.SCSI_ADDRESS),
        ("DeviceInterfaceType", Guid),
        ("DeviceInterfaceName", Char * 260),
        ("LegacyName", Char * 260),
        ("StorageDeviceNumber", win32more.System.Ioctl.STORAGE_DEVICE_NUMBER),
        ("DeviceInstance", UInt32),
    ]
    return ISCSI_DEVICE_ON_SESSIONW
def _define_ISCSI_DEVICE_ON_SESSIONA_head():
    class ISCSI_DEVICE_ON_SESSIONA(Structure):
        pass
    return ISCSI_DEVICE_ON_SESSIONA
def _define_ISCSI_DEVICE_ON_SESSIONA():
    ISCSI_DEVICE_ON_SESSIONA = win32more.Storage.IscsiDisc.ISCSI_DEVICE_ON_SESSIONA_head
    ISCSI_DEVICE_ON_SESSIONA._fields_ = [
        ("InitiatorName", win32more.Foundation.CHAR * 256),
        ("TargetName", win32more.Foundation.CHAR * 224),
        ("ScsiAddress", win32more.Storage.IscsiDisc.SCSI_ADDRESS),
        ("DeviceInterfaceType", Guid),
        ("DeviceInterfaceName", win32more.Foundation.CHAR * 260),
        ("LegacyName", win32more.Foundation.CHAR * 260),
        ("StorageDeviceNumber", win32more.System.Ioctl.STORAGE_DEVICE_NUMBER),
        ("DeviceInstance", UInt32),
    ]
    return ISCSI_DEVICE_ON_SESSIONA
def _define_PERSISTENT_ISCSI_LOGIN_INFOW_head():
    class PERSISTENT_ISCSI_LOGIN_INFOW(Structure):
        pass
    return PERSISTENT_ISCSI_LOGIN_INFOW
def _define_PERSISTENT_ISCSI_LOGIN_INFOW():
    PERSISTENT_ISCSI_LOGIN_INFOW = win32more.Storage.IscsiDisc.PERSISTENT_ISCSI_LOGIN_INFOW_head
    PERSISTENT_ISCSI_LOGIN_INFOW._fields_ = [
        ("TargetName", Char * 224),
        ("IsInformationalSession", win32more.Foundation.BOOLEAN),
        ("InitiatorInstance", Char * 256),
        ("InitiatorPortNumber", UInt32),
        ("TargetPortal", win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTALW),
        ("SecurityFlags", UInt64),
        ("Mappings", POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_MAPPINGW_head)),
        ("LoginOptions", win32more.Storage.IscsiDisc.ISCSI_LOGIN_OPTIONS),
    ]
    return PERSISTENT_ISCSI_LOGIN_INFOW
def _define_PERSISTENT_ISCSI_LOGIN_INFOA_head():
    class PERSISTENT_ISCSI_LOGIN_INFOA(Structure):
        pass
    return PERSISTENT_ISCSI_LOGIN_INFOA
def _define_PERSISTENT_ISCSI_LOGIN_INFOA():
    PERSISTENT_ISCSI_LOGIN_INFOA = win32more.Storage.IscsiDisc.PERSISTENT_ISCSI_LOGIN_INFOA_head
    PERSISTENT_ISCSI_LOGIN_INFOA._fields_ = [
        ("TargetName", win32more.Foundation.CHAR * 224),
        ("IsInformationalSession", win32more.Foundation.BOOLEAN),
        ("InitiatorInstance", win32more.Foundation.CHAR * 256),
        ("InitiatorPortNumber", UInt32),
        ("TargetPortal", win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTALA),
        ("SecurityFlags", UInt64),
        ("Mappings", POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_MAPPINGA_head)),
        ("LoginOptions", win32more.Storage.IscsiDisc.ISCSI_LOGIN_OPTIONS),
    ]
    return PERSISTENT_ISCSI_LOGIN_INFOA
TARGETPROTOCOLTYPE = Int32
ISCSI_TCP_PROTOCOL_TYPE = 0
TARGET_INFORMATION_CLASS = Int32
TARGET_INFORMATION_CLASS_ProtocolType = 0
TARGET_INFORMATION_CLASS_TargetAlias = 1
TARGET_INFORMATION_CLASS_DiscoveryMechanisms = 2
TARGET_INFORMATION_CLASS_PortalGroups = 3
TARGET_INFORMATION_CLASS_PersistentTargetMappings = 4
TARGET_INFORMATION_CLASS_InitiatorName = 5
TARGET_INFORMATION_CLASS_TargetFlags = 6
TARGET_INFORMATION_CLASS_LoginOptions = 7
def _define_ISCSI_VERSION_INFO_head():
    class ISCSI_VERSION_INFO(Structure):
        pass
    return ISCSI_VERSION_INFO
def _define_ISCSI_VERSION_INFO():
    ISCSI_VERSION_INFO = win32more.Storage.IscsiDisc.ISCSI_VERSION_INFO_head
    ISCSI_VERSION_INFO._fields_ = [
        ("MajorVersion", UInt32),
        ("MinorVersion", UInt32),
        ("BuildNumber", UInt32),
    ]
    return ISCSI_VERSION_INFO
def _define_GetIScsiVersionInformation():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Storage.IscsiDisc.ISCSI_VERSION_INFO_head), use_last_error=False)(("GetIScsiVersionInformation", windll["ISCSIDSC"]), ((1, 'VersionInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetIScsiTargetInformationW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Storage.IscsiDisc.TARGET_INFORMATION_CLASS,POINTER(UInt32),c_void_p, use_last_error=False)(("GetIScsiTargetInformationW", windll["ISCSIDSC"]), ((1, 'TargetName'),(1, 'DiscoveryMechanism'),(1, 'InfoClass'),(1, 'BufferSize'),(1, 'Buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetIScsiTargetInformation():
    return win32more.Storage.IscsiDisc.GetIScsiTargetInformationW
def _define_GetIScsiTargetInformationA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Storage.IscsiDisc.TARGET_INFORMATION_CLASS,POINTER(UInt32),c_void_p, use_last_error=False)(("GetIScsiTargetInformationA", windll["ISCSIDSC"]), ((1, 'TargetName'),(1, 'DiscoveryMechanism'),(1, 'InfoClass'),(1, 'BufferSize'),(1, 'Buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddIScsiConnectionW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID_head),c_void_p,UInt32,POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTALW_head),UInt64,POINTER(win32more.Storage.IscsiDisc.ISCSI_LOGIN_OPTIONS_head),UInt32,POINTER(Byte),POINTER(win32more.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID_head), use_last_error=False)(("AddIScsiConnectionW", windll["ISCSIDSC"]), ((1, 'UniqueSessionId'),(1, 'Reserved'),(1, 'InitiatorPortNumber'),(1, 'TargetPortal'),(1, 'SecurityFlags'),(1, 'LoginOptions'),(1, 'KeySize'),(1, 'Key'),(1, 'ConnectionId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddIScsiConnection():
    return win32more.Storage.IscsiDisc.AddIScsiConnectionW
def _define_AddIScsiConnectionA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID_head),c_void_p,UInt32,POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTALA_head),UInt64,POINTER(win32more.Storage.IscsiDisc.ISCSI_LOGIN_OPTIONS_head),UInt32,POINTER(Byte),POINTER(win32more.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID_head), use_last_error=False)(("AddIScsiConnectionA", windll["ISCSIDSC"]), ((1, 'UniqueSessionId'),(1, 'Reserved'),(1, 'InitiatorPortNumber'),(1, 'TargetPortal'),(1, 'SecurityFlags'),(1, 'LoginOptions'),(1, 'KeySize'),(1, 'Key'),(1, 'ConnectionId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RemoveIScsiConnection():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID_head),POINTER(win32more.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID_head), use_last_error=False)(("RemoveIScsiConnection", windll["ISCSIDSC"]), ((1, 'UniqueSessionId'),(1, 'ConnectionId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReportIScsiTargetsW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.BOOLEAN,POINTER(UInt32),POINTER(Char), use_last_error=False)(("ReportIScsiTargetsW", windll["ISCSIDSC"]), ((1, 'ForceUpdate'),(1, 'BufferSize'),(1, 'Buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReportIScsiTargets():
    return win32more.Storage.IscsiDisc.ReportIScsiTargetsW
def _define_ReportIScsiTargetsA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.BOOLEAN,POINTER(UInt32),POINTER(Byte), use_last_error=False)(("ReportIScsiTargetsA", windll["ISCSIDSC"]), ((1, 'ForceUpdate'),(1, 'BufferSize'),(1, 'Buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddIScsiStaticTargetW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.BOOLEAN,POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_MAPPINGW_head),POINTER(win32more.Storage.IscsiDisc.ISCSI_LOGIN_OPTIONS_head),POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTAL_GROUPW_head), use_last_error=False)(("AddIScsiStaticTargetW", windll["ISCSIDSC"]), ((1, 'TargetName'),(1, 'TargetAlias'),(1, 'TargetFlags'),(1, 'Persist'),(1, 'Mappings'),(1, 'LoginOptions'),(1, 'PortalGroup'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddIScsiStaticTarget():
    return win32more.Storage.IscsiDisc.AddIScsiStaticTargetW
def _define_AddIScsiStaticTargetA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32,win32more.Foundation.BOOLEAN,POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_MAPPINGA_head),POINTER(win32more.Storage.IscsiDisc.ISCSI_LOGIN_OPTIONS_head),POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTAL_GROUPA_head), use_last_error=False)(("AddIScsiStaticTargetA", windll["ISCSIDSC"]), ((1, 'TargetName'),(1, 'TargetAlias'),(1, 'TargetFlags'),(1, 'Persist'),(1, 'Mappings'),(1, 'LoginOptions'),(1, 'PortalGroup'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RemoveIScsiStaticTargetW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR, use_last_error=False)(("RemoveIScsiStaticTargetW", windll["ISCSIDSC"]), ((1, 'TargetName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RemoveIScsiStaticTarget():
    return win32more.Storage.IscsiDisc.RemoveIScsiStaticTargetW
def _define_RemoveIScsiStaticTargetA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR, use_last_error=False)(("RemoveIScsiStaticTargetA", windll["ISCSIDSC"]), ((1, 'TargetName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddIScsiSendTargetPortalW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Storage.IscsiDisc.ISCSI_LOGIN_OPTIONS_head),UInt64,POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTALW_head), use_last_error=False)(("AddIScsiSendTargetPortalW", windll["ISCSIDSC"]), ((1, 'InitiatorInstance'),(1, 'InitiatorPortNumber'),(1, 'LoginOptions'),(1, 'SecurityFlags'),(1, 'Portal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddIScsiSendTargetPortal():
    return win32more.Storage.IscsiDisc.AddIScsiSendTargetPortalW
def _define_AddIScsiSendTargetPortalA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,UInt32,POINTER(win32more.Storage.IscsiDisc.ISCSI_LOGIN_OPTIONS_head),UInt64,POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTALA_head), use_last_error=False)(("AddIScsiSendTargetPortalA", windll["ISCSIDSC"]), ((1, 'InitiatorInstance'),(1, 'InitiatorPortNumber'),(1, 'LoginOptions'),(1, 'SecurityFlags'),(1, 'Portal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RemoveIScsiSendTargetPortalW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTALW_head), use_last_error=False)(("RemoveIScsiSendTargetPortalW", windll["ISCSIDSC"]), ((1, 'InitiatorInstance'),(1, 'InitiatorPortNumber'),(1, 'Portal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RemoveIScsiSendTargetPortal():
    return win32more.Storage.IscsiDisc.RemoveIScsiSendTargetPortalW
def _define_RemoveIScsiSendTargetPortalA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,UInt32,POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTALA_head), use_last_error=False)(("RemoveIScsiSendTargetPortalA", windll["ISCSIDSC"]), ((1, 'InitiatorInstance'),(1, 'InitiatorPortNumber'),(1, 'Portal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RefreshIScsiSendTargetPortalW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTALW_head), use_last_error=False)(("RefreshIScsiSendTargetPortalW", windll["ISCSIDSC"]), ((1, 'InitiatorInstance'),(1, 'InitiatorPortNumber'),(1, 'Portal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RefreshIScsiSendTargetPortal():
    return win32more.Storage.IscsiDisc.RefreshIScsiSendTargetPortalW
def _define_RefreshIScsiSendTargetPortalA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,UInt32,POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTALA_head), use_last_error=False)(("RefreshIScsiSendTargetPortalA", windll["ISCSIDSC"]), ((1, 'InitiatorInstance'),(1, 'InitiatorPortNumber'),(1, 'Portal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReportIScsiSendTargetPortalsW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTAL_INFOW_head), use_last_error=False)(("ReportIScsiSendTargetPortalsW", windll["ISCSIDSC"]), ((1, 'PortalCount'),(1, 'PortalInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReportIScsiSendTargetPortals():
    return win32more.Storage.IscsiDisc.ReportIScsiSendTargetPortalsW
def _define_ReportIScsiSendTargetPortalsA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTAL_INFOA_head), use_last_error=False)(("ReportIScsiSendTargetPortalsA", windll["ISCSIDSC"]), ((1, 'PortalCount'),(1, 'PortalInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReportIScsiSendTargetPortalsExW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTAL_INFO_EXW_head), use_last_error=False)(("ReportIScsiSendTargetPortalsExW", windll["ISCSIDSC"]), ((1, 'PortalCount'),(1, 'PortalInfoSize'),(1, 'PortalInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReportIScsiSendTargetPortalsEx():
    return win32more.Storage.IscsiDisc.ReportIScsiSendTargetPortalsExW
def _define_ReportIScsiSendTargetPortalsExA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTAL_INFO_EXA_head), use_last_error=False)(("ReportIScsiSendTargetPortalsExA", windll["ISCSIDSC"]), ((1, 'PortalCount'),(1, 'PortalInfoSize'),(1, 'PortalInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LoginIScsiTargetW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.BOOLEAN,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTALW_head),UInt64,POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_MAPPINGW_head),POINTER(win32more.Storage.IscsiDisc.ISCSI_LOGIN_OPTIONS_head),UInt32,POINTER(Byte),win32more.Foundation.BOOLEAN,POINTER(win32more.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID_head),POINTER(win32more.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID_head), use_last_error=False)(("LoginIScsiTargetW", windll["ISCSIDSC"]), ((1, 'TargetName'),(1, 'IsInformationalSession'),(1, 'InitiatorInstance'),(1, 'InitiatorPortNumber'),(1, 'TargetPortal'),(1, 'SecurityFlags'),(1, 'Mappings'),(1, 'LoginOptions'),(1, 'KeySize'),(1, 'Key'),(1, 'IsPersistent'),(1, 'UniqueSessionId'),(1, 'UniqueConnectionId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LoginIScsiTarget():
    return win32more.Storage.IscsiDisc.LoginIScsiTargetW
def _define_LoginIScsiTargetA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.BOOLEAN,win32more.Foundation.PSTR,UInt32,POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTALA_head),UInt64,POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_MAPPINGA_head),POINTER(win32more.Storage.IscsiDisc.ISCSI_LOGIN_OPTIONS_head),UInt32,POINTER(Byte),win32more.Foundation.BOOLEAN,POINTER(win32more.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID_head),POINTER(win32more.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID_head), use_last_error=False)(("LoginIScsiTargetA", windll["ISCSIDSC"]), ((1, 'TargetName'),(1, 'IsInformationalSession'),(1, 'InitiatorInstance'),(1, 'InitiatorPortNumber'),(1, 'TargetPortal'),(1, 'SecurityFlags'),(1, 'Mappings'),(1, 'LoginOptions'),(1, 'KeySize'),(1, 'Key'),(1, 'IsPersistent'),(1, 'UniqueSessionId'),(1, 'UniqueConnectionId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReportIScsiPersistentLoginsW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),POINTER(win32more.Storage.IscsiDisc.PERSISTENT_ISCSI_LOGIN_INFOW_head),POINTER(UInt32), use_last_error=False)(("ReportIScsiPersistentLoginsW", windll["ISCSIDSC"]), ((1, 'Count'),(1, 'PersistentLoginInfo'),(1, 'BufferSizeInBytes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReportIScsiPersistentLogins():
    return win32more.Storage.IscsiDisc.ReportIScsiPersistentLoginsW
def _define_ReportIScsiPersistentLoginsA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),POINTER(win32more.Storage.IscsiDisc.PERSISTENT_ISCSI_LOGIN_INFOA_head),POINTER(UInt32), use_last_error=False)(("ReportIScsiPersistentLoginsA", windll["ISCSIDSC"]), ((1, 'Count'),(1, 'PersistentLoginInfo'),(1, 'BufferSizeInBytes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LogoutIScsiTarget():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID_head), use_last_error=False)(("LogoutIScsiTarget", windll["ISCSIDSC"]), ((1, 'UniqueSessionId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RemoveIScsiPersistentTargetW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTALW_head), use_last_error=False)(("RemoveIScsiPersistentTargetW", windll["ISCSIDSC"]), ((1, 'InitiatorInstance'),(1, 'InitiatorPortNumber'),(1, 'TargetName'),(1, 'Portal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RemoveIScsiPersistentTarget():
    return win32more.Storage.IscsiDisc.RemoveIScsiPersistentTargetW
def _define_RemoveIScsiPersistentTargetA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTALA_head), use_last_error=False)(("RemoveIScsiPersistentTargetA", windll["ISCSIDSC"]), ((1, 'InitiatorInstance'),(1, 'InitiatorPortNumber'),(1, 'TargetName'),(1, 'Portal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SendScsiInquiry():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID_head),UInt64,Byte,Byte,c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(UInt32),c_char_p_no, use_last_error=False)(("SendScsiInquiry", windll["ISCSIDSC"]), ((1, 'UniqueSessionId'),(1, 'Lun'),(1, 'EvpdCmddt'),(1, 'PageCode'),(1, 'ScsiStatus'),(1, 'ResponseSize'),(1, 'ResponseBuffer'),(1, 'SenseSize'),(1, 'SenseBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SendScsiReadCapacity():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID_head),UInt64,c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(UInt32),c_char_p_no, use_last_error=False)(("SendScsiReadCapacity", windll["ISCSIDSC"]), ((1, 'UniqueSessionId'),(1, 'Lun'),(1, 'ScsiStatus'),(1, 'ResponseSize'),(1, 'ResponseBuffer'),(1, 'SenseSize'),(1, 'SenseBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SendScsiReportLuns():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID_head),c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(UInt32),c_char_p_no, use_last_error=False)(("SendScsiReportLuns", windll["ISCSIDSC"]), ((1, 'UniqueSessionId'),(1, 'ScsiStatus'),(1, 'ResponseSize'),(1, 'ResponseBuffer'),(1, 'SenseSize'),(1, 'SenseBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReportIScsiInitiatorListW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),POINTER(Char), use_last_error=False)(("ReportIScsiInitiatorListW", windll["ISCSIDSC"]), ((1, 'BufferSize'),(1, 'Buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReportIScsiInitiatorList():
    return win32more.Storage.IscsiDisc.ReportIScsiInitiatorListW
def _define_ReportIScsiInitiatorListA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),POINTER(Byte), use_last_error=False)(("ReportIScsiInitiatorListA", windll["ISCSIDSC"]), ((1, 'BufferSize'),(1, 'Buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReportActiveIScsiTargetMappingsW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_MAPPINGW_head), use_last_error=False)(("ReportActiveIScsiTargetMappingsW", windll["ISCSIDSC"]), ((1, 'BufferSize'),(1, 'MappingCount'),(1, 'Mappings'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReportActiveIScsiTargetMappings():
    return win32more.Storage.IscsiDisc.ReportActiveIScsiTargetMappingsW
def _define_ReportActiveIScsiTargetMappingsA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_MAPPINGA_head), use_last_error=False)(("ReportActiveIScsiTargetMappingsA", windll["ISCSIDSC"]), ((1, 'BufferSize'),(1, 'MappingCount'),(1, 'Mappings'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetIScsiTunnelModeOuterAddressW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.BOOLEAN, use_last_error=False)(("SetIScsiTunnelModeOuterAddressW", windll["ISCSIDSC"]), ((1, 'InitiatorName'),(1, 'InitiatorPortNumber'),(1, 'DestinationAddress'),(1, 'OuterModeAddress'),(1, 'Persist'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetIScsiTunnelModeOuterAddress():
    return win32more.Storage.IscsiDisc.SetIScsiTunnelModeOuterAddressW
def _define_SetIScsiTunnelModeOuterAddressA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.BOOLEAN, use_last_error=False)(("SetIScsiTunnelModeOuterAddressA", windll["ISCSIDSC"]), ((1, 'InitiatorName'),(1, 'InitiatorPortNumber'),(1, 'DestinationAddress'),(1, 'OuterModeAddress'),(1, 'Persist'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetIScsiIKEInfoW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Storage.IscsiDisc.IKE_AUTHENTICATION_INFORMATION_head),win32more.Foundation.BOOLEAN, use_last_error=False)(("SetIScsiIKEInfoW", windll["ISCSIDSC"]), ((1, 'InitiatorName'),(1, 'InitiatorPortNumber'),(1, 'AuthInfo'),(1, 'Persist'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetIScsiIKEInfo():
    return win32more.Storage.IscsiDisc.SetIScsiIKEInfoW
def _define_SetIScsiIKEInfoA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,UInt32,POINTER(win32more.Storage.IscsiDisc.IKE_AUTHENTICATION_INFORMATION_head),win32more.Foundation.BOOLEAN, use_last_error=False)(("SetIScsiIKEInfoA", windll["ISCSIDSC"]), ((1, 'InitiatorName'),(1, 'InitiatorPortNumber'),(1, 'AuthInfo'),(1, 'Persist'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetIScsiIKEInfoW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32),POINTER(win32more.Storage.IscsiDisc.IKE_AUTHENTICATION_INFORMATION_head), use_last_error=False)(("GetIScsiIKEInfoW", windll["ISCSIDSC"]), ((1, 'InitiatorName'),(1, 'InitiatorPortNumber'),(1, 'Reserved'),(1, 'AuthInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetIScsiIKEInfo():
    return win32more.Storage.IscsiDisc.GetIScsiIKEInfoW
def _define_GetIScsiIKEInfoA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,UInt32,POINTER(UInt32),POINTER(win32more.Storage.IscsiDisc.IKE_AUTHENTICATION_INFORMATION_head), use_last_error=False)(("GetIScsiIKEInfoA", windll["ISCSIDSC"]), ((1, 'InitiatorName'),(1, 'InitiatorPortNumber'),(1, 'Reserved'),(1, 'AuthInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetIScsiGroupPresharedKey():
    try:
        return WINFUNCTYPE(UInt32,UInt32,c_char_p_no,win32more.Foundation.BOOLEAN, use_last_error=False)(("SetIScsiGroupPresharedKey", windll["ISCSIDSC"]), ((1, 'KeyLength'),(1, 'Key'),(1, 'Persist'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetIScsiInitiatorCHAPSharedSecret():
    try:
        return WINFUNCTYPE(UInt32,UInt32,c_char_p_no, use_last_error=False)(("SetIScsiInitiatorCHAPSharedSecret", windll["ISCSIDSC"]), ((1, 'SharedSecretLength'),(1, 'SharedSecret'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetIScsiInitiatorRADIUSSharedSecret():
    try:
        return WINFUNCTYPE(UInt32,UInt32,c_char_p_no, use_last_error=False)(("SetIScsiInitiatorRADIUSSharedSecret", windll["ISCSIDSC"]), ((1, 'SharedSecretLength'),(1, 'SharedSecret'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetIScsiInitiatorNodeNameW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR, use_last_error=False)(("SetIScsiInitiatorNodeNameW", windll["ISCSIDSC"]), ((1, 'InitiatorNodeName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetIScsiInitiatorNodeName():
    return win32more.Storage.IscsiDisc.SetIScsiInitiatorNodeNameW
def _define_SetIScsiInitiatorNodeNameA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR, use_last_error=False)(("SetIScsiInitiatorNodeNameA", windll["ISCSIDSC"]), ((1, 'InitiatorNodeName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetIScsiInitiatorNodeNameW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR, use_last_error=False)(("GetIScsiInitiatorNodeNameW", windll["ISCSIDSC"]), ((1, 'InitiatorNodeName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetIScsiInitiatorNodeName():
    return win32more.Storage.IscsiDisc.GetIScsiInitiatorNodeNameW
def _define_GetIScsiInitiatorNodeNameA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR, use_last_error=False)(("GetIScsiInitiatorNodeNameA", windll["ISCSIDSC"]), ((1, 'InitiatorNodeName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddISNSServerW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR, use_last_error=False)(("AddISNSServerW", windll["ISCSIDSC"]), ((1, 'Address'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddISNSServer():
    return win32more.Storage.IscsiDisc.AddISNSServerW
def _define_AddISNSServerA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR, use_last_error=False)(("AddISNSServerA", windll["ISCSIDSC"]), ((1, 'Address'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RemoveISNSServerW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR, use_last_error=False)(("RemoveISNSServerW", windll["ISCSIDSC"]), ((1, 'Address'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RemoveISNSServer():
    return win32more.Storage.IscsiDisc.RemoveISNSServerW
def _define_RemoveISNSServerA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR, use_last_error=False)(("RemoveISNSServerA", windll["ISCSIDSC"]), ((1, 'Address'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RefreshISNSServerW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR, use_last_error=False)(("RefreshISNSServerW", windll["ISCSIDSC"]), ((1, 'Address'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RefreshISNSServer():
    return win32more.Storage.IscsiDisc.RefreshISNSServerW
def _define_RefreshISNSServerA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR, use_last_error=False)(("RefreshISNSServerA", windll["ISCSIDSC"]), ((1, 'Address'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReportISNSServerListW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),POINTER(Char), use_last_error=False)(("ReportISNSServerListW", windll["ISCSIDSC"]), ((1, 'BufferSizeInChar'),(1, 'Buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReportISNSServerList():
    return win32more.Storage.IscsiDisc.ReportISNSServerListW
def _define_ReportISNSServerListA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),POINTER(Byte), use_last_error=False)(("ReportISNSServerListA", windll["ISCSIDSC"]), ((1, 'BufferSizeInChar'),(1, 'Buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetIScsiSessionListW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(win32more.Storage.IscsiDisc.ISCSI_SESSION_INFOW_head), use_last_error=False)(("GetIScsiSessionListW", windll["ISCSIDSC"]), ((1, 'BufferSize'),(1, 'SessionCount'),(1, 'SessionInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetIScsiSessionList():
    return win32more.Storage.IscsiDisc.GetIScsiSessionListW
def _define_GetIScsiSessionListA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(win32more.Storage.IscsiDisc.ISCSI_SESSION_INFOA_head), use_last_error=False)(("GetIScsiSessionListA", windll["ISCSIDSC"]), ((1, 'BufferSize'),(1, 'SessionCount'),(1, 'SessionInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetIScsiSessionListEx():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(win32more.Storage.IscsiDisc.ISCSI_SESSION_INFO_EX_head), use_last_error=False)(("GetIScsiSessionListEx", windll["ISCSIDSC"]), ((1, 'BufferSize'),(1, 'SessionCountPtr'),(1, 'SessionInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDevicesForIScsiSessionW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID_head),POINTER(UInt32),POINTER(win32more.Storage.IscsiDisc.ISCSI_DEVICE_ON_SESSIONW_head), use_last_error=False)(("GetDevicesForIScsiSessionW", windll["ISCSIDSC"]), ((1, 'UniqueSessionId'),(1, 'DeviceCount'),(1, 'Devices'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDevicesForIScsiSession():
    return win32more.Storage.IscsiDisc.GetDevicesForIScsiSessionW
def _define_GetDevicesForIScsiSessionA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID_head),POINTER(UInt32),POINTER(win32more.Storage.IscsiDisc.ISCSI_DEVICE_ON_SESSIONA_head), use_last_error=False)(("GetDevicesForIScsiSessionA", windll["ISCSIDSC"]), ((1, 'UniqueSessionId'),(1, 'DeviceCount'),(1, 'Devices'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetupPersistentIScsiVolumes():
    try:
        return WINFUNCTYPE(UInt32, use_last_error=False)(("SetupPersistentIScsiVolumes", windll["ISCSIDSC"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetupPersistentIScsiDevices():
    try:
        return WINFUNCTYPE(UInt32, use_last_error=False)(("SetupPersistentIScsiDevices", windll["ISCSIDSC"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddPersistentIScsiDeviceW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR, use_last_error=False)(("AddPersistentIScsiDeviceW", windll["ISCSIDSC"]), ((1, 'DevicePath'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddPersistentIScsiDevice():
    return win32more.Storage.IscsiDisc.AddPersistentIScsiDeviceW
def _define_AddPersistentIScsiDeviceA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR, use_last_error=False)(("AddPersistentIScsiDeviceA", windll["ISCSIDSC"]), ((1, 'DevicePath'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RemovePersistentIScsiDeviceW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR, use_last_error=False)(("RemovePersistentIScsiDeviceW", windll["ISCSIDSC"]), ((1, 'DevicePath'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RemovePersistentIScsiDevice():
    return win32more.Storage.IscsiDisc.RemovePersistentIScsiDeviceW
def _define_RemovePersistentIScsiDeviceA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR, use_last_error=False)(("RemovePersistentIScsiDeviceA", windll["ISCSIDSC"]), ((1, 'DevicePath'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ClearPersistentIScsiDevices():
    try:
        return WINFUNCTYPE(UInt32, use_last_error=False)(("ClearPersistentIScsiDevices", windll["ISCSIDSC"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReportPersistentIScsiDevicesW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),POINTER(Char), use_last_error=False)(("ReportPersistentIScsiDevicesW", windll["ISCSIDSC"]), ((1, 'BufferSizeInChar'),(1, 'Buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReportPersistentIScsiDevices():
    return win32more.Storage.IscsiDisc.ReportPersistentIScsiDevicesW
def _define_ReportPersistentIScsiDevicesA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),POINTER(Byte), use_last_error=False)(("ReportPersistentIScsiDevicesA", windll["ISCSIDSC"]), ((1, 'BufferSizeInChar'),(1, 'Buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReportIScsiTargetPortalsW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt16),POINTER(UInt32),POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTALW_head), use_last_error=False)(("ReportIScsiTargetPortalsW", windll["ISCSIDSC"]), ((1, 'InitiatorName'),(1, 'TargetName'),(1, 'TargetPortalTag'),(1, 'ElementCount'),(1, 'Portals'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReportIScsiTargetPortals():
    return win32more.Storage.IscsiDisc.ReportIScsiTargetPortalsW
def _define_ReportIScsiTargetPortalsA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(UInt16),POINTER(UInt32),POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTALA_head), use_last_error=False)(("ReportIScsiTargetPortalsA", windll["ISCSIDSC"]), ((1, 'InitiatorName'),(1, 'TargetName'),(1, 'TargetPortalTag'),(1, 'ElementCount'),(1, 'Portals'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddRadiusServerW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR, use_last_error=False)(("AddRadiusServerW", windll["ISCSIDSC"]), ((1, 'Address'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddRadiusServer():
    return win32more.Storage.IscsiDisc.AddRadiusServerW
def _define_AddRadiusServerA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR, use_last_error=False)(("AddRadiusServerA", windll["ISCSIDSC"]), ((1, 'Address'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RemoveRadiusServerW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR, use_last_error=False)(("RemoveRadiusServerW", windll["ISCSIDSC"]), ((1, 'Address'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RemoveRadiusServer():
    return win32more.Storage.IscsiDisc.RemoveRadiusServerW
def _define_RemoveRadiusServerA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR, use_last_error=False)(("RemoveRadiusServerA", windll["ISCSIDSC"]), ((1, 'Address'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReportRadiusServerListW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),POINTER(Char), use_last_error=False)(("ReportRadiusServerListW", windll["ISCSIDSC"]), ((1, 'BufferSizeInChar'),(1, 'Buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReportRadiusServerList():
    return win32more.Storage.IscsiDisc.ReportRadiusServerListW
def _define_ReportRadiusServerListA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),POINTER(Byte), use_last_error=False)(("ReportRadiusServerListA", windll["ISCSIDSC"]), ((1, 'BufferSizeInChar'),(1, 'Buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "IOCTL_SCSI_BASE",
    "ScsiRawInterfaceGuid",
    "WmiScsiAddressGuid",
    "FILE_DEVICE_SCSI",
    "IOCTL_SCSI_PASS_THROUGH",
    "IOCTL_SCSI_MINIPORT",
    "IOCTL_SCSI_GET_INQUIRY_DATA",
    "IOCTL_SCSI_GET_CAPABILITIES",
    "IOCTL_SCSI_PASS_THROUGH_DIRECT",
    "IOCTL_SCSI_GET_ADDRESS",
    "IOCTL_SCSI_RESCAN_BUS",
    "IOCTL_SCSI_GET_DUMP_POINTERS",
    "IOCTL_SCSI_FREE_DUMP_POINTERS",
    "IOCTL_IDE_PASS_THROUGH",
    "IOCTL_ATA_PASS_THROUGH",
    "IOCTL_ATA_PASS_THROUGH_DIRECT",
    "IOCTL_ATA_MINIPORT",
    "IOCTL_MINIPORT_PROCESS_SERVICE_IRP",
    "IOCTL_MPIO_PASS_THROUGH_PATH",
    "IOCTL_MPIO_PASS_THROUGH_PATH_DIRECT",
    "IOCTL_SCSI_PASS_THROUGH_EX",
    "IOCTL_SCSI_PASS_THROUGH_DIRECT_EX",
    "IOCTL_MPIO_PASS_THROUGH_PATH_EX",
    "IOCTL_MPIO_PASS_THROUGH_PATH_DIRECT_EX",
    "ATA_FLAGS_DRDY_REQUIRED",
    "ATA_FLAGS_DATA_IN",
    "ATA_FLAGS_DATA_OUT",
    "ATA_FLAGS_48BIT_COMMAND",
    "ATA_FLAGS_USE_DMA",
    "ATA_FLAGS_NO_MULTIPLE",
    "NRB_FUNCTION_NVCACHE_INFO",
    "NRB_FUNCTION_SPINDLE_STATUS",
    "NRB_FUNCTION_NVCACHE_POWER_MODE_SET",
    "NRB_FUNCTION_NVCACHE_POWER_MODE_RETURN",
    "NRB_FUNCTION_FLUSH_NVCACHE",
    "NRB_FUNCTION_QUERY_PINNED_SET",
    "NRB_FUNCTION_QUERY_CACHE_MISS",
    "NRB_FUNCTION_ADD_LBAS_PINNED_SET",
    "NRB_FUNCTION_REMOVE_LBAS_PINNED_SET",
    "NRB_FUNCTION_QUERY_ASCENDER_STATUS",
    "NRB_FUNCTION_QUERY_HYBRID_DISK_STATUS",
    "NRB_FUNCTION_PASS_HINT_PAYLOAD",
    "NRB_FUNCTION_NVSEPARATED_INFO",
    "NRB_FUNCTION_NVSEPARATED_FLUSH",
    "NRB_FUNCTION_NVSEPARATED_WB_DISABLE",
    "NRB_FUNCTION_NVSEPARATED_WB_REVERT_DEFAULT",
    "NRB_SUCCESS",
    "NRB_ILLEGAL_REQUEST",
    "NRB_INVALID_PARAMETER",
    "NRB_INPUT_DATA_OVERRUN",
    "NRB_INPUT_DATA_UNDERRUN",
    "NRB_OUTPUT_DATA_OVERRUN",
    "NRB_OUTPUT_DATA_UNDERRUN",
    "NV_SEP_CACHE_PARAMETER_VERSION_1",
    "NV_SEP_CACHE_PARAMETER_VERSION",
    "STORAGE_DIAGNOSTIC_STATUS_SUCCESS",
    "STORAGE_DIAGNOSTIC_STATUS_BUFFER_TOO_SMALL",
    "STORAGE_DIAGNOSTIC_STATUS_UNSUPPORTED_VERSION",
    "STORAGE_DIAGNOSTIC_STATUS_INVALID_PARAMETER",
    "STORAGE_DIAGNOSTIC_STATUS_INVALID_SIGNATURE",
    "STORAGE_DIAGNOSTIC_STATUS_INVALID_TARGET_TYPE",
    "STORAGE_DIAGNOSTIC_STATUS_MORE_DATA",
    "MINIPORT_DSM_NOTIFICATION_VERSION_1",
    "MINIPORT_DSM_NOTIFICATION_VERSION",
    "MINIPORT_DSM_PROFILE_UNKNOWN",
    "MINIPORT_DSM_PROFILE_PAGE_FILE",
    "MINIPORT_DSM_PROFILE_HIBERNATION_FILE",
    "MINIPORT_DSM_PROFILE_CRASHDUMP_FILE",
    "MINIPORT_DSM_NOTIFY_FLAG_BEGIN",
    "MINIPORT_DSM_NOTIFY_FLAG_END",
    "HYBRID_FUNCTION_GET_INFO",
    "HYBRID_FUNCTION_DISABLE_CACHING_MEDIUM",
    "HYBRID_FUNCTION_ENABLE_CACHING_MEDIUM",
    "HYBRID_FUNCTION_SET_DIRTY_THRESHOLD",
    "HYBRID_FUNCTION_DEMOTE_BY_SIZE",
    "HYBRID_STATUS_SUCCESS",
    "HYBRID_STATUS_ILLEGAL_REQUEST",
    "HYBRID_STATUS_INVALID_PARAMETER",
    "HYBRID_STATUS_OUTPUT_BUFFER_TOO_SMALL",
    "HYBRID_STATUS_ENABLE_REFCOUNT_HOLD",
    "HYBRID_REQUEST_BLOCK_STRUCTURE_VERSION",
    "HYBRID_REQUEST_INFO_STRUCTURE_VERSION",
    "FIRMWARE_FUNCTION_GET_INFO",
    "FIRMWARE_FUNCTION_DOWNLOAD",
    "FIRMWARE_FUNCTION_ACTIVATE",
    "FIRMWARE_STATUS_SUCCESS",
    "FIRMWARE_STATUS_ERROR",
    "FIRMWARE_STATUS_ILLEGAL_REQUEST",
    "FIRMWARE_STATUS_INVALID_PARAMETER",
    "FIRMWARE_STATUS_INPUT_BUFFER_TOO_BIG",
    "FIRMWARE_STATUS_OUTPUT_BUFFER_TOO_SMALL",
    "FIRMWARE_STATUS_INVALID_SLOT",
    "FIRMWARE_STATUS_INVALID_IMAGE",
    "FIRMWARE_STATUS_CONTROLLER_ERROR",
    "FIRMWARE_STATUS_POWER_CYCLE_REQUIRED",
    "FIRMWARE_STATUS_DEVICE_ERROR",
    "FIRMWARE_STATUS_INTERFACE_CRC_ERROR",
    "FIRMWARE_STATUS_UNCORRECTABLE_DATA_ERROR",
    "FIRMWARE_STATUS_MEDIA_CHANGE",
    "FIRMWARE_STATUS_ID_NOT_FOUND",
    "FIRMWARE_STATUS_MEDIA_CHANGE_REQUEST",
    "FIRMWARE_STATUS_COMMAND_ABORT",
    "FIRMWARE_STATUS_END_OF_MEDIA",
    "FIRMWARE_STATUS_ILLEGAL_LENGTH",
    "FIRMWARE_REQUEST_BLOCK_STRUCTURE_VERSION",
    "FIRMWARE_REQUEST_FLAG_CONTROLLER",
    "FIRMWARE_REQUEST_FLAG_LAST_SEGMENT",
    "FIRMWARE_REQUEST_FLAG_FIRST_SEGMENT",
    "FIRMWARE_REQUEST_FLAG_SWITCH_TO_EXISTING_FIRMWARE",
    "STORAGE_FIRMWARE_INFO_STRUCTURE_VERSION",
    "STORAGE_FIRMWARE_INFO_STRUCTURE_VERSION_V2",
    "STORAGE_FIRMWARE_INFO_INVALID_SLOT",
    "STORAGE_FIRMWARE_SLOT_INFO_V2_REVISION_LENGTH",
    "STORAGE_FIRMWARE_DOWNLOAD_STRUCTURE_VERSION",
    "STORAGE_FIRMWARE_DOWNLOAD_STRUCTURE_VERSION_V2",
    "STORAGE_FIRMWARE_ACTIVATE_STRUCTURE_VERSION",
    "DUMP_POINTERS_VERSION_1",
    "DUMP_POINTERS_VERSION_2",
    "DUMP_POINTERS_VERSION_3",
    "DUMP_POINTERS_VERSION_4",
    "DUMP_DRIVER_NAME_LENGTH",
    "DUMP_EX_FLAG_SUPPORT_64BITMEMORY",
    "DUMP_EX_FLAG_SUPPORT_DD_TELEMETRY",
    "DUMP_EX_FLAG_RESUME_SUPPORT",
    "DUMP_EX_FLAG_DRIVER_FULL_PATH_SUPPORT",
    "SCSI_IOCTL_DATA_OUT",
    "SCSI_IOCTL_DATA_IN",
    "SCSI_IOCTL_DATA_UNSPECIFIED",
    "SCSI_IOCTL_DATA_BIDIRECTIONAL",
    "MPIO_IOCTL_FLAG_USE_PATHID",
    "MPIO_IOCTL_FLAG_USE_SCSIADDRESS",
    "MPIO_IOCTL_FLAG_INVOLVE_DSM",
    "MAX_ISCSI_HBANAME_LEN",
    "MAX_ISCSI_NAME_LEN",
    "MAX_ISCSI_ALIAS_LEN",
    "MAX_ISCSI_PORTAL_NAME_LEN",
    "MAX_ISCSI_PORTAL_ALIAS_LEN",
    "MAX_ISCSI_TEXT_ADDRESS_LEN",
    "MAX_ISCSI_PORTAL_ADDRESS_LEN",
    "MAX_ISCSI_DISCOVERY_DOMAIN_LEN",
    "MAX_RADIUS_ADDRESS_LEN",
    "ISCSI_SECURITY_FLAG_TUNNEL_MODE_PREFERRED",
    "ISCSI_SECURITY_FLAG_TRANSPORT_MODE_PREFERRED",
    "ISCSI_SECURITY_FLAG_PFS_ENABLED",
    "ISCSI_SECURITY_FLAG_AGGRESSIVE_MODE_ENABLED",
    "ISCSI_SECURITY_FLAG_MAIN_MODE_ENABLED",
    "ISCSI_SECURITY_FLAG_IKE_IPSEC_ENABLED",
    "ISCSI_SECURITY_FLAG_VALID",
    "ISCSI_LOGIN_FLAG_REQUIRE_IPSEC",
    "ISCSI_LOGIN_FLAG_MULTIPATH_ENABLED",
    "ISCSI_LOGIN_FLAG_RESERVED1",
    "ISCSI_LOGIN_FLAG_ALLOW_PORTAL_HOPPING",
    "ISCSI_LOGIN_FLAG_USE_RADIUS_RESPONSE",
    "ISCSI_LOGIN_FLAG_USE_RADIUS_VERIFICATION",
    "ISCSI_LOGIN_OPTIONS_HEADER_DIGEST",
    "ISCSI_LOGIN_OPTIONS_DATA_DIGEST",
    "ISCSI_LOGIN_OPTIONS_MAXIMUM_CONNECTIONS",
    "ISCSI_LOGIN_OPTIONS_DEFAULT_TIME_2_WAIT",
    "ISCSI_LOGIN_OPTIONS_DEFAULT_TIME_2_RETAIN",
    "ISCSI_LOGIN_OPTIONS_USERNAME",
    "ISCSI_LOGIN_OPTIONS_PASSWORD",
    "ISCSI_LOGIN_OPTIONS_AUTH_TYPE",
    "ISCSI_LOGIN_OPTIONS_VERSION",
    "ISCSI_TARGET_FLAG_HIDE_STATIC_TARGET",
    "ISCSI_TARGET_FLAG_MERGE_TARGET_INFORMATION",
    "ID_IPV4_ADDR",
    "ID_FQDN",
    "ID_USER_FQDN",
    "ID_IPV6_ADDR",
    "_ADAPTER_OBJECT",
    "SCSI_PASS_THROUGH",
    "SCSI_PASS_THROUGH_DIRECT",
    "SCSI_PASS_THROUGH32",
    "SCSI_PASS_THROUGH_DIRECT32",
    "SCSI_PASS_THROUGH_EX",
    "SCSI_PASS_THROUGH_DIRECT_EX",
    "SCSI_PASS_THROUGH32_EX",
    "SCSI_PASS_THROUGH_DIRECT32_EX",
    "ATA_PASS_THROUGH_EX",
    "ATA_PASS_THROUGH_DIRECT",
    "ATA_PASS_THROUGH_EX32",
    "ATA_PASS_THROUGH_DIRECT32",
    "IDE_IO_CONTROL",
    "MPIO_PASS_THROUGH_PATH",
    "MPIO_PASS_THROUGH_PATH_DIRECT",
    "MPIO_PASS_THROUGH_PATH_EX",
    "MPIO_PASS_THROUGH_PATH_DIRECT_EX",
    "MPIO_PASS_THROUGH_PATH32",
    "MPIO_PASS_THROUGH_PATH_DIRECT32",
    "MPIO_PASS_THROUGH_PATH32_EX",
    "MPIO_PASS_THROUGH_PATH_DIRECT32_EX",
    "SCSI_BUS_DATA",
    "SCSI_ADAPTER_BUS_INFO",
    "SCSI_INQUIRY_DATA",
    "SRB_IO_CONTROL",
    "NVCACHE_REQUEST_BLOCK",
    "NV_FEATURE_PARAMETER",
    "NVCACHE_HINT_PAYLOAD",
    "NV_SEP_CACHE_PARAMETER",
    "NV_SEP_WRITE_CACHE_TYPE",
    "NV_SEP_WRITE_CACHE_TYPE_NVSEPWriteCacheTypeUnknown",
    "NV_SEP_WRITE_CACHE_TYPE_NVSEPWriteCacheTypeNone",
    "NV_SEP_WRITE_CACHE_TYPE_NVSEPWriteCacheTypeWriteBack",
    "NV_SEP_WRITE_CACHE_TYPE_NVSEPWriteCacheTypeWriteThrough",
    "MP_STORAGE_DIAGNOSTIC_LEVEL",
    "MP_STORAGE_DIAGNOSTIC_LEVEL_MpStorageDiagnosticLevelDefault",
    "MP_STORAGE_DIAGNOSTIC_LEVEL_MpStorageDiagnosticLevelMax",
    "MP_STORAGE_DIAGNOSTIC_TARGET_TYPE",
    "MP_STORAGE_DIAGNOSTIC_TARGET_TYPE_MpStorageDiagnosticTargetTypeUndefined",
    "MP_STORAGE_DIAGNOSTIC_TARGET_TYPE_MpStorageDiagnosticTargetTypeMiniport",
    "MP_STORAGE_DIAGNOSTIC_TARGET_TYPE_MpStorageDiagnosticTargetTypeHbaFirmware",
    "MP_STORAGE_DIAGNOSTIC_TARGET_TYPE_MpStorageDiagnosticTargetTypeMax",
    "STORAGE_DIAGNOSTIC_MP_REQUEST",
    "MP_DEVICE_DATA_SET_RANGE",
    "DSM_NOTIFICATION_REQUEST_BLOCK",
    "HYBRID_REQUEST_BLOCK",
    "NVCACHE_TYPE",
    "NVCACHE_TYPE_NvCacheTypeUnknown",
    "NVCACHE_TYPE_NvCacheTypeNone",
    "NVCACHE_TYPE_NvCacheTypeWriteBack",
    "NVCACHE_TYPE_NvCacheTypeWriteThrough",
    "NVCACHE_STATUS",
    "NVCACHE_STATUS_NvCacheStatusUnknown",
    "NVCACHE_STATUS_NvCacheStatusDisabling",
    "NVCACHE_STATUS_NvCacheStatusDisabled",
    "NVCACHE_STATUS_NvCacheStatusEnabled",
    "NVCACHE_PRIORITY_LEVEL_DESCRIPTOR",
    "HYBRID_INFORMATION",
    "HYBRID_DIRTY_THRESHOLDS",
    "HYBRID_DEMOTE_BY_SIZE",
    "FIRMWARE_REQUEST_BLOCK",
    "STORAGE_FIRMWARE_SLOT_INFO",
    "STORAGE_FIRMWARE_SLOT_INFO_V2",
    "STORAGE_FIRMWARE_INFO",
    "STORAGE_FIRMWARE_INFO_V2",
    "STORAGE_FIRMWARE_DOWNLOAD",
    "STORAGE_FIRMWARE_DOWNLOAD_V2",
    "STORAGE_FIRMWARE_ACTIVATE",
    "IO_SCSI_CAPABILITIES",
    "SCSI_ADDRESS",
    "DUMP_DEVICE_POWERON_ROUTINE",
    "PDUMP_DEVICE_POWERON_ROUTINE",
    "DUMP_POINTERS_VERSION",
    "DUMP_POINTERS",
    "DUMP_POINTERS_EX",
    "DUMP_DRIVER",
    "NTSCSI_UNICODE_STRING",
    "DUMP_DRIVER_EX",
    "STORAGE_ENDURANCE_INFO",
    "STORAGE_ENDURANCE_DATA_DESCRIPTOR",
    "ISCSI_DIGEST_TYPES",
    "ISCSI_DIGEST_TYPE_NONE",
    "ISCSI_DIGEST_TYPE_CRC32C",
    "ISCSI_AUTH_TYPES",
    "ISCSI_NO_AUTH_TYPE",
    "ISCSI_CHAP_AUTH_TYPE",
    "ISCSI_MUTUAL_CHAP_AUTH_TYPE",
    "ISCSI_LOGIN_OPTIONS",
    "IKE_AUTHENTICATION_METHOD",
    "IKE_AUTHENTICATION_PRESHARED_KEY_METHOD",
    "IKE_AUTHENTICATION_PRESHARED_KEY",
    "IKE_AUTHENTICATION_INFORMATION",
    "ISCSI_UNIQUE_SESSION_ID",
    "SCSI_LUN_LIST",
    "ISCSI_TARGET_MAPPINGW",
    "ISCSI_TARGET_MAPPINGA",
    "ISCSI_TARGET_PORTALW",
    "ISCSI_TARGET_PORTALA",
    "ISCSI_TARGET_PORTAL_INFOW",
    "ISCSI_TARGET_PORTAL_INFOA",
    "ISCSI_TARGET_PORTAL_INFO_EXW",
    "ISCSI_TARGET_PORTAL_INFO_EXA",
    "ISCSI_TARGET_PORTAL_GROUPW",
    "ISCSI_TARGET_PORTAL_GROUPA",
    "ISCSI_CONNECTION_INFOW",
    "ISCSI_SESSION_INFOW",
    "ISCSI_CONNECTION_INFOA",
    "ISCSI_SESSION_INFOA",
    "ISCSI_CONNECTION_INFO_EX",
    "ISCSI_SESSION_INFO_EX",
    "ISCSI_DEVICE_ON_SESSIONW",
    "ISCSI_DEVICE_ON_SESSIONA",
    "PERSISTENT_ISCSI_LOGIN_INFOW",
    "PERSISTENT_ISCSI_LOGIN_INFOA",
    "TARGETPROTOCOLTYPE",
    "ISCSI_TCP_PROTOCOL_TYPE",
    "TARGET_INFORMATION_CLASS",
    "TARGET_INFORMATION_CLASS_ProtocolType",
    "TARGET_INFORMATION_CLASS_TargetAlias",
    "TARGET_INFORMATION_CLASS_DiscoveryMechanisms",
    "TARGET_INFORMATION_CLASS_PortalGroups",
    "TARGET_INFORMATION_CLASS_PersistentTargetMappings",
    "TARGET_INFORMATION_CLASS_InitiatorName",
    "TARGET_INFORMATION_CLASS_TargetFlags",
    "TARGET_INFORMATION_CLASS_LoginOptions",
    "ISCSI_VERSION_INFO",
    "GetIScsiVersionInformation",
    "GetIScsiTargetInformationW",
    "GetIScsiTargetInformation",
    "GetIScsiTargetInformationA",
    "AddIScsiConnectionW",
    "AddIScsiConnection",
    "AddIScsiConnectionA",
    "RemoveIScsiConnection",
    "ReportIScsiTargetsW",
    "ReportIScsiTargets",
    "ReportIScsiTargetsA",
    "AddIScsiStaticTargetW",
    "AddIScsiStaticTarget",
    "AddIScsiStaticTargetA",
    "RemoveIScsiStaticTargetW",
    "RemoveIScsiStaticTarget",
    "RemoveIScsiStaticTargetA",
    "AddIScsiSendTargetPortalW",
    "AddIScsiSendTargetPortal",
    "AddIScsiSendTargetPortalA",
    "RemoveIScsiSendTargetPortalW",
    "RemoveIScsiSendTargetPortal",
    "RemoveIScsiSendTargetPortalA",
    "RefreshIScsiSendTargetPortalW",
    "RefreshIScsiSendTargetPortal",
    "RefreshIScsiSendTargetPortalA",
    "ReportIScsiSendTargetPortalsW",
    "ReportIScsiSendTargetPortals",
    "ReportIScsiSendTargetPortalsA",
    "ReportIScsiSendTargetPortalsExW",
    "ReportIScsiSendTargetPortalsEx",
    "ReportIScsiSendTargetPortalsExA",
    "LoginIScsiTargetW",
    "LoginIScsiTarget",
    "LoginIScsiTargetA",
    "ReportIScsiPersistentLoginsW",
    "ReportIScsiPersistentLogins",
    "ReportIScsiPersistentLoginsA",
    "LogoutIScsiTarget",
    "RemoveIScsiPersistentTargetW",
    "RemoveIScsiPersistentTarget",
    "RemoveIScsiPersistentTargetA",
    "SendScsiInquiry",
    "SendScsiReadCapacity",
    "SendScsiReportLuns",
    "ReportIScsiInitiatorListW",
    "ReportIScsiInitiatorList",
    "ReportIScsiInitiatorListA",
    "ReportActiveIScsiTargetMappingsW",
    "ReportActiveIScsiTargetMappings",
    "ReportActiveIScsiTargetMappingsA",
    "SetIScsiTunnelModeOuterAddressW",
    "SetIScsiTunnelModeOuterAddress",
    "SetIScsiTunnelModeOuterAddressA",
    "SetIScsiIKEInfoW",
    "SetIScsiIKEInfo",
    "SetIScsiIKEInfoA",
    "GetIScsiIKEInfoW",
    "GetIScsiIKEInfo",
    "GetIScsiIKEInfoA",
    "SetIScsiGroupPresharedKey",
    "SetIScsiInitiatorCHAPSharedSecret",
    "SetIScsiInitiatorRADIUSSharedSecret",
    "SetIScsiInitiatorNodeNameW",
    "SetIScsiInitiatorNodeName",
    "SetIScsiInitiatorNodeNameA",
    "GetIScsiInitiatorNodeNameW",
    "GetIScsiInitiatorNodeName",
    "GetIScsiInitiatorNodeNameA",
    "AddISNSServerW",
    "AddISNSServer",
    "AddISNSServerA",
    "RemoveISNSServerW",
    "RemoveISNSServer",
    "RemoveISNSServerA",
    "RefreshISNSServerW",
    "RefreshISNSServer",
    "RefreshISNSServerA",
    "ReportISNSServerListW",
    "ReportISNSServerList",
    "ReportISNSServerListA",
    "GetIScsiSessionListW",
    "GetIScsiSessionList",
    "GetIScsiSessionListA",
    "GetIScsiSessionListEx",
    "GetDevicesForIScsiSessionW",
    "GetDevicesForIScsiSession",
    "GetDevicesForIScsiSessionA",
    "SetupPersistentIScsiVolumes",
    "SetupPersistentIScsiDevices",
    "AddPersistentIScsiDeviceW",
    "AddPersistentIScsiDevice",
    "AddPersistentIScsiDeviceA",
    "RemovePersistentIScsiDeviceW",
    "RemovePersistentIScsiDevice",
    "RemovePersistentIScsiDeviceA",
    "ClearPersistentIScsiDevices",
    "ReportPersistentIScsiDevicesW",
    "ReportPersistentIScsiDevices",
    "ReportPersistentIScsiDevicesA",
    "ReportIScsiTargetPortalsW",
    "ReportIScsiTargetPortals",
    "ReportIScsiTargetPortalsA",
    "AddRadiusServerW",
    "AddRadiusServer",
    "AddRadiusServerA",
    "RemoveRadiusServerW",
    "RemoveRadiusServer",
    "RemoveRadiusServerA",
    "ReportRadiusServerListW",
    "ReportRadiusServerList",
    "ReportRadiusServerListA",
]
