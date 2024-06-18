from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Storage.FileServerResourceManager
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Variant
AdSyncTask = Guid('{2ae64751-b728-4d6b-97a0-b2da2e7d2a3b}')
AdrClientDisplayFlags = Int32
AdrClientDisplayFlags_AllowEmailRequests: win32more.Windows.Win32.Storage.FileServerResourceManager.AdrClientDisplayFlags = 1
AdrClientDisplayFlags_ShowDeviceTroubleshooting: win32more.Windows.Win32.Storage.FileServerResourceManager.AdrClientDisplayFlags = 2
AdrClientErrorType = Int32
AdrClientErrorType_Unknown: win32more.Windows.Win32.Storage.FileServerResourceManager.AdrClientErrorType = 0
AdrClientErrorType_AccessDenied: win32more.Windows.Win32.Storage.FileServerResourceManager.AdrClientErrorType = 1
AdrClientErrorType_FileNotFound: win32more.Windows.Win32.Storage.FileServerResourceManager.AdrClientErrorType = 2
AdrClientFlags = Int32
AdrClientFlags_None: win32more.Windows.Win32.Storage.FileServerResourceManager.AdrClientFlags = 0
AdrClientFlags_FailForLocalPaths: win32more.Windows.Win32.Storage.FileServerResourceManager.AdrClientFlags = 1
AdrClientFlags_FailIfNotSupportedByServer: win32more.Windows.Win32.Storage.FileServerResourceManager.AdrClientFlags = 2
AdrClientFlags_FailIfNotDomainJoined: win32more.Windows.Win32.Storage.FileServerResourceManager.AdrClientFlags = 4
AdrEmailFlags = Int32
AdrEmailFlags_PutDataOwnerOnToLine: win32more.Windows.Win32.Storage.FileServerResourceManager.AdrEmailFlags = 1
AdrEmailFlags_PutAdminOnToLine: win32more.Windows.Win32.Storage.FileServerResourceManager.AdrEmailFlags = 2
AdrEmailFlags_IncludeDeviceClaims: win32more.Windows.Win32.Storage.FileServerResourceManager.AdrEmailFlags = 4
AdrEmailFlags_IncludeUserInfo: win32more.Windows.Win32.Storage.FileServerResourceManager.AdrEmailFlags = 8
AdrEmailFlags_GenerateEventLog: win32more.Windows.Win32.Storage.FileServerResourceManager.AdrEmailFlags = 16
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
FSRM_S_PARTIAL_BATCH: win32more.Windows.Win32.Foundation.HRESULT = 283396
FSRM_S_PARTIAL_CLASSIFICATION: win32more.Windows.Win32.Foundation.HRESULT = 283397
FSRM_S_CLASSIFICATION_SCAN_FAILURES: win32more.Windows.Win32.Foundation.HRESULT = 283398
FSRM_E_NOT_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -2147200255
FSRM_E_INVALID_SCHEDULER_ARGUMENT: win32more.Windows.Win32.Foundation.HRESULT = -2147200254
FSRM_E_ALREADY_EXISTS: win32more.Windows.Win32.Foundation.HRESULT = -2147200253
FSRM_E_PATH_NOT_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -2147200252
FSRM_E_INVALID_USER: win32more.Windows.Win32.Foundation.HRESULT = -2147200251
FSRM_E_INVALID_PATH: win32more.Windows.Win32.Foundation.HRESULT = -2147200250
FSRM_E_INVALID_LIMIT: win32more.Windows.Win32.Foundation.HRESULT = -2147200249
FSRM_E_INVALID_NAME: win32more.Windows.Win32.Foundation.HRESULT = -2147200248
FSRM_E_FAIL_BATCH: win32more.Windows.Win32.Foundation.HRESULT = -2147200247
FSRM_E_INVALID_TEXT: win32more.Windows.Win32.Foundation.HRESULT = -2147200246
FSRM_E_INVALID_IMPORT_VERSION: win32more.Windows.Win32.Foundation.HRESULT = -2147200245
FSRM_E_OUT_OF_RANGE: win32more.Windows.Win32.Foundation.HRESULT = -2147200243
FSRM_E_REQD_PARAM_MISSING: win32more.Windows.Win32.Foundation.HRESULT = -2147200242
FSRM_E_INVALID_COMBINATION: win32more.Windows.Win32.Foundation.HRESULT = -2147200241
FSRM_E_DUPLICATE_NAME: win32more.Windows.Win32.Foundation.HRESULT = -2147200240
FSRM_E_NOT_SUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -2147200239
FSRM_E_DRIVER_NOT_READY: win32more.Windows.Win32.Foundation.HRESULT = -2147200237
FSRM_E_INSUFFICIENT_DISK: win32more.Windows.Win32.Foundation.HRESULT = -2147200236
FSRM_E_VOLUME_UNSUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -2147200235
FSRM_E_UNEXPECTED: win32more.Windows.Win32.Foundation.HRESULT = -2147200234
FSRM_E_INSECURE_PATH: win32more.Windows.Win32.Foundation.HRESULT = -2147200233
FSRM_E_INVALID_SMTP_SERVER: win32more.Windows.Win32.Foundation.HRESULT = -2147200232
FSRM_E_AUTO_QUOTA: win32more.Windows.Win32.Foundation.HRESULT = 283419
FSRM_E_EMAIL_NOT_SENT: win32more.Windows.Win32.Foundation.HRESULT = -2147200228
FSRM_E_INVALID_EMAIL_ADDRESS: win32more.Windows.Win32.Foundation.HRESULT = -2147200226
FSRM_E_FILE_SYSTEM_CORRUPT: win32more.Windows.Win32.Foundation.HRESULT = -2147200225
FSRM_E_LONG_CMDLINE: win32more.Windows.Win32.Foundation.HRESULT = -2147200224
FSRM_E_INVALID_FILEGROUP_DEFINITION: win32more.Windows.Win32.Foundation.HRESULT = -2147200223
FSRM_E_INVALID_DATASCREEN_DEFINITION: win32more.Windows.Win32.Foundation.HRESULT = -2147200220
FSRM_E_INVALID_REPORT_FORMAT: win32more.Windows.Win32.Foundation.HRESULT = -2147200216
FSRM_E_INVALID_REPORT_DESC: win32more.Windows.Win32.Foundation.HRESULT = -2147200215
FSRM_E_INVALID_FILENAME: win32more.Windows.Win32.Foundation.HRESULT = -2147200214
FSRM_E_SHADOW_COPY: win32more.Windows.Win32.Foundation.HRESULT = -2147200212
FSRM_E_XML_CORRUPTED: win32more.Windows.Win32.Foundation.HRESULT = -2147200211
FSRM_E_CLUSTER_NOT_RUNNING: win32more.Windows.Win32.Foundation.HRESULT = -2147200210
FSRM_E_STORE_NOT_INSTALLED: win32more.Windows.Win32.Foundation.HRESULT = -2147200209
FSRM_E_NOT_CLUSTER_VOLUME: win32more.Windows.Win32.Foundation.HRESULT = -2147200208
FSRM_E_DIFFERENT_CLUSTER_GROUP: win32more.Windows.Win32.Foundation.HRESULT = -2147200207
FSRM_E_REPORT_TYPE_ALREADY_EXISTS: win32more.Windows.Win32.Foundation.HRESULT = -2147200206
FSRM_E_REPORT_JOB_ALREADY_RUNNING: win32more.Windows.Win32.Foundation.HRESULT = -2147200205
FSRM_E_REPORT_GENERATION_ERR: win32more.Windows.Win32.Foundation.HRESULT = -2147200204
FSRM_E_REPORT_TASK_TRIGGER: win32more.Windows.Win32.Foundation.HRESULT = -2147200203
FSRM_E_LOADING_DISABLED_MODULE: win32more.Windows.Win32.Foundation.HRESULT = -2147200202
FSRM_E_CANNOT_AGGREGATE: win32more.Windows.Win32.Foundation.HRESULT = -2147200201
FSRM_E_MESSAGE_LIMIT_EXCEEDED: win32more.Windows.Win32.Foundation.HRESULT = -2147200200
FSRM_E_OBJECT_IN_USE: win32more.Windows.Win32.Foundation.HRESULT = -2147200199
FSRM_E_CANNOT_RENAME_PROPERTY: win32more.Windows.Win32.Foundation.HRESULT = -2147200198
FSRM_E_CANNOT_CHANGE_PROPERTY_TYPE: win32more.Windows.Win32.Foundation.HRESULT = -2147200197
FSRM_E_MAX_PROPERTY_DEFINITIONS: win32more.Windows.Win32.Foundation.HRESULT = -2147200196
FSRM_E_CLASSIFICATION_ALREADY_RUNNING: win32more.Windows.Win32.Foundation.HRESULT = -2147200195
FSRM_E_CLASSIFICATION_NOT_RUNNING: win32more.Windows.Win32.Foundation.HRESULT = -2147200194
FSRM_E_FILE_MANAGEMENT_JOB_ALREADY_RUNNING: win32more.Windows.Win32.Foundation.HRESULT = -2147200193
FSRM_E_FILE_MANAGEMENT_JOB_EXPIRATION: win32more.Windows.Win32.Foundation.HRESULT = -2147200192
FSRM_E_FILE_MANAGEMENT_JOB_CUSTOM: win32more.Windows.Win32.Foundation.HRESULT = -2147200191
FSRM_E_FILE_MANAGEMENT_JOB_NOTIFICATION: win32more.Windows.Win32.Foundation.HRESULT = -2147200190
FSRM_E_FILE_OPEN_ERROR: win32more.Windows.Win32.Foundation.HRESULT = -2147200189
FSRM_E_UNSECURE_LINK_TO_HOSTED_MODULE: win32more.Windows.Win32.Foundation.HRESULT = -2147200188
FSRM_E_CACHE_INVALID: win32more.Windows.Win32.Foundation.HRESULT = -2147200187
FSRM_E_CACHE_MODULE_ALREADY_EXISTS: win32more.Windows.Win32.Foundation.HRESULT = -2147200186
FSRM_E_FILE_MANAGEMENT_EXPIRATION_DIR_IN_SCOPE: win32more.Windows.Win32.Foundation.HRESULT = -2147200185
FSRM_E_FILE_MANAGEMENT_JOB_ALREADY_EXISTS: win32more.Windows.Win32.Foundation.HRESULT = -2147200184
FSRM_E_PROPERTY_DELETED: win32more.Windows.Win32.Foundation.HRESULT = -2147200183
FSRM_E_LAST_ACCESS_UPDATE_DISABLED: win32more.Windows.Win32.Foundation.HRESULT = -2147200176
FSRM_E_NO_PROPERTY_VALUE: win32more.Windows.Win32.Foundation.HRESULT = -2147200175
FSRM_E_INPROC_MODULE_BLOCKED: win32more.Windows.Win32.Foundation.HRESULT = -2147200174
FSRM_E_ENUM_PROPERTIES_FAILED: win32more.Windows.Win32.Foundation.HRESULT = -2147200173
FSRM_E_SET_PROPERTY_FAILED: win32more.Windows.Win32.Foundation.HRESULT = -2147200172
FSRM_E_CANNOT_STORE_PROPERTIES: win32more.Windows.Win32.Foundation.HRESULT = -2147200171
FSRM_E_CANNOT_ALLOW_REPARSE_POINT_TAG: win32more.Windows.Win32.Foundation.HRESULT = -2147200170
FSRM_E_PARTIAL_CLASSIFICATION_PROPERTY_NOT_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -2147200169
FSRM_E_TEXTREADER_NOT_INITIALIZED: win32more.Windows.Win32.Foundation.HRESULT = -2147200168
FSRM_E_TEXTREADER_IFILTER_NOT_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -2147200167
FSRM_E_PERSIST_PROPERTIES_FAILED_ENCRYPTED: win32more.Windows.Win32.Foundation.HRESULT = -2147200166
FSRM_E_TEXTREADER_IFILTER_CLSID_MALFORMED: win32more.Windows.Win32.Foundation.HRESULT = -2147200160
FSRM_E_TEXTREADER_STREAM_ERROR: win32more.Windows.Win32.Foundation.HRESULT = -2147200159
FSRM_E_TEXTREADER_FILENAME_TOO_LONG: win32more.Windows.Win32.Foundation.HRESULT = -2147200158
FSRM_E_INCOMPATIBLE_FORMAT: win32more.Windows.Win32.Foundation.HRESULT = -2147200157
FSRM_E_FILE_ENCRYPTED: win32more.Windows.Win32.Foundation.HRESULT = -2147200156
FSRM_E_PERSIST_PROPERTIES_FAILED: win32more.Windows.Win32.Foundation.HRESULT = -2147200155
FSRM_E_VOLUME_OFFLINE: win32more.Windows.Win32.Foundation.HRESULT = -2147200154
FSRM_E_FILE_MANAGEMENT_ACTION_TIMEOUT: win32more.Windows.Win32.Foundation.HRESULT = -2147200153
FSRM_E_FILE_MANAGEMENT_ACTION_GET_EXITCODE_FAILED: win32more.Windows.Win32.Foundation.HRESULT = -2147200152
FSRM_E_MODULE_INVALID_PARAM: win32more.Windows.Win32.Foundation.HRESULT = -2147200151
FSRM_E_MODULE_INITIALIZATION: win32more.Windows.Win32.Foundation.HRESULT = -2147200150
FSRM_E_MODULE_SESSION_INITIALIZATION: win32more.Windows.Win32.Foundation.HRESULT = -2147200149
FSRM_E_CLASSIFICATION_SCAN_FAIL: win32more.Windows.Win32.Foundation.HRESULT = -2147200148
FSRM_E_FILE_MANAGEMENT_JOB_NOT_LEGACY_ACCESSIBLE: win32more.Windows.Win32.Foundation.HRESULT = -2147200147
FSRM_E_FILE_MANAGEMENT_JOB_MAX_FILE_CONDITIONS: win32more.Windows.Win32.Foundation.HRESULT = -2147200146
FSRM_E_CANNOT_USE_DEPRECATED_PROPERTY: win32more.Windows.Win32.Foundation.HRESULT = -2147200145
FSRM_E_SYNC_TASK_TIMEOUT: win32more.Windows.Win32.Foundation.HRESULT = -2147200144
FSRM_E_CANNOT_USE_DELETED_PROPERTY: win32more.Windows.Win32.Foundation.HRESULT = -2147200143
FSRM_E_INVALID_AD_CLAIM: win32more.Windows.Win32.Foundation.HRESULT = -2147200142
FSRM_E_CLASSIFICATION_CANCELED: win32more.Windows.Win32.Foundation.HRESULT = -2147200141
FSRM_E_INVALID_FOLDER_PROPERTY_STORE: win32more.Windows.Win32.Foundation.HRESULT = -2147200140
FSRM_E_REBUILDING_FODLER_TYPE_INDEX: win32more.Windows.Win32.Foundation.HRESULT = -2147200139
FSRM_E_PROPERTY_MUST_APPLY_TO_FILES: win32more.Windows.Win32.Foundation.HRESULT = -2147200138
FSRM_E_CLASSIFICATION_TIMEOUT: win32more.Windows.Win32.Foundation.HRESULT = -2147200137
FSRM_E_CLASSIFICATION_PARTIAL_BATCH: win32more.Windows.Win32.Foundation.HRESULT = -2147200136
FSRM_E_CANNOT_DELETE_SYSTEM_PROPERTY: win32more.Windows.Win32.Foundation.HRESULT = -2147200135
FSRM_E_FILE_IN_USE: win32more.Windows.Win32.Foundation.HRESULT = -2147200134
FSRM_E_ERROR_NOT_ENABLED: win32more.Windows.Win32.Foundation.HRESULT = -2147200133
FSRM_E_CANNOT_CREATE_TEMP_COPY: win32more.Windows.Win32.Foundation.HRESULT = -2147200132
FSRM_E_NO_EMAIL_ADDRESS: win32more.Windows.Win32.Foundation.HRESULT = -2147200131
FSRM_E_ADR_MAX_EMAILS_SENT: win32more.Windows.Win32.Foundation.HRESULT = -2147200130
FSRM_E_PATH_NOT_IN_NAMESPACE: win32more.Windows.Win32.Foundation.HRESULT = -2147200129
FSRM_E_RMS_TEMPLATE_NOT_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -2147200128
FSRM_E_SECURE_PROPERTIES_NOT_SUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -2147200127
FSRM_E_RMS_NO_PROTECTORS_INSTALLED: win32more.Windows.Win32.Foundation.HRESULT = -2147200126
FSRM_E_RMS_NO_PROTECTOR_INSTALLED_FOR_FILE: win32more.Windows.Win32.Foundation.HRESULT = -2147200125
FSRM_E_PROPERTY_MUST_APPLY_TO_FOLDERS: win32more.Windows.Win32.Foundation.HRESULT = -2147200124
FSRM_E_PROPERTY_MUST_BE_SECURE: win32more.Windows.Win32.Foundation.HRESULT = -2147200123
FSRM_E_PROPERTY_MUST_BE_GLOBAL: win32more.Windows.Win32.Foundation.HRESULT = -2147200122
FSRM_E_WMI_FAILURE: win32more.Windows.Win32.Foundation.HRESULT = -2147200121
FSRM_E_FILE_MANAGEMENT_JOB_RMS: win32more.Windows.Win32.Foundation.HRESULT = -2147200120
FSRM_E_SYNC_TASK_HAD_ERRORS: win32more.Windows.Win32.Foundation.HRESULT = -2147200119
FSRM_E_ADR_SRV_NOT_SUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -2147200112
FSRM_E_ADR_PATH_IS_LOCAL: win32more.Windows.Win32.Foundation.HRESULT = -2147200111
FSRM_E_ADR_NOT_DOMAIN_JOINED: win32more.Windows.Win32.Foundation.HRESULT = -2147200110
FSRM_E_CANNOT_REMOVE_READONLY: win32more.Windows.Win32.Foundation.HRESULT = -2147200109
FSRM_E_FILE_MANAGEMENT_JOB_INVALID_CONTINUOUS_CONFIG: win32more.Windows.Win32.Foundation.HRESULT = -2147200108
FSRM_E_LEGACY_SCHEDULE: win32more.Windows.Win32.Foundation.HRESULT = -2147200107
FSRM_E_CSC_PATH_NOT_SUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -2147200106
FSRM_E_EXPIRATION_PATH_NOT_WRITEABLE: win32more.Windows.Win32.Foundation.HRESULT = -2147200105
FSRM_E_EXPIRATION_PATH_TOO_LONG: win32more.Windows.Win32.Foundation.HRESULT = -2147200104
FSRM_E_EXPIRATION_VOLUME_NOT_NTFS: win32more.Windows.Win32.Foundation.HRESULT = -2147200103
FSRM_E_FILE_MANAGEMENT_JOB_DEPRECATED: win32more.Windows.Win32.Foundation.HRESULT = -2147200102
FSRM_E_MODULE_TIMEOUT: win32more.Windows.Win32.Foundation.HRESULT = -2147200101
class DIFsrmClassificationEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{26942db0-dabf-41d8-bbdd-b129a9f70424}')
FsrmAccessDeniedRemediationClient = Guid('{100b4fc8-74c1-470f-b1b7-dd7b6bae79bd}')
FsrmAccountType = Int32
FsrmAccountType_Unknown: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmAccountType = 0
FsrmAccountType_NetworkService: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmAccountType = 1
FsrmAccountType_LocalService: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmAccountType = 2
FsrmAccountType_LocalSystem: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmAccountType = 3
FsrmAccountType_InProc: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmAccountType = 4
FsrmAccountType_External: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmAccountType = 5
FsrmAccountType_Automatic: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmAccountType = 500
FsrmActionType = Int32
FsrmActionType_Unknown: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmActionType = 0
FsrmActionType_EventLog: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmActionType = 1
FsrmActionType_Email: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmActionType = 2
FsrmActionType_Command: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmActionType = 3
FsrmActionType_Report: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmActionType = 4
FsrmClassificationLoggingFlags = Int32
FsrmClassificationLoggingFlags_None: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmClassificationLoggingFlags = 0
FsrmClassificationLoggingFlags_ClassificationsInLogFile: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmClassificationLoggingFlags = 1
FsrmClassificationLoggingFlags_ErrorsInLogFile: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmClassificationLoggingFlags = 2
FsrmClassificationLoggingFlags_ClassificationsInSystemLog: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmClassificationLoggingFlags = 4
FsrmClassificationLoggingFlags_ErrorsInSystemLog: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmClassificationLoggingFlags = 8
FsrmClassificationManager = Guid('{b15c0e47-c391-45b9-95c8-eb596c853f3a}')
FsrmCollectionState = Int32
FsrmCollectionState_Fetching: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmCollectionState = 1
FsrmCollectionState_Committing: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmCollectionState = 2
FsrmCollectionState_Complete: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmCollectionState = 3
FsrmCollectionState_Cancelled: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmCollectionState = 4
FsrmCommitOptions = Int32
FsrmCommitOptions_None: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmCommitOptions = 0
FsrmCommitOptions_Asynchronous: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmCommitOptions = 1
FsrmEnumOptions = Int32
FsrmEnumOptions_None: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmEnumOptions = 0
FsrmEnumOptions_Asynchronous: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmEnumOptions = 1
FsrmEnumOptions_CheckRecycleBin: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmEnumOptions = 2
FsrmEnumOptions_IncludeClusterNodes: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmEnumOptions = 4
FsrmEnumOptions_IncludeDeprecatedObjects: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmEnumOptions = 8
FsrmEventType = Int32
FsrmEventType_Unknown: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmEventType = 0
FsrmEventType_Information: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmEventType = 1
FsrmEventType_Warning: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmEventType = 2
FsrmEventType_Error: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmEventType = 3
FsrmExecutionOption = Int32
FsrmExecutionOption_Unknown: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmExecutionOption = 0
FsrmExecutionOption_EvaluateUnset: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmExecutionOption = 1
FsrmExecutionOption_ReEvaluate_ConsiderExistingValue: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmExecutionOption = 2
FsrmExecutionOption_ReEvaluate_IgnoreExistingValue: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmExecutionOption = 3
FsrmExportImport = Guid('{1482dc37-fae9-4787-9025-8ce4e024ab56}')
FsrmFileConditionType = Int32
FsrmFileConditionType_Unknown: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmFileConditionType = 0
FsrmFileConditionType_Property: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmFileConditionType = 1
FsrmFileGroupManager = Guid('{8f1363f6-656f-4496-9226-13aecbd7718f}')
FsrmFileManagementJobManager = Guid('{eb18f9b2-4c3a-4321-b203-205120cff614}')
FsrmFileManagementLoggingFlags = Int32
FsrmFileManagementLoggingFlags_None: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmFileManagementLoggingFlags = 0
FsrmFileManagementLoggingFlags_Error: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmFileManagementLoggingFlags = 1
FsrmFileManagementLoggingFlags_Information: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmFileManagementLoggingFlags = 2
FsrmFileManagementLoggingFlags_Audit: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmFileManagementLoggingFlags = 4
FsrmFileManagementType = Int32
FsrmFileManagementType_Unknown: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmFileManagementType = 0
FsrmFileManagementType_Expiration: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmFileManagementType = 1
FsrmFileManagementType_Custom: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmFileManagementType = 2
FsrmFileManagementType_Rms: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmFileManagementType = 3
FsrmFileScreenFlags = Int32
FsrmFileScreenFlags_Enforce: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmFileScreenFlags = 1
FsrmFileScreenManager = Guid('{95941183-db53-4c5f-b37b-7d0921cf9dc7}')
FsrmFileScreenTemplateManager = Guid('{243111df-e474-46aa-a054-eaa33edc292a}')
FsrmFileStreamingInterfaceType = Int32
FsrmFileStreamingInterfaceType_Unknown: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmFileStreamingInterfaceType = 0
FsrmFileStreamingInterfaceType_ILockBytes: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmFileStreamingInterfaceType = 1
FsrmFileStreamingInterfaceType_IStream: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmFileStreamingInterfaceType = 2
FsrmFileStreamingMode = Int32
FsrmFileStreamingMode_Unknown: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmFileStreamingMode = 0
FsrmFileStreamingMode_Read: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmFileStreamingMode = 1
FsrmFileStreamingMode_Write: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmFileStreamingMode = 2
FsrmFileSystemPropertyId = Int32
FsrmFileSystemPropertyId_Undefined: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmFileSystemPropertyId = 0
FsrmFileSystemPropertyId_FileName: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmFileSystemPropertyId = 1
FsrmFileSystemPropertyId_DateCreated: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmFileSystemPropertyId = 2
FsrmFileSystemPropertyId_DateLastAccessed: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmFileSystemPropertyId = 3
FsrmFileSystemPropertyId_DateLastModified: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmFileSystemPropertyId = 4
FsrmFileSystemPropertyId_DateNow: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmFileSystemPropertyId = 5
FsrmGetFilePropertyOptions = Int32
FsrmGetFilePropertyOptions_None: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmGetFilePropertyOptions = 0
FsrmGetFilePropertyOptions_NoRuleEvaluation: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmGetFilePropertyOptions = 1
FsrmGetFilePropertyOptions_Persistent: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmGetFilePropertyOptions = 2
FsrmGetFilePropertyOptions_FailOnPersistErrors: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmGetFilePropertyOptions = 4
FsrmGetFilePropertyOptions_SkipOrphaned: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmGetFilePropertyOptions = 8
FsrmPathMapper = Guid('{f3be42bd-8ac2-409e-bbd8-faf9b6b41feb}')
FsrmPipelineModuleConnector = Guid('{c7643375-1eb5-44de-a062-623547d933bc}')
FsrmPipelineModuleType = Int32
FsrmPipelineModuleType_Unknown: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPipelineModuleType = 0
FsrmPipelineModuleType_Storage: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPipelineModuleType = 1
FsrmPipelineModuleType_Classifier: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPipelineModuleType = 2
FsrmPropertyBagField = Int32
FsrmPropertyBagField_AccessVolume: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyBagField = 0
FsrmPropertyBagField_VolumeGuidName: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyBagField = 1
FsrmPropertyBagFlags = Int32
FsrmPropertyBagFlags_UpdatedByClassifier: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyBagFlags = 1
FsrmPropertyBagFlags_FailedLoadingProperties: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyBagFlags = 2
FsrmPropertyBagFlags_FailedSavingProperties: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyBagFlags = 4
FsrmPropertyBagFlags_FailedClassifyingProperties: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyBagFlags = 8
FsrmPropertyConditionType = Int32
FsrmPropertyConditionType_Unknown: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyConditionType = 0
FsrmPropertyConditionType_Equal: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyConditionType = 1
FsrmPropertyConditionType_NotEqual: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyConditionType = 2
FsrmPropertyConditionType_GreaterThan: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyConditionType = 3
FsrmPropertyConditionType_LessThan: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyConditionType = 4
FsrmPropertyConditionType_Contain: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyConditionType = 5
FsrmPropertyConditionType_Exist: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyConditionType = 6
FsrmPropertyConditionType_NotExist: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyConditionType = 7
FsrmPropertyConditionType_StartWith: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyConditionType = 8
FsrmPropertyConditionType_EndWith: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyConditionType = 9
FsrmPropertyConditionType_ContainedIn: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyConditionType = 10
FsrmPropertyConditionType_PrefixOf: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyConditionType = 11
FsrmPropertyConditionType_SuffixOf: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyConditionType = 12
FsrmPropertyConditionType_MatchesPattern: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyConditionType = 13
FsrmPropertyDefinitionAppliesTo = Int32
FsrmPropertyDefinitionAppliesTo_Files: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyDefinitionAppliesTo = 1
FsrmPropertyDefinitionAppliesTo_Folders: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyDefinitionAppliesTo = 2
FsrmPropertyDefinitionFlags = Int32
FsrmPropertyDefinitionFlags_Global: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyDefinitionFlags = 1
FsrmPropertyDefinitionFlags_Deprecated: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyDefinitionFlags = 2
FsrmPropertyDefinitionFlags_Secure: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyDefinitionFlags = 4
FsrmPropertyDefinitionType = Int32
FsrmPropertyDefinitionType_Unknown: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyDefinitionType = 0
FsrmPropertyDefinitionType_OrderedList: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyDefinitionType = 1
FsrmPropertyDefinitionType_MultiChoiceList: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyDefinitionType = 2
FsrmPropertyDefinitionType_SingleChoiceList: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyDefinitionType = 3
FsrmPropertyDefinitionType_String: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyDefinitionType = 4
FsrmPropertyDefinitionType_MultiString: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyDefinitionType = 5
FsrmPropertyDefinitionType_Int: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyDefinitionType = 6
FsrmPropertyDefinitionType_Bool: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyDefinitionType = 7
FsrmPropertyDefinitionType_Date: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyDefinitionType = 8
FsrmPropertyFlags = Int32
FsrmPropertyFlags_None: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyFlags = 0
FsrmPropertyFlags_Orphaned: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyFlags = 1
FsrmPropertyFlags_RetrievedFromCache: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyFlags = 2
FsrmPropertyFlags_RetrievedFromStorage: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyFlags = 4
FsrmPropertyFlags_SetByClassifier: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyFlags = 8
FsrmPropertyFlags_Deleted: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyFlags = 16
FsrmPropertyFlags_Reclassified: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyFlags = 32
FsrmPropertyFlags_AggregationFailed: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyFlags = 64
FsrmPropertyFlags_Existing: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyFlags = 128
FsrmPropertyFlags_FailedLoadingProperties: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyFlags = 256
FsrmPropertyFlags_FailedClassifyingProperties: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyFlags = 512
FsrmPropertyFlags_FailedSavingProperties: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyFlags = 1024
FsrmPropertyFlags_Secure: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyFlags = 2048
FsrmPropertyFlags_PolicyDerived: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyFlags = 4096
FsrmPropertyFlags_Inherited: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyFlags = 8192
FsrmPropertyFlags_Manual: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyFlags = 16384
FsrmPropertyFlags_ExplicitValueDeleted: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyFlags = 32768
FsrmPropertyFlags_PropertyDeletedFromClear: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyFlags = 65536
FsrmPropertyFlags_PropertySourceMask: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyFlags = 14
FsrmPropertyFlags_PersistentMask: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyFlags = 20480
FsrmPropertyValueType = Int32
FsrmPropertyValueType_Undefined: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyValueType = 0
FsrmPropertyValueType_Literal: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyValueType = 1
FsrmPropertyValueType_DateOffset: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyValueType = 2
FsrmQuotaFlags = Int32
FsrmQuotaFlags_Enforce: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmQuotaFlags = 256
FsrmQuotaFlags_Disable: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmQuotaFlags = 512
FsrmQuotaFlags_StatusIncomplete: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmQuotaFlags = 65536
FsrmQuotaFlags_StatusRebuilding: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmQuotaFlags = 131072
FsrmQuotaManager = Guid('{90dcab7f-347c-4bfc-b543-540326305fbe}')
FsrmQuotaTemplateManager = Guid('{97d3d443-251c-4337-81e7-b32e8f4ee65e}')
FsrmReportFilter = Int32
FsrmReportFilter_MinSize: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportFilter = 1
FsrmReportFilter_MinAgeDays: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportFilter = 2
FsrmReportFilter_MaxAgeDays: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportFilter = 3
FsrmReportFilter_MinQuotaUsage: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportFilter = 4
FsrmReportFilter_FileGroups: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportFilter = 5
FsrmReportFilter_Owners: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportFilter = 6
FsrmReportFilter_NamePattern: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportFilter = 7
FsrmReportFilter_Property: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportFilter = 8
FsrmReportFormat = Int32
FsrmReportFormat_Unknown: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportFormat = 0
FsrmReportFormat_DHtml: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportFormat = 1
FsrmReportFormat_Html: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportFormat = 2
FsrmReportFormat_Txt: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportFormat = 3
FsrmReportFormat_Csv: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportFormat = 4
FsrmReportFormat_Xml: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportFormat = 5
FsrmReportGenerationContext = Int32
FsrmReportGenerationContext_Undefined: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportGenerationContext = 1
FsrmReportGenerationContext_ScheduledReport: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportGenerationContext = 2
FsrmReportGenerationContext_InteractiveReport: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportGenerationContext = 3
FsrmReportGenerationContext_IncidentReport: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportGenerationContext = 4
FsrmReportLimit = Int32
FsrmReportLimit_MaxFiles: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportLimit = 1
FsrmReportLimit_MaxFileGroups: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportLimit = 2
FsrmReportLimit_MaxOwners: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportLimit = 3
FsrmReportLimit_MaxFilesPerFileGroup: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportLimit = 4
FsrmReportLimit_MaxFilesPerOwner: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportLimit = 5
FsrmReportLimit_MaxFilesPerDuplGroup: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportLimit = 6
FsrmReportLimit_MaxDuplicateGroups: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportLimit = 7
FsrmReportLimit_MaxQuotas: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportLimit = 8
FsrmReportLimit_MaxFileScreenEvents: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportLimit = 9
FsrmReportLimit_MaxPropertyValues: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportLimit = 10
FsrmReportLimit_MaxFilesPerPropertyValue: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportLimit = 11
FsrmReportLimit_MaxFolders: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportLimit = 12
FsrmReportManager = Guid('{0058ef37-aa66-4c48-bd5b-2fce432ab0c8}')
FsrmReportRunningStatus = Int32
FsrmReportRunningStatus_Unknown: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportRunningStatus = 0
FsrmReportRunningStatus_NotRunning: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportRunningStatus = 1
FsrmReportRunningStatus_Queued: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportRunningStatus = 2
FsrmReportRunningStatus_Running: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportRunningStatus = 3
FsrmReportScheduler = Guid('{ea25f1b8-1b8d-4290-8ee8-e17c12c2fe20}')
FsrmReportType = Int32
FsrmReportType_Unknown: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportType = 0
FsrmReportType_LargeFiles: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportType = 1
FsrmReportType_FilesByType: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportType = 2
FsrmReportType_LeastRecentlyAccessed: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportType = 3
FsrmReportType_MostRecentlyAccessed: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportType = 4
FsrmReportType_QuotaUsage: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportType = 5
FsrmReportType_FilesByOwner: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportType = 6
FsrmReportType_ExportReport: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportType = 7
FsrmReportType_DuplicateFiles: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportType = 8
FsrmReportType_FileScreenAudit: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportType = 9
FsrmReportType_FilesByProperty: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportType = 10
FsrmReportType_AutomaticClassification: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportType = 11
FsrmReportType_Expiration: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportType = 12
FsrmReportType_FoldersByProperty: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportType = 13
FsrmRuleFlags = Int32
FsrmRuleFlags_Disabled: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmRuleFlags = 256
FsrmRuleFlags_ClearAutomaticallyClassifiedProperty: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmRuleFlags = 1024
FsrmRuleFlags_ClearManuallyClassifiedProperty: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmRuleFlags = 2048
FsrmRuleFlags_Invalid: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmRuleFlags = 4096
FsrmRuleType = Int32
FsrmRuleType_Unknown: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmRuleType = 0
FsrmRuleType_Classification: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmRuleType = 1
FsrmRuleType_Generic: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmRuleType = 2
FsrmSetting = Guid('{f556d708-6d4d-4594-9c61-7dbb0dae2a46}')
FsrmStorageModuleCaps = Int32
FsrmStorageModuleCaps_Unknown: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmStorageModuleCaps = 0
FsrmStorageModuleCaps_CanGet: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmStorageModuleCaps = 1
FsrmStorageModuleCaps_CanSet: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmStorageModuleCaps = 2
FsrmStorageModuleCaps_CanHandleDirectories: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmStorageModuleCaps = 4
FsrmStorageModuleCaps_CanHandleFiles: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmStorageModuleCaps = 8
FsrmStorageModuleType = Int32
FsrmStorageModuleType_Unknown: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmStorageModuleType = 0
FsrmStorageModuleType_Cache: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmStorageModuleType = 1
FsrmStorageModuleType_InFile: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmStorageModuleType = 2
FsrmStorageModuleType_Database: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmStorageModuleType = 3
FsrmStorageModuleType_System: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmStorageModuleType = 100
FsrmTemplateApplyOptions = Int32
FsrmTemplateApplyOptions_ApplyToDerivedMatching: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmTemplateApplyOptions = 1
FsrmTemplateApplyOptions_ApplyToDerivedAll: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmTemplateApplyOptions = 2
class IFsrmAccessDeniedRemediationClient(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{40002314-590b-45a5-8e1b-8c05da527e52}')
    @commethod(7)
    def Show(self, parentWnd: UIntPtr, accessPath: win32more.Windows.Win32.Foundation.BSTR, errorType: win32more.Windows.Win32.Storage.FileServerResourceManager.AdrClientErrorType, flags: Int32, windowTitle: win32more.Windows.Win32.Foundation.BSTR, windowMessage: win32more.Windows.Win32.Foundation.BSTR, result: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmAction(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{6cd6408a-ae60-463b-9ef1-e117534d69dc}')
    @commethod(7)
    def get_Id(self, id: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_ActionType(self, actionType: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmActionType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_RunLimitInterval(self, minutes: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_RunLimitInterval(self, minutes: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Delete(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmActionCommand(ComPtr):
    extends: win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmAction
    _iid_ = Guid('{12937789-e247-4917-9c20-f3ee9c7ee783}')
    @commethod(12)
    def get_ExecutablePath(self, executablePath: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_ExecutablePath(self, executablePath: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_Arguments(self, arguments: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_Arguments(self, arguments: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_Account(self, account: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmAccountType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_Account(self, account: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmAccountType) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_WorkingDirectory(self, workingDirectory: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def put_WorkingDirectory(self, workingDirectory: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_MonitorCommand(self, monitorCommand: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def put_MonitorCommand(self, monitorCommand: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_KillTimeOut(self, minutes: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_KillTimeOut(self, minutes: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_LogResult(self, logResults: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_LogResult(self, logResults: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmActionEmail(ComPtr):
    extends: win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmAction
    _iid_ = Guid('{d646567d-26ae-4caa-9f84-4e0aad207fca}')
    @commethod(12)
    def get_MailFrom(self, mailFrom: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_MailFrom(self, mailFrom: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_MailReplyTo(self, mailReplyTo: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_MailReplyTo(self, mailReplyTo: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_MailTo(self, mailTo: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_MailTo(self, mailTo: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_MailCc(self, mailCc: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def put_MailCc(self, mailCc: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_MailBcc(self, mailBcc: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def put_MailBcc(self, mailBcc: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_MailSubject(self, mailSubject: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_MailSubject(self, mailSubject: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_MessageText(self, messageText: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_MessageText(self, messageText: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmActionEmail2(ComPtr):
    extends: win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmActionEmail
    _iid_ = Guid('{8276702f-2532-4839-89bf-4872609a2ea4}')
    @commethod(26)
    def get_AttachmentFileListSize(self, attachmentFileListSize: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_AttachmentFileListSize(self, attachmentFileListSize: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmActionEventLog(ComPtr):
    extends: win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmAction
    _iid_ = Guid('{4c8f96c3-5d94-4f37-a4f4-f56ab463546f}')
    @commethod(12)
    def get_EventType(self, eventType: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmEventType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_EventType(self, eventType: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmEventType) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_MessageText(self, messageText: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_MessageText(self, messageText: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmActionReport(ComPtr):
    extends: win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmAction
    _iid_ = Guid('{2dbe63c4-b340-48a0-a5b0-158e07fc567e}')
    @commethod(12)
    def get_ReportTypes(self, reportTypes: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_ReportTypes(self, reportTypes: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_MailTo(self, mailTo: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_MailTo(self, mailTo: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmAutoApplyQuota(ComPtr):
    extends: win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmQuotaObject
    _iid_ = Guid('{f82e5729-6aba-4740-bfc7-c7f58f75fb7b}')
    @commethod(28)
    def get_ExcludeFolders(self, folders: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def put_ExcludeFolders(self, folders: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def CommitAndUpdateDerived(self, commitOptions: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmCommitOptions, applyOptions: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmTemplateApplyOptions, derivedObjectsResult: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmDerivedObjectsResult)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmClassificationManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{d2dc89da-ee91-48a0-85d8-cc72a56f7d04}')
    @commethod(7)
    def get_ClassificationReportFormats(self, formats: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_ClassificationReportFormats(self, formats: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Logging(self, logging: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Logging(self, logging: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_ClassificationReportMailTo(self, mailTo: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_ClassificationReportMailTo(self, mailTo: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_ClassificationReportEnabled(self, reportEnabled: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_ClassificationReportEnabled(self, reportEnabled: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_ClassificationLastReportPathWithoutExtension(self, lastReportPath: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_ClassificationLastError(self, lastError: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_ClassificationRunningStatus(self, runningStatus: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportRunningStatus)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def EnumPropertyDefinitions(self, options: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmEnumOptions, propertyDefinitions: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def CreatePropertyDefinition(self, propertyDefinition: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmPropertyDefinition)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetPropertyDefinition(self, propertyName: win32more.Windows.Win32.Foundation.BSTR, propertyDefinition: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmPropertyDefinition)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def EnumRules(self, ruleType: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmRuleType, options: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmEnumOptions, Rules: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def CreateRule(self, ruleType: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmRuleType, Rule: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmRule)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetRule(self, ruleName: win32more.Windows.Win32.Foundation.BSTR, ruleType: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmRuleType, Rule: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmRule)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def EnumModuleDefinitions(self, moduleType: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPipelineModuleType, options: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmEnumOptions, moduleDefinitions: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def CreateModuleDefinition(self, moduleType: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPipelineModuleType, moduleDefinition: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmPipelineModuleDefinition)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetModuleDefinition(self, moduleName: win32more.Windows.Win32.Foundation.BSTR, moduleType: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPipelineModuleType, moduleDefinition: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmPipelineModuleDefinition)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def RunClassification(self, context: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportGenerationContext, reserved: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def WaitForClassificationCompletion(self, waitSeconds: Int32, completed: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def CancelClassification(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def EnumFileProperties(self, filePath: win32more.Windows.Win32.Foundation.BSTR, options: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmGetFilePropertyOptions, fileProperties: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def GetFileProperty(self, filePath: win32more.Windows.Win32.Foundation.BSTR, propertyName: win32more.Windows.Win32.Foundation.BSTR, options: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmGetFilePropertyOptions, property: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmProperty)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def SetFileProperty(self, filePath: win32more.Windows.Win32.Foundation.BSTR, propertyName: win32more.Windows.Win32.Foundation.BSTR, propertyValue: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def ClearFileProperty(self, filePath: win32more.Windows.Win32.Foundation.BSTR, property: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmClassificationManager2(ComPtr):
    extends: win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmClassificationManager
    _iid_ = Guid('{0004c1c9-127e-4765-ba07-6a3147bca112}')
    @commethod(34)
    def ClassifyFiles(self, filePaths: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY), propertyNames: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY), propertyValues: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY), options: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmGetFilePropertyOptions) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmClassificationRule(ComPtr):
    extends: win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmRule
    _iid_ = Guid('{afc052c2-5315-45ab-841b-c6db0e120148}')
    @commethod(24)
    def get_ExecutionOption(self, executionOption: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmExecutionOption)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_ExecutionOption(self, executionOption: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmExecutionOption) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_PropertyAffected(self, property: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_PropertyAffected(self, property: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_Value(self, value: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def put_Value(self, value: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmClassifierModuleDefinition(ComPtr):
    extends: win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmPipelineModuleDefinition
    _iid_ = Guid('{bb36ea26-6318-4b8c-8592-f72dd602e7a5}')
    @commethod(31)
    def get_PropertiesAffected(self, propertiesAffected: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def put_PropertiesAffected(self, propertiesAffected: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_PropertiesUsed(self, propertiesUsed: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def put_PropertiesUsed(self, propertiesUsed: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def get_NeedsExplicitValue(self, needsExplicitValue: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def put_NeedsExplicitValue(self, needsExplicitValue: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmClassifierModuleImplementation(ComPtr):
    extends: win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmPipelineModuleImplementation
    _iid_ = Guid('{4c968fc6-6edb-4051-9c18-73b7291ae106}')
    @commethod(9)
    def get_LastModified(self, lastModified: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def UseRulesAndDefinitions(self, rules: win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmCollection, propertyDefinitions: win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmCollection) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def OnBeginFile(self, propertyBag: win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmPropertyBag, arrayRuleIds: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def DoesPropertyValueApply(self, property: win32more.Windows.Win32.Foundation.BSTR, value: win32more.Windows.Win32.Foundation.BSTR, applyValue: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL), idRule: Guid, idPropDef: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetPropertyValueToApply(self, property: win32more.Windows.Win32.Foundation.BSTR, value: POINTER(win32more.Windows.Win32.Foundation.BSTR), idRule: Guid, idPropDef: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def OnEndFile(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmCollection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{f76fbf3b-8ddd-4b42-b05a-cb1c3ff1fee8}')
    @commethod(7)
    def get__NewEnum(self, unknown: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, index: Int32, item: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(self, count: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_State(self, state: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmCollectionState)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Cancel(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def WaitForCompletion(self, waitSeconds: Int32, completed: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetById(self, id: Guid, entry: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmCommittableCollection(ComPtr):
    extends: win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmMutableCollection
    _iid_ = Guid('{96deb3b5-8b91-4a2a-9d93-80a35d8aa847}')
    @commethod(18)
    def Commit(self, options: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmCommitOptions, results: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmDerivedObjectsResult(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{39322a2d-38ee-4d0d-8095-421a80849a82}')
    @commethod(7)
    def get_DerivedObjects(self, derivedObjects: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Results(self, results: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmExportImport(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{efcb0ab1-16c4-4a79-812c-725614c3306b}')
    @commethod(7)
    def ExportFileGroups(self, filePath: win32more.Windows.Win32.Foundation.BSTR, fileGroupNamesSafeArray: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), remoteHost: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ImportFileGroups(self, filePath: win32more.Windows.Win32.Foundation.BSTR, fileGroupNamesSafeArray: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), remoteHost: win32more.Windows.Win32.Foundation.BSTR, fileGroups: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmCommittableCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ExportFileScreenTemplates(self, filePath: win32more.Windows.Win32.Foundation.BSTR, templateNamesSafeArray: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), remoteHost: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def ImportFileScreenTemplates(self, filePath: win32more.Windows.Win32.Foundation.BSTR, templateNamesSafeArray: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), remoteHost: win32more.Windows.Win32.Foundation.BSTR, templates: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmCommittableCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def ExportQuotaTemplates(self, filePath: win32more.Windows.Win32.Foundation.BSTR, templateNamesSafeArray: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), remoteHost: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def ImportQuotaTemplates(self, filePath: win32more.Windows.Win32.Foundation.BSTR, templateNamesSafeArray: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), remoteHost: win32more.Windows.Win32.Foundation.BSTR, templates: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmCommittableCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmFileCondition(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{70684ffc-691a-4a1a-b922-97752e138cc1}')
    @commethod(7)
    def get_Type(self, pVal: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmFileConditionType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Delete(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmFileConditionProperty(ComPtr):
    extends: win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmFileCondition
    _iid_ = Guid('{81926775-b981-4479-988f-da171d627360}')
    @commethod(9)
    def get_PropertyName(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_PropertyName(self, newVal: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_PropertyId(self, pVal: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmFileSystemPropertyId)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_PropertyId(self, newVal: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmFileSystemPropertyId) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Operator(self, pVal: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyConditionType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_Operator(self, newVal: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyConditionType) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_ValueType(self, pVal: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyValueType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_ValueType(self, newVal: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyValueType) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_Value(self, pVal: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_Value(self, newVal: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmFileGroup(ComPtr):
    extends: win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmObject
    _iid_ = Guid('{8dd04909-0e34-4d55-afaa-89e1f1a1bbb9}')
    @commethod(12)
    def get_Name(self, name: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_Name(self, name: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_Members(self, members: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmMutableCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_Members(self, members: win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmMutableCollection) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_NonMembers(self, nonMembers: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmMutableCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_NonMembers(self, nonMembers: win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmMutableCollection) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmFileGroupImported(ComPtr):
    extends: win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmFileGroup
    _iid_ = Guid('{ad55f10b-5f11-4be7-94ef-d9ee2e470ded}')
    @commethod(18)
    def get_OverwriteOnCommit(self, overwrite: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def put_OverwriteOnCommit(self, overwrite: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmFileGroupManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{426677d5-018c-485c-8a51-20b86d00bdc4}')
    @commethod(7)
    def CreateFileGroup(self, fileGroup: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmFileGroup)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetFileGroup(self, name: win32more.Windows.Win32.Foundation.BSTR, fileGroup: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmFileGroup)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def EnumFileGroups(self, options: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmEnumOptions, fileGroups: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmCommittableCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def ExportFileGroups(self, fileGroupNamesArray: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), serializedFileGroups: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def ImportFileGroups(self, serializedFileGroups: win32more.Windows.Win32.Foundation.BSTR, fileGroupNamesArray: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), fileGroups: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmCommittableCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmFileManagementJob(ComPtr):
    extends: win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmObject
    _iid_ = Guid('{0770687e-9f36-4d6f-8778-599d188461c9}')
    @commethod(12)
    def get_Name(self, name: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_Name(self, name: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_NamespaceRoots(self, namespaceRoots: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_NamespaceRoots(self, namespaceRoots: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_Enabled(self, enabled: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_Enabled(self, enabled: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_OperationType(self, operationType: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmFileManagementType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def put_OperationType(self, operationType: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmFileManagementType) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_ExpirationDirectory(self, expirationDirectory: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def put_ExpirationDirectory(self, expirationDirectory: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_CustomAction(self, action: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmActionCommand)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_Notifications(self, notifications: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_Logging(self, loggingFlags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_Logging(self, loggingFlags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_ReportEnabled(self, reportEnabled: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_ReportEnabled(self, reportEnabled: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_Formats(self, formats: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def put_Formats(self, formats: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_MailTo(self, mailTo: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def put_MailTo(self, mailTo: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def get_DaysSinceFileCreated(self, daysSinceCreation: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def put_DaysSinceFileCreated(self, daysSinceCreation: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def get_DaysSinceFileLastAccessed(self, daysSinceAccess: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def put_DaysSinceFileLastAccessed(self, daysSinceAccess: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def get_DaysSinceFileLastModified(self, daysSinceModify: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def put_DaysSinceFileLastModified(self, daysSinceModify: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def get_PropertyConditions(self, propertyConditions: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def get_FromDate(self, fromDate: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def put_FromDate(self, fromDate: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def get_Task(self, taskName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def put_Task(self, taskName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def get_Parameters(self, parameters: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def put_Parameters(self, parameters: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def get_RunningStatus(self, runningStatus: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportRunningStatus)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def get_LastError(self, lastError: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def get_LastReportPathWithoutExtension(self, path: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def get_LastRun(self, lastRun: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def get_FileNamePattern(self, fileNamePattern: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def put_FileNamePattern(self, fileNamePattern: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def Run(self, context: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportGenerationContext) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def WaitForCompletion(self, waitSeconds: Int32, completed: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def Cancel(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def AddNotification(self, days: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def DeleteNotification(self, days: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def ModifyNotification(self, days: Int32, newDays: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(57)
    def CreateNotificationAction(self, days: Int32, actionType: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmActionType, action: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmAction)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(58)
    def EnumNotificationActions(self, days: Int32, actions: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(59)
    def CreatePropertyCondition(self, name: win32more.Windows.Win32.Foundation.BSTR, propertyCondition: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmPropertyCondition)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(60)
    def CreateCustomAction(self, customAction: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmActionCommand)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmFileManagementJobManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{ee321ecb-d95e-48e9-907c-c7685a013235}')
    @commethod(7)
    def get_ActionVariables(self, variables: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_ActionVariableDescriptions(self, descriptions: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def EnumFileManagementJobs(self, options: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmEnumOptions, fileManagementJobs: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def CreateFileManagementJob(self, fileManagementJob: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmFileManagementJob)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetFileManagementJob(self, name: win32more.Windows.Win32.Foundation.BSTR, fileManagementJob: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmFileManagementJob)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmFileScreen(ComPtr):
    extends: win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmFileScreenBase
    _iid_ = Guid('{5f6325d3-ce88-4733-84c1-2d6aefc5ea07}')
    @commethod(18)
    def get_Path(self, path: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_SourceTemplateName(self, fileScreenTemplateName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_MatchesSourceTemplate(self, matches: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_UserSid(self, userSid: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_UserAccount(self, userAccount: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def ApplyTemplate(self, fileScreenTemplateName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmFileScreenBase(ComPtr):
    extends: win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmObject
    _iid_ = Guid('{f3637e80-5b22-4a2b-a637-bbb642b41cfc}')
    @commethod(12)
    def get_BlockedFileGroups(self, blockList: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmMutableCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_BlockedFileGroups(self, blockList: win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmMutableCollection) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_FileScreenFlags(self, fileScreenFlags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_FileScreenFlags(self, fileScreenFlags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def CreateAction(self, actionType: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmActionType, action: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmAction)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def EnumActions(self, actions: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmFileScreenException(ComPtr):
    extends: win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmObject
    _iid_ = Guid('{bee7ce02-df77-4515-9389-78f01c5afc1a}')
    @commethod(12)
    def get_Path(self, path: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_AllowedFileGroups(self, allowList: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmMutableCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_AllowedFileGroups(self, allowList: win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmMutableCollection) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmFileScreenManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{ff4fa04e-5a94-4bda-a3a0-d5b4d3c52eba}')
    @commethod(7)
    def get_ActionVariables(self, variables: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_ActionVariableDescriptions(self, descriptions: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def CreateFileScreen(self, path: win32more.Windows.Win32.Foundation.BSTR, fileScreen: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmFileScreen)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetFileScreen(self, path: win32more.Windows.Win32.Foundation.BSTR, fileScreen: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmFileScreen)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def EnumFileScreens(self, path: win32more.Windows.Win32.Foundation.BSTR, options: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmEnumOptions, fileScreens: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmCommittableCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def CreateFileScreenException(self, path: win32more.Windows.Win32.Foundation.BSTR, fileScreenException: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmFileScreenException)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetFileScreenException(self, path: win32more.Windows.Win32.Foundation.BSTR, fileScreenException: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmFileScreenException)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def EnumFileScreenExceptions(self, path: win32more.Windows.Win32.Foundation.BSTR, options: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmEnumOptions, fileScreenExceptions: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmCommittableCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def CreateFileScreenCollection(self, collection: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmCommittableCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmFileScreenTemplate(ComPtr):
    extends: win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmFileScreenBase
    _iid_ = Guid('{205bebf8-dd93-452a-95a6-32b566b35828}')
    @commethod(18)
    def get_Name(self, name: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def put_Name(self, name: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def CopyTemplate(self, fileScreenTemplateName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def CommitAndUpdateDerived(self, commitOptions: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmCommitOptions, applyOptions: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmTemplateApplyOptions, derivedObjectsResult: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmDerivedObjectsResult)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmFileScreenTemplateImported(ComPtr):
    extends: win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmFileScreenTemplate
    _iid_ = Guid('{e1010359-3e5d-4ecd-9fe4-ef48622fdf30}')
    @commethod(22)
    def get_OverwriteOnCommit(self, overwrite: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_OverwriteOnCommit(self, overwrite: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmFileScreenTemplateManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{cfe36cba-1949-4e74-a14f-f1d580ceaf13}')
    @commethod(7)
    def CreateTemplate(self, fileScreenTemplate: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmFileScreenTemplate)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetTemplate(self, name: win32more.Windows.Win32.Foundation.BSTR, fileScreenTemplate: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmFileScreenTemplate)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def EnumTemplates(self, options: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmEnumOptions, fileScreenTemplates: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmCommittableCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def ExportTemplates(self, fileScreenTemplateNamesArray: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), serializedFileScreenTemplates: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def ImportTemplates(self, serializedFileScreenTemplates: win32more.Windows.Win32.Foundation.BSTR, fileScreenTemplateNamesArray: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), fileScreenTemplates: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmCommittableCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmMutableCollection(ComPtr):
    extends: win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmCollection
    _iid_ = Guid('{1bb617b8-3886-49dc-af82-a6c90fa35dda}')
    @commethod(14)
    def Add(self, item: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def Remove(self, index: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def RemoveById(self, id: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def Clone(self, collection: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmMutableCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmObject(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{22bcef93-4a3f-4183-89f9-2f8b8a628aee}')
    @commethod(7)
    def get_Id(self, id: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Description(self, description: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_Description(self, description: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Delete(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Commit(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmPathMapper(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{6f4dbfff-6920-4821-a6c3-b7e94c1fd60c}')
    @commethod(7)
    def GetSharePathsForLocalPath(self, localPath: win32more.Windows.Win32.Foundation.BSTR, sharePaths: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmPipelineModuleConnector(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{c16014f3-9aa1-46b3-b0a7-ab146eb205f2}')
    @commethod(7)
    def get_ModuleImplementation(self, pipelineModuleImplementation: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmPipelineModuleImplementation)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_ModuleName(self, userName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_HostingUserAccount(self, userAccount: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_HostingProcessPid(self, pid: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Bind(self, moduleDefinition: win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmPipelineModuleDefinition, moduleImplementation: win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmPipelineModuleImplementation) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmPipelineModuleDefinition(ComPtr):
    extends: win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmObject
    _iid_ = Guid('{515c1277-2c81-440e-8fcf-367921ed4f59}')
    @commethod(12)
    def get_ModuleClsid(self, moduleClsid: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_ModuleClsid(self, moduleClsid: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_Name(self, name: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_Name(self, name: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_Company(self, company: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_Company(self, company: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_Version(self, version: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def put_Version(self, version: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_ModuleType(self, moduleType: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPipelineModuleType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_Enabled(self, enabled: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_Enabled(self, enabled: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_NeedsFileContent(self, needsFileContent: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_NeedsFileContent(self, needsFileContent: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_Account(self, retrievalAccount: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmAccountType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_Account(self, retrievalAccount: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmAccountType) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_SupportedExtensions(self, supportedExtensions: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def put_SupportedExtensions(self, supportedExtensions: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def get_Parameters(self, parameters: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def put_Parameters(self, parameters: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmPipelineModuleImplementation(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{b7907906-2b02-4cb5-84a9-fdf54613d6cd}')
    @commethod(7)
    def OnLoad(self, moduleDefinition: win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmPipelineModuleDefinition, moduleConnector: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmPipelineModuleConnector)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnUnload(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmProperty(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{4a73fee4-4102-4fcc-9ffb-38614f9ee768}')
    @commethod(7)
    def get_Name(self, name: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Value(self, value: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Sources(self, sources: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_PropertyFlags(self, flags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmPropertyBag(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{774589d1-d300-4f7a-9a24-f7b766800250}')
    @commethod(7)
    def get_Name(self, name: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_RelativePath(self, path: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_VolumeName(self, volumeName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_RelativeNamespaceRoot(self, relativeNamespaceRoot: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_VolumeIndex(self, volumeId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_FileId(self, fileId: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_ParentDirectoryId(self, parentDirectoryId: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_Size(self, size: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_SizeAllocated(self, sizeAllocated: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_CreationTime(self, creationTime: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_LastAccessTime(self, lastAccessTime: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_LastModificationTime(self, lastModificationTime: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_Attributes(self, attributes: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_OwnerSid(self, ownerSid: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_FilePropertyNames(self, filePropertyNames: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_Messages(self, messages: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_PropertyBagFlags(self, flags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetFileProperty(self, name: win32more.Windows.Win32.Foundation.BSTR, fileProperty: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmProperty)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def SetFileProperty(self, name: win32more.Windows.Win32.Foundation.BSTR, value: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def AddMessage(self, message: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def GetFileStreamInterface(self, accessMode: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmFileStreamingMode, interfaceType: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmFileStreamingInterfaceType, pStreamInterface: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmPropertyBag2(ComPtr):
    extends: win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmPropertyBag
    _iid_ = Guid('{0e46bdbd-2402-4fed-9c30-9266e6eb2cc9}')
    @commethod(28)
    def GetFieldValue(self, field: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyBagField, value: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def GetUntrustedInFileProperties(self, props: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmPropertyCondition(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{326af66f-2ac0-4f68-bf8c-4759f054fa29}')
    @commethod(7)
    def get_Name(self, name: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Name(self, name: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Type(self, type: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyConditionType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Type(self, type: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyConditionType) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Value(self, value: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_Value(self, value: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Delete(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmPropertyDefinition(ComPtr):
    extends: win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmObject
    _iid_ = Guid('{ede0150f-e9a3-419c-877c-01fe5d24c5d3}')
    @commethod(12)
    def get_Name(self, name: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_Name(self, name: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_Type(self, type: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyDefinitionType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_Type(self, type: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmPropertyDefinitionType) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_PossibleValues(self, possibleValues: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_PossibleValues(self, possibleValues: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_ValueDescriptions(self, valueDescriptions: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def put_ValueDescriptions(self, valueDescriptions: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_Parameters(self, parameters: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def put_Parameters(self, parameters: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmPropertyDefinition2(ComPtr):
    extends: win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmPropertyDefinition
    _iid_ = Guid('{47782152-d16c-4229-b4e1-0ddfe308b9f6}')
    @commethod(22)
    def get_PropertyDefinitionFlags(self, propertyDefinitionFlags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_DisplayName(self, name: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_DisplayName(self, name: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_AppliesTo(self, appliesTo: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_ValueDefinitions(self, valueDefinitions: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmPropertyDefinitionValue(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{e946d148-bd67-4178-8e22-1c44925ed710}')
    @commethod(7)
    def get_Name(self, name: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_DisplayName(self, displayName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Description(self, description: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_UniqueID(self, uniqueID: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmQuota(ComPtr):
    extends: win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmQuotaObject
    _iid_ = Guid('{377f739d-9647-4b8e-97d2-5ffce6d759cd}')
    @commethod(28)
    def get_QuotaUsed(self, used: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def get_QuotaPeakUsage(self, peakUsage: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_QuotaPeakUsageTime(self, peakUsageDateTime: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def ResetPeakUsage(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def RefreshUsageProperties(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmQuotaBase(ComPtr):
    extends: win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmObject
    _iid_ = Guid('{1568a795-3924-4118-b74b-68d8f0fa5daf}')
    @commethod(12)
    def get_QuotaLimit(self, quotaLimit: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_QuotaLimit(self, quotaLimit: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_QuotaFlags(self, quotaFlags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_QuotaFlags(self, quotaFlags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_Thresholds(self, thresholds: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def AddThreshold(self, threshold: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def DeleteThreshold(self, threshold: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def ModifyThreshold(self, threshold: Int32, newThreshold: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def CreateThresholdAction(self, threshold: Int32, actionType: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmActionType, action: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmAction)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def EnumThresholdActions(self, threshold: Int32, actions: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmQuotaManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{8bb68c7d-19d8-4ffb-809e-be4fc1734014}')
    @commethod(7)
    def get_ActionVariables(self, variables: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_ActionVariableDescriptions(self, descriptions: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def CreateQuota(self, path: win32more.Windows.Win32.Foundation.BSTR, quota: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmQuota)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def CreateAutoApplyQuota(self, quotaTemplateName: win32more.Windows.Win32.Foundation.BSTR, path: win32more.Windows.Win32.Foundation.BSTR, quota: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmAutoApplyQuota)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetQuota(self, path: win32more.Windows.Win32.Foundation.BSTR, quota: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmQuota)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetAutoApplyQuota(self, path: win32more.Windows.Win32.Foundation.BSTR, quota: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmAutoApplyQuota)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetRestrictiveQuota(self, path: win32more.Windows.Win32.Foundation.BSTR, quota: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmQuota)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def EnumQuotas(self, path: win32more.Windows.Win32.Foundation.BSTR, options: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmEnumOptions, quotas: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmCommittableCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def EnumAutoApplyQuotas(self, path: win32more.Windows.Win32.Foundation.BSTR, options: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmEnumOptions, quotas: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmCommittableCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def EnumEffectiveQuotas(self, path: win32more.Windows.Win32.Foundation.BSTR, options: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmEnumOptions, quotas: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmCommittableCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def Scan(self, strPath: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def CreateQuotaCollection(self, collection: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmCommittableCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmQuotaManagerEx(ComPtr):
    extends: win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmQuotaManager
    _iid_ = Guid('{4846cb01-d430-494f-abb4-b1054999fb09}')
    @commethod(19)
    def IsAffectedByQuota(self, path: win32more.Windows.Win32.Foundation.BSTR, options: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmEnumOptions, affected: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmQuotaObject(ComPtr):
    extends: win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmQuotaBase
    _iid_ = Guid('{42dc3511-61d5-48ae-b6dc-59fc00c0a8d6}')
    @commethod(22)
    def get_Path(self, path: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_UserSid(self, userSid: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_UserAccount(self, userAccount: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_SourceTemplateName(self, quotaTemplateName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_MatchesSourceTemplate(self, matches: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def ApplyTemplate(self, quotaTemplateName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmQuotaTemplate(ComPtr):
    extends: win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmQuotaBase
    _iid_ = Guid('{a2efab31-295e-46bb-b976-e86d58b52e8b}')
    @commethod(22)
    def get_Name(self, name: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_Name(self, name: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def CopyTemplate(self, quotaTemplateName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def CommitAndUpdateDerived(self, commitOptions: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmCommitOptions, applyOptions: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmTemplateApplyOptions, derivedObjectsResult: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmDerivedObjectsResult)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmQuotaTemplateImported(ComPtr):
    extends: win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmQuotaTemplate
    _iid_ = Guid('{9a2bf113-a329-44cc-809a-5c00fce8da40}')
    @commethod(26)
    def get_OverwriteOnCommit(self, overwrite: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_OverwriteOnCommit(self, overwrite: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmQuotaTemplateManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{4173ac41-172d-4d52-963c-fdc7e415f717}')
    @commethod(7)
    def CreateTemplate(self, quotaTemplate: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmQuotaTemplate)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetTemplate(self, name: win32more.Windows.Win32.Foundation.BSTR, quotaTemplate: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmQuotaTemplate)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def EnumTemplates(self, options: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmEnumOptions, quotaTemplates: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmCommittableCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def ExportTemplates(self, quotaTemplateNamesArray: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), serializedQuotaTemplates: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def ImportTemplates(self, serializedQuotaTemplates: win32more.Windows.Win32.Foundation.BSTR, quotaTemplateNamesArray: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), quotaTemplates: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmCommittableCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmReport(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{d8cc81d9-46b8-4fa4-bfa5-4aa9dec9b638}')
    @commethod(7)
    def get_Type(self, reportType: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Name(self, name: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_Name(self, name: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Description(self, description: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_Description(self, description: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_LastGeneratedFileNamePrefix(self, prefix: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetFilter(self, filter: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportFilter, filterValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetFilter(self, filter: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportFilter, filterValue: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def Delete(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmReportJob(ComPtr):
    extends: win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmObject
    _iid_ = Guid('{38e87280-715c-4c7d-a280-ea1651a19fef}')
    @commethod(12)
    def get_Task(self, taskName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_Task(self, taskName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_NamespaceRoots(self, namespaceRoots: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_NamespaceRoots(self, namespaceRoots: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_Formats(self, formats: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_Formats(self, formats: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_MailTo(self, mailTo: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def put_MailTo(self, mailTo: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_RunningStatus(self, runningStatus: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportRunningStatus)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_LastRun(self, lastRun: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_LastError(self, lastError: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_LastGeneratedInDirectory(self, path: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def EnumReports(self, reports: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def CreateReport(self, reportType: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportType, report: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmReport)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def Run(self, context: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportGenerationContext) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def WaitForCompletion(self, waitSeconds: Int32, completed: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def Cancel(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmReportManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{27b899fe-6ffa-4481-a184-d3daade8a02b}')
    @commethod(7)
    def EnumReportJobs(self, options: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmEnumOptions, reportJobs: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CreateReportJob(self, reportJob: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmReportJob)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetReportJob(self, taskName: win32more.Windows.Win32.Foundation.BSTR, reportJob: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmReportJob)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetOutputDirectory(self, context: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportGenerationContext, path: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetOutputDirectory(self, context: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportGenerationContext, path: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def IsFilterValidForReportType(self, reportType: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportType, filter: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportFilter, valid: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetDefaultFilter(self, reportType: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportType, filter: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportFilter, filterValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetDefaultFilter(self, reportType: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportType, filter: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportFilter, filterValue: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetReportSizeLimit(self, limit: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportLimit, limitValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetReportSizeLimit(self, limit: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmReportLimit, limitValue: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmReportScheduler(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{6879caf9-6617-4484-8719-71c3d8645f94}')
    @commethod(7)
    def VerifyNamespaces(self, namespacesSafeArray: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CreateScheduleTask(self, taskName: win32more.Windows.Win32.Foundation.BSTR, namespacesSafeArray: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), serializedTask: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ModifyScheduleTask(self, taskName: win32more.Windows.Win32.Foundation.BSTR, namespacesSafeArray: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), serializedTask: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def DeleteScheduleTask(self, taskName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmRule(ComPtr):
    extends: win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmObject
    _iid_ = Guid('{cb0df960-16f5-4495-9079-3f9360d831df}')
    @commethod(12)
    def get_Name(self, name: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_Name(self, name: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_RuleType(self, ruleType: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmRuleType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_ModuleDefinitionName(self, moduleDefinitionName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_ModuleDefinitionName(self, moduleDefinitionName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_NamespaceRoots(self, namespaceRoots: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_NamespaceRoots(self, namespaceRoots: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_RuleFlags(self, ruleFlags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_RuleFlags(self, ruleFlags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_Parameters(self, parameters: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_Parameters(self, parameters: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_LastModified(self, lastModified: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmSetting(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{f411d4fd-14be-4260-8c40-03b7c95e608a}')
    @commethod(7)
    def get_SmtpServer(self, smtpServer: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_SmtpServer(self, smtpServer: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_MailFrom(self, mailFrom: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_MailFrom(self, mailFrom: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_AdminEmail(self, adminEmail: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_AdminEmail(self, adminEmail: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_DisableCommandLine(self, disableCommandLine: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_DisableCommandLine(self, disableCommandLine: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_EnableScreeningAudit(self, enableScreeningAudit: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_EnableScreeningAudit(self, enableScreeningAudit: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def EmailTest(self, mailTo: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetActionRunLimitInterval(self, actionType: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmActionType, delayTimeMinutes: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetActionRunLimitInterval(self, actionType: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmActionType, delayTimeMinutes: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmStorageModuleDefinition(ComPtr):
    extends: win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmPipelineModuleDefinition
    _iid_ = Guid('{15a81350-497d-4aba-80e9-d4dbcc5521fe}')
    @commethod(31)
    def get_Capabilities(self, capabilities: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmStorageModuleCaps)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def put_Capabilities(self, capabilities: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmStorageModuleCaps) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_StorageType(self, storageType: POINTER(win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmStorageModuleType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def put_StorageType(self, storageType: win32more.Windows.Win32.Storage.FileServerResourceManager.FsrmStorageModuleType) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def get_UpdatesFileContent(self, updatesFileContent: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def put_UpdatesFileContent(self, updatesFileContent: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsrmStorageModuleImplementation(ComPtr):
    extends: win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmPipelineModuleImplementation
    _iid_ = Guid('{0af4a0da-895a-4e50-8712-a96724bcec64}')
    @commethod(9)
    def UseDefinitions(self, propertyDefinitions: win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmCollection) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def LoadProperties(self, propertyBag: win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmPropertyBag) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SaveProperties(self, propertyBag: win32more.Windows.Win32.Storage.FileServerResourceManager.IFsrmPropertyBag) -> win32more.Windows.Win32.Foundation.HRESULT: ...


make_ready(__name__)
