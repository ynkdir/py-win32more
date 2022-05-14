from win32more import *
import win32more.Storage.ProjectedFileSystem
import win32more.Foundation

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.Storage.ProjectedFileSystem, name, eval(f"_define_{name}()"))
    return getattr(win32more.Storage.ProjectedFileSystem, name)
PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT = IntPtr
PRJ_DIR_ENTRY_BUFFER_HANDLE = IntPtr
PRJ_NOTIFY_TYPES = UInt32
PRJ_NOTIFY_NONE = 0
PRJ_NOTIFY_SUPPRESS_NOTIFICATIONS = 1
PRJ_NOTIFY_FILE_OPENED = 2
PRJ_NOTIFY_NEW_FILE_CREATED = 4
PRJ_NOTIFY_FILE_OVERWRITTEN = 8
PRJ_NOTIFY_PRE_DELETE = 16
PRJ_NOTIFY_PRE_RENAME = 32
PRJ_NOTIFY_PRE_SET_HARDLINK = 64
PRJ_NOTIFY_FILE_RENAMED = 128
PRJ_NOTIFY_HARDLINK_CREATED = 256
PRJ_NOTIFY_FILE_HANDLE_CLOSED_NO_MODIFICATION = 512
PRJ_NOTIFY_FILE_HANDLE_CLOSED_FILE_MODIFIED = 1024
PRJ_NOTIFY_FILE_HANDLE_CLOSED_FILE_DELETED = 2048
PRJ_NOTIFY_FILE_PRE_CONVERT_TO_FULL = 4096
PRJ_NOTIFY_USE_EXISTING_MASK = 4294967295
PRJ_NOTIFICATION = Int32
PRJ_NOTIFICATION_FILE_OPENED = 2
PRJ_NOTIFICATION_NEW_FILE_CREATED = 4
PRJ_NOTIFICATION_FILE_OVERWRITTEN = 8
PRJ_NOTIFICATION_PRE_DELETE = 16
PRJ_NOTIFICATION_PRE_RENAME = 32
PRJ_NOTIFICATION_PRE_SET_HARDLINK = 64
PRJ_NOTIFICATION_FILE_RENAMED = 128
PRJ_NOTIFICATION_HARDLINK_CREATED = 256
PRJ_NOTIFICATION_FILE_HANDLE_CLOSED_NO_MODIFICATION = 512
PRJ_NOTIFICATION_FILE_HANDLE_CLOSED_FILE_MODIFIED = 1024
PRJ_NOTIFICATION_FILE_HANDLE_CLOSED_FILE_DELETED = 2048
PRJ_NOTIFICATION_FILE_PRE_CONVERT_TO_FULL = 4096
PRJ_EXT_INFO_TYPE = Int32
PRJ_EXT_INFO_TYPE_SYMLINK = 1
def _define_PRJ_EXTENDED_INFO_head():
    class PRJ_EXTENDED_INFO(Structure):
        pass
    return PRJ_EXTENDED_INFO
def _define_PRJ_EXTENDED_INFO():
    PRJ_EXTENDED_INFO = win32more.Storage.ProjectedFileSystem.PRJ_EXTENDED_INFO_head
    class PRJ_EXTENDED_INFO__Anonymous_e__Union(Union):
        pass
    class PRJ_EXTENDED_INFO__Anonymous_e__Union__Symlink_e__Struct(Structure):
        pass
    PRJ_EXTENDED_INFO__Anonymous_e__Union__Symlink_e__Struct._fields_ = [
        ("TargetName", win32more.Foundation.PWSTR),
    ]
    PRJ_EXTENDED_INFO__Anonymous_e__Union._fields_ = [
        ("Symlink", PRJ_EXTENDED_INFO__Anonymous_e__Union__Symlink_e__Struct),
    ]
    PRJ_EXTENDED_INFO._anonymous_ = [
        'Anonymous',
    ]
    PRJ_EXTENDED_INFO._fields_ = [
        ("InfoType", win32more.Storage.ProjectedFileSystem.PRJ_EXT_INFO_TYPE),
        ("NextInfoOffset", UInt32),
        ("Anonymous", PRJ_EXTENDED_INFO__Anonymous_e__Union),
    ]
    return PRJ_EXTENDED_INFO
def _define_PRJ_NOTIFICATION_MAPPING_head():
    class PRJ_NOTIFICATION_MAPPING(Structure):
        pass
    return PRJ_NOTIFICATION_MAPPING
def _define_PRJ_NOTIFICATION_MAPPING():
    PRJ_NOTIFICATION_MAPPING = win32more.Storage.ProjectedFileSystem.PRJ_NOTIFICATION_MAPPING_head
    PRJ_NOTIFICATION_MAPPING._fields_ = [
        ("NotificationBitMask", win32more.Storage.ProjectedFileSystem.PRJ_NOTIFY_TYPES),
        ("NotificationRoot", win32more.Foundation.PWSTR),
    ]
    return PRJ_NOTIFICATION_MAPPING
PRJ_STARTVIRTUALIZING_FLAGS = UInt32
PRJ_FLAG_NONE = 0
PRJ_FLAG_USE_NEGATIVE_PATH_CACHE = 1
def _define_PRJ_STARTVIRTUALIZING_OPTIONS_head():
    class PRJ_STARTVIRTUALIZING_OPTIONS(Structure):
        pass
    return PRJ_STARTVIRTUALIZING_OPTIONS
def _define_PRJ_STARTVIRTUALIZING_OPTIONS():
    PRJ_STARTVIRTUALIZING_OPTIONS = win32more.Storage.ProjectedFileSystem.PRJ_STARTVIRTUALIZING_OPTIONS_head
    PRJ_STARTVIRTUALIZING_OPTIONS._fields_ = [
        ("Flags", win32more.Storage.ProjectedFileSystem.PRJ_STARTVIRTUALIZING_FLAGS),
        ("PoolThreadCount", UInt32),
        ("ConcurrentThreadCount", UInt32),
        ("NotificationMappings", POINTER(win32more.Storage.ProjectedFileSystem.PRJ_NOTIFICATION_MAPPING_head)),
        ("NotificationMappingsCount", UInt32),
    ]
    return PRJ_STARTVIRTUALIZING_OPTIONS
def _define_PRJ_VIRTUALIZATION_INSTANCE_INFO_head():
    class PRJ_VIRTUALIZATION_INSTANCE_INFO(Structure):
        pass
    return PRJ_VIRTUALIZATION_INSTANCE_INFO
def _define_PRJ_VIRTUALIZATION_INSTANCE_INFO():
    PRJ_VIRTUALIZATION_INSTANCE_INFO = win32more.Storage.ProjectedFileSystem.PRJ_VIRTUALIZATION_INSTANCE_INFO_head
    PRJ_VIRTUALIZATION_INSTANCE_INFO._fields_ = [
        ("InstanceID", Guid),
        ("WriteAlignment", UInt32),
    ]
    return PRJ_VIRTUALIZATION_INSTANCE_INFO
PRJ_PLACEHOLDER_ID = Int32
PRJ_PLACEHOLDER_ID_LENGTH = 128
def _define_PRJ_PLACEHOLDER_VERSION_INFO_head():
    class PRJ_PLACEHOLDER_VERSION_INFO(Structure):
        pass
    return PRJ_PLACEHOLDER_VERSION_INFO
def _define_PRJ_PLACEHOLDER_VERSION_INFO():
    PRJ_PLACEHOLDER_VERSION_INFO = win32more.Storage.ProjectedFileSystem.PRJ_PLACEHOLDER_VERSION_INFO_head
    PRJ_PLACEHOLDER_VERSION_INFO._fields_ = [
        ("ProviderID", Byte * 128),
        ("ContentID", Byte * 128),
    ]
    return PRJ_PLACEHOLDER_VERSION_INFO
def _define_PRJ_FILE_BASIC_INFO_head():
    class PRJ_FILE_BASIC_INFO(Structure):
        pass
    return PRJ_FILE_BASIC_INFO
def _define_PRJ_FILE_BASIC_INFO():
    PRJ_FILE_BASIC_INFO = win32more.Storage.ProjectedFileSystem.PRJ_FILE_BASIC_INFO_head
    PRJ_FILE_BASIC_INFO._fields_ = [
        ("IsDirectory", win32more.Foundation.BOOLEAN),
        ("FileSize", Int64),
        ("CreationTime", win32more.Foundation.LARGE_INTEGER),
        ("LastAccessTime", win32more.Foundation.LARGE_INTEGER),
        ("LastWriteTime", win32more.Foundation.LARGE_INTEGER),
        ("ChangeTime", win32more.Foundation.LARGE_INTEGER),
        ("FileAttributes", UInt32),
    ]
    return PRJ_FILE_BASIC_INFO
def _define_PRJ_PLACEHOLDER_INFO_head():
    class PRJ_PLACEHOLDER_INFO(Structure):
        pass
    return PRJ_PLACEHOLDER_INFO
def _define_PRJ_PLACEHOLDER_INFO():
    PRJ_PLACEHOLDER_INFO = win32more.Storage.ProjectedFileSystem.PRJ_PLACEHOLDER_INFO_head
    class PRJ_PLACEHOLDER_INFO__StreamsInformation_e__Struct(Structure):
        pass
    PRJ_PLACEHOLDER_INFO__StreamsInformation_e__Struct._fields_ = [
        ("StreamsInfoBufferSize", UInt32),
        ("OffsetToFirstStreamInfo", UInt32),
    ]
    class PRJ_PLACEHOLDER_INFO__EaInformation_e__Struct(Structure):
        pass
    PRJ_PLACEHOLDER_INFO__EaInformation_e__Struct._fields_ = [
        ("EaBufferSize", UInt32),
        ("OffsetToFirstEa", UInt32),
    ]
    class PRJ_PLACEHOLDER_INFO__SecurityInformation_e__Struct(Structure):
        pass
    PRJ_PLACEHOLDER_INFO__SecurityInformation_e__Struct._fields_ = [
        ("SecurityBufferSize", UInt32),
        ("OffsetToSecurityDescriptor", UInt32),
    ]
    PRJ_PLACEHOLDER_INFO._fields_ = [
        ("FileBasicInfo", win32more.Storage.ProjectedFileSystem.PRJ_FILE_BASIC_INFO),
        ("EaInformation", PRJ_PLACEHOLDER_INFO__EaInformation_e__Struct),
        ("SecurityInformation", PRJ_PLACEHOLDER_INFO__SecurityInformation_e__Struct),
        ("StreamsInformation", PRJ_PLACEHOLDER_INFO__StreamsInformation_e__Struct),
        ("VersionInfo", win32more.Storage.ProjectedFileSystem.PRJ_PLACEHOLDER_VERSION_INFO),
        ("VariableData", Byte * 0),
    ]
    return PRJ_PLACEHOLDER_INFO
PRJ_UPDATE_TYPES = UInt32
PRJ_UPDATE_NONE = 0
PRJ_UPDATE_ALLOW_DIRTY_METADATA = 1
PRJ_UPDATE_ALLOW_DIRTY_DATA = 2
PRJ_UPDATE_ALLOW_TOMBSTONE = 4
PRJ_UPDATE_RESERVED1 = 8
PRJ_UPDATE_RESERVED2 = 16
PRJ_UPDATE_ALLOW_READ_ONLY = 32
PRJ_UPDATE_MAX_VAL = 64
PRJ_UPDATE_FAILURE_CAUSES = UInt32
PRJ_UPDATE_FAILURE_CAUSE_NONE = 0
PRJ_UPDATE_FAILURE_CAUSE_DIRTY_METADATA = 1
PRJ_UPDATE_FAILURE_CAUSE_DIRTY_DATA = 2
PRJ_UPDATE_FAILURE_CAUSE_TOMBSTONE = 4
PRJ_UPDATE_FAILURE_CAUSE_READ_ONLY = 8
PRJ_FILE_STATE = UInt32
PRJ_FILE_STATE_PLACEHOLDER = 1
PRJ_FILE_STATE_HYDRATED_PLACEHOLDER = 2
PRJ_FILE_STATE_DIRTY_PLACEHOLDER = 4
PRJ_FILE_STATE_FULL = 8
PRJ_FILE_STATE_TOMBSTONE = 16
PRJ_CALLBACK_DATA_FLAGS = Int32
PRJ_CB_DATA_FLAG_ENUM_RESTART_SCAN = 1
PRJ_CB_DATA_FLAG_ENUM_RETURN_SINGLE_ENTRY = 2
def _define_PRJ_CALLBACK_DATA_head():
    class PRJ_CALLBACK_DATA(Structure):
        pass
    return PRJ_CALLBACK_DATA
def _define_PRJ_CALLBACK_DATA():
    PRJ_CALLBACK_DATA = win32more.Storage.ProjectedFileSystem.PRJ_CALLBACK_DATA_head
    PRJ_CALLBACK_DATA._fields_ = [
        ("Size", UInt32),
        ("Flags", win32more.Storage.ProjectedFileSystem.PRJ_CALLBACK_DATA_FLAGS),
        ("NamespaceVirtualizationContext", win32more.Storage.ProjectedFileSystem.PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT),
        ("CommandId", Int32),
        ("FileId", Guid),
        ("DataStreamId", Guid),
        ("FilePathName", win32more.Foundation.PWSTR),
        ("VersionInfo", POINTER(win32more.Storage.ProjectedFileSystem.PRJ_PLACEHOLDER_VERSION_INFO_head)),
        ("TriggeringProcessId", UInt32),
        ("TriggeringProcessImageFileName", win32more.Foundation.PWSTR),
        ("InstanceContext", c_void_p),
    ]
    return PRJ_CALLBACK_DATA
def _define_PRJ_START_DIRECTORY_ENUMERATION_CB():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.ProjectedFileSystem.PRJ_CALLBACK_DATA_head),POINTER(Guid), use_last_error=False)
def _define_PRJ_GET_DIRECTORY_ENUMERATION_CB():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.ProjectedFileSystem.PRJ_CALLBACK_DATA_head),POINTER(Guid),win32more.Foundation.PWSTR,win32more.Storage.ProjectedFileSystem.PRJ_DIR_ENTRY_BUFFER_HANDLE, use_last_error=False)
def _define_PRJ_END_DIRECTORY_ENUMERATION_CB():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.ProjectedFileSystem.PRJ_CALLBACK_DATA_head),POINTER(Guid), use_last_error=False)
def _define_PRJ_GET_PLACEHOLDER_INFO_CB():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.ProjectedFileSystem.PRJ_CALLBACK_DATA_head), use_last_error=False)
def _define_PRJ_GET_FILE_DATA_CB():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.ProjectedFileSystem.PRJ_CALLBACK_DATA_head),UInt64,UInt32, use_last_error=False)
def _define_PRJ_QUERY_FILE_NAME_CB():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.ProjectedFileSystem.PRJ_CALLBACK_DATA_head), use_last_error=False)
def _define_PRJ_NOTIFICATION_PARAMETERS_head():
    class PRJ_NOTIFICATION_PARAMETERS(Union):
        pass
    return PRJ_NOTIFICATION_PARAMETERS
def _define_PRJ_NOTIFICATION_PARAMETERS():
    PRJ_NOTIFICATION_PARAMETERS = win32more.Storage.ProjectedFileSystem.PRJ_NOTIFICATION_PARAMETERS_head
    class PRJ_NOTIFICATION_PARAMETERS__FileRenamed_e__Struct(Structure):
        pass
    PRJ_NOTIFICATION_PARAMETERS__FileRenamed_e__Struct._fields_ = [
        ("NotificationMask", win32more.Storage.ProjectedFileSystem.PRJ_NOTIFY_TYPES),
    ]
    class PRJ_NOTIFICATION_PARAMETERS__FileDeletedOnHandleClose_e__Struct(Structure):
        pass
    PRJ_NOTIFICATION_PARAMETERS__FileDeletedOnHandleClose_e__Struct._fields_ = [
        ("IsFileModified", win32more.Foundation.BOOLEAN),
    ]
    class PRJ_NOTIFICATION_PARAMETERS__PostCreate_e__Struct(Structure):
        pass
    PRJ_NOTIFICATION_PARAMETERS__PostCreate_e__Struct._fields_ = [
        ("NotificationMask", win32more.Storage.ProjectedFileSystem.PRJ_NOTIFY_TYPES),
    ]
    PRJ_NOTIFICATION_PARAMETERS._fields_ = [
        ("PostCreate", PRJ_NOTIFICATION_PARAMETERS__PostCreate_e__Struct),
        ("FileRenamed", PRJ_NOTIFICATION_PARAMETERS__FileRenamed_e__Struct),
        ("FileDeletedOnHandleClose", PRJ_NOTIFICATION_PARAMETERS__FileDeletedOnHandleClose_e__Struct),
    ]
    return PRJ_NOTIFICATION_PARAMETERS
def _define_PRJ_NOTIFICATION_CB():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.ProjectedFileSystem.PRJ_CALLBACK_DATA_head),win32more.Foundation.BOOLEAN,win32more.Storage.ProjectedFileSystem.PRJ_NOTIFICATION,win32more.Foundation.PWSTR,POINTER(win32more.Storage.ProjectedFileSystem.PRJ_NOTIFICATION_PARAMETERS_head), use_last_error=False)
def _define_PRJ_CANCEL_COMMAND_CB():
    return CFUNCTYPE(Void,POINTER(win32more.Storage.ProjectedFileSystem.PRJ_CALLBACK_DATA_head), use_last_error=False)
def _define_PRJ_CALLBACKS_head():
    class PRJ_CALLBACKS(Structure):
        pass
    return PRJ_CALLBACKS
def _define_PRJ_CALLBACKS():
    PRJ_CALLBACKS = win32more.Storage.ProjectedFileSystem.PRJ_CALLBACKS_head
    PRJ_CALLBACKS._fields_ = [
        ("StartDirectoryEnumerationCallback", win32more.Storage.ProjectedFileSystem.PRJ_START_DIRECTORY_ENUMERATION_CB),
        ("EndDirectoryEnumerationCallback", win32more.Storage.ProjectedFileSystem.PRJ_END_DIRECTORY_ENUMERATION_CB),
        ("GetDirectoryEnumerationCallback", win32more.Storage.ProjectedFileSystem.PRJ_GET_DIRECTORY_ENUMERATION_CB),
        ("GetPlaceholderInfoCallback", win32more.Storage.ProjectedFileSystem.PRJ_GET_PLACEHOLDER_INFO_CB),
        ("GetFileDataCallback", win32more.Storage.ProjectedFileSystem.PRJ_GET_FILE_DATA_CB),
        ("QueryFileNameCallback", win32more.Storage.ProjectedFileSystem.PRJ_QUERY_FILE_NAME_CB),
        ("NotificationCallback", win32more.Storage.ProjectedFileSystem.PRJ_NOTIFICATION_CB),
        ("CancelCommandCallback", win32more.Storage.ProjectedFileSystem.PRJ_CANCEL_COMMAND_CB),
    ]
    return PRJ_CALLBACKS
PRJ_COMPLETE_COMMAND_TYPE = Int32
PRJ_COMPLETE_COMMAND_TYPE_NOTIFICATION = 1
PRJ_COMPLETE_COMMAND_TYPE_ENUMERATION = 2
def _define_PRJ_COMPLETE_COMMAND_EXTENDED_PARAMETERS_head():
    class PRJ_COMPLETE_COMMAND_EXTENDED_PARAMETERS(Structure):
        pass
    return PRJ_COMPLETE_COMMAND_EXTENDED_PARAMETERS
def _define_PRJ_COMPLETE_COMMAND_EXTENDED_PARAMETERS():
    PRJ_COMPLETE_COMMAND_EXTENDED_PARAMETERS = win32more.Storage.ProjectedFileSystem.PRJ_COMPLETE_COMMAND_EXTENDED_PARAMETERS_head
    class PRJ_COMPLETE_COMMAND_EXTENDED_PARAMETERS__Anonymous_e__Union(Union):
        pass
    class PRJ_COMPLETE_COMMAND_EXTENDED_PARAMETERS__Anonymous_e__Union__Enumeration_e__Struct(Structure):
        pass
    PRJ_COMPLETE_COMMAND_EXTENDED_PARAMETERS__Anonymous_e__Union__Enumeration_e__Struct._fields_ = [
        ("DirEntryBufferHandle", win32more.Storage.ProjectedFileSystem.PRJ_DIR_ENTRY_BUFFER_HANDLE),
    ]
    class PRJ_COMPLETE_COMMAND_EXTENDED_PARAMETERS__Anonymous_e__Union__Notification_e__Struct(Structure):
        pass
    PRJ_COMPLETE_COMMAND_EXTENDED_PARAMETERS__Anonymous_e__Union__Notification_e__Struct._fields_ = [
        ("NotificationMask", win32more.Storage.ProjectedFileSystem.PRJ_NOTIFY_TYPES),
    ]
    PRJ_COMPLETE_COMMAND_EXTENDED_PARAMETERS__Anonymous_e__Union._fields_ = [
        ("Notification", PRJ_COMPLETE_COMMAND_EXTENDED_PARAMETERS__Anonymous_e__Union__Notification_e__Struct),
        ("Enumeration", PRJ_COMPLETE_COMMAND_EXTENDED_PARAMETERS__Anonymous_e__Union__Enumeration_e__Struct),
    ]
    PRJ_COMPLETE_COMMAND_EXTENDED_PARAMETERS._anonymous_ = [
        'Anonymous',
    ]
    PRJ_COMPLETE_COMMAND_EXTENDED_PARAMETERS._fields_ = [
        ("CommandType", win32more.Storage.ProjectedFileSystem.PRJ_COMPLETE_COMMAND_TYPE),
        ("Anonymous", PRJ_COMPLETE_COMMAND_EXTENDED_PARAMETERS__Anonymous_e__Union),
    ]
    return PRJ_COMPLETE_COMMAND_EXTENDED_PARAMETERS
def _define_PrjStartVirtualizing():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Storage.ProjectedFileSystem.PRJ_CALLBACKS_head),c_void_p,POINTER(win32more.Storage.ProjectedFileSystem.PRJ_STARTVIRTUALIZING_OPTIONS_head),POINTER(win32more.Storage.ProjectedFileSystem.PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT), use_last_error=False)(("PrjStartVirtualizing", windll["PROJECTEDFSLIB"]), ((1, 'virtualizationRootPath'),(1, 'callbacks'),(1, 'instanceContext'),(1, 'options'),(1, 'namespaceVirtualizationContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PrjStopVirtualizing():
    try:
        return WINFUNCTYPE(Void,win32more.Storage.ProjectedFileSystem.PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT, use_last_error=False)(("PrjStopVirtualizing", windll["PROJECTEDFSLIB"]), ((1, 'namespaceVirtualizationContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PrjClearNegativePathCache():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.ProjectedFileSystem.PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT,POINTER(UInt32), use_last_error=False)(("PrjClearNegativePathCache", windll["PROJECTEDFSLIB"]), ((1, 'namespaceVirtualizationContext'),(1, 'totalEntryNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PrjGetVirtualizationInstanceInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.ProjectedFileSystem.PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT,POINTER(win32more.Storage.ProjectedFileSystem.PRJ_VIRTUALIZATION_INSTANCE_INFO_head), use_last_error=False)(("PrjGetVirtualizationInstanceInfo", windll["PROJECTEDFSLIB"]), ((1, 'namespaceVirtualizationContext'),(1, 'virtualizationInstanceInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PrjMarkDirectoryAsPlaceholder():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Storage.ProjectedFileSystem.PRJ_PLACEHOLDER_VERSION_INFO_head),POINTER(Guid), use_last_error=False)(("PrjMarkDirectoryAsPlaceholder", windll["PROJECTEDFSLIB"]), ((1, 'rootPathName'),(1, 'targetPathName'),(1, 'versionInfo'),(1, 'virtualizationInstanceID'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PrjWritePlaceholderInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.ProjectedFileSystem.PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT,win32more.Foundation.PWSTR,POINTER(win32more.Storage.ProjectedFileSystem.PRJ_PLACEHOLDER_INFO_head),UInt32, use_last_error=False)(("PrjWritePlaceholderInfo", windll["PROJECTEDFSLIB"]), ((1, 'namespaceVirtualizationContext'),(1, 'destinationFileName'),(1, 'placeholderInfo'),(1, 'placeholderInfoSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PrjWritePlaceholderInfo2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.ProjectedFileSystem.PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT,win32more.Foundation.PWSTR,POINTER(win32more.Storage.ProjectedFileSystem.PRJ_PLACEHOLDER_INFO_head),UInt32,POINTER(win32more.Storage.ProjectedFileSystem.PRJ_EXTENDED_INFO_head), use_last_error=False)(("PrjWritePlaceholderInfo2", windll["PROJECTEDFSLIB"]), ((1, 'namespaceVirtualizationContext'),(1, 'destinationFileName'),(1, 'placeholderInfo'),(1, 'placeholderInfoSize'),(1, 'ExtendedInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PrjUpdateFileIfNeeded():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.ProjectedFileSystem.PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT,win32more.Foundation.PWSTR,POINTER(win32more.Storage.ProjectedFileSystem.PRJ_PLACEHOLDER_INFO_head),UInt32,win32more.Storage.ProjectedFileSystem.PRJ_UPDATE_TYPES,POINTER(win32more.Storage.ProjectedFileSystem.PRJ_UPDATE_FAILURE_CAUSES), use_last_error=False)(("PrjUpdateFileIfNeeded", windll["PROJECTEDFSLIB"]), ((1, 'namespaceVirtualizationContext'),(1, 'destinationFileName'),(1, 'placeholderInfo'),(1, 'placeholderInfoSize'),(1, 'updateFlags'),(1, 'failureReason'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PrjDeleteFile():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.ProjectedFileSystem.PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT,win32more.Foundation.PWSTR,win32more.Storage.ProjectedFileSystem.PRJ_UPDATE_TYPES,POINTER(win32more.Storage.ProjectedFileSystem.PRJ_UPDATE_FAILURE_CAUSES), use_last_error=False)(("PrjDeleteFile", windll["PROJECTEDFSLIB"]), ((1, 'namespaceVirtualizationContext'),(1, 'destinationFileName'),(1, 'updateFlags'),(1, 'failureReason'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PrjWriteFileData():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.ProjectedFileSystem.PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT,POINTER(Guid),c_void_p,UInt64,UInt32, use_last_error=False)(("PrjWriteFileData", windll["PROJECTEDFSLIB"]), ((1, 'namespaceVirtualizationContext'),(1, 'dataStreamId'),(1, 'buffer'),(1, 'byteOffset'),(1, 'length'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PrjGetOnDiskFileState():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Storage.ProjectedFileSystem.PRJ_FILE_STATE), use_last_error=False)(("PrjGetOnDiskFileState", windll["PROJECTEDFSLIB"]), ((1, 'destinationFileName'),(1, 'fileState'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PrjAllocateAlignedBuffer():
    try:
        return WINFUNCTYPE(c_void_p,win32more.Storage.ProjectedFileSystem.PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT,UIntPtr, use_last_error=False)(("PrjAllocateAlignedBuffer", windll["PROJECTEDFSLIB"]), ((1, 'namespaceVirtualizationContext'),(1, 'size'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PrjFreeAlignedBuffer():
    try:
        return WINFUNCTYPE(Void,c_void_p, use_last_error=False)(("PrjFreeAlignedBuffer", windll["PROJECTEDFSLIB"]), ((1, 'buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PrjCompleteCommand():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.ProjectedFileSystem.PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT,Int32,win32more.Foundation.HRESULT,POINTER(win32more.Storage.ProjectedFileSystem.PRJ_COMPLETE_COMMAND_EXTENDED_PARAMETERS_head), use_last_error=False)(("PrjCompleteCommand", windll["PROJECTEDFSLIB"]), ((1, 'namespaceVirtualizationContext'),(1, 'commandId'),(1, 'completionResult'),(1, 'extendedParameters'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PrjFillDirEntryBuffer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Storage.ProjectedFileSystem.PRJ_FILE_BASIC_INFO_head),win32more.Storage.ProjectedFileSystem.PRJ_DIR_ENTRY_BUFFER_HANDLE, use_last_error=False)(("PrjFillDirEntryBuffer", windll["PROJECTEDFSLIB"]), ((1, 'fileName'),(1, 'fileBasicInfo'),(1, 'dirEntryBufferHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PrjFillDirEntryBuffer2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.ProjectedFileSystem.PRJ_DIR_ENTRY_BUFFER_HANDLE,win32more.Foundation.PWSTR,POINTER(win32more.Storage.ProjectedFileSystem.PRJ_FILE_BASIC_INFO_head),POINTER(win32more.Storage.ProjectedFileSystem.PRJ_EXTENDED_INFO_head), use_last_error=False)(("PrjFillDirEntryBuffer2", windll["PROJECTEDFSLIB"]), ((1, 'dirEntryBufferHandle'),(1, 'fileName'),(1, 'fileBasicInfo'),(1, 'extendedInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PrjFileNameMatch():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("PrjFileNameMatch", windll["PROJECTEDFSLIB"]), ((1, 'fileNameToCheck'),(1, 'pattern'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PrjFileNameCompare():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("PrjFileNameCompare", windll["PROJECTEDFSLIB"]), ((1, 'fileName1'),(1, 'fileName2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PrjDoesNameContainWildCards():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,win32more.Foundation.PWSTR, use_last_error=False)(("PrjDoesNameContainWildCards", windll["PROJECTEDFSLIB"]), ((1, 'fileName'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT",
    "PRJ_DIR_ENTRY_BUFFER_HANDLE",
    "PRJ_NOTIFY_TYPES",
    "PRJ_NOTIFY_NONE",
    "PRJ_NOTIFY_SUPPRESS_NOTIFICATIONS",
    "PRJ_NOTIFY_FILE_OPENED",
    "PRJ_NOTIFY_NEW_FILE_CREATED",
    "PRJ_NOTIFY_FILE_OVERWRITTEN",
    "PRJ_NOTIFY_PRE_DELETE",
    "PRJ_NOTIFY_PRE_RENAME",
    "PRJ_NOTIFY_PRE_SET_HARDLINK",
    "PRJ_NOTIFY_FILE_RENAMED",
    "PRJ_NOTIFY_HARDLINK_CREATED",
    "PRJ_NOTIFY_FILE_HANDLE_CLOSED_NO_MODIFICATION",
    "PRJ_NOTIFY_FILE_HANDLE_CLOSED_FILE_MODIFIED",
    "PRJ_NOTIFY_FILE_HANDLE_CLOSED_FILE_DELETED",
    "PRJ_NOTIFY_FILE_PRE_CONVERT_TO_FULL",
    "PRJ_NOTIFY_USE_EXISTING_MASK",
    "PRJ_NOTIFICATION",
    "PRJ_NOTIFICATION_FILE_OPENED",
    "PRJ_NOTIFICATION_NEW_FILE_CREATED",
    "PRJ_NOTIFICATION_FILE_OVERWRITTEN",
    "PRJ_NOTIFICATION_PRE_DELETE",
    "PRJ_NOTIFICATION_PRE_RENAME",
    "PRJ_NOTIFICATION_PRE_SET_HARDLINK",
    "PRJ_NOTIFICATION_FILE_RENAMED",
    "PRJ_NOTIFICATION_HARDLINK_CREATED",
    "PRJ_NOTIFICATION_FILE_HANDLE_CLOSED_NO_MODIFICATION",
    "PRJ_NOTIFICATION_FILE_HANDLE_CLOSED_FILE_MODIFIED",
    "PRJ_NOTIFICATION_FILE_HANDLE_CLOSED_FILE_DELETED",
    "PRJ_NOTIFICATION_FILE_PRE_CONVERT_TO_FULL",
    "PRJ_EXT_INFO_TYPE",
    "PRJ_EXT_INFO_TYPE_SYMLINK",
    "PRJ_EXTENDED_INFO",
    "PRJ_NOTIFICATION_MAPPING",
    "PRJ_STARTVIRTUALIZING_FLAGS",
    "PRJ_FLAG_NONE",
    "PRJ_FLAG_USE_NEGATIVE_PATH_CACHE",
    "PRJ_STARTVIRTUALIZING_OPTIONS",
    "PRJ_VIRTUALIZATION_INSTANCE_INFO",
    "PRJ_PLACEHOLDER_ID",
    "PRJ_PLACEHOLDER_ID_LENGTH",
    "PRJ_PLACEHOLDER_VERSION_INFO",
    "PRJ_FILE_BASIC_INFO",
    "PRJ_PLACEHOLDER_INFO",
    "PRJ_UPDATE_TYPES",
    "PRJ_UPDATE_NONE",
    "PRJ_UPDATE_ALLOW_DIRTY_METADATA",
    "PRJ_UPDATE_ALLOW_DIRTY_DATA",
    "PRJ_UPDATE_ALLOW_TOMBSTONE",
    "PRJ_UPDATE_RESERVED1",
    "PRJ_UPDATE_RESERVED2",
    "PRJ_UPDATE_ALLOW_READ_ONLY",
    "PRJ_UPDATE_MAX_VAL",
    "PRJ_UPDATE_FAILURE_CAUSES",
    "PRJ_UPDATE_FAILURE_CAUSE_NONE",
    "PRJ_UPDATE_FAILURE_CAUSE_DIRTY_METADATA",
    "PRJ_UPDATE_FAILURE_CAUSE_DIRTY_DATA",
    "PRJ_UPDATE_FAILURE_CAUSE_TOMBSTONE",
    "PRJ_UPDATE_FAILURE_CAUSE_READ_ONLY",
    "PRJ_FILE_STATE",
    "PRJ_FILE_STATE_PLACEHOLDER",
    "PRJ_FILE_STATE_HYDRATED_PLACEHOLDER",
    "PRJ_FILE_STATE_DIRTY_PLACEHOLDER",
    "PRJ_FILE_STATE_FULL",
    "PRJ_FILE_STATE_TOMBSTONE",
    "PRJ_CALLBACK_DATA_FLAGS",
    "PRJ_CB_DATA_FLAG_ENUM_RESTART_SCAN",
    "PRJ_CB_DATA_FLAG_ENUM_RETURN_SINGLE_ENTRY",
    "PRJ_CALLBACK_DATA",
    "PRJ_START_DIRECTORY_ENUMERATION_CB",
    "PRJ_GET_DIRECTORY_ENUMERATION_CB",
    "PRJ_END_DIRECTORY_ENUMERATION_CB",
    "PRJ_GET_PLACEHOLDER_INFO_CB",
    "PRJ_GET_FILE_DATA_CB",
    "PRJ_QUERY_FILE_NAME_CB",
    "PRJ_NOTIFICATION_PARAMETERS",
    "PRJ_NOTIFICATION_CB",
    "PRJ_CANCEL_COMMAND_CB",
    "PRJ_CALLBACKS",
    "PRJ_COMPLETE_COMMAND_TYPE",
    "PRJ_COMPLETE_COMMAND_TYPE_NOTIFICATION",
    "PRJ_COMPLETE_COMMAND_TYPE_ENUMERATION",
    "PRJ_COMPLETE_COMMAND_EXTENDED_PARAMETERS",
    "PrjStartVirtualizing",
    "PrjStopVirtualizing",
    "PrjClearNegativePathCache",
    "PrjGetVirtualizationInstanceInfo",
    "PrjMarkDirectoryAsPlaceholder",
    "PrjWritePlaceholderInfo",
    "PrjWritePlaceholderInfo2",
    "PrjUpdateFileIfNeeded",
    "PrjDeleteFile",
    "PrjWriteFileData",
    "PrjGetOnDiskFileState",
    "PrjAllocateAlignedBuffer",
    "PrjFreeAlignedBuffer",
    "PrjCompleteCommand",
    "PrjFillDirEntryBuffer",
    "PrjFillDirEntryBuffer2",
    "PrjFileNameMatch",
    "PrjFileNameCompare",
    "PrjDoesNameContainWildCards",
]
