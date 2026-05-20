from __future__ import annotations
from win32more._prelude import *
import win32more.Windows.Wdk.Foundation
import win32more.Windows.Wdk.Storage.FileSystem
import win32more.Windows.Wdk.Storage.FileSystem.Minifilters
import win32more.Windows.Wdk.System.SystemServices
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Security
import win32more.Windows.Win32.Storage.InstallableFileSystems
import win32more.Windows.Win32.System.IO
import win32more.Windows.Win32.System.Kernel
IRP_MJ_ACQUIRE_FOR_SECTION_SYNCHRONIZATION: UInt16 = 65535
IRP_MJ_RELEASE_FOR_SECTION_SYNCHRONIZATION: UInt16 = 65534
IRP_MJ_ACQUIRE_FOR_MOD_WRITE: UInt16 = 65533
IRP_MJ_RELEASE_FOR_MOD_WRITE: UInt16 = 65532
IRP_MJ_ACQUIRE_FOR_CC_FLUSH: UInt16 = 65531
IRP_MJ_RELEASE_FOR_CC_FLUSH: UInt16 = 65530
IRP_MJ_QUERY_OPEN: UInt16 = 65529
IRP_MJ_FAST_IO_CHECK_IF_POSSIBLE: UInt16 = 65523
IRP_MJ_NETWORK_QUERY_OPEN: UInt16 = 65522
IRP_MJ_MDL_READ: UInt16 = 65521
IRP_MJ_MDL_READ_COMPLETE: UInt16 = 65520
IRP_MJ_PREPARE_MDL_WRITE: UInt16 = 65519
IRP_MJ_MDL_WRITE_COMPLETE: UInt16 = 65518
IRP_MJ_VOLUME_MOUNT: UInt16 = 65517
IRP_MJ_VOLUME_DISMOUNT: UInt16 = 65516
FLT_INTERNAL_OPERATION_COUNT: UInt32 = 22
IRP_MJ_OPERATION_END: UInt16 = 128
FLTFL_CALLBACK_DATA_REISSUE_MASK: UInt32 = 65535
FLTFL_CALLBACK_DATA_IRP_OPERATION: UInt32 = 1
FLTFL_CALLBACK_DATA_FAST_IO_OPERATION: UInt32 = 2
FLTFL_CALLBACK_DATA_FS_FILTER_OPERATION: UInt32 = 4
FLTFL_CALLBACK_DATA_SYSTEM_BUFFER: UInt32 = 8
FLTFL_CALLBACK_DATA_GENERATED_IO: UInt32 = 65536
FLTFL_CALLBACK_DATA_REISSUED_IO: UInt32 = 131072
FLTFL_CALLBACK_DATA_DRAINING_IO: UInt32 = 262144
FLTFL_CALLBACK_DATA_POST_OPERATION: UInt32 = 524288
FLTFL_CALLBACK_DATA_NEW_SYSTEM_BUFFER: UInt32 = 1048576
FLTFL_CALLBACK_DATA_DIRTY: UInt32 = 2147483648
FLT_ALLOCATE_CALLBACK_DATA_PREALLOCATE_ALL_MEMORY: UInt32 = 1
FLT_VOLUME_CONTEXT: UInt32 = 1
FLT_INSTANCE_CONTEXT: UInt32 = 2
FLT_FILE_CONTEXT: UInt32 = 4
FLT_STREAM_CONTEXT: UInt32 = 8
FLT_STREAMHANDLE_CONTEXT: UInt32 = 16
FLT_TRANSACTION_CONTEXT: UInt32 = 32
FLT_SECTION_CONTEXT: UInt32 = 64
FLT_CONTEXT_END: UInt32 = 65535
FLTFL_CONTEXT_REGISTRATION_NO_EXACT_SIZE_MATCH: UInt32 = 1
FLTFL_INSTANCE_SETUP_AUTOMATIC_ATTACHMENT: UInt32 = 1
FLTFL_INSTANCE_SETUP_MANUAL_ATTACHMENT: UInt32 = 2
FLTFL_INSTANCE_SETUP_NEWLY_MOUNTED_VOLUME: UInt32 = 4
FLTFL_INSTANCE_SETUP_DETACHED_VOLUME: UInt32 = 8
FLTFL_INSTANCE_TEARDOWN_MANUAL: UInt32 = 1
FLTFL_INSTANCE_TEARDOWN_FILTER_UNLOAD: UInt32 = 2
FLTFL_INSTANCE_TEARDOWN_MANDATORY_FILTER_UNLOAD: UInt32 = 4
FLTFL_INSTANCE_TEARDOWN_VOLUME_DISMOUNT: UInt32 = 8
FLTFL_INSTANCE_TEARDOWN_INTERNAL_ERROR: UInt32 = 16
FLTFL_POST_OPERATION_DRAINING: UInt32 = 1
FLTFL_OPERATION_REGISTRATION_SKIP_PAGING_IO: UInt32 = 1
FLTFL_OPERATION_REGISTRATION_SKIP_CACHED_IO: UInt32 = 2
FLTFL_OPERATION_REGISTRATION_SKIP_NON_DASD_IO: UInt32 = 4
FLTFL_OPERATION_REGISTRATION_SKIP_NON_CACHED_NON_PAGING_IO: UInt32 = 8
FLTFL_FILTER_UNLOAD_MANDATORY: UInt32 = 1
FLTFL_NORMALIZE_NAME_CASE_SENSITIVE: UInt32 = 1
FLTFL_NORMALIZE_NAME_DESTINATION_FILE_NAME: UInt32 = 2
FLT_REGISTRATION_VERSION_0200: UInt32 = 512
FLT_REGISTRATION_VERSION_0201: UInt32 = 513
FLT_REGISTRATION_VERSION_0202: UInt32 = 514
FLT_REGISTRATION_VERSION_0203: UInt32 = 515
FLT_REGISTRATION_VERSION: UInt32 = 515
FLTFL_REGISTRATION_DO_NOT_SUPPORT_SERVICE_STOP: UInt32 = 1
FLTFL_REGISTRATION_SUPPORT_NPFS_MSFS: UInt32 = 2
FLTFL_REGISTRATION_SUPPORT_DAX_VOLUME: UInt32 = 4
FLTFL_REGISTRATION_SUPPORT_WCOS: UInt32 = 8
FLTFL_IO_OPERATION_NON_CACHED: UInt32 = 1
FLTFL_IO_OPERATION_PAGING: UInt32 = 2
FLTFL_IO_OPERATION_DO_NOT_UPDATE_BYTE_OFFSET: UInt32 = 4
FLTFL_IO_OPERATION_SYNCHRONOUS_PAGING: UInt32 = 8
FLT_VALID_FILE_NAME_FORMATS: UInt32 = 255
FLT_FILE_NAME_NORMALIZED: UInt32 = 1
FLT_FILE_NAME_OPENED: UInt32 = 2
FLT_FILE_NAME_SHORT: UInt32 = 3
FLT_VALID_FILE_NAME_QUERY_METHODS: UInt32 = 65280
FLT_FILE_NAME_QUERY_DEFAULT: UInt32 = 256
FLT_FILE_NAME_QUERY_CACHE_ONLY: UInt32 = 512
FLT_FILE_NAME_QUERY_FILESYSTEM_ONLY: UInt32 = 768
FLT_FILE_NAME_QUERY_ALWAYS_ALLOW_CACHE_LOOKUP: UInt32 = 1024
FLT_VALID_FILE_NAME_FLAGS: UInt32 = 4278190080
FLT_FILE_NAME_REQUEST_FROM_CURRENT_PROVIDER: UInt32 = 16777216
FLT_FILE_NAME_DO_NOT_CACHE: UInt32 = 33554432
FLT_FILE_NAME_ALLOW_QUERY_ON_REPARSE: UInt32 = 67108864
FLTFL_FILE_NAME_PARSED_FINAL_COMPONENT: UInt32 = 1
FLTFL_FILE_NAME_PARSED_EXTENSION: UInt32 = 2
FLTFL_FILE_NAME_PARSED_STREAM: UInt32 = 4
FLTFL_FILE_NAME_PARSED_PARENT_DIR: UInt32 = 8
FLT_MAX_DEVICE_REPARSE_ATTEMPTS: UInt32 = 64
FLTTCFL_AUTO_REPARSE: UInt32 = 1
FLT_FLUSH_TYPE_FLUSH_AND_PURGE: UInt32 = 1
FLT_FLUSH_TYPE_FILE_DATA_ONLY: UInt32 = 2
FLT_FLUSH_TYPE_NO_SYNC: UInt32 = 4
FLT_FLUSH_TYPE_DATA_SYNC_ONLY: UInt32 = 8
VOL_PROP_FL_DAX_VOLUME: UInt32 = 1
FLT_PORT_CONNECT: UInt32 = 1
FLT_PUSH_LOCK_ENABLE_AUTO_BOOST: UInt32 = 1
FLT_PUSH_LOCK_DISABLE_AUTO_BOOST: UInt32 = 2
FLT_PUSH_LOCK_VALID_FLAGS: UInt32 = 3
GUID_ECP_FLT_CREATEFILE_TARGET: Guid = Guid('{ce08041d-f411-447f-b70d-ccee45c23fac}')
@winfunctype('FLTMGR.SYS')
def FltSetCallbackDataDirty(Data: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA)) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltClearCallbackDataDirty(Data: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA)) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltIsCallbackDataDirty(Data: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('FLTMGR.SYS')
def FltDoCompletionProcessingWhenSafe(Data: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA), FltObjects: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_RELATED_OBJECTS), CompletionContext: VoidPtr, Flags: UInt32, SafePostCallback: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_POST_OPERATION_CALLBACK, RetPostOperationStatus: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_POSTOP_CALLBACK_STATUS)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('FLTMGR.SYS')
def FltCheckAndGrowNameControl(NameCtrl: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_NAME_CONTROL), NewSize: UInt16) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltPurgeFileNameInformationCache(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltRegisterForDataScan(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltCreateSectionForDataScan(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), SectionContext: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT, DesiredAccess: UInt32, ObjectAttributes: POINTER(win32more.Windows.Wdk.Foundation.OBJECT_ATTRIBUTES), MaximumSize: POINTER(Int64), SectionPageProtection: UInt32, AllocationAttributes: UInt32, Flags: UInt32, SectionHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE), SectionObject: POINTER(VoidPtr), SectionFileSize: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltCloseSectionForDataScan(SectionContext: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltRegisterFilter(Driver: POINTER(win32more.Windows.Wdk.Foundation.DRIVER_OBJECT), Registration: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_REGISTRATION), RetFilter: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltUnregisterFilter(Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltStartFiltering(Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltGetRoutineAddress(FltMgrRoutineName: win32more.Windows.Win32.Foundation.PSTR) -> VoidPtr: ...
@winfunctype('FLTMGR.SYS')
def FltCompletePendedPreOperation(CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA), CallbackStatus: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_PREOP_CALLBACK_STATUS, Context: VoidPtr) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltCompletePendedPostOperation(CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA)) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltRequestOperationStatusCallback(Data: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA), CallbackRoutine: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_GET_OPERATION_STATUS_CALLBACK, RequesterContext: VoidPtr) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltAllocatePoolAlignedWithTag(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, PoolType: win32more.Windows.Wdk.Foundation.POOL_TYPE, NumberOfBytes: UIntPtr, Tag: UInt32) -> VoidPtr: ...
@winfunctype('FLTMGR.SYS')
def FltFreePoolAlignedWithTag(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, Buffer: VoidPtr, Tag: UInt32) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltGetFileNameInformation(CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA), NameOptions: UInt32, FileNameInformation: POINTER(POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_FILE_NAME_INFORMATION))) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltGetFileNameInformationUnsafe(FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, NameOptions: UInt32, FileNameInformation: POINTER(POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_FILE_NAME_INFORMATION))) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltReleaseFileNameInformation(FileNameInformation: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_FILE_NAME_INFORMATION)) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltReferenceFileNameInformation(FileNameInformation: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_FILE_NAME_INFORMATION)) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltParseFileName(FileName: POINTER(win32more.Windows.Win32.Foundation.UNICODE_STRING), Extension: POINTER(win32more.Windows.Win32.Foundation.UNICODE_STRING), Stream: POINTER(win32more.Windows.Win32.Foundation.UNICODE_STRING), FinalComponent: POINTER(win32more.Windows.Win32.Foundation.UNICODE_STRING)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltParseFileNameInformation(FileNameInformation: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_FILE_NAME_INFORMATION)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltGetTunneledName(CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA), FileNameInformation: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_FILE_NAME_INFORMATION), RetTunneledFileNameInformation: POINTER(POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_FILE_NAME_INFORMATION))) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltGetVolumeName(Volume: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_VOLUME, VolumeName: POINTER(win32more.Windows.Win32.Foundation.UNICODE_STRING), BufferSizeNeeded: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltGetDestinationFileNameInformation(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), RootDirectory: win32more.Windows.Win32.Foundation.HANDLE, FileName: win32more.Windows.Win32.Foundation.PWSTR, FileNameLength: UInt32, NameOptions: UInt32, RetFileNameInformation: POINTER(POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_FILE_NAME_INFORMATION))) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltIsDirectory(FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, IsDirectory: POINTER(win32more.Windows.Win32.Foundation.BOOLEAN)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltLoadFilter(FilterName: POINTER(win32more.Windows.Win32.Foundation.UNICODE_STRING)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltUnloadFilter(FilterName: POINTER(win32more.Windows.Win32.Foundation.UNICODE_STRING)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltAttachVolume(Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER, Volume: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_VOLUME, InstanceName: POINTER(win32more.Windows.Win32.Foundation.UNICODE_STRING), RetInstance: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltAttachVolumeAtAltitude(Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER, Volume: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_VOLUME, Altitude: POINTER(win32more.Windows.Win32.Foundation.UNICODE_STRING), InstanceName: POINTER(win32more.Windows.Win32.Foundation.UNICODE_STRING), RetInstance: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltDetachVolume(Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER, Volume: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_VOLUME, InstanceName: POINTER(win32more.Windows.Win32.Foundation.UNICODE_STRING)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltAllocateCallbackData(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), RetNewCallbackData: POINTER(POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA))) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltAllocateCallbackDataEx(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), Flags: UInt32, RetNewCallbackData: POINTER(POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA))) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltFreeCallbackData(CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA)) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltReuseCallbackData(CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA)) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltPerformSynchronousIo(CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA)) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltPerformAsynchronousIo(CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA), CallbackRoutine: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_COMPLETED_ASYNC_IO_CALLBACK, CallbackContext: VoidPtr) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltpTraceRedirectedFileIo(OriginatingFileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), ChildCallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltCreateNamedPipeFile(Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER, Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, FileHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE), FileObject: POINTER(POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT)), DesiredAccess: UInt32, ObjectAttributes: POINTER(win32more.Windows.Wdk.Foundation.OBJECT_ATTRIBUTES), IoStatusBlock: POINTER(win32more.Windows.Win32.System.IO.IO_STATUS_BLOCK), ShareAccess: UInt32, CreateDisposition: UInt32, CreateOptions: UInt32, NamedPipeType: UInt32, ReadMode: UInt32, CompletionMode: UInt32, MaximumInstances: UInt32, InboundQuota: UInt32, OutboundQuota: UInt32, DefaultTimeout: POINTER(Int64), DriverContext: POINTER(win32more.Windows.Wdk.System.SystemServices.IO_DRIVER_CREATE_CONTEXT)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltCreateMailslotFile(Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER, Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, FileHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE), FileObject: POINTER(POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT)), DesiredAccess: UInt32, ObjectAttributes: POINTER(win32more.Windows.Wdk.Foundation.OBJECT_ATTRIBUTES), IoStatusBlock: POINTER(win32more.Windows.Win32.System.IO.IO_STATUS_BLOCK), CreateOptions: UInt32, MailslotQuota: UInt32, MaximumMessageSize: UInt32, ReadTimeout: POINTER(Int64), DriverContext: POINTER(win32more.Windows.Wdk.System.SystemServices.IO_DRIVER_CREATE_CONTEXT)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltCreateFileEx2(Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER, Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, FileHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE), FileObject: POINTER(POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT)), DesiredAccess: UInt32, ObjectAttributes: POINTER(win32more.Windows.Wdk.Foundation.OBJECT_ATTRIBUTES), IoStatusBlock: POINTER(win32more.Windows.Win32.System.IO.IO_STATUS_BLOCK), AllocationSize: POINTER(Int64), FileAttributes: UInt32, ShareAccess: UInt32, CreateDisposition: UInt32, CreateOptions: UInt32, EaBuffer: VoidPtr, EaLength: UInt32, Flags: UInt32, DriverContext: POINTER(win32more.Windows.Wdk.System.SystemServices.IO_DRIVER_CREATE_CONTEXT)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltCreateFileEx(Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER, Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, FileHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE), FileObject: POINTER(POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT)), DesiredAccess: UInt32, ObjectAttributes: POINTER(win32more.Windows.Wdk.Foundation.OBJECT_ATTRIBUTES), IoStatusBlock: POINTER(win32more.Windows.Win32.System.IO.IO_STATUS_BLOCK), AllocationSize: POINTER(Int64), FileAttributes: UInt32, ShareAccess: UInt32, CreateDisposition: UInt32, CreateOptions: UInt32, EaBuffer: VoidPtr, EaLength: UInt32, Flags: UInt32) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltCreateFile(Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER, Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, FileHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE), DesiredAccess: UInt32, ObjectAttributes: POINTER(win32more.Windows.Wdk.Foundation.OBJECT_ATTRIBUTES), IoStatusBlock: POINTER(win32more.Windows.Win32.System.IO.IO_STATUS_BLOCK), AllocationSize: POINTER(Int64), FileAttributes: UInt32, ShareAccess: UInt32, CreateDisposition: UInt32, CreateOptions: UInt32, EaBuffer: VoidPtr, EaLength: UInt32, Flags: UInt32) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltOpenVolume(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, VolumeHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE), VolumeFileObject: POINTER(POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT))) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltReadFile(InitiatingInstance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), ByteOffset: POINTER(Int64), Length: UInt32, Buffer: VoidPtr, Flags: UInt32, BytesRead: POINTER(UInt32), CallbackRoutine: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_COMPLETED_ASYNC_IO_CALLBACK, CallbackContext: VoidPtr) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltReadFileEx(InitiatingInstance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), ByteOffset: POINTER(Int64), Length: UInt32, Buffer: VoidPtr, Flags: UInt32, BytesRead: POINTER(UInt32), CallbackRoutine: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_COMPLETED_ASYNC_IO_CALLBACK, CallbackContext: VoidPtr, Key: POINTER(UInt32), Mdl: POINTER(win32more.Windows.Wdk.Foundation.MDL)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltTagFile(InitiatingInstance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), FileTag: UInt32, Guid: POINTER(Guid), DataBuffer: VoidPtr, DataBufferLength: UInt16) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltTagFileEx(InitiatingInstance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), FileTag: UInt32, Guid: POINTER(Guid), DataBuffer: VoidPtr, DataBufferLength: UInt16, ExistingFileTag: UInt32, ExistingGuid: POINTER(Guid), Flags: UInt32) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltUntagFile(InitiatingInstance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), FileTag: UInt32, Guid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltWriteFile(InitiatingInstance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), ByteOffset: POINTER(Int64), Length: UInt32, Buffer: VoidPtr, Flags: UInt32, BytesWritten: POINTER(UInt32), CallbackRoutine: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_COMPLETED_ASYNC_IO_CALLBACK, CallbackContext: VoidPtr) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltWriteFileEx(InitiatingInstance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), ByteOffset: POINTER(Int64), Length: UInt32, Buffer: VoidPtr, Flags: UInt32, BytesWritten: POINTER(UInt32), CallbackRoutine: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_COMPLETED_ASYNC_IO_CALLBACK, CallbackContext: VoidPtr, Key: POINTER(UInt32), Mdl: POINTER(win32more.Windows.Wdk.Foundation.MDL)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltFastIoMdlRead(InitiatingInstance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), FileOffset: POINTER(Int64), Length: UInt32, LockKey: UInt32, MdlChain: POINTER(POINTER(win32more.Windows.Wdk.Foundation.MDL)), IoStatus: POINTER(win32more.Windows.Win32.System.IO.IO_STATUS_BLOCK)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('FLTMGR.SYS')
def FltFastIoMdlReadComplete(InitiatingInstance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), MdlChain: POINTER(win32more.Windows.Wdk.Foundation.MDL)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('FLTMGR.SYS')
def FltFastIoPrepareMdlWrite(InitiatingInstance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), FileOffset: POINTER(Int64), Length: UInt32, LockKey: UInt32, MdlChain: POINTER(POINTER(win32more.Windows.Wdk.Foundation.MDL)), IoStatus: POINTER(win32more.Windows.Win32.System.IO.IO_STATUS_BLOCK)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('FLTMGR.SYS')
def FltFastIoMdlWriteComplete(InitiatingInstance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), FileOffset: POINTER(Int64), MdlChain: POINTER(win32more.Windows.Wdk.Foundation.MDL)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('FLTMGR.SYS')
def FltQueryInformationByName(Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER, Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, ObjectAttributes: POINTER(win32more.Windows.Wdk.Foundation.OBJECT_ATTRIBUTES), IoStatusBlock: POINTER(win32more.Windows.Win32.System.IO.IO_STATUS_BLOCK), FileInformation: VoidPtr, Length: UInt32, FileInformationClass: win32more.Windows.Wdk.Storage.FileSystem.FILE_INFORMATION_CLASS, DriverContext: POINTER(win32more.Windows.Wdk.System.SystemServices.IO_DRIVER_CREATE_CONTEXT)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltQueryInformationFile(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), FileInformation: VoidPtr, Length: UInt32, FileInformationClass: win32more.Windows.Wdk.Storage.FileSystem.FILE_INFORMATION_CLASS, LengthReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltSetInformationFile(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), FileInformation: VoidPtr, Length: UInt32, FileInformationClass: win32more.Windows.Wdk.Storage.FileSystem.FILE_INFORMATION_CLASS) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltQueryDirectoryFile(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), FileInformation: VoidPtr, Length: UInt32, FileInformationClass: win32more.Windows.Wdk.Storage.FileSystem.FILE_INFORMATION_CLASS, ReturnSingleEntry: win32more.Windows.Win32.Foundation.BOOLEAN, FileName: POINTER(win32more.Windows.Win32.Foundation.UNICODE_STRING), RestartScan: win32more.Windows.Win32.Foundation.BOOLEAN, LengthReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltQueryDirectoryFileEx(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), FileInformation: VoidPtr, Length: UInt32, FileInformationClass: win32more.Windows.Wdk.Storage.FileSystem.FILE_INFORMATION_CLASS, QueryFlags: UInt32, FileName: POINTER(win32more.Windows.Win32.Foundation.UNICODE_STRING), LengthReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltQueryQuotaInformationFile(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), IoStatusBlock: POINTER(win32more.Windows.Win32.System.IO.IO_STATUS_BLOCK), Buffer: VoidPtr, Length: UInt32, ReturnSingleEntry: win32more.Windows.Win32.Foundation.BOOLEAN, SidList: VoidPtr, SidListLength: UInt32, StartSid: POINTER(UInt32), RestartScan: win32more.Windows.Win32.Foundation.BOOLEAN, LengthReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltSetQuotaInformationFile(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), Buffer: VoidPtr, Length: UInt32) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltQueryEaFile(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), ReturnedEaData: VoidPtr, Length: UInt32, ReturnSingleEntry: win32more.Windows.Win32.Foundation.BOOLEAN, EaList: VoidPtr, EaListLength: UInt32, EaIndex: POINTER(UInt32), RestartScan: win32more.Windows.Win32.Foundation.BOOLEAN, LengthReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltSetEaFile(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), EaBuffer: VoidPtr, Length: UInt32) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltQueryVolumeInformationFile(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), FsInformation: VoidPtr, Length: UInt32, FsInformationClass: win32more.Windows.Wdk.Storage.FileSystem.FS_INFORMATION_CLASS, LengthReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltQuerySecurityObject(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), SecurityInformation: UInt32, SecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, Length: UInt32, LengthNeeded: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltSetSecurityObject(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), SecurityInformation: UInt32, SecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltFlushBuffers(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltFlushBuffers2(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), FlushType: UInt32, CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltFsControlFile(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), FsControlCode: UInt32, InputBuffer: VoidPtr, InputBufferLength: UInt32, OutputBuffer: VoidPtr, OutputBufferLength: UInt32, LengthReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltDeviceIoControlFile(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), IoControlCode: UInt32, InputBuffer: VoidPtr, InputBufferLength: UInt32, OutputBuffer: VoidPtr, OutputBufferLength: UInt32, LengthReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltReissueSynchronousIo(InitiatingInstance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA)) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltClose(FileHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltCancelFileOpen(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT)) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltCreateSystemVolumeInformationFolder(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltSupportsFileContextsEx(FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('FLTMGR.SYS')
def FltSupportsFileContexts(FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('FLTMGR.SYS')
def FltSupportsStreamContexts(FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('FLTMGR.SYS')
def FltSupportsStreamHandleContexts(FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('FLTMGR.SYS')
def FltAllocateContext(Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER, ContextType: UInt16, ContextSize: UIntPtr, PoolType: win32more.Windows.Wdk.Foundation.POOL_TYPE, ReturnedContext: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltGetContexts(FltObjects: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_RELATED_OBJECTS), DesiredContexts: UInt16, Contexts: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_RELATED_CONTEXTS)) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltReleaseContexts(Contexts: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_RELATED_CONTEXTS)) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltGetContextsEx(FltObjects: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_RELATED_OBJECTS), DesiredContexts: UInt16, ContextsSize: UIntPtr, Contexts: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_RELATED_CONTEXTS_EX)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltReleaseContextsEx(ContextsSize: UIntPtr, Contexts: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_RELATED_CONTEXTS_EX)) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltSetVolumeContext(Volume: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_VOLUME, Operation: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_SET_CONTEXT_OPERATION, NewContext: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT, OldContext: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltSetInstanceContext(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, Operation: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_SET_CONTEXT_OPERATION, NewContext: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT, OldContext: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltSetFileContext(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), Operation: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_SET_CONTEXT_OPERATION, NewContext: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT, OldContext: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltSetStreamContext(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), Operation: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_SET_CONTEXT_OPERATION, NewContext: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT, OldContext: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltSetStreamHandleContext(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), Operation: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_SET_CONTEXT_OPERATION, NewContext: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT, OldContext: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltSetTransactionContext(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, Transaction: POINTER(win32more.Windows.Wdk.Foundation.KTRANSACTION), Operation: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_SET_CONTEXT_OPERATION, NewContext: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT, OldContext: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltDeleteContext(Context: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltDeleteVolumeContext(Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER, Volume: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_VOLUME, OldContext: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltDeleteInstanceContext(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, OldContext: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltDeleteFileContext(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), OldContext: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltDeleteStreamContext(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), OldContext: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltDeleteStreamHandleContext(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), OldContext: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltDeleteTransactionContext(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, Transaction: POINTER(win32more.Windows.Wdk.Foundation.KTRANSACTION), OldContext: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltGetVolumeContext(Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER, Volume: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_VOLUME, Context: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltGetInstanceContext(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, Context: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltGetFileContext(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), Context: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltGetStreamContext(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), Context: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltGetStreamHandleContext(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), Context: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltGetTransactionContext(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, Transaction: POINTER(win32more.Windows.Wdk.Foundation.KTRANSACTION), Context: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltGetSectionContext(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), Context: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltReferenceContext(Context: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltReleaseContext(Context: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltGetFilterFromName(FilterName: POINTER(win32more.Windows.Win32.Foundation.UNICODE_STRING), RetFilter: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltGetVolumeFromName(Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER, VolumeName: POINTER(win32more.Windows.Win32.Foundation.UNICODE_STRING), RetVolume: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_VOLUME)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltGetVolumeInstanceFromName(Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER, Volume: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_VOLUME, InstanceName: POINTER(win32more.Windows.Win32.Foundation.UNICODE_STRING), RetInstance: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltGetVolumeFromInstance(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, RetVolume: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_VOLUME)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltGetFilterFromInstance(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, RetFilter: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltGetVolumeFromFileObject(Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER, FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), RetVolume: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_VOLUME)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltGetVolumeFromDeviceObject(Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER, DeviceObject: POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT), RetVolume: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_VOLUME)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltIsFltMgrVolumeDeviceObject(DeviceObject: POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('FLTMGR.SYS')
def FltGetDeviceObject(Volume: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_VOLUME, DeviceObject: POINTER(POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT))) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltGetDiskDeviceObject(Volume: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_VOLUME, DiskDeviceObject: POINTER(POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT))) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltGetLowerInstance(CurrentInstance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, LowerInstance: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltGetUpperInstance(CurrentInstance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, UpperInstance: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltGetTopInstance(Volume: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_VOLUME, Instance: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltGetBottomInstance(Volume: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_VOLUME, Instance: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltCompareInstanceAltitudes(Instance1: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, Instance2: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE) -> Int32: ...
@winfunctype('FLTMGR.SYS')
def FltGetFilterInformation(Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER, InformationClass: win32more.Windows.Win32.Storage.InstallableFileSystems.FILTER_INFORMATION_CLASS, Buffer: VoidPtr, BufferSize: UInt32, BytesReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltGetInstanceInformation(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, InformationClass: win32more.Windows.Win32.Storage.InstallableFileSystems.INSTANCE_INFORMATION_CLASS, Buffer: VoidPtr, BufferSize: UInt32, BytesReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltGetVolumeInformation(Volume: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_VOLUME, InformationClass: win32more.Windows.Win32.Storage.InstallableFileSystems.FILTER_VOLUME_INFORMATION_CLASS, Buffer: VoidPtr, BufferSize: UInt32, BytesReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltGetVolumeProperties(Volume: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_VOLUME, VolumeProperties: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_VOLUME_PROPERTIES), VolumePropertiesLength: UInt32, LengthReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltIsVolumeWritable(FltObject: VoidPtr, IsWritable: POINTER(win32more.Windows.Win32.Foundation.BOOLEAN)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltGetFileSystemType(FltObject: VoidPtr, FileSystemType: POINTER(win32more.Windows.Win32.Storage.InstallableFileSystems.FLT_FILESYSTEM_TYPE)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltIsVolumeSnapshot(FltObject: VoidPtr, IsSnapshotVolume: POINTER(win32more.Windows.Win32.Foundation.BOOLEAN)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltGetVolumeGuidName(Volume: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_VOLUME, VolumeGuidName: POINTER(win32more.Windows.Win32.Foundation.UNICODE_STRING), BufferSizeNeeded: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltQueryVolumeInformation(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, Iosb: POINTER(win32more.Windows.Win32.System.IO.IO_STATUS_BLOCK), FsInformation: VoidPtr, Length: UInt32, FsInformationClass: win32more.Windows.Wdk.Storage.FileSystem.FS_INFORMATION_CLASS) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltSetVolumeInformation(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, Iosb: POINTER(win32more.Windows.Win32.System.IO.IO_STATUS_BLOCK), FsInformation: VoidPtr, Length: UInt32, FsInformationClass: win32more.Windows.Wdk.Storage.FileSystem.FS_INFORMATION_CLASS) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltEnumerateFilters(FilterList: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER), FilterListSize: UInt32, NumberFiltersReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltEnumerateVolumes(Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER, VolumeList: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_VOLUME), VolumeListSize: UInt32, NumberVolumesReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltEnumerateInstances(Volume: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_VOLUME, Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER, InstanceList: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE), InstanceListSize: UInt32, NumberInstancesReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltEnumerateFilterInformation(Index: UInt32, InformationClass: win32more.Windows.Win32.Storage.InstallableFileSystems.FILTER_INFORMATION_CLASS, Buffer: VoidPtr, BufferSize: UInt32, BytesReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltEnumerateInstanceInformationByFilter(Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER, Index: UInt32, InformationClass: win32more.Windows.Win32.Storage.InstallableFileSystems.INSTANCE_INFORMATION_CLASS, Buffer: VoidPtr, BufferSize: UInt32, BytesReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltEnumerateInstanceInformationByVolume(Volume: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_VOLUME, Index: UInt32, InformationClass: win32more.Windows.Win32.Storage.InstallableFileSystems.INSTANCE_INFORMATION_CLASS, Buffer: VoidPtr, BufferSize: UInt32, BytesReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltEnumerateInstanceInformationByVolumeName(VolumeName: POINTER(win32more.Windows.Win32.Foundation.UNICODE_STRING), Index: UInt32, InformationClass: win32more.Windows.Win32.Storage.InstallableFileSystems.INSTANCE_INFORMATION_CLASS, Buffer: VoidPtr, BufferSize: UInt32, BytesReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltEnumerateInstanceInformationByDeviceObject(DeviceObject: POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT), Index: UInt32, InformationClass: win32more.Windows.Win32.Storage.InstallableFileSystems.INSTANCE_INFORMATION_CLASS, Buffer: VoidPtr, BufferSize: UInt32, BytesReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltEnumerateVolumeInformation(Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER, Index: UInt32, InformationClass: win32more.Windows.Win32.Storage.InstallableFileSystems.FILTER_VOLUME_INFORMATION_CLASS, Buffer: VoidPtr, BufferSize: UInt32, BytesReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltObjectReference(FltObject: VoidPtr) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltObjectDereference(FltObject: VoidPtr) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltCreateCommunicationPort(Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER, ServerPort: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_PORT), ObjectAttributes: POINTER(win32more.Windows.Wdk.Foundation.OBJECT_ATTRIBUTES), ServerPortCookie: VoidPtr, ConnectNotifyCallback: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONNECT_NOTIFY, DisconnectNotifyCallback: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_DISCONNECT_NOTIFY, MessageNotifyCallback: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_MESSAGE_NOTIFY, MaxConnections: Int32) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltCloseCommunicationPort(ServerPort: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_PORT) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltCloseClientPort(Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER, ClientPort: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_PORT)) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltSendMessage(Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER, ClientPort: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_PORT), SenderBuffer: VoidPtr, SenderBufferLength: UInt32, ReplyBuffer: VoidPtr, ReplyLength: POINTER(UInt32), Timeout: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltBuildDefaultSecurityDescriptor(SecurityDescriptor: POINTER(win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR), DesiredAccess: UInt32) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltFreeSecurityDescriptor(SecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltCancelIo(CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('FLTMGR.SYS')
def FltSetCancelCompletion(CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA), CanceledCallback: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_COMPLETE_CANCELED_CALLBACK) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltClearCancelCompletion(CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltIsIoCanceled(CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('FLTMGR.SYS')
def FltAllocateDeferredIoWorkItem() -> win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_DEFERRED_IO_WORKITEM: ...
@winfunctype('FLTMGR.SYS')
def FltFreeDeferredIoWorkItem(FltWorkItem: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_DEFERRED_IO_WORKITEM) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltAllocateGenericWorkItem() -> win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_GENERIC_WORKITEM: ...
@winfunctype('FLTMGR.SYS')
def FltFreeGenericWorkItem(FltWorkItem: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_GENERIC_WORKITEM) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltQueueDeferredIoWorkItem(FltWorkItem: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_DEFERRED_IO_WORKITEM, Data: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA), WorkerRoutine: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_DEFERRED_IO_WORKITEM_ROUTINE, QueueType: win32more.Windows.Wdk.System.SystemServices.WORK_QUEUE_TYPE, Context: VoidPtr) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltQueueGenericWorkItem(FltWorkItem: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_GENERIC_WORKITEM, FltObject: VoidPtr, WorkerRoutine: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_GENERIC_WORKITEM_ROUTINE, QueueType: win32more.Windows.Wdk.System.SystemServices.WORK_QUEUE_TYPE, Context: VoidPtr) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltLockUserBuffer(CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltDecodeParameters(CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA), MdlAddressPointer: POINTER(POINTER(POINTER(win32more.Windows.Wdk.Foundation.MDL))), Buffer: POINTER(POINTER(VoidPtr)), Length: POINTER(POINTER(UInt32)), DesiredAccess: POINTER(win32more.Windows.Wdk.System.SystemServices.LOCK_OPERATION)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltGetSwappedBufferMdlAddress(CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA)) -> POINTER(win32more.Windows.Wdk.Foundation.MDL): ...
@winfunctype('FLTMGR.SYS')
def FltRetainSwappedBufferMdlAddress(CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA)) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltGetNewSystemBufferAddress(CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA)) -> VoidPtr: ...
@winfunctype('FLTMGR.SYS')
def FltCbdqInitialize(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, Cbdq: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA_QUEUE), CbdqInsertIo: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CALLBACK_DATA_QUEUE_INSERT_IO, CbdqRemoveIo: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CALLBACK_DATA_QUEUE_REMOVE_IO, CbdqPeekNextIo: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CALLBACK_DATA_QUEUE_PEEK_NEXT_IO, CbdqAcquire: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CALLBACK_DATA_QUEUE_ACQUIRE, CbdqRelease: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CALLBACK_DATA_QUEUE_RELEASE, CbdqCompleteCanceledIo: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CALLBACK_DATA_QUEUE_COMPLETE_CANCELED_IO) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltCbdqEnable(Cbdq: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA_QUEUE)) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltCbdqDisable(Cbdq: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA_QUEUE)) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltCbdqInsertIo(Cbdq: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA_QUEUE), Cbd: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA), Context: POINTER(win32more.Windows.Wdk.System.SystemServices.IO_CSQ_IRP_CONTEXT), InsertContext: VoidPtr) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltCbdqRemoveIo(Cbdq: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA_QUEUE), Context: POINTER(win32more.Windows.Wdk.System.SystemServices.IO_CSQ_IRP_CONTEXT)) -> POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA): ...
@winfunctype('FLTMGR.SYS')
def FltCbdqRemoveNextIo(Cbdq: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA_QUEUE), PeekContext: VoidPtr) -> POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA): ...
@winfunctype('FLTMGR.SYS')
def FltInitializeOplock(Oplock: POINTER(VoidPtr)) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltUninitializeOplock(Oplock: POINTER(VoidPtr)) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltOplockFsctrl(Oplock: POINTER(VoidPtr), CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA), OpenCount: UInt32) -> win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_PREOP_CALLBACK_STATUS: ...
@winfunctype('FLTMGR.SYS')
def FltCheckOplock(Oplock: POINTER(VoidPtr), CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA), Context: VoidPtr, WaitCompletionRoutine: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLTOPLOCK_WAIT_COMPLETE_ROUTINE, PrePostCallbackDataRoutine: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLTOPLOCK_PREPOST_CALLBACKDATA_ROUTINE) -> win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_PREOP_CALLBACK_STATUS: ...
@winfunctype('FLTMGR.SYS')
def FltOplockIsFastIoPossible(Oplock: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('FLTMGR.SYS')
def FltCurrentBatchOplock(Oplock: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('FLTMGR.SYS')
def FltCheckOplockEx(Oplock: POINTER(VoidPtr), CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA), Flags: UInt32, Context: VoidPtr, WaitCompletionRoutine: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLTOPLOCK_WAIT_COMPLETE_ROUTINE, PrePostCallbackDataRoutine: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLTOPLOCK_PREPOST_CALLBACKDATA_ROUTINE) -> win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_PREOP_CALLBACK_STATUS: ...
@winfunctype('FLTMGR.SYS')
def FltCurrentOplock(Oplock: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('FLTMGR.SYS')
def FltCurrentOplockH(Oplock: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('FLTMGR.SYS')
def FltOplockBreakH(Oplock: POINTER(VoidPtr), CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA), Flags: UInt32, Context: VoidPtr, WaitCompletionRoutine: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLTOPLOCK_WAIT_COMPLETE_ROUTINE, PrePostCallbackDataRoutine: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLTOPLOCK_PREPOST_CALLBACKDATA_ROUTINE) -> win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_PREOP_CALLBACK_STATUS: ...
@winfunctype('FLTMGR.SYS')
def FltOplockBreakToNone(Oplock: POINTER(VoidPtr), CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA), Context: VoidPtr, WaitCompletionRoutine: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLTOPLOCK_WAIT_COMPLETE_ROUTINE, PrePostCallbackDataRoutine: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLTOPLOCK_PREPOST_CALLBACKDATA_ROUTINE) -> win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_PREOP_CALLBACK_STATUS: ...
@winfunctype('FLTMGR.SYS')
def FltOplockBreakToNoneEx(Oplock: POINTER(VoidPtr), CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA), Flags: UInt32, Context: VoidPtr, WaitCompletionRoutine: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLTOPLOCK_WAIT_COMPLETE_ROUTINE, PrePostCallbackDataRoutine: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLTOPLOCK_PREPOST_CALLBACKDATA_ROUTINE) -> win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_PREOP_CALLBACK_STATUS: ...
@winfunctype('FLTMGR.SYS')
def FltOplockIsSharedRequest(CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('FLTMGR.SYS')
def FltOplockFsctrlEx(Oplock: POINTER(VoidPtr), CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA), OpenCount: UInt32, Flags: UInt32) -> win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_PREOP_CALLBACK_STATUS: ...
@winfunctype('FLTMGR.SYS')
def FltOplockKeysEqual(Fo1: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), Fo2: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('FLTMGR.SYS')
def FltInitializeFileLock(FileLock: POINTER(win32more.Windows.Wdk.Storage.FileSystem.FILE_LOCK)) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltUninitializeFileLock(FileLock: POINTER(win32more.Windows.Wdk.Storage.FileSystem.FILE_LOCK)) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltAllocateFileLock(CompleteLockCallbackDataRoutine: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_COMPLETE_LOCK_CALLBACK_DATA_ROUTINE, UnlockRoutine: win32more.Windows.Wdk.Storage.FileSystem.PUNLOCK_ROUTINE) -> POINTER(win32more.Windows.Wdk.Storage.FileSystem.FILE_LOCK): ...
@winfunctype('FLTMGR.SYS')
def FltFreeFileLock(FileLock: POINTER(win32more.Windows.Wdk.Storage.FileSystem.FILE_LOCK)) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltProcessFileLock(FileLock: POINTER(win32more.Windows.Wdk.Storage.FileSystem.FILE_LOCK), CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA), Context: VoidPtr) -> win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_PREOP_CALLBACK_STATUS: ...
@winfunctype('FLTMGR.SYS')
def FltCheckLockForReadAccess(FileLock: POINTER(win32more.Windows.Wdk.Storage.FileSystem.FILE_LOCK), CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('FLTMGR.SYS')
def FltCheckLockForWriteAccess(FileLock: POINTER(win32more.Windows.Wdk.Storage.FileSystem.FILE_LOCK), CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('FLTMGR.SYS')
def FltAcquireResourceExclusive(Resource: POINTER(win32more.Windows.Wdk.Foundation.ERESOURCE)) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltAcquireResourceShared(Resource: POINTER(win32more.Windows.Wdk.Foundation.ERESOURCE)) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltReleaseResource(Resource: POINTER(win32more.Windows.Wdk.Foundation.ERESOURCE)) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltInitializePushLock(PushLock: POINTER(UIntPtr)) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltDeletePushLock(PushLock: POINTER(UIntPtr)) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltAcquirePushLockExclusive(PushLock: POINTER(UIntPtr)) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltAcquirePushLockShared(PushLock: POINTER(UIntPtr)) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltReleasePushLock(PushLock: POINTER(UIntPtr)) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltAcquirePushLockExclusiveEx(PushLock: POINTER(UIntPtr), Flags: UInt32) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltAcquirePushLockSharedEx(PushLock: POINTER(UIntPtr), Flags: UInt32) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltReleasePushLockEx(PushLock: POINTER(UIntPtr), Flags: UInt32) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltCancellableWaitForSingleObject(Object: VoidPtr, Timeout: POINTER(Int64), CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltCancellableWaitForMultipleObjects(Count: UInt32, ObjectArray: POINTER(VoidPtr), WaitType: win32more.Windows.Win32.System.Kernel.WAIT_TYPE, Timeout: POINTER(Int64), WaitBlockArray: POINTER(win32more.Windows.Wdk.Foundation.KWAIT_BLOCK), CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltIsOperationSynchronous(CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('FLTMGR.SYS')
def FltIs32bitProcess(CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('FLTMGR.SYS')
def FltGetRequestorProcess(CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA)) -> win32more.Windows.Wdk.Foundation.PEPROCESS: ...
@winfunctype('FLTMGR.SYS')
def FltGetRequestorProcessId(CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA)) -> UInt32: ...
@winfunctype('FLTMGR.SYS')
def FltGetRequestorProcessIdEx(CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA)) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('FLTMGR.SYS')
def FltNotifyFilterChangeDirectory(NotifySync: win32more.Windows.Wdk.Foundation.PNOTIFY_SYNC, NotifyList: POINTER(win32more.Windows.Win32.System.Kernel.LIST_ENTRY), FsContext: VoidPtr, FullDirectoryName: POINTER(win32more.Windows.Win32.System.Kernel.STRING), WatchTree: win32more.Windows.Win32.Foundation.BOOLEAN, IgnoreBuffer: win32more.Windows.Win32.Foundation.BOOLEAN, CompletionFilter: UInt32, NotifyCallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA), TraverseCallback: win32more.Windows.Wdk.Storage.FileSystem.PCHECK_FOR_TRAVERSE_ACCESS, SubjectContext: POINTER(win32more.Windows.Wdk.Foundation.SECURITY_SUBJECT_CONTEXT), FilterCallback: win32more.Windows.Wdk.Storage.FileSystem.PFILTER_REPORT_CHANGE) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltGetRequestorSessionId(CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA), SessionId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltAdjustDeviceStackSizeForIoRedirection(SourceInstance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, TargetInstance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, SourceDeviceStackSizeModified: POINTER(win32more.Windows.Win32.Foundation.BOOLEAN)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltIsIoRedirectionAllowed(SourceInstance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, TargetInstance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, RedirectionAllowed: POINTER(win32more.Windows.Win32.Foundation.BOOLEAN)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltIsIoRedirectionAllowedForOperation(Data: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA), TargetInstance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, RedirectionAllowedThisIo: POINTER(win32more.Windows.Win32.Foundation.BOOLEAN), RedirectionAllowedAllIo: POINTER(win32more.Windows.Win32.Foundation.BOOLEAN)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltVetoBypassIo(CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA), FltObjects: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_RELATED_OBJECTS), OperationStatus: win32more.Windows.Win32.Foundation.NTSTATUS, FailureReason: POINTER(win32more.Windows.Win32.Foundation.UNICODE_STRING)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltEnlistInTransaction(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, Transaction: POINTER(win32more.Windows.Wdk.Foundation.KTRANSACTION), TransactionContext: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT, NotificationMask: UInt32) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltRollbackEnlistment(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, Transaction: POINTER(win32more.Windows.Wdk.Foundation.KTRANSACTION), TransactionContext: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltPrePrepareComplete(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, Transaction: POINTER(win32more.Windows.Wdk.Foundation.KTRANSACTION), TransactionContext: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltPrepareComplete(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, Transaction: POINTER(win32more.Windows.Wdk.Foundation.KTRANSACTION), TransactionContext: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltCommitComplete(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, Transaction: POINTER(win32more.Windows.Wdk.Foundation.KTRANSACTION), TransactionContext: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltCommitFinalizeComplete(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, Transaction: POINTER(win32more.Windows.Wdk.Foundation.KTRANSACTION), TransactionContext: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltRollbackComplete(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, Transaction: POINTER(win32more.Windows.Wdk.Foundation.KTRANSACTION), TransactionContext: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltAllocateExtraCreateParameterList(Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER, Flags: UInt32, EcpList: POINTER(POINTER(win32more.Windows.Wdk.Foundation.ECP_LIST))) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltAllocateExtraCreateParameter(Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER, EcpType: POINTER(Guid), SizeOfContext: UInt32, Flags: UInt32, CleanupCallback: win32more.Windows.Wdk.Storage.FileSystem.PFSRTL_EXTRA_CREATE_PARAMETER_CLEANUP_CALLBACK, PoolTag: UInt32, EcpContext: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltInitExtraCreateParameterLookasideList(Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER, Lookaside: VoidPtr, Flags: UInt32, Size: UIntPtr, Tag: UInt32) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltDeleteExtraCreateParameterLookasideList(Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER, Lookaside: VoidPtr, Flags: UInt32) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltAllocateExtraCreateParameterFromLookasideList(Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER, EcpType: POINTER(Guid), SizeOfContext: UInt32, Flags: UInt32, CleanupCallback: win32more.Windows.Wdk.Storage.FileSystem.PFSRTL_EXTRA_CREATE_PARAMETER_CLEANUP_CALLBACK, LookasideList: VoidPtr, EcpContext: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltInsertExtraCreateParameter(Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER, EcpList: POINTER(win32more.Windows.Wdk.Foundation.ECP_LIST), EcpContext: VoidPtr) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltFindExtraCreateParameter(Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER, EcpList: POINTER(win32more.Windows.Wdk.Foundation.ECP_LIST), EcpType: POINTER(Guid), EcpContext: POINTER(VoidPtr), EcpContextSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltRemoveExtraCreateParameter(Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER, EcpList: POINTER(win32more.Windows.Wdk.Foundation.ECP_LIST), EcpType: POINTER(Guid), EcpContext: POINTER(VoidPtr), EcpContextSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltFreeExtraCreateParameterList(Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER, EcpList: POINTER(win32more.Windows.Wdk.Foundation.ECP_LIST)) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltFreeExtraCreateParameter(Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER, EcpContext: VoidPtr) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltGetEcpListFromCallbackData(Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER, CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA), EcpList: POINTER(POINTER(win32more.Windows.Wdk.Foundation.ECP_LIST))) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltSetEcpListIntoCallbackData(Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER, CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA), EcpList: POINTER(win32more.Windows.Wdk.Foundation.ECP_LIST)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltGetNextExtraCreateParameter(Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER, EcpList: POINTER(win32more.Windows.Wdk.Foundation.ECP_LIST), CurrentEcpContext: VoidPtr, NextEcpType: POINTER(Guid), NextEcpContext: POINTER(VoidPtr), NextEcpContextSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltAcknowledgeEcp(Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER, EcpContext: VoidPtr) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltIsEcpAcknowledged(Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER, EcpContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('FLTMGR.SYS')
def FltIsEcpFromUserMode(Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER, EcpContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('FLTMGR.SYS')
def FltPrepareToReuseEcp(Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER, EcpContext: VoidPtr) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltAddOpenReparseEntry(Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER, Data: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA), OpenReparseEntry: POINTER(win32more.Windows.Wdk.Storage.FileSystem.OPEN_REPARSE_LIST_ENTRY)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltRemoveOpenReparseEntry(Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER, Data: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA), OpenReparseEntry: POINTER(win32more.Windows.Wdk.Storage.FileSystem.OPEN_REPARSE_LIST_ENTRY)) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltCopyOpenReparseList(Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER, Data: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA), EcpList: POINTER(win32more.Windows.Wdk.Foundation.ECP_LIST)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltFreeOpenReparseList(Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER, EcpList: POINTER(win32more.Windows.Wdk.Foundation.ECP_LIST)) -> Void: ...
@winfunctype('FLTMGR.SYS')
def FltRequestFileInfoOnCreateCompletion(Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER, Data: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA), InfoClassFlags: UInt32) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltRetrieveFileInfoOnCreateCompletion(Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER, Data: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA), InfoClass: UInt32, Size: POINTER(UInt32)) -> VoidPtr: ...
@winfunctype('FLTMGR.SYS')
def FltRetrieveFileInfoOnCreateCompletionEx(Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER, Data: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA), InfoClass: UInt32, RetInfoSize: POINTER(UInt32), RetInfoBuffer: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltRetrieveIoPriorityInfo(Data: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA), FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), Thread: win32more.Windows.Wdk.Foundation.PETHREAD, PriorityInfo: POINTER(win32more.Windows.Wdk.Storage.FileSystem.IO_PRIORITY_INFO)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltApplyPriorityInfoThread(InputPriorityInfo: POINTER(win32more.Windows.Wdk.Storage.FileSystem.IO_PRIORITY_INFO), OutputPriorityInfo: POINTER(win32more.Windows.Wdk.Storage.FileSystem.IO_PRIORITY_INFO), Thread: win32more.Windows.Wdk.Foundation.PETHREAD) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltGetIoPriorityHint(Data: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA)) -> win32more.Windows.Wdk.Foundation.IO_PRIORITY_HINT: ...
@winfunctype('FLTMGR.SYS')
def FltGetIoPriorityHintFromCallbackData(Data: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA)) -> win32more.Windows.Wdk.Foundation.IO_PRIORITY_HINT: ...
@winfunctype('FLTMGR.SYS')
def FltSetIoPriorityHintIntoCallbackData(Data: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA), PriorityHint: win32more.Windows.Wdk.Foundation.IO_PRIORITY_HINT) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltGetIoPriorityHintFromFileObject(FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT)) -> win32more.Windows.Wdk.Foundation.IO_PRIORITY_HINT: ...
@winfunctype('FLTMGR.SYS')
def FltSetIoPriorityHintIntoFileObject(FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), PriorityHint: win32more.Windows.Wdk.Foundation.IO_PRIORITY_HINT) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltGetIoPriorityHintFromThread(Thread: win32more.Windows.Wdk.Foundation.PETHREAD) -> win32more.Windows.Wdk.Foundation.IO_PRIORITY_HINT: ...
@winfunctype('FLTMGR.SYS')
def FltSetIoPriorityHintIntoThread(Thread: win32more.Windows.Wdk.Foundation.PETHREAD, PriorityHint: win32more.Windows.Wdk.Foundation.IO_PRIORITY_HINT) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltGetActivityIdCallbackData(CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA), Guid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltSetActivityIdCallbackData(CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA), Guid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltPropagateActivityIdToThread(CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA), PropagateId: POINTER(Guid), OriginalId: POINTER(POINTER(Guid))) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltGetFsZeroingOffset(Data: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA), ZeroingOffset: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltSetFsZeroingOffsetRequired(Data: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltSetFsZeroingOffset(Data: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA), ZeroingOffset: UInt32) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltGetIoAttributionHandleFromCallbackData(Data: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA)) -> VoidPtr: ...
@winfunctype('FLTMGR.SYS')
def FltPropagateIrpExtension(SourceData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA), TargetData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA), Flags: UInt32) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('FLTMGR.SYS')
def FltGetIrpName(IrpMajorCode: Byte) -> win32more.Windows.Win32.Foundation.PSTR: ...
class FLT_CALLBACK_DATA(Structure):
    Flags: UInt32
    Thread: win32more.Windows.Wdk.Foundation.PETHREAD
    Iopb: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_IO_PARAMETER_BLOCK)
    IoStatus: win32more.Windows.Win32.System.IO.IO_STATUS_BLOCK
    TagData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_TAG_DATA_BUFFER)
    Anonymous: _Anonymous_e__Union
    RequestorMode: SByte
    _anonymous_ = ('Anonymous',)
    class _Anonymous_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        FilterContext: VoidPtr * 4
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            QueueLinks: win32more.Windows.Win32.System.Kernel.LIST_ENTRY
            QueueContext: VoidPtr * 2
class FLT_CALLBACK_DATA_QUEUE(Structure):
    Csq: win32more.Windows.Wdk.System.SystemServices.IO_CSQ
    Flags: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA_QUEUE_FLAGS
    Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE
    InsertIo: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CALLBACK_DATA_QUEUE_INSERT_IO
    RemoveIo: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CALLBACK_DATA_QUEUE_REMOVE_IO
    PeekNextIo: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CALLBACK_DATA_QUEUE_PEEK_NEXT_IO
    Acquire: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CALLBACK_DATA_QUEUE_ACQUIRE
    Release: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CALLBACK_DATA_QUEUE_RELEASE
    CompleteCanceledIo: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CALLBACK_DATA_QUEUE_COMPLETE_CANCELED_IO
FLT_CALLBACK_DATA_QUEUE_FLAGS = Int32
class FLT_CONTEXT_REGISTRATION(Structure):
    ContextType: UInt16
    Flags: UInt16
    ContextCleanupCallback: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT_CLEANUP_CALLBACK
    Size: UIntPtr
    PoolTag: UInt32
    ContextAllocateCallback: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT_ALLOCATE_CALLBACK
    ContextFreeCallback: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT_FREE_CALLBACK
    Reserved1: VoidPtr
class FLT_CREATEFILE_TARGET_ECP_CONTEXT(Structure):
    Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE
    Volume: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_VOLUME
    FileNameInformation: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_FILE_NAME_INFORMATION)
    Flags: UInt16
class FLT_FILE_NAME_INFORMATION(Structure):
    Size: UInt16
    NamesParsed: UInt16
    Format: UInt32
    Name: win32more.Windows.Win32.Foundation.UNICODE_STRING
    Volume: win32more.Windows.Win32.Foundation.UNICODE_STRING
    Share: win32more.Windows.Win32.Foundation.UNICODE_STRING
    Extension: win32more.Windows.Win32.Foundation.UNICODE_STRING
    Stream: win32more.Windows.Win32.Foundation.UNICODE_STRING
    FinalComponent: win32more.Windows.Win32.Foundation.UNICODE_STRING
    ParentDir: win32more.Windows.Win32.Foundation.UNICODE_STRING
class FLT_IO_PARAMETER_BLOCK(Structure):
    IrpFlags: UInt32
    MajorFunction: Byte
    MinorFunction: Byte
    OperationFlags: Byte
    Reserved: Byte
    TargetFileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT)
    TargetInstance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE
    Parameters: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_PARAMETERS
class FLT_NAME_CONTROL(Structure):
    Name: win32more.Windows.Win32.Foundation.UNICODE_STRING
class FLT_OPERATION_REGISTRATION(Structure):
    MajorFunction: Byte
    Flags: UInt32
    PreOperation: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_PRE_OPERATION_CALLBACK
    PostOperation: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_POST_OPERATION_CALLBACK
    Reserved1: VoidPtr
class FLT_PARAMETERS(Union):
    Create: _Create_e__Struct
    CreatePipe: _CreatePipe_e__Struct
    CreateMailslot: _CreateMailslot_e__Struct
    Read: _Read_e__Struct
    Write: _Write_e__Struct
    QueryFileInformation: _QueryFileInformation_e__Struct
    SetFileInformation: _SetFileInformation_e__Struct
    QueryEa: _QueryEa_e__Struct
    SetEa: _SetEa_e__Struct
    QueryVolumeInformation: _QueryVolumeInformation_e__Struct
    SetVolumeInformation: _SetVolumeInformation_e__Struct
    DirectoryControl: _DirectoryControl_e__Union
    FileSystemControl: _FileSystemControl_e__Union
    DeviceIoControl: _DeviceIoControl_e__Union
    LockControl: _LockControl_e__Struct
    QuerySecurity: _QuerySecurity_e__Struct
    SetSecurity: _SetSecurity_e__Struct
    WMI: _WMI_e__Struct
    QueryQuota: _QueryQuota_e__Struct
    SetQuota: _SetQuota_e__Struct
    Pnp: _Pnp_e__Union
    AcquireForSectionSynchronization: _AcquireForSectionSynchronization_e__Struct
    AcquireForModifiedPageWriter: _AcquireForModifiedPageWriter_e__Struct
    ReleaseForModifiedPageWriter: _ReleaseForModifiedPageWriter_e__Struct
    QueryOpen: _QueryOpen_e__Struct
    FastIoCheckIfPossible: _FastIoCheckIfPossible_e__Struct
    NetworkQueryOpen: _NetworkQueryOpen_e__Struct
    MdlRead: _MdlRead_e__Struct
    MdlReadComplete: _MdlReadComplete_e__Struct
    PrepareMdlWrite: _PrepareMdlWrite_e__Struct
    MdlWriteComplete: _MdlWriteComplete_e__Struct
    MountVolume: _MountVolume_e__Struct
    Others: _Others_e__Struct
    class _Create_e__Struct(Structure):
        SecurityContext: POINTER(win32more.Windows.Wdk.Foundation.IO_SECURITY_CONTEXT)
        Options: UInt32
        FileAttributes: UInt16
        ShareAccess: UInt16
        EaLength: UInt32
        EaBuffer: VoidPtr
        AllocationSize: Int64
        _pack_ = 4
    class _CreatePipe_e__Struct(Structure):
        SecurityContext: POINTER(win32more.Windows.Wdk.Foundation.IO_SECURITY_CONTEXT)
        Options: UInt32
        Reserved: UInt16
        ShareAccess: UInt16
        Parameters: VoidPtr
    class _CreateMailslot_e__Struct(Structure):
        SecurityContext: POINTER(win32more.Windows.Wdk.Foundation.IO_SECURITY_CONTEXT)
        Options: UInt32
        Reserved: UInt16
        ShareAccess: UInt16
        Parameters: VoidPtr
    class _Read_e__Struct(Structure):
        Length: UInt32
        Key: UInt32
        ByteOffset: Int64
        ReadBuffer: VoidPtr
        MdlAddress: POINTER(win32more.Windows.Wdk.Foundation.MDL)
        _pack_ = 4
    class _Write_e__Struct(Structure):
        Length: UInt32
        Key: UInt32
        ByteOffset: Int64
        WriteBuffer: VoidPtr
        MdlAddress: POINTER(win32more.Windows.Wdk.Foundation.MDL)
        _pack_ = 4
    class _QueryFileInformation_e__Struct(Structure):
        Length: UInt32
        FileInformationClass: win32more.Windows.Wdk.Storage.FileSystem.FILE_INFORMATION_CLASS
        InfoBuffer: VoidPtr
    class _SetFileInformation_e__Struct(Structure):
        Length: UInt32
        FileInformationClass: win32more.Windows.Wdk.Storage.FileSystem.FILE_INFORMATION_CLASS
        ParentOfTarget: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT)
        Anonymous: _Anonymous_e__Union
        InfoBuffer: VoidPtr
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Union(Union):
            Anonymous: _Anonymous_e__Struct
            ClusterCount: UInt32
            DeleteHandle: win32more.Windows.Win32.Foundation.HANDLE
            _anonymous_ = ('Anonymous',)
            class _Anonymous_e__Struct(Structure):
                ReplaceIfExists: win32more.Windows.Win32.Foundation.BOOLEAN
                AdvanceOnly: win32more.Windows.Win32.Foundation.BOOLEAN
    class _QueryEa_e__Struct(Structure):
        Length: UInt32
        EaList: VoidPtr
        EaListLength: UInt32
        EaIndex: UInt32
        EaBuffer: VoidPtr
        MdlAddress: POINTER(win32more.Windows.Wdk.Foundation.MDL)
    class _SetEa_e__Struct(Structure):
        Length: UInt32
        EaBuffer: VoidPtr
        MdlAddress: POINTER(win32more.Windows.Wdk.Foundation.MDL)
    class _QueryVolumeInformation_e__Struct(Structure):
        Length: UInt32
        FsInformationClass: win32more.Windows.Wdk.Storage.FileSystem.FS_INFORMATION_CLASS
        VolumeBuffer: VoidPtr
    class _SetVolumeInformation_e__Struct(Structure):
        Length: UInt32
        FsInformationClass: win32more.Windows.Wdk.Storage.FileSystem.FS_INFORMATION_CLASS
        VolumeBuffer: VoidPtr
    class _DirectoryControl_e__Union(Union):
        QueryDirectory: _QueryDirectory_e__Struct
        NotifyDirectory: _NotifyDirectory_e__Struct
        NotifyDirectoryEx: _NotifyDirectoryEx_e__Struct
        class _QueryDirectory_e__Struct(Structure):
            Length: UInt32
            FileName: POINTER(win32more.Windows.Win32.Foundation.UNICODE_STRING)
            FileInformationClass: win32more.Windows.Wdk.Storage.FileSystem.FILE_INFORMATION_CLASS
            FileIndex: UInt32
            DirectoryBuffer: VoidPtr
            MdlAddress: POINTER(win32more.Windows.Wdk.Foundation.MDL)
        class _NotifyDirectory_e__Struct(Structure):
            Length: UInt32
            CompletionFilter: UInt32
            Spare1: UInt32
            Spare2: UInt32
            DirectoryBuffer: VoidPtr
            MdlAddress: POINTER(win32more.Windows.Wdk.Foundation.MDL)
        class _NotifyDirectoryEx_e__Struct(Structure):
            Length: UInt32
            CompletionFilter: UInt32
            DirectoryNotifyInformationClass: win32more.Windows.Wdk.System.SystemServices.DIRECTORY_NOTIFY_INFORMATION_CLASS
            Spare2: UInt32
            DirectoryBuffer: VoidPtr
            MdlAddress: POINTER(win32more.Windows.Wdk.Foundation.MDL)
    class _FileSystemControl_e__Union(Union):
        VerifyVolume: _VerifyVolume_e__Struct
        Common: _Common_e__Struct
        Neither: _Neither_e__Struct
        Buffered: _Buffered_e__Struct
        Direct: _Direct_e__Struct
        class _VerifyVolume_e__Struct(Structure):
            Vpb: POINTER(win32more.Windows.Wdk.Foundation.VPB)
            DeviceObject: POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT)
        class _Common_e__Struct(Structure):
            OutputBufferLength: UInt32
            InputBufferLength: UInt32
            FsControlCode: UInt32
        class _Neither_e__Struct(Structure):
            OutputBufferLength: UInt32
            InputBufferLength: UInt32
            FsControlCode: UInt32
            InputBuffer: VoidPtr
            OutputBuffer: VoidPtr
            OutputMdlAddress: POINTER(win32more.Windows.Wdk.Foundation.MDL)
        class _Buffered_e__Struct(Structure):
            OutputBufferLength: UInt32
            InputBufferLength: UInt32
            FsControlCode: UInt32
            SystemBuffer: VoidPtr
        class _Direct_e__Struct(Structure):
            OutputBufferLength: UInt32
            InputBufferLength: UInt32
            FsControlCode: UInt32
            InputSystemBuffer: VoidPtr
            OutputBuffer: VoidPtr
            OutputMdlAddress: POINTER(win32more.Windows.Wdk.Foundation.MDL)
    class _DeviceIoControl_e__Union(Union):
        Common: _Common_e__Struct
        Neither: _Neither_e__Struct
        Buffered: _Buffered_e__Struct
        Direct: _Direct_e__Struct
        FastIo: _FastIo_e__Struct
        class _Common_e__Struct(Structure):
            OutputBufferLength: UInt32
            InputBufferLength: UInt32
            IoControlCode: UInt32
        class _Neither_e__Struct(Structure):
            OutputBufferLength: UInt32
            InputBufferLength: UInt32
            IoControlCode: UInt32
            InputBuffer: VoidPtr
            OutputBuffer: VoidPtr
            OutputMdlAddress: POINTER(win32more.Windows.Wdk.Foundation.MDL)
        class _Buffered_e__Struct(Structure):
            OutputBufferLength: UInt32
            InputBufferLength: UInt32
            IoControlCode: UInt32
            SystemBuffer: VoidPtr
        class _Direct_e__Struct(Structure):
            OutputBufferLength: UInt32
            InputBufferLength: UInt32
            IoControlCode: UInt32
            InputSystemBuffer: VoidPtr
            OutputBuffer: VoidPtr
            OutputMdlAddress: POINTER(win32more.Windows.Wdk.Foundation.MDL)
        class _FastIo_e__Struct(Structure):
            OutputBufferLength: UInt32
            InputBufferLength: UInt32
            IoControlCode: UInt32
            InputBuffer: VoidPtr
            OutputBuffer: VoidPtr
    class _LockControl_e__Struct(Structure):
        Length: POINTER(Int64)
        Key: UInt32
        ByteOffset: Int64
        ProcessId: win32more.Windows.Wdk.Foundation.PEPROCESS
        FailImmediately: win32more.Windows.Win32.Foundation.BOOLEAN
        ExclusiveLock: win32more.Windows.Win32.Foundation.BOOLEAN
        _pack_ = 4
    class _QuerySecurity_e__Struct(Structure):
        SecurityInformation: UInt32
        Length: UInt32
        SecurityBuffer: VoidPtr
        MdlAddress: POINTER(win32more.Windows.Wdk.Foundation.MDL)
    class _SetSecurity_e__Struct(Structure):
        SecurityInformation: UInt32
        SecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR
    class _WMI_e__Struct(Structure):
        ProviderId: UIntPtr
        DataPath: VoidPtr
        BufferSize: UInt32
        Buffer: VoidPtr
    class _QueryQuota_e__Struct(Structure):
        Length: UInt32
        StartSid: win32more.Windows.Win32.Security.PSID
        SidList: POINTER(win32more.Windows.Wdk.Storage.FileSystem.FILE_GET_QUOTA_INFORMATION)
        SidListLength: UInt32
        QuotaBuffer: VoidPtr
        MdlAddress: POINTER(win32more.Windows.Wdk.Foundation.MDL)
    class _SetQuota_e__Struct(Structure):
        Length: UInt32
        QuotaBuffer: VoidPtr
        MdlAddress: POINTER(win32more.Windows.Wdk.Foundation.MDL)
    class _Pnp_e__Union(Union):
        StartDevice: _StartDevice_e__Struct
        QueryDeviceRelations: _QueryDeviceRelations_e__Struct
        QueryInterface: _QueryInterface_e__Struct
        DeviceCapabilities: _DeviceCapabilities_e__Struct
        FilterResourceRequirements: _FilterResourceRequirements_e__Struct
        ReadWriteConfig: _ReadWriteConfig_e__Struct
        SetLock: _SetLock_e__Struct
        QueryId: _QueryId_e__Struct
        QueryDeviceText: _QueryDeviceText_e__Struct
        UsageNotification: _UsageNotification_e__Struct
        class _StartDevice_e__Struct(Structure):
            AllocatedResources: POINTER(win32more.Windows.Wdk.System.SystemServices.CM_RESOURCE_LIST)
            AllocatedResourcesTranslated: POINTER(win32more.Windows.Wdk.System.SystemServices.CM_RESOURCE_LIST)
        class _QueryDeviceRelations_e__Struct(Structure):
            Type: win32more.Windows.Wdk.System.SystemServices.DEVICE_RELATION_TYPE
        class _QueryInterface_e__Struct(Structure):
            InterfaceType: POINTER(Guid)
            Size: UInt16
            Version: UInt16
            Interface: POINTER(win32more.Windows.Wdk.System.SystemServices.INTERFACE)
            InterfaceSpecificData: VoidPtr
        class _DeviceCapabilities_e__Struct(Structure):
            Capabilities: POINTER(win32more.Windows.Wdk.System.SystemServices.DEVICE_CAPABILITIES)
        class _FilterResourceRequirements_e__Struct(Structure):
            IoResourceRequirementList: POINTER(win32more.Windows.Wdk.System.SystemServices.IO_RESOURCE_REQUIREMENTS_LIST)
        class _ReadWriteConfig_e__Struct(Structure):
            WhichSpace: UInt32
            Buffer: VoidPtr
            Offset: UInt32
            Length: UInt32
        class _SetLock_e__Struct(Structure):
            Lock: win32more.Windows.Win32.Foundation.BOOLEAN
        class _QueryId_e__Struct(Structure):
            IdType: win32more.Windows.Wdk.System.SystemServices.BUS_QUERY_ID_TYPE
        class _QueryDeviceText_e__Struct(Structure):
            DeviceTextType: win32more.Windows.Wdk.System.SystemServices.DEVICE_TEXT_TYPE
            LocaleId: UInt32
        class _UsageNotification_e__Struct(Structure):
            InPath: win32more.Windows.Win32.Foundation.BOOLEAN
            Reserved: win32more.Windows.Win32.Foundation.BOOLEAN * 3
            Type: win32more.Windows.Wdk.System.SystemServices.DEVICE_USAGE_NOTIFICATION_TYPE
    class _AcquireForSectionSynchronization_e__Struct(Structure):
        SyncType: win32more.Windows.Wdk.Storage.FileSystem.FS_FILTER_SECTION_SYNC_TYPE
        PageProtection: UInt32
        OutputInformation: POINTER(win32more.Windows.Wdk.Storage.FileSystem.FS_FILTER_SECTION_SYNC_OUTPUT)
        Flags: UInt32
        AllocationAttributes: UInt32
    class _AcquireForModifiedPageWriter_e__Struct(Structure):
        EndingOffset: POINTER(Int64)
        ResourceToRelease: POINTER(POINTER(win32more.Windows.Wdk.Foundation.ERESOURCE))
    class _ReleaseForModifiedPageWriter_e__Struct(Structure):
        ResourceToRelease: POINTER(win32more.Windows.Wdk.Foundation.ERESOURCE)
    class _QueryOpen_e__Struct(Structure):
        Irp: POINTER(win32more.Windows.Wdk.Foundation.IRP)
        FileInformation: VoidPtr
        Length: POINTER(UInt32)
        FileInformationClass: win32more.Windows.Wdk.Storage.FileSystem.FILE_INFORMATION_CLASS
    class _FastIoCheckIfPossible_e__Struct(Structure):
        FileOffset: Int64
        Length: UInt32
        LockKey: UInt32
        CheckForReadOperation: win32more.Windows.Win32.Foundation.BOOLEAN
        _pack_ = 4
    class _NetworkQueryOpen_e__Struct(Structure):
        Irp: POINTER(win32more.Windows.Wdk.Foundation.IRP)
        NetworkInformation: POINTER(win32more.Windows.Wdk.Storage.FileSystem.FILE_NETWORK_OPEN_INFORMATION)
    class _MdlRead_e__Struct(Structure):
        FileOffset: Int64
        Length: UInt32
        Key: UInt32
        MdlChain: POINTER(POINTER(win32more.Windows.Wdk.Foundation.MDL))
        _pack_ = 4
    class _MdlReadComplete_e__Struct(Structure):
        MdlChain: POINTER(win32more.Windows.Wdk.Foundation.MDL)
    class _PrepareMdlWrite_e__Struct(Structure):
        FileOffset: Int64
        Length: UInt32
        Key: UInt32
        MdlChain: POINTER(POINTER(win32more.Windows.Wdk.Foundation.MDL))
        _pack_ = 4
    class _MdlWriteComplete_e__Struct(Structure):
        FileOffset: Int64
        MdlChain: POINTER(win32more.Windows.Wdk.Foundation.MDL)
        _pack_ = 4
    class _MountVolume_e__Struct(Structure):
        DeviceType: UInt32
    class _Others_e__Struct(Structure):
        Argument1: VoidPtr
        Argument2: VoidPtr
        Argument3: VoidPtr
        Argument4: VoidPtr
        Argument5: VoidPtr
        Argument6: Int64
        _pack_ = 4
FLT_POSTOP_CALLBACK_STATUS = Int32
FLT_POSTOP_FINISHED_PROCESSING: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_POSTOP_CALLBACK_STATUS = 0
FLT_POSTOP_MORE_PROCESSING_REQUIRED: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_POSTOP_CALLBACK_STATUS = 1
FLT_POSTOP_DISALLOW_FSFILTER_IO: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_POSTOP_CALLBACK_STATUS = 2
FLT_PREOP_CALLBACK_STATUS = Int32
FLT_PREOP_SUCCESS_WITH_CALLBACK: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_PREOP_CALLBACK_STATUS = 0
FLT_PREOP_SUCCESS_NO_CALLBACK: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_PREOP_CALLBACK_STATUS = 1
FLT_PREOP_PENDING: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_PREOP_CALLBACK_STATUS = 2
FLT_PREOP_DISALLOW_FASTIO: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_PREOP_CALLBACK_STATUS = 3
FLT_PREOP_COMPLETE: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_PREOP_CALLBACK_STATUS = 4
FLT_PREOP_SYNCHRONIZE: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_PREOP_CALLBACK_STATUS = 5
FLT_PREOP_DISALLOW_FSFILTER_IO: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_PREOP_CALLBACK_STATUS = 6
class FLT_REGISTRATION(Structure):
    Size: UInt16
    Version: UInt16
    Flags: UInt32
    ContextRegistration: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CONTEXT_REGISTRATION)
    OperationRegistration: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_OPERATION_REGISTRATION)
    FilterUnloadCallback: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER_UNLOAD_CALLBACK
    InstanceSetupCallback: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE_SETUP_CALLBACK
    InstanceQueryTeardownCallback: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE_QUERY_TEARDOWN_CALLBACK
    InstanceTeardownStartCallback: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE_TEARDOWN_CALLBACK
    InstanceTeardownCompleteCallback: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE_TEARDOWN_CALLBACK
    GenerateFileNameCallback: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_GENERATE_FILE_NAME
    NormalizeNameComponentCallback: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_NORMALIZE_NAME_COMPONENT
    NormalizeContextCleanupCallback: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_NORMALIZE_CONTEXT_CLEANUP
    TransactionNotificationCallback: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_TRANSACTION_NOTIFICATION_CALLBACK
    NormalizeNameComponentExCallback: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_NORMALIZE_NAME_COMPONENT_EX
    SectionNotificationCallback: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_SECTION_CONFLICT_NOTIFICATION_CALLBACK
class FLT_RELATED_CONTEXTS(Structure):
    VolumeContext: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT
    InstanceContext: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT
    FileContext: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT
    StreamContext: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT
    StreamHandleContext: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT
    TransactionContext: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT
class FLT_RELATED_CONTEXTS_EX(Structure):
    VolumeContext: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT
    InstanceContext: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT
    FileContext: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT
    StreamContext: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT
    StreamHandleContext: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT
    TransactionContext: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT
    SectionContext: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT
class FLT_RELATED_OBJECTS(Structure):
    Size: UInt16
    TransactionContext: UInt16
    Filter: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_FILTER
    Volume: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_VOLUME
    Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE
    FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT)
    Transaction: POINTER(win32more.Windows.Wdk.Foundation.KTRANSACTION)
FLT_SET_CONTEXT_OPERATION = Int32
FLT_SET_CONTEXT_REPLACE_IF_EXISTS: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_SET_CONTEXT_OPERATION = 0
FLT_SET_CONTEXT_KEEP_IF_EXISTS: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_SET_CONTEXT_OPERATION = 1
class FLT_TAG_DATA_BUFFER(Structure):
    FileTag: UInt32
    TagDataLength: UInt16
    UnparsedNameLength: UInt16
    Anonymous: _Anonymous_e__Union
    _anonymous_ = ('Anonymous',)
    class _Anonymous_e__Union(Union):
        SymbolicLinkReparseBuffer: _SymbolicLinkReparseBuffer_e__Struct
        MountPointReparseBuffer: _MountPointReparseBuffer_e__Struct
        GenericReparseBuffer: _GenericReparseBuffer_e__Struct
        GenericGUIDReparseBuffer: _GenericGUIDReparseBuffer_e__Struct
        class _SymbolicLinkReparseBuffer_e__Struct(Structure):
            SubstituteNameOffset: UInt16
            SubstituteNameLength: UInt16
            PrintNameOffset: UInt16
            PrintNameLength: UInt16
            Flags: UInt32
            PathBuffer: FlexibleArray[Char]
        class _MountPointReparseBuffer_e__Struct(Structure):
            SubstituteNameOffset: UInt16
            SubstituteNameLength: UInt16
            PrintNameOffset: UInt16
            PrintNameLength: UInt16
            PathBuffer: FlexibleArray[Char]
        class _GenericReparseBuffer_e__Struct(Structure):
            DataBuffer: FlexibleArray[Byte]
        class _GenericGUIDReparseBuffer_e__Struct(Structure):
            TagGuid: Guid
            DataBuffer: FlexibleArray[Byte]
class FLT_VOLUME_PROPERTIES(Structure):
    DeviceType: UInt32
    DeviceCharacteristics: UInt32
    DeviceObjectFlags: UInt32
    AlignmentRequirement: UInt32
    SectorSize: UInt16
    Flags: UInt16
    FileSystemDriverName: win32more.Windows.Win32.Foundation.UNICODE_STRING
    FileSystemDeviceName: win32more.Windows.Win32.Foundation.UNICODE_STRING
    RealDeviceName: win32more.Windows.Win32.Foundation.UNICODE_STRING
@winfunctype_pointer
def PFLTOPLOCK_PREPOST_CALLBACKDATA_ROUTINE(CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA), Context: VoidPtr) -> Void: ...
@winfunctype_pointer
def PFLTOPLOCK_WAIT_COMPLETE_ROUTINE(CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA), Context: VoidPtr) -> Void: ...
@winfunctype_pointer
def PFLT_CALLBACK_DATA_QUEUE_ACQUIRE(Cbdq: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA_QUEUE), Irql: POINTER(Byte)) -> Void: ...
@winfunctype_pointer
def PFLT_CALLBACK_DATA_QUEUE_COMPLETE_CANCELED_IO(Cbdq: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA_QUEUE), Cbd: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA)) -> Void: ...
@winfunctype_pointer
def PFLT_CALLBACK_DATA_QUEUE_INSERT_IO(Cbdq: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA_QUEUE), Cbd: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA), InsertContext: VoidPtr) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype_pointer
def PFLT_CALLBACK_DATA_QUEUE_PEEK_NEXT_IO(Cbdq: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA_QUEUE), Cbd: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA), PeekContext: VoidPtr) -> POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA): ...
@winfunctype_pointer
def PFLT_CALLBACK_DATA_QUEUE_RELEASE(Cbdq: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA_QUEUE), Irql: Byte) -> Void: ...
@winfunctype_pointer
def PFLT_CALLBACK_DATA_QUEUE_REMOVE_IO(Cbdq: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA_QUEUE), Cbd: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA)) -> Void: ...
@winfunctype_pointer
def PFLT_COMPLETED_ASYNC_IO_CALLBACK(CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA), Context: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT) -> Void: ...
@winfunctype_pointer
def PFLT_COMPLETE_CANCELED_CALLBACK(CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA)) -> Void: ...
@winfunctype_pointer
def PFLT_COMPLETE_LOCK_CALLBACK_DATA_ROUTINE(Context: VoidPtr, CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype_pointer
def PFLT_CONNECT_NOTIFY(ClientPort: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_PORT, ServerPortCookie: VoidPtr, ConnectionContext: VoidPtr, SizeOfContext: UInt32, ConnectionPortCookie: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
PFLT_CONTEXT = VoidPtr
@winfunctype_pointer
def PFLT_CONTEXT_ALLOCATE_CALLBACK(PoolType: win32more.Windows.Wdk.Foundation.POOL_TYPE, Size: UIntPtr, ContextType: UInt16) -> VoidPtr: ...
@winfunctype_pointer
def PFLT_CONTEXT_CLEANUP_CALLBACK(Context: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT, ContextType: UInt16) -> Void: ...
@winfunctype_pointer
def PFLT_CONTEXT_FREE_CALLBACK(Pool: VoidPtr, ContextType: UInt16) -> Void: ...
PFLT_DEFERRED_IO_WORKITEM = IntPtr
@winfunctype_pointer
def PFLT_DEFERRED_IO_WORKITEM_ROUTINE(FltWorkItem: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_DEFERRED_IO_WORKITEM, CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA), Context: VoidPtr) -> Void: ...
@winfunctype_pointer
def PFLT_DISCONNECT_NOTIFY(ConnectionCookie: VoidPtr) -> Void: ...
PFLT_FILTER = IntPtr
@winfunctype_pointer
def PFLT_FILTER_UNLOAD_CALLBACK(Flags: UInt32) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype_pointer
def PFLT_GENERATE_FILE_NAME(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), CallbackData: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA), NameOptions: UInt32, CacheFileNameInformation: POINTER(win32more.Windows.Win32.Foundation.BOOLEAN), FileName: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_NAME_CONTROL)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
PFLT_GENERIC_WORKITEM = IntPtr
@winfunctype_pointer
def PFLT_GENERIC_WORKITEM_ROUTINE(FltWorkItem: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_GENERIC_WORKITEM, FltObject: VoidPtr, Context: VoidPtr) -> Void: ...
@winfunctype_pointer
def PFLT_GET_OPERATION_STATUS_CALLBACK(FltObjects: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_RELATED_OBJECTS), IopbSnapshot: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_IO_PARAMETER_BLOCK), OperationStatus: win32more.Windows.Win32.Foundation.NTSTATUS, RequesterContext: VoidPtr) -> Void: ...
PFLT_INSTANCE = IntPtr
@winfunctype_pointer
def PFLT_INSTANCE_QUERY_TEARDOWN_CALLBACK(FltObjects: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_RELATED_OBJECTS), Flags: UInt32) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype_pointer
def PFLT_INSTANCE_SETUP_CALLBACK(FltObjects: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_RELATED_OBJECTS), Flags: UInt32, VolumeDeviceType: UInt32, VolumeFilesystemType: win32more.Windows.Win32.Storage.InstallableFileSystems.FLT_FILESYSTEM_TYPE) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype_pointer
def PFLT_INSTANCE_TEARDOWN_CALLBACK(FltObjects: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_RELATED_OBJECTS), Reason: UInt32) -> Void: ...
@winfunctype_pointer
def PFLT_MESSAGE_NOTIFY(PortCookie: VoidPtr, InputBuffer: VoidPtr, InputBufferLength: UInt32, OutputBuffer: VoidPtr, OutputBufferLength: UInt32, ReturnOutputBufferLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype_pointer
def PFLT_NORMALIZE_CONTEXT_CLEANUP(NormalizationContext: POINTER(VoidPtr)) -> Void: ...
@winfunctype_pointer
def PFLT_NORMALIZE_NAME_COMPONENT(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, ParentDirectory: POINTER(win32more.Windows.Win32.Foundation.UNICODE_STRING), VolumeNameLength: UInt16, Component: POINTER(win32more.Windows.Win32.Foundation.UNICODE_STRING), ExpandComponentName: POINTER(win32more.Windows.Wdk.Storage.FileSystem.FILE_NAMES_INFORMATION), ExpandComponentNameLength: UInt32, Flags: UInt32, NormalizationContext: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype_pointer
def PFLT_NORMALIZE_NAME_COMPONENT_EX(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), ParentDirectory: POINTER(win32more.Windows.Win32.Foundation.UNICODE_STRING), VolumeNameLength: UInt16, Component: POINTER(win32more.Windows.Win32.Foundation.UNICODE_STRING), ExpandComponentName: POINTER(win32more.Windows.Wdk.Storage.FileSystem.FILE_NAMES_INFORMATION), ExpandComponentNameLength: UInt32, Flags: UInt32, NormalizationContext: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
PFLT_PORT = IntPtr
@winfunctype_pointer
def PFLT_POST_OPERATION_CALLBACK(Data: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA), FltObjects: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_RELATED_OBJECTS), CompletionContext: VoidPtr, Flags: UInt32) -> win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_POSTOP_CALLBACK_STATUS: ...
@winfunctype_pointer
def PFLT_PRE_OPERATION_CALLBACK(Data: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA), FltObjects: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_RELATED_OBJECTS), CompletionContext: POINTER(VoidPtr)) -> win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_PREOP_CALLBACK_STATUS: ...
@winfunctype_pointer
def PFLT_SECTION_CONFLICT_NOTIFICATION_CALLBACK(Instance: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_INSTANCE, SectionContext: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT, Data: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_CALLBACK_DATA)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype_pointer
def PFLT_TRANSACTION_NOTIFICATION_CALLBACK(FltObjects: POINTER(win32more.Windows.Wdk.Storage.FileSystem.Minifilters.FLT_RELATED_OBJECTS), TransactionContext: win32more.Windows.Wdk.Storage.FileSystem.Minifilters.PFLT_CONTEXT, NotificationMask: UInt32) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
PFLT_VOLUME = IntPtr


make_ready(__name__)
