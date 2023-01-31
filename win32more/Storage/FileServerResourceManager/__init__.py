from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Storage.FileServerResourceManager
import win32more.System.Com
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
AdSyncTask = Guid('2ae64751-b728-4d6b-97-a0-b2-da-2e-7d-2a-3b')
AdrClientDisplayFlags = Int32
AdrClientDisplayFlags_AllowEmailRequests: AdrClientDisplayFlags = 1
AdrClientDisplayFlags_ShowDeviceTroubleshooting: AdrClientDisplayFlags = 2
AdrClientErrorType = Int32
AdrClientErrorType_Unknown: AdrClientErrorType = 0
AdrClientErrorType_AccessDenied: AdrClientErrorType = 1
AdrClientErrorType_FileNotFound: AdrClientErrorType = 2
AdrClientFlags = Int32
AdrClientFlags_None: AdrClientFlags = 0
AdrClientFlags_FailForLocalPaths: AdrClientFlags = 1
AdrClientFlags_FailIfNotSupportedByServer: AdrClientFlags = 2
AdrClientFlags_FailIfNotDomainJoined: AdrClientFlags = 4
AdrEmailFlags = Int32
AdrEmailFlags_PutDataOwnerOnToLine: AdrEmailFlags = 1
AdrEmailFlags_PutAdminOnToLine: AdrEmailFlags = 2
AdrEmailFlags_IncludeDeviceClaims: AdrEmailFlags = 4
AdrEmailFlags_IncludeUserInfo: AdrEmailFlags = 8
AdrEmailFlags_GenerateEventLog: AdrEmailFlags = 16
FSRM_DISPID_FEATURE_MASK: UInt32 = 251658240
FSRM_DISPID_INTERFACE_A_MASK: UInt32 = 15728640
FSRM_DISPID_INTERFACE_B_MASK: UInt32 = 983040
FSRM_DISPID_INTERFACE_C_MASK: UInt32 = 61440
FSRM_DISPID_INTERFACE_D_MASK: UInt32 = 3840
FSRM_DISPID_IS_PROPERTY: UInt32 = 128
FSRM_DISPID_METHOD_NUM_MASK: UInt32 = 127
FSRM_DISPID_FEATURE_GENERAL: UInt32 = 16777216
FSRM_DISPID_FEATURE_QUOTA: UInt32 = 33554432
FSRM_DISPID_FEATURE_FILESCREEN: UInt32 = 50331648
FSRM_DISPID_FEATURE_REPORTS: UInt32 = 67108864
FSRM_DISPID_FEATURE_CLASSIFICATION: UInt32 = 83886080
FSRM_DISPID_FEATURE_PIPELINE: UInt32 = 100663296
FsrmMaxNumberThresholds: UInt32 = 16
FsrmMinThresholdValue: UInt32 = 1
FsrmMaxThresholdValue: UInt32 = 250
FsrmMinQuotaLimit: UInt32 = 1024
FsrmMaxExcludeFolders: UInt32 = 32
FsrmMaxNumberPropertyDefinitions: UInt32 = 100
MessageSizeLimit: UInt32 = 4096
FsrmDaysNotSpecified: Int32 = -1
FSRM_S_PARTIAL_BATCH: win32more.Foundation.HRESULT = 283396
FSRM_S_PARTIAL_CLASSIFICATION: win32more.Foundation.HRESULT = 283397
FSRM_S_CLASSIFICATION_SCAN_FAILURES: win32more.Foundation.HRESULT = 283398
FSRM_E_NOT_FOUND: win32more.Foundation.HRESULT = -2147200255
FSRM_E_INVALID_SCHEDULER_ARGUMENT: win32more.Foundation.HRESULT = -2147200254
FSRM_E_ALREADY_EXISTS: win32more.Foundation.HRESULT = -2147200253
FSRM_E_PATH_NOT_FOUND: win32more.Foundation.HRESULT = -2147200252
FSRM_E_INVALID_USER: win32more.Foundation.HRESULT = -2147200251
FSRM_E_INVALID_PATH: win32more.Foundation.HRESULT = -2147200250
FSRM_E_INVALID_LIMIT: win32more.Foundation.HRESULT = -2147200249
FSRM_E_INVALID_NAME: win32more.Foundation.HRESULT = -2147200248
FSRM_E_FAIL_BATCH: win32more.Foundation.HRESULT = -2147200247
FSRM_E_INVALID_TEXT: win32more.Foundation.HRESULT = -2147200246
FSRM_E_INVALID_IMPORT_VERSION: win32more.Foundation.HRESULT = -2147200245
FSRM_E_OUT_OF_RANGE: win32more.Foundation.HRESULT = -2147200243
FSRM_E_REQD_PARAM_MISSING: win32more.Foundation.HRESULT = -2147200242
FSRM_E_INVALID_COMBINATION: win32more.Foundation.HRESULT = -2147200241
FSRM_E_DUPLICATE_NAME: win32more.Foundation.HRESULT = -2147200240
FSRM_E_NOT_SUPPORTED: win32more.Foundation.HRESULT = -2147200239
FSRM_E_DRIVER_NOT_READY: win32more.Foundation.HRESULT = -2147200237
FSRM_E_INSUFFICIENT_DISK: win32more.Foundation.HRESULT = -2147200236
FSRM_E_VOLUME_UNSUPPORTED: win32more.Foundation.HRESULT = -2147200235
FSRM_E_UNEXPECTED: win32more.Foundation.HRESULT = -2147200234
FSRM_E_INSECURE_PATH: win32more.Foundation.HRESULT = -2147200233
FSRM_E_INVALID_SMTP_SERVER: win32more.Foundation.HRESULT = -2147200232
FSRM_E_AUTO_QUOTA: win32more.Foundation.HRESULT = 283419
FSRM_E_EMAIL_NOT_SENT: win32more.Foundation.HRESULT = -2147200228
FSRM_E_INVALID_EMAIL_ADDRESS: win32more.Foundation.HRESULT = -2147200226
FSRM_E_FILE_SYSTEM_CORRUPT: win32more.Foundation.HRESULT = -2147200225
FSRM_E_LONG_CMDLINE: win32more.Foundation.HRESULT = -2147200224
FSRM_E_INVALID_FILEGROUP_DEFINITION: win32more.Foundation.HRESULT = -2147200223
FSRM_E_INVALID_DATASCREEN_DEFINITION: win32more.Foundation.HRESULT = -2147200220
FSRM_E_INVALID_REPORT_FORMAT: win32more.Foundation.HRESULT = -2147200216
FSRM_E_INVALID_REPORT_DESC: win32more.Foundation.HRESULT = -2147200215
FSRM_E_INVALID_FILENAME: win32more.Foundation.HRESULT = -2147200214
FSRM_E_SHADOW_COPY: win32more.Foundation.HRESULT = -2147200212
FSRM_E_XML_CORRUPTED: win32more.Foundation.HRESULT = -2147200211
FSRM_E_CLUSTER_NOT_RUNNING: win32more.Foundation.HRESULT = -2147200210
FSRM_E_STORE_NOT_INSTALLED: win32more.Foundation.HRESULT = -2147200209
FSRM_E_NOT_CLUSTER_VOLUME: win32more.Foundation.HRESULT = -2147200208
FSRM_E_DIFFERENT_CLUSTER_GROUP: win32more.Foundation.HRESULT = -2147200207
FSRM_E_REPORT_TYPE_ALREADY_EXISTS: win32more.Foundation.HRESULT = -2147200206
FSRM_E_REPORT_JOB_ALREADY_RUNNING: win32more.Foundation.HRESULT = -2147200205
FSRM_E_REPORT_GENERATION_ERR: win32more.Foundation.HRESULT = -2147200204
FSRM_E_REPORT_TASK_TRIGGER: win32more.Foundation.HRESULT = -2147200203
FSRM_E_LOADING_DISABLED_MODULE: win32more.Foundation.HRESULT = -2147200202
FSRM_E_CANNOT_AGGREGATE: win32more.Foundation.HRESULT = -2147200201
FSRM_E_MESSAGE_LIMIT_EXCEEDED: win32more.Foundation.HRESULT = -2147200200
FSRM_E_OBJECT_IN_USE: win32more.Foundation.HRESULT = -2147200199
FSRM_E_CANNOT_RENAME_PROPERTY: win32more.Foundation.HRESULT = -2147200198
FSRM_E_CANNOT_CHANGE_PROPERTY_TYPE: win32more.Foundation.HRESULT = -2147200197
FSRM_E_MAX_PROPERTY_DEFINITIONS: win32more.Foundation.HRESULT = -2147200196
FSRM_E_CLASSIFICATION_ALREADY_RUNNING: win32more.Foundation.HRESULT = -2147200195
FSRM_E_CLASSIFICATION_NOT_RUNNING: win32more.Foundation.HRESULT = -2147200194
FSRM_E_FILE_MANAGEMENT_JOB_ALREADY_RUNNING: win32more.Foundation.HRESULT = -2147200193
FSRM_E_FILE_MANAGEMENT_JOB_EXPIRATION: win32more.Foundation.HRESULT = -2147200192
FSRM_E_FILE_MANAGEMENT_JOB_CUSTOM: win32more.Foundation.HRESULT = -2147200191
FSRM_E_FILE_MANAGEMENT_JOB_NOTIFICATION: win32more.Foundation.HRESULT = -2147200190
FSRM_E_FILE_OPEN_ERROR: win32more.Foundation.HRESULT = -2147200189
FSRM_E_UNSECURE_LINK_TO_HOSTED_MODULE: win32more.Foundation.HRESULT = -2147200188
FSRM_E_CACHE_INVALID: win32more.Foundation.HRESULT = -2147200187
FSRM_E_CACHE_MODULE_ALREADY_EXISTS: win32more.Foundation.HRESULT = -2147200186
FSRM_E_FILE_MANAGEMENT_EXPIRATION_DIR_IN_SCOPE: win32more.Foundation.HRESULT = -2147200185
FSRM_E_FILE_MANAGEMENT_JOB_ALREADY_EXISTS: win32more.Foundation.HRESULT = -2147200184
FSRM_E_PROPERTY_DELETED: win32more.Foundation.HRESULT = -2147200183
FSRM_E_LAST_ACCESS_UPDATE_DISABLED: win32more.Foundation.HRESULT = -2147200176
FSRM_E_NO_PROPERTY_VALUE: win32more.Foundation.HRESULT = -2147200175
FSRM_E_INPROC_MODULE_BLOCKED: win32more.Foundation.HRESULT = -2147200174
FSRM_E_ENUM_PROPERTIES_FAILED: win32more.Foundation.HRESULT = -2147200173
FSRM_E_SET_PROPERTY_FAILED: win32more.Foundation.HRESULT = -2147200172
FSRM_E_CANNOT_STORE_PROPERTIES: win32more.Foundation.HRESULT = -2147200171
FSRM_E_CANNOT_ALLOW_REPARSE_POINT_TAG: win32more.Foundation.HRESULT = -2147200170
FSRM_E_PARTIAL_CLASSIFICATION_PROPERTY_NOT_FOUND: win32more.Foundation.HRESULT = -2147200169
FSRM_E_TEXTREADER_NOT_INITIALIZED: win32more.Foundation.HRESULT = -2147200168
FSRM_E_TEXTREADER_IFILTER_NOT_FOUND: win32more.Foundation.HRESULT = -2147200167
FSRM_E_PERSIST_PROPERTIES_FAILED_ENCRYPTED: win32more.Foundation.HRESULT = -2147200166
FSRM_E_TEXTREADER_IFILTER_CLSID_MALFORMED: win32more.Foundation.HRESULT = -2147200160
FSRM_E_TEXTREADER_STREAM_ERROR: win32more.Foundation.HRESULT = -2147200159
FSRM_E_TEXTREADER_FILENAME_TOO_LONG: win32more.Foundation.HRESULT = -2147200158
FSRM_E_INCOMPATIBLE_FORMAT: win32more.Foundation.HRESULT = -2147200157
FSRM_E_FILE_ENCRYPTED: win32more.Foundation.HRESULT = -2147200156
FSRM_E_PERSIST_PROPERTIES_FAILED: win32more.Foundation.HRESULT = -2147200155
FSRM_E_VOLUME_OFFLINE: win32more.Foundation.HRESULT = -2147200154
FSRM_E_FILE_MANAGEMENT_ACTION_TIMEOUT: win32more.Foundation.HRESULT = -2147200153
FSRM_E_FILE_MANAGEMENT_ACTION_GET_EXITCODE_FAILED: win32more.Foundation.HRESULT = -2147200152
FSRM_E_MODULE_INVALID_PARAM: win32more.Foundation.HRESULT = -2147200151
FSRM_E_MODULE_INITIALIZATION: win32more.Foundation.HRESULT = -2147200150
FSRM_E_MODULE_SESSION_INITIALIZATION: win32more.Foundation.HRESULT = -2147200149
FSRM_E_CLASSIFICATION_SCAN_FAIL: win32more.Foundation.HRESULT = -2147200148
FSRM_E_FILE_MANAGEMENT_JOB_NOT_LEGACY_ACCESSIBLE: win32more.Foundation.HRESULT = -2147200147
FSRM_E_FILE_MANAGEMENT_JOB_MAX_FILE_CONDITIONS: win32more.Foundation.HRESULT = -2147200146
FSRM_E_CANNOT_USE_DEPRECATED_PROPERTY: win32more.Foundation.HRESULT = -2147200145
FSRM_E_SYNC_TASK_TIMEOUT: win32more.Foundation.HRESULT = -2147200144
FSRM_E_CANNOT_USE_DELETED_PROPERTY: win32more.Foundation.HRESULT = -2147200143
FSRM_E_INVALID_AD_CLAIM: win32more.Foundation.HRESULT = -2147200142
FSRM_E_CLASSIFICATION_CANCELED: win32more.Foundation.HRESULT = -2147200141
FSRM_E_INVALID_FOLDER_PROPERTY_STORE: win32more.Foundation.HRESULT = -2147200140
FSRM_E_REBUILDING_FODLER_TYPE_INDEX: win32more.Foundation.HRESULT = -2147200139
FSRM_E_PROPERTY_MUST_APPLY_TO_FILES: win32more.Foundation.HRESULT = -2147200138
FSRM_E_CLASSIFICATION_TIMEOUT: win32more.Foundation.HRESULT = -2147200137
FSRM_E_CLASSIFICATION_PARTIAL_BATCH: win32more.Foundation.HRESULT = -2147200136
FSRM_E_CANNOT_DELETE_SYSTEM_PROPERTY: win32more.Foundation.HRESULT = -2147200135
FSRM_E_FILE_IN_USE: win32more.Foundation.HRESULT = -2147200134
FSRM_E_ERROR_NOT_ENABLED: win32more.Foundation.HRESULT = -2147200133
FSRM_E_CANNOT_CREATE_TEMP_COPY: win32more.Foundation.HRESULT = -2147200132
FSRM_E_NO_EMAIL_ADDRESS: win32more.Foundation.HRESULT = -2147200131
FSRM_E_ADR_MAX_EMAILS_SENT: win32more.Foundation.HRESULT = -2147200130
FSRM_E_PATH_NOT_IN_NAMESPACE: win32more.Foundation.HRESULT = -2147200129
FSRM_E_RMS_TEMPLATE_NOT_FOUND: win32more.Foundation.HRESULT = -2147200128
FSRM_E_SECURE_PROPERTIES_NOT_SUPPORTED: win32more.Foundation.HRESULT = -2147200127
FSRM_E_RMS_NO_PROTECTORS_INSTALLED: win32more.Foundation.HRESULT = -2147200126
FSRM_E_RMS_NO_PROTECTOR_INSTALLED_FOR_FILE: win32more.Foundation.HRESULT = -2147200125
FSRM_E_PROPERTY_MUST_APPLY_TO_FOLDERS: win32more.Foundation.HRESULT = -2147200124
FSRM_E_PROPERTY_MUST_BE_SECURE: win32more.Foundation.HRESULT = -2147200123
FSRM_E_PROPERTY_MUST_BE_GLOBAL: win32more.Foundation.HRESULT = -2147200122
FSRM_E_WMI_FAILURE: win32more.Foundation.HRESULT = -2147200121
FSRM_E_FILE_MANAGEMENT_JOB_RMS: win32more.Foundation.HRESULT = -2147200120
FSRM_E_SYNC_TASK_HAD_ERRORS: win32more.Foundation.HRESULT = -2147200119
FSRM_E_ADR_SRV_NOT_SUPPORTED: win32more.Foundation.HRESULT = -2147200112
FSRM_E_ADR_PATH_IS_LOCAL: win32more.Foundation.HRESULT = -2147200111
FSRM_E_ADR_NOT_DOMAIN_JOINED: win32more.Foundation.HRESULT = -2147200110
FSRM_E_CANNOT_REMOVE_READONLY: win32more.Foundation.HRESULT = -2147200109
FSRM_E_FILE_MANAGEMENT_JOB_INVALID_CONTINUOUS_CONFIG: win32more.Foundation.HRESULT = -2147200108
FSRM_E_LEGACY_SCHEDULE: win32more.Foundation.HRESULT = -2147200107
FSRM_E_CSC_PATH_NOT_SUPPORTED: win32more.Foundation.HRESULT = -2147200106
FSRM_E_EXPIRATION_PATH_NOT_WRITEABLE: win32more.Foundation.HRESULT = -2147200105
FSRM_E_EXPIRATION_PATH_TOO_LONG: win32more.Foundation.HRESULT = -2147200104
FSRM_E_EXPIRATION_VOLUME_NOT_NTFS: win32more.Foundation.HRESULT = -2147200103
FSRM_E_FILE_MANAGEMENT_JOB_DEPRECATED: win32more.Foundation.HRESULT = -2147200102
FSRM_E_MODULE_TIMEOUT: win32more.Foundation.HRESULT = -2147200101
class DIFsrmClassificationEvents(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('26942db0-dabf-41d8-bb-dd-b1-29-a9-f7-04-24')
FsrmAccessDeniedRemediationClient = Guid('100b4fc8-74c1-470f-b1-b7-dd-7b-6b-ae-79-bd')
FsrmAccountType = Int32
FsrmAccountType_Unknown: FsrmAccountType = 0
FsrmAccountType_NetworkService: FsrmAccountType = 1
FsrmAccountType_LocalService: FsrmAccountType = 2
FsrmAccountType_LocalSystem: FsrmAccountType = 3
FsrmAccountType_InProc: FsrmAccountType = 4
FsrmAccountType_External: FsrmAccountType = 5
FsrmAccountType_Automatic: FsrmAccountType = 500
FsrmActionType = Int32
FsrmActionType_Unknown: FsrmActionType = 0
FsrmActionType_EventLog: FsrmActionType = 1
FsrmActionType_Email: FsrmActionType = 2
FsrmActionType_Command: FsrmActionType = 3
FsrmActionType_Report: FsrmActionType = 4
FsrmClassificationLoggingFlags = Int32
FsrmClassificationLoggingFlags_None: FsrmClassificationLoggingFlags = 0
FsrmClassificationLoggingFlags_ClassificationsInLogFile: FsrmClassificationLoggingFlags = 1
FsrmClassificationLoggingFlags_ErrorsInLogFile: FsrmClassificationLoggingFlags = 2
FsrmClassificationLoggingFlags_ClassificationsInSystemLog: FsrmClassificationLoggingFlags = 4
FsrmClassificationLoggingFlags_ErrorsInSystemLog: FsrmClassificationLoggingFlags = 8
FsrmClassificationManager = Guid('b15c0e47-c391-45b9-95-c8-eb-59-6c-85-3f-3a')
FsrmCollectionState = Int32
FsrmCollectionState_Fetching: FsrmCollectionState = 1
FsrmCollectionState_Committing: FsrmCollectionState = 2
FsrmCollectionState_Complete: FsrmCollectionState = 3
FsrmCollectionState_Cancelled: FsrmCollectionState = 4
FsrmCommitOptions = Int32
FsrmCommitOptions_None: FsrmCommitOptions = 0
FsrmCommitOptions_Asynchronous: FsrmCommitOptions = 1
FsrmEnumOptions = Int32
FsrmEnumOptions_None: FsrmEnumOptions = 0
FsrmEnumOptions_Asynchronous: FsrmEnumOptions = 1
FsrmEnumOptions_CheckRecycleBin: FsrmEnumOptions = 2
FsrmEnumOptions_IncludeClusterNodes: FsrmEnumOptions = 4
FsrmEnumOptions_IncludeDeprecatedObjects: FsrmEnumOptions = 8
FsrmEventType = Int32
FsrmEventType_Unknown: FsrmEventType = 0
FsrmEventType_Information: FsrmEventType = 1
FsrmEventType_Warning: FsrmEventType = 2
FsrmEventType_Error: FsrmEventType = 3
FsrmExecutionOption = Int32
FsrmExecutionOption_Unknown: FsrmExecutionOption = 0
FsrmExecutionOption_EvaluateUnset: FsrmExecutionOption = 1
FsrmExecutionOption_ReEvaluate_ConsiderExistingValue: FsrmExecutionOption = 2
FsrmExecutionOption_ReEvaluate_IgnoreExistingValue: FsrmExecutionOption = 3
FsrmExportImport = Guid('1482dc37-fae9-4787-90-25-8c-e4-e0-24-ab-56')
FsrmFileConditionType = Int32
FsrmFileConditionType_Unknown: FsrmFileConditionType = 0
FsrmFileConditionType_Property: FsrmFileConditionType = 1
FsrmFileGroupManager = Guid('8f1363f6-656f-4496-92-26-13-ae-cb-d7-71-8f')
FsrmFileManagementJobManager = Guid('eb18f9b2-4c3a-4321-b2-03-20-51-20-cf-f6-14')
FsrmFileManagementLoggingFlags = Int32
FsrmFileManagementLoggingFlags_None: FsrmFileManagementLoggingFlags = 0
FsrmFileManagementLoggingFlags_Error: FsrmFileManagementLoggingFlags = 1
FsrmFileManagementLoggingFlags_Information: FsrmFileManagementLoggingFlags = 2
FsrmFileManagementLoggingFlags_Audit: FsrmFileManagementLoggingFlags = 4
FsrmFileManagementType = Int32
FsrmFileManagementType_Unknown: FsrmFileManagementType = 0
FsrmFileManagementType_Expiration: FsrmFileManagementType = 1
FsrmFileManagementType_Custom: FsrmFileManagementType = 2
FsrmFileManagementType_Rms: FsrmFileManagementType = 3
FsrmFileScreenFlags = Int32
FsrmFileScreenFlags_Enforce: FsrmFileScreenFlags = 1
FsrmFileScreenManager = Guid('95941183-db53-4c5f-b3-7b-7d-09-21-cf-9d-c7')
FsrmFileScreenTemplateManager = Guid('243111df-e474-46aa-a0-54-ea-a3-3e-dc-29-2a')
FsrmFileStreamingInterfaceType = Int32
FsrmFileStreamingInterfaceType_Unknown: FsrmFileStreamingInterfaceType = 0
FsrmFileStreamingInterfaceType_ILockBytes: FsrmFileStreamingInterfaceType = 1
FsrmFileStreamingInterfaceType_IStream: FsrmFileStreamingInterfaceType = 2
FsrmFileStreamingMode = Int32
FsrmFileStreamingMode_Unknown: FsrmFileStreamingMode = 0
FsrmFileStreamingMode_Read: FsrmFileStreamingMode = 1
FsrmFileStreamingMode_Write: FsrmFileStreamingMode = 2
FsrmFileSystemPropertyId = Int32
FsrmFileSystemPropertyId_Undefined: FsrmFileSystemPropertyId = 0
FsrmFileSystemPropertyId_FileName: FsrmFileSystemPropertyId = 1
FsrmFileSystemPropertyId_DateCreated: FsrmFileSystemPropertyId = 2
FsrmFileSystemPropertyId_DateLastAccessed: FsrmFileSystemPropertyId = 3
FsrmFileSystemPropertyId_DateLastModified: FsrmFileSystemPropertyId = 4
FsrmFileSystemPropertyId_DateNow: FsrmFileSystemPropertyId = 5
FsrmGetFilePropertyOptions = Int32
FsrmGetFilePropertyOptions_None: FsrmGetFilePropertyOptions = 0
FsrmGetFilePropertyOptions_NoRuleEvaluation: FsrmGetFilePropertyOptions = 1
FsrmGetFilePropertyOptions_Persistent: FsrmGetFilePropertyOptions = 2
FsrmGetFilePropertyOptions_FailOnPersistErrors: FsrmGetFilePropertyOptions = 4
FsrmGetFilePropertyOptions_SkipOrphaned: FsrmGetFilePropertyOptions = 8
FsrmPathMapper = Guid('f3be42bd-8ac2-409e-bb-d8-fa-f9-b6-b4-1f-eb')
FsrmPipelineModuleConnector = Guid('c7643375-1eb5-44de-a0-62-62-35-47-d9-33-bc')
FsrmPipelineModuleType = Int32
FsrmPipelineModuleType_Unknown: FsrmPipelineModuleType = 0
FsrmPipelineModuleType_Storage: FsrmPipelineModuleType = 1
FsrmPipelineModuleType_Classifier: FsrmPipelineModuleType = 2
FsrmPropertyBagField = Int32
FsrmPropertyBagField_AccessVolume: FsrmPropertyBagField = 0
FsrmPropertyBagField_VolumeGuidName: FsrmPropertyBagField = 1
FsrmPropertyBagFlags = Int32
FsrmPropertyBagFlags_UpdatedByClassifier: FsrmPropertyBagFlags = 1
FsrmPropertyBagFlags_FailedLoadingProperties: FsrmPropertyBagFlags = 2
FsrmPropertyBagFlags_FailedSavingProperties: FsrmPropertyBagFlags = 4
FsrmPropertyBagFlags_FailedClassifyingProperties: FsrmPropertyBagFlags = 8
FsrmPropertyConditionType = Int32
FsrmPropertyConditionType_Unknown: FsrmPropertyConditionType = 0
FsrmPropertyConditionType_Equal: FsrmPropertyConditionType = 1
FsrmPropertyConditionType_NotEqual: FsrmPropertyConditionType = 2
FsrmPropertyConditionType_GreaterThan: FsrmPropertyConditionType = 3
FsrmPropertyConditionType_LessThan: FsrmPropertyConditionType = 4
FsrmPropertyConditionType_Contain: FsrmPropertyConditionType = 5
FsrmPropertyConditionType_Exist: FsrmPropertyConditionType = 6
FsrmPropertyConditionType_NotExist: FsrmPropertyConditionType = 7
FsrmPropertyConditionType_StartWith: FsrmPropertyConditionType = 8
FsrmPropertyConditionType_EndWith: FsrmPropertyConditionType = 9
FsrmPropertyConditionType_ContainedIn: FsrmPropertyConditionType = 10
FsrmPropertyConditionType_PrefixOf: FsrmPropertyConditionType = 11
FsrmPropertyConditionType_SuffixOf: FsrmPropertyConditionType = 12
FsrmPropertyConditionType_MatchesPattern: FsrmPropertyConditionType = 13
FsrmPropertyDefinitionAppliesTo = Int32
FsrmPropertyDefinitionAppliesTo_Files: FsrmPropertyDefinitionAppliesTo = 1
FsrmPropertyDefinitionAppliesTo_Folders: FsrmPropertyDefinitionAppliesTo = 2
FsrmPropertyDefinitionFlags = Int32
FsrmPropertyDefinitionFlags_Global: FsrmPropertyDefinitionFlags = 1
FsrmPropertyDefinitionFlags_Deprecated: FsrmPropertyDefinitionFlags = 2
FsrmPropertyDefinitionFlags_Secure: FsrmPropertyDefinitionFlags = 4
FsrmPropertyDefinitionType = Int32
FsrmPropertyDefinitionType_Unknown: FsrmPropertyDefinitionType = 0
FsrmPropertyDefinitionType_OrderedList: FsrmPropertyDefinitionType = 1
FsrmPropertyDefinitionType_MultiChoiceList: FsrmPropertyDefinitionType = 2
FsrmPropertyDefinitionType_SingleChoiceList: FsrmPropertyDefinitionType = 3
FsrmPropertyDefinitionType_String: FsrmPropertyDefinitionType = 4
FsrmPropertyDefinitionType_MultiString: FsrmPropertyDefinitionType = 5
FsrmPropertyDefinitionType_Int: FsrmPropertyDefinitionType = 6
FsrmPropertyDefinitionType_Bool: FsrmPropertyDefinitionType = 7
FsrmPropertyDefinitionType_Date: FsrmPropertyDefinitionType = 8
FsrmPropertyFlags = Int32
FsrmPropertyFlags_None: FsrmPropertyFlags = 0
FsrmPropertyFlags_Orphaned: FsrmPropertyFlags = 1
FsrmPropertyFlags_RetrievedFromCache: FsrmPropertyFlags = 2
FsrmPropertyFlags_RetrievedFromStorage: FsrmPropertyFlags = 4
FsrmPropertyFlags_SetByClassifier: FsrmPropertyFlags = 8
FsrmPropertyFlags_Deleted: FsrmPropertyFlags = 16
FsrmPropertyFlags_Reclassified: FsrmPropertyFlags = 32
FsrmPropertyFlags_AggregationFailed: FsrmPropertyFlags = 64
FsrmPropertyFlags_Existing: FsrmPropertyFlags = 128
FsrmPropertyFlags_FailedLoadingProperties: FsrmPropertyFlags = 256
FsrmPropertyFlags_FailedClassifyingProperties: FsrmPropertyFlags = 512
FsrmPropertyFlags_FailedSavingProperties: FsrmPropertyFlags = 1024
FsrmPropertyFlags_Secure: FsrmPropertyFlags = 2048
FsrmPropertyFlags_PolicyDerived: FsrmPropertyFlags = 4096
FsrmPropertyFlags_Inherited: FsrmPropertyFlags = 8192
FsrmPropertyFlags_Manual: FsrmPropertyFlags = 16384
FsrmPropertyFlags_ExplicitValueDeleted: FsrmPropertyFlags = 32768
FsrmPropertyFlags_PropertyDeletedFromClear: FsrmPropertyFlags = 65536
FsrmPropertyFlags_PropertySourceMask: FsrmPropertyFlags = 14
FsrmPropertyFlags_PersistentMask: FsrmPropertyFlags = 20480
FsrmPropertyValueType = Int32
FsrmPropertyValueType_Undefined: FsrmPropertyValueType = 0
FsrmPropertyValueType_Literal: FsrmPropertyValueType = 1
FsrmPropertyValueType_DateOffset: FsrmPropertyValueType = 2
FsrmQuotaFlags = Int32
FsrmQuotaFlags_Enforce: FsrmQuotaFlags = 256
FsrmQuotaFlags_Disable: FsrmQuotaFlags = 512
FsrmQuotaFlags_StatusIncomplete: FsrmQuotaFlags = 65536
FsrmQuotaFlags_StatusRebuilding: FsrmQuotaFlags = 131072
FsrmQuotaManager = Guid('90dcab7f-347c-4bfc-b5-43-54-03-26-30-5f-be')
FsrmQuotaTemplateManager = Guid('97d3d443-251c-4337-81-e7-b3-2e-8f-4e-e6-5e')
FsrmReportFilter = Int32
FsrmReportFilter_MinSize: FsrmReportFilter = 1
FsrmReportFilter_MinAgeDays: FsrmReportFilter = 2
FsrmReportFilter_MaxAgeDays: FsrmReportFilter = 3
FsrmReportFilter_MinQuotaUsage: FsrmReportFilter = 4
FsrmReportFilter_FileGroups: FsrmReportFilter = 5
FsrmReportFilter_Owners: FsrmReportFilter = 6
FsrmReportFilter_NamePattern: FsrmReportFilter = 7
FsrmReportFilter_Property: FsrmReportFilter = 8
FsrmReportFormat = Int32
FsrmReportFormat_Unknown: FsrmReportFormat = 0
FsrmReportFormat_DHtml: FsrmReportFormat = 1
FsrmReportFormat_Html: FsrmReportFormat = 2
FsrmReportFormat_Txt: FsrmReportFormat = 3
FsrmReportFormat_Csv: FsrmReportFormat = 4
FsrmReportFormat_Xml: FsrmReportFormat = 5
FsrmReportGenerationContext = Int32
FsrmReportGenerationContext_Undefined: FsrmReportGenerationContext = 1
FsrmReportGenerationContext_ScheduledReport: FsrmReportGenerationContext = 2
FsrmReportGenerationContext_InteractiveReport: FsrmReportGenerationContext = 3
FsrmReportGenerationContext_IncidentReport: FsrmReportGenerationContext = 4
FsrmReportLimit = Int32
FsrmReportLimit_MaxFiles: FsrmReportLimit = 1
FsrmReportLimit_MaxFileGroups: FsrmReportLimit = 2
FsrmReportLimit_MaxOwners: FsrmReportLimit = 3
FsrmReportLimit_MaxFilesPerFileGroup: FsrmReportLimit = 4
FsrmReportLimit_MaxFilesPerOwner: FsrmReportLimit = 5
FsrmReportLimit_MaxFilesPerDuplGroup: FsrmReportLimit = 6
FsrmReportLimit_MaxDuplicateGroups: FsrmReportLimit = 7
FsrmReportLimit_MaxQuotas: FsrmReportLimit = 8
FsrmReportLimit_MaxFileScreenEvents: FsrmReportLimit = 9
FsrmReportLimit_MaxPropertyValues: FsrmReportLimit = 10
FsrmReportLimit_MaxFilesPerPropertyValue: FsrmReportLimit = 11
FsrmReportLimit_MaxFolders: FsrmReportLimit = 12
FsrmReportManager = Guid('0058ef37-aa66-4c48-bd-5b-2f-ce-43-2a-b0-c8')
FsrmReportRunningStatus = Int32
FsrmReportRunningStatus_Unknown: FsrmReportRunningStatus = 0
FsrmReportRunningStatus_NotRunning: FsrmReportRunningStatus = 1
FsrmReportRunningStatus_Queued: FsrmReportRunningStatus = 2
FsrmReportRunningStatus_Running: FsrmReportRunningStatus = 3
FsrmReportScheduler = Guid('ea25f1b8-1b8d-4290-8e-e8-e1-7c-12-c2-fe-20')
FsrmReportType = Int32
FsrmReportType_Unknown: FsrmReportType = 0
FsrmReportType_LargeFiles: FsrmReportType = 1
FsrmReportType_FilesByType: FsrmReportType = 2
FsrmReportType_LeastRecentlyAccessed: FsrmReportType = 3
FsrmReportType_MostRecentlyAccessed: FsrmReportType = 4
FsrmReportType_QuotaUsage: FsrmReportType = 5
FsrmReportType_FilesByOwner: FsrmReportType = 6
FsrmReportType_ExportReport: FsrmReportType = 7
FsrmReportType_DuplicateFiles: FsrmReportType = 8
FsrmReportType_FileScreenAudit: FsrmReportType = 9
FsrmReportType_FilesByProperty: FsrmReportType = 10
FsrmReportType_AutomaticClassification: FsrmReportType = 11
FsrmReportType_Expiration: FsrmReportType = 12
FsrmReportType_FoldersByProperty: FsrmReportType = 13
FsrmRuleFlags = Int32
FsrmRuleFlags_Disabled: FsrmRuleFlags = 256
FsrmRuleFlags_ClearAutomaticallyClassifiedProperty: FsrmRuleFlags = 1024
FsrmRuleFlags_ClearManuallyClassifiedProperty: FsrmRuleFlags = 2048
FsrmRuleFlags_Invalid: FsrmRuleFlags = 4096
FsrmRuleType = Int32
FsrmRuleType_Unknown: FsrmRuleType = 0
FsrmRuleType_Classification: FsrmRuleType = 1
FsrmRuleType_Generic: FsrmRuleType = 2
FsrmSetting = Guid('f556d708-6d4d-4594-9c-61-7d-bb-0d-ae-2a-46')
FsrmStorageModuleCaps = Int32
FsrmStorageModuleCaps_Unknown: FsrmStorageModuleCaps = 0
FsrmStorageModuleCaps_CanGet: FsrmStorageModuleCaps = 1
FsrmStorageModuleCaps_CanSet: FsrmStorageModuleCaps = 2
FsrmStorageModuleCaps_CanHandleDirectories: FsrmStorageModuleCaps = 4
FsrmStorageModuleCaps_CanHandleFiles: FsrmStorageModuleCaps = 8
FsrmStorageModuleType = Int32
FsrmStorageModuleType_Unknown: FsrmStorageModuleType = 0
FsrmStorageModuleType_Cache: FsrmStorageModuleType = 1
FsrmStorageModuleType_InFile: FsrmStorageModuleType = 2
FsrmStorageModuleType_Database: FsrmStorageModuleType = 3
FsrmStorageModuleType_System: FsrmStorageModuleType = 100
FsrmTemplateApplyOptions = Int32
FsrmTemplateApplyOptions_ApplyToDerivedMatching: FsrmTemplateApplyOptions = 1
FsrmTemplateApplyOptions_ApplyToDerivedAll: FsrmTemplateApplyOptions = 2
class IFsrmAccessDeniedRemediationClient(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('40002314-590b-45a5-8e-1b-8c-05-da-52-7e-52')
    @commethod(7)
    def Show(parentWnd: UIntPtr, accessPath: win32more.Foundation.BSTR, errorType: win32more.Storage.FileServerResourceManager.AdrClientErrorType, flags: Int32, windowTitle: win32more.Foundation.BSTR, windowMessage: win32more.Foundation.BSTR, result: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class IFsrmAction(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('6cd6408a-ae60-463b-9e-f1-e1-17-53-4d-69-dc')
    @commethod(7)
    def get_Id(id: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_ActionType(actionType: POINTER(win32more.Storage.FileServerResourceManager.FsrmActionType)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_RunLimitInterval(minutes: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_RunLimitInterval(minutes: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Delete() -> win32more.Foundation.HRESULT: ...
class IFsrmActionCommand(c_void_p):
    extends: win32more.Storage.FileServerResourceManager.IFsrmAction
    Guid = Guid('12937789-e247-4917-9c-20-f3-ee-9c-7e-e7-83')
    @commethod(12)
    def get_ExecutablePath(executablePath: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def put_ExecutablePath(executablePath: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_Arguments(arguments: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def put_Arguments(arguments: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_Account(account: POINTER(win32more.Storage.FileServerResourceManager.FsrmAccountType)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def put_Account(account: win32more.Storage.FileServerResourceManager.FsrmAccountType) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def get_WorkingDirectory(workingDirectory: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def put_WorkingDirectory(workingDirectory: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def get_MonitorCommand(monitorCommand: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def put_MonitorCommand(monitorCommand: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def get_KillTimeOut(minutes: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def put_KillTimeOut(minutes: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def get_LogResult(logResults: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def put_LogResult(logResults: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
class IFsrmActionEmail(c_void_p):
    extends: win32more.Storage.FileServerResourceManager.IFsrmAction
    Guid = Guid('d646567d-26ae-4caa-9f-84-4e-0a-ad-20-7f-ca')
    @commethod(12)
    def get_MailFrom(mailFrom: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def put_MailFrom(mailFrom: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_MailReplyTo(mailReplyTo: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def put_MailReplyTo(mailReplyTo: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_MailTo(mailTo: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def put_MailTo(mailTo: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def get_MailCc(mailCc: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def put_MailCc(mailCc: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def get_MailBcc(mailBcc: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def put_MailBcc(mailBcc: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def get_MailSubject(mailSubject: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def put_MailSubject(mailSubject: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def get_MessageText(messageText: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def put_MessageText(messageText: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class IFsrmActionEmail2(c_void_p):
    extends: win32more.Storage.FileServerResourceManager.IFsrmActionEmail
    Guid = Guid('8276702f-2532-4839-89-bf-48-72-60-9a-2e-a4')
    @commethod(26)
    def get_AttachmentFileListSize(attachmentFileListSize: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def put_AttachmentFileListSize(attachmentFileListSize: Int32) -> win32more.Foundation.HRESULT: ...
class IFsrmActionEventLog(c_void_p):
    extends: win32more.Storage.FileServerResourceManager.IFsrmAction
    Guid = Guid('4c8f96c3-5d94-4f37-a4-f4-f5-6a-b4-63-54-6f')
    @commethod(12)
    def get_EventType(eventType: POINTER(win32more.Storage.FileServerResourceManager.FsrmEventType)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def put_EventType(eventType: win32more.Storage.FileServerResourceManager.FsrmEventType) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_MessageText(messageText: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def put_MessageText(messageText: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class IFsrmActionReport(c_void_p):
    extends: win32more.Storage.FileServerResourceManager.IFsrmAction
    Guid = Guid('2dbe63c4-b340-48a0-a5-b0-15-8e-07-fc-56-7e')
    @commethod(12)
    def get_ReportTypes(reportTypes: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def put_ReportTypes(reportTypes: POINTER(win32more.System.Com.SAFEARRAY_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_MailTo(mailTo: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def put_MailTo(mailTo: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class IFsrmAutoApplyQuota(c_void_p):
    extends: win32more.Storage.FileServerResourceManager.IFsrmQuotaObject
    Guid = Guid('f82e5729-6aba-4740-bf-c7-c7-f5-8f-75-fb-7b')
    @commethod(28)
    def get_ExcludeFolders(folders: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def put_ExcludeFolders(folders: POINTER(win32more.System.Com.SAFEARRAY_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def CommitAndUpdateDerived(commitOptions: win32more.Storage.FileServerResourceManager.FsrmCommitOptions, applyOptions: win32more.Storage.FileServerResourceManager.FsrmTemplateApplyOptions, derivedObjectsResult: POINTER(win32more.Storage.FileServerResourceManager.IFsrmDerivedObjectsResult_head)) -> win32more.Foundation.HRESULT: ...
class IFsrmClassificationManager(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('d2dc89da-ee91-48a0-85-d8-cc-72-a5-6f-7d-04')
    @commethod(7)
    def get_ClassificationReportFormats(formats: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_ClassificationReportFormats(formats: POINTER(win32more.System.Com.SAFEARRAY_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Logging(logging: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_Logging(logging: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_ClassificationReportMailTo(mailTo: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def put_ClassificationReportMailTo(mailTo: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_ClassificationReportEnabled(reportEnabled: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def put_ClassificationReportEnabled(reportEnabled: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_ClassificationLastReportPathWithoutExtension(lastReportPath: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_ClassificationLastError(lastError: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_ClassificationRunningStatus(runningStatus: POINTER(win32more.Storage.FileServerResourceManager.FsrmReportRunningStatus)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def EnumPropertyDefinitions(options: win32more.Storage.FileServerResourceManager.FsrmEnumOptions, propertyDefinitions: POINTER(win32more.Storage.FileServerResourceManager.IFsrmCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def CreatePropertyDefinition(propertyDefinition: POINTER(win32more.Storage.FileServerResourceManager.IFsrmPropertyDefinition_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def GetPropertyDefinition(propertyName: win32more.Foundation.BSTR, propertyDefinition: POINTER(win32more.Storage.FileServerResourceManager.IFsrmPropertyDefinition_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def EnumRules(ruleType: win32more.Storage.FileServerResourceManager.FsrmRuleType, options: win32more.Storage.FileServerResourceManager.FsrmEnumOptions, Rules: POINTER(win32more.Storage.FileServerResourceManager.IFsrmCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def CreateRule(ruleType: win32more.Storage.FileServerResourceManager.FsrmRuleType, Rule: POINTER(win32more.Storage.FileServerResourceManager.IFsrmRule_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def GetRule(ruleName: win32more.Foundation.BSTR, ruleType: win32more.Storage.FileServerResourceManager.FsrmRuleType, Rule: POINTER(win32more.Storage.FileServerResourceManager.IFsrmRule_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def EnumModuleDefinitions(moduleType: win32more.Storage.FileServerResourceManager.FsrmPipelineModuleType, options: win32more.Storage.FileServerResourceManager.FsrmEnumOptions, moduleDefinitions: POINTER(win32more.Storage.FileServerResourceManager.IFsrmCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def CreateModuleDefinition(moduleType: win32more.Storage.FileServerResourceManager.FsrmPipelineModuleType, moduleDefinition: POINTER(win32more.Storage.FileServerResourceManager.IFsrmPipelineModuleDefinition_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def GetModuleDefinition(moduleName: win32more.Foundation.BSTR, moduleType: win32more.Storage.FileServerResourceManager.FsrmPipelineModuleType, moduleDefinition: POINTER(win32more.Storage.FileServerResourceManager.IFsrmPipelineModuleDefinition_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def RunClassification(context: win32more.Storage.FileServerResourceManager.FsrmReportGenerationContext, reserved: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def WaitForClassificationCompletion(waitSeconds: Int32, completed: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def CancelClassification() -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def EnumFileProperties(filePath: win32more.Foundation.BSTR, options: win32more.Storage.FileServerResourceManager.FsrmGetFilePropertyOptions, fileProperties: POINTER(win32more.Storage.FileServerResourceManager.IFsrmCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def GetFileProperty(filePath: win32more.Foundation.BSTR, propertyName: win32more.Foundation.BSTR, options: win32more.Storage.FileServerResourceManager.FsrmGetFilePropertyOptions, property: POINTER(win32more.Storage.FileServerResourceManager.IFsrmProperty_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def SetFileProperty(filePath: win32more.Foundation.BSTR, propertyName: win32more.Foundation.BSTR, propertyValue: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def ClearFileProperty(filePath: win32more.Foundation.BSTR, property: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class IFsrmClassificationManager2(c_void_p):
    extends: win32more.Storage.FileServerResourceManager.IFsrmClassificationManager
    Guid = Guid('0004c1c9-127e-4765-ba-07-6a-31-47-bc-a1-12')
    @commethod(34)
    def ClassifyFiles(filePaths: POINTER(win32more.System.Com.SAFEARRAY_head), propertyNames: POINTER(win32more.System.Com.SAFEARRAY_head), propertyValues: POINTER(win32more.System.Com.SAFEARRAY_head), options: win32more.Storage.FileServerResourceManager.FsrmGetFilePropertyOptions) -> win32more.Foundation.HRESULT: ...
class IFsrmClassificationRule(c_void_p):
    extends: win32more.Storage.FileServerResourceManager.IFsrmRule
    Guid = Guid('afc052c2-5315-45ab-84-1b-c6-db-0e-12-01-48')
    @commethod(24)
    def get_ExecutionOption(executionOption: POINTER(win32more.Storage.FileServerResourceManager.FsrmExecutionOption)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def put_ExecutionOption(executionOption: win32more.Storage.FileServerResourceManager.FsrmExecutionOption) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def get_PropertyAffected(property: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def put_PropertyAffected(property: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def get_Value(value: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def put_Value(value: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class IFsrmClassifierModuleDefinition(c_void_p):
    extends: win32more.Storage.FileServerResourceManager.IFsrmPipelineModuleDefinition
    Guid = Guid('bb36ea26-6318-4b8c-85-92-f7-2d-d6-02-e7-a5')
    @commethod(31)
    def get_PropertiesAffected(propertiesAffected: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def put_PropertiesAffected(propertiesAffected: POINTER(win32more.System.Com.SAFEARRAY_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def get_PropertiesUsed(propertiesUsed: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def put_PropertiesUsed(propertiesUsed: POINTER(win32more.System.Com.SAFEARRAY_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def get_NeedsExplicitValue(needsExplicitValue: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def put_NeedsExplicitValue(needsExplicitValue: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
class IFsrmClassifierModuleImplementation(c_void_p):
    extends: win32more.Storage.FileServerResourceManager.IFsrmPipelineModuleImplementation
    Guid = Guid('4c968fc6-6edb-4051-9c-18-73-b7-29-1a-e1-06')
    @commethod(9)
    def get_LastModified(lastModified: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def UseRulesAndDefinitions(rules: win32more.Storage.FileServerResourceManager.IFsrmCollection_head, propertyDefinitions: win32more.Storage.FileServerResourceManager.IFsrmCollection_head) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def OnBeginFile(propertyBag: win32more.Storage.FileServerResourceManager.IFsrmPropertyBag_head, arrayRuleIds: POINTER(win32more.System.Com.SAFEARRAY_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def DoesPropertyValueApply(property: win32more.Foundation.BSTR, value: win32more.Foundation.BSTR, applyValue: POINTER(win32more.Foundation.VARIANT_BOOL), idRule: Guid, idPropDef: Guid) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetPropertyValueToApply(property: win32more.Foundation.BSTR, value: POINTER(win32more.Foundation.BSTR), idRule: Guid, idPropDef: Guid) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def OnEndFile() -> win32more.Foundation.HRESULT: ...
class IFsrmCollection(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('f76fbf3b-8ddd-4b42-b0-5a-cb-1c-3f-f1-fe-e8')
    @commethod(7)
    def get__NewEnum(unknown: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(index: Int32, item: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(count: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_State(state: POINTER(win32more.Storage.FileServerResourceManager.FsrmCollectionState)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Cancel() -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def WaitForCompletion(waitSeconds: Int32, completed: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetById(id: Guid, entry: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
class IFsrmCommittableCollection(c_void_p):
    extends: win32more.Storage.FileServerResourceManager.IFsrmMutableCollection
    Guid = Guid('96deb3b5-8b91-4a2a-9d-93-80-a3-5d-8a-a8-47')
    @commethod(18)
    def Commit(options: win32more.Storage.FileServerResourceManager.FsrmCommitOptions, results: POINTER(win32more.Storage.FileServerResourceManager.IFsrmCollection_head)) -> win32more.Foundation.HRESULT: ...
class IFsrmDerivedObjectsResult(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('39322a2d-38ee-4d0d-80-95-42-1a-80-84-9a-82')
    @commethod(7)
    def get_DerivedObjects(derivedObjects: POINTER(win32more.Storage.FileServerResourceManager.IFsrmCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Results(results: POINTER(win32more.Storage.FileServerResourceManager.IFsrmCollection_head)) -> win32more.Foundation.HRESULT: ...
class IFsrmExportImport(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('efcb0ab1-16c4-4a79-81-2c-72-56-14-c3-30-6b')
    @commethod(7)
    def ExportFileGroups(filePath: win32more.Foundation.BSTR, fileGroupNamesSafeArray: POINTER(win32more.System.Com.VARIANT_head), remoteHost: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def ImportFileGroups(filePath: win32more.Foundation.BSTR, fileGroupNamesSafeArray: POINTER(win32more.System.Com.VARIANT_head), remoteHost: win32more.Foundation.BSTR, fileGroups: POINTER(win32more.Storage.FileServerResourceManager.IFsrmCommittableCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def ExportFileScreenTemplates(filePath: win32more.Foundation.BSTR, templateNamesSafeArray: POINTER(win32more.System.Com.VARIANT_head), remoteHost: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def ImportFileScreenTemplates(filePath: win32more.Foundation.BSTR, templateNamesSafeArray: POINTER(win32more.System.Com.VARIANT_head), remoteHost: win32more.Foundation.BSTR, templates: POINTER(win32more.Storage.FileServerResourceManager.IFsrmCommittableCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def ExportQuotaTemplates(filePath: win32more.Foundation.BSTR, templateNamesSafeArray: POINTER(win32more.System.Com.VARIANT_head), remoteHost: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def ImportQuotaTemplates(filePath: win32more.Foundation.BSTR, templateNamesSafeArray: POINTER(win32more.System.Com.VARIANT_head), remoteHost: win32more.Foundation.BSTR, templates: POINTER(win32more.Storage.FileServerResourceManager.IFsrmCommittableCollection_head)) -> win32more.Foundation.HRESULT: ...
class IFsrmFileCondition(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('70684ffc-691a-4a1a-b9-22-97-75-2e-13-8c-c1')
    @commethod(7)
    def get_Type(pVal: POINTER(win32more.Storage.FileServerResourceManager.FsrmFileConditionType)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Delete() -> win32more.Foundation.HRESULT: ...
class IFsrmFileConditionProperty(c_void_p):
    extends: win32more.Storage.FileServerResourceManager.IFsrmFileCondition
    Guid = Guid('81926775-b981-4479-98-8f-da-17-1d-62-73-60')
    @commethod(9)
    def get_PropertyName(pVal: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_PropertyName(newVal: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_PropertyId(pVal: POINTER(win32more.Storage.FileServerResourceManager.FsrmFileSystemPropertyId)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def put_PropertyId(newVal: win32more.Storage.FileServerResourceManager.FsrmFileSystemPropertyId) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_Operator(pVal: POINTER(win32more.Storage.FileServerResourceManager.FsrmPropertyConditionType)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def put_Operator(newVal: win32more.Storage.FileServerResourceManager.FsrmPropertyConditionType) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_ValueType(pVal: POINTER(win32more.Storage.FileServerResourceManager.FsrmPropertyValueType)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def put_ValueType(newVal: win32more.Storage.FileServerResourceManager.FsrmPropertyValueType) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_Value(pVal: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def put_Value(newVal: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
class IFsrmFileGroup(c_void_p):
    extends: win32more.Storage.FileServerResourceManager.IFsrmObject
    Guid = Guid('8dd04909-0e34-4d55-af-aa-89-e1-f1-a1-bb-b9')
    @commethod(12)
    def get_Name(name: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def put_Name(name: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_Members(members: POINTER(win32more.Storage.FileServerResourceManager.IFsrmMutableCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def put_Members(members: win32more.Storage.FileServerResourceManager.IFsrmMutableCollection_head) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_NonMembers(nonMembers: POINTER(win32more.Storage.FileServerResourceManager.IFsrmMutableCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def put_NonMembers(nonMembers: win32more.Storage.FileServerResourceManager.IFsrmMutableCollection_head) -> win32more.Foundation.HRESULT: ...
class IFsrmFileGroupImported(c_void_p):
    extends: win32more.Storage.FileServerResourceManager.IFsrmFileGroup
    Guid = Guid('ad55f10b-5f11-4be7-94-ef-d9-ee-2e-47-0d-ed')
    @commethod(18)
    def get_OverwriteOnCommit(overwrite: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def put_OverwriteOnCommit(overwrite: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
class IFsrmFileGroupManager(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('426677d5-018c-485c-8a-51-20-b8-6d-00-bd-c4')
    @commethod(7)
    def CreateFileGroup(fileGroup: POINTER(win32more.Storage.FileServerResourceManager.IFsrmFileGroup_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetFileGroup(name: win32more.Foundation.BSTR, fileGroup: POINTER(win32more.Storage.FileServerResourceManager.IFsrmFileGroup_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def EnumFileGroups(options: win32more.Storage.FileServerResourceManager.FsrmEnumOptions, fileGroups: POINTER(win32more.Storage.FileServerResourceManager.IFsrmCommittableCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def ExportFileGroups(fileGroupNamesArray: POINTER(win32more.System.Com.VARIANT_head), serializedFileGroups: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def ImportFileGroups(serializedFileGroups: win32more.Foundation.BSTR, fileGroupNamesArray: POINTER(win32more.System.Com.VARIANT_head), fileGroups: POINTER(win32more.Storage.FileServerResourceManager.IFsrmCommittableCollection_head)) -> win32more.Foundation.HRESULT: ...
class IFsrmFileManagementJob(c_void_p):
    extends: win32more.Storage.FileServerResourceManager.IFsrmObject
    Guid = Guid('0770687e-9f36-4d6f-87-78-59-9d-18-84-61-c9')
    @commethod(12)
    def get_Name(name: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def put_Name(name: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_NamespaceRoots(namespaceRoots: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def put_NamespaceRoots(namespaceRoots: POINTER(win32more.System.Com.SAFEARRAY_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_Enabled(enabled: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def put_Enabled(enabled: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def get_OperationType(operationType: POINTER(win32more.Storage.FileServerResourceManager.FsrmFileManagementType)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def put_OperationType(operationType: win32more.Storage.FileServerResourceManager.FsrmFileManagementType) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def get_ExpirationDirectory(expirationDirectory: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def put_ExpirationDirectory(expirationDirectory: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def get_CustomAction(action: POINTER(win32more.Storage.FileServerResourceManager.IFsrmActionCommand_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def get_Notifications(notifications: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def get_Logging(loggingFlags: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def put_Logging(loggingFlags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def get_ReportEnabled(reportEnabled: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def put_ReportEnabled(reportEnabled: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def get_Formats(formats: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def put_Formats(formats: POINTER(win32more.System.Com.SAFEARRAY_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def get_MailTo(mailTo: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def put_MailTo(mailTo: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def get_DaysSinceFileCreated(daysSinceCreation: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def put_DaysSinceFileCreated(daysSinceCreation: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def get_DaysSinceFileLastAccessed(daysSinceAccess: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def put_DaysSinceFileLastAccessed(daysSinceAccess: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def get_DaysSinceFileLastModified(daysSinceModify: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def put_DaysSinceFileLastModified(daysSinceModify: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def get_PropertyConditions(propertyConditions: POINTER(win32more.Storage.FileServerResourceManager.IFsrmCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def get_FromDate(fromDate: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(40)
    def put_FromDate(fromDate: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(41)
    def get_Task(taskName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(42)
    def put_Task(taskName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(43)
    def get_Parameters(parameters: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(44)
    def put_Parameters(parameters: POINTER(win32more.System.Com.SAFEARRAY_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(45)
    def get_RunningStatus(runningStatus: POINTER(win32more.Storage.FileServerResourceManager.FsrmReportRunningStatus)) -> win32more.Foundation.HRESULT: ...
    @commethod(46)
    def get_LastError(lastError: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(47)
    def get_LastReportPathWithoutExtension(path: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(48)
    def get_LastRun(lastRun: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(49)
    def get_FileNamePattern(fileNamePattern: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(50)
    def put_FileNamePattern(fileNamePattern: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(51)
    def Run(context: win32more.Storage.FileServerResourceManager.FsrmReportGenerationContext) -> win32more.Foundation.HRESULT: ...
    @commethod(52)
    def WaitForCompletion(waitSeconds: Int32, completed: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(53)
    def Cancel() -> win32more.Foundation.HRESULT: ...
    @commethod(54)
    def AddNotification(days: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(55)
    def DeleteNotification(days: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(56)
    def ModifyNotification(days: Int32, newDays: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(57)
    def CreateNotificationAction(days: Int32, actionType: win32more.Storage.FileServerResourceManager.FsrmActionType, action: POINTER(win32more.Storage.FileServerResourceManager.IFsrmAction_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(58)
    def EnumNotificationActions(days: Int32, actions: POINTER(win32more.Storage.FileServerResourceManager.IFsrmCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(59)
    def CreatePropertyCondition(name: win32more.Foundation.BSTR, propertyCondition: POINTER(win32more.Storage.FileServerResourceManager.IFsrmPropertyCondition_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(60)
    def CreateCustomAction(customAction: POINTER(win32more.Storage.FileServerResourceManager.IFsrmActionCommand_head)) -> win32more.Foundation.HRESULT: ...
class IFsrmFileManagementJobManager(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('ee321ecb-d95e-48e9-90-7c-c7-68-5a-01-32-35')
    @commethod(7)
    def get_ActionVariables(variables: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_ActionVariableDescriptions(descriptions: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def EnumFileManagementJobs(options: win32more.Storage.FileServerResourceManager.FsrmEnumOptions, fileManagementJobs: POINTER(win32more.Storage.FileServerResourceManager.IFsrmCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def CreateFileManagementJob(fileManagementJob: POINTER(win32more.Storage.FileServerResourceManager.IFsrmFileManagementJob_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetFileManagementJob(name: win32more.Foundation.BSTR, fileManagementJob: POINTER(win32more.Storage.FileServerResourceManager.IFsrmFileManagementJob_head)) -> win32more.Foundation.HRESULT: ...
class IFsrmFileScreen(c_void_p):
    extends: win32more.Storage.FileServerResourceManager.IFsrmFileScreenBase
    Guid = Guid('5f6325d3-ce88-4733-84-c1-2d-6a-ef-c5-ea-07')
    @commethod(18)
    def get_Path(path: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get_SourceTemplateName(fileScreenTemplateName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def get_MatchesSourceTemplate(matches: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def get_UserSid(userSid: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def get_UserAccount(userAccount: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def ApplyTemplate(fileScreenTemplateName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class IFsrmFileScreenBase(c_void_p):
    extends: win32more.Storage.FileServerResourceManager.IFsrmObject
    Guid = Guid('f3637e80-5b22-4a2b-a6-37-bb-b6-42-b4-1c-fc')
    @commethod(12)
    def get_BlockedFileGroups(blockList: POINTER(win32more.Storage.FileServerResourceManager.IFsrmMutableCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def put_BlockedFileGroups(blockList: win32more.Storage.FileServerResourceManager.IFsrmMutableCollection_head) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_FileScreenFlags(fileScreenFlags: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def put_FileScreenFlags(fileScreenFlags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def CreateAction(actionType: win32more.Storage.FileServerResourceManager.FsrmActionType, action: POINTER(win32more.Storage.FileServerResourceManager.IFsrmAction_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def EnumActions(actions: POINTER(win32more.Storage.FileServerResourceManager.IFsrmCollection_head)) -> win32more.Foundation.HRESULT: ...
class IFsrmFileScreenException(c_void_p):
    extends: win32more.Storage.FileServerResourceManager.IFsrmObject
    Guid = Guid('bee7ce02-df77-4515-93-89-78-f0-1c-5a-fc-1a')
    @commethod(12)
    def get_Path(path: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_AllowedFileGroups(allowList: POINTER(win32more.Storage.FileServerResourceManager.IFsrmMutableCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def put_AllowedFileGroups(allowList: win32more.Storage.FileServerResourceManager.IFsrmMutableCollection_head) -> win32more.Foundation.HRESULT: ...
class IFsrmFileScreenManager(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('ff4fa04e-5a94-4bda-a3-a0-d5-b4-d3-c5-2e-ba')
    @commethod(7)
    def get_ActionVariables(variables: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_ActionVariableDescriptions(descriptions: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def CreateFileScreen(path: win32more.Foundation.BSTR, fileScreen: POINTER(win32more.Storage.FileServerResourceManager.IFsrmFileScreen_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetFileScreen(path: win32more.Foundation.BSTR, fileScreen: POINTER(win32more.Storage.FileServerResourceManager.IFsrmFileScreen_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def EnumFileScreens(path: win32more.Foundation.BSTR, options: win32more.Storage.FileServerResourceManager.FsrmEnumOptions, fileScreens: POINTER(win32more.Storage.FileServerResourceManager.IFsrmCommittableCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def CreateFileScreenException(path: win32more.Foundation.BSTR, fileScreenException: POINTER(win32more.Storage.FileServerResourceManager.IFsrmFileScreenException_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetFileScreenException(path: win32more.Foundation.BSTR, fileScreenException: POINTER(win32more.Storage.FileServerResourceManager.IFsrmFileScreenException_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def EnumFileScreenExceptions(path: win32more.Foundation.BSTR, options: win32more.Storage.FileServerResourceManager.FsrmEnumOptions, fileScreenExceptions: POINTER(win32more.Storage.FileServerResourceManager.IFsrmCommittableCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def CreateFileScreenCollection(collection: POINTER(win32more.Storage.FileServerResourceManager.IFsrmCommittableCollection_head)) -> win32more.Foundation.HRESULT: ...
class IFsrmFileScreenTemplate(c_void_p):
    extends: win32more.Storage.FileServerResourceManager.IFsrmFileScreenBase
    Guid = Guid('205bebf8-dd93-452a-95-a6-32-b5-66-b3-58-28')
    @commethod(18)
    def get_Name(name: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def put_Name(name: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def CopyTemplate(fileScreenTemplateName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def CommitAndUpdateDerived(commitOptions: win32more.Storage.FileServerResourceManager.FsrmCommitOptions, applyOptions: win32more.Storage.FileServerResourceManager.FsrmTemplateApplyOptions, derivedObjectsResult: POINTER(win32more.Storage.FileServerResourceManager.IFsrmDerivedObjectsResult_head)) -> win32more.Foundation.HRESULT: ...
class IFsrmFileScreenTemplateImported(c_void_p):
    extends: win32more.Storage.FileServerResourceManager.IFsrmFileScreenTemplate
    Guid = Guid('e1010359-3e5d-4ecd-9f-e4-ef-48-62-2f-df-30')
    @commethod(22)
    def get_OverwriteOnCommit(overwrite: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def put_OverwriteOnCommit(overwrite: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
class IFsrmFileScreenTemplateManager(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('cfe36cba-1949-4e74-a1-4f-f1-d5-80-ce-af-13')
    @commethod(7)
    def CreateTemplate(fileScreenTemplate: POINTER(win32more.Storage.FileServerResourceManager.IFsrmFileScreenTemplate_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetTemplate(name: win32more.Foundation.BSTR, fileScreenTemplate: POINTER(win32more.Storage.FileServerResourceManager.IFsrmFileScreenTemplate_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def EnumTemplates(options: win32more.Storage.FileServerResourceManager.FsrmEnumOptions, fileScreenTemplates: POINTER(win32more.Storage.FileServerResourceManager.IFsrmCommittableCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def ExportTemplates(fileScreenTemplateNamesArray: POINTER(win32more.System.Com.VARIANT_head), serializedFileScreenTemplates: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def ImportTemplates(serializedFileScreenTemplates: win32more.Foundation.BSTR, fileScreenTemplateNamesArray: POINTER(win32more.System.Com.VARIANT_head), fileScreenTemplates: POINTER(win32more.Storage.FileServerResourceManager.IFsrmCommittableCollection_head)) -> win32more.Foundation.HRESULT: ...
class IFsrmMutableCollection(c_void_p):
    extends: win32more.Storage.FileServerResourceManager.IFsrmCollection
    Guid = Guid('1bb617b8-3886-49dc-af-82-a6-c9-0f-a3-5d-da')
    @commethod(14)
    def Add(item: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def Remove(index: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def RemoveById(id: Guid) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def Clone(collection: POINTER(win32more.Storage.FileServerResourceManager.IFsrmMutableCollection_head)) -> win32more.Foundation.HRESULT: ...
class IFsrmObject(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('22bcef93-4a3f-4183-89-f9-2f-8b-8a-62-8a-ee')
    @commethod(7)
    def get_Id(id: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Description(description: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def put_Description(description: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def Delete() -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Commit() -> win32more.Foundation.HRESULT: ...
class IFsrmPathMapper(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('6f4dbfff-6920-4821-a6-c3-b7-e9-4c-1f-d6-0c')
    @commethod(7)
    def GetSharePathsForLocalPath(localPath: win32more.Foundation.BSTR, sharePaths: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
class IFsrmPipelineModuleConnector(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('c16014f3-9aa1-46b3-b0-a7-ab-14-6e-b2-05-f2')
    @commethod(7)
    def get_ModuleImplementation(pipelineModuleImplementation: POINTER(win32more.Storage.FileServerResourceManager.IFsrmPipelineModuleImplementation_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_ModuleName(userName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_HostingUserAccount(userAccount: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_HostingProcessPid(pid: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Bind(moduleDefinition: win32more.Storage.FileServerResourceManager.IFsrmPipelineModuleDefinition_head, moduleImplementation: win32more.Storage.FileServerResourceManager.IFsrmPipelineModuleImplementation_head) -> win32more.Foundation.HRESULT: ...
class IFsrmPipelineModuleDefinition(c_void_p):
    extends: win32more.Storage.FileServerResourceManager.IFsrmObject
    Guid = Guid('515c1277-2c81-440e-8f-cf-36-79-21-ed-4f-59')
    @commethod(12)
    def get_ModuleClsid(moduleClsid: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def put_ModuleClsid(moduleClsid: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_Name(name: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def put_Name(name: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_Company(company: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def put_Company(company: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def get_Version(version: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def put_Version(version: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def get_ModuleType(moduleType: POINTER(win32more.Storage.FileServerResourceManager.FsrmPipelineModuleType)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def get_Enabled(enabled: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def put_Enabled(enabled: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def get_NeedsFileContent(needsFileContent: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def put_NeedsFileContent(needsFileContent: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def get_Account(retrievalAccount: POINTER(win32more.Storage.FileServerResourceManager.FsrmAccountType)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def put_Account(retrievalAccount: win32more.Storage.FileServerResourceManager.FsrmAccountType) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def get_SupportedExtensions(supportedExtensions: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def put_SupportedExtensions(supportedExtensions: POINTER(win32more.System.Com.SAFEARRAY_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def get_Parameters(parameters: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def put_Parameters(parameters: POINTER(win32more.System.Com.SAFEARRAY_head)) -> win32more.Foundation.HRESULT: ...
class IFsrmPipelineModuleImplementation(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('b7907906-2b02-4cb5-84-a9-fd-f5-46-13-d6-cd')
    @commethod(7)
    def OnLoad(moduleDefinition: win32more.Storage.FileServerResourceManager.IFsrmPipelineModuleDefinition_head, moduleConnector: POINTER(win32more.Storage.FileServerResourceManager.IFsrmPipelineModuleConnector_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def OnUnload() -> win32more.Foundation.HRESULT: ...
class IFsrmProperty(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('4a73fee4-4102-4fcc-9f-fb-38-61-4f-9e-e7-68')
    @commethod(7)
    def get_Name(name: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Value(value: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Sources(sources: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_PropertyFlags(flags: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class IFsrmPropertyBag(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('774589d1-d300-4f7a-9a-24-f7-b7-66-80-02-50')
    @commethod(7)
    def get_Name(name: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_RelativePath(path: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_VolumeName(volumeName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_RelativeNamespaceRoot(relativeNamespaceRoot: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_VolumeIndex(volumeId: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_FileId(fileId: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_ParentDirectoryId(parentDirectoryId: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_Size(size: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_SizeAllocated(sizeAllocated: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_CreationTime(creationTime: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_LastAccessTime(lastAccessTime: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def get_LastModificationTime(lastModificationTime: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get_Attributes(attributes: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def get_OwnerSid(ownerSid: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def get_FilePropertyNames(filePropertyNames: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def get_Messages(messages: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def get_PropertyBagFlags(flags: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def GetFileProperty(name: win32more.Foundation.BSTR, fileProperty: POINTER(win32more.Storage.FileServerResourceManager.IFsrmProperty_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def SetFileProperty(name: win32more.Foundation.BSTR, value: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def AddMessage(message: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def GetFileStreamInterface(accessMode: win32more.Storage.FileServerResourceManager.FsrmFileStreamingMode, interfaceType: win32more.Storage.FileServerResourceManager.FsrmFileStreamingInterfaceType, pStreamInterface: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
class IFsrmPropertyBag2(c_void_p):
    extends: win32more.Storage.FileServerResourceManager.IFsrmPropertyBag
    Guid = Guid('0e46bdbd-2402-4fed-9c-30-92-66-e6-eb-2c-c9')
    @commethod(28)
    def GetFieldValue(field: win32more.Storage.FileServerResourceManager.FsrmPropertyBagField, value: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def GetUntrustedInFileProperties(props: POINTER(win32more.Storage.FileServerResourceManager.IFsrmCollection_head)) -> win32more.Foundation.HRESULT: ...
class IFsrmPropertyCondition(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('326af66f-2ac0-4f68-bf-8c-47-59-f0-54-fa-29')
    @commethod(7)
    def get_Name(name: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_Name(name: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Type(type: POINTER(win32more.Storage.FileServerResourceManager.FsrmPropertyConditionType)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_Type(type: win32more.Storage.FileServerResourceManager.FsrmPropertyConditionType) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_Value(value: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def put_Value(value: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def Delete() -> win32more.Foundation.HRESULT: ...
class IFsrmPropertyDefinition(c_void_p):
    extends: win32more.Storage.FileServerResourceManager.IFsrmObject
    Guid = Guid('ede0150f-e9a3-419c-87-7c-01-fe-5d-24-c5-d3')
    @commethod(12)
    def get_Name(name: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def put_Name(name: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_Type(type: POINTER(win32more.Storage.FileServerResourceManager.FsrmPropertyDefinitionType)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def put_Type(type: win32more.Storage.FileServerResourceManager.FsrmPropertyDefinitionType) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_PossibleValues(possibleValues: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def put_PossibleValues(possibleValues: POINTER(win32more.System.Com.SAFEARRAY_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def get_ValueDescriptions(valueDescriptions: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def put_ValueDescriptions(valueDescriptions: POINTER(win32more.System.Com.SAFEARRAY_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def get_Parameters(parameters: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def put_Parameters(parameters: POINTER(win32more.System.Com.SAFEARRAY_head)) -> win32more.Foundation.HRESULT: ...
class IFsrmPropertyDefinition2(c_void_p):
    extends: win32more.Storage.FileServerResourceManager.IFsrmPropertyDefinition
    Guid = Guid('47782152-d16c-4229-b4-e1-0d-df-e3-08-b9-f6')
    @commethod(22)
    def get_PropertyDefinitionFlags(propertyDefinitionFlags: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def get_DisplayName(name: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def put_DisplayName(name: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def get_AppliesTo(appliesTo: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def get_ValueDefinitions(valueDefinitions: POINTER(win32more.Storage.FileServerResourceManager.IFsrmCollection_head)) -> win32more.Foundation.HRESULT: ...
class IFsrmPropertyDefinitionValue(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('e946d148-bd67-4178-8e-22-1c-44-92-5e-d7-10')
    @commethod(7)
    def get_Name(name: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_DisplayName(displayName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Description(description: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_UniqueID(uniqueID: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IFsrmQuota(c_void_p):
    extends: win32more.Storage.FileServerResourceManager.IFsrmQuotaObject
    Guid = Guid('377f739d-9647-4b8e-97-d2-5f-fc-e6-d7-59-cd')
    @commethod(28)
    def get_QuotaUsed(used: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def get_QuotaPeakUsage(peakUsage: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def get_QuotaPeakUsageTime(peakUsageDateTime: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def ResetPeakUsage() -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def RefreshUsageProperties() -> win32more.Foundation.HRESULT: ...
class IFsrmQuotaBase(c_void_p):
    extends: win32more.Storage.FileServerResourceManager.IFsrmObject
    Guid = Guid('1568a795-3924-4118-b7-4b-68-d8-f0-fa-5d-af')
    @commethod(12)
    def get_QuotaLimit(quotaLimit: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def put_QuotaLimit(quotaLimit: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_QuotaFlags(quotaFlags: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def put_QuotaFlags(quotaFlags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_Thresholds(thresholds: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def AddThreshold(threshold: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def DeleteThreshold(threshold: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def ModifyThreshold(threshold: Int32, newThreshold: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def CreateThresholdAction(threshold: Int32, actionType: win32more.Storage.FileServerResourceManager.FsrmActionType, action: POINTER(win32more.Storage.FileServerResourceManager.IFsrmAction_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def EnumThresholdActions(threshold: Int32, actions: POINTER(win32more.Storage.FileServerResourceManager.IFsrmCollection_head)) -> win32more.Foundation.HRESULT: ...
class IFsrmQuotaManager(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('8bb68c7d-19d8-4ffb-80-9e-be-4f-c1-73-40-14')
    @commethod(7)
    def get_ActionVariables(variables: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_ActionVariableDescriptions(descriptions: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def CreateQuota(path: win32more.Foundation.BSTR, quota: POINTER(win32more.Storage.FileServerResourceManager.IFsrmQuota_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def CreateAutoApplyQuota(quotaTemplateName: win32more.Foundation.BSTR, path: win32more.Foundation.BSTR, quota: POINTER(win32more.Storage.FileServerResourceManager.IFsrmAutoApplyQuota_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetQuota(path: win32more.Foundation.BSTR, quota: POINTER(win32more.Storage.FileServerResourceManager.IFsrmQuota_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetAutoApplyQuota(path: win32more.Foundation.BSTR, quota: POINTER(win32more.Storage.FileServerResourceManager.IFsrmAutoApplyQuota_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetRestrictiveQuota(path: win32more.Foundation.BSTR, quota: POINTER(win32more.Storage.FileServerResourceManager.IFsrmQuota_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def EnumQuotas(path: win32more.Foundation.BSTR, options: win32more.Storage.FileServerResourceManager.FsrmEnumOptions, quotas: POINTER(win32more.Storage.FileServerResourceManager.IFsrmCommittableCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def EnumAutoApplyQuotas(path: win32more.Foundation.BSTR, options: win32more.Storage.FileServerResourceManager.FsrmEnumOptions, quotas: POINTER(win32more.Storage.FileServerResourceManager.IFsrmCommittableCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def EnumEffectiveQuotas(path: win32more.Foundation.BSTR, options: win32more.Storage.FileServerResourceManager.FsrmEnumOptions, quotas: POINTER(win32more.Storage.FileServerResourceManager.IFsrmCommittableCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def Scan(strPath: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def CreateQuotaCollection(collection: POINTER(win32more.Storage.FileServerResourceManager.IFsrmCommittableCollection_head)) -> win32more.Foundation.HRESULT: ...
class IFsrmQuotaManagerEx(c_void_p):
    extends: win32more.Storage.FileServerResourceManager.IFsrmQuotaManager
    Guid = Guid('4846cb01-d430-494f-ab-b4-b1-05-49-99-fb-09')
    @commethod(19)
    def IsAffectedByQuota(path: win32more.Foundation.BSTR, options: win32more.Storage.FileServerResourceManager.FsrmEnumOptions, affected: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
class IFsrmQuotaObject(c_void_p):
    extends: win32more.Storage.FileServerResourceManager.IFsrmQuotaBase
    Guid = Guid('42dc3511-61d5-48ae-b6-dc-59-fc-00-c0-a8-d6')
    @commethod(22)
    def get_Path(path: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def get_UserSid(userSid: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def get_UserAccount(userAccount: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def get_SourceTemplateName(quotaTemplateName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def get_MatchesSourceTemplate(matches: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def ApplyTemplate(quotaTemplateName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class IFsrmQuotaTemplate(c_void_p):
    extends: win32more.Storage.FileServerResourceManager.IFsrmQuotaBase
    Guid = Guid('a2efab31-295e-46bb-b9-76-e8-6d-58-b5-2e-8b')
    @commethod(22)
    def get_Name(name: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def put_Name(name: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def CopyTemplate(quotaTemplateName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def CommitAndUpdateDerived(commitOptions: win32more.Storage.FileServerResourceManager.FsrmCommitOptions, applyOptions: win32more.Storage.FileServerResourceManager.FsrmTemplateApplyOptions, derivedObjectsResult: POINTER(win32more.Storage.FileServerResourceManager.IFsrmDerivedObjectsResult_head)) -> win32more.Foundation.HRESULT: ...
class IFsrmQuotaTemplateImported(c_void_p):
    extends: win32more.Storage.FileServerResourceManager.IFsrmQuotaTemplate
    Guid = Guid('9a2bf113-a329-44cc-80-9a-5c-00-fc-e8-da-40')
    @commethod(26)
    def get_OverwriteOnCommit(overwrite: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def put_OverwriteOnCommit(overwrite: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
class IFsrmQuotaTemplateManager(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('4173ac41-172d-4d52-96-3c-fd-c7-e4-15-f7-17')
    @commethod(7)
    def CreateTemplate(quotaTemplate: POINTER(win32more.Storage.FileServerResourceManager.IFsrmQuotaTemplate_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetTemplate(name: win32more.Foundation.BSTR, quotaTemplate: POINTER(win32more.Storage.FileServerResourceManager.IFsrmQuotaTemplate_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def EnumTemplates(options: win32more.Storage.FileServerResourceManager.FsrmEnumOptions, quotaTemplates: POINTER(win32more.Storage.FileServerResourceManager.IFsrmCommittableCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def ExportTemplates(quotaTemplateNamesArray: POINTER(win32more.System.Com.VARIANT_head), serializedQuotaTemplates: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def ImportTemplates(serializedQuotaTemplates: win32more.Foundation.BSTR, quotaTemplateNamesArray: POINTER(win32more.System.Com.VARIANT_head), quotaTemplates: POINTER(win32more.Storage.FileServerResourceManager.IFsrmCommittableCollection_head)) -> win32more.Foundation.HRESULT: ...
class IFsrmReport(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('d8cc81d9-46b8-4fa4-bf-a5-4a-a9-de-c9-b6-38')
    @commethod(7)
    def get_Type(reportType: POINTER(win32more.Storage.FileServerResourceManager.FsrmReportType)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Name(name: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def put_Name(name: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_Description(description: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def put_Description(description: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_LastGeneratedFileNamePrefix(prefix: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetFilter(filter: win32more.Storage.FileServerResourceManager.FsrmReportFilter, filterValue: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def SetFilter(filter: win32more.Storage.FileServerResourceManager.FsrmReportFilter, filterValue: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def Delete() -> win32more.Foundation.HRESULT: ...
class IFsrmReportJob(c_void_p):
    extends: win32more.Storage.FileServerResourceManager.IFsrmObject
    Guid = Guid('38e87280-715c-4c7d-a2-80-ea-16-51-a1-9f-ef')
    @commethod(12)
    def get_Task(taskName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def put_Task(taskName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_NamespaceRoots(namespaceRoots: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def put_NamespaceRoots(namespaceRoots: POINTER(win32more.System.Com.SAFEARRAY_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_Formats(formats: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def put_Formats(formats: POINTER(win32more.System.Com.SAFEARRAY_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def get_MailTo(mailTo: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def put_MailTo(mailTo: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def get_RunningStatus(runningStatus: POINTER(win32more.Storage.FileServerResourceManager.FsrmReportRunningStatus)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def get_LastRun(lastRun: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def get_LastError(lastError: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def get_LastGeneratedInDirectory(path: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def EnumReports(reports: POINTER(win32more.Storage.FileServerResourceManager.IFsrmCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def CreateReport(reportType: win32more.Storage.FileServerResourceManager.FsrmReportType, report: POINTER(win32more.Storage.FileServerResourceManager.IFsrmReport_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def Run(context: win32more.Storage.FileServerResourceManager.FsrmReportGenerationContext) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def WaitForCompletion(waitSeconds: Int32, completed: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def Cancel() -> win32more.Foundation.HRESULT: ...
class IFsrmReportManager(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('27b899fe-6ffa-4481-a1-84-d3-da-ad-e8-a0-2b')
    @commethod(7)
    def EnumReportJobs(options: win32more.Storage.FileServerResourceManager.FsrmEnumOptions, reportJobs: POINTER(win32more.Storage.FileServerResourceManager.IFsrmCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def CreateReportJob(reportJob: POINTER(win32more.Storage.FileServerResourceManager.IFsrmReportJob_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetReportJob(taskName: win32more.Foundation.BSTR, reportJob: POINTER(win32more.Storage.FileServerResourceManager.IFsrmReportJob_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetOutputDirectory(context: win32more.Storage.FileServerResourceManager.FsrmReportGenerationContext, path: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def SetOutputDirectory(context: win32more.Storage.FileServerResourceManager.FsrmReportGenerationContext, path: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def IsFilterValidForReportType(reportType: win32more.Storage.FileServerResourceManager.FsrmReportType, filter: win32more.Storage.FileServerResourceManager.FsrmReportFilter, valid: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetDefaultFilter(reportType: win32more.Storage.FileServerResourceManager.FsrmReportType, filter: win32more.Storage.FileServerResourceManager.FsrmReportFilter, filterValue: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def SetDefaultFilter(reportType: win32more.Storage.FileServerResourceManager.FsrmReportType, filter: win32more.Storage.FileServerResourceManager.FsrmReportFilter, filterValue: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetReportSizeLimit(limit: win32more.Storage.FileServerResourceManager.FsrmReportLimit, limitValue: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def SetReportSizeLimit(limit: win32more.Storage.FileServerResourceManager.FsrmReportLimit, limitValue: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
class IFsrmReportScheduler(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('6879caf9-6617-4484-87-19-71-c3-d8-64-5f-94')
    @commethod(7)
    def VerifyNamespaces(namespacesSafeArray: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def CreateScheduleTask(taskName: win32more.Foundation.BSTR, namespacesSafeArray: POINTER(win32more.System.Com.VARIANT_head), serializedTask: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def ModifyScheduleTask(taskName: win32more.Foundation.BSTR, namespacesSafeArray: POINTER(win32more.System.Com.VARIANT_head), serializedTask: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def DeleteScheduleTask(taskName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class IFsrmRule(c_void_p):
    extends: win32more.Storage.FileServerResourceManager.IFsrmObject
    Guid = Guid('cb0df960-16f5-4495-90-79-3f-93-60-d8-31-df')
    @commethod(12)
    def get_Name(name: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def put_Name(name: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_RuleType(ruleType: POINTER(win32more.Storage.FileServerResourceManager.FsrmRuleType)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_ModuleDefinitionName(moduleDefinitionName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def put_ModuleDefinitionName(moduleDefinitionName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_NamespaceRoots(namespaceRoots: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def put_NamespaceRoots(namespaceRoots: POINTER(win32more.System.Com.SAFEARRAY_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get_RuleFlags(ruleFlags: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def put_RuleFlags(ruleFlags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def get_Parameters(parameters: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def put_Parameters(parameters: POINTER(win32more.System.Com.SAFEARRAY_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def get_LastModified(lastModified: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
class IFsrmSetting(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('f411d4fd-14be-4260-8c-40-03-b7-c9-5e-60-8a')
    @commethod(7)
    def get_SmtpServer(smtpServer: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_SmtpServer(smtpServer: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_MailFrom(mailFrom: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_MailFrom(mailFrom: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_AdminEmail(adminEmail: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def put_AdminEmail(adminEmail: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_DisableCommandLine(disableCommandLine: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def put_DisableCommandLine(disableCommandLine: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_EnableScreeningAudit(enableScreeningAudit: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def put_EnableScreeningAudit(enableScreeningAudit: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def EmailTest(mailTo: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def SetActionRunLimitInterval(actionType: win32more.Storage.FileServerResourceManager.FsrmActionType, delayTimeMinutes: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def GetActionRunLimitInterval(actionType: win32more.Storage.FileServerResourceManager.FsrmActionType, delayTimeMinutes: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class IFsrmStorageModuleDefinition(c_void_p):
    extends: win32more.Storage.FileServerResourceManager.IFsrmPipelineModuleDefinition
    Guid = Guid('15a81350-497d-4aba-80-e9-d4-db-cc-55-21-fe')
    @commethod(31)
    def get_Capabilities(capabilities: POINTER(win32more.Storage.FileServerResourceManager.FsrmStorageModuleCaps)) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def put_Capabilities(capabilities: win32more.Storage.FileServerResourceManager.FsrmStorageModuleCaps) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def get_StorageType(storageType: POINTER(win32more.Storage.FileServerResourceManager.FsrmStorageModuleType)) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def put_StorageType(storageType: win32more.Storage.FileServerResourceManager.FsrmStorageModuleType) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def get_UpdatesFileContent(updatesFileContent: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def put_UpdatesFileContent(updatesFileContent: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
class IFsrmStorageModuleImplementation(c_void_p):
    extends: win32more.Storage.FileServerResourceManager.IFsrmPipelineModuleImplementation
    Guid = Guid('0af4a0da-895a-4e50-87-12-a9-67-24-bc-ec-64')
    @commethod(9)
    def UseDefinitions(propertyDefinitions: win32more.Storage.FileServerResourceManager.IFsrmCollection_head) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def LoadProperties(propertyBag: win32more.Storage.FileServerResourceManager.IFsrmPropertyBag_head) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def SaveProperties(propertyBag: win32more.Storage.FileServerResourceManager.IFsrmPropertyBag_head) -> win32more.Foundation.HRESULT: ...
make_head(_module, 'DIFsrmClassificationEvents')
make_head(_module, 'IFsrmAccessDeniedRemediationClient')
make_head(_module, 'IFsrmAction')
make_head(_module, 'IFsrmActionCommand')
make_head(_module, 'IFsrmActionEmail')
make_head(_module, 'IFsrmActionEmail2')
make_head(_module, 'IFsrmActionEventLog')
make_head(_module, 'IFsrmActionReport')
make_head(_module, 'IFsrmAutoApplyQuota')
make_head(_module, 'IFsrmClassificationManager')
make_head(_module, 'IFsrmClassificationManager2')
make_head(_module, 'IFsrmClassificationRule')
make_head(_module, 'IFsrmClassifierModuleDefinition')
make_head(_module, 'IFsrmClassifierModuleImplementation')
make_head(_module, 'IFsrmCollection')
make_head(_module, 'IFsrmCommittableCollection')
make_head(_module, 'IFsrmDerivedObjectsResult')
make_head(_module, 'IFsrmExportImport')
make_head(_module, 'IFsrmFileCondition')
make_head(_module, 'IFsrmFileConditionProperty')
make_head(_module, 'IFsrmFileGroup')
make_head(_module, 'IFsrmFileGroupImported')
make_head(_module, 'IFsrmFileGroupManager')
make_head(_module, 'IFsrmFileManagementJob')
make_head(_module, 'IFsrmFileManagementJobManager')
make_head(_module, 'IFsrmFileScreen')
make_head(_module, 'IFsrmFileScreenBase')
make_head(_module, 'IFsrmFileScreenException')
make_head(_module, 'IFsrmFileScreenManager')
make_head(_module, 'IFsrmFileScreenTemplate')
make_head(_module, 'IFsrmFileScreenTemplateImported')
make_head(_module, 'IFsrmFileScreenTemplateManager')
make_head(_module, 'IFsrmMutableCollection')
make_head(_module, 'IFsrmObject')
make_head(_module, 'IFsrmPathMapper')
make_head(_module, 'IFsrmPipelineModuleConnector')
make_head(_module, 'IFsrmPipelineModuleDefinition')
make_head(_module, 'IFsrmPipelineModuleImplementation')
make_head(_module, 'IFsrmProperty')
make_head(_module, 'IFsrmPropertyBag')
make_head(_module, 'IFsrmPropertyBag2')
make_head(_module, 'IFsrmPropertyCondition')
make_head(_module, 'IFsrmPropertyDefinition')
make_head(_module, 'IFsrmPropertyDefinition2')
make_head(_module, 'IFsrmPropertyDefinitionValue')
make_head(_module, 'IFsrmQuota')
make_head(_module, 'IFsrmQuotaBase')
make_head(_module, 'IFsrmQuotaManager')
make_head(_module, 'IFsrmQuotaManagerEx')
make_head(_module, 'IFsrmQuotaObject')
make_head(_module, 'IFsrmQuotaTemplate')
make_head(_module, 'IFsrmQuotaTemplateImported')
make_head(_module, 'IFsrmQuotaTemplateManager')
make_head(_module, 'IFsrmReport')
make_head(_module, 'IFsrmReportJob')
make_head(_module, 'IFsrmReportManager')
make_head(_module, 'IFsrmReportScheduler')
make_head(_module, 'IFsrmRule')
make_head(_module, 'IFsrmSetting')
make_head(_module, 'IFsrmStorageModuleDefinition')
make_head(_module, 'IFsrmStorageModuleImplementation')
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
_arch_optional = [
]
