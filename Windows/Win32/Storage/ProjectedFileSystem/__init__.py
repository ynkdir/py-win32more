from __future__ import annotations
from ctypes import POINTER
from Windows import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import Windows.Win32.Foundation
import Windows.Win32.Storage.ProjectedFileSystem
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
@winfunctype('PROJECTEDFSLIB.dll')
def PrjStartVirtualizing(virtualizationRootPath: Windows.Win32.Foundation.PWSTR, callbacks: POINTER(Windows.Win32.Storage.ProjectedFileSystem.PRJ_CALLBACKS_head), instanceContext: VoidPtr, options: POINTER(Windows.Win32.Storage.ProjectedFileSystem.PRJ_STARTVIRTUALIZING_OPTIONS_head), namespaceVirtualizationContext: POINTER(Windows.Win32.Storage.ProjectedFileSystem.PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjStopVirtualizing(namespaceVirtualizationContext: Windows.Win32.Storage.ProjectedFileSystem.PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT) -> Void: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjClearNegativePathCache(namespaceVirtualizationContext: Windows.Win32.Storage.ProjectedFileSystem.PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT, totalEntryNumber: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjGetVirtualizationInstanceInfo(namespaceVirtualizationContext: Windows.Win32.Storage.ProjectedFileSystem.PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT, virtualizationInstanceInfo: POINTER(Windows.Win32.Storage.ProjectedFileSystem.PRJ_VIRTUALIZATION_INSTANCE_INFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjMarkDirectoryAsPlaceholder(rootPathName: Windows.Win32.Foundation.PWSTR, targetPathName: Windows.Win32.Foundation.PWSTR, versionInfo: POINTER(Windows.Win32.Storage.ProjectedFileSystem.PRJ_PLACEHOLDER_VERSION_INFO_head), virtualizationInstanceID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjWritePlaceholderInfo(namespaceVirtualizationContext: Windows.Win32.Storage.ProjectedFileSystem.PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT, destinationFileName: Windows.Win32.Foundation.PWSTR, placeholderInfo: POINTER(Windows.Win32.Storage.ProjectedFileSystem.PRJ_PLACEHOLDER_INFO_head), placeholderInfoSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjWritePlaceholderInfo2(namespaceVirtualizationContext: Windows.Win32.Storage.ProjectedFileSystem.PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT, destinationFileName: Windows.Win32.Foundation.PWSTR, placeholderInfo: POINTER(Windows.Win32.Storage.ProjectedFileSystem.PRJ_PLACEHOLDER_INFO_head), placeholderInfoSize: UInt32, ExtendedInfo: POINTER(Windows.Win32.Storage.ProjectedFileSystem.PRJ_EXTENDED_INFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjUpdateFileIfNeeded(namespaceVirtualizationContext: Windows.Win32.Storage.ProjectedFileSystem.PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT, destinationFileName: Windows.Win32.Foundation.PWSTR, placeholderInfo: POINTER(Windows.Win32.Storage.ProjectedFileSystem.PRJ_PLACEHOLDER_INFO_head), placeholderInfoSize: UInt32, updateFlags: Windows.Win32.Storage.ProjectedFileSystem.PRJ_UPDATE_TYPES, failureReason: POINTER(Windows.Win32.Storage.ProjectedFileSystem.PRJ_UPDATE_FAILURE_CAUSES)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjDeleteFile(namespaceVirtualizationContext: Windows.Win32.Storage.ProjectedFileSystem.PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT, destinationFileName: Windows.Win32.Foundation.PWSTR, updateFlags: Windows.Win32.Storage.ProjectedFileSystem.PRJ_UPDATE_TYPES, failureReason: POINTER(Windows.Win32.Storage.ProjectedFileSystem.PRJ_UPDATE_FAILURE_CAUSES)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjWriteFileData(namespaceVirtualizationContext: Windows.Win32.Storage.ProjectedFileSystem.PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT, dataStreamId: POINTER(Guid), buffer: VoidPtr, byteOffset: UInt64, length: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjGetOnDiskFileState(destinationFileName: Windows.Win32.Foundation.PWSTR, fileState: POINTER(Windows.Win32.Storage.ProjectedFileSystem.PRJ_FILE_STATE)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjAllocateAlignedBuffer(namespaceVirtualizationContext: Windows.Win32.Storage.ProjectedFileSystem.PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT, size: UIntPtr) -> VoidPtr: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjFreeAlignedBuffer(buffer: VoidPtr) -> Void: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjCompleteCommand(namespaceVirtualizationContext: Windows.Win32.Storage.ProjectedFileSystem.PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT, commandId: Int32, completionResult: Windows.Win32.Foundation.HRESULT, extendedParameters: POINTER(Windows.Win32.Storage.ProjectedFileSystem.PRJ_COMPLETE_COMMAND_EXTENDED_PARAMETERS_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjFillDirEntryBuffer(fileName: Windows.Win32.Foundation.PWSTR, fileBasicInfo: POINTER(Windows.Win32.Storage.ProjectedFileSystem.PRJ_FILE_BASIC_INFO_head), dirEntryBufferHandle: Windows.Win32.Storage.ProjectedFileSystem.PRJ_DIR_ENTRY_BUFFER_HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjFillDirEntryBuffer2(dirEntryBufferHandle: Windows.Win32.Storage.ProjectedFileSystem.PRJ_DIR_ENTRY_BUFFER_HANDLE, fileName: Windows.Win32.Foundation.PWSTR, fileBasicInfo: POINTER(Windows.Win32.Storage.ProjectedFileSystem.PRJ_FILE_BASIC_INFO_head), extendedInfo: POINTER(Windows.Win32.Storage.ProjectedFileSystem.PRJ_EXTENDED_INFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjFileNameMatch(fileNameToCheck: Windows.Win32.Foundation.PWSTR, pattern: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjFileNameCompare(fileName1: Windows.Win32.Foundation.PWSTR, fileName2: Windows.Win32.Foundation.PWSTR) -> Int32: ...
@winfunctype('PROJECTEDFSLIB.dll')
def PrjDoesNameContainWildCards(fileName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOLEAN: ...
class PRJ_CALLBACKS(EasyCastStructure):
    StartDirectoryEnumerationCallback: Windows.Win32.Storage.ProjectedFileSystem.PRJ_START_DIRECTORY_ENUMERATION_CB
    EndDirectoryEnumerationCallback: Windows.Win32.Storage.ProjectedFileSystem.PRJ_END_DIRECTORY_ENUMERATION_CB
    GetDirectoryEnumerationCallback: Windows.Win32.Storage.ProjectedFileSystem.PRJ_GET_DIRECTORY_ENUMERATION_CB
    GetPlaceholderInfoCallback: Windows.Win32.Storage.ProjectedFileSystem.PRJ_GET_PLACEHOLDER_INFO_CB
    GetFileDataCallback: Windows.Win32.Storage.ProjectedFileSystem.PRJ_GET_FILE_DATA_CB
    QueryFileNameCallback: Windows.Win32.Storage.ProjectedFileSystem.PRJ_QUERY_FILE_NAME_CB
    NotificationCallback: Windows.Win32.Storage.ProjectedFileSystem.PRJ_NOTIFICATION_CB
    CancelCommandCallback: Windows.Win32.Storage.ProjectedFileSystem.PRJ_CANCEL_COMMAND_CB
class PRJ_CALLBACK_DATA(EasyCastStructure):
    Size: UInt32
    Flags: Windows.Win32.Storage.ProjectedFileSystem.PRJ_CALLBACK_DATA_FLAGS
    NamespaceVirtualizationContext: Windows.Win32.Storage.ProjectedFileSystem.PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT
    CommandId: Int32
    FileId: Guid
    DataStreamId: Guid
    FilePathName: Windows.Win32.Foundation.PWSTR
    VersionInfo: POINTER(Windows.Win32.Storage.ProjectedFileSystem.PRJ_PLACEHOLDER_VERSION_INFO_head)
    TriggeringProcessId: UInt32
    TriggeringProcessImageFileName: Windows.Win32.Foundation.PWSTR
    InstanceContext: VoidPtr
PRJ_CALLBACK_DATA_FLAGS = Int32
PRJ_CB_DATA_FLAG_ENUM_RESTART_SCAN: PRJ_CALLBACK_DATA_FLAGS = 1
PRJ_CB_DATA_FLAG_ENUM_RETURN_SINGLE_ENTRY: PRJ_CALLBACK_DATA_FLAGS = 2
@winfunctype_pointer
def PRJ_CANCEL_COMMAND_CB(callbackData: POINTER(Windows.Win32.Storage.ProjectedFileSystem.PRJ_CALLBACK_DATA_head)) -> Void: ...
class PRJ_COMPLETE_COMMAND_EXTENDED_PARAMETERS(EasyCastStructure):
    CommandType: Windows.Win32.Storage.ProjectedFileSystem.PRJ_COMPLETE_COMMAND_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Notification: _Notification_e__Struct
        Enumeration: _Enumeration_e__Struct
        class _Notification_e__Struct(EasyCastStructure):
            NotificationMask: Windows.Win32.Storage.ProjectedFileSystem.PRJ_NOTIFY_TYPES
        class _Enumeration_e__Struct(EasyCastStructure):
            DirEntryBufferHandle: Windows.Win32.Storage.ProjectedFileSystem.PRJ_DIR_ENTRY_BUFFER_HANDLE
PRJ_COMPLETE_COMMAND_TYPE = Int32
PRJ_COMPLETE_COMMAND_TYPE_NOTIFICATION: PRJ_COMPLETE_COMMAND_TYPE = 1
PRJ_COMPLETE_COMMAND_TYPE_ENUMERATION: PRJ_COMPLETE_COMMAND_TYPE = 2
PRJ_DIR_ENTRY_BUFFER_HANDLE = IntPtr
@winfunctype_pointer
def PRJ_END_DIRECTORY_ENUMERATION_CB(callbackData: POINTER(Windows.Win32.Storage.ProjectedFileSystem.PRJ_CALLBACK_DATA_head), enumerationId: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class PRJ_EXTENDED_INFO(EasyCastStructure):
    InfoType: Windows.Win32.Storage.ProjectedFileSystem.PRJ_EXT_INFO_TYPE
    NextInfoOffset: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Symlink: _Symlink_e__Struct
        class _Symlink_e__Struct(EasyCastStructure):
            TargetName: Windows.Win32.Foundation.PWSTR
PRJ_EXT_INFO_TYPE = Int32
PRJ_EXT_INFO_TYPE_SYMLINK: PRJ_EXT_INFO_TYPE = 1
class PRJ_FILE_BASIC_INFO(EasyCastStructure):
    IsDirectory: Windows.Win32.Foundation.BOOLEAN
    FileSize: Int64
    CreationTime: Int64
    LastAccessTime: Int64
    LastWriteTime: Int64
    ChangeTime: Int64
    FileAttributes: UInt32
PRJ_FILE_STATE = Int32
PRJ_FILE_STATE_PLACEHOLDER: PRJ_FILE_STATE = 1
PRJ_FILE_STATE_HYDRATED_PLACEHOLDER: PRJ_FILE_STATE = 2
PRJ_FILE_STATE_DIRTY_PLACEHOLDER: PRJ_FILE_STATE = 4
PRJ_FILE_STATE_FULL: PRJ_FILE_STATE = 8
PRJ_FILE_STATE_TOMBSTONE: PRJ_FILE_STATE = 16
@winfunctype_pointer
def PRJ_GET_DIRECTORY_ENUMERATION_CB(callbackData: POINTER(Windows.Win32.Storage.ProjectedFileSystem.PRJ_CALLBACK_DATA_head), enumerationId: POINTER(Guid), searchExpression: Windows.Win32.Foundation.PWSTR, dirEntryBufferHandle: Windows.Win32.Storage.ProjectedFileSystem.PRJ_DIR_ENTRY_BUFFER_HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PRJ_GET_FILE_DATA_CB(callbackData: POINTER(Windows.Win32.Storage.ProjectedFileSystem.PRJ_CALLBACK_DATA_head), byteOffset: UInt64, length: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PRJ_GET_PLACEHOLDER_INFO_CB(callbackData: POINTER(Windows.Win32.Storage.ProjectedFileSystem.PRJ_CALLBACK_DATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
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
def PRJ_NOTIFICATION_CB(callbackData: POINTER(Windows.Win32.Storage.ProjectedFileSystem.PRJ_CALLBACK_DATA_head), isDirectory: Windows.Win32.Foundation.BOOLEAN, notification: Windows.Win32.Storage.ProjectedFileSystem.PRJ_NOTIFICATION, destinationFileName: Windows.Win32.Foundation.PWSTR, operationParameters: POINTER(Windows.Win32.Storage.ProjectedFileSystem.PRJ_NOTIFICATION_PARAMETERS_head)) -> Windows.Win32.Foundation.HRESULT: ...
class PRJ_NOTIFICATION_MAPPING(EasyCastStructure):
    NotificationBitMask: Windows.Win32.Storage.ProjectedFileSystem.PRJ_NOTIFY_TYPES
    NotificationRoot: Windows.Win32.Foundation.PWSTR
class PRJ_NOTIFICATION_PARAMETERS(EasyCastUnion):
    PostCreate: _PostCreate_e__Struct
    FileRenamed: _FileRenamed_e__Struct
    FileDeletedOnHandleClose: _FileDeletedOnHandleClose_e__Struct
    class _PostCreate_e__Struct(EasyCastStructure):
        NotificationMask: Windows.Win32.Storage.ProjectedFileSystem.PRJ_NOTIFY_TYPES
    class _FileRenamed_e__Struct(EasyCastStructure):
        NotificationMask: Windows.Win32.Storage.ProjectedFileSystem.PRJ_NOTIFY_TYPES
    class _FileDeletedOnHandleClose_e__Struct(EasyCastStructure):
        IsFileModified: Windows.Win32.Foundation.BOOLEAN
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
class PRJ_PLACEHOLDER_INFO(EasyCastStructure):
    FileBasicInfo: Windows.Win32.Storage.ProjectedFileSystem.PRJ_FILE_BASIC_INFO
    EaInformation: _EaInformation_e__Struct
    SecurityInformation: _SecurityInformation_e__Struct
    StreamsInformation: _StreamsInformation_e__Struct
    VersionInfo: Windows.Win32.Storage.ProjectedFileSystem.PRJ_PLACEHOLDER_VERSION_INFO
    VariableData: Byte * 1
    class _EaInformation_e__Struct(EasyCastStructure):
        EaBufferSize: UInt32
        OffsetToFirstEa: UInt32
    class _SecurityInformation_e__Struct(EasyCastStructure):
        SecurityBufferSize: UInt32
        OffsetToSecurityDescriptor: UInt32
    class _StreamsInformation_e__Struct(EasyCastStructure):
        StreamsInfoBufferSize: UInt32
        OffsetToFirstStreamInfo: UInt32
class PRJ_PLACEHOLDER_VERSION_INFO(EasyCastStructure):
    ProviderID: Byte * 128
    ContentID: Byte * 128
@winfunctype_pointer
def PRJ_QUERY_FILE_NAME_CB(callbackData: POINTER(Windows.Win32.Storage.ProjectedFileSystem.PRJ_CALLBACK_DATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
PRJ_STARTVIRTUALIZING_FLAGS = Int32
PRJ_FLAG_NONE: PRJ_STARTVIRTUALIZING_FLAGS = 0
PRJ_FLAG_USE_NEGATIVE_PATH_CACHE: PRJ_STARTVIRTUALIZING_FLAGS = 1
class PRJ_STARTVIRTUALIZING_OPTIONS(EasyCastStructure):
    Flags: Windows.Win32.Storage.ProjectedFileSystem.PRJ_STARTVIRTUALIZING_FLAGS
    PoolThreadCount: UInt32
    ConcurrentThreadCount: UInt32
    NotificationMappings: POINTER(Windows.Win32.Storage.ProjectedFileSystem.PRJ_NOTIFICATION_MAPPING_head)
    NotificationMappingsCount: UInt32
@winfunctype_pointer
def PRJ_START_DIRECTORY_ENUMERATION_CB(callbackData: POINTER(Windows.Win32.Storage.ProjectedFileSystem.PRJ_CALLBACK_DATA_head), enumerationId: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
PRJ_UPDATE_FAILURE_CAUSES = Int32
PRJ_UPDATE_FAILURE_CAUSE_NONE: PRJ_UPDATE_FAILURE_CAUSES = 0
PRJ_UPDATE_FAILURE_CAUSE_DIRTY_METADATA: PRJ_UPDATE_FAILURE_CAUSES = 1
PRJ_UPDATE_FAILURE_CAUSE_DIRTY_DATA: PRJ_UPDATE_FAILURE_CAUSES = 2
PRJ_UPDATE_FAILURE_CAUSE_TOMBSTONE: PRJ_UPDATE_FAILURE_CAUSES = 4
PRJ_UPDATE_FAILURE_CAUSE_READ_ONLY: PRJ_UPDATE_FAILURE_CAUSES = 8
PRJ_UPDATE_TYPES = Int32
PRJ_UPDATE_NONE: PRJ_UPDATE_TYPES = 0
PRJ_UPDATE_ALLOW_DIRTY_METADATA: PRJ_UPDATE_TYPES = 1
PRJ_UPDATE_ALLOW_DIRTY_DATA: PRJ_UPDATE_TYPES = 2
PRJ_UPDATE_ALLOW_TOMBSTONE: PRJ_UPDATE_TYPES = 4
PRJ_UPDATE_RESERVED1: PRJ_UPDATE_TYPES = 8
PRJ_UPDATE_RESERVED2: PRJ_UPDATE_TYPES = 16
PRJ_UPDATE_ALLOW_READ_ONLY: PRJ_UPDATE_TYPES = 32
PRJ_UPDATE_MAX_VAL: PRJ_UPDATE_TYPES = 64
class PRJ_VIRTUALIZATION_INSTANCE_INFO(EasyCastStructure):
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
