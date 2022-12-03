from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Storage.FileServerResourceManager
import win32more.System.Com
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f'_define_{name}']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
AdrClientDisplayFlags = Int32
AdrClientDisplayFlags_AllowEmailRequests = 1
AdrClientDisplayFlags_ShowDeviceTroubleshooting = 2
AdrClientErrorType = Int32
AdrClientErrorType_Unknown = 0
AdrClientErrorType_AccessDenied = 1
AdrClientErrorType_FileNotFound = 2
AdrClientFlags = Int32
AdrClientFlags_None = 0
AdrClientFlags_FailForLocalPaths = 1
AdrClientFlags_FailIfNotSupportedByServer = 2
AdrClientFlags_FailIfNotDomainJoined = 4
AdrEmailFlags = Int32
AdrEmailFlags_PutDataOwnerOnToLine = 1
AdrEmailFlags_PutAdminOnToLine = 2
AdrEmailFlags_IncludeDeviceClaims = 4
AdrEmailFlags_IncludeUserInfo = 8
AdrEmailFlags_GenerateEventLog = 16
AdSyncTask = Guid('2ae64751-b728-4d6b-97-a0-b2-da-2e-7d-2a-3b')
FSRM_DISPID_FEATURE_MASK = 251658240
FSRM_DISPID_INTERFACE_A_MASK = 15728640
FSRM_DISPID_INTERFACE_B_MASK = 983040
FSRM_DISPID_INTERFACE_C_MASK = 61440
FSRM_DISPID_INTERFACE_D_MASK = 3840
FSRM_DISPID_IS_PROPERTY = 128
FSRM_DISPID_METHOD_NUM_MASK = 127
FSRM_DISPID_FEATURE_GENERAL = 16777216
FSRM_DISPID_FEATURE_QUOTA = 33554432
FSRM_DISPID_FEATURE_FILESCREEN = 50331648
FSRM_DISPID_FEATURE_REPORTS = 67108864
FSRM_DISPID_FEATURE_CLASSIFICATION = 83886080
FSRM_DISPID_FEATURE_PIPELINE = 100663296
FsrmMaxNumberThresholds = 16
FsrmMinThresholdValue = 1
FsrmMaxThresholdValue = 250
FsrmMinQuotaLimit = 1024
FsrmMaxExcludeFolders = 32
FsrmMaxNumberPropertyDefinitions = 100
MessageSizeLimit = 4096
FsrmDaysNotSpecified = -1
FSRM_S_PARTIAL_BATCH = 283396
FSRM_S_PARTIAL_CLASSIFICATION = 283397
FSRM_S_CLASSIFICATION_SCAN_FAILURES = 283398
FSRM_E_NOT_FOUND = -2147200255
FSRM_E_INVALID_SCHEDULER_ARGUMENT = -2147200254
FSRM_E_ALREADY_EXISTS = -2147200253
FSRM_E_PATH_NOT_FOUND = -2147200252
FSRM_E_INVALID_USER = -2147200251
FSRM_E_INVALID_PATH = -2147200250
FSRM_E_INVALID_LIMIT = -2147200249
FSRM_E_INVALID_NAME = -2147200248
FSRM_E_FAIL_BATCH = -2147200247
FSRM_E_INVALID_TEXT = -2147200246
FSRM_E_INVALID_IMPORT_VERSION = -2147200245
FSRM_E_OUT_OF_RANGE = -2147200243
FSRM_E_REQD_PARAM_MISSING = -2147200242
FSRM_E_INVALID_COMBINATION = -2147200241
FSRM_E_DUPLICATE_NAME = -2147200240
FSRM_E_NOT_SUPPORTED = -2147200239
FSRM_E_DRIVER_NOT_READY = -2147200237
FSRM_E_INSUFFICIENT_DISK = -2147200236
FSRM_E_VOLUME_UNSUPPORTED = -2147200235
FSRM_E_UNEXPECTED = -2147200234
FSRM_E_INSECURE_PATH = -2147200233
FSRM_E_INVALID_SMTP_SERVER = -2147200232
FSRM_E_AUTO_QUOTA = 283419
FSRM_E_EMAIL_NOT_SENT = -2147200228
FSRM_E_INVALID_EMAIL_ADDRESS = -2147200226
FSRM_E_FILE_SYSTEM_CORRUPT = -2147200225
FSRM_E_LONG_CMDLINE = -2147200224
FSRM_E_INVALID_FILEGROUP_DEFINITION = -2147200223
FSRM_E_INVALID_DATASCREEN_DEFINITION = -2147200220
FSRM_E_INVALID_REPORT_FORMAT = -2147200216
FSRM_E_INVALID_REPORT_DESC = -2147200215
FSRM_E_INVALID_FILENAME = -2147200214
FSRM_E_SHADOW_COPY = -2147200212
FSRM_E_XML_CORRUPTED = -2147200211
FSRM_E_CLUSTER_NOT_RUNNING = -2147200210
FSRM_E_STORE_NOT_INSTALLED = -2147200209
FSRM_E_NOT_CLUSTER_VOLUME = -2147200208
FSRM_E_DIFFERENT_CLUSTER_GROUP = -2147200207
FSRM_E_REPORT_TYPE_ALREADY_EXISTS = -2147200206
FSRM_E_REPORT_JOB_ALREADY_RUNNING = -2147200205
FSRM_E_REPORT_GENERATION_ERR = -2147200204
FSRM_E_REPORT_TASK_TRIGGER = -2147200203
FSRM_E_LOADING_DISABLED_MODULE = -2147200202
FSRM_E_CANNOT_AGGREGATE = -2147200201
FSRM_E_MESSAGE_LIMIT_EXCEEDED = -2147200200
FSRM_E_OBJECT_IN_USE = -2147200199
FSRM_E_CANNOT_RENAME_PROPERTY = -2147200198
FSRM_E_CANNOT_CHANGE_PROPERTY_TYPE = -2147200197
FSRM_E_MAX_PROPERTY_DEFINITIONS = -2147200196
FSRM_E_CLASSIFICATION_ALREADY_RUNNING = -2147200195
FSRM_E_CLASSIFICATION_NOT_RUNNING = -2147200194
FSRM_E_FILE_MANAGEMENT_JOB_ALREADY_RUNNING = -2147200193
FSRM_E_FILE_MANAGEMENT_JOB_EXPIRATION = -2147200192
FSRM_E_FILE_MANAGEMENT_JOB_CUSTOM = -2147200191
FSRM_E_FILE_MANAGEMENT_JOB_NOTIFICATION = -2147200190
FSRM_E_FILE_OPEN_ERROR = -2147200189
FSRM_E_UNSECURE_LINK_TO_HOSTED_MODULE = -2147200188
FSRM_E_CACHE_INVALID = -2147200187
FSRM_E_CACHE_MODULE_ALREADY_EXISTS = -2147200186
FSRM_E_FILE_MANAGEMENT_EXPIRATION_DIR_IN_SCOPE = -2147200185
FSRM_E_FILE_MANAGEMENT_JOB_ALREADY_EXISTS = -2147200184
FSRM_E_PROPERTY_DELETED = -2147200183
FSRM_E_LAST_ACCESS_UPDATE_DISABLED = -2147200176
FSRM_E_NO_PROPERTY_VALUE = -2147200175
FSRM_E_INPROC_MODULE_BLOCKED = -2147200174
FSRM_E_ENUM_PROPERTIES_FAILED = -2147200173
FSRM_E_SET_PROPERTY_FAILED = -2147200172
FSRM_E_CANNOT_STORE_PROPERTIES = -2147200171
FSRM_E_CANNOT_ALLOW_REPARSE_POINT_TAG = -2147200170
FSRM_E_PARTIAL_CLASSIFICATION_PROPERTY_NOT_FOUND = -2147200169
FSRM_E_TEXTREADER_NOT_INITIALIZED = -2147200168
FSRM_E_TEXTREADER_IFILTER_NOT_FOUND = -2147200167
FSRM_E_PERSIST_PROPERTIES_FAILED_ENCRYPTED = -2147200166
FSRM_E_TEXTREADER_IFILTER_CLSID_MALFORMED = -2147200160
FSRM_E_TEXTREADER_STREAM_ERROR = -2147200159
FSRM_E_TEXTREADER_FILENAME_TOO_LONG = -2147200158
FSRM_E_INCOMPATIBLE_FORMAT = -2147200157
FSRM_E_FILE_ENCRYPTED = -2147200156
FSRM_E_PERSIST_PROPERTIES_FAILED = -2147200155
FSRM_E_VOLUME_OFFLINE = -2147200154
FSRM_E_FILE_MANAGEMENT_ACTION_TIMEOUT = -2147200153
FSRM_E_FILE_MANAGEMENT_ACTION_GET_EXITCODE_FAILED = -2147200152
FSRM_E_MODULE_INVALID_PARAM = -2147200151
FSRM_E_MODULE_INITIALIZATION = -2147200150
FSRM_E_MODULE_SESSION_INITIALIZATION = -2147200149
FSRM_E_CLASSIFICATION_SCAN_FAIL = -2147200148
FSRM_E_FILE_MANAGEMENT_JOB_NOT_LEGACY_ACCESSIBLE = -2147200147
FSRM_E_FILE_MANAGEMENT_JOB_MAX_FILE_CONDITIONS = -2147200146
FSRM_E_CANNOT_USE_DEPRECATED_PROPERTY = -2147200145
FSRM_E_SYNC_TASK_TIMEOUT = -2147200144
FSRM_E_CANNOT_USE_DELETED_PROPERTY = -2147200143
FSRM_E_INVALID_AD_CLAIM = -2147200142
FSRM_E_CLASSIFICATION_CANCELED = -2147200141
FSRM_E_INVALID_FOLDER_PROPERTY_STORE = -2147200140
FSRM_E_REBUILDING_FODLER_TYPE_INDEX = -2147200139
FSRM_E_PROPERTY_MUST_APPLY_TO_FILES = -2147200138
FSRM_E_CLASSIFICATION_TIMEOUT = -2147200137
FSRM_E_CLASSIFICATION_PARTIAL_BATCH = -2147200136
FSRM_E_CANNOT_DELETE_SYSTEM_PROPERTY = -2147200135
FSRM_E_FILE_IN_USE = -2147200134
FSRM_E_ERROR_NOT_ENABLED = -2147200133
FSRM_E_CANNOT_CREATE_TEMP_COPY = -2147200132
FSRM_E_NO_EMAIL_ADDRESS = -2147200131
FSRM_E_ADR_MAX_EMAILS_SENT = -2147200130
FSRM_E_PATH_NOT_IN_NAMESPACE = -2147200129
FSRM_E_RMS_TEMPLATE_NOT_FOUND = -2147200128
FSRM_E_SECURE_PROPERTIES_NOT_SUPPORTED = -2147200127
FSRM_E_RMS_NO_PROTECTORS_INSTALLED = -2147200126
FSRM_E_RMS_NO_PROTECTOR_INSTALLED_FOR_FILE = -2147200125
FSRM_E_PROPERTY_MUST_APPLY_TO_FOLDERS = -2147200124
FSRM_E_PROPERTY_MUST_BE_SECURE = -2147200123
FSRM_E_PROPERTY_MUST_BE_GLOBAL = -2147200122
FSRM_E_WMI_FAILURE = -2147200121
FSRM_E_FILE_MANAGEMENT_JOB_RMS = -2147200120
FSRM_E_SYNC_TASK_HAD_ERRORS = -2147200119
FSRM_E_ADR_SRV_NOT_SUPPORTED = -2147200112
FSRM_E_ADR_PATH_IS_LOCAL = -2147200111
FSRM_E_ADR_NOT_DOMAIN_JOINED = -2147200110
FSRM_E_CANNOT_REMOVE_READONLY = -2147200109
FSRM_E_FILE_MANAGEMENT_JOB_INVALID_CONTINUOUS_CONFIG = -2147200108
FSRM_E_LEGACY_SCHEDULE = -2147200107
FSRM_E_CSC_PATH_NOT_SUPPORTED = -2147200106
FSRM_E_EXPIRATION_PATH_NOT_WRITEABLE = -2147200105
FSRM_E_EXPIRATION_PATH_TOO_LONG = -2147200104
FSRM_E_EXPIRATION_VOLUME_NOT_NTFS = -2147200103
FSRM_E_FILE_MANAGEMENT_JOB_DEPRECATED = -2147200102
FSRM_E_MODULE_TIMEOUT = -2147200101
def _define_DIFsrmClassificationEvents_head():
    class DIFsrmClassificationEvents(win32more.System.Com.IDispatch_head):
        Guid = Guid('26942db0-dabf-41d8-bb-dd-b1-29-a9-f7-04-24')
    return DIFsrmClassificationEvents
def _define_DIFsrmClassificationEvents():
    DIFsrmClassificationEvents = win32more.Storage.FileServerResourceManager.DIFsrmClassificationEvents_head
    win32more.System.Com.IDispatch
    return DIFsrmClassificationEvents
FsrmAccessDeniedRemediationClient = Guid('100b4fc8-74c1-470f-b1-b7-dd-7b-6b-ae-79-bd')
FsrmAccountType = Int32
FsrmAccountType_Unknown = 0
FsrmAccountType_NetworkService = 1
FsrmAccountType_LocalService = 2
FsrmAccountType_LocalSystem = 3
FsrmAccountType_InProc = 4
FsrmAccountType_External = 5
FsrmAccountType_Automatic = 500
FsrmActionType = Int32
FsrmActionType_Unknown = 0
FsrmActionType_EventLog = 1
FsrmActionType_Email = 2
FsrmActionType_Command = 3
FsrmActionType_Report = 4
FsrmClassificationLoggingFlags = Int32
FsrmClassificationLoggingFlags_None = 0
FsrmClassificationLoggingFlags_ClassificationsInLogFile = 1
FsrmClassificationLoggingFlags_ErrorsInLogFile = 2
FsrmClassificationLoggingFlags_ClassificationsInSystemLog = 4
FsrmClassificationLoggingFlags_ErrorsInSystemLog = 8
FsrmClassificationManager = Guid('b15c0e47-c391-45b9-95-c8-eb-59-6c-85-3f-3a')
FsrmCollectionState = Int32
FsrmCollectionState_Fetching = 1
FsrmCollectionState_Committing = 2
FsrmCollectionState_Complete = 3
FsrmCollectionState_Cancelled = 4
FsrmCommitOptions = Int32
FsrmCommitOptions_None = 0
FsrmCommitOptions_Asynchronous = 1
FsrmEnumOptions = Int32
FsrmEnumOptions_None = 0
FsrmEnumOptions_Asynchronous = 1
FsrmEnumOptions_CheckRecycleBin = 2
FsrmEnumOptions_IncludeClusterNodes = 4
FsrmEnumOptions_IncludeDeprecatedObjects = 8
FsrmEventType = Int32
FsrmEventType_Unknown = 0
FsrmEventType_Information = 1
FsrmEventType_Warning = 2
FsrmEventType_Error = 3
FsrmExecutionOption = Int32
FsrmExecutionOption_Unknown = 0
FsrmExecutionOption_EvaluateUnset = 1
FsrmExecutionOption_ReEvaluate_ConsiderExistingValue = 2
FsrmExecutionOption_ReEvaluate_IgnoreExistingValue = 3
FsrmExportImport = Guid('1482dc37-fae9-4787-90-25-8c-e4-e0-24-ab-56')
FsrmFileConditionType = Int32
FsrmFileConditionType_Unknown = 0
FsrmFileConditionType_Property = 1
FsrmFileGroupManager = Guid('8f1363f6-656f-4496-92-26-13-ae-cb-d7-71-8f')
FsrmFileManagementJobManager = Guid('eb18f9b2-4c3a-4321-b2-03-20-51-20-cf-f6-14')
FsrmFileManagementLoggingFlags = Int32
FsrmFileManagementLoggingFlags_None = 0
FsrmFileManagementLoggingFlags_Error = 1
FsrmFileManagementLoggingFlags_Information = 2
FsrmFileManagementLoggingFlags_Audit = 4
FsrmFileManagementType = Int32
FsrmFileManagementType_Unknown = 0
FsrmFileManagementType_Expiration = 1
FsrmFileManagementType_Custom = 2
FsrmFileManagementType_Rms = 3
FsrmFileScreenFlags = Int32
FsrmFileScreenFlags_Enforce = 1
FsrmFileScreenManager = Guid('95941183-db53-4c5f-b3-7b-7d-09-21-cf-9d-c7')
FsrmFileScreenTemplateManager = Guid('243111df-e474-46aa-a0-54-ea-a3-3e-dc-29-2a')
FsrmFileStreamingInterfaceType = Int32
FsrmFileStreamingInterfaceType_Unknown = 0
FsrmFileStreamingInterfaceType_ILockBytes = 1
FsrmFileStreamingInterfaceType_IStream = 2
FsrmFileStreamingMode = Int32
FsrmFileStreamingMode_Unknown = 0
FsrmFileStreamingMode_Read = 1
FsrmFileStreamingMode_Write = 2
FsrmFileSystemPropertyId = Int32
FsrmFileSystemPropertyId_Undefined = 0
FsrmFileSystemPropertyId_FileName = 1
FsrmFileSystemPropertyId_DateCreated = 2
FsrmFileSystemPropertyId_DateLastAccessed = 3
FsrmFileSystemPropertyId_DateLastModified = 4
FsrmFileSystemPropertyId_DateNow = 5
FsrmGetFilePropertyOptions = Int32
FsrmGetFilePropertyOptions_None = 0
FsrmGetFilePropertyOptions_NoRuleEvaluation = 1
FsrmGetFilePropertyOptions_Persistent = 2
FsrmGetFilePropertyOptions_FailOnPersistErrors = 4
FsrmGetFilePropertyOptions_SkipOrphaned = 8
FsrmPathMapper = Guid('f3be42bd-8ac2-409e-bb-d8-fa-f9-b6-b4-1f-eb')
FsrmPipelineModuleConnector = Guid('c7643375-1eb5-44de-a0-62-62-35-47-d9-33-bc')
FsrmPipelineModuleType = Int32
FsrmPipelineModuleType_Unknown = 0
FsrmPipelineModuleType_Storage = 1
FsrmPipelineModuleType_Classifier = 2
FsrmPropertyBagField = Int32
FsrmPropertyBagField_AccessVolume = 0
FsrmPropertyBagField_VolumeGuidName = 1
FsrmPropertyBagFlags = Int32
FsrmPropertyBagFlags_UpdatedByClassifier = 1
FsrmPropertyBagFlags_FailedLoadingProperties = 2
FsrmPropertyBagFlags_FailedSavingProperties = 4
FsrmPropertyBagFlags_FailedClassifyingProperties = 8
FsrmPropertyConditionType = Int32
FsrmPropertyConditionType_Unknown = 0
FsrmPropertyConditionType_Equal = 1
FsrmPropertyConditionType_NotEqual = 2
FsrmPropertyConditionType_GreaterThan = 3
FsrmPropertyConditionType_LessThan = 4
FsrmPropertyConditionType_Contain = 5
FsrmPropertyConditionType_Exist = 6
FsrmPropertyConditionType_NotExist = 7
FsrmPropertyConditionType_StartWith = 8
FsrmPropertyConditionType_EndWith = 9
FsrmPropertyConditionType_ContainedIn = 10
FsrmPropertyConditionType_PrefixOf = 11
FsrmPropertyConditionType_SuffixOf = 12
FsrmPropertyConditionType_MatchesPattern = 13
FsrmPropertyDefinitionAppliesTo = Int32
FsrmPropertyDefinitionAppliesTo_Files = 1
FsrmPropertyDefinitionAppliesTo_Folders = 2
FsrmPropertyDefinitionFlags = Int32
FsrmPropertyDefinitionFlags_Global = 1
FsrmPropertyDefinitionFlags_Deprecated = 2
FsrmPropertyDefinitionFlags_Secure = 4
FsrmPropertyDefinitionType = Int32
FsrmPropertyDefinitionType_Unknown = 0
FsrmPropertyDefinitionType_OrderedList = 1
FsrmPropertyDefinitionType_MultiChoiceList = 2
FsrmPropertyDefinitionType_SingleChoiceList = 3
FsrmPropertyDefinitionType_String = 4
FsrmPropertyDefinitionType_MultiString = 5
FsrmPropertyDefinitionType_Int = 6
FsrmPropertyDefinitionType_Bool = 7
FsrmPropertyDefinitionType_Date = 8
FsrmPropertyFlags = Int32
FsrmPropertyFlags_None = 0
FsrmPropertyFlags_Orphaned = 1
FsrmPropertyFlags_RetrievedFromCache = 2
FsrmPropertyFlags_RetrievedFromStorage = 4
FsrmPropertyFlags_SetByClassifier = 8
FsrmPropertyFlags_Deleted = 16
FsrmPropertyFlags_Reclassified = 32
FsrmPropertyFlags_AggregationFailed = 64
FsrmPropertyFlags_Existing = 128
FsrmPropertyFlags_FailedLoadingProperties = 256
FsrmPropertyFlags_FailedClassifyingProperties = 512
FsrmPropertyFlags_FailedSavingProperties = 1024
FsrmPropertyFlags_Secure = 2048
FsrmPropertyFlags_PolicyDerived = 4096
FsrmPropertyFlags_Inherited = 8192
FsrmPropertyFlags_Manual = 16384
FsrmPropertyFlags_ExplicitValueDeleted = 32768
FsrmPropertyFlags_PropertyDeletedFromClear = 65536
FsrmPropertyFlags_PropertySourceMask = 14
FsrmPropertyFlags_PersistentMask = 20480
FsrmPropertyValueType = Int32
FsrmPropertyValueType_Undefined = 0
FsrmPropertyValueType_Literal = 1
FsrmPropertyValueType_DateOffset = 2
FsrmQuotaFlags = Int32
FsrmQuotaFlags_Enforce = 256
FsrmQuotaFlags_Disable = 512
FsrmQuotaFlags_StatusIncomplete = 65536
FsrmQuotaFlags_StatusRebuilding = 131072
FsrmQuotaManager = Guid('90dcab7f-347c-4bfc-b5-43-54-03-26-30-5f-be')
FsrmQuotaTemplateManager = Guid('97d3d443-251c-4337-81-e7-b3-2e-8f-4e-e6-5e')
FsrmReportFilter = Int32
FsrmReportFilter_MinSize = 1
FsrmReportFilter_MinAgeDays = 2
FsrmReportFilter_MaxAgeDays = 3
FsrmReportFilter_MinQuotaUsage = 4
FsrmReportFilter_FileGroups = 5
FsrmReportFilter_Owners = 6
FsrmReportFilter_NamePattern = 7
FsrmReportFilter_Property = 8
FsrmReportFormat = Int32
FsrmReportFormat_Unknown = 0
FsrmReportFormat_DHtml = 1
FsrmReportFormat_Html = 2
FsrmReportFormat_Txt = 3
FsrmReportFormat_Csv = 4
FsrmReportFormat_Xml = 5
FsrmReportGenerationContext = Int32
FsrmReportGenerationContext_Undefined = 1
FsrmReportGenerationContext_ScheduledReport = 2
FsrmReportGenerationContext_InteractiveReport = 3
FsrmReportGenerationContext_IncidentReport = 4
FsrmReportLimit = Int32
FsrmReportLimit_MaxFiles = 1
FsrmReportLimit_MaxFileGroups = 2
FsrmReportLimit_MaxOwners = 3
FsrmReportLimit_MaxFilesPerFileGroup = 4
FsrmReportLimit_MaxFilesPerOwner = 5
FsrmReportLimit_MaxFilesPerDuplGroup = 6
FsrmReportLimit_MaxDuplicateGroups = 7
FsrmReportLimit_MaxQuotas = 8
FsrmReportLimit_MaxFileScreenEvents = 9
FsrmReportLimit_MaxPropertyValues = 10
FsrmReportLimit_MaxFilesPerPropertyValue = 11
FsrmReportLimit_MaxFolders = 12
FsrmReportManager = Guid('0058ef37-aa66-4c48-bd-5b-2f-ce-43-2a-b0-c8')
FsrmReportRunningStatus = Int32
FsrmReportRunningStatus_Unknown = 0
FsrmReportRunningStatus_NotRunning = 1
FsrmReportRunningStatus_Queued = 2
FsrmReportRunningStatus_Running = 3
FsrmReportScheduler = Guid('ea25f1b8-1b8d-4290-8e-e8-e1-7c-12-c2-fe-20')
FsrmReportType = Int32
FsrmReportType_Unknown = 0
FsrmReportType_LargeFiles = 1
FsrmReportType_FilesByType = 2
FsrmReportType_LeastRecentlyAccessed = 3
FsrmReportType_MostRecentlyAccessed = 4
FsrmReportType_QuotaUsage = 5
FsrmReportType_FilesByOwner = 6
FsrmReportType_ExportReport = 7
FsrmReportType_DuplicateFiles = 8
FsrmReportType_FileScreenAudit = 9
FsrmReportType_FilesByProperty = 10
FsrmReportType_AutomaticClassification = 11
FsrmReportType_Expiration = 12
FsrmReportType_FoldersByProperty = 13
FsrmRuleFlags = Int32
FsrmRuleFlags_Disabled = 256
FsrmRuleFlags_ClearAutomaticallyClassifiedProperty = 1024
FsrmRuleFlags_ClearManuallyClassifiedProperty = 2048
FsrmRuleFlags_Invalid = 4096
FsrmRuleType = Int32
FsrmRuleType_Unknown = 0
FsrmRuleType_Classification = 1
FsrmRuleType_Generic = 2
FsrmSetting = Guid('f556d708-6d4d-4594-9c-61-7d-bb-0d-ae-2a-46')
FsrmStorageModuleCaps = Int32
FsrmStorageModuleCaps_Unknown = 0
FsrmStorageModuleCaps_CanGet = 1
FsrmStorageModuleCaps_CanSet = 2
FsrmStorageModuleCaps_CanHandleDirectories = 4
FsrmStorageModuleCaps_CanHandleFiles = 8
FsrmStorageModuleType = Int32
FsrmStorageModuleType_Unknown = 0
FsrmStorageModuleType_Cache = 1
FsrmStorageModuleType_InFile = 2
FsrmStorageModuleType_Database = 3
FsrmStorageModuleType_System = 100
FsrmTemplateApplyOptions = Int32
FsrmTemplateApplyOptions_ApplyToDerivedMatching = 1
FsrmTemplateApplyOptions_ApplyToDerivedAll = 2
def _define_IFsrmAccessDeniedRemediationClient_head():
    class IFsrmAccessDeniedRemediationClient(win32more.System.Com.IDispatch_head):
        Guid = Guid('40002314-590b-45a5-8e-1b-8c-05-da-52-7e-52')
    return IFsrmAccessDeniedRemediationClient
def _define_IFsrmAccessDeniedRemediationClient():
    IFsrmAccessDeniedRemediationClient = win32more.Storage.FileServerResourceManager.IFsrmAccessDeniedRemediationClient_head
    IFsrmAccessDeniedRemediationClient.Show = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UIntPtr,win32more.Foundation.BSTR,win32more.Storage.FileServerResourceManager.AdrClientErrorType,Int32,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(Int32))(7, 'Show', ((1, 'parentWnd'),(1, 'accessPath'),(1, 'errorType'),(1, 'flags'),(1, 'windowTitle'),(1, 'windowMessage'),(1, 'result'),)))
    win32more.System.Com.IDispatch
    return IFsrmAccessDeniedRemediationClient
def _define_IFsrmAction_head():
    class IFsrmAction(win32more.System.Com.IDispatch_head):
        Guid = Guid('6cd6408a-ae60-463b-9e-f1-e1-17-53-4d-69-dc')
    return IFsrmAction
def _define_IFsrmAction():
    IFsrmAction = win32more.Storage.FileServerResourceManager.IFsrmAction_head
    IFsrmAction.get_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(7, 'get_Id', ((1, 'id'),)))
    IFsrmAction.get_ActionType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileServerResourceManager.FsrmActionType))(8, 'get_ActionType', ((1, 'actionType'),)))
    IFsrmAction.get_RunLimitInterval = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(9, 'get_RunLimitInterval', ((1, 'minutes'),)))
    IFsrmAction.put_RunLimitInterval = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(10, 'put_RunLimitInterval', ((1, 'minutes'),)))
    IFsrmAction.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(11, 'Delete', ()))
    win32more.System.Com.IDispatch
    return IFsrmAction
def _define_IFsrmActionCommand_head():
    class IFsrmActionCommand(win32more.Storage.FileServerResourceManager.IFsrmAction_head):
        Guid = Guid('12937789-e247-4917-9c-20-f3-ee-9c-7e-e7-83')
    return IFsrmActionCommand
def _define_IFsrmActionCommand():
    IFsrmActionCommand = win32more.Storage.FileServerResourceManager.IFsrmActionCommand_head
    IFsrmActionCommand.get_ExecutablePath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(12, 'get_ExecutablePath', ((1, 'executablePath'),)))
    IFsrmActionCommand.put_ExecutablePath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(13, 'put_ExecutablePath', ((1, 'executablePath'),)))
    IFsrmActionCommand.get_Arguments = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(14, 'get_Arguments', ((1, 'arguments'),)))
    IFsrmActionCommand.put_Arguments = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(15, 'put_Arguments', ((1, 'arguments'),)))
    IFsrmActionCommand.get_Account = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileServerResourceManager.FsrmAccountType))(16, 'get_Account', ((1, 'account'),)))
    IFsrmActionCommand.put_Account = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.FsrmAccountType)(17, 'put_Account', ((1, 'account'),)))
    IFsrmActionCommand.get_WorkingDirectory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(18, 'get_WorkingDirectory', ((1, 'workingDirectory'),)))
    IFsrmActionCommand.put_WorkingDirectory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(19, 'put_WorkingDirectory', ((1, 'workingDirectory'),)))
    IFsrmActionCommand.get_MonitorCommand = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(20, 'get_MonitorCommand', ((1, 'monitorCommand'),)))
    IFsrmActionCommand.put_MonitorCommand = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(21, 'put_MonitorCommand', ((1, 'monitorCommand'),)))
    IFsrmActionCommand.get_KillTimeOut = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(22, 'get_KillTimeOut', ((1, 'minutes'),)))
    IFsrmActionCommand.put_KillTimeOut = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(23, 'put_KillTimeOut', ((1, 'minutes'),)))
    IFsrmActionCommand.get_LogResult = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(24, 'get_LogResult', ((1, 'logResults'),)))
    IFsrmActionCommand.put_LogResult = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(25, 'put_LogResult', ((1, 'logResults'),)))
    win32more.Storage.FileServerResourceManager.IFsrmAction
    return IFsrmActionCommand
def _define_IFsrmActionEmail_head():
    class IFsrmActionEmail(win32more.Storage.FileServerResourceManager.IFsrmAction_head):
        Guid = Guid('d646567d-26ae-4caa-9f-84-4e-0a-ad-20-7f-ca')
    return IFsrmActionEmail
def _define_IFsrmActionEmail():
    IFsrmActionEmail = win32more.Storage.FileServerResourceManager.IFsrmActionEmail_head
    IFsrmActionEmail.get_MailFrom = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(12, 'get_MailFrom', ((1, 'mailFrom'),)))
    IFsrmActionEmail.put_MailFrom = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(13, 'put_MailFrom', ((1, 'mailFrom'),)))
    IFsrmActionEmail.get_MailReplyTo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(14, 'get_MailReplyTo', ((1, 'mailReplyTo'),)))
    IFsrmActionEmail.put_MailReplyTo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(15, 'put_MailReplyTo', ((1, 'mailReplyTo'),)))
    IFsrmActionEmail.get_MailTo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(16, 'get_MailTo', ((1, 'mailTo'),)))
    IFsrmActionEmail.put_MailTo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(17, 'put_MailTo', ((1, 'mailTo'),)))
    IFsrmActionEmail.get_MailCc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(18, 'get_MailCc', ((1, 'mailCc'),)))
    IFsrmActionEmail.put_MailCc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(19, 'put_MailCc', ((1, 'mailCc'),)))
    IFsrmActionEmail.get_MailBcc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(20, 'get_MailBcc', ((1, 'mailBcc'),)))
    IFsrmActionEmail.put_MailBcc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(21, 'put_MailBcc', ((1, 'mailBcc'),)))
    IFsrmActionEmail.get_MailSubject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(22, 'get_MailSubject', ((1, 'mailSubject'),)))
    IFsrmActionEmail.put_MailSubject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(23, 'put_MailSubject', ((1, 'mailSubject'),)))
    IFsrmActionEmail.get_MessageText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(24, 'get_MessageText', ((1, 'messageText'),)))
    IFsrmActionEmail.put_MessageText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(25, 'put_MessageText', ((1, 'messageText'),)))
    win32more.Storage.FileServerResourceManager.IFsrmAction
    return IFsrmActionEmail
def _define_IFsrmActionEmail2_head():
    class IFsrmActionEmail2(win32more.Storage.FileServerResourceManager.IFsrmActionEmail_head):
        Guid = Guid('8276702f-2532-4839-89-bf-48-72-60-9a-2e-a4')
    return IFsrmActionEmail2
def _define_IFsrmActionEmail2():
    IFsrmActionEmail2 = win32more.Storage.FileServerResourceManager.IFsrmActionEmail2_head
    IFsrmActionEmail2.get_AttachmentFileListSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(26, 'get_AttachmentFileListSize', ((1, 'attachmentFileListSize'),)))
    IFsrmActionEmail2.put_AttachmentFileListSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(27, 'put_AttachmentFileListSize', ((1, 'attachmentFileListSize'),)))
    win32more.Storage.FileServerResourceManager.IFsrmActionEmail
    return IFsrmActionEmail2
def _define_IFsrmActionEventLog_head():
    class IFsrmActionEventLog(win32more.Storage.FileServerResourceManager.IFsrmAction_head):
        Guid = Guid('4c8f96c3-5d94-4f37-a4-f4-f5-6a-b4-63-54-6f')
    return IFsrmActionEventLog
def _define_IFsrmActionEventLog():
    IFsrmActionEventLog = win32more.Storage.FileServerResourceManager.IFsrmActionEventLog_head
    IFsrmActionEventLog.get_EventType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileServerResourceManager.FsrmEventType))(12, 'get_EventType', ((1, 'eventType'),)))
    IFsrmActionEventLog.put_EventType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.FsrmEventType)(13, 'put_EventType', ((1, 'eventType'),)))
    IFsrmActionEventLog.get_MessageText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(14, 'get_MessageText', ((1, 'messageText'),)))
    IFsrmActionEventLog.put_MessageText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(15, 'put_MessageText', ((1, 'messageText'),)))
    win32more.Storage.FileServerResourceManager.IFsrmAction
    return IFsrmActionEventLog
def _define_IFsrmActionReport_head():
    class IFsrmActionReport(win32more.Storage.FileServerResourceManager.IFsrmAction_head):
        Guid = Guid('2dbe63c4-b340-48a0-a5-b0-15-8e-07-fc-56-7e')
    return IFsrmActionReport
def _define_IFsrmActionReport():
    IFsrmActionReport = win32more.Storage.FileServerResourceManager.IFsrmActionReport_head
    IFsrmActionReport.get_ReportTypes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(12, 'get_ReportTypes', ((1, 'reportTypes'),)))
    IFsrmActionReport.put_ReportTypes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head))(13, 'put_ReportTypes', ((1, 'reportTypes'),)))
    IFsrmActionReport.get_MailTo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(14, 'get_MailTo', ((1, 'mailTo'),)))
    IFsrmActionReport.put_MailTo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(15, 'put_MailTo', ((1, 'mailTo'),)))
    win32more.Storage.FileServerResourceManager.IFsrmAction
    return IFsrmActionReport
def _define_IFsrmAutoApplyQuota_head():
    class IFsrmAutoApplyQuota(win32more.Storage.FileServerResourceManager.IFsrmQuotaObject_head):
        Guid = Guid('f82e5729-6aba-4740-bf-c7-c7-f5-8f-75-fb-7b')
    return IFsrmAutoApplyQuota
def _define_IFsrmAutoApplyQuota():
    IFsrmAutoApplyQuota = win32more.Storage.FileServerResourceManager.IFsrmAutoApplyQuota_head
    IFsrmAutoApplyQuota.get_ExcludeFolders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(28, 'get_ExcludeFolders', ((1, 'folders'),)))
    IFsrmAutoApplyQuota.put_ExcludeFolders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head))(29, 'put_ExcludeFolders', ((1, 'folders'),)))
    IFsrmAutoApplyQuota.CommitAndUpdateDerived = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.FsrmCommitOptions,win32more.Storage.FileServerResourceManager.FsrmTemplateApplyOptions,POINTER(win32more.Storage.FileServerResourceManager.IFsrmDerivedObjectsResult_head))(30, 'CommitAndUpdateDerived', ((1, 'commitOptions'),(1, 'applyOptions'),(1, 'derivedObjectsResult'),)))
    win32more.Storage.FileServerResourceManager.IFsrmQuotaObject
    return IFsrmAutoApplyQuota
def _define_IFsrmClassificationManager_head():
    class IFsrmClassificationManager(win32more.System.Com.IDispatch_head):
        Guid = Guid('d2dc89da-ee91-48a0-85-d8-cc-72-a5-6f-7d-04')
    return IFsrmClassificationManager
def _define_IFsrmClassificationManager():
    IFsrmClassificationManager = win32more.Storage.FileServerResourceManager.IFsrmClassificationManager_head
    IFsrmClassificationManager.get_ClassificationReportFormats = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(7, 'get_ClassificationReportFormats', ((1, 'formats'),)))
    IFsrmClassificationManager.put_ClassificationReportFormats = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head))(8, 'put_ClassificationReportFormats', ((1, 'formats'),)))
    IFsrmClassificationManager.get_Logging = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(9, 'get_Logging', ((1, 'logging'),)))
    IFsrmClassificationManager.put_Logging = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(10, 'put_Logging', ((1, 'logging'),)))
    IFsrmClassificationManager.get_ClassificationReportMailTo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(11, 'get_ClassificationReportMailTo', ((1, 'mailTo'),)))
    IFsrmClassificationManager.put_ClassificationReportMailTo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(12, 'put_ClassificationReportMailTo', ((1, 'mailTo'),)))
    IFsrmClassificationManager.get_ClassificationReportEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(13, 'get_ClassificationReportEnabled', ((1, 'reportEnabled'),)))
    IFsrmClassificationManager.put_ClassificationReportEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(14, 'put_ClassificationReportEnabled', ((1, 'reportEnabled'),)))
    IFsrmClassificationManager.get_ClassificationLastReportPathWithoutExtension = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(15, 'get_ClassificationLastReportPathWithoutExtension', ((1, 'lastReportPath'),)))
    IFsrmClassificationManager.get_ClassificationLastError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(16, 'get_ClassificationLastError', ((1, 'lastError'),)))
    IFsrmClassificationManager.get_ClassificationRunningStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileServerResourceManager.FsrmReportRunningStatus))(17, 'get_ClassificationRunningStatus', ((1, 'runningStatus'),)))
    IFsrmClassificationManager.EnumPropertyDefinitions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.FsrmEnumOptions,POINTER(win32more.Storage.FileServerResourceManager.IFsrmCollection_head))(18, 'EnumPropertyDefinitions', ((1, 'options'),(1, 'propertyDefinitions'),)))
    IFsrmClassificationManager.CreatePropertyDefinition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileServerResourceManager.IFsrmPropertyDefinition_head))(19, 'CreatePropertyDefinition', ((1, 'propertyDefinition'),)))
    IFsrmClassificationManager.GetPropertyDefinition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Storage.FileServerResourceManager.IFsrmPropertyDefinition_head))(20, 'GetPropertyDefinition', ((1, 'propertyName'),(1, 'propertyDefinition'),)))
    IFsrmClassificationManager.EnumRules = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.FsrmRuleType,win32more.Storage.FileServerResourceManager.FsrmEnumOptions,POINTER(win32more.Storage.FileServerResourceManager.IFsrmCollection_head))(21, 'EnumRules', ((1, 'ruleType'),(1, 'options'),(1, 'Rules'),)))
    IFsrmClassificationManager.CreateRule = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.FsrmRuleType,POINTER(win32more.Storage.FileServerResourceManager.IFsrmRule_head))(22, 'CreateRule', ((1, 'ruleType'),(1, 'Rule'),)))
    IFsrmClassificationManager.GetRule = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Storage.FileServerResourceManager.FsrmRuleType,POINTER(win32more.Storage.FileServerResourceManager.IFsrmRule_head))(23, 'GetRule', ((1, 'ruleName'),(1, 'ruleType'),(1, 'Rule'),)))
    IFsrmClassificationManager.EnumModuleDefinitions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.FsrmPipelineModuleType,win32more.Storage.FileServerResourceManager.FsrmEnumOptions,POINTER(win32more.Storage.FileServerResourceManager.IFsrmCollection_head))(24, 'EnumModuleDefinitions', ((1, 'moduleType'),(1, 'options'),(1, 'moduleDefinitions'),)))
    IFsrmClassificationManager.CreateModuleDefinition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.FsrmPipelineModuleType,POINTER(win32more.Storage.FileServerResourceManager.IFsrmPipelineModuleDefinition_head))(25, 'CreateModuleDefinition', ((1, 'moduleType'),(1, 'moduleDefinition'),)))
    IFsrmClassificationManager.GetModuleDefinition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Storage.FileServerResourceManager.FsrmPipelineModuleType,POINTER(win32more.Storage.FileServerResourceManager.IFsrmPipelineModuleDefinition_head))(26, 'GetModuleDefinition', ((1, 'moduleName'),(1, 'moduleType'),(1, 'moduleDefinition'),)))
    IFsrmClassificationManager.RunClassification = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.FsrmReportGenerationContext,win32more.Foundation.BSTR)(27, 'RunClassification', ((1, 'context'),(1, 'reserved'),)))
    IFsrmClassificationManager.WaitForClassificationCompletion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.VARIANT_BOOL))(28, 'WaitForClassificationCompletion', ((1, 'waitSeconds'),(1, 'completed'),)))
    IFsrmClassificationManager.CancelClassification = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(29, 'CancelClassification', ()))
    IFsrmClassificationManager.EnumFileProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Storage.FileServerResourceManager.FsrmGetFilePropertyOptions,POINTER(win32more.Storage.FileServerResourceManager.IFsrmCollection_head))(30, 'EnumFileProperties', ((1, 'filePath'),(1, 'options'),(1, 'fileProperties'),)))
    IFsrmClassificationManager.GetFileProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Storage.FileServerResourceManager.FsrmGetFilePropertyOptions,POINTER(win32more.Storage.FileServerResourceManager.IFsrmProperty_head))(31, 'GetFileProperty', ((1, 'filePath'),(1, 'propertyName'),(1, 'options'),(1, 'property'),)))
    IFsrmClassificationManager.SetFileProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR)(32, 'SetFileProperty', ((1, 'filePath'),(1, 'propertyName'),(1, 'propertyValue'),)))
    IFsrmClassificationManager.ClearFileProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR)(33, 'ClearFileProperty', ((1, 'filePath'),(1, 'property'),)))
    win32more.System.Com.IDispatch
    return IFsrmClassificationManager
def _define_IFsrmClassificationManager2_head():
    class IFsrmClassificationManager2(win32more.Storage.FileServerResourceManager.IFsrmClassificationManager_head):
        Guid = Guid('0004c1c9-127e-4765-ba-07-6a-31-47-bc-a1-12')
    return IFsrmClassificationManager2
def _define_IFsrmClassificationManager2():
    IFsrmClassificationManager2 = win32more.Storage.FileServerResourceManager.IFsrmClassificationManager2_head
    IFsrmClassificationManager2.ClassifyFiles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head),POINTER(win32more.System.Com.SAFEARRAY_head),POINTER(win32more.System.Com.SAFEARRAY_head),win32more.Storage.FileServerResourceManager.FsrmGetFilePropertyOptions)(34, 'ClassifyFiles', ((1, 'filePaths'),(1, 'propertyNames'),(1, 'propertyValues'),(1, 'options'),)))
    win32more.Storage.FileServerResourceManager.IFsrmClassificationManager
    return IFsrmClassificationManager2
def _define_IFsrmClassificationRule_head():
    class IFsrmClassificationRule(win32more.Storage.FileServerResourceManager.IFsrmRule_head):
        Guid = Guid('afc052c2-5315-45ab-84-1b-c6-db-0e-12-01-48')
    return IFsrmClassificationRule
def _define_IFsrmClassificationRule():
    IFsrmClassificationRule = win32more.Storage.FileServerResourceManager.IFsrmClassificationRule_head
    IFsrmClassificationRule.get_ExecutionOption = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileServerResourceManager.FsrmExecutionOption))(24, 'get_ExecutionOption', ((1, 'executionOption'),)))
    IFsrmClassificationRule.put_ExecutionOption = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.FsrmExecutionOption)(25, 'put_ExecutionOption', ((1, 'executionOption'),)))
    IFsrmClassificationRule.get_PropertyAffected = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(26, 'get_PropertyAffected', ((1, 'property'),)))
    IFsrmClassificationRule.put_PropertyAffected = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(27, 'put_PropertyAffected', ((1, 'property'),)))
    IFsrmClassificationRule.get_Value = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(28, 'get_Value', ((1, 'value'),)))
    IFsrmClassificationRule.put_Value = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(29, 'put_Value', ((1, 'value'),)))
    win32more.Storage.FileServerResourceManager.IFsrmRule
    return IFsrmClassificationRule
def _define_IFsrmClassifierModuleDefinition_head():
    class IFsrmClassifierModuleDefinition(win32more.Storage.FileServerResourceManager.IFsrmPipelineModuleDefinition_head):
        Guid = Guid('bb36ea26-6318-4b8c-85-92-f7-2d-d6-02-e7-a5')
    return IFsrmClassifierModuleDefinition
def _define_IFsrmClassifierModuleDefinition():
    IFsrmClassifierModuleDefinition = win32more.Storage.FileServerResourceManager.IFsrmClassifierModuleDefinition_head
    IFsrmClassifierModuleDefinition.get_PropertiesAffected = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(31, 'get_PropertiesAffected', ((1, 'propertiesAffected'),)))
    IFsrmClassifierModuleDefinition.put_PropertiesAffected = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head))(32, 'put_PropertiesAffected', ((1, 'propertiesAffected'),)))
    IFsrmClassifierModuleDefinition.get_PropertiesUsed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(33, 'get_PropertiesUsed', ((1, 'propertiesUsed'),)))
    IFsrmClassifierModuleDefinition.put_PropertiesUsed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head))(34, 'put_PropertiesUsed', ((1, 'propertiesUsed'),)))
    IFsrmClassifierModuleDefinition.get_NeedsExplicitValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(35, 'get_NeedsExplicitValue', ((1, 'needsExplicitValue'),)))
    IFsrmClassifierModuleDefinition.put_NeedsExplicitValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(36, 'put_NeedsExplicitValue', ((1, 'needsExplicitValue'),)))
    win32more.Storage.FileServerResourceManager.IFsrmPipelineModuleDefinition
    return IFsrmClassifierModuleDefinition
def _define_IFsrmClassifierModuleImplementation_head():
    class IFsrmClassifierModuleImplementation(win32more.Storage.FileServerResourceManager.IFsrmPipelineModuleImplementation_head):
        Guid = Guid('4c968fc6-6edb-4051-9c-18-73-b7-29-1a-e1-06')
    return IFsrmClassifierModuleImplementation
def _define_IFsrmClassifierModuleImplementation():
    IFsrmClassifierModuleImplementation = win32more.Storage.FileServerResourceManager.IFsrmClassifierModuleImplementation_head
    IFsrmClassifierModuleImplementation.get_LastModified = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(9, 'get_LastModified', ((1, 'lastModified'),)))
    IFsrmClassifierModuleImplementation.UseRulesAndDefinitions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.IFsrmCollection_head,win32more.Storage.FileServerResourceManager.IFsrmCollection_head)(10, 'UseRulesAndDefinitions', ((1, 'rules'),(1, 'propertyDefinitions'),)))
    IFsrmClassifierModuleImplementation.OnBeginFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.IFsrmPropertyBag_head,POINTER(win32more.System.Com.SAFEARRAY_head))(11, 'OnBeginFile', ((1, 'propertyBag'),(1, 'arrayRuleIds'),)))
    IFsrmClassifierModuleImplementation.DoesPropertyValueApply = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.Foundation.VARIANT_BOOL),Guid,Guid)(12, 'DoesPropertyValueApply', ((1, 'property'),(1, 'value'),(1, 'applyValue'),(1, 'idRule'),(1, 'idPropDef'),)))
    IFsrmClassifierModuleImplementation.GetPropertyValueToApply = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Foundation.BSTR),Guid,Guid)(13, 'GetPropertyValueToApply', ((1, 'property'),(1, 'value'),(1, 'idRule'),(1, 'idPropDef'),)))
    IFsrmClassifierModuleImplementation.OnEndFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(14, 'OnEndFile', ()))
    win32more.Storage.FileServerResourceManager.IFsrmPipelineModuleImplementation
    return IFsrmClassifierModuleImplementation
def _define_IFsrmCollection_head():
    class IFsrmCollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('f76fbf3b-8ddd-4b42-b0-5a-cb-1c-3f-f1-fe-e8')
    return IFsrmCollection
def _define_IFsrmCollection():
    IFsrmCollection = win32more.Storage.FileServerResourceManager.IFsrmCollection_head
    IFsrmCollection.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(7, 'get__NewEnum', ((1, 'unknown'),)))
    IFsrmCollection.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Com.VARIANT_head))(8, 'get_Item', ((1, 'index'),(1, 'item'),)))
    IFsrmCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(9, 'get_Count', ((1, 'count'),)))
    IFsrmCollection.get_State = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileServerResourceManager.FsrmCollectionState))(10, 'get_State', ((1, 'state'),)))
    IFsrmCollection.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(11, 'Cancel', ()))
    IFsrmCollection.WaitForCompletion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.VARIANT_BOOL))(12, 'WaitForCompletion', ((1, 'waitSeconds'),(1, 'completed'),)))
    IFsrmCollection.GetById = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,POINTER(win32more.System.Com.VARIANT_head))(13, 'GetById', ((1, 'id'),(1, 'entry'),)))
    win32more.System.Com.IDispatch
    return IFsrmCollection
def _define_IFsrmCommittableCollection_head():
    class IFsrmCommittableCollection(win32more.Storage.FileServerResourceManager.IFsrmMutableCollection_head):
        Guid = Guid('96deb3b5-8b91-4a2a-9d-93-80-a3-5d-8a-a8-47')
    return IFsrmCommittableCollection
def _define_IFsrmCommittableCollection():
    IFsrmCommittableCollection = win32more.Storage.FileServerResourceManager.IFsrmCommittableCollection_head
    IFsrmCommittableCollection.Commit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.FsrmCommitOptions,POINTER(win32more.Storage.FileServerResourceManager.IFsrmCollection_head))(18, 'Commit', ((1, 'options'),(1, 'results'),)))
    win32more.Storage.FileServerResourceManager.IFsrmMutableCollection
    return IFsrmCommittableCollection
def _define_IFsrmDerivedObjectsResult_head():
    class IFsrmDerivedObjectsResult(win32more.System.Com.IDispatch_head):
        Guid = Guid('39322a2d-38ee-4d0d-80-95-42-1a-80-84-9a-82')
    return IFsrmDerivedObjectsResult
def _define_IFsrmDerivedObjectsResult():
    IFsrmDerivedObjectsResult = win32more.Storage.FileServerResourceManager.IFsrmDerivedObjectsResult_head
    IFsrmDerivedObjectsResult.get_DerivedObjects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileServerResourceManager.IFsrmCollection_head))(7, 'get_DerivedObjects', ((1, 'derivedObjects'),)))
    IFsrmDerivedObjectsResult.get_Results = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileServerResourceManager.IFsrmCollection_head))(8, 'get_Results', ((1, 'results'),)))
    win32more.System.Com.IDispatch
    return IFsrmDerivedObjectsResult
def _define_IFsrmExportImport_head():
    class IFsrmExportImport(win32more.System.Com.IDispatch_head):
        Guid = Guid('efcb0ab1-16c4-4a79-81-2c-72-56-14-c3-30-6b')
    return IFsrmExportImport
def _define_IFsrmExportImport():
    IFsrmExportImport = win32more.Storage.FileServerResourceManager.IFsrmExportImport_head
    IFsrmExportImport.ExportFileGroups = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head),win32more.Foundation.BSTR)(7, 'ExportFileGroups', ((1, 'filePath'),(1, 'fileGroupNamesSafeArray'),(1, 'remoteHost'),)))
    IFsrmExportImport.ImportFileGroups = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head),win32more.Foundation.BSTR,POINTER(win32more.Storage.FileServerResourceManager.IFsrmCommittableCollection_head))(8, 'ImportFileGroups', ((1, 'filePath'),(1, 'fileGroupNamesSafeArray'),(1, 'remoteHost'),(1, 'fileGroups'),)))
    IFsrmExportImport.ExportFileScreenTemplates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head),win32more.Foundation.BSTR)(9, 'ExportFileScreenTemplates', ((1, 'filePath'),(1, 'templateNamesSafeArray'),(1, 'remoteHost'),)))
    IFsrmExportImport.ImportFileScreenTemplates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head),win32more.Foundation.BSTR,POINTER(win32more.Storage.FileServerResourceManager.IFsrmCommittableCollection_head))(10, 'ImportFileScreenTemplates', ((1, 'filePath'),(1, 'templateNamesSafeArray'),(1, 'remoteHost'),(1, 'templates'),)))
    IFsrmExportImport.ExportQuotaTemplates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head),win32more.Foundation.BSTR)(11, 'ExportQuotaTemplates', ((1, 'filePath'),(1, 'templateNamesSafeArray'),(1, 'remoteHost'),)))
    IFsrmExportImport.ImportQuotaTemplates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head),win32more.Foundation.BSTR,POINTER(win32more.Storage.FileServerResourceManager.IFsrmCommittableCollection_head))(12, 'ImportQuotaTemplates', ((1, 'filePath'),(1, 'templateNamesSafeArray'),(1, 'remoteHost'),(1, 'templates'),)))
    win32more.System.Com.IDispatch
    return IFsrmExportImport
def _define_IFsrmFileCondition_head():
    class IFsrmFileCondition(win32more.System.Com.IDispatch_head):
        Guid = Guid('70684ffc-691a-4a1a-b9-22-97-75-2e-13-8c-c1')
    return IFsrmFileCondition
def _define_IFsrmFileCondition():
    IFsrmFileCondition = win32more.Storage.FileServerResourceManager.IFsrmFileCondition_head
    IFsrmFileCondition.get_Type = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileServerResourceManager.FsrmFileConditionType))(7, 'get_Type', ((1, 'pVal'),)))
    IFsrmFileCondition.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(8, 'Delete', ()))
    win32more.System.Com.IDispatch
    return IFsrmFileCondition
def _define_IFsrmFileConditionProperty_head():
    class IFsrmFileConditionProperty(win32more.Storage.FileServerResourceManager.IFsrmFileCondition_head):
        Guid = Guid('81926775-b981-4479-98-8f-da-17-1d-62-73-60')
    return IFsrmFileConditionProperty
def _define_IFsrmFileConditionProperty():
    IFsrmFileConditionProperty = win32more.Storage.FileServerResourceManager.IFsrmFileConditionProperty_head
    IFsrmFileConditionProperty.get_PropertyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_PropertyName', ((1, 'pVal'),)))
    IFsrmFileConditionProperty.put_PropertyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(10, 'put_PropertyName', ((1, 'newVal'),)))
    IFsrmFileConditionProperty.get_PropertyId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileServerResourceManager.FsrmFileSystemPropertyId))(11, 'get_PropertyId', ((1, 'pVal'),)))
    IFsrmFileConditionProperty.put_PropertyId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.FsrmFileSystemPropertyId)(12, 'put_PropertyId', ((1, 'newVal'),)))
    IFsrmFileConditionProperty.get_Operator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileServerResourceManager.FsrmPropertyConditionType))(13, 'get_Operator', ((1, 'pVal'),)))
    IFsrmFileConditionProperty.put_Operator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.FsrmPropertyConditionType)(14, 'put_Operator', ((1, 'newVal'),)))
    IFsrmFileConditionProperty.get_ValueType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileServerResourceManager.FsrmPropertyValueType))(15, 'get_ValueType', ((1, 'pVal'),)))
    IFsrmFileConditionProperty.put_ValueType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.FsrmPropertyValueType)(16, 'put_ValueType', ((1, 'newVal'),)))
    IFsrmFileConditionProperty.get_Value = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(17, 'get_Value', ((1, 'pVal'),)))
    IFsrmFileConditionProperty.put_Value = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT)(18, 'put_Value', ((1, 'newVal'),)))
    win32more.Storage.FileServerResourceManager.IFsrmFileCondition
    return IFsrmFileConditionProperty
def _define_IFsrmFileGroup_head():
    class IFsrmFileGroup(win32more.Storage.FileServerResourceManager.IFsrmObject_head):
        Guid = Guid('8dd04909-0e34-4d55-af-aa-89-e1-f1-a1-bb-b9')
    return IFsrmFileGroup
def _define_IFsrmFileGroup():
    IFsrmFileGroup = win32more.Storage.FileServerResourceManager.IFsrmFileGroup_head
    IFsrmFileGroup.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(12, 'get_Name', ((1, 'name'),)))
    IFsrmFileGroup.put_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(13, 'put_Name', ((1, 'name'),)))
    IFsrmFileGroup.get_Members = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileServerResourceManager.IFsrmMutableCollection_head))(14, 'get_Members', ((1, 'members'),)))
    IFsrmFileGroup.put_Members = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.IFsrmMutableCollection_head)(15, 'put_Members', ((1, 'members'),)))
    IFsrmFileGroup.get_NonMembers = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileServerResourceManager.IFsrmMutableCollection_head))(16, 'get_NonMembers', ((1, 'nonMembers'),)))
    IFsrmFileGroup.put_NonMembers = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.IFsrmMutableCollection_head)(17, 'put_NonMembers', ((1, 'nonMembers'),)))
    win32more.Storage.FileServerResourceManager.IFsrmObject
    return IFsrmFileGroup
def _define_IFsrmFileGroupImported_head():
    class IFsrmFileGroupImported(win32more.Storage.FileServerResourceManager.IFsrmFileGroup_head):
        Guid = Guid('ad55f10b-5f11-4be7-94-ef-d9-ee-2e-47-0d-ed')
    return IFsrmFileGroupImported
def _define_IFsrmFileGroupImported():
    IFsrmFileGroupImported = win32more.Storage.FileServerResourceManager.IFsrmFileGroupImported_head
    IFsrmFileGroupImported.get_OverwriteOnCommit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(18, 'get_OverwriteOnCommit', ((1, 'overwrite'),)))
    IFsrmFileGroupImported.put_OverwriteOnCommit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(19, 'put_OverwriteOnCommit', ((1, 'overwrite'),)))
    win32more.Storage.FileServerResourceManager.IFsrmFileGroup
    return IFsrmFileGroupImported
def _define_IFsrmFileGroupManager_head():
    class IFsrmFileGroupManager(win32more.System.Com.IDispatch_head):
        Guid = Guid('426677d5-018c-485c-8a-51-20-b8-6d-00-bd-c4')
    return IFsrmFileGroupManager
def _define_IFsrmFileGroupManager():
    IFsrmFileGroupManager = win32more.Storage.FileServerResourceManager.IFsrmFileGroupManager_head
    IFsrmFileGroupManager.CreateFileGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileServerResourceManager.IFsrmFileGroup_head))(7, 'CreateFileGroup', ((1, 'fileGroup'),)))
    IFsrmFileGroupManager.GetFileGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Storage.FileServerResourceManager.IFsrmFileGroup_head))(8, 'GetFileGroup', ((1, 'name'),(1, 'fileGroup'),)))
    IFsrmFileGroupManager.EnumFileGroups = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.FsrmEnumOptions,POINTER(win32more.Storage.FileServerResourceManager.IFsrmCommittableCollection_head))(9, 'EnumFileGroups', ((1, 'options'),(1, 'fileGroups'),)))
    IFsrmFileGroupManager.ExportFileGroups = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.Foundation.BSTR))(10, 'ExportFileGroups', ((1, 'fileGroupNamesArray'),(1, 'serializedFileGroups'),)))
    IFsrmFileGroupManager.ImportFileGroups = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.Storage.FileServerResourceManager.IFsrmCommittableCollection_head))(11, 'ImportFileGroups', ((1, 'serializedFileGroups'),(1, 'fileGroupNamesArray'),(1, 'fileGroups'),)))
    win32more.System.Com.IDispatch
    return IFsrmFileGroupManager
def _define_IFsrmFileManagementJob_head():
    class IFsrmFileManagementJob(win32more.Storage.FileServerResourceManager.IFsrmObject_head):
        Guid = Guid('0770687e-9f36-4d6f-87-78-59-9d-18-84-61-c9')
    return IFsrmFileManagementJob
def _define_IFsrmFileManagementJob():
    IFsrmFileManagementJob = win32more.Storage.FileServerResourceManager.IFsrmFileManagementJob_head
    IFsrmFileManagementJob.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(12, 'get_Name', ((1, 'name'),)))
    IFsrmFileManagementJob.put_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(13, 'put_Name', ((1, 'name'),)))
    IFsrmFileManagementJob.get_NamespaceRoots = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(14, 'get_NamespaceRoots', ((1, 'namespaceRoots'),)))
    IFsrmFileManagementJob.put_NamespaceRoots = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head))(15, 'put_NamespaceRoots', ((1, 'namespaceRoots'),)))
    IFsrmFileManagementJob.get_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(16, 'get_Enabled', ((1, 'enabled'),)))
    IFsrmFileManagementJob.put_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(17, 'put_Enabled', ((1, 'enabled'),)))
    IFsrmFileManagementJob.get_OperationType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileServerResourceManager.FsrmFileManagementType))(18, 'get_OperationType', ((1, 'operationType'),)))
    IFsrmFileManagementJob.put_OperationType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.FsrmFileManagementType)(19, 'put_OperationType', ((1, 'operationType'),)))
    IFsrmFileManagementJob.get_ExpirationDirectory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(20, 'get_ExpirationDirectory', ((1, 'expirationDirectory'),)))
    IFsrmFileManagementJob.put_ExpirationDirectory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(21, 'put_ExpirationDirectory', ((1, 'expirationDirectory'),)))
    IFsrmFileManagementJob.get_CustomAction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileServerResourceManager.IFsrmActionCommand_head))(22, 'get_CustomAction', ((1, 'action'),)))
    IFsrmFileManagementJob.get_Notifications = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(23, 'get_Notifications', ((1, 'notifications'),)))
    IFsrmFileManagementJob.get_Logging = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(24, 'get_Logging', ((1, 'loggingFlags'),)))
    IFsrmFileManagementJob.put_Logging = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(25, 'put_Logging', ((1, 'loggingFlags'),)))
    IFsrmFileManagementJob.get_ReportEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(26, 'get_ReportEnabled', ((1, 'reportEnabled'),)))
    IFsrmFileManagementJob.put_ReportEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(27, 'put_ReportEnabled', ((1, 'reportEnabled'),)))
    IFsrmFileManagementJob.get_Formats = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(28, 'get_Formats', ((1, 'formats'),)))
    IFsrmFileManagementJob.put_Formats = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head))(29, 'put_Formats', ((1, 'formats'),)))
    IFsrmFileManagementJob.get_MailTo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(30, 'get_MailTo', ((1, 'mailTo'),)))
    IFsrmFileManagementJob.put_MailTo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(31, 'put_MailTo', ((1, 'mailTo'),)))
    IFsrmFileManagementJob.get_DaysSinceFileCreated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(32, 'get_DaysSinceFileCreated', ((1, 'daysSinceCreation'),)))
    IFsrmFileManagementJob.put_DaysSinceFileCreated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(33, 'put_DaysSinceFileCreated', ((1, 'daysSinceCreation'),)))
    IFsrmFileManagementJob.get_DaysSinceFileLastAccessed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(34, 'get_DaysSinceFileLastAccessed', ((1, 'daysSinceAccess'),)))
    IFsrmFileManagementJob.put_DaysSinceFileLastAccessed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(35, 'put_DaysSinceFileLastAccessed', ((1, 'daysSinceAccess'),)))
    IFsrmFileManagementJob.get_DaysSinceFileLastModified = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(36, 'get_DaysSinceFileLastModified', ((1, 'daysSinceModify'),)))
    IFsrmFileManagementJob.put_DaysSinceFileLastModified = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(37, 'put_DaysSinceFileLastModified', ((1, 'daysSinceModify'),)))
    IFsrmFileManagementJob.get_PropertyConditions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileServerResourceManager.IFsrmCollection_head))(38, 'get_PropertyConditions', ((1, 'propertyConditions'),)))
    IFsrmFileManagementJob.get_FromDate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(39, 'get_FromDate', ((1, 'fromDate'),)))
    IFsrmFileManagementJob.put_FromDate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double)(40, 'put_FromDate', ((1, 'fromDate'),)))
    IFsrmFileManagementJob.get_Task = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(41, 'get_Task', ((1, 'taskName'),)))
    IFsrmFileManagementJob.put_Task = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(42, 'put_Task', ((1, 'taskName'),)))
    IFsrmFileManagementJob.get_Parameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(43, 'get_Parameters', ((1, 'parameters'),)))
    IFsrmFileManagementJob.put_Parameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head))(44, 'put_Parameters', ((1, 'parameters'),)))
    IFsrmFileManagementJob.get_RunningStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileServerResourceManager.FsrmReportRunningStatus))(45, 'get_RunningStatus', ((1, 'runningStatus'),)))
    IFsrmFileManagementJob.get_LastError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(46, 'get_LastError', ((1, 'lastError'),)))
    IFsrmFileManagementJob.get_LastReportPathWithoutExtension = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(47, 'get_LastReportPathWithoutExtension', ((1, 'path'),)))
    IFsrmFileManagementJob.get_LastRun = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(48, 'get_LastRun', ((1, 'lastRun'),)))
    IFsrmFileManagementJob.get_FileNamePattern = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(49, 'get_FileNamePattern', ((1, 'fileNamePattern'),)))
    IFsrmFileManagementJob.put_FileNamePattern = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(50, 'put_FileNamePattern', ((1, 'fileNamePattern'),)))
    IFsrmFileManagementJob.Run = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.FsrmReportGenerationContext)(51, 'Run', ((1, 'context'),)))
    IFsrmFileManagementJob.WaitForCompletion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.VARIANT_BOOL))(52, 'WaitForCompletion', ((1, 'waitSeconds'),(1, 'completed'),)))
    IFsrmFileManagementJob.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(53, 'Cancel', ()))
    IFsrmFileManagementJob.AddNotification = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(54, 'AddNotification', ((1, 'days'),)))
    IFsrmFileManagementJob.DeleteNotification = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(55, 'DeleteNotification', ((1, 'days'),)))
    IFsrmFileManagementJob.ModifyNotification = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32)(56, 'ModifyNotification', ((1, 'days'),(1, 'newDays'),)))
    IFsrmFileManagementJob.CreateNotificationAction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Storage.FileServerResourceManager.FsrmActionType,POINTER(win32more.Storage.FileServerResourceManager.IFsrmAction_head))(57, 'CreateNotificationAction', ((1, 'days'),(1, 'actionType'),(1, 'action'),)))
    IFsrmFileManagementJob.EnumNotificationActions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Storage.FileServerResourceManager.IFsrmCollection_head))(58, 'EnumNotificationActions', ((1, 'days'),(1, 'actions'),)))
    IFsrmFileManagementJob.CreatePropertyCondition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Storage.FileServerResourceManager.IFsrmPropertyCondition_head))(59, 'CreatePropertyCondition', ((1, 'name'),(1, 'propertyCondition'),)))
    IFsrmFileManagementJob.CreateCustomAction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileServerResourceManager.IFsrmActionCommand_head))(60, 'CreateCustomAction', ((1, 'customAction'),)))
    win32more.Storage.FileServerResourceManager.IFsrmObject
    return IFsrmFileManagementJob
def _define_IFsrmFileManagementJobManager_head():
    class IFsrmFileManagementJobManager(win32more.System.Com.IDispatch_head):
        Guid = Guid('ee321ecb-d95e-48e9-90-7c-c7-68-5a-01-32-35')
    return IFsrmFileManagementJobManager
def _define_IFsrmFileManagementJobManager():
    IFsrmFileManagementJobManager = win32more.Storage.FileServerResourceManager.IFsrmFileManagementJobManager_head
    IFsrmFileManagementJobManager.get_ActionVariables = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(7, 'get_ActionVariables', ((1, 'variables'),)))
    IFsrmFileManagementJobManager.get_ActionVariableDescriptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(8, 'get_ActionVariableDescriptions', ((1, 'descriptions'),)))
    IFsrmFileManagementJobManager.EnumFileManagementJobs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.FsrmEnumOptions,POINTER(win32more.Storage.FileServerResourceManager.IFsrmCollection_head))(9, 'EnumFileManagementJobs', ((1, 'options'),(1, 'fileManagementJobs'),)))
    IFsrmFileManagementJobManager.CreateFileManagementJob = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileServerResourceManager.IFsrmFileManagementJob_head))(10, 'CreateFileManagementJob', ((1, 'fileManagementJob'),)))
    IFsrmFileManagementJobManager.GetFileManagementJob = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Storage.FileServerResourceManager.IFsrmFileManagementJob_head))(11, 'GetFileManagementJob', ((1, 'name'),(1, 'fileManagementJob'),)))
    win32more.System.Com.IDispatch
    return IFsrmFileManagementJobManager
def _define_IFsrmFileScreen_head():
    class IFsrmFileScreen(win32more.Storage.FileServerResourceManager.IFsrmFileScreenBase_head):
        Guid = Guid('5f6325d3-ce88-4733-84-c1-2d-6a-ef-c5-ea-07')
    return IFsrmFileScreen
def _define_IFsrmFileScreen():
    IFsrmFileScreen = win32more.Storage.FileServerResourceManager.IFsrmFileScreen_head
    IFsrmFileScreen.get_Path = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(18, 'get_Path', ((1, 'path'),)))
    IFsrmFileScreen.get_SourceTemplateName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(19, 'get_SourceTemplateName', ((1, 'fileScreenTemplateName'),)))
    IFsrmFileScreen.get_MatchesSourceTemplate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(20, 'get_MatchesSourceTemplate', ((1, 'matches'),)))
    IFsrmFileScreen.get_UserSid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(21, 'get_UserSid', ((1, 'userSid'),)))
    IFsrmFileScreen.get_UserAccount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(22, 'get_UserAccount', ((1, 'userAccount'),)))
    IFsrmFileScreen.ApplyTemplate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(23, 'ApplyTemplate', ((1, 'fileScreenTemplateName'),)))
    win32more.Storage.FileServerResourceManager.IFsrmFileScreenBase
    return IFsrmFileScreen
def _define_IFsrmFileScreenBase_head():
    class IFsrmFileScreenBase(win32more.Storage.FileServerResourceManager.IFsrmObject_head):
        Guid = Guid('f3637e80-5b22-4a2b-a6-37-bb-b6-42-b4-1c-fc')
    return IFsrmFileScreenBase
def _define_IFsrmFileScreenBase():
    IFsrmFileScreenBase = win32more.Storage.FileServerResourceManager.IFsrmFileScreenBase_head
    IFsrmFileScreenBase.get_BlockedFileGroups = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileServerResourceManager.IFsrmMutableCollection_head))(12, 'get_BlockedFileGroups', ((1, 'blockList'),)))
    IFsrmFileScreenBase.put_BlockedFileGroups = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.IFsrmMutableCollection_head)(13, 'put_BlockedFileGroups', ((1, 'blockList'),)))
    IFsrmFileScreenBase.get_FileScreenFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(14, 'get_FileScreenFlags', ((1, 'fileScreenFlags'),)))
    IFsrmFileScreenBase.put_FileScreenFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(15, 'put_FileScreenFlags', ((1, 'fileScreenFlags'),)))
    IFsrmFileScreenBase.CreateAction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.FsrmActionType,POINTER(win32more.Storage.FileServerResourceManager.IFsrmAction_head))(16, 'CreateAction', ((1, 'actionType'),(1, 'action'),)))
    IFsrmFileScreenBase.EnumActions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileServerResourceManager.IFsrmCollection_head))(17, 'EnumActions', ((1, 'actions'),)))
    win32more.Storage.FileServerResourceManager.IFsrmObject
    return IFsrmFileScreenBase
def _define_IFsrmFileScreenException_head():
    class IFsrmFileScreenException(win32more.Storage.FileServerResourceManager.IFsrmObject_head):
        Guid = Guid('bee7ce02-df77-4515-93-89-78-f0-1c-5a-fc-1a')
    return IFsrmFileScreenException
def _define_IFsrmFileScreenException():
    IFsrmFileScreenException = win32more.Storage.FileServerResourceManager.IFsrmFileScreenException_head
    IFsrmFileScreenException.get_Path = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(12, 'get_Path', ((1, 'path'),)))
    IFsrmFileScreenException.get_AllowedFileGroups = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileServerResourceManager.IFsrmMutableCollection_head))(13, 'get_AllowedFileGroups', ((1, 'allowList'),)))
    IFsrmFileScreenException.put_AllowedFileGroups = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.IFsrmMutableCollection_head)(14, 'put_AllowedFileGroups', ((1, 'allowList'),)))
    win32more.Storage.FileServerResourceManager.IFsrmObject
    return IFsrmFileScreenException
def _define_IFsrmFileScreenManager_head():
    class IFsrmFileScreenManager(win32more.System.Com.IDispatch_head):
        Guid = Guid('ff4fa04e-5a94-4bda-a3-a0-d5-b4-d3-c5-2e-ba')
    return IFsrmFileScreenManager
def _define_IFsrmFileScreenManager():
    IFsrmFileScreenManager = win32more.Storage.FileServerResourceManager.IFsrmFileScreenManager_head
    IFsrmFileScreenManager.get_ActionVariables = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(7, 'get_ActionVariables', ((1, 'variables'),)))
    IFsrmFileScreenManager.get_ActionVariableDescriptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(8, 'get_ActionVariableDescriptions', ((1, 'descriptions'),)))
    IFsrmFileScreenManager.CreateFileScreen = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Storage.FileServerResourceManager.IFsrmFileScreen_head))(9, 'CreateFileScreen', ((1, 'path'),(1, 'fileScreen'),)))
    IFsrmFileScreenManager.GetFileScreen = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Storage.FileServerResourceManager.IFsrmFileScreen_head))(10, 'GetFileScreen', ((1, 'path'),(1, 'fileScreen'),)))
    IFsrmFileScreenManager.EnumFileScreens = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Storage.FileServerResourceManager.FsrmEnumOptions,POINTER(win32more.Storage.FileServerResourceManager.IFsrmCommittableCollection_head))(11, 'EnumFileScreens', ((1, 'path'),(1, 'options'),(1, 'fileScreens'),)))
    IFsrmFileScreenManager.CreateFileScreenException = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Storage.FileServerResourceManager.IFsrmFileScreenException_head))(12, 'CreateFileScreenException', ((1, 'path'),(1, 'fileScreenException'),)))
    IFsrmFileScreenManager.GetFileScreenException = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Storage.FileServerResourceManager.IFsrmFileScreenException_head))(13, 'GetFileScreenException', ((1, 'path'),(1, 'fileScreenException'),)))
    IFsrmFileScreenManager.EnumFileScreenExceptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Storage.FileServerResourceManager.FsrmEnumOptions,POINTER(win32more.Storage.FileServerResourceManager.IFsrmCommittableCollection_head))(14, 'EnumFileScreenExceptions', ((1, 'path'),(1, 'options'),(1, 'fileScreenExceptions'),)))
    IFsrmFileScreenManager.CreateFileScreenCollection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileServerResourceManager.IFsrmCommittableCollection_head))(15, 'CreateFileScreenCollection', ((1, 'collection'),)))
    win32more.System.Com.IDispatch
    return IFsrmFileScreenManager
def _define_IFsrmFileScreenTemplate_head():
    class IFsrmFileScreenTemplate(win32more.Storage.FileServerResourceManager.IFsrmFileScreenBase_head):
        Guid = Guid('205bebf8-dd93-452a-95-a6-32-b5-66-b3-58-28')
    return IFsrmFileScreenTemplate
def _define_IFsrmFileScreenTemplate():
    IFsrmFileScreenTemplate = win32more.Storage.FileServerResourceManager.IFsrmFileScreenTemplate_head
    IFsrmFileScreenTemplate.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(18, 'get_Name', ((1, 'name'),)))
    IFsrmFileScreenTemplate.put_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(19, 'put_Name', ((1, 'name'),)))
    IFsrmFileScreenTemplate.CopyTemplate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(20, 'CopyTemplate', ((1, 'fileScreenTemplateName'),)))
    IFsrmFileScreenTemplate.CommitAndUpdateDerived = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.FsrmCommitOptions,win32more.Storage.FileServerResourceManager.FsrmTemplateApplyOptions,POINTER(win32more.Storage.FileServerResourceManager.IFsrmDerivedObjectsResult_head))(21, 'CommitAndUpdateDerived', ((1, 'commitOptions'),(1, 'applyOptions'),(1, 'derivedObjectsResult'),)))
    win32more.Storage.FileServerResourceManager.IFsrmFileScreenBase
    return IFsrmFileScreenTemplate
def _define_IFsrmFileScreenTemplateImported_head():
    class IFsrmFileScreenTemplateImported(win32more.Storage.FileServerResourceManager.IFsrmFileScreenTemplate_head):
        Guid = Guid('e1010359-3e5d-4ecd-9f-e4-ef-48-62-2f-df-30')
    return IFsrmFileScreenTemplateImported
def _define_IFsrmFileScreenTemplateImported():
    IFsrmFileScreenTemplateImported = win32more.Storage.FileServerResourceManager.IFsrmFileScreenTemplateImported_head
    IFsrmFileScreenTemplateImported.get_OverwriteOnCommit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(22, 'get_OverwriteOnCommit', ((1, 'overwrite'),)))
    IFsrmFileScreenTemplateImported.put_OverwriteOnCommit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(23, 'put_OverwriteOnCommit', ((1, 'overwrite'),)))
    win32more.Storage.FileServerResourceManager.IFsrmFileScreenTemplate
    return IFsrmFileScreenTemplateImported
def _define_IFsrmFileScreenTemplateManager_head():
    class IFsrmFileScreenTemplateManager(win32more.System.Com.IDispatch_head):
        Guid = Guid('cfe36cba-1949-4e74-a1-4f-f1-d5-80-ce-af-13')
    return IFsrmFileScreenTemplateManager
def _define_IFsrmFileScreenTemplateManager():
    IFsrmFileScreenTemplateManager = win32more.Storage.FileServerResourceManager.IFsrmFileScreenTemplateManager_head
    IFsrmFileScreenTemplateManager.CreateTemplate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileServerResourceManager.IFsrmFileScreenTemplate_head))(7, 'CreateTemplate', ((1, 'fileScreenTemplate'),)))
    IFsrmFileScreenTemplateManager.GetTemplate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Storage.FileServerResourceManager.IFsrmFileScreenTemplate_head))(8, 'GetTemplate', ((1, 'name'),(1, 'fileScreenTemplate'),)))
    IFsrmFileScreenTemplateManager.EnumTemplates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.FsrmEnumOptions,POINTER(win32more.Storage.FileServerResourceManager.IFsrmCommittableCollection_head))(9, 'EnumTemplates', ((1, 'options'),(1, 'fileScreenTemplates'),)))
    IFsrmFileScreenTemplateManager.ExportTemplates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.Foundation.BSTR))(10, 'ExportTemplates', ((1, 'fileScreenTemplateNamesArray'),(1, 'serializedFileScreenTemplates'),)))
    IFsrmFileScreenTemplateManager.ImportTemplates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.Storage.FileServerResourceManager.IFsrmCommittableCollection_head))(11, 'ImportTemplates', ((1, 'serializedFileScreenTemplates'),(1, 'fileScreenTemplateNamesArray'),(1, 'fileScreenTemplates'),)))
    win32more.System.Com.IDispatch
    return IFsrmFileScreenTemplateManager
def _define_IFsrmMutableCollection_head():
    class IFsrmMutableCollection(win32more.Storage.FileServerResourceManager.IFsrmCollection_head):
        Guid = Guid('1bb617b8-3886-49dc-af-82-a6-c9-0f-a3-5d-da')
    return IFsrmMutableCollection
def _define_IFsrmMutableCollection():
    IFsrmMutableCollection = win32more.Storage.FileServerResourceManager.IFsrmMutableCollection_head
    IFsrmMutableCollection.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT)(14, 'Add', ((1, 'item'),)))
    IFsrmMutableCollection.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(15, 'Remove', ((1, 'index'),)))
    IFsrmMutableCollection.RemoveById = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid)(16, 'RemoveById', ((1, 'id'),)))
    IFsrmMutableCollection.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileServerResourceManager.IFsrmMutableCollection_head))(17, 'Clone', ((1, 'collection'),)))
    win32more.Storage.FileServerResourceManager.IFsrmCollection
    return IFsrmMutableCollection
def _define_IFsrmObject_head():
    class IFsrmObject(win32more.System.Com.IDispatch_head):
        Guid = Guid('22bcef93-4a3f-4183-89-f9-2f-8b-8a-62-8a-ee')
    return IFsrmObject
def _define_IFsrmObject():
    IFsrmObject = win32more.Storage.FileServerResourceManager.IFsrmObject_head
    IFsrmObject.get_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(7, 'get_Id', ((1, 'id'),)))
    IFsrmObject.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(8, 'get_Description', ((1, 'description'),)))
    IFsrmObject.put_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(9, 'put_Description', ((1, 'description'),)))
    IFsrmObject.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(10, 'Delete', ()))
    IFsrmObject.Commit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(11, 'Commit', ()))
    win32more.System.Com.IDispatch
    return IFsrmObject
def _define_IFsrmPathMapper_head():
    class IFsrmPathMapper(win32more.System.Com.IDispatch_head):
        Guid = Guid('6f4dbfff-6920-4821-a6-c3-b7-e9-4c-1f-d6-0c')
    return IFsrmPathMapper
def _define_IFsrmPathMapper():
    IFsrmPathMapper = win32more.Storage.FileServerResourceManager.IFsrmPathMapper_head
    IFsrmPathMapper.GetSharePathsForLocalPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(7, 'GetSharePathsForLocalPath', ((1, 'localPath'),(1, 'sharePaths'),)))
    win32more.System.Com.IDispatch
    return IFsrmPathMapper
def _define_IFsrmPipelineModuleConnector_head():
    class IFsrmPipelineModuleConnector(win32more.System.Com.IDispatch_head):
        Guid = Guid('c16014f3-9aa1-46b3-b0-a7-ab-14-6e-b2-05-f2')
    return IFsrmPipelineModuleConnector
def _define_IFsrmPipelineModuleConnector():
    IFsrmPipelineModuleConnector = win32more.Storage.FileServerResourceManager.IFsrmPipelineModuleConnector_head
    IFsrmPipelineModuleConnector.get_ModuleImplementation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileServerResourceManager.IFsrmPipelineModuleImplementation_head))(7, 'get_ModuleImplementation', ((1, 'pipelineModuleImplementation'),)))
    IFsrmPipelineModuleConnector.get_ModuleName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(8, 'get_ModuleName', ((1, 'userName'),)))
    IFsrmPipelineModuleConnector.get_HostingUserAccount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_HostingUserAccount', ((1, 'userAccount'),)))
    IFsrmPipelineModuleConnector.get_HostingProcessPid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(10, 'get_HostingProcessPid', ((1, 'pid'),)))
    IFsrmPipelineModuleConnector.Bind = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.IFsrmPipelineModuleDefinition_head,win32more.Storage.FileServerResourceManager.IFsrmPipelineModuleImplementation_head)(11, 'Bind', ((1, 'moduleDefinition'),(1, 'moduleImplementation'),)))
    win32more.System.Com.IDispatch
    return IFsrmPipelineModuleConnector
def _define_IFsrmPipelineModuleDefinition_head():
    class IFsrmPipelineModuleDefinition(win32more.Storage.FileServerResourceManager.IFsrmObject_head):
        Guid = Guid('515c1277-2c81-440e-8f-cf-36-79-21-ed-4f-59')
    return IFsrmPipelineModuleDefinition
def _define_IFsrmPipelineModuleDefinition():
    IFsrmPipelineModuleDefinition = win32more.Storage.FileServerResourceManager.IFsrmPipelineModuleDefinition_head
    IFsrmPipelineModuleDefinition.get_ModuleClsid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(12, 'get_ModuleClsid', ((1, 'moduleClsid'),)))
    IFsrmPipelineModuleDefinition.put_ModuleClsid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(13, 'put_ModuleClsid', ((1, 'moduleClsid'),)))
    IFsrmPipelineModuleDefinition.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(14, 'get_Name', ((1, 'name'),)))
    IFsrmPipelineModuleDefinition.put_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(15, 'put_Name', ((1, 'name'),)))
    IFsrmPipelineModuleDefinition.get_Company = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(16, 'get_Company', ((1, 'company'),)))
    IFsrmPipelineModuleDefinition.put_Company = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(17, 'put_Company', ((1, 'company'),)))
    IFsrmPipelineModuleDefinition.get_Version = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(18, 'get_Version', ((1, 'version'),)))
    IFsrmPipelineModuleDefinition.put_Version = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(19, 'put_Version', ((1, 'version'),)))
    IFsrmPipelineModuleDefinition.get_ModuleType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileServerResourceManager.FsrmPipelineModuleType))(20, 'get_ModuleType', ((1, 'moduleType'),)))
    IFsrmPipelineModuleDefinition.get_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(21, 'get_Enabled', ((1, 'enabled'),)))
    IFsrmPipelineModuleDefinition.put_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(22, 'put_Enabled', ((1, 'enabled'),)))
    IFsrmPipelineModuleDefinition.get_NeedsFileContent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(23, 'get_NeedsFileContent', ((1, 'needsFileContent'),)))
    IFsrmPipelineModuleDefinition.put_NeedsFileContent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(24, 'put_NeedsFileContent', ((1, 'needsFileContent'),)))
    IFsrmPipelineModuleDefinition.get_Account = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileServerResourceManager.FsrmAccountType))(25, 'get_Account', ((1, 'retrievalAccount'),)))
    IFsrmPipelineModuleDefinition.put_Account = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.FsrmAccountType)(26, 'put_Account', ((1, 'retrievalAccount'),)))
    IFsrmPipelineModuleDefinition.get_SupportedExtensions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(27, 'get_SupportedExtensions', ((1, 'supportedExtensions'),)))
    IFsrmPipelineModuleDefinition.put_SupportedExtensions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head))(28, 'put_SupportedExtensions', ((1, 'supportedExtensions'),)))
    IFsrmPipelineModuleDefinition.get_Parameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(29, 'get_Parameters', ((1, 'parameters'),)))
    IFsrmPipelineModuleDefinition.put_Parameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head))(30, 'put_Parameters', ((1, 'parameters'),)))
    win32more.Storage.FileServerResourceManager.IFsrmObject
    return IFsrmPipelineModuleDefinition
def _define_IFsrmPipelineModuleImplementation_head():
    class IFsrmPipelineModuleImplementation(win32more.System.Com.IDispatch_head):
        Guid = Guid('b7907906-2b02-4cb5-84-a9-fd-f5-46-13-d6-cd')
    return IFsrmPipelineModuleImplementation
def _define_IFsrmPipelineModuleImplementation():
    IFsrmPipelineModuleImplementation = win32more.Storage.FileServerResourceManager.IFsrmPipelineModuleImplementation_head
    IFsrmPipelineModuleImplementation.OnLoad = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.IFsrmPipelineModuleDefinition_head,POINTER(win32more.Storage.FileServerResourceManager.IFsrmPipelineModuleConnector_head))(7, 'OnLoad', ((1, 'moduleDefinition'),(1, 'moduleConnector'),)))
    IFsrmPipelineModuleImplementation.OnUnload = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(8, 'OnUnload', ()))
    win32more.System.Com.IDispatch
    return IFsrmPipelineModuleImplementation
def _define_IFsrmProperty_head():
    class IFsrmProperty(win32more.System.Com.IDispatch_head):
        Guid = Guid('4a73fee4-4102-4fcc-9f-fb-38-61-4f-9e-e7-68')
    return IFsrmProperty
def _define_IFsrmProperty():
    IFsrmProperty = win32more.Storage.FileServerResourceManager.IFsrmProperty_head
    IFsrmProperty.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_Name', ((1, 'name'),)))
    IFsrmProperty.get_Value = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(8, 'get_Value', ((1, 'value'),)))
    IFsrmProperty.get_Sources = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(9, 'get_Sources', ((1, 'sources'),)))
    IFsrmProperty.get_PropertyFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(10, 'get_PropertyFlags', ((1, 'flags'),)))
    win32more.System.Com.IDispatch
    return IFsrmProperty
def _define_IFsrmPropertyBag_head():
    class IFsrmPropertyBag(win32more.System.Com.IDispatch_head):
        Guid = Guid('774589d1-d300-4f7a-9a-24-f7-b7-66-80-02-50')
    return IFsrmPropertyBag
def _define_IFsrmPropertyBag():
    IFsrmPropertyBag = win32more.Storage.FileServerResourceManager.IFsrmPropertyBag_head
    IFsrmPropertyBag.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_Name', ((1, 'name'),)))
    IFsrmPropertyBag.get_RelativePath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(8, 'get_RelativePath', ((1, 'path'),)))
    IFsrmPropertyBag.get_VolumeName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_VolumeName', ((1, 'volumeName'),)))
    IFsrmPropertyBag.get_RelativeNamespaceRoot = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(10, 'get_RelativeNamespaceRoot', ((1, 'relativeNamespaceRoot'),)))
    IFsrmPropertyBag.get_VolumeIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(11, 'get_VolumeIndex', ((1, 'volumeId'),)))
    IFsrmPropertyBag.get_FileId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(12, 'get_FileId', ((1, 'fileId'),)))
    IFsrmPropertyBag.get_ParentDirectoryId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(13, 'get_ParentDirectoryId', ((1, 'parentDirectoryId'),)))
    IFsrmPropertyBag.get_Size = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(14, 'get_Size', ((1, 'size'),)))
    IFsrmPropertyBag.get_SizeAllocated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(15, 'get_SizeAllocated', ((1, 'sizeAllocated'),)))
    IFsrmPropertyBag.get_CreationTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(16, 'get_CreationTime', ((1, 'creationTime'),)))
    IFsrmPropertyBag.get_LastAccessTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(17, 'get_LastAccessTime', ((1, 'lastAccessTime'),)))
    IFsrmPropertyBag.get_LastModificationTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(18, 'get_LastModificationTime', ((1, 'lastModificationTime'),)))
    IFsrmPropertyBag.get_Attributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(19, 'get_Attributes', ((1, 'attributes'),)))
    IFsrmPropertyBag.get_OwnerSid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(20, 'get_OwnerSid', ((1, 'ownerSid'),)))
    IFsrmPropertyBag.get_FilePropertyNames = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(21, 'get_FilePropertyNames', ((1, 'filePropertyNames'),)))
    IFsrmPropertyBag.get_Messages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(22, 'get_Messages', ((1, 'messages'),)))
    IFsrmPropertyBag.get_PropertyBagFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(23, 'get_PropertyBagFlags', ((1, 'flags'),)))
    IFsrmPropertyBag.GetFileProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Storage.FileServerResourceManager.IFsrmProperty_head))(24, 'GetFileProperty', ((1, 'name'),(1, 'fileProperty'),)))
    IFsrmPropertyBag.SetFileProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR)(25, 'SetFileProperty', ((1, 'name'),(1, 'value'),)))
    IFsrmPropertyBag.AddMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(26, 'AddMessage', ((1, 'message'),)))
    IFsrmPropertyBag.GetFileStreamInterface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.FsrmFileStreamingMode,win32more.Storage.FileServerResourceManager.FsrmFileStreamingInterfaceType,POINTER(win32more.System.Com.VARIANT_head))(27, 'GetFileStreamInterface', ((1, 'accessMode'),(1, 'interfaceType'),(1, 'pStreamInterface'),)))
    win32more.System.Com.IDispatch
    return IFsrmPropertyBag
def _define_IFsrmPropertyBag2_head():
    class IFsrmPropertyBag2(win32more.Storage.FileServerResourceManager.IFsrmPropertyBag_head):
        Guid = Guid('0e46bdbd-2402-4fed-9c-30-92-66-e6-eb-2c-c9')
    return IFsrmPropertyBag2
def _define_IFsrmPropertyBag2():
    IFsrmPropertyBag2 = win32more.Storage.FileServerResourceManager.IFsrmPropertyBag2_head
    IFsrmPropertyBag2.GetFieldValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.FsrmPropertyBagField,POINTER(win32more.System.Com.VARIANT_head))(28, 'GetFieldValue', ((1, 'field'),(1, 'value'),)))
    IFsrmPropertyBag2.GetUntrustedInFileProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileServerResourceManager.IFsrmCollection_head))(29, 'GetUntrustedInFileProperties', ((1, 'props'),)))
    win32more.Storage.FileServerResourceManager.IFsrmPropertyBag
    return IFsrmPropertyBag2
def _define_IFsrmPropertyCondition_head():
    class IFsrmPropertyCondition(win32more.System.Com.IDispatch_head):
        Guid = Guid('326af66f-2ac0-4f68-bf-8c-47-59-f0-54-fa-29')
    return IFsrmPropertyCondition
def _define_IFsrmPropertyCondition():
    IFsrmPropertyCondition = win32more.Storage.FileServerResourceManager.IFsrmPropertyCondition_head
    IFsrmPropertyCondition.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_Name', ((1, 'name'),)))
    IFsrmPropertyCondition.put_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(8, 'put_Name', ((1, 'name'),)))
    IFsrmPropertyCondition.get_Type = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileServerResourceManager.FsrmPropertyConditionType))(9, 'get_Type', ((1, 'type'),)))
    IFsrmPropertyCondition.put_Type = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.FsrmPropertyConditionType)(10, 'put_Type', ((1, 'type'),)))
    IFsrmPropertyCondition.get_Value = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(11, 'get_Value', ((1, 'value'),)))
    IFsrmPropertyCondition.put_Value = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(12, 'put_Value', ((1, 'value'),)))
    IFsrmPropertyCondition.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(13, 'Delete', ()))
    win32more.System.Com.IDispatch
    return IFsrmPropertyCondition
def _define_IFsrmPropertyDefinition_head():
    class IFsrmPropertyDefinition(win32more.Storage.FileServerResourceManager.IFsrmObject_head):
        Guid = Guid('ede0150f-e9a3-419c-87-7c-01-fe-5d-24-c5-d3')
    return IFsrmPropertyDefinition
def _define_IFsrmPropertyDefinition():
    IFsrmPropertyDefinition = win32more.Storage.FileServerResourceManager.IFsrmPropertyDefinition_head
    IFsrmPropertyDefinition.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(12, 'get_Name', ((1, 'name'),)))
    IFsrmPropertyDefinition.put_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(13, 'put_Name', ((1, 'name'),)))
    IFsrmPropertyDefinition.get_Type = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileServerResourceManager.FsrmPropertyDefinitionType))(14, 'get_Type', ((1, 'type'),)))
    IFsrmPropertyDefinition.put_Type = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.FsrmPropertyDefinitionType)(15, 'put_Type', ((1, 'type'),)))
    IFsrmPropertyDefinition.get_PossibleValues = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(16, 'get_PossibleValues', ((1, 'possibleValues'),)))
    IFsrmPropertyDefinition.put_PossibleValues = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head))(17, 'put_PossibleValues', ((1, 'possibleValues'),)))
    IFsrmPropertyDefinition.get_ValueDescriptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(18, 'get_ValueDescriptions', ((1, 'valueDescriptions'),)))
    IFsrmPropertyDefinition.put_ValueDescriptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head))(19, 'put_ValueDescriptions', ((1, 'valueDescriptions'),)))
    IFsrmPropertyDefinition.get_Parameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(20, 'get_Parameters', ((1, 'parameters'),)))
    IFsrmPropertyDefinition.put_Parameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head))(21, 'put_Parameters', ((1, 'parameters'),)))
    win32more.Storage.FileServerResourceManager.IFsrmObject
    return IFsrmPropertyDefinition
def _define_IFsrmPropertyDefinition2_head():
    class IFsrmPropertyDefinition2(win32more.Storage.FileServerResourceManager.IFsrmPropertyDefinition_head):
        Guid = Guid('47782152-d16c-4229-b4-e1-0d-df-e3-08-b9-f6')
    return IFsrmPropertyDefinition2
def _define_IFsrmPropertyDefinition2():
    IFsrmPropertyDefinition2 = win32more.Storage.FileServerResourceManager.IFsrmPropertyDefinition2_head
    IFsrmPropertyDefinition2.get_PropertyDefinitionFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(22, 'get_PropertyDefinitionFlags', ((1, 'propertyDefinitionFlags'),)))
    IFsrmPropertyDefinition2.get_DisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(23, 'get_DisplayName', ((1, 'name'),)))
    IFsrmPropertyDefinition2.put_DisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(24, 'put_DisplayName', ((1, 'name'),)))
    IFsrmPropertyDefinition2.get_AppliesTo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(25, 'get_AppliesTo', ((1, 'appliesTo'),)))
    IFsrmPropertyDefinition2.get_ValueDefinitions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileServerResourceManager.IFsrmCollection_head))(26, 'get_ValueDefinitions', ((1, 'valueDefinitions'),)))
    win32more.Storage.FileServerResourceManager.IFsrmPropertyDefinition
    return IFsrmPropertyDefinition2
def _define_IFsrmPropertyDefinitionValue_head():
    class IFsrmPropertyDefinitionValue(win32more.System.Com.IDispatch_head):
        Guid = Guid('e946d148-bd67-4178-8e-22-1c-44-92-5e-d7-10')
    return IFsrmPropertyDefinitionValue
def _define_IFsrmPropertyDefinitionValue():
    IFsrmPropertyDefinitionValue = win32more.Storage.FileServerResourceManager.IFsrmPropertyDefinitionValue_head
    IFsrmPropertyDefinitionValue.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_Name', ((1, 'name'),)))
    IFsrmPropertyDefinitionValue.get_DisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(8, 'get_DisplayName', ((1, 'displayName'),)))
    IFsrmPropertyDefinitionValue.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_Description', ((1, 'description'),)))
    IFsrmPropertyDefinitionValue.get_UniqueID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(10, 'get_UniqueID', ((1, 'uniqueID'),)))
    win32more.System.Com.IDispatch
    return IFsrmPropertyDefinitionValue
def _define_IFsrmQuota_head():
    class IFsrmQuota(win32more.Storage.FileServerResourceManager.IFsrmQuotaObject_head):
        Guid = Guid('377f739d-9647-4b8e-97-d2-5f-fc-e6-d7-59-cd')
    return IFsrmQuota
def _define_IFsrmQuota():
    IFsrmQuota = win32more.Storage.FileServerResourceManager.IFsrmQuota_head
    IFsrmQuota.get_QuotaUsed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(28, 'get_QuotaUsed', ((1, 'used'),)))
    IFsrmQuota.get_QuotaPeakUsage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(29, 'get_QuotaPeakUsage', ((1, 'peakUsage'),)))
    IFsrmQuota.get_QuotaPeakUsageTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(30, 'get_QuotaPeakUsageTime', ((1, 'peakUsageDateTime'),)))
    IFsrmQuota.ResetPeakUsage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(31, 'ResetPeakUsage', ()))
    IFsrmQuota.RefreshUsageProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(32, 'RefreshUsageProperties', ()))
    win32more.Storage.FileServerResourceManager.IFsrmQuotaObject
    return IFsrmQuota
def _define_IFsrmQuotaBase_head():
    class IFsrmQuotaBase(win32more.Storage.FileServerResourceManager.IFsrmObject_head):
        Guid = Guid('1568a795-3924-4118-b7-4b-68-d8-f0-fa-5d-af')
    return IFsrmQuotaBase
def _define_IFsrmQuotaBase():
    IFsrmQuotaBase = win32more.Storage.FileServerResourceManager.IFsrmQuotaBase_head
    IFsrmQuotaBase.get_QuotaLimit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(12, 'get_QuotaLimit', ((1, 'quotaLimit'),)))
    IFsrmQuotaBase.put_QuotaLimit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT)(13, 'put_QuotaLimit', ((1, 'quotaLimit'),)))
    IFsrmQuotaBase.get_QuotaFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(14, 'get_QuotaFlags', ((1, 'quotaFlags'),)))
    IFsrmQuotaBase.put_QuotaFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(15, 'put_QuotaFlags', ((1, 'quotaFlags'),)))
    IFsrmQuotaBase.get_Thresholds = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(16, 'get_Thresholds', ((1, 'thresholds'),)))
    IFsrmQuotaBase.AddThreshold = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(17, 'AddThreshold', ((1, 'threshold'),)))
    IFsrmQuotaBase.DeleteThreshold = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(18, 'DeleteThreshold', ((1, 'threshold'),)))
    IFsrmQuotaBase.ModifyThreshold = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32)(19, 'ModifyThreshold', ((1, 'threshold'),(1, 'newThreshold'),)))
    IFsrmQuotaBase.CreateThresholdAction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Storage.FileServerResourceManager.FsrmActionType,POINTER(win32more.Storage.FileServerResourceManager.IFsrmAction_head))(20, 'CreateThresholdAction', ((1, 'threshold'),(1, 'actionType'),(1, 'action'),)))
    IFsrmQuotaBase.EnumThresholdActions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Storage.FileServerResourceManager.IFsrmCollection_head))(21, 'EnumThresholdActions', ((1, 'threshold'),(1, 'actions'),)))
    win32more.Storage.FileServerResourceManager.IFsrmObject
    return IFsrmQuotaBase
def _define_IFsrmQuotaManager_head():
    class IFsrmQuotaManager(win32more.System.Com.IDispatch_head):
        Guid = Guid('8bb68c7d-19d8-4ffb-80-9e-be-4f-c1-73-40-14')
    return IFsrmQuotaManager
def _define_IFsrmQuotaManager():
    IFsrmQuotaManager = win32more.Storage.FileServerResourceManager.IFsrmQuotaManager_head
    IFsrmQuotaManager.get_ActionVariables = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(7, 'get_ActionVariables', ((1, 'variables'),)))
    IFsrmQuotaManager.get_ActionVariableDescriptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(8, 'get_ActionVariableDescriptions', ((1, 'descriptions'),)))
    IFsrmQuotaManager.CreateQuota = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Storage.FileServerResourceManager.IFsrmQuota_head))(9, 'CreateQuota', ((1, 'path'),(1, 'quota'),)))
    IFsrmQuotaManager.CreateAutoApplyQuota = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.Storage.FileServerResourceManager.IFsrmAutoApplyQuota_head))(10, 'CreateAutoApplyQuota', ((1, 'quotaTemplateName'),(1, 'path'),(1, 'quota'),)))
    IFsrmQuotaManager.GetQuota = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Storage.FileServerResourceManager.IFsrmQuota_head))(11, 'GetQuota', ((1, 'path'),(1, 'quota'),)))
    IFsrmQuotaManager.GetAutoApplyQuota = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Storage.FileServerResourceManager.IFsrmAutoApplyQuota_head))(12, 'GetAutoApplyQuota', ((1, 'path'),(1, 'quota'),)))
    IFsrmQuotaManager.GetRestrictiveQuota = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Storage.FileServerResourceManager.IFsrmQuota_head))(13, 'GetRestrictiveQuota', ((1, 'path'),(1, 'quota'),)))
    IFsrmQuotaManager.EnumQuotas = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Storage.FileServerResourceManager.FsrmEnumOptions,POINTER(win32more.Storage.FileServerResourceManager.IFsrmCommittableCollection_head))(14, 'EnumQuotas', ((1, 'path'),(1, 'options'),(1, 'quotas'),)))
    IFsrmQuotaManager.EnumAutoApplyQuotas = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Storage.FileServerResourceManager.FsrmEnumOptions,POINTER(win32more.Storage.FileServerResourceManager.IFsrmCommittableCollection_head))(15, 'EnumAutoApplyQuotas', ((1, 'path'),(1, 'options'),(1, 'quotas'),)))
    IFsrmQuotaManager.EnumEffectiveQuotas = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Storage.FileServerResourceManager.FsrmEnumOptions,POINTER(win32more.Storage.FileServerResourceManager.IFsrmCommittableCollection_head))(16, 'EnumEffectiveQuotas', ((1, 'path'),(1, 'options'),(1, 'quotas'),)))
    IFsrmQuotaManager.Scan = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(17, 'Scan', ((1, 'strPath'),)))
    IFsrmQuotaManager.CreateQuotaCollection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileServerResourceManager.IFsrmCommittableCollection_head))(18, 'CreateQuotaCollection', ((1, 'collection'),)))
    win32more.System.Com.IDispatch
    return IFsrmQuotaManager
def _define_IFsrmQuotaManagerEx_head():
    class IFsrmQuotaManagerEx(win32more.Storage.FileServerResourceManager.IFsrmQuotaManager_head):
        Guid = Guid('4846cb01-d430-494f-ab-b4-b1-05-49-99-fb-09')
    return IFsrmQuotaManagerEx
def _define_IFsrmQuotaManagerEx():
    IFsrmQuotaManagerEx = win32more.Storage.FileServerResourceManager.IFsrmQuotaManagerEx_head
    IFsrmQuotaManagerEx.IsAffectedByQuota = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Storage.FileServerResourceManager.FsrmEnumOptions,POINTER(win32more.Foundation.VARIANT_BOOL))(19, 'IsAffectedByQuota', ((1, 'path'),(1, 'options'),(1, 'affected'),)))
    win32more.Storage.FileServerResourceManager.IFsrmQuotaManager
    return IFsrmQuotaManagerEx
def _define_IFsrmQuotaObject_head():
    class IFsrmQuotaObject(win32more.Storage.FileServerResourceManager.IFsrmQuotaBase_head):
        Guid = Guid('42dc3511-61d5-48ae-b6-dc-59-fc-00-c0-a8-d6')
    return IFsrmQuotaObject
def _define_IFsrmQuotaObject():
    IFsrmQuotaObject = win32more.Storage.FileServerResourceManager.IFsrmQuotaObject_head
    IFsrmQuotaObject.get_Path = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(22, 'get_Path', ((1, 'path'),)))
    IFsrmQuotaObject.get_UserSid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(23, 'get_UserSid', ((1, 'userSid'),)))
    IFsrmQuotaObject.get_UserAccount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(24, 'get_UserAccount', ((1, 'userAccount'),)))
    IFsrmQuotaObject.get_SourceTemplateName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(25, 'get_SourceTemplateName', ((1, 'quotaTemplateName'),)))
    IFsrmQuotaObject.get_MatchesSourceTemplate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(26, 'get_MatchesSourceTemplate', ((1, 'matches'),)))
    IFsrmQuotaObject.ApplyTemplate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(27, 'ApplyTemplate', ((1, 'quotaTemplateName'),)))
    win32more.Storage.FileServerResourceManager.IFsrmQuotaBase
    return IFsrmQuotaObject
def _define_IFsrmQuotaTemplate_head():
    class IFsrmQuotaTemplate(win32more.Storage.FileServerResourceManager.IFsrmQuotaBase_head):
        Guid = Guid('a2efab31-295e-46bb-b9-76-e8-6d-58-b5-2e-8b')
    return IFsrmQuotaTemplate
def _define_IFsrmQuotaTemplate():
    IFsrmQuotaTemplate = win32more.Storage.FileServerResourceManager.IFsrmQuotaTemplate_head
    IFsrmQuotaTemplate.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(22, 'get_Name', ((1, 'name'),)))
    IFsrmQuotaTemplate.put_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(23, 'put_Name', ((1, 'name'),)))
    IFsrmQuotaTemplate.CopyTemplate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(24, 'CopyTemplate', ((1, 'quotaTemplateName'),)))
    IFsrmQuotaTemplate.CommitAndUpdateDerived = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.FsrmCommitOptions,win32more.Storage.FileServerResourceManager.FsrmTemplateApplyOptions,POINTER(win32more.Storage.FileServerResourceManager.IFsrmDerivedObjectsResult_head))(25, 'CommitAndUpdateDerived', ((1, 'commitOptions'),(1, 'applyOptions'),(1, 'derivedObjectsResult'),)))
    win32more.Storage.FileServerResourceManager.IFsrmQuotaBase
    return IFsrmQuotaTemplate
def _define_IFsrmQuotaTemplateImported_head():
    class IFsrmQuotaTemplateImported(win32more.Storage.FileServerResourceManager.IFsrmQuotaTemplate_head):
        Guid = Guid('9a2bf113-a329-44cc-80-9a-5c-00-fc-e8-da-40')
    return IFsrmQuotaTemplateImported
def _define_IFsrmQuotaTemplateImported():
    IFsrmQuotaTemplateImported = win32more.Storage.FileServerResourceManager.IFsrmQuotaTemplateImported_head
    IFsrmQuotaTemplateImported.get_OverwriteOnCommit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(26, 'get_OverwriteOnCommit', ((1, 'overwrite'),)))
    IFsrmQuotaTemplateImported.put_OverwriteOnCommit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(27, 'put_OverwriteOnCommit', ((1, 'overwrite'),)))
    win32more.Storage.FileServerResourceManager.IFsrmQuotaTemplate
    return IFsrmQuotaTemplateImported
def _define_IFsrmQuotaTemplateManager_head():
    class IFsrmQuotaTemplateManager(win32more.System.Com.IDispatch_head):
        Guid = Guid('4173ac41-172d-4d52-96-3c-fd-c7-e4-15-f7-17')
    return IFsrmQuotaTemplateManager
def _define_IFsrmQuotaTemplateManager():
    IFsrmQuotaTemplateManager = win32more.Storage.FileServerResourceManager.IFsrmQuotaTemplateManager_head
    IFsrmQuotaTemplateManager.CreateTemplate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileServerResourceManager.IFsrmQuotaTemplate_head))(7, 'CreateTemplate', ((1, 'quotaTemplate'),)))
    IFsrmQuotaTemplateManager.GetTemplate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Storage.FileServerResourceManager.IFsrmQuotaTemplate_head))(8, 'GetTemplate', ((1, 'name'),(1, 'quotaTemplate'),)))
    IFsrmQuotaTemplateManager.EnumTemplates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.FsrmEnumOptions,POINTER(win32more.Storage.FileServerResourceManager.IFsrmCommittableCollection_head))(9, 'EnumTemplates', ((1, 'options'),(1, 'quotaTemplates'),)))
    IFsrmQuotaTemplateManager.ExportTemplates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.Foundation.BSTR))(10, 'ExportTemplates', ((1, 'quotaTemplateNamesArray'),(1, 'serializedQuotaTemplates'),)))
    IFsrmQuotaTemplateManager.ImportTemplates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.Storage.FileServerResourceManager.IFsrmCommittableCollection_head))(11, 'ImportTemplates', ((1, 'serializedQuotaTemplates'),(1, 'quotaTemplateNamesArray'),(1, 'quotaTemplates'),)))
    win32more.System.Com.IDispatch
    return IFsrmQuotaTemplateManager
def _define_IFsrmReport_head():
    class IFsrmReport(win32more.System.Com.IDispatch_head):
        Guid = Guid('d8cc81d9-46b8-4fa4-bf-a5-4a-a9-de-c9-b6-38')
    return IFsrmReport
def _define_IFsrmReport():
    IFsrmReport = win32more.Storage.FileServerResourceManager.IFsrmReport_head
    IFsrmReport.get_Type = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileServerResourceManager.FsrmReportType))(7, 'get_Type', ((1, 'reportType'),)))
    IFsrmReport.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(8, 'get_Name', ((1, 'name'),)))
    IFsrmReport.put_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(9, 'put_Name', ((1, 'name'),)))
    IFsrmReport.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(10, 'get_Description', ((1, 'description'),)))
    IFsrmReport.put_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(11, 'put_Description', ((1, 'description'),)))
    IFsrmReport.get_LastGeneratedFileNamePrefix = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(12, 'get_LastGeneratedFileNamePrefix', ((1, 'prefix'),)))
    IFsrmReport.GetFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.FsrmReportFilter,POINTER(win32more.System.Com.VARIANT_head))(13, 'GetFilter', ((1, 'filter'),(1, 'filterValue'),)))
    IFsrmReport.SetFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.FsrmReportFilter,win32more.System.Com.VARIANT)(14, 'SetFilter', ((1, 'filter'),(1, 'filterValue'),)))
    IFsrmReport.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(15, 'Delete', ()))
    win32more.System.Com.IDispatch
    return IFsrmReport
def _define_IFsrmReportJob_head():
    class IFsrmReportJob(win32more.Storage.FileServerResourceManager.IFsrmObject_head):
        Guid = Guid('38e87280-715c-4c7d-a2-80-ea-16-51-a1-9f-ef')
    return IFsrmReportJob
def _define_IFsrmReportJob():
    IFsrmReportJob = win32more.Storage.FileServerResourceManager.IFsrmReportJob_head
    IFsrmReportJob.get_Task = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(12, 'get_Task', ((1, 'taskName'),)))
    IFsrmReportJob.put_Task = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(13, 'put_Task', ((1, 'taskName'),)))
    IFsrmReportJob.get_NamespaceRoots = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(14, 'get_NamespaceRoots', ((1, 'namespaceRoots'),)))
    IFsrmReportJob.put_NamespaceRoots = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head))(15, 'put_NamespaceRoots', ((1, 'namespaceRoots'),)))
    IFsrmReportJob.get_Formats = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(16, 'get_Formats', ((1, 'formats'),)))
    IFsrmReportJob.put_Formats = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head))(17, 'put_Formats', ((1, 'formats'),)))
    IFsrmReportJob.get_MailTo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(18, 'get_MailTo', ((1, 'mailTo'),)))
    IFsrmReportJob.put_MailTo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(19, 'put_MailTo', ((1, 'mailTo'),)))
    IFsrmReportJob.get_RunningStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileServerResourceManager.FsrmReportRunningStatus))(20, 'get_RunningStatus', ((1, 'runningStatus'),)))
    IFsrmReportJob.get_LastRun = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(21, 'get_LastRun', ((1, 'lastRun'),)))
    IFsrmReportJob.get_LastError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(22, 'get_LastError', ((1, 'lastError'),)))
    IFsrmReportJob.get_LastGeneratedInDirectory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(23, 'get_LastGeneratedInDirectory', ((1, 'path'),)))
    IFsrmReportJob.EnumReports = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileServerResourceManager.IFsrmCollection_head))(24, 'EnumReports', ((1, 'reports'),)))
    IFsrmReportJob.CreateReport = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.FsrmReportType,POINTER(win32more.Storage.FileServerResourceManager.IFsrmReport_head))(25, 'CreateReport', ((1, 'reportType'),(1, 'report'),)))
    IFsrmReportJob.Run = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.FsrmReportGenerationContext)(26, 'Run', ((1, 'context'),)))
    IFsrmReportJob.WaitForCompletion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.VARIANT_BOOL))(27, 'WaitForCompletion', ((1, 'waitSeconds'),(1, 'completed'),)))
    IFsrmReportJob.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(28, 'Cancel', ()))
    win32more.Storage.FileServerResourceManager.IFsrmObject
    return IFsrmReportJob
def _define_IFsrmReportManager_head():
    class IFsrmReportManager(win32more.System.Com.IDispatch_head):
        Guid = Guid('27b899fe-6ffa-4481-a1-84-d3-da-ad-e8-a0-2b')
    return IFsrmReportManager
def _define_IFsrmReportManager():
    IFsrmReportManager = win32more.Storage.FileServerResourceManager.IFsrmReportManager_head
    IFsrmReportManager.EnumReportJobs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.FsrmEnumOptions,POINTER(win32more.Storage.FileServerResourceManager.IFsrmCollection_head))(7, 'EnumReportJobs', ((1, 'options'),(1, 'reportJobs'),)))
    IFsrmReportManager.CreateReportJob = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileServerResourceManager.IFsrmReportJob_head))(8, 'CreateReportJob', ((1, 'reportJob'),)))
    IFsrmReportManager.GetReportJob = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Storage.FileServerResourceManager.IFsrmReportJob_head))(9, 'GetReportJob', ((1, 'taskName'),(1, 'reportJob'),)))
    IFsrmReportManager.GetOutputDirectory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.FsrmReportGenerationContext,POINTER(win32more.Foundation.BSTR))(10, 'GetOutputDirectory', ((1, 'context'),(1, 'path'),)))
    IFsrmReportManager.SetOutputDirectory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.FsrmReportGenerationContext,win32more.Foundation.BSTR)(11, 'SetOutputDirectory', ((1, 'context'),(1, 'path'),)))
    IFsrmReportManager.IsFilterValidForReportType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.FsrmReportType,win32more.Storage.FileServerResourceManager.FsrmReportFilter,POINTER(win32more.Foundation.VARIANT_BOOL))(12, 'IsFilterValidForReportType', ((1, 'reportType'),(1, 'filter'),(1, 'valid'),)))
    IFsrmReportManager.GetDefaultFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.FsrmReportType,win32more.Storage.FileServerResourceManager.FsrmReportFilter,POINTER(win32more.System.Com.VARIANT_head))(13, 'GetDefaultFilter', ((1, 'reportType'),(1, 'filter'),(1, 'filterValue'),)))
    IFsrmReportManager.SetDefaultFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.FsrmReportType,win32more.Storage.FileServerResourceManager.FsrmReportFilter,win32more.System.Com.VARIANT)(14, 'SetDefaultFilter', ((1, 'reportType'),(1, 'filter'),(1, 'filterValue'),)))
    IFsrmReportManager.GetReportSizeLimit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.FsrmReportLimit,POINTER(win32more.System.Com.VARIANT_head))(15, 'GetReportSizeLimit', ((1, 'limit'),(1, 'limitValue'),)))
    IFsrmReportManager.SetReportSizeLimit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.FsrmReportLimit,win32more.System.Com.VARIANT)(16, 'SetReportSizeLimit', ((1, 'limit'),(1, 'limitValue'),)))
    win32more.System.Com.IDispatch
    return IFsrmReportManager
def _define_IFsrmReportScheduler_head():
    class IFsrmReportScheduler(win32more.System.Com.IDispatch_head):
        Guid = Guid('6879caf9-6617-4484-87-19-71-c3-d8-64-5f-94')
    return IFsrmReportScheduler
def _define_IFsrmReportScheduler():
    IFsrmReportScheduler = win32more.Storage.FileServerResourceManager.IFsrmReportScheduler_head
    IFsrmReportScheduler.VerifyNamespaces = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(7, 'VerifyNamespaces', ((1, 'namespacesSafeArray'),)))
    IFsrmReportScheduler.CreateScheduleTask = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head),win32more.Foundation.BSTR)(8, 'CreateScheduleTask', ((1, 'taskName'),(1, 'namespacesSafeArray'),(1, 'serializedTask'),)))
    IFsrmReportScheduler.ModifyScheduleTask = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head),win32more.Foundation.BSTR)(9, 'ModifyScheduleTask', ((1, 'taskName'),(1, 'namespacesSafeArray'),(1, 'serializedTask'),)))
    IFsrmReportScheduler.DeleteScheduleTask = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(10, 'DeleteScheduleTask', ((1, 'taskName'),)))
    win32more.System.Com.IDispatch
    return IFsrmReportScheduler
def _define_IFsrmRule_head():
    class IFsrmRule(win32more.Storage.FileServerResourceManager.IFsrmObject_head):
        Guid = Guid('cb0df960-16f5-4495-90-79-3f-93-60-d8-31-df')
    return IFsrmRule
def _define_IFsrmRule():
    IFsrmRule = win32more.Storage.FileServerResourceManager.IFsrmRule_head
    IFsrmRule.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(12, 'get_Name', ((1, 'name'),)))
    IFsrmRule.put_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(13, 'put_Name', ((1, 'name'),)))
    IFsrmRule.get_RuleType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileServerResourceManager.FsrmRuleType))(14, 'get_RuleType', ((1, 'ruleType'),)))
    IFsrmRule.get_ModuleDefinitionName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(15, 'get_ModuleDefinitionName', ((1, 'moduleDefinitionName'),)))
    IFsrmRule.put_ModuleDefinitionName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(16, 'put_ModuleDefinitionName', ((1, 'moduleDefinitionName'),)))
    IFsrmRule.get_NamespaceRoots = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(17, 'get_NamespaceRoots', ((1, 'namespaceRoots'),)))
    IFsrmRule.put_NamespaceRoots = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head))(18, 'put_NamespaceRoots', ((1, 'namespaceRoots'),)))
    IFsrmRule.get_RuleFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(19, 'get_RuleFlags', ((1, 'ruleFlags'),)))
    IFsrmRule.put_RuleFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(20, 'put_RuleFlags', ((1, 'ruleFlags'),)))
    IFsrmRule.get_Parameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(21, 'get_Parameters', ((1, 'parameters'),)))
    IFsrmRule.put_Parameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head))(22, 'put_Parameters', ((1, 'parameters'),)))
    IFsrmRule.get_LastModified = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(23, 'get_LastModified', ((1, 'lastModified'),)))
    win32more.Storage.FileServerResourceManager.IFsrmObject
    return IFsrmRule
def _define_IFsrmSetting_head():
    class IFsrmSetting(win32more.System.Com.IDispatch_head):
        Guid = Guid('f411d4fd-14be-4260-8c-40-03-b7-c9-5e-60-8a')
    return IFsrmSetting
def _define_IFsrmSetting():
    IFsrmSetting = win32more.Storage.FileServerResourceManager.IFsrmSetting_head
    IFsrmSetting.get_SmtpServer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_SmtpServer', ((1, 'smtpServer'),)))
    IFsrmSetting.put_SmtpServer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(8, 'put_SmtpServer', ((1, 'smtpServer'),)))
    IFsrmSetting.get_MailFrom = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_MailFrom', ((1, 'mailFrom'),)))
    IFsrmSetting.put_MailFrom = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(10, 'put_MailFrom', ((1, 'mailFrom'),)))
    IFsrmSetting.get_AdminEmail = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(11, 'get_AdminEmail', ((1, 'adminEmail'),)))
    IFsrmSetting.put_AdminEmail = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(12, 'put_AdminEmail', ((1, 'adminEmail'),)))
    IFsrmSetting.get_DisableCommandLine = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(13, 'get_DisableCommandLine', ((1, 'disableCommandLine'),)))
    IFsrmSetting.put_DisableCommandLine = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(14, 'put_DisableCommandLine', ((1, 'disableCommandLine'),)))
    IFsrmSetting.get_EnableScreeningAudit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(15, 'get_EnableScreeningAudit', ((1, 'enableScreeningAudit'),)))
    IFsrmSetting.put_EnableScreeningAudit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(16, 'put_EnableScreeningAudit', ((1, 'enableScreeningAudit'),)))
    IFsrmSetting.EmailTest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(17, 'EmailTest', ((1, 'mailTo'),)))
    IFsrmSetting.SetActionRunLimitInterval = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.FsrmActionType,Int32)(18, 'SetActionRunLimitInterval', ((1, 'actionType'),(1, 'delayTimeMinutes'),)))
    IFsrmSetting.GetActionRunLimitInterval = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.FsrmActionType,POINTER(Int32))(19, 'GetActionRunLimitInterval', ((1, 'actionType'),(1, 'delayTimeMinutes'),)))
    win32more.System.Com.IDispatch
    return IFsrmSetting
def _define_IFsrmStorageModuleDefinition_head():
    class IFsrmStorageModuleDefinition(win32more.Storage.FileServerResourceManager.IFsrmPipelineModuleDefinition_head):
        Guid = Guid('15a81350-497d-4aba-80-e9-d4-db-cc-55-21-fe')
    return IFsrmStorageModuleDefinition
def _define_IFsrmStorageModuleDefinition():
    IFsrmStorageModuleDefinition = win32more.Storage.FileServerResourceManager.IFsrmStorageModuleDefinition_head
    IFsrmStorageModuleDefinition.get_Capabilities = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileServerResourceManager.FsrmStorageModuleCaps))(31, 'get_Capabilities', ((1, 'capabilities'),)))
    IFsrmStorageModuleDefinition.put_Capabilities = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.FsrmStorageModuleCaps)(32, 'put_Capabilities', ((1, 'capabilities'),)))
    IFsrmStorageModuleDefinition.get_StorageType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileServerResourceManager.FsrmStorageModuleType))(33, 'get_StorageType', ((1, 'storageType'),)))
    IFsrmStorageModuleDefinition.put_StorageType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.FsrmStorageModuleType)(34, 'put_StorageType', ((1, 'storageType'),)))
    IFsrmStorageModuleDefinition.get_UpdatesFileContent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(35, 'get_UpdatesFileContent', ((1, 'updatesFileContent'),)))
    IFsrmStorageModuleDefinition.put_UpdatesFileContent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(36, 'put_UpdatesFileContent', ((1, 'updatesFileContent'),)))
    win32more.Storage.FileServerResourceManager.IFsrmPipelineModuleDefinition
    return IFsrmStorageModuleDefinition
def _define_IFsrmStorageModuleImplementation_head():
    class IFsrmStorageModuleImplementation(win32more.Storage.FileServerResourceManager.IFsrmPipelineModuleImplementation_head):
        Guid = Guid('0af4a0da-895a-4e50-87-12-a9-67-24-bc-ec-64')
    return IFsrmStorageModuleImplementation
def _define_IFsrmStorageModuleImplementation():
    IFsrmStorageModuleImplementation = win32more.Storage.FileServerResourceManager.IFsrmStorageModuleImplementation_head
    IFsrmStorageModuleImplementation.UseDefinitions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.IFsrmCollection_head)(9, 'UseDefinitions', ((1, 'propertyDefinitions'),)))
    IFsrmStorageModuleImplementation.LoadProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.IFsrmPropertyBag_head)(10, 'LoadProperties', ((1, 'propertyBag'),)))
    IFsrmStorageModuleImplementation.SaveProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileServerResourceManager.IFsrmPropertyBag_head)(11, 'SaveProperties', ((1, 'propertyBag'),)))
    win32more.Storage.FileServerResourceManager.IFsrmPipelineModuleImplementation
    return IFsrmStorageModuleImplementation
__all__ = [
    "AdSyncTask",
    "AdrClientDisplayFlags",
    "AdrClientDisplayFlags_AllowEmailRequests",
    "AdrClientDisplayFlags_ShowDeviceTroubleshooting",
    "AdrClientErrorType",
    "AdrClientErrorType_AccessDenied",
    "AdrClientErrorType_FileNotFound",
    "AdrClientErrorType_Unknown",
    "AdrClientFlags",
    "AdrClientFlags_FailForLocalPaths",
    "AdrClientFlags_FailIfNotDomainJoined",
    "AdrClientFlags_FailIfNotSupportedByServer",
    "AdrClientFlags_None",
    "AdrEmailFlags",
    "AdrEmailFlags_GenerateEventLog",
    "AdrEmailFlags_IncludeDeviceClaims",
    "AdrEmailFlags_IncludeUserInfo",
    "AdrEmailFlags_PutAdminOnToLine",
    "AdrEmailFlags_PutDataOwnerOnToLine",
    "DIFsrmClassificationEvents",
    "FSRM_DISPID_FEATURE_CLASSIFICATION",
    "FSRM_DISPID_FEATURE_FILESCREEN",
    "FSRM_DISPID_FEATURE_GENERAL",
    "FSRM_DISPID_FEATURE_MASK",
    "FSRM_DISPID_FEATURE_PIPELINE",
    "FSRM_DISPID_FEATURE_QUOTA",
    "FSRM_DISPID_FEATURE_REPORTS",
    "FSRM_DISPID_INTERFACE_A_MASK",
    "FSRM_DISPID_INTERFACE_B_MASK",
    "FSRM_DISPID_INTERFACE_C_MASK",
    "FSRM_DISPID_INTERFACE_D_MASK",
    "FSRM_DISPID_IS_PROPERTY",
    "FSRM_DISPID_METHOD_NUM_MASK",
    "FSRM_E_ADR_MAX_EMAILS_SENT",
    "FSRM_E_ADR_NOT_DOMAIN_JOINED",
    "FSRM_E_ADR_PATH_IS_LOCAL",
    "FSRM_E_ADR_SRV_NOT_SUPPORTED",
    "FSRM_E_ALREADY_EXISTS",
    "FSRM_E_AUTO_QUOTA",
    "FSRM_E_CACHE_INVALID",
    "FSRM_E_CACHE_MODULE_ALREADY_EXISTS",
    "FSRM_E_CANNOT_AGGREGATE",
    "FSRM_E_CANNOT_ALLOW_REPARSE_POINT_TAG",
    "FSRM_E_CANNOT_CHANGE_PROPERTY_TYPE",
    "FSRM_E_CANNOT_CREATE_TEMP_COPY",
    "FSRM_E_CANNOT_DELETE_SYSTEM_PROPERTY",
    "FSRM_E_CANNOT_REMOVE_READONLY",
    "FSRM_E_CANNOT_RENAME_PROPERTY",
    "FSRM_E_CANNOT_STORE_PROPERTIES",
    "FSRM_E_CANNOT_USE_DELETED_PROPERTY",
    "FSRM_E_CANNOT_USE_DEPRECATED_PROPERTY",
    "FSRM_E_CLASSIFICATION_ALREADY_RUNNING",
    "FSRM_E_CLASSIFICATION_CANCELED",
    "FSRM_E_CLASSIFICATION_NOT_RUNNING",
    "FSRM_E_CLASSIFICATION_PARTIAL_BATCH",
    "FSRM_E_CLASSIFICATION_SCAN_FAIL",
    "FSRM_E_CLASSIFICATION_TIMEOUT",
    "FSRM_E_CLUSTER_NOT_RUNNING",
    "FSRM_E_CSC_PATH_NOT_SUPPORTED",
    "FSRM_E_DIFFERENT_CLUSTER_GROUP",
    "FSRM_E_DRIVER_NOT_READY",
    "FSRM_E_DUPLICATE_NAME",
    "FSRM_E_EMAIL_NOT_SENT",
    "FSRM_E_ENUM_PROPERTIES_FAILED",
    "FSRM_E_ERROR_NOT_ENABLED",
    "FSRM_E_EXPIRATION_PATH_NOT_WRITEABLE",
    "FSRM_E_EXPIRATION_PATH_TOO_LONG",
    "FSRM_E_EXPIRATION_VOLUME_NOT_NTFS",
    "FSRM_E_FAIL_BATCH",
    "FSRM_E_FILE_ENCRYPTED",
    "FSRM_E_FILE_IN_USE",
    "FSRM_E_FILE_MANAGEMENT_ACTION_GET_EXITCODE_FAILED",
    "FSRM_E_FILE_MANAGEMENT_ACTION_TIMEOUT",
    "FSRM_E_FILE_MANAGEMENT_EXPIRATION_DIR_IN_SCOPE",
    "FSRM_E_FILE_MANAGEMENT_JOB_ALREADY_EXISTS",
    "FSRM_E_FILE_MANAGEMENT_JOB_ALREADY_RUNNING",
    "FSRM_E_FILE_MANAGEMENT_JOB_CUSTOM",
    "FSRM_E_FILE_MANAGEMENT_JOB_DEPRECATED",
    "FSRM_E_FILE_MANAGEMENT_JOB_EXPIRATION",
    "FSRM_E_FILE_MANAGEMENT_JOB_INVALID_CONTINUOUS_CONFIG",
    "FSRM_E_FILE_MANAGEMENT_JOB_MAX_FILE_CONDITIONS",
    "FSRM_E_FILE_MANAGEMENT_JOB_NOTIFICATION",
    "FSRM_E_FILE_MANAGEMENT_JOB_NOT_LEGACY_ACCESSIBLE",
    "FSRM_E_FILE_MANAGEMENT_JOB_RMS",
    "FSRM_E_FILE_OPEN_ERROR",
    "FSRM_E_FILE_SYSTEM_CORRUPT",
    "FSRM_E_INCOMPATIBLE_FORMAT",
    "FSRM_E_INPROC_MODULE_BLOCKED",
    "FSRM_E_INSECURE_PATH",
    "FSRM_E_INSUFFICIENT_DISK",
    "FSRM_E_INVALID_AD_CLAIM",
    "FSRM_E_INVALID_COMBINATION",
    "FSRM_E_INVALID_DATASCREEN_DEFINITION",
    "FSRM_E_INVALID_EMAIL_ADDRESS",
    "FSRM_E_INVALID_FILEGROUP_DEFINITION",
    "FSRM_E_INVALID_FILENAME",
    "FSRM_E_INVALID_FOLDER_PROPERTY_STORE",
    "FSRM_E_INVALID_IMPORT_VERSION",
    "FSRM_E_INVALID_LIMIT",
    "FSRM_E_INVALID_NAME",
    "FSRM_E_INVALID_PATH",
    "FSRM_E_INVALID_REPORT_DESC",
    "FSRM_E_INVALID_REPORT_FORMAT",
    "FSRM_E_INVALID_SCHEDULER_ARGUMENT",
    "FSRM_E_INVALID_SMTP_SERVER",
    "FSRM_E_INVALID_TEXT",
    "FSRM_E_INVALID_USER",
    "FSRM_E_LAST_ACCESS_UPDATE_DISABLED",
    "FSRM_E_LEGACY_SCHEDULE",
    "FSRM_E_LOADING_DISABLED_MODULE",
    "FSRM_E_LONG_CMDLINE",
    "FSRM_E_MAX_PROPERTY_DEFINITIONS",
    "FSRM_E_MESSAGE_LIMIT_EXCEEDED",
    "FSRM_E_MODULE_INITIALIZATION",
    "FSRM_E_MODULE_INVALID_PARAM",
    "FSRM_E_MODULE_SESSION_INITIALIZATION",
    "FSRM_E_MODULE_TIMEOUT",
    "FSRM_E_NOT_CLUSTER_VOLUME",
    "FSRM_E_NOT_FOUND",
    "FSRM_E_NOT_SUPPORTED",
    "FSRM_E_NO_EMAIL_ADDRESS",
    "FSRM_E_NO_PROPERTY_VALUE",
    "FSRM_E_OBJECT_IN_USE",
    "FSRM_E_OUT_OF_RANGE",
    "FSRM_E_PARTIAL_CLASSIFICATION_PROPERTY_NOT_FOUND",
    "FSRM_E_PATH_NOT_FOUND",
    "FSRM_E_PATH_NOT_IN_NAMESPACE",
    "FSRM_E_PERSIST_PROPERTIES_FAILED",
    "FSRM_E_PERSIST_PROPERTIES_FAILED_ENCRYPTED",
    "FSRM_E_PROPERTY_DELETED",
    "FSRM_E_PROPERTY_MUST_APPLY_TO_FILES",
    "FSRM_E_PROPERTY_MUST_APPLY_TO_FOLDERS",
    "FSRM_E_PROPERTY_MUST_BE_GLOBAL",
    "FSRM_E_PROPERTY_MUST_BE_SECURE",
    "FSRM_E_REBUILDING_FODLER_TYPE_INDEX",
    "FSRM_E_REPORT_GENERATION_ERR",
    "FSRM_E_REPORT_JOB_ALREADY_RUNNING",
    "FSRM_E_REPORT_TASK_TRIGGER",
    "FSRM_E_REPORT_TYPE_ALREADY_EXISTS",
    "FSRM_E_REQD_PARAM_MISSING",
    "FSRM_E_RMS_NO_PROTECTORS_INSTALLED",
    "FSRM_E_RMS_NO_PROTECTOR_INSTALLED_FOR_FILE",
    "FSRM_E_RMS_TEMPLATE_NOT_FOUND",
    "FSRM_E_SECURE_PROPERTIES_NOT_SUPPORTED",
    "FSRM_E_SET_PROPERTY_FAILED",
    "FSRM_E_SHADOW_COPY",
    "FSRM_E_STORE_NOT_INSTALLED",
    "FSRM_E_SYNC_TASK_HAD_ERRORS",
    "FSRM_E_SYNC_TASK_TIMEOUT",
    "FSRM_E_TEXTREADER_FILENAME_TOO_LONG",
    "FSRM_E_TEXTREADER_IFILTER_CLSID_MALFORMED",
    "FSRM_E_TEXTREADER_IFILTER_NOT_FOUND",
    "FSRM_E_TEXTREADER_NOT_INITIALIZED",
    "FSRM_E_TEXTREADER_STREAM_ERROR",
    "FSRM_E_UNEXPECTED",
    "FSRM_E_UNSECURE_LINK_TO_HOSTED_MODULE",
    "FSRM_E_VOLUME_OFFLINE",
    "FSRM_E_VOLUME_UNSUPPORTED",
    "FSRM_E_WMI_FAILURE",
    "FSRM_E_XML_CORRUPTED",
    "FSRM_S_CLASSIFICATION_SCAN_FAILURES",
    "FSRM_S_PARTIAL_BATCH",
    "FSRM_S_PARTIAL_CLASSIFICATION",
    "FsrmAccessDeniedRemediationClient",
    "FsrmAccountType",
    "FsrmAccountType_Automatic",
    "FsrmAccountType_External",
    "FsrmAccountType_InProc",
    "FsrmAccountType_LocalService",
    "FsrmAccountType_LocalSystem",
    "FsrmAccountType_NetworkService",
    "FsrmAccountType_Unknown",
    "FsrmActionType",
    "FsrmActionType_Command",
    "FsrmActionType_Email",
    "FsrmActionType_EventLog",
    "FsrmActionType_Report",
    "FsrmActionType_Unknown",
    "FsrmClassificationLoggingFlags",
    "FsrmClassificationLoggingFlags_ClassificationsInLogFile",
    "FsrmClassificationLoggingFlags_ClassificationsInSystemLog",
    "FsrmClassificationLoggingFlags_ErrorsInLogFile",
    "FsrmClassificationLoggingFlags_ErrorsInSystemLog",
    "FsrmClassificationLoggingFlags_None",
    "FsrmClassificationManager",
    "FsrmCollectionState",
    "FsrmCollectionState_Cancelled",
    "FsrmCollectionState_Committing",
    "FsrmCollectionState_Complete",
    "FsrmCollectionState_Fetching",
    "FsrmCommitOptions",
    "FsrmCommitOptions_Asynchronous",
    "FsrmCommitOptions_None",
    "FsrmDaysNotSpecified",
    "FsrmEnumOptions",
    "FsrmEnumOptions_Asynchronous",
    "FsrmEnumOptions_CheckRecycleBin",
    "FsrmEnumOptions_IncludeClusterNodes",
    "FsrmEnumOptions_IncludeDeprecatedObjects",
    "FsrmEnumOptions_None",
    "FsrmEventType",
    "FsrmEventType_Error",
    "FsrmEventType_Information",
    "FsrmEventType_Unknown",
    "FsrmEventType_Warning",
    "FsrmExecutionOption",
    "FsrmExecutionOption_EvaluateUnset",
    "FsrmExecutionOption_ReEvaluate_ConsiderExistingValue",
    "FsrmExecutionOption_ReEvaluate_IgnoreExistingValue",
    "FsrmExecutionOption_Unknown",
    "FsrmExportImport",
    "FsrmFileConditionType",
    "FsrmFileConditionType_Property",
    "FsrmFileConditionType_Unknown",
    "FsrmFileGroupManager",
    "FsrmFileManagementJobManager",
    "FsrmFileManagementLoggingFlags",
    "FsrmFileManagementLoggingFlags_Audit",
    "FsrmFileManagementLoggingFlags_Error",
    "FsrmFileManagementLoggingFlags_Information",
    "FsrmFileManagementLoggingFlags_None",
    "FsrmFileManagementType",
    "FsrmFileManagementType_Custom",
    "FsrmFileManagementType_Expiration",
    "FsrmFileManagementType_Rms",
    "FsrmFileManagementType_Unknown",
    "FsrmFileScreenFlags",
    "FsrmFileScreenFlags_Enforce",
    "FsrmFileScreenManager",
    "FsrmFileScreenTemplateManager",
    "FsrmFileStreamingInterfaceType",
    "FsrmFileStreamingInterfaceType_ILockBytes",
    "FsrmFileStreamingInterfaceType_IStream",
    "FsrmFileStreamingInterfaceType_Unknown",
    "FsrmFileStreamingMode",
    "FsrmFileStreamingMode_Read",
    "FsrmFileStreamingMode_Unknown",
    "FsrmFileStreamingMode_Write",
    "FsrmFileSystemPropertyId",
    "FsrmFileSystemPropertyId_DateCreated",
    "FsrmFileSystemPropertyId_DateLastAccessed",
    "FsrmFileSystemPropertyId_DateLastModified",
    "FsrmFileSystemPropertyId_DateNow",
    "FsrmFileSystemPropertyId_FileName",
    "FsrmFileSystemPropertyId_Undefined",
    "FsrmGetFilePropertyOptions",
    "FsrmGetFilePropertyOptions_FailOnPersistErrors",
    "FsrmGetFilePropertyOptions_NoRuleEvaluation",
    "FsrmGetFilePropertyOptions_None",
    "FsrmGetFilePropertyOptions_Persistent",
    "FsrmGetFilePropertyOptions_SkipOrphaned",
    "FsrmMaxExcludeFolders",
    "FsrmMaxNumberPropertyDefinitions",
    "FsrmMaxNumberThresholds",
    "FsrmMaxThresholdValue",
    "FsrmMinQuotaLimit",
    "FsrmMinThresholdValue",
    "FsrmPathMapper",
    "FsrmPipelineModuleConnector",
    "FsrmPipelineModuleType",
    "FsrmPipelineModuleType_Classifier",
    "FsrmPipelineModuleType_Storage",
    "FsrmPipelineModuleType_Unknown",
    "FsrmPropertyBagField",
    "FsrmPropertyBagField_AccessVolume",
    "FsrmPropertyBagField_VolumeGuidName",
    "FsrmPropertyBagFlags",
    "FsrmPropertyBagFlags_FailedClassifyingProperties",
    "FsrmPropertyBagFlags_FailedLoadingProperties",
    "FsrmPropertyBagFlags_FailedSavingProperties",
    "FsrmPropertyBagFlags_UpdatedByClassifier",
    "FsrmPropertyConditionType",
    "FsrmPropertyConditionType_Contain",
    "FsrmPropertyConditionType_ContainedIn",
    "FsrmPropertyConditionType_EndWith",
    "FsrmPropertyConditionType_Equal",
    "FsrmPropertyConditionType_Exist",
    "FsrmPropertyConditionType_GreaterThan",
    "FsrmPropertyConditionType_LessThan",
    "FsrmPropertyConditionType_MatchesPattern",
    "FsrmPropertyConditionType_NotEqual",
    "FsrmPropertyConditionType_NotExist",
    "FsrmPropertyConditionType_PrefixOf",
    "FsrmPropertyConditionType_StartWith",
    "FsrmPropertyConditionType_SuffixOf",
    "FsrmPropertyConditionType_Unknown",
    "FsrmPropertyDefinitionAppliesTo",
    "FsrmPropertyDefinitionAppliesTo_Files",
    "FsrmPropertyDefinitionAppliesTo_Folders",
    "FsrmPropertyDefinitionFlags",
    "FsrmPropertyDefinitionFlags_Deprecated",
    "FsrmPropertyDefinitionFlags_Global",
    "FsrmPropertyDefinitionFlags_Secure",
    "FsrmPropertyDefinitionType",
    "FsrmPropertyDefinitionType_Bool",
    "FsrmPropertyDefinitionType_Date",
    "FsrmPropertyDefinitionType_Int",
    "FsrmPropertyDefinitionType_MultiChoiceList",
    "FsrmPropertyDefinitionType_MultiString",
    "FsrmPropertyDefinitionType_OrderedList",
    "FsrmPropertyDefinitionType_SingleChoiceList",
    "FsrmPropertyDefinitionType_String",
    "FsrmPropertyDefinitionType_Unknown",
    "FsrmPropertyFlags",
    "FsrmPropertyFlags_AggregationFailed",
    "FsrmPropertyFlags_Deleted",
    "FsrmPropertyFlags_Existing",
    "FsrmPropertyFlags_ExplicitValueDeleted",
    "FsrmPropertyFlags_FailedClassifyingProperties",
    "FsrmPropertyFlags_FailedLoadingProperties",
    "FsrmPropertyFlags_FailedSavingProperties",
    "FsrmPropertyFlags_Inherited",
    "FsrmPropertyFlags_Manual",
    "FsrmPropertyFlags_None",
    "FsrmPropertyFlags_Orphaned",
    "FsrmPropertyFlags_PersistentMask",
    "FsrmPropertyFlags_PolicyDerived",
    "FsrmPropertyFlags_PropertyDeletedFromClear",
    "FsrmPropertyFlags_PropertySourceMask",
    "FsrmPropertyFlags_Reclassified",
    "FsrmPropertyFlags_RetrievedFromCache",
    "FsrmPropertyFlags_RetrievedFromStorage",
    "FsrmPropertyFlags_Secure",
    "FsrmPropertyFlags_SetByClassifier",
    "FsrmPropertyValueType",
    "FsrmPropertyValueType_DateOffset",
    "FsrmPropertyValueType_Literal",
    "FsrmPropertyValueType_Undefined",
    "FsrmQuotaFlags",
    "FsrmQuotaFlags_Disable",
    "FsrmQuotaFlags_Enforce",
    "FsrmQuotaFlags_StatusIncomplete",
    "FsrmQuotaFlags_StatusRebuilding",
    "FsrmQuotaManager",
    "FsrmQuotaTemplateManager",
    "FsrmReportFilter",
    "FsrmReportFilter_FileGroups",
    "FsrmReportFilter_MaxAgeDays",
    "FsrmReportFilter_MinAgeDays",
    "FsrmReportFilter_MinQuotaUsage",
    "FsrmReportFilter_MinSize",
    "FsrmReportFilter_NamePattern",
    "FsrmReportFilter_Owners",
    "FsrmReportFilter_Property",
    "FsrmReportFormat",
    "FsrmReportFormat_Csv",
    "FsrmReportFormat_DHtml",
    "FsrmReportFormat_Html",
    "FsrmReportFormat_Txt",
    "FsrmReportFormat_Unknown",
    "FsrmReportFormat_Xml",
    "FsrmReportGenerationContext",
    "FsrmReportGenerationContext_IncidentReport",
    "FsrmReportGenerationContext_InteractiveReport",
    "FsrmReportGenerationContext_ScheduledReport",
    "FsrmReportGenerationContext_Undefined",
    "FsrmReportLimit",
    "FsrmReportLimit_MaxDuplicateGroups",
    "FsrmReportLimit_MaxFileGroups",
    "FsrmReportLimit_MaxFileScreenEvents",
    "FsrmReportLimit_MaxFiles",
    "FsrmReportLimit_MaxFilesPerDuplGroup",
    "FsrmReportLimit_MaxFilesPerFileGroup",
    "FsrmReportLimit_MaxFilesPerOwner",
    "FsrmReportLimit_MaxFilesPerPropertyValue",
    "FsrmReportLimit_MaxFolders",
    "FsrmReportLimit_MaxOwners",
    "FsrmReportLimit_MaxPropertyValues",
    "FsrmReportLimit_MaxQuotas",
    "FsrmReportManager",
    "FsrmReportRunningStatus",
    "FsrmReportRunningStatus_NotRunning",
    "FsrmReportRunningStatus_Queued",
    "FsrmReportRunningStatus_Running",
    "FsrmReportRunningStatus_Unknown",
    "FsrmReportScheduler",
    "FsrmReportType",
    "FsrmReportType_AutomaticClassification",
    "FsrmReportType_DuplicateFiles",
    "FsrmReportType_Expiration",
    "FsrmReportType_ExportReport",
    "FsrmReportType_FileScreenAudit",
    "FsrmReportType_FilesByOwner",
    "FsrmReportType_FilesByProperty",
    "FsrmReportType_FilesByType",
    "FsrmReportType_FoldersByProperty",
    "FsrmReportType_LargeFiles",
    "FsrmReportType_LeastRecentlyAccessed",
    "FsrmReportType_MostRecentlyAccessed",
    "FsrmReportType_QuotaUsage",
    "FsrmReportType_Unknown",
    "FsrmRuleFlags",
    "FsrmRuleFlags_ClearAutomaticallyClassifiedProperty",
    "FsrmRuleFlags_ClearManuallyClassifiedProperty",
    "FsrmRuleFlags_Disabled",
    "FsrmRuleFlags_Invalid",
    "FsrmRuleType",
    "FsrmRuleType_Classification",
    "FsrmRuleType_Generic",
    "FsrmRuleType_Unknown",
    "FsrmSetting",
    "FsrmStorageModuleCaps",
    "FsrmStorageModuleCaps_CanGet",
    "FsrmStorageModuleCaps_CanHandleDirectories",
    "FsrmStorageModuleCaps_CanHandleFiles",
    "FsrmStorageModuleCaps_CanSet",
    "FsrmStorageModuleCaps_Unknown",
    "FsrmStorageModuleType",
    "FsrmStorageModuleType_Cache",
    "FsrmStorageModuleType_Database",
    "FsrmStorageModuleType_InFile",
    "FsrmStorageModuleType_System",
    "FsrmStorageModuleType_Unknown",
    "FsrmTemplateApplyOptions",
    "FsrmTemplateApplyOptions_ApplyToDerivedAll",
    "FsrmTemplateApplyOptions_ApplyToDerivedMatching",
    "IFsrmAccessDeniedRemediationClient",
    "IFsrmAction",
    "IFsrmActionCommand",
    "IFsrmActionEmail",
    "IFsrmActionEmail2",
    "IFsrmActionEventLog",
    "IFsrmActionReport",
    "IFsrmAutoApplyQuota",
    "IFsrmClassificationManager",
    "IFsrmClassificationManager2",
    "IFsrmClassificationRule",
    "IFsrmClassifierModuleDefinition",
    "IFsrmClassifierModuleImplementation",
    "IFsrmCollection",
    "IFsrmCommittableCollection",
    "IFsrmDerivedObjectsResult",
    "IFsrmExportImport",
    "IFsrmFileCondition",
    "IFsrmFileConditionProperty",
    "IFsrmFileGroup",
    "IFsrmFileGroupImported",
    "IFsrmFileGroupManager",
    "IFsrmFileManagementJob",
    "IFsrmFileManagementJobManager",
    "IFsrmFileScreen",
    "IFsrmFileScreenBase",
    "IFsrmFileScreenException",
    "IFsrmFileScreenManager",
    "IFsrmFileScreenTemplate",
    "IFsrmFileScreenTemplateImported",
    "IFsrmFileScreenTemplateManager",
    "IFsrmMutableCollection",
    "IFsrmObject",
    "IFsrmPathMapper",
    "IFsrmPipelineModuleConnector",
    "IFsrmPipelineModuleDefinition",
    "IFsrmPipelineModuleImplementation",
    "IFsrmProperty",
    "IFsrmPropertyBag",
    "IFsrmPropertyBag2",
    "IFsrmPropertyCondition",
    "IFsrmPropertyDefinition",
    "IFsrmPropertyDefinition2",
    "IFsrmPropertyDefinitionValue",
    "IFsrmQuota",
    "IFsrmQuotaBase",
    "IFsrmQuotaManager",
    "IFsrmQuotaManagerEx",
    "IFsrmQuotaObject",
    "IFsrmQuotaTemplate",
    "IFsrmQuotaTemplateImported",
    "IFsrmQuotaTemplateManager",
    "IFsrmReport",
    "IFsrmReportJob",
    "IFsrmReportManager",
    "IFsrmReportScheduler",
    "IFsrmRule",
    "IFsrmSetting",
    "IFsrmStorageModuleDefinition",
    "IFsrmStorageModuleImplementation",
    "MessageSizeLimit",
]
