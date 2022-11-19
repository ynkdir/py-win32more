from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, PROPERTYKEY, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Networking.BackgroundIntelligentTransferService
import win32more.System.Com

import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
BG_NOTIFY_JOB_TRANSFERRED = 1
BG_NOTIFY_JOB_ERROR = 2
BG_NOTIFY_DISABLE = 4
BG_NOTIFY_JOB_MODIFICATION = 8
BG_NOTIFY_FILE_TRANSFERRED = 16
BG_NOTIFY_FILE_RANGES_TRANSFERRED = 32
BG_JOB_ENUM_ALL_USERS = 1
BG_COPY_FILE_OWNER = 1
BG_COPY_FILE_GROUP = 2
BG_COPY_FILE_DACL = 4
BG_COPY_FILE_SACL = 8
BG_COPY_FILE_ALL = 15
BG_SSL_ENABLE_CRL_CHECK = 1
BG_SSL_IGNORE_CERT_CN_INVALID = 2
BG_SSL_IGNORE_CERT_DATE_INVALID = 4
BG_SSL_IGNORE_UNKNOWN_CA = 8
BG_SSL_IGNORE_CERT_WRONG_USAGE = 16
BG_HTTP_REDIRECT_POLICY_MASK = 1792
BG_HTTP_REDIRECT_POLICY_ALLOW_SILENT = 0
BG_HTTP_REDIRECT_POLICY_ALLOW_REPORT = 256
BG_HTTP_REDIRECT_POLICY_DISALLOW = 512
BG_HTTP_REDIRECT_POLICY_ALLOW_HTTPS_TO_HTTP = 2048
BG_ENABLE_PEERCACHING_CLIENT = 1
BG_ENABLE_PEERCACHING_SERVER = 2
BG_DISABLE_BRANCH_CACHE = 4
BG_JOB_ENABLE_PEERCACHING_CLIENT = 1
BG_JOB_ENABLE_PEERCACHING_SERVER = 2
BG_JOB_DISABLE_BRANCH_CACHE = 4
BITS_COST_STATE_UNRESTRICTED = 1
BITS_COST_STATE_CAPPED_USAGE_UNKNOWN = 2
BITS_COST_STATE_BELOW_CAP = 4
BITS_COST_STATE_NEAR_CAP = 8
BITS_COST_STATE_OVERCAP_CHARGED = 16
BITS_COST_STATE_OVERCAP_THROTTLED = 32
BITS_COST_STATE_USAGE_BASED = 64
BITS_COST_STATE_ROAMING = 128
BITS_COST_OPTION_IGNORE_CONGESTION = 2147483648
BITS_COST_STATE_RESERVED = 1073741824
QM_NOTIFY_FILE_DONE = 1
QM_NOTIFY_JOB_DONE = 2
QM_NOTIFY_GROUP_DONE = 4
QM_NOTIFY_DISABLE_NOTIFY = 64
QM_NOTIFY_USE_PROGRESSEX = 128
QM_STATUS_FILE_COMPLETE = 1
QM_STATUS_FILE_INCOMPLETE = 2
QM_STATUS_JOB_COMPLETE = 4
QM_STATUS_JOB_INCOMPLETE = 8
QM_STATUS_JOB_ERROR = 16
QM_STATUS_JOB_FOREGROUND = 32
QM_STATUS_GROUP_COMPLETE = 64
QM_STATUS_GROUP_INCOMPLETE = 128
QM_STATUS_GROUP_SUSPENDED = 256
QM_STATUS_GROUP_ERROR = 512
QM_STATUS_GROUP_FOREGROUND = 1024
QM_PROTOCOL_HTTP = 1
QM_PROTOCOL_FTP = 2
QM_PROTOCOL_SMB = 3
QM_PROTOCOL_CUSTOM = 4
QM_PROGRESS_PERCENT_DONE = 1
QM_PROGRESS_TIME_DONE = 2
QM_PROGRESS_SIZE_DONE = 3
QM_E_INVALID_STATE = 2164264961
QM_E_SERVICE_UNAVAILABLE = 2164264962
QM_E_DOWNLOADER_UNAVAILABLE = 2164264963
QM_E_ITEM_NOT_FOUND = 2164264964
BG_E_NOT_FOUND = -2145386495
BG_E_INVALID_STATE = -2145386494
BG_E_EMPTY = -2145386493
BG_E_FILE_NOT_AVAILABLE = -2145386492
BG_E_PROTOCOL_NOT_AVAILABLE = -2145386491
BG_S_ERROR_CONTEXT_NONE = 2097158
BG_E_ERROR_CONTEXT_UNKNOWN = -2145386489
BG_E_ERROR_CONTEXT_GENERAL_QUEUE_MANAGER = -2145386488
BG_E_ERROR_CONTEXT_LOCAL_FILE = -2145386487
BG_E_ERROR_CONTEXT_REMOTE_FILE = -2145386486
BG_E_ERROR_CONTEXT_GENERAL_TRANSPORT = -2145386485
BG_E_ERROR_CONTEXT_QUEUE_MANAGER_NOTIFICATION = -2145386484
BG_E_DESTINATION_LOCKED = -2145386483
BG_E_VOLUME_CHANGED = -2145386482
BG_E_ERROR_INFORMATION_UNAVAILABLE = -2145386481
BG_E_NETWORK_DISCONNECTED = -2145386480
BG_E_MISSING_FILE_SIZE = -2145386479
BG_E_INSUFFICIENT_HTTP_SUPPORT = -2145386478
BG_E_INSUFFICIENT_RANGE_SUPPORT = -2145386477
BG_E_REMOTE_NOT_SUPPORTED = -2145386476
BG_E_NEW_OWNER_DIFF_MAPPING = -2145386475
BG_E_NEW_OWNER_NO_FILE_ACCESS = -2145386474
BG_S_PARTIAL_COMPLETE = 2097175
BG_E_PROXY_LIST_TOO_LARGE = -2145386472
BG_E_PROXY_BYPASS_LIST_TOO_LARGE = -2145386471
BG_S_UNABLE_TO_DELETE_FILES = 2097178
BG_E_INVALID_SERVER_RESPONSE = -2145386469
BG_E_TOO_MANY_FILES = -2145386468
BG_E_LOCAL_FILE_CHANGED = -2145386467
BG_E_ERROR_CONTEXT_REMOTE_APPLICATION = -2145386466
BG_E_SESSION_NOT_FOUND = -2145386465
BG_E_TOO_LARGE = -2145386464
BG_E_STRING_TOO_LONG = -2145386463
BG_E_CLIENT_SERVER_PROTOCOL_MISMATCH = -2145386462
BG_E_SERVER_EXECUTE_ENABLE = -2145386461
BG_E_NO_PROGRESS = -2145386460
BG_E_USERNAME_TOO_LARGE = -2145386459
BG_E_PASSWORD_TOO_LARGE = -2145386458
BG_E_INVALID_AUTH_TARGET = -2145386457
BG_E_INVALID_AUTH_SCHEME = -2145386456
BG_E_FILE_NOT_FOUND = -2145386455
BG_S_PROXY_CHANGED = 2097194
BG_E_INVALID_RANGE = -2145386453
BG_E_OVERLAPPING_RANGES = -2145386452
BG_E_CONNECT_FAILURE = -2145386451
BG_E_CONNECTION_CLOSED = -2145386450
BG_E_BLOCKED_BY_POLICY = -2145386434
BG_E_INVALID_PROXY_INFO = -2145386433
BG_E_INVALID_CREDENTIALS = -2145386432
BG_E_INVALID_HASH_ALGORITHM = -2145386431
BG_E_RECORD_DELETED = -2145386430
BG_E_COMMIT_IN_PROGRESS = -2145386429
BG_E_DISCOVERY_IN_PROGRESS = -2145386428
BG_E_UPNP_ERROR = -2145386427
BG_E_TEST_OPTION_BLOCKED_DOWNLOAD = -2145386426
BG_E_PEERCACHING_DISABLED = -2145386425
BG_E_BUSYCACHERECORD = -2145386424
BG_E_TOO_MANY_JOBS_PER_USER = -2145386423
BG_E_TOO_MANY_JOBS_PER_MACHINE = -2145386416
BG_E_TOO_MANY_FILES_IN_JOB = -2145386415
BG_E_TOO_MANY_RANGES_IN_FILE = -2145386414
BG_E_VALIDATION_FAILED = -2145386413
BG_E_MAXDOWNLOAD_TIMEOUT = -2145386412
BG_S_OVERRIDDEN_BY_POLICY = 2097237
BG_E_TOKEN_REQUIRED = -2145386410
BG_E_UNKNOWN_PROPERTY_ID = -2145386409
BG_E_READ_ONLY_PROPERTY = -2145386408
BG_E_BLOCKED_BY_COST_TRANSFER_POLICY = -2145386407
BG_E_PROPERTY_SUPPORTED_FOR_DOWNLOAD_JOBS_ONLY = -2145386400
BG_E_READ_ONLY_PROPERTY_AFTER_ADDFILE = -2145386399
BG_E_READ_ONLY_PROPERTY_AFTER_RESUME = -2145386398
BG_E_MAX_DOWNLOAD_SIZE_INVALID_VALUE = -2145386397
BG_E_MAX_DOWNLOAD_SIZE_LIMIT_REACHED = -2145386396
BG_E_STANDBY_MODE = -2145386395
BG_E_USE_STORED_CREDENTIALS_NOT_SUPPORTED = -2145386394
BG_E_BLOCKED_BY_BATTERY_POLICY = -2145386393
BG_E_BLOCKED_BY_BATTERY_SAVER = -2145386392
BG_E_WATCHDOG_TIMEOUT = -2145386391
BG_E_APP_PACKAGE_NOT_FOUND = -2145386390
BG_E_APP_PACKAGE_SCENARIO_NOT_SUPPORTED = -2145386389
BG_E_DATABASE_CORRUPT = -2145386388
BG_E_RANDOM_ACCESS_NOT_SUPPORTED = -2145386387
BG_E_BLOCKED_BY_BACKGROUND_ACCESS_POLICY = -2145386386
BG_E_BLOCKED_BY_GAME_MODE = -2145386385
BG_E_BLOCKED_BY_SYSTEM_POLICY = -2145386384
BG_E_NOT_SUPPORTED_WITH_CUSTOM_HTTP_METHOD = -2145386383
BG_E_UNSUPPORTED_JOB_CONFIGURATION = -2145386382
BG_E_REMOTE_FILE_CHANGED = -2145386381
BG_E_SERVER_CERT_VALIDATION_INTERFACE_REQUIRED = -2145386380
BG_E_READ_ONLY_WHEN_JOB_ACTIVE = -2145386379
BG_E_ERROR_CONTEXT_SERVER_CERTIFICATE_CALLBACK = -2145386378
BG_E_HTTP_ERROR_100 = -2145845148
BG_E_HTTP_ERROR_101 = -2145845147
BG_E_HTTP_ERROR_200 = -2145845048
BG_E_HTTP_ERROR_201 = -2145845047
BG_E_HTTP_ERROR_202 = -2145845046
BG_E_HTTP_ERROR_203 = -2145845045
BG_E_HTTP_ERROR_204 = -2145845044
BG_E_HTTP_ERROR_205 = -2145845043
BG_E_HTTP_ERROR_206 = -2145845042
BG_E_HTTP_ERROR_300 = -2145844948
BG_E_HTTP_ERROR_301 = -2145844947
BG_E_HTTP_ERROR_302 = -2145844946
BG_E_HTTP_ERROR_303 = -2145844945
BG_E_HTTP_ERROR_304 = -2145844944
BG_E_HTTP_ERROR_305 = -2145844943
BG_E_HTTP_ERROR_307 = -2145844941
BG_E_HTTP_ERROR_400 = -2145844848
BG_E_HTTP_ERROR_401 = -2145844847
BG_E_HTTP_ERROR_402 = -2145844846
BG_E_HTTP_ERROR_403 = -2145844845
BG_E_HTTP_ERROR_404 = -2145844844
BG_E_HTTP_ERROR_405 = -2145844843
BG_E_HTTP_ERROR_406 = -2145844842
BG_E_HTTP_ERROR_407 = -2145844841
BG_E_HTTP_ERROR_408 = -2145844840
BG_E_HTTP_ERROR_409 = -2145844839
BG_E_HTTP_ERROR_410 = -2145844838
BG_E_HTTP_ERROR_411 = -2145844837
BG_E_HTTP_ERROR_412 = -2145844836
BG_E_HTTP_ERROR_413 = -2145844835
BG_E_HTTP_ERROR_414 = -2145844834
BG_E_HTTP_ERROR_415 = -2145844833
BG_E_HTTP_ERROR_416 = -2145844832
BG_E_HTTP_ERROR_417 = -2145844831
BG_E_HTTP_ERROR_449 = -2145844799
BG_E_HTTP_ERROR_500 = -2145844748
BG_E_HTTP_ERROR_501 = -2145844747
BG_E_HTTP_ERROR_502 = -2145844746
BG_E_HTTP_ERROR_503 = -2145844745
BG_E_HTTP_ERROR_504 = -2145844744
BG_E_HTTP_ERROR_505 = -2145844743
BITS_MC_JOB_CANCELLED = -2145828864
BITS_MC_FILE_DELETION_FAILED = -2145828863
BITS_MC_FILE_DELETION_FAILED_MORE = -2145828862
BITS_MC_JOB_PROPERTY_CHANGE = -2145828861
BITS_MC_JOB_TAKE_OWNERSHIP = -2145828860
BITS_MC_JOB_SCAVENGED = -2145828859
BITS_MC_JOB_NOTIFICATION_FAILURE = -2145828858
BITS_MC_STATE_FILE_CORRUPT = -2145828857
BITS_MC_FAILED_TO_START = -2145828856
BITS_MC_FATAL_IGD_ERROR = -2145828855
BITS_MC_PEERCACHING_PORT = -2145828854
BITS_MC_WSD_PORT = -2145828853
BG_TOKEN = UInt32
BG_TOKEN_LOCAL_FILE = 1
BG_TOKEN_NETWORK = 2
BackgroundCopyManager = Guid('4991d34b-80a1-4291-83b6-3328366b9097')
def _define_BG_FILE_PROGRESS_head():
    class BG_FILE_PROGRESS(Structure):
        pass
    return BG_FILE_PROGRESS
def _define_BG_FILE_PROGRESS():
    BG_FILE_PROGRESS = win32more.Networking.BackgroundIntelligentTransferService.BG_FILE_PROGRESS_head
    BG_FILE_PROGRESS._fields_ = [
        ("BytesTotal", UInt64),
        ("BytesTransferred", UInt64),
        ("Completed", win32more.Foundation.BOOL),
    ]
    return BG_FILE_PROGRESS
def _define_IBackgroundCopyFile_head():
    class IBackgroundCopyFile(win32more.System.Com.IUnknown_head):
        Guid = Guid('01b7bd23-fb88-4a77-8490-5891d3e4653a')
    return IBackgroundCopyFile
def _define_IBackgroundCopyFile():
    IBackgroundCopyFile = win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile_head
    IBackgroundCopyFile.GetRemoteName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(3, 'GetRemoteName', ((1, 'pVal'),)))
    IBackgroundCopyFile.GetLocalName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(4, 'GetLocalName', ((1, 'pVal'),)))
    IBackgroundCopyFile.GetProgress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.BackgroundIntelligentTransferService.BG_FILE_PROGRESS_head), use_last_error=False)(5, 'GetProgress', ((1, 'pVal'),)))
    win32more.System.Com.IUnknown
    return IBackgroundCopyFile
def _define_IEnumBackgroundCopyFiles_head():
    class IEnumBackgroundCopyFiles(win32more.System.Com.IUnknown_head):
        Guid = Guid('ca51e165-c365-424c-8d41-24aaa4ff3c40')
    return IEnumBackgroundCopyFiles
def _define_IEnumBackgroundCopyFiles():
    IEnumBackgroundCopyFiles = win32more.Networking.BackgroundIntelligentTransferService.IEnumBackgroundCopyFiles_head
    IEnumBackgroundCopyFiles.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile_head),POINTER(UInt32), use_last_error=False)(3, 'Next', ((1, 'celt'),(1, 'rgelt'),(1, 'pceltFetched'),)))
    IEnumBackgroundCopyFiles.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'Skip', ((1, 'celt'),)))
    IEnumBackgroundCopyFiles.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumBackgroundCopyFiles.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.BackgroundIntelligentTransferService.IEnumBackgroundCopyFiles_head), use_last_error=False)(6, 'Clone', ((1, 'ppenum'),)))
    IEnumBackgroundCopyFiles.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(7, 'GetCount', ((1, 'puCount'),)))
    win32more.System.Com.IUnknown
    return IEnumBackgroundCopyFiles
BG_ERROR_CONTEXT = Int32
BG_ERROR_CONTEXT_NONE = 0
BG_ERROR_CONTEXT_UNKNOWN = 1
BG_ERROR_CONTEXT_GENERAL_QUEUE_MANAGER = 2
BG_ERROR_CONTEXT_QUEUE_MANAGER_NOTIFICATION = 3
BG_ERROR_CONTEXT_LOCAL_FILE = 4
BG_ERROR_CONTEXT_REMOTE_FILE = 5
BG_ERROR_CONTEXT_GENERAL_TRANSPORT = 6
BG_ERROR_CONTEXT_REMOTE_APPLICATION = 7
BG_ERROR_CONTEXT_SERVER_CERTIFICATE_CALLBACK = 8
def _define_IBackgroundCopyError_head():
    class IBackgroundCopyError(win32more.System.Com.IUnknown_head):
        Guid = Guid('19c613a0-fcb8-4f28-81ae-897c3d078f81')
    return IBackgroundCopyError
def _define_IBackgroundCopyError():
    IBackgroundCopyError = win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyError_head
    IBackgroundCopyError.GetError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.BackgroundIntelligentTransferService.BG_ERROR_CONTEXT),POINTER(win32more.Foundation.HRESULT), use_last_error=False)(3, 'GetError', ((1, 'pContext'),(1, 'pCode'),)))
    IBackgroundCopyError.GetFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile_head), use_last_error=False)(4, 'GetFile', ((1, 'pVal'),)))
    IBackgroundCopyError.GetErrorDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(5, 'GetErrorDescription', ((1, 'LanguageId'),(1, 'pErrorDescription'),)))
    IBackgroundCopyError.GetErrorContextDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(6, 'GetErrorContextDescription', ((1, 'LanguageId'),(1, 'pContextDescription'),)))
    IBackgroundCopyError.GetProtocol = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(7, 'GetProtocol', ((1, 'pProtocol'),)))
    win32more.System.Com.IUnknown
    return IBackgroundCopyError
def _define_BG_FILE_INFO_head():
    class BG_FILE_INFO(Structure):
        pass
    return BG_FILE_INFO
def _define_BG_FILE_INFO():
    BG_FILE_INFO = win32more.Networking.BackgroundIntelligentTransferService.BG_FILE_INFO_head
    BG_FILE_INFO._fields_ = [
        ("RemoteName", win32more.Foundation.PWSTR),
        ("LocalName", win32more.Foundation.PWSTR),
    ]
    return BG_FILE_INFO
def _define_BG_JOB_PROGRESS_head():
    class BG_JOB_PROGRESS(Structure):
        pass
    return BG_JOB_PROGRESS
def _define_BG_JOB_PROGRESS():
    BG_JOB_PROGRESS = win32more.Networking.BackgroundIntelligentTransferService.BG_JOB_PROGRESS_head
    BG_JOB_PROGRESS._fields_ = [
        ("BytesTotal", UInt64),
        ("BytesTransferred", UInt64),
        ("FilesTotal", UInt32),
        ("FilesTransferred", UInt32),
    ]
    return BG_JOB_PROGRESS
def _define_BG_JOB_TIMES_head():
    class BG_JOB_TIMES(Structure):
        pass
    return BG_JOB_TIMES
def _define_BG_JOB_TIMES():
    BG_JOB_TIMES = win32more.Networking.BackgroundIntelligentTransferService.BG_JOB_TIMES_head
    BG_JOB_TIMES._fields_ = [
        ("CreationTime", win32more.Foundation.FILETIME),
        ("ModificationTime", win32more.Foundation.FILETIME),
        ("TransferCompletionTime", win32more.Foundation.FILETIME),
    ]
    return BG_JOB_TIMES
BG_JOB_PRIORITY = Int32
BG_JOB_PRIORITY_FOREGROUND = 0
BG_JOB_PRIORITY_HIGH = 1
BG_JOB_PRIORITY_NORMAL = 2
BG_JOB_PRIORITY_LOW = 3
BG_JOB_STATE = Int32
BG_JOB_STATE_QUEUED = 0
BG_JOB_STATE_CONNECTING = 1
BG_JOB_STATE_TRANSFERRING = 2
BG_JOB_STATE_SUSPENDED = 3
BG_JOB_STATE_ERROR = 4
BG_JOB_STATE_TRANSIENT_ERROR = 5
BG_JOB_STATE_TRANSFERRED = 6
BG_JOB_STATE_ACKNOWLEDGED = 7
BG_JOB_STATE_CANCELLED = 8
BG_JOB_TYPE = Int32
BG_JOB_TYPE_DOWNLOAD = 0
BG_JOB_TYPE_UPLOAD = 1
BG_JOB_TYPE_UPLOAD_REPLY = 2
BG_JOB_PROXY_USAGE = Int32
BG_JOB_PROXY_USAGE_PRECONFIG = 0
BG_JOB_PROXY_USAGE_NO_PROXY = 1
BG_JOB_PROXY_USAGE_OVERRIDE = 2
BG_JOB_PROXY_USAGE_AUTODETECT = 3
def _define_IBackgroundCopyJob_head():
    class IBackgroundCopyJob(win32more.System.Com.IUnknown_head):
        Guid = Guid('37668d37-507e-4160-9316-26306d150b12')
    return IBackgroundCopyJob
def _define_IBackgroundCopyJob():
    IBackgroundCopyJob = win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob_head
    IBackgroundCopyJob.AddFileSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Networking.BackgroundIntelligentTransferService.BG_FILE_INFO), use_last_error=False)(3, 'AddFileSet', ((1, 'cFileCount'),(1, 'pFileSet'),)))
    IBackgroundCopyJob.AddFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(4, 'AddFile', ((1, 'RemoteUrl'),(1, 'LocalName'),)))
    IBackgroundCopyJob.EnumFiles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.BackgroundIntelligentTransferService.IEnumBackgroundCopyFiles_head), use_last_error=False)(5, 'EnumFiles', ((1, 'pEnum'),)))
    IBackgroundCopyJob.Suspend = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(6, 'Suspend', ()))
    IBackgroundCopyJob.Resume = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'Resume', ()))
    IBackgroundCopyJob.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'Cancel', ()))
    IBackgroundCopyJob.Complete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(9, 'Complete', ()))
    IBackgroundCopyJob.GetId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(10, 'GetId', ((1, 'pVal'),)))
    IBackgroundCopyJob.GetType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.BackgroundIntelligentTransferService.BG_JOB_TYPE), use_last_error=False)(11, 'GetType', ((1, 'pVal'),)))
    IBackgroundCopyJob.GetProgress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.BackgroundIntelligentTransferService.BG_JOB_PROGRESS_head), use_last_error=False)(12, 'GetProgress', ((1, 'pVal'),)))
    IBackgroundCopyJob.GetTimes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.BackgroundIntelligentTransferService.BG_JOB_TIMES_head), use_last_error=False)(13, 'GetTimes', ((1, 'pVal'),)))
    IBackgroundCopyJob.GetState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.BackgroundIntelligentTransferService.BG_JOB_STATE), use_last_error=False)(14, 'GetState', ((1, 'pVal'),)))
    IBackgroundCopyJob.GetError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyError_head), use_last_error=False)(15, 'GetError', ((1, 'ppError'),)))
    IBackgroundCopyJob.GetOwner = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(16, 'GetOwner', ((1, 'pVal'),)))
    IBackgroundCopyJob.SetDisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(17, 'SetDisplayName', ((1, 'Val'),)))
    IBackgroundCopyJob.GetDisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(18, 'GetDisplayName', ((1, 'pVal'),)))
    IBackgroundCopyJob.SetDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(19, 'SetDescription', ((1, 'Val'),)))
    IBackgroundCopyJob.GetDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(20, 'GetDescription', ((1, 'pVal'),)))
    IBackgroundCopyJob.SetPriority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.BackgroundIntelligentTransferService.BG_JOB_PRIORITY, use_last_error=False)(21, 'SetPriority', ((1, 'Val'),)))
    IBackgroundCopyJob.GetPriority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.BackgroundIntelligentTransferService.BG_JOB_PRIORITY), use_last_error=False)(22, 'GetPriority', ((1, 'pVal'),)))
    IBackgroundCopyJob.SetNotifyFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(23, 'SetNotifyFlags', ((1, 'Val'),)))
    IBackgroundCopyJob.GetNotifyFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(24, 'GetNotifyFlags', ((1, 'pVal'),)))
    IBackgroundCopyJob.SetNotifyInterface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)(25, 'SetNotifyInterface', ((1, 'Val'),)))
    IBackgroundCopyJob.GetNotifyInterface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(26, 'GetNotifyInterface', ((1, 'pVal'),)))
    IBackgroundCopyJob.SetMinimumRetryDelay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(27, 'SetMinimumRetryDelay', ((1, 'Seconds'),)))
    IBackgroundCopyJob.GetMinimumRetryDelay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(28, 'GetMinimumRetryDelay', ((1, 'Seconds'),)))
    IBackgroundCopyJob.SetNoProgressTimeout = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(29, 'SetNoProgressTimeout', ((1, 'Seconds'),)))
    IBackgroundCopyJob.GetNoProgressTimeout = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(30, 'GetNoProgressTimeout', ((1, 'Seconds'),)))
    IBackgroundCopyJob.GetErrorCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(31, 'GetErrorCount', ((1, 'Errors'),)))
    IBackgroundCopyJob.SetProxySettings = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.BackgroundIntelligentTransferService.BG_JOB_PROXY_USAGE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(32, 'SetProxySettings', ((1, 'ProxyUsage'),(1, 'ProxyList'),(1, 'ProxyBypassList'),)))
    IBackgroundCopyJob.GetProxySettings = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.BackgroundIntelligentTransferService.BG_JOB_PROXY_USAGE),POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(33, 'GetProxySettings', ((1, 'pProxyUsage'),(1, 'pProxyList'),(1, 'pProxyBypassList'),)))
    IBackgroundCopyJob.TakeOwnership = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(34, 'TakeOwnership', ()))
    win32more.System.Com.IUnknown
    return IBackgroundCopyJob
def _define_IEnumBackgroundCopyJobs_head():
    class IEnumBackgroundCopyJobs(win32more.System.Com.IUnknown_head):
        Guid = Guid('1af4f612-3b71-466f-8f58-7b6f73ac57ad')
    return IEnumBackgroundCopyJobs
def _define_IEnumBackgroundCopyJobs():
    IEnumBackgroundCopyJobs = win32more.Networking.BackgroundIntelligentTransferService.IEnumBackgroundCopyJobs_head
    IEnumBackgroundCopyJobs.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob_head),POINTER(UInt32), use_last_error=False)(3, 'Next', ((1, 'celt'),(1, 'rgelt'),(1, 'pceltFetched'),)))
    IEnumBackgroundCopyJobs.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'Skip', ((1, 'celt'),)))
    IEnumBackgroundCopyJobs.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumBackgroundCopyJobs.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.BackgroundIntelligentTransferService.IEnumBackgroundCopyJobs_head), use_last_error=False)(6, 'Clone', ((1, 'ppenum'),)))
    IEnumBackgroundCopyJobs.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(7, 'GetCount', ((1, 'puCount'),)))
    win32more.System.Com.IUnknown
    return IEnumBackgroundCopyJobs
def _define_IBackgroundCopyCallback_head():
    class IBackgroundCopyCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('97ea99c7-0186-4ad4-8df9-c5b4e0ed6b22')
    return IBackgroundCopyCallback
def _define_IBackgroundCopyCallback():
    IBackgroundCopyCallback = win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyCallback_head
    IBackgroundCopyCallback.JobTransferred = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob_head, use_last_error=False)(3, 'JobTransferred', ((1, 'pJob'),)))
    IBackgroundCopyCallback.JobError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob_head,win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyError_head, use_last_error=False)(4, 'JobError', ((1, 'pJob'),(1, 'pError'),)))
    IBackgroundCopyCallback.JobModification = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob_head,UInt32, use_last_error=False)(5, 'JobModification', ((1, 'pJob'),(1, 'dwReserved'),)))
    win32more.System.Com.IUnknown
    return IBackgroundCopyCallback
def _define_AsyncIBackgroundCopyCallback_head():
    class AsyncIBackgroundCopyCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('ca29d251-b4bb-4679-a3d9-ae8006119d54')
    return AsyncIBackgroundCopyCallback
def _define_AsyncIBackgroundCopyCallback():
    AsyncIBackgroundCopyCallback = win32more.Networking.BackgroundIntelligentTransferService.AsyncIBackgroundCopyCallback_head
    AsyncIBackgroundCopyCallback.Begin_JobTransferred = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob_head, use_last_error=False)(3, 'Begin_JobTransferred', ((1, 'pJob'),)))
    AsyncIBackgroundCopyCallback.Finish_JobTransferred = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Finish_JobTransferred', ()))
    AsyncIBackgroundCopyCallback.Begin_JobError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob_head,win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyError_head, use_last_error=False)(5, 'Begin_JobError', ((1, 'pJob'),(1, 'pError'),)))
    AsyncIBackgroundCopyCallback.Finish_JobError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(6, 'Finish_JobError', ()))
    AsyncIBackgroundCopyCallback.Begin_JobModification = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob_head,UInt32, use_last_error=False)(7, 'Begin_JobModification', ((1, 'pJob'),(1, 'dwReserved'),)))
    AsyncIBackgroundCopyCallback.Finish_JobModification = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'Finish_JobModification', ()))
    win32more.System.Com.IUnknown
    return AsyncIBackgroundCopyCallback
def _define_IBackgroundCopyManager_head():
    class IBackgroundCopyManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('5ce34c0d-0dc9-4c1f-897c-daa1b78cee7c')
    return IBackgroundCopyManager
def _define_IBackgroundCopyManager():
    IBackgroundCopyManager = win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyManager_head
    IBackgroundCopyManager.CreateJob = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Networking.BackgroundIntelligentTransferService.BG_JOB_TYPE,POINTER(Guid),POINTER(win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob_head), use_last_error=False)(3, 'CreateJob', ((1, 'DisplayName'),(1, 'Type'),(1, 'pJobId'),(1, 'ppJob'),)))
    IBackgroundCopyManager.GetJob = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob_head), use_last_error=False)(4, 'GetJob', ((1, 'jobID'),(1, 'ppJob'),)))
    IBackgroundCopyManager.EnumJobs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Networking.BackgroundIntelligentTransferService.IEnumBackgroundCopyJobs_head), use_last_error=False)(5, 'EnumJobs', ((1, 'dwFlags'),(1, 'ppEnum'),)))
    IBackgroundCopyManager.GetErrorDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(6, 'GetErrorDescription', ((1, 'hResult'),(1, 'LanguageId'),(1, 'pErrorDescription'),)))
    win32more.System.Com.IUnknown
    return IBackgroundCopyManager
BackgroundCopyManager1_5 = Guid('f087771f-d74f-4c1a-bb8a-e16aca9124ea')
def _define_BG_JOB_REPLY_PROGRESS_head():
    class BG_JOB_REPLY_PROGRESS(Structure):
        pass
    return BG_JOB_REPLY_PROGRESS
def _define_BG_JOB_REPLY_PROGRESS():
    BG_JOB_REPLY_PROGRESS = win32more.Networking.BackgroundIntelligentTransferService.BG_JOB_REPLY_PROGRESS_head
    BG_JOB_REPLY_PROGRESS._fields_ = [
        ("BytesTotal", UInt64),
        ("BytesTransferred", UInt64),
    ]
    return BG_JOB_REPLY_PROGRESS
BG_AUTH_TARGET = Int32
BG_AUTH_TARGET_SERVER = 1
BG_AUTH_TARGET_PROXY = 2
BG_AUTH_SCHEME = Int32
BG_AUTH_SCHEME_BASIC = 1
BG_AUTH_SCHEME_DIGEST = 2
BG_AUTH_SCHEME_NTLM = 3
BG_AUTH_SCHEME_NEGOTIATE = 4
BG_AUTH_SCHEME_PASSPORT = 5
def _define_BG_BASIC_CREDENTIALS_head():
    class BG_BASIC_CREDENTIALS(Structure):
        pass
    return BG_BASIC_CREDENTIALS
def _define_BG_BASIC_CREDENTIALS():
    BG_BASIC_CREDENTIALS = win32more.Networking.BackgroundIntelligentTransferService.BG_BASIC_CREDENTIALS_head
    BG_BASIC_CREDENTIALS._fields_ = [
        ("UserName", win32more.Foundation.PWSTR),
        ("Password", win32more.Foundation.PWSTR),
    ]
    return BG_BASIC_CREDENTIALS
def _define_BG_AUTH_CREDENTIALS_UNION_head():
    class BG_AUTH_CREDENTIALS_UNION(Union):
        pass
    return BG_AUTH_CREDENTIALS_UNION
def _define_BG_AUTH_CREDENTIALS_UNION():
    BG_AUTH_CREDENTIALS_UNION = win32more.Networking.BackgroundIntelligentTransferService.BG_AUTH_CREDENTIALS_UNION_head
    BG_AUTH_CREDENTIALS_UNION._fields_ = [
        ("Basic", win32more.Networking.BackgroundIntelligentTransferService.BG_BASIC_CREDENTIALS),
    ]
    return BG_AUTH_CREDENTIALS_UNION
def _define_BG_AUTH_CREDENTIALS_head():
    class BG_AUTH_CREDENTIALS(Structure):
        pass
    return BG_AUTH_CREDENTIALS
def _define_BG_AUTH_CREDENTIALS():
    BG_AUTH_CREDENTIALS = win32more.Networking.BackgroundIntelligentTransferService.BG_AUTH_CREDENTIALS_head
    BG_AUTH_CREDENTIALS._fields_ = [
        ("Target", win32more.Networking.BackgroundIntelligentTransferService.BG_AUTH_TARGET),
        ("Scheme", win32more.Networking.BackgroundIntelligentTransferService.BG_AUTH_SCHEME),
        ("Credentials", win32more.Networking.BackgroundIntelligentTransferService.BG_AUTH_CREDENTIALS_UNION),
    ]
    return BG_AUTH_CREDENTIALS
def _define_IBackgroundCopyJob2_head():
    class IBackgroundCopyJob2(win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob_head):
        Guid = Guid('54b50739-686f-45eb-9dff-d6a9a0faa9af')
    return IBackgroundCopyJob2
def _define_IBackgroundCopyJob2():
    IBackgroundCopyJob2 = win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob2_head
    IBackgroundCopyJob2.SetNotifyCmdLine = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(35, 'SetNotifyCmdLine', ((1, 'Program'),(1, 'Parameters'),)))
    IBackgroundCopyJob2.GetNotifyCmdLine = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(36, 'GetNotifyCmdLine', ((1, 'pProgram'),(1, 'pParameters'),)))
    IBackgroundCopyJob2.GetReplyProgress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.BackgroundIntelligentTransferService.BG_JOB_REPLY_PROGRESS_head), use_last_error=False)(37, 'GetReplyProgress', ((1, 'pProgress'),)))
    IBackgroundCopyJob2.GetReplyData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(c_char_p_no),POINTER(UInt64), use_last_error=False)(38, 'GetReplyData', ((1, 'ppBuffer'),(1, 'pLength'),)))
    IBackgroundCopyJob2.SetReplyFileName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(39, 'SetReplyFileName', ((1, 'ReplyFileName'),)))
    IBackgroundCopyJob2.GetReplyFileName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(40, 'GetReplyFileName', ((1, 'pReplyFileName'),)))
    IBackgroundCopyJob2.SetCredentials = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.BackgroundIntelligentTransferService.BG_AUTH_CREDENTIALS_head), use_last_error=False)(41, 'SetCredentials', ((1, 'credentials'),)))
    IBackgroundCopyJob2.RemoveCredentials = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.BackgroundIntelligentTransferService.BG_AUTH_TARGET,win32more.Networking.BackgroundIntelligentTransferService.BG_AUTH_SCHEME, use_last_error=False)(42, 'RemoveCredentials', ((1, 'Target'),(1, 'Scheme'),)))
    win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob
    return IBackgroundCopyJob2
BackgroundCopyManager2_0 = Guid('6d18ad12-bde3-4393-b311-099c346e6df9')
def _define_BG_FILE_RANGE_head():
    class BG_FILE_RANGE(Structure):
        pass
    return BG_FILE_RANGE
def _define_BG_FILE_RANGE():
    BG_FILE_RANGE = win32more.Networking.BackgroundIntelligentTransferService.BG_FILE_RANGE_head
    BG_FILE_RANGE._fields_ = [
        ("InitialOffset", UInt64),
        ("Length", UInt64),
    ]
    return BG_FILE_RANGE
def _define_IBackgroundCopyJob3_head():
    class IBackgroundCopyJob3(win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob2_head):
        Guid = Guid('443c8934-90ff-48ed-bcde-26f5c7450042')
    return IBackgroundCopyJob3
def _define_IBackgroundCopyJob3():
    IBackgroundCopyJob3 = win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob3_head
    IBackgroundCopyJob3.ReplaceRemotePrefix = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(43, 'ReplaceRemotePrefix', ((1, 'OldPrefix'),(1, 'NewPrefix'),)))
    IBackgroundCopyJob3.AddFileWithRanges = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Networking.BackgroundIntelligentTransferService.BG_FILE_RANGE), use_last_error=False)(44, 'AddFileWithRanges', ((1, 'RemoteUrl'),(1, 'LocalName'),(1, 'RangeCount'),(1, 'Ranges'),)))
    IBackgroundCopyJob3.SetFileACLFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(45, 'SetFileACLFlags', ((1, 'Flags'),)))
    IBackgroundCopyJob3.GetFileACLFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(46, 'GetFileACLFlags', ((1, 'Flags'),)))
    win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob2
    return IBackgroundCopyJob3
def _define_IBackgroundCopyFile2_head():
    class IBackgroundCopyFile2(win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile_head):
        Guid = Guid('83e81b93-0873-474d-8a8c-f2018b1a939c')
    return IBackgroundCopyFile2
def _define_IBackgroundCopyFile2():
    IBackgroundCopyFile2 = win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile2_head
    IBackgroundCopyFile2.GetFileRanges = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(POINTER(win32more.Networking.BackgroundIntelligentTransferService.BG_FILE_RANGE_head)), use_last_error=False)(6, 'GetFileRanges', ((1, 'RangeCount'),(1, 'Ranges'),)))
    IBackgroundCopyFile2.SetRemoteName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(7, 'SetRemoteName', ((1, 'Val'),)))
    win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile
    return IBackgroundCopyFile2
BackgroundCopyManager2_5 = Guid('03ca98d6-ff5d-49b8-abc6-03dd84127020')
BG_CERT_STORE_LOCATION = Int32
BG_CERT_STORE_LOCATION_CURRENT_USER = 0
BG_CERT_STORE_LOCATION_LOCAL_MACHINE = 1
BG_CERT_STORE_LOCATION_CURRENT_SERVICE = 2
BG_CERT_STORE_LOCATION_SERVICES = 3
BG_CERT_STORE_LOCATION_USERS = 4
BG_CERT_STORE_LOCATION_CURRENT_USER_GROUP_POLICY = 5
BG_CERT_STORE_LOCATION_LOCAL_MACHINE_GROUP_POLICY = 6
BG_CERT_STORE_LOCATION_LOCAL_MACHINE_ENTERPRISE = 7
def _define_IBackgroundCopyJobHttpOptions_head():
    class IBackgroundCopyJobHttpOptions(win32more.System.Com.IUnknown_head):
        Guid = Guid('f1bd1079-9f01-4bdc-8036-f09b70095066')
    return IBackgroundCopyJobHttpOptions
def _define_IBackgroundCopyJobHttpOptions():
    IBackgroundCopyJobHttpOptions = win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJobHttpOptions_head
    IBackgroundCopyJobHttpOptions.SetClientCertificateByID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.BackgroundIntelligentTransferService.BG_CERT_STORE_LOCATION,win32more.Foundation.PWSTR,POINTER(Byte), use_last_error=False)(3, 'SetClientCertificateByID', ((1, 'StoreLocation'),(1, 'StoreName'),(1, 'pCertHashBlob'),)))
    IBackgroundCopyJobHttpOptions.SetClientCertificateByName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.BackgroundIntelligentTransferService.BG_CERT_STORE_LOCATION,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(4, 'SetClientCertificateByName', ((1, 'StoreLocation'),(1, 'StoreName'),(1, 'SubjectName'),)))
    IBackgroundCopyJobHttpOptions.RemoveClientCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'RemoveClientCertificate', ()))
    IBackgroundCopyJobHttpOptions.GetClientCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.BackgroundIntelligentTransferService.BG_CERT_STORE_LOCATION),POINTER(win32more.Foundation.PWSTR),POINTER(c_char_p_no),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(6, 'GetClientCertificate', ((1, 'pStoreLocation'),(1, 'pStoreName'),(1, 'ppCertHashBlob'),(1, 'pSubjectName'),)))
    IBackgroundCopyJobHttpOptions.SetCustomHeaders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(7, 'SetCustomHeaders', ((1, 'RequestHeaders'),)))
    IBackgroundCopyJobHttpOptions.GetCustomHeaders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(8, 'GetCustomHeaders', ((1, 'pRequestHeaders'),)))
    IBackgroundCopyJobHttpOptions.SetSecurityFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(9, 'SetSecurityFlags', ((1, 'Flags'),)))
    IBackgroundCopyJobHttpOptions.GetSecurityFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(10, 'GetSecurityFlags', ((1, 'pFlags'),)))
    win32more.System.Com.IUnknown
    return IBackgroundCopyJobHttpOptions
BackgroundCopyManager3_0 = Guid('659cdea7-489e-11d9-a9cd-000d56965251')
def _define_IBitsPeerCacheRecord_head():
    class IBitsPeerCacheRecord(win32more.System.Com.IUnknown_head):
        Guid = Guid('659cdeaf-489e-11d9-a9cd-000d56965251')
    return IBitsPeerCacheRecord
def _define_IBitsPeerCacheRecord():
    IBitsPeerCacheRecord = win32more.Networking.BackgroundIntelligentTransferService.IBitsPeerCacheRecord_head
    IBitsPeerCacheRecord.GetId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(3, 'GetId', ((1, 'pVal'),)))
    IBitsPeerCacheRecord.GetOriginUrl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(4, 'GetOriginUrl', ((1, 'pVal'),)))
    IBitsPeerCacheRecord.GetFileSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64), use_last_error=False)(5, 'GetFileSize', ((1, 'pVal'),)))
    IBitsPeerCacheRecord.GetFileModificationTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.FILETIME_head), use_last_error=False)(6, 'GetFileModificationTime', ((1, 'pVal'),)))
    IBitsPeerCacheRecord.GetLastAccessTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.FILETIME_head), use_last_error=False)(7, 'GetLastAccessTime', ((1, 'pVal'),)))
    IBitsPeerCacheRecord.IsFileValidated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'IsFileValidated', ()))
    IBitsPeerCacheRecord.GetFileRanges = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(POINTER(win32more.Networking.BackgroundIntelligentTransferService.BG_FILE_RANGE_head)), use_last_error=False)(9, 'GetFileRanges', ((1, 'pRangeCount'),(1, 'ppRanges'),)))
    win32more.System.Com.IUnknown
    return IBitsPeerCacheRecord
def _define_IEnumBitsPeerCacheRecords_head():
    class IEnumBitsPeerCacheRecords(win32more.System.Com.IUnknown_head):
        Guid = Guid('659cdea4-489e-11d9-a9cd-000d56965251')
    return IEnumBitsPeerCacheRecords
def _define_IEnumBitsPeerCacheRecords():
    IEnumBitsPeerCacheRecords = win32more.Networking.BackgroundIntelligentTransferService.IEnumBitsPeerCacheRecords_head
    IEnumBitsPeerCacheRecords.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Networking.BackgroundIntelligentTransferService.IBitsPeerCacheRecord_head),POINTER(UInt32), use_last_error=False)(3, 'Next', ((1, 'celt'),(1, 'rgelt'),(1, 'pceltFetched'),)))
    IEnumBitsPeerCacheRecords.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'Skip', ((1, 'celt'),)))
    IEnumBitsPeerCacheRecords.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumBitsPeerCacheRecords.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.BackgroundIntelligentTransferService.IEnumBitsPeerCacheRecords_head), use_last_error=False)(6, 'Clone', ((1, 'ppenum'),)))
    IEnumBitsPeerCacheRecords.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(7, 'GetCount', ((1, 'puCount'),)))
    win32more.System.Com.IUnknown
    return IEnumBitsPeerCacheRecords
def _define_IBitsPeer_head():
    class IBitsPeer(win32more.System.Com.IUnknown_head):
        Guid = Guid('659cdea2-489e-11d9-a9cd-000d56965251')
    return IBitsPeer
def _define_IBitsPeer():
    IBitsPeer = win32more.Networking.BackgroundIntelligentTransferService.IBitsPeer_head
    IBitsPeer.GetPeerName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(3, 'GetPeerName', ((1, 'pName'),)))
    IBitsPeer.IsAuthenticated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'IsAuthenticated', ((1, 'pAuth'),)))
    IBitsPeer.IsAvailable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'IsAvailable', ((1, 'pOnline'),)))
    win32more.System.Com.IUnknown
    return IBitsPeer
def _define_IEnumBitsPeers_head():
    class IEnumBitsPeers(win32more.System.Com.IUnknown_head):
        Guid = Guid('659cdea5-489e-11d9-a9cd-000d56965251')
    return IEnumBitsPeers
def _define_IEnumBitsPeers():
    IEnumBitsPeers = win32more.Networking.BackgroundIntelligentTransferService.IEnumBitsPeers_head
    IEnumBitsPeers.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Networking.BackgroundIntelligentTransferService.IBitsPeer_head),POINTER(UInt32), use_last_error=False)(3, 'Next', ((1, 'celt'),(1, 'rgelt'),(1, 'pceltFetched'),)))
    IEnumBitsPeers.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'Skip', ((1, 'celt'),)))
    IEnumBitsPeers.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumBitsPeers.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.BackgroundIntelligentTransferService.IEnumBitsPeers_head), use_last_error=False)(6, 'Clone', ((1, 'ppenum'),)))
    IEnumBitsPeers.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(7, 'GetCount', ((1, 'puCount'),)))
    win32more.System.Com.IUnknown
    return IEnumBitsPeers
def _define_IBitsPeerCacheAdministration_head():
    class IBitsPeerCacheAdministration(win32more.System.Com.IUnknown_head):
        Guid = Guid('659cdead-489e-11d9-a9cd-000d56965251')
    return IBitsPeerCacheAdministration
def _define_IBitsPeerCacheAdministration():
    IBitsPeerCacheAdministration = win32more.Networking.BackgroundIntelligentTransferService.IBitsPeerCacheAdministration_head
    IBitsPeerCacheAdministration.GetMaximumCacheSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetMaximumCacheSize', ((1, 'pBytes'),)))
    IBitsPeerCacheAdministration.SetMaximumCacheSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'SetMaximumCacheSize', ((1, 'Bytes'),)))
    IBitsPeerCacheAdministration.GetMaximumContentAge = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(5, 'GetMaximumContentAge', ((1, 'pSeconds'),)))
    IBitsPeerCacheAdministration.SetMaximumContentAge = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'SetMaximumContentAge', ((1, 'Seconds'),)))
    IBitsPeerCacheAdministration.GetConfigurationFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(7, 'GetConfigurationFlags', ((1, 'pFlags'),)))
    IBitsPeerCacheAdministration.SetConfigurationFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(8, 'SetConfigurationFlags', ((1, 'Flags'),)))
    IBitsPeerCacheAdministration.EnumRecords = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.BackgroundIntelligentTransferService.IEnumBitsPeerCacheRecords_head), use_last_error=False)(9, 'EnumRecords', ((1, 'ppEnum'),)))
    IBitsPeerCacheAdministration.GetRecord = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Networking.BackgroundIntelligentTransferService.IBitsPeerCacheRecord_head), use_last_error=False)(10, 'GetRecord', ((1, 'id'),(1, 'ppRecord'),)))
    IBitsPeerCacheAdministration.ClearRecords = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(11, 'ClearRecords', ()))
    IBitsPeerCacheAdministration.DeleteRecord = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(12, 'DeleteRecord', ((1, 'id'),)))
    IBitsPeerCacheAdministration.DeleteUrl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(13, 'DeleteUrl', ((1, 'url'),)))
    IBitsPeerCacheAdministration.EnumPeers = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.BackgroundIntelligentTransferService.IEnumBitsPeers_head), use_last_error=False)(14, 'EnumPeers', ((1, 'ppEnum'),)))
    IBitsPeerCacheAdministration.ClearPeers = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(15, 'ClearPeers', ()))
    IBitsPeerCacheAdministration.DiscoverPeers = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(16, 'DiscoverPeers', ()))
    win32more.System.Com.IUnknown
    return IBitsPeerCacheAdministration
def _define_IBackgroundCopyJob4_head():
    class IBackgroundCopyJob4(win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob3_head):
        Guid = Guid('659cdeae-489e-11d9-a9cd-000d56965251')
    return IBackgroundCopyJob4
def _define_IBackgroundCopyJob4():
    IBackgroundCopyJob4 = win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob4_head
    IBackgroundCopyJob4.SetPeerCachingFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(47, 'SetPeerCachingFlags', ((1, 'Flags'),)))
    IBackgroundCopyJob4.GetPeerCachingFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(48, 'GetPeerCachingFlags', ((1, 'pFlags'),)))
    IBackgroundCopyJob4.GetOwnerIntegrityLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(49, 'GetOwnerIntegrityLevel', ((1, 'pLevel'),)))
    IBackgroundCopyJob4.GetOwnerElevationState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(50, 'GetOwnerElevationState', ((1, 'pElevated'),)))
    IBackgroundCopyJob4.SetMaximumDownloadTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(51, 'SetMaximumDownloadTime', ((1, 'Timeout'),)))
    IBackgroundCopyJob4.GetMaximumDownloadTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(52, 'GetMaximumDownloadTime', ((1, 'pTimeout'),)))
    win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob3
    return IBackgroundCopyJob4
def _define_IBackgroundCopyFile3_head():
    class IBackgroundCopyFile3(win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile2_head):
        Guid = Guid('659cdeaa-489e-11d9-a9cd-000d56965251')
    return IBackgroundCopyFile3
def _define_IBackgroundCopyFile3():
    IBackgroundCopyFile3 = win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile3_head
    IBackgroundCopyFile3.GetTemporaryName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(8, 'GetTemporaryName', ((1, 'pFilename'),)))
    IBackgroundCopyFile3.SetValidationState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(9, 'SetValidationState', ((1, 'state'),)))
    IBackgroundCopyFile3.GetValidationState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(10, 'GetValidationState', ((1, 'pState'),)))
    IBackgroundCopyFile3.IsDownloadedFromPeer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(11, 'IsDownloadedFromPeer', ((1, 'pVal'),)))
    win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile2
    return IBackgroundCopyFile3
def _define_IBackgroundCopyCallback2_head():
    class IBackgroundCopyCallback2(win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyCallback_head):
        Guid = Guid('659cdeac-489e-11d9-a9cd-000d56965251')
    return IBackgroundCopyCallback2
def _define_IBackgroundCopyCallback2():
    IBackgroundCopyCallback2 = win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyCallback2_head
    IBackgroundCopyCallback2.FileTransferred = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob_head,win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile_head, use_last_error=False)(6, 'FileTransferred', ((1, 'pJob'),(1, 'pFile'),)))
    win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyCallback
    return IBackgroundCopyCallback2
BackgroundCopyManager4_0 = Guid('bb6df56b-cace-11dc-9992-0019b93a3a84')
def _define_IBitsTokenOptions_head():
    class IBitsTokenOptions(win32more.System.Com.IUnknown_head):
        Guid = Guid('9a2584c3-f7d2-457a-9a5e-22b67bffc7d2')
    return IBitsTokenOptions
def _define_IBitsTokenOptions():
    IBitsTokenOptions = win32more.Networking.BackgroundIntelligentTransferService.IBitsTokenOptions_head
    IBitsTokenOptions.SetHelperTokenFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.BackgroundIntelligentTransferService.BG_TOKEN, use_last_error=False)(3, 'SetHelperTokenFlags', ((1, 'UsageFlags'),)))
    IBitsTokenOptions.GetHelperTokenFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.BackgroundIntelligentTransferService.BG_TOKEN), use_last_error=False)(4, 'GetHelperTokenFlags', ((1, 'pFlags'),)))
    IBitsTokenOptions.SetHelperToken = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'SetHelperToken', ()))
    IBitsTokenOptions.ClearHelperToken = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(6, 'ClearHelperToken', ()))
    IBitsTokenOptions.GetHelperTokenSid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(7, 'GetHelperTokenSid', ((1, 'pSid'),)))
    win32more.System.Com.IUnknown
    return IBitsTokenOptions
def _define_IBackgroundCopyFile4_head():
    class IBackgroundCopyFile4(win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile3_head):
        Guid = Guid('ef7e0655-7888-4960-b0e5-730846e03492')
    return IBackgroundCopyFile4
def _define_IBackgroundCopyFile4():
    IBackgroundCopyFile4 = win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile4_head
    IBackgroundCopyFile4.GetPeerDownloadStats = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64),POINTER(UInt64), use_last_error=False)(12, 'GetPeerDownloadStats', ((1, 'pFromOrigin'),(1, 'pFromPeers'),)))
    win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile3
    return IBackgroundCopyFile4
BackgroundCopyManager5_0 = Guid('1ecca34c-e88a-44e3-8d6a-8921bde9e452')
BITS_JOB_TRANSFER_POLICY = Int32
BITS_JOB_TRANSFER_POLICY_ALWAYS = -2147483393
BITS_JOB_TRANSFER_POLICY_NOT_ROAMING = -2147483521
BITS_JOB_TRANSFER_POLICY_NO_SURCHARGE = -2147483537
BITS_JOB_TRANSFER_POLICY_STANDARD = -2147483545
BITS_JOB_TRANSFER_POLICY_UNRESTRICTED = -2147483615
BITS_JOB_PROPERTY_ID = Int32
BITS_JOB_PROPERTY_ID_COST_FLAGS = 1
BITS_JOB_PROPERTY_NOTIFICATION_CLSID = 2
BITS_JOB_PROPERTY_DYNAMIC_CONTENT = 3
BITS_JOB_PROPERTY_HIGH_PERFORMANCE = 4
BITS_JOB_PROPERTY_MAX_DOWNLOAD_SIZE = 5
BITS_JOB_PROPERTY_USE_STORED_CREDENTIALS = 7
BITS_JOB_PROPERTY_MINIMUM_NOTIFICATION_INTERVAL_MS = 9
BITS_JOB_PROPERTY_ON_DEMAND_MODE = 10
def _define_BITS_JOB_PROPERTY_VALUE_head():
    class BITS_JOB_PROPERTY_VALUE(Union):
        pass
    return BITS_JOB_PROPERTY_VALUE
def _define_BITS_JOB_PROPERTY_VALUE():
    BITS_JOB_PROPERTY_VALUE = win32more.Networking.BackgroundIntelligentTransferService.BITS_JOB_PROPERTY_VALUE_head
    BITS_JOB_PROPERTY_VALUE._fields_ = [
        ("Dword", UInt32),
        ("ClsID", Guid),
        ("Enable", win32more.Foundation.BOOL),
        ("Uint64", UInt64),
        ("Target", win32more.Networking.BackgroundIntelligentTransferService.BG_AUTH_TARGET),
    ]
    return BITS_JOB_PROPERTY_VALUE
BITS_FILE_PROPERTY_ID = Int32
BITS_FILE_PROPERTY_ID_HTTP_RESPONSE_HEADERS = 1
def _define_BITS_FILE_PROPERTY_VALUE_head():
    class BITS_FILE_PROPERTY_VALUE(Union):
        pass
    return BITS_FILE_PROPERTY_VALUE
def _define_BITS_FILE_PROPERTY_VALUE():
    BITS_FILE_PROPERTY_VALUE = win32more.Networking.BackgroundIntelligentTransferService.BITS_FILE_PROPERTY_VALUE_head
    BITS_FILE_PROPERTY_VALUE._fields_ = [
        ("String", win32more.Foundation.PWSTR),
    ]
    return BITS_FILE_PROPERTY_VALUE
def _define_IBackgroundCopyJob5_head():
    class IBackgroundCopyJob5(win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob4_head):
        Guid = Guid('e847030c-bbba-4657-af6d-484aa42bf1fe')
    return IBackgroundCopyJob5
def _define_IBackgroundCopyJob5():
    IBackgroundCopyJob5 = win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob5_head
    IBackgroundCopyJob5.SetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.BackgroundIntelligentTransferService.BITS_JOB_PROPERTY_ID,win32more.Networking.BackgroundIntelligentTransferService.BITS_JOB_PROPERTY_VALUE, use_last_error=False)(53, 'SetProperty', ((1, 'PropertyId'),(1, 'PropertyValue'),)))
    IBackgroundCopyJob5.GetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.BackgroundIntelligentTransferService.BITS_JOB_PROPERTY_ID,POINTER(win32more.Networking.BackgroundIntelligentTransferService.BITS_JOB_PROPERTY_VALUE_head), use_last_error=False)(54, 'GetProperty', ((1, 'PropertyId'),(1, 'PropertyValue'),)))
    win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob4
    return IBackgroundCopyJob5
def _define_IBackgroundCopyFile5_head():
    class IBackgroundCopyFile5(win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile4_head):
        Guid = Guid('85c1657f-dafc-40e8-8834-df18ea25717e')
    return IBackgroundCopyFile5
def _define_IBackgroundCopyFile5():
    IBackgroundCopyFile5 = win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile5_head
    IBackgroundCopyFile5.SetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.BackgroundIntelligentTransferService.BITS_FILE_PROPERTY_ID,win32more.Networking.BackgroundIntelligentTransferService.BITS_FILE_PROPERTY_VALUE, use_last_error=False)(13, 'SetProperty', ((1, 'PropertyId'),(1, 'PropertyValue'),)))
    IBackgroundCopyFile5.GetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.BackgroundIntelligentTransferService.BITS_FILE_PROPERTY_ID,POINTER(win32more.Networking.BackgroundIntelligentTransferService.BITS_FILE_PROPERTY_VALUE_head), use_last_error=False)(14, 'GetProperty', ((1, 'PropertyId'),(1, 'PropertyValue'),)))
    win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile4
    return IBackgroundCopyFile5
BackgroundCopyManager10_1 = Guid('4bd3e4e1-7bd4-4a2b-9964-496400de5193')
def _define_IBackgroundCopyCallback3_head():
    class IBackgroundCopyCallback3(win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyCallback2_head):
        Guid = Guid('98c97bd2-e32b-4ad8-a528-95fd8b16bd42')
    return IBackgroundCopyCallback3
def _define_IBackgroundCopyCallback3():
    IBackgroundCopyCallback3 = win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyCallback3_head
    IBackgroundCopyCallback3.FileRangesTransferred = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob_head,win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile_head,UInt32,POINTER(win32more.Networking.BackgroundIntelligentTransferService.BG_FILE_RANGE), use_last_error=False)(7, 'FileRangesTransferred', ((1, 'job'),(1, 'file'),(1, 'rangeCount'),(1, 'ranges'),)))
    win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyCallback2
    return IBackgroundCopyCallback3
def _define_IBackgroundCopyFile6_head():
    class IBackgroundCopyFile6(win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile5_head):
        Guid = Guid('cf6784f7-d677-49fd-9368-cb47aee9d1ad')
    return IBackgroundCopyFile6
def _define_IBackgroundCopyFile6():
    IBackgroundCopyFile6 = win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile6_head
    IBackgroundCopyFile6.UpdateDownloadPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64, use_last_error=False)(15, 'UpdateDownloadPosition', ((1, 'offset'),)))
    IBackgroundCopyFile6.RequestFileRanges = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Networking.BackgroundIntelligentTransferService.BG_FILE_RANGE), use_last_error=False)(16, 'RequestFileRanges', ((1, 'rangeCount'),(1, 'ranges'),)))
    IBackgroundCopyFile6.GetFilledFileRanges = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(POINTER(win32more.Networking.BackgroundIntelligentTransferService.BG_FILE_RANGE_head)), use_last_error=False)(17, 'GetFilledFileRanges', ((1, 'rangeCount'),(1, 'ranges'),)))
    win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile5
    return IBackgroundCopyFile6
BackgroundCopyManager10_2 = Guid('4575438f-a6c8-4976-b0fe-2f26b80d959e')
def _define_IBackgroundCopyJobHttpOptions2_head():
    class IBackgroundCopyJobHttpOptions2(win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJobHttpOptions_head):
        Guid = Guid('b591a192-a405-4fc3-8323-4c5c542578fc')
    return IBackgroundCopyJobHttpOptions2
def _define_IBackgroundCopyJobHttpOptions2():
    IBackgroundCopyJobHttpOptions2 = win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJobHttpOptions2_head
    IBackgroundCopyJobHttpOptions2.SetHttpMethod = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(11, 'SetHttpMethod', ((1, 'method'),)))
    IBackgroundCopyJobHttpOptions2.GetHttpMethod = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(12, 'GetHttpMethod', ((1, 'method'),)))
    win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJobHttpOptions
    return IBackgroundCopyJobHttpOptions2
BackgroundCopyManager10_3 = Guid('5fd42ad5-c04e-4d36-adc7-e08ff15737ad')
def _define_IBackgroundCopyServerCertificateValidationCallback_head():
    class IBackgroundCopyServerCertificateValidationCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('4cec0d02-def7-4158-813a-c32a46945ff7')
    return IBackgroundCopyServerCertificateValidationCallback
def _define_IBackgroundCopyServerCertificateValidationCallback():
    IBackgroundCopyServerCertificateValidationCallback = win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyServerCertificateValidationCallback_head
    IBackgroundCopyServerCertificateValidationCallback.ValidateServerCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob_head,win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyFile_head,UInt32,POINTER(Byte),UInt32,UInt32,POINTER(Byte), use_last_error=False)(3, 'ValidateServerCertificate', ((1, 'job'),(1, 'file'),(1, 'certLength'),(1, 'certData'),(1, 'certEncodingType'),(1, 'certStoreLength'),(1, 'certStoreData'),)))
    win32more.System.Com.IUnknown
    return IBackgroundCopyServerCertificateValidationCallback
def _define_IBackgroundCopyJobHttpOptions3_head():
    class IBackgroundCopyJobHttpOptions3(win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJobHttpOptions2_head):
        Guid = Guid('8a9263d3-fd4c-4eda-9b28-30132a4d4e3c')
    return IBackgroundCopyJobHttpOptions3
def _define_IBackgroundCopyJobHttpOptions3():
    IBackgroundCopyJobHttpOptions3 = win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJobHttpOptions3_head
    IBackgroundCopyJobHttpOptions3.SetServerCertificateValidationInterface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)(13, 'SetServerCertificateValidationInterface', ((1, 'certValidationCallback'),)))
    IBackgroundCopyJobHttpOptions3.MakeCustomHeadersWriteOnly = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(14, 'MakeCustomHeadersWriteOnly', ()))
    win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJobHttpOptions2
    return IBackgroundCopyJobHttpOptions3
BITSExtensionSetupFactory = Guid('efbbab68-7286-4783-94bf-9461d8b7e7e9')
def _define_IBITSExtensionSetup_head():
    class IBITSExtensionSetup(win32more.System.Com.IDispatch_head):
        Guid = Guid('29cfbbf7-09e4-4b97-b0bc-f2287e3d8eb3')
    return IBITSExtensionSetup
def _define_IBITSExtensionSetup():
    IBITSExtensionSetup = win32more.Networking.BackgroundIntelligentTransferService.IBITSExtensionSetup_head
    IBITSExtensionSetup.EnableBITSUploads = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'EnableBITSUploads', ()))
    IBITSExtensionSetup.DisableBITSUploads = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'DisableBITSUploads', ()))
    IBITSExtensionSetup.GetCleanupTaskName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'GetCleanupTaskName', ((1, 'pTaskName'),)))
    IBITSExtensionSetup.GetCleanupTask = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(10, 'GetCleanupTask', ((1, 'riid'),(1, 'ppUnk'),)))
    win32more.System.Com.IDispatch
    return IBITSExtensionSetup
def _define_IBITSExtensionSetupFactory_head():
    class IBITSExtensionSetupFactory(win32more.System.Com.IDispatch_head):
        Guid = Guid('d5d2d542-5503-4e64-8b48-72ef91a32ee1')
    return IBITSExtensionSetupFactory
def _define_IBITSExtensionSetupFactory():
    IBITSExtensionSetupFactory = win32more.Networking.BackgroundIntelligentTransferService.IBITSExtensionSetupFactory_head
    IBITSExtensionSetupFactory.GetObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Networking.BackgroundIntelligentTransferService.IBITSExtensionSetup_head), use_last_error=False)(7, 'GetObject', ((1, 'Path'),(1, 'ppExtensionSetup'),)))
    win32more.System.Com.IDispatch
    return IBITSExtensionSetupFactory
BackgroundCopyQMgr = Guid('69ad4aee-51be-439b-a92c-86ae490e8b30')
def _define_FILESETINFO_head():
    class FILESETINFO(Structure):
        pass
    return FILESETINFO
def _define_FILESETINFO():
    FILESETINFO = win32more.Networking.BackgroundIntelligentTransferService.FILESETINFO_head
    FILESETINFO._fields_ = [
        ("bstrRemoteFile", win32more.Foundation.BSTR),
        ("bstrLocalFile", win32more.Foundation.BSTR),
        ("dwSizeHint", UInt32),
    ]
    return FILESETINFO
def _define_IBackgroundCopyJob1_head():
    class IBackgroundCopyJob1(win32more.System.Com.IUnknown_head):
        Guid = Guid('59f5553c-2031-4629-bb18-2645a6970947')
    return IBackgroundCopyJob1
def _define_IBackgroundCopyJob1():
    IBackgroundCopyJob1 = win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob1_head
    IBackgroundCopyJob1.CancelJob = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'CancelJob', ()))
    IBackgroundCopyJob1.GetProgress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(4, 'GetProgress', ((1, 'dwFlags'),(1, 'pdwProgress'),)))
    IBackgroundCopyJob1.GetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(5, 'GetStatus', ((1, 'pdwStatus'),(1, 'pdwWin32Result'),(1, 'pdwTransportResult'),(1, 'pdwNumOfRetries'),)))
    IBackgroundCopyJob1.AddFiles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(POINTER(win32more.Networking.BackgroundIntelligentTransferService.FILESETINFO_head)), use_last_error=False)(6, 'AddFiles', ((1, 'cFileCount'),(1, 'ppFileSet'),)))
    IBackgroundCopyJob1.GetFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Networking.BackgroundIntelligentTransferService.FILESETINFO_head), use_last_error=False)(7, 'GetFile', ((1, 'cFileIndex'),(1, 'pFileInfo'),)))
    IBackgroundCopyJob1.GetFileCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(8, 'GetFileCount', ((1, 'pdwFileCount'),)))
    IBackgroundCopyJob1.SwitchToForeground = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(9, 'SwitchToForeground', ()))
    IBackgroundCopyJob1.get_JobID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(10, 'get_JobID', ((1, 'pguidJobID'),)))
    win32more.System.Com.IUnknown
    return IBackgroundCopyJob1
def _define_IEnumBackgroundCopyJobs1_head():
    class IEnumBackgroundCopyJobs1(win32more.System.Com.IUnknown_head):
        Guid = Guid('8baeba9d-8f1c-42c4-b82c-09ae79980d25')
    return IEnumBackgroundCopyJobs1
def _define_IEnumBackgroundCopyJobs1():
    IEnumBackgroundCopyJobs1 = win32more.Networking.BackgroundIntelligentTransferService.IEnumBackgroundCopyJobs1_head
    IEnumBackgroundCopyJobs1.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(UInt32), use_last_error=False)(3, 'Next', ((1, 'celt'),(1, 'rgelt'),(1, 'pceltFetched'),)))
    IEnumBackgroundCopyJobs1.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'Skip', ((1, 'celt'),)))
    IEnumBackgroundCopyJobs1.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumBackgroundCopyJobs1.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.BackgroundIntelligentTransferService.IEnumBackgroundCopyJobs1_head), use_last_error=False)(6, 'Clone', ((1, 'ppenum'),)))
    IEnumBackgroundCopyJobs1.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(7, 'GetCount', ((1, 'puCount'),)))
    win32more.System.Com.IUnknown
    return IEnumBackgroundCopyJobs1
GROUPPROP = Int32
GROUPPROP_PRIORITY = 0
GROUPPROP_REMOTEUSERID = 1
GROUPPROP_REMOTEUSERPWD = 2
GROUPPROP_LOCALUSERID = 3
GROUPPROP_LOCALUSERPWD = 4
GROUPPROP_PROTOCOLFLAGS = 5
GROUPPROP_NOTIFYFLAGS = 6
GROUPPROP_NOTIFYCLSID = 7
GROUPPROP_PROGRESSSIZE = 8
GROUPPROP_PROGRESSPERCENT = 9
GROUPPROP_PROGRESSTIME = 10
GROUPPROP_DISPLAYNAME = 11
GROUPPROP_DESCRIPTION = 12
def _define_IBackgroundCopyGroup_head():
    class IBackgroundCopyGroup(win32more.System.Com.IUnknown_head):
        Guid = Guid('1ded80a7-53ea-424f-8a04-17fea9adc4f5')
    return IBackgroundCopyGroup
def _define_IBackgroundCopyGroup():
    IBackgroundCopyGroup = win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyGroup_head
    IBackgroundCopyGroup.GetProp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.BackgroundIntelligentTransferService.GROUPPROP,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(3, 'GetProp', ((1, 'propID'),(1, 'pvarVal'),)))
    IBackgroundCopyGroup.SetProp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.BackgroundIntelligentTransferService.GROUPPROP,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(4, 'SetProp', ((1, 'propID'),(1, 'pvarVal'),)))
    IBackgroundCopyGroup.GetProgress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(5, 'GetProgress', ((1, 'dwFlags'),(1, 'pdwProgress'),)))
    IBackgroundCopyGroup.GetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(6, 'GetStatus', ((1, 'pdwStatus'),(1, 'pdwJobIndex'),)))
    IBackgroundCopyGroup.GetJob = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,POINTER(win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob1_head), use_last_error=False)(7, 'GetJob', ((1, 'jobID'),(1, 'ppJob'),)))
    IBackgroundCopyGroup.SuspendGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'SuspendGroup', ()))
    IBackgroundCopyGroup.ResumeGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(9, 'ResumeGroup', ()))
    IBackgroundCopyGroup.CancelGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(10, 'CancelGroup', ()))
    IBackgroundCopyGroup.get_Size = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(11, 'get_Size', ((1, 'pdwSize'),)))
    IBackgroundCopyGroup.get_GroupID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(12, 'get_GroupID', ((1, 'pguidGroupID'),)))
    IBackgroundCopyGroup.CreateJob = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,POINTER(win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob1_head), use_last_error=False)(13, 'CreateJob', ((1, 'guidJobID'),(1, 'ppJob'),)))
    IBackgroundCopyGroup.EnumJobs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Networking.BackgroundIntelligentTransferService.IEnumBackgroundCopyJobs1_head), use_last_error=False)(14, 'EnumJobs', ((1, 'dwFlags'),(1, 'ppEnumJobs'),)))
    IBackgroundCopyGroup.SwitchToForeground = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(15, 'SwitchToForeground', ()))
    IBackgroundCopyGroup.QueryNewJobInterface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(16, 'QueryNewJobInterface', ((1, 'iid'),(1, 'pUnk'),)))
    IBackgroundCopyGroup.SetNotificationPointer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.IUnknown_head, use_last_error=False)(17, 'SetNotificationPointer', ((1, 'iid'),(1, 'pUnk'),)))
    win32more.System.Com.IUnknown
    return IBackgroundCopyGroup
def _define_IEnumBackgroundCopyGroups_head():
    class IEnumBackgroundCopyGroups(win32more.System.Com.IUnknown_head):
        Guid = Guid('d993e603-4aa4-47c5-8665-c20d39c2ba4f')
    return IEnumBackgroundCopyGroups
def _define_IEnumBackgroundCopyGroups():
    IEnumBackgroundCopyGroups = win32more.Networking.BackgroundIntelligentTransferService.IEnumBackgroundCopyGroups_head
    IEnumBackgroundCopyGroups.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(UInt32), use_last_error=False)(3, 'Next', ((1, 'celt'),(1, 'rgelt'),(1, 'pceltFetched'),)))
    IEnumBackgroundCopyGroups.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'Skip', ((1, 'celt'),)))
    IEnumBackgroundCopyGroups.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumBackgroundCopyGroups.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.BackgroundIntelligentTransferService.IEnumBackgroundCopyGroups_head), use_last_error=False)(6, 'Clone', ((1, 'ppenum'),)))
    IEnumBackgroundCopyGroups.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(7, 'GetCount', ((1, 'puCount'),)))
    win32more.System.Com.IUnknown
    return IEnumBackgroundCopyGroups
def _define_IBackgroundCopyCallback1_head():
    class IBackgroundCopyCallback1(win32more.System.Com.IUnknown_head):
        Guid = Guid('084f6593-3800-4e08-9b59-99fa59addf82')
    return IBackgroundCopyCallback1
def _define_IBackgroundCopyCallback1():
    IBackgroundCopyCallback1 = win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyCallback1_head
    IBackgroundCopyCallback1.OnStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyGroup_head,win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob1_head,UInt32,UInt32,UInt32,UInt32,UInt32, use_last_error=False)(3, 'OnStatus', ((1, 'pGroup'),(1, 'pJob'),(1, 'dwFileIndex'),(1, 'dwStatus'),(1, 'dwNumOfRetries'),(1, 'dwWin32Result'),(1, 'dwTransportResult'),)))
    IBackgroundCopyCallback1.OnProgress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyGroup_head,win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob1_head,UInt32,UInt32, use_last_error=False)(4, 'OnProgress', ((1, 'ProgressType'),(1, 'pGroup'),(1, 'pJob'),(1, 'dwFileIndex'),(1, 'dwProgressValue'),)))
    IBackgroundCopyCallback1.OnProgressEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyGroup_head,win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyJob1_head,UInt32,UInt32,UInt32,POINTER(Byte), use_last_error=False)(5, 'OnProgressEx', ((1, 'ProgressType'),(1, 'pGroup'),(1, 'pJob'),(1, 'dwFileIndex'),(1, 'dwProgressValue'),(1, 'dwByteArraySize'),(1, 'pByte'),)))
    win32more.System.Com.IUnknown
    return IBackgroundCopyCallback1
def _define_IBackgroundCopyQMgr_head():
    class IBackgroundCopyQMgr(win32more.System.Com.IUnknown_head):
        Guid = Guid('16f41c69-09f5-41d2-8cd8-3c08c47bc8a8')
    return IBackgroundCopyQMgr
def _define_IBackgroundCopyQMgr():
    IBackgroundCopyQMgr = win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyQMgr_head
    IBackgroundCopyQMgr.CreateGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,POINTER(win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyGroup_head), use_last_error=False)(3, 'CreateGroup', ((1, 'guidGroupID'),(1, 'ppGroup'),)))
    IBackgroundCopyQMgr.GetGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,POINTER(win32more.Networking.BackgroundIntelligentTransferService.IBackgroundCopyGroup_head), use_last_error=False)(4, 'GetGroup', ((1, 'groupID'),(1, 'ppGroup'),)))
    IBackgroundCopyQMgr.EnumGroups = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Networking.BackgroundIntelligentTransferService.IEnumBackgroundCopyGroups_head), use_last_error=False)(5, 'EnumGroups', ((1, 'dwFlags'),(1, 'ppEnumGroups'),)))
    win32more.System.Com.IUnknown
    return IBackgroundCopyQMgr
__all__ = [
    "BG_NOTIFY_JOB_TRANSFERRED",
    "BG_NOTIFY_JOB_ERROR",
    "BG_NOTIFY_DISABLE",
    "BG_NOTIFY_JOB_MODIFICATION",
    "BG_NOTIFY_FILE_TRANSFERRED",
    "BG_NOTIFY_FILE_RANGES_TRANSFERRED",
    "BG_JOB_ENUM_ALL_USERS",
    "BG_COPY_FILE_OWNER",
    "BG_COPY_FILE_GROUP",
    "BG_COPY_FILE_DACL",
    "BG_COPY_FILE_SACL",
    "BG_COPY_FILE_ALL",
    "BG_SSL_ENABLE_CRL_CHECK",
    "BG_SSL_IGNORE_CERT_CN_INVALID",
    "BG_SSL_IGNORE_CERT_DATE_INVALID",
    "BG_SSL_IGNORE_UNKNOWN_CA",
    "BG_SSL_IGNORE_CERT_WRONG_USAGE",
    "BG_HTTP_REDIRECT_POLICY_MASK",
    "BG_HTTP_REDIRECT_POLICY_ALLOW_SILENT",
    "BG_HTTP_REDIRECT_POLICY_ALLOW_REPORT",
    "BG_HTTP_REDIRECT_POLICY_DISALLOW",
    "BG_HTTP_REDIRECT_POLICY_ALLOW_HTTPS_TO_HTTP",
    "BG_ENABLE_PEERCACHING_CLIENT",
    "BG_ENABLE_PEERCACHING_SERVER",
    "BG_DISABLE_BRANCH_CACHE",
    "BG_JOB_ENABLE_PEERCACHING_CLIENT",
    "BG_JOB_ENABLE_PEERCACHING_SERVER",
    "BG_JOB_DISABLE_BRANCH_CACHE",
    "BITS_COST_STATE_UNRESTRICTED",
    "BITS_COST_STATE_CAPPED_USAGE_UNKNOWN",
    "BITS_COST_STATE_BELOW_CAP",
    "BITS_COST_STATE_NEAR_CAP",
    "BITS_COST_STATE_OVERCAP_CHARGED",
    "BITS_COST_STATE_OVERCAP_THROTTLED",
    "BITS_COST_STATE_USAGE_BASED",
    "BITS_COST_STATE_ROAMING",
    "BITS_COST_OPTION_IGNORE_CONGESTION",
    "BITS_COST_STATE_RESERVED",
    "QM_NOTIFY_FILE_DONE",
    "QM_NOTIFY_JOB_DONE",
    "QM_NOTIFY_GROUP_DONE",
    "QM_NOTIFY_DISABLE_NOTIFY",
    "QM_NOTIFY_USE_PROGRESSEX",
    "QM_STATUS_FILE_COMPLETE",
    "QM_STATUS_FILE_INCOMPLETE",
    "QM_STATUS_JOB_COMPLETE",
    "QM_STATUS_JOB_INCOMPLETE",
    "QM_STATUS_JOB_ERROR",
    "QM_STATUS_JOB_FOREGROUND",
    "QM_STATUS_GROUP_COMPLETE",
    "QM_STATUS_GROUP_INCOMPLETE",
    "QM_STATUS_GROUP_SUSPENDED",
    "QM_STATUS_GROUP_ERROR",
    "QM_STATUS_GROUP_FOREGROUND",
    "QM_PROTOCOL_HTTP",
    "QM_PROTOCOL_FTP",
    "QM_PROTOCOL_SMB",
    "QM_PROTOCOL_CUSTOM",
    "QM_PROGRESS_PERCENT_DONE",
    "QM_PROGRESS_TIME_DONE",
    "QM_PROGRESS_SIZE_DONE",
    "QM_E_INVALID_STATE",
    "QM_E_SERVICE_UNAVAILABLE",
    "QM_E_DOWNLOADER_UNAVAILABLE",
    "QM_E_ITEM_NOT_FOUND",
    "BG_E_NOT_FOUND",
    "BG_E_INVALID_STATE",
    "BG_E_EMPTY",
    "BG_E_FILE_NOT_AVAILABLE",
    "BG_E_PROTOCOL_NOT_AVAILABLE",
    "BG_S_ERROR_CONTEXT_NONE",
    "BG_E_ERROR_CONTEXT_UNKNOWN",
    "BG_E_ERROR_CONTEXT_GENERAL_QUEUE_MANAGER",
    "BG_E_ERROR_CONTEXT_LOCAL_FILE",
    "BG_E_ERROR_CONTEXT_REMOTE_FILE",
    "BG_E_ERROR_CONTEXT_GENERAL_TRANSPORT",
    "BG_E_ERROR_CONTEXT_QUEUE_MANAGER_NOTIFICATION",
    "BG_E_DESTINATION_LOCKED",
    "BG_E_VOLUME_CHANGED",
    "BG_E_ERROR_INFORMATION_UNAVAILABLE",
    "BG_E_NETWORK_DISCONNECTED",
    "BG_E_MISSING_FILE_SIZE",
    "BG_E_INSUFFICIENT_HTTP_SUPPORT",
    "BG_E_INSUFFICIENT_RANGE_SUPPORT",
    "BG_E_REMOTE_NOT_SUPPORTED",
    "BG_E_NEW_OWNER_DIFF_MAPPING",
    "BG_E_NEW_OWNER_NO_FILE_ACCESS",
    "BG_S_PARTIAL_COMPLETE",
    "BG_E_PROXY_LIST_TOO_LARGE",
    "BG_E_PROXY_BYPASS_LIST_TOO_LARGE",
    "BG_S_UNABLE_TO_DELETE_FILES",
    "BG_E_INVALID_SERVER_RESPONSE",
    "BG_E_TOO_MANY_FILES",
    "BG_E_LOCAL_FILE_CHANGED",
    "BG_E_ERROR_CONTEXT_REMOTE_APPLICATION",
    "BG_E_SESSION_NOT_FOUND",
    "BG_E_TOO_LARGE",
    "BG_E_STRING_TOO_LONG",
    "BG_E_CLIENT_SERVER_PROTOCOL_MISMATCH",
    "BG_E_SERVER_EXECUTE_ENABLE",
    "BG_E_NO_PROGRESS",
    "BG_E_USERNAME_TOO_LARGE",
    "BG_E_PASSWORD_TOO_LARGE",
    "BG_E_INVALID_AUTH_TARGET",
    "BG_E_INVALID_AUTH_SCHEME",
    "BG_E_FILE_NOT_FOUND",
    "BG_S_PROXY_CHANGED",
    "BG_E_INVALID_RANGE",
    "BG_E_OVERLAPPING_RANGES",
    "BG_E_CONNECT_FAILURE",
    "BG_E_CONNECTION_CLOSED",
    "BG_E_BLOCKED_BY_POLICY",
    "BG_E_INVALID_PROXY_INFO",
    "BG_E_INVALID_CREDENTIALS",
    "BG_E_INVALID_HASH_ALGORITHM",
    "BG_E_RECORD_DELETED",
    "BG_E_COMMIT_IN_PROGRESS",
    "BG_E_DISCOVERY_IN_PROGRESS",
    "BG_E_UPNP_ERROR",
    "BG_E_TEST_OPTION_BLOCKED_DOWNLOAD",
    "BG_E_PEERCACHING_DISABLED",
    "BG_E_BUSYCACHERECORD",
    "BG_E_TOO_MANY_JOBS_PER_USER",
    "BG_E_TOO_MANY_JOBS_PER_MACHINE",
    "BG_E_TOO_MANY_FILES_IN_JOB",
    "BG_E_TOO_MANY_RANGES_IN_FILE",
    "BG_E_VALIDATION_FAILED",
    "BG_E_MAXDOWNLOAD_TIMEOUT",
    "BG_S_OVERRIDDEN_BY_POLICY",
    "BG_E_TOKEN_REQUIRED",
    "BG_E_UNKNOWN_PROPERTY_ID",
    "BG_E_READ_ONLY_PROPERTY",
    "BG_E_BLOCKED_BY_COST_TRANSFER_POLICY",
    "BG_E_PROPERTY_SUPPORTED_FOR_DOWNLOAD_JOBS_ONLY",
    "BG_E_READ_ONLY_PROPERTY_AFTER_ADDFILE",
    "BG_E_READ_ONLY_PROPERTY_AFTER_RESUME",
    "BG_E_MAX_DOWNLOAD_SIZE_INVALID_VALUE",
    "BG_E_MAX_DOWNLOAD_SIZE_LIMIT_REACHED",
    "BG_E_STANDBY_MODE",
    "BG_E_USE_STORED_CREDENTIALS_NOT_SUPPORTED",
    "BG_E_BLOCKED_BY_BATTERY_POLICY",
    "BG_E_BLOCKED_BY_BATTERY_SAVER",
    "BG_E_WATCHDOG_TIMEOUT",
    "BG_E_APP_PACKAGE_NOT_FOUND",
    "BG_E_APP_PACKAGE_SCENARIO_NOT_SUPPORTED",
    "BG_E_DATABASE_CORRUPT",
    "BG_E_RANDOM_ACCESS_NOT_SUPPORTED",
    "BG_E_BLOCKED_BY_BACKGROUND_ACCESS_POLICY",
    "BG_E_BLOCKED_BY_GAME_MODE",
    "BG_E_BLOCKED_BY_SYSTEM_POLICY",
    "BG_E_NOT_SUPPORTED_WITH_CUSTOM_HTTP_METHOD",
    "BG_E_UNSUPPORTED_JOB_CONFIGURATION",
    "BG_E_REMOTE_FILE_CHANGED",
    "BG_E_SERVER_CERT_VALIDATION_INTERFACE_REQUIRED",
    "BG_E_READ_ONLY_WHEN_JOB_ACTIVE",
    "BG_E_ERROR_CONTEXT_SERVER_CERTIFICATE_CALLBACK",
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
    "BITS_MC_JOB_CANCELLED",
    "BITS_MC_FILE_DELETION_FAILED",
    "BITS_MC_FILE_DELETION_FAILED_MORE",
    "BITS_MC_JOB_PROPERTY_CHANGE",
    "BITS_MC_JOB_TAKE_OWNERSHIP",
    "BITS_MC_JOB_SCAVENGED",
    "BITS_MC_JOB_NOTIFICATION_FAILURE",
    "BITS_MC_STATE_FILE_CORRUPT",
    "BITS_MC_FAILED_TO_START",
    "BITS_MC_FATAL_IGD_ERROR",
    "BITS_MC_PEERCACHING_PORT",
    "BITS_MC_WSD_PORT",
    "BG_TOKEN",
    "BG_TOKEN_LOCAL_FILE",
    "BG_TOKEN_NETWORK",
    "BackgroundCopyManager",
    "BG_FILE_PROGRESS",
    "IBackgroundCopyFile",
    "IEnumBackgroundCopyFiles",
    "BG_ERROR_CONTEXT",
    "BG_ERROR_CONTEXT_NONE",
    "BG_ERROR_CONTEXT_UNKNOWN",
    "BG_ERROR_CONTEXT_GENERAL_QUEUE_MANAGER",
    "BG_ERROR_CONTEXT_QUEUE_MANAGER_NOTIFICATION",
    "BG_ERROR_CONTEXT_LOCAL_FILE",
    "BG_ERROR_CONTEXT_REMOTE_FILE",
    "BG_ERROR_CONTEXT_GENERAL_TRANSPORT",
    "BG_ERROR_CONTEXT_REMOTE_APPLICATION",
    "BG_ERROR_CONTEXT_SERVER_CERTIFICATE_CALLBACK",
    "IBackgroundCopyError",
    "BG_FILE_INFO",
    "BG_JOB_PROGRESS",
    "BG_JOB_TIMES",
    "BG_JOB_PRIORITY",
    "BG_JOB_PRIORITY_FOREGROUND",
    "BG_JOB_PRIORITY_HIGH",
    "BG_JOB_PRIORITY_NORMAL",
    "BG_JOB_PRIORITY_LOW",
    "BG_JOB_STATE",
    "BG_JOB_STATE_QUEUED",
    "BG_JOB_STATE_CONNECTING",
    "BG_JOB_STATE_TRANSFERRING",
    "BG_JOB_STATE_SUSPENDED",
    "BG_JOB_STATE_ERROR",
    "BG_JOB_STATE_TRANSIENT_ERROR",
    "BG_JOB_STATE_TRANSFERRED",
    "BG_JOB_STATE_ACKNOWLEDGED",
    "BG_JOB_STATE_CANCELLED",
    "BG_JOB_TYPE",
    "BG_JOB_TYPE_DOWNLOAD",
    "BG_JOB_TYPE_UPLOAD",
    "BG_JOB_TYPE_UPLOAD_REPLY",
    "BG_JOB_PROXY_USAGE",
    "BG_JOB_PROXY_USAGE_PRECONFIG",
    "BG_JOB_PROXY_USAGE_NO_PROXY",
    "BG_JOB_PROXY_USAGE_OVERRIDE",
    "BG_JOB_PROXY_USAGE_AUTODETECT",
    "IBackgroundCopyJob",
    "IEnumBackgroundCopyJobs",
    "IBackgroundCopyCallback",
    "AsyncIBackgroundCopyCallback",
    "IBackgroundCopyManager",
    "BackgroundCopyManager1_5",
    "BG_JOB_REPLY_PROGRESS",
    "BG_AUTH_TARGET",
    "BG_AUTH_TARGET_SERVER",
    "BG_AUTH_TARGET_PROXY",
    "BG_AUTH_SCHEME",
    "BG_AUTH_SCHEME_BASIC",
    "BG_AUTH_SCHEME_DIGEST",
    "BG_AUTH_SCHEME_NTLM",
    "BG_AUTH_SCHEME_NEGOTIATE",
    "BG_AUTH_SCHEME_PASSPORT",
    "BG_BASIC_CREDENTIALS",
    "BG_AUTH_CREDENTIALS_UNION",
    "BG_AUTH_CREDENTIALS",
    "IBackgroundCopyJob2",
    "BackgroundCopyManager2_0",
    "BG_FILE_RANGE",
    "IBackgroundCopyJob3",
    "IBackgroundCopyFile2",
    "BackgroundCopyManager2_5",
    "BG_CERT_STORE_LOCATION",
    "BG_CERT_STORE_LOCATION_CURRENT_USER",
    "BG_CERT_STORE_LOCATION_LOCAL_MACHINE",
    "BG_CERT_STORE_LOCATION_CURRENT_SERVICE",
    "BG_CERT_STORE_LOCATION_SERVICES",
    "BG_CERT_STORE_LOCATION_USERS",
    "BG_CERT_STORE_LOCATION_CURRENT_USER_GROUP_POLICY",
    "BG_CERT_STORE_LOCATION_LOCAL_MACHINE_GROUP_POLICY",
    "BG_CERT_STORE_LOCATION_LOCAL_MACHINE_ENTERPRISE",
    "IBackgroundCopyJobHttpOptions",
    "BackgroundCopyManager3_0",
    "IBitsPeerCacheRecord",
    "IEnumBitsPeerCacheRecords",
    "IBitsPeer",
    "IEnumBitsPeers",
    "IBitsPeerCacheAdministration",
    "IBackgroundCopyJob4",
    "IBackgroundCopyFile3",
    "IBackgroundCopyCallback2",
    "BackgroundCopyManager4_0",
    "IBitsTokenOptions",
    "IBackgroundCopyFile4",
    "BackgroundCopyManager5_0",
    "BITS_JOB_TRANSFER_POLICY",
    "BITS_JOB_TRANSFER_POLICY_ALWAYS",
    "BITS_JOB_TRANSFER_POLICY_NOT_ROAMING",
    "BITS_JOB_TRANSFER_POLICY_NO_SURCHARGE",
    "BITS_JOB_TRANSFER_POLICY_STANDARD",
    "BITS_JOB_TRANSFER_POLICY_UNRESTRICTED",
    "BITS_JOB_PROPERTY_ID",
    "BITS_JOB_PROPERTY_ID_COST_FLAGS",
    "BITS_JOB_PROPERTY_NOTIFICATION_CLSID",
    "BITS_JOB_PROPERTY_DYNAMIC_CONTENT",
    "BITS_JOB_PROPERTY_HIGH_PERFORMANCE",
    "BITS_JOB_PROPERTY_MAX_DOWNLOAD_SIZE",
    "BITS_JOB_PROPERTY_USE_STORED_CREDENTIALS",
    "BITS_JOB_PROPERTY_MINIMUM_NOTIFICATION_INTERVAL_MS",
    "BITS_JOB_PROPERTY_ON_DEMAND_MODE",
    "BITS_JOB_PROPERTY_VALUE",
    "BITS_FILE_PROPERTY_ID",
    "BITS_FILE_PROPERTY_ID_HTTP_RESPONSE_HEADERS",
    "BITS_FILE_PROPERTY_VALUE",
    "IBackgroundCopyJob5",
    "IBackgroundCopyFile5",
    "BackgroundCopyManager10_1",
    "IBackgroundCopyCallback3",
    "IBackgroundCopyFile6",
    "BackgroundCopyManager10_2",
    "IBackgroundCopyJobHttpOptions2",
    "BackgroundCopyManager10_3",
    "IBackgroundCopyServerCertificateValidationCallback",
    "IBackgroundCopyJobHttpOptions3",
    "BITSExtensionSetupFactory",
    "IBITSExtensionSetup",
    "IBITSExtensionSetupFactory",
    "BackgroundCopyQMgr",
    "FILESETINFO",
    "IBackgroundCopyJob1",
    "IEnumBackgroundCopyJobs1",
    "GROUPPROP",
    "GROUPPROP_PRIORITY",
    "GROUPPROP_REMOTEUSERID",
    "GROUPPROP_REMOTEUSERPWD",
    "GROUPPROP_LOCALUSERID",
    "GROUPPROP_LOCALUSERPWD",
    "GROUPPROP_PROTOCOLFLAGS",
    "GROUPPROP_NOTIFYFLAGS",
    "GROUPPROP_NOTIFYCLSID",
    "GROUPPROP_PROGRESSSIZE",
    "GROUPPROP_PROGRESSPERCENT",
    "GROUPPROP_PROGRESSTIME",
    "GROUPPROP_DISPLAYNAME",
    "GROUPPROP_DESCRIPTION",
    "IBackgroundCopyGroup",
    "IEnumBackgroundCopyGroups",
    "IBackgroundCopyCallback1",
    "IBackgroundCopyQMgr",
]
