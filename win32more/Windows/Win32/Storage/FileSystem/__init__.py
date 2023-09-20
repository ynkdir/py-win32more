from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Security
import win32more.Windows.Win32.Security.Cryptography
import win32more.Windows.Win32.Storage.FileSystem
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.IO
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
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
PARTITION_BASIC_DATA_GUID: Guid = Guid('{ebd0a0a2-b9e5-4433-87c0-68b6b72699c7}')
PARTITION_BSP_GUID: Guid = Guid('{57434f53-4df9-45b9-8e9e-2370f006457c}')
PARTITION_CLUSTER_GUID: Guid = Guid('{db97dba9-0840-4bae-97f0-ffb9a327c7e1}')
PARTITION_DPP_GUID: Guid = Guid('{57434f53-94cb-43f0-a533-d73c10cfa57d}')
PARTITION_ENTRY_UNUSED_GUID: Guid = Guid('{00000000-0000-0000-0000-000000000000}')
PARTITION_LDM_DATA_GUID: Guid = Guid('{af9b60a0-1431-4f62-bc68-3311714a69ad}')
PARTITION_LDM_METADATA_GUID: Guid = Guid('{5808c8aa-7e8f-42e0-85d2-e1e90434cfb3}')
PARTITION_LEGACY_BL_GUID: Guid = Guid('{424ca0e2-7cb2-4fb9-8143-c52a99398bc6}')
PARTITION_LEGACY_BL_GUID_BACKUP: Guid = Guid('{424c3e6c-d79f-49cb-935d-36d71467a288}')
PARTITION_MAIN_OS_GUID: Guid = Guid('{57434f53-8f45-405e-8a23-186d8a4330d3}')
PARTITION_MSFT_RECOVERY_GUID: Guid = Guid('{de94bba4-06d1-4d40-a16a-bfd50179d6ac}')
PARTITION_MSFT_RESERVED_GUID: Guid = Guid('{e3c9e316-0b5c-4db8-817d-f92df00215ae}')
PARTITION_MSFT_SNAPSHOT_GUID: Guid = Guid('{caddebf1-4400-4de8-b103-12117dcf3ccf}')
PARTITION_OS_DATA_GUID: Guid = Guid('{57434f53-23f2-44d5-a830-67bbdaa609f9}')
PARTITION_PATCH_GUID: Guid = Guid('{8967a686-96aa-6aa8-9589-a84256541090}')
PARTITION_PRE_INSTALLED_GUID: Guid = Guid('{57434f53-7fe0-4196-9b42-427b51643484}')
PARTITION_SBL_CACHE_SSD_GUID: Guid = Guid('{eeff8352-dd2a-44db-ae83-bee1cf7481dc}')
PARTITION_SBL_CACHE_SSD_RESERVED_GUID: Guid = Guid('{dcc0c7c1-55ad-4f17-9d43-4bc776e0117e}')
PARTITION_SBL_CACHE_HDD_GUID: Guid = Guid('{03aaa829-ebfc-4e7e-aac9-c4d76c63b24b}')
PARTITION_SERVICING_FILES_GUID: Guid = Guid('{57434f53-432e-4014-ae4c-8deaa9c0006a}')
PARTITION_SERVICING_METADATA_GUID: Guid = Guid('{57434f53-c691-4a05-bb4e-703dafd229ce}')
PARTITION_SERVICING_RESERVE_GUID: Guid = Guid('{57434f53-4b81-460b-a319-ffb6fe136d14}')
PARTITION_SERVICING_STAGING_ROOT_GUID: Guid = Guid('{57434f53-e84d-4e84-aaf3-ecbbbd04b9df}')
PARTITION_SPACES_GUID: Guid = Guid('{e75caf8f-f680-4cee-afa3-b001e56efc2d}')
PARTITION_SPACES_DATA_GUID: Guid = Guid('{e7addcb4-dc34-4539-9a76-ebbd07be6f7e}')
PARTITION_SYSTEM_GUID: Guid = Guid('{c12a7328-f81f-11d2-ba4b-00a0c93ec93b}')
PARTITION_WINDOWS_SYSTEM_GUID: Guid = Guid('{57434f53-e3e3-4631-a5c5-26d2243873aa}')
_FT_TYPES_DEFINITION_: UInt32 = 1
CLFS_MGMT_POLICY_VERSION: UInt32 = 1
LOG_POLICY_OVERWRITE: UInt32 = 1
LOG_POLICY_PERSIST: UInt32 = 2
CLFS_MGMT_CLIENT_REGISTRATION_VERSION: UInt32 = 1
CLSID_DiskQuotaControl: Guid = Guid('{7988b571-ec89-11cf-9c00-00aa00a14f56}')
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
SHARE_QOS_POLICY_PARMNUM: UInt32 = 504
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
SHI1005_FLAGS_ISOLATED_TRANSPORT: UInt32 = 2097152
SHI1005_FLAGS_DISABLE_DIRECTORY_HANDLE_LEASING: UInt32 = 4194304
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
def SearchPathW(lpPath: win32more.Windows.Win32.Foundation.PWSTR, lpFileName: win32more.Windows.Win32.Foundation.PWSTR, lpExtension: win32more.Windows.Win32.Foundation.PWSTR, nBufferLength: UInt32, lpBuffer: win32more.Windows.Win32.Foundation.PWSTR, lpFilePart: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def SearchPathA(lpPath: win32more.Windows.Win32.Foundation.PSTR, lpFileName: win32more.Windows.Win32.Foundation.PSTR, lpExtension: win32more.Windows.Win32.Foundation.PSTR, nBufferLength: UInt32, lpBuffer: win32more.Windows.Win32.Foundation.PSTR, lpFilePart: POINTER(win32more.Windows.Win32.Foundation.PSTR)) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def CompareFileTime(lpFileTime1: POINTER(win32more.Windows.Win32.Foundation.FILETIME_head), lpFileTime2: POINTER(win32more.Windows.Win32.Foundation.FILETIME_head)) -> Int32: ...
@winfunctype('KERNEL32.dll')
def CreateDirectoryA(lpPathName: win32more.Windows.Win32.Foundation.PSTR, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateDirectoryW(lpPathName: win32more.Windows.Win32.Foundation.PWSTR, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateFileA(lpFileName: win32more.Windows.Win32.Foundation.PSTR, dwDesiredAccess: UInt32, dwShareMode: win32more.Windows.Win32.Storage.FileSystem.FILE_SHARE_MODE, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES_head), dwCreationDisposition: win32more.Windows.Win32.Storage.FileSystem.FILE_CREATION_DISPOSITION, dwFlagsAndAttributes: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES, hTemplateFile: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def CreateFileW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, dwDesiredAccess: UInt32, dwShareMode: win32more.Windows.Win32.Storage.FileSystem.FILE_SHARE_MODE, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES_head), dwCreationDisposition: win32more.Windows.Win32.Storage.FileSystem.FILE_CREATION_DISPOSITION, dwFlagsAndAttributes: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES, hTemplateFile: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def DefineDosDeviceW(dwFlags: win32more.Windows.Win32.Storage.FileSystem.DEFINE_DOS_DEVICE_FLAGS, lpDeviceName: win32more.Windows.Win32.Foundation.PWSTR, lpTargetPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DeleteFileA(lpFileName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DeleteFileW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DeleteVolumeMountPointW(lpszVolumeMountPoint: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FileTimeToLocalFileTime(lpFileTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME_head), lpLocalFileTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FindClose(hFindFile: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FindCloseChangeNotification(hChangeHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FindFirstChangeNotificationA(lpPathName: win32more.Windows.Win32.Foundation.PSTR, bWatchSubtree: win32more.Windows.Win32.Foundation.BOOL, dwNotifyFilter: win32more.Windows.Win32.Storage.FileSystem.FILE_NOTIFY_CHANGE) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def FindFirstChangeNotificationW(lpPathName: win32more.Windows.Win32.Foundation.PWSTR, bWatchSubtree: win32more.Windows.Win32.Foundation.BOOL, dwNotifyFilter: win32more.Windows.Win32.Storage.FileSystem.FILE_NOTIFY_CHANGE) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def FindFirstFileA(lpFileName: win32more.Windows.Win32.Foundation.PSTR, lpFindFileData: POINTER(win32more.Windows.Win32.Storage.FileSystem.WIN32_FIND_DATAA_head)) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def FindFirstFileW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, lpFindFileData: POINTER(win32more.Windows.Win32.Storage.FileSystem.WIN32_FIND_DATAW_head)) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def FindFirstFileExA(lpFileName: win32more.Windows.Win32.Foundation.PSTR, fInfoLevelId: win32more.Windows.Win32.Storage.FileSystem.FINDEX_INFO_LEVELS, lpFindFileData: VoidPtr, fSearchOp: win32more.Windows.Win32.Storage.FileSystem.FINDEX_SEARCH_OPS, lpSearchFilter: VoidPtr, dwAdditionalFlags: win32more.Windows.Win32.Storage.FileSystem.FIND_FIRST_EX_FLAGS) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def FindFirstFileExW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, fInfoLevelId: win32more.Windows.Win32.Storage.FileSystem.FINDEX_INFO_LEVELS, lpFindFileData: VoidPtr, fSearchOp: win32more.Windows.Win32.Storage.FileSystem.FINDEX_SEARCH_OPS, lpSearchFilter: VoidPtr, dwAdditionalFlags: win32more.Windows.Win32.Storage.FileSystem.FIND_FIRST_EX_FLAGS) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def FindFirstVolumeW(lpszVolumeName: win32more.Windows.Win32.Foundation.PWSTR, cchBufferLength: UInt32) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def FindNextChangeNotification(hChangeHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FindNextFileA(hFindFile: win32more.Windows.Win32.Foundation.HANDLE, lpFindFileData: POINTER(win32more.Windows.Win32.Storage.FileSystem.WIN32_FIND_DATAA_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FindNextFileW(hFindFile: win32more.Windows.Win32.Foundation.HANDLE, lpFindFileData: POINTER(win32more.Windows.Win32.Storage.FileSystem.WIN32_FIND_DATAW_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FindNextVolumeW(hFindVolume: win32more.Windows.Win32.Foundation.HANDLE, lpszVolumeName: win32more.Windows.Win32.Foundation.PWSTR, cchBufferLength: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FindVolumeClose(hFindVolume: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FlushFileBuffers(hFile: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetDiskFreeSpaceA(lpRootPathName: win32more.Windows.Win32.Foundation.PSTR, lpSectorsPerCluster: POINTER(UInt32), lpBytesPerSector: POINTER(UInt32), lpNumberOfFreeClusters: POINTER(UInt32), lpTotalNumberOfClusters: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetDiskFreeSpaceW(lpRootPathName: win32more.Windows.Win32.Foundation.PWSTR, lpSectorsPerCluster: POINTER(UInt32), lpBytesPerSector: POINTER(UInt32), lpNumberOfFreeClusters: POINTER(UInt32), lpTotalNumberOfClusters: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetDiskFreeSpaceExA(lpDirectoryName: win32more.Windows.Win32.Foundation.PSTR, lpFreeBytesAvailableToCaller: POINTER(UInt64), lpTotalNumberOfBytes: POINTER(UInt64), lpTotalNumberOfFreeBytes: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetDiskFreeSpaceExW(lpDirectoryName: win32more.Windows.Win32.Foundation.PWSTR, lpFreeBytesAvailableToCaller: POINTER(UInt64), lpTotalNumberOfBytes: POINTER(UInt64), lpTotalNumberOfFreeBytes: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetDiskSpaceInformationA(rootPath: win32more.Windows.Win32.Foundation.PSTR, diskSpaceInfo: POINTER(win32more.Windows.Win32.Storage.FileSystem.DISK_SPACE_INFORMATION_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def GetDiskSpaceInformationW(rootPath: win32more.Windows.Win32.Foundation.PWSTR, diskSpaceInfo: POINTER(win32more.Windows.Win32.Storage.FileSystem.DISK_SPACE_INFORMATION_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def GetDriveTypeA(lpRootPathName: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetDriveTypeW(lpRootPathName: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetFileAttributesA(lpFileName: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetFileAttributesW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetFileAttributesExA(lpFileName: win32more.Windows.Win32.Foundation.PSTR, fInfoLevelId: win32more.Windows.Win32.Storage.FileSystem.GET_FILEEX_INFO_LEVELS, lpFileInformation: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetFileAttributesExW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, fInfoLevelId: win32more.Windows.Win32.Storage.FileSystem.GET_FILEEX_INFO_LEVELS, lpFileInformation: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetFileInformationByHandle(hFile: win32more.Windows.Win32.Foundation.HANDLE, lpFileInformation: POINTER(win32more.Windows.Win32.Storage.FileSystem.BY_HANDLE_FILE_INFORMATION_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetFileSize(hFile: win32more.Windows.Win32.Foundation.HANDLE, lpFileSizeHigh: POINTER(UInt32)) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetFileSizeEx(hFile: win32more.Windows.Win32.Foundation.HANDLE, lpFileSize: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetFileType(hFile: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Storage.FileSystem.FILE_TYPE: ...
@winfunctype('KERNEL32.dll')
def GetFinalPathNameByHandleA(hFile: win32more.Windows.Win32.Foundation.HANDLE, lpszFilePath: win32more.Windows.Win32.Foundation.PSTR, cchFilePath: UInt32, dwFlags: win32more.Windows.Win32.Storage.FileSystem.GETFINALPATHNAMEBYHANDLE_FLAGS) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetFinalPathNameByHandleW(hFile: win32more.Windows.Win32.Foundation.HANDLE, lpszFilePath: win32more.Windows.Win32.Foundation.PWSTR, cchFilePath: UInt32, dwFlags: win32more.Windows.Win32.Storage.FileSystem.GETFINALPATHNAMEBYHANDLE_FLAGS) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetFileTime(hFile: win32more.Windows.Win32.Foundation.HANDLE, lpCreationTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME_head), lpLastAccessTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME_head), lpLastWriteTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetFullPathNameW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, nBufferLength: UInt32, lpBuffer: win32more.Windows.Win32.Foundation.PWSTR, lpFilePart: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetFullPathNameA(lpFileName: win32more.Windows.Win32.Foundation.PSTR, nBufferLength: UInt32, lpBuffer: win32more.Windows.Win32.Foundation.PSTR, lpFilePart: POINTER(win32more.Windows.Win32.Foundation.PSTR)) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetLogicalDrives() -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetLogicalDriveStringsW(nBufferLength: UInt32, lpBuffer: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetLongPathNameA(lpszShortPath: win32more.Windows.Win32.Foundation.PSTR, lpszLongPath: win32more.Windows.Win32.Foundation.PSTR, cchBuffer: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetLongPathNameW(lpszShortPath: win32more.Windows.Win32.Foundation.PWSTR, lpszLongPath: win32more.Windows.Win32.Foundation.PWSTR, cchBuffer: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def AreShortNamesEnabled(Handle: win32more.Windows.Win32.Foundation.HANDLE, Enabled: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetShortPathNameW(lpszLongPath: win32more.Windows.Win32.Foundation.PWSTR, lpszShortPath: win32more.Windows.Win32.Foundation.PWSTR, cchBuffer: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetTempFileNameW(lpPathName: win32more.Windows.Win32.Foundation.PWSTR, lpPrefixString: win32more.Windows.Win32.Foundation.PWSTR, uUnique: UInt32, lpTempFileName: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetVolumeInformationByHandleW(hFile: win32more.Windows.Win32.Foundation.HANDLE, lpVolumeNameBuffer: win32more.Windows.Win32.Foundation.PWSTR, nVolumeNameSize: UInt32, lpVolumeSerialNumber: POINTER(UInt32), lpMaximumComponentLength: POINTER(UInt32), lpFileSystemFlags: POINTER(UInt32), lpFileSystemNameBuffer: win32more.Windows.Win32.Foundation.PWSTR, nFileSystemNameSize: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetVolumeInformationW(lpRootPathName: win32more.Windows.Win32.Foundation.PWSTR, lpVolumeNameBuffer: win32more.Windows.Win32.Foundation.PWSTR, nVolumeNameSize: UInt32, lpVolumeSerialNumber: POINTER(UInt32), lpMaximumComponentLength: POINTER(UInt32), lpFileSystemFlags: POINTER(UInt32), lpFileSystemNameBuffer: win32more.Windows.Win32.Foundation.PWSTR, nFileSystemNameSize: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetVolumePathNameW(lpszFileName: win32more.Windows.Win32.Foundation.PWSTR, lpszVolumePathName: win32more.Windows.Win32.Foundation.PWSTR, cchBufferLength: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def LocalFileTimeToFileTime(lpLocalFileTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME_head), lpFileTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def LockFile(hFile: win32more.Windows.Win32.Foundation.HANDLE, dwFileOffsetLow: UInt32, dwFileOffsetHigh: UInt32, nNumberOfBytesToLockLow: UInt32, nNumberOfBytesToLockHigh: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def LockFileEx(hFile: win32more.Windows.Win32.Foundation.HANDLE, dwFlags: win32more.Windows.Win32.Storage.FileSystem.LOCK_FILE_FLAGS, dwReserved: UInt32, nNumberOfBytesToLockLow: UInt32, nNumberOfBytesToLockHigh: UInt32, lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def QueryDosDeviceW(lpDeviceName: win32more.Windows.Win32.Foundation.PWSTR, lpTargetPath: win32more.Windows.Win32.Foundation.PWSTR, ucchMax: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def ReadFile(hFile: win32more.Windows.Win32.Foundation.HANDLE, lpBuffer: POINTER(Byte), nNumberOfBytesToRead: UInt32, lpNumberOfBytesRead: POINTER(UInt32), lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ReadFileEx(hFile: win32more.Windows.Win32.Foundation.HANDLE, lpBuffer: POINTER(Byte), nNumberOfBytesToRead: UInt32, lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED_head), lpCompletionRoutine: win32more.Windows.Win32.System.IO.LPOVERLAPPED_COMPLETION_ROUTINE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ReadFileScatter(hFile: win32more.Windows.Win32.Foundation.HANDLE, aSegmentArray: POINTER(win32more.Windows.Win32.Storage.FileSystem.FILE_SEGMENT_ELEMENT_head), nNumberOfBytesToRead: UInt32, lpReserved: POINTER(UInt32), lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def RemoveDirectoryA(lpPathName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def RemoveDirectoryW(lpPathName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetEndOfFile(hFile: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetFileAttributesA(lpFileName: win32more.Windows.Win32.Foundation.PSTR, dwFileAttributes: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetFileAttributesW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, dwFileAttributes: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetFileInformationByHandle(hFile: win32more.Windows.Win32.Foundation.HANDLE, FileInformationClass: win32more.Windows.Win32.Storage.FileSystem.FILE_INFO_BY_HANDLE_CLASS, lpFileInformation: VoidPtr, dwBufferSize: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetFilePointer(hFile: win32more.Windows.Win32.Foundation.HANDLE, lDistanceToMove: Int32, lpDistanceToMoveHigh: POINTER(Int32), dwMoveMethod: win32more.Windows.Win32.Storage.FileSystem.SET_FILE_POINTER_MOVE_METHOD) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def SetFilePointerEx(hFile: win32more.Windows.Win32.Foundation.HANDLE, liDistanceToMove: Int64, lpNewFilePointer: POINTER(Int64), dwMoveMethod: win32more.Windows.Win32.Storage.FileSystem.SET_FILE_POINTER_MOVE_METHOD) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetFileTime(hFile: win32more.Windows.Win32.Foundation.HANDLE, lpCreationTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME_head), lpLastAccessTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME_head), lpLastWriteTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetFileValidData(hFile: win32more.Windows.Win32.Foundation.HANDLE, ValidDataLength: Int64) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def UnlockFile(hFile: win32more.Windows.Win32.Foundation.HANDLE, dwFileOffsetLow: UInt32, dwFileOffsetHigh: UInt32, nNumberOfBytesToUnlockLow: UInt32, nNumberOfBytesToUnlockHigh: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def UnlockFileEx(hFile: win32more.Windows.Win32.Foundation.HANDLE, dwReserved: UInt32, nNumberOfBytesToUnlockLow: UInt32, nNumberOfBytesToUnlockHigh: UInt32, lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WriteFile(hFile: win32more.Windows.Win32.Foundation.HANDLE, lpBuffer: POINTER(Byte), nNumberOfBytesToWrite: UInt32, lpNumberOfBytesWritten: POINTER(UInt32), lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WriteFileEx(hFile: win32more.Windows.Win32.Foundation.HANDLE, lpBuffer: POINTER(Byte), nNumberOfBytesToWrite: UInt32, lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED_head), lpCompletionRoutine: win32more.Windows.Win32.System.IO.LPOVERLAPPED_COMPLETION_ROUTINE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WriteFileGather(hFile: win32more.Windows.Win32.Foundation.HANDLE, aSegmentArray: POINTER(win32more.Windows.Win32.Storage.FileSystem.FILE_SEGMENT_ELEMENT_head), nNumberOfBytesToWrite: UInt32, lpReserved: POINTER(UInt32), lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetTempPathW(nBufferLength: UInt32, lpBuffer: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetVolumeNameForVolumeMountPointW(lpszVolumeMountPoint: win32more.Windows.Win32.Foundation.PWSTR, lpszVolumeName: win32more.Windows.Win32.Foundation.PWSTR, cchBufferLength: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetVolumePathNamesForVolumeNameW(lpszVolumeName: win32more.Windows.Win32.Foundation.PWSTR, lpszVolumePathNames: win32more.Windows.Win32.Foundation.PWSTR, cchBufferLength: UInt32, lpcchReturnLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateFile2(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, dwDesiredAccess: UInt32, dwShareMode: win32more.Windows.Win32.Storage.FileSystem.FILE_SHARE_MODE, dwCreationDisposition: win32more.Windows.Win32.Storage.FileSystem.FILE_CREATION_DISPOSITION, pCreateExParams: POINTER(win32more.Windows.Win32.Storage.FileSystem.CREATEFILE2_EXTENDED_PARAMETERS_head)) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def SetFileIoOverlappedRange(FileHandle: win32more.Windows.Win32.Foundation.HANDLE, OverlappedRangeStart: POINTER(Byte), Length: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetCompressedFileSizeA(lpFileName: win32more.Windows.Win32.Foundation.PSTR, lpFileSizeHigh: POINTER(UInt32)) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetCompressedFileSizeW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, lpFileSizeHigh: POINTER(UInt32)) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def FindFirstStreamW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, InfoLevel: win32more.Windows.Win32.Storage.FileSystem.STREAM_INFO_LEVELS, lpFindStreamData: VoidPtr, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def FindNextStreamW(hFindStream: win32more.Windows.Win32.Foundation.HANDLE, lpFindStreamData: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def AreFileApisANSI() -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetTempPathA(nBufferLength: UInt32, lpBuffer: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def FindFirstFileNameW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, StringLength: POINTER(UInt32), LinkName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def FindNextFileNameW(hFindStream: win32more.Windows.Win32.Foundation.HANDLE, StringLength: POINTER(UInt32), LinkName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetVolumeInformationA(lpRootPathName: win32more.Windows.Win32.Foundation.PSTR, lpVolumeNameBuffer: win32more.Windows.Win32.Foundation.PSTR, nVolumeNameSize: UInt32, lpVolumeSerialNumber: POINTER(UInt32), lpMaximumComponentLength: POINTER(UInt32), lpFileSystemFlags: POINTER(UInt32), lpFileSystemNameBuffer: win32more.Windows.Win32.Foundation.PSTR, nFileSystemNameSize: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetTempFileNameA(lpPathName: win32more.Windows.Win32.Foundation.PSTR, lpPrefixString: win32more.Windows.Win32.Foundation.PSTR, uUnique: UInt32, lpTempFileName: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def SetFileApisToOEM() -> Void: ...
@winfunctype('KERNEL32.dll')
def SetFileApisToANSI() -> Void: ...
@winfunctype('KERNEL32.dll')
def GetTempPath2W(BufferLength: UInt32, Buffer: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetTempPath2A(BufferLength: UInt32, Buffer: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('api-ms-win-core-file-fromapp-l1-1-0.dll')
def CopyFileFromAppW(lpExistingFileName: win32more.Windows.Win32.Foundation.PWSTR, lpNewFileName: win32more.Windows.Win32.Foundation.PWSTR, bFailIfExists: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-file-fromapp-l1-1-0.dll')
def CreateDirectoryFromAppW(lpPathName: win32more.Windows.Win32.Foundation.PWSTR, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-file-fromapp-l1-1-0.dll')
def CreateFileFromAppW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, dwDesiredAccess: UInt32, dwShareMode: UInt32, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES_head), dwCreationDisposition: UInt32, dwFlagsAndAttributes: UInt32, hTemplateFile: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('api-ms-win-core-file-fromapp-l1-1-0.dll')
def CreateFile2FromAppW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, dwDesiredAccess: UInt32, dwShareMode: UInt32, dwCreationDisposition: UInt32, pCreateExParams: POINTER(win32more.Windows.Win32.Storage.FileSystem.CREATEFILE2_EXTENDED_PARAMETERS_head)) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('api-ms-win-core-file-fromapp-l1-1-0.dll')
def DeleteFileFromAppW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-file-fromapp-l1-1-0.dll')
def FindFirstFileExFromAppW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, fInfoLevelId: win32more.Windows.Win32.Storage.FileSystem.FINDEX_INFO_LEVELS, lpFindFileData: VoidPtr, fSearchOp: win32more.Windows.Win32.Storage.FileSystem.FINDEX_SEARCH_OPS, lpSearchFilter: VoidPtr, dwAdditionalFlags: UInt32) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('api-ms-win-core-file-fromapp-l1-1-0.dll')
def GetFileAttributesExFromAppW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, fInfoLevelId: win32more.Windows.Win32.Storage.FileSystem.GET_FILEEX_INFO_LEVELS, lpFileInformation: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-file-fromapp-l1-1-0.dll')
def MoveFileFromAppW(lpExistingFileName: win32more.Windows.Win32.Foundation.PWSTR, lpNewFileName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-file-fromapp-l1-1-0.dll')
def RemoveDirectoryFromAppW(lpPathName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-file-fromapp-l1-1-0.dll')
def ReplaceFileFromAppW(lpReplacedFileName: win32more.Windows.Win32.Foundation.PWSTR, lpReplacementFileName: win32more.Windows.Win32.Foundation.PWSTR, lpBackupFileName: win32more.Windows.Win32.Foundation.PWSTR, dwReplaceFlags: UInt32, lpExclude: VoidPtr, lpReserved: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-file-fromapp-l1-1-0.dll')
def SetFileAttributesFromAppW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, dwFileAttributes: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('VERSION.dll')
def VerFindFileA(uFlags: win32more.Windows.Win32.Storage.FileSystem.VER_FIND_FILE_FLAGS, szFileName: win32more.Windows.Win32.Foundation.PSTR, szWinDir: win32more.Windows.Win32.Foundation.PSTR, szAppDir: win32more.Windows.Win32.Foundation.PSTR, szCurDir: win32more.Windows.Win32.Foundation.PSTR, puCurDirLen: POINTER(UInt32), szDestDir: win32more.Windows.Win32.Foundation.PSTR, puDestDirLen: POINTER(UInt32)) -> win32more.Windows.Win32.Storage.FileSystem.VER_FIND_FILE_STATUS: ...
@winfunctype('VERSION.dll')
def VerFindFileW(uFlags: win32more.Windows.Win32.Storage.FileSystem.VER_FIND_FILE_FLAGS, szFileName: win32more.Windows.Win32.Foundation.PWSTR, szWinDir: win32more.Windows.Win32.Foundation.PWSTR, szAppDir: win32more.Windows.Win32.Foundation.PWSTR, szCurDir: win32more.Windows.Win32.Foundation.PWSTR, puCurDirLen: POINTER(UInt32), szDestDir: win32more.Windows.Win32.Foundation.PWSTR, puDestDirLen: POINTER(UInt32)) -> win32more.Windows.Win32.Storage.FileSystem.VER_FIND_FILE_STATUS: ...
@winfunctype('VERSION.dll')
def VerInstallFileA(uFlags: win32more.Windows.Win32.Storage.FileSystem.VER_INSTALL_FILE_FLAGS, szSrcFileName: win32more.Windows.Win32.Foundation.PSTR, szDestFileName: win32more.Windows.Win32.Foundation.PSTR, szSrcDir: win32more.Windows.Win32.Foundation.PSTR, szDestDir: win32more.Windows.Win32.Foundation.PSTR, szCurDir: win32more.Windows.Win32.Foundation.PSTR, szTmpFile: win32more.Windows.Win32.Foundation.PSTR, puTmpFileLen: POINTER(UInt32)) -> win32more.Windows.Win32.Storage.FileSystem.VER_INSTALL_FILE_STATUS: ...
@winfunctype('VERSION.dll')
def VerInstallFileW(uFlags: win32more.Windows.Win32.Storage.FileSystem.VER_INSTALL_FILE_FLAGS, szSrcFileName: win32more.Windows.Win32.Foundation.PWSTR, szDestFileName: win32more.Windows.Win32.Foundation.PWSTR, szSrcDir: win32more.Windows.Win32.Foundation.PWSTR, szDestDir: win32more.Windows.Win32.Foundation.PWSTR, szCurDir: win32more.Windows.Win32.Foundation.PWSTR, szTmpFile: win32more.Windows.Win32.Foundation.PWSTR, puTmpFileLen: POINTER(UInt32)) -> win32more.Windows.Win32.Storage.FileSystem.VER_INSTALL_FILE_STATUS: ...
@winfunctype('VERSION.dll')
def GetFileVersionInfoSizeA(lptstrFilename: win32more.Windows.Win32.Foundation.PSTR, lpdwHandle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('VERSION.dll')
def GetFileVersionInfoSizeW(lptstrFilename: win32more.Windows.Win32.Foundation.PWSTR, lpdwHandle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('VERSION.dll')
def GetFileVersionInfoA(lptstrFilename: win32more.Windows.Win32.Foundation.PSTR, dwHandle: UInt32, dwLen: UInt32, lpData: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('VERSION.dll')
def GetFileVersionInfoW(lptstrFilename: win32more.Windows.Win32.Foundation.PWSTR, dwHandle: UInt32, dwLen: UInt32, lpData: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('VERSION.dll')
def GetFileVersionInfoSizeExA(dwFlags: win32more.Windows.Win32.Storage.FileSystem.GET_FILE_VERSION_INFO_FLAGS, lpwstrFilename: win32more.Windows.Win32.Foundation.PSTR, lpdwHandle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('VERSION.dll')
def GetFileVersionInfoSizeExW(dwFlags: win32more.Windows.Win32.Storage.FileSystem.GET_FILE_VERSION_INFO_FLAGS, lpwstrFilename: win32more.Windows.Win32.Foundation.PWSTR, lpdwHandle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('VERSION.dll')
def GetFileVersionInfoExA(dwFlags: win32more.Windows.Win32.Storage.FileSystem.GET_FILE_VERSION_INFO_FLAGS, lpwstrFilename: win32more.Windows.Win32.Foundation.PSTR, dwHandle: UInt32, dwLen: UInt32, lpData: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('VERSION.dll')
def GetFileVersionInfoExW(dwFlags: win32more.Windows.Win32.Storage.FileSystem.GET_FILE_VERSION_INFO_FLAGS, lpwstrFilename: win32more.Windows.Win32.Foundation.PWSTR, dwHandle: UInt32, dwLen: UInt32, lpData: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def VerLanguageNameA(wLang: UInt32, szLang: win32more.Windows.Win32.Foundation.PSTR, cchLang: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def VerLanguageNameW(wLang: UInt32, szLang: win32more.Windows.Win32.Foundation.PWSTR, cchLang: UInt32) -> UInt32: ...
@winfunctype('VERSION.dll')
def VerQueryValueA(pBlock: VoidPtr, lpSubBlock: win32more.Windows.Win32.Foundation.PSTR, lplpBuffer: POINTER(VoidPtr), puLen: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('VERSION.dll')
def VerQueryValueW(pBlock: VoidPtr, lpSubBlock: win32more.Windows.Win32.Foundation.PWSTR, lplpBuffer: POINTER(VoidPtr), puLen: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def LsnEqual(plsn1: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN_head), plsn2: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN_head)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('clfsw32.dll')
def LsnLess(plsn1: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN_head), plsn2: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN_head)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('clfsw32.dll')
def LsnGreater(plsn1: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN_head), plsn2: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN_head)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('clfsw32.dll')
def LsnNull(plsn: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN_head)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('clfsw32.dll')
def LsnContainer(plsn: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN_head)) -> UInt32: ...
@winfunctype('clfsw32.dll')
def LsnCreate(cidContainer: UInt32, offBlock: UInt32, cRecord: UInt32) -> win32more.Windows.Win32.Storage.FileSystem.CLS_LSN: ...
@winfunctype('clfsw32.dll')
def LsnBlockOffset(plsn: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN_head)) -> UInt32: ...
@winfunctype('clfsw32.dll')
def LsnRecordSequence(plsn: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN_head)) -> UInt32: ...
@winfunctype('clfsw32.dll')
def LsnInvalid(plsn: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN_head)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('clfsw32.dll')
def LsnIncrement(plsn: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN_head)) -> win32more.Windows.Win32.Storage.FileSystem.CLS_LSN: ...
@winfunctype('clfsw32.dll')
def CreateLogFile(pszLogFileName: win32more.Windows.Win32.Foundation.PWSTR, fDesiredAccess: UInt32, dwShareMode: win32more.Windows.Win32.Storage.FileSystem.FILE_SHARE_MODE, psaLogFile: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES_head), fCreateDisposition: win32more.Windows.Win32.Storage.FileSystem.FILE_CREATION_DISPOSITION, fFlagsAndAttributes: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('clfsw32.dll')
def DeleteLogByHandle(hLog: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def DeleteLogFile(pszLogFileName: win32more.Windows.Win32.Foundation.PWSTR, pvReserved: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def AddLogContainer(hLog: win32more.Windows.Win32.Foundation.HANDLE, pcbContainer: POINTER(UInt64), pwszContainerPath: win32more.Windows.Win32.Foundation.PWSTR, pReserved: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def AddLogContainerSet(hLog: win32more.Windows.Win32.Foundation.HANDLE, cContainer: UInt16, pcbContainer: POINTER(UInt64), rgwszContainerPath: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pReserved: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def RemoveLogContainer(hLog: win32more.Windows.Win32.Foundation.HANDLE, pwszContainerPath: win32more.Windows.Win32.Foundation.PWSTR, fForce: win32more.Windows.Win32.Foundation.BOOL, pReserved: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def RemoveLogContainerSet(hLog: win32more.Windows.Win32.Foundation.HANDLE, cContainer: UInt16, rgwszContainerPath: POINTER(win32more.Windows.Win32.Foundation.PWSTR), fForce: win32more.Windows.Win32.Foundation.BOOL, pReserved: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def SetLogArchiveTail(hLog: win32more.Windows.Win32.Foundation.HANDLE, plsnArchiveTail: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN_head), pReserved: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def SetEndOfLog(hLog: win32more.Windows.Win32.Foundation.HANDLE, plsnEnd: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN_head), lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def TruncateLog(pvMarshal: VoidPtr, plsnEnd: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN_head), lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def CreateLogContainerScanContext(hLog: win32more.Windows.Win32.Foundation.HANDLE, cFromContainer: UInt32, cContainers: UInt32, eScanMode: Byte, pcxScan: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_SCAN_CONTEXT_head), pOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def ScanLogContainers(pcxScan: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_SCAN_CONTEXT_head), eScanMode: Byte, pReserved: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def AlignReservedLog(pvMarshal: VoidPtr, cReservedRecords: UInt32, rgcbReservation: POINTER(Int64), pcbAlignReservation: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def AllocReservedLog(pvMarshal: VoidPtr, cReservedRecords: UInt32, pcbAdjustment: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def FreeReservedLog(pvMarshal: VoidPtr, cReservedRecords: UInt32, pcbAdjustment: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def GetLogFileInformation(hLog: win32more.Windows.Win32.Foundation.HANDLE, pinfoBuffer: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_INFORMATION_head), cbBuffer: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def SetLogArchiveMode(hLog: win32more.Windows.Win32.Foundation.HANDLE, eMode: win32more.Windows.Win32.Storage.FileSystem.CLFS_LOG_ARCHIVE_MODE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def ReadLogRestartArea(pvMarshal: VoidPtr, ppvRestartBuffer: POINTER(VoidPtr), pcbRestartBuffer: POINTER(UInt32), plsn: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN_head), ppvContext: POINTER(VoidPtr), pOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def ReadPreviousLogRestartArea(pvReadContext: VoidPtr, ppvRestartBuffer: POINTER(VoidPtr), pcbRestartBuffer: POINTER(UInt32), plsnRestart: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN_head), pOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def WriteLogRestartArea(pvMarshal: VoidPtr, pvRestartBuffer: VoidPtr, cbRestartBuffer: UInt32, plsnBase: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN_head), fFlags: win32more.Windows.Win32.Storage.FileSystem.CLFS_FLAG, pcbWritten: POINTER(UInt32), plsnNext: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN_head), pOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def GetLogReservationInfo(pvMarshal: VoidPtr, pcbRecordNumber: POINTER(UInt32), pcbUserReservation: POINTER(Int64), pcbCommitReservation: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def AdvanceLogBase(pvMarshal: VoidPtr, plsnBase: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN_head), fFlags: UInt32, pOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def CloseAndResetLogFile(hLog: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def CreateLogMarshallingArea(hLog: win32more.Windows.Win32.Foundation.HANDLE, pfnAllocBuffer: win32more.Windows.Win32.Storage.FileSystem.CLFS_BLOCK_ALLOCATION, pfnFreeBuffer: win32more.Windows.Win32.Storage.FileSystem.CLFS_BLOCK_DEALLOCATION, pvBlockAllocContext: VoidPtr, cbMarshallingBuffer: UInt32, cMaxWriteBuffers: UInt32, cMaxReadBuffers: UInt32, ppvMarshal: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def DeleteLogMarshallingArea(pvMarshal: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def ReserveAndAppendLog(pvMarshal: VoidPtr, rgWriteEntries: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_WRITE_ENTRY_head), cWriteEntries: UInt32, plsnUndoNext: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN_head), plsnPrevious: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN_head), cReserveRecords: UInt32, rgcbReservation: POINTER(Int64), fFlags: win32more.Windows.Win32.Storage.FileSystem.CLFS_FLAG, plsn: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN_head), pOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def ReserveAndAppendLogAligned(pvMarshal: VoidPtr, rgWriteEntries: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_WRITE_ENTRY_head), cWriteEntries: UInt32, cbEntryAlignment: UInt32, plsnUndoNext: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN_head), plsnPrevious: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN_head), cReserveRecords: UInt32, rgcbReservation: POINTER(Int64), fFlags: win32more.Windows.Win32.Storage.FileSystem.CLFS_FLAG, plsn: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN_head), pOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def FlushLogBuffers(pvMarshal: VoidPtr, pOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def FlushLogToLsn(pvMarshalContext: VoidPtr, plsnFlush: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN_head), plsnLastFlushed: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN_head), pOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def ReadLogRecord(pvMarshal: VoidPtr, plsnFirst: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN_head), eContextMode: win32more.Windows.Win32.Storage.FileSystem.CLFS_CONTEXT_MODE, ppvReadBuffer: POINTER(VoidPtr), pcbReadBuffer: POINTER(UInt32), peRecordType: POINTER(Byte), plsnUndoNext: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN_head), plsnPrevious: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN_head), ppvReadContext: POINTER(VoidPtr), pOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def ReadNextLogRecord(pvReadContext: VoidPtr, ppvBuffer: POINTER(VoidPtr), pcbBuffer: POINTER(UInt32), peRecordType: POINTER(Byte), plsnUser: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN_head), plsnUndoNext: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN_head), plsnPrevious: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN_head), plsnRecord: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN_head), pOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def TerminateReadLog(pvCursorContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def PrepareLogArchive(hLog: win32more.Windows.Win32.Foundation.HANDLE, pszBaseLogFileName: win32more.Windows.Win32.Foundation.PWSTR, cLen: UInt32, plsnLow: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN_head), plsnHigh: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN_head), pcActualLength: POINTER(UInt32), poffBaseLogFileData: POINTER(UInt64), pcbBaseLogFileLength: POINTER(UInt64), plsnBase: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN_head), plsnLast: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN_head), plsnCurrentArchiveTail: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN_head), ppvArchiveContext: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def ReadLogArchiveMetadata(pvArchiveContext: VoidPtr, cbOffset: UInt32, cbBytesToRead: UInt32, pbReadBuffer: POINTER(Byte), pcbBytesRead: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def GetNextLogArchiveExtent(pvArchiveContext: VoidPtr, rgadExtent: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_ARCHIVE_DESCRIPTOR_head), cDescriptors: UInt32, pcDescriptorsReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def TerminateLogArchive(pvArchiveContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def ValidateLog(pszLogFileName: win32more.Windows.Win32.Foundation.PWSTR, psaLogFile: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES_head), pinfoBuffer: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_INFORMATION_head), pcbBuffer: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def GetLogContainerName(hLog: win32more.Windows.Win32.Foundation.HANDLE, cidLogicalContainer: UInt32, pwstrContainerName: win32more.Windows.Win32.Foundation.PWSTR, cLenContainerName: UInt32, pcActualLenContainerName: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def GetLogIoStatistics(hLog: win32more.Windows.Win32.Foundation.HANDLE, pvStatsBuffer: VoidPtr, cbStatsBuffer: UInt32, eStatsClass: win32more.Windows.Win32.Storage.FileSystem.CLFS_IOSTATS_CLASS, pcbStatsWritten: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def RegisterManageableLogClient(hLog: win32more.Windows.Win32.Foundation.HANDLE, pCallbacks: POINTER(win32more.Windows.Win32.Storage.FileSystem.LOG_MANAGEMENT_CALLBACKS_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def DeregisterManageableLogClient(hLog: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def ReadLogNotification(hLog: win32more.Windows.Win32.Foundation.HANDLE, pNotification: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLFS_MGMT_NOTIFICATION_head), lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def InstallLogPolicy(hLog: win32more.Windows.Win32.Foundation.HANDLE, pPolicy: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLFS_MGMT_POLICY_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def RemoveLogPolicy(hLog: win32more.Windows.Win32.Foundation.HANDLE, ePolicyType: win32more.Windows.Win32.Storage.FileSystem.CLFS_MGMT_POLICY_TYPE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def QueryLogPolicy(hLog: win32more.Windows.Win32.Foundation.HANDLE, ePolicyType: win32more.Windows.Win32.Storage.FileSystem.CLFS_MGMT_POLICY_TYPE, pPolicyBuffer: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLFS_MGMT_POLICY_head), pcbPolicyBuffer: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def SetLogFileSizeWithPolicy(hLog: win32more.Windows.Win32.Foundation.HANDLE, pDesiredSize: POINTER(UInt64), pResultingSize: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def HandleLogFull(hLog: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def LogTailAdvanceFailure(hLog: win32more.Windows.Win32.Foundation.HANDLE, dwReason: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def RegisterForLogWriteNotification(hLog: win32more.Windows.Win32.Foundation.HANDLE, cbThreshold: UInt32, fEnable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def QueryUsersOnEncryptedFile(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, pUsers: POINTER(POINTER(win32more.Windows.Win32.Storage.FileSystem.ENCRYPTION_CERTIFICATE_HASH_LIST_head))) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def QueryRecoveryAgentsOnEncryptedFile(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, pRecoveryAgents: POINTER(POINTER(win32more.Windows.Win32.Storage.FileSystem.ENCRYPTION_CERTIFICATE_HASH_LIST_head))) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def RemoveUsersFromEncryptedFile(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, pHashes: POINTER(win32more.Windows.Win32.Storage.FileSystem.ENCRYPTION_CERTIFICATE_HASH_LIST_head)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def AddUsersToEncryptedFile(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, pEncryptionCertificates: POINTER(win32more.Windows.Win32.Storage.FileSystem.ENCRYPTION_CERTIFICATE_LIST_head)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def SetUserFileEncryptionKey(pEncryptionCertificate: POINTER(win32more.Windows.Win32.Storage.FileSystem.ENCRYPTION_CERTIFICATE_head)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def SetUserFileEncryptionKeyEx(pEncryptionCertificate: POINTER(win32more.Windows.Win32.Storage.FileSystem.ENCRYPTION_CERTIFICATE_head), dwCapabilities: UInt32, dwFlags: UInt32, pvReserved: VoidPtr) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def FreeEncryptionCertificateHashList(pUsers: POINTER(win32more.Windows.Win32.Storage.FileSystem.ENCRYPTION_CERTIFICATE_HASH_LIST_head)) -> Void: ...
@winfunctype('ADVAPI32.dll')
def EncryptionDisable(DirPath: win32more.Windows.Win32.Foundation.PWSTR, Disable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def DuplicateEncryptionInfoFile(SrcFileName: win32more.Windows.Win32.Foundation.PWSTR, DstFileName: win32more.Windows.Win32.Foundation.PWSTR, dwCreationDistribution: UInt32, dwAttributes: UInt32, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES_head)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def GetEncryptedFileMetadata(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, pcbMetadata: POINTER(UInt32), ppbMetadata: POINTER(POINTER(Byte))) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def SetEncryptedFileMetadata(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, pbOldMetadata: POINTER(Byte), pbNewMetadata: POINTER(Byte), pOwnerHash: POINTER(win32more.Windows.Win32.Storage.FileSystem.ENCRYPTION_CERTIFICATE_HASH_head), dwOperation: UInt32, pCertificatesAdded: POINTER(win32more.Windows.Win32.Storage.FileSystem.ENCRYPTION_CERTIFICATE_HASH_LIST_head)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def FreeEncryptedFileMetadata(pbMetadata: POINTER(Byte)) -> Void: ...
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
def GetExpandedNameA(lpszSource: win32more.Windows.Win32.Foundation.PSTR, lpszBuffer: win32more.Windows.Win32.Foundation.PSTR) -> Int32: ...
@winfunctype('KERNEL32.dll')
def GetExpandedNameW(lpszSource: win32more.Windows.Win32.Foundation.PWSTR, lpszBuffer: win32more.Windows.Win32.Foundation.PWSTR) -> Int32: ...
@winfunctype('KERNEL32.dll')
def LZOpenFileA(lpFileName: win32more.Windows.Win32.Foundation.PSTR, lpReOpenBuf: POINTER(win32more.Windows.Win32.Storage.FileSystem.OFSTRUCT_head), wStyle: win32more.Windows.Win32.Storage.FileSystem.LZOPENFILE_STYLE) -> Int32: ...
@winfunctype('KERNEL32.dll')
def LZOpenFileW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, lpReOpenBuf: POINTER(win32more.Windows.Win32.Storage.FileSystem.OFSTRUCT_head), wStyle: win32more.Windows.Win32.Storage.FileSystem.LZOPENFILE_STYLE) -> Int32: ...
@winfunctype('KERNEL32.dll')
def LZSeek(hFile: Int32, lOffset: Int32, iOrigin: Int32) -> Int32: ...
@winfunctype('KERNEL32.dll')
def LZRead(hFile: Int32, lpBuffer: win32more.Windows.Win32.Foundation.PSTR, cbRead: Int32) -> Int32: ...
@winfunctype('KERNEL32.dll')
def LZClose(hFile: Int32) -> Void: ...
@winfunctype('WOFUTIL.dll')
def WofShouldCompressBinaries(Volume: win32more.Windows.Win32.Foundation.PWSTR, Algorithm: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WOFUTIL.dll')
def WofGetDriverVersion(FileOrVolumeHandle: win32more.Windows.Win32.Foundation.HANDLE, Provider: UInt32, WofVersion: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WOFUTIL.dll')
def WofSetFileDataLocation(FileHandle: win32more.Windows.Win32.Foundation.HANDLE, Provider: UInt32, ExternalFileInfo: VoidPtr, Length: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WOFUTIL.dll')
def WofIsExternalFile(FilePath: win32more.Windows.Win32.Foundation.PWSTR, IsExternalFile: POINTER(win32more.Windows.Win32.Foundation.BOOL), Provider: POINTER(UInt32), ExternalFileInfo: VoidPtr, BufferLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WOFUTIL.dll')
def WofEnumEntries(VolumeName: win32more.Windows.Win32.Foundation.PWSTR, Provider: UInt32, EnumProc: win32more.Windows.Win32.Storage.FileSystem.WofEnumEntryProc, UserData: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WOFUTIL.dll')
def WofWimAddEntry(VolumeName: win32more.Windows.Win32.Foundation.PWSTR, WimPath: win32more.Windows.Win32.Foundation.PWSTR, WimType: UInt32, WimIndex: UInt32, DataSourceId: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WOFUTIL.dll')
def WofWimEnumFiles(VolumeName: win32more.Windows.Win32.Foundation.PWSTR, DataSourceId: Int64, EnumProc: win32more.Windows.Win32.Storage.FileSystem.WofEnumFilesProc, UserData: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WOFUTIL.dll')
def WofWimSuspendEntry(VolumeName: win32more.Windows.Win32.Foundation.PWSTR, DataSourceId: Int64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WOFUTIL.dll')
def WofWimRemoveEntry(VolumeName: win32more.Windows.Win32.Foundation.PWSTR, DataSourceId: Int64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WOFUTIL.dll')
def WofWimUpdateEntry(VolumeName: win32more.Windows.Win32.Foundation.PWSTR, DataSourceId: Int64, NewWimPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WOFUTIL.dll')
def WofFileEnumFiles(VolumeName: win32more.Windows.Win32.Foundation.PWSTR, Algorithm: UInt32, EnumProc: win32more.Windows.Win32.Storage.FileSystem.WofEnumFilesProc, UserData: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('txfw32.dll')
def TxfLogCreateFileReadContext(LogPath: win32more.Windows.Win32.Foundation.PWSTR, BeginningLsn: win32more.Windows.Win32.Storage.FileSystem.CLS_LSN, EndingLsn: win32more.Windows.Win32.Storage.FileSystem.CLS_LSN, TxfFileId: POINTER(win32more.Windows.Win32.Storage.FileSystem.TXF_ID_head), TxfLogContext: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('txfw32.dll')
def TxfLogCreateRangeReadContext(LogPath: win32more.Windows.Win32.Foundation.PWSTR, BeginningLsn: win32more.Windows.Win32.Storage.FileSystem.CLS_LSN, EndingLsn: win32more.Windows.Win32.Storage.FileSystem.CLS_LSN, BeginningVirtualClock: POINTER(Int64), EndingVirtualClock: POINTER(Int64), RecordTypeMask: UInt32, TxfLogContext: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('txfw32.dll')
def TxfLogDestroyReadContext(TxfLogContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('txfw32.dll')
def TxfLogReadRecords(TxfLogContext: VoidPtr, BufferLength: UInt32, Buffer: VoidPtr, BytesUsed: POINTER(UInt32), RecordCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('txfw32.dll')
def TxfReadMetadataInfo(FileHandle: win32more.Windows.Win32.Foundation.HANDLE, TxfFileId: POINTER(win32more.Windows.Win32.Storage.FileSystem.TXF_ID_head), LastLsn: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN_head), TransactionState: POINTER(UInt32), LockingTransaction: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('txfw32.dll')
def TxfLogRecordGetFileName(RecordBuffer: VoidPtr, RecordBufferLengthInBytes: UInt32, NameBuffer: win32more.Windows.Win32.Foundation.PWSTR, NameBufferLengthInBytes: POINTER(UInt32), TxfId: POINTER(win32more.Windows.Win32.Storage.FileSystem.TXF_ID_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('txfw32.dll')
def TxfLogRecordGetGenericType(RecordBuffer: VoidPtr, RecordBufferLengthInBytes: UInt32, GenericType: POINTER(UInt32), VirtualClock: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('txfw32.dll')
def TxfSetThreadMiniVersionForCreate(MiniVersion: UInt16) -> Void: ...
@winfunctype('txfw32.dll')
def TxfGetThreadMiniVersionForCreate(MiniVersion: POINTER(UInt16)) -> Void: ...
@winfunctype('ktmw32.dll')
def CreateTransaction(lpTransactionAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES_head), UOW: POINTER(Guid), CreateOptions: UInt32, IsolationLevel: UInt32, IsolationFlags: UInt32, Timeout: UInt32, Description: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('ktmw32.dll')
def OpenTransaction(dwDesiredAccess: UInt32, TransactionId: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('ktmw32.dll')
def CommitTransaction(TransactionHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def CommitTransactionAsync(TransactionHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def RollbackTransaction(TransactionHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def RollbackTransactionAsync(TransactionHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def GetTransactionId(TransactionHandle: win32more.Windows.Win32.Foundation.HANDLE, TransactionId: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def GetTransactionInformation(TransactionHandle: win32more.Windows.Win32.Foundation.HANDLE, Outcome: POINTER(UInt32), IsolationLevel: POINTER(UInt32), IsolationFlags: POINTER(UInt32), Timeout: POINTER(UInt32), BufferLength: UInt32, Description: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def SetTransactionInformation(TransactionHandle: win32more.Windows.Win32.Foundation.HANDLE, IsolationLevel: UInt32, IsolationFlags: UInt32, Timeout: UInt32, Description: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def CreateTransactionManager(lpTransactionAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES_head), LogFileName: win32more.Windows.Win32.Foundation.PWSTR, CreateOptions: UInt32, CommitStrength: UInt32) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('ktmw32.dll')
def OpenTransactionManager(LogFileName: win32more.Windows.Win32.Foundation.PWSTR, DesiredAccess: UInt32, OpenOptions: UInt32) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('ktmw32.dll')
def OpenTransactionManagerById(TransactionManagerId: POINTER(Guid), DesiredAccess: UInt32, OpenOptions: UInt32) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('ktmw32.dll')
def RenameTransactionManager(LogFileName: win32more.Windows.Win32.Foundation.PWSTR, ExistingTransactionManagerGuid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def RollforwardTransactionManager(TransactionManagerHandle: win32more.Windows.Win32.Foundation.HANDLE, TmVirtualClock: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def RecoverTransactionManager(TransactionManagerHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def GetCurrentClockTransactionManager(TransactionManagerHandle: win32more.Windows.Win32.Foundation.HANDLE, TmVirtualClock: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def GetTransactionManagerId(TransactionManagerHandle: win32more.Windows.Win32.Foundation.HANDLE, TransactionManagerId: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def CreateResourceManager(lpResourceManagerAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES_head), ResourceManagerId: POINTER(Guid), CreateOptions: UInt32, TmHandle: win32more.Windows.Win32.Foundation.HANDLE, Description: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('ktmw32.dll')
def OpenResourceManager(dwDesiredAccess: UInt32, TmHandle: win32more.Windows.Win32.Foundation.HANDLE, ResourceManagerId: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('ktmw32.dll')
def RecoverResourceManager(ResourceManagerHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def GetNotificationResourceManager(ResourceManagerHandle: win32more.Windows.Win32.Foundation.HANDLE, TransactionNotification: POINTER(win32more.Windows.Win32.Storage.FileSystem.TRANSACTION_NOTIFICATION_head), NotificationLength: UInt32, dwMilliseconds: UInt32, ReturnLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def GetNotificationResourceManagerAsync(ResourceManagerHandle: win32more.Windows.Win32.Foundation.HANDLE, TransactionNotification: POINTER(win32more.Windows.Win32.Storage.FileSystem.TRANSACTION_NOTIFICATION_head), TransactionNotificationLength: UInt32, ReturnLength: POINTER(UInt32), lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def SetResourceManagerCompletionPort(ResourceManagerHandle: win32more.Windows.Win32.Foundation.HANDLE, IoCompletionPortHandle: win32more.Windows.Win32.Foundation.HANDLE, CompletionKey: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def CreateEnlistment(lpEnlistmentAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES_head), ResourceManagerHandle: win32more.Windows.Win32.Foundation.HANDLE, TransactionHandle: win32more.Windows.Win32.Foundation.HANDLE, NotificationMask: UInt32, CreateOptions: UInt32, EnlistmentKey: VoidPtr) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('ktmw32.dll')
def OpenEnlistment(dwDesiredAccess: UInt32, ResourceManagerHandle: win32more.Windows.Win32.Foundation.HANDLE, EnlistmentId: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('ktmw32.dll')
def RecoverEnlistment(EnlistmentHandle: win32more.Windows.Win32.Foundation.HANDLE, EnlistmentKey: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def GetEnlistmentRecoveryInformation(EnlistmentHandle: win32more.Windows.Win32.Foundation.HANDLE, BufferSize: UInt32, Buffer: VoidPtr, BufferUsed: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def GetEnlistmentId(EnlistmentHandle: win32more.Windows.Win32.Foundation.HANDLE, EnlistmentId: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def SetEnlistmentRecoveryInformation(EnlistmentHandle: win32more.Windows.Win32.Foundation.HANDLE, BufferSize: UInt32, Buffer: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def PrepareEnlistment(EnlistmentHandle: win32more.Windows.Win32.Foundation.HANDLE, TmVirtualClock: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def PrePrepareEnlistment(EnlistmentHandle: win32more.Windows.Win32.Foundation.HANDLE, TmVirtualClock: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def CommitEnlistment(EnlistmentHandle: win32more.Windows.Win32.Foundation.HANDLE, TmVirtualClock: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def RollbackEnlistment(EnlistmentHandle: win32more.Windows.Win32.Foundation.HANDLE, TmVirtualClock: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def PrePrepareComplete(EnlistmentHandle: win32more.Windows.Win32.Foundation.HANDLE, TmVirtualClock: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def PrepareComplete(EnlistmentHandle: win32more.Windows.Win32.Foundation.HANDLE, TmVirtualClock: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def ReadOnlyEnlistment(EnlistmentHandle: win32more.Windows.Win32.Foundation.HANDLE, TmVirtualClock: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def CommitComplete(EnlistmentHandle: win32more.Windows.Win32.Foundation.HANDLE, TmVirtualClock: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def RollbackComplete(EnlistmentHandle: win32more.Windows.Win32.Foundation.HANDLE, TmVirtualClock: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def SinglePhaseReject(EnlistmentHandle: win32more.Windows.Win32.Foundation.HANDLE, TmVirtualClock: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('NETAPI32.dll')
def NetShareAdd(servername: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, buf: POINTER(Byte), parm_err: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetShareEnum(servername: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, bufptr: POINTER(POINTER(Byte)), prefmaxlen: UInt32, entriesread: POINTER(UInt32), totalentries: POINTER(UInt32), resume_handle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetShareEnumSticky(servername: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, bufptr: POINTER(POINTER(Byte)), prefmaxlen: UInt32, entriesread: POINTER(UInt32), totalentries: POINTER(UInt32), resume_handle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetShareGetInfo(servername: win32more.Windows.Win32.Foundation.PWSTR, netname: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, bufptr: POINTER(POINTER(Byte))) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetShareSetInfo(servername: win32more.Windows.Win32.Foundation.PWSTR, netname: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, buf: POINTER(Byte), parm_err: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetShareDel(servername: win32more.Windows.Win32.Foundation.PWSTR, netname: win32more.Windows.Win32.Foundation.PWSTR, reserved: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetShareDelSticky(servername: win32more.Windows.Win32.Foundation.PWSTR, netname: win32more.Windows.Win32.Foundation.PWSTR, reserved: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetShareCheck(servername: win32more.Windows.Win32.Foundation.PWSTR, device: win32more.Windows.Win32.Foundation.PWSTR, type: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetShareDelEx(servername: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, buf: POINTER(Byte)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetServerAliasAdd(servername: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, buf: POINTER(Byte)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetServerAliasDel(servername: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, buf: POINTER(Byte)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetServerAliasEnum(servername: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, bufptr: POINTER(POINTER(Byte)), prefmaxlen: UInt32, entriesread: POINTER(UInt32), totalentries: POINTER(UInt32), resumehandle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetSessionEnum(servername: win32more.Windows.Win32.Foundation.PWSTR, UncClientName: win32more.Windows.Win32.Foundation.PWSTR, username: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, bufptr: POINTER(POINTER(Byte)), prefmaxlen: UInt32, entriesread: POINTER(UInt32), totalentries: POINTER(UInt32), resume_handle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetSessionDel(servername: win32more.Windows.Win32.Foundation.PWSTR, UncClientName: win32more.Windows.Win32.Foundation.PWSTR, username: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetSessionGetInfo(servername: win32more.Windows.Win32.Foundation.PWSTR, UncClientName: win32more.Windows.Win32.Foundation.PWSTR, username: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, bufptr: POINTER(POINTER(Byte))) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetConnectionEnum(servername: win32more.Windows.Win32.Foundation.PWSTR, qualifier: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, bufptr: POINTER(POINTER(Byte)), prefmaxlen: UInt32, entriesread: POINTER(UInt32), totalentries: POINTER(UInt32), resume_handle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetFileClose(servername: win32more.Windows.Win32.Foundation.PWSTR, fileid: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetFileEnum(servername: win32more.Windows.Win32.Foundation.PWSTR, basepath: win32more.Windows.Win32.Foundation.PWSTR, username: win32more.Windows.Win32.Foundation.PWSTR, level: UInt32, bufptr: POINTER(POINTER(Byte)), prefmaxlen: UInt32, entriesread: POINTER(UInt32), totalentries: POINTER(UInt32), resume_handle: POINTER(UIntPtr)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetFileGetInfo(servername: win32more.Windows.Win32.Foundation.PWSTR, fileid: UInt32, level: UInt32, bufptr: POINTER(POINTER(Byte))) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetStatisticsGet(ServerName: POINTER(SByte), Service: POINTER(SByte), Level: UInt32, Options: UInt32, Buffer: POINTER(POINTER(Byte))) -> UInt32: ...
@winfunctype('api-ms-win-core-ioring-l1-1-0.dll')
def QueryIoRingCapabilities(capabilities: POINTER(win32more.Windows.Win32.Storage.FileSystem.IORING_CAPABILITIES_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-ioring-l1-1-0.dll')
def IsIoRingOpSupported(ioRing: win32more.Windows.Win32.Storage.FileSystem.HIORING, op: win32more.Windows.Win32.Storage.FileSystem.IORING_OP_CODE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-ioring-l1-1-0.dll')
def CreateIoRing(ioringVersion: win32more.Windows.Win32.Storage.FileSystem.IORING_VERSION, flags: win32more.Windows.Win32.Storage.FileSystem.IORING_CREATE_FLAGS, submissionQueueSize: UInt32, completionQueueSize: UInt32, h: POINTER(win32more.Windows.Win32.Storage.FileSystem.HIORING)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-ioring-l1-1-0.dll')
def GetIoRingInfo(ioRing: win32more.Windows.Win32.Storage.FileSystem.HIORING, info: POINTER(win32more.Windows.Win32.Storage.FileSystem.IORING_INFO_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-ioring-l1-1-0.dll')
def SubmitIoRing(ioRing: win32more.Windows.Win32.Storage.FileSystem.HIORING, waitOperations: UInt32, milliseconds: UInt32, submittedEntries: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-ioring-l1-1-0.dll')
def CloseIoRing(ioRing: win32more.Windows.Win32.Storage.FileSystem.HIORING) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-ioring-l1-1-0.dll')
def PopIoRingCompletion(ioRing: win32more.Windows.Win32.Storage.FileSystem.HIORING, cqe: POINTER(win32more.Windows.Win32.Storage.FileSystem.IORING_CQE_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-ioring-l1-1-0.dll')
def SetIoRingCompletionEvent(ioRing: win32more.Windows.Win32.Storage.FileSystem.HIORING, hEvent: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-ioring-l1-1-0.dll')
def BuildIoRingCancelRequest(ioRing: win32more.Windows.Win32.Storage.FileSystem.HIORING, file: win32more.Windows.Win32.Storage.FileSystem.IORING_HANDLE_REF, opToCancel: UIntPtr, userData: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-ioring-l1-1-0.dll')
def BuildIoRingReadFile(ioRing: win32more.Windows.Win32.Storage.FileSystem.HIORING, fileRef: win32more.Windows.Win32.Storage.FileSystem.IORING_HANDLE_REF, dataRef: win32more.Windows.Win32.Storage.FileSystem.IORING_BUFFER_REF, numberOfBytesToRead: UInt32, fileOffset: UInt64, userData: UIntPtr, sqeFlags: win32more.Windows.Win32.Storage.FileSystem.IORING_SQE_FLAGS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-ioring-l1-1-0.dll')
def BuildIoRingRegisterFileHandles(ioRing: win32more.Windows.Win32.Storage.FileSystem.HIORING, count: UInt32, handles: POINTER(win32more.Windows.Win32.Foundation.HANDLE), userData: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-ioring-l1-1-0.dll')
def BuildIoRingRegisterBuffers(ioRing: win32more.Windows.Win32.Storage.FileSystem.HIORING, count: UInt32, buffers: POINTER(win32more.Windows.Win32.Storage.FileSystem.IORING_BUFFER_INFO_head), userData: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def BuildIoRingWriteFile(ioRing: win32more.Windows.Win32.Storage.FileSystem.HIORING, fileRef: win32more.Windows.Win32.Storage.FileSystem.IORING_HANDLE_REF, bufferRef: win32more.Windows.Win32.Storage.FileSystem.IORING_BUFFER_REF, numberOfBytesToWrite: UInt32, fileOffset: UInt64, writeFlags: win32more.Windows.Win32.Storage.FileSystem.FILE_WRITE_FLAGS, userData: UIntPtr, sqeFlags: win32more.Windows.Win32.Storage.FileSystem.IORING_SQE_FLAGS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def BuildIoRingFlushFile(ioRing: win32more.Windows.Win32.Storage.FileSystem.HIORING, fileRef: win32more.Windows.Win32.Storage.FileSystem.IORING_HANDLE_REF, flushMode: win32more.Windows.Win32.Storage.FileSystem.FILE_FLUSH_MODE, userData: UIntPtr, sqeFlags: win32more.Windows.Win32.Storage.FileSystem.IORING_SQE_FLAGS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def Wow64EnableWow64FsRedirection(Wow64FsEnableRedirection: win32more.Windows.Win32.Foundation.BOOLEAN) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('KERNEL32.dll')
def Wow64DisableWow64FsRedirection(OldValue: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def Wow64RevertWow64FsRedirection(OlValue: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetBinaryTypeA(lpApplicationName: win32more.Windows.Win32.Foundation.PSTR, lpBinaryType: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetBinaryTypeW(lpApplicationName: win32more.Windows.Win32.Foundation.PWSTR, lpBinaryType: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetShortPathNameA(lpszLongPath: win32more.Windows.Win32.Foundation.PSTR, lpszShortPath: win32more.Windows.Win32.Foundation.PSTR, cchBuffer: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetLongPathNameTransactedA(lpszShortPath: win32more.Windows.Win32.Foundation.PSTR, lpszLongPath: win32more.Windows.Win32.Foundation.PSTR, cchBuffer: UInt32, hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetLongPathNameTransactedW(lpszShortPath: win32more.Windows.Win32.Foundation.PWSTR, lpszLongPath: win32more.Windows.Win32.Foundation.PWSTR, cchBuffer: UInt32, hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def SetFileCompletionNotificationModes(FileHandle: win32more.Windows.Win32.Foundation.HANDLE, Flags: Byte) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetFileShortNameA(hFile: win32more.Windows.Win32.Foundation.HANDLE, lpShortName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetFileShortNameW(hFile: win32more.Windows.Win32.Foundation.HANDLE, lpShortName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetTapePosition(hDevice: win32more.Windows.Win32.Foundation.HANDLE, dwPositionMethod: win32more.Windows.Win32.Storage.FileSystem.TAPE_POSITION_METHOD, dwPartition: UInt32, dwOffsetLow: UInt32, dwOffsetHigh: UInt32, bImmediate: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetTapePosition(hDevice: win32more.Windows.Win32.Foundation.HANDLE, dwPositionType: win32more.Windows.Win32.Storage.FileSystem.TAPE_POSITION_TYPE, lpdwPartition: POINTER(UInt32), lpdwOffsetLow: POINTER(UInt32), lpdwOffsetHigh: POINTER(UInt32)) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def PrepareTape(hDevice: win32more.Windows.Win32.Foundation.HANDLE, dwOperation: win32more.Windows.Win32.Storage.FileSystem.PREPARE_TAPE_OPERATION, bImmediate: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def EraseTape(hDevice: win32more.Windows.Win32.Foundation.HANDLE, dwEraseType: win32more.Windows.Win32.Storage.FileSystem.ERASE_TAPE_TYPE, bImmediate: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def CreateTapePartition(hDevice: win32more.Windows.Win32.Foundation.HANDLE, dwPartitionMethod: win32more.Windows.Win32.Storage.FileSystem.CREATE_TAPE_PARTITION_METHOD, dwCount: UInt32, dwSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def WriteTapemark(hDevice: win32more.Windows.Win32.Foundation.HANDLE, dwTapemarkType: win32more.Windows.Win32.Storage.FileSystem.TAPEMARK_TYPE, dwTapemarkCount: UInt32, bImmediate: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetTapeStatus(hDevice: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetTapeParameters(hDevice: win32more.Windows.Win32.Foundation.HANDLE, dwOperation: win32more.Windows.Win32.Storage.FileSystem.GET_TAPE_DRIVE_PARAMETERS_OPERATION, lpdwSize: POINTER(UInt32), lpTapeInformation: VoidPtr) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def SetTapeParameters(hDevice: win32more.Windows.Win32.Foundation.HANDLE, dwOperation: win32more.Windows.Win32.Storage.FileSystem.TAPE_INFORMATION_TYPE, lpTapeInformation: VoidPtr) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def EncryptFileA(lpFileName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def EncryptFileW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def DecryptFileA(lpFileName: win32more.Windows.Win32.Foundation.PSTR, dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def DecryptFileW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def FileEncryptionStatusA(lpFileName: win32more.Windows.Win32.Foundation.PSTR, lpStatus: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def FileEncryptionStatusW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, lpStatus: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def OpenEncryptedFileRawA(lpFileName: win32more.Windows.Win32.Foundation.PSTR, ulFlags: UInt32, pvContext: POINTER(VoidPtr)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def OpenEncryptedFileRawW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, ulFlags: UInt32, pvContext: POINTER(VoidPtr)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def ReadEncryptedFileRaw(pfExportCallback: win32more.Windows.Win32.Storage.FileSystem.PFE_EXPORT_FUNC, pvCallbackContext: VoidPtr, pvContext: VoidPtr) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def WriteEncryptedFileRaw(pfImportCallback: win32more.Windows.Win32.Storage.FileSystem.PFE_IMPORT_FUNC, pvCallbackContext: VoidPtr, pvContext: VoidPtr) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def CloseEncryptedFileRaw(pvContext: VoidPtr) -> Void: ...
@winfunctype('KERNEL32.dll')
def OpenFile(lpFileName: win32more.Windows.Win32.Foundation.PSTR, lpReOpenBuff: POINTER(win32more.Windows.Win32.Storage.FileSystem.OFSTRUCT_head), uStyle: UInt32) -> Int32: ...
@winfunctype('KERNEL32.dll')
def BackupRead(hFile: win32more.Windows.Win32.Foundation.HANDLE, lpBuffer: POINTER(Byte), nNumberOfBytesToRead: UInt32, lpNumberOfBytesRead: POINTER(UInt32), bAbort: win32more.Windows.Win32.Foundation.BOOL, bProcessSecurity: win32more.Windows.Win32.Foundation.BOOL, lpContext: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def BackupSeek(hFile: win32more.Windows.Win32.Foundation.HANDLE, dwLowBytesToSeek: UInt32, dwHighBytesToSeek: UInt32, lpdwLowByteSeeked: POINTER(UInt32), lpdwHighByteSeeked: POINTER(UInt32), lpContext: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def BackupWrite(hFile: win32more.Windows.Win32.Foundation.HANDLE, lpBuffer: POINTER(Byte), nNumberOfBytesToWrite: UInt32, lpNumberOfBytesWritten: POINTER(UInt32), bAbort: win32more.Windows.Win32.Foundation.BOOL, bProcessSecurity: win32more.Windows.Win32.Foundation.BOOL, lpContext: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetLogicalDriveStringsA(nBufferLength: UInt32, lpBuffer: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def SetSearchPathMode(Flags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateDirectoryExA(lpTemplateDirectory: win32more.Windows.Win32.Foundation.PSTR, lpNewDirectory: win32more.Windows.Win32.Foundation.PSTR, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateDirectoryExW(lpTemplateDirectory: win32more.Windows.Win32.Foundation.PWSTR, lpNewDirectory: win32more.Windows.Win32.Foundation.PWSTR, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateDirectoryTransactedA(lpTemplateDirectory: win32more.Windows.Win32.Foundation.PSTR, lpNewDirectory: win32more.Windows.Win32.Foundation.PSTR, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES_head), hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateDirectoryTransactedW(lpTemplateDirectory: win32more.Windows.Win32.Foundation.PWSTR, lpNewDirectory: win32more.Windows.Win32.Foundation.PWSTR, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES_head), hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def RemoveDirectoryTransactedA(lpPathName: win32more.Windows.Win32.Foundation.PSTR, hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def RemoveDirectoryTransactedW(lpPathName: win32more.Windows.Win32.Foundation.PWSTR, hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetFullPathNameTransactedA(lpFileName: win32more.Windows.Win32.Foundation.PSTR, nBufferLength: UInt32, lpBuffer: win32more.Windows.Win32.Foundation.PSTR, lpFilePart: POINTER(win32more.Windows.Win32.Foundation.PSTR), hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetFullPathNameTransactedW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, nBufferLength: UInt32, lpBuffer: win32more.Windows.Win32.Foundation.PWSTR, lpFilePart: POINTER(win32more.Windows.Win32.Foundation.PWSTR), hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def DefineDosDeviceA(dwFlags: win32more.Windows.Win32.Storage.FileSystem.DEFINE_DOS_DEVICE_FLAGS, lpDeviceName: win32more.Windows.Win32.Foundation.PSTR, lpTargetPath: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def QueryDosDeviceA(lpDeviceName: win32more.Windows.Win32.Foundation.PSTR, lpTargetPath: win32more.Windows.Win32.Foundation.PSTR, ucchMax: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def CreateFileTransactedA(lpFileName: win32more.Windows.Win32.Foundation.PSTR, dwDesiredAccess: UInt32, dwShareMode: win32more.Windows.Win32.Storage.FileSystem.FILE_SHARE_MODE, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES_head), dwCreationDisposition: win32more.Windows.Win32.Storage.FileSystem.FILE_CREATION_DISPOSITION, dwFlagsAndAttributes: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES, hTemplateFile: win32more.Windows.Win32.Foundation.HANDLE, hTransaction: win32more.Windows.Win32.Foundation.HANDLE, pusMiniVersion: POINTER(win32more.Windows.Win32.Storage.FileSystem.TXFS_MINIVERSION), lpExtendedParameter: VoidPtr) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def CreateFileTransactedW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, dwDesiredAccess: UInt32, dwShareMode: win32more.Windows.Win32.Storage.FileSystem.FILE_SHARE_MODE, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES_head), dwCreationDisposition: win32more.Windows.Win32.Storage.FileSystem.FILE_CREATION_DISPOSITION, dwFlagsAndAttributes: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES, hTemplateFile: win32more.Windows.Win32.Foundation.HANDLE, hTransaction: win32more.Windows.Win32.Foundation.HANDLE, pusMiniVersion: POINTER(win32more.Windows.Win32.Storage.FileSystem.TXFS_MINIVERSION), lpExtendedParameter: VoidPtr) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def ReOpenFile(hOriginalFile: win32more.Windows.Win32.Foundation.HANDLE, dwDesiredAccess: UInt32, dwShareMode: win32more.Windows.Win32.Storage.FileSystem.FILE_SHARE_MODE, dwFlagsAndAttributes: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def SetFileAttributesTransactedA(lpFileName: win32more.Windows.Win32.Foundation.PSTR, dwFileAttributes: UInt32, hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetFileAttributesTransactedW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, dwFileAttributes: UInt32, hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetFileAttributesTransactedA(lpFileName: win32more.Windows.Win32.Foundation.PSTR, fInfoLevelId: win32more.Windows.Win32.Storage.FileSystem.GET_FILEEX_INFO_LEVELS, lpFileInformation: VoidPtr, hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetFileAttributesTransactedW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, fInfoLevelId: win32more.Windows.Win32.Storage.FileSystem.GET_FILEEX_INFO_LEVELS, lpFileInformation: VoidPtr, hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetCompressedFileSizeTransactedA(lpFileName: win32more.Windows.Win32.Foundation.PSTR, lpFileSizeHigh: POINTER(UInt32), hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetCompressedFileSizeTransactedW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, lpFileSizeHigh: POINTER(UInt32), hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def DeleteFileTransactedA(lpFileName: win32more.Windows.Win32.Foundation.PSTR, hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DeleteFileTransactedW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CheckNameLegalDOS8Dot3A(lpName: win32more.Windows.Win32.Foundation.PSTR, lpOemName: win32more.Windows.Win32.Foundation.PSTR, OemNameSize: UInt32, pbNameContainsSpaces: POINTER(win32more.Windows.Win32.Foundation.BOOL), pbNameLegal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CheckNameLegalDOS8Dot3W(lpName: win32more.Windows.Win32.Foundation.PWSTR, lpOemName: win32more.Windows.Win32.Foundation.PSTR, OemNameSize: UInt32, pbNameContainsSpaces: POINTER(win32more.Windows.Win32.Foundation.BOOL), pbNameLegal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FindFirstFileTransactedA(lpFileName: win32more.Windows.Win32.Foundation.PSTR, fInfoLevelId: win32more.Windows.Win32.Storage.FileSystem.FINDEX_INFO_LEVELS, lpFindFileData: VoidPtr, fSearchOp: win32more.Windows.Win32.Storage.FileSystem.FINDEX_SEARCH_OPS, lpSearchFilter: VoidPtr, dwAdditionalFlags: UInt32, hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def FindFirstFileTransactedW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, fInfoLevelId: win32more.Windows.Win32.Storage.FileSystem.FINDEX_INFO_LEVELS, lpFindFileData: VoidPtr, fSearchOp: win32more.Windows.Win32.Storage.FileSystem.FINDEX_SEARCH_OPS, lpSearchFilter: VoidPtr, dwAdditionalFlags: UInt32, hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def CopyFileA(lpExistingFileName: win32more.Windows.Win32.Foundation.PSTR, lpNewFileName: win32more.Windows.Win32.Foundation.PSTR, bFailIfExists: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CopyFileW(lpExistingFileName: win32more.Windows.Win32.Foundation.PWSTR, lpNewFileName: win32more.Windows.Win32.Foundation.PWSTR, bFailIfExists: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CopyFileExA(lpExistingFileName: win32more.Windows.Win32.Foundation.PSTR, lpNewFileName: win32more.Windows.Win32.Foundation.PSTR, lpProgressRoutine: win32more.Windows.Win32.Storage.FileSystem.LPPROGRESS_ROUTINE, lpData: VoidPtr, pbCancel: POINTER(win32more.Windows.Win32.Foundation.BOOL), dwCopyFlags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CopyFileExW(lpExistingFileName: win32more.Windows.Win32.Foundation.PWSTR, lpNewFileName: win32more.Windows.Win32.Foundation.PWSTR, lpProgressRoutine: win32more.Windows.Win32.Storage.FileSystem.LPPROGRESS_ROUTINE, lpData: VoidPtr, pbCancel: POINTER(win32more.Windows.Win32.Foundation.BOOL), dwCopyFlags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CopyFileTransactedA(lpExistingFileName: win32more.Windows.Win32.Foundation.PSTR, lpNewFileName: win32more.Windows.Win32.Foundation.PSTR, lpProgressRoutine: win32more.Windows.Win32.Storage.FileSystem.LPPROGRESS_ROUTINE, lpData: VoidPtr, pbCancel: POINTER(win32more.Windows.Win32.Foundation.BOOL), dwCopyFlags: UInt32, hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CopyFileTransactedW(lpExistingFileName: win32more.Windows.Win32.Foundation.PWSTR, lpNewFileName: win32more.Windows.Win32.Foundation.PWSTR, lpProgressRoutine: win32more.Windows.Win32.Storage.FileSystem.LPPROGRESS_ROUTINE, lpData: VoidPtr, pbCancel: POINTER(win32more.Windows.Win32.Foundation.BOOL), dwCopyFlags: UInt32, hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CopyFile2(pwszExistingFileName: win32more.Windows.Win32.Foundation.PWSTR, pwszNewFileName: win32more.Windows.Win32.Foundation.PWSTR, pExtendedParameters: POINTER(win32more.Windows.Win32.Storage.FileSystem.COPYFILE2_EXTENDED_PARAMETERS_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def MoveFileA(lpExistingFileName: win32more.Windows.Win32.Foundation.PSTR, lpNewFileName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def MoveFileW(lpExistingFileName: win32more.Windows.Win32.Foundation.PWSTR, lpNewFileName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def MoveFileExA(lpExistingFileName: win32more.Windows.Win32.Foundation.PSTR, lpNewFileName: win32more.Windows.Win32.Foundation.PSTR, dwFlags: win32more.Windows.Win32.Storage.FileSystem.MOVE_FILE_FLAGS) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def MoveFileExW(lpExistingFileName: win32more.Windows.Win32.Foundation.PWSTR, lpNewFileName: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: win32more.Windows.Win32.Storage.FileSystem.MOVE_FILE_FLAGS) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def MoveFileWithProgressA(lpExistingFileName: win32more.Windows.Win32.Foundation.PSTR, lpNewFileName: win32more.Windows.Win32.Foundation.PSTR, lpProgressRoutine: win32more.Windows.Win32.Storage.FileSystem.LPPROGRESS_ROUTINE, lpData: VoidPtr, dwFlags: win32more.Windows.Win32.Storage.FileSystem.MOVE_FILE_FLAGS) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def MoveFileWithProgressW(lpExistingFileName: win32more.Windows.Win32.Foundation.PWSTR, lpNewFileName: win32more.Windows.Win32.Foundation.PWSTR, lpProgressRoutine: win32more.Windows.Win32.Storage.FileSystem.LPPROGRESS_ROUTINE, lpData: VoidPtr, dwFlags: win32more.Windows.Win32.Storage.FileSystem.MOVE_FILE_FLAGS) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def MoveFileTransactedA(lpExistingFileName: win32more.Windows.Win32.Foundation.PSTR, lpNewFileName: win32more.Windows.Win32.Foundation.PSTR, lpProgressRoutine: win32more.Windows.Win32.Storage.FileSystem.LPPROGRESS_ROUTINE, lpData: VoidPtr, dwFlags: win32more.Windows.Win32.Storage.FileSystem.MOVE_FILE_FLAGS, hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def MoveFileTransactedW(lpExistingFileName: win32more.Windows.Win32.Foundation.PWSTR, lpNewFileName: win32more.Windows.Win32.Foundation.PWSTR, lpProgressRoutine: win32more.Windows.Win32.Storage.FileSystem.LPPROGRESS_ROUTINE, lpData: VoidPtr, dwFlags: win32more.Windows.Win32.Storage.FileSystem.MOVE_FILE_FLAGS, hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ReplaceFileA(lpReplacedFileName: win32more.Windows.Win32.Foundation.PSTR, lpReplacementFileName: win32more.Windows.Win32.Foundation.PSTR, lpBackupFileName: win32more.Windows.Win32.Foundation.PSTR, dwReplaceFlags: win32more.Windows.Win32.Storage.FileSystem.REPLACE_FILE_FLAGS, lpExclude: VoidPtr, lpReserved: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ReplaceFileW(lpReplacedFileName: win32more.Windows.Win32.Foundation.PWSTR, lpReplacementFileName: win32more.Windows.Win32.Foundation.PWSTR, lpBackupFileName: win32more.Windows.Win32.Foundation.PWSTR, dwReplaceFlags: win32more.Windows.Win32.Storage.FileSystem.REPLACE_FILE_FLAGS, lpExclude: VoidPtr, lpReserved: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateHardLinkA(lpFileName: win32more.Windows.Win32.Foundation.PSTR, lpExistingFileName: win32more.Windows.Win32.Foundation.PSTR, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateHardLinkW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, lpExistingFileName: win32more.Windows.Win32.Foundation.PWSTR, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateHardLinkTransactedA(lpFileName: win32more.Windows.Win32.Foundation.PSTR, lpExistingFileName: win32more.Windows.Win32.Foundation.PSTR, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES_head), hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateHardLinkTransactedW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, lpExistingFileName: win32more.Windows.Win32.Foundation.PWSTR, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES_head), hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FindFirstStreamTransactedW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, InfoLevel: win32more.Windows.Win32.Storage.FileSystem.STREAM_INFO_LEVELS, lpFindStreamData: VoidPtr, dwFlags: UInt32, hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def FindFirstFileNameTransactedW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, StringLength: POINTER(UInt32), LinkName: win32more.Windows.Win32.Foundation.PWSTR, hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def SetVolumeLabelA(lpRootPathName: win32more.Windows.Win32.Foundation.PSTR, lpVolumeName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetVolumeLabelW(lpRootPathName: win32more.Windows.Win32.Foundation.PWSTR, lpVolumeName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetFileBandwidthReservation(hFile: win32more.Windows.Win32.Foundation.HANDLE, nPeriodMilliseconds: UInt32, nBytesPerPeriod: UInt32, bDiscardable: win32more.Windows.Win32.Foundation.BOOL, lpTransferSize: POINTER(UInt32), lpNumOutstandingRequests: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetFileBandwidthReservation(hFile: win32more.Windows.Win32.Foundation.HANDLE, lpPeriodMilliseconds: POINTER(UInt32), lpBytesPerPeriod: POINTER(UInt32), pDiscardable: POINTER(win32more.Windows.Win32.Foundation.BOOL), lpTransferSize: POINTER(UInt32), lpNumOutstandingRequests: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ReadDirectoryChangesW(hDirectory: win32more.Windows.Win32.Foundation.HANDLE, lpBuffer: VoidPtr, nBufferLength: UInt32, bWatchSubtree: win32more.Windows.Win32.Foundation.BOOL, dwNotifyFilter: win32more.Windows.Win32.Storage.FileSystem.FILE_NOTIFY_CHANGE, lpBytesReturned: POINTER(UInt32), lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED_head), lpCompletionRoutine: win32more.Windows.Win32.System.IO.LPOVERLAPPED_COMPLETION_ROUTINE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ReadDirectoryChangesExW(hDirectory: win32more.Windows.Win32.Foundation.HANDLE, lpBuffer: VoidPtr, nBufferLength: UInt32, bWatchSubtree: win32more.Windows.Win32.Foundation.BOOL, dwNotifyFilter: win32more.Windows.Win32.Storage.FileSystem.FILE_NOTIFY_CHANGE, lpBytesReturned: POINTER(UInt32), lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED_head), lpCompletionRoutine: win32more.Windows.Win32.System.IO.LPOVERLAPPED_COMPLETION_ROUTINE, ReadDirectoryNotifyInformationClass: win32more.Windows.Win32.Storage.FileSystem.READ_DIRECTORY_NOTIFY_INFORMATION_CLASS) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FindFirstVolumeA(lpszVolumeName: win32more.Windows.Win32.Foundation.PSTR, cchBufferLength: UInt32) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def FindNextVolumeA(hFindVolume: win32more.Windows.Win32.Foundation.HANDLE, lpszVolumeName: win32more.Windows.Win32.Foundation.PSTR, cchBufferLength: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FindFirstVolumeMountPointA(lpszRootPathName: win32more.Windows.Win32.Foundation.PSTR, lpszVolumeMountPoint: win32more.Windows.Win32.Foundation.PSTR, cchBufferLength: UInt32) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def FindFirstVolumeMountPointW(lpszRootPathName: win32more.Windows.Win32.Foundation.PWSTR, lpszVolumeMountPoint: win32more.Windows.Win32.Foundation.PWSTR, cchBufferLength: UInt32) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def FindNextVolumeMountPointA(hFindVolumeMountPoint: win32more.Windows.Win32.Foundation.HANDLE, lpszVolumeMountPoint: win32more.Windows.Win32.Foundation.PSTR, cchBufferLength: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FindNextVolumeMountPointW(hFindVolumeMountPoint: win32more.Windows.Win32.Foundation.HANDLE, lpszVolumeMountPoint: win32more.Windows.Win32.Foundation.PWSTR, cchBufferLength: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FindVolumeMountPointClose(hFindVolumeMountPoint: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetVolumeMountPointA(lpszVolumeMountPoint: win32more.Windows.Win32.Foundation.PSTR, lpszVolumeName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetVolumeMountPointW(lpszVolumeMountPoint: win32more.Windows.Win32.Foundation.PWSTR, lpszVolumeName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DeleteVolumeMountPointA(lpszVolumeMountPoint: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetVolumeNameForVolumeMountPointA(lpszVolumeMountPoint: win32more.Windows.Win32.Foundation.PSTR, lpszVolumeName: win32more.Windows.Win32.Foundation.PSTR, cchBufferLength: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetVolumePathNameA(lpszFileName: win32more.Windows.Win32.Foundation.PSTR, lpszVolumePathName: win32more.Windows.Win32.Foundation.PSTR, cchBufferLength: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetVolumePathNamesForVolumeNameA(lpszVolumeName: win32more.Windows.Win32.Foundation.PSTR, lpszVolumePathNames: win32more.Windows.Win32.Foundation.PSTR, cchBufferLength: UInt32, lpcchReturnLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetFileInformationByHandleEx(hFile: win32more.Windows.Win32.Foundation.HANDLE, FileInformationClass: win32more.Windows.Win32.Storage.FileSystem.FILE_INFO_BY_HANDLE_CLASS, lpFileInformation: VoidPtr, dwBufferSize: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def OpenFileById(hVolumeHint: win32more.Windows.Win32.Foundation.HANDLE, lpFileId: POINTER(win32more.Windows.Win32.Storage.FileSystem.FILE_ID_DESCRIPTOR_head), dwDesiredAccess: UInt32, dwShareMode: win32more.Windows.Win32.Storage.FileSystem.FILE_SHARE_MODE, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES_head), dwFlagsAndAttributes: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def CreateSymbolicLinkA(lpSymlinkFileName: win32more.Windows.Win32.Foundation.PSTR, lpTargetFileName: win32more.Windows.Win32.Foundation.PSTR, dwFlags: win32more.Windows.Win32.Storage.FileSystem.SYMBOLIC_LINK_FLAGS) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('KERNEL32.dll')
def CreateSymbolicLinkW(lpSymlinkFileName: win32more.Windows.Win32.Foundation.PWSTR, lpTargetFileName: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: win32more.Windows.Win32.Storage.FileSystem.SYMBOLIC_LINK_FLAGS) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('KERNEL32.dll')
def CreateSymbolicLinkTransactedA(lpSymlinkFileName: win32more.Windows.Win32.Foundation.PSTR, lpTargetFileName: win32more.Windows.Win32.Foundation.PSTR, dwFlags: win32more.Windows.Win32.Storage.FileSystem.SYMBOLIC_LINK_FLAGS, hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('KERNEL32.dll')
def CreateSymbolicLinkTransactedW(lpSymlinkFileName: win32more.Windows.Win32.Foundation.PWSTR, lpTargetFileName: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: win32more.Windows.Win32.Storage.FileSystem.SYMBOLIC_LINK_FLAGS, hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
class BY_HANDLE_FILE_INFORMATION(EasyCastStructure):
    dwFileAttributes: UInt32
    ftCreationTime: win32more.Windows.Win32.Foundation.FILETIME
    ftLastAccessTime: win32more.Windows.Win32.Foundation.FILETIME
    ftLastWriteTime: win32more.Windows.Win32.Foundation.FILETIME
    dwVolumeSerialNumber: UInt32
    nFileSizeHigh: UInt32
    nFileSizeLow: UInt32
    nNumberOfLinks: UInt32
    nFileIndexHigh: UInt32
    nFileIndexLow: UInt32
@winfunctype_pointer
def CACHE_ACCESS_CHECK(pSecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, hClientToken: win32more.Windows.Win32.Foundation.HANDLE, dwDesiredAccess: UInt32, GenericMapping: POINTER(win32more.Windows.Win32.Security.GENERIC_MAPPING_head), PrivilegeSet: POINTER(win32more.Windows.Win32.Security.PRIVILEGE_SET_head), PrivilegeSetLength: POINTER(UInt32), GrantedAccess: POINTER(UInt32), AccessStatus: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def CACHE_DESTROY_CALLBACK(cb: UInt32, lpb: POINTER(Byte)) -> Void: ...
@winfunctype_pointer
def CACHE_KEY_COMPARE(cbKey1: UInt32, lpbKey1: POINTER(Byte), cbKey2: UInt32, lpbKey2: POINTER(Byte)) -> Int32: ...
@winfunctype_pointer
def CACHE_KEY_HASH(lpbKey: POINTER(Byte), cbKey: UInt32) -> UInt32: ...
@winfunctype_pointer
def CACHE_READ_CALLBACK(cb: UInt32, lpb: POINTER(Byte), lpvContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def CLAIMMEDIALABEL(pBuffer: POINTER(Byte), nBufferSize: UInt32, pLabelInfo: POINTER(win32more.Windows.Win32.Storage.FileSystem.MediaLabelInfo_head)) -> UInt32: ...
@winfunctype_pointer
def CLAIMMEDIALABELEX(pBuffer: POINTER(Byte), nBufferSize: UInt32, pLabelInfo: POINTER(win32more.Windows.Win32.Storage.FileSystem.MediaLabelInfo_head), LabelGuid: POINTER(Guid)) -> UInt32: ...
@winfunctype_pointer
def CLFS_BLOCK_ALLOCATION(cbBufferLength: UInt32, pvUserContext: VoidPtr) -> VoidPtr: ...
@winfunctype_pointer
def CLFS_BLOCK_DEALLOCATION(pvBuffer: VoidPtr, pvUserContext: VoidPtr) -> Void: ...
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
class CLFS_LOG_NAME_INFORMATION(EasyCastStructure):
    NameLengthInBytes: UInt16
    Name: Char * 1
class CLFS_MGMT_NOTIFICATION(EasyCastStructure):
    Notification: win32more.Windows.Win32.Storage.FileSystem.CLFS_MGMT_NOTIFICATION_TYPE
    Lsn: win32more.Windows.Win32.Storage.FileSystem.CLS_LSN
    LogIsPinned: UInt16
CLFS_MGMT_NOTIFICATION_TYPE = Int32
CLFS_MGMT_NOTIFICATION_TYPE_ClfsMgmtAdvanceTailNotification: CLFS_MGMT_NOTIFICATION_TYPE = 0
CLFS_MGMT_NOTIFICATION_TYPE_ClfsMgmtLogFullHandlerNotification: CLFS_MGMT_NOTIFICATION_TYPE = 1
CLFS_MGMT_NOTIFICATION_TYPE_ClfsMgmtLogUnpinnedNotification: CLFS_MGMT_NOTIFICATION_TYPE = 2
CLFS_MGMT_NOTIFICATION_TYPE_ClfsMgmtLogWriteNotification: CLFS_MGMT_NOTIFICATION_TYPE = 3
class CLFS_MGMT_POLICY(EasyCastStructure):
    Version: UInt32
    LengthInBytes: UInt32
    PolicyFlags: UInt32
    PolicyType: win32more.Windows.Win32.Storage.FileSystem.CLFS_MGMT_POLICY_TYPE
    PolicyParameters: _PolicyParameters_e__Union
    class _PolicyParameters_e__Union(EasyCastUnion):
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
        class _MaximumSize_e__Struct(EasyCastStructure):
            Containers: UInt32
        class _MinimumSize_e__Struct(EasyCastStructure):
            Containers: UInt32
        class _NewContainerSize_e__Struct(EasyCastStructure):
            SizeInBytes: UInt32
        class _GrowthRate_e__Struct(EasyCastStructure):
            AbsoluteGrowthInContainers: UInt32
            RelativeGrowthPercentage: UInt32
        class _LogTail_e__Struct(EasyCastStructure):
            MinimumAvailablePercentage: UInt32
            MinimumAvailableContainers: UInt32
        class _AutoShrink_e__Struct(EasyCastStructure):
            Percentage: UInt32
        class _AutoGrow_e__Struct(EasyCastStructure):
            Enabled: UInt32
        class _NewContainerPrefix_e__Struct(EasyCastStructure):
            PrefixLengthInBytes: UInt16
            PrefixString: Char * 1
        class _NewContainerSuffix_e__Struct(EasyCastStructure):
            NextContainerSuffix: UInt64
        class _NewContainerExtension_e__Struct(EasyCastStructure):
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
class CLFS_NODE_ID(EasyCastStructure):
    cType: UInt32
    cbNode: UInt32
class CLFS_PHYSICAL_LSN_INFORMATION(EasyCastStructure):
    StreamIdentifier: Byte
    VirtualLsn: win32more.Windows.Win32.Storage.FileSystem.CLS_LSN
    PhysicalLsn: win32more.Windows.Win32.Storage.FileSystem.CLS_LSN
class CLFS_STREAM_ID_INFORMATION(EasyCastStructure):
    StreamIdentifier: Byte
class CLS_ARCHIVE_DESCRIPTOR(EasyCastStructure):
    coffLow: UInt64
    coffHigh: UInt64
    infoContainer: win32more.Windows.Win32.Storage.FileSystem.CLS_CONTAINER_INFORMATION
class CLS_CONTAINER_INFORMATION(EasyCastStructure):
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
class CLS_INFORMATION(EasyCastStructure):
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
    MinArchiveTailLsn: win32more.Windows.Win32.Storage.FileSystem.CLS_LSN
    BaseLsn: win32more.Windows.Win32.Storage.FileSystem.CLS_LSN
    LastFlushedLsn: win32more.Windows.Win32.Storage.FileSystem.CLS_LSN
    LastLsn: win32more.Windows.Win32.Storage.FileSystem.CLS_LSN
    RestartLsn: win32more.Windows.Win32.Storage.FileSystem.CLS_LSN
    Identity: Guid
CLS_IOSTATS_CLASS = Int32
CLS_IOSTATS_CLASS_ClsIoStatsDefault: CLS_IOSTATS_CLASS = 0
CLS_IOSTATS_CLASS_ClsIoStatsMax: CLS_IOSTATS_CLASS = 65535
class CLS_IO_STATISTICS(EasyCastStructure):
    hdrIoStats: win32more.Windows.Win32.Storage.FileSystem.CLS_IO_STATISTICS_HEADER
    cFlush: UInt64
    cbFlush: UInt64
    cMetaFlush: UInt64
    cbMetaFlush: UInt64
class CLS_IO_STATISTICS_HEADER(EasyCastStructure):
    ubMajorVersion: Byte
    ubMinorVersion: Byte
    eStatsClass: win32more.Windows.Win32.Storage.FileSystem.CLFS_IOSTATS_CLASS
    cbLength: UInt16
    coffData: UInt32
CLS_LOG_INFORMATION_CLASS = Int32
CLS_LOG_INFORMATION_CLASS_ClfsLogBasicInformation: CLS_LOG_INFORMATION_CLASS = 0
CLS_LOG_INFORMATION_CLASS_ClfsLogBasicInformationPhysical: CLS_LOG_INFORMATION_CLASS = 1
CLS_LOG_INFORMATION_CLASS_ClfsLogPhysicalNameInformation: CLS_LOG_INFORMATION_CLASS = 2
CLS_LOG_INFORMATION_CLASS_ClfsLogStreamIdentifierInformation: CLS_LOG_INFORMATION_CLASS = 3
CLS_LOG_INFORMATION_CLASS_ClfsLogSystemMarkingInformation: CLS_LOG_INFORMATION_CLASS = 4
CLS_LOG_INFORMATION_CLASS_ClfsLogPhysicalLsnInformation: CLS_LOG_INFORMATION_CLASS = 5
class CLS_LSN(EasyCastStructure):
    Internal: UInt64
class CLS_SCAN_CONTEXT(EasyCastStructure):
    cidNode: win32more.Windows.Win32.Storage.FileSystem.CLFS_NODE_ID
    hLog: win32more.Windows.Win32.Foundation.HANDLE
    cIndex: UInt32
    cContainers: UInt32
    cContainersReturned: UInt32
    eScanMode: Byte
    pinfoContainer: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_CONTAINER_INFORMATION_head)
class CLS_WRITE_ENTRY(EasyCastStructure):
    Buffer: VoidPtr
    ByteLength: UInt32
COMPRESSION_FORMAT = UInt16
COMPRESSION_FORMAT_NONE: COMPRESSION_FORMAT = 0
COMPRESSION_FORMAT_DEFAULT: COMPRESSION_FORMAT = 1
COMPRESSION_FORMAT_LZNT1: COMPRESSION_FORMAT = 2
COMPRESSION_FORMAT_XPRESS: COMPRESSION_FORMAT = 3
COMPRESSION_FORMAT_XPRESS_HUFF: COMPRESSION_FORMAT = 4
COMPRESSION_FORMAT_XP10: COMPRESSION_FORMAT = 5
class CONNECTION_INFO_0(EasyCastStructure):
    coni0_id: UInt32
class CONNECTION_INFO_1(EasyCastStructure):
    coni1_id: UInt32
    coni1_type: win32more.Windows.Win32.Storage.FileSystem.SHARE_TYPE
    coni1_num_opens: UInt32
    coni1_num_users: UInt32
    coni1_time: UInt32
    coni1_username: win32more.Windows.Win32.Foundation.PWSTR
    coni1_netname: win32more.Windows.Win32.Foundation.PWSTR
COPYFILE2_COPY_PHASE = Int32
COPYFILE2_PHASE_NONE: COPYFILE2_COPY_PHASE = 0
COPYFILE2_PHASE_PREPARE_SOURCE: COPYFILE2_COPY_PHASE = 1
COPYFILE2_PHASE_PREPARE_DEST: COPYFILE2_COPY_PHASE = 2
COPYFILE2_PHASE_READ_SOURCE: COPYFILE2_COPY_PHASE = 3
COPYFILE2_PHASE_WRITE_DESTINATION: COPYFILE2_COPY_PHASE = 4
COPYFILE2_PHASE_SERVER_COPY: COPYFILE2_COPY_PHASE = 5
COPYFILE2_PHASE_NAMEGRAFT_COPY: COPYFILE2_COPY_PHASE = 6
COPYFILE2_PHASE_MAX: COPYFILE2_COPY_PHASE = 7
class COPYFILE2_EXTENDED_PARAMETERS(EasyCastStructure):
    dwSize: UInt32
    dwCopyFlags: UInt32
    pfCancel: POINTER(win32more.Windows.Win32.Foundation.BOOL)
    pProgressRoutine: win32more.Windows.Win32.Storage.FileSystem.PCOPYFILE2_PROGRESS_ROUTINE
    pvCallbackContext: VoidPtr
class COPYFILE2_EXTENDED_PARAMETERS_V2(EasyCastStructure):
    dwSize: UInt32
    dwCopyFlags: UInt32
    pfCancel: POINTER(win32more.Windows.Win32.Foundation.BOOL)
    pProgressRoutine: win32more.Windows.Win32.Storage.FileSystem.PCOPYFILE2_PROGRESS_ROUTINE
    pvCallbackContext: VoidPtr
    dwCopyFlagsV2: UInt32
    ioDesiredSize: UInt32
    ioDesiredRate: UInt32
    reserved: VoidPtr * 8
class COPYFILE2_MESSAGE(EasyCastStructure):
    Type: win32more.Windows.Win32.Storage.FileSystem.COPYFILE2_MESSAGE_TYPE
    dwPadding: UInt32
    Info: _Info_e__Union
    class _Info_e__Union(EasyCastUnion):
        ChunkStarted: _ChunkStarted_e__Struct
        ChunkFinished: _ChunkFinished_e__Struct
        StreamStarted: _StreamStarted_e__Struct
        StreamFinished: _StreamFinished_e__Struct
        PollContinue: _PollContinue_e__Struct
        Error: _Error_e__Struct
        class _ChunkStarted_e__Struct(EasyCastStructure):
            dwStreamNumber: UInt32
            dwReserved: UInt32
            hSourceFile: win32more.Windows.Win32.Foundation.HANDLE
            hDestinationFile: win32more.Windows.Win32.Foundation.HANDLE
            uliChunkNumber: UInt64
            uliChunkSize: UInt64
            uliStreamSize: UInt64
            uliTotalFileSize: UInt64
        class _ChunkFinished_e__Struct(EasyCastStructure):
            dwStreamNumber: UInt32
            dwFlags: UInt32
            hSourceFile: win32more.Windows.Win32.Foundation.HANDLE
            hDestinationFile: win32more.Windows.Win32.Foundation.HANDLE
            uliChunkNumber: UInt64
            uliChunkSize: UInt64
            uliStreamSize: UInt64
            uliStreamBytesTransferred: UInt64
            uliTotalFileSize: UInt64
            uliTotalBytesTransferred: UInt64
        class _StreamStarted_e__Struct(EasyCastStructure):
            dwStreamNumber: UInt32
            dwReserved: UInt32
            hSourceFile: win32more.Windows.Win32.Foundation.HANDLE
            hDestinationFile: win32more.Windows.Win32.Foundation.HANDLE
            uliStreamSize: UInt64
            uliTotalFileSize: UInt64
        class _StreamFinished_e__Struct(EasyCastStructure):
            dwStreamNumber: UInt32
            dwReserved: UInt32
            hSourceFile: win32more.Windows.Win32.Foundation.HANDLE
            hDestinationFile: win32more.Windows.Win32.Foundation.HANDLE
            uliStreamSize: UInt64
            uliStreamBytesTransferred: UInt64
            uliTotalFileSize: UInt64
            uliTotalBytesTransferred: UInt64
        class _PollContinue_e__Struct(EasyCastStructure):
            dwReserved: UInt32
        class _Error_e__Struct(EasyCastStructure):
            CopyPhase: win32more.Windows.Win32.Storage.FileSystem.COPYFILE2_COPY_PHASE
            dwStreamNumber: UInt32
            hrFailure: win32more.Windows.Win32.Foundation.HRESULT
            dwReserved: UInt32
            uliChunkNumber: UInt64
            uliStreamSize: UInt64
            uliStreamBytesTransferred: UInt64
            uliTotalFileSize: UInt64
            uliTotalBytesTransferred: UInt64
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
class CREATEFILE2_EXTENDED_PARAMETERS(EasyCastStructure):
    dwSize: UInt32
    dwFileAttributes: UInt32
    dwFileFlags: UInt32
    dwSecurityQosFlags: UInt32
    lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES_head)
    hTemplateFile: win32more.Windows.Win32.Foundation.HANDLE
CREATE_TAPE_PARTITION_METHOD = UInt32
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
class DISKQUOTA_USER_INFORMATION(EasyCastStructure):
    QuotaUsed: Int64
    QuotaThreshold: Int64
    QuotaLimit: Int64
class DISK_SPACE_INFORMATION(EasyCastStructure):
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
class EFS_CERTIFICATE_BLOB(EasyCastStructure):
    dwCertEncodingType: UInt32
    cbData: UInt32
    pbData: POINTER(Byte)
class EFS_COMPATIBILITY_INFO(EasyCastStructure):
    EfsVersion: UInt32
class EFS_DECRYPTION_STATUS_INFO(EasyCastStructure):
    dwDecryptionError: UInt32
    dwHashOffset: UInt32
    cbHash: UInt32
class EFS_ENCRYPTION_STATUS_INFO(EasyCastStructure):
    bHasCurrentKey: win32more.Windows.Win32.Foundation.BOOL
    dwEncryptionError: UInt32
class EFS_HASH_BLOB(EasyCastStructure):
    cbData: UInt32
    pbData: POINTER(Byte)
class EFS_KEY_INFO(EasyCastStructure):
    dwVersion: UInt32
    Entropy: UInt32
    Algorithm: win32more.Windows.Win32.Security.Cryptography.ALG_ID
    KeyLength: UInt32
class EFS_PIN_BLOB(EasyCastStructure):
    cbPadding: UInt32
    cbData: UInt32
    pbData: POINTER(Byte)
class EFS_RPC_BLOB(EasyCastStructure):
    cbData: UInt32
    pbData: POINTER(Byte)
class EFS_VERSION_INFO(EasyCastStructure):
    EfsVersion: UInt32
    SubVersion: UInt32
class ENCRYPTED_FILE_METADATA_SIGNATURE(EasyCastStructure):
    dwEfsAccessType: UInt32
    pCertificatesAdded: POINTER(win32more.Windows.Win32.Storage.FileSystem.ENCRYPTION_CERTIFICATE_HASH_LIST_head)
    pEncryptionCertificate: POINTER(win32more.Windows.Win32.Storage.FileSystem.ENCRYPTION_CERTIFICATE_head)
    pEfsStreamSignature: POINTER(win32more.Windows.Win32.Storage.FileSystem.EFS_RPC_BLOB_head)
class ENCRYPTION_CERTIFICATE(EasyCastStructure):
    cbTotalLength: UInt32
    pUserSid: POINTER(win32more.Windows.Win32.Security.SID_head)
    pCertBlob: POINTER(win32more.Windows.Win32.Storage.FileSystem.EFS_CERTIFICATE_BLOB_head)
class ENCRYPTION_CERTIFICATE_HASH(EasyCastStructure):
    cbTotalLength: UInt32
    pUserSid: POINTER(win32more.Windows.Win32.Security.SID_head)
    pHash: POINTER(win32more.Windows.Win32.Storage.FileSystem.EFS_HASH_BLOB_head)
    lpDisplayInformation: win32more.Windows.Win32.Foundation.PWSTR
class ENCRYPTION_CERTIFICATE_HASH_LIST(EasyCastStructure):
    nCert_Hash: UInt32
    pUsers: POINTER(POINTER(win32more.Windows.Win32.Storage.FileSystem.ENCRYPTION_CERTIFICATE_HASH_head))
class ENCRYPTION_CERTIFICATE_LIST(EasyCastStructure):
    nUsers: UInt32
    pUsers: POINTER(POINTER(win32more.Windows.Win32.Storage.FileSystem.ENCRYPTION_CERTIFICATE_head))
class ENCRYPTION_PROTECTOR(EasyCastStructure):
    cbTotalLength: UInt32
    pUserSid: POINTER(win32more.Windows.Win32.Security.SID_head)
    lpProtectorDescriptor: win32more.Windows.Win32.Foundation.PWSTR
class ENCRYPTION_PROTECTOR_LIST(EasyCastStructure):
    nProtectors: UInt32
    pProtectors: POINTER(POINTER(win32more.Windows.Win32.Storage.FileSystem.ENCRYPTION_PROTECTOR_head))
ERASE_TAPE_TYPE = UInt32
TAPE_ERASE_LONG: ERASE_TAPE_TYPE = 1
TAPE_ERASE_SHORT: ERASE_TAPE_TYPE = 0
@winfunctype_pointer
def FCACHE_CREATE_CALLBACK(lpstrName: win32more.Windows.Win32.Foundation.PSTR, lpvData: VoidPtr, cbFileSize: POINTER(UInt32), cbFileSizeHigh: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype_pointer
def FCACHE_RICHCREATE_CALLBACK(lpstrName: win32more.Windows.Win32.Foundation.PSTR, lpvData: VoidPtr, cbFileSize: POINTER(UInt32), cbFileSizeHigh: POINTER(UInt32), pfDidWeScanIt: POINTER(win32more.Windows.Win32.Foundation.BOOL), pfIsStuffed: POINTER(win32more.Windows.Win32.Foundation.BOOL), pfStoredWithDots: POINTER(win32more.Windows.Win32.Foundation.BOOL), pfStoredWithTerminatingDot: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HANDLE: ...
class FH_OVERLAPPED(EasyCastStructure):
    Internal: UIntPtr
    InternalHigh: UIntPtr
    Offset: UInt32
    OffsetHigh: UInt32
    hEvent: win32more.Windows.Win32.Foundation.HANDLE
    pfnCompletion: win32more.Windows.Win32.Storage.FileSystem.PFN_IO_COMPLETION
    Reserved1: UIntPtr
    Reserved2: UIntPtr
    Reserved3: UIntPtr
    Reserved4: UIntPtr
FILE_ACCESS_RIGHTS = UInt32
FILE_READ_DATA: FILE_ACCESS_RIGHTS = 1
FILE_LIST_DIRECTORY: FILE_ACCESS_RIGHTS = 1
FILE_WRITE_DATA: FILE_ACCESS_RIGHTS = 2
FILE_ADD_FILE: FILE_ACCESS_RIGHTS = 2
FILE_APPEND_DATA: FILE_ACCESS_RIGHTS = 4
FILE_ADD_SUBDIRECTORY: FILE_ACCESS_RIGHTS = 4
FILE_CREATE_PIPE_INSTANCE: FILE_ACCESS_RIGHTS = 4
FILE_READ_EA: FILE_ACCESS_RIGHTS = 8
FILE_WRITE_EA: FILE_ACCESS_RIGHTS = 16
FILE_EXECUTE: FILE_ACCESS_RIGHTS = 32
FILE_TRAVERSE: FILE_ACCESS_RIGHTS = 32
FILE_DELETE_CHILD: FILE_ACCESS_RIGHTS = 64
FILE_READ_ATTRIBUTES: FILE_ACCESS_RIGHTS = 128
FILE_WRITE_ATTRIBUTES: FILE_ACCESS_RIGHTS = 256
DELETE: FILE_ACCESS_RIGHTS = 65536
READ_CONTROL: FILE_ACCESS_RIGHTS = 131072
WRITE_DAC: FILE_ACCESS_RIGHTS = 262144
WRITE_OWNER: FILE_ACCESS_RIGHTS = 524288
SYNCHRONIZE: FILE_ACCESS_RIGHTS = 1048576
STANDARD_RIGHTS_REQUIRED: FILE_ACCESS_RIGHTS = 983040
STANDARD_RIGHTS_READ: FILE_ACCESS_RIGHTS = 131072
STANDARD_RIGHTS_WRITE: FILE_ACCESS_RIGHTS = 131072
STANDARD_RIGHTS_EXECUTE: FILE_ACCESS_RIGHTS = 131072
STANDARD_RIGHTS_ALL: FILE_ACCESS_RIGHTS = 2031616
SPECIFIC_RIGHTS_ALL: FILE_ACCESS_RIGHTS = 65535
FILE_ALL_ACCESS: FILE_ACCESS_RIGHTS = 2032127
FILE_GENERIC_READ: FILE_ACCESS_RIGHTS = 1179785
FILE_GENERIC_WRITE: FILE_ACCESS_RIGHTS = 1179926
FILE_GENERIC_EXECUTE: FILE_ACCESS_RIGHTS = 1179808
FILE_ACTION = UInt32
FILE_ACTION_ADDED: FILE_ACTION = 1
FILE_ACTION_REMOVED: FILE_ACTION = 2
FILE_ACTION_MODIFIED: FILE_ACTION = 3
FILE_ACTION_RENAMED_OLD_NAME: FILE_ACTION = 4
FILE_ACTION_RENAMED_NEW_NAME: FILE_ACTION = 5
class FILE_ALIGNMENT_INFO(EasyCastStructure):
    AlignmentRequirement: UInt32
class FILE_ALLOCATION_INFO(EasyCastStructure):
    AllocationSize: Int64
class FILE_ATTRIBUTE_TAG_INFO(EasyCastStructure):
    FileAttributes: UInt32
    ReparseTag: UInt32
class FILE_BASIC_INFO(EasyCastStructure):
    CreationTime: Int64
    LastAccessTime: Int64
    LastWriteTime: Int64
    ChangeTime: Int64
    FileAttributes: UInt32
class FILE_COMPRESSION_INFO(EasyCastStructure):
    CompressedFileSize: Int64
    CompressionFormat: win32more.Windows.Win32.Storage.FileSystem.COMPRESSION_FORMAT
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
class FILE_DISPOSITION_INFO(EasyCastStructure):
    DeleteFile: win32more.Windows.Win32.Foundation.BOOLEAN
class FILE_DISPOSITION_INFO_EX(EasyCastStructure):
    Flags: win32more.Windows.Win32.Storage.FileSystem.FILE_DISPOSITION_INFO_EX_FLAGS
FILE_DISPOSITION_INFO_EX_FLAGS = UInt32
FILE_DISPOSITION_FLAG_DO_NOT_DELETE: FILE_DISPOSITION_INFO_EX_FLAGS = 0
FILE_DISPOSITION_FLAG_DELETE: FILE_DISPOSITION_INFO_EX_FLAGS = 1
FILE_DISPOSITION_FLAG_POSIX_SEMANTICS: FILE_DISPOSITION_INFO_EX_FLAGS = 2
FILE_DISPOSITION_FLAG_FORCE_IMAGE_SECTION_CHECK: FILE_DISPOSITION_INFO_EX_FLAGS = 4
FILE_DISPOSITION_FLAG_ON_CLOSE: FILE_DISPOSITION_INFO_EX_FLAGS = 8
FILE_DISPOSITION_FLAG_IGNORE_READONLY_ATTRIBUTE: FILE_DISPOSITION_INFO_EX_FLAGS = 16
class FILE_END_OF_FILE_INFO(EasyCastStructure):
    EndOfFile: Int64
class FILE_EXTENT(EasyCastStructure):
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
FILE_FLUSH_MODE = Int32
FILE_FLUSH_DEFAULT: FILE_FLUSH_MODE = 0
FILE_FLUSH_DATA: FILE_FLUSH_MODE = 1
FILE_FLUSH_MIN_METADATA: FILE_FLUSH_MODE = 2
FILE_FLUSH_NO_SYNC: FILE_FLUSH_MODE = 3
class FILE_FULL_DIR_INFO(EasyCastStructure):
    NextEntryOffset: UInt32
    FileIndex: UInt32
    CreationTime: Int64
    LastAccessTime: Int64
    LastWriteTime: Int64
    ChangeTime: Int64
    EndOfFile: Int64
    AllocationSize: Int64
    FileAttributes: UInt32
    FileNameLength: UInt32
    EaSize: UInt32
    FileName: Char * 1
class FILE_ID_128(EasyCastStructure):
    Identifier: Byte * 16
class FILE_ID_BOTH_DIR_INFO(EasyCastStructure):
    NextEntryOffset: UInt32
    FileIndex: UInt32
    CreationTime: Int64
    LastAccessTime: Int64
    LastWriteTime: Int64
    ChangeTime: Int64
    EndOfFile: Int64
    AllocationSize: Int64
    FileAttributes: UInt32
    FileNameLength: UInt32
    EaSize: UInt32
    ShortNameLength: SByte
    ShortName: Char * 12
    FileId: Int64
    FileName: Char * 1
class FILE_ID_DESCRIPTOR(EasyCastStructure):
    dwSize: UInt32
    Type: win32more.Windows.Win32.Storage.FileSystem.FILE_ID_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        FileId: Int64
        ObjectId: Guid
        ExtendedFileId: win32more.Windows.Win32.Storage.FileSystem.FILE_ID_128
class FILE_ID_EXTD_DIR_INFO(EasyCastStructure):
    NextEntryOffset: UInt32
    FileIndex: UInt32
    CreationTime: Int64
    LastAccessTime: Int64
    LastWriteTime: Int64
    ChangeTime: Int64
    EndOfFile: Int64
    AllocationSize: Int64
    FileAttributes: UInt32
    FileNameLength: UInt32
    EaSize: UInt32
    ReparsePointTag: UInt32
    FileId: win32more.Windows.Win32.Storage.FileSystem.FILE_ID_128
    FileName: Char * 1
class FILE_ID_INFO(EasyCastStructure):
    VolumeSerialNumber: UInt64
    FileId: win32more.Windows.Win32.Storage.FileSystem.FILE_ID_128
FILE_ID_TYPE = Int32
FILE_ID_TYPE_FileIdType: FILE_ID_TYPE = 0
FILE_ID_TYPE_ObjectIdType: FILE_ID_TYPE = 1
FILE_ID_TYPE_ExtendedFileIdType: FILE_ID_TYPE = 2
FILE_ID_TYPE_MaximumFileIdType: FILE_ID_TYPE = 3
class FILE_INFO_2(EasyCastStructure):
    fi2_id: UInt32
class FILE_INFO_3(EasyCastStructure):
    fi3_id: UInt32
    fi3_permissions: win32more.Windows.Win32.Storage.FileSystem.FILE_INFO_FLAGS_PERMISSIONS
    fi3_num_locks: UInt32
    fi3_pathname: win32more.Windows.Win32.Foundation.PWSTR
    fi3_username: win32more.Windows.Win32.Foundation.PWSTR
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
class FILE_IO_PRIORITY_HINT_INFO(EasyCastStructure):
    PriorityHint: win32more.Windows.Win32.Storage.FileSystem.PRIORITY_HINT
class FILE_NAME_INFO(EasyCastStructure):
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
class FILE_NOTIFY_EXTENDED_INFORMATION(EasyCastStructure):
    NextEntryOffset: UInt32
    Action: win32more.Windows.Win32.Storage.FileSystem.FILE_ACTION
    CreationTime: Int64
    LastModificationTime: Int64
    LastChangeTime: Int64
    LastAccessTime: Int64
    AllocatedLength: Int64
    FileSize: Int64
    FileAttributes: UInt32
    Anonymous: _Anonymous_e__Union
    FileId: Int64
    ParentFileId: Int64
    FileNameLength: UInt32
    FileName: Char * 1
    class _Anonymous_e__Union(EasyCastUnion):
        ReparsePointTag: UInt32
        EaSize: UInt32
class FILE_NOTIFY_INFORMATION(EasyCastStructure):
    NextEntryOffset: UInt32
    Action: win32more.Windows.Win32.Storage.FileSystem.FILE_ACTION
    FileNameLength: UInt32
    FileName: Char * 1
class FILE_REMOTE_PROTOCOL_INFO(EasyCastStructure):
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
    class _GenericReserved_e__Struct(EasyCastStructure):
        Reserved: UInt32 * 8
    class _ProtocolSpecific_e__Union(EasyCastUnion):
        Smb2: _Smb2_e__Struct
        Reserved: UInt32 * 16
        class _Smb2_e__Struct(EasyCastStructure):
            Server: _Server_e__Struct
            Share: _Share_e__Struct
            class _Server_e__Struct(EasyCastStructure):
                Capabilities: UInt32
            class _Share_e__Struct(EasyCastStructure):
                Capabilities: UInt32
                ShareFlags: UInt32
class FILE_RENAME_INFO(EasyCastStructure):
    Anonymous: _Anonymous_e__Union
    RootDirectory: win32more.Windows.Win32.Foundation.HANDLE
    FileNameLength: UInt32
    FileName: Char * 1
    class _Anonymous_e__Union(EasyCastUnion):
        ReplaceIfExists: win32more.Windows.Win32.Foundation.BOOLEAN
        Flags: UInt32
class FILE_SEGMENT_ELEMENT(EasyCastUnion):
    Buffer: VoidPtr
    Alignment: UInt64
FILE_SHARE_MODE = UInt32
FILE_SHARE_NONE: FILE_SHARE_MODE = 0
FILE_SHARE_DELETE: FILE_SHARE_MODE = 4
FILE_SHARE_READ: FILE_SHARE_MODE = 1
FILE_SHARE_WRITE: FILE_SHARE_MODE = 2
class FILE_STANDARD_INFO(EasyCastStructure):
    AllocationSize: Int64
    EndOfFile: Int64
    NumberOfLinks: UInt32
    DeletePending: win32more.Windows.Win32.Foundation.BOOLEAN
    Directory: win32more.Windows.Win32.Foundation.BOOLEAN
class FILE_STORAGE_INFO(EasyCastStructure):
    LogicalBytesPerSector: UInt32
    PhysicalBytesPerSectorForAtomicity: UInt32
    PhysicalBytesPerSectorForPerformance: UInt32
    FileSystemEffectivePhysicalBytesPerSectorForAtomicity: UInt32
    Flags: UInt32
    ByteOffsetForSectorAlignment: UInt32
    ByteOffsetForPartitionAlignment: UInt32
class FILE_STREAM_INFO(EasyCastStructure):
    NextEntryOffset: UInt32
    StreamNameLength: UInt32
    StreamSize: Int64
    StreamAllocationSize: Int64
    StreamName: Char * 1
FILE_TYPE = UInt32
FILE_TYPE_UNKNOWN: FILE_TYPE = 0
FILE_TYPE_DISK: FILE_TYPE = 1
FILE_TYPE_CHAR: FILE_TYPE = 2
FILE_TYPE_PIPE: FILE_TYPE = 3
FILE_TYPE_REMOTE: FILE_TYPE = 32768
FILE_WRITE_FLAGS = Int32
FILE_WRITE_FLAGS_NONE: FILE_WRITE_FLAGS = 0
FILE_WRITE_FLAGS_WRITE_THROUGH: FILE_WRITE_FLAGS = 1
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
class FIO_CONTEXT(EasyCastStructure):
    m_dwTempHack: UInt32
    m_dwSignature: UInt32
    m_hFile: win32more.Windows.Win32.Foundation.HANDLE
    m_dwLinesOffset: UInt32
    m_dwHeaderLength: UInt32
GETFINALPATHNAMEBYHANDLE_FLAGS = UInt32
VOLUME_NAME_DOS: GETFINALPATHNAMEBYHANDLE_FLAGS = 0
VOLUME_NAME_GUID: GETFINALPATHNAMEBYHANDLE_FLAGS = 1
VOLUME_NAME_NT: GETFINALPATHNAMEBYHANDLE_FLAGS = 2
VOLUME_NAME_NONE: GETFINALPATHNAMEBYHANDLE_FLAGS = 4
FILE_NAME_NORMALIZED: GETFINALPATHNAMEBYHANDLE_FLAGS = 0
FILE_NAME_OPENED: GETFINALPATHNAMEBYHANDLE_FLAGS = 8
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
HIORING = IntPtr
class IDiskQuotaControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IConnectionPointContainer
    _iid_ = Guid('{7988b572-ec89-11cf-9c00-00aa00a14f56}')
    @commethod(5)
    def Initialize(self, pszPath: win32more.Windows.Win32.Foundation.PWSTR, bReadWrite: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetQuotaState(self, dwState: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetQuotaState(self, pdwState: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetQuotaLogFlags(self, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetQuotaLogFlags(self, pdwFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetDefaultQuotaThreshold(self, llThreshold: Int64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetDefaultQuotaThreshold(self, pllThreshold: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetDefaultQuotaThresholdText(self, pszText: win32more.Windows.Win32.Foundation.PWSTR, cchText: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetDefaultQuotaLimit(self, llLimit: Int64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetDefaultQuotaLimit(self, pllLimit: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetDefaultQuotaLimitText(self, pszText: win32more.Windows.Win32.Foundation.PWSTR, cchText: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def AddUserSid(self, pUserSid: win32more.Windows.Win32.Foundation.PSID, fNameResolution: win32more.Windows.Win32.Storage.FileSystem.DISKQUOTA_USERNAME_RESOLVE, ppUser: POINTER(win32more.Windows.Win32.Storage.FileSystem.IDiskQuotaUser_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def AddUserName(self, pszLogonName: win32more.Windows.Win32.Foundation.PWSTR, fNameResolution: win32more.Windows.Win32.Storage.FileSystem.DISKQUOTA_USERNAME_RESOLVE, ppUser: POINTER(win32more.Windows.Win32.Storage.FileSystem.IDiskQuotaUser_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def DeleteUser(self, pUser: win32more.Windows.Win32.Storage.FileSystem.IDiskQuotaUser_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def FindUserSid(self, pUserSid: win32more.Windows.Win32.Foundation.PSID, fNameResolution: win32more.Windows.Win32.Storage.FileSystem.DISKQUOTA_USERNAME_RESOLVE, ppUser: POINTER(win32more.Windows.Win32.Storage.FileSystem.IDiskQuotaUser_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def FindUserName(self, pszLogonName: win32more.Windows.Win32.Foundation.PWSTR, ppUser: POINTER(win32more.Windows.Win32.Storage.FileSystem.IDiskQuotaUser_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def CreateEnumUsers(self, rgpUserSids: POINTER(win32more.Windows.Win32.Foundation.PSID), cpSids: UInt32, fNameResolution: win32more.Windows.Win32.Storage.FileSystem.DISKQUOTA_USERNAME_RESOLVE, ppEnum: POINTER(win32more.Windows.Win32.Storage.FileSystem.IEnumDiskQuotaUsers_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def CreateUserBatch(self, ppBatch: POINTER(win32more.Windows.Win32.Storage.FileSystem.IDiskQuotaUserBatch_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def InvalidateSidNameCache(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GiveUserNameResolutionPriority(self, pUser: win32more.Windows.Win32.Storage.FileSystem.IDiskQuotaUser_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def ShutdownNameResolution(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDiskQuotaEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7988b579-ec89-11cf-9c00-00aa00a14f56}')
    @commethod(3)
    def OnUserNameChanged(self, pUser: win32more.Windows.Win32.Storage.FileSystem.IDiskQuotaUser_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDiskQuotaUser(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7988b574-ec89-11cf-9c00-00aa00a14f56}')
    @commethod(3)
    def GetID(self, pulID: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetName(self, pszAccountContainer: win32more.Windows.Win32.Foundation.PWSTR, cchAccountContainer: UInt32, pszLogonName: win32more.Windows.Win32.Foundation.PWSTR, cchLogonName: UInt32, pszDisplayName: win32more.Windows.Win32.Foundation.PWSTR, cchDisplayName: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSidLength(self, pdwLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSid(self, pbSidBuffer: POINTER(Byte), cbSidBuffer: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetQuotaThreshold(self, pllThreshold: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetQuotaThresholdText(self, pszText: win32more.Windows.Win32.Foundation.PWSTR, cchText: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetQuotaLimit(self, pllLimit: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetQuotaLimitText(self, pszText: win32more.Windows.Win32.Foundation.PWSTR, cchText: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetQuotaUsed(self, pllUsed: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetQuotaUsedText(self, pszText: win32more.Windows.Win32.Foundation.PWSTR, cchText: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetQuotaInformation(self, pbQuotaInfo: VoidPtr, cbQuotaInfo: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetQuotaThreshold(self, llThreshold: Int64, fWriteThrough: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetQuotaLimit(self, llLimit: Int64, fWriteThrough: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Invalidate(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetAccountStatus(self, pdwStatus: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDiskQuotaUserBatch(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7988b576-ec89-11cf-9c00-00aa00a14f56}')
    @commethod(3)
    def Add(self, pUser: win32more.Windows.Win32.Storage.FileSystem.IDiskQuotaUser_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Remove(self, pUser: win32more.Windows.Win32.Storage.FileSystem.IDiskQuotaUser_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RemoveAll(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def FlushToDisk(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumDiskQuotaUsers(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7988b577-ec89-11cf-9c00-00aa00a14f56}')
    @commethod(3)
    def Next(self, cUsers: UInt32, rgUsers: POINTER(win32more.Windows.Win32.Storage.FileSystem.IDiskQuotaUser_head), pcUsersFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, cUsers: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.Storage.FileSystem.IEnumDiskQuotaUsers_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IORING_BUFFER_INFO(EasyCastStructure):
    Address: VoidPtr
    Length: UInt32
class IORING_BUFFER_REF(EasyCastStructure):
    Kind: win32more.Windows.Win32.Storage.FileSystem.IORING_REF_KIND
    Buffer: BufferUnion
    class BufferUnion(EasyCastUnion):
        Address: VoidPtr
        IndexAndOffset: win32more.Windows.Win32.Storage.FileSystem.IORING_REGISTERED_BUFFER
class IORING_CAPABILITIES(EasyCastStructure):
    MaxVersion: win32more.Windows.Win32.Storage.FileSystem.IORING_VERSION
    MaxSubmissionQueueSize: UInt32
    MaxCompletionQueueSize: UInt32
    FeatureFlags: win32more.Windows.Win32.Storage.FileSystem.IORING_FEATURE_FLAGS
class IORING_CQE(EasyCastStructure):
    UserData: UIntPtr
    ResultCode: win32more.Windows.Win32.Foundation.HRESULT
    Information: UIntPtr
IORING_CREATE_ADVISORY_FLAGS = Int32
IORING_CREATE_ADVISORY_FLAGS_NONE: IORING_CREATE_ADVISORY_FLAGS = 0
class IORING_CREATE_FLAGS(EasyCastStructure):
    Required: win32more.Windows.Win32.Storage.FileSystem.IORING_CREATE_REQUIRED_FLAGS
    Advisory: win32more.Windows.Win32.Storage.FileSystem.IORING_CREATE_ADVISORY_FLAGS
IORING_CREATE_REQUIRED_FLAGS = Int32
IORING_CREATE_REQUIRED_FLAGS_NONE: IORING_CREATE_REQUIRED_FLAGS = 0
IORING_FEATURE_FLAGS = Int32
IORING_FEATURE_FLAGS_NONE: IORING_FEATURE_FLAGS = 0
IORING_FEATURE_UM_EMULATION: IORING_FEATURE_FLAGS = 1
IORING_FEATURE_SET_COMPLETION_EVENT: IORING_FEATURE_FLAGS = 2
class IORING_HANDLE_REF(EasyCastStructure):
    Kind: win32more.Windows.Win32.Storage.FileSystem.IORING_REF_KIND
    Handle: HandleUnion
    class HandleUnion(EasyCastUnion):
        Handle: win32more.Windows.Win32.Foundation.HANDLE
        Index: UInt32
class IORING_INFO(EasyCastStructure):
    IoRingVersion: win32more.Windows.Win32.Storage.FileSystem.IORING_VERSION
    Flags: win32more.Windows.Win32.Storage.FileSystem.IORING_CREATE_FLAGS
    SubmissionQueueSize: UInt32
    CompletionQueueSize: UInt32
IORING_OP_CODE = Int32
IORING_OP_NOP: IORING_OP_CODE = 0
IORING_OP_READ: IORING_OP_CODE = 1
IORING_OP_REGISTER_FILES: IORING_OP_CODE = 2
IORING_OP_REGISTER_BUFFERS: IORING_OP_CODE = 3
IORING_OP_CANCEL: IORING_OP_CODE = 4
IORING_OP_WRITE: IORING_OP_CODE = 5
IORING_OP_FLUSH: IORING_OP_CODE = 6
IORING_REF_KIND = Int32
IORING_REF_RAW: IORING_REF_KIND = 0
IORING_REF_REGISTERED: IORING_REF_KIND = 1
class IORING_REGISTERED_BUFFER(EasyCastStructure):
    BufferIndex: UInt32
    Offset: UInt32
IORING_SQE_FLAGS = Int32
IOSQE_FLAGS_NONE: IORING_SQE_FLAGS = 0
IOSQE_FLAGS_DRAIN_PRECEDING_OPS: IORING_SQE_FLAGS = 1
IORING_VERSION = Int32
IORING_VERSION_INVALID: IORING_VERSION = 0
IORING_VERSION_1: IORING_VERSION = 1
IORING_VERSION_2: IORING_VERSION = 2
IORING_VERSION_3: IORING_VERSION = 300
class KCRM_MARSHAL_HEADER(EasyCastStructure):
    VersionMajor: UInt32
    VersionMinor: UInt32
    NumProtocols: UInt32
    Unused: UInt32
class KCRM_PROTOCOL_BLOB(EasyCastStructure):
    ProtocolId: Guid
    StaticInfoLength: UInt32
    TransactionIdInfoLength: UInt32
    Unused1: UInt32
    Unused2: UInt32
class KCRM_TRANSACTION_BLOB(EasyCastStructure):
    UOW: Guid
    TmIdentity: Guid
    IsolationLevel: UInt32
    IsolationFlags: UInt32
    Timeout: UInt32
    Description: Char * 64
LOCK_FILE_FLAGS = UInt32
LOCKFILE_EXCLUSIVE_LOCK: LOCK_FILE_FLAGS = 2
LOCKFILE_FAIL_IMMEDIATELY: LOCK_FILE_FLAGS = 1
class LOG_MANAGEMENT_CALLBACKS(EasyCastStructure):
    CallbackContext: VoidPtr
    AdvanceTailCallback: win32more.Windows.Win32.Storage.FileSystem.PLOG_TAIL_ADVANCE_CALLBACK
    LogFullHandlerCallback: win32more.Windows.Win32.Storage.FileSystem.PLOG_FULL_HANDLER_CALLBACK
    LogUnpinnedCallback: win32more.Windows.Win32.Storage.FileSystem.PLOG_UNPINNED_CALLBACK
@winfunctype_pointer
def LPPROGRESS_ROUTINE(TotalFileSize: Int64, TotalBytesTransferred: Int64, StreamSize: Int64, StreamBytesTransferred: Int64, dwStreamNumber: UInt32, dwCallbackReason: win32more.Windows.Win32.Storage.FileSystem.LPPROGRESS_ROUTINE_CALLBACK_REASON, hSourceFile: win32more.Windows.Win32.Foundation.HANDLE, hDestinationFile: win32more.Windows.Win32.Foundation.HANDLE, lpData: VoidPtr) -> UInt32: ...
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
class MediaLabelInfo(EasyCastStructure):
    LabelType: Char * 64
    LabelIDSize: UInt32
    LabelID: Byte * 256
    LabelAppDescr: Char * 256
class NAME_CACHE_CONTEXT(EasyCastStructure):
    m_dwSignature: UInt32
class NTMS_ALLOCATION_INFORMATION(EasyCastStructure):
    dwSize: UInt32
    lpReserved: VoidPtr
    AllocatedFrom: Guid
class NTMS_ASYNC_IO(EasyCastStructure):
    OperationId: Guid
    EventId: Guid
    dwOperationType: UInt32
    dwResult: UInt32
    dwAsyncState: UInt32
    hEvent: win32more.Windows.Win32.Foundation.HANDLE
    bOnStateChange: win32more.Windows.Win32.Foundation.BOOL
class NTMS_CHANGERINFORMATIONA(EasyCastStructure):
    Number: UInt32
    ChangerType: Guid
    szSerialNumber: win32more.Windows.Win32.Foundation.CHAR * 32
    szRevision: win32more.Windows.Win32.Foundation.CHAR * 32
    szDeviceName: win32more.Windows.Win32.Foundation.CHAR * 64
    ScsiPort: UInt16
    ScsiBus: UInt16
    ScsiTarget: UInt16
    ScsiLun: UInt16
    Library: Guid
class NTMS_CHANGERINFORMATIONW(EasyCastStructure):
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
class NTMS_CHANGERTYPEINFORMATIONA(EasyCastStructure):
    szVendor: win32more.Windows.Win32.Foundation.CHAR * 128
    szProduct: win32more.Windows.Win32.Foundation.CHAR * 128
    DeviceType: UInt32
class NTMS_CHANGERTYPEINFORMATIONW(EasyCastStructure):
    szVendor: Char * 128
    szProduct: Char * 128
    DeviceType: UInt32
class NTMS_COMPUTERINFORMATION(EasyCastStructure):
    dwLibRequestPurgeTime: UInt32
    dwOpRequestPurgeTime: UInt32
    dwLibRequestFlags: UInt32
    dwOpRequestFlags: UInt32
    dwMediaPoolPolicy: UInt32
class NTMS_DRIVEINFORMATIONA(EasyCastStructure):
    Number: UInt32
    State: UInt32
    DriveType: Guid
    szDeviceName: win32more.Windows.Win32.Foundation.CHAR * 64
    szSerialNumber: win32more.Windows.Win32.Foundation.CHAR * 32
    szRevision: win32more.Windows.Win32.Foundation.CHAR * 32
    ScsiPort: UInt16
    ScsiBus: UInt16
    ScsiTarget: UInt16
    ScsiLun: UInt16
    dwMountCount: UInt32
    LastCleanedTs: win32more.Windows.Win32.Foundation.SYSTEMTIME
    SavedPartitionId: Guid
    Library: Guid
    Reserved: Guid
    dwDeferDismountDelay: UInt32
class NTMS_DRIVEINFORMATIONW(EasyCastStructure):
    Number: UInt32
    State: UInt32
    DriveType: Guid
    szDeviceName: Char * 64
    szSerialNumber: Char * 32
    szRevision: Char * 32
    ScsiPort: UInt16
    ScsiBus: UInt16
    ScsiTarget: UInt16
    ScsiLun: UInt16
    dwMountCount: UInt32
    LastCleanedTs: win32more.Windows.Win32.Foundation.SYSTEMTIME
    SavedPartitionId: Guid
    Library: Guid
    Reserved: Guid
    dwDeferDismountDelay: UInt32
class NTMS_DRIVETYPEINFORMATIONA(EasyCastStructure):
    szVendor: win32more.Windows.Win32.Foundation.CHAR * 128
    szProduct: win32more.Windows.Win32.Foundation.CHAR * 128
    NumberOfHeads: UInt32
    DeviceType: win32more.Windows.Win32.Storage.FileSystem.FILE_DEVICE_TYPE
class NTMS_DRIVETYPEINFORMATIONW(EasyCastStructure):
    szVendor: Char * 128
    szProduct: Char * 128
    NumberOfHeads: UInt32
    DeviceType: win32more.Windows.Win32.Storage.FileSystem.FILE_DEVICE_TYPE
class NTMS_FILESYSTEM_INFO(EasyCastStructure):
    FileSystemType: Char * 64
    VolumeName: Char * 256
    SerialNumber: UInt32
class NTMS_I1_LIBRARYINFORMATION(EasyCastStructure):
    LibraryType: UInt32
    CleanerSlot: Guid
    CleanerSlotDefault: Guid
    LibrarySupportsDriveCleaning: win32more.Windows.Win32.Foundation.BOOL
    BarCodeReaderInstalled: win32more.Windows.Win32.Foundation.BOOL
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
class NTMS_I1_LIBREQUESTINFORMATIONA(EasyCastStructure):
    OperationCode: UInt32
    OperationOption: UInt32
    State: UInt32
    PartitionId: Guid
    DriveId: Guid
    PhysMediaId: Guid
    Library: Guid
    SlotId: Guid
    TimeQueued: win32more.Windows.Win32.Foundation.SYSTEMTIME
    TimeCompleted: win32more.Windows.Win32.Foundation.SYSTEMTIME
    szApplication: win32more.Windows.Win32.Foundation.CHAR * 64
    szUser: win32more.Windows.Win32.Foundation.CHAR * 64
    szComputer: win32more.Windows.Win32.Foundation.CHAR * 64
class NTMS_I1_LIBREQUESTINFORMATIONW(EasyCastStructure):
    OperationCode: UInt32
    OperationOption: UInt32
    State: UInt32
    PartitionId: Guid
    DriveId: Guid
    PhysMediaId: Guid
    Library: Guid
    SlotId: Guid
    TimeQueued: win32more.Windows.Win32.Foundation.SYSTEMTIME
    TimeCompleted: win32more.Windows.Win32.Foundation.SYSTEMTIME
    szApplication: Char * 64
    szUser: Char * 64
    szComputer: Char * 64
class NTMS_I1_OBJECTINFORMATIONA(EasyCastStructure):
    dwSize: UInt32
    dwType: UInt32
    Created: win32more.Windows.Win32.Foundation.SYSTEMTIME
    Modified: win32more.Windows.Win32.Foundation.SYSTEMTIME
    ObjectGuid: Guid
    Enabled: win32more.Windows.Win32.Foundation.BOOL
    dwOperationalState: UInt32
    szName: win32more.Windows.Win32.Foundation.CHAR * 64
    szDescription: win32more.Windows.Win32.Foundation.CHAR * 127
    Info: _Info_e__Union
    class _Info_e__Union(EasyCastUnion):
        Drive: win32more.Windows.Win32.Storage.FileSystem.NTMS_DRIVEINFORMATIONA
        DriveType: win32more.Windows.Win32.Storage.FileSystem.NTMS_DRIVETYPEINFORMATIONA
        Library: win32more.Windows.Win32.Storage.FileSystem.NTMS_I1_LIBRARYINFORMATION
        Changer: win32more.Windows.Win32.Storage.FileSystem.NTMS_CHANGERINFORMATIONA
        ChangerType: win32more.Windows.Win32.Storage.FileSystem.NTMS_CHANGERTYPEINFORMATIONA
        StorageSlot: win32more.Windows.Win32.Storage.FileSystem.NTMS_STORAGESLOTINFORMATION
        IEDoor: win32more.Windows.Win32.Storage.FileSystem.NTMS_IEDOORINFORMATION
        IEPort: win32more.Windows.Win32.Storage.FileSystem.NTMS_IEPORTINFORMATION
        PhysicalMedia: win32more.Windows.Win32.Storage.FileSystem.NTMS_I1_PMIDINFORMATIONA
        LogicalMedia: win32more.Windows.Win32.Storage.FileSystem.NTMS_LMIDINFORMATION
        Partition: win32more.Windows.Win32.Storage.FileSystem.NTMS_I1_PARTITIONINFORMATIONA
        MediaPool: win32more.Windows.Win32.Storage.FileSystem.NTMS_MEDIAPOOLINFORMATION
        MediaType: win32more.Windows.Win32.Storage.FileSystem.NTMS_MEDIATYPEINFORMATION
        LibRequest: win32more.Windows.Win32.Storage.FileSystem.NTMS_I1_LIBREQUESTINFORMATIONA
        OpRequest: win32more.Windows.Win32.Storage.FileSystem.NTMS_I1_OPREQUESTINFORMATIONA
class NTMS_I1_OBJECTINFORMATIONW(EasyCastStructure):
    dwSize: UInt32
    dwType: UInt32
    Created: win32more.Windows.Win32.Foundation.SYSTEMTIME
    Modified: win32more.Windows.Win32.Foundation.SYSTEMTIME
    ObjectGuid: Guid
    Enabled: win32more.Windows.Win32.Foundation.BOOL
    dwOperationalState: UInt32
    szName: Char * 64
    szDescription: Char * 127
    Info: _Info_e__Union
    class _Info_e__Union(EasyCastUnion):
        Drive: win32more.Windows.Win32.Storage.FileSystem.NTMS_DRIVEINFORMATIONW
        DriveType: win32more.Windows.Win32.Storage.FileSystem.NTMS_DRIVETYPEINFORMATIONW
        Library: win32more.Windows.Win32.Storage.FileSystem.NTMS_I1_LIBRARYINFORMATION
        Changer: win32more.Windows.Win32.Storage.FileSystem.NTMS_CHANGERINFORMATIONW
        ChangerType: win32more.Windows.Win32.Storage.FileSystem.NTMS_CHANGERTYPEINFORMATIONW
        StorageSlot: win32more.Windows.Win32.Storage.FileSystem.NTMS_STORAGESLOTINFORMATION
        IEDoor: win32more.Windows.Win32.Storage.FileSystem.NTMS_IEDOORINFORMATION
        IEPort: win32more.Windows.Win32.Storage.FileSystem.NTMS_IEPORTINFORMATION
        PhysicalMedia: win32more.Windows.Win32.Storage.FileSystem.NTMS_I1_PMIDINFORMATIONW
        LogicalMedia: win32more.Windows.Win32.Storage.FileSystem.NTMS_LMIDINFORMATION
        Partition: win32more.Windows.Win32.Storage.FileSystem.NTMS_I1_PARTITIONINFORMATIONW
        MediaPool: win32more.Windows.Win32.Storage.FileSystem.NTMS_MEDIAPOOLINFORMATION
        MediaType: win32more.Windows.Win32.Storage.FileSystem.NTMS_MEDIATYPEINFORMATION
        LibRequest: win32more.Windows.Win32.Storage.FileSystem.NTMS_I1_LIBREQUESTINFORMATIONW
        OpRequest: win32more.Windows.Win32.Storage.FileSystem.NTMS_I1_OPREQUESTINFORMATIONW
class NTMS_I1_OPREQUESTINFORMATIONA(EasyCastStructure):
    Request: UInt32
    Submitted: win32more.Windows.Win32.Foundation.SYSTEMTIME
    State: UInt32
    szMessage: win32more.Windows.Win32.Foundation.CHAR * 127
    Arg1Type: UInt32
    Arg1: Guid
    Arg2Type: UInt32
    Arg2: Guid
    szApplication: win32more.Windows.Win32.Foundation.CHAR * 64
    szUser: win32more.Windows.Win32.Foundation.CHAR * 64
    szComputer: win32more.Windows.Win32.Foundation.CHAR * 64
class NTMS_I1_OPREQUESTINFORMATIONW(EasyCastStructure):
    Request: UInt32
    Submitted: win32more.Windows.Win32.Foundation.SYSTEMTIME
    State: UInt32
    szMessage: Char * 127
    Arg1Type: UInt32
    Arg1: Guid
    Arg2Type: UInt32
    Arg2: Guid
    szApplication: Char * 64
    szUser: Char * 64
    szComputer: Char * 64
class NTMS_I1_PARTITIONINFORMATIONA(EasyCastStructure):
    PhysicalMedia: Guid
    LogicalMedia: Guid
    State: UInt32
    Side: UInt16
    dwOmidLabelIdLength: UInt32
    OmidLabelId: Byte * 255
    szOmidLabelType: win32more.Windows.Win32.Foundation.CHAR * 64
    szOmidLabelInfo: win32more.Windows.Win32.Foundation.CHAR * 256
    dwMountCount: UInt32
    dwAllocateCount: UInt32
class NTMS_I1_PARTITIONINFORMATIONW(EasyCastStructure):
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
class NTMS_I1_PMIDINFORMATIONA(EasyCastStructure):
    CurrentLibrary: Guid
    MediaPool: Guid
    Location: Guid
    LocationType: UInt32
    MediaType: Guid
    HomeSlot: Guid
    szBarCode: win32more.Windows.Win32.Foundation.CHAR * 64
    BarCodeState: UInt32
    szSequenceNumber: win32more.Windows.Win32.Foundation.CHAR * 32
    MediaState: UInt32
    dwNumberOfPartitions: UInt32
class NTMS_I1_PMIDINFORMATIONW(EasyCastStructure):
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
class NTMS_IEDOORINFORMATION(EasyCastStructure):
    Number: UInt32
    State: UInt32
    MaxOpenSecs: UInt16
    Library: Guid
class NTMS_IEPORTINFORMATION(EasyCastStructure):
    Number: UInt32
    Content: UInt32
    Position: UInt32
    MaxExtendSecs: UInt16
    Library: Guid
class NTMS_LIBRARYINFORMATION(EasyCastStructure):
    LibraryType: UInt32
    CleanerSlot: Guid
    CleanerSlotDefault: Guid
    LibrarySupportsDriveCleaning: win32more.Windows.Win32.Foundation.BOOL
    BarCodeReaderInstalled: win32more.Windows.Win32.Foundation.BOOL
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
    AutoRecovery: win32more.Windows.Win32.Foundation.BOOL
    dwFlags: UInt32
class NTMS_LIBREQUESTINFORMATIONA(EasyCastStructure):
    OperationCode: UInt32
    OperationOption: UInt32
    State: UInt32
    PartitionId: Guid
    DriveId: Guid
    PhysMediaId: Guid
    Library: Guid
    SlotId: Guid
    TimeQueued: win32more.Windows.Win32.Foundation.SYSTEMTIME
    TimeCompleted: win32more.Windows.Win32.Foundation.SYSTEMTIME
    szApplication: win32more.Windows.Win32.Foundation.CHAR * 64
    szUser: win32more.Windows.Win32.Foundation.CHAR * 64
    szComputer: win32more.Windows.Win32.Foundation.CHAR * 64
    dwErrorCode: UInt32
    WorkItemId: Guid
    dwPriority: UInt32
class NTMS_LIBREQUESTINFORMATIONW(EasyCastStructure):
    OperationCode: UInt32
    OperationOption: UInt32
    State: UInt32
    PartitionId: Guid
    DriveId: Guid
    PhysMediaId: Guid
    Library: Guid
    SlotId: Guid
    TimeQueued: win32more.Windows.Win32.Foundation.SYSTEMTIME
    TimeCompleted: win32more.Windows.Win32.Foundation.SYSTEMTIME
    szApplication: Char * 64
    szUser: Char * 64
    szComputer: Char * 64
    dwErrorCode: UInt32
    WorkItemId: Guid
    dwPriority: UInt32
class NTMS_LMIDINFORMATION(EasyCastStructure):
    MediaPool: Guid
    dwNumberOfPartitions: UInt32
class NTMS_MEDIAPOOLINFORMATION(EasyCastStructure):
    PoolType: UInt32
    MediaType: Guid
    Parent: Guid
    AllocationPolicy: UInt32
    DeallocationPolicy: UInt32
    dwMaxAllocates: UInt32
    dwNumberOfPhysicalMedia: UInt32
    dwNumberOfLogicalMedia: UInt32
    dwNumberOfMediaPools: UInt32
class NTMS_MEDIATYPEINFORMATION(EasyCastStructure):
    MediaType: UInt32
    NumberOfSides: UInt32
    ReadWriteCharacteristics: UInt32
    DeviceType: win32more.Windows.Win32.Storage.FileSystem.FILE_DEVICE_TYPE
class NTMS_MOUNT_INFORMATION(EasyCastStructure):
    dwSize: UInt32
    lpReserved: VoidPtr
class NTMS_NOTIFICATIONINFORMATION(EasyCastStructure):
    dwOperation: UInt32
    ObjectId: Guid
class NTMS_OBJECTINFORMATIONA(EasyCastStructure):
    dwSize: UInt32
    dwType: UInt32
    Created: win32more.Windows.Win32.Foundation.SYSTEMTIME
    Modified: win32more.Windows.Win32.Foundation.SYSTEMTIME
    ObjectGuid: Guid
    Enabled: win32more.Windows.Win32.Foundation.BOOL
    dwOperationalState: UInt32
    szName: win32more.Windows.Win32.Foundation.CHAR * 64
    szDescription: win32more.Windows.Win32.Foundation.CHAR * 127
    Info: _Info_e__Union
    class _Info_e__Union(EasyCastUnion):
        Drive: win32more.Windows.Win32.Storage.FileSystem.NTMS_DRIVEINFORMATIONA
        DriveType: win32more.Windows.Win32.Storage.FileSystem.NTMS_DRIVETYPEINFORMATIONA
        Library: win32more.Windows.Win32.Storage.FileSystem.NTMS_LIBRARYINFORMATION
        Changer: win32more.Windows.Win32.Storage.FileSystem.NTMS_CHANGERINFORMATIONA
        ChangerType: win32more.Windows.Win32.Storage.FileSystem.NTMS_CHANGERTYPEINFORMATIONA
        StorageSlot: win32more.Windows.Win32.Storage.FileSystem.NTMS_STORAGESLOTINFORMATION
        IEDoor: win32more.Windows.Win32.Storage.FileSystem.NTMS_IEDOORINFORMATION
        IEPort: win32more.Windows.Win32.Storage.FileSystem.NTMS_IEPORTINFORMATION
        PhysicalMedia: win32more.Windows.Win32.Storage.FileSystem.NTMS_PMIDINFORMATIONA
        LogicalMedia: win32more.Windows.Win32.Storage.FileSystem.NTMS_LMIDINFORMATION
        Partition: win32more.Windows.Win32.Storage.FileSystem.NTMS_PARTITIONINFORMATIONA
        MediaPool: win32more.Windows.Win32.Storage.FileSystem.NTMS_MEDIAPOOLINFORMATION
        MediaType: win32more.Windows.Win32.Storage.FileSystem.NTMS_MEDIATYPEINFORMATION
        LibRequest: win32more.Windows.Win32.Storage.FileSystem.NTMS_LIBREQUESTINFORMATIONA
        OpRequest: win32more.Windows.Win32.Storage.FileSystem.NTMS_OPREQUESTINFORMATIONA
        Computer: win32more.Windows.Win32.Storage.FileSystem.NTMS_COMPUTERINFORMATION
class NTMS_OBJECTINFORMATIONW(EasyCastStructure):
    dwSize: UInt32
    dwType: UInt32
    Created: win32more.Windows.Win32.Foundation.SYSTEMTIME
    Modified: win32more.Windows.Win32.Foundation.SYSTEMTIME
    ObjectGuid: Guid
    Enabled: win32more.Windows.Win32.Foundation.BOOL
    dwOperationalState: UInt32
    szName: Char * 64
    szDescription: Char * 127
    Info: _Info_e__Union
    class _Info_e__Union(EasyCastUnion):
        Drive: win32more.Windows.Win32.Storage.FileSystem.NTMS_DRIVEINFORMATIONW
        DriveType: win32more.Windows.Win32.Storage.FileSystem.NTMS_DRIVETYPEINFORMATIONW
        Library: win32more.Windows.Win32.Storage.FileSystem.NTMS_LIBRARYINFORMATION
        Changer: win32more.Windows.Win32.Storage.FileSystem.NTMS_CHANGERINFORMATIONW
        ChangerType: win32more.Windows.Win32.Storage.FileSystem.NTMS_CHANGERTYPEINFORMATIONW
        StorageSlot: win32more.Windows.Win32.Storage.FileSystem.NTMS_STORAGESLOTINFORMATION
        IEDoor: win32more.Windows.Win32.Storage.FileSystem.NTMS_IEDOORINFORMATION
        IEPort: win32more.Windows.Win32.Storage.FileSystem.NTMS_IEPORTINFORMATION
        PhysicalMedia: win32more.Windows.Win32.Storage.FileSystem.NTMS_PMIDINFORMATIONW
        LogicalMedia: win32more.Windows.Win32.Storage.FileSystem.NTMS_LMIDINFORMATION
        Partition: win32more.Windows.Win32.Storage.FileSystem.NTMS_PARTITIONINFORMATIONW
        MediaPool: win32more.Windows.Win32.Storage.FileSystem.NTMS_MEDIAPOOLINFORMATION
        MediaType: win32more.Windows.Win32.Storage.FileSystem.NTMS_MEDIATYPEINFORMATION
        LibRequest: win32more.Windows.Win32.Storage.FileSystem.NTMS_LIBREQUESTINFORMATIONW
        OpRequest: win32more.Windows.Win32.Storage.FileSystem.NTMS_OPREQUESTINFORMATIONW
        Computer: win32more.Windows.Win32.Storage.FileSystem.NTMS_COMPUTERINFORMATION
NTMS_OMID_TYPE = UInt32
NTMS_OMID_TYPE_FILESYSTEM_INFO: NTMS_OMID_TYPE = 2
NTMS_OMID_TYPE_RAW_LABEL: NTMS_OMID_TYPE = 1
class NTMS_OPREQUESTINFORMATIONA(EasyCastStructure):
    Request: UInt32
    Submitted: win32more.Windows.Win32.Foundation.SYSTEMTIME
    State: UInt32
    szMessage: win32more.Windows.Win32.Foundation.CHAR * 256
    Arg1Type: UInt32
    Arg1: Guid
    Arg2Type: UInt32
    Arg2: Guid
    szApplication: win32more.Windows.Win32.Foundation.CHAR * 64
    szUser: win32more.Windows.Win32.Foundation.CHAR * 64
    szComputer: win32more.Windows.Win32.Foundation.CHAR * 64
class NTMS_OPREQUESTINFORMATIONW(EasyCastStructure):
    Request: UInt32
    Submitted: win32more.Windows.Win32.Foundation.SYSTEMTIME
    State: UInt32
    szMessage: Char * 256
    Arg1Type: UInt32
    Arg1: Guid
    Arg2Type: UInt32
    Arg2: Guid
    szApplication: Char * 64
    szUser: Char * 64
    szComputer: Char * 64
class NTMS_PARTITIONINFORMATIONA(EasyCastStructure):
    PhysicalMedia: Guid
    LogicalMedia: Guid
    State: UInt32
    Side: UInt16
    dwOmidLabelIdLength: UInt32
    OmidLabelId: Byte * 255
    szOmidLabelType: win32more.Windows.Win32.Foundation.CHAR * 64
    szOmidLabelInfo: win32more.Windows.Win32.Foundation.CHAR * 256
    dwMountCount: UInt32
    dwAllocateCount: UInt32
    Capacity: Int64
class NTMS_PARTITIONINFORMATIONW(EasyCastStructure):
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
    Capacity: Int64
class NTMS_PMIDINFORMATIONA(EasyCastStructure):
    CurrentLibrary: Guid
    MediaPool: Guid
    Location: Guid
    LocationType: UInt32
    MediaType: Guid
    HomeSlot: Guid
    szBarCode: win32more.Windows.Win32.Foundation.CHAR * 64
    BarCodeState: UInt32
    szSequenceNumber: win32more.Windows.Win32.Foundation.CHAR * 32
    MediaState: UInt32
    dwNumberOfPartitions: UInt32
    dwMediaTypeCode: UInt32
    dwDensityCode: UInt32
    MountedPartition: Guid
class NTMS_PMIDINFORMATIONW(EasyCastStructure):
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
    dwMediaTypeCode: UInt32
    dwDensityCode: UInt32
    MountedPartition: Guid
class NTMS_STORAGESLOTINFORMATION(EasyCastStructure):
    Number: UInt32
    State: UInt32
    Library: Guid
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
class OFSTRUCT(EasyCastStructure):
    cBytes: Byte
    fFixedDisk: Byte
    nErrCode: UInt16
    Reserved1: UInt16
    Reserved2: UInt16
    szPathName: win32more.Windows.Win32.Foundation.CHAR * 128
@winfunctype_pointer
def PCLFS_COMPLETION_ROUTINE(pvOverlapped: VoidPtr, ulReserved: UInt32) -> Void: ...
@winfunctype_pointer
def PCOPYFILE2_PROGRESS_ROUTINE(pMessage: POINTER(win32more.Windows.Win32.Storage.FileSystem.COPYFILE2_MESSAGE_head), pvCallbackContext: VoidPtr) -> win32more.Windows.Win32.Storage.FileSystem.COPYFILE2_MESSAGE_ACTION: ...
@winfunctype_pointer
def PFE_EXPORT_FUNC(pbData: POINTER(Byte), pvCallbackContext: VoidPtr, ulLength: UInt32) -> UInt32: ...
@winfunctype_pointer
def PFE_IMPORT_FUNC(pbData: POINTER(Byte), pvCallbackContext: VoidPtr, ulLength: POINTER(UInt32)) -> UInt32: ...
@winfunctype_pointer
def PFN_IO_COMPLETION(pContext: POINTER(win32more.Windows.Win32.Storage.FileSystem.FIO_CONTEXT_head), lpo: POINTER(win32more.Windows.Win32.Storage.FileSystem.FH_OVERLAPPED_head), cb: UInt32, dwCompletionStatus: UInt32) -> Void: ...
@winfunctype_pointer
def PLOG_FULL_HANDLER_CALLBACK(hLogFile: win32more.Windows.Win32.Foundation.HANDLE, dwError: UInt32, fLogIsPinned: win32more.Windows.Win32.Foundation.BOOL, pvClientContext: VoidPtr) -> Void: ...
@winfunctype_pointer
def PLOG_TAIL_ADVANCE_CALLBACK(hLogFile: win32more.Windows.Win32.Foundation.HANDLE, lsnTarget: win32more.Windows.Win32.Storage.FileSystem.CLS_LSN, pvClientContext: VoidPtr) -> Void: ...
@winfunctype_pointer
def PLOG_UNPINNED_CALLBACK(hLogFile: win32more.Windows.Win32.Foundation.HANDLE, pvClientContext: VoidPtr) -> Void: ...
PREPARE_TAPE_OPERATION = UInt32
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
READ_DIRECTORY_NOTIFY_INFORMATION_CLASS_ReadDirectoryNotifyFullInformation: READ_DIRECTORY_NOTIFY_INFORMATION_CLASS = 3
READ_DIRECTORY_NOTIFY_INFORMATION_CLASS_ReadDirectoryNotifyMaximumInformation: READ_DIRECTORY_NOTIFY_INFORMATION_CLASS = 4
class REPARSE_GUID_DATA_BUFFER(EasyCastStructure):
    ReparseTag: UInt32
    ReparseDataLength: UInt16
    Reserved: UInt16
    ReparseGuid: Guid
    GenericReparseBuffer: _GenericReparseBuffer_e__Struct
    class _GenericReparseBuffer_e__Struct(EasyCastStructure):
        DataBuffer: Byte * 1
REPLACE_FILE_FLAGS = UInt32
REPLACEFILE_WRITE_THROUGH: REPLACE_FILE_FLAGS = 1
REPLACEFILE_IGNORE_MERGE_ERRORS: REPLACE_FILE_FLAGS = 2
REPLACEFILE_IGNORE_ACL_ERRORS: REPLACE_FILE_FLAGS = 4
class SERVER_ALIAS_INFO_0(EasyCastStructure):
    srvai0_alias: win32more.Windows.Win32.Foundation.PWSTR
    srvai0_target: win32more.Windows.Win32.Foundation.PWSTR
    srvai0_default: win32more.Windows.Win32.Foundation.BOOLEAN
    srvai0_reserved: UInt32
class SERVER_CERTIFICATE_INFO_0(EasyCastStructure):
    srvci0_name: win32more.Windows.Win32.Foundation.PWSTR
    srvci0_subject: win32more.Windows.Win32.Foundation.PWSTR
    srvci0_issuer: win32more.Windows.Win32.Foundation.PWSTR
    srvci0_thumbprint: win32more.Windows.Win32.Foundation.PWSTR
    srvci0_friendlyname: win32more.Windows.Win32.Foundation.PWSTR
    srvci0_notbefore: win32more.Windows.Win32.Foundation.PWSTR
    srvci0_notafter: win32more.Windows.Win32.Foundation.PWSTR
    srvci0_storelocation: win32more.Windows.Win32.Foundation.PWSTR
    srvci0_storename: win32more.Windows.Win32.Foundation.PWSTR
    srvci0_renewalchain: win32more.Windows.Win32.Foundation.PWSTR
    srvci0_type: UInt32
    srvci0_flags: UInt32
    srvci0_mapping_status: UInt32
SERVER_CERTIFICATE_TYPE = Int32
QUIC: SERVER_CERTIFICATE_TYPE = 0
class SESSION_INFO_0(EasyCastStructure):
    sesi0_cname: win32more.Windows.Win32.Foundation.PWSTR
class SESSION_INFO_1(EasyCastStructure):
    sesi1_cname: win32more.Windows.Win32.Foundation.PWSTR
    sesi1_username: win32more.Windows.Win32.Foundation.PWSTR
    sesi1_num_opens: UInt32
    sesi1_time: UInt32
    sesi1_idle_time: UInt32
    sesi1_user_flags: win32more.Windows.Win32.Storage.FileSystem.SESSION_INFO_USER_FLAGS
class SESSION_INFO_10(EasyCastStructure):
    sesi10_cname: win32more.Windows.Win32.Foundation.PWSTR
    sesi10_username: win32more.Windows.Win32.Foundation.PWSTR
    sesi10_time: UInt32
    sesi10_idle_time: UInt32
class SESSION_INFO_2(EasyCastStructure):
    sesi2_cname: win32more.Windows.Win32.Foundation.PWSTR
    sesi2_username: win32more.Windows.Win32.Foundation.PWSTR
    sesi2_num_opens: UInt32
    sesi2_time: UInt32
    sesi2_idle_time: UInt32
    sesi2_user_flags: win32more.Windows.Win32.Storage.FileSystem.SESSION_INFO_USER_FLAGS
    sesi2_cltype_name: win32more.Windows.Win32.Foundation.PWSTR
class SESSION_INFO_502(EasyCastStructure):
    sesi502_cname: win32more.Windows.Win32.Foundation.PWSTR
    sesi502_username: win32more.Windows.Win32.Foundation.PWSTR
    sesi502_num_opens: UInt32
    sesi502_time: UInt32
    sesi502_idle_time: UInt32
    sesi502_user_flags: win32more.Windows.Win32.Storage.FileSystem.SESSION_INFO_USER_FLAGS
    sesi502_cltype_name: win32more.Windows.Win32.Foundation.PWSTR
    sesi502_transport: win32more.Windows.Win32.Foundation.PWSTR
SESSION_INFO_USER_FLAGS = UInt32
SESS_GUEST: SESSION_INFO_USER_FLAGS = 1
SESS_NOENCRYPTION: SESSION_INFO_USER_FLAGS = 2
SET_FILE_POINTER_MOVE_METHOD = UInt32
FILE_BEGIN: SET_FILE_POINTER_MOVE_METHOD = 0
FILE_CURRENT: SET_FILE_POINTER_MOVE_METHOD = 1
FILE_END: SET_FILE_POINTER_MOVE_METHOD = 2
class SHARE_INFO_0(EasyCastStructure):
    shi0_netname: win32more.Windows.Win32.Foundation.PWSTR
class SHARE_INFO_1(EasyCastStructure):
    shi1_netname: win32more.Windows.Win32.Foundation.PWSTR
    shi1_type: win32more.Windows.Win32.Storage.FileSystem.SHARE_TYPE
    shi1_remark: win32more.Windows.Win32.Foundation.PWSTR
class SHARE_INFO_1004(EasyCastStructure):
    shi1004_remark: win32more.Windows.Win32.Foundation.PWSTR
class SHARE_INFO_1005(EasyCastStructure):
    shi1005_flags: UInt32
class SHARE_INFO_1006(EasyCastStructure):
    shi1006_max_uses: UInt32
class SHARE_INFO_1501(EasyCastStructure):
    shi1501_reserved: UInt32
    shi1501_security_descriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR
class SHARE_INFO_1503(EasyCastStructure):
    shi1503_sharefilter: Guid
class SHARE_INFO_2(EasyCastStructure):
    shi2_netname: win32more.Windows.Win32.Foundation.PWSTR
    shi2_type: win32more.Windows.Win32.Storage.FileSystem.SHARE_TYPE
    shi2_remark: win32more.Windows.Win32.Foundation.PWSTR
    shi2_permissions: win32more.Windows.Win32.Storage.FileSystem.SHARE_INFO_PERMISSIONS
    shi2_max_uses: UInt32
    shi2_current_uses: UInt32
    shi2_path: win32more.Windows.Win32.Foundation.PWSTR
    shi2_passwd: win32more.Windows.Win32.Foundation.PWSTR
class SHARE_INFO_501(EasyCastStructure):
    shi501_netname: win32more.Windows.Win32.Foundation.PWSTR
    shi501_type: win32more.Windows.Win32.Storage.FileSystem.SHARE_TYPE
    shi501_remark: win32more.Windows.Win32.Foundation.PWSTR
    shi501_flags: UInt32
class SHARE_INFO_502(EasyCastStructure):
    shi502_netname: win32more.Windows.Win32.Foundation.PWSTR
    shi502_type: win32more.Windows.Win32.Storage.FileSystem.SHARE_TYPE
    shi502_remark: win32more.Windows.Win32.Foundation.PWSTR
    shi502_permissions: win32more.Windows.Win32.Storage.FileSystem.SHARE_INFO_PERMISSIONS
    shi502_max_uses: UInt32
    shi502_current_uses: UInt32
    shi502_path: win32more.Windows.Win32.Foundation.PWSTR
    shi502_passwd: win32more.Windows.Win32.Foundation.PWSTR
    shi502_reserved: UInt32
    shi502_security_descriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR
class SHARE_INFO_503(EasyCastStructure):
    shi503_netname: win32more.Windows.Win32.Foundation.PWSTR
    shi503_type: win32more.Windows.Win32.Storage.FileSystem.SHARE_TYPE
    shi503_remark: win32more.Windows.Win32.Foundation.PWSTR
    shi503_permissions: win32more.Windows.Win32.Storage.FileSystem.SHARE_INFO_PERMISSIONS
    shi503_max_uses: UInt32
    shi503_current_uses: UInt32
    shi503_path: win32more.Windows.Win32.Foundation.PWSTR
    shi503_passwd: win32more.Windows.Win32.Foundation.PWSTR
    shi503_servername: win32more.Windows.Win32.Foundation.PWSTR
    shi503_reserved: UInt32
    shi503_security_descriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR
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
class STAT_SERVER_0(EasyCastStructure):
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
class STAT_WORKSTATION_0(EasyCastStructure):
    StatisticsStartTime: Int64
    BytesReceived: Int64
    SmbsReceived: Int64
    PagingReadBytesRequested: Int64
    NonPagingReadBytesRequested: Int64
    CacheReadBytesRequested: Int64
    NetworkReadBytesRequested: Int64
    BytesTransmitted: Int64
    SmbsTransmitted: Int64
    PagingWriteBytesRequested: Int64
    NonPagingWriteBytesRequested: Int64
    CacheWriteBytesRequested: Int64
    NetworkWriteBytesRequested: Int64
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
TAPEMARK_TYPE = UInt32
TAPE_FILEMARKS: TAPEMARK_TYPE = 1
TAPE_LONG_FILEMARKS: TAPEMARK_TYPE = 3
TAPE_SETMARKS: TAPEMARK_TYPE = 0
TAPE_SHORT_FILEMARKS: TAPEMARK_TYPE = 2
class TAPE_ERASE(EasyCastStructure):
    Type: win32more.Windows.Win32.Storage.FileSystem.ERASE_TAPE_TYPE
    Immediate: win32more.Windows.Win32.Foundation.BOOLEAN
class TAPE_GET_POSITION(EasyCastStructure):
    Type: win32more.Windows.Win32.Storage.FileSystem.TAPE_POSITION_TYPE
    Partition: UInt32
    Offset: Int64
TAPE_INFORMATION_TYPE = UInt32
SET_TAPE_DRIVE_INFORMATION: TAPE_INFORMATION_TYPE = 1
SET_TAPE_MEDIA_INFORMATION: TAPE_INFORMATION_TYPE = 0
TAPE_POSITION_METHOD = UInt32
TAPE_ABSOLUTE_BLOCK: TAPE_POSITION_METHOD = 1
TAPE_LOGICAL_BLOCK: TAPE_POSITION_METHOD = 2
TAPE_REWIND: TAPE_POSITION_METHOD = 0
TAPE_SPACE_END_OF_DATA: TAPE_POSITION_METHOD = 4
TAPE_SPACE_FILEMARKS: TAPE_POSITION_METHOD = 6
TAPE_SPACE_RELATIVE_BLOCKS: TAPE_POSITION_METHOD = 5
TAPE_SPACE_SEQUENTIAL_FMKS: TAPE_POSITION_METHOD = 7
TAPE_SPACE_SEQUENTIAL_SMKS: TAPE_POSITION_METHOD = 9
TAPE_SPACE_SETMARKS: TAPE_POSITION_METHOD = 8
TAPE_POSITION_TYPE = UInt32
TAPE_ABSOLUTE_POSITION: TAPE_POSITION_TYPE = 0
TAPE_LOGICAL_POSITION: TAPE_POSITION_TYPE = 1
class TAPE_PREPARE(EasyCastStructure):
    Operation: win32more.Windows.Win32.Storage.FileSystem.PREPARE_TAPE_OPERATION
    Immediate: win32more.Windows.Win32.Foundation.BOOLEAN
class TAPE_SET_POSITION(EasyCastStructure):
    Method: win32more.Windows.Win32.Storage.FileSystem.TAPE_POSITION_METHOD
    Partition: UInt32
    Offset: Int64
    Immediate: win32more.Windows.Win32.Foundation.BOOLEAN
class TAPE_WRITE_MARKS(EasyCastStructure):
    Type: win32more.Windows.Win32.Storage.FileSystem.TAPEMARK_TYPE
    Count: UInt32
    Immediate: win32more.Windows.Win32.Foundation.BOOLEAN
class TRANSACTION_NOTIFICATION(EasyCastStructure):
    TransactionKey: VoidPtr
    TransactionNotification: UInt32
    TmVirtualClock: Int64
    ArgumentLength: UInt32
class TRANSACTION_NOTIFICATION_MARSHAL_ARGUMENT(EasyCastStructure):
    MarshalCookie: UInt32
    UOW: Guid
class TRANSACTION_NOTIFICATION_PROPAGATE_ARGUMENT(EasyCastStructure):
    PropagationCookie: UInt32
    UOW: Guid
    TmIdentity: Guid
    BufferLength: UInt32
class TRANSACTION_NOTIFICATION_RECOVERY_ARGUMENT(EasyCastStructure):
    EnlistmentId: Guid
    UOW: Guid
class TRANSACTION_NOTIFICATION_SAVEPOINT_ARGUMENT(EasyCastStructure):
    SavepointId: UInt32
class TRANSACTION_NOTIFICATION_TM_ONLINE_ARGUMENT(EasyCastStructure):
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
class TXF_ID(EasyCastStructure):
    Anonymous: _Anonymous_e__Struct
    _pack_ = 4
    class _Anonymous_e__Struct(EasyCastStructure):
        LowPart: Int64
        HighPart: Int64
        _pack_ = 4
class TXF_LOG_RECORD_AFFECTED_FILE(EasyCastStructure):
    Version: UInt16
    RecordLength: UInt32
    Flags: UInt32
    TxfFileId: win32more.Windows.Win32.Storage.FileSystem.TXF_ID
    KtmGuid: Guid
    FileNameLength: UInt32
    FileNameByteOffsetInStructure: UInt32
    _pack_ = 4
class TXF_LOG_RECORD_BASE(EasyCastStructure):
    Version: UInt16
    RecordType: win32more.Windows.Win32.Storage.FileSystem.TXF_LOG_RECORD_TYPE
    RecordLength: UInt32
    _pack_ = 4
class TXF_LOG_RECORD_TRUNCATE(EasyCastStructure):
    Version: UInt16
    RecordType: UInt16
    RecordLength: UInt32
    Flags: UInt32
    TxfFileId: win32more.Windows.Win32.Storage.FileSystem.TXF_ID
    KtmGuid: Guid
    NewFileSize: Int64
    FileNameLength: UInt32
    FileNameByteOffsetInStructure: UInt32
    _pack_ = 4
TXF_LOG_RECORD_TYPE = UInt16
TXF_LOG_RECORD_TYPE_AFFECTED_FILE: TXF_LOG_RECORD_TYPE = 4
TXF_LOG_RECORD_TYPE_TRUNCATE: TXF_LOG_RECORD_TYPE = 2
TXF_LOG_RECORD_TYPE_WRITE: TXF_LOG_RECORD_TYPE = 1
class TXF_LOG_RECORD_WRITE(EasyCastStructure):
    Version: UInt16
    RecordType: UInt16
    RecordLength: UInt32
    Flags: UInt32
    TxfFileId: win32more.Windows.Win32.Storage.FileSystem.TXF_ID
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
class VOLUME_ALLOCATE_BC_STREAM_INPUT(EasyCastStructure):
    Version: UInt32
    RequestsPerPeriod: UInt32
    Period: UInt32
    RetryFailures: win32more.Windows.Win32.Foundation.BOOLEAN
    Discardable: win32more.Windows.Win32.Foundation.BOOLEAN
    Reserved1: win32more.Windows.Win32.Foundation.BOOLEAN * 2
    LowestByteOffset: UInt64
    HighestByteOffset: UInt64
    AccessType: UInt32
    AccessMode: UInt32
class VOLUME_ALLOCATE_BC_STREAM_OUTPUT(EasyCastStructure):
    RequestSize: UInt64
    NumOutStandingRequests: UInt32
class VOLUME_ALLOCATION_HINT_INPUT(EasyCastStructure):
    ClusterSize: UInt32
    NumberOfClusters: UInt32
    StartingClusterNumber: Int64
class VOLUME_ALLOCATION_HINT_OUTPUT(EasyCastStructure):
    Bitmap: UInt32 * 1
class VOLUME_CRITICAL_IO(EasyCastStructure):
    AccessType: UInt32
    ExtentsCount: UInt32
    Extents: win32more.Windows.Win32.Storage.FileSystem.FILE_EXTENT * 1
class VOLUME_FAILOVER_SET(EasyCastStructure):
    NumberOfDisks: UInt32
    DiskNumbers: UInt32 * 1
class VOLUME_GET_BC_PROPERTIES_INPUT(EasyCastStructure):
    Version: UInt32
    Reserved1: UInt32
    LowestByteOffset: UInt64
    HighestByteOffset: UInt64
    AccessType: UInt32
    AccessMode: UInt32
class VOLUME_GET_BC_PROPERTIES_OUTPUT(EasyCastStructure):
    MaximumRequestsPerPeriod: UInt32
    MinimumPeriod: UInt32
    MaximumRequestSize: UInt64
    EstimatedTimePerRequest: UInt32
    NumOutStandingRequests: UInt32
    RequestSize: UInt64
class VOLUME_LOGICAL_OFFSET(EasyCastStructure):
    LogicalOffset: Int64
class VOLUME_NUMBER(EasyCastStructure):
    VolumeNumber: UInt32
    VolumeManagerName: Char * 8
class VOLUME_PHYSICAL_OFFSET(EasyCastStructure):
    DiskNumber: UInt32
    Offset: Int64
class VOLUME_PHYSICAL_OFFSETS(EasyCastStructure):
    NumberOfPhysicalOffsets: UInt32
    PhysicalOffset: win32more.Windows.Win32.Storage.FileSystem.VOLUME_PHYSICAL_OFFSET * 1
class VOLUME_READ_PLEX_INPUT(EasyCastStructure):
    ByteOffset: Int64
    Length: UInt32
    PlexNumber: UInt32
class VOLUME_SET_GPT_ATTRIBUTES_INFORMATION(EasyCastStructure):
    GptAttributes: UInt64
    RevertOnClose: win32more.Windows.Win32.Foundation.BOOLEAN
    ApplyToAllConnectedVolumes: win32more.Windows.Win32.Foundation.BOOLEAN
    Reserved1: UInt16
    Reserved2: UInt32
class VOLUME_SHRINK_INFO(EasyCastStructure):
    VolumeSize: UInt64
class VS_FIXEDFILEINFO(EasyCastStructure):
    dwSignature: UInt32
    dwStrucVersion: UInt32
    dwFileVersionMS: UInt32
    dwFileVersionLS: UInt32
    dwProductVersionMS: UInt32
    dwProductVersionLS: UInt32
    dwFileFlagsMask: UInt32
    dwFileFlags: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_FLAGS
    dwFileOS: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_OS
    dwFileType: UInt32
    dwFileSubtype: UInt32
    dwFileDateMS: UInt32
    dwFileDateLS: UInt32
VS_FIXEDFILEINFO_FILE_FLAGS = UInt32
VS_FF_DEBUG: VS_FIXEDFILEINFO_FILE_FLAGS = 1
VS_FF_PRERELEASE: VS_FIXEDFILEINFO_FILE_FLAGS = 2
VS_FF_PATCHED: VS_FIXEDFILEINFO_FILE_FLAGS = 4
VS_FF_PRIVATEBUILD: VS_FIXEDFILEINFO_FILE_FLAGS = 8
VS_FF_INFOINFERRED: VS_FIXEDFILEINFO_FILE_FLAGS = 16
VS_FF_SPECIALBUILD: VS_FIXEDFILEINFO_FILE_FLAGS = 32
VS_FIXEDFILEINFO_FILE_OS = UInt32
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
class WIM_ENTRY_INFO(EasyCastStructure):
    WimEntryInfoSize: UInt32
    WimType: UInt32
    DataSourceId: Int64
    WimGuid: Guid
    WimPath: win32more.Windows.Win32.Foundation.PWSTR
    WimIndex: UInt32
    Flags: UInt32
class WIM_EXTERNAL_FILE_INFO(EasyCastStructure):
    DataSourceId: Int64
    ResourceHash: Byte * 20
    Flags: UInt32
class WIN32_FILE_ATTRIBUTE_DATA(EasyCastStructure):
    dwFileAttributes: UInt32
    ftCreationTime: win32more.Windows.Win32.Foundation.FILETIME
    ftLastAccessTime: win32more.Windows.Win32.Foundation.FILETIME
    ftLastWriteTime: win32more.Windows.Win32.Foundation.FILETIME
    nFileSizeHigh: UInt32
    nFileSizeLow: UInt32
class WIN32_FIND_DATAA(EasyCastStructure):
    dwFileAttributes: UInt32
    ftCreationTime: win32more.Windows.Win32.Foundation.FILETIME
    ftLastAccessTime: win32more.Windows.Win32.Foundation.FILETIME
    ftLastWriteTime: win32more.Windows.Win32.Foundation.FILETIME
    nFileSizeHigh: UInt32
    nFileSizeLow: UInt32
    dwReserved0: UInt32
    dwReserved1: UInt32
    cFileName: win32more.Windows.Win32.Foundation.CHAR * 260
    cAlternateFileName: win32more.Windows.Win32.Foundation.CHAR * 14
class WIN32_FIND_DATAW(EasyCastStructure):
    dwFileAttributes: UInt32
    ftCreationTime: win32more.Windows.Win32.Foundation.FILETIME
    ftLastAccessTime: win32more.Windows.Win32.Foundation.FILETIME
    ftLastWriteTime: win32more.Windows.Win32.Foundation.FILETIME
    nFileSizeHigh: UInt32
    nFileSizeLow: UInt32
    dwReserved0: UInt32
    dwReserved1: UInt32
    cFileName: Char * 260
    cAlternateFileName: Char * 14
class WIN32_FIND_STREAM_DATA(EasyCastStructure):
    StreamSize: Int64
    cStreamName: Char * 296
class WIN32_STREAM_ID(EasyCastStructure):
    dwStreamId: win32more.Windows.Win32.Storage.FileSystem.WIN_STREAM_ID
    dwStreamAttributes: UInt32
    Size: Int64
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
class WOF_FILE_COMPRESSION_INFO_V0(EasyCastStructure):
    Algorithm: UInt32
class WOF_FILE_COMPRESSION_INFO_V1(EasyCastStructure):
    Algorithm: UInt32
    Flags: UInt32
@winfunctype_pointer
def WofEnumEntryProc(EntryInfo: VoidPtr, UserData: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def WofEnumFilesProc(FilePath: win32more.Windows.Win32.Foundation.PWSTR, ExternalFileInfo: VoidPtr, UserData: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
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
make_head(_module, 'FILE_DISPOSITION_INFO_EX')
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
