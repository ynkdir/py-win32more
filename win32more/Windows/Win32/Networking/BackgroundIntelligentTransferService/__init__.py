from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Variant
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
class AsyncIBackgroundCopyCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ca29d251-b4bb-4679-a3d9-ae8006119d54}')
    @commethod(3)
    def Begin_JobTransferred(self, pJob: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Finish_JobTransferred(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Begin_JobError(self, pJob: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob, pError: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyError) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Finish_JobError(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Begin_JobModification(self, pJob: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob, dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Finish_JobModification(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class BG_AUTH_CREDENTIALS(Structure):
    Target: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_AUTH_TARGET
    Scheme: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_AUTH_SCHEME
    Credentials: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_AUTH_CREDENTIALS_UNION
class BG_AUTH_CREDENTIALS_UNION(Union):
    Basic: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_BASIC_CREDENTIALS
BG_AUTH_SCHEME = Int32
BG_AUTH_SCHEME_BASIC: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_AUTH_SCHEME = 1
BG_AUTH_SCHEME_DIGEST: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_AUTH_SCHEME = 2
BG_AUTH_SCHEME_NTLM: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_AUTH_SCHEME = 3
BG_AUTH_SCHEME_NEGOTIATE: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_AUTH_SCHEME = 4
BG_AUTH_SCHEME_PASSPORT: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_AUTH_SCHEME = 5
BG_AUTH_TARGET = Int32
BG_AUTH_TARGET_SERVER: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_AUTH_TARGET = 1
BG_AUTH_TARGET_PROXY: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_AUTH_TARGET = 2
class BG_BASIC_CREDENTIALS(Structure):
    UserName: win32more.Windows.Win32.Foundation.PWSTR
    Password: win32more.Windows.Win32.Foundation.PWSTR
BG_CERT_STORE_LOCATION = Int32
BG_CERT_STORE_LOCATION_CURRENT_USER: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_CERT_STORE_LOCATION = 0
BG_CERT_STORE_LOCATION_LOCAL_MACHINE: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_CERT_STORE_LOCATION = 1
BG_CERT_STORE_LOCATION_CURRENT_SERVICE: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_CERT_STORE_LOCATION = 2
BG_CERT_STORE_LOCATION_SERVICES: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_CERT_STORE_LOCATION = 3
BG_CERT_STORE_LOCATION_USERS: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_CERT_STORE_LOCATION = 4
BG_CERT_STORE_LOCATION_CURRENT_USER_GROUP_POLICY: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_CERT_STORE_LOCATION = 5
BG_CERT_STORE_LOCATION_LOCAL_MACHINE_GROUP_POLICY: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_CERT_STORE_LOCATION = 6
BG_CERT_STORE_LOCATION_LOCAL_MACHINE_ENTERPRISE: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_CERT_STORE_LOCATION = 7
BG_ERROR_CONTEXT = Int32
BG_ERROR_CONTEXT_NONE: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_ERROR_CONTEXT = 0
BG_ERROR_CONTEXT_UNKNOWN: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_ERROR_CONTEXT = 1
BG_ERROR_CONTEXT_GENERAL_QUEUE_MANAGER: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_ERROR_CONTEXT = 2
BG_ERROR_CONTEXT_QUEUE_MANAGER_NOTIFICATION: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_ERROR_CONTEXT = 3
BG_ERROR_CONTEXT_LOCAL_FILE: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_ERROR_CONTEXT = 4
BG_ERROR_CONTEXT_REMOTE_FILE: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_ERROR_CONTEXT = 5
BG_ERROR_CONTEXT_GENERAL_TRANSPORT: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_ERROR_CONTEXT = 6
BG_ERROR_CONTEXT_REMOTE_APPLICATION: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_ERROR_CONTEXT = 7
BG_ERROR_CONTEXT_SERVER_CERTIFICATE_CALLBACK: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_ERROR_CONTEXT = 8
class BG_FILE_INFO(Structure):
    RemoteName: win32more.Windows.Win32.Foundation.PWSTR
    LocalName: win32more.Windows.Win32.Foundation.PWSTR
class BG_FILE_PROGRESS(Structure):
    BytesTotal: UInt64
    BytesTransferred: UInt64
    Completed: win32more.Windows.Win32.Foundation.BOOL
class BG_FILE_RANGE(Structure):
    InitialOffset: UInt64
    Length: UInt64
BG_JOB_PRIORITY = Int32
BG_JOB_PRIORITY_FOREGROUND: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_JOB_PRIORITY = 0
BG_JOB_PRIORITY_HIGH: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_JOB_PRIORITY = 1
BG_JOB_PRIORITY_NORMAL: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_JOB_PRIORITY = 2
BG_JOB_PRIORITY_LOW: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_JOB_PRIORITY = 3
class BG_JOB_PROGRESS(Structure):
    BytesTotal: UInt64
    BytesTransferred: UInt64
    FilesTotal: UInt32
    FilesTransferred: UInt32
BG_JOB_PROXY_USAGE = Int32
BG_JOB_PROXY_USAGE_PRECONFIG: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_JOB_PROXY_USAGE = 0
BG_JOB_PROXY_USAGE_NO_PROXY: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_JOB_PROXY_USAGE = 1
BG_JOB_PROXY_USAGE_OVERRIDE: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_JOB_PROXY_USAGE = 2
BG_JOB_PROXY_USAGE_AUTODETECT: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_JOB_PROXY_USAGE = 3
class BG_JOB_REPLY_PROGRESS(Structure):
    BytesTotal: UInt64
    BytesTransferred: UInt64
BG_JOB_STATE = Int32
BG_JOB_STATE_QUEUED: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_JOB_STATE = 0
BG_JOB_STATE_CONNECTING: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_JOB_STATE = 1
BG_JOB_STATE_TRANSFERRING: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_JOB_STATE = 2
BG_JOB_STATE_SUSPENDED: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_JOB_STATE = 3
BG_JOB_STATE_ERROR: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_JOB_STATE = 4
BG_JOB_STATE_TRANSIENT_ERROR: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_JOB_STATE = 5
BG_JOB_STATE_TRANSFERRED: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_JOB_STATE = 6
BG_JOB_STATE_ACKNOWLEDGED: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_JOB_STATE = 7
BG_JOB_STATE_CANCELLED: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_JOB_STATE = 8
class BG_JOB_TIMES(Structure):
    CreationTime: win32more.Windows.Win32.Foundation.FILETIME
    ModificationTime: win32more.Windows.Win32.Foundation.FILETIME
    TransferCompletionTime: win32more.Windows.Win32.Foundation.FILETIME
BG_JOB_TYPE = Int32
BG_JOB_TYPE_DOWNLOAD: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_JOB_TYPE = 0
BG_JOB_TYPE_UPLOAD: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_JOB_TYPE = 1
BG_JOB_TYPE_UPLOAD_REPLY: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_JOB_TYPE = 2
BG_TOKEN = UInt32
BG_TOKEN_LOCAL_FILE: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_TOKEN = 1
BG_TOKEN_NETWORK: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_TOKEN = 2
BITSExtensionSetupFactory = Guid('{efbbab68-7286-4783-94bf-9461d8b7e7e9}')
BITS_FILE_PROPERTY_ID = Int32
BITS_FILE_PROPERTY_ID_HTTP_RESPONSE_HEADERS: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BITS_FILE_PROPERTY_ID = 1
class BITS_FILE_PROPERTY_VALUE(Union):
    String: win32more.Windows.Win32.Foundation.PWSTR
BITS_JOB_PROPERTY_ID = Int32
BITS_JOB_PROPERTY_ID_COST_FLAGS: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BITS_JOB_PROPERTY_ID = 1
BITS_JOB_PROPERTY_NOTIFICATION_CLSID: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BITS_JOB_PROPERTY_ID = 2
BITS_JOB_PROPERTY_DYNAMIC_CONTENT: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BITS_JOB_PROPERTY_ID = 3
BITS_JOB_PROPERTY_HIGH_PERFORMANCE: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BITS_JOB_PROPERTY_ID = 4
BITS_JOB_PROPERTY_MAX_DOWNLOAD_SIZE: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BITS_JOB_PROPERTY_ID = 5
BITS_JOB_PROPERTY_USE_STORED_CREDENTIALS: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BITS_JOB_PROPERTY_ID = 7
BITS_JOB_PROPERTY_MINIMUM_NOTIFICATION_INTERVAL_MS: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BITS_JOB_PROPERTY_ID = 9
BITS_JOB_PROPERTY_ON_DEMAND_MODE: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BITS_JOB_PROPERTY_ID = 10
class BITS_JOB_PROPERTY_VALUE(Union):
    Dword: UInt32
    ClsID: Guid
    Enable: win32more.Windows.Win32.Foundation.BOOL
    Uint64: UInt64
    Target: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_AUTH_TARGET
BITS_JOB_TRANSFER_POLICY = Int32
BITS_JOB_TRANSFER_POLICY_ALWAYS: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BITS_JOB_TRANSFER_POLICY = -2147483393
BITS_JOB_TRANSFER_POLICY_NOT_ROAMING: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BITS_JOB_TRANSFER_POLICY = -2147483521
BITS_JOB_TRANSFER_POLICY_NO_SURCHARGE: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BITS_JOB_TRANSFER_POLICY = -2147483537
BITS_JOB_TRANSFER_POLICY_STANDARD: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BITS_JOB_TRANSFER_POLICY = -2147483545
BITS_JOB_TRANSFER_POLICY_UNRESTRICTED: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BITS_JOB_TRANSFER_POLICY = -2147483615
BackgroundCopyManager = Guid('{4991d34b-80a1-4291-83b6-3328366b9097}')
BackgroundCopyManager10_1 = Guid('{4bd3e4e1-7bd4-4a2b-9964-496400de5193}')
BackgroundCopyManager10_2 = Guid('{4575438f-a6c8-4976-b0fe-2f26b80d959e}')
BackgroundCopyManager10_3 = Guid('{5fd42ad5-c04e-4d36-adc7-e08ff15737ad}')
BackgroundCopyManager1_5 = Guid('{f087771f-d74f-4c1a-bb8a-e16aca9124ea}')
BackgroundCopyManager2_0 = Guid('{6d18ad12-bde3-4393-b311-099c346e6df9}')
BackgroundCopyManager2_5 = Guid('{03ca98d6-ff5d-49b8-abc6-03dd84127020}')
BackgroundCopyManager3_0 = Guid('{659cdea7-489e-11d9-a9cd-000d56965251}')
BackgroundCopyManager4_0 = Guid('{bb6df56b-cace-11dc-9992-0019b93a3a84}')
BackgroundCopyManager5_0 = Guid('{1ecca34c-e88a-44e3-8d6a-8921bde9e452}')
BackgroundCopyQMgr = Guid('{69ad4aee-51be-439b-a92c-86ae490e8b30}')
class FILESETINFO(Structure):
    bstrRemoteFile: win32more.Windows.Win32.Foundation.BSTR
    bstrLocalFile: win32more.Windows.Win32.Foundation.BSTR
    dwSizeHint: UInt32
GROUPPROP = Int32
GROUPPROP_PRIORITY: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.GROUPPROP = 0
GROUPPROP_REMOTEUSERID: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.GROUPPROP = 1
GROUPPROP_REMOTEUSERPWD: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.GROUPPROP = 2
GROUPPROP_LOCALUSERID: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.GROUPPROP = 3
GROUPPROP_LOCALUSERPWD: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.GROUPPROP = 4
GROUPPROP_PROTOCOLFLAGS: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.GROUPPROP = 5
GROUPPROP_NOTIFYFLAGS: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.GROUPPROP = 6
GROUPPROP_NOTIFYCLSID: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.GROUPPROP = 7
GROUPPROP_PROGRESSSIZE: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.GROUPPROP = 8
GROUPPROP_PROGRESSPERCENT: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.GROUPPROP = 9
GROUPPROP_PROGRESSTIME: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.GROUPPROP = 10
GROUPPROP_DISPLAYNAME: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.GROUPPROP = 11
GROUPPROP_DESCRIPTION: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.GROUPPROP = 12
class IBITSExtensionSetup(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{29cfbbf7-09e4-4b97-b0bc-f2287e3d8eb3}')
    @commethod(7)
    def EnableBITSUploads(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def DisableBITSUploads(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetCleanupTaskName(self, pTaskName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetCleanupTask(self, riid: POINTER(Guid), ppUnk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBITSExtensionSetupFactory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{d5d2d542-5503-4e64-8b48-72ef91a32ee1}')
    @commethod(7)
    def GetObject(self, Path: win32more.Windows.Win32.Foundation.BSTR, ppExtensionSetup: POINTER(win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IBITSExtensionSetup)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBackgroundCopyCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{97ea99c7-0186-4ad4-8df9-c5b4e0ed6b22}')
    @commethod(3)
    def JobTransferred(self, pJob: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def JobError(self, pJob: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob, pError: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyError) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def JobModification(self, pJob: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob, dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBackgroundCopyCallback1(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{084f6593-3800-4e08-9b59-99fa59addf82}')
    @commethod(3)
    def OnStatus(self, pGroup: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyGroup, pJob: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob1, dwFileIndex: UInt32, dwStatus: UInt32, dwNumOfRetries: UInt32, dwWin32Result: UInt32, dwTransportResult: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnProgress(self, ProgressType: UInt32, pGroup: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyGroup, pJob: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob1, dwFileIndex: UInt32, dwProgressValue: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnProgressEx(self, ProgressType: UInt32, pGroup: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyGroup, pJob: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob1, dwFileIndex: UInt32, dwProgressValue: UInt32, dwByteArraySize: UInt32, pByte: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBackgroundCopyCallback2(ComPtr):
    extends: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyCallback
    _iid_ = Guid('{659cdeac-489e-11d9-a9cd-000d56965251}')
    @commethod(6)
    def FileTransferred(self, pJob: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob, pFile: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBackgroundCopyCallback3(ComPtr):
    extends: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyCallback2
    _iid_ = Guid('{98c97bd2-e32b-4ad8-a528-95fd8b16bd42}')
    @commethod(7)
    def FileRangesTransferred(self, job: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob, file: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile, rangeCount: UInt32, ranges: POINTER(win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_FILE_RANGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBackgroundCopyError(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{19c613a0-fcb8-4f28-81ae-897c3d078f81}')
    @commethod(3)
    def GetError(self, pContext: POINTER(win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_ERROR_CONTEXT), pCode: POINTER(win32more.Windows.Win32.Foundation.HRESULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFile(self, pVal: POINTER(win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetErrorDescription(self, LanguageId: UInt32, pErrorDescription: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetErrorContextDescription(self, LanguageId: UInt32, pContextDescription: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetProtocol(self, pProtocol: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBackgroundCopyFile(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{01b7bd23-fb88-4a77-8490-5891d3e4653a}')
    @commethod(3)
    def GetRemoteName(self, pVal: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLocalName(self, pVal: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetProgress(self, pVal: POINTER(win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_FILE_PROGRESS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBackgroundCopyFile2(ComPtr):
    extends: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile
    _iid_ = Guid('{83e81b93-0873-474d-8a8c-f2018b1a939c}')
    @commethod(6)
    def GetFileRanges(self, RangeCount: POINTER(UInt32), Ranges: POINTER(POINTER(win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_FILE_RANGE))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetRemoteName(self, Val: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBackgroundCopyFile3(ComPtr):
    extends: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile2
    _iid_ = Guid('{659cdeaa-489e-11d9-a9cd-000d56965251}')
    @commethod(8)
    def GetTemporaryName(self, pFilename: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetValidationState(self, state: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetValidationState(self, pState: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def IsDownloadedFromPeer(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBackgroundCopyFile4(ComPtr):
    extends: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile3
    _iid_ = Guid('{ef7e0655-7888-4960-b0e5-730846e03492}')
    @commethod(12)
    def GetPeerDownloadStats(self, pFromOrigin: POINTER(UInt64), pFromPeers: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBackgroundCopyFile5(ComPtr):
    extends: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile4
    _iid_ = Guid('{85c1657f-dafc-40e8-8834-df18ea25717e}')
    @commethod(13)
    def SetProperty(self, PropertyId: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BITS_FILE_PROPERTY_ID, PropertyValue: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BITS_FILE_PROPERTY_VALUE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetProperty(self, PropertyId: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BITS_FILE_PROPERTY_ID, PropertyValue: POINTER(win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BITS_FILE_PROPERTY_VALUE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBackgroundCopyFile6(ComPtr):
    extends: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile5
    _iid_ = Guid('{cf6784f7-d677-49fd-9368-cb47aee9d1ad}')
    @commethod(15)
    def UpdateDownloadPosition(self, offset: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def RequestFileRanges(self, rangeCount: UInt32, ranges: POINTER(win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_FILE_RANGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetFilledFileRanges(self, rangeCount: POINTER(UInt32), ranges: POINTER(POINTER(win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_FILE_RANGE))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBackgroundCopyGroup(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1ded80a7-53ea-424f-8a04-17fea9adc4f5}')
    @commethod(3)
    def GetProp(self, propID: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.GROUPPROP, pvarVal: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetProp(self, propID: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.GROUPPROP, pvarVal: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetProgress(self, dwFlags: UInt32, pdwProgress: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetStatus(self, pdwStatus: POINTER(UInt32), pdwJobIndex: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetJob(self, jobID: Guid, ppJob: POINTER(win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob1)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SuspendGroup(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ResumeGroup(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def CancelGroup(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Size(self, pdwSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_GroupID(self, pguidGroupID: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def CreateJob(self, guidJobID: Guid, ppJob: POINTER(win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob1)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def EnumJobs(self, dwFlags: UInt32, ppEnumJobs: POINTER(win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IEnumBackgroundCopyJobs1)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SwitchToForeground(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def QueryNewJobInterface(self, iid: POINTER(Guid), pUnk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetNotificationPointer(self, iid: POINTER(Guid), pUnk: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBackgroundCopyJob(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{37668d37-507e-4160-9316-26306d150b12}')
    @commethod(3)
    def AddFileSet(self, cFileCount: UInt32, pFileSet: POINTER(win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_FILE_INFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddFile(self, RemoteUrl: win32more.Windows.Win32.Foundation.PWSTR, LocalName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumFiles(self, pEnum: POINTER(win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IEnumBackgroundCopyFiles)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Suspend(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Resume(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Cancel(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Complete(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetId(self, pVal: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetType(self, pVal: POINTER(win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_JOB_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetProgress(self, pVal: POINTER(win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_JOB_PROGRESS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetTimes(self, pVal: POINTER(win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_JOB_TIMES)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetState(self, pVal: POINTER(win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_JOB_STATE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetError(self, ppError: POINTER(win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyError)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetOwner(self, pVal: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetDisplayName(self, Val: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetDisplayName(self, pVal: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetDescription(self, Val: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetDescription(self, pVal: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def SetPriority(self, Val: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_JOB_PRIORITY) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetPriority(self, pVal: POINTER(win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_JOB_PRIORITY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetNotifyFlags(self, Val: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetNotifyFlags(self, pVal: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def SetNotifyInterface(self, Val: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetNotifyInterface(self, pVal: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def SetMinimumRetryDelay(self, Seconds: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetMinimumRetryDelay(self, Seconds: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def SetNoProgressTimeout(self, Seconds: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def GetNoProgressTimeout(self, Seconds: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def GetErrorCount(self, Errors: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def SetProxySettings(self, ProxyUsage: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_JOB_PROXY_USAGE, ProxyList: win32more.Windows.Win32.Foundation.PWSTR, ProxyBypassList: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def GetProxySettings(self, pProxyUsage: POINTER(win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_JOB_PROXY_USAGE), pProxyList: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pProxyBypassList: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def TakeOwnership(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBackgroundCopyJob1(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{59f5553c-2031-4629-bb18-2645a6970947}')
    @commethod(3)
    def CancelJob(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetProgress(self, dwFlags: UInt32, pdwProgress: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetStatus(self, pdwStatus: POINTER(UInt32), pdwWin32Result: POINTER(UInt32), pdwTransportResult: POINTER(UInt32), pdwNumOfRetries: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AddFiles(self, cFileCount: UInt32, ppFileSet: POINTER(POINTER(win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.FILESETINFO))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetFile(self, cFileIndex: UInt32, pFileInfo: POINTER(win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.FILESETINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetFileCount(self, pdwFileCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SwitchToForeground(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_JobID(self, pguidJobID: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBackgroundCopyJob2(ComPtr):
    extends: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob
    _iid_ = Guid('{54b50739-686f-45eb-9dff-d6a9a0faa9af}')
    @commethod(35)
    def SetNotifyCmdLine(self, Program: win32more.Windows.Win32.Foundation.PWSTR, Parameters: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def GetNotifyCmdLine(self, pProgram: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pParameters: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def GetReplyProgress(self, pProgress: POINTER(win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_JOB_REPLY_PROGRESS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def GetReplyData(self, ppBuffer: POINTER(POINTER(Byte)), pLength: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def SetReplyFileName(self, ReplyFileName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def GetReplyFileName(self, pReplyFileName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def SetCredentials(self, credentials: POINTER(win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_AUTH_CREDENTIALS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def RemoveCredentials(self, Target: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_AUTH_TARGET, Scheme: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_AUTH_SCHEME) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBackgroundCopyJob3(ComPtr):
    extends: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob2
    _iid_ = Guid('{443c8934-90ff-48ed-bcde-26f5c7450042}')
    @commethod(43)
    def ReplaceRemotePrefix(self, OldPrefix: win32more.Windows.Win32.Foundation.PWSTR, NewPrefix: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def AddFileWithRanges(self, RemoteUrl: win32more.Windows.Win32.Foundation.PWSTR, LocalName: win32more.Windows.Win32.Foundation.PWSTR, RangeCount: UInt32, Ranges: POINTER(win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_FILE_RANGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def SetFileACLFlags(self, Flags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def GetFileACLFlags(self, Flags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBackgroundCopyJob4(ComPtr):
    extends: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob3
    _iid_ = Guid('{659cdeae-489e-11d9-a9cd-000d56965251}')
    @commethod(47)
    def SetPeerCachingFlags(self, Flags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def GetPeerCachingFlags(self, pFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def GetOwnerIntegrityLevel(self, pLevel: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def GetOwnerElevationState(self, pElevated: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def SetMaximumDownloadTime(self, Timeout: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def GetMaximumDownloadTime(self, pTimeout: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBackgroundCopyJob5(ComPtr):
    extends: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob4
    _iid_ = Guid('{e847030c-bbba-4657-af6d-484aa42bf1fe}')
    @commethod(53)
    def SetProperty(self, PropertyId: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BITS_JOB_PROPERTY_ID, PropertyValue: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BITS_JOB_PROPERTY_VALUE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def GetProperty(self, PropertyId: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BITS_JOB_PROPERTY_ID, PropertyValue: POINTER(win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BITS_JOB_PROPERTY_VALUE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBackgroundCopyJobHttpOptions(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f1bd1079-9f01-4bdc-8036-f09b70095066}')
    @commethod(3)
    def SetClientCertificateByID(self, StoreLocation: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_CERT_STORE_LOCATION, StoreName: win32more.Windows.Win32.Foundation.PWSTR, pCertHashBlob: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetClientCertificateByName(self, StoreLocation: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_CERT_STORE_LOCATION, StoreName: win32more.Windows.Win32.Foundation.PWSTR, SubjectName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RemoveClientCertificate(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetClientCertificate(self, pStoreLocation: POINTER(win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_CERT_STORE_LOCATION), pStoreName: POINTER(win32more.Windows.Win32.Foundation.PWSTR), ppCertHashBlob: POINTER(POINTER(Byte)), pSubjectName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetCustomHeaders(self, RequestHeaders: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetCustomHeaders(self, pRequestHeaders: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetSecurityFlags(self, Flags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetSecurityFlags(self, pFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBackgroundCopyJobHttpOptions2(ComPtr):
    extends: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJobHttpOptions
    _iid_ = Guid('{b591a192-a405-4fc3-8323-4c5c542578fc}')
    @commethod(11)
    def SetHttpMethod(self, method: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetHttpMethod(self, method: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBackgroundCopyJobHttpOptions3(ComPtr):
    extends: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJobHttpOptions2
    _iid_ = Guid('{8a9263d3-fd4c-4eda-9b28-30132a4d4e3c}')
    @commethod(13)
    def SetServerCertificateValidationInterface(self, certValidationCallback: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def MakeCustomHeadersWriteOnly(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBackgroundCopyManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5ce34c0d-0dc9-4c1f-897c-daa1b78cee7c}')
    @commethod(3)
    def CreateJob(self, DisplayName: win32more.Windows.Win32.Foundation.PWSTR, Type: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_JOB_TYPE, pJobId: POINTER(Guid), ppJob: POINTER(win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetJob(self, jobID: POINTER(Guid), ppJob: POINTER(win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumJobs(self, dwFlags: UInt32, ppEnum: POINTER(win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IEnumBackgroundCopyJobs)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetErrorDescription(self, hResult: win32more.Windows.Win32.Foundation.HRESULT, LanguageId: UInt32, pErrorDescription: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBackgroundCopyQMgr(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{16f41c69-09f5-41d2-8cd8-3c08c47bc8a8}')
    @commethod(3)
    def CreateGroup(self, guidGroupID: Guid, ppGroup: POINTER(win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyGroup)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetGroup(self, groupID: Guid, ppGroup: POINTER(win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyGroup)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumGroups(self, dwFlags: UInt32, ppEnumGroups: POINTER(win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IEnumBackgroundCopyGroups)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBackgroundCopyServerCertificateValidationCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4cec0d02-def7-4158-813a-c32a46945ff7}')
    @commethod(3)
    def ValidateServerCertificate(self, job: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob, file: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile, certLength: UInt32, certData: POINTER(Byte), certEncodingType: UInt32, certStoreLength: UInt32, certStoreData: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBitsPeer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{659cdea2-489e-11d9-a9cd-000d56965251}')
    @commethod(3)
    def GetPeerName(self, pName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def IsAuthenticated(self, pAuth: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def IsAvailable(self, pOnline: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBitsPeerCacheAdministration(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{659cdead-489e-11d9-a9cd-000d56965251}')
    @commethod(3)
    def GetMaximumCacheSize(self, pBytes: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetMaximumCacheSize(self, Bytes: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetMaximumContentAge(self, pSeconds: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetMaximumContentAge(self, Seconds: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetConfigurationFlags(self, pFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetConfigurationFlags(self, Flags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def EnumRecords(self, ppEnum: POINTER(win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IEnumBitsPeerCacheRecords)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetRecord(self, id: POINTER(Guid), ppRecord: POINTER(win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IBitsPeerCacheRecord)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def ClearRecords(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def DeleteRecord(self, id: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def DeleteUrl(self, url: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def EnumPeers(self, ppEnum: POINTER(win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IEnumBitsPeers)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def ClearPeers(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def DiscoverPeers(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBitsPeerCacheRecord(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{659cdeaf-489e-11d9-a9cd-000d56965251}')
    @commethod(3)
    def GetId(self, pVal: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetOriginUrl(self, pVal: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetFileSize(self, pVal: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetFileModificationTime(self, pVal: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetLastAccessTime(self, pVal: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def IsFileValidated(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetFileRanges(self, pRangeCount: POINTER(UInt32), ppRanges: POINTER(POINTER(win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_FILE_RANGE))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBitsTokenOptions(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9a2584c3-f7d2-457a-9a5e-22b67bffc7d2}')
    @commethod(3)
    def SetHelperTokenFlags(self, UsageFlags: win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_TOKEN) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHelperTokenFlags(self, pFlags: POINTER(win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.BG_TOKEN)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetHelperToken(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ClearHelperToken(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetHelperTokenSid(self, pSid: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumBackgroundCopyFiles(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ca51e165-c365-424c-8d41-24aaa4ff3c40}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IEnumBackgroundCopyFiles)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCount(self, puCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumBackgroundCopyGroups(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d993e603-4aa4-47c5-8665-c20d39c2ba4f}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(Guid), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IEnumBackgroundCopyGroups)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCount(self, puCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumBackgroundCopyJobs(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1af4f612-3b71-466f-8f58-7b6f73ac57ad}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IEnumBackgroundCopyJobs)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCount(self, puCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumBackgroundCopyJobs1(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8baeba9d-8f1c-42c4-b82c-09ae79980d25}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(Guid), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IEnumBackgroundCopyJobs1)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCount(self, puCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumBitsPeerCacheRecords(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{659cdea4-489e-11d9-a9cd-000d56965251}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IBitsPeerCacheRecord), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IEnumBitsPeerCacheRecords)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCount(self, puCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumBitsPeers(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{659cdea5-489e-11d9-a9cd-000d56965251}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IBitsPeer), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(win32more.Windows.Win32.Networking.BackgroundIntelligentTransferService.IEnumBitsPeers)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCount(self, puCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...


make_ready(__name__)
