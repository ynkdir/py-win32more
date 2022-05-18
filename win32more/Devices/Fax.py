from win32more import *
import win32more.Devices.Fax
import win32more.Foundation
import win32more.Graphics.Gdi
import win32more.System.Com
import win32more.System.IO
import win32more.System.Registry
import win32more.UI.Controls
import win32more.UI.Shell.PropertiesSystem

def __getattr__(name):
    module = globals()
    try:
        f = module[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    module[name] = f()
    return module[name]
def __dir__():
    return __all__
FS_INITIALIZING = 536870912
FS_DIALING = 536870913
FS_TRANSMITTING = 536870914
FS_RECEIVING = 536870916
FS_COMPLETED = 536870920
FS_HANDLED = 536870928
FS_LINE_UNAVAILABLE = 536870944
FS_BUSY = 536870976
FS_NO_ANSWER = 536871040
FS_BAD_ADDRESS = 536871168
FS_NO_DIAL_TONE = 536871424
FS_DISCONNECTED = 536871936
FS_FATAL_ERROR = 536872960
FS_NOT_FAX_CALL = 536875008
FS_CALL_DELAYED = 536879104
FS_CALL_BLACKLISTED = 536887296
FS_USER_ABORT = 538968064
FS_ANSWERED = 545259520
FAXDEVRECEIVE_SIZE = 4096
FAXDEVREPORTSTATUS_SIZE = 4096
FAX_ERR_START = 7001
FAX_ERR_SRV_OUTOFMEMORY = 7001
FAX_ERR_GROUP_NOT_FOUND = 7002
FAX_ERR_BAD_GROUP_CONFIGURATION = 7003
FAX_ERR_GROUP_IN_USE = 7004
FAX_ERR_RULE_NOT_FOUND = 7005
FAX_ERR_NOT_NTFS = 7006
FAX_ERR_DIRECTORY_IN_USE = 7007
FAX_ERR_FILE_ACCESS_DENIED = 7008
FAX_ERR_MESSAGE_NOT_FOUND = 7009
FAX_ERR_DEVICE_NUM_LIMIT_EXCEEDED = 7010
FAX_ERR_NOT_SUPPORTED_ON_THIS_SKU = 7011
FAX_ERR_VERSION_MISMATCH = 7012
FAX_ERR_RECIPIENTS_LIMIT = 7013
FAX_ERR_END = 7013
FAX_E_SRV_OUTOFMEMORY = -2147214503
FAX_E_GROUP_NOT_FOUND = -2147214502
FAX_E_BAD_GROUP_CONFIGURATION = -2147214501
FAX_E_GROUP_IN_USE = -2147214500
FAX_E_RULE_NOT_FOUND = -2147214499
FAX_E_NOT_NTFS = -2147214498
FAX_E_DIRECTORY_IN_USE = -2147214497
FAX_E_FILE_ACCESS_DENIED = -2147214496
FAX_E_MESSAGE_NOT_FOUND = -2147214495
FAX_E_DEVICE_NUM_LIMIT_EXCEEDED = -2147214494
FAX_E_NOT_SUPPORTED_ON_THIS_SKU = -2147214493
FAX_E_VERSION_MISMATCH = -2147214492
FAX_E_RECIPIENTS_LIMIT = -2147214491
JT_UNKNOWN = 0
JT_SEND = 1
JT_RECEIVE = 2
JT_ROUTING = 3
JT_FAIL_RECEIVE = 4
JS_PENDING = 0
JS_INPROGRESS = 1
JS_DELETING = 2
JS_FAILED = 4
JS_PAUSED = 8
JS_NOLINE = 16
JS_RETRYING = 32
JS_RETRIES_EXCEEDED = 64
FPS_DIALING = 536870913
FPS_SENDING = 536870914
FPS_RECEIVING = 536870916
FPS_COMPLETED = 536870920
FPS_HANDLED = 536870928
FPS_UNAVAILABLE = 536870944
FPS_BUSY = 536870976
FPS_NO_ANSWER = 536871040
FPS_BAD_ADDRESS = 536871168
FPS_NO_DIAL_TONE = 536871424
FPS_DISCONNECTED = 536871936
FPS_FATAL_ERROR = 536872960
FPS_NOT_FAX_CALL = 536875008
FPS_CALL_DELAYED = 536879104
FPS_CALL_BLACKLISTED = 536887296
FPS_INITIALIZING = 536903680
FPS_OFFLINE = 536936448
FPS_RINGING = 537001984
FPS_AVAILABLE = 537919488
FPS_ABORTING = 538968064
FPS_ROUTING = 541065216
FPS_ANSWERED = 545259520
FPF_RECEIVE = 1
FPF_SEND = 2
FPF_VIRTUAL = 4
FEI_DIALING = 1
FEI_SENDING = 2
FEI_RECEIVING = 3
FEI_COMPLETED = 4
FEI_BUSY = 5
FEI_NO_ANSWER = 6
FEI_BAD_ADDRESS = 7
FEI_NO_DIAL_TONE = 8
FEI_DISCONNECTED = 9
FEI_FATAL_ERROR = 10
FEI_NOT_FAX_CALL = 11
FEI_CALL_DELAYED = 12
FEI_CALL_BLACKLISTED = 13
FEI_RINGING = 14
FEI_ABORTING = 15
FEI_ROUTING = 16
FEI_MODEM_POWERED_ON = 17
FEI_MODEM_POWERED_OFF = 18
FEI_IDLE = 19
FEI_FAXSVC_ENDED = 20
FEI_ANSWERED = 21
FEI_JOB_QUEUED = 22
FEI_DELETED = 23
FEI_INITIALIZING = 24
FEI_LINE_UNAVAILABLE = 25
FEI_HANDLED = 26
FEI_FAXSVC_STARTED = 27
FEI_NEVENTS = 27
FAX_JOB_SUBMIT = 1
FAX_JOB_QUERY = 2
FAX_CONFIG_QUERY = 4
FAX_CONFIG_SET = 8
FAX_PORT_QUERY = 16
FAX_PORT_SET = 32
FAX_JOB_MANAGE = 64
STI_UNICODE = 1
CLSID_Sti = 'b323f8e0-2e68-11d0-90ea-00aa0060f86c'
GUID_DeviceArrivedLaunch = '740d9ee6-70f1-11d1-ad10-00a02438ad48'
GUID_ScanImage = 'a6c5a715-8c6e-11d2-977a-0000f87a926f'
GUID_ScanPrintImage = 'b441f425-8c6e-11d2-977a-0000f87a926f'
GUID_ScanFaxImage = 'c00eb793-8c6e-11d2-977a-0000f87a926f'
GUID_STIUserDefined1 = 'c00eb795-8c6e-11d2-977a-0000f87a926f'
GUID_STIUserDefined2 = 'c77ae9c5-8c6e-11d2-977a-0000f87a926f'
GUID_STIUserDefined3 = 'c77ae9c6-8c6e-11d2-977a-0000f87a926f'
STI_VERSION_FLAG_MASK = 4278190080
STI_VERSION_FLAG_UNICODE = 16777216
STI_VERSION_REAL = 2
STI_VERSION_MIN_ALLOWED = 2
STI_VERSION = 2
STI_MAX_INTERNAL_NAME_LENGTH = 128
STI_GENCAP_NOTIFICATIONS = 1
STI_GENCAP_POLLING_NEEDED = 2
STI_GENCAP_GENERATE_ARRIVALEVENT = 4
STI_GENCAP_AUTO_PORTSELECT = 8
STI_GENCAP_WIA = 16
STI_GENCAP_SUBSET = 32
WIA_INCOMPAT_XP = 1
STI_HW_CONFIG_UNKNOWN = 1
STI_HW_CONFIG_SCSI = 2
STI_HW_CONFIG_USB = 4
STI_HW_CONFIG_SERIAL = 8
STI_HW_CONFIG_PARALLEL = 16
STI_DEVSTATUS_ONLINE_STATE = 1
STI_DEVSTATUS_EVENTS_STATE = 2
STI_ONLINESTATE_OPERATIONAL = 1
STI_ONLINESTATE_PENDING = 2
STI_ONLINESTATE_ERROR = 4
STI_ONLINESTATE_PAUSED = 8
STI_ONLINESTATE_PAPER_JAM = 16
STI_ONLINESTATE_PAPER_PROBLEM = 32
STI_ONLINESTATE_OFFLINE = 64
STI_ONLINESTATE_IO_ACTIVE = 128
STI_ONLINESTATE_BUSY = 256
STI_ONLINESTATE_TRANSFERRING = 512
STI_ONLINESTATE_INITIALIZING = 1024
STI_ONLINESTATE_WARMING_UP = 2048
STI_ONLINESTATE_USER_INTERVENTION = 4096
STI_ONLINESTATE_POWER_SAVE = 8192
STI_EVENTHANDLING_ENABLED = 1
STI_EVENTHANDLING_POLLING = 2
STI_EVENTHANDLING_PENDING = 4
STI_DIAGCODE_HWPRESENCE = 1
STI_TRACE_INFORMATION = 1
STI_TRACE_WARNING = 2
STI_TRACE_ERROR = 4
STI_SUBSCRIBE_FLAG_WINDOW = 1
STI_SUBSCRIBE_FLAG_EVENT = 2
MAX_NOTIFICATION_DATA = 64
STI_DEVICE_CREATE_STATUS = 1
STI_DEVICE_CREATE_DATA = 2
STI_DEVICE_CREATE_BOTH = 3
STI_DEVICE_CREATE_MASK = 65535
STIEDFL_ALLDEVICES = 0
STIEDFL_ATTACHEDONLY = 1
STI_RAW_RESERVED = 4096
STI_OK = 0
STI_ERROR_NO_ERROR = 0
STI_NOTCONNECTED = 1
STI_CHANGENOEFFECT = 1
STIERR_OLD_VERSION = -2147023746
STIERR_BETA_VERSION = -2147023743
STIERR_BADDRIVER = -2147024777
STIERR_DEVICENOTREG = -2147221164
STIERR_OBJECTNOTFOUND = -2147024894
STIERR_INVALID_PARAM = -2147024809
STIERR_NOINTERFACE = -2147467262
STIERR_GENERIC = -2147467259
STIERR_OUTOFMEMORY = -2147024882
STIERR_UNSUPPORTED = -2147467263
STIERR_NOT_INITIALIZED = -2147024875
STIERR_ALREADY_INITIALIZED = -2147023649
STIERR_DEVICE_LOCKED = -2147024863
STIERR_READONLY = -2147024891
STIERR_NOTINITIALIZED = -2147024891
STIERR_NEEDS_LOCK = -2147024738
STIERR_SHARING_VIOLATION = -2147024864
STIERR_HANDLEEXISTS = -2147024713
STIERR_INVALID_DEVICE_NAME = -2147024773
STIERR_INVALID_HW_TYPE = -2147024883
STIERR_NOEVENTS = -2147024637
STIERR_DEVICE_NOTREADY = -2147024875
IS_DIGITAL_CAMERA_VAL = 1
SUPPORTS_MSCPLUS_VAL = 1
DEVPKEY_WIA_DeviceType = PROPERTYKEY(Fmtid='6bdd1fc6-810f-11d0-bec7-08002be2092f', Pid=2)
DEVPKEY_WIA_USDClassId = PROPERTYKEY(Fmtid='6bdd1fc6-810f-11d0-bec7-08002be2092f', Pid=3)
STI_USD_GENCAP_NATIVE_PUSHSUPPORT = 1
STI_DEVICE_CREATE_FOR_MONITOR = 16777216
lDEFAULT_PREFETCH_SIZE = 100
wcharREASSIGN_RECIPIENTS_DELIMITER = 59
FAX_ENUM_LOG_LEVELS = Int32
FAXLOG_LEVEL_NONE = 0
FAXLOG_LEVEL_MIN = 1
FAXLOG_LEVEL_MED = 2
FAXLOG_LEVEL_MAX = 3
FAX_ENUM_LOG_CATEGORIES = Int32
FAXLOG_CATEGORY_INIT = 1
FAXLOG_CATEGORY_OUTBOUND = 2
FAXLOG_CATEGORY_INBOUND = 3
FAXLOG_CATEGORY_UNKNOWN = 4
def _define_FAX_LOG_CATEGORYA_head():
    class FAX_LOG_CATEGORYA(Structure):
        pass
    return FAX_LOG_CATEGORYA
def _define_FAX_LOG_CATEGORYA():
    FAX_LOG_CATEGORYA = win32more.Devices.Fax.FAX_LOG_CATEGORYA_head
    FAX_LOG_CATEGORYA._fields_ = [
        ("Name", win32more.Foundation.PSTR),
        ("Category", UInt32),
        ("Level", UInt32),
    ]
    return FAX_LOG_CATEGORYA
def _define_FAX_LOG_CATEGORYW_head():
    class FAX_LOG_CATEGORYW(Structure):
        pass
    return FAX_LOG_CATEGORYW
def _define_FAX_LOG_CATEGORYW():
    FAX_LOG_CATEGORYW = win32more.Devices.Fax.FAX_LOG_CATEGORYW_head
    FAX_LOG_CATEGORYW._fields_ = [
        ("Name", win32more.Foundation.PWSTR),
        ("Category", UInt32),
        ("Level", UInt32),
    ]
    return FAX_LOG_CATEGORYW
def _define_FAX_TIME_head():
    class FAX_TIME(Structure):
        pass
    return FAX_TIME
def _define_FAX_TIME():
    FAX_TIME = win32more.Devices.Fax.FAX_TIME_head
    FAX_TIME._fields_ = [
        ("Hour", UInt16),
        ("Minute", UInt16),
    ]
    return FAX_TIME
def _define_FAX_CONFIGURATIONA_head():
    class FAX_CONFIGURATIONA(Structure):
        pass
    return FAX_CONFIGURATIONA
def _define_FAX_CONFIGURATIONA():
    FAX_CONFIGURATIONA = win32more.Devices.Fax.FAX_CONFIGURATIONA_head
    FAX_CONFIGURATIONA._fields_ = [
        ("SizeOfStruct", UInt32),
        ("Retries", UInt32),
        ("RetryDelay", UInt32),
        ("DirtyDays", UInt32),
        ("Branding", win32more.Foundation.BOOL),
        ("UseDeviceTsid", win32more.Foundation.BOOL),
        ("ServerCp", win32more.Foundation.BOOL),
        ("PauseServerQueue", win32more.Foundation.BOOL),
        ("StartCheapTime", win32more.Devices.Fax.FAX_TIME),
        ("StopCheapTime", win32more.Devices.Fax.FAX_TIME),
        ("ArchiveOutgoingFaxes", win32more.Foundation.BOOL),
        ("ArchiveDirectory", win32more.Foundation.PSTR),
        ("Reserved", win32more.Foundation.PSTR),
    ]
    return FAX_CONFIGURATIONA
def _define_FAX_CONFIGURATIONW_head():
    class FAX_CONFIGURATIONW(Structure):
        pass
    return FAX_CONFIGURATIONW
def _define_FAX_CONFIGURATIONW():
    FAX_CONFIGURATIONW = win32more.Devices.Fax.FAX_CONFIGURATIONW_head
    FAX_CONFIGURATIONW._fields_ = [
        ("SizeOfStruct", UInt32),
        ("Retries", UInt32),
        ("RetryDelay", UInt32),
        ("DirtyDays", UInt32),
        ("Branding", win32more.Foundation.BOOL),
        ("UseDeviceTsid", win32more.Foundation.BOOL),
        ("ServerCp", win32more.Foundation.BOOL),
        ("PauseServerQueue", win32more.Foundation.BOOL),
        ("StartCheapTime", win32more.Devices.Fax.FAX_TIME),
        ("StopCheapTime", win32more.Devices.Fax.FAX_TIME),
        ("ArchiveOutgoingFaxes", win32more.Foundation.BOOL),
        ("ArchiveDirectory", win32more.Foundation.PWSTR),
        ("Reserved", win32more.Foundation.PWSTR),
    ]
    return FAX_CONFIGURATIONW
FAX_ENUM_JOB_COMMANDS = Int32
JC_UNKNOWN = 0
JC_DELETE = 1
JC_PAUSE = 2
JC_RESUME = 3
def _define_FAX_DEVICE_STATUSA_head():
    class FAX_DEVICE_STATUSA(Structure):
        pass
    return FAX_DEVICE_STATUSA
def _define_FAX_DEVICE_STATUSA():
    FAX_DEVICE_STATUSA = win32more.Devices.Fax.FAX_DEVICE_STATUSA_head
    FAX_DEVICE_STATUSA._fields_ = [
        ("SizeOfStruct", UInt32),
        ("CallerId", win32more.Foundation.PSTR),
        ("Csid", win32more.Foundation.PSTR),
        ("CurrentPage", UInt32),
        ("DeviceId", UInt32),
        ("DeviceName", win32more.Foundation.PSTR),
        ("DocumentName", win32more.Foundation.PSTR),
        ("JobType", UInt32),
        ("PhoneNumber", win32more.Foundation.PSTR),
        ("RoutingString", win32more.Foundation.PSTR),
        ("SenderName", win32more.Foundation.PSTR),
        ("RecipientName", win32more.Foundation.PSTR),
        ("Size", UInt32),
        ("StartTime", win32more.Foundation.FILETIME),
        ("Status", UInt32),
        ("StatusString", win32more.Foundation.PSTR),
        ("SubmittedTime", win32more.Foundation.FILETIME),
        ("TotalPages", UInt32),
        ("Tsid", win32more.Foundation.PSTR),
        ("UserName", win32more.Foundation.PSTR),
    ]
    return FAX_DEVICE_STATUSA
def _define_FAX_DEVICE_STATUSW_head():
    class FAX_DEVICE_STATUSW(Structure):
        pass
    return FAX_DEVICE_STATUSW
def _define_FAX_DEVICE_STATUSW():
    FAX_DEVICE_STATUSW = win32more.Devices.Fax.FAX_DEVICE_STATUSW_head
    FAX_DEVICE_STATUSW._fields_ = [
        ("SizeOfStruct", UInt32),
        ("CallerId", win32more.Foundation.PWSTR),
        ("Csid", win32more.Foundation.PWSTR),
        ("CurrentPage", UInt32),
        ("DeviceId", UInt32),
        ("DeviceName", win32more.Foundation.PWSTR),
        ("DocumentName", win32more.Foundation.PWSTR),
        ("JobType", UInt32),
        ("PhoneNumber", win32more.Foundation.PWSTR),
        ("RoutingString", win32more.Foundation.PWSTR),
        ("SenderName", win32more.Foundation.PWSTR),
        ("RecipientName", win32more.Foundation.PWSTR),
        ("Size", UInt32),
        ("StartTime", win32more.Foundation.FILETIME),
        ("Status", UInt32),
        ("StatusString", win32more.Foundation.PWSTR),
        ("SubmittedTime", win32more.Foundation.FILETIME),
        ("TotalPages", UInt32),
        ("Tsid", win32more.Foundation.PWSTR),
        ("UserName", win32more.Foundation.PWSTR),
    ]
    return FAX_DEVICE_STATUSW
def _define_FAX_JOB_ENTRYA_head():
    class FAX_JOB_ENTRYA(Structure):
        pass
    return FAX_JOB_ENTRYA
def _define_FAX_JOB_ENTRYA():
    FAX_JOB_ENTRYA = win32more.Devices.Fax.FAX_JOB_ENTRYA_head
    FAX_JOB_ENTRYA._fields_ = [
        ("SizeOfStruct", UInt32),
        ("JobId", UInt32),
        ("UserName", win32more.Foundation.PSTR),
        ("JobType", UInt32),
        ("QueueStatus", UInt32),
        ("Status", UInt32),
        ("Size", UInt32),
        ("PageCount", UInt32),
        ("RecipientNumber", win32more.Foundation.PSTR),
        ("RecipientName", win32more.Foundation.PSTR),
        ("Tsid", win32more.Foundation.PSTR),
        ("SenderName", win32more.Foundation.PSTR),
        ("SenderCompany", win32more.Foundation.PSTR),
        ("SenderDept", win32more.Foundation.PSTR),
        ("BillingCode", win32more.Foundation.PSTR),
        ("ScheduleAction", UInt32),
        ("ScheduleTime", win32more.Foundation.SYSTEMTIME),
        ("DeliveryReportType", UInt32),
        ("DeliveryReportAddress", win32more.Foundation.PSTR),
        ("DocumentName", win32more.Foundation.PSTR),
    ]
    return FAX_JOB_ENTRYA
def _define_FAX_JOB_ENTRYW_head():
    class FAX_JOB_ENTRYW(Structure):
        pass
    return FAX_JOB_ENTRYW
def _define_FAX_JOB_ENTRYW():
    FAX_JOB_ENTRYW = win32more.Devices.Fax.FAX_JOB_ENTRYW_head
    FAX_JOB_ENTRYW._fields_ = [
        ("SizeOfStruct", UInt32),
        ("JobId", UInt32),
        ("UserName", win32more.Foundation.PWSTR),
        ("JobType", UInt32),
        ("QueueStatus", UInt32),
        ("Status", UInt32),
        ("Size", UInt32),
        ("PageCount", UInt32),
        ("RecipientNumber", win32more.Foundation.PWSTR),
        ("RecipientName", win32more.Foundation.PWSTR),
        ("Tsid", win32more.Foundation.PWSTR),
        ("SenderName", win32more.Foundation.PWSTR),
        ("SenderCompany", win32more.Foundation.PWSTR),
        ("SenderDept", win32more.Foundation.PWSTR),
        ("BillingCode", win32more.Foundation.PWSTR),
        ("ScheduleAction", UInt32),
        ("ScheduleTime", win32more.Foundation.SYSTEMTIME),
        ("DeliveryReportType", UInt32),
        ("DeliveryReportAddress", win32more.Foundation.PWSTR),
        ("DocumentName", win32more.Foundation.PWSTR),
    ]
    return FAX_JOB_ENTRYW
def _define_FAX_PORT_INFOA_head():
    class FAX_PORT_INFOA(Structure):
        pass
    return FAX_PORT_INFOA
def _define_FAX_PORT_INFOA():
    FAX_PORT_INFOA = win32more.Devices.Fax.FAX_PORT_INFOA_head
    FAX_PORT_INFOA._fields_ = [
        ("SizeOfStruct", UInt32),
        ("DeviceId", UInt32),
        ("State", UInt32),
        ("Flags", UInt32),
        ("Rings", UInt32),
        ("Priority", UInt32),
        ("DeviceName", win32more.Foundation.PSTR),
        ("Tsid", win32more.Foundation.PSTR),
        ("Csid", win32more.Foundation.PSTR),
    ]
    return FAX_PORT_INFOA
def _define_FAX_PORT_INFOW_head():
    class FAX_PORT_INFOW(Structure):
        pass
    return FAX_PORT_INFOW
def _define_FAX_PORT_INFOW():
    FAX_PORT_INFOW = win32more.Devices.Fax.FAX_PORT_INFOW_head
    FAX_PORT_INFOW._fields_ = [
        ("SizeOfStruct", UInt32),
        ("DeviceId", UInt32),
        ("State", UInt32),
        ("Flags", UInt32),
        ("Rings", UInt32),
        ("Priority", UInt32),
        ("DeviceName", win32more.Foundation.PWSTR),
        ("Tsid", win32more.Foundation.PWSTR),
        ("Csid", win32more.Foundation.PWSTR),
    ]
    return FAX_PORT_INFOW
def _define_FAX_ROUTING_METHODA_head():
    class FAX_ROUTING_METHODA(Structure):
        pass
    return FAX_ROUTING_METHODA
def _define_FAX_ROUTING_METHODA():
    FAX_ROUTING_METHODA = win32more.Devices.Fax.FAX_ROUTING_METHODA_head
    FAX_ROUTING_METHODA._fields_ = [
        ("SizeOfStruct", UInt32),
        ("DeviceId", UInt32),
        ("Enabled", win32more.Foundation.BOOL),
        ("DeviceName", win32more.Foundation.PSTR),
        ("Guid", win32more.Foundation.PSTR),
        ("FriendlyName", win32more.Foundation.PSTR),
        ("FunctionName", win32more.Foundation.PSTR),
        ("ExtensionImageName", win32more.Foundation.PSTR),
        ("ExtensionFriendlyName", win32more.Foundation.PSTR),
    ]
    return FAX_ROUTING_METHODA
def _define_FAX_ROUTING_METHODW_head():
    class FAX_ROUTING_METHODW(Structure):
        pass
    return FAX_ROUTING_METHODW
def _define_FAX_ROUTING_METHODW():
    FAX_ROUTING_METHODW = win32more.Devices.Fax.FAX_ROUTING_METHODW_head
    FAX_ROUTING_METHODW._fields_ = [
        ("SizeOfStruct", UInt32),
        ("DeviceId", UInt32),
        ("Enabled", win32more.Foundation.BOOL),
        ("DeviceName", win32more.Foundation.PWSTR),
        ("Guid", win32more.Foundation.PWSTR),
        ("FriendlyName", win32more.Foundation.PWSTR),
        ("FunctionName", win32more.Foundation.PWSTR),
        ("ExtensionImageName", win32more.Foundation.PWSTR),
        ("ExtensionFriendlyName", win32more.Foundation.PWSTR),
    ]
    return FAX_ROUTING_METHODW
def _define_FAX_GLOBAL_ROUTING_INFOA_head():
    class FAX_GLOBAL_ROUTING_INFOA(Structure):
        pass
    return FAX_GLOBAL_ROUTING_INFOA
def _define_FAX_GLOBAL_ROUTING_INFOA():
    FAX_GLOBAL_ROUTING_INFOA = win32more.Devices.Fax.FAX_GLOBAL_ROUTING_INFOA_head
    FAX_GLOBAL_ROUTING_INFOA._fields_ = [
        ("SizeOfStruct", UInt32),
        ("Priority", UInt32),
        ("Guid", win32more.Foundation.PSTR),
        ("FriendlyName", win32more.Foundation.PSTR),
        ("FunctionName", win32more.Foundation.PSTR),
        ("ExtensionImageName", win32more.Foundation.PSTR),
        ("ExtensionFriendlyName", win32more.Foundation.PSTR),
    ]
    return FAX_GLOBAL_ROUTING_INFOA
def _define_FAX_GLOBAL_ROUTING_INFOW_head():
    class FAX_GLOBAL_ROUTING_INFOW(Structure):
        pass
    return FAX_GLOBAL_ROUTING_INFOW
def _define_FAX_GLOBAL_ROUTING_INFOW():
    FAX_GLOBAL_ROUTING_INFOW = win32more.Devices.Fax.FAX_GLOBAL_ROUTING_INFOW_head
    FAX_GLOBAL_ROUTING_INFOW._fields_ = [
        ("SizeOfStruct", UInt32),
        ("Priority", UInt32),
        ("Guid", win32more.Foundation.PWSTR),
        ("FriendlyName", win32more.Foundation.PWSTR),
        ("FunctionName", win32more.Foundation.PWSTR),
        ("ExtensionImageName", win32more.Foundation.PWSTR),
        ("ExtensionFriendlyName", win32more.Foundation.PWSTR),
    ]
    return FAX_GLOBAL_ROUTING_INFOW
def _define_FAX_COVERPAGE_INFOA_head():
    class FAX_COVERPAGE_INFOA(Structure):
        pass
    return FAX_COVERPAGE_INFOA
def _define_FAX_COVERPAGE_INFOA():
    FAX_COVERPAGE_INFOA = win32more.Devices.Fax.FAX_COVERPAGE_INFOA_head
    FAX_COVERPAGE_INFOA._fields_ = [
        ("SizeOfStruct", UInt32),
        ("CoverPageName", win32more.Foundation.PSTR),
        ("UseServerCoverPage", win32more.Foundation.BOOL),
        ("RecName", win32more.Foundation.PSTR),
        ("RecFaxNumber", win32more.Foundation.PSTR),
        ("RecCompany", win32more.Foundation.PSTR),
        ("RecStreetAddress", win32more.Foundation.PSTR),
        ("RecCity", win32more.Foundation.PSTR),
        ("RecState", win32more.Foundation.PSTR),
        ("RecZip", win32more.Foundation.PSTR),
        ("RecCountry", win32more.Foundation.PSTR),
        ("RecTitle", win32more.Foundation.PSTR),
        ("RecDepartment", win32more.Foundation.PSTR),
        ("RecOfficeLocation", win32more.Foundation.PSTR),
        ("RecHomePhone", win32more.Foundation.PSTR),
        ("RecOfficePhone", win32more.Foundation.PSTR),
        ("SdrName", win32more.Foundation.PSTR),
        ("SdrFaxNumber", win32more.Foundation.PSTR),
        ("SdrCompany", win32more.Foundation.PSTR),
        ("SdrAddress", win32more.Foundation.PSTR),
        ("SdrTitle", win32more.Foundation.PSTR),
        ("SdrDepartment", win32more.Foundation.PSTR),
        ("SdrOfficeLocation", win32more.Foundation.PSTR),
        ("SdrHomePhone", win32more.Foundation.PSTR),
        ("SdrOfficePhone", win32more.Foundation.PSTR),
        ("Note", win32more.Foundation.PSTR),
        ("Subject", win32more.Foundation.PSTR),
        ("TimeSent", win32more.Foundation.SYSTEMTIME),
        ("PageCount", UInt32),
    ]
    return FAX_COVERPAGE_INFOA
def _define_FAX_COVERPAGE_INFOW_head():
    class FAX_COVERPAGE_INFOW(Structure):
        pass
    return FAX_COVERPAGE_INFOW
def _define_FAX_COVERPAGE_INFOW():
    FAX_COVERPAGE_INFOW = win32more.Devices.Fax.FAX_COVERPAGE_INFOW_head
    FAX_COVERPAGE_INFOW._fields_ = [
        ("SizeOfStruct", UInt32),
        ("CoverPageName", win32more.Foundation.PWSTR),
        ("UseServerCoverPage", win32more.Foundation.BOOL),
        ("RecName", win32more.Foundation.PWSTR),
        ("RecFaxNumber", win32more.Foundation.PWSTR),
        ("RecCompany", win32more.Foundation.PWSTR),
        ("RecStreetAddress", win32more.Foundation.PWSTR),
        ("RecCity", win32more.Foundation.PWSTR),
        ("RecState", win32more.Foundation.PWSTR),
        ("RecZip", win32more.Foundation.PWSTR),
        ("RecCountry", win32more.Foundation.PWSTR),
        ("RecTitle", win32more.Foundation.PWSTR),
        ("RecDepartment", win32more.Foundation.PWSTR),
        ("RecOfficeLocation", win32more.Foundation.PWSTR),
        ("RecHomePhone", win32more.Foundation.PWSTR),
        ("RecOfficePhone", win32more.Foundation.PWSTR),
        ("SdrName", win32more.Foundation.PWSTR),
        ("SdrFaxNumber", win32more.Foundation.PWSTR),
        ("SdrCompany", win32more.Foundation.PWSTR),
        ("SdrAddress", win32more.Foundation.PWSTR),
        ("SdrTitle", win32more.Foundation.PWSTR),
        ("SdrDepartment", win32more.Foundation.PWSTR),
        ("SdrOfficeLocation", win32more.Foundation.PWSTR),
        ("SdrHomePhone", win32more.Foundation.PWSTR),
        ("SdrOfficePhone", win32more.Foundation.PWSTR),
        ("Note", win32more.Foundation.PWSTR),
        ("Subject", win32more.Foundation.PWSTR),
        ("TimeSent", win32more.Foundation.SYSTEMTIME),
        ("PageCount", UInt32),
    ]
    return FAX_COVERPAGE_INFOW
FAX_ENUM_JOB_SEND_ATTRIBUTES = Int32
JSA_NOW = 0
JSA_SPECIFIC_TIME = 1
JSA_DISCOUNT_PERIOD = 2
FAX_ENUM_DELIVERY_REPORT_TYPES = Int32
DRT_NONE = 0
DRT_EMAIL = 1
DRT_INBOX = 2
def _define_FAX_JOB_PARAMA_head():
    class FAX_JOB_PARAMA(Structure):
        pass
    return FAX_JOB_PARAMA
def _define_FAX_JOB_PARAMA():
    FAX_JOB_PARAMA = win32more.Devices.Fax.FAX_JOB_PARAMA_head
    FAX_JOB_PARAMA._fields_ = [
        ("SizeOfStruct", UInt32),
        ("RecipientNumber", win32more.Foundation.PSTR),
        ("RecipientName", win32more.Foundation.PSTR),
        ("Tsid", win32more.Foundation.PSTR),
        ("SenderName", win32more.Foundation.PSTR),
        ("SenderCompany", win32more.Foundation.PSTR),
        ("SenderDept", win32more.Foundation.PSTR),
        ("BillingCode", win32more.Foundation.PSTR),
        ("ScheduleAction", UInt32),
        ("ScheduleTime", win32more.Foundation.SYSTEMTIME),
        ("DeliveryReportType", UInt32),
        ("DeliveryReportAddress", win32more.Foundation.PSTR),
        ("DocumentName", win32more.Foundation.PSTR),
        ("CallHandle", UInt32),
        ("Reserved", UIntPtr * 3),
    ]
    return FAX_JOB_PARAMA
def _define_FAX_JOB_PARAMW_head():
    class FAX_JOB_PARAMW(Structure):
        pass
    return FAX_JOB_PARAMW
def _define_FAX_JOB_PARAMW():
    FAX_JOB_PARAMW = win32more.Devices.Fax.FAX_JOB_PARAMW_head
    FAX_JOB_PARAMW._fields_ = [
        ("SizeOfStruct", UInt32),
        ("RecipientNumber", win32more.Foundation.PWSTR),
        ("RecipientName", win32more.Foundation.PWSTR),
        ("Tsid", win32more.Foundation.PWSTR),
        ("SenderName", win32more.Foundation.PWSTR),
        ("SenderCompany", win32more.Foundation.PWSTR),
        ("SenderDept", win32more.Foundation.PWSTR),
        ("BillingCode", win32more.Foundation.PWSTR),
        ("ScheduleAction", UInt32),
        ("ScheduleTime", win32more.Foundation.SYSTEMTIME),
        ("DeliveryReportType", UInt32),
        ("DeliveryReportAddress", win32more.Foundation.PWSTR),
        ("DocumentName", win32more.Foundation.PWSTR),
        ("CallHandle", UInt32),
        ("Reserved", UIntPtr * 3),
    ]
    return FAX_JOB_PARAMW
def _define_FAX_EVENTA_head():
    class FAX_EVENTA(Structure):
        pass
    return FAX_EVENTA
def _define_FAX_EVENTA():
    FAX_EVENTA = win32more.Devices.Fax.FAX_EVENTA_head
    FAX_EVENTA._fields_ = [
        ("SizeOfStruct", UInt32),
        ("TimeStamp", win32more.Foundation.FILETIME),
        ("DeviceId", UInt32),
        ("EventId", UInt32),
        ("JobId", UInt32),
    ]
    return FAX_EVENTA
def _define_FAX_EVENTW_head():
    class FAX_EVENTW(Structure):
        pass
    return FAX_EVENTW
def _define_FAX_EVENTW():
    FAX_EVENTW = win32more.Devices.Fax.FAX_EVENTW_head
    FAX_EVENTW._fields_ = [
        ("SizeOfStruct", UInt32),
        ("TimeStamp", win32more.Foundation.FILETIME),
        ("DeviceId", UInt32),
        ("EventId", UInt32),
        ("JobId", UInt32),
    ]
    return FAX_EVENTW
def _define_FAX_PRINT_INFOA_head():
    class FAX_PRINT_INFOA(Structure):
        pass
    return FAX_PRINT_INFOA
def _define_FAX_PRINT_INFOA():
    FAX_PRINT_INFOA = win32more.Devices.Fax.FAX_PRINT_INFOA_head
    FAX_PRINT_INFOA._fields_ = [
        ("SizeOfStruct", UInt32),
        ("DocName", win32more.Foundation.PSTR),
        ("RecipientName", win32more.Foundation.PSTR),
        ("RecipientNumber", win32more.Foundation.PSTR),
        ("SenderName", win32more.Foundation.PSTR),
        ("SenderCompany", win32more.Foundation.PSTR),
        ("SenderDept", win32more.Foundation.PSTR),
        ("SenderBillingCode", win32more.Foundation.PSTR),
        ("Reserved", win32more.Foundation.PSTR),
        ("DrEmailAddress", win32more.Foundation.PSTR),
        ("OutputFileName", win32more.Foundation.PSTR),
    ]
    return FAX_PRINT_INFOA
def _define_FAX_PRINT_INFOW_head():
    class FAX_PRINT_INFOW(Structure):
        pass
    return FAX_PRINT_INFOW
def _define_FAX_PRINT_INFOW():
    FAX_PRINT_INFOW = win32more.Devices.Fax.FAX_PRINT_INFOW_head
    FAX_PRINT_INFOW._fields_ = [
        ("SizeOfStruct", UInt32),
        ("DocName", win32more.Foundation.PWSTR),
        ("RecipientName", win32more.Foundation.PWSTR),
        ("RecipientNumber", win32more.Foundation.PWSTR),
        ("SenderName", win32more.Foundation.PWSTR),
        ("SenderCompany", win32more.Foundation.PWSTR),
        ("SenderDept", win32more.Foundation.PWSTR),
        ("SenderBillingCode", win32more.Foundation.PWSTR),
        ("Reserved", win32more.Foundation.PWSTR),
        ("DrEmailAddress", win32more.Foundation.PWSTR),
        ("OutputFileName", win32more.Foundation.PWSTR),
    ]
    return FAX_PRINT_INFOW
def _define_FAX_CONTEXT_INFOA_head():
    class FAX_CONTEXT_INFOA(Structure):
        pass
    return FAX_CONTEXT_INFOA
def _define_FAX_CONTEXT_INFOA():
    FAX_CONTEXT_INFOA = win32more.Devices.Fax.FAX_CONTEXT_INFOA_head
    FAX_CONTEXT_INFOA._fields_ = [
        ("SizeOfStruct", UInt32),
        ("hDC", win32more.Graphics.Gdi.HDC),
        ("ServerName", win32more.Foundation.CHAR * 16),
    ]
    return FAX_CONTEXT_INFOA
def _define_FAX_CONTEXT_INFOW_head():
    class FAX_CONTEXT_INFOW(Structure):
        pass
    return FAX_CONTEXT_INFOW
def _define_FAX_CONTEXT_INFOW():
    FAX_CONTEXT_INFOW = win32more.Devices.Fax.FAX_CONTEXT_INFOW_head
    FAX_CONTEXT_INFOW._fields_ = [
        ("SizeOfStruct", UInt32),
        ("hDC", win32more.Graphics.Gdi.HDC),
        ("ServerName", Char * 16),
    ]
    return FAX_CONTEXT_INFOW
def _define_PFAXCONNECTFAXSERVERA():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,POINTER(win32more.Foundation.HANDLE), use_last_error=False)
def _define_PFAXCONNECTFAXSERVERW():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.HANDLE), use_last_error=False)
def _define_PFAXCLOSE():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE, use_last_error=False)
FAX_ENUM_PORT_OPEN_TYPE = Int32
PORT_OPEN_QUERY = 1
PORT_OPEN_MODIFY = 2
def _define_PFAXOPENPORT():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,UInt32,POINTER(win32more.Foundation.HANDLE), use_last_error=False)
def _define_PFAXCOMPLETEJOBPARAMSA():
    return CFUNCTYPE(win32more.Foundation.BOOL,POINTER(POINTER(win32more.Devices.Fax.FAX_JOB_PARAMA_head)),POINTER(POINTER(win32more.Devices.Fax.FAX_COVERPAGE_INFOA_head)), use_last_error=False)
def _define_PFAXCOMPLETEJOBPARAMSW():
    return CFUNCTYPE(win32more.Foundation.BOOL,POINTER(POINTER(win32more.Devices.Fax.FAX_JOB_PARAMW_head)),POINTER(POINTER(win32more.Devices.Fax.FAX_COVERPAGE_INFOW_head)), use_last_error=False)
def _define_PFAXSENDDOCUMENTA():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,POINTER(win32more.Devices.Fax.FAX_JOB_PARAMA_head),POINTER(win32more.Devices.Fax.FAX_COVERPAGE_INFOA_head),POINTER(UInt32), use_last_error=False)
def _define_PFAXSENDDOCUMENTW():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,POINTER(win32more.Devices.Fax.FAX_JOB_PARAMW_head),POINTER(win32more.Devices.Fax.FAX_COVERPAGE_INFOW_head),POINTER(UInt32), use_last_error=False)
def _define_PFAX_RECIPIENT_CALLBACKA():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,c_void_p,POINTER(win32more.Devices.Fax.FAX_JOB_PARAMA_head),POINTER(win32more.Devices.Fax.FAX_COVERPAGE_INFOA_head), use_last_error=False)
def _define_PFAX_RECIPIENT_CALLBACKW():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,c_void_p,POINTER(win32more.Devices.Fax.FAX_JOB_PARAMW_head),POINTER(win32more.Devices.Fax.FAX_COVERPAGE_INFOW_head), use_last_error=False)
def _define_PFAXSENDDOCUMENTFORBROADCASTA():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,POINTER(UInt32),win32more.Devices.Fax.PFAX_RECIPIENT_CALLBACKA,c_void_p, use_last_error=False)
def _define_PFAXSENDDOCUMENTFORBROADCASTW():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,POINTER(UInt32),win32more.Devices.Fax.PFAX_RECIPIENT_CALLBACKW,c_void_p, use_last_error=False)
def _define_PFAXENUMJOBSA():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_JOB_ENTRYA_head)),POINTER(UInt32), use_last_error=False)
def _define_PFAXENUMJOBSW():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_JOB_ENTRYW_head)),POINTER(UInt32), use_last_error=False)
def _define_PFAXGETJOBA():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,POINTER(POINTER(win32more.Devices.Fax.FAX_JOB_ENTRYA_head)), use_last_error=False)
def _define_PFAXGETJOBW():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,POINTER(POINTER(win32more.Devices.Fax.FAX_JOB_ENTRYW_head)), use_last_error=False)
def _define_PFAXSETJOBA():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,UInt32,POINTER(win32more.Devices.Fax.FAX_JOB_ENTRYA_head), use_last_error=False)
def _define_PFAXSETJOBW():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,UInt32,POINTER(win32more.Devices.Fax.FAX_JOB_ENTRYW_head), use_last_error=False)
def _define_PFAXGETPAGEDATA():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,POINTER(c_char_p_no),POINTER(UInt32),POINTER(UInt32),POINTER(UInt32), use_last_error=False)
def _define_PFAXGETDEVICESTATUSA():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_DEVICE_STATUSA_head)), use_last_error=False)
def _define_PFAXGETDEVICESTATUSW():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_DEVICE_STATUSW_head)), use_last_error=False)
def _define_PFAXABORT():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32, use_last_error=False)
def _define_PFAXGETCONFIGURATIONA():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_CONFIGURATIONA_head)), use_last_error=False)
def _define_PFAXGETCONFIGURATIONW():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_CONFIGURATIONW_head)), use_last_error=False)
def _define_PFAXSETCONFIGURATIONA():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Fax.FAX_CONFIGURATIONA_head), use_last_error=False)
def _define_PFAXSETCONFIGURATIONW():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Fax.FAX_CONFIGURATIONW_head), use_last_error=False)
def _define_PFAXGETLOGGINGCATEGORIESA():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_LOG_CATEGORYA_head)),POINTER(UInt32), use_last_error=False)
def _define_PFAXGETLOGGINGCATEGORIESW():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_LOG_CATEGORYW_head)),POINTER(UInt32), use_last_error=False)
def _define_PFAXSETLOGGINGCATEGORIESA():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Fax.FAX_LOG_CATEGORYA_head),UInt32, use_last_error=False)
def _define_PFAXSETLOGGINGCATEGORIESW():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Fax.FAX_LOG_CATEGORYW_head),UInt32, use_last_error=False)
def _define_PFAXENUMPORTSA():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_PORT_INFOA_head)),POINTER(UInt32), use_last_error=False)
def _define_PFAXENUMPORTSW():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_PORT_INFOW_head)),POINTER(UInt32), use_last_error=False)
def _define_PFAXGETPORTA():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_PORT_INFOA_head)), use_last_error=False)
def _define_PFAXGETPORTW():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_PORT_INFOW_head)), use_last_error=False)
def _define_PFAXSETPORTA():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Fax.FAX_PORT_INFOA_head), use_last_error=False)
def _define_PFAXSETPORTW():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Fax.FAX_PORT_INFOW_head), use_last_error=False)
def _define_PFAXENUMROUTINGMETHODSA():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_ROUTING_METHODA_head)),POINTER(UInt32), use_last_error=False)
def _define_PFAXENUMROUTINGMETHODSW():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_ROUTING_METHODW_head)),POINTER(UInt32), use_last_error=False)
def _define_PFAXENABLEROUTINGMETHODA():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,win32more.Foundation.BOOL, use_last_error=False)
def _define_PFAXENABLEROUTINGMETHODW():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,win32more.Foundation.BOOL, use_last_error=False)
def _define_PFAXENUMGLOBALROUTINGINFOA():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_GLOBAL_ROUTING_INFOA_head)),POINTER(UInt32), use_last_error=False)
def _define_PFAXENUMGLOBALROUTINGINFOW():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_GLOBAL_ROUTING_INFOW_head)),POINTER(UInt32), use_last_error=False)
def _define_PFAXSETGLOBALROUTINGINFOA():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Fax.FAX_GLOBAL_ROUTING_INFOA_head), use_last_error=False)
def _define_PFAXSETGLOBALROUTINGINFOW():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Fax.FAX_GLOBAL_ROUTING_INFOW_head), use_last_error=False)
def _define_PFAXGETROUTINGINFOA():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,POINTER(c_char_p_no),POINTER(UInt32), use_last_error=False)
def _define_PFAXGETROUTINGINFOW():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,POINTER(c_char_p_no),POINTER(UInt32), use_last_error=False)
def _define_PFAXSETROUTINGINFOA():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,c_char_p_no,UInt32, use_last_error=False)
def _define_PFAXSETROUTINGINFOW():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,c_char_p_no,UInt32, use_last_error=False)
def _define_PFAXINITIALIZEEVENTQUEUE():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,UIntPtr,win32more.Foundation.HWND,UInt32, use_last_error=False)
def _define_PFAXFREEBUFFER():
    return CFUNCTYPE(Void,c_void_p, use_last_error=False)
def _define_PFAXSTARTPRINTJOBA():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,POINTER(win32more.Devices.Fax.FAX_PRINT_INFOA_head),POINTER(UInt32),POINTER(win32more.Devices.Fax.FAX_CONTEXT_INFOA_head), use_last_error=False)
def _define_PFAXSTARTPRINTJOBW():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,POINTER(win32more.Devices.Fax.FAX_PRINT_INFOW_head),POINTER(UInt32),POINTER(win32more.Devices.Fax.FAX_CONTEXT_INFOW_head), use_last_error=False)
def _define_PFAXPRINTCOVERPAGEA():
    return CFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Fax.FAX_CONTEXT_INFOA_head),POINTER(win32more.Devices.Fax.FAX_COVERPAGE_INFOA_head), use_last_error=False)
def _define_PFAXPRINTCOVERPAGEW():
    return CFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Fax.FAX_CONTEXT_INFOW_head),POINTER(win32more.Devices.Fax.FAX_COVERPAGE_INFOW_head), use_last_error=False)
def _define_PFAXREGISTERSERVICEPROVIDERW():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)
def _define_PFAXUNREGISTERSERVICEPROVIDERW():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR, use_last_error=False)
def _define_PFAX_ROUTING_INSTALLATION_CALLBACKW():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,c_void_p,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)
def _define_PFAXREGISTERROUTINGEXTENSIONW():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Devices.Fax.PFAX_ROUTING_INSTALLATION_CALLBACKW,c_void_p, use_last_error=False)
def _define_PFAXACCESSCHECK():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32, use_last_error=False)
def _define_FAX_SEND_head():
    class FAX_SEND(Structure):
        pass
    return FAX_SEND
def _define_FAX_SEND():
    FAX_SEND = win32more.Devices.Fax.FAX_SEND_head
    FAX_SEND._fields_ = [
        ("SizeOfStruct", UInt32),
        ("FileName", win32more.Foundation.PWSTR),
        ("CallerName", win32more.Foundation.PWSTR),
        ("CallerNumber", win32more.Foundation.PWSTR),
        ("ReceiverName", win32more.Foundation.PWSTR),
        ("ReceiverNumber", win32more.Foundation.PWSTR),
        ("Branding", win32more.Foundation.BOOL),
        ("CallHandle", UInt32),
        ("Reserved", UInt32 * 3),
    ]
    return FAX_SEND
def _define_FAX_RECEIVE_head():
    class FAX_RECEIVE(Structure):
        pass
    return FAX_RECEIVE
def _define_FAX_RECEIVE():
    FAX_RECEIVE = win32more.Devices.Fax.FAX_RECEIVE_head
    FAX_RECEIVE._fields_ = [
        ("SizeOfStruct", UInt32),
        ("FileName", win32more.Foundation.PWSTR),
        ("ReceiverName", win32more.Foundation.PWSTR),
        ("ReceiverNumber", win32more.Foundation.PWSTR),
        ("Reserved", UInt32 * 4),
    ]
    return FAX_RECEIVE
def _define_FAX_DEV_STATUS_head():
    class FAX_DEV_STATUS(Structure):
        pass
    return FAX_DEV_STATUS
def _define_FAX_DEV_STATUS():
    FAX_DEV_STATUS = win32more.Devices.Fax.FAX_DEV_STATUS_head
    FAX_DEV_STATUS._fields_ = [
        ("SizeOfStruct", UInt32),
        ("StatusId", UInt32),
        ("StringId", UInt32),
        ("PageCount", UInt32),
        ("CSI", win32more.Foundation.PWSTR),
        ("CallerId", win32more.Foundation.PWSTR),
        ("RoutingInfo", win32more.Foundation.PWSTR),
        ("ErrorCode", UInt32),
        ("Reserved", UInt32 * 3),
    ]
    return FAX_DEV_STATUS
def _define_PFAX_SERVICE_CALLBACK():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,UIntPtr,UIntPtr,UIntPtr, use_last_error=False)
def _define_PFAX_LINECALLBACK():
    return CFUNCTYPE(Void,win32more.Foundation.HANDLE,UInt32,UInt32,UIntPtr,UIntPtr,UIntPtr,UIntPtr, use_last_error=False)
def _define_PFAX_SEND_CALLBACK():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,UInt32,UInt32, use_last_error=False)
def _define_PFAXDEVINITIALIZE():
    return CFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Fax.PFAX_LINECALLBACK),win32more.Devices.Fax.PFAX_SERVICE_CALLBACK, use_last_error=False)
def _define_PFAXDEVVIRTUALDEVICECREATION():
    return CFUNCTYPE(win32more.Foundation.BOOL,POINTER(UInt32),POINTER(Char),POINTER(UInt32),win32more.Foundation.HANDLE,UIntPtr, use_last_error=False)
def _define_PFAXDEVSTARTJOB():
    return CFUNCTYPE(win32more.Foundation.BOOL,UInt32,UInt32,POINTER(win32more.Foundation.HANDLE),win32more.Foundation.HANDLE,UIntPtr, use_last_error=False)
def _define_PFAXDEVENDJOB():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE, use_last_error=False)
def _define_PFAXDEVSEND():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Fax.FAX_SEND_head),win32more.Devices.Fax.PFAX_SEND_CALLBACK, use_last_error=False)
def _define_PFAXDEVRECEIVE():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,POINTER(win32more.Devices.Fax.FAX_RECEIVE_head), use_last_error=False)
def _define_PFAXDEVREPORTSTATUS():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Fax.FAX_DEV_STATUS_head),UInt32,POINTER(UInt32), use_last_error=False)
def _define_PFAXDEVABORTOPERATION():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE, use_last_error=False)
def _define_PFAXDEVCONFIGURE():
    return CFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.UI.Controls.HPROPSHEETPAGE), use_last_error=False)
def _define_PFAXDEVSHUTDOWN():
    return CFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)
FaxServer = Guid('cda8acb0-8cf5-4f6c-9ba2-5931d40c8cae')
FaxDeviceProviders = Guid('eb8fe768-875a-4f5f-82c5-03f23aac1bd7')
FaxDevices = Guid('5589e28e-23cb-4919-8808-e6101846e80d')
FaxInboundRouting = Guid('e80248ed-ad65-4218-8108-991924d4e7ed')
FaxFolders = Guid('c35211d7-5776-48cb-af44-c31be3b2cfe5')
FaxLoggingOptions = Guid('1bf9eea6-ece0-4785-a18b-de56e9eef96a')
FaxActivity = Guid('cfef5d0e-e84d-462e-aabb-87d31eb04fef')
FaxOutboundRouting = Guid('c81b385e-b869-4afd-86c0-616498ed9be2')
FaxReceiptOptions = Guid('6982487b-227b-4c96-a61c-248348b05ab6')
FaxSecurity = Guid('10c4ddde-abf0-43df-964f-7f3ac21a4c7b')
FaxDocument = Guid('0f3f9f91-c838-415e-a4f3-3e828ca445e0')
FaxSender = Guid('265d84d0-1850-4360-b7c8-758bbb5f0b96')
FaxRecipients = Guid('ea9bdf53-10a9-4d4f-a067-63c8f84f01b0')
FaxIncomingArchive = Guid('8426c56a-35a1-4c6f-af93-fc952422e2c2')
FaxIncomingQueue = Guid('69131717-f3f1-40e3-809d-a6cbf7bd85e5')
FaxOutgoingArchive = Guid('43c28403-e04f-474d-990c-b94669148f59')
FaxOutgoingQueue = Guid('7421169e-8c43-4b0d-bb16-645c8fa40357')
FaxIncomingMessageIterator = Guid('6088e1d8-3fc8-45c2-87b1-909a29607ea9')
FaxIncomingMessage = Guid('1932fcf7-9d43-4d5a-89ff-03861b321736')
FaxOutgoingJobs = Guid('92bf2a6c-37be-43fa-a37d-cb0e5f753b35')
FaxOutgoingJob = Guid('71bb429c-0ef9-4915-bec5-a5d897a3e924')
FaxOutgoingMessageIterator = Guid('8a3224d0-d30b-49de-9813-cb385790fbbb')
FaxOutgoingMessage = Guid('91b4a378-4ad8-4aef-a4dc-97d96e939a3a')
FaxIncomingJobs = Guid('a1bb8a43-8866-4fb7-a15d-6266c875a5cc')
FaxIncomingJob = Guid('c47311ec-ae32-41b8-ae4b-3eae0629d0c9')
FaxDeviceProvider = Guid('17cf1aa3-f5eb-484a-9c9a-4440a5baabfc')
FaxDevice = Guid('59e3a5b2-d676-484b-a6de-720bfa89b5af')
FaxActivityLogging = Guid('f0a0294e-3bbd-48b8-8f13-8c591a55bdbc')
FaxEventLogging = Guid('a6850930-a0f6-4a6f-95b7-db2ebf3d02e3')
FaxOutboundRoutingGroups = Guid('ccbea1a5-e2b4-4b57-9421-b04b6289464b')
FaxOutboundRoutingGroup = Guid('0213f3e0-6791-4d77-a271-04d2357c50d6')
FaxDeviceIds = Guid('cdc539ea-7277-460e-8de0-48a0a5760d1f')
FaxOutboundRoutingRules = Guid('d385beca-e624-4473-bfaa-9f4000831f54')
FaxOutboundRoutingRule = Guid('6549eebf-08d1-475a-828b-3bf105952fa0')
FaxInboundRoutingExtensions = Guid('189a48ed-623c-4c0d-80f2-d66c7b9efec2')
FaxInboundRoutingExtension = Guid('1d7dfb51-7207-4436-a0d9-24e32ee56988')
FaxInboundRoutingMethods = Guid('25fcb76a-b750-4b82-9266-fbbbae8922ba')
FaxInboundRoutingMethod = Guid('4b9fd75c-0194-4b72-9ce5-02a8205ac7d4')
FaxJobStatus = Guid('7bf222f4-be8d-442f-841d-6132742423bb')
FaxRecipient = Guid('60bf3301-7df8-4bd8-9148-7b5801f9efdf')
FaxConfiguration = Guid('5857326f-e7b3-41a7-9c19-a91b463e2d56')
FaxAccountSet = Guid('fbc23c4b-79e0-4291-bc56-c12e253bbf3a')
FaxAccounts = Guid('da1f94aa-ee2c-47c0-8f4f-2a217075b76e')
FaxAccount = Guid('a7e0647f-4524-4464-a56d-b9fe666f715e')
FaxAccountFolders = Guid('85398f49-c034-4a3f-821c-db7d685e8129')
FaxAccountIncomingQueue = Guid('9bcf6094-b4da-45f4-b8d6-ddeb2186652c')
FaxAccountOutgoingQueue = Guid('feeceefb-c149-48ba-bab8-b791e101f62f')
FaxAccountIncomingArchive = Guid('14b33db5-4c40-4ecf-9ef8-a360cbe809ed')
FaxAccountOutgoingArchive = Guid('851e7af5-433a-4739-a2df-ad245c2cb98e')
FaxSecurity2 = Guid('735c1248-ec89-4c30-a127-656e92e3c4ea')
FAX_JOB_STATUS_ENUM = Int32
FAX_JOB_STATUS_ENUM_fjsPENDING = 1
FAX_JOB_STATUS_ENUM_fjsINPROGRESS = 2
FAX_JOB_STATUS_ENUM_fjsFAILED = 8
FAX_JOB_STATUS_ENUM_fjsPAUSED = 16
FAX_JOB_STATUS_ENUM_fjsNOLINE = 32
FAX_JOB_STATUS_ENUM_fjsRETRYING = 64
FAX_JOB_STATUS_ENUM_fjsRETRIES_EXCEEDED = 128
FAX_JOB_STATUS_ENUM_fjsCOMPLETED = 256
FAX_JOB_STATUS_ENUM_fjsCANCELED = 512
FAX_JOB_STATUS_ENUM_fjsCANCELING = 1024
FAX_JOB_STATUS_ENUM_fjsROUTING = 2048
FAX_JOB_EXTENDED_STATUS_ENUM = Int32
FAX_JOB_EXTENDED_STATUS_ENUM_fjesNONE = 0
FAX_JOB_EXTENDED_STATUS_ENUM_fjesDISCONNECTED = 1
FAX_JOB_EXTENDED_STATUS_ENUM_fjesINITIALIZING = 2
FAX_JOB_EXTENDED_STATUS_ENUM_fjesDIALING = 3
FAX_JOB_EXTENDED_STATUS_ENUM_fjesTRANSMITTING = 4
FAX_JOB_EXTENDED_STATUS_ENUM_fjesANSWERED = 5
FAX_JOB_EXTENDED_STATUS_ENUM_fjesRECEIVING = 6
FAX_JOB_EXTENDED_STATUS_ENUM_fjesLINE_UNAVAILABLE = 7
FAX_JOB_EXTENDED_STATUS_ENUM_fjesBUSY = 8
FAX_JOB_EXTENDED_STATUS_ENUM_fjesNO_ANSWER = 9
FAX_JOB_EXTENDED_STATUS_ENUM_fjesBAD_ADDRESS = 10
FAX_JOB_EXTENDED_STATUS_ENUM_fjesNO_DIAL_TONE = 11
FAX_JOB_EXTENDED_STATUS_ENUM_fjesFATAL_ERROR = 12
FAX_JOB_EXTENDED_STATUS_ENUM_fjesCALL_DELAYED = 13
FAX_JOB_EXTENDED_STATUS_ENUM_fjesCALL_BLACKLISTED = 14
FAX_JOB_EXTENDED_STATUS_ENUM_fjesNOT_FAX_CALL = 15
FAX_JOB_EXTENDED_STATUS_ENUM_fjesPARTIALLY_RECEIVED = 16
FAX_JOB_EXTENDED_STATUS_ENUM_fjesHANDLED = 17
FAX_JOB_EXTENDED_STATUS_ENUM_fjesCALL_COMPLETED = 18
FAX_JOB_EXTENDED_STATUS_ENUM_fjesCALL_ABORTED = 19
FAX_JOB_EXTENDED_STATUS_ENUM_fjesPROPRIETARY = 16777216
FAX_JOB_OPERATIONS_ENUM = Int32
FAX_JOB_OPERATIONS_ENUM_fjoVIEW = 1
FAX_JOB_OPERATIONS_ENUM_fjoPAUSE = 2
FAX_JOB_OPERATIONS_ENUM_fjoRESUME = 4
FAX_JOB_OPERATIONS_ENUM_fjoRESTART = 8
FAX_JOB_OPERATIONS_ENUM_fjoDELETE = 16
FAX_JOB_OPERATIONS_ENUM_fjoRECIPIENT_INFO = 32
FAX_JOB_OPERATIONS_ENUM_fjoSENDER_INFO = 64
FAX_JOB_TYPE_ENUM = Int32
FAX_JOB_TYPE_ENUM_fjtSEND = 0
FAX_JOB_TYPE_ENUM_fjtRECEIVE = 1
FAX_JOB_TYPE_ENUM_fjtROUTING = 2
def _define_IFaxJobStatus_head():
    class IFaxJobStatus(win32more.System.Com.IDispatch_head):
        Guid = Guid('8b86f485-fd7f-4824-886b-40c5caa617cc')
    return IFaxJobStatus
def _define_IFaxJobStatus():
    IFaxJobStatus = win32more.Devices.Fax.IFaxJobStatus_head
    IFaxJobStatus.get_Status = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_JOB_STATUS_ENUM), use_last_error=False)(7, 'get_Status', ((1, 'pStatus'),)))
    IFaxJobStatus.get_Pages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_Pages', ((1, 'plPages'),)))
    IFaxJobStatus.get_Size = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_Size', ((1, 'plSize'),)))
    IFaxJobStatus.get_CurrentPage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(10, 'get_CurrentPage', ((1, 'plCurrentPage'),)))
    IFaxJobStatus.get_DeviceId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(11, 'get_DeviceId', ((1, 'plDeviceId'),)))
    IFaxJobStatus.get_CSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(12, 'get_CSID', ((1, 'pbstrCSID'),)))
    IFaxJobStatus.get_TSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(13, 'get_TSID', ((1, 'pbstrTSID'),)))
    IFaxJobStatus.get_ExtendedStatusCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_JOB_EXTENDED_STATUS_ENUM), use_last_error=False)(14, 'get_ExtendedStatusCode', ((1, 'pExtendedStatusCode'),)))
    IFaxJobStatus.get_ExtendedStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(15, 'get_ExtendedStatus', ((1, 'pbstrExtendedStatus'),)))
    IFaxJobStatus.get_AvailableOperations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_JOB_OPERATIONS_ENUM), use_last_error=False)(16, 'get_AvailableOperations', ((1, 'pAvailableOperations'),)))
    IFaxJobStatus.get_Retries = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(17, 'get_Retries', ((1, 'plRetries'),)))
    IFaxJobStatus.get_JobType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_JOB_TYPE_ENUM), use_last_error=False)(18, 'get_JobType', ((1, 'pJobType'),)))
    IFaxJobStatus.get_ScheduledTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(19, 'get_ScheduledTime', ((1, 'pdateScheduledTime'),)))
    IFaxJobStatus.get_TransmissionStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(20, 'get_TransmissionStart', ((1, 'pdateTransmissionStart'),)))
    IFaxJobStatus.get_TransmissionEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(21, 'get_TransmissionEnd', ((1, 'pdateTransmissionEnd'),)))
    IFaxJobStatus.get_CallerId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(22, 'get_CallerId', ((1, 'pbstrCallerId'),)))
    IFaxJobStatus.get_RoutingInformation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(23, 'get_RoutingInformation', ((1, 'pbstrRoutingInformation'),)))
    return IFaxJobStatus
FAX_SERVER_EVENTS_TYPE_ENUM = Int32
FAX_SERVER_EVENTS_TYPE_ENUM_fsetNONE = 0
FAX_SERVER_EVENTS_TYPE_ENUM_fsetIN_QUEUE = 1
FAX_SERVER_EVENTS_TYPE_ENUM_fsetOUT_QUEUE = 2
FAX_SERVER_EVENTS_TYPE_ENUM_fsetCONFIG = 4
FAX_SERVER_EVENTS_TYPE_ENUM_fsetACTIVITY = 8
FAX_SERVER_EVENTS_TYPE_ENUM_fsetQUEUE_STATE = 16
FAX_SERVER_EVENTS_TYPE_ENUM_fsetIN_ARCHIVE = 32
FAX_SERVER_EVENTS_TYPE_ENUM_fsetOUT_ARCHIVE = 64
FAX_SERVER_EVENTS_TYPE_ENUM_fsetFXSSVC_ENDED = 128
FAX_SERVER_EVENTS_TYPE_ENUM_fsetDEVICE_STATUS = 256
FAX_SERVER_EVENTS_TYPE_ENUM_fsetINCOMING_CALL = 512
FAX_SERVER_APIVERSION_ENUM = Int32
fsAPI_VERSION_0 = 0
fsAPI_VERSION_1 = 65536
fsAPI_VERSION_2 = 131072
fsAPI_VERSION_3 = 196608
def _define_IFaxServer_head():
    class IFaxServer(win32more.System.Com.IDispatch_head):
        Guid = Guid('475b6469-90a5-4878-a577-17a86e8e3462')
    return IFaxServer
def _define_IFaxServer():
    IFaxServer = win32more.Devices.Fax.IFaxServer_head
    IFaxServer.Connect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(7, 'Connect', ((1, 'bstrServerName'),)))
    IFaxServer.get_ServerName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'get_ServerName', ((1, 'pbstrServerName'),)))
    IFaxServer.GetDeviceProviders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxDeviceProviders_head), use_last_error=False)(9, 'GetDeviceProviders', ((1, 'ppFaxDeviceProviders'),)))
    IFaxServer.GetDevices = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxDevices_head), use_last_error=False)(10, 'GetDevices', ((1, 'ppFaxDevices'),)))
    IFaxServer.get_InboundRouting = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxInboundRouting_head), use_last_error=False)(11, 'get_InboundRouting', ((1, 'ppFaxInboundRouting'),)))
    IFaxServer.get_Folders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxFolders_head), use_last_error=False)(12, 'get_Folders', ((1, 'pFaxFolders'),)))
    IFaxServer.get_LoggingOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxLoggingOptions_head), use_last_error=False)(13, 'get_LoggingOptions', ((1, 'ppFaxLoggingOptions'),)))
    IFaxServer.get_MajorVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(14, 'get_MajorVersion', ((1, 'plMajorVersion'),)))
    IFaxServer.get_MinorVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(15, 'get_MinorVersion', ((1, 'plMinorVersion'),)))
    IFaxServer.get_MajorBuild = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(16, 'get_MajorBuild', ((1, 'plMajorBuild'),)))
    IFaxServer.get_MinorBuild = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(17, 'get_MinorBuild', ((1, 'plMinorBuild'),)))
    IFaxServer.get_Debug = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(18, 'get_Debug', ((1, 'pbDebug'),)))
    IFaxServer.get_Activity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxActivity_head), use_last_error=False)(19, 'get_Activity', ((1, 'ppFaxActivity'),)))
    IFaxServer.get_OutboundRouting = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxOutboundRouting_head), use_last_error=False)(20, 'get_OutboundRouting', ((1, 'ppFaxOutboundRouting'),)))
    IFaxServer.get_ReceiptOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxReceiptOptions_head), use_last_error=False)(21, 'get_ReceiptOptions', ((1, 'ppFaxReceiptOptions'),)))
    IFaxServer.get_Security = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxSecurity_head), use_last_error=False)(22, 'get_Security', ((1, 'ppFaxSecurity'),)))
    IFaxServer.Disconnect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(23, 'Disconnect', ()))
    IFaxServer.GetExtensionProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(24, 'GetExtensionProperty', ((1, 'bstrGUID'),(1, 'pvProperty'),)))
    IFaxServer.SetExtensionProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(25, 'SetExtensionProperty', ((1, 'bstrGUID'),(1, 'vProperty'),)))
    IFaxServer.ListenToServerEvents = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.FAX_SERVER_EVENTS_TYPE_ENUM, use_last_error=False)(26, 'ListenToServerEvents', ((1, 'EventTypes'),)))
    IFaxServer.RegisterDeviceProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32, use_last_error=False)(27, 'RegisterDeviceProvider', ((1, 'bstrGUID'),(1, 'bstrFriendlyName'),(1, 'bstrImageName'),(1, 'TspName'),(1, 'lFSPIVersion'),)))
    IFaxServer.UnregisterDeviceProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(28, 'UnregisterDeviceProvider', ((1, 'bstrUniqueName'),)))
    IFaxServer.RegisterInboundRoutingExtension = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(29, 'RegisterInboundRoutingExtension', ((1, 'bstrExtensionName'),(1, 'bstrFriendlyName'),(1, 'bstrImageName'),(1, 'vMethods'),)))
    IFaxServer.UnregisterInboundRoutingExtension = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(30, 'UnregisterInboundRoutingExtension', ((1, 'bstrExtensionUniqueName'),)))
    IFaxServer.get_RegisteredEvents = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_SERVER_EVENTS_TYPE_ENUM), use_last_error=False)(31, 'get_RegisteredEvents', ((1, 'pEventTypes'),)))
    IFaxServer.get_APIVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_SERVER_APIVERSION_ENUM), use_last_error=False)(32, 'get_APIVersion', ((1, 'pAPIVersion'),)))
    return IFaxServer
def _define_IFaxDeviceProviders_head():
    class IFaxDeviceProviders(win32more.System.Com.IDispatch_head):
        Guid = Guid('9fb76f62-4c7e-43a5-b6fd-502893f7e13e')
    return IFaxDeviceProviders
def _define_IFaxDeviceProviders():
    IFaxDeviceProviders = win32more.Devices.Fax.IFaxDeviceProviders_head
    IFaxDeviceProviders.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(7, 'get__NewEnum', ((1, 'ppUnk'),)))
    IFaxDeviceProviders.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.Devices.Fax.IFaxDeviceProvider_head), use_last_error=False)(8, 'get_Item', ((1, 'vIndex'),(1, 'pFaxDeviceProvider'),)))
    IFaxDeviceProviders.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_Count', ((1, 'plCount'),)))
    return IFaxDeviceProviders
def _define_IFaxDevices_head():
    class IFaxDevices(win32more.System.Com.IDispatch_head):
        Guid = Guid('9e46783e-f34f-482e-a360-0416becbbd96')
    return IFaxDevices
def _define_IFaxDevices():
    IFaxDevices = win32more.Devices.Fax.IFaxDevices_head
    IFaxDevices.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(7, 'get__NewEnum', ((1, 'ppUnk'),)))
    IFaxDevices.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.Devices.Fax.IFaxDevice_head), use_last_error=False)(8, 'get_Item', ((1, 'vIndex'),(1, 'pFaxDevice'),)))
    IFaxDevices.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_Count', ((1, 'plCount'),)))
    IFaxDevices.get_ItemById = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Devices.Fax.IFaxDevice_head), use_last_error=False)(10, 'get_ItemById', ((1, 'lId'),(1, 'ppFaxDevice'),)))
    return IFaxDevices
def _define_IFaxInboundRouting_head():
    class IFaxInboundRouting(win32more.System.Com.IDispatch_head):
        Guid = Guid('8148c20f-9d52-45b1-bf96-38fc12713527')
    return IFaxInboundRouting
def _define_IFaxInboundRouting():
    IFaxInboundRouting = win32more.Devices.Fax.IFaxInboundRouting_head
    IFaxInboundRouting.GetExtensions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxInboundRoutingExtensions_head), use_last_error=False)(7, 'GetExtensions', ((1, 'pFaxInboundRoutingExtensions'),)))
    IFaxInboundRouting.GetMethods = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxInboundRoutingMethods_head), use_last_error=False)(8, 'GetMethods', ((1, 'pFaxInboundRoutingMethods'),)))
    return IFaxInboundRouting
def _define_IFaxFolders_head():
    class IFaxFolders(win32more.System.Com.IDispatch_head):
        Guid = Guid('dce3b2a8-a7ab-42bc-9d0a-3149457261a0')
    return IFaxFolders
def _define_IFaxFolders():
    IFaxFolders = win32more.Devices.Fax.IFaxFolders_head
    IFaxFolders.get_OutgoingQueue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxOutgoingQueue_head), use_last_error=False)(7, 'get_OutgoingQueue', ((1, 'pFaxOutgoingQueue'),)))
    IFaxFolders.get_IncomingQueue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxIncomingQueue_head), use_last_error=False)(8, 'get_IncomingQueue', ((1, 'pFaxIncomingQueue'),)))
    IFaxFolders.get_IncomingArchive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxIncomingArchive_head), use_last_error=False)(9, 'get_IncomingArchive', ((1, 'pFaxIncomingArchive'),)))
    IFaxFolders.get_OutgoingArchive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxOutgoingArchive_head), use_last_error=False)(10, 'get_OutgoingArchive', ((1, 'pFaxOutgoingArchive'),)))
    return IFaxFolders
def _define_IFaxLoggingOptions_head():
    class IFaxLoggingOptions(win32more.System.Com.IDispatch_head):
        Guid = Guid('34e64fb9-6b31-4d32-8b27-d286c0c33606')
    return IFaxLoggingOptions
def _define_IFaxLoggingOptions():
    IFaxLoggingOptions = win32more.Devices.Fax.IFaxLoggingOptions_head
    IFaxLoggingOptions.get_EventLogging = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxEventLogging_head), use_last_error=False)(7, 'get_EventLogging', ((1, 'pFaxEventLogging'),)))
    IFaxLoggingOptions.get_ActivityLogging = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxActivityLogging_head), use_last_error=False)(8, 'get_ActivityLogging', ((1, 'pFaxActivityLogging'),)))
    return IFaxLoggingOptions
def _define_IFaxActivity_head():
    class IFaxActivity(win32more.System.Com.IDispatch_head):
        Guid = Guid('4b106f97-3df5-40f2-bc3c-44cb8115ebdf')
    return IFaxActivity
def _define_IFaxActivity():
    IFaxActivity = win32more.Devices.Fax.IFaxActivity_head
    IFaxActivity.get_IncomingMessages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_IncomingMessages', ((1, 'plIncomingMessages'),)))
    IFaxActivity.get_RoutingMessages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_RoutingMessages', ((1, 'plRoutingMessages'),)))
    IFaxActivity.get_OutgoingMessages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_OutgoingMessages', ((1, 'plOutgoingMessages'),)))
    IFaxActivity.get_QueuedMessages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(10, 'get_QueuedMessages', ((1, 'plQueuedMessages'),)))
    IFaxActivity.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(11, 'Refresh', ()))
    return IFaxActivity
def _define_IFaxOutboundRouting_head():
    class IFaxOutboundRouting(win32more.System.Com.IDispatch_head):
        Guid = Guid('25dc05a4-9909-41bd-a95b-7e5d1dec1d43')
    return IFaxOutboundRouting
def _define_IFaxOutboundRouting():
    IFaxOutboundRouting = win32more.Devices.Fax.IFaxOutboundRouting_head
    IFaxOutboundRouting.GetGroups = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxOutboundRoutingGroups_head), use_last_error=False)(7, 'GetGroups', ((1, 'pFaxOutboundRoutingGroups'),)))
    IFaxOutboundRouting.GetRules = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxOutboundRoutingRules_head), use_last_error=False)(8, 'GetRules', ((1, 'pFaxOutboundRoutingRules'),)))
    return IFaxOutboundRouting
FAX_SMTP_AUTHENTICATION_TYPE_ENUM = Int32
FAX_SMTP_AUTHENTICATION_TYPE_ENUM_fsatANONYMOUS = 0
FAX_SMTP_AUTHENTICATION_TYPE_ENUM_fsatBASIC = 1
FAX_SMTP_AUTHENTICATION_TYPE_ENUM_fsatNTLM = 2
FAX_RECEIPT_TYPE_ENUM = Int32
FAX_RECEIPT_TYPE_ENUM_frtNONE = 0
FAX_RECEIPT_TYPE_ENUM_frtMAIL = 1
FAX_RECEIPT_TYPE_ENUM_frtMSGBOX = 4
def _define_IFaxReceiptOptions_head():
    class IFaxReceiptOptions(win32more.System.Com.IDispatch_head):
        Guid = Guid('378efaeb-5fcb-4afb-b2ee-e16e80614487')
    return IFaxReceiptOptions
def _define_IFaxReceiptOptions():
    IFaxReceiptOptions = win32more.Devices.Fax.IFaxReceiptOptions_head
    IFaxReceiptOptions.get_AuthenticationType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_SMTP_AUTHENTICATION_TYPE_ENUM), use_last_error=False)(7, 'get_AuthenticationType', ((1, 'pType'),)))
    IFaxReceiptOptions.put_AuthenticationType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.FAX_SMTP_AUTHENTICATION_TYPE_ENUM, use_last_error=False)(8, 'put_AuthenticationType', ((1, 'Type'),)))
    IFaxReceiptOptions.get_SMTPServer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_SMTPServer', ((1, 'pbstrSMTPServer'),)))
    IFaxReceiptOptions.put_SMTPServer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(10, 'put_SMTPServer', ((1, 'bstrSMTPServer'),)))
    IFaxReceiptOptions.get_SMTPPort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(11, 'get_SMTPPort', ((1, 'plSMTPPort'),)))
    IFaxReceiptOptions.put_SMTPPort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(12, 'put_SMTPPort', ((1, 'lSMTPPort'),)))
    IFaxReceiptOptions.get_SMTPSender = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(13, 'get_SMTPSender', ((1, 'pbstrSMTPSender'),)))
    IFaxReceiptOptions.put_SMTPSender = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(14, 'put_SMTPSender', ((1, 'bstrSMTPSender'),)))
    IFaxReceiptOptions.get_SMTPUser = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(15, 'get_SMTPUser', ((1, 'pbstrSMTPUser'),)))
    IFaxReceiptOptions.put_SMTPUser = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(16, 'put_SMTPUser', ((1, 'bstrSMTPUser'),)))
    IFaxReceiptOptions.get_AllowedReceipts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_RECEIPT_TYPE_ENUM), use_last_error=False)(17, 'get_AllowedReceipts', ((1, 'pAllowedReceipts'),)))
    IFaxReceiptOptions.put_AllowedReceipts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.FAX_RECEIPT_TYPE_ENUM, use_last_error=False)(18, 'put_AllowedReceipts', ((1, 'AllowedReceipts'),)))
    IFaxReceiptOptions.get_SMTPPassword = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(19, 'get_SMTPPassword', ((1, 'pbstrSMTPPassword'),)))
    IFaxReceiptOptions.put_SMTPPassword = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(20, 'put_SMTPPassword', ((1, 'bstrSMTPPassword'),)))
    IFaxReceiptOptions.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(21, 'Refresh', ()))
    IFaxReceiptOptions.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(22, 'Save', ()))
    IFaxReceiptOptions.get_UseForInboundRouting = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(23, 'get_UseForInboundRouting', ((1, 'pbUseForInboundRouting'),)))
    IFaxReceiptOptions.put_UseForInboundRouting = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(24, 'put_UseForInboundRouting', ((1, 'bUseForInboundRouting'),)))
    return IFaxReceiptOptions
FAX_ACCESS_RIGHTS_ENUM = Int32
farSUBMIT_LOW = 1
farSUBMIT_NORMAL = 2
farSUBMIT_HIGH = 4
farQUERY_JOBS = 8
farMANAGE_JOBS = 16
farQUERY_CONFIG = 32
farMANAGE_CONFIG = 64
farQUERY_IN_ARCHIVE = 128
farMANAGE_IN_ARCHIVE = 256
farQUERY_OUT_ARCHIVE = 512
farMANAGE_OUT_ARCHIVE = 1024
def _define_IFaxSecurity_head():
    class IFaxSecurity(win32more.System.Com.IDispatch_head):
        Guid = Guid('77b508c1-09c0-47a2-91eb-fce7fdf2690e')
    return IFaxSecurity
def _define_IFaxSecurity():
    IFaxSecurity = win32more.Devices.Fax.IFaxSecurity_head
    IFaxSecurity.get_Descriptor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(7, 'get_Descriptor', ((1, 'pvDescriptor'),)))
    IFaxSecurity.put_Descriptor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(8, 'put_Descriptor', ((1, 'vDescriptor'),)))
    IFaxSecurity.get_GrantedRights = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_ACCESS_RIGHTS_ENUM), use_last_error=False)(9, 'get_GrantedRights', ((1, 'pGrantedRights'),)))
    IFaxSecurity.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(10, 'Refresh', ()))
    IFaxSecurity.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(11, 'Save', ()))
    IFaxSecurity.get_InformationType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(12, 'get_InformationType', ((1, 'plInformationType'),)))
    IFaxSecurity.put_InformationType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(13, 'put_InformationType', ((1, 'lInformationType'),)))
    return IFaxSecurity
FAX_PRIORITY_TYPE_ENUM = Int32
FAX_PRIORITY_TYPE_ENUM_fptLOW = 0
FAX_PRIORITY_TYPE_ENUM_fptNORMAL = 1
FAX_PRIORITY_TYPE_ENUM_fptHIGH = 2
FAX_COVERPAGE_TYPE_ENUM = Int32
FAX_COVERPAGE_TYPE_ENUM_fcptNONE = 0
FAX_COVERPAGE_TYPE_ENUM_fcptLOCAL = 1
FAX_COVERPAGE_TYPE_ENUM_fcptSERVER = 2
FAX_SCHEDULE_TYPE_ENUM = Int32
FAX_SCHEDULE_TYPE_ENUM_fstNOW = 0
FAX_SCHEDULE_TYPE_ENUM_fstSPECIFIC_TIME = 1
FAX_SCHEDULE_TYPE_ENUM_fstDISCOUNT_PERIOD = 2
def _define_IFaxDocument_head():
    class IFaxDocument(win32more.System.Com.IDispatch_head):
        Guid = Guid('b207a246-09e3-4a4e-a7dc-fea31d29458f')
    return IFaxDocument
def _define_IFaxDocument():
    IFaxDocument = win32more.Devices.Fax.IFaxDocument_head
    IFaxDocument.get_Body = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_Body', ((1, 'pbstrBody'),)))
    IFaxDocument.put_Body = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'put_Body', ((1, 'bstrBody'),)))
    IFaxDocument.get_Sender = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxSender_head), use_last_error=False)(9, 'get_Sender', ((1, 'ppFaxSender'),)))
    IFaxDocument.get_Recipients = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxRecipients_head), use_last_error=False)(10, 'get_Recipients', ((1, 'ppFaxRecipients'),)))
    IFaxDocument.get_CoverPage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'get_CoverPage', ((1, 'pbstrCoverPage'),)))
    IFaxDocument.put_CoverPage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(12, 'put_CoverPage', ((1, 'bstrCoverPage'),)))
    IFaxDocument.get_Subject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(13, 'get_Subject', ((1, 'pbstrSubject'),)))
    IFaxDocument.put_Subject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(14, 'put_Subject', ((1, 'bstrSubject'),)))
    IFaxDocument.get_Note = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(15, 'get_Note', ((1, 'pbstrNote'),)))
    IFaxDocument.put_Note = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(16, 'put_Note', ((1, 'bstrNote'),)))
    IFaxDocument.get_ScheduleTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(17, 'get_ScheduleTime', ((1, 'pdateScheduleTime'),)))
    IFaxDocument.put_ScheduleTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(18, 'put_ScheduleTime', ((1, 'dateScheduleTime'),)))
    IFaxDocument.get_ReceiptAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(19, 'get_ReceiptAddress', ((1, 'pbstrReceiptAddress'),)))
    IFaxDocument.put_ReceiptAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(20, 'put_ReceiptAddress', ((1, 'bstrReceiptAddress'),)))
    IFaxDocument.get_DocumentName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(21, 'get_DocumentName', ((1, 'pbstrDocumentName'),)))
    IFaxDocument.put_DocumentName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(22, 'put_DocumentName', ((1, 'bstrDocumentName'),)))
    IFaxDocument.get_CallHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(23, 'get_CallHandle', ((1, 'plCallHandle'),)))
    IFaxDocument.put_CallHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(24, 'put_CallHandle', ((1, 'lCallHandle'),)))
    IFaxDocument.get_CoverPageType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_COVERPAGE_TYPE_ENUM), use_last_error=False)(25, 'get_CoverPageType', ((1, 'pCoverPageType'),)))
    IFaxDocument.put_CoverPageType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.FAX_COVERPAGE_TYPE_ENUM, use_last_error=False)(26, 'put_CoverPageType', ((1, 'CoverPageType'),)))
    IFaxDocument.get_ScheduleType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_SCHEDULE_TYPE_ENUM), use_last_error=False)(27, 'get_ScheduleType', ((1, 'pScheduleType'),)))
    IFaxDocument.put_ScheduleType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.FAX_SCHEDULE_TYPE_ENUM, use_last_error=False)(28, 'put_ScheduleType', ((1, 'ScheduleType'),)))
    IFaxDocument.get_ReceiptType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_RECEIPT_TYPE_ENUM), use_last_error=False)(29, 'get_ReceiptType', ((1, 'pReceiptType'),)))
    IFaxDocument.put_ReceiptType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.FAX_RECEIPT_TYPE_ENUM, use_last_error=False)(30, 'put_ReceiptType', ((1, 'ReceiptType'),)))
    IFaxDocument.get_GroupBroadcastReceipts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(31, 'get_GroupBroadcastReceipts', ((1, 'pbUseGrouping'),)))
    IFaxDocument.put_GroupBroadcastReceipts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(32, 'put_GroupBroadcastReceipts', ((1, 'bUseGrouping'),)))
    IFaxDocument.get_Priority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_PRIORITY_TYPE_ENUM), use_last_error=False)(33, 'get_Priority', ((1, 'pPriority'),)))
    IFaxDocument.put_Priority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.FAX_PRIORITY_TYPE_ENUM, use_last_error=False)(34, 'put_Priority', ((1, 'Priority'),)))
    IFaxDocument.get_TapiConnection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(35, 'get_TapiConnection', ((1, 'ppTapiConnection'),)))
    IFaxDocument.putref_TapiConnection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head, use_last_error=False)(36, 'putref_TapiConnection', ((1, 'pTapiConnection'),)))
    IFaxDocument.Submit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(37, 'Submit', ((1, 'bstrFaxServerName'),(1, 'pvFaxOutgoingJobIDs'),)))
    IFaxDocument.ConnectedSubmit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer_head,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(38, 'ConnectedSubmit', ((1, 'pFaxServer'),(1, 'pvFaxOutgoingJobIDs'),)))
    IFaxDocument.get_AttachFaxToReceipt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(39, 'get_AttachFaxToReceipt', ((1, 'pbAttachFax'),)))
    IFaxDocument.put_AttachFaxToReceipt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(40, 'put_AttachFaxToReceipt', ((1, 'bAttachFax'),)))
    return IFaxDocument
def _define_IFaxSender_head():
    class IFaxSender(win32more.System.Com.IDispatch_head):
        Guid = Guid('0d879d7d-f57a-4cc6-a6f9-3ee5d527b46a')
    return IFaxSender
def _define_IFaxSender():
    IFaxSender = win32more.Devices.Fax.IFaxSender_head
    IFaxSender.get_BillingCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_BillingCode', ((1, 'pbstrBillingCode'),)))
    IFaxSender.put_BillingCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'put_BillingCode', ((1, 'bstrBillingCode'),)))
    IFaxSender.get_City = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_City', ((1, 'pbstrCity'),)))
    IFaxSender.put_City = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(10, 'put_City', ((1, 'bstrCity'),)))
    IFaxSender.get_Company = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'get_Company', ((1, 'pbstrCompany'),)))
    IFaxSender.put_Company = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(12, 'put_Company', ((1, 'bstrCompany'),)))
    IFaxSender.get_Country = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(13, 'get_Country', ((1, 'pbstrCountry'),)))
    IFaxSender.put_Country = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(14, 'put_Country', ((1, 'bstrCountry'),)))
    IFaxSender.get_Department = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(15, 'get_Department', ((1, 'pbstrDepartment'),)))
    IFaxSender.put_Department = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(16, 'put_Department', ((1, 'bstrDepartment'),)))
    IFaxSender.get_Email = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(17, 'get_Email', ((1, 'pbstrEmail'),)))
    IFaxSender.put_Email = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(18, 'put_Email', ((1, 'bstrEmail'),)))
    IFaxSender.get_FaxNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(19, 'get_FaxNumber', ((1, 'pbstrFaxNumber'),)))
    IFaxSender.put_FaxNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(20, 'put_FaxNumber', ((1, 'bstrFaxNumber'),)))
    IFaxSender.get_HomePhone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(21, 'get_HomePhone', ((1, 'pbstrHomePhone'),)))
    IFaxSender.put_HomePhone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(22, 'put_HomePhone', ((1, 'bstrHomePhone'),)))
    IFaxSender.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(23, 'get_Name', ((1, 'pbstrName'),)))
    IFaxSender.put_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(24, 'put_Name', ((1, 'bstrName'),)))
    IFaxSender.get_TSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(25, 'get_TSID', ((1, 'pbstrTSID'),)))
    IFaxSender.put_TSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(26, 'put_TSID', ((1, 'bstrTSID'),)))
    IFaxSender.get_OfficePhone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(27, 'get_OfficePhone', ((1, 'pbstrOfficePhone'),)))
    IFaxSender.put_OfficePhone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(28, 'put_OfficePhone', ((1, 'bstrOfficePhone'),)))
    IFaxSender.get_OfficeLocation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(29, 'get_OfficeLocation', ((1, 'pbstrOfficeLocation'),)))
    IFaxSender.put_OfficeLocation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(30, 'put_OfficeLocation', ((1, 'bstrOfficeLocation'),)))
    IFaxSender.get_State = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(31, 'get_State', ((1, 'pbstrState'),)))
    IFaxSender.put_State = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(32, 'put_State', ((1, 'bstrState'),)))
    IFaxSender.get_StreetAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(33, 'get_StreetAddress', ((1, 'pbstrStreetAddress'),)))
    IFaxSender.put_StreetAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(34, 'put_StreetAddress', ((1, 'bstrStreetAddress'),)))
    IFaxSender.get_Title = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(35, 'get_Title', ((1, 'pbstrTitle'),)))
    IFaxSender.put_Title = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(36, 'put_Title', ((1, 'bstrTitle'),)))
    IFaxSender.get_ZipCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(37, 'get_ZipCode', ((1, 'pbstrZipCode'),)))
    IFaxSender.put_ZipCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(38, 'put_ZipCode', ((1, 'bstrZipCode'),)))
    IFaxSender.LoadDefaultSender = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(39, 'LoadDefaultSender', ()))
    IFaxSender.SaveDefaultSender = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(40, 'SaveDefaultSender', ()))
    return IFaxSender
def _define_IFaxRecipient_head():
    class IFaxRecipient(win32more.System.Com.IDispatch_head):
        Guid = Guid('9a3da3a0-538d-42b6-9444-aaa57d0ce2bc')
    return IFaxRecipient
def _define_IFaxRecipient():
    IFaxRecipient = win32more.Devices.Fax.IFaxRecipient_head
    IFaxRecipient.get_FaxNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_FaxNumber', ((1, 'pbstrFaxNumber'),)))
    IFaxRecipient.put_FaxNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'put_FaxNumber', ((1, 'bstrFaxNumber'),)))
    IFaxRecipient.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_Name', ((1, 'pbstrName'),)))
    IFaxRecipient.put_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(10, 'put_Name', ((1, 'bstrName'),)))
    return IFaxRecipient
def _define_IFaxRecipients_head():
    class IFaxRecipients(win32more.System.Com.IDispatch_head):
        Guid = Guid('b9c9de5a-894e-4492-9fa3-08c627c11d5d')
    return IFaxRecipients
def _define_IFaxRecipients():
    IFaxRecipients = win32more.Devices.Fax.IFaxRecipients_head
    IFaxRecipients.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(7, 'get__NewEnum', ((1, 'ppUnk'),)))
    IFaxRecipients.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Devices.Fax.IFaxRecipient_head), use_last_error=False)(8, 'get_Item', ((1, 'lIndex'),(1, 'ppFaxRecipient'),)))
    IFaxRecipients.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_Count', ((1, 'plCount'),)))
    IFaxRecipients.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.Devices.Fax.IFaxRecipient_head), use_last_error=False)(10, 'Add', ((1, 'bstrFaxNumber'),(1, 'bstrRecipientName'),(1, 'ppFaxRecipient'),)))
    IFaxRecipients.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(11, 'Remove', ((1, 'lIndex'),)))
    return IFaxRecipients
def _define_IFaxIncomingArchive_head():
    class IFaxIncomingArchive(win32more.System.Com.IDispatch_head):
        Guid = Guid('76062cc7-f714-4fbd-aa06-ed6e4a4b70f3')
    return IFaxIncomingArchive
def _define_IFaxIncomingArchive():
    IFaxIncomingArchive = win32more.Devices.Fax.IFaxIncomingArchive_head
    IFaxIncomingArchive.get_UseArchive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(7, 'get_UseArchive', ((1, 'pbUseArchive'),)))
    IFaxIncomingArchive.put_UseArchive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(8, 'put_UseArchive', ((1, 'bUseArchive'),)))
    IFaxIncomingArchive.get_ArchiveFolder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_ArchiveFolder', ((1, 'pbstrArchiveFolder'),)))
    IFaxIncomingArchive.put_ArchiveFolder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(10, 'put_ArchiveFolder', ((1, 'bstrArchiveFolder'),)))
    IFaxIncomingArchive.get_SizeQuotaWarning = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(11, 'get_SizeQuotaWarning', ((1, 'pbSizeQuotaWarning'),)))
    IFaxIncomingArchive.put_SizeQuotaWarning = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(12, 'put_SizeQuotaWarning', ((1, 'bSizeQuotaWarning'),)))
    IFaxIncomingArchive.get_HighQuotaWaterMark = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(13, 'get_HighQuotaWaterMark', ((1, 'plHighQuotaWaterMark'),)))
    IFaxIncomingArchive.put_HighQuotaWaterMark = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(14, 'put_HighQuotaWaterMark', ((1, 'lHighQuotaWaterMark'),)))
    IFaxIncomingArchive.get_LowQuotaWaterMark = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(15, 'get_LowQuotaWaterMark', ((1, 'plLowQuotaWaterMark'),)))
    IFaxIncomingArchive.put_LowQuotaWaterMark = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(16, 'put_LowQuotaWaterMark', ((1, 'lLowQuotaWaterMark'),)))
    IFaxIncomingArchive.get_AgeLimit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(17, 'get_AgeLimit', ((1, 'plAgeLimit'),)))
    IFaxIncomingArchive.put_AgeLimit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(18, 'put_AgeLimit', ((1, 'lAgeLimit'),)))
    IFaxIncomingArchive.get_SizeLow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(19, 'get_SizeLow', ((1, 'plSizeLow'),)))
    IFaxIncomingArchive.get_SizeHigh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(20, 'get_SizeHigh', ((1, 'plSizeHigh'),)))
    IFaxIncomingArchive.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(21, 'Refresh', ()))
    IFaxIncomingArchive.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(22, 'Save', ()))
    IFaxIncomingArchive.GetMessages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Devices.Fax.IFaxIncomingMessageIterator_head), use_last_error=False)(23, 'GetMessages', ((1, 'lPrefetchSize'),(1, 'pFaxIncomingMessageIterator'),)))
    IFaxIncomingArchive.GetMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Devices.Fax.IFaxIncomingMessage_head), use_last_error=False)(24, 'GetMessage', ((1, 'bstrMessageId'),(1, 'pFaxIncomingMessage'),)))
    return IFaxIncomingArchive
def _define_IFaxIncomingQueue_head():
    class IFaxIncomingQueue(win32more.System.Com.IDispatch_head):
        Guid = Guid('902e64ef-8fd8-4b75-9725-6014df161545')
    return IFaxIncomingQueue
def _define_IFaxIncomingQueue():
    IFaxIncomingQueue = win32more.Devices.Fax.IFaxIncomingQueue_head
    IFaxIncomingQueue.get_Blocked = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(7, 'get_Blocked', ((1, 'pbBlocked'),)))
    IFaxIncomingQueue.put_Blocked = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(8, 'put_Blocked', ((1, 'bBlocked'),)))
    IFaxIncomingQueue.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(9, 'Refresh', ()))
    IFaxIncomingQueue.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(10, 'Save', ()))
    IFaxIncomingQueue.GetJobs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxIncomingJobs_head), use_last_error=False)(11, 'GetJobs', ((1, 'pFaxIncomingJobs'),)))
    IFaxIncomingQueue.GetJob = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Devices.Fax.IFaxIncomingJob_head), use_last_error=False)(12, 'GetJob', ((1, 'bstrJobId'),(1, 'pFaxIncomingJob'),)))
    return IFaxIncomingQueue
def _define_IFaxOutgoingArchive_head():
    class IFaxOutgoingArchive(win32more.System.Com.IDispatch_head):
        Guid = Guid('c9c28f40-8d80-4e53-810f-9a79919b49fd')
    return IFaxOutgoingArchive
def _define_IFaxOutgoingArchive():
    IFaxOutgoingArchive = win32more.Devices.Fax.IFaxOutgoingArchive_head
    IFaxOutgoingArchive.get_UseArchive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(7, 'get_UseArchive', ((1, 'pbUseArchive'),)))
    IFaxOutgoingArchive.put_UseArchive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(8, 'put_UseArchive', ((1, 'bUseArchive'),)))
    IFaxOutgoingArchive.get_ArchiveFolder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_ArchiveFolder', ((1, 'pbstrArchiveFolder'),)))
    IFaxOutgoingArchive.put_ArchiveFolder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(10, 'put_ArchiveFolder', ((1, 'bstrArchiveFolder'),)))
    IFaxOutgoingArchive.get_SizeQuotaWarning = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(11, 'get_SizeQuotaWarning', ((1, 'pbSizeQuotaWarning'),)))
    IFaxOutgoingArchive.put_SizeQuotaWarning = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(12, 'put_SizeQuotaWarning', ((1, 'bSizeQuotaWarning'),)))
    IFaxOutgoingArchive.get_HighQuotaWaterMark = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(13, 'get_HighQuotaWaterMark', ((1, 'plHighQuotaWaterMark'),)))
    IFaxOutgoingArchive.put_HighQuotaWaterMark = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(14, 'put_HighQuotaWaterMark', ((1, 'lHighQuotaWaterMark'),)))
    IFaxOutgoingArchive.get_LowQuotaWaterMark = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(15, 'get_LowQuotaWaterMark', ((1, 'plLowQuotaWaterMark'),)))
    IFaxOutgoingArchive.put_LowQuotaWaterMark = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(16, 'put_LowQuotaWaterMark', ((1, 'lLowQuotaWaterMark'),)))
    IFaxOutgoingArchive.get_AgeLimit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(17, 'get_AgeLimit', ((1, 'plAgeLimit'),)))
    IFaxOutgoingArchive.put_AgeLimit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(18, 'put_AgeLimit', ((1, 'lAgeLimit'),)))
    IFaxOutgoingArchive.get_SizeLow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(19, 'get_SizeLow', ((1, 'plSizeLow'),)))
    IFaxOutgoingArchive.get_SizeHigh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(20, 'get_SizeHigh', ((1, 'plSizeHigh'),)))
    IFaxOutgoingArchive.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(21, 'Refresh', ()))
    IFaxOutgoingArchive.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(22, 'Save', ()))
    IFaxOutgoingArchive.GetMessages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Devices.Fax.IFaxOutgoingMessageIterator_head), use_last_error=False)(23, 'GetMessages', ((1, 'lPrefetchSize'),(1, 'pFaxOutgoingMessageIterator'),)))
    IFaxOutgoingArchive.GetMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Devices.Fax.IFaxOutgoingMessage_head), use_last_error=False)(24, 'GetMessage', ((1, 'bstrMessageId'),(1, 'pFaxOutgoingMessage'),)))
    return IFaxOutgoingArchive
def _define_IFaxOutgoingQueue_head():
    class IFaxOutgoingQueue(win32more.System.Com.IDispatch_head):
        Guid = Guid('80b1df24-d9ac-4333-b373-487cedc80ce5')
    return IFaxOutgoingQueue
def _define_IFaxOutgoingQueue():
    IFaxOutgoingQueue = win32more.Devices.Fax.IFaxOutgoingQueue_head
    IFaxOutgoingQueue.get_Blocked = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(7, 'get_Blocked', ((1, 'pbBlocked'),)))
    IFaxOutgoingQueue.put_Blocked = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(8, 'put_Blocked', ((1, 'bBlocked'),)))
    IFaxOutgoingQueue.get_Paused = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(9, 'get_Paused', ((1, 'pbPaused'),)))
    IFaxOutgoingQueue.put_Paused = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(10, 'put_Paused', ((1, 'bPaused'),)))
    IFaxOutgoingQueue.get_AllowPersonalCoverPages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(11, 'get_AllowPersonalCoverPages', ((1, 'pbAllowPersonalCoverPages'),)))
    IFaxOutgoingQueue.put_AllowPersonalCoverPages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(12, 'put_AllowPersonalCoverPages', ((1, 'bAllowPersonalCoverPages'),)))
    IFaxOutgoingQueue.get_UseDeviceTSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(13, 'get_UseDeviceTSID', ((1, 'pbUseDeviceTSID'),)))
    IFaxOutgoingQueue.put_UseDeviceTSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(14, 'put_UseDeviceTSID', ((1, 'bUseDeviceTSID'),)))
    IFaxOutgoingQueue.get_Retries = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(15, 'get_Retries', ((1, 'plRetries'),)))
    IFaxOutgoingQueue.put_Retries = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(16, 'put_Retries', ((1, 'lRetries'),)))
    IFaxOutgoingQueue.get_RetryDelay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(17, 'get_RetryDelay', ((1, 'plRetryDelay'),)))
    IFaxOutgoingQueue.put_RetryDelay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(18, 'put_RetryDelay', ((1, 'lRetryDelay'),)))
    IFaxOutgoingQueue.get_DiscountRateStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(19, 'get_DiscountRateStart', ((1, 'pdateDiscountRateStart'),)))
    IFaxOutgoingQueue.put_DiscountRateStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(20, 'put_DiscountRateStart', ((1, 'dateDiscountRateStart'),)))
    IFaxOutgoingQueue.get_DiscountRateEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(21, 'get_DiscountRateEnd', ((1, 'pdateDiscountRateEnd'),)))
    IFaxOutgoingQueue.put_DiscountRateEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(22, 'put_DiscountRateEnd', ((1, 'dateDiscountRateEnd'),)))
    IFaxOutgoingQueue.get_AgeLimit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(23, 'get_AgeLimit', ((1, 'plAgeLimit'),)))
    IFaxOutgoingQueue.put_AgeLimit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(24, 'put_AgeLimit', ((1, 'lAgeLimit'),)))
    IFaxOutgoingQueue.get_Branding = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(25, 'get_Branding', ((1, 'pbBranding'),)))
    IFaxOutgoingQueue.put_Branding = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(26, 'put_Branding', ((1, 'bBranding'),)))
    IFaxOutgoingQueue.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(27, 'Refresh', ()))
    IFaxOutgoingQueue.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(28, 'Save', ()))
    IFaxOutgoingQueue.GetJobs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxOutgoingJobs_head), use_last_error=False)(29, 'GetJobs', ((1, 'pFaxOutgoingJobs'),)))
    IFaxOutgoingQueue.GetJob = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Devices.Fax.IFaxOutgoingJob_head), use_last_error=False)(30, 'GetJob', ((1, 'bstrJobId'),(1, 'pFaxOutgoingJob'),)))
    return IFaxOutgoingQueue
def _define_IFaxIncomingMessageIterator_head():
    class IFaxIncomingMessageIterator(win32more.System.Com.IDispatch_head):
        Guid = Guid('fd73ecc4-6f06-4f52-82a8-f7ba06ae3108')
    return IFaxIncomingMessageIterator
def _define_IFaxIncomingMessageIterator():
    IFaxIncomingMessageIterator = win32more.Devices.Fax.IFaxIncomingMessageIterator_head
    IFaxIncomingMessageIterator.get_Message = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxIncomingMessage_head), use_last_error=False)(7, 'get_Message', ((1, 'pFaxIncomingMessage'),)))
    IFaxIncomingMessageIterator.get_PrefetchSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_PrefetchSize', ((1, 'plPrefetchSize'),)))
    IFaxIncomingMessageIterator.put_PrefetchSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(9, 'put_PrefetchSize', ((1, 'lPrefetchSize'),)))
    IFaxIncomingMessageIterator.get_AtEOF = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(10, 'get_AtEOF', ((1, 'pbEOF'),)))
    IFaxIncomingMessageIterator.MoveFirst = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(11, 'MoveFirst', ()))
    IFaxIncomingMessageIterator.MoveNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'MoveNext', ()))
    return IFaxIncomingMessageIterator
def _define_IFaxIncomingMessage_head():
    class IFaxIncomingMessage(win32more.System.Com.IDispatch_head):
        Guid = Guid('7cab88fa-2ef9-4851-b2f3-1d148fed8447')
    return IFaxIncomingMessage
def _define_IFaxIncomingMessage():
    IFaxIncomingMessage = win32more.Devices.Fax.IFaxIncomingMessage_head
    IFaxIncomingMessage.get_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_Id', ((1, 'pbstrId'),)))
    IFaxIncomingMessage.get_Pages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_Pages', ((1, 'plPages'),)))
    IFaxIncomingMessage.get_Size = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_Size', ((1, 'plSize'),)))
    IFaxIncomingMessage.get_DeviceName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'get_DeviceName', ((1, 'pbstrDeviceName'),)))
    IFaxIncomingMessage.get_Retries = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(11, 'get_Retries', ((1, 'plRetries'),)))
    IFaxIncomingMessage.get_TransmissionStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(12, 'get_TransmissionStart', ((1, 'pdateTransmissionStart'),)))
    IFaxIncomingMessage.get_TransmissionEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(13, 'get_TransmissionEnd', ((1, 'pdateTransmissionEnd'),)))
    IFaxIncomingMessage.get_CSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(14, 'get_CSID', ((1, 'pbstrCSID'),)))
    IFaxIncomingMessage.get_TSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(15, 'get_TSID', ((1, 'pbstrTSID'),)))
    IFaxIncomingMessage.get_CallerId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(16, 'get_CallerId', ((1, 'pbstrCallerId'),)))
    IFaxIncomingMessage.get_RoutingInformation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(17, 'get_RoutingInformation', ((1, 'pbstrRoutingInformation'),)))
    IFaxIncomingMessage.CopyTiff = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(18, 'CopyTiff', ((1, 'bstrTiffPath'),)))
    IFaxIncomingMessage.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(19, 'Delete', ()))
    return IFaxIncomingMessage
def _define_IFaxOutgoingJobs_head():
    class IFaxOutgoingJobs(win32more.System.Com.IDispatch_head):
        Guid = Guid('2c56d8e6-8c2f-4573-944c-e505f8f5aeed')
    return IFaxOutgoingJobs
def _define_IFaxOutgoingJobs():
    IFaxOutgoingJobs = win32more.Devices.Fax.IFaxOutgoingJobs_head
    IFaxOutgoingJobs.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(7, 'get__NewEnum', ((1, 'ppUnk'),)))
    IFaxOutgoingJobs.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.Devices.Fax.IFaxOutgoingJob_head), use_last_error=False)(8, 'get_Item', ((1, 'vIndex'),(1, 'pFaxOutgoingJob'),)))
    IFaxOutgoingJobs.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_Count', ((1, 'plCount'),)))
    return IFaxOutgoingJobs
def _define_IFaxOutgoingJob_head():
    class IFaxOutgoingJob(win32more.System.Com.IDispatch_head):
        Guid = Guid('6356daad-6614-4583-bf7a-3ad67bbfc71c')
    return IFaxOutgoingJob
def _define_IFaxOutgoingJob():
    IFaxOutgoingJob = win32more.Devices.Fax.IFaxOutgoingJob_head
    IFaxOutgoingJob.get_Subject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_Subject', ((1, 'pbstrSubject'),)))
    IFaxOutgoingJob.get_DocumentName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'get_DocumentName', ((1, 'pbstrDocumentName'),)))
    IFaxOutgoingJob.get_Pages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_Pages', ((1, 'plPages'),)))
    IFaxOutgoingJob.get_Size = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(10, 'get_Size', ((1, 'plSize'),)))
    IFaxOutgoingJob.get_SubmissionId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'get_SubmissionId', ((1, 'pbstrSubmissionId'),)))
    IFaxOutgoingJob.get_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(12, 'get_Id', ((1, 'pbstrId'),)))
    IFaxOutgoingJob.get_OriginalScheduledTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(13, 'get_OriginalScheduledTime', ((1, 'pdateOriginalScheduledTime'),)))
    IFaxOutgoingJob.get_SubmissionTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(14, 'get_SubmissionTime', ((1, 'pdateSubmissionTime'),)))
    IFaxOutgoingJob.get_ReceiptType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_RECEIPT_TYPE_ENUM), use_last_error=False)(15, 'get_ReceiptType', ((1, 'pReceiptType'),)))
    IFaxOutgoingJob.get_Priority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_PRIORITY_TYPE_ENUM), use_last_error=False)(16, 'get_Priority', ((1, 'pPriority'),)))
    IFaxOutgoingJob.get_Sender = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxSender_head), use_last_error=False)(17, 'get_Sender', ((1, 'ppFaxSender'),)))
    IFaxOutgoingJob.get_Recipient = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxRecipient_head), use_last_error=False)(18, 'get_Recipient', ((1, 'ppFaxRecipient'),)))
    IFaxOutgoingJob.get_CurrentPage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(19, 'get_CurrentPage', ((1, 'plCurrentPage'),)))
    IFaxOutgoingJob.get_DeviceId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(20, 'get_DeviceId', ((1, 'plDeviceId'),)))
    IFaxOutgoingJob.get_Status = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_JOB_STATUS_ENUM), use_last_error=False)(21, 'get_Status', ((1, 'pStatus'),)))
    IFaxOutgoingJob.get_ExtendedStatusCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_JOB_EXTENDED_STATUS_ENUM), use_last_error=False)(22, 'get_ExtendedStatusCode', ((1, 'pExtendedStatusCode'),)))
    IFaxOutgoingJob.get_ExtendedStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(23, 'get_ExtendedStatus', ((1, 'pbstrExtendedStatus'),)))
    IFaxOutgoingJob.get_AvailableOperations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_JOB_OPERATIONS_ENUM), use_last_error=False)(24, 'get_AvailableOperations', ((1, 'pAvailableOperations'),)))
    IFaxOutgoingJob.get_Retries = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(25, 'get_Retries', ((1, 'plRetries'),)))
    IFaxOutgoingJob.get_ScheduledTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(26, 'get_ScheduledTime', ((1, 'pdateScheduledTime'),)))
    IFaxOutgoingJob.get_TransmissionStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(27, 'get_TransmissionStart', ((1, 'pdateTransmissionStart'),)))
    IFaxOutgoingJob.get_TransmissionEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(28, 'get_TransmissionEnd', ((1, 'pdateTransmissionEnd'),)))
    IFaxOutgoingJob.get_CSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(29, 'get_CSID', ((1, 'pbstrCSID'),)))
    IFaxOutgoingJob.get_TSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(30, 'get_TSID', ((1, 'pbstrTSID'),)))
    IFaxOutgoingJob.get_GroupBroadcastReceipts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(31, 'get_GroupBroadcastReceipts', ((1, 'pbGroupBroadcastReceipts'),)))
    IFaxOutgoingJob.Pause = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(32, 'Pause', ()))
    IFaxOutgoingJob.Resume = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(33, 'Resume', ()))
    IFaxOutgoingJob.Restart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(34, 'Restart', ()))
    IFaxOutgoingJob.CopyTiff = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(35, 'CopyTiff', ((1, 'bstrTiffPath'),)))
    IFaxOutgoingJob.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(36, 'Refresh', ()))
    IFaxOutgoingJob.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(37, 'Cancel', ()))
    return IFaxOutgoingJob
def _define_IFaxOutgoingMessageIterator_head():
    class IFaxOutgoingMessageIterator(win32more.System.Com.IDispatch_head):
        Guid = Guid('f5ec5d4f-b840-432f-9980-112fe42a9b7a')
    return IFaxOutgoingMessageIterator
def _define_IFaxOutgoingMessageIterator():
    IFaxOutgoingMessageIterator = win32more.Devices.Fax.IFaxOutgoingMessageIterator_head
    IFaxOutgoingMessageIterator.get_Message = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxOutgoingMessage_head), use_last_error=False)(7, 'get_Message', ((1, 'pFaxOutgoingMessage'),)))
    IFaxOutgoingMessageIterator.get_AtEOF = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(8, 'get_AtEOF', ((1, 'pbEOF'),)))
    IFaxOutgoingMessageIterator.get_PrefetchSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_PrefetchSize', ((1, 'plPrefetchSize'),)))
    IFaxOutgoingMessageIterator.put_PrefetchSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(10, 'put_PrefetchSize', ((1, 'lPrefetchSize'),)))
    IFaxOutgoingMessageIterator.MoveFirst = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(11, 'MoveFirst', ()))
    IFaxOutgoingMessageIterator.MoveNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'MoveNext', ()))
    return IFaxOutgoingMessageIterator
def _define_IFaxOutgoingMessage_head():
    class IFaxOutgoingMessage(win32more.System.Com.IDispatch_head):
        Guid = Guid('f0ea35de-caa5-4a7c-82c7-2b60ba5f2be2')
    return IFaxOutgoingMessage
def _define_IFaxOutgoingMessage():
    IFaxOutgoingMessage = win32more.Devices.Fax.IFaxOutgoingMessage_head
    IFaxOutgoingMessage.get_SubmissionId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_SubmissionId', ((1, 'pbstrSubmissionId'),)))
    IFaxOutgoingMessage.get_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'get_Id', ((1, 'pbstrId'),)))
    IFaxOutgoingMessage.get_Subject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_Subject', ((1, 'pbstrSubject'),)))
    IFaxOutgoingMessage.get_DocumentName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'get_DocumentName', ((1, 'pbstrDocumentName'),)))
    IFaxOutgoingMessage.get_Retries = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(11, 'get_Retries', ((1, 'plRetries'),)))
    IFaxOutgoingMessage.get_Pages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(12, 'get_Pages', ((1, 'plPages'),)))
    IFaxOutgoingMessage.get_Size = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(13, 'get_Size', ((1, 'plSize'),)))
    IFaxOutgoingMessage.get_OriginalScheduledTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(14, 'get_OriginalScheduledTime', ((1, 'pdateOriginalScheduledTime'),)))
    IFaxOutgoingMessage.get_SubmissionTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(15, 'get_SubmissionTime', ((1, 'pdateSubmissionTime'),)))
    IFaxOutgoingMessage.get_Priority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_PRIORITY_TYPE_ENUM), use_last_error=False)(16, 'get_Priority', ((1, 'pPriority'),)))
    IFaxOutgoingMessage.get_Sender = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxSender_head), use_last_error=False)(17, 'get_Sender', ((1, 'ppFaxSender'),)))
    IFaxOutgoingMessage.get_Recipient = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxRecipient_head), use_last_error=False)(18, 'get_Recipient', ((1, 'ppFaxRecipient'),)))
    IFaxOutgoingMessage.get_DeviceName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(19, 'get_DeviceName', ((1, 'pbstrDeviceName'),)))
    IFaxOutgoingMessage.get_TransmissionStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(20, 'get_TransmissionStart', ((1, 'pdateTransmissionStart'),)))
    IFaxOutgoingMessage.get_TransmissionEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(21, 'get_TransmissionEnd', ((1, 'pdateTransmissionEnd'),)))
    IFaxOutgoingMessage.get_CSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(22, 'get_CSID', ((1, 'pbstrCSID'),)))
    IFaxOutgoingMessage.get_TSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(23, 'get_TSID', ((1, 'pbstrTSID'),)))
    IFaxOutgoingMessage.CopyTiff = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(24, 'CopyTiff', ((1, 'bstrTiffPath'),)))
    IFaxOutgoingMessage.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(25, 'Delete', ()))
    return IFaxOutgoingMessage
def _define_IFaxIncomingJobs_head():
    class IFaxIncomingJobs(win32more.System.Com.IDispatch_head):
        Guid = Guid('011f04e9-4fd6-4c23-9513-b6b66bb26be9')
    return IFaxIncomingJobs
def _define_IFaxIncomingJobs():
    IFaxIncomingJobs = win32more.Devices.Fax.IFaxIncomingJobs_head
    IFaxIncomingJobs.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(7, 'get__NewEnum', ((1, 'ppUnk'),)))
    IFaxIncomingJobs.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.Devices.Fax.IFaxIncomingJob_head), use_last_error=False)(8, 'get_Item', ((1, 'vIndex'),(1, 'pFaxIncomingJob'),)))
    IFaxIncomingJobs.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_Count', ((1, 'plCount'),)))
    return IFaxIncomingJobs
def _define_IFaxIncomingJob_head():
    class IFaxIncomingJob(win32more.System.Com.IDispatch_head):
        Guid = Guid('207529e6-654a-4916-9f88-4d232ee8a107')
    return IFaxIncomingJob
def _define_IFaxIncomingJob():
    IFaxIncomingJob = win32more.Devices.Fax.IFaxIncomingJob_head
    IFaxIncomingJob.get_Size = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Size', ((1, 'plSize'),)))
    IFaxIncomingJob.get_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'get_Id', ((1, 'pbstrId'),)))
    IFaxIncomingJob.get_CurrentPage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_CurrentPage', ((1, 'plCurrentPage'),)))
    IFaxIncomingJob.get_DeviceId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(10, 'get_DeviceId', ((1, 'plDeviceId'),)))
    IFaxIncomingJob.get_Status = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_JOB_STATUS_ENUM), use_last_error=False)(11, 'get_Status', ((1, 'pStatus'),)))
    IFaxIncomingJob.get_ExtendedStatusCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_JOB_EXTENDED_STATUS_ENUM), use_last_error=False)(12, 'get_ExtendedStatusCode', ((1, 'pExtendedStatusCode'),)))
    IFaxIncomingJob.get_ExtendedStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(13, 'get_ExtendedStatus', ((1, 'pbstrExtendedStatus'),)))
    IFaxIncomingJob.get_AvailableOperations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_JOB_OPERATIONS_ENUM), use_last_error=False)(14, 'get_AvailableOperations', ((1, 'pAvailableOperations'),)))
    IFaxIncomingJob.get_Retries = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(15, 'get_Retries', ((1, 'plRetries'),)))
    IFaxIncomingJob.get_TransmissionStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(16, 'get_TransmissionStart', ((1, 'pdateTransmissionStart'),)))
    IFaxIncomingJob.get_TransmissionEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(17, 'get_TransmissionEnd', ((1, 'pdateTransmissionEnd'),)))
    IFaxIncomingJob.get_CSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(18, 'get_CSID', ((1, 'pbstrCSID'),)))
    IFaxIncomingJob.get_TSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(19, 'get_TSID', ((1, 'pbstrTSID'),)))
    IFaxIncomingJob.get_CallerId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(20, 'get_CallerId', ((1, 'pbstrCallerId'),)))
    IFaxIncomingJob.get_RoutingInformation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(21, 'get_RoutingInformation', ((1, 'pbstrRoutingInformation'),)))
    IFaxIncomingJob.get_JobType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_JOB_TYPE_ENUM), use_last_error=False)(22, 'get_JobType', ((1, 'pJobType'),)))
    IFaxIncomingJob.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(23, 'Cancel', ()))
    IFaxIncomingJob.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(24, 'Refresh', ()))
    IFaxIncomingJob.CopyTiff = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(25, 'CopyTiff', ((1, 'bstrTiffPath'),)))
    return IFaxIncomingJob
FAX_PROVIDER_STATUS_ENUM = Int32
FAX_PROVIDER_STATUS_ENUM_fpsSUCCESS = 0
FAX_PROVIDER_STATUS_ENUM_fpsSERVER_ERROR = 1
FAX_PROVIDER_STATUS_ENUM_fpsBAD_GUID = 2
FAX_PROVIDER_STATUS_ENUM_fpsBAD_VERSION = 3
FAX_PROVIDER_STATUS_ENUM_fpsCANT_LOAD = 4
FAX_PROVIDER_STATUS_ENUM_fpsCANT_LINK = 5
FAX_PROVIDER_STATUS_ENUM_fpsCANT_INIT = 6
def _define_IFaxDeviceProvider_head():
    class IFaxDeviceProvider(win32more.System.Com.IDispatch_head):
        Guid = Guid('290eac63-83ec-449c-8417-f148df8c682a')
    return IFaxDeviceProvider
def _define_IFaxDeviceProvider():
    IFaxDeviceProvider = win32more.Devices.Fax.IFaxDeviceProvider_head
    IFaxDeviceProvider.get_FriendlyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_FriendlyName', ((1, 'pbstrFriendlyName'),)))
    IFaxDeviceProvider.get_ImageName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'get_ImageName', ((1, 'pbstrImageName'),)))
    IFaxDeviceProvider.get_UniqueName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_UniqueName', ((1, 'pbstrUniqueName'),)))
    IFaxDeviceProvider.get_TapiProviderName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'get_TapiProviderName', ((1, 'pbstrTapiProviderName'),)))
    IFaxDeviceProvider.get_MajorVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(11, 'get_MajorVersion', ((1, 'plMajorVersion'),)))
    IFaxDeviceProvider.get_MinorVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(12, 'get_MinorVersion', ((1, 'plMinorVersion'),)))
    IFaxDeviceProvider.get_MajorBuild = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(13, 'get_MajorBuild', ((1, 'plMajorBuild'),)))
    IFaxDeviceProvider.get_MinorBuild = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(14, 'get_MinorBuild', ((1, 'plMinorBuild'),)))
    IFaxDeviceProvider.get_Debug = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(15, 'get_Debug', ((1, 'pbDebug'),)))
    IFaxDeviceProvider.get_Status = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_PROVIDER_STATUS_ENUM), use_last_error=False)(16, 'get_Status', ((1, 'pStatus'),)))
    IFaxDeviceProvider.get_InitErrorCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(17, 'get_InitErrorCode', ((1, 'plInitErrorCode'),)))
    IFaxDeviceProvider.get_DeviceIds = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(18, 'get_DeviceIds', ((1, 'pvDeviceIds'),)))
    return IFaxDeviceProvider
FAX_DEVICE_RECEIVE_MODE_ENUM = Int32
fdrmNO_ANSWER = 0
fdrmAUTO_ANSWER = 1
fdrmMANUAL_ANSWER = 2
def _define_IFaxDevice_head():
    class IFaxDevice(win32more.System.Com.IDispatch_head):
        Guid = Guid('49306c59-b52e-4867-9df4-ca5841c956d0')
    return IFaxDevice
def _define_IFaxDevice():
    IFaxDevice = win32more.Devices.Fax.IFaxDevice_head
    IFaxDevice.get_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Id', ((1, 'plId'),)))
    IFaxDevice.get_DeviceName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'get_DeviceName', ((1, 'pbstrDeviceName'),)))
    IFaxDevice.get_ProviderUniqueName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_ProviderUniqueName', ((1, 'pbstrProviderUniqueName'),)))
    IFaxDevice.get_PoweredOff = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(10, 'get_PoweredOff', ((1, 'pbPoweredOff'),)))
    IFaxDevice.get_ReceivingNow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(11, 'get_ReceivingNow', ((1, 'pbReceivingNow'),)))
    IFaxDevice.get_SendingNow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(12, 'get_SendingNow', ((1, 'pbSendingNow'),)))
    IFaxDevice.get_UsedRoutingMethods = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(13, 'get_UsedRoutingMethods', ((1, 'pvUsedRoutingMethods'),)))
    IFaxDevice.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(14, 'get_Description', ((1, 'pbstrDescription'),)))
    IFaxDevice.put_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(15, 'put_Description', ((1, 'bstrDescription'),)))
    IFaxDevice.get_SendEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(16, 'get_SendEnabled', ((1, 'pbSendEnabled'),)))
    IFaxDevice.put_SendEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(17, 'put_SendEnabled', ((1, 'bSendEnabled'),)))
    IFaxDevice.get_ReceiveMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_DEVICE_RECEIVE_MODE_ENUM), use_last_error=False)(18, 'get_ReceiveMode', ((1, 'pReceiveMode'),)))
    IFaxDevice.put_ReceiveMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.FAX_DEVICE_RECEIVE_MODE_ENUM, use_last_error=False)(19, 'put_ReceiveMode', ((1, 'ReceiveMode'),)))
    IFaxDevice.get_RingsBeforeAnswer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(20, 'get_RingsBeforeAnswer', ((1, 'plRingsBeforeAnswer'),)))
    IFaxDevice.put_RingsBeforeAnswer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(21, 'put_RingsBeforeAnswer', ((1, 'lRingsBeforeAnswer'),)))
    IFaxDevice.get_CSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(22, 'get_CSID', ((1, 'pbstrCSID'),)))
    IFaxDevice.put_CSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(23, 'put_CSID', ((1, 'bstrCSID'),)))
    IFaxDevice.get_TSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(24, 'get_TSID', ((1, 'pbstrTSID'),)))
    IFaxDevice.put_TSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(25, 'put_TSID', ((1, 'bstrTSID'),)))
    IFaxDevice.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(26, 'Refresh', ()))
    IFaxDevice.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(27, 'Save', ()))
    IFaxDevice.GetExtensionProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(28, 'GetExtensionProperty', ((1, 'bstrGUID'),(1, 'pvProperty'),)))
    IFaxDevice.SetExtensionProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(29, 'SetExtensionProperty', ((1, 'bstrGUID'),(1, 'vProperty'),)))
    IFaxDevice.UseRoutingMethod = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int16, use_last_error=False)(30, 'UseRoutingMethod', ((1, 'bstrMethodGUID'),(1, 'bUse'),)))
    IFaxDevice.get_RingingNow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(31, 'get_RingingNow', ((1, 'pbRingingNow'),)))
    IFaxDevice.AnswerCall = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(32, 'AnswerCall', ()))
    return IFaxDevice
def _define_IFaxActivityLogging_head():
    class IFaxActivityLogging(win32more.System.Com.IDispatch_head):
        Guid = Guid('1e29078b-5a69-497b-9592-49b7e7faddb5')
    return IFaxActivityLogging
def _define_IFaxActivityLogging():
    IFaxActivityLogging = win32more.Devices.Fax.IFaxActivityLogging_head
    IFaxActivityLogging.get_LogIncoming = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(7, 'get_LogIncoming', ((1, 'pbLogIncoming'),)))
    IFaxActivityLogging.put_LogIncoming = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(8, 'put_LogIncoming', ((1, 'bLogIncoming'),)))
    IFaxActivityLogging.get_LogOutgoing = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(9, 'get_LogOutgoing', ((1, 'pbLogOutgoing'),)))
    IFaxActivityLogging.put_LogOutgoing = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(10, 'put_LogOutgoing', ((1, 'bLogOutgoing'),)))
    IFaxActivityLogging.get_DatabasePath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'get_DatabasePath', ((1, 'pbstrDatabasePath'),)))
    IFaxActivityLogging.put_DatabasePath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(12, 'put_DatabasePath', ((1, 'bstrDatabasePath'),)))
    IFaxActivityLogging.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(13, 'Refresh', ()))
    IFaxActivityLogging.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(14, 'Save', ()))
    return IFaxActivityLogging
FAX_LOG_LEVEL_ENUM = Int32
FAX_LOG_LEVEL_ENUM_fllNONE = 0
FAX_LOG_LEVEL_ENUM_fllMIN = 1
FAX_LOG_LEVEL_ENUM_fllMED = 2
FAX_LOG_LEVEL_ENUM_fllMAX = 3
def _define_IFaxEventLogging_head():
    class IFaxEventLogging(win32more.System.Com.IDispatch_head):
        Guid = Guid('0880d965-20e8-42e4-8e17-944f192caad4')
    return IFaxEventLogging
def _define_IFaxEventLogging():
    IFaxEventLogging = win32more.Devices.Fax.IFaxEventLogging_head
    IFaxEventLogging.get_InitEventsLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_LOG_LEVEL_ENUM), use_last_error=False)(7, 'get_InitEventsLevel', ((1, 'pInitEventLevel'),)))
    IFaxEventLogging.put_InitEventsLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.FAX_LOG_LEVEL_ENUM, use_last_error=False)(8, 'put_InitEventsLevel', ((1, 'InitEventLevel'),)))
    IFaxEventLogging.get_InboundEventsLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_LOG_LEVEL_ENUM), use_last_error=False)(9, 'get_InboundEventsLevel', ((1, 'pInboundEventLevel'),)))
    IFaxEventLogging.put_InboundEventsLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.FAX_LOG_LEVEL_ENUM, use_last_error=False)(10, 'put_InboundEventsLevel', ((1, 'InboundEventLevel'),)))
    IFaxEventLogging.get_OutboundEventsLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_LOG_LEVEL_ENUM), use_last_error=False)(11, 'get_OutboundEventsLevel', ((1, 'pOutboundEventLevel'),)))
    IFaxEventLogging.put_OutboundEventsLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.FAX_LOG_LEVEL_ENUM, use_last_error=False)(12, 'put_OutboundEventsLevel', ((1, 'OutboundEventLevel'),)))
    IFaxEventLogging.get_GeneralEventsLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_LOG_LEVEL_ENUM), use_last_error=False)(13, 'get_GeneralEventsLevel', ((1, 'pGeneralEventLevel'),)))
    IFaxEventLogging.put_GeneralEventsLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.FAX_LOG_LEVEL_ENUM, use_last_error=False)(14, 'put_GeneralEventsLevel', ((1, 'GeneralEventLevel'),)))
    IFaxEventLogging.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(15, 'Refresh', ()))
    IFaxEventLogging.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(16, 'Save', ()))
    return IFaxEventLogging
def _define_IFaxOutboundRoutingGroups_head():
    class IFaxOutboundRoutingGroups(win32more.System.Com.IDispatch_head):
        Guid = Guid('235cbef7-c2de-4bfd-b8da-75097c82c87f')
    return IFaxOutboundRoutingGroups
def _define_IFaxOutboundRoutingGroups():
    IFaxOutboundRoutingGroups = win32more.Devices.Fax.IFaxOutboundRoutingGroups_head
    IFaxOutboundRoutingGroups.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(7, 'get__NewEnum', ((1, 'ppUnk'),)))
    IFaxOutboundRoutingGroups.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.Devices.Fax.IFaxOutboundRoutingGroup_head), use_last_error=False)(8, 'get_Item', ((1, 'vIndex'),(1, 'pFaxOutboundRoutingGroup'),)))
    IFaxOutboundRoutingGroups.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_Count', ((1, 'plCount'),)))
    IFaxOutboundRoutingGroups.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Devices.Fax.IFaxOutboundRoutingGroup_head), use_last_error=False)(10, 'Add', ((1, 'bstrName'),(1, 'pFaxOutboundRoutingGroup'),)))
    IFaxOutboundRoutingGroups.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(11, 'Remove', ((1, 'vIndex'),)))
    return IFaxOutboundRoutingGroups
FAX_GROUP_STATUS_ENUM = Int32
FAX_GROUP_STATUS_ENUM_fgsALL_DEV_VALID = 0
FAX_GROUP_STATUS_ENUM_fgsEMPTY = 1
FAX_GROUP_STATUS_ENUM_fgsALL_DEV_NOT_VALID = 2
FAX_GROUP_STATUS_ENUM_fgsSOME_DEV_NOT_VALID = 3
def _define_IFaxOutboundRoutingGroup_head():
    class IFaxOutboundRoutingGroup(win32more.System.Com.IDispatch_head):
        Guid = Guid('ca6289a1-7e25-4f87-9a0b-93365734962c')
    return IFaxOutboundRoutingGroup
def _define_IFaxOutboundRoutingGroup():
    IFaxOutboundRoutingGroup = win32more.Devices.Fax.IFaxOutboundRoutingGroup_head
    IFaxOutboundRoutingGroup.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_Name', ((1, 'pbstrName'),)))
    IFaxOutboundRoutingGroup.get_Status = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_GROUP_STATUS_ENUM), use_last_error=False)(8, 'get_Status', ((1, 'pStatus'),)))
    IFaxOutboundRoutingGroup.get_DeviceIds = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxDeviceIds_head), use_last_error=False)(9, 'get_DeviceIds', ((1, 'pFaxDeviceIds'),)))
    return IFaxOutboundRoutingGroup
def _define_IFaxDeviceIds_head():
    class IFaxDeviceIds(win32more.System.Com.IDispatch_head):
        Guid = Guid('2f0f813f-4ce9-443e-8ca1-738cfaeee149')
    return IFaxDeviceIds
def _define_IFaxDeviceIds():
    IFaxDeviceIds = win32more.Devices.Fax.IFaxDeviceIds_head
    IFaxDeviceIds.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(7, 'get__NewEnum', ((1, 'ppUnk'),)))
    IFaxDeviceIds.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Int32), use_last_error=False)(8, 'get_Item', ((1, 'lIndex'),(1, 'plDeviceId'),)))
    IFaxDeviceIds.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_Count', ((1, 'plCount'),)))
    IFaxDeviceIds.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(10, 'Add', ((1, 'lDeviceId'),)))
    IFaxDeviceIds.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(11, 'Remove', ((1, 'lIndex'),)))
    IFaxDeviceIds.SetOrder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32, use_last_error=False)(12, 'SetOrder', ((1, 'lDeviceId'),(1, 'lNewOrder'),)))
    return IFaxDeviceIds
def _define_IFaxOutboundRoutingRules_head():
    class IFaxOutboundRoutingRules(win32more.System.Com.IDispatch_head):
        Guid = Guid('dcefa1e7-ae7d-4ed6-8521-369edcca5120')
    return IFaxOutboundRoutingRules
def _define_IFaxOutboundRoutingRules():
    IFaxOutboundRoutingRules = win32more.Devices.Fax.IFaxOutboundRoutingRules_head
    IFaxOutboundRoutingRules.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(7, 'get__NewEnum', ((1, 'ppUnk'),)))
    IFaxOutboundRoutingRules.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Devices.Fax.IFaxOutboundRoutingRule_head), use_last_error=False)(8, 'get_Item', ((1, 'lIndex'),(1, 'pFaxOutboundRoutingRule'),)))
    IFaxOutboundRoutingRules.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_Count', ((1, 'plCount'),)))
    IFaxOutboundRoutingRules.ItemByCountryAndArea = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(win32more.Devices.Fax.IFaxOutboundRoutingRule_head), use_last_error=False)(10, 'ItemByCountryAndArea', ((1, 'lCountryCode'),(1, 'lAreaCode'),(1, 'pFaxOutboundRoutingRule'),)))
    IFaxOutboundRoutingRules.RemoveByCountryAndArea = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32, use_last_error=False)(11, 'RemoveByCountryAndArea', ((1, 'lCountryCode'),(1, 'lAreaCode'),)))
    IFaxOutboundRoutingRules.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(12, 'Remove', ((1, 'lIndex'),)))
    IFaxOutboundRoutingRules.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,Int16,win32more.Foundation.BSTR,Int32,POINTER(win32more.Devices.Fax.IFaxOutboundRoutingRule_head), use_last_error=False)(13, 'Add', ((1, 'lCountryCode'),(1, 'lAreaCode'),(1, 'bUseDevice'),(1, 'bstrGroupName'),(1, 'lDeviceId'),(1, 'pFaxOutboundRoutingRule'),)))
    return IFaxOutboundRoutingRules
FAX_RULE_STATUS_ENUM = Int32
FAX_RULE_STATUS_ENUM_frsVALID = 0
FAX_RULE_STATUS_ENUM_frsEMPTY_GROUP = 1
FAX_RULE_STATUS_ENUM_frsALL_GROUP_DEV_NOT_VALID = 2
FAX_RULE_STATUS_ENUM_frsSOME_GROUP_DEV_NOT_VALID = 3
FAX_RULE_STATUS_ENUM_frsBAD_DEVICE = 4
def _define_IFaxOutboundRoutingRule_head():
    class IFaxOutboundRoutingRule(win32more.System.Com.IDispatch_head):
        Guid = Guid('e1f795d5-07c2-469f-b027-acacc23219da')
    return IFaxOutboundRoutingRule
def _define_IFaxOutboundRoutingRule():
    IFaxOutboundRoutingRule = win32more.Devices.Fax.IFaxOutboundRoutingRule_head
    IFaxOutboundRoutingRule.get_CountryCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_CountryCode', ((1, 'plCountryCode'),)))
    IFaxOutboundRoutingRule.get_AreaCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_AreaCode', ((1, 'plAreaCode'),)))
    IFaxOutboundRoutingRule.get_Status = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_RULE_STATUS_ENUM), use_last_error=False)(9, 'get_Status', ((1, 'pStatus'),)))
    IFaxOutboundRoutingRule.get_UseDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(10, 'get_UseDevice', ((1, 'pbUseDevice'),)))
    IFaxOutboundRoutingRule.put_UseDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(11, 'put_UseDevice', ((1, 'bUseDevice'),)))
    IFaxOutboundRoutingRule.get_DeviceId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(12, 'get_DeviceId', ((1, 'plDeviceId'),)))
    IFaxOutboundRoutingRule.put_DeviceId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(13, 'put_DeviceId', ((1, 'DeviceId'),)))
    IFaxOutboundRoutingRule.get_GroupName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(14, 'get_GroupName', ((1, 'pbstrGroupName'),)))
    IFaxOutboundRoutingRule.put_GroupName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(15, 'put_GroupName', ((1, 'bstrGroupName'),)))
    IFaxOutboundRoutingRule.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(16, 'Refresh', ()))
    IFaxOutboundRoutingRule.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(17, 'Save', ()))
    return IFaxOutboundRoutingRule
def _define_IFaxInboundRoutingExtensions_head():
    class IFaxInboundRoutingExtensions(win32more.System.Com.IDispatch_head):
        Guid = Guid('2f6c9673-7b26-42de-8eb0-915dcd2a4f4c')
    return IFaxInboundRoutingExtensions
def _define_IFaxInboundRoutingExtensions():
    IFaxInboundRoutingExtensions = win32more.Devices.Fax.IFaxInboundRoutingExtensions_head
    IFaxInboundRoutingExtensions.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(7, 'get__NewEnum', ((1, 'ppUnk'),)))
    IFaxInboundRoutingExtensions.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.Devices.Fax.IFaxInboundRoutingExtension_head), use_last_error=False)(8, 'get_Item', ((1, 'vIndex'),(1, 'pFaxInboundRoutingExtension'),)))
    IFaxInboundRoutingExtensions.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_Count', ((1, 'plCount'),)))
    return IFaxInboundRoutingExtensions
def _define_IFaxInboundRoutingExtension_head():
    class IFaxInboundRoutingExtension(win32more.System.Com.IDispatch_head):
        Guid = Guid('885b5e08-c26c-4ef9-af83-51580a750be1')
    return IFaxInboundRoutingExtension
def _define_IFaxInboundRoutingExtension():
    IFaxInboundRoutingExtension = win32more.Devices.Fax.IFaxInboundRoutingExtension_head
    IFaxInboundRoutingExtension.get_FriendlyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_FriendlyName', ((1, 'pbstrFriendlyName'),)))
    IFaxInboundRoutingExtension.get_ImageName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'get_ImageName', ((1, 'pbstrImageName'),)))
    IFaxInboundRoutingExtension.get_UniqueName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_UniqueName', ((1, 'pbstrUniqueName'),)))
    IFaxInboundRoutingExtension.get_MajorVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(10, 'get_MajorVersion', ((1, 'plMajorVersion'),)))
    IFaxInboundRoutingExtension.get_MinorVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(11, 'get_MinorVersion', ((1, 'plMinorVersion'),)))
    IFaxInboundRoutingExtension.get_MajorBuild = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(12, 'get_MajorBuild', ((1, 'plMajorBuild'),)))
    IFaxInboundRoutingExtension.get_MinorBuild = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(13, 'get_MinorBuild', ((1, 'plMinorBuild'),)))
    IFaxInboundRoutingExtension.get_Debug = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(14, 'get_Debug', ((1, 'pbDebug'),)))
    IFaxInboundRoutingExtension.get_Status = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_PROVIDER_STATUS_ENUM), use_last_error=False)(15, 'get_Status', ((1, 'pStatus'),)))
    IFaxInboundRoutingExtension.get_InitErrorCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(16, 'get_InitErrorCode', ((1, 'plInitErrorCode'),)))
    IFaxInboundRoutingExtension.get_Methods = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(17, 'get_Methods', ((1, 'pvMethods'),)))
    return IFaxInboundRoutingExtension
def _define_IFaxInboundRoutingMethods_head():
    class IFaxInboundRoutingMethods(win32more.System.Com.IDispatch_head):
        Guid = Guid('783fca10-8908-4473-9d69-f67fbea0c6b9')
    return IFaxInboundRoutingMethods
def _define_IFaxInboundRoutingMethods():
    IFaxInboundRoutingMethods = win32more.Devices.Fax.IFaxInboundRoutingMethods_head
    IFaxInboundRoutingMethods.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(7, 'get__NewEnum', ((1, 'ppUnk'),)))
    IFaxInboundRoutingMethods.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.Devices.Fax.IFaxInboundRoutingMethod_head), use_last_error=False)(8, 'get_Item', ((1, 'vIndex'),(1, 'pFaxInboundRoutingMethod'),)))
    IFaxInboundRoutingMethods.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_Count', ((1, 'plCount'),)))
    return IFaxInboundRoutingMethods
def _define_IFaxInboundRoutingMethod_head():
    class IFaxInboundRoutingMethod(win32more.System.Com.IDispatch_head):
        Guid = Guid('45700061-ad9d-4776-a8c4-64065492cf4b')
    return IFaxInboundRoutingMethod
def _define_IFaxInboundRoutingMethod():
    IFaxInboundRoutingMethod = win32more.Devices.Fax.IFaxInboundRoutingMethod_head
    IFaxInboundRoutingMethod.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_Name', ((1, 'pbstrName'),)))
    IFaxInboundRoutingMethod.get_GUID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'get_GUID', ((1, 'pbstrGUID'),)))
    IFaxInboundRoutingMethod.get_FunctionName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_FunctionName', ((1, 'pbstrFunctionName'),)))
    IFaxInboundRoutingMethod.get_ExtensionFriendlyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'get_ExtensionFriendlyName', ((1, 'pbstrExtensionFriendlyName'),)))
    IFaxInboundRoutingMethod.get_ExtensionImageName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'get_ExtensionImageName', ((1, 'pbstrExtensionImageName'),)))
    IFaxInboundRoutingMethod.get_Priority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(12, 'get_Priority', ((1, 'plPriority'),)))
    IFaxInboundRoutingMethod.put_Priority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(13, 'put_Priority', ((1, 'lPriority'),)))
    IFaxInboundRoutingMethod.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(14, 'Refresh', ()))
    IFaxInboundRoutingMethod.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(15, 'Save', ()))
    return IFaxInboundRoutingMethod
def _define_IFaxDocument2_head():
    class IFaxDocument2(win32more.Devices.Fax.IFaxDocument_head):
        Guid = Guid('e1347661-f9ef-4d6d-b4a5-c0a068b65cff')
    return IFaxDocument2
def _define_IFaxDocument2():
    IFaxDocument2 = win32more.Devices.Fax.IFaxDocument2_head
    IFaxDocument2.get_SubmissionId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(41, 'get_SubmissionId', ((1, 'pbstrSubmissionId'),)))
    IFaxDocument2.get_Bodies = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(42, 'get_Bodies', ((1, 'pvBodies'),)))
    IFaxDocument2.put_Bodies = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(43, 'put_Bodies', ((1, 'vBodies'),)))
    IFaxDocument2.Submit2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head),POINTER(Int32), use_last_error=False)(44, 'Submit2', ((1, 'bstrFaxServerName'),(1, 'pvFaxOutgoingJobIDs'),(1, 'plErrorBodyFile'),)))
    IFaxDocument2.ConnectedSubmit2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer_head,POINTER(win32more.System.Com.VARIANT_head),POINTER(Int32), use_last_error=False)(45, 'ConnectedSubmit2', ((1, 'pFaxServer'),(1, 'pvFaxOutgoingJobIDs'),(1, 'plErrorBodyFile'),)))
    return IFaxDocument2
def _define_IFaxConfiguration_head():
    class IFaxConfiguration(win32more.System.Com.IDispatch_head):
        Guid = Guid('10f4d0f7-0994-4543-ab6e-506949128c40')
    return IFaxConfiguration
def _define_IFaxConfiguration():
    IFaxConfiguration = win32more.Devices.Fax.IFaxConfiguration_head
    IFaxConfiguration.get_UseArchive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(7, 'get_UseArchive', ((1, 'pbUseArchive'),)))
    IFaxConfiguration.put_UseArchive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(8, 'put_UseArchive', ((1, 'bUseArchive'),)))
    IFaxConfiguration.get_ArchiveLocation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_ArchiveLocation', ((1, 'pbstrArchiveLocation'),)))
    IFaxConfiguration.put_ArchiveLocation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(10, 'put_ArchiveLocation', ((1, 'bstrArchiveLocation'),)))
    IFaxConfiguration.get_SizeQuotaWarning = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(11, 'get_SizeQuotaWarning', ((1, 'pbSizeQuotaWarning'),)))
    IFaxConfiguration.put_SizeQuotaWarning = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(12, 'put_SizeQuotaWarning', ((1, 'bSizeQuotaWarning'),)))
    IFaxConfiguration.get_HighQuotaWaterMark = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(13, 'get_HighQuotaWaterMark', ((1, 'plHighQuotaWaterMark'),)))
    IFaxConfiguration.put_HighQuotaWaterMark = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(14, 'put_HighQuotaWaterMark', ((1, 'lHighQuotaWaterMark'),)))
    IFaxConfiguration.get_LowQuotaWaterMark = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(15, 'get_LowQuotaWaterMark', ((1, 'plLowQuotaWaterMark'),)))
    IFaxConfiguration.put_LowQuotaWaterMark = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(16, 'put_LowQuotaWaterMark', ((1, 'lLowQuotaWaterMark'),)))
    IFaxConfiguration.get_ArchiveAgeLimit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(17, 'get_ArchiveAgeLimit', ((1, 'plArchiveAgeLimit'),)))
    IFaxConfiguration.put_ArchiveAgeLimit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(18, 'put_ArchiveAgeLimit', ((1, 'lArchiveAgeLimit'),)))
    IFaxConfiguration.get_ArchiveSizeLow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(19, 'get_ArchiveSizeLow', ((1, 'plSizeLow'),)))
    IFaxConfiguration.get_ArchiveSizeHigh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(20, 'get_ArchiveSizeHigh', ((1, 'plSizeHigh'),)))
    IFaxConfiguration.get_OutgoingQueueBlocked = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(21, 'get_OutgoingQueueBlocked', ((1, 'pbOutgoingBlocked'),)))
    IFaxConfiguration.put_OutgoingQueueBlocked = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(22, 'put_OutgoingQueueBlocked', ((1, 'bOutgoingBlocked'),)))
    IFaxConfiguration.get_OutgoingQueuePaused = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(23, 'get_OutgoingQueuePaused', ((1, 'pbOutgoingPaused'),)))
    IFaxConfiguration.put_OutgoingQueuePaused = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(24, 'put_OutgoingQueuePaused', ((1, 'bOutgoingPaused'),)))
    IFaxConfiguration.get_AllowPersonalCoverPages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(25, 'get_AllowPersonalCoverPages', ((1, 'pbAllowPersonalCoverPages'),)))
    IFaxConfiguration.put_AllowPersonalCoverPages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(26, 'put_AllowPersonalCoverPages', ((1, 'bAllowPersonalCoverPages'),)))
    IFaxConfiguration.get_UseDeviceTSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(27, 'get_UseDeviceTSID', ((1, 'pbUseDeviceTSID'),)))
    IFaxConfiguration.put_UseDeviceTSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(28, 'put_UseDeviceTSID', ((1, 'bUseDeviceTSID'),)))
    IFaxConfiguration.get_Retries = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(29, 'get_Retries', ((1, 'plRetries'),)))
    IFaxConfiguration.put_Retries = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(30, 'put_Retries', ((1, 'lRetries'),)))
    IFaxConfiguration.get_RetryDelay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(31, 'get_RetryDelay', ((1, 'plRetryDelay'),)))
    IFaxConfiguration.put_RetryDelay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(32, 'put_RetryDelay', ((1, 'lRetryDelay'),)))
    IFaxConfiguration.get_DiscountRateStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(33, 'get_DiscountRateStart', ((1, 'pdateDiscountRateStart'),)))
    IFaxConfiguration.put_DiscountRateStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(34, 'put_DiscountRateStart', ((1, 'dateDiscountRateStart'),)))
    IFaxConfiguration.get_DiscountRateEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(35, 'get_DiscountRateEnd', ((1, 'pdateDiscountRateEnd'),)))
    IFaxConfiguration.put_DiscountRateEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(36, 'put_DiscountRateEnd', ((1, 'dateDiscountRateEnd'),)))
    IFaxConfiguration.get_OutgoingQueueAgeLimit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(37, 'get_OutgoingQueueAgeLimit', ((1, 'plOutgoingQueueAgeLimit'),)))
    IFaxConfiguration.put_OutgoingQueueAgeLimit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(38, 'put_OutgoingQueueAgeLimit', ((1, 'lOutgoingQueueAgeLimit'),)))
    IFaxConfiguration.get_Branding = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(39, 'get_Branding', ((1, 'pbBranding'),)))
    IFaxConfiguration.put_Branding = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(40, 'put_Branding', ((1, 'bBranding'),)))
    IFaxConfiguration.get_IncomingQueueBlocked = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(41, 'get_IncomingQueueBlocked', ((1, 'pbIncomingBlocked'),)))
    IFaxConfiguration.put_IncomingQueueBlocked = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(42, 'put_IncomingQueueBlocked', ((1, 'bIncomingBlocked'),)))
    IFaxConfiguration.get_AutoCreateAccountOnConnect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(43, 'get_AutoCreateAccountOnConnect', ((1, 'pbAutoCreateAccountOnConnect'),)))
    IFaxConfiguration.put_AutoCreateAccountOnConnect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(44, 'put_AutoCreateAccountOnConnect', ((1, 'bAutoCreateAccountOnConnect'),)))
    IFaxConfiguration.get_IncomingFaxesArePublic = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(45, 'get_IncomingFaxesArePublic', ((1, 'pbIncomingFaxesArePublic'),)))
    IFaxConfiguration.put_IncomingFaxesArePublic = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(46, 'put_IncomingFaxesArePublic', ((1, 'bIncomingFaxesArePublic'),)))
    IFaxConfiguration.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(47, 'Refresh', ()))
    IFaxConfiguration.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(48, 'Save', ()))
    return IFaxConfiguration
def _define_IFaxServer2_head():
    class IFaxServer2(win32more.Devices.Fax.IFaxServer_head):
        Guid = Guid('571ced0f-5609-4f40-9176-547e3a72ca7c')
    return IFaxServer2
def _define_IFaxServer2():
    IFaxServer2 = win32more.Devices.Fax.IFaxServer2_head
    IFaxServer2.get_Configuration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxConfiguration_head), use_last_error=False)(33, 'get_Configuration', ((1, 'ppFaxConfiguration'),)))
    IFaxServer2.get_CurrentAccount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxAccount_head), use_last_error=False)(34, 'get_CurrentAccount', ((1, 'ppCurrentAccount'),)))
    IFaxServer2.get_FaxAccountSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxAccountSet_head), use_last_error=False)(35, 'get_FaxAccountSet', ((1, 'ppFaxAccountSet'),)))
    IFaxServer2.get_Security2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxSecurity2_head), use_last_error=False)(36, 'get_Security2', ((1, 'ppFaxSecurity2'),)))
    return IFaxServer2
def _define_IFaxAccountSet_head():
    class IFaxAccountSet(win32more.System.Com.IDispatch_head):
        Guid = Guid('7428fbae-841e-47b8-86f4-2288946dca1b')
    return IFaxAccountSet
def _define_IFaxAccountSet():
    IFaxAccountSet = win32more.Devices.Fax.IFaxAccountSet_head
    IFaxAccountSet.GetAccounts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxAccounts_head), use_last_error=False)(7, 'GetAccounts', ((1, 'ppFaxAccounts'),)))
    IFaxAccountSet.GetAccount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Devices.Fax.IFaxAccount_head), use_last_error=False)(8, 'GetAccount', ((1, 'bstrAccountName'),(1, 'pFaxAccount'),)))
    IFaxAccountSet.AddAccount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Devices.Fax.IFaxAccount_head), use_last_error=False)(9, 'AddAccount', ((1, 'bstrAccountName'),(1, 'pFaxAccount'),)))
    IFaxAccountSet.RemoveAccount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(10, 'RemoveAccount', ((1, 'bstrAccountName'),)))
    return IFaxAccountSet
def _define_IFaxAccounts_head():
    class IFaxAccounts(win32more.System.Com.IDispatch_head):
        Guid = Guid('93ea8162-8be7-42d1-ae7b-ec74e2d989da')
    return IFaxAccounts
def _define_IFaxAccounts():
    IFaxAccounts = win32more.Devices.Fax.IFaxAccounts_head
    IFaxAccounts.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(7, 'get__NewEnum', ((1, 'ppUnk'),)))
    IFaxAccounts.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.Devices.Fax.IFaxAccount_head), use_last_error=False)(8, 'get_Item', ((1, 'vIndex'),(1, 'pFaxAccount'),)))
    IFaxAccounts.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_Count', ((1, 'plCount'),)))
    return IFaxAccounts
FAX_ACCOUNT_EVENTS_TYPE_ENUM = Int32
FAX_ACCOUNT_EVENTS_TYPE_ENUM_faetNONE = 0
FAX_ACCOUNT_EVENTS_TYPE_ENUM_faetIN_QUEUE = 1
FAX_ACCOUNT_EVENTS_TYPE_ENUM_faetOUT_QUEUE = 2
FAX_ACCOUNT_EVENTS_TYPE_ENUM_faetIN_ARCHIVE = 4
FAX_ACCOUNT_EVENTS_TYPE_ENUM_faetOUT_ARCHIVE = 8
FAX_ACCOUNT_EVENTS_TYPE_ENUM_faetFXSSVC_ENDED = 16
def _define_IFaxAccount_head():
    class IFaxAccount(win32more.System.Com.IDispatch_head):
        Guid = Guid('68535b33-5dc4-4086-be26-b76f9b711006')
    return IFaxAccount
def _define_IFaxAccount():
    IFaxAccount = win32more.Devices.Fax.IFaxAccount_head
    IFaxAccount.get_AccountName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_AccountName', ((1, 'pbstrAccountName'),)))
    IFaxAccount.get_Folders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxAccountFolders_head), use_last_error=False)(8, 'get_Folders', ((1, 'ppFolders'),)))
    IFaxAccount.ListenToAccountEvents = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.FAX_ACCOUNT_EVENTS_TYPE_ENUM, use_last_error=False)(9, 'ListenToAccountEvents', ((1, 'EventTypes'),)))
    IFaxAccount.get_RegisteredEvents = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_ACCOUNT_EVENTS_TYPE_ENUM), use_last_error=False)(10, 'get_RegisteredEvents', ((1, 'pRegisteredEvents'),)))
    return IFaxAccount
def _define_IFaxOutgoingJob2_head():
    class IFaxOutgoingJob2(win32more.Devices.Fax.IFaxOutgoingJob_head):
        Guid = Guid('418a8d96-59a0-4789-b176-edf3dc8fa8f7')
    return IFaxOutgoingJob2
def _define_IFaxOutgoingJob2():
    IFaxOutgoingJob2 = win32more.Devices.Fax.IFaxOutgoingJob2_head
    IFaxOutgoingJob2.get_HasCoverPage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(38, 'get_HasCoverPage', ((1, 'pbHasCoverPage'),)))
    IFaxOutgoingJob2.get_ReceiptAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(39, 'get_ReceiptAddress', ((1, 'pbstrReceiptAddress'),)))
    IFaxOutgoingJob2.get_ScheduleType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_SCHEDULE_TYPE_ENUM), use_last_error=False)(40, 'get_ScheduleType', ((1, 'pScheduleType'),)))
    return IFaxOutgoingJob2
def _define_IFaxAccountFolders_head():
    class IFaxAccountFolders(win32more.System.Com.IDispatch_head):
        Guid = Guid('6463f89d-23d8-46a9-8f86-c47b77ca7926')
    return IFaxAccountFolders
def _define_IFaxAccountFolders():
    IFaxAccountFolders = win32more.Devices.Fax.IFaxAccountFolders_head
    IFaxAccountFolders.get_OutgoingQueue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxAccountOutgoingQueue_head), use_last_error=False)(7, 'get_OutgoingQueue', ((1, 'pFaxOutgoingQueue'),)))
    IFaxAccountFolders.get_IncomingQueue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxAccountIncomingQueue_head), use_last_error=False)(8, 'get_IncomingQueue', ((1, 'pFaxIncomingQueue'),)))
    IFaxAccountFolders.get_IncomingArchive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxAccountIncomingArchive_head), use_last_error=False)(9, 'get_IncomingArchive', ((1, 'pFaxIncomingArchive'),)))
    IFaxAccountFolders.get_OutgoingArchive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxAccountOutgoingArchive_head), use_last_error=False)(10, 'get_OutgoingArchive', ((1, 'pFaxOutgoingArchive'),)))
    return IFaxAccountFolders
def _define_IFaxAccountIncomingQueue_head():
    class IFaxAccountIncomingQueue(win32more.System.Com.IDispatch_head):
        Guid = Guid('dd142d92-0186-4a95-a090-cbc3eadba6b4')
    return IFaxAccountIncomingQueue
def _define_IFaxAccountIncomingQueue():
    IFaxAccountIncomingQueue = win32more.Devices.Fax.IFaxAccountIncomingQueue_head
    IFaxAccountIncomingQueue.GetJobs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxIncomingJobs_head), use_last_error=False)(7, 'GetJobs', ((1, 'pFaxIncomingJobs'),)))
    IFaxAccountIncomingQueue.GetJob = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Devices.Fax.IFaxIncomingJob_head), use_last_error=False)(8, 'GetJob', ((1, 'bstrJobId'),(1, 'pFaxIncomingJob'),)))
    return IFaxAccountIncomingQueue
def _define_IFaxAccountOutgoingQueue_head():
    class IFaxAccountOutgoingQueue(win32more.System.Com.IDispatch_head):
        Guid = Guid('0f1424e9-f22d-4553-b7a5-0d24bd0d7e46')
    return IFaxAccountOutgoingQueue
def _define_IFaxAccountOutgoingQueue():
    IFaxAccountOutgoingQueue = win32more.Devices.Fax.IFaxAccountOutgoingQueue_head
    IFaxAccountOutgoingQueue.GetJobs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxOutgoingJobs_head), use_last_error=False)(7, 'GetJobs', ((1, 'pFaxOutgoingJobs'),)))
    IFaxAccountOutgoingQueue.GetJob = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Devices.Fax.IFaxOutgoingJob_head), use_last_error=False)(8, 'GetJob', ((1, 'bstrJobId'),(1, 'pFaxOutgoingJob'),)))
    return IFaxAccountOutgoingQueue
def _define_IFaxOutgoingMessage2_head():
    class IFaxOutgoingMessage2(win32more.Devices.Fax.IFaxOutgoingMessage_head):
        Guid = Guid('b37df687-bc88-4b46-b3be-b458b3ea9e7f')
    return IFaxOutgoingMessage2
def _define_IFaxOutgoingMessage2():
    IFaxOutgoingMessage2 = win32more.Devices.Fax.IFaxOutgoingMessage2_head
    IFaxOutgoingMessage2.get_HasCoverPage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(26, 'get_HasCoverPage', ((1, 'pbHasCoverPage'),)))
    IFaxOutgoingMessage2.get_ReceiptType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_RECEIPT_TYPE_ENUM), use_last_error=False)(27, 'get_ReceiptType', ((1, 'pReceiptType'),)))
    IFaxOutgoingMessage2.get_ReceiptAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(28, 'get_ReceiptAddress', ((1, 'pbstrReceiptAddress'),)))
    IFaxOutgoingMessage2.get_Read = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(29, 'get_Read', ((1, 'pbRead'),)))
    IFaxOutgoingMessage2.put_Read = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(30, 'put_Read', ((1, 'bRead'),)))
    IFaxOutgoingMessage2.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(31, 'Save', ()))
    IFaxOutgoingMessage2.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(32, 'Refresh', ()))
    return IFaxOutgoingMessage2
def _define_IFaxAccountIncomingArchive_head():
    class IFaxAccountIncomingArchive(win32more.System.Com.IDispatch_head):
        Guid = Guid('a8a5b6ef-e0d6-4aee-955c-91625bec9db4')
    return IFaxAccountIncomingArchive
def _define_IFaxAccountIncomingArchive():
    IFaxAccountIncomingArchive = win32more.Devices.Fax.IFaxAccountIncomingArchive_head
    IFaxAccountIncomingArchive.get_SizeLow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_SizeLow', ((1, 'plSizeLow'),)))
    IFaxAccountIncomingArchive.get_SizeHigh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_SizeHigh', ((1, 'plSizeHigh'),)))
    IFaxAccountIncomingArchive.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(9, 'Refresh', ()))
    IFaxAccountIncomingArchive.GetMessages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Devices.Fax.IFaxIncomingMessageIterator_head), use_last_error=False)(10, 'GetMessages', ((1, 'lPrefetchSize'),(1, 'pFaxIncomingMessageIterator'),)))
    IFaxAccountIncomingArchive.GetMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Devices.Fax.IFaxIncomingMessage_head), use_last_error=False)(11, 'GetMessage', ((1, 'bstrMessageId'),(1, 'pFaxIncomingMessage'),)))
    return IFaxAccountIncomingArchive
def _define_IFaxAccountOutgoingArchive_head():
    class IFaxAccountOutgoingArchive(win32more.System.Com.IDispatch_head):
        Guid = Guid('5463076d-ec14-491f-926e-b3ceda5e5662')
    return IFaxAccountOutgoingArchive
def _define_IFaxAccountOutgoingArchive():
    IFaxAccountOutgoingArchive = win32more.Devices.Fax.IFaxAccountOutgoingArchive_head
    IFaxAccountOutgoingArchive.get_SizeLow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_SizeLow', ((1, 'plSizeLow'),)))
    IFaxAccountOutgoingArchive.get_SizeHigh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_SizeHigh', ((1, 'plSizeHigh'),)))
    IFaxAccountOutgoingArchive.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(9, 'Refresh', ()))
    IFaxAccountOutgoingArchive.GetMessages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Devices.Fax.IFaxOutgoingMessageIterator_head), use_last_error=False)(10, 'GetMessages', ((1, 'lPrefetchSize'),(1, 'pFaxOutgoingMessageIterator'),)))
    IFaxAccountOutgoingArchive.GetMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Devices.Fax.IFaxOutgoingMessage_head), use_last_error=False)(11, 'GetMessage', ((1, 'bstrMessageId'),(1, 'pFaxOutgoingMessage'),)))
    return IFaxAccountOutgoingArchive
FAX_ACCESS_RIGHTS_ENUM_2 = Int32
far2SUBMIT_LOW = 1
far2SUBMIT_NORMAL = 2
far2SUBMIT_HIGH = 4
far2QUERY_OUT_JOBS = 8
far2MANAGE_OUT_JOBS = 16
far2QUERY_CONFIG = 32
far2MANAGE_CONFIG = 64
far2QUERY_ARCHIVES = 128
far2MANAGE_ARCHIVES = 256
far2MANAGE_RECEIVE_FOLDER = 512
def _define_IFaxSecurity2_head():
    class IFaxSecurity2(win32more.System.Com.IDispatch_head):
        Guid = Guid('17d851f4-d09b-48fc-99c9-8f24c4db9ab1')
    return IFaxSecurity2
def _define_IFaxSecurity2():
    IFaxSecurity2 = win32more.Devices.Fax.IFaxSecurity2_head
    IFaxSecurity2.get_Descriptor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(7, 'get_Descriptor', ((1, 'pvDescriptor'),)))
    IFaxSecurity2.put_Descriptor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(8, 'put_Descriptor', ((1, 'vDescriptor'),)))
    IFaxSecurity2.get_GrantedRights = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_ACCESS_RIGHTS_ENUM_2), use_last_error=False)(9, 'get_GrantedRights', ((1, 'pGrantedRights'),)))
    IFaxSecurity2.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(10, 'Refresh', ()))
    IFaxSecurity2.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(11, 'Save', ()))
    IFaxSecurity2.get_InformationType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(12, 'get_InformationType', ((1, 'plInformationType'),)))
    IFaxSecurity2.put_InformationType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(13, 'put_InformationType', ((1, 'lInformationType'),)))
    return IFaxSecurity2
def _define_IFaxIncomingMessage2_head():
    class IFaxIncomingMessage2(win32more.Devices.Fax.IFaxIncomingMessage_head):
        Guid = Guid('f9208503-e2bc-48f3-9ec0-e6236f9b509a')
    return IFaxIncomingMessage2
def _define_IFaxIncomingMessage2():
    IFaxIncomingMessage2 = win32more.Devices.Fax.IFaxIncomingMessage2_head
    IFaxIncomingMessage2.get_Subject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(20, 'get_Subject', ((1, 'pbstrSubject'),)))
    IFaxIncomingMessage2.put_Subject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(21, 'put_Subject', ((1, 'bstrSubject'),)))
    IFaxIncomingMessage2.get_SenderName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(22, 'get_SenderName', ((1, 'pbstrSenderName'),)))
    IFaxIncomingMessage2.put_SenderName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(23, 'put_SenderName', ((1, 'bstrSenderName'),)))
    IFaxIncomingMessage2.get_SenderFaxNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(24, 'get_SenderFaxNumber', ((1, 'pbstrSenderFaxNumber'),)))
    IFaxIncomingMessage2.put_SenderFaxNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(25, 'put_SenderFaxNumber', ((1, 'bstrSenderFaxNumber'),)))
    IFaxIncomingMessage2.get_HasCoverPage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(26, 'get_HasCoverPage', ((1, 'pbHasCoverPage'),)))
    IFaxIncomingMessage2.put_HasCoverPage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(27, 'put_HasCoverPage', ((1, 'bHasCoverPage'),)))
    IFaxIncomingMessage2.get_Recipients = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(28, 'get_Recipients', ((1, 'pbstrRecipients'),)))
    IFaxIncomingMessage2.put_Recipients = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(29, 'put_Recipients', ((1, 'bstrRecipients'),)))
    IFaxIncomingMessage2.get_WasReAssigned = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(30, 'get_WasReAssigned', ((1, 'pbWasReAssigned'),)))
    IFaxIncomingMessage2.get_Read = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(31, 'get_Read', ((1, 'pbRead'),)))
    IFaxIncomingMessage2.put_Read = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(32, 'put_Read', ((1, 'bRead'),)))
    IFaxIncomingMessage2.ReAssign = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(33, 'ReAssign', ()))
    IFaxIncomingMessage2.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(34, 'Save', ()))
    IFaxIncomingMessage2.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(35, 'Refresh', ()))
    return IFaxIncomingMessage2
FAX_ROUTING_RULE_CODE_ENUM = Int32
frrcANY_CODE = 0
def _define_IFaxServerNotify_head():
    class IFaxServerNotify(win32more.System.Com.IDispatch_head):
        Guid = Guid('2e037b27-cf8a-4abd-b1e0-5704943bea6f')
    return IFaxServerNotify
def _define_IFaxServerNotify():
    IFaxServerNotify = win32more.Devices.Fax.IFaxServerNotify_head
    return IFaxServerNotify
def _define__IFaxServerNotify2_head():
    class _IFaxServerNotify2(win32more.System.Com.IDispatch_head):
        Guid = Guid('ec9c69b9-5fe7-4805-9467-82fcd96af903')
    return _IFaxServerNotify2
def _define__IFaxServerNotify2():
    _IFaxServerNotify2 = win32more.Devices.Fax._IFaxServerNotify2_head
    _IFaxServerNotify2.OnIncomingJobAdded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head,win32more.Foundation.BSTR, use_last_error=False)(7, 'OnIncomingJobAdded', ((1, 'pFaxServer'),(1, 'bstrJobId'),)))
    _IFaxServerNotify2.OnIncomingJobRemoved = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head,win32more.Foundation.BSTR, use_last_error=False)(8, 'OnIncomingJobRemoved', ((1, 'pFaxServer'),(1, 'bstrJobId'),)))
    _IFaxServerNotify2.OnIncomingJobChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head,win32more.Foundation.BSTR,win32more.Devices.Fax.IFaxJobStatus_head, use_last_error=False)(9, 'OnIncomingJobChanged', ((1, 'pFaxServer'),(1, 'bstrJobId'),(1, 'pJobStatus'),)))
    _IFaxServerNotify2.OnOutgoingJobAdded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head,win32more.Foundation.BSTR, use_last_error=False)(10, 'OnOutgoingJobAdded', ((1, 'pFaxServer'),(1, 'bstrJobId'),)))
    _IFaxServerNotify2.OnOutgoingJobRemoved = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head,win32more.Foundation.BSTR, use_last_error=False)(11, 'OnOutgoingJobRemoved', ((1, 'pFaxServer'),(1, 'bstrJobId'),)))
    _IFaxServerNotify2.OnOutgoingJobChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head,win32more.Foundation.BSTR,win32more.Devices.Fax.IFaxJobStatus_head, use_last_error=False)(12, 'OnOutgoingJobChanged', ((1, 'pFaxServer'),(1, 'bstrJobId'),(1, 'pJobStatus'),)))
    _IFaxServerNotify2.OnIncomingMessageAdded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head,win32more.Foundation.BSTR, use_last_error=False)(13, 'OnIncomingMessageAdded', ((1, 'pFaxServer'),(1, 'bstrMessageId'),)))
    _IFaxServerNotify2.OnIncomingMessageRemoved = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head,win32more.Foundation.BSTR, use_last_error=False)(14, 'OnIncomingMessageRemoved', ((1, 'pFaxServer'),(1, 'bstrMessageId'),)))
    _IFaxServerNotify2.OnOutgoingMessageAdded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head,win32more.Foundation.BSTR, use_last_error=False)(15, 'OnOutgoingMessageAdded', ((1, 'pFaxServer'),(1, 'bstrMessageId'),)))
    _IFaxServerNotify2.OnOutgoingMessageRemoved = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head,win32more.Foundation.BSTR, use_last_error=False)(16, 'OnOutgoingMessageRemoved', ((1, 'pFaxServer'),(1, 'bstrMessageId'),)))
    _IFaxServerNotify2.OnReceiptOptionsChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head, use_last_error=False)(17, 'OnReceiptOptionsChange', ((1, 'pFaxServer'),)))
    _IFaxServerNotify2.OnActivityLoggingConfigChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head, use_last_error=False)(18, 'OnActivityLoggingConfigChange', ((1, 'pFaxServer'),)))
    _IFaxServerNotify2.OnSecurityConfigChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head, use_last_error=False)(19, 'OnSecurityConfigChange', ((1, 'pFaxServer'),)))
    _IFaxServerNotify2.OnEventLoggingConfigChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head, use_last_error=False)(20, 'OnEventLoggingConfigChange', ((1, 'pFaxServer'),)))
    _IFaxServerNotify2.OnOutgoingQueueConfigChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head, use_last_error=False)(21, 'OnOutgoingQueueConfigChange', ((1, 'pFaxServer'),)))
    _IFaxServerNotify2.OnOutgoingArchiveConfigChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head, use_last_error=False)(22, 'OnOutgoingArchiveConfigChange', ((1, 'pFaxServer'),)))
    _IFaxServerNotify2.OnIncomingArchiveConfigChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head, use_last_error=False)(23, 'OnIncomingArchiveConfigChange', ((1, 'pFaxServer'),)))
    _IFaxServerNotify2.OnDevicesConfigChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head, use_last_error=False)(24, 'OnDevicesConfigChange', ((1, 'pFaxServer'),)))
    _IFaxServerNotify2.OnOutboundRoutingGroupsConfigChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head, use_last_error=False)(25, 'OnOutboundRoutingGroupsConfigChange', ((1, 'pFaxServer'),)))
    _IFaxServerNotify2.OnOutboundRoutingRulesConfigChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head, use_last_error=False)(26, 'OnOutboundRoutingRulesConfigChange', ((1, 'pFaxServer'),)))
    _IFaxServerNotify2.OnServerActivityChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head,Int32,Int32,Int32,Int32, use_last_error=False)(27, 'OnServerActivityChange', ((1, 'pFaxServer'),(1, 'lIncomingMessages'),(1, 'lRoutingMessages'),(1, 'lOutgoingMessages'),(1, 'lQueuedMessages'),)))
    _IFaxServerNotify2.OnQueuesStatusChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head,Int16,Int16,Int16, use_last_error=False)(28, 'OnQueuesStatusChange', ((1, 'pFaxServer'),(1, 'bOutgoingQueueBlocked'),(1, 'bOutgoingQueuePaused'),(1, 'bIncomingQueueBlocked'),)))
    _IFaxServerNotify2.OnNewCall = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head,Int32,Int32,win32more.Foundation.BSTR, use_last_error=False)(29, 'OnNewCall', ((1, 'pFaxServer'),(1, 'lCallId'),(1, 'lDeviceId'),(1, 'bstrCallerId'),)))
    _IFaxServerNotify2.OnServerShutDown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head, use_last_error=False)(30, 'OnServerShutDown', ((1, 'pFaxServer'),)))
    _IFaxServerNotify2.OnDeviceStatusChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head,Int32,Int16,Int16,Int16,Int16, use_last_error=False)(31, 'OnDeviceStatusChange', ((1, 'pFaxServer'),(1, 'lDeviceId'),(1, 'bPoweredOff'),(1, 'bSending'),(1, 'bReceiving'),(1, 'bRinging'),)))
    _IFaxServerNotify2.OnGeneralServerConfigChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head, use_last_error=False)(32, 'OnGeneralServerConfigChanged', ((1, 'pFaxServer'),)))
    return _IFaxServerNotify2
def _define_IFaxServerNotify2_head():
    class IFaxServerNotify2(win32more.System.Com.IDispatch_head):
        Guid = Guid('616ca8d6-a77a-4062-abfd-0e471241c7aa')
    return IFaxServerNotify2
def _define_IFaxServerNotify2():
    IFaxServerNotify2 = win32more.Devices.Fax.IFaxServerNotify2_head
    return IFaxServerNotify2
def _define__IFaxAccountNotify_head():
    class _IFaxAccountNotify(win32more.System.Com.IDispatch_head):
        Guid = Guid('b9b3bc81-ac1b-46f3-b39d-0adc30e1b788')
    return _IFaxAccountNotify
def _define__IFaxAccountNotify():
    _IFaxAccountNotify = win32more.Devices.Fax._IFaxAccountNotify_head
    _IFaxAccountNotify.OnIncomingJobAdded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxAccount_head,win32more.Foundation.BSTR, use_last_error=False)(7, 'OnIncomingJobAdded', ((1, 'pFaxAccount'),(1, 'bstrJobId'),)))
    _IFaxAccountNotify.OnIncomingJobRemoved = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxAccount_head,win32more.Foundation.BSTR, use_last_error=False)(8, 'OnIncomingJobRemoved', ((1, 'pFaxAccount'),(1, 'bstrJobId'),)))
    _IFaxAccountNotify.OnIncomingJobChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxAccount_head,win32more.Foundation.BSTR,win32more.Devices.Fax.IFaxJobStatus_head, use_last_error=False)(9, 'OnIncomingJobChanged', ((1, 'pFaxAccount'),(1, 'bstrJobId'),(1, 'pJobStatus'),)))
    _IFaxAccountNotify.OnOutgoingJobAdded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxAccount_head,win32more.Foundation.BSTR, use_last_error=False)(10, 'OnOutgoingJobAdded', ((1, 'pFaxAccount'),(1, 'bstrJobId'),)))
    _IFaxAccountNotify.OnOutgoingJobRemoved = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxAccount_head,win32more.Foundation.BSTR, use_last_error=False)(11, 'OnOutgoingJobRemoved', ((1, 'pFaxAccount'),(1, 'bstrJobId'),)))
    _IFaxAccountNotify.OnOutgoingJobChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxAccount_head,win32more.Foundation.BSTR,win32more.Devices.Fax.IFaxJobStatus_head, use_last_error=False)(12, 'OnOutgoingJobChanged', ((1, 'pFaxAccount'),(1, 'bstrJobId'),(1, 'pJobStatus'),)))
    _IFaxAccountNotify.OnIncomingMessageAdded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxAccount_head,win32more.Foundation.BSTR,Int16, use_last_error=False)(13, 'OnIncomingMessageAdded', ((1, 'pFaxAccount'),(1, 'bstrMessageId'),(1, 'fAddedToReceiveFolder'),)))
    _IFaxAccountNotify.OnIncomingMessageRemoved = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxAccount_head,win32more.Foundation.BSTR,Int16, use_last_error=False)(14, 'OnIncomingMessageRemoved', ((1, 'pFaxAccount'),(1, 'bstrMessageId'),(1, 'fRemovedFromReceiveFolder'),)))
    _IFaxAccountNotify.OnOutgoingMessageAdded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxAccount_head,win32more.Foundation.BSTR, use_last_error=False)(15, 'OnOutgoingMessageAdded', ((1, 'pFaxAccount'),(1, 'bstrMessageId'),)))
    _IFaxAccountNotify.OnOutgoingMessageRemoved = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxAccount_head,win32more.Foundation.BSTR, use_last_error=False)(16, 'OnOutgoingMessageRemoved', ((1, 'pFaxAccount'),(1, 'bstrMessageId'),)))
    _IFaxAccountNotify.OnServerShutDown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head, use_last_error=False)(17, 'OnServerShutDown', ((1, 'pFaxServer'),)))
    return _IFaxAccountNotify
def _define_IFaxAccountNotify_head():
    class IFaxAccountNotify(win32more.System.Com.IDispatch_head):
        Guid = Guid('0b5e5bd1-b8a9-47a0-a323-ef4a293ba06a')
    return IFaxAccountNotify
def _define_IFaxAccountNotify():
    IFaxAccountNotify = win32more.Devices.Fax.IFaxAccountNotify_head
    return IFaxAccountNotify
def _define_PFAXROUTEADDFILE():
    return CFUNCTYPE(Int32,UInt32,win32more.Foundation.PWSTR,POINTER(Guid), use_last_error=False)
def _define_PFAXROUTEDELETEFILE():
    return CFUNCTYPE(Int32,UInt32,win32more.Foundation.PWSTR, use_last_error=False)
def _define_PFAXROUTEGETFILE():
    return CFUNCTYPE(win32more.Foundation.BOOL,UInt32,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)
def _define_PFAXROUTEENUMFILE():
    return CFUNCTYPE(win32more.Foundation.BOOL,UInt32,POINTER(Guid),POINTER(Guid),win32more.Foundation.PWSTR,c_void_p, use_last_error=False)
def _define_PFAXROUTEENUMFILES():
    return CFUNCTYPE(win32more.Foundation.BOOL,UInt32,POINTER(Guid),win32more.Devices.Fax.PFAXROUTEENUMFILE,c_void_p, use_last_error=False)
def _define_PFAXROUTEMODIFYROUTINGDATA():
    return CFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.Foundation.PWSTR,c_char_p_no,UInt32, use_last_error=False)
def _define_FAX_ROUTE_CALLBACKROUTINES_head():
    class FAX_ROUTE_CALLBACKROUTINES(Structure):
        pass
    return FAX_ROUTE_CALLBACKROUTINES
def _define_FAX_ROUTE_CALLBACKROUTINES():
    FAX_ROUTE_CALLBACKROUTINES = win32more.Devices.Fax.FAX_ROUTE_CALLBACKROUTINES_head
    FAX_ROUTE_CALLBACKROUTINES._fields_ = [
        ("SizeOfStruct", UInt32),
        ("FaxRouteAddFile", win32more.Devices.Fax.PFAXROUTEADDFILE),
        ("FaxRouteDeleteFile", win32more.Devices.Fax.PFAXROUTEDELETEFILE),
        ("FaxRouteGetFile", win32more.Devices.Fax.PFAXROUTEGETFILE),
        ("FaxRouteEnumFiles", win32more.Devices.Fax.PFAXROUTEENUMFILES),
        ("FaxRouteModifyRoutingData", win32more.Devices.Fax.PFAXROUTEMODIFYROUTINGDATA),
    ]
    return FAX_ROUTE_CALLBACKROUTINES
def _define_FAX_ROUTE_head():
    class FAX_ROUTE(Structure):
        pass
    return FAX_ROUTE
def _define_FAX_ROUTE():
    FAX_ROUTE = win32more.Devices.Fax.FAX_ROUTE_head
    FAX_ROUTE._fields_ = [
        ("SizeOfStruct", UInt32),
        ("JobId", UInt32),
        ("ElapsedTime", UInt64),
        ("ReceiveTime", UInt64),
        ("PageCount", UInt32),
        ("Csid", win32more.Foundation.PWSTR),
        ("Tsid", win32more.Foundation.PWSTR),
        ("CallerId", win32more.Foundation.PWSTR),
        ("RoutingInfo", win32more.Foundation.PWSTR),
        ("ReceiverName", win32more.Foundation.PWSTR),
        ("ReceiverNumber", win32more.Foundation.PWSTR),
        ("DeviceName", win32more.Foundation.PWSTR),
        ("DeviceId", UInt32),
        ("RoutingInfoData", c_char_p_no),
        ("RoutingInfoDataSize", UInt32),
    ]
    return FAX_ROUTE
FAXROUTE_ENABLE = Int32
QUERY_STATUS = -1
STATUS_DISABLE = 0
STATUS_ENABLE = 1
def _define_PFAXROUTEINITIALIZE():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Fax.FAX_ROUTE_CALLBACKROUTINES_head), use_last_error=False)
def _define_PFAXROUTEMETHOD():
    return CFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Fax.FAX_ROUTE_head),POINTER(c_void_p),POINTER(UInt32), use_last_error=False)
def _define_PFAXROUTEDEVICEENABLE():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,UInt32,Int32, use_last_error=False)
def _define_PFAXROUTEDEVICECHANGENOTIFICATION():
    return CFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.Foundation.BOOL, use_last_error=False)
def _define_PFAXROUTEGETROUTINGINFO():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,UInt32,c_char_p_no,POINTER(UInt32), use_last_error=False)
def _define_PFAXROUTESETROUTINGINFO():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,UInt32,c_char_p_no,UInt32, use_last_error=False)
FAX_ENUM_DEVICE_ID_SOURCE = Int32
DEV_ID_SRC_FAX = 0
DEV_ID_SRC_TAPI = 1
def _define_PFAX_EXT_GET_DATA():
    return CFUNCTYPE(UInt32,UInt32,win32more.Devices.Fax.FAX_ENUM_DEVICE_ID_SOURCE,win32more.Foundation.PWSTR,POINTER(c_char_p_no),POINTER(UInt32), use_last_error=False)
def _define_PFAX_EXT_SET_DATA():
    return CFUNCTYPE(UInt32,win32more.Foundation.HINSTANCE,UInt32,win32more.Devices.Fax.FAX_ENUM_DEVICE_ID_SOURCE,win32more.Foundation.PWSTR,c_char_p_no,UInt32, use_last_error=False)
def _define_PFAX_EXT_CONFIG_CHANGE():
    return CFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,c_char_p_no,UInt32, use_last_error=False)
def _define_PFAX_EXT_REGISTER_FOR_EVENTS():
    return CFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.HINSTANCE,UInt32,win32more.Devices.Fax.FAX_ENUM_DEVICE_ID_SOURCE,win32more.Foundation.PWSTR,win32more.Devices.Fax.PFAX_EXT_CONFIG_CHANGE, use_last_error=False)
def _define_PFAX_EXT_UNREGISTER_FOR_EVENTS():
    return CFUNCTYPE(UInt32,win32more.Foundation.HANDLE, use_last_error=False)
def _define_PFAX_EXT_FREE_BUFFER():
    return CFUNCTYPE(Void,c_void_p, use_last_error=False)
def _define_PFAX_EXT_INITIALIZE_CONFIG():
    return CFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.PFAX_EXT_GET_DATA,win32more.Devices.Fax.PFAX_EXT_SET_DATA,win32more.Devices.Fax.PFAX_EXT_REGISTER_FOR_EVENTS,win32more.Devices.Fax.PFAX_EXT_UNREGISTER_FOR_EVENTS,win32more.Devices.Fax.PFAX_EXT_FREE_BUFFER, use_last_error=False)
SendToMode = Int32
SEND_TO_FAX_RECIPIENT_ATTACHMENT = 0
STI_DEVICE_MJ_TYPE = Int32
STI_DEVICE_MJ_TYPE_StiDeviceTypeDefault = 0
STI_DEVICE_MJ_TYPE_StiDeviceTypeScanner = 1
STI_DEVICE_MJ_TYPE_StiDeviceTypeDigitalCamera = 2
STI_DEVICE_MJ_TYPE_StiDeviceTypeStreamingVideo = 3
def _define_STI_DEV_CAPS_head():
    class STI_DEV_CAPS(Structure):
        pass
    return STI_DEV_CAPS
def _define_STI_DEV_CAPS():
    STI_DEV_CAPS = win32more.Devices.Fax.STI_DEV_CAPS_head
    STI_DEV_CAPS._fields_ = [
        ("dwGeneric", UInt32),
    ]
    return STI_DEV_CAPS
def _define_STI_DEVICE_INFORMATIONW_head():
    class STI_DEVICE_INFORMATIONW(Structure):
        pass
    return STI_DEVICE_INFORMATIONW
def _define_STI_DEVICE_INFORMATIONW():
    STI_DEVICE_INFORMATIONW = win32more.Devices.Fax.STI_DEVICE_INFORMATIONW_head
    STI_DEVICE_INFORMATIONW._fields_ = [
        ("dwSize", UInt32),
        ("DeviceType", UInt32),
        ("szDeviceInternalName", Char * 128),
        ("DeviceCapabilitiesA", win32more.Devices.Fax.STI_DEV_CAPS),
        ("dwHardwareConfiguration", UInt32),
        ("pszVendorDescription", win32more.Foundation.PWSTR),
        ("pszDeviceDescription", win32more.Foundation.PWSTR),
        ("pszPortName", win32more.Foundation.PWSTR),
        ("pszPropProvider", win32more.Foundation.PWSTR),
        ("pszLocalName", win32more.Foundation.PWSTR),
    ]
    return STI_DEVICE_INFORMATIONW
def _define_STI_WIA_DEVICE_INFORMATIONW_head():
    class STI_WIA_DEVICE_INFORMATIONW(Structure):
        pass
    return STI_WIA_DEVICE_INFORMATIONW
def _define_STI_WIA_DEVICE_INFORMATIONW():
    STI_WIA_DEVICE_INFORMATIONW = win32more.Devices.Fax.STI_WIA_DEVICE_INFORMATIONW_head
    STI_WIA_DEVICE_INFORMATIONW._fields_ = [
        ("dwSize", UInt32),
        ("DeviceType", UInt32),
        ("szDeviceInternalName", Char * 128),
        ("DeviceCapabilitiesA", win32more.Devices.Fax.STI_DEV_CAPS),
        ("dwHardwareConfiguration", UInt32),
        ("pszVendorDescription", win32more.Foundation.PWSTR),
        ("pszDeviceDescription", win32more.Foundation.PWSTR),
        ("pszPortName", win32more.Foundation.PWSTR),
        ("pszPropProvider", win32more.Foundation.PWSTR),
        ("pszLocalName", win32more.Foundation.PWSTR),
        ("pszUiDll", win32more.Foundation.PWSTR),
        ("pszServer", win32more.Foundation.PWSTR),
    ]
    return STI_WIA_DEVICE_INFORMATIONW
def _define_STI_DEVICE_STATUS_head():
    class STI_DEVICE_STATUS(Structure):
        pass
    return STI_DEVICE_STATUS
def _define_STI_DEVICE_STATUS():
    STI_DEVICE_STATUS = win32more.Devices.Fax.STI_DEVICE_STATUS_head
    STI_DEVICE_STATUS._fields_ = [
        ("dwSize", UInt32),
        ("StatusMask", UInt32),
        ("dwOnlineState", UInt32),
        ("dwHardwareStatusCode", UInt32),
        ("dwEventHandlingState", UInt32),
        ("dwPollingInterval", UInt32),
    ]
    return STI_DEVICE_STATUS
def _define__ERROR_INFOW_head():
    class _ERROR_INFOW(Structure):
        pass
    return _ERROR_INFOW
def _define__ERROR_INFOW():
    _ERROR_INFOW = win32more.Devices.Fax._ERROR_INFOW_head
    _ERROR_INFOW._fields_ = [
        ("dwSize", UInt32),
        ("dwGenericError", UInt32),
        ("dwVendorError", UInt32),
        ("szExtendedErrorText", Char * 255),
    ]
    return _ERROR_INFOW
def _define_STI_DIAG_head():
    class STI_DIAG(Structure):
        pass
    return STI_DIAG
def _define_STI_DIAG():
    STI_DIAG = win32more.Devices.Fax.STI_DIAG_head
    STI_DIAG._fields_ = [
        ("dwSize", UInt32),
        ("dwBasicDiagCode", UInt32),
        ("dwVendorDiagCode", UInt32),
        ("dwStatusMask", UInt32),
        ("sErrorInfo", win32more.Devices.Fax._ERROR_INFOW),
    ]
    return STI_DIAG
def _define_STISUBSCRIBE_head():
    class STISUBSCRIBE(Structure):
        pass
    return STISUBSCRIBE
def _define_STISUBSCRIBE():
    STISUBSCRIBE = win32more.Devices.Fax.STISUBSCRIBE_head
    STISUBSCRIBE._fields_ = [
        ("dwSize", UInt32),
        ("dwFlags", UInt32),
        ("dwFilter", UInt32),
        ("hWndNotify", win32more.Foundation.HWND),
        ("hEvent", win32more.Foundation.HANDLE),
        ("uiNotificationMessage", UInt32),
    ]
    return STISUBSCRIBE
def _define_STINOTIFY_head():
    class STINOTIFY(Structure):
        pass
    return STINOTIFY
def _define_STINOTIFY():
    STINOTIFY = win32more.Devices.Fax.STINOTIFY_head
    STINOTIFY._fields_ = [
        ("dwSize", UInt32),
        ("guidNotificationCode", Guid),
        ("abNotificationData", Byte * 64),
    ]
    return STINOTIFY
def _define_IStiDeviceW_head():
    class IStiDeviceW(Structure):
        pass
    return IStiDeviceW
def _define_IStiDeviceW():
    IStiDeviceW = win32more.Devices.Fax.IStiDeviceW_head
    return IStiDeviceW
def _define_IStillImageW_head():
    class IStillImageW(win32more.System.Com.IUnknown_head):
        Guid = Guid('641bd880-2dc8-11d0-90ea-00aa0060f86c')
    return IStillImageW
def _define_IStillImageW():
    IStillImageW = win32more.Devices.Fax.IStillImageW_head
    IStillImageW.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HINSTANCE,UInt32, use_last_error=False)(3, 'Initialize', ((1, 'hinst'),(1, 'dwVersion'),)))
    IStillImageW.GetDeviceList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(UInt32),POINTER(c_void_p), use_last_error=False)(4, 'GetDeviceList', ((1, 'dwType'),(1, 'dwFlags'),(1, 'pdwItemsReturned'),(1, 'ppBuffer'),)))
    IStillImageW.GetDeviceInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(c_void_p), use_last_error=False)(5, 'GetDeviceInfo', ((1, 'pwszDeviceName'),(1, 'ppBuffer'),)))
    IStillImageW.CreateDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Devices.Fax.IStiDevice_head),win32more.System.Com.IUnknown_head, use_last_error=False)(6, 'CreateDevice', ((1, 'pwszDeviceName'),(1, 'dwMode'),(1, 'pDevice'),(1, 'punkOuter'),)))
    IStillImageW.GetDeviceValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32),c_char_p_no,POINTER(UInt32), use_last_error=False)(7, 'GetDeviceValue', ((1, 'pwszDeviceName'),(1, 'pValueName'),(1, 'pType'),(1, 'pData'),(1, 'cbData'),)))
    IStillImageW.SetDeviceValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,c_char_p_no,UInt32, use_last_error=False)(8, 'SetDeviceValue', ((1, 'pwszDeviceName'),(1, 'pValueName'),(1, 'Type'),(1, 'pData'),(1, 'cbData'),)))
    IStillImageW.GetSTILaunchInformation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),POINTER(UInt32),POINTER(Char), use_last_error=False)(9, 'GetSTILaunchInformation', ((1, 'pwszDeviceName'),(1, 'pdwEventCode'),(1, 'pwszEventName'),)))
    IStillImageW.RegisterLaunchApplication = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(10, 'RegisterLaunchApplication', ((1, 'pwszAppName'),(1, 'pwszCommandLine'),)))
    IStillImageW.UnregisterLaunchApplication = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(11, 'UnregisterLaunchApplication', ((1, 'pwszAppName'),)))
    IStillImageW.EnableHwNotifications = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.BOOL, use_last_error=False)(12, 'EnableHwNotifications', ((1, 'pwszDeviceName'),(1, 'bNewState'),)))
    IStillImageW.GetHwNotificationState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.BOOL), use_last_error=False)(13, 'GetHwNotificationState', ((1, 'pwszDeviceName'),(1, 'pbCurrentState'),)))
    IStillImageW.RefreshDeviceBus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(14, 'RefreshDeviceBus', ((1, 'pwszDeviceName'),)))
    IStillImageW.LaunchApplicationForDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Devices.Fax.STINOTIFY_head), use_last_error=False)(15, 'LaunchApplicationForDevice', ((1, 'pwszDeviceName'),(1, 'pwszAppName'),(1, 'pStiNotify'),)))
    IStillImageW.SetupDeviceParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.STI_DEVICE_INFORMATIONW_head), use_last_error=False)(16, 'SetupDeviceParameters', ((1, 'param0'),)))
    IStillImageW.WriteToErrorLog = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR, use_last_error=False)(17, 'WriteToErrorLog', ((1, 'dwMessageType'),(1, 'pszMessage'),)))
    return IStillImageW
def _define_IStiDevice_head():
    class IStiDevice(win32more.System.Com.IUnknown_head):
        Guid = Guid('6cfa5a80-2dc8-11d0-90ea-00aa0060f86c')
    return IStiDevice
def _define_IStiDevice():
    IStiDevice = win32more.Devices.Fax.IStiDevice_head
    IStiDevice.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HINSTANCE,win32more.Foundation.PWSTR,UInt32,UInt32, use_last_error=False)(3, 'Initialize', ((1, 'hinst'),(1, 'pwszDeviceName'),(1, 'dwVersion'),(1, 'dwMode'),)))
    IStiDevice.GetCapabilities = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.STI_DEV_CAPS_head), use_last_error=False)(4, 'GetCapabilities', ((1, 'pDevCaps'),)))
    IStiDevice.GetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.STI_DEVICE_STATUS_head), use_last_error=False)(5, 'GetStatus', ((1, 'pDevStatus'),)))
    IStiDevice.DeviceReset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(6, 'DeviceReset', ()))
    IStiDevice.Diagnostic = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.STI_DIAG_head), use_last_error=False)(7, 'Diagnostic', ((1, 'pBuffer'),)))
    IStiDevice.Escape = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_void_p,UInt32,c_void_p,UInt32,POINTER(UInt32), use_last_error=False)(8, 'Escape', ((1, 'EscapeFunction'),(1, 'lpInData'),(1, 'cbInDataSize'),(1, 'pOutData'),(1, 'dwOutDataSize'),(1, 'pdwActualData'),)))
    IStiDevice.GetLastError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(9, 'GetLastError', ((1, 'pdwLastDeviceError'),)))
    IStiDevice.LockDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(10, 'LockDevice', ((1, 'dwTimeOut'),)))
    IStiDevice.UnLockDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(11, 'UnLockDevice', ()))
    IStiDevice.RawReadData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(UInt32),POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(12, 'RawReadData', ((1, 'lpBuffer'),(1, 'lpdwNumberOfBytes'),(1, 'lpOverlapped'),)))
    IStiDevice.RawWriteData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(13, 'RawWriteData', ((1, 'lpBuffer'),(1, 'nNumberOfBytes'),(1, 'lpOverlapped'),)))
    IStiDevice.RawReadCommand = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(UInt32),POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(14, 'RawReadCommand', ((1, 'lpBuffer'),(1, 'lpdwNumberOfBytes'),(1, 'lpOverlapped'),)))
    IStiDevice.RawWriteCommand = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(15, 'RawWriteCommand', ((1, 'lpBuffer'),(1, 'nNumberOfBytes'),(1, 'lpOverlapped'),)))
    IStiDevice.Subscribe = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.STISUBSCRIBE_head), use_last_error=False)(16, 'Subscribe', ((1, 'lpSubsribe'),)))
    IStiDevice.GetLastNotificationData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.STINOTIFY_head), use_last_error=False)(17, 'GetLastNotificationData', ((1, 'lpNotify'),)))
    IStiDevice.UnSubscribe = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(18, 'UnSubscribe', ()))
    IStiDevice.GetLastErrorInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax._ERROR_INFOW_head), use_last_error=False)(19, 'GetLastErrorInfo', ((1, 'pLastErrorInfo'),)))
    return IStiDevice
def _define_STI_USD_CAPS_head():
    class STI_USD_CAPS(Structure):
        pass
    return STI_USD_CAPS
def _define_STI_USD_CAPS():
    STI_USD_CAPS = win32more.Devices.Fax.STI_USD_CAPS_head
    STI_USD_CAPS._fields_ = [
        ("dwVersion", UInt32),
        ("dwGenericCaps", UInt32),
    ]
    return STI_USD_CAPS
def _define_IStiDeviceControl_head():
    class IStiDeviceControl(win32more.System.Com.IUnknown_head):
        Guid = Guid('128a9860-52dc-11d0-9edf-444553540000')
    return IStiDeviceControl
def _define_IStiDeviceControl():
    IStiDeviceControl = win32more.Devices.Fax.IStiDeviceControl_head
    IStiDeviceControl.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(3, 'Initialize', ((1, 'dwDeviceType'),(1, 'dwMode'),(1, 'pwszPortName'),(1, 'dwFlags'),)))
    IStiDeviceControl.RawReadData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(UInt32),POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(4, 'RawReadData', ((1, 'lpBuffer'),(1, 'lpdwNumberOfBytes'),(1, 'lpOverlapped'),)))
    IStiDeviceControl.RawWriteData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(5, 'RawWriteData', ((1, 'lpBuffer'),(1, 'nNumberOfBytes'),(1, 'lpOverlapped'),)))
    IStiDeviceControl.RawReadCommand = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(UInt32),POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(6, 'RawReadCommand', ((1, 'lpBuffer'),(1, 'lpdwNumberOfBytes'),(1, 'lpOverlapped'),)))
    IStiDeviceControl.RawWriteCommand = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(7, 'RawWriteCommand', ((1, 'lpBuffer'),(1, 'nNumberOfBytes'),(1, 'lpOverlapped'),)))
    IStiDeviceControl.RawDeviceControl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_void_p,UInt32,c_void_p,UInt32,POINTER(UInt32), use_last_error=False)(8, 'RawDeviceControl', ((1, 'EscapeFunction'),(1, 'lpInData'),(1, 'cbInDataSize'),(1, 'pOutData'),(1, 'dwOutDataSize'),(1, 'pdwActualData'),)))
    IStiDeviceControl.GetLastError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(9, 'GetLastError', ((1, 'lpdwLastError'),)))
    IStiDeviceControl.GetMyDevicePortName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),UInt32, use_last_error=False)(10, 'GetMyDevicePortName', ((1, 'lpszDevicePath'),(1, 'cwDevicePathSize'),)))
    IStiDeviceControl.GetMyDeviceHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(11, 'GetMyDeviceHandle', ((1, 'lph'),)))
    IStiDeviceControl.GetMyDeviceOpenMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(12, 'GetMyDeviceOpenMode', ((1, 'pdwOpenMode'),)))
    IStiDeviceControl.WriteToErrorLog = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(13, 'WriteToErrorLog', ((1, 'dwMessageType'),(1, 'pszMessage'),(1, 'dwErrorCode'),)))
    return IStiDeviceControl
def _define_IStiUSD_head():
    class IStiUSD(win32more.System.Com.IUnknown_head):
        Guid = Guid('0c9bb460-51ac-11d0-90ea-00aa0060f86c')
    return IStiUSD
def _define_IStiUSD():
    IStiUSD = win32more.Devices.Fax.IStiUSD_head
    IStiUSD.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IStiDeviceControl_head,UInt32,win32more.System.Registry.HKEY, use_last_error=False)(3, 'Initialize', ((1, 'pHelDcb'),(1, 'dwStiVersion'),(1, 'hParametersKey'),)))
    IStiUSD.GetCapabilities = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.STI_USD_CAPS_head), use_last_error=False)(4, 'GetCapabilities', ((1, 'pDevCaps'),)))
    IStiUSD.GetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.STI_DEVICE_STATUS_head), use_last_error=False)(5, 'GetStatus', ((1, 'pDevStatus'),)))
    IStiUSD.DeviceReset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(6, 'DeviceReset', ()))
    IStiUSD.Diagnostic = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.STI_DIAG_head), use_last_error=False)(7, 'Diagnostic', ((1, 'pBuffer'),)))
    IStiUSD.Escape = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_void_p,UInt32,c_void_p,UInt32,POINTER(UInt32), use_last_error=False)(8, 'Escape', ((1, 'EscapeFunction'),(1, 'lpInData'),(1, 'cbInDataSize'),(1, 'pOutData'),(1, 'cbOutDataSize'),(1, 'pdwActualData'),)))
    IStiUSD.GetLastError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(9, 'GetLastError', ((1, 'pdwLastDeviceError'),)))
    IStiUSD.LockDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(10, 'LockDevice', ()))
    IStiUSD.UnLockDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(11, 'UnLockDevice', ()))
    IStiUSD.RawReadData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(UInt32),POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(12, 'RawReadData', ((1, 'lpBuffer'),(1, 'lpdwNumberOfBytes'),(1, 'lpOverlapped'),)))
    IStiUSD.RawWriteData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(13, 'RawWriteData', ((1, 'lpBuffer'),(1, 'nNumberOfBytes'),(1, 'lpOverlapped'),)))
    IStiUSD.RawReadCommand = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(UInt32),POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(14, 'RawReadCommand', ((1, 'lpBuffer'),(1, 'lpdwNumberOfBytes'),(1, 'lpOverlapped'),)))
    IStiUSD.RawWriteCommand = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(15, 'RawWriteCommand', ((1, 'lpBuffer'),(1, 'nNumberOfBytes'),(1, 'lpOverlapped'),)))
    IStiUSD.SetNotificationHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE, use_last_error=False)(16, 'SetNotificationHandle', ((1, 'hEvent'),)))
    IStiUSD.GetNotificationData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.STINOTIFY_head), use_last_error=False)(17, 'GetNotificationData', ((1, 'lpNotify'),)))
    IStiUSD.GetLastErrorInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax._ERROR_INFOW_head), use_last_error=False)(18, 'GetLastErrorInfo', ((1, 'pLastErrorInfo'),)))
    return IStiUSD
def _define_FaxConnectFaxServerA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,POINTER(win32more.Foundation.HANDLE), use_last_error=True)(("FaxConnectFaxServerA", windll["WINFAX"]), ((1, 'MachineName'),(1, 'FaxHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxConnectFaxServerW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.HANDLE), use_last_error=True)(("FaxConnectFaxServerW", windll["WINFAX"]), ((1, 'MachineName'),(1, 'FaxHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxConnectFaxServer():
    return win32more.Devices.Fax.FaxConnectFaxServerW
def _define_FaxClose():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE, use_last_error=False)(("FaxClose", windll["WINFAX"]), ((1, 'FaxHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxOpenPort():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,UInt32,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("FaxOpenPort", windll["WINFAX"]), ((1, 'FaxHandle'),(1, 'DeviceId'),(1, 'Flags'),(1, 'FaxPortHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxCompleteJobParamsA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(POINTER(win32more.Devices.Fax.FAX_JOB_PARAMA_head)),POINTER(POINTER(win32more.Devices.Fax.FAX_COVERPAGE_INFOA_head)), use_last_error=False)(("FaxCompleteJobParamsA", windll["WINFAX"]), ((1, 'JobParams'),(1, 'CoverpageInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxCompleteJobParamsW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(POINTER(win32more.Devices.Fax.FAX_JOB_PARAMW_head)),POINTER(POINTER(win32more.Devices.Fax.FAX_COVERPAGE_INFOW_head)), use_last_error=False)(("FaxCompleteJobParamsW", windll["WINFAX"]), ((1, 'JobParams'),(1, 'CoverpageInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxCompleteJobParams():
    return win32more.Devices.Fax.FaxCompleteJobParamsW
def _define_FaxSendDocumentA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,POINTER(win32more.Devices.Fax.FAX_JOB_PARAMA_head),POINTER(win32more.Devices.Fax.FAX_COVERPAGE_INFOA_head),POINTER(UInt32), use_last_error=True)(("FaxSendDocumentA", windll["WINFAX"]), ((1, 'FaxHandle'),(1, 'FileName'),(1, 'JobParams'),(1, 'CoverpageInfo'),(1, 'FaxJobId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxSendDocumentW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,POINTER(win32more.Devices.Fax.FAX_JOB_PARAMW_head),POINTER(win32more.Devices.Fax.FAX_COVERPAGE_INFOW_head),POINTER(UInt32), use_last_error=True)(("FaxSendDocumentW", windll["WINFAX"]), ((1, 'FaxHandle'),(1, 'FileName'),(1, 'JobParams'),(1, 'CoverpageInfo'),(1, 'FaxJobId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxSendDocument():
    return win32more.Devices.Fax.FaxSendDocumentW
def _define_FaxSendDocumentForBroadcastA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,POINTER(UInt32),win32more.Devices.Fax.PFAX_RECIPIENT_CALLBACKA,c_void_p, use_last_error=True)(("FaxSendDocumentForBroadcastA", windll["WINFAX"]), ((1, 'FaxHandle'),(1, 'FileName'),(1, 'FaxJobId'),(1, 'FaxRecipientCallback'),(1, 'Context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxSendDocumentForBroadcastW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,POINTER(UInt32),win32more.Devices.Fax.PFAX_RECIPIENT_CALLBACKW,c_void_p, use_last_error=True)(("FaxSendDocumentForBroadcastW", windll["WINFAX"]), ((1, 'FaxHandle'),(1, 'FileName'),(1, 'FaxJobId'),(1, 'FaxRecipientCallback'),(1, 'Context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxSendDocumentForBroadcast():
    return win32more.Devices.Fax.FaxSendDocumentForBroadcastW
def _define_FaxEnumJobsA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_JOB_ENTRYA_head)),POINTER(UInt32), use_last_error=True)(("FaxEnumJobsA", windll["WINFAX"]), ((1, 'FaxHandle'),(1, 'JobEntry'),(1, 'JobsReturned'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxEnumJobsW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_JOB_ENTRYW_head)),POINTER(UInt32), use_last_error=True)(("FaxEnumJobsW", windll["WINFAX"]), ((1, 'FaxHandle'),(1, 'JobEntry'),(1, 'JobsReturned'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxEnumJobs():
    return win32more.Devices.Fax.FaxEnumJobsW
def _define_FaxGetJobA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,POINTER(POINTER(win32more.Devices.Fax.FAX_JOB_ENTRYA_head)), use_last_error=True)(("FaxGetJobA", windll["WINFAX"]), ((1, 'FaxHandle'),(1, 'JobId'),(1, 'JobEntry'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxGetJobW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,POINTER(POINTER(win32more.Devices.Fax.FAX_JOB_ENTRYW_head)), use_last_error=True)(("FaxGetJobW", windll["WINFAX"]), ((1, 'FaxHandle'),(1, 'JobId'),(1, 'JobEntry'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxGetJob():
    return win32more.Devices.Fax.FaxGetJobW
def _define_FaxSetJobA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,UInt32,POINTER(win32more.Devices.Fax.FAX_JOB_ENTRYA_head), use_last_error=True)(("FaxSetJobA", windll["WINFAX"]), ((1, 'FaxHandle'),(1, 'JobId'),(1, 'Command'),(1, 'JobEntry'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxSetJobW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,UInt32,POINTER(win32more.Devices.Fax.FAX_JOB_ENTRYW_head), use_last_error=True)(("FaxSetJobW", windll["WINFAX"]), ((1, 'FaxHandle'),(1, 'JobId'),(1, 'Command'),(1, 'JobEntry'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxSetJob():
    return win32more.Devices.Fax.FaxSetJobW
def _define_FaxGetPageData():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,POINTER(c_char_p_no),POINTER(UInt32),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("FaxGetPageData", windll["WINFAX"]), ((1, 'FaxHandle'),(1, 'JobId'),(1, 'Buffer'),(1, 'BufferSize'),(1, 'ImageWidth'),(1, 'ImageHeight'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxGetDeviceStatusA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_DEVICE_STATUSA_head)), use_last_error=True)(("FaxGetDeviceStatusA", windll["WINFAX"]), ((1, 'FaxPortHandle'),(1, 'DeviceStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxGetDeviceStatusW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_DEVICE_STATUSW_head)), use_last_error=True)(("FaxGetDeviceStatusW", windll["WINFAX"]), ((1, 'FaxPortHandle'),(1, 'DeviceStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxGetDeviceStatus():
    return win32more.Devices.Fax.FaxGetDeviceStatusW
def _define_FaxAbort():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32, use_last_error=False)(("FaxAbort", windll["WINFAX"]), ((1, 'FaxHandle'),(1, 'JobId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxGetConfigurationA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_CONFIGURATIONA_head)), use_last_error=True)(("FaxGetConfigurationA", windll["WINFAX"]), ((1, 'FaxHandle'),(1, 'FaxConfig'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxGetConfigurationW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_CONFIGURATIONW_head)), use_last_error=True)(("FaxGetConfigurationW", windll["WINFAX"]), ((1, 'FaxHandle'),(1, 'FaxConfig'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxGetConfiguration():
    return win32more.Devices.Fax.FaxGetConfigurationW
def _define_FaxSetConfigurationA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Fax.FAX_CONFIGURATIONA_head), use_last_error=True)(("FaxSetConfigurationA", windll["WINFAX"]), ((1, 'FaxHandle'),(1, 'FaxConfig'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxSetConfigurationW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Fax.FAX_CONFIGURATIONW_head), use_last_error=True)(("FaxSetConfigurationW", windll["WINFAX"]), ((1, 'FaxHandle'),(1, 'FaxConfig'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxSetConfiguration():
    return win32more.Devices.Fax.FaxSetConfigurationW
def _define_FaxGetLoggingCategoriesA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_LOG_CATEGORYA_head)),POINTER(UInt32), use_last_error=True)(("FaxGetLoggingCategoriesA", windll["WINFAX"]), ((1, 'FaxHandle'),(1, 'Categories'),(1, 'NumberCategories'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxGetLoggingCategoriesW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_LOG_CATEGORYW_head)),POINTER(UInt32), use_last_error=True)(("FaxGetLoggingCategoriesW", windll["WINFAX"]), ((1, 'FaxHandle'),(1, 'Categories'),(1, 'NumberCategories'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxGetLoggingCategories():
    return win32more.Devices.Fax.FaxGetLoggingCategoriesW
def _define_FaxSetLoggingCategoriesA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Fax.FAX_LOG_CATEGORYA_head),UInt32, use_last_error=True)(("FaxSetLoggingCategoriesA", windll["WINFAX"]), ((1, 'FaxHandle'),(1, 'Categories'),(1, 'NumberCategories'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxSetLoggingCategoriesW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Fax.FAX_LOG_CATEGORYW_head),UInt32, use_last_error=True)(("FaxSetLoggingCategoriesW", windll["WINFAX"]), ((1, 'FaxHandle'),(1, 'Categories'),(1, 'NumberCategories'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxSetLoggingCategories():
    return win32more.Devices.Fax.FaxSetLoggingCategoriesW
def _define_FaxEnumPortsA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_PORT_INFOA_head)),POINTER(UInt32), use_last_error=True)(("FaxEnumPortsA", windll["WINFAX"]), ((1, 'FaxHandle'),(1, 'PortInfo'),(1, 'PortsReturned'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxEnumPortsW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_PORT_INFOW_head)),POINTER(UInt32), use_last_error=True)(("FaxEnumPortsW", windll["WINFAX"]), ((1, 'FaxHandle'),(1, 'PortInfo'),(1, 'PortsReturned'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxEnumPorts():
    return win32more.Devices.Fax.FaxEnumPortsW
def _define_FaxGetPortA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_PORT_INFOA_head)), use_last_error=True)(("FaxGetPortA", windll["WINFAX"]), ((1, 'FaxPortHandle'),(1, 'PortInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxGetPortW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_PORT_INFOW_head)), use_last_error=True)(("FaxGetPortW", windll["WINFAX"]), ((1, 'FaxPortHandle'),(1, 'PortInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxGetPort():
    return win32more.Devices.Fax.FaxGetPortW
def _define_FaxSetPortA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Fax.FAX_PORT_INFOA_head), use_last_error=True)(("FaxSetPortA", windll["WINFAX"]), ((1, 'FaxPortHandle'),(1, 'PortInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxSetPortW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Fax.FAX_PORT_INFOW_head), use_last_error=True)(("FaxSetPortW", windll["WINFAX"]), ((1, 'FaxPortHandle'),(1, 'PortInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxSetPort():
    return win32more.Devices.Fax.FaxSetPortW
def _define_FaxEnumRoutingMethodsA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_ROUTING_METHODA_head)),POINTER(UInt32), use_last_error=True)(("FaxEnumRoutingMethodsA", windll["WINFAX"]), ((1, 'FaxPortHandle'),(1, 'RoutingMethod'),(1, 'MethodsReturned'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxEnumRoutingMethodsW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_ROUTING_METHODW_head)),POINTER(UInt32), use_last_error=True)(("FaxEnumRoutingMethodsW", windll["WINFAX"]), ((1, 'FaxPortHandle'),(1, 'RoutingMethod'),(1, 'MethodsReturned'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxEnumRoutingMethods():
    return win32more.Devices.Fax.FaxEnumRoutingMethodsW
def _define_FaxEnableRoutingMethodA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,win32more.Foundation.BOOL, use_last_error=True)(("FaxEnableRoutingMethodA", windll["WINFAX"]), ((1, 'FaxPortHandle'),(1, 'RoutingGuid'),(1, 'Enabled'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxEnableRoutingMethodW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,win32more.Foundation.BOOL, use_last_error=True)(("FaxEnableRoutingMethodW", windll["WINFAX"]), ((1, 'FaxPortHandle'),(1, 'RoutingGuid'),(1, 'Enabled'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxEnableRoutingMethod():
    return win32more.Devices.Fax.FaxEnableRoutingMethodW
def _define_FaxEnumGlobalRoutingInfoA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_GLOBAL_ROUTING_INFOA_head)),POINTER(UInt32), use_last_error=True)(("FaxEnumGlobalRoutingInfoA", windll["WINFAX"]), ((1, 'FaxHandle'),(1, 'RoutingInfo'),(1, 'MethodsReturned'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxEnumGlobalRoutingInfoW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_GLOBAL_ROUTING_INFOW_head)),POINTER(UInt32), use_last_error=True)(("FaxEnumGlobalRoutingInfoW", windll["WINFAX"]), ((1, 'FaxHandle'),(1, 'RoutingInfo'),(1, 'MethodsReturned'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxEnumGlobalRoutingInfo():
    return win32more.Devices.Fax.FaxEnumGlobalRoutingInfoW
def _define_FaxSetGlobalRoutingInfoA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Fax.FAX_GLOBAL_ROUTING_INFOA_head), use_last_error=True)(("FaxSetGlobalRoutingInfoA", windll["WINFAX"]), ((1, 'FaxHandle'),(1, 'RoutingInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxSetGlobalRoutingInfoW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Fax.FAX_GLOBAL_ROUTING_INFOW_head), use_last_error=True)(("FaxSetGlobalRoutingInfoW", windll["WINFAX"]), ((1, 'FaxHandle'),(1, 'RoutingInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxSetGlobalRoutingInfo():
    return win32more.Devices.Fax.FaxSetGlobalRoutingInfoW
def _define_FaxGetRoutingInfoA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,POINTER(c_char_p_no),POINTER(UInt32), use_last_error=True)(("FaxGetRoutingInfoA", windll["WINFAX"]), ((1, 'FaxPortHandle'),(1, 'RoutingGuid'),(1, 'RoutingInfoBuffer'),(1, 'RoutingInfoBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxGetRoutingInfoW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,POINTER(c_char_p_no),POINTER(UInt32), use_last_error=True)(("FaxGetRoutingInfoW", windll["WINFAX"]), ((1, 'FaxPortHandle'),(1, 'RoutingGuid'),(1, 'RoutingInfoBuffer'),(1, 'RoutingInfoBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxGetRoutingInfo():
    return win32more.Devices.Fax.FaxGetRoutingInfoW
def _define_FaxSetRoutingInfoA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,c_char_p_no,UInt32, use_last_error=True)(("FaxSetRoutingInfoA", windll["WINFAX"]), ((1, 'FaxPortHandle'),(1, 'RoutingGuid'),(1, 'RoutingInfoBuffer'),(1, 'RoutingInfoBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxSetRoutingInfoW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,c_char_p_no,UInt32, use_last_error=True)(("FaxSetRoutingInfoW", windll["WINFAX"]), ((1, 'FaxPortHandle'),(1, 'RoutingGuid'),(1, 'RoutingInfoBuffer'),(1, 'RoutingInfoBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxSetRoutingInfo():
    return win32more.Devices.Fax.FaxSetRoutingInfoW
def _define_FaxInitializeEventQueue():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,UIntPtr,win32more.Foundation.HWND,UInt32, use_last_error=False)(("FaxInitializeEventQueue", windll["WINFAX"]), ((1, 'FaxHandle'),(1, 'CompletionPort'),(1, 'CompletionKey'),(1, 'hWnd'),(1, 'MessageStart'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxFreeBuffer():
    try:
        return WINFUNCTYPE(Void,c_void_p, use_last_error=False)(("FaxFreeBuffer", windll["WINFAX"]), ((1, 'Buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxStartPrintJobA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,POINTER(win32more.Devices.Fax.FAX_PRINT_INFOA_head),POINTER(UInt32),POINTER(win32more.Devices.Fax.FAX_CONTEXT_INFOA_head), use_last_error=True)(("FaxStartPrintJobA", windll["WINFAX"]), ((1, 'PrinterName'),(1, 'PrintInfo'),(1, 'FaxJobId'),(1, 'FaxContextInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxStartPrintJobW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,POINTER(win32more.Devices.Fax.FAX_PRINT_INFOW_head),POINTER(UInt32),POINTER(win32more.Devices.Fax.FAX_CONTEXT_INFOW_head), use_last_error=True)(("FaxStartPrintJobW", windll["WINFAX"]), ((1, 'PrinterName'),(1, 'PrintInfo'),(1, 'FaxJobId'),(1, 'FaxContextInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxStartPrintJob():
    return win32more.Devices.Fax.FaxStartPrintJobW
def _define_FaxPrintCoverPageA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Fax.FAX_CONTEXT_INFOA_head),POINTER(win32more.Devices.Fax.FAX_COVERPAGE_INFOA_head), use_last_error=True)(("FaxPrintCoverPageA", windll["WINFAX"]), ((1, 'FaxContextInfo'),(1, 'CoverPageInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxPrintCoverPageW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Fax.FAX_CONTEXT_INFOW_head),POINTER(win32more.Devices.Fax.FAX_COVERPAGE_INFOW_head), use_last_error=True)(("FaxPrintCoverPageW", windll["WINFAX"]), ((1, 'FaxContextInfo'),(1, 'CoverPageInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxPrintCoverPage():
    return win32more.Devices.Fax.FaxPrintCoverPageW
def _define_FaxRegisterServiceProviderW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=True)(("FaxRegisterServiceProviderW", windll["WINFAX"]), ((1, 'DeviceProvider'),(1, 'FriendlyName'),(1, 'ImageName'),(1, 'TspName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxUnregisterServiceProviderW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR, use_last_error=False)(("FaxUnregisterServiceProviderW", windll["WINFAX"]), ((1, 'DeviceProvider'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxRegisterRoutingExtensionW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Devices.Fax.PFAX_ROUTING_INSTALLATION_CALLBACKW,c_void_p, use_last_error=True)(("FaxRegisterRoutingExtensionW", windll["WINFAX"]), ((1, 'FaxHandle'),(1, 'ExtensionName'),(1, 'FriendlyName'),(1, 'ImageName'),(1, 'CallBack'),(1, 'Context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxAccessCheck():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32, use_last_error=False)(("FaxAccessCheck", windll["WINFAX"]), ((1, 'FaxHandle'),(1, 'AccessMask'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CanSendToFaxRecipient():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL, use_last_error=False)(("CanSendToFaxRecipient", windll["fxsutility"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_SendToFaxRecipient():
    try:
        return WINFUNCTYPE(UInt32,win32more.Devices.Fax.SendToMode,win32more.Foundation.PWSTR, use_last_error=False)(("SendToFaxRecipient", windll["fxsutility"]), ((1, 'sndMode'),(1, 'lpFileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_StiCreateInstanceW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HINSTANCE,UInt32,POINTER(win32more.Devices.Fax.IStillImageW_head),win32more.System.Com.IUnknown_head, use_last_error=False)(("StiCreateInstanceW", windll["STI"]), ((1, 'hinst'),(1, 'dwVer'),(1, 'ppSti'),(1, 'punkOuter'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "FS_INITIALIZING",
    "FS_DIALING",
    "FS_TRANSMITTING",
    "FS_RECEIVING",
    "FS_COMPLETED",
    "FS_HANDLED",
    "FS_LINE_UNAVAILABLE",
    "FS_BUSY",
    "FS_NO_ANSWER",
    "FS_BAD_ADDRESS",
    "FS_NO_DIAL_TONE",
    "FS_DISCONNECTED",
    "FS_FATAL_ERROR",
    "FS_NOT_FAX_CALL",
    "FS_CALL_DELAYED",
    "FS_CALL_BLACKLISTED",
    "FS_USER_ABORT",
    "FS_ANSWERED",
    "FAXDEVRECEIVE_SIZE",
    "FAXDEVREPORTSTATUS_SIZE",
    "FAX_ERR_START",
    "FAX_ERR_SRV_OUTOFMEMORY",
    "FAX_ERR_GROUP_NOT_FOUND",
    "FAX_ERR_BAD_GROUP_CONFIGURATION",
    "FAX_ERR_GROUP_IN_USE",
    "FAX_ERR_RULE_NOT_FOUND",
    "FAX_ERR_NOT_NTFS",
    "FAX_ERR_DIRECTORY_IN_USE",
    "FAX_ERR_FILE_ACCESS_DENIED",
    "FAX_ERR_MESSAGE_NOT_FOUND",
    "FAX_ERR_DEVICE_NUM_LIMIT_EXCEEDED",
    "FAX_ERR_NOT_SUPPORTED_ON_THIS_SKU",
    "FAX_ERR_VERSION_MISMATCH",
    "FAX_ERR_RECIPIENTS_LIMIT",
    "FAX_ERR_END",
    "FAX_E_SRV_OUTOFMEMORY",
    "FAX_E_GROUP_NOT_FOUND",
    "FAX_E_BAD_GROUP_CONFIGURATION",
    "FAX_E_GROUP_IN_USE",
    "FAX_E_RULE_NOT_FOUND",
    "FAX_E_NOT_NTFS",
    "FAX_E_DIRECTORY_IN_USE",
    "FAX_E_FILE_ACCESS_DENIED",
    "FAX_E_MESSAGE_NOT_FOUND",
    "FAX_E_DEVICE_NUM_LIMIT_EXCEEDED",
    "FAX_E_NOT_SUPPORTED_ON_THIS_SKU",
    "FAX_E_VERSION_MISMATCH",
    "FAX_E_RECIPIENTS_LIMIT",
    "JT_UNKNOWN",
    "JT_SEND",
    "JT_RECEIVE",
    "JT_ROUTING",
    "JT_FAIL_RECEIVE",
    "JS_PENDING",
    "JS_INPROGRESS",
    "JS_DELETING",
    "JS_FAILED",
    "JS_PAUSED",
    "JS_NOLINE",
    "JS_RETRYING",
    "JS_RETRIES_EXCEEDED",
    "FPS_DIALING",
    "FPS_SENDING",
    "FPS_RECEIVING",
    "FPS_COMPLETED",
    "FPS_HANDLED",
    "FPS_UNAVAILABLE",
    "FPS_BUSY",
    "FPS_NO_ANSWER",
    "FPS_BAD_ADDRESS",
    "FPS_NO_DIAL_TONE",
    "FPS_DISCONNECTED",
    "FPS_FATAL_ERROR",
    "FPS_NOT_FAX_CALL",
    "FPS_CALL_DELAYED",
    "FPS_CALL_BLACKLISTED",
    "FPS_INITIALIZING",
    "FPS_OFFLINE",
    "FPS_RINGING",
    "FPS_AVAILABLE",
    "FPS_ABORTING",
    "FPS_ROUTING",
    "FPS_ANSWERED",
    "FPF_RECEIVE",
    "FPF_SEND",
    "FPF_VIRTUAL",
    "FEI_DIALING",
    "FEI_SENDING",
    "FEI_RECEIVING",
    "FEI_COMPLETED",
    "FEI_BUSY",
    "FEI_NO_ANSWER",
    "FEI_BAD_ADDRESS",
    "FEI_NO_DIAL_TONE",
    "FEI_DISCONNECTED",
    "FEI_FATAL_ERROR",
    "FEI_NOT_FAX_CALL",
    "FEI_CALL_DELAYED",
    "FEI_CALL_BLACKLISTED",
    "FEI_RINGING",
    "FEI_ABORTING",
    "FEI_ROUTING",
    "FEI_MODEM_POWERED_ON",
    "FEI_MODEM_POWERED_OFF",
    "FEI_IDLE",
    "FEI_FAXSVC_ENDED",
    "FEI_ANSWERED",
    "FEI_JOB_QUEUED",
    "FEI_DELETED",
    "FEI_INITIALIZING",
    "FEI_LINE_UNAVAILABLE",
    "FEI_HANDLED",
    "FEI_FAXSVC_STARTED",
    "FEI_NEVENTS",
    "FAX_JOB_SUBMIT",
    "FAX_JOB_QUERY",
    "FAX_CONFIG_QUERY",
    "FAX_CONFIG_SET",
    "FAX_PORT_QUERY",
    "FAX_PORT_SET",
    "FAX_JOB_MANAGE",
    "STI_UNICODE",
    "CLSID_Sti",
    "GUID_DeviceArrivedLaunch",
    "GUID_ScanImage",
    "GUID_ScanPrintImage",
    "GUID_ScanFaxImage",
    "GUID_STIUserDefined1",
    "GUID_STIUserDefined2",
    "GUID_STIUserDefined3",
    "STI_VERSION_FLAG_MASK",
    "STI_VERSION_FLAG_UNICODE",
    "STI_VERSION_REAL",
    "STI_VERSION_MIN_ALLOWED",
    "STI_VERSION",
    "STI_MAX_INTERNAL_NAME_LENGTH",
    "STI_GENCAP_NOTIFICATIONS",
    "STI_GENCAP_POLLING_NEEDED",
    "STI_GENCAP_GENERATE_ARRIVALEVENT",
    "STI_GENCAP_AUTO_PORTSELECT",
    "STI_GENCAP_WIA",
    "STI_GENCAP_SUBSET",
    "WIA_INCOMPAT_XP",
    "STI_HW_CONFIG_UNKNOWN",
    "STI_HW_CONFIG_SCSI",
    "STI_HW_CONFIG_USB",
    "STI_HW_CONFIG_SERIAL",
    "STI_HW_CONFIG_PARALLEL",
    "STI_DEVSTATUS_ONLINE_STATE",
    "STI_DEVSTATUS_EVENTS_STATE",
    "STI_ONLINESTATE_OPERATIONAL",
    "STI_ONLINESTATE_PENDING",
    "STI_ONLINESTATE_ERROR",
    "STI_ONLINESTATE_PAUSED",
    "STI_ONLINESTATE_PAPER_JAM",
    "STI_ONLINESTATE_PAPER_PROBLEM",
    "STI_ONLINESTATE_OFFLINE",
    "STI_ONLINESTATE_IO_ACTIVE",
    "STI_ONLINESTATE_BUSY",
    "STI_ONLINESTATE_TRANSFERRING",
    "STI_ONLINESTATE_INITIALIZING",
    "STI_ONLINESTATE_WARMING_UP",
    "STI_ONLINESTATE_USER_INTERVENTION",
    "STI_ONLINESTATE_POWER_SAVE",
    "STI_EVENTHANDLING_ENABLED",
    "STI_EVENTHANDLING_POLLING",
    "STI_EVENTHANDLING_PENDING",
    "STI_DIAGCODE_HWPRESENCE",
    "STI_TRACE_INFORMATION",
    "STI_TRACE_WARNING",
    "STI_TRACE_ERROR",
    "STI_SUBSCRIBE_FLAG_WINDOW",
    "STI_SUBSCRIBE_FLAG_EVENT",
    "MAX_NOTIFICATION_DATA",
    "STI_DEVICE_CREATE_STATUS",
    "STI_DEVICE_CREATE_DATA",
    "STI_DEVICE_CREATE_BOTH",
    "STI_DEVICE_CREATE_MASK",
    "STIEDFL_ALLDEVICES",
    "STIEDFL_ATTACHEDONLY",
    "STI_RAW_RESERVED",
    "STI_OK",
    "STI_ERROR_NO_ERROR",
    "STI_NOTCONNECTED",
    "STI_CHANGENOEFFECT",
    "STIERR_OLD_VERSION",
    "STIERR_BETA_VERSION",
    "STIERR_BADDRIVER",
    "STIERR_DEVICENOTREG",
    "STIERR_OBJECTNOTFOUND",
    "STIERR_INVALID_PARAM",
    "STIERR_NOINTERFACE",
    "STIERR_GENERIC",
    "STIERR_OUTOFMEMORY",
    "STIERR_UNSUPPORTED",
    "STIERR_NOT_INITIALIZED",
    "STIERR_ALREADY_INITIALIZED",
    "STIERR_DEVICE_LOCKED",
    "STIERR_READONLY",
    "STIERR_NOTINITIALIZED",
    "STIERR_NEEDS_LOCK",
    "STIERR_SHARING_VIOLATION",
    "STIERR_HANDLEEXISTS",
    "STIERR_INVALID_DEVICE_NAME",
    "STIERR_INVALID_HW_TYPE",
    "STIERR_NOEVENTS",
    "STIERR_DEVICE_NOTREADY",
    "IS_DIGITAL_CAMERA_VAL",
    "SUPPORTS_MSCPLUS_VAL",
    "DEVPKEY_WIA_DeviceType",
    "DEVPKEY_WIA_USDClassId",
    "STI_USD_GENCAP_NATIVE_PUSHSUPPORT",
    "STI_DEVICE_CREATE_FOR_MONITOR",
    "lDEFAULT_PREFETCH_SIZE",
    "wcharREASSIGN_RECIPIENTS_DELIMITER",
    "FAX_ENUM_LOG_LEVELS",
    "FAXLOG_LEVEL_NONE",
    "FAXLOG_LEVEL_MIN",
    "FAXLOG_LEVEL_MED",
    "FAXLOG_LEVEL_MAX",
    "FAX_ENUM_LOG_CATEGORIES",
    "FAXLOG_CATEGORY_INIT",
    "FAXLOG_CATEGORY_OUTBOUND",
    "FAXLOG_CATEGORY_INBOUND",
    "FAXLOG_CATEGORY_UNKNOWN",
    "FAX_LOG_CATEGORYA",
    "FAX_LOG_CATEGORYW",
    "FAX_TIME",
    "FAX_CONFIGURATIONA",
    "FAX_CONFIGURATIONW",
    "FAX_ENUM_JOB_COMMANDS",
    "JC_UNKNOWN",
    "JC_DELETE",
    "JC_PAUSE",
    "JC_RESUME",
    "FAX_DEVICE_STATUSA",
    "FAX_DEVICE_STATUSW",
    "FAX_JOB_ENTRYA",
    "FAX_JOB_ENTRYW",
    "FAX_PORT_INFOA",
    "FAX_PORT_INFOW",
    "FAX_ROUTING_METHODA",
    "FAX_ROUTING_METHODW",
    "FAX_GLOBAL_ROUTING_INFOA",
    "FAX_GLOBAL_ROUTING_INFOW",
    "FAX_COVERPAGE_INFOA",
    "FAX_COVERPAGE_INFOW",
    "FAX_ENUM_JOB_SEND_ATTRIBUTES",
    "JSA_NOW",
    "JSA_SPECIFIC_TIME",
    "JSA_DISCOUNT_PERIOD",
    "FAX_ENUM_DELIVERY_REPORT_TYPES",
    "DRT_NONE",
    "DRT_EMAIL",
    "DRT_INBOX",
    "FAX_JOB_PARAMA",
    "FAX_JOB_PARAMW",
    "FAX_EVENTA",
    "FAX_EVENTW",
    "FAX_PRINT_INFOA",
    "FAX_PRINT_INFOW",
    "FAX_CONTEXT_INFOA",
    "FAX_CONTEXT_INFOW",
    "PFAXCONNECTFAXSERVERA",
    "PFAXCONNECTFAXSERVERW",
    "PFAXCLOSE",
    "FAX_ENUM_PORT_OPEN_TYPE",
    "PORT_OPEN_QUERY",
    "PORT_OPEN_MODIFY",
    "PFAXOPENPORT",
    "PFAXCOMPLETEJOBPARAMSA",
    "PFAXCOMPLETEJOBPARAMSW",
    "PFAXSENDDOCUMENTA",
    "PFAXSENDDOCUMENTW",
    "PFAX_RECIPIENT_CALLBACKA",
    "PFAX_RECIPIENT_CALLBACKW",
    "PFAXSENDDOCUMENTFORBROADCASTA",
    "PFAXSENDDOCUMENTFORBROADCASTW",
    "PFAXENUMJOBSA",
    "PFAXENUMJOBSW",
    "PFAXGETJOBA",
    "PFAXGETJOBW",
    "PFAXSETJOBA",
    "PFAXSETJOBW",
    "PFAXGETPAGEDATA",
    "PFAXGETDEVICESTATUSA",
    "PFAXGETDEVICESTATUSW",
    "PFAXABORT",
    "PFAXGETCONFIGURATIONA",
    "PFAXGETCONFIGURATIONW",
    "PFAXSETCONFIGURATIONA",
    "PFAXSETCONFIGURATIONW",
    "PFAXGETLOGGINGCATEGORIESA",
    "PFAXGETLOGGINGCATEGORIESW",
    "PFAXSETLOGGINGCATEGORIESA",
    "PFAXSETLOGGINGCATEGORIESW",
    "PFAXENUMPORTSA",
    "PFAXENUMPORTSW",
    "PFAXGETPORTA",
    "PFAXGETPORTW",
    "PFAXSETPORTA",
    "PFAXSETPORTW",
    "PFAXENUMROUTINGMETHODSA",
    "PFAXENUMROUTINGMETHODSW",
    "PFAXENABLEROUTINGMETHODA",
    "PFAXENABLEROUTINGMETHODW",
    "PFAXENUMGLOBALROUTINGINFOA",
    "PFAXENUMGLOBALROUTINGINFOW",
    "PFAXSETGLOBALROUTINGINFOA",
    "PFAXSETGLOBALROUTINGINFOW",
    "PFAXGETROUTINGINFOA",
    "PFAXGETROUTINGINFOW",
    "PFAXSETROUTINGINFOA",
    "PFAXSETROUTINGINFOW",
    "PFAXINITIALIZEEVENTQUEUE",
    "PFAXFREEBUFFER",
    "PFAXSTARTPRINTJOBA",
    "PFAXSTARTPRINTJOBW",
    "PFAXPRINTCOVERPAGEA",
    "PFAXPRINTCOVERPAGEW",
    "PFAXREGISTERSERVICEPROVIDERW",
    "PFAXUNREGISTERSERVICEPROVIDERW",
    "PFAX_ROUTING_INSTALLATION_CALLBACKW",
    "PFAXREGISTERROUTINGEXTENSIONW",
    "PFAXACCESSCHECK",
    "FAX_SEND",
    "FAX_RECEIVE",
    "FAX_DEV_STATUS",
    "PFAX_SERVICE_CALLBACK",
    "PFAX_LINECALLBACK",
    "PFAX_SEND_CALLBACK",
    "PFAXDEVINITIALIZE",
    "PFAXDEVVIRTUALDEVICECREATION",
    "PFAXDEVSTARTJOB",
    "PFAXDEVENDJOB",
    "PFAXDEVSEND",
    "PFAXDEVRECEIVE",
    "PFAXDEVREPORTSTATUS",
    "PFAXDEVABORTOPERATION",
    "PFAXDEVCONFIGURE",
    "PFAXDEVSHUTDOWN",
    "FaxServer",
    "FaxDeviceProviders",
    "FaxDevices",
    "FaxInboundRouting",
    "FaxFolders",
    "FaxLoggingOptions",
    "FaxActivity",
    "FaxOutboundRouting",
    "FaxReceiptOptions",
    "FaxSecurity",
    "FaxDocument",
    "FaxSender",
    "FaxRecipients",
    "FaxIncomingArchive",
    "FaxIncomingQueue",
    "FaxOutgoingArchive",
    "FaxOutgoingQueue",
    "FaxIncomingMessageIterator",
    "FaxIncomingMessage",
    "FaxOutgoingJobs",
    "FaxOutgoingJob",
    "FaxOutgoingMessageIterator",
    "FaxOutgoingMessage",
    "FaxIncomingJobs",
    "FaxIncomingJob",
    "FaxDeviceProvider",
    "FaxDevice",
    "FaxActivityLogging",
    "FaxEventLogging",
    "FaxOutboundRoutingGroups",
    "FaxOutboundRoutingGroup",
    "FaxDeviceIds",
    "FaxOutboundRoutingRules",
    "FaxOutboundRoutingRule",
    "FaxInboundRoutingExtensions",
    "FaxInboundRoutingExtension",
    "FaxInboundRoutingMethods",
    "FaxInboundRoutingMethod",
    "FaxJobStatus",
    "FaxRecipient",
    "FaxConfiguration",
    "FaxAccountSet",
    "FaxAccounts",
    "FaxAccount",
    "FaxAccountFolders",
    "FaxAccountIncomingQueue",
    "FaxAccountOutgoingQueue",
    "FaxAccountIncomingArchive",
    "FaxAccountOutgoingArchive",
    "FaxSecurity2",
    "FAX_JOB_STATUS_ENUM",
    "FAX_JOB_STATUS_ENUM_fjsPENDING",
    "FAX_JOB_STATUS_ENUM_fjsINPROGRESS",
    "FAX_JOB_STATUS_ENUM_fjsFAILED",
    "FAX_JOB_STATUS_ENUM_fjsPAUSED",
    "FAX_JOB_STATUS_ENUM_fjsNOLINE",
    "FAX_JOB_STATUS_ENUM_fjsRETRYING",
    "FAX_JOB_STATUS_ENUM_fjsRETRIES_EXCEEDED",
    "FAX_JOB_STATUS_ENUM_fjsCOMPLETED",
    "FAX_JOB_STATUS_ENUM_fjsCANCELED",
    "FAX_JOB_STATUS_ENUM_fjsCANCELING",
    "FAX_JOB_STATUS_ENUM_fjsROUTING",
    "FAX_JOB_EXTENDED_STATUS_ENUM",
    "FAX_JOB_EXTENDED_STATUS_ENUM_fjesNONE",
    "FAX_JOB_EXTENDED_STATUS_ENUM_fjesDISCONNECTED",
    "FAX_JOB_EXTENDED_STATUS_ENUM_fjesINITIALIZING",
    "FAX_JOB_EXTENDED_STATUS_ENUM_fjesDIALING",
    "FAX_JOB_EXTENDED_STATUS_ENUM_fjesTRANSMITTING",
    "FAX_JOB_EXTENDED_STATUS_ENUM_fjesANSWERED",
    "FAX_JOB_EXTENDED_STATUS_ENUM_fjesRECEIVING",
    "FAX_JOB_EXTENDED_STATUS_ENUM_fjesLINE_UNAVAILABLE",
    "FAX_JOB_EXTENDED_STATUS_ENUM_fjesBUSY",
    "FAX_JOB_EXTENDED_STATUS_ENUM_fjesNO_ANSWER",
    "FAX_JOB_EXTENDED_STATUS_ENUM_fjesBAD_ADDRESS",
    "FAX_JOB_EXTENDED_STATUS_ENUM_fjesNO_DIAL_TONE",
    "FAX_JOB_EXTENDED_STATUS_ENUM_fjesFATAL_ERROR",
    "FAX_JOB_EXTENDED_STATUS_ENUM_fjesCALL_DELAYED",
    "FAX_JOB_EXTENDED_STATUS_ENUM_fjesCALL_BLACKLISTED",
    "FAX_JOB_EXTENDED_STATUS_ENUM_fjesNOT_FAX_CALL",
    "FAX_JOB_EXTENDED_STATUS_ENUM_fjesPARTIALLY_RECEIVED",
    "FAX_JOB_EXTENDED_STATUS_ENUM_fjesHANDLED",
    "FAX_JOB_EXTENDED_STATUS_ENUM_fjesCALL_COMPLETED",
    "FAX_JOB_EXTENDED_STATUS_ENUM_fjesCALL_ABORTED",
    "FAX_JOB_EXTENDED_STATUS_ENUM_fjesPROPRIETARY",
    "FAX_JOB_OPERATIONS_ENUM",
    "FAX_JOB_OPERATIONS_ENUM_fjoVIEW",
    "FAX_JOB_OPERATIONS_ENUM_fjoPAUSE",
    "FAX_JOB_OPERATIONS_ENUM_fjoRESUME",
    "FAX_JOB_OPERATIONS_ENUM_fjoRESTART",
    "FAX_JOB_OPERATIONS_ENUM_fjoDELETE",
    "FAX_JOB_OPERATIONS_ENUM_fjoRECIPIENT_INFO",
    "FAX_JOB_OPERATIONS_ENUM_fjoSENDER_INFO",
    "FAX_JOB_TYPE_ENUM",
    "FAX_JOB_TYPE_ENUM_fjtSEND",
    "FAX_JOB_TYPE_ENUM_fjtRECEIVE",
    "FAX_JOB_TYPE_ENUM_fjtROUTING",
    "IFaxJobStatus",
    "FAX_SERVER_EVENTS_TYPE_ENUM",
    "FAX_SERVER_EVENTS_TYPE_ENUM_fsetNONE",
    "FAX_SERVER_EVENTS_TYPE_ENUM_fsetIN_QUEUE",
    "FAX_SERVER_EVENTS_TYPE_ENUM_fsetOUT_QUEUE",
    "FAX_SERVER_EVENTS_TYPE_ENUM_fsetCONFIG",
    "FAX_SERVER_EVENTS_TYPE_ENUM_fsetACTIVITY",
    "FAX_SERVER_EVENTS_TYPE_ENUM_fsetQUEUE_STATE",
    "FAX_SERVER_EVENTS_TYPE_ENUM_fsetIN_ARCHIVE",
    "FAX_SERVER_EVENTS_TYPE_ENUM_fsetOUT_ARCHIVE",
    "FAX_SERVER_EVENTS_TYPE_ENUM_fsetFXSSVC_ENDED",
    "FAX_SERVER_EVENTS_TYPE_ENUM_fsetDEVICE_STATUS",
    "FAX_SERVER_EVENTS_TYPE_ENUM_fsetINCOMING_CALL",
    "FAX_SERVER_APIVERSION_ENUM",
    "fsAPI_VERSION_0",
    "fsAPI_VERSION_1",
    "fsAPI_VERSION_2",
    "fsAPI_VERSION_3",
    "IFaxServer",
    "IFaxDeviceProviders",
    "IFaxDevices",
    "IFaxInboundRouting",
    "IFaxFolders",
    "IFaxLoggingOptions",
    "IFaxActivity",
    "IFaxOutboundRouting",
    "FAX_SMTP_AUTHENTICATION_TYPE_ENUM",
    "FAX_SMTP_AUTHENTICATION_TYPE_ENUM_fsatANONYMOUS",
    "FAX_SMTP_AUTHENTICATION_TYPE_ENUM_fsatBASIC",
    "FAX_SMTP_AUTHENTICATION_TYPE_ENUM_fsatNTLM",
    "FAX_RECEIPT_TYPE_ENUM",
    "FAX_RECEIPT_TYPE_ENUM_frtNONE",
    "FAX_RECEIPT_TYPE_ENUM_frtMAIL",
    "FAX_RECEIPT_TYPE_ENUM_frtMSGBOX",
    "IFaxReceiptOptions",
    "FAX_ACCESS_RIGHTS_ENUM",
    "farSUBMIT_LOW",
    "farSUBMIT_NORMAL",
    "farSUBMIT_HIGH",
    "farQUERY_JOBS",
    "farMANAGE_JOBS",
    "farQUERY_CONFIG",
    "farMANAGE_CONFIG",
    "farQUERY_IN_ARCHIVE",
    "farMANAGE_IN_ARCHIVE",
    "farQUERY_OUT_ARCHIVE",
    "farMANAGE_OUT_ARCHIVE",
    "IFaxSecurity",
    "FAX_PRIORITY_TYPE_ENUM",
    "FAX_PRIORITY_TYPE_ENUM_fptLOW",
    "FAX_PRIORITY_TYPE_ENUM_fptNORMAL",
    "FAX_PRIORITY_TYPE_ENUM_fptHIGH",
    "FAX_COVERPAGE_TYPE_ENUM",
    "FAX_COVERPAGE_TYPE_ENUM_fcptNONE",
    "FAX_COVERPAGE_TYPE_ENUM_fcptLOCAL",
    "FAX_COVERPAGE_TYPE_ENUM_fcptSERVER",
    "FAX_SCHEDULE_TYPE_ENUM",
    "FAX_SCHEDULE_TYPE_ENUM_fstNOW",
    "FAX_SCHEDULE_TYPE_ENUM_fstSPECIFIC_TIME",
    "FAX_SCHEDULE_TYPE_ENUM_fstDISCOUNT_PERIOD",
    "IFaxDocument",
    "IFaxSender",
    "IFaxRecipient",
    "IFaxRecipients",
    "IFaxIncomingArchive",
    "IFaxIncomingQueue",
    "IFaxOutgoingArchive",
    "IFaxOutgoingQueue",
    "IFaxIncomingMessageIterator",
    "IFaxIncomingMessage",
    "IFaxOutgoingJobs",
    "IFaxOutgoingJob",
    "IFaxOutgoingMessageIterator",
    "IFaxOutgoingMessage",
    "IFaxIncomingJobs",
    "IFaxIncomingJob",
    "FAX_PROVIDER_STATUS_ENUM",
    "FAX_PROVIDER_STATUS_ENUM_fpsSUCCESS",
    "FAX_PROVIDER_STATUS_ENUM_fpsSERVER_ERROR",
    "FAX_PROVIDER_STATUS_ENUM_fpsBAD_GUID",
    "FAX_PROVIDER_STATUS_ENUM_fpsBAD_VERSION",
    "FAX_PROVIDER_STATUS_ENUM_fpsCANT_LOAD",
    "FAX_PROVIDER_STATUS_ENUM_fpsCANT_LINK",
    "FAX_PROVIDER_STATUS_ENUM_fpsCANT_INIT",
    "IFaxDeviceProvider",
    "FAX_DEVICE_RECEIVE_MODE_ENUM",
    "fdrmNO_ANSWER",
    "fdrmAUTO_ANSWER",
    "fdrmMANUAL_ANSWER",
    "IFaxDevice",
    "IFaxActivityLogging",
    "FAX_LOG_LEVEL_ENUM",
    "FAX_LOG_LEVEL_ENUM_fllNONE",
    "FAX_LOG_LEVEL_ENUM_fllMIN",
    "FAX_LOG_LEVEL_ENUM_fllMED",
    "FAX_LOG_LEVEL_ENUM_fllMAX",
    "IFaxEventLogging",
    "IFaxOutboundRoutingGroups",
    "FAX_GROUP_STATUS_ENUM",
    "FAX_GROUP_STATUS_ENUM_fgsALL_DEV_VALID",
    "FAX_GROUP_STATUS_ENUM_fgsEMPTY",
    "FAX_GROUP_STATUS_ENUM_fgsALL_DEV_NOT_VALID",
    "FAX_GROUP_STATUS_ENUM_fgsSOME_DEV_NOT_VALID",
    "IFaxOutboundRoutingGroup",
    "IFaxDeviceIds",
    "IFaxOutboundRoutingRules",
    "FAX_RULE_STATUS_ENUM",
    "FAX_RULE_STATUS_ENUM_frsVALID",
    "FAX_RULE_STATUS_ENUM_frsEMPTY_GROUP",
    "FAX_RULE_STATUS_ENUM_frsALL_GROUP_DEV_NOT_VALID",
    "FAX_RULE_STATUS_ENUM_frsSOME_GROUP_DEV_NOT_VALID",
    "FAX_RULE_STATUS_ENUM_frsBAD_DEVICE",
    "IFaxOutboundRoutingRule",
    "IFaxInboundRoutingExtensions",
    "IFaxInboundRoutingExtension",
    "IFaxInboundRoutingMethods",
    "IFaxInboundRoutingMethod",
    "IFaxDocument2",
    "IFaxConfiguration",
    "IFaxServer2",
    "IFaxAccountSet",
    "IFaxAccounts",
    "FAX_ACCOUNT_EVENTS_TYPE_ENUM",
    "FAX_ACCOUNT_EVENTS_TYPE_ENUM_faetNONE",
    "FAX_ACCOUNT_EVENTS_TYPE_ENUM_faetIN_QUEUE",
    "FAX_ACCOUNT_EVENTS_TYPE_ENUM_faetOUT_QUEUE",
    "FAX_ACCOUNT_EVENTS_TYPE_ENUM_faetIN_ARCHIVE",
    "FAX_ACCOUNT_EVENTS_TYPE_ENUM_faetOUT_ARCHIVE",
    "FAX_ACCOUNT_EVENTS_TYPE_ENUM_faetFXSSVC_ENDED",
    "IFaxAccount",
    "IFaxOutgoingJob2",
    "IFaxAccountFolders",
    "IFaxAccountIncomingQueue",
    "IFaxAccountOutgoingQueue",
    "IFaxOutgoingMessage2",
    "IFaxAccountIncomingArchive",
    "IFaxAccountOutgoingArchive",
    "FAX_ACCESS_RIGHTS_ENUM_2",
    "far2SUBMIT_LOW",
    "far2SUBMIT_NORMAL",
    "far2SUBMIT_HIGH",
    "far2QUERY_OUT_JOBS",
    "far2MANAGE_OUT_JOBS",
    "far2QUERY_CONFIG",
    "far2MANAGE_CONFIG",
    "far2QUERY_ARCHIVES",
    "far2MANAGE_ARCHIVES",
    "far2MANAGE_RECEIVE_FOLDER",
    "IFaxSecurity2",
    "IFaxIncomingMessage2",
    "FAX_ROUTING_RULE_CODE_ENUM",
    "frrcANY_CODE",
    "IFaxServerNotify",
    "_IFaxServerNotify2",
    "IFaxServerNotify2",
    "_IFaxAccountNotify",
    "IFaxAccountNotify",
    "PFAXROUTEADDFILE",
    "PFAXROUTEDELETEFILE",
    "PFAXROUTEGETFILE",
    "PFAXROUTEENUMFILE",
    "PFAXROUTEENUMFILES",
    "PFAXROUTEMODIFYROUTINGDATA",
    "FAX_ROUTE_CALLBACKROUTINES",
    "FAX_ROUTE",
    "FAXROUTE_ENABLE",
    "QUERY_STATUS",
    "STATUS_DISABLE",
    "STATUS_ENABLE",
    "PFAXROUTEINITIALIZE",
    "PFAXROUTEMETHOD",
    "PFAXROUTEDEVICEENABLE",
    "PFAXROUTEDEVICECHANGENOTIFICATION",
    "PFAXROUTEGETROUTINGINFO",
    "PFAXROUTESETROUTINGINFO",
    "FAX_ENUM_DEVICE_ID_SOURCE",
    "DEV_ID_SRC_FAX",
    "DEV_ID_SRC_TAPI",
    "PFAX_EXT_GET_DATA",
    "PFAX_EXT_SET_DATA",
    "PFAX_EXT_CONFIG_CHANGE",
    "PFAX_EXT_REGISTER_FOR_EVENTS",
    "PFAX_EXT_UNREGISTER_FOR_EVENTS",
    "PFAX_EXT_FREE_BUFFER",
    "PFAX_EXT_INITIALIZE_CONFIG",
    "SendToMode",
    "SEND_TO_FAX_RECIPIENT_ATTACHMENT",
    "STI_DEVICE_MJ_TYPE",
    "STI_DEVICE_MJ_TYPE_StiDeviceTypeDefault",
    "STI_DEVICE_MJ_TYPE_StiDeviceTypeScanner",
    "STI_DEVICE_MJ_TYPE_StiDeviceTypeDigitalCamera",
    "STI_DEVICE_MJ_TYPE_StiDeviceTypeStreamingVideo",
    "STI_DEV_CAPS",
    "STI_DEVICE_INFORMATIONW",
    "STI_WIA_DEVICE_INFORMATIONW",
    "STI_DEVICE_STATUS",
    "_ERROR_INFOW",
    "STI_DIAG",
    "STISUBSCRIBE",
    "STINOTIFY",
    "IStiDeviceW",
    "IStillImageW",
    "IStiDevice",
    "STI_USD_CAPS",
    "IStiDeviceControl",
    "IStiUSD",
    "FaxConnectFaxServerA",
    "FaxConnectFaxServerW",
    "FaxConnectFaxServer",
    "FaxClose",
    "FaxOpenPort",
    "FaxCompleteJobParamsA",
    "FaxCompleteJobParamsW",
    "FaxCompleteJobParams",
    "FaxSendDocumentA",
    "FaxSendDocumentW",
    "FaxSendDocument",
    "FaxSendDocumentForBroadcastA",
    "FaxSendDocumentForBroadcastW",
    "FaxSendDocumentForBroadcast",
    "FaxEnumJobsA",
    "FaxEnumJobsW",
    "FaxEnumJobs",
    "FaxGetJobA",
    "FaxGetJobW",
    "FaxGetJob",
    "FaxSetJobA",
    "FaxSetJobW",
    "FaxSetJob",
    "FaxGetPageData",
    "FaxGetDeviceStatusA",
    "FaxGetDeviceStatusW",
    "FaxGetDeviceStatus",
    "FaxAbort",
    "FaxGetConfigurationA",
    "FaxGetConfigurationW",
    "FaxGetConfiguration",
    "FaxSetConfigurationA",
    "FaxSetConfigurationW",
    "FaxSetConfiguration",
    "FaxGetLoggingCategoriesA",
    "FaxGetLoggingCategoriesW",
    "FaxGetLoggingCategories",
    "FaxSetLoggingCategoriesA",
    "FaxSetLoggingCategoriesW",
    "FaxSetLoggingCategories",
    "FaxEnumPortsA",
    "FaxEnumPortsW",
    "FaxEnumPorts",
    "FaxGetPortA",
    "FaxGetPortW",
    "FaxGetPort",
    "FaxSetPortA",
    "FaxSetPortW",
    "FaxSetPort",
    "FaxEnumRoutingMethodsA",
    "FaxEnumRoutingMethodsW",
    "FaxEnumRoutingMethods",
    "FaxEnableRoutingMethodA",
    "FaxEnableRoutingMethodW",
    "FaxEnableRoutingMethod",
    "FaxEnumGlobalRoutingInfoA",
    "FaxEnumGlobalRoutingInfoW",
    "FaxEnumGlobalRoutingInfo",
    "FaxSetGlobalRoutingInfoA",
    "FaxSetGlobalRoutingInfoW",
    "FaxSetGlobalRoutingInfo",
    "FaxGetRoutingInfoA",
    "FaxGetRoutingInfoW",
    "FaxGetRoutingInfo",
    "FaxSetRoutingInfoA",
    "FaxSetRoutingInfoW",
    "FaxSetRoutingInfo",
    "FaxInitializeEventQueue",
    "FaxFreeBuffer",
    "FaxStartPrintJobA",
    "FaxStartPrintJobW",
    "FaxStartPrintJob",
    "FaxPrintCoverPageA",
    "FaxPrintCoverPageW",
    "FaxPrintCoverPage",
    "FaxRegisterServiceProviderW",
    "FaxUnregisterServiceProviderW",
    "FaxRegisterRoutingExtensionW",
    "FaxAccessCheck",
    "CanSendToFaxRecipient",
    "SendToFaxRecipient",
    "StiCreateInstanceW",
]
