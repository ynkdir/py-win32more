from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.Security
import Windows.Win32.Storage.FileSystem
import Windows.Win32.System.Com
import Windows.Win32.System.IO
import Windows.Win32.System.WindowsProgramming
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
MAXIMUM_REPARSE_DATA_BUFFER_SIZE: UInt32 = 16384
EA_CONTAINER_NAME: String = 'ContainerName'
EA_CONTAINER_SIZE: String = 'ContainerSize'
CLFS_BASELOG_EXTENSION: String = '.blf'
CLFS_FLAG_REENTRANT_FILE_SYSTEM: UInt32 = 8
CLFS_FLAG_NON_REENTRANT_FILTER: UInt32 = 16
CLFS_FLAG_REENTRANT_FILTER: UInt32 = 32
CLFS_FLAG_IGNORE_SHARE_ACCESS: UInt32 = 64
CLFS_FLAG_READ_IN_PROGRESS: UInt32 = 128
CLFS_FLAG_MINIFILTER_LEVEL: UInt32 = 256
CLFS_FLAG_HIDDEN_SYSTEM_LOG: UInt32 = 512
CLFS_MARSHALLING_FLAG_NONE: UInt32 = 0
CLFS_MARSHALLING_FLAG_DISABLE_BUFF_INIT: UInt32 = 1
CLFS_FLAG_FILTER_INTERMEDIATE_LEVEL: UInt32 = 16
CLFS_FLAG_FILTER_TOP_LEVEL: UInt32 = 32
CLFS_CONTAINER_STREAM_PREFIX: String = '%BLF%:'
CLFS_CONTAINER_RELATIVE_PREFIX: String = '%BLF%\\'
TRANSACTION_MANAGER_VOLATILE: UInt32 = 1
TRANSACTION_MANAGER_COMMIT_DEFAULT: UInt32 = 0
TRANSACTION_MANAGER_COMMIT_SYSTEM_VOLUME: UInt32 = 2
TRANSACTION_MANAGER_COMMIT_SYSTEM_HIVES: UInt32 = 4
TRANSACTION_MANAGER_COMMIT_LOWEST: UInt32 = 8
TRANSACTION_MANAGER_CORRUPT_FOR_RECOVERY: UInt32 = 16
TRANSACTION_MANAGER_CORRUPT_FOR_PROGRESS: UInt32 = 32
TRANSACTION_MANAGER_MAXIMUM_OPTION: UInt32 = 63
TRANSACTION_DO_NOT_PROMOTE: UInt32 = 1
TRANSACTION_MAXIMUM_OPTION: UInt32 = 1
RESOURCE_MANAGER_VOLATILE: UInt32 = 1
RESOURCE_MANAGER_COMMUNICATION: UInt32 = 2
RESOURCE_MANAGER_MAXIMUM_OPTION: UInt32 = 3
CRM_PROTOCOL_EXPLICIT_MARSHAL_ONLY: UInt32 = 1
CRM_PROTOCOL_DYNAMIC_MARSHAL_INFO: UInt32 = 2
CRM_PROTOCOL_MAXIMUM_OPTION: UInt32 = 3
ENLISTMENT_SUPERIOR: UInt32 = 1
ENLISTMENT_MAXIMUM_OPTION: UInt32 = 1
TRANSACTION_NOTIFY_MASK: UInt32 = 1073741823
TRANSACTION_NOTIFY_PREPREPARE: UInt32 = 1
TRANSACTION_NOTIFY_PREPARE: UInt32 = 2
TRANSACTION_NOTIFY_COMMIT: UInt32 = 4
TRANSACTION_NOTIFY_ROLLBACK: UInt32 = 8
TRANSACTION_NOTIFY_PREPREPARE_COMPLETE: UInt32 = 16
TRANSACTION_NOTIFY_PREPARE_COMPLETE: UInt32 = 32
TRANSACTION_NOTIFY_COMMIT_COMPLETE: UInt32 = 64
TRANSACTION_NOTIFY_ROLLBACK_COMPLETE: UInt32 = 128
TRANSACTION_NOTIFY_RECOVER: UInt32 = 256
TRANSACTION_NOTIFY_SINGLE_PHASE_COMMIT: UInt32 = 512
TRANSACTION_NOTIFY_DELEGATE_COMMIT: UInt32 = 1024
TRANSACTION_NOTIFY_RECOVER_QUERY: UInt32 = 2048
TRANSACTION_NOTIFY_ENLIST_PREPREPARE: UInt32 = 4096
TRANSACTION_NOTIFY_LAST_RECOVER: UInt32 = 8192
TRANSACTION_NOTIFY_INDOUBT: UInt32 = 16384
TRANSACTION_NOTIFY_PROPAGATE_PULL: UInt32 = 32768
TRANSACTION_NOTIFY_PROPAGATE_PUSH: UInt32 = 65536
TRANSACTION_NOTIFY_MARSHAL: UInt32 = 131072
TRANSACTION_NOTIFY_ENLIST_MASK: UInt32 = 262144
TRANSACTION_NOTIFY_RM_DISCONNECTED: UInt32 = 16777216
TRANSACTION_NOTIFY_TM_ONLINE: UInt32 = 33554432
TRANSACTION_NOTIFY_COMMIT_REQUEST: UInt32 = 67108864
TRANSACTION_NOTIFY_PROMOTE: UInt32 = 134217728
TRANSACTION_NOTIFY_PROMOTE_NEW: UInt32 = 268435456
TRANSACTION_NOTIFY_REQUEST_OUTCOME: UInt32 = 536870912
TRANSACTION_NOTIFY_COMMIT_FINALIZE: UInt32 = 1073741824
TRANSACTIONMANAGER_OBJECT_PATH: String = '\\TransactionManager\\'
TRANSACTION_OBJECT_PATH: String = '\\Transaction\\'
ENLISTMENT_OBJECT_PATH: String = '\\Enlistment\\'
RESOURCE_MANAGER_OBJECT_PATH: String = '\\ResourceManager\\'
TRANSACTION_NOTIFICATION_TM_ONLINE_FLAG_IS_CLUSTERED: UInt32 = 1
KTM_MARSHAL_BLOB_VERSION_MAJOR: UInt32 = 1
KTM_MARSHAL_BLOB_VERSION_MINOR: UInt32 = 1
MAX_TRANSACTION_DESCRIPTION_LENGTH: UInt32 = 64
MAX_RESOURCEMANAGER_DESCRIPTION_LENGTH: UInt32 = 64
IOCTL_VOLUME_BASE: UInt32 = 86
IOCTL_VOLUME_GET_VOLUME_DISK_EXTENTS: UInt32 = 5636096
IOCTL_VOLUME_ONLINE: UInt32 = 5685256
IOCTL_VOLUME_OFFLINE: UInt32 = 5685260
IOCTL_VOLUME_IS_CLUSTERED: UInt32 = 5636144
IOCTL_VOLUME_GET_GPT_ATTRIBUTES: UInt32 = 5636152
IOCTL_VOLUME_SUPPORTS_ONLINE_OFFLINE: UInt32 = 5636100
IOCTL_VOLUME_IS_OFFLINE: UInt32 = 5636112
IOCTL_VOLUME_IS_IO_CAPABLE: UInt32 = 5636116
IOCTL_VOLUME_QUERY_FAILOVER_SET: UInt32 = 5636120
IOCTL_VOLUME_QUERY_VOLUME_NUMBER: UInt32 = 5636124
IOCTL_VOLUME_LOGICAL_TO_PHYSICAL: UInt32 = 5636128
IOCTL_VOLUME_PHYSICAL_TO_LOGICAL: UInt32 = 5636132
IOCTL_VOLUME_IS_PARTITION: UInt32 = 5636136
IOCTL_VOLUME_READ_PLEX: UInt32 = 5652526
IOCTL_VOLUME_SET_GPT_ATTRIBUTES: UInt32 = 5636148
IOCTL_VOLUME_GET_BC_PROPERTIES: UInt32 = 5652540
IOCTL_VOLUME_ALLOCATE_BC_STREAM: UInt32 = 5685312
IOCTL_VOLUME_FREE_BC_STREAM: UInt32 = 5685316
IOCTL_VOLUME_BC_VERSION: UInt32 = 1
IOCTL_VOLUME_IS_DYNAMIC: UInt32 = 5636168
IOCTL_VOLUME_PREPARE_FOR_CRITICAL_IO: UInt32 = 5685324
IOCTL_VOLUME_QUERY_ALLOCATION_HINT: UInt32 = 5652562
IOCTL_VOLUME_UPDATE_PROPERTIES: UInt32 = 5636180
IOCTL_VOLUME_QUERY_MINIMUM_SHRINK_SIZE: UInt32 = 5652568
IOCTL_VOLUME_PREPARE_FOR_SHRINK: UInt32 = 5685340
IOCTL_VOLUME_IS_CSV: UInt32 = 5636192
IOCTL_VOLUME_POST_ONLINE: UInt32 = 5685348
IOCTL_VOLUME_GET_CSVBLOCKCACHE_CALLBACK: UInt32 = 5685352
CSV_BLOCK_CACHE_CALLBACK_VERSION: UInt32 = 1
CSV_BLOCK_AND_FILE_CACHE_CALLBACK_VERSION: UInt32 = 2
PARTITION_BASIC_DATA_GUID: Guid = Guid('ebd0a0a2-b9e5-4433-87-c0-68-b6-b7-26-99-c7')
PARTITION_BSP_GUID: Guid = Guid('57434f53-4df9-45b9-8e-9e-23-70-f0-06-45-7c')
PARTITION_CLUSTER_GUID: Guid = Guid('db97dba9-0840-4bae-97-f0-ff-b9-a3-27-c7-e1')
PARTITION_DPP_GUID: Guid = Guid('57434f53-94cb-43f0-a5-33-d7-3c-10-cf-a5-7d')
PARTITION_ENTRY_UNUSED_GUID: Guid = Guid('00000000-0000-0000-00-00-00-00-00-00-00-00')
PARTITION_LDM_DATA_GUID: Guid = Guid('af9b60a0-1431-4f62-bc-68-33-11-71-4a-69-ad')
PARTITION_LDM_METADATA_GUID: Guid = Guid('5808c8aa-7e8f-42e0-85-d2-e1-e9-04-34-cf-b3')
PARTITION_LEGACY_BL_GUID: Guid = Guid('424ca0e2-7cb2-4fb9-81-43-c5-2a-99-39-8b-c6')
PARTITION_LEGACY_BL_GUID_BACKUP: Guid = Guid('424c3e6c-d79f-49cb-93-5d-36-d7-14-67-a2-88')
PARTITION_MAIN_OS_GUID: Guid = Guid('57434f53-8f45-405e-8a-23-18-6d-8a-43-30-d3')
PARTITION_MSFT_RECOVERY_GUID: Guid = Guid('de94bba4-06d1-4d40-a1-6a-bf-d5-01-79-d6-ac')
PARTITION_MSFT_RESERVED_GUID: Guid = Guid('e3c9e316-0b5c-4db8-81-7d-f9-2d-f0-02-15-ae')
PARTITION_MSFT_SNAPSHOT_GUID: Guid = Guid('caddebf1-4400-4de8-b1-03-12-11-7d-cf-3c-cf')
PARTITION_OS_DATA_GUID: Guid = Guid('57434f53-23f2-44d5-a8-30-67-bb-da-a6-09-f9')
PARTITION_PATCH_GUID: Guid = Guid('8967a686-96aa-6aa8-95-89-a8-42-56-54-10-90')
PARTITION_PRE_INSTALLED_GUID: Guid = Guid('57434f53-7fe0-4196-9b-42-42-7b-51-64-34-84')
PARTITION_SERVICING_FILES_GUID: Guid = Guid('57434f53-432e-4014-ae-4c-8d-ea-a9-c0-00-6a')
PARTITION_SERVICING_METADATA_GUID: Guid = Guid('57434f53-c691-4a05-bb-4e-70-3d-af-d2-29-ce')
PARTITION_SERVICING_RESERVE_GUID: Guid = Guid('57434f53-4b81-460b-a3-19-ff-b6-fe-13-6d-14')
PARTITION_SERVICING_STAGING_ROOT_GUID: Guid = Guid('57434f53-e84d-4e84-aa-f3-ec-bb-bd-04-b9-df')
PARTITION_SPACES_GUID: Guid = Guid('e75caf8f-f680-4cee-af-a3-b0-01-e5-6e-fc-2d')
PARTITION_SPACES_DATA_GUID: Guid = Guid('e7addcb4-dc34-4539-9a-76-eb-bd-07-be-6f-7e')
PARTITION_SYSTEM_GUID: Guid = Guid('c12a7328-f81f-11d2-ba-4b-00-a0-c9-3e-c9-3b')
PARTITION_WINDOWS_SYSTEM_GUID: Guid = Guid('57434f53-e3e3-4631-a5-c5-26-d2-24-38-73-aa')
_FT_TYPES_DEFINITION_: UInt32 = 1
CLFS_MGMT_POLICY_VERSION: UInt32 = 1
LOG_POLICY_OVERWRITE: UInt32 = 1
LOG_POLICY_PERSIST: UInt32 = 2
CLFS_MGMT_CLIENT_REGISTRATION_VERSION: UInt32 = 1
CLSID_DiskQuotaControl: Guid = Guid('7988b571-ec89-11cf-9c-00-00-aa-00-a1-4f-56')
DISKQUOTA_STATE_DISABLED: UInt32 = 0
DISKQUOTA_STATE_TRACK: UInt32 = 1
DISKQUOTA_STATE_ENFORCE: UInt32 = 2
DISKQUOTA_STATE_MASK: UInt32 = 3
DISKQUOTA_FILESTATE_INCOMPLETE: UInt32 = 256
DISKQUOTA_FILESTATE_REBUILDING: UInt32 = 512
DISKQUOTA_FILESTATE_MASK: UInt32 = 768
DISKQUOTA_LOGFLAG_USER_THRESHOLD: UInt32 = 1
DISKQUOTA_LOGFLAG_USER_LIMIT: UInt32 = 2
DISKQUOTA_USER_ACCOUNT_RESOLVED: UInt32 = 0
DISKQUOTA_USER_ACCOUNT_UNAVAILABLE: UInt32 = 1
DISKQUOTA_USER_ACCOUNT_DELETED: UInt32 = 2
DISKQUOTA_USER_ACCOUNT_INVALID: UInt32 = 3
DISKQUOTA_USER_ACCOUNT_UNKNOWN: UInt32 = 4
DISKQUOTA_USER_ACCOUNT_UNRESOLVED: UInt32 = 5
INVALID_FILE_SIZE: UInt32 = 4294967295
INVALID_SET_FILE_POINTER: UInt32 = 4294967295
INVALID_FILE_ATTRIBUTES: UInt32 = 4294967295
SHARE_NETNAME_PARMNUM: UInt32 = 1
SHARE_TYPE_PARMNUM: UInt32 = 3
SHARE_REMARK_PARMNUM: UInt32 = 4
SHARE_PERMISSIONS_PARMNUM: UInt32 = 5
SHARE_MAX_USES_PARMNUM: UInt32 = 6
SHARE_CURRENT_USES_PARMNUM: UInt32 = 7
SHARE_PATH_PARMNUM: UInt32 = 8
SHARE_PASSWD_PARMNUM: UInt32 = 9
SHARE_FILE_SD_PARMNUM: UInt32 = 501
SHARE_SERVER_PARMNUM: UInt32 = 503
SHI1_NUM_ELEMENTS: UInt32 = 4
SHI2_NUM_ELEMENTS: UInt32 = 10
STYPE_RESERVED1: UInt32 = 16777216
STYPE_RESERVED2: UInt32 = 33554432
STYPE_RESERVED3: UInt32 = 67108864
STYPE_RESERVED4: UInt32 = 134217728
STYPE_RESERVED5: UInt32 = 1048576
STYPE_RESERVED_ALL: UInt32 = 1073741568
SHI_USES_UNLIMITED: UInt32 = 4294967295
SHI1005_FLAGS_DFS: UInt32 = 1
SHI1005_FLAGS_DFS_ROOT: UInt32 = 2
CSC_MASK_EXT: UInt32 = 8240
CSC_MASK: UInt32 = 48
CSC_CACHE_MANUAL_REINT: UInt32 = 0
CSC_CACHE_AUTO_REINT: UInt32 = 16
CSC_CACHE_VDO: UInt32 = 32
CSC_CACHE_NONE: UInt32 = 48
SHI1005_FLAGS_RESTRICT_EXCLUSIVE_OPENS: UInt32 = 256
SHI1005_FLAGS_FORCE_SHARED_DELETE: UInt32 = 512
SHI1005_FLAGS_ALLOW_NAMESPACE_CACHING: UInt32 = 1024
SHI1005_FLAGS_ACCESS_BASED_DIRECTORY_ENUM: UInt32 = 2048
SHI1005_FLAGS_FORCE_LEVELII_OPLOCK: UInt32 = 4096
SHI1005_FLAGS_ENABLE_HASH: UInt32 = 8192
SHI1005_FLAGS_ENABLE_CA: UInt32 = 16384
SHI1005_FLAGS_ENCRYPT_DATA: UInt32 = 32768
SHI1005_FLAGS_RESERVED: UInt32 = 65536
SHI1005_FLAGS_DISABLE_CLIENT_BUFFERING: UInt32 = 131072
SHI1005_FLAGS_IDENTITY_REMOTING: UInt32 = 262144
SHI1005_FLAGS_CLUSTER_MANAGED: UInt32 = 524288
SHI1005_FLAGS_COMPRESS_DATA: UInt32 = 1048576
SESI1_NUM_ELEMENTS: UInt32 = 8
SESI2_NUM_ELEMENTS: UInt32 = 9
STATSOPT_CLR: UInt32 = 1
LZERROR_BADINHANDLE: Int32 = -1
LZERROR_BADOUTHANDLE: Int32 = -2
LZERROR_READ: Int32 = -3
LZERROR_WRITE: Int32 = -4
LZERROR_GLOBALLOC: Int32 = -5
LZERROR_GLOBLOCK: Int32 = -6
LZERROR_BADVALUE: Int32 = -7
LZERROR_UNKNOWNALG: Int32 = -8
NTMS_OBJECTNAME_LENGTH: UInt32 = 64
NTMS_DESCRIPTION_LENGTH: UInt32 = 127
NTMS_DEVICENAME_LENGTH: UInt32 = 64
NTMS_SERIALNUMBER_LENGTH: UInt32 = 32
NTMS_REVISION_LENGTH: UInt32 = 32
NTMS_BARCODE_LENGTH: UInt32 = 64
NTMS_SEQUENCE_LENGTH: UInt32 = 32
NTMS_VENDORNAME_LENGTH: UInt32 = 128
NTMS_PRODUCTNAME_LENGTH: UInt32 = 128
NTMS_USERNAME_LENGTH: UInt32 = 64
NTMS_APPLICATIONNAME_LENGTH: UInt32 = 64
NTMS_COMPUTERNAME_LENGTH: UInt32 = 64
NTMS_I1_MESSAGE_LENGTH: UInt32 = 127
NTMS_MESSAGE_LENGTH: UInt32 = 256
NTMS_POOLHIERARCHY_LENGTH: UInt32 = 512
NTMS_OMIDLABELID_LENGTH: UInt32 = 255
NTMS_OMIDLABELTYPE_LENGTH: UInt32 = 64
NTMS_OMIDLABELINFO_LENGTH: UInt32 = 256
NTMS_MAXATTR_LENGTH: UInt32 = 65536
NTMS_MAXATTR_NAMELEN: UInt32 = 32
NTMSMLI_MAXTYPE: UInt32 = 64
NTMSMLI_MAXIDSIZE: UInt32 = 256
NTMSMLI_MAXAPPDESCR: UInt32 = 256
TXF_LOG_RECORD_GENERIC_TYPE_COMMIT: UInt32 = 1
TXF_LOG_RECORD_GENERIC_TYPE_ABORT: UInt32 = 2
TXF_LOG_RECORD_GENERIC_TYPE_PREPARE: UInt32 = 4
TXF_LOG_RECORD_GENERIC_TYPE_DATA: UInt32 = 8
VS_VERSION_INFO: UInt32 = 1
VS_USER_DEFINED: UInt32 = 100
VS_FFI_SIGNATURE: Int32 = -17890115
VS_FFI_STRUCVERSION: Int32 = 65536
VS_FFI_FILEFLAGSMASK: Int32 = 63
WINEFS_SETUSERKEY_SET_CAPABILITIES: UInt32 = 1
EFS_COMPATIBILITY_VERSION_NCRYPT_PROTECTOR: UInt32 = 5
EFS_COMPATIBILITY_VERSION_PFILE_PROTECTOR: UInt32 = 6
EFS_SUBVER_UNKNOWN: UInt32 = 0
EFS_EFS_SUBVER_EFS_CERT: UInt32 = 1
EFS_PFILE_SUBVER_RMS: UInt32 = 2
EFS_PFILE_SUBVER_APPX: UInt32 = 3
MAX_SID_SIZE: UInt32 = 256
EFS_METADATA_ADD_USER: UInt32 = 1
EFS_METADATA_REMOVE_USER: UInt32 = 2
EFS_METADATA_REPLACE_USER: UInt32 = 4
EFS_METADATA_GENERAL_OP: UInt32 = 8
WOF_PROVIDER_WIM: UInt32 = 1
WOF_PROVIDER_FILE: UInt32 = 2
WIM_PROVIDER_HASH_SIZE: UInt32 = 20
WIM_BOOT_OS_WIM: UInt32 = 1
WIM_BOOT_NOT_OS_WIM: UInt32 = 0
WIM_ENTRY_FLAG_NOT_ACTIVE: UInt32 = 1
WIM_ENTRY_FLAG_SUSPENDED: UInt32 = 2
WIM_EXTERNAL_FILE_INFO_FLAG_NOT_ACTIVE: UInt32 = 1
WIM_EXTERNAL_FILE_INFO_FLAG_SUSPENDED: UInt32 = 2
FILE_PROVIDER_COMPRESSION_XPRESS4K: UInt32 = 0
FILE_PROVIDER_COMPRESSION_LZX: UInt32 = 1
FILE_PROVIDER_COMPRESSION_XPRESS8K: UInt32 = 2
FILE_PROVIDER_COMPRESSION_XPRESS16K: UInt32 = 3
ClfsNullRecord: Byte = 0
ClfsDataRecord: Byte = 1
ClfsRestartRecord: Byte = 2
ClfsClientRecord: Byte = 3
ClsContainerInitializing: UInt32 = 1
ClsContainerInactive: UInt32 = 2
ClsContainerActive: UInt32 = 4
ClsContainerActivePendingDelete: UInt32 = 8
ClsContainerPendingArchive: UInt32 = 16
ClsContainerPendingArchiveAndDelete: UInt32 = 32
ClfsContainerInitializing: UInt32 = 1
ClfsContainerInactive: UInt32 = 2
ClfsContainerActive: UInt32 = 4
ClfsContainerActivePendingDelete: UInt32 = 8
ClfsContainerPendingArchive: UInt32 = 16
ClfsContainerPendingArchiveAndDelete: UInt32 = 32
CLFS_MAX_CONTAINER_INFO: UInt32 = 256
CLFS_SCAN_INIT: Byte = 1
CLFS_SCAN_FORWARD: Byte = 2
CLFS_SCAN_BACKWARD: Byte = 4
CLFS_SCAN_CLOSE: Byte = 8
CLFS_SCAN_INITIALIZED: Byte = 16
CLFS_SCAN_BUFFERED: Byte = 32
@winfunctype('KERNEL32.dll')
def SearchPathW(lpPath: Windows.Win32.Foundation.PWSTR, lpFileName: Windows.Win32.Foundation.PWSTR, lpExtension: Windows.Win32.Foundation.PWSTR, nBufferLength: UInt32, lpBuffer: Windows.Win32.Foundation.PWSTR, lpFilePart: POINTER(Windows.Win32.Foundation.PWSTR)) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def SearchPathA(lpPath: Windows.Win32.Foundation.PSTR, lpFileName: Windows.Win32.Foundation.PSTR, lpExtension: Windows.Win32.Foundation.PSTR, nBufferLength: UInt32, lpBuffer: Windows.Win32.Foundation.PSTR, lpFilePart: POINTER(Windows.Win32.Foundation.PSTR)) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def CompareFileTime(lpFileTime1: POINTER(Windows.Win32.Foundation.FILETIME_head), lpFileTime2: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Int32: ...
@winfunctype('KERNEL32.dll')
def CreateDirectoryA(lpPathName: Windows.Win32.Foundation.PSTR, lpSecurityAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateDirectoryW(lpPathName: Windows.Win32.Foundation.PWSTR, lpSecurityAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateFileA(lpFileName: Windows.Win32.Foundation.PSTR, dwDesiredAccess: Windows.Win32.Storage.FileSystem.FILE_ACCESS_FLAGS, dwShareMode: Windows.Win32.Storage.FileSystem.FILE_SHARE_MODE, lpSecurityAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head), dwCreationDisposition: Windows.Win32.Storage.FileSystem.FILE_CREATION_DISPOSITION, dwFlagsAndAttributes: Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES, hTemplateFile: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def CreateFileW(lpFileName: Windows.Win32.Foundation.PWSTR, dwDesiredAccess: Windows.Win32.Storage.FileSystem.FILE_ACCESS_FLAGS, dwShareMode: Windows.Win32.Storage.FileSystem.FILE_SHARE_MODE, lpSecurityAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head), dwCreationDisposition: Windows.Win32.Storage.FileSystem.FILE_CREATION_DISPOSITION, dwFlagsAndAttributes: Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES, hTemplateFile: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def DefineDosDeviceW(dwFlags: Windows.Win32.Storage.FileSystem.DEFINE_DOS_DEVICE_FLAGS, lpDeviceName: Windows.Win32.Foundation.PWSTR, lpTargetPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DeleteFileA(lpFileName: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DeleteFileW(lpFileName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DeleteVolumeMountPointW(lpszVolumeMountPoint: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FileTimeToLocalFileTime(lpFileTime: POINTER(Windows.Win32.Foundation.FILETIME_head), lpLocalFileTime: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FindClose(hFindFile: Windows.Win32.Storage.FileSystem.FindFileHandle) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FindCloseChangeNotification(hChangeHandle: Windows.Win32.Storage.FileSystem.FindChangeNotificationHandle) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FindFirstChangeNotificationA(lpPathName: Windows.Win32.Foundation.PSTR, bWatchSubtree: Windows.Win32.Foundation.BOOL, dwNotifyFilter: Windows.Win32.Storage.FileSystem.FILE_NOTIFY_CHANGE) -> Windows.Win32.Storage.FileSystem.FindChangeNotificationHandle: ...
@winfunctype('KERNEL32.dll')
def FindFirstChangeNotificationW(lpPathName: Windows.Win32.Foundation.PWSTR, bWatchSubtree: Windows.Win32.Foundation.BOOL, dwNotifyFilter: Windows.Win32.Storage.FileSystem.FILE_NOTIFY_CHANGE) -> Windows.Win32.Storage.FileSystem.FindChangeNotificationHandle: ...
@winfunctype('KERNEL32.dll')
def FindFirstFileA(lpFileName: Windows.Win32.Foundation.PSTR, lpFindFileData: POINTER(Windows.Win32.Storage.FileSystem.WIN32_FIND_DATAA_head)) -> Windows.Win32.Storage.FileSystem.FindFileHandle: ...
@winfunctype('KERNEL32.dll')
def FindFirstFileW(lpFileName: Windows.Win32.Foundation.PWSTR, lpFindFileData: POINTER(Windows.Win32.Storage.FileSystem.WIN32_FIND_DATAW_head)) -> Windows.Win32.Storage.FileSystem.FindFileHandle: ...
@winfunctype('KERNEL32.dll')
def FindFirstFileExA(lpFileName: Windows.Win32.Foundation.PSTR, fInfoLevelId: Windows.Win32.Storage.FileSystem.FINDEX_INFO_LEVELS, lpFindFileData: c_void_p, fSearchOp: Windows.Win32.Storage.FileSystem.FINDEX_SEARCH_OPS, lpSearchFilter: c_void_p, dwAdditionalFlags: Windows.Win32.Storage.FileSystem.FIND_FIRST_EX_FLAGS) -> Windows.Win32.Storage.FileSystem.FindFileHandle: ...
@winfunctype('KERNEL32.dll')
def FindFirstFileExW(lpFileName: Windows.Win32.Foundation.PWSTR, fInfoLevelId: Windows.Win32.Storage.FileSystem.FINDEX_INFO_LEVELS, lpFindFileData: c_void_p, fSearchOp: Windows.Win32.Storage.FileSystem.FINDEX_SEARCH_OPS, lpSearchFilter: c_void_p, dwAdditionalFlags: Windows.Win32.Storage.FileSystem.FIND_FIRST_EX_FLAGS) -> Windows.Win32.Storage.FileSystem.FindFileHandle: ...
@winfunctype('KERNEL32.dll')
def FindFirstVolumeW(lpszVolumeName: Windows.Win32.Foundation.PWSTR, cchBufferLength: UInt32) -> Windows.Win32.Storage.FileSystem.FindVolumeHandle: ...
@winfunctype('KERNEL32.dll')
def FindNextChangeNotification(hChangeHandle: Windows.Win32.Storage.FileSystem.FindChangeNotificationHandle) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FindNextFileA(hFindFile: Windows.Win32.Storage.FileSystem.FindFileHandle, lpFindFileData: POINTER(Windows.Win32.Storage.FileSystem.WIN32_FIND_DATAA_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FindNextFileW(hFindFile: Windows.Win32.Storage.FileSystem.FindFileHandle, lpFindFileData: POINTER(Windows.Win32.Storage.FileSystem.WIN32_FIND_DATAW_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FindNextVolumeW(hFindVolume: Windows.Win32.Storage.FileSystem.FindVolumeHandle, lpszVolumeName: Windows.Win32.Foundation.PWSTR, cchBufferLength: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FindVolumeClose(hFindVolume: Windows.Win32.Storage.FileSystem.FindVolumeHandle) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FlushFileBuffers(hFile: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetDiskFreeSpaceA(lpRootPathName: Windows.Win32.Foundation.PSTR, lpSectorsPerCluster: POINTER(UInt32), lpBytesPerSector: POINTER(UInt32), lpNumberOfFreeClusters: POINTER(UInt32), lpTotalNumberOfClusters: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetDiskFreeSpaceW(lpRootPathName: Windows.Win32.Foundation.PWSTR, lpSectorsPerCluster: POINTER(UInt32), lpBytesPerSector: POINTER(UInt32), lpNumberOfFreeClusters: POINTER(UInt32), lpTotalNumberOfClusters: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetDiskFreeSpaceExA(lpDirectoryName: Windows.Win32.Foundation.PSTR, lpFreeBytesAvailableToCaller: POINTER(Windows.Win32.Foundation.ULARGE_INTEGER_head), lpTotalNumberOfBytes: POINTER(Windows.Win32.Foundation.ULARGE_INTEGER_head), lpTotalNumberOfFreeBytes: POINTER(Windows.Win32.Foundation.ULARGE_INTEGER_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetDiskFreeSpaceExW(lpDirectoryName: Windows.Win32.Foundation.PWSTR, lpFreeBytesAvailableToCaller: POINTER(Windows.Win32.Foundation.ULARGE_INTEGER_head), lpTotalNumberOfBytes: POINTER(Windows.Win32.Foundation.ULARGE_INTEGER_head), lpTotalNumberOfFreeBytes: POINTER(Windows.Win32.Foundation.ULARGE_INTEGER_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetDiskSpaceInformationA(rootPath: Windows.Win32.Foundation.PSTR, diskSpaceInfo: POINTER(Windows.Win32.Storage.FileSystem.DISK_SPACE_INFORMATION_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def GetDiskSpaceInformationW(rootPath: Windows.Win32.Foundation.PWSTR, diskSpaceInfo: POINTER(Windows.Win32.Storage.FileSystem.DISK_SPACE_INFORMATION_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def GetDriveTypeA(lpRootPathName: Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetDriveTypeW(lpRootPathName: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetFileAttributesA(lpFileName: Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetFileAttributesW(lpFileName: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetFileAttributesExA(lpFileName: Windows.Win32.Foundation.PSTR, fInfoLevelId: Windows.Win32.Storage.FileSystem.GET_FILEEX_INFO_LEVELS, lpFileInformation: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetFileAttributesExW(lpFileName: Windows.Win32.Foundation.PWSTR, fInfoLevelId: Windows.Win32.Storage.FileSystem.GET_FILEEX_INFO_LEVELS, lpFileInformation: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetFileInformationByHandle(hFile: Windows.Win32.Foundation.HANDLE, lpFileInformation: POINTER(Windows.Win32.Storage.FileSystem.BY_HANDLE_FILE_INFORMATION_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetFileSize(hFile: Windows.Win32.Foundation.HANDLE, lpFileSizeHigh: POINTER(UInt32)) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetFileSizeEx(hFile: Windows.Win32.Foundation.HANDLE, lpFileSize: POINTER(Windows.Win32.Foundation.LARGE_INTEGER_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetFileType(hFile: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Storage.FileSystem.FILE_TYPE: ...
@winfunctype('KERNEL32.dll')
def GetFinalPathNameByHandleA(hFile: Windows.Win32.Foundation.HANDLE, lpszFilePath: Windows.Win32.Foundation.PSTR, cchFilePath: UInt32, dwFlags: Windows.Win32.Storage.FileSystem.FILE_NAME) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetFinalPathNameByHandleW(hFile: Windows.Win32.Foundation.HANDLE, lpszFilePath: Windows.Win32.Foundation.PWSTR, cchFilePath: UInt32, dwFlags: Windows.Win32.Storage.FileSystem.FILE_NAME) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetFileTime(hFile: Windows.Win32.Foundation.HANDLE, lpCreationTime: POINTER(Windows.Win32.Foundation.FILETIME_head), lpLastAccessTime: POINTER(Windows.Win32.Foundation.FILETIME_head), lpLastWriteTime: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetFullPathNameW(lpFileName: Windows.Win32.Foundation.PWSTR, nBufferLength: UInt32, lpBuffer: Windows.Win32.Foundation.PWSTR, lpFilePart: POINTER(Windows.Win32.Foundation.PWSTR)) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetFullPathNameA(lpFileName: Windows.Win32.Foundation.PSTR, nBufferLength: UInt32, lpBuffer: Windows.Win32.Foundation.PSTR, lpFilePart: POINTER(Windows.Win32.Foundation.PSTR)) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetLogicalDrives() -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetLogicalDriveStringsW(nBufferLength: UInt32, lpBuffer: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetLongPathNameA(lpszShortPath: Windows.Win32.Foundation.PSTR, lpszLongPath: Windows.Win32.Foundation.PSTR, cchBuffer: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetLongPathNameW(lpszShortPath: Windows.Win32.Foundation.PWSTR, lpszLongPath: Windows.Win32.Foundation.PWSTR, cchBuffer: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def AreShortNamesEnabled(Handle: Windows.Win32.Foundation.HANDLE, Enabled: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetShortPathNameW(lpszLongPath: Windows.Win32.Foundation.PWSTR, lpszShortPath: Windows.Win32.Foundation.PWSTR, cchBuffer: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetTempFileNameW(lpPathName: Windows.Win32.Foundation.PWSTR, lpPrefixString: Windows.Win32.Foundation.PWSTR, uUnique: UInt32, lpTempFileName: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetVolumeInformationByHandleW(hFile: Windows.Win32.Foundation.HANDLE, lpVolumeNameBuffer: Windows.Win32.Foundation.PWSTR, nVolumeNameSize: UInt32, lpVolumeSerialNumber: POINTER(UInt32), lpMaximumComponentLength: POINTER(UInt32), lpFileSystemFlags: POINTER(UInt32), lpFileSystemNameBuffer: Windows.Win32.Foundation.PWSTR, nFileSystemNameSize: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetVolumeInformationW(lpRootPathName: Windows.Win32.Foundation.PWSTR, lpVolumeNameBuffer: Windows.Win32.Foundation.PWSTR, nVolumeNameSize: UInt32, lpVolumeSerialNumber: POINTER(UInt32), lpMaximumComponentLength: POINTER(UInt32), lpFileSystemFlags: POINTER(UInt32), lpFileSystemNameBuffer: Windows.Win32.Foundation.PWSTR, nFileSystemNameSize: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetVolumePathNameW(lpszFileName: Windows.Win32.Foundation.PWSTR, lpszVolumePathName: Windows.Win32.Foundation.PWSTR, cchBufferLength: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def LocalFileTimeToFileTime(lpLocalFileTime: POINTER(Windows.Win32.Foundation.FILETIME_head), lpFileTime: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def LockFile(hFile: Windows.Win32.Foundation.HANDLE, dwFileOffsetLow: UInt32, dwFileOffsetHigh: UInt32, nNumberOfBytesToLockLow: UInt32, nNumberOfBytesToLockHigh: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def LockFileEx(hFile: Windows.Win32.Foundation.HANDLE, dwFlags: Windows.Win32.Storage.FileSystem.LOCK_FILE_FLAGS, dwReserved: UInt32, nNumberOfBytesToLockLow: UInt32, nNumberOfBytesToLockHigh: UInt32, lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def QueryDosDeviceW(lpDeviceName: Windows.Win32.Foundation.PWSTR, lpTargetPath: Windows.Win32.Foundation.PWSTR, ucchMax: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def ReadFile(hFile: Windows.Win32.Foundation.HANDLE, lpBuffer: c_void_p, nNumberOfBytesToRead: UInt32, lpNumberOfBytesRead: POINTER(UInt32), lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ReadFileEx(hFile: Windows.Win32.Foundation.HANDLE, lpBuffer: c_void_p, nNumberOfBytesToRead: UInt32, lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head), lpCompletionRoutine: Windows.Win32.System.IO.LPOVERLAPPED_COMPLETION_ROUTINE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ReadFileScatter(hFile: Windows.Win32.Foundation.HANDLE, aSegmentArray: POINTER(Windows.Win32.Storage.FileSystem.FILE_SEGMENT_ELEMENT_head), nNumberOfBytesToRead: UInt32, lpReserved: POINTER(UInt32), lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def RemoveDirectoryA(lpPathName: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def RemoveDirectoryW(lpPathName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetEndOfFile(hFile: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetFileAttributesA(lpFileName: Windows.Win32.Foundation.PSTR, dwFileAttributes: Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetFileAttributesW(lpFileName: Windows.Win32.Foundation.PWSTR, dwFileAttributes: Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetFileInformationByHandle(hFile: Windows.Win32.Foundation.HANDLE, FileInformationClass: Windows.Win32.Storage.FileSystem.FILE_INFO_BY_HANDLE_CLASS, lpFileInformation: c_void_p, dwBufferSize: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetFilePointer(hFile: Windows.Win32.Foundation.HANDLE, lDistanceToMove: Int32, lpDistanceToMoveHigh: POINTER(Int32), dwMoveMethod: Windows.Win32.Storage.FileSystem.SET_FILE_POINTER_MOVE_METHOD) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def SetFilePointerEx(hFile: Windows.Win32.Foundation.HANDLE, liDistanceToMove: Windows.Win32.Foundation.LARGE_INTEGER, lpNewFilePointer: POINTER(Windows.Win32.Foundation.LARGE_INTEGER_head), dwMoveMethod: Windows.Win32.Storage.FileSystem.SET_FILE_POINTER_MOVE_METHOD) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetFileTime(hFile: Windows.Win32.Foundation.HANDLE, lpCreationTime: POINTER(Windows.Win32.Foundation.FILETIME_head), lpLastAccessTime: POINTER(Windows.Win32.Foundation.FILETIME_head), lpLastWriteTime: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetFileValidData(hFile: Windows.Win32.Foundation.HANDLE, ValidDataLength: Int64) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def UnlockFile(hFile: Windows.Win32.Foundation.HANDLE, dwFileOffsetLow: UInt32, dwFileOffsetHigh: UInt32, nNumberOfBytesToUnlockLow: UInt32, nNumberOfBytesToUnlockHigh: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def UnlockFileEx(hFile: Windows.Win32.Foundation.HANDLE, dwReserved: UInt32, nNumberOfBytesToUnlockLow: UInt32, nNumberOfBytesToUnlockHigh: UInt32, lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WriteFile(hFile: Windows.Win32.Foundation.HANDLE, lpBuffer: c_char_p_no, nNumberOfBytesToWrite: UInt32, lpNumberOfBytesWritten: POINTER(UInt32), lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WriteFileEx(hFile: Windows.Win32.Foundation.HANDLE, lpBuffer: c_char_p_no, nNumberOfBytesToWrite: UInt32, lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head), lpCompletionRoutine: Windows.Win32.System.IO.LPOVERLAPPED_COMPLETION_ROUTINE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WriteFileGather(hFile: Windows.Win32.Foundation.HANDLE, aSegmentArray: POINTER(Windows.Win32.Storage.FileSystem.FILE_SEGMENT_ELEMENT_head), nNumberOfBytesToWrite: UInt32, lpReserved: POINTER(UInt32), lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetTempPathW(nBufferLength: UInt32, lpBuffer: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetVolumeNameForVolumeMountPointW(lpszVolumeMountPoint: Windows.Win32.Foundation.PWSTR, lpszVolumeName: Windows.Win32.Foundation.PWSTR, cchBufferLength: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetVolumePathNamesForVolumeNameW(lpszVolumeName: Windows.Win32.Foundation.PWSTR, lpszVolumePathNames: Windows.Win32.Foundation.PWSTR, cchBufferLength: UInt32, lpcchReturnLength: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateFile2(lpFileName: Windows.Win32.Foundation.PWSTR, dwDesiredAccess: Windows.Win32.Storage.FileSystem.FILE_ACCESS_FLAGS, dwShareMode: Windows.Win32.Storage.FileSystem.FILE_SHARE_MODE, dwCreationDisposition: Windows.Win32.Storage.FileSystem.FILE_CREATION_DISPOSITION, pCreateExParams: POINTER(Windows.Win32.Storage.FileSystem.CREATEFILE2_EXTENDED_PARAMETERS_head)) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def SetFileIoOverlappedRange(FileHandle: Windows.Win32.Foundation.HANDLE, OverlappedRangeStart: c_char_p_no, Length: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetCompressedFileSizeA(lpFileName: Windows.Win32.Foundation.PSTR, lpFileSizeHigh: POINTER(UInt32)) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetCompressedFileSizeW(lpFileName: Windows.Win32.Foundation.PWSTR, lpFileSizeHigh: POINTER(UInt32)) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def FindFirstStreamW(lpFileName: Windows.Win32.Foundation.PWSTR, InfoLevel: Windows.Win32.Storage.FileSystem.STREAM_INFO_LEVELS, lpFindStreamData: c_void_p, dwFlags: UInt32) -> Windows.Win32.Storage.FileSystem.FindStreamHandle: ...
@winfunctype('KERNEL32.dll')
def FindNextStreamW(hFindStream: Windows.Win32.Storage.FileSystem.FindStreamHandle, lpFindStreamData: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def AreFileApisANSI() -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetTempPathA(nBufferLength: UInt32, lpBuffer: Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def FindFirstFileNameW(lpFileName: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, StringLength: POINTER(UInt32), LinkName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Storage.FileSystem.FindFileNameHandle: ...
@winfunctype('KERNEL32.dll')
def FindNextFileNameW(hFindStream: Windows.Win32.Storage.FileSystem.FindFileNameHandle, StringLength: POINTER(UInt32), LinkName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetVolumeInformationA(lpRootPathName: Windows.Win32.Foundation.PSTR, lpVolumeNameBuffer: Windows.Win32.Foundation.PSTR, nVolumeNameSize: UInt32, lpVolumeSerialNumber: POINTER(UInt32), lpMaximumComponentLength: POINTER(UInt32), lpFileSystemFlags: POINTER(UInt32), lpFileSystemNameBuffer: Windows.Win32.Foundation.PSTR, nFileSystemNameSize: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetTempFileNameA(lpPathName: Windows.Win32.Foundation.PSTR, lpPrefixString: Windows.Win32.Foundation.PSTR, uUnique: UInt32, lpTempFileName: Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def SetFileApisToOEM() -> Void: ...
@winfunctype('KERNEL32.dll')
def SetFileApisToANSI() -> Void: ...
@winfunctype('KERNEL32.dll')
def GetTempPath2W(BufferLength: UInt32, Buffer: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetTempPath2A(BufferLength: UInt32, Buffer: Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('api-ms-win-core-file-fromapp-l1-1-0.dll')
def CopyFileFromAppW(lpExistingFileName: Windows.Win32.Foundation.PWSTR, lpNewFileName: Windows.Win32.Foundation.PWSTR, bFailIfExists: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-file-fromapp-l1-1-0.dll')
def CreateDirectoryFromAppW(lpPathName: Windows.Win32.Foundation.PWSTR, lpSecurityAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-file-fromapp-l1-1-0.dll')
def CreateFileFromAppW(lpFileName: Windows.Win32.Foundation.PWSTR, dwDesiredAccess: UInt32, dwShareMode: UInt32, lpSecurityAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head), dwCreationDisposition: UInt32, dwFlagsAndAttributes: UInt32, hTemplateFile: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('api-ms-win-core-file-fromapp-l1-1-0.dll')
def CreateFile2FromAppW(lpFileName: Windows.Win32.Foundation.PWSTR, dwDesiredAccess: UInt32, dwShareMode: UInt32, dwCreationDisposition: UInt32, pCreateExParams: POINTER(Windows.Win32.Storage.FileSystem.CREATEFILE2_EXTENDED_PARAMETERS_head)) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('api-ms-win-core-file-fromapp-l1-1-0.dll')
def DeleteFileFromAppW(lpFileName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-file-fromapp-l1-1-0.dll')
def FindFirstFileExFromAppW(lpFileName: Windows.Win32.Foundation.PWSTR, fInfoLevelId: Windows.Win32.Storage.FileSystem.FINDEX_INFO_LEVELS, lpFindFileData: c_void_p, fSearchOp: Windows.Win32.Storage.FileSystem.FINDEX_SEARCH_OPS, lpSearchFilter: c_void_p, dwAdditionalFlags: UInt32) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('api-ms-win-core-file-fromapp-l1-1-0.dll')
def GetFileAttributesExFromAppW(lpFileName: Windows.Win32.Foundation.PWSTR, fInfoLevelId: Windows.Win32.Storage.FileSystem.GET_FILEEX_INFO_LEVELS, lpFileInformation: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-file-fromapp-l1-1-0.dll')
def MoveFileFromAppW(lpExistingFileName: Windows.Win32.Foundation.PWSTR, lpNewFileName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-file-fromapp-l1-1-0.dll')
def RemoveDirectoryFromAppW(lpPathName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-file-fromapp-l1-1-0.dll')
def ReplaceFileFromAppW(lpReplacedFileName: Windows.Win32.Foundation.PWSTR, lpReplacementFileName: Windows.Win32.Foundation.PWSTR, lpBackupFileName: Windows.Win32.Foundation.PWSTR, dwReplaceFlags: UInt32, lpExclude: c_void_p, lpReserved: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-file-fromapp-l1-1-0.dll')
def SetFileAttributesFromAppW(lpFileName: Windows.Win32.Foundation.PWSTR, dwFileAttributes: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('VERSION.dll')
def VerFindFileA(uFlags: Windows.Win32.Storage.FileSystem.VER_FIND_FILE_FLAGS, szFileName: Windows.Win32.Foundation.PSTR, szWinDir: Windows.Win32.Foundation.PSTR, szAppDir: Windows.Win32.Foundation.PSTR, szCurDir: Windows.Win32.Foundation.PSTR, puCurDirLen: POINTER(UInt32), szDestDir: Windows.Win32.Foundation.PSTR, puDestDirLen: POINTER(UInt32)) -> Windows.Win32.Storage.FileSystem.VER_FIND_FILE_STATUS: ...
@winfunctype('VERSION.dll')
def VerFindFileW(uFlags: Windows.Win32.Storage.FileSystem.VER_FIND_FILE_FLAGS, szFileName: Windows.Win32.Foundation.PWSTR, szWinDir: Windows.Win32.Foundation.PWSTR, szAppDir: Windows.Win32.Foundation.PWSTR, szCurDir: Windows.Win32.Foundation.PWSTR, puCurDirLen: POINTER(UInt32), szDestDir: Windows.Win32.Foundation.PWSTR, puDestDirLen: POINTER(UInt32)) -> Windows.Win32.Storage.FileSystem.VER_FIND_FILE_STATUS: ...
@winfunctype('VERSION.dll')
def VerInstallFileA(uFlags: Windows.Win32.Storage.FileSystem.VER_INSTALL_FILE_FLAGS, szSrcFileName: Windows.Win32.Foundation.PSTR, szDestFileName: Windows.Win32.Foundation.PSTR, szSrcDir: Windows.Win32.Foundation.PSTR, szDestDir: Windows.Win32.Foundation.PSTR, szCurDir: Windows.Win32.Foundation.PSTR, szTmpFile: Windows.Win32.Foundation.PSTR, puTmpFileLen: POINTER(UInt32)) -> Windows.Win32.Storage.FileSystem.VER_INSTALL_FILE_STATUS: ...
@winfunctype('VERSION.dll')
def VerInstallFileW(uFlags: Windows.Win32.Storage.FileSystem.VER_INSTALL_FILE_FLAGS, szSrcFileName: Windows.Win32.Foundation.PWSTR, szDestFileName: Windows.Win32.Foundation.PWSTR, szSrcDir: Windows.Win32.Foundation.PWSTR, szDestDir: Windows.Win32.Foundation.PWSTR, szCurDir: Windows.Win32.Foundation.PWSTR, szTmpFile: Windows.Win32.Foundation.PWSTR, puTmpFileLen: POINTER(UInt32)) -> Windows.Win32.Storage.FileSystem.VER_INSTALL_FILE_STATUS: ...
@winfunctype('VERSION.dll')
def GetFileVersionInfoSizeA(lptstrFilename: Windows.Win32.Foundation.PSTR, lpdwHandle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('VERSION.dll')
def GetFileVersionInfoSizeW(lptstrFilename: Windows.Win32.Foundation.PWSTR, lpdwHandle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('VERSION.dll')
def GetFileVersionInfoA(lptstrFilename: Windows.Win32.Foundation.PSTR, dwHandle: UInt32, dwLen: UInt32, lpData: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('VERSION.dll')
def GetFileVersionInfoW(lptstrFilename: Windows.Win32.Foundation.PWSTR, dwHandle: UInt32, dwLen: UInt32, lpData: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('VERSION.dll')
def GetFileVersionInfoSizeExA(dwFlags: Windows.Win32.Storage.FileSystem.GET_FILE_VERSION_INFO_FLAGS, lpwstrFilename: Windows.Win32.Foundation.PSTR, lpdwHandle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('VERSION.dll')
def GetFileVersionInfoSizeExW(dwFlags: Windows.Win32.Storage.FileSystem.GET_FILE_VERSION_INFO_FLAGS, lpwstrFilename: Windows.Win32.Foundation.PWSTR, lpdwHandle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('VERSION.dll')
def GetFileVersionInfoExA(dwFlags: Windows.Win32.Storage.FileSystem.GET_FILE_VERSION_INFO_FLAGS, lpwstrFilename: Windows.Win32.Foundation.PSTR, dwHandle: UInt32, dwLen: UInt32, lpData: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('VERSION.dll')
def GetFileVersionInfoExW(dwFlags: Windows.Win32.Storage.FileSystem.GET_FILE_VERSION_INFO_FLAGS, lpwstrFilename: Windows.Win32.Foundation.PWSTR, dwHandle: UInt32, dwLen: UInt32, lpData: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def VerLanguageNameA(wLang: UInt32, szLang: Windows.Win32.Foundation.PSTR, cchLang: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def VerLanguageNameW(wLang: UInt32, szLang: Windows.Win32.Foundation.PWSTR, cchLang: UInt32) -> UInt32: ...
@winfunctype('VERSION.dll')
def VerQueryValueA(pBlock: c_void_p, lpSubBlock: Windows.Win32.Foundation.PSTR, lplpBuffer: POINTER(c_void_p), puLen: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('VERSION.dll')
def VerQueryValueW(pBlock: c_void_p, lpSubBlock: Windows.Win32.Foundation.PWSTR, lplpBuffer: POINTER(c_void_p), puLen: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def LsnEqual(plsn1: POINTER(Windows.Win32.Storage.FileSystem.CLS_LSN_head), plsn2: POINTER(Windows.Win32.Storage.FileSystem.CLS_LSN_head)) -> Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('clfsw32.dll')
def LsnLess(plsn1: POINTER(Windows.Win32.Storage.FileSystem.CLS_LSN_head), plsn2: POINTER(Windows.Win32.Storage.FileSystem.CLS_LSN_head)) -> Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('clfsw32.dll')
def LsnGreater(plsn1: POINTER(Windows.Win32.Storage.FileSystem.CLS_LSN_head), plsn2: POINTER(Windows.Win32.Storage.FileSystem.CLS_LSN_head)) -> Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('clfsw32.dll')
def LsnNull(plsn: POINTER(Windows.Win32.Storage.FileSystem.CLS_LSN_head)) -> Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('clfsw32.dll')
def LsnContainer(plsn: POINTER(Windows.Win32.Storage.FileSystem.CLS_LSN_head)) -> UInt32: ...
@winfunctype('clfsw32.dll')
def LsnCreate(cidContainer: UInt32, offBlock: UInt32, cRecord: UInt32) -> Windows.Win32.Storage.FileSystem.CLS_LSN: ...
@winfunctype('clfsw32.dll')
def LsnBlockOffset(plsn: POINTER(Windows.Win32.Storage.FileSystem.CLS_LSN_head)) -> UInt32: ...
@winfunctype('clfsw32.dll')
def LsnRecordSequence(plsn: POINTER(Windows.Win32.Storage.FileSystem.CLS_LSN_head)) -> UInt32: ...
@winfunctype('clfsw32.dll')
def LsnInvalid(plsn: POINTER(Windows.Win32.Storage.FileSystem.CLS_LSN_head)) -> Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('clfsw32.dll')
def LsnIncrement(plsn: POINTER(Windows.Win32.Storage.FileSystem.CLS_LSN_head)) -> Windows.Win32.Storage.FileSystem.CLS_LSN: ...
@winfunctype('clfsw32.dll')
def CreateLogFile(pszLogFileName: Windows.Win32.Foundation.PWSTR, fDesiredAccess: Windows.Win32.Storage.FileSystem.FILE_ACCESS_FLAGS, dwShareMode: Windows.Win32.Storage.FileSystem.FILE_SHARE_MODE, psaLogFile: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head), fCreateDisposition: Windows.Win32.Storage.FileSystem.FILE_CREATION_DISPOSITION, fFlagsAndAttributes: Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('clfsw32.dll')
def DeleteLogByHandle(hLog: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def DeleteLogFile(pszLogFileName: Windows.Win32.Foundation.PWSTR, pvReserved: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def AddLogContainer(hLog: Windows.Win32.Foundation.HANDLE, pcbContainer: POINTER(UInt64), pwszContainerPath: Windows.Win32.Foundation.PWSTR, pReserved: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def AddLogContainerSet(hLog: Windows.Win32.Foundation.HANDLE, cContainer: UInt16, pcbContainer: POINTER(UInt64), rgwszContainerPath: POINTER(Windows.Win32.Foundation.PWSTR), pReserved: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def RemoveLogContainer(hLog: Windows.Win32.Foundation.HANDLE, pwszContainerPath: Windows.Win32.Foundation.PWSTR, fForce: Windows.Win32.Foundation.BOOL, pReserved: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def RemoveLogContainerSet(hLog: Windows.Win32.Foundation.HANDLE, cContainer: UInt16, rgwszContainerPath: POINTER(Windows.Win32.Foundation.PWSTR), fForce: Windows.Win32.Foundation.BOOL, pReserved: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def SetLogArchiveTail(hLog: Windows.Win32.Foundation.HANDLE, plsnArchiveTail: POINTER(Windows.Win32.Storage.FileSystem.CLS_LSN_head), pReserved: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def SetEndOfLog(hLog: Windows.Win32.Foundation.HANDLE, plsnEnd: POINTER(Windows.Win32.Storage.FileSystem.CLS_LSN_head), lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def TruncateLog(pvMarshal: c_void_p, plsnEnd: POINTER(Windows.Win32.Storage.FileSystem.CLS_LSN_head), lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def CreateLogContainerScanContext(hLog: Windows.Win32.Foundation.HANDLE, cFromContainer: UInt32, cContainers: UInt32, eScanMode: Byte, pcxScan: POINTER(Windows.Win32.Storage.FileSystem.CLS_SCAN_CONTEXT_head), pOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def ScanLogContainers(pcxScan: POINTER(Windows.Win32.Storage.FileSystem.CLS_SCAN_CONTEXT_head), eScanMode: Byte, pReserved: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def AlignReservedLog(pvMarshal: c_void_p, cReservedRecords: UInt32, rgcbReservation: POINTER(Int64), pcbAlignReservation: POINTER(Int64)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def AllocReservedLog(pvMarshal: c_void_p, cReservedRecords: UInt32, pcbAdjustment: POINTER(Int64)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def FreeReservedLog(pvMarshal: c_void_p, cReservedRecords: UInt32, pcbAdjustment: POINTER(Int64)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def GetLogFileInformation(hLog: Windows.Win32.Foundation.HANDLE, pinfoBuffer: POINTER(Windows.Win32.Storage.FileSystem.CLS_INFORMATION_head), cbBuffer: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def SetLogArchiveMode(hLog: Windows.Win32.Foundation.HANDLE, eMode: Windows.Win32.Storage.FileSystem.CLFS_LOG_ARCHIVE_MODE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def ReadLogRestartArea(pvMarshal: c_void_p, ppvRestartBuffer: POINTER(c_void_p), pcbRestartBuffer: POINTER(UInt32), plsn: POINTER(Windows.Win32.Storage.FileSystem.CLS_LSN_head), ppvContext: POINTER(c_void_p), pOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def ReadPreviousLogRestartArea(pvReadContext: c_void_p, ppvRestartBuffer: POINTER(c_void_p), pcbRestartBuffer: POINTER(UInt32), plsnRestart: POINTER(Windows.Win32.Storage.FileSystem.CLS_LSN_head), pOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def WriteLogRestartArea(pvMarshal: c_void_p, pvRestartBuffer: c_void_p, cbRestartBuffer: UInt32, plsnBase: POINTER(Windows.Win32.Storage.FileSystem.CLS_LSN_head), fFlags: Windows.Win32.Storage.FileSystem.CLFS_FLAG, pcbWritten: POINTER(UInt32), plsnNext: POINTER(Windows.Win32.Storage.FileSystem.CLS_LSN_head), pOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def GetLogReservationInfo(pvMarshal: c_void_p, pcbRecordNumber: POINTER(UInt32), pcbUserReservation: POINTER(Int64), pcbCommitReservation: POINTER(Int64)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def AdvanceLogBase(pvMarshal: c_void_p, plsnBase: POINTER(Windows.Win32.Storage.FileSystem.CLS_LSN_head), fFlags: UInt32, pOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def CloseAndResetLogFile(hLog: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def CreateLogMarshallingArea(hLog: Windows.Win32.Foundation.HANDLE, pfnAllocBuffer: Windows.Win32.Storage.FileSystem.CLFS_BLOCK_ALLOCATION, pfnFreeBuffer: Windows.Win32.Storage.FileSystem.CLFS_BLOCK_DEALLOCATION, pvBlockAllocContext: c_void_p, cbMarshallingBuffer: UInt32, cMaxWriteBuffers: UInt32, cMaxReadBuffers: UInt32, ppvMarshal: POINTER(c_void_p)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def DeleteLogMarshallingArea(pvMarshal: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def ReserveAndAppendLog(pvMarshal: c_void_p, rgWriteEntries: POINTER(Windows.Win32.Storage.FileSystem.CLS_WRITE_ENTRY_head), cWriteEntries: UInt32, plsnUndoNext: POINTER(Windows.Win32.Storage.FileSystem.CLS_LSN_head), plsnPrevious: POINTER(Windows.Win32.Storage.FileSystem.CLS_LSN_head), cReserveRecords: UInt32, rgcbReservation: POINTER(Int64), fFlags: Windows.Win32.Storage.FileSystem.CLFS_FLAG, plsn: POINTER(Windows.Win32.Storage.FileSystem.CLS_LSN_head), pOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def ReserveAndAppendLogAligned(pvMarshal: c_void_p, rgWriteEntries: POINTER(Windows.Win32.Storage.FileSystem.CLS_WRITE_ENTRY_head), cWriteEntries: UInt32, cbEntryAlignment: UInt32, plsnUndoNext: POINTER(Windows.Win32.Storage.FileSystem.CLS_LSN_head), plsnPrevious: POINTER(Windows.Win32.Storage.FileSystem.CLS_LSN_head), cReserveRecords: UInt32, rgcbReservation: POINTER(Int64), fFlags: Windows.Win32.Storage.FileSystem.CLFS_FLAG, plsn: POINTER(Windows.Win32.Storage.FileSystem.CLS_LSN_head), pOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def FlushLogBuffers(pvMarshal: c_void_p, pOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def FlushLogToLsn(pvMarshalContext: c_void_p, plsnFlush: POINTER(Windows.Win32.Storage.FileSystem.CLS_LSN_head), plsnLastFlushed: POINTER(Windows.Win32.Storage.FileSystem.CLS_LSN_head), pOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def ReadLogRecord(pvMarshal: c_void_p, plsnFirst: POINTER(Windows.Win32.Storage.FileSystem.CLS_LSN_head), eContextMode: Windows.Win32.Storage.FileSystem.CLFS_CONTEXT_MODE, ppvReadBuffer: POINTER(c_void_p), pcbReadBuffer: POINTER(UInt32), peRecordType: c_char_p_no, plsnUndoNext: POINTER(Windows.Win32.Storage.FileSystem.CLS_LSN_head), plsnPrevious: POINTER(Windows.Win32.Storage.FileSystem.CLS_LSN_head), ppvReadContext: POINTER(c_void_p), pOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def ReadNextLogRecord(pvReadContext: c_void_p, ppvBuffer: POINTER(c_void_p), pcbBuffer: POINTER(UInt32), peRecordType: c_char_p_no, plsnUser: POINTER(Windows.Win32.Storage.FileSystem.CLS_LSN_head), plsnUndoNext: POINTER(Windows.Win32.Storage.FileSystem.CLS_LSN_head), plsnPrevious: POINTER(Windows.Win32.Storage.FileSystem.CLS_LSN_head), plsnRecord: POINTER(Windows.Win32.Storage.FileSystem.CLS_LSN_head), pOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def TerminateReadLog(pvCursorContext: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def PrepareLogArchive(hLog: Windows.Win32.Foundation.HANDLE, pszBaseLogFileName: Windows.Win32.Foundation.PWSTR, cLen: UInt32, plsnLow: POINTER(Windows.Win32.Storage.FileSystem.CLS_LSN_head), plsnHigh: POINTER(Windows.Win32.Storage.FileSystem.CLS_LSN_head), pcActualLength: POINTER(UInt32), poffBaseLogFileData: POINTER(UInt64), pcbBaseLogFileLength: POINTER(UInt64), plsnBase: POINTER(Windows.Win32.Storage.FileSystem.CLS_LSN_head), plsnLast: POINTER(Windows.Win32.Storage.FileSystem.CLS_LSN_head), plsnCurrentArchiveTail: POINTER(Windows.Win32.Storage.FileSystem.CLS_LSN_head), ppvArchiveContext: POINTER(c_void_p)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def ReadLogArchiveMetadata(pvArchiveContext: c_void_p, cbOffset: UInt32, cbBytesToRead: UInt32, pbReadBuffer: c_char_p_no, pcbBytesRead: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def GetNextLogArchiveExtent(pvArchiveContext: c_void_p, rgadExtent: POINTER(Windows.Win32.Storage.FileSystem.CLS_ARCHIVE_DESCRIPTOR_head), cDescriptors: UInt32, pcDescriptorsReturned: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def TerminateLogArchive(pvArchiveContext: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def ValidateLog(pszLogFileName: Windows.Win32.Foundation.PWSTR, psaLogFile: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head), pinfoBuffer: POINTER(Windows.Win32.Storage.FileSystem.CLS_INFORMATION_head), pcbBuffer: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def GetLogContainerName(hLog: Windows.Win32.Foundation.HANDLE, cidLogicalContainer: UInt32, pwstrContainerName: Windows.Win32.Foundation.PWSTR, cLenContainerName: UInt32, pcActualLenContainerName: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def GetLogIoStatistics(hLog: Windows.Win32.Foundation.HANDLE, pvStatsBuffer: c_void_p, cbStatsBuffer: UInt32, eStatsClass: Windows.Win32.Storage.FileSystem.CLFS_IOSTATS_CLASS, pcbStatsWritten: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def RegisterManageableLogClient(hLog: Windows.Win32.Foundation.HANDLE, pCallbacks: POINTER(Windows.Win32.Storage.FileSystem.LOG_MANAGEMENT_CALLBACKS_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def DeregisterManageableLogClient(hLog: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def ReadLogNotification(hLog: Windows.Win32.Foundation.HANDLE, pNotification: POINTER(Windows.Win32.Storage.FileSystem.CLFS_MGMT_NOTIFICATION_head), lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def InstallLogPolicy(hLog: Windows.Win32.Foundation.HANDLE, pPolicy: POINTER(Windows.Win32.Storage.FileSystem.CLFS_MGMT_POLICY_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def RemoveLogPolicy(hLog: Windows.Win32.Foundation.HANDLE, ePolicyType: Windows.Win32.Storage.FileSystem.CLFS_MGMT_POLICY_TYPE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def QueryLogPolicy(hLog: Windows.Win32.Foundation.HANDLE, ePolicyType: Windows.Win32.Storage.FileSystem.CLFS_MGMT_POLICY_TYPE, pPolicyBuffer: POINTER(Windows.Win32.Storage.FileSystem.CLFS_MGMT_POLICY_head), pcbPolicyBuffer: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def SetLogFileSizeWithPolicy(hLog: Windows.Win32.Foundation.HANDLE, pDesiredSize: POINTER(UInt64), pResultingSize: POINTER(UInt64)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def HandleLogFull(hLog: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def LogTailAdvanceFailure(hLog: Windows.Win32.Foundation.HANDLE, dwReason: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def RegisterForLogWriteNotification(hLog: Windows.Win32.Foundation.HANDLE, cbThreshold: UInt32, fEnable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def QueryUsersOnEncryptedFile(lpFileName: Windows.Win32.Foundation.PWSTR, pUsers: POINTER(POINTER(Windows.Win32.Storage.FileSystem.ENCRYPTION_CERTIFICATE_HASH_LIST_head))) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def QueryRecoveryAgentsOnEncryptedFile(lpFileName: Windows.Win32.Foundation.PWSTR, pRecoveryAgents: POINTER(POINTER(Windows.Win32.Storage.FileSystem.ENCRYPTION_CERTIFICATE_HASH_LIST_head))) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def RemoveUsersFromEncryptedFile(lpFileName: Windows.Win32.Foundation.PWSTR, pHashes: POINTER(Windows.Win32.Storage.FileSystem.ENCRYPTION_CERTIFICATE_HASH_LIST_head)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def AddUsersToEncryptedFile(lpFileName: Windows.Win32.Foundation.PWSTR, pEncryptionCertificates: POINTER(Windows.Win32.Storage.FileSystem.ENCRYPTION_CERTIFICATE_LIST_head)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def SetUserFileEncryptionKey(pEncryptionCertificate: POINTER(Windows.Win32.Storage.FileSystem.ENCRYPTION_CERTIFICATE_head)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def SetUserFileEncryptionKeyEx(pEncryptionCertificate: POINTER(Windows.Win32.Storage.FileSystem.ENCRYPTION_CERTIFICATE_head), dwCapabilities: UInt32, dwFlags: UInt32, pvReserved: c_void_p) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def FreeEncryptionCertificateHashList(pUsers: POINTER(Windows.Win32.Storage.FileSystem.ENCRYPTION_CERTIFICATE_HASH_LIST_head)) -> Void: ...
@winfunctype('ADVAPI32.dll')
def EncryptionDisable(DirPath: Windows.Win32.Foundation.PWSTR, Disable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def DuplicateEncryptionInfoFile(SrcFileName: Windows.Win32.Foundation.PWSTR, DstFileName: Windows.Win32.Foundation.PWSTR, dwCreationDistribution: UInt32, dwAttributes: UInt32, lpSecurityAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def GetEncryptedFileMetadata(lpFileName: Windows.Win32.Foundation.PWSTR, pcbMetadata: POINTER(UInt32), ppbMetadata: POINTER(c_char_p_no)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def SetEncryptedFileMetadata(lpFileName: Windows.Win32.Foundation.PWSTR, pbOldMetadata: c_char_p_no, pbNewMetadata: c_char_p_no, pOwnerHash: POINTER(Windows.Win32.Storage.FileSystem.ENCRYPTION_CERTIFICATE_HASH_head), dwOperation: UInt32, pCertificatesAdded: POINTER(Windows.Win32.Storage.FileSystem.ENCRYPTION_CERTIFICATE_HASH_LIST_head)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def FreeEncryptedFileMetadata(pbMetadata: c_char_p_no) -> Void: ...
@winfunctype('KERNEL32.dll')
def LZStart() -> Int32: ...
@winfunctype('KERNEL32.dll')
def LZDone() -> Void: ...
@winfunctype('KERNEL32.dll')
def CopyLZFile(hfSource: Int32, hfDest: Int32) -> Int32: ...
@winfunctype('KERNEL32.dll')
def LZCopy(hfSource: Int32, hfDest: Int32) -> Int32: ...
@winfunctype('KERNEL32.dll')
def LZInit(hfSource: Int32) -> Int32: ...
@winfunctype('KERNEL32.dll')
def GetExpandedNameA(lpszSource: Windows.Win32.Foundation.PSTR, lpszBuffer: Windows.Win32.Foundation.PSTR) -> Int32: ...
@winfunctype('KERNEL32.dll')
def GetExpandedNameW(lpszSource: Windows.Win32.Foundation.PWSTR, lpszBuffer: Windows.Win32.Foundation.PWSTR) -> Int32: ...
@winfunctype('KERNEL32.dll')
def LZOpenFileA(lpFileName: Windows.Win32.Foundation.PSTR, lpReOpenBuf: POINTER(Windows.Win32.Storage.FileSystem.OFSTRUCT_head), wStyle: Windows.Win32.Storage.FileSystem.LZOPENFILE_STYLE) -> Int32: ...
@winfunctype('KERNEL32.dll')
def LZOpenFileW(lpFileName: Windows.Win32.Foundation.PWSTR, lpReOpenBuf: POINTER(Windows.Win32.Storage.FileSystem.OFSTRUCT_head), wStyle: Windows.Win32.Storage.FileSystem.LZOPENFILE_STYLE) -> Int32: ...
@winfunctype('KERNEL32.dll')
def LZSeek(hFile: Int32, lOffset: Int32, iOrigin: Int32) -> Int32: ...
@winfunctype('KERNEL32.dll')
def LZRead(hFile: Int32, lpBuffer: Windows.Win32.Foundation.PSTR, cbRead: Int32) -> Int32: ...
@winfunctype('KERNEL32.dll')
def LZClose(hFile: Int32) -> Void: ...
@winfunctype('WOFUTIL.dll')
def WofShouldCompressBinaries(Volume: Windows.Win32.Foundation.PWSTR, Algorithm: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WOFUTIL.dll')
def WofGetDriverVersion(FileOrVolumeHandle: Windows.Win32.Foundation.HANDLE, Provider: UInt32, WofVersion: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WOFUTIL.dll')
def WofSetFileDataLocation(FileHandle: Windows.Win32.Foundation.HANDLE, Provider: UInt32, ExternalFileInfo: c_void_p, Length: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WOFUTIL.dll')
def WofIsExternalFile(FilePath: Windows.Win32.Foundation.PWSTR, IsExternalFile: POINTER(Windows.Win32.Foundation.BOOL), Provider: POINTER(UInt32), ExternalFileInfo: c_void_p, BufferLength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WOFUTIL.dll')
def WofEnumEntries(VolumeName: Windows.Win32.Foundation.PWSTR, Provider: UInt32, EnumProc: Windows.Win32.Storage.FileSystem.WofEnumEntryProc, UserData: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WOFUTIL.dll')
def WofWimAddEntry(VolumeName: Windows.Win32.Foundation.PWSTR, WimPath: Windows.Win32.Foundation.PWSTR, WimType: UInt32, WimIndex: UInt32, DataSourceId: POINTER(Windows.Win32.Foundation.LARGE_INTEGER_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WOFUTIL.dll')
def WofWimEnumFiles(VolumeName: Windows.Win32.Foundation.PWSTR, DataSourceId: Windows.Win32.Foundation.LARGE_INTEGER, EnumProc: Windows.Win32.Storage.FileSystem.WofEnumFilesProc, UserData: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WOFUTIL.dll')
def WofWimSuspendEntry(VolumeName: Windows.Win32.Foundation.PWSTR, DataSourceId: Windows.Win32.Foundation.LARGE_INTEGER) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WOFUTIL.dll')
def WofWimRemoveEntry(VolumeName: Windows.Win32.Foundation.PWSTR, DataSourceId: Windows.Win32.Foundation.LARGE_INTEGER) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WOFUTIL.dll')
def WofWimUpdateEntry(VolumeName: Windows.Win32.Foundation.PWSTR, DataSourceId: Windows.Win32.Foundation.LARGE_INTEGER, NewWimPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WOFUTIL.dll')
def WofFileEnumFiles(VolumeName: Windows.Win32.Foundation.PWSTR, Algorithm: UInt32, EnumProc: Windows.Win32.Storage.FileSystem.WofEnumFilesProc, UserData: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('txfw32.dll')
def TxfLogCreateFileReadContext(LogPath: Windows.Win32.Foundation.PWSTR, BeginningLsn: Windows.Win32.Storage.FileSystem.CLS_LSN, EndingLsn: Windows.Win32.Storage.FileSystem.CLS_LSN, TxfFileId: POINTER(Windows.Win32.Storage.FileSystem.TXF_ID_head), TxfLogContext: POINTER(c_void_p)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('txfw32.dll')
def TxfLogCreateRangeReadContext(LogPath: Windows.Win32.Foundation.PWSTR, BeginningLsn: Windows.Win32.Storage.FileSystem.CLS_LSN, EndingLsn: Windows.Win32.Storage.FileSystem.CLS_LSN, BeginningVirtualClock: POINTER(Windows.Win32.Foundation.LARGE_INTEGER_head), EndingVirtualClock: POINTER(Windows.Win32.Foundation.LARGE_INTEGER_head), RecordTypeMask: UInt32, TxfLogContext: POINTER(c_void_p)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('txfw32.dll')
def TxfLogDestroyReadContext(TxfLogContext: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('txfw32.dll')
def TxfLogReadRecords(TxfLogContext: c_void_p, BufferLength: UInt32, Buffer: c_void_p, BytesUsed: POINTER(UInt32), RecordCount: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('txfw32.dll')
def TxfReadMetadataInfo(FileHandle: Windows.Win32.Foundation.HANDLE, TxfFileId: POINTER(Windows.Win32.Storage.FileSystem.TXF_ID_head), LastLsn: POINTER(Windows.Win32.Storage.FileSystem.CLS_LSN_head), TransactionState: POINTER(UInt32), LockingTransaction: POINTER(Guid)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('txfw32.dll')
def TxfLogRecordGetFileName(RecordBuffer: c_void_p, RecordBufferLengthInBytes: UInt32, NameBuffer: Windows.Win32.Foundation.PWSTR, NameBufferLengthInBytes: POINTER(UInt32), TxfId: POINTER(Windows.Win32.Storage.FileSystem.TXF_ID_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('txfw32.dll')
def TxfLogRecordGetGenericType(RecordBuffer: c_void_p, RecordBufferLengthInBytes: UInt32, GenericType: POINTER(UInt32), VirtualClock: POINTER(Windows.Win32.Foundation.LARGE_INTEGER_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('txfw32.dll')
def TxfSetThreadMiniVersionForCreate(MiniVersion: UInt16) -> Void: ...
@winfunctype('txfw32.dll')
def TxfGetThreadMiniVersionForCreate(MiniVersion: POINTER(UInt16)) -> Void: ...
@winfunctype('ktmw32.dll')
def CreateTransaction(lpTransactionAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head), UOW: POINTER(Guid), CreateOptions: UInt32, IsolationLevel: UInt32, IsolationFlags: UInt32, Timeout: UInt32, Description: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('ktmw32.dll')
def OpenTransaction(dwDesiredAccess: UInt32, TransactionId: POINTER(Guid)) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('ktmw32.dll')
def CommitTransaction(TransactionHandle: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def CommitTransactionAsync(TransactionHandle: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def RollbackTransaction(TransactionHandle: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def RollbackTransactionAsync(TransactionHandle: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def GetTransactionId(TransactionHandle: Windows.Win32.Foundation.HANDLE, TransactionId: POINTER(Guid)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def GetTransactionInformation(TransactionHandle: Windows.Win32.Foundation.HANDLE, Outcome: POINTER(UInt32), IsolationLevel: POINTER(UInt32), IsolationFlags: POINTER(UInt32), Timeout: POINTER(UInt32), BufferLength: UInt32, Description: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def SetTransactionInformation(TransactionHandle: Windows.Win32.Foundation.HANDLE, IsolationLevel: UInt32, IsolationFlags: UInt32, Timeout: UInt32, Description: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def CreateTransactionManager(lpTransactionAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head), LogFileName: Windows.Win32.Foundation.PWSTR, CreateOptions: UInt32, CommitStrength: UInt32) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('ktmw32.dll')
def OpenTransactionManager(LogFileName: Windows.Win32.Foundation.PWSTR, DesiredAccess: UInt32, OpenOptions: UInt32) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('ktmw32.dll')
def OpenTransactionManagerById(TransactionManagerId: POINTER(Guid), DesiredAccess: UInt32, OpenOptions: UInt32) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('ktmw32.dll')
def RenameTransactionManager(LogFileName: Windows.Win32.Foundation.PWSTR, ExistingTransactionManagerGuid: POINTER(Guid)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def RollforwardTransactionManager(TransactionManagerHandle: Windows.Win32.Foundation.HANDLE, TmVirtualClock: POINTER(Windows.Win32.Foundation.LARGE_INTEGER_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def RecoverTransactionManager(TransactionManagerHandle: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def GetCurrentClockTransactionManager(TransactionManagerHandle: Windows.Win32.Foundation.HANDLE, TmVirtualClock: POINTER(Windows.Win32.Foundation.LARGE_INTEGER_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def GetTransactionManagerId(TransactionManagerHandle: Windows.Win32.Foundation.HANDLE, TransactionManagerId: POINTER(Guid)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def CreateResourceManager(lpResourceManagerAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head), ResourceManagerId: POINTER(Guid), CreateOptions: UInt32, TmHandle: Windows.Win32.Foundation.HANDLE, Description: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('ktmw32.dll')
def OpenResourceManager(dwDesiredAccess: UInt32, TmHandle: Windows.Win32.Foundation.HANDLE, ResourceManagerId: POINTER(Guid)) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('ktmw32.dll')
def RecoverResourceManager(ResourceManagerHandle: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def GetNotificationResourceManager(ResourceManagerHandle: Windows.Win32.Foundation.HANDLE, TransactionNotification: POINTER(Windows.Win32.Storage.FileSystem.TRANSACTION_NOTIFICATION_head), NotificationLength: UInt32, dwMilliseconds: UInt32, ReturnLength: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def GetNotificationResourceManagerAsync(ResourceManagerHandle: Windows.Win32.Foundation.HANDLE, TransactionNotification: POINTER(Windows.Win32.Storage.FileSystem.TRANSACTION_NOTIFICATION_head), TransactionNotificationLength: UInt32, ReturnLength: POINTER(UInt32), lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def SetResourceManagerCompletionPort(ResourceManagerHandle: Windows.Win32.Foundation.HANDLE, IoCompletionPortHandle: Windows.Win32.Foundation.HANDLE, CompletionKey: UIntPtr) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def CreateEnlistment(lpEnlistmentAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head), ResourceManagerHandle: Windows.Win32.Foundation.HANDLE, TransactionHandle: Windows.Win32.Foundation.HANDLE, NotificationMask: UInt32, CreateOptions: UInt32, EnlistmentKey: c_void_p) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('ktmw32.dll')
def OpenEnlistment(dwDesiredAccess: UInt32, ResourceManagerHandle: Windows.Win32.Foundation.HANDLE, EnlistmentId: POINTER(Guid)) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('ktmw32.dll')
def RecoverEnlistment(EnlistmentHandle: Windows.Win32.Foundation.HANDLE, EnlistmentKey: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def GetEnlistmentRecoveryInformation(EnlistmentHandle: Windows.Win32.Foundation.HANDLE, BufferSize: UInt32, Buffer: c_void_p, BufferUsed: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def GetEnlistmentId(EnlistmentHandle: Windows.Win32.Foundation.HANDLE, EnlistmentId: POINTER(Guid)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def SetEnlistmentRecoveryInformation(EnlistmentHandle: Windows.Win32.Foundation.HANDLE, BufferSize: UInt32, Buffer: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def PrepareEnlistment(EnlistmentHandle: Windows.Win32.Foundation.HANDLE, TmVirtualClock: POINTER(Windows.Win32.Foundation.LARGE_INTEGER_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def PrePrepareEnlistment(EnlistmentHandle: Windows.Win32.Foundation.HANDLE, TmVirtualClock: POINTER(Windows.Win32.Foundation.LARGE_INTEGER_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def CommitEnlistment(EnlistmentHandle: Windows.Win32.Foundation.HANDLE, TmVirtualClock: POINTER(Windows.Win32.Foundation.LARGE_INTEGER_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def RollbackEnlistment(EnlistmentHandle: Windows.Win32.Foundation.HANDLE, TmVirtualClock: POINTER(Windows.Win32.Foundation.LARGE_INTEGER_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def PrePrepareComplete(EnlistmentHandle: Windows.Win32.Foundation.HANDLE, TmVirtualClock: POINTER(Windows.Win32.Foundation.LARGE_INTEGER_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def PrepareComplete(EnlistmentHandle: Windows.Win32.Foundation.HANDLE, TmVirtualClock: POINTER(Windows.Win32.Foundation.LARGE_INTEGER_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def ReadOnlyEnlistment(EnlistmentHandle: Windows.Win32.Foundation.HANDLE, TmVirtualClock: POINTER(Windows.Win32.Foundation.LARGE_INTEGER_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def CommitComplete(EnlistmentHandle: Windows.Win32.Foundation.HANDLE, TmVirtualClock: POINTER(Windows.Win32.Foundation.LARGE_INTEGER_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def RollbackComplete(EnlistmentHandle: Windows.Win32.Foundation.HANDLE, TmVirtualClock: POINTER(Windows.Win32.Foundation.LARGE_INTEGER_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def SinglePhaseReject(EnlistmentHandle: Windows.Win32.Foundation.HANDLE, TmVirtualClock: POINTER(Windows.Win32.Foundation.LARGE_INTEGER_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('NETAPI32.dll')
def NetShareAdd(servername: Windows.Win32.Foundation.PWSTR, level: UInt32, buf: c_char_p_no, parm_err: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetShareEnum(servername: Windows.Win32.Foundation.PWSTR, level: UInt32, bufptr: POINTER(c_char_p_no), prefmaxlen: UInt32, entriesread: POINTER(UInt32), totalentries: POINTER(UInt32), resume_handle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetShareEnumSticky(servername: Windows.Win32.Foundation.PWSTR, level: UInt32, bufptr: POINTER(c_char_p_no), prefmaxlen: UInt32, entriesread: POINTER(UInt32), totalentries: POINTER(UInt32), resume_handle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetShareGetInfo(servername: Windows.Win32.Foundation.PWSTR, netname: Windows.Win32.Foundation.PWSTR, level: UInt32, bufptr: POINTER(c_char_p_no)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetShareSetInfo(servername: Windows.Win32.Foundation.PWSTR, netname: Windows.Win32.Foundation.PWSTR, level: UInt32, buf: c_char_p_no, parm_err: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetShareDel(servername: Windows.Win32.Foundation.PWSTR, netname: Windows.Win32.Foundation.PWSTR, reserved: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetShareDelSticky(servername: Windows.Win32.Foundation.PWSTR, netname: Windows.Win32.Foundation.PWSTR, reserved: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetShareCheck(servername: Windows.Win32.Foundation.PWSTR, device: Windows.Win32.Foundation.PWSTR, type: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetShareDelEx(servername: Windows.Win32.Foundation.PWSTR, level: UInt32, buf: c_char_p_no) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetServerAliasAdd(servername: Windows.Win32.Foundation.PWSTR, level: UInt32, buf: c_char_p_no) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetServerAliasDel(servername: Windows.Win32.Foundation.PWSTR, level: UInt32, buf: c_char_p_no) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetServerAliasEnum(servername: Windows.Win32.Foundation.PWSTR, level: UInt32, bufptr: POINTER(c_char_p_no), prefmaxlen: UInt32, entriesread: POINTER(UInt32), totalentries: POINTER(UInt32), resumehandle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetSessionEnum(servername: Windows.Win32.Foundation.PWSTR, UncClientName: Windows.Win32.Foundation.PWSTR, username: Windows.Win32.Foundation.PWSTR, level: UInt32, bufptr: POINTER(c_char_p_no), prefmaxlen: UInt32, entriesread: POINTER(UInt32), totalentries: POINTER(UInt32), resume_handle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetSessionDel(servername: Windows.Win32.Foundation.PWSTR, UncClientName: Windows.Win32.Foundation.PWSTR, username: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetSessionGetInfo(servername: Windows.Win32.Foundation.PWSTR, UncClientName: Windows.Win32.Foundation.PWSTR, username: Windows.Win32.Foundation.PWSTR, level: UInt32, bufptr: POINTER(c_char_p_no)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetConnectionEnum(servername: Windows.Win32.Foundation.PWSTR, qualifier: Windows.Win32.Foundation.PWSTR, level: UInt32, bufptr: POINTER(c_char_p_no), prefmaxlen: UInt32, entriesread: POINTER(UInt32), totalentries: POINTER(UInt32), resume_handle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetFileClose(servername: Windows.Win32.Foundation.PWSTR, fileid: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetFileEnum(servername: Windows.Win32.Foundation.PWSTR, basepath: Windows.Win32.Foundation.PWSTR, username: Windows.Win32.Foundation.PWSTR, level: UInt32, bufptr: POINTER(c_char_p_no), prefmaxlen: UInt32, entriesread: POINTER(UInt32), totalentries: POINTER(UInt32), resume_handle: POINTER(UIntPtr)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetFileGetInfo(servername: Windows.Win32.Foundation.PWSTR, fileid: UInt32, level: UInt32, bufptr: POINTER(c_char_p_no)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetStatisticsGet(ServerName: POINTER(SByte), Service: POINTER(SByte), Level: UInt32, Options: UInt32, Buffer: POINTER(c_char_p_no)) -> UInt32: ...
@winfunctype('api-ms-win-core-ioring-l1-1-0.dll')
def QueryIoRingCapabilities(capabilities: POINTER(Windows.Win32.Storage.FileSystem.IORING_CAPABILITIES_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-ioring-l1-1-0.dll')
def IsIoRingOpSupported(ioRing: POINTER(Windows.Win32.Storage.FileSystem.HIORING___head), op: Windows.Win32.Storage.FileSystem.IORING_OP_CODE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-ioring-l1-1-0.dll')
def CreateIoRing(ioringVersion: Windows.Win32.Storage.FileSystem.IORING_VERSION, flags: Windows.Win32.Storage.FileSystem.IORING_CREATE_FLAGS, submissionQueueSize: UInt32, completionQueueSize: UInt32, h: POINTER(POINTER(Windows.Win32.Storage.FileSystem.HIORING___head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-ioring-l1-1-0.dll')
def GetIoRingInfo(ioRing: POINTER(Windows.Win32.Storage.FileSystem.HIORING___head), info: POINTER(Windows.Win32.Storage.FileSystem.IORING_INFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-ioring-l1-1-0.dll')
def SubmitIoRing(ioRing: POINTER(Windows.Win32.Storage.FileSystem.HIORING___head), waitOperations: UInt32, milliseconds: UInt32, submittedEntries: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-ioring-l1-1-0.dll')
def CloseIoRing(ioRing: POINTER(Windows.Win32.Storage.FileSystem.HIORING___head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-ioring-l1-1-0.dll')
def PopIoRingCompletion(ioRing: POINTER(Windows.Win32.Storage.FileSystem.HIORING___head), cqe: POINTER(Windows.Win32.Storage.FileSystem.IORING_CQE_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-ioring-l1-1-0.dll')
def SetIoRingCompletionEvent(ioRing: POINTER(Windows.Win32.Storage.FileSystem.HIORING___head), hEvent: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-ioring-l1-1-0.dll')
def BuildIoRingCancelRequest(ioRing: POINTER(Windows.Win32.Storage.FileSystem.HIORING___head), file: Windows.Win32.Storage.FileSystem.IORING_HANDLE_REF, opToCancel: UIntPtr, userData: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-ioring-l1-1-0.dll')
def BuildIoRingReadFile(ioRing: POINTER(Windows.Win32.Storage.FileSystem.HIORING___head), fileRef: Windows.Win32.Storage.FileSystem.IORING_HANDLE_REF, dataRef: Windows.Win32.Storage.FileSystem.IORING_BUFFER_REF, numberOfBytesToRead: UInt32, fileOffset: UInt64, userData: UIntPtr, flags: Windows.Win32.Storage.FileSystem.IORING_SQE_FLAGS) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-ioring-l1-1-0.dll')
def BuildIoRingRegisterFileHandles(ioRing: POINTER(Windows.Win32.Storage.FileSystem.HIORING___head), count: UInt32, handles: POINTER(Windows.Win32.Foundation.HANDLE), userData: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-ioring-l1-1-0.dll')
def BuildIoRingRegisterBuffers(ioRing: POINTER(Windows.Win32.Storage.FileSystem.HIORING___head), count: UInt32, buffers: POINTER(Windows.Win32.Storage.FileSystem.IORING_BUFFER_INFO_head), userData: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def Wow64EnableWow64FsRedirection(Wow64FsEnableRedirection: Windows.Win32.Foundation.BOOLEAN) -> Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('KERNEL32.dll')
def Wow64DisableWow64FsRedirection(OldValue: POINTER(c_void_p)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def Wow64RevertWow64FsRedirection(OlValue: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetBinaryTypeA(lpApplicationName: Windows.Win32.Foundation.PSTR, lpBinaryType: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetBinaryTypeW(lpApplicationName: Windows.Win32.Foundation.PWSTR, lpBinaryType: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetShortPathNameA(lpszLongPath: Windows.Win32.Foundation.PSTR, lpszShortPath: Windows.Win32.Foundation.PSTR, cchBuffer: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetLongPathNameTransactedA(lpszShortPath: Windows.Win32.Foundation.PSTR, lpszLongPath: Windows.Win32.Foundation.PSTR, cchBuffer: UInt32, hTransaction: Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetLongPathNameTransactedW(lpszShortPath: Windows.Win32.Foundation.PWSTR, lpszLongPath: Windows.Win32.Foundation.PWSTR, cchBuffer: UInt32, hTransaction: Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def SetFileCompletionNotificationModes(FileHandle: Windows.Win32.Foundation.HANDLE, Flags: Byte) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetFileShortNameA(hFile: Windows.Win32.Foundation.HANDLE, lpShortName: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetFileShortNameW(hFile: Windows.Win32.Foundation.HANDLE, lpShortName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetTapePosition(hDevice: Windows.Win32.Foundation.HANDLE, dwPositionMethod: Windows.Win32.Storage.FileSystem.TAPE_POSITION_METHOD, dwPartition: UInt32, dwOffsetLow: UInt32, dwOffsetHigh: UInt32, bImmediate: Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetTapePosition(hDevice: Windows.Win32.Foundation.HANDLE, dwPositionType: Windows.Win32.Storage.FileSystem.TAPE_POSITION_TYPE, lpdwPartition: POINTER(UInt32), lpdwOffsetLow: POINTER(UInt32), lpdwOffsetHigh: POINTER(UInt32)) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def PrepareTape(hDevice: Windows.Win32.Foundation.HANDLE, dwOperation: Windows.Win32.Storage.FileSystem.PREPARE_TAPE_OPERATION, bImmediate: Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def EraseTape(hDevice: Windows.Win32.Foundation.HANDLE, dwEraseType: Windows.Win32.Storage.FileSystem.ERASE_TAPE_TYPE, bImmediate: Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def CreateTapePartition(hDevice: Windows.Win32.Foundation.HANDLE, dwPartitionMethod: Windows.Win32.Storage.FileSystem.CREATE_TAPE_PARTITION_METHOD, dwCount: UInt32, dwSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def WriteTapemark(hDevice: Windows.Win32.Foundation.HANDLE, dwTapemarkType: Windows.Win32.Storage.FileSystem.TAPEMARK_TYPE, dwTapemarkCount: UInt32, bImmediate: Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetTapeStatus(hDevice: Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetTapeParameters(hDevice: Windows.Win32.Foundation.HANDLE, dwOperation: Windows.Win32.Storage.FileSystem.GET_TAPE_DRIVE_PARAMETERS_OPERATION, lpdwSize: POINTER(UInt32), lpTapeInformation: c_void_p) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def SetTapeParameters(hDevice: Windows.Win32.Foundation.HANDLE, dwOperation: Windows.Win32.Storage.FileSystem.TAPE_INFORMATION_TYPE, lpTapeInformation: c_void_p) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def EncryptFileA(lpFileName: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def EncryptFileW(lpFileName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def DecryptFileA(lpFileName: Windows.Win32.Foundation.PSTR, dwReserved: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def DecryptFileW(lpFileName: Windows.Win32.Foundation.PWSTR, dwReserved: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def FileEncryptionStatusA(lpFileName: Windows.Win32.Foundation.PSTR, lpStatus: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def FileEncryptionStatusW(lpFileName: Windows.Win32.Foundation.PWSTR, lpStatus: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def OpenEncryptedFileRawA(lpFileName: Windows.Win32.Foundation.PSTR, ulFlags: UInt32, pvContext: POINTER(c_void_p)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def OpenEncryptedFileRawW(lpFileName: Windows.Win32.Foundation.PWSTR, ulFlags: UInt32, pvContext: POINTER(c_void_p)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def ReadEncryptedFileRaw(pfExportCallback: Windows.Win32.Storage.FileSystem.PFE_EXPORT_FUNC, pvCallbackContext: c_void_p, pvContext: c_void_p) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def WriteEncryptedFileRaw(pfImportCallback: Windows.Win32.Storage.FileSystem.PFE_IMPORT_FUNC, pvCallbackContext: c_void_p, pvContext: c_void_p) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def CloseEncryptedFileRaw(pvContext: c_void_p) -> Void: ...
@winfunctype('KERNEL32.dll')
def OpenFile(lpFileName: Windows.Win32.Foundation.PSTR, lpReOpenBuff: POINTER(Windows.Win32.Storage.FileSystem.OFSTRUCT_head), uStyle: UInt32) -> Int32: ...
@winfunctype('KERNEL32.dll')
def BackupRead(hFile: Windows.Win32.Foundation.HANDLE, lpBuffer: c_char_p_no, nNumberOfBytesToRead: UInt32, lpNumberOfBytesRead: POINTER(UInt32), bAbort: Windows.Win32.Foundation.BOOL, bProcessSecurity: Windows.Win32.Foundation.BOOL, lpContext: POINTER(c_void_p)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def BackupSeek(hFile: Windows.Win32.Foundation.HANDLE, dwLowBytesToSeek: UInt32, dwHighBytesToSeek: UInt32, lpdwLowByteSeeked: POINTER(UInt32), lpdwHighByteSeeked: POINTER(UInt32), lpContext: POINTER(c_void_p)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def BackupWrite(hFile: Windows.Win32.Foundation.HANDLE, lpBuffer: c_char_p_no, nNumberOfBytesToWrite: UInt32, lpNumberOfBytesWritten: POINTER(UInt32), bAbort: Windows.Win32.Foundation.BOOL, bProcessSecurity: Windows.Win32.Foundation.BOOL, lpContext: POINTER(c_void_p)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetLogicalDriveStringsA(nBufferLength: UInt32, lpBuffer: Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def SetSearchPathMode(Flags: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateDirectoryExA(lpTemplateDirectory: Windows.Win32.Foundation.PSTR, lpNewDirectory: Windows.Win32.Foundation.PSTR, lpSecurityAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateDirectoryExW(lpTemplateDirectory: Windows.Win32.Foundation.PWSTR, lpNewDirectory: Windows.Win32.Foundation.PWSTR, lpSecurityAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateDirectoryTransactedA(lpTemplateDirectory: Windows.Win32.Foundation.PSTR, lpNewDirectory: Windows.Win32.Foundation.PSTR, lpSecurityAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head), hTransaction: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateDirectoryTransactedW(lpTemplateDirectory: Windows.Win32.Foundation.PWSTR, lpNewDirectory: Windows.Win32.Foundation.PWSTR, lpSecurityAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head), hTransaction: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def RemoveDirectoryTransactedA(lpPathName: Windows.Win32.Foundation.PSTR, hTransaction: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def RemoveDirectoryTransactedW(lpPathName: Windows.Win32.Foundation.PWSTR, hTransaction: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetFullPathNameTransactedA(lpFileName: Windows.Win32.Foundation.PSTR, nBufferLength: UInt32, lpBuffer: Windows.Win32.Foundation.PSTR, lpFilePart: POINTER(Windows.Win32.Foundation.PSTR), hTransaction: Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetFullPathNameTransactedW(lpFileName: Windows.Win32.Foundation.PWSTR, nBufferLength: UInt32, lpBuffer: Windows.Win32.Foundation.PWSTR, lpFilePart: POINTER(Windows.Win32.Foundation.PWSTR), hTransaction: Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def DefineDosDeviceA(dwFlags: Windows.Win32.Storage.FileSystem.DEFINE_DOS_DEVICE_FLAGS, lpDeviceName: Windows.Win32.Foundation.PSTR, lpTargetPath: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def QueryDosDeviceA(lpDeviceName: Windows.Win32.Foundation.PSTR, lpTargetPath: Windows.Win32.Foundation.PSTR, ucchMax: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def CreateFileTransactedA(lpFileName: Windows.Win32.Foundation.PSTR, dwDesiredAccess: UInt32, dwShareMode: Windows.Win32.Storage.FileSystem.FILE_SHARE_MODE, lpSecurityAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head), dwCreationDisposition: Windows.Win32.Storage.FileSystem.FILE_CREATION_DISPOSITION, dwFlagsAndAttributes: Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES, hTemplateFile: Windows.Win32.Foundation.HANDLE, hTransaction: Windows.Win32.Foundation.HANDLE, pusMiniVersion: POINTER(Windows.Win32.Storage.FileSystem.TXFS_MINIVERSION), lpExtendedParameter: c_void_p) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def CreateFileTransactedW(lpFileName: Windows.Win32.Foundation.PWSTR, dwDesiredAccess: UInt32, dwShareMode: Windows.Win32.Storage.FileSystem.FILE_SHARE_MODE, lpSecurityAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head), dwCreationDisposition: Windows.Win32.Storage.FileSystem.FILE_CREATION_DISPOSITION, dwFlagsAndAttributes: Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES, hTemplateFile: Windows.Win32.Foundation.HANDLE, hTransaction: Windows.Win32.Foundation.HANDLE, pusMiniVersion: POINTER(Windows.Win32.Storage.FileSystem.TXFS_MINIVERSION), lpExtendedParameter: c_void_p) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def ReOpenFile(hOriginalFile: Windows.Win32.Foundation.HANDLE, dwDesiredAccess: Windows.Win32.Storage.FileSystem.FILE_ACCESS_FLAGS, dwShareMode: Windows.Win32.Storage.FileSystem.FILE_SHARE_MODE, dwFlagsAndAttributes: Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def SetFileAttributesTransactedA(lpFileName: Windows.Win32.Foundation.PSTR, dwFileAttributes: UInt32, hTransaction: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetFileAttributesTransactedW(lpFileName: Windows.Win32.Foundation.PWSTR, dwFileAttributes: UInt32, hTransaction: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetFileAttributesTransactedA(lpFileName: Windows.Win32.Foundation.PSTR, fInfoLevelId: Windows.Win32.Storage.FileSystem.GET_FILEEX_INFO_LEVELS, lpFileInformation: c_void_p, hTransaction: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetFileAttributesTransactedW(lpFileName: Windows.Win32.Foundation.PWSTR, fInfoLevelId: Windows.Win32.Storage.FileSystem.GET_FILEEX_INFO_LEVELS, lpFileInformation: c_void_p, hTransaction: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetCompressedFileSizeTransactedA(lpFileName: Windows.Win32.Foundation.PSTR, lpFileSizeHigh: POINTER(UInt32), hTransaction: Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetCompressedFileSizeTransactedW(lpFileName: Windows.Win32.Foundation.PWSTR, lpFileSizeHigh: POINTER(UInt32), hTransaction: Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def DeleteFileTransactedA(lpFileName: Windows.Win32.Foundation.PSTR, hTransaction: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DeleteFileTransactedW(lpFileName: Windows.Win32.Foundation.PWSTR, hTransaction: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CheckNameLegalDOS8Dot3A(lpName: Windows.Win32.Foundation.PSTR, lpOemName: Windows.Win32.Foundation.PSTR, OemNameSize: UInt32, pbNameContainsSpaces: POINTER(Windows.Win32.Foundation.BOOL), pbNameLegal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CheckNameLegalDOS8Dot3W(lpName: Windows.Win32.Foundation.PWSTR, lpOemName: Windows.Win32.Foundation.PSTR, OemNameSize: UInt32, pbNameContainsSpaces: POINTER(Windows.Win32.Foundation.BOOL), pbNameLegal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FindFirstFileTransactedA(lpFileName: Windows.Win32.Foundation.PSTR, fInfoLevelId: Windows.Win32.Storage.FileSystem.FINDEX_INFO_LEVELS, lpFindFileData: c_void_p, fSearchOp: Windows.Win32.Storage.FileSystem.FINDEX_SEARCH_OPS, lpSearchFilter: c_void_p, dwAdditionalFlags: UInt32, hTransaction: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Storage.FileSystem.FindFileHandle: ...
@winfunctype('KERNEL32.dll')
def FindFirstFileTransactedW(lpFileName: Windows.Win32.Foundation.PWSTR, fInfoLevelId: Windows.Win32.Storage.FileSystem.FINDEX_INFO_LEVELS, lpFindFileData: c_void_p, fSearchOp: Windows.Win32.Storage.FileSystem.FINDEX_SEARCH_OPS, lpSearchFilter: c_void_p, dwAdditionalFlags: UInt32, hTransaction: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Storage.FileSystem.FindFileHandle: ...
@winfunctype('KERNEL32.dll')
def CopyFileA(lpExistingFileName: Windows.Win32.Foundation.PSTR, lpNewFileName: Windows.Win32.Foundation.PSTR, bFailIfExists: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CopyFileW(lpExistingFileName: Windows.Win32.Foundation.PWSTR, lpNewFileName: Windows.Win32.Foundation.PWSTR, bFailIfExists: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CopyFileExA(lpExistingFileName: Windows.Win32.Foundation.PSTR, lpNewFileName: Windows.Win32.Foundation.PSTR, lpProgressRoutine: Windows.Win32.Storage.FileSystem.LPPROGRESS_ROUTINE, lpData: c_void_p, pbCancel: POINTER(Int32), dwCopyFlags: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CopyFileExW(lpExistingFileName: Windows.Win32.Foundation.PWSTR, lpNewFileName: Windows.Win32.Foundation.PWSTR, lpProgressRoutine: Windows.Win32.Storage.FileSystem.LPPROGRESS_ROUTINE, lpData: c_void_p, pbCancel: POINTER(Int32), dwCopyFlags: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CopyFileTransactedA(lpExistingFileName: Windows.Win32.Foundation.PSTR, lpNewFileName: Windows.Win32.Foundation.PSTR, lpProgressRoutine: Windows.Win32.Storage.FileSystem.LPPROGRESS_ROUTINE, lpData: c_void_p, pbCancel: POINTER(Int32), dwCopyFlags: UInt32, hTransaction: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CopyFileTransactedW(lpExistingFileName: Windows.Win32.Foundation.PWSTR, lpNewFileName: Windows.Win32.Foundation.PWSTR, lpProgressRoutine: Windows.Win32.Storage.FileSystem.LPPROGRESS_ROUTINE, lpData: c_void_p, pbCancel: POINTER(Int32), dwCopyFlags: UInt32, hTransaction: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CopyFile2(pwszExistingFileName: Windows.Win32.Foundation.PWSTR, pwszNewFileName: Windows.Win32.Foundation.PWSTR, pExtendedParameters: POINTER(Windows.Win32.Storage.FileSystem.COPYFILE2_EXTENDED_PARAMETERS_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def MoveFileA(lpExistingFileName: Windows.Win32.Foundation.PSTR, lpNewFileName: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def MoveFileW(lpExistingFileName: Windows.Win32.Foundation.PWSTR, lpNewFileName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def MoveFileExA(lpExistingFileName: Windows.Win32.Foundation.PSTR, lpNewFileName: Windows.Win32.Foundation.PSTR, dwFlags: Windows.Win32.Storage.FileSystem.MOVE_FILE_FLAGS) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def MoveFileExW(lpExistingFileName: Windows.Win32.Foundation.PWSTR, lpNewFileName: Windows.Win32.Foundation.PWSTR, dwFlags: Windows.Win32.Storage.FileSystem.MOVE_FILE_FLAGS) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def MoveFileWithProgressA(lpExistingFileName: Windows.Win32.Foundation.PSTR, lpNewFileName: Windows.Win32.Foundation.PSTR, lpProgressRoutine: Windows.Win32.Storage.FileSystem.LPPROGRESS_ROUTINE, lpData: c_void_p, dwFlags: Windows.Win32.Storage.FileSystem.MOVE_FILE_FLAGS) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def MoveFileWithProgressW(lpExistingFileName: Windows.Win32.Foundation.PWSTR, lpNewFileName: Windows.Win32.Foundation.PWSTR, lpProgressRoutine: Windows.Win32.Storage.FileSystem.LPPROGRESS_ROUTINE, lpData: c_void_p, dwFlags: Windows.Win32.Storage.FileSystem.MOVE_FILE_FLAGS) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def MoveFileTransactedA(lpExistingFileName: Windows.Win32.Foundation.PSTR, lpNewFileName: Windows.Win32.Foundation.PSTR, lpProgressRoutine: Windows.Win32.Storage.FileSystem.LPPROGRESS_ROUTINE, lpData: c_void_p, dwFlags: Windows.Win32.Storage.FileSystem.MOVE_FILE_FLAGS, hTransaction: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def MoveFileTransactedW(lpExistingFileName: Windows.Win32.Foundation.PWSTR, lpNewFileName: Windows.Win32.Foundation.PWSTR, lpProgressRoutine: Windows.Win32.Storage.FileSystem.LPPROGRESS_ROUTINE, lpData: c_void_p, dwFlags: Windows.Win32.Storage.FileSystem.MOVE_FILE_FLAGS, hTransaction: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ReplaceFileA(lpReplacedFileName: Windows.Win32.Foundation.PSTR, lpReplacementFileName: Windows.Win32.Foundation.PSTR, lpBackupFileName: Windows.Win32.Foundation.PSTR, dwReplaceFlags: Windows.Win32.Storage.FileSystem.REPLACE_FILE_FLAGS, lpExclude: c_void_p, lpReserved: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ReplaceFileW(lpReplacedFileName: Windows.Win32.Foundation.PWSTR, lpReplacementFileName: Windows.Win32.Foundation.PWSTR, lpBackupFileName: Windows.Win32.Foundation.PWSTR, dwReplaceFlags: Windows.Win32.Storage.FileSystem.REPLACE_FILE_FLAGS, lpExclude: c_void_p, lpReserved: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateHardLinkA(lpFileName: Windows.Win32.Foundation.PSTR, lpExistingFileName: Windows.Win32.Foundation.PSTR, lpSecurityAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateHardLinkW(lpFileName: Windows.Win32.Foundation.PWSTR, lpExistingFileName: Windows.Win32.Foundation.PWSTR, lpSecurityAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateHardLinkTransactedA(lpFileName: Windows.Win32.Foundation.PSTR, lpExistingFileName: Windows.Win32.Foundation.PSTR, lpSecurityAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head), hTransaction: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateHardLinkTransactedW(lpFileName: Windows.Win32.Foundation.PWSTR, lpExistingFileName: Windows.Win32.Foundation.PWSTR, lpSecurityAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head), hTransaction: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FindFirstStreamTransactedW(lpFileName: Windows.Win32.Foundation.PWSTR, InfoLevel: Windows.Win32.Storage.FileSystem.STREAM_INFO_LEVELS, lpFindStreamData: c_void_p, dwFlags: UInt32, hTransaction: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Storage.FileSystem.FindStreamHandle: ...
@winfunctype('KERNEL32.dll')
def FindFirstFileNameTransactedW(lpFileName: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, StringLength: POINTER(UInt32), LinkName: Windows.Win32.Foundation.PWSTR, hTransaction: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Storage.FileSystem.FindFileNameHandle: ...
@winfunctype('KERNEL32.dll')
def SetVolumeLabelA(lpRootPathName: Windows.Win32.Foundation.PSTR, lpVolumeName: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetVolumeLabelW(lpRootPathName: Windows.Win32.Foundation.PWSTR, lpVolumeName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetFileBandwidthReservation(hFile: Windows.Win32.Foundation.HANDLE, nPeriodMilliseconds: UInt32, nBytesPerPeriod: UInt32, bDiscardable: Windows.Win32.Foundation.BOOL, lpTransferSize: POINTER(UInt32), lpNumOutstandingRequests: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetFileBandwidthReservation(hFile: Windows.Win32.Foundation.HANDLE, lpPeriodMilliseconds: POINTER(UInt32), lpBytesPerPeriod: POINTER(UInt32), pDiscardable: POINTER(Int32), lpTransferSize: POINTER(UInt32), lpNumOutstandingRequests: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ReadDirectoryChangesW(hDirectory: Windows.Win32.Foundation.HANDLE, lpBuffer: c_void_p, nBufferLength: UInt32, bWatchSubtree: Windows.Win32.Foundation.BOOL, dwNotifyFilter: Windows.Win32.Storage.FileSystem.FILE_NOTIFY_CHANGE, lpBytesReturned: POINTER(UInt32), lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head), lpCompletionRoutine: Windows.Win32.System.IO.LPOVERLAPPED_COMPLETION_ROUTINE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ReadDirectoryChangesExW(hDirectory: Windows.Win32.Foundation.HANDLE, lpBuffer: c_void_p, nBufferLength: UInt32, bWatchSubtree: Windows.Win32.Foundation.BOOL, dwNotifyFilter: Windows.Win32.Storage.FileSystem.FILE_NOTIFY_CHANGE, lpBytesReturned: POINTER(UInt32), lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head), lpCompletionRoutine: Windows.Win32.System.IO.LPOVERLAPPED_COMPLETION_ROUTINE, ReadDirectoryNotifyInformationClass: Windows.Win32.Storage.FileSystem.READ_DIRECTORY_NOTIFY_INFORMATION_CLASS) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FindFirstVolumeA(lpszVolumeName: Windows.Win32.Foundation.PSTR, cchBufferLength: UInt32) -> Windows.Win32.Storage.FileSystem.FindVolumeHandle: ...
@winfunctype('KERNEL32.dll')
def FindNextVolumeA(hFindVolume: Windows.Win32.Storage.FileSystem.FindVolumeHandle, lpszVolumeName: Windows.Win32.Foundation.PSTR, cchBufferLength: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FindFirstVolumeMountPointA(lpszRootPathName: Windows.Win32.Foundation.PSTR, lpszVolumeMountPoint: Windows.Win32.Foundation.PSTR, cchBufferLength: UInt32) -> Windows.Win32.Storage.FileSystem.FindVolumeMointPointHandle: ...
@winfunctype('KERNEL32.dll')
def FindFirstVolumeMountPointW(lpszRootPathName: Windows.Win32.Foundation.PWSTR, lpszVolumeMountPoint: Windows.Win32.Foundation.PWSTR, cchBufferLength: UInt32) -> Windows.Win32.Storage.FileSystem.FindVolumeMointPointHandle: ...
@winfunctype('KERNEL32.dll')
def FindNextVolumeMountPointA(hFindVolumeMountPoint: Windows.Win32.Storage.FileSystem.FindVolumeMointPointHandle, lpszVolumeMountPoint: Windows.Win32.Foundation.PSTR, cchBufferLength: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FindNextVolumeMountPointW(hFindVolumeMountPoint: Windows.Win32.Storage.FileSystem.FindVolumeMointPointHandle, lpszVolumeMountPoint: Windows.Win32.Foundation.PWSTR, cchBufferLength: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FindVolumeMountPointClose(hFindVolumeMountPoint: Windows.Win32.Storage.FileSystem.FindVolumeMointPointHandle) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetVolumeMountPointA(lpszVolumeMountPoint: Windows.Win32.Foundation.PSTR, lpszVolumeName: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetVolumeMountPointW(lpszVolumeMountPoint: Windows.Win32.Foundation.PWSTR, lpszVolumeName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DeleteVolumeMountPointA(lpszVolumeMountPoint: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetVolumeNameForVolumeMountPointA(lpszVolumeMountPoint: Windows.Win32.Foundation.PSTR, lpszVolumeName: Windows.Win32.Foundation.PSTR, cchBufferLength: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetVolumePathNameA(lpszFileName: Windows.Win32.Foundation.PSTR, lpszVolumePathName: Windows.Win32.Foundation.PSTR, cchBufferLength: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetVolumePathNamesForVolumeNameA(lpszVolumeName: Windows.Win32.Foundation.PSTR, lpszVolumePathNames: Windows.Win32.Foundation.PSTR, cchBufferLength: UInt32, lpcchReturnLength: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetFileInformationByHandleEx(hFile: Windows.Win32.Foundation.HANDLE, FileInformationClass: Windows.Win32.Storage.FileSystem.FILE_INFO_BY_HANDLE_CLASS, lpFileInformation: c_void_p, dwBufferSize: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def OpenFileById(hVolumeHint: Windows.Win32.Foundation.HANDLE, lpFileId: POINTER(Windows.Win32.Storage.FileSystem.FILE_ID_DESCRIPTOR_head), dwDesiredAccess: Windows.Win32.Storage.FileSystem.FILE_ACCESS_FLAGS, dwShareMode: Windows.Win32.Storage.FileSystem.FILE_SHARE_MODE, lpSecurityAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head), dwFlagsAndAttributes: Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def CreateSymbolicLinkA(lpSymlinkFileName: Windows.Win32.Foundation.PSTR, lpTargetFileName: Windows.Win32.Foundation.PSTR, dwFlags: Windows.Win32.Storage.FileSystem.SYMBOLIC_LINK_FLAGS) -> Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('KERNEL32.dll')
def CreateSymbolicLinkW(lpSymlinkFileName: Windows.Win32.Foundation.PWSTR, lpTargetFileName: Windows.Win32.Foundation.PWSTR, dwFlags: Windows.Win32.Storage.FileSystem.SYMBOLIC_LINK_FLAGS) -> Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('KERNEL32.dll')
def CreateSymbolicLinkTransactedA(lpSymlinkFileName: Windows.Win32.Foundation.PSTR, lpTargetFileName: Windows.Win32.Foundation.PSTR, dwFlags: Windows.Win32.Storage.FileSystem.SYMBOLIC_LINK_FLAGS, hTransaction: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('KERNEL32.dll')
def CreateSymbolicLinkTransactedW(lpSymlinkFileName: Windows.Win32.Foundation.PWSTR, lpTargetFileName: Windows.Win32.Foundation.PWSTR, dwFlags: Windows.Win32.Storage.FileSystem.SYMBOLIC_LINK_FLAGS, hTransaction: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('ntdll.dll')
def NtCreateFile(FileHandle: POINTER(Windows.Win32.Foundation.HANDLE), DesiredAccess: UInt32, ObjectAttributes: POINTER(Windows.Win32.System.WindowsProgramming.OBJECT_ATTRIBUTES_head), IoStatusBlock: POINTER(Windows.Win32.System.WindowsProgramming.IO_STATUS_BLOCK_head), AllocationSize: POINTER(Windows.Win32.Foundation.LARGE_INTEGER_head), FileAttributes: UInt32, ShareAccess: Windows.Win32.Storage.FileSystem.FILE_SHARE_MODE, CreateDisposition: Windows.Win32.Storage.FileSystem.NT_CREATE_FILE_DISPOSITION, CreateOptions: UInt32, EaBuffer: c_void_p, EaLength: UInt32) -> Windows.Win32.Foundation.NTSTATUS: ...
class BY_HANDLE_FILE_INFORMATION(Structure):
    dwFileAttributes: UInt32
    ftCreationTime: Windows.Win32.Foundation.FILETIME
    ftLastAccessTime: Windows.Win32.Foundation.FILETIME
    ftLastWriteTime: Windows.Win32.Foundation.FILETIME
    dwVolumeSerialNumber: UInt32
    nFileSizeHigh: UInt32
    nFileSizeLow: UInt32
    nNumberOfLinks: UInt32
    nFileIndexHigh: UInt32
    nFileIndexLow: UInt32
@winfunctype_pointer
def CACHE_ACCESS_CHECK(pSecurityDescriptor: Windows.Win32.Security.PSECURITY_DESCRIPTOR, hClientToken: Windows.Win32.Foundation.HANDLE, dwDesiredAccess: UInt32, GenericMapping: POINTER(Windows.Win32.Security.GENERIC_MAPPING_head), PrivilegeSet: POINTER(Windows.Win32.Security.PRIVILEGE_SET_head), PrivilegeSetLength: POINTER(UInt32), GrantedAccess: POINTER(UInt32), AccessStatus: POINTER(Int32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def CACHE_DESTROY_CALLBACK(cb: UInt32, lpb: c_char_p_no) -> Void: ...
@winfunctype_pointer
def CACHE_KEY_COMPARE(cbKey1: UInt32, lpbKey1: c_char_p_no, cbKey2: UInt32, lpbKey2: c_char_p_no) -> Int32: ...
@winfunctype_pointer
def CACHE_KEY_HASH(lpbKey: c_char_p_no, cbKey: UInt32) -> UInt32: ...
@winfunctype_pointer
def CACHE_READ_CALLBACK(cb: UInt32, lpb: c_char_p_no, lpvContext: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def CLAIMMEDIALABEL(pBuffer: c_char_p_no, nBufferSize: UInt32, pLabelInfo: POINTER(Windows.Win32.Storage.FileSystem.MediaLabelInfo_head)) -> UInt32: ...
@winfunctype_pointer
def CLAIMMEDIALABELEX(pBuffer: c_char_p_no, nBufferSize: UInt32, pLabelInfo: POINTER(Windows.Win32.Storage.FileSystem.MediaLabelInfo_head), LabelGuid: POINTER(Guid)) -> UInt32: ...
@winfunctype_pointer
def CLFS_BLOCK_ALLOCATION(cbBufferLength: UInt32, pvUserContext: c_void_p) -> c_void_p: ...
@winfunctype_pointer
def CLFS_BLOCK_DEALLOCATION(pvBuffer: c_void_p, pvUserContext: c_void_p) -> Void: ...
CLFS_CONTEXT_MODE = Int32
CLFS_CONTEXT_MODE_ClfsContextNone: CLFS_CONTEXT_MODE = 0
CLFS_CONTEXT_MODE_ClfsContextUndoNext: CLFS_CONTEXT_MODE = 1
CLFS_CONTEXT_MODE_ClfsContextPrevious: CLFS_CONTEXT_MODE = 2
CLFS_CONTEXT_MODE_ClfsContextForward: CLFS_CONTEXT_MODE = 3
CLFS_FLAG = UInt32
CLFS_FLAG_FORCE_APPEND: CLFS_FLAG = 1
CLFS_FLAG_FORCE_FLUSH: CLFS_FLAG = 2
CLFS_FLAG_NO_FLAGS: CLFS_FLAG = 0
CLFS_FLAG_USE_RESERVATION: CLFS_FLAG = 4
CLFS_IOSTATS_CLASS = Int32
CLFS_IOSTATS_CLASS_ClfsIoStatsDefault: CLFS_IOSTATS_CLASS = 0
CLFS_IOSTATS_CLASS_ClfsIoStatsMax: CLFS_IOSTATS_CLASS = 65535
CLFS_LOG_ARCHIVE_MODE = Int32
CLFS_LOG_ARCHIVE_MODE_ClfsLogArchiveEnabled: CLFS_LOG_ARCHIVE_MODE = 1
CLFS_LOG_ARCHIVE_MODE_ClfsLogArchiveDisabled: CLFS_LOG_ARCHIVE_MODE = 2
class CLFS_LOG_NAME_INFORMATION(Structure):
    NameLengthInBytes: UInt16
    Name: Char * 1
class CLFS_MGMT_NOTIFICATION(Structure):
    Notification: Windows.Win32.Storage.FileSystem.CLFS_MGMT_NOTIFICATION_TYPE
    Lsn: Windows.Win32.Storage.FileSystem.CLS_LSN
    LogIsPinned: UInt16
CLFS_MGMT_NOTIFICATION_TYPE = Int32
CLFS_MGMT_NOTIFICATION_TYPE_ClfsMgmtAdvanceTailNotification: CLFS_MGMT_NOTIFICATION_TYPE = 0
CLFS_MGMT_NOTIFICATION_TYPE_ClfsMgmtLogFullHandlerNotification: CLFS_MGMT_NOTIFICATION_TYPE = 1
CLFS_MGMT_NOTIFICATION_TYPE_ClfsMgmtLogUnpinnedNotification: CLFS_MGMT_NOTIFICATION_TYPE = 2
CLFS_MGMT_NOTIFICATION_TYPE_ClfsMgmtLogWriteNotification: CLFS_MGMT_NOTIFICATION_TYPE = 3
class CLFS_MGMT_POLICY(Structure):
    Version: UInt32
    LengthInBytes: UInt32
    PolicyFlags: UInt32
    PolicyType: Windows.Win32.Storage.FileSystem.CLFS_MGMT_POLICY_TYPE
    PolicyParameters: _PolicyParameters_e__Union
    class _PolicyParameters_e__Union(Union):
        MaximumSize: _MaximumSize_e__Struct
        MinimumSize: _MinimumSize_e__Struct
        NewContainerSize: _NewContainerSize_e__Struct
        GrowthRate: _GrowthRate_e__Struct
        LogTail: _LogTail_e__Struct
        AutoShrink: _AutoShrink_e__Struct
        AutoGrow: _AutoGrow_e__Struct
        NewContainerPrefix: _NewContainerPrefix_e__Struct
        NewContainerSuffix: _NewContainerSuffix_e__Struct
        NewContainerExtension: _NewContainerExtension_e__Struct
        class _MaximumSize_e__Struct(Structure):
            Containers: UInt32
        class _MinimumSize_e__Struct(Structure):
            Containers: UInt32
        class _NewContainerSize_e__Struct(Structure):
            SizeInBytes: UInt32
        class _GrowthRate_e__Struct(Structure):
            AbsoluteGrowthInContainers: UInt32
            RelativeGrowthPercentage: UInt32
        class _LogTail_e__Struct(Structure):
            MinimumAvailablePercentage: UInt32
            MinimumAvailableContainers: UInt32
        class _AutoShrink_e__Struct(Structure):
            Percentage: UInt32
        class _AutoGrow_e__Struct(Structure):
            Enabled: UInt32
        class _NewContainerPrefix_e__Struct(Structure):
            PrefixLengthInBytes: UInt16
            PrefixString: Char * 1
        class _NewContainerSuffix_e__Struct(Structure):
            NextContainerSuffix: UInt64
        class _NewContainerExtension_e__Struct(Structure):
            ExtensionLengthInBytes: UInt16
            ExtensionString: Char * 1
CLFS_MGMT_POLICY_TYPE = Int32
CLFS_MGMT_POLICY_TYPE_ClfsMgmtPolicyMaximumSize: CLFS_MGMT_POLICY_TYPE = 0
CLFS_MGMT_POLICY_TYPE_ClfsMgmtPolicyMinimumSize: CLFS_MGMT_POLICY_TYPE = 1
CLFS_MGMT_POLICY_TYPE_ClfsMgmtPolicyNewContainerSize: CLFS_MGMT_POLICY_TYPE = 2
CLFS_MGMT_POLICY_TYPE_ClfsMgmtPolicyGrowthRate: CLFS_MGMT_POLICY_TYPE = 3
CLFS_MGMT_POLICY_TYPE_ClfsMgmtPolicyLogTail: CLFS_MGMT_POLICY_TYPE = 4
CLFS_MGMT_POLICY_TYPE_ClfsMgmtPolicyAutoShrink: CLFS_MGMT_POLICY_TYPE = 5
CLFS_MGMT_POLICY_TYPE_ClfsMgmtPolicyAutoGrow: CLFS_MGMT_POLICY_TYPE = 6
CLFS_MGMT_POLICY_TYPE_ClfsMgmtPolicyNewContainerPrefix: CLFS_MGMT_POLICY_TYPE = 7
CLFS_MGMT_POLICY_TYPE_ClfsMgmtPolicyNewContainerSuffix: CLFS_MGMT_POLICY_TYPE = 8
CLFS_MGMT_POLICY_TYPE_ClfsMgmtPolicyNewContainerExtension: CLFS_MGMT_POLICY_TYPE = 9
CLFS_MGMT_POLICY_TYPE_ClfsMgmtPolicyInvalid: CLFS_MGMT_POLICY_TYPE = 10
class CLFS_NODE_ID(Structure):
    cType: UInt32
    cbNode: UInt32
class CLFS_PHYSICAL_LSN_INFORMATION(Structure):
    StreamIdentifier: Byte
    VirtualLsn: Windows.Win32.Storage.FileSystem.CLS_LSN
    PhysicalLsn: Windows.Win32.Storage.FileSystem.CLS_LSN
class CLFS_STREAM_ID_INFORMATION(Structure):
    StreamIdentifier: Byte
class CLS_ARCHIVE_DESCRIPTOR(Structure):
    coffLow: UInt64
    coffHigh: UInt64
    infoContainer: Windows.Win32.Storage.FileSystem.CLS_CONTAINER_INFORMATION
class CLS_CONTAINER_INFORMATION(Structure):
    FileAttributes: UInt32
    CreationTime: UInt64
    LastAccessTime: UInt64
    LastWriteTime: UInt64
    ContainerSize: Int64
    FileNameActualLength: UInt32
    FileNameLength: UInt32
    FileName: Char * 256
    State: UInt32
    PhysicalContainerId: UInt32
    LogicalContainerId: UInt32
CLS_CONTEXT_MODE = Int32
CLS_CONTEXT_MODE_ClsContextNone: CLS_CONTEXT_MODE = 0
CLS_CONTEXT_MODE_ClsContextUndoNext: CLS_CONTEXT_MODE = 1
CLS_CONTEXT_MODE_ClsContextPrevious: CLS_CONTEXT_MODE = 2
CLS_CONTEXT_MODE_ClsContextForward: CLS_CONTEXT_MODE = 3
class CLS_INFORMATION(Structure):
    TotalAvailable: Int64
    CurrentAvailable: Int64
    TotalReservation: Int64
    BaseFileSize: UInt64
    ContainerSize: UInt64
    TotalContainers: UInt32
    FreeContainers: UInt32
    TotalClients: UInt32
    Attributes: UInt32
    FlushThreshold: UInt32
    SectorSize: UInt32
    MinArchiveTailLsn: Windows.Win32.Storage.FileSystem.CLS_LSN
    BaseLsn: Windows.Win32.Storage.FileSystem.CLS_LSN
    LastFlushedLsn: Windows.Win32.Storage.FileSystem.CLS_LSN
    LastLsn: Windows.Win32.Storage.FileSystem.CLS_LSN
    RestartLsn: Windows.Win32.Storage.FileSystem.CLS_LSN
    Identity: Guid
CLS_IOSTATS_CLASS = Int32
CLS_IOSTATS_CLASS_ClsIoStatsDefault: CLS_IOSTATS_CLASS = 0
CLS_IOSTATS_CLASS_ClsIoStatsMax: CLS_IOSTATS_CLASS = 65535
class CLS_IO_STATISTICS(Structure):
    hdrIoStats: Windows.Win32.Storage.FileSystem.CLS_IO_STATISTICS_HEADER
    cFlush: UInt64
    cbFlush: UInt64
    cMetaFlush: UInt64
    cbMetaFlush: UInt64
class CLS_IO_STATISTICS_HEADER(Structure):
    ubMajorVersion: Byte
    ubMinorVersion: Byte
    eStatsClass: Windows.Win32.Storage.FileSystem.CLFS_IOSTATS_CLASS
    cbLength: UInt16
    coffData: UInt32
CLS_LOG_INFORMATION_CLASS = Int32
CLS_LOG_INFORMATION_CLASS_ClfsLogBasicInformation: CLS_LOG_INFORMATION_CLASS = 0
CLS_LOG_INFORMATION_CLASS_ClfsLogBasicInformationPhysical: CLS_LOG_INFORMATION_CLASS = 1
CLS_LOG_INFORMATION_CLASS_ClfsLogPhysicalNameInformation: CLS_LOG_INFORMATION_CLASS = 2
CLS_LOG_INFORMATION_CLASS_ClfsLogStreamIdentifierInformation: CLS_LOG_INFORMATION_CLASS = 3
CLS_LOG_INFORMATION_CLASS_ClfsLogSystemMarkingInformation: CLS_LOG_INFORMATION_CLASS = 4
CLS_LOG_INFORMATION_CLASS_ClfsLogPhysicalLsnInformation: CLS_LOG_INFORMATION_CLASS = 5
class CLS_LSN(Structure):
    Internal: UInt64
class CLS_SCAN_CONTEXT(Structure):
    cidNode: Windows.Win32.Storage.FileSystem.CLFS_NODE_ID
    hLog: Windows.Win32.Foundation.HANDLE
    cIndex: UInt32
    cContainers: UInt32
    cContainersReturned: UInt32
    eScanMode: Byte
    pinfoContainer: POINTER(Windows.Win32.Storage.FileSystem.CLS_CONTAINER_INFORMATION_head)
class CLS_WRITE_ENTRY(Structure):
    Buffer: c_void_p
    ByteLength: UInt32
COMPRESSION_FORMAT = UInt16
COMPRESSION_FORMAT_NONE: COMPRESSION_FORMAT = 0
COMPRESSION_FORMAT_DEFAULT: COMPRESSION_FORMAT = 1
COMPRESSION_FORMAT_LZNT1: COMPRESSION_FORMAT = 2
COMPRESSION_FORMAT_XPRESS: COMPRESSION_FORMAT = 3
COMPRESSION_FORMAT_XPRESS_HUFF: COMPRESSION_FORMAT = 4
COMPRESSION_FORMAT_XP10: COMPRESSION_FORMAT = 5
class CONNECTION_INFO_0(Structure):
    coni0_id: UInt32
class CONNECTION_INFO_1(Structure):
    coni1_id: UInt32
    coni1_type: Windows.Win32.Storage.FileSystem.SHARE_TYPE
    coni1_num_opens: UInt32
    coni1_num_users: UInt32
    coni1_time: UInt32
    coni1_username: Windows.Win32.Foundation.PWSTR
    coni1_netname: Windows.Win32.Foundation.PWSTR
COPYFILE2_COPY_PHASE = Int32
COPYFILE2_PHASE_NONE: COPYFILE2_COPY_PHASE = 0
COPYFILE2_PHASE_PREPARE_SOURCE: COPYFILE2_COPY_PHASE = 1
COPYFILE2_PHASE_PREPARE_DEST: COPYFILE2_COPY_PHASE = 2
COPYFILE2_PHASE_READ_SOURCE: COPYFILE2_COPY_PHASE = 3
COPYFILE2_PHASE_WRITE_DESTINATION: COPYFILE2_COPY_PHASE = 4
COPYFILE2_PHASE_SERVER_COPY: COPYFILE2_COPY_PHASE = 5
COPYFILE2_PHASE_NAMEGRAFT_COPY: COPYFILE2_COPY_PHASE = 6
COPYFILE2_PHASE_MAX: COPYFILE2_COPY_PHASE = 7
class COPYFILE2_EXTENDED_PARAMETERS(Structure):
    dwSize: UInt32
    dwCopyFlags: UInt32
    pfCancel: POINTER(Windows.Win32.Foundation.BOOL)
    pProgressRoutine: Windows.Win32.Storage.FileSystem.PCOPYFILE2_PROGRESS_ROUTINE
    pvCallbackContext: c_void_p
class COPYFILE2_EXTENDED_PARAMETERS_V2(Structure):
    dwSize: UInt32
    dwCopyFlags: UInt32
    pfCancel: POINTER(Windows.Win32.Foundation.BOOL)
    pProgressRoutine: Windows.Win32.Storage.FileSystem.PCOPYFILE2_PROGRESS_ROUTINE
    pvCallbackContext: c_void_p
    dwCopyFlagsV2: UInt32
    ioDesiredSize: UInt32
    ioDesiredRate: UInt32
    reserved: c_void_p * 8
class COPYFILE2_MESSAGE(Structure):
    Type: Windows.Win32.Storage.FileSystem.COPYFILE2_MESSAGE_TYPE
    dwPadding: UInt32
    Info: _Info_e__Union
    class _Info_e__Union(Union):
        ChunkStarted: _ChunkStarted_e__Struct
        ChunkFinished: _ChunkFinished_e__Struct
        StreamStarted: _StreamStarted_e__Struct
        StreamFinished: _StreamFinished_e__Struct
        PollContinue: _PollContinue_e__Struct
        Error: _Error_e__Struct
        class _ChunkStarted_e__Struct(Structure):
            dwStreamNumber: UInt32
            dwReserved: UInt32
            hSourceFile: Windows.Win32.Foundation.HANDLE
            hDestinationFile: Windows.Win32.Foundation.HANDLE
            uliChunkNumber: Windows.Win32.Foundation.ULARGE_INTEGER
            uliChunkSize: Windows.Win32.Foundation.ULARGE_INTEGER
            uliStreamSize: Windows.Win32.Foundation.ULARGE_INTEGER
            uliTotalFileSize: Windows.Win32.Foundation.ULARGE_INTEGER
        class _ChunkFinished_e__Struct(Structure):
            dwStreamNumber: UInt32
            dwFlags: UInt32
            hSourceFile: Windows.Win32.Foundation.HANDLE
            hDestinationFile: Windows.Win32.Foundation.HANDLE
            uliChunkNumber: Windows.Win32.Foundation.ULARGE_INTEGER
            uliChunkSize: Windows.Win32.Foundation.ULARGE_INTEGER
            uliStreamSize: Windows.Win32.Foundation.ULARGE_INTEGER
            uliStreamBytesTransferred: Windows.Win32.Foundation.ULARGE_INTEGER
            uliTotalFileSize: Windows.Win32.Foundation.ULARGE_INTEGER
            uliTotalBytesTransferred: Windows.Win32.Foundation.ULARGE_INTEGER
        class _StreamStarted_e__Struct(Structure):
            dwStreamNumber: UInt32
            dwReserved: UInt32
            hSourceFile: Windows.Win32.Foundation.HANDLE
            hDestinationFile: Windows.Win32.Foundation.HANDLE
            uliStreamSize: Windows.Win32.Foundation.ULARGE_INTEGER
            uliTotalFileSize: Windows.Win32.Foundation.ULARGE_INTEGER
        class _StreamFinished_e__Struct(Structure):
            dwStreamNumber: UInt32
            dwReserved: UInt32
            hSourceFile: Windows.Win32.Foundation.HANDLE
            hDestinationFile: Windows.Win32.Foundation.HANDLE
            uliStreamSize: Windows.Win32.Foundation.ULARGE_INTEGER
            uliStreamBytesTransferred: Windows.Win32.Foundation.ULARGE_INTEGER
            uliTotalFileSize: Windows.Win32.Foundation.ULARGE_INTEGER
            uliTotalBytesTransferred: Windows.Win32.Foundation.ULARGE_INTEGER
        class _PollContinue_e__Struct(Structure):
            dwReserved: UInt32
        class _Error_e__Struct(Structure):
            CopyPhase: Windows.Win32.Storage.FileSystem.COPYFILE2_COPY_PHASE
            dwStreamNumber: UInt32
            hrFailure: Windows.Win32.Foundation.HRESULT
            dwReserved: UInt32
            uliChunkNumber: Windows.Win32.Foundation.ULARGE_INTEGER
            uliStreamSize: Windows.Win32.Foundation.ULARGE_INTEGER
            uliStreamBytesTransferred: Windows.Win32.Foundation.ULARGE_INTEGER
            uliTotalFileSize: Windows.Win32.Foundation.ULARGE_INTEGER
            uliTotalBytesTransferred: Windows.Win32.Foundation.ULARGE_INTEGER
COPYFILE2_MESSAGE_ACTION = Int32
COPYFILE2_PROGRESS_CONTINUE: COPYFILE2_MESSAGE_ACTION = 0
COPYFILE2_PROGRESS_CANCEL: COPYFILE2_MESSAGE_ACTION = 1
COPYFILE2_PROGRESS_STOP: COPYFILE2_MESSAGE_ACTION = 2
COPYFILE2_PROGRESS_QUIET: COPYFILE2_MESSAGE_ACTION = 3
COPYFILE2_PROGRESS_PAUSE: COPYFILE2_MESSAGE_ACTION = 4
COPYFILE2_MESSAGE_TYPE = Int32
COPYFILE2_CALLBACK_NONE: COPYFILE2_MESSAGE_TYPE = 0
COPYFILE2_CALLBACK_CHUNK_STARTED: COPYFILE2_MESSAGE_TYPE = 1
COPYFILE2_CALLBACK_CHUNK_FINISHED: COPYFILE2_MESSAGE_TYPE = 2
COPYFILE2_CALLBACK_STREAM_STARTED: COPYFILE2_MESSAGE_TYPE = 3
COPYFILE2_CALLBACK_STREAM_FINISHED: COPYFILE2_MESSAGE_TYPE = 4
COPYFILE2_CALLBACK_POLL_CONTINUE: COPYFILE2_MESSAGE_TYPE = 5
COPYFILE2_CALLBACK_ERROR: COPYFILE2_MESSAGE_TYPE = 6
COPYFILE2_CALLBACK_MAX: COPYFILE2_MESSAGE_TYPE = 7
class CREATEFILE2_EXTENDED_PARAMETERS(Structure):
    dwSize: UInt32
    dwFileAttributes: UInt32
    dwFileFlags: UInt32
    dwSecurityQosFlags: UInt32
    lpSecurityAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head)
    hTemplateFile: Windows.Win32.Foundation.HANDLE
CREATE_TAPE_PARTITION_METHOD = Int32
TAPE_FIXED_PARTITIONS: CREATE_TAPE_PARTITION_METHOD = 0
TAPE_INITIATOR_PARTITIONS: CREATE_TAPE_PARTITION_METHOD = 2
TAPE_SELECT_PARTITIONS: CREATE_TAPE_PARTITION_METHOD = 1
DEFINE_DOS_DEVICE_FLAGS = UInt32
DDD_RAW_TARGET_PATH: DEFINE_DOS_DEVICE_FLAGS = 1
DDD_REMOVE_DEFINITION: DEFINE_DOS_DEVICE_FLAGS = 2
DDD_EXACT_MATCH_ON_REMOVE: DEFINE_DOS_DEVICE_FLAGS = 4
DDD_NO_BROADCAST_SYSTEM: DEFINE_DOS_DEVICE_FLAGS = 8
DDD_LUID_BROADCAST_DRIVE: DEFINE_DOS_DEVICE_FLAGS = 16
DISKQUOTA_USERNAME_RESOLVE = UInt32
DISKQUOTA_USERNAME_RESOLVE_ASYNC: DISKQUOTA_USERNAME_RESOLVE = 2
DISKQUOTA_USERNAME_RESOLVE_NONE: DISKQUOTA_USERNAME_RESOLVE = 0
DISKQUOTA_USERNAME_RESOLVE_SYNC: DISKQUOTA_USERNAME_RESOLVE = 1
class DISKQUOTA_USER_INFORMATION(Structure):
    QuotaUsed: Int64
    QuotaThreshold: Int64
    QuotaLimit: Int64
class DISK_SPACE_INFORMATION(Structure):
    ActualTotalAllocationUnits: UInt64
    ActualAvailableAllocationUnits: UInt64
    ActualPoolUnavailableAllocationUnits: UInt64
    CallerTotalAllocationUnits: UInt64
    CallerAvailableAllocationUnits: UInt64
    CallerPoolUnavailableAllocationUnits: UInt64
    UsedAllocationUnits: UInt64
    TotalReservedAllocationUnits: UInt64
    VolumeStorageReserveAllocationUnits: UInt64
    AvailableCommittedAllocationUnits: UInt64
    PoolAvailableAllocationUnits: UInt64
    SectorsPerAllocationUnit: UInt32
    BytesPerSector: UInt32
class EFS_CERTIFICATE_BLOB(Structure):
    dwCertEncodingType: UInt32
    cbData: UInt32
    pbData: c_char_p_no
class EFS_COMPATIBILITY_INFO(Structure):
    EfsVersion: UInt32
class EFS_DECRYPTION_STATUS_INFO(Structure):
    dwDecryptionError: UInt32
    dwHashOffset: UInt32
    cbHash: UInt32
class EFS_ENCRYPTION_STATUS_INFO(Structure):
    bHasCurrentKey: Windows.Win32.Foundation.BOOL
    dwEncryptionError: UInt32
class EFS_HASH_BLOB(Structure):
    cbData: UInt32
    pbData: c_char_p_no
class EFS_KEY_INFO(Structure):
    dwVersion: UInt32
    Entropy: UInt32
    Algorithm: UInt32
    KeyLength: UInt32
class EFS_PIN_BLOB(Structure):
    cbPadding: UInt32
    cbData: UInt32
    pbData: c_char_p_no
class EFS_RPC_BLOB(Structure):
    cbData: UInt32
    pbData: c_char_p_no
class EFS_VERSION_INFO(Structure):
    EfsVersion: UInt32
    SubVersion: UInt32
class ENCRYPTED_FILE_METADATA_SIGNATURE(Structure):
    dwEfsAccessType: UInt32
    pCertificatesAdded: POINTER(Windows.Win32.Storage.FileSystem.ENCRYPTION_CERTIFICATE_HASH_LIST_head)
    pEncryptionCertificate: POINTER(Windows.Win32.Storage.FileSystem.ENCRYPTION_CERTIFICATE_head)
    pEfsStreamSignature: POINTER(Windows.Win32.Storage.FileSystem.EFS_RPC_BLOB_head)
class ENCRYPTION_CERTIFICATE(Structure):
    cbTotalLength: UInt32
    pUserSid: POINTER(Windows.Win32.Security.SID_head)
    pCertBlob: POINTER(Windows.Win32.Storage.FileSystem.EFS_CERTIFICATE_BLOB_head)
class ENCRYPTION_CERTIFICATE_HASH(Structure):
    cbTotalLength: UInt32
    pUserSid: POINTER(Windows.Win32.Security.SID_head)
    pHash: POINTER(Windows.Win32.Storage.FileSystem.EFS_HASH_BLOB_head)
    lpDisplayInformation: Windows.Win32.Foundation.PWSTR
class ENCRYPTION_CERTIFICATE_HASH_LIST(Structure):
    nCert_Hash: UInt32
    pUsers: POINTER(POINTER(Windows.Win32.Storage.FileSystem.ENCRYPTION_CERTIFICATE_HASH_head))
class ENCRYPTION_CERTIFICATE_LIST(Structure):
    nUsers: UInt32
    pUsers: POINTER(POINTER(Windows.Win32.Storage.FileSystem.ENCRYPTION_CERTIFICATE_head))
class ENCRYPTION_PROTECTOR(Structure):
    cbTotalLength: UInt32
    pUserSid: POINTER(Windows.Win32.Security.SID_head)
    lpProtectorDescriptor: Windows.Win32.Foundation.PWSTR
class ENCRYPTION_PROTECTOR_LIST(Structure):
    nProtectors: UInt32
    pProtectors: POINTER(POINTER(Windows.Win32.Storage.FileSystem.ENCRYPTION_PROTECTOR_head))
ERASE_TAPE_TYPE = Int32
TAPE_ERASE_LONG: ERASE_TAPE_TYPE = 1
TAPE_ERASE_SHORT: ERASE_TAPE_TYPE = 0
@winfunctype_pointer
def FCACHE_CREATE_CALLBACK(lpstrName: Windows.Win32.Foundation.PSTR, lpvData: c_void_p, cbFileSize: POINTER(UInt32), cbFileSizeHigh: POINTER(UInt32)) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype_pointer
def FCACHE_RICHCREATE_CALLBACK(lpstrName: Windows.Win32.Foundation.PSTR, lpvData: c_void_p, cbFileSize: POINTER(UInt32), cbFileSizeHigh: POINTER(UInt32), pfDidWeScanIt: POINTER(Windows.Win32.Foundation.BOOL), pfIsStuffed: POINTER(Windows.Win32.Foundation.BOOL), pfStoredWithDots: POINTER(Windows.Win32.Foundation.BOOL), pfStoredWithTerminatingDot: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HANDLE: ...
class FH_OVERLAPPED(Structure):
    Internal: UIntPtr
    InternalHigh: UIntPtr
    Offset: UInt32
    OffsetHigh: UInt32
    hEvent: Windows.Win32.Foundation.HANDLE
    pfnCompletion: Windows.Win32.Storage.FileSystem.PFN_IO_COMPLETION
    Reserved1: UIntPtr
    Reserved2: UIntPtr
    Reserved3: UIntPtr
    Reserved4: UIntPtr
FILE_ACCESS_FLAGS = UInt32
FILE_READ_DATA: FILE_ACCESS_FLAGS = 1
FILE_LIST_DIRECTORY: FILE_ACCESS_FLAGS = 1
FILE_WRITE_DATA: FILE_ACCESS_FLAGS = 2
FILE_ADD_FILE: FILE_ACCESS_FLAGS = 2
FILE_APPEND_DATA: FILE_ACCESS_FLAGS = 4
FILE_ADD_SUBDIRECTORY: FILE_ACCESS_FLAGS = 4
FILE_CREATE_PIPE_INSTANCE: FILE_ACCESS_FLAGS = 4
FILE_READ_EA: FILE_ACCESS_FLAGS = 8
FILE_WRITE_EA: FILE_ACCESS_FLAGS = 16
FILE_EXECUTE: FILE_ACCESS_FLAGS = 32
FILE_TRAVERSE: FILE_ACCESS_FLAGS = 32
FILE_DELETE_CHILD: FILE_ACCESS_FLAGS = 64
FILE_READ_ATTRIBUTES: FILE_ACCESS_FLAGS = 128
FILE_WRITE_ATTRIBUTES: FILE_ACCESS_FLAGS = 256
DELETE: FILE_ACCESS_FLAGS = 65536
READ_CONTROL: FILE_ACCESS_FLAGS = 131072
WRITE_DAC: FILE_ACCESS_FLAGS = 262144
WRITE_OWNER: FILE_ACCESS_FLAGS = 524288
SYNCHRONIZE: FILE_ACCESS_FLAGS = 1048576
STANDARD_RIGHTS_REQUIRED: FILE_ACCESS_FLAGS = 983040
STANDARD_RIGHTS_READ: FILE_ACCESS_FLAGS = 131072
STANDARD_RIGHTS_WRITE: FILE_ACCESS_FLAGS = 131072
STANDARD_RIGHTS_EXECUTE: FILE_ACCESS_FLAGS = 131072
STANDARD_RIGHTS_ALL: FILE_ACCESS_FLAGS = 2031616
SPECIFIC_RIGHTS_ALL: FILE_ACCESS_FLAGS = 65535
FILE_ALL_ACCESS: FILE_ACCESS_FLAGS = 2032127
FILE_GENERIC_READ: FILE_ACCESS_FLAGS = 1179785
FILE_GENERIC_WRITE: FILE_ACCESS_FLAGS = 1179926
FILE_GENERIC_EXECUTE: FILE_ACCESS_FLAGS = 1179808
FILE_ACTION = UInt32
FILE_ACTION_ADDED: FILE_ACTION = 1
FILE_ACTION_REMOVED: FILE_ACTION = 2
FILE_ACTION_MODIFIED: FILE_ACTION = 3
FILE_ACTION_RENAMED_OLD_NAME: FILE_ACTION = 4
FILE_ACTION_RENAMED_NEW_NAME: FILE_ACTION = 5
class FILE_ALIGNMENT_INFO(Structure):
    AlignmentRequirement: UInt32
class FILE_ALLOCATION_INFO(Structure):
    AllocationSize: Windows.Win32.Foundation.LARGE_INTEGER
class FILE_ATTRIBUTE_TAG_INFO(Structure):
    FileAttributes: UInt32
    ReparseTag: UInt32
class FILE_BASIC_INFO(Structure):
    CreationTime: Windows.Win32.Foundation.LARGE_INTEGER
    LastAccessTime: Windows.Win32.Foundation.LARGE_INTEGER
    LastWriteTime: Windows.Win32.Foundation.LARGE_INTEGER
    ChangeTime: Windows.Win32.Foundation.LARGE_INTEGER
    FileAttributes: UInt32
class FILE_COMPRESSION_INFO(Structure):
    CompressedFileSize: Windows.Win32.Foundation.LARGE_INTEGER
    CompressionFormat: Windows.Win32.Storage.FileSystem.COMPRESSION_FORMAT
    CompressionUnitShift: Byte
    ChunkShift: Byte
    ClusterShift: Byte
    Reserved: Byte * 3
FILE_CREATION_DISPOSITION = UInt32
CREATE_NEW: FILE_CREATION_DISPOSITION = 1
CREATE_ALWAYS: FILE_CREATION_DISPOSITION = 2
OPEN_EXISTING: FILE_CREATION_DISPOSITION = 3
OPEN_ALWAYS: FILE_CREATION_DISPOSITION = 4
TRUNCATE_EXISTING: FILE_CREATION_DISPOSITION = 5
FILE_DEVICE_TYPE = UInt32
FILE_DEVICE_CD_ROM: FILE_DEVICE_TYPE = 2
FILE_DEVICE_DISK: FILE_DEVICE_TYPE = 7
FILE_DEVICE_TAPE: FILE_DEVICE_TYPE = 31
FILE_DEVICE_DVD: FILE_DEVICE_TYPE = 51
class FILE_DISPOSITION_INFO(Structure):
    DeleteFile: Windows.Win32.Foundation.BOOLEAN
class FILE_END_OF_FILE_INFO(Structure):
    EndOfFile: Windows.Win32.Foundation.LARGE_INTEGER
class FILE_EXTENT(Structure):
    VolumeOffset: UInt64
    ExtentLength: UInt64
FILE_FLAGS_AND_ATTRIBUTES = UInt32
FILE_ATTRIBUTE_READONLY: FILE_FLAGS_AND_ATTRIBUTES = 1
FILE_ATTRIBUTE_HIDDEN: FILE_FLAGS_AND_ATTRIBUTES = 2
FILE_ATTRIBUTE_SYSTEM: FILE_FLAGS_AND_ATTRIBUTES = 4
FILE_ATTRIBUTE_DIRECTORY: FILE_FLAGS_AND_ATTRIBUTES = 16
FILE_ATTRIBUTE_ARCHIVE: FILE_FLAGS_AND_ATTRIBUTES = 32
FILE_ATTRIBUTE_DEVICE: FILE_FLAGS_AND_ATTRIBUTES = 64
FILE_ATTRIBUTE_NORMAL: FILE_FLAGS_AND_ATTRIBUTES = 128
FILE_ATTRIBUTE_TEMPORARY: FILE_FLAGS_AND_ATTRIBUTES = 256
FILE_ATTRIBUTE_SPARSE_FILE: FILE_FLAGS_AND_ATTRIBUTES = 512
FILE_ATTRIBUTE_REPARSE_POINT: FILE_FLAGS_AND_ATTRIBUTES = 1024
FILE_ATTRIBUTE_COMPRESSED: FILE_FLAGS_AND_ATTRIBUTES = 2048
FILE_ATTRIBUTE_OFFLINE: FILE_FLAGS_AND_ATTRIBUTES = 4096
FILE_ATTRIBUTE_NOT_CONTENT_INDEXED: FILE_FLAGS_AND_ATTRIBUTES = 8192
FILE_ATTRIBUTE_ENCRYPTED: FILE_FLAGS_AND_ATTRIBUTES = 16384
FILE_ATTRIBUTE_INTEGRITY_STREAM: FILE_FLAGS_AND_ATTRIBUTES = 32768
FILE_ATTRIBUTE_VIRTUAL: FILE_FLAGS_AND_ATTRIBUTES = 65536
FILE_ATTRIBUTE_NO_SCRUB_DATA: FILE_FLAGS_AND_ATTRIBUTES = 131072
FILE_ATTRIBUTE_EA: FILE_FLAGS_AND_ATTRIBUTES = 262144
FILE_ATTRIBUTE_PINNED: FILE_FLAGS_AND_ATTRIBUTES = 524288
FILE_ATTRIBUTE_UNPINNED: FILE_FLAGS_AND_ATTRIBUTES = 1048576
FILE_ATTRIBUTE_RECALL_ON_OPEN: FILE_FLAGS_AND_ATTRIBUTES = 262144
FILE_ATTRIBUTE_RECALL_ON_DATA_ACCESS: FILE_FLAGS_AND_ATTRIBUTES = 4194304
FILE_FLAG_WRITE_THROUGH: FILE_FLAGS_AND_ATTRIBUTES = 2147483648
FILE_FLAG_OVERLAPPED: FILE_FLAGS_AND_ATTRIBUTES = 1073741824
FILE_FLAG_NO_BUFFERING: FILE_FLAGS_AND_ATTRIBUTES = 536870912
FILE_FLAG_RANDOM_ACCESS: FILE_FLAGS_AND_ATTRIBUTES = 268435456
FILE_FLAG_SEQUENTIAL_SCAN: FILE_FLAGS_AND_ATTRIBUTES = 134217728
FILE_FLAG_DELETE_ON_CLOSE: FILE_FLAGS_AND_ATTRIBUTES = 67108864
FILE_FLAG_BACKUP_SEMANTICS: FILE_FLAGS_AND_ATTRIBUTES = 33554432
FILE_FLAG_POSIX_SEMANTICS: FILE_FLAGS_AND_ATTRIBUTES = 16777216
FILE_FLAG_SESSION_AWARE: FILE_FLAGS_AND_ATTRIBUTES = 8388608
FILE_FLAG_OPEN_REPARSE_POINT: FILE_FLAGS_AND_ATTRIBUTES = 2097152
FILE_FLAG_OPEN_NO_RECALL: FILE_FLAGS_AND_ATTRIBUTES = 1048576
FILE_FLAG_FIRST_PIPE_INSTANCE: FILE_FLAGS_AND_ATTRIBUTES = 524288
PIPE_ACCESS_DUPLEX: FILE_FLAGS_AND_ATTRIBUTES = 3
PIPE_ACCESS_INBOUND: FILE_FLAGS_AND_ATTRIBUTES = 1
PIPE_ACCESS_OUTBOUND: FILE_FLAGS_AND_ATTRIBUTES = 2
SECURITY_ANONYMOUS: FILE_FLAGS_AND_ATTRIBUTES = 0
SECURITY_IDENTIFICATION: FILE_FLAGS_AND_ATTRIBUTES = 65536
SECURITY_IMPERSONATION: FILE_FLAGS_AND_ATTRIBUTES = 131072
SECURITY_DELEGATION: FILE_FLAGS_AND_ATTRIBUTES = 196608
SECURITY_CONTEXT_TRACKING: FILE_FLAGS_AND_ATTRIBUTES = 262144
SECURITY_EFFECTIVE_ONLY: FILE_FLAGS_AND_ATTRIBUTES = 524288
SECURITY_SQOS_PRESENT: FILE_FLAGS_AND_ATTRIBUTES = 1048576
SECURITY_VALID_SQOS_FLAGS: FILE_FLAGS_AND_ATTRIBUTES = 2031616
class FILE_FULL_DIR_INFO(Structure):
    NextEntryOffset: UInt32
    FileIndex: UInt32
    CreationTime: Windows.Win32.Foundation.LARGE_INTEGER
    LastAccessTime: Windows.Win32.Foundation.LARGE_INTEGER
    LastWriteTime: Windows.Win32.Foundation.LARGE_INTEGER
    ChangeTime: Windows.Win32.Foundation.LARGE_INTEGER
    EndOfFile: Windows.Win32.Foundation.LARGE_INTEGER
    AllocationSize: Windows.Win32.Foundation.LARGE_INTEGER
    FileAttributes: UInt32
    FileNameLength: UInt32
    EaSize: UInt32
    FileName: Char * 1
class FILE_ID_128(Structure):
    Identifier: Byte * 16
class FILE_ID_BOTH_DIR_INFO(Structure):
    NextEntryOffset: UInt32
    FileIndex: UInt32
    CreationTime: Windows.Win32.Foundation.LARGE_INTEGER
    LastAccessTime: Windows.Win32.Foundation.LARGE_INTEGER
    LastWriteTime: Windows.Win32.Foundation.LARGE_INTEGER
    ChangeTime: Windows.Win32.Foundation.LARGE_INTEGER
    EndOfFile: Windows.Win32.Foundation.LARGE_INTEGER
    AllocationSize: Windows.Win32.Foundation.LARGE_INTEGER
    FileAttributes: UInt32
    FileNameLength: UInt32
    EaSize: UInt32
    ShortNameLength: SByte
    ShortName: Char * 12
    FileId: Windows.Win32.Foundation.LARGE_INTEGER
    FileName: Char * 1
class FILE_ID_DESCRIPTOR(Structure):
    dwSize: UInt32
    Type: Windows.Win32.Storage.FileSystem.FILE_ID_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        FileId: Windows.Win32.Foundation.LARGE_INTEGER
        ObjectId: Guid
        ExtendedFileId: Windows.Win32.Storage.FileSystem.FILE_ID_128
class FILE_ID_EXTD_DIR_INFO(Structure):
    NextEntryOffset: UInt32
    FileIndex: UInt32
    CreationTime: Windows.Win32.Foundation.LARGE_INTEGER
    LastAccessTime: Windows.Win32.Foundation.LARGE_INTEGER
    LastWriteTime: Windows.Win32.Foundation.LARGE_INTEGER
    ChangeTime: Windows.Win32.Foundation.LARGE_INTEGER
    EndOfFile: Windows.Win32.Foundation.LARGE_INTEGER
    AllocationSize: Windows.Win32.Foundation.LARGE_INTEGER
    FileAttributes: UInt32
    FileNameLength: UInt32
    EaSize: UInt32
    ReparsePointTag: UInt32
    FileId: Windows.Win32.Storage.FileSystem.FILE_ID_128
    FileName: Char * 1
class FILE_ID_INFO(Structure):
    VolumeSerialNumber: UInt64
    FileId: Windows.Win32.Storage.FileSystem.FILE_ID_128
FILE_ID_TYPE = Int32
FILE_ID_TYPE_FileIdType: FILE_ID_TYPE = 0
FILE_ID_TYPE_ObjectIdType: FILE_ID_TYPE = 1
FILE_ID_TYPE_ExtendedFileIdType: FILE_ID_TYPE = 2
FILE_ID_TYPE_MaximumFileIdType: FILE_ID_TYPE = 3
class FILE_INFO_2(Structure):
    fi2_id: UInt32
class FILE_INFO_3(Structure):
    fi3_id: UInt32
    fi3_permissions: Windows.Win32.Storage.FileSystem.FILE_INFO_FLAGS_PERMISSIONS
    fi3_num_locks: UInt32
    fi3_pathname: Windows.Win32.Foundation.PWSTR
    fi3_username: Windows.Win32.Foundation.PWSTR
FILE_INFO_BY_HANDLE_CLASS = Int32
FILE_INFO_BY_HANDLE_CLASS_FileBasicInfo: FILE_INFO_BY_HANDLE_CLASS = 0
FILE_INFO_BY_HANDLE_CLASS_FileStandardInfo: FILE_INFO_BY_HANDLE_CLASS = 1
FILE_INFO_BY_HANDLE_CLASS_FileNameInfo: FILE_INFO_BY_HANDLE_CLASS = 2
FILE_INFO_BY_HANDLE_CLASS_FileRenameInfo: FILE_INFO_BY_HANDLE_CLASS = 3
FILE_INFO_BY_HANDLE_CLASS_FileDispositionInfo: FILE_INFO_BY_HANDLE_CLASS = 4
FILE_INFO_BY_HANDLE_CLASS_FileAllocationInfo: FILE_INFO_BY_HANDLE_CLASS = 5
FILE_INFO_BY_HANDLE_CLASS_FileEndOfFileInfo: FILE_INFO_BY_HANDLE_CLASS = 6
FILE_INFO_BY_HANDLE_CLASS_FileStreamInfo: FILE_INFO_BY_HANDLE_CLASS = 7
FILE_INFO_BY_HANDLE_CLASS_FileCompressionInfo: FILE_INFO_BY_HANDLE_CLASS = 8
FILE_INFO_BY_HANDLE_CLASS_FileAttributeTagInfo: FILE_INFO_BY_HANDLE_CLASS = 9
FILE_INFO_BY_HANDLE_CLASS_FileIdBothDirectoryInfo: FILE_INFO_BY_HANDLE_CLASS = 10
FILE_INFO_BY_HANDLE_CLASS_FileIdBothDirectoryRestartInfo: FILE_INFO_BY_HANDLE_CLASS = 11
FILE_INFO_BY_HANDLE_CLASS_FileIoPriorityHintInfo: FILE_INFO_BY_HANDLE_CLASS = 12
FILE_INFO_BY_HANDLE_CLASS_FileRemoteProtocolInfo: FILE_INFO_BY_HANDLE_CLASS = 13
FILE_INFO_BY_HANDLE_CLASS_FileFullDirectoryInfo: FILE_INFO_BY_HANDLE_CLASS = 14
FILE_INFO_BY_HANDLE_CLASS_FileFullDirectoryRestartInfo: FILE_INFO_BY_HANDLE_CLASS = 15
FILE_INFO_BY_HANDLE_CLASS_FileStorageInfo: FILE_INFO_BY_HANDLE_CLASS = 16
FILE_INFO_BY_HANDLE_CLASS_FileAlignmentInfo: FILE_INFO_BY_HANDLE_CLASS = 17
FILE_INFO_BY_HANDLE_CLASS_FileIdInfo: FILE_INFO_BY_HANDLE_CLASS = 18
FILE_INFO_BY_HANDLE_CLASS_FileIdExtdDirectoryInfo: FILE_INFO_BY_HANDLE_CLASS = 19
FILE_INFO_BY_HANDLE_CLASS_FileIdExtdDirectoryRestartInfo: FILE_INFO_BY_HANDLE_CLASS = 20
FILE_INFO_BY_HANDLE_CLASS_FileDispositionInfoEx: FILE_INFO_BY_HANDLE_CLASS = 21
FILE_INFO_BY_HANDLE_CLASS_FileRenameInfoEx: FILE_INFO_BY_HANDLE_CLASS = 22
FILE_INFO_BY_HANDLE_CLASS_FileCaseSensitiveInfo: FILE_INFO_BY_HANDLE_CLASS = 23
FILE_INFO_BY_HANDLE_CLASS_FileNormalizedNameInfo: FILE_INFO_BY_HANDLE_CLASS = 24
FILE_INFO_BY_HANDLE_CLASS_MaximumFileInfoByHandleClass: FILE_INFO_BY_HANDLE_CLASS = 25
FILE_INFO_FLAGS_PERMISSIONS = UInt32
PERM_FILE_READ: FILE_INFO_FLAGS_PERMISSIONS = 1
PERM_FILE_WRITE: FILE_INFO_FLAGS_PERMISSIONS = 2
PERM_FILE_CREATE: FILE_INFO_FLAGS_PERMISSIONS = 4
class FILE_IO_PRIORITY_HINT_INFO(Structure):
    PriorityHint: Windows.Win32.Storage.FileSystem.PRIORITY_HINT
FILE_NAME = UInt32
FILE_NAME_NORMALIZED: FILE_NAME = 0
FILE_NAME_OPENED: FILE_NAME = 8
class FILE_NAME_INFO(Structure):
    FileNameLength: UInt32
    FileName: Char * 1
FILE_NOTIFY_CHANGE = UInt32
FILE_NOTIFY_CHANGE_FILE_NAME: FILE_NOTIFY_CHANGE = 1
FILE_NOTIFY_CHANGE_DIR_NAME: FILE_NOTIFY_CHANGE = 2
FILE_NOTIFY_CHANGE_ATTRIBUTES: FILE_NOTIFY_CHANGE = 4
FILE_NOTIFY_CHANGE_SIZE: FILE_NOTIFY_CHANGE = 8
FILE_NOTIFY_CHANGE_LAST_WRITE: FILE_NOTIFY_CHANGE = 16
FILE_NOTIFY_CHANGE_LAST_ACCESS: FILE_NOTIFY_CHANGE = 32
FILE_NOTIFY_CHANGE_CREATION: FILE_NOTIFY_CHANGE = 64
FILE_NOTIFY_CHANGE_SECURITY: FILE_NOTIFY_CHANGE = 256
class FILE_NOTIFY_EXTENDED_INFORMATION(Structure):
    NextEntryOffset: UInt32
    Action: Windows.Win32.Storage.FileSystem.FILE_ACTION
    CreationTime: Windows.Win32.Foundation.LARGE_INTEGER
    LastModificationTime: Windows.Win32.Foundation.LARGE_INTEGER
    LastChangeTime: Windows.Win32.Foundation.LARGE_INTEGER
    LastAccessTime: Windows.Win32.Foundation.LARGE_INTEGER
    AllocatedLength: Windows.Win32.Foundation.LARGE_INTEGER
    FileSize: Windows.Win32.Foundation.LARGE_INTEGER
    FileAttributes: UInt32
    ReparsePointTag: UInt32
    FileId: Windows.Win32.Foundation.LARGE_INTEGER
    ParentFileId: Windows.Win32.Foundation.LARGE_INTEGER
    FileNameLength: UInt32
    FileName: Char * 1
class FILE_NOTIFY_INFORMATION(Structure):
    NextEntryOffset: UInt32
    Action: Windows.Win32.Storage.FileSystem.FILE_ACTION
    FileNameLength: UInt32
    FileName: Char * 1
class FILE_REMOTE_PROTOCOL_INFO(Structure):
    StructureVersion: UInt16
    StructureSize: UInt16
    Protocol: UInt32
    ProtocolMajorVersion: UInt16
    ProtocolMinorVersion: UInt16
    ProtocolRevision: UInt16
    Reserved: UInt16
    Flags: UInt32
    GenericReserved: _GenericReserved_e__Struct
    ProtocolSpecific: _ProtocolSpecific_e__Union
    class _GenericReserved_e__Struct(Structure):
        Reserved: UInt32 * 8
    class _ProtocolSpecific_e__Union(Union):
        Smb2: _Smb2_e__Struct
        Reserved: UInt32 * 16
        class _Smb2_e__Struct(Structure):
            Server: _Server_e__Struct
            Share: _Share_e__Struct
            class _Server_e__Struct(Structure):
                Capabilities: UInt32
            class _Share_e__Struct(Structure):
                Capabilities: UInt32
                CachingFlags: UInt32
class FILE_RENAME_INFO(Structure):
    Anonymous: _Anonymous_e__Union
    RootDirectory: Windows.Win32.Foundation.HANDLE
    FileNameLength: UInt32
    FileName: Char * 1
    class _Anonymous_e__Union(Union):
        ReplaceIfExists: Windows.Win32.Foundation.BOOLEAN
        Flags: UInt32
class FILE_SEGMENT_ELEMENT(Union):
    Buffer: c_void_p
    Alignment: UInt64
FILE_SHARE_MODE = UInt32
FILE_SHARE_NONE: FILE_SHARE_MODE = 0
FILE_SHARE_DELETE: FILE_SHARE_MODE = 4
FILE_SHARE_READ: FILE_SHARE_MODE = 1
FILE_SHARE_WRITE: FILE_SHARE_MODE = 2
class FILE_STANDARD_INFO(Structure):
    AllocationSize: Windows.Win32.Foundation.LARGE_INTEGER
    EndOfFile: Windows.Win32.Foundation.LARGE_INTEGER
    NumberOfLinks: UInt32
    DeletePending: Windows.Win32.Foundation.BOOLEAN
    Directory: Windows.Win32.Foundation.BOOLEAN
class FILE_STORAGE_INFO(Structure):
    LogicalBytesPerSector: UInt32
    PhysicalBytesPerSectorForAtomicity: UInt32
    PhysicalBytesPerSectorForPerformance: UInt32
    FileSystemEffectivePhysicalBytesPerSectorForAtomicity: UInt32
    Flags: UInt32
    ByteOffsetForSectorAlignment: UInt32
    ByteOffsetForPartitionAlignment: UInt32
class FILE_STREAM_INFO(Structure):
    NextEntryOffset: UInt32
    StreamNameLength: UInt32
    StreamSize: Windows.Win32.Foundation.LARGE_INTEGER
    StreamAllocationSize: Windows.Win32.Foundation.LARGE_INTEGER
    StreamName: Char * 1
FILE_TYPE = UInt32
FILE_TYPE_UNKNOWN: FILE_TYPE = 0
FILE_TYPE_DISK: FILE_TYPE = 1
FILE_TYPE_CHAR: FILE_TYPE = 2
FILE_TYPE_PIPE: FILE_TYPE = 3
FILE_TYPE_REMOTE: FILE_TYPE = 32768
FINDEX_INFO_LEVELS = Int32
FINDEX_INFO_LEVELS_FindExInfoStandard: FINDEX_INFO_LEVELS = 0
FINDEX_INFO_LEVELS_FindExInfoBasic: FINDEX_INFO_LEVELS = 1
FINDEX_INFO_LEVELS_FindExInfoMaxInfoLevel: FINDEX_INFO_LEVELS = 2
FINDEX_SEARCH_OPS = Int32
FINDEX_SEARCH_OPS_FindExSearchNameMatch: FINDEX_SEARCH_OPS = 0
FINDEX_SEARCH_OPS_FindExSearchLimitToDirectories: FINDEX_SEARCH_OPS = 1
FINDEX_SEARCH_OPS_FindExSearchLimitToDevices: FINDEX_SEARCH_OPS = 2
FINDEX_SEARCH_OPS_FindExSearchMaxSearchOp: FINDEX_SEARCH_OPS = 3
FIND_FIRST_EX_FLAGS = UInt32
FIND_FIRST_EX_CASE_SENSITIVE: FIND_FIRST_EX_FLAGS = 1
FIND_FIRST_EX_LARGE_FETCH: FIND_FIRST_EX_FLAGS = 2
FIND_FIRST_EX_ON_DISK_ENTRIES_ONLY: FIND_FIRST_EX_FLAGS = 4
class FIO_CONTEXT(Structure):
    m_dwTempHack: UInt32
    m_dwSignature: UInt32
    m_hFile: Windows.Win32.Foundation.HANDLE
    m_dwLinesOffset: UInt32
    m_dwHeaderLength: UInt32
FindChangeNotificationHandle = IntPtr
FindFileHandle = IntPtr
FindFileNameHandle = IntPtr
FindStreamHandle = IntPtr
FindVolumeHandle = IntPtr
FindVolumeMointPointHandle = IntPtr
GET_FILEEX_INFO_LEVELS = Int32
GET_FILEEX_INFO_LEVELS_GetFileExInfoStandard: GET_FILEEX_INFO_LEVELS = 0
GET_FILEEX_INFO_LEVELS_GetFileExMaxInfoLevel: GET_FILEEX_INFO_LEVELS = 1
GET_FILE_VERSION_INFO_FLAGS = UInt32
FILE_VER_GET_LOCALISED: GET_FILE_VERSION_INFO_FLAGS = 1
FILE_VER_GET_NEUTRAL: GET_FILE_VERSION_INFO_FLAGS = 2
FILE_VER_GET_PREFETCHED: GET_FILE_VERSION_INFO_FLAGS = 4
GET_TAPE_DRIVE_PARAMETERS_OPERATION = UInt32
GET_TAPE_DRIVE_INFORMATION: GET_TAPE_DRIVE_PARAMETERS_OPERATION = 1
GET_TAPE_MEDIA_INFORMATION: GET_TAPE_DRIVE_PARAMETERS_OPERATION = 0
class HIORING__(Structure):
    unused: Int32
class IDiskQuotaControl(c_void_p):
    extends: Windows.Win32.System.Com.IConnectionPointContainer
    Guid = Guid('7988b572-ec89-11cf-9c-00-00-aa-00-a1-4f-56')
    @commethod(5)
    def Initialize(pszPath: Windows.Win32.Foundation.PWSTR, bReadWrite: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetQuotaState(dwState: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetQuotaState(pdwState: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetQuotaLogFlags(dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetQuotaLogFlags(pdwFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetDefaultQuotaThreshold(llThreshold: Int64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetDefaultQuotaThreshold(pllThreshold: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetDefaultQuotaThresholdText(pszText: Windows.Win32.Foundation.PWSTR, cchText: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetDefaultQuotaLimit(llLimit: Int64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetDefaultQuotaLimit(pllLimit: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetDefaultQuotaLimitText(pszText: Windows.Win32.Foundation.PWSTR, cchText: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def AddUserSid(pUserSid: Windows.Win32.Foundation.PSID, fNameResolution: Windows.Win32.Storage.FileSystem.DISKQUOTA_USERNAME_RESOLVE, ppUser: POINTER(Windows.Win32.Storage.FileSystem.IDiskQuotaUser_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def AddUserName(pszLogonName: Windows.Win32.Foundation.PWSTR, fNameResolution: Windows.Win32.Storage.FileSystem.DISKQUOTA_USERNAME_RESOLVE, ppUser: POINTER(Windows.Win32.Storage.FileSystem.IDiskQuotaUser_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def DeleteUser(pUser: Windows.Win32.Storage.FileSystem.IDiskQuotaUser_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def FindUserSid(pUserSid: Windows.Win32.Foundation.PSID, fNameResolution: Windows.Win32.Storage.FileSystem.DISKQUOTA_USERNAME_RESOLVE, ppUser: POINTER(Windows.Win32.Storage.FileSystem.IDiskQuotaUser_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def FindUserName(pszLogonName: Windows.Win32.Foundation.PWSTR, ppUser: POINTER(Windows.Win32.Storage.FileSystem.IDiskQuotaUser_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def CreateEnumUsers(rgpUserSids: POINTER(Windows.Win32.Foundation.PSID), cpSids: UInt32, fNameResolution: Windows.Win32.Storage.FileSystem.DISKQUOTA_USERNAME_RESOLVE, ppEnum: POINTER(Windows.Win32.Storage.FileSystem.IEnumDiskQuotaUsers_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def CreateUserBatch(ppBatch: POINTER(Windows.Win32.Storage.FileSystem.IDiskQuotaUserBatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def InvalidateSidNameCache() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GiveUserNameResolutionPriority(pUser: Windows.Win32.Storage.FileSystem.IDiskQuotaUser_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def ShutdownNameResolution() -> Windows.Win32.Foundation.HRESULT: ...
class IDiskQuotaEvents(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('7988b579-ec89-11cf-9c-00-00-aa-00-a1-4f-56')
    @commethod(3)
    def OnUserNameChanged(pUser: Windows.Win32.Storage.FileSystem.IDiskQuotaUser_head) -> Windows.Win32.Foundation.HRESULT: ...
class IDiskQuotaUser(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('7988b574-ec89-11cf-9c-00-00-aa-00-a1-4f-56')
    @commethod(3)
    def GetID(pulID: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetName(pszAccountContainer: Windows.Win32.Foundation.PWSTR, cchAccountContainer: UInt32, pszLogonName: Windows.Win32.Foundation.PWSTR, cchLogonName: UInt32, pszDisplayName: Windows.Win32.Foundation.PWSTR, cchDisplayName: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSidLength(pdwLength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSid(pbSidBuffer: c_char_p_no, cbSidBuffer: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetQuotaThreshold(pllThreshold: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetQuotaThresholdText(pszText: Windows.Win32.Foundation.PWSTR, cchText: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetQuotaLimit(pllLimit: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetQuotaLimitText(pszText: Windows.Win32.Foundation.PWSTR, cchText: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetQuotaUsed(pllUsed: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetQuotaUsedText(pszText: Windows.Win32.Foundation.PWSTR, cchText: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetQuotaInformation(pbQuotaInfo: c_void_p, cbQuotaInfo: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetQuotaThreshold(llThreshold: Int64, fWriteThrough: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetQuotaLimit(llLimit: Int64, fWriteThrough: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Invalidate() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetAccountStatus(pdwStatus: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IDiskQuotaUserBatch(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('7988b576-ec89-11cf-9c-00-00-aa-00-a1-4f-56')
    @commethod(3)
    def Add(pUser: Windows.Win32.Storage.FileSystem.IDiskQuotaUser_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Remove(pUser: Windows.Win32.Storage.FileSystem.IDiskQuotaUser_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RemoveAll() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def FlushToDisk() -> Windows.Win32.Foundation.HRESULT: ...
class IEnumDiskQuotaUsers(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('7988b577-ec89-11cf-9c-00-00-aa-00-a1-4f-56')
    @commethod(3)
    def Next(cUsers: UInt32, rgUsers: POINTER(Windows.Win32.Storage.FileSystem.IDiskQuotaUser_head), pcUsersFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(cUsers: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppEnum: POINTER(Windows.Win32.Storage.FileSystem.IEnumDiskQuotaUsers_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IORING_BUFFER_INFO(Structure):
    Address: c_void_p
    Length: UInt32
class IORING_BUFFER_REF(Structure):
    Kind: Windows.Win32.Storage.FileSystem.IORING_REF_KIND
    Buffer: BufferUnion
    class BufferUnion(Union):
        Address: c_void_p
        IndexAndOffset: Windows.Win32.Storage.FileSystem.IORING_REGISTERED_BUFFER
class IORING_CAPABILITIES(Structure):
    MaxVersion: Windows.Win32.Storage.FileSystem.IORING_VERSION
    MaxSubmissionQueueSize: UInt32
    MaxCompletionQueueSize: UInt32
    FeatureFlags: Windows.Win32.Storage.FileSystem.IORING_FEATURE_FLAGS
class IORING_CQE(Structure):
    UserData: UIntPtr
    ResultCode: Windows.Win32.Foundation.HRESULT
    Information: UIntPtr
IORING_CREATE_ADVISORY_FLAGS = Int32
IORING_CREATE_ADVISORY_FLAGS_NONE: IORING_CREATE_ADVISORY_FLAGS = 0
class IORING_CREATE_FLAGS(Structure):
    Required: Windows.Win32.Storage.FileSystem.IORING_CREATE_REQUIRED_FLAGS
    Advisory: Windows.Win32.Storage.FileSystem.IORING_CREATE_ADVISORY_FLAGS
IORING_CREATE_REQUIRED_FLAGS = Int32
IORING_CREATE_REQUIRED_FLAGS_NONE: IORING_CREATE_REQUIRED_FLAGS = 0
IORING_FEATURE_FLAGS = Int32
IORING_FEATURE_FLAGS_NONE: IORING_FEATURE_FLAGS = 0
IORING_FEATURE_UM_EMULATION: IORING_FEATURE_FLAGS = 1
IORING_FEATURE_SET_COMPLETION_EVENT: IORING_FEATURE_FLAGS = 2
class IORING_HANDLE_REF(Structure):
    Kind: Windows.Win32.Storage.FileSystem.IORING_REF_KIND
    Handle: HandleUnion
    class HandleUnion(Union):
        Handle: Windows.Win32.Foundation.HANDLE
        Index: UInt32
class IORING_INFO(Structure):
    IoRingVersion: Windows.Win32.Storage.FileSystem.IORING_VERSION
    Flags: Windows.Win32.Storage.FileSystem.IORING_CREATE_FLAGS
    SubmissionQueueSize: UInt32
    CompletionQueueSize: UInt32
IORING_OP_CODE = Int32
IORING_OP_NOP: IORING_OP_CODE = 0
IORING_OP_READ: IORING_OP_CODE = 1
IORING_OP_REGISTER_FILES: IORING_OP_CODE = 2
IORING_OP_REGISTER_BUFFERS: IORING_OP_CODE = 3
IORING_OP_CANCEL: IORING_OP_CODE = 4
IORING_REF_KIND = Int32
IORING_REF_RAW: IORING_REF_KIND = 0
IORING_REF_REGISTERED: IORING_REF_KIND = 1
class IORING_REGISTERED_BUFFER(Structure):
    BufferIndex: UInt32
    Offset: UInt32
IORING_SQE_FLAGS = Int32
IOSQE_FLAGS_NONE: IORING_SQE_FLAGS = 0
IORING_VERSION = Int32
IORING_VERSION_INVALID: IORING_VERSION = 0
IORING_VERSION_1: IORING_VERSION = 1
class KCRM_MARSHAL_HEADER(Structure):
    VersionMajor: UInt32
    VersionMinor: UInt32
    NumProtocols: UInt32
    Unused: UInt32
class KCRM_PROTOCOL_BLOB(Structure):
    ProtocolId: Guid
    StaticInfoLength: UInt32
    TransactionIdInfoLength: UInt32
    Unused1: UInt32
    Unused2: UInt32
class KCRM_TRANSACTION_BLOB(Structure):
    UOW: Guid
    TmIdentity: Guid
    IsolationLevel: UInt32
    IsolationFlags: UInt32
    Timeout: UInt32
    Description: Char * 64
LOCK_FILE_FLAGS = UInt32
LOCKFILE_EXCLUSIVE_LOCK: LOCK_FILE_FLAGS = 2
LOCKFILE_FAIL_IMMEDIATELY: LOCK_FILE_FLAGS = 1
class LOG_MANAGEMENT_CALLBACKS(Structure):
    CallbackContext: c_void_p
    AdvanceTailCallback: Windows.Win32.Storage.FileSystem.PLOG_TAIL_ADVANCE_CALLBACK
    LogFullHandlerCallback: Windows.Win32.Storage.FileSystem.PLOG_FULL_HANDLER_CALLBACK
    LogUnpinnedCallback: Windows.Win32.Storage.FileSystem.PLOG_UNPINNED_CALLBACK
@winfunctype_pointer
def LPPROGRESS_ROUTINE(TotalFileSize: Windows.Win32.Foundation.LARGE_INTEGER, TotalBytesTransferred: Windows.Win32.Foundation.LARGE_INTEGER, StreamSize: Windows.Win32.Foundation.LARGE_INTEGER, StreamBytesTransferred: Windows.Win32.Foundation.LARGE_INTEGER, dwStreamNumber: UInt32, dwCallbackReason: Windows.Win32.Storage.FileSystem.LPPROGRESS_ROUTINE_CALLBACK_REASON, hSourceFile: Windows.Win32.Foundation.HANDLE, hDestinationFile: Windows.Win32.Foundation.HANDLE, lpData: c_void_p) -> UInt32: ...
LPPROGRESS_ROUTINE_CALLBACK_REASON = UInt32
CALLBACK_CHUNK_FINISHED: LPPROGRESS_ROUTINE_CALLBACK_REASON = 0
CALLBACK_STREAM_SWITCH: LPPROGRESS_ROUTINE_CALLBACK_REASON = 1
LZOPENFILE_STYLE = UInt16
OF_CANCEL: LZOPENFILE_STYLE = 2048
OF_CREATE: LZOPENFILE_STYLE = 4096
OF_DELETE: LZOPENFILE_STYLE = 512
OF_EXIST: LZOPENFILE_STYLE = 16384
OF_PARSE: LZOPENFILE_STYLE = 256
OF_PROMPT: LZOPENFILE_STYLE = 8192
OF_READ: LZOPENFILE_STYLE = 0
OF_READWRITE: LZOPENFILE_STYLE = 2
OF_REOPEN: LZOPENFILE_STYLE = 32768
OF_SHARE_DENY_NONE: LZOPENFILE_STYLE = 64
OF_SHARE_DENY_READ: LZOPENFILE_STYLE = 48
OF_SHARE_DENY_WRITE: LZOPENFILE_STYLE = 32
OF_SHARE_EXCLUSIVE: LZOPENFILE_STYLE = 16
OF_WRITE: LZOPENFILE_STYLE = 1
OF_SHARE_COMPAT: LZOPENFILE_STYLE = 0
OF_VERIFY: LZOPENFILE_STYLE = 1024
@winfunctype_pointer
def MAXMEDIALABEL(pMaxSize: POINTER(UInt32)) -> UInt32: ...
MOVE_FILE_FLAGS = UInt32
MOVEFILE_COPY_ALLOWED: MOVE_FILE_FLAGS = 2
MOVEFILE_CREATE_HARDLINK: MOVE_FILE_FLAGS = 16
MOVEFILE_DELAY_UNTIL_REBOOT: MOVE_FILE_FLAGS = 4
MOVEFILE_REPLACE_EXISTING: MOVE_FILE_FLAGS = 1
MOVEFILE_WRITE_THROUGH: MOVE_FILE_FLAGS = 8
MOVEFILE_FAIL_IF_NOT_TRACKABLE: MOVE_FILE_FLAGS = 32
class MediaLabelInfo(Structure):
    LabelType: Char * 64
    LabelIDSize: UInt32
    LabelID: Byte * 256
    LabelAppDescr: Char * 256
class NAME_CACHE_CONTEXT(Structure):
    m_dwSignature: UInt32
class NTMS_ALLOCATION_INFORMATION(Structure):
    dwSize: UInt32
    lpReserved: c_void_p
    AllocatedFrom: Guid
class NTMS_ASYNC_IO(Structure):
    OperationId: Guid
    EventId: Guid
    dwOperationType: UInt32
    dwResult: UInt32
    dwAsyncState: UInt32
    hEvent: Windows.Win32.Foundation.HANDLE
    bOnStateChange: Windows.Win32.Foundation.BOOL
class NTMS_CHANGERINFORMATIONA(Structure):
    Number: UInt32
    ChangerType: Guid
    szSerialNumber: Windows.Win32.Foundation.CHAR * 32
    szRevision: Windows.Win32.Foundation.CHAR * 32
    szDeviceName: Windows.Win32.Foundation.CHAR * 64
    ScsiPort: UInt16
    ScsiBus: UInt16
    ScsiTarget: UInt16
    ScsiLun: UInt16
    Library: Guid
class NTMS_CHANGERINFORMATIONW(Structure):
    Number: UInt32
    ChangerType: Guid
    szSerialNumber: Char * 32
    szRevision: Char * 32
    szDeviceName: Char * 64
    ScsiPort: UInt16
    ScsiBus: UInt16
    ScsiTarget: UInt16
    ScsiLun: UInt16
    Library: Guid
class NTMS_CHANGERTYPEINFORMATIONA(Structure):
    szVendor: Windows.Win32.Foundation.CHAR * 128
    szProduct: Windows.Win32.Foundation.CHAR * 128
    DeviceType: UInt32
class NTMS_CHANGERTYPEINFORMATIONW(Structure):
    szVendor: Char * 128
    szProduct: Char * 128
    DeviceType: UInt32
class NTMS_COMPUTERINFORMATION(Structure):
    dwLibRequestPurgeTime: UInt32
    dwOpRequestPurgeTime: UInt32
    dwLibRequestFlags: UInt32
    dwOpRequestFlags: UInt32
    dwMediaPoolPolicy: UInt32
class NTMS_DRIVEINFORMATIONA(Structure):
    Number: UInt32
    State: Windows.Win32.Storage.FileSystem.NtmsDriveState
    DriveType: Guid
    szDeviceName: Windows.Win32.Foundation.CHAR * 64
    szSerialNumber: Windows.Win32.Foundation.CHAR * 32
    szRevision: Windows.Win32.Foundation.CHAR * 32
    ScsiPort: UInt16
    ScsiBus: UInt16
    ScsiTarget: UInt16
    ScsiLun: UInt16
    dwMountCount: UInt32
    LastCleanedTs: Windows.Win32.Foundation.SYSTEMTIME
    SavedPartitionId: Guid
    Library: Guid
    Reserved: Guid
    dwDeferDismountDelay: UInt32
class NTMS_DRIVEINFORMATIONW(Structure):
    Number: UInt32
    State: Windows.Win32.Storage.FileSystem.NtmsDriveState
    DriveType: Guid
    szDeviceName: Char * 64
    szSerialNumber: Char * 32
    szRevision: Char * 32
    ScsiPort: UInt16
    ScsiBus: UInt16
    ScsiTarget: UInt16
    ScsiLun: UInt16
    dwMountCount: UInt32
    LastCleanedTs: Windows.Win32.Foundation.SYSTEMTIME
    SavedPartitionId: Guid
    Library: Guid
    Reserved: Guid
    dwDeferDismountDelay: UInt32
class NTMS_DRIVETYPEINFORMATIONA(Structure):
    szVendor: Windows.Win32.Foundation.CHAR * 128
    szProduct: Windows.Win32.Foundation.CHAR * 128
    NumberOfHeads: UInt32
    DeviceType: Windows.Win32.Storage.FileSystem.FILE_DEVICE_TYPE
class NTMS_DRIVETYPEINFORMATIONW(Structure):
    szVendor: Char * 128
    szProduct: Char * 128
    NumberOfHeads: UInt32
    DeviceType: Windows.Win32.Storage.FileSystem.FILE_DEVICE_TYPE
class NTMS_FILESYSTEM_INFO(Structure):
    FileSystemType: Char * 64
    VolumeName: Char * 256
    SerialNumber: UInt32
class NTMS_I1_LIBRARYINFORMATION(Structure):
    LibraryType: UInt32
    CleanerSlot: Guid
    CleanerSlotDefault: Guid
    LibrarySupportsDriveCleaning: Windows.Win32.Foundation.BOOL
    BarCodeReaderInstalled: Windows.Win32.Foundation.BOOL
    InventoryMethod: UInt32
    dwCleanerUsesRemaining: UInt32
    FirstDriveNumber: UInt32
    dwNumberOfDrives: UInt32
    FirstSlotNumber: UInt32
    dwNumberOfSlots: UInt32
    FirstDoorNumber: UInt32
    dwNumberOfDoors: UInt32
    FirstPortNumber: UInt32
    dwNumberOfPorts: UInt32
    FirstChangerNumber: UInt32
    dwNumberOfChangers: UInt32
    dwNumberOfMedia: UInt32
    dwNumberOfMediaTypes: UInt32
    dwNumberOfLibRequests: UInt32
    Reserved: Guid
class NTMS_I1_LIBREQUESTINFORMATIONA(Structure):
    OperationCode: UInt32
    OperationOption: UInt32
    State: UInt32
    PartitionId: Guid
    DriveId: Guid
    PhysMediaId: Guid
    Library: Guid
    SlotId: Guid
    TimeQueued: Windows.Win32.Foundation.SYSTEMTIME
    TimeCompleted: Windows.Win32.Foundation.SYSTEMTIME
    szApplication: Windows.Win32.Foundation.CHAR * 64
    szUser: Windows.Win32.Foundation.CHAR * 64
    szComputer: Windows.Win32.Foundation.CHAR * 64
class NTMS_I1_LIBREQUESTINFORMATIONW(Structure):
    OperationCode: UInt32
    OperationOption: UInt32
    State: UInt32
    PartitionId: Guid
    DriveId: Guid
    PhysMediaId: Guid
    Library: Guid
    SlotId: Guid
    TimeQueued: Windows.Win32.Foundation.SYSTEMTIME
    TimeCompleted: Windows.Win32.Foundation.SYSTEMTIME
    szApplication: Char * 64
    szUser: Char * 64
    szComputer: Char * 64
class NTMS_I1_OBJECTINFORMATIONA(Structure):
    dwSize: UInt32
    dwType: UInt32
    Created: Windows.Win32.Foundation.SYSTEMTIME
    Modified: Windows.Win32.Foundation.SYSTEMTIME
    ObjectGuid: Guid
    Enabled: Windows.Win32.Foundation.BOOL
    dwOperationalState: UInt32
    szName: Windows.Win32.Foundation.CHAR * 64
    szDescription: Windows.Win32.Foundation.CHAR * 127
    Info: _Info_e__Union
    class _Info_e__Union(Union):
        Drive: Windows.Win32.Storage.FileSystem.NTMS_DRIVEINFORMATIONA
        DriveType: Windows.Win32.Storage.FileSystem.NTMS_DRIVETYPEINFORMATIONA
        Library: Windows.Win32.Storage.FileSystem.NTMS_I1_LIBRARYINFORMATION
        Changer: Windows.Win32.Storage.FileSystem.NTMS_CHANGERINFORMATIONA
        ChangerType: Windows.Win32.Storage.FileSystem.NTMS_CHANGERTYPEINFORMATIONA
        StorageSlot: Windows.Win32.Storage.FileSystem.NTMS_STORAGESLOTINFORMATION
        IEDoor: Windows.Win32.Storage.FileSystem.NTMS_IEDOORINFORMATION
        IEPort: Windows.Win32.Storage.FileSystem.NTMS_IEPORTINFORMATION
        PhysicalMedia: Windows.Win32.Storage.FileSystem.NTMS_I1_PMIDINFORMATIONA
        LogicalMedia: Windows.Win32.Storage.FileSystem.NTMS_LMIDINFORMATION
        Partition: Windows.Win32.Storage.FileSystem.NTMS_I1_PARTITIONINFORMATIONA
        MediaPool: Windows.Win32.Storage.FileSystem.NTMS_MEDIAPOOLINFORMATION
        MediaType: Windows.Win32.Storage.FileSystem.NTMS_MEDIATYPEINFORMATION
        LibRequest: Windows.Win32.Storage.FileSystem.NTMS_I1_LIBREQUESTINFORMATIONA
        OpRequest: Windows.Win32.Storage.FileSystem.NTMS_I1_OPREQUESTINFORMATIONA
class NTMS_I1_OBJECTINFORMATIONW(Structure):
    dwSize: UInt32
    dwType: UInt32
    Created: Windows.Win32.Foundation.SYSTEMTIME
    Modified: Windows.Win32.Foundation.SYSTEMTIME
    ObjectGuid: Guid
    Enabled: Windows.Win32.Foundation.BOOL
    dwOperationalState: UInt32
    szName: Char * 64
    szDescription: Char * 127
    Info: _Info_e__Union
    class _Info_e__Union(Union):
        Drive: Windows.Win32.Storage.FileSystem.NTMS_DRIVEINFORMATIONW
        DriveType: Windows.Win32.Storage.FileSystem.NTMS_DRIVETYPEINFORMATIONW
        Library: Windows.Win32.Storage.FileSystem.NTMS_I1_LIBRARYINFORMATION
        Changer: Windows.Win32.Storage.FileSystem.NTMS_CHANGERINFORMATIONW
        ChangerType: Windows.Win32.Storage.FileSystem.NTMS_CHANGERTYPEINFORMATIONW
        StorageSlot: Windows.Win32.Storage.FileSystem.NTMS_STORAGESLOTINFORMATION
        IEDoor: Windows.Win32.Storage.FileSystem.NTMS_IEDOORINFORMATION
        IEPort: Windows.Win32.Storage.FileSystem.NTMS_IEPORTINFORMATION
        PhysicalMedia: Windows.Win32.Storage.FileSystem.NTMS_I1_PMIDINFORMATIONW
        LogicalMedia: Windows.Win32.Storage.FileSystem.NTMS_LMIDINFORMATION
        Partition: Windows.Win32.Storage.FileSystem.NTMS_I1_PARTITIONINFORMATIONW
        MediaPool: Windows.Win32.Storage.FileSystem.NTMS_MEDIAPOOLINFORMATION
        MediaType: Windows.Win32.Storage.FileSystem.NTMS_MEDIATYPEINFORMATION
        LibRequest: Windows.Win32.Storage.FileSystem.NTMS_I1_LIBREQUESTINFORMATIONW
        OpRequest: Windows.Win32.Storage.FileSystem.NTMS_I1_OPREQUESTINFORMATIONW
class NTMS_I1_OPREQUESTINFORMATIONA(Structure):
    Request: UInt32
    Submitted: Windows.Win32.Foundation.SYSTEMTIME
    State: UInt32
    szMessage: Windows.Win32.Foundation.CHAR * 127
    Arg1Type: UInt32
    Arg1: Guid
    Arg2Type: UInt32
    Arg2: Guid
    szApplication: Windows.Win32.Foundation.CHAR * 64
    szUser: Windows.Win32.Foundation.CHAR * 64
    szComputer: Windows.Win32.Foundation.CHAR * 64
class NTMS_I1_OPREQUESTINFORMATIONW(Structure):
    Request: UInt32
    Submitted: Windows.Win32.Foundation.SYSTEMTIME
    State: UInt32
    szMessage: Char * 127
    Arg1Type: UInt32
    Arg1: Guid
    Arg2Type: UInt32
    Arg2: Guid
    szApplication: Char * 64
    szUser: Char * 64
    szComputer: Char * 64
class NTMS_I1_PARTITIONINFORMATIONA(Structure):
    PhysicalMedia: Guid
    LogicalMedia: Guid
    State: UInt32
    Side: UInt16
    dwOmidLabelIdLength: UInt32
    OmidLabelId: Byte * 255
    szOmidLabelType: Windows.Win32.Foundation.CHAR * 64
    szOmidLabelInfo: Windows.Win32.Foundation.CHAR * 256
    dwMountCount: UInt32
    dwAllocateCount: UInt32
class NTMS_I1_PARTITIONINFORMATIONW(Structure):
    PhysicalMedia: Guid
    LogicalMedia: Guid
    State: UInt32
    Side: UInt16
    dwOmidLabelIdLength: UInt32
    OmidLabelId: Byte * 255
    szOmidLabelType: Char * 64
    szOmidLabelInfo: Char * 256
    dwMountCount: UInt32
    dwAllocateCount: UInt32
class NTMS_I1_PMIDINFORMATIONA(Structure):
    CurrentLibrary: Guid
    MediaPool: Guid
    Location: Guid
    LocationType: UInt32
    MediaType: Guid
    HomeSlot: Guid
    szBarCode: Windows.Win32.Foundation.CHAR * 64
    BarCodeState: UInt32
    szSequenceNumber: Windows.Win32.Foundation.CHAR * 32
    MediaState: UInt32
    dwNumberOfPartitions: UInt32
class NTMS_I1_PMIDINFORMATIONW(Structure):
    CurrentLibrary: Guid
    MediaPool: Guid
    Location: Guid
    LocationType: UInt32
    MediaType: Guid
    HomeSlot: Guid
    szBarCode: Char * 64
    BarCodeState: UInt32
    szSequenceNumber: Char * 32
    MediaState: UInt32
    dwNumberOfPartitions: UInt32
class NTMS_IEDOORINFORMATION(Structure):
    Number: UInt32
    State: Windows.Win32.Storage.FileSystem.NtmsDoorState
    MaxOpenSecs: UInt16
    Library: Guid
class NTMS_IEPORTINFORMATION(Structure):
    Number: UInt32
    Content: Windows.Win32.Storage.FileSystem.NtmsPortContent
    Position: Windows.Win32.Storage.FileSystem.NtmsPortPosition
    MaxExtendSecs: UInt16
    Library: Guid
class NTMS_LIBRARYINFORMATION(Structure):
    LibraryType: Windows.Win32.Storage.FileSystem.NtmsLibraryType
    CleanerSlot: Guid
    CleanerSlotDefault: Guid
    LibrarySupportsDriveCleaning: Windows.Win32.Foundation.BOOL
    BarCodeReaderInstalled: Windows.Win32.Foundation.BOOL
    InventoryMethod: Windows.Win32.Storage.FileSystem.NtmsInventoryMethod
    dwCleanerUsesRemaining: UInt32
    FirstDriveNumber: UInt32
    dwNumberOfDrives: UInt32
    FirstSlotNumber: UInt32
    dwNumberOfSlots: UInt32
    FirstDoorNumber: UInt32
    dwNumberOfDoors: UInt32
    FirstPortNumber: UInt32
    dwNumberOfPorts: UInt32
    FirstChangerNumber: UInt32
    dwNumberOfChangers: UInt32
    dwNumberOfMedia: UInt32
    dwNumberOfMediaTypes: UInt32
    dwNumberOfLibRequests: UInt32
    Reserved: Guid
    AutoRecovery: Windows.Win32.Foundation.BOOL
    dwFlags: Windows.Win32.Storage.FileSystem.NtmsLibraryFlags
class NTMS_LIBREQUESTINFORMATIONA(Structure):
    OperationCode: Windows.Win32.Storage.FileSystem.NtmsLmOperation
    OperationOption: UInt32
    State: Windows.Win32.Storage.FileSystem.NtmsLmState
    PartitionId: Guid
    DriveId: Guid
    PhysMediaId: Guid
    Library: Guid
    SlotId: Guid
    TimeQueued: Windows.Win32.Foundation.SYSTEMTIME
    TimeCompleted: Windows.Win32.Foundation.SYSTEMTIME
    szApplication: Windows.Win32.Foundation.CHAR * 64
    szUser: Windows.Win32.Foundation.CHAR * 64
    szComputer: Windows.Win32.Foundation.CHAR * 64
    dwErrorCode: UInt32
    WorkItemId: Guid
    dwPriority: UInt32
class NTMS_LIBREQUESTINFORMATIONW(Structure):
    OperationCode: Windows.Win32.Storage.FileSystem.NtmsLmOperation
    OperationOption: UInt32
    State: Windows.Win32.Storage.FileSystem.NtmsLmState
    PartitionId: Guid
    DriveId: Guid
    PhysMediaId: Guid
    Library: Guid
    SlotId: Guid
    TimeQueued: Windows.Win32.Foundation.SYSTEMTIME
    TimeCompleted: Windows.Win32.Foundation.SYSTEMTIME
    szApplication: Char * 64
    szUser: Char * 64
    szComputer: Char * 64
    dwErrorCode: UInt32
    WorkItemId: Guid
    dwPriority: UInt32
class NTMS_LMIDINFORMATION(Structure):
    MediaPool: Guid
    dwNumberOfPartitions: UInt32
class NTMS_MEDIAPOOLINFORMATION(Structure):
    PoolType: UInt32
    MediaType: Guid
    Parent: Guid
    AllocationPolicy: UInt32
    DeallocationPolicy: UInt32
    dwMaxAllocates: UInt32
    dwNumberOfPhysicalMedia: UInt32
    dwNumberOfLogicalMedia: UInt32
    dwNumberOfMediaPools: UInt32
class NTMS_MEDIATYPEINFORMATION(Structure):
    MediaType: UInt32
    NumberOfSides: UInt32
    ReadWriteCharacteristics: Windows.Win32.Storage.FileSystem.NtmsReadWriteCharacteristics
    DeviceType: Windows.Win32.Storage.FileSystem.FILE_DEVICE_TYPE
class NTMS_MOUNT_INFORMATION(Structure):
    dwSize: UInt32
    lpReserved: c_void_p
class NTMS_NOTIFICATIONINFORMATION(Structure):
    dwOperation: Windows.Win32.Storage.FileSystem.NtmsNotificationOperations
    ObjectId: Guid
class NTMS_OBJECTINFORMATIONA(Structure):
    dwSize: UInt32
    dwType: Windows.Win32.Storage.FileSystem.NtmsObjectsTypes
    Created: Windows.Win32.Foundation.SYSTEMTIME
    Modified: Windows.Win32.Foundation.SYSTEMTIME
    ObjectGuid: Guid
    Enabled: Windows.Win32.Foundation.BOOL
    dwOperationalState: Windows.Win32.Storage.FileSystem.NtmsOperationalState
    szName: Windows.Win32.Foundation.CHAR * 64
    szDescription: Windows.Win32.Foundation.CHAR * 127
    Info: _Info_e__Union
    class _Info_e__Union(Union):
        Drive: Windows.Win32.Storage.FileSystem.NTMS_DRIVEINFORMATIONA
        DriveType: Windows.Win32.Storage.FileSystem.NTMS_DRIVETYPEINFORMATIONA
        Library: Windows.Win32.Storage.FileSystem.NTMS_LIBRARYINFORMATION
        Changer: Windows.Win32.Storage.FileSystem.NTMS_CHANGERINFORMATIONA
        ChangerType: Windows.Win32.Storage.FileSystem.NTMS_CHANGERTYPEINFORMATIONA
        StorageSlot: Windows.Win32.Storage.FileSystem.NTMS_STORAGESLOTINFORMATION
        IEDoor: Windows.Win32.Storage.FileSystem.NTMS_IEDOORINFORMATION
        IEPort: Windows.Win32.Storage.FileSystem.NTMS_IEPORTINFORMATION
        PhysicalMedia: Windows.Win32.Storage.FileSystem.NTMS_PMIDINFORMATIONA
        LogicalMedia: Windows.Win32.Storage.FileSystem.NTMS_LMIDINFORMATION
        Partition: Windows.Win32.Storage.FileSystem.NTMS_PARTITIONINFORMATIONA
        MediaPool: Windows.Win32.Storage.FileSystem.NTMS_MEDIAPOOLINFORMATION
        MediaType: Windows.Win32.Storage.FileSystem.NTMS_MEDIATYPEINFORMATION
        LibRequest: Windows.Win32.Storage.FileSystem.NTMS_LIBREQUESTINFORMATIONA
        OpRequest: Windows.Win32.Storage.FileSystem.NTMS_OPREQUESTINFORMATIONA
        Computer: Windows.Win32.Storage.FileSystem.NTMS_COMPUTERINFORMATION
class NTMS_OBJECTINFORMATIONW(Structure):
    dwSize: UInt32
    dwType: Windows.Win32.Storage.FileSystem.NtmsObjectsTypes
    Created: Windows.Win32.Foundation.SYSTEMTIME
    Modified: Windows.Win32.Foundation.SYSTEMTIME
    ObjectGuid: Guid
    Enabled: Windows.Win32.Foundation.BOOL
    dwOperationalState: Windows.Win32.Storage.FileSystem.NtmsOperationalState
    szName: Char * 64
    szDescription: Char * 127
    Info: _Info_e__Union
    class _Info_e__Union(Union):
        Drive: Windows.Win32.Storage.FileSystem.NTMS_DRIVEINFORMATIONW
        DriveType: Windows.Win32.Storage.FileSystem.NTMS_DRIVETYPEINFORMATIONW
        Library: Windows.Win32.Storage.FileSystem.NTMS_LIBRARYINFORMATION
        Changer: Windows.Win32.Storage.FileSystem.NTMS_CHANGERINFORMATIONW
        ChangerType: Windows.Win32.Storage.FileSystem.NTMS_CHANGERTYPEINFORMATIONW
        StorageSlot: Windows.Win32.Storage.FileSystem.NTMS_STORAGESLOTINFORMATION
        IEDoor: Windows.Win32.Storage.FileSystem.NTMS_IEDOORINFORMATION
        IEPort: Windows.Win32.Storage.FileSystem.NTMS_IEPORTINFORMATION
        PhysicalMedia: Windows.Win32.Storage.FileSystem.NTMS_PMIDINFORMATIONW
        LogicalMedia: Windows.Win32.Storage.FileSystem.NTMS_LMIDINFORMATION
        Partition: Windows.Win32.Storage.FileSystem.NTMS_PARTITIONINFORMATIONW
        MediaPool: Windows.Win32.Storage.FileSystem.NTMS_MEDIAPOOLINFORMATION
        MediaType: Windows.Win32.Storage.FileSystem.NTMS_MEDIATYPEINFORMATION
        LibRequest: Windows.Win32.Storage.FileSystem.NTMS_LIBREQUESTINFORMATIONW
        OpRequest: Windows.Win32.Storage.FileSystem.NTMS_OPREQUESTINFORMATIONW
        Computer: Windows.Win32.Storage.FileSystem.NTMS_COMPUTERINFORMATION
NTMS_OMID_TYPE = UInt32
NTMS_OMID_TYPE_FILESYSTEM_INFO: NTMS_OMID_TYPE = 2
NTMS_OMID_TYPE_RAW_LABEL: NTMS_OMID_TYPE = 1
class NTMS_OPREQUESTINFORMATIONA(Structure):
    Request: Windows.Win32.Storage.FileSystem.NtmsOpreqCommand
    Submitted: Windows.Win32.Foundation.SYSTEMTIME
    State: Windows.Win32.Storage.FileSystem.NtmsOpreqState
    szMessage: Windows.Win32.Foundation.CHAR * 256
    Arg1Type: Windows.Win32.Storage.FileSystem.NtmsObjectsTypes
    Arg1: Guid
    Arg2Type: Windows.Win32.Storage.FileSystem.NtmsObjectsTypes
    Arg2: Guid
    szApplication: Windows.Win32.Foundation.CHAR * 64
    szUser: Windows.Win32.Foundation.CHAR * 64
    szComputer: Windows.Win32.Foundation.CHAR * 64
class NTMS_OPREQUESTINFORMATIONW(Structure):
    Request: Windows.Win32.Storage.FileSystem.NtmsOpreqCommand
    Submitted: Windows.Win32.Foundation.SYSTEMTIME
    State: Windows.Win32.Storage.FileSystem.NtmsOpreqState
    szMessage: Char * 256
    Arg1Type: Windows.Win32.Storage.FileSystem.NtmsObjectsTypes
    Arg1: Guid
    Arg2Type: Windows.Win32.Storage.FileSystem.NtmsObjectsTypes
    Arg2: Guid
    szApplication: Char * 64
    szUser: Char * 64
    szComputer: Char * 64
class NTMS_PARTITIONINFORMATIONA(Structure):
    PhysicalMedia: Guid
    LogicalMedia: Guid
    State: Windows.Win32.Storage.FileSystem.NtmsPartitionState
    Side: UInt16
    dwOmidLabelIdLength: UInt32
    OmidLabelId: Byte * 255
    szOmidLabelType: Windows.Win32.Foundation.CHAR * 64
    szOmidLabelInfo: Windows.Win32.Foundation.CHAR * 256
    dwMountCount: UInt32
    dwAllocateCount: UInt32
    Capacity: Windows.Win32.Foundation.LARGE_INTEGER
class NTMS_PARTITIONINFORMATIONW(Structure):
    PhysicalMedia: Guid
    LogicalMedia: Guid
    State: Windows.Win32.Storage.FileSystem.NtmsPartitionState
    Side: UInt16
    dwOmidLabelIdLength: UInt32
    OmidLabelId: Byte * 255
    szOmidLabelType: Char * 64
    szOmidLabelInfo: Char * 256
    dwMountCount: UInt32
    dwAllocateCount: UInt32
    Capacity: Windows.Win32.Foundation.LARGE_INTEGER
class NTMS_PMIDINFORMATIONA(Structure):
    CurrentLibrary: Guid
    MediaPool: Guid
    Location: Guid
    LocationType: UInt32
    MediaType: Guid
    HomeSlot: Guid
    szBarCode: Windows.Win32.Foundation.CHAR * 64
    BarCodeState: Windows.Win32.Storage.FileSystem.NtmsBarCodeState
    szSequenceNumber: Windows.Win32.Foundation.CHAR * 32
    MediaState: Windows.Win32.Storage.FileSystem.NtmsMediaState
    dwNumberOfPartitions: UInt32
    dwMediaTypeCode: UInt32
    dwDensityCode: UInt32
    MountedPartition: Guid
class NTMS_PMIDINFORMATIONW(Structure):
    CurrentLibrary: Guid
    MediaPool: Guid
    Location: Guid
    LocationType: UInt32
    MediaType: Guid
    HomeSlot: Guid
    szBarCode: Char * 64
    BarCodeState: Windows.Win32.Storage.FileSystem.NtmsBarCodeState
    szSequenceNumber: Char * 32
    MediaState: Windows.Win32.Storage.FileSystem.NtmsMediaState
    dwNumberOfPartitions: UInt32
    dwMediaTypeCode: UInt32
    dwDensityCode: UInt32
    MountedPartition: Guid
class NTMS_STORAGESLOTINFORMATION(Structure):
    Number: UInt32
    State: UInt32
    Library: Guid
NT_CREATE_FILE_DISPOSITION = UInt32
FILE_SUPERSEDE: NT_CREATE_FILE_DISPOSITION = 0
FILE_CREATE: NT_CREATE_FILE_DISPOSITION = 2
FILE_OPEN: NT_CREATE_FILE_DISPOSITION = 1
FILE_OPEN_IF: NT_CREATE_FILE_DISPOSITION = 3
FILE_OVERWRITE: NT_CREATE_FILE_DISPOSITION = 4
FILE_OVERWRITE_IF: NT_CREATE_FILE_DISPOSITION = 5
NtmsAccessMask = Int32
NTMS_USE_ACCESS: NtmsAccessMask = 1
NTMS_MODIFY_ACCESS: NtmsAccessMask = 2
NTMS_CONTROL_ACCESS: NtmsAccessMask = 4
NtmsAllocateOptions = Int32
NTMS_ALLOCATE_NEW: NtmsAllocateOptions = 1
NTMS_ALLOCATE_NEXT: NtmsAllocateOptions = 2
NTMS_ALLOCATE_ERROR_IF_UNAVAILABLE: NtmsAllocateOptions = 4
NtmsAllocationPolicy = Int32
NTMS_ALLOCATE_FROMSCRATCH: NtmsAllocationPolicy = 1
NtmsAsyncOperations = Int32
NTMS_ASYNCOP_MOUNT: NtmsAsyncOperations = 1
NtmsAsyncStatus = Int32
NTMS_ASYNCSTATE_QUEUED: NtmsAsyncStatus = 0
NTMS_ASYNCSTATE_WAIT_RESOURCE: NtmsAsyncStatus = 1
NTMS_ASYNCSTATE_WAIT_OPERATOR: NtmsAsyncStatus = 2
NTMS_ASYNCSTATE_INPROCESS: NtmsAsyncStatus = 3
NTMS_ASYNCSTATE_COMPLETE: NtmsAsyncStatus = 4
NtmsBarCodeState = Int32
NTMS_BARCODESTATE_OK: NtmsBarCodeState = 1
NTMS_BARCODESTATE_UNREADABLE: NtmsBarCodeState = 2
NtmsCreateNtmsMediaOptions = Int32
NTMS_ERROR_ON_DUPLICATE: NtmsCreateNtmsMediaOptions = 1
NtmsCreateOptions = Int32
NTMS_OPEN_EXISTING: NtmsCreateOptions = 1
NTMS_CREATE_NEW: NtmsCreateOptions = 2
NTMS_OPEN_ALWAYS: NtmsCreateOptions = 3
NtmsDeallocationPolicy = Int32
NTMS_DEALLOCATE_TOSCRATCH: NtmsDeallocationPolicy = 1
NtmsDismountOptions = Int32
NTMS_DISMOUNT_DEFERRED: NtmsDismountOptions = 1
NTMS_DISMOUNT_IMMEDIATE: NtmsDismountOptions = 2
NtmsDoorState = Int32
NTMS_DOORSTATE_UNKNOWN: NtmsDoorState = 0
NTMS_DOORSTATE_CLOSED: NtmsDoorState = 1
NTMS_DOORSTATE_OPEN: NtmsDoorState = 2
NtmsDriveState = Int32
NTMS_DRIVESTATE_DISMOUNTED: NtmsDriveState = 0
NTMS_DRIVESTATE_MOUNTED: NtmsDriveState = 1
NTMS_DRIVESTATE_LOADED: NtmsDriveState = 2
NTMS_DRIVESTATE_UNLOADED: NtmsDriveState = 5
NTMS_DRIVESTATE_BEING_CLEANED: NtmsDriveState = 6
NTMS_DRIVESTATE_DISMOUNTABLE: NtmsDriveState = 7
NtmsDriveType = Int32
NTMS_UNKNOWN_DRIVE: NtmsDriveType = 0
NtmsEjectOperation = Int32
NTMS_EJECT_START: NtmsEjectOperation = 0
NTMS_EJECT_STOP: NtmsEjectOperation = 1
NTMS_EJECT_QUEUE: NtmsEjectOperation = 2
NTMS_EJECT_FORCE: NtmsEjectOperation = 3
NTMS_EJECT_IMMEDIATE: NtmsEjectOperation = 4
NTMS_EJECT_ASK_USER: NtmsEjectOperation = 5
NtmsEnumerateOption = Int32
NTMS_ENUM_DEFAULT: NtmsEnumerateOption = 0
NTMS_ENUM_ROOTPOOL: NtmsEnumerateOption = 1
NtmsInjectOperation = Int32
NTMS_INJECT_START: NtmsInjectOperation = 0
NTMS_INJECT_STOP: NtmsInjectOperation = 1
NTMS_INJECT_RETRACT: NtmsInjectOperation = 2
NTMS_INJECT_STARTMANY: NtmsInjectOperation = 3
NtmsInventoryMethod = Int32
NTMS_INVENTORY_NONE: NtmsInventoryMethod = 0
NTMS_INVENTORY_FAST: NtmsInventoryMethod = 1
NTMS_INVENTORY_OMID: NtmsInventoryMethod = 2
NTMS_INVENTORY_DEFAULT: NtmsInventoryMethod = 3
NTMS_INVENTORY_SLOT: NtmsInventoryMethod = 4
NTMS_INVENTORY_STOP: NtmsInventoryMethod = 5
NTMS_INVENTORY_MAX: NtmsInventoryMethod = 6
NtmsLibRequestFlags = Int32
NTMS_LIBREQFLAGS_NOAUTOPURGE: NtmsLibRequestFlags = 1
NTMS_LIBREQFLAGS_NOFAILEDPURGE: NtmsLibRequestFlags = 2
NtmsLibraryFlags = Int32
NTMS_LIBRARYFLAG_FIXEDOFFLINE: NtmsLibraryFlags = 1
NTMS_LIBRARYFLAG_CLEANERPRESENT: NtmsLibraryFlags = 2
NTMS_LIBRARYFLAG_AUTODETECTCHANGE: NtmsLibraryFlags = 4
NTMS_LIBRARYFLAG_IGNORECLEANERUSESREMAINING: NtmsLibraryFlags = 8
NTMS_LIBRARYFLAG_RECOGNIZECLEANERBARCODE: NtmsLibraryFlags = 16
NtmsLibraryType = Int32
NTMS_LIBRARYTYPE_UNKNOWN: NtmsLibraryType = 0
NTMS_LIBRARYTYPE_OFFLINE: NtmsLibraryType = 1
NTMS_LIBRARYTYPE_ONLINE: NtmsLibraryType = 2
NTMS_LIBRARYTYPE_STANDALONE: NtmsLibraryType = 3
NtmsLmOperation = Int32
NTMS_LM_REMOVE: NtmsLmOperation = 0
NTMS_LM_DISABLECHANGER: NtmsLmOperation = 1
NTMS_LM_DISABLELIBRARY: NtmsLmOperation = 1
NTMS_LM_ENABLECHANGER: NtmsLmOperation = 2
NTMS_LM_ENABLELIBRARY: NtmsLmOperation = 2
NTMS_LM_DISABLEDRIVE: NtmsLmOperation = 3
NTMS_LM_ENABLEDRIVE: NtmsLmOperation = 4
NTMS_LM_DISABLEMEDIA: NtmsLmOperation = 5
NTMS_LM_ENABLEMEDIA: NtmsLmOperation = 6
NTMS_LM_UPDATEOMID: NtmsLmOperation = 7
NTMS_LM_INVENTORY: NtmsLmOperation = 8
NTMS_LM_DOORACCESS: NtmsLmOperation = 9
NTMS_LM_EJECT: NtmsLmOperation = 10
NTMS_LM_EJECTCLEANER: NtmsLmOperation = 11
NTMS_LM_INJECT: NtmsLmOperation = 12
NTMS_LM_INJECTCLEANER: NtmsLmOperation = 13
NTMS_LM_PROCESSOMID: NtmsLmOperation = 14
NTMS_LM_CLEANDRIVE: NtmsLmOperation = 15
NTMS_LM_DISMOUNT: NtmsLmOperation = 16
NTMS_LM_MOUNT: NtmsLmOperation = 17
NTMS_LM_WRITESCRATCH: NtmsLmOperation = 18
NTMS_LM_CLASSIFY: NtmsLmOperation = 19
NTMS_LM_RESERVECLEANER: NtmsLmOperation = 20
NTMS_LM_RELEASECLEANER: NtmsLmOperation = 21
NTMS_LM_MAXWORKITEM: NtmsLmOperation = 22
NtmsLmState = Int32
NTMS_LM_QUEUED: NtmsLmState = 0
NTMS_LM_INPROCESS: NtmsLmState = 1
NTMS_LM_PASSED: NtmsLmState = 2
NTMS_LM_FAILED: NtmsLmState = 3
NTMS_LM_INVALID: NtmsLmState = 4
NTMS_LM_WAITING: NtmsLmState = 5
NTMS_LM_DEFERRED: NtmsLmState = 6
NTMS_LM_DEFFERED: NtmsLmState = 6
NTMS_LM_CANCELLED: NtmsLmState = 7
NTMS_LM_STOPPED: NtmsLmState = 8
NtmsMediaPoolPolicy = Int32
NTMS_POOLPOLICY_PURGEOFFLINESCRATCH: NtmsMediaPoolPolicy = 1
NTMS_POOLPOLICY_KEEPOFFLINEIMPORT: NtmsMediaPoolPolicy = 2
NtmsMediaState = Int32
NTMS_MEDIASTATE_IDLE: NtmsMediaState = 0
NTMS_MEDIASTATE_INUSE: NtmsMediaState = 1
NTMS_MEDIASTATE_MOUNTED: NtmsMediaState = 2
NTMS_MEDIASTATE_LOADED: NtmsMediaState = 3
NTMS_MEDIASTATE_UNLOADED: NtmsMediaState = 4
NTMS_MEDIASTATE_OPERROR: NtmsMediaState = 5
NTMS_MEDIASTATE_OPREQ: NtmsMediaState = 6
NtmsMountOptions = Int32
NTMS_MOUNT_READ: NtmsMountOptions = 1
NTMS_MOUNT_WRITE: NtmsMountOptions = 2
NTMS_MOUNT_ERROR_NOT_AVAILABLE: NtmsMountOptions = 4
NTMS_MOUNT_ERROR_IF_UNAVAILABLE: NtmsMountOptions = 4
NTMS_MOUNT_ERROR_OFFLINE: NtmsMountOptions = 8
NTMS_MOUNT_ERROR_IF_OFFLINE: NtmsMountOptions = 8
NTMS_MOUNT_SPECIFIC_DRIVE: NtmsMountOptions = 16
NTMS_MOUNT_NOWAIT: NtmsMountOptions = 32
NtmsMountPriority = Int32
NTMS_PRIORITY_DEFAULT: NtmsMountPriority = 0
NTMS_PRIORITY_HIGHEST: NtmsMountPriority = 15
NTMS_PRIORITY_HIGH: NtmsMountPriority = 7
NTMS_PRIORITY_NORMAL: NtmsMountPriority = 0
NTMS_PRIORITY_LOW: NtmsMountPriority = -7
NTMS_PRIORITY_LOWEST: NtmsMountPriority = -15
NtmsNotificationOperations = Int32
NTMS_OBJ_UPDATE: NtmsNotificationOperations = 1
NTMS_OBJ_INSERT: NtmsNotificationOperations = 2
NTMS_OBJ_DELETE: NtmsNotificationOperations = 3
NTMS_EVENT_SIGNAL: NtmsNotificationOperations = 4
NTMS_EVENT_COMPLETE: NtmsNotificationOperations = 5
NtmsObjectsTypes = Int32
NTMS_UNKNOWN: NtmsObjectsTypes = 0
NTMS_OBJECT: NtmsObjectsTypes = 1
NTMS_CHANGER: NtmsObjectsTypes = 2
NTMS_CHANGER_TYPE: NtmsObjectsTypes = 3
NTMS_COMPUTER: NtmsObjectsTypes = 4
NTMS_DRIVE: NtmsObjectsTypes = 5
NTMS_DRIVE_TYPE: NtmsObjectsTypes = 6
NTMS_IEDOOR: NtmsObjectsTypes = 7
NTMS_IEPORT: NtmsObjectsTypes = 8
NTMS_LIBRARY: NtmsObjectsTypes = 9
NTMS_LIBREQUEST: NtmsObjectsTypes = 10
NTMS_LOGICAL_MEDIA: NtmsObjectsTypes = 11
NTMS_MEDIA_POOL: NtmsObjectsTypes = 12
NTMS_MEDIA_TYPE: NtmsObjectsTypes = 13
NTMS_PARTITION: NtmsObjectsTypes = 14
NTMS_PHYSICAL_MEDIA: NtmsObjectsTypes = 15
NTMS_STORAGESLOT: NtmsObjectsTypes = 16
NTMS_OPREQUEST: NtmsObjectsTypes = 17
NTMS_UI_DESTINATION: NtmsObjectsTypes = 18
NTMS_NUMBER_OF_OBJECT_TYPES: NtmsObjectsTypes = 19
NtmsOpRequestFlags = Int32
NTMS_OPREQFLAGS_NOAUTOPURGE: NtmsOpRequestFlags = 1
NTMS_OPREQFLAGS_NOFAILEDPURGE: NtmsOpRequestFlags = 2
NTMS_OPREQFLAGS_NOALERTS: NtmsOpRequestFlags = 16
NTMS_OPREQFLAGS_NOTRAYICON: NtmsOpRequestFlags = 32
NtmsOperationalState = Int32
NTMS_READY: NtmsOperationalState = 0
NTMS_INITIALIZING: NtmsOperationalState = 10
NTMS_NEEDS_SERVICE: NtmsOperationalState = 20
NTMS_NOT_PRESENT: NtmsOperationalState = 21
NtmsOpreqCommand = Int32
NTMS_OPREQ_UNKNOWN: NtmsOpreqCommand = 0
NTMS_OPREQ_NEWMEDIA: NtmsOpreqCommand = 1
NTMS_OPREQ_CLEANER: NtmsOpreqCommand = 2
NTMS_OPREQ_DEVICESERVICE: NtmsOpreqCommand = 3
NTMS_OPREQ_MOVEMEDIA: NtmsOpreqCommand = 4
NTMS_OPREQ_MESSAGE: NtmsOpreqCommand = 5
NtmsOpreqState = Int32
NTMS_OPSTATE_UNKNOWN: NtmsOpreqState = 0
NTMS_OPSTATE_SUBMITTED: NtmsOpreqState = 1
NTMS_OPSTATE_ACTIVE: NtmsOpreqState = 2
NTMS_OPSTATE_INPROGRESS: NtmsOpreqState = 3
NTMS_OPSTATE_REFUSED: NtmsOpreqState = 4
NTMS_OPSTATE_COMPLETE: NtmsOpreqState = 5
NtmsPartitionState = Int32
NTMS_PARTSTATE_UNKNOWN: NtmsPartitionState = 0
NTMS_PARTSTATE_UNPREPARED: NtmsPartitionState = 1
NTMS_PARTSTATE_INCOMPATIBLE: NtmsPartitionState = 2
NTMS_PARTSTATE_DECOMMISSIONED: NtmsPartitionState = 3
NTMS_PARTSTATE_AVAILABLE: NtmsPartitionState = 4
NTMS_PARTSTATE_ALLOCATED: NtmsPartitionState = 5
NTMS_PARTSTATE_COMPLETE: NtmsPartitionState = 6
NTMS_PARTSTATE_FOREIGN: NtmsPartitionState = 7
NTMS_PARTSTATE_IMPORT: NtmsPartitionState = 8
NTMS_PARTSTATE_RESERVED: NtmsPartitionState = 9
NtmsPoolType = Int32
NTMS_POOLTYPE_UNKNOWN: NtmsPoolType = 0
NTMS_POOLTYPE_SCRATCH: NtmsPoolType = 1
NTMS_POOLTYPE_FOREIGN: NtmsPoolType = 2
NTMS_POOLTYPE_IMPORT: NtmsPoolType = 3
NTMS_POOLTYPE_APPLICATION: NtmsPoolType = 1000
NtmsPortContent = Int32
NTMS_PORTCONTENT_UNKNOWN: NtmsPortContent = 0
NTMS_PORTCONTENT_FULL: NtmsPortContent = 1
NTMS_PORTCONTENT_EMPTY: NtmsPortContent = 2
NtmsPortPosition = Int32
NTMS_PORTPOSITION_UNKNOWN: NtmsPortPosition = 0
NTMS_PORTPOSITION_EXTENDED: NtmsPortPosition = 1
NTMS_PORTPOSITION_RETRACTED: NtmsPortPosition = 2
NtmsReadWriteCharacteristics = Int32
NTMS_MEDIARW_UNKNOWN: NtmsReadWriteCharacteristics = 0
NTMS_MEDIARW_REWRITABLE: NtmsReadWriteCharacteristics = 1
NTMS_MEDIARW_WRITEONCE: NtmsReadWriteCharacteristics = 2
NTMS_MEDIARW_READONLY: NtmsReadWriteCharacteristics = 3
NtmsSessionOptions = Int32
NTMS_SESSION_QUERYEXPEDITE: NtmsSessionOptions = 1
NtmsSlotState = Int32
NTMS_SLOTSTATE_UNKNOWN: NtmsSlotState = 0
NTMS_SLOTSTATE_FULL: NtmsSlotState = 1
NTMS_SLOTSTATE_EMPTY: NtmsSlotState = 2
NTMS_SLOTSTATE_NOTPRESENT: NtmsSlotState = 3
NTMS_SLOTSTATE_NEEDSINVENTORY: NtmsSlotState = 4
NtmsUIOperations = Int32
NTMS_UIDEST_ADD: NtmsUIOperations = 1
NTMS_UIDEST_DELETE: NtmsUIOperations = 2
NTMS_UIDEST_DELETEALL: NtmsUIOperations = 3
NTMS_UIOPERATION_MAX: NtmsUIOperations = 4
NtmsUITypes = Int32
NTMS_UITYPE_INVALID: NtmsUITypes = 0
NTMS_UITYPE_INFO: NtmsUITypes = 1
NTMS_UITYPE_REQ: NtmsUITypes = 2
NTMS_UITYPE_ERR: NtmsUITypes = 3
NTMS_UITYPE_MAX: NtmsUITypes = 4
class OFSTRUCT(Structure):
    cBytes: Byte
    fFixedDisk: Byte
    nErrCode: UInt16
    Reserved1: UInt16
    Reserved2: UInt16
    szPathName: Windows.Win32.Foundation.CHAR * 128
@winfunctype_pointer
def PCLFS_COMPLETION_ROUTINE(pvOverlapped: c_void_p, ulReserved: UInt32) -> Void: ...
@winfunctype_pointer
def PCOPYFILE2_PROGRESS_ROUTINE(pMessage: POINTER(Windows.Win32.Storage.FileSystem.COPYFILE2_MESSAGE_head), pvCallbackContext: c_void_p) -> Windows.Win32.Storage.FileSystem.COPYFILE2_MESSAGE_ACTION: ...
@winfunctype_pointer
def PFE_EXPORT_FUNC(pbData: c_char_p_no, pvCallbackContext: c_void_p, ulLength: UInt32) -> UInt32: ...
@winfunctype_pointer
def PFE_IMPORT_FUNC(pbData: c_char_p_no, pvCallbackContext: c_void_p, ulLength: POINTER(UInt32)) -> UInt32: ...
@winfunctype_pointer
def PFN_IO_COMPLETION(pContext: POINTER(Windows.Win32.Storage.FileSystem.FIO_CONTEXT_head), lpo: POINTER(Windows.Win32.Storage.FileSystem.FH_OVERLAPPED_head), cb: UInt32, dwCompletionStatus: UInt32) -> Void: ...
@winfunctype_pointer
def PLOG_FULL_HANDLER_CALLBACK(hLogFile: Windows.Win32.Foundation.HANDLE, dwError: UInt32, fLogIsPinned: Windows.Win32.Foundation.BOOL, pvClientContext: c_void_p) -> Void: ...
@winfunctype_pointer
def PLOG_TAIL_ADVANCE_CALLBACK(hLogFile: Windows.Win32.Foundation.HANDLE, lsnTarget: Windows.Win32.Storage.FileSystem.CLS_LSN, pvClientContext: c_void_p) -> Void: ...
@winfunctype_pointer
def PLOG_UNPINNED_CALLBACK(hLogFile: Windows.Win32.Foundation.HANDLE, pvClientContext: c_void_p) -> Void: ...
PREPARE_TAPE_OPERATION = Int32
TAPE_FORMAT: PREPARE_TAPE_OPERATION = 5
TAPE_LOAD: PREPARE_TAPE_OPERATION = 0
TAPE_LOCK: PREPARE_TAPE_OPERATION = 3
TAPE_TENSION: PREPARE_TAPE_OPERATION = 2
TAPE_UNLOAD: PREPARE_TAPE_OPERATION = 1
TAPE_UNLOCK: PREPARE_TAPE_OPERATION = 4
PRIORITY_HINT = Int32
PRIORITY_HINT_IoPriorityHintVeryLow: PRIORITY_HINT = 0
PRIORITY_HINT_IoPriorityHintLow: PRIORITY_HINT = 1
PRIORITY_HINT_IoPriorityHintNormal: PRIORITY_HINT = 2
PRIORITY_HINT_MaximumIoPriorityHintType: PRIORITY_HINT = 3
READ_DIRECTORY_NOTIFY_INFORMATION_CLASS = Int32
READ_DIRECTORY_NOTIFY_INFORMATION_CLASS_ReadDirectoryNotifyInformation: READ_DIRECTORY_NOTIFY_INFORMATION_CLASS = 1
READ_DIRECTORY_NOTIFY_INFORMATION_CLASS_ReadDirectoryNotifyExtendedInformation: READ_DIRECTORY_NOTIFY_INFORMATION_CLASS = 2
class REPARSE_GUID_DATA_BUFFER(Structure):
    ReparseTag: UInt32
    ReparseDataLength: UInt16
    Reserved: UInt16
    ReparseGuid: Guid
    GenericReparseBuffer: _GenericReparseBuffer_e__Struct
    class _GenericReparseBuffer_e__Struct(Structure):
        DataBuffer: Byte * 1
REPLACE_FILE_FLAGS = UInt32
REPLACEFILE_WRITE_THROUGH: REPLACE_FILE_FLAGS = 1
REPLACEFILE_IGNORE_MERGE_ERRORS: REPLACE_FILE_FLAGS = 2
REPLACEFILE_IGNORE_ACL_ERRORS: REPLACE_FILE_FLAGS = 4
class SERVER_ALIAS_INFO_0(Structure):
    srvai0_alias: Windows.Win32.Foundation.PWSTR
    srvai0_target: Windows.Win32.Foundation.PWSTR
    srvai0_default: Windows.Win32.Foundation.BOOLEAN
    srvai0_reserved: UInt32
class SERVER_CERTIFICATE_INFO_0(Structure):
    srvci0_name: Windows.Win32.Foundation.PWSTR
    srvci0_subject: Windows.Win32.Foundation.PWSTR
    srvci0_issuer: Windows.Win32.Foundation.PWSTR
    srvci0_thumbprint: Windows.Win32.Foundation.PWSTR
    srvci0_friendlyname: Windows.Win32.Foundation.PWSTR
    srvci0_notbefore: Windows.Win32.Foundation.PWSTR
    srvci0_notafter: Windows.Win32.Foundation.PWSTR
    srvci0_storelocation: Windows.Win32.Foundation.PWSTR
    srvci0_storename: Windows.Win32.Foundation.PWSTR
    srvci0_renewalchain: Windows.Win32.Foundation.PWSTR
    srvci0_type: UInt32
    srvci0_flags: UInt32
SERVER_CERTIFICATE_TYPE = Int32
QUIC: SERVER_CERTIFICATE_TYPE = 0
class SESSION_INFO_0(Structure):
    sesi0_cname: Windows.Win32.Foundation.PWSTR
class SESSION_INFO_1(Structure):
    sesi1_cname: Windows.Win32.Foundation.PWSTR
    sesi1_username: Windows.Win32.Foundation.PWSTR
    sesi1_num_opens: UInt32
    sesi1_time: UInt32
    sesi1_idle_time: UInt32
    sesi1_user_flags: Windows.Win32.Storage.FileSystem.SESSION_INFO_USER_FLAGS
class SESSION_INFO_10(Structure):
    sesi10_cname: Windows.Win32.Foundation.PWSTR
    sesi10_username: Windows.Win32.Foundation.PWSTR
    sesi10_time: UInt32
    sesi10_idle_time: UInt32
class SESSION_INFO_2(Structure):
    sesi2_cname: Windows.Win32.Foundation.PWSTR
    sesi2_username: Windows.Win32.Foundation.PWSTR
    sesi2_num_opens: UInt32
    sesi2_time: UInt32
    sesi2_idle_time: UInt32
    sesi2_user_flags: Windows.Win32.Storage.FileSystem.SESSION_INFO_USER_FLAGS
    sesi2_cltype_name: Windows.Win32.Foundation.PWSTR
class SESSION_INFO_502(Structure):
    sesi502_cname: Windows.Win32.Foundation.PWSTR
    sesi502_username: Windows.Win32.Foundation.PWSTR
    sesi502_num_opens: UInt32
    sesi502_time: UInt32
    sesi502_idle_time: UInt32
    sesi502_user_flags: Windows.Win32.Storage.FileSystem.SESSION_INFO_USER_FLAGS
    sesi502_cltype_name: Windows.Win32.Foundation.PWSTR
    sesi502_transport: Windows.Win32.Foundation.PWSTR
SESSION_INFO_USER_FLAGS = UInt32
SESS_GUEST: SESSION_INFO_USER_FLAGS = 1
SESS_NOENCRYPTION: SESSION_INFO_USER_FLAGS = 2
SET_FILE_POINTER_MOVE_METHOD = UInt32
FILE_BEGIN: SET_FILE_POINTER_MOVE_METHOD = 0
FILE_CURRENT: SET_FILE_POINTER_MOVE_METHOD = 1
FILE_END: SET_FILE_POINTER_MOVE_METHOD = 2
class SHARE_INFO_0(Structure):
    shi0_netname: Windows.Win32.Foundation.PWSTR
class SHARE_INFO_1(Structure):
    shi1_netname: Windows.Win32.Foundation.PWSTR
    shi1_type: Windows.Win32.Storage.FileSystem.SHARE_TYPE
    shi1_remark: Windows.Win32.Foundation.PWSTR
class SHARE_INFO_1004(Structure):
    shi1004_remark: Windows.Win32.Foundation.PWSTR
class SHARE_INFO_1005(Structure):
    shi1005_flags: UInt32
class SHARE_INFO_1006(Structure):
    shi1006_max_uses: UInt32
class SHARE_INFO_1501(Structure):
    shi1501_reserved: UInt32
    shi1501_security_descriptor: Windows.Win32.Security.PSECURITY_DESCRIPTOR
class SHARE_INFO_1503(Structure):
    shi1503_sharefilter: Guid
class SHARE_INFO_2(Structure):
    shi2_netname: Windows.Win32.Foundation.PWSTR
    shi2_type: Windows.Win32.Storage.FileSystem.SHARE_TYPE
    shi2_remark: Windows.Win32.Foundation.PWSTR
    shi2_permissions: Windows.Win32.Storage.FileSystem.SHARE_INFO_PERMISSIONS
    shi2_max_uses: UInt32
    shi2_current_uses: UInt32
    shi2_path: Windows.Win32.Foundation.PWSTR
    shi2_passwd: Windows.Win32.Foundation.PWSTR
class SHARE_INFO_501(Structure):
    shi501_netname: Windows.Win32.Foundation.PWSTR
    shi501_type: Windows.Win32.Storage.FileSystem.SHARE_TYPE
    shi501_remark: Windows.Win32.Foundation.PWSTR
    shi501_flags: UInt32
class SHARE_INFO_502(Structure):
    shi502_netname: Windows.Win32.Foundation.PWSTR
    shi502_type: Windows.Win32.Storage.FileSystem.SHARE_TYPE
    shi502_remark: Windows.Win32.Foundation.PWSTR
    shi502_permissions: Windows.Win32.Storage.FileSystem.SHARE_INFO_PERMISSIONS
    shi502_max_uses: UInt32
    shi502_current_uses: UInt32
    shi502_path: Windows.Win32.Foundation.PWSTR
    shi502_passwd: Windows.Win32.Foundation.PWSTR
    shi502_reserved: UInt32
    shi502_security_descriptor: Windows.Win32.Security.PSECURITY_DESCRIPTOR
class SHARE_INFO_503(Structure):
    shi503_netname: Windows.Win32.Foundation.PWSTR
    shi503_type: Windows.Win32.Storage.FileSystem.SHARE_TYPE
    shi503_remark: Windows.Win32.Foundation.PWSTR
    shi503_permissions: Windows.Win32.Storage.FileSystem.SHARE_INFO_PERMISSIONS
    shi503_max_uses: UInt32
    shi503_current_uses: UInt32
    shi503_path: Windows.Win32.Foundation.PWSTR
    shi503_passwd: Windows.Win32.Foundation.PWSTR
    shi503_servername: Windows.Win32.Foundation.PWSTR
    shi503_reserved: UInt32
    shi503_security_descriptor: Windows.Win32.Security.PSECURITY_DESCRIPTOR
SHARE_INFO_PERMISSIONS = UInt32
ACCESS_READ: SHARE_INFO_PERMISSIONS = 1
ACCESS_WRITE: SHARE_INFO_PERMISSIONS = 2
ACCESS_CREATE: SHARE_INFO_PERMISSIONS = 4
ACCESS_EXEC: SHARE_INFO_PERMISSIONS = 8
ACCESS_DELETE: SHARE_INFO_PERMISSIONS = 16
ACCESS_ATRIB: SHARE_INFO_PERMISSIONS = 32
ACCESS_PERM: SHARE_INFO_PERMISSIONS = 64
ACCESS_ALL: SHARE_INFO_PERMISSIONS = 32768
SHARE_TYPE = UInt32
STYPE_DISKTREE: SHARE_TYPE = 0
STYPE_PRINTQ: SHARE_TYPE = 1
STYPE_DEVICE: SHARE_TYPE = 2
STYPE_IPC: SHARE_TYPE = 3
STYPE_SPECIAL: SHARE_TYPE = 2147483648
STYPE_TEMPORARY: SHARE_TYPE = 1073741824
STYPE_MASK: SHARE_TYPE = 255
class STAT_SERVER_0(Structure):
    sts0_start: UInt32
    sts0_fopens: UInt32
    sts0_devopens: UInt32
    sts0_jobsqueued: UInt32
    sts0_sopens: UInt32
    sts0_stimedout: UInt32
    sts0_serrorout: UInt32
    sts0_pwerrors: UInt32
    sts0_permerrors: UInt32
    sts0_syserrors: UInt32
    sts0_bytessent_low: UInt32
    sts0_bytessent_high: UInt32
    sts0_bytesrcvd_low: UInt32
    sts0_bytesrcvd_high: UInt32
    sts0_avresponse: UInt32
    sts0_reqbufneed: UInt32
    sts0_bigbufneed: UInt32
class STAT_WORKSTATION_0(Structure):
    StatisticsStartTime: Windows.Win32.Foundation.LARGE_INTEGER
    BytesReceived: Windows.Win32.Foundation.LARGE_INTEGER
    SmbsReceived: Windows.Win32.Foundation.LARGE_INTEGER
    PagingReadBytesRequested: Windows.Win32.Foundation.LARGE_INTEGER
    NonPagingReadBytesRequested: Windows.Win32.Foundation.LARGE_INTEGER
    CacheReadBytesRequested: Windows.Win32.Foundation.LARGE_INTEGER
    NetworkReadBytesRequested: Windows.Win32.Foundation.LARGE_INTEGER
    BytesTransmitted: Windows.Win32.Foundation.LARGE_INTEGER
    SmbsTransmitted: Windows.Win32.Foundation.LARGE_INTEGER
    PagingWriteBytesRequested: Windows.Win32.Foundation.LARGE_INTEGER
    NonPagingWriteBytesRequested: Windows.Win32.Foundation.LARGE_INTEGER
    CacheWriteBytesRequested: Windows.Win32.Foundation.LARGE_INTEGER
    NetworkWriteBytesRequested: Windows.Win32.Foundation.LARGE_INTEGER
    InitiallyFailedOperations: UInt32
    FailedCompletionOperations: UInt32
    ReadOperations: UInt32
    RandomReadOperations: UInt32
    ReadSmbs: UInt32
    LargeReadSmbs: UInt32
    SmallReadSmbs: UInt32
    WriteOperations: UInt32
    RandomWriteOperations: UInt32
    WriteSmbs: UInt32
    LargeWriteSmbs: UInt32
    SmallWriteSmbs: UInt32
    RawReadsDenied: UInt32
    RawWritesDenied: UInt32
    NetworkErrors: UInt32
    Sessions: UInt32
    FailedSessions: UInt32
    Reconnects: UInt32
    CoreConnects: UInt32
    Lanman20Connects: UInt32
    Lanman21Connects: UInt32
    LanmanNtConnects: UInt32
    ServerDisconnects: UInt32
    HungSessions: UInt32
    UseCount: UInt32
    FailedUseCount: UInt32
    CurrentCommands: UInt32
STORAGE_BUS_TYPE = Int32
STORAGE_BUS_TYPE_BusTypeUnknown: STORAGE_BUS_TYPE = 0
STORAGE_BUS_TYPE_BusTypeScsi: STORAGE_BUS_TYPE = 1
STORAGE_BUS_TYPE_BusTypeAtapi: STORAGE_BUS_TYPE = 2
STORAGE_BUS_TYPE_BusTypeAta: STORAGE_BUS_TYPE = 3
STORAGE_BUS_TYPE_BusType1394: STORAGE_BUS_TYPE = 4
STORAGE_BUS_TYPE_BusTypeSsa: STORAGE_BUS_TYPE = 5
STORAGE_BUS_TYPE_BusTypeFibre: STORAGE_BUS_TYPE = 6
STORAGE_BUS_TYPE_BusTypeUsb: STORAGE_BUS_TYPE = 7
STORAGE_BUS_TYPE_BusTypeRAID: STORAGE_BUS_TYPE = 8
STORAGE_BUS_TYPE_BusTypeiScsi: STORAGE_BUS_TYPE = 9
STORAGE_BUS_TYPE_BusTypeSas: STORAGE_BUS_TYPE = 10
STORAGE_BUS_TYPE_BusTypeSata: STORAGE_BUS_TYPE = 11
STORAGE_BUS_TYPE_BusTypeSd: STORAGE_BUS_TYPE = 12
STORAGE_BUS_TYPE_BusTypeMmc: STORAGE_BUS_TYPE = 13
STORAGE_BUS_TYPE_BusTypeVirtual: STORAGE_BUS_TYPE = 14
STORAGE_BUS_TYPE_BusTypeFileBackedVirtual: STORAGE_BUS_TYPE = 15
STORAGE_BUS_TYPE_BusTypeSpaces: STORAGE_BUS_TYPE = 16
STORAGE_BUS_TYPE_BusTypeNvme: STORAGE_BUS_TYPE = 17
STORAGE_BUS_TYPE_BusTypeSCM: STORAGE_BUS_TYPE = 18
STORAGE_BUS_TYPE_BusTypeUfs: STORAGE_BUS_TYPE = 19
STORAGE_BUS_TYPE_BusTypeMax: STORAGE_BUS_TYPE = 20
STORAGE_BUS_TYPE_BusTypeMaxReserved: STORAGE_BUS_TYPE = 127
STREAM_INFO_LEVELS = Int32
STREAM_INFO_LEVELS_FindStreamInfoStandard: STREAM_INFO_LEVELS = 0
STREAM_INFO_LEVELS_FindStreamInfoMaxInfoLevel: STREAM_INFO_LEVELS = 1
SYMBOLIC_LINK_FLAGS = UInt32
SYMBOLIC_LINK_FLAG_DIRECTORY: SYMBOLIC_LINK_FLAGS = 1
SYMBOLIC_LINK_FLAG_ALLOW_UNPRIVILEGED_CREATE: SYMBOLIC_LINK_FLAGS = 2
TAPEMARK_TYPE = Int32
TAPE_FILEMARKS: TAPEMARK_TYPE = 1
TAPE_LONG_FILEMARKS: TAPEMARK_TYPE = 3
TAPE_SETMARKS: TAPEMARK_TYPE = 0
TAPE_SHORT_FILEMARKS: TAPEMARK_TYPE = 2
class TAPE_ERASE(Structure):
    Type: Windows.Win32.Storage.FileSystem.ERASE_TAPE_TYPE
    Immediate: Windows.Win32.Foundation.BOOLEAN
class TAPE_GET_POSITION(Structure):
    Type: Windows.Win32.Storage.FileSystem.TAPE_POSITION_TYPE
    Partition: UInt32
    Offset: Windows.Win32.Foundation.LARGE_INTEGER
TAPE_INFORMATION_TYPE = UInt32
SET_TAPE_DRIVE_INFORMATION: TAPE_INFORMATION_TYPE = 1
SET_TAPE_MEDIA_INFORMATION: TAPE_INFORMATION_TYPE = 0
TAPE_POSITION_METHOD = Int32
TAPE_ABSOLUTE_BLOCK: TAPE_POSITION_METHOD = 1
TAPE_LOGICAL_BLOCK: TAPE_POSITION_METHOD = 2
TAPE_REWIND: TAPE_POSITION_METHOD = 0
TAPE_SPACE_END_OF_DATA: TAPE_POSITION_METHOD = 4
TAPE_SPACE_FILEMARKS: TAPE_POSITION_METHOD = 6
TAPE_SPACE_RELATIVE_BLOCKS: TAPE_POSITION_METHOD = 5
TAPE_SPACE_SEQUENTIAL_FMKS: TAPE_POSITION_METHOD = 7
TAPE_SPACE_SEQUENTIAL_SMKS: TAPE_POSITION_METHOD = 9
TAPE_SPACE_SETMARKS: TAPE_POSITION_METHOD = 8
TAPE_POSITION_TYPE = Int32
TAPE_ABSOLUTE_POSITION: TAPE_POSITION_TYPE = 0
TAPE_LOGICAL_POSITION: TAPE_POSITION_TYPE = 1
class TAPE_PREPARE(Structure):
    Operation: Windows.Win32.Storage.FileSystem.PREPARE_TAPE_OPERATION
    Immediate: Windows.Win32.Foundation.BOOLEAN
class TAPE_SET_POSITION(Structure):
    Method: Windows.Win32.Storage.FileSystem.TAPE_POSITION_METHOD
    Partition: UInt32
    Offset: Windows.Win32.Foundation.LARGE_INTEGER
    Immediate: Windows.Win32.Foundation.BOOLEAN
class TAPE_WRITE_MARKS(Structure):
    Type: Windows.Win32.Storage.FileSystem.TAPEMARK_TYPE
    Count: UInt32
    Immediate: Windows.Win32.Foundation.BOOLEAN
class TRANSACTION_NOTIFICATION(Structure):
    TransactionKey: c_void_p
    TransactionNotification: UInt32
    TmVirtualClock: Windows.Win32.Foundation.LARGE_INTEGER
    ArgumentLength: UInt32
class TRANSACTION_NOTIFICATION_MARSHAL_ARGUMENT(Structure):
    MarshalCookie: UInt32
    UOW: Guid
class TRANSACTION_NOTIFICATION_PROPAGATE_ARGUMENT(Structure):
    PropagationCookie: UInt32
    UOW: Guid
    TmIdentity: Guid
    BufferLength: UInt32
class TRANSACTION_NOTIFICATION_RECOVERY_ARGUMENT(Structure):
    EnlistmentId: Guid
    UOW: Guid
class TRANSACTION_NOTIFICATION_SAVEPOINT_ARGUMENT(Structure):
    SavepointId: UInt32
class TRANSACTION_NOTIFICATION_TM_ONLINE_ARGUMENT(Structure):
    TmIdentity: Guid
    Flags: UInt32
TRANSACTION_OUTCOME = Int32
TRANSACTION_OUTCOME_TransactionOutcomeUndetermined: TRANSACTION_OUTCOME = 1
TRANSACTION_OUTCOME_TransactionOutcomeCommitted: TRANSACTION_OUTCOME = 2
TRANSACTION_OUTCOME_TransactionOutcomeAborted: TRANSACTION_OUTCOME = 3
TXFS_MINIVERSION = UInt32
TXFS_MINIVERSION_COMMITTED_VIEW: TXFS_MINIVERSION = 0
TXFS_MINIVERSION_DIRTY_VIEW: TXFS_MINIVERSION = 65535
TXFS_MINIVERSION_DEFAULT_VIEW: TXFS_MINIVERSION = 65534
class TXF_ID(Structure):
    Anonymous: _Anonymous_e__Struct
    _pack_ = 4
    class _Anonymous_e__Struct(Structure):
        LowPart: Int64
        HighPart: Int64
        _pack_ = 4
class TXF_LOG_RECORD_AFFECTED_FILE(Structure):
    Version: UInt16
    RecordLength: UInt32
    Flags: UInt32
    TxfFileId: Windows.Win32.Storage.FileSystem.TXF_ID
    KtmGuid: Guid
    FileNameLength: UInt32
    FileNameByteOffsetInStructure: UInt32
    _pack_ = 4
class TXF_LOG_RECORD_BASE(Structure):
    Version: UInt16
    RecordType: Windows.Win32.Storage.FileSystem.TXF_LOG_RECORD_TYPE
    RecordLength: UInt32
    _pack_ = 4
class TXF_LOG_RECORD_TRUNCATE(Structure):
    Version: UInt16
    RecordType: UInt16
    RecordLength: UInt32
    Flags: UInt32
    TxfFileId: Windows.Win32.Storage.FileSystem.TXF_ID
    KtmGuid: Guid
    NewFileSize: Int64
    FileNameLength: UInt32
    FileNameByteOffsetInStructure: UInt32
    _pack_ = 4
TXF_LOG_RECORD_TYPE = UInt16
TXF_LOG_RECORD_TYPE_AFFECTED_FILE: TXF_LOG_RECORD_TYPE = 4
TXF_LOG_RECORD_TYPE_TRUNCATE: TXF_LOG_RECORD_TYPE = 2
TXF_LOG_RECORD_TYPE_WRITE: TXF_LOG_RECORD_TYPE = 1
class TXF_LOG_RECORD_WRITE(Structure):
    Version: UInt16
    RecordType: UInt16
    RecordLength: UInt32
    Flags: UInt32
    TxfFileId: Windows.Win32.Storage.FileSystem.TXF_ID
    KtmGuid: Guid
    ByteOffsetInFile: Int64
    NumBytesWritten: UInt32
    ByteOffsetInStructure: UInt32
    FileNameLength: UInt32
    FileNameByteOffsetInStructure: UInt32
    _pack_ = 4
VER_FIND_FILE_FLAGS = UInt32
VFFF_ISSHAREDFILE: VER_FIND_FILE_FLAGS = 1
VER_FIND_FILE_STATUS = UInt32
VFF_CURNEDEST: VER_FIND_FILE_STATUS = 1
VFF_FILEINUSE: VER_FIND_FILE_STATUS = 2
VFF_BUFFTOOSMALL: VER_FIND_FILE_STATUS = 4
VER_INSTALL_FILE_FLAGS = UInt32
VIFF_FORCEINSTALL: VER_INSTALL_FILE_FLAGS = 1
VIFF_DONTDELETEOLD: VER_INSTALL_FILE_FLAGS = 2
VER_INSTALL_FILE_STATUS = UInt32
VIF_TEMPFILE: VER_INSTALL_FILE_STATUS = 1
VIF_MISMATCH: VER_INSTALL_FILE_STATUS = 2
VIF_SRCOLD: VER_INSTALL_FILE_STATUS = 4
VIF_DIFFLANG: VER_INSTALL_FILE_STATUS = 8
VIF_DIFFCODEPG: VER_INSTALL_FILE_STATUS = 16
VIF_DIFFTYPE: VER_INSTALL_FILE_STATUS = 32
VIF_WRITEPROT: VER_INSTALL_FILE_STATUS = 64
VIF_FILEINUSE: VER_INSTALL_FILE_STATUS = 128
VIF_OUTOFSPACE: VER_INSTALL_FILE_STATUS = 256
VIF_ACCESSVIOLATION: VER_INSTALL_FILE_STATUS = 512
VIF_SHARINGVIOLATION: VER_INSTALL_FILE_STATUS = 1024
VIF_CANNOTCREATE: VER_INSTALL_FILE_STATUS = 2048
VIF_CANNOTDELETE: VER_INSTALL_FILE_STATUS = 4096
VIF_CANNOTRENAME: VER_INSTALL_FILE_STATUS = 8192
VIF_CANNOTDELETECUR: VER_INSTALL_FILE_STATUS = 16384
VIF_OUTOFMEMORY: VER_INSTALL_FILE_STATUS = 32768
VIF_CANNOTREADSRC: VER_INSTALL_FILE_STATUS = 65536
VIF_CANNOTREADDST: VER_INSTALL_FILE_STATUS = 131072
VIF_BUFFTOOSMALL: VER_INSTALL_FILE_STATUS = 262144
VIF_CANNOTLOADLZ32: VER_INSTALL_FILE_STATUS = 524288
VIF_CANNOTLOADCABINET: VER_INSTALL_FILE_STATUS = 1048576
class VOLUME_ALLOCATE_BC_STREAM_INPUT(Structure):
    Version: UInt32
    RequestsPerPeriod: UInt32
    Period: UInt32
    RetryFailures: Windows.Win32.Foundation.BOOLEAN
    Discardable: Windows.Win32.Foundation.BOOLEAN
    Reserved1: Windows.Win32.Foundation.BOOLEAN * 2
    LowestByteOffset: UInt64
    HighestByteOffset: UInt64
    AccessType: UInt32
    AccessMode: UInt32
class VOLUME_ALLOCATE_BC_STREAM_OUTPUT(Structure):
    RequestSize: UInt64
    NumOutStandingRequests: UInt32
class VOLUME_ALLOCATION_HINT_INPUT(Structure):
    ClusterSize: UInt32
    NumberOfClusters: UInt32
    StartingClusterNumber: Int64
class VOLUME_ALLOCATION_HINT_OUTPUT(Structure):
    Bitmap: UInt32 * 1
class VOLUME_CRITICAL_IO(Structure):
    AccessType: UInt32
    ExtentsCount: UInt32
    Extents: Windows.Win32.Storage.FileSystem.FILE_EXTENT * 1
class VOLUME_FAILOVER_SET(Structure):
    NumberOfDisks: UInt32
    DiskNumbers: UInt32 * 1
class VOLUME_GET_BC_PROPERTIES_INPUT(Structure):
    Version: UInt32
    Reserved1: UInt32
    LowestByteOffset: UInt64
    HighestByteOffset: UInt64
    AccessType: UInt32
    AccessMode: UInt32
class VOLUME_GET_BC_PROPERTIES_OUTPUT(Structure):
    MaximumRequestsPerPeriod: UInt32
    MinimumPeriod: UInt32
    MaximumRequestSize: UInt64
    EstimatedTimePerRequest: UInt32
    NumOutStandingRequests: UInt32
    RequestSize: UInt64
class VOLUME_LOGICAL_OFFSET(Structure):
    LogicalOffset: Int64
class VOLUME_NUMBER(Structure):
    VolumeNumber: UInt32
    VolumeManagerName: Char * 8
class VOLUME_PHYSICAL_OFFSET(Structure):
    DiskNumber: UInt32
    Offset: Int64
class VOLUME_PHYSICAL_OFFSETS(Structure):
    NumberOfPhysicalOffsets: UInt32
    PhysicalOffset: Windows.Win32.Storage.FileSystem.VOLUME_PHYSICAL_OFFSET * 1
class VOLUME_READ_PLEX_INPUT(Structure):
    ByteOffset: Windows.Win32.Foundation.LARGE_INTEGER
    Length: UInt32
    PlexNumber: UInt32
class VOLUME_SET_GPT_ATTRIBUTES_INFORMATION(Structure):
    GptAttributes: UInt64
    RevertOnClose: Windows.Win32.Foundation.BOOLEAN
    ApplyToAllConnectedVolumes: Windows.Win32.Foundation.BOOLEAN
    Reserved1: UInt16
    Reserved2: UInt32
class VOLUME_SHRINK_INFO(Structure):
    VolumeSize: UInt64
class VS_FIXEDFILEINFO(Structure):
    dwSignature: UInt32
    dwStrucVersion: UInt32
    dwFileVersionMS: UInt32
    dwFileVersionLS: UInt32
    dwProductVersionMS: UInt32
    dwProductVersionLS: UInt32
    dwFileFlagsMask: UInt32
    dwFileFlags: Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_FLAGS
    dwFileOS: Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_OS
    dwFileType: Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_TYPE
    dwFileSubtype: Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_SUBTYPE
    dwFileDateMS: UInt32
    dwFileDateLS: UInt32
VS_FIXEDFILEINFO_FILE_FLAGS = UInt32
VS_FF_DEBUG: VS_FIXEDFILEINFO_FILE_FLAGS = 1
VS_FF_PRERELEASE: VS_FIXEDFILEINFO_FILE_FLAGS = 2
VS_FF_PATCHED: VS_FIXEDFILEINFO_FILE_FLAGS = 4
VS_FF_PRIVATEBUILD: VS_FIXEDFILEINFO_FILE_FLAGS = 8
VS_FF_INFOINFERRED: VS_FIXEDFILEINFO_FILE_FLAGS = 16
VS_FF_SPECIALBUILD: VS_FIXEDFILEINFO_FILE_FLAGS = 32
VS_FIXEDFILEINFO_FILE_OS = Int32
VOS_UNKNOWN: VS_FIXEDFILEINFO_FILE_OS = 0
VOS_DOS: VS_FIXEDFILEINFO_FILE_OS = 65536
VOS_OS216: VS_FIXEDFILEINFO_FILE_OS = 131072
VOS_OS232: VS_FIXEDFILEINFO_FILE_OS = 196608
VOS_NT: VS_FIXEDFILEINFO_FILE_OS = 262144
VOS_WINCE: VS_FIXEDFILEINFO_FILE_OS = 327680
VOS__BASE: VS_FIXEDFILEINFO_FILE_OS = 0
VOS__WINDOWS16: VS_FIXEDFILEINFO_FILE_OS = 1
VOS__PM16: VS_FIXEDFILEINFO_FILE_OS = 2
VOS__PM32: VS_FIXEDFILEINFO_FILE_OS = 3
VOS__WINDOWS32: VS_FIXEDFILEINFO_FILE_OS = 4
VOS_DOS_WINDOWS16: VS_FIXEDFILEINFO_FILE_OS = 65537
VOS_DOS_WINDOWS32: VS_FIXEDFILEINFO_FILE_OS = 65540
VOS_OS216_PM16: VS_FIXEDFILEINFO_FILE_OS = 131074
VOS_OS232_PM32: VS_FIXEDFILEINFO_FILE_OS = 196611
VOS_NT_WINDOWS32: VS_FIXEDFILEINFO_FILE_OS = 262148
VS_FIXEDFILEINFO_FILE_SUBTYPE = Int32
VFT2_UNKNOWN: VS_FIXEDFILEINFO_FILE_SUBTYPE = 0
VFT2_DRV_PRINTER: VS_FIXEDFILEINFO_FILE_SUBTYPE = 1
VFT2_DRV_KEYBOARD: VS_FIXEDFILEINFO_FILE_SUBTYPE = 2
VFT2_DRV_LANGUAGE: VS_FIXEDFILEINFO_FILE_SUBTYPE = 3
VFT2_DRV_DISPLAY: VS_FIXEDFILEINFO_FILE_SUBTYPE = 4
VFT2_DRV_MOUSE: VS_FIXEDFILEINFO_FILE_SUBTYPE = 5
VFT2_DRV_NETWORK: VS_FIXEDFILEINFO_FILE_SUBTYPE = 6
VFT2_DRV_SYSTEM: VS_FIXEDFILEINFO_FILE_SUBTYPE = 7
VFT2_DRV_INSTALLABLE: VS_FIXEDFILEINFO_FILE_SUBTYPE = 8
VFT2_DRV_SOUND: VS_FIXEDFILEINFO_FILE_SUBTYPE = 9
VFT2_DRV_COMM: VS_FIXEDFILEINFO_FILE_SUBTYPE = 10
VFT2_DRV_INPUTMETHOD: VS_FIXEDFILEINFO_FILE_SUBTYPE = 11
VFT2_DRV_VERSIONED_PRINTER: VS_FIXEDFILEINFO_FILE_SUBTYPE = 12
VFT2_FONT_RASTER: VS_FIXEDFILEINFO_FILE_SUBTYPE = 1
VFT2_FONT_VECTOR: VS_FIXEDFILEINFO_FILE_SUBTYPE = 2
VFT2_FONT_TRUETYPE: VS_FIXEDFILEINFO_FILE_SUBTYPE = 3
VS_FIXEDFILEINFO_FILE_TYPE = Int32
VFT_UNKNOWN: VS_FIXEDFILEINFO_FILE_TYPE = 0
VFT_APP: VS_FIXEDFILEINFO_FILE_TYPE = 1
VFT_DLL: VS_FIXEDFILEINFO_FILE_TYPE = 2
VFT_DRV: VS_FIXEDFILEINFO_FILE_TYPE = 3
VFT_FONT: VS_FIXEDFILEINFO_FILE_TYPE = 4
VFT_VXD: VS_FIXEDFILEINFO_FILE_TYPE = 5
VFT_STATIC_LIB: VS_FIXEDFILEINFO_FILE_TYPE = 7
class WIM_ENTRY_INFO(Structure):
    WimEntryInfoSize: UInt32
    WimType: UInt32
    DataSourceId: Windows.Win32.Foundation.LARGE_INTEGER
    WimGuid: Guid
    WimPath: Windows.Win32.Foundation.PWSTR
    WimIndex: UInt32
    Flags: UInt32
class WIM_EXTERNAL_FILE_INFO(Structure):
    DataSourceId: Windows.Win32.Foundation.LARGE_INTEGER
    ResourceHash: Byte * 20
    Flags: UInt32
class WIN32_FILE_ATTRIBUTE_DATA(Structure):
    dwFileAttributes: UInt32
    ftCreationTime: Windows.Win32.Foundation.FILETIME
    ftLastAccessTime: Windows.Win32.Foundation.FILETIME
    ftLastWriteTime: Windows.Win32.Foundation.FILETIME
    nFileSizeHigh: UInt32
    nFileSizeLow: UInt32
class WIN32_FIND_DATAA(Structure):
    dwFileAttributes: UInt32
    ftCreationTime: Windows.Win32.Foundation.FILETIME
    ftLastAccessTime: Windows.Win32.Foundation.FILETIME
    ftLastWriteTime: Windows.Win32.Foundation.FILETIME
    nFileSizeHigh: UInt32
    nFileSizeLow: UInt32
    dwReserved0: UInt32
    dwReserved1: UInt32
    cFileName: Windows.Win32.Foundation.CHAR * 260
    cAlternateFileName: Windows.Win32.Foundation.CHAR * 14
class WIN32_FIND_DATAW(Structure):
    dwFileAttributes: UInt32
    ftCreationTime: Windows.Win32.Foundation.FILETIME
    ftLastAccessTime: Windows.Win32.Foundation.FILETIME
    ftLastWriteTime: Windows.Win32.Foundation.FILETIME
    nFileSizeHigh: UInt32
    nFileSizeLow: UInt32
    dwReserved0: UInt32
    dwReserved1: UInt32
    cFileName: Char * 260
    cAlternateFileName: Char * 14
class WIN32_FIND_STREAM_DATA(Structure):
    StreamSize: Windows.Win32.Foundation.LARGE_INTEGER
    cStreamName: Char * 296
class WIN32_STREAM_ID(Structure):
    dwStreamId: Windows.Win32.Storage.FileSystem.WIN_STREAM_ID
    dwStreamAttributes: UInt32
    Size: Windows.Win32.Foundation.LARGE_INTEGER
    dwStreamNameSize: UInt32
    cStreamName: Char * 1
WIN_STREAM_ID = UInt32
BACKUP_ALTERNATE_DATA: WIN_STREAM_ID = 4
BACKUP_DATA: WIN_STREAM_ID = 1
BACKUP_EA_DATA: WIN_STREAM_ID = 2
BACKUP_LINK: WIN_STREAM_ID = 5
BACKUP_OBJECT_ID: WIN_STREAM_ID = 7
BACKUP_PROPERTY_DATA: WIN_STREAM_ID = 6
BACKUP_REPARSE_DATA: WIN_STREAM_ID = 8
BACKUP_SECURITY_DATA: WIN_STREAM_ID = 3
BACKUP_SPARSE_BLOCK: WIN_STREAM_ID = 9
BACKUP_TXFS_DATA: WIN_STREAM_ID = 10
class WOF_FILE_COMPRESSION_INFO_V0(Structure):
    Algorithm: UInt32
class WOF_FILE_COMPRESSION_INFO_V1(Structure):
    Algorithm: UInt32
    Flags: UInt32
@winfunctype_pointer
def WofEnumEntryProc(EntryInfo: c_void_p, UserData: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def WofEnumFilesProc(FilePath: Windows.Win32.Foundation.PWSTR, ExternalFileInfo: c_void_p, UserData: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
make_head(_module, 'BY_HANDLE_FILE_INFORMATION')
make_head(_module, 'CACHE_ACCESS_CHECK')
make_head(_module, 'CACHE_DESTROY_CALLBACK')
make_head(_module, 'CACHE_KEY_COMPARE')
make_head(_module, 'CACHE_KEY_HASH')
make_head(_module, 'CACHE_READ_CALLBACK')
make_head(_module, 'CLAIMMEDIALABEL')
make_head(_module, 'CLAIMMEDIALABELEX')
make_head(_module, 'CLFS_BLOCK_ALLOCATION')
make_head(_module, 'CLFS_BLOCK_DEALLOCATION')
make_head(_module, 'CLFS_LOG_NAME_INFORMATION')
make_head(_module, 'CLFS_MGMT_NOTIFICATION')
make_head(_module, 'CLFS_MGMT_POLICY')
make_head(_module, 'CLFS_NODE_ID')
make_head(_module, 'CLFS_PHYSICAL_LSN_INFORMATION')
make_head(_module, 'CLFS_STREAM_ID_INFORMATION')
make_head(_module, 'CLS_ARCHIVE_DESCRIPTOR')
make_head(_module, 'CLS_CONTAINER_INFORMATION')
make_head(_module, 'CLS_INFORMATION')
make_head(_module, 'CLS_IO_STATISTICS')
make_head(_module, 'CLS_IO_STATISTICS_HEADER')
make_head(_module, 'CLS_LSN')
make_head(_module, 'CLS_SCAN_CONTEXT')
make_head(_module, 'CLS_WRITE_ENTRY')
make_head(_module, 'CONNECTION_INFO_0')
make_head(_module, 'CONNECTION_INFO_1')
make_head(_module, 'COPYFILE2_EXTENDED_PARAMETERS')
make_head(_module, 'COPYFILE2_EXTENDED_PARAMETERS_V2')
make_head(_module, 'COPYFILE2_MESSAGE')
make_head(_module, 'CREATEFILE2_EXTENDED_PARAMETERS')
make_head(_module, 'DISKQUOTA_USER_INFORMATION')
make_head(_module, 'DISK_SPACE_INFORMATION')
make_head(_module, 'EFS_CERTIFICATE_BLOB')
make_head(_module, 'EFS_COMPATIBILITY_INFO')
make_head(_module, 'EFS_DECRYPTION_STATUS_INFO')
make_head(_module, 'EFS_ENCRYPTION_STATUS_INFO')
make_head(_module, 'EFS_HASH_BLOB')
make_head(_module, 'EFS_KEY_INFO')
make_head(_module, 'EFS_PIN_BLOB')
make_head(_module, 'EFS_RPC_BLOB')
make_head(_module, 'EFS_VERSION_INFO')
make_head(_module, 'ENCRYPTED_FILE_METADATA_SIGNATURE')
make_head(_module, 'ENCRYPTION_CERTIFICATE')
make_head(_module, 'ENCRYPTION_CERTIFICATE_HASH')
make_head(_module, 'ENCRYPTION_CERTIFICATE_HASH_LIST')
make_head(_module, 'ENCRYPTION_CERTIFICATE_LIST')
make_head(_module, 'ENCRYPTION_PROTECTOR')
make_head(_module, 'ENCRYPTION_PROTECTOR_LIST')
make_head(_module, 'FCACHE_CREATE_CALLBACK')
make_head(_module, 'FCACHE_RICHCREATE_CALLBACK')
make_head(_module, 'FH_OVERLAPPED')
make_head(_module, 'FILE_ALIGNMENT_INFO')
make_head(_module, 'FILE_ALLOCATION_INFO')
make_head(_module, 'FILE_ATTRIBUTE_TAG_INFO')
make_head(_module, 'FILE_BASIC_INFO')
make_head(_module, 'FILE_COMPRESSION_INFO')
make_head(_module, 'FILE_DISPOSITION_INFO')
make_head(_module, 'FILE_END_OF_FILE_INFO')
make_head(_module, 'FILE_EXTENT')
make_head(_module, 'FILE_FULL_DIR_INFO')
make_head(_module, 'FILE_ID_128')
make_head(_module, 'FILE_ID_BOTH_DIR_INFO')
make_head(_module, 'FILE_ID_DESCRIPTOR')
make_head(_module, 'FILE_ID_EXTD_DIR_INFO')
make_head(_module, 'FILE_ID_INFO')
make_head(_module, 'FILE_INFO_2')
make_head(_module, 'FILE_INFO_3')
make_head(_module, 'FILE_IO_PRIORITY_HINT_INFO')
make_head(_module, 'FILE_NAME_INFO')
make_head(_module, 'FILE_NOTIFY_EXTENDED_INFORMATION')
make_head(_module, 'FILE_NOTIFY_INFORMATION')
make_head(_module, 'FILE_REMOTE_PROTOCOL_INFO')
make_head(_module, 'FILE_RENAME_INFO')
make_head(_module, 'FILE_SEGMENT_ELEMENT')
make_head(_module, 'FILE_STANDARD_INFO')
make_head(_module, 'FILE_STORAGE_INFO')
make_head(_module, 'FILE_STREAM_INFO')
make_head(_module, 'FIO_CONTEXT')
make_head(_module, 'HIORING__')
make_head(_module, 'IDiskQuotaControl')
make_head(_module, 'IDiskQuotaEvents')
make_head(_module, 'IDiskQuotaUser')
make_head(_module, 'IDiskQuotaUserBatch')
make_head(_module, 'IEnumDiskQuotaUsers')
make_head(_module, 'IORING_BUFFER_INFO')
make_head(_module, 'IORING_BUFFER_REF')
make_head(_module, 'IORING_CAPABILITIES')
make_head(_module, 'IORING_CQE')
make_head(_module, 'IORING_CREATE_FLAGS')
make_head(_module, 'IORING_HANDLE_REF')
make_head(_module, 'IORING_INFO')
make_head(_module, 'IORING_REGISTERED_BUFFER')
make_head(_module, 'KCRM_MARSHAL_HEADER')
make_head(_module, 'KCRM_PROTOCOL_BLOB')
make_head(_module, 'KCRM_TRANSACTION_BLOB')
make_head(_module, 'LOG_MANAGEMENT_CALLBACKS')
make_head(_module, 'LPPROGRESS_ROUTINE')
make_head(_module, 'MAXMEDIALABEL')
make_head(_module, 'MediaLabelInfo')
make_head(_module, 'NAME_CACHE_CONTEXT')
make_head(_module, 'NTMS_ALLOCATION_INFORMATION')
make_head(_module, 'NTMS_ASYNC_IO')
make_head(_module, 'NTMS_CHANGERINFORMATIONA')
make_head(_module, 'NTMS_CHANGERINFORMATIONW')
make_head(_module, 'NTMS_CHANGERTYPEINFORMATIONA')
make_head(_module, 'NTMS_CHANGERTYPEINFORMATIONW')
make_head(_module, 'NTMS_COMPUTERINFORMATION')
make_head(_module, 'NTMS_DRIVEINFORMATIONA')
make_head(_module, 'NTMS_DRIVEINFORMATIONW')
make_head(_module, 'NTMS_DRIVETYPEINFORMATIONA')
make_head(_module, 'NTMS_DRIVETYPEINFORMATIONW')
make_head(_module, 'NTMS_FILESYSTEM_INFO')
make_head(_module, 'NTMS_I1_LIBRARYINFORMATION')
make_head(_module, 'NTMS_I1_LIBREQUESTINFORMATIONA')
make_head(_module, 'NTMS_I1_LIBREQUESTINFORMATIONW')
make_head(_module, 'NTMS_I1_OBJECTINFORMATIONA')
make_head(_module, 'NTMS_I1_OBJECTINFORMATIONW')
make_head(_module, 'NTMS_I1_OPREQUESTINFORMATIONA')
make_head(_module, 'NTMS_I1_OPREQUESTINFORMATIONW')
make_head(_module, 'NTMS_I1_PARTITIONINFORMATIONA')
make_head(_module, 'NTMS_I1_PARTITIONINFORMATIONW')
make_head(_module, 'NTMS_I1_PMIDINFORMATIONA')
make_head(_module, 'NTMS_I1_PMIDINFORMATIONW')
make_head(_module, 'NTMS_IEDOORINFORMATION')
make_head(_module, 'NTMS_IEPORTINFORMATION')
make_head(_module, 'NTMS_LIBRARYINFORMATION')
make_head(_module, 'NTMS_LIBREQUESTINFORMATIONA')
make_head(_module, 'NTMS_LIBREQUESTINFORMATIONW')
make_head(_module, 'NTMS_LMIDINFORMATION')
make_head(_module, 'NTMS_MEDIAPOOLINFORMATION')
make_head(_module, 'NTMS_MEDIATYPEINFORMATION')
make_head(_module, 'NTMS_MOUNT_INFORMATION')
make_head(_module, 'NTMS_NOTIFICATIONINFORMATION')
make_head(_module, 'NTMS_OBJECTINFORMATIONA')
make_head(_module, 'NTMS_OBJECTINFORMATIONW')
make_head(_module, 'NTMS_OPREQUESTINFORMATIONA')
make_head(_module, 'NTMS_OPREQUESTINFORMATIONW')
make_head(_module, 'NTMS_PARTITIONINFORMATIONA')
make_head(_module, 'NTMS_PARTITIONINFORMATIONW')
make_head(_module, 'NTMS_PMIDINFORMATIONA')
make_head(_module, 'NTMS_PMIDINFORMATIONW')
make_head(_module, 'NTMS_STORAGESLOTINFORMATION')
make_head(_module, 'OFSTRUCT')
make_head(_module, 'PCLFS_COMPLETION_ROUTINE')
make_head(_module, 'PCOPYFILE2_PROGRESS_ROUTINE')
make_head(_module, 'PFE_EXPORT_FUNC')
make_head(_module, 'PFE_IMPORT_FUNC')
make_head(_module, 'PFN_IO_COMPLETION')
make_head(_module, 'PLOG_FULL_HANDLER_CALLBACK')
make_head(_module, 'PLOG_TAIL_ADVANCE_CALLBACK')
make_head(_module, 'PLOG_UNPINNED_CALLBACK')
make_head(_module, 'REPARSE_GUID_DATA_BUFFER')
make_head(_module, 'SERVER_ALIAS_INFO_0')
make_head(_module, 'SERVER_CERTIFICATE_INFO_0')
make_head(_module, 'SESSION_INFO_0')
make_head(_module, 'SESSION_INFO_1')
make_head(_module, 'SESSION_INFO_10')
make_head(_module, 'SESSION_INFO_2')
make_head(_module, 'SESSION_INFO_502')
make_head(_module, 'SHARE_INFO_0')
make_head(_module, 'SHARE_INFO_1')
make_head(_module, 'SHARE_INFO_1004')
make_head(_module, 'SHARE_INFO_1005')
make_head(_module, 'SHARE_INFO_1006')
make_head(_module, 'SHARE_INFO_1501')
make_head(_module, 'SHARE_INFO_1503')
make_head(_module, 'SHARE_INFO_2')
make_head(_module, 'SHARE_INFO_501')
make_head(_module, 'SHARE_INFO_502')
make_head(_module, 'SHARE_INFO_503')
make_head(_module, 'STAT_SERVER_0')
make_head(_module, 'STAT_WORKSTATION_0')
make_head(_module, 'TAPE_ERASE')
make_head(_module, 'TAPE_GET_POSITION')
make_head(_module, 'TAPE_PREPARE')
make_head(_module, 'TAPE_SET_POSITION')
make_head(_module, 'TAPE_WRITE_MARKS')
make_head(_module, 'TRANSACTION_NOTIFICATION')
make_head(_module, 'TRANSACTION_NOTIFICATION_MARSHAL_ARGUMENT')
make_head(_module, 'TRANSACTION_NOTIFICATION_PROPAGATE_ARGUMENT')
make_head(_module, 'TRANSACTION_NOTIFICATION_RECOVERY_ARGUMENT')
make_head(_module, 'TRANSACTION_NOTIFICATION_SAVEPOINT_ARGUMENT')
make_head(_module, 'TRANSACTION_NOTIFICATION_TM_ONLINE_ARGUMENT')
make_head(_module, 'TXF_ID')
make_head(_module, 'TXF_LOG_RECORD_AFFECTED_FILE')
make_head(_module, 'TXF_LOG_RECORD_BASE')
make_head(_module, 'TXF_LOG_RECORD_TRUNCATE')
make_head(_module, 'TXF_LOG_RECORD_WRITE')
make_head(_module, 'VOLUME_ALLOCATE_BC_STREAM_INPUT')
make_head(_module, 'VOLUME_ALLOCATE_BC_STREAM_OUTPUT')
make_head(_module, 'VOLUME_ALLOCATION_HINT_INPUT')
make_head(_module, 'VOLUME_ALLOCATION_HINT_OUTPUT')
make_head(_module, 'VOLUME_CRITICAL_IO')
make_head(_module, 'VOLUME_FAILOVER_SET')
make_head(_module, 'VOLUME_GET_BC_PROPERTIES_INPUT')
make_head(_module, 'VOLUME_GET_BC_PROPERTIES_OUTPUT')
make_head(_module, 'VOLUME_LOGICAL_OFFSET')
make_head(_module, 'VOLUME_NUMBER')
make_head(_module, 'VOLUME_PHYSICAL_OFFSET')
make_head(_module, 'VOLUME_PHYSICAL_OFFSETS')
make_head(_module, 'VOLUME_READ_PLEX_INPUT')
make_head(_module, 'VOLUME_SET_GPT_ATTRIBUTES_INFORMATION')
make_head(_module, 'VOLUME_SHRINK_INFO')
make_head(_module, 'VS_FIXEDFILEINFO')
make_head(_module, 'WIM_ENTRY_INFO')
make_head(_module, 'WIM_EXTERNAL_FILE_INFO')
make_head(_module, 'WIN32_FILE_ATTRIBUTE_DATA')
make_head(_module, 'WIN32_FIND_DATAA')
make_head(_module, 'WIN32_FIND_DATAW')
make_head(_module, 'WIN32_FIND_STREAM_DATA')
make_head(_module, 'WIN32_STREAM_ID')
make_head(_module, 'WOF_FILE_COMPRESSION_INFO_V0')
make_head(_module, 'WOF_FILE_COMPRESSION_INFO_V1')
make_head(_module, 'WofEnumEntryProc')
make_head(_module, 'WofEnumFilesProc')
__all__ = [
    "ACCESS_ALL",
    "ACCESS_ATRIB",
    "ACCESS_CREATE",
    "ACCESS_DELETE",
    "ACCESS_EXEC",
    "ACCESS_PERM",
    "ACCESS_READ",
    "ACCESS_WRITE",
    "AddLogContainer",
    "AddLogContainerSet",
    "AddUsersToEncryptedFile",
    "AdvanceLogBase",
    "AlignReservedLog",
    "AllocReservedLog",
    "AreFileApisANSI",
    "AreShortNamesEnabled",
    "BACKUP_ALTERNATE_DATA",
    "BACKUP_DATA",
    "BACKUP_EA_DATA",
    "BACKUP_LINK",
    "BACKUP_OBJECT_ID",
    "BACKUP_PROPERTY_DATA",
    "BACKUP_REPARSE_DATA",
    "BACKUP_SECURITY_DATA",
    "BACKUP_SPARSE_BLOCK",
    "BACKUP_TXFS_DATA",
    "BY_HANDLE_FILE_INFORMATION",
    "BackupRead",
    "BackupSeek",
    "BackupWrite",
    "BuildIoRingCancelRequest",
    "BuildIoRingReadFile",
    "BuildIoRingRegisterBuffers",
    "BuildIoRingRegisterFileHandles",
    "CACHE_ACCESS_CHECK",
    "CACHE_DESTROY_CALLBACK",
    "CACHE_KEY_COMPARE",
    "CACHE_KEY_HASH",
    "CACHE_READ_CALLBACK",
    "CALLBACK_CHUNK_FINISHED",
    "CALLBACK_STREAM_SWITCH",
    "CLAIMMEDIALABEL",
    "CLAIMMEDIALABELEX",
    "CLFS_BASELOG_EXTENSION",
    "CLFS_BLOCK_ALLOCATION",
    "CLFS_BLOCK_DEALLOCATION",
    "CLFS_CONTAINER_RELATIVE_PREFIX",
    "CLFS_CONTAINER_STREAM_PREFIX",
    "CLFS_CONTEXT_MODE",
    "CLFS_CONTEXT_MODE_ClfsContextForward",
    "CLFS_CONTEXT_MODE_ClfsContextNone",
    "CLFS_CONTEXT_MODE_ClfsContextPrevious",
    "CLFS_CONTEXT_MODE_ClfsContextUndoNext",
    "CLFS_FLAG",
    "CLFS_FLAG_FILTER_INTERMEDIATE_LEVEL",
    "CLFS_FLAG_FILTER_TOP_LEVEL",
    "CLFS_FLAG_FORCE_APPEND",
    "CLFS_FLAG_FORCE_FLUSH",
    "CLFS_FLAG_HIDDEN_SYSTEM_LOG",
    "CLFS_FLAG_IGNORE_SHARE_ACCESS",
    "CLFS_FLAG_MINIFILTER_LEVEL",
    "CLFS_FLAG_NON_REENTRANT_FILTER",
    "CLFS_FLAG_NO_FLAGS",
    "CLFS_FLAG_READ_IN_PROGRESS",
    "CLFS_FLAG_REENTRANT_FILE_SYSTEM",
    "CLFS_FLAG_REENTRANT_FILTER",
    "CLFS_FLAG_USE_RESERVATION",
    "CLFS_IOSTATS_CLASS",
    "CLFS_IOSTATS_CLASS_ClfsIoStatsDefault",
    "CLFS_IOSTATS_CLASS_ClfsIoStatsMax",
    "CLFS_LOG_ARCHIVE_MODE",
    "CLFS_LOG_ARCHIVE_MODE_ClfsLogArchiveDisabled",
    "CLFS_LOG_ARCHIVE_MODE_ClfsLogArchiveEnabled",
    "CLFS_LOG_NAME_INFORMATION",
    "CLFS_MARSHALLING_FLAG_DISABLE_BUFF_INIT",
    "CLFS_MARSHALLING_FLAG_NONE",
    "CLFS_MAX_CONTAINER_INFO",
    "CLFS_MGMT_CLIENT_REGISTRATION_VERSION",
    "CLFS_MGMT_NOTIFICATION",
    "CLFS_MGMT_NOTIFICATION_TYPE",
    "CLFS_MGMT_NOTIFICATION_TYPE_ClfsMgmtAdvanceTailNotification",
    "CLFS_MGMT_NOTIFICATION_TYPE_ClfsMgmtLogFullHandlerNotification",
    "CLFS_MGMT_NOTIFICATION_TYPE_ClfsMgmtLogUnpinnedNotification",
    "CLFS_MGMT_NOTIFICATION_TYPE_ClfsMgmtLogWriteNotification",
    "CLFS_MGMT_POLICY",
    "CLFS_MGMT_POLICY_TYPE",
    "CLFS_MGMT_POLICY_TYPE_ClfsMgmtPolicyAutoGrow",
    "CLFS_MGMT_POLICY_TYPE_ClfsMgmtPolicyAutoShrink",
    "CLFS_MGMT_POLICY_TYPE_ClfsMgmtPolicyGrowthRate",
    "CLFS_MGMT_POLICY_TYPE_ClfsMgmtPolicyInvalid",
    "CLFS_MGMT_POLICY_TYPE_ClfsMgmtPolicyLogTail",
    "CLFS_MGMT_POLICY_TYPE_ClfsMgmtPolicyMaximumSize",
    "CLFS_MGMT_POLICY_TYPE_ClfsMgmtPolicyMinimumSize",
    "CLFS_MGMT_POLICY_TYPE_ClfsMgmtPolicyNewContainerExtension",
    "CLFS_MGMT_POLICY_TYPE_ClfsMgmtPolicyNewContainerPrefix",
    "CLFS_MGMT_POLICY_TYPE_ClfsMgmtPolicyNewContainerSize",
    "CLFS_MGMT_POLICY_TYPE_ClfsMgmtPolicyNewContainerSuffix",
    "CLFS_MGMT_POLICY_VERSION",
    "CLFS_NODE_ID",
    "CLFS_PHYSICAL_LSN_INFORMATION",
    "CLFS_SCAN_BACKWARD",
    "CLFS_SCAN_BUFFERED",
    "CLFS_SCAN_CLOSE",
    "CLFS_SCAN_FORWARD",
    "CLFS_SCAN_INIT",
    "CLFS_SCAN_INITIALIZED",
    "CLFS_STREAM_ID_INFORMATION",
    "CLSID_DiskQuotaControl",
    "CLS_ARCHIVE_DESCRIPTOR",
    "CLS_CONTAINER_INFORMATION",
    "CLS_CONTEXT_MODE",
    "CLS_CONTEXT_MODE_ClsContextForward",
    "CLS_CONTEXT_MODE_ClsContextNone",
    "CLS_CONTEXT_MODE_ClsContextPrevious",
    "CLS_CONTEXT_MODE_ClsContextUndoNext",
    "CLS_INFORMATION",
    "CLS_IOSTATS_CLASS",
    "CLS_IOSTATS_CLASS_ClsIoStatsDefault",
    "CLS_IOSTATS_CLASS_ClsIoStatsMax",
    "CLS_IO_STATISTICS",
    "CLS_IO_STATISTICS_HEADER",
    "CLS_LOG_INFORMATION_CLASS",
    "CLS_LOG_INFORMATION_CLASS_ClfsLogBasicInformation",
    "CLS_LOG_INFORMATION_CLASS_ClfsLogBasicInformationPhysical",
    "CLS_LOG_INFORMATION_CLASS_ClfsLogPhysicalLsnInformation",
    "CLS_LOG_INFORMATION_CLASS_ClfsLogPhysicalNameInformation",
    "CLS_LOG_INFORMATION_CLASS_ClfsLogStreamIdentifierInformation",
    "CLS_LOG_INFORMATION_CLASS_ClfsLogSystemMarkingInformation",
    "CLS_LSN",
    "CLS_SCAN_CONTEXT",
    "CLS_WRITE_ENTRY",
    "COMPRESSION_FORMAT",
    "COMPRESSION_FORMAT_DEFAULT",
    "COMPRESSION_FORMAT_LZNT1",
    "COMPRESSION_FORMAT_NONE",
    "COMPRESSION_FORMAT_XP10",
    "COMPRESSION_FORMAT_XPRESS",
    "COMPRESSION_FORMAT_XPRESS_HUFF",
    "CONNECTION_INFO_0",
    "CONNECTION_INFO_1",
    "COPYFILE2_CALLBACK_CHUNK_FINISHED",
    "COPYFILE2_CALLBACK_CHUNK_STARTED",
    "COPYFILE2_CALLBACK_ERROR",
    "COPYFILE2_CALLBACK_MAX",
    "COPYFILE2_CALLBACK_NONE",
    "COPYFILE2_CALLBACK_POLL_CONTINUE",
    "COPYFILE2_CALLBACK_STREAM_FINISHED",
    "COPYFILE2_CALLBACK_STREAM_STARTED",
    "COPYFILE2_COPY_PHASE",
    "COPYFILE2_EXTENDED_PARAMETERS",
    "COPYFILE2_EXTENDED_PARAMETERS_V2",
    "COPYFILE2_MESSAGE",
    "COPYFILE2_MESSAGE_ACTION",
    "COPYFILE2_MESSAGE_TYPE",
    "COPYFILE2_PHASE_MAX",
    "COPYFILE2_PHASE_NAMEGRAFT_COPY",
    "COPYFILE2_PHASE_NONE",
    "COPYFILE2_PHASE_PREPARE_DEST",
    "COPYFILE2_PHASE_PREPARE_SOURCE",
    "COPYFILE2_PHASE_READ_SOURCE",
    "COPYFILE2_PHASE_SERVER_COPY",
    "COPYFILE2_PHASE_WRITE_DESTINATION",
    "COPYFILE2_PROGRESS_CANCEL",
    "COPYFILE2_PROGRESS_CONTINUE",
    "COPYFILE2_PROGRESS_PAUSE",
    "COPYFILE2_PROGRESS_QUIET",
    "COPYFILE2_PROGRESS_STOP",
    "CREATEFILE2_EXTENDED_PARAMETERS",
    "CREATE_ALWAYS",
    "CREATE_NEW",
    "CREATE_TAPE_PARTITION_METHOD",
    "CRM_PROTOCOL_DYNAMIC_MARSHAL_INFO",
    "CRM_PROTOCOL_EXPLICIT_MARSHAL_ONLY",
    "CRM_PROTOCOL_MAXIMUM_OPTION",
    "CSC_CACHE_AUTO_REINT",
    "CSC_CACHE_MANUAL_REINT",
    "CSC_CACHE_NONE",
    "CSC_CACHE_VDO",
    "CSC_MASK",
    "CSC_MASK_EXT",
    "CSV_BLOCK_AND_FILE_CACHE_CALLBACK_VERSION",
    "CSV_BLOCK_CACHE_CALLBACK_VERSION",
    "CheckNameLegalDOS8Dot3A",
    "CheckNameLegalDOS8Dot3W",
    "ClfsClientRecord",
    "ClfsContainerActive",
    "ClfsContainerActivePendingDelete",
    "ClfsContainerInactive",
    "ClfsContainerInitializing",
    "ClfsContainerPendingArchive",
    "ClfsContainerPendingArchiveAndDelete",
    "ClfsDataRecord",
    "ClfsNullRecord",
    "ClfsRestartRecord",
    "CloseAndResetLogFile",
    "CloseEncryptedFileRaw",
    "CloseIoRing",
    "ClsContainerActive",
    "ClsContainerActivePendingDelete",
    "ClsContainerInactive",
    "ClsContainerInitializing",
    "ClsContainerPendingArchive",
    "ClsContainerPendingArchiveAndDelete",
    "CommitComplete",
    "CommitEnlistment",
    "CommitTransaction",
    "CommitTransactionAsync",
    "CompareFileTime",
    "CopyFile2",
    "CopyFileA",
    "CopyFileExA",
    "CopyFileExW",
    "CopyFileFromAppW",
    "CopyFileTransactedA",
    "CopyFileTransactedW",
    "CopyFileW",
    "CopyLZFile",
    "CreateDirectoryA",
    "CreateDirectoryExA",
    "CreateDirectoryExW",
    "CreateDirectoryFromAppW",
    "CreateDirectoryTransactedA",
    "CreateDirectoryTransactedW",
    "CreateDirectoryW",
    "CreateEnlistment",
    "CreateFile2",
    "CreateFile2FromAppW",
    "CreateFileA",
    "CreateFileFromAppW",
    "CreateFileTransactedA",
    "CreateFileTransactedW",
    "CreateFileW",
    "CreateHardLinkA",
    "CreateHardLinkTransactedA",
    "CreateHardLinkTransactedW",
    "CreateHardLinkW",
    "CreateIoRing",
    "CreateLogContainerScanContext",
    "CreateLogFile",
    "CreateLogMarshallingArea",
    "CreateResourceManager",
    "CreateSymbolicLinkA",
    "CreateSymbolicLinkTransactedA",
    "CreateSymbolicLinkTransactedW",
    "CreateSymbolicLinkW",
    "CreateTapePartition",
    "CreateTransaction",
    "CreateTransactionManager",
    "DDD_EXACT_MATCH_ON_REMOVE",
    "DDD_LUID_BROADCAST_DRIVE",
    "DDD_NO_BROADCAST_SYSTEM",
    "DDD_RAW_TARGET_PATH",
    "DDD_REMOVE_DEFINITION",
    "DEFINE_DOS_DEVICE_FLAGS",
    "DELETE",
    "DISKQUOTA_FILESTATE_INCOMPLETE",
    "DISKQUOTA_FILESTATE_MASK",
    "DISKQUOTA_FILESTATE_REBUILDING",
    "DISKQUOTA_LOGFLAG_USER_LIMIT",
    "DISKQUOTA_LOGFLAG_USER_THRESHOLD",
    "DISKQUOTA_STATE_DISABLED",
    "DISKQUOTA_STATE_ENFORCE",
    "DISKQUOTA_STATE_MASK",
    "DISKQUOTA_STATE_TRACK",
    "DISKQUOTA_USERNAME_RESOLVE",
    "DISKQUOTA_USERNAME_RESOLVE_ASYNC",
    "DISKQUOTA_USERNAME_RESOLVE_NONE",
    "DISKQUOTA_USERNAME_RESOLVE_SYNC",
    "DISKQUOTA_USER_ACCOUNT_DELETED",
    "DISKQUOTA_USER_ACCOUNT_INVALID",
    "DISKQUOTA_USER_ACCOUNT_RESOLVED",
    "DISKQUOTA_USER_ACCOUNT_UNAVAILABLE",
    "DISKQUOTA_USER_ACCOUNT_UNKNOWN",
    "DISKQUOTA_USER_ACCOUNT_UNRESOLVED",
    "DISKQUOTA_USER_INFORMATION",
    "DISK_SPACE_INFORMATION",
    "DecryptFileA",
    "DecryptFileW",
    "DefineDosDeviceA",
    "DefineDosDeviceW",
    "DeleteFileA",
    "DeleteFileFromAppW",
    "DeleteFileTransactedA",
    "DeleteFileTransactedW",
    "DeleteFileW",
    "DeleteLogByHandle",
    "DeleteLogFile",
    "DeleteLogMarshallingArea",
    "DeleteVolumeMountPointA",
    "DeleteVolumeMountPointW",
    "DeregisterManageableLogClient",
    "DuplicateEncryptionInfoFile",
    "EA_CONTAINER_NAME",
    "EA_CONTAINER_SIZE",
    "EFS_CERTIFICATE_BLOB",
    "EFS_COMPATIBILITY_INFO",
    "EFS_COMPATIBILITY_VERSION_NCRYPT_PROTECTOR",
    "EFS_COMPATIBILITY_VERSION_PFILE_PROTECTOR",
    "EFS_DECRYPTION_STATUS_INFO",
    "EFS_EFS_SUBVER_EFS_CERT",
    "EFS_ENCRYPTION_STATUS_INFO",
    "EFS_HASH_BLOB",
    "EFS_KEY_INFO",
    "EFS_METADATA_ADD_USER",
    "EFS_METADATA_GENERAL_OP",
    "EFS_METADATA_REMOVE_USER",
    "EFS_METADATA_REPLACE_USER",
    "EFS_PFILE_SUBVER_APPX",
    "EFS_PFILE_SUBVER_RMS",
    "EFS_PIN_BLOB",
    "EFS_RPC_BLOB",
    "EFS_SUBVER_UNKNOWN",
    "EFS_VERSION_INFO",
    "ENCRYPTED_FILE_METADATA_SIGNATURE",
    "ENCRYPTION_CERTIFICATE",
    "ENCRYPTION_CERTIFICATE_HASH",
    "ENCRYPTION_CERTIFICATE_HASH_LIST",
    "ENCRYPTION_CERTIFICATE_LIST",
    "ENCRYPTION_PROTECTOR",
    "ENCRYPTION_PROTECTOR_LIST",
    "ENLISTMENT_MAXIMUM_OPTION",
    "ENLISTMENT_OBJECT_PATH",
    "ENLISTMENT_SUPERIOR",
    "ERASE_TAPE_TYPE",
    "EncryptFileA",
    "EncryptFileW",
    "EncryptionDisable",
    "EraseTape",
    "FCACHE_CREATE_CALLBACK",
    "FCACHE_RICHCREATE_CALLBACK",
    "FH_OVERLAPPED",
    "FILE_ACCESS_FLAGS",
    "FILE_ACTION",
    "FILE_ACTION_ADDED",
    "FILE_ACTION_MODIFIED",
    "FILE_ACTION_REMOVED",
    "FILE_ACTION_RENAMED_NEW_NAME",
    "FILE_ACTION_RENAMED_OLD_NAME",
    "FILE_ADD_FILE",
    "FILE_ADD_SUBDIRECTORY",
    "FILE_ALIGNMENT_INFO",
    "FILE_ALLOCATION_INFO",
    "FILE_ALL_ACCESS",
    "FILE_APPEND_DATA",
    "FILE_ATTRIBUTE_ARCHIVE",
    "FILE_ATTRIBUTE_COMPRESSED",
    "FILE_ATTRIBUTE_DEVICE",
    "FILE_ATTRIBUTE_DIRECTORY",
    "FILE_ATTRIBUTE_EA",
    "FILE_ATTRIBUTE_ENCRYPTED",
    "FILE_ATTRIBUTE_HIDDEN",
    "FILE_ATTRIBUTE_INTEGRITY_STREAM",
    "FILE_ATTRIBUTE_NORMAL",
    "FILE_ATTRIBUTE_NOT_CONTENT_INDEXED",
    "FILE_ATTRIBUTE_NO_SCRUB_DATA",
    "FILE_ATTRIBUTE_OFFLINE",
    "FILE_ATTRIBUTE_PINNED",
    "FILE_ATTRIBUTE_READONLY",
    "FILE_ATTRIBUTE_RECALL_ON_DATA_ACCESS",
    "FILE_ATTRIBUTE_RECALL_ON_OPEN",
    "FILE_ATTRIBUTE_REPARSE_POINT",
    "FILE_ATTRIBUTE_SPARSE_FILE",
    "FILE_ATTRIBUTE_SYSTEM",
    "FILE_ATTRIBUTE_TAG_INFO",
    "FILE_ATTRIBUTE_TEMPORARY",
    "FILE_ATTRIBUTE_UNPINNED",
    "FILE_ATTRIBUTE_VIRTUAL",
    "FILE_BASIC_INFO",
    "FILE_BEGIN",
    "FILE_COMPRESSION_INFO",
    "FILE_CREATE",
    "FILE_CREATE_PIPE_INSTANCE",
    "FILE_CREATION_DISPOSITION",
    "FILE_CURRENT",
    "FILE_DELETE_CHILD",
    "FILE_DEVICE_CD_ROM",
    "FILE_DEVICE_DISK",
    "FILE_DEVICE_DVD",
    "FILE_DEVICE_TAPE",
    "FILE_DEVICE_TYPE",
    "FILE_DISPOSITION_INFO",
    "FILE_END",
    "FILE_END_OF_FILE_INFO",
    "FILE_EXECUTE",
    "FILE_EXTENT",
    "FILE_FLAGS_AND_ATTRIBUTES",
    "FILE_FLAG_BACKUP_SEMANTICS",
    "FILE_FLAG_DELETE_ON_CLOSE",
    "FILE_FLAG_FIRST_PIPE_INSTANCE",
    "FILE_FLAG_NO_BUFFERING",
    "FILE_FLAG_OPEN_NO_RECALL",
    "FILE_FLAG_OPEN_REPARSE_POINT",
    "FILE_FLAG_OVERLAPPED",
    "FILE_FLAG_POSIX_SEMANTICS",
    "FILE_FLAG_RANDOM_ACCESS",
    "FILE_FLAG_SEQUENTIAL_SCAN",
    "FILE_FLAG_SESSION_AWARE",
    "FILE_FLAG_WRITE_THROUGH",
    "FILE_FULL_DIR_INFO",
    "FILE_GENERIC_EXECUTE",
    "FILE_GENERIC_READ",
    "FILE_GENERIC_WRITE",
    "FILE_ID_128",
    "FILE_ID_BOTH_DIR_INFO",
    "FILE_ID_DESCRIPTOR",
    "FILE_ID_EXTD_DIR_INFO",
    "FILE_ID_INFO",
    "FILE_ID_TYPE",
    "FILE_ID_TYPE_ExtendedFileIdType",
    "FILE_ID_TYPE_FileIdType",
    "FILE_ID_TYPE_MaximumFileIdType",
    "FILE_ID_TYPE_ObjectIdType",
    "FILE_INFO_2",
    "FILE_INFO_3",
    "FILE_INFO_BY_HANDLE_CLASS",
    "FILE_INFO_BY_HANDLE_CLASS_FileAlignmentInfo",
    "FILE_INFO_BY_HANDLE_CLASS_FileAllocationInfo",
    "FILE_INFO_BY_HANDLE_CLASS_FileAttributeTagInfo",
    "FILE_INFO_BY_HANDLE_CLASS_FileBasicInfo",
    "FILE_INFO_BY_HANDLE_CLASS_FileCaseSensitiveInfo",
    "FILE_INFO_BY_HANDLE_CLASS_FileCompressionInfo",
    "FILE_INFO_BY_HANDLE_CLASS_FileDispositionInfo",
    "FILE_INFO_BY_HANDLE_CLASS_FileDispositionInfoEx",
    "FILE_INFO_BY_HANDLE_CLASS_FileEndOfFileInfo",
    "FILE_INFO_BY_HANDLE_CLASS_FileFullDirectoryInfo",
    "FILE_INFO_BY_HANDLE_CLASS_FileFullDirectoryRestartInfo",
    "FILE_INFO_BY_HANDLE_CLASS_FileIdBothDirectoryInfo",
    "FILE_INFO_BY_HANDLE_CLASS_FileIdBothDirectoryRestartInfo",
    "FILE_INFO_BY_HANDLE_CLASS_FileIdExtdDirectoryInfo",
    "FILE_INFO_BY_HANDLE_CLASS_FileIdExtdDirectoryRestartInfo",
    "FILE_INFO_BY_HANDLE_CLASS_FileIdInfo",
    "FILE_INFO_BY_HANDLE_CLASS_FileIoPriorityHintInfo",
    "FILE_INFO_BY_HANDLE_CLASS_FileNameInfo",
    "FILE_INFO_BY_HANDLE_CLASS_FileNormalizedNameInfo",
    "FILE_INFO_BY_HANDLE_CLASS_FileRemoteProtocolInfo",
    "FILE_INFO_BY_HANDLE_CLASS_FileRenameInfo",
    "FILE_INFO_BY_HANDLE_CLASS_FileRenameInfoEx",
    "FILE_INFO_BY_HANDLE_CLASS_FileStandardInfo",
    "FILE_INFO_BY_HANDLE_CLASS_FileStorageInfo",
    "FILE_INFO_BY_HANDLE_CLASS_FileStreamInfo",
    "FILE_INFO_BY_HANDLE_CLASS_MaximumFileInfoByHandleClass",
    "FILE_INFO_FLAGS_PERMISSIONS",
    "FILE_IO_PRIORITY_HINT_INFO",
    "FILE_LIST_DIRECTORY",
    "FILE_NAME",
    "FILE_NAME_INFO",
    "FILE_NAME_NORMALIZED",
    "FILE_NAME_OPENED",
    "FILE_NOTIFY_CHANGE",
    "FILE_NOTIFY_CHANGE_ATTRIBUTES",
    "FILE_NOTIFY_CHANGE_CREATION",
    "FILE_NOTIFY_CHANGE_DIR_NAME",
    "FILE_NOTIFY_CHANGE_FILE_NAME",
    "FILE_NOTIFY_CHANGE_LAST_ACCESS",
    "FILE_NOTIFY_CHANGE_LAST_WRITE",
    "FILE_NOTIFY_CHANGE_SECURITY",
    "FILE_NOTIFY_CHANGE_SIZE",
    "FILE_NOTIFY_EXTENDED_INFORMATION",
    "FILE_NOTIFY_INFORMATION",
    "FILE_OPEN",
    "FILE_OPEN_IF",
    "FILE_OVERWRITE",
    "FILE_OVERWRITE_IF",
    "FILE_PROVIDER_COMPRESSION_LZX",
    "FILE_PROVIDER_COMPRESSION_XPRESS16K",
    "FILE_PROVIDER_COMPRESSION_XPRESS4K",
    "FILE_PROVIDER_COMPRESSION_XPRESS8K",
    "FILE_READ_ATTRIBUTES",
    "FILE_READ_DATA",
    "FILE_READ_EA",
    "FILE_REMOTE_PROTOCOL_INFO",
    "FILE_RENAME_INFO",
    "FILE_SEGMENT_ELEMENT",
    "FILE_SHARE_DELETE",
    "FILE_SHARE_MODE",
    "FILE_SHARE_NONE",
    "FILE_SHARE_READ",
    "FILE_SHARE_WRITE",
    "FILE_STANDARD_INFO",
    "FILE_STORAGE_INFO",
    "FILE_STREAM_INFO",
    "FILE_SUPERSEDE",
    "FILE_TRAVERSE",
    "FILE_TYPE",
    "FILE_TYPE_CHAR",
    "FILE_TYPE_DISK",
    "FILE_TYPE_PIPE",
    "FILE_TYPE_REMOTE",
    "FILE_TYPE_UNKNOWN",
    "FILE_VER_GET_LOCALISED",
    "FILE_VER_GET_NEUTRAL",
    "FILE_VER_GET_PREFETCHED",
    "FILE_WRITE_ATTRIBUTES",
    "FILE_WRITE_DATA",
    "FILE_WRITE_EA",
    "FINDEX_INFO_LEVELS",
    "FINDEX_INFO_LEVELS_FindExInfoBasic",
    "FINDEX_INFO_LEVELS_FindExInfoMaxInfoLevel",
    "FINDEX_INFO_LEVELS_FindExInfoStandard",
    "FINDEX_SEARCH_OPS",
    "FINDEX_SEARCH_OPS_FindExSearchLimitToDevices",
    "FINDEX_SEARCH_OPS_FindExSearchLimitToDirectories",
    "FINDEX_SEARCH_OPS_FindExSearchMaxSearchOp",
    "FINDEX_SEARCH_OPS_FindExSearchNameMatch",
    "FIND_FIRST_EX_CASE_SENSITIVE",
    "FIND_FIRST_EX_FLAGS",
    "FIND_FIRST_EX_LARGE_FETCH",
    "FIND_FIRST_EX_ON_DISK_ENTRIES_ONLY",
    "FIO_CONTEXT",
    "FileEncryptionStatusA",
    "FileEncryptionStatusW",
    "FileTimeToLocalFileTime",
    "FindChangeNotificationHandle",
    "FindClose",
    "FindCloseChangeNotification",
    "FindFileHandle",
    "FindFileNameHandle",
    "FindFirstChangeNotificationA",
    "FindFirstChangeNotificationW",
    "FindFirstFileA",
    "FindFirstFileExA",
    "FindFirstFileExFromAppW",
    "FindFirstFileExW",
    "FindFirstFileNameTransactedW",
    "FindFirstFileNameW",
    "FindFirstFileTransactedA",
    "FindFirstFileTransactedW",
    "FindFirstFileW",
    "FindFirstStreamTransactedW",
    "FindFirstStreamW",
    "FindFirstVolumeA",
    "FindFirstVolumeMountPointA",
    "FindFirstVolumeMountPointW",
    "FindFirstVolumeW",
    "FindNextChangeNotification",
    "FindNextFileA",
    "FindNextFileNameW",
    "FindNextFileW",
    "FindNextStreamW",
    "FindNextVolumeA",
    "FindNextVolumeMountPointA",
    "FindNextVolumeMountPointW",
    "FindNextVolumeW",
    "FindStreamHandle",
    "FindVolumeClose",
    "FindVolumeHandle",
    "FindVolumeMointPointHandle",
    "FindVolumeMountPointClose",
    "FlushFileBuffers",
    "FlushLogBuffers",
    "FlushLogToLsn",
    "FreeEncryptedFileMetadata",
    "FreeEncryptionCertificateHashList",
    "FreeReservedLog",
    "GET_FILEEX_INFO_LEVELS",
    "GET_FILEEX_INFO_LEVELS_GetFileExInfoStandard",
    "GET_FILEEX_INFO_LEVELS_GetFileExMaxInfoLevel",
    "GET_FILE_VERSION_INFO_FLAGS",
    "GET_TAPE_DRIVE_INFORMATION",
    "GET_TAPE_DRIVE_PARAMETERS_OPERATION",
    "GET_TAPE_MEDIA_INFORMATION",
    "GetBinaryTypeA",
    "GetBinaryTypeW",
    "GetCompressedFileSizeA",
    "GetCompressedFileSizeTransactedA",
    "GetCompressedFileSizeTransactedW",
    "GetCompressedFileSizeW",
    "GetCurrentClockTransactionManager",
    "GetDiskFreeSpaceA",
    "GetDiskFreeSpaceExA",
    "GetDiskFreeSpaceExW",
    "GetDiskFreeSpaceW",
    "GetDiskSpaceInformationA",
    "GetDiskSpaceInformationW",
    "GetDriveTypeA",
    "GetDriveTypeW",
    "GetEncryptedFileMetadata",
    "GetEnlistmentId",
    "GetEnlistmentRecoveryInformation",
    "GetExpandedNameA",
    "GetExpandedNameW",
    "GetFileAttributesA",
    "GetFileAttributesExA",
    "GetFileAttributesExFromAppW",
    "GetFileAttributesExW",
    "GetFileAttributesTransactedA",
    "GetFileAttributesTransactedW",
    "GetFileAttributesW",
    "GetFileBandwidthReservation",
    "GetFileInformationByHandle",
    "GetFileInformationByHandleEx",
    "GetFileSize",
    "GetFileSizeEx",
    "GetFileTime",
    "GetFileType",
    "GetFileVersionInfoA",
    "GetFileVersionInfoExA",
    "GetFileVersionInfoExW",
    "GetFileVersionInfoSizeA",
    "GetFileVersionInfoSizeExA",
    "GetFileVersionInfoSizeExW",
    "GetFileVersionInfoSizeW",
    "GetFileVersionInfoW",
    "GetFinalPathNameByHandleA",
    "GetFinalPathNameByHandleW",
    "GetFullPathNameA",
    "GetFullPathNameTransactedA",
    "GetFullPathNameTransactedW",
    "GetFullPathNameW",
    "GetIoRingInfo",
    "GetLogContainerName",
    "GetLogFileInformation",
    "GetLogIoStatistics",
    "GetLogReservationInfo",
    "GetLogicalDriveStringsA",
    "GetLogicalDriveStringsW",
    "GetLogicalDrives",
    "GetLongPathNameA",
    "GetLongPathNameTransactedA",
    "GetLongPathNameTransactedW",
    "GetLongPathNameW",
    "GetNextLogArchiveExtent",
    "GetNotificationResourceManager",
    "GetNotificationResourceManagerAsync",
    "GetShortPathNameA",
    "GetShortPathNameW",
    "GetTapeParameters",
    "GetTapePosition",
    "GetTapeStatus",
    "GetTempFileNameA",
    "GetTempFileNameW",
    "GetTempPath2A",
    "GetTempPath2W",
    "GetTempPathA",
    "GetTempPathW",
    "GetTransactionId",
    "GetTransactionInformation",
    "GetTransactionManagerId",
    "GetVolumeInformationA",
    "GetVolumeInformationByHandleW",
    "GetVolumeInformationW",
    "GetVolumeNameForVolumeMountPointA",
    "GetVolumeNameForVolumeMountPointW",
    "GetVolumePathNameA",
    "GetVolumePathNameW",
    "GetVolumePathNamesForVolumeNameA",
    "GetVolumePathNamesForVolumeNameW",
    "HIORING__",
    "HandleLogFull",
    "IDiskQuotaControl",
    "IDiskQuotaEvents",
    "IDiskQuotaUser",
    "IDiskQuotaUserBatch",
    "IEnumDiskQuotaUsers",
    "INVALID_FILE_ATTRIBUTES",
    "INVALID_FILE_SIZE",
    "INVALID_SET_FILE_POINTER",
    "IOCTL_VOLUME_ALLOCATE_BC_STREAM",
    "IOCTL_VOLUME_BASE",
    "IOCTL_VOLUME_BC_VERSION",
    "IOCTL_VOLUME_FREE_BC_STREAM",
    "IOCTL_VOLUME_GET_BC_PROPERTIES",
    "IOCTL_VOLUME_GET_CSVBLOCKCACHE_CALLBACK",
    "IOCTL_VOLUME_GET_GPT_ATTRIBUTES",
    "IOCTL_VOLUME_GET_VOLUME_DISK_EXTENTS",
    "IOCTL_VOLUME_IS_CLUSTERED",
    "IOCTL_VOLUME_IS_CSV",
    "IOCTL_VOLUME_IS_DYNAMIC",
    "IOCTL_VOLUME_IS_IO_CAPABLE",
    "IOCTL_VOLUME_IS_OFFLINE",
    "IOCTL_VOLUME_IS_PARTITION",
    "IOCTL_VOLUME_LOGICAL_TO_PHYSICAL",
    "IOCTL_VOLUME_OFFLINE",
    "IOCTL_VOLUME_ONLINE",
    "IOCTL_VOLUME_PHYSICAL_TO_LOGICAL",
    "IOCTL_VOLUME_POST_ONLINE",
    "IOCTL_VOLUME_PREPARE_FOR_CRITICAL_IO",
    "IOCTL_VOLUME_PREPARE_FOR_SHRINK",
    "IOCTL_VOLUME_QUERY_ALLOCATION_HINT",
    "IOCTL_VOLUME_QUERY_FAILOVER_SET",
    "IOCTL_VOLUME_QUERY_MINIMUM_SHRINK_SIZE",
    "IOCTL_VOLUME_QUERY_VOLUME_NUMBER",
    "IOCTL_VOLUME_READ_PLEX",
    "IOCTL_VOLUME_SET_GPT_ATTRIBUTES",
    "IOCTL_VOLUME_SUPPORTS_ONLINE_OFFLINE",
    "IOCTL_VOLUME_UPDATE_PROPERTIES",
    "IORING_BUFFER_INFO",
    "IORING_BUFFER_REF",
    "IORING_CAPABILITIES",
    "IORING_CQE",
    "IORING_CREATE_ADVISORY_FLAGS",
    "IORING_CREATE_ADVISORY_FLAGS_NONE",
    "IORING_CREATE_FLAGS",
    "IORING_CREATE_REQUIRED_FLAGS",
    "IORING_CREATE_REQUIRED_FLAGS_NONE",
    "IORING_FEATURE_FLAGS",
    "IORING_FEATURE_FLAGS_NONE",
    "IORING_FEATURE_SET_COMPLETION_EVENT",
    "IORING_FEATURE_UM_EMULATION",
    "IORING_HANDLE_REF",
    "IORING_INFO",
    "IORING_OP_CANCEL",
    "IORING_OP_CODE",
    "IORING_OP_NOP",
    "IORING_OP_READ",
    "IORING_OP_REGISTER_BUFFERS",
    "IORING_OP_REGISTER_FILES",
    "IORING_REF_KIND",
    "IORING_REF_RAW",
    "IORING_REF_REGISTERED",
    "IORING_REGISTERED_BUFFER",
    "IORING_SQE_FLAGS",
    "IORING_VERSION",
    "IORING_VERSION_1",
    "IORING_VERSION_INVALID",
    "IOSQE_FLAGS_NONE",
    "InstallLogPolicy",
    "IsIoRingOpSupported",
    "KCRM_MARSHAL_HEADER",
    "KCRM_PROTOCOL_BLOB",
    "KCRM_TRANSACTION_BLOB",
    "KTM_MARSHAL_BLOB_VERSION_MAJOR",
    "KTM_MARSHAL_BLOB_VERSION_MINOR",
    "LOCKFILE_EXCLUSIVE_LOCK",
    "LOCKFILE_FAIL_IMMEDIATELY",
    "LOCK_FILE_FLAGS",
    "LOG_MANAGEMENT_CALLBACKS",
    "LOG_POLICY_OVERWRITE",
    "LOG_POLICY_PERSIST",
    "LPPROGRESS_ROUTINE",
    "LPPROGRESS_ROUTINE_CALLBACK_REASON",
    "LZClose",
    "LZCopy",
    "LZDone",
    "LZERROR_BADINHANDLE",
    "LZERROR_BADOUTHANDLE",
    "LZERROR_BADVALUE",
    "LZERROR_GLOBALLOC",
    "LZERROR_GLOBLOCK",
    "LZERROR_READ",
    "LZERROR_UNKNOWNALG",
    "LZERROR_WRITE",
    "LZInit",
    "LZOPENFILE_STYLE",
    "LZOpenFileA",
    "LZOpenFileW",
    "LZRead",
    "LZSeek",
    "LZStart",
    "LocalFileTimeToFileTime",
    "LockFile",
    "LockFileEx",
    "LogTailAdvanceFailure",
    "LsnBlockOffset",
    "LsnContainer",
    "LsnCreate",
    "LsnEqual",
    "LsnGreater",
    "LsnIncrement",
    "LsnInvalid",
    "LsnLess",
    "LsnNull",
    "LsnRecordSequence",
    "MAXIMUM_REPARSE_DATA_BUFFER_SIZE",
    "MAXMEDIALABEL",
    "MAX_RESOURCEMANAGER_DESCRIPTION_LENGTH",
    "MAX_SID_SIZE",
    "MAX_TRANSACTION_DESCRIPTION_LENGTH",
    "MOVEFILE_COPY_ALLOWED",
    "MOVEFILE_CREATE_HARDLINK",
    "MOVEFILE_DELAY_UNTIL_REBOOT",
    "MOVEFILE_FAIL_IF_NOT_TRACKABLE",
    "MOVEFILE_REPLACE_EXISTING",
    "MOVEFILE_WRITE_THROUGH",
    "MOVE_FILE_FLAGS",
    "MediaLabelInfo",
    "MoveFileA",
    "MoveFileExA",
    "MoveFileExW",
    "MoveFileFromAppW",
    "MoveFileTransactedA",
    "MoveFileTransactedW",
    "MoveFileW",
    "MoveFileWithProgressA",
    "MoveFileWithProgressW",
    "NAME_CACHE_CONTEXT",
    "NTMSMLI_MAXAPPDESCR",
    "NTMSMLI_MAXIDSIZE",
    "NTMSMLI_MAXTYPE",
    "NTMS_ALLOCATE_ERROR_IF_UNAVAILABLE",
    "NTMS_ALLOCATE_FROMSCRATCH",
    "NTMS_ALLOCATE_NEW",
    "NTMS_ALLOCATE_NEXT",
    "NTMS_ALLOCATION_INFORMATION",
    "NTMS_APPLICATIONNAME_LENGTH",
    "NTMS_ASYNCOP_MOUNT",
    "NTMS_ASYNCSTATE_COMPLETE",
    "NTMS_ASYNCSTATE_INPROCESS",
    "NTMS_ASYNCSTATE_QUEUED",
    "NTMS_ASYNCSTATE_WAIT_OPERATOR",
    "NTMS_ASYNCSTATE_WAIT_RESOURCE",
    "NTMS_ASYNC_IO",
    "NTMS_BARCODESTATE_OK",
    "NTMS_BARCODESTATE_UNREADABLE",
    "NTMS_BARCODE_LENGTH",
    "NTMS_CHANGER",
    "NTMS_CHANGERINFORMATIONA",
    "NTMS_CHANGERINFORMATIONW",
    "NTMS_CHANGERTYPEINFORMATIONA",
    "NTMS_CHANGERTYPEINFORMATIONW",
    "NTMS_CHANGER_TYPE",
    "NTMS_COMPUTER",
    "NTMS_COMPUTERINFORMATION",
    "NTMS_COMPUTERNAME_LENGTH",
    "NTMS_CONTROL_ACCESS",
    "NTMS_CREATE_NEW",
    "NTMS_DEALLOCATE_TOSCRATCH",
    "NTMS_DESCRIPTION_LENGTH",
    "NTMS_DEVICENAME_LENGTH",
    "NTMS_DISMOUNT_DEFERRED",
    "NTMS_DISMOUNT_IMMEDIATE",
    "NTMS_DOORSTATE_CLOSED",
    "NTMS_DOORSTATE_OPEN",
    "NTMS_DOORSTATE_UNKNOWN",
    "NTMS_DRIVE",
    "NTMS_DRIVEINFORMATIONA",
    "NTMS_DRIVEINFORMATIONW",
    "NTMS_DRIVESTATE_BEING_CLEANED",
    "NTMS_DRIVESTATE_DISMOUNTABLE",
    "NTMS_DRIVESTATE_DISMOUNTED",
    "NTMS_DRIVESTATE_LOADED",
    "NTMS_DRIVESTATE_MOUNTED",
    "NTMS_DRIVESTATE_UNLOADED",
    "NTMS_DRIVETYPEINFORMATIONA",
    "NTMS_DRIVETYPEINFORMATIONW",
    "NTMS_DRIVE_TYPE",
    "NTMS_EJECT_ASK_USER",
    "NTMS_EJECT_FORCE",
    "NTMS_EJECT_IMMEDIATE",
    "NTMS_EJECT_QUEUE",
    "NTMS_EJECT_START",
    "NTMS_EJECT_STOP",
    "NTMS_ENUM_DEFAULT",
    "NTMS_ENUM_ROOTPOOL",
    "NTMS_ERROR_ON_DUPLICATE",
    "NTMS_EVENT_COMPLETE",
    "NTMS_EVENT_SIGNAL",
    "NTMS_FILESYSTEM_INFO",
    "NTMS_I1_LIBRARYINFORMATION",
    "NTMS_I1_LIBREQUESTINFORMATIONA",
    "NTMS_I1_LIBREQUESTINFORMATIONW",
    "NTMS_I1_MESSAGE_LENGTH",
    "NTMS_I1_OBJECTINFORMATIONA",
    "NTMS_I1_OBJECTINFORMATIONW",
    "NTMS_I1_OPREQUESTINFORMATIONA",
    "NTMS_I1_OPREQUESTINFORMATIONW",
    "NTMS_I1_PARTITIONINFORMATIONA",
    "NTMS_I1_PARTITIONINFORMATIONW",
    "NTMS_I1_PMIDINFORMATIONA",
    "NTMS_I1_PMIDINFORMATIONW",
    "NTMS_IEDOOR",
    "NTMS_IEDOORINFORMATION",
    "NTMS_IEPORT",
    "NTMS_IEPORTINFORMATION",
    "NTMS_INITIALIZING",
    "NTMS_INJECT_RETRACT",
    "NTMS_INJECT_START",
    "NTMS_INJECT_STARTMANY",
    "NTMS_INJECT_STOP",
    "NTMS_INVENTORY_DEFAULT",
    "NTMS_INVENTORY_FAST",
    "NTMS_INVENTORY_MAX",
    "NTMS_INVENTORY_NONE",
    "NTMS_INVENTORY_OMID",
    "NTMS_INVENTORY_SLOT",
    "NTMS_INVENTORY_STOP",
    "NTMS_LIBRARY",
    "NTMS_LIBRARYFLAG_AUTODETECTCHANGE",
    "NTMS_LIBRARYFLAG_CLEANERPRESENT",
    "NTMS_LIBRARYFLAG_FIXEDOFFLINE",
    "NTMS_LIBRARYFLAG_IGNORECLEANERUSESREMAINING",
    "NTMS_LIBRARYFLAG_RECOGNIZECLEANERBARCODE",
    "NTMS_LIBRARYINFORMATION",
    "NTMS_LIBRARYTYPE_OFFLINE",
    "NTMS_LIBRARYTYPE_ONLINE",
    "NTMS_LIBRARYTYPE_STANDALONE",
    "NTMS_LIBRARYTYPE_UNKNOWN",
    "NTMS_LIBREQFLAGS_NOAUTOPURGE",
    "NTMS_LIBREQFLAGS_NOFAILEDPURGE",
    "NTMS_LIBREQUEST",
    "NTMS_LIBREQUESTINFORMATIONA",
    "NTMS_LIBREQUESTINFORMATIONW",
    "NTMS_LMIDINFORMATION",
    "NTMS_LM_CANCELLED",
    "NTMS_LM_CLASSIFY",
    "NTMS_LM_CLEANDRIVE",
    "NTMS_LM_DEFERRED",
    "NTMS_LM_DEFFERED",
    "NTMS_LM_DISABLECHANGER",
    "NTMS_LM_DISABLEDRIVE",
    "NTMS_LM_DISABLELIBRARY",
    "NTMS_LM_DISABLEMEDIA",
    "NTMS_LM_DISMOUNT",
    "NTMS_LM_DOORACCESS",
    "NTMS_LM_EJECT",
    "NTMS_LM_EJECTCLEANER",
    "NTMS_LM_ENABLECHANGER",
    "NTMS_LM_ENABLEDRIVE",
    "NTMS_LM_ENABLELIBRARY",
    "NTMS_LM_ENABLEMEDIA",
    "NTMS_LM_FAILED",
    "NTMS_LM_INJECT",
    "NTMS_LM_INJECTCLEANER",
    "NTMS_LM_INPROCESS",
    "NTMS_LM_INVALID",
    "NTMS_LM_INVENTORY",
    "NTMS_LM_MAXWORKITEM",
    "NTMS_LM_MOUNT",
    "NTMS_LM_PASSED",
    "NTMS_LM_PROCESSOMID",
    "NTMS_LM_QUEUED",
    "NTMS_LM_RELEASECLEANER",
    "NTMS_LM_REMOVE",
    "NTMS_LM_RESERVECLEANER",
    "NTMS_LM_STOPPED",
    "NTMS_LM_UPDATEOMID",
    "NTMS_LM_WAITING",
    "NTMS_LM_WRITESCRATCH",
    "NTMS_LOGICAL_MEDIA",
    "NTMS_MAXATTR_LENGTH",
    "NTMS_MAXATTR_NAMELEN",
    "NTMS_MEDIAPOOLINFORMATION",
    "NTMS_MEDIARW_READONLY",
    "NTMS_MEDIARW_REWRITABLE",
    "NTMS_MEDIARW_UNKNOWN",
    "NTMS_MEDIARW_WRITEONCE",
    "NTMS_MEDIASTATE_IDLE",
    "NTMS_MEDIASTATE_INUSE",
    "NTMS_MEDIASTATE_LOADED",
    "NTMS_MEDIASTATE_MOUNTED",
    "NTMS_MEDIASTATE_OPERROR",
    "NTMS_MEDIASTATE_OPREQ",
    "NTMS_MEDIASTATE_UNLOADED",
    "NTMS_MEDIATYPEINFORMATION",
    "NTMS_MEDIA_POOL",
    "NTMS_MEDIA_TYPE",
    "NTMS_MESSAGE_LENGTH",
    "NTMS_MODIFY_ACCESS",
    "NTMS_MOUNT_ERROR_IF_OFFLINE",
    "NTMS_MOUNT_ERROR_IF_UNAVAILABLE",
    "NTMS_MOUNT_ERROR_NOT_AVAILABLE",
    "NTMS_MOUNT_ERROR_OFFLINE",
    "NTMS_MOUNT_INFORMATION",
    "NTMS_MOUNT_NOWAIT",
    "NTMS_MOUNT_READ",
    "NTMS_MOUNT_SPECIFIC_DRIVE",
    "NTMS_MOUNT_WRITE",
    "NTMS_NEEDS_SERVICE",
    "NTMS_NOTIFICATIONINFORMATION",
    "NTMS_NOT_PRESENT",
    "NTMS_NUMBER_OF_OBJECT_TYPES",
    "NTMS_OBJECT",
    "NTMS_OBJECTINFORMATIONA",
    "NTMS_OBJECTINFORMATIONW",
    "NTMS_OBJECTNAME_LENGTH",
    "NTMS_OBJ_DELETE",
    "NTMS_OBJ_INSERT",
    "NTMS_OBJ_UPDATE",
    "NTMS_OMIDLABELID_LENGTH",
    "NTMS_OMIDLABELINFO_LENGTH",
    "NTMS_OMIDLABELTYPE_LENGTH",
    "NTMS_OMID_TYPE",
    "NTMS_OMID_TYPE_FILESYSTEM_INFO",
    "NTMS_OMID_TYPE_RAW_LABEL",
    "NTMS_OPEN_ALWAYS",
    "NTMS_OPEN_EXISTING",
    "NTMS_OPREQFLAGS_NOALERTS",
    "NTMS_OPREQFLAGS_NOAUTOPURGE",
    "NTMS_OPREQFLAGS_NOFAILEDPURGE",
    "NTMS_OPREQFLAGS_NOTRAYICON",
    "NTMS_OPREQUEST",
    "NTMS_OPREQUESTINFORMATIONA",
    "NTMS_OPREQUESTINFORMATIONW",
    "NTMS_OPREQ_CLEANER",
    "NTMS_OPREQ_DEVICESERVICE",
    "NTMS_OPREQ_MESSAGE",
    "NTMS_OPREQ_MOVEMEDIA",
    "NTMS_OPREQ_NEWMEDIA",
    "NTMS_OPREQ_UNKNOWN",
    "NTMS_OPSTATE_ACTIVE",
    "NTMS_OPSTATE_COMPLETE",
    "NTMS_OPSTATE_INPROGRESS",
    "NTMS_OPSTATE_REFUSED",
    "NTMS_OPSTATE_SUBMITTED",
    "NTMS_OPSTATE_UNKNOWN",
    "NTMS_PARTITION",
    "NTMS_PARTITIONINFORMATIONA",
    "NTMS_PARTITIONINFORMATIONW",
    "NTMS_PARTSTATE_ALLOCATED",
    "NTMS_PARTSTATE_AVAILABLE",
    "NTMS_PARTSTATE_COMPLETE",
    "NTMS_PARTSTATE_DECOMMISSIONED",
    "NTMS_PARTSTATE_FOREIGN",
    "NTMS_PARTSTATE_IMPORT",
    "NTMS_PARTSTATE_INCOMPATIBLE",
    "NTMS_PARTSTATE_RESERVED",
    "NTMS_PARTSTATE_UNKNOWN",
    "NTMS_PARTSTATE_UNPREPARED",
    "NTMS_PHYSICAL_MEDIA",
    "NTMS_PMIDINFORMATIONA",
    "NTMS_PMIDINFORMATIONW",
    "NTMS_POOLHIERARCHY_LENGTH",
    "NTMS_POOLPOLICY_KEEPOFFLINEIMPORT",
    "NTMS_POOLPOLICY_PURGEOFFLINESCRATCH",
    "NTMS_POOLTYPE_APPLICATION",
    "NTMS_POOLTYPE_FOREIGN",
    "NTMS_POOLTYPE_IMPORT",
    "NTMS_POOLTYPE_SCRATCH",
    "NTMS_POOLTYPE_UNKNOWN",
    "NTMS_PORTCONTENT_EMPTY",
    "NTMS_PORTCONTENT_FULL",
    "NTMS_PORTCONTENT_UNKNOWN",
    "NTMS_PORTPOSITION_EXTENDED",
    "NTMS_PORTPOSITION_RETRACTED",
    "NTMS_PORTPOSITION_UNKNOWN",
    "NTMS_PRIORITY_DEFAULT",
    "NTMS_PRIORITY_HIGH",
    "NTMS_PRIORITY_HIGHEST",
    "NTMS_PRIORITY_LOW",
    "NTMS_PRIORITY_LOWEST",
    "NTMS_PRIORITY_NORMAL",
    "NTMS_PRODUCTNAME_LENGTH",
    "NTMS_READY",
    "NTMS_REVISION_LENGTH",
    "NTMS_SEQUENCE_LENGTH",
    "NTMS_SERIALNUMBER_LENGTH",
    "NTMS_SESSION_QUERYEXPEDITE",
    "NTMS_SLOTSTATE_EMPTY",
    "NTMS_SLOTSTATE_FULL",
    "NTMS_SLOTSTATE_NEEDSINVENTORY",
    "NTMS_SLOTSTATE_NOTPRESENT",
    "NTMS_SLOTSTATE_UNKNOWN",
    "NTMS_STORAGESLOT",
    "NTMS_STORAGESLOTINFORMATION",
    "NTMS_UIDEST_ADD",
    "NTMS_UIDEST_DELETE",
    "NTMS_UIDEST_DELETEALL",
    "NTMS_UIOPERATION_MAX",
    "NTMS_UITYPE_ERR",
    "NTMS_UITYPE_INFO",
    "NTMS_UITYPE_INVALID",
    "NTMS_UITYPE_MAX",
    "NTMS_UITYPE_REQ",
    "NTMS_UI_DESTINATION",
    "NTMS_UNKNOWN",
    "NTMS_UNKNOWN_DRIVE",
    "NTMS_USERNAME_LENGTH",
    "NTMS_USE_ACCESS",
    "NTMS_VENDORNAME_LENGTH",
    "NT_CREATE_FILE_DISPOSITION",
    "NetConnectionEnum",
    "NetFileClose",
    "NetFileEnum",
    "NetFileGetInfo",
    "NetServerAliasAdd",
    "NetServerAliasDel",
    "NetServerAliasEnum",
    "NetSessionDel",
    "NetSessionEnum",
    "NetSessionGetInfo",
    "NetShareAdd",
    "NetShareCheck",
    "NetShareDel",
    "NetShareDelEx",
    "NetShareDelSticky",
    "NetShareEnum",
    "NetShareEnumSticky",
    "NetShareGetInfo",
    "NetShareSetInfo",
    "NetStatisticsGet",
    "NtCreateFile",
    "NtmsAccessMask",
    "NtmsAllocateOptions",
    "NtmsAllocationPolicy",
    "NtmsAsyncOperations",
    "NtmsAsyncStatus",
    "NtmsBarCodeState",
    "NtmsCreateNtmsMediaOptions",
    "NtmsCreateOptions",
    "NtmsDeallocationPolicy",
    "NtmsDismountOptions",
    "NtmsDoorState",
    "NtmsDriveState",
    "NtmsDriveType",
    "NtmsEjectOperation",
    "NtmsEnumerateOption",
    "NtmsInjectOperation",
    "NtmsInventoryMethod",
    "NtmsLibRequestFlags",
    "NtmsLibraryFlags",
    "NtmsLibraryType",
    "NtmsLmOperation",
    "NtmsLmState",
    "NtmsMediaPoolPolicy",
    "NtmsMediaState",
    "NtmsMountOptions",
    "NtmsMountPriority",
    "NtmsNotificationOperations",
    "NtmsObjectsTypes",
    "NtmsOpRequestFlags",
    "NtmsOperationalState",
    "NtmsOpreqCommand",
    "NtmsOpreqState",
    "NtmsPartitionState",
    "NtmsPoolType",
    "NtmsPortContent",
    "NtmsPortPosition",
    "NtmsReadWriteCharacteristics",
    "NtmsSessionOptions",
    "NtmsSlotState",
    "NtmsUIOperations",
    "NtmsUITypes",
    "OFSTRUCT",
    "OF_CANCEL",
    "OF_CREATE",
    "OF_DELETE",
    "OF_EXIST",
    "OF_PARSE",
    "OF_PROMPT",
    "OF_READ",
    "OF_READWRITE",
    "OF_REOPEN",
    "OF_SHARE_COMPAT",
    "OF_SHARE_DENY_NONE",
    "OF_SHARE_DENY_READ",
    "OF_SHARE_DENY_WRITE",
    "OF_SHARE_EXCLUSIVE",
    "OF_VERIFY",
    "OF_WRITE",
    "OPEN_ALWAYS",
    "OPEN_EXISTING",
    "OpenEncryptedFileRawA",
    "OpenEncryptedFileRawW",
    "OpenEnlistment",
    "OpenFile",
    "OpenFileById",
    "OpenResourceManager",
    "OpenTransaction",
    "OpenTransactionManager",
    "OpenTransactionManagerById",
    "PARTITION_BASIC_DATA_GUID",
    "PARTITION_BSP_GUID",
    "PARTITION_CLUSTER_GUID",
    "PARTITION_DPP_GUID",
    "PARTITION_ENTRY_UNUSED_GUID",
    "PARTITION_LDM_DATA_GUID",
    "PARTITION_LDM_METADATA_GUID",
    "PARTITION_LEGACY_BL_GUID",
    "PARTITION_LEGACY_BL_GUID_BACKUP",
    "PARTITION_MAIN_OS_GUID",
    "PARTITION_MSFT_RECOVERY_GUID",
    "PARTITION_MSFT_RESERVED_GUID",
    "PARTITION_MSFT_SNAPSHOT_GUID",
    "PARTITION_OS_DATA_GUID",
    "PARTITION_PATCH_GUID",
    "PARTITION_PRE_INSTALLED_GUID",
    "PARTITION_SERVICING_FILES_GUID",
    "PARTITION_SERVICING_METADATA_GUID",
    "PARTITION_SERVICING_RESERVE_GUID",
    "PARTITION_SERVICING_STAGING_ROOT_GUID",
    "PARTITION_SPACES_DATA_GUID",
    "PARTITION_SPACES_GUID",
    "PARTITION_SYSTEM_GUID",
    "PARTITION_WINDOWS_SYSTEM_GUID",
    "PCLFS_COMPLETION_ROUTINE",
    "PCOPYFILE2_PROGRESS_ROUTINE",
    "PERM_FILE_CREATE",
    "PERM_FILE_READ",
    "PERM_FILE_WRITE",
    "PFE_EXPORT_FUNC",
    "PFE_IMPORT_FUNC",
    "PFN_IO_COMPLETION",
    "PIPE_ACCESS_DUPLEX",
    "PIPE_ACCESS_INBOUND",
    "PIPE_ACCESS_OUTBOUND",
    "PLOG_FULL_HANDLER_CALLBACK",
    "PLOG_TAIL_ADVANCE_CALLBACK",
    "PLOG_UNPINNED_CALLBACK",
    "PREPARE_TAPE_OPERATION",
    "PRIORITY_HINT",
    "PRIORITY_HINT_IoPriorityHintLow",
    "PRIORITY_HINT_IoPriorityHintNormal",
    "PRIORITY_HINT_IoPriorityHintVeryLow",
    "PRIORITY_HINT_MaximumIoPriorityHintType",
    "PopIoRingCompletion",
    "PrePrepareComplete",
    "PrePrepareEnlistment",
    "PrepareComplete",
    "PrepareEnlistment",
    "PrepareLogArchive",
    "PrepareTape",
    "QUIC",
    "QueryDosDeviceA",
    "QueryDosDeviceW",
    "QueryIoRingCapabilities",
    "QueryLogPolicy",
    "QueryRecoveryAgentsOnEncryptedFile",
    "QueryUsersOnEncryptedFile",
    "READ_CONTROL",
    "READ_DIRECTORY_NOTIFY_INFORMATION_CLASS",
    "READ_DIRECTORY_NOTIFY_INFORMATION_CLASS_ReadDirectoryNotifyExtendedInformation",
    "READ_DIRECTORY_NOTIFY_INFORMATION_CLASS_ReadDirectoryNotifyInformation",
    "REPARSE_GUID_DATA_BUFFER",
    "REPLACEFILE_IGNORE_ACL_ERRORS",
    "REPLACEFILE_IGNORE_MERGE_ERRORS",
    "REPLACEFILE_WRITE_THROUGH",
    "REPLACE_FILE_FLAGS",
    "RESOURCE_MANAGER_COMMUNICATION",
    "RESOURCE_MANAGER_MAXIMUM_OPTION",
    "RESOURCE_MANAGER_OBJECT_PATH",
    "RESOURCE_MANAGER_VOLATILE",
    "ReOpenFile",
    "ReadDirectoryChangesExW",
    "ReadDirectoryChangesW",
    "ReadEncryptedFileRaw",
    "ReadFile",
    "ReadFileEx",
    "ReadFileScatter",
    "ReadLogArchiveMetadata",
    "ReadLogNotification",
    "ReadLogRecord",
    "ReadLogRestartArea",
    "ReadNextLogRecord",
    "ReadOnlyEnlistment",
    "ReadPreviousLogRestartArea",
    "RecoverEnlistment",
    "RecoverResourceManager",
    "RecoverTransactionManager",
    "RegisterForLogWriteNotification",
    "RegisterManageableLogClient",
    "RemoveDirectoryA",
    "RemoveDirectoryFromAppW",
    "RemoveDirectoryTransactedA",
    "RemoveDirectoryTransactedW",
    "RemoveDirectoryW",
    "RemoveLogContainer",
    "RemoveLogContainerSet",
    "RemoveLogPolicy",
    "RemoveUsersFromEncryptedFile",
    "RenameTransactionManager",
    "ReplaceFileA",
    "ReplaceFileFromAppW",
    "ReplaceFileW",
    "ReserveAndAppendLog",
    "ReserveAndAppendLogAligned",
    "RollbackComplete",
    "RollbackEnlistment",
    "RollbackTransaction",
    "RollbackTransactionAsync",
    "RollforwardTransactionManager",
    "SECURITY_ANONYMOUS",
    "SECURITY_CONTEXT_TRACKING",
    "SECURITY_DELEGATION",
    "SECURITY_EFFECTIVE_ONLY",
    "SECURITY_IDENTIFICATION",
    "SECURITY_IMPERSONATION",
    "SECURITY_SQOS_PRESENT",
    "SECURITY_VALID_SQOS_FLAGS",
    "SERVER_ALIAS_INFO_0",
    "SERVER_CERTIFICATE_INFO_0",
    "SERVER_CERTIFICATE_TYPE",
    "SESI1_NUM_ELEMENTS",
    "SESI2_NUM_ELEMENTS",
    "SESSION_INFO_0",
    "SESSION_INFO_1",
    "SESSION_INFO_10",
    "SESSION_INFO_2",
    "SESSION_INFO_502",
    "SESSION_INFO_USER_FLAGS",
    "SESS_GUEST",
    "SESS_NOENCRYPTION",
    "SET_FILE_POINTER_MOVE_METHOD",
    "SET_TAPE_DRIVE_INFORMATION",
    "SET_TAPE_MEDIA_INFORMATION",
    "SHARE_CURRENT_USES_PARMNUM",
    "SHARE_FILE_SD_PARMNUM",
    "SHARE_INFO_0",
    "SHARE_INFO_1",
    "SHARE_INFO_1004",
    "SHARE_INFO_1005",
    "SHARE_INFO_1006",
    "SHARE_INFO_1501",
    "SHARE_INFO_1503",
    "SHARE_INFO_2",
    "SHARE_INFO_501",
    "SHARE_INFO_502",
    "SHARE_INFO_503",
    "SHARE_INFO_PERMISSIONS",
    "SHARE_MAX_USES_PARMNUM",
    "SHARE_NETNAME_PARMNUM",
    "SHARE_PASSWD_PARMNUM",
    "SHARE_PATH_PARMNUM",
    "SHARE_PERMISSIONS_PARMNUM",
    "SHARE_REMARK_PARMNUM",
    "SHARE_SERVER_PARMNUM",
    "SHARE_TYPE",
    "SHARE_TYPE_PARMNUM",
    "SHI1005_FLAGS_ACCESS_BASED_DIRECTORY_ENUM",
    "SHI1005_FLAGS_ALLOW_NAMESPACE_CACHING",
    "SHI1005_FLAGS_CLUSTER_MANAGED",
    "SHI1005_FLAGS_COMPRESS_DATA",
    "SHI1005_FLAGS_DFS",
    "SHI1005_FLAGS_DFS_ROOT",
    "SHI1005_FLAGS_DISABLE_CLIENT_BUFFERING",
    "SHI1005_FLAGS_ENABLE_CA",
    "SHI1005_FLAGS_ENABLE_HASH",
    "SHI1005_FLAGS_ENCRYPT_DATA",
    "SHI1005_FLAGS_FORCE_LEVELII_OPLOCK",
    "SHI1005_FLAGS_FORCE_SHARED_DELETE",
    "SHI1005_FLAGS_IDENTITY_REMOTING",
    "SHI1005_FLAGS_RESERVED",
    "SHI1005_FLAGS_RESTRICT_EXCLUSIVE_OPENS",
    "SHI1_NUM_ELEMENTS",
    "SHI2_NUM_ELEMENTS",
    "SHI_USES_UNLIMITED",
    "SPECIFIC_RIGHTS_ALL",
    "STANDARD_RIGHTS_ALL",
    "STANDARD_RIGHTS_EXECUTE",
    "STANDARD_RIGHTS_READ",
    "STANDARD_RIGHTS_REQUIRED",
    "STANDARD_RIGHTS_WRITE",
    "STATSOPT_CLR",
    "STAT_SERVER_0",
    "STAT_WORKSTATION_0",
    "STORAGE_BUS_TYPE",
    "STORAGE_BUS_TYPE_BusType1394",
    "STORAGE_BUS_TYPE_BusTypeAta",
    "STORAGE_BUS_TYPE_BusTypeAtapi",
    "STORAGE_BUS_TYPE_BusTypeFibre",
    "STORAGE_BUS_TYPE_BusTypeFileBackedVirtual",
    "STORAGE_BUS_TYPE_BusTypeMax",
    "STORAGE_BUS_TYPE_BusTypeMaxReserved",
    "STORAGE_BUS_TYPE_BusTypeMmc",
    "STORAGE_BUS_TYPE_BusTypeNvme",
    "STORAGE_BUS_TYPE_BusTypeRAID",
    "STORAGE_BUS_TYPE_BusTypeSCM",
    "STORAGE_BUS_TYPE_BusTypeSas",
    "STORAGE_BUS_TYPE_BusTypeSata",
    "STORAGE_BUS_TYPE_BusTypeScsi",
    "STORAGE_BUS_TYPE_BusTypeSd",
    "STORAGE_BUS_TYPE_BusTypeSpaces",
    "STORAGE_BUS_TYPE_BusTypeSsa",
    "STORAGE_BUS_TYPE_BusTypeUfs",
    "STORAGE_BUS_TYPE_BusTypeUnknown",
    "STORAGE_BUS_TYPE_BusTypeUsb",
    "STORAGE_BUS_TYPE_BusTypeVirtual",
    "STORAGE_BUS_TYPE_BusTypeiScsi",
    "STREAM_INFO_LEVELS",
    "STREAM_INFO_LEVELS_FindStreamInfoMaxInfoLevel",
    "STREAM_INFO_LEVELS_FindStreamInfoStandard",
    "STYPE_DEVICE",
    "STYPE_DISKTREE",
    "STYPE_IPC",
    "STYPE_MASK",
    "STYPE_PRINTQ",
    "STYPE_RESERVED1",
    "STYPE_RESERVED2",
    "STYPE_RESERVED3",
    "STYPE_RESERVED4",
    "STYPE_RESERVED5",
    "STYPE_RESERVED_ALL",
    "STYPE_SPECIAL",
    "STYPE_TEMPORARY",
    "SYMBOLIC_LINK_FLAGS",
    "SYMBOLIC_LINK_FLAG_ALLOW_UNPRIVILEGED_CREATE",
    "SYMBOLIC_LINK_FLAG_DIRECTORY",
    "SYNCHRONIZE",
    "ScanLogContainers",
    "SearchPathA",
    "SearchPathW",
    "SetEncryptedFileMetadata",
    "SetEndOfFile",
    "SetEndOfLog",
    "SetEnlistmentRecoveryInformation",
    "SetFileApisToANSI",
    "SetFileApisToOEM",
    "SetFileAttributesA",
    "SetFileAttributesFromAppW",
    "SetFileAttributesTransactedA",
    "SetFileAttributesTransactedW",
    "SetFileAttributesW",
    "SetFileBandwidthReservation",
    "SetFileCompletionNotificationModes",
    "SetFileInformationByHandle",
    "SetFileIoOverlappedRange",
    "SetFilePointer",
    "SetFilePointerEx",
    "SetFileShortNameA",
    "SetFileShortNameW",
    "SetFileTime",
    "SetFileValidData",
    "SetIoRingCompletionEvent",
    "SetLogArchiveMode",
    "SetLogArchiveTail",
    "SetLogFileSizeWithPolicy",
    "SetResourceManagerCompletionPort",
    "SetSearchPathMode",
    "SetTapeParameters",
    "SetTapePosition",
    "SetTransactionInformation",
    "SetUserFileEncryptionKey",
    "SetUserFileEncryptionKeyEx",
    "SetVolumeLabelA",
    "SetVolumeLabelW",
    "SetVolumeMountPointA",
    "SetVolumeMountPointW",
    "SinglePhaseReject",
    "SubmitIoRing",
    "TAPEMARK_TYPE",
    "TAPE_ABSOLUTE_BLOCK",
    "TAPE_ABSOLUTE_POSITION",
    "TAPE_ERASE",
    "TAPE_ERASE_LONG",
    "TAPE_ERASE_SHORT",
    "TAPE_FILEMARKS",
    "TAPE_FIXED_PARTITIONS",
    "TAPE_FORMAT",
    "TAPE_GET_POSITION",
    "TAPE_INFORMATION_TYPE",
    "TAPE_INITIATOR_PARTITIONS",
    "TAPE_LOAD",
    "TAPE_LOCK",
    "TAPE_LOGICAL_BLOCK",
    "TAPE_LOGICAL_POSITION",
    "TAPE_LONG_FILEMARKS",
    "TAPE_POSITION_METHOD",
    "TAPE_POSITION_TYPE",
    "TAPE_PREPARE",
    "TAPE_REWIND",
    "TAPE_SELECT_PARTITIONS",
    "TAPE_SETMARKS",
    "TAPE_SET_POSITION",
    "TAPE_SHORT_FILEMARKS",
    "TAPE_SPACE_END_OF_DATA",
    "TAPE_SPACE_FILEMARKS",
    "TAPE_SPACE_RELATIVE_BLOCKS",
    "TAPE_SPACE_SEQUENTIAL_FMKS",
    "TAPE_SPACE_SEQUENTIAL_SMKS",
    "TAPE_SPACE_SETMARKS",
    "TAPE_TENSION",
    "TAPE_UNLOAD",
    "TAPE_UNLOCK",
    "TAPE_WRITE_MARKS",
    "TRANSACTIONMANAGER_OBJECT_PATH",
    "TRANSACTION_DO_NOT_PROMOTE",
    "TRANSACTION_MANAGER_COMMIT_DEFAULT",
    "TRANSACTION_MANAGER_COMMIT_LOWEST",
    "TRANSACTION_MANAGER_COMMIT_SYSTEM_HIVES",
    "TRANSACTION_MANAGER_COMMIT_SYSTEM_VOLUME",
    "TRANSACTION_MANAGER_CORRUPT_FOR_PROGRESS",
    "TRANSACTION_MANAGER_CORRUPT_FOR_RECOVERY",
    "TRANSACTION_MANAGER_MAXIMUM_OPTION",
    "TRANSACTION_MANAGER_VOLATILE",
    "TRANSACTION_MAXIMUM_OPTION",
    "TRANSACTION_NOTIFICATION",
    "TRANSACTION_NOTIFICATION_MARSHAL_ARGUMENT",
    "TRANSACTION_NOTIFICATION_PROPAGATE_ARGUMENT",
    "TRANSACTION_NOTIFICATION_RECOVERY_ARGUMENT",
    "TRANSACTION_NOTIFICATION_SAVEPOINT_ARGUMENT",
    "TRANSACTION_NOTIFICATION_TM_ONLINE_ARGUMENT",
    "TRANSACTION_NOTIFICATION_TM_ONLINE_FLAG_IS_CLUSTERED",
    "TRANSACTION_NOTIFY_COMMIT",
    "TRANSACTION_NOTIFY_COMMIT_COMPLETE",
    "TRANSACTION_NOTIFY_COMMIT_FINALIZE",
    "TRANSACTION_NOTIFY_COMMIT_REQUEST",
    "TRANSACTION_NOTIFY_DELEGATE_COMMIT",
    "TRANSACTION_NOTIFY_ENLIST_MASK",
    "TRANSACTION_NOTIFY_ENLIST_PREPREPARE",
    "TRANSACTION_NOTIFY_INDOUBT",
    "TRANSACTION_NOTIFY_LAST_RECOVER",
    "TRANSACTION_NOTIFY_MARSHAL",
    "TRANSACTION_NOTIFY_MASK",
    "TRANSACTION_NOTIFY_PREPARE",
    "TRANSACTION_NOTIFY_PREPARE_COMPLETE",
    "TRANSACTION_NOTIFY_PREPREPARE",
    "TRANSACTION_NOTIFY_PREPREPARE_COMPLETE",
    "TRANSACTION_NOTIFY_PROMOTE",
    "TRANSACTION_NOTIFY_PROMOTE_NEW",
    "TRANSACTION_NOTIFY_PROPAGATE_PULL",
    "TRANSACTION_NOTIFY_PROPAGATE_PUSH",
    "TRANSACTION_NOTIFY_RECOVER",
    "TRANSACTION_NOTIFY_RECOVER_QUERY",
    "TRANSACTION_NOTIFY_REQUEST_OUTCOME",
    "TRANSACTION_NOTIFY_RM_DISCONNECTED",
    "TRANSACTION_NOTIFY_ROLLBACK",
    "TRANSACTION_NOTIFY_ROLLBACK_COMPLETE",
    "TRANSACTION_NOTIFY_SINGLE_PHASE_COMMIT",
    "TRANSACTION_NOTIFY_TM_ONLINE",
    "TRANSACTION_OBJECT_PATH",
    "TRANSACTION_OUTCOME",
    "TRANSACTION_OUTCOME_TransactionOutcomeAborted",
    "TRANSACTION_OUTCOME_TransactionOutcomeCommitted",
    "TRANSACTION_OUTCOME_TransactionOutcomeUndetermined",
    "TRUNCATE_EXISTING",
    "TXFS_MINIVERSION",
    "TXFS_MINIVERSION_COMMITTED_VIEW",
    "TXFS_MINIVERSION_DEFAULT_VIEW",
    "TXFS_MINIVERSION_DIRTY_VIEW",
    "TXF_ID",
    "TXF_LOG_RECORD_AFFECTED_FILE",
    "TXF_LOG_RECORD_BASE",
    "TXF_LOG_RECORD_GENERIC_TYPE_ABORT",
    "TXF_LOG_RECORD_GENERIC_TYPE_COMMIT",
    "TXF_LOG_RECORD_GENERIC_TYPE_DATA",
    "TXF_LOG_RECORD_GENERIC_TYPE_PREPARE",
    "TXF_LOG_RECORD_TRUNCATE",
    "TXF_LOG_RECORD_TYPE",
    "TXF_LOG_RECORD_TYPE_AFFECTED_FILE",
    "TXF_LOG_RECORD_TYPE_TRUNCATE",
    "TXF_LOG_RECORD_TYPE_WRITE",
    "TXF_LOG_RECORD_WRITE",
    "TerminateLogArchive",
    "TerminateReadLog",
    "TruncateLog",
    "TxfGetThreadMiniVersionForCreate",
    "TxfLogCreateFileReadContext",
    "TxfLogCreateRangeReadContext",
    "TxfLogDestroyReadContext",
    "TxfLogReadRecords",
    "TxfLogRecordGetFileName",
    "TxfLogRecordGetGenericType",
    "TxfReadMetadataInfo",
    "TxfSetThreadMiniVersionForCreate",
    "UnlockFile",
    "UnlockFileEx",
    "VER_FIND_FILE_FLAGS",
    "VER_FIND_FILE_STATUS",
    "VER_INSTALL_FILE_FLAGS",
    "VER_INSTALL_FILE_STATUS",
    "VFFF_ISSHAREDFILE",
    "VFF_BUFFTOOSMALL",
    "VFF_CURNEDEST",
    "VFF_FILEINUSE",
    "VFT2_DRV_COMM",
    "VFT2_DRV_DISPLAY",
    "VFT2_DRV_INPUTMETHOD",
    "VFT2_DRV_INSTALLABLE",
    "VFT2_DRV_KEYBOARD",
    "VFT2_DRV_LANGUAGE",
    "VFT2_DRV_MOUSE",
    "VFT2_DRV_NETWORK",
    "VFT2_DRV_PRINTER",
    "VFT2_DRV_SOUND",
    "VFT2_DRV_SYSTEM",
    "VFT2_DRV_VERSIONED_PRINTER",
    "VFT2_FONT_RASTER",
    "VFT2_FONT_TRUETYPE",
    "VFT2_FONT_VECTOR",
    "VFT2_UNKNOWN",
    "VFT_APP",
    "VFT_DLL",
    "VFT_DRV",
    "VFT_FONT",
    "VFT_STATIC_LIB",
    "VFT_UNKNOWN",
    "VFT_VXD",
    "VIFF_DONTDELETEOLD",
    "VIFF_FORCEINSTALL",
    "VIF_ACCESSVIOLATION",
    "VIF_BUFFTOOSMALL",
    "VIF_CANNOTCREATE",
    "VIF_CANNOTDELETE",
    "VIF_CANNOTDELETECUR",
    "VIF_CANNOTLOADCABINET",
    "VIF_CANNOTLOADLZ32",
    "VIF_CANNOTREADDST",
    "VIF_CANNOTREADSRC",
    "VIF_CANNOTRENAME",
    "VIF_DIFFCODEPG",
    "VIF_DIFFLANG",
    "VIF_DIFFTYPE",
    "VIF_FILEINUSE",
    "VIF_MISMATCH",
    "VIF_OUTOFMEMORY",
    "VIF_OUTOFSPACE",
    "VIF_SHARINGVIOLATION",
    "VIF_SRCOLD",
    "VIF_TEMPFILE",
    "VIF_WRITEPROT",
    "VOLUME_ALLOCATE_BC_STREAM_INPUT",
    "VOLUME_ALLOCATE_BC_STREAM_OUTPUT",
    "VOLUME_ALLOCATION_HINT_INPUT",
    "VOLUME_ALLOCATION_HINT_OUTPUT",
    "VOLUME_CRITICAL_IO",
    "VOLUME_FAILOVER_SET",
    "VOLUME_GET_BC_PROPERTIES_INPUT",
    "VOLUME_GET_BC_PROPERTIES_OUTPUT",
    "VOLUME_LOGICAL_OFFSET",
    "VOLUME_NUMBER",
    "VOLUME_PHYSICAL_OFFSET",
    "VOLUME_PHYSICAL_OFFSETS",
    "VOLUME_READ_PLEX_INPUT",
    "VOLUME_SET_GPT_ATTRIBUTES_INFORMATION",
    "VOLUME_SHRINK_INFO",
    "VOS_DOS",
    "VOS_DOS_WINDOWS16",
    "VOS_DOS_WINDOWS32",
    "VOS_NT",
    "VOS_NT_WINDOWS32",
    "VOS_OS216",
    "VOS_OS216_PM16",
    "VOS_OS232",
    "VOS_OS232_PM32",
    "VOS_UNKNOWN",
    "VOS_WINCE",
    "VOS__BASE",
    "VOS__PM16",
    "VOS__PM32",
    "VOS__WINDOWS16",
    "VOS__WINDOWS32",
    "VS_FFI_FILEFLAGSMASK",
    "VS_FFI_SIGNATURE",
    "VS_FFI_STRUCVERSION",
    "VS_FF_DEBUG",
    "VS_FF_INFOINFERRED",
    "VS_FF_PATCHED",
    "VS_FF_PRERELEASE",
    "VS_FF_PRIVATEBUILD",
    "VS_FF_SPECIALBUILD",
    "VS_FIXEDFILEINFO",
    "VS_FIXEDFILEINFO_FILE_FLAGS",
    "VS_FIXEDFILEINFO_FILE_OS",
    "VS_FIXEDFILEINFO_FILE_SUBTYPE",
    "VS_FIXEDFILEINFO_FILE_TYPE",
    "VS_USER_DEFINED",
    "VS_VERSION_INFO",
    "ValidateLog",
    "VerFindFileA",
    "VerFindFileW",
    "VerInstallFileA",
    "VerInstallFileW",
    "VerLanguageNameA",
    "VerLanguageNameW",
    "VerQueryValueA",
    "VerQueryValueW",
    "WIM_BOOT_NOT_OS_WIM",
    "WIM_BOOT_OS_WIM",
    "WIM_ENTRY_FLAG_NOT_ACTIVE",
    "WIM_ENTRY_FLAG_SUSPENDED",
    "WIM_ENTRY_INFO",
    "WIM_EXTERNAL_FILE_INFO",
    "WIM_EXTERNAL_FILE_INFO_FLAG_NOT_ACTIVE",
    "WIM_EXTERNAL_FILE_INFO_FLAG_SUSPENDED",
    "WIM_PROVIDER_HASH_SIZE",
    "WIN32_FILE_ATTRIBUTE_DATA",
    "WIN32_FIND_DATAA",
    "WIN32_FIND_DATAW",
    "WIN32_FIND_STREAM_DATA",
    "WIN32_STREAM_ID",
    "WINEFS_SETUSERKEY_SET_CAPABILITIES",
    "WIN_STREAM_ID",
    "WOF_FILE_COMPRESSION_INFO_V0",
    "WOF_FILE_COMPRESSION_INFO_V1",
    "WOF_PROVIDER_FILE",
    "WOF_PROVIDER_WIM",
    "WRITE_DAC",
    "WRITE_OWNER",
    "WofEnumEntries",
    "WofEnumEntryProc",
    "WofEnumFilesProc",
    "WofFileEnumFiles",
    "WofGetDriverVersion",
    "WofIsExternalFile",
    "WofSetFileDataLocation",
    "WofShouldCompressBinaries",
    "WofWimAddEntry",
    "WofWimEnumFiles",
    "WofWimRemoveEntry",
    "WofWimSuspendEntry",
    "WofWimUpdateEntry",
    "Wow64DisableWow64FsRedirection",
    "Wow64EnableWow64FsRedirection",
    "Wow64RevertWow64FsRedirection",
    "WriteEncryptedFileRaw",
    "WriteFile",
    "WriteFileEx",
    "WriteFileGather",
    "WriteLogRestartArea",
    "WriteTapemark",
    "_FT_TYPES_DEFINITION_",
]
_arch_optional = [
]
