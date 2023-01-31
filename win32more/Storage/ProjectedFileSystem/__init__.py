from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Storage.ProjectedFileSystem
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
@winfunctype('PROJECTEDFSLIB.dll')
def PrjStartVirtualizing(virtualizationRootPath: win32more.Foundation.PWSTR, callbacks: POINTER(win32more.Storage.ProjectedFileSystem.PRJ_CALLBACKS_head), instanceContext: c_void_p, options: POINTER(win32more.Storage.ProjectedFileSystem.PRJ_STARTVIRTUALIZING_OPTIONS_head), namespaceVirtualizationContext: POINTER(win32more.Storage.ProjectedFileSystem.PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjStopVirtualizing(namespaceVirtualizationContext: win32more.Storage.ProjectedFileSystem.PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT) -> Void: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjClearNegativePathCache(namespaceVirtualizationContext: win32more.Storage.ProjectedFileSystem.PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT, totalEntryNumber: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjGetVirtualizationInstanceInfo(namespaceVirtualizationContext: win32more.Storage.ProjectedFileSystem.PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT, virtualizationInstanceInfo: POINTER(win32more.Storage.ProjectedFileSystem.PRJ_VIRTUALIZATION_INSTANCE_INFO_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjMarkDirectoryAsPlaceholder(rootPathName: win32more.Foundation.PWSTR, targetPathName: win32more.Foundation.PWSTR, versionInfo: POINTER(win32more.Storage.ProjectedFileSystem.PRJ_PLACEHOLDER_VERSION_INFO_head), virtualizationInstanceID: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjWritePlaceholderInfo(namespaceVirtualizationContext: win32more.Storage.ProjectedFileSystem.PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT, destinationFileName: win32more.Foundation.PWSTR, placeholderInfo: POINTER(win32more.Storage.ProjectedFileSystem.PRJ_PLACEHOLDER_INFO_head), placeholderInfoSize: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjWritePlaceholderInfo2(namespaceVirtualizationContext: win32more.Storage.ProjectedFileSystem.PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT, destinationFileName: win32more.Foundation.PWSTR, placeholderInfo: POINTER(win32more.Storage.ProjectedFileSystem.PRJ_PLACEHOLDER_INFO_head), placeholderInfoSize: UInt32, ExtendedInfo: POINTER(win32more.Storage.ProjectedFileSystem.PRJ_EXTENDED_INFO_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjUpdateFileIfNeeded(namespaceVirtualizationContext: win32more.Storage.ProjectedFileSystem.PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT, destinationFileName: win32more.Foundation.PWSTR, placeholderInfo: POINTER(win32more.Storage.ProjectedFileSystem.PRJ_PLACEHOLDER_INFO_head), placeholderInfoSize: UInt32, updateFlags: win32more.Storage.ProjectedFileSystem.PRJ_UPDATE_TYPES, failureReason: POINTER(win32more.Storage.ProjectedFileSystem.PRJ_UPDATE_FAILURE_CAUSES)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjDeleteFile(namespaceVirtualizationContext: win32more.Storage.ProjectedFileSystem.PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT, destinationFileName: win32more.Foundation.PWSTR, updateFlags: win32more.Storage.ProjectedFileSystem.PRJ_UPDATE_TYPES, failureReason: POINTER(win32more.Storage.ProjectedFileSystem.PRJ_UPDATE_FAILURE_CAUSES)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjWriteFileData(namespaceVirtualizationContext: win32more.Storage.ProjectedFileSystem.PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT, dataStreamId: POINTER(Guid), buffer: c_void_p, byteOffset: UInt64, length: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjGetOnDiskFileState(destinationFileName: win32more.Foundation.PWSTR, fileState: POINTER(win32more.Storage.ProjectedFileSystem.PRJ_FILE_STATE)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjAllocateAlignedBuffer(namespaceVirtualizationContext: win32more.Storage.ProjectedFileSystem.PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT, size: UIntPtr) -> c_void_p: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjFreeAlignedBuffer(buffer: c_void_p) -> Void: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjCompleteCommand(namespaceVirtualizationContext: win32more.Storage.ProjectedFileSystem.PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT, commandId: Int32, completionResult: win32more.Foundation.HRESULT, extendedParameters: POINTER(win32more.Storage.ProjectedFileSystem.PRJ_COMPLETE_COMMAND_EXTENDED_PARAMETERS_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjFillDirEntryBuffer(fileName: win32more.Foundation.PWSTR, fileBasicInfo: POINTER(win32more.Storage.ProjectedFileSystem.PRJ_FILE_BASIC_INFO_head), dirEntryBufferHandle: win32more.Storage.ProjectedFileSystem.PRJ_DIR_ENTRY_BUFFER_HANDLE) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjFillDirEntryBuffer2(dirEntryBufferHandle: win32more.Storage.ProjectedFileSystem.PRJ_DIR_ENTRY_BUFFER_HANDLE, fileName: win32more.Foundation.PWSTR, fileBasicInfo: POINTER(win32more.Storage.ProjectedFileSystem.PRJ_FILE_BASIC_INFO_head), extendedInfo: POINTER(win32more.Storage.ProjectedFileSystem.PRJ_EXTENDED_INFO_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjFileNameMatch(fileNameToCheck: win32more.Foundation.PWSTR, pattern: win32more.Foundation.PWSTR) -> win32more.Foundation.BOOLEAN: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjFileNameCompare(fileName1: win32more.Foundation.PWSTR, fileName2: win32more.Foundation.PWSTR) -> Int32: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjDoesNameContainWildCards(fileName: win32more.Foundation.PWSTR) -> win32more.Foundation.BOOLEAN: ...
class PRJ_CALLBACKS(Structure):
    StartDirectoryEnumerationCallback: win32more.Storage.ProjectedFileSystem.PRJ_START_DIRECTORY_ENUMERATION_CB
    EndDirectoryEnumerationCallback: win32more.Storage.ProjectedFileSystem.PRJ_END_DIRECTORY_ENUMERATION_CB
    GetDirectoryEnumerationCallback: win32more.Storage.ProjectedFileSystem.PRJ_GET_DIRECTORY_ENUMERATION_CB
    GetPlaceholderInfoCallback: win32more.Storage.ProjectedFileSystem.PRJ_GET_PLACEHOLDER_INFO_CB
    GetFileDataCallback: win32more.Storage.ProjectedFileSystem.PRJ_GET_FILE_DATA_CB
    QueryFileNameCallback: win32more.Storage.ProjectedFileSystem.PRJ_QUERY_FILE_NAME_CB
    NotificationCallback: win32more.Storage.ProjectedFileSystem.PRJ_NOTIFICATION_CB
    CancelCommandCallback: win32more.Storage.ProjectedFileSystem.PRJ_CANCEL_COMMAND_CB
class PRJ_CALLBACK_DATA(Structure):
    Size: UInt32
    Flags: win32more.Storage.ProjectedFileSystem.PRJ_CALLBACK_DATA_FLAGS
    NamespaceVirtualizationContext: win32more.Storage.ProjectedFileSystem.PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT
    CommandId: Int32
    FileId: Guid
    DataStreamId: Guid
    FilePathName: win32more.Foundation.PWSTR
    VersionInfo: POINTER(win32more.Storage.ProjectedFileSystem.PRJ_PLACEHOLDER_VERSION_INFO_head)
    TriggeringProcessId: UInt32
    TriggeringProcessImageFileName: win32more.Foundation.PWSTR
    InstanceContext: c_void_p
PRJ_CALLBACK_DATA_FLAGS = Int32
PRJ_CB_DATA_FLAG_ENUM_RESTART_SCAN: PRJ_CALLBACK_DATA_FLAGS = 1
PRJ_CB_DATA_FLAG_ENUM_RETURN_SINGLE_ENTRY: PRJ_CALLBACK_DATA_FLAGS = 2
@winfunctype_pointer
def PRJ_CANCEL_COMMAND_CB(callbackData: POINTER(win32more.Storage.ProjectedFileSystem.PRJ_CALLBACK_DATA_head)) -> Void: ...
class PRJ_COMPLETE_COMMAND_EXTENDED_PARAMETERS(Structure):
    CommandType: win32more.Storage.ProjectedFileSystem.PRJ_COMPLETE_COMMAND_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Notification: _Notification_e__Struct
        Enumeration: _Enumeration_e__Struct
        class _Notification_e__Struct(Structure):
            NotificationMask: win32more.Storage.ProjectedFileSystem.PRJ_NOTIFY_TYPES
        class _Enumeration_e__Struct(Structure):
            DirEntryBufferHandle: win32more.Storage.ProjectedFileSystem.PRJ_DIR_ENTRY_BUFFER_HANDLE
PRJ_COMPLETE_COMMAND_TYPE = Int32
PRJ_COMPLETE_COMMAND_TYPE_NOTIFICATION: PRJ_COMPLETE_COMMAND_TYPE = 1
PRJ_COMPLETE_COMMAND_TYPE_ENUMERATION: PRJ_COMPLETE_COMMAND_TYPE = 2
PRJ_DIR_ENTRY_BUFFER_HANDLE = IntPtr
@winfunctype_pointer
def PRJ_END_DIRECTORY_ENUMERATION_CB(callbackData: POINTER(win32more.Storage.ProjectedFileSystem.PRJ_CALLBACK_DATA_head), enumerationId: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
class PRJ_EXTENDED_INFO(Structure):
    InfoType: win32more.Storage.ProjectedFileSystem.PRJ_EXT_INFO_TYPE
    NextInfoOffset: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Symlink: _Symlink_e__Struct
        class _Symlink_e__Struct(Structure):
            TargetName: win32more.Foundation.PWSTR
PRJ_EXT_INFO_TYPE = Int32
PRJ_EXT_INFO_TYPE_SYMLINK: PRJ_EXT_INFO_TYPE = 1
class PRJ_FILE_BASIC_INFO(Structure):
    IsDirectory: win32more.Foundation.BOOLEAN
    FileSize: Int64
    CreationTime: win32more.Foundation.LARGE_INTEGER
    LastAccessTime: win32more.Foundation.LARGE_INTEGER
    LastWriteTime: win32more.Foundation.LARGE_INTEGER
    ChangeTime: win32more.Foundation.LARGE_INTEGER
    FileAttributes: UInt32
PRJ_FILE_STATE = UInt32
PRJ_FILE_STATE_PLACEHOLDER: PRJ_FILE_STATE = 1
PRJ_FILE_STATE_HYDRATED_PLACEHOLDER: PRJ_FILE_STATE = 2
PRJ_FILE_STATE_DIRTY_PLACEHOLDER: PRJ_FILE_STATE = 4
PRJ_FILE_STATE_FULL: PRJ_FILE_STATE = 8
PRJ_FILE_STATE_TOMBSTONE: PRJ_FILE_STATE = 16
@winfunctype_pointer
def PRJ_GET_DIRECTORY_ENUMERATION_CB(callbackData: POINTER(win32more.Storage.ProjectedFileSystem.PRJ_CALLBACK_DATA_head), enumerationId: POINTER(Guid), searchExpression: win32more.Foundation.PWSTR, dirEntryBufferHandle: win32more.Storage.ProjectedFileSystem.PRJ_DIR_ENTRY_BUFFER_HANDLE) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def PRJ_GET_FILE_DATA_CB(callbackData: POINTER(win32more.Storage.ProjectedFileSystem.PRJ_CALLBACK_DATA_head), byteOffset: UInt64, length: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def PRJ_GET_PLACEHOLDER_INFO_CB(callbackData: POINTER(win32more.Storage.ProjectedFileSystem.PRJ_CALLBACK_DATA_head)) -> win32more.Foundation.HRESULT: ...
PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT = IntPtr
PRJ_NOTIFICATION = Int32
PRJ_NOTIFICATION_FILE_OPENED: PRJ_NOTIFICATION = 2
PRJ_NOTIFICATION_NEW_FILE_CREATED: PRJ_NOTIFICATION = 4
PRJ_NOTIFICATION_FILE_OVERWRITTEN: PRJ_NOTIFICATION = 8
PRJ_NOTIFICATION_PRE_DELETE: PRJ_NOTIFICATION = 16
PRJ_NOTIFICATION_PRE_RENAME: PRJ_NOTIFICATION = 32
PRJ_NOTIFICATION_PRE_SET_HARDLINK: PRJ_NOTIFICATION = 64
PRJ_NOTIFICATION_FILE_RENAMED: PRJ_NOTIFICATION = 128
PRJ_NOTIFICATION_HARDLINK_CREATED: PRJ_NOTIFICATION = 256
PRJ_NOTIFICATION_FILE_HANDLE_CLOSED_NO_MODIFICATION: PRJ_NOTIFICATION = 512
PRJ_NOTIFICATION_FILE_HANDLE_CLOSED_FILE_MODIFIED: PRJ_NOTIFICATION = 1024
PRJ_NOTIFICATION_FILE_HANDLE_CLOSED_FILE_DELETED: PRJ_NOTIFICATION = 2048
PRJ_NOTIFICATION_FILE_PRE_CONVERT_TO_FULL: PRJ_NOTIFICATION = 4096
@winfunctype_pointer
def PRJ_NOTIFICATION_CB(callbackData: POINTER(win32more.Storage.ProjectedFileSystem.PRJ_CALLBACK_DATA_head), isDirectory: win32more.Foundation.BOOLEAN, notification: win32more.Storage.ProjectedFileSystem.PRJ_NOTIFICATION, destinationFileName: win32more.Foundation.PWSTR, operationParameters: POINTER(win32more.Storage.ProjectedFileSystem.PRJ_NOTIFICATION_PARAMETERS_head)) -> win32more.Foundation.HRESULT: ...
class PRJ_NOTIFICATION_MAPPING(Structure):
    NotificationBitMask: win32more.Storage.ProjectedFileSystem.PRJ_NOTIFY_TYPES
    NotificationRoot: win32more.Foundation.PWSTR
class PRJ_NOTIFICATION_PARAMETERS(Union):
    PostCreate: _PostCreate_e__Struct
    FileRenamed: _FileRenamed_e__Struct
    FileDeletedOnHandleClose: _FileDeletedOnHandleClose_e__Struct
    class _PostCreate_e__Struct(Structure):
        NotificationMask: win32more.Storage.ProjectedFileSystem.PRJ_NOTIFY_TYPES
    class _FileRenamed_e__Struct(Structure):
        NotificationMask: win32more.Storage.ProjectedFileSystem.PRJ_NOTIFY_TYPES
    class _FileDeletedOnHandleClose_e__Struct(Structure):
        IsFileModified: win32more.Foundation.BOOLEAN
PRJ_NOTIFY_TYPES = UInt32
PRJ_NOTIFY_NONE: PRJ_NOTIFY_TYPES = 0
PRJ_NOTIFY_SUPPRESS_NOTIFICATIONS: PRJ_NOTIFY_TYPES = 1
PRJ_NOTIFY_FILE_OPENED: PRJ_NOTIFY_TYPES = 2
PRJ_NOTIFY_NEW_FILE_CREATED: PRJ_NOTIFY_TYPES = 4
PRJ_NOTIFY_FILE_OVERWRITTEN: PRJ_NOTIFY_TYPES = 8
PRJ_NOTIFY_PRE_DELETE: PRJ_NOTIFY_TYPES = 16
PRJ_NOTIFY_PRE_RENAME: PRJ_NOTIFY_TYPES = 32
PRJ_NOTIFY_PRE_SET_HARDLINK: PRJ_NOTIFY_TYPES = 64
PRJ_NOTIFY_FILE_RENAMED: PRJ_NOTIFY_TYPES = 128
PRJ_NOTIFY_HARDLINK_CREATED: PRJ_NOTIFY_TYPES = 256
PRJ_NOTIFY_FILE_HANDLE_CLOSED_NO_MODIFICATION: PRJ_NOTIFY_TYPES = 512
PRJ_NOTIFY_FILE_HANDLE_CLOSED_FILE_MODIFIED: PRJ_NOTIFY_TYPES = 1024
PRJ_NOTIFY_FILE_HANDLE_CLOSED_FILE_DELETED: PRJ_NOTIFY_TYPES = 2048
PRJ_NOTIFY_FILE_PRE_CONVERT_TO_FULL: PRJ_NOTIFY_TYPES = 4096
PRJ_NOTIFY_USE_EXISTING_MASK: PRJ_NOTIFY_TYPES = 4294967295
PRJ_PLACEHOLDER_ID = Int32
PRJ_PLACEHOLDER_ID_LENGTH: PRJ_PLACEHOLDER_ID = 128
class PRJ_PLACEHOLDER_INFO(Structure):
    FileBasicInfo: win32more.Storage.ProjectedFileSystem.PRJ_FILE_BASIC_INFO
    EaInformation: _EaInformation_e__Struct
    SecurityInformation: _SecurityInformation_e__Struct
    StreamsInformation: _StreamsInformation_e__Struct
    VersionInfo: win32more.Storage.ProjectedFileSystem.PRJ_PLACEHOLDER_VERSION_INFO
    VariableData: Byte * 1
    class _EaInformation_e__Struct(Structure):
        EaBufferSize: UInt32
        OffsetToFirstEa: UInt32
    class _SecurityInformation_e__Struct(Structure):
        SecurityBufferSize: UInt32
        OffsetToSecurityDescriptor: UInt32
    class _StreamsInformation_e__Struct(Structure):
        StreamsInfoBufferSize: UInt32
        OffsetToFirstStreamInfo: UInt32
class PRJ_PLACEHOLDER_VERSION_INFO(Structure):
    ProviderID: Byte * 128
    ContentID: Byte * 128
@winfunctype_pointer
def PRJ_QUERY_FILE_NAME_CB(callbackData: POINTER(win32more.Storage.ProjectedFileSystem.PRJ_CALLBACK_DATA_head)) -> win32more.Foundation.HRESULT: ...
PRJ_STARTVIRTUALIZING_FLAGS = UInt32
PRJ_FLAG_NONE: PRJ_STARTVIRTUALIZING_FLAGS = 0
PRJ_FLAG_USE_NEGATIVE_PATH_CACHE: PRJ_STARTVIRTUALIZING_FLAGS = 1
class PRJ_STARTVIRTUALIZING_OPTIONS(Structure):
    Flags: win32more.Storage.ProjectedFileSystem.PRJ_STARTVIRTUALIZING_FLAGS
    PoolThreadCount: UInt32
    ConcurrentThreadCount: UInt32
    NotificationMappings: POINTER(win32more.Storage.ProjectedFileSystem.PRJ_NOTIFICATION_MAPPING_head)
    NotificationMappingsCount: UInt32
@winfunctype_pointer
def PRJ_START_DIRECTORY_ENUMERATION_CB(callbackData: POINTER(win32more.Storage.ProjectedFileSystem.PRJ_CALLBACK_DATA_head), enumerationId: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
PRJ_UPDATE_FAILURE_CAUSES = UInt32
PRJ_UPDATE_FAILURE_CAUSE_NONE: PRJ_UPDATE_FAILURE_CAUSES = 0
PRJ_UPDATE_FAILURE_CAUSE_DIRTY_METADATA: PRJ_UPDATE_FAILURE_CAUSES = 1
PRJ_UPDATE_FAILURE_CAUSE_DIRTY_DATA: PRJ_UPDATE_FAILURE_CAUSES = 2
PRJ_UPDATE_FAILURE_CAUSE_TOMBSTONE: PRJ_UPDATE_FAILURE_CAUSES = 4
PRJ_UPDATE_FAILURE_CAUSE_READ_ONLY: PRJ_UPDATE_FAILURE_CAUSES = 8
PRJ_UPDATE_TYPES = UInt32
PRJ_UPDATE_NONE: PRJ_UPDATE_TYPES = 0
PRJ_UPDATE_ALLOW_DIRTY_METADATA: PRJ_UPDATE_TYPES = 1
PRJ_UPDATE_ALLOW_DIRTY_DATA: PRJ_UPDATE_TYPES = 2
PRJ_UPDATE_ALLOW_TOMBSTONE: PRJ_UPDATE_TYPES = 4
PRJ_UPDATE_RESERVED1: PRJ_UPDATE_TYPES = 8
PRJ_UPDATE_RESERVED2: PRJ_UPDATE_TYPES = 16
PRJ_UPDATE_ALLOW_READ_ONLY: PRJ_UPDATE_TYPES = 32
PRJ_UPDATE_MAX_VAL: PRJ_UPDATE_TYPES = 64
class PRJ_VIRTUALIZATION_INSTANCE_INFO(Structure):
    InstanceID: Guid
    WriteAlignment: UInt32
make_head(_module, 'PRJ_CALLBACKS')
make_head(_module, 'PRJ_CALLBACK_DATA')
make_head(_module, 'PRJ_CANCEL_COMMAND_CB')
make_head(_module, 'PRJ_COMPLETE_COMMAND_EXTENDED_PARAMETERS')
make_head(_module, 'PRJ_END_DIRECTORY_ENUMERATION_CB')
make_head(_module, 'PRJ_EXTENDED_INFO')
make_head(_module, 'PRJ_FILE_BASIC_INFO')
make_head(_module, 'PRJ_GET_DIRECTORY_ENUMERATION_CB')
make_head(_module, 'PRJ_GET_FILE_DATA_CB')
make_head(_module, 'PRJ_GET_PLACEHOLDER_INFO_CB')
make_head(_module, 'PRJ_NOTIFICATION_CB')
make_head(_module, 'PRJ_NOTIFICATION_MAPPING')
make_head(_module, 'PRJ_NOTIFICATION_PARAMETERS')
make_head(_module, 'PRJ_PLACEHOLDER_INFO')
make_head(_module, 'PRJ_PLACEHOLDER_VERSION_INFO')
make_head(_module, 'PRJ_QUERY_FILE_NAME_CB')
make_head(_module, 'PRJ_STARTVIRTUALIZING_OPTIONS')
make_head(_module, 'PRJ_START_DIRECTORY_ENUMERATION_CB')
make_head(_module, 'PRJ_VIRTUALIZATION_INSTANCE_INFO')
__all__ = [
    "PRJ_CALLBACKS",
    "PRJ_CALLBACK_DATA",
    "PRJ_CALLBACK_DATA_FLAGS",
    "PRJ_CANCEL_COMMAND_CB",
    "PRJ_CB_DATA_FLAG_ENUM_RESTART_SCAN",
    "PRJ_CB_DATA_FLAG_ENUM_RETURN_SINGLE_ENTRY",
    "PRJ_COMPLETE_COMMAND_EXTENDED_PARAMETERS",
    "PRJ_COMPLETE_COMMAND_TYPE",
    "PRJ_COMPLETE_COMMAND_TYPE_ENUMERATION",
    "PRJ_COMPLETE_COMMAND_TYPE_NOTIFICATION",
    "PRJ_DIR_ENTRY_BUFFER_HANDLE",
    "PRJ_END_DIRECTORY_ENUMERATION_CB",
    "PRJ_EXTENDED_INFO",
    "PRJ_EXT_INFO_TYPE",
    "PRJ_EXT_INFO_TYPE_SYMLINK",
    "PRJ_FILE_BASIC_INFO",
    "PRJ_FILE_STATE",
    "PRJ_FILE_STATE_DIRTY_PLACEHOLDER",
    "PRJ_FILE_STATE_FULL",
    "PRJ_FILE_STATE_HYDRATED_PLACEHOLDER",
    "PRJ_FILE_STATE_PLACEHOLDER",
    "PRJ_FILE_STATE_TOMBSTONE",
    "PRJ_FLAG_NONE",
    "PRJ_FLAG_USE_NEGATIVE_PATH_CACHE",
    "PRJ_GET_DIRECTORY_ENUMERATION_CB",
    "PRJ_GET_FILE_DATA_CB",
    "PRJ_GET_PLACEHOLDER_INFO_CB",
    "PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT",
    "PRJ_NOTIFICATION",
    "PRJ_NOTIFICATION_CB",
    "PRJ_NOTIFICATION_FILE_HANDLE_CLOSED_FILE_DELETED",
    "PRJ_NOTIFICATION_FILE_HANDLE_CLOSED_FILE_MODIFIED",
    "PRJ_NOTIFICATION_FILE_HANDLE_CLOSED_NO_MODIFICATION",
    "PRJ_NOTIFICATION_FILE_OPENED",
    "PRJ_NOTIFICATION_FILE_OVERWRITTEN",
    "PRJ_NOTIFICATION_FILE_PRE_CONVERT_TO_FULL",
    "PRJ_NOTIFICATION_FILE_RENAMED",
    "PRJ_NOTIFICATION_HARDLINK_CREATED",
    "PRJ_NOTIFICATION_MAPPING",
    "PRJ_NOTIFICATION_NEW_FILE_CREATED",
    "PRJ_NOTIFICATION_PARAMETERS",
    "PRJ_NOTIFICATION_PRE_DELETE",
    "PRJ_NOTIFICATION_PRE_RENAME",
    "PRJ_NOTIFICATION_PRE_SET_HARDLINK",
    "PRJ_NOTIFY_FILE_HANDLE_CLOSED_FILE_DELETED",
    "PRJ_NOTIFY_FILE_HANDLE_CLOSED_FILE_MODIFIED",
    "PRJ_NOTIFY_FILE_HANDLE_CLOSED_NO_MODIFICATION",
    "PRJ_NOTIFY_FILE_OPENED",
    "PRJ_NOTIFY_FILE_OVERWRITTEN",
    "PRJ_NOTIFY_FILE_PRE_CONVERT_TO_FULL",
    "PRJ_NOTIFY_FILE_RENAMED",
    "PRJ_NOTIFY_HARDLINK_CREATED",
    "PRJ_NOTIFY_NEW_FILE_CREATED",
    "PRJ_NOTIFY_NONE",
    "PRJ_NOTIFY_PRE_DELETE",
    "PRJ_NOTIFY_PRE_RENAME",
    "PRJ_NOTIFY_PRE_SET_HARDLINK",
    "PRJ_NOTIFY_SUPPRESS_NOTIFICATIONS",
    "PRJ_NOTIFY_TYPES",
    "PRJ_NOTIFY_USE_EXISTING_MASK",
    "PRJ_PLACEHOLDER_ID",
    "PRJ_PLACEHOLDER_ID_LENGTH",
    "PRJ_PLACEHOLDER_INFO",
    "PRJ_PLACEHOLDER_VERSION_INFO",
    "PRJ_QUERY_FILE_NAME_CB",
    "PRJ_STARTVIRTUALIZING_FLAGS",
    "PRJ_STARTVIRTUALIZING_OPTIONS",
    "PRJ_START_DIRECTORY_ENUMERATION_CB",
    "PRJ_UPDATE_ALLOW_DIRTY_DATA",
    "PRJ_UPDATE_ALLOW_DIRTY_METADATA",
    "PRJ_UPDATE_ALLOW_READ_ONLY",
    "PRJ_UPDATE_ALLOW_TOMBSTONE",
    "PRJ_UPDATE_FAILURE_CAUSES",
    "PRJ_UPDATE_FAILURE_CAUSE_DIRTY_DATA",
    "PRJ_UPDATE_FAILURE_CAUSE_DIRTY_METADATA",
    "PRJ_UPDATE_FAILURE_CAUSE_NONE",
    "PRJ_UPDATE_FAILURE_CAUSE_READ_ONLY",
    "PRJ_UPDATE_FAILURE_CAUSE_TOMBSTONE",
    "PRJ_UPDATE_MAX_VAL",
    "PRJ_UPDATE_NONE",
    "PRJ_UPDATE_RESERVED1",
    "PRJ_UPDATE_RESERVED2",
    "PRJ_UPDATE_TYPES",
    "PRJ_VIRTUALIZATION_INSTANCE_INFO",
    "PrjAllocateAlignedBuffer",
    "PrjClearNegativePathCache",
    "PrjCompleteCommand",
    "PrjDeleteFile",
    "PrjDoesNameContainWildCards",
    "PrjFileNameCompare",
    "PrjFileNameMatch",
    "PrjFillDirEntryBuffer",
    "PrjFillDirEntryBuffer2",
    "PrjFreeAlignedBuffer",
    "PrjGetOnDiskFileState",
    "PrjGetVirtualizationInstanceInfo",
    "PrjMarkDirectoryAsPlaceholder",
    "PrjStartVirtualizing",
    "PrjStopVirtualizing",
    "PrjUpdateFileIfNeeded",
    "PrjWriteFileData",
    "PrjWritePlaceholderInfo",
    "PrjWritePlaceholderInfo2",
]
_arch_optional = [
]
