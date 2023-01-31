from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Storage.CloudFilters
import win32more.Storage.FileSystem
import win32more.System.CorrelationVector
import win32more.System.IO
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
CF_REQUEST_KEY_DEFAULT: UInt32 = 0
CF_PLACEHOLDER_MAX_FILE_IDENTITY_LENGTH: UInt32 = 4096
CF_MAX_PRIORITY_HINT: UInt32 = 15
CF_MAX_PROVIDER_NAME_LENGTH: UInt32 = 255
CF_MAX_PROVIDER_VERSION_LENGTH: UInt32 = 255
@winfunctype('cldapi.dll')
def CfGetPlatformInfo(PlatformVersion: POINTER(win32more.Storage.CloudFilters.CF_PLATFORM_INFO_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfRegisterSyncRoot(SyncRootPath: win32more.Foundation.PWSTR, Registration: POINTER(win32more.Storage.CloudFilters.CF_SYNC_REGISTRATION_head), Policies: POINTER(win32more.Storage.CloudFilters.CF_SYNC_POLICIES_head), RegisterFlags: win32more.Storage.CloudFilters.CF_REGISTER_FLAGS) -> win32more.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfUnregisterSyncRoot(SyncRootPath: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfConnectSyncRoot(SyncRootPath: win32more.Foundation.PWSTR, CallbackTable: POINTER(win32more.Storage.CloudFilters.CF_CALLBACK_REGISTRATION_head), CallbackContext: c_void_p, ConnectFlags: win32more.Storage.CloudFilters.CF_CONNECT_FLAGS, ConnectionKey: POINTER(win32more.Storage.CloudFilters.CF_CONNECTION_KEY)) -> win32more.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfDisconnectSyncRoot(ConnectionKey: win32more.Storage.CloudFilters.CF_CONNECTION_KEY) -> win32more.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfGetTransferKey(FileHandle: win32more.Foundation.HANDLE, TransferKey: POINTER(win32more.Foundation.LARGE_INTEGER_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfReleaseTransferKey(FileHandle: win32more.Foundation.HANDLE, TransferKey: POINTER(win32more.Foundation.LARGE_INTEGER_head)) -> Void: ...
@winfunctype('cldapi.dll')
def CfExecute(OpInfo: POINTER(win32more.Storage.CloudFilters.CF_OPERATION_INFO_head), OpParams: POINTER(win32more.Storage.CloudFilters.CF_OPERATION_PARAMETERS_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfUpdateSyncProviderStatus(ConnectionKey: win32more.Storage.CloudFilters.CF_CONNECTION_KEY, ProviderStatus: win32more.Storage.CloudFilters.CF_SYNC_PROVIDER_STATUS) -> win32more.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfQuerySyncProviderStatus(ConnectionKey: win32more.Storage.CloudFilters.CF_CONNECTION_KEY, ProviderStatus: POINTER(win32more.Storage.CloudFilters.CF_SYNC_PROVIDER_STATUS)) -> win32more.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfReportSyncStatus(SyncRootPath: win32more.Foundation.PWSTR, SyncStatus: POINTER(win32more.Storage.CloudFilters.CF_SYNC_STATUS_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfCreatePlaceholders(BaseDirectoryPath: win32more.Foundation.PWSTR, PlaceholderArray: POINTER(win32more.Storage.CloudFilters.CF_PLACEHOLDER_CREATE_INFO_head), PlaceholderCount: UInt32, CreateFlags: win32more.Storage.CloudFilters.CF_CREATE_FLAGS, EntriesProcessed: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfOpenFileWithOplock(FilePath: win32more.Foundation.PWSTR, Flags: win32more.Storage.CloudFilters.CF_OPEN_FILE_FLAGS, ProtectedHandle: POINTER(win32more.Foundation.HANDLE)) -> win32more.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfReferenceProtectedHandle(ProtectedHandle: win32more.Foundation.HANDLE) -> win32more.Foundation.BOOLEAN: ...
@winfunctype('cldapi.dll')
def CfGetWin32HandleFromProtectedHandle(ProtectedHandle: win32more.Foundation.HANDLE) -> win32more.Foundation.HANDLE: ...
@winfunctype('cldapi.dll')
def CfReleaseProtectedHandle(ProtectedHandle: win32more.Foundation.HANDLE) -> Void: ...
@winfunctype('cldapi.dll')
def CfCloseHandle(FileHandle: win32more.Foundation.HANDLE) -> Void: ...
@winfunctype('cldapi.dll')
def CfConvertToPlaceholder(FileHandle: win32more.Foundation.HANDLE, FileIdentity: c_void_p, FileIdentityLength: UInt32, ConvertFlags: win32more.Storage.CloudFilters.CF_CONVERT_FLAGS, ConvertUsn: POINTER(Int64), Overlapped: POINTER(win32more.System.IO.OVERLAPPED_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfUpdatePlaceholder(FileHandle: win32more.Foundation.HANDLE, FsMetadata: POINTER(win32more.Storage.CloudFilters.CF_FS_METADATA_head), FileIdentity: c_void_p, FileIdentityLength: UInt32, DehydrateRangeArray: POINTER(win32more.Storage.CloudFilters.CF_FILE_RANGE_head), DehydrateRangeCount: UInt32, UpdateFlags: win32more.Storage.CloudFilters.CF_UPDATE_FLAGS, UpdateUsn: POINTER(Int64), Overlapped: POINTER(win32more.System.IO.OVERLAPPED_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfRevertPlaceholder(FileHandle: win32more.Foundation.HANDLE, RevertFlags: win32more.Storage.CloudFilters.CF_REVERT_FLAGS, Overlapped: POINTER(win32more.System.IO.OVERLAPPED_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfHydratePlaceholder(FileHandle: win32more.Foundation.HANDLE, StartingOffset: win32more.Foundation.LARGE_INTEGER, Length: win32more.Foundation.LARGE_INTEGER, HydrateFlags: win32more.Storage.CloudFilters.CF_HYDRATE_FLAGS, Overlapped: POINTER(win32more.System.IO.OVERLAPPED_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfDehydratePlaceholder(FileHandle: win32more.Foundation.HANDLE, StartingOffset: win32more.Foundation.LARGE_INTEGER, Length: win32more.Foundation.LARGE_INTEGER, DehydrateFlags: win32more.Storage.CloudFilters.CF_DEHYDRATE_FLAGS, Overlapped: POINTER(win32more.System.IO.OVERLAPPED_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfSetPinState(FileHandle: win32more.Foundation.HANDLE, PinState: win32more.Storage.CloudFilters.CF_PIN_STATE, PinFlags: win32more.Storage.CloudFilters.CF_SET_PIN_FLAGS, Overlapped: POINTER(win32more.System.IO.OVERLAPPED_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfSetInSyncState(FileHandle: win32more.Foundation.HANDLE, InSyncState: win32more.Storage.CloudFilters.CF_IN_SYNC_STATE, InSyncFlags: win32more.Storage.CloudFilters.CF_SET_IN_SYNC_FLAGS, InSyncUsn: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfSetCorrelationVector(FileHandle: win32more.Foundation.HANDLE, CorrelationVector: POINTER(win32more.System.CorrelationVector.CORRELATION_VECTOR_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfGetCorrelationVector(FileHandle: win32more.Foundation.HANDLE, CorrelationVector: POINTER(win32more.System.CorrelationVector.CORRELATION_VECTOR_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfGetPlaceholderStateFromAttributeTag(FileAttributes: UInt32, ReparseTag: UInt32) -> win32more.Storage.CloudFilters.CF_PLACEHOLDER_STATE: ...
@winfunctype('cldapi.dll')
def CfGetPlaceholderStateFromFileInfo(InfoBuffer: c_void_p, InfoClass: win32more.Storage.FileSystem.FILE_INFO_BY_HANDLE_CLASS) -> win32more.Storage.CloudFilters.CF_PLACEHOLDER_STATE: ...
@winfunctype('cldapi.dll')
def CfGetPlaceholderStateFromFindData(FindData: POINTER(win32more.Storage.FileSystem.WIN32_FIND_DATAA_head)) -> win32more.Storage.CloudFilters.CF_PLACEHOLDER_STATE: ...
@winfunctype('cldapi.dll')
def CfGetPlaceholderInfo(FileHandle: win32more.Foundation.HANDLE, InfoClass: win32more.Storage.CloudFilters.CF_PLACEHOLDER_INFO_CLASS, InfoBuffer: c_void_p, InfoBufferLength: UInt32, ReturnedLength: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfGetSyncRootInfoByPath(FilePath: win32more.Foundation.PWSTR, InfoClass: win32more.Storage.CloudFilters.CF_SYNC_ROOT_INFO_CLASS, InfoBuffer: c_void_p, InfoBufferLength: UInt32, ReturnedLength: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfGetSyncRootInfoByHandle(FileHandle: win32more.Foundation.HANDLE, InfoClass: win32more.Storage.CloudFilters.CF_SYNC_ROOT_INFO_CLASS, InfoBuffer: c_void_p, InfoBufferLength: UInt32, ReturnedLength: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfGetPlaceholderRangeInfo(FileHandle: win32more.Foundation.HANDLE, InfoClass: win32more.Storage.CloudFilters.CF_PLACEHOLDER_RANGE_INFO_CLASS, StartingOffset: win32more.Foundation.LARGE_INTEGER, Length: win32more.Foundation.LARGE_INTEGER, InfoBuffer: c_void_p, InfoBufferLength: UInt32, ReturnedLength: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfReportProviderProgress(ConnectionKey: win32more.Storage.CloudFilters.CF_CONNECTION_KEY, TransferKey: win32more.Foundation.LARGE_INTEGER, ProviderProgressTotal: win32more.Foundation.LARGE_INTEGER, ProviderProgressCompleted: win32more.Foundation.LARGE_INTEGER) -> win32more.Foundation.HRESULT: ...
@winfunctype('cldapi.dll')
def CfReportProviderProgress2(ConnectionKey: win32more.Storage.CloudFilters.CF_CONNECTION_KEY, TransferKey: win32more.Foundation.LARGE_INTEGER, RequestKey: win32more.Foundation.LARGE_INTEGER, ProviderProgressTotal: win32more.Foundation.LARGE_INTEGER, ProviderProgressCompleted: win32more.Foundation.LARGE_INTEGER, TargetSessionId: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def CF_CALLBACK(CallbackInfo: POINTER(win32more.Storage.CloudFilters.CF_CALLBACK_INFO_head), CallbackParameters: POINTER(win32more.Storage.CloudFilters.CF_CALLBACK_PARAMETERS_head)) -> Void: ...
CF_CALLBACK_CANCEL_FLAGS = UInt32
CF_CALLBACK_CANCEL_FLAG_NONE: CF_CALLBACK_CANCEL_FLAGS = 0
CF_CALLBACK_CANCEL_FLAG_IO_TIMEOUT: CF_CALLBACK_CANCEL_FLAGS = 1
CF_CALLBACK_CANCEL_FLAG_IO_ABORTED: CF_CALLBACK_CANCEL_FLAGS = 2
CF_CALLBACK_CLOSE_COMPLETION_FLAGS = UInt32
CF_CALLBACK_CLOSE_COMPLETION_FLAG_NONE: CF_CALLBACK_CLOSE_COMPLETION_FLAGS = 0
CF_CALLBACK_CLOSE_COMPLETION_FLAG_DELETED: CF_CALLBACK_CLOSE_COMPLETION_FLAGS = 1
CF_CALLBACK_DEHYDRATE_COMPLETION_FLAGS = UInt32
CF_CALLBACK_DEHYDRATE_COMPLETION_FLAG_NONE: CF_CALLBACK_DEHYDRATE_COMPLETION_FLAGS = 0
CF_CALLBACK_DEHYDRATE_COMPLETION_FLAG_BACKGROUND: CF_CALLBACK_DEHYDRATE_COMPLETION_FLAGS = 1
CF_CALLBACK_DEHYDRATE_COMPLETION_FLAG_DEHYDRATED: CF_CALLBACK_DEHYDRATE_COMPLETION_FLAGS = 2
CF_CALLBACK_DEHYDRATE_FLAGS = UInt32
CF_CALLBACK_DEHYDRATE_FLAG_NONE: CF_CALLBACK_DEHYDRATE_FLAGS = 0
CF_CALLBACK_DEHYDRATE_FLAG_BACKGROUND: CF_CALLBACK_DEHYDRATE_FLAGS = 1
CF_CALLBACK_DEHYDRATION_REASON = Int32
CF_CALLBACK_DEHYDRATION_REASON_NONE: CF_CALLBACK_DEHYDRATION_REASON = 0
CF_CALLBACK_DEHYDRATION_REASON_USER_MANUAL: CF_CALLBACK_DEHYDRATION_REASON = 1
CF_CALLBACK_DEHYDRATION_REASON_SYSTEM_LOW_SPACE: CF_CALLBACK_DEHYDRATION_REASON = 2
CF_CALLBACK_DEHYDRATION_REASON_SYSTEM_INACTIVITY: CF_CALLBACK_DEHYDRATION_REASON = 3
CF_CALLBACK_DEHYDRATION_REASON_SYSTEM_OS_UPGRADE: CF_CALLBACK_DEHYDRATION_REASON = 4
CF_CALLBACK_DELETE_COMPLETION_FLAGS = UInt32
CF_CALLBACK_DELETE_COMPLETION_FLAG_NONE: CF_CALLBACK_DELETE_COMPLETION_FLAGS = 0
CF_CALLBACK_DELETE_FLAGS = UInt32
CF_CALLBACK_DELETE_FLAG_NONE: CF_CALLBACK_DELETE_FLAGS = 0
CF_CALLBACK_DELETE_FLAG_IS_DIRECTORY: CF_CALLBACK_DELETE_FLAGS = 1
CF_CALLBACK_DELETE_FLAG_IS_UNDELETE: CF_CALLBACK_DELETE_FLAGS = 2
CF_CALLBACK_FETCH_DATA_FLAGS = UInt32
CF_CALLBACK_FETCH_DATA_FLAG_NONE: CF_CALLBACK_FETCH_DATA_FLAGS = 0
CF_CALLBACK_FETCH_DATA_FLAG_RECOVERY: CF_CALLBACK_FETCH_DATA_FLAGS = 1
CF_CALLBACK_FETCH_DATA_FLAG_EXPLICIT_HYDRATION: CF_CALLBACK_FETCH_DATA_FLAGS = 2
CF_CALLBACK_FETCH_PLACEHOLDERS_FLAGS = UInt32
CF_CALLBACK_FETCH_PLACEHOLDERS_FLAG_NONE: CF_CALLBACK_FETCH_PLACEHOLDERS_FLAGS = 0
class CF_CALLBACK_INFO(Structure):
    StructSize: UInt32
    ConnectionKey: win32more.Storage.CloudFilters.CF_CONNECTION_KEY
    CallbackContext: c_void_p
    VolumeGuidName: win32more.Foundation.PWSTR
    VolumeDosName: win32more.Foundation.PWSTR
    VolumeSerialNumber: UInt32
    SyncRootFileId: win32more.Foundation.LARGE_INTEGER
    SyncRootIdentity: c_void_p
    SyncRootIdentityLength: UInt32
    FileId: win32more.Foundation.LARGE_INTEGER
    FileSize: win32more.Foundation.LARGE_INTEGER
    FileIdentity: c_void_p
    FileIdentityLength: UInt32
    NormalizedPath: win32more.Foundation.PWSTR
    TransferKey: win32more.Foundation.LARGE_INTEGER
    PriorityHint: Byte
    CorrelationVector: POINTER(win32more.System.CorrelationVector.CORRELATION_VECTOR_head)
    ProcessInfo: POINTER(win32more.Storage.CloudFilters.CF_PROCESS_INFO_head)
    RequestKey: win32more.Foundation.LARGE_INTEGER
CF_CALLBACK_OPEN_COMPLETION_FLAGS = UInt32
CF_CALLBACK_OPEN_COMPLETION_FLAG_NONE: CF_CALLBACK_OPEN_COMPLETION_FLAGS = 0
CF_CALLBACK_OPEN_COMPLETION_FLAG_PLACEHOLDER_UNKNOWN: CF_CALLBACK_OPEN_COMPLETION_FLAGS = 1
CF_CALLBACK_OPEN_COMPLETION_FLAG_PLACEHOLDER_UNSUPPORTED: CF_CALLBACK_OPEN_COMPLETION_FLAGS = 2
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
            Flags: win32more.Storage.CloudFilters.CF_CALLBACK_CANCEL_FLAGS
            Anonymous: _Anonymous_e__Union
            class _Anonymous_e__Union(Union):
                FetchData: _FetchData_e__Struct
                class _FetchData_e__Struct(Structure):
                    FileOffset: win32more.Foundation.LARGE_INTEGER
                    Length: win32more.Foundation.LARGE_INTEGER
        class _FetchData_e__Struct(Structure):
            Flags: win32more.Storage.CloudFilters.CF_CALLBACK_FETCH_DATA_FLAGS
            RequiredFileOffset: win32more.Foundation.LARGE_INTEGER
            RequiredLength: win32more.Foundation.LARGE_INTEGER
            OptionalFileOffset: win32more.Foundation.LARGE_INTEGER
            OptionalLength: win32more.Foundation.LARGE_INTEGER
            LastDehydrationTime: win32more.Foundation.LARGE_INTEGER
            LastDehydrationReason: win32more.Storage.CloudFilters.CF_CALLBACK_DEHYDRATION_REASON
        class _ValidateData_e__Struct(Structure):
            Flags: win32more.Storage.CloudFilters.CF_CALLBACK_VALIDATE_DATA_FLAGS
            RequiredFileOffset: win32more.Foundation.LARGE_INTEGER
            RequiredLength: win32more.Foundation.LARGE_INTEGER
        class _FetchPlaceholders_e__Struct(Structure):
            Flags: win32more.Storage.CloudFilters.CF_CALLBACK_FETCH_PLACEHOLDERS_FLAGS
            Pattern: win32more.Foundation.PWSTR
        class _OpenCompletion_e__Struct(Structure):
            Flags: win32more.Storage.CloudFilters.CF_CALLBACK_OPEN_COMPLETION_FLAGS
        class _CloseCompletion_e__Struct(Structure):
            Flags: win32more.Storage.CloudFilters.CF_CALLBACK_CLOSE_COMPLETION_FLAGS
        class _Dehydrate_e__Struct(Structure):
            Flags: win32more.Storage.CloudFilters.CF_CALLBACK_DEHYDRATE_FLAGS
            Reason: win32more.Storage.CloudFilters.CF_CALLBACK_DEHYDRATION_REASON
        class _DehydrateCompletion_e__Struct(Structure):
            Flags: win32more.Storage.CloudFilters.CF_CALLBACK_DEHYDRATE_COMPLETION_FLAGS
            Reason: win32more.Storage.CloudFilters.CF_CALLBACK_DEHYDRATION_REASON
        class _Delete_e__Struct(Structure):
            Flags: win32more.Storage.CloudFilters.CF_CALLBACK_DELETE_FLAGS
        class _DeleteCompletion_e__Struct(Structure):
            Flags: win32more.Storage.CloudFilters.CF_CALLBACK_DELETE_COMPLETION_FLAGS
        class _Rename_e__Struct(Structure):
            Flags: win32more.Storage.CloudFilters.CF_CALLBACK_RENAME_FLAGS
            TargetPath: win32more.Foundation.PWSTR
        class _RenameCompletion_e__Struct(Structure):
            Flags: win32more.Storage.CloudFilters.CF_CALLBACK_RENAME_COMPLETION_FLAGS
            SourcePath: win32more.Foundation.PWSTR
class CF_CALLBACK_REGISTRATION(Structure):
    Type: win32more.Storage.CloudFilters.CF_CALLBACK_TYPE
    Callback: win32more.Storage.CloudFilters.CF_CALLBACK
CF_CALLBACK_RENAME_COMPLETION_FLAGS = UInt32
CF_CALLBACK_RENAME_COMPLETION_FLAG_NONE: CF_CALLBACK_RENAME_COMPLETION_FLAGS = 0
CF_CALLBACK_RENAME_FLAGS = UInt32
CF_CALLBACK_RENAME_FLAG_NONE: CF_CALLBACK_RENAME_FLAGS = 0
CF_CALLBACK_RENAME_FLAG_IS_DIRECTORY: CF_CALLBACK_RENAME_FLAGS = 1
CF_CALLBACK_RENAME_FLAG_SOURCE_IN_SCOPE: CF_CALLBACK_RENAME_FLAGS = 2
CF_CALLBACK_RENAME_FLAG_TARGET_IN_SCOPE: CF_CALLBACK_RENAME_FLAGS = 4
CF_CALLBACK_TYPE = Int32
CF_CALLBACK_TYPE_FETCH_DATA: CF_CALLBACK_TYPE = 0
CF_CALLBACK_TYPE_VALIDATE_DATA: CF_CALLBACK_TYPE = 1
CF_CALLBACK_TYPE_CANCEL_FETCH_DATA: CF_CALLBACK_TYPE = 2
CF_CALLBACK_TYPE_FETCH_PLACEHOLDERS: CF_CALLBACK_TYPE = 3
CF_CALLBACK_TYPE_CANCEL_FETCH_PLACEHOLDERS: CF_CALLBACK_TYPE = 4
CF_CALLBACK_TYPE_NOTIFY_FILE_OPEN_COMPLETION: CF_CALLBACK_TYPE = 5
CF_CALLBACK_TYPE_NOTIFY_FILE_CLOSE_COMPLETION: CF_CALLBACK_TYPE = 6
CF_CALLBACK_TYPE_NOTIFY_DEHYDRATE: CF_CALLBACK_TYPE = 7
CF_CALLBACK_TYPE_NOTIFY_DEHYDRATE_COMPLETION: CF_CALLBACK_TYPE = 8
CF_CALLBACK_TYPE_NOTIFY_DELETE: CF_CALLBACK_TYPE = 9
CF_CALLBACK_TYPE_NOTIFY_DELETE_COMPLETION: CF_CALLBACK_TYPE = 10
CF_CALLBACK_TYPE_NOTIFY_RENAME: CF_CALLBACK_TYPE = 11
CF_CALLBACK_TYPE_NOTIFY_RENAME_COMPLETION: CF_CALLBACK_TYPE = 12
CF_CALLBACK_TYPE_NONE: CF_CALLBACK_TYPE = -1
CF_CALLBACK_VALIDATE_DATA_FLAGS = UInt32
CF_CALLBACK_VALIDATE_DATA_FLAG_NONE: CF_CALLBACK_VALIDATE_DATA_FLAGS = 0
CF_CALLBACK_VALIDATE_DATA_FLAG_EXPLICIT_HYDRATION: CF_CALLBACK_VALIDATE_DATA_FLAGS = 2
CF_CONNECTION_KEY = Int64
CF_CONNECT_FLAGS = UInt32
CF_CONNECT_FLAG_NONE: CF_CONNECT_FLAGS = 0
CF_CONNECT_FLAG_REQUIRE_PROCESS_INFO: CF_CONNECT_FLAGS = 2
CF_CONNECT_FLAG_REQUIRE_FULL_FILE_PATH: CF_CONNECT_FLAGS = 4
CF_CONNECT_FLAG_BLOCK_SELF_IMPLICIT_HYDRATION: CF_CONNECT_FLAGS = 8
CF_CONVERT_FLAGS = UInt32
CF_CONVERT_FLAG_NONE: CF_CONVERT_FLAGS = 0
CF_CONVERT_FLAG_MARK_IN_SYNC: CF_CONVERT_FLAGS = 1
CF_CONVERT_FLAG_DEHYDRATE: CF_CONVERT_FLAGS = 2
CF_CONVERT_FLAG_ENABLE_ON_DEMAND_POPULATION: CF_CONVERT_FLAGS = 4
CF_CONVERT_FLAG_ALWAYS_FULL: CF_CONVERT_FLAGS = 8
CF_CONVERT_FLAG_FORCE_CONVERT_TO_CLOUD_FILE: CF_CONVERT_FLAGS = 16
CF_CREATE_FLAGS = UInt32
CF_CREATE_FLAG_NONE: CF_CREATE_FLAGS = 0
CF_CREATE_FLAG_STOP_ON_ERROR: CF_CREATE_FLAGS = 1
CF_DEHYDRATE_FLAGS = UInt32
CF_DEHYDRATE_FLAG_NONE: CF_DEHYDRATE_FLAGS = 0
CF_DEHYDRATE_FLAG_BACKGROUND: CF_DEHYDRATE_FLAGS = 1
class CF_FILE_RANGE(Structure):
    StartingOffset: win32more.Foundation.LARGE_INTEGER
    Length: win32more.Foundation.LARGE_INTEGER
class CF_FS_METADATA(Structure):
    BasicInfo: win32more.Storage.FileSystem.FILE_BASIC_INFO
    FileSize: win32more.Foundation.LARGE_INTEGER
CF_HARDLINK_POLICY = UInt32
CF_HARDLINK_POLICY_NONE: CF_HARDLINK_POLICY = 0
CF_HARDLINK_POLICY_ALLOWED: CF_HARDLINK_POLICY = 1
CF_HYDRATE_FLAGS = UInt32
CF_HYDRATE_FLAG_NONE: CF_HYDRATE_FLAGS = 0
class CF_HYDRATION_POLICY(Structure):
    Primary: win32more.Storage.CloudFilters.CF_HYDRATION_POLICY_PRIMARY_USHORT
    Modifier: win32more.Storage.CloudFilters.CF_HYDRATION_POLICY_MODIFIER_USHORT
CF_HYDRATION_POLICY_MODIFIER = UInt16
CF_HYDRATION_POLICY_MODIFIER_NONE: CF_HYDRATION_POLICY_MODIFIER = 0
CF_HYDRATION_POLICY_MODIFIER_VALIDATION_REQUIRED: CF_HYDRATION_POLICY_MODIFIER = 1
CF_HYDRATION_POLICY_MODIFIER_STREAMING_ALLOWED: CF_HYDRATION_POLICY_MODIFIER = 2
CF_HYDRATION_POLICY_MODIFIER_AUTO_DEHYDRATION_ALLOWED: CF_HYDRATION_POLICY_MODIFIER = 4
CF_HYDRATION_POLICY_MODIFIER_ALLOW_FULL_RESTART_HYDRATION: CF_HYDRATION_POLICY_MODIFIER = 8
class CF_HYDRATION_POLICY_MODIFIER_USHORT(Structure):
    us: UInt16
CF_HYDRATION_POLICY_PRIMARY = UInt16
CF_HYDRATION_POLICY_PARTIAL: CF_HYDRATION_POLICY_PRIMARY = 0
CF_HYDRATION_POLICY_PROGRESSIVE: CF_HYDRATION_POLICY_PRIMARY = 1
CF_HYDRATION_POLICY_FULL: CF_HYDRATION_POLICY_PRIMARY = 2
CF_HYDRATION_POLICY_ALWAYS_FULL: CF_HYDRATION_POLICY_PRIMARY = 3
class CF_HYDRATION_POLICY_PRIMARY_USHORT(Structure):
    us: UInt16
CF_INSYNC_POLICY = UInt32
CF_INSYNC_POLICY_NONE: CF_INSYNC_POLICY = 0
CF_INSYNC_POLICY_TRACK_FILE_CREATION_TIME: CF_INSYNC_POLICY = 1
CF_INSYNC_POLICY_TRACK_FILE_READONLY_ATTRIBUTE: CF_INSYNC_POLICY = 2
CF_INSYNC_POLICY_TRACK_FILE_HIDDEN_ATTRIBUTE: CF_INSYNC_POLICY = 4
CF_INSYNC_POLICY_TRACK_FILE_SYSTEM_ATTRIBUTE: CF_INSYNC_POLICY = 8
CF_INSYNC_POLICY_TRACK_DIRECTORY_CREATION_TIME: CF_INSYNC_POLICY = 16
CF_INSYNC_POLICY_TRACK_DIRECTORY_READONLY_ATTRIBUTE: CF_INSYNC_POLICY = 32
CF_INSYNC_POLICY_TRACK_DIRECTORY_HIDDEN_ATTRIBUTE: CF_INSYNC_POLICY = 64
CF_INSYNC_POLICY_TRACK_DIRECTORY_SYSTEM_ATTRIBUTE: CF_INSYNC_POLICY = 128
CF_INSYNC_POLICY_TRACK_FILE_LAST_WRITE_TIME: CF_INSYNC_POLICY = 256
CF_INSYNC_POLICY_TRACK_DIRECTORY_LAST_WRITE_TIME: CF_INSYNC_POLICY = 512
CF_INSYNC_POLICY_TRACK_FILE_ALL: CF_INSYNC_POLICY = 5592335
CF_INSYNC_POLICY_TRACK_DIRECTORY_ALL: CF_INSYNC_POLICY = 11184880
CF_INSYNC_POLICY_TRACK_ALL: CF_INSYNC_POLICY = 16777215
CF_INSYNC_POLICY_PRESERVE_INSYNC_FOR_SYNC_ENGINE: CF_INSYNC_POLICY = 2147483648
CF_IN_SYNC_STATE = Int32
CF_IN_SYNC_STATE_NOT_IN_SYNC: CF_IN_SYNC_STATE = 0
CF_IN_SYNC_STATE_IN_SYNC: CF_IN_SYNC_STATE = 1
CF_OPEN_FILE_FLAGS = UInt32
CF_OPEN_FILE_FLAG_NONE: CF_OPEN_FILE_FLAGS = 0
CF_OPEN_FILE_FLAG_EXCLUSIVE: CF_OPEN_FILE_FLAGS = 1
CF_OPEN_FILE_FLAG_WRITE_ACCESS: CF_OPEN_FILE_FLAGS = 2
CF_OPEN_FILE_FLAG_DELETE_ACCESS: CF_OPEN_FILE_FLAGS = 4
CF_OPEN_FILE_FLAG_FOREGROUND: CF_OPEN_FILE_FLAGS = 8
CF_OPERATION_ACK_DATA_FLAGS = UInt32
CF_OPERATION_ACK_DATA_FLAG_NONE: CF_OPERATION_ACK_DATA_FLAGS = 0
CF_OPERATION_ACK_DEHYDRATE_FLAGS = UInt32
CF_OPERATION_ACK_DEHYDRATE_FLAG_NONE: CF_OPERATION_ACK_DEHYDRATE_FLAGS = 0
CF_OPERATION_ACK_DELETE_FLAGS = UInt32
CF_OPERATION_ACK_DELETE_FLAG_NONE: CF_OPERATION_ACK_DELETE_FLAGS = 0
CF_OPERATION_ACK_RENAME_FLAGS = UInt32
CF_OPERATION_ACK_RENAME_FLAG_NONE: CF_OPERATION_ACK_RENAME_FLAGS = 0
class CF_OPERATION_INFO(Structure):
    StructSize: UInt32
    Type: win32more.Storage.CloudFilters.CF_OPERATION_TYPE
    ConnectionKey: win32more.Storage.CloudFilters.CF_CONNECTION_KEY
    TransferKey: win32more.Foundation.LARGE_INTEGER
    CorrelationVector: POINTER(win32more.System.CorrelationVector.CORRELATION_VECTOR_head)
    SyncStatus: POINTER(win32more.Storage.CloudFilters.CF_SYNC_STATUS_head)
    RequestKey: win32more.Foundation.LARGE_INTEGER
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
            Flags: win32more.Storage.CloudFilters.CF_OPERATION_TRANSFER_DATA_FLAGS
            CompletionStatus: win32more.Foundation.NTSTATUS
            Buffer: c_void_p
            Offset: win32more.Foundation.LARGE_INTEGER
            Length: win32more.Foundation.LARGE_INTEGER
        class _RetrieveData_e__Struct(Structure):
            Flags: win32more.Storage.CloudFilters.CF_OPERATION_RETRIEVE_DATA_FLAGS
            Buffer: c_void_p
            Offset: win32more.Foundation.LARGE_INTEGER
            Length: win32more.Foundation.LARGE_INTEGER
            ReturnedLength: win32more.Foundation.LARGE_INTEGER
        class _AckData_e__Struct(Structure):
            Flags: win32more.Storage.CloudFilters.CF_OPERATION_ACK_DATA_FLAGS
            CompletionStatus: win32more.Foundation.NTSTATUS
            Offset: win32more.Foundation.LARGE_INTEGER
            Length: win32more.Foundation.LARGE_INTEGER
        class _RestartHydration_e__Struct(Structure):
            Flags: win32more.Storage.CloudFilters.CF_OPERATION_RESTART_HYDRATION_FLAGS
            FsMetadata: POINTER(win32more.Storage.CloudFilters.CF_FS_METADATA_head)
            FileIdentity: c_void_p
            FileIdentityLength: UInt32
        class _TransferPlaceholders_e__Struct(Structure):
            Flags: win32more.Storage.CloudFilters.CF_OPERATION_TRANSFER_PLACEHOLDERS_FLAGS
            CompletionStatus: win32more.Foundation.NTSTATUS
            PlaceholderTotalCount: win32more.Foundation.LARGE_INTEGER
            PlaceholderArray: POINTER(win32more.Storage.CloudFilters.CF_PLACEHOLDER_CREATE_INFO_head)
            PlaceholderCount: UInt32
            EntriesProcessed: UInt32
        class _AckDehydrate_e__Struct(Structure):
            Flags: win32more.Storage.CloudFilters.CF_OPERATION_ACK_DEHYDRATE_FLAGS
            CompletionStatus: win32more.Foundation.NTSTATUS
            FileIdentity: c_void_p
            FileIdentityLength: UInt32
        class _AckRename_e__Struct(Structure):
            Flags: win32more.Storage.CloudFilters.CF_OPERATION_ACK_RENAME_FLAGS
            CompletionStatus: win32more.Foundation.NTSTATUS
        class _AckDelete_e__Struct(Structure):
            Flags: win32more.Storage.CloudFilters.CF_OPERATION_ACK_DELETE_FLAGS
            CompletionStatus: win32more.Foundation.NTSTATUS
CF_OPERATION_RESTART_HYDRATION_FLAGS = UInt32
CF_OPERATION_RESTART_HYDRATION_FLAG_NONE: CF_OPERATION_RESTART_HYDRATION_FLAGS = 0
CF_OPERATION_RESTART_HYDRATION_FLAG_MARK_IN_SYNC: CF_OPERATION_RESTART_HYDRATION_FLAGS = 1
CF_OPERATION_RETRIEVE_DATA_FLAGS = UInt32
CF_OPERATION_RETRIEVE_DATA_FLAG_NONE: CF_OPERATION_RETRIEVE_DATA_FLAGS = 0
CF_OPERATION_TRANSFER_DATA_FLAGS = UInt32
CF_OPERATION_TRANSFER_DATA_FLAG_NONE: CF_OPERATION_TRANSFER_DATA_FLAGS = 0
CF_OPERATION_TRANSFER_PLACEHOLDERS_FLAGS = UInt32
CF_OPERATION_TRANSFER_PLACEHOLDERS_FLAG_NONE: CF_OPERATION_TRANSFER_PLACEHOLDERS_FLAGS = 0
CF_OPERATION_TRANSFER_PLACEHOLDERS_FLAG_STOP_ON_ERROR: CF_OPERATION_TRANSFER_PLACEHOLDERS_FLAGS = 1
CF_OPERATION_TRANSFER_PLACEHOLDERS_FLAG_DISABLE_ON_DEMAND_POPULATION: CF_OPERATION_TRANSFER_PLACEHOLDERS_FLAGS = 2
CF_OPERATION_TYPE = Int32
CF_OPERATION_TYPE_TRANSFER_DATA: CF_OPERATION_TYPE = 0
CF_OPERATION_TYPE_RETRIEVE_DATA: CF_OPERATION_TYPE = 1
CF_OPERATION_TYPE_ACK_DATA: CF_OPERATION_TYPE = 2
CF_OPERATION_TYPE_RESTART_HYDRATION: CF_OPERATION_TYPE = 3
CF_OPERATION_TYPE_TRANSFER_PLACEHOLDERS: CF_OPERATION_TYPE = 4
CF_OPERATION_TYPE_ACK_DEHYDRATE: CF_OPERATION_TYPE = 5
CF_OPERATION_TYPE_ACK_DELETE: CF_OPERATION_TYPE = 6
CF_OPERATION_TYPE_ACK_RENAME: CF_OPERATION_TYPE = 7
CF_PIN_STATE = Int32
CF_PIN_STATE_UNSPECIFIED: CF_PIN_STATE = 0
CF_PIN_STATE_PINNED: CF_PIN_STATE = 1
CF_PIN_STATE_UNPINNED: CF_PIN_STATE = 2
CF_PIN_STATE_EXCLUDED: CF_PIN_STATE = 3
CF_PIN_STATE_INHERIT: CF_PIN_STATE = 4
class CF_PLACEHOLDER_BASIC_INFO(Structure):
    PinState: win32more.Storage.CloudFilters.CF_PIN_STATE
    InSyncState: win32more.Storage.CloudFilters.CF_IN_SYNC_STATE
    FileId: win32more.Foundation.LARGE_INTEGER
    SyncRootFileId: win32more.Foundation.LARGE_INTEGER
    FileIdentityLength: UInt32
    FileIdentity: Byte * 1
CF_PLACEHOLDER_CREATE_FLAGS = UInt32
CF_PLACEHOLDER_CREATE_FLAG_NONE: CF_PLACEHOLDER_CREATE_FLAGS = 0
CF_PLACEHOLDER_CREATE_FLAG_DISABLE_ON_DEMAND_POPULATION: CF_PLACEHOLDER_CREATE_FLAGS = 1
CF_PLACEHOLDER_CREATE_FLAG_MARK_IN_SYNC: CF_PLACEHOLDER_CREATE_FLAGS = 2
CF_PLACEHOLDER_CREATE_FLAG_SUPERSEDE: CF_PLACEHOLDER_CREATE_FLAGS = 4
CF_PLACEHOLDER_CREATE_FLAG_ALWAYS_FULL: CF_PLACEHOLDER_CREATE_FLAGS = 8
class CF_PLACEHOLDER_CREATE_INFO(Structure):
    RelativeFileName: win32more.Foundation.PWSTR
    FsMetadata: win32more.Storage.CloudFilters.CF_FS_METADATA
    FileIdentity: c_void_p
    FileIdentityLength: UInt32
    Flags: win32more.Storage.CloudFilters.CF_PLACEHOLDER_CREATE_FLAGS
    Result: win32more.Foundation.HRESULT
    CreateUsn: Int64
CF_PLACEHOLDER_INFO_CLASS = Int32
CF_PLACEHOLDER_INFO_BASIC: CF_PLACEHOLDER_INFO_CLASS = 0
CF_PLACEHOLDER_INFO_STANDARD: CF_PLACEHOLDER_INFO_CLASS = 1
CF_PLACEHOLDER_MANAGEMENT_POLICY = Int32
CF_PLACEHOLDER_MANAGEMENT_POLICY_DEFAULT: CF_PLACEHOLDER_MANAGEMENT_POLICY = 0
CF_PLACEHOLDER_MANAGEMENT_POLICY_CREATE_UNRESTRICTED: CF_PLACEHOLDER_MANAGEMENT_POLICY = 1
CF_PLACEHOLDER_MANAGEMENT_POLICY_CONVERT_TO_UNRESTRICTED: CF_PLACEHOLDER_MANAGEMENT_POLICY = 2
CF_PLACEHOLDER_MANAGEMENT_POLICY_UPDATE_UNRESTRICTED: CF_PLACEHOLDER_MANAGEMENT_POLICY = 4
CF_PLACEHOLDER_RANGE_INFO_CLASS = Int32
CF_PLACEHOLDER_RANGE_INFO_ONDISK: CF_PLACEHOLDER_RANGE_INFO_CLASS = 1
CF_PLACEHOLDER_RANGE_INFO_VALIDATED: CF_PLACEHOLDER_RANGE_INFO_CLASS = 2
CF_PLACEHOLDER_RANGE_INFO_MODIFIED: CF_PLACEHOLDER_RANGE_INFO_CLASS = 3
class CF_PLACEHOLDER_STANDARD_INFO(Structure):
    OnDiskDataSize: win32more.Foundation.LARGE_INTEGER
    ValidatedDataSize: win32more.Foundation.LARGE_INTEGER
    ModifiedDataSize: win32more.Foundation.LARGE_INTEGER
    PropertiesSize: win32more.Foundation.LARGE_INTEGER
    PinState: win32more.Storage.CloudFilters.CF_PIN_STATE
    InSyncState: win32more.Storage.CloudFilters.CF_IN_SYNC_STATE
    FileId: win32more.Foundation.LARGE_INTEGER
    SyncRootFileId: win32more.Foundation.LARGE_INTEGER
    FileIdentityLength: UInt32
    FileIdentity: Byte * 1
CF_PLACEHOLDER_STATE = UInt32
CF_PLACEHOLDER_STATE_NO_STATES: CF_PLACEHOLDER_STATE = 0
CF_PLACEHOLDER_STATE_PLACEHOLDER: CF_PLACEHOLDER_STATE = 1
CF_PLACEHOLDER_STATE_SYNC_ROOT: CF_PLACEHOLDER_STATE = 2
CF_PLACEHOLDER_STATE_ESSENTIAL_PROP_PRESENT: CF_PLACEHOLDER_STATE = 4
CF_PLACEHOLDER_STATE_IN_SYNC: CF_PLACEHOLDER_STATE = 8
CF_PLACEHOLDER_STATE_PARTIAL: CF_PLACEHOLDER_STATE = 16
CF_PLACEHOLDER_STATE_PARTIALLY_ON_DISK: CF_PLACEHOLDER_STATE = 32
CF_PLACEHOLDER_STATE_INVALID: CF_PLACEHOLDER_STATE = 4294967295
class CF_PLATFORM_INFO(Structure):
    BuildNumber: UInt32
    RevisionNumber: UInt32
    IntegrationNumber: UInt32
class CF_POPULATION_POLICY(Structure):
    Primary: win32more.Storage.CloudFilters.CF_POPULATION_POLICY_PRIMARY_USHORT
    Modifier: win32more.Storage.CloudFilters.CF_POPULATION_POLICY_MODIFIER_USHORT
CF_POPULATION_POLICY_MODIFIER = UInt16
CF_POPULATION_POLICY_MODIFIER_NONE: CF_POPULATION_POLICY_MODIFIER = 0
class CF_POPULATION_POLICY_MODIFIER_USHORT(Structure):
    us: UInt16
CF_POPULATION_POLICY_PRIMARY = UInt16
CF_POPULATION_POLICY_PARTIAL: CF_POPULATION_POLICY_PRIMARY = 0
CF_POPULATION_POLICY_FULL: CF_POPULATION_POLICY_PRIMARY = 2
CF_POPULATION_POLICY_ALWAYS_FULL: CF_POPULATION_POLICY_PRIMARY = 3
class CF_POPULATION_POLICY_PRIMARY_USHORT(Structure):
    us: UInt16
class CF_PROCESS_INFO(Structure):
    StructSize: UInt32
    ProcessId: UInt32
    ImagePath: win32more.Foundation.PWSTR
    PackageName: win32more.Foundation.PWSTR
    ApplicationId: win32more.Foundation.PWSTR
    CommandLine: win32more.Foundation.PWSTR
    SessionId: UInt32
CF_REGISTER_FLAGS = UInt32
CF_REGISTER_FLAG_NONE: CF_REGISTER_FLAGS = 0
CF_REGISTER_FLAG_UPDATE: CF_REGISTER_FLAGS = 1
CF_REGISTER_FLAG_DISABLE_ON_DEMAND_POPULATION_ON_ROOT: CF_REGISTER_FLAGS = 2
CF_REGISTER_FLAG_MARK_IN_SYNC_ON_ROOT: CF_REGISTER_FLAGS = 4
CF_REVERT_FLAGS = UInt32
CF_REVERT_FLAG_NONE: CF_REVERT_FLAGS = 0
CF_SET_IN_SYNC_FLAGS = UInt32
CF_SET_IN_SYNC_FLAG_NONE: CF_SET_IN_SYNC_FLAGS = 0
CF_SET_PIN_FLAGS = UInt32
CF_SET_PIN_FLAG_NONE: CF_SET_PIN_FLAGS = 0
CF_SET_PIN_FLAG_RECURSE: CF_SET_PIN_FLAGS = 1
CF_SET_PIN_FLAG_RECURSE_ONLY: CF_SET_PIN_FLAGS = 2
CF_SET_PIN_FLAG_RECURSE_STOP_ON_ERROR: CF_SET_PIN_FLAGS = 4
class CF_SYNC_POLICIES(Structure):
    StructSize: UInt32
    Hydration: win32more.Storage.CloudFilters.CF_HYDRATION_POLICY
    Population: win32more.Storage.CloudFilters.CF_POPULATION_POLICY
    InSync: win32more.Storage.CloudFilters.CF_INSYNC_POLICY
    HardLink: win32more.Storage.CloudFilters.CF_HARDLINK_POLICY
    PlaceholderManagement: win32more.Storage.CloudFilters.CF_PLACEHOLDER_MANAGEMENT_POLICY
CF_SYNC_PROVIDER_STATUS = UInt32
CF_PROVIDER_STATUS_DISCONNECTED: CF_SYNC_PROVIDER_STATUS = 0
CF_PROVIDER_STATUS_IDLE: CF_SYNC_PROVIDER_STATUS = 1
CF_PROVIDER_STATUS_POPULATE_NAMESPACE: CF_SYNC_PROVIDER_STATUS = 2
CF_PROVIDER_STATUS_POPULATE_METADATA: CF_SYNC_PROVIDER_STATUS = 4
CF_PROVIDER_STATUS_POPULATE_CONTENT: CF_SYNC_PROVIDER_STATUS = 8
CF_PROVIDER_STATUS_SYNC_INCREMENTAL: CF_SYNC_PROVIDER_STATUS = 16
CF_PROVIDER_STATUS_SYNC_FULL: CF_SYNC_PROVIDER_STATUS = 32
CF_PROVIDER_STATUS_CONNECTIVITY_LOST: CF_SYNC_PROVIDER_STATUS = 64
CF_PROVIDER_STATUS_CLEAR_FLAGS: CF_SYNC_PROVIDER_STATUS = 2147483648
CF_PROVIDER_STATUS_TERMINATED: CF_SYNC_PROVIDER_STATUS = 3221225473
CF_PROVIDER_STATUS_ERROR: CF_SYNC_PROVIDER_STATUS = 3221225474
class CF_SYNC_REGISTRATION(Structure):
    StructSize: UInt32
    ProviderName: win32more.Foundation.PWSTR
    ProviderVersion: win32more.Foundation.PWSTR
    SyncRootIdentity: c_void_p
    SyncRootIdentityLength: UInt32
    FileIdentity: c_void_p
    FileIdentityLength: UInt32
    ProviderId: Guid
class CF_SYNC_ROOT_BASIC_INFO(Structure):
    SyncRootFileId: win32more.Foundation.LARGE_INTEGER
CF_SYNC_ROOT_INFO_CLASS = Int32
CF_SYNC_ROOT_INFO_BASIC: CF_SYNC_ROOT_INFO_CLASS = 0
CF_SYNC_ROOT_INFO_STANDARD: CF_SYNC_ROOT_INFO_CLASS = 1
CF_SYNC_ROOT_INFO_PROVIDER: CF_SYNC_ROOT_INFO_CLASS = 2
class CF_SYNC_ROOT_PROVIDER_INFO(Structure):
    ProviderStatus: win32more.Storage.CloudFilters.CF_SYNC_PROVIDER_STATUS
    ProviderName: Char * 256
    ProviderVersion: Char * 256
class CF_SYNC_ROOT_STANDARD_INFO(Structure):
    SyncRootFileId: win32more.Foundation.LARGE_INTEGER
    HydrationPolicy: win32more.Storage.CloudFilters.CF_HYDRATION_POLICY
    PopulationPolicy: win32more.Storage.CloudFilters.CF_POPULATION_POLICY
    InSyncPolicy: win32more.Storage.CloudFilters.CF_INSYNC_POLICY
    HardLinkPolicy: win32more.Storage.CloudFilters.CF_HARDLINK_POLICY
    ProviderStatus: win32more.Storage.CloudFilters.CF_SYNC_PROVIDER_STATUS
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
CF_UPDATE_FLAGS = UInt32
CF_UPDATE_FLAG_NONE: CF_UPDATE_FLAGS = 0
CF_UPDATE_FLAG_VERIFY_IN_SYNC: CF_UPDATE_FLAGS = 1
CF_UPDATE_FLAG_MARK_IN_SYNC: CF_UPDATE_FLAGS = 2
CF_UPDATE_FLAG_DEHYDRATE: CF_UPDATE_FLAGS = 4
CF_UPDATE_FLAG_ENABLE_ON_DEMAND_POPULATION: CF_UPDATE_FLAGS = 8
CF_UPDATE_FLAG_DISABLE_ON_DEMAND_POPULATION: CF_UPDATE_FLAGS = 16
CF_UPDATE_FLAG_REMOVE_FILE_IDENTITY: CF_UPDATE_FLAGS = 32
CF_UPDATE_FLAG_CLEAR_IN_SYNC: CF_UPDATE_FLAGS = 64
CF_UPDATE_FLAG_REMOVE_PROPERTY: CF_UPDATE_FLAGS = 128
CF_UPDATE_FLAG_PASSTHROUGH_FS_METADATA: CF_UPDATE_FLAGS = 256
CF_UPDATE_FLAG_ALWAYS_FULL: CF_UPDATE_FLAGS = 512
CF_UPDATE_FLAG_ALLOW_PARTIAL: CF_UPDATE_FLAGS = 1024
make_head(_module, 'CF_CALLBACK')
make_head(_module, 'CF_CALLBACK_INFO')
make_head(_module, 'CF_CALLBACK_PARAMETERS')
make_head(_module, 'CF_CALLBACK_REGISTRATION')
make_head(_module, 'CF_FILE_RANGE')
make_head(_module, 'CF_FS_METADATA')
make_head(_module, 'CF_HYDRATION_POLICY')
make_head(_module, 'CF_HYDRATION_POLICY_MODIFIER_USHORT')
make_head(_module, 'CF_HYDRATION_POLICY_PRIMARY_USHORT')
make_head(_module, 'CF_OPERATION_INFO')
make_head(_module, 'CF_OPERATION_PARAMETERS')
make_head(_module, 'CF_PLACEHOLDER_BASIC_INFO')
make_head(_module, 'CF_PLACEHOLDER_CREATE_INFO')
make_head(_module, 'CF_PLACEHOLDER_STANDARD_INFO')
make_head(_module, 'CF_PLATFORM_INFO')
make_head(_module, 'CF_POPULATION_POLICY')
make_head(_module, 'CF_POPULATION_POLICY_MODIFIER_USHORT')
make_head(_module, 'CF_POPULATION_POLICY_PRIMARY_USHORT')
make_head(_module, 'CF_PROCESS_INFO')
make_head(_module, 'CF_SYNC_POLICIES')
make_head(_module, 'CF_SYNC_REGISTRATION')
make_head(_module, 'CF_SYNC_ROOT_BASIC_INFO')
make_head(_module, 'CF_SYNC_ROOT_PROVIDER_INFO')
make_head(_module, 'CF_SYNC_ROOT_STANDARD_INFO')
make_head(_module, 'CF_SYNC_STATUS')
__all__ = [
    "CF_CALLBACK",
    "CF_CALLBACK_CANCEL_FLAGS",
    "CF_CALLBACK_CANCEL_FLAG_IO_ABORTED",
    "CF_CALLBACK_CANCEL_FLAG_IO_TIMEOUT",
    "CF_CALLBACK_CANCEL_FLAG_NONE",
    "CF_CALLBACK_CLOSE_COMPLETION_FLAGS",
    "CF_CALLBACK_CLOSE_COMPLETION_FLAG_DELETED",
    "CF_CALLBACK_CLOSE_COMPLETION_FLAG_NONE",
    "CF_CALLBACK_DEHYDRATE_COMPLETION_FLAGS",
    "CF_CALLBACK_DEHYDRATE_COMPLETION_FLAG_BACKGROUND",
    "CF_CALLBACK_DEHYDRATE_COMPLETION_FLAG_DEHYDRATED",
    "CF_CALLBACK_DEHYDRATE_COMPLETION_FLAG_NONE",
    "CF_CALLBACK_DEHYDRATE_FLAGS",
    "CF_CALLBACK_DEHYDRATE_FLAG_BACKGROUND",
    "CF_CALLBACK_DEHYDRATE_FLAG_NONE",
    "CF_CALLBACK_DEHYDRATION_REASON",
    "CF_CALLBACK_DEHYDRATION_REASON_NONE",
    "CF_CALLBACK_DEHYDRATION_REASON_SYSTEM_INACTIVITY",
    "CF_CALLBACK_DEHYDRATION_REASON_SYSTEM_LOW_SPACE",
    "CF_CALLBACK_DEHYDRATION_REASON_SYSTEM_OS_UPGRADE",
    "CF_CALLBACK_DEHYDRATION_REASON_USER_MANUAL",
    "CF_CALLBACK_DELETE_COMPLETION_FLAGS",
    "CF_CALLBACK_DELETE_COMPLETION_FLAG_NONE",
    "CF_CALLBACK_DELETE_FLAGS",
    "CF_CALLBACK_DELETE_FLAG_IS_DIRECTORY",
    "CF_CALLBACK_DELETE_FLAG_IS_UNDELETE",
    "CF_CALLBACK_DELETE_FLAG_NONE",
    "CF_CALLBACK_FETCH_DATA_FLAGS",
    "CF_CALLBACK_FETCH_DATA_FLAG_EXPLICIT_HYDRATION",
    "CF_CALLBACK_FETCH_DATA_FLAG_NONE",
    "CF_CALLBACK_FETCH_DATA_FLAG_RECOVERY",
    "CF_CALLBACK_FETCH_PLACEHOLDERS_FLAGS",
    "CF_CALLBACK_FETCH_PLACEHOLDERS_FLAG_NONE",
    "CF_CALLBACK_INFO",
    "CF_CALLBACK_OPEN_COMPLETION_FLAGS",
    "CF_CALLBACK_OPEN_COMPLETION_FLAG_NONE",
    "CF_CALLBACK_OPEN_COMPLETION_FLAG_PLACEHOLDER_UNKNOWN",
    "CF_CALLBACK_OPEN_COMPLETION_FLAG_PLACEHOLDER_UNSUPPORTED",
    "CF_CALLBACK_PARAMETERS",
    "CF_CALLBACK_REGISTRATION",
    "CF_CALLBACK_RENAME_COMPLETION_FLAGS",
    "CF_CALLBACK_RENAME_COMPLETION_FLAG_NONE",
    "CF_CALLBACK_RENAME_FLAGS",
    "CF_CALLBACK_RENAME_FLAG_IS_DIRECTORY",
    "CF_CALLBACK_RENAME_FLAG_NONE",
    "CF_CALLBACK_RENAME_FLAG_SOURCE_IN_SCOPE",
    "CF_CALLBACK_RENAME_FLAG_TARGET_IN_SCOPE",
    "CF_CALLBACK_TYPE",
    "CF_CALLBACK_TYPE_CANCEL_FETCH_DATA",
    "CF_CALLBACK_TYPE_CANCEL_FETCH_PLACEHOLDERS",
    "CF_CALLBACK_TYPE_FETCH_DATA",
    "CF_CALLBACK_TYPE_FETCH_PLACEHOLDERS",
    "CF_CALLBACK_TYPE_NONE",
    "CF_CALLBACK_TYPE_NOTIFY_DEHYDRATE",
    "CF_CALLBACK_TYPE_NOTIFY_DEHYDRATE_COMPLETION",
    "CF_CALLBACK_TYPE_NOTIFY_DELETE",
    "CF_CALLBACK_TYPE_NOTIFY_DELETE_COMPLETION",
    "CF_CALLBACK_TYPE_NOTIFY_FILE_CLOSE_COMPLETION",
    "CF_CALLBACK_TYPE_NOTIFY_FILE_OPEN_COMPLETION",
    "CF_CALLBACK_TYPE_NOTIFY_RENAME",
    "CF_CALLBACK_TYPE_NOTIFY_RENAME_COMPLETION",
    "CF_CALLBACK_TYPE_VALIDATE_DATA",
    "CF_CALLBACK_VALIDATE_DATA_FLAGS",
    "CF_CALLBACK_VALIDATE_DATA_FLAG_EXPLICIT_HYDRATION",
    "CF_CALLBACK_VALIDATE_DATA_FLAG_NONE",
    "CF_CONNECTION_KEY",
    "CF_CONNECT_FLAGS",
    "CF_CONNECT_FLAG_BLOCK_SELF_IMPLICIT_HYDRATION",
    "CF_CONNECT_FLAG_NONE",
    "CF_CONNECT_FLAG_REQUIRE_FULL_FILE_PATH",
    "CF_CONNECT_FLAG_REQUIRE_PROCESS_INFO",
    "CF_CONVERT_FLAGS",
    "CF_CONVERT_FLAG_ALWAYS_FULL",
    "CF_CONVERT_FLAG_DEHYDRATE",
    "CF_CONVERT_FLAG_ENABLE_ON_DEMAND_POPULATION",
    "CF_CONVERT_FLAG_FORCE_CONVERT_TO_CLOUD_FILE",
    "CF_CONVERT_FLAG_MARK_IN_SYNC",
    "CF_CONVERT_FLAG_NONE",
    "CF_CREATE_FLAGS",
    "CF_CREATE_FLAG_NONE",
    "CF_CREATE_FLAG_STOP_ON_ERROR",
    "CF_DEHYDRATE_FLAGS",
    "CF_DEHYDRATE_FLAG_BACKGROUND",
    "CF_DEHYDRATE_FLAG_NONE",
    "CF_FILE_RANGE",
    "CF_FS_METADATA",
    "CF_HARDLINK_POLICY",
    "CF_HARDLINK_POLICY_ALLOWED",
    "CF_HARDLINK_POLICY_NONE",
    "CF_HYDRATE_FLAGS",
    "CF_HYDRATE_FLAG_NONE",
    "CF_HYDRATION_POLICY",
    "CF_HYDRATION_POLICY_ALWAYS_FULL",
    "CF_HYDRATION_POLICY_FULL",
    "CF_HYDRATION_POLICY_MODIFIER",
    "CF_HYDRATION_POLICY_MODIFIER_ALLOW_FULL_RESTART_HYDRATION",
    "CF_HYDRATION_POLICY_MODIFIER_AUTO_DEHYDRATION_ALLOWED",
    "CF_HYDRATION_POLICY_MODIFIER_NONE",
    "CF_HYDRATION_POLICY_MODIFIER_STREAMING_ALLOWED",
    "CF_HYDRATION_POLICY_MODIFIER_USHORT",
    "CF_HYDRATION_POLICY_MODIFIER_VALIDATION_REQUIRED",
    "CF_HYDRATION_POLICY_PARTIAL",
    "CF_HYDRATION_POLICY_PRIMARY",
    "CF_HYDRATION_POLICY_PRIMARY_USHORT",
    "CF_HYDRATION_POLICY_PROGRESSIVE",
    "CF_INSYNC_POLICY",
    "CF_INSYNC_POLICY_NONE",
    "CF_INSYNC_POLICY_PRESERVE_INSYNC_FOR_SYNC_ENGINE",
    "CF_INSYNC_POLICY_TRACK_ALL",
    "CF_INSYNC_POLICY_TRACK_DIRECTORY_ALL",
    "CF_INSYNC_POLICY_TRACK_DIRECTORY_CREATION_TIME",
    "CF_INSYNC_POLICY_TRACK_DIRECTORY_HIDDEN_ATTRIBUTE",
    "CF_INSYNC_POLICY_TRACK_DIRECTORY_LAST_WRITE_TIME",
    "CF_INSYNC_POLICY_TRACK_DIRECTORY_READONLY_ATTRIBUTE",
    "CF_INSYNC_POLICY_TRACK_DIRECTORY_SYSTEM_ATTRIBUTE",
    "CF_INSYNC_POLICY_TRACK_FILE_ALL",
    "CF_INSYNC_POLICY_TRACK_FILE_CREATION_TIME",
    "CF_INSYNC_POLICY_TRACK_FILE_HIDDEN_ATTRIBUTE",
    "CF_INSYNC_POLICY_TRACK_FILE_LAST_WRITE_TIME",
    "CF_INSYNC_POLICY_TRACK_FILE_READONLY_ATTRIBUTE",
    "CF_INSYNC_POLICY_TRACK_FILE_SYSTEM_ATTRIBUTE",
    "CF_IN_SYNC_STATE",
    "CF_IN_SYNC_STATE_IN_SYNC",
    "CF_IN_SYNC_STATE_NOT_IN_SYNC",
    "CF_MAX_PRIORITY_HINT",
    "CF_MAX_PROVIDER_NAME_LENGTH",
    "CF_MAX_PROVIDER_VERSION_LENGTH",
    "CF_OPEN_FILE_FLAGS",
    "CF_OPEN_FILE_FLAG_DELETE_ACCESS",
    "CF_OPEN_FILE_FLAG_EXCLUSIVE",
    "CF_OPEN_FILE_FLAG_FOREGROUND",
    "CF_OPEN_FILE_FLAG_NONE",
    "CF_OPEN_FILE_FLAG_WRITE_ACCESS",
    "CF_OPERATION_ACK_DATA_FLAGS",
    "CF_OPERATION_ACK_DATA_FLAG_NONE",
    "CF_OPERATION_ACK_DEHYDRATE_FLAGS",
    "CF_OPERATION_ACK_DEHYDRATE_FLAG_NONE",
    "CF_OPERATION_ACK_DELETE_FLAGS",
    "CF_OPERATION_ACK_DELETE_FLAG_NONE",
    "CF_OPERATION_ACK_RENAME_FLAGS",
    "CF_OPERATION_ACK_RENAME_FLAG_NONE",
    "CF_OPERATION_INFO",
    "CF_OPERATION_PARAMETERS",
    "CF_OPERATION_RESTART_HYDRATION_FLAGS",
    "CF_OPERATION_RESTART_HYDRATION_FLAG_MARK_IN_SYNC",
    "CF_OPERATION_RESTART_HYDRATION_FLAG_NONE",
    "CF_OPERATION_RETRIEVE_DATA_FLAGS",
    "CF_OPERATION_RETRIEVE_DATA_FLAG_NONE",
    "CF_OPERATION_TRANSFER_DATA_FLAGS",
    "CF_OPERATION_TRANSFER_DATA_FLAG_NONE",
    "CF_OPERATION_TRANSFER_PLACEHOLDERS_FLAGS",
    "CF_OPERATION_TRANSFER_PLACEHOLDERS_FLAG_DISABLE_ON_DEMAND_POPULATION",
    "CF_OPERATION_TRANSFER_PLACEHOLDERS_FLAG_NONE",
    "CF_OPERATION_TRANSFER_PLACEHOLDERS_FLAG_STOP_ON_ERROR",
    "CF_OPERATION_TYPE",
    "CF_OPERATION_TYPE_ACK_DATA",
    "CF_OPERATION_TYPE_ACK_DEHYDRATE",
    "CF_OPERATION_TYPE_ACK_DELETE",
    "CF_OPERATION_TYPE_ACK_RENAME",
    "CF_OPERATION_TYPE_RESTART_HYDRATION",
    "CF_OPERATION_TYPE_RETRIEVE_DATA",
    "CF_OPERATION_TYPE_TRANSFER_DATA",
    "CF_OPERATION_TYPE_TRANSFER_PLACEHOLDERS",
    "CF_PIN_STATE",
    "CF_PIN_STATE_EXCLUDED",
    "CF_PIN_STATE_INHERIT",
    "CF_PIN_STATE_PINNED",
    "CF_PIN_STATE_UNPINNED",
    "CF_PIN_STATE_UNSPECIFIED",
    "CF_PLACEHOLDER_BASIC_INFO",
    "CF_PLACEHOLDER_CREATE_FLAGS",
    "CF_PLACEHOLDER_CREATE_FLAG_ALWAYS_FULL",
    "CF_PLACEHOLDER_CREATE_FLAG_DISABLE_ON_DEMAND_POPULATION",
    "CF_PLACEHOLDER_CREATE_FLAG_MARK_IN_SYNC",
    "CF_PLACEHOLDER_CREATE_FLAG_NONE",
    "CF_PLACEHOLDER_CREATE_FLAG_SUPERSEDE",
    "CF_PLACEHOLDER_CREATE_INFO",
    "CF_PLACEHOLDER_INFO_BASIC",
    "CF_PLACEHOLDER_INFO_CLASS",
    "CF_PLACEHOLDER_INFO_STANDARD",
    "CF_PLACEHOLDER_MANAGEMENT_POLICY",
    "CF_PLACEHOLDER_MANAGEMENT_POLICY_CONVERT_TO_UNRESTRICTED",
    "CF_PLACEHOLDER_MANAGEMENT_POLICY_CREATE_UNRESTRICTED",
    "CF_PLACEHOLDER_MANAGEMENT_POLICY_DEFAULT",
    "CF_PLACEHOLDER_MANAGEMENT_POLICY_UPDATE_UNRESTRICTED",
    "CF_PLACEHOLDER_MAX_FILE_IDENTITY_LENGTH",
    "CF_PLACEHOLDER_RANGE_INFO_CLASS",
    "CF_PLACEHOLDER_RANGE_INFO_MODIFIED",
    "CF_PLACEHOLDER_RANGE_INFO_ONDISK",
    "CF_PLACEHOLDER_RANGE_INFO_VALIDATED",
    "CF_PLACEHOLDER_STANDARD_INFO",
    "CF_PLACEHOLDER_STATE",
    "CF_PLACEHOLDER_STATE_ESSENTIAL_PROP_PRESENT",
    "CF_PLACEHOLDER_STATE_INVALID",
    "CF_PLACEHOLDER_STATE_IN_SYNC",
    "CF_PLACEHOLDER_STATE_NO_STATES",
    "CF_PLACEHOLDER_STATE_PARTIAL",
    "CF_PLACEHOLDER_STATE_PARTIALLY_ON_DISK",
    "CF_PLACEHOLDER_STATE_PLACEHOLDER",
    "CF_PLACEHOLDER_STATE_SYNC_ROOT",
    "CF_PLATFORM_INFO",
    "CF_POPULATION_POLICY",
    "CF_POPULATION_POLICY_ALWAYS_FULL",
    "CF_POPULATION_POLICY_FULL",
    "CF_POPULATION_POLICY_MODIFIER",
    "CF_POPULATION_POLICY_MODIFIER_NONE",
    "CF_POPULATION_POLICY_MODIFIER_USHORT",
    "CF_POPULATION_POLICY_PARTIAL",
    "CF_POPULATION_POLICY_PRIMARY",
    "CF_POPULATION_POLICY_PRIMARY_USHORT",
    "CF_PROCESS_INFO",
    "CF_PROVIDER_STATUS_CLEAR_FLAGS",
    "CF_PROVIDER_STATUS_CONNECTIVITY_LOST",
    "CF_PROVIDER_STATUS_DISCONNECTED",
    "CF_PROVIDER_STATUS_ERROR",
    "CF_PROVIDER_STATUS_IDLE",
    "CF_PROVIDER_STATUS_POPULATE_CONTENT",
    "CF_PROVIDER_STATUS_POPULATE_METADATA",
    "CF_PROVIDER_STATUS_POPULATE_NAMESPACE",
    "CF_PROVIDER_STATUS_SYNC_FULL",
    "CF_PROVIDER_STATUS_SYNC_INCREMENTAL",
    "CF_PROVIDER_STATUS_TERMINATED",
    "CF_REGISTER_FLAGS",
    "CF_REGISTER_FLAG_DISABLE_ON_DEMAND_POPULATION_ON_ROOT",
    "CF_REGISTER_FLAG_MARK_IN_SYNC_ON_ROOT",
    "CF_REGISTER_FLAG_NONE",
    "CF_REGISTER_FLAG_UPDATE",
    "CF_REQUEST_KEY_DEFAULT",
    "CF_REVERT_FLAGS",
    "CF_REVERT_FLAG_NONE",
    "CF_SET_IN_SYNC_FLAGS",
    "CF_SET_IN_SYNC_FLAG_NONE",
    "CF_SET_PIN_FLAGS",
    "CF_SET_PIN_FLAG_NONE",
    "CF_SET_PIN_FLAG_RECURSE",
    "CF_SET_PIN_FLAG_RECURSE_ONLY",
    "CF_SET_PIN_FLAG_RECURSE_STOP_ON_ERROR",
    "CF_SYNC_POLICIES",
    "CF_SYNC_PROVIDER_STATUS",
    "CF_SYNC_REGISTRATION",
    "CF_SYNC_ROOT_BASIC_INFO",
    "CF_SYNC_ROOT_INFO_BASIC",
    "CF_SYNC_ROOT_INFO_CLASS",
    "CF_SYNC_ROOT_INFO_PROVIDER",
    "CF_SYNC_ROOT_INFO_STANDARD",
    "CF_SYNC_ROOT_PROVIDER_INFO",
    "CF_SYNC_ROOT_STANDARD_INFO",
    "CF_SYNC_STATUS",
    "CF_UPDATE_FLAGS",
    "CF_UPDATE_FLAG_ALLOW_PARTIAL",
    "CF_UPDATE_FLAG_ALWAYS_FULL",
    "CF_UPDATE_FLAG_CLEAR_IN_SYNC",
    "CF_UPDATE_FLAG_DEHYDRATE",
    "CF_UPDATE_FLAG_DISABLE_ON_DEMAND_POPULATION",
    "CF_UPDATE_FLAG_ENABLE_ON_DEMAND_POPULATION",
    "CF_UPDATE_FLAG_MARK_IN_SYNC",
    "CF_UPDATE_FLAG_NONE",
    "CF_UPDATE_FLAG_PASSTHROUGH_FS_METADATA",
    "CF_UPDATE_FLAG_REMOVE_FILE_IDENTITY",
    "CF_UPDATE_FLAG_REMOVE_PROPERTY",
    "CF_UPDATE_FLAG_VERIFY_IN_SYNC",
    "CfCloseHandle",
    "CfConnectSyncRoot",
    "CfConvertToPlaceholder",
    "CfCreatePlaceholders",
    "CfDehydratePlaceholder",
    "CfDisconnectSyncRoot",
    "CfExecute",
    "CfGetCorrelationVector",
    "CfGetPlaceholderInfo",
    "CfGetPlaceholderRangeInfo",
    "CfGetPlaceholderStateFromAttributeTag",
    "CfGetPlaceholderStateFromFileInfo",
    "CfGetPlaceholderStateFromFindData",
    "CfGetPlatformInfo",
    "CfGetSyncRootInfoByHandle",
    "CfGetSyncRootInfoByPath",
    "CfGetTransferKey",
    "CfGetWin32HandleFromProtectedHandle",
    "CfHydratePlaceholder",
    "CfOpenFileWithOplock",
    "CfQuerySyncProviderStatus",
    "CfReferenceProtectedHandle",
    "CfRegisterSyncRoot",
    "CfReleaseProtectedHandle",
    "CfReleaseTransferKey",
    "CfReportProviderProgress",
    "CfReportProviderProgress2",
    "CfReportSyncStatus",
    "CfRevertPlaceholder",
    "CfSetCorrelationVector",
    "CfSetInSyncState",
    "CfSetPinState",
    "CfUnregisterSyncRoot",
    "CfUpdatePlaceholder",
    "CfUpdateSyncProviderStatus",
]
_arch_optional = [
]
