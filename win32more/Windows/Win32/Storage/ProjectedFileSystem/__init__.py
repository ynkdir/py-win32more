from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Storage.ProjectedFileSystem
@winfunctype('PROJECTEDFSLIB.dll')
def PrjStartVirtualizing(virtualizationRootPath: win32more.Windows.Win32.Foundation.PWSTR, callbacks: POINTER(win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_CALLBACKS), instanceContext: VoidPtr, options: POINTER(win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_STARTVIRTUALIZING_OPTIONS), namespaceVirtualizationContext: POINTER(win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjStopVirtualizing(namespaceVirtualizationContext: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT) -> Void: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjClearNegativePathCache(namespaceVirtualizationContext: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT, totalEntryNumber: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjGetVirtualizationInstanceInfo(namespaceVirtualizationContext: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT, virtualizationInstanceInfo: POINTER(win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_VIRTUALIZATION_INSTANCE_INFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjMarkDirectoryAsPlaceholder(rootPathName: win32more.Windows.Win32.Foundation.PWSTR, targetPathName: win32more.Windows.Win32.Foundation.PWSTR, versionInfo: POINTER(win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_PLACEHOLDER_VERSION_INFO), virtualizationInstanceID: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjWritePlaceholderInfo(namespaceVirtualizationContext: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT, destinationFileName: win32more.Windows.Win32.Foundation.PWSTR, placeholderInfo: POINTER(win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_PLACEHOLDER_INFO), placeholderInfoSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjWritePlaceholderInfo2(namespaceVirtualizationContext: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT, destinationFileName: win32more.Windows.Win32.Foundation.PWSTR, placeholderInfo: POINTER(win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_PLACEHOLDER_INFO), placeholderInfoSize: UInt32, ExtendedInfo: POINTER(win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_EXTENDED_INFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjUpdateFileIfNeeded(namespaceVirtualizationContext: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT, destinationFileName: win32more.Windows.Win32.Foundation.PWSTR, placeholderInfo: POINTER(win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_PLACEHOLDER_INFO), placeholderInfoSize: UInt32, updateFlags: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_UPDATE_TYPES, failureReason: POINTER(win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_UPDATE_FAILURE_CAUSES)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjDeleteFile(namespaceVirtualizationContext: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT, destinationFileName: win32more.Windows.Win32.Foundation.PWSTR, updateFlags: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_UPDATE_TYPES, failureReason: POINTER(win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_UPDATE_FAILURE_CAUSES)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjWriteFileData(namespaceVirtualizationContext: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT, dataStreamId: POINTER(Guid), buffer: VoidPtr, byteOffset: UInt64, length: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjGetOnDiskFileState(destinationFileName: win32more.Windows.Win32.Foundation.PWSTR, fileState: POINTER(win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_FILE_STATE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjAllocateAlignedBuffer(namespaceVirtualizationContext: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT, size: UIntPtr) -> VoidPtr: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjFreeAlignedBuffer(buffer: VoidPtr) -> Void: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjCompleteCommand(namespaceVirtualizationContext: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT, commandId: Int32, completionResult: win32more.Windows.Win32.Foundation.HRESULT, extendedParameters: POINTER(win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_COMPLETE_COMMAND_EXTENDED_PARAMETERS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjFillDirEntryBuffer(fileName: win32more.Windows.Win32.Foundation.PWSTR, fileBasicInfo: POINTER(win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_FILE_BASIC_INFO), dirEntryBufferHandle: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_DIR_ENTRY_BUFFER_HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjFillDirEntryBuffer2(dirEntryBufferHandle: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_DIR_ENTRY_BUFFER_HANDLE, fileName: win32more.Windows.Win32.Foundation.PWSTR, fileBasicInfo: POINTER(win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_FILE_BASIC_INFO), extendedInfo: POINTER(win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_EXTENDED_INFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjFileNameMatch(fileNameToCheck: win32more.Windows.Win32.Foundation.PWSTR, pattern: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjFileNameCompare(fileName1: win32more.Windows.Win32.Foundation.PWSTR, fileName2: win32more.Windows.Win32.Foundation.PWSTR) -> Int32: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjDoesNameContainWildCards(fileName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
class PRJ_CALLBACKS(Structure):
    StartDirectoryEnumerationCallback: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_START_DIRECTORY_ENUMERATION_CB
    EndDirectoryEnumerationCallback: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_END_DIRECTORY_ENUMERATION_CB
    GetDirectoryEnumerationCallback: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_GET_DIRECTORY_ENUMERATION_CB
    GetPlaceholderInfoCallback: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_GET_PLACEHOLDER_INFO_CB
    GetFileDataCallback: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_GET_FILE_DATA_CB
    QueryFileNameCallback: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_QUERY_FILE_NAME_CB
    NotificationCallback: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_NOTIFICATION_CB
    CancelCommandCallback: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_CANCEL_COMMAND_CB
class PRJ_CALLBACK_DATA(Structure):
    Size: UInt32
    Flags: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_CALLBACK_DATA_FLAGS
    NamespaceVirtualizationContext: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT
    CommandId: Int32
    FileId: Guid
    DataStreamId: Guid
    FilePathName: win32more.Windows.Win32.Foundation.PWSTR
    VersionInfo: POINTER(win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_PLACEHOLDER_VERSION_INFO)
    TriggeringProcessId: UInt32
    TriggeringProcessImageFileName: win32more.Windows.Win32.Foundation.PWSTR
    InstanceContext: VoidPtr
PRJ_CALLBACK_DATA_FLAGS = Int32
PRJ_CB_DATA_FLAG_ENUM_RESTART_SCAN: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_CALLBACK_DATA_FLAGS = 1
PRJ_CB_DATA_FLAG_ENUM_RETURN_SINGLE_ENTRY: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_CALLBACK_DATA_FLAGS = 2
@winfunctype_pointer
def PRJ_CANCEL_COMMAND_CB(callbackData: POINTER(win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_CALLBACK_DATA)) -> Void: ...
class PRJ_COMPLETE_COMMAND_EXTENDED_PARAMETERS(Structure):
    CommandType: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_COMPLETE_COMMAND_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Notification: _Notification_e__Struct
        Enumeration: _Enumeration_e__Struct
        class _Notification_e__Struct(Structure):
            NotificationMask: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_NOTIFY_TYPES
        class _Enumeration_e__Struct(Structure):
            DirEntryBufferHandle: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_DIR_ENTRY_BUFFER_HANDLE
PRJ_COMPLETE_COMMAND_TYPE = Int32
PRJ_COMPLETE_COMMAND_TYPE_NOTIFICATION: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_COMPLETE_COMMAND_TYPE = 1
PRJ_COMPLETE_COMMAND_TYPE_ENUMERATION: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_COMPLETE_COMMAND_TYPE = 2
PRJ_DIR_ENTRY_BUFFER_HANDLE = VoidPtr
@winfunctype_pointer
def PRJ_END_DIRECTORY_ENUMERATION_CB(callbackData: POINTER(win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_CALLBACK_DATA), enumerationId: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class PRJ_EXTENDED_INFO(Structure):
    InfoType: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_EXT_INFO_TYPE
    NextInfoOffset: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Symlink: _Symlink_e__Struct
        class _Symlink_e__Struct(Structure):
            TargetName: win32more.Windows.Win32.Foundation.PWSTR
PRJ_EXT_INFO_TYPE = Int32
PRJ_EXT_INFO_TYPE_SYMLINK: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_EXT_INFO_TYPE = 1
class PRJ_FILE_BASIC_INFO(Structure):
    IsDirectory: win32more.Windows.Win32.Foundation.BOOLEAN
    FileSize: Int64
    CreationTime: Int64
    LastAccessTime: Int64
    LastWriteTime: Int64
    ChangeTime: Int64
    FileAttributes: UInt32
PRJ_FILE_STATE = Int32
PRJ_FILE_STATE_PLACEHOLDER: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_FILE_STATE = 1
PRJ_FILE_STATE_HYDRATED_PLACEHOLDER: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_FILE_STATE = 2
PRJ_FILE_STATE_DIRTY_PLACEHOLDER: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_FILE_STATE = 4
PRJ_FILE_STATE_FULL: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_FILE_STATE = 8
PRJ_FILE_STATE_TOMBSTONE: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_FILE_STATE = 16
@winfunctype_pointer
def PRJ_GET_DIRECTORY_ENUMERATION_CB(callbackData: POINTER(win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_CALLBACK_DATA), enumerationId: POINTER(Guid), searchExpression: win32more.Windows.Win32.Foundation.PWSTR, dirEntryBufferHandle: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_DIR_ENTRY_BUFFER_HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PRJ_GET_FILE_DATA_CB(callbackData: POINTER(win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_CALLBACK_DATA), byteOffset: UInt64, length: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PRJ_GET_PLACEHOLDER_INFO_CB(callbackData: POINTER(win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_CALLBACK_DATA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT = VoidPtr
PRJ_NOTIFICATION = Int32
PRJ_NOTIFICATION_FILE_OPENED: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_NOTIFICATION = 2
PRJ_NOTIFICATION_NEW_FILE_CREATED: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_NOTIFICATION = 4
PRJ_NOTIFICATION_FILE_OVERWRITTEN: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_NOTIFICATION = 8
PRJ_NOTIFICATION_PRE_DELETE: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_NOTIFICATION = 16
PRJ_NOTIFICATION_PRE_RENAME: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_NOTIFICATION = 32
PRJ_NOTIFICATION_PRE_SET_HARDLINK: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_NOTIFICATION = 64
PRJ_NOTIFICATION_FILE_RENAMED: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_NOTIFICATION = 128
PRJ_NOTIFICATION_HARDLINK_CREATED: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_NOTIFICATION = 256
PRJ_NOTIFICATION_FILE_HANDLE_CLOSED_NO_MODIFICATION: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_NOTIFICATION = 512
PRJ_NOTIFICATION_FILE_HANDLE_CLOSED_FILE_MODIFIED: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_NOTIFICATION = 1024
PRJ_NOTIFICATION_FILE_HANDLE_CLOSED_FILE_DELETED: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_NOTIFICATION = 2048
PRJ_NOTIFICATION_FILE_PRE_CONVERT_TO_FULL: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_NOTIFICATION = 4096
@winfunctype_pointer
def PRJ_NOTIFICATION_CB(callbackData: POINTER(win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_CALLBACK_DATA), isDirectory: win32more.Windows.Win32.Foundation.BOOLEAN, notification: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_NOTIFICATION, destinationFileName: win32more.Windows.Win32.Foundation.PWSTR, operationParameters: POINTER(win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_NOTIFICATION_PARAMETERS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class PRJ_NOTIFICATION_MAPPING(Structure):
    NotificationBitMask: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_NOTIFY_TYPES
    NotificationRoot: win32more.Windows.Win32.Foundation.PWSTR
class PRJ_NOTIFICATION_PARAMETERS(Union):
    PostCreate: _PostCreate_e__Struct
    FileRenamed: _FileRenamed_e__Struct
    FileDeletedOnHandleClose: _FileDeletedOnHandleClose_e__Struct
    class _PostCreate_e__Struct(Structure):
        NotificationMask: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_NOTIFY_TYPES
    class _FileRenamed_e__Struct(Structure):
        NotificationMask: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_NOTIFY_TYPES
    class _FileDeletedOnHandleClose_e__Struct(Structure):
        IsFileModified: win32more.Windows.Win32.Foundation.BOOLEAN
PRJ_NOTIFY_TYPES = UInt32
PRJ_NOTIFY_NONE: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_NOTIFY_TYPES = 0
PRJ_NOTIFY_SUPPRESS_NOTIFICATIONS: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_NOTIFY_TYPES = 1
PRJ_NOTIFY_FILE_OPENED: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_NOTIFY_TYPES = 2
PRJ_NOTIFY_NEW_FILE_CREATED: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_NOTIFY_TYPES = 4
PRJ_NOTIFY_FILE_OVERWRITTEN: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_NOTIFY_TYPES = 8
PRJ_NOTIFY_PRE_DELETE: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_NOTIFY_TYPES = 16
PRJ_NOTIFY_PRE_RENAME: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_NOTIFY_TYPES = 32
PRJ_NOTIFY_PRE_SET_HARDLINK: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_NOTIFY_TYPES = 64
PRJ_NOTIFY_FILE_RENAMED: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_NOTIFY_TYPES = 128
PRJ_NOTIFY_HARDLINK_CREATED: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_NOTIFY_TYPES = 256
PRJ_NOTIFY_FILE_HANDLE_CLOSED_NO_MODIFICATION: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_NOTIFY_TYPES = 512
PRJ_NOTIFY_FILE_HANDLE_CLOSED_FILE_MODIFIED: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_NOTIFY_TYPES = 1024
PRJ_NOTIFY_FILE_HANDLE_CLOSED_FILE_DELETED: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_NOTIFY_TYPES = 2048
PRJ_NOTIFY_FILE_PRE_CONVERT_TO_FULL: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_NOTIFY_TYPES = 4096
PRJ_NOTIFY_USE_EXISTING_MASK: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_NOTIFY_TYPES = 4294967295
PRJ_PLACEHOLDER_ID = Int32
PRJ_PLACEHOLDER_ID_LENGTH: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_PLACEHOLDER_ID = 128
class PRJ_PLACEHOLDER_INFO(Structure):
    FileBasicInfo: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_FILE_BASIC_INFO
    EaInformation: _EaInformation_e__Struct
    SecurityInformation: _SecurityInformation_e__Struct
    StreamsInformation: _StreamsInformation_e__Struct
    VersionInfo: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_PLACEHOLDER_VERSION_INFO
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
def PRJ_QUERY_FILE_NAME_CB(callbackData: POINTER(win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_CALLBACK_DATA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
PRJ_STARTVIRTUALIZING_FLAGS = Int32
PRJ_FLAG_NONE: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_STARTVIRTUALIZING_FLAGS = 0
PRJ_FLAG_USE_NEGATIVE_PATH_CACHE: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_STARTVIRTUALIZING_FLAGS = 1
class PRJ_STARTVIRTUALIZING_OPTIONS(Structure):
    Flags: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_STARTVIRTUALIZING_FLAGS
    PoolThreadCount: UInt32
    ConcurrentThreadCount: UInt32
    NotificationMappings: POINTER(win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_NOTIFICATION_MAPPING)
    NotificationMappingsCount: UInt32
@winfunctype_pointer
def PRJ_START_DIRECTORY_ENUMERATION_CB(callbackData: POINTER(win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_CALLBACK_DATA), enumerationId: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
PRJ_UPDATE_FAILURE_CAUSES = Int32
PRJ_UPDATE_FAILURE_CAUSE_NONE: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_UPDATE_FAILURE_CAUSES = 0
PRJ_UPDATE_FAILURE_CAUSE_DIRTY_METADATA: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_UPDATE_FAILURE_CAUSES = 1
PRJ_UPDATE_FAILURE_CAUSE_DIRTY_DATA: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_UPDATE_FAILURE_CAUSES = 2
PRJ_UPDATE_FAILURE_CAUSE_TOMBSTONE: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_UPDATE_FAILURE_CAUSES = 4
PRJ_UPDATE_FAILURE_CAUSE_READ_ONLY: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_UPDATE_FAILURE_CAUSES = 8
PRJ_UPDATE_TYPES = Int32
PRJ_UPDATE_NONE: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_UPDATE_TYPES = 0
PRJ_UPDATE_ALLOW_DIRTY_METADATA: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_UPDATE_TYPES = 1
PRJ_UPDATE_ALLOW_DIRTY_DATA: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_UPDATE_TYPES = 2
PRJ_UPDATE_ALLOW_TOMBSTONE: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_UPDATE_TYPES = 4
PRJ_UPDATE_RESERVED1: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_UPDATE_TYPES = 8
PRJ_UPDATE_RESERVED2: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_UPDATE_TYPES = 16
PRJ_UPDATE_ALLOW_READ_ONLY: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_UPDATE_TYPES = 32
PRJ_UPDATE_MAX_VAL: win32more.Windows.Win32.Storage.ProjectedFileSystem.PRJ_UPDATE_TYPES = 64
class PRJ_VIRTUALIZATION_INSTANCE_INFO(Structure):
    InstanceID: Guid
    WriteAlignment: UInt32


make_ready(__name__)
