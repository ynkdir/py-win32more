from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.Foundation
import Windows.Win32.Networking.BackgroundIntelligentTransferService
import Windows.Win32.System.Com
import Windows.Win32.System.Variant
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
BG_NOTIFY_JOB_TRANSFERRED: UInt32 = 1
BG_NOTIFY_JOB_ERROR: UInt32 = 2
BG_NOTIFY_DISABLE: UInt32 = 4
BG_NOTIFY_JOB_MODIFICATION: UInt32 = 8
BG_NOTIFY_FILE_TRANSFERRED: UInt32 = 16
BG_NOTIFY_FILE_RANGES_TRANSFERRED: UInt32 = 32
BG_JOB_ENUM_ALL_USERS: UInt32 = 1
BG_COPY_FILE_OWNER: UInt32 = 1
BG_COPY_FILE_GROUP: UInt32 = 2
BG_COPY_FILE_DACL: UInt32 = 4
BG_COPY_FILE_SACL: UInt32 = 8
BG_COPY_FILE_ALL: UInt32 = 15
BG_SSL_ENABLE_CRL_CHECK: UInt32 = 1
BG_SSL_IGNORE_CERT_CN_INVALID: UInt32 = 2
BG_SSL_IGNORE_CERT_DATE_INVALID: UInt32 = 4
BG_SSL_IGNORE_UNKNOWN_CA: UInt32 = 8
BG_SSL_IGNORE_CERT_WRONG_USAGE: UInt32 = 16
BG_HTTP_REDIRECT_POLICY_MASK: UInt32 = 1792
BG_HTTP_REDIRECT_POLICY_ALLOW_SILENT: UInt32 = 0
BG_HTTP_REDIRECT_POLICY_ALLOW_REPORT: UInt32 = 256
BG_HTTP_REDIRECT_POLICY_DISALLOW: UInt32 = 512
BG_HTTP_REDIRECT_POLICY_ALLOW_HTTPS_TO_HTTP: UInt32 = 2048
BG_ENABLE_PEERCACHING_CLIENT: UInt32 = 1
BG_ENABLE_PEERCACHING_SERVER: UInt32 = 2
BG_DISABLE_BRANCH_CACHE: UInt32 = 4
BG_JOB_ENABLE_PEERCACHING_CLIENT: UInt32 = 1
BG_JOB_ENABLE_PEERCACHING_SERVER: UInt32 = 2
BG_JOB_DISABLE_BRANCH_CACHE: UInt32 = 4
BITS_COST_STATE_UNRESTRICTED: UInt32 = 1
BITS_COST_STATE_CAPPED_USAGE_UNKNOWN: UInt32 = 2
BITS_COST_STATE_BELOW_CAP: UInt32 = 4
BITS_COST_STATE_NEAR_CAP: UInt32 = 8
BITS_COST_STATE_OVERCAP_CHARGED: UInt32 = 16
BITS_COST_STATE_OVERCAP_THROTTLED: UInt32 = 32
BITS_COST_STATE_USAGE_BASED: UInt32 = 64
BITS_COST_STATE_ROAMING: UInt32 = 128
BITS_COST_OPTION_IGNORE_CONGESTION: UInt32 = 2147483648
BITS_COST_STATE_RESERVED: UInt32 = 1073741824
QM_NOTIFY_FILE_DONE: UInt32 = 1
QM_NOTIFY_JOB_DONE: UInt32 = 2
QM_NOTIFY_GROUP_DONE: UInt32 = 4
QM_NOTIFY_DISABLE_NOTIFY: UInt32 = 64
QM_NOTIFY_USE_PROGRESSEX: UInt32 = 128
QM_STATUS_FILE_COMPLETE: UInt32 = 1
QM_STATUS_FILE_INCOMPLETE: UInt32 = 2
QM_STATUS_JOB_COMPLETE: UInt32 = 4
QM_STATUS_JOB_INCOMPLETE: UInt32 = 8
QM_STATUS_JOB_ERROR: UInt32 = 16
QM_STATUS_JOB_FOREGROUND: UInt32 = 32
QM_STATUS_GROUP_COMPLETE: UInt32 = 64
QM_STATUS_GROUP_INCOMPLETE: UInt32 = 128
QM_STATUS_GROUP_SUSPENDED: UInt32 = 256
QM_STATUS_GROUP_ERROR: UInt32 = 512
QM_STATUS_GROUP_FOREGROUND: UInt32 = 1024
QM_PROTOCOL_HTTP: UInt32 = 1
QM_PROTOCOL_FTP: UInt32 = 2
QM_PROTOCOL_SMB: UInt32 = 3
QM_PROTOCOL_CUSTOM: UInt32 = 4
QM_PROGRESS_PERCENT_DONE: UInt32 = 1
QM_PROGRESS_TIME_DONE: UInt32 = 2
QM_PROGRESS_SIZE_DONE: UInt32 = 3
QM_E_INVALID_STATE: UInt32 = 2164264961
QM_E_SERVICE_UNAVAILABLE: UInt32 = 2164264962
QM_E_DOWNLOADER_UNAVAILABLE: UInt32 = 2164264963
QM_E_ITEM_NOT_FOUND: UInt32 = 2164264964
BG_E_NOT_FOUND: Int32 = -2145386495
BG_E_INVALID_STATE: Int32 = -2145386494
BG_E_EMPTY: Int32 = -2145386493
BG_E_FILE_NOT_AVAILABLE: Int32 = -2145386492
BG_E_PROTOCOL_NOT_AVAILABLE: Int32 = -2145386491
BG_S_ERROR_CONTEXT_NONE: Int32 = 2097158
BG_E_ERROR_CONTEXT_UNKNOWN: Int32 = -2145386489
BG_E_ERROR_CONTEXT_GENERAL_QUEUE_MANAGER: Int32 = -2145386488
BG_E_ERROR_CONTEXT_LOCAL_FILE: Int32 = -2145386487
BG_E_ERROR_CONTEXT_REMOTE_FILE: Int32 = -2145386486
BG_E_ERROR_CONTEXT_GENERAL_TRANSPORT: Int32 = -2145386485
BG_E_ERROR_CONTEXT_QUEUE_MANAGER_NOTIFICATION: Int32 = -2145386484
BG_E_DESTINATION_LOCKED: Int32 = -2145386483
BG_E_VOLUME_CHANGED: Int32 = -2145386482
BG_E_ERROR_INFORMATION_UNAVAILABLE: Int32 = -2145386481
BG_E_NETWORK_DISCONNECTED: Int32 = -2145386480
BG_E_MISSING_FILE_SIZE: Int32 = -2145386479
BG_E_INSUFFICIENT_HTTP_SUPPORT: Int32 = -2145386478
BG_E_INSUFFICIENT_RANGE_SUPPORT: Int32 = -2145386477
BG_E_REMOTE_NOT_SUPPORTED: Int32 = -2145386476
BG_E_NEW_OWNER_DIFF_MAPPING: Int32 = -2145386475
BG_E_NEW_OWNER_NO_FILE_ACCESS: Int32 = -2145386474
BG_S_PARTIAL_COMPLETE: Int32 = 2097175
BG_E_PROXY_LIST_TOO_LARGE: Int32 = -2145386472
BG_E_PROXY_BYPASS_LIST_TOO_LARGE: Int32 = -2145386471
BG_S_UNABLE_TO_DELETE_FILES: Int32 = 2097178
BG_E_INVALID_SERVER_RESPONSE: Int32 = -2145386469
BG_E_TOO_MANY_FILES: Int32 = -2145386468
BG_E_LOCAL_FILE_CHANGED: Int32 = -2145386467
BG_E_ERROR_CONTEXT_REMOTE_APPLICATION: Int32 = -2145386466
BG_E_SESSION_NOT_FOUND: Int32 = -2145386465
BG_E_TOO_LARGE: Int32 = -2145386464
BG_E_STRING_TOO_LONG: Int32 = -2145386463
BG_E_CLIENT_SERVER_PROTOCOL_MISMATCH: Int32 = -2145386462
BG_E_SERVER_EXECUTE_ENABLE: Int32 = -2145386461
BG_E_NO_PROGRESS: Int32 = -2145386460
BG_E_USERNAME_TOO_LARGE: Int32 = -2145386459
BG_E_PASSWORD_TOO_LARGE: Int32 = -2145386458
BG_E_INVALID_AUTH_TARGET: Int32 = -2145386457
BG_E_INVALID_AUTH_SCHEME: Int32 = -2145386456
BG_E_FILE_NOT_FOUND: Int32 = -2145386455
BG_S_PROXY_CHANGED: Int32 = 2097194
BG_E_INVALID_RANGE: Int32 = -2145386453
BG_E_OVERLAPPING_RANGES: Int32 = -2145386452
BG_E_CONNECT_FAILURE: Int32 = -2145386451
BG_E_CONNECTION_CLOSED: Int32 = -2145386450
BG_E_BLOCKED_BY_POLICY: Int32 = -2145386434
BG_E_INVALID_PROXY_INFO: Int32 = -2145386433
BG_E_INVALID_CREDENTIALS: Int32 = -2145386432
BG_E_INVALID_HASH_ALGORITHM: Int32 = -2145386431
BG_E_RECORD_DELETED: Int32 = -2145386430
BG_E_COMMIT_IN_PROGRESS: Int32 = -2145386429
BG_E_DISCOVERY_IN_PROGRESS: Int32 = -2145386428
BG_E_UPNP_ERROR: Int32 = -2145386427
BG_E_TEST_OPTION_BLOCKED_DOWNLOAD: Int32 = -2145386426
BG_E_PEERCACHING_DISABLED: Int32 = -2145386425
BG_E_BUSYCACHERECORD: Int32 = -2145386424
BG_E_TOO_MANY_JOBS_PER_USER: Int32 = -2145386423
BG_E_TOO_MANY_JOBS_PER_MACHINE: Int32 = -2145386416
BG_E_TOO_MANY_FILES_IN_JOB: Int32 = -2145386415
BG_E_TOO_MANY_RANGES_IN_FILE: Int32 = -2145386414
BG_E_VALIDATION_FAILED: Int32 = -2145386413
BG_E_MAXDOWNLOAD_TIMEOUT: Int32 = -2145386412
BG_S_OVERRIDDEN_BY_POLICY: Int32 = 2097237
BG_E_TOKEN_REQUIRED: Int32 = -2145386410
BG_E_UNKNOWN_PROPERTY_ID: Int32 = -2145386409
BG_E_READ_ONLY_PROPERTY: Int32 = -2145386408
BG_E_BLOCKED_BY_COST_TRANSFER_POLICY: Int32 = -2145386407
BG_E_PROPERTY_SUPPORTED_FOR_DOWNLOAD_JOBS_ONLY: Int32 = -2145386400
BG_E_READ_ONLY_PROPERTY_AFTER_ADDFILE: Int32 = -2145386399
BG_E_READ_ONLY_PROPERTY_AFTER_RESUME: Int32 = -2145386398
BG_E_MAX_DOWNLOAD_SIZE_INVALID_VALUE: Int32 = -2145386397
BG_E_MAX_DOWNLOAD_SIZE_LIMIT_REACHED: Int32 = -2145386396
BG_E_STANDBY_MODE: Int32 = -2145386395
BG_E_USE_STORED_CREDENTIALS_NOT_SUPPORTED: Int32 = -2145386394
BG_E_BLOCKED_BY_BATTERY_POLICY: Int32 = -2145386393
BG_E_BLOCKED_BY_BATTERY_SAVER: Int32 = -2145386392
BG_E_WATCHDOG_TIMEOUT: Int32 = -2145386391
BG_E_APP_PACKAGE_NOT_FOUND: Int32 = -2145386390
BG_E_APP_PACKAGE_SCENARIO_NOT_SUPPORTED: Int32 = -2145386389
BG_E_DATABASE_CORRUPT: Int32 = -2145386388
BG_E_RANDOM_ACCESS_NOT_SUPPORTED: Int32 = -2145386387
BG_E_BLOCKED_BY_BACKGROUND_ACCESS_POLICY: Int32 = -2145386386
BG_E_BLOCKED_BY_GAME_MODE: Int32 = -2145386385
BG_E_BLOCKED_BY_SYSTEM_POLICY: Int32 = -2145386384
BG_E_NOT_SUPPORTED_WITH_CUSTOM_HTTP_METHOD: Int32 = -2145386383
BG_E_UNSUPPORTED_JOB_CONFIGURATION: Int32 = -2145386382
BG_E_REMOTE_FILE_CHANGED: Int32 = -2145386381
BG_E_SERVER_CERT_VALIDATION_INTERFACE_REQUIRED: Int32 = -2145386380
BG_E_READ_ONLY_WHEN_JOB_ACTIVE: Int32 = -2145386379
BG_E_ERROR_CONTEXT_SERVER_CERTIFICATE_CALLBACK: Int32 = -2145386378
BG_E_HTTP_ERROR_100: Int32 = -2145845148
BG_E_HTTP_ERROR_101: Int32 = -2145845147
BG_E_HTTP_ERROR_200: Int32 = -2145845048
BG_E_HTTP_ERROR_201: Int32 = -2145845047
BG_E_HTTP_ERROR_202: Int32 = -2145845046
BG_E_HTTP_ERROR_203: Int32 = -2145845045
BG_E_HTTP_ERROR_204: Int32 = -2145845044
BG_E_HTTP_ERROR_205: Int32 = -2145845043
BG_E_HTTP_ERROR_206: Int32 = -2145845042
BG_E_HTTP_ERROR_300: Int32 = -2145844948
BG_E_HTTP_ERROR_301: Int32 = -2145844947
BG_E_HTTP_ERROR_302: Int32 = -2145844946
BG_E_HTTP_ERROR_303: Int32 = -2145844945
BG_E_HTTP_ERROR_304: Int32 = -2145844944
BG_E_HTTP_ERROR_305: Int32 = -2145844943
BG_E_HTTP_ERROR_307: Int32 = -2145844941
BG_E_HTTP_ERROR_400: Int32 = -2145844848
BG_E_HTTP_ERROR_401: Int32 = -2145844847
BG_E_HTTP_ERROR_402: Int32 = -2145844846
BG_E_HTTP_ERROR_403: Int32 = -2145844845
BG_E_HTTP_ERROR_404: Int32 = -2145844844
BG_E_HTTP_ERROR_405: Int32 = -2145844843
BG_E_HTTP_ERROR_406: Int32 = -2145844842
BG_E_HTTP_ERROR_407: Int32 = -2145844841
BG_E_HTTP_ERROR_408: Int32 = -2145844840
BG_E_HTTP_ERROR_409: Int32 = -2145844839
BG_E_HTTP_ERROR_410: Int32 = -2145844838
BG_E_HTTP_ERROR_411: Int32 = -2145844837
BG_E_HTTP_ERROR_412: Int32 = -2145844836
BG_E_HTTP_ERROR_413: Int32 = -2145844835
BG_E_HTTP_ERROR_414: Int32 = -2145844834
BG_E_HTTP_ERROR_415: Int32 = -2145844833
BG_E_HTTP_ERROR_416: Int32 = -2145844832
BG_E_HTTP_ERROR_417: Int32 = -2145844831
BG_E_HTTP_ERROR_449: Int32 = -2145844799
BG_E_HTTP_ERROR_500: Int32 = -2145844748
BG_E_HTTP_ERROR_501: Int32 = -2145844747
BG_E_HTTP_ERROR_502: Int32 = -2145844746
BG_E_HTTP_ERROR_503: Int32 = -2145844745
BG_E_HTTP_ERROR_504: Int32 = -2145844744
BG_E_HTTP_ERROR_505: Int32 = -2145844743
BITS_MC_JOB_CANCELLED: Int32 = -2145828864
BITS_MC_FILE_DELETION_FAILED: Int32 = -2145828863
BITS_MC_FILE_DELETION_FAILED_MORE: Int32 = -2145828862
BITS_MC_JOB_PROPERTY_CHANGE: Int32 = -2145828861
BITS_MC_JOB_TAKE_OWNERSHIP: Int32 = -2145828860
BITS_MC_JOB_SCAVENGED: Int32 = -2145828859
BITS_MC_JOB_NOTIFICATION_FAILURE: Int32 = -2145828858
BITS_MC_STATE_FILE_CORRUPT: Int32 = -2145828857
BITS_MC_FAILED_TO_START: Int32 = -2145828856
BITS_MC_FATAL_IGD_ERROR: Int32 = -2145828855
BITS_MC_PEERCACHING_PORT: Int32 = -2145828854
BITS_MC_WSD_PORT: Int32 = -2145828853
class AsyncIBackgroundCopyCallback(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('ca29d251-b4bb-4679-a3-d9-ae-80-06-11-9d-54')
    @commethod(3)
    def Begin_JobTransferred(self, pJob: Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Finish_JobTransferred(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Begin_JobError(self, pJob: Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob_head, pError: Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyError_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Finish_JobError(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Begin_JobModification(self, pJob: Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob_head, dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Finish_JobModification(self) -> Windows.Win32.Foundation.HRESULT: ...
class BG_AUTH_CREDENTIALS(EasyCastStructure):
    Target: Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_AUTH_TARGET
    Scheme: Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_AUTH_SCHEME
    Credentials: Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_AUTH_CREDENTIALS_UNION
class BG_AUTH_CREDENTIALS_UNION(EasyCastUnion):
    Basic: Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_BASIC_CREDENTIALS
BG_AUTH_SCHEME = Int32
BG_AUTH_SCHEME_BASIC: BG_AUTH_SCHEME = 1
BG_AUTH_SCHEME_DIGEST: BG_AUTH_SCHEME = 2
BG_AUTH_SCHEME_NTLM: BG_AUTH_SCHEME = 3
BG_AUTH_SCHEME_NEGOTIATE: BG_AUTH_SCHEME = 4
BG_AUTH_SCHEME_PASSPORT: BG_AUTH_SCHEME = 5
BG_AUTH_TARGET = Int32
BG_AUTH_TARGET_SERVER: BG_AUTH_TARGET = 1
BG_AUTH_TARGET_PROXY: BG_AUTH_TARGET = 2
class BG_BASIC_CREDENTIALS(EasyCastStructure):
    UserName: Windows.Win32.Foundation.PWSTR
    Password: Windows.Win32.Foundation.PWSTR
BG_CERT_STORE_LOCATION = Int32
BG_CERT_STORE_LOCATION_CURRENT_USER: BG_CERT_STORE_LOCATION = 0
BG_CERT_STORE_LOCATION_LOCAL_MACHINE: BG_CERT_STORE_LOCATION = 1
BG_CERT_STORE_LOCATION_CURRENT_SERVICE: BG_CERT_STORE_LOCATION = 2
BG_CERT_STORE_LOCATION_SERVICES: BG_CERT_STORE_LOCATION = 3
BG_CERT_STORE_LOCATION_USERS: BG_CERT_STORE_LOCATION = 4
BG_CERT_STORE_LOCATION_CURRENT_USER_GROUP_POLICY: BG_CERT_STORE_LOCATION = 5
BG_CERT_STORE_LOCATION_LOCAL_MACHINE_GROUP_POLICY: BG_CERT_STORE_LOCATION = 6
BG_CERT_STORE_LOCATION_LOCAL_MACHINE_ENTERPRISE: BG_CERT_STORE_LOCATION = 7
BG_ERROR_CONTEXT = Int32
BG_ERROR_CONTEXT_NONE: BG_ERROR_CONTEXT = 0
BG_ERROR_CONTEXT_UNKNOWN: BG_ERROR_CONTEXT = 1
BG_ERROR_CONTEXT_GENERAL_QUEUE_MANAGER: BG_ERROR_CONTEXT = 2
BG_ERROR_CONTEXT_QUEUE_MANAGER_NOTIFICATION: BG_ERROR_CONTEXT = 3
BG_ERROR_CONTEXT_LOCAL_FILE: BG_ERROR_CONTEXT = 4
BG_ERROR_CONTEXT_REMOTE_FILE: BG_ERROR_CONTEXT = 5
BG_ERROR_CONTEXT_GENERAL_TRANSPORT: BG_ERROR_CONTEXT = 6
BG_ERROR_CONTEXT_REMOTE_APPLICATION: BG_ERROR_CONTEXT = 7
BG_ERROR_CONTEXT_SERVER_CERTIFICATE_CALLBACK: BG_ERROR_CONTEXT = 8
class BG_FILE_INFO(EasyCastStructure):
    RemoteName: Windows.Win32.Foundation.PWSTR
    LocalName: Windows.Win32.Foundation.PWSTR
class BG_FILE_PROGRESS(EasyCastStructure):
    BytesTotal: UInt64
    BytesTransferred: UInt64
    Completed: Windows.Win32.Foundation.BOOL
class BG_FILE_RANGE(EasyCastStructure):
    InitialOffset: UInt64
    Length: UInt64
BG_JOB_PRIORITY = Int32
BG_JOB_PRIORITY_FOREGROUND: BG_JOB_PRIORITY = 0
BG_JOB_PRIORITY_HIGH: BG_JOB_PRIORITY = 1
BG_JOB_PRIORITY_NORMAL: BG_JOB_PRIORITY = 2
BG_JOB_PRIORITY_LOW: BG_JOB_PRIORITY = 3
class BG_JOB_PROGRESS(EasyCastStructure):
    BytesTotal: UInt64
    BytesTransferred: UInt64
    FilesTotal: UInt32
    FilesTransferred: UInt32
BG_JOB_PROXY_USAGE = Int32
BG_JOB_PROXY_USAGE_PRECONFIG: BG_JOB_PROXY_USAGE = 0
BG_JOB_PROXY_USAGE_NO_PROXY: BG_JOB_PROXY_USAGE = 1
BG_JOB_PROXY_USAGE_OVERRIDE: BG_JOB_PROXY_USAGE = 2
BG_JOB_PROXY_USAGE_AUTODETECT: BG_JOB_PROXY_USAGE = 3
class BG_JOB_REPLY_PROGRESS(EasyCastStructure):
    BytesTotal: UInt64
    BytesTransferred: UInt64
BG_JOB_STATE = Int32
BG_JOB_STATE_QUEUED: BG_JOB_STATE = 0
BG_JOB_STATE_CONNECTING: BG_JOB_STATE = 1
BG_JOB_STATE_TRANSFERRING: BG_JOB_STATE = 2
BG_JOB_STATE_SUSPENDED: BG_JOB_STATE = 3
BG_JOB_STATE_ERROR: BG_JOB_STATE = 4
BG_JOB_STATE_TRANSIENT_ERROR: BG_JOB_STATE = 5
BG_JOB_STATE_TRANSFERRED: BG_JOB_STATE = 6
BG_JOB_STATE_ACKNOWLEDGED: BG_JOB_STATE = 7
BG_JOB_STATE_CANCELLED: BG_JOB_STATE = 8
class BG_JOB_TIMES(EasyCastStructure):
    CreationTime: Windows.Win32.Foundation.FILETIME
    ModificationTime: Windows.Win32.Foundation.FILETIME
    TransferCompletionTime: Windows.Win32.Foundation.FILETIME
BG_JOB_TYPE = Int32
BG_JOB_TYPE_DOWNLOAD: BG_JOB_TYPE = 0
BG_JOB_TYPE_UPLOAD: BG_JOB_TYPE = 1
BG_JOB_TYPE_UPLOAD_REPLY: BG_JOB_TYPE = 2
BG_TOKEN = UInt32
BG_TOKEN_LOCAL_FILE: BG_TOKEN = 1
BG_TOKEN_NETWORK: BG_TOKEN = 2
BITSExtensionSetupFactory = Guid('efbbab68-7286-4783-94-bf-94-61-d8-b7-e7-e9')
BITS_FILE_PROPERTY_ID = Int32
BITS_FILE_PROPERTY_ID_HTTP_RESPONSE_HEADERS: BITS_FILE_PROPERTY_ID = 1
class BITS_FILE_PROPERTY_VALUE(EasyCastUnion):
    String: Windows.Win32.Foundation.PWSTR
BITS_JOB_PROPERTY_ID = Int32
BITS_JOB_PROPERTY_ID_COST_FLAGS: BITS_JOB_PROPERTY_ID = 1
BITS_JOB_PROPERTY_NOTIFICATION_CLSID: BITS_JOB_PROPERTY_ID = 2
BITS_JOB_PROPERTY_DYNAMIC_CONTENT: BITS_JOB_PROPERTY_ID = 3
BITS_JOB_PROPERTY_HIGH_PERFORMANCE: BITS_JOB_PROPERTY_ID = 4
BITS_JOB_PROPERTY_MAX_DOWNLOAD_SIZE: BITS_JOB_PROPERTY_ID = 5
BITS_JOB_PROPERTY_USE_STORED_CREDENTIALS: BITS_JOB_PROPERTY_ID = 7
BITS_JOB_PROPERTY_MINIMUM_NOTIFICATION_INTERVAL_MS: BITS_JOB_PROPERTY_ID = 9
BITS_JOB_PROPERTY_ON_DEMAND_MODE: BITS_JOB_PROPERTY_ID = 10
class BITS_JOB_PROPERTY_VALUE(EasyCastUnion):
    Dword: UInt32
    ClsID: Guid
    Enable: Windows.Win32.Foundation.BOOL
    Uint64: UInt64
    Target: Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_AUTH_TARGET
BITS_JOB_TRANSFER_POLICY = Int32
BITS_JOB_TRANSFER_POLICY_ALWAYS: BITS_JOB_TRANSFER_POLICY = -2147483393
BITS_JOB_TRANSFER_POLICY_NOT_ROAMING: BITS_JOB_TRANSFER_POLICY = -2147483521
BITS_JOB_TRANSFER_POLICY_NO_SURCHARGE: BITS_JOB_TRANSFER_POLICY = -2147483537
BITS_JOB_TRANSFER_POLICY_STANDARD: BITS_JOB_TRANSFER_POLICY = -2147483545
BITS_JOB_TRANSFER_POLICY_UNRESTRICTED: BITS_JOB_TRANSFER_POLICY = -2147483615
BackgroundCopyManager = Guid('4991d34b-80a1-4291-83-b6-33-28-36-6b-90-97')
BackgroundCopyManager10_1 = Guid('4bd3e4e1-7bd4-4a2b-99-64-49-64-00-de-51-93')
BackgroundCopyManager10_2 = Guid('4575438f-a6c8-4976-b0-fe-2f-26-b8-0d-95-9e')
BackgroundCopyManager10_3 = Guid('5fd42ad5-c04e-4d36-ad-c7-e0-8f-f1-57-37-ad')
BackgroundCopyManager1_5 = Guid('f087771f-d74f-4c1a-bb-8a-e1-6a-ca-91-24-ea')
BackgroundCopyManager2_0 = Guid('6d18ad12-bde3-4393-b3-11-09-9c-34-6e-6d-f9')
BackgroundCopyManager2_5 = Guid('03ca98d6-ff5d-49b8-ab-c6-03-dd-84-12-70-20')
BackgroundCopyManager3_0 = Guid('659cdea7-489e-11d9-a9-cd-00-0d-56-96-52-51')
BackgroundCopyManager4_0 = Guid('bb6df56b-cace-11dc-99-92-00-19-b9-3a-3a-84')
BackgroundCopyManager5_0 = Guid('1ecca34c-e88a-44e3-8d-6a-89-21-bd-e9-e4-52')
BackgroundCopyQMgr = Guid('69ad4aee-51be-439b-a9-2c-86-ae-49-0e-8b-30')
class FILESETINFO(EasyCastStructure):
    bstrRemoteFile: Windows.Win32.Foundation.BSTR
    bstrLocalFile: Windows.Win32.Foundation.BSTR
    dwSizeHint: UInt32
GROUPPROP = Int32
GROUPPROP_PRIORITY: GROUPPROP = 0
GROUPPROP_REMOTEUSERID: GROUPPROP = 1
GROUPPROP_REMOTEUSERPWD: GROUPPROP = 2
GROUPPROP_LOCALUSERID: GROUPPROP = 3
GROUPPROP_LOCALUSERPWD: GROUPPROP = 4
GROUPPROP_PROTOCOLFLAGS: GROUPPROP = 5
GROUPPROP_NOTIFYFLAGS: GROUPPROP = 6
GROUPPROP_NOTIFYCLSID: GROUPPROP = 7
GROUPPROP_PROGRESSSIZE: GROUPPROP = 8
GROUPPROP_PROGRESSPERCENT: GROUPPROP = 9
GROUPPROP_PROGRESSTIME: GROUPPROP = 10
GROUPPROP_DISPLAYNAME: GROUPPROP = 11
GROUPPROP_DESCRIPTION: GROUPPROP = 12
class IBITSExtensionSetup(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('29cfbbf7-09e4-4b97-b0-bc-f2-28-7e-3d-8e-b3')
    @commethod(7)
    def EnableBITSUploads(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def DisableBITSUploads(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetCleanupTaskName(self, pTaskName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetCleanupTask(self, riid: POINTER(Guid), ppUnk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IBITSExtensionSetupFactory(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('d5d2d542-5503-4e64-8b-48-72-ef-91-a3-2e-e1')
    @commethod(7)
    def GetObject(self, Path: Windows.Win32.Foundation.BSTR, ppExtensionSetup: POINTER(Windows.Win32.Networking.BackgroundIntelligentTransferService.IBITSExtensionSetup_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IBackgroundCopyCallback(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('97ea99c7-0186-4ad4-8d-f9-c5-b4-e0-ed-6b-22')
    @commethod(3)
    def JobTransferred(self, pJob: Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def JobError(self, pJob: Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob_head, pError: Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyError_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def JobModification(self, pJob: Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob_head, dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IBackgroundCopyCallback1(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('084f6593-3800-4e08-9b-59-99-fa-59-ad-df-82')
    @commethod(3)
    def OnStatus(self, pGroup: Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyGroup_head, pJob: Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob1_head, dwFileIndex: UInt32, dwStatus: UInt32, dwNumOfRetries: UInt32, dwWin32Result: UInt32, dwTransportResult: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnProgress(self, ProgressType: UInt32, pGroup: Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyGroup_head, pJob: Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob1_head, dwFileIndex: UInt32, dwProgressValue: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnProgressEx(self, ProgressType: UInt32, pGroup: Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyGroup_head, pJob: Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob1_head, dwFileIndex: UInt32, dwProgressValue: UInt32, dwByteArraySize: UInt32, pByte: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
class IBackgroundCopyCallback2(c_void_p):
    extends: Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyCallback
    Guid = Guid('659cdeac-489e-11d9-a9-cd-00-0d-56-96-52-51')
    @commethod(6)
    def FileTransferred(self, pJob: Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob_head, pFile: Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile_head) -> Windows.Win32.Foundation.HRESULT: ...
class IBackgroundCopyCallback3(c_void_p):
    extends: Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyCallback2
    Guid = Guid('98c97bd2-e32b-4ad8-a5-28-95-fd-8b-16-bd-42')
    @commethod(7)
    def FileRangesTransferred(self, job: Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob_head, file: Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile_head, rangeCount: UInt32, ranges: POINTER(Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_FILE_RANGE_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IBackgroundCopyError(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('19c613a0-fcb8-4f28-81-ae-89-7c-3d-07-8f-81')
    @commethod(3)
    def GetError(self, pContext: POINTER(Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_ERROR_CONTEXT), pCode: POINTER(Windows.Win32.Foundation.HRESULT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFile(self, pVal: POINTER(Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetErrorDescription(self, LanguageId: UInt32, pErrorDescription: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetErrorContextDescription(self, LanguageId: UInt32, pContextDescription: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetProtocol(self, pProtocol: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IBackgroundCopyFile(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('01b7bd23-fb88-4a77-84-90-58-91-d3-e4-65-3a')
    @commethod(3)
    def GetRemoteName(self, pVal: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLocalName(self, pVal: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetProgress(self, pVal: POINTER(Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_FILE_PROGRESS_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IBackgroundCopyFile2(c_void_p):
    extends: Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile
    Guid = Guid('83e81b93-0873-474d-8a-8c-f2-01-8b-1a-93-9c')
    @commethod(6)
    def GetFileRanges(self, RangeCount: POINTER(UInt32), Ranges: POINTER(POINTER(Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_FILE_RANGE_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetRemoteName(self, Val: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IBackgroundCopyFile3(c_void_p):
    extends: Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile2
    Guid = Guid('659cdeaa-489e-11d9-a9-cd-00-0d-56-96-52-51')
    @commethod(8)
    def GetTemporaryName(self, pFilename: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetValidationState(self, state: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetValidationState(self, pState: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def IsDownloadedFromPeer(self, pVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IBackgroundCopyFile4(c_void_p):
    extends: Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile3
    Guid = Guid('ef7e0655-7888-4960-b0-e5-73-08-46-e0-34-92')
    @commethod(12)
    def GetPeerDownloadStats(self, pFromOrigin: POINTER(UInt64), pFromPeers: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
class IBackgroundCopyFile5(c_void_p):
    extends: Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile4
    Guid = Guid('85c1657f-dafc-40e8-88-34-df-18-ea-25-71-7e')
    @commethod(13)
    def SetProperty(self, PropertyId: Windows.Win32.Networking.BackgroundIntelligentTransferService.BITS_FILE_PROPERTY_ID, PropertyValue: Windows.Win32.Networking.BackgroundIntelligentTransferService.BITS_FILE_PROPERTY_VALUE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetProperty(self, PropertyId: Windows.Win32.Networking.BackgroundIntelligentTransferService.BITS_FILE_PROPERTY_ID, PropertyValue: POINTER(Windows.Win32.Networking.BackgroundIntelligentTransferService.BITS_FILE_PROPERTY_VALUE_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IBackgroundCopyFile6(c_void_p):
    extends: Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile5
    Guid = Guid('cf6784f7-d677-49fd-93-68-cb-47-ae-e9-d1-ad')
    @commethod(15)
    def UpdateDownloadPosition(self, offset: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def RequestFileRanges(self, rangeCount: UInt32, ranges: POINTER(Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_FILE_RANGE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetFilledFileRanges(self, rangeCount: POINTER(UInt32), ranges: POINTER(POINTER(Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_FILE_RANGE_head))) -> Windows.Win32.Foundation.HRESULT: ...
class IBackgroundCopyGroup(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1ded80a7-53ea-424f-8a-04-17-fe-a9-ad-c4-f5')
    @commethod(3)
    def GetProp(self, propID: Windows.Win32.Networking.BackgroundIntelligentTransferService.GROUPPROP, pvarVal: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetProp(self, propID: Windows.Win32.Networking.BackgroundIntelligentTransferService.GROUPPROP, pvarVal: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetProgress(self, dwFlags: UInt32, pdwProgress: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetStatus(self, pdwStatus: POINTER(UInt32), pdwJobIndex: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetJob(self, jobID: Guid, ppJob: POINTER(Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob1_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SuspendGroup(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ResumeGroup(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def CancelGroup(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Size(self, pdwSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_GroupID(self, pguidGroupID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def CreateJob(self, guidJobID: Guid, ppJob: POINTER(Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob1_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def EnumJobs(self, dwFlags: UInt32, ppEnumJobs: POINTER(Windows.Win32.Networking.BackgroundIntelligentTransferService.IEnumBackgroundCopyJobs1_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SwitchToForeground(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def QueryNewJobInterface(self, iid: POINTER(Guid), pUnk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetNotificationPointer(self, iid: POINTER(Guid), pUnk: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
class IBackgroundCopyJob(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('37668d37-507e-4160-93-16-26-30-6d-15-0b-12')
    @commethod(3)
    def AddFileSet(self, cFileCount: UInt32, pFileSet: POINTER(Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_FILE_INFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddFile(self, RemoteUrl: Windows.Win32.Foundation.PWSTR, LocalName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumFiles(self, pEnum: POINTER(Windows.Win32.Networking.BackgroundIntelligentTransferService.IEnumBackgroundCopyFiles_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Suspend(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Resume(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Cancel(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Complete(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetId(self, pVal: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetType(self, pVal: POINTER(Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_JOB_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetProgress(self, pVal: POINTER(Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_JOB_PROGRESS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetTimes(self, pVal: POINTER(Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_JOB_TIMES_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetState(self, pVal: POINTER(Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_JOB_STATE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetError(self, ppError: POINTER(Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyError_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetOwner(self, pVal: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetDisplayName(self, Val: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetDisplayName(self, pVal: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetDescription(self, Val: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetDescription(self, pVal: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def SetPriority(self, Val: Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_JOB_PRIORITY) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetPriority(self, pVal: POINTER(Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_JOB_PRIORITY)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetNotifyFlags(self, Val: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetNotifyFlags(self, pVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def SetNotifyInterface(self, Val: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetNotifyInterface(self, pVal: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def SetMinimumRetryDelay(self, Seconds: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetMinimumRetryDelay(self, Seconds: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def SetNoProgressTimeout(self, Seconds: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def GetNoProgressTimeout(self, Seconds: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def GetErrorCount(self, Errors: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def SetProxySettings(self, ProxyUsage: Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_JOB_PROXY_USAGE, ProxyList: Windows.Win32.Foundation.PWSTR, ProxyBypassList: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def GetProxySettings(self, pProxyUsage: POINTER(Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_JOB_PROXY_USAGE), pProxyList: POINTER(Windows.Win32.Foundation.PWSTR), pProxyBypassList: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def TakeOwnership(self) -> Windows.Win32.Foundation.HRESULT: ...
class IBackgroundCopyJob1(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('59f5553c-2031-4629-bb-18-26-45-a6-97-09-47')
    @commethod(3)
    def CancelJob(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetProgress(self, dwFlags: UInt32, pdwProgress: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetStatus(self, pdwStatus: POINTER(UInt32), pdwWin32Result: POINTER(UInt32), pdwTransportResult: POINTER(UInt32), pdwNumOfRetries: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AddFiles(self, cFileCount: UInt32, ppFileSet: POINTER(POINTER(Windows.Win32.Networking.BackgroundIntelligentTransferService.FILESETINFO_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetFile(self, cFileIndex: UInt32, pFileInfo: POINTER(Windows.Win32.Networking.BackgroundIntelligentTransferService.FILESETINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetFileCount(self, pdwFileCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SwitchToForeground(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_JobID(self, pguidJobID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IBackgroundCopyJob2(c_void_p):
    extends: Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob
    Guid = Guid('54b50739-686f-45eb-9d-ff-d6-a9-a0-fa-a9-af')
    @commethod(35)
    def SetNotifyCmdLine(self, Program: Windows.Win32.Foundation.PWSTR, Parameters: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def GetNotifyCmdLine(self, pProgram: POINTER(Windows.Win32.Foundation.PWSTR), pParameters: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def GetReplyProgress(self, pProgress: POINTER(Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_JOB_REPLY_PROGRESS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def GetReplyData(self, ppBuffer: POINTER(POINTER(Byte)), pLength: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def SetReplyFileName(self, ReplyFileName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def GetReplyFileName(self, pReplyFileName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def SetCredentials(self, credentials: POINTER(Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_AUTH_CREDENTIALS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def RemoveCredentials(self, Target: Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_AUTH_TARGET, Scheme: Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_AUTH_SCHEME) -> Windows.Win32.Foundation.HRESULT: ...
class IBackgroundCopyJob3(c_void_p):
    extends: Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob2
    Guid = Guid('443c8934-90ff-48ed-bc-de-26-f5-c7-45-00-42')
    @commethod(43)
    def ReplaceRemotePrefix(self, OldPrefix: Windows.Win32.Foundation.PWSTR, NewPrefix: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def AddFileWithRanges(self, RemoteUrl: Windows.Win32.Foundation.PWSTR, LocalName: Windows.Win32.Foundation.PWSTR, RangeCount: UInt32, Ranges: POINTER(Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_FILE_RANGE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def SetFileACLFlags(self, Flags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def GetFileACLFlags(self, Flags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IBackgroundCopyJob4(c_void_p):
    extends: Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob3
    Guid = Guid('659cdeae-489e-11d9-a9-cd-00-0d-56-96-52-51')
    @commethod(47)
    def SetPeerCachingFlags(self, Flags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def GetPeerCachingFlags(self, pFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def GetOwnerIntegrityLevel(self, pLevel: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def GetOwnerElevationState(self, pElevated: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def SetMaximumDownloadTime(self, Timeout: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def GetMaximumDownloadTime(self, pTimeout: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IBackgroundCopyJob5(c_void_p):
    extends: Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob4
    Guid = Guid('e847030c-bbba-4657-af-6d-48-4a-a4-2b-f1-fe')
    @commethod(53)
    def SetProperty(self, PropertyId: Windows.Win32.Networking.BackgroundIntelligentTransferService.BITS_JOB_PROPERTY_ID, PropertyValue: Windows.Win32.Networking.BackgroundIntelligentTransferService.BITS_JOB_PROPERTY_VALUE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def GetProperty(self, PropertyId: Windows.Win32.Networking.BackgroundIntelligentTransferService.BITS_JOB_PROPERTY_ID, PropertyValue: POINTER(Windows.Win32.Networking.BackgroundIntelligentTransferService.BITS_JOB_PROPERTY_VALUE_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IBackgroundCopyJobHttpOptions(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f1bd1079-9f01-4bdc-80-36-f0-9b-70-09-50-66')
    @commethod(3)
    def SetClientCertificateByID(self, StoreLocation: Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_CERT_STORE_LOCATION, StoreName: Windows.Win32.Foundation.PWSTR, pCertHashBlob: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetClientCertificateByName(self, StoreLocation: Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_CERT_STORE_LOCATION, StoreName: Windows.Win32.Foundation.PWSTR, SubjectName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RemoveClientCertificate(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetClientCertificate(self, pStoreLocation: POINTER(Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_CERT_STORE_LOCATION), pStoreName: POINTER(Windows.Win32.Foundation.PWSTR), ppCertHashBlob: POINTER(POINTER(Byte)), pSubjectName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetCustomHeaders(self, RequestHeaders: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetCustomHeaders(self, pRequestHeaders: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetSecurityFlags(self, Flags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetSecurityFlags(self, pFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IBackgroundCopyJobHttpOptions2(c_void_p):
    extends: Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJobHttpOptions
    Guid = Guid('b591a192-a405-4fc3-83-23-4c-5c-54-25-78-fc')
    @commethod(11)
    def SetHttpMethod(self, method: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetHttpMethod(self, method: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IBackgroundCopyJobHttpOptions3(c_void_p):
    extends: Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJobHttpOptions2
    Guid = Guid('8a9263d3-fd4c-4eda-9b-28-30-13-2a-4d-4e-3c')
    @commethod(13)
    def SetServerCertificateValidationInterface(self, certValidationCallback: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def MakeCustomHeadersWriteOnly(self) -> Windows.Win32.Foundation.HRESULT: ...
class IBackgroundCopyManager(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('5ce34c0d-0dc9-4c1f-89-7c-da-a1-b7-8c-ee-7c')
    @commethod(3)
    def CreateJob(self, DisplayName: Windows.Win32.Foundation.PWSTR, Type: Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_JOB_TYPE, pJobId: POINTER(Guid), ppJob: POINTER(Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetJob(self, jobID: POINTER(Guid), ppJob: POINTER(Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumJobs(self, dwFlags: UInt32, ppEnum: POINTER(Windows.Win32.Networking.BackgroundIntelligentTransferService.IEnumBackgroundCopyJobs_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetErrorDescription(self, hResult: Windows.Win32.Foundation.HRESULT, LanguageId: UInt32, pErrorDescription: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IBackgroundCopyQMgr(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('16f41c69-09f5-41d2-8c-d8-3c-08-c4-7b-c8-a8')
    @commethod(3)
    def CreateGroup(self, guidGroupID: Guid, ppGroup: POINTER(Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyGroup_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetGroup(self, groupID: Guid, ppGroup: POINTER(Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyGroup_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumGroups(self, dwFlags: UInt32, ppEnumGroups: POINTER(Windows.Win32.Networking.BackgroundIntelligentTransferService.IEnumBackgroundCopyGroups_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IBackgroundCopyServerCertificateValidationCallback(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('4cec0d02-def7-4158-81-3a-c3-2a-46-94-5f-f7')
    @commethod(3)
    def ValidateServerCertificate(self, job: Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob_head, file: Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile_head, certLength: UInt32, certData: POINTER(Byte), certEncodingType: UInt32, certStoreLength: UInt32, certStoreData: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
class IBitsPeer(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('659cdea2-489e-11d9-a9-cd-00-0d-56-96-52-51')
    @commethod(3)
    def GetPeerName(self, pName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def IsAuthenticated(self, pAuth: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def IsAvailable(self, pOnline: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IBitsPeerCacheAdministration(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('659cdead-489e-11d9-a9-cd-00-0d-56-96-52-51')
    @commethod(3)
    def GetMaximumCacheSize(self, pBytes: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetMaximumCacheSize(self, Bytes: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetMaximumContentAge(self, pSeconds: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetMaximumContentAge(self, Seconds: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetConfigurationFlags(self, pFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetConfigurationFlags(self, Flags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def EnumRecords(self, ppEnum: POINTER(Windows.Win32.Networking.BackgroundIntelligentTransferService.IEnumBitsPeerCacheRecords_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetRecord(self, id: POINTER(Guid), ppRecord: POINTER(Windows.Win32.Networking.BackgroundIntelligentTransferService.IBitsPeerCacheRecord_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def ClearRecords(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def DeleteRecord(self, id: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def DeleteUrl(self, url: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def EnumPeers(self, ppEnum: POINTER(Windows.Win32.Networking.BackgroundIntelligentTransferService.IEnumBitsPeers_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def ClearPeers(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def DiscoverPeers(self) -> Windows.Win32.Foundation.HRESULT: ...
class IBitsPeerCacheRecord(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('659cdeaf-489e-11d9-a9-cd-00-0d-56-96-52-51')
    @commethod(3)
    def GetId(self, pVal: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetOriginUrl(self, pVal: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetFileSize(self, pVal: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetFileModificationTime(self, pVal: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetLastAccessTime(self, pVal: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def IsFileValidated(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetFileRanges(self, pRangeCount: POINTER(UInt32), ppRanges: POINTER(POINTER(Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_FILE_RANGE_head))) -> Windows.Win32.Foundation.HRESULT: ...
class IBitsTokenOptions(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('9a2584c3-f7d2-457a-9a-5e-22-b6-7b-ff-c7-d2')
    @commethod(3)
    def SetHelperTokenFlags(self, UsageFlags: Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_TOKEN) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHelperTokenFlags(self, pFlags: POINTER(Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_TOKEN)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetHelperToken(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ClearHelperToken(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetHelperTokenSid(self, pSid: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumBackgroundCopyFiles(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('ca51e165-c365-424c-8d-41-24-aa-a4-ff-3c-40')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(Windows.Win32.Networking.BackgroundIntelligentTransferService.IEnumBackgroundCopyFiles_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCount(self, puCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumBackgroundCopyGroups(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d993e603-4aa4-47c5-86-65-c2-0d-39-c2-ba-4f')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(Guid), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(Windows.Win32.Networking.BackgroundIntelligentTransferService.IEnumBackgroundCopyGroups_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCount(self, puCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumBackgroundCopyJobs(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1af4f612-3b71-466f-8f-58-7b-6f-73-ac-57-ad')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(Windows.Win32.Networking.BackgroundIntelligentTransferService.IEnumBackgroundCopyJobs_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCount(self, puCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumBackgroundCopyJobs1(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('8baeba9d-8f1c-42c4-b8-2c-09-ae-79-98-0d-25')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(Guid), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(Windows.Win32.Networking.BackgroundIntelligentTransferService.IEnumBackgroundCopyJobs1_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCount(self, puCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumBitsPeerCacheRecords(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('659cdea4-489e-11d9-a9-cd-00-0d-56-96-52-51')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(Windows.Win32.Networking.BackgroundIntelligentTransferService.IBitsPeerCacheRecord_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(Windows.Win32.Networking.BackgroundIntelligentTransferService.IEnumBitsPeerCacheRecords_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCount(self, puCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumBitsPeers(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('659cdea5-489e-11d9-a9-cd-00-0d-56-96-52-51')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(Windows.Win32.Networking.BackgroundIntelligentTransferService.IBitsPeer_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(Windows.Win32.Networking.BackgroundIntelligentTransferService.IEnumBitsPeers_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCount(self, puCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'AsyncIBackgroundCopyCallback')
make_head(_module, 'BG_AUTH_CREDENTIALS')
make_head(_module, 'BG_AUTH_CREDENTIALS_UNION')
make_head(_module, 'BG_BASIC_CREDENTIALS')
make_head(_module, 'BG_FILE_INFO')
make_head(_module, 'BG_FILE_PROGRESS')
make_head(_module, 'BG_FILE_RANGE')
make_head(_module, 'BG_JOB_PROGRESS')
make_head(_module, 'BG_JOB_REPLY_PROGRESS')
make_head(_module, 'BG_JOB_TIMES')
make_head(_module, 'BITS_FILE_PROPERTY_VALUE')
make_head(_module, 'BITS_JOB_PROPERTY_VALUE')
make_head(_module, 'FILESETINFO')
make_head(_module, 'IBITSExtensionSetup')
make_head(_module, 'IBITSExtensionSetupFactory')
make_head(_module, 'IBackgroundCopyCallback')
make_head(_module, 'IBackgroundCopyCallback1')
make_head(_module, 'IBackgroundCopyCallback2')
make_head(_module, 'IBackgroundCopyCallback3')
make_head(_module, 'IBackgroundCopyError')
make_head(_module, 'IBackgroundCopyFile')
make_head(_module, 'IBackgroundCopyFile2')
make_head(_module, 'IBackgroundCopyFile3')
make_head(_module, 'IBackgroundCopyFile4')
make_head(_module, 'IBackgroundCopyFile5')
make_head(_module, 'IBackgroundCopyFile6')
make_head(_module, 'IBackgroundCopyGroup')
make_head(_module, 'IBackgroundCopyJob')
make_head(_module, 'IBackgroundCopyJob1')
make_head(_module, 'IBackgroundCopyJob2')
make_head(_module, 'IBackgroundCopyJob3')
make_head(_module, 'IBackgroundCopyJob4')
make_head(_module, 'IBackgroundCopyJob5')
make_head(_module, 'IBackgroundCopyJobHttpOptions')
make_head(_module, 'IBackgroundCopyJobHttpOptions2')
make_head(_module, 'IBackgroundCopyJobHttpOptions3')
make_head(_module, 'IBackgroundCopyManager')
make_head(_module, 'IBackgroundCopyQMgr')
make_head(_module, 'IBackgroundCopyServerCertificateValidationCallback')
make_head(_module, 'IBitsPeer')
make_head(_module, 'IBitsPeerCacheAdministration')
make_head(_module, 'IBitsPeerCacheRecord')
make_head(_module, 'IBitsTokenOptions')
make_head(_module, 'IEnumBackgroundCopyFiles')
make_head(_module, 'IEnumBackgroundCopyGroups')
make_head(_module, 'IEnumBackgroundCopyJobs')
make_head(_module, 'IEnumBackgroundCopyJobs1')
make_head(_module, 'IEnumBitsPeerCacheRecords')
make_head(_module, 'IEnumBitsPeers')
