from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Storage.CloudFilters
import win32more.Windows.Win32.Storage.FileSystem
import win32more.Windows.Win32.System.CorrelationVector
import win32more.Windows.Win32.System.IO
CF_REQUEST_KEY_DEFAULT: UInt32 = 0
CF_PLACEHOLDER_MAX_FILE_IDENTITY_LENGTH: UInt32 = 4096
CF_MAX_PRIORITY_HINT: UInt32 = 15
CF_MAX_PROVIDER_NAME_LENGTH: UInt32 = 255
CF_MAX_PROVIDER_VERSION_LENGTH: UInt32 = 255
@winfunctype('cldapi.dll')
def CfGetPlatformInfo(PlatformVersion: POINTER(win32more.Windows.Win32.Storage.CloudFilters.CF_PLATFORM_INFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfRegisterSyncRoot(SyncRootPath: win32more.Windows.Win32.Foundation.PWSTR, Registration: POINTER(win32more.Windows.Win32.Storage.CloudFilters.CF_SYNC_REGISTRATION), Policies: POINTER(win32more.Windows.Win32.Storage.CloudFilters.CF_SYNC_POLICIES), RegisterFlags: win32more.Windows.Win32.Storage.CloudFilters.CF_REGISTER_FLAGS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfUnregisterSyncRoot(SyncRootPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfConnectSyncRoot(SyncRootPath: win32more.Windows.Win32.Foundation.PWSTR, CallbackTable: POINTER(win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_REGISTRATION), CallbackContext: VoidPtr, ConnectFlags: win32more.Windows.Win32.Storage.CloudFilters.CF_CONNECT_FLAGS, ConnectionKey: POINTER(win32more.Windows.Win32.Storage.CloudFilters.CF_CONNECTION_KEY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfDisconnectSyncRoot(ConnectionKey: win32more.Windows.Win32.Storage.CloudFilters.CF_CONNECTION_KEY) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfGetTransferKey(FileHandle: win32more.Windows.Win32.Foundation.HANDLE, TransferKey: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfReleaseTransferKey(FileHandle: win32more.Windows.Win32.Foundation.HANDLE, TransferKey: POINTER(Int64)) -> Void: ...
@winfunctype('cldapi.dll')
def CfExecute(OpInfo: POINTER(win32more.Windows.Win32.Storage.CloudFilters.CF_OPERATION_INFO), OpParams: POINTER(win32more.Windows.Win32.Storage.CloudFilters.CF_OPERATION_PARAMETERS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfUpdateSyncProviderStatus(ConnectionKey: win32more.Windows.Win32.Storage.CloudFilters.CF_CONNECTION_KEY, ProviderStatus: win32more.Windows.Win32.Storage.CloudFilters.CF_SYNC_PROVIDER_STATUS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfQuerySyncProviderStatus(ConnectionKey: win32more.Windows.Win32.Storage.CloudFilters.CF_CONNECTION_KEY, ProviderStatus: POINTER(win32more.Windows.Win32.Storage.CloudFilters.CF_SYNC_PROVIDER_STATUS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfReportSyncStatus(SyncRootPath: win32more.Windows.Win32.Foundation.PWSTR, SyncStatus: POINTER(win32more.Windows.Win32.Storage.CloudFilters.CF_SYNC_STATUS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfCreatePlaceholders(BaseDirectoryPath: win32more.Windows.Win32.Foundation.PWSTR, PlaceholderArray: POINTER(win32more.Windows.Win32.Storage.CloudFilters.CF_PLACEHOLDER_CREATE_INFO), PlaceholderCount: UInt32, CreateFlags: win32more.Windows.Win32.Storage.CloudFilters.CF_CREATE_FLAGS, EntriesProcessed: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfOpenFileWithOplock(FilePath: win32more.Windows.Win32.Foundation.PWSTR, Flags: win32more.Windows.Win32.Storage.CloudFilters.CF_OPEN_FILE_FLAGS, ProtectedHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfReferenceProtectedHandle(ProtectedHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('cldapi.dll')
def CfGetWin32HandleFromProtectedHandle(ProtectedHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('cldapi.dll')
def CfReleaseProtectedHandle(ProtectedHandle: win32more.Windows.Win32.Foundation.HANDLE) -> Void: ...
@winfunctype('cldapi.dll')
def CfCloseHandle(FileHandle: win32more.Windows.Win32.Foundation.HANDLE) -> Void: ...
@winfunctype('cldapi.dll')
def CfConvertToPlaceholder(FileHandle: win32more.Windows.Win32.Foundation.HANDLE, FileIdentity: VoidPtr, FileIdentityLength: UInt32, ConvertFlags: win32more.Windows.Win32.Storage.CloudFilters.CF_CONVERT_FLAGS, ConvertUsn: POINTER(Int64), Overlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfUpdatePlaceholder(FileHandle: win32more.Windows.Win32.Foundation.HANDLE, FsMetadata: POINTER(win32more.Windows.Win32.Storage.CloudFilters.CF_FS_METADATA), FileIdentity: VoidPtr, FileIdentityLength: UInt32, DehydrateRangeArray: POINTER(win32more.Windows.Win32.Storage.CloudFilters.CF_FILE_RANGE), DehydrateRangeCount: UInt32, UpdateFlags: win32more.Windows.Win32.Storage.CloudFilters.CF_UPDATE_FLAGS, UpdateUsn: POINTER(Int64), Overlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfRevertPlaceholder(FileHandle: win32more.Windows.Win32.Foundation.HANDLE, RevertFlags: win32more.Windows.Win32.Storage.CloudFilters.CF_REVERT_FLAGS, Overlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfHydratePlaceholder(FileHandle: win32more.Windows.Win32.Foundation.HANDLE, StartingOffset: Int64, Length: Int64, HydrateFlags: win32more.Windows.Win32.Storage.CloudFilters.CF_HYDRATE_FLAGS, Overlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfDehydratePlaceholder(FileHandle: win32more.Windows.Win32.Foundation.HANDLE, StartingOffset: Int64, Length: Int64, DehydrateFlags: win32more.Windows.Win32.Storage.CloudFilters.CF_DEHYDRATE_FLAGS, Overlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfSetPinState(FileHandle: win32more.Windows.Win32.Foundation.HANDLE, PinState: win32more.Windows.Win32.Storage.CloudFilters.CF_PIN_STATE, PinFlags: win32more.Windows.Win32.Storage.CloudFilters.CF_SET_PIN_FLAGS, Overlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfSetInSyncState(FileHandle: win32more.Windows.Win32.Foundation.HANDLE, InSyncState: win32more.Windows.Win32.Storage.CloudFilters.CF_IN_SYNC_STATE, InSyncFlags: win32more.Windows.Win32.Storage.CloudFilters.CF_SET_IN_SYNC_FLAGS, InSyncUsn: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfSetCorrelationVector(FileHandle: win32more.Windows.Win32.Foundation.HANDLE, CorrelationVector: POINTER(win32more.Windows.Win32.System.CorrelationVector.CORRELATION_VECTOR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfGetCorrelationVector(FileHandle: win32more.Windows.Win32.Foundation.HANDLE, CorrelationVector: POINTER(win32more.Windows.Win32.System.CorrelationVector.CORRELATION_VECTOR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfGetPlaceholderStateFromAttributeTag(FileAttributes: UInt32, ReparseTag: UInt32) -> win32more.Windows.Win32.Storage.CloudFilters.CF_PLACEHOLDER_STATE: ...
@winfunctype('cldapi.dll')
def CfGetPlaceholderStateFromFileInfo(InfoBuffer: VoidPtr, InfoClass: win32more.Windows.Win32.Storage.FileSystem.FILE_INFO_BY_HANDLE_CLASS) -> win32more.Windows.Win32.Storage.CloudFilters.CF_PLACEHOLDER_STATE: ...
@winfunctype('cldapi.dll')
def CfGetPlaceholderStateFromFindData(FindData: POINTER(win32more.Windows.Win32.Storage.FileSystem.WIN32_FIND_DATAA)) -> win32more.Windows.Win32.Storage.CloudFilters.CF_PLACEHOLDER_STATE: ...
@winfunctype('cldapi.dll')
def CfGetPlaceholderInfo(FileHandle: win32more.Windows.Win32.Foundation.HANDLE, InfoClass: win32more.Windows.Win32.Storage.CloudFilters.CF_PLACEHOLDER_INFO_CLASS, InfoBuffer: VoidPtr, InfoBufferLength: UInt32, ReturnedLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfGetSyncRootInfoByPath(FilePath: win32more.Windows.Win32.Foundation.PWSTR, InfoClass: win32more.Windows.Win32.Storage.CloudFilters.CF_SYNC_ROOT_INFO_CLASS, InfoBuffer: VoidPtr, InfoBufferLength: UInt32, ReturnedLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfGetSyncRootInfoByHandle(FileHandle: win32more.Windows.Win32.Foundation.HANDLE, InfoClass: win32more.Windows.Win32.Storage.CloudFilters.CF_SYNC_ROOT_INFO_CLASS, InfoBuffer: VoidPtr, InfoBufferLength: UInt32, ReturnedLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfGetPlaceholderRangeInfo(FileHandle: win32more.Windows.Win32.Foundation.HANDLE, InfoClass: win32more.Windows.Win32.Storage.CloudFilters.CF_PLACEHOLDER_RANGE_INFO_CLASS, StartingOffset: Int64, Length: Int64, InfoBuffer: VoidPtr, InfoBufferLength: UInt32, ReturnedLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfGetPlaceholderRangeInfoForHydration(ConnectionKey: win32more.Windows.Win32.Storage.CloudFilters.CF_CONNECTION_KEY, TransferKey: Int64, FileId: Int64, InfoClass: win32more.Windows.Win32.Storage.CloudFilters.CF_PLACEHOLDER_RANGE_INFO_CLASS, StartingOffset: Int64, RangeLength: Int64, InfoBuffer: VoidPtr, InfoBufferSize: UInt32, InfoBufferWritten: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfReportProviderProgress(ConnectionKey: win32more.Windows.Win32.Storage.CloudFilters.CF_CONNECTION_KEY, TransferKey: Int64, ProviderProgressTotal: Int64, ProviderProgressCompleted: Int64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfReportProviderProgress2(ConnectionKey: win32more.Windows.Win32.Storage.CloudFilters.CF_CONNECTION_KEY, TransferKey: Int64, RequestKey: Int64, ProviderProgressTotal: Int64, ProviderProgressCompleted: Int64, TargetSessionId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def CF_CALLBACK(CallbackInfo: POINTER(win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_INFO), CallbackParameters: POINTER(win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_PARAMETERS)) -> Void: ...
CF_CALLBACK_CANCEL_FLAGS = Int32
CF_CALLBACK_CANCEL_FLAG_NONE: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_CANCEL_FLAGS = 0
CF_CALLBACK_CANCEL_FLAG_IO_TIMEOUT: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_CANCEL_FLAGS = 1
CF_CALLBACK_CANCEL_FLAG_IO_ABORTED: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_CANCEL_FLAGS = 2
CF_CALLBACK_CLOSE_COMPLETION_FLAGS = Int32
CF_CALLBACK_CLOSE_COMPLETION_FLAG_NONE: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_CLOSE_COMPLETION_FLAGS = 0
CF_CALLBACK_CLOSE_COMPLETION_FLAG_DELETED: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_CLOSE_COMPLETION_FLAGS = 1
CF_CALLBACK_DEHYDRATE_COMPLETION_FLAGS = Int32
CF_CALLBACK_DEHYDRATE_COMPLETION_FLAG_NONE: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_DEHYDRATE_COMPLETION_FLAGS = 0
CF_CALLBACK_DEHYDRATE_COMPLETION_FLAG_BACKGROUND: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_DEHYDRATE_COMPLETION_FLAGS = 1
CF_CALLBACK_DEHYDRATE_COMPLETION_FLAG_DEHYDRATED: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_DEHYDRATE_COMPLETION_FLAGS = 2
CF_CALLBACK_DEHYDRATE_FLAGS = Int32
CF_CALLBACK_DEHYDRATE_FLAG_NONE: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_DEHYDRATE_FLAGS = 0
CF_CALLBACK_DEHYDRATE_FLAG_BACKGROUND: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_DEHYDRATE_FLAGS = 1
CF_CALLBACK_DEHYDRATION_REASON = Int32
CF_CALLBACK_DEHYDRATION_REASON_NONE: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_DEHYDRATION_REASON = 0
CF_CALLBACK_DEHYDRATION_REASON_USER_MANUAL: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_DEHYDRATION_REASON = 1
CF_CALLBACK_DEHYDRATION_REASON_SYSTEM_LOW_SPACE: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_DEHYDRATION_REASON = 2
CF_CALLBACK_DEHYDRATION_REASON_SYSTEM_INACTIVITY: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_DEHYDRATION_REASON = 3
CF_CALLBACK_DEHYDRATION_REASON_SYSTEM_OS_UPGRADE: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_DEHYDRATION_REASON = 4
CF_CALLBACK_DELETE_COMPLETION_FLAGS = Int32
CF_CALLBACK_DELETE_COMPLETION_FLAG_NONE: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_DELETE_COMPLETION_FLAGS = 0
CF_CALLBACK_DELETE_FLAGS = Int32
CF_CALLBACK_DELETE_FLAG_NONE: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_DELETE_FLAGS = 0
CF_CALLBACK_DELETE_FLAG_IS_DIRECTORY: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_DELETE_FLAGS = 1
CF_CALLBACK_DELETE_FLAG_IS_UNDELETE: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_DELETE_FLAGS = 2
CF_CALLBACK_FETCH_DATA_FLAGS = Int32
CF_CALLBACK_FETCH_DATA_FLAG_NONE: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_FETCH_DATA_FLAGS = 0
CF_CALLBACK_FETCH_DATA_FLAG_RECOVERY: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_FETCH_DATA_FLAGS = 1
CF_CALLBACK_FETCH_DATA_FLAG_EXPLICIT_HYDRATION: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_FETCH_DATA_FLAGS = 2
CF_CALLBACK_FETCH_PLACEHOLDERS_FLAGS = Int32
CF_CALLBACK_FETCH_PLACEHOLDERS_FLAG_NONE: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_FETCH_PLACEHOLDERS_FLAGS = 0
class CF_CALLBACK_INFO(Structure):
    StructSize: UInt32
    ConnectionKey: win32more.Windows.Win32.Storage.CloudFilters.CF_CONNECTION_KEY
    CallbackContext: VoidPtr
    VolumeGuidName: win32more.Windows.Win32.Foundation.PWSTR
    VolumeDosName: win32more.Windows.Win32.Foundation.PWSTR
    VolumeSerialNumber: UInt32
    SyncRootFileId: Int64
    SyncRootIdentity: VoidPtr
    SyncRootIdentityLength: UInt32
    FileId: Int64
    FileSize: Int64
    FileIdentity: VoidPtr
    FileIdentityLength: UInt32
    NormalizedPath: win32more.Windows.Win32.Foundation.PWSTR
    TransferKey: Int64
    PriorityHint: Byte
    CorrelationVector: POINTER(win32more.Windows.Win32.System.CorrelationVector.CORRELATION_VECTOR)
    ProcessInfo: POINTER(win32more.Windows.Win32.Storage.CloudFilters.CF_PROCESS_INFO)
    RequestKey: Int64
CF_CALLBACK_OPEN_COMPLETION_FLAGS = Int32
CF_CALLBACK_OPEN_COMPLETION_FLAG_NONE: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_OPEN_COMPLETION_FLAGS = 0
CF_CALLBACK_OPEN_COMPLETION_FLAG_PLACEHOLDER_UNKNOWN: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_OPEN_COMPLETION_FLAGS = 1
CF_CALLBACK_OPEN_COMPLETION_FLAG_PLACEHOLDER_UNSUPPORTED: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_OPEN_COMPLETION_FLAGS = 2
class CF_CALLBACK_PARAMETERS(Structure):
    ParamSize: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Cancel: _Cancel_e__Struct
        FetchData: _FetchData_e__Struct
        ValidateData: _ValidateData_e__Struct
        FetchPlaceholders: _FetchPlaceholders_e__Struct
        OpenCompletion: _OpenCompletion_e__Struct
        CloseCompletion: _CloseCompletion_e__Struct
        Dehydrate: _Dehydrate_e__Struct
        DehydrateCompletion: _DehydrateCompletion_e__Struct
        Delete: _Delete_e__Struct
        DeleteCompletion: _DeleteCompletion_e__Struct
        Rename: _Rename_e__Struct
        RenameCompletion: _RenameCompletion_e__Struct
        class _Cancel_e__Struct(Structure):
            Flags: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_CANCEL_FLAGS
            Anonymous: _Anonymous_e__Union
            class _Anonymous_e__Union(Union):
                FetchData: _FetchData_e__Struct
                class _FetchData_e__Struct(Structure):
                    FileOffset: Int64
                    Length: Int64
        class _FetchData_e__Struct(Structure):
            Flags: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_FETCH_DATA_FLAGS
            RequiredFileOffset: Int64
            RequiredLength: Int64
            OptionalFileOffset: Int64
            OptionalLength: Int64
            LastDehydrationTime: Int64
            LastDehydrationReason: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_DEHYDRATION_REASON
        class _ValidateData_e__Struct(Structure):
            Flags: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_VALIDATE_DATA_FLAGS
            RequiredFileOffset: Int64
            RequiredLength: Int64
        class _FetchPlaceholders_e__Struct(Structure):
            Flags: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_FETCH_PLACEHOLDERS_FLAGS
            Pattern: win32more.Windows.Win32.Foundation.PWSTR
        class _OpenCompletion_e__Struct(Structure):
            Flags: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_OPEN_COMPLETION_FLAGS
        class _CloseCompletion_e__Struct(Structure):
            Flags: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_CLOSE_COMPLETION_FLAGS
        class _Dehydrate_e__Struct(Structure):
            Flags: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_DEHYDRATE_FLAGS
            Reason: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_DEHYDRATION_REASON
        class _DehydrateCompletion_e__Struct(Structure):
            Flags: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_DEHYDRATE_COMPLETION_FLAGS
            Reason: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_DEHYDRATION_REASON
        class _Delete_e__Struct(Structure):
            Flags: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_DELETE_FLAGS
        class _DeleteCompletion_e__Struct(Structure):
            Flags: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_DELETE_COMPLETION_FLAGS
        class _Rename_e__Struct(Structure):
            Flags: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_RENAME_FLAGS
            TargetPath: win32more.Windows.Win32.Foundation.PWSTR
        class _RenameCompletion_e__Struct(Structure):
            Flags: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_RENAME_COMPLETION_FLAGS
            SourcePath: win32more.Windows.Win32.Foundation.PWSTR
class CF_CALLBACK_REGISTRATION(Structure):
    Type: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_TYPE
    Callback: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK
CF_CALLBACK_RENAME_COMPLETION_FLAGS = Int32
CF_CALLBACK_RENAME_COMPLETION_FLAG_NONE: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_RENAME_COMPLETION_FLAGS = 0
CF_CALLBACK_RENAME_FLAGS = Int32
CF_CALLBACK_RENAME_FLAG_NONE: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_RENAME_FLAGS = 0
CF_CALLBACK_RENAME_FLAG_IS_DIRECTORY: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_RENAME_FLAGS = 1
CF_CALLBACK_RENAME_FLAG_SOURCE_IN_SCOPE: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_RENAME_FLAGS = 2
CF_CALLBACK_RENAME_FLAG_TARGET_IN_SCOPE: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_RENAME_FLAGS = 4
CF_CALLBACK_TYPE = Int32
CF_CALLBACK_TYPE_FETCH_DATA: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_TYPE = 0
CF_CALLBACK_TYPE_VALIDATE_DATA: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_TYPE = 1
CF_CALLBACK_TYPE_CANCEL_FETCH_DATA: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_TYPE = 2
CF_CALLBACK_TYPE_FETCH_PLACEHOLDERS: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_TYPE = 3
CF_CALLBACK_TYPE_CANCEL_FETCH_PLACEHOLDERS: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_TYPE = 4
CF_CALLBACK_TYPE_NOTIFY_FILE_OPEN_COMPLETION: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_TYPE = 5
CF_CALLBACK_TYPE_NOTIFY_FILE_CLOSE_COMPLETION: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_TYPE = 6
CF_CALLBACK_TYPE_NOTIFY_DEHYDRATE: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_TYPE = 7
CF_CALLBACK_TYPE_NOTIFY_DEHYDRATE_COMPLETION: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_TYPE = 8
CF_CALLBACK_TYPE_NOTIFY_DELETE: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_TYPE = 9
CF_CALLBACK_TYPE_NOTIFY_DELETE_COMPLETION: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_TYPE = 10
CF_CALLBACK_TYPE_NOTIFY_RENAME: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_TYPE = 11
CF_CALLBACK_TYPE_NOTIFY_RENAME_COMPLETION: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_TYPE = 12
CF_CALLBACK_TYPE_NONE: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_TYPE = -1
CF_CALLBACK_VALIDATE_DATA_FLAGS = Int32
CF_CALLBACK_VALIDATE_DATA_FLAG_NONE: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_VALIDATE_DATA_FLAGS = 0
CF_CALLBACK_VALIDATE_DATA_FLAG_EXPLICIT_HYDRATION: win32more.Windows.Win32.Storage.CloudFilters.CF_CALLBACK_VALIDATE_DATA_FLAGS = 2
CF_CONNECTION_KEY = Int64
CF_CONNECT_FLAGS = Int32
CF_CONNECT_FLAG_NONE: win32more.Windows.Win32.Storage.CloudFilters.CF_CONNECT_FLAGS = 0
CF_CONNECT_FLAG_REQUIRE_PROCESS_INFO: win32more.Windows.Win32.Storage.CloudFilters.CF_CONNECT_FLAGS = 2
CF_CONNECT_FLAG_REQUIRE_FULL_FILE_PATH: win32more.Windows.Win32.Storage.CloudFilters.CF_CONNECT_FLAGS = 4
CF_CONNECT_FLAG_BLOCK_SELF_IMPLICIT_HYDRATION: win32more.Windows.Win32.Storage.CloudFilters.CF_CONNECT_FLAGS = 8
CF_CONVERT_FLAGS = Int32
CF_CONVERT_FLAG_NONE: win32more.Windows.Win32.Storage.CloudFilters.CF_CONVERT_FLAGS = 0
CF_CONVERT_FLAG_MARK_IN_SYNC: win32more.Windows.Win32.Storage.CloudFilters.CF_CONVERT_FLAGS = 1
CF_CONVERT_FLAG_DEHYDRATE: win32more.Windows.Win32.Storage.CloudFilters.CF_CONVERT_FLAGS = 2
CF_CONVERT_FLAG_ENABLE_ON_DEMAND_POPULATION: win32more.Windows.Win32.Storage.CloudFilters.CF_CONVERT_FLAGS = 4
CF_CONVERT_FLAG_ALWAYS_FULL: win32more.Windows.Win32.Storage.CloudFilters.CF_CONVERT_FLAGS = 8
CF_CONVERT_FLAG_FORCE_CONVERT_TO_CLOUD_FILE: win32more.Windows.Win32.Storage.CloudFilters.CF_CONVERT_FLAGS = 16
CF_CREATE_FLAGS = Int32
CF_CREATE_FLAG_NONE: win32more.Windows.Win32.Storage.CloudFilters.CF_CREATE_FLAGS = 0
CF_CREATE_FLAG_STOP_ON_ERROR: win32more.Windows.Win32.Storage.CloudFilters.CF_CREATE_FLAGS = 1
CF_DEHYDRATE_FLAGS = Int32
CF_DEHYDRATE_FLAG_NONE: win32more.Windows.Win32.Storage.CloudFilters.CF_DEHYDRATE_FLAGS = 0
CF_DEHYDRATE_FLAG_BACKGROUND: win32more.Windows.Win32.Storage.CloudFilters.CF_DEHYDRATE_FLAGS = 1
class CF_FILE_RANGE(Structure):
    StartingOffset: Int64
    Length: Int64
class CF_FS_METADATA(Structure):
    BasicInfo: win32more.Windows.Win32.Storage.FileSystem.FILE_BASIC_INFO
    FileSize: Int64
CF_HARDLINK_POLICY = Int32
CF_HARDLINK_POLICY_NONE: win32more.Windows.Win32.Storage.CloudFilters.CF_HARDLINK_POLICY = 0
CF_HARDLINK_POLICY_ALLOWED: win32more.Windows.Win32.Storage.CloudFilters.CF_HARDLINK_POLICY = 1
CF_HYDRATE_FLAGS = Int32
CF_HYDRATE_FLAG_NONE: win32more.Windows.Win32.Storage.CloudFilters.CF_HYDRATE_FLAGS = 0
class CF_HYDRATION_POLICY(Structure):
    Primary: win32more.Windows.Win32.Storage.CloudFilters.CF_HYDRATION_POLICY_PRIMARY
    Modifier: win32more.Windows.Win32.Storage.CloudFilters.CF_HYDRATION_POLICY_MODIFIER
CF_HYDRATION_POLICY_MODIFIER = UInt16
CF_HYDRATION_POLICY_MODIFIER_NONE: win32more.Windows.Win32.Storage.CloudFilters.CF_HYDRATION_POLICY_MODIFIER = 0
CF_HYDRATION_POLICY_MODIFIER_VALIDATION_REQUIRED: win32more.Windows.Win32.Storage.CloudFilters.CF_HYDRATION_POLICY_MODIFIER = 1
CF_HYDRATION_POLICY_MODIFIER_STREAMING_ALLOWED: win32more.Windows.Win32.Storage.CloudFilters.CF_HYDRATION_POLICY_MODIFIER = 2
CF_HYDRATION_POLICY_MODIFIER_AUTO_DEHYDRATION_ALLOWED: win32more.Windows.Win32.Storage.CloudFilters.CF_HYDRATION_POLICY_MODIFIER = 4
CF_HYDRATION_POLICY_MODIFIER_ALLOW_FULL_RESTART_HYDRATION: win32more.Windows.Win32.Storage.CloudFilters.CF_HYDRATION_POLICY_MODIFIER = 8
CF_HYDRATION_POLICY_PRIMARY = UInt16
CF_HYDRATION_POLICY_PARTIAL: win32more.Windows.Win32.Storage.CloudFilters.CF_HYDRATION_POLICY_PRIMARY = 0
CF_HYDRATION_POLICY_PROGRESSIVE: win32more.Windows.Win32.Storage.CloudFilters.CF_HYDRATION_POLICY_PRIMARY = 1
CF_HYDRATION_POLICY_FULL: win32more.Windows.Win32.Storage.CloudFilters.CF_HYDRATION_POLICY_PRIMARY = 2
CF_HYDRATION_POLICY_ALWAYS_FULL: win32more.Windows.Win32.Storage.CloudFilters.CF_HYDRATION_POLICY_PRIMARY = 3
CF_INSYNC_POLICY = UInt32
CF_INSYNC_POLICY_NONE: win32more.Windows.Win32.Storage.CloudFilters.CF_INSYNC_POLICY = 0
CF_INSYNC_POLICY_TRACK_FILE_CREATION_TIME: win32more.Windows.Win32.Storage.CloudFilters.CF_INSYNC_POLICY = 1
CF_INSYNC_POLICY_TRACK_FILE_READONLY_ATTRIBUTE: win32more.Windows.Win32.Storage.CloudFilters.CF_INSYNC_POLICY = 2
CF_INSYNC_POLICY_TRACK_FILE_HIDDEN_ATTRIBUTE: win32more.Windows.Win32.Storage.CloudFilters.CF_INSYNC_POLICY = 4
CF_INSYNC_POLICY_TRACK_FILE_SYSTEM_ATTRIBUTE: win32more.Windows.Win32.Storage.CloudFilters.CF_INSYNC_POLICY = 8
CF_INSYNC_POLICY_TRACK_DIRECTORY_CREATION_TIME: win32more.Windows.Win32.Storage.CloudFilters.CF_INSYNC_POLICY = 16
CF_INSYNC_POLICY_TRACK_DIRECTORY_READONLY_ATTRIBUTE: win32more.Windows.Win32.Storage.CloudFilters.CF_INSYNC_POLICY = 32
CF_INSYNC_POLICY_TRACK_DIRECTORY_HIDDEN_ATTRIBUTE: win32more.Windows.Win32.Storage.CloudFilters.CF_INSYNC_POLICY = 64
CF_INSYNC_POLICY_TRACK_DIRECTORY_SYSTEM_ATTRIBUTE: win32more.Windows.Win32.Storage.CloudFilters.CF_INSYNC_POLICY = 128
CF_INSYNC_POLICY_TRACK_FILE_LAST_WRITE_TIME: win32more.Windows.Win32.Storage.CloudFilters.CF_INSYNC_POLICY = 256
CF_INSYNC_POLICY_TRACK_DIRECTORY_LAST_WRITE_TIME: win32more.Windows.Win32.Storage.CloudFilters.CF_INSYNC_POLICY = 512
CF_INSYNC_POLICY_TRACK_FILE_ALL: win32more.Windows.Win32.Storage.CloudFilters.CF_INSYNC_POLICY = 5592335
CF_INSYNC_POLICY_TRACK_DIRECTORY_ALL: win32more.Windows.Win32.Storage.CloudFilters.CF_INSYNC_POLICY = 11184880
CF_INSYNC_POLICY_TRACK_ALL: win32more.Windows.Win32.Storage.CloudFilters.CF_INSYNC_POLICY = 16777215
CF_INSYNC_POLICY_PRESERVE_INSYNC_FOR_SYNC_ENGINE: win32more.Windows.Win32.Storage.CloudFilters.CF_INSYNC_POLICY = 2147483648
CF_IN_SYNC_STATE = Int32
CF_IN_SYNC_STATE_NOT_IN_SYNC: win32more.Windows.Win32.Storage.CloudFilters.CF_IN_SYNC_STATE = 0
CF_IN_SYNC_STATE_IN_SYNC: win32more.Windows.Win32.Storage.CloudFilters.CF_IN_SYNC_STATE = 1
CF_OPEN_FILE_FLAGS = Int32
CF_OPEN_FILE_FLAG_NONE: win32more.Windows.Win32.Storage.CloudFilters.CF_OPEN_FILE_FLAGS = 0
CF_OPEN_FILE_FLAG_EXCLUSIVE: win32more.Windows.Win32.Storage.CloudFilters.CF_OPEN_FILE_FLAGS = 1
CF_OPEN_FILE_FLAG_WRITE_ACCESS: win32more.Windows.Win32.Storage.CloudFilters.CF_OPEN_FILE_FLAGS = 2
CF_OPEN_FILE_FLAG_DELETE_ACCESS: win32more.Windows.Win32.Storage.CloudFilters.CF_OPEN_FILE_FLAGS = 4
CF_OPEN_FILE_FLAG_FOREGROUND: win32more.Windows.Win32.Storage.CloudFilters.CF_OPEN_FILE_FLAGS = 8
CF_OPERATION_ACK_DATA_FLAGS = Int32
CF_OPERATION_ACK_DATA_FLAG_NONE: win32more.Windows.Win32.Storage.CloudFilters.CF_OPERATION_ACK_DATA_FLAGS = 0
CF_OPERATION_ACK_DEHYDRATE_FLAGS = Int32
CF_OPERATION_ACK_DEHYDRATE_FLAG_NONE: win32more.Windows.Win32.Storage.CloudFilters.CF_OPERATION_ACK_DEHYDRATE_FLAGS = 0
CF_OPERATION_ACK_DELETE_FLAGS = Int32
CF_OPERATION_ACK_DELETE_FLAG_NONE: win32more.Windows.Win32.Storage.CloudFilters.CF_OPERATION_ACK_DELETE_FLAGS = 0
CF_OPERATION_ACK_RENAME_FLAGS = Int32
CF_OPERATION_ACK_RENAME_FLAG_NONE: win32more.Windows.Win32.Storage.CloudFilters.CF_OPERATION_ACK_RENAME_FLAGS = 0
class CF_OPERATION_INFO(Structure):
    StructSize: UInt32
    Type: win32more.Windows.Win32.Storage.CloudFilters.CF_OPERATION_TYPE
    ConnectionKey: win32more.Windows.Win32.Storage.CloudFilters.CF_CONNECTION_KEY
    TransferKey: Int64
    CorrelationVector: POINTER(win32more.Windows.Win32.System.CorrelationVector.CORRELATION_VECTOR)
    SyncStatus: POINTER(win32more.Windows.Win32.Storage.CloudFilters.CF_SYNC_STATUS)
    RequestKey: Int64
class CF_OPERATION_PARAMETERS(Structure):
    ParamSize: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        TransferData: _TransferData_e__Struct
        RetrieveData: _RetrieveData_e__Struct
        AckData: _AckData_e__Struct
        RestartHydration: _RestartHydration_e__Struct
        TransferPlaceholders: _TransferPlaceholders_e__Struct
        AckDehydrate: _AckDehydrate_e__Struct
        AckRename: _AckRename_e__Struct
        AckDelete: _AckDelete_e__Struct
        class _TransferData_e__Struct(Structure):
            Flags: win32more.Windows.Win32.Storage.CloudFilters.CF_OPERATION_TRANSFER_DATA_FLAGS
            CompletionStatus: win32more.Windows.Win32.Foundation.NTSTATUS
            Buffer: VoidPtr
            Offset: Int64
            Length: Int64
        class _RetrieveData_e__Struct(Structure):
            Flags: win32more.Windows.Win32.Storage.CloudFilters.CF_OPERATION_RETRIEVE_DATA_FLAGS
            Buffer: VoidPtr
            Offset: Int64
            Length: Int64
            ReturnedLength: Int64
        class _AckData_e__Struct(Structure):
            Flags: win32more.Windows.Win32.Storage.CloudFilters.CF_OPERATION_ACK_DATA_FLAGS
            CompletionStatus: win32more.Windows.Win32.Foundation.NTSTATUS
            Offset: Int64
            Length: Int64
        class _RestartHydration_e__Struct(Structure):
            Flags: win32more.Windows.Win32.Storage.CloudFilters.CF_OPERATION_RESTART_HYDRATION_FLAGS
            FsMetadata: POINTER(win32more.Windows.Win32.Storage.CloudFilters.CF_FS_METADATA)
            FileIdentity: VoidPtr
            FileIdentityLength: UInt32
        class _TransferPlaceholders_e__Struct(Structure):
            Flags: win32more.Windows.Win32.Storage.CloudFilters.CF_OPERATION_TRANSFER_PLACEHOLDERS_FLAGS
            CompletionStatus: win32more.Windows.Win32.Foundation.NTSTATUS
            PlaceholderTotalCount: Int64
            PlaceholderArray: POINTER(win32more.Windows.Win32.Storage.CloudFilters.CF_PLACEHOLDER_CREATE_INFO)
            PlaceholderCount: UInt32
            EntriesProcessed: UInt32
        class _AckDehydrate_e__Struct(Structure):
            Flags: win32more.Windows.Win32.Storage.CloudFilters.CF_OPERATION_ACK_DEHYDRATE_FLAGS
            CompletionStatus: win32more.Windows.Win32.Foundation.NTSTATUS
            FileIdentity: VoidPtr
            FileIdentityLength: UInt32
        class _AckRename_e__Struct(Structure):
            Flags: win32more.Windows.Win32.Storage.CloudFilters.CF_OPERATION_ACK_RENAME_FLAGS
            CompletionStatus: win32more.Windows.Win32.Foundation.NTSTATUS
        class _AckDelete_e__Struct(Structure):
            Flags: win32more.Windows.Win32.Storage.CloudFilters.CF_OPERATION_ACK_DELETE_FLAGS
            CompletionStatus: win32more.Windows.Win32.Foundation.NTSTATUS
CF_OPERATION_RESTART_HYDRATION_FLAGS = Int32
CF_OPERATION_RESTART_HYDRATION_FLAG_NONE: win32more.Windows.Win32.Storage.CloudFilters.CF_OPERATION_RESTART_HYDRATION_FLAGS = 0
CF_OPERATION_RESTART_HYDRATION_FLAG_MARK_IN_SYNC: win32more.Windows.Win32.Storage.CloudFilters.CF_OPERATION_RESTART_HYDRATION_FLAGS = 1
CF_OPERATION_RETRIEVE_DATA_FLAGS = Int32
CF_OPERATION_RETRIEVE_DATA_FLAG_NONE: win32more.Windows.Win32.Storage.CloudFilters.CF_OPERATION_RETRIEVE_DATA_FLAGS = 0
CF_OPERATION_TRANSFER_DATA_FLAGS = Int32
CF_OPERATION_TRANSFER_DATA_FLAG_NONE: win32more.Windows.Win32.Storage.CloudFilters.CF_OPERATION_TRANSFER_DATA_FLAGS = 0
CF_OPERATION_TRANSFER_PLACEHOLDERS_FLAGS = Int32
CF_OPERATION_TRANSFER_PLACEHOLDERS_FLAG_NONE: win32more.Windows.Win32.Storage.CloudFilters.CF_OPERATION_TRANSFER_PLACEHOLDERS_FLAGS = 0
CF_OPERATION_TRANSFER_PLACEHOLDERS_FLAG_STOP_ON_ERROR: win32more.Windows.Win32.Storage.CloudFilters.CF_OPERATION_TRANSFER_PLACEHOLDERS_FLAGS = 1
CF_OPERATION_TRANSFER_PLACEHOLDERS_FLAG_DISABLE_ON_DEMAND_POPULATION: win32more.Windows.Win32.Storage.CloudFilters.CF_OPERATION_TRANSFER_PLACEHOLDERS_FLAGS = 2
CF_OPERATION_TYPE = Int32
CF_OPERATION_TYPE_TRANSFER_DATA: win32more.Windows.Win32.Storage.CloudFilters.CF_OPERATION_TYPE = 0
CF_OPERATION_TYPE_RETRIEVE_DATA: win32more.Windows.Win32.Storage.CloudFilters.CF_OPERATION_TYPE = 1
CF_OPERATION_TYPE_ACK_DATA: win32more.Windows.Win32.Storage.CloudFilters.CF_OPERATION_TYPE = 2
CF_OPERATION_TYPE_RESTART_HYDRATION: win32more.Windows.Win32.Storage.CloudFilters.CF_OPERATION_TYPE = 3
CF_OPERATION_TYPE_TRANSFER_PLACEHOLDERS: win32more.Windows.Win32.Storage.CloudFilters.CF_OPERATION_TYPE = 4
CF_OPERATION_TYPE_ACK_DEHYDRATE: win32more.Windows.Win32.Storage.CloudFilters.CF_OPERATION_TYPE = 5
CF_OPERATION_TYPE_ACK_DELETE: win32more.Windows.Win32.Storage.CloudFilters.CF_OPERATION_TYPE = 6
CF_OPERATION_TYPE_ACK_RENAME: win32more.Windows.Win32.Storage.CloudFilters.CF_OPERATION_TYPE = 7
CF_PIN_STATE = Int32
CF_PIN_STATE_UNSPECIFIED: win32more.Windows.Win32.Storage.CloudFilters.CF_PIN_STATE = 0
CF_PIN_STATE_PINNED: win32more.Windows.Win32.Storage.CloudFilters.CF_PIN_STATE = 1
CF_PIN_STATE_UNPINNED: win32more.Windows.Win32.Storage.CloudFilters.CF_PIN_STATE = 2
CF_PIN_STATE_EXCLUDED: win32more.Windows.Win32.Storage.CloudFilters.CF_PIN_STATE = 3
CF_PIN_STATE_INHERIT: win32more.Windows.Win32.Storage.CloudFilters.CF_PIN_STATE = 4
class CF_PLACEHOLDER_BASIC_INFO(Structure):
    PinState: win32more.Windows.Win32.Storage.CloudFilters.CF_PIN_STATE
    InSyncState: win32more.Windows.Win32.Storage.CloudFilters.CF_IN_SYNC_STATE
    FileId: Int64
    SyncRootFileId: Int64
    FileIdentityLength: UInt32
    FileIdentity: Byte * 1
CF_PLACEHOLDER_CREATE_FLAGS = Int32
CF_PLACEHOLDER_CREATE_FLAG_NONE: win32more.Windows.Win32.Storage.CloudFilters.CF_PLACEHOLDER_CREATE_FLAGS = 0
CF_PLACEHOLDER_CREATE_FLAG_DISABLE_ON_DEMAND_POPULATION: win32more.Windows.Win32.Storage.CloudFilters.CF_PLACEHOLDER_CREATE_FLAGS = 1
CF_PLACEHOLDER_CREATE_FLAG_MARK_IN_SYNC: win32more.Windows.Win32.Storage.CloudFilters.CF_PLACEHOLDER_CREATE_FLAGS = 2
CF_PLACEHOLDER_CREATE_FLAG_SUPERSEDE: win32more.Windows.Win32.Storage.CloudFilters.CF_PLACEHOLDER_CREATE_FLAGS = 4
CF_PLACEHOLDER_CREATE_FLAG_ALWAYS_FULL: win32more.Windows.Win32.Storage.CloudFilters.CF_PLACEHOLDER_CREATE_FLAGS = 8
class CF_PLACEHOLDER_CREATE_INFO(Structure):
    RelativeFileName: win32more.Windows.Win32.Foundation.PWSTR
    FsMetadata: win32more.Windows.Win32.Storage.CloudFilters.CF_FS_METADATA
    FileIdentity: VoidPtr
    FileIdentityLength: UInt32
    Flags: win32more.Windows.Win32.Storage.CloudFilters.CF_PLACEHOLDER_CREATE_FLAGS
    Result: win32more.Windows.Win32.Foundation.HRESULT
    CreateUsn: Int64
CF_PLACEHOLDER_INFO_CLASS = Int32
CF_PLACEHOLDER_INFO_BASIC: win32more.Windows.Win32.Storage.CloudFilters.CF_PLACEHOLDER_INFO_CLASS = 0
CF_PLACEHOLDER_INFO_STANDARD: win32more.Windows.Win32.Storage.CloudFilters.CF_PLACEHOLDER_INFO_CLASS = 1
CF_PLACEHOLDER_MANAGEMENT_POLICY = Int32
CF_PLACEHOLDER_MANAGEMENT_POLICY_DEFAULT: win32more.Windows.Win32.Storage.CloudFilters.CF_PLACEHOLDER_MANAGEMENT_POLICY = 0
CF_PLACEHOLDER_MANAGEMENT_POLICY_CREATE_UNRESTRICTED: win32more.Windows.Win32.Storage.CloudFilters.CF_PLACEHOLDER_MANAGEMENT_POLICY = 1
CF_PLACEHOLDER_MANAGEMENT_POLICY_CONVERT_TO_UNRESTRICTED: win32more.Windows.Win32.Storage.CloudFilters.CF_PLACEHOLDER_MANAGEMENT_POLICY = 2
CF_PLACEHOLDER_MANAGEMENT_POLICY_UPDATE_UNRESTRICTED: win32more.Windows.Win32.Storage.CloudFilters.CF_PLACEHOLDER_MANAGEMENT_POLICY = 4
CF_PLACEHOLDER_RANGE_INFO_CLASS = Int32
CF_PLACEHOLDER_RANGE_INFO_ONDISK: win32more.Windows.Win32.Storage.CloudFilters.CF_PLACEHOLDER_RANGE_INFO_CLASS = 1
CF_PLACEHOLDER_RANGE_INFO_VALIDATED: win32more.Windows.Win32.Storage.CloudFilters.CF_PLACEHOLDER_RANGE_INFO_CLASS = 2
CF_PLACEHOLDER_RANGE_INFO_MODIFIED: win32more.Windows.Win32.Storage.CloudFilters.CF_PLACEHOLDER_RANGE_INFO_CLASS = 3
class CF_PLACEHOLDER_STANDARD_INFO(Structure):
    OnDiskDataSize: Int64
    ValidatedDataSize: Int64
    ModifiedDataSize: Int64
    PropertiesSize: Int64
    PinState: win32more.Windows.Win32.Storage.CloudFilters.CF_PIN_STATE
    InSyncState: win32more.Windows.Win32.Storage.CloudFilters.CF_IN_SYNC_STATE
    FileId: Int64
    SyncRootFileId: Int64
    FileIdentityLength: UInt32
    FileIdentity: Byte * 1
CF_PLACEHOLDER_STATE = UInt32
CF_PLACEHOLDER_STATE_NO_STATES: win32more.Windows.Win32.Storage.CloudFilters.CF_PLACEHOLDER_STATE = 0
CF_PLACEHOLDER_STATE_PLACEHOLDER: win32more.Windows.Win32.Storage.CloudFilters.CF_PLACEHOLDER_STATE = 1
CF_PLACEHOLDER_STATE_SYNC_ROOT: win32more.Windows.Win32.Storage.CloudFilters.CF_PLACEHOLDER_STATE = 2
CF_PLACEHOLDER_STATE_ESSENTIAL_PROP_PRESENT: win32more.Windows.Win32.Storage.CloudFilters.CF_PLACEHOLDER_STATE = 4
CF_PLACEHOLDER_STATE_IN_SYNC: win32more.Windows.Win32.Storage.CloudFilters.CF_PLACEHOLDER_STATE = 8
CF_PLACEHOLDER_STATE_PARTIAL: win32more.Windows.Win32.Storage.CloudFilters.CF_PLACEHOLDER_STATE = 16
CF_PLACEHOLDER_STATE_PARTIALLY_ON_DISK: win32more.Windows.Win32.Storage.CloudFilters.CF_PLACEHOLDER_STATE = 32
CF_PLACEHOLDER_STATE_INVALID: win32more.Windows.Win32.Storage.CloudFilters.CF_PLACEHOLDER_STATE = 4294967295
class CF_PLATFORM_INFO(Structure):
    BuildNumber: UInt32
    RevisionNumber: UInt32
    IntegrationNumber: UInt32
class CF_POPULATION_POLICY(Structure):
    Primary: win32more.Windows.Win32.Storage.CloudFilters.CF_POPULATION_POLICY_PRIMARY
    Modifier: win32more.Windows.Win32.Storage.CloudFilters.CF_POPULATION_POLICY_MODIFIER
CF_POPULATION_POLICY_MODIFIER = UInt16
CF_POPULATION_POLICY_MODIFIER_NONE: win32more.Windows.Win32.Storage.CloudFilters.CF_POPULATION_POLICY_MODIFIER = 0
CF_POPULATION_POLICY_PRIMARY = UInt16
CF_POPULATION_POLICY_PARTIAL: win32more.Windows.Win32.Storage.CloudFilters.CF_POPULATION_POLICY_PRIMARY = 0
CF_POPULATION_POLICY_FULL: win32more.Windows.Win32.Storage.CloudFilters.CF_POPULATION_POLICY_PRIMARY = 2
CF_POPULATION_POLICY_ALWAYS_FULL: win32more.Windows.Win32.Storage.CloudFilters.CF_POPULATION_POLICY_PRIMARY = 3
class CF_PROCESS_INFO(Structure):
    StructSize: UInt32
    ProcessId: UInt32
    ImagePath: win32more.Windows.Win32.Foundation.PWSTR
    PackageName: win32more.Windows.Win32.Foundation.PWSTR
    ApplicationId: win32more.Windows.Win32.Foundation.PWSTR
    CommandLine: win32more.Windows.Win32.Foundation.PWSTR
    SessionId: UInt32
CF_REGISTER_FLAGS = Int32
CF_REGISTER_FLAG_NONE: win32more.Windows.Win32.Storage.CloudFilters.CF_REGISTER_FLAGS = 0
CF_REGISTER_FLAG_UPDATE: win32more.Windows.Win32.Storage.CloudFilters.CF_REGISTER_FLAGS = 1
CF_REGISTER_FLAG_DISABLE_ON_DEMAND_POPULATION_ON_ROOT: win32more.Windows.Win32.Storage.CloudFilters.CF_REGISTER_FLAGS = 2
CF_REGISTER_FLAG_MARK_IN_SYNC_ON_ROOT: win32more.Windows.Win32.Storage.CloudFilters.CF_REGISTER_FLAGS = 4
CF_REVERT_FLAGS = Int32
CF_REVERT_FLAG_NONE: win32more.Windows.Win32.Storage.CloudFilters.CF_REVERT_FLAGS = 0
CF_SET_IN_SYNC_FLAGS = Int32
CF_SET_IN_SYNC_FLAG_NONE: win32more.Windows.Win32.Storage.CloudFilters.CF_SET_IN_SYNC_FLAGS = 0
CF_SET_PIN_FLAGS = Int32
CF_SET_PIN_FLAG_NONE: win32more.Windows.Win32.Storage.CloudFilters.CF_SET_PIN_FLAGS = 0
CF_SET_PIN_FLAG_RECURSE: win32more.Windows.Win32.Storage.CloudFilters.CF_SET_PIN_FLAGS = 1
CF_SET_PIN_FLAG_RECURSE_ONLY: win32more.Windows.Win32.Storage.CloudFilters.CF_SET_PIN_FLAGS = 2
CF_SET_PIN_FLAG_RECURSE_STOP_ON_ERROR: win32more.Windows.Win32.Storage.CloudFilters.CF_SET_PIN_FLAGS = 4
class CF_SYNC_POLICIES(Structure):
    StructSize: UInt32
    Hydration: win32more.Windows.Win32.Storage.CloudFilters.CF_HYDRATION_POLICY
    Population: win32more.Windows.Win32.Storage.CloudFilters.CF_POPULATION_POLICY
    InSync: win32more.Windows.Win32.Storage.CloudFilters.CF_INSYNC_POLICY
    HardLink: win32more.Windows.Win32.Storage.CloudFilters.CF_HARDLINK_POLICY
    PlaceholderManagement: win32more.Windows.Win32.Storage.CloudFilters.CF_PLACEHOLDER_MANAGEMENT_POLICY
CF_SYNC_PROVIDER_STATUS = UInt32
CF_PROVIDER_STATUS_DISCONNECTED: win32more.Windows.Win32.Storage.CloudFilters.CF_SYNC_PROVIDER_STATUS = 0
CF_PROVIDER_STATUS_IDLE: win32more.Windows.Win32.Storage.CloudFilters.CF_SYNC_PROVIDER_STATUS = 1
CF_PROVIDER_STATUS_POPULATE_NAMESPACE: win32more.Windows.Win32.Storage.CloudFilters.CF_SYNC_PROVIDER_STATUS = 2
CF_PROVIDER_STATUS_POPULATE_METADATA: win32more.Windows.Win32.Storage.CloudFilters.CF_SYNC_PROVIDER_STATUS = 4
CF_PROVIDER_STATUS_POPULATE_CONTENT: win32more.Windows.Win32.Storage.CloudFilters.CF_SYNC_PROVIDER_STATUS = 8
CF_PROVIDER_STATUS_SYNC_INCREMENTAL: win32more.Windows.Win32.Storage.CloudFilters.CF_SYNC_PROVIDER_STATUS = 16
CF_PROVIDER_STATUS_SYNC_FULL: win32more.Windows.Win32.Storage.CloudFilters.CF_SYNC_PROVIDER_STATUS = 32
CF_PROVIDER_STATUS_CONNECTIVITY_LOST: win32more.Windows.Win32.Storage.CloudFilters.CF_SYNC_PROVIDER_STATUS = 64
CF_PROVIDER_STATUS_CLEAR_FLAGS: win32more.Windows.Win32.Storage.CloudFilters.CF_SYNC_PROVIDER_STATUS = 2147483648
CF_PROVIDER_STATUS_TERMINATED: win32more.Windows.Win32.Storage.CloudFilters.CF_SYNC_PROVIDER_STATUS = 3221225473
CF_PROVIDER_STATUS_ERROR: win32more.Windows.Win32.Storage.CloudFilters.CF_SYNC_PROVIDER_STATUS = 3221225474
class CF_SYNC_REGISTRATION(Structure):
    StructSize: UInt32
    ProviderName: win32more.Windows.Win32.Foundation.PWSTR
    ProviderVersion: win32more.Windows.Win32.Foundation.PWSTR
    SyncRootIdentity: VoidPtr
    SyncRootIdentityLength: UInt32
    FileIdentity: VoidPtr
    FileIdentityLength: UInt32
    ProviderId: Guid
class CF_SYNC_ROOT_BASIC_INFO(Structure):
    SyncRootFileId: Int64
CF_SYNC_ROOT_INFO_CLASS = Int32
CF_SYNC_ROOT_INFO_BASIC: win32more.Windows.Win32.Storage.CloudFilters.CF_SYNC_ROOT_INFO_CLASS = 0
CF_SYNC_ROOT_INFO_STANDARD: win32more.Windows.Win32.Storage.CloudFilters.CF_SYNC_ROOT_INFO_CLASS = 1
CF_SYNC_ROOT_INFO_PROVIDER: win32more.Windows.Win32.Storage.CloudFilters.CF_SYNC_ROOT_INFO_CLASS = 2
class CF_SYNC_ROOT_PROVIDER_INFO(Structure):
    ProviderStatus: win32more.Windows.Win32.Storage.CloudFilters.CF_SYNC_PROVIDER_STATUS
    ProviderName: Char * 256
    ProviderVersion: Char * 256
class CF_SYNC_ROOT_STANDARD_INFO(Structure):
    SyncRootFileId: Int64
    HydrationPolicy: win32more.Windows.Win32.Storage.CloudFilters.CF_HYDRATION_POLICY
    PopulationPolicy: win32more.Windows.Win32.Storage.CloudFilters.CF_POPULATION_POLICY
    InSyncPolicy: win32more.Windows.Win32.Storage.CloudFilters.CF_INSYNC_POLICY
    HardLinkPolicy: win32more.Windows.Win32.Storage.CloudFilters.CF_HARDLINK_POLICY
    ProviderStatus: win32more.Windows.Win32.Storage.CloudFilters.CF_SYNC_PROVIDER_STATUS
    ProviderName: Char * 256
    ProviderVersion: Char * 256
    SyncRootIdentityLength: UInt32
    SyncRootIdentity: Byte * 1
class CF_SYNC_STATUS(Structure):
    StructSize: UInt32
    Code: UInt32
    DescriptionOffset: UInt32
    DescriptionLength: UInt32
    DeviceIdOffset: UInt32
    DeviceIdLength: UInt32
CF_UPDATE_FLAGS = Int32
CF_UPDATE_FLAG_NONE: win32more.Windows.Win32.Storage.CloudFilters.CF_UPDATE_FLAGS = 0
CF_UPDATE_FLAG_VERIFY_IN_SYNC: win32more.Windows.Win32.Storage.CloudFilters.CF_UPDATE_FLAGS = 1
CF_UPDATE_FLAG_MARK_IN_SYNC: win32more.Windows.Win32.Storage.CloudFilters.CF_UPDATE_FLAGS = 2
CF_UPDATE_FLAG_DEHYDRATE: win32more.Windows.Win32.Storage.CloudFilters.CF_UPDATE_FLAGS = 4
CF_UPDATE_FLAG_ENABLE_ON_DEMAND_POPULATION: win32more.Windows.Win32.Storage.CloudFilters.CF_UPDATE_FLAGS = 8
CF_UPDATE_FLAG_DISABLE_ON_DEMAND_POPULATION: win32more.Windows.Win32.Storage.CloudFilters.CF_UPDATE_FLAGS = 16
CF_UPDATE_FLAG_REMOVE_FILE_IDENTITY: win32more.Windows.Win32.Storage.CloudFilters.CF_UPDATE_FLAGS = 32
CF_UPDATE_FLAG_CLEAR_IN_SYNC: win32more.Windows.Win32.Storage.CloudFilters.CF_UPDATE_FLAGS = 64
CF_UPDATE_FLAG_REMOVE_PROPERTY: win32more.Windows.Win32.Storage.CloudFilters.CF_UPDATE_FLAGS = 128
CF_UPDATE_FLAG_PASSTHROUGH_FS_METADATA: win32more.Windows.Win32.Storage.CloudFilters.CF_UPDATE_FLAGS = 256
CF_UPDATE_FLAG_ALWAYS_FULL: win32more.Windows.Win32.Storage.CloudFilters.CF_UPDATE_FLAGS = 512
CF_UPDATE_FLAG_ALLOW_PARTIAL: win32more.Windows.Win32.Storage.CloudFilters.CF_UPDATE_FLAGS = 1024


make_ready(__name__)
