from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Devices.Fax
import win32more.Devices.Properties
import win32more.Foundation
import win32more.Graphics.Gdi
import win32more.System.Com
import win32more.System.IO
import win32more.System.Registry
import win32more.UI.Controls
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
def _define__ERROR_INFOW_head():
    class _ERROR_INFOW(Structure):
        pass
    return _ERROR_INFOW
def _define__ERROR_INFOW():
    _ERROR_INFOW = win32more.Devices.Fax._ERROR_INFOW_head
    _ERROR_INFOW._fields_ = [
        ('dwSize', UInt32),
        ('dwGenericError', UInt32),
        ('dwVendorError', UInt32),
        ('szExtendedErrorText', Char * 255),
    ]
    return _ERROR_INFOW
prv_DEFAULT_PREFETCH_SIZE = 100
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
MS_FAXROUTE_PRINTING_GUID = '{aec1b37c-9af2-11d0-abf7-00c04fd91a4e}'
MS_FAXROUTE_FOLDER_GUID = '{92041a90-9af2-11d0-abf7-00c04fd91a4e}'
MS_FAXROUTE_EMAIL_GUID = '{6bbf7bfe-9af2-11d0-abf7-00c04fd91a4e}'
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
CF_MSFAXSRV_DEVICE_ID = 'FAXSRV_DeviceID'
CF_MSFAXSRV_FSP_GUID = 'FAXSRV_FSPGuid'
CF_MSFAXSRV_SERVER_NAME = 'FAXSRV_ServerName'
CF_MSFAXSRV_ROUTEEXT_NAME = 'FAXSRV_RoutingExtName'
CF_MSFAXSRV_ROUTING_METHOD_GUID = 'FAXSRV_RoutingMethodGuid'
STI_UNICODE = 1
def _define_CLSID_Sti():
    return Guid('b323f8e0-2e68-11d0-90-ea-00-aa-00-60-f8-6c')
def _define_GUID_DeviceArrivedLaunch():
    return Guid('740d9ee6-70f1-11d1-ad-10-00-a0-24-38-ad-48')
def _define_GUID_ScanImage():
    return Guid('a6c5a715-8c6e-11d2-97-7a-00-00-f8-7a-92-6f')
def _define_GUID_ScanPrintImage():
    return Guid('b441f425-8c6e-11d2-97-7a-00-00-f8-7a-92-6f')
def _define_GUID_ScanFaxImage():
    return Guid('c00eb793-8c6e-11d2-97-7a-00-00-f8-7a-92-6f')
def _define_GUID_STIUserDefined1():
    return Guid('c00eb795-8c6e-11d2-97-7a-00-00-f8-7a-92-6f')
def _define_GUID_STIUserDefined2():
    return Guid('c77ae9c5-8c6e-11d2-97-7a-00-00-f8-7a-92-6f')
def _define_GUID_STIUserDefined3():
    return Guid('c77ae9c6-8c6e-11d2-97-7a-00-00-f8-7a-92-6f')
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
STI_ADD_DEVICE_BROADCAST_ACTION = 'Arrival'
STI_REMOVE_DEVICE_BROADCAST_ACTION = 'Removal'
STI_ADD_DEVICE_BROADCAST_STRING = 'STI\\'
STI_REMOVE_DEVICE_BROADCAST_STRING = 'STI\\'
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
REGSTR_VAL_TYPE_W = 'Type'
REGSTR_VAL_VENDOR_NAME_W = 'Vendor'
REGSTR_VAL_DEVICETYPE_W = 'DeviceType'
REGSTR_VAL_DEVICESUBTYPE_W = 'DeviceSubType'
REGSTR_VAL_DEV_NAME_W = 'DeviceName'
REGSTR_VAL_DRIVER_DESC_W = 'DriverDesc'
REGSTR_VAL_FRIENDLY_NAME_W = 'FriendlyName'
REGSTR_VAL_GENERIC_CAPS_W = 'Capabilities'
REGSTR_VAL_HARDWARE_W = 'HardwareConfig'
REGSTR_VAL_HARDWARE = 'HardwareConfig'
REGSTR_VAL_DEVICE_NAME_W = 'DriverDesc'
REGSTR_VAL_DATA_W = 'DeviceData'
REGSTR_VAL_GUID_W = 'GUID'
REGSTR_VAL_GUID = 'GUID'
REGSTR_VAL_LAUNCH_APPS_W = 'LaunchApplications'
REGSTR_VAL_LAUNCH_APPS = 'LaunchApplications'
REGSTR_VAL_LAUNCHABLE_W = 'Launchable'
REGSTR_VAL_LAUNCHABLE = 'Launchable'
REGSTR_VAL_SHUTDOWNDELAY_W = 'ShutdownIfUnusedDelay'
REGSTR_VAL_SHUTDOWNDELAY = 'ShutdownIfUnusedDelay'
IS_DIGITAL_CAMERA_STR = 'IsDigitalCamera'
IS_DIGITAL_CAMERA_VAL = 1
SUPPORTS_MSCPLUS_STR = 'SupportsMSCPlus'
SUPPORTS_MSCPLUS_VAL = 1
STI_DEVICE_VALUE_TWAIN_NAME = 'TwainDS'
STI_DEVICE_VALUE_ISIS_NAME = 'ISISDriverName'
STI_DEVICE_VALUE_ICM_PROFILE = 'ICMProfile'
STI_DEVICE_VALUE_DEFAULT_LAUNCHAPP = 'DefaultLaunchApp'
STI_DEVICE_VALUE_TIMEOUT = 'PollTimeout'
STI_DEVICE_VALUE_DISABLE_NOTIFICATIONS = 'DisableNotifications'
REGSTR_VAL_BAUDRATE = 'BaudRate'
STI_DEVICE_VALUE_TWAIN_NAME_A = 'TwainDS'
STI_DEVICE_VALUE_ISIS_NAME_A = 'ISISDriverName'
STI_DEVICE_VALUE_ICM_PROFILE_A = 'ICMProfile'
STI_DEVICE_VALUE_DEFAULT_LAUNCHAPP_A = 'DefaultLaunchApp'
STI_DEVICE_VALUE_TIMEOUT_A = 'PollTimeout'
STI_DEVICE_VALUE_DISABLE_NOTIFICATIONS_A = 'DisableNotifications'
REGSTR_VAL_BAUDRATE_A = 'BaudRate'
def _define_DEVPKEY_WIA_DeviceType():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('6bdd1fc6-810f-11d0-be-c7-08-00-2b-e2-09-2f'), pid=2)
def _define_DEVPKEY_WIA_USDClassId():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('6bdd1fc6-810f-11d0-be-c7-08-00-2b-e2-09-2f'), pid=3)
STI_USD_GENCAP_NATIVE_PUSHSUPPORT = 1
STI_DEVICE_CREATE_FOR_MONITOR = 16777216
lDEFAULT_PREFETCH_SIZE = 100
wcharREASSIGN_RECIPIENTS_DELIMITER = 59
def _define_FaxConnectFaxServerA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,POINTER(win32more.Foundation.HANDLE))(('FaxConnectFaxServerA', windll['WINFAX.dll']), ((1, 'MachineName'),(1, 'FaxHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxConnectFaxServerW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.HANDLE))(('FaxConnectFaxServerW', windll['WINFAX.dll']), ((1, 'MachineName'),(1, 'FaxHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxClose():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE)(('FaxClose', windll['WINFAX.dll']), ((1, 'FaxHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxOpenPort():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,UInt32,POINTER(win32more.Foundation.HANDLE))(('FaxOpenPort', windll['WINFAX.dll']), ((1, 'FaxHandle'),(1, 'DeviceId'),(1, 'Flags'),(1, 'FaxPortHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxCompleteJobParamsA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(POINTER(win32more.Devices.Fax.FAX_JOB_PARAMA_head)),POINTER(POINTER(win32more.Devices.Fax.FAX_COVERPAGE_INFOA_head)))(('FaxCompleteJobParamsA', windll['WINFAX.dll']), ((1, 'JobParams'),(1, 'CoverpageInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxCompleteJobParamsW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(POINTER(win32more.Devices.Fax.FAX_JOB_PARAMW_head)),POINTER(POINTER(win32more.Devices.Fax.FAX_COVERPAGE_INFOW_head)))(('FaxCompleteJobParamsW', windll['WINFAX.dll']), ((1, 'JobParams'),(1, 'CoverpageInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxSendDocumentA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,POINTER(win32more.Devices.Fax.FAX_JOB_PARAMA_head),POINTER(win32more.Devices.Fax.FAX_COVERPAGE_INFOA_head),POINTER(UInt32))(('FaxSendDocumentA', windll['WINFAX.dll']), ((1, 'FaxHandle'),(1, 'FileName'),(1, 'JobParams'),(1, 'CoverpageInfo'),(1, 'FaxJobId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxSendDocumentW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,POINTER(win32more.Devices.Fax.FAX_JOB_PARAMW_head),POINTER(win32more.Devices.Fax.FAX_COVERPAGE_INFOW_head),POINTER(UInt32))(('FaxSendDocumentW', windll['WINFAX.dll']), ((1, 'FaxHandle'),(1, 'FileName'),(1, 'JobParams'),(1, 'CoverpageInfo'),(1, 'FaxJobId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxSendDocumentForBroadcastA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,POINTER(UInt32),win32more.Devices.Fax.PFAX_RECIPIENT_CALLBACKA,c_void_p)(('FaxSendDocumentForBroadcastA', windll['WINFAX.dll']), ((1, 'FaxHandle'),(1, 'FileName'),(1, 'FaxJobId'),(1, 'FaxRecipientCallback'),(1, 'Context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxSendDocumentForBroadcastW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,POINTER(UInt32),win32more.Devices.Fax.PFAX_RECIPIENT_CALLBACKW,c_void_p)(('FaxSendDocumentForBroadcastW', windll['WINFAX.dll']), ((1, 'FaxHandle'),(1, 'FileName'),(1, 'FaxJobId'),(1, 'FaxRecipientCallback'),(1, 'Context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxEnumJobsA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_JOB_ENTRYA_head)),POINTER(UInt32))(('FaxEnumJobsA', windll['WINFAX.dll']), ((1, 'FaxHandle'),(1, 'JobEntry'),(1, 'JobsReturned'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxEnumJobsW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_JOB_ENTRYW_head)),POINTER(UInt32))(('FaxEnumJobsW', windll['WINFAX.dll']), ((1, 'FaxHandle'),(1, 'JobEntry'),(1, 'JobsReturned'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxGetJobA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,POINTER(POINTER(win32more.Devices.Fax.FAX_JOB_ENTRYA_head)))(('FaxGetJobA', windll['WINFAX.dll']), ((1, 'FaxHandle'),(1, 'JobId'),(1, 'JobEntry'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxGetJobW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,POINTER(POINTER(win32more.Devices.Fax.FAX_JOB_ENTRYW_head)))(('FaxGetJobW', windll['WINFAX.dll']), ((1, 'FaxHandle'),(1, 'JobId'),(1, 'JobEntry'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxSetJobA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,UInt32,POINTER(win32more.Devices.Fax.FAX_JOB_ENTRYA_head))(('FaxSetJobA', windll['WINFAX.dll']), ((1, 'FaxHandle'),(1, 'JobId'),(1, 'Command'),(1, 'JobEntry'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxSetJobW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,UInt32,POINTER(win32more.Devices.Fax.FAX_JOB_ENTRYW_head))(('FaxSetJobW', windll['WINFAX.dll']), ((1, 'FaxHandle'),(1, 'JobId'),(1, 'Command'),(1, 'JobEntry'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxGetPageData():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,POINTER(c_char_p_no),POINTER(UInt32),POINTER(UInt32),POINTER(UInt32))(('FaxGetPageData', windll['WINFAX.dll']), ((1, 'FaxHandle'),(1, 'JobId'),(1, 'Buffer'),(1, 'BufferSize'),(1, 'ImageWidth'),(1, 'ImageHeight'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxGetDeviceStatusA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_DEVICE_STATUSA_head)))(('FaxGetDeviceStatusA', windll['WINFAX.dll']), ((1, 'FaxPortHandle'),(1, 'DeviceStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxGetDeviceStatusW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_DEVICE_STATUSW_head)))(('FaxGetDeviceStatusW', windll['WINFAX.dll']), ((1, 'FaxPortHandle'),(1, 'DeviceStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxAbort():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32)(('FaxAbort', windll['WINFAX.dll']), ((1, 'FaxHandle'),(1, 'JobId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxGetConfigurationA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_CONFIGURATIONA_head)))(('FaxGetConfigurationA', windll['WINFAX.dll']), ((1, 'FaxHandle'),(1, 'FaxConfig'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxGetConfigurationW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_CONFIGURATIONW_head)))(('FaxGetConfigurationW', windll['WINFAX.dll']), ((1, 'FaxHandle'),(1, 'FaxConfig'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxSetConfigurationA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Fax.FAX_CONFIGURATIONA_head))(('FaxSetConfigurationA', windll['WINFAX.dll']), ((1, 'FaxHandle'),(1, 'FaxConfig'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxSetConfigurationW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Fax.FAX_CONFIGURATIONW_head))(('FaxSetConfigurationW', windll['WINFAX.dll']), ((1, 'FaxHandle'),(1, 'FaxConfig'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxGetLoggingCategoriesA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_LOG_CATEGORYA_head)),POINTER(UInt32))(('FaxGetLoggingCategoriesA', windll['WINFAX.dll']), ((1, 'FaxHandle'),(1, 'Categories'),(1, 'NumberCategories'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxGetLoggingCategoriesW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_LOG_CATEGORYW_head)),POINTER(UInt32))(('FaxGetLoggingCategoriesW', windll['WINFAX.dll']), ((1, 'FaxHandle'),(1, 'Categories'),(1, 'NumberCategories'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxSetLoggingCategoriesA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Fax.FAX_LOG_CATEGORYA_head),UInt32)(('FaxSetLoggingCategoriesA', windll['WINFAX.dll']), ((1, 'FaxHandle'),(1, 'Categories'),(1, 'NumberCategories'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxSetLoggingCategoriesW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Fax.FAX_LOG_CATEGORYW_head),UInt32)(('FaxSetLoggingCategoriesW', windll['WINFAX.dll']), ((1, 'FaxHandle'),(1, 'Categories'),(1, 'NumberCategories'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxEnumPortsA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_PORT_INFOA_head)),POINTER(UInt32))(('FaxEnumPortsA', windll['WINFAX.dll']), ((1, 'FaxHandle'),(1, 'PortInfo'),(1, 'PortsReturned'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxEnumPortsW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_PORT_INFOW_head)),POINTER(UInt32))(('FaxEnumPortsW', windll['WINFAX.dll']), ((1, 'FaxHandle'),(1, 'PortInfo'),(1, 'PortsReturned'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxGetPortA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_PORT_INFOA_head)))(('FaxGetPortA', windll['WINFAX.dll']), ((1, 'FaxPortHandle'),(1, 'PortInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxGetPortW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_PORT_INFOW_head)))(('FaxGetPortW', windll['WINFAX.dll']), ((1, 'FaxPortHandle'),(1, 'PortInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxSetPortA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Fax.FAX_PORT_INFOA_head))(('FaxSetPortA', windll['WINFAX.dll']), ((1, 'FaxPortHandle'),(1, 'PortInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxSetPortW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Fax.FAX_PORT_INFOW_head))(('FaxSetPortW', windll['WINFAX.dll']), ((1, 'FaxPortHandle'),(1, 'PortInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxEnumRoutingMethodsA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_ROUTING_METHODA_head)),POINTER(UInt32))(('FaxEnumRoutingMethodsA', windll['WINFAX.dll']), ((1, 'FaxPortHandle'),(1, 'RoutingMethod'),(1, 'MethodsReturned'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxEnumRoutingMethodsW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_ROUTING_METHODW_head)),POINTER(UInt32))(('FaxEnumRoutingMethodsW', windll['WINFAX.dll']), ((1, 'FaxPortHandle'),(1, 'RoutingMethod'),(1, 'MethodsReturned'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxEnableRoutingMethodA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,win32more.Foundation.BOOL)(('FaxEnableRoutingMethodA', windll['WINFAX.dll']), ((1, 'FaxPortHandle'),(1, 'RoutingGuid'),(1, 'Enabled'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxEnableRoutingMethodW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,win32more.Foundation.BOOL)(('FaxEnableRoutingMethodW', windll['WINFAX.dll']), ((1, 'FaxPortHandle'),(1, 'RoutingGuid'),(1, 'Enabled'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxEnumGlobalRoutingInfoA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_GLOBAL_ROUTING_INFOA_head)),POINTER(UInt32))(('FaxEnumGlobalRoutingInfoA', windll['WINFAX.dll']), ((1, 'FaxHandle'),(1, 'RoutingInfo'),(1, 'MethodsReturned'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxEnumGlobalRoutingInfoW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_GLOBAL_ROUTING_INFOW_head)),POINTER(UInt32))(('FaxEnumGlobalRoutingInfoW', windll['WINFAX.dll']), ((1, 'FaxHandle'),(1, 'RoutingInfo'),(1, 'MethodsReturned'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxSetGlobalRoutingInfoA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Fax.FAX_GLOBAL_ROUTING_INFOA_head))(('FaxSetGlobalRoutingInfoA', windll['WINFAX.dll']), ((1, 'FaxHandle'),(1, 'RoutingInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxSetGlobalRoutingInfoW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Fax.FAX_GLOBAL_ROUTING_INFOW_head))(('FaxSetGlobalRoutingInfoW', windll['WINFAX.dll']), ((1, 'FaxHandle'),(1, 'RoutingInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxGetRoutingInfoA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,POINTER(c_char_p_no),POINTER(UInt32))(('FaxGetRoutingInfoA', windll['WINFAX.dll']), ((1, 'FaxPortHandle'),(1, 'RoutingGuid'),(1, 'RoutingInfoBuffer'),(1, 'RoutingInfoBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxGetRoutingInfoW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,POINTER(c_char_p_no),POINTER(UInt32))(('FaxGetRoutingInfoW', windll['WINFAX.dll']), ((1, 'FaxPortHandle'),(1, 'RoutingGuid'),(1, 'RoutingInfoBuffer'),(1, 'RoutingInfoBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxSetRoutingInfoA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,c_char_p_no,UInt32)(('FaxSetRoutingInfoA', windll['WINFAX.dll']), ((1, 'FaxPortHandle'),(1, 'RoutingGuid'),(1, 'RoutingInfoBuffer'),(1, 'RoutingInfoBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxSetRoutingInfoW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,c_char_p_no,UInt32)(('FaxSetRoutingInfoW', windll['WINFAX.dll']), ((1, 'FaxPortHandle'),(1, 'RoutingGuid'),(1, 'RoutingInfoBuffer'),(1, 'RoutingInfoBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxInitializeEventQueue():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,UIntPtr,win32more.Foundation.HWND,UInt32)(('FaxInitializeEventQueue', windll['WINFAX.dll']), ((1, 'FaxHandle'),(1, 'CompletionPort'),(1, 'CompletionKey'),(1, 'hWnd'),(1, 'MessageStart'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxFreeBuffer():
    try:
        return WINFUNCTYPE(Void,c_void_p)(('FaxFreeBuffer', windll['WINFAX.dll']), ((1, 'Buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxStartPrintJobA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,POINTER(win32more.Devices.Fax.FAX_PRINT_INFOA_head),POINTER(UInt32),POINTER(win32more.Devices.Fax.FAX_CONTEXT_INFOA_head))(('FaxStartPrintJobA', windll['WINFAX.dll']), ((1, 'PrinterName'),(1, 'PrintInfo'),(1, 'FaxJobId'),(1, 'FaxContextInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxStartPrintJobW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,POINTER(win32more.Devices.Fax.FAX_PRINT_INFOW_head),POINTER(UInt32),POINTER(win32more.Devices.Fax.FAX_CONTEXT_INFOW_head))(('FaxStartPrintJobW', windll['WINFAX.dll']), ((1, 'PrinterName'),(1, 'PrintInfo'),(1, 'FaxJobId'),(1, 'FaxContextInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxPrintCoverPageA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Fax.FAX_CONTEXT_INFOA_head),POINTER(win32more.Devices.Fax.FAX_COVERPAGE_INFOA_head))(('FaxPrintCoverPageA', windll['WINFAX.dll']), ((1, 'FaxContextInfo'),(1, 'CoverPageInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxPrintCoverPageW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Fax.FAX_CONTEXT_INFOW_head),POINTER(win32more.Devices.Fax.FAX_COVERPAGE_INFOW_head))(('FaxPrintCoverPageW', windll['WINFAX.dll']), ((1, 'FaxContextInfo'),(1, 'CoverPageInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxRegisterServiceProviderW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('FaxRegisterServiceProviderW', windll['WINFAX.dll']), ((1, 'DeviceProvider'),(1, 'FriendlyName'),(1, 'ImageName'),(1, 'TspName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxUnregisterServiceProviderW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR)(('FaxUnregisterServiceProviderW', windll['WINFAX.dll']), ((1, 'DeviceProvider'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxRegisterRoutingExtensionW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Devices.Fax.PFAX_ROUTING_INSTALLATION_CALLBACKW,c_void_p)(('FaxRegisterRoutingExtensionW', windll['WINFAX.dll']), ((1, 'FaxHandle'),(1, 'ExtensionName'),(1, 'FriendlyName'),(1, 'ImageName'),(1, 'CallBack'),(1, 'Context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaxAccessCheck():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32)(('FaxAccessCheck', windll['WINFAX.dll']), ((1, 'FaxHandle'),(1, 'AccessMask'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CanSendToFaxRecipient():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,)(('CanSendToFaxRecipient', windll['fxsutility.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_SendToFaxRecipient():
    try:
        return WINFUNCTYPE(UInt32,win32more.Devices.Fax.SendToMode,win32more.Foundation.PWSTR)(('SendToFaxRecipient', windll['fxsutility.dll']), ((1, 'sndMode'),(1, 'lpFileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_StiCreateInstanceW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HINSTANCE,UInt32,POINTER(win32more.Devices.Fax.IStillImageW_head),win32more.System.Com.IUnknown_head)(('StiCreateInstanceW', windll['STI.dll']), ((1, 'hinst'),(1, 'dwVer'),(1, 'ppSti'),(1, 'punkOuter'),))
    except (FileNotFoundError, AttributeError):
        return None
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
FAX_ACCOUNT_EVENTS_TYPE_ENUM = Int32
FAX_ACCOUNT_EVENTS_TYPE_ENUM_faetNONE = 0
FAX_ACCOUNT_EVENTS_TYPE_ENUM_faetIN_QUEUE = 1
FAX_ACCOUNT_EVENTS_TYPE_ENUM_faetOUT_QUEUE = 2
FAX_ACCOUNT_EVENTS_TYPE_ENUM_faetIN_ARCHIVE = 4
FAX_ACCOUNT_EVENTS_TYPE_ENUM_faetOUT_ARCHIVE = 8
FAX_ACCOUNT_EVENTS_TYPE_ENUM_faetFXSSVC_ENDED = 16
def _define_FAX_CONFIGURATIONA_head():
    class FAX_CONFIGURATIONA(Structure):
        pass
    return FAX_CONFIGURATIONA
def _define_FAX_CONFIGURATIONA():
    FAX_CONFIGURATIONA = win32more.Devices.Fax.FAX_CONFIGURATIONA_head
    FAX_CONFIGURATIONA._fields_ = [
        ('SizeOfStruct', UInt32),
        ('Retries', UInt32),
        ('RetryDelay', UInt32),
        ('DirtyDays', UInt32),
        ('Branding', win32more.Foundation.BOOL),
        ('UseDeviceTsid', win32more.Foundation.BOOL),
        ('ServerCp', win32more.Foundation.BOOL),
        ('PauseServerQueue', win32more.Foundation.BOOL),
        ('StartCheapTime', win32more.Devices.Fax.FAX_TIME),
        ('StopCheapTime', win32more.Devices.Fax.FAX_TIME),
        ('ArchiveOutgoingFaxes', win32more.Foundation.BOOL),
        ('ArchiveDirectory', win32more.Foundation.PSTR),
        ('Reserved', win32more.Foundation.PSTR),
    ]
    return FAX_CONFIGURATIONA
def _define_FAX_CONFIGURATIONW_head():
    class FAX_CONFIGURATIONW(Structure):
        pass
    return FAX_CONFIGURATIONW
def _define_FAX_CONFIGURATIONW():
    FAX_CONFIGURATIONW = win32more.Devices.Fax.FAX_CONFIGURATIONW_head
    FAX_CONFIGURATIONW._fields_ = [
        ('SizeOfStruct', UInt32),
        ('Retries', UInt32),
        ('RetryDelay', UInt32),
        ('DirtyDays', UInt32),
        ('Branding', win32more.Foundation.BOOL),
        ('UseDeviceTsid', win32more.Foundation.BOOL),
        ('ServerCp', win32more.Foundation.BOOL),
        ('PauseServerQueue', win32more.Foundation.BOOL),
        ('StartCheapTime', win32more.Devices.Fax.FAX_TIME),
        ('StopCheapTime', win32more.Devices.Fax.FAX_TIME),
        ('ArchiveOutgoingFaxes', win32more.Foundation.BOOL),
        ('ArchiveDirectory', win32more.Foundation.PWSTR),
        ('Reserved', win32more.Foundation.PWSTR),
    ]
    return FAX_CONFIGURATIONW
def _define_FAX_CONTEXT_INFOA_head():
    class FAX_CONTEXT_INFOA(Structure):
        pass
    return FAX_CONTEXT_INFOA
def _define_FAX_CONTEXT_INFOA():
    FAX_CONTEXT_INFOA = win32more.Devices.Fax.FAX_CONTEXT_INFOA_head
    FAX_CONTEXT_INFOA._fields_ = [
        ('SizeOfStruct', UInt32),
        ('hDC', win32more.Graphics.Gdi.HDC),
        ('ServerName', win32more.Foundation.CHAR * 16),
    ]
    return FAX_CONTEXT_INFOA
def _define_FAX_CONTEXT_INFOW_head():
    class FAX_CONTEXT_INFOW(Structure):
        pass
    return FAX_CONTEXT_INFOW
def _define_FAX_CONTEXT_INFOW():
    FAX_CONTEXT_INFOW = win32more.Devices.Fax.FAX_CONTEXT_INFOW_head
    FAX_CONTEXT_INFOW._fields_ = [
        ('SizeOfStruct', UInt32),
        ('hDC', win32more.Graphics.Gdi.HDC),
        ('ServerName', Char * 16),
    ]
    return FAX_CONTEXT_INFOW
def _define_FAX_COVERPAGE_INFOA_head():
    class FAX_COVERPAGE_INFOA(Structure):
        pass
    return FAX_COVERPAGE_INFOA
def _define_FAX_COVERPAGE_INFOA():
    FAX_COVERPAGE_INFOA = win32more.Devices.Fax.FAX_COVERPAGE_INFOA_head
    FAX_COVERPAGE_INFOA._fields_ = [
        ('SizeOfStruct', UInt32),
        ('CoverPageName', win32more.Foundation.PSTR),
        ('UseServerCoverPage', win32more.Foundation.BOOL),
        ('RecName', win32more.Foundation.PSTR),
        ('RecFaxNumber', win32more.Foundation.PSTR),
        ('RecCompany', win32more.Foundation.PSTR),
        ('RecStreetAddress', win32more.Foundation.PSTR),
        ('RecCity', win32more.Foundation.PSTR),
        ('RecState', win32more.Foundation.PSTR),
        ('RecZip', win32more.Foundation.PSTR),
        ('RecCountry', win32more.Foundation.PSTR),
        ('RecTitle', win32more.Foundation.PSTR),
        ('RecDepartment', win32more.Foundation.PSTR),
        ('RecOfficeLocation', win32more.Foundation.PSTR),
        ('RecHomePhone', win32more.Foundation.PSTR),
        ('RecOfficePhone', win32more.Foundation.PSTR),
        ('SdrName', win32more.Foundation.PSTR),
        ('SdrFaxNumber', win32more.Foundation.PSTR),
        ('SdrCompany', win32more.Foundation.PSTR),
        ('SdrAddress', win32more.Foundation.PSTR),
        ('SdrTitle', win32more.Foundation.PSTR),
        ('SdrDepartment', win32more.Foundation.PSTR),
        ('SdrOfficeLocation', win32more.Foundation.PSTR),
        ('SdrHomePhone', win32more.Foundation.PSTR),
        ('SdrOfficePhone', win32more.Foundation.PSTR),
        ('Note', win32more.Foundation.PSTR),
        ('Subject', win32more.Foundation.PSTR),
        ('TimeSent', win32more.Foundation.SYSTEMTIME),
        ('PageCount', UInt32),
    ]
    return FAX_COVERPAGE_INFOA
def _define_FAX_COVERPAGE_INFOW_head():
    class FAX_COVERPAGE_INFOW(Structure):
        pass
    return FAX_COVERPAGE_INFOW
def _define_FAX_COVERPAGE_INFOW():
    FAX_COVERPAGE_INFOW = win32more.Devices.Fax.FAX_COVERPAGE_INFOW_head
    FAX_COVERPAGE_INFOW._fields_ = [
        ('SizeOfStruct', UInt32),
        ('CoverPageName', win32more.Foundation.PWSTR),
        ('UseServerCoverPage', win32more.Foundation.BOOL),
        ('RecName', win32more.Foundation.PWSTR),
        ('RecFaxNumber', win32more.Foundation.PWSTR),
        ('RecCompany', win32more.Foundation.PWSTR),
        ('RecStreetAddress', win32more.Foundation.PWSTR),
        ('RecCity', win32more.Foundation.PWSTR),
        ('RecState', win32more.Foundation.PWSTR),
        ('RecZip', win32more.Foundation.PWSTR),
        ('RecCountry', win32more.Foundation.PWSTR),
        ('RecTitle', win32more.Foundation.PWSTR),
        ('RecDepartment', win32more.Foundation.PWSTR),
        ('RecOfficeLocation', win32more.Foundation.PWSTR),
        ('RecHomePhone', win32more.Foundation.PWSTR),
        ('RecOfficePhone', win32more.Foundation.PWSTR),
        ('SdrName', win32more.Foundation.PWSTR),
        ('SdrFaxNumber', win32more.Foundation.PWSTR),
        ('SdrCompany', win32more.Foundation.PWSTR),
        ('SdrAddress', win32more.Foundation.PWSTR),
        ('SdrTitle', win32more.Foundation.PWSTR),
        ('SdrDepartment', win32more.Foundation.PWSTR),
        ('SdrOfficeLocation', win32more.Foundation.PWSTR),
        ('SdrHomePhone', win32more.Foundation.PWSTR),
        ('SdrOfficePhone', win32more.Foundation.PWSTR),
        ('Note', win32more.Foundation.PWSTR),
        ('Subject', win32more.Foundation.PWSTR),
        ('TimeSent', win32more.Foundation.SYSTEMTIME),
        ('PageCount', UInt32),
    ]
    return FAX_COVERPAGE_INFOW
FAX_COVERPAGE_TYPE_ENUM = Int32
FAX_COVERPAGE_TYPE_ENUM_fcptNONE = 0
FAX_COVERPAGE_TYPE_ENUM_fcptLOCAL = 1
FAX_COVERPAGE_TYPE_ENUM_fcptSERVER = 2
def _define_FAX_DEV_STATUS_head():
    class FAX_DEV_STATUS(Structure):
        pass
    return FAX_DEV_STATUS
def _define_FAX_DEV_STATUS():
    FAX_DEV_STATUS = win32more.Devices.Fax.FAX_DEV_STATUS_head
    FAX_DEV_STATUS._fields_ = [
        ('SizeOfStruct', UInt32),
        ('StatusId', UInt32),
        ('StringId', UInt32),
        ('PageCount', UInt32),
        ('CSI', win32more.Foundation.PWSTR),
        ('CallerId', win32more.Foundation.PWSTR),
        ('RoutingInfo', win32more.Foundation.PWSTR),
        ('ErrorCode', UInt32),
        ('Reserved', UInt32 * 3),
    ]
    return FAX_DEV_STATUS
FAX_DEVICE_RECEIVE_MODE_ENUM = Int32
fdrmNO_ANSWER = 0
fdrmAUTO_ANSWER = 1
fdrmMANUAL_ANSWER = 2
def _define_FAX_DEVICE_STATUSA_head():
    class FAX_DEVICE_STATUSA(Structure):
        pass
    return FAX_DEVICE_STATUSA
def _define_FAX_DEVICE_STATUSA():
    FAX_DEVICE_STATUSA = win32more.Devices.Fax.FAX_DEVICE_STATUSA_head
    FAX_DEVICE_STATUSA._fields_ = [
        ('SizeOfStruct', UInt32),
        ('CallerId', win32more.Foundation.PSTR),
        ('Csid', win32more.Foundation.PSTR),
        ('CurrentPage', UInt32),
        ('DeviceId', UInt32),
        ('DeviceName', win32more.Foundation.PSTR),
        ('DocumentName', win32more.Foundation.PSTR),
        ('JobType', UInt32),
        ('PhoneNumber', win32more.Foundation.PSTR),
        ('RoutingString', win32more.Foundation.PSTR),
        ('SenderName', win32more.Foundation.PSTR),
        ('RecipientName', win32more.Foundation.PSTR),
        ('Size', UInt32),
        ('StartTime', win32more.Foundation.FILETIME),
        ('Status', UInt32),
        ('StatusString', win32more.Foundation.PSTR),
        ('SubmittedTime', win32more.Foundation.FILETIME),
        ('TotalPages', UInt32),
        ('Tsid', win32more.Foundation.PSTR),
        ('UserName', win32more.Foundation.PSTR),
    ]
    return FAX_DEVICE_STATUSA
def _define_FAX_DEVICE_STATUSW_head():
    class FAX_DEVICE_STATUSW(Structure):
        pass
    return FAX_DEVICE_STATUSW
def _define_FAX_DEVICE_STATUSW():
    FAX_DEVICE_STATUSW = win32more.Devices.Fax.FAX_DEVICE_STATUSW_head
    FAX_DEVICE_STATUSW._fields_ = [
        ('SizeOfStruct', UInt32),
        ('CallerId', win32more.Foundation.PWSTR),
        ('Csid', win32more.Foundation.PWSTR),
        ('CurrentPage', UInt32),
        ('DeviceId', UInt32),
        ('DeviceName', win32more.Foundation.PWSTR),
        ('DocumentName', win32more.Foundation.PWSTR),
        ('JobType', UInt32),
        ('PhoneNumber', win32more.Foundation.PWSTR),
        ('RoutingString', win32more.Foundation.PWSTR),
        ('SenderName', win32more.Foundation.PWSTR),
        ('RecipientName', win32more.Foundation.PWSTR),
        ('Size', UInt32),
        ('StartTime', win32more.Foundation.FILETIME),
        ('Status', UInt32),
        ('StatusString', win32more.Foundation.PWSTR),
        ('SubmittedTime', win32more.Foundation.FILETIME),
        ('TotalPages', UInt32),
        ('Tsid', win32more.Foundation.PWSTR),
        ('UserName', win32more.Foundation.PWSTR),
    ]
    return FAX_DEVICE_STATUSW
FAX_ENUM_DELIVERY_REPORT_TYPES = Int32
DRT_NONE = 0
DRT_EMAIL = 1
DRT_INBOX = 2
FAX_ENUM_DEVICE_ID_SOURCE = Int32
DEV_ID_SRC_FAX = 0
DEV_ID_SRC_TAPI = 1
FAX_ENUM_JOB_COMMANDS = Int32
JC_UNKNOWN = 0
JC_DELETE = 1
JC_PAUSE = 2
JC_RESUME = 3
FAX_ENUM_JOB_SEND_ATTRIBUTES = Int32
JSA_NOW = 0
JSA_SPECIFIC_TIME = 1
JSA_DISCOUNT_PERIOD = 2
FAX_ENUM_LOG_CATEGORIES = Int32
FAXLOG_CATEGORY_INIT = 1
FAXLOG_CATEGORY_OUTBOUND = 2
FAXLOG_CATEGORY_INBOUND = 3
FAXLOG_CATEGORY_UNKNOWN = 4
FAX_ENUM_LOG_LEVELS = Int32
FAXLOG_LEVEL_NONE = 0
FAXLOG_LEVEL_MIN = 1
FAXLOG_LEVEL_MED = 2
FAXLOG_LEVEL_MAX = 3
FAX_ENUM_PORT_OPEN_TYPE = Int32
PORT_OPEN_QUERY = 1
PORT_OPEN_MODIFY = 2
def _define_FAX_EVENTA_head():
    class FAX_EVENTA(Structure):
        pass
    return FAX_EVENTA
def _define_FAX_EVENTA():
    FAX_EVENTA = win32more.Devices.Fax.FAX_EVENTA_head
    FAX_EVENTA._fields_ = [
        ('SizeOfStruct', UInt32),
        ('TimeStamp', win32more.Foundation.FILETIME),
        ('DeviceId', UInt32),
        ('EventId', UInt32),
        ('JobId', UInt32),
    ]
    return FAX_EVENTA
def _define_FAX_EVENTW_head():
    class FAX_EVENTW(Structure):
        pass
    return FAX_EVENTW
def _define_FAX_EVENTW():
    FAX_EVENTW = win32more.Devices.Fax.FAX_EVENTW_head
    FAX_EVENTW._fields_ = [
        ('SizeOfStruct', UInt32),
        ('TimeStamp', win32more.Foundation.FILETIME),
        ('DeviceId', UInt32),
        ('EventId', UInt32),
        ('JobId', UInt32),
    ]
    return FAX_EVENTW
def _define_FAX_GLOBAL_ROUTING_INFOA_head():
    class FAX_GLOBAL_ROUTING_INFOA(Structure):
        pass
    return FAX_GLOBAL_ROUTING_INFOA
def _define_FAX_GLOBAL_ROUTING_INFOA():
    FAX_GLOBAL_ROUTING_INFOA = win32more.Devices.Fax.FAX_GLOBAL_ROUTING_INFOA_head
    FAX_GLOBAL_ROUTING_INFOA._fields_ = [
        ('SizeOfStruct', UInt32),
        ('Priority', UInt32),
        ('Guid', win32more.Foundation.PSTR),
        ('FriendlyName', win32more.Foundation.PSTR),
        ('FunctionName', win32more.Foundation.PSTR),
        ('ExtensionImageName', win32more.Foundation.PSTR),
        ('ExtensionFriendlyName', win32more.Foundation.PSTR),
    ]
    return FAX_GLOBAL_ROUTING_INFOA
def _define_FAX_GLOBAL_ROUTING_INFOW_head():
    class FAX_GLOBAL_ROUTING_INFOW(Structure):
        pass
    return FAX_GLOBAL_ROUTING_INFOW
def _define_FAX_GLOBAL_ROUTING_INFOW():
    FAX_GLOBAL_ROUTING_INFOW = win32more.Devices.Fax.FAX_GLOBAL_ROUTING_INFOW_head
    FAX_GLOBAL_ROUTING_INFOW._fields_ = [
        ('SizeOfStruct', UInt32),
        ('Priority', UInt32),
        ('Guid', win32more.Foundation.PWSTR),
        ('FriendlyName', win32more.Foundation.PWSTR),
        ('FunctionName', win32more.Foundation.PWSTR),
        ('ExtensionImageName', win32more.Foundation.PWSTR),
        ('ExtensionFriendlyName', win32more.Foundation.PWSTR),
    ]
    return FAX_GLOBAL_ROUTING_INFOW
FAX_GROUP_STATUS_ENUM = Int32
FAX_GROUP_STATUS_ENUM_fgsALL_DEV_VALID = 0
FAX_GROUP_STATUS_ENUM_fgsEMPTY = 1
FAX_GROUP_STATUS_ENUM_fgsALL_DEV_NOT_VALID = 2
FAX_GROUP_STATUS_ENUM_fgsSOME_DEV_NOT_VALID = 3
def _define_FAX_JOB_ENTRYA_head():
    class FAX_JOB_ENTRYA(Structure):
        pass
    return FAX_JOB_ENTRYA
def _define_FAX_JOB_ENTRYA():
    FAX_JOB_ENTRYA = win32more.Devices.Fax.FAX_JOB_ENTRYA_head
    FAX_JOB_ENTRYA._fields_ = [
        ('SizeOfStruct', UInt32),
        ('JobId', UInt32),
        ('UserName', win32more.Foundation.PSTR),
        ('JobType', UInt32),
        ('QueueStatus', UInt32),
        ('Status', UInt32),
        ('Size', UInt32),
        ('PageCount', UInt32),
        ('RecipientNumber', win32more.Foundation.PSTR),
        ('RecipientName', win32more.Foundation.PSTR),
        ('Tsid', win32more.Foundation.PSTR),
        ('SenderName', win32more.Foundation.PSTR),
        ('SenderCompany', win32more.Foundation.PSTR),
        ('SenderDept', win32more.Foundation.PSTR),
        ('BillingCode', win32more.Foundation.PSTR),
        ('ScheduleAction', UInt32),
        ('ScheduleTime', win32more.Foundation.SYSTEMTIME),
        ('DeliveryReportType', UInt32),
        ('DeliveryReportAddress', win32more.Foundation.PSTR),
        ('DocumentName', win32more.Foundation.PSTR),
    ]
    return FAX_JOB_ENTRYA
def _define_FAX_JOB_ENTRYW_head():
    class FAX_JOB_ENTRYW(Structure):
        pass
    return FAX_JOB_ENTRYW
def _define_FAX_JOB_ENTRYW():
    FAX_JOB_ENTRYW = win32more.Devices.Fax.FAX_JOB_ENTRYW_head
    FAX_JOB_ENTRYW._fields_ = [
        ('SizeOfStruct', UInt32),
        ('JobId', UInt32),
        ('UserName', win32more.Foundation.PWSTR),
        ('JobType', UInt32),
        ('QueueStatus', UInt32),
        ('Status', UInt32),
        ('Size', UInt32),
        ('PageCount', UInt32),
        ('RecipientNumber', win32more.Foundation.PWSTR),
        ('RecipientName', win32more.Foundation.PWSTR),
        ('Tsid', win32more.Foundation.PWSTR),
        ('SenderName', win32more.Foundation.PWSTR),
        ('SenderCompany', win32more.Foundation.PWSTR),
        ('SenderDept', win32more.Foundation.PWSTR),
        ('BillingCode', win32more.Foundation.PWSTR),
        ('ScheduleAction', UInt32),
        ('ScheduleTime', win32more.Foundation.SYSTEMTIME),
        ('DeliveryReportType', UInt32),
        ('DeliveryReportAddress', win32more.Foundation.PWSTR),
        ('DocumentName', win32more.Foundation.PWSTR),
    ]
    return FAX_JOB_ENTRYW
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
def _define_FAX_JOB_PARAMA_head():
    class FAX_JOB_PARAMA(Structure):
        pass
    return FAX_JOB_PARAMA
def _define_FAX_JOB_PARAMA():
    FAX_JOB_PARAMA = win32more.Devices.Fax.FAX_JOB_PARAMA_head
    FAX_JOB_PARAMA._fields_ = [
        ('SizeOfStruct', UInt32),
        ('RecipientNumber', win32more.Foundation.PSTR),
        ('RecipientName', win32more.Foundation.PSTR),
        ('Tsid', win32more.Foundation.PSTR),
        ('SenderName', win32more.Foundation.PSTR),
        ('SenderCompany', win32more.Foundation.PSTR),
        ('SenderDept', win32more.Foundation.PSTR),
        ('BillingCode', win32more.Foundation.PSTR),
        ('ScheduleAction', UInt32),
        ('ScheduleTime', win32more.Foundation.SYSTEMTIME),
        ('DeliveryReportType', UInt32),
        ('DeliveryReportAddress', win32more.Foundation.PSTR),
        ('DocumentName', win32more.Foundation.PSTR),
        ('CallHandle', UInt32),
        ('Reserved', UIntPtr * 3),
    ]
    return FAX_JOB_PARAMA
def _define_FAX_JOB_PARAMW_head():
    class FAX_JOB_PARAMW(Structure):
        pass
    return FAX_JOB_PARAMW
def _define_FAX_JOB_PARAMW():
    FAX_JOB_PARAMW = win32more.Devices.Fax.FAX_JOB_PARAMW_head
    FAX_JOB_PARAMW._fields_ = [
        ('SizeOfStruct', UInt32),
        ('RecipientNumber', win32more.Foundation.PWSTR),
        ('RecipientName', win32more.Foundation.PWSTR),
        ('Tsid', win32more.Foundation.PWSTR),
        ('SenderName', win32more.Foundation.PWSTR),
        ('SenderCompany', win32more.Foundation.PWSTR),
        ('SenderDept', win32more.Foundation.PWSTR),
        ('BillingCode', win32more.Foundation.PWSTR),
        ('ScheduleAction', UInt32),
        ('ScheduleTime', win32more.Foundation.SYSTEMTIME),
        ('DeliveryReportType', UInt32),
        ('DeliveryReportAddress', win32more.Foundation.PWSTR),
        ('DocumentName', win32more.Foundation.PWSTR),
        ('CallHandle', UInt32),
        ('Reserved', UIntPtr * 3),
    ]
    return FAX_JOB_PARAMW
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
FAX_JOB_TYPE_ENUM = Int32
FAX_JOB_TYPE_ENUM_fjtSEND = 0
FAX_JOB_TYPE_ENUM_fjtRECEIVE = 1
FAX_JOB_TYPE_ENUM_fjtROUTING = 2
def _define_FAX_LOG_CATEGORYA_head():
    class FAX_LOG_CATEGORYA(Structure):
        pass
    return FAX_LOG_CATEGORYA
def _define_FAX_LOG_CATEGORYA():
    FAX_LOG_CATEGORYA = win32more.Devices.Fax.FAX_LOG_CATEGORYA_head
    FAX_LOG_CATEGORYA._fields_ = [
        ('Name', win32more.Foundation.PSTR),
        ('Category', UInt32),
        ('Level', UInt32),
    ]
    return FAX_LOG_CATEGORYA
def _define_FAX_LOG_CATEGORYW_head():
    class FAX_LOG_CATEGORYW(Structure):
        pass
    return FAX_LOG_CATEGORYW
def _define_FAX_LOG_CATEGORYW():
    FAX_LOG_CATEGORYW = win32more.Devices.Fax.FAX_LOG_CATEGORYW_head
    FAX_LOG_CATEGORYW._fields_ = [
        ('Name', win32more.Foundation.PWSTR),
        ('Category', UInt32),
        ('Level', UInt32),
    ]
    return FAX_LOG_CATEGORYW
FAX_LOG_LEVEL_ENUM = Int32
FAX_LOG_LEVEL_ENUM_fllNONE = 0
FAX_LOG_LEVEL_ENUM_fllMIN = 1
FAX_LOG_LEVEL_ENUM_fllMED = 2
FAX_LOG_LEVEL_ENUM_fllMAX = 3
def _define_FAX_PORT_INFOA_head():
    class FAX_PORT_INFOA(Structure):
        pass
    return FAX_PORT_INFOA
def _define_FAX_PORT_INFOA():
    FAX_PORT_INFOA = win32more.Devices.Fax.FAX_PORT_INFOA_head
    FAX_PORT_INFOA._fields_ = [
        ('SizeOfStruct', UInt32),
        ('DeviceId', UInt32),
        ('State', UInt32),
        ('Flags', UInt32),
        ('Rings', UInt32),
        ('Priority', UInt32),
        ('DeviceName', win32more.Foundation.PSTR),
        ('Tsid', win32more.Foundation.PSTR),
        ('Csid', win32more.Foundation.PSTR),
    ]
    return FAX_PORT_INFOA
def _define_FAX_PORT_INFOW_head():
    class FAX_PORT_INFOW(Structure):
        pass
    return FAX_PORT_INFOW
def _define_FAX_PORT_INFOW():
    FAX_PORT_INFOW = win32more.Devices.Fax.FAX_PORT_INFOW_head
    FAX_PORT_INFOW._fields_ = [
        ('SizeOfStruct', UInt32),
        ('DeviceId', UInt32),
        ('State', UInt32),
        ('Flags', UInt32),
        ('Rings', UInt32),
        ('Priority', UInt32),
        ('DeviceName', win32more.Foundation.PWSTR),
        ('Tsid', win32more.Foundation.PWSTR),
        ('Csid', win32more.Foundation.PWSTR),
    ]
    return FAX_PORT_INFOW
def _define_FAX_PRINT_INFOA_head():
    class FAX_PRINT_INFOA(Structure):
        pass
    return FAX_PRINT_INFOA
def _define_FAX_PRINT_INFOA():
    FAX_PRINT_INFOA = win32more.Devices.Fax.FAX_PRINT_INFOA_head
    FAX_PRINT_INFOA._fields_ = [
        ('SizeOfStruct', UInt32),
        ('DocName', win32more.Foundation.PSTR),
        ('RecipientName', win32more.Foundation.PSTR),
        ('RecipientNumber', win32more.Foundation.PSTR),
        ('SenderName', win32more.Foundation.PSTR),
        ('SenderCompany', win32more.Foundation.PSTR),
        ('SenderDept', win32more.Foundation.PSTR),
        ('SenderBillingCode', win32more.Foundation.PSTR),
        ('Reserved', win32more.Foundation.PSTR),
        ('DrEmailAddress', win32more.Foundation.PSTR),
        ('OutputFileName', win32more.Foundation.PSTR),
    ]
    return FAX_PRINT_INFOA
def _define_FAX_PRINT_INFOW_head():
    class FAX_PRINT_INFOW(Structure):
        pass
    return FAX_PRINT_INFOW
def _define_FAX_PRINT_INFOW():
    FAX_PRINT_INFOW = win32more.Devices.Fax.FAX_PRINT_INFOW_head
    FAX_PRINT_INFOW._fields_ = [
        ('SizeOfStruct', UInt32),
        ('DocName', win32more.Foundation.PWSTR),
        ('RecipientName', win32more.Foundation.PWSTR),
        ('RecipientNumber', win32more.Foundation.PWSTR),
        ('SenderName', win32more.Foundation.PWSTR),
        ('SenderCompany', win32more.Foundation.PWSTR),
        ('SenderDept', win32more.Foundation.PWSTR),
        ('SenderBillingCode', win32more.Foundation.PWSTR),
        ('Reserved', win32more.Foundation.PWSTR),
        ('DrEmailAddress', win32more.Foundation.PWSTR),
        ('OutputFileName', win32more.Foundation.PWSTR),
    ]
    return FAX_PRINT_INFOW
FAX_PRIORITY_TYPE_ENUM = Int32
FAX_PRIORITY_TYPE_ENUM_fptLOW = 0
FAX_PRIORITY_TYPE_ENUM_fptNORMAL = 1
FAX_PRIORITY_TYPE_ENUM_fptHIGH = 2
FAX_PROVIDER_STATUS_ENUM = Int32
FAX_PROVIDER_STATUS_ENUM_fpsSUCCESS = 0
FAX_PROVIDER_STATUS_ENUM_fpsSERVER_ERROR = 1
FAX_PROVIDER_STATUS_ENUM_fpsBAD_GUID = 2
FAX_PROVIDER_STATUS_ENUM_fpsBAD_VERSION = 3
FAX_PROVIDER_STATUS_ENUM_fpsCANT_LOAD = 4
FAX_PROVIDER_STATUS_ENUM_fpsCANT_LINK = 5
FAX_PROVIDER_STATUS_ENUM_fpsCANT_INIT = 6
FAX_RECEIPT_TYPE_ENUM = Int32
FAX_RECEIPT_TYPE_ENUM_frtNONE = 0
FAX_RECEIPT_TYPE_ENUM_frtMAIL = 1
FAX_RECEIPT_TYPE_ENUM_frtMSGBOX = 4
def _define_FAX_RECEIVE_head():
    class FAX_RECEIVE(Structure):
        pass
    return FAX_RECEIVE
def _define_FAX_RECEIVE():
    FAX_RECEIVE = win32more.Devices.Fax.FAX_RECEIVE_head
    FAX_RECEIVE._fields_ = [
        ('SizeOfStruct', UInt32),
        ('FileName', win32more.Foundation.PWSTR),
        ('ReceiverName', win32more.Foundation.PWSTR),
        ('ReceiverNumber', win32more.Foundation.PWSTR),
        ('Reserved', UInt32 * 4),
    ]
    return FAX_RECEIVE
def _define_FAX_ROUTE_head():
    class FAX_ROUTE(Structure):
        pass
    return FAX_ROUTE
def _define_FAX_ROUTE():
    FAX_ROUTE = win32more.Devices.Fax.FAX_ROUTE_head
    FAX_ROUTE._fields_ = [
        ('SizeOfStruct', UInt32),
        ('JobId', UInt32),
        ('ElapsedTime', UInt64),
        ('ReceiveTime', UInt64),
        ('PageCount', UInt32),
        ('Csid', win32more.Foundation.PWSTR),
        ('Tsid', win32more.Foundation.PWSTR),
        ('CallerId', win32more.Foundation.PWSTR),
        ('RoutingInfo', win32more.Foundation.PWSTR),
        ('ReceiverName', win32more.Foundation.PWSTR),
        ('ReceiverNumber', win32more.Foundation.PWSTR),
        ('DeviceName', win32more.Foundation.PWSTR),
        ('DeviceId', UInt32),
        ('RoutingInfoData', c_char_p_no),
        ('RoutingInfoDataSize', UInt32),
    ]
    return FAX_ROUTE
def _define_FAX_ROUTE_CALLBACKROUTINES_head():
    class FAX_ROUTE_CALLBACKROUTINES(Structure):
        pass
    return FAX_ROUTE_CALLBACKROUTINES
def _define_FAX_ROUTE_CALLBACKROUTINES():
    FAX_ROUTE_CALLBACKROUTINES = win32more.Devices.Fax.FAX_ROUTE_CALLBACKROUTINES_head
    FAX_ROUTE_CALLBACKROUTINES._fields_ = [
        ('SizeOfStruct', UInt32),
        ('FaxRouteAddFile', win32more.Devices.Fax.PFAXROUTEADDFILE),
        ('FaxRouteDeleteFile', win32more.Devices.Fax.PFAXROUTEDELETEFILE),
        ('FaxRouteGetFile', win32more.Devices.Fax.PFAXROUTEGETFILE),
        ('FaxRouteEnumFiles', win32more.Devices.Fax.PFAXROUTEENUMFILES),
        ('FaxRouteModifyRoutingData', win32more.Devices.Fax.PFAXROUTEMODIFYROUTINGDATA),
    ]
    return FAX_ROUTE_CALLBACKROUTINES
def _define_FAX_ROUTING_METHODA_head():
    class FAX_ROUTING_METHODA(Structure):
        pass
    return FAX_ROUTING_METHODA
def _define_FAX_ROUTING_METHODA():
    FAX_ROUTING_METHODA = win32more.Devices.Fax.FAX_ROUTING_METHODA_head
    FAX_ROUTING_METHODA._fields_ = [
        ('SizeOfStruct', UInt32),
        ('DeviceId', UInt32),
        ('Enabled', win32more.Foundation.BOOL),
        ('DeviceName', win32more.Foundation.PSTR),
        ('Guid', win32more.Foundation.PSTR),
        ('FriendlyName', win32more.Foundation.PSTR),
        ('FunctionName', win32more.Foundation.PSTR),
        ('ExtensionImageName', win32more.Foundation.PSTR),
        ('ExtensionFriendlyName', win32more.Foundation.PSTR),
    ]
    return FAX_ROUTING_METHODA
def _define_FAX_ROUTING_METHODW_head():
    class FAX_ROUTING_METHODW(Structure):
        pass
    return FAX_ROUTING_METHODW
def _define_FAX_ROUTING_METHODW():
    FAX_ROUTING_METHODW = win32more.Devices.Fax.FAX_ROUTING_METHODW_head
    FAX_ROUTING_METHODW._fields_ = [
        ('SizeOfStruct', UInt32),
        ('DeviceId', UInt32),
        ('Enabled', win32more.Foundation.BOOL),
        ('DeviceName', win32more.Foundation.PWSTR),
        ('Guid', win32more.Foundation.PWSTR),
        ('FriendlyName', win32more.Foundation.PWSTR),
        ('FunctionName', win32more.Foundation.PWSTR),
        ('ExtensionImageName', win32more.Foundation.PWSTR),
        ('ExtensionFriendlyName', win32more.Foundation.PWSTR),
    ]
    return FAX_ROUTING_METHODW
FAX_ROUTING_RULE_CODE_ENUM = Int32
frrcANY_CODE = 0
FAX_RULE_STATUS_ENUM = Int32
FAX_RULE_STATUS_ENUM_frsVALID = 0
FAX_RULE_STATUS_ENUM_frsEMPTY_GROUP = 1
FAX_RULE_STATUS_ENUM_frsALL_GROUP_DEV_NOT_VALID = 2
FAX_RULE_STATUS_ENUM_frsSOME_GROUP_DEV_NOT_VALID = 3
FAX_RULE_STATUS_ENUM_frsBAD_DEVICE = 4
FAX_SCHEDULE_TYPE_ENUM = Int32
FAX_SCHEDULE_TYPE_ENUM_fstNOW = 0
FAX_SCHEDULE_TYPE_ENUM_fstSPECIFIC_TIME = 1
FAX_SCHEDULE_TYPE_ENUM_fstDISCOUNT_PERIOD = 2
def _define_FAX_SEND_head():
    class FAX_SEND(Structure):
        pass
    return FAX_SEND
def _define_FAX_SEND():
    FAX_SEND = win32more.Devices.Fax.FAX_SEND_head
    FAX_SEND._fields_ = [
        ('SizeOfStruct', UInt32),
        ('FileName', win32more.Foundation.PWSTR),
        ('CallerName', win32more.Foundation.PWSTR),
        ('CallerNumber', win32more.Foundation.PWSTR),
        ('ReceiverName', win32more.Foundation.PWSTR),
        ('ReceiverNumber', win32more.Foundation.PWSTR),
        ('Branding', win32more.Foundation.BOOL),
        ('CallHandle', UInt32),
        ('Reserved', UInt32 * 3),
    ]
    return FAX_SEND
FAX_SERVER_APIVERSION_ENUM = Int32
fsAPI_VERSION_0 = 0
fsAPI_VERSION_1 = 65536
fsAPI_VERSION_2 = 131072
fsAPI_VERSION_3 = 196608
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
FAX_SMTP_AUTHENTICATION_TYPE_ENUM = Int32
FAX_SMTP_AUTHENTICATION_TYPE_ENUM_fsatANONYMOUS = 0
FAX_SMTP_AUTHENTICATION_TYPE_ENUM_fsatBASIC = 1
FAX_SMTP_AUTHENTICATION_TYPE_ENUM_fsatNTLM = 2
def _define_FAX_TIME_head():
    class FAX_TIME(Structure):
        pass
    return FAX_TIME
def _define_FAX_TIME():
    FAX_TIME = win32more.Devices.Fax.FAX_TIME_head
    FAX_TIME._fields_ = [
        ('Hour', UInt16),
        ('Minute', UInt16),
    ]
    return FAX_TIME
FaxAccount = Guid('a7e0647f-4524-4464-a5-6d-b9-fe-66-6f-71-5e')
FaxAccountFolders = Guid('85398f49-c034-4a3f-82-1c-db-7d-68-5e-81-29')
FaxAccountIncomingArchive = Guid('14b33db5-4c40-4ecf-9e-f8-a3-60-cb-e8-09-ed')
FaxAccountIncomingQueue = Guid('9bcf6094-b4da-45f4-b8-d6-dd-eb-21-86-65-2c')
FaxAccountOutgoingArchive = Guid('851e7af5-433a-4739-a2-df-ad-24-5c-2c-b9-8e')
FaxAccountOutgoingQueue = Guid('feeceefb-c149-48ba-ba-b8-b7-91-e1-01-f6-2f')
FaxAccounts = Guid('da1f94aa-ee2c-47c0-8f-4f-2a-21-70-75-b7-6e')
FaxAccountSet = Guid('fbc23c4b-79e0-4291-bc-56-c1-2e-25-3b-bf-3a')
FaxActivity = Guid('cfef5d0e-e84d-462e-aa-bb-87-d3-1e-b0-4f-ef')
FaxActivityLogging = Guid('f0a0294e-3bbd-48b8-8f-13-8c-59-1a-55-bd-bc')
FaxConfiguration = Guid('5857326f-e7b3-41a7-9c-19-a9-1b-46-3e-2d-56')
FaxDevice = Guid('59e3a5b2-d676-484b-a6-de-72-0b-fa-89-b5-af')
FaxDeviceIds = Guid('cdc539ea-7277-460e-8d-e0-48-a0-a5-76-0d-1f')
FaxDeviceProvider = Guid('17cf1aa3-f5eb-484a-9c-9a-44-40-a5-ba-ab-fc')
FaxDeviceProviders = Guid('eb8fe768-875a-4f5f-82-c5-03-f2-3a-ac-1b-d7')
FaxDevices = Guid('5589e28e-23cb-4919-88-08-e6-10-18-46-e8-0d')
FaxDocument = Guid('0f3f9f91-c838-415e-a4-f3-3e-82-8c-a4-45-e0')
FaxEventLogging = Guid('a6850930-a0f6-4a6f-95-b7-db-2e-bf-3d-02-e3')
FaxFolders = Guid('c35211d7-5776-48cb-af-44-c3-1b-e3-b2-cf-e5')
FaxInboundRouting = Guid('e80248ed-ad65-4218-81-08-99-19-24-d4-e7-ed')
FaxInboundRoutingExtension = Guid('1d7dfb51-7207-4436-a0-d9-24-e3-2e-e5-69-88')
FaxInboundRoutingExtensions = Guid('189a48ed-623c-4c0d-80-f2-d6-6c-7b-9e-fe-c2')
FaxInboundRoutingMethod = Guid('4b9fd75c-0194-4b72-9c-e5-02-a8-20-5a-c7-d4')
FaxInboundRoutingMethods = Guid('25fcb76a-b750-4b82-92-66-fb-bb-ae-89-22-ba')
FaxIncomingArchive = Guid('8426c56a-35a1-4c6f-af-93-fc-95-24-22-e2-c2')
FaxIncomingJob = Guid('c47311ec-ae32-41b8-ae-4b-3e-ae-06-29-d0-c9')
FaxIncomingJobs = Guid('a1bb8a43-8866-4fb7-a1-5d-62-66-c8-75-a5-cc')
FaxIncomingMessage = Guid('1932fcf7-9d43-4d5a-89-ff-03-86-1b-32-17-36')
FaxIncomingMessageIterator = Guid('6088e1d8-3fc8-45c2-87-b1-90-9a-29-60-7e-a9')
FaxIncomingQueue = Guid('69131717-f3f1-40e3-80-9d-a6-cb-f7-bd-85-e5')
FaxJobStatus = Guid('7bf222f4-be8d-442f-84-1d-61-32-74-24-23-bb')
FaxLoggingOptions = Guid('1bf9eea6-ece0-4785-a1-8b-de-56-e9-ee-f9-6a')
FaxOutboundRouting = Guid('c81b385e-b869-4afd-86-c0-61-64-98-ed-9b-e2')
FaxOutboundRoutingGroup = Guid('0213f3e0-6791-4d77-a2-71-04-d2-35-7c-50-d6')
FaxOutboundRoutingGroups = Guid('ccbea1a5-e2b4-4b57-94-21-b0-4b-62-89-46-4b')
FaxOutboundRoutingRule = Guid('6549eebf-08d1-475a-82-8b-3b-f1-05-95-2f-a0')
FaxOutboundRoutingRules = Guid('d385beca-e624-4473-bf-aa-9f-40-00-83-1f-54')
FaxOutgoingArchive = Guid('43c28403-e04f-474d-99-0c-b9-46-69-14-8f-59')
FaxOutgoingJob = Guid('71bb429c-0ef9-4915-be-c5-a5-d8-97-a3-e9-24')
FaxOutgoingJobs = Guid('92bf2a6c-37be-43fa-a3-7d-cb-0e-5f-75-3b-35')
FaxOutgoingMessage = Guid('91b4a378-4ad8-4aef-a4-dc-97-d9-6e-93-9a-3a')
FaxOutgoingMessageIterator = Guid('8a3224d0-d30b-49de-98-13-cb-38-57-90-fb-bb')
FaxOutgoingQueue = Guid('7421169e-8c43-4b0d-bb-16-64-5c-8f-a4-03-57')
FaxReceiptOptions = Guid('6982487b-227b-4c96-a6-1c-24-83-48-b0-5a-b6')
FaxRecipient = Guid('60bf3301-7df8-4bd8-91-48-7b-58-01-f9-ef-df')
FaxRecipients = Guid('ea9bdf53-10a9-4d4f-a0-67-63-c8-f8-4f-01-b0')
FAXROUTE_ENABLE = Int32
QUERY_STATUS = -1
STATUS_DISABLE = 0
STATUS_ENABLE = 1
FaxSecurity = Guid('10c4ddde-abf0-43df-96-4f-7f-3a-c2-1a-4c-7b')
FaxSecurity2 = Guid('735c1248-ec89-4c30-a1-27-65-6e-92-e3-c4-ea')
FaxSender = Guid('265d84d0-1850-4360-b7-c8-75-8b-bb-5f-0b-96')
FaxServer = Guid('cda8acb0-8cf5-4f6c-9b-a2-59-31-d4-0c-8c-ae')
def _define_IFaxAccount_head():
    class IFaxAccount(win32more.System.Com.IDispatch_head):
        Guid = Guid('68535b33-5dc4-4086-be-26-b7-6f-9b-71-10-06')
    return IFaxAccount
def _define_IFaxAccount():
    IFaxAccount = win32more.Devices.Fax.IFaxAccount_head
    IFaxAccount.get_AccountName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_AccountName', ((1, 'pbstrAccountName'),)))
    IFaxAccount.get_Folders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxAccountFolders_head))(8, 'get_Folders', ((1, 'ppFolders'),)))
    IFaxAccount.ListenToAccountEvents = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.FAX_ACCOUNT_EVENTS_TYPE_ENUM)(9, 'ListenToAccountEvents', ((1, 'EventTypes'),)))
    IFaxAccount.get_RegisteredEvents = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_ACCOUNT_EVENTS_TYPE_ENUM))(10, 'get_RegisteredEvents', ((1, 'pRegisteredEvents'),)))
    win32more.System.Com.IDispatch
    return IFaxAccount
def _define_IFaxAccountFolders_head():
    class IFaxAccountFolders(win32more.System.Com.IDispatch_head):
        Guid = Guid('6463f89d-23d8-46a9-8f-86-c4-7b-77-ca-79-26')
    return IFaxAccountFolders
def _define_IFaxAccountFolders():
    IFaxAccountFolders = win32more.Devices.Fax.IFaxAccountFolders_head
    IFaxAccountFolders.get_OutgoingQueue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxAccountOutgoingQueue_head))(7, 'get_OutgoingQueue', ((1, 'pFaxOutgoingQueue'),)))
    IFaxAccountFolders.get_IncomingQueue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxAccountIncomingQueue_head))(8, 'get_IncomingQueue', ((1, 'pFaxIncomingQueue'),)))
    IFaxAccountFolders.get_IncomingArchive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxAccountIncomingArchive_head))(9, 'get_IncomingArchive', ((1, 'pFaxIncomingArchive'),)))
    IFaxAccountFolders.get_OutgoingArchive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxAccountOutgoingArchive_head))(10, 'get_OutgoingArchive', ((1, 'pFaxOutgoingArchive'),)))
    win32more.System.Com.IDispatch
    return IFaxAccountFolders
def _define_IFaxAccountIncomingArchive_head():
    class IFaxAccountIncomingArchive(win32more.System.Com.IDispatch_head):
        Guid = Guid('a8a5b6ef-e0d6-4aee-95-5c-91-62-5b-ec-9d-b4')
    return IFaxAccountIncomingArchive
def _define_IFaxAccountIncomingArchive():
    IFaxAccountIncomingArchive = win32more.Devices.Fax.IFaxAccountIncomingArchive_head
    IFaxAccountIncomingArchive.get_SizeLow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_SizeLow', ((1, 'plSizeLow'),)))
    IFaxAccountIncomingArchive.get_SizeHigh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(8, 'get_SizeHigh', ((1, 'plSizeHigh'),)))
    IFaxAccountIncomingArchive.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(9, 'Refresh', ()))
    IFaxAccountIncomingArchive.GetMessages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Devices.Fax.IFaxIncomingMessageIterator_head))(10, 'GetMessages', ((1, 'lPrefetchSize'),(1, 'pFaxIncomingMessageIterator'),)))
    IFaxAccountIncomingArchive.GetMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Devices.Fax.IFaxIncomingMessage_head))(11, 'GetMessage', ((1, 'bstrMessageId'),(1, 'pFaxIncomingMessage'),)))
    win32more.System.Com.IDispatch
    return IFaxAccountIncomingArchive
def _define_IFaxAccountIncomingQueue_head():
    class IFaxAccountIncomingQueue(win32more.System.Com.IDispatch_head):
        Guid = Guid('dd142d92-0186-4a95-a0-90-cb-c3-ea-db-a6-b4')
    return IFaxAccountIncomingQueue
def _define_IFaxAccountIncomingQueue():
    IFaxAccountIncomingQueue = win32more.Devices.Fax.IFaxAccountIncomingQueue_head
    IFaxAccountIncomingQueue.GetJobs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxIncomingJobs_head))(7, 'GetJobs', ((1, 'pFaxIncomingJobs'),)))
    IFaxAccountIncomingQueue.GetJob = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Devices.Fax.IFaxIncomingJob_head))(8, 'GetJob', ((1, 'bstrJobId'),(1, 'pFaxIncomingJob'),)))
    win32more.System.Com.IDispatch
    return IFaxAccountIncomingQueue
def _define_IFaxAccountNotify_head():
    class IFaxAccountNotify(win32more.System.Com.IDispatch_head):
        Guid = Guid('b9b3bc81-ac1b-46f3-b3-9d-0a-dc-30-e1-b7-88')
    return IFaxAccountNotify
def _define_IFaxAccountNotify():
    IFaxAccountNotify = win32more.Devices.Fax.IFaxAccountNotify_head
    IFaxAccountNotify.OnIncomingJobAdded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxAccount_head,win32more.Foundation.BSTR)(7, 'OnIncomingJobAdded', ((1, 'pFaxAccount'),(1, 'bstrJobId'),)))
    IFaxAccountNotify.OnIncomingJobRemoved = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxAccount_head,win32more.Foundation.BSTR)(8, 'OnIncomingJobRemoved', ((1, 'pFaxAccount'),(1, 'bstrJobId'),)))
    IFaxAccountNotify.OnIncomingJobChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxAccount_head,win32more.Foundation.BSTR,win32more.Devices.Fax.IFaxJobStatus_head)(9, 'OnIncomingJobChanged', ((1, 'pFaxAccount'),(1, 'bstrJobId'),(1, 'pJobStatus'),)))
    IFaxAccountNotify.OnOutgoingJobAdded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxAccount_head,win32more.Foundation.BSTR)(10, 'OnOutgoingJobAdded', ((1, 'pFaxAccount'),(1, 'bstrJobId'),)))
    IFaxAccountNotify.OnOutgoingJobRemoved = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxAccount_head,win32more.Foundation.BSTR)(11, 'OnOutgoingJobRemoved', ((1, 'pFaxAccount'),(1, 'bstrJobId'),)))
    IFaxAccountNotify.OnOutgoingJobChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxAccount_head,win32more.Foundation.BSTR,win32more.Devices.Fax.IFaxJobStatus_head)(12, 'OnOutgoingJobChanged', ((1, 'pFaxAccount'),(1, 'bstrJobId'),(1, 'pJobStatus'),)))
    IFaxAccountNotify.OnIncomingMessageAdded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxAccount_head,win32more.Foundation.BSTR,win32more.Foundation.VARIANT_BOOL)(13, 'OnIncomingMessageAdded', ((1, 'pFaxAccount'),(1, 'bstrMessageId'),(1, 'fAddedToReceiveFolder'),)))
    IFaxAccountNotify.OnIncomingMessageRemoved = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxAccount_head,win32more.Foundation.BSTR,win32more.Foundation.VARIANT_BOOL)(14, 'OnIncomingMessageRemoved', ((1, 'pFaxAccount'),(1, 'bstrMessageId'),(1, 'fRemovedFromReceiveFolder'),)))
    IFaxAccountNotify.OnOutgoingMessageAdded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxAccount_head,win32more.Foundation.BSTR)(15, 'OnOutgoingMessageAdded', ((1, 'pFaxAccount'),(1, 'bstrMessageId'),)))
    IFaxAccountNotify.OnOutgoingMessageRemoved = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxAccount_head,win32more.Foundation.BSTR)(16, 'OnOutgoingMessageRemoved', ((1, 'pFaxAccount'),(1, 'bstrMessageId'),)))
    IFaxAccountNotify.OnServerShutDown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head)(17, 'OnServerShutDown', ((1, 'pFaxServer'),)))
    win32more.System.Com.IDispatch
    return IFaxAccountNotify
def _define_IFaxAccountOutgoingArchive_head():
    class IFaxAccountOutgoingArchive(win32more.System.Com.IDispatch_head):
        Guid = Guid('5463076d-ec14-491f-92-6e-b3-ce-da-5e-56-62')
    return IFaxAccountOutgoingArchive
def _define_IFaxAccountOutgoingArchive():
    IFaxAccountOutgoingArchive = win32more.Devices.Fax.IFaxAccountOutgoingArchive_head
    IFaxAccountOutgoingArchive.get_SizeLow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_SizeLow', ((1, 'plSizeLow'),)))
    IFaxAccountOutgoingArchive.get_SizeHigh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(8, 'get_SizeHigh', ((1, 'plSizeHigh'),)))
    IFaxAccountOutgoingArchive.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(9, 'Refresh', ()))
    IFaxAccountOutgoingArchive.GetMessages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Devices.Fax.IFaxOutgoingMessageIterator_head))(10, 'GetMessages', ((1, 'lPrefetchSize'),(1, 'pFaxOutgoingMessageIterator'),)))
    IFaxAccountOutgoingArchive.GetMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Devices.Fax.IFaxOutgoingMessage_head))(11, 'GetMessage', ((1, 'bstrMessageId'),(1, 'pFaxOutgoingMessage'),)))
    win32more.System.Com.IDispatch
    return IFaxAccountOutgoingArchive
def _define_IFaxAccountOutgoingQueue_head():
    class IFaxAccountOutgoingQueue(win32more.System.Com.IDispatch_head):
        Guid = Guid('0f1424e9-f22d-4553-b7-a5-0d-24-bd-0d-7e-46')
    return IFaxAccountOutgoingQueue
def _define_IFaxAccountOutgoingQueue():
    IFaxAccountOutgoingQueue = win32more.Devices.Fax.IFaxAccountOutgoingQueue_head
    IFaxAccountOutgoingQueue.GetJobs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxOutgoingJobs_head))(7, 'GetJobs', ((1, 'pFaxOutgoingJobs'),)))
    IFaxAccountOutgoingQueue.GetJob = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Devices.Fax.IFaxOutgoingJob_head))(8, 'GetJob', ((1, 'bstrJobId'),(1, 'pFaxOutgoingJob'),)))
    win32more.System.Com.IDispatch
    return IFaxAccountOutgoingQueue
def _define_IFaxAccounts_head():
    class IFaxAccounts(win32more.System.Com.IDispatch_head):
        Guid = Guid('93ea8162-8be7-42d1-ae-7b-ec-74-e2-d9-89-da')
    return IFaxAccounts
def _define_IFaxAccounts():
    IFaxAccounts = win32more.Devices.Fax.IFaxAccounts_head
    IFaxAccounts.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(7, 'get__NewEnum', ((1, 'ppUnk'),)))
    IFaxAccounts.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.Devices.Fax.IFaxAccount_head))(8, 'get_Item', ((1, 'vIndex'),(1, 'pFaxAccount'),)))
    IFaxAccounts.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(9, 'get_Count', ((1, 'plCount'),)))
    win32more.System.Com.IDispatch
    return IFaxAccounts
def _define_IFaxAccountSet_head():
    class IFaxAccountSet(win32more.System.Com.IDispatch_head):
        Guid = Guid('7428fbae-841e-47b8-86-f4-22-88-94-6d-ca-1b')
    return IFaxAccountSet
def _define_IFaxAccountSet():
    IFaxAccountSet = win32more.Devices.Fax.IFaxAccountSet_head
    IFaxAccountSet.GetAccounts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxAccounts_head))(7, 'GetAccounts', ((1, 'ppFaxAccounts'),)))
    IFaxAccountSet.GetAccount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Devices.Fax.IFaxAccount_head))(8, 'GetAccount', ((1, 'bstrAccountName'),(1, 'pFaxAccount'),)))
    IFaxAccountSet.AddAccount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Devices.Fax.IFaxAccount_head))(9, 'AddAccount', ((1, 'bstrAccountName'),(1, 'pFaxAccount'),)))
    IFaxAccountSet.RemoveAccount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(10, 'RemoveAccount', ((1, 'bstrAccountName'),)))
    win32more.System.Com.IDispatch
    return IFaxAccountSet
def _define_IFaxActivity_head():
    class IFaxActivity(win32more.System.Com.IDispatch_head):
        Guid = Guid('4b106f97-3df5-40f2-bc-3c-44-cb-81-15-eb-df')
    return IFaxActivity
def _define_IFaxActivity():
    IFaxActivity = win32more.Devices.Fax.IFaxActivity_head
    IFaxActivity.get_IncomingMessages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_IncomingMessages', ((1, 'plIncomingMessages'),)))
    IFaxActivity.get_RoutingMessages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(8, 'get_RoutingMessages', ((1, 'plRoutingMessages'),)))
    IFaxActivity.get_OutgoingMessages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(9, 'get_OutgoingMessages', ((1, 'plOutgoingMessages'),)))
    IFaxActivity.get_QueuedMessages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(10, 'get_QueuedMessages', ((1, 'plQueuedMessages'),)))
    IFaxActivity.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(11, 'Refresh', ()))
    win32more.System.Com.IDispatch
    return IFaxActivity
def _define_IFaxActivityLogging_head():
    class IFaxActivityLogging(win32more.System.Com.IDispatch_head):
        Guid = Guid('1e29078b-5a69-497b-95-92-49-b7-e7-fa-dd-b5')
    return IFaxActivityLogging
def _define_IFaxActivityLogging():
    IFaxActivityLogging = win32more.Devices.Fax.IFaxActivityLogging_head
    IFaxActivityLogging.get_LogIncoming = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(7, 'get_LogIncoming', ((1, 'pbLogIncoming'),)))
    IFaxActivityLogging.put_LogIncoming = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(8, 'put_LogIncoming', ((1, 'bLogIncoming'),)))
    IFaxActivityLogging.get_LogOutgoing = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(9, 'get_LogOutgoing', ((1, 'pbLogOutgoing'),)))
    IFaxActivityLogging.put_LogOutgoing = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(10, 'put_LogOutgoing', ((1, 'bLogOutgoing'),)))
    IFaxActivityLogging.get_DatabasePath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(11, 'get_DatabasePath', ((1, 'pbstrDatabasePath'),)))
    IFaxActivityLogging.put_DatabasePath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(12, 'put_DatabasePath', ((1, 'bstrDatabasePath'),)))
    IFaxActivityLogging.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(13, 'Refresh', ()))
    IFaxActivityLogging.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(14, 'Save', ()))
    win32more.System.Com.IDispatch
    return IFaxActivityLogging
def _define_IFaxConfiguration_head():
    class IFaxConfiguration(win32more.System.Com.IDispatch_head):
        Guid = Guid('10f4d0f7-0994-4543-ab-6e-50-69-49-12-8c-40')
    return IFaxConfiguration
def _define_IFaxConfiguration():
    IFaxConfiguration = win32more.Devices.Fax.IFaxConfiguration_head
    IFaxConfiguration.get_UseArchive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(7, 'get_UseArchive', ((1, 'pbUseArchive'),)))
    IFaxConfiguration.put_UseArchive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(8, 'put_UseArchive', ((1, 'bUseArchive'),)))
    IFaxConfiguration.get_ArchiveLocation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_ArchiveLocation', ((1, 'pbstrArchiveLocation'),)))
    IFaxConfiguration.put_ArchiveLocation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(10, 'put_ArchiveLocation', ((1, 'bstrArchiveLocation'),)))
    IFaxConfiguration.get_SizeQuotaWarning = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(11, 'get_SizeQuotaWarning', ((1, 'pbSizeQuotaWarning'),)))
    IFaxConfiguration.put_SizeQuotaWarning = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(12, 'put_SizeQuotaWarning', ((1, 'bSizeQuotaWarning'),)))
    IFaxConfiguration.get_HighQuotaWaterMark = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(13, 'get_HighQuotaWaterMark', ((1, 'plHighQuotaWaterMark'),)))
    IFaxConfiguration.put_HighQuotaWaterMark = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(14, 'put_HighQuotaWaterMark', ((1, 'lHighQuotaWaterMark'),)))
    IFaxConfiguration.get_LowQuotaWaterMark = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(15, 'get_LowQuotaWaterMark', ((1, 'plLowQuotaWaterMark'),)))
    IFaxConfiguration.put_LowQuotaWaterMark = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(16, 'put_LowQuotaWaterMark', ((1, 'lLowQuotaWaterMark'),)))
    IFaxConfiguration.get_ArchiveAgeLimit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(17, 'get_ArchiveAgeLimit', ((1, 'plArchiveAgeLimit'),)))
    IFaxConfiguration.put_ArchiveAgeLimit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(18, 'put_ArchiveAgeLimit', ((1, 'lArchiveAgeLimit'),)))
    IFaxConfiguration.get_ArchiveSizeLow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(19, 'get_ArchiveSizeLow', ((1, 'plSizeLow'),)))
    IFaxConfiguration.get_ArchiveSizeHigh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(20, 'get_ArchiveSizeHigh', ((1, 'plSizeHigh'),)))
    IFaxConfiguration.get_OutgoingQueueBlocked = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(21, 'get_OutgoingQueueBlocked', ((1, 'pbOutgoingBlocked'),)))
    IFaxConfiguration.put_OutgoingQueueBlocked = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(22, 'put_OutgoingQueueBlocked', ((1, 'bOutgoingBlocked'),)))
    IFaxConfiguration.get_OutgoingQueuePaused = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(23, 'get_OutgoingQueuePaused', ((1, 'pbOutgoingPaused'),)))
    IFaxConfiguration.put_OutgoingQueuePaused = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(24, 'put_OutgoingQueuePaused', ((1, 'bOutgoingPaused'),)))
    IFaxConfiguration.get_AllowPersonalCoverPages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(25, 'get_AllowPersonalCoverPages', ((1, 'pbAllowPersonalCoverPages'),)))
    IFaxConfiguration.put_AllowPersonalCoverPages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(26, 'put_AllowPersonalCoverPages', ((1, 'bAllowPersonalCoverPages'),)))
    IFaxConfiguration.get_UseDeviceTSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(27, 'get_UseDeviceTSID', ((1, 'pbUseDeviceTSID'),)))
    IFaxConfiguration.put_UseDeviceTSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(28, 'put_UseDeviceTSID', ((1, 'bUseDeviceTSID'),)))
    IFaxConfiguration.get_Retries = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(29, 'get_Retries', ((1, 'plRetries'),)))
    IFaxConfiguration.put_Retries = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(30, 'put_Retries', ((1, 'lRetries'),)))
    IFaxConfiguration.get_RetryDelay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(31, 'get_RetryDelay', ((1, 'plRetryDelay'),)))
    IFaxConfiguration.put_RetryDelay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(32, 'put_RetryDelay', ((1, 'lRetryDelay'),)))
    IFaxConfiguration.get_DiscountRateStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(33, 'get_DiscountRateStart', ((1, 'pdateDiscountRateStart'),)))
    IFaxConfiguration.put_DiscountRateStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double)(34, 'put_DiscountRateStart', ((1, 'dateDiscountRateStart'),)))
    IFaxConfiguration.get_DiscountRateEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(35, 'get_DiscountRateEnd', ((1, 'pdateDiscountRateEnd'),)))
    IFaxConfiguration.put_DiscountRateEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double)(36, 'put_DiscountRateEnd', ((1, 'dateDiscountRateEnd'),)))
    IFaxConfiguration.get_OutgoingQueueAgeLimit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(37, 'get_OutgoingQueueAgeLimit', ((1, 'plOutgoingQueueAgeLimit'),)))
    IFaxConfiguration.put_OutgoingQueueAgeLimit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(38, 'put_OutgoingQueueAgeLimit', ((1, 'lOutgoingQueueAgeLimit'),)))
    IFaxConfiguration.get_Branding = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(39, 'get_Branding', ((1, 'pbBranding'),)))
    IFaxConfiguration.put_Branding = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(40, 'put_Branding', ((1, 'bBranding'),)))
    IFaxConfiguration.get_IncomingQueueBlocked = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(41, 'get_IncomingQueueBlocked', ((1, 'pbIncomingBlocked'),)))
    IFaxConfiguration.put_IncomingQueueBlocked = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(42, 'put_IncomingQueueBlocked', ((1, 'bIncomingBlocked'),)))
    IFaxConfiguration.get_AutoCreateAccountOnConnect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(43, 'get_AutoCreateAccountOnConnect', ((1, 'pbAutoCreateAccountOnConnect'),)))
    IFaxConfiguration.put_AutoCreateAccountOnConnect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(44, 'put_AutoCreateAccountOnConnect', ((1, 'bAutoCreateAccountOnConnect'),)))
    IFaxConfiguration.get_IncomingFaxesArePublic = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(45, 'get_IncomingFaxesArePublic', ((1, 'pbIncomingFaxesArePublic'),)))
    IFaxConfiguration.put_IncomingFaxesArePublic = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(46, 'put_IncomingFaxesArePublic', ((1, 'bIncomingFaxesArePublic'),)))
    IFaxConfiguration.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(47, 'Refresh', ()))
    IFaxConfiguration.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(48, 'Save', ()))
    win32more.System.Com.IDispatch
    return IFaxConfiguration
def _define_IFaxDevice_head():
    class IFaxDevice(win32more.System.Com.IDispatch_head):
        Guid = Guid('49306c59-b52e-4867-9d-f4-ca-58-41-c9-56-d0')
    return IFaxDevice
def _define_IFaxDevice():
    IFaxDevice = win32more.Devices.Fax.IFaxDevice_head
    IFaxDevice.get_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_Id', ((1, 'plId'),)))
    IFaxDevice.get_DeviceName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(8, 'get_DeviceName', ((1, 'pbstrDeviceName'),)))
    IFaxDevice.get_ProviderUniqueName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_ProviderUniqueName', ((1, 'pbstrProviderUniqueName'),)))
    IFaxDevice.get_PoweredOff = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(10, 'get_PoweredOff', ((1, 'pbPoweredOff'),)))
    IFaxDevice.get_ReceivingNow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(11, 'get_ReceivingNow', ((1, 'pbReceivingNow'),)))
    IFaxDevice.get_SendingNow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(12, 'get_SendingNow', ((1, 'pbSendingNow'),)))
    IFaxDevice.get_UsedRoutingMethods = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(13, 'get_UsedRoutingMethods', ((1, 'pvUsedRoutingMethods'),)))
    IFaxDevice.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(14, 'get_Description', ((1, 'pbstrDescription'),)))
    IFaxDevice.put_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(15, 'put_Description', ((1, 'bstrDescription'),)))
    IFaxDevice.get_SendEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(16, 'get_SendEnabled', ((1, 'pbSendEnabled'),)))
    IFaxDevice.put_SendEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(17, 'put_SendEnabled', ((1, 'bSendEnabled'),)))
    IFaxDevice.get_ReceiveMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_DEVICE_RECEIVE_MODE_ENUM))(18, 'get_ReceiveMode', ((1, 'pReceiveMode'),)))
    IFaxDevice.put_ReceiveMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.FAX_DEVICE_RECEIVE_MODE_ENUM)(19, 'put_ReceiveMode', ((1, 'ReceiveMode'),)))
    IFaxDevice.get_RingsBeforeAnswer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(20, 'get_RingsBeforeAnswer', ((1, 'plRingsBeforeAnswer'),)))
    IFaxDevice.put_RingsBeforeAnswer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(21, 'put_RingsBeforeAnswer', ((1, 'lRingsBeforeAnswer'),)))
    IFaxDevice.get_CSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(22, 'get_CSID', ((1, 'pbstrCSID'),)))
    IFaxDevice.put_CSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(23, 'put_CSID', ((1, 'bstrCSID'),)))
    IFaxDevice.get_TSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(24, 'get_TSID', ((1, 'pbstrTSID'),)))
    IFaxDevice.put_TSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(25, 'put_TSID', ((1, 'bstrTSID'),)))
    IFaxDevice.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(26, 'Refresh', ()))
    IFaxDevice.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(27, 'Save', ()))
    IFaxDevice.GetExtensionProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head))(28, 'GetExtensionProperty', ((1, 'bstrGUID'),(1, 'pvProperty'),)))
    IFaxDevice.SetExtensionProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT)(29, 'SetExtensionProperty', ((1, 'bstrGUID'),(1, 'vProperty'),)))
    IFaxDevice.UseRoutingMethod = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.VARIANT_BOOL)(30, 'UseRoutingMethod', ((1, 'bstrMethodGUID'),(1, 'bUse'),)))
    IFaxDevice.get_RingingNow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(31, 'get_RingingNow', ((1, 'pbRingingNow'),)))
    IFaxDevice.AnswerCall = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(32, 'AnswerCall', ()))
    win32more.System.Com.IDispatch
    return IFaxDevice
def _define_IFaxDeviceIds_head():
    class IFaxDeviceIds(win32more.System.Com.IDispatch_head):
        Guid = Guid('2f0f813f-4ce9-443e-8c-a1-73-8c-fa-ee-e1-49')
    return IFaxDeviceIds
def _define_IFaxDeviceIds():
    IFaxDeviceIds = win32more.Devices.Fax.IFaxDeviceIds_head
    IFaxDeviceIds.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(7, 'get__NewEnum', ((1, 'ppUnk'),)))
    IFaxDeviceIds.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Int32))(8, 'get_Item', ((1, 'lIndex'),(1, 'plDeviceId'),)))
    IFaxDeviceIds.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(9, 'get_Count', ((1, 'plCount'),)))
    IFaxDeviceIds.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(10, 'Add', ((1, 'lDeviceId'),)))
    IFaxDeviceIds.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(11, 'Remove', ((1, 'lIndex'),)))
    IFaxDeviceIds.SetOrder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32)(12, 'SetOrder', ((1, 'lDeviceId'),(1, 'lNewOrder'),)))
    win32more.System.Com.IDispatch
    return IFaxDeviceIds
def _define_IFaxDeviceProvider_head():
    class IFaxDeviceProvider(win32more.System.Com.IDispatch_head):
        Guid = Guid('290eac63-83ec-449c-84-17-f1-48-df-8c-68-2a')
    return IFaxDeviceProvider
def _define_IFaxDeviceProvider():
    IFaxDeviceProvider = win32more.Devices.Fax.IFaxDeviceProvider_head
    IFaxDeviceProvider.get_FriendlyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_FriendlyName', ((1, 'pbstrFriendlyName'),)))
    IFaxDeviceProvider.get_ImageName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(8, 'get_ImageName', ((1, 'pbstrImageName'),)))
    IFaxDeviceProvider.get_UniqueName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_UniqueName', ((1, 'pbstrUniqueName'),)))
    IFaxDeviceProvider.get_TapiProviderName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(10, 'get_TapiProviderName', ((1, 'pbstrTapiProviderName'),)))
    IFaxDeviceProvider.get_MajorVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(11, 'get_MajorVersion', ((1, 'plMajorVersion'),)))
    IFaxDeviceProvider.get_MinorVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(12, 'get_MinorVersion', ((1, 'plMinorVersion'),)))
    IFaxDeviceProvider.get_MajorBuild = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(13, 'get_MajorBuild', ((1, 'plMajorBuild'),)))
    IFaxDeviceProvider.get_MinorBuild = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(14, 'get_MinorBuild', ((1, 'plMinorBuild'),)))
    IFaxDeviceProvider.get_Debug = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(15, 'get_Debug', ((1, 'pbDebug'),)))
    IFaxDeviceProvider.get_Status = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_PROVIDER_STATUS_ENUM))(16, 'get_Status', ((1, 'pStatus'),)))
    IFaxDeviceProvider.get_InitErrorCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(17, 'get_InitErrorCode', ((1, 'plInitErrorCode'),)))
    IFaxDeviceProvider.get_DeviceIds = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(18, 'get_DeviceIds', ((1, 'pvDeviceIds'),)))
    win32more.System.Com.IDispatch
    return IFaxDeviceProvider
def _define_IFaxDeviceProviders_head():
    class IFaxDeviceProviders(win32more.System.Com.IDispatch_head):
        Guid = Guid('9fb76f62-4c7e-43a5-b6-fd-50-28-93-f7-e1-3e')
    return IFaxDeviceProviders
def _define_IFaxDeviceProviders():
    IFaxDeviceProviders = win32more.Devices.Fax.IFaxDeviceProviders_head
    IFaxDeviceProviders.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(7, 'get__NewEnum', ((1, 'ppUnk'),)))
    IFaxDeviceProviders.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.Devices.Fax.IFaxDeviceProvider_head))(8, 'get_Item', ((1, 'vIndex'),(1, 'pFaxDeviceProvider'),)))
    IFaxDeviceProviders.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(9, 'get_Count', ((1, 'plCount'),)))
    win32more.System.Com.IDispatch
    return IFaxDeviceProviders
def _define_IFaxDevices_head():
    class IFaxDevices(win32more.System.Com.IDispatch_head):
        Guid = Guid('9e46783e-f34f-482e-a3-60-04-16-be-cb-bd-96')
    return IFaxDevices
def _define_IFaxDevices():
    IFaxDevices = win32more.Devices.Fax.IFaxDevices_head
    IFaxDevices.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(7, 'get__NewEnum', ((1, 'ppUnk'),)))
    IFaxDevices.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.Devices.Fax.IFaxDevice_head))(8, 'get_Item', ((1, 'vIndex'),(1, 'pFaxDevice'),)))
    IFaxDevices.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(9, 'get_Count', ((1, 'plCount'),)))
    IFaxDevices.get_ItemById = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Devices.Fax.IFaxDevice_head))(10, 'get_ItemById', ((1, 'lId'),(1, 'ppFaxDevice'),)))
    win32more.System.Com.IDispatch
    return IFaxDevices
def _define_IFaxDocument_head():
    class IFaxDocument(win32more.System.Com.IDispatch_head):
        Guid = Guid('b207a246-09e3-4a4e-a7-dc-fe-a3-1d-29-45-8f')
    return IFaxDocument
def _define_IFaxDocument():
    IFaxDocument = win32more.Devices.Fax.IFaxDocument_head
    IFaxDocument.get_Body = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_Body', ((1, 'pbstrBody'),)))
    IFaxDocument.put_Body = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(8, 'put_Body', ((1, 'bstrBody'),)))
    IFaxDocument.get_Sender = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxSender_head))(9, 'get_Sender', ((1, 'ppFaxSender'),)))
    IFaxDocument.get_Recipients = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxRecipients_head))(10, 'get_Recipients', ((1, 'ppFaxRecipients'),)))
    IFaxDocument.get_CoverPage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(11, 'get_CoverPage', ((1, 'pbstrCoverPage'),)))
    IFaxDocument.put_CoverPage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(12, 'put_CoverPage', ((1, 'bstrCoverPage'),)))
    IFaxDocument.get_Subject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(13, 'get_Subject', ((1, 'pbstrSubject'),)))
    IFaxDocument.put_Subject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(14, 'put_Subject', ((1, 'bstrSubject'),)))
    IFaxDocument.get_Note = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(15, 'get_Note', ((1, 'pbstrNote'),)))
    IFaxDocument.put_Note = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(16, 'put_Note', ((1, 'bstrNote'),)))
    IFaxDocument.get_ScheduleTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(17, 'get_ScheduleTime', ((1, 'pdateScheduleTime'),)))
    IFaxDocument.put_ScheduleTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double)(18, 'put_ScheduleTime', ((1, 'dateScheduleTime'),)))
    IFaxDocument.get_ReceiptAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(19, 'get_ReceiptAddress', ((1, 'pbstrReceiptAddress'),)))
    IFaxDocument.put_ReceiptAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(20, 'put_ReceiptAddress', ((1, 'bstrReceiptAddress'),)))
    IFaxDocument.get_DocumentName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(21, 'get_DocumentName', ((1, 'pbstrDocumentName'),)))
    IFaxDocument.put_DocumentName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(22, 'put_DocumentName', ((1, 'bstrDocumentName'),)))
    IFaxDocument.get_CallHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(23, 'get_CallHandle', ((1, 'plCallHandle'),)))
    IFaxDocument.put_CallHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(24, 'put_CallHandle', ((1, 'lCallHandle'),)))
    IFaxDocument.get_CoverPageType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_COVERPAGE_TYPE_ENUM))(25, 'get_CoverPageType', ((1, 'pCoverPageType'),)))
    IFaxDocument.put_CoverPageType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.FAX_COVERPAGE_TYPE_ENUM)(26, 'put_CoverPageType', ((1, 'CoverPageType'),)))
    IFaxDocument.get_ScheduleType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_SCHEDULE_TYPE_ENUM))(27, 'get_ScheduleType', ((1, 'pScheduleType'),)))
    IFaxDocument.put_ScheduleType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.FAX_SCHEDULE_TYPE_ENUM)(28, 'put_ScheduleType', ((1, 'ScheduleType'),)))
    IFaxDocument.get_ReceiptType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_RECEIPT_TYPE_ENUM))(29, 'get_ReceiptType', ((1, 'pReceiptType'),)))
    IFaxDocument.put_ReceiptType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.FAX_RECEIPT_TYPE_ENUM)(30, 'put_ReceiptType', ((1, 'ReceiptType'),)))
    IFaxDocument.get_GroupBroadcastReceipts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(31, 'get_GroupBroadcastReceipts', ((1, 'pbUseGrouping'),)))
    IFaxDocument.put_GroupBroadcastReceipts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(32, 'put_GroupBroadcastReceipts', ((1, 'bUseGrouping'),)))
    IFaxDocument.get_Priority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_PRIORITY_TYPE_ENUM))(33, 'get_Priority', ((1, 'pPriority'),)))
    IFaxDocument.put_Priority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.FAX_PRIORITY_TYPE_ENUM)(34, 'put_Priority', ((1, 'Priority'),)))
    IFaxDocument.get_TapiConnection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDispatch_head))(35, 'get_TapiConnection', ((1, 'ppTapiConnection'),)))
    IFaxDocument.putref_TapiConnection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head)(36, 'putref_TapiConnection', ((1, 'pTapiConnection'),)))
    IFaxDocument.Submit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head))(37, 'Submit', ((1, 'bstrFaxServerName'),(1, 'pvFaxOutgoingJobIDs'),)))
    IFaxDocument.ConnectedSubmit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer_head,POINTER(win32more.System.Com.VARIANT_head))(38, 'ConnectedSubmit', ((1, 'pFaxServer'),(1, 'pvFaxOutgoingJobIDs'),)))
    IFaxDocument.get_AttachFaxToReceipt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(39, 'get_AttachFaxToReceipt', ((1, 'pbAttachFax'),)))
    IFaxDocument.put_AttachFaxToReceipt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(40, 'put_AttachFaxToReceipt', ((1, 'bAttachFax'),)))
    win32more.System.Com.IDispatch
    return IFaxDocument
def _define_IFaxDocument2_head():
    class IFaxDocument2(win32more.Devices.Fax.IFaxDocument_head):
        Guid = Guid('e1347661-f9ef-4d6d-b4-a5-c0-a0-68-b6-5c-ff')
    return IFaxDocument2
def _define_IFaxDocument2():
    IFaxDocument2 = win32more.Devices.Fax.IFaxDocument2_head
    IFaxDocument2.get_SubmissionId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(41, 'get_SubmissionId', ((1, 'pbstrSubmissionId'),)))
    IFaxDocument2.get_Bodies = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(42, 'get_Bodies', ((1, 'pvBodies'),)))
    IFaxDocument2.put_Bodies = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT)(43, 'put_Bodies', ((1, 'vBodies'),)))
    IFaxDocument2.Submit2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head),POINTER(Int32))(44, 'Submit2', ((1, 'bstrFaxServerName'),(1, 'pvFaxOutgoingJobIDs'),(1, 'plErrorBodyFile'),)))
    IFaxDocument2.ConnectedSubmit2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer_head,POINTER(win32more.System.Com.VARIANT_head),POINTER(Int32))(45, 'ConnectedSubmit2', ((1, 'pFaxServer'),(1, 'pvFaxOutgoingJobIDs'),(1, 'plErrorBodyFile'),)))
    win32more.Devices.Fax.IFaxDocument
    return IFaxDocument2
def _define_IFaxEventLogging_head():
    class IFaxEventLogging(win32more.System.Com.IDispatch_head):
        Guid = Guid('0880d965-20e8-42e4-8e-17-94-4f-19-2c-aa-d4')
    return IFaxEventLogging
def _define_IFaxEventLogging():
    IFaxEventLogging = win32more.Devices.Fax.IFaxEventLogging_head
    IFaxEventLogging.get_InitEventsLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_LOG_LEVEL_ENUM))(7, 'get_InitEventsLevel', ((1, 'pInitEventLevel'),)))
    IFaxEventLogging.put_InitEventsLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.FAX_LOG_LEVEL_ENUM)(8, 'put_InitEventsLevel', ((1, 'InitEventLevel'),)))
    IFaxEventLogging.get_InboundEventsLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_LOG_LEVEL_ENUM))(9, 'get_InboundEventsLevel', ((1, 'pInboundEventLevel'),)))
    IFaxEventLogging.put_InboundEventsLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.FAX_LOG_LEVEL_ENUM)(10, 'put_InboundEventsLevel', ((1, 'InboundEventLevel'),)))
    IFaxEventLogging.get_OutboundEventsLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_LOG_LEVEL_ENUM))(11, 'get_OutboundEventsLevel', ((1, 'pOutboundEventLevel'),)))
    IFaxEventLogging.put_OutboundEventsLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.FAX_LOG_LEVEL_ENUM)(12, 'put_OutboundEventsLevel', ((1, 'OutboundEventLevel'),)))
    IFaxEventLogging.get_GeneralEventsLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_LOG_LEVEL_ENUM))(13, 'get_GeneralEventsLevel', ((1, 'pGeneralEventLevel'),)))
    IFaxEventLogging.put_GeneralEventsLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.FAX_LOG_LEVEL_ENUM)(14, 'put_GeneralEventsLevel', ((1, 'GeneralEventLevel'),)))
    IFaxEventLogging.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(15, 'Refresh', ()))
    IFaxEventLogging.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(16, 'Save', ()))
    win32more.System.Com.IDispatch
    return IFaxEventLogging
def _define_IFaxFolders_head():
    class IFaxFolders(win32more.System.Com.IDispatch_head):
        Guid = Guid('dce3b2a8-a7ab-42bc-9d-0a-31-49-45-72-61-a0')
    return IFaxFolders
def _define_IFaxFolders():
    IFaxFolders = win32more.Devices.Fax.IFaxFolders_head
    IFaxFolders.get_OutgoingQueue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxOutgoingQueue_head))(7, 'get_OutgoingQueue', ((1, 'pFaxOutgoingQueue'),)))
    IFaxFolders.get_IncomingQueue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxIncomingQueue_head))(8, 'get_IncomingQueue', ((1, 'pFaxIncomingQueue'),)))
    IFaxFolders.get_IncomingArchive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxIncomingArchive_head))(9, 'get_IncomingArchive', ((1, 'pFaxIncomingArchive'),)))
    IFaxFolders.get_OutgoingArchive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxOutgoingArchive_head))(10, 'get_OutgoingArchive', ((1, 'pFaxOutgoingArchive'),)))
    win32more.System.Com.IDispatch
    return IFaxFolders
def _define_IFaxInboundRouting_head():
    class IFaxInboundRouting(win32more.System.Com.IDispatch_head):
        Guid = Guid('8148c20f-9d52-45b1-bf-96-38-fc-12-71-35-27')
    return IFaxInboundRouting
def _define_IFaxInboundRouting():
    IFaxInboundRouting = win32more.Devices.Fax.IFaxInboundRouting_head
    IFaxInboundRouting.GetExtensions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxInboundRoutingExtensions_head))(7, 'GetExtensions', ((1, 'pFaxInboundRoutingExtensions'),)))
    IFaxInboundRouting.GetMethods = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxInboundRoutingMethods_head))(8, 'GetMethods', ((1, 'pFaxInboundRoutingMethods'),)))
    win32more.System.Com.IDispatch
    return IFaxInboundRouting
def _define_IFaxInboundRoutingExtension_head():
    class IFaxInboundRoutingExtension(win32more.System.Com.IDispatch_head):
        Guid = Guid('885b5e08-c26c-4ef9-af-83-51-58-0a-75-0b-e1')
    return IFaxInboundRoutingExtension
def _define_IFaxInboundRoutingExtension():
    IFaxInboundRoutingExtension = win32more.Devices.Fax.IFaxInboundRoutingExtension_head
    IFaxInboundRoutingExtension.get_FriendlyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_FriendlyName', ((1, 'pbstrFriendlyName'),)))
    IFaxInboundRoutingExtension.get_ImageName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(8, 'get_ImageName', ((1, 'pbstrImageName'),)))
    IFaxInboundRoutingExtension.get_UniqueName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_UniqueName', ((1, 'pbstrUniqueName'),)))
    IFaxInboundRoutingExtension.get_MajorVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(10, 'get_MajorVersion', ((1, 'plMajorVersion'),)))
    IFaxInboundRoutingExtension.get_MinorVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(11, 'get_MinorVersion', ((1, 'plMinorVersion'),)))
    IFaxInboundRoutingExtension.get_MajorBuild = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(12, 'get_MajorBuild', ((1, 'plMajorBuild'),)))
    IFaxInboundRoutingExtension.get_MinorBuild = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(13, 'get_MinorBuild', ((1, 'plMinorBuild'),)))
    IFaxInboundRoutingExtension.get_Debug = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(14, 'get_Debug', ((1, 'pbDebug'),)))
    IFaxInboundRoutingExtension.get_Status = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_PROVIDER_STATUS_ENUM))(15, 'get_Status', ((1, 'pStatus'),)))
    IFaxInboundRoutingExtension.get_InitErrorCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(16, 'get_InitErrorCode', ((1, 'plInitErrorCode'),)))
    IFaxInboundRoutingExtension.get_Methods = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(17, 'get_Methods', ((1, 'pvMethods'),)))
    win32more.System.Com.IDispatch
    return IFaxInboundRoutingExtension
def _define_IFaxInboundRoutingExtensions_head():
    class IFaxInboundRoutingExtensions(win32more.System.Com.IDispatch_head):
        Guid = Guid('2f6c9673-7b26-42de-8e-b0-91-5d-cd-2a-4f-4c')
    return IFaxInboundRoutingExtensions
def _define_IFaxInboundRoutingExtensions():
    IFaxInboundRoutingExtensions = win32more.Devices.Fax.IFaxInboundRoutingExtensions_head
    IFaxInboundRoutingExtensions.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(7, 'get__NewEnum', ((1, 'ppUnk'),)))
    IFaxInboundRoutingExtensions.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.Devices.Fax.IFaxInboundRoutingExtension_head))(8, 'get_Item', ((1, 'vIndex'),(1, 'pFaxInboundRoutingExtension'),)))
    IFaxInboundRoutingExtensions.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(9, 'get_Count', ((1, 'plCount'),)))
    win32more.System.Com.IDispatch
    return IFaxInboundRoutingExtensions
def _define_IFaxInboundRoutingMethod_head():
    class IFaxInboundRoutingMethod(win32more.System.Com.IDispatch_head):
        Guid = Guid('45700061-ad9d-4776-a8-c4-64-06-54-92-cf-4b')
    return IFaxInboundRoutingMethod
def _define_IFaxInboundRoutingMethod():
    IFaxInboundRoutingMethod = win32more.Devices.Fax.IFaxInboundRoutingMethod_head
    IFaxInboundRoutingMethod.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_Name', ((1, 'pbstrName'),)))
    IFaxInboundRoutingMethod.get_GUID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(8, 'get_GUID', ((1, 'pbstrGUID'),)))
    IFaxInboundRoutingMethod.get_FunctionName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_FunctionName', ((1, 'pbstrFunctionName'),)))
    IFaxInboundRoutingMethod.get_ExtensionFriendlyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(10, 'get_ExtensionFriendlyName', ((1, 'pbstrExtensionFriendlyName'),)))
    IFaxInboundRoutingMethod.get_ExtensionImageName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(11, 'get_ExtensionImageName', ((1, 'pbstrExtensionImageName'),)))
    IFaxInboundRoutingMethod.get_Priority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(12, 'get_Priority', ((1, 'plPriority'),)))
    IFaxInboundRoutingMethod.put_Priority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(13, 'put_Priority', ((1, 'lPriority'),)))
    IFaxInboundRoutingMethod.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(14, 'Refresh', ()))
    IFaxInboundRoutingMethod.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(15, 'Save', ()))
    win32more.System.Com.IDispatch
    return IFaxInboundRoutingMethod
def _define_IFaxInboundRoutingMethods_head():
    class IFaxInboundRoutingMethods(win32more.System.Com.IDispatch_head):
        Guid = Guid('783fca10-8908-4473-9d-69-f6-7f-be-a0-c6-b9')
    return IFaxInboundRoutingMethods
def _define_IFaxInboundRoutingMethods():
    IFaxInboundRoutingMethods = win32more.Devices.Fax.IFaxInboundRoutingMethods_head
    IFaxInboundRoutingMethods.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(7, 'get__NewEnum', ((1, 'ppUnk'),)))
    IFaxInboundRoutingMethods.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.Devices.Fax.IFaxInboundRoutingMethod_head))(8, 'get_Item', ((1, 'vIndex'),(1, 'pFaxInboundRoutingMethod'),)))
    IFaxInboundRoutingMethods.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(9, 'get_Count', ((1, 'plCount'),)))
    win32more.System.Com.IDispatch
    return IFaxInboundRoutingMethods
def _define_IFaxIncomingArchive_head():
    class IFaxIncomingArchive(win32more.System.Com.IDispatch_head):
        Guid = Guid('76062cc7-f714-4fbd-aa-06-ed-6e-4a-4b-70-f3')
    return IFaxIncomingArchive
def _define_IFaxIncomingArchive():
    IFaxIncomingArchive = win32more.Devices.Fax.IFaxIncomingArchive_head
    IFaxIncomingArchive.get_UseArchive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(7, 'get_UseArchive', ((1, 'pbUseArchive'),)))
    IFaxIncomingArchive.put_UseArchive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(8, 'put_UseArchive', ((1, 'bUseArchive'),)))
    IFaxIncomingArchive.get_ArchiveFolder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_ArchiveFolder', ((1, 'pbstrArchiveFolder'),)))
    IFaxIncomingArchive.put_ArchiveFolder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(10, 'put_ArchiveFolder', ((1, 'bstrArchiveFolder'),)))
    IFaxIncomingArchive.get_SizeQuotaWarning = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(11, 'get_SizeQuotaWarning', ((1, 'pbSizeQuotaWarning'),)))
    IFaxIncomingArchive.put_SizeQuotaWarning = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(12, 'put_SizeQuotaWarning', ((1, 'bSizeQuotaWarning'),)))
    IFaxIncomingArchive.get_HighQuotaWaterMark = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(13, 'get_HighQuotaWaterMark', ((1, 'plHighQuotaWaterMark'),)))
    IFaxIncomingArchive.put_HighQuotaWaterMark = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(14, 'put_HighQuotaWaterMark', ((1, 'lHighQuotaWaterMark'),)))
    IFaxIncomingArchive.get_LowQuotaWaterMark = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(15, 'get_LowQuotaWaterMark', ((1, 'plLowQuotaWaterMark'),)))
    IFaxIncomingArchive.put_LowQuotaWaterMark = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(16, 'put_LowQuotaWaterMark', ((1, 'lLowQuotaWaterMark'),)))
    IFaxIncomingArchive.get_AgeLimit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(17, 'get_AgeLimit', ((1, 'plAgeLimit'),)))
    IFaxIncomingArchive.put_AgeLimit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(18, 'put_AgeLimit', ((1, 'lAgeLimit'),)))
    IFaxIncomingArchive.get_SizeLow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(19, 'get_SizeLow', ((1, 'plSizeLow'),)))
    IFaxIncomingArchive.get_SizeHigh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(20, 'get_SizeHigh', ((1, 'plSizeHigh'),)))
    IFaxIncomingArchive.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(21, 'Refresh', ()))
    IFaxIncomingArchive.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(22, 'Save', ()))
    IFaxIncomingArchive.GetMessages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Devices.Fax.IFaxIncomingMessageIterator_head))(23, 'GetMessages', ((1, 'lPrefetchSize'),(1, 'pFaxIncomingMessageIterator'),)))
    IFaxIncomingArchive.GetMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Devices.Fax.IFaxIncomingMessage_head))(24, 'GetMessage', ((1, 'bstrMessageId'),(1, 'pFaxIncomingMessage'),)))
    win32more.System.Com.IDispatch
    return IFaxIncomingArchive
def _define_IFaxIncomingJob_head():
    class IFaxIncomingJob(win32more.System.Com.IDispatch_head):
        Guid = Guid('207529e6-654a-4916-9f-88-4d-23-2e-e8-a1-07')
    return IFaxIncomingJob
def _define_IFaxIncomingJob():
    IFaxIncomingJob = win32more.Devices.Fax.IFaxIncomingJob_head
    IFaxIncomingJob.get_Size = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_Size', ((1, 'plSize'),)))
    IFaxIncomingJob.get_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(8, 'get_Id', ((1, 'pbstrId'),)))
    IFaxIncomingJob.get_CurrentPage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(9, 'get_CurrentPage', ((1, 'plCurrentPage'),)))
    IFaxIncomingJob.get_DeviceId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(10, 'get_DeviceId', ((1, 'plDeviceId'),)))
    IFaxIncomingJob.get_Status = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_JOB_STATUS_ENUM))(11, 'get_Status', ((1, 'pStatus'),)))
    IFaxIncomingJob.get_ExtendedStatusCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_JOB_EXTENDED_STATUS_ENUM))(12, 'get_ExtendedStatusCode', ((1, 'pExtendedStatusCode'),)))
    IFaxIncomingJob.get_ExtendedStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(13, 'get_ExtendedStatus', ((1, 'pbstrExtendedStatus'),)))
    IFaxIncomingJob.get_AvailableOperations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_JOB_OPERATIONS_ENUM))(14, 'get_AvailableOperations', ((1, 'pAvailableOperations'),)))
    IFaxIncomingJob.get_Retries = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(15, 'get_Retries', ((1, 'plRetries'),)))
    IFaxIncomingJob.get_TransmissionStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(16, 'get_TransmissionStart', ((1, 'pdateTransmissionStart'),)))
    IFaxIncomingJob.get_TransmissionEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(17, 'get_TransmissionEnd', ((1, 'pdateTransmissionEnd'),)))
    IFaxIncomingJob.get_CSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(18, 'get_CSID', ((1, 'pbstrCSID'),)))
    IFaxIncomingJob.get_TSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(19, 'get_TSID', ((1, 'pbstrTSID'),)))
    IFaxIncomingJob.get_CallerId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(20, 'get_CallerId', ((1, 'pbstrCallerId'),)))
    IFaxIncomingJob.get_RoutingInformation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(21, 'get_RoutingInformation', ((1, 'pbstrRoutingInformation'),)))
    IFaxIncomingJob.get_JobType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_JOB_TYPE_ENUM))(22, 'get_JobType', ((1, 'pJobType'),)))
    IFaxIncomingJob.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(23, 'Cancel', ()))
    IFaxIncomingJob.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(24, 'Refresh', ()))
    IFaxIncomingJob.CopyTiff = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(25, 'CopyTiff', ((1, 'bstrTiffPath'),)))
    win32more.System.Com.IDispatch
    return IFaxIncomingJob
def _define_IFaxIncomingJobs_head():
    class IFaxIncomingJobs(win32more.System.Com.IDispatch_head):
        Guid = Guid('011f04e9-4fd6-4c23-95-13-b6-b6-6b-b2-6b-e9')
    return IFaxIncomingJobs
def _define_IFaxIncomingJobs():
    IFaxIncomingJobs = win32more.Devices.Fax.IFaxIncomingJobs_head
    IFaxIncomingJobs.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(7, 'get__NewEnum', ((1, 'ppUnk'),)))
    IFaxIncomingJobs.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.Devices.Fax.IFaxIncomingJob_head))(8, 'get_Item', ((1, 'vIndex'),(1, 'pFaxIncomingJob'),)))
    IFaxIncomingJobs.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(9, 'get_Count', ((1, 'plCount'),)))
    win32more.System.Com.IDispatch
    return IFaxIncomingJobs
def _define_IFaxIncomingMessage_head():
    class IFaxIncomingMessage(win32more.System.Com.IDispatch_head):
        Guid = Guid('7cab88fa-2ef9-4851-b2-f3-1d-14-8f-ed-84-47')
    return IFaxIncomingMessage
def _define_IFaxIncomingMessage():
    IFaxIncomingMessage = win32more.Devices.Fax.IFaxIncomingMessage_head
    IFaxIncomingMessage.get_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_Id', ((1, 'pbstrId'),)))
    IFaxIncomingMessage.get_Pages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(8, 'get_Pages', ((1, 'plPages'),)))
    IFaxIncomingMessage.get_Size = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(9, 'get_Size', ((1, 'plSize'),)))
    IFaxIncomingMessage.get_DeviceName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(10, 'get_DeviceName', ((1, 'pbstrDeviceName'),)))
    IFaxIncomingMessage.get_Retries = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(11, 'get_Retries', ((1, 'plRetries'),)))
    IFaxIncomingMessage.get_TransmissionStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(12, 'get_TransmissionStart', ((1, 'pdateTransmissionStart'),)))
    IFaxIncomingMessage.get_TransmissionEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(13, 'get_TransmissionEnd', ((1, 'pdateTransmissionEnd'),)))
    IFaxIncomingMessage.get_CSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(14, 'get_CSID', ((1, 'pbstrCSID'),)))
    IFaxIncomingMessage.get_TSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(15, 'get_TSID', ((1, 'pbstrTSID'),)))
    IFaxIncomingMessage.get_CallerId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(16, 'get_CallerId', ((1, 'pbstrCallerId'),)))
    IFaxIncomingMessage.get_RoutingInformation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(17, 'get_RoutingInformation', ((1, 'pbstrRoutingInformation'),)))
    IFaxIncomingMessage.CopyTiff = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(18, 'CopyTiff', ((1, 'bstrTiffPath'),)))
    IFaxIncomingMessage.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(19, 'Delete', ()))
    win32more.System.Com.IDispatch
    return IFaxIncomingMessage
def _define_IFaxIncomingMessage2_head():
    class IFaxIncomingMessage2(win32more.Devices.Fax.IFaxIncomingMessage_head):
        Guid = Guid('f9208503-e2bc-48f3-9e-c0-e6-23-6f-9b-50-9a')
    return IFaxIncomingMessage2
def _define_IFaxIncomingMessage2():
    IFaxIncomingMessage2 = win32more.Devices.Fax.IFaxIncomingMessage2_head
    IFaxIncomingMessage2.get_Subject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(20, 'get_Subject', ((1, 'pbstrSubject'),)))
    IFaxIncomingMessage2.put_Subject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(21, 'put_Subject', ((1, 'bstrSubject'),)))
    IFaxIncomingMessage2.get_SenderName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(22, 'get_SenderName', ((1, 'pbstrSenderName'),)))
    IFaxIncomingMessage2.put_SenderName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(23, 'put_SenderName', ((1, 'bstrSenderName'),)))
    IFaxIncomingMessage2.get_SenderFaxNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(24, 'get_SenderFaxNumber', ((1, 'pbstrSenderFaxNumber'),)))
    IFaxIncomingMessage2.put_SenderFaxNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(25, 'put_SenderFaxNumber', ((1, 'bstrSenderFaxNumber'),)))
    IFaxIncomingMessage2.get_HasCoverPage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(26, 'get_HasCoverPage', ((1, 'pbHasCoverPage'),)))
    IFaxIncomingMessage2.put_HasCoverPage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(27, 'put_HasCoverPage', ((1, 'bHasCoverPage'),)))
    IFaxIncomingMessage2.get_Recipients = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(28, 'get_Recipients', ((1, 'pbstrRecipients'),)))
    IFaxIncomingMessage2.put_Recipients = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(29, 'put_Recipients', ((1, 'bstrRecipients'),)))
    IFaxIncomingMessage2.get_WasReAssigned = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(30, 'get_WasReAssigned', ((1, 'pbWasReAssigned'),)))
    IFaxIncomingMessage2.get_Read = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(31, 'get_Read', ((1, 'pbRead'),)))
    IFaxIncomingMessage2.put_Read = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(32, 'put_Read', ((1, 'bRead'),)))
    IFaxIncomingMessage2.ReAssign = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(33, 'ReAssign', ()))
    IFaxIncomingMessage2.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(34, 'Save', ()))
    IFaxIncomingMessage2.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(35, 'Refresh', ()))
    win32more.Devices.Fax.IFaxIncomingMessage
    return IFaxIncomingMessage2
def _define_IFaxIncomingMessageIterator_head():
    class IFaxIncomingMessageIterator(win32more.System.Com.IDispatch_head):
        Guid = Guid('fd73ecc4-6f06-4f52-82-a8-f7-ba-06-ae-31-08')
    return IFaxIncomingMessageIterator
def _define_IFaxIncomingMessageIterator():
    IFaxIncomingMessageIterator = win32more.Devices.Fax.IFaxIncomingMessageIterator_head
    IFaxIncomingMessageIterator.get_Message = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxIncomingMessage_head))(7, 'get_Message', ((1, 'pFaxIncomingMessage'),)))
    IFaxIncomingMessageIterator.get_PrefetchSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(8, 'get_PrefetchSize', ((1, 'plPrefetchSize'),)))
    IFaxIncomingMessageIterator.put_PrefetchSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(9, 'put_PrefetchSize', ((1, 'lPrefetchSize'),)))
    IFaxIncomingMessageIterator.get_AtEOF = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(10, 'get_AtEOF', ((1, 'pbEOF'),)))
    IFaxIncomingMessageIterator.MoveFirst = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(11, 'MoveFirst', ()))
    IFaxIncomingMessageIterator.MoveNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(12, 'MoveNext', ()))
    win32more.System.Com.IDispatch
    return IFaxIncomingMessageIterator
def _define_IFaxIncomingQueue_head():
    class IFaxIncomingQueue(win32more.System.Com.IDispatch_head):
        Guid = Guid('902e64ef-8fd8-4b75-97-25-60-14-df-16-15-45')
    return IFaxIncomingQueue
def _define_IFaxIncomingQueue():
    IFaxIncomingQueue = win32more.Devices.Fax.IFaxIncomingQueue_head
    IFaxIncomingQueue.get_Blocked = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(7, 'get_Blocked', ((1, 'pbBlocked'),)))
    IFaxIncomingQueue.put_Blocked = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(8, 'put_Blocked', ((1, 'bBlocked'),)))
    IFaxIncomingQueue.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(9, 'Refresh', ()))
    IFaxIncomingQueue.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(10, 'Save', ()))
    IFaxIncomingQueue.GetJobs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxIncomingJobs_head))(11, 'GetJobs', ((1, 'pFaxIncomingJobs'),)))
    IFaxIncomingQueue.GetJob = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Devices.Fax.IFaxIncomingJob_head))(12, 'GetJob', ((1, 'bstrJobId'),(1, 'pFaxIncomingJob'),)))
    win32more.System.Com.IDispatch
    return IFaxIncomingQueue
def _define_IFaxJobStatus_head():
    class IFaxJobStatus(win32more.System.Com.IDispatch_head):
        Guid = Guid('8b86f485-fd7f-4824-88-6b-40-c5-ca-a6-17-cc')
    return IFaxJobStatus
def _define_IFaxJobStatus():
    IFaxJobStatus = win32more.Devices.Fax.IFaxJobStatus_head
    IFaxJobStatus.get_Status = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_JOB_STATUS_ENUM))(7, 'get_Status', ((1, 'pStatus'),)))
    IFaxJobStatus.get_Pages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(8, 'get_Pages', ((1, 'plPages'),)))
    IFaxJobStatus.get_Size = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(9, 'get_Size', ((1, 'plSize'),)))
    IFaxJobStatus.get_CurrentPage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(10, 'get_CurrentPage', ((1, 'plCurrentPage'),)))
    IFaxJobStatus.get_DeviceId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(11, 'get_DeviceId', ((1, 'plDeviceId'),)))
    IFaxJobStatus.get_CSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(12, 'get_CSID', ((1, 'pbstrCSID'),)))
    IFaxJobStatus.get_TSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(13, 'get_TSID', ((1, 'pbstrTSID'),)))
    IFaxJobStatus.get_ExtendedStatusCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_JOB_EXTENDED_STATUS_ENUM))(14, 'get_ExtendedStatusCode', ((1, 'pExtendedStatusCode'),)))
    IFaxJobStatus.get_ExtendedStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(15, 'get_ExtendedStatus', ((1, 'pbstrExtendedStatus'),)))
    IFaxJobStatus.get_AvailableOperations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_JOB_OPERATIONS_ENUM))(16, 'get_AvailableOperations', ((1, 'pAvailableOperations'),)))
    IFaxJobStatus.get_Retries = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(17, 'get_Retries', ((1, 'plRetries'),)))
    IFaxJobStatus.get_JobType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_JOB_TYPE_ENUM))(18, 'get_JobType', ((1, 'pJobType'),)))
    IFaxJobStatus.get_ScheduledTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(19, 'get_ScheduledTime', ((1, 'pdateScheduledTime'),)))
    IFaxJobStatus.get_TransmissionStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(20, 'get_TransmissionStart', ((1, 'pdateTransmissionStart'),)))
    IFaxJobStatus.get_TransmissionEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(21, 'get_TransmissionEnd', ((1, 'pdateTransmissionEnd'),)))
    IFaxJobStatus.get_CallerId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(22, 'get_CallerId', ((1, 'pbstrCallerId'),)))
    IFaxJobStatus.get_RoutingInformation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(23, 'get_RoutingInformation', ((1, 'pbstrRoutingInformation'),)))
    win32more.System.Com.IDispatch
    return IFaxJobStatus
def _define_IFaxLoggingOptions_head():
    class IFaxLoggingOptions(win32more.System.Com.IDispatch_head):
        Guid = Guid('34e64fb9-6b31-4d32-8b-27-d2-86-c0-c3-36-06')
    return IFaxLoggingOptions
def _define_IFaxLoggingOptions():
    IFaxLoggingOptions = win32more.Devices.Fax.IFaxLoggingOptions_head
    IFaxLoggingOptions.get_EventLogging = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxEventLogging_head))(7, 'get_EventLogging', ((1, 'pFaxEventLogging'),)))
    IFaxLoggingOptions.get_ActivityLogging = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxActivityLogging_head))(8, 'get_ActivityLogging', ((1, 'pFaxActivityLogging'),)))
    win32more.System.Com.IDispatch
    return IFaxLoggingOptions
def _define_IFaxOutboundRouting_head():
    class IFaxOutboundRouting(win32more.System.Com.IDispatch_head):
        Guid = Guid('25dc05a4-9909-41bd-a9-5b-7e-5d-1d-ec-1d-43')
    return IFaxOutboundRouting
def _define_IFaxOutboundRouting():
    IFaxOutboundRouting = win32more.Devices.Fax.IFaxOutboundRouting_head
    IFaxOutboundRouting.GetGroups = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxOutboundRoutingGroups_head))(7, 'GetGroups', ((1, 'pFaxOutboundRoutingGroups'),)))
    IFaxOutboundRouting.GetRules = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxOutboundRoutingRules_head))(8, 'GetRules', ((1, 'pFaxOutboundRoutingRules'),)))
    win32more.System.Com.IDispatch
    return IFaxOutboundRouting
def _define_IFaxOutboundRoutingGroup_head():
    class IFaxOutboundRoutingGroup(win32more.System.Com.IDispatch_head):
        Guid = Guid('ca6289a1-7e25-4f87-9a-0b-93-36-57-34-96-2c')
    return IFaxOutboundRoutingGroup
def _define_IFaxOutboundRoutingGroup():
    IFaxOutboundRoutingGroup = win32more.Devices.Fax.IFaxOutboundRoutingGroup_head
    IFaxOutboundRoutingGroup.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_Name', ((1, 'pbstrName'),)))
    IFaxOutboundRoutingGroup.get_Status = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_GROUP_STATUS_ENUM))(8, 'get_Status', ((1, 'pStatus'),)))
    IFaxOutboundRoutingGroup.get_DeviceIds = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxDeviceIds_head))(9, 'get_DeviceIds', ((1, 'pFaxDeviceIds'),)))
    win32more.System.Com.IDispatch
    return IFaxOutboundRoutingGroup
def _define_IFaxOutboundRoutingGroups_head():
    class IFaxOutboundRoutingGroups(win32more.System.Com.IDispatch_head):
        Guid = Guid('235cbef7-c2de-4bfd-b8-da-75-09-7c-82-c8-7f')
    return IFaxOutboundRoutingGroups
def _define_IFaxOutboundRoutingGroups():
    IFaxOutboundRoutingGroups = win32more.Devices.Fax.IFaxOutboundRoutingGroups_head
    IFaxOutboundRoutingGroups.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(7, 'get__NewEnum', ((1, 'ppUnk'),)))
    IFaxOutboundRoutingGroups.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.Devices.Fax.IFaxOutboundRoutingGroup_head))(8, 'get_Item', ((1, 'vIndex'),(1, 'pFaxOutboundRoutingGroup'),)))
    IFaxOutboundRoutingGroups.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(9, 'get_Count', ((1, 'plCount'),)))
    IFaxOutboundRoutingGroups.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Devices.Fax.IFaxOutboundRoutingGroup_head))(10, 'Add', ((1, 'bstrName'),(1, 'pFaxOutboundRoutingGroup'),)))
    IFaxOutboundRoutingGroups.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT)(11, 'Remove', ((1, 'vIndex'),)))
    win32more.System.Com.IDispatch
    return IFaxOutboundRoutingGroups
def _define_IFaxOutboundRoutingRule_head():
    class IFaxOutboundRoutingRule(win32more.System.Com.IDispatch_head):
        Guid = Guid('e1f795d5-07c2-469f-b0-27-ac-ac-c2-32-19-da')
    return IFaxOutboundRoutingRule
def _define_IFaxOutboundRoutingRule():
    IFaxOutboundRoutingRule = win32more.Devices.Fax.IFaxOutboundRoutingRule_head
    IFaxOutboundRoutingRule.get_CountryCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_CountryCode', ((1, 'plCountryCode'),)))
    IFaxOutboundRoutingRule.get_AreaCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(8, 'get_AreaCode', ((1, 'plAreaCode'),)))
    IFaxOutboundRoutingRule.get_Status = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_RULE_STATUS_ENUM))(9, 'get_Status', ((1, 'pStatus'),)))
    IFaxOutboundRoutingRule.get_UseDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(10, 'get_UseDevice', ((1, 'pbUseDevice'),)))
    IFaxOutboundRoutingRule.put_UseDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(11, 'put_UseDevice', ((1, 'bUseDevice'),)))
    IFaxOutboundRoutingRule.get_DeviceId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(12, 'get_DeviceId', ((1, 'plDeviceId'),)))
    IFaxOutboundRoutingRule.put_DeviceId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(13, 'put_DeviceId', ((1, 'DeviceId'),)))
    IFaxOutboundRoutingRule.get_GroupName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(14, 'get_GroupName', ((1, 'pbstrGroupName'),)))
    IFaxOutboundRoutingRule.put_GroupName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(15, 'put_GroupName', ((1, 'bstrGroupName'),)))
    IFaxOutboundRoutingRule.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(16, 'Refresh', ()))
    IFaxOutboundRoutingRule.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(17, 'Save', ()))
    win32more.System.Com.IDispatch
    return IFaxOutboundRoutingRule
def _define_IFaxOutboundRoutingRules_head():
    class IFaxOutboundRoutingRules(win32more.System.Com.IDispatch_head):
        Guid = Guid('dcefa1e7-ae7d-4ed6-85-21-36-9e-dc-ca-51-20')
    return IFaxOutboundRoutingRules
def _define_IFaxOutboundRoutingRules():
    IFaxOutboundRoutingRules = win32more.Devices.Fax.IFaxOutboundRoutingRules_head
    IFaxOutboundRoutingRules.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(7, 'get__NewEnum', ((1, 'ppUnk'),)))
    IFaxOutboundRoutingRules.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Devices.Fax.IFaxOutboundRoutingRule_head))(8, 'get_Item', ((1, 'lIndex'),(1, 'pFaxOutboundRoutingRule'),)))
    IFaxOutboundRoutingRules.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(9, 'get_Count', ((1, 'plCount'),)))
    IFaxOutboundRoutingRules.ItemByCountryAndArea = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(win32more.Devices.Fax.IFaxOutboundRoutingRule_head))(10, 'ItemByCountryAndArea', ((1, 'lCountryCode'),(1, 'lAreaCode'),(1, 'pFaxOutboundRoutingRule'),)))
    IFaxOutboundRoutingRules.RemoveByCountryAndArea = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32)(11, 'RemoveByCountryAndArea', ((1, 'lCountryCode'),(1, 'lAreaCode'),)))
    IFaxOutboundRoutingRules.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(12, 'Remove', ((1, 'lIndex'),)))
    IFaxOutboundRoutingRules.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,win32more.Foundation.VARIANT_BOOL,win32more.Foundation.BSTR,Int32,POINTER(win32more.Devices.Fax.IFaxOutboundRoutingRule_head))(13, 'Add', ((1, 'lCountryCode'),(1, 'lAreaCode'),(1, 'bUseDevice'),(1, 'bstrGroupName'),(1, 'lDeviceId'),(1, 'pFaxOutboundRoutingRule'),)))
    win32more.System.Com.IDispatch
    return IFaxOutboundRoutingRules
def _define_IFaxOutgoingArchive_head():
    class IFaxOutgoingArchive(win32more.System.Com.IDispatch_head):
        Guid = Guid('c9c28f40-8d80-4e53-81-0f-9a-79-91-9b-49-fd')
    return IFaxOutgoingArchive
def _define_IFaxOutgoingArchive():
    IFaxOutgoingArchive = win32more.Devices.Fax.IFaxOutgoingArchive_head
    IFaxOutgoingArchive.get_UseArchive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(7, 'get_UseArchive', ((1, 'pbUseArchive'),)))
    IFaxOutgoingArchive.put_UseArchive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(8, 'put_UseArchive', ((1, 'bUseArchive'),)))
    IFaxOutgoingArchive.get_ArchiveFolder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_ArchiveFolder', ((1, 'pbstrArchiveFolder'),)))
    IFaxOutgoingArchive.put_ArchiveFolder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(10, 'put_ArchiveFolder', ((1, 'bstrArchiveFolder'),)))
    IFaxOutgoingArchive.get_SizeQuotaWarning = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(11, 'get_SizeQuotaWarning', ((1, 'pbSizeQuotaWarning'),)))
    IFaxOutgoingArchive.put_SizeQuotaWarning = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(12, 'put_SizeQuotaWarning', ((1, 'bSizeQuotaWarning'),)))
    IFaxOutgoingArchive.get_HighQuotaWaterMark = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(13, 'get_HighQuotaWaterMark', ((1, 'plHighQuotaWaterMark'),)))
    IFaxOutgoingArchive.put_HighQuotaWaterMark = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(14, 'put_HighQuotaWaterMark', ((1, 'lHighQuotaWaterMark'),)))
    IFaxOutgoingArchive.get_LowQuotaWaterMark = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(15, 'get_LowQuotaWaterMark', ((1, 'plLowQuotaWaterMark'),)))
    IFaxOutgoingArchive.put_LowQuotaWaterMark = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(16, 'put_LowQuotaWaterMark', ((1, 'lLowQuotaWaterMark'),)))
    IFaxOutgoingArchive.get_AgeLimit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(17, 'get_AgeLimit', ((1, 'plAgeLimit'),)))
    IFaxOutgoingArchive.put_AgeLimit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(18, 'put_AgeLimit', ((1, 'lAgeLimit'),)))
    IFaxOutgoingArchive.get_SizeLow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(19, 'get_SizeLow', ((1, 'plSizeLow'),)))
    IFaxOutgoingArchive.get_SizeHigh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(20, 'get_SizeHigh', ((1, 'plSizeHigh'),)))
    IFaxOutgoingArchive.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(21, 'Refresh', ()))
    IFaxOutgoingArchive.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(22, 'Save', ()))
    IFaxOutgoingArchive.GetMessages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Devices.Fax.IFaxOutgoingMessageIterator_head))(23, 'GetMessages', ((1, 'lPrefetchSize'),(1, 'pFaxOutgoingMessageIterator'),)))
    IFaxOutgoingArchive.GetMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Devices.Fax.IFaxOutgoingMessage_head))(24, 'GetMessage', ((1, 'bstrMessageId'),(1, 'pFaxOutgoingMessage'),)))
    win32more.System.Com.IDispatch
    return IFaxOutgoingArchive
def _define_IFaxOutgoingJob_head():
    class IFaxOutgoingJob(win32more.System.Com.IDispatch_head):
        Guid = Guid('6356daad-6614-4583-bf-7a-3a-d6-7b-bf-c7-1c')
    return IFaxOutgoingJob
def _define_IFaxOutgoingJob():
    IFaxOutgoingJob = win32more.Devices.Fax.IFaxOutgoingJob_head
    IFaxOutgoingJob.get_Subject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_Subject', ((1, 'pbstrSubject'),)))
    IFaxOutgoingJob.get_DocumentName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(8, 'get_DocumentName', ((1, 'pbstrDocumentName'),)))
    IFaxOutgoingJob.get_Pages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(9, 'get_Pages', ((1, 'plPages'),)))
    IFaxOutgoingJob.get_Size = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(10, 'get_Size', ((1, 'plSize'),)))
    IFaxOutgoingJob.get_SubmissionId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(11, 'get_SubmissionId', ((1, 'pbstrSubmissionId'),)))
    IFaxOutgoingJob.get_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(12, 'get_Id', ((1, 'pbstrId'),)))
    IFaxOutgoingJob.get_OriginalScheduledTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(13, 'get_OriginalScheduledTime', ((1, 'pdateOriginalScheduledTime'),)))
    IFaxOutgoingJob.get_SubmissionTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(14, 'get_SubmissionTime', ((1, 'pdateSubmissionTime'),)))
    IFaxOutgoingJob.get_ReceiptType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_RECEIPT_TYPE_ENUM))(15, 'get_ReceiptType', ((1, 'pReceiptType'),)))
    IFaxOutgoingJob.get_Priority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_PRIORITY_TYPE_ENUM))(16, 'get_Priority', ((1, 'pPriority'),)))
    IFaxOutgoingJob.get_Sender = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxSender_head))(17, 'get_Sender', ((1, 'ppFaxSender'),)))
    IFaxOutgoingJob.get_Recipient = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxRecipient_head))(18, 'get_Recipient', ((1, 'ppFaxRecipient'),)))
    IFaxOutgoingJob.get_CurrentPage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(19, 'get_CurrentPage', ((1, 'plCurrentPage'),)))
    IFaxOutgoingJob.get_DeviceId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(20, 'get_DeviceId', ((1, 'plDeviceId'),)))
    IFaxOutgoingJob.get_Status = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_JOB_STATUS_ENUM))(21, 'get_Status', ((1, 'pStatus'),)))
    IFaxOutgoingJob.get_ExtendedStatusCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_JOB_EXTENDED_STATUS_ENUM))(22, 'get_ExtendedStatusCode', ((1, 'pExtendedStatusCode'),)))
    IFaxOutgoingJob.get_ExtendedStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(23, 'get_ExtendedStatus', ((1, 'pbstrExtendedStatus'),)))
    IFaxOutgoingJob.get_AvailableOperations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_JOB_OPERATIONS_ENUM))(24, 'get_AvailableOperations', ((1, 'pAvailableOperations'),)))
    IFaxOutgoingJob.get_Retries = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(25, 'get_Retries', ((1, 'plRetries'),)))
    IFaxOutgoingJob.get_ScheduledTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(26, 'get_ScheduledTime', ((1, 'pdateScheduledTime'),)))
    IFaxOutgoingJob.get_TransmissionStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(27, 'get_TransmissionStart', ((1, 'pdateTransmissionStart'),)))
    IFaxOutgoingJob.get_TransmissionEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(28, 'get_TransmissionEnd', ((1, 'pdateTransmissionEnd'),)))
    IFaxOutgoingJob.get_CSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(29, 'get_CSID', ((1, 'pbstrCSID'),)))
    IFaxOutgoingJob.get_TSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(30, 'get_TSID', ((1, 'pbstrTSID'),)))
    IFaxOutgoingJob.get_GroupBroadcastReceipts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(31, 'get_GroupBroadcastReceipts', ((1, 'pbGroupBroadcastReceipts'),)))
    IFaxOutgoingJob.Pause = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(32, 'Pause', ()))
    IFaxOutgoingJob.Resume = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(33, 'Resume', ()))
    IFaxOutgoingJob.Restart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(34, 'Restart', ()))
    IFaxOutgoingJob.CopyTiff = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(35, 'CopyTiff', ((1, 'bstrTiffPath'),)))
    IFaxOutgoingJob.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(36, 'Refresh', ()))
    IFaxOutgoingJob.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(37, 'Cancel', ()))
    win32more.System.Com.IDispatch
    return IFaxOutgoingJob
def _define_IFaxOutgoingJob2_head():
    class IFaxOutgoingJob2(win32more.Devices.Fax.IFaxOutgoingJob_head):
        Guid = Guid('418a8d96-59a0-4789-b1-76-ed-f3-dc-8f-a8-f7')
    return IFaxOutgoingJob2
def _define_IFaxOutgoingJob2():
    IFaxOutgoingJob2 = win32more.Devices.Fax.IFaxOutgoingJob2_head
    IFaxOutgoingJob2.get_HasCoverPage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(38, 'get_HasCoverPage', ((1, 'pbHasCoverPage'),)))
    IFaxOutgoingJob2.get_ReceiptAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(39, 'get_ReceiptAddress', ((1, 'pbstrReceiptAddress'),)))
    IFaxOutgoingJob2.get_ScheduleType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_SCHEDULE_TYPE_ENUM))(40, 'get_ScheduleType', ((1, 'pScheduleType'),)))
    win32more.Devices.Fax.IFaxOutgoingJob
    return IFaxOutgoingJob2
def _define_IFaxOutgoingJobs_head():
    class IFaxOutgoingJobs(win32more.System.Com.IDispatch_head):
        Guid = Guid('2c56d8e6-8c2f-4573-94-4c-e5-05-f8-f5-ae-ed')
    return IFaxOutgoingJobs
def _define_IFaxOutgoingJobs():
    IFaxOutgoingJobs = win32more.Devices.Fax.IFaxOutgoingJobs_head
    IFaxOutgoingJobs.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(7, 'get__NewEnum', ((1, 'ppUnk'),)))
    IFaxOutgoingJobs.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.Devices.Fax.IFaxOutgoingJob_head))(8, 'get_Item', ((1, 'vIndex'),(1, 'pFaxOutgoingJob'),)))
    IFaxOutgoingJobs.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(9, 'get_Count', ((1, 'plCount'),)))
    win32more.System.Com.IDispatch
    return IFaxOutgoingJobs
def _define_IFaxOutgoingMessage_head():
    class IFaxOutgoingMessage(win32more.System.Com.IDispatch_head):
        Guid = Guid('f0ea35de-caa5-4a7c-82-c7-2b-60-ba-5f-2b-e2')
    return IFaxOutgoingMessage
def _define_IFaxOutgoingMessage():
    IFaxOutgoingMessage = win32more.Devices.Fax.IFaxOutgoingMessage_head
    IFaxOutgoingMessage.get_SubmissionId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_SubmissionId', ((1, 'pbstrSubmissionId'),)))
    IFaxOutgoingMessage.get_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(8, 'get_Id', ((1, 'pbstrId'),)))
    IFaxOutgoingMessage.get_Subject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_Subject', ((1, 'pbstrSubject'),)))
    IFaxOutgoingMessage.get_DocumentName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(10, 'get_DocumentName', ((1, 'pbstrDocumentName'),)))
    IFaxOutgoingMessage.get_Retries = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(11, 'get_Retries', ((1, 'plRetries'),)))
    IFaxOutgoingMessage.get_Pages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(12, 'get_Pages', ((1, 'plPages'),)))
    IFaxOutgoingMessage.get_Size = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(13, 'get_Size', ((1, 'plSize'),)))
    IFaxOutgoingMessage.get_OriginalScheduledTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(14, 'get_OriginalScheduledTime', ((1, 'pdateOriginalScheduledTime'),)))
    IFaxOutgoingMessage.get_SubmissionTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(15, 'get_SubmissionTime', ((1, 'pdateSubmissionTime'),)))
    IFaxOutgoingMessage.get_Priority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_PRIORITY_TYPE_ENUM))(16, 'get_Priority', ((1, 'pPriority'),)))
    IFaxOutgoingMessage.get_Sender = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxSender_head))(17, 'get_Sender', ((1, 'ppFaxSender'),)))
    IFaxOutgoingMessage.get_Recipient = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxRecipient_head))(18, 'get_Recipient', ((1, 'ppFaxRecipient'),)))
    IFaxOutgoingMessage.get_DeviceName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(19, 'get_DeviceName', ((1, 'pbstrDeviceName'),)))
    IFaxOutgoingMessage.get_TransmissionStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(20, 'get_TransmissionStart', ((1, 'pdateTransmissionStart'),)))
    IFaxOutgoingMessage.get_TransmissionEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(21, 'get_TransmissionEnd', ((1, 'pdateTransmissionEnd'),)))
    IFaxOutgoingMessage.get_CSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(22, 'get_CSID', ((1, 'pbstrCSID'),)))
    IFaxOutgoingMessage.get_TSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(23, 'get_TSID', ((1, 'pbstrTSID'),)))
    IFaxOutgoingMessage.CopyTiff = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(24, 'CopyTiff', ((1, 'bstrTiffPath'),)))
    IFaxOutgoingMessage.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(25, 'Delete', ()))
    win32more.System.Com.IDispatch
    return IFaxOutgoingMessage
def _define_IFaxOutgoingMessage2_head():
    class IFaxOutgoingMessage2(win32more.Devices.Fax.IFaxOutgoingMessage_head):
        Guid = Guid('b37df687-bc88-4b46-b3-be-b4-58-b3-ea-9e-7f')
    return IFaxOutgoingMessage2
def _define_IFaxOutgoingMessage2():
    IFaxOutgoingMessage2 = win32more.Devices.Fax.IFaxOutgoingMessage2_head
    IFaxOutgoingMessage2.get_HasCoverPage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(26, 'get_HasCoverPage', ((1, 'pbHasCoverPage'),)))
    IFaxOutgoingMessage2.get_ReceiptType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_RECEIPT_TYPE_ENUM))(27, 'get_ReceiptType', ((1, 'pReceiptType'),)))
    IFaxOutgoingMessage2.get_ReceiptAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(28, 'get_ReceiptAddress', ((1, 'pbstrReceiptAddress'),)))
    IFaxOutgoingMessage2.get_Read = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(29, 'get_Read', ((1, 'pbRead'),)))
    IFaxOutgoingMessage2.put_Read = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(30, 'put_Read', ((1, 'bRead'),)))
    IFaxOutgoingMessage2.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(31, 'Save', ()))
    IFaxOutgoingMessage2.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(32, 'Refresh', ()))
    win32more.Devices.Fax.IFaxOutgoingMessage
    return IFaxOutgoingMessage2
def _define_IFaxOutgoingMessageIterator_head():
    class IFaxOutgoingMessageIterator(win32more.System.Com.IDispatch_head):
        Guid = Guid('f5ec5d4f-b840-432f-99-80-11-2f-e4-2a-9b-7a')
    return IFaxOutgoingMessageIterator
def _define_IFaxOutgoingMessageIterator():
    IFaxOutgoingMessageIterator = win32more.Devices.Fax.IFaxOutgoingMessageIterator_head
    IFaxOutgoingMessageIterator.get_Message = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxOutgoingMessage_head))(7, 'get_Message', ((1, 'pFaxOutgoingMessage'),)))
    IFaxOutgoingMessageIterator.get_AtEOF = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(8, 'get_AtEOF', ((1, 'pbEOF'),)))
    IFaxOutgoingMessageIterator.get_PrefetchSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(9, 'get_PrefetchSize', ((1, 'plPrefetchSize'),)))
    IFaxOutgoingMessageIterator.put_PrefetchSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(10, 'put_PrefetchSize', ((1, 'lPrefetchSize'),)))
    IFaxOutgoingMessageIterator.MoveFirst = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(11, 'MoveFirst', ()))
    IFaxOutgoingMessageIterator.MoveNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(12, 'MoveNext', ()))
    win32more.System.Com.IDispatch
    return IFaxOutgoingMessageIterator
def _define_IFaxOutgoingQueue_head():
    class IFaxOutgoingQueue(win32more.System.Com.IDispatch_head):
        Guid = Guid('80b1df24-d9ac-4333-b3-73-48-7c-ed-c8-0c-e5')
    return IFaxOutgoingQueue
def _define_IFaxOutgoingQueue():
    IFaxOutgoingQueue = win32more.Devices.Fax.IFaxOutgoingQueue_head
    IFaxOutgoingQueue.get_Blocked = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(7, 'get_Blocked', ((1, 'pbBlocked'),)))
    IFaxOutgoingQueue.put_Blocked = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(8, 'put_Blocked', ((1, 'bBlocked'),)))
    IFaxOutgoingQueue.get_Paused = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(9, 'get_Paused', ((1, 'pbPaused'),)))
    IFaxOutgoingQueue.put_Paused = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(10, 'put_Paused', ((1, 'bPaused'),)))
    IFaxOutgoingQueue.get_AllowPersonalCoverPages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(11, 'get_AllowPersonalCoverPages', ((1, 'pbAllowPersonalCoverPages'),)))
    IFaxOutgoingQueue.put_AllowPersonalCoverPages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(12, 'put_AllowPersonalCoverPages', ((1, 'bAllowPersonalCoverPages'),)))
    IFaxOutgoingQueue.get_UseDeviceTSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(13, 'get_UseDeviceTSID', ((1, 'pbUseDeviceTSID'),)))
    IFaxOutgoingQueue.put_UseDeviceTSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(14, 'put_UseDeviceTSID', ((1, 'bUseDeviceTSID'),)))
    IFaxOutgoingQueue.get_Retries = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(15, 'get_Retries', ((1, 'plRetries'),)))
    IFaxOutgoingQueue.put_Retries = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(16, 'put_Retries', ((1, 'lRetries'),)))
    IFaxOutgoingQueue.get_RetryDelay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(17, 'get_RetryDelay', ((1, 'plRetryDelay'),)))
    IFaxOutgoingQueue.put_RetryDelay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(18, 'put_RetryDelay', ((1, 'lRetryDelay'),)))
    IFaxOutgoingQueue.get_DiscountRateStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(19, 'get_DiscountRateStart', ((1, 'pdateDiscountRateStart'),)))
    IFaxOutgoingQueue.put_DiscountRateStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double)(20, 'put_DiscountRateStart', ((1, 'dateDiscountRateStart'),)))
    IFaxOutgoingQueue.get_DiscountRateEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(21, 'get_DiscountRateEnd', ((1, 'pdateDiscountRateEnd'),)))
    IFaxOutgoingQueue.put_DiscountRateEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double)(22, 'put_DiscountRateEnd', ((1, 'dateDiscountRateEnd'),)))
    IFaxOutgoingQueue.get_AgeLimit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(23, 'get_AgeLimit', ((1, 'plAgeLimit'),)))
    IFaxOutgoingQueue.put_AgeLimit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(24, 'put_AgeLimit', ((1, 'lAgeLimit'),)))
    IFaxOutgoingQueue.get_Branding = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(25, 'get_Branding', ((1, 'pbBranding'),)))
    IFaxOutgoingQueue.put_Branding = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(26, 'put_Branding', ((1, 'bBranding'),)))
    IFaxOutgoingQueue.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(27, 'Refresh', ()))
    IFaxOutgoingQueue.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(28, 'Save', ()))
    IFaxOutgoingQueue.GetJobs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxOutgoingJobs_head))(29, 'GetJobs', ((1, 'pFaxOutgoingJobs'),)))
    IFaxOutgoingQueue.GetJob = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Devices.Fax.IFaxOutgoingJob_head))(30, 'GetJob', ((1, 'bstrJobId'),(1, 'pFaxOutgoingJob'),)))
    win32more.System.Com.IDispatch
    return IFaxOutgoingQueue
def _define_IFaxReceiptOptions_head():
    class IFaxReceiptOptions(win32more.System.Com.IDispatch_head):
        Guid = Guid('378efaeb-5fcb-4afb-b2-ee-e1-6e-80-61-44-87')
    return IFaxReceiptOptions
def _define_IFaxReceiptOptions():
    IFaxReceiptOptions = win32more.Devices.Fax.IFaxReceiptOptions_head
    IFaxReceiptOptions.get_AuthenticationType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_SMTP_AUTHENTICATION_TYPE_ENUM))(7, 'get_AuthenticationType', ((1, 'pType'),)))
    IFaxReceiptOptions.put_AuthenticationType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.FAX_SMTP_AUTHENTICATION_TYPE_ENUM)(8, 'put_AuthenticationType', ((1, 'Type'),)))
    IFaxReceiptOptions.get_SMTPServer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_SMTPServer', ((1, 'pbstrSMTPServer'),)))
    IFaxReceiptOptions.put_SMTPServer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(10, 'put_SMTPServer', ((1, 'bstrSMTPServer'),)))
    IFaxReceiptOptions.get_SMTPPort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(11, 'get_SMTPPort', ((1, 'plSMTPPort'),)))
    IFaxReceiptOptions.put_SMTPPort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(12, 'put_SMTPPort', ((1, 'lSMTPPort'),)))
    IFaxReceiptOptions.get_SMTPSender = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(13, 'get_SMTPSender', ((1, 'pbstrSMTPSender'),)))
    IFaxReceiptOptions.put_SMTPSender = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(14, 'put_SMTPSender', ((1, 'bstrSMTPSender'),)))
    IFaxReceiptOptions.get_SMTPUser = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(15, 'get_SMTPUser', ((1, 'pbstrSMTPUser'),)))
    IFaxReceiptOptions.put_SMTPUser = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(16, 'put_SMTPUser', ((1, 'bstrSMTPUser'),)))
    IFaxReceiptOptions.get_AllowedReceipts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_RECEIPT_TYPE_ENUM))(17, 'get_AllowedReceipts', ((1, 'pAllowedReceipts'),)))
    IFaxReceiptOptions.put_AllowedReceipts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.FAX_RECEIPT_TYPE_ENUM)(18, 'put_AllowedReceipts', ((1, 'AllowedReceipts'),)))
    IFaxReceiptOptions.get_SMTPPassword = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(19, 'get_SMTPPassword', ((1, 'pbstrSMTPPassword'),)))
    IFaxReceiptOptions.put_SMTPPassword = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(20, 'put_SMTPPassword', ((1, 'bstrSMTPPassword'),)))
    IFaxReceiptOptions.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(21, 'Refresh', ()))
    IFaxReceiptOptions.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(22, 'Save', ()))
    IFaxReceiptOptions.get_UseForInboundRouting = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(23, 'get_UseForInboundRouting', ((1, 'pbUseForInboundRouting'),)))
    IFaxReceiptOptions.put_UseForInboundRouting = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(24, 'put_UseForInboundRouting', ((1, 'bUseForInboundRouting'),)))
    win32more.System.Com.IDispatch
    return IFaxReceiptOptions
def _define_IFaxRecipient_head():
    class IFaxRecipient(win32more.System.Com.IDispatch_head):
        Guid = Guid('9a3da3a0-538d-42b6-94-44-aa-a5-7d-0c-e2-bc')
    return IFaxRecipient
def _define_IFaxRecipient():
    IFaxRecipient = win32more.Devices.Fax.IFaxRecipient_head
    IFaxRecipient.get_FaxNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_FaxNumber', ((1, 'pbstrFaxNumber'),)))
    IFaxRecipient.put_FaxNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(8, 'put_FaxNumber', ((1, 'bstrFaxNumber'),)))
    IFaxRecipient.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_Name', ((1, 'pbstrName'),)))
    IFaxRecipient.put_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(10, 'put_Name', ((1, 'bstrName'),)))
    win32more.System.Com.IDispatch
    return IFaxRecipient
def _define_IFaxRecipients_head():
    class IFaxRecipients(win32more.System.Com.IDispatch_head):
        Guid = Guid('b9c9de5a-894e-4492-9f-a3-08-c6-27-c1-1d-5d')
    return IFaxRecipients
def _define_IFaxRecipients():
    IFaxRecipients = win32more.Devices.Fax.IFaxRecipients_head
    IFaxRecipients.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(7, 'get__NewEnum', ((1, 'ppUnk'),)))
    IFaxRecipients.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Devices.Fax.IFaxRecipient_head))(8, 'get_Item', ((1, 'lIndex'),(1, 'ppFaxRecipient'),)))
    IFaxRecipients.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(9, 'get_Count', ((1, 'plCount'),)))
    IFaxRecipients.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.Devices.Fax.IFaxRecipient_head))(10, 'Add', ((1, 'bstrFaxNumber'),(1, 'bstrRecipientName'),(1, 'ppFaxRecipient'),)))
    IFaxRecipients.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(11, 'Remove', ((1, 'lIndex'),)))
    win32more.System.Com.IDispatch
    return IFaxRecipients
def _define_IFaxSecurity_head():
    class IFaxSecurity(win32more.System.Com.IDispatch_head):
        Guid = Guid('77b508c1-09c0-47a2-91-eb-fc-e7-fd-f2-69-0e')
    return IFaxSecurity
def _define_IFaxSecurity():
    IFaxSecurity = win32more.Devices.Fax.IFaxSecurity_head
    IFaxSecurity.get_Descriptor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(7, 'get_Descriptor', ((1, 'pvDescriptor'),)))
    IFaxSecurity.put_Descriptor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT)(8, 'put_Descriptor', ((1, 'vDescriptor'),)))
    IFaxSecurity.get_GrantedRights = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_ACCESS_RIGHTS_ENUM))(9, 'get_GrantedRights', ((1, 'pGrantedRights'),)))
    IFaxSecurity.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(10, 'Refresh', ()))
    IFaxSecurity.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(11, 'Save', ()))
    IFaxSecurity.get_InformationType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(12, 'get_InformationType', ((1, 'plInformationType'),)))
    IFaxSecurity.put_InformationType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(13, 'put_InformationType', ((1, 'lInformationType'),)))
    win32more.System.Com.IDispatch
    return IFaxSecurity
def _define_IFaxSecurity2_head():
    class IFaxSecurity2(win32more.System.Com.IDispatch_head):
        Guid = Guid('17d851f4-d09b-48fc-99-c9-8f-24-c4-db-9a-b1')
    return IFaxSecurity2
def _define_IFaxSecurity2():
    IFaxSecurity2 = win32more.Devices.Fax.IFaxSecurity2_head
    IFaxSecurity2.get_Descriptor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(7, 'get_Descriptor', ((1, 'pvDescriptor'),)))
    IFaxSecurity2.put_Descriptor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT)(8, 'put_Descriptor', ((1, 'vDescriptor'),)))
    IFaxSecurity2.get_GrantedRights = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_ACCESS_RIGHTS_ENUM_2))(9, 'get_GrantedRights', ((1, 'pGrantedRights'),)))
    IFaxSecurity2.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(10, 'Refresh', ()))
    IFaxSecurity2.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(11, 'Save', ()))
    IFaxSecurity2.get_InformationType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(12, 'get_InformationType', ((1, 'plInformationType'),)))
    IFaxSecurity2.put_InformationType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(13, 'put_InformationType', ((1, 'lInformationType'),)))
    win32more.System.Com.IDispatch
    return IFaxSecurity2
def _define_IFaxSender_head():
    class IFaxSender(win32more.System.Com.IDispatch_head):
        Guid = Guid('0d879d7d-f57a-4cc6-a6-f9-3e-e5-d5-27-b4-6a')
    return IFaxSender
def _define_IFaxSender():
    IFaxSender = win32more.Devices.Fax.IFaxSender_head
    IFaxSender.get_BillingCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_BillingCode', ((1, 'pbstrBillingCode'),)))
    IFaxSender.put_BillingCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(8, 'put_BillingCode', ((1, 'bstrBillingCode'),)))
    IFaxSender.get_City = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_City', ((1, 'pbstrCity'),)))
    IFaxSender.put_City = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(10, 'put_City', ((1, 'bstrCity'),)))
    IFaxSender.get_Company = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(11, 'get_Company', ((1, 'pbstrCompany'),)))
    IFaxSender.put_Company = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(12, 'put_Company', ((1, 'bstrCompany'),)))
    IFaxSender.get_Country = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(13, 'get_Country', ((1, 'pbstrCountry'),)))
    IFaxSender.put_Country = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(14, 'put_Country', ((1, 'bstrCountry'),)))
    IFaxSender.get_Department = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(15, 'get_Department', ((1, 'pbstrDepartment'),)))
    IFaxSender.put_Department = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(16, 'put_Department', ((1, 'bstrDepartment'),)))
    IFaxSender.get_Email = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(17, 'get_Email', ((1, 'pbstrEmail'),)))
    IFaxSender.put_Email = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(18, 'put_Email', ((1, 'bstrEmail'),)))
    IFaxSender.get_FaxNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(19, 'get_FaxNumber', ((1, 'pbstrFaxNumber'),)))
    IFaxSender.put_FaxNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(20, 'put_FaxNumber', ((1, 'bstrFaxNumber'),)))
    IFaxSender.get_HomePhone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(21, 'get_HomePhone', ((1, 'pbstrHomePhone'),)))
    IFaxSender.put_HomePhone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(22, 'put_HomePhone', ((1, 'bstrHomePhone'),)))
    IFaxSender.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(23, 'get_Name', ((1, 'pbstrName'),)))
    IFaxSender.put_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(24, 'put_Name', ((1, 'bstrName'),)))
    IFaxSender.get_TSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(25, 'get_TSID', ((1, 'pbstrTSID'),)))
    IFaxSender.put_TSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(26, 'put_TSID', ((1, 'bstrTSID'),)))
    IFaxSender.get_OfficePhone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(27, 'get_OfficePhone', ((1, 'pbstrOfficePhone'),)))
    IFaxSender.put_OfficePhone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(28, 'put_OfficePhone', ((1, 'bstrOfficePhone'),)))
    IFaxSender.get_OfficeLocation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(29, 'get_OfficeLocation', ((1, 'pbstrOfficeLocation'),)))
    IFaxSender.put_OfficeLocation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(30, 'put_OfficeLocation', ((1, 'bstrOfficeLocation'),)))
    IFaxSender.get_State = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(31, 'get_State', ((1, 'pbstrState'),)))
    IFaxSender.put_State = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(32, 'put_State', ((1, 'bstrState'),)))
    IFaxSender.get_StreetAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(33, 'get_StreetAddress', ((1, 'pbstrStreetAddress'),)))
    IFaxSender.put_StreetAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(34, 'put_StreetAddress', ((1, 'bstrStreetAddress'),)))
    IFaxSender.get_Title = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(35, 'get_Title', ((1, 'pbstrTitle'),)))
    IFaxSender.put_Title = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(36, 'put_Title', ((1, 'bstrTitle'),)))
    IFaxSender.get_ZipCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(37, 'get_ZipCode', ((1, 'pbstrZipCode'),)))
    IFaxSender.put_ZipCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(38, 'put_ZipCode', ((1, 'bstrZipCode'),)))
    IFaxSender.LoadDefaultSender = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(39, 'LoadDefaultSender', ()))
    IFaxSender.SaveDefaultSender = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(40, 'SaveDefaultSender', ()))
    win32more.System.Com.IDispatch
    return IFaxSender
def _define_IFaxServer_head():
    class IFaxServer(win32more.System.Com.IDispatch_head):
        Guid = Guid('475b6469-90a5-4878-a5-77-17-a8-6e-8e-34-62')
    return IFaxServer
def _define_IFaxServer():
    IFaxServer = win32more.Devices.Fax.IFaxServer_head
    IFaxServer.Connect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(7, 'Connect', ((1, 'bstrServerName'),)))
    IFaxServer.get_ServerName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(8, 'get_ServerName', ((1, 'pbstrServerName'),)))
    IFaxServer.GetDeviceProviders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxDeviceProviders_head))(9, 'GetDeviceProviders', ((1, 'ppFaxDeviceProviders'),)))
    IFaxServer.GetDevices = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxDevices_head))(10, 'GetDevices', ((1, 'ppFaxDevices'),)))
    IFaxServer.get_InboundRouting = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxInboundRouting_head))(11, 'get_InboundRouting', ((1, 'ppFaxInboundRouting'),)))
    IFaxServer.get_Folders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxFolders_head))(12, 'get_Folders', ((1, 'pFaxFolders'),)))
    IFaxServer.get_LoggingOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxLoggingOptions_head))(13, 'get_LoggingOptions', ((1, 'ppFaxLoggingOptions'),)))
    IFaxServer.get_MajorVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(14, 'get_MajorVersion', ((1, 'plMajorVersion'),)))
    IFaxServer.get_MinorVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(15, 'get_MinorVersion', ((1, 'plMinorVersion'),)))
    IFaxServer.get_MajorBuild = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(16, 'get_MajorBuild', ((1, 'plMajorBuild'),)))
    IFaxServer.get_MinorBuild = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(17, 'get_MinorBuild', ((1, 'plMinorBuild'),)))
    IFaxServer.get_Debug = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(18, 'get_Debug', ((1, 'pbDebug'),)))
    IFaxServer.get_Activity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxActivity_head))(19, 'get_Activity', ((1, 'ppFaxActivity'),)))
    IFaxServer.get_OutboundRouting = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxOutboundRouting_head))(20, 'get_OutboundRouting', ((1, 'ppFaxOutboundRouting'),)))
    IFaxServer.get_ReceiptOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxReceiptOptions_head))(21, 'get_ReceiptOptions', ((1, 'ppFaxReceiptOptions'),)))
    IFaxServer.get_Security = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxSecurity_head))(22, 'get_Security', ((1, 'ppFaxSecurity'),)))
    IFaxServer.Disconnect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(23, 'Disconnect', ()))
    IFaxServer.GetExtensionProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head))(24, 'GetExtensionProperty', ((1, 'bstrGUID'),(1, 'pvProperty'),)))
    IFaxServer.SetExtensionProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT)(25, 'SetExtensionProperty', ((1, 'bstrGUID'),(1, 'vProperty'),)))
    IFaxServer.ListenToServerEvents = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.FAX_SERVER_EVENTS_TYPE_ENUM)(26, 'ListenToServerEvents', ((1, 'EventTypes'),)))
    IFaxServer.RegisterDeviceProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32)(27, 'RegisterDeviceProvider', ((1, 'bstrGUID'),(1, 'bstrFriendlyName'),(1, 'bstrImageName'),(1, 'TspName'),(1, 'lFSPIVersion'),)))
    IFaxServer.UnregisterDeviceProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(28, 'UnregisterDeviceProvider', ((1, 'bstrUniqueName'),)))
    IFaxServer.RegisterInboundRoutingExtension = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.System.Com.VARIANT)(29, 'RegisterInboundRoutingExtension', ((1, 'bstrExtensionName'),(1, 'bstrFriendlyName'),(1, 'bstrImageName'),(1, 'vMethods'),)))
    IFaxServer.UnregisterInboundRoutingExtension = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(30, 'UnregisterInboundRoutingExtension', ((1, 'bstrExtensionUniqueName'),)))
    IFaxServer.get_RegisteredEvents = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_SERVER_EVENTS_TYPE_ENUM))(31, 'get_RegisteredEvents', ((1, 'pEventTypes'),)))
    IFaxServer.get_APIVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.FAX_SERVER_APIVERSION_ENUM))(32, 'get_APIVersion', ((1, 'pAPIVersion'),)))
    win32more.System.Com.IDispatch
    return IFaxServer
def _define_IFaxServer2_head():
    class IFaxServer2(win32more.Devices.Fax.IFaxServer_head):
        Guid = Guid('571ced0f-5609-4f40-91-76-54-7e-3a-72-ca-7c')
    return IFaxServer2
def _define_IFaxServer2():
    IFaxServer2 = win32more.Devices.Fax.IFaxServer2_head
    IFaxServer2.get_Configuration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxConfiguration_head))(33, 'get_Configuration', ((1, 'ppFaxConfiguration'),)))
    IFaxServer2.get_CurrentAccount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxAccount_head))(34, 'get_CurrentAccount', ((1, 'ppCurrentAccount'),)))
    IFaxServer2.get_FaxAccountSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxAccountSet_head))(35, 'get_FaxAccountSet', ((1, 'ppFaxAccountSet'),)))
    IFaxServer2.get_Security2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.IFaxSecurity2_head))(36, 'get_Security2', ((1, 'ppFaxSecurity2'),)))
    win32more.Devices.Fax.IFaxServer
    return IFaxServer2
def _define_IFaxServerNotify_head():
    class IFaxServerNotify(win32more.System.Com.IDispatch_head):
        Guid = Guid('2e037b27-cf8a-4abd-b1-e0-57-04-94-3b-ea-6f')
    return IFaxServerNotify
def _define_IFaxServerNotify():
    IFaxServerNotify = win32more.Devices.Fax.IFaxServerNotify_head
    win32more.System.Com.IDispatch
    return IFaxServerNotify
def _define_IFaxServerNotify2_head():
    class IFaxServerNotify2(win32more.System.Com.IDispatch_head):
        Guid = Guid('ec9c69b9-5fe7-4805-94-67-82-fc-d9-6a-f9-03')
    return IFaxServerNotify2
def _define_IFaxServerNotify2():
    IFaxServerNotify2 = win32more.Devices.Fax.IFaxServerNotify2_head
    IFaxServerNotify2.OnIncomingJobAdded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head,win32more.Foundation.BSTR)(7, 'OnIncomingJobAdded', ((1, 'pFaxServer'),(1, 'bstrJobId'),)))
    IFaxServerNotify2.OnIncomingJobRemoved = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head,win32more.Foundation.BSTR)(8, 'OnIncomingJobRemoved', ((1, 'pFaxServer'),(1, 'bstrJobId'),)))
    IFaxServerNotify2.OnIncomingJobChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head,win32more.Foundation.BSTR,win32more.Devices.Fax.IFaxJobStatus_head)(9, 'OnIncomingJobChanged', ((1, 'pFaxServer'),(1, 'bstrJobId'),(1, 'pJobStatus'),)))
    IFaxServerNotify2.OnOutgoingJobAdded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head,win32more.Foundation.BSTR)(10, 'OnOutgoingJobAdded', ((1, 'pFaxServer'),(1, 'bstrJobId'),)))
    IFaxServerNotify2.OnOutgoingJobRemoved = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head,win32more.Foundation.BSTR)(11, 'OnOutgoingJobRemoved', ((1, 'pFaxServer'),(1, 'bstrJobId'),)))
    IFaxServerNotify2.OnOutgoingJobChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head,win32more.Foundation.BSTR,win32more.Devices.Fax.IFaxJobStatus_head)(12, 'OnOutgoingJobChanged', ((1, 'pFaxServer'),(1, 'bstrJobId'),(1, 'pJobStatus'),)))
    IFaxServerNotify2.OnIncomingMessageAdded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head,win32more.Foundation.BSTR)(13, 'OnIncomingMessageAdded', ((1, 'pFaxServer'),(1, 'bstrMessageId'),)))
    IFaxServerNotify2.OnIncomingMessageRemoved = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head,win32more.Foundation.BSTR)(14, 'OnIncomingMessageRemoved', ((1, 'pFaxServer'),(1, 'bstrMessageId'),)))
    IFaxServerNotify2.OnOutgoingMessageAdded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head,win32more.Foundation.BSTR)(15, 'OnOutgoingMessageAdded', ((1, 'pFaxServer'),(1, 'bstrMessageId'),)))
    IFaxServerNotify2.OnOutgoingMessageRemoved = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head,win32more.Foundation.BSTR)(16, 'OnOutgoingMessageRemoved', ((1, 'pFaxServer'),(1, 'bstrMessageId'),)))
    IFaxServerNotify2.OnReceiptOptionsChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head)(17, 'OnReceiptOptionsChange', ((1, 'pFaxServer'),)))
    IFaxServerNotify2.OnActivityLoggingConfigChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head)(18, 'OnActivityLoggingConfigChange', ((1, 'pFaxServer'),)))
    IFaxServerNotify2.OnSecurityConfigChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head)(19, 'OnSecurityConfigChange', ((1, 'pFaxServer'),)))
    IFaxServerNotify2.OnEventLoggingConfigChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head)(20, 'OnEventLoggingConfigChange', ((1, 'pFaxServer'),)))
    IFaxServerNotify2.OnOutgoingQueueConfigChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head)(21, 'OnOutgoingQueueConfigChange', ((1, 'pFaxServer'),)))
    IFaxServerNotify2.OnOutgoingArchiveConfigChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head)(22, 'OnOutgoingArchiveConfigChange', ((1, 'pFaxServer'),)))
    IFaxServerNotify2.OnIncomingArchiveConfigChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head)(23, 'OnIncomingArchiveConfigChange', ((1, 'pFaxServer'),)))
    IFaxServerNotify2.OnDevicesConfigChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head)(24, 'OnDevicesConfigChange', ((1, 'pFaxServer'),)))
    IFaxServerNotify2.OnOutboundRoutingGroupsConfigChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head)(25, 'OnOutboundRoutingGroupsConfigChange', ((1, 'pFaxServer'),)))
    IFaxServerNotify2.OnOutboundRoutingRulesConfigChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head)(26, 'OnOutboundRoutingRulesConfigChange', ((1, 'pFaxServer'),)))
    IFaxServerNotify2.OnServerActivityChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head,Int32,Int32,Int32,Int32)(27, 'OnServerActivityChange', ((1, 'pFaxServer'),(1, 'lIncomingMessages'),(1, 'lRoutingMessages'),(1, 'lOutgoingMessages'),(1, 'lQueuedMessages'),)))
    IFaxServerNotify2.OnQueuesStatusChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head,win32more.Foundation.VARIANT_BOOL,win32more.Foundation.VARIANT_BOOL,win32more.Foundation.VARIANT_BOOL)(28, 'OnQueuesStatusChange', ((1, 'pFaxServer'),(1, 'bOutgoingQueueBlocked'),(1, 'bOutgoingQueuePaused'),(1, 'bIncomingQueueBlocked'),)))
    IFaxServerNotify2.OnNewCall = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head,Int32,Int32,win32more.Foundation.BSTR)(29, 'OnNewCall', ((1, 'pFaxServer'),(1, 'lCallId'),(1, 'lDeviceId'),(1, 'bstrCallerId'),)))
    IFaxServerNotify2.OnServerShutDown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head)(30, 'OnServerShutDown', ((1, 'pFaxServer'),)))
    IFaxServerNotify2.OnDeviceStatusChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head,Int32,win32more.Foundation.VARIANT_BOOL,win32more.Foundation.VARIANT_BOOL,win32more.Foundation.VARIANT_BOOL,win32more.Foundation.VARIANT_BOOL)(31, 'OnDeviceStatusChange', ((1, 'pFaxServer'),(1, 'lDeviceId'),(1, 'bPoweredOff'),(1, 'bSending'),(1, 'bReceiving'),(1, 'bRinging'),)))
    IFaxServerNotify2.OnGeneralServerConfigChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IFaxServer2_head)(32, 'OnGeneralServerConfigChanged', ((1, 'pFaxServer'),)))
    win32more.System.Com.IDispatch
    return IFaxServerNotify2
def _define_IStiDevice_head():
    class IStiDevice(win32more.System.Com.IUnknown_head):
        Guid = Guid('6cfa5a80-2dc8-11d0-90-ea-00-aa-00-60-f8-6c')
    return IStiDevice
def _define_IStiDevice():
    IStiDevice = win32more.Devices.Fax.IStiDevice_head
    IStiDevice.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HINSTANCE,win32more.Foundation.PWSTR,UInt32,UInt32)(3, 'Initialize', ((1, 'hinst'),(1, 'pwszDeviceName'),(1, 'dwVersion'),(1, 'dwMode'),)))
    IStiDevice.GetCapabilities = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.STI_DEV_CAPS_head))(4, 'GetCapabilities', ((1, 'pDevCaps'),)))
    IStiDevice.GetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.STI_DEVICE_STATUS_head))(5, 'GetStatus', ((1, 'pDevStatus'),)))
    IStiDevice.DeviceReset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(6, 'DeviceReset', ()))
    IStiDevice.Diagnostic = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.STI_DIAG_head))(7, 'Diagnostic', ((1, 'pBuffer'),)))
    IStiDevice.Escape = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_void_p,UInt32,c_void_p,UInt32,POINTER(UInt32))(8, 'Escape', ((1, 'EscapeFunction'),(1, 'lpInData'),(1, 'cbInDataSize'),(1, 'pOutData'),(1, 'dwOutDataSize'),(1, 'pdwActualData'),)))
    IStiDevice.GetLastError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(9, 'GetLastError', ((1, 'pdwLastDeviceError'),)))
    IStiDevice.LockDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(10, 'LockDevice', ((1, 'dwTimeOut'),)))
    IStiDevice.UnLockDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(11, 'UnLockDevice', ()))
    IStiDevice.RawReadData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(UInt32),POINTER(win32more.System.IO.OVERLAPPED_head))(12, 'RawReadData', ((1, 'lpBuffer'),(1, 'lpdwNumberOfBytes'),(1, 'lpOverlapped'),)))
    IStiDevice.RawWriteData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,POINTER(win32more.System.IO.OVERLAPPED_head))(13, 'RawWriteData', ((1, 'lpBuffer'),(1, 'nNumberOfBytes'),(1, 'lpOverlapped'),)))
    IStiDevice.RawReadCommand = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(UInt32),POINTER(win32more.System.IO.OVERLAPPED_head))(14, 'RawReadCommand', ((1, 'lpBuffer'),(1, 'lpdwNumberOfBytes'),(1, 'lpOverlapped'),)))
    IStiDevice.RawWriteCommand = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,POINTER(win32more.System.IO.OVERLAPPED_head))(15, 'RawWriteCommand', ((1, 'lpBuffer'),(1, 'nNumberOfBytes'),(1, 'lpOverlapped'),)))
    IStiDevice.Subscribe = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.STISUBSCRIBE_head))(16, 'Subscribe', ((1, 'lpSubsribe'),)))
    IStiDevice.GetLastNotificationData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.STINOTIFY_head))(17, 'GetLastNotificationData', ((1, 'lpNotify'),)))
    IStiDevice.UnSubscribe = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(18, 'UnSubscribe', ()))
    IStiDevice.GetLastErrorInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax._ERROR_INFOW_head))(19, 'GetLastErrorInfo', ((1, 'pLastErrorInfo'),)))
    win32more.System.Com.IUnknown
    return IStiDevice
def _define_IStiDeviceControl_head():
    class IStiDeviceControl(win32more.System.Com.IUnknown_head):
        Guid = Guid('128a9860-52dc-11d0-9e-df-44-45-53-54-00-00')
    return IStiDeviceControl
def _define_IStiDeviceControl():
    IStiDeviceControl = win32more.Devices.Fax.IStiDeviceControl_head
    IStiDeviceControl.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,win32more.Foundation.PWSTR,UInt32)(3, 'Initialize', ((1, 'dwDeviceType'),(1, 'dwMode'),(1, 'pwszPortName'),(1, 'dwFlags'),)))
    IStiDeviceControl.RawReadData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(UInt32),POINTER(win32more.System.IO.OVERLAPPED_head))(4, 'RawReadData', ((1, 'lpBuffer'),(1, 'lpdwNumberOfBytes'),(1, 'lpOverlapped'),)))
    IStiDeviceControl.RawWriteData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,POINTER(win32more.System.IO.OVERLAPPED_head))(5, 'RawWriteData', ((1, 'lpBuffer'),(1, 'nNumberOfBytes'),(1, 'lpOverlapped'),)))
    IStiDeviceControl.RawReadCommand = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(UInt32),POINTER(win32more.System.IO.OVERLAPPED_head))(6, 'RawReadCommand', ((1, 'lpBuffer'),(1, 'lpdwNumberOfBytes'),(1, 'lpOverlapped'),)))
    IStiDeviceControl.RawWriteCommand = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,POINTER(win32more.System.IO.OVERLAPPED_head))(7, 'RawWriteCommand', ((1, 'lpBuffer'),(1, 'nNumberOfBytes'),(1, 'lpOverlapped'),)))
    IStiDeviceControl.RawDeviceControl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_void_p,UInt32,c_void_p,UInt32,POINTER(UInt32))(8, 'RawDeviceControl', ((1, 'EscapeFunction'),(1, 'lpInData'),(1, 'cbInDataSize'),(1, 'pOutData'),(1, 'dwOutDataSize'),(1, 'pdwActualData'),)))
    IStiDeviceControl.GetLastError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(9, 'GetLastError', ((1, 'lpdwLastError'),)))
    IStiDeviceControl.GetMyDevicePortName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32)(10, 'GetMyDevicePortName', ((1, 'lpszDevicePath'),(1, 'cwDevicePathSize'),)))
    IStiDeviceControl.GetMyDeviceHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HANDLE))(11, 'GetMyDeviceHandle', ((1, 'lph'),)))
    IStiDeviceControl.GetMyDeviceOpenMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(12, 'GetMyDeviceOpenMode', ((1, 'pdwOpenMode'),)))
    IStiDeviceControl.WriteToErrorLog = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,UInt32)(13, 'WriteToErrorLog', ((1, 'dwMessageType'),(1, 'pszMessage'),(1, 'dwErrorCode'),)))
    win32more.System.Com.IUnknown
    return IStiDeviceControl
def _define_IStillImageW_head():
    class IStillImageW(win32more.System.Com.IUnknown_head):
        Guid = Guid('641bd880-2dc8-11d0-90-ea-00-aa-00-60-f8-6c')
    return IStillImageW
def _define_IStillImageW():
    IStillImageW = win32more.Devices.Fax.IStillImageW_head
    IStillImageW.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HINSTANCE,UInt32)(3, 'Initialize', ((1, 'hinst'),(1, 'dwVersion'),)))
    IStillImageW.GetDeviceList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(UInt32),POINTER(c_void_p))(4, 'GetDeviceList', ((1, 'dwType'),(1, 'dwFlags'),(1, 'pdwItemsReturned'),(1, 'ppBuffer'),)))
    IStillImageW.GetDeviceInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(c_void_p))(5, 'GetDeviceInfo', ((1, 'pwszDeviceName'),(1, 'ppBuffer'),)))
    IStillImageW.CreateDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Devices.Fax.IStiDevice_head),win32more.System.Com.IUnknown_head)(6, 'CreateDevice', ((1, 'pwszDeviceName'),(1, 'dwMode'),(1, 'pDevice'),(1, 'punkOuter'),)))
    IStillImageW.GetDeviceValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32),c_char_p_no,POINTER(UInt32))(7, 'GetDeviceValue', ((1, 'pwszDeviceName'),(1, 'pValueName'),(1, 'pType'),(1, 'pData'),(1, 'cbData'),)))
    IStillImageW.SetDeviceValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,c_char_p_no,UInt32)(8, 'SetDeviceValue', ((1, 'pwszDeviceName'),(1, 'pValueName'),(1, 'Type'),(1, 'pData'),(1, 'cbData'),)))
    IStillImageW.GetSTILaunchInformation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(UInt32),win32more.Foundation.PWSTR)(9, 'GetSTILaunchInformation', ((1, 'pwszDeviceName'),(1, 'pdwEventCode'),(1, 'pwszEventName'),)))
    IStillImageW.RegisterLaunchApplication = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(10, 'RegisterLaunchApplication', ((1, 'pwszAppName'),(1, 'pwszCommandLine'),)))
    IStillImageW.UnregisterLaunchApplication = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(11, 'UnregisterLaunchApplication', ((1, 'pwszAppName'),)))
    IStillImageW.EnableHwNotifications = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.BOOL)(12, 'EnableHwNotifications', ((1, 'pwszDeviceName'),(1, 'bNewState'),)))
    IStillImageW.GetHwNotificationState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.BOOL))(13, 'GetHwNotificationState', ((1, 'pwszDeviceName'),(1, 'pbCurrentState'),)))
    IStillImageW.RefreshDeviceBus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(14, 'RefreshDeviceBus', ((1, 'pwszDeviceName'),)))
    IStillImageW.LaunchApplicationForDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Devices.Fax.STINOTIFY_head))(15, 'LaunchApplicationForDevice', ((1, 'pwszDeviceName'),(1, 'pwszAppName'),(1, 'pStiNotify'),)))
    IStillImageW.SetupDeviceParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.STI_DEVICE_INFORMATIONW_head))(16, 'SetupDeviceParameters', ((1, 'param0'),)))
    IStillImageW.WriteToErrorLog = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR)(17, 'WriteToErrorLog', ((1, 'dwMessageType'),(1, 'pszMessage'),)))
    win32more.System.Com.IUnknown
    return IStillImageW
def _define_IStiUSD_head():
    class IStiUSD(win32more.System.Com.IUnknown_head):
        Guid = Guid('0c9bb460-51ac-11d0-90-ea-00-aa-00-60-f8-6c')
    return IStiUSD
def _define_IStiUSD():
    IStiUSD = win32more.Devices.Fax.IStiUSD_head
    IStiUSD.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.IStiDeviceControl_head,UInt32,win32more.System.Registry.HKEY)(3, 'Initialize', ((1, 'pHelDcb'),(1, 'dwStiVersion'),(1, 'hParametersKey'),)))
    IStiUSD.GetCapabilities = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.STI_USD_CAPS_head))(4, 'GetCapabilities', ((1, 'pDevCaps'),)))
    IStiUSD.GetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.STI_DEVICE_STATUS_head))(5, 'GetStatus', ((1, 'pDevStatus'),)))
    IStiUSD.DeviceReset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(6, 'DeviceReset', ()))
    IStiUSD.Diagnostic = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.STI_DIAG_head))(7, 'Diagnostic', ((1, 'pBuffer'),)))
    IStiUSD.Escape = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_void_p,UInt32,c_void_p,UInt32,POINTER(UInt32))(8, 'Escape', ((1, 'EscapeFunction'),(1, 'lpInData'),(1, 'cbInDataSize'),(1, 'pOutData'),(1, 'cbOutDataSize'),(1, 'pdwActualData'),)))
    IStiUSD.GetLastError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(9, 'GetLastError', ((1, 'pdwLastDeviceError'),)))
    IStiUSD.LockDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(10, 'LockDevice', ()))
    IStiUSD.UnLockDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(11, 'UnLockDevice', ()))
    IStiUSD.RawReadData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(UInt32),POINTER(win32more.System.IO.OVERLAPPED_head))(12, 'RawReadData', ((1, 'lpBuffer'),(1, 'lpdwNumberOfBytes'),(1, 'lpOverlapped'),)))
    IStiUSD.RawWriteData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,POINTER(win32more.System.IO.OVERLAPPED_head))(13, 'RawWriteData', ((1, 'lpBuffer'),(1, 'nNumberOfBytes'),(1, 'lpOverlapped'),)))
    IStiUSD.RawReadCommand = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(UInt32),POINTER(win32more.System.IO.OVERLAPPED_head))(14, 'RawReadCommand', ((1, 'lpBuffer'),(1, 'lpdwNumberOfBytes'),(1, 'lpOverlapped'),)))
    IStiUSD.RawWriteCommand = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,POINTER(win32more.System.IO.OVERLAPPED_head))(15, 'RawWriteCommand', ((1, 'lpBuffer'),(1, 'nNumberOfBytes'),(1, 'lpOverlapped'),)))
    IStiUSD.SetNotificationHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE)(16, 'SetNotificationHandle', ((1, 'hEvent'),)))
    IStiUSD.GetNotificationData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax.STINOTIFY_head))(17, 'GetNotificationData', ((1, 'lpNotify'),)))
    IStiUSD.GetLastErrorInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Fax._ERROR_INFOW_head))(18, 'GetLastErrorInfo', ((1, 'pLastErrorInfo'),)))
    win32more.System.Com.IUnknown
    return IStiUSD
def _define_PFAX_EXT_CONFIG_CHANGE():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,c_char_p_no,UInt32)
def _define_PFAX_EXT_FREE_BUFFER():
    return WINFUNCTYPE(Void,c_void_p)
def _define_PFAX_EXT_GET_DATA():
    return WINFUNCTYPE(UInt32,UInt32,win32more.Devices.Fax.FAX_ENUM_DEVICE_ID_SOURCE,win32more.Foundation.PWSTR,POINTER(c_char_p_no),POINTER(UInt32))
def _define_PFAX_EXT_INITIALIZE_CONFIG():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Fax.PFAX_EXT_GET_DATA,win32more.Devices.Fax.PFAX_EXT_SET_DATA,win32more.Devices.Fax.PFAX_EXT_REGISTER_FOR_EVENTS,win32more.Devices.Fax.PFAX_EXT_UNREGISTER_FOR_EVENTS,win32more.Devices.Fax.PFAX_EXT_FREE_BUFFER)
def _define_PFAX_EXT_REGISTER_FOR_EVENTS():
    return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.HINSTANCE,UInt32,win32more.Devices.Fax.FAX_ENUM_DEVICE_ID_SOURCE,win32more.Foundation.PWSTR,win32more.Devices.Fax.PFAX_EXT_CONFIG_CHANGE)
def _define_PFAX_EXT_SET_DATA():
    return WINFUNCTYPE(UInt32,win32more.Foundation.HINSTANCE,UInt32,win32more.Devices.Fax.FAX_ENUM_DEVICE_ID_SOURCE,win32more.Foundation.PWSTR,c_char_p_no,UInt32)
def _define_PFAX_EXT_UNREGISTER_FOR_EVENTS():
    return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE)
def _define_PFAX_LINECALLBACK():
    return WINFUNCTYPE(Void,win32more.Foundation.HANDLE,UInt32,UInt32,UIntPtr,UIntPtr,UIntPtr,UIntPtr)
def _define_PFAX_RECIPIENT_CALLBACKA():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,c_void_p,POINTER(win32more.Devices.Fax.FAX_JOB_PARAMA_head),POINTER(win32more.Devices.Fax.FAX_COVERPAGE_INFOA_head))
def _define_PFAX_RECIPIENT_CALLBACKW():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,c_void_p,POINTER(win32more.Devices.Fax.FAX_JOB_PARAMW_head),POINTER(win32more.Devices.Fax.FAX_COVERPAGE_INFOW_head))
def _define_PFAX_ROUTING_INSTALLATION_CALLBACKW():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,c_void_p,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)
def _define_PFAX_SEND_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,UInt32,UInt32)
def _define_PFAX_SERVICE_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,UIntPtr,UIntPtr,UIntPtr)
def _define_PFAXABORT():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32)
def _define_PFAXACCESSCHECK():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32)
def _define_PFAXCLOSE():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE)
def _define_PFAXCOMPLETEJOBPARAMSA():
    return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(POINTER(win32more.Devices.Fax.FAX_JOB_PARAMA_head)),POINTER(POINTER(win32more.Devices.Fax.FAX_COVERPAGE_INFOA_head)))
def _define_PFAXCOMPLETEJOBPARAMSW():
    return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(POINTER(win32more.Devices.Fax.FAX_JOB_PARAMW_head)),POINTER(POINTER(win32more.Devices.Fax.FAX_COVERPAGE_INFOW_head)))
def _define_PFAXCONNECTFAXSERVERA():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,POINTER(win32more.Foundation.HANDLE))
def _define_PFAXCONNECTFAXSERVERW():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.HANDLE))
def _define_PFAXDEVABORTOPERATION():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE)
def _define_PFAXDEVCONFIGURE():
    return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.UI.Controls.HPROPSHEETPAGE))
def _define_PFAXDEVENDJOB():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE)
def _define_PFAXDEVINITIALIZE():
    return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Fax.PFAX_LINECALLBACK),win32more.Devices.Fax.PFAX_SERVICE_CALLBACK)
def _define_PFAXDEVRECEIVE():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,POINTER(win32more.Devices.Fax.FAX_RECEIVE_head))
def _define_PFAXDEVREPORTSTATUS():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Fax.FAX_DEV_STATUS_head),UInt32,POINTER(UInt32))
def _define_PFAXDEVSEND():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Fax.FAX_SEND_head),win32more.Devices.Fax.PFAX_SEND_CALLBACK)
def _define_PFAXDEVSHUTDOWN():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,)
def _define_PFAXDEVSTARTJOB():
    return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,UInt32,POINTER(win32more.Foundation.HANDLE),win32more.Foundation.HANDLE,UIntPtr)
def _define_PFAXDEVVIRTUALDEVICECREATION():
    return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(UInt32),win32more.Foundation.PWSTR,POINTER(UInt32),win32more.Foundation.HANDLE,UIntPtr)
def _define_PFAXENABLEROUTINGMETHODA():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,win32more.Foundation.BOOL)
def _define_PFAXENABLEROUTINGMETHODW():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,win32more.Foundation.BOOL)
def _define_PFAXENUMGLOBALROUTINGINFOA():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_GLOBAL_ROUTING_INFOA_head)),POINTER(UInt32))
def _define_PFAXENUMGLOBALROUTINGINFOW():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_GLOBAL_ROUTING_INFOW_head)),POINTER(UInt32))
def _define_PFAXENUMJOBSA():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_JOB_ENTRYA_head)),POINTER(UInt32))
def _define_PFAXENUMJOBSW():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_JOB_ENTRYW_head)),POINTER(UInt32))
def _define_PFAXENUMPORTSA():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_PORT_INFOA_head)),POINTER(UInt32))
def _define_PFAXENUMPORTSW():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_PORT_INFOW_head)),POINTER(UInt32))
def _define_PFAXENUMROUTINGMETHODSA():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_ROUTING_METHODA_head)),POINTER(UInt32))
def _define_PFAXENUMROUTINGMETHODSW():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_ROUTING_METHODW_head)),POINTER(UInt32))
def _define_PFAXFREEBUFFER():
    return WINFUNCTYPE(Void,c_void_p)
def _define_PFAXGETCONFIGURATIONA():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_CONFIGURATIONA_head)))
def _define_PFAXGETCONFIGURATIONW():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_CONFIGURATIONW_head)))
def _define_PFAXGETDEVICESTATUSA():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_DEVICE_STATUSA_head)))
def _define_PFAXGETDEVICESTATUSW():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_DEVICE_STATUSW_head)))
def _define_PFAXGETJOBA():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,POINTER(POINTER(win32more.Devices.Fax.FAX_JOB_ENTRYA_head)))
def _define_PFAXGETJOBW():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,POINTER(POINTER(win32more.Devices.Fax.FAX_JOB_ENTRYW_head)))
def _define_PFAXGETLOGGINGCATEGORIESA():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_LOG_CATEGORYA_head)),POINTER(UInt32))
def _define_PFAXGETLOGGINGCATEGORIESW():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_LOG_CATEGORYW_head)),POINTER(UInt32))
def _define_PFAXGETPAGEDATA():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,POINTER(c_char_p_no),POINTER(UInt32),POINTER(UInt32),POINTER(UInt32))
def _define_PFAXGETPORTA():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_PORT_INFOA_head)))
def _define_PFAXGETPORTW():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Devices.Fax.FAX_PORT_INFOW_head)))
def _define_PFAXGETROUTINGINFOA():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,POINTER(c_char_p_no),POINTER(UInt32))
def _define_PFAXGETROUTINGINFOW():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,POINTER(c_char_p_no),POINTER(UInt32))
def _define_PFAXINITIALIZEEVENTQUEUE():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,UIntPtr,win32more.Foundation.HWND,UInt32)
def _define_PFAXOPENPORT():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,UInt32,POINTER(win32more.Foundation.HANDLE))
def _define_PFAXPRINTCOVERPAGEA():
    return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Fax.FAX_CONTEXT_INFOA_head),POINTER(win32more.Devices.Fax.FAX_COVERPAGE_INFOA_head))
def _define_PFAXPRINTCOVERPAGEW():
    return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Fax.FAX_CONTEXT_INFOW_head),POINTER(win32more.Devices.Fax.FAX_COVERPAGE_INFOW_head))
def _define_PFAXREGISTERROUTINGEXTENSIONW():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Devices.Fax.PFAX_ROUTING_INSTALLATION_CALLBACKW,c_void_p)
def _define_PFAXREGISTERSERVICEPROVIDERW():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)
def _define_PFAXROUTEADDFILE():
    return WINFUNCTYPE(Int32,UInt32,win32more.Foundation.PWSTR,POINTER(Guid))
def _define_PFAXROUTEDELETEFILE():
    return WINFUNCTYPE(Int32,UInt32,win32more.Foundation.PWSTR)
def _define_PFAXROUTEDEVICECHANGENOTIFICATION():
    return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.Foundation.BOOL)
def _define_PFAXROUTEDEVICEENABLE():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,UInt32,Int32)
def _define_PFAXROUTEENUMFILE():
    return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,POINTER(Guid),POINTER(Guid),win32more.Foundation.PWSTR,c_void_p)
def _define_PFAXROUTEENUMFILES():
    return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,POINTER(Guid),win32more.Devices.Fax.PFAXROUTEENUMFILE,c_void_p)
def _define_PFAXROUTEGETFILE():
    return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32))
def _define_PFAXROUTEGETROUTINGINFO():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,UInt32,c_char_p_no,POINTER(UInt32))
def _define_PFAXROUTEINITIALIZE():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Fax.FAX_ROUTE_CALLBACKROUTINES_head))
def _define_PFAXROUTEMETHOD():
    return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Fax.FAX_ROUTE_head),POINTER(c_void_p),POINTER(UInt32))
def _define_PFAXROUTEMODIFYROUTINGDATA():
    return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.Foundation.PWSTR,c_char_p_no,UInt32)
def _define_PFAXROUTESETROUTINGINFO():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,UInt32,c_char_p_no,UInt32)
def _define_PFAXSENDDOCUMENTA():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,POINTER(win32more.Devices.Fax.FAX_JOB_PARAMA_head),POINTER(win32more.Devices.Fax.FAX_COVERPAGE_INFOA_head),POINTER(UInt32))
def _define_PFAXSENDDOCUMENTFORBROADCASTA():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,POINTER(UInt32),win32more.Devices.Fax.PFAX_RECIPIENT_CALLBACKA,c_void_p)
def _define_PFAXSENDDOCUMENTFORBROADCASTW():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,POINTER(UInt32),win32more.Devices.Fax.PFAX_RECIPIENT_CALLBACKW,c_void_p)
def _define_PFAXSENDDOCUMENTW():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,POINTER(win32more.Devices.Fax.FAX_JOB_PARAMW_head),POINTER(win32more.Devices.Fax.FAX_COVERPAGE_INFOW_head),POINTER(UInt32))
def _define_PFAXSETCONFIGURATIONA():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Fax.FAX_CONFIGURATIONA_head))
def _define_PFAXSETCONFIGURATIONW():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Fax.FAX_CONFIGURATIONW_head))
def _define_PFAXSETGLOBALROUTINGINFOA():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Fax.FAX_GLOBAL_ROUTING_INFOA_head))
def _define_PFAXSETGLOBALROUTINGINFOW():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Fax.FAX_GLOBAL_ROUTING_INFOW_head))
def _define_PFAXSETJOBA():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,UInt32,POINTER(win32more.Devices.Fax.FAX_JOB_ENTRYA_head))
def _define_PFAXSETJOBW():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,UInt32,POINTER(win32more.Devices.Fax.FAX_JOB_ENTRYW_head))
def _define_PFAXSETLOGGINGCATEGORIESA():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Fax.FAX_LOG_CATEGORYA_head),UInt32)
def _define_PFAXSETLOGGINGCATEGORIESW():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Fax.FAX_LOG_CATEGORYW_head),UInt32)
def _define_PFAXSETPORTA():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Fax.FAX_PORT_INFOA_head))
def _define_PFAXSETPORTW():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Fax.FAX_PORT_INFOW_head))
def _define_PFAXSETROUTINGINFOA():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,c_char_p_no,UInt32)
def _define_PFAXSETROUTINGINFOW():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,c_char_p_no,UInt32)
def _define_PFAXSTARTPRINTJOBA():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,POINTER(win32more.Devices.Fax.FAX_PRINT_INFOA_head),POINTER(UInt32),POINTER(win32more.Devices.Fax.FAX_CONTEXT_INFOA_head))
def _define_PFAXSTARTPRINTJOBW():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,POINTER(win32more.Devices.Fax.FAX_PRINT_INFOW_head),POINTER(UInt32),POINTER(win32more.Devices.Fax.FAX_CONTEXT_INFOW_head))
def _define_PFAXUNREGISTERSERVICEPROVIDERW():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR)
SendToMode = Int32
SEND_TO_FAX_RECIPIENT_ATTACHMENT = 0
def _define_STI_DEV_CAPS_head():
    class STI_DEV_CAPS(Structure):
        pass
    return STI_DEV_CAPS
def _define_STI_DEV_CAPS():
    STI_DEV_CAPS = win32more.Devices.Fax.STI_DEV_CAPS_head
    STI_DEV_CAPS._fields_ = [
        ('dwGeneric', UInt32),
    ]
    return STI_DEV_CAPS
def _define_STI_DEVICE_INFORMATIONW_head():
    class STI_DEVICE_INFORMATIONW(Structure):
        pass
    return STI_DEVICE_INFORMATIONW
def _define_STI_DEVICE_INFORMATIONW():
    STI_DEVICE_INFORMATIONW = win32more.Devices.Fax.STI_DEVICE_INFORMATIONW_head
    STI_DEVICE_INFORMATIONW._fields_ = [
        ('dwSize', UInt32),
        ('DeviceType', UInt32),
        ('szDeviceInternalName', Char * 128),
        ('DeviceCapabilitiesA', win32more.Devices.Fax.STI_DEV_CAPS),
        ('dwHardwareConfiguration', UInt32),
        ('pszVendorDescription', win32more.Foundation.PWSTR),
        ('pszDeviceDescription', win32more.Foundation.PWSTR),
        ('pszPortName', win32more.Foundation.PWSTR),
        ('pszPropProvider', win32more.Foundation.PWSTR),
        ('pszLocalName', win32more.Foundation.PWSTR),
    ]
    return STI_DEVICE_INFORMATIONW
STI_DEVICE_MJ_TYPE = Int32
STI_DEVICE_MJ_TYPE_StiDeviceTypeDefault = 0
STI_DEVICE_MJ_TYPE_StiDeviceTypeScanner = 1
STI_DEVICE_MJ_TYPE_StiDeviceTypeDigitalCamera = 2
STI_DEVICE_MJ_TYPE_StiDeviceTypeStreamingVideo = 3
def _define_STI_DEVICE_STATUS_head():
    class STI_DEVICE_STATUS(Structure):
        pass
    return STI_DEVICE_STATUS
def _define_STI_DEVICE_STATUS():
    STI_DEVICE_STATUS = win32more.Devices.Fax.STI_DEVICE_STATUS_head
    STI_DEVICE_STATUS._fields_ = [
        ('dwSize', UInt32),
        ('StatusMask', UInt32),
        ('dwOnlineState', UInt32),
        ('dwHardwareStatusCode', UInt32),
        ('dwEventHandlingState', UInt32),
        ('dwPollingInterval', UInt32),
    ]
    return STI_DEVICE_STATUS
def _define_STI_DIAG_head():
    class STI_DIAG(Structure):
        pass
    return STI_DIAG
def _define_STI_DIAG():
    STI_DIAG = win32more.Devices.Fax.STI_DIAG_head
    STI_DIAG._fields_ = [
        ('dwSize', UInt32),
        ('dwBasicDiagCode', UInt32),
        ('dwVendorDiagCode', UInt32),
        ('dwStatusMask', UInt32),
        ('sErrorInfo', win32more.Devices.Fax._ERROR_INFOW),
    ]
    return STI_DIAG
def _define_STI_USD_CAPS_head():
    class STI_USD_CAPS(Structure):
        pass
    return STI_USD_CAPS
def _define_STI_USD_CAPS():
    STI_USD_CAPS = win32more.Devices.Fax.STI_USD_CAPS_head
    STI_USD_CAPS._fields_ = [
        ('dwVersion', UInt32),
        ('dwGenericCaps', UInt32),
    ]
    return STI_USD_CAPS
def _define_STI_WIA_DEVICE_INFORMATIONW_head():
    class STI_WIA_DEVICE_INFORMATIONW(Structure):
        pass
    return STI_WIA_DEVICE_INFORMATIONW
def _define_STI_WIA_DEVICE_INFORMATIONW():
    STI_WIA_DEVICE_INFORMATIONW = win32more.Devices.Fax.STI_WIA_DEVICE_INFORMATIONW_head
    STI_WIA_DEVICE_INFORMATIONW._fields_ = [
        ('dwSize', UInt32),
        ('DeviceType', UInt32),
        ('szDeviceInternalName', Char * 128),
        ('DeviceCapabilitiesA', win32more.Devices.Fax.STI_DEV_CAPS),
        ('dwHardwareConfiguration', UInt32),
        ('pszVendorDescription', win32more.Foundation.PWSTR),
        ('pszDeviceDescription', win32more.Foundation.PWSTR),
        ('pszPortName', win32more.Foundation.PWSTR),
        ('pszPropProvider', win32more.Foundation.PWSTR),
        ('pszLocalName', win32more.Foundation.PWSTR),
        ('pszUiDll', win32more.Foundation.PWSTR),
        ('pszServer', win32more.Foundation.PWSTR),
    ]
    return STI_WIA_DEVICE_INFORMATIONW
def _define_STINOTIFY_head():
    class STINOTIFY(Structure):
        pass
    return STINOTIFY
def _define_STINOTIFY():
    STINOTIFY = win32more.Devices.Fax.STINOTIFY_head
    STINOTIFY._fields_ = [
        ('dwSize', UInt32),
        ('guidNotificationCode', Guid),
        ('abNotificationData', Byte * 64),
    ]
    return STINOTIFY
def _define_STISUBSCRIBE_head():
    class STISUBSCRIBE(Structure):
        pass
    return STISUBSCRIBE
def _define_STISUBSCRIBE():
    STISUBSCRIBE = win32more.Devices.Fax.STISUBSCRIBE_head
    STISUBSCRIBE._fields_ = [
        ('dwSize', UInt32),
        ('dwFlags', UInt32),
        ('dwFilter', UInt32),
        ('hWndNotify', win32more.Foundation.HWND),
        ('hEvent', win32more.Foundation.HANDLE),
        ('uiNotificationMessage', UInt32),
    ]
    return STISUBSCRIBE
__all__ = [
    "CF_MSFAXSRV_DEVICE_ID",
    "CF_MSFAXSRV_FSP_GUID",
    "CF_MSFAXSRV_ROUTEEXT_NAME",
    "CF_MSFAXSRV_ROUTING_METHOD_GUID",
    "CF_MSFAXSRV_SERVER_NAME",
    "CLSID_Sti",
    "CanSendToFaxRecipient",
    "DEVPKEY_WIA_DeviceType",
    "DEVPKEY_WIA_USDClassId",
    "DEV_ID_SRC_FAX",
    "DEV_ID_SRC_TAPI",
    "DRT_EMAIL",
    "DRT_INBOX",
    "DRT_NONE",
    "FAXDEVRECEIVE_SIZE",
    "FAXDEVREPORTSTATUS_SIZE",
    "FAXLOG_CATEGORY_INBOUND",
    "FAXLOG_CATEGORY_INIT",
    "FAXLOG_CATEGORY_OUTBOUND",
    "FAXLOG_CATEGORY_UNKNOWN",
    "FAXLOG_LEVEL_MAX",
    "FAXLOG_LEVEL_MED",
    "FAXLOG_LEVEL_MIN",
    "FAXLOG_LEVEL_NONE",
    "FAXROUTE_ENABLE",
    "FAX_ACCESS_RIGHTS_ENUM",
    "FAX_ACCESS_RIGHTS_ENUM_2",
    "FAX_ACCOUNT_EVENTS_TYPE_ENUM",
    "FAX_ACCOUNT_EVENTS_TYPE_ENUM_faetFXSSVC_ENDED",
    "FAX_ACCOUNT_EVENTS_TYPE_ENUM_faetIN_ARCHIVE",
    "FAX_ACCOUNT_EVENTS_TYPE_ENUM_faetIN_QUEUE",
    "FAX_ACCOUNT_EVENTS_TYPE_ENUM_faetNONE",
    "FAX_ACCOUNT_EVENTS_TYPE_ENUM_faetOUT_ARCHIVE",
    "FAX_ACCOUNT_EVENTS_TYPE_ENUM_faetOUT_QUEUE",
    "FAX_CONFIGURATIONA",
    "FAX_CONFIGURATIONW",
    "FAX_CONFIG_QUERY",
    "FAX_CONFIG_SET",
    "FAX_CONTEXT_INFOA",
    "FAX_CONTEXT_INFOW",
    "FAX_COVERPAGE_INFOA",
    "FAX_COVERPAGE_INFOW",
    "FAX_COVERPAGE_TYPE_ENUM",
    "FAX_COVERPAGE_TYPE_ENUM_fcptLOCAL",
    "FAX_COVERPAGE_TYPE_ENUM_fcptNONE",
    "FAX_COVERPAGE_TYPE_ENUM_fcptSERVER",
    "FAX_DEVICE_RECEIVE_MODE_ENUM",
    "FAX_DEVICE_STATUSA",
    "FAX_DEVICE_STATUSW",
    "FAX_DEV_STATUS",
    "FAX_ENUM_DELIVERY_REPORT_TYPES",
    "FAX_ENUM_DEVICE_ID_SOURCE",
    "FAX_ENUM_JOB_COMMANDS",
    "FAX_ENUM_JOB_SEND_ATTRIBUTES",
    "FAX_ENUM_LOG_CATEGORIES",
    "FAX_ENUM_LOG_LEVELS",
    "FAX_ENUM_PORT_OPEN_TYPE",
    "FAX_ERR_BAD_GROUP_CONFIGURATION",
    "FAX_ERR_DEVICE_NUM_LIMIT_EXCEEDED",
    "FAX_ERR_DIRECTORY_IN_USE",
    "FAX_ERR_END",
    "FAX_ERR_FILE_ACCESS_DENIED",
    "FAX_ERR_GROUP_IN_USE",
    "FAX_ERR_GROUP_NOT_FOUND",
    "FAX_ERR_MESSAGE_NOT_FOUND",
    "FAX_ERR_NOT_NTFS",
    "FAX_ERR_NOT_SUPPORTED_ON_THIS_SKU",
    "FAX_ERR_RECIPIENTS_LIMIT",
    "FAX_ERR_RULE_NOT_FOUND",
    "FAX_ERR_SRV_OUTOFMEMORY",
    "FAX_ERR_START",
    "FAX_ERR_VERSION_MISMATCH",
    "FAX_EVENTA",
    "FAX_EVENTW",
    "FAX_E_BAD_GROUP_CONFIGURATION",
    "FAX_E_DEVICE_NUM_LIMIT_EXCEEDED",
    "FAX_E_DIRECTORY_IN_USE",
    "FAX_E_FILE_ACCESS_DENIED",
    "FAX_E_GROUP_IN_USE",
    "FAX_E_GROUP_NOT_FOUND",
    "FAX_E_MESSAGE_NOT_FOUND",
    "FAX_E_NOT_NTFS",
    "FAX_E_NOT_SUPPORTED_ON_THIS_SKU",
    "FAX_E_RECIPIENTS_LIMIT",
    "FAX_E_RULE_NOT_FOUND",
    "FAX_E_SRV_OUTOFMEMORY",
    "FAX_E_VERSION_MISMATCH",
    "FAX_GLOBAL_ROUTING_INFOA",
    "FAX_GLOBAL_ROUTING_INFOW",
    "FAX_GROUP_STATUS_ENUM",
    "FAX_GROUP_STATUS_ENUM_fgsALL_DEV_NOT_VALID",
    "FAX_GROUP_STATUS_ENUM_fgsALL_DEV_VALID",
    "FAX_GROUP_STATUS_ENUM_fgsEMPTY",
    "FAX_GROUP_STATUS_ENUM_fgsSOME_DEV_NOT_VALID",
    "FAX_JOB_ENTRYA",
    "FAX_JOB_ENTRYW",
    "FAX_JOB_EXTENDED_STATUS_ENUM",
    "FAX_JOB_EXTENDED_STATUS_ENUM_fjesANSWERED",
    "FAX_JOB_EXTENDED_STATUS_ENUM_fjesBAD_ADDRESS",
    "FAX_JOB_EXTENDED_STATUS_ENUM_fjesBUSY",
    "FAX_JOB_EXTENDED_STATUS_ENUM_fjesCALL_ABORTED",
    "FAX_JOB_EXTENDED_STATUS_ENUM_fjesCALL_BLACKLISTED",
    "FAX_JOB_EXTENDED_STATUS_ENUM_fjesCALL_COMPLETED",
    "FAX_JOB_EXTENDED_STATUS_ENUM_fjesCALL_DELAYED",
    "FAX_JOB_EXTENDED_STATUS_ENUM_fjesDIALING",
    "FAX_JOB_EXTENDED_STATUS_ENUM_fjesDISCONNECTED",
    "FAX_JOB_EXTENDED_STATUS_ENUM_fjesFATAL_ERROR",
    "FAX_JOB_EXTENDED_STATUS_ENUM_fjesHANDLED",
    "FAX_JOB_EXTENDED_STATUS_ENUM_fjesINITIALIZING",
    "FAX_JOB_EXTENDED_STATUS_ENUM_fjesLINE_UNAVAILABLE",
    "FAX_JOB_EXTENDED_STATUS_ENUM_fjesNONE",
    "FAX_JOB_EXTENDED_STATUS_ENUM_fjesNOT_FAX_CALL",
    "FAX_JOB_EXTENDED_STATUS_ENUM_fjesNO_ANSWER",
    "FAX_JOB_EXTENDED_STATUS_ENUM_fjesNO_DIAL_TONE",
    "FAX_JOB_EXTENDED_STATUS_ENUM_fjesPARTIALLY_RECEIVED",
    "FAX_JOB_EXTENDED_STATUS_ENUM_fjesPROPRIETARY",
    "FAX_JOB_EXTENDED_STATUS_ENUM_fjesRECEIVING",
    "FAX_JOB_EXTENDED_STATUS_ENUM_fjesTRANSMITTING",
    "FAX_JOB_MANAGE",
    "FAX_JOB_OPERATIONS_ENUM",
    "FAX_JOB_OPERATIONS_ENUM_fjoDELETE",
    "FAX_JOB_OPERATIONS_ENUM_fjoPAUSE",
    "FAX_JOB_OPERATIONS_ENUM_fjoRECIPIENT_INFO",
    "FAX_JOB_OPERATIONS_ENUM_fjoRESTART",
    "FAX_JOB_OPERATIONS_ENUM_fjoRESUME",
    "FAX_JOB_OPERATIONS_ENUM_fjoSENDER_INFO",
    "FAX_JOB_OPERATIONS_ENUM_fjoVIEW",
    "FAX_JOB_PARAMA",
    "FAX_JOB_PARAMW",
    "FAX_JOB_QUERY",
    "FAX_JOB_STATUS_ENUM",
    "FAX_JOB_STATUS_ENUM_fjsCANCELED",
    "FAX_JOB_STATUS_ENUM_fjsCANCELING",
    "FAX_JOB_STATUS_ENUM_fjsCOMPLETED",
    "FAX_JOB_STATUS_ENUM_fjsFAILED",
    "FAX_JOB_STATUS_ENUM_fjsINPROGRESS",
    "FAX_JOB_STATUS_ENUM_fjsNOLINE",
    "FAX_JOB_STATUS_ENUM_fjsPAUSED",
    "FAX_JOB_STATUS_ENUM_fjsPENDING",
    "FAX_JOB_STATUS_ENUM_fjsRETRIES_EXCEEDED",
    "FAX_JOB_STATUS_ENUM_fjsRETRYING",
    "FAX_JOB_STATUS_ENUM_fjsROUTING",
    "FAX_JOB_SUBMIT",
    "FAX_JOB_TYPE_ENUM",
    "FAX_JOB_TYPE_ENUM_fjtRECEIVE",
    "FAX_JOB_TYPE_ENUM_fjtROUTING",
    "FAX_JOB_TYPE_ENUM_fjtSEND",
    "FAX_LOG_CATEGORYA",
    "FAX_LOG_CATEGORYW",
    "FAX_LOG_LEVEL_ENUM",
    "FAX_LOG_LEVEL_ENUM_fllMAX",
    "FAX_LOG_LEVEL_ENUM_fllMED",
    "FAX_LOG_LEVEL_ENUM_fllMIN",
    "FAX_LOG_LEVEL_ENUM_fllNONE",
    "FAX_PORT_INFOA",
    "FAX_PORT_INFOW",
    "FAX_PORT_QUERY",
    "FAX_PORT_SET",
    "FAX_PRINT_INFOA",
    "FAX_PRINT_INFOW",
    "FAX_PRIORITY_TYPE_ENUM",
    "FAX_PRIORITY_TYPE_ENUM_fptHIGH",
    "FAX_PRIORITY_TYPE_ENUM_fptLOW",
    "FAX_PRIORITY_TYPE_ENUM_fptNORMAL",
    "FAX_PROVIDER_STATUS_ENUM",
    "FAX_PROVIDER_STATUS_ENUM_fpsBAD_GUID",
    "FAX_PROVIDER_STATUS_ENUM_fpsBAD_VERSION",
    "FAX_PROVIDER_STATUS_ENUM_fpsCANT_INIT",
    "FAX_PROVIDER_STATUS_ENUM_fpsCANT_LINK",
    "FAX_PROVIDER_STATUS_ENUM_fpsCANT_LOAD",
    "FAX_PROVIDER_STATUS_ENUM_fpsSERVER_ERROR",
    "FAX_PROVIDER_STATUS_ENUM_fpsSUCCESS",
    "FAX_RECEIPT_TYPE_ENUM",
    "FAX_RECEIPT_TYPE_ENUM_frtMAIL",
    "FAX_RECEIPT_TYPE_ENUM_frtMSGBOX",
    "FAX_RECEIPT_TYPE_ENUM_frtNONE",
    "FAX_RECEIVE",
    "FAX_ROUTE",
    "FAX_ROUTE_CALLBACKROUTINES",
    "FAX_ROUTING_METHODA",
    "FAX_ROUTING_METHODW",
    "FAX_ROUTING_RULE_CODE_ENUM",
    "FAX_RULE_STATUS_ENUM",
    "FAX_RULE_STATUS_ENUM_frsALL_GROUP_DEV_NOT_VALID",
    "FAX_RULE_STATUS_ENUM_frsBAD_DEVICE",
    "FAX_RULE_STATUS_ENUM_frsEMPTY_GROUP",
    "FAX_RULE_STATUS_ENUM_frsSOME_GROUP_DEV_NOT_VALID",
    "FAX_RULE_STATUS_ENUM_frsVALID",
    "FAX_SCHEDULE_TYPE_ENUM",
    "FAX_SCHEDULE_TYPE_ENUM_fstDISCOUNT_PERIOD",
    "FAX_SCHEDULE_TYPE_ENUM_fstNOW",
    "FAX_SCHEDULE_TYPE_ENUM_fstSPECIFIC_TIME",
    "FAX_SEND",
    "FAX_SERVER_APIVERSION_ENUM",
    "FAX_SERVER_EVENTS_TYPE_ENUM",
    "FAX_SERVER_EVENTS_TYPE_ENUM_fsetACTIVITY",
    "FAX_SERVER_EVENTS_TYPE_ENUM_fsetCONFIG",
    "FAX_SERVER_EVENTS_TYPE_ENUM_fsetDEVICE_STATUS",
    "FAX_SERVER_EVENTS_TYPE_ENUM_fsetFXSSVC_ENDED",
    "FAX_SERVER_EVENTS_TYPE_ENUM_fsetINCOMING_CALL",
    "FAX_SERVER_EVENTS_TYPE_ENUM_fsetIN_ARCHIVE",
    "FAX_SERVER_EVENTS_TYPE_ENUM_fsetIN_QUEUE",
    "FAX_SERVER_EVENTS_TYPE_ENUM_fsetNONE",
    "FAX_SERVER_EVENTS_TYPE_ENUM_fsetOUT_ARCHIVE",
    "FAX_SERVER_EVENTS_TYPE_ENUM_fsetOUT_QUEUE",
    "FAX_SERVER_EVENTS_TYPE_ENUM_fsetQUEUE_STATE",
    "FAX_SMTP_AUTHENTICATION_TYPE_ENUM",
    "FAX_SMTP_AUTHENTICATION_TYPE_ENUM_fsatANONYMOUS",
    "FAX_SMTP_AUTHENTICATION_TYPE_ENUM_fsatBASIC",
    "FAX_SMTP_AUTHENTICATION_TYPE_ENUM_fsatNTLM",
    "FAX_TIME",
    "FEI_ABORTING",
    "FEI_ANSWERED",
    "FEI_BAD_ADDRESS",
    "FEI_BUSY",
    "FEI_CALL_BLACKLISTED",
    "FEI_CALL_DELAYED",
    "FEI_COMPLETED",
    "FEI_DELETED",
    "FEI_DIALING",
    "FEI_DISCONNECTED",
    "FEI_FATAL_ERROR",
    "FEI_FAXSVC_ENDED",
    "FEI_FAXSVC_STARTED",
    "FEI_HANDLED",
    "FEI_IDLE",
    "FEI_INITIALIZING",
    "FEI_JOB_QUEUED",
    "FEI_LINE_UNAVAILABLE",
    "FEI_MODEM_POWERED_OFF",
    "FEI_MODEM_POWERED_ON",
    "FEI_NEVENTS",
    "FEI_NOT_FAX_CALL",
    "FEI_NO_ANSWER",
    "FEI_NO_DIAL_TONE",
    "FEI_RECEIVING",
    "FEI_RINGING",
    "FEI_ROUTING",
    "FEI_SENDING",
    "FPF_RECEIVE",
    "FPF_SEND",
    "FPF_VIRTUAL",
    "FPS_ABORTING",
    "FPS_ANSWERED",
    "FPS_AVAILABLE",
    "FPS_BAD_ADDRESS",
    "FPS_BUSY",
    "FPS_CALL_BLACKLISTED",
    "FPS_CALL_DELAYED",
    "FPS_COMPLETED",
    "FPS_DIALING",
    "FPS_DISCONNECTED",
    "FPS_FATAL_ERROR",
    "FPS_HANDLED",
    "FPS_INITIALIZING",
    "FPS_NOT_FAX_CALL",
    "FPS_NO_ANSWER",
    "FPS_NO_DIAL_TONE",
    "FPS_OFFLINE",
    "FPS_RECEIVING",
    "FPS_RINGING",
    "FPS_ROUTING",
    "FPS_SENDING",
    "FPS_UNAVAILABLE",
    "FS_ANSWERED",
    "FS_BAD_ADDRESS",
    "FS_BUSY",
    "FS_CALL_BLACKLISTED",
    "FS_CALL_DELAYED",
    "FS_COMPLETED",
    "FS_DIALING",
    "FS_DISCONNECTED",
    "FS_FATAL_ERROR",
    "FS_HANDLED",
    "FS_INITIALIZING",
    "FS_LINE_UNAVAILABLE",
    "FS_NOT_FAX_CALL",
    "FS_NO_ANSWER",
    "FS_NO_DIAL_TONE",
    "FS_RECEIVING",
    "FS_TRANSMITTING",
    "FS_USER_ABORT",
    "FaxAbort",
    "FaxAccessCheck",
    "FaxAccount",
    "FaxAccountFolders",
    "FaxAccountIncomingArchive",
    "FaxAccountIncomingQueue",
    "FaxAccountOutgoingArchive",
    "FaxAccountOutgoingQueue",
    "FaxAccountSet",
    "FaxAccounts",
    "FaxActivity",
    "FaxActivityLogging",
    "FaxClose",
    "FaxCompleteJobParamsA",
    "FaxCompleteJobParamsW",
    "FaxConfiguration",
    "FaxConnectFaxServerA",
    "FaxConnectFaxServerW",
    "FaxDevice",
    "FaxDeviceIds",
    "FaxDeviceProvider",
    "FaxDeviceProviders",
    "FaxDevices",
    "FaxDocument",
    "FaxEnableRoutingMethodA",
    "FaxEnableRoutingMethodW",
    "FaxEnumGlobalRoutingInfoA",
    "FaxEnumGlobalRoutingInfoW",
    "FaxEnumJobsA",
    "FaxEnumJobsW",
    "FaxEnumPortsA",
    "FaxEnumPortsW",
    "FaxEnumRoutingMethodsA",
    "FaxEnumRoutingMethodsW",
    "FaxEventLogging",
    "FaxFolders",
    "FaxFreeBuffer",
    "FaxGetConfigurationA",
    "FaxGetConfigurationW",
    "FaxGetDeviceStatusA",
    "FaxGetDeviceStatusW",
    "FaxGetJobA",
    "FaxGetJobW",
    "FaxGetLoggingCategoriesA",
    "FaxGetLoggingCategoriesW",
    "FaxGetPageData",
    "FaxGetPortA",
    "FaxGetPortW",
    "FaxGetRoutingInfoA",
    "FaxGetRoutingInfoW",
    "FaxInboundRouting",
    "FaxInboundRoutingExtension",
    "FaxInboundRoutingExtensions",
    "FaxInboundRoutingMethod",
    "FaxInboundRoutingMethods",
    "FaxIncomingArchive",
    "FaxIncomingJob",
    "FaxIncomingJobs",
    "FaxIncomingMessage",
    "FaxIncomingMessageIterator",
    "FaxIncomingQueue",
    "FaxInitializeEventQueue",
    "FaxJobStatus",
    "FaxLoggingOptions",
    "FaxOpenPort",
    "FaxOutboundRouting",
    "FaxOutboundRoutingGroup",
    "FaxOutboundRoutingGroups",
    "FaxOutboundRoutingRule",
    "FaxOutboundRoutingRules",
    "FaxOutgoingArchive",
    "FaxOutgoingJob",
    "FaxOutgoingJobs",
    "FaxOutgoingMessage",
    "FaxOutgoingMessageIterator",
    "FaxOutgoingQueue",
    "FaxPrintCoverPageA",
    "FaxPrintCoverPageW",
    "FaxReceiptOptions",
    "FaxRecipient",
    "FaxRecipients",
    "FaxRegisterRoutingExtensionW",
    "FaxRegisterServiceProviderW",
    "FaxSecurity",
    "FaxSecurity2",
    "FaxSendDocumentA",
    "FaxSendDocumentForBroadcastA",
    "FaxSendDocumentForBroadcastW",
    "FaxSendDocumentW",
    "FaxSender",
    "FaxServer",
    "FaxSetConfigurationA",
    "FaxSetConfigurationW",
    "FaxSetGlobalRoutingInfoA",
    "FaxSetGlobalRoutingInfoW",
    "FaxSetJobA",
    "FaxSetJobW",
    "FaxSetLoggingCategoriesA",
    "FaxSetLoggingCategoriesW",
    "FaxSetPortA",
    "FaxSetPortW",
    "FaxSetRoutingInfoA",
    "FaxSetRoutingInfoW",
    "FaxStartPrintJobA",
    "FaxStartPrintJobW",
    "FaxUnregisterServiceProviderW",
    "GUID_DeviceArrivedLaunch",
    "GUID_STIUserDefined1",
    "GUID_STIUserDefined2",
    "GUID_STIUserDefined3",
    "GUID_ScanFaxImage",
    "GUID_ScanImage",
    "GUID_ScanPrintImage",
    "IFaxAccount",
    "IFaxAccountFolders",
    "IFaxAccountIncomingArchive",
    "IFaxAccountIncomingQueue",
    "IFaxAccountNotify",
    "IFaxAccountOutgoingArchive",
    "IFaxAccountOutgoingQueue",
    "IFaxAccountSet",
    "IFaxAccounts",
    "IFaxActivity",
    "IFaxActivityLogging",
    "IFaxConfiguration",
    "IFaxDevice",
    "IFaxDeviceIds",
    "IFaxDeviceProvider",
    "IFaxDeviceProviders",
    "IFaxDevices",
    "IFaxDocument",
    "IFaxDocument2",
    "IFaxEventLogging",
    "IFaxFolders",
    "IFaxInboundRouting",
    "IFaxInboundRoutingExtension",
    "IFaxInboundRoutingExtensions",
    "IFaxInboundRoutingMethod",
    "IFaxInboundRoutingMethods",
    "IFaxIncomingArchive",
    "IFaxIncomingJob",
    "IFaxIncomingJobs",
    "IFaxIncomingMessage",
    "IFaxIncomingMessage2",
    "IFaxIncomingMessageIterator",
    "IFaxIncomingQueue",
    "IFaxJobStatus",
    "IFaxLoggingOptions",
    "IFaxOutboundRouting",
    "IFaxOutboundRoutingGroup",
    "IFaxOutboundRoutingGroups",
    "IFaxOutboundRoutingRule",
    "IFaxOutboundRoutingRules",
    "IFaxOutgoingArchive",
    "IFaxOutgoingJob",
    "IFaxOutgoingJob2",
    "IFaxOutgoingJobs",
    "IFaxOutgoingMessage",
    "IFaxOutgoingMessage2",
    "IFaxOutgoingMessageIterator",
    "IFaxOutgoingQueue",
    "IFaxReceiptOptions",
    "IFaxRecipient",
    "IFaxRecipients",
    "IFaxSecurity",
    "IFaxSecurity2",
    "IFaxSender",
    "IFaxServer",
    "IFaxServer2",
    "IFaxServerNotify",
    "IFaxServerNotify2",
    "IS_DIGITAL_CAMERA_STR",
    "IS_DIGITAL_CAMERA_VAL",
    "IStiDevice",
    "IStiDeviceControl",
    "IStiUSD",
    "IStillImageW",
    "JC_DELETE",
    "JC_PAUSE",
    "JC_RESUME",
    "JC_UNKNOWN",
    "JSA_DISCOUNT_PERIOD",
    "JSA_NOW",
    "JSA_SPECIFIC_TIME",
    "JS_DELETING",
    "JS_FAILED",
    "JS_INPROGRESS",
    "JS_NOLINE",
    "JS_PAUSED",
    "JS_PENDING",
    "JS_RETRIES_EXCEEDED",
    "JS_RETRYING",
    "JT_FAIL_RECEIVE",
    "JT_RECEIVE",
    "JT_ROUTING",
    "JT_SEND",
    "JT_UNKNOWN",
    "MAX_NOTIFICATION_DATA",
    "MS_FAXROUTE_EMAIL_GUID",
    "MS_FAXROUTE_FOLDER_GUID",
    "MS_FAXROUTE_PRINTING_GUID",
    "PFAXABORT",
    "PFAXACCESSCHECK",
    "PFAXCLOSE",
    "PFAXCOMPLETEJOBPARAMSA",
    "PFAXCOMPLETEJOBPARAMSW",
    "PFAXCONNECTFAXSERVERA",
    "PFAXCONNECTFAXSERVERW",
    "PFAXDEVABORTOPERATION",
    "PFAXDEVCONFIGURE",
    "PFAXDEVENDJOB",
    "PFAXDEVINITIALIZE",
    "PFAXDEVRECEIVE",
    "PFAXDEVREPORTSTATUS",
    "PFAXDEVSEND",
    "PFAXDEVSHUTDOWN",
    "PFAXDEVSTARTJOB",
    "PFAXDEVVIRTUALDEVICECREATION",
    "PFAXENABLEROUTINGMETHODA",
    "PFAXENABLEROUTINGMETHODW",
    "PFAXENUMGLOBALROUTINGINFOA",
    "PFAXENUMGLOBALROUTINGINFOW",
    "PFAXENUMJOBSA",
    "PFAXENUMJOBSW",
    "PFAXENUMPORTSA",
    "PFAXENUMPORTSW",
    "PFAXENUMROUTINGMETHODSA",
    "PFAXENUMROUTINGMETHODSW",
    "PFAXFREEBUFFER",
    "PFAXGETCONFIGURATIONA",
    "PFAXGETCONFIGURATIONW",
    "PFAXGETDEVICESTATUSA",
    "PFAXGETDEVICESTATUSW",
    "PFAXGETJOBA",
    "PFAXGETJOBW",
    "PFAXGETLOGGINGCATEGORIESA",
    "PFAXGETLOGGINGCATEGORIESW",
    "PFAXGETPAGEDATA",
    "PFAXGETPORTA",
    "PFAXGETPORTW",
    "PFAXGETROUTINGINFOA",
    "PFAXGETROUTINGINFOW",
    "PFAXINITIALIZEEVENTQUEUE",
    "PFAXOPENPORT",
    "PFAXPRINTCOVERPAGEA",
    "PFAXPRINTCOVERPAGEW",
    "PFAXREGISTERROUTINGEXTENSIONW",
    "PFAXREGISTERSERVICEPROVIDERW",
    "PFAXROUTEADDFILE",
    "PFAXROUTEDELETEFILE",
    "PFAXROUTEDEVICECHANGENOTIFICATION",
    "PFAXROUTEDEVICEENABLE",
    "PFAXROUTEENUMFILE",
    "PFAXROUTEENUMFILES",
    "PFAXROUTEGETFILE",
    "PFAXROUTEGETROUTINGINFO",
    "PFAXROUTEINITIALIZE",
    "PFAXROUTEMETHOD",
    "PFAXROUTEMODIFYROUTINGDATA",
    "PFAXROUTESETROUTINGINFO",
    "PFAXSENDDOCUMENTA",
    "PFAXSENDDOCUMENTFORBROADCASTA",
    "PFAXSENDDOCUMENTFORBROADCASTW",
    "PFAXSENDDOCUMENTW",
    "PFAXSETCONFIGURATIONA",
    "PFAXSETCONFIGURATIONW",
    "PFAXSETGLOBALROUTINGINFOA",
    "PFAXSETGLOBALROUTINGINFOW",
    "PFAXSETJOBA",
    "PFAXSETJOBW",
    "PFAXSETLOGGINGCATEGORIESA",
    "PFAXSETLOGGINGCATEGORIESW",
    "PFAXSETPORTA",
    "PFAXSETPORTW",
    "PFAXSETROUTINGINFOA",
    "PFAXSETROUTINGINFOW",
    "PFAXSTARTPRINTJOBA",
    "PFAXSTARTPRINTJOBW",
    "PFAXUNREGISTERSERVICEPROVIDERW",
    "PFAX_EXT_CONFIG_CHANGE",
    "PFAX_EXT_FREE_BUFFER",
    "PFAX_EXT_GET_DATA",
    "PFAX_EXT_INITIALIZE_CONFIG",
    "PFAX_EXT_REGISTER_FOR_EVENTS",
    "PFAX_EXT_SET_DATA",
    "PFAX_EXT_UNREGISTER_FOR_EVENTS",
    "PFAX_LINECALLBACK",
    "PFAX_RECIPIENT_CALLBACKA",
    "PFAX_RECIPIENT_CALLBACKW",
    "PFAX_ROUTING_INSTALLATION_CALLBACKW",
    "PFAX_SEND_CALLBACK",
    "PFAX_SERVICE_CALLBACK",
    "PORT_OPEN_MODIFY",
    "PORT_OPEN_QUERY",
    "QUERY_STATUS",
    "REGSTR_VAL_BAUDRATE",
    "REGSTR_VAL_BAUDRATE_A",
    "REGSTR_VAL_DATA_W",
    "REGSTR_VAL_DEVICESUBTYPE_W",
    "REGSTR_VAL_DEVICETYPE_W",
    "REGSTR_VAL_DEVICE_NAME_W",
    "REGSTR_VAL_DEV_NAME_W",
    "REGSTR_VAL_DRIVER_DESC_W",
    "REGSTR_VAL_FRIENDLY_NAME_W",
    "REGSTR_VAL_GENERIC_CAPS_W",
    "REGSTR_VAL_GUID",
    "REGSTR_VAL_GUID_W",
    "REGSTR_VAL_HARDWARE",
    "REGSTR_VAL_HARDWARE_W",
    "REGSTR_VAL_LAUNCHABLE",
    "REGSTR_VAL_LAUNCHABLE_W",
    "REGSTR_VAL_LAUNCH_APPS",
    "REGSTR_VAL_LAUNCH_APPS_W",
    "REGSTR_VAL_SHUTDOWNDELAY",
    "REGSTR_VAL_SHUTDOWNDELAY_W",
    "REGSTR_VAL_TYPE_W",
    "REGSTR_VAL_VENDOR_NAME_W",
    "SEND_TO_FAX_RECIPIENT_ATTACHMENT",
    "STATUS_DISABLE",
    "STATUS_ENABLE",
    "STIEDFL_ALLDEVICES",
    "STIEDFL_ATTACHEDONLY",
    "STIERR_ALREADY_INITIALIZED",
    "STIERR_BADDRIVER",
    "STIERR_BETA_VERSION",
    "STIERR_DEVICENOTREG",
    "STIERR_DEVICE_LOCKED",
    "STIERR_DEVICE_NOTREADY",
    "STIERR_GENERIC",
    "STIERR_HANDLEEXISTS",
    "STIERR_INVALID_DEVICE_NAME",
    "STIERR_INVALID_HW_TYPE",
    "STIERR_INVALID_PARAM",
    "STIERR_NEEDS_LOCK",
    "STIERR_NOEVENTS",
    "STIERR_NOINTERFACE",
    "STIERR_NOTINITIALIZED",
    "STIERR_NOT_INITIALIZED",
    "STIERR_OBJECTNOTFOUND",
    "STIERR_OLD_VERSION",
    "STIERR_OUTOFMEMORY",
    "STIERR_READONLY",
    "STIERR_SHARING_VIOLATION",
    "STIERR_UNSUPPORTED",
    "STINOTIFY",
    "STISUBSCRIBE",
    "STI_ADD_DEVICE_BROADCAST_ACTION",
    "STI_ADD_DEVICE_BROADCAST_STRING",
    "STI_CHANGENOEFFECT",
    "STI_DEVICE_CREATE_BOTH",
    "STI_DEVICE_CREATE_DATA",
    "STI_DEVICE_CREATE_FOR_MONITOR",
    "STI_DEVICE_CREATE_MASK",
    "STI_DEVICE_CREATE_STATUS",
    "STI_DEVICE_INFORMATIONW",
    "STI_DEVICE_MJ_TYPE",
    "STI_DEVICE_MJ_TYPE_StiDeviceTypeDefault",
    "STI_DEVICE_MJ_TYPE_StiDeviceTypeDigitalCamera",
    "STI_DEVICE_MJ_TYPE_StiDeviceTypeScanner",
    "STI_DEVICE_MJ_TYPE_StiDeviceTypeStreamingVideo",
    "STI_DEVICE_STATUS",
    "STI_DEVICE_VALUE_DEFAULT_LAUNCHAPP",
    "STI_DEVICE_VALUE_DEFAULT_LAUNCHAPP_A",
    "STI_DEVICE_VALUE_DISABLE_NOTIFICATIONS",
    "STI_DEVICE_VALUE_DISABLE_NOTIFICATIONS_A",
    "STI_DEVICE_VALUE_ICM_PROFILE",
    "STI_DEVICE_VALUE_ICM_PROFILE_A",
    "STI_DEVICE_VALUE_ISIS_NAME",
    "STI_DEVICE_VALUE_ISIS_NAME_A",
    "STI_DEVICE_VALUE_TIMEOUT",
    "STI_DEVICE_VALUE_TIMEOUT_A",
    "STI_DEVICE_VALUE_TWAIN_NAME",
    "STI_DEVICE_VALUE_TWAIN_NAME_A",
    "STI_DEVSTATUS_EVENTS_STATE",
    "STI_DEVSTATUS_ONLINE_STATE",
    "STI_DEV_CAPS",
    "STI_DIAG",
    "STI_DIAGCODE_HWPRESENCE",
    "STI_ERROR_NO_ERROR",
    "STI_EVENTHANDLING_ENABLED",
    "STI_EVENTHANDLING_PENDING",
    "STI_EVENTHANDLING_POLLING",
    "STI_GENCAP_AUTO_PORTSELECT",
    "STI_GENCAP_GENERATE_ARRIVALEVENT",
    "STI_GENCAP_NOTIFICATIONS",
    "STI_GENCAP_POLLING_NEEDED",
    "STI_GENCAP_SUBSET",
    "STI_GENCAP_WIA",
    "STI_HW_CONFIG_PARALLEL",
    "STI_HW_CONFIG_SCSI",
    "STI_HW_CONFIG_SERIAL",
    "STI_HW_CONFIG_UNKNOWN",
    "STI_HW_CONFIG_USB",
    "STI_MAX_INTERNAL_NAME_LENGTH",
    "STI_NOTCONNECTED",
    "STI_OK",
    "STI_ONLINESTATE_BUSY",
    "STI_ONLINESTATE_ERROR",
    "STI_ONLINESTATE_INITIALIZING",
    "STI_ONLINESTATE_IO_ACTIVE",
    "STI_ONLINESTATE_OFFLINE",
    "STI_ONLINESTATE_OPERATIONAL",
    "STI_ONLINESTATE_PAPER_JAM",
    "STI_ONLINESTATE_PAPER_PROBLEM",
    "STI_ONLINESTATE_PAUSED",
    "STI_ONLINESTATE_PENDING",
    "STI_ONLINESTATE_POWER_SAVE",
    "STI_ONLINESTATE_TRANSFERRING",
    "STI_ONLINESTATE_USER_INTERVENTION",
    "STI_ONLINESTATE_WARMING_UP",
    "STI_RAW_RESERVED",
    "STI_REMOVE_DEVICE_BROADCAST_ACTION",
    "STI_REMOVE_DEVICE_BROADCAST_STRING",
    "STI_SUBSCRIBE_FLAG_EVENT",
    "STI_SUBSCRIBE_FLAG_WINDOW",
    "STI_TRACE_ERROR",
    "STI_TRACE_INFORMATION",
    "STI_TRACE_WARNING",
    "STI_UNICODE",
    "STI_USD_CAPS",
    "STI_USD_GENCAP_NATIVE_PUSHSUPPORT",
    "STI_VERSION",
    "STI_VERSION_FLAG_MASK",
    "STI_VERSION_FLAG_UNICODE",
    "STI_VERSION_MIN_ALLOWED",
    "STI_VERSION_REAL",
    "STI_WIA_DEVICE_INFORMATIONW",
    "SUPPORTS_MSCPLUS_STR",
    "SUPPORTS_MSCPLUS_VAL",
    "SendToFaxRecipient",
    "SendToMode",
    "StiCreateInstanceW",
    "WIA_INCOMPAT_XP",
    "_ERROR_INFOW",
    "far2MANAGE_ARCHIVES",
    "far2MANAGE_CONFIG",
    "far2MANAGE_OUT_JOBS",
    "far2MANAGE_RECEIVE_FOLDER",
    "far2QUERY_ARCHIVES",
    "far2QUERY_CONFIG",
    "far2QUERY_OUT_JOBS",
    "far2SUBMIT_HIGH",
    "far2SUBMIT_LOW",
    "far2SUBMIT_NORMAL",
    "farMANAGE_CONFIG",
    "farMANAGE_IN_ARCHIVE",
    "farMANAGE_JOBS",
    "farMANAGE_OUT_ARCHIVE",
    "farQUERY_CONFIG",
    "farQUERY_IN_ARCHIVE",
    "farQUERY_JOBS",
    "farQUERY_OUT_ARCHIVE",
    "farSUBMIT_HIGH",
    "farSUBMIT_LOW",
    "farSUBMIT_NORMAL",
    "fdrmAUTO_ANSWER",
    "fdrmMANUAL_ANSWER",
    "fdrmNO_ANSWER",
    "frrcANY_CODE",
    "fsAPI_VERSION_0",
    "fsAPI_VERSION_1",
    "fsAPI_VERSION_2",
    "fsAPI_VERSION_3",
    "lDEFAULT_PREFETCH_SIZE",
    "prv_DEFAULT_PREFETCH_SIZE",
    "wcharREASSIGN_RECIPIENTS_DELIMITER",
]
