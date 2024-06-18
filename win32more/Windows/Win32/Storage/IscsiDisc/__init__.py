from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Storage.IscsiDisc
import win32more.Windows.Win32.System.Ioctl
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
    DataBuffer: VoidPtr
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
        DataBuffer: VoidPtr
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
ScsiRawInterfaceGuid: Guid = Guid('{53f56309-b6bf-11d0-94f2-00a0c91efb8b}')
WmiScsiAddressGuid: Guid = Guid('{53f5630f-b6bf-11d0-94f2-00a0c91efb8b}')
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
FIRMWARE_REQUEST_FLAG_REPLACE_EXISTING_IMAGE: UInt32 = 1073741824
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
def GetIScsiVersionInformation(VersionInfo: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_VERSION_INFO)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def GetIScsiTargetInformationW(TargetName: win32more.Windows.Win32.Foundation.PWSTR, DiscoveryMechanism: win32more.Windows.Win32.Foundation.PWSTR, InfoClass: win32more.Windows.Win32.Storage.IscsiDisc.TARGET_INFORMATION_CLASS, BufferSize: POINTER(UInt32), Buffer: VoidPtr) -> UInt32: ...
GetIScsiTargetInformation = UnicodeAlias('GetIScsiTargetInformationW')
@winfunctype('ISCSIDSC.dll')
def GetIScsiTargetInformationA(TargetName: win32more.Windows.Win32.Foundation.PSTR, DiscoveryMechanism: win32more.Windows.Win32.Foundation.PSTR, InfoClass: win32more.Windows.Win32.Storage.IscsiDisc.TARGET_INFORMATION_CLASS, BufferSize: POINTER(UInt32), Buffer: VoidPtr) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def AddIScsiConnectionW(UniqueSessionId: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID), Reserved: VoidPtr, InitiatorPortNumber: UInt32, TargetPortal: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_TARGET_PORTALW), SecurityFlags: UInt64, LoginOptions: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_LOGIN_OPTIONS), KeySize: UInt32, Key: win32more.Windows.Win32.Foundation.PSTR, ConnectionId: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID)) -> UInt32: ...
AddIScsiConnection = UnicodeAlias('AddIScsiConnectionW')
@winfunctype('ISCSIDSC.dll')
def AddIScsiConnectionA(UniqueSessionId: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID), Reserved: VoidPtr, InitiatorPortNumber: UInt32, TargetPortal: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_TARGET_PORTALA), SecurityFlags: UInt64, LoginOptions: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_LOGIN_OPTIONS), KeySize: UInt32, Key: win32more.Windows.Win32.Foundation.PSTR, ConnectionId: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def RemoveIScsiConnection(UniqueSessionId: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID), ConnectionId: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def ReportIScsiTargetsW(ForceUpdate: win32more.Windows.Win32.Foundation.BOOLEAN, BufferSize: POINTER(UInt32), Buffer: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
ReportIScsiTargets = UnicodeAlias('ReportIScsiTargetsW')
@winfunctype('ISCSIDSC.dll')
def ReportIScsiTargetsA(ForceUpdate: win32more.Windows.Win32.Foundation.BOOLEAN, BufferSize: POINTER(UInt32), Buffer: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def AddIScsiStaticTargetW(TargetName: win32more.Windows.Win32.Foundation.PWSTR, TargetAlias: win32more.Windows.Win32.Foundation.PWSTR, TargetFlags: UInt32, Persist: win32more.Windows.Win32.Foundation.BOOLEAN, Mappings: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_TARGET_MAPPINGW), LoginOptions: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_LOGIN_OPTIONS), PortalGroup: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_TARGET_PORTAL_GROUPW)) -> UInt32: ...
AddIScsiStaticTarget = UnicodeAlias('AddIScsiStaticTargetW')
@winfunctype('ISCSIDSC.dll')
def AddIScsiStaticTargetA(TargetName: win32more.Windows.Win32.Foundation.PSTR, TargetAlias: win32more.Windows.Win32.Foundation.PSTR, TargetFlags: UInt32, Persist: win32more.Windows.Win32.Foundation.BOOLEAN, Mappings: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_TARGET_MAPPINGA), LoginOptions: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_LOGIN_OPTIONS), PortalGroup: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_TARGET_PORTAL_GROUPA)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def RemoveIScsiStaticTargetW(TargetName: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
RemoveIScsiStaticTarget = UnicodeAlias('RemoveIScsiStaticTargetW')
@winfunctype('ISCSIDSC.dll')
def RemoveIScsiStaticTargetA(TargetName: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def AddIScsiSendTargetPortalW(InitiatorInstance: win32more.Windows.Win32.Foundation.PWSTR, InitiatorPortNumber: UInt32, LoginOptions: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_LOGIN_OPTIONS), SecurityFlags: UInt64, Portal: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_TARGET_PORTALW)) -> UInt32: ...
AddIScsiSendTargetPortal = UnicodeAlias('AddIScsiSendTargetPortalW')
@winfunctype('ISCSIDSC.dll')
def AddIScsiSendTargetPortalA(InitiatorInstance: win32more.Windows.Win32.Foundation.PSTR, InitiatorPortNumber: UInt32, LoginOptions: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_LOGIN_OPTIONS), SecurityFlags: UInt64, Portal: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_TARGET_PORTALA)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def RemoveIScsiSendTargetPortalW(InitiatorInstance: win32more.Windows.Win32.Foundation.PWSTR, InitiatorPortNumber: UInt32, Portal: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_TARGET_PORTALW)) -> UInt32: ...
RemoveIScsiSendTargetPortal = UnicodeAlias('RemoveIScsiSendTargetPortalW')
@winfunctype('ISCSIDSC.dll')
def RemoveIScsiSendTargetPortalA(InitiatorInstance: win32more.Windows.Win32.Foundation.PSTR, InitiatorPortNumber: UInt32, Portal: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_TARGET_PORTALA)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def RefreshIScsiSendTargetPortalW(InitiatorInstance: win32more.Windows.Win32.Foundation.PWSTR, InitiatorPortNumber: UInt32, Portal: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_TARGET_PORTALW)) -> UInt32: ...
RefreshIScsiSendTargetPortal = UnicodeAlias('RefreshIScsiSendTargetPortalW')
@winfunctype('ISCSIDSC.dll')
def RefreshIScsiSendTargetPortalA(InitiatorInstance: win32more.Windows.Win32.Foundation.PSTR, InitiatorPortNumber: UInt32, Portal: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_TARGET_PORTALA)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def ReportIScsiSendTargetPortalsW(PortalCount: POINTER(UInt32), PortalInfo: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_TARGET_PORTAL_INFOW)) -> UInt32: ...
ReportIScsiSendTargetPortals = UnicodeAlias('ReportIScsiSendTargetPortalsW')
@winfunctype('ISCSIDSC.dll')
def ReportIScsiSendTargetPortalsA(PortalCount: POINTER(UInt32), PortalInfo: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_TARGET_PORTAL_INFOA)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def ReportIScsiSendTargetPortalsExW(PortalCount: POINTER(UInt32), PortalInfoSize: POINTER(UInt32), PortalInfo: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_TARGET_PORTAL_INFO_EXW)) -> UInt32: ...
ReportIScsiSendTargetPortalsEx = UnicodeAlias('ReportIScsiSendTargetPortalsExW')
@winfunctype('ISCSIDSC.dll')
def ReportIScsiSendTargetPortalsExA(PortalCount: POINTER(UInt32), PortalInfoSize: POINTER(UInt32), PortalInfo: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_TARGET_PORTAL_INFO_EXA)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def LoginIScsiTargetW(TargetName: win32more.Windows.Win32.Foundation.PWSTR, IsInformationalSession: win32more.Windows.Win32.Foundation.BOOLEAN, InitiatorInstance: win32more.Windows.Win32.Foundation.PWSTR, InitiatorPortNumber: UInt32, TargetPortal: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_TARGET_PORTALW), SecurityFlags: UInt64, Mappings: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_TARGET_MAPPINGW), LoginOptions: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_LOGIN_OPTIONS), KeySize: UInt32, Key: win32more.Windows.Win32.Foundation.PSTR, IsPersistent: win32more.Windows.Win32.Foundation.BOOLEAN, UniqueSessionId: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID), UniqueConnectionId: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID)) -> UInt32: ...
LoginIScsiTarget = UnicodeAlias('LoginIScsiTargetW')
@winfunctype('ISCSIDSC.dll')
def LoginIScsiTargetA(TargetName: win32more.Windows.Win32.Foundation.PSTR, IsInformationalSession: win32more.Windows.Win32.Foundation.BOOLEAN, InitiatorInstance: win32more.Windows.Win32.Foundation.PSTR, InitiatorPortNumber: UInt32, TargetPortal: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_TARGET_PORTALA), SecurityFlags: UInt64, Mappings: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_TARGET_MAPPINGA), LoginOptions: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_LOGIN_OPTIONS), KeySize: UInt32, Key: win32more.Windows.Win32.Foundation.PSTR, IsPersistent: win32more.Windows.Win32.Foundation.BOOLEAN, UniqueSessionId: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID), UniqueConnectionId: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def ReportIScsiPersistentLoginsW(Count: POINTER(UInt32), PersistentLoginInfo: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.PERSISTENT_ISCSI_LOGIN_INFOW), BufferSizeInBytes: POINTER(UInt32)) -> UInt32: ...
ReportIScsiPersistentLogins = UnicodeAlias('ReportIScsiPersistentLoginsW')
@winfunctype('ISCSIDSC.dll')
def ReportIScsiPersistentLoginsA(Count: POINTER(UInt32), PersistentLoginInfo: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.PERSISTENT_ISCSI_LOGIN_INFOA), BufferSizeInBytes: POINTER(UInt32)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def LogoutIScsiTarget(UniqueSessionId: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def RemoveIScsiPersistentTargetW(InitiatorInstance: win32more.Windows.Win32.Foundation.PWSTR, InitiatorPortNumber: UInt32, TargetName: win32more.Windows.Win32.Foundation.PWSTR, Portal: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_TARGET_PORTALW)) -> UInt32: ...
RemoveIScsiPersistentTarget = UnicodeAlias('RemoveIScsiPersistentTargetW')
@winfunctype('ISCSIDSC.dll')
def RemoveIScsiPersistentTargetA(InitiatorInstance: win32more.Windows.Win32.Foundation.PSTR, InitiatorPortNumber: UInt32, TargetName: win32more.Windows.Win32.Foundation.PSTR, Portal: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_TARGET_PORTALA)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def SendScsiInquiry(UniqueSessionId: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID), Lun: UInt64, EvpdCmddt: Byte, PageCode: Byte, ScsiStatus: POINTER(Byte), ResponseSize: POINTER(UInt32), ResponseBuffer: POINTER(Byte), SenseSize: POINTER(UInt32), SenseBuffer: POINTER(Byte)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def SendScsiReadCapacity(UniqueSessionId: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID), Lun: UInt64, ScsiStatus: POINTER(Byte), ResponseSize: POINTER(UInt32), ResponseBuffer: POINTER(Byte), SenseSize: POINTER(UInt32), SenseBuffer: POINTER(Byte)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def SendScsiReportLuns(UniqueSessionId: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID), ScsiStatus: POINTER(Byte), ResponseSize: POINTER(UInt32), ResponseBuffer: POINTER(Byte), SenseSize: POINTER(UInt32), SenseBuffer: POINTER(Byte)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def ReportIScsiInitiatorListW(BufferSize: POINTER(UInt32), Buffer: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
ReportIScsiInitiatorList = UnicodeAlias('ReportIScsiInitiatorListW')
@winfunctype('ISCSIDSC.dll')
def ReportIScsiInitiatorListA(BufferSize: POINTER(UInt32), Buffer: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def ReportActiveIScsiTargetMappingsW(BufferSize: POINTER(UInt32), MappingCount: POINTER(UInt32), Mappings: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_TARGET_MAPPINGW)) -> UInt32: ...
ReportActiveIScsiTargetMappings = UnicodeAlias('ReportActiveIScsiTargetMappingsW')
@winfunctype('ISCSIDSC.dll')
def ReportActiveIScsiTargetMappingsA(BufferSize: POINTER(UInt32), MappingCount: POINTER(UInt32), Mappings: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_TARGET_MAPPINGA)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def SetIScsiTunnelModeOuterAddressW(InitiatorName: win32more.Windows.Win32.Foundation.PWSTR, InitiatorPortNumber: UInt32, DestinationAddress: win32more.Windows.Win32.Foundation.PWSTR, OuterModeAddress: win32more.Windows.Win32.Foundation.PWSTR, Persist: win32more.Windows.Win32.Foundation.BOOLEAN) -> UInt32: ...
SetIScsiTunnelModeOuterAddress = UnicodeAlias('SetIScsiTunnelModeOuterAddressW')
@winfunctype('ISCSIDSC.dll')
def SetIScsiTunnelModeOuterAddressA(InitiatorName: win32more.Windows.Win32.Foundation.PSTR, InitiatorPortNumber: UInt32, DestinationAddress: win32more.Windows.Win32.Foundation.PSTR, OuterModeAddress: win32more.Windows.Win32.Foundation.PSTR, Persist: win32more.Windows.Win32.Foundation.BOOLEAN) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def SetIScsiIKEInfoW(InitiatorName: win32more.Windows.Win32.Foundation.PWSTR, InitiatorPortNumber: UInt32, AuthInfo: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.IKE_AUTHENTICATION_INFORMATION), Persist: win32more.Windows.Win32.Foundation.BOOLEAN) -> UInt32: ...
SetIScsiIKEInfo = UnicodeAlias('SetIScsiIKEInfoW')
@winfunctype('ISCSIDSC.dll')
def SetIScsiIKEInfoA(InitiatorName: win32more.Windows.Win32.Foundation.PSTR, InitiatorPortNumber: UInt32, AuthInfo: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.IKE_AUTHENTICATION_INFORMATION), Persist: win32more.Windows.Win32.Foundation.BOOLEAN) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def GetIScsiIKEInfoW(InitiatorName: win32more.Windows.Win32.Foundation.PWSTR, InitiatorPortNumber: UInt32, Reserved: POINTER(UInt32), AuthInfo: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.IKE_AUTHENTICATION_INFORMATION)) -> UInt32: ...
GetIScsiIKEInfo = UnicodeAlias('GetIScsiIKEInfoW')
@winfunctype('ISCSIDSC.dll')
def GetIScsiIKEInfoA(InitiatorName: win32more.Windows.Win32.Foundation.PSTR, InitiatorPortNumber: UInt32, Reserved: POINTER(UInt32), AuthInfo: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.IKE_AUTHENTICATION_INFORMATION)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def SetIScsiGroupPresharedKey(KeyLength: UInt32, Key: POINTER(Byte), Persist: win32more.Windows.Win32.Foundation.BOOLEAN) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def SetIScsiInitiatorCHAPSharedSecret(SharedSecretLength: UInt32, SharedSecret: POINTER(Byte)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def SetIScsiInitiatorRADIUSSharedSecret(SharedSecretLength: UInt32, SharedSecret: POINTER(Byte)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def SetIScsiInitiatorNodeNameW(InitiatorNodeName: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
SetIScsiInitiatorNodeName = UnicodeAlias('SetIScsiInitiatorNodeNameW')
@winfunctype('ISCSIDSC.dll')
def SetIScsiInitiatorNodeNameA(InitiatorNodeName: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def GetIScsiInitiatorNodeNameW(InitiatorNodeName: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
GetIScsiInitiatorNodeName = UnicodeAlias('GetIScsiInitiatorNodeNameW')
@winfunctype('ISCSIDSC.dll')
def GetIScsiInitiatorNodeNameA(InitiatorNodeName: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def AddISNSServerW(Address: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
AddISNSServer = UnicodeAlias('AddISNSServerW')
@winfunctype('ISCSIDSC.dll')
def AddISNSServerA(Address: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def RemoveISNSServerW(Address: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
RemoveISNSServer = UnicodeAlias('RemoveISNSServerW')
@winfunctype('ISCSIDSC.dll')
def RemoveISNSServerA(Address: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def RefreshISNSServerW(Address: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
RefreshISNSServer = UnicodeAlias('RefreshISNSServerW')
@winfunctype('ISCSIDSC.dll')
def RefreshISNSServerA(Address: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def ReportISNSServerListW(BufferSizeInChar: POINTER(UInt32), Buffer: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
ReportISNSServerList = UnicodeAlias('ReportISNSServerListW')
@winfunctype('ISCSIDSC.dll')
def ReportISNSServerListA(BufferSizeInChar: POINTER(UInt32), Buffer: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def GetIScsiSessionListW(BufferSize: POINTER(UInt32), SessionCount: POINTER(UInt32), SessionInfo: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_SESSION_INFOW)) -> UInt32: ...
GetIScsiSessionList = UnicodeAlias('GetIScsiSessionListW')
@winfunctype('ISCSIDSC.dll')
def GetIScsiSessionListA(BufferSize: POINTER(UInt32), SessionCount: POINTER(UInt32), SessionInfo: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_SESSION_INFOA)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def GetIScsiSessionListEx(BufferSize: POINTER(UInt32), SessionCountPtr: POINTER(UInt32), SessionInfo: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_SESSION_INFO_EX)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def GetDevicesForIScsiSessionW(UniqueSessionId: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID), DeviceCount: POINTER(UInt32), Devices: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_DEVICE_ON_SESSIONW)) -> UInt32: ...
GetDevicesForIScsiSession = UnicodeAlias('GetDevicesForIScsiSessionW')
@winfunctype('ISCSIDSC.dll')
def GetDevicesForIScsiSessionA(UniqueSessionId: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID), DeviceCount: POINTER(UInt32), Devices: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_DEVICE_ON_SESSIONA)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def SetupPersistentIScsiVolumes() -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def SetupPersistentIScsiDevices() -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def AddPersistentIScsiDeviceW(DevicePath: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
AddPersistentIScsiDevice = UnicodeAlias('AddPersistentIScsiDeviceW')
@winfunctype('ISCSIDSC.dll')
def AddPersistentIScsiDeviceA(DevicePath: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def RemovePersistentIScsiDeviceW(DevicePath: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
RemovePersistentIScsiDevice = UnicodeAlias('RemovePersistentIScsiDeviceW')
@winfunctype('ISCSIDSC.dll')
def RemovePersistentIScsiDeviceA(DevicePath: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def ClearPersistentIScsiDevices() -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def ReportPersistentIScsiDevicesW(BufferSizeInChar: POINTER(UInt32), Buffer: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
ReportPersistentIScsiDevices = UnicodeAlias('ReportPersistentIScsiDevicesW')
@winfunctype('ISCSIDSC.dll')
def ReportPersistentIScsiDevicesA(BufferSizeInChar: POINTER(UInt32), Buffer: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def ReportIScsiTargetPortalsW(InitiatorName: win32more.Windows.Win32.Foundation.PWSTR, TargetName: win32more.Windows.Win32.Foundation.PWSTR, TargetPortalTag: POINTER(UInt16), ElementCount: POINTER(UInt32), Portals: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_TARGET_PORTALW)) -> UInt32: ...
ReportIScsiTargetPortals = UnicodeAlias('ReportIScsiTargetPortalsW')
@winfunctype('ISCSIDSC.dll')
def ReportIScsiTargetPortalsA(InitiatorName: win32more.Windows.Win32.Foundation.PSTR, TargetName: win32more.Windows.Win32.Foundation.PSTR, TargetPortalTag: POINTER(UInt16), ElementCount: POINTER(UInt32), Portals: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_TARGET_PORTALA)) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def AddRadiusServerW(Address: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
AddRadiusServer = UnicodeAlias('AddRadiusServerW')
@winfunctype('ISCSIDSC.dll')
def AddRadiusServerA(Address: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def RemoveRadiusServerW(Address: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
RemoveRadiusServer = UnicodeAlias('RemoveRadiusServerW')
@winfunctype('ISCSIDSC.dll')
def RemoveRadiusServerA(Address: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('ISCSIDSC.dll')
def ReportRadiusServerListW(BufferSizeInChar: POINTER(UInt32), Buffer: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
ReportRadiusServerList = UnicodeAlias('ReportRadiusServerListW')
@winfunctype('ISCSIDSC.dll')
def ReportRadiusServerListA(BufferSizeInChar: POINTER(UInt32), Buffer: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
class DSM_NOTIFICATION_REQUEST_BLOCK(Structure):
    Size: UInt32
    Version: UInt32
    NotifyFlags: UInt32
    DataSetProfile: UInt32
    Reserved: UInt32 * 3
    DataSetRangesCount: UInt32
    DataSetRanges: win32more.Windows.Win32.Storage.IscsiDisc.MP_DEVICE_DATA_SET_RANGE * 1
class DUMP_DRIVER(Structure):
    DumpDriverList: VoidPtr
    DriverName: Char * 15
    BaseName: Char * 15
class DUMP_DRIVER_EX(Structure):
    DumpDriverList: VoidPtr
    DriverName: Char * 15
    BaseName: Char * 15
    DriverFullPath: win32more.Windows.Win32.Storage.IscsiDisc.NTSCSI_UNICODE_STRING
class DUMP_POINTERS(Structure):
    AdapterObject: POINTER(win32more.Windows.Win32.Storage.IscsiDisc._ADAPTER_OBJECT)
    MappedRegisterBase: VoidPtr
    DumpData: VoidPtr
    CommonBufferVa: VoidPtr
    CommonBufferPa: Int64
    CommonBufferSize: UInt32
    AllocateCommonBuffers: win32more.Windows.Win32.Foundation.BOOLEAN
    UseDiskDump: win32more.Windows.Win32.Foundation.BOOLEAN
    Spare1: Byte * 2
    DeviceObject: VoidPtr
class DUMP_POINTERS_EX(Structure):
    Header: win32more.Windows.Win32.Storage.IscsiDisc.DUMP_POINTERS_VERSION
    DumpData: VoidPtr
    CommonBufferVa: VoidPtr
    CommonBufferSize: UInt32
    AllocateCommonBuffers: win32more.Windows.Win32.Foundation.BOOLEAN
    DeviceObject: VoidPtr
    DriverList: VoidPtr
    dwPortFlags: UInt32
    MaxDeviceDumpSectionSize: UInt32
    MaxDeviceDumpLevel: UInt32
    MaxTransferSize: UInt32
    AdapterObject: VoidPtr
    MappedRegisterBase: VoidPtr
    DeviceReady: POINTER(win32more.Windows.Win32.Foundation.BOOLEAN)
    DumpDevicePowerOn: win32more.Windows.Win32.Storage.IscsiDisc.PDUMP_DEVICE_POWERON_ROUTINE
    DumpDevicePowerOnContext: VoidPtr
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
    HybridSupported: win32more.Windows.Win32.Foundation.BOOLEAN
    Status: win32more.Windows.Win32.Storage.IscsiDisc.NVCACHE_STATUS
    CacheTypeEffective: win32more.Windows.Win32.Storage.IscsiDisc.NVCACHE_TYPE
    CacheTypeDefault: win32more.Windows.Win32.Storage.IscsiDisc.NVCACHE_TYPE
    FractionBase: UInt32
    CacheSize: UInt64
    Attributes: _Attributes_e__Struct
    Priorities: _Priorities_e__Struct
    class _Attributes_e__Struct(Structure):
        WriteCacheChangeable: Annotated[UInt32, 1]
        WriteThroughIoSupported: Annotated[UInt32, 1]
        FlushCacheSupported: Annotated[UInt32, 1]
        Removable: Annotated[UInt32, 1]
        ReservedBits: Annotated[UInt32, 28]
    class _Priorities_e__Struct(Structure):
        PriorityLevelCount: Byte
        MaxPriorityBehavior: win32more.Windows.Win32.Foundation.BOOLEAN
        OptimalWriteGranularity: Byte
        Reserved: Byte
        DirtyThresholdLow: UInt32
        DirtyThresholdHigh: UInt32
        SupportedCommands: _SupportedCommands_e__Struct
        Priority: win32more.Windows.Win32.Storage.IscsiDisc.NVCACHE_PRIORITY_LEVEL_DESCRIPTOR * 1
        class _SupportedCommands_e__Struct(Structure):
            CacheDisable: Annotated[UInt32, 1]
            SetDirtyThreshold: Annotated[UInt32, 1]
            PriorityDemoteBySize: Annotated[UInt32, 1]
            PriorityChangeByLbaRange: Annotated[UInt32, 1]
            Evict: Annotated[UInt32, 1]
            ReservedBits: Annotated[UInt32, 27]
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
    AuthMethod: win32more.Windows.Win32.Storage.IscsiDisc.IKE_AUTHENTICATION_METHOD
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        PsKey: win32more.Windows.Win32.Storage.IscsiDisc.IKE_AUTHENTICATION_PRESHARED_KEY
IKE_AUTHENTICATION_METHOD = Int32
IKE_AUTHENTICATION_PRESHARED_KEY_METHOD: win32more.Windows.Win32.Storage.IscsiDisc.IKE_AUTHENTICATION_METHOD = 1
class IKE_AUTHENTICATION_PRESHARED_KEY(Structure):
    SecurityFlags: UInt64
    IdType: Byte
    IdLengthInBytes: UInt32
    Id: POINTER(Byte)
    KeyLengthInBytes: UInt32
    Key: POINTER(Byte)
class IO_SCSI_CAPABILITIES(Structure):
    Length: UInt32
    MaximumTransferLength: UInt32
    MaximumPhysicalPages: UInt32
    SupportedAsynchronousEvents: UInt32
    AlignmentMask: UInt32
    TaggedQueuing: win32more.Windows.Win32.Foundation.BOOLEAN
    AdapterScansDown: win32more.Windows.Win32.Foundation.BOOLEAN
    AdapterUsesPio: win32more.Windows.Win32.Foundation.BOOLEAN
ISCSI_AUTH_TYPES = Int32
ISCSI_NO_AUTH_TYPE: win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_AUTH_TYPES = 0
ISCSI_CHAP_AUTH_TYPE: win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_AUTH_TYPES = 1
ISCSI_MUTUAL_CHAP_AUTH_TYPE: win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_AUTH_TYPES = 2
class ISCSI_CONNECTION_INFOA(Structure):
    ConnectionId: win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID
    InitiatorAddress: win32more.Windows.Win32.Foundation.PSTR
    TargetAddress: win32more.Windows.Win32.Foundation.PSTR
    InitiatorSocket: UInt16
    TargetSocket: UInt16
    CID: Byte * 2
class ISCSI_CONNECTION_INFOW(Structure):
    ConnectionId: win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID
    InitiatorAddress: win32more.Windows.Win32.Foundation.PWSTR
    TargetAddress: win32more.Windows.Win32.Foundation.PWSTR
    InitiatorSocket: UInt16
    TargetSocket: UInt16
    CID: Byte * 2
ISCSI_CONNECTION_INFO = UnicodeAlias('ISCSI_CONNECTION_INFOW')
class ISCSI_CONNECTION_INFO_EX(Structure):
    ConnectionId: win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID
    State: Byte
    Protocol: Byte
    HeaderDigest: Byte
    DataDigest: Byte
    MaxRecvDataSegmentLength: UInt32
    AuthType: win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_AUTH_TYPES
    EstimatedThroughput: UInt64
    MaxDatagramSize: UInt32
class ISCSI_DEVICE_ON_SESSIONA(Structure):
    InitiatorName: win32more.Windows.Win32.Foundation.CHAR * 256
    TargetName: win32more.Windows.Win32.Foundation.CHAR * 224
    ScsiAddress: win32more.Windows.Win32.Storage.IscsiDisc.SCSI_ADDRESS
    DeviceInterfaceType: Guid
    DeviceInterfaceName: win32more.Windows.Win32.Foundation.CHAR * 260
    LegacyName: win32more.Windows.Win32.Foundation.CHAR * 260
    StorageDeviceNumber: win32more.Windows.Win32.System.Ioctl.STORAGE_DEVICE_NUMBER
    DeviceInstance: UInt32
class ISCSI_DEVICE_ON_SESSIONW(Structure):
    InitiatorName: Char * 256
    TargetName: Char * 224
    ScsiAddress: win32more.Windows.Win32.Storage.IscsiDisc.SCSI_ADDRESS
    DeviceInterfaceType: Guid
    DeviceInterfaceName: Char * 260
    LegacyName: Char * 260
    StorageDeviceNumber: win32more.Windows.Win32.System.Ioctl.STORAGE_DEVICE_NUMBER
    DeviceInstance: UInt32
ISCSI_DEVICE_ON_SESSION = UnicodeAlias('ISCSI_DEVICE_ON_SESSIONW')
ISCSI_DIGEST_TYPES = Int32
ISCSI_DIGEST_TYPE_NONE: win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_DIGEST_TYPES = 0
ISCSI_DIGEST_TYPE_CRC32C: win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_DIGEST_TYPES = 1
class ISCSI_LOGIN_OPTIONS(Structure):
    Version: UInt32
    InformationSpecified: UInt32
    LoginFlags: UInt32
    AuthType: win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_AUTH_TYPES
    HeaderDigest: win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_DIGEST_TYPES
    DataDigest: win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_DIGEST_TYPES
    MaximumConnections: UInt32
    DefaultTime2Wait: UInt32
    DefaultTime2Retain: UInt32
    UsernameLength: UInt32
    PasswordLength: UInt32
    Username: POINTER(Byte)
    Password: POINTER(Byte)
class ISCSI_SESSION_INFOA(Structure):
    SessionId: win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID
    InitiatorName: win32more.Windows.Win32.Foundation.PSTR
    TargetNodeName: win32more.Windows.Win32.Foundation.PSTR
    TargetName: win32more.Windows.Win32.Foundation.PSTR
    ISID: Byte * 6
    TSID: Byte * 2
    ConnectionCount: UInt32
    Connections: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_CONNECTION_INFOA)
class ISCSI_SESSION_INFOW(Structure):
    SessionId: win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID
    InitiatorName: win32more.Windows.Win32.Foundation.PWSTR
    TargetNodeName: win32more.Windows.Win32.Foundation.PWSTR
    TargetName: win32more.Windows.Win32.Foundation.PWSTR
    ISID: Byte * 6
    TSID: Byte * 2
    ConnectionCount: UInt32
    Connections: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_CONNECTION_INFOW)
ISCSI_SESSION_INFO = UnicodeAlias('ISCSI_SESSION_INFOW')
class ISCSI_SESSION_INFO_EX(Structure):
    SessionId: win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID
    InitialR2t: win32more.Windows.Win32.Foundation.BOOLEAN
    ImmediateData: win32more.Windows.Win32.Foundation.BOOLEAN
    Type: Byte
    DataSequenceInOrder: win32more.Windows.Win32.Foundation.BOOLEAN
    DataPduInOrder: win32more.Windows.Win32.Foundation.BOOLEAN
    ErrorRecoveryLevel: Byte
    MaxOutstandingR2t: UInt32
    FirstBurstLength: UInt32
    MaxBurstLength: UInt32
    MaximumConnections: UInt32
    ConnectionCount: UInt32
    Connections: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_CONNECTION_INFO_EX)
class ISCSI_TARGET_MAPPINGA(Structure):
    InitiatorName: win32more.Windows.Win32.Foundation.CHAR * 256
    TargetName: win32more.Windows.Win32.Foundation.CHAR * 224
    OSDeviceName: win32more.Windows.Win32.Foundation.CHAR * 260
    SessionId: win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID
    OSBusNumber: UInt32
    OSTargetNumber: UInt32
    LUNCount: UInt32
    LUNList: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.SCSI_LUN_LIST)
class ISCSI_TARGET_MAPPINGW(Structure):
    InitiatorName: Char * 256
    TargetName: Char * 224
    OSDeviceName: Char * 260
    SessionId: win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_UNIQUE_SESSION_ID
    OSBusNumber: UInt32
    OSTargetNumber: UInt32
    LUNCount: UInt32
    LUNList: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.SCSI_LUN_LIST)
ISCSI_TARGET_MAPPING = UnicodeAlias('ISCSI_TARGET_MAPPINGW')
class ISCSI_TARGET_PORTALA(Structure):
    SymbolicName: win32more.Windows.Win32.Foundation.CHAR * 256
    Address: win32more.Windows.Win32.Foundation.CHAR * 256
    Socket: UInt16
class ISCSI_TARGET_PORTALW(Structure):
    SymbolicName: Char * 256
    Address: Char * 256
    Socket: UInt16
ISCSI_TARGET_PORTAL = UnicodeAlias('ISCSI_TARGET_PORTALW')
class ISCSI_TARGET_PORTAL_GROUPA(Structure):
    Count: UInt32
    Portals: win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_TARGET_PORTALA * 1
class ISCSI_TARGET_PORTAL_GROUPW(Structure):
    Count: UInt32
    Portals: win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_TARGET_PORTALW * 1
ISCSI_TARGET_PORTAL_GROUP = UnicodeAlias('ISCSI_TARGET_PORTAL_GROUPW')
class ISCSI_TARGET_PORTAL_INFOA(Structure):
    InitiatorName: win32more.Windows.Win32.Foundation.CHAR * 256
    InitiatorPortNumber: UInt32
    SymbolicName: win32more.Windows.Win32.Foundation.CHAR * 256
    Address: win32more.Windows.Win32.Foundation.CHAR * 256
    Socket: UInt16
class ISCSI_TARGET_PORTAL_INFOW(Structure):
    InitiatorName: Char * 256
    InitiatorPortNumber: UInt32
    SymbolicName: Char * 256
    Address: Char * 256
    Socket: UInt16
ISCSI_TARGET_PORTAL_INFO = UnicodeAlias('ISCSI_TARGET_PORTAL_INFOW')
class ISCSI_TARGET_PORTAL_INFO_EXA(Structure):
    InitiatorName: win32more.Windows.Win32.Foundation.CHAR * 256
    InitiatorPortNumber: UInt32
    SymbolicName: win32more.Windows.Win32.Foundation.CHAR * 256
    Address: win32more.Windows.Win32.Foundation.CHAR * 256
    Socket: UInt16
    SecurityFlags: UInt64
    LoginOptions: win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_LOGIN_OPTIONS
class ISCSI_TARGET_PORTAL_INFO_EXW(Structure):
    InitiatorName: Char * 256
    InitiatorPortNumber: UInt32
    SymbolicName: Char * 256
    Address: Char * 256
    Socket: UInt16
    SecurityFlags: UInt64
    LoginOptions: win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_LOGIN_OPTIONS
ISCSI_TARGET_PORTAL_INFO_EX = UnicodeAlias('ISCSI_TARGET_PORTAL_INFO_EXW')
class ISCSI_UNIQUE_SESSION_ID(Structure):
    AdapterUnique: UInt64
    AdapterSpecific: UInt64
class ISCSI_VERSION_INFO(Structure):
    MajorVersion: UInt32
    MinorVersion: UInt32
    BuildNumber: UInt32
class MPIO_PASS_THROUGH_PATH(Structure):
    PassThrough: win32more.Windows.Win32.Storage.IscsiDisc.SCSI_PASS_THROUGH
    Version: UInt32
    Length: UInt16
    Flags: Byte
    PortNumber: Byte
    MpioPathId: UInt64
if ARCH in 'X64,ARM64':
    class MPIO_PASS_THROUGH_PATH32(Structure):
        PassThrough: win32more.Windows.Win32.Storage.IscsiDisc.SCSI_PASS_THROUGH32
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
    PassThrough: win32more.Windows.Win32.Storage.IscsiDisc.SCSI_PASS_THROUGH_DIRECT
    Version: UInt32
    Length: UInt16
    Flags: Byte
    PortNumber: Byte
    MpioPathId: UInt64
if ARCH in 'X64,ARM64':
    class MPIO_PASS_THROUGH_PATH_DIRECT32(Structure):
        PassThrough: win32more.Windows.Win32.Storage.IscsiDisc.SCSI_PASS_THROUGH_DIRECT32
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
MpStorageDiagnosticLevelDefault: win32more.Windows.Win32.Storage.IscsiDisc.MP_STORAGE_DIAGNOSTIC_LEVEL = 0
MpStorageDiagnosticLevelMax: win32more.Windows.Win32.Storage.IscsiDisc.MP_STORAGE_DIAGNOSTIC_LEVEL = 1
MP_STORAGE_DIAGNOSTIC_TARGET_TYPE = Int32
MpStorageDiagnosticTargetTypeUndefined: win32more.Windows.Win32.Storage.IscsiDisc.MP_STORAGE_DIAGNOSTIC_TARGET_TYPE = 0
MpStorageDiagnosticTargetTypeMiniport: win32more.Windows.Win32.Storage.IscsiDisc.MP_STORAGE_DIAGNOSTIC_TARGET_TYPE = 2
MpStorageDiagnosticTargetTypeHbaFirmware: win32more.Windows.Win32.Storage.IscsiDisc.MP_STORAGE_DIAGNOSTIC_TARGET_TYPE = 3
MpStorageDiagnosticTargetTypeMax: win32more.Windows.Win32.Storage.IscsiDisc.MP_STORAGE_DIAGNOSTIC_TARGET_TYPE = 4
class NTSCSI_UNICODE_STRING(Structure):
    Length: UInt16
    MaximumLength: UInt16
    Buffer: win32more.Windows.Win32.Foundation.PWSTR
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
NvCacheStatusUnknown: win32more.Windows.Win32.Storage.IscsiDisc.NVCACHE_STATUS = 0
NvCacheStatusDisabling: win32more.Windows.Win32.Storage.IscsiDisc.NVCACHE_STATUS = 1
NvCacheStatusDisabled: win32more.Windows.Win32.Storage.IscsiDisc.NVCACHE_STATUS = 2
NvCacheStatusEnabled: win32more.Windows.Win32.Storage.IscsiDisc.NVCACHE_STATUS = 3
NVCACHE_TYPE = Int32
NvCacheTypeUnknown: win32more.Windows.Win32.Storage.IscsiDisc.NVCACHE_TYPE = 0
NvCacheTypeNone: win32more.Windows.Win32.Storage.IscsiDisc.NVCACHE_TYPE = 1
NvCacheTypeWriteBack: win32more.Windows.Win32.Storage.IscsiDisc.NVCACHE_TYPE = 2
NvCacheTypeWriteThrough: win32more.Windows.Win32.Storage.IscsiDisc.NVCACHE_TYPE = 3
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
            WriteCacheEnabled: Annotated[Byte, 1]
            WriteCacheChangeable: Annotated[Byte, 1]
            WriteThroughIOSupported: Annotated[Byte, 1]
            FlushCacheSupported: Annotated[Byte, 1]
            ReservedBits: Annotated[Byte, 4]
NV_SEP_WRITE_CACHE_TYPE = Int32
NVSEPWriteCacheTypeUnknown: win32more.Windows.Win32.Storage.IscsiDisc.NV_SEP_WRITE_CACHE_TYPE = 0
NVSEPWriteCacheTypeNone: win32more.Windows.Win32.Storage.IscsiDisc.NV_SEP_WRITE_CACHE_TYPE = 1
NVSEPWriteCacheTypeWriteBack: win32more.Windows.Win32.Storage.IscsiDisc.NV_SEP_WRITE_CACHE_TYPE = 2
NVSEPWriteCacheTypeWriteThrough: win32more.Windows.Win32.Storage.IscsiDisc.NV_SEP_WRITE_CACHE_TYPE = 3
@winfunctype_pointer
def PDUMP_DEVICE_POWERON_ROUTINE(Context: VoidPtr) -> Int32: ...
class PERSISTENT_ISCSI_LOGIN_INFOA(Structure):
    TargetName: win32more.Windows.Win32.Foundation.CHAR * 224
    IsInformationalSession: win32more.Windows.Win32.Foundation.BOOLEAN
    InitiatorInstance: win32more.Windows.Win32.Foundation.CHAR * 256
    InitiatorPortNumber: UInt32
    TargetPortal: win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_TARGET_PORTALA
    SecurityFlags: UInt64
    Mappings: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_TARGET_MAPPINGA)
    LoginOptions: win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_LOGIN_OPTIONS
class PERSISTENT_ISCSI_LOGIN_INFOW(Structure):
    TargetName: Char * 224
    IsInformationalSession: win32more.Windows.Win32.Foundation.BOOLEAN
    InitiatorInstance: Char * 256
    InitiatorPortNumber: UInt32
    TargetPortal: win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_TARGET_PORTALW
    SecurityFlags: UInt64
    Mappings: POINTER(win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_TARGET_MAPPINGW)
    LoginOptions: win32more.Windows.Win32.Storage.IscsiDisc.ISCSI_LOGIN_OPTIONS
PERSISTENT_ISCSI_LOGIN_INFO = UnicodeAlias('PERSISTENT_ISCSI_LOGIN_INFOW')
class SCSI_ADAPTER_BUS_INFO(Structure):
    NumberOfBuses: Byte
    BusData: win32more.Windows.Win32.Storage.IscsiDisc.SCSI_BUS_DATA * 1
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
    DeviceClaimed: win32more.Windows.Win32.Foundation.BOOLEAN
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
    DataBuffer: VoidPtr
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
        DataBuffer: VoidPtr
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
        DataOutBuffer: VoidPtr
        DataInBuffer: VoidPtr
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
    DataOutBuffer: VoidPtr
    DataInBuffer: VoidPtr
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
    TargetType: win32more.Windows.Win32.Storage.IscsiDisc.MP_STORAGE_DIAGNOSTIC_TARGET_TYPE
    Level: win32more.Windows.Win32.Storage.IscsiDisc.MP_STORAGE_DIAGNOSTIC_LEVEL
    ProviderId: Guid
    BufferSize: UInt32
    Reserved: UInt32
    DataBuffer: Byte * 1
class STORAGE_ENDURANCE_DATA_DESCRIPTOR(Structure):
    Version: UInt32
    Size: UInt32
    EnduranceInfo: win32more.Windows.Win32.Storage.IscsiDisc.STORAGE_ENDURANCE_INFO
class STORAGE_ENDURANCE_INFO(Structure):
    ValidFields: UInt32
    GroupId: UInt32
    Flags: _Flags_e__Struct
    LifePercentage: UInt32
    BytesReadCount: Byte * 16
    ByteWriteCount: Byte * 16
    class _Flags_e__Struct(Structure):
        Shared: Annotated[UInt32, 1]
        Reserved: Annotated[UInt32, 31]
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
    UpgradeSupport: win32more.Windows.Win32.Foundation.BOOLEAN
    SlotCount: Byte
    ActiveSlot: Byte
    PendingActivateSlot: Byte
    Reserved: UInt32
    Slot: win32more.Windows.Win32.Storage.IscsiDisc.STORAGE_FIRMWARE_SLOT_INFO * 1
class STORAGE_FIRMWARE_INFO_V2(Structure):
    Version: UInt32
    Size: UInt32
    UpgradeSupport: win32more.Windows.Win32.Foundation.BOOLEAN
    SlotCount: Byte
    ActiveSlot: Byte
    PendingActivateSlot: Byte
    FirmwareShared: win32more.Windows.Win32.Foundation.BOOLEAN
    Reserved: Byte * 3
    ImagePayloadAlignment: UInt32
    ImagePayloadMaxSize: UInt32
    Slot: win32more.Windows.Win32.Storage.IscsiDisc.STORAGE_FIRMWARE_SLOT_INFO_V2 * 1
class STORAGE_FIRMWARE_SLOT_INFO(Structure):
    SlotNumber: Byte
    ReadOnly: win32more.Windows.Win32.Foundation.BOOLEAN
    Reserved: Byte * 6
    Revision: _Revision_e__Union
    class _Revision_e__Union(Union):
        Info: Byte * 8
        AsUlonglong: UInt64
class STORAGE_FIRMWARE_SLOT_INFO_V2(Structure):
    SlotNumber: Byte
    ReadOnly: win32more.Windows.Win32.Foundation.BOOLEAN
    Reserved: Byte * 6
    Revision: Byte * 16
TARGETPROTOCOLTYPE = Int32
ISCSI_TCP_PROTOCOL_TYPE: win32more.Windows.Win32.Storage.IscsiDisc.TARGETPROTOCOLTYPE = 0
TARGET_INFORMATION_CLASS = Int32
ProtocolType: win32more.Windows.Win32.Storage.IscsiDisc.TARGET_INFORMATION_CLASS = 0
TargetAlias: win32more.Windows.Win32.Storage.IscsiDisc.TARGET_INFORMATION_CLASS = 1
DiscoveryMechanisms: win32more.Windows.Win32.Storage.IscsiDisc.TARGET_INFORMATION_CLASS = 2
PortalGroups: win32more.Windows.Win32.Storage.IscsiDisc.TARGET_INFORMATION_CLASS = 3
PersistentTargetMappings: win32more.Windows.Win32.Storage.IscsiDisc.TARGET_INFORMATION_CLASS = 4
InitiatorName: win32more.Windows.Win32.Storage.IscsiDisc.TARGET_INFORMATION_CLASS = 5
TargetFlags: win32more.Windows.Win32.Storage.IscsiDisc.TARGET_INFORMATION_CLASS = 6
LoginOptions: win32more.Windows.Win32.Storage.IscsiDisc.TARGET_INFORMATION_CLASS = 7
_ADAPTER_OBJECT = IntPtr


make_ready(__name__)
