from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Storage.IscsiDisc
import win32more.System.Ioctl
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
class ATA_PASS_THROUGH_DIRECT(Structure):
    Length: UInt16
    AtaFlags: UInt16
    PathId: Byte
    TargetId: Byte
    Lun: Byte
    ReservedAsUchar: Byte
    DataTransferLength: UInt32
    TimeOutValue: UInt32
    ReservedAsUlong: UInt32
    DataBuffer: c_void_p
    PreviousTaskFile: Byte * 8
    CurrentTaskFile: Byte * 8
if ARCH in 'X64,ARM64':
    class ATA_PASS_THROUGH_DIRECT32(Structure):
        Length: UInt16
        AtaFlags: UInt16
        PathId: Byte
        TargetId: Byte
        Lun: Byte
        ReservedAsUchar: Byte
        DataTransferLength: UInt32
        TimeOutValue: UInt32
        ReservedAsUlong: UInt32
        DataBuffer: c_void_p
        PreviousTaskFile: Byte * 8
        CurrentTaskFile: Byte * 8
class ATA_PASS_THROUGH_EX(Structure):
    Length: UInt16
    AtaFlags: UInt16
    PathId: Byte
    TargetId: Byte
    Lun: Byte
    ReservedAsUchar: Byte
    DataTransferLength: UInt32
    TimeOutValue: UInt32
    ReservedAsUlong: UInt32
    DataBufferOffset: UIntPtr
    PreviousTaskFile: Byte * 8
    CurrentTaskFile: Byte * 8
if ARCH in 'X64,ARM64':
    class ATA_PASS_THROUGH_EX32(Structure):
        Length: UInt16
        AtaFlags: UInt16
        PathId: Byte
        TargetId: Byte
        Lun: Byte
        ReservedAsUchar: Byte
        DataTransferLength: UInt32
        TimeOutValue: UInt32
        ReservedAsUlong: UInt32
        DataBufferOffset: UInt32
        PreviousTaskFile: Byte * 8
        CurrentTaskFile: Byte * 8
IOCTL_SCSI_BASE: UInt32 = 4
ScsiRawInterfaceGuid: Guid = Guid('53f56309-b6bf-11d0-94-f2-00-a0-c9-1e-fb-8b')
WmiScsiAddressGuid: Guid = Guid('53f5630f-b6bf-11d0-94-f2-00-a0-c9-1e-fb-8b')
FILE_DEVICE_SCSI: UInt32 = 27
DD_SCSI_DEVICE_NAME: String = '\\Device\\ScsiPort'
IOCTL_SCSI_PASS_THROUGH: UInt32 = 315396
IOCTL_SCSI_MINIPORT: UInt32 = 315400
IOCTL_SCSI_GET_INQUIRY_DATA: UInt32 = 266252
IOCTL_SCSI_GET_CAPABILITIES: UInt32 = 266256
IOCTL_SCSI_PASS_THROUGH_DIRECT: UInt32 = 315412
IOCTL_SCSI_GET_ADDRESS: UInt32 = 266264
IOCTL_SCSI_RESCAN_BUS: UInt32 = 266268
IOCTL_SCSI_GET_DUMP_POINTERS: UInt32 = 266272
IOCTL_SCSI_FREE_DUMP_POINTERS: UInt32 = 266276
IOCTL_IDE_PASS_THROUGH: UInt32 = 315432
IOCTL_ATA_PASS_THROUGH: UInt32 = 315436
IOCTL_ATA_PASS_THROUGH_DIRECT: UInt32 = 315440
IOCTL_ATA_MINIPORT: UInt32 = 315444
IOCTL_MINIPORT_PROCESS_SERVICE_IRP: UInt32 = 315448
IOCTL_MPIO_PASS_THROUGH_PATH: UInt32 = 315452
IOCTL_MPIO_PASS_THROUGH_PATH_DIRECT: UInt32 = 315456
IOCTL_SCSI_PASS_THROUGH_EX: UInt32 = 315460
IOCTL_SCSI_PASS_THROUGH_DIRECT_EX: UInt32 = 315464
IOCTL_MPIO_PASS_THROUGH_PATH_EX: UInt32 = 315468
IOCTL_MPIO_PASS_THROUGH_PATH_DIRECT_EX: UInt32 = 315472
ATA_FLAGS_DRDY_REQUIRED: UInt32 = 1
ATA_FLAGS_DATA_IN: UInt32 = 2
ATA_FLAGS_DATA_OUT: UInt32 = 4
ATA_FLAGS_48BIT_COMMAND: UInt32 = 8
ATA_FLAGS_USE_DMA: UInt32 = 16
ATA_FLAGS_NO_MULTIPLE: UInt32 = 32
IOCTL_MINIPORT_SIGNATURE_SCSIDISK: String = 'SCSIDISK'
IOCTL_MINIPORT_SIGNATURE_HYBRDISK: String = 'HYBRDISK'
IOCTL_MINIPORT_SIGNATURE_DSM_NOTIFICATION: String = 'MPDSM   '
IOCTL_MINIPORT_SIGNATURE_DSM_GENERAL: String = 'MPDSMGEN'
IOCTL_MINIPORT_SIGNATURE_FIRMWARE: String = 'FIRMWARE'
IOCTL_MINIPORT_SIGNATURE_QUERY_PROTOCOL: String = 'PROTOCOL'
IOCTL_MINIPORT_SIGNATURE_SET_PROTOCOL: String = 'SETPROTO'
IOCTL_MINIPORT_SIGNATURE_QUERY_TEMPERATURE: String = 'TEMPERAT'
IOCTL_MINIPORT_SIGNATURE_SET_TEMPERATURE_THRESHOLD: String = 'SETTEMPT'
IOCTL_MINIPORT_SIGNATURE_QUERY_PHYSICAL_TOPOLOGY: String = 'TOPOLOGY'
IOCTL_MINIPORT_SIGNATURE_ENDURANCE_INFO: String = 'ENDURINF'
NRB_FUNCTION_NVCACHE_INFO: UInt32 = 236
NRB_FUNCTION_SPINDLE_STATUS: UInt32 = 229
NRB_FUNCTION_NVCACHE_POWER_MODE_SET: UInt32 = 0
NRB_FUNCTION_NVCACHE_POWER_MODE_RETURN: UInt32 = 1
NRB_FUNCTION_FLUSH_NVCACHE: UInt32 = 20
NRB_FUNCTION_QUERY_PINNED_SET: UInt32 = 18
NRB_FUNCTION_QUERY_CACHE_MISS: UInt32 = 19
NRB_FUNCTION_ADD_LBAS_PINNED_SET: UInt32 = 16
NRB_FUNCTION_REMOVE_LBAS_PINNED_SET: UInt32 = 17
NRB_FUNCTION_QUERY_ASCENDER_STATUS: UInt32 = 208
NRB_FUNCTION_QUERY_HYBRID_DISK_STATUS: UInt32 = 209
NRB_FUNCTION_PASS_HINT_PAYLOAD: UInt32 = 224
NRB_FUNCTION_NVSEPARATED_INFO: UInt32 = 192
NRB_FUNCTION_NVSEPARATED_FLUSH: UInt32 = 193
NRB_FUNCTION_NVSEPARATED_WB_DISABLE: UInt32 = 194
NRB_FUNCTION_NVSEPARATED_WB_REVERT_DEFAULT: UInt32 = 195
NRB_SUCCESS: UInt32 = 0
NRB_ILLEGAL_REQUEST: UInt32 = 1
NRB_INVALID_PARAMETER: UInt32 = 2
NRB_INPUT_DATA_OVERRUN: UInt32 = 3
NRB_INPUT_DATA_UNDERRUN: UInt32 = 4
NRB_OUTPUT_DATA_OVERRUN: UInt32 = 5
NRB_OUTPUT_DATA_UNDERRUN: UInt32 = 6
NV_SEP_CACHE_PARAMETER_VERSION_1: UInt32 = 1
NV_SEP_CACHE_PARAMETER_VERSION: UInt32 = 1
STORAGE_DIAGNOSTIC_STATUS_SUCCESS: UInt32 = 0
STORAGE_DIAGNOSTIC_STATUS_BUFFER_TOO_SMALL: UInt32 = 1
STORAGE_DIAGNOSTIC_STATUS_UNSUPPORTED_VERSION: UInt32 = 2
STORAGE_DIAGNOSTIC_STATUS_INVALID_PARAMETER: UInt32 = 3
STORAGE_DIAGNOSTIC_STATUS_INVALID_SIGNATURE: UInt32 = 4
STORAGE_DIAGNOSTIC_STATUS_INVALID_TARGET_TYPE: UInt32 = 5
STORAGE_DIAGNOSTIC_STATUS_MORE_DATA: UInt32 = 6
MINIPORT_DSM_NOTIFICATION_VERSION_1: UInt32 = 1
MINIPORT_DSM_NOTIFICATION_VERSION: UInt32 = 1
MINIPORT_DSM_PROFILE_UNKNOWN: UInt32 = 0
MINIPORT_DSM_PROFILE_PAGE_FILE: UInt32 = 1
MINIPORT_DSM_PROFILE_HIBERNATION_FILE: UInt32 = 2
MINIPORT_DSM_PROFILE_CRASHDUMP_FILE: UInt32 = 3
MINIPORT_DSM_NOTIFY_FLAG_BEGIN: UInt32 = 1
MINIPORT_DSM_NOTIFY_FLAG_END: UInt32 = 2
HYBRID_FUNCTION_GET_INFO: UInt32 = 1
HYBRID_FUNCTION_DISABLE_CACHING_MEDIUM: UInt32 = 16
HYBRID_FUNCTION_ENABLE_CACHING_MEDIUM: UInt32 = 17
HYBRID_FUNCTION_SET_DIRTY_THRESHOLD: UInt32 = 18
HYBRID_FUNCTION_DEMOTE_BY_SIZE: UInt32 = 19
HYBRID_STATUS_SUCCESS: UInt32 = 0
HYBRID_STATUS_ILLEGAL_REQUEST: UInt32 = 1
HYBRID_STATUS_INVALID_PARAMETER: UInt32 = 2
HYBRID_STATUS_OUTPUT_BUFFER_TOO_SMALL: UInt32 = 3
HYBRID_STATUS_ENABLE_REFCOUNT_HOLD: UInt32 = 16
HYBRID_REQUEST_BLOCK_STRUCTURE_VERSION: UInt32 = 1
HYBRID_REQUEST_INFO_STRUCTURE_VERSION: UInt32 = 1
FIRMWARE_FUNCTION_GET_INFO: UInt32 = 1
FIRMWARE_FUNCTION_DOWNLOAD: UInt32 = 2
FIRMWARE_FUNCTION_ACTIVATE: UInt32 = 3
FIRMWARE_STATUS_SUCCESS: UInt32 = 0
FIRMWARE_STATUS_ERROR: UInt32 = 1
FIRMWARE_STATUS_ILLEGAL_REQUEST: UInt32 = 2
FIRMWARE_STATUS_INVALID_PARAMETER: UInt32 = 3
FIRMWARE_STATUS_INPUT_BUFFER_TOO_BIG: UInt32 = 4
FIRMWARE_STATUS_OUTPUT_BUFFER_TOO_SMALL: UInt32 = 5
FIRMWARE_STATUS_INVALID_SLOT: UInt32 = 6
FIRMWARE_STATUS_INVALID_IMAGE: UInt32 = 7
FIRMWARE_STATUS_CONTROLLER_ERROR: UInt32 = 16
FIRMWARE_STATUS_POWER_CYCLE_REQUIRED: UInt32 = 32
FIRMWARE_STATUS_DEVICE_ERROR: UInt32 = 64
FIRMWARE_STATUS_INTERFACE_CRC_ERROR: UInt32 = 128
FIRMWARE_STATUS_UNCORRECTABLE_DATA_ERROR: UInt32 = 129
FIRMWARE_STATUS_MEDIA_CHANGE: UInt32 = 130
FIRMWARE_STATUS_ID_NOT_FOUND: UInt32 = 131
FIRMWARE_STATUS_MEDIA_CHANGE_REQUEST: UInt32 = 132
FIRMWARE_STATUS_COMMAND_ABORT: UInt32 = 133
FIRMWARE_STATUS_END_OF_MEDIA: UInt32 = 134
FIRMWARE_STATUS_ILLEGAL_LENGTH: UInt32 = 135
FIRMWARE_REQUEST_BLOCK_STRUCTURE_VERSION: UInt32 = 1
FIRMWARE_REQUEST_FLAG_CONTROLLER: UInt32 = 1
FIRMWARE_REQUEST_FLAG_LAST_SEGMENT: UInt32 = 2
FIRMWARE_REQUEST_FLAG_FIRST_SEGMENT: UInt32 = 4
FIRMWARE_REQUEST_FLAG_SWITCH_TO_EXISTING_FIRMWARE: UInt32 = 2147483648
STORAGE_FIRMWARE_INFO_STRUCTURE_VERSION: UInt32 = 1
STORAGE_FIRMWARE_INFO_STRUCTURE_VERSION_V2: UInt32 = 2
STORAGE_FIRMWARE_INFO_INVALID_SLOT: UInt32 = 255
STORAGE_FIRMWARE_SLOT_INFO_V2_REVISION_LENGTH: UInt32 = 16
STORAGE_FIRMWARE_DOWNLOAD_STRUCTURE_VERSION: UInt32 = 1
STORAGE_FIRMWARE_DOWNLOAD_STRUCTURE_VERSION_V2: UInt32 = 2
STORAGE_FIRMWARE_ACTIVATE_STRUCTURE_VERSION: UInt32 = 1
DUMP_POINTERS_VERSION_1: UInt32 = 1
DUMP_POINTERS_VERSION_2: UInt32 = 2
DUMP_POINTERS_VERSION_3: UInt32 = 3
DUMP_POINTERS_VERSION_4: UInt32 = 4
DUMP_DRIVER_NAME_LENGTH: UInt32 = 15
DUMP_EX_FLAG_SUPPORT_64BITMEMORY: UInt32 = 1
DUMP_EX_FLAG_SUPPORT_DD_TELEMETRY: UInt32 = 2
DUMP_EX_FLAG_RESUME_SUPPORT: UInt32 = 4
DUMP_EX_FLAG_DRIVER_FULL_PATH_SUPPORT: UInt32 = 8
SCSI_IOCTL_DATA_OUT: UInt32 = 0
SCSI_IOCTL_DATA_IN: UInt32 = 1
SCSI_IOCTL_DATA_UNSPECIFIED: UInt32 = 2
SCSI_IOCTL_DATA_BIDIRECTIONAL: UInt32 = 3
MPIO_IOCTL_FLAG_USE_PATHID: UInt32 = 1
MPIO_IOCTL_FLAG_USE_SCSIADDRESS: UInt32 = 2
MPIO_IOCTL_FLAG_INVOLVE_DSM: UInt32 = 4
MAX_ISCSI_HBANAME_LEN: UInt32 = 256
MAX_ISCSI_NAME_LEN: UInt32 = 223
MAX_ISCSI_ALIAS_LEN: UInt32 = 255
MAX_ISCSI_PORTAL_NAME_LEN: UInt32 = 256
MAX_ISCSI_PORTAL_ALIAS_LEN: UInt32 = 256
MAX_ISCSI_TEXT_ADDRESS_LEN: UInt32 = 256
MAX_ISCSI_PORTAL_ADDRESS_LEN: UInt32 = 256
MAX_ISCSI_DISCOVERY_DOMAIN_LEN: UInt32 = 256
MAX_RADIUS_ADDRESS_LEN: UInt32 = 41
ISCSI_SECURITY_FLAG_TUNNEL_MODE_PREFERRED: String = '0x00000040'
ISCSI_SECURITY_FLAG_TRANSPORT_MODE_PREFERRED: String = '0x00000020'
ISCSI_SECURITY_FLAG_PFS_ENABLED: String = '0x00000010'
ISCSI_SECURITY_FLAG_AGGRESSIVE_MODE_ENABLED: String = '0x00000008'
ISCSI_SECURITY_FLAG_MAIN_MODE_ENABLED: String = '0x00000004'
ISCSI_SECURITY_FLAG_IKE_IPSEC_ENABLED: String = '0x00000002'
ISCSI_SECURITY_FLAG_VALID: String = '0x00000001'
ISCSI_LOGIN_OPTIONS_HEADER_DIGEST: String = '0x00000001'
ISCSI_LOGIN_OPTIONS_DATA_DIGEST: String = '0x00000002'
ISCSI_LOGIN_OPTIONS_MAXIMUM_CONNECTIONS: String = '0x00000004'
ISCSI_LOGIN_OPTIONS_DEFAULT_TIME_2_WAIT: String = '0x00000008'
ISCSI_LOGIN_OPTIONS_DEFAULT_TIME_2_RETAIN: String = '0x00000010'
ISCSI_LOGIN_OPTIONS_USERNAME: String = '0x00000020'
ISCSI_LOGIN_OPTIONS_PASSWORD: String = '0x00000040'
ISCSI_LOGIN_OPTIONS_AUTH_TYPE: String = '0x00000080'
ID_IPV4_ADDR: String = '1'
ID_FQDN: String = '2'
ID_USER_FQDN: String = '3'
ID_IPV6_ADDR: String = '5'
ISCSI_LOGIN_FLAG_REQUIRE_IPSEC: UInt32 = 1
ISCSI_LOGIN_FLAG_MULTIPATH_ENABLED: UInt32 = 2
ISCSI_LOGIN_FLAG_RESERVED1: UInt32 = 4
ISCSI_LOGIN_FLAG_ALLOW_PORTAL_HOPPING: UInt32 = 8
ISCSI_LOGIN_FLAG_USE_RADIUS_RESPONSE: UInt32 = 16
ISCSI_LOGIN_FLAG_USE_RADIUS_VERIFICATION: UInt32 = 32
ISCSI_LOGIN_OPTIONS_VERSION: UInt32 = 0
ISCSI_TARGET_FLAG_HIDE_STATIC_TARGET: UInt32 = 2
ISCSI_TARGET_FLAG_MERGE_TARGET_INFORMATION: UInt32 = 4
@winfunctype('ISCSIDSC.dll')
def GetIScsiVersionInformation(VersionInfo: POINTER(win32more.Storage.IscsiDisc.ISCSI_VERSION_INFO_head)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def GetIScsiTargetInformationW(TargetName: win32more.Foundation.PWSTR, DiscoveryMechanism: win32more.Foundation.PWSTR, InfoClass: win32more.Storage.IscsiDisc.TARGET_INFORMATION_CLASS, BufferSize: POINTER(UInt32), Buffer: c_void_p) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def GetIScsiTargetInformationA(TargetName: win32more.Foundation.PSTR, DiscoveryMechanism: win32more.Foundation.PSTR, InfoClass: win32more.Storage.IscsiDisc.TARGET_INFORMATION_CLASS, BufferSize: POINTER(UInt32), Buffer: c_void_p) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def AddIScsiConnectionW(UniqueSessionId: POINTER(win32more.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID_head), Reserved: c_void_p, InitiatorPortNumber: UInt32, TargetPortal: POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTALW_head), SecurityFlags: UInt64, LoginOptions: POINTER(win32more.Storage.IscsiDisc.ISCSI_LOGIN_OPTIONS_head), KeySize: UInt32, Key: win32more.Foundation.PSTR, ConnectionId: POINTER(win32more.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID_head)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def AddIScsiConnectionA(UniqueSessionId: POINTER(win32more.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID_head), Reserved: c_void_p, InitiatorPortNumber: UInt32, TargetPortal: POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTALA_head), SecurityFlags: UInt64, LoginOptions: POINTER(win32more.Storage.IscsiDisc.ISCSI_LOGIN_OPTIONS_head), KeySize: UInt32, Key: win32more.Foundation.PSTR, ConnectionId: POINTER(win32more.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID_head)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def RemoveIScsiConnection(UniqueSessionId: POINTER(win32more.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID_head), ConnectionId: POINTER(win32more.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID_head)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def ReportIScsiTargetsW(ForceUpdate: win32more.Foundation.BOOLEAN, BufferSize: POINTER(UInt32), Buffer: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def ReportIScsiTargetsA(ForceUpdate: win32more.Foundation.BOOLEAN, BufferSize: POINTER(UInt32), Buffer: win32more.Foundation.PSTR) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def AddIScsiStaticTargetW(TargetName: win32more.Foundation.PWSTR, TargetAlias: win32more.Foundation.PWSTR, TargetFlags: UInt32, Persist: win32more.Foundation.BOOLEAN, Mappings: POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_MAPPINGW_head), LoginOptions: POINTER(win32more.Storage.IscsiDisc.ISCSI_LOGIN_OPTIONS_head), PortalGroup: POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTAL_GROUPW_head)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def AddIScsiStaticTargetA(TargetName: win32more.Foundation.PSTR, TargetAlias: win32more.Foundation.PSTR, TargetFlags: UInt32, Persist: win32more.Foundation.BOOLEAN, Mappings: POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_MAPPINGA_head), LoginOptions: POINTER(win32more.Storage.IscsiDisc.ISCSI_LOGIN_OPTIONS_head), PortalGroup: POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTAL_GROUPA_head)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def RemoveIScsiStaticTargetW(TargetName: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def RemoveIScsiStaticTargetA(TargetName: win32more.Foundation.PSTR) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def AddIScsiSendTargetPortalW(InitiatorInstance: win32more.Foundation.PWSTR, InitiatorPortNumber: UInt32, LoginOptions: POINTER(win32more.Storage.IscsiDisc.ISCSI_LOGIN_OPTIONS_head), SecurityFlags: UInt64, Portal: POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTALW_head)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def AddIScsiSendTargetPortalA(InitiatorInstance: win32more.Foundation.PSTR, InitiatorPortNumber: UInt32, LoginOptions: POINTER(win32more.Storage.IscsiDisc.ISCSI_LOGIN_OPTIONS_head), SecurityFlags: UInt64, Portal: POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTALA_head)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def RemoveIScsiSendTargetPortalW(InitiatorInstance: win32more.Foundation.PWSTR, InitiatorPortNumber: UInt32, Portal: POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTALW_head)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def RemoveIScsiSendTargetPortalA(InitiatorInstance: win32more.Foundation.PSTR, InitiatorPortNumber: UInt32, Portal: POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTALA_head)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def RefreshIScsiSendTargetPortalW(InitiatorInstance: win32more.Foundation.PWSTR, InitiatorPortNumber: UInt32, Portal: POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTALW_head)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def RefreshIScsiSendTargetPortalA(InitiatorInstance: win32more.Foundation.PSTR, InitiatorPortNumber: UInt32, Portal: POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTALA_head)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def ReportIScsiSendTargetPortalsW(PortalCount: POINTER(UInt32), PortalInfo: POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTAL_INFOW_head)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def ReportIScsiSendTargetPortalsA(PortalCount: POINTER(UInt32), PortalInfo: POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTAL_INFOA_head)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def ReportIScsiSendTargetPortalsExW(PortalCount: POINTER(UInt32), PortalInfoSize: POINTER(UInt32), PortalInfo: POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTAL_INFO_EXW_head)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def ReportIScsiSendTargetPortalsExA(PortalCount: POINTER(UInt32), PortalInfoSize: POINTER(UInt32), PortalInfo: POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTAL_INFO_EXA_head)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def LoginIScsiTargetW(TargetName: win32more.Foundation.PWSTR, IsInformationalSession: win32more.Foundation.BOOLEAN, InitiatorInstance: win32more.Foundation.PWSTR, InitiatorPortNumber: UInt32, TargetPortal: POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTALW_head), SecurityFlags: UInt64, Mappings: POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_MAPPINGW_head), LoginOptions: POINTER(win32more.Storage.IscsiDisc.ISCSI_LOGIN_OPTIONS_head), KeySize: UInt32, Key: win32more.Foundation.PSTR, IsPersistent: win32more.Foundation.BOOLEAN, UniqueSessionId: POINTER(win32more.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID_head), UniqueConnectionId: POINTER(win32more.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID_head)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def LoginIScsiTargetA(TargetName: win32more.Foundation.PSTR, IsInformationalSession: win32more.Foundation.BOOLEAN, InitiatorInstance: win32more.Foundation.PSTR, InitiatorPortNumber: UInt32, TargetPortal: POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTALA_head), SecurityFlags: UInt64, Mappings: POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_MAPPINGA_head), LoginOptions: POINTER(win32more.Storage.IscsiDisc.ISCSI_LOGIN_OPTIONS_head), KeySize: UInt32, Key: win32more.Foundation.PSTR, IsPersistent: win32more.Foundation.BOOLEAN, UniqueSessionId: POINTER(win32more.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID_head), UniqueConnectionId: POINTER(win32more.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID_head)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def ReportIScsiPersistentLoginsW(Count: POINTER(UInt32), PersistentLoginInfo: POINTER(win32more.Storage.IscsiDisc.PERSISTENT_ISCSI_LOGIN_INFOW_head), BufferSizeInBytes: POINTER(UInt32)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def ReportIScsiPersistentLoginsA(Count: POINTER(UInt32), PersistentLoginInfo: POINTER(win32more.Storage.IscsiDisc.PERSISTENT_ISCSI_LOGIN_INFOA_head), BufferSizeInBytes: POINTER(UInt32)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def LogoutIScsiTarget(UniqueSessionId: POINTER(win32more.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID_head)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def RemoveIScsiPersistentTargetW(InitiatorInstance: win32more.Foundation.PWSTR, InitiatorPortNumber: UInt32, TargetName: win32more.Foundation.PWSTR, Portal: POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTALW_head)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def RemoveIScsiPersistentTargetA(InitiatorInstance: win32more.Foundation.PSTR, InitiatorPortNumber: UInt32, TargetName: win32more.Foundation.PSTR, Portal: POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTALA_head)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def SendScsiInquiry(UniqueSessionId: POINTER(win32more.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID_head), Lun: UInt64, EvpdCmddt: Byte, PageCode: Byte, ScsiStatus: c_char_p_no, ResponseSize: POINTER(UInt32), ResponseBuffer: c_char_p_no, SenseSize: POINTER(UInt32), SenseBuffer: c_char_p_no) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def SendScsiReadCapacity(UniqueSessionId: POINTER(win32more.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID_head), Lun: UInt64, ScsiStatus: c_char_p_no, ResponseSize: POINTER(UInt32), ResponseBuffer: c_char_p_no, SenseSize: POINTER(UInt32), SenseBuffer: c_char_p_no) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def SendScsiReportLuns(UniqueSessionId: POINTER(win32more.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID_head), ScsiStatus: c_char_p_no, ResponseSize: POINTER(UInt32), ResponseBuffer: c_char_p_no, SenseSize: POINTER(UInt32), SenseBuffer: c_char_p_no) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def ReportIScsiInitiatorListW(BufferSize: POINTER(UInt32), Buffer: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def ReportIScsiInitiatorListA(BufferSize: POINTER(UInt32), Buffer: win32more.Foundation.PSTR) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def ReportActiveIScsiTargetMappingsW(BufferSize: POINTER(UInt32), MappingCount: POINTER(UInt32), Mappings: POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_MAPPINGW_head)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def ReportActiveIScsiTargetMappingsA(BufferSize: POINTER(UInt32), MappingCount: POINTER(UInt32), Mappings: POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_MAPPINGA_head)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def SetIScsiTunnelModeOuterAddressW(InitiatorName: win32more.Foundation.PWSTR, InitiatorPortNumber: UInt32, DestinationAddress: win32more.Foundation.PWSTR, OuterModeAddress: win32more.Foundation.PWSTR, Persist: win32more.Foundation.BOOLEAN) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def SetIScsiTunnelModeOuterAddressA(InitiatorName: win32more.Foundation.PSTR, InitiatorPortNumber: UInt32, DestinationAddress: win32more.Foundation.PSTR, OuterModeAddress: win32more.Foundation.PSTR, Persist: win32more.Foundation.BOOLEAN) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def SetIScsiIKEInfoW(InitiatorName: win32more.Foundation.PWSTR, InitiatorPortNumber: UInt32, AuthInfo: POINTER(win32more.Storage.IscsiDisc.IKE_AUTHENTICATION_INFORMATION_head), Persist: win32more.Foundation.BOOLEAN) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def SetIScsiIKEInfoA(InitiatorName: win32more.Foundation.PSTR, InitiatorPortNumber: UInt32, AuthInfo: POINTER(win32more.Storage.IscsiDisc.IKE_AUTHENTICATION_INFORMATION_head), Persist: win32more.Foundation.BOOLEAN) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def GetIScsiIKEInfoW(InitiatorName: win32more.Foundation.PWSTR, InitiatorPortNumber: UInt32, Reserved: POINTER(UInt32), AuthInfo: POINTER(win32more.Storage.IscsiDisc.IKE_AUTHENTICATION_INFORMATION_head)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def GetIScsiIKEInfoA(InitiatorName: win32more.Foundation.PSTR, InitiatorPortNumber: UInt32, Reserved: POINTER(UInt32), AuthInfo: POINTER(win32more.Storage.IscsiDisc.IKE_AUTHENTICATION_INFORMATION_head)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def SetIScsiGroupPresharedKey(KeyLength: UInt32, Key: c_char_p_no, Persist: win32more.Foundation.BOOLEAN) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def SetIScsiInitiatorCHAPSharedSecret(SharedSecretLength: UInt32, SharedSecret: c_char_p_no) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def SetIScsiInitiatorRADIUSSharedSecret(SharedSecretLength: UInt32, SharedSecret: c_char_p_no) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def SetIScsiInitiatorNodeNameW(InitiatorNodeName: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def SetIScsiInitiatorNodeNameA(InitiatorNodeName: win32more.Foundation.PSTR) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def GetIScsiInitiatorNodeNameW(InitiatorNodeName: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def GetIScsiInitiatorNodeNameA(InitiatorNodeName: win32more.Foundation.PSTR) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def AddISNSServerW(Address: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def AddISNSServerA(Address: win32more.Foundation.PSTR) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def RemoveISNSServerW(Address: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def RemoveISNSServerA(Address: win32more.Foundation.PSTR) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def RefreshISNSServerW(Address: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def RefreshISNSServerA(Address: win32more.Foundation.PSTR) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def ReportISNSServerListW(BufferSizeInChar: POINTER(UInt32), Buffer: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def ReportISNSServerListA(BufferSizeInChar: POINTER(UInt32), Buffer: win32more.Foundation.PSTR) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def GetIScsiSessionListW(BufferSize: POINTER(UInt32), SessionCount: POINTER(UInt32), SessionInfo: POINTER(win32more.Storage.IscsiDisc.ISCSI_SESSION_INFOW_head)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def GetIScsiSessionListA(BufferSize: POINTER(UInt32), SessionCount: POINTER(UInt32), SessionInfo: POINTER(win32more.Storage.IscsiDisc.ISCSI_SESSION_INFOA_head)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def GetIScsiSessionListEx(BufferSize: POINTER(UInt32), SessionCountPtr: POINTER(UInt32), SessionInfo: POINTER(win32more.Storage.IscsiDisc.ISCSI_SESSION_INFO_EX_head)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def GetDevicesForIScsiSessionW(UniqueSessionId: POINTER(win32more.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID_head), DeviceCount: POINTER(UInt32), Devices: POINTER(win32more.Storage.IscsiDisc.ISCSI_DEVICE_ON_SESSIONW_head)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def GetDevicesForIScsiSessionA(UniqueSessionId: POINTER(win32more.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID_head), DeviceCount: POINTER(UInt32), Devices: POINTER(win32more.Storage.IscsiDisc.ISCSI_DEVICE_ON_SESSIONA_head)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def SetupPersistentIScsiVolumes() -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def SetupPersistentIScsiDevices() -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def AddPersistentIScsiDeviceW(DevicePath: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def AddPersistentIScsiDeviceA(DevicePath: win32more.Foundation.PSTR) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def RemovePersistentIScsiDeviceW(DevicePath: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def RemovePersistentIScsiDeviceA(DevicePath: win32more.Foundation.PSTR) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def ClearPersistentIScsiDevices() -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def ReportPersistentIScsiDevicesW(BufferSizeInChar: POINTER(UInt32), Buffer: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def ReportPersistentIScsiDevicesA(BufferSizeInChar: POINTER(UInt32), Buffer: win32more.Foundation.PSTR) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def ReportIScsiTargetPortalsW(InitiatorName: win32more.Foundation.PWSTR, TargetName: win32more.Foundation.PWSTR, TargetPortalTag: POINTER(UInt16), ElementCount: POINTER(UInt32), Portals: POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTALW_head)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def ReportIScsiTargetPortalsA(InitiatorName: win32more.Foundation.PSTR, TargetName: win32more.Foundation.PSTR, TargetPortalTag: POINTER(UInt16), ElementCount: POINTER(UInt32), Portals: POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTALA_head)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def AddRadiusServerW(Address: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def AddRadiusServerA(Address: win32more.Foundation.PSTR) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def RemoveRadiusServerW(Address: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def RemoveRadiusServerA(Address: win32more.Foundation.PSTR) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def ReportRadiusServerListW(BufferSizeInChar: POINTER(UInt32), Buffer: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def ReportRadiusServerListA(BufferSizeInChar: POINTER(UInt32), Buffer: win32more.Foundation.PSTR) -> UInt32: ...
class DSM_NOTIFICATION_REQUEST_BLOCK(Structure):
    Size: UInt32
    Version: UInt32
    NotifyFlags: UInt32
    DataSetProfile: UInt32
    Reserved: UInt32 * 3
    DataSetRangesCount: UInt32
    DataSetRanges: win32more.Storage.IscsiDisc.MP_DEVICE_DATA_SET_RANGE * 1
class DUMP_DRIVER(Structure):
    DumpDriverList: c_void_p
    DriverName: Char * 15
    BaseName: Char * 15
class DUMP_DRIVER_EX(Structure):
    DumpDriverList: c_void_p
    DriverName: Char * 15
    BaseName: Char * 15
    DriverFullPath: win32more.Storage.IscsiDisc.NTSCSI_UNICODE_STRING
class DUMP_POINTERS(Structure):
    AdapterObject: POINTER(win32more.Storage.IscsiDisc._ADAPTER_OBJECT_head)
    MappedRegisterBase: c_void_p
    DumpData: c_void_p
    CommonBufferVa: c_void_p
    CommonBufferPa: win32more.Foundation.LARGE_INTEGER
    CommonBufferSize: UInt32
    AllocateCommonBuffers: win32more.Foundation.BOOLEAN
    UseDiskDump: win32more.Foundation.BOOLEAN
    Spare1: Byte * 2
    DeviceObject: c_void_p
class DUMP_POINTERS_EX(Structure):
    Header: win32more.Storage.IscsiDisc.DUMP_POINTERS_VERSION
    DumpData: c_void_p
    CommonBufferVa: c_void_p
    CommonBufferSize: UInt32
    AllocateCommonBuffers: win32more.Foundation.BOOLEAN
    DeviceObject: c_void_p
    DriverList: c_void_p
    dwPortFlags: UInt32
    MaxDeviceDumpSectionSize: UInt32
    MaxDeviceDumpLevel: UInt32
    MaxTransferSize: UInt32
    AdapterObject: c_void_p
    MappedRegisterBase: c_void_p
    DeviceReady: POINTER(win32more.Foundation.BOOLEAN)
    DumpDevicePowerOn: win32more.Storage.IscsiDisc.PDUMP_DEVICE_POWERON_ROUTINE
    DumpDevicePowerOnContext: c_void_p
class DUMP_POINTERS_VERSION(Structure):
    Version: UInt32
    Size: UInt32
class FIRMWARE_REQUEST_BLOCK(Structure):
    Version: UInt32
    Size: UInt32
    Function: UInt32
    Flags: UInt32
    DataBufferOffset: UInt32
    DataBufferLength: UInt32
class HYBRID_DEMOTE_BY_SIZE(Structure):
    Version: UInt32
    Size: UInt32
    SourcePriority: Byte
    TargetPriority: Byte
    Reserved0: UInt16
    Reserved1: UInt32
    LbaCount: UInt64
class HYBRID_DIRTY_THRESHOLDS(Structure):
    Version: UInt32
    Size: UInt32
    DirtyLowThreshold: UInt32
    DirtyHighThreshold: UInt32
class HYBRID_INFORMATION(Structure):
    Version: UInt32
    Size: UInt32
    HybridSupported: win32more.Foundation.BOOLEAN
    Status: win32more.Storage.IscsiDisc.NVCACHE_STATUS
    CacheTypeEffective: win32more.Storage.IscsiDisc.NVCACHE_TYPE
    CacheTypeDefault: win32more.Storage.IscsiDisc.NVCACHE_TYPE
    FractionBase: UInt32
    CacheSize: UInt64
    Attributes: _Attributes_e__Struct
    Priorities: _Priorities_e__Struct
    class _Attributes_e__Struct(Structure):
        _bitfield: UInt32
    class _Priorities_e__Struct(Structure):
        PriorityLevelCount: Byte
        MaxPriorityBehavior: win32more.Foundation.BOOLEAN
        OptimalWriteGranularity: Byte
        Reserved: Byte
        DirtyThresholdLow: UInt32
        DirtyThresholdHigh: UInt32
        SupportedCommands: _SupportedCommands_e__Struct
        Priority: win32more.Storage.IscsiDisc.NVCACHE_PRIORITY_LEVEL_DESCRIPTOR * 1
        class _SupportedCommands_e__Struct(Structure):
            _bitfield: UInt32
            MaxEvictCommands: UInt32
            MaxLbaRangeCountForEvict: UInt32
            MaxLbaRangeCountForChangeLba: UInt32
class HYBRID_REQUEST_BLOCK(Structure):
    Version: UInt32
    Size: UInt32
    Function: UInt32
    Flags: UInt32
    DataBufferOffset: UInt32
    DataBufferLength: UInt32
class IDE_IO_CONTROL(Structure):
    HeaderLength: UInt32
    Signature: Byte * 8
    Timeout: UInt32
    ControlCode: UInt32
    ReturnStatus: UInt32
    DataLength: UInt32
class IKE_AUTHENTICATION_INFORMATION(Structure):
    AuthMethod: win32more.Storage.IscsiDisc.IKE_AUTHENTICATION_METHOD
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        PsKey: win32more.Storage.IscsiDisc.IKE_AUTHENTICATION_PRESHARED_KEY
IKE_AUTHENTICATION_METHOD = Int32
IKE_AUTHENTICATION_PRESHARED_KEY_METHOD: IKE_AUTHENTICATION_METHOD = 1
class IKE_AUTHENTICATION_PRESHARED_KEY(Structure):
    SecurityFlags: UInt64
    IdType: Byte
    IdLengthInBytes: UInt32
    Id: c_char_p_no
    KeyLengthInBytes: UInt32
    Key: c_char_p_no
class IO_SCSI_CAPABILITIES(Structure):
    Length: UInt32
    MaximumTransferLength: UInt32
    MaximumPhysicalPages: UInt32
    SupportedAsynchronousEvents: UInt32
    AlignmentMask: UInt32
    TaggedQueuing: win32more.Foundation.BOOLEAN
    AdapterScansDown: win32more.Foundation.BOOLEAN
    AdapterUsesPio: win32more.Foundation.BOOLEAN
ISCSI_AUTH_TYPES = Int32
ISCSI_NO_AUTH_TYPE: ISCSI_AUTH_TYPES = 0
ISCSI_CHAP_AUTH_TYPE: ISCSI_AUTH_TYPES = 1
ISCSI_MUTUAL_CHAP_AUTH_TYPE: ISCSI_AUTH_TYPES = 2
class ISCSI_CONNECTION_INFOA(Structure):
    ConnectionId: win32more.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID
    InitiatorAddress: win32more.Foundation.PSTR
    TargetAddress: win32more.Foundation.PSTR
    InitiatorSocket: UInt16
    TargetSocket: UInt16
    CID: Byte * 2
class ISCSI_CONNECTION_INFOW(Structure):
    ConnectionId: win32more.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID
    InitiatorAddress: win32more.Foundation.PWSTR
    TargetAddress: win32more.Foundation.PWSTR
    InitiatorSocket: UInt16
    TargetSocket: UInt16
    CID: Byte * 2
class ISCSI_CONNECTION_INFO_EX(Structure):
    ConnectionId: win32more.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID
    State: Byte
    Protocol: Byte
    HeaderDigest: Byte
    DataDigest: Byte
    MaxRecvDataSegmentLength: UInt32
    AuthType: win32more.Storage.IscsiDisc.ISCSI_AUTH_TYPES
    EstimatedThroughput: UInt64
    MaxDatagramSize: UInt32
class ISCSI_DEVICE_ON_SESSIONA(Structure):
    InitiatorName: win32more.Foundation.CHAR * 256
    TargetName: win32more.Foundation.CHAR * 224
    ScsiAddress: win32more.Storage.IscsiDisc.SCSI_ADDRESS
    DeviceInterfaceType: Guid
    DeviceInterfaceName: win32more.Foundation.CHAR * 260
    LegacyName: win32more.Foundation.CHAR * 260
    StorageDeviceNumber: win32more.System.Ioctl.STORAGE_DEVICE_NUMBER
    DeviceInstance: UInt32
class ISCSI_DEVICE_ON_SESSIONW(Structure):
    InitiatorName: Char * 256
    TargetName: Char * 224
    ScsiAddress: win32more.Storage.IscsiDisc.SCSI_ADDRESS
    DeviceInterfaceType: Guid
    DeviceInterfaceName: Char * 260
    LegacyName: Char * 260
    StorageDeviceNumber: win32more.System.Ioctl.STORAGE_DEVICE_NUMBER
    DeviceInstance: UInt32
ISCSI_DIGEST_TYPES = Int32
ISCSI_DIGEST_TYPE_NONE: ISCSI_DIGEST_TYPES = 0
ISCSI_DIGEST_TYPE_CRC32C: ISCSI_DIGEST_TYPES = 1
class ISCSI_LOGIN_OPTIONS(Structure):
    Version: UInt32
    InformationSpecified: UInt32
    LoginFlags: UInt32
    AuthType: win32more.Storage.IscsiDisc.ISCSI_AUTH_TYPES
    HeaderDigest: win32more.Storage.IscsiDisc.ISCSI_DIGEST_TYPES
    DataDigest: win32more.Storage.IscsiDisc.ISCSI_DIGEST_TYPES
    MaximumConnections: UInt32
    DefaultTime2Wait: UInt32
    DefaultTime2Retain: UInt32
    UsernameLength: UInt32
    PasswordLength: UInt32
    Username: c_char_p_no
    Password: c_char_p_no
class ISCSI_SESSION_INFOA(Structure):
    SessionId: win32more.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID
    InitiatorName: win32more.Foundation.PSTR
    TargetNodeName: win32more.Foundation.PSTR
    TargetName: win32more.Foundation.PSTR
    ISID: Byte * 6
    TSID: Byte * 2
    ConnectionCount: UInt32
    Connections: POINTER(win32more.Storage.IscsiDisc.ISCSI_CONNECTION_INFOA_head)
class ISCSI_SESSION_INFOW(Structure):
    SessionId: win32more.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID
    InitiatorName: win32more.Foundation.PWSTR
    TargetNodeName: win32more.Foundation.PWSTR
    TargetName: win32more.Foundation.PWSTR
    ISID: Byte * 6
    TSID: Byte * 2
    ConnectionCount: UInt32
    Connections: POINTER(win32more.Storage.IscsiDisc.ISCSI_CONNECTION_INFOW_head)
class ISCSI_SESSION_INFO_EX(Structure):
    SessionId: win32more.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID
    InitialR2t: win32more.Foundation.BOOLEAN
    ImmediateData: win32more.Foundation.BOOLEAN
    Type: Byte
    DataSequenceInOrder: win32more.Foundation.BOOLEAN
    DataPduInOrder: win32more.Foundation.BOOLEAN
    ErrorRecoveryLevel: Byte
    MaxOutstandingR2t: UInt32
    FirstBurstLength: UInt32
    MaxBurstLength: UInt32
    MaximumConnections: UInt32
    ConnectionCount: UInt32
    Connections: POINTER(win32more.Storage.IscsiDisc.ISCSI_CONNECTION_INFO_EX_head)
class ISCSI_TARGET_MAPPINGA(Structure):
    InitiatorName: win32more.Foundation.CHAR * 256
    TargetName: win32more.Foundation.CHAR * 224
    OSDeviceName: win32more.Foundation.CHAR * 260
    SessionId: win32more.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID
    OSBusNumber: UInt32
    OSTargetNumber: UInt32
    LUNCount: UInt32
    LUNList: POINTER(win32more.Storage.IscsiDisc.SCSI_LUN_LIST_head)
class ISCSI_TARGET_MAPPINGW(Structure):
    InitiatorName: Char * 256
    TargetName: Char * 224
    OSDeviceName: Char * 260
    SessionId: win32more.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID
    OSBusNumber: UInt32
    OSTargetNumber: UInt32
    LUNCount: UInt32
    LUNList: POINTER(win32more.Storage.IscsiDisc.SCSI_LUN_LIST_head)
class ISCSI_TARGET_PORTALA(Structure):
    SymbolicName: win32more.Foundation.CHAR * 256
    Address: win32more.Foundation.CHAR * 256
    Socket: UInt16
class ISCSI_TARGET_PORTALW(Structure):
    SymbolicName: Char * 256
    Address: Char * 256
    Socket: UInt16
class ISCSI_TARGET_PORTAL_GROUPA(Structure):
    Count: UInt32
    Portals: win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTALA * 1
class ISCSI_TARGET_PORTAL_GROUPW(Structure):
    Count: UInt32
    Portals: win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTALW * 1
class ISCSI_TARGET_PORTAL_INFOA(Structure):
    InitiatorName: win32more.Foundation.CHAR * 256
    InitiatorPortNumber: UInt32
    SymbolicName: win32more.Foundation.CHAR * 256
    Address: win32more.Foundation.CHAR * 256
    Socket: UInt16
class ISCSI_TARGET_PORTAL_INFOW(Structure):
    InitiatorName: Char * 256
    InitiatorPortNumber: UInt32
    SymbolicName: Char * 256
    Address: Char * 256
    Socket: UInt16
class ISCSI_TARGET_PORTAL_INFO_EXA(Structure):
    InitiatorName: win32more.Foundation.CHAR * 256
    InitiatorPortNumber: UInt32
    SymbolicName: win32more.Foundation.CHAR * 256
    Address: win32more.Foundation.CHAR * 256
    Socket: UInt16
    SecurityFlags: UInt64
    LoginOptions: win32more.Storage.IscsiDisc.ISCSI_LOGIN_OPTIONS
class ISCSI_TARGET_PORTAL_INFO_EXW(Structure):
    InitiatorName: Char * 256
    InitiatorPortNumber: UInt32
    SymbolicName: Char * 256
    Address: Char * 256
    Socket: UInt16
    SecurityFlags: UInt64
    LoginOptions: win32more.Storage.IscsiDisc.ISCSI_LOGIN_OPTIONS
class ISCSI_UNIQUE_SESSION_ID(Structure):
    AdapterUnique: UInt64
    AdapterSpecific: UInt64
class ISCSI_VERSION_INFO(Structure):
    MajorVersion: UInt32
    MinorVersion: UInt32
    BuildNumber: UInt32
class MPIO_PASS_THROUGH_PATH(Structure):
    PassThrough: win32more.Storage.IscsiDisc.SCSI_PASS_THROUGH
    Version: UInt32
    Length: UInt16
    Flags: Byte
    PortNumber: Byte
    MpioPathId: UInt64
if ARCH in 'X64,ARM64':
    class MPIO_PASS_THROUGH_PATH32(Structure):
        PassThrough: win32more.Storage.IscsiDisc.SCSI_PASS_THROUGH32
        Version: UInt32
        Length: UInt16
        Flags: Byte
        PortNumber: Byte
        MpioPathId: UInt64
if ARCH in 'X64,ARM64':
    class MPIO_PASS_THROUGH_PATH32_EX(Structure):
        PassThroughOffset: UInt32
        Version: UInt32
        Length: UInt16
        Flags: Byte
        PortNumber: Byte
        MpioPathId: UInt64
class MPIO_PASS_THROUGH_PATH_DIRECT(Structure):
    PassThrough: win32more.Storage.IscsiDisc.SCSI_PASS_THROUGH_DIRECT
    Version: UInt32
    Length: UInt16
    Flags: Byte
    PortNumber: Byte
    MpioPathId: UInt64
if ARCH in 'X64,ARM64':
    class MPIO_PASS_THROUGH_PATH_DIRECT32(Structure):
        PassThrough: win32more.Storage.IscsiDisc.SCSI_PASS_THROUGH_DIRECT32
        Version: UInt32
        Length: UInt16
        Flags: Byte
        PortNumber: Byte
        MpioPathId: UInt64
if ARCH in 'X64,ARM64':
    class MPIO_PASS_THROUGH_PATH_DIRECT32_EX(Structure):
        PassThroughOffset: UInt32
        Version: UInt32
        Length: UInt16
        Flags: Byte
        PortNumber: Byte
        MpioPathId: UInt64
class MPIO_PASS_THROUGH_PATH_DIRECT_EX(Structure):
    PassThroughOffset: UInt32
    Version: UInt32
    Length: UInt16
    Flags: Byte
    PortNumber: Byte
    MpioPathId: UInt64
class MPIO_PASS_THROUGH_PATH_EX(Structure):
    PassThroughOffset: UInt32
    Version: UInt32
    Length: UInt16
    Flags: Byte
    PortNumber: Byte
    MpioPathId: UInt64
class MP_DEVICE_DATA_SET_RANGE(Structure):
    StartingOffset: Int64
    LengthInBytes: UInt64
MP_STORAGE_DIAGNOSTIC_LEVEL = Int32
MP_STORAGE_DIAGNOSTIC_LEVEL_MpStorageDiagnosticLevelDefault: MP_STORAGE_DIAGNOSTIC_LEVEL = 0
MP_STORAGE_DIAGNOSTIC_LEVEL_MpStorageDiagnosticLevelMax: MP_STORAGE_DIAGNOSTIC_LEVEL = 1
MP_STORAGE_DIAGNOSTIC_TARGET_TYPE = Int32
MP_STORAGE_DIAGNOSTIC_TARGET_TYPE_MpStorageDiagnosticTargetTypeUndefined: MP_STORAGE_DIAGNOSTIC_TARGET_TYPE = 0
MP_STORAGE_DIAGNOSTIC_TARGET_TYPE_MpStorageDiagnosticTargetTypeMiniport: MP_STORAGE_DIAGNOSTIC_TARGET_TYPE = 2
MP_STORAGE_DIAGNOSTIC_TARGET_TYPE_MpStorageDiagnosticTargetTypeHbaFirmware: MP_STORAGE_DIAGNOSTIC_TARGET_TYPE = 3
MP_STORAGE_DIAGNOSTIC_TARGET_TYPE_MpStorageDiagnosticTargetTypeMax: MP_STORAGE_DIAGNOSTIC_TARGET_TYPE = 4
class NTSCSI_UNICODE_STRING(Structure):
    Length: UInt16
    MaximumLength: UInt16
    Buffer: win32more.Foundation.PWSTR
class NVCACHE_HINT_PAYLOAD(Structure):
    Command: Byte
    Feature7_0: Byte
    Feature15_8: Byte
    Count15_8: Byte
    LBA7_0: Byte
    LBA15_8: Byte
    LBA23_16: Byte
    LBA31_24: Byte
    LBA39_32: Byte
    LBA47_40: Byte
    Auxiliary7_0: Byte
    Auxiliary23_16: Byte
    Reserved: Byte * 4
class NVCACHE_PRIORITY_LEVEL_DESCRIPTOR(Structure):
    PriorityLevel: Byte
    Reserved0: Byte * 3
    ConsumedNVMSizeFraction: UInt32
    ConsumedMappingResourcesFraction: UInt32
    ConsumedNVMSizeForDirtyDataFraction: UInt32
    ConsumedMappingResourcesForDirtyDataFraction: UInt32
    Reserved1: UInt32
class NVCACHE_REQUEST_BLOCK(Structure):
    NRBSize: UInt32
    Function: UInt16
    NRBFlags: UInt32
    NRBStatus: UInt32
    Count: UInt32
    LBA: UInt64
    DataBufSize: UInt32
    NVCacheStatus: UInt32
    NVCacheSubStatus: UInt32
NVCACHE_STATUS = Int32
NVCACHE_STATUS_NvCacheStatusUnknown: NVCACHE_STATUS = 0
NVCACHE_STATUS_NvCacheStatusDisabling: NVCACHE_STATUS = 1
NVCACHE_STATUS_NvCacheStatusDisabled: NVCACHE_STATUS = 2
NVCACHE_STATUS_NvCacheStatusEnabled: NVCACHE_STATUS = 3
NVCACHE_TYPE = Int32
NVCACHE_TYPE_NvCacheTypeUnknown: NVCACHE_TYPE = 0
NVCACHE_TYPE_NvCacheTypeNone: NVCACHE_TYPE = 1
NVCACHE_TYPE_NvCacheTypeWriteBack: NVCACHE_TYPE = 2
NVCACHE_TYPE_NvCacheTypeWriteThrough: NVCACHE_TYPE = 3
class NV_FEATURE_PARAMETER(Structure):
    NVPowerModeEnabled: UInt16
    NVParameterReserv1: UInt16
    NVCmdEnabled: UInt16
    NVParameterReserv2: UInt16
    NVPowerModeVer: UInt16
    NVCmdVer: UInt16
    NVSize: UInt32
    NVReadSpeed: UInt16
    NVWrtSpeed: UInt16
    DeviceSpinUpTime: UInt32
class NV_SEP_CACHE_PARAMETER(Structure):
    Version: UInt32
    Size: UInt32
    Flags: _Flags_e__Union
    WriteCacheType: Byte
    WriteCacheTypeEffective: Byte
    ParameterReserve1: Byte * 3
    class _Flags_e__Union(Union):
        CacheFlags: _CacheFlags_e__Struct
        CacheFlagsSet: Byte
        class _CacheFlags_e__Struct(Structure):
            _bitfield: Byte
NV_SEP_WRITE_CACHE_TYPE = Int32
NV_SEP_WRITE_CACHE_TYPE_NVSEPWriteCacheTypeUnknown: NV_SEP_WRITE_CACHE_TYPE = 0
NV_SEP_WRITE_CACHE_TYPE_NVSEPWriteCacheTypeNone: NV_SEP_WRITE_CACHE_TYPE = 1
NV_SEP_WRITE_CACHE_TYPE_NVSEPWriteCacheTypeWriteBack: NV_SEP_WRITE_CACHE_TYPE = 2
NV_SEP_WRITE_CACHE_TYPE_NVSEPWriteCacheTypeWriteThrough: NV_SEP_WRITE_CACHE_TYPE = 3
@winfunctype_pointer
def PDUMP_DEVICE_POWERON_ROUTINE(Context: c_void_p) -> Int32: ...
class PERSISTENT_ISCSI_LOGIN_INFOA(Structure):
    TargetName: win32more.Foundation.CHAR * 224
    IsInformationalSession: win32more.Foundation.BOOLEAN
    InitiatorInstance: win32more.Foundation.CHAR * 256
    InitiatorPortNumber: UInt32
    TargetPortal: win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTALA
    SecurityFlags: UInt64
    Mappings: POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_MAPPINGA_head)
    LoginOptions: win32more.Storage.IscsiDisc.ISCSI_LOGIN_OPTIONS
class PERSISTENT_ISCSI_LOGIN_INFOW(Structure):
    TargetName: Char * 224
    IsInformationalSession: win32more.Foundation.BOOLEAN
    InitiatorInstance: Char * 256
    InitiatorPortNumber: UInt32
    TargetPortal: win32more.Storage.IscsiDisc.ISCSI_TARGET_PORTALW
    SecurityFlags: UInt64
    Mappings: POINTER(win32more.Storage.IscsiDisc.ISCSI_TARGET_MAPPINGW_head)
    LoginOptions: win32more.Storage.IscsiDisc.ISCSI_LOGIN_OPTIONS
class SCSI_ADAPTER_BUS_INFO(Structure):
    NumberOfBuses: Byte
    BusData: win32more.Storage.IscsiDisc.SCSI_BUS_DATA * 1
class SCSI_ADDRESS(Structure):
    Length: UInt32
    PortNumber: Byte
    PathId: Byte
    TargetId: Byte
    Lun: Byte
class SCSI_BUS_DATA(Structure):
    NumberOfLogicalUnits: Byte
    InitiatorBusId: Byte
    InquiryDataOffset: UInt32
class SCSI_INQUIRY_DATA(Structure):
    PathId: Byte
    TargetId: Byte
    Lun: Byte
    DeviceClaimed: win32more.Foundation.BOOLEAN
    InquiryDataLength: UInt32
    NextInquiryDataOffset: UInt32
    InquiryData: Byte * 1
class SCSI_LUN_LIST(Structure):
    OSLUN: UInt32
    TargetLUN: UInt64
class SCSI_PASS_THROUGH(Structure):
    Length: UInt16
    ScsiStatus: Byte
    PathId: Byte
    TargetId: Byte
    Lun: Byte
    CdbLength: Byte
    SenseInfoLength: Byte
    DataIn: Byte
    DataTransferLength: UInt32
    TimeOutValue: UInt32
    DataBufferOffset: UIntPtr
    SenseInfoOffset: UInt32
    Cdb: Byte * 16
if ARCH in 'X64,ARM64':
    class SCSI_PASS_THROUGH32(Structure):
        Length: UInt16
        ScsiStatus: Byte
        PathId: Byte
        TargetId: Byte
        Lun: Byte
        CdbLength: Byte
        SenseInfoLength: Byte
        DataIn: Byte
        DataTransferLength: UInt32
        TimeOutValue: UInt32
        DataBufferOffset: UInt32
        SenseInfoOffset: UInt32
        Cdb: Byte * 16
if ARCH in 'X64,ARM64':
    class SCSI_PASS_THROUGH32_EX(Structure):
        Version: UInt32
        Length: UInt32
        CdbLength: UInt32
        StorAddressLength: UInt32
        ScsiStatus: Byte
        SenseInfoLength: Byte
        DataDirection: Byte
        Reserved: Byte
        TimeOutValue: UInt32
        StorAddressOffset: UInt32
        SenseInfoOffset: UInt32
        DataOutTransferLength: UInt32
        DataInTransferLength: UInt32
        DataOutBufferOffset: UInt32
        DataInBufferOffset: UInt32
        Cdb: Byte * 1
class SCSI_PASS_THROUGH_DIRECT(Structure):
    Length: UInt16
    ScsiStatus: Byte
    PathId: Byte
    TargetId: Byte
    Lun: Byte
    CdbLength: Byte
    SenseInfoLength: Byte
    DataIn: Byte
    DataTransferLength: UInt32
    TimeOutValue: UInt32
    DataBuffer: c_void_p
    SenseInfoOffset: UInt32
    Cdb: Byte * 16
if ARCH in 'X64,ARM64':
    class SCSI_PASS_THROUGH_DIRECT32(Structure):
        Length: UInt16
        ScsiStatus: Byte
        PathId: Byte
        TargetId: Byte
        Lun: Byte
        CdbLength: Byte
        SenseInfoLength: Byte
        DataIn: Byte
        DataTransferLength: UInt32
        TimeOutValue: UInt32
        DataBuffer: c_void_p
        SenseInfoOffset: UInt32
        Cdb: Byte * 16
if ARCH in 'X64,ARM64':
    class SCSI_PASS_THROUGH_DIRECT32_EX(Structure):
        Version: UInt32
        Length: UInt32
        CdbLength: UInt32
        StorAddressLength: UInt32
        ScsiStatus: Byte
        SenseInfoLength: Byte
        DataDirection: Byte
        Reserved: Byte
        TimeOutValue: UInt32
        StorAddressOffset: UInt32
        SenseInfoOffset: UInt32
        DataOutTransferLength: UInt32
        DataInTransferLength: UInt32
        DataOutBuffer: c_void_p
        DataInBuffer: c_void_p
        Cdb: Byte * 1
class SCSI_PASS_THROUGH_DIRECT_EX(Structure):
    Version: UInt32
    Length: UInt32
    CdbLength: UInt32
    StorAddressLength: UInt32
    ScsiStatus: Byte
    SenseInfoLength: Byte
    DataDirection: Byte
    Reserved: Byte
    TimeOutValue: UInt32
    StorAddressOffset: UInt32
    SenseInfoOffset: UInt32
    DataOutTransferLength: UInt32
    DataInTransferLength: UInt32
    DataOutBuffer: c_void_p
    DataInBuffer: c_void_p
    Cdb: Byte * 1
class SCSI_PASS_THROUGH_EX(Structure):
    Version: UInt32
    Length: UInt32
    CdbLength: UInt32
    StorAddressLength: UInt32
    ScsiStatus: Byte
    SenseInfoLength: Byte
    DataDirection: Byte
    Reserved: Byte
    TimeOutValue: UInt32
    StorAddressOffset: UInt32
    SenseInfoOffset: UInt32
    DataOutTransferLength: UInt32
    DataInTransferLength: UInt32
    DataOutBufferOffset: UIntPtr
    DataInBufferOffset: UIntPtr
    Cdb: Byte * 1
class SRB_IO_CONTROL(Structure):
    HeaderLength: UInt32
    Signature: Byte * 8
    Timeout: UInt32
    ControlCode: UInt32
    ReturnCode: UInt32
    Length: UInt32
class STORAGE_DIAGNOSTIC_MP_REQUEST(Structure):
    Version: UInt32
    Size: UInt32
    TargetType: win32more.Storage.IscsiDisc.MP_STORAGE_DIAGNOSTIC_TARGET_TYPE
    Level: win32more.Storage.IscsiDisc.MP_STORAGE_DIAGNOSTIC_LEVEL
    ProviderId: Guid
    BufferSize: UInt32
    Reserved: UInt32
    DataBuffer: Byte * 1
class STORAGE_ENDURANCE_DATA_DESCRIPTOR(Structure):
    Version: UInt32
    Size: UInt32
    EnduranceInfo: win32more.Storage.IscsiDisc.STORAGE_ENDURANCE_INFO
class STORAGE_ENDURANCE_INFO(Structure):
    ValidFields: UInt32
    GroupId: UInt32
    Flags: _Flags_e__Struct
    LifePercentage: UInt32
    BytesReadCount: Byte * 16
    ByteWriteCount: Byte * 16
    class _Flags_e__Struct(Structure):
        _bitfield: UInt32
class STORAGE_FIRMWARE_ACTIVATE(Structure):
    Version: UInt32
    Size: UInt32
    SlotToActivate: Byte
    Reserved0: Byte * 3
class STORAGE_FIRMWARE_DOWNLOAD(Structure):
    Version: UInt32
    Size: UInt32
    Offset: UInt64
    BufferSize: UInt64
    ImageBuffer: Byte * 1
class STORAGE_FIRMWARE_DOWNLOAD_V2(Structure):
    Version: UInt32
    Size: UInt32
    Offset: UInt64
    BufferSize: UInt64
    Slot: Byte
    Reserved: Byte * 3
    ImageSize: UInt32
    ImageBuffer: Byte * 1
class STORAGE_FIRMWARE_INFO(Structure):
    Version: UInt32
    Size: UInt32
    UpgradeSupport: win32more.Foundation.BOOLEAN
    SlotCount: Byte
    ActiveSlot: Byte
    PendingActivateSlot: Byte
    Reserved: UInt32
    Slot: win32more.Storage.IscsiDisc.STORAGE_FIRMWARE_SLOT_INFO * 1
class STORAGE_FIRMWARE_INFO_V2(Structure):
    Version: UInt32
    Size: UInt32
    UpgradeSupport: win32more.Foundation.BOOLEAN
    SlotCount: Byte
    ActiveSlot: Byte
    PendingActivateSlot: Byte
    FirmwareShared: win32more.Foundation.BOOLEAN
    Reserved: Byte * 3
    ImagePayloadAlignment: UInt32
    ImagePayloadMaxSize: UInt32
    Slot: win32more.Storage.IscsiDisc.STORAGE_FIRMWARE_SLOT_INFO_V2 * 1
class STORAGE_FIRMWARE_SLOT_INFO(Structure):
    SlotNumber: Byte
    ReadOnly: win32more.Foundation.BOOLEAN
    Reserved: Byte * 6
    Revision: _Revision_e__Union
    class _Revision_e__Union(Union):
        Info: Byte * 8
        AsUlonglong: UInt64
class STORAGE_FIRMWARE_SLOT_INFO_V2(Structure):
    SlotNumber: Byte
    ReadOnly: win32more.Foundation.BOOLEAN
    Reserved: Byte * 6
    Revision: Byte * 16
TARGETPROTOCOLTYPE = Int32
ISCSI_TCP_PROTOCOL_TYPE: TARGETPROTOCOLTYPE = 0
TARGET_INFORMATION_CLASS = Int32
TARGET_INFORMATION_CLASS_ProtocolType: TARGET_INFORMATION_CLASS = 0
TARGET_INFORMATION_CLASS_TargetAlias: TARGET_INFORMATION_CLASS = 1
TARGET_INFORMATION_CLASS_DiscoveryMechanisms: TARGET_INFORMATION_CLASS = 2
TARGET_INFORMATION_CLASS_PortalGroups: TARGET_INFORMATION_CLASS = 3
TARGET_INFORMATION_CLASS_PersistentTargetMappings: TARGET_INFORMATION_CLASS = 4
TARGET_INFORMATION_CLASS_InitiatorName: TARGET_INFORMATION_CLASS = 5
TARGET_INFORMATION_CLASS_TargetFlags: TARGET_INFORMATION_CLASS = 6
TARGET_INFORMATION_CLASS_LoginOptions: TARGET_INFORMATION_CLASS = 7
class _ADAPTER_OBJECT(Structure):
    pass
make_head(_module, 'ATA_PASS_THROUGH_DIRECT')
if ARCH in 'X64,ARM64':
    make_head(_module, 'ATA_PASS_THROUGH_DIRECT32')
make_head(_module, 'ATA_PASS_THROUGH_EX')
if ARCH in 'X64,ARM64':
    make_head(_module, 'ATA_PASS_THROUGH_EX32')
make_head(_module, 'DSM_NOTIFICATION_REQUEST_BLOCK')
make_head(_module, 'DUMP_DRIVER')
make_head(_module, 'DUMP_DRIVER_EX')
make_head(_module, 'DUMP_POINTERS')
make_head(_module, 'DUMP_POINTERS_EX')
make_head(_module, 'DUMP_POINTERS_VERSION')
make_head(_module, 'FIRMWARE_REQUEST_BLOCK')
make_head(_module, 'HYBRID_DEMOTE_BY_SIZE')
make_head(_module, 'HYBRID_DIRTY_THRESHOLDS')
make_head(_module, 'HYBRID_INFORMATION')
make_head(_module, 'HYBRID_REQUEST_BLOCK')
make_head(_module, 'IDE_IO_CONTROL')
make_head(_module, 'IKE_AUTHENTICATION_INFORMATION')
make_head(_module, 'IKE_AUTHENTICATION_PRESHARED_KEY')
make_head(_module, 'IO_SCSI_CAPABILITIES')
make_head(_module, 'ISCSI_CONNECTION_INFOA')
make_head(_module, 'ISCSI_CONNECTION_INFOW')
make_head(_module, 'ISCSI_CONNECTION_INFO_EX')
make_head(_module, 'ISCSI_DEVICE_ON_SESSIONA')
make_head(_module, 'ISCSI_DEVICE_ON_SESSIONW')
make_head(_module, 'ISCSI_LOGIN_OPTIONS')
make_head(_module, 'ISCSI_SESSION_INFOA')
make_head(_module, 'ISCSI_SESSION_INFOW')
make_head(_module, 'ISCSI_SESSION_INFO_EX')
make_head(_module, 'ISCSI_TARGET_MAPPINGA')
make_head(_module, 'ISCSI_TARGET_MAPPINGW')
make_head(_module, 'ISCSI_TARGET_PORTALA')
make_head(_module, 'ISCSI_TARGET_PORTALW')
make_head(_module, 'ISCSI_TARGET_PORTAL_GROUPA')
make_head(_module, 'ISCSI_TARGET_PORTAL_GROUPW')
make_head(_module, 'ISCSI_TARGET_PORTAL_INFOA')
make_head(_module, 'ISCSI_TARGET_PORTAL_INFOW')
make_head(_module, 'ISCSI_TARGET_PORTAL_INFO_EXA')
make_head(_module, 'ISCSI_TARGET_PORTAL_INFO_EXW')
make_head(_module, 'ISCSI_UNIQUE_SESSION_ID')
make_head(_module, 'ISCSI_VERSION_INFO')
make_head(_module, 'MPIO_PASS_THROUGH_PATH')
if ARCH in 'X64,ARM64':
    make_head(_module, 'MPIO_PASS_THROUGH_PATH32')
if ARCH in 'X64,ARM64':
    make_head(_module, 'MPIO_PASS_THROUGH_PATH32_EX')
make_head(_module, 'MPIO_PASS_THROUGH_PATH_DIRECT')
if ARCH in 'X64,ARM64':
    make_head(_module, 'MPIO_PASS_THROUGH_PATH_DIRECT32')
if ARCH in 'X64,ARM64':
    make_head(_module, 'MPIO_PASS_THROUGH_PATH_DIRECT32_EX')
make_head(_module, 'MPIO_PASS_THROUGH_PATH_DIRECT_EX')
make_head(_module, 'MPIO_PASS_THROUGH_PATH_EX')
make_head(_module, 'MP_DEVICE_DATA_SET_RANGE')
make_head(_module, 'NTSCSI_UNICODE_STRING')
make_head(_module, 'NVCACHE_HINT_PAYLOAD')
make_head(_module, 'NVCACHE_PRIORITY_LEVEL_DESCRIPTOR')
make_head(_module, 'NVCACHE_REQUEST_BLOCK')
make_head(_module, 'NV_FEATURE_PARAMETER')
make_head(_module, 'NV_SEP_CACHE_PARAMETER')
make_head(_module, 'PDUMP_DEVICE_POWERON_ROUTINE')
make_head(_module, 'PERSISTENT_ISCSI_LOGIN_INFOA')
make_head(_module, 'PERSISTENT_ISCSI_LOGIN_INFOW')
make_head(_module, 'SCSI_ADAPTER_BUS_INFO')
make_head(_module, 'SCSI_ADDRESS')
make_head(_module, 'SCSI_BUS_DATA')
make_head(_module, 'SCSI_INQUIRY_DATA')
make_head(_module, 'SCSI_LUN_LIST')
make_head(_module, 'SCSI_PASS_THROUGH')
if ARCH in 'X64,ARM64':
    make_head(_module, 'SCSI_PASS_THROUGH32')
if ARCH in 'X64,ARM64':
    make_head(_module, 'SCSI_PASS_THROUGH32_EX')
make_head(_module, 'SCSI_PASS_THROUGH_DIRECT')
if ARCH in 'X64,ARM64':
    make_head(_module, 'SCSI_PASS_THROUGH_DIRECT32')
if ARCH in 'X64,ARM64':
    make_head(_module, 'SCSI_PASS_THROUGH_DIRECT32_EX')
make_head(_module, 'SCSI_PASS_THROUGH_DIRECT_EX')
make_head(_module, 'SCSI_PASS_THROUGH_EX')
make_head(_module, 'SRB_IO_CONTROL')
make_head(_module, 'STORAGE_DIAGNOSTIC_MP_REQUEST')
make_head(_module, 'STORAGE_ENDURANCE_DATA_DESCRIPTOR')
make_head(_module, 'STORAGE_ENDURANCE_INFO')
make_head(_module, 'STORAGE_FIRMWARE_ACTIVATE')
make_head(_module, 'STORAGE_FIRMWARE_DOWNLOAD')
make_head(_module, 'STORAGE_FIRMWARE_DOWNLOAD_V2')
make_head(_module, 'STORAGE_FIRMWARE_INFO')
make_head(_module, 'STORAGE_FIRMWARE_INFO_V2')
make_head(_module, 'STORAGE_FIRMWARE_SLOT_INFO')
make_head(_module, 'STORAGE_FIRMWARE_SLOT_INFO_V2')
make_head(_module, '_ADAPTER_OBJECT')
__all__ = [
    "ATA_FLAGS_48BIT_COMMAND",
    "ATA_FLAGS_DATA_IN",
    "ATA_FLAGS_DATA_OUT",
    "ATA_FLAGS_DRDY_REQUIRED",
    "ATA_FLAGS_NO_MULTIPLE",
    "ATA_FLAGS_USE_DMA",
    "ATA_PASS_THROUGH_DIRECT",
    "ATA_PASS_THROUGH_DIRECT32",
    "ATA_PASS_THROUGH_EX",
    "ATA_PASS_THROUGH_EX32",
    "AddISNSServerA",
    "AddISNSServerW",
    "AddIScsiConnectionA",
    "AddIScsiConnectionW",
    "AddIScsiSendTargetPortalA",
    "AddIScsiSendTargetPortalW",
    "AddIScsiStaticTargetA",
    "AddIScsiStaticTargetW",
    "AddPersistentIScsiDeviceA",
    "AddPersistentIScsiDeviceW",
    "AddRadiusServerA",
    "AddRadiusServerW",
    "ClearPersistentIScsiDevices",
    "DD_SCSI_DEVICE_NAME",
    "DSM_NOTIFICATION_REQUEST_BLOCK",
    "DUMP_DRIVER",
    "DUMP_DRIVER_EX",
    "DUMP_DRIVER_NAME_LENGTH",
    "DUMP_EX_FLAG_DRIVER_FULL_PATH_SUPPORT",
    "DUMP_EX_FLAG_RESUME_SUPPORT",
    "DUMP_EX_FLAG_SUPPORT_64BITMEMORY",
    "DUMP_EX_FLAG_SUPPORT_DD_TELEMETRY",
    "DUMP_POINTERS",
    "DUMP_POINTERS_EX",
    "DUMP_POINTERS_VERSION",
    "DUMP_POINTERS_VERSION_1",
    "DUMP_POINTERS_VERSION_2",
    "DUMP_POINTERS_VERSION_3",
    "DUMP_POINTERS_VERSION_4",
    "FILE_DEVICE_SCSI",
    "FIRMWARE_FUNCTION_ACTIVATE",
    "FIRMWARE_FUNCTION_DOWNLOAD",
    "FIRMWARE_FUNCTION_GET_INFO",
    "FIRMWARE_REQUEST_BLOCK",
    "FIRMWARE_REQUEST_BLOCK_STRUCTURE_VERSION",
    "FIRMWARE_REQUEST_FLAG_CONTROLLER",
    "FIRMWARE_REQUEST_FLAG_FIRST_SEGMENT",
    "FIRMWARE_REQUEST_FLAG_LAST_SEGMENT",
    "FIRMWARE_REQUEST_FLAG_SWITCH_TO_EXISTING_FIRMWARE",
    "FIRMWARE_STATUS_COMMAND_ABORT",
    "FIRMWARE_STATUS_CONTROLLER_ERROR",
    "FIRMWARE_STATUS_DEVICE_ERROR",
    "FIRMWARE_STATUS_END_OF_MEDIA",
    "FIRMWARE_STATUS_ERROR",
    "FIRMWARE_STATUS_ID_NOT_FOUND",
    "FIRMWARE_STATUS_ILLEGAL_LENGTH",
    "FIRMWARE_STATUS_ILLEGAL_REQUEST",
    "FIRMWARE_STATUS_INPUT_BUFFER_TOO_BIG",
    "FIRMWARE_STATUS_INTERFACE_CRC_ERROR",
    "FIRMWARE_STATUS_INVALID_IMAGE",
    "FIRMWARE_STATUS_INVALID_PARAMETER",
    "FIRMWARE_STATUS_INVALID_SLOT",
    "FIRMWARE_STATUS_MEDIA_CHANGE",
    "FIRMWARE_STATUS_MEDIA_CHANGE_REQUEST",
    "FIRMWARE_STATUS_OUTPUT_BUFFER_TOO_SMALL",
    "FIRMWARE_STATUS_POWER_CYCLE_REQUIRED",
    "FIRMWARE_STATUS_SUCCESS",
    "FIRMWARE_STATUS_UNCORRECTABLE_DATA_ERROR",
    "GetDevicesForIScsiSessionA",
    "GetDevicesForIScsiSessionW",
    "GetIScsiIKEInfoA",
    "GetIScsiIKEInfoW",
    "GetIScsiInitiatorNodeNameA",
    "GetIScsiInitiatorNodeNameW",
    "GetIScsiSessionListA",
    "GetIScsiSessionListEx",
    "GetIScsiSessionListW",
    "GetIScsiTargetInformationA",
    "GetIScsiTargetInformationW",
    "GetIScsiVersionInformation",
    "HYBRID_DEMOTE_BY_SIZE",
    "HYBRID_DIRTY_THRESHOLDS",
    "HYBRID_FUNCTION_DEMOTE_BY_SIZE",
    "HYBRID_FUNCTION_DISABLE_CACHING_MEDIUM",
    "HYBRID_FUNCTION_ENABLE_CACHING_MEDIUM",
    "HYBRID_FUNCTION_GET_INFO",
    "HYBRID_FUNCTION_SET_DIRTY_THRESHOLD",
    "HYBRID_INFORMATION",
    "HYBRID_REQUEST_BLOCK",
    "HYBRID_REQUEST_BLOCK_STRUCTURE_VERSION",
    "HYBRID_REQUEST_INFO_STRUCTURE_VERSION",
    "HYBRID_STATUS_ENABLE_REFCOUNT_HOLD",
    "HYBRID_STATUS_ILLEGAL_REQUEST",
    "HYBRID_STATUS_INVALID_PARAMETER",
    "HYBRID_STATUS_OUTPUT_BUFFER_TOO_SMALL",
    "HYBRID_STATUS_SUCCESS",
    "IDE_IO_CONTROL",
    "ID_FQDN",
    "ID_IPV4_ADDR",
    "ID_IPV6_ADDR",
    "ID_USER_FQDN",
    "IKE_AUTHENTICATION_INFORMATION",
    "IKE_AUTHENTICATION_METHOD",
    "IKE_AUTHENTICATION_PRESHARED_KEY",
    "IKE_AUTHENTICATION_PRESHARED_KEY_METHOD",
    "IOCTL_ATA_MINIPORT",
    "IOCTL_ATA_PASS_THROUGH",
    "IOCTL_ATA_PASS_THROUGH_DIRECT",
    "IOCTL_IDE_PASS_THROUGH",
    "IOCTL_MINIPORT_PROCESS_SERVICE_IRP",
    "IOCTL_MINIPORT_SIGNATURE_DSM_GENERAL",
    "IOCTL_MINIPORT_SIGNATURE_DSM_NOTIFICATION",
    "IOCTL_MINIPORT_SIGNATURE_ENDURANCE_INFO",
    "IOCTL_MINIPORT_SIGNATURE_FIRMWARE",
    "IOCTL_MINIPORT_SIGNATURE_HYBRDISK",
    "IOCTL_MINIPORT_SIGNATURE_QUERY_PHYSICAL_TOPOLOGY",
    "IOCTL_MINIPORT_SIGNATURE_QUERY_PROTOCOL",
    "IOCTL_MINIPORT_SIGNATURE_QUERY_TEMPERATURE",
    "IOCTL_MINIPORT_SIGNATURE_SCSIDISK",
    "IOCTL_MINIPORT_SIGNATURE_SET_PROTOCOL",
    "IOCTL_MINIPORT_SIGNATURE_SET_TEMPERATURE_THRESHOLD",
    "IOCTL_MPIO_PASS_THROUGH_PATH",
    "IOCTL_MPIO_PASS_THROUGH_PATH_DIRECT",
    "IOCTL_MPIO_PASS_THROUGH_PATH_DIRECT_EX",
    "IOCTL_MPIO_PASS_THROUGH_PATH_EX",
    "IOCTL_SCSI_BASE",
    "IOCTL_SCSI_FREE_DUMP_POINTERS",
    "IOCTL_SCSI_GET_ADDRESS",
    "IOCTL_SCSI_GET_CAPABILITIES",
    "IOCTL_SCSI_GET_DUMP_POINTERS",
    "IOCTL_SCSI_GET_INQUIRY_DATA",
    "IOCTL_SCSI_MINIPORT",
    "IOCTL_SCSI_PASS_THROUGH",
    "IOCTL_SCSI_PASS_THROUGH_DIRECT",
    "IOCTL_SCSI_PASS_THROUGH_DIRECT_EX",
    "IOCTL_SCSI_PASS_THROUGH_EX",
    "IOCTL_SCSI_RESCAN_BUS",
    "IO_SCSI_CAPABILITIES",
    "ISCSI_AUTH_TYPES",
    "ISCSI_CHAP_AUTH_TYPE",
    "ISCSI_CONNECTION_INFOA",
    "ISCSI_CONNECTION_INFOW",
    "ISCSI_CONNECTION_INFO_EX",
    "ISCSI_DEVICE_ON_SESSIONA",
    "ISCSI_DEVICE_ON_SESSIONW",
    "ISCSI_DIGEST_TYPES",
    "ISCSI_DIGEST_TYPE_CRC32C",
    "ISCSI_DIGEST_TYPE_NONE",
    "ISCSI_LOGIN_FLAG_ALLOW_PORTAL_HOPPING",
    "ISCSI_LOGIN_FLAG_MULTIPATH_ENABLED",
    "ISCSI_LOGIN_FLAG_REQUIRE_IPSEC",
    "ISCSI_LOGIN_FLAG_RESERVED1",
    "ISCSI_LOGIN_FLAG_USE_RADIUS_RESPONSE",
    "ISCSI_LOGIN_FLAG_USE_RADIUS_VERIFICATION",
    "ISCSI_LOGIN_OPTIONS",
    "ISCSI_LOGIN_OPTIONS_AUTH_TYPE",
    "ISCSI_LOGIN_OPTIONS_DATA_DIGEST",
    "ISCSI_LOGIN_OPTIONS_DEFAULT_TIME_2_RETAIN",
    "ISCSI_LOGIN_OPTIONS_DEFAULT_TIME_2_WAIT",
    "ISCSI_LOGIN_OPTIONS_HEADER_DIGEST",
    "ISCSI_LOGIN_OPTIONS_MAXIMUM_CONNECTIONS",
    "ISCSI_LOGIN_OPTIONS_PASSWORD",
    "ISCSI_LOGIN_OPTIONS_USERNAME",
    "ISCSI_LOGIN_OPTIONS_VERSION",
    "ISCSI_MUTUAL_CHAP_AUTH_TYPE",
    "ISCSI_NO_AUTH_TYPE",
    "ISCSI_SECURITY_FLAG_AGGRESSIVE_MODE_ENABLED",
    "ISCSI_SECURITY_FLAG_IKE_IPSEC_ENABLED",
    "ISCSI_SECURITY_FLAG_MAIN_MODE_ENABLED",
    "ISCSI_SECURITY_FLAG_PFS_ENABLED",
    "ISCSI_SECURITY_FLAG_TRANSPORT_MODE_PREFERRED",
    "ISCSI_SECURITY_FLAG_TUNNEL_MODE_PREFERRED",
    "ISCSI_SECURITY_FLAG_VALID",
    "ISCSI_SESSION_INFOA",
    "ISCSI_SESSION_INFOW",
    "ISCSI_SESSION_INFO_EX",
    "ISCSI_TARGET_FLAG_HIDE_STATIC_TARGET",
    "ISCSI_TARGET_FLAG_MERGE_TARGET_INFORMATION",
    "ISCSI_TARGET_MAPPINGA",
    "ISCSI_TARGET_MAPPINGW",
    "ISCSI_TARGET_PORTALA",
    "ISCSI_TARGET_PORTALW",
    "ISCSI_TARGET_PORTAL_GROUPA",
    "ISCSI_TARGET_PORTAL_GROUPW",
    "ISCSI_TARGET_PORTAL_INFOA",
    "ISCSI_TARGET_PORTAL_INFOW",
    "ISCSI_TARGET_PORTAL_INFO_EXA",
    "ISCSI_TARGET_PORTAL_INFO_EXW",
    "ISCSI_TCP_PROTOCOL_TYPE",
    "ISCSI_UNIQUE_SESSION_ID",
    "ISCSI_VERSION_INFO",
    "LoginIScsiTargetA",
    "LoginIScsiTargetW",
    "LogoutIScsiTarget",
    "MAX_ISCSI_ALIAS_LEN",
    "MAX_ISCSI_DISCOVERY_DOMAIN_LEN",
    "MAX_ISCSI_HBANAME_LEN",
    "MAX_ISCSI_NAME_LEN",
    "MAX_ISCSI_PORTAL_ADDRESS_LEN",
    "MAX_ISCSI_PORTAL_ALIAS_LEN",
    "MAX_ISCSI_PORTAL_NAME_LEN",
    "MAX_ISCSI_TEXT_ADDRESS_LEN",
    "MAX_RADIUS_ADDRESS_LEN",
    "MINIPORT_DSM_NOTIFICATION_VERSION",
    "MINIPORT_DSM_NOTIFICATION_VERSION_1",
    "MINIPORT_DSM_NOTIFY_FLAG_BEGIN",
    "MINIPORT_DSM_NOTIFY_FLAG_END",
    "MINIPORT_DSM_PROFILE_CRASHDUMP_FILE",
    "MINIPORT_DSM_PROFILE_HIBERNATION_FILE",
    "MINIPORT_DSM_PROFILE_PAGE_FILE",
    "MINIPORT_DSM_PROFILE_UNKNOWN",
    "MPIO_IOCTL_FLAG_INVOLVE_DSM",
    "MPIO_IOCTL_FLAG_USE_PATHID",
    "MPIO_IOCTL_FLAG_USE_SCSIADDRESS",
    "MPIO_PASS_THROUGH_PATH",
    "MPIO_PASS_THROUGH_PATH32",
    "MPIO_PASS_THROUGH_PATH32_EX",
    "MPIO_PASS_THROUGH_PATH_DIRECT",
    "MPIO_PASS_THROUGH_PATH_DIRECT32",
    "MPIO_PASS_THROUGH_PATH_DIRECT32_EX",
    "MPIO_PASS_THROUGH_PATH_DIRECT_EX",
    "MPIO_PASS_THROUGH_PATH_EX",
    "MP_DEVICE_DATA_SET_RANGE",
    "MP_STORAGE_DIAGNOSTIC_LEVEL",
    "MP_STORAGE_DIAGNOSTIC_LEVEL_MpStorageDiagnosticLevelDefault",
    "MP_STORAGE_DIAGNOSTIC_LEVEL_MpStorageDiagnosticLevelMax",
    "MP_STORAGE_DIAGNOSTIC_TARGET_TYPE",
    "MP_STORAGE_DIAGNOSTIC_TARGET_TYPE_MpStorageDiagnosticTargetTypeHbaFirmware",
    "MP_STORAGE_DIAGNOSTIC_TARGET_TYPE_MpStorageDiagnosticTargetTypeMax",
    "MP_STORAGE_DIAGNOSTIC_TARGET_TYPE_MpStorageDiagnosticTargetTypeMiniport",
    "MP_STORAGE_DIAGNOSTIC_TARGET_TYPE_MpStorageDiagnosticTargetTypeUndefined",
    "NRB_FUNCTION_ADD_LBAS_PINNED_SET",
    "NRB_FUNCTION_FLUSH_NVCACHE",
    "NRB_FUNCTION_NVCACHE_INFO",
    "NRB_FUNCTION_NVCACHE_POWER_MODE_RETURN",
    "NRB_FUNCTION_NVCACHE_POWER_MODE_SET",
    "NRB_FUNCTION_NVSEPARATED_FLUSH",
    "NRB_FUNCTION_NVSEPARATED_INFO",
    "NRB_FUNCTION_NVSEPARATED_WB_DISABLE",
    "NRB_FUNCTION_NVSEPARATED_WB_REVERT_DEFAULT",
    "NRB_FUNCTION_PASS_HINT_PAYLOAD",
    "NRB_FUNCTION_QUERY_ASCENDER_STATUS",
    "NRB_FUNCTION_QUERY_CACHE_MISS",
    "NRB_FUNCTION_QUERY_HYBRID_DISK_STATUS",
    "NRB_FUNCTION_QUERY_PINNED_SET",
    "NRB_FUNCTION_REMOVE_LBAS_PINNED_SET",
    "NRB_FUNCTION_SPINDLE_STATUS",
    "NRB_ILLEGAL_REQUEST",
    "NRB_INPUT_DATA_OVERRUN",
    "NRB_INPUT_DATA_UNDERRUN",
    "NRB_INVALID_PARAMETER",
    "NRB_OUTPUT_DATA_OVERRUN",
    "NRB_OUTPUT_DATA_UNDERRUN",
    "NRB_SUCCESS",
    "NTSCSI_UNICODE_STRING",
    "NVCACHE_HINT_PAYLOAD",
    "NVCACHE_PRIORITY_LEVEL_DESCRIPTOR",
    "NVCACHE_REQUEST_BLOCK",
    "NVCACHE_STATUS",
    "NVCACHE_STATUS_NvCacheStatusDisabled",
    "NVCACHE_STATUS_NvCacheStatusDisabling",
    "NVCACHE_STATUS_NvCacheStatusEnabled",
    "NVCACHE_STATUS_NvCacheStatusUnknown",
    "NVCACHE_TYPE",
    "NVCACHE_TYPE_NvCacheTypeNone",
    "NVCACHE_TYPE_NvCacheTypeUnknown",
    "NVCACHE_TYPE_NvCacheTypeWriteBack",
    "NVCACHE_TYPE_NvCacheTypeWriteThrough",
    "NV_FEATURE_PARAMETER",
    "NV_SEP_CACHE_PARAMETER",
    "NV_SEP_CACHE_PARAMETER_VERSION",
    "NV_SEP_CACHE_PARAMETER_VERSION_1",
    "NV_SEP_WRITE_CACHE_TYPE",
    "NV_SEP_WRITE_CACHE_TYPE_NVSEPWriteCacheTypeNone",
    "NV_SEP_WRITE_CACHE_TYPE_NVSEPWriteCacheTypeUnknown",
    "NV_SEP_WRITE_CACHE_TYPE_NVSEPWriteCacheTypeWriteBack",
    "NV_SEP_WRITE_CACHE_TYPE_NVSEPWriteCacheTypeWriteThrough",
    "PDUMP_DEVICE_POWERON_ROUTINE",
    "PERSISTENT_ISCSI_LOGIN_INFOA",
    "PERSISTENT_ISCSI_LOGIN_INFOW",
    "RefreshISNSServerA",
    "RefreshISNSServerW",
    "RefreshIScsiSendTargetPortalA",
    "RefreshIScsiSendTargetPortalW",
    "RemoveISNSServerA",
    "RemoveISNSServerW",
    "RemoveIScsiConnection",
    "RemoveIScsiPersistentTargetA",
    "RemoveIScsiPersistentTargetW",
    "RemoveIScsiSendTargetPortalA",
    "RemoveIScsiSendTargetPortalW",
    "RemoveIScsiStaticTargetA",
    "RemoveIScsiStaticTargetW",
    "RemovePersistentIScsiDeviceA",
    "RemovePersistentIScsiDeviceW",
    "RemoveRadiusServerA",
    "RemoveRadiusServerW",
    "ReportActiveIScsiTargetMappingsA",
    "ReportActiveIScsiTargetMappingsW",
    "ReportISNSServerListA",
    "ReportISNSServerListW",
    "ReportIScsiInitiatorListA",
    "ReportIScsiInitiatorListW",
    "ReportIScsiPersistentLoginsA",
    "ReportIScsiPersistentLoginsW",
    "ReportIScsiSendTargetPortalsA",
    "ReportIScsiSendTargetPortalsExA",
    "ReportIScsiSendTargetPortalsExW",
    "ReportIScsiSendTargetPortalsW",
    "ReportIScsiTargetPortalsA",
    "ReportIScsiTargetPortalsW",
    "ReportIScsiTargetsA",
    "ReportIScsiTargetsW",
    "ReportPersistentIScsiDevicesA",
    "ReportPersistentIScsiDevicesW",
    "ReportRadiusServerListA",
    "ReportRadiusServerListW",
    "SCSI_ADAPTER_BUS_INFO",
    "SCSI_ADDRESS",
    "SCSI_BUS_DATA",
    "SCSI_INQUIRY_DATA",
    "SCSI_IOCTL_DATA_BIDIRECTIONAL",
    "SCSI_IOCTL_DATA_IN",
    "SCSI_IOCTL_DATA_OUT",
    "SCSI_IOCTL_DATA_UNSPECIFIED",
    "SCSI_LUN_LIST",
    "SCSI_PASS_THROUGH",
    "SCSI_PASS_THROUGH32",
    "SCSI_PASS_THROUGH32_EX",
    "SCSI_PASS_THROUGH_DIRECT",
    "SCSI_PASS_THROUGH_DIRECT32",
    "SCSI_PASS_THROUGH_DIRECT32_EX",
    "SCSI_PASS_THROUGH_DIRECT_EX",
    "SCSI_PASS_THROUGH_EX",
    "SRB_IO_CONTROL",
    "STORAGE_DIAGNOSTIC_MP_REQUEST",
    "STORAGE_DIAGNOSTIC_STATUS_BUFFER_TOO_SMALL",
    "STORAGE_DIAGNOSTIC_STATUS_INVALID_PARAMETER",
    "STORAGE_DIAGNOSTIC_STATUS_INVALID_SIGNATURE",
    "STORAGE_DIAGNOSTIC_STATUS_INVALID_TARGET_TYPE",
    "STORAGE_DIAGNOSTIC_STATUS_MORE_DATA",
    "STORAGE_DIAGNOSTIC_STATUS_SUCCESS",
    "STORAGE_DIAGNOSTIC_STATUS_UNSUPPORTED_VERSION",
    "STORAGE_ENDURANCE_DATA_DESCRIPTOR",
    "STORAGE_ENDURANCE_INFO",
    "STORAGE_FIRMWARE_ACTIVATE",
    "STORAGE_FIRMWARE_ACTIVATE_STRUCTURE_VERSION",
    "STORAGE_FIRMWARE_DOWNLOAD",
    "STORAGE_FIRMWARE_DOWNLOAD_STRUCTURE_VERSION",
    "STORAGE_FIRMWARE_DOWNLOAD_STRUCTURE_VERSION_V2",
    "STORAGE_FIRMWARE_DOWNLOAD_V2",
    "STORAGE_FIRMWARE_INFO",
    "STORAGE_FIRMWARE_INFO_INVALID_SLOT",
    "STORAGE_FIRMWARE_INFO_STRUCTURE_VERSION",
    "STORAGE_FIRMWARE_INFO_STRUCTURE_VERSION_V2",
    "STORAGE_FIRMWARE_INFO_V2",
    "STORAGE_FIRMWARE_SLOT_INFO",
    "STORAGE_FIRMWARE_SLOT_INFO_V2",
    "STORAGE_FIRMWARE_SLOT_INFO_V2_REVISION_LENGTH",
    "ScsiRawInterfaceGuid",
    "SendScsiInquiry",
    "SendScsiReadCapacity",
    "SendScsiReportLuns",
    "SetIScsiGroupPresharedKey",
    "SetIScsiIKEInfoA",
    "SetIScsiIKEInfoW",
    "SetIScsiInitiatorCHAPSharedSecret",
    "SetIScsiInitiatorNodeNameA",
    "SetIScsiInitiatorNodeNameW",
    "SetIScsiInitiatorRADIUSSharedSecret",
    "SetIScsiTunnelModeOuterAddressA",
    "SetIScsiTunnelModeOuterAddressW",
    "SetupPersistentIScsiDevices",
    "SetupPersistentIScsiVolumes",
    "TARGETPROTOCOLTYPE",
    "TARGET_INFORMATION_CLASS",
    "TARGET_INFORMATION_CLASS_DiscoveryMechanisms",
    "TARGET_INFORMATION_CLASS_InitiatorName",
    "TARGET_INFORMATION_CLASS_LoginOptions",
    "TARGET_INFORMATION_CLASS_PersistentTargetMappings",
    "TARGET_INFORMATION_CLASS_PortalGroups",
    "TARGET_INFORMATION_CLASS_ProtocolType",
    "TARGET_INFORMATION_CLASS_TargetAlias",
    "TARGET_INFORMATION_CLASS_TargetFlags",
    "WmiScsiAddressGuid",
    "_ADAPTER_OBJECT",
]
_arch_optional = [
    "ATA_PASS_THROUGH_DIRECT32",
    "ATA_PASS_THROUGH_EX32",
    "MPIO_PASS_THROUGH_PATH32",
    "MPIO_PASS_THROUGH_PATH32_EX",
    "MPIO_PASS_THROUGH_PATH_DIRECT32",
    "MPIO_PASS_THROUGH_PATH_DIRECT32_EX",
    "SCSI_PASS_THROUGH32",
    "SCSI_PASS_THROUGH32_EX",
    "SCSI_PASS_THROUGH_DIRECT32",
    "SCSI_PASS_THROUGH_DIRECT32_EX",
]
