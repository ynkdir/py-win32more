from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Security
import win32more.Windows.Win32.Security.Cryptography
import win32more.Windows.Win32.Storage.FileSystem
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.IO
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
COPYFILE2_MESSAGE_COPY_OFFLOAD: Int32 = 1
COPYFILE2_IO_CYCLE_SIZE_MIN: UInt32 = 4096
COPYFILE2_IO_CYCLE_SIZE_MAX: UInt32 = 1073741824
COPYFILE2_IO_RATE_MIN: UInt32 = 512
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
SearchPath = UnicodeAlias('SearchPathW')
@winfunctype('KERNEL32.dll')
def SearchPathA(lpPath: win32more.Windows.Win32.Foundation.PSTR, lpFileName: win32more.Windows.Win32.Foundation.PSTR, lpExtension: win32more.Windows.Win32.Foundation.PSTR, nBufferLength: UInt32, lpBuffer: win32more.Windows.Win32.Foundation.PSTR, lpFilePart: POINTER(win32more.Windows.Win32.Foundation.PSTR)) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def CompareFileTime(lpFileTime1: POINTER(win32more.Windows.Win32.Foundation.FILETIME), lpFileTime2: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> Int32: ...
@winfunctype('KERNEL32.dll')
def CreateDirectoryA(lpPathName: win32more.Windows.Win32.Foundation.PSTR, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateDirectoryW(lpPathName: win32more.Windows.Win32.Foundation.PWSTR, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES)) -> win32more.Windows.Win32.Foundation.BOOL: ...
CreateDirectory = UnicodeAlias('CreateDirectoryW')
@winfunctype('KERNEL32.dll')
def CreateFileA(lpFileName: win32more.Windows.Win32.Foundation.PSTR, dwDesiredAccess: UInt32, dwShareMode: win32more.Windows.Win32.Storage.FileSystem.FILE_SHARE_MODE, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), dwCreationDisposition: win32more.Windows.Win32.Storage.FileSystem.FILE_CREATION_DISPOSITION, dwFlagsAndAttributes: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES, hTemplateFile: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def CreateFileW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, dwDesiredAccess: UInt32, dwShareMode: win32more.Windows.Win32.Storage.FileSystem.FILE_SHARE_MODE, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), dwCreationDisposition: win32more.Windows.Win32.Storage.FileSystem.FILE_CREATION_DISPOSITION, dwFlagsAndAttributes: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES, hTemplateFile: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HANDLE: ...
CreateFile = UnicodeAlias('CreateFileW')
@winfunctype('KERNEL32.dll')
def DefineDosDeviceW(dwFlags: win32more.Windows.Win32.Storage.FileSystem.DEFINE_DOS_DEVICE_FLAGS, lpDeviceName: win32more.Windows.Win32.Foundation.PWSTR, lpTargetPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
DefineDosDevice = UnicodeAlias('DefineDosDeviceW')
@winfunctype('KERNEL32.dll')
def DeleteFileA(lpFileName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DeleteFileW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
DeleteFile = UnicodeAlias('DeleteFileW')
@winfunctype('KERNEL32.dll')
def DeleteVolumeMountPointW(lpszVolumeMountPoint: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
DeleteVolumeMountPoint = UnicodeAlias('DeleteVolumeMountPointW')
@winfunctype('KERNEL32.dll')
def FileTimeToLocalFileTime(lpFileTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME), lpLocalFileTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FindClose(hFindFile: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FindCloseChangeNotification(hChangeHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FindFirstChangeNotificationA(lpPathName: win32more.Windows.Win32.Foundation.PSTR, bWatchSubtree: win32more.Windows.Win32.Foundation.BOOL, dwNotifyFilter: win32more.Windows.Win32.Storage.FileSystem.FILE_NOTIFY_CHANGE) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def FindFirstChangeNotificationW(lpPathName: win32more.Windows.Win32.Foundation.PWSTR, bWatchSubtree: win32more.Windows.Win32.Foundation.BOOL, dwNotifyFilter: win32more.Windows.Win32.Storage.FileSystem.FILE_NOTIFY_CHANGE) -> win32more.Windows.Win32.Foundation.HANDLE: ...
FindFirstChangeNotification = UnicodeAlias('FindFirstChangeNotificationW')
@winfunctype('KERNEL32.dll')
def FindFirstFileA(lpFileName: win32more.Windows.Win32.Foundation.PSTR, lpFindFileData: POINTER(win32more.Windows.Win32.Storage.FileSystem.WIN32_FIND_DATAA)) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def FindFirstFileW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, lpFindFileData: POINTER(win32more.Windows.Win32.Storage.FileSystem.WIN32_FIND_DATAW)) -> win32more.Windows.Win32.Foundation.HANDLE: ...
FindFirstFile = UnicodeAlias('FindFirstFileW')
@winfunctype('KERNEL32.dll')
def FindFirstFileExA(lpFileName: win32more.Windows.Win32.Foundation.PSTR, fInfoLevelId: win32more.Windows.Win32.Storage.FileSystem.FINDEX_INFO_LEVELS, lpFindFileData: VoidPtr, fSearchOp: win32more.Windows.Win32.Storage.FileSystem.FINDEX_SEARCH_OPS, lpSearchFilter: VoidPtr, dwAdditionalFlags: win32more.Windows.Win32.Storage.FileSystem.FIND_FIRST_EX_FLAGS) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def FindFirstFileExW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, fInfoLevelId: win32more.Windows.Win32.Storage.FileSystem.FINDEX_INFO_LEVELS, lpFindFileData: VoidPtr, fSearchOp: win32more.Windows.Win32.Storage.FileSystem.FINDEX_SEARCH_OPS, lpSearchFilter: VoidPtr, dwAdditionalFlags: win32more.Windows.Win32.Storage.FileSystem.FIND_FIRST_EX_FLAGS) -> win32more.Windows.Win32.Foundation.HANDLE: ...
FindFirstFileEx = UnicodeAlias('FindFirstFileExW')
@winfunctype('KERNEL32.dll')
def FindFirstVolumeW(lpszVolumeName: win32more.Windows.Win32.Foundation.PWSTR, cchBufferLength: UInt32) -> win32more.Windows.Win32.Foundation.HANDLE: ...
FindFirstVolume = UnicodeAlias('FindFirstVolumeW')
@winfunctype('KERNEL32.dll')
def FindNextChangeNotification(hChangeHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FindNextFileA(hFindFile: win32more.Windows.Win32.Foundation.HANDLE, lpFindFileData: POINTER(win32more.Windows.Win32.Storage.FileSystem.WIN32_FIND_DATAA)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FindNextFileW(hFindFile: win32more.Windows.Win32.Foundation.HANDLE, lpFindFileData: POINTER(win32more.Windows.Win32.Storage.FileSystem.WIN32_FIND_DATAW)) -> win32more.Windows.Win32.Foundation.BOOL: ...
FindNextFile = UnicodeAlias('FindNextFileW')
@winfunctype('KERNEL32.dll')
def FindNextVolumeW(hFindVolume: win32more.Windows.Win32.Foundation.HANDLE, lpszVolumeName: win32more.Windows.Win32.Foundation.PWSTR, cchBufferLength: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
FindNextVolume = UnicodeAlias('FindNextVolumeW')
@winfunctype('KERNEL32.dll')
def FindVolumeClose(hFindVolume: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FlushFileBuffers(hFile: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetDiskFreeSpaceA(lpRootPathName: win32more.Windows.Win32.Foundation.PSTR, lpSectorsPerCluster: POINTER(UInt32), lpBytesPerSector: POINTER(UInt32), lpNumberOfFreeClusters: POINTER(UInt32), lpTotalNumberOfClusters: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetDiskFreeSpaceW(lpRootPathName: win32more.Windows.Win32.Foundation.PWSTR, lpSectorsPerCluster: POINTER(UInt32), lpBytesPerSector: POINTER(UInt32), lpNumberOfFreeClusters: POINTER(UInt32), lpTotalNumberOfClusters: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
GetDiskFreeSpace = UnicodeAlias('GetDiskFreeSpaceW')
@winfunctype('KERNEL32.dll')
def GetDiskFreeSpaceExA(lpDirectoryName: win32more.Windows.Win32.Foundation.PSTR, lpFreeBytesAvailableToCaller: POINTER(UInt64), lpTotalNumberOfBytes: POINTER(UInt64), lpTotalNumberOfFreeBytes: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetDiskFreeSpaceExW(lpDirectoryName: win32more.Windows.Win32.Foundation.PWSTR, lpFreeBytesAvailableToCaller: POINTER(UInt64), lpTotalNumberOfBytes: POINTER(UInt64), lpTotalNumberOfFreeBytes: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
GetDiskFreeSpaceEx = UnicodeAlias('GetDiskFreeSpaceExW')
@winfunctype('KERNEL32.dll')
def GetDiskSpaceInformationA(rootPath: win32more.Windows.Win32.Foundation.PSTR, diskSpaceInfo: POINTER(win32more.Windows.Win32.Storage.FileSystem.DISK_SPACE_INFORMATION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def GetDiskSpaceInformationW(rootPath: win32more.Windows.Win32.Foundation.PWSTR, diskSpaceInfo: POINTER(win32more.Windows.Win32.Storage.FileSystem.DISK_SPACE_INFORMATION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
GetDiskSpaceInformation = UnicodeAlias('GetDiskSpaceInformationW')
@winfunctype('KERNEL32.dll')
def GetDriveTypeA(lpRootPathName: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetDriveTypeW(lpRootPathName: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
GetDriveType = UnicodeAlias('GetDriveTypeW')
@winfunctype('KERNEL32.dll')
def GetFileAttributesA(lpFileName: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetFileAttributesW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
GetFileAttributes = UnicodeAlias('GetFileAttributesW')
@winfunctype('KERNEL32.dll')
def GetFileAttributesExA(lpFileName: win32more.Windows.Win32.Foundation.PSTR, fInfoLevelId: win32more.Windows.Win32.Storage.FileSystem.GET_FILEEX_INFO_LEVELS, lpFileInformation: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetFileAttributesExW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, fInfoLevelId: win32more.Windows.Win32.Storage.FileSystem.GET_FILEEX_INFO_LEVELS, lpFileInformation: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
GetFileAttributesEx = UnicodeAlias('GetFileAttributesExW')
@winfunctype('KERNEL32.dll')
def GetFileInformationByHandle(hFile: win32more.Windows.Win32.Foundation.HANDLE, lpFileInformation: POINTER(win32more.Windows.Win32.Storage.FileSystem.BY_HANDLE_FILE_INFORMATION)) -> win32more.Windows.Win32.Foundation.BOOL: ...
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
GetFinalPathNameByHandle = UnicodeAlias('GetFinalPathNameByHandleW')
@winfunctype('KERNEL32.dll')
def GetFileTime(hFile: win32more.Windows.Win32.Foundation.HANDLE, lpCreationTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME), lpLastAccessTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME), lpLastWriteTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetFullPathNameW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, nBufferLength: UInt32, lpBuffer: win32more.Windows.Win32.Foundation.PWSTR, lpFilePart: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> UInt32: ...
GetFullPathName = UnicodeAlias('GetFullPathNameW')
@winfunctype('KERNEL32.dll')
def GetFullPathNameA(lpFileName: win32more.Windows.Win32.Foundation.PSTR, nBufferLength: UInt32, lpBuffer: win32more.Windows.Win32.Foundation.PSTR, lpFilePart: POINTER(win32more.Windows.Win32.Foundation.PSTR)) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetLogicalDrives() -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetLogicalDriveStringsW(nBufferLength: UInt32, lpBuffer: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
GetLogicalDriveStrings = UnicodeAlias('GetLogicalDriveStringsW')
@winfunctype('KERNEL32.dll')
def GetLongPathNameA(lpszShortPath: win32more.Windows.Win32.Foundation.PSTR, lpszLongPath: win32more.Windows.Win32.Foundation.PSTR, cchBuffer: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetLongPathNameW(lpszShortPath: win32more.Windows.Win32.Foundation.PWSTR, lpszLongPath: win32more.Windows.Win32.Foundation.PWSTR, cchBuffer: UInt32) -> UInt32: ...
GetLongPathName = UnicodeAlias('GetLongPathNameW')
@winfunctype('KERNEL32.dll')
def AreShortNamesEnabled(Handle: win32more.Windows.Win32.Foundation.HANDLE, Enabled: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetShortPathNameW(lpszLongPath: win32more.Windows.Win32.Foundation.PWSTR, lpszShortPath: win32more.Windows.Win32.Foundation.PWSTR, cchBuffer: UInt32) -> UInt32: ...
GetShortPathName = UnicodeAlias('GetShortPathNameW')
@winfunctype('KERNEL32.dll')
def GetTempFileNameW(lpPathName: win32more.Windows.Win32.Foundation.PWSTR, lpPrefixString: win32more.Windows.Win32.Foundation.PWSTR, uUnique: UInt32, lpTempFileName: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
GetTempFileName = UnicodeAlias('GetTempFileNameW')
@winfunctype('KERNEL32.dll')
def GetVolumeInformationByHandleW(hFile: win32more.Windows.Win32.Foundation.HANDLE, lpVolumeNameBuffer: win32more.Windows.Win32.Foundation.PWSTR, nVolumeNameSize: UInt32, lpVolumeSerialNumber: POINTER(UInt32), lpMaximumComponentLength: POINTER(UInt32), lpFileSystemFlags: POINTER(UInt32), lpFileSystemNameBuffer: win32more.Windows.Win32.Foundation.PWSTR, nFileSystemNameSize: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetVolumeInformationW(lpRootPathName: win32more.Windows.Win32.Foundation.PWSTR, lpVolumeNameBuffer: win32more.Windows.Win32.Foundation.PWSTR, nVolumeNameSize: UInt32, lpVolumeSerialNumber: POINTER(UInt32), lpMaximumComponentLength: POINTER(UInt32), lpFileSystemFlags: POINTER(UInt32), lpFileSystemNameBuffer: win32more.Windows.Win32.Foundation.PWSTR, nFileSystemNameSize: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
GetVolumeInformation = UnicodeAlias('GetVolumeInformationW')
@winfunctype('KERNEL32.dll')
def GetVolumePathNameW(lpszFileName: win32more.Windows.Win32.Foundation.PWSTR, lpszVolumePathName: win32more.Windows.Win32.Foundation.PWSTR, cchBufferLength: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
GetVolumePathName = UnicodeAlias('GetVolumePathNameW')
@winfunctype('KERNEL32.dll')
def LocalFileTimeToFileTime(lpLocalFileTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME), lpFileTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def LockFile(hFile: win32more.Windows.Win32.Foundation.HANDLE, dwFileOffsetLow: UInt32, dwFileOffsetHigh: UInt32, nNumberOfBytesToLockLow: UInt32, nNumberOfBytesToLockHigh: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def LockFileEx(hFile: win32more.Windows.Win32.Foundation.HANDLE, dwFlags: win32more.Windows.Win32.Storage.FileSystem.LOCK_FILE_FLAGS, dwReserved: UInt32, nNumberOfBytesToLockLow: UInt32, nNumberOfBytesToLockHigh: UInt32, lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def QueryDosDeviceW(lpDeviceName: win32more.Windows.Win32.Foundation.PWSTR, lpTargetPath: win32more.Windows.Win32.Foundation.PWSTR, ucchMax: UInt32) -> UInt32: ...
QueryDosDevice = UnicodeAlias('QueryDosDeviceW')
@winfunctype('KERNEL32.dll')
def ReadFile(hFile: win32more.Windows.Win32.Foundation.HANDLE, lpBuffer: POINTER(Byte), nNumberOfBytesToRead: UInt32, lpNumberOfBytesRead: POINTER(UInt32), lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ReadFileEx(hFile: win32more.Windows.Win32.Foundation.HANDLE, lpBuffer: POINTER(Byte), nNumberOfBytesToRead: UInt32, lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED), lpCompletionRoutine: win32more.Windows.Win32.System.IO.LPOVERLAPPED_COMPLETION_ROUTINE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ReadFileScatter(hFile: win32more.Windows.Win32.Foundation.HANDLE, aSegmentArray: POINTER(win32more.Windows.Win32.Storage.FileSystem.FILE_SEGMENT_ELEMENT), nNumberOfBytesToRead: UInt32, lpReserved: POINTER(UInt32), lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def RemoveDirectoryA(lpPathName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def RemoveDirectoryW(lpPathName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
RemoveDirectory = UnicodeAlias('RemoveDirectoryW')
@winfunctype('KERNEL32.dll')
def SetEndOfFile(hFile: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetFileAttributesA(lpFileName: win32more.Windows.Win32.Foundation.PSTR, dwFileAttributes: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetFileAttributesW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, dwFileAttributes: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES) -> win32more.Windows.Win32.Foundation.BOOL: ...
SetFileAttributes = UnicodeAlias('SetFileAttributesW')
@winfunctype('KERNEL32.dll')
def SetFileInformationByHandle(hFile: win32more.Windows.Win32.Foundation.HANDLE, FileInformationClass: win32more.Windows.Win32.Storage.FileSystem.FILE_INFO_BY_HANDLE_CLASS, lpFileInformation: VoidPtr, dwBufferSize: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetFilePointer(hFile: win32more.Windows.Win32.Foundation.HANDLE, lDistanceToMove: Int32, lpDistanceToMoveHigh: POINTER(Int32), dwMoveMethod: win32more.Windows.Win32.Storage.FileSystem.SET_FILE_POINTER_MOVE_METHOD) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def SetFilePointerEx(hFile: win32more.Windows.Win32.Foundation.HANDLE, liDistanceToMove: Int64, lpNewFilePointer: POINTER(Int64), dwMoveMethod: win32more.Windows.Win32.Storage.FileSystem.SET_FILE_POINTER_MOVE_METHOD) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetFileTime(hFile: win32more.Windows.Win32.Foundation.HANDLE, lpCreationTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME), lpLastAccessTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME), lpLastWriteTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetFileValidData(hFile: win32more.Windows.Win32.Foundation.HANDLE, ValidDataLength: Int64) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def UnlockFile(hFile: win32more.Windows.Win32.Foundation.HANDLE, dwFileOffsetLow: UInt32, dwFileOffsetHigh: UInt32, nNumberOfBytesToUnlockLow: UInt32, nNumberOfBytesToUnlockHigh: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def UnlockFileEx(hFile: win32more.Windows.Win32.Foundation.HANDLE, dwReserved: UInt32, nNumberOfBytesToUnlockLow: UInt32, nNumberOfBytesToUnlockHigh: UInt32, lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WriteFile(hFile: win32more.Windows.Win32.Foundation.HANDLE, lpBuffer: POINTER(Byte), nNumberOfBytesToWrite: UInt32, lpNumberOfBytesWritten: POINTER(UInt32), lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WriteFileEx(hFile: win32more.Windows.Win32.Foundation.HANDLE, lpBuffer: POINTER(Byte), nNumberOfBytesToWrite: UInt32, lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED), lpCompletionRoutine: win32more.Windows.Win32.System.IO.LPOVERLAPPED_COMPLETION_ROUTINE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WriteFileGather(hFile: win32more.Windows.Win32.Foundation.HANDLE, aSegmentArray: POINTER(win32more.Windows.Win32.Storage.FileSystem.FILE_SEGMENT_ELEMENT), nNumberOfBytesToWrite: UInt32, lpReserved: POINTER(UInt32), lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetTempPathW(nBufferLength: UInt32, lpBuffer: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
GetTempPath = UnicodeAlias('GetTempPathW')
@winfunctype('KERNEL32.dll')
def GetVolumeNameForVolumeMountPointW(lpszVolumeMountPoint: win32more.Windows.Win32.Foundation.PWSTR, lpszVolumeName: win32more.Windows.Win32.Foundation.PWSTR, cchBufferLength: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
GetVolumeNameForVolumeMountPoint = UnicodeAlias('GetVolumeNameForVolumeMountPointW')
@winfunctype('KERNEL32.dll')
def GetVolumePathNamesForVolumeNameW(lpszVolumeName: win32more.Windows.Win32.Foundation.PWSTR, lpszVolumePathNames: win32more.Windows.Win32.Foundation.PWSTR, cchBufferLength: UInt32, lpcchReturnLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
GetVolumePathNamesForVolumeName = UnicodeAlias('GetVolumePathNamesForVolumeNameW')
@winfunctype('KERNEL32.dll')
def CreateFile2(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, dwDesiredAccess: UInt32, dwShareMode: win32more.Windows.Win32.Storage.FileSystem.FILE_SHARE_MODE, dwCreationDisposition: win32more.Windows.Win32.Storage.FileSystem.FILE_CREATION_DISPOSITION, pCreateExParams: POINTER(win32more.Windows.Win32.Storage.FileSystem.CREATEFILE2_EXTENDED_PARAMETERS)) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def SetFileIoOverlappedRange(FileHandle: win32more.Windows.Win32.Foundation.HANDLE, OverlappedRangeStart: POINTER(Byte), Length: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetCompressedFileSizeA(lpFileName: win32more.Windows.Win32.Foundation.PSTR, lpFileSizeHigh: POINTER(UInt32)) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetCompressedFileSizeW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, lpFileSizeHigh: POINTER(UInt32)) -> UInt32: ...
GetCompressedFileSize = UnicodeAlias('GetCompressedFileSizeW')
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
GetTempPath2 = UnicodeAlias('GetTempPath2W')
@winfunctype('KERNEL32.dll')
def GetTempPath2A(BufferLength: UInt32, Buffer: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('api-ms-win-core-file-fromapp-l1-1-0.dll')
def CopyFileFromAppW(lpExistingFileName: win32more.Windows.Win32.Foundation.PWSTR, lpNewFileName: win32more.Windows.Win32.Foundation.PWSTR, bFailIfExists: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-file-fromapp-l1-1-0.dll')
def CreateDirectoryFromAppW(lpPathName: win32more.Windows.Win32.Foundation.PWSTR, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-file-fromapp-l1-1-0.dll')
def CreateFileFromAppW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, dwDesiredAccess: UInt32, dwShareMode: UInt32, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), dwCreationDisposition: UInt32, dwFlagsAndAttributes: UInt32, hTemplateFile: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('api-ms-win-core-file-fromapp-l1-1-0.dll')
def CreateFile2FromAppW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, dwDesiredAccess: UInt32, dwShareMode: UInt32, dwCreationDisposition: UInt32, pCreateExParams: POINTER(win32more.Windows.Win32.Storage.FileSystem.CREATEFILE2_EXTENDED_PARAMETERS)) -> win32more.Windows.Win32.Foundation.HANDLE: ...
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
VerFindFile = UnicodeAlias('VerFindFileW')
@winfunctype('VERSION.dll')
def VerInstallFileA(uFlags: win32more.Windows.Win32.Storage.FileSystem.VER_INSTALL_FILE_FLAGS, szSrcFileName: win32more.Windows.Win32.Foundation.PSTR, szDestFileName: win32more.Windows.Win32.Foundation.PSTR, szSrcDir: win32more.Windows.Win32.Foundation.PSTR, szDestDir: win32more.Windows.Win32.Foundation.PSTR, szCurDir: win32more.Windows.Win32.Foundation.PSTR, szTmpFile: win32more.Windows.Win32.Foundation.PSTR, puTmpFileLen: POINTER(UInt32)) -> win32more.Windows.Win32.Storage.FileSystem.VER_INSTALL_FILE_STATUS: ...
@winfunctype('VERSION.dll')
def VerInstallFileW(uFlags: win32more.Windows.Win32.Storage.FileSystem.VER_INSTALL_FILE_FLAGS, szSrcFileName: win32more.Windows.Win32.Foundation.PWSTR, szDestFileName: win32more.Windows.Win32.Foundation.PWSTR, szSrcDir: win32more.Windows.Win32.Foundation.PWSTR, szDestDir: win32more.Windows.Win32.Foundation.PWSTR, szCurDir: win32more.Windows.Win32.Foundation.PWSTR, szTmpFile: win32more.Windows.Win32.Foundation.PWSTR, puTmpFileLen: POINTER(UInt32)) -> win32more.Windows.Win32.Storage.FileSystem.VER_INSTALL_FILE_STATUS: ...
VerInstallFile = UnicodeAlias('VerInstallFileW')
@winfunctype('VERSION.dll')
def GetFileVersionInfoSizeA(lptstrFilename: win32more.Windows.Win32.Foundation.PSTR, lpdwHandle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('VERSION.dll')
def GetFileVersionInfoSizeW(lptstrFilename: win32more.Windows.Win32.Foundation.PWSTR, lpdwHandle: POINTER(UInt32)) -> UInt32: ...
GetFileVersionInfoSize = UnicodeAlias('GetFileVersionInfoSizeW')
@winfunctype('VERSION.dll')
def GetFileVersionInfoA(lptstrFilename: win32more.Windows.Win32.Foundation.PSTR, dwHandle: UInt32, dwLen: UInt32, lpData: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('VERSION.dll')
def GetFileVersionInfoW(lptstrFilename: win32more.Windows.Win32.Foundation.PWSTR, dwHandle: UInt32, dwLen: UInt32, lpData: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
GetFileVersionInfo = UnicodeAlias('GetFileVersionInfoW')
@winfunctype('VERSION.dll')
def GetFileVersionInfoSizeExA(dwFlags: win32more.Windows.Win32.Storage.FileSystem.GET_FILE_VERSION_INFO_FLAGS, lpwstrFilename: win32more.Windows.Win32.Foundation.PSTR, lpdwHandle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('VERSION.dll')
def GetFileVersionInfoSizeExW(dwFlags: win32more.Windows.Win32.Storage.FileSystem.GET_FILE_VERSION_INFO_FLAGS, lpwstrFilename: win32more.Windows.Win32.Foundation.PWSTR, lpdwHandle: POINTER(UInt32)) -> UInt32: ...
GetFileVersionInfoSizeEx = UnicodeAlias('GetFileVersionInfoSizeExW')
@winfunctype('VERSION.dll')
def GetFileVersionInfoExA(dwFlags: win32more.Windows.Win32.Storage.FileSystem.GET_FILE_VERSION_INFO_FLAGS, lpwstrFilename: win32more.Windows.Win32.Foundation.PSTR, dwHandle: UInt32, dwLen: UInt32, lpData: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('VERSION.dll')
def GetFileVersionInfoExW(dwFlags: win32more.Windows.Win32.Storage.FileSystem.GET_FILE_VERSION_INFO_FLAGS, lpwstrFilename: win32more.Windows.Win32.Foundation.PWSTR, dwHandle: UInt32, dwLen: UInt32, lpData: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
GetFileVersionInfoEx = UnicodeAlias('GetFileVersionInfoExW')
@winfunctype('KERNEL32.dll')
def VerLanguageNameA(wLang: UInt32, szLang: win32more.Windows.Win32.Foundation.PSTR, cchLang: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def VerLanguageNameW(wLang: UInt32, szLang: win32more.Windows.Win32.Foundation.PWSTR, cchLang: UInt32) -> UInt32: ...
VerLanguageName = UnicodeAlias('VerLanguageNameW')
@winfunctype('VERSION.dll')
def VerQueryValueA(pBlock: VoidPtr, lpSubBlock: win32more.Windows.Win32.Foundation.PSTR, lplpBuffer: POINTER(VoidPtr), puLen: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('VERSION.dll')
def VerQueryValueW(pBlock: VoidPtr, lpSubBlock: win32more.Windows.Win32.Foundation.PWSTR, lplpBuffer: POINTER(VoidPtr), puLen: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
VerQueryValue = UnicodeAlias('VerQueryValueW')
@winfunctype('clfsw32.dll')
def LsnEqual(plsn1: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN), plsn2: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('clfsw32.dll')
def LsnLess(plsn1: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN), plsn2: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('clfsw32.dll')
def LsnGreater(plsn1: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN), plsn2: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('clfsw32.dll')
def LsnNull(plsn: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('clfsw32.dll')
def LsnContainer(plsn: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN)) -> UInt32: ...
@winfunctype('clfsw32.dll')
def LsnCreate(cidContainer: UInt32, offBlock: UInt32, cRecord: UInt32) -> win32more.Windows.Win32.Storage.FileSystem.CLS_LSN: ...
@winfunctype('clfsw32.dll')
def LsnBlockOffset(plsn: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN)) -> UInt32: ...
@winfunctype('clfsw32.dll')
def LsnRecordSequence(plsn: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN)) -> UInt32: ...
@winfunctype('clfsw32.dll')
def LsnInvalid(plsn: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('clfsw32.dll')
def LsnIncrement(plsn: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN)) -> win32more.Windows.Win32.Storage.FileSystem.CLS_LSN: ...
@winfunctype('clfsw32.dll')
def CreateLogFile(pszLogFileName: win32more.Windows.Win32.Foundation.PWSTR, fDesiredAccess: UInt32, dwShareMode: win32more.Windows.Win32.Storage.FileSystem.FILE_SHARE_MODE, psaLogFile: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), fCreateDisposition: win32more.Windows.Win32.Storage.FileSystem.FILE_CREATION_DISPOSITION, fFlagsAndAttributes: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES) -> win32more.Windows.Win32.Foundation.HANDLE: ...
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
def SetLogArchiveTail(hLog: win32more.Windows.Win32.Foundation.HANDLE, plsnArchiveTail: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN), pReserved: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def SetEndOfLog(hLog: win32more.Windows.Win32.Foundation.HANDLE, plsnEnd: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN), lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def TruncateLog(pvMarshal: VoidPtr, plsnEnd: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN), lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def CreateLogContainerScanContext(hLog: win32more.Windows.Win32.Foundation.HANDLE, cFromContainer: UInt32, cContainers: UInt32, eScanMode: Byte, pcxScan: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_SCAN_CONTEXT), pOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def ScanLogContainers(pcxScan: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_SCAN_CONTEXT), eScanMode: Byte, pReserved: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def AlignReservedLog(pvMarshal: VoidPtr, cReservedRecords: UInt32, rgcbReservation: POINTER(Int64), pcbAlignReservation: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def AllocReservedLog(pvMarshal: VoidPtr, cReservedRecords: UInt32, pcbAdjustment: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def FreeReservedLog(pvMarshal: VoidPtr, cReservedRecords: UInt32, pcbAdjustment: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def GetLogFileInformation(hLog: win32more.Windows.Win32.Foundation.HANDLE, pinfoBuffer: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_INFORMATION), cbBuffer: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def SetLogArchiveMode(hLog: win32more.Windows.Win32.Foundation.HANDLE, eMode: win32more.Windows.Win32.Storage.FileSystem.CLFS_LOG_ARCHIVE_MODE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def ReadLogRestartArea(pvMarshal: VoidPtr, ppvRestartBuffer: POINTER(VoidPtr), pcbRestartBuffer: POINTER(UInt32), plsn: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN), ppvContext: POINTER(VoidPtr), pOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def ReadPreviousLogRestartArea(pvReadContext: VoidPtr, ppvRestartBuffer: POINTER(VoidPtr), pcbRestartBuffer: POINTER(UInt32), plsnRestart: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN), pOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def WriteLogRestartArea(pvMarshal: VoidPtr, pvRestartBuffer: VoidPtr, cbRestartBuffer: UInt32, plsnBase: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN), fFlags: win32more.Windows.Win32.Storage.FileSystem.CLFS_FLAG, pcbWritten: POINTER(UInt32), plsnNext: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN), pOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def GetLogReservationInfo(pvMarshal: VoidPtr, pcbRecordNumber: POINTER(UInt32), pcbUserReservation: POINTER(Int64), pcbCommitReservation: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def AdvanceLogBase(pvMarshal: VoidPtr, plsnBase: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN), fFlags: UInt32, pOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def CloseAndResetLogFile(hLog: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def CreateLogMarshallingArea(hLog: win32more.Windows.Win32.Foundation.HANDLE, pfnAllocBuffer: win32more.Windows.Win32.Storage.FileSystem.CLFS_BLOCK_ALLOCATION, pfnFreeBuffer: win32more.Windows.Win32.Storage.FileSystem.CLFS_BLOCK_DEALLOCATION, pvBlockAllocContext: VoidPtr, cbMarshallingBuffer: UInt32, cMaxWriteBuffers: UInt32, cMaxReadBuffers: UInt32, ppvMarshal: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def DeleteLogMarshallingArea(pvMarshal: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def ReserveAndAppendLog(pvMarshal: VoidPtr, rgWriteEntries: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_WRITE_ENTRY), cWriteEntries: UInt32, plsnUndoNext: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN), plsnPrevious: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN), cReserveRecords: UInt32, rgcbReservation: POINTER(Int64), fFlags: win32more.Windows.Win32.Storage.FileSystem.CLFS_FLAG, plsn: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN), pOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def ReserveAndAppendLogAligned(pvMarshal: VoidPtr, rgWriteEntries: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_WRITE_ENTRY), cWriteEntries: UInt32, cbEntryAlignment: UInt32, plsnUndoNext: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN), plsnPrevious: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN), cReserveRecords: UInt32, rgcbReservation: POINTER(Int64), fFlags: win32more.Windows.Win32.Storage.FileSystem.CLFS_FLAG, plsn: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN), pOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def FlushLogBuffers(pvMarshal: VoidPtr, pOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def FlushLogToLsn(pvMarshalContext: VoidPtr, plsnFlush: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN), plsnLastFlushed: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN), pOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def ReadLogRecord(pvMarshal: VoidPtr, plsnFirst: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN), eContextMode: win32more.Windows.Win32.Storage.FileSystem.CLFS_CONTEXT_MODE, ppvReadBuffer: POINTER(VoidPtr), pcbReadBuffer: POINTER(UInt32), peRecordType: POINTER(Byte), plsnUndoNext: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN), plsnPrevious: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN), ppvReadContext: POINTER(VoidPtr), pOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def ReadNextLogRecord(pvReadContext: VoidPtr, ppvBuffer: POINTER(VoidPtr), pcbBuffer: POINTER(UInt32), peRecordType: POINTER(Byte), plsnUser: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN), plsnUndoNext: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN), plsnPrevious: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN), plsnRecord: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN), pOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def TerminateReadLog(pvCursorContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def PrepareLogArchive(hLog: win32more.Windows.Win32.Foundation.HANDLE, pszBaseLogFileName: win32more.Windows.Win32.Foundation.PWSTR, cLen: UInt32, plsnLow: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN), plsnHigh: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN), pcActualLength: POINTER(UInt32), poffBaseLogFileData: POINTER(UInt64), pcbBaseLogFileLength: POINTER(UInt64), plsnBase: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN), plsnLast: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN), plsnCurrentArchiveTail: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN), ppvArchiveContext: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def ReadLogArchiveMetadata(pvArchiveContext: VoidPtr, cbOffset: UInt32, cbBytesToRead: UInt32, pbReadBuffer: POINTER(Byte), pcbBytesRead: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def GetNextLogArchiveExtent(pvArchiveContext: VoidPtr, rgadExtent: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_ARCHIVE_DESCRIPTOR), cDescriptors: UInt32, pcDescriptorsReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def TerminateLogArchive(pvArchiveContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def ValidateLog(pszLogFileName: win32more.Windows.Win32.Foundation.PWSTR, psaLogFile: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), pinfoBuffer: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_INFORMATION), pcbBuffer: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def GetLogContainerName(hLog: win32more.Windows.Win32.Foundation.HANDLE, cidLogicalContainer: UInt32, pwstrContainerName: win32more.Windows.Win32.Foundation.PWSTR, cLenContainerName: UInt32, pcActualLenContainerName: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def GetLogIoStatistics(hLog: win32more.Windows.Win32.Foundation.HANDLE, pvStatsBuffer: VoidPtr, cbStatsBuffer: UInt32, eStatsClass: win32more.Windows.Win32.Storage.FileSystem.CLFS_IOSTATS_CLASS, pcbStatsWritten: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def RegisterManageableLogClient(hLog: win32more.Windows.Win32.Foundation.HANDLE, pCallbacks: POINTER(win32more.Windows.Win32.Storage.FileSystem.LOG_MANAGEMENT_CALLBACKS)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def DeregisterManageableLogClient(hLog: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def ReadLogNotification(hLog: win32more.Windows.Win32.Foundation.HANDLE, pNotification: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLFS_MGMT_NOTIFICATION), lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def InstallLogPolicy(hLog: win32more.Windows.Win32.Foundation.HANDLE, pPolicy: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLFS_MGMT_POLICY)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def RemoveLogPolicy(hLog: win32more.Windows.Win32.Foundation.HANDLE, ePolicyType: win32more.Windows.Win32.Storage.FileSystem.CLFS_MGMT_POLICY_TYPE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def QueryLogPolicy(hLog: win32more.Windows.Win32.Foundation.HANDLE, ePolicyType: win32more.Windows.Win32.Storage.FileSystem.CLFS_MGMT_POLICY_TYPE, pPolicyBuffer: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLFS_MGMT_POLICY), pcbPolicyBuffer: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def SetLogFileSizeWithPolicy(hLog: win32more.Windows.Win32.Foundation.HANDLE, pDesiredSize: POINTER(UInt64), pResultingSize: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def HandleLogFull(hLog: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def LogTailAdvanceFailure(hLog: win32more.Windows.Win32.Foundation.HANDLE, dwReason: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('clfsw32.dll')
def RegisterForLogWriteNotification(hLog: win32more.Windows.Win32.Foundation.HANDLE, cbThreshold: UInt32, fEnable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def QueryUsersOnEncryptedFile(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, pUsers: POINTER(POINTER(win32more.Windows.Win32.Storage.FileSystem.ENCRYPTION_CERTIFICATE_HASH_LIST))) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def QueryRecoveryAgentsOnEncryptedFile(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, pRecoveryAgents: POINTER(POINTER(win32more.Windows.Win32.Storage.FileSystem.ENCRYPTION_CERTIFICATE_HASH_LIST))) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def RemoveUsersFromEncryptedFile(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, pHashes: POINTER(win32more.Windows.Win32.Storage.FileSystem.ENCRYPTION_CERTIFICATE_HASH_LIST)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def AddUsersToEncryptedFile(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, pEncryptionCertificates: POINTER(win32more.Windows.Win32.Storage.FileSystem.ENCRYPTION_CERTIFICATE_LIST)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def SetUserFileEncryptionKey(pEncryptionCertificate: POINTER(win32more.Windows.Win32.Storage.FileSystem.ENCRYPTION_CERTIFICATE)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def SetUserFileEncryptionKeyEx(pEncryptionCertificate: POINTER(win32more.Windows.Win32.Storage.FileSystem.ENCRYPTION_CERTIFICATE), dwCapabilities: UInt32, dwFlags: UInt32, pvReserved: VoidPtr) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def FreeEncryptionCertificateHashList(pUsers: POINTER(win32more.Windows.Win32.Storage.FileSystem.ENCRYPTION_CERTIFICATE_HASH_LIST)) -> Void: ...
@winfunctype('ADVAPI32.dll')
def EncryptionDisable(DirPath: win32more.Windows.Win32.Foundation.PWSTR, Disable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def DuplicateEncryptionInfoFile(SrcFileName: win32more.Windows.Win32.Foundation.PWSTR, DstFileName: win32more.Windows.Win32.Foundation.PWSTR, dwCreationDistribution: UInt32, dwAttributes: UInt32, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def GetEncryptedFileMetadata(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, pcbMetadata: POINTER(UInt32), ppbMetadata: POINTER(POINTER(Byte))) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def SetEncryptedFileMetadata(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, pbOldMetadata: POINTER(Byte), pbNewMetadata: POINTER(Byte), pOwnerHash: POINTER(win32more.Windows.Win32.Storage.FileSystem.ENCRYPTION_CERTIFICATE_HASH), dwOperation: UInt32, pCertificatesAdded: POINTER(win32more.Windows.Win32.Storage.FileSystem.ENCRYPTION_CERTIFICATE_HASH_LIST)) -> UInt32: ...
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
GetExpandedName = UnicodeAlias('GetExpandedNameW')
@winfunctype('KERNEL32.dll')
def LZOpenFileA(lpFileName: win32more.Windows.Win32.Foundation.PSTR, lpReOpenBuf: POINTER(win32more.Windows.Win32.Storage.FileSystem.OFSTRUCT), wStyle: win32more.Windows.Win32.Storage.FileSystem.LZOPENFILE_STYLE) -> Int32: ...
@winfunctype('KERNEL32.dll')
def LZOpenFileW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, lpReOpenBuf: POINTER(win32more.Windows.Win32.Storage.FileSystem.OFSTRUCT), wStyle: win32more.Windows.Win32.Storage.FileSystem.LZOPENFILE_STYLE) -> Int32: ...
LZOpenFile = UnicodeAlias('LZOpenFileW')
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
def TxfLogCreateFileReadContext(LogPath: win32more.Windows.Win32.Foundation.PWSTR, BeginningLsn: win32more.Windows.Win32.Storage.FileSystem.CLS_LSN, EndingLsn: win32more.Windows.Win32.Storage.FileSystem.CLS_LSN, TxfFileId: POINTER(win32more.Windows.Win32.Storage.FileSystem.TXF_ID), TxfLogContext: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('txfw32.dll')
def TxfLogCreateRangeReadContext(LogPath: win32more.Windows.Win32.Foundation.PWSTR, BeginningLsn: win32more.Windows.Win32.Storage.FileSystem.CLS_LSN, EndingLsn: win32more.Windows.Win32.Storage.FileSystem.CLS_LSN, BeginningVirtualClock: POINTER(Int64), EndingVirtualClock: POINTER(Int64), RecordTypeMask: UInt32, TxfLogContext: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('txfw32.dll')
def TxfLogDestroyReadContext(TxfLogContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('txfw32.dll')
def TxfLogReadRecords(TxfLogContext: VoidPtr, BufferLength: UInt32, Buffer: VoidPtr, BytesUsed: POINTER(UInt32), RecordCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('txfw32.dll')
def TxfReadMetadataInfo(FileHandle: win32more.Windows.Win32.Foundation.HANDLE, TxfFileId: POINTER(win32more.Windows.Win32.Storage.FileSystem.TXF_ID), LastLsn: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_LSN), TransactionState: POINTER(UInt32), LockingTransaction: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('txfw32.dll')
def TxfLogRecordGetFileName(RecordBuffer: VoidPtr, RecordBufferLengthInBytes: UInt32, NameBuffer: win32more.Windows.Win32.Foundation.PWSTR, NameBufferLengthInBytes: POINTER(UInt32), TxfId: POINTER(win32more.Windows.Win32.Storage.FileSystem.TXF_ID)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('txfw32.dll')
def TxfLogRecordGetGenericType(RecordBuffer: VoidPtr, RecordBufferLengthInBytes: UInt32, GenericType: POINTER(UInt32), VirtualClock: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('txfw32.dll')
def TxfSetThreadMiniVersionForCreate(MiniVersion: UInt16) -> Void: ...
@winfunctype('txfw32.dll')
def TxfGetThreadMiniVersionForCreate(MiniVersion: POINTER(UInt16)) -> Void: ...
@winfunctype('ktmw32.dll')
def CreateTransaction(lpTransactionAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), UOW: POINTER(Guid), CreateOptions: UInt32, IsolationLevel: UInt32, IsolationFlags: UInt32, Timeout: UInt32, Description: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
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
def CreateTransactionManager(lpTransactionAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), LogFileName: win32more.Windows.Win32.Foundation.PWSTR, CreateOptions: UInt32, CommitStrength: UInt32) -> win32more.Windows.Win32.Foundation.HANDLE: ...
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
def CreateResourceManager(lpResourceManagerAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), ResourceManagerId: POINTER(Guid), CreateOptions: UInt32, TmHandle: win32more.Windows.Win32.Foundation.HANDLE, Description: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('ktmw32.dll')
def OpenResourceManager(dwDesiredAccess: UInt32, TmHandle: win32more.Windows.Win32.Foundation.HANDLE, ResourceManagerId: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('ktmw32.dll')
def RecoverResourceManager(ResourceManagerHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def GetNotificationResourceManager(ResourceManagerHandle: win32more.Windows.Win32.Foundation.HANDLE, TransactionNotification: POINTER(win32more.Windows.Win32.Storage.FileSystem.TRANSACTION_NOTIFICATION), NotificationLength: UInt32, dwMilliseconds: UInt32, ReturnLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def GetNotificationResourceManagerAsync(ResourceManagerHandle: win32more.Windows.Win32.Foundation.HANDLE, TransactionNotification: POINTER(win32more.Windows.Win32.Storage.FileSystem.TRANSACTION_NOTIFICATION), TransactionNotificationLength: UInt32, ReturnLength: POINTER(UInt32), lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def SetResourceManagerCompletionPort(ResourceManagerHandle: win32more.Windows.Win32.Foundation.HANDLE, IoCompletionPortHandle: win32more.Windows.Win32.Foundation.HANDLE, CompletionKey: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ktmw32.dll')
def CreateEnlistment(lpEnlistmentAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), ResourceManagerHandle: win32more.Windows.Win32.Foundation.HANDLE, TransactionHandle: win32more.Windows.Win32.Foundation.HANDLE, NotificationMask: UInt32, CreateOptions: UInt32, EnlistmentKey: VoidPtr) -> win32more.Windows.Win32.Foundation.HANDLE: ...
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
def QueryIoRingCapabilities(capabilities: POINTER(win32more.Windows.Win32.Storage.FileSystem.IORING_CAPABILITIES)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-ioring-l1-1-0.dll')
def IsIoRingOpSupported(ioRing: win32more.Windows.Win32.Storage.FileSystem.HIORING, op: win32more.Windows.Win32.Storage.FileSystem.IORING_OP_CODE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-ioring-l1-1-0.dll')
def CreateIoRing(ioringVersion: win32more.Windows.Win32.Storage.FileSystem.IORING_VERSION, flags: win32more.Windows.Win32.Storage.FileSystem.IORING_CREATE_FLAGS, submissionQueueSize: UInt32, completionQueueSize: UInt32, h: POINTER(win32more.Windows.Win32.Storage.FileSystem.HIORING)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-ioring-l1-1-0.dll')
def GetIoRingInfo(ioRing: win32more.Windows.Win32.Storage.FileSystem.HIORING, info: POINTER(win32more.Windows.Win32.Storage.FileSystem.IORING_INFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-ioring-l1-1-0.dll')
def SubmitIoRing(ioRing: win32more.Windows.Win32.Storage.FileSystem.HIORING, waitOperations: UInt32, milliseconds: UInt32, submittedEntries: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-ioring-l1-1-0.dll')
def CloseIoRing(ioRing: win32more.Windows.Win32.Storage.FileSystem.HIORING) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-ioring-l1-1-0.dll')
def PopIoRingCompletion(ioRing: win32more.Windows.Win32.Storage.FileSystem.HIORING, cqe: POINTER(win32more.Windows.Win32.Storage.FileSystem.IORING_CQE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-ioring-l1-1-0.dll')
def SetIoRingCompletionEvent(ioRing: win32more.Windows.Win32.Storage.FileSystem.HIORING, hEvent: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-ioring-l1-1-0.dll')
def BuildIoRingCancelRequest(ioRing: win32more.Windows.Win32.Storage.FileSystem.HIORING, file: win32more.Windows.Win32.Storage.FileSystem.IORING_HANDLE_REF, opToCancel: UIntPtr, userData: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-ioring-l1-1-0.dll')
def BuildIoRingReadFile(ioRing: win32more.Windows.Win32.Storage.FileSystem.HIORING, fileRef: win32more.Windows.Win32.Storage.FileSystem.IORING_HANDLE_REF, dataRef: win32more.Windows.Win32.Storage.FileSystem.IORING_BUFFER_REF, numberOfBytesToRead: UInt32, fileOffset: UInt64, userData: UIntPtr, sqeFlags: win32more.Windows.Win32.Storage.FileSystem.IORING_SQE_FLAGS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-ioring-l1-1-0.dll')
def BuildIoRingRegisterFileHandles(ioRing: win32more.Windows.Win32.Storage.FileSystem.HIORING, count: UInt32, handles: POINTER(win32more.Windows.Win32.Foundation.HANDLE), userData: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-ioring-l1-1-0.dll')
def BuildIoRingRegisterBuffers(ioRing: win32more.Windows.Win32.Storage.FileSystem.HIORING, count: UInt32, buffers: POINTER(win32more.Windows.Win32.Storage.FileSystem.IORING_BUFFER_INFO), userData: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
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
GetBinaryType = UnicodeAlias('GetBinaryTypeW')
@winfunctype('KERNEL32.dll')
def GetShortPathNameA(lpszLongPath: win32more.Windows.Win32.Foundation.PSTR, lpszShortPath: win32more.Windows.Win32.Foundation.PSTR, cchBuffer: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetLongPathNameTransactedA(lpszShortPath: win32more.Windows.Win32.Foundation.PSTR, lpszLongPath: win32more.Windows.Win32.Foundation.PSTR, cchBuffer: UInt32, hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetLongPathNameTransactedW(lpszShortPath: win32more.Windows.Win32.Foundation.PWSTR, lpszLongPath: win32more.Windows.Win32.Foundation.PWSTR, cchBuffer: UInt32, hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
GetLongPathNameTransacted = UnicodeAlias('GetLongPathNameTransactedW')
@winfunctype('KERNEL32.dll')
def SetFileCompletionNotificationModes(FileHandle: win32more.Windows.Win32.Foundation.HANDLE, Flags: Byte) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetFileShortNameA(hFile: win32more.Windows.Win32.Foundation.HANDLE, lpShortName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetFileShortNameW(hFile: win32more.Windows.Win32.Foundation.HANDLE, lpShortName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
SetFileShortName = UnicodeAlias('SetFileShortNameW')
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
EncryptFile = UnicodeAlias('EncryptFileW')
@winfunctype('ADVAPI32.dll')
def DecryptFileA(lpFileName: win32more.Windows.Win32.Foundation.PSTR, dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def DecryptFileW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
DecryptFile = UnicodeAlias('DecryptFileW')
@winfunctype('ADVAPI32.dll')
def FileEncryptionStatusA(lpFileName: win32more.Windows.Win32.Foundation.PSTR, lpStatus: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def FileEncryptionStatusW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, lpStatus: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
FileEncryptionStatus = UnicodeAlias('FileEncryptionStatusW')
@winfunctype('ADVAPI32.dll')
def OpenEncryptedFileRawA(lpFileName: win32more.Windows.Win32.Foundation.PSTR, ulFlags: UInt32, pvContext: POINTER(VoidPtr)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def OpenEncryptedFileRawW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, ulFlags: UInt32, pvContext: POINTER(VoidPtr)) -> UInt32: ...
OpenEncryptedFileRaw = UnicodeAlias('OpenEncryptedFileRawW')
@winfunctype('ADVAPI32.dll')
def ReadEncryptedFileRaw(pfExportCallback: win32more.Windows.Win32.Storage.FileSystem.PFE_EXPORT_FUNC, pvCallbackContext: VoidPtr, pvContext: VoidPtr) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def WriteEncryptedFileRaw(pfImportCallback: win32more.Windows.Win32.Storage.FileSystem.PFE_IMPORT_FUNC, pvCallbackContext: VoidPtr, pvContext: VoidPtr) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def CloseEncryptedFileRaw(pvContext: VoidPtr) -> Void: ...
@winfunctype('KERNEL32.dll')
def OpenFile(lpFileName: win32more.Windows.Win32.Foundation.PSTR, lpReOpenBuff: POINTER(win32more.Windows.Win32.Storage.FileSystem.OFSTRUCT), uStyle: UInt32) -> Int32: ...
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
def CreateDirectoryExA(lpTemplateDirectory: win32more.Windows.Win32.Foundation.PSTR, lpNewDirectory: win32more.Windows.Win32.Foundation.PSTR, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateDirectoryExW(lpTemplateDirectory: win32more.Windows.Win32.Foundation.PWSTR, lpNewDirectory: win32more.Windows.Win32.Foundation.PWSTR, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES)) -> win32more.Windows.Win32.Foundation.BOOL: ...
CreateDirectoryEx = UnicodeAlias('CreateDirectoryExW')
@winfunctype('KERNEL32.dll')
def CreateDirectoryTransactedA(lpTemplateDirectory: win32more.Windows.Win32.Foundation.PSTR, lpNewDirectory: win32more.Windows.Win32.Foundation.PSTR, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateDirectoryTransactedW(lpTemplateDirectory: win32more.Windows.Win32.Foundation.PWSTR, lpNewDirectory: win32more.Windows.Win32.Foundation.PWSTR, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
CreateDirectoryTransacted = UnicodeAlias('CreateDirectoryTransactedW')
@winfunctype('KERNEL32.dll')
def RemoveDirectoryTransactedA(lpPathName: win32more.Windows.Win32.Foundation.PSTR, hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def RemoveDirectoryTransactedW(lpPathName: win32more.Windows.Win32.Foundation.PWSTR, hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
RemoveDirectoryTransacted = UnicodeAlias('RemoveDirectoryTransactedW')
@winfunctype('KERNEL32.dll')
def GetFullPathNameTransactedA(lpFileName: win32more.Windows.Win32.Foundation.PSTR, nBufferLength: UInt32, lpBuffer: win32more.Windows.Win32.Foundation.PSTR, lpFilePart: POINTER(win32more.Windows.Win32.Foundation.PSTR), hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetFullPathNameTransactedW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, nBufferLength: UInt32, lpBuffer: win32more.Windows.Win32.Foundation.PWSTR, lpFilePart: POINTER(win32more.Windows.Win32.Foundation.PWSTR), hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
GetFullPathNameTransacted = UnicodeAlias('GetFullPathNameTransactedW')
@winfunctype('KERNEL32.dll')
def DefineDosDeviceA(dwFlags: win32more.Windows.Win32.Storage.FileSystem.DEFINE_DOS_DEVICE_FLAGS, lpDeviceName: win32more.Windows.Win32.Foundation.PSTR, lpTargetPath: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def QueryDosDeviceA(lpDeviceName: win32more.Windows.Win32.Foundation.PSTR, lpTargetPath: win32more.Windows.Win32.Foundation.PSTR, ucchMax: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def CreateFileTransactedA(lpFileName: win32more.Windows.Win32.Foundation.PSTR, dwDesiredAccess: UInt32, dwShareMode: win32more.Windows.Win32.Storage.FileSystem.FILE_SHARE_MODE, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), dwCreationDisposition: win32more.Windows.Win32.Storage.FileSystem.FILE_CREATION_DISPOSITION, dwFlagsAndAttributes: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES, hTemplateFile: win32more.Windows.Win32.Foundation.HANDLE, hTransaction: win32more.Windows.Win32.Foundation.HANDLE, pusMiniVersion: POINTER(win32more.Windows.Win32.Storage.FileSystem.TXFS_MINIVERSION), lpExtendedParameter: VoidPtr) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def CreateFileTransactedW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, dwDesiredAccess: UInt32, dwShareMode: win32more.Windows.Win32.Storage.FileSystem.FILE_SHARE_MODE, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), dwCreationDisposition: win32more.Windows.Win32.Storage.FileSystem.FILE_CREATION_DISPOSITION, dwFlagsAndAttributes: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES, hTemplateFile: win32more.Windows.Win32.Foundation.HANDLE, hTransaction: win32more.Windows.Win32.Foundation.HANDLE, pusMiniVersion: POINTER(win32more.Windows.Win32.Storage.FileSystem.TXFS_MINIVERSION), lpExtendedParameter: VoidPtr) -> win32more.Windows.Win32.Foundation.HANDLE: ...
CreateFileTransacted = UnicodeAlias('CreateFileTransactedW')
@winfunctype('KERNEL32.dll')
def ReOpenFile(hOriginalFile: win32more.Windows.Win32.Foundation.HANDLE, dwDesiredAccess: UInt32, dwShareMode: win32more.Windows.Win32.Storage.FileSystem.FILE_SHARE_MODE, dwFlagsAndAttributes: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def SetFileAttributesTransactedA(lpFileName: win32more.Windows.Win32.Foundation.PSTR, dwFileAttributes: UInt32, hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetFileAttributesTransactedW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, dwFileAttributes: UInt32, hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
SetFileAttributesTransacted = UnicodeAlias('SetFileAttributesTransactedW')
@winfunctype('KERNEL32.dll')
def GetFileAttributesTransactedA(lpFileName: win32more.Windows.Win32.Foundation.PSTR, fInfoLevelId: win32more.Windows.Win32.Storage.FileSystem.GET_FILEEX_INFO_LEVELS, lpFileInformation: VoidPtr, hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetFileAttributesTransactedW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, fInfoLevelId: win32more.Windows.Win32.Storage.FileSystem.GET_FILEEX_INFO_LEVELS, lpFileInformation: VoidPtr, hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
GetFileAttributesTransacted = UnicodeAlias('GetFileAttributesTransactedW')
@winfunctype('KERNEL32.dll')
def GetCompressedFileSizeTransactedA(lpFileName: win32more.Windows.Win32.Foundation.PSTR, lpFileSizeHigh: POINTER(UInt32), hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetCompressedFileSizeTransactedW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, lpFileSizeHigh: POINTER(UInt32), hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
GetCompressedFileSizeTransacted = UnicodeAlias('GetCompressedFileSizeTransactedW')
@winfunctype('KERNEL32.dll')
def DeleteFileTransactedA(lpFileName: win32more.Windows.Win32.Foundation.PSTR, hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DeleteFileTransactedW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
DeleteFileTransacted = UnicodeAlias('DeleteFileTransactedW')
@winfunctype('KERNEL32.dll')
def CheckNameLegalDOS8Dot3A(lpName: win32more.Windows.Win32.Foundation.PSTR, lpOemName: win32more.Windows.Win32.Foundation.PSTR, OemNameSize: UInt32, pbNameContainsSpaces: POINTER(win32more.Windows.Win32.Foundation.BOOL), pbNameLegal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CheckNameLegalDOS8Dot3W(lpName: win32more.Windows.Win32.Foundation.PWSTR, lpOemName: win32more.Windows.Win32.Foundation.PSTR, OemNameSize: UInt32, pbNameContainsSpaces: POINTER(win32more.Windows.Win32.Foundation.BOOL), pbNameLegal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
CheckNameLegalDOS8Dot3 = UnicodeAlias('CheckNameLegalDOS8Dot3W')
@winfunctype('KERNEL32.dll')
def FindFirstFileTransactedA(lpFileName: win32more.Windows.Win32.Foundation.PSTR, fInfoLevelId: win32more.Windows.Win32.Storage.FileSystem.FINDEX_INFO_LEVELS, lpFindFileData: VoidPtr, fSearchOp: win32more.Windows.Win32.Storage.FileSystem.FINDEX_SEARCH_OPS, lpSearchFilter: VoidPtr, dwAdditionalFlags: UInt32, hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def FindFirstFileTransactedW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, fInfoLevelId: win32more.Windows.Win32.Storage.FileSystem.FINDEX_INFO_LEVELS, lpFindFileData: VoidPtr, fSearchOp: win32more.Windows.Win32.Storage.FileSystem.FINDEX_SEARCH_OPS, lpSearchFilter: VoidPtr, dwAdditionalFlags: UInt32, hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HANDLE: ...
FindFirstFileTransacted = UnicodeAlias('FindFirstFileTransactedW')
@winfunctype('KERNEL32.dll')
def CopyFileA(lpExistingFileName: win32more.Windows.Win32.Foundation.PSTR, lpNewFileName: win32more.Windows.Win32.Foundation.PSTR, bFailIfExists: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CopyFileW(lpExistingFileName: win32more.Windows.Win32.Foundation.PWSTR, lpNewFileName: win32more.Windows.Win32.Foundation.PWSTR, bFailIfExists: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
CopyFile = UnicodeAlias('CopyFileW')
@winfunctype('KERNEL32.dll')
def CopyFileExA(lpExistingFileName: win32more.Windows.Win32.Foundation.PSTR, lpNewFileName: win32more.Windows.Win32.Foundation.PSTR, lpProgressRoutine: win32more.Windows.Win32.Storage.FileSystem.LPPROGRESS_ROUTINE, lpData: VoidPtr, pbCancel: POINTER(win32more.Windows.Win32.Foundation.BOOL), dwCopyFlags: win32more.Windows.Win32.Storage.FileSystem.COPYFILE_FLAGS) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CopyFileExW(lpExistingFileName: win32more.Windows.Win32.Foundation.PWSTR, lpNewFileName: win32more.Windows.Win32.Foundation.PWSTR, lpProgressRoutine: win32more.Windows.Win32.Storage.FileSystem.LPPROGRESS_ROUTINE, lpData: VoidPtr, pbCancel: POINTER(win32more.Windows.Win32.Foundation.BOOL), dwCopyFlags: win32more.Windows.Win32.Storage.FileSystem.COPYFILE_FLAGS) -> win32more.Windows.Win32.Foundation.BOOL: ...
CopyFileEx = UnicodeAlias('CopyFileExW')
@winfunctype('KERNEL32.dll')
def CopyFileTransactedA(lpExistingFileName: win32more.Windows.Win32.Foundation.PSTR, lpNewFileName: win32more.Windows.Win32.Foundation.PSTR, lpProgressRoutine: win32more.Windows.Win32.Storage.FileSystem.LPPROGRESS_ROUTINE, lpData: VoidPtr, pbCancel: POINTER(win32more.Windows.Win32.Foundation.BOOL), dwCopyFlags: UInt32, hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CopyFileTransactedW(lpExistingFileName: win32more.Windows.Win32.Foundation.PWSTR, lpNewFileName: win32more.Windows.Win32.Foundation.PWSTR, lpProgressRoutine: win32more.Windows.Win32.Storage.FileSystem.LPPROGRESS_ROUTINE, lpData: VoidPtr, pbCancel: POINTER(win32more.Windows.Win32.Foundation.BOOL), dwCopyFlags: UInt32, hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
CopyFileTransacted = UnicodeAlias('CopyFileTransactedW')
@winfunctype('KERNEL32.dll')
def CopyFile2(pwszExistingFileName: win32more.Windows.Win32.Foundation.PWSTR, pwszNewFileName: win32more.Windows.Win32.Foundation.PWSTR, pExtendedParameters: POINTER(win32more.Windows.Win32.Storage.FileSystem.COPYFILE2_EXTENDED_PARAMETERS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def MoveFileA(lpExistingFileName: win32more.Windows.Win32.Foundation.PSTR, lpNewFileName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def MoveFileW(lpExistingFileName: win32more.Windows.Win32.Foundation.PWSTR, lpNewFileName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
MoveFile = UnicodeAlias('MoveFileW')
@winfunctype('KERNEL32.dll')
def MoveFileExA(lpExistingFileName: win32more.Windows.Win32.Foundation.PSTR, lpNewFileName: win32more.Windows.Win32.Foundation.PSTR, dwFlags: win32more.Windows.Win32.Storage.FileSystem.MOVE_FILE_FLAGS) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def MoveFileExW(lpExistingFileName: win32more.Windows.Win32.Foundation.PWSTR, lpNewFileName: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: win32more.Windows.Win32.Storage.FileSystem.MOVE_FILE_FLAGS) -> win32more.Windows.Win32.Foundation.BOOL: ...
MoveFileEx = UnicodeAlias('MoveFileExW')
@winfunctype('KERNEL32.dll')
def MoveFileWithProgressA(lpExistingFileName: win32more.Windows.Win32.Foundation.PSTR, lpNewFileName: win32more.Windows.Win32.Foundation.PSTR, lpProgressRoutine: win32more.Windows.Win32.Storage.FileSystem.LPPROGRESS_ROUTINE, lpData: VoidPtr, dwFlags: win32more.Windows.Win32.Storage.FileSystem.MOVE_FILE_FLAGS) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def MoveFileWithProgressW(lpExistingFileName: win32more.Windows.Win32.Foundation.PWSTR, lpNewFileName: win32more.Windows.Win32.Foundation.PWSTR, lpProgressRoutine: win32more.Windows.Win32.Storage.FileSystem.LPPROGRESS_ROUTINE, lpData: VoidPtr, dwFlags: win32more.Windows.Win32.Storage.FileSystem.MOVE_FILE_FLAGS) -> win32more.Windows.Win32.Foundation.BOOL: ...
MoveFileWithProgress = UnicodeAlias('MoveFileWithProgressW')
@winfunctype('KERNEL32.dll')
def MoveFileTransactedA(lpExistingFileName: win32more.Windows.Win32.Foundation.PSTR, lpNewFileName: win32more.Windows.Win32.Foundation.PSTR, lpProgressRoutine: win32more.Windows.Win32.Storage.FileSystem.LPPROGRESS_ROUTINE, lpData: VoidPtr, dwFlags: win32more.Windows.Win32.Storage.FileSystem.MOVE_FILE_FLAGS, hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def MoveFileTransactedW(lpExistingFileName: win32more.Windows.Win32.Foundation.PWSTR, lpNewFileName: win32more.Windows.Win32.Foundation.PWSTR, lpProgressRoutine: win32more.Windows.Win32.Storage.FileSystem.LPPROGRESS_ROUTINE, lpData: VoidPtr, dwFlags: win32more.Windows.Win32.Storage.FileSystem.MOVE_FILE_FLAGS, hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
MoveFileTransacted = UnicodeAlias('MoveFileTransactedW')
@winfunctype('KERNEL32.dll')
def ReplaceFileA(lpReplacedFileName: win32more.Windows.Win32.Foundation.PSTR, lpReplacementFileName: win32more.Windows.Win32.Foundation.PSTR, lpBackupFileName: win32more.Windows.Win32.Foundation.PSTR, dwReplaceFlags: win32more.Windows.Win32.Storage.FileSystem.REPLACE_FILE_FLAGS, lpExclude: VoidPtr, lpReserved: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ReplaceFileW(lpReplacedFileName: win32more.Windows.Win32.Foundation.PWSTR, lpReplacementFileName: win32more.Windows.Win32.Foundation.PWSTR, lpBackupFileName: win32more.Windows.Win32.Foundation.PWSTR, dwReplaceFlags: win32more.Windows.Win32.Storage.FileSystem.REPLACE_FILE_FLAGS, lpExclude: VoidPtr, lpReserved: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
ReplaceFile = UnicodeAlias('ReplaceFileW')
@winfunctype('KERNEL32.dll')
def CreateHardLinkA(lpFileName: win32more.Windows.Win32.Foundation.PSTR, lpExistingFileName: win32more.Windows.Win32.Foundation.PSTR, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateHardLinkW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, lpExistingFileName: win32more.Windows.Win32.Foundation.PWSTR, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES)) -> win32more.Windows.Win32.Foundation.BOOL: ...
CreateHardLink = UnicodeAlias('CreateHardLinkW')
@winfunctype('KERNEL32.dll')
def CreateHardLinkTransactedA(lpFileName: win32more.Windows.Win32.Foundation.PSTR, lpExistingFileName: win32more.Windows.Win32.Foundation.PSTR, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateHardLinkTransactedW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, lpExistingFileName: win32more.Windows.Win32.Foundation.PWSTR, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
CreateHardLinkTransacted = UnicodeAlias('CreateHardLinkTransactedW')
@winfunctype('KERNEL32.dll')
def FindFirstStreamTransactedW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, InfoLevel: win32more.Windows.Win32.Storage.FileSystem.STREAM_INFO_LEVELS, lpFindStreamData: VoidPtr, dwFlags: UInt32, hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def FindFirstFileNameTransactedW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, StringLength: POINTER(UInt32), LinkName: win32more.Windows.Win32.Foundation.PWSTR, hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def SetVolumeLabelA(lpRootPathName: win32more.Windows.Win32.Foundation.PSTR, lpVolumeName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetVolumeLabelW(lpRootPathName: win32more.Windows.Win32.Foundation.PWSTR, lpVolumeName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
SetVolumeLabel = UnicodeAlias('SetVolumeLabelW')
@winfunctype('KERNEL32.dll')
def SetFileBandwidthReservation(hFile: win32more.Windows.Win32.Foundation.HANDLE, nPeriodMilliseconds: UInt32, nBytesPerPeriod: UInt32, bDiscardable: win32more.Windows.Win32.Foundation.BOOL, lpTransferSize: POINTER(UInt32), lpNumOutstandingRequests: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetFileBandwidthReservation(hFile: win32more.Windows.Win32.Foundation.HANDLE, lpPeriodMilliseconds: POINTER(UInt32), lpBytesPerPeriod: POINTER(UInt32), pDiscardable: POINTER(win32more.Windows.Win32.Foundation.BOOL), lpTransferSize: POINTER(UInt32), lpNumOutstandingRequests: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ReadDirectoryChangesW(hDirectory: win32more.Windows.Win32.Foundation.HANDLE, lpBuffer: VoidPtr, nBufferLength: UInt32, bWatchSubtree: win32more.Windows.Win32.Foundation.BOOL, dwNotifyFilter: win32more.Windows.Win32.Storage.FileSystem.FILE_NOTIFY_CHANGE, lpBytesReturned: POINTER(UInt32), lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED), lpCompletionRoutine: win32more.Windows.Win32.System.IO.LPOVERLAPPED_COMPLETION_ROUTINE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ReadDirectoryChangesExW(hDirectory: win32more.Windows.Win32.Foundation.HANDLE, lpBuffer: VoidPtr, nBufferLength: UInt32, bWatchSubtree: win32more.Windows.Win32.Foundation.BOOL, dwNotifyFilter: win32more.Windows.Win32.Storage.FileSystem.FILE_NOTIFY_CHANGE, lpBytesReturned: POINTER(UInt32), lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED), lpCompletionRoutine: win32more.Windows.Win32.System.IO.LPOVERLAPPED_COMPLETION_ROUTINE, ReadDirectoryNotifyInformationClass: win32more.Windows.Win32.Storage.FileSystem.READ_DIRECTORY_NOTIFY_INFORMATION_CLASS) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FindFirstVolumeA(lpszVolumeName: win32more.Windows.Win32.Foundation.PSTR, cchBufferLength: UInt32) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def FindNextVolumeA(hFindVolume: win32more.Windows.Win32.Foundation.HANDLE, lpszVolumeName: win32more.Windows.Win32.Foundation.PSTR, cchBufferLength: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FindFirstVolumeMountPointA(lpszRootPathName: win32more.Windows.Win32.Foundation.PSTR, lpszVolumeMountPoint: win32more.Windows.Win32.Foundation.PSTR, cchBufferLength: UInt32) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def FindFirstVolumeMountPointW(lpszRootPathName: win32more.Windows.Win32.Foundation.PWSTR, lpszVolumeMountPoint: win32more.Windows.Win32.Foundation.PWSTR, cchBufferLength: UInt32) -> win32more.Windows.Win32.Foundation.HANDLE: ...
FindFirstVolumeMountPoint = UnicodeAlias('FindFirstVolumeMountPointW')
@winfunctype('KERNEL32.dll')
def FindNextVolumeMountPointA(hFindVolumeMountPoint: win32more.Windows.Win32.Foundation.HANDLE, lpszVolumeMountPoint: win32more.Windows.Win32.Foundation.PSTR, cchBufferLength: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FindNextVolumeMountPointW(hFindVolumeMountPoint: win32more.Windows.Win32.Foundation.HANDLE, lpszVolumeMountPoint: win32more.Windows.Win32.Foundation.PWSTR, cchBufferLength: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
FindNextVolumeMountPoint = UnicodeAlias('FindNextVolumeMountPointW')
@winfunctype('KERNEL32.dll')
def FindVolumeMountPointClose(hFindVolumeMountPoint: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetVolumeMountPointA(lpszVolumeMountPoint: win32more.Windows.Win32.Foundation.PSTR, lpszVolumeName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetVolumeMountPointW(lpszVolumeMountPoint: win32more.Windows.Win32.Foundation.PWSTR, lpszVolumeName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
SetVolumeMountPoint = UnicodeAlias('SetVolumeMountPointW')
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
def OpenFileById(hVolumeHint: win32more.Windows.Win32.Foundation.HANDLE, lpFileId: POINTER(win32more.Windows.Win32.Storage.FileSystem.FILE_ID_DESCRIPTOR), dwDesiredAccess: UInt32, dwShareMode: win32more.Windows.Win32.Storage.FileSystem.FILE_SHARE_MODE, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), dwFlagsAndAttributes: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def CreateSymbolicLinkA(lpSymlinkFileName: win32more.Windows.Win32.Foundation.PSTR, lpTargetFileName: win32more.Windows.Win32.Foundation.PSTR, dwFlags: win32more.Windows.Win32.Storage.FileSystem.SYMBOLIC_LINK_FLAGS) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('KERNEL32.dll')
def CreateSymbolicLinkW(lpSymlinkFileName: win32more.Windows.Win32.Foundation.PWSTR, lpTargetFileName: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: win32more.Windows.Win32.Storage.FileSystem.SYMBOLIC_LINK_FLAGS) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
CreateSymbolicLink = UnicodeAlias('CreateSymbolicLinkW')
@winfunctype('KERNEL32.dll')
def CreateSymbolicLinkTransactedA(lpSymlinkFileName: win32more.Windows.Win32.Foundation.PSTR, lpTargetFileName: win32more.Windows.Win32.Foundation.PSTR, dwFlags: win32more.Windows.Win32.Storage.FileSystem.SYMBOLIC_LINK_FLAGS, hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('KERNEL32.dll')
def CreateSymbolicLinkTransactedW(lpSymlinkFileName: win32more.Windows.Win32.Foundation.PWSTR, lpTargetFileName: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: win32more.Windows.Win32.Storage.FileSystem.SYMBOLIC_LINK_FLAGS, hTransaction: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
CreateSymbolicLinkTransacted = UnicodeAlias('CreateSymbolicLinkTransactedW')
class BY_HANDLE_FILE_INFORMATION(Structure):
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
def CACHE_ACCESS_CHECK(pSecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, hClientToken: win32more.Windows.Win32.Foundation.HANDLE, dwDesiredAccess: UInt32, GenericMapping: POINTER(win32more.Windows.Win32.Security.GENERIC_MAPPING), PrivilegeSet: POINTER(win32more.Windows.Win32.Security.PRIVILEGE_SET), PrivilegeSetLength: POINTER(UInt32), GrantedAccess: POINTER(UInt32), AccessStatus: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def CACHE_DESTROY_CALLBACK(cb: UInt32, lpb: POINTER(Byte)) -> Void: ...
@winfunctype_pointer
def CACHE_KEY_COMPARE(cbKey1: UInt32, lpbKey1: POINTER(Byte), cbKey2: UInt32, lpbKey2: POINTER(Byte)) -> Int32: ...
@winfunctype_pointer
def CACHE_KEY_HASH(lpbKey: POINTER(Byte), cbKey: UInt32) -> UInt32: ...
@winfunctype_pointer
def CACHE_READ_CALLBACK(cb: UInt32, lpb: POINTER(Byte), lpvContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def CLAIMMEDIALABEL(pBuffer: POINTER(Byte), nBufferSize: UInt32, pLabelInfo: POINTER(win32more.Windows.Win32.Storage.FileSystem.MediaLabelInfo)) -> UInt32: ...
@winfunctype_pointer
def CLAIMMEDIALABELEX(pBuffer: POINTER(Byte), nBufferSize: UInt32, pLabelInfo: POINTER(win32more.Windows.Win32.Storage.FileSystem.MediaLabelInfo), LabelGuid: POINTER(Guid)) -> UInt32: ...
@winfunctype_pointer
def CLFS_BLOCK_ALLOCATION(cbBufferLength: UInt32, pvUserContext: VoidPtr) -> VoidPtr: ...
@winfunctype_pointer
def CLFS_BLOCK_DEALLOCATION(pvBuffer: VoidPtr, pvUserContext: VoidPtr) -> Void: ...
CLFS_CONTEXT_MODE = Int32
ClfsContextNone: win32more.Windows.Win32.Storage.FileSystem.CLFS_CONTEXT_MODE = 0
ClfsContextUndoNext: win32more.Windows.Win32.Storage.FileSystem.CLFS_CONTEXT_MODE = 1
ClfsContextPrevious: win32more.Windows.Win32.Storage.FileSystem.CLFS_CONTEXT_MODE = 2
ClfsContextForward: win32more.Windows.Win32.Storage.FileSystem.CLFS_CONTEXT_MODE = 3
CLFS_FLAG = UInt32
CLFS_FLAG_FORCE_APPEND: win32more.Windows.Win32.Storage.FileSystem.CLFS_FLAG = 1
CLFS_FLAG_FORCE_FLUSH: win32more.Windows.Win32.Storage.FileSystem.CLFS_FLAG = 2
CLFS_FLAG_NO_FLAGS: win32more.Windows.Win32.Storage.FileSystem.CLFS_FLAG = 0
CLFS_FLAG_USE_RESERVATION: win32more.Windows.Win32.Storage.FileSystem.CLFS_FLAG = 4
CLFS_IOSTATS_CLASS = Int32
ClfsIoStatsDefault: win32more.Windows.Win32.Storage.FileSystem.CLFS_IOSTATS_CLASS = 0
ClfsIoStatsMax: win32more.Windows.Win32.Storage.FileSystem.CLFS_IOSTATS_CLASS = 65535
CLFS_LOG_ARCHIVE_MODE = Int32
ClfsLogArchiveEnabled: win32more.Windows.Win32.Storage.FileSystem.CLFS_LOG_ARCHIVE_MODE = 1
ClfsLogArchiveDisabled: win32more.Windows.Win32.Storage.FileSystem.CLFS_LOG_ARCHIVE_MODE = 2
class CLFS_LOG_NAME_INFORMATION(Structure):
    NameLengthInBytes: UInt16
    Name: Char * 1
class CLFS_MGMT_NOTIFICATION(Structure):
    Notification: win32more.Windows.Win32.Storage.FileSystem.CLFS_MGMT_NOTIFICATION_TYPE
    Lsn: win32more.Windows.Win32.Storage.FileSystem.CLS_LSN
    LogIsPinned: UInt16
CLFS_MGMT_NOTIFICATION_TYPE = Int32
ClfsMgmtAdvanceTailNotification: win32more.Windows.Win32.Storage.FileSystem.CLFS_MGMT_NOTIFICATION_TYPE = 0
ClfsMgmtLogFullHandlerNotification: win32more.Windows.Win32.Storage.FileSystem.CLFS_MGMT_NOTIFICATION_TYPE = 1
ClfsMgmtLogUnpinnedNotification: win32more.Windows.Win32.Storage.FileSystem.CLFS_MGMT_NOTIFICATION_TYPE = 2
ClfsMgmtLogWriteNotification: win32more.Windows.Win32.Storage.FileSystem.CLFS_MGMT_NOTIFICATION_TYPE = 3
class CLFS_MGMT_POLICY(Structure):
    Version: UInt32
    LengthInBytes: UInt32
    PolicyFlags: UInt32
    PolicyType: win32more.Windows.Win32.Storage.FileSystem.CLFS_MGMT_POLICY_TYPE
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
ClfsMgmtPolicyMaximumSize: win32more.Windows.Win32.Storage.FileSystem.CLFS_MGMT_POLICY_TYPE = 0
ClfsMgmtPolicyMinimumSize: win32more.Windows.Win32.Storage.FileSystem.CLFS_MGMT_POLICY_TYPE = 1
ClfsMgmtPolicyNewContainerSize: win32more.Windows.Win32.Storage.FileSystem.CLFS_MGMT_POLICY_TYPE = 2
ClfsMgmtPolicyGrowthRate: win32more.Windows.Win32.Storage.FileSystem.CLFS_MGMT_POLICY_TYPE = 3
ClfsMgmtPolicyLogTail: win32more.Windows.Win32.Storage.FileSystem.CLFS_MGMT_POLICY_TYPE = 4
ClfsMgmtPolicyAutoShrink: win32more.Windows.Win32.Storage.FileSystem.CLFS_MGMT_POLICY_TYPE = 5
ClfsMgmtPolicyAutoGrow: win32more.Windows.Win32.Storage.FileSystem.CLFS_MGMT_POLICY_TYPE = 6
ClfsMgmtPolicyNewContainerPrefix: win32more.Windows.Win32.Storage.FileSystem.CLFS_MGMT_POLICY_TYPE = 7
ClfsMgmtPolicyNewContainerSuffix: win32more.Windows.Win32.Storage.FileSystem.CLFS_MGMT_POLICY_TYPE = 8
ClfsMgmtPolicyNewContainerExtension: win32more.Windows.Win32.Storage.FileSystem.CLFS_MGMT_POLICY_TYPE = 9
ClfsMgmtPolicyInvalid: win32more.Windows.Win32.Storage.FileSystem.CLFS_MGMT_POLICY_TYPE = 10
class CLFS_NODE_ID(Structure):
    cType: UInt32
    cbNode: UInt32
class CLFS_PHYSICAL_LSN_INFORMATION(Structure):
    StreamIdentifier: Byte
    VirtualLsn: win32more.Windows.Win32.Storage.FileSystem.CLS_LSN
    PhysicalLsn: win32more.Windows.Win32.Storage.FileSystem.CLS_LSN
class CLFS_STREAM_ID_INFORMATION(Structure):
    StreamIdentifier: Byte
class CLS_ARCHIVE_DESCRIPTOR(Structure):
    coffLow: UInt64
    coffHigh: UInt64
    infoContainer: win32more.Windows.Win32.Storage.FileSystem.CLS_CONTAINER_INFORMATION
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
ClsContextNone: win32more.Windows.Win32.Storage.FileSystem.CLS_CONTEXT_MODE = 0
ClsContextUndoNext: win32more.Windows.Win32.Storage.FileSystem.CLS_CONTEXT_MODE = 1
ClsContextPrevious: win32more.Windows.Win32.Storage.FileSystem.CLS_CONTEXT_MODE = 2
ClsContextForward: win32more.Windows.Win32.Storage.FileSystem.CLS_CONTEXT_MODE = 3
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
    MinArchiveTailLsn: win32more.Windows.Win32.Storage.FileSystem.CLS_LSN
    BaseLsn: win32more.Windows.Win32.Storage.FileSystem.CLS_LSN
    LastFlushedLsn: win32more.Windows.Win32.Storage.FileSystem.CLS_LSN
    LastLsn: win32more.Windows.Win32.Storage.FileSystem.CLS_LSN
    RestartLsn: win32more.Windows.Win32.Storage.FileSystem.CLS_LSN
    Identity: Guid
CLS_IOSTATS_CLASS = Int32
ClsIoStatsDefault: win32more.Windows.Win32.Storage.FileSystem.CLS_IOSTATS_CLASS = 0
ClsIoStatsMax: win32more.Windows.Win32.Storage.FileSystem.CLS_IOSTATS_CLASS = 65535
class CLS_IO_STATISTICS(Structure):
    hdrIoStats: win32more.Windows.Win32.Storage.FileSystem.CLS_IO_STATISTICS_HEADER
    cFlush: UInt64
    cbFlush: UInt64
    cMetaFlush: UInt64
    cbMetaFlush: UInt64
class CLS_IO_STATISTICS_HEADER(Structure):
    ubMajorVersion: Byte
    ubMinorVersion: Byte
    eStatsClass: win32more.Windows.Win32.Storage.FileSystem.CLFS_IOSTATS_CLASS
    cbLength: UInt16
    coffData: UInt32
CLS_LOG_INFORMATION_CLASS = Int32
ClfsLogBasicInformation: win32more.Windows.Win32.Storage.FileSystem.CLS_LOG_INFORMATION_CLASS = 0
ClfsLogBasicInformationPhysical: win32more.Windows.Win32.Storage.FileSystem.CLS_LOG_INFORMATION_CLASS = 1
ClfsLogPhysicalNameInformation: win32more.Windows.Win32.Storage.FileSystem.CLS_LOG_INFORMATION_CLASS = 2
ClfsLogStreamIdentifierInformation: win32more.Windows.Win32.Storage.FileSystem.CLS_LOG_INFORMATION_CLASS = 3
ClfsLogSystemMarkingInformation: win32more.Windows.Win32.Storage.FileSystem.CLS_LOG_INFORMATION_CLASS = 4
ClfsLogPhysicalLsnInformation: win32more.Windows.Win32.Storage.FileSystem.CLS_LOG_INFORMATION_CLASS = 5
class CLS_LSN(Structure):
    Internal: UInt64
class CLS_SCAN_CONTEXT(Structure):
    cidNode: win32more.Windows.Win32.Storage.FileSystem.CLFS_NODE_ID
    hLog: win32more.Windows.Win32.Foundation.HANDLE
    cIndex: UInt32
    cContainers: UInt32
    cContainersReturned: UInt32
    eScanMode: Byte
    pinfoContainer: POINTER(win32more.Windows.Win32.Storage.FileSystem.CLS_CONTAINER_INFORMATION)
class CLS_WRITE_ENTRY(Structure):
    Buffer: VoidPtr
    ByteLength: UInt32
COMPRESSION_FORMAT = UInt16
COMPRESSION_FORMAT_NONE: win32more.Windows.Win32.Storage.FileSystem.COMPRESSION_FORMAT = 0
COMPRESSION_FORMAT_DEFAULT: win32more.Windows.Win32.Storage.FileSystem.COMPRESSION_FORMAT = 1
COMPRESSION_FORMAT_LZNT1: win32more.Windows.Win32.Storage.FileSystem.COMPRESSION_FORMAT = 2
COMPRESSION_FORMAT_XPRESS: win32more.Windows.Win32.Storage.FileSystem.COMPRESSION_FORMAT = 3
COMPRESSION_FORMAT_XPRESS_HUFF: win32more.Windows.Win32.Storage.FileSystem.COMPRESSION_FORMAT = 4
COMPRESSION_FORMAT_XP10: win32more.Windows.Win32.Storage.FileSystem.COMPRESSION_FORMAT = 5
class CONNECTION_INFO_0(Structure):
    coni0_id: UInt32
class CONNECTION_INFO_1(Structure):
    coni1_id: UInt32
    coni1_type: win32more.Windows.Win32.Storage.FileSystem.SHARE_TYPE
    coni1_num_opens: UInt32
    coni1_num_users: UInt32
    coni1_time: UInt32
    coni1_username: win32more.Windows.Win32.Foundation.PWSTR
    coni1_netname: win32more.Windows.Win32.Foundation.PWSTR
COPYFILE2_COPY_PHASE = Int32
COPYFILE2_PHASE_NONE: win32more.Windows.Win32.Storage.FileSystem.COPYFILE2_COPY_PHASE = 0
COPYFILE2_PHASE_PREPARE_SOURCE: win32more.Windows.Win32.Storage.FileSystem.COPYFILE2_COPY_PHASE = 1
COPYFILE2_PHASE_PREPARE_DEST: win32more.Windows.Win32.Storage.FileSystem.COPYFILE2_COPY_PHASE = 2
COPYFILE2_PHASE_READ_SOURCE: win32more.Windows.Win32.Storage.FileSystem.COPYFILE2_COPY_PHASE = 3
COPYFILE2_PHASE_WRITE_DESTINATION: win32more.Windows.Win32.Storage.FileSystem.COPYFILE2_COPY_PHASE = 4
COPYFILE2_PHASE_SERVER_COPY: win32more.Windows.Win32.Storage.FileSystem.COPYFILE2_COPY_PHASE = 5
COPYFILE2_PHASE_NAMEGRAFT_COPY: win32more.Windows.Win32.Storage.FileSystem.COPYFILE2_COPY_PHASE = 6
COPYFILE2_PHASE_MAX: win32more.Windows.Win32.Storage.FileSystem.COPYFILE2_COPY_PHASE = 7
class COPYFILE2_EXTENDED_PARAMETERS(Structure):
    dwSize: UInt32
    dwCopyFlags: win32more.Windows.Win32.Storage.FileSystem.COPYFILE_FLAGS
    pfCancel: POINTER(win32more.Windows.Win32.Foundation.BOOL)
    pProgressRoutine: win32more.Windows.Win32.Storage.FileSystem.PCOPYFILE2_PROGRESS_ROUTINE
    pvCallbackContext: VoidPtr
class COPYFILE2_EXTENDED_PARAMETERS_V2(Structure):
    dwSize: UInt32
    dwCopyFlags: win32more.Windows.Win32.Storage.FileSystem.COPYFILE_FLAGS
    pfCancel: POINTER(win32more.Windows.Win32.Foundation.BOOL)
    pProgressRoutine: win32more.Windows.Win32.Storage.FileSystem.PCOPYFILE2_PROGRESS_ROUTINE
    pvCallbackContext: VoidPtr
    dwCopyFlagsV2: win32more.Windows.Win32.Storage.FileSystem.COPYFILE2_V2_FLAGS
    ioDesiredSize: UInt32
    ioDesiredRate: UInt32
    reserved: VoidPtr * 8
class COPYFILE2_MESSAGE(Structure):
    Type: win32more.Windows.Win32.Storage.FileSystem.COPYFILE2_MESSAGE_TYPE
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
            hSourceFile: win32more.Windows.Win32.Foundation.HANDLE
            hDestinationFile: win32more.Windows.Win32.Foundation.HANDLE
            uliChunkNumber: UInt64
            uliChunkSize: UInt64
            uliStreamSize: UInt64
            uliTotalFileSize: UInt64
        class _ChunkFinished_e__Struct(Structure):
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
        class _StreamStarted_e__Struct(Structure):
            dwStreamNumber: UInt32
            dwReserved: UInt32
            hSourceFile: win32more.Windows.Win32.Foundation.HANDLE
            hDestinationFile: win32more.Windows.Win32.Foundation.HANDLE
            uliStreamSize: UInt64
            uliTotalFileSize: UInt64
        class _StreamFinished_e__Struct(Structure):
            dwStreamNumber: UInt32
            dwReserved: UInt32
            hSourceFile: win32more.Windows.Win32.Foundation.HANDLE
            hDestinationFile: win32more.Windows.Win32.Foundation.HANDLE
            uliStreamSize: UInt64
            uliStreamBytesTransferred: UInt64
            uliTotalFileSize: UInt64
            uliTotalBytesTransferred: UInt64
        class _PollContinue_e__Struct(Structure):
            dwReserved: UInt32
        class _Error_e__Struct(Structure):
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
COPYFILE2_PROGRESS_CONTINUE: win32more.Windows.Win32.Storage.FileSystem.COPYFILE2_MESSAGE_ACTION = 0
COPYFILE2_PROGRESS_CANCEL: win32more.Windows.Win32.Storage.FileSystem.COPYFILE2_MESSAGE_ACTION = 1
COPYFILE2_PROGRESS_STOP: win32more.Windows.Win32.Storage.FileSystem.COPYFILE2_MESSAGE_ACTION = 2
COPYFILE2_PROGRESS_QUIET: win32more.Windows.Win32.Storage.FileSystem.COPYFILE2_MESSAGE_ACTION = 3
COPYFILE2_PROGRESS_PAUSE: win32more.Windows.Win32.Storage.FileSystem.COPYFILE2_MESSAGE_ACTION = 4
COPYFILE2_MESSAGE_TYPE = Int32
COPYFILE2_CALLBACK_NONE: win32more.Windows.Win32.Storage.FileSystem.COPYFILE2_MESSAGE_TYPE = 0
COPYFILE2_CALLBACK_CHUNK_STARTED: win32more.Windows.Win32.Storage.FileSystem.COPYFILE2_MESSAGE_TYPE = 1
COPYFILE2_CALLBACK_CHUNK_FINISHED: win32more.Windows.Win32.Storage.FileSystem.COPYFILE2_MESSAGE_TYPE = 2
COPYFILE2_CALLBACK_STREAM_STARTED: win32more.Windows.Win32.Storage.FileSystem.COPYFILE2_MESSAGE_TYPE = 3
COPYFILE2_CALLBACK_STREAM_FINISHED: win32more.Windows.Win32.Storage.FileSystem.COPYFILE2_MESSAGE_TYPE = 4
COPYFILE2_CALLBACK_POLL_CONTINUE: win32more.Windows.Win32.Storage.FileSystem.COPYFILE2_MESSAGE_TYPE = 5
COPYFILE2_CALLBACK_ERROR: win32more.Windows.Win32.Storage.FileSystem.COPYFILE2_MESSAGE_TYPE = 6
COPYFILE2_CALLBACK_MAX: win32more.Windows.Win32.Storage.FileSystem.COPYFILE2_MESSAGE_TYPE = 7
COPYFILE2_V2_FLAGS = UInt32
COPY_FILE2_V2_DONT_COPY_JUNCTIONS: win32more.Windows.Win32.Storage.FileSystem.COPYFILE2_V2_FLAGS = 1
COPY_FILE2_V2_VALID_FLAGS: win32more.Windows.Win32.Storage.FileSystem.COPYFILE2_V2_FLAGS = 1
COPYFILE_FLAGS = UInt32
COPY_FILE_FAIL_IF_EXISTS: win32more.Windows.Win32.Storage.FileSystem.COPYFILE_FLAGS = 1
COPY_FILE_RESTARTABLE: win32more.Windows.Win32.Storage.FileSystem.COPYFILE_FLAGS = 2
COPY_FILE_OPEN_SOURCE_FOR_WRITE: win32more.Windows.Win32.Storage.FileSystem.COPYFILE_FLAGS = 4
COPY_FILE_ALLOW_DECRYPTED_DESTINATION: win32more.Windows.Win32.Storage.FileSystem.COPYFILE_FLAGS = 8
COPY_FILE_COPY_SYMLINK: win32more.Windows.Win32.Storage.FileSystem.COPYFILE_FLAGS = 2048
COPY_FILE_NO_BUFFERING: win32more.Windows.Win32.Storage.FileSystem.COPYFILE_FLAGS = 4096
COPY_FILE_REQUEST_SECURITY_PRIVILEGES: win32more.Windows.Win32.Storage.FileSystem.COPYFILE_FLAGS = 8192
COPY_FILE_RESUME_FROM_PAUSE: win32more.Windows.Win32.Storage.FileSystem.COPYFILE_FLAGS = 16384
COPY_FILE_NO_OFFLOAD: win32more.Windows.Win32.Storage.FileSystem.COPYFILE_FLAGS = 262144
COPY_FILE_IGNORE_EDP_BLOCK: win32more.Windows.Win32.Storage.FileSystem.COPYFILE_FLAGS = 4194304
COPY_FILE_IGNORE_SOURCE_ENCRYPTION: win32more.Windows.Win32.Storage.FileSystem.COPYFILE_FLAGS = 8388608
COPY_FILE_DONT_REQUEST_DEST_WRITE_DAC: win32more.Windows.Win32.Storage.FileSystem.COPYFILE_FLAGS = 33554432
COPY_FILE_REQUEST_COMPRESSED_TRAFFIC: win32more.Windows.Win32.Storage.FileSystem.COPYFILE_FLAGS = 268435456
COPY_FILE_OPEN_AND_COPY_REPARSE_POINT: win32more.Windows.Win32.Storage.FileSystem.COPYFILE_FLAGS = 2097152
COPY_FILE_DIRECTORY: win32more.Windows.Win32.Storage.FileSystem.COPYFILE_FLAGS = 128
COPY_FILE_SKIP_ALTERNATE_STREAMS: win32more.Windows.Win32.Storage.FileSystem.COPYFILE_FLAGS = 32768
COPY_FILE_DISABLE_PRE_ALLOCATION: win32more.Windows.Win32.Storage.FileSystem.COPYFILE_FLAGS = 67108864
COPY_FILE_ENABLE_LOW_FREE_SPACE_MODE: win32more.Windows.Win32.Storage.FileSystem.COPYFILE_FLAGS = 134217728
COPY_FILE_ENABLE_SPARSE_COPY: win32more.Windows.Win32.Storage.FileSystem.COPYFILE_FLAGS = 536870912
COPYPROGRESSROUTINE_PROGRESS = UInt32
PROGRESS_CONTINUE: win32more.Windows.Win32.Storage.FileSystem.COPYPROGRESSROUTINE_PROGRESS = 0
PROGRESS_CANCEL: win32more.Windows.Win32.Storage.FileSystem.COPYPROGRESSROUTINE_PROGRESS = 1
PROGRESS_STOP: win32more.Windows.Win32.Storage.FileSystem.COPYPROGRESSROUTINE_PROGRESS = 2
PROGRESS_QUIET: win32more.Windows.Win32.Storage.FileSystem.COPYPROGRESSROUTINE_PROGRESS = 3
class CREATEFILE2_EXTENDED_PARAMETERS(Structure):
    dwSize: UInt32
    dwFileAttributes: UInt32
    dwFileFlags: UInt32
    dwSecurityQosFlags: UInt32
    lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES)
    hTemplateFile: win32more.Windows.Win32.Foundation.HANDLE
CREATE_TAPE_PARTITION_METHOD = UInt32
TAPE_FIXED_PARTITIONS: win32more.Windows.Win32.Storage.FileSystem.CREATE_TAPE_PARTITION_METHOD = 0
TAPE_INITIATOR_PARTITIONS: win32more.Windows.Win32.Storage.FileSystem.CREATE_TAPE_PARTITION_METHOD = 2
TAPE_SELECT_PARTITIONS: win32more.Windows.Win32.Storage.FileSystem.CREATE_TAPE_PARTITION_METHOD = 1
DEFINE_DOS_DEVICE_FLAGS = UInt32
DDD_RAW_TARGET_PATH: win32more.Windows.Win32.Storage.FileSystem.DEFINE_DOS_DEVICE_FLAGS = 1
DDD_REMOVE_DEFINITION: win32more.Windows.Win32.Storage.FileSystem.DEFINE_DOS_DEVICE_FLAGS = 2
DDD_EXACT_MATCH_ON_REMOVE: win32more.Windows.Win32.Storage.FileSystem.DEFINE_DOS_DEVICE_FLAGS = 4
DDD_NO_BROADCAST_SYSTEM: win32more.Windows.Win32.Storage.FileSystem.DEFINE_DOS_DEVICE_FLAGS = 8
DDD_LUID_BROADCAST_DRIVE: win32more.Windows.Win32.Storage.FileSystem.DEFINE_DOS_DEVICE_FLAGS = 16
DISKQUOTA_USERNAME_RESOLVE = UInt32
DISKQUOTA_USERNAME_RESOLVE_ASYNC: win32more.Windows.Win32.Storage.FileSystem.DISKQUOTA_USERNAME_RESOLVE = 2
DISKQUOTA_USERNAME_RESOLVE_NONE: win32more.Windows.Win32.Storage.FileSystem.DISKQUOTA_USERNAME_RESOLVE = 0
DISKQUOTA_USERNAME_RESOLVE_SYNC: win32more.Windows.Win32.Storage.FileSystem.DISKQUOTA_USERNAME_RESOLVE = 1
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
    pbData: POINTER(Byte)
class EFS_COMPATIBILITY_INFO(Structure):
    EfsVersion: UInt32
class EFS_DECRYPTION_STATUS_INFO(Structure):
    dwDecryptionError: UInt32
    dwHashOffset: UInt32
    cbHash: UInt32
class EFS_ENCRYPTION_STATUS_INFO(Structure):
    bHasCurrentKey: win32more.Windows.Win32.Foundation.BOOL
    dwEncryptionError: UInt32
class EFS_HASH_BLOB(Structure):
    cbData: UInt32
    pbData: POINTER(Byte)
class EFS_KEY_INFO(Structure):
    dwVersion: UInt32
    Entropy: UInt32
    Algorithm: win32more.Windows.Win32.Security.Cryptography.ALG_ID
    KeyLength: UInt32
class EFS_PIN_BLOB(Structure):
    cbPadding: UInt32
    cbData: UInt32
    pbData: POINTER(Byte)
class EFS_RPC_BLOB(Structure):
    cbData: UInt32
    pbData: POINTER(Byte)
class EFS_VERSION_INFO(Structure):
    EfsVersion: UInt32
    SubVersion: UInt32
class ENCRYPTED_FILE_METADATA_SIGNATURE(Structure):
    dwEfsAccessType: UInt32
    pCertificatesAdded: POINTER(win32more.Windows.Win32.Storage.FileSystem.ENCRYPTION_CERTIFICATE_HASH_LIST)
    pEncryptionCertificate: POINTER(win32more.Windows.Win32.Storage.FileSystem.ENCRYPTION_CERTIFICATE)
    pEfsStreamSignature: POINTER(win32more.Windows.Win32.Storage.FileSystem.EFS_RPC_BLOB)
class ENCRYPTION_CERTIFICATE(Structure):
    cbTotalLength: UInt32
    pUserSid: POINTER(win32more.Windows.Win32.Security.SID)
    pCertBlob: POINTER(win32more.Windows.Win32.Storage.FileSystem.EFS_CERTIFICATE_BLOB)
class ENCRYPTION_CERTIFICATE_HASH(Structure):
    cbTotalLength: UInt32
    pUserSid: POINTER(win32more.Windows.Win32.Security.SID)
    pHash: POINTER(win32more.Windows.Win32.Storage.FileSystem.EFS_HASH_BLOB)
    lpDisplayInformation: win32more.Windows.Win32.Foundation.PWSTR
class ENCRYPTION_CERTIFICATE_HASH_LIST(Structure):
    nCert_Hash: UInt32
    pUsers: POINTER(POINTER(win32more.Windows.Win32.Storage.FileSystem.ENCRYPTION_CERTIFICATE_HASH))
class ENCRYPTION_CERTIFICATE_LIST(Structure):
    nUsers: UInt32
    pUsers: POINTER(POINTER(win32more.Windows.Win32.Storage.FileSystem.ENCRYPTION_CERTIFICATE))
class ENCRYPTION_PROTECTOR(Structure):
    cbTotalLength: UInt32
    pUserSid: POINTER(win32more.Windows.Win32.Security.SID)
    lpProtectorDescriptor: win32more.Windows.Win32.Foundation.PWSTR
class ENCRYPTION_PROTECTOR_LIST(Structure):
    nProtectors: UInt32
    pProtectors: POINTER(POINTER(win32more.Windows.Win32.Storage.FileSystem.ENCRYPTION_PROTECTOR))
ERASE_TAPE_TYPE = UInt32
TAPE_ERASE_LONG: win32more.Windows.Win32.Storage.FileSystem.ERASE_TAPE_TYPE = 1
TAPE_ERASE_SHORT: win32more.Windows.Win32.Storage.FileSystem.ERASE_TAPE_TYPE = 0
@winfunctype_pointer
def FCACHE_CREATE_CALLBACK(lpstrName: win32more.Windows.Win32.Foundation.PSTR, lpvData: VoidPtr, cbFileSize: POINTER(UInt32), cbFileSizeHigh: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype_pointer
def FCACHE_RICHCREATE_CALLBACK(lpstrName: win32more.Windows.Win32.Foundation.PSTR, lpvData: VoidPtr, cbFileSize: POINTER(UInt32), cbFileSizeHigh: POINTER(UInt32), pfDidWeScanIt: POINTER(win32more.Windows.Win32.Foundation.BOOL), pfIsStuffed: POINTER(win32more.Windows.Win32.Foundation.BOOL), pfStoredWithDots: POINTER(win32more.Windows.Win32.Foundation.BOOL), pfStoredWithTerminatingDot: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HANDLE: ...
class FH_OVERLAPPED(Structure):
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
FILE_READ_DATA: win32more.Windows.Win32.Storage.FileSystem.FILE_ACCESS_RIGHTS = 1
FILE_LIST_DIRECTORY: win32more.Windows.Win32.Storage.FileSystem.FILE_ACCESS_RIGHTS = 1
FILE_WRITE_DATA: win32more.Windows.Win32.Storage.FileSystem.FILE_ACCESS_RIGHTS = 2
FILE_ADD_FILE: win32more.Windows.Win32.Storage.FileSystem.FILE_ACCESS_RIGHTS = 2
FILE_APPEND_DATA: win32more.Windows.Win32.Storage.FileSystem.FILE_ACCESS_RIGHTS = 4
FILE_ADD_SUBDIRECTORY: win32more.Windows.Win32.Storage.FileSystem.FILE_ACCESS_RIGHTS = 4
FILE_CREATE_PIPE_INSTANCE: win32more.Windows.Win32.Storage.FileSystem.FILE_ACCESS_RIGHTS = 4
FILE_READ_EA: win32more.Windows.Win32.Storage.FileSystem.FILE_ACCESS_RIGHTS = 8
FILE_WRITE_EA: win32more.Windows.Win32.Storage.FileSystem.FILE_ACCESS_RIGHTS = 16
FILE_EXECUTE: win32more.Windows.Win32.Storage.FileSystem.FILE_ACCESS_RIGHTS = 32
FILE_TRAVERSE: win32more.Windows.Win32.Storage.FileSystem.FILE_ACCESS_RIGHTS = 32
FILE_DELETE_CHILD: win32more.Windows.Win32.Storage.FileSystem.FILE_ACCESS_RIGHTS = 64
FILE_READ_ATTRIBUTES: win32more.Windows.Win32.Storage.FileSystem.FILE_ACCESS_RIGHTS = 128
FILE_WRITE_ATTRIBUTES: win32more.Windows.Win32.Storage.FileSystem.FILE_ACCESS_RIGHTS = 256
DELETE: win32more.Windows.Win32.Storage.FileSystem.FILE_ACCESS_RIGHTS = 65536
READ_CONTROL: win32more.Windows.Win32.Storage.FileSystem.FILE_ACCESS_RIGHTS = 131072
WRITE_DAC: win32more.Windows.Win32.Storage.FileSystem.FILE_ACCESS_RIGHTS = 262144
WRITE_OWNER: win32more.Windows.Win32.Storage.FileSystem.FILE_ACCESS_RIGHTS = 524288
SYNCHRONIZE: win32more.Windows.Win32.Storage.FileSystem.FILE_ACCESS_RIGHTS = 1048576
STANDARD_RIGHTS_REQUIRED: win32more.Windows.Win32.Storage.FileSystem.FILE_ACCESS_RIGHTS = 983040
STANDARD_RIGHTS_READ: win32more.Windows.Win32.Storage.FileSystem.FILE_ACCESS_RIGHTS = 131072
STANDARD_RIGHTS_WRITE: win32more.Windows.Win32.Storage.FileSystem.FILE_ACCESS_RIGHTS = 131072
STANDARD_RIGHTS_EXECUTE: win32more.Windows.Win32.Storage.FileSystem.FILE_ACCESS_RIGHTS = 131072
STANDARD_RIGHTS_ALL: win32more.Windows.Win32.Storage.FileSystem.FILE_ACCESS_RIGHTS = 2031616
SPECIFIC_RIGHTS_ALL: win32more.Windows.Win32.Storage.FileSystem.FILE_ACCESS_RIGHTS = 65535
FILE_ALL_ACCESS: win32more.Windows.Win32.Storage.FileSystem.FILE_ACCESS_RIGHTS = 2032127
FILE_GENERIC_READ: win32more.Windows.Win32.Storage.FileSystem.FILE_ACCESS_RIGHTS = 1179785
FILE_GENERIC_WRITE: win32more.Windows.Win32.Storage.FileSystem.FILE_ACCESS_RIGHTS = 1179926
FILE_GENERIC_EXECUTE: win32more.Windows.Win32.Storage.FileSystem.FILE_ACCESS_RIGHTS = 1179808
FILE_ACTION = UInt32
FILE_ACTION_ADDED: win32more.Windows.Win32.Storage.FileSystem.FILE_ACTION = 1
FILE_ACTION_REMOVED: win32more.Windows.Win32.Storage.FileSystem.FILE_ACTION = 2
FILE_ACTION_MODIFIED: win32more.Windows.Win32.Storage.FileSystem.FILE_ACTION = 3
FILE_ACTION_RENAMED_OLD_NAME: win32more.Windows.Win32.Storage.FileSystem.FILE_ACTION = 4
FILE_ACTION_RENAMED_NEW_NAME: win32more.Windows.Win32.Storage.FileSystem.FILE_ACTION = 5
class FILE_ALIGNMENT_INFO(Structure):
    AlignmentRequirement: UInt32
class FILE_ALLOCATION_INFO(Structure):
    AllocationSize: Int64
class FILE_ATTRIBUTE_TAG_INFO(Structure):
    FileAttributes: UInt32
    ReparseTag: UInt32
class FILE_BASIC_INFO(Structure):
    CreationTime: Int64
    LastAccessTime: Int64
    LastWriteTime: Int64
    ChangeTime: Int64
    FileAttributes: UInt32
class FILE_CASE_SENSITIVE_INFO(Structure):
    Flags: UInt32
class FILE_COMPRESSION_INFO(Structure):
    CompressedFileSize: Int64
    CompressionFormat: win32more.Windows.Win32.Storage.FileSystem.COMPRESSION_FORMAT
    CompressionUnitShift: Byte
    ChunkShift: Byte
    ClusterShift: Byte
    Reserved: Byte * 3
FILE_CREATION_DISPOSITION = UInt32
CREATE_NEW: win32more.Windows.Win32.Storage.FileSystem.FILE_CREATION_DISPOSITION = 1
CREATE_ALWAYS: win32more.Windows.Win32.Storage.FileSystem.FILE_CREATION_DISPOSITION = 2
OPEN_EXISTING: win32more.Windows.Win32.Storage.FileSystem.FILE_CREATION_DISPOSITION = 3
OPEN_ALWAYS: win32more.Windows.Win32.Storage.FileSystem.FILE_CREATION_DISPOSITION = 4
TRUNCATE_EXISTING: win32more.Windows.Win32.Storage.FileSystem.FILE_CREATION_DISPOSITION = 5
FILE_DEVICE_TYPE = UInt32
FILE_DEVICE_CD_ROM: win32more.Windows.Win32.Storage.FileSystem.FILE_DEVICE_TYPE = 2
FILE_DEVICE_DISK: win32more.Windows.Win32.Storage.FileSystem.FILE_DEVICE_TYPE = 7
FILE_DEVICE_TAPE: win32more.Windows.Win32.Storage.FileSystem.FILE_DEVICE_TYPE = 31
FILE_DEVICE_DVD: win32more.Windows.Win32.Storage.FileSystem.FILE_DEVICE_TYPE = 51
class FILE_DISPOSITION_INFO(Structure):
    DeleteFile: win32more.Windows.Win32.Foundation.BOOLEAN
class FILE_DISPOSITION_INFO_EX(Structure):
    Flags: win32more.Windows.Win32.Storage.FileSystem.FILE_DISPOSITION_INFO_EX_FLAGS
FILE_DISPOSITION_INFO_EX_FLAGS = UInt32
FILE_DISPOSITION_FLAG_DO_NOT_DELETE: win32more.Windows.Win32.Storage.FileSystem.FILE_DISPOSITION_INFO_EX_FLAGS = 0
FILE_DISPOSITION_FLAG_DELETE: win32more.Windows.Win32.Storage.FileSystem.FILE_DISPOSITION_INFO_EX_FLAGS = 1
FILE_DISPOSITION_FLAG_POSIX_SEMANTICS: win32more.Windows.Win32.Storage.FileSystem.FILE_DISPOSITION_INFO_EX_FLAGS = 2
FILE_DISPOSITION_FLAG_FORCE_IMAGE_SECTION_CHECK: win32more.Windows.Win32.Storage.FileSystem.FILE_DISPOSITION_INFO_EX_FLAGS = 4
FILE_DISPOSITION_FLAG_ON_CLOSE: win32more.Windows.Win32.Storage.FileSystem.FILE_DISPOSITION_INFO_EX_FLAGS = 8
FILE_DISPOSITION_FLAG_IGNORE_READONLY_ATTRIBUTE: win32more.Windows.Win32.Storage.FileSystem.FILE_DISPOSITION_INFO_EX_FLAGS = 16
class FILE_END_OF_FILE_INFO(Structure):
    EndOfFile: Int64
class FILE_EXTENT(Structure):
    VolumeOffset: UInt64
    ExtentLength: UInt64
FILE_FLAGS_AND_ATTRIBUTES = UInt32
FILE_ATTRIBUTE_READONLY: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES = 1
FILE_ATTRIBUTE_HIDDEN: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES = 2
FILE_ATTRIBUTE_SYSTEM: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES = 4
FILE_ATTRIBUTE_DIRECTORY: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES = 16
FILE_ATTRIBUTE_ARCHIVE: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES = 32
FILE_ATTRIBUTE_DEVICE: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES = 64
FILE_ATTRIBUTE_NORMAL: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES = 128
FILE_ATTRIBUTE_TEMPORARY: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES = 256
FILE_ATTRIBUTE_SPARSE_FILE: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES = 512
FILE_ATTRIBUTE_REPARSE_POINT: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES = 1024
FILE_ATTRIBUTE_COMPRESSED: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES = 2048
FILE_ATTRIBUTE_OFFLINE: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES = 4096
FILE_ATTRIBUTE_NOT_CONTENT_INDEXED: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES = 8192
FILE_ATTRIBUTE_ENCRYPTED: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES = 16384
FILE_ATTRIBUTE_INTEGRITY_STREAM: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES = 32768
FILE_ATTRIBUTE_VIRTUAL: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES = 65536
FILE_ATTRIBUTE_NO_SCRUB_DATA: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES = 131072
FILE_ATTRIBUTE_EA: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES = 262144
FILE_ATTRIBUTE_PINNED: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES = 524288
FILE_ATTRIBUTE_UNPINNED: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES = 1048576
FILE_ATTRIBUTE_RECALL_ON_OPEN: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES = 262144
FILE_ATTRIBUTE_RECALL_ON_DATA_ACCESS: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES = 4194304
FILE_FLAG_WRITE_THROUGH: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES = 2147483648
FILE_FLAG_OVERLAPPED: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES = 1073741824
FILE_FLAG_NO_BUFFERING: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES = 536870912
FILE_FLAG_RANDOM_ACCESS: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES = 268435456
FILE_FLAG_SEQUENTIAL_SCAN: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES = 134217728
FILE_FLAG_DELETE_ON_CLOSE: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES = 67108864
FILE_FLAG_BACKUP_SEMANTICS: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES = 33554432
FILE_FLAG_POSIX_SEMANTICS: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES = 16777216
FILE_FLAG_SESSION_AWARE: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES = 8388608
FILE_FLAG_OPEN_REPARSE_POINT: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES = 2097152
FILE_FLAG_OPEN_NO_RECALL: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES = 1048576
FILE_FLAG_FIRST_PIPE_INSTANCE: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES = 524288
PIPE_ACCESS_DUPLEX: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES = 3
PIPE_ACCESS_INBOUND: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES = 1
PIPE_ACCESS_OUTBOUND: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES = 2
SECURITY_ANONYMOUS: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES = 0
SECURITY_IDENTIFICATION: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES = 65536
SECURITY_IMPERSONATION: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES = 131072
SECURITY_DELEGATION: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES = 196608
SECURITY_CONTEXT_TRACKING: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES = 262144
SECURITY_EFFECTIVE_ONLY: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES = 524288
SECURITY_SQOS_PRESENT: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES = 1048576
SECURITY_VALID_SQOS_FLAGS: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES = 2031616
FILE_FLUSH_MODE = Int32
FILE_FLUSH_DEFAULT: win32more.Windows.Win32.Storage.FileSystem.FILE_FLUSH_MODE = 0
FILE_FLUSH_DATA: win32more.Windows.Win32.Storage.FileSystem.FILE_FLUSH_MODE = 1
FILE_FLUSH_MIN_METADATA: win32more.Windows.Win32.Storage.FileSystem.FILE_FLUSH_MODE = 2
FILE_FLUSH_NO_SYNC: win32more.Windows.Win32.Storage.FileSystem.FILE_FLUSH_MODE = 3
class FILE_FULL_DIR_INFO(Structure):
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
class FILE_ID_128(Structure):
    Identifier: Byte * 16
class FILE_ID_BOTH_DIR_INFO(Structure):
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
class FILE_ID_DESCRIPTOR(Structure):
    dwSize: UInt32
    Type: win32more.Windows.Win32.Storage.FileSystem.FILE_ID_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        FileId: Int64
        ObjectId: Guid
        ExtendedFileId: win32more.Windows.Win32.Storage.FileSystem.FILE_ID_128
class FILE_ID_EXTD_DIR_INFO(Structure):
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
class FILE_ID_INFO(Structure):
    VolumeSerialNumber: UInt64
    FileId: win32more.Windows.Win32.Storage.FileSystem.FILE_ID_128
FILE_ID_TYPE = Int32
FileIdType: win32more.Windows.Win32.Storage.FileSystem.FILE_ID_TYPE = 0
ObjectIdType: win32more.Windows.Win32.Storage.FileSystem.FILE_ID_TYPE = 1
ExtendedFileIdType: win32more.Windows.Win32.Storage.FileSystem.FILE_ID_TYPE = 2
MaximumFileIdType: win32more.Windows.Win32.Storage.FileSystem.FILE_ID_TYPE = 3
class FILE_INFO_2(Structure):
    fi2_id: UInt32
class FILE_INFO_3(Structure):
    fi3_id: UInt32
    fi3_permissions: win32more.Windows.Win32.Storage.FileSystem.FILE_INFO_FLAGS_PERMISSIONS
    fi3_num_locks: UInt32
    fi3_pathname: win32more.Windows.Win32.Foundation.PWSTR
    fi3_username: win32more.Windows.Win32.Foundation.PWSTR
FILE_INFO_BY_HANDLE_CLASS = Int32
FileBasicInfo: win32more.Windows.Win32.Storage.FileSystem.FILE_INFO_BY_HANDLE_CLASS = 0
FileStandardInfo: win32more.Windows.Win32.Storage.FileSystem.FILE_INFO_BY_HANDLE_CLASS = 1
FileNameInfo: win32more.Windows.Win32.Storage.FileSystem.FILE_INFO_BY_HANDLE_CLASS = 2
FileRenameInfo: win32more.Windows.Win32.Storage.FileSystem.FILE_INFO_BY_HANDLE_CLASS = 3
FileDispositionInfo: win32more.Windows.Win32.Storage.FileSystem.FILE_INFO_BY_HANDLE_CLASS = 4
FileAllocationInfo: win32more.Windows.Win32.Storage.FileSystem.FILE_INFO_BY_HANDLE_CLASS = 5
FileEndOfFileInfo: win32more.Windows.Win32.Storage.FileSystem.FILE_INFO_BY_HANDLE_CLASS = 6
FileStreamInfo: win32more.Windows.Win32.Storage.FileSystem.FILE_INFO_BY_HANDLE_CLASS = 7
FileCompressionInfo: win32more.Windows.Win32.Storage.FileSystem.FILE_INFO_BY_HANDLE_CLASS = 8
FileAttributeTagInfo: win32more.Windows.Win32.Storage.FileSystem.FILE_INFO_BY_HANDLE_CLASS = 9
FileIdBothDirectoryInfo: win32more.Windows.Win32.Storage.FileSystem.FILE_INFO_BY_HANDLE_CLASS = 10
FileIdBothDirectoryRestartInfo: win32more.Windows.Win32.Storage.FileSystem.FILE_INFO_BY_HANDLE_CLASS = 11
FileIoPriorityHintInfo: win32more.Windows.Win32.Storage.FileSystem.FILE_INFO_BY_HANDLE_CLASS = 12
FileRemoteProtocolInfo: win32more.Windows.Win32.Storage.FileSystem.FILE_INFO_BY_HANDLE_CLASS = 13
FileFullDirectoryInfo: win32more.Windows.Win32.Storage.FileSystem.FILE_INFO_BY_HANDLE_CLASS = 14
FileFullDirectoryRestartInfo: win32more.Windows.Win32.Storage.FileSystem.FILE_INFO_BY_HANDLE_CLASS = 15
FileStorageInfo: win32more.Windows.Win32.Storage.FileSystem.FILE_INFO_BY_HANDLE_CLASS = 16
FileAlignmentInfo: win32more.Windows.Win32.Storage.FileSystem.FILE_INFO_BY_HANDLE_CLASS = 17
FileIdInfo: win32more.Windows.Win32.Storage.FileSystem.FILE_INFO_BY_HANDLE_CLASS = 18
FileIdExtdDirectoryInfo: win32more.Windows.Win32.Storage.FileSystem.FILE_INFO_BY_HANDLE_CLASS = 19
FileIdExtdDirectoryRestartInfo: win32more.Windows.Win32.Storage.FileSystem.FILE_INFO_BY_HANDLE_CLASS = 20
FileDispositionInfoEx: win32more.Windows.Win32.Storage.FileSystem.FILE_INFO_BY_HANDLE_CLASS = 21
FileRenameInfoEx: win32more.Windows.Win32.Storage.FileSystem.FILE_INFO_BY_HANDLE_CLASS = 22
FileCaseSensitiveInfo: win32more.Windows.Win32.Storage.FileSystem.FILE_INFO_BY_HANDLE_CLASS = 23
FileNormalizedNameInfo: win32more.Windows.Win32.Storage.FileSystem.FILE_INFO_BY_HANDLE_CLASS = 24
MaximumFileInfoByHandleClass: win32more.Windows.Win32.Storage.FileSystem.FILE_INFO_BY_HANDLE_CLASS = 25
FILE_INFO_FLAGS_PERMISSIONS = UInt32
PERM_FILE_READ: win32more.Windows.Win32.Storage.FileSystem.FILE_INFO_FLAGS_PERMISSIONS = 1
PERM_FILE_WRITE: win32more.Windows.Win32.Storage.FileSystem.FILE_INFO_FLAGS_PERMISSIONS = 2
PERM_FILE_CREATE: win32more.Windows.Win32.Storage.FileSystem.FILE_INFO_FLAGS_PERMISSIONS = 4
class FILE_IO_PRIORITY_HINT_INFO(Structure):
    PriorityHint: win32more.Windows.Win32.Storage.FileSystem.PRIORITY_HINT
class FILE_NAME_INFO(Structure):
    FileNameLength: UInt32
    FileName: Char * 1
FILE_NOTIFY_CHANGE = UInt32
FILE_NOTIFY_CHANGE_FILE_NAME: win32more.Windows.Win32.Storage.FileSystem.FILE_NOTIFY_CHANGE = 1
FILE_NOTIFY_CHANGE_DIR_NAME: win32more.Windows.Win32.Storage.FileSystem.FILE_NOTIFY_CHANGE = 2
FILE_NOTIFY_CHANGE_ATTRIBUTES: win32more.Windows.Win32.Storage.FileSystem.FILE_NOTIFY_CHANGE = 4
FILE_NOTIFY_CHANGE_SIZE: win32more.Windows.Win32.Storage.FileSystem.FILE_NOTIFY_CHANGE = 8
FILE_NOTIFY_CHANGE_LAST_WRITE: win32more.Windows.Win32.Storage.FileSystem.FILE_NOTIFY_CHANGE = 16
FILE_NOTIFY_CHANGE_LAST_ACCESS: win32more.Windows.Win32.Storage.FileSystem.FILE_NOTIFY_CHANGE = 32
FILE_NOTIFY_CHANGE_CREATION: win32more.Windows.Win32.Storage.FileSystem.FILE_NOTIFY_CHANGE = 64
FILE_NOTIFY_CHANGE_SECURITY: win32more.Windows.Win32.Storage.FileSystem.FILE_NOTIFY_CHANGE = 256
class FILE_NOTIFY_EXTENDED_INFORMATION(Structure):
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
    class _Anonymous_e__Union(Union):
        ReparsePointTag: UInt32
        EaSize: UInt32
class FILE_NOTIFY_INFORMATION(Structure):
    NextEntryOffset: UInt32
    Action: win32more.Windows.Win32.Storage.FileSystem.FILE_ACTION
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
                ShareFlags: UInt32
class FILE_RENAME_INFO(Structure):
    Anonymous: _Anonymous_e__Union
    RootDirectory: win32more.Windows.Win32.Foundation.HANDLE
    FileNameLength: UInt32
    FileName: Char * 1
    class _Anonymous_e__Union(Union):
        ReplaceIfExists: win32more.Windows.Win32.Foundation.BOOLEAN
        Flags: UInt32
class FILE_SEGMENT_ELEMENT(Union):
    Buffer: VoidPtr
    Alignment: UInt64
FILE_SHARE_MODE = UInt32
FILE_SHARE_NONE: win32more.Windows.Win32.Storage.FileSystem.FILE_SHARE_MODE = 0
FILE_SHARE_DELETE: win32more.Windows.Win32.Storage.FileSystem.FILE_SHARE_MODE = 4
FILE_SHARE_READ: win32more.Windows.Win32.Storage.FileSystem.FILE_SHARE_MODE = 1
FILE_SHARE_WRITE: win32more.Windows.Win32.Storage.FileSystem.FILE_SHARE_MODE = 2
class FILE_STANDARD_INFO(Structure):
    AllocationSize: Int64
    EndOfFile: Int64
    NumberOfLinks: UInt32
    DeletePending: win32more.Windows.Win32.Foundation.BOOLEAN
    Directory: win32more.Windows.Win32.Foundation.BOOLEAN
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
    StreamSize: Int64
    StreamAllocationSize: Int64
    StreamName: Char * 1
FILE_TYPE = UInt32
FILE_TYPE_UNKNOWN: win32more.Windows.Win32.Storage.FileSystem.FILE_TYPE = 0
FILE_TYPE_DISK: win32more.Windows.Win32.Storage.FileSystem.FILE_TYPE = 1
FILE_TYPE_CHAR: win32more.Windows.Win32.Storage.FileSystem.FILE_TYPE = 2
FILE_TYPE_PIPE: win32more.Windows.Win32.Storage.FileSystem.FILE_TYPE = 3
FILE_TYPE_REMOTE: win32more.Windows.Win32.Storage.FileSystem.FILE_TYPE = 32768
FILE_WRITE_FLAGS = Int32
FILE_WRITE_FLAGS_NONE: win32more.Windows.Win32.Storage.FileSystem.FILE_WRITE_FLAGS = 0
FILE_WRITE_FLAGS_WRITE_THROUGH: win32more.Windows.Win32.Storage.FileSystem.FILE_WRITE_FLAGS = 1
FINDEX_INFO_LEVELS = Int32
FindExInfoStandard: win32more.Windows.Win32.Storage.FileSystem.FINDEX_INFO_LEVELS = 0
FindExInfoBasic: win32more.Windows.Win32.Storage.FileSystem.FINDEX_INFO_LEVELS = 1
FindExInfoMaxInfoLevel: win32more.Windows.Win32.Storage.FileSystem.FINDEX_INFO_LEVELS = 2
FINDEX_SEARCH_OPS = Int32
FindExSearchNameMatch: win32more.Windows.Win32.Storage.FileSystem.FINDEX_SEARCH_OPS = 0
FindExSearchLimitToDirectories: win32more.Windows.Win32.Storage.FileSystem.FINDEX_SEARCH_OPS = 1
FindExSearchLimitToDevices: win32more.Windows.Win32.Storage.FileSystem.FINDEX_SEARCH_OPS = 2
FindExSearchMaxSearchOp: win32more.Windows.Win32.Storage.FileSystem.FINDEX_SEARCH_OPS = 3
FIND_FIRST_EX_FLAGS = UInt32
FIND_FIRST_EX_CASE_SENSITIVE: win32more.Windows.Win32.Storage.FileSystem.FIND_FIRST_EX_FLAGS = 1
FIND_FIRST_EX_LARGE_FETCH: win32more.Windows.Win32.Storage.FileSystem.FIND_FIRST_EX_FLAGS = 2
FIND_FIRST_EX_ON_DISK_ENTRIES_ONLY: win32more.Windows.Win32.Storage.FileSystem.FIND_FIRST_EX_FLAGS = 4
class FIO_CONTEXT(Structure):
    m_dwTempHack: UInt32
    m_dwSignature: UInt32
    m_hFile: win32more.Windows.Win32.Foundation.HANDLE
    m_dwLinesOffset: UInt32
    m_dwHeaderLength: UInt32
GETFINALPATHNAMEBYHANDLE_FLAGS = UInt32
VOLUME_NAME_DOS: win32more.Windows.Win32.Storage.FileSystem.GETFINALPATHNAMEBYHANDLE_FLAGS = 0
VOLUME_NAME_GUID: win32more.Windows.Win32.Storage.FileSystem.GETFINALPATHNAMEBYHANDLE_FLAGS = 1
VOLUME_NAME_NT: win32more.Windows.Win32.Storage.FileSystem.GETFINALPATHNAMEBYHANDLE_FLAGS = 2
VOLUME_NAME_NONE: win32more.Windows.Win32.Storage.FileSystem.GETFINALPATHNAMEBYHANDLE_FLAGS = 4
FILE_NAME_NORMALIZED: win32more.Windows.Win32.Storage.FileSystem.GETFINALPATHNAMEBYHANDLE_FLAGS = 0
FILE_NAME_OPENED: win32more.Windows.Win32.Storage.FileSystem.GETFINALPATHNAMEBYHANDLE_FLAGS = 8
GET_FILEEX_INFO_LEVELS = Int32
GetFileExInfoStandard: win32more.Windows.Win32.Storage.FileSystem.GET_FILEEX_INFO_LEVELS = 0
GetFileExMaxInfoLevel: win32more.Windows.Win32.Storage.FileSystem.GET_FILEEX_INFO_LEVELS = 1
GET_FILE_VERSION_INFO_FLAGS = UInt32
FILE_VER_GET_LOCALISED: win32more.Windows.Win32.Storage.FileSystem.GET_FILE_VERSION_INFO_FLAGS = 1
FILE_VER_GET_NEUTRAL: win32more.Windows.Win32.Storage.FileSystem.GET_FILE_VERSION_INFO_FLAGS = 2
FILE_VER_GET_PREFETCHED: win32more.Windows.Win32.Storage.FileSystem.GET_FILE_VERSION_INFO_FLAGS = 4
GET_TAPE_DRIVE_PARAMETERS_OPERATION = UInt32
GET_TAPE_DRIVE_INFORMATION: win32more.Windows.Win32.Storage.FileSystem.GET_TAPE_DRIVE_PARAMETERS_OPERATION = 1
GET_TAPE_MEDIA_INFORMATION: win32more.Windows.Win32.Storage.FileSystem.GET_TAPE_DRIVE_PARAMETERS_OPERATION = 0
HIORING = VoidPtr
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
    def AddUserSid(self, pUserSid: win32more.Windows.Win32.Security.PSID, fNameResolution: win32more.Windows.Win32.Storage.FileSystem.DISKQUOTA_USERNAME_RESOLVE, ppUser: POINTER(win32more.Windows.Win32.Storage.FileSystem.IDiskQuotaUser)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def AddUserName(self, pszLogonName: win32more.Windows.Win32.Foundation.PWSTR, fNameResolution: win32more.Windows.Win32.Storage.FileSystem.DISKQUOTA_USERNAME_RESOLVE, ppUser: POINTER(win32more.Windows.Win32.Storage.FileSystem.IDiskQuotaUser)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def DeleteUser(self, pUser: win32more.Windows.Win32.Storage.FileSystem.IDiskQuotaUser) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def FindUserSid(self, pUserSid: win32more.Windows.Win32.Security.PSID, fNameResolution: win32more.Windows.Win32.Storage.FileSystem.DISKQUOTA_USERNAME_RESOLVE, ppUser: POINTER(win32more.Windows.Win32.Storage.FileSystem.IDiskQuotaUser)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def FindUserName(self, pszLogonName: win32more.Windows.Win32.Foundation.PWSTR, ppUser: POINTER(win32more.Windows.Win32.Storage.FileSystem.IDiskQuotaUser)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def CreateEnumUsers(self, rgpUserSids: POINTER(win32more.Windows.Win32.Security.PSID), cpSids: UInt32, fNameResolution: win32more.Windows.Win32.Storage.FileSystem.DISKQUOTA_USERNAME_RESOLVE, ppEnum: POINTER(win32more.Windows.Win32.Storage.FileSystem.IEnumDiskQuotaUsers)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def CreateUserBatch(self, ppBatch: POINTER(win32more.Windows.Win32.Storage.FileSystem.IDiskQuotaUserBatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def InvalidateSidNameCache(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GiveUserNameResolutionPriority(self, pUser: win32more.Windows.Win32.Storage.FileSystem.IDiskQuotaUser) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def ShutdownNameResolution(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDiskQuotaEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7988b579-ec89-11cf-9c00-00aa00a14f56}')
    @commethod(3)
    def OnUserNameChanged(self, pUser: win32more.Windows.Win32.Storage.FileSystem.IDiskQuotaUser) -> win32more.Windows.Win32.Foundation.HRESULT: ...
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
    def Add(self, pUser: win32more.Windows.Win32.Storage.FileSystem.IDiskQuotaUser) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Remove(self, pUser: win32more.Windows.Win32.Storage.FileSystem.IDiskQuotaUser) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RemoveAll(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def FlushToDisk(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumDiskQuotaUsers(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7988b577-ec89-11cf-9c00-00aa00a14f56}')
    @commethod(3)
    def Next(self, cUsers: UInt32, rgUsers: POINTER(win32more.Windows.Win32.Storage.FileSystem.IDiskQuotaUser), pcUsersFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, cUsers: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.Storage.FileSystem.IEnumDiskQuotaUsers)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IORING_BUFFER_INFO(Structure):
    Address: VoidPtr
    Length: UInt32
class IORING_BUFFER_REF(Structure):
    Kind: win32more.Windows.Win32.Storage.FileSystem.IORING_REF_KIND
    Buffer: BufferUnion
    class BufferUnion(Union):
        Address: VoidPtr
        IndexAndOffset: win32more.Windows.Win32.Storage.FileSystem.IORING_REGISTERED_BUFFER
class IORING_CAPABILITIES(Structure):
    MaxVersion: win32more.Windows.Win32.Storage.FileSystem.IORING_VERSION
    MaxSubmissionQueueSize: UInt32
    MaxCompletionQueueSize: UInt32
    FeatureFlags: win32more.Windows.Win32.Storage.FileSystem.IORING_FEATURE_FLAGS
class IORING_CQE(Structure):
    UserData: UIntPtr
    ResultCode: win32more.Windows.Win32.Foundation.HRESULT
    Information: UIntPtr
IORING_CREATE_ADVISORY_FLAGS = Int32
IORING_CREATE_ADVISORY_FLAGS_NONE: win32more.Windows.Win32.Storage.FileSystem.IORING_CREATE_ADVISORY_FLAGS = 0
class IORING_CREATE_FLAGS(Structure):
    Required: win32more.Windows.Win32.Storage.FileSystem.IORING_CREATE_REQUIRED_FLAGS
    Advisory: win32more.Windows.Win32.Storage.FileSystem.IORING_CREATE_ADVISORY_FLAGS
IORING_CREATE_REQUIRED_FLAGS = Int32
IORING_CREATE_REQUIRED_FLAGS_NONE: win32more.Windows.Win32.Storage.FileSystem.IORING_CREATE_REQUIRED_FLAGS = 0
IORING_FEATURE_FLAGS = Int32
IORING_FEATURE_FLAGS_NONE: win32more.Windows.Win32.Storage.FileSystem.IORING_FEATURE_FLAGS = 0
IORING_FEATURE_UM_EMULATION: win32more.Windows.Win32.Storage.FileSystem.IORING_FEATURE_FLAGS = 1
IORING_FEATURE_SET_COMPLETION_EVENT: win32more.Windows.Win32.Storage.FileSystem.IORING_FEATURE_FLAGS = 2
class IORING_HANDLE_REF(Structure):
    Kind: win32more.Windows.Win32.Storage.FileSystem.IORING_REF_KIND
    Handle: HandleUnion
    class HandleUnion(Union):
        Handle: win32more.Windows.Win32.Foundation.HANDLE
        Index: UInt32
class IORING_INFO(Structure):
    IoRingVersion: win32more.Windows.Win32.Storage.FileSystem.IORING_VERSION
    Flags: win32more.Windows.Win32.Storage.FileSystem.IORING_CREATE_FLAGS
    SubmissionQueueSize: UInt32
    CompletionQueueSize: UInt32
IORING_OP_CODE = Int32
IORING_OP_NOP: win32more.Windows.Win32.Storage.FileSystem.IORING_OP_CODE = 0
IORING_OP_READ: win32more.Windows.Win32.Storage.FileSystem.IORING_OP_CODE = 1
IORING_OP_REGISTER_FILES: win32more.Windows.Win32.Storage.FileSystem.IORING_OP_CODE = 2
IORING_OP_REGISTER_BUFFERS: win32more.Windows.Win32.Storage.FileSystem.IORING_OP_CODE = 3
IORING_OP_CANCEL: win32more.Windows.Win32.Storage.FileSystem.IORING_OP_CODE = 4
IORING_OP_WRITE: win32more.Windows.Win32.Storage.FileSystem.IORING_OP_CODE = 5
IORING_OP_FLUSH: win32more.Windows.Win32.Storage.FileSystem.IORING_OP_CODE = 6
IORING_REF_KIND = Int32
IORING_REF_RAW: win32more.Windows.Win32.Storage.FileSystem.IORING_REF_KIND = 0
IORING_REF_REGISTERED: win32more.Windows.Win32.Storage.FileSystem.IORING_REF_KIND = 1
class IORING_REGISTERED_BUFFER(Structure):
    BufferIndex: UInt32
    Offset: UInt32
IORING_SQE_FLAGS = Int32
IOSQE_FLAGS_NONE: win32more.Windows.Win32.Storage.FileSystem.IORING_SQE_FLAGS = 0
IOSQE_FLAGS_DRAIN_PRECEDING_OPS: win32more.Windows.Win32.Storage.FileSystem.IORING_SQE_FLAGS = 1
IORING_VERSION = Int32
IORING_VERSION_INVALID: win32more.Windows.Win32.Storage.FileSystem.IORING_VERSION = 0
IORING_VERSION_1: win32more.Windows.Win32.Storage.FileSystem.IORING_VERSION = 1
IORING_VERSION_2: win32more.Windows.Win32.Storage.FileSystem.IORING_VERSION = 2
IORING_VERSION_3: win32more.Windows.Win32.Storage.FileSystem.IORING_VERSION = 300
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
LOCKFILE_EXCLUSIVE_LOCK: win32more.Windows.Win32.Storage.FileSystem.LOCK_FILE_FLAGS = 2
LOCKFILE_FAIL_IMMEDIATELY: win32more.Windows.Win32.Storage.FileSystem.LOCK_FILE_FLAGS = 1
class LOG_MANAGEMENT_CALLBACKS(Structure):
    CallbackContext: VoidPtr
    AdvanceTailCallback: win32more.Windows.Win32.Storage.FileSystem.PLOG_TAIL_ADVANCE_CALLBACK
    LogFullHandlerCallback: win32more.Windows.Win32.Storage.FileSystem.PLOG_FULL_HANDLER_CALLBACK
    LogUnpinnedCallback: win32more.Windows.Win32.Storage.FileSystem.PLOG_UNPINNED_CALLBACK
@winfunctype_pointer
def LPPROGRESS_ROUTINE(TotalFileSize: Int64, TotalBytesTransferred: Int64, StreamSize: Int64, StreamBytesTransferred: Int64, dwStreamNumber: UInt32, dwCallbackReason: win32more.Windows.Win32.Storage.FileSystem.LPPROGRESS_ROUTINE_CALLBACK_REASON, hSourceFile: win32more.Windows.Win32.Foundation.HANDLE, hDestinationFile: win32more.Windows.Win32.Foundation.HANDLE, lpData: VoidPtr) -> win32more.Windows.Win32.Storage.FileSystem.COPYPROGRESSROUTINE_PROGRESS: ...
LPPROGRESS_ROUTINE_CALLBACK_REASON = UInt32
CALLBACK_CHUNK_FINISHED: win32more.Windows.Win32.Storage.FileSystem.LPPROGRESS_ROUTINE_CALLBACK_REASON = 0
CALLBACK_STREAM_SWITCH: win32more.Windows.Win32.Storage.FileSystem.LPPROGRESS_ROUTINE_CALLBACK_REASON = 1
LZOPENFILE_STYLE = UInt16
OF_CANCEL: win32more.Windows.Win32.Storage.FileSystem.LZOPENFILE_STYLE = 2048
OF_CREATE: win32more.Windows.Win32.Storage.FileSystem.LZOPENFILE_STYLE = 4096
OF_DELETE: win32more.Windows.Win32.Storage.FileSystem.LZOPENFILE_STYLE = 512
OF_EXIST: win32more.Windows.Win32.Storage.FileSystem.LZOPENFILE_STYLE = 16384
OF_PARSE: win32more.Windows.Win32.Storage.FileSystem.LZOPENFILE_STYLE = 256
OF_PROMPT: win32more.Windows.Win32.Storage.FileSystem.LZOPENFILE_STYLE = 8192
OF_READ: win32more.Windows.Win32.Storage.FileSystem.LZOPENFILE_STYLE = 0
OF_READWRITE: win32more.Windows.Win32.Storage.FileSystem.LZOPENFILE_STYLE = 2
OF_REOPEN: win32more.Windows.Win32.Storage.FileSystem.LZOPENFILE_STYLE = 32768
OF_SHARE_DENY_NONE: win32more.Windows.Win32.Storage.FileSystem.LZOPENFILE_STYLE = 64
OF_SHARE_DENY_READ: win32more.Windows.Win32.Storage.FileSystem.LZOPENFILE_STYLE = 48
OF_SHARE_DENY_WRITE: win32more.Windows.Win32.Storage.FileSystem.LZOPENFILE_STYLE = 32
OF_SHARE_EXCLUSIVE: win32more.Windows.Win32.Storage.FileSystem.LZOPENFILE_STYLE = 16
OF_WRITE: win32more.Windows.Win32.Storage.FileSystem.LZOPENFILE_STYLE = 1
OF_SHARE_COMPAT: win32more.Windows.Win32.Storage.FileSystem.LZOPENFILE_STYLE = 0
OF_VERIFY: win32more.Windows.Win32.Storage.FileSystem.LZOPENFILE_STYLE = 1024
@winfunctype_pointer
def MAXMEDIALABEL(pMaxSize: POINTER(UInt32)) -> UInt32: ...
MOVE_FILE_FLAGS = UInt32
MOVEFILE_COPY_ALLOWED: win32more.Windows.Win32.Storage.FileSystem.MOVE_FILE_FLAGS = 2
MOVEFILE_CREATE_HARDLINK: win32more.Windows.Win32.Storage.FileSystem.MOVE_FILE_FLAGS = 16
MOVEFILE_DELAY_UNTIL_REBOOT: win32more.Windows.Win32.Storage.FileSystem.MOVE_FILE_FLAGS = 4
MOVEFILE_REPLACE_EXISTING: win32more.Windows.Win32.Storage.FileSystem.MOVE_FILE_FLAGS = 1
MOVEFILE_WRITE_THROUGH: win32more.Windows.Win32.Storage.FileSystem.MOVE_FILE_FLAGS = 8
MOVEFILE_FAIL_IF_NOT_TRACKABLE: win32more.Windows.Win32.Storage.FileSystem.MOVE_FILE_FLAGS = 32
class MediaLabelInfo(Structure):
    LabelType: Char * 64
    LabelIDSize: UInt32
    LabelID: Byte * 256
    LabelAppDescr: Char * 256
class NAME_CACHE_CONTEXT(Structure):
    m_dwSignature: UInt32
class NTMS_ALLOCATION_INFORMATION(Structure):
    dwSize: UInt32
    lpReserved: VoidPtr
    AllocatedFrom: Guid
class NTMS_ASYNC_IO(Structure):
    OperationId: Guid
    EventId: Guid
    dwOperationType: UInt32
    dwResult: UInt32
    dwAsyncState: UInt32
    hEvent: win32more.Windows.Win32.Foundation.HANDLE
    bOnStateChange: win32more.Windows.Win32.Foundation.BOOL
class NTMS_CHANGERINFORMATIONA(Structure):
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
NTMS_CHANGERINFORMATION = UnicodeAlias('NTMS_CHANGERINFORMATIONW')
class NTMS_CHANGERTYPEINFORMATIONA(Structure):
    szVendor: win32more.Windows.Win32.Foundation.CHAR * 128
    szProduct: win32more.Windows.Win32.Foundation.CHAR * 128
    DeviceType: UInt32
class NTMS_CHANGERTYPEINFORMATIONW(Structure):
    szVendor: Char * 128
    szProduct: Char * 128
    DeviceType: UInt32
NTMS_CHANGERTYPEINFORMATION = UnicodeAlias('NTMS_CHANGERTYPEINFORMATIONW')
class NTMS_COMPUTERINFORMATION(Structure):
    dwLibRequestPurgeTime: UInt32
    dwOpRequestPurgeTime: UInt32
    dwLibRequestFlags: UInt32
    dwOpRequestFlags: UInt32
    dwMediaPoolPolicy: UInt32
class NTMS_DRIVEINFORMATIONA(Structure):
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
class NTMS_DRIVEINFORMATIONW(Structure):
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
NTMS_DRIVEINFORMATION = UnicodeAlias('NTMS_DRIVEINFORMATIONW')
class NTMS_DRIVETYPEINFORMATIONA(Structure):
    szVendor: win32more.Windows.Win32.Foundation.CHAR * 128
    szProduct: win32more.Windows.Win32.Foundation.CHAR * 128
    NumberOfHeads: UInt32
    DeviceType: win32more.Windows.Win32.Storage.FileSystem.FILE_DEVICE_TYPE
class NTMS_DRIVETYPEINFORMATIONW(Structure):
    szVendor: Char * 128
    szProduct: Char * 128
    NumberOfHeads: UInt32
    DeviceType: win32more.Windows.Win32.Storage.FileSystem.FILE_DEVICE_TYPE
NTMS_DRIVETYPEINFORMATION = UnicodeAlias('NTMS_DRIVETYPEINFORMATIONW')
class NTMS_FILESYSTEM_INFO(Structure):
    FileSystemType: Char * 64
    VolumeName: Char * 256
    SerialNumber: UInt32
class NTMS_I1_LIBRARYINFORMATION(Structure):
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
class NTMS_I1_LIBREQUESTINFORMATIONA(Structure):
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
class NTMS_I1_LIBREQUESTINFORMATIONW(Structure):
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
NTMS_I1_LIBREQUESTINFORMATION = UnicodeAlias('NTMS_I1_LIBREQUESTINFORMATIONW')
class NTMS_I1_OBJECTINFORMATIONA(Structure):
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
    class _Info_e__Union(Union):
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
class NTMS_I1_OBJECTINFORMATIONW(Structure):
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
    class _Info_e__Union(Union):
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
NTMS_I1_OBJECTINFORMATION = UnicodeAlias('NTMS_I1_OBJECTINFORMATIONW')
class NTMS_I1_OPREQUESTINFORMATIONA(Structure):
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
class NTMS_I1_OPREQUESTINFORMATIONW(Structure):
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
NTMS_I1_OPREQUESTINFORMATION = UnicodeAlias('NTMS_I1_OPREQUESTINFORMATIONW')
class NTMS_I1_PARTITIONINFORMATIONA(Structure):
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
NTMS_I1_PARTITIONINFORMATION = UnicodeAlias('NTMS_I1_PARTITIONINFORMATIONW')
class NTMS_I1_PMIDINFORMATIONA(Structure):
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
NTMS_I1_PMIDINFORMATION = UnicodeAlias('NTMS_I1_PMIDINFORMATIONW')
class NTMS_IEDOORINFORMATION(Structure):
    Number: UInt32
    State: UInt32
    MaxOpenSecs: UInt16
    Library: Guid
class NTMS_IEPORTINFORMATION(Structure):
    Number: UInt32
    Content: UInt32
    Position: UInt32
    MaxExtendSecs: UInt16
    Library: Guid
class NTMS_LIBRARYINFORMATION(Structure):
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
class NTMS_LIBREQUESTINFORMATIONA(Structure):
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
class NTMS_LIBREQUESTINFORMATIONW(Structure):
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
NTMS_LIBREQUESTINFORMATION = UnicodeAlias('NTMS_LIBREQUESTINFORMATIONW')
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
    ReadWriteCharacteristics: UInt32
    DeviceType: win32more.Windows.Win32.Storage.FileSystem.FILE_DEVICE_TYPE
class NTMS_MOUNT_INFORMATION(Structure):
    dwSize: UInt32
    lpReserved: VoidPtr
class NTMS_NOTIFICATIONINFORMATION(Structure):
    dwOperation: UInt32
    ObjectId: Guid
class NTMS_OBJECTINFORMATIONA(Structure):
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
    class _Info_e__Union(Union):
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
class NTMS_OBJECTINFORMATIONW(Structure):
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
    class _Info_e__Union(Union):
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
NTMS_OBJECTINFORMATION = UnicodeAlias('NTMS_OBJECTINFORMATIONW')
NTMS_OMID_TYPE = UInt32
NTMS_OMID_TYPE_FILESYSTEM_INFO: win32more.Windows.Win32.Storage.FileSystem.NTMS_OMID_TYPE = 2
NTMS_OMID_TYPE_RAW_LABEL: win32more.Windows.Win32.Storage.FileSystem.NTMS_OMID_TYPE = 1
class NTMS_OPREQUESTINFORMATIONA(Structure):
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
class NTMS_OPREQUESTINFORMATIONW(Structure):
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
NTMS_OPREQUESTINFORMATION = UnicodeAlias('NTMS_OPREQUESTINFORMATIONW')
class NTMS_PARTITIONINFORMATIONA(Structure):
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
class NTMS_PARTITIONINFORMATIONW(Structure):
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
NTMS_PARTITIONINFORMATION = UnicodeAlias('NTMS_PARTITIONINFORMATIONW')
class NTMS_PMIDINFORMATIONA(Structure):
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
class NTMS_PMIDINFORMATIONW(Structure):
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
NTMS_PMIDINFORMATION = UnicodeAlias('NTMS_PMIDINFORMATIONW')
class NTMS_STORAGESLOTINFORMATION(Structure):
    Number: UInt32
    State: UInt32
    Library: Guid
NtmsAccessMask = Int32
NTMS_USE_ACCESS: win32more.Windows.Win32.Storage.FileSystem.NtmsAccessMask = 1
NTMS_MODIFY_ACCESS: win32more.Windows.Win32.Storage.FileSystem.NtmsAccessMask = 2
NTMS_CONTROL_ACCESS: win32more.Windows.Win32.Storage.FileSystem.NtmsAccessMask = 4
NtmsAllocateOptions = Int32
NTMS_ALLOCATE_NEW: win32more.Windows.Win32.Storage.FileSystem.NtmsAllocateOptions = 1
NTMS_ALLOCATE_NEXT: win32more.Windows.Win32.Storage.FileSystem.NtmsAllocateOptions = 2
NTMS_ALLOCATE_ERROR_IF_UNAVAILABLE: win32more.Windows.Win32.Storage.FileSystem.NtmsAllocateOptions = 4
NtmsAllocationPolicy = Int32
NTMS_ALLOCATE_FROMSCRATCH: win32more.Windows.Win32.Storage.FileSystem.NtmsAllocationPolicy = 1
NtmsAsyncOperations = Int32
NTMS_ASYNCOP_MOUNT: win32more.Windows.Win32.Storage.FileSystem.NtmsAsyncOperations = 1
NtmsAsyncStatus = Int32
NTMS_ASYNCSTATE_QUEUED: win32more.Windows.Win32.Storage.FileSystem.NtmsAsyncStatus = 0
NTMS_ASYNCSTATE_WAIT_RESOURCE: win32more.Windows.Win32.Storage.FileSystem.NtmsAsyncStatus = 1
NTMS_ASYNCSTATE_WAIT_OPERATOR: win32more.Windows.Win32.Storage.FileSystem.NtmsAsyncStatus = 2
NTMS_ASYNCSTATE_INPROCESS: win32more.Windows.Win32.Storage.FileSystem.NtmsAsyncStatus = 3
NTMS_ASYNCSTATE_COMPLETE: win32more.Windows.Win32.Storage.FileSystem.NtmsAsyncStatus = 4
NtmsBarCodeState = Int32
NTMS_BARCODESTATE_OK: win32more.Windows.Win32.Storage.FileSystem.NtmsBarCodeState = 1
NTMS_BARCODESTATE_UNREADABLE: win32more.Windows.Win32.Storage.FileSystem.NtmsBarCodeState = 2
NtmsCreateNtmsMediaOptions = Int32
NTMS_ERROR_ON_DUPLICATE: win32more.Windows.Win32.Storage.FileSystem.NtmsCreateNtmsMediaOptions = 1
NtmsCreateOptions = Int32
NTMS_OPEN_EXISTING: win32more.Windows.Win32.Storage.FileSystem.NtmsCreateOptions = 1
NTMS_CREATE_NEW: win32more.Windows.Win32.Storage.FileSystem.NtmsCreateOptions = 2
NTMS_OPEN_ALWAYS: win32more.Windows.Win32.Storage.FileSystem.NtmsCreateOptions = 3
NtmsDeallocationPolicy = Int32
NTMS_DEALLOCATE_TOSCRATCH: win32more.Windows.Win32.Storage.FileSystem.NtmsDeallocationPolicy = 1
NtmsDismountOptions = Int32
NTMS_DISMOUNT_DEFERRED: win32more.Windows.Win32.Storage.FileSystem.NtmsDismountOptions = 1
NTMS_DISMOUNT_IMMEDIATE: win32more.Windows.Win32.Storage.FileSystem.NtmsDismountOptions = 2
NtmsDoorState = Int32
NTMS_DOORSTATE_UNKNOWN: win32more.Windows.Win32.Storage.FileSystem.NtmsDoorState = 0
NTMS_DOORSTATE_CLOSED: win32more.Windows.Win32.Storage.FileSystem.NtmsDoorState = 1
NTMS_DOORSTATE_OPEN: win32more.Windows.Win32.Storage.FileSystem.NtmsDoorState = 2
NtmsDriveState = Int32
NTMS_DRIVESTATE_DISMOUNTED: win32more.Windows.Win32.Storage.FileSystem.NtmsDriveState = 0
NTMS_DRIVESTATE_MOUNTED: win32more.Windows.Win32.Storage.FileSystem.NtmsDriveState = 1
NTMS_DRIVESTATE_LOADED: win32more.Windows.Win32.Storage.FileSystem.NtmsDriveState = 2
NTMS_DRIVESTATE_UNLOADED: win32more.Windows.Win32.Storage.FileSystem.NtmsDriveState = 5
NTMS_DRIVESTATE_BEING_CLEANED: win32more.Windows.Win32.Storage.FileSystem.NtmsDriveState = 6
NTMS_DRIVESTATE_DISMOUNTABLE: win32more.Windows.Win32.Storage.FileSystem.NtmsDriveState = 7
NtmsDriveType = Int32
NTMS_UNKNOWN_DRIVE: win32more.Windows.Win32.Storage.FileSystem.NtmsDriveType = 0
NtmsEjectOperation = Int32
NTMS_EJECT_START: win32more.Windows.Win32.Storage.FileSystem.NtmsEjectOperation = 0
NTMS_EJECT_STOP: win32more.Windows.Win32.Storage.FileSystem.NtmsEjectOperation = 1
NTMS_EJECT_QUEUE: win32more.Windows.Win32.Storage.FileSystem.NtmsEjectOperation = 2
NTMS_EJECT_FORCE: win32more.Windows.Win32.Storage.FileSystem.NtmsEjectOperation = 3
NTMS_EJECT_IMMEDIATE: win32more.Windows.Win32.Storage.FileSystem.NtmsEjectOperation = 4
NTMS_EJECT_ASK_USER: win32more.Windows.Win32.Storage.FileSystem.NtmsEjectOperation = 5
NtmsEnumerateOption = Int32
NTMS_ENUM_DEFAULT: win32more.Windows.Win32.Storage.FileSystem.NtmsEnumerateOption = 0
NTMS_ENUM_ROOTPOOL: win32more.Windows.Win32.Storage.FileSystem.NtmsEnumerateOption = 1
NtmsInjectOperation = Int32
NTMS_INJECT_START: win32more.Windows.Win32.Storage.FileSystem.NtmsInjectOperation = 0
NTMS_INJECT_STOP: win32more.Windows.Win32.Storage.FileSystem.NtmsInjectOperation = 1
NTMS_INJECT_RETRACT: win32more.Windows.Win32.Storage.FileSystem.NtmsInjectOperation = 2
NTMS_INJECT_STARTMANY: win32more.Windows.Win32.Storage.FileSystem.NtmsInjectOperation = 3
NtmsInventoryMethod = Int32
NTMS_INVENTORY_NONE: win32more.Windows.Win32.Storage.FileSystem.NtmsInventoryMethod = 0
NTMS_INVENTORY_FAST: win32more.Windows.Win32.Storage.FileSystem.NtmsInventoryMethod = 1
NTMS_INVENTORY_OMID: win32more.Windows.Win32.Storage.FileSystem.NtmsInventoryMethod = 2
NTMS_INVENTORY_DEFAULT: win32more.Windows.Win32.Storage.FileSystem.NtmsInventoryMethod = 3
NTMS_INVENTORY_SLOT: win32more.Windows.Win32.Storage.FileSystem.NtmsInventoryMethod = 4
NTMS_INVENTORY_STOP: win32more.Windows.Win32.Storage.FileSystem.NtmsInventoryMethod = 5
NTMS_INVENTORY_MAX: win32more.Windows.Win32.Storage.FileSystem.NtmsInventoryMethod = 6
NtmsLibRequestFlags = Int32
NTMS_LIBREQFLAGS_NOAUTOPURGE: win32more.Windows.Win32.Storage.FileSystem.NtmsLibRequestFlags = 1
NTMS_LIBREQFLAGS_NOFAILEDPURGE: win32more.Windows.Win32.Storage.FileSystem.NtmsLibRequestFlags = 2
NtmsLibraryFlags = Int32
NTMS_LIBRARYFLAG_FIXEDOFFLINE: win32more.Windows.Win32.Storage.FileSystem.NtmsLibraryFlags = 1
NTMS_LIBRARYFLAG_CLEANERPRESENT: win32more.Windows.Win32.Storage.FileSystem.NtmsLibraryFlags = 2
NTMS_LIBRARYFLAG_AUTODETECTCHANGE: win32more.Windows.Win32.Storage.FileSystem.NtmsLibraryFlags = 4
NTMS_LIBRARYFLAG_IGNORECLEANERUSESREMAINING: win32more.Windows.Win32.Storage.FileSystem.NtmsLibraryFlags = 8
NTMS_LIBRARYFLAG_RECOGNIZECLEANERBARCODE: win32more.Windows.Win32.Storage.FileSystem.NtmsLibraryFlags = 16
NtmsLibraryType = Int32
NTMS_LIBRARYTYPE_UNKNOWN: win32more.Windows.Win32.Storage.FileSystem.NtmsLibraryType = 0
NTMS_LIBRARYTYPE_OFFLINE: win32more.Windows.Win32.Storage.FileSystem.NtmsLibraryType = 1
NTMS_LIBRARYTYPE_ONLINE: win32more.Windows.Win32.Storage.FileSystem.NtmsLibraryType = 2
NTMS_LIBRARYTYPE_STANDALONE: win32more.Windows.Win32.Storage.FileSystem.NtmsLibraryType = 3
NtmsLmOperation = Int32
NTMS_LM_REMOVE: win32more.Windows.Win32.Storage.FileSystem.NtmsLmOperation = 0
NTMS_LM_DISABLECHANGER: win32more.Windows.Win32.Storage.FileSystem.NtmsLmOperation = 1
NTMS_LM_DISABLELIBRARY: win32more.Windows.Win32.Storage.FileSystem.NtmsLmOperation = 1
NTMS_LM_ENABLECHANGER: win32more.Windows.Win32.Storage.FileSystem.NtmsLmOperation = 2
NTMS_LM_ENABLELIBRARY: win32more.Windows.Win32.Storage.FileSystem.NtmsLmOperation = 2
NTMS_LM_DISABLEDRIVE: win32more.Windows.Win32.Storage.FileSystem.NtmsLmOperation = 3
NTMS_LM_ENABLEDRIVE: win32more.Windows.Win32.Storage.FileSystem.NtmsLmOperation = 4
NTMS_LM_DISABLEMEDIA: win32more.Windows.Win32.Storage.FileSystem.NtmsLmOperation = 5
NTMS_LM_ENABLEMEDIA: win32more.Windows.Win32.Storage.FileSystem.NtmsLmOperation = 6
NTMS_LM_UPDATEOMID: win32more.Windows.Win32.Storage.FileSystem.NtmsLmOperation = 7
NTMS_LM_INVENTORY: win32more.Windows.Win32.Storage.FileSystem.NtmsLmOperation = 8
NTMS_LM_DOORACCESS: win32more.Windows.Win32.Storage.FileSystem.NtmsLmOperation = 9
NTMS_LM_EJECT: win32more.Windows.Win32.Storage.FileSystem.NtmsLmOperation = 10
NTMS_LM_EJECTCLEANER: win32more.Windows.Win32.Storage.FileSystem.NtmsLmOperation = 11
NTMS_LM_INJECT: win32more.Windows.Win32.Storage.FileSystem.NtmsLmOperation = 12
NTMS_LM_INJECTCLEANER: win32more.Windows.Win32.Storage.FileSystem.NtmsLmOperation = 13
NTMS_LM_PROCESSOMID: win32more.Windows.Win32.Storage.FileSystem.NtmsLmOperation = 14
NTMS_LM_CLEANDRIVE: win32more.Windows.Win32.Storage.FileSystem.NtmsLmOperation = 15
NTMS_LM_DISMOUNT: win32more.Windows.Win32.Storage.FileSystem.NtmsLmOperation = 16
NTMS_LM_MOUNT: win32more.Windows.Win32.Storage.FileSystem.NtmsLmOperation = 17
NTMS_LM_WRITESCRATCH: win32more.Windows.Win32.Storage.FileSystem.NtmsLmOperation = 18
NTMS_LM_CLASSIFY: win32more.Windows.Win32.Storage.FileSystem.NtmsLmOperation = 19
NTMS_LM_RESERVECLEANER: win32more.Windows.Win32.Storage.FileSystem.NtmsLmOperation = 20
NTMS_LM_RELEASECLEANER: win32more.Windows.Win32.Storage.FileSystem.NtmsLmOperation = 21
NTMS_LM_MAXWORKITEM: win32more.Windows.Win32.Storage.FileSystem.NtmsLmOperation = 22
NtmsLmState = Int32
NTMS_LM_QUEUED: win32more.Windows.Win32.Storage.FileSystem.NtmsLmState = 0
NTMS_LM_INPROCESS: win32more.Windows.Win32.Storage.FileSystem.NtmsLmState = 1
NTMS_LM_PASSED: win32more.Windows.Win32.Storage.FileSystem.NtmsLmState = 2
NTMS_LM_FAILED: win32more.Windows.Win32.Storage.FileSystem.NtmsLmState = 3
NTMS_LM_INVALID: win32more.Windows.Win32.Storage.FileSystem.NtmsLmState = 4
NTMS_LM_WAITING: win32more.Windows.Win32.Storage.FileSystem.NtmsLmState = 5
NTMS_LM_DEFERRED: win32more.Windows.Win32.Storage.FileSystem.NtmsLmState = 6
NTMS_LM_DEFFERED: win32more.Windows.Win32.Storage.FileSystem.NtmsLmState = 6
NTMS_LM_CANCELLED: win32more.Windows.Win32.Storage.FileSystem.NtmsLmState = 7
NTMS_LM_STOPPED: win32more.Windows.Win32.Storage.FileSystem.NtmsLmState = 8
NtmsMediaPoolPolicy = Int32
NTMS_POOLPOLICY_PURGEOFFLINESCRATCH: win32more.Windows.Win32.Storage.FileSystem.NtmsMediaPoolPolicy = 1
NTMS_POOLPOLICY_KEEPOFFLINEIMPORT: win32more.Windows.Win32.Storage.FileSystem.NtmsMediaPoolPolicy = 2
NtmsMediaState = Int32
NTMS_MEDIASTATE_IDLE: win32more.Windows.Win32.Storage.FileSystem.NtmsMediaState = 0
NTMS_MEDIASTATE_INUSE: win32more.Windows.Win32.Storage.FileSystem.NtmsMediaState = 1
NTMS_MEDIASTATE_MOUNTED: win32more.Windows.Win32.Storage.FileSystem.NtmsMediaState = 2
NTMS_MEDIASTATE_LOADED: win32more.Windows.Win32.Storage.FileSystem.NtmsMediaState = 3
NTMS_MEDIASTATE_UNLOADED: win32more.Windows.Win32.Storage.FileSystem.NtmsMediaState = 4
NTMS_MEDIASTATE_OPERROR: win32more.Windows.Win32.Storage.FileSystem.NtmsMediaState = 5
NTMS_MEDIASTATE_OPREQ: win32more.Windows.Win32.Storage.FileSystem.NtmsMediaState = 6
NtmsMountOptions = Int32
NTMS_MOUNT_READ: win32more.Windows.Win32.Storage.FileSystem.NtmsMountOptions = 1
NTMS_MOUNT_WRITE: win32more.Windows.Win32.Storage.FileSystem.NtmsMountOptions = 2
NTMS_MOUNT_ERROR_NOT_AVAILABLE: win32more.Windows.Win32.Storage.FileSystem.NtmsMountOptions = 4
NTMS_MOUNT_ERROR_IF_UNAVAILABLE: win32more.Windows.Win32.Storage.FileSystem.NtmsMountOptions = 4
NTMS_MOUNT_ERROR_OFFLINE: win32more.Windows.Win32.Storage.FileSystem.NtmsMountOptions = 8
NTMS_MOUNT_ERROR_IF_OFFLINE: win32more.Windows.Win32.Storage.FileSystem.NtmsMountOptions = 8
NTMS_MOUNT_SPECIFIC_DRIVE: win32more.Windows.Win32.Storage.FileSystem.NtmsMountOptions = 16
NTMS_MOUNT_NOWAIT: win32more.Windows.Win32.Storage.FileSystem.NtmsMountOptions = 32
NtmsMountPriority = Int32
NTMS_PRIORITY_DEFAULT: win32more.Windows.Win32.Storage.FileSystem.NtmsMountPriority = 0
NTMS_PRIORITY_HIGHEST: win32more.Windows.Win32.Storage.FileSystem.NtmsMountPriority = 15
NTMS_PRIORITY_HIGH: win32more.Windows.Win32.Storage.FileSystem.NtmsMountPriority = 7
NTMS_PRIORITY_NORMAL: win32more.Windows.Win32.Storage.FileSystem.NtmsMountPriority = 0
NTMS_PRIORITY_LOW: win32more.Windows.Win32.Storage.FileSystem.NtmsMountPriority = -7
NTMS_PRIORITY_LOWEST: win32more.Windows.Win32.Storage.FileSystem.NtmsMountPriority = -15
NtmsNotificationOperations = Int32
NTMS_OBJ_UPDATE: win32more.Windows.Win32.Storage.FileSystem.NtmsNotificationOperations = 1
NTMS_OBJ_INSERT: win32more.Windows.Win32.Storage.FileSystem.NtmsNotificationOperations = 2
NTMS_OBJ_DELETE: win32more.Windows.Win32.Storage.FileSystem.NtmsNotificationOperations = 3
NTMS_EVENT_SIGNAL: win32more.Windows.Win32.Storage.FileSystem.NtmsNotificationOperations = 4
NTMS_EVENT_COMPLETE: win32more.Windows.Win32.Storage.FileSystem.NtmsNotificationOperations = 5
NtmsObjectsTypes = Int32
NTMS_UNKNOWN: win32more.Windows.Win32.Storage.FileSystem.NtmsObjectsTypes = 0
NTMS_OBJECT: win32more.Windows.Win32.Storage.FileSystem.NtmsObjectsTypes = 1
NTMS_CHANGER: win32more.Windows.Win32.Storage.FileSystem.NtmsObjectsTypes = 2
NTMS_CHANGER_TYPE: win32more.Windows.Win32.Storage.FileSystem.NtmsObjectsTypes = 3
NTMS_COMPUTER: win32more.Windows.Win32.Storage.FileSystem.NtmsObjectsTypes = 4
NTMS_DRIVE: win32more.Windows.Win32.Storage.FileSystem.NtmsObjectsTypes = 5
NTMS_DRIVE_TYPE: win32more.Windows.Win32.Storage.FileSystem.NtmsObjectsTypes = 6
NTMS_IEDOOR: win32more.Windows.Win32.Storage.FileSystem.NtmsObjectsTypes = 7
NTMS_IEPORT: win32more.Windows.Win32.Storage.FileSystem.NtmsObjectsTypes = 8
NTMS_LIBRARY: win32more.Windows.Win32.Storage.FileSystem.NtmsObjectsTypes = 9
NTMS_LIBREQUEST: win32more.Windows.Win32.Storage.FileSystem.NtmsObjectsTypes = 10
NTMS_LOGICAL_MEDIA: win32more.Windows.Win32.Storage.FileSystem.NtmsObjectsTypes = 11
NTMS_MEDIA_POOL: win32more.Windows.Win32.Storage.FileSystem.NtmsObjectsTypes = 12
NTMS_MEDIA_TYPE: win32more.Windows.Win32.Storage.FileSystem.NtmsObjectsTypes = 13
NTMS_PARTITION: win32more.Windows.Win32.Storage.FileSystem.NtmsObjectsTypes = 14
NTMS_PHYSICAL_MEDIA: win32more.Windows.Win32.Storage.FileSystem.NtmsObjectsTypes = 15
NTMS_STORAGESLOT: win32more.Windows.Win32.Storage.FileSystem.NtmsObjectsTypes = 16
NTMS_OPREQUEST: win32more.Windows.Win32.Storage.FileSystem.NtmsObjectsTypes = 17
NTMS_UI_DESTINATION: win32more.Windows.Win32.Storage.FileSystem.NtmsObjectsTypes = 18
NTMS_NUMBER_OF_OBJECT_TYPES: win32more.Windows.Win32.Storage.FileSystem.NtmsObjectsTypes = 19
NtmsOpRequestFlags = Int32
NTMS_OPREQFLAGS_NOAUTOPURGE: win32more.Windows.Win32.Storage.FileSystem.NtmsOpRequestFlags = 1
NTMS_OPREQFLAGS_NOFAILEDPURGE: win32more.Windows.Win32.Storage.FileSystem.NtmsOpRequestFlags = 2
NTMS_OPREQFLAGS_NOALERTS: win32more.Windows.Win32.Storage.FileSystem.NtmsOpRequestFlags = 16
NTMS_OPREQFLAGS_NOTRAYICON: win32more.Windows.Win32.Storage.FileSystem.NtmsOpRequestFlags = 32
NtmsOperationalState = Int32
NTMS_READY: win32more.Windows.Win32.Storage.FileSystem.NtmsOperationalState = 0
NTMS_INITIALIZING: win32more.Windows.Win32.Storage.FileSystem.NtmsOperationalState = 10
NTMS_NEEDS_SERVICE: win32more.Windows.Win32.Storage.FileSystem.NtmsOperationalState = 20
NTMS_NOT_PRESENT: win32more.Windows.Win32.Storage.FileSystem.NtmsOperationalState = 21
NtmsOpreqCommand = Int32
NTMS_OPREQ_UNKNOWN: win32more.Windows.Win32.Storage.FileSystem.NtmsOpreqCommand = 0
NTMS_OPREQ_NEWMEDIA: win32more.Windows.Win32.Storage.FileSystem.NtmsOpreqCommand = 1
NTMS_OPREQ_CLEANER: win32more.Windows.Win32.Storage.FileSystem.NtmsOpreqCommand = 2
NTMS_OPREQ_DEVICESERVICE: win32more.Windows.Win32.Storage.FileSystem.NtmsOpreqCommand = 3
NTMS_OPREQ_MOVEMEDIA: win32more.Windows.Win32.Storage.FileSystem.NtmsOpreqCommand = 4
NTMS_OPREQ_MESSAGE: win32more.Windows.Win32.Storage.FileSystem.NtmsOpreqCommand = 5
NtmsOpreqState = Int32
NTMS_OPSTATE_UNKNOWN: win32more.Windows.Win32.Storage.FileSystem.NtmsOpreqState = 0
NTMS_OPSTATE_SUBMITTED: win32more.Windows.Win32.Storage.FileSystem.NtmsOpreqState = 1
NTMS_OPSTATE_ACTIVE: win32more.Windows.Win32.Storage.FileSystem.NtmsOpreqState = 2
NTMS_OPSTATE_INPROGRESS: win32more.Windows.Win32.Storage.FileSystem.NtmsOpreqState = 3
NTMS_OPSTATE_REFUSED: win32more.Windows.Win32.Storage.FileSystem.NtmsOpreqState = 4
NTMS_OPSTATE_COMPLETE: win32more.Windows.Win32.Storage.FileSystem.NtmsOpreqState = 5
NtmsPartitionState = Int32
NTMS_PARTSTATE_UNKNOWN: win32more.Windows.Win32.Storage.FileSystem.NtmsPartitionState = 0
NTMS_PARTSTATE_UNPREPARED: win32more.Windows.Win32.Storage.FileSystem.NtmsPartitionState = 1
NTMS_PARTSTATE_INCOMPATIBLE: win32more.Windows.Win32.Storage.FileSystem.NtmsPartitionState = 2
NTMS_PARTSTATE_DECOMMISSIONED: win32more.Windows.Win32.Storage.FileSystem.NtmsPartitionState = 3
NTMS_PARTSTATE_AVAILABLE: win32more.Windows.Win32.Storage.FileSystem.NtmsPartitionState = 4
NTMS_PARTSTATE_ALLOCATED: win32more.Windows.Win32.Storage.FileSystem.NtmsPartitionState = 5
NTMS_PARTSTATE_COMPLETE: win32more.Windows.Win32.Storage.FileSystem.NtmsPartitionState = 6
NTMS_PARTSTATE_FOREIGN: win32more.Windows.Win32.Storage.FileSystem.NtmsPartitionState = 7
NTMS_PARTSTATE_IMPORT: win32more.Windows.Win32.Storage.FileSystem.NtmsPartitionState = 8
NTMS_PARTSTATE_RESERVED: win32more.Windows.Win32.Storage.FileSystem.NtmsPartitionState = 9
NtmsPoolType = Int32
NTMS_POOLTYPE_UNKNOWN: win32more.Windows.Win32.Storage.FileSystem.NtmsPoolType = 0
NTMS_POOLTYPE_SCRATCH: win32more.Windows.Win32.Storage.FileSystem.NtmsPoolType = 1
NTMS_POOLTYPE_FOREIGN: win32more.Windows.Win32.Storage.FileSystem.NtmsPoolType = 2
NTMS_POOLTYPE_IMPORT: win32more.Windows.Win32.Storage.FileSystem.NtmsPoolType = 3
NTMS_POOLTYPE_APPLICATION: win32more.Windows.Win32.Storage.FileSystem.NtmsPoolType = 1000
NtmsPortContent = Int32
NTMS_PORTCONTENT_UNKNOWN: win32more.Windows.Win32.Storage.FileSystem.NtmsPortContent = 0
NTMS_PORTCONTENT_FULL: win32more.Windows.Win32.Storage.FileSystem.NtmsPortContent = 1
NTMS_PORTCONTENT_EMPTY: win32more.Windows.Win32.Storage.FileSystem.NtmsPortContent = 2
NtmsPortPosition = Int32
NTMS_PORTPOSITION_UNKNOWN: win32more.Windows.Win32.Storage.FileSystem.NtmsPortPosition = 0
NTMS_PORTPOSITION_EXTENDED: win32more.Windows.Win32.Storage.FileSystem.NtmsPortPosition = 1
NTMS_PORTPOSITION_RETRACTED: win32more.Windows.Win32.Storage.FileSystem.NtmsPortPosition = 2
NtmsReadWriteCharacteristics = Int32
NTMS_MEDIARW_UNKNOWN: win32more.Windows.Win32.Storage.FileSystem.NtmsReadWriteCharacteristics = 0
NTMS_MEDIARW_REWRITABLE: win32more.Windows.Win32.Storage.FileSystem.NtmsReadWriteCharacteristics = 1
NTMS_MEDIARW_WRITEONCE: win32more.Windows.Win32.Storage.FileSystem.NtmsReadWriteCharacteristics = 2
NTMS_MEDIARW_READONLY: win32more.Windows.Win32.Storage.FileSystem.NtmsReadWriteCharacteristics = 3
NtmsSessionOptions = Int32
NTMS_SESSION_QUERYEXPEDITE: win32more.Windows.Win32.Storage.FileSystem.NtmsSessionOptions = 1
NtmsSlotState = Int32
NTMS_SLOTSTATE_UNKNOWN: win32more.Windows.Win32.Storage.FileSystem.NtmsSlotState = 0
NTMS_SLOTSTATE_FULL: win32more.Windows.Win32.Storage.FileSystem.NtmsSlotState = 1
NTMS_SLOTSTATE_EMPTY: win32more.Windows.Win32.Storage.FileSystem.NtmsSlotState = 2
NTMS_SLOTSTATE_NOTPRESENT: win32more.Windows.Win32.Storage.FileSystem.NtmsSlotState = 3
NTMS_SLOTSTATE_NEEDSINVENTORY: win32more.Windows.Win32.Storage.FileSystem.NtmsSlotState = 4
NtmsUIOperations = Int32
NTMS_UIDEST_ADD: win32more.Windows.Win32.Storage.FileSystem.NtmsUIOperations = 1
NTMS_UIDEST_DELETE: win32more.Windows.Win32.Storage.FileSystem.NtmsUIOperations = 2
NTMS_UIDEST_DELETEALL: win32more.Windows.Win32.Storage.FileSystem.NtmsUIOperations = 3
NTMS_UIOPERATION_MAX: win32more.Windows.Win32.Storage.FileSystem.NtmsUIOperations = 4
NtmsUITypes = Int32
NTMS_UITYPE_INVALID: win32more.Windows.Win32.Storage.FileSystem.NtmsUITypes = 0
NTMS_UITYPE_INFO: win32more.Windows.Win32.Storage.FileSystem.NtmsUITypes = 1
NTMS_UITYPE_REQ: win32more.Windows.Win32.Storage.FileSystem.NtmsUITypes = 2
NTMS_UITYPE_ERR: win32more.Windows.Win32.Storage.FileSystem.NtmsUITypes = 3
NTMS_UITYPE_MAX: win32more.Windows.Win32.Storage.FileSystem.NtmsUITypes = 4
class OFSTRUCT(Structure):
    cBytes: Byte
    fFixedDisk: Byte
    nErrCode: UInt16
    Reserved1: UInt16
    Reserved2: UInt16
    szPathName: win32more.Windows.Win32.Foundation.CHAR * 128
@winfunctype_pointer
def PCLFS_COMPLETION_ROUTINE(pvOverlapped: VoidPtr, ulReserved: UInt32) -> Void: ...
@winfunctype_pointer
def PCOPYFILE2_PROGRESS_ROUTINE(pMessage: POINTER(win32more.Windows.Win32.Storage.FileSystem.COPYFILE2_MESSAGE), pvCallbackContext: VoidPtr) -> win32more.Windows.Win32.Storage.FileSystem.COPYFILE2_MESSAGE_ACTION: ...
@winfunctype_pointer
def PFE_EXPORT_FUNC(pbData: POINTER(Byte), pvCallbackContext: VoidPtr, ulLength: UInt32) -> UInt32: ...
@winfunctype_pointer
def PFE_IMPORT_FUNC(pbData: POINTER(Byte), pvCallbackContext: VoidPtr, ulLength: POINTER(UInt32)) -> UInt32: ...
@winfunctype_pointer
def PFN_IO_COMPLETION(pContext: POINTER(win32more.Windows.Win32.Storage.FileSystem.FIO_CONTEXT), lpo: POINTER(win32more.Windows.Win32.Storage.FileSystem.FH_OVERLAPPED), cb: UInt32, dwCompletionStatus: UInt32) -> Void: ...
@winfunctype_pointer
def PLOG_FULL_HANDLER_CALLBACK(hLogFile: win32more.Windows.Win32.Foundation.HANDLE, dwError: UInt32, fLogIsPinned: win32more.Windows.Win32.Foundation.BOOL, pvClientContext: VoidPtr) -> Void: ...
@winfunctype_pointer
def PLOG_TAIL_ADVANCE_CALLBACK(hLogFile: win32more.Windows.Win32.Foundation.HANDLE, lsnTarget: win32more.Windows.Win32.Storage.FileSystem.CLS_LSN, pvClientContext: VoidPtr) -> Void: ...
@winfunctype_pointer
def PLOG_UNPINNED_CALLBACK(hLogFile: win32more.Windows.Win32.Foundation.HANDLE, pvClientContext: VoidPtr) -> Void: ...
PREPARE_TAPE_OPERATION = UInt32
TAPE_FORMAT: win32more.Windows.Win32.Storage.FileSystem.PREPARE_TAPE_OPERATION = 5
TAPE_LOAD: win32more.Windows.Win32.Storage.FileSystem.PREPARE_TAPE_OPERATION = 0
TAPE_LOCK: win32more.Windows.Win32.Storage.FileSystem.PREPARE_TAPE_OPERATION = 3
TAPE_TENSION: win32more.Windows.Win32.Storage.FileSystem.PREPARE_TAPE_OPERATION = 2
TAPE_UNLOAD: win32more.Windows.Win32.Storage.FileSystem.PREPARE_TAPE_OPERATION = 1
TAPE_UNLOCK: win32more.Windows.Win32.Storage.FileSystem.PREPARE_TAPE_OPERATION = 4
PRIORITY_HINT = Int32
IoPriorityHintVeryLow: win32more.Windows.Win32.Storage.FileSystem.PRIORITY_HINT = 0
IoPriorityHintLow: win32more.Windows.Win32.Storage.FileSystem.PRIORITY_HINT = 1
IoPriorityHintNormal: win32more.Windows.Win32.Storage.FileSystem.PRIORITY_HINT = 2
MaximumIoPriorityHintType: win32more.Windows.Win32.Storage.FileSystem.PRIORITY_HINT = 3
READ_DIRECTORY_NOTIFY_INFORMATION_CLASS = Int32
ReadDirectoryNotifyInformation: win32more.Windows.Win32.Storage.FileSystem.READ_DIRECTORY_NOTIFY_INFORMATION_CLASS = 1
ReadDirectoryNotifyExtendedInformation: win32more.Windows.Win32.Storage.FileSystem.READ_DIRECTORY_NOTIFY_INFORMATION_CLASS = 2
ReadDirectoryNotifyFullInformation: win32more.Windows.Win32.Storage.FileSystem.READ_DIRECTORY_NOTIFY_INFORMATION_CLASS = 3
ReadDirectoryNotifyMaximumInformation: win32more.Windows.Win32.Storage.FileSystem.READ_DIRECTORY_NOTIFY_INFORMATION_CLASS = 4
class REPARSE_GUID_DATA_BUFFER(Structure):
    ReparseTag: UInt32
    ReparseDataLength: UInt16
    Reserved: UInt16
    ReparseGuid: Guid
    GenericReparseBuffer: _GenericReparseBuffer_e__Struct
    class _GenericReparseBuffer_e__Struct(Structure):
        DataBuffer: Byte * 1
REPLACE_FILE_FLAGS = UInt32
REPLACEFILE_WRITE_THROUGH: win32more.Windows.Win32.Storage.FileSystem.REPLACE_FILE_FLAGS = 1
REPLACEFILE_IGNORE_MERGE_ERRORS: win32more.Windows.Win32.Storage.FileSystem.REPLACE_FILE_FLAGS = 2
REPLACEFILE_IGNORE_ACL_ERRORS: win32more.Windows.Win32.Storage.FileSystem.REPLACE_FILE_FLAGS = 4
class SERVER_ALIAS_INFO_0(Structure):
    srvai0_alias: win32more.Windows.Win32.Foundation.PWSTR
    srvai0_target: win32more.Windows.Win32.Foundation.PWSTR
    srvai0_default: win32more.Windows.Win32.Foundation.BOOLEAN
    srvai0_reserved: UInt32
class SERVER_CERTIFICATE_INFO_0(Structure):
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
QUIC: win32more.Windows.Win32.Storage.FileSystem.SERVER_CERTIFICATE_TYPE = 0
class SESSION_INFO_0(Structure):
    sesi0_cname: win32more.Windows.Win32.Foundation.PWSTR
class SESSION_INFO_1(Structure):
    sesi1_cname: win32more.Windows.Win32.Foundation.PWSTR
    sesi1_username: win32more.Windows.Win32.Foundation.PWSTR
    sesi1_num_opens: UInt32
    sesi1_time: UInt32
    sesi1_idle_time: UInt32
    sesi1_user_flags: win32more.Windows.Win32.Storage.FileSystem.SESSION_INFO_USER_FLAGS
class SESSION_INFO_10(Structure):
    sesi10_cname: win32more.Windows.Win32.Foundation.PWSTR
    sesi10_username: win32more.Windows.Win32.Foundation.PWSTR
    sesi10_time: UInt32
    sesi10_idle_time: UInt32
class SESSION_INFO_2(Structure):
    sesi2_cname: win32more.Windows.Win32.Foundation.PWSTR
    sesi2_username: win32more.Windows.Win32.Foundation.PWSTR
    sesi2_num_opens: UInt32
    sesi2_time: UInt32
    sesi2_idle_time: UInt32
    sesi2_user_flags: win32more.Windows.Win32.Storage.FileSystem.SESSION_INFO_USER_FLAGS
    sesi2_cltype_name: win32more.Windows.Win32.Foundation.PWSTR
class SESSION_INFO_502(Structure):
    sesi502_cname: win32more.Windows.Win32.Foundation.PWSTR
    sesi502_username: win32more.Windows.Win32.Foundation.PWSTR
    sesi502_num_opens: UInt32
    sesi502_time: UInt32
    sesi502_idle_time: UInt32
    sesi502_user_flags: win32more.Windows.Win32.Storage.FileSystem.SESSION_INFO_USER_FLAGS
    sesi502_cltype_name: win32more.Windows.Win32.Foundation.PWSTR
    sesi502_transport: win32more.Windows.Win32.Foundation.PWSTR
SESSION_INFO_USER_FLAGS = UInt32
SESS_GUEST: win32more.Windows.Win32.Storage.FileSystem.SESSION_INFO_USER_FLAGS = 1
SESS_NOENCRYPTION: win32more.Windows.Win32.Storage.FileSystem.SESSION_INFO_USER_FLAGS = 2
SET_FILE_POINTER_MOVE_METHOD = UInt32
FILE_BEGIN: win32more.Windows.Win32.Storage.FileSystem.SET_FILE_POINTER_MOVE_METHOD = 0
FILE_CURRENT: win32more.Windows.Win32.Storage.FileSystem.SET_FILE_POINTER_MOVE_METHOD = 1
FILE_END: win32more.Windows.Win32.Storage.FileSystem.SET_FILE_POINTER_MOVE_METHOD = 2
class SHARE_INFO_0(Structure):
    shi0_netname: win32more.Windows.Win32.Foundation.PWSTR
class SHARE_INFO_1(Structure):
    shi1_netname: win32more.Windows.Win32.Foundation.PWSTR
    shi1_type: win32more.Windows.Win32.Storage.FileSystem.SHARE_TYPE
    shi1_remark: win32more.Windows.Win32.Foundation.PWSTR
class SHARE_INFO_1004(Structure):
    shi1004_remark: win32more.Windows.Win32.Foundation.PWSTR
class SHARE_INFO_1005(Structure):
    shi1005_flags: UInt32
class SHARE_INFO_1006(Structure):
    shi1006_max_uses: UInt32
class SHARE_INFO_1501(Structure):
    shi1501_reserved: UInt32
    shi1501_security_descriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR
class SHARE_INFO_1503(Structure):
    shi1503_sharefilter: Guid
class SHARE_INFO_2(Structure):
    shi2_netname: win32more.Windows.Win32.Foundation.PWSTR
    shi2_type: win32more.Windows.Win32.Storage.FileSystem.SHARE_TYPE
    shi2_remark: win32more.Windows.Win32.Foundation.PWSTR
    shi2_permissions: win32more.Windows.Win32.Storage.FileSystem.SHARE_INFO_PERMISSIONS
    shi2_max_uses: UInt32
    shi2_current_uses: UInt32
    shi2_path: win32more.Windows.Win32.Foundation.PWSTR
    shi2_passwd: win32more.Windows.Win32.Foundation.PWSTR
class SHARE_INFO_501(Structure):
    shi501_netname: win32more.Windows.Win32.Foundation.PWSTR
    shi501_type: win32more.Windows.Win32.Storage.FileSystem.SHARE_TYPE
    shi501_remark: win32more.Windows.Win32.Foundation.PWSTR
    shi501_flags: UInt32
class SHARE_INFO_502(Structure):
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
class SHARE_INFO_503(Structure):
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
ACCESS_READ: win32more.Windows.Win32.Storage.FileSystem.SHARE_INFO_PERMISSIONS = 1
ACCESS_WRITE: win32more.Windows.Win32.Storage.FileSystem.SHARE_INFO_PERMISSIONS = 2
ACCESS_CREATE: win32more.Windows.Win32.Storage.FileSystem.SHARE_INFO_PERMISSIONS = 4
ACCESS_EXEC: win32more.Windows.Win32.Storage.FileSystem.SHARE_INFO_PERMISSIONS = 8
ACCESS_DELETE: win32more.Windows.Win32.Storage.FileSystem.SHARE_INFO_PERMISSIONS = 16
ACCESS_ATRIB: win32more.Windows.Win32.Storage.FileSystem.SHARE_INFO_PERMISSIONS = 32
ACCESS_PERM: win32more.Windows.Win32.Storage.FileSystem.SHARE_INFO_PERMISSIONS = 64
ACCESS_ALL: win32more.Windows.Win32.Storage.FileSystem.SHARE_INFO_PERMISSIONS = 32768
SHARE_TYPE = UInt32
STYPE_DISKTREE: win32more.Windows.Win32.Storage.FileSystem.SHARE_TYPE = 0
STYPE_PRINTQ: win32more.Windows.Win32.Storage.FileSystem.SHARE_TYPE = 1
STYPE_DEVICE: win32more.Windows.Win32.Storage.FileSystem.SHARE_TYPE = 2
STYPE_IPC: win32more.Windows.Win32.Storage.FileSystem.SHARE_TYPE = 3
STYPE_SPECIAL: win32more.Windows.Win32.Storage.FileSystem.SHARE_TYPE = 2147483648
STYPE_TEMPORARY: win32more.Windows.Win32.Storage.FileSystem.SHARE_TYPE = 1073741824
STYPE_MASK: win32more.Windows.Win32.Storage.FileSystem.SHARE_TYPE = 255
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
BusTypeUnknown: win32more.Windows.Win32.Storage.FileSystem.STORAGE_BUS_TYPE = 0
BusTypeScsi: win32more.Windows.Win32.Storage.FileSystem.STORAGE_BUS_TYPE = 1
BusTypeAtapi: win32more.Windows.Win32.Storage.FileSystem.STORAGE_BUS_TYPE = 2
BusTypeAta: win32more.Windows.Win32.Storage.FileSystem.STORAGE_BUS_TYPE = 3
BusType1394: win32more.Windows.Win32.Storage.FileSystem.STORAGE_BUS_TYPE = 4
BusTypeSsa: win32more.Windows.Win32.Storage.FileSystem.STORAGE_BUS_TYPE = 5
BusTypeFibre: win32more.Windows.Win32.Storage.FileSystem.STORAGE_BUS_TYPE = 6
BusTypeUsb: win32more.Windows.Win32.Storage.FileSystem.STORAGE_BUS_TYPE = 7
BusTypeRAID: win32more.Windows.Win32.Storage.FileSystem.STORAGE_BUS_TYPE = 8
BusTypeiScsi: win32more.Windows.Win32.Storage.FileSystem.STORAGE_BUS_TYPE = 9
BusTypeSas: win32more.Windows.Win32.Storage.FileSystem.STORAGE_BUS_TYPE = 10
BusTypeSata: win32more.Windows.Win32.Storage.FileSystem.STORAGE_BUS_TYPE = 11
BusTypeSd: win32more.Windows.Win32.Storage.FileSystem.STORAGE_BUS_TYPE = 12
BusTypeMmc: win32more.Windows.Win32.Storage.FileSystem.STORAGE_BUS_TYPE = 13
BusTypeVirtual: win32more.Windows.Win32.Storage.FileSystem.STORAGE_BUS_TYPE = 14
BusTypeFileBackedVirtual: win32more.Windows.Win32.Storage.FileSystem.STORAGE_BUS_TYPE = 15
BusTypeSpaces: win32more.Windows.Win32.Storage.FileSystem.STORAGE_BUS_TYPE = 16
BusTypeNvme: win32more.Windows.Win32.Storage.FileSystem.STORAGE_BUS_TYPE = 17
BusTypeSCM: win32more.Windows.Win32.Storage.FileSystem.STORAGE_BUS_TYPE = 18
BusTypeUfs: win32more.Windows.Win32.Storage.FileSystem.STORAGE_BUS_TYPE = 19
BusTypeMax: win32more.Windows.Win32.Storage.FileSystem.STORAGE_BUS_TYPE = 20
BusTypeMaxReserved: win32more.Windows.Win32.Storage.FileSystem.STORAGE_BUS_TYPE = 127
STREAM_INFO_LEVELS = Int32
FindStreamInfoStandard: win32more.Windows.Win32.Storage.FileSystem.STREAM_INFO_LEVELS = 0
FindStreamInfoMaxInfoLevel: win32more.Windows.Win32.Storage.FileSystem.STREAM_INFO_LEVELS = 1
SYMBOLIC_LINK_FLAGS = UInt32
SYMBOLIC_LINK_FLAG_DIRECTORY: win32more.Windows.Win32.Storage.FileSystem.SYMBOLIC_LINK_FLAGS = 1
SYMBOLIC_LINK_FLAG_ALLOW_UNPRIVILEGED_CREATE: win32more.Windows.Win32.Storage.FileSystem.SYMBOLIC_LINK_FLAGS = 2
TAPEMARK_TYPE = UInt32
TAPE_FILEMARKS: win32more.Windows.Win32.Storage.FileSystem.TAPEMARK_TYPE = 1
TAPE_LONG_FILEMARKS: win32more.Windows.Win32.Storage.FileSystem.TAPEMARK_TYPE = 3
TAPE_SETMARKS: win32more.Windows.Win32.Storage.FileSystem.TAPEMARK_TYPE = 0
TAPE_SHORT_FILEMARKS: win32more.Windows.Win32.Storage.FileSystem.TAPEMARK_TYPE = 2
class TAPE_ERASE(Structure):
    Type: win32more.Windows.Win32.Storage.FileSystem.ERASE_TAPE_TYPE
    Immediate: win32more.Windows.Win32.Foundation.BOOLEAN
class TAPE_GET_POSITION(Structure):
    Type: win32more.Windows.Win32.Storage.FileSystem.TAPE_POSITION_TYPE
    Partition: UInt32
    Offset: Int64
TAPE_INFORMATION_TYPE = UInt32
SET_TAPE_DRIVE_INFORMATION: win32more.Windows.Win32.Storage.FileSystem.TAPE_INFORMATION_TYPE = 1
SET_TAPE_MEDIA_INFORMATION: win32more.Windows.Win32.Storage.FileSystem.TAPE_INFORMATION_TYPE = 0
TAPE_POSITION_METHOD = UInt32
TAPE_ABSOLUTE_BLOCK: win32more.Windows.Win32.Storage.FileSystem.TAPE_POSITION_METHOD = 1
TAPE_LOGICAL_BLOCK: win32more.Windows.Win32.Storage.FileSystem.TAPE_POSITION_METHOD = 2
TAPE_REWIND: win32more.Windows.Win32.Storage.FileSystem.TAPE_POSITION_METHOD = 0
TAPE_SPACE_END_OF_DATA: win32more.Windows.Win32.Storage.FileSystem.TAPE_POSITION_METHOD = 4
TAPE_SPACE_FILEMARKS: win32more.Windows.Win32.Storage.FileSystem.TAPE_POSITION_METHOD = 6
TAPE_SPACE_RELATIVE_BLOCKS: win32more.Windows.Win32.Storage.FileSystem.TAPE_POSITION_METHOD = 5
TAPE_SPACE_SEQUENTIAL_FMKS: win32more.Windows.Win32.Storage.FileSystem.TAPE_POSITION_METHOD = 7
TAPE_SPACE_SEQUENTIAL_SMKS: win32more.Windows.Win32.Storage.FileSystem.TAPE_POSITION_METHOD = 9
TAPE_SPACE_SETMARKS: win32more.Windows.Win32.Storage.FileSystem.TAPE_POSITION_METHOD = 8
TAPE_POSITION_TYPE = UInt32
TAPE_ABSOLUTE_POSITION: win32more.Windows.Win32.Storage.FileSystem.TAPE_POSITION_TYPE = 0
TAPE_LOGICAL_POSITION: win32more.Windows.Win32.Storage.FileSystem.TAPE_POSITION_TYPE = 1
class TAPE_PREPARE(Structure):
    Operation: win32more.Windows.Win32.Storage.FileSystem.PREPARE_TAPE_OPERATION
    Immediate: win32more.Windows.Win32.Foundation.BOOLEAN
class TAPE_SET_POSITION(Structure):
    Method: win32more.Windows.Win32.Storage.FileSystem.TAPE_POSITION_METHOD
    Partition: UInt32
    Offset: Int64
    Immediate: win32more.Windows.Win32.Foundation.BOOLEAN
class TAPE_WRITE_MARKS(Structure):
    Type: win32more.Windows.Win32.Storage.FileSystem.TAPEMARK_TYPE
    Count: UInt32
    Immediate: win32more.Windows.Win32.Foundation.BOOLEAN
class TRANSACTION_NOTIFICATION(Structure):
    TransactionKey: VoidPtr
    TransactionNotification: UInt32
    TmVirtualClock: Int64
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
TransactionOutcomeUndetermined: win32more.Windows.Win32.Storage.FileSystem.TRANSACTION_OUTCOME = 1
TransactionOutcomeCommitted: win32more.Windows.Win32.Storage.FileSystem.TRANSACTION_OUTCOME = 2
TransactionOutcomeAborted: win32more.Windows.Win32.Storage.FileSystem.TRANSACTION_OUTCOME = 3
TXFS_MINIVERSION = UInt32
TXFS_MINIVERSION_COMMITTED_VIEW: win32more.Windows.Win32.Storage.FileSystem.TXFS_MINIVERSION = 0
TXFS_MINIVERSION_DIRTY_VIEW: win32more.Windows.Win32.Storage.FileSystem.TXFS_MINIVERSION = 65535
TXFS_MINIVERSION_DEFAULT_VIEW: win32more.Windows.Win32.Storage.FileSystem.TXFS_MINIVERSION = 65534
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
    TxfFileId: win32more.Windows.Win32.Storage.FileSystem.TXF_ID
    KtmGuid: Guid
    FileNameLength: UInt32
    FileNameByteOffsetInStructure: UInt32
    _pack_ = 4
class TXF_LOG_RECORD_BASE(Structure):
    Version: UInt16
    RecordType: win32more.Windows.Win32.Storage.FileSystem.TXF_LOG_RECORD_TYPE
    RecordLength: UInt32
    _pack_ = 4
class TXF_LOG_RECORD_TRUNCATE(Structure):
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
TXF_LOG_RECORD_TYPE_AFFECTED_FILE: win32more.Windows.Win32.Storage.FileSystem.TXF_LOG_RECORD_TYPE = 4
TXF_LOG_RECORD_TYPE_TRUNCATE: win32more.Windows.Win32.Storage.FileSystem.TXF_LOG_RECORD_TYPE = 2
TXF_LOG_RECORD_TYPE_WRITE: win32more.Windows.Win32.Storage.FileSystem.TXF_LOG_RECORD_TYPE = 1
class TXF_LOG_RECORD_WRITE(Structure):
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
VFFF_ISSHAREDFILE: win32more.Windows.Win32.Storage.FileSystem.VER_FIND_FILE_FLAGS = 1
VER_FIND_FILE_STATUS = UInt32
VFF_CURNEDEST: win32more.Windows.Win32.Storage.FileSystem.VER_FIND_FILE_STATUS = 1
VFF_FILEINUSE: win32more.Windows.Win32.Storage.FileSystem.VER_FIND_FILE_STATUS = 2
VFF_BUFFTOOSMALL: win32more.Windows.Win32.Storage.FileSystem.VER_FIND_FILE_STATUS = 4
VER_INSTALL_FILE_FLAGS = UInt32
VIFF_FORCEINSTALL: win32more.Windows.Win32.Storage.FileSystem.VER_INSTALL_FILE_FLAGS = 1
VIFF_DONTDELETEOLD: win32more.Windows.Win32.Storage.FileSystem.VER_INSTALL_FILE_FLAGS = 2
VER_INSTALL_FILE_STATUS = UInt32
VIF_TEMPFILE: win32more.Windows.Win32.Storage.FileSystem.VER_INSTALL_FILE_STATUS = 1
VIF_MISMATCH: win32more.Windows.Win32.Storage.FileSystem.VER_INSTALL_FILE_STATUS = 2
VIF_SRCOLD: win32more.Windows.Win32.Storage.FileSystem.VER_INSTALL_FILE_STATUS = 4
VIF_DIFFLANG: win32more.Windows.Win32.Storage.FileSystem.VER_INSTALL_FILE_STATUS = 8
VIF_DIFFCODEPG: win32more.Windows.Win32.Storage.FileSystem.VER_INSTALL_FILE_STATUS = 16
VIF_DIFFTYPE: win32more.Windows.Win32.Storage.FileSystem.VER_INSTALL_FILE_STATUS = 32
VIF_WRITEPROT: win32more.Windows.Win32.Storage.FileSystem.VER_INSTALL_FILE_STATUS = 64
VIF_FILEINUSE: win32more.Windows.Win32.Storage.FileSystem.VER_INSTALL_FILE_STATUS = 128
VIF_OUTOFSPACE: win32more.Windows.Win32.Storage.FileSystem.VER_INSTALL_FILE_STATUS = 256
VIF_ACCESSVIOLATION: win32more.Windows.Win32.Storage.FileSystem.VER_INSTALL_FILE_STATUS = 512
VIF_SHARINGVIOLATION: win32more.Windows.Win32.Storage.FileSystem.VER_INSTALL_FILE_STATUS = 1024
VIF_CANNOTCREATE: win32more.Windows.Win32.Storage.FileSystem.VER_INSTALL_FILE_STATUS = 2048
VIF_CANNOTDELETE: win32more.Windows.Win32.Storage.FileSystem.VER_INSTALL_FILE_STATUS = 4096
VIF_CANNOTRENAME: win32more.Windows.Win32.Storage.FileSystem.VER_INSTALL_FILE_STATUS = 8192
VIF_CANNOTDELETECUR: win32more.Windows.Win32.Storage.FileSystem.VER_INSTALL_FILE_STATUS = 16384
VIF_OUTOFMEMORY: win32more.Windows.Win32.Storage.FileSystem.VER_INSTALL_FILE_STATUS = 32768
VIF_CANNOTREADSRC: win32more.Windows.Win32.Storage.FileSystem.VER_INSTALL_FILE_STATUS = 65536
VIF_CANNOTREADDST: win32more.Windows.Win32.Storage.FileSystem.VER_INSTALL_FILE_STATUS = 131072
VIF_BUFFTOOSMALL: win32more.Windows.Win32.Storage.FileSystem.VER_INSTALL_FILE_STATUS = 262144
VIF_CANNOTLOADLZ32: win32more.Windows.Win32.Storage.FileSystem.VER_INSTALL_FILE_STATUS = 524288
VIF_CANNOTLOADCABINET: win32more.Windows.Win32.Storage.FileSystem.VER_INSTALL_FILE_STATUS = 1048576
class VOLUME_ALLOCATE_BC_STREAM_INPUT(Structure):
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
    Extents: win32more.Windows.Win32.Storage.FileSystem.FILE_EXTENT * 1
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
    PhysicalOffset: win32more.Windows.Win32.Storage.FileSystem.VOLUME_PHYSICAL_OFFSET * 1
class VOLUME_READ_PLEX_INPUT(Structure):
    ByteOffset: Int64
    Length: UInt32
    PlexNumber: UInt32
class VOLUME_SET_GPT_ATTRIBUTES_INFORMATION(Structure):
    GptAttributes: UInt64
    RevertOnClose: win32more.Windows.Win32.Foundation.BOOLEAN
    ApplyToAllConnectedVolumes: win32more.Windows.Win32.Foundation.BOOLEAN
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
    dwFileFlags: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_FLAGS
    dwFileOS: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_OS
    dwFileType: UInt32
    dwFileSubtype: UInt32
    dwFileDateMS: UInt32
    dwFileDateLS: UInt32
VS_FIXEDFILEINFO_FILE_FLAGS = UInt32
VS_FF_DEBUG: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_FLAGS = 1
VS_FF_PRERELEASE: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_FLAGS = 2
VS_FF_PATCHED: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_FLAGS = 4
VS_FF_PRIVATEBUILD: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_FLAGS = 8
VS_FF_INFOINFERRED: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_FLAGS = 16
VS_FF_SPECIALBUILD: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_FLAGS = 32
VS_FIXEDFILEINFO_FILE_OS = UInt32
VOS_UNKNOWN: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_OS = 0
VOS_DOS: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_OS = 65536
VOS_OS216: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_OS = 131072
VOS_OS232: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_OS = 196608
VOS_NT: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_OS = 262144
VOS_WINCE: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_OS = 327680
VOS__BASE: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_OS = 0
VOS__WINDOWS16: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_OS = 1
VOS__PM16: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_OS = 2
VOS__PM32: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_OS = 3
VOS__WINDOWS32: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_OS = 4
VOS_DOS_WINDOWS16: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_OS = 65537
VOS_DOS_WINDOWS32: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_OS = 65540
VOS_OS216_PM16: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_OS = 131074
VOS_OS232_PM32: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_OS = 196611
VOS_NT_WINDOWS32: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_OS = 262148
VS_FIXEDFILEINFO_FILE_SUBTYPE = Int32
VFT2_UNKNOWN: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_SUBTYPE = 0
VFT2_DRV_PRINTER: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_SUBTYPE = 1
VFT2_DRV_KEYBOARD: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_SUBTYPE = 2
VFT2_DRV_LANGUAGE: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_SUBTYPE = 3
VFT2_DRV_DISPLAY: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_SUBTYPE = 4
VFT2_DRV_MOUSE: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_SUBTYPE = 5
VFT2_DRV_NETWORK: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_SUBTYPE = 6
VFT2_DRV_SYSTEM: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_SUBTYPE = 7
VFT2_DRV_INSTALLABLE: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_SUBTYPE = 8
VFT2_DRV_SOUND: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_SUBTYPE = 9
VFT2_DRV_COMM: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_SUBTYPE = 10
VFT2_DRV_INPUTMETHOD: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_SUBTYPE = 11
VFT2_DRV_VERSIONED_PRINTER: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_SUBTYPE = 12
VFT2_FONT_RASTER: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_SUBTYPE = 1
VFT2_FONT_VECTOR: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_SUBTYPE = 2
VFT2_FONT_TRUETYPE: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_SUBTYPE = 3
VS_FIXEDFILEINFO_FILE_TYPE = Int32
VFT_UNKNOWN: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_TYPE = 0
VFT_APP: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_TYPE = 1
VFT_DLL: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_TYPE = 2
VFT_DRV: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_TYPE = 3
VFT_FONT: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_TYPE = 4
VFT_VXD: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_TYPE = 5
VFT_STATIC_LIB: win32more.Windows.Win32.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_TYPE = 7
class WIM_ENTRY_INFO(Structure):
    WimEntryInfoSize: UInt32
    WimType: UInt32
    DataSourceId: Int64
    WimGuid: Guid
    WimPath: win32more.Windows.Win32.Foundation.PWSTR
    WimIndex: UInt32
    Flags: UInt32
class WIM_EXTERNAL_FILE_INFO(Structure):
    DataSourceId: Int64
    ResourceHash: Byte * 20
    Flags: UInt32
class WIN32_FILE_ATTRIBUTE_DATA(Structure):
    dwFileAttributes: UInt32
    ftCreationTime: win32more.Windows.Win32.Foundation.FILETIME
    ftLastAccessTime: win32more.Windows.Win32.Foundation.FILETIME
    ftLastWriteTime: win32more.Windows.Win32.Foundation.FILETIME
    nFileSizeHigh: UInt32
    nFileSizeLow: UInt32
class WIN32_FIND_DATAA(Structure):
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
class WIN32_FIND_DATAW(Structure):
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
WIN32_FIND_DATA = UnicodeAlias('WIN32_FIND_DATAW')
class WIN32_FIND_STREAM_DATA(Structure):
    StreamSize: Int64
    cStreamName: Char * 296
class WIN32_STREAM_ID(Structure):
    dwStreamId: win32more.Windows.Win32.Storage.FileSystem.WIN_STREAM_ID
    dwStreamAttributes: UInt32
    Size: Int64
    dwStreamNameSize: UInt32
    cStreamName: Char * 1
WIN_STREAM_ID = UInt32
BACKUP_ALTERNATE_DATA: win32more.Windows.Win32.Storage.FileSystem.WIN_STREAM_ID = 4
BACKUP_DATA: win32more.Windows.Win32.Storage.FileSystem.WIN_STREAM_ID = 1
BACKUP_EA_DATA: win32more.Windows.Win32.Storage.FileSystem.WIN_STREAM_ID = 2
BACKUP_LINK: win32more.Windows.Win32.Storage.FileSystem.WIN_STREAM_ID = 5
BACKUP_OBJECT_ID: win32more.Windows.Win32.Storage.FileSystem.WIN_STREAM_ID = 7
BACKUP_PROPERTY_DATA: win32more.Windows.Win32.Storage.FileSystem.WIN_STREAM_ID = 6
BACKUP_REPARSE_DATA: win32more.Windows.Win32.Storage.FileSystem.WIN_STREAM_ID = 8
BACKUP_SECURITY_DATA: win32more.Windows.Win32.Storage.FileSystem.WIN_STREAM_ID = 3
BACKUP_SPARSE_BLOCK: win32more.Windows.Win32.Storage.FileSystem.WIN_STREAM_ID = 9
BACKUP_TXFS_DATA: win32more.Windows.Win32.Storage.FileSystem.WIN_STREAM_ID = 10
class WOF_FILE_COMPRESSION_INFO_V0(Structure):
    Algorithm: UInt32
class WOF_FILE_COMPRESSION_INFO_V1(Structure):
    Algorithm: UInt32
    Flags: UInt32
@winfunctype_pointer
def WofEnumEntryProc(EntryInfo: VoidPtr, UserData: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def WofEnumFilesProc(FilePath: win32more.Windows.Win32.Foundation.PWSTR, ExternalFileInfo: VoidPtr, UserData: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...


make_ready(__name__)
