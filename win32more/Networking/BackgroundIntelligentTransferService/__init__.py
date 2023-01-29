from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Networking.BackgroundIntelligentTransferService
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
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ca29d251-b4bb-4679-a3-d9-ae-80-06-11-9d-54')
    @commethod(3)
    def Begin_JobTransferred(pJob: win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Finish_JobTransferred() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Begin_JobError(pJob: win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob_head, pError: win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyError_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Finish_JobError() -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def Begin_JobModification(pJob: win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob_head, dwReserved: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Finish_JobModification() -> win32more.Foundation.HRESULT: ...
BackgroundCopyManager = Guid('4991d34b-80a1-4291-83-b6-33-28-36-6b-90-97')
BackgroundCopyManager1_5 = Guid('f087771f-d74f-4c1a-bb-8a-e1-6a-ca-91-24-ea')
BackgroundCopyManager10_1 = Guid('4bd3e4e1-7bd4-4a2b-99-64-49-64-00-de-51-93')
BackgroundCopyManager10_2 = Guid('4575438f-a6c8-4976-b0-fe-2f-26-b8-0d-95-9e')
BackgroundCopyManager10_3 = Guid('5fd42ad5-c04e-4d36-ad-c7-e0-8f-f1-57-37-ad')
BackgroundCopyManager2_0 = Guid('6d18ad12-bde3-4393-b3-11-09-9c-34-6e-6d-f9')
BackgroundCopyManager2_5 = Guid('03ca98d6-ff5d-49b8-ab-c6-03-dd-84-12-70-20')
BackgroundCopyManager3_0 = Guid('659cdea7-489e-11d9-a9-cd-00-0d-56-96-52-51')
BackgroundCopyManager4_0 = Guid('bb6df56b-cace-11dc-99-92-00-19-b9-3a-3a-84')
BackgroundCopyManager5_0 = Guid('1ecca34c-e88a-44e3-8d-6a-89-21-bd-e9-e4-52')
BackgroundCopyQMgr = Guid('69ad4aee-51be-439b-a9-2c-86-ae-49-0e-8b-30')
class BG_AUTH_CREDENTIALS(Structure):
    Target: win32more.Networking.BackgroundIntelligentTransferService.BG_AUTH_TARGET
    Scheme: win32more.Networking.BackgroundIntelligentTransferService.BG_AUTH_SCHEME
    Credentials: win32more.Networking.BackgroundIntelligentTransferService.BG_AUTH_CREDENTIALS_UNION
class BG_AUTH_CREDENTIALS_UNION(Union):
    Basic: win32more.Networking.BackgroundIntelligentTransferService.BG_BASIC_CREDENTIALS
BG_AUTH_SCHEME = Int32
BG_AUTH_SCHEME_BASIC: BG_AUTH_SCHEME = 1
BG_AUTH_SCHEME_DIGEST: BG_AUTH_SCHEME = 2
BG_AUTH_SCHEME_NTLM: BG_AUTH_SCHEME = 3
BG_AUTH_SCHEME_NEGOTIATE: BG_AUTH_SCHEME = 4
BG_AUTH_SCHEME_PASSPORT: BG_AUTH_SCHEME = 5
BG_AUTH_TARGET = Int32
BG_AUTH_TARGET_SERVER: BG_AUTH_TARGET = 1
BG_AUTH_TARGET_PROXY: BG_AUTH_TARGET = 2
class BG_BASIC_CREDENTIALS(Structure):
    UserName: win32more.Foundation.PWSTR
    Password: win32more.Foundation.PWSTR
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
class BG_FILE_INFO(Structure):
    RemoteName: win32more.Foundation.PWSTR
    LocalName: win32more.Foundation.PWSTR
class BG_FILE_PROGRESS(Structure):
    BytesTotal: UInt64
    BytesTransferred: UInt64
    Completed: win32more.Foundation.BOOL
class BG_FILE_RANGE(Structure):
    InitialOffset: UInt64
    Length: UInt64
BG_JOB_PRIORITY = Int32
BG_JOB_PRIORITY_FOREGROUND: BG_JOB_PRIORITY = 0
BG_JOB_PRIORITY_HIGH: BG_JOB_PRIORITY = 1
BG_JOB_PRIORITY_NORMAL: BG_JOB_PRIORITY = 2
BG_JOB_PRIORITY_LOW: BG_JOB_PRIORITY = 3
class BG_JOB_PROGRESS(Structure):
    BytesTotal: UInt64
    BytesTransferred: UInt64
    FilesTotal: UInt32
    FilesTransferred: UInt32
BG_JOB_PROXY_USAGE = Int32
BG_JOB_PROXY_USAGE_PRECONFIG: BG_JOB_PROXY_USAGE = 0
BG_JOB_PROXY_USAGE_NO_PROXY: BG_JOB_PROXY_USAGE = 1
BG_JOB_PROXY_USAGE_OVERRIDE: BG_JOB_PROXY_USAGE = 2
BG_JOB_PROXY_USAGE_AUTODETECT: BG_JOB_PROXY_USAGE = 3
class BG_JOB_REPLY_PROGRESS(Structure):
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
class BG_JOB_TIMES(Structure):
    CreationTime: win32more.Foundation.FILETIME
    ModificationTime: win32more.Foundation.FILETIME
    TransferCompletionTime: win32more.Foundation.FILETIME
BG_JOB_TYPE = Int32
BG_JOB_TYPE_DOWNLOAD: BG_JOB_TYPE = 0
BG_JOB_TYPE_UPLOAD: BG_JOB_TYPE = 1
BG_JOB_TYPE_UPLOAD_REPLY: BG_JOB_TYPE = 2
BG_TOKEN = UInt32
BG_TOKEN_LOCAL_FILE: BG_TOKEN = 1
BG_TOKEN_NETWORK: BG_TOKEN = 2
BITS_FILE_PROPERTY_ID = Int32
BITS_FILE_PROPERTY_ID_HTTP_RESPONSE_HEADERS: BITS_FILE_PROPERTY_ID = 1
class BITS_FILE_PROPERTY_VALUE(Union):
    String: win32more.Foundation.PWSTR
BITS_JOB_PROPERTY_ID = Int32
BITS_JOB_PROPERTY_ID_COST_FLAGS: BITS_JOB_PROPERTY_ID = 1
BITS_JOB_PROPERTY_NOTIFICATION_CLSID: BITS_JOB_PROPERTY_ID = 2
BITS_JOB_PROPERTY_DYNAMIC_CONTENT: BITS_JOB_PROPERTY_ID = 3
BITS_JOB_PROPERTY_HIGH_PERFORMANCE: BITS_JOB_PROPERTY_ID = 4
BITS_JOB_PROPERTY_MAX_DOWNLOAD_SIZE: BITS_JOB_PROPERTY_ID = 5
BITS_JOB_PROPERTY_USE_STORED_CREDENTIALS: BITS_JOB_PROPERTY_ID = 7
BITS_JOB_PROPERTY_MINIMUM_NOTIFICATION_INTERVAL_MS: BITS_JOB_PROPERTY_ID = 9
BITS_JOB_PROPERTY_ON_DEMAND_MODE: BITS_JOB_PROPERTY_ID = 10
class BITS_JOB_PROPERTY_VALUE(Union):
    Dword: UInt32
    ClsID: Guid
    Enable: win32more.Foundation.BOOL
    Uint64: UInt64
    Target: win32more.Networking.BackgroundIntelligentTransferService.BG_AUTH_TARGET
BITS_JOB_TRANSFER_POLICY = Int32
BITS_JOB_TRANSFER_POLICY_ALWAYS: BITS_JOB_TRANSFER_POLICY = -2147483393
BITS_JOB_TRANSFER_POLICY_NOT_ROAMING: BITS_JOB_TRANSFER_POLICY = -2147483521
BITS_JOB_TRANSFER_POLICY_NO_SURCHARGE: BITS_JOB_TRANSFER_POLICY = -2147483537
BITS_JOB_TRANSFER_POLICY_STANDARD: BITS_JOB_TRANSFER_POLICY = -2147483545
BITS_JOB_TRANSFER_POLICY_UNRESTRICTED: BITS_JOB_TRANSFER_POLICY = -2147483615
BITSExtensionSetupFactory = Guid('efbbab68-7286-4783-94-bf-94-61-d8-b7-e7-e9')
class FILESETINFO(Structure):
    bstrRemoteFile: win32more.Foundation.BSTR
    bstrLocalFile: win32more.Foundation.BSTR
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
class IBackgroundCopyCallback(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('97ea99c7-0186-4ad4-8d-f9-c5-b4-e0-ed-6b-22')
    @commethod(3)
    def JobTransferred(pJob: win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def JobError(pJob: win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob_head, pError: win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyError_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def JobModification(pJob: win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob_head, dwReserved: UInt32) -> win32more.Foundation.HRESULT: ...
class IBackgroundCopyCallback1(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('084f6593-3800-4e08-9b-59-99-fa-59-ad-df-82')
    @commethod(3)
    def OnStatus(pGroup: win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyGroup_head, pJob: win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob1_head, dwFileIndex: UInt32, dwStatus: UInt32, dwNumOfRetries: UInt32, dwWin32Result: UInt32, dwTransportResult: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OnProgress(ProgressType: UInt32, pGroup: win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyGroup_head, pJob: win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob1_head, dwFileIndex: UInt32, dwProgressValue: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def OnProgressEx(ProgressType: UInt32, pGroup: win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyGroup_head, pJob: win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob1_head, dwFileIndex: UInt32, dwProgressValue: UInt32, dwByteArraySize: UInt32, pByte: c_char_p_no) -> win32more.Foundation.HRESULT: ...
class IBackgroundCopyCallback2(c_void_p):
    extends: win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyCallback
    Guid = Guid('659cdeac-489e-11d9-a9-cd-00-0d-56-96-52-51')
    @commethod(6)
    def FileTransferred(pJob: win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob_head, pFile: win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile_head) -> win32more.Foundation.HRESULT: ...
class IBackgroundCopyCallback3(c_void_p):
    extends: win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyCallback2
    Guid = Guid('98c97bd2-e32b-4ad8-a5-28-95-fd-8b-16-bd-42')
    @commethod(7)
    def FileRangesTransferred(job: win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob_head, file: win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile_head, rangeCount: UInt32, ranges: POINTER(win32more.Networking.BackgroundIntelligentTransferService.BG_FILE_RANGE_head)) -> win32more.Foundation.HRESULT: ...
class IBackgroundCopyError(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('19c613a0-fcb8-4f28-81-ae-89-7c-3d-07-8f-81')
    @commethod(3)
    def GetError(pContext: POINTER(win32more.Networking.BackgroundIntelligentTransferService.BG_ERROR_CONTEXT), pCode: POINTER(win32more.Foundation.HRESULT)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetFile(pVal: POINTER(win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetErrorDescription(LanguageId: UInt32, pErrorDescription: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetErrorContextDescription(LanguageId: UInt32, pContextDescription: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetProtocol(pProtocol: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
class IBackgroundCopyFile(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('01b7bd23-fb88-4a77-84-90-58-91-d3-e4-65-3a')
    @commethod(3)
    def GetRemoteName(pVal: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLocalName(pVal: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetProgress(pVal: POINTER(win32more.Networking.BackgroundIntelligentTransferService.BG_FILE_PROGRESS_head)) -> win32more.Foundation.HRESULT: ...
class IBackgroundCopyFile2(c_void_p):
    extends: win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile
    Guid = Guid('83e81b93-0873-474d-8a-8c-f2-01-8b-1a-93-9c')
    @commethod(6)
    def GetFileRanges(RangeCount: POINTER(UInt32), Ranges: POINTER(POINTER(win32more.Networking.BackgroundIntelligentTransferService.BG_FILE_RANGE_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetRemoteName(Val: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
class IBackgroundCopyFile3(c_void_p):
    extends: win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile2
    Guid = Guid('659cdeaa-489e-11d9-a9-cd-00-0d-56-96-52-51')
    @commethod(8)
    def GetTemporaryName(pFilename: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetValidationState(state: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetValidationState(pState: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def IsDownloadedFromPeer(pVal: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
class IBackgroundCopyFile4(c_void_p):
    extends: win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile3
    Guid = Guid('ef7e0655-7888-4960-b0-e5-73-08-46-e0-34-92')
    @commethod(12)
    def GetPeerDownloadStats(pFromOrigin: POINTER(UInt64), pFromPeers: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
class IBackgroundCopyFile5(c_void_p):
    extends: win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile4
    Guid = Guid('85c1657f-dafc-40e8-88-34-df-18-ea-25-71-7e')
    @commethod(13)
    def SetProperty(PropertyId: win32more.Networking.BackgroundIntelligentTransferService.BITS_FILE_PROPERTY_ID, PropertyValue: win32more.Networking.BackgroundIntelligentTransferService.BITS_FILE_PROPERTY_VALUE) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetProperty(PropertyId: win32more.Networking.BackgroundIntelligentTransferService.BITS_FILE_PROPERTY_ID, PropertyValue: POINTER(win32more.Networking.BackgroundIntelligentTransferService.BITS_FILE_PROPERTY_VALUE_head)) -> win32more.Foundation.HRESULT: ...
class IBackgroundCopyFile6(c_void_p):
    extends: win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile5
    Guid = Guid('cf6784f7-d677-49fd-93-68-cb-47-ae-e9-d1-ad')
    @commethod(15)
    def UpdateDownloadPosition(offset: UInt64) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def RequestFileRanges(rangeCount: UInt32, ranges: POINTER(win32more.Networking.BackgroundIntelligentTransferService.BG_FILE_RANGE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def GetFilledFileRanges(rangeCount: POINTER(UInt32), ranges: POINTER(POINTER(win32more.Networking.BackgroundIntelligentTransferService.BG_FILE_RANGE_head))) -> win32more.Foundation.HRESULT: ...
class IBackgroundCopyGroup(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('1ded80a7-53ea-424f-8a-04-17-fe-a9-ad-c4-f5')
    @commethod(3)
    def GetProp(propID: win32more.Networking.BackgroundIntelligentTransferService.GROUPPROP, pvarVal: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetProp(propID: win32more.Networking.BackgroundIntelligentTransferService.GROUPPROP, pvarVal: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetProgress(dwFlags: UInt32, pdwProgress: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetStatus(pdwStatus: POINTER(UInt32), pdwJobIndex: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetJob(jobID: Guid, ppJob: POINTER(win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob1_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SuspendGroup() -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def ResumeGroup() -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def CancelGroup() -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_Size(pdwSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_GroupID(pguidGroupID: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def CreateJob(guidJobID: Guid, ppJob: POINTER(win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob1_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def EnumJobs(dwFlags: UInt32, ppEnumJobs: POINTER(win32more.Networking.BackgroundIntelligentTransferService.IEnumBackgroundCopyJobs1_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def SwitchToForeground() -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def QueryNewJobInterface(iid: POINTER(Guid), pUnk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def SetNotificationPointer(iid: POINTER(Guid), pUnk: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
class IBackgroundCopyJob(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('37668d37-507e-4160-93-16-26-30-6d-15-0b-12')
    @commethod(3)
    def AddFileSet(cFileCount: UInt32, pFileSet: POINTER(win32more.Networking.BackgroundIntelligentTransferService.BG_FILE_INFO_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def AddFile(RemoteUrl: win32more.Foundation.PWSTR, LocalName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def EnumFiles(pEnum: POINTER(win32more.Networking.BackgroundIntelligentTransferService.IEnumBackgroundCopyFiles_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Suspend() -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def Resume() -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Cancel() -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def Complete() -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetId(pVal: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetType(pVal: POINTER(win32more.Networking.BackgroundIntelligentTransferService.BG_JOB_TYPE)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetProgress(pVal: POINTER(win32more.Networking.BackgroundIntelligentTransferService.BG_JOB_PROGRESS_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetTimes(pVal: POINTER(win32more.Networking.BackgroundIntelligentTransferService.BG_JOB_TIMES_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetState(pVal: POINTER(win32more.Networking.BackgroundIntelligentTransferService.BG_JOB_STATE)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetError(ppError: POINTER(win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyError_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def GetOwner(pVal: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def SetDisplayName(Val: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def GetDisplayName(pVal: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def SetDescription(Val: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def GetDescription(pVal: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def SetPriority(Val: win32more.Networking.BackgroundIntelligentTransferService.BG_JOB_PRIORITY) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def GetPriority(pVal: POINTER(win32more.Networking.BackgroundIntelligentTransferService.BG_JOB_PRIORITY)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def SetNotifyFlags(Val: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def GetNotifyFlags(pVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def SetNotifyInterface(Val: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def GetNotifyInterface(pVal: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def SetMinimumRetryDelay(Seconds: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def GetMinimumRetryDelay(Seconds: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def SetNoProgressTimeout(Seconds: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def GetNoProgressTimeout(Seconds: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def GetErrorCount(Errors: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def SetProxySettings(ProxyUsage: win32more.Networking.BackgroundIntelligentTransferService.BG_JOB_PROXY_USAGE, ProxyList: win32more.Foundation.PWSTR, ProxyBypassList: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def GetProxySettings(pProxyUsage: POINTER(win32more.Networking.BackgroundIntelligentTransferService.BG_JOB_PROXY_USAGE), pProxyList: POINTER(win32more.Foundation.PWSTR), pProxyBypassList: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def TakeOwnership() -> win32more.Foundation.HRESULT: ...
class IBackgroundCopyJob1(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('59f5553c-2031-4629-bb-18-26-45-a6-97-09-47')
    @commethod(3)
    def CancelJob() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetProgress(dwFlags: UInt32, pdwProgress: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetStatus(pdwStatus: POINTER(UInt32), pdwWin32Result: POINTER(UInt32), pdwTransportResult: POINTER(UInt32), pdwNumOfRetries: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def AddFiles(cFileCount: UInt32, ppFileSet: POINTER(POINTER(win32more.Networking.BackgroundIntelligentTransferService.FILESETINFO_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetFile(cFileIndex: UInt32, pFileInfo: POINTER(win32more.Networking.BackgroundIntelligentTransferService.FILESETINFO_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetFileCount(pdwFileCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SwitchToForeground() -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_JobID(pguidJobID: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
class IBackgroundCopyJob2(c_void_p):
    extends: win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob
    Guid = Guid('54b50739-686f-45eb-9d-ff-d6-a9-a0-fa-a9-af')
    @commethod(35)
    def SetNotifyCmdLine(Program: win32more.Foundation.PWSTR, Parameters: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def GetNotifyCmdLine(pProgram: POINTER(win32more.Foundation.PWSTR), pParameters: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def GetReplyProgress(pProgress: POINTER(win32more.Networking.BackgroundIntelligentTransferService.BG_JOB_REPLY_PROGRESS_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def GetReplyData(ppBuffer: POINTER(c_char_p_no), pLength: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def SetReplyFileName(ReplyFileName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(40)
    def GetReplyFileName(pReplyFileName: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(41)
    def SetCredentials(credentials: POINTER(win32more.Networking.BackgroundIntelligentTransferService.BG_AUTH_CREDENTIALS_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(42)
    def RemoveCredentials(Target: win32more.Networking.BackgroundIntelligentTransferService.BG_AUTH_TARGET, Scheme: win32more.Networking.BackgroundIntelligentTransferService.BG_AUTH_SCHEME) -> win32more.Foundation.HRESULT: ...
class IBackgroundCopyJob3(c_void_p):
    extends: win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob2
    Guid = Guid('443c8934-90ff-48ed-bc-de-26-f5-c7-45-00-42')
    @commethod(43)
    def ReplaceRemotePrefix(OldPrefix: win32more.Foundation.PWSTR, NewPrefix: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(44)
    def AddFileWithRanges(RemoteUrl: win32more.Foundation.PWSTR, LocalName: win32more.Foundation.PWSTR, RangeCount: UInt32, Ranges: POINTER(win32more.Networking.BackgroundIntelligentTransferService.BG_FILE_RANGE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(45)
    def SetFileACLFlags(Flags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(46)
    def GetFileACLFlags(Flags: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IBackgroundCopyJob4(c_void_p):
    extends: win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob3
    Guid = Guid('659cdeae-489e-11d9-a9-cd-00-0d-56-96-52-51')
    @commethod(47)
    def SetPeerCachingFlags(Flags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(48)
    def GetPeerCachingFlags(pFlags: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(49)
    def GetOwnerIntegrityLevel(pLevel: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(50)
    def GetOwnerElevationState(pElevated: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(51)
    def SetMaximumDownloadTime(Timeout: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(52)
    def GetMaximumDownloadTime(pTimeout: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IBackgroundCopyJob5(c_void_p):
    extends: win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob4
    Guid = Guid('e847030c-bbba-4657-af-6d-48-4a-a4-2b-f1-fe')
    @commethod(53)
    def SetProperty(PropertyId: win32more.Networking.BackgroundIntelligentTransferService.BITS_JOB_PROPERTY_ID, PropertyValue: win32more.Networking.BackgroundIntelligentTransferService.BITS_JOB_PROPERTY_VALUE) -> win32more.Foundation.HRESULT: ...
    @commethod(54)
    def GetProperty(PropertyId: win32more.Networking.BackgroundIntelligentTransferService.BITS_JOB_PROPERTY_ID, PropertyValue: POINTER(win32more.Networking.BackgroundIntelligentTransferService.BITS_JOB_PROPERTY_VALUE_head)) -> win32more.Foundation.HRESULT: ...
class IBackgroundCopyJobHttpOptions(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('f1bd1079-9f01-4bdc-80-36-f0-9b-70-09-50-66')
    @commethod(3)
    def SetClientCertificateByID(StoreLocation: win32more.Networking.BackgroundIntelligentTransferService.BG_CERT_STORE_LOCATION, StoreName: win32more.Foundation.PWSTR, pCertHashBlob: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetClientCertificateByName(StoreLocation: win32more.Networking.BackgroundIntelligentTransferService.BG_CERT_STORE_LOCATION, StoreName: win32more.Foundation.PWSTR, SubjectName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def RemoveClientCertificate() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetClientCertificate(pStoreLocation: POINTER(win32more.Networking.BackgroundIntelligentTransferService.BG_CERT_STORE_LOCATION), pStoreName: POINTER(win32more.Foundation.PWSTR), ppCertHashBlob: POINTER(c_char_p_no), pSubjectName: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetCustomHeaders(RequestHeaders: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetCustomHeaders(pRequestHeaders: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetSecurityFlags(Flags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetSecurityFlags(pFlags: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IBackgroundCopyJobHttpOptions2(c_void_p):
    extends: win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJobHttpOptions
    Guid = Guid('b591a192-a405-4fc3-83-23-4c-5c-54-25-78-fc')
    @commethod(11)
    def SetHttpMethod(method: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetHttpMethod(method: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
class IBackgroundCopyJobHttpOptions3(c_void_p):
    extends: win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJobHttpOptions2
    Guid = Guid('8a9263d3-fd4c-4eda-9b-28-30-13-2a-4d-4e-3c')
    @commethod(13)
    def SetServerCertificateValidationInterface(certValidationCallback: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def MakeCustomHeadersWriteOnly() -> win32more.Foundation.HRESULT: ...
class IBackgroundCopyManager(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('5ce34c0d-0dc9-4c1f-89-7c-da-a1-b7-8c-ee-7c')
    @commethod(3)
    def CreateJob(DisplayName: win32more.Foundation.PWSTR, Type: win32more.Networking.BackgroundIntelligentTransferService.BG_JOB_TYPE, pJobId: POINTER(Guid), ppJob: POINTER(win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetJob(jobID: POINTER(Guid), ppJob: POINTER(win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def EnumJobs(dwFlags: UInt32, ppEnum: POINTER(win32more.Networking.BackgroundIntelligentTransferService.IEnumBackgroundCopyJobs_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetErrorDescription(hResult: win32more.Foundation.HRESULT, LanguageId: UInt32, pErrorDescription: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
class IBackgroundCopyQMgr(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('16f41c69-09f5-41d2-8c-d8-3c-08-c4-7b-c8-a8')
    @commethod(3)
    def CreateGroup(guidGroupID: Guid, ppGroup: POINTER(win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyGroup_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetGroup(groupID: Guid, ppGroup: POINTER(win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyGroup_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def EnumGroups(dwFlags: UInt32, ppEnumGroups: POINTER(win32more.Networking.BackgroundIntelligentTransferService.IEnumBackgroundCopyGroups_head)) -> win32more.Foundation.HRESULT: ...
class IBackgroundCopyServerCertificateValidationCallback(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('4cec0d02-def7-4158-81-3a-c3-2a-46-94-5f-f7')
    @commethod(3)
    def ValidateServerCertificate(job: win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob_head, file: win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile_head, certLength: UInt32, certData: c_char_p_no, certEncodingType: UInt32, certStoreLength: UInt32, certStoreData: c_char_p_no) -> win32more.Foundation.HRESULT: ...
class IBITSExtensionSetup(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('29cfbbf7-09e4-4b97-b0-bc-f2-28-7e-3d-8e-b3')
    @commethod(7)
    def EnableBITSUploads() -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def DisableBITSUploads() -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetCleanupTaskName(pTaskName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetCleanupTask(riid: POINTER(Guid), ppUnk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
class IBITSExtensionSetupFactory(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('d5d2d542-5503-4e64-8b-48-72-ef-91-a3-2e-e1')
    @commethod(7)
    def GetObject(Path: win32more.Foundation.BSTR, ppExtensionSetup: POINTER(win32more.Networking.BackgroundIntelligentTransferService.IBITSExtensionSetup_head)) -> win32more.Foundation.HRESULT: ...
class IBitsPeer(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('659cdea2-489e-11d9-a9-cd-00-0d-56-96-52-51')
    @commethod(3)
    def GetPeerName(pName: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def IsAuthenticated(pAuth: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def IsAvailable(pOnline: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
class IBitsPeerCacheAdministration(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('659cdead-489e-11d9-a9-cd-00-0d-56-96-52-51')
    @commethod(3)
    def GetMaximumCacheSize(pBytes: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetMaximumCacheSize(Bytes: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetMaximumContentAge(pSeconds: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetMaximumContentAge(Seconds: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetConfigurationFlags(pFlags: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetConfigurationFlags(Flags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def EnumRecords(ppEnum: POINTER(win32more.Networking.BackgroundIntelligentTransferService.IEnumBitsPeerCacheRecords_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetRecord(id: POINTER(Guid), ppRecord: POINTER(win32more.Networking.BackgroundIntelligentTransferService.IBitsPeerCacheRecord_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def ClearRecords() -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def DeleteRecord(id: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def DeleteUrl(url: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def EnumPeers(ppEnum: POINTER(win32more.Networking.BackgroundIntelligentTransferService.IEnumBitsPeers_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def ClearPeers() -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def DiscoverPeers() -> win32more.Foundation.HRESULT: ...
class IBitsPeerCacheRecord(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('659cdeaf-489e-11d9-a9-cd-00-0d-56-96-52-51')
    @commethod(3)
    def GetId(pVal: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetOriginUrl(pVal: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetFileSize(pVal: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetFileModificationTime(pVal: POINTER(win32more.Foundation.FILETIME_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetLastAccessTime(pVal: POINTER(win32more.Foundation.FILETIME_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def IsFileValidated() -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetFileRanges(pRangeCount: POINTER(UInt32), ppRanges: POINTER(POINTER(win32more.Networking.BackgroundIntelligentTransferService.BG_FILE_RANGE_head))) -> win32more.Foundation.HRESULT: ...
class IBitsTokenOptions(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('9a2584c3-f7d2-457a-9a-5e-22-b6-7b-ff-c7-d2')
    @commethod(3)
    def SetHelperTokenFlags(UsageFlags: win32more.Networking.BackgroundIntelligentTransferService.BG_TOKEN) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetHelperTokenFlags(pFlags: POINTER(win32more.Networking.BackgroundIntelligentTransferService.BG_TOKEN)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetHelperToken() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def ClearHelperToken() -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetHelperTokenSid(pSid: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
class IEnumBackgroundCopyFiles(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ca51e165-c365-424c-8d-41-24-aa-a4-ff-3c-40')
    @commethod(3)
    def Next(celt: UInt32, rgelt: POINTER(win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile_head), pceltFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppenum: POINTER(win32more.Networking.BackgroundIntelligentTransferService.IEnumBackgroundCopyFiles_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetCount(puCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IEnumBackgroundCopyGroups(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('d993e603-4aa4-47c5-86-65-c2-0d-39-c2-ba-4f')
    @commethod(3)
    def Next(celt: UInt32, rgelt: POINTER(Guid), pceltFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppenum: POINTER(win32more.Networking.BackgroundIntelligentTransferService.IEnumBackgroundCopyGroups_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetCount(puCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IEnumBackgroundCopyJobs(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('1af4f612-3b71-466f-8f-58-7b-6f-73-ac-57-ad')
    @commethod(3)
    def Next(celt: UInt32, rgelt: POINTER(win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob_head), pceltFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppenum: POINTER(win32more.Networking.BackgroundIntelligentTransferService.IEnumBackgroundCopyJobs_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetCount(puCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IEnumBackgroundCopyJobs1(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('8baeba9d-8f1c-42c4-b8-2c-09-ae-79-98-0d-25')
    @commethod(3)
    def Next(celt: UInt32, rgelt: POINTER(Guid), pceltFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppenum: POINTER(win32more.Networking.BackgroundIntelligentTransferService.IEnumBackgroundCopyJobs1_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetCount(puCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IEnumBitsPeerCacheRecords(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('659cdea4-489e-11d9-a9-cd-00-0d-56-96-52-51')
    @commethod(3)
    def Next(celt: UInt32, rgelt: POINTER(win32more.Networking.BackgroundIntelligentTransferService.IBitsPeerCacheRecord_head), pceltFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppenum: POINTER(win32more.Networking.BackgroundIntelligentTransferService.IEnumBitsPeerCacheRecords_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetCount(puCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IEnumBitsPeers(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('659cdea5-489e-11d9-a9-cd-00-0d-56-96-52-51')
    @commethod(3)
    def Next(celt: UInt32, rgelt: POINTER(win32more.Networking.BackgroundIntelligentTransferService.IBitsPeer_head), pceltFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppenum: POINTER(win32more.Networking.BackgroundIntelligentTransferService.IEnumBitsPeers_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetCount(puCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
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
make_head(_module, 'IBITSExtensionSetup')
make_head(_module, 'IBITSExtensionSetupFactory')
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
__all__ = [
    "AsyncIBackgroundCopyCallback",
    "BG_AUTH_CREDENTIALS",
    "BG_AUTH_CREDENTIALS_UNION",
    "BG_AUTH_SCHEME",
    "BG_AUTH_SCHEME_BASIC",
    "BG_AUTH_SCHEME_DIGEST",
    "BG_AUTH_SCHEME_NEGOTIATE",
    "BG_AUTH_SCHEME_NTLM",
    "BG_AUTH_SCHEME_PASSPORT",
    "BG_AUTH_TARGET",
    "BG_AUTH_TARGET_PROXY",
    "BG_AUTH_TARGET_SERVER",
    "BG_BASIC_CREDENTIALS",
    "BG_CERT_STORE_LOCATION",
    "BG_CERT_STORE_LOCATION_CURRENT_SERVICE",
    "BG_CERT_STORE_LOCATION_CURRENT_USER",
    "BG_CERT_STORE_LOCATION_CURRENT_USER_GROUP_POLICY",
    "BG_CERT_STORE_LOCATION_LOCAL_MACHINE",
    "BG_CERT_STORE_LOCATION_LOCAL_MACHINE_ENTERPRISE",
    "BG_CERT_STORE_LOCATION_LOCAL_MACHINE_GROUP_POLICY",
    "BG_CERT_STORE_LOCATION_SERVICES",
    "BG_CERT_STORE_LOCATION_USERS",
    "BG_COPY_FILE_ALL",
    "BG_COPY_FILE_DACL",
    "BG_COPY_FILE_GROUP",
    "BG_COPY_FILE_OWNER",
    "BG_COPY_FILE_SACL",
    "BG_DISABLE_BRANCH_CACHE",
    "BG_ENABLE_PEERCACHING_CLIENT",
    "BG_ENABLE_PEERCACHING_SERVER",
    "BG_ERROR_CONTEXT",
    "BG_ERROR_CONTEXT_GENERAL_QUEUE_MANAGER",
    "BG_ERROR_CONTEXT_GENERAL_TRANSPORT",
    "BG_ERROR_CONTEXT_LOCAL_FILE",
    "BG_ERROR_CONTEXT_NONE",
    "BG_ERROR_CONTEXT_QUEUE_MANAGER_NOTIFICATION",
    "BG_ERROR_CONTEXT_REMOTE_APPLICATION",
    "BG_ERROR_CONTEXT_REMOTE_FILE",
    "BG_ERROR_CONTEXT_SERVER_CERTIFICATE_CALLBACK",
    "BG_ERROR_CONTEXT_UNKNOWN",
    "BG_E_APP_PACKAGE_NOT_FOUND",
    "BG_E_APP_PACKAGE_SCENARIO_NOT_SUPPORTED",
    "BG_E_BLOCKED_BY_BACKGROUND_ACCESS_POLICY",
    "BG_E_BLOCKED_BY_BATTERY_POLICY",
    "BG_E_BLOCKED_BY_BATTERY_SAVER",
    "BG_E_BLOCKED_BY_COST_TRANSFER_POLICY",
    "BG_E_BLOCKED_BY_GAME_MODE",
    "BG_E_BLOCKED_BY_POLICY",
    "BG_E_BLOCKED_BY_SYSTEM_POLICY",
    "BG_E_BUSYCACHERECORD",
    "BG_E_CLIENT_SERVER_PROTOCOL_MISMATCH",
    "BG_E_COMMIT_IN_PROGRESS",
    "BG_E_CONNECTION_CLOSED",
    "BG_E_CONNECT_FAILURE",
    "BG_E_DATABASE_CORRUPT",
    "BG_E_DESTINATION_LOCKED",
    "BG_E_DISCOVERY_IN_PROGRESS",
    "BG_E_EMPTY",
    "BG_E_ERROR_CONTEXT_GENERAL_QUEUE_MANAGER",
    "BG_E_ERROR_CONTEXT_GENERAL_TRANSPORT",
    "BG_E_ERROR_CONTEXT_LOCAL_FILE",
    "BG_E_ERROR_CONTEXT_QUEUE_MANAGER_NOTIFICATION",
    "BG_E_ERROR_CONTEXT_REMOTE_APPLICATION",
    "BG_E_ERROR_CONTEXT_REMOTE_FILE",
    "BG_E_ERROR_CONTEXT_SERVER_CERTIFICATE_CALLBACK",
    "BG_E_ERROR_CONTEXT_UNKNOWN",
    "BG_E_ERROR_INFORMATION_UNAVAILABLE",
    "BG_E_FILE_NOT_AVAILABLE",
    "BG_E_FILE_NOT_FOUND",
    "BG_E_HTTP_ERROR_100",
    "BG_E_HTTP_ERROR_101",
    "BG_E_HTTP_ERROR_200",
    "BG_E_HTTP_ERROR_201",
    "BG_E_HTTP_ERROR_202",
    "BG_E_HTTP_ERROR_203",
    "BG_E_HTTP_ERROR_204",
    "BG_E_HTTP_ERROR_205",
    "BG_E_HTTP_ERROR_206",
    "BG_E_HTTP_ERROR_300",
    "BG_E_HTTP_ERROR_301",
    "BG_E_HTTP_ERROR_302",
    "BG_E_HTTP_ERROR_303",
    "BG_E_HTTP_ERROR_304",
    "BG_E_HTTP_ERROR_305",
    "BG_E_HTTP_ERROR_307",
    "BG_E_HTTP_ERROR_400",
    "BG_E_HTTP_ERROR_401",
    "BG_E_HTTP_ERROR_402",
    "BG_E_HTTP_ERROR_403",
    "BG_E_HTTP_ERROR_404",
    "BG_E_HTTP_ERROR_405",
    "BG_E_HTTP_ERROR_406",
    "BG_E_HTTP_ERROR_407",
    "BG_E_HTTP_ERROR_408",
    "BG_E_HTTP_ERROR_409",
    "BG_E_HTTP_ERROR_410",
    "BG_E_HTTP_ERROR_411",
    "BG_E_HTTP_ERROR_412",
    "BG_E_HTTP_ERROR_413",
    "BG_E_HTTP_ERROR_414",
    "BG_E_HTTP_ERROR_415",
    "BG_E_HTTP_ERROR_416",
    "BG_E_HTTP_ERROR_417",
    "BG_E_HTTP_ERROR_449",
    "BG_E_HTTP_ERROR_500",
    "BG_E_HTTP_ERROR_501",
    "BG_E_HTTP_ERROR_502",
    "BG_E_HTTP_ERROR_503",
    "BG_E_HTTP_ERROR_504",
    "BG_E_HTTP_ERROR_505",
    "BG_E_INSUFFICIENT_HTTP_SUPPORT",
    "BG_E_INSUFFICIENT_RANGE_SUPPORT",
    "BG_E_INVALID_AUTH_SCHEME",
    "BG_E_INVALID_AUTH_TARGET",
    "BG_E_INVALID_CREDENTIALS",
    "BG_E_INVALID_HASH_ALGORITHM",
    "BG_E_INVALID_PROXY_INFO",
    "BG_E_INVALID_RANGE",
    "BG_E_INVALID_SERVER_RESPONSE",
    "BG_E_INVALID_STATE",
    "BG_E_LOCAL_FILE_CHANGED",
    "BG_E_MAXDOWNLOAD_TIMEOUT",
    "BG_E_MAX_DOWNLOAD_SIZE_INVALID_VALUE",
    "BG_E_MAX_DOWNLOAD_SIZE_LIMIT_REACHED",
    "BG_E_MISSING_FILE_SIZE",
    "BG_E_NETWORK_DISCONNECTED",
    "BG_E_NEW_OWNER_DIFF_MAPPING",
    "BG_E_NEW_OWNER_NO_FILE_ACCESS",
    "BG_E_NOT_FOUND",
    "BG_E_NOT_SUPPORTED_WITH_CUSTOM_HTTP_METHOD",
    "BG_E_NO_PROGRESS",
    "BG_E_OVERLAPPING_RANGES",
    "BG_E_PASSWORD_TOO_LARGE",
    "BG_E_PEERCACHING_DISABLED",
    "BG_E_PROPERTY_SUPPORTED_FOR_DOWNLOAD_JOBS_ONLY",
    "BG_E_PROTOCOL_NOT_AVAILABLE",
    "BG_E_PROXY_BYPASS_LIST_TOO_LARGE",
    "BG_E_PROXY_LIST_TOO_LARGE",
    "BG_E_RANDOM_ACCESS_NOT_SUPPORTED",
    "BG_E_READ_ONLY_PROPERTY",
    "BG_E_READ_ONLY_PROPERTY_AFTER_ADDFILE",
    "BG_E_READ_ONLY_PROPERTY_AFTER_RESUME",
    "BG_E_READ_ONLY_WHEN_JOB_ACTIVE",
    "BG_E_RECORD_DELETED",
    "BG_E_REMOTE_FILE_CHANGED",
    "BG_E_REMOTE_NOT_SUPPORTED",
    "BG_E_SERVER_CERT_VALIDATION_INTERFACE_REQUIRED",
    "BG_E_SERVER_EXECUTE_ENABLE",
    "BG_E_SESSION_NOT_FOUND",
    "BG_E_STANDBY_MODE",
    "BG_E_STRING_TOO_LONG",
    "BG_E_TEST_OPTION_BLOCKED_DOWNLOAD",
    "BG_E_TOKEN_REQUIRED",
    "BG_E_TOO_LARGE",
    "BG_E_TOO_MANY_FILES",
    "BG_E_TOO_MANY_FILES_IN_JOB",
    "BG_E_TOO_MANY_JOBS_PER_MACHINE",
    "BG_E_TOO_MANY_JOBS_PER_USER",
    "BG_E_TOO_MANY_RANGES_IN_FILE",
    "BG_E_UNKNOWN_PROPERTY_ID",
    "BG_E_UNSUPPORTED_JOB_CONFIGURATION",
    "BG_E_UPNP_ERROR",
    "BG_E_USERNAME_TOO_LARGE",
    "BG_E_USE_STORED_CREDENTIALS_NOT_SUPPORTED",
    "BG_E_VALIDATION_FAILED",
    "BG_E_VOLUME_CHANGED",
    "BG_E_WATCHDOG_TIMEOUT",
    "BG_FILE_INFO",
    "BG_FILE_PROGRESS",
    "BG_FILE_RANGE",
    "BG_HTTP_REDIRECT_POLICY_ALLOW_HTTPS_TO_HTTP",
    "BG_HTTP_REDIRECT_POLICY_ALLOW_REPORT",
    "BG_HTTP_REDIRECT_POLICY_ALLOW_SILENT",
    "BG_HTTP_REDIRECT_POLICY_DISALLOW",
    "BG_HTTP_REDIRECT_POLICY_MASK",
    "BG_JOB_DISABLE_BRANCH_CACHE",
    "BG_JOB_ENABLE_PEERCACHING_CLIENT",
    "BG_JOB_ENABLE_PEERCACHING_SERVER",
    "BG_JOB_ENUM_ALL_USERS",
    "BG_JOB_PRIORITY",
    "BG_JOB_PRIORITY_FOREGROUND",
    "BG_JOB_PRIORITY_HIGH",
    "BG_JOB_PRIORITY_LOW",
    "BG_JOB_PRIORITY_NORMAL",
    "BG_JOB_PROGRESS",
    "BG_JOB_PROXY_USAGE",
    "BG_JOB_PROXY_USAGE_AUTODETECT",
    "BG_JOB_PROXY_USAGE_NO_PROXY",
    "BG_JOB_PROXY_USAGE_OVERRIDE",
    "BG_JOB_PROXY_USAGE_PRECONFIG",
    "BG_JOB_REPLY_PROGRESS",
    "BG_JOB_STATE",
    "BG_JOB_STATE_ACKNOWLEDGED",
    "BG_JOB_STATE_CANCELLED",
    "BG_JOB_STATE_CONNECTING",
    "BG_JOB_STATE_ERROR",
    "BG_JOB_STATE_QUEUED",
    "BG_JOB_STATE_SUSPENDED",
    "BG_JOB_STATE_TRANSFERRED",
    "BG_JOB_STATE_TRANSFERRING",
    "BG_JOB_STATE_TRANSIENT_ERROR",
    "BG_JOB_TIMES",
    "BG_JOB_TYPE",
    "BG_JOB_TYPE_DOWNLOAD",
    "BG_JOB_TYPE_UPLOAD",
    "BG_JOB_TYPE_UPLOAD_REPLY",
    "BG_NOTIFY_DISABLE",
    "BG_NOTIFY_FILE_RANGES_TRANSFERRED",
    "BG_NOTIFY_FILE_TRANSFERRED",
    "BG_NOTIFY_JOB_ERROR",
    "BG_NOTIFY_JOB_MODIFICATION",
    "BG_NOTIFY_JOB_TRANSFERRED",
    "BG_SSL_ENABLE_CRL_CHECK",
    "BG_SSL_IGNORE_CERT_CN_INVALID",
    "BG_SSL_IGNORE_CERT_DATE_INVALID",
    "BG_SSL_IGNORE_CERT_WRONG_USAGE",
    "BG_SSL_IGNORE_UNKNOWN_CA",
    "BG_S_ERROR_CONTEXT_NONE",
    "BG_S_OVERRIDDEN_BY_POLICY",
    "BG_S_PARTIAL_COMPLETE",
    "BG_S_PROXY_CHANGED",
    "BG_S_UNABLE_TO_DELETE_FILES",
    "BG_TOKEN",
    "BG_TOKEN_LOCAL_FILE",
    "BG_TOKEN_NETWORK",
    "BITSExtensionSetupFactory",
    "BITS_COST_OPTION_IGNORE_CONGESTION",
    "BITS_COST_STATE_BELOW_CAP",
    "BITS_COST_STATE_CAPPED_USAGE_UNKNOWN",
    "BITS_COST_STATE_NEAR_CAP",
    "BITS_COST_STATE_OVERCAP_CHARGED",
    "BITS_COST_STATE_OVERCAP_THROTTLED",
    "BITS_COST_STATE_RESERVED",
    "BITS_COST_STATE_ROAMING",
    "BITS_COST_STATE_UNRESTRICTED",
    "BITS_COST_STATE_USAGE_BASED",
    "BITS_FILE_PROPERTY_ID",
    "BITS_FILE_PROPERTY_ID_HTTP_RESPONSE_HEADERS",
    "BITS_FILE_PROPERTY_VALUE",
    "BITS_JOB_PROPERTY_DYNAMIC_CONTENT",
    "BITS_JOB_PROPERTY_HIGH_PERFORMANCE",
    "BITS_JOB_PROPERTY_ID",
    "BITS_JOB_PROPERTY_ID_COST_FLAGS",
    "BITS_JOB_PROPERTY_MAX_DOWNLOAD_SIZE",
    "BITS_JOB_PROPERTY_MINIMUM_NOTIFICATION_INTERVAL_MS",
    "BITS_JOB_PROPERTY_NOTIFICATION_CLSID",
    "BITS_JOB_PROPERTY_ON_DEMAND_MODE",
    "BITS_JOB_PROPERTY_USE_STORED_CREDENTIALS",
    "BITS_JOB_PROPERTY_VALUE",
    "BITS_JOB_TRANSFER_POLICY",
    "BITS_JOB_TRANSFER_POLICY_ALWAYS",
    "BITS_JOB_TRANSFER_POLICY_NOT_ROAMING",
    "BITS_JOB_TRANSFER_POLICY_NO_SURCHARGE",
    "BITS_JOB_TRANSFER_POLICY_STANDARD",
    "BITS_JOB_TRANSFER_POLICY_UNRESTRICTED",
    "BITS_MC_FAILED_TO_START",
    "BITS_MC_FATAL_IGD_ERROR",
    "BITS_MC_FILE_DELETION_FAILED",
    "BITS_MC_FILE_DELETION_FAILED_MORE",
    "BITS_MC_JOB_CANCELLED",
    "BITS_MC_JOB_NOTIFICATION_FAILURE",
    "BITS_MC_JOB_PROPERTY_CHANGE",
    "BITS_MC_JOB_SCAVENGED",
    "BITS_MC_JOB_TAKE_OWNERSHIP",
    "BITS_MC_PEERCACHING_PORT",
    "BITS_MC_STATE_FILE_CORRUPT",
    "BITS_MC_WSD_PORT",
    "BackgroundCopyManager",
    "BackgroundCopyManager10_1",
    "BackgroundCopyManager10_2",
    "BackgroundCopyManager10_3",
    "BackgroundCopyManager1_5",
    "BackgroundCopyManager2_0",
    "BackgroundCopyManager2_5",
    "BackgroundCopyManager3_0",
    "BackgroundCopyManager4_0",
    "BackgroundCopyManager5_0",
    "BackgroundCopyQMgr",
    "FILESETINFO",
    "GROUPPROP",
    "GROUPPROP_DESCRIPTION",
    "GROUPPROP_DISPLAYNAME",
    "GROUPPROP_LOCALUSERID",
    "GROUPPROP_LOCALUSERPWD",
    "GROUPPROP_NOTIFYCLSID",
    "GROUPPROP_NOTIFYFLAGS",
    "GROUPPROP_PRIORITY",
    "GROUPPROP_PROGRESSPERCENT",
    "GROUPPROP_PROGRESSSIZE",
    "GROUPPROP_PROGRESSTIME",
    "GROUPPROP_PROTOCOLFLAGS",
    "GROUPPROP_REMOTEUSERID",
    "GROUPPROP_REMOTEUSERPWD",
    "IBITSExtensionSetup",
    "IBITSExtensionSetupFactory",
    "IBackgroundCopyCallback",
    "IBackgroundCopyCallback1",
    "IBackgroundCopyCallback2",
    "IBackgroundCopyCallback3",
    "IBackgroundCopyError",
    "IBackgroundCopyFile",
    "IBackgroundCopyFile2",
    "IBackgroundCopyFile3",
    "IBackgroundCopyFile4",
    "IBackgroundCopyFile5",
    "IBackgroundCopyFile6",
    "IBackgroundCopyGroup",
    "IBackgroundCopyJob",
    "IBackgroundCopyJob1",
    "IBackgroundCopyJob2",
    "IBackgroundCopyJob3",
    "IBackgroundCopyJob4",
    "IBackgroundCopyJob5",
    "IBackgroundCopyJobHttpOptions",
    "IBackgroundCopyJobHttpOptions2",
    "IBackgroundCopyJobHttpOptions3",
    "IBackgroundCopyManager",
    "IBackgroundCopyQMgr",
    "IBackgroundCopyServerCertificateValidationCallback",
    "IBitsPeer",
    "IBitsPeerCacheAdministration",
    "IBitsPeerCacheRecord",
    "IBitsTokenOptions",
    "IEnumBackgroundCopyFiles",
    "IEnumBackgroundCopyGroups",
    "IEnumBackgroundCopyJobs",
    "IEnumBackgroundCopyJobs1",
    "IEnumBitsPeerCacheRecords",
    "IEnumBitsPeers",
    "QM_E_DOWNLOADER_UNAVAILABLE",
    "QM_E_INVALID_STATE",
    "QM_E_ITEM_NOT_FOUND",
    "QM_E_SERVICE_UNAVAILABLE",
    "QM_NOTIFY_DISABLE_NOTIFY",
    "QM_NOTIFY_FILE_DONE",
    "QM_NOTIFY_GROUP_DONE",
    "QM_NOTIFY_JOB_DONE",
    "QM_NOTIFY_USE_PROGRESSEX",
    "QM_PROGRESS_PERCENT_DONE",
    "QM_PROGRESS_SIZE_DONE",
    "QM_PROGRESS_TIME_DONE",
    "QM_PROTOCOL_CUSTOM",
    "QM_PROTOCOL_FTP",
    "QM_PROTOCOL_HTTP",
    "QM_PROTOCOL_SMB",
    "QM_STATUS_FILE_COMPLETE",
    "QM_STATUS_FILE_INCOMPLETE",
    "QM_STATUS_GROUP_COMPLETE",
    "QM_STATUS_GROUP_ERROR",
    "QM_STATUS_GROUP_FOREGROUND",
    "QM_STATUS_GROUP_INCOMPLETE",
    "QM_STATUS_GROUP_SUSPENDED",
    "QM_STATUS_JOB_COMPLETE",
    "QM_STATUS_JOB_ERROR",
    "QM_STATUS_JOB_FOREGROUND",
    "QM_STATUS_JOB_INCOMPLETE",
]
_arch_optional = [
]
