from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, PROPERTYKEY, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Storage.CloudFilters
import win32more.Storage.FileSystem
import win32more.System.CorrelationVector
import win32more.System.IO

import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
CF_REQUEST_KEY_DEFAULT = 0
CF_PLACEHOLDER_MAX_FILE_IDENTITY_LENGTH = 4096
CF_MAX_PRIORITY_HINT = 15
CF_MAX_PROVIDER_NAME_LENGTH = 255
CF_MAX_PROVIDER_VERSION_LENGTH = 255
CF_CONNECTION_KEY = IntPtr
def _define_CF_FS_METADATA_head():
    class CF_FS_METADATA(Structure):
        pass
    return CF_FS_METADATA
def _define_CF_FS_METADATA():
    CF_FS_METADATA = win32more.Storage.CloudFilters.CF_FS_METADATA_head
    CF_FS_METADATA._fields_ = [
        ("BasicInfo", win32more.Storage.FileSystem.FILE_BASIC_INFO),
        ("FileSize", win32more.Foundation.LARGE_INTEGER),
    ]
    return CF_FS_METADATA
CF_PLACEHOLDER_CREATE_FLAGS = UInt32
CF_PLACEHOLDER_CREATE_FLAG_NONE = 0
CF_PLACEHOLDER_CREATE_FLAG_DISABLE_ON_DEMAND_POPULATION = 1
CF_PLACEHOLDER_CREATE_FLAG_MARK_IN_SYNC = 2
CF_PLACEHOLDER_CREATE_FLAG_SUPERSEDE = 4
CF_PLACEHOLDER_CREATE_FLAG_ALWAYS_FULL = 8
def _define_CF_PLACEHOLDER_CREATE_INFO_head():
    class CF_PLACEHOLDER_CREATE_INFO(Structure):
        pass
    return CF_PLACEHOLDER_CREATE_INFO
def _define_CF_PLACEHOLDER_CREATE_INFO():
    CF_PLACEHOLDER_CREATE_INFO = win32more.Storage.CloudFilters.CF_PLACEHOLDER_CREATE_INFO_head
    CF_PLACEHOLDER_CREATE_INFO._fields_ = [
        ("RelativeFileName", win32more.Foundation.PWSTR),
        ("FsMetadata", win32more.Storage.CloudFilters.CF_FS_METADATA),
        ("FileIdentity", c_void_p),
        ("FileIdentityLength", UInt32),
        ("Flags", win32more.Storage.CloudFilters.CF_PLACEHOLDER_CREATE_FLAGS),
        ("Result", win32more.Foundation.HRESULT),
        ("CreateUsn", Int64),
    ]
    return CF_PLACEHOLDER_CREATE_INFO
CF_SYNC_PROVIDER_STATUS = UInt32
CF_PROVIDER_STATUS_DISCONNECTED = 0
CF_PROVIDER_STATUS_IDLE = 1
CF_PROVIDER_STATUS_POPULATE_NAMESPACE = 2
CF_PROVIDER_STATUS_POPULATE_METADATA = 4
CF_PROVIDER_STATUS_POPULATE_CONTENT = 8
CF_PROVIDER_STATUS_SYNC_INCREMENTAL = 16
CF_PROVIDER_STATUS_SYNC_FULL = 32
CF_PROVIDER_STATUS_CONNECTIVITY_LOST = 64
CF_PROVIDER_STATUS_CLEAR_FLAGS = 2147483648
CF_PROVIDER_STATUS_TERMINATED = 3221225473
CF_PROVIDER_STATUS_ERROR = 3221225474
def _define_CF_PROCESS_INFO_head():
    class CF_PROCESS_INFO(Structure):
        pass
    return CF_PROCESS_INFO
def _define_CF_PROCESS_INFO():
    CF_PROCESS_INFO = win32more.Storage.CloudFilters.CF_PROCESS_INFO_head
    CF_PROCESS_INFO._fields_ = [
        ("StructSize", UInt32),
        ("ProcessId", UInt32),
        ("ImagePath", win32more.Foundation.PWSTR),
        ("PackageName", win32more.Foundation.PWSTR),
        ("ApplicationId", win32more.Foundation.PWSTR),
        ("CommandLine", win32more.Foundation.PWSTR),
        ("SessionId", UInt32),
    ]
    return CF_PROCESS_INFO
def _define_CF_PLATFORM_INFO_head():
    class CF_PLATFORM_INFO(Structure):
        pass
    return CF_PLATFORM_INFO
def _define_CF_PLATFORM_INFO():
    CF_PLATFORM_INFO = win32more.Storage.CloudFilters.CF_PLATFORM_INFO_head
    CF_PLATFORM_INFO._fields_ = [
        ("BuildNumber", UInt32),
        ("RevisionNumber", UInt32),
        ("IntegrationNumber", UInt32),
    ]
    return CF_PLATFORM_INFO
CF_REGISTER_FLAGS = UInt32
CF_REGISTER_FLAG_NONE = 0
CF_REGISTER_FLAG_UPDATE = 1
CF_REGISTER_FLAG_DISABLE_ON_DEMAND_POPULATION_ON_ROOT = 2
CF_REGISTER_FLAG_MARK_IN_SYNC_ON_ROOT = 4
CF_HYDRATION_POLICY_PRIMARY = UInt16
CF_HYDRATION_POLICY_PARTIAL = 0
CF_HYDRATION_POLICY_PROGRESSIVE = 1
CF_HYDRATION_POLICY_FULL = 2
CF_HYDRATION_POLICY_ALWAYS_FULL = 3
def _define_CF_HYDRATION_POLICY_PRIMARY_USHORT_head():
    class CF_HYDRATION_POLICY_PRIMARY_USHORT(Structure):
        pass
    return CF_HYDRATION_POLICY_PRIMARY_USHORT
def _define_CF_HYDRATION_POLICY_PRIMARY_USHORT():
    CF_HYDRATION_POLICY_PRIMARY_USHORT = win32more.Storage.CloudFilters.CF_HYDRATION_POLICY_PRIMARY_USHORT_head
    CF_HYDRATION_POLICY_PRIMARY_USHORT._fields_ = [
        ("us", UInt16),
    ]
    return CF_HYDRATION_POLICY_PRIMARY_USHORT
CF_HYDRATION_POLICY_MODIFIER = UInt16
CF_HYDRATION_POLICY_MODIFIER_NONE = 0
CF_HYDRATION_POLICY_MODIFIER_VALIDATION_REQUIRED = 1
CF_HYDRATION_POLICY_MODIFIER_STREAMING_ALLOWED = 2
CF_HYDRATION_POLICY_MODIFIER_AUTO_DEHYDRATION_ALLOWED = 4
CF_HYDRATION_POLICY_MODIFIER_ALLOW_FULL_RESTART_HYDRATION = 8
def _define_CF_HYDRATION_POLICY_MODIFIER_USHORT_head():
    class CF_HYDRATION_POLICY_MODIFIER_USHORT(Structure):
        pass
    return CF_HYDRATION_POLICY_MODIFIER_USHORT
def _define_CF_HYDRATION_POLICY_MODIFIER_USHORT():
    CF_HYDRATION_POLICY_MODIFIER_USHORT = win32more.Storage.CloudFilters.CF_HYDRATION_POLICY_MODIFIER_USHORT_head
    CF_HYDRATION_POLICY_MODIFIER_USHORT._fields_ = [
        ("us", UInt16),
    ]
    return CF_HYDRATION_POLICY_MODIFIER_USHORT
def _define_CF_HYDRATION_POLICY_head():
    class CF_HYDRATION_POLICY(Structure):
        pass
    return CF_HYDRATION_POLICY
def _define_CF_HYDRATION_POLICY():
    CF_HYDRATION_POLICY = win32more.Storage.CloudFilters.CF_HYDRATION_POLICY_head
    CF_HYDRATION_POLICY._fields_ = [
        ("Primary", win32more.Storage.CloudFilters.CF_HYDRATION_POLICY_PRIMARY_USHORT),
        ("Modifier", win32more.Storage.CloudFilters.CF_HYDRATION_POLICY_MODIFIER_USHORT),
    ]
    return CF_HYDRATION_POLICY
CF_POPULATION_POLICY_PRIMARY = UInt16
CF_POPULATION_POLICY_PARTIAL = 0
CF_POPULATION_POLICY_FULL = 2
CF_POPULATION_POLICY_ALWAYS_FULL = 3
def _define_CF_POPULATION_POLICY_PRIMARY_USHORT_head():
    class CF_POPULATION_POLICY_PRIMARY_USHORT(Structure):
        pass
    return CF_POPULATION_POLICY_PRIMARY_USHORT
def _define_CF_POPULATION_POLICY_PRIMARY_USHORT():
    CF_POPULATION_POLICY_PRIMARY_USHORT = win32more.Storage.CloudFilters.CF_POPULATION_POLICY_PRIMARY_USHORT_head
    CF_POPULATION_POLICY_PRIMARY_USHORT._fields_ = [
        ("us", UInt16),
    ]
    return CF_POPULATION_POLICY_PRIMARY_USHORT
CF_POPULATION_POLICY_MODIFIER = UInt16
CF_POPULATION_POLICY_MODIFIER_NONE = 0
def _define_CF_POPULATION_POLICY_MODIFIER_USHORT_head():
    class CF_POPULATION_POLICY_MODIFIER_USHORT(Structure):
        pass
    return CF_POPULATION_POLICY_MODIFIER_USHORT
def _define_CF_POPULATION_POLICY_MODIFIER_USHORT():
    CF_POPULATION_POLICY_MODIFIER_USHORT = win32more.Storage.CloudFilters.CF_POPULATION_POLICY_MODIFIER_USHORT_head
    CF_POPULATION_POLICY_MODIFIER_USHORT._fields_ = [
        ("us", UInt16),
    ]
    return CF_POPULATION_POLICY_MODIFIER_USHORT
def _define_CF_POPULATION_POLICY_head():
    class CF_POPULATION_POLICY(Structure):
        pass
    return CF_POPULATION_POLICY
def _define_CF_POPULATION_POLICY():
    CF_POPULATION_POLICY = win32more.Storage.CloudFilters.CF_POPULATION_POLICY_head
    CF_POPULATION_POLICY._fields_ = [
        ("Primary", win32more.Storage.CloudFilters.CF_POPULATION_POLICY_PRIMARY_USHORT),
        ("Modifier", win32more.Storage.CloudFilters.CF_POPULATION_POLICY_MODIFIER_USHORT),
    ]
    return CF_POPULATION_POLICY
CF_PLACEHOLDER_MANAGEMENT_POLICY = Int32
CF_PLACEHOLDER_MANAGEMENT_POLICY_DEFAULT = 0
CF_PLACEHOLDER_MANAGEMENT_POLICY_CREATE_UNRESTRICTED = 1
CF_PLACEHOLDER_MANAGEMENT_POLICY_CONVERT_TO_UNRESTRICTED = 2
CF_PLACEHOLDER_MANAGEMENT_POLICY_UPDATE_UNRESTRICTED = 4
CF_INSYNC_POLICY = UInt32
CF_INSYNC_POLICY_NONE = 0
CF_INSYNC_POLICY_TRACK_FILE_CREATION_TIME = 1
CF_INSYNC_POLICY_TRACK_FILE_READONLY_ATTRIBUTE = 2
CF_INSYNC_POLICY_TRACK_FILE_HIDDEN_ATTRIBUTE = 4
CF_INSYNC_POLICY_TRACK_FILE_SYSTEM_ATTRIBUTE = 8
CF_INSYNC_POLICY_TRACK_DIRECTORY_CREATION_TIME = 16
CF_INSYNC_POLICY_TRACK_DIRECTORY_READONLY_ATTRIBUTE = 32
CF_INSYNC_POLICY_TRACK_DIRECTORY_HIDDEN_ATTRIBUTE = 64
CF_INSYNC_POLICY_TRACK_DIRECTORY_SYSTEM_ATTRIBUTE = 128
CF_INSYNC_POLICY_TRACK_FILE_LAST_WRITE_TIME = 256
CF_INSYNC_POLICY_TRACK_DIRECTORY_LAST_WRITE_TIME = 512
CF_INSYNC_POLICY_TRACK_FILE_ALL = 5592335
CF_INSYNC_POLICY_TRACK_DIRECTORY_ALL = 11184880
CF_INSYNC_POLICY_TRACK_ALL = 16777215
CF_INSYNC_POLICY_PRESERVE_INSYNC_FOR_SYNC_ENGINE = 2147483648
CF_HARDLINK_POLICY = UInt32
CF_HARDLINK_POLICY_NONE = 0
CF_HARDLINK_POLICY_ALLOWED = 1
def _define_CF_SYNC_POLICIES_head():
    class CF_SYNC_POLICIES(Structure):
        pass
    return CF_SYNC_POLICIES
def _define_CF_SYNC_POLICIES():
    CF_SYNC_POLICIES = win32more.Storage.CloudFilters.CF_SYNC_POLICIES_head
    CF_SYNC_POLICIES._fields_ = [
        ("StructSize", UInt32),
        ("Hydration", win32more.Storage.CloudFilters.CF_HYDRATION_POLICY),
        ("Population", win32more.Storage.CloudFilters.CF_POPULATION_POLICY),
        ("InSync", win32more.Storage.CloudFilters.CF_INSYNC_POLICY),
        ("HardLink", win32more.Storage.CloudFilters.CF_HARDLINK_POLICY),
        ("PlaceholderManagement", win32more.Storage.CloudFilters.CF_PLACEHOLDER_MANAGEMENT_POLICY),
    ]
    return CF_SYNC_POLICIES
def _define_CF_SYNC_REGISTRATION_head():
    class CF_SYNC_REGISTRATION(Structure):
        pass
    return CF_SYNC_REGISTRATION
def _define_CF_SYNC_REGISTRATION():
    CF_SYNC_REGISTRATION = win32more.Storage.CloudFilters.CF_SYNC_REGISTRATION_head
    CF_SYNC_REGISTRATION._fields_ = [
        ("StructSize", UInt32),
        ("ProviderName", win32more.Foundation.PWSTR),
        ("ProviderVersion", win32more.Foundation.PWSTR),
        ("SyncRootIdentity", c_void_p),
        ("SyncRootIdentityLength", UInt32),
        ("FileIdentity", c_void_p),
        ("FileIdentityLength", UInt32),
        ("ProviderId", Guid),
    ]
    return CF_SYNC_REGISTRATION
def _define_CF_CALLBACK_INFO_head():
    class CF_CALLBACK_INFO(Structure):
        pass
    return CF_CALLBACK_INFO
def _define_CF_CALLBACK_INFO():
    CF_CALLBACK_INFO = win32more.Storage.CloudFilters.CF_CALLBACK_INFO_head
    CF_CALLBACK_INFO._fields_ = [
        ("StructSize", UInt32),
        ("ConnectionKey", win32more.Storage.CloudFilters.CF_CONNECTION_KEY),
        ("CallbackContext", c_void_p),
        ("VolumeGuidName", win32more.Foundation.PWSTR),
        ("VolumeDosName", win32more.Foundation.PWSTR),
        ("VolumeSerialNumber", UInt32),
        ("SyncRootFileId", win32more.Foundation.LARGE_INTEGER),
        ("SyncRootIdentity", c_void_p),
        ("SyncRootIdentityLength", UInt32),
        ("FileId", win32more.Foundation.LARGE_INTEGER),
        ("FileSize", win32more.Foundation.LARGE_INTEGER),
        ("FileIdentity", c_void_p),
        ("FileIdentityLength", UInt32),
        ("NormalizedPath", win32more.Foundation.PWSTR),
        ("TransferKey", win32more.Foundation.LARGE_INTEGER),
        ("PriorityHint", Byte),
        ("CorrelationVector", POINTER(win32more.System.CorrelationVector.CORRELATION_VECTOR_head)),
        ("ProcessInfo", POINTER(win32more.Storage.CloudFilters.CF_PROCESS_INFO_head)),
        ("RequestKey", win32more.Foundation.LARGE_INTEGER),
    ]
    return CF_CALLBACK_INFO
CF_CALLBACK_CANCEL_FLAGS = UInt32
CF_CALLBACK_CANCEL_FLAG_NONE = 0
CF_CALLBACK_CANCEL_FLAG_IO_TIMEOUT = 1
CF_CALLBACK_CANCEL_FLAG_IO_ABORTED = 2
CF_CALLBACK_FETCH_DATA_FLAGS = UInt32
CF_CALLBACK_FETCH_DATA_FLAG_NONE = 0
CF_CALLBACK_FETCH_DATA_FLAG_RECOVERY = 1
CF_CALLBACK_FETCH_DATA_FLAG_EXPLICIT_HYDRATION = 2
CF_CALLBACK_VALIDATE_DATA_FLAGS = UInt32
CF_CALLBACK_VALIDATE_DATA_FLAG_NONE = 0
CF_CALLBACK_VALIDATE_DATA_FLAG_EXPLICIT_HYDRATION = 2
CF_CALLBACK_FETCH_PLACEHOLDERS_FLAGS = UInt32
CF_CALLBACK_FETCH_PLACEHOLDERS_FLAG_NONE = 0
CF_CALLBACK_OPEN_COMPLETION_FLAGS = UInt32
CF_CALLBACK_OPEN_COMPLETION_FLAG_NONE = 0
CF_CALLBACK_OPEN_COMPLETION_FLAG_PLACEHOLDER_UNKNOWN = 1
CF_CALLBACK_OPEN_COMPLETION_FLAG_PLACEHOLDER_UNSUPPORTED = 2
CF_CALLBACK_CLOSE_COMPLETION_FLAGS = UInt32
CF_CALLBACK_CLOSE_COMPLETION_FLAG_NONE = 0
CF_CALLBACK_CLOSE_COMPLETION_FLAG_DELETED = 1
CF_CALLBACK_DEHYDRATE_FLAGS = UInt32
CF_CALLBACK_DEHYDRATE_FLAG_NONE = 0
CF_CALLBACK_DEHYDRATE_FLAG_BACKGROUND = 1
CF_CALLBACK_DEHYDRATE_COMPLETION_FLAGS = UInt32
CF_CALLBACK_DEHYDRATE_COMPLETION_FLAG_NONE = 0
CF_CALLBACK_DEHYDRATE_COMPLETION_FLAG_BACKGROUND = 1
CF_CALLBACK_DEHYDRATE_COMPLETION_FLAG_DEHYDRATED = 2
CF_CALLBACK_DELETE_FLAGS = UInt32
CF_CALLBACK_DELETE_FLAG_NONE = 0
CF_CALLBACK_DELETE_FLAG_IS_DIRECTORY = 1
CF_CALLBACK_DELETE_FLAG_IS_UNDELETE = 2
CF_CALLBACK_DELETE_COMPLETION_FLAGS = UInt32
CF_CALLBACK_DELETE_COMPLETION_FLAG_NONE = 0
CF_CALLBACK_RENAME_FLAGS = UInt32
CF_CALLBACK_RENAME_FLAG_NONE = 0
CF_CALLBACK_RENAME_FLAG_IS_DIRECTORY = 1
CF_CALLBACK_RENAME_FLAG_SOURCE_IN_SCOPE = 2
CF_CALLBACK_RENAME_FLAG_TARGET_IN_SCOPE = 4
CF_CALLBACK_RENAME_COMPLETION_FLAGS = UInt32
CF_CALLBACK_RENAME_COMPLETION_FLAG_NONE = 0
CF_CALLBACK_DEHYDRATION_REASON = Int32
CF_CALLBACK_DEHYDRATION_REASON_NONE = 0
CF_CALLBACK_DEHYDRATION_REASON_USER_MANUAL = 1
CF_CALLBACK_DEHYDRATION_REASON_SYSTEM_LOW_SPACE = 2
CF_CALLBACK_DEHYDRATION_REASON_SYSTEM_INACTIVITY = 3
CF_CALLBACK_DEHYDRATION_REASON_SYSTEM_OS_UPGRADE = 4
def _define_CF_CALLBACK_PARAMETERS_head():
    class CF_CALLBACK_PARAMETERS(Structure):
        pass
    return CF_CALLBACK_PARAMETERS
def _define_CF_CALLBACK_PARAMETERS():
    CF_CALLBACK_PARAMETERS = win32more.Storage.CloudFilters.CF_CALLBACK_PARAMETERS_head
    class CF_CALLBACK_PARAMETERS__Anonymous_e__Union(Union):
        pass
    class CF_CALLBACK_PARAMETERS__Anonymous_e__Union__Rename_e__Struct(Structure):
        pass
    CF_CALLBACK_PARAMETERS__Anonymous_e__Union__Rename_e__Struct._fields_ = [
        ("Flags", win32more.Storage.CloudFilters.CF_CALLBACK_RENAME_FLAGS),
        ("TargetPath", win32more.Foundation.PWSTR),
    ]
    class CF_CALLBACK_PARAMETERS__Anonymous_e__Union__Delete_e__Struct(Structure):
        pass
    CF_CALLBACK_PARAMETERS__Anonymous_e__Union__Delete_e__Struct._fields_ = [
        ("Flags", win32more.Storage.CloudFilters.CF_CALLBACK_DELETE_FLAGS),
    ]
    class CF_CALLBACK_PARAMETERS__Anonymous_e__Union__Dehydrate_e__Struct(Structure):
        pass
    CF_CALLBACK_PARAMETERS__Anonymous_e__Union__Dehydrate_e__Struct._fields_ = [
        ("Flags", win32more.Storage.CloudFilters.CF_CALLBACK_DEHYDRATE_FLAGS),
        ("Reason", win32more.Storage.CloudFilters.CF_CALLBACK_DEHYDRATION_REASON),
    ]
    class CF_CALLBACK_PARAMETERS__Anonymous_e__Union__OpenCompletion_e__Struct(Structure):
        pass
    CF_CALLBACK_PARAMETERS__Anonymous_e__Union__OpenCompletion_e__Struct._fields_ = [
        ("Flags", win32more.Storage.CloudFilters.CF_CALLBACK_OPEN_COMPLETION_FLAGS),
    ]
    class CF_CALLBACK_PARAMETERS__Anonymous_e__Union__ValidateData_e__Struct(Structure):
        pass
    CF_CALLBACK_PARAMETERS__Anonymous_e__Union__ValidateData_e__Struct._fields_ = [
        ("Flags", win32more.Storage.CloudFilters.CF_CALLBACK_VALIDATE_DATA_FLAGS),
        ("RequiredFileOffset", win32more.Foundation.LARGE_INTEGER),
        ("RequiredLength", win32more.Foundation.LARGE_INTEGER),
    ]
    class CF_CALLBACK_PARAMETERS__Anonymous_e__Union__Cancel_e__Struct(Structure):
        pass
    class CF_CALLBACK_PARAMETERS__Anonymous_e__Union__Cancel_e__Struct__Anonymous_e__Union(Union):
        pass
    class CF_CALLBACK_PARAMETERS__Anonymous_e__Union__Cancel_e__Struct__Anonymous_e__Union__FetchData_e__Struct(Structure):
        pass
    CF_CALLBACK_PARAMETERS__Anonymous_e__Union__Cancel_e__Struct__Anonymous_e__Union__FetchData_e__Struct._fields_ = [
        ("FileOffset", win32more.Foundation.LARGE_INTEGER),
        ("Length", win32more.Foundation.LARGE_INTEGER),
    ]
    CF_CALLBACK_PARAMETERS__Anonymous_e__Union__Cancel_e__Struct__Anonymous_e__Union._fields_ = [
        ("FetchData", CF_CALLBACK_PARAMETERS__Anonymous_e__Union__Cancel_e__Struct__Anonymous_e__Union__FetchData_e__Struct),
    ]
    CF_CALLBACK_PARAMETERS__Anonymous_e__Union__Cancel_e__Struct._anonymous_ = [
        'Anonymous',
    ]
    CF_CALLBACK_PARAMETERS__Anonymous_e__Union__Cancel_e__Struct._fields_ = [
        ("Flags", win32more.Storage.CloudFilters.CF_CALLBACK_CANCEL_FLAGS),
        ("Anonymous", CF_CALLBACK_PARAMETERS__Anonymous_e__Union__Cancel_e__Struct__Anonymous_e__Union),
    ]
    class CF_CALLBACK_PARAMETERS__Anonymous_e__Union__RenameCompletion_e__Struct(Structure):
        pass
    CF_CALLBACK_PARAMETERS__Anonymous_e__Union__RenameCompletion_e__Struct._fields_ = [
        ("Flags", win32more.Storage.CloudFilters.CF_CALLBACK_RENAME_COMPLETION_FLAGS),
        ("SourcePath", win32more.Foundation.PWSTR),
    ]
    class CF_CALLBACK_PARAMETERS__Anonymous_e__Union__DehydrateCompletion_e__Struct(Structure):
        pass
    CF_CALLBACK_PARAMETERS__Anonymous_e__Union__DehydrateCompletion_e__Struct._fields_ = [
        ("Flags", win32more.Storage.CloudFilters.CF_CALLBACK_DEHYDRATE_COMPLETION_FLAGS),
        ("Reason", win32more.Storage.CloudFilters.CF_CALLBACK_DEHYDRATION_REASON),
    ]
    class CF_CALLBACK_PARAMETERS__Anonymous_e__Union__FetchPlaceholders_e__Struct(Structure):
        pass
    CF_CALLBACK_PARAMETERS__Anonymous_e__Union__FetchPlaceholders_e__Struct._fields_ = [
        ("Flags", win32more.Storage.CloudFilters.CF_CALLBACK_FETCH_PLACEHOLDERS_FLAGS),
        ("Pattern", win32more.Foundation.PWSTR),
    ]
    class CF_CALLBACK_PARAMETERS__Anonymous_e__Union__DeleteCompletion_e__Struct(Structure):
        pass
    CF_CALLBACK_PARAMETERS__Anonymous_e__Union__DeleteCompletion_e__Struct._fields_ = [
        ("Flags", win32more.Storage.CloudFilters.CF_CALLBACK_DELETE_COMPLETION_FLAGS),
    ]
    class CF_CALLBACK_PARAMETERS__Anonymous_e__Union__FetchData_e__Struct(Structure):
        pass
    CF_CALLBACK_PARAMETERS__Anonymous_e__Union__FetchData_e__Struct._fields_ = [
        ("Flags", win32more.Storage.CloudFilters.CF_CALLBACK_FETCH_DATA_FLAGS),
        ("RequiredFileOffset", win32more.Foundation.LARGE_INTEGER),
        ("RequiredLength", win32more.Foundation.LARGE_INTEGER),
        ("OptionalFileOffset", win32more.Foundation.LARGE_INTEGER),
        ("OptionalLength", win32more.Foundation.LARGE_INTEGER),
        ("LastDehydrationTime", win32more.Foundation.LARGE_INTEGER),
        ("LastDehydrationReason", win32more.Storage.CloudFilters.CF_CALLBACK_DEHYDRATION_REASON),
    ]
    class CF_CALLBACK_PARAMETERS__Anonymous_e__Union__CloseCompletion_e__Struct(Structure):
        pass
    CF_CALLBACK_PARAMETERS__Anonymous_e__Union__CloseCompletion_e__Struct._fields_ = [
        ("Flags", win32more.Storage.CloudFilters.CF_CALLBACK_CLOSE_COMPLETION_FLAGS),
    ]
    CF_CALLBACK_PARAMETERS__Anonymous_e__Union._fields_ = [
        ("Cancel", CF_CALLBACK_PARAMETERS__Anonymous_e__Union__Cancel_e__Struct),
        ("FetchData", CF_CALLBACK_PARAMETERS__Anonymous_e__Union__FetchData_e__Struct),
        ("ValidateData", CF_CALLBACK_PARAMETERS__Anonymous_e__Union__ValidateData_e__Struct),
        ("FetchPlaceholders", CF_CALLBACK_PARAMETERS__Anonymous_e__Union__FetchPlaceholders_e__Struct),
        ("OpenCompletion", CF_CALLBACK_PARAMETERS__Anonymous_e__Union__OpenCompletion_e__Struct),
        ("CloseCompletion", CF_CALLBACK_PARAMETERS__Anonymous_e__Union__CloseCompletion_e__Struct),
        ("Dehydrate", CF_CALLBACK_PARAMETERS__Anonymous_e__Union__Dehydrate_e__Struct),
        ("DehydrateCompletion", CF_CALLBACK_PARAMETERS__Anonymous_e__Union__DehydrateCompletion_e__Struct),
        ("Delete", CF_CALLBACK_PARAMETERS__Anonymous_e__Union__Delete_e__Struct),
        ("DeleteCompletion", CF_CALLBACK_PARAMETERS__Anonymous_e__Union__DeleteCompletion_e__Struct),
        ("Rename", CF_CALLBACK_PARAMETERS__Anonymous_e__Union__Rename_e__Struct),
        ("RenameCompletion", CF_CALLBACK_PARAMETERS__Anonymous_e__Union__RenameCompletion_e__Struct),
    ]
    CF_CALLBACK_PARAMETERS._anonymous_ = [
        'Anonymous',
    ]
    CF_CALLBACK_PARAMETERS._fields_ = [
        ("ParamSize", UInt32),
        ("Anonymous", CF_CALLBACK_PARAMETERS__Anonymous_e__Union),
    ]
    return CF_CALLBACK_PARAMETERS
def _define_CF_CALLBACK():
    return CFUNCTYPE(Void,POINTER(win32more.Storage.CloudFilters.CF_CALLBACK_INFO_head),POINTER(win32more.Storage.CloudFilters.CF_CALLBACK_PARAMETERS_head), use_last_error=False)
CF_CALLBACK_TYPE = Int32
CF_CALLBACK_TYPE_FETCH_DATA = 0
CF_CALLBACK_TYPE_VALIDATE_DATA = 1
CF_CALLBACK_TYPE_CANCEL_FETCH_DATA = 2
CF_CALLBACK_TYPE_FETCH_PLACEHOLDERS = 3
CF_CALLBACK_TYPE_CANCEL_FETCH_PLACEHOLDERS = 4
CF_CALLBACK_TYPE_NOTIFY_FILE_OPEN_COMPLETION = 5
CF_CALLBACK_TYPE_NOTIFY_FILE_CLOSE_COMPLETION = 6
CF_CALLBACK_TYPE_NOTIFY_DEHYDRATE = 7
CF_CALLBACK_TYPE_NOTIFY_DEHYDRATE_COMPLETION = 8
CF_CALLBACK_TYPE_NOTIFY_DELETE = 9
CF_CALLBACK_TYPE_NOTIFY_DELETE_COMPLETION = 10
CF_CALLBACK_TYPE_NOTIFY_RENAME = 11
CF_CALLBACK_TYPE_NOTIFY_RENAME_COMPLETION = 12
CF_CALLBACK_TYPE_NONE = -1
def _define_CF_CALLBACK_REGISTRATION_head():
    class CF_CALLBACK_REGISTRATION(Structure):
        pass
    return CF_CALLBACK_REGISTRATION
def _define_CF_CALLBACK_REGISTRATION():
    CF_CALLBACK_REGISTRATION = win32more.Storage.CloudFilters.CF_CALLBACK_REGISTRATION_head
    CF_CALLBACK_REGISTRATION._fields_ = [
        ("Type", win32more.Storage.CloudFilters.CF_CALLBACK_TYPE),
        ("Callback", win32more.Storage.CloudFilters.CF_CALLBACK),
    ]
    return CF_CALLBACK_REGISTRATION
CF_CONNECT_FLAGS = UInt32
CF_CONNECT_FLAG_NONE = 0
CF_CONNECT_FLAG_REQUIRE_PROCESS_INFO = 2
CF_CONNECT_FLAG_REQUIRE_FULL_FILE_PATH = 4
CF_CONNECT_FLAG_BLOCK_SELF_IMPLICIT_HYDRATION = 8
CF_OPERATION_TYPE = Int32
CF_OPERATION_TYPE_TRANSFER_DATA = 0
CF_OPERATION_TYPE_RETRIEVE_DATA = 1
CF_OPERATION_TYPE_ACK_DATA = 2
CF_OPERATION_TYPE_RESTART_HYDRATION = 3
CF_OPERATION_TYPE_TRANSFER_PLACEHOLDERS = 4
CF_OPERATION_TYPE_ACK_DEHYDRATE = 5
CF_OPERATION_TYPE_ACK_DELETE = 6
CF_OPERATION_TYPE_ACK_RENAME = 7
def _define_CF_SYNC_STATUS_head():
    class CF_SYNC_STATUS(Structure):
        pass
    return CF_SYNC_STATUS
def _define_CF_SYNC_STATUS():
    CF_SYNC_STATUS = win32more.Storage.CloudFilters.CF_SYNC_STATUS_head
    CF_SYNC_STATUS._fields_ = [
        ("StructSize", UInt32),
        ("Code", UInt32),
        ("DescriptionOffset", UInt32),
        ("DescriptionLength", UInt32),
        ("DeviceIdOffset", UInt32),
        ("DeviceIdLength", UInt32),
    ]
    return CF_SYNC_STATUS
def _define_CF_OPERATION_INFO_head():
    class CF_OPERATION_INFO(Structure):
        pass
    return CF_OPERATION_INFO
def _define_CF_OPERATION_INFO():
    CF_OPERATION_INFO = win32more.Storage.CloudFilters.CF_OPERATION_INFO_head
    CF_OPERATION_INFO._fields_ = [
        ("StructSize", UInt32),
        ("Type", win32more.Storage.CloudFilters.CF_OPERATION_TYPE),
        ("ConnectionKey", win32more.Storage.CloudFilters.CF_CONNECTION_KEY),
        ("TransferKey", win32more.Foundation.LARGE_INTEGER),
        ("CorrelationVector", POINTER(win32more.System.CorrelationVector.CORRELATION_VECTOR_head)),
        ("SyncStatus", POINTER(win32more.Storage.CloudFilters.CF_SYNC_STATUS_head)),
        ("RequestKey", win32more.Foundation.LARGE_INTEGER),
    ]
    return CF_OPERATION_INFO
CF_OPERATION_TRANSFER_DATA_FLAGS = UInt32
CF_OPERATION_TRANSFER_DATA_FLAG_NONE = 0
CF_OPERATION_RETRIEVE_DATA_FLAGS = UInt32
CF_OPERATION_RETRIEVE_DATA_FLAG_NONE = 0
CF_OPERATION_ACK_DATA_FLAGS = UInt32
CF_OPERATION_ACK_DATA_FLAG_NONE = 0
CF_OPERATION_RESTART_HYDRATION_FLAGS = UInt32
CF_OPERATION_RESTART_HYDRATION_FLAG_NONE = 0
CF_OPERATION_RESTART_HYDRATION_FLAG_MARK_IN_SYNC = 1
CF_OPERATION_TRANSFER_PLACEHOLDERS_FLAGS = UInt32
CF_OPERATION_TRANSFER_PLACEHOLDERS_FLAG_NONE = 0
CF_OPERATION_TRANSFER_PLACEHOLDERS_FLAG_STOP_ON_ERROR = 1
CF_OPERATION_TRANSFER_PLACEHOLDERS_FLAG_DISABLE_ON_DEMAND_POPULATION = 2
CF_OPERATION_ACK_DEHYDRATE_FLAGS = UInt32
CF_OPERATION_ACK_DEHYDRATE_FLAG_NONE = 0
CF_OPERATION_ACK_RENAME_FLAGS = UInt32
CF_OPERATION_ACK_RENAME_FLAG_NONE = 0
CF_OPERATION_ACK_DELETE_FLAGS = UInt32
CF_OPERATION_ACK_DELETE_FLAG_NONE = 0
def _define_CF_OPERATION_PARAMETERS_head():
    class CF_OPERATION_PARAMETERS(Structure):
        pass
    return CF_OPERATION_PARAMETERS
def _define_CF_OPERATION_PARAMETERS():
    CF_OPERATION_PARAMETERS = win32more.Storage.CloudFilters.CF_OPERATION_PARAMETERS_head
    class CF_OPERATION_PARAMETERS__Anonymous_e__Union(Union):
        pass
    class CF_OPERATION_PARAMETERS__Anonymous_e__Union__AckRename_e__Struct(Structure):
        pass
    CF_OPERATION_PARAMETERS__Anonymous_e__Union__AckRename_e__Struct._fields_ = [
        ("Flags", win32more.Storage.CloudFilters.CF_OPERATION_ACK_RENAME_FLAGS),
        ("CompletionStatus", win32more.Foundation.NTSTATUS),
    ]
    class CF_OPERATION_PARAMETERS__Anonymous_e__Union__TransferPlaceholders_e__Struct(Structure):
        pass
    CF_OPERATION_PARAMETERS__Anonymous_e__Union__TransferPlaceholders_e__Struct._fields_ = [
        ("Flags", win32more.Storage.CloudFilters.CF_OPERATION_TRANSFER_PLACEHOLDERS_FLAGS),
        ("CompletionStatus", win32more.Foundation.NTSTATUS),
        ("PlaceholderTotalCount", win32more.Foundation.LARGE_INTEGER),
        ("PlaceholderArray", POINTER(win32more.Storage.CloudFilters.CF_PLACEHOLDER_CREATE_INFO_head)),
        ("PlaceholderCount", UInt32),
        ("EntriesProcessed", UInt32),
    ]
    class CF_OPERATION_PARAMETERS__Anonymous_e__Union__AckData_e__Struct(Structure):
        pass
    CF_OPERATION_PARAMETERS__Anonymous_e__Union__AckData_e__Struct._fields_ = [
        ("Flags", win32more.Storage.CloudFilters.CF_OPERATION_ACK_DATA_FLAGS),
        ("CompletionStatus", win32more.Foundation.NTSTATUS),
        ("Offset", win32more.Foundation.LARGE_INTEGER),
        ("Length", win32more.Foundation.LARGE_INTEGER),
    ]
    class CF_OPERATION_PARAMETERS__Anonymous_e__Union__TransferData_e__Struct(Structure):
        pass
    CF_OPERATION_PARAMETERS__Anonymous_e__Union__TransferData_e__Struct._fields_ = [
        ("Flags", win32more.Storage.CloudFilters.CF_OPERATION_TRANSFER_DATA_FLAGS),
        ("CompletionStatus", win32more.Foundation.NTSTATUS),
        ("Buffer", c_void_p),
        ("Offset", win32more.Foundation.LARGE_INTEGER),
        ("Length", win32more.Foundation.LARGE_INTEGER),
    ]
    class CF_OPERATION_PARAMETERS__Anonymous_e__Union__AckDelete_e__Struct(Structure):
        pass
    CF_OPERATION_PARAMETERS__Anonymous_e__Union__AckDelete_e__Struct._fields_ = [
        ("Flags", win32more.Storage.CloudFilters.CF_OPERATION_ACK_DELETE_FLAGS),
        ("CompletionStatus", win32more.Foundation.NTSTATUS),
    ]
    class CF_OPERATION_PARAMETERS__Anonymous_e__Union__RestartHydration_e__Struct(Structure):
        pass
    CF_OPERATION_PARAMETERS__Anonymous_e__Union__RestartHydration_e__Struct._fields_ = [
        ("Flags", win32more.Storage.CloudFilters.CF_OPERATION_RESTART_HYDRATION_FLAGS),
        ("FsMetadata", POINTER(win32more.Storage.CloudFilters.CF_FS_METADATA_head)),
        ("FileIdentity", c_void_p),
        ("FileIdentityLength", UInt32),
    ]
    class CF_OPERATION_PARAMETERS__Anonymous_e__Union__AckDehydrate_e__Struct(Structure):
        pass
    CF_OPERATION_PARAMETERS__Anonymous_e__Union__AckDehydrate_e__Struct._fields_ = [
        ("Flags", win32more.Storage.CloudFilters.CF_OPERATION_ACK_DEHYDRATE_FLAGS),
        ("CompletionStatus", win32more.Foundation.NTSTATUS),
        ("FileIdentity", c_void_p),
        ("FileIdentityLength", UInt32),
    ]
    class CF_OPERATION_PARAMETERS__Anonymous_e__Union__RetrieveData_e__Struct(Structure):
        pass
    CF_OPERATION_PARAMETERS__Anonymous_e__Union__RetrieveData_e__Struct._fields_ = [
        ("Flags", win32more.Storage.CloudFilters.CF_OPERATION_RETRIEVE_DATA_FLAGS),
        ("Buffer", c_void_p),
        ("Offset", win32more.Foundation.LARGE_INTEGER),
        ("Length", win32more.Foundation.LARGE_INTEGER),
        ("ReturnedLength", win32more.Foundation.LARGE_INTEGER),
    ]
    CF_OPERATION_PARAMETERS__Anonymous_e__Union._fields_ = [
        ("TransferData", CF_OPERATION_PARAMETERS__Anonymous_e__Union__TransferData_e__Struct),
        ("RetrieveData", CF_OPERATION_PARAMETERS__Anonymous_e__Union__RetrieveData_e__Struct),
        ("AckData", CF_OPERATION_PARAMETERS__Anonymous_e__Union__AckData_e__Struct),
        ("RestartHydration", CF_OPERATION_PARAMETERS__Anonymous_e__Union__RestartHydration_e__Struct),
        ("TransferPlaceholders", CF_OPERATION_PARAMETERS__Anonymous_e__Union__TransferPlaceholders_e__Struct),
        ("AckDehydrate", CF_OPERATION_PARAMETERS__Anonymous_e__Union__AckDehydrate_e__Struct),
        ("AckRename", CF_OPERATION_PARAMETERS__Anonymous_e__Union__AckRename_e__Struct),
        ("AckDelete", CF_OPERATION_PARAMETERS__Anonymous_e__Union__AckDelete_e__Struct),
    ]
    CF_OPERATION_PARAMETERS._anonymous_ = [
        'Anonymous',
    ]
    CF_OPERATION_PARAMETERS._fields_ = [
        ("ParamSize", UInt32),
        ("Anonymous", CF_OPERATION_PARAMETERS__Anonymous_e__Union),
    ]
    return CF_OPERATION_PARAMETERS
CF_CREATE_FLAGS = UInt32
CF_CREATE_FLAG_NONE = 0
CF_CREATE_FLAG_STOP_ON_ERROR = 1
CF_OPEN_FILE_FLAGS = UInt32
CF_OPEN_FILE_FLAG_NONE = 0
CF_OPEN_FILE_FLAG_EXCLUSIVE = 1
CF_OPEN_FILE_FLAG_WRITE_ACCESS = 2
CF_OPEN_FILE_FLAG_DELETE_ACCESS = 4
CF_OPEN_FILE_FLAG_FOREGROUND = 8
def _define_CF_FILE_RANGE_head():
    class CF_FILE_RANGE(Structure):
        pass
    return CF_FILE_RANGE
def _define_CF_FILE_RANGE():
    CF_FILE_RANGE = win32more.Storage.CloudFilters.CF_FILE_RANGE_head
    CF_FILE_RANGE._fields_ = [
        ("StartingOffset", win32more.Foundation.LARGE_INTEGER),
        ("Length", win32more.Foundation.LARGE_INTEGER),
    ]
    return CF_FILE_RANGE
CF_CONVERT_FLAGS = UInt32
CF_CONVERT_FLAG_NONE = 0
CF_CONVERT_FLAG_MARK_IN_SYNC = 1
CF_CONVERT_FLAG_DEHYDRATE = 2
CF_CONVERT_FLAG_ENABLE_ON_DEMAND_POPULATION = 4
CF_CONVERT_FLAG_ALWAYS_FULL = 8
CF_CONVERT_FLAG_FORCE_CONVERT_TO_CLOUD_FILE = 16
CF_UPDATE_FLAGS = UInt32
CF_UPDATE_FLAG_NONE = 0
CF_UPDATE_FLAG_VERIFY_IN_SYNC = 1
CF_UPDATE_FLAG_MARK_IN_SYNC = 2
CF_UPDATE_FLAG_DEHYDRATE = 4
CF_UPDATE_FLAG_ENABLE_ON_DEMAND_POPULATION = 8
CF_UPDATE_FLAG_DISABLE_ON_DEMAND_POPULATION = 16
CF_UPDATE_FLAG_REMOVE_FILE_IDENTITY = 32
CF_UPDATE_FLAG_CLEAR_IN_SYNC = 64
CF_UPDATE_FLAG_REMOVE_PROPERTY = 128
CF_UPDATE_FLAG_PASSTHROUGH_FS_METADATA = 256
CF_UPDATE_FLAG_ALWAYS_FULL = 512
CF_UPDATE_FLAG_ALLOW_PARTIAL = 1024
CF_REVERT_FLAGS = UInt32
CF_REVERT_FLAG_NONE = 0
CF_HYDRATE_FLAGS = UInt32
CF_HYDRATE_FLAG_NONE = 0
CF_DEHYDRATE_FLAGS = UInt32
CF_DEHYDRATE_FLAG_NONE = 0
CF_DEHYDRATE_FLAG_BACKGROUND = 1
CF_PIN_STATE = Int32
CF_PIN_STATE_UNSPECIFIED = 0
CF_PIN_STATE_PINNED = 1
CF_PIN_STATE_UNPINNED = 2
CF_PIN_STATE_EXCLUDED = 3
CF_PIN_STATE_INHERIT = 4
CF_SET_PIN_FLAGS = UInt32
CF_SET_PIN_FLAG_NONE = 0
CF_SET_PIN_FLAG_RECURSE = 1
CF_SET_PIN_FLAG_RECURSE_ONLY = 2
CF_SET_PIN_FLAG_RECURSE_STOP_ON_ERROR = 4
CF_IN_SYNC_STATE = Int32
CF_IN_SYNC_STATE_NOT_IN_SYNC = 0
CF_IN_SYNC_STATE_IN_SYNC = 1
CF_SET_IN_SYNC_FLAGS = UInt32
CF_SET_IN_SYNC_FLAG_NONE = 0
CF_PLACEHOLDER_STATE = UInt32
CF_PLACEHOLDER_STATE_NO_STATES = 0
CF_PLACEHOLDER_STATE_PLACEHOLDER = 1
CF_PLACEHOLDER_STATE_SYNC_ROOT = 2
CF_PLACEHOLDER_STATE_ESSENTIAL_PROP_PRESENT = 4
CF_PLACEHOLDER_STATE_IN_SYNC = 8
CF_PLACEHOLDER_STATE_PARTIAL = 16
CF_PLACEHOLDER_STATE_PARTIALLY_ON_DISK = 32
CF_PLACEHOLDER_STATE_INVALID = 4294967295
CF_PLACEHOLDER_INFO_CLASS = Int32
CF_PLACEHOLDER_INFO_BASIC = 0
CF_PLACEHOLDER_INFO_STANDARD = 1
def _define_CF_PLACEHOLDER_BASIC_INFO_head():
    class CF_PLACEHOLDER_BASIC_INFO(Structure):
        pass
    return CF_PLACEHOLDER_BASIC_INFO
def _define_CF_PLACEHOLDER_BASIC_INFO():
    CF_PLACEHOLDER_BASIC_INFO = win32more.Storage.CloudFilters.CF_PLACEHOLDER_BASIC_INFO_head
    CF_PLACEHOLDER_BASIC_INFO._fields_ = [
        ("PinState", win32more.Storage.CloudFilters.CF_PIN_STATE),
        ("InSyncState", win32more.Storage.CloudFilters.CF_IN_SYNC_STATE),
        ("FileId", win32more.Foundation.LARGE_INTEGER),
        ("SyncRootFileId", win32more.Foundation.LARGE_INTEGER),
        ("FileIdentityLength", UInt32),
        ("FileIdentity", Byte * 0),
    ]
    return CF_PLACEHOLDER_BASIC_INFO
def _define_CF_PLACEHOLDER_STANDARD_INFO_head():
    class CF_PLACEHOLDER_STANDARD_INFO(Structure):
        pass
    return CF_PLACEHOLDER_STANDARD_INFO
def _define_CF_PLACEHOLDER_STANDARD_INFO():
    CF_PLACEHOLDER_STANDARD_INFO = win32more.Storage.CloudFilters.CF_PLACEHOLDER_STANDARD_INFO_head
    CF_PLACEHOLDER_STANDARD_INFO._fields_ = [
        ("OnDiskDataSize", win32more.Foundation.LARGE_INTEGER),
        ("ValidatedDataSize", win32more.Foundation.LARGE_INTEGER),
        ("ModifiedDataSize", win32more.Foundation.LARGE_INTEGER),
        ("PropertiesSize", win32more.Foundation.LARGE_INTEGER),
        ("PinState", win32more.Storage.CloudFilters.CF_PIN_STATE),
        ("InSyncState", win32more.Storage.CloudFilters.CF_IN_SYNC_STATE),
        ("FileId", win32more.Foundation.LARGE_INTEGER),
        ("SyncRootFileId", win32more.Foundation.LARGE_INTEGER),
        ("FileIdentityLength", UInt32),
        ("FileIdentity", Byte * 0),
    ]
    return CF_PLACEHOLDER_STANDARD_INFO
CF_SYNC_ROOT_INFO_CLASS = Int32
CF_SYNC_ROOT_INFO_BASIC = 0
CF_SYNC_ROOT_INFO_STANDARD = 1
CF_SYNC_ROOT_INFO_PROVIDER = 2
def _define_CF_SYNC_ROOT_BASIC_INFO_head():
    class CF_SYNC_ROOT_BASIC_INFO(Structure):
        pass
    return CF_SYNC_ROOT_BASIC_INFO
def _define_CF_SYNC_ROOT_BASIC_INFO():
    CF_SYNC_ROOT_BASIC_INFO = win32more.Storage.CloudFilters.CF_SYNC_ROOT_BASIC_INFO_head
    CF_SYNC_ROOT_BASIC_INFO._fields_ = [
        ("SyncRootFileId", win32more.Foundation.LARGE_INTEGER),
    ]
    return CF_SYNC_ROOT_BASIC_INFO
def _define_CF_SYNC_ROOT_PROVIDER_INFO_head():
    class CF_SYNC_ROOT_PROVIDER_INFO(Structure):
        pass
    return CF_SYNC_ROOT_PROVIDER_INFO
def _define_CF_SYNC_ROOT_PROVIDER_INFO():
    CF_SYNC_ROOT_PROVIDER_INFO = win32more.Storage.CloudFilters.CF_SYNC_ROOT_PROVIDER_INFO_head
    CF_SYNC_ROOT_PROVIDER_INFO._fields_ = [
        ("ProviderStatus", win32more.Storage.CloudFilters.CF_SYNC_PROVIDER_STATUS),
        ("ProviderName", Char * 256),
        ("ProviderVersion", Char * 256),
    ]
    return CF_SYNC_ROOT_PROVIDER_INFO
def _define_CF_SYNC_ROOT_STANDARD_INFO_head():
    class CF_SYNC_ROOT_STANDARD_INFO(Structure):
        pass
    return CF_SYNC_ROOT_STANDARD_INFO
def _define_CF_SYNC_ROOT_STANDARD_INFO():
    CF_SYNC_ROOT_STANDARD_INFO = win32more.Storage.CloudFilters.CF_SYNC_ROOT_STANDARD_INFO_head
    CF_SYNC_ROOT_STANDARD_INFO._fields_ = [
        ("SyncRootFileId", win32more.Foundation.LARGE_INTEGER),
        ("HydrationPolicy", win32more.Storage.CloudFilters.CF_HYDRATION_POLICY),
        ("PopulationPolicy", win32more.Storage.CloudFilters.CF_POPULATION_POLICY),
        ("InSyncPolicy", win32more.Storage.CloudFilters.CF_INSYNC_POLICY),
        ("HardLinkPolicy", win32more.Storage.CloudFilters.CF_HARDLINK_POLICY),
        ("ProviderStatus", win32more.Storage.CloudFilters.CF_SYNC_PROVIDER_STATUS),
        ("ProviderName", Char * 256),
        ("ProviderVersion", Char * 256),
        ("SyncRootIdentityLength", UInt32),
        ("SyncRootIdentity", Byte * 0),
    ]
    return CF_SYNC_ROOT_STANDARD_INFO
CF_PLACEHOLDER_RANGE_INFO_CLASS = Int32
CF_PLACEHOLDER_RANGE_INFO_ONDISK = 1
CF_PLACEHOLDER_RANGE_INFO_VALIDATED = 2
CF_PLACEHOLDER_RANGE_INFO_MODIFIED = 3
def _define_CfGetPlatformInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.CloudFilters.CF_PLATFORM_INFO_head), use_last_error=False)(("CfGetPlatformInfo", windll["cldapi"]), ((1, 'PlatformVersion'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CfRegisterSyncRoot():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Storage.CloudFilters.CF_SYNC_REGISTRATION_head),POINTER(win32more.Storage.CloudFilters.CF_SYNC_POLICIES_head),win32more.Storage.CloudFilters.CF_REGISTER_FLAGS, use_last_error=False)(("CfRegisterSyncRoot", windll["cldapi"]), ((1, 'SyncRootPath'),(1, 'Registration'),(1, 'Policies'),(1, 'RegisterFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CfUnregisterSyncRoot():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(("CfUnregisterSyncRoot", windll["cldapi"]), ((1, 'SyncRootPath'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CfConnectSyncRoot():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Storage.CloudFilters.CF_CALLBACK_REGISTRATION_head),c_void_p,win32more.Storage.CloudFilters.CF_CONNECT_FLAGS,POINTER(win32more.Storage.CloudFilters.CF_CONNECTION_KEY), use_last_error=False)(("CfConnectSyncRoot", windll["cldapi"]), ((1, 'SyncRootPath'),(1, 'CallbackTable'),(1, 'CallbackContext'),(1, 'ConnectFlags'),(1, 'ConnectionKey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CfDisconnectSyncRoot():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.CloudFilters.CF_CONNECTION_KEY, use_last_error=False)(("CfDisconnectSyncRoot", windll["cldapi"]), ((1, 'ConnectionKey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CfGetTransferKey():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.LARGE_INTEGER_head), use_last_error=False)(("CfGetTransferKey", windll["cldapi"]), ((1, 'FileHandle'),(1, 'TransferKey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CfReleaseTransferKey():
    try:
        return WINFUNCTYPE(Void,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.LARGE_INTEGER_head), use_last_error=False)(("CfReleaseTransferKey", windll["cldapi"]), ((1, 'FileHandle'),(1, 'TransferKey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CfExecute():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.CloudFilters.CF_OPERATION_INFO_head),POINTER(win32more.Storage.CloudFilters.CF_OPERATION_PARAMETERS_head), use_last_error=False)(("CfExecute", windll["cldapi"]), ((1, 'OpInfo'),(1, 'OpParams'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CfUpdateSyncProviderStatus():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.CloudFilters.CF_CONNECTION_KEY,win32more.Storage.CloudFilters.CF_SYNC_PROVIDER_STATUS, use_last_error=False)(("CfUpdateSyncProviderStatus", windll["cldapi"]), ((1, 'ConnectionKey'),(1, 'ProviderStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CfQuerySyncProviderStatus():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.CloudFilters.CF_CONNECTION_KEY,POINTER(win32more.Storage.CloudFilters.CF_SYNC_PROVIDER_STATUS), use_last_error=False)(("CfQuerySyncProviderStatus", windll["cldapi"]), ((1, 'ConnectionKey'),(1, 'ProviderStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CfReportSyncStatus():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Storage.CloudFilters.CF_SYNC_STATUS_head), use_last_error=False)(("CfReportSyncStatus", windll["cldapi"]), ((1, 'SyncRootPath'),(1, 'SyncStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CfCreatePlaceholders():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Storage.CloudFilters.CF_PLACEHOLDER_CREATE_INFO),UInt32,win32more.Storage.CloudFilters.CF_CREATE_FLAGS,POINTER(UInt32), use_last_error=False)(("CfCreatePlaceholders", windll["cldapi"]), ((1, 'BaseDirectoryPath'),(1, 'PlaceholderArray'),(1, 'PlaceholderCount'),(1, 'CreateFlags'),(1, 'EntriesProcessed'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CfOpenFileWithOplock():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Storage.CloudFilters.CF_OPEN_FILE_FLAGS,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("CfOpenFileWithOplock", windll["cldapi"]), ((1, 'FilePath'),(1, 'Flags'),(1, 'ProtectedHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CfReferenceProtectedHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,win32more.Foundation.HANDLE, use_last_error=False)(("CfReferenceProtectedHandle", windll["cldapi"]), ((1, 'ProtectedHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CfGetWin32HandleFromProtectedHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.HANDLE, use_last_error=False)(("CfGetWin32HandleFromProtectedHandle", windll["cldapi"]), ((1, 'ProtectedHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CfReleaseProtectedHandle():
    try:
        return WINFUNCTYPE(Void,win32more.Foundation.HANDLE, use_last_error=False)(("CfReleaseProtectedHandle", windll["cldapi"]), ((1, 'ProtectedHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CfCloseHandle():
    try:
        return WINFUNCTYPE(Void,win32more.Foundation.HANDLE, use_last_error=False)(("CfCloseHandle", windll["cldapi"]), ((1, 'FileHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CfConvertToPlaceholder():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,c_void_p,UInt32,win32more.Storage.CloudFilters.CF_CONVERT_FLAGS,POINTER(Int64),POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(("CfConvertToPlaceholder", windll["cldapi"]), ((1, 'FileHandle'),(1, 'FileIdentity'),(1, 'FileIdentityLength'),(1, 'ConvertFlags'),(1, 'ConvertUsn'),(1, 'Overlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CfUpdatePlaceholder():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(win32more.Storage.CloudFilters.CF_FS_METADATA_head),c_void_p,UInt32,POINTER(win32more.Storage.CloudFilters.CF_FILE_RANGE),UInt32,win32more.Storage.CloudFilters.CF_UPDATE_FLAGS,POINTER(Int64),POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(("CfUpdatePlaceholder", windll["cldapi"]), ((1, 'FileHandle'),(1, 'FsMetadata'),(1, 'FileIdentity'),(1, 'FileIdentityLength'),(1, 'DehydrateRangeArray'),(1, 'DehydrateRangeCount'),(1, 'UpdateFlags'),(1, 'UpdateUsn'),(1, 'Overlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CfRevertPlaceholder():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,win32more.Storage.CloudFilters.CF_REVERT_FLAGS,POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(("CfRevertPlaceholder", windll["cldapi"]), ((1, 'FileHandle'),(1, 'RevertFlags'),(1, 'Overlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CfHydratePlaceholder():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,win32more.Foundation.LARGE_INTEGER,win32more.Foundation.LARGE_INTEGER,win32more.Storage.CloudFilters.CF_HYDRATE_FLAGS,POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(("CfHydratePlaceholder", windll["cldapi"]), ((1, 'FileHandle'),(1, 'StartingOffset'),(1, 'Length'),(1, 'HydrateFlags'),(1, 'Overlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CfDehydratePlaceholder():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,win32more.Foundation.LARGE_INTEGER,win32more.Foundation.LARGE_INTEGER,win32more.Storage.CloudFilters.CF_DEHYDRATE_FLAGS,POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(("CfDehydratePlaceholder", windll["cldapi"]), ((1, 'FileHandle'),(1, 'StartingOffset'),(1, 'Length'),(1, 'DehydrateFlags'),(1, 'Overlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CfSetPinState():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,win32more.Storage.CloudFilters.CF_PIN_STATE,win32more.Storage.CloudFilters.CF_SET_PIN_FLAGS,POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(("CfSetPinState", windll["cldapi"]), ((1, 'FileHandle'),(1, 'PinState'),(1, 'PinFlags'),(1, 'Overlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CfSetInSyncState():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,win32more.Storage.CloudFilters.CF_IN_SYNC_STATE,win32more.Storage.CloudFilters.CF_SET_IN_SYNC_FLAGS,POINTER(Int64), use_last_error=False)(("CfSetInSyncState", windll["cldapi"]), ((1, 'FileHandle'),(1, 'InSyncState'),(1, 'InSyncFlags'),(1, 'InSyncUsn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CfSetCorrelationVector():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(win32more.System.CorrelationVector.CORRELATION_VECTOR_head), use_last_error=False)(("CfSetCorrelationVector", windll["cldapi"]), ((1, 'FileHandle'),(1, 'CorrelationVector'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CfGetCorrelationVector():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(win32more.System.CorrelationVector.CORRELATION_VECTOR_head), use_last_error=False)(("CfGetCorrelationVector", windll["cldapi"]), ((1, 'FileHandle'),(1, 'CorrelationVector'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CfGetPlaceholderStateFromAttributeTag():
    try:
        return WINFUNCTYPE(win32more.Storage.CloudFilters.CF_PLACEHOLDER_STATE,UInt32,UInt32, use_last_error=False)(("CfGetPlaceholderStateFromAttributeTag", windll["cldapi"]), ((1, 'FileAttributes'),(1, 'ReparseTag'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CfGetPlaceholderStateFromFileInfo():
    try:
        return WINFUNCTYPE(win32more.Storage.CloudFilters.CF_PLACEHOLDER_STATE,c_void_p,win32more.Storage.FileSystem.FILE_INFO_BY_HANDLE_CLASS, use_last_error=False)(("CfGetPlaceholderStateFromFileInfo", windll["cldapi"]), ((1, 'InfoBuffer'),(1, 'InfoClass'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CfGetPlaceholderStateFromFindData():
    try:
        return WINFUNCTYPE(win32more.Storage.CloudFilters.CF_PLACEHOLDER_STATE,POINTER(win32more.Storage.FileSystem.WIN32_FIND_DATAA_head), use_last_error=False)(("CfGetPlaceholderStateFromFindData", windll["cldapi"]), ((1, 'FindData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CfGetPlaceholderInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,win32more.Storage.CloudFilters.CF_PLACEHOLDER_INFO_CLASS,c_void_p,UInt32,POINTER(UInt32), use_last_error=False)(("CfGetPlaceholderInfo", windll["cldapi"]), ((1, 'FileHandle'),(1, 'InfoClass'),(1, 'InfoBuffer'),(1, 'InfoBufferLength'),(1, 'ReturnedLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CfGetSyncRootInfoByPath():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Storage.CloudFilters.CF_SYNC_ROOT_INFO_CLASS,c_void_p,UInt32,POINTER(UInt32), use_last_error=False)(("CfGetSyncRootInfoByPath", windll["cldapi"]), ((1, 'FilePath'),(1, 'InfoClass'),(1, 'InfoBuffer'),(1, 'InfoBufferLength'),(1, 'ReturnedLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CfGetSyncRootInfoByHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,win32more.Storage.CloudFilters.CF_SYNC_ROOT_INFO_CLASS,c_void_p,UInt32,POINTER(UInt32), use_last_error=False)(("CfGetSyncRootInfoByHandle", windll["cldapi"]), ((1, 'FileHandle'),(1, 'InfoClass'),(1, 'InfoBuffer'),(1, 'InfoBufferLength'),(1, 'ReturnedLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CfGetPlaceholderRangeInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,win32more.Storage.CloudFilters.CF_PLACEHOLDER_RANGE_INFO_CLASS,win32more.Foundation.LARGE_INTEGER,win32more.Foundation.LARGE_INTEGER,c_void_p,UInt32,POINTER(UInt32), use_last_error=False)(("CfGetPlaceholderRangeInfo", windll["cldapi"]), ((1, 'FileHandle'),(1, 'InfoClass'),(1, 'StartingOffset'),(1, 'Length'),(1, 'InfoBuffer'),(1, 'InfoBufferLength'),(1, 'ReturnedLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CfReportProviderProgress():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.CloudFilters.CF_CONNECTION_KEY,win32more.Foundation.LARGE_INTEGER,win32more.Foundation.LARGE_INTEGER,win32more.Foundation.LARGE_INTEGER, use_last_error=False)(("CfReportProviderProgress", windll["cldapi"]), ((1, 'ConnectionKey'),(1, 'TransferKey'),(1, 'ProviderProgressTotal'),(1, 'ProviderProgressCompleted'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CfReportProviderProgress2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.CloudFilters.CF_CONNECTION_KEY,win32more.Foundation.LARGE_INTEGER,win32more.Foundation.LARGE_INTEGER,win32more.Foundation.LARGE_INTEGER,win32more.Foundation.LARGE_INTEGER,UInt32, use_last_error=False)(("CfReportProviderProgress2", windll["cldapi"]), ((1, 'ConnectionKey'),(1, 'TransferKey'),(1, 'RequestKey'),(1, 'ProviderProgressTotal'),(1, 'ProviderProgressCompleted'),(1, 'TargetSessionId'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "CF_REQUEST_KEY_DEFAULT",
    "CF_PLACEHOLDER_MAX_FILE_IDENTITY_LENGTH",
    "CF_MAX_PRIORITY_HINT",
    "CF_MAX_PROVIDER_NAME_LENGTH",
    "CF_MAX_PROVIDER_VERSION_LENGTH",
    "CF_CONNECTION_KEY",
    "CF_FS_METADATA",
    "CF_PLACEHOLDER_CREATE_FLAGS",
    "CF_PLACEHOLDER_CREATE_FLAG_NONE",
    "CF_PLACEHOLDER_CREATE_FLAG_DISABLE_ON_DEMAND_POPULATION",
    "CF_PLACEHOLDER_CREATE_FLAG_MARK_IN_SYNC",
    "CF_PLACEHOLDER_CREATE_FLAG_SUPERSEDE",
    "CF_PLACEHOLDER_CREATE_FLAG_ALWAYS_FULL",
    "CF_PLACEHOLDER_CREATE_INFO",
    "CF_SYNC_PROVIDER_STATUS",
    "CF_PROVIDER_STATUS_DISCONNECTED",
    "CF_PROVIDER_STATUS_IDLE",
    "CF_PROVIDER_STATUS_POPULATE_NAMESPACE",
    "CF_PROVIDER_STATUS_POPULATE_METADATA",
    "CF_PROVIDER_STATUS_POPULATE_CONTENT",
    "CF_PROVIDER_STATUS_SYNC_INCREMENTAL",
    "CF_PROVIDER_STATUS_SYNC_FULL",
    "CF_PROVIDER_STATUS_CONNECTIVITY_LOST",
    "CF_PROVIDER_STATUS_CLEAR_FLAGS",
    "CF_PROVIDER_STATUS_TERMINATED",
    "CF_PROVIDER_STATUS_ERROR",
    "CF_PROCESS_INFO",
    "CF_PLATFORM_INFO",
    "CF_REGISTER_FLAGS",
    "CF_REGISTER_FLAG_NONE",
    "CF_REGISTER_FLAG_UPDATE",
    "CF_REGISTER_FLAG_DISABLE_ON_DEMAND_POPULATION_ON_ROOT",
    "CF_REGISTER_FLAG_MARK_IN_SYNC_ON_ROOT",
    "CF_HYDRATION_POLICY_PRIMARY",
    "CF_HYDRATION_POLICY_PARTIAL",
    "CF_HYDRATION_POLICY_PROGRESSIVE",
    "CF_HYDRATION_POLICY_FULL",
    "CF_HYDRATION_POLICY_ALWAYS_FULL",
    "CF_HYDRATION_POLICY_PRIMARY_USHORT",
    "CF_HYDRATION_POLICY_MODIFIER",
    "CF_HYDRATION_POLICY_MODIFIER_NONE",
    "CF_HYDRATION_POLICY_MODIFIER_VALIDATION_REQUIRED",
    "CF_HYDRATION_POLICY_MODIFIER_STREAMING_ALLOWED",
    "CF_HYDRATION_POLICY_MODIFIER_AUTO_DEHYDRATION_ALLOWED",
    "CF_HYDRATION_POLICY_MODIFIER_ALLOW_FULL_RESTART_HYDRATION",
    "CF_HYDRATION_POLICY_MODIFIER_USHORT",
    "CF_HYDRATION_POLICY",
    "CF_POPULATION_POLICY_PRIMARY",
    "CF_POPULATION_POLICY_PARTIAL",
    "CF_POPULATION_POLICY_FULL",
    "CF_POPULATION_POLICY_ALWAYS_FULL",
    "CF_POPULATION_POLICY_PRIMARY_USHORT",
    "CF_POPULATION_POLICY_MODIFIER",
    "CF_POPULATION_POLICY_MODIFIER_NONE",
    "CF_POPULATION_POLICY_MODIFIER_USHORT",
    "CF_POPULATION_POLICY",
    "CF_PLACEHOLDER_MANAGEMENT_POLICY",
    "CF_PLACEHOLDER_MANAGEMENT_POLICY_DEFAULT",
    "CF_PLACEHOLDER_MANAGEMENT_POLICY_CREATE_UNRESTRICTED",
    "CF_PLACEHOLDER_MANAGEMENT_POLICY_CONVERT_TO_UNRESTRICTED",
    "CF_PLACEHOLDER_MANAGEMENT_POLICY_UPDATE_UNRESTRICTED",
    "CF_INSYNC_POLICY",
    "CF_INSYNC_POLICY_NONE",
    "CF_INSYNC_POLICY_TRACK_FILE_CREATION_TIME",
    "CF_INSYNC_POLICY_TRACK_FILE_READONLY_ATTRIBUTE",
    "CF_INSYNC_POLICY_TRACK_FILE_HIDDEN_ATTRIBUTE",
    "CF_INSYNC_POLICY_TRACK_FILE_SYSTEM_ATTRIBUTE",
    "CF_INSYNC_POLICY_TRACK_DIRECTORY_CREATION_TIME",
    "CF_INSYNC_POLICY_TRACK_DIRECTORY_READONLY_ATTRIBUTE",
    "CF_INSYNC_POLICY_TRACK_DIRECTORY_HIDDEN_ATTRIBUTE",
    "CF_INSYNC_POLICY_TRACK_DIRECTORY_SYSTEM_ATTRIBUTE",
    "CF_INSYNC_POLICY_TRACK_FILE_LAST_WRITE_TIME",
    "CF_INSYNC_POLICY_TRACK_DIRECTORY_LAST_WRITE_TIME",
    "CF_INSYNC_POLICY_TRACK_FILE_ALL",
    "CF_INSYNC_POLICY_TRACK_DIRECTORY_ALL",
    "CF_INSYNC_POLICY_TRACK_ALL",
    "CF_INSYNC_POLICY_PRESERVE_INSYNC_FOR_SYNC_ENGINE",
    "CF_HARDLINK_POLICY",
    "CF_HARDLINK_POLICY_NONE",
    "CF_HARDLINK_POLICY_ALLOWED",
    "CF_SYNC_POLICIES",
    "CF_SYNC_REGISTRATION",
    "CF_CALLBACK_INFO",
    "CF_CALLBACK_CANCEL_FLAGS",
    "CF_CALLBACK_CANCEL_FLAG_NONE",
    "CF_CALLBACK_CANCEL_FLAG_IO_TIMEOUT",
    "CF_CALLBACK_CANCEL_FLAG_IO_ABORTED",
    "CF_CALLBACK_FETCH_DATA_FLAGS",
    "CF_CALLBACK_FETCH_DATA_FLAG_NONE",
    "CF_CALLBACK_FETCH_DATA_FLAG_RECOVERY",
    "CF_CALLBACK_FETCH_DATA_FLAG_EXPLICIT_HYDRATION",
    "CF_CALLBACK_VALIDATE_DATA_FLAGS",
    "CF_CALLBACK_VALIDATE_DATA_FLAG_NONE",
    "CF_CALLBACK_VALIDATE_DATA_FLAG_EXPLICIT_HYDRATION",
    "CF_CALLBACK_FETCH_PLACEHOLDERS_FLAGS",
    "CF_CALLBACK_FETCH_PLACEHOLDERS_FLAG_NONE",
    "CF_CALLBACK_OPEN_COMPLETION_FLAGS",
    "CF_CALLBACK_OPEN_COMPLETION_FLAG_NONE",
    "CF_CALLBACK_OPEN_COMPLETION_FLAG_PLACEHOLDER_UNKNOWN",
    "CF_CALLBACK_OPEN_COMPLETION_FLAG_PLACEHOLDER_UNSUPPORTED",
    "CF_CALLBACK_CLOSE_COMPLETION_FLAGS",
    "CF_CALLBACK_CLOSE_COMPLETION_FLAG_NONE",
    "CF_CALLBACK_CLOSE_COMPLETION_FLAG_DELETED",
    "CF_CALLBACK_DEHYDRATE_FLAGS",
    "CF_CALLBACK_DEHYDRATE_FLAG_NONE",
    "CF_CALLBACK_DEHYDRATE_FLAG_BACKGROUND",
    "CF_CALLBACK_DEHYDRATE_COMPLETION_FLAGS",
    "CF_CALLBACK_DEHYDRATE_COMPLETION_FLAG_NONE",
    "CF_CALLBACK_DEHYDRATE_COMPLETION_FLAG_BACKGROUND",
    "CF_CALLBACK_DEHYDRATE_COMPLETION_FLAG_DEHYDRATED",
    "CF_CALLBACK_DELETE_FLAGS",
    "CF_CALLBACK_DELETE_FLAG_NONE",
    "CF_CALLBACK_DELETE_FLAG_IS_DIRECTORY",
    "CF_CALLBACK_DELETE_FLAG_IS_UNDELETE",
    "CF_CALLBACK_DELETE_COMPLETION_FLAGS",
    "CF_CALLBACK_DELETE_COMPLETION_FLAG_NONE",
    "CF_CALLBACK_RENAME_FLAGS",
    "CF_CALLBACK_RENAME_FLAG_NONE",
    "CF_CALLBACK_RENAME_FLAG_IS_DIRECTORY",
    "CF_CALLBACK_RENAME_FLAG_SOURCE_IN_SCOPE",
    "CF_CALLBACK_RENAME_FLAG_TARGET_IN_SCOPE",
    "CF_CALLBACK_RENAME_COMPLETION_FLAGS",
    "CF_CALLBACK_RENAME_COMPLETION_FLAG_NONE",
    "CF_CALLBACK_DEHYDRATION_REASON",
    "CF_CALLBACK_DEHYDRATION_REASON_NONE",
    "CF_CALLBACK_DEHYDRATION_REASON_USER_MANUAL",
    "CF_CALLBACK_DEHYDRATION_REASON_SYSTEM_LOW_SPACE",
    "CF_CALLBACK_DEHYDRATION_REASON_SYSTEM_INACTIVITY",
    "CF_CALLBACK_DEHYDRATION_REASON_SYSTEM_OS_UPGRADE",
    "CF_CALLBACK_PARAMETERS",
    "CF_CALLBACK",
    "CF_CALLBACK_TYPE",
    "CF_CALLBACK_TYPE_FETCH_DATA",
    "CF_CALLBACK_TYPE_VALIDATE_DATA",
    "CF_CALLBACK_TYPE_CANCEL_FETCH_DATA",
    "CF_CALLBACK_TYPE_FETCH_PLACEHOLDERS",
    "CF_CALLBACK_TYPE_CANCEL_FETCH_PLACEHOLDERS",
    "CF_CALLBACK_TYPE_NOTIFY_FILE_OPEN_COMPLETION",
    "CF_CALLBACK_TYPE_NOTIFY_FILE_CLOSE_COMPLETION",
    "CF_CALLBACK_TYPE_NOTIFY_DEHYDRATE",
    "CF_CALLBACK_TYPE_NOTIFY_DEHYDRATE_COMPLETION",
    "CF_CALLBACK_TYPE_NOTIFY_DELETE",
    "CF_CALLBACK_TYPE_NOTIFY_DELETE_COMPLETION",
    "CF_CALLBACK_TYPE_NOTIFY_RENAME",
    "CF_CALLBACK_TYPE_NOTIFY_RENAME_COMPLETION",
    "CF_CALLBACK_TYPE_NONE",
    "CF_CALLBACK_REGISTRATION",
    "CF_CONNECT_FLAGS",
    "CF_CONNECT_FLAG_NONE",
    "CF_CONNECT_FLAG_REQUIRE_PROCESS_INFO",
    "CF_CONNECT_FLAG_REQUIRE_FULL_FILE_PATH",
    "CF_CONNECT_FLAG_BLOCK_SELF_IMPLICIT_HYDRATION",
    "CF_OPERATION_TYPE",
    "CF_OPERATION_TYPE_TRANSFER_DATA",
    "CF_OPERATION_TYPE_RETRIEVE_DATA",
    "CF_OPERATION_TYPE_ACK_DATA",
    "CF_OPERATION_TYPE_RESTART_HYDRATION",
    "CF_OPERATION_TYPE_TRANSFER_PLACEHOLDERS",
    "CF_OPERATION_TYPE_ACK_DEHYDRATE",
    "CF_OPERATION_TYPE_ACK_DELETE",
    "CF_OPERATION_TYPE_ACK_RENAME",
    "CF_SYNC_STATUS",
    "CF_OPERATION_INFO",
    "CF_OPERATION_TRANSFER_DATA_FLAGS",
    "CF_OPERATION_TRANSFER_DATA_FLAG_NONE",
    "CF_OPERATION_RETRIEVE_DATA_FLAGS",
    "CF_OPERATION_RETRIEVE_DATA_FLAG_NONE",
    "CF_OPERATION_ACK_DATA_FLAGS",
    "CF_OPERATION_ACK_DATA_FLAG_NONE",
    "CF_OPERATION_RESTART_HYDRATION_FLAGS",
    "CF_OPERATION_RESTART_HYDRATION_FLAG_NONE",
    "CF_OPERATION_RESTART_HYDRATION_FLAG_MARK_IN_SYNC",
    "CF_OPERATION_TRANSFER_PLACEHOLDERS_FLAGS",
    "CF_OPERATION_TRANSFER_PLACEHOLDERS_FLAG_NONE",
    "CF_OPERATION_TRANSFER_PLACEHOLDERS_FLAG_STOP_ON_ERROR",
    "CF_OPERATION_TRANSFER_PLACEHOLDERS_FLAG_DISABLE_ON_DEMAND_POPULATION",
    "CF_OPERATION_ACK_DEHYDRATE_FLAGS",
    "CF_OPERATION_ACK_DEHYDRATE_FLAG_NONE",
    "CF_OPERATION_ACK_RENAME_FLAGS",
    "CF_OPERATION_ACK_RENAME_FLAG_NONE",
    "CF_OPERATION_ACK_DELETE_FLAGS",
    "CF_OPERATION_ACK_DELETE_FLAG_NONE",
    "CF_OPERATION_PARAMETERS",
    "CF_CREATE_FLAGS",
    "CF_CREATE_FLAG_NONE",
    "CF_CREATE_FLAG_STOP_ON_ERROR",
    "CF_OPEN_FILE_FLAGS",
    "CF_OPEN_FILE_FLAG_NONE",
    "CF_OPEN_FILE_FLAG_EXCLUSIVE",
    "CF_OPEN_FILE_FLAG_WRITE_ACCESS",
    "CF_OPEN_FILE_FLAG_DELETE_ACCESS",
    "CF_OPEN_FILE_FLAG_FOREGROUND",
    "CF_FILE_RANGE",
    "CF_CONVERT_FLAGS",
    "CF_CONVERT_FLAG_NONE",
    "CF_CONVERT_FLAG_MARK_IN_SYNC",
    "CF_CONVERT_FLAG_DEHYDRATE",
    "CF_CONVERT_FLAG_ENABLE_ON_DEMAND_POPULATION",
    "CF_CONVERT_FLAG_ALWAYS_FULL",
    "CF_CONVERT_FLAG_FORCE_CONVERT_TO_CLOUD_FILE",
    "CF_UPDATE_FLAGS",
    "CF_UPDATE_FLAG_NONE",
    "CF_UPDATE_FLAG_VERIFY_IN_SYNC",
    "CF_UPDATE_FLAG_MARK_IN_SYNC",
    "CF_UPDATE_FLAG_DEHYDRATE",
    "CF_UPDATE_FLAG_ENABLE_ON_DEMAND_POPULATION",
    "CF_UPDATE_FLAG_DISABLE_ON_DEMAND_POPULATION",
    "CF_UPDATE_FLAG_REMOVE_FILE_IDENTITY",
    "CF_UPDATE_FLAG_CLEAR_IN_SYNC",
    "CF_UPDATE_FLAG_REMOVE_PROPERTY",
    "CF_UPDATE_FLAG_PASSTHROUGH_FS_METADATA",
    "CF_UPDATE_FLAG_ALWAYS_FULL",
    "CF_UPDATE_FLAG_ALLOW_PARTIAL",
    "CF_REVERT_FLAGS",
    "CF_REVERT_FLAG_NONE",
    "CF_HYDRATE_FLAGS",
    "CF_HYDRATE_FLAG_NONE",
    "CF_DEHYDRATE_FLAGS",
    "CF_DEHYDRATE_FLAG_NONE",
    "CF_DEHYDRATE_FLAG_BACKGROUND",
    "CF_PIN_STATE",
    "CF_PIN_STATE_UNSPECIFIED",
    "CF_PIN_STATE_PINNED",
    "CF_PIN_STATE_UNPINNED",
    "CF_PIN_STATE_EXCLUDED",
    "CF_PIN_STATE_INHERIT",
    "CF_SET_PIN_FLAGS",
    "CF_SET_PIN_FLAG_NONE",
    "CF_SET_PIN_FLAG_RECURSE",
    "CF_SET_PIN_FLAG_RECURSE_ONLY",
    "CF_SET_PIN_FLAG_RECURSE_STOP_ON_ERROR",
    "CF_IN_SYNC_STATE",
    "CF_IN_SYNC_STATE_NOT_IN_SYNC",
    "CF_IN_SYNC_STATE_IN_SYNC",
    "CF_SET_IN_SYNC_FLAGS",
    "CF_SET_IN_SYNC_FLAG_NONE",
    "CF_PLACEHOLDER_STATE",
    "CF_PLACEHOLDER_STATE_NO_STATES",
    "CF_PLACEHOLDER_STATE_PLACEHOLDER",
    "CF_PLACEHOLDER_STATE_SYNC_ROOT",
    "CF_PLACEHOLDER_STATE_ESSENTIAL_PROP_PRESENT",
    "CF_PLACEHOLDER_STATE_IN_SYNC",
    "CF_PLACEHOLDER_STATE_PARTIAL",
    "CF_PLACEHOLDER_STATE_PARTIALLY_ON_DISK",
    "CF_PLACEHOLDER_STATE_INVALID",
    "CF_PLACEHOLDER_INFO_CLASS",
    "CF_PLACEHOLDER_INFO_BASIC",
    "CF_PLACEHOLDER_INFO_STANDARD",
    "CF_PLACEHOLDER_BASIC_INFO",
    "CF_PLACEHOLDER_STANDARD_INFO",
    "CF_SYNC_ROOT_INFO_CLASS",
    "CF_SYNC_ROOT_INFO_BASIC",
    "CF_SYNC_ROOT_INFO_STANDARD",
    "CF_SYNC_ROOT_INFO_PROVIDER",
    "CF_SYNC_ROOT_BASIC_INFO",
    "CF_SYNC_ROOT_PROVIDER_INFO",
    "CF_SYNC_ROOT_STANDARD_INFO",
    "CF_PLACEHOLDER_RANGE_INFO_CLASS",
    "CF_PLACEHOLDER_RANGE_INFO_ONDISK",
    "CF_PLACEHOLDER_RANGE_INFO_VALIDATED",
    "CF_PLACEHOLDER_RANGE_INFO_MODIFIED",
    "CfGetPlatformInfo",
    "CfRegisterSyncRoot",
    "CfUnregisterSyncRoot",
    "CfConnectSyncRoot",
    "CfDisconnectSyncRoot",
    "CfGetTransferKey",
    "CfReleaseTransferKey",
    "CfExecute",
    "CfUpdateSyncProviderStatus",
    "CfQuerySyncProviderStatus",
    "CfReportSyncStatus",
    "CfCreatePlaceholders",
    "CfOpenFileWithOplock",
    "CfReferenceProtectedHandle",
    "CfGetWin32HandleFromProtectedHandle",
    "CfReleaseProtectedHandle",
    "CfCloseHandle",
    "CfConvertToPlaceholder",
    "CfUpdatePlaceholder",
    "CfRevertPlaceholder",
    "CfHydratePlaceholder",
    "CfDehydratePlaceholder",
    "CfSetPinState",
    "CfSetInSyncState",
    "CfSetCorrelationVector",
    "CfGetCorrelationVector",
    "CfGetPlaceholderStateFromAttributeTag",
    "CfGetPlaceholderStateFromFileInfo",
    "CfGetPlaceholderStateFromFindData",
    "CfGetPlaceholderInfo",
    "CfGetSyncRootInfoByPath",
    "CfGetSyncRootInfoByHandle",
    "CfGetPlaceholderRangeInfo",
    "CfReportProviderProgress",
    "CfReportProviderProgress2",
]
