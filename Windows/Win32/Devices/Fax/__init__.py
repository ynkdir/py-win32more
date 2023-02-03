from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Devices.Fax
import Windows.Win32.Devices.Properties
import Windows.Win32.Foundation
import Windows.Win32.Graphics.Gdi
import Windows.Win32.System.Com
import Windows.Win32.System.IO
import Windows.Win32.System.Registry
import Windows.Win32.UI.Controls
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
prv_DEFAULT_PREFETCH_SIZE: UInt32 = 100
FS_INITIALIZING: UInt32 = 536870912
FS_DIALING: UInt32 = 536870913
FS_TRANSMITTING: UInt32 = 536870914
FS_RECEIVING: UInt32 = 536870916
FS_COMPLETED: UInt32 = 536870920
FS_HANDLED: UInt32 = 536870928
FS_LINE_UNAVAILABLE: UInt32 = 536870944
FS_BUSY: UInt32 = 536870976
FS_NO_ANSWER: UInt32 = 536871040
FS_BAD_ADDRESS: UInt32 = 536871168
FS_NO_DIAL_TONE: UInt32 = 536871424
FS_DISCONNECTED: UInt32 = 536871936
FS_FATAL_ERROR: UInt32 = 536872960
FS_NOT_FAX_CALL: UInt32 = 536875008
FS_CALL_DELAYED: UInt32 = 536879104
FS_CALL_BLACKLISTED: UInt32 = 536887296
FS_USER_ABORT: UInt32 = 538968064
FS_ANSWERED: UInt32 = 545259520
FAXDEVRECEIVE_SIZE: UInt32 = 4096
FAXDEVREPORTSTATUS_SIZE: UInt32 = 4096
MS_FAXROUTE_PRINTING_GUID: String = '{aec1b37c-9af2-11d0-abf7-00c04fd91a4e}'
MS_FAXROUTE_FOLDER_GUID: String = '{92041a90-9af2-11d0-abf7-00c04fd91a4e}'
MS_FAXROUTE_EMAIL_GUID: String = '{6bbf7bfe-9af2-11d0-abf7-00c04fd91a4e}'
FAX_ERR_START: Int32 = 7001
FAX_ERR_SRV_OUTOFMEMORY: Int32 = 7001
FAX_ERR_GROUP_NOT_FOUND: Int32 = 7002
FAX_ERR_BAD_GROUP_CONFIGURATION: Int32 = 7003
FAX_ERR_GROUP_IN_USE: Int32 = 7004
FAX_ERR_RULE_NOT_FOUND: Int32 = 7005
FAX_ERR_NOT_NTFS: Int32 = 7006
FAX_ERR_DIRECTORY_IN_USE: Int32 = 7007
FAX_ERR_FILE_ACCESS_DENIED: Int32 = 7008
FAX_ERR_MESSAGE_NOT_FOUND: Int32 = 7009
FAX_ERR_DEVICE_NUM_LIMIT_EXCEEDED: Int32 = 7010
FAX_ERR_NOT_SUPPORTED_ON_THIS_SKU: Int32 = 7011
FAX_ERR_VERSION_MISMATCH: Int32 = 7012
FAX_ERR_RECIPIENTS_LIMIT: Int32 = 7013
FAX_ERR_END: Int32 = 7013
FAX_E_SRV_OUTOFMEMORY: Windows.Win32.Foundation.HRESULT = -2147214503
FAX_E_GROUP_NOT_FOUND: Windows.Win32.Foundation.HRESULT = -2147214502
FAX_E_BAD_GROUP_CONFIGURATION: Windows.Win32.Foundation.HRESULT = -2147214501
FAX_E_GROUP_IN_USE: Windows.Win32.Foundation.HRESULT = -2147214500
FAX_E_RULE_NOT_FOUND: Windows.Win32.Foundation.HRESULT = -2147214499
FAX_E_NOT_NTFS: Windows.Win32.Foundation.HRESULT = -2147214498
FAX_E_DIRECTORY_IN_USE: Windows.Win32.Foundation.HRESULT = -2147214497
FAX_E_FILE_ACCESS_DENIED: Windows.Win32.Foundation.HRESULT = -2147214496
FAX_E_MESSAGE_NOT_FOUND: Windows.Win32.Foundation.HRESULT = -2147214495
FAX_E_DEVICE_NUM_LIMIT_EXCEEDED: Windows.Win32.Foundation.HRESULT = -2147214494
FAX_E_NOT_SUPPORTED_ON_THIS_SKU: Windows.Win32.Foundation.HRESULT = -2147214493
FAX_E_VERSION_MISMATCH: Windows.Win32.Foundation.HRESULT = -2147214492
FAX_E_RECIPIENTS_LIMIT: Windows.Win32.Foundation.HRESULT = -2147214491
JT_UNKNOWN: UInt32 = 0
JT_SEND: UInt32 = 1
JT_RECEIVE: UInt32 = 2
JT_ROUTING: UInt32 = 3
JT_FAIL_RECEIVE: UInt32 = 4
JS_PENDING: UInt32 = 0
JS_INPROGRESS: UInt32 = 1
JS_DELETING: UInt32 = 2
JS_FAILED: UInt32 = 4
JS_PAUSED: UInt32 = 8
JS_NOLINE: UInt32 = 16
JS_RETRYING: UInt32 = 32
JS_RETRIES_EXCEEDED: UInt32 = 64
FPS_DIALING: UInt32 = 536870913
FPS_SENDING: UInt32 = 536870914
FPS_RECEIVING: UInt32 = 536870916
FPS_COMPLETED: UInt32 = 536870920
FPS_HANDLED: UInt32 = 536870928
FPS_UNAVAILABLE: UInt32 = 536870944
FPS_BUSY: UInt32 = 536870976
FPS_NO_ANSWER: UInt32 = 536871040
FPS_BAD_ADDRESS: UInt32 = 536871168
FPS_NO_DIAL_TONE: UInt32 = 536871424
FPS_DISCONNECTED: UInt32 = 536871936
FPS_FATAL_ERROR: UInt32 = 536872960
FPS_NOT_FAX_CALL: UInt32 = 536875008
FPS_CALL_DELAYED: UInt32 = 536879104
FPS_CALL_BLACKLISTED: UInt32 = 536887296
FPS_INITIALIZING: UInt32 = 536903680
FPS_OFFLINE: UInt32 = 536936448
FPS_RINGING: UInt32 = 537001984
FPS_AVAILABLE: UInt32 = 537919488
FPS_ABORTING: UInt32 = 538968064
FPS_ROUTING: UInt32 = 541065216
FPS_ANSWERED: UInt32 = 545259520
FPF_RECEIVE: UInt32 = 1
FPF_SEND: UInt32 = 2
FPF_VIRTUAL: UInt32 = 4
FEI_DIALING: UInt32 = 1
FEI_SENDING: UInt32 = 2
FEI_RECEIVING: UInt32 = 3
FEI_COMPLETED: UInt32 = 4
FEI_BUSY: UInt32 = 5
FEI_NO_ANSWER: UInt32 = 6
FEI_BAD_ADDRESS: UInt32 = 7
FEI_NO_DIAL_TONE: UInt32 = 8
FEI_DISCONNECTED: UInt32 = 9
FEI_FATAL_ERROR: UInt32 = 10
FEI_NOT_FAX_CALL: UInt32 = 11
FEI_CALL_DELAYED: UInt32 = 12
FEI_CALL_BLACKLISTED: UInt32 = 13
FEI_RINGING: UInt32 = 14
FEI_ABORTING: UInt32 = 15
FEI_ROUTING: UInt32 = 16
FEI_MODEM_POWERED_ON: UInt32 = 17
FEI_MODEM_POWERED_OFF: UInt32 = 18
FEI_IDLE: UInt32 = 19
FEI_FAXSVC_ENDED: UInt32 = 20
FEI_ANSWERED: UInt32 = 21
FEI_JOB_QUEUED: UInt32 = 22
FEI_DELETED: UInt32 = 23
FEI_INITIALIZING: UInt32 = 24
FEI_LINE_UNAVAILABLE: UInt32 = 25
FEI_HANDLED: UInt32 = 26
FEI_FAXSVC_STARTED: UInt32 = 27
FEI_NEVENTS: UInt32 = 27
FAX_JOB_SUBMIT: UInt32 = 1
FAX_JOB_QUERY: UInt32 = 2
FAX_CONFIG_QUERY: UInt32 = 4
FAX_CONFIG_SET: UInt32 = 8
FAX_PORT_QUERY: UInt32 = 16
FAX_PORT_SET: UInt32 = 32
FAX_JOB_MANAGE: UInt32 = 64
CF_MSFAXSRV_DEVICE_ID: String = 'FAXSRV_DeviceID'
CF_MSFAXSRV_FSP_GUID: String = 'FAXSRV_FSPGuid'
CF_MSFAXSRV_SERVER_NAME: String = 'FAXSRV_ServerName'
CF_MSFAXSRV_ROUTEEXT_NAME: String = 'FAXSRV_RoutingExtName'
CF_MSFAXSRV_ROUTING_METHOD_GUID: String = 'FAXSRV_RoutingMethodGuid'
STI_UNICODE: UInt32 = 1
CLSID_Sti: Guid = Guid('b323f8e0-2e68-11d0-90-ea-00-aa-00-60-f8-6c')
GUID_DeviceArrivedLaunch: Guid = Guid('740d9ee6-70f1-11d1-ad-10-00-a0-24-38-ad-48')
GUID_ScanImage: Guid = Guid('a6c5a715-8c6e-11d2-97-7a-00-00-f8-7a-92-6f')
GUID_ScanPrintImage: Guid = Guid('b441f425-8c6e-11d2-97-7a-00-00-f8-7a-92-6f')
GUID_ScanFaxImage: Guid = Guid('c00eb793-8c6e-11d2-97-7a-00-00-f8-7a-92-6f')
GUID_STIUserDefined1: Guid = Guid('c00eb795-8c6e-11d2-97-7a-00-00-f8-7a-92-6f')
GUID_STIUserDefined2: Guid = Guid('c77ae9c5-8c6e-11d2-97-7a-00-00-f8-7a-92-6f')
GUID_STIUserDefined3: Guid = Guid('c77ae9c6-8c6e-11d2-97-7a-00-00-f8-7a-92-6f')
STI_VERSION_FLAG_MASK: UInt32 = 4278190080
STI_VERSION_FLAG_UNICODE: UInt32 = 16777216
STI_VERSION_REAL: UInt32 = 2
STI_VERSION_MIN_ALLOWED: UInt32 = 2
STI_VERSION: UInt32 = 2
STI_MAX_INTERNAL_NAME_LENGTH: UInt32 = 128
STI_GENCAP_COMMON_MASK: UInt32 = 255
STI_GENCAP_NOTIFICATIONS: UInt32 = 1
STI_GENCAP_POLLING_NEEDED: UInt32 = 2
STI_GENCAP_GENERATE_ARRIVALEVENT: UInt32 = 4
STI_GENCAP_AUTO_PORTSELECT: UInt32 = 8
STI_GENCAP_WIA: UInt32 = 16
STI_GENCAP_SUBSET: UInt32 = 32
WIA_INCOMPAT_XP: UInt32 = 1
STI_HW_CONFIG_UNKNOWN: UInt32 = 1
STI_HW_CONFIG_SCSI: UInt32 = 2
STI_HW_CONFIG_USB: UInt32 = 4
STI_HW_CONFIG_SERIAL: UInt32 = 8
STI_HW_CONFIG_PARALLEL: UInt32 = 16
STI_DEVSTATUS_ONLINE_STATE: UInt32 = 1
STI_DEVSTATUS_EVENTS_STATE: UInt32 = 2
STI_ONLINESTATE_OPERATIONAL: UInt32 = 1
STI_ONLINESTATE_PENDING: UInt32 = 2
STI_ONLINESTATE_ERROR: UInt32 = 4
STI_ONLINESTATE_PAUSED: UInt32 = 8
STI_ONLINESTATE_PAPER_JAM: UInt32 = 16
STI_ONLINESTATE_PAPER_PROBLEM: UInt32 = 32
STI_ONLINESTATE_OFFLINE: UInt32 = 64
STI_ONLINESTATE_IO_ACTIVE: UInt32 = 128
STI_ONLINESTATE_BUSY: UInt32 = 256
STI_ONLINESTATE_TRANSFERRING: UInt32 = 512
STI_ONLINESTATE_INITIALIZING: UInt32 = 1024
STI_ONLINESTATE_WARMING_UP: UInt32 = 2048
STI_ONLINESTATE_USER_INTERVENTION: UInt32 = 4096
STI_ONLINESTATE_POWER_SAVE: UInt32 = 8192
STI_EVENTHANDLING_ENABLED: UInt32 = 1
STI_EVENTHANDLING_POLLING: UInt32 = 2
STI_EVENTHANDLING_PENDING: UInt32 = 4
STI_DIAGCODE_HWPRESENCE: UInt32 = 1
STI_TRACE_INFORMATION: UInt32 = 1
STI_TRACE_WARNING: UInt32 = 2
STI_TRACE_ERROR: UInt32 = 4
STI_SUBSCRIBE_FLAG_WINDOW: UInt32 = 1
STI_SUBSCRIBE_FLAG_EVENT: UInt32 = 2
MAX_NOTIFICATION_DATA: UInt32 = 64
STI_ADD_DEVICE_BROADCAST_ACTION: String = 'Arrival'
STI_REMOVE_DEVICE_BROADCAST_ACTION: String = 'Removal'
STI_ADD_DEVICE_BROADCAST_STRING: String = 'STI\\'
STI_REMOVE_DEVICE_BROADCAST_STRING: String = 'STI\\'
STI_DEVICE_CREATE_STATUS: UInt32 = 1
STI_DEVICE_CREATE_DATA: UInt32 = 2
STI_DEVICE_CREATE_BOTH: UInt32 = 3
STI_DEVICE_CREATE_MASK: UInt32 = 65535
STIEDFL_ALLDEVICES: UInt32 = 0
STIEDFL_ATTACHEDONLY: UInt32 = 1
STI_RAW_RESERVED: UInt32 = 4096
STI_OK: Int32 = 0
STI_ERROR_NO_ERROR: Int32 = 0
STI_NOTCONNECTED: Int32 = 1
STI_CHANGENOEFFECT: Int32 = 1
STIERR_OLD_VERSION: Windows.Win32.Foundation.HRESULT = -2147023746
STIERR_BETA_VERSION: Windows.Win32.Foundation.HRESULT = -2147023743
STIERR_BADDRIVER: Windows.Win32.Foundation.HRESULT = -2147024777
STIERR_DEVICENOTREG: Int32 = -2147221164
STIERR_OBJECTNOTFOUND: Windows.Win32.Foundation.HRESULT = -2147024894
STIERR_INVALID_PARAM: Int32 = -2147024809
STIERR_NOINTERFACE: Int32 = -2147467262
STIERR_GENERIC: Int32 = -2147467259
STIERR_OUTOFMEMORY: Int32 = -2147024882
STIERR_UNSUPPORTED: Int32 = -2147467263
STIERR_NOT_INITIALIZED: Windows.Win32.Foundation.HRESULT = -2147024875
STIERR_ALREADY_INITIALIZED: Windows.Win32.Foundation.HRESULT = -2147023649
STIERR_DEVICE_LOCKED: Windows.Win32.Foundation.HRESULT = -2147024863
STIERR_READONLY: Int32 = -2147024891
STIERR_NOTINITIALIZED: Int32 = -2147024891
STIERR_NEEDS_LOCK: Windows.Win32.Foundation.HRESULT = -2147024738
STIERR_SHARING_VIOLATION: Windows.Win32.Foundation.HRESULT = -2147024864
STIERR_HANDLEEXISTS: Windows.Win32.Foundation.HRESULT = -2147024713
STIERR_INVALID_DEVICE_NAME: Windows.Win32.Foundation.HRESULT = -2147024773
STIERR_INVALID_HW_TYPE: Windows.Win32.Foundation.HRESULT = -2147024883
STIERR_NOEVENTS: Windows.Win32.Foundation.HRESULT = -2147024637
STIERR_DEVICE_NOTREADY: Windows.Win32.Foundation.HRESULT = -2147024875
REGSTR_VAL_TYPE_W: String = 'Type'
REGSTR_VAL_VENDOR_NAME_W: String = 'Vendor'
REGSTR_VAL_DEVICETYPE_W: String = 'DeviceType'
REGSTR_VAL_DEVICESUBTYPE_W: String = 'DeviceSubType'
REGSTR_VAL_DEV_NAME_W: String = 'DeviceName'
REGSTR_VAL_DRIVER_DESC_W: String = 'DriverDesc'
REGSTR_VAL_FRIENDLY_NAME_W: String = 'FriendlyName'
REGSTR_VAL_GENERIC_CAPS_W: String = 'Capabilities'
REGSTR_VAL_HARDWARE_W: String = 'HardwareConfig'
REGSTR_VAL_HARDWARE: String = 'HardwareConfig'
REGSTR_VAL_DEVICE_NAME_W: String = 'DriverDesc'
REGSTR_VAL_DATA_W: String = 'DeviceData'
REGSTR_VAL_GUID_W: String = 'GUID'
REGSTR_VAL_GUID: String = 'GUID'
REGSTR_VAL_LAUNCH_APPS_W: String = 'LaunchApplications'
REGSTR_VAL_LAUNCH_APPS: String = 'LaunchApplications'
REGSTR_VAL_LAUNCHABLE_W: String = 'Launchable'
REGSTR_VAL_LAUNCHABLE: String = 'Launchable'
REGSTR_VAL_SHUTDOWNDELAY_W: String = 'ShutdownIfUnusedDelay'
REGSTR_VAL_SHUTDOWNDELAY: String = 'ShutdownIfUnusedDelay'
IS_DIGITAL_CAMERA_STR: String = 'IsDigitalCamera'
IS_DIGITAL_CAMERA_VAL: UInt32 = 1
SUPPORTS_MSCPLUS_STR: String = 'SupportsMSCPlus'
SUPPORTS_MSCPLUS_VAL: UInt32 = 1
STI_DEVICE_VALUE_TWAIN_NAME: String = 'TwainDS'
STI_DEVICE_VALUE_ISIS_NAME: String = 'ISISDriverName'
STI_DEVICE_VALUE_ICM_PROFILE: String = 'ICMProfile'
STI_DEVICE_VALUE_DEFAULT_LAUNCHAPP: String = 'DefaultLaunchApp'
STI_DEVICE_VALUE_TIMEOUT: String = 'PollTimeout'
STI_DEVICE_VALUE_DISABLE_NOTIFICATIONS: String = 'DisableNotifications'
REGSTR_VAL_BAUDRATE: String = 'BaudRate'
STI_DEVICE_VALUE_TWAIN_NAME_A: String = 'TwainDS'
STI_DEVICE_VALUE_ISIS_NAME_A: String = 'ISISDriverName'
STI_DEVICE_VALUE_ICM_PROFILE_A: String = 'ICMProfile'
STI_DEVICE_VALUE_DEFAULT_LAUNCHAPP_A: String = 'DefaultLaunchApp'
STI_DEVICE_VALUE_TIMEOUT_A: String = 'PollTimeout'
STI_DEVICE_VALUE_DISABLE_NOTIFICATIONS_A: String = 'DisableNotifications'
REGSTR_VAL_BAUDRATE_A: String = 'BaudRate'
def DEVPKEY_WIA_DeviceType():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('6bdd1fc6-810f-11d0-be-c7-08-00-2b-e2-09-2f'), pid=2)
def DEVPKEY_WIA_USDClassId():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('6bdd1fc6-810f-11d0-be-c7-08-00-2b-e2-09-2f'), pid=3)
STI_USD_GENCAP_NATIVE_PUSHSUPPORT: UInt32 = 1
STI_DEVICE_CREATE_FOR_MONITOR: UInt32 = 16777216
lDEFAULT_PREFETCH_SIZE: Int32 = 100
wcharREASSIGN_RECIPIENTS_DELIMITER: UInt16 = 59
@winfunctype('WINFAX.dll')
def FaxConnectFaxServerA(MachineName: Windows.Win32.Foundation.PSTR, FaxHandle: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxConnectFaxServerW(MachineName: Windows.Win32.Foundation.PWSTR, FaxHandle: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxClose(FaxHandle: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxOpenPort(FaxHandle: Windows.Win32.Foundation.HANDLE, DeviceId: UInt32, Flags: UInt32, FaxPortHandle: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxCompleteJobParamsA(JobParams: POINTER(POINTER(Windows.Win32.Devices.Fax.FAX_JOB_PARAMA_head)), CoverpageInfo: POINTER(POINTER(Windows.Win32.Devices.Fax.FAX_COVERPAGE_INFOA_head))) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxCompleteJobParamsW(JobParams: POINTER(POINTER(Windows.Win32.Devices.Fax.FAX_JOB_PARAMW_head)), CoverpageInfo: POINTER(POINTER(Windows.Win32.Devices.Fax.FAX_COVERPAGE_INFOW_head))) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxSendDocumentA(FaxHandle: Windows.Win32.Foundation.HANDLE, FileName: Windows.Win32.Foundation.PSTR, JobParams: POINTER(Windows.Win32.Devices.Fax.FAX_JOB_PARAMA_head), CoverpageInfo: POINTER(Windows.Win32.Devices.Fax.FAX_COVERPAGE_INFOA_head), FaxJobId: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxSendDocumentW(FaxHandle: Windows.Win32.Foundation.HANDLE, FileName: Windows.Win32.Foundation.PWSTR, JobParams: POINTER(Windows.Win32.Devices.Fax.FAX_JOB_PARAMW_head), CoverpageInfo: POINTER(Windows.Win32.Devices.Fax.FAX_COVERPAGE_INFOW_head), FaxJobId: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxSendDocumentForBroadcastA(FaxHandle: Windows.Win32.Foundation.HANDLE, FileName: Windows.Win32.Foundation.PSTR, FaxJobId: POINTER(UInt32), FaxRecipientCallback: Windows.Win32.Devices.Fax.PFAX_RECIPIENT_CALLBACKA, Context: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxSendDocumentForBroadcastW(FaxHandle: Windows.Win32.Foundation.HANDLE, FileName: Windows.Win32.Foundation.PWSTR, FaxJobId: POINTER(UInt32), FaxRecipientCallback: Windows.Win32.Devices.Fax.PFAX_RECIPIENT_CALLBACKW, Context: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxEnumJobsA(FaxHandle: Windows.Win32.Foundation.HANDLE, JobEntry: POINTER(POINTER(Windows.Win32.Devices.Fax.FAX_JOB_ENTRYA_head)), JobsReturned: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxEnumJobsW(FaxHandle: Windows.Win32.Foundation.HANDLE, JobEntry: POINTER(POINTER(Windows.Win32.Devices.Fax.FAX_JOB_ENTRYW_head)), JobsReturned: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxGetJobA(FaxHandle: Windows.Win32.Foundation.HANDLE, JobId: UInt32, JobEntry: POINTER(POINTER(Windows.Win32.Devices.Fax.FAX_JOB_ENTRYA_head))) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxGetJobW(FaxHandle: Windows.Win32.Foundation.HANDLE, JobId: UInt32, JobEntry: POINTER(POINTER(Windows.Win32.Devices.Fax.FAX_JOB_ENTRYW_head))) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxSetJobA(FaxHandle: Windows.Win32.Foundation.HANDLE, JobId: UInt32, Command: UInt32, JobEntry: POINTER(Windows.Win32.Devices.Fax.FAX_JOB_ENTRYA_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxSetJobW(FaxHandle: Windows.Win32.Foundation.HANDLE, JobId: UInt32, Command: UInt32, JobEntry: POINTER(Windows.Win32.Devices.Fax.FAX_JOB_ENTRYW_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxGetPageData(FaxHandle: Windows.Win32.Foundation.HANDLE, JobId: UInt32, Buffer: POINTER(c_char_p_no), BufferSize: POINTER(UInt32), ImageWidth: POINTER(UInt32), ImageHeight: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxGetDeviceStatusA(FaxPortHandle: Windows.Win32.Foundation.HANDLE, DeviceStatus: POINTER(POINTER(Windows.Win32.Devices.Fax.FAX_DEVICE_STATUSA_head))) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxGetDeviceStatusW(FaxPortHandle: Windows.Win32.Foundation.HANDLE, DeviceStatus: POINTER(POINTER(Windows.Win32.Devices.Fax.FAX_DEVICE_STATUSW_head))) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxAbort(FaxHandle: Windows.Win32.Foundation.HANDLE, JobId: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxGetConfigurationA(FaxHandle: Windows.Win32.Foundation.HANDLE, FaxConfig: POINTER(POINTER(Windows.Win32.Devices.Fax.FAX_CONFIGURATIONA_head))) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxGetConfigurationW(FaxHandle: Windows.Win32.Foundation.HANDLE, FaxConfig: POINTER(POINTER(Windows.Win32.Devices.Fax.FAX_CONFIGURATIONW_head))) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxSetConfigurationA(FaxHandle: Windows.Win32.Foundation.HANDLE, FaxConfig: POINTER(Windows.Win32.Devices.Fax.FAX_CONFIGURATIONA_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxSetConfigurationW(FaxHandle: Windows.Win32.Foundation.HANDLE, FaxConfig: POINTER(Windows.Win32.Devices.Fax.FAX_CONFIGURATIONW_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxGetLoggingCategoriesA(FaxHandle: Windows.Win32.Foundation.HANDLE, Categories: POINTER(POINTER(Windows.Win32.Devices.Fax.FAX_LOG_CATEGORYA_head)), NumberCategories: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxGetLoggingCategoriesW(FaxHandle: Windows.Win32.Foundation.HANDLE, Categories: POINTER(POINTER(Windows.Win32.Devices.Fax.FAX_LOG_CATEGORYW_head)), NumberCategories: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxSetLoggingCategoriesA(FaxHandle: Windows.Win32.Foundation.HANDLE, Categories: POINTER(Windows.Win32.Devices.Fax.FAX_LOG_CATEGORYA_head), NumberCategories: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxSetLoggingCategoriesW(FaxHandle: Windows.Win32.Foundation.HANDLE, Categories: POINTER(Windows.Win32.Devices.Fax.FAX_LOG_CATEGORYW_head), NumberCategories: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxEnumPortsA(FaxHandle: Windows.Win32.Foundation.HANDLE, PortInfo: POINTER(POINTER(Windows.Win32.Devices.Fax.FAX_PORT_INFOA_head)), PortsReturned: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxEnumPortsW(FaxHandle: Windows.Win32.Foundation.HANDLE, PortInfo: POINTER(POINTER(Windows.Win32.Devices.Fax.FAX_PORT_INFOW_head)), PortsReturned: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxGetPortA(FaxPortHandle: Windows.Win32.Foundation.HANDLE, PortInfo: POINTER(POINTER(Windows.Win32.Devices.Fax.FAX_PORT_INFOA_head))) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxGetPortW(FaxPortHandle: Windows.Win32.Foundation.HANDLE, PortInfo: POINTER(POINTER(Windows.Win32.Devices.Fax.FAX_PORT_INFOW_head))) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxSetPortA(FaxPortHandle: Windows.Win32.Foundation.HANDLE, PortInfo: POINTER(Windows.Win32.Devices.Fax.FAX_PORT_INFOA_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxSetPortW(FaxPortHandle: Windows.Win32.Foundation.HANDLE, PortInfo: POINTER(Windows.Win32.Devices.Fax.FAX_PORT_INFOW_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxEnumRoutingMethodsA(FaxPortHandle: Windows.Win32.Foundation.HANDLE, RoutingMethod: POINTER(POINTER(Windows.Win32.Devices.Fax.FAX_ROUTING_METHODA_head)), MethodsReturned: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxEnumRoutingMethodsW(FaxPortHandle: Windows.Win32.Foundation.HANDLE, RoutingMethod: POINTER(POINTER(Windows.Win32.Devices.Fax.FAX_ROUTING_METHODW_head)), MethodsReturned: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxEnableRoutingMethodA(FaxPortHandle: Windows.Win32.Foundation.HANDLE, RoutingGuid: Windows.Win32.Foundation.PSTR, Enabled: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxEnableRoutingMethodW(FaxPortHandle: Windows.Win32.Foundation.HANDLE, RoutingGuid: Windows.Win32.Foundation.PWSTR, Enabled: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxEnumGlobalRoutingInfoA(FaxHandle: Windows.Win32.Foundation.HANDLE, RoutingInfo: POINTER(POINTER(Windows.Win32.Devices.Fax.FAX_GLOBAL_ROUTING_INFOA_head)), MethodsReturned: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxEnumGlobalRoutingInfoW(FaxHandle: Windows.Win32.Foundation.HANDLE, RoutingInfo: POINTER(POINTER(Windows.Win32.Devices.Fax.FAX_GLOBAL_ROUTING_INFOW_head)), MethodsReturned: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxSetGlobalRoutingInfoA(FaxHandle: Windows.Win32.Foundation.HANDLE, RoutingInfo: POINTER(Windows.Win32.Devices.Fax.FAX_GLOBAL_ROUTING_INFOA_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxSetGlobalRoutingInfoW(FaxHandle: Windows.Win32.Foundation.HANDLE, RoutingInfo: POINTER(Windows.Win32.Devices.Fax.FAX_GLOBAL_ROUTING_INFOW_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxGetRoutingInfoA(FaxPortHandle: Windows.Win32.Foundation.HANDLE, RoutingGuid: Windows.Win32.Foundation.PSTR, RoutingInfoBuffer: POINTER(c_char_p_no), RoutingInfoBufferSize: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxGetRoutingInfoW(FaxPortHandle: Windows.Win32.Foundation.HANDLE, RoutingGuid: Windows.Win32.Foundation.PWSTR, RoutingInfoBuffer: POINTER(c_char_p_no), RoutingInfoBufferSize: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxSetRoutingInfoA(FaxPortHandle: Windows.Win32.Foundation.HANDLE, RoutingGuid: Windows.Win32.Foundation.PSTR, RoutingInfoBuffer: c_char_p_no, RoutingInfoBufferSize: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxSetRoutingInfoW(FaxPortHandle: Windows.Win32.Foundation.HANDLE, RoutingGuid: Windows.Win32.Foundation.PWSTR, RoutingInfoBuffer: c_char_p_no, RoutingInfoBufferSize: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxInitializeEventQueue(FaxHandle: Windows.Win32.Foundation.HANDLE, CompletionPort: Windows.Win32.Foundation.HANDLE, CompletionKey: UIntPtr, hWnd: Windows.Win32.Foundation.HWND, MessageStart: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxFreeBuffer(Buffer: c_void_p) -> Void: ...
@winfunctype('WINFAX.dll')
def FaxStartPrintJobA(PrinterName: Windows.Win32.Foundation.PSTR, PrintInfo: POINTER(Windows.Win32.Devices.Fax.FAX_PRINT_INFOA_head), FaxJobId: POINTER(UInt32), FaxContextInfo: POINTER(Windows.Win32.Devices.Fax.FAX_CONTEXT_INFOA_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxStartPrintJobW(PrinterName: Windows.Win32.Foundation.PWSTR, PrintInfo: POINTER(Windows.Win32.Devices.Fax.FAX_PRINT_INFOW_head), FaxJobId: POINTER(UInt32), FaxContextInfo: POINTER(Windows.Win32.Devices.Fax.FAX_CONTEXT_INFOW_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxPrintCoverPageA(FaxContextInfo: POINTER(Windows.Win32.Devices.Fax.FAX_CONTEXT_INFOA_head), CoverPageInfo: POINTER(Windows.Win32.Devices.Fax.FAX_COVERPAGE_INFOA_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxPrintCoverPageW(FaxContextInfo: POINTER(Windows.Win32.Devices.Fax.FAX_CONTEXT_INFOW_head), CoverPageInfo: POINTER(Windows.Win32.Devices.Fax.FAX_COVERPAGE_INFOW_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxRegisterServiceProviderW(DeviceProvider: Windows.Win32.Foundation.PWSTR, FriendlyName: Windows.Win32.Foundation.PWSTR, ImageName: Windows.Win32.Foundation.PWSTR, TspName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxUnregisterServiceProviderW(DeviceProvider: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxRegisterRoutingExtensionW(FaxHandle: Windows.Win32.Foundation.HANDLE, ExtensionName: Windows.Win32.Foundation.PWSTR, FriendlyName: Windows.Win32.Foundation.PWSTR, ImageName: Windows.Win32.Foundation.PWSTR, CallBack: Windows.Win32.Devices.Fax.PFAX_ROUTING_INSTALLATION_CALLBACKW, Context: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxAccessCheck(FaxHandle: Windows.Win32.Foundation.HANDLE, AccessMask: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('fxsutility.dll')
def CanSendToFaxRecipient() -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('fxsutility.dll')
def SendToFaxRecipient(sndMode: Windows.Win32.Devices.Fax.SendToMode, lpFileName: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('STI.dll')
def StiCreateInstanceW(hinst: Windows.Win32.Foundation.HINSTANCE, dwVer: UInt32, ppSti: POINTER(Windows.Win32.Devices.Fax.IStillImageW_head), punkOuter: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
FAXROUTE_ENABLE = Int32
QUERY_STATUS: FAXROUTE_ENABLE = -1
STATUS_DISABLE: FAXROUTE_ENABLE = 0
STATUS_ENABLE: FAXROUTE_ENABLE = 1
FAX_ACCESS_RIGHTS_ENUM = Int32
farSUBMIT_LOW: FAX_ACCESS_RIGHTS_ENUM = 1
farSUBMIT_NORMAL: FAX_ACCESS_RIGHTS_ENUM = 2
farSUBMIT_HIGH: FAX_ACCESS_RIGHTS_ENUM = 4
farQUERY_JOBS: FAX_ACCESS_RIGHTS_ENUM = 8
farMANAGE_JOBS: FAX_ACCESS_RIGHTS_ENUM = 16
farQUERY_CONFIG: FAX_ACCESS_RIGHTS_ENUM = 32
farMANAGE_CONFIG: FAX_ACCESS_RIGHTS_ENUM = 64
farQUERY_IN_ARCHIVE: FAX_ACCESS_RIGHTS_ENUM = 128
farMANAGE_IN_ARCHIVE: FAX_ACCESS_RIGHTS_ENUM = 256
farQUERY_OUT_ARCHIVE: FAX_ACCESS_RIGHTS_ENUM = 512
farMANAGE_OUT_ARCHIVE: FAX_ACCESS_RIGHTS_ENUM = 1024
FAX_ACCESS_RIGHTS_ENUM_2 = Int32
far2SUBMIT_LOW: FAX_ACCESS_RIGHTS_ENUM_2 = 1
far2SUBMIT_NORMAL: FAX_ACCESS_RIGHTS_ENUM_2 = 2
far2SUBMIT_HIGH: FAX_ACCESS_RIGHTS_ENUM_2 = 4
far2QUERY_OUT_JOBS: FAX_ACCESS_RIGHTS_ENUM_2 = 8
far2MANAGE_OUT_JOBS: FAX_ACCESS_RIGHTS_ENUM_2 = 16
far2QUERY_CONFIG: FAX_ACCESS_RIGHTS_ENUM_2 = 32
far2MANAGE_CONFIG: FAX_ACCESS_RIGHTS_ENUM_2 = 64
far2QUERY_ARCHIVES: FAX_ACCESS_RIGHTS_ENUM_2 = 128
far2MANAGE_ARCHIVES: FAX_ACCESS_RIGHTS_ENUM_2 = 256
far2MANAGE_RECEIVE_FOLDER: FAX_ACCESS_RIGHTS_ENUM_2 = 512
FAX_ACCOUNT_EVENTS_TYPE_ENUM = Int32
FAX_ACCOUNT_EVENTS_TYPE_ENUM_faetNONE: FAX_ACCOUNT_EVENTS_TYPE_ENUM = 0
FAX_ACCOUNT_EVENTS_TYPE_ENUM_faetIN_QUEUE: FAX_ACCOUNT_EVENTS_TYPE_ENUM = 1
FAX_ACCOUNT_EVENTS_TYPE_ENUM_faetOUT_QUEUE: FAX_ACCOUNT_EVENTS_TYPE_ENUM = 2
FAX_ACCOUNT_EVENTS_TYPE_ENUM_faetIN_ARCHIVE: FAX_ACCOUNT_EVENTS_TYPE_ENUM = 4
FAX_ACCOUNT_EVENTS_TYPE_ENUM_faetOUT_ARCHIVE: FAX_ACCOUNT_EVENTS_TYPE_ENUM = 8
FAX_ACCOUNT_EVENTS_TYPE_ENUM_faetFXSSVC_ENDED: FAX_ACCOUNT_EVENTS_TYPE_ENUM = 16
class FAX_CONFIGURATIONA(Structure):
    SizeOfStruct: UInt32
    Retries: UInt32
    RetryDelay: UInt32
    DirtyDays: UInt32
    Branding: Windows.Win32.Foundation.BOOL
    UseDeviceTsid: Windows.Win32.Foundation.BOOL
    ServerCp: Windows.Win32.Foundation.BOOL
    PauseServerQueue: Windows.Win32.Foundation.BOOL
    StartCheapTime: Windows.Win32.Devices.Fax.FAX_TIME
    StopCheapTime: Windows.Win32.Devices.Fax.FAX_TIME
    ArchiveOutgoingFaxes: Windows.Win32.Foundation.BOOL
    ArchiveDirectory: Windows.Win32.Foundation.PSTR
    Reserved: Windows.Win32.Foundation.PSTR
class FAX_CONFIGURATIONW(Structure):
    SizeOfStruct: UInt32
    Retries: UInt32
    RetryDelay: UInt32
    DirtyDays: UInt32
    Branding: Windows.Win32.Foundation.BOOL
    UseDeviceTsid: Windows.Win32.Foundation.BOOL
    ServerCp: Windows.Win32.Foundation.BOOL
    PauseServerQueue: Windows.Win32.Foundation.BOOL
    StartCheapTime: Windows.Win32.Devices.Fax.FAX_TIME
    StopCheapTime: Windows.Win32.Devices.Fax.FAX_TIME
    ArchiveOutgoingFaxes: Windows.Win32.Foundation.BOOL
    ArchiveDirectory: Windows.Win32.Foundation.PWSTR
    Reserved: Windows.Win32.Foundation.PWSTR
class FAX_CONTEXT_INFOA(Structure):
    SizeOfStruct: UInt32
    hDC: Windows.Win32.Graphics.Gdi.HDC
    ServerName: Windows.Win32.Foundation.CHAR * 16
class FAX_CONTEXT_INFOW(Structure):
    SizeOfStruct: UInt32
    hDC: Windows.Win32.Graphics.Gdi.HDC
    ServerName: Char * 16
class FAX_COVERPAGE_INFOA(Structure):
    SizeOfStruct: UInt32
    CoverPageName: Windows.Win32.Foundation.PSTR
    UseServerCoverPage: Windows.Win32.Foundation.BOOL
    RecName: Windows.Win32.Foundation.PSTR
    RecFaxNumber: Windows.Win32.Foundation.PSTR
    RecCompany: Windows.Win32.Foundation.PSTR
    RecStreetAddress: Windows.Win32.Foundation.PSTR
    RecCity: Windows.Win32.Foundation.PSTR
    RecState: Windows.Win32.Foundation.PSTR
    RecZip: Windows.Win32.Foundation.PSTR
    RecCountry: Windows.Win32.Foundation.PSTR
    RecTitle: Windows.Win32.Foundation.PSTR
    RecDepartment: Windows.Win32.Foundation.PSTR
    RecOfficeLocation: Windows.Win32.Foundation.PSTR
    RecHomePhone: Windows.Win32.Foundation.PSTR
    RecOfficePhone: Windows.Win32.Foundation.PSTR
    SdrName: Windows.Win32.Foundation.PSTR
    SdrFaxNumber: Windows.Win32.Foundation.PSTR
    SdrCompany: Windows.Win32.Foundation.PSTR
    SdrAddress: Windows.Win32.Foundation.PSTR
    SdrTitle: Windows.Win32.Foundation.PSTR
    SdrDepartment: Windows.Win32.Foundation.PSTR
    SdrOfficeLocation: Windows.Win32.Foundation.PSTR
    SdrHomePhone: Windows.Win32.Foundation.PSTR
    SdrOfficePhone: Windows.Win32.Foundation.PSTR
    Note: Windows.Win32.Foundation.PSTR
    Subject: Windows.Win32.Foundation.PSTR
    TimeSent: Windows.Win32.Foundation.SYSTEMTIME
    PageCount: UInt32
class FAX_COVERPAGE_INFOW(Structure):
    SizeOfStruct: UInt32
    CoverPageName: Windows.Win32.Foundation.PWSTR
    UseServerCoverPage: Windows.Win32.Foundation.BOOL
    RecName: Windows.Win32.Foundation.PWSTR
    RecFaxNumber: Windows.Win32.Foundation.PWSTR
    RecCompany: Windows.Win32.Foundation.PWSTR
    RecStreetAddress: Windows.Win32.Foundation.PWSTR
    RecCity: Windows.Win32.Foundation.PWSTR
    RecState: Windows.Win32.Foundation.PWSTR
    RecZip: Windows.Win32.Foundation.PWSTR
    RecCountry: Windows.Win32.Foundation.PWSTR
    RecTitle: Windows.Win32.Foundation.PWSTR
    RecDepartment: Windows.Win32.Foundation.PWSTR
    RecOfficeLocation: Windows.Win32.Foundation.PWSTR
    RecHomePhone: Windows.Win32.Foundation.PWSTR
    RecOfficePhone: Windows.Win32.Foundation.PWSTR
    SdrName: Windows.Win32.Foundation.PWSTR
    SdrFaxNumber: Windows.Win32.Foundation.PWSTR
    SdrCompany: Windows.Win32.Foundation.PWSTR
    SdrAddress: Windows.Win32.Foundation.PWSTR
    SdrTitle: Windows.Win32.Foundation.PWSTR
    SdrDepartment: Windows.Win32.Foundation.PWSTR
    SdrOfficeLocation: Windows.Win32.Foundation.PWSTR
    SdrHomePhone: Windows.Win32.Foundation.PWSTR
    SdrOfficePhone: Windows.Win32.Foundation.PWSTR
    Note: Windows.Win32.Foundation.PWSTR
    Subject: Windows.Win32.Foundation.PWSTR
    TimeSent: Windows.Win32.Foundation.SYSTEMTIME
    PageCount: UInt32
FAX_COVERPAGE_TYPE_ENUM = Int32
FAX_COVERPAGE_TYPE_ENUM_fcptNONE: FAX_COVERPAGE_TYPE_ENUM = 0
FAX_COVERPAGE_TYPE_ENUM_fcptLOCAL: FAX_COVERPAGE_TYPE_ENUM = 1
FAX_COVERPAGE_TYPE_ENUM_fcptSERVER: FAX_COVERPAGE_TYPE_ENUM = 2
FAX_DEVICE_RECEIVE_MODE_ENUM = Int32
fdrmNO_ANSWER: FAX_DEVICE_RECEIVE_MODE_ENUM = 0
fdrmAUTO_ANSWER: FAX_DEVICE_RECEIVE_MODE_ENUM = 1
fdrmMANUAL_ANSWER: FAX_DEVICE_RECEIVE_MODE_ENUM = 2
class FAX_DEVICE_STATUSA(Structure):
    SizeOfStruct: UInt32
    CallerId: Windows.Win32.Foundation.PSTR
    Csid: Windows.Win32.Foundation.PSTR
    CurrentPage: UInt32
    DeviceId: UInt32
    DeviceName: Windows.Win32.Foundation.PSTR
    DocumentName: Windows.Win32.Foundation.PSTR
    JobType: UInt32
    PhoneNumber: Windows.Win32.Foundation.PSTR
    RoutingString: Windows.Win32.Foundation.PSTR
    SenderName: Windows.Win32.Foundation.PSTR
    RecipientName: Windows.Win32.Foundation.PSTR
    Size: UInt32
    StartTime: Windows.Win32.Foundation.FILETIME
    Status: UInt32
    StatusString: Windows.Win32.Foundation.PSTR
    SubmittedTime: Windows.Win32.Foundation.FILETIME
    TotalPages: UInt32
    Tsid: Windows.Win32.Foundation.PSTR
    UserName: Windows.Win32.Foundation.PSTR
class FAX_DEVICE_STATUSW(Structure):
    SizeOfStruct: UInt32
    CallerId: Windows.Win32.Foundation.PWSTR
    Csid: Windows.Win32.Foundation.PWSTR
    CurrentPage: UInt32
    DeviceId: UInt32
    DeviceName: Windows.Win32.Foundation.PWSTR
    DocumentName: Windows.Win32.Foundation.PWSTR
    JobType: UInt32
    PhoneNumber: Windows.Win32.Foundation.PWSTR
    RoutingString: Windows.Win32.Foundation.PWSTR
    SenderName: Windows.Win32.Foundation.PWSTR
    RecipientName: Windows.Win32.Foundation.PWSTR
    Size: UInt32
    StartTime: Windows.Win32.Foundation.FILETIME
    Status: UInt32
    StatusString: Windows.Win32.Foundation.PWSTR
    SubmittedTime: Windows.Win32.Foundation.FILETIME
    TotalPages: UInt32
    Tsid: Windows.Win32.Foundation.PWSTR
    UserName: Windows.Win32.Foundation.PWSTR
class FAX_DEV_STATUS(Structure):
    SizeOfStruct: UInt32
    StatusId: UInt32
    StringId: UInt32
    PageCount: UInt32
    CSI: Windows.Win32.Foundation.PWSTR
    CallerId: Windows.Win32.Foundation.PWSTR
    RoutingInfo: Windows.Win32.Foundation.PWSTR
    ErrorCode: UInt32
    Reserved: UInt32 * 3
FAX_ENUM_DELIVERY_REPORT_TYPES = Int32
DRT_NONE: FAX_ENUM_DELIVERY_REPORT_TYPES = 0
DRT_EMAIL: FAX_ENUM_DELIVERY_REPORT_TYPES = 1
DRT_INBOX: FAX_ENUM_DELIVERY_REPORT_TYPES = 2
FAX_ENUM_DEVICE_ID_SOURCE = Int32
DEV_ID_SRC_FAX: FAX_ENUM_DEVICE_ID_SOURCE = 0
DEV_ID_SRC_TAPI: FAX_ENUM_DEVICE_ID_SOURCE = 1
FAX_ENUM_JOB_COMMANDS = Int32
JC_UNKNOWN: FAX_ENUM_JOB_COMMANDS = 0
JC_DELETE: FAX_ENUM_JOB_COMMANDS = 1
JC_PAUSE: FAX_ENUM_JOB_COMMANDS = 2
JC_RESUME: FAX_ENUM_JOB_COMMANDS = 3
FAX_ENUM_JOB_SEND_ATTRIBUTES = Int32
JSA_NOW: FAX_ENUM_JOB_SEND_ATTRIBUTES = 0
JSA_SPECIFIC_TIME: FAX_ENUM_JOB_SEND_ATTRIBUTES = 1
JSA_DISCOUNT_PERIOD: FAX_ENUM_JOB_SEND_ATTRIBUTES = 2
FAX_ENUM_LOG_CATEGORIES = Int32
FAXLOG_CATEGORY_INIT: FAX_ENUM_LOG_CATEGORIES = 1
FAXLOG_CATEGORY_OUTBOUND: FAX_ENUM_LOG_CATEGORIES = 2
FAXLOG_CATEGORY_INBOUND: FAX_ENUM_LOG_CATEGORIES = 3
FAXLOG_CATEGORY_UNKNOWN: FAX_ENUM_LOG_CATEGORIES = 4
FAX_ENUM_LOG_LEVELS = Int32
FAXLOG_LEVEL_NONE: FAX_ENUM_LOG_LEVELS = 0
FAXLOG_LEVEL_MIN: FAX_ENUM_LOG_LEVELS = 1
FAXLOG_LEVEL_MED: FAX_ENUM_LOG_LEVELS = 2
FAXLOG_LEVEL_MAX: FAX_ENUM_LOG_LEVELS = 3
FAX_ENUM_PORT_OPEN_TYPE = Int32
PORT_OPEN_QUERY: FAX_ENUM_PORT_OPEN_TYPE = 1
PORT_OPEN_MODIFY: FAX_ENUM_PORT_OPEN_TYPE = 2
class FAX_EVENTA(Structure):
    SizeOfStruct: UInt32
    TimeStamp: Windows.Win32.Foundation.FILETIME
    DeviceId: UInt32
    EventId: UInt32
    JobId: UInt32
class FAX_EVENTW(Structure):
    SizeOfStruct: UInt32
    TimeStamp: Windows.Win32.Foundation.FILETIME
    DeviceId: UInt32
    EventId: UInt32
    JobId: UInt32
class FAX_GLOBAL_ROUTING_INFOA(Structure):
    SizeOfStruct: UInt32
    Priority: UInt32
    Guid: Windows.Win32.Foundation.PSTR
    FriendlyName: Windows.Win32.Foundation.PSTR
    FunctionName: Windows.Win32.Foundation.PSTR
    ExtensionImageName: Windows.Win32.Foundation.PSTR
    ExtensionFriendlyName: Windows.Win32.Foundation.PSTR
class FAX_GLOBAL_ROUTING_INFOW(Structure):
    SizeOfStruct: UInt32
    Priority: UInt32
    Guid: Windows.Win32.Foundation.PWSTR
    FriendlyName: Windows.Win32.Foundation.PWSTR
    FunctionName: Windows.Win32.Foundation.PWSTR
    ExtensionImageName: Windows.Win32.Foundation.PWSTR
    ExtensionFriendlyName: Windows.Win32.Foundation.PWSTR
FAX_GROUP_STATUS_ENUM = Int32
FAX_GROUP_STATUS_ENUM_fgsALL_DEV_VALID: FAX_GROUP_STATUS_ENUM = 0
FAX_GROUP_STATUS_ENUM_fgsEMPTY: FAX_GROUP_STATUS_ENUM = 1
FAX_GROUP_STATUS_ENUM_fgsALL_DEV_NOT_VALID: FAX_GROUP_STATUS_ENUM = 2
FAX_GROUP_STATUS_ENUM_fgsSOME_DEV_NOT_VALID: FAX_GROUP_STATUS_ENUM = 3
class FAX_JOB_ENTRYA(Structure):
    SizeOfStruct: UInt32
    JobId: UInt32
    UserName: Windows.Win32.Foundation.PSTR
    JobType: UInt32
    QueueStatus: UInt32
    Status: UInt32
    Size: UInt32
    PageCount: UInt32
    RecipientNumber: Windows.Win32.Foundation.PSTR
    RecipientName: Windows.Win32.Foundation.PSTR
    Tsid: Windows.Win32.Foundation.PSTR
    SenderName: Windows.Win32.Foundation.PSTR
    SenderCompany: Windows.Win32.Foundation.PSTR
    SenderDept: Windows.Win32.Foundation.PSTR
    BillingCode: Windows.Win32.Foundation.PSTR
    ScheduleAction: UInt32
    ScheduleTime: Windows.Win32.Foundation.SYSTEMTIME
    DeliveryReportType: UInt32
    DeliveryReportAddress: Windows.Win32.Foundation.PSTR
    DocumentName: Windows.Win32.Foundation.PSTR
class FAX_JOB_ENTRYW(Structure):
    SizeOfStruct: UInt32
    JobId: UInt32
    UserName: Windows.Win32.Foundation.PWSTR
    JobType: UInt32
    QueueStatus: UInt32
    Status: UInt32
    Size: UInt32
    PageCount: UInt32
    RecipientNumber: Windows.Win32.Foundation.PWSTR
    RecipientName: Windows.Win32.Foundation.PWSTR
    Tsid: Windows.Win32.Foundation.PWSTR
    SenderName: Windows.Win32.Foundation.PWSTR
    SenderCompany: Windows.Win32.Foundation.PWSTR
    SenderDept: Windows.Win32.Foundation.PWSTR
    BillingCode: Windows.Win32.Foundation.PWSTR
    ScheduleAction: UInt32
    ScheduleTime: Windows.Win32.Foundation.SYSTEMTIME
    DeliveryReportType: UInt32
    DeliveryReportAddress: Windows.Win32.Foundation.PWSTR
    DocumentName: Windows.Win32.Foundation.PWSTR
FAX_JOB_EXTENDED_STATUS_ENUM = Int32
FAX_JOB_EXTENDED_STATUS_ENUM_fjesNONE: FAX_JOB_EXTENDED_STATUS_ENUM = 0
FAX_JOB_EXTENDED_STATUS_ENUM_fjesDISCONNECTED: FAX_JOB_EXTENDED_STATUS_ENUM = 1
FAX_JOB_EXTENDED_STATUS_ENUM_fjesINITIALIZING: FAX_JOB_EXTENDED_STATUS_ENUM = 2
FAX_JOB_EXTENDED_STATUS_ENUM_fjesDIALING: FAX_JOB_EXTENDED_STATUS_ENUM = 3
FAX_JOB_EXTENDED_STATUS_ENUM_fjesTRANSMITTING: FAX_JOB_EXTENDED_STATUS_ENUM = 4
FAX_JOB_EXTENDED_STATUS_ENUM_fjesANSWERED: FAX_JOB_EXTENDED_STATUS_ENUM = 5
FAX_JOB_EXTENDED_STATUS_ENUM_fjesRECEIVING: FAX_JOB_EXTENDED_STATUS_ENUM = 6
FAX_JOB_EXTENDED_STATUS_ENUM_fjesLINE_UNAVAILABLE: FAX_JOB_EXTENDED_STATUS_ENUM = 7
FAX_JOB_EXTENDED_STATUS_ENUM_fjesBUSY: FAX_JOB_EXTENDED_STATUS_ENUM = 8
FAX_JOB_EXTENDED_STATUS_ENUM_fjesNO_ANSWER: FAX_JOB_EXTENDED_STATUS_ENUM = 9
FAX_JOB_EXTENDED_STATUS_ENUM_fjesBAD_ADDRESS: FAX_JOB_EXTENDED_STATUS_ENUM = 10
FAX_JOB_EXTENDED_STATUS_ENUM_fjesNO_DIAL_TONE: FAX_JOB_EXTENDED_STATUS_ENUM = 11
FAX_JOB_EXTENDED_STATUS_ENUM_fjesFATAL_ERROR: FAX_JOB_EXTENDED_STATUS_ENUM = 12
FAX_JOB_EXTENDED_STATUS_ENUM_fjesCALL_DELAYED: FAX_JOB_EXTENDED_STATUS_ENUM = 13
FAX_JOB_EXTENDED_STATUS_ENUM_fjesCALL_BLACKLISTED: FAX_JOB_EXTENDED_STATUS_ENUM = 14
FAX_JOB_EXTENDED_STATUS_ENUM_fjesNOT_FAX_CALL: FAX_JOB_EXTENDED_STATUS_ENUM = 15
FAX_JOB_EXTENDED_STATUS_ENUM_fjesPARTIALLY_RECEIVED: FAX_JOB_EXTENDED_STATUS_ENUM = 16
FAX_JOB_EXTENDED_STATUS_ENUM_fjesHANDLED: FAX_JOB_EXTENDED_STATUS_ENUM = 17
FAX_JOB_EXTENDED_STATUS_ENUM_fjesCALL_COMPLETED: FAX_JOB_EXTENDED_STATUS_ENUM = 18
FAX_JOB_EXTENDED_STATUS_ENUM_fjesCALL_ABORTED: FAX_JOB_EXTENDED_STATUS_ENUM = 19
FAX_JOB_EXTENDED_STATUS_ENUM_fjesPROPRIETARY: FAX_JOB_EXTENDED_STATUS_ENUM = 16777216
FAX_JOB_OPERATIONS_ENUM = Int32
FAX_JOB_OPERATIONS_ENUM_fjoVIEW: FAX_JOB_OPERATIONS_ENUM = 1
FAX_JOB_OPERATIONS_ENUM_fjoPAUSE: FAX_JOB_OPERATIONS_ENUM = 2
FAX_JOB_OPERATIONS_ENUM_fjoRESUME: FAX_JOB_OPERATIONS_ENUM = 4
FAX_JOB_OPERATIONS_ENUM_fjoRESTART: FAX_JOB_OPERATIONS_ENUM = 8
FAX_JOB_OPERATIONS_ENUM_fjoDELETE: FAX_JOB_OPERATIONS_ENUM = 16
FAX_JOB_OPERATIONS_ENUM_fjoRECIPIENT_INFO: FAX_JOB_OPERATIONS_ENUM = 32
FAX_JOB_OPERATIONS_ENUM_fjoSENDER_INFO: FAX_JOB_OPERATIONS_ENUM = 64
class FAX_JOB_PARAMA(Structure):
    SizeOfStruct: UInt32
    RecipientNumber: Windows.Win32.Foundation.PSTR
    RecipientName: Windows.Win32.Foundation.PSTR
    Tsid: Windows.Win32.Foundation.PSTR
    SenderName: Windows.Win32.Foundation.PSTR
    SenderCompany: Windows.Win32.Foundation.PSTR
    SenderDept: Windows.Win32.Foundation.PSTR
    BillingCode: Windows.Win32.Foundation.PSTR
    ScheduleAction: UInt32
    ScheduleTime: Windows.Win32.Foundation.SYSTEMTIME
    DeliveryReportType: UInt32
    DeliveryReportAddress: Windows.Win32.Foundation.PSTR
    DocumentName: Windows.Win32.Foundation.PSTR
    CallHandle: UInt32
    Reserved: UIntPtr * 3
class FAX_JOB_PARAMW(Structure):
    SizeOfStruct: UInt32
    RecipientNumber: Windows.Win32.Foundation.PWSTR
    RecipientName: Windows.Win32.Foundation.PWSTR
    Tsid: Windows.Win32.Foundation.PWSTR
    SenderName: Windows.Win32.Foundation.PWSTR
    SenderCompany: Windows.Win32.Foundation.PWSTR
    SenderDept: Windows.Win32.Foundation.PWSTR
    BillingCode: Windows.Win32.Foundation.PWSTR
    ScheduleAction: UInt32
    ScheduleTime: Windows.Win32.Foundation.SYSTEMTIME
    DeliveryReportType: UInt32
    DeliveryReportAddress: Windows.Win32.Foundation.PWSTR
    DocumentName: Windows.Win32.Foundation.PWSTR
    CallHandle: UInt32
    Reserved: UIntPtr * 3
FAX_JOB_STATUS_ENUM = Int32
FAX_JOB_STATUS_ENUM_fjsPENDING: FAX_JOB_STATUS_ENUM = 1
FAX_JOB_STATUS_ENUM_fjsINPROGRESS: FAX_JOB_STATUS_ENUM = 2
FAX_JOB_STATUS_ENUM_fjsFAILED: FAX_JOB_STATUS_ENUM = 8
FAX_JOB_STATUS_ENUM_fjsPAUSED: FAX_JOB_STATUS_ENUM = 16
FAX_JOB_STATUS_ENUM_fjsNOLINE: FAX_JOB_STATUS_ENUM = 32
FAX_JOB_STATUS_ENUM_fjsRETRYING: FAX_JOB_STATUS_ENUM = 64
FAX_JOB_STATUS_ENUM_fjsRETRIES_EXCEEDED: FAX_JOB_STATUS_ENUM = 128
FAX_JOB_STATUS_ENUM_fjsCOMPLETED: FAX_JOB_STATUS_ENUM = 256
FAX_JOB_STATUS_ENUM_fjsCANCELED: FAX_JOB_STATUS_ENUM = 512
FAX_JOB_STATUS_ENUM_fjsCANCELING: FAX_JOB_STATUS_ENUM = 1024
FAX_JOB_STATUS_ENUM_fjsROUTING: FAX_JOB_STATUS_ENUM = 2048
FAX_JOB_TYPE_ENUM = Int32
FAX_JOB_TYPE_ENUM_fjtSEND: FAX_JOB_TYPE_ENUM = 0
FAX_JOB_TYPE_ENUM_fjtRECEIVE: FAX_JOB_TYPE_ENUM = 1
FAX_JOB_TYPE_ENUM_fjtROUTING: FAX_JOB_TYPE_ENUM = 2
class FAX_LOG_CATEGORYA(Structure):
    Name: Windows.Win32.Foundation.PSTR
    Category: UInt32
    Level: UInt32
class FAX_LOG_CATEGORYW(Structure):
    Name: Windows.Win32.Foundation.PWSTR
    Category: UInt32
    Level: UInt32
FAX_LOG_LEVEL_ENUM = Int32
FAX_LOG_LEVEL_ENUM_fllNONE: FAX_LOG_LEVEL_ENUM = 0
FAX_LOG_LEVEL_ENUM_fllMIN: FAX_LOG_LEVEL_ENUM = 1
FAX_LOG_LEVEL_ENUM_fllMED: FAX_LOG_LEVEL_ENUM = 2
FAX_LOG_LEVEL_ENUM_fllMAX: FAX_LOG_LEVEL_ENUM = 3
class FAX_PORT_INFOA(Structure):
    SizeOfStruct: UInt32
    DeviceId: UInt32
    State: UInt32
    Flags: UInt32
    Rings: UInt32
    Priority: UInt32
    DeviceName: Windows.Win32.Foundation.PSTR
    Tsid: Windows.Win32.Foundation.PSTR
    Csid: Windows.Win32.Foundation.PSTR
class FAX_PORT_INFOW(Structure):
    SizeOfStruct: UInt32
    DeviceId: UInt32
    State: UInt32
    Flags: UInt32
    Rings: UInt32
    Priority: UInt32
    DeviceName: Windows.Win32.Foundation.PWSTR
    Tsid: Windows.Win32.Foundation.PWSTR
    Csid: Windows.Win32.Foundation.PWSTR
class FAX_PRINT_INFOA(Structure):
    SizeOfStruct: UInt32
    DocName: Windows.Win32.Foundation.PSTR
    RecipientName: Windows.Win32.Foundation.PSTR
    RecipientNumber: Windows.Win32.Foundation.PSTR
    SenderName: Windows.Win32.Foundation.PSTR
    SenderCompany: Windows.Win32.Foundation.PSTR
    SenderDept: Windows.Win32.Foundation.PSTR
    SenderBillingCode: Windows.Win32.Foundation.PSTR
    Reserved: Windows.Win32.Foundation.PSTR
    DrEmailAddress: Windows.Win32.Foundation.PSTR
    OutputFileName: Windows.Win32.Foundation.PSTR
class FAX_PRINT_INFOW(Structure):
    SizeOfStruct: UInt32
    DocName: Windows.Win32.Foundation.PWSTR
    RecipientName: Windows.Win32.Foundation.PWSTR
    RecipientNumber: Windows.Win32.Foundation.PWSTR
    SenderName: Windows.Win32.Foundation.PWSTR
    SenderCompany: Windows.Win32.Foundation.PWSTR
    SenderDept: Windows.Win32.Foundation.PWSTR
    SenderBillingCode: Windows.Win32.Foundation.PWSTR
    Reserved: Windows.Win32.Foundation.PWSTR
    DrEmailAddress: Windows.Win32.Foundation.PWSTR
    OutputFileName: Windows.Win32.Foundation.PWSTR
FAX_PRIORITY_TYPE_ENUM = Int32
FAX_PRIORITY_TYPE_ENUM_fptLOW: FAX_PRIORITY_TYPE_ENUM = 0
FAX_PRIORITY_TYPE_ENUM_fptNORMAL: FAX_PRIORITY_TYPE_ENUM = 1
FAX_PRIORITY_TYPE_ENUM_fptHIGH: FAX_PRIORITY_TYPE_ENUM = 2
FAX_PROVIDER_STATUS_ENUM = Int32
FAX_PROVIDER_STATUS_ENUM_fpsSUCCESS: FAX_PROVIDER_STATUS_ENUM = 0
FAX_PROVIDER_STATUS_ENUM_fpsSERVER_ERROR: FAX_PROVIDER_STATUS_ENUM = 1
FAX_PROVIDER_STATUS_ENUM_fpsBAD_GUID: FAX_PROVIDER_STATUS_ENUM = 2
FAX_PROVIDER_STATUS_ENUM_fpsBAD_VERSION: FAX_PROVIDER_STATUS_ENUM = 3
FAX_PROVIDER_STATUS_ENUM_fpsCANT_LOAD: FAX_PROVIDER_STATUS_ENUM = 4
FAX_PROVIDER_STATUS_ENUM_fpsCANT_LINK: FAX_PROVIDER_STATUS_ENUM = 5
FAX_PROVIDER_STATUS_ENUM_fpsCANT_INIT: FAX_PROVIDER_STATUS_ENUM = 6
FAX_RECEIPT_TYPE_ENUM = Int32
FAX_RECEIPT_TYPE_ENUM_frtNONE: FAX_RECEIPT_TYPE_ENUM = 0
FAX_RECEIPT_TYPE_ENUM_frtMAIL: FAX_RECEIPT_TYPE_ENUM = 1
FAX_RECEIPT_TYPE_ENUM_frtMSGBOX: FAX_RECEIPT_TYPE_ENUM = 4
class FAX_RECEIVE(Structure):
    SizeOfStruct: UInt32
    FileName: Windows.Win32.Foundation.PWSTR
    ReceiverName: Windows.Win32.Foundation.PWSTR
    ReceiverNumber: Windows.Win32.Foundation.PWSTR
    Reserved: UInt32 * 4
class FAX_ROUTE(Structure):
    SizeOfStruct: UInt32
    JobId: UInt32
    ElapsedTime: UInt64
    ReceiveTime: UInt64
    PageCount: UInt32
    Csid: Windows.Win32.Foundation.PWSTR
    Tsid: Windows.Win32.Foundation.PWSTR
    CallerId: Windows.Win32.Foundation.PWSTR
    RoutingInfo: Windows.Win32.Foundation.PWSTR
    ReceiverName: Windows.Win32.Foundation.PWSTR
    ReceiverNumber: Windows.Win32.Foundation.PWSTR
    DeviceName: Windows.Win32.Foundation.PWSTR
    DeviceId: UInt32
    RoutingInfoData: c_char_p_no
    RoutingInfoDataSize: UInt32
class FAX_ROUTE_CALLBACKROUTINES(Structure):
    SizeOfStruct: UInt32
    FaxRouteAddFile: Windows.Win32.Devices.Fax.PFAXROUTEADDFILE
    FaxRouteDeleteFile: Windows.Win32.Devices.Fax.PFAXROUTEDELETEFILE
    FaxRouteGetFile: Windows.Win32.Devices.Fax.PFAXROUTEGETFILE
    FaxRouteEnumFiles: Windows.Win32.Devices.Fax.PFAXROUTEENUMFILES
    FaxRouteModifyRoutingData: Windows.Win32.Devices.Fax.PFAXROUTEMODIFYROUTINGDATA
class FAX_ROUTING_METHODA(Structure):
    SizeOfStruct: UInt32
    DeviceId: UInt32
    Enabled: Windows.Win32.Foundation.BOOL
    DeviceName: Windows.Win32.Foundation.PSTR
    Guid: Windows.Win32.Foundation.PSTR
    FriendlyName: Windows.Win32.Foundation.PSTR
    FunctionName: Windows.Win32.Foundation.PSTR
    ExtensionImageName: Windows.Win32.Foundation.PSTR
    ExtensionFriendlyName: Windows.Win32.Foundation.PSTR
class FAX_ROUTING_METHODW(Structure):
    SizeOfStruct: UInt32
    DeviceId: UInt32
    Enabled: Windows.Win32.Foundation.BOOL
    DeviceName: Windows.Win32.Foundation.PWSTR
    Guid: Windows.Win32.Foundation.PWSTR
    FriendlyName: Windows.Win32.Foundation.PWSTR
    FunctionName: Windows.Win32.Foundation.PWSTR
    ExtensionImageName: Windows.Win32.Foundation.PWSTR
    ExtensionFriendlyName: Windows.Win32.Foundation.PWSTR
FAX_ROUTING_RULE_CODE_ENUM = Int32
frrcANY_CODE: FAX_ROUTING_RULE_CODE_ENUM = 0
FAX_RULE_STATUS_ENUM = Int32
FAX_RULE_STATUS_ENUM_frsVALID: FAX_RULE_STATUS_ENUM = 0
FAX_RULE_STATUS_ENUM_frsEMPTY_GROUP: FAX_RULE_STATUS_ENUM = 1
FAX_RULE_STATUS_ENUM_frsALL_GROUP_DEV_NOT_VALID: FAX_RULE_STATUS_ENUM = 2
FAX_RULE_STATUS_ENUM_frsSOME_GROUP_DEV_NOT_VALID: FAX_RULE_STATUS_ENUM = 3
FAX_RULE_STATUS_ENUM_frsBAD_DEVICE: FAX_RULE_STATUS_ENUM = 4
FAX_SCHEDULE_TYPE_ENUM = Int32
FAX_SCHEDULE_TYPE_ENUM_fstNOW: FAX_SCHEDULE_TYPE_ENUM = 0
FAX_SCHEDULE_TYPE_ENUM_fstSPECIFIC_TIME: FAX_SCHEDULE_TYPE_ENUM = 1
FAX_SCHEDULE_TYPE_ENUM_fstDISCOUNT_PERIOD: FAX_SCHEDULE_TYPE_ENUM = 2
class FAX_SEND(Structure):
    SizeOfStruct: UInt32
    FileName: Windows.Win32.Foundation.PWSTR
    CallerName: Windows.Win32.Foundation.PWSTR
    CallerNumber: Windows.Win32.Foundation.PWSTR
    ReceiverName: Windows.Win32.Foundation.PWSTR
    ReceiverNumber: Windows.Win32.Foundation.PWSTR
    Branding: Windows.Win32.Foundation.BOOL
    CallHandle: UInt32
    Reserved: UInt32 * 3
FAX_SERVER_APIVERSION_ENUM = Int32
fsAPI_VERSION_0: FAX_SERVER_APIVERSION_ENUM = 0
fsAPI_VERSION_1: FAX_SERVER_APIVERSION_ENUM = 65536
fsAPI_VERSION_2: FAX_SERVER_APIVERSION_ENUM = 131072
fsAPI_VERSION_3: FAX_SERVER_APIVERSION_ENUM = 196608
FAX_SERVER_EVENTS_TYPE_ENUM = Int32
FAX_SERVER_EVENTS_TYPE_ENUM_fsetNONE: FAX_SERVER_EVENTS_TYPE_ENUM = 0
FAX_SERVER_EVENTS_TYPE_ENUM_fsetIN_QUEUE: FAX_SERVER_EVENTS_TYPE_ENUM = 1
FAX_SERVER_EVENTS_TYPE_ENUM_fsetOUT_QUEUE: FAX_SERVER_EVENTS_TYPE_ENUM = 2
FAX_SERVER_EVENTS_TYPE_ENUM_fsetCONFIG: FAX_SERVER_EVENTS_TYPE_ENUM = 4
FAX_SERVER_EVENTS_TYPE_ENUM_fsetACTIVITY: FAX_SERVER_EVENTS_TYPE_ENUM = 8
FAX_SERVER_EVENTS_TYPE_ENUM_fsetQUEUE_STATE: FAX_SERVER_EVENTS_TYPE_ENUM = 16
FAX_SERVER_EVENTS_TYPE_ENUM_fsetIN_ARCHIVE: FAX_SERVER_EVENTS_TYPE_ENUM = 32
FAX_SERVER_EVENTS_TYPE_ENUM_fsetOUT_ARCHIVE: FAX_SERVER_EVENTS_TYPE_ENUM = 64
FAX_SERVER_EVENTS_TYPE_ENUM_fsetFXSSVC_ENDED: FAX_SERVER_EVENTS_TYPE_ENUM = 128
FAX_SERVER_EVENTS_TYPE_ENUM_fsetDEVICE_STATUS: FAX_SERVER_EVENTS_TYPE_ENUM = 256
FAX_SERVER_EVENTS_TYPE_ENUM_fsetINCOMING_CALL: FAX_SERVER_EVENTS_TYPE_ENUM = 512
FAX_SMTP_AUTHENTICATION_TYPE_ENUM = Int32
FAX_SMTP_AUTHENTICATION_TYPE_ENUM_fsatANONYMOUS: FAX_SMTP_AUTHENTICATION_TYPE_ENUM = 0
FAX_SMTP_AUTHENTICATION_TYPE_ENUM_fsatBASIC: FAX_SMTP_AUTHENTICATION_TYPE_ENUM = 1
FAX_SMTP_AUTHENTICATION_TYPE_ENUM_fsatNTLM: FAX_SMTP_AUTHENTICATION_TYPE_ENUM = 2
class FAX_TIME(Structure):
    Hour: UInt16
    Minute: UInt16
FaxAccount = Guid('a7e0647f-4524-4464-a5-6d-b9-fe-66-6f-71-5e')
FaxAccountFolders = Guid('85398f49-c034-4a3f-82-1c-db-7d-68-5e-81-29')
FaxAccountIncomingArchive = Guid('14b33db5-4c40-4ecf-9e-f8-a3-60-cb-e8-09-ed')
FaxAccountIncomingQueue = Guid('9bcf6094-b4da-45f4-b8-d6-dd-eb-21-86-65-2c')
FaxAccountOutgoingArchive = Guid('851e7af5-433a-4739-a2-df-ad-24-5c-2c-b9-8e')
FaxAccountOutgoingQueue = Guid('feeceefb-c149-48ba-ba-b8-b7-91-e1-01-f6-2f')
FaxAccountSet = Guid('fbc23c4b-79e0-4291-bc-56-c1-2e-25-3b-bf-3a')
FaxAccounts = Guid('da1f94aa-ee2c-47c0-8f-4f-2a-21-70-75-b7-6e')
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
FaxSecurity = Guid('10c4ddde-abf0-43df-96-4f-7f-3a-c2-1a-4c-7b')
FaxSecurity2 = Guid('735c1248-ec89-4c30-a1-27-65-6e-92-e3-c4-ea')
FaxSender = Guid('265d84d0-1850-4360-b7-c8-75-8b-bb-5f-0b-96')
FaxServer = Guid('cda8acb0-8cf5-4f6c-9b-a2-59-31-d4-0c-8c-ae')
class IFaxAccount(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('68535b33-5dc4-4086-be-26-b7-6f-9b-71-10-06')
    @commethod(7)
    def get_AccountName(pbstrAccountName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Folders(ppFolders: POINTER(Windows.Win32.Devices.Fax.IFaxAccountFolders_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ListenToAccountEvents(EventTypes: Windows.Win32.Devices.Fax.FAX_ACCOUNT_EVENTS_TYPE_ENUM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_RegisteredEvents(pRegisteredEvents: POINTER(Windows.Win32.Devices.Fax.FAX_ACCOUNT_EVENTS_TYPE_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxAccountFolders(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('6463f89d-23d8-46a9-8f-86-c4-7b-77-ca-79-26')
    @commethod(7)
    def get_OutgoingQueue(pFaxOutgoingQueue: POINTER(Windows.Win32.Devices.Fax.IFaxAccountOutgoingQueue_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_IncomingQueue(pFaxIncomingQueue: POINTER(Windows.Win32.Devices.Fax.IFaxAccountIncomingQueue_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_IncomingArchive(pFaxIncomingArchive: POINTER(Windows.Win32.Devices.Fax.IFaxAccountIncomingArchive_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_OutgoingArchive(pFaxOutgoingArchive: POINTER(Windows.Win32.Devices.Fax.IFaxAccountOutgoingArchive_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxAccountIncomingArchive(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('a8a5b6ef-e0d6-4aee-95-5c-91-62-5b-ec-9d-b4')
    @commethod(7)
    def get_SizeLow(plSizeLow: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_SizeHigh(plSizeHigh: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Refresh() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetMessages(lPrefetchSize: Int32, pFaxIncomingMessageIterator: POINTER(Windows.Win32.Devices.Fax.IFaxIncomingMessageIterator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetMessage(bstrMessageId: Windows.Win32.Foundation.BSTR, pFaxIncomingMessage: POINTER(Windows.Win32.Devices.Fax.IFaxIncomingMessage_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxAccountIncomingQueue(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('dd142d92-0186-4a95-a0-90-cb-c3-ea-db-a6-b4')
    @commethod(7)
    def GetJobs(pFaxIncomingJobs: POINTER(Windows.Win32.Devices.Fax.IFaxIncomingJobs_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetJob(bstrJobId: Windows.Win32.Foundation.BSTR, pFaxIncomingJob: POINTER(Windows.Win32.Devices.Fax.IFaxIncomingJob_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxAccountNotify(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('b9b3bc81-ac1b-46f3-b3-9d-0a-dc-30-e1-b7-88')
    @commethod(7)
    def OnIncomingJobAdded(pFaxAccount: Windows.Win32.Devices.Fax.IFaxAccount_head, bstrJobId: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnIncomingJobRemoved(pFaxAccount: Windows.Win32.Devices.Fax.IFaxAccount_head, bstrJobId: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OnIncomingJobChanged(pFaxAccount: Windows.Win32.Devices.Fax.IFaxAccount_head, bstrJobId: Windows.Win32.Foundation.BSTR, pJobStatus: Windows.Win32.Devices.Fax.IFaxJobStatus_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def OnOutgoingJobAdded(pFaxAccount: Windows.Win32.Devices.Fax.IFaxAccount_head, bstrJobId: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def OnOutgoingJobRemoved(pFaxAccount: Windows.Win32.Devices.Fax.IFaxAccount_head, bstrJobId: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def OnOutgoingJobChanged(pFaxAccount: Windows.Win32.Devices.Fax.IFaxAccount_head, bstrJobId: Windows.Win32.Foundation.BSTR, pJobStatus: Windows.Win32.Devices.Fax.IFaxJobStatus_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def OnIncomingMessageAdded(pFaxAccount: Windows.Win32.Devices.Fax.IFaxAccount_head, bstrMessageId: Windows.Win32.Foundation.BSTR, fAddedToReceiveFolder: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def OnIncomingMessageRemoved(pFaxAccount: Windows.Win32.Devices.Fax.IFaxAccount_head, bstrMessageId: Windows.Win32.Foundation.BSTR, fRemovedFromReceiveFolder: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def OnOutgoingMessageAdded(pFaxAccount: Windows.Win32.Devices.Fax.IFaxAccount_head, bstrMessageId: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def OnOutgoingMessageRemoved(pFaxAccount: Windows.Win32.Devices.Fax.IFaxAccount_head, bstrMessageId: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def OnServerShutDown(pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxAccountOutgoingArchive(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('5463076d-ec14-491f-92-6e-b3-ce-da-5e-56-62')
    @commethod(7)
    def get_SizeLow(plSizeLow: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_SizeHigh(plSizeHigh: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Refresh() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetMessages(lPrefetchSize: Int32, pFaxOutgoingMessageIterator: POINTER(Windows.Win32.Devices.Fax.IFaxOutgoingMessageIterator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetMessage(bstrMessageId: Windows.Win32.Foundation.BSTR, pFaxOutgoingMessage: POINTER(Windows.Win32.Devices.Fax.IFaxOutgoingMessage_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxAccountOutgoingQueue(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('0f1424e9-f22d-4553-b7-a5-0d-24-bd-0d-7e-46')
    @commethod(7)
    def GetJobs(pFaxOutgoingJobs: POINTER(Windows.Win32.Devices.Fax.IFaxOutgoingJobs_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetJob(bstrJobId: Windows.Win32.Foundation.BSTR, pFaxOutgoingJob: POINTER(Windows.Win32.Devices.Fax.IFaxOutgoingJob_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxAccountSet(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('7428fbae-841e-47b8-86-f4-22-88-94-6d-ca-1b')
    @commethod(7)
    def GetAccounts(ppFaxAccounts: POINTER(Windows.Win32.Devices.Fax.IFaxAccounts_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetAccount(bstrAccountName: Windows.Win32.Foundation.BSTR, pFaxAccount: POINTER(Windows.Win32.Devices.Fax.IFaxAccount_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AddAccount(bstrAccountName: Windows.Win32.Foundation.BSTR, pFaxAccount: POINTER(Windows.Win32.Devices.Fax.IFaxAccount_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def RemoveAccount(bstrAccountName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxAccounts(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('93ea8162-8be7-42d1-ae-7b-ec-74-e2-d9-89-da')
    @commethod(7)
    def get__NewEnum(ppUnk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(vIndex: Windows.Win32.System.Com.VARIANT, pFaxAccount: POINTER(Windows.Win32.Devices.Fax.IFaxAccount_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(plCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxActivity(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('4b106f97-3df5-40f2-bc-3c-44-cb-81-15-eb-df')
    @commethod(7)
    def get_IncomingMessages(plIncomingMessages: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_RoutingMessages(plRoutingMessages: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_OutgoingMessages(plOutgoingMessages: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_QueuedMessages(plQueuedMessages: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Refresh() -> Windows.Win32.Foundation.HRESULT: ...
class IFaxActivityLogging(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('1e29078b-5a69-497b-95-92-49-b7-e7-fa-dd-b5')
    @commethod(7)
    def get_LogIncoming(pbLogIncoming: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_LogIncoming(bLogIncoming: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_LogOutgoing(pbLogOutgoing: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_LogOutgoing(bLogOutgoing: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_DatabasePath(pbstrDatabasePath: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_DatabasePath(bstrDatabasePath: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Refresh() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def Save() -> Windows.Win32.Foundation.HRESULT: ...
class IFaxConfiguration(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('10f4d0f7-0994-4543-ab-6e-50-69-49-12-8c-40')
    @commethod(7)
    def get_UseArchive(pbUseArchive: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_UseArchive(bUseArchive: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ArchiveLocation(pbstrArchiveLocation: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_ArchiveLocation(bstrArchiveLocation: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_SizeQuotaWarning(pbSizeQuotaWarning: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_SizeQuotaWarning(bSizeQuotaWarning: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_HighQuotaWaterMark(plHighQuotaWaterMark: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_HighQuotaWaterMark(lHighQuotaWaterMark: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_LowQuotaWaterMark(plLowQuotaWaterMark: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_LowQuotaWaterMark(lLowQuotaWaterMark: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_ArchiveAgeLimit(plArchiveAgeLimit: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_ArchiveAgeLimit(lArchiveAgeLimit: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_ArchiveSizeLow(plSizeLow: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_ArchiveSizeHigh(plSizeHigh: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_OutgoingQueueBlocked(pbOutgoingBlocked: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_OutgoingQueueBlocked(bOutgoingBlocked: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_OutgoingQueuePaused(pbOutgoingPaused: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_OutgoingQueuePaused(bOutgoingPaused: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_AllowPersonalCoverPages(pbAllowPersonalCoverPages: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_AllowPersonalCoverPages(bAllowPersonalCoverPages: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_UseDeviceTSID(pbUseDeviceTSID: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def put_UseDeviceTSID(bUseDeviceTSID: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def get_Retries(plRetries: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def put_Retries(lRetries: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_RetryDelay(plRetryDelay: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def put_RetryDelay(lRetryDelay: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_DiscountRateStart(pdateDiscountRateStart: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def put_DiscountRateStart(dateDiscountRateStart: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def get_DiscountRateEnd(pdateDiscountRateEnd: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def put_DiscountRateEnd(dateDiscountRateEnd: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def get_OutgoingQueueAgeLimit(plOutgoingQueueAgeLimit: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def put_OutgoingQueueAgeLimit(lOutgoingQueueAgeLimit: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def get_Branding(pbBranding: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def put_Branding(bBranding: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def get_IncomingQueueBlocked(pbIncomingBlocked: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def put_IncomingQueueBlocked(bIncomingBlocked: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def get_AutoCreateAccountOnConnect(pbAutoCreateAccountOnConnect: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def put_AutoCreateAccountOnConnect(bAutoCreateAccountOnConnect: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def get_IncomingFaxesArePublic(pbIncomingFaxesArePublic: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def put_IncomingFaxesArePublic(bIncomingFaxesArePublic: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def Refresh() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def Save() -> Windows.Win32.Foundation.HRESULT: ...
class IFaxDevice(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('49306c59-b52e-4867-9d-f4-ca-58-41-c9-56-d0')
    @commethod(7)
    def get_Id(plId: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_DeviceName(pbstrDeviceName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ProviderUniqueName(pbstrProviderUniqueName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_PoweredOff(pbPoweredOff: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_ReceivingNow(pbReceivingNow: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_SendingNow(pbSendingNow: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_UsedRoutingMethods(pvUsedRoutingMethods: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_Description(pbstrDescription: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_Description(bstrDescription: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_SendEnabled(pbSendEnabled: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_SendEnabled(bSendEnabled: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_ReceiveMode(pReceiveMode: POINTER(Windows.Win32.Devices.Fax.FAX_DEVICE_RECEIVE_MODE_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def put_ReceiveMode(ReceiveMode: Windows.Win32.Devices.Fax.FAX_DEVICE_RECEIVE_MODE_ENUM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_RingsBeforeAnswer(plRingsBeforeAnswer: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def put_RingsBeforeAnswer(lRingsBeforeAnswer: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_CSID(pbstrCSID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_CSID(bstrCSID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_TSID(pbstrTSID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_TSID(bstrTSID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def Refresh() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def Save() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetExtensionProperty(bstrGUID: Windows.Win32.Foundation.BSTR, pvProperty: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def SetExtensionProperty(bstrGUID: Windows.Win32.Foundation.BSTR, vProperty: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def UseRoutingMethod(bstrMethodGUID: Windows.Win32.Foundation.BSTR, bUse: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_RingingNow(pbRingingNow: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def AnswerCall() -> Windows.Win32.Foundation.HRESULT: ...
class IFaxDeviceIds(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('2f0f813f-4ce9-443e-8c-a1-73-8c-fa-ee-e1-49')
    @commethod(7)
    def get__NewEnum(ppUnk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(lIndex: Int32, plDeviceId: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(plCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Add(lDeviceId: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(lIndex: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetOrder(lDeviceId: Int32, lNewOrder: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxDeviceProvider(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('290eac63-83ec-449c-84-17-f1-48-df-8c-68-2a')
    @commethod(7)
    def get_FriendlyName(pbstrFriendlyName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_ImageName(pbstrImageName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_UniqueName(pbstrUniqueName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_TapiProviderName(pbstrTapiProviderName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_MajorVersion(plMajorVersion: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_MinorVersion(plMinorVersion: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_MajorBuild(plMajorBuild: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_MinorBuild(plMinorBuild: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Debug(pbDebug: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_Status(pStatus: POINTER(Windows.Win32.Devices.Fax.FAX_PROVIDER_STATUS_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_InitErrorCode(plInitErrorCode: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_DeviceIds(pvDeviceIds: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxDeviceProviders(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('9fb76f62-4c7e-43a5-b6-fd-50-28-93-f7-e1-3e')
    @commethod(7)
    def get__NewEnum(ppUnk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(vIndex: Windows.Win32.System.Com.VARIANT, pFaxDeviceProvider: POINTER(Windows.Win32.Devices.Fax.IFaxDeviceProvider_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(plCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxDevices(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('9e46783e-f34f-482e-a3-60-04-16-be-cb-bd-96')
    @commethod(7)
    def get__NewEnum(ppUnk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(vIndex: Windows.Win32.System.Com.VARIANT, pFaxDevice: POINTER(Windows.Win32.Devices.Fax.IFaxDevice_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(plCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_ItemById(lId: Int32, ppFaxDevice: POINTER(Windows.Win32.Devices.Fax.IFaxDevice_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxDocument(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('b207a246-09e3-4a4e-a7-dc-fe-a3-1d-29-45-8f')
    @commethod(7)
    def get_Body(pbstrBody: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Body(bstrBody: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Sender(ppFaxSender: POINTER(Windows.Win32.Devices.Fax.IFaxSender_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Recipients(ppFaxRecipients: POINTER(Windows.Win32.Devices.Fax.IFaxRecipients_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_CoverPage(pbstrCoverPage: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_CoverPage(bstrCoverPage: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Subject(pbstrSubject: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_Subject(bstrSubject: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Note(pbstrNote: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_Note(bstrNote: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_ScheduleTime(pdateScheduleTime: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_ScheduleTime(dateScheduleTime: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_ReceiptAddress(pbstrReceiptAddress: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_ReceiptAddress(bstrReceiptAddress: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_DocumentName(pbstrDocumentName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_DocumentName(bstrDocumentName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_CallHandle(plCallHandle: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_CallHandle(lCallHandle: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_CoverPageType(pCoverPageType: POINTER(Windows.Win32.Devices.Fax.FAX_COVERPAGE_TYPE_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_CoverPageType(CoverPageType: Windows.Win32.Devices.Fax.FAX_COVERPAGE_TYPE_ENUM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_ScheduleType(pScheduleType: POINTER(Windows.Win32.Devices.Fax.FAX_SCHEDULE_TYPE_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def put_ScheduleType(ScheduleType: Windows.Win32.Devices.Fax.FAX_SCHEDULE_TYPE_ENUM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def get_ReceiptType(pReceiptType: POINTER(Windows.Win32.Devices.Fax.FAX_RECEIPT_TYPE_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def put_ReceiptType(ReceiptType: Windows.Win32.Devices.Fax.FAX_RECEIPT_TYPE_ENUM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_GroupBroadcastReceipts(pbUseGrouping: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def put_GroupBroadcastReceipts(bUseGrouping: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_Priority(pPriority: POINTER(Windows.Win32.Devices.Fax.FAX_PRIORITY_TYPE_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def put_Priority(Priority: Windows.Win32.Devices.Fax.FAX_PRIORITY_TYPE_ENUM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def get_TapiConnection(ppTapiConnection: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def putref_TapiConnection(pTapiConnection: Windows.Win32.System.Com.IDispatch_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def Submit(bstrFaxServerName: Windows.Win32.Foundation.BSTR, pvFaxOutgoingJobIDs: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def ConnectedSubmit(pFaxServer: Windows.Win32.Devices.Fax.IFaxServer_head, pvFaxOutgoingJobIDs: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def get_AttachFaxToReceipt(pbAttachFax: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def put_AttachFaxToReceipt(bAttachFax: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxDocument2(c_void_p):
    extends: Windows.Win32.Devices.Fax.IFaxDocument
    Guid = Guid('e1347661-f9ef-4d6d-b4-a5-c0-a0-68-b6-5c-ff')
    @commethod(41)
    def get_SubmissionId(pbstrSubmissionId: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def get_Bodies(pvBodies: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def put_Bodies(vBodies: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def Submit2(bstrFaxServerName: Windows.Win32.Foundation.BSTR, pvFaxOutgoingJobIDs: POINTER(Windows.Win32.System.Com.VARIANT_head), plErrorBodyFile: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def ConnectedSubmit2(pFaxServer: Windows.Win32.Devices.Fax.IFaxServer_head, pvFaxOutgoingJobIDs: POINTER(Windows.Win32.System.Com.VARIANT_head), plErrorBodyFile: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxEventLogging(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('0880d965-20e8-42e4-8e-17-94-4f-19-2c-aa-d4')
    @commethod(7)
    def get_InitEventsLevel(pInitEventLevel: POINTER(Windows.Win32.Devices.Fax.FAX_LOG_LEVEL_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_InitEventsLevel(InitEventLevel: Windows.Win32.Devices.Fax.FAX_LOG_LEVEL_ENUM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_InboundEventsLevel(pInboundEventLevel: POINTER(Windows.Win32.Devices.Fax.FAX_LOG_LEVEL_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_InboundEventsLevel(InboundEventLevel: Windows.Win32.Devices.Fax.FAX_LOG_LEVEL_ENUM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_OutboundEventsLevel(pOutboundEventLevel: POINTER(Windows.Win32.Devices.Fax.FAX_LOG_LEVEL_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_OutboundEventsLevel(OutboundEventLevel: Windows.Win32.Devices.Fax.FAX_LOG_LEVEL_ENUM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_GeneralEventsLevel(pGeneralEventLevel: POINTER(Windows.Win32.Devices.Fax.FAX_LOG_LEVEL_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_GeneralEventsLevel(GeneralEventLevel: Windows.Win32.Devices.Fax.FAX_LOG_LEVEL_ENUM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def Refresh() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Save() -> Windows.Win32.Foundation.HRESULT: ...
class IFaxFolders(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('dce3b2a8-a7ab-42bc-9d-0a-31-49-45-72-61-a0')
    @commethod(7)
    def get_OutgoingQueue(pFaxOutgoingQueue: POINTER(Windows.Win32.Devices.Fax.IFaxOutgoingQueue_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_IncomingQueue(pFaxIncomingQueue: POINTER(Windows.Win32.Devices.Fax.IFaxIncomingQueue_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_IncomingArchive(pFaxIncomingArchive: POINTER(Windows.Win32.Devices.Fax.IFaxIncomingArchive_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_OutgoingArchive(pFaxOutgoingArchive: POINTER(Windows.Win32.Devices.Fax.IFaxOutgoingArchive_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxInboundRouting(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('8148c20f-9d52-45b1-bf-96-38-fc-12-71-35-27')
    @commethod(7)
    def GetExtensions(pFaxInboundRoutingExtensions: POINTER(Windows.Win32.Devices.Fax.IFaxInboundRoutingExtensions_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetMethods(pFaxInboundRoutingMethods: POINTER(Windows.Win32.Devices.Fax.IFaxInboundRoutingMethods_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxInboundRoutingExtension(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('885b5e08-c26c-4ef9-af-83-51-58-0a-75-0b-e1')
    @commethod(7)
    def get_FriendlyName(pbstrFriendlyName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_ImageName(pbstrImageName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_UniqueName(pbstrUniqueName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_MajorVersion(plMajorVersion: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_MinorVersion(plMinorVersion: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_MajorBuild(plMajorBuild: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_MinorBuild(plMinorBuild: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_Debug(pbDebug: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Status(pStatus: POINTER(Windows.Win32.Devices.Fax.FAX_PROVIDER_STATUS_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_InitErrorCode(plInitErrorCode: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_Methods(pvMethods: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxInboundRoutingExtensions(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('2f6c9673-7b26-42de-8e-b0-91-5d-cd-2a-4f-4c')
    @commethod(7)
    def get__NewEnum(ppUnk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(vIndex: Windows.Win32.System.Com.VARIANT, pFaxInboundRoutingExtension: POINTER(Windows.Win32.Devices.Fax.IFaxInboundRoutingExtension_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(plCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxInboundRoutingMethod(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('45700061-ad9d-4776-a8-c4-64-06-54-92-cf-4b')
    @commethod(7)
    def get_Name(pbstrName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_GUID(pbstrGUID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_FunctionName(pbstrFunctionName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_ExtensionFriendlyName(pbstrExtensionFriendlyName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_ExtensionImageName(pbstrExtensionImageName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Priority(plPriority: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_Priority(lPriority: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def Refresh() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def Save() -> Windows.Win32.Foundation.HRESULT: ...
class IFaxInboundRoutingMethods(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('783fca10-8908-4473-9d-69-f6-7f-be-a0-c6-b9')
    @commethod(7)
    def get__NewEnum(ppUnk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(vIndex: Windows.Win32.System.Com.VARIANT, pFaxInboundRoutingMethod: POINTER(Windows.Win32.Devices.Fax.IFaxInboundRoutingMethod_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(plCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxIncomingArchive(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('76062cc7-f714-4fbd-aa-06-ed-6e-4a-4b-70-f3')
    @commethod(7)
    def get_UseArchive(pbUseArchive: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_UseArchive(bUseArchive: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ArchiveFolder(pbstrArchiveFolder: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_ArchiveFolder(bstrArchiveFolder: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_SizeQuotaWarning(pbSizeQuotaWarning: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_SizeQuotaWarning(bSizeQuotaWarning: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_HighQuotaWaterMark(plHighQuotaWaterMark: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_HighQuotaWaterMark(lHighQuotaWaterMark: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_LowQuotaWaterMark(plLowQuotaWaterMark: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_LowQuotaWaterMark(lLowQuotaWaterMark: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_AgeLimit(plAgeLimit: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_AgeLimit(lAgeLimit: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_SizeLow(plSizeLow: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_SizeHigh(plSizeHigh: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def Refresh() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def Save() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetMessages(lPrefetchSize: Int32, pFaxIncomingMessageIterator: POINTER(Windows.Win32.Devices.Fax.IFaxIncomingMessageIterator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetMessage(bstrMessageId: Windows.Win32.Foundation.BSTR, pFaxIncomingMessage: POINTER(Windows.Win32.Devices.Fax.IFaxIncomingMessage_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxIncomingJob(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('207529e6-654a-4916-9f-88-4d-23-2e-e8-a1-07')
    @commethod(7)
    def get_Size(plSize: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Id(pbstrId: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_CurrentPage(plCurrentPage: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_DeviceId(plDeviceId: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Status(pStatus: POINTER(Windows.Win32.Devices.Fax.FAX_JOB_STATUS_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_ExtendedStatusCode(pExtendedStatusCode: POINTER(Windows.Win32.Devices.Fax.FAX_JOB_EXTENDED_STATUS_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_ExtendedStatus(pbstrExtendedStatus: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_AvailableOperations(pAvailableOperations: POINTER(Windows.Win32.Devices.Fax.FAX_JOB_OPERATIONS_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Retries(plRetries: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_TransmissionStart(pdateTransmissionStart: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_TransmissionEnd(pdateTransmissionEnd: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_CSID(pbstrCSID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_TSID(pbstrTSID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_CallerId(pbstrCallerId: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_RoutingInformation(pbstrRoutingInformation: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_JobType(pJobType: POINTER(Windows.Win32.Devices.Fax.FAX_JOB_TYPE_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def Cancel() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def Refresh() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def CopyTiff(bstrTiffPath: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxIncomingJobs(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('011f04e9-4fd6-4c23-95-13-b6-b6-6b-b2-6b-e9')
    @commethod(7)
    def get__NewEnum(ppUnk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(vIndex: Windows.Win32.System.Com.VARIANT, pFaxIncomingJob: POINTER(Windows.Win32.Devices.Fax.IFaxIncomingJob_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(plCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxIncomingMessage(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('7cab88fa-2ef9-4851-b2-f3-1d-14-8f-ed-84-47')
    @commethod(7)
    def get_Id(pbstrId: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Pages(plPages: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Size(plSize: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_DeviceName(pbstrDeviceName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Retries(plRetries: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_TransmissionStart(pdateTransmissionStart: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_TransmissionEnd(pdateTransmissionEnd: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_CSID(pbstrCSID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_TSID(pbstrTSID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_CallerId(pbstrCallerId: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_RoutingInformation(pbstrRoutingInformation: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def CopyTiff(bstrTiffPath: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def Delete() -> Windows.Win32.Foundation.HRESULT: ...
class IFaxIncomingMessage2(c_void_p):
    extends: Windows.Win32.Devices.Fax.IFaxIncomingMessage
    Guid = Guid('f9208503-e2bc-48f3-9e-c0-e6-23-6f-9b-50-9a')
    @commethod(20)
    def get_Subject(pbstrSubject: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def put_Subject(bstrSubject: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_SenderName(pbstrSenderName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_SenderName(bstrSenderName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_SenderFaxNumber(pbstrSenderFaxNumber: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_SenderFaxNumber(bstrSenderFaxNumber: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_HasCoverPage(pbHasCoverPage: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_HasCoverPage(bHasCoverPage: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_Recipients(pbstrRecipients: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def put_Recipients(bstrRecipients: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_WasReAssigned(pbWasReAssigned: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_Read(pbRead: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def put_Read(bRead: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def ReAssign() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def Save() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def Refresh() -> Windows.Win32.Foundation.HRESULT: ...
class IFaxIncomingMessageIterator(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('fd73ecc4-6f06-4f52-82-a8-f7-ba-06-ae-31-08')
    @commethod(7)
    def get_Message(pFaxIncomingMessage: POINTER(Windows.Win32.Devices.Fax.IFaxIncomingMessage_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_PrefetchSize(plPrefetchSize: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_PrefetchSize(lPrefetchSize: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_AtEOF(pbEOF: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def MoveFirst() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def MoveNext() -> Windows.Win32.Foundation.HRESULT: ...
class IFaxIncomingQueue(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('902e64ef-8fd8-4b75-97-25-60-14-df-16-15-45')
    @commethod(7)
    def get_Blocked(pbBlocked: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Blocked(bBlocked: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Refresh() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Save() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetJobs(pFaxIncomingJobs: POINTER(Windows.Win32.Devices.Fax.IFaxIncomingJobs_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetJob(bstrJobId: Windows.Win32.Foundation.BSTR, pFaxIncomingJob: POINTER(Windows.Win32.Devices.Fax.IFaxIncomingJob_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxJobStatus(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('8b86f485-fd7f-4824-88-6b-40-c5-ca-a6-17-cc')
    @commethod(7)
    def get_Status(pStatus: POINTER(Windows.Win32.Devices.Fax.FAX_JOB_STATUS_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Pages(plPages: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Size(plSize: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_CurrentPage(plCurrentPage: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_DeviceId(plDeviceId: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_CSID(pbstrCSID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_TSID(pbstrTSID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_ExtendedStatusCode(pExtendedStatusCode: POINTER(Windows.Win32.Devices.Fax.FAX_JOB_EXTENDED_STATUS_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_ExtendedStatus(pbstrExtendedStatus: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_AvailableOperations(pAvailableOperations: POINTER(Windows.Win32.Devices.Fax.FAX_JOB_OPERATIONS_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_Retries(plRetries: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_JobType(pJobType: POINTER(Windows.Win32.Devices.Fax.FAX_JOB_TYPE_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_ScheduledTime(pdateScheduledTime: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_TransmissionStart(pdateTransmissionStart: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_TransmissionEnd(pdateTransmissionEnd: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_CallerId(pbstrCallerId: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_RoutingInformation(pbstrRoutingInformation: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxLoggingOptions(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('34e64fb9-6b31-4d32-8b-27-d2-86-c0-c3-36-06')
    @commethod(7)
    def get_EventLogging(pFaxEventLogging: POINTER(Windows.Win32.Devices.Fax.IFaxEventLogging_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_ActivityLogging(pFaxActivityLogging: POINTER(Windows.Win32.Devices.Fax.IFaxActivityLogging_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxOutboundRouting(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('25dc05a4-9909-41bd-a9-5b-7e-5d-1d-ec-1d-43')
    @commethod(7)
    def GetGroups(pFaxOutboundRoutingGroups: POINTER(Windows.Win32.Devices.Fax.IFaxOutboundRoutingGroups_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetRules(pFaxOutboundRoutingRules: POINTER(Windows.Win32.Devices.Fax.IFaxOutboundRoutingRules_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxOutboundRoutingGroup(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('ca6289a1-7e25-4f87-9a-0b-93-36-57-34-96-2c')
    @commethod(7)
    def get_Name(pbstrName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Status(pStatus: POINTER(Windows.Win32.Devices.Fax.FAX_GROUP_STATUS_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_DeviceIds(pFaxDeviceIds: POINTER(Windows.Win32.Devices.Fax.IFaxDeviceIds_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxOutboundRoutingGroups(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('235cbef7-c2de-4bfd-b8-da-75-09-7c-82-c8-7f')
    @commethod(7)
    def get__NewEnum(ppUnk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(vIndex: Windows.Win32.System.Com.VARIANT, pFaxOutboundRoutingGroup: POINTER(Windows.Win32.Devices.Fax.IFaxOutboundRoutingGroup_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(plCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Add(bstrName: Windows.Win32.Foundation.BSTR, pFaxOutboundRoutingGroup: POINTER(Windows.Win32.Devices.Fax.IFaxOutboundRoutingGroup_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(vIndex: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxOutboundRoutingRule(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('e1f795d5-07c2-469f-b0-27-ac-ac-c2-32-19-da')
    @commethod(7)
    def get_CountryCode(plCountryCode: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_AreaCode(plAreaCode: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Status(pStatus: POINTER(Windows.Win32.Devices.Fax.FAX_RULE_STATUS_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_UseDevice(pbUseDevice: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_UseDevice(bUseDevice: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_DeviceId(plDeviceId: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_DeviceId(DeviceId: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_GroupName(pbstrGroupName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_GroupName(bstrGroupName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Refresh() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def Save() -> Windows.Win32.Foundation.HRESULT: ...
class IFaxOutboundRoutingRules(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('dcefa1e7-ae7d-4ed6-85-21-36-9e-dc-ca-51-20')
    @commethod(7)
    def get__NewEnum(ppUnk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(lIndex: Int32, pFaxOutboundRoutingRule: POINTER(Windows.Win32.Devices.Fax.IFaxOutboundRoutingRule_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(plCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def ItemByCountryAndArea(lCountryCode: Int32, lAreaCode: Int32, pFaxOutboundRoutingRule: POINTER(Windows.Win32.Devices.Fax.IFaxOutboundRoutingRule_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RemoveByCountryAndArea(lCountryCode: Int32, lAreaCode: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Remove(lIndex: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Add(lCountryCode: Int32, lAreaCode: Int32, bUseDevice: Windows.Win32.Foundation.VARIANT_BOOL, bstrGroupName: Windows.Win32.Foundation.BSTR, lDeviceId: Int32, pFaxOutboundRoutingRule: POINTER(Windows.Win32.Devices.Fax.IFaxOutboundRoutingRule_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxOutgoingArchive(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('c9c28f40-8d80-4e53-81-0f-9a-79-91-9b-49-fd')
    @commethod(7)
    def get_UseArchive(pbUseArchive: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_UseArchive(bUseArchive: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ArchiveFolder(pbstrArchiveFolder: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_ArchiveFolder(bstrArchiveFolder: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_SizeQuotaWarning(pbSizeQuotaWarning: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_SizeQuotaWarning(bSizeQuotaWarning: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_HighQuotaWaterMark(plHighQuotaWaterMark: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_HighQuotaWaterMark(lHighQuotaWaterMark: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_LowQuotaWaterMark(plLowQuotaWaterMark: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_LowQuotaWaterMark(lLowQuotaWaterMark: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_AgeLimit(plAgeLimit: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_AgeLimit(lAgeLimit: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_SizeLow(plSizeLow: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_SizeHigh(plSizeHigh: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def Refresh() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def Save() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetMessages(lPrefetchSize: Int32, pFaxOutgoingMessageIterator: POINTER(Windows.Win32.Devices.Fax.IFaxOutgoingMessageIterator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetMessage(bstrMessageId: Windows.Win32.Foundation.BSTR, pFaxOutgoingMessage: POINTER(Windows.Win32.Devices.Fax.IFaxOutgoingMessage_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxOutgoingJob(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('6356daad-6614-4583-bf-7a-3a-d6-7b-bf-c7-1c')
    @commethod(7)
    def get_Subject(pbstrSubject: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_DocumentName(pbstrDocumentName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Pages(plPages: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Size(plSize: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_SubmissionId(pbstrSubmissionId: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Id(pbstrId: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_OriginalScheduledTime(pdateOriginalScheduledTime: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_SubmissionTime(pdateSubmissionTime: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_ReceiptType(pReceiptType: POINTER(Windows.Win32.Devices.Fax.FAX_RECEIPT_TYPE_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_Priority(pPriority: POINTER(Windows.Win32.Devices.Fax.FAX_PRIORITY_TYPE_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_Sender(ppFaxSender: POINTER(Windows.Win32.Devices.Fax.IFaxSender_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_Recipient(ppFaxRecipient: POINTER(Windows.Win32.Devices.Fax.IFaxRecipient_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_CurrentPage(plCurrentPage: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_DeviceId(plDeviceId: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_Status(pStatus: POINTER(Windows.Win32.Devices.Fax.FAX_JOB_STATUS_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_ExtendedStatusCode(pExtendedStatusCode: POINTER(Windows.Win32.Devices.Fax.FAX_JOB_EXTENDED_STATUS_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_ExtendedStatus(pbstrExtendedStatus: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_AvailableOperations(pAvailableOperations: POINTER(Windows.Win32.Devices.Fax.FAX_JOB_OPERATIONS_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_Retries(plRetries: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_ScheduledTime(pdateScheduledTime: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_TransmissionStart(pdateTransmissionStart: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_TransmissionEnd(pdateTransmissionEnd: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def get_CSID(pbstrCSID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_TSID(pbstrTSID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_GroupBroadcastReceipts(pbGroupBroadcastReceipts: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def Pause() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def Resume() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def Restart() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def CopyTiff(bstrTiffPath: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def Refresh() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def Cancel() -> Windows.Win32.Foundation.HRESULT: ...
class IFaxOutgoingJob2(c_void_p):
    extends: Windows.Win32.Devices.Fax.IFaxOutgoingJob
    Guid = Guid('418a8d96-59a0-4789-b1-76-ed-f3-dc-8f-a8-f7')
    @commethod(38)
    def get_HasCoverPage(pbHasCoverPage: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def get_ReceiptAddress(pbstrReceiptAddress: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def get_ScheduleType(pScheduleType: POINTER(Windows.Win32.Devices.Fax.FAX_SCHEDULE_TYPE_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxOutgoingJobs(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('2c56d8e6-8c2f-4573-94-4c-e5-05-f8-f5-ae-ed')
    @commethod(7)
    def get__NewEnum(ppUnk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(vIndex: Windows.Win32.System.Com.VARIANT, pFaxOutgoingJob: POINTER(Windows.Win32.Devices.Fax.IFaxOutgoingJob_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(plCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxOutgoingMessage(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('f0ea35de-caa5-4a7c-82-c7-2b-60-ba-5f-2b-e2')
    @commethod(7)
    def get_SubmissionId(pbstrSubmissionId: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Id(pbstrId: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Subject(pbstrSubject: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_DocumentName(pbstrDocumentName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Retries(plRetries: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Pages(plPages: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Size(plSize: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_OriginalScheduledTime(pdateOriginalScheduledTime: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_SubmissionTime(pdateSubmissionTime: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_Priority(pPriority: POINTER(Windows.Win32.Devices.Fax.FAX_PRIORITY_TYPE_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_Sender(ppFaxSender: POINTER(Windows.Win32.Devices.Fax.IFaxSender_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_Recipient(ppFaxRecipient: POINTER(Windows.Win32.Devices.Fax.IFaxRecipient_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_DeviceName(pbstrDeviceName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_TransmissionStart(pdateTransmissionStart: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_TransmissionEnd(pdateTransmissionEnd: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_CSID(pbstrCSID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_TSID(pbstrTSID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def CopyTiff(bstrTiffPath: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def Delete() -> Windows.Win32.Foundation.HRESULT: ...
class IFaxOutgoingMessage2(c_void_p):
    extends: Windows.Win32.Devices.Fax.IFaxOutgoingMessage
    Guid = Guid('b37df687-bc88-4b46-b3-be-b4-58-b3-ea-9e-7f')
    @commethod(26)
    def get_HasCoverPage(pbHasCoverPage: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_ReceiptType(pReceiptType: POINTER(Windows.Win32.Devices.Fax.FAX_RECEIPT_TYPE_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_ReceiptAddress(pbstrReceiptAddress: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def get_Read(pbRead: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def put_Read(bRead: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def Save() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def Refresh() -> Windows.Win32.Foundation.HRESULT: ...
class IFaxOutgoingMessageIterator(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('f5ec5d4f-b840-432f-99-80-11-2f-e4-2a-9b-7a')
    @commethod(7)
    def get_Message(pFaxOutgoingMessage: POINTER(Windows.Win32.Devices.Fax.IFaxOutgoingMessage_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_AtEOF(pbEOF: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_PrefetchSize(plPrefetchSize: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_PrefetchSize(lPrefetchSize: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def MoveFirst() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def MoveNext() -> Windows.Win32.Foundation.HRESULT: ...
class IFaxOutgoingQueue(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('80b1df24-d9ac-4333-b3-73-48-7c-ed-c8-0c-e5')
    @commethod(7)
    def get_Blocked(pbBlocked: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Blocked(bBlocked: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Paused(pbPaused: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Paused(bPaused: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_AllowPersonalCoverPages(pbAllowPersonalCoverPages: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_AllowPersonalCoverPages(bAllowPersonalCoverPages: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_UseDeviceTSID(pbUseDeviceTSID: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_UseDeviceTSID(bUseDeviceTSID: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Retries(plRetries: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_Retries(lRetries: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_RetryDelay(plRetryDelay: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_RetryDelay(lRetryDelay: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_DiscountRateStart(pdateDiscountRateStart: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_DiscountRateStart(dateDiscountRateStart: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_DiscountRateEnd(pdateDiscountRateEnd: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_DiscountRateEnd(dateDiscountRateEnd: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_AgeLimit(plAgeLimit: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_AgeLimit(lAgeLimit: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_Branding(pbBranding: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_Branding(bBranding: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def Refresh() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def Save() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def GetJobs(pFaxOutgoingJobs: POINTER(Windows.Win32.Devices.Fax.IFaxOutgoingJobs_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def GetJob(bstrJobId: Windows.Win32.Foundation.BSTR, pFaxOutgoingJob: POINTER(Windows.Win32.Devices.Fax.IFaxOutgoingJob_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxReceiptOptions(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('378efaeb-5fcb-4afb-b2-ee-e1-6e-80-61-44-87')
    @commethod(7)
    def get_AuthenticationType(pType: POINTER(Windows.Win32.Devices.Fax.FAX_SMTP_AUTHENTICATION_TYPE_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_AuthenticationType(Type: Windows.Win32.Devices.Fax.FAX_SMTP_AUTHENTICATION_TYPE_ENUM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_SMTPServer(pbstrSMTPServer: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_SMTPServer(bstrSMTPServer: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_SMTPPort(plSMTPPort: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_SMTPPort(lSMTPPort: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_SMTPSender(pbstrSMTPSender: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_SMTPSender(bstrSMTPSender: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_SMTPUser(pbstrSMTPUser: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_SMTPUser(bstrSMTPUser: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_AllowedReceipts(pAllowedReceipts: POINTER(Windows.Win32.Devices.Fax.FAX_RECEIPT_TYPE_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_AllowedReceipts(AllowedReceipts: Windows.Win32.Devices.Fax.FAX_RECEIPT_TYPE_ENUM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_SMTPPassword(pbstrSMTPPassword: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_SMTPPassword(bstrSMTPPassword: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def Refresh() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def Save() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_UseForInboundRouting(pbUseForInboundRouting: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_UseForInboundRouting(bUseForInboundRouting: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxRecipient(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('9a3da3a0-538d-42b6-94-44-aa-a5-7d-0c-e2-bc')
    @commethod(7)
    def get_FaxNumber(pbstrFaxNumber: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_FaxNumber(bstrFaxNumber: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Name(pbstrName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Name(bstrName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxRecipients(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('b9c9de5a-894e-4492-9f-a3-08-c6-27-c1-1d-5d')
    @commethod(7)
    def get__NewEnum(ppUnk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(lIndex: Int32, ppFaxRecipient: POINTER(Windows.Win32.Devices.Fax.IFaxRecipient_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(plCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Add(bstrFaxNumber: Windows.Win32.Foundation.BSTR, bstrRecipientName: Windows.Win32.Foundation.BSTR, ppFaxRecipient: POINTER(Windows.Win32.Devices.Fax.IFaxRecipient_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(lIndex: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxSecurity(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('77b508c1-09c0-47a2-91-eb-fc-e7-fd-f2-69-0e')
    @commethod(7)
    def get_Descriptor(pvDescriptor: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Descriptor(vDescriptor: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_GrantedRights(pGrantedRights: POINTER(Windows.Win32.Devices.Fax.FAX_ACCESS_RIGHTS_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Refresh() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Save() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_InformationType(plInformationType: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_InformationType(lInformationType: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxSecurity2(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('17d851f4-d09b-48fc-99-c9-8f-24-c4-db-9a-b1')
    @commethod(7)
    def get_Descriptor(pvDescriptor: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Descriptor(vDescriptor: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_GrantedRights(pGrantedRights: POINTER(Windows.Win32.Devices.Fax.FAX_ACCESS_RIGHTS_ENUM_2)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Refresh() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Save() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_InformationType(plInformationType: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_InformationType(lInformationType: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxSender(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('0d879d7d-f57a-4cc6-a6-f9-3e-e5-d5-27-b4-6a')
    @commethod(7)
    def get_BillingCode(pbstrBillingCode: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_BillingCode(bstrBillingCode: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_City(pbstrCity: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_City(bstrCity: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Company(pbstrCompany: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_Company(bstrCompany: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Country(pbstrCountry: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_Country(bstrCountry: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Department(pbstrDepartment: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_Department(bstrDepartment: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_Email(pbstrEmail: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_Email(bstrEmail: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_FaxNumber(pbstrFaxNumber: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_FaxNumber(bstrFaxNumber: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_HomePhone(pbstrHomePhone: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_HomePhone(bstrHomePhone: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_Name(pbstrName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_Name(bstrName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_TSID(pbstrTSID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_TSID(bstrTSID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_OfficePhone(pbstrOfficePhone: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def put_OfficePhone(bstrOfficePhone: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def get_OfficeLocation(pbstrOfficeLocation: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def put_OfficeLocation(bstrOfficeLocation: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_State(pbstrState: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def put_State(bstrState: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_StreetAddress(pbstrStreetAddress: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def put_StreetAddress(bstrStreetAddress: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def get_Title(pbstrTitle: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def put_Title(bstrTitle: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def get_ZipCode(pbstrZipCode: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def put_ZipCode(bstrZipCode: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def LoadDefaultSender() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def SaveDefaultSender() -> Windows.Win32.Foundation.HRESULT: ...
class IFaxServer(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('475b6469-90a5-4878-a5-77-17-a8-6e-8e-34-62')
    @commethod(7)
    def Connect(bstrServerName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_ServerName(pbstrServerName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetDeviceProviders(ppFaxDeviceProviders: POINTER(Windows.Win32.Devices.Fax.IFaxDeviceProviders_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetDevices(ppFaxDevices: POINTER(Windows.Win32.Devices.Fax.IFaxDevices_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_InboundRouting(ppFaxInboundRouting: POINTER(Windows.Win32.Devices.Fax.IFaxInboundRouting_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Folders(pFaxFolders: POINTER(Windows.Win32.Devices.Fax.IFaxFolders_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_LoggingOptions(ppFaxLoggingOptions: POINTER(Windows.Win32.Devices.Fax.IFaxLoggingOptions_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_MajorVersion(plMajorVersion: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_MinorVersion(plMinorVersion: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_MajorBuild(plMajorBuild: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_MinorBuild(plMinorBuild: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_Debug(pbDebug: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_Activity(ppFaxActivity: POINTER(Windows.Win32.Devices.Fax.IFaxActivity_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_OutboundRouting(ppFaxOutboundRouting: POINTER(Windows.Win32.Devices.Fax.IFaxOutboundRouting_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_ReceiptOptions(ppFaxReceiptOptions: POINTER(Windows.Win32.Devices.Fax.IFaxReceiptOptions_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_Security(ppFaxSecurity: POINTER(Windows.Win32.Devices.Fax.IFaxSecurity_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def Disconnect() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetExtensionProperty(bstrGUID: Windows.Win32.Foundation.BSTR, pvProperty: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def SetExtensionProperty(bstrGUID: Windows.Win32.Foundation.BSTR, vProperty: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def ListenToServerEvents(EventTypes: Windows.Win32.Devices.Fax.FAX_SERVER_EVENTS_TYPE_ENUM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def RegisterDeviceProvider(bstrGUID: Windows.Win32.Foundation.BSTR, bstrFriendlyName: Windows.Win32.Foundation.BSTR, bstrImageName: Windows.Win32.Foundation.BSTR, TspName: Windows.Win32.Foundation.BSTR, lFSPIVersion: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def UnregisterDeviceProvider(bstrUniqueName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def RegisterInboundRoutingExtension(bstrExtensionName: Windows.Win32.Foundation.BSTR, bstrFriendlyName: Windows.Win32.Foundation.BSTR, bstrImageName: Windows.Win32.Foundation.BSTR, vMethods: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def UnregisterInboundRoutingExtension(bstrExtensionUniqueName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_RegisteredEvents(pEventTypes: POINTER(Windows.Win32.Devices.Fax.FAX_SERVER_EVENTS_TYPE_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def get_APIVersion(pAPIVersion: POINTER(Windows.Win32.Devices.Fax.FAX_SERVER_APIVERSION_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxServer2(c_void_p):
    extends: Windows.Win32.Devices.Fax.IFaxServer
    Guid = Guid('571ced0f-5609-4f40-91-76-54-7e-3a-72-ca-7c')
    @commethod(33)
    def get_Configuration(ppFaxConfiguration: POINTER(Windows.Win32.Devices.Fax.IFaxConfiguration_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def get_CurrentAccount(ppCurrentAccount: POINTER(Windows.Win32.Devices.Fax.IFaxAccount_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def get_FaxAccountSet(ppFaxAccountSet: POINTER(Windows.Win32.Devices.Fax.IFaxAccountSet_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def get_Security2(ppFaxSecurity2: POINTER(Windows.Win32.Devices.Fax.IFaxSecurity2_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxServerNotify(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('2e037b27-cf8a-4abd-b1-e0-57-04-94-3b-ea-6f')
class IFaxServerNotify2(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('ec9c69b9-5fe7-4805-94-67-82-fc-d9-6a-f9-03')
    @commethod(7)
    def OnIncomingJobAdded(pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head, bstrJobId: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnIncomingJobRemoved(pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head, bstrJobId: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OnIncomingJobChanged(pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head, bstrJobId: Windows.Win32.Foundation.BSTR, pJobStatus: Windows.Win32.Devices.Fax.IFaxJobStatus_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def OnOutgoingJobAdded(pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head, bstrJobId: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def OnOutgoingJobRemoved(pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head, bstrJobId: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def OnOutgoingJobChanged(pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head, bstrJobId: Windows.Win32.Foundation.BSTR, pJobStatus: Windows.Win32.Devices.Fax.IFaxJobStatus_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def OnIncomingMessageAdded(pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head, bstrMessageId: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def OnIncomingMessageRemoved(pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head, bstrMessageId: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def OnOutgoingMessageAdded(pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head, bstrMessageId: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def OnOutgoingMessageRemoved(pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head, bstrMessageId: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def OnReceiptOptionsChange(pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def OnActivityLoggingConfigChange(pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def OnSecurityConfigChange(pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def OnEventLoggingConfigChange(pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def OnOutgoingQueueConfigChange(pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def OnOutgoingArchiveConfigChange(pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def OnIncomingArchiveConfigChange(pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def OnDevicesConfigChange(pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def OnOutboundRoutingGroupsConfigChange(pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def OnOutboundRoutingRulesConfigChange(pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def OnServerActivityChange(pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head, lIncomingMessages: Int32, lRoutingMessages: Int32, lOutgoingMessages: Int32, lQueuedMessages: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def OnQueuesStatusChange(pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head, bOutgoingQueueBlocked: Windows.Win32.Foundation.VARIANT_BOOL, bOutgoingQueuePaused: Windows.Win32.Foundation.VARIANT_BOOL, bIncomingQueueBlocked: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def OnNewCall(pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head, lCallId: Int32, lDeviceId: Int32, bstrCallerId: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def OnServerShutDown(pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def OnDeviceStatusChange(pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head, lDeviceId: Int32, bPoweredOff: Windows.Win32.Foundation.VARIANT_BOOL, bSending: Windows.Win32.Foundation.VARIANT_BOOL, bReceiving: Windows.Win32.Foundation.VARIANT_BOOL, bRinging: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def OnGeneralServerConfigChanged(pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head) -> Windows.Win32.Foundation.HRESULT: ...
class IStiDevice(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('6cfa5a80-2dc8-11d0-90-ea-00-aa-00-60-f8-6c')
    @commethod(3)
    def Initialize(hinst: Windows.Win32.Foundation.HINSTANCE, pwszDeviceName: Windows.Win32.Foundation.PWSTR, dwVersion: UInt32, dwMode: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCapabilities(pDevCaps: POINTER(Windows.Win32.Devices.Fax.STI_DEV_CAPS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetStatus(pDevStatus: POINTER(Windows.Win32.Devices.Fax.STI_DEVICE_STATUS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def DeviceReset() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Diagnostic(pBuffer: POINTER(Windows.Win32.Devices.Fax.STI_DIAG_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Escape(EscapeFunction: UInt32, lpInData: c_void_p, cbInDataSize: UInt32, pOutData: c_void_p, dwOutDataSize: UInt32, pdwActualData: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetLastError(pdwLastDeviceError: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def LockDevice(dwTimeOut: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def UnLockDevice() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def RawReadData(lpBuffer: c_void_p, lpdwNumberOfBytes: POINTER(UInt32), lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def RawWriteData(lpBuffer: c_void_p, nNumberOfBytes: UInt32, lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def RawReadCommand(lpBuffer: c_void_p, lpdwNumberOfBytes: POINTER(UInt32), lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def RawWriteCommand(lpBuffer: c_void_p, nNumberOfBytes: UInt32, lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Subscribe(lpSubsribe: POINTER(Windows.Win32.Devices.Fax.STISUBSCRIBE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetLastNotificationData(lpNotify: POINTER(Windows.Win32.Devices.Fax.STINOTIFY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def UnSubscribe() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetLastErrorInfo(pLastErrorInfo: POINTER(Windows.Win32.Devices.Fax._ERROR_INFOW_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IStiDeviceControl(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('128a9860-52dc-11d0-9e-df-44-45-53-54-00-00')
    @commethod(3)
    def Initialize(dwDeviceType: UInt32, dwMode: UInt32, pwszPortName: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RawReadData(lpBuffer: c_void_p, lpdwNumberOfBytes: POINTER(UInt32), lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RawWriteData(lpBuffer: c_void_p, nNumberOfBytes: UInt32, lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RawReadCommand(lpBuffer: c_void_p, lpdwNumberOfBytes: POINTER(UInt32), lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RawWriteCommand(lpBuffer: c_void_p, nNumberOfBytes: UInt32, lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RawDeviceControl(EscapeFunction: UInt32, lpInData: c_void_p, cbInDataSize: UInt32, pOutData: c_void_p, dwOutDataSize: UInt32, pdwActualData: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetLastError(lpdwLastError: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetMyDevicePortName(lpszDevicePath: Windows.Win32.Foundation.PWSTR, cwDevicePathSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetMyDeviceHandle(lph: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetMyDeviceOpenMode(pdwOpenMode: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def WriteToErrorLog(dwMessageType: UInt32, pszMessage: Windows.Win32.Foundation.PWSTR, dwErrorCode: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IStiUSD(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('0c9bb460-51ac-11d0-90-ea-00-aa-00-60-f8-6c')
    @commethod(3)
    def Initialize(pHelDcb: Windows.Win32.Devices.Fax.IStiDeviceControl_head, dwStiVersion: UInt32, hParametersKey: Windows.Win32.System.Registry.HKEY) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCapabilities(pDevCaps: POINTER(Windows.Win32.Devices.Fax.STI_USD_CAPS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetStatus(pDevStatus: POINTER(Windows.Win32.Devices.Fax.STI_DEVICE_STATUS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def DeviceReset() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Diagnostic(pBuffer: POINTER(Windows.Win32.Devices.Fax.STI_DIAG_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Escape(EscapeFunction: UInt32, lpInData: c_void_p, cbInDataSize: UInt32, pOutData: c_void_p, cbOutDataSize: UInt32, pdwActualData: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetLastError(pdwLastDeviceError: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def LockDevice() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def UnLockDevice() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def RawReadData(lpBuffer: c_void_p, lpdwNumberOfBytes: POINTER(UInt32), lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def RawWriteData(lpBuffer: c_void_p, nNumberOfBytes: UInt32, lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def RawReadCommand(lpBuffer: c_void_p, lpdwNumberOfBytes: POINTER(UInt32), lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def RawWriteCommand(lpBuffer: c_void_p, nNumberOfBytes: UInt32, lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetNotificationHandle(hEvent: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetNotificationData(lpNotify: POINTER(Windows.Win32.Devices.Fax.STINOTIFY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetLastErrorInfo(pLastErrorInfo: POINTER(Windows.Win32.Devices.Fax._ERROR_INFOW_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IStillImageW(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('641bd880-2dc8-11d0-90-ea-00-aa-00-60-f8-6c')
    @commethod(3)
    def Initialize(hinst: Windows.Win32.Foundation.HINSTANCE, dwVersion: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDeviceList(dwType: UInt32, dwFlags: UInt32, pdwItemsReturned: POINTER(UInt32), ppBuffer: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDeviceInfo(pwszDeviceName: Windows.Win32.Foundation.PWSTR, ppBuffer: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateDevice(pwszDeviceName: Windows.Win32.Foundation.PWSTR, dwMode: UInt32, pDevice: POINTER(Windows.Win32.Devices.Fax.IStiDevice_head), punkOuter: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetDeviceValue(pwszDeviceName: Windows.Win32.Foundation.PWSTR, pValueName: Windows.Win32.Foundation.PWSTR, pType: POINTER(UInt32), pData: c_char_p_no, cbData: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetDeviceValue(pwszDeviceName: Windows.Win32.Foundation.PWSTR, pValueName: Windows.Win32.Foundation.PWSTR, Type: UInt32, pData: c_char_p_no, cbData: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetSTILaunchInformation(pwszDeviceName: Windows.Win32.Foundation.PWSTR, pdwEventCode: POINTER(UInt32), pwszEventName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def RegisterLaunchApplication(pwszAppName: Windows.Win32.Foundation.PWSTR, pwszCommandLine: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def UnregisterLaunchApplication(pwszAppName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def EnableHwNotifications(pwszDeviceName: Windows.Win32.Foundation.PWSTR, bNewState: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetHwNotificationState(pwszDeviceName: Windows.Win32.Foundation.PWSTR, pbCurrentState: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def RefreshDeviceBus(pwszDeviceName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def LaunchApplicationForDevice(pwszDeviceName: Windows.Win32.Foundation.PWSTR, pwszAppName: Windows.Win32.Foundation.PWSTR, pStiNotify: POINTER(Windows.Win32.Devices.Fax.STINOTIFY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetupDeviceParameters(param0: POINTER(Windows.Win32.Devices.Fax.STI_DEVICE_INFORMATIONW_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def WriteToErrorLog(dwMessageType: UInt32, pszMessage: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFAXABORT(FaxHandle: Windows.Win32.Foundation.HANDLE, JobId: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXACCESSCHECK(FaxHandle: Windows.Win32.Foundation.HANDLE, AccessMask: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXCLOSE(FaxHandle: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXCOMPLETEJOBPARAMSA(JobParams: POINTER(POINTER(Windows.Win32.Devices.Fax.FAX_JOB_PARAMA_head)), CoverpageInfo: POINTER(POINTER(Windows.Win32.Devices.Fax.FAX_COVERPAGE_INFOA_head))) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXCOMPLETEJOBPARAMSW(JobParams: POINTER(POINTER(Windows.Win32.Devices.Fax.FAX_JOB_PARAMW_head)), CoverpageInfo: POINTER(POINTER(Windows.Win32.Devices.Fax.FAX_COVERPAGE_INFOW_head))) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXCONNECTFAXSERVERA(MachineName: Windows.Win32.Foundation.PSTR, FaxHandle: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXCONNECTFAXSERVERW(MachineName: Windows.Win32.Foundation.PWSTR, FaxHandle: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXDEVABORTOPERATION(param0: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXDEVCONFIGURE(param0: POINTER(Windows.Win32.UI.Controls.HPROPSHEETPAGE)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXDEVENDJOB(param0: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXDEVINITIALIZE(param0: UInt32, param1: Windows.Win32.Foundation.HANDLE, param2: POINTER(Windows.Win32.Devices.Fax.PFAX_LINECALLBACK), param3: Windows.Win32.Devices.Fax.PFAX_SERVICE_CALLBACK) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXDEVRECEIVE(param0: Windows.Win32.Foundation.HANDLE, param1: UInt32, param2: POINTER(Windows.Win32.Devices.Fax.FAX_RECEIVE_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXDEVREPORTSTATUS(param0: Windows.Win32.Foundation.HANDLE, param1: POINTER(Windows.Win32.Devices.Fax.FAX_DEV_STATUS_head), param2: UInt32, param3: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXDEVSEND(param0: Windows.Win32.Foundation.HANDLE, param1: POINTER(Windows.Win32.Devices.Fax.FAX_SEND_head), param2: Windows.Win32.Devices.Fax.PFAX_SEND_CALLBACK) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXDEVSHUTDOWN() -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFAXDEVSTARTJOB(param0: UInt32, param1: UInt32, param2: POINTER(Windows.Win32.Foundation.HANDLE), param3: Windows.Win32.Foundation.HANDLE, param4: UIntPtr) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXDEVVIRTUALDEVICECREATION(DeviceCount: POINTER(UInt32), DeviceNamePrefix: Windows.Win32.Foundation.PWSTR, DeviceIdPrefix: POINTER(UInt32), CompletionPort: Windows.Win32.Foundation.HANDLE, CompletionKey: UIntPtr) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXENABLEROUTINGMETHODA(FaxPortHandle: Windows.Win32.Foundation.HANDLE, RoutingGuid: Windows.Win32.Foundation.PSTR, Enabled: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXENABLEROUTINGMETHODW(FaxPortHandle: Windows.Win32.Foundation.HANDLE, RoutingGuid: Windows.Win32.Foundation.PWSTR, Enabled: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXENUMGLOBALROUTINGINFOA(FaxHandle: Windows.Win32.Foundation.HANDLE, RoutingInfo: POINTER(POINTER(Windows.Win32.Devices.Fax.FAX_GLOBAL_ROUTING_INFOA_head)), MethodsReturned: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXENUMGLOBALROUTINGINFOW(FaxHandle: Windows.Win32.Foundation.HANDLE, RoutingInfo: POINTER(POINTER(Windows.Win32.Devices.Fax.FAX_GLOBAL_ROUTING_INFOW_head)), MethodsReturned: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXENUMJOBSA(FaxHandle: Windows.Win32.Foundation.HANDLE, JobEntry: POINTER(POINTER(Windows.Win32.Devices.Fax.FAX_JOB_ENTRYA_head)), JobsReturned: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXENUMJOBSW(FaxHandle: Windows.Win32.Foundation.HANDLE, JobEntry: POINTER(POINTER(Windows.Win32.Devices.Fax.FAX_JOB_ENTRYW_head)), JobsReturned: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXENUMPORTSA(FaxHandle: Windows.Win32.Foundation.HANDLE, PortInfo: POINTER(POINTER(Windows.Win32.Devices.Fax.FAX_PORT_INFOA_head)), PortsReturned: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXENUMPORTSW(FaxHandle: Windows.Win32.Foundation.HANDLE, PortInfo: POINTER(POINTER(Windows.Win32.Devices.Fax.FAX_PORT_INFOW_head)), PortsReturned: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXENUMROUTINGMETHODSA(FaxPortHandle: Windows.Win32.Foundation.HANDLE, RoutingMethod: POINTER(POINTER(Windows.Win32.Devices.Fax.FAX_ROUTING_METHODA_head)), MethodsReturned: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXENUMROUTINGMETHODSW(FaxPortHandle: Windows.Win32.Foundation.HANDLE, RoutingMethod: POINTER(POINTER(Windows.Win32.Devices.Fax.FAX_ROUTING_METHODW_head)), MethodsReturned: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXFREEBUFFER(Buffer: c_void_p) -> Void: ...
@winfunctype_pointer
def PFAXGETCONFIGURATIONA(FaxHandle: Windows.Win32.Foundation.HANDLE, FaxConfig: POINTER(POINTER(Windows.Win32.Devices.Fax.FAX_CONFIGURATIONA_head))) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXGETCONFIGURATIONW(FaxHandle: Windows.Win32.Foundation.HANDLE, FaxConfig: POINTER(POINTER(Windows.Win32.Devices.Fax.FAX_CONFIGURATIONW_head))) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXGETDEVICESTATUSA(FaxPortHandle: Windows.Win32.Foundation.HANDLE, DeviceStatus: POINTER(POINTER(Windows.Win32.Devices.Fax.FAX_DEVICE_STATUSA_head))) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXGETDEVICESTATUSW(FaxPortHandle: Windows.Win32.Foundation.HANDLE, DeviceStatus: POINTER(POINTER(Windows.Win32.Devices.Fax.FAX_DEVICE_STATUSW_head))) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXGETJOBA(FaxHandle: Windows.Win32.Foundation.HANDLE, JobId: UInt32, JobEntry: POINTER(POINTER(Windows.Win32.Devices.Fax.FAX_JOB_ENTRYA_head))) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXGETJOBW(FaxHandle: Windows.Win32.Foundation.HANDLE, JobId: UInt32, JobEntry: POINTER(POINTER(Windows.Win32.Devices.Fax.FAX_JOB_ENTRYW_head))) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXGETLOGGINGCATEGORIESA(FaxHandle: Windows.Win32.Foundation.HANDLE, Categories: POINTER(POINTER(Windows.Win32.Devices.Fax.FAX_LOG_CATEGORYA_head)), NumberCategories: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXGETLOGGINGCATEGORIESW(FaxHandle: Windows.Win32.Foundation.HANDLE, Categories: POINTER(POINTER(Windows.Win32.Devices.Fax.FAX_LOG_CATEGORYW_head)), NumberCategories: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXGETPAGEDATA(FaxHandle: Windows.Win32.Foundation.HANDLE, JobId: UInt32, Buffer: POINTER(c_char_p_no), BufferSize: POINTER(UInt32), ImageWidth: POINTER(UInt32), ImageHeight: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXGETPORTA(FaxPortHandle: Windows.Win32.Foundation.HANDLE, PortInfo: POINTER(POINTER(Windows.Win32.Devices.Fax.FAX_PORT_INFOA_head))) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXGETPORTW(FaxPortHandle: Windows.Win32.Foundation.HANDLE, PortInfo: POINTER(POINTER(Windows.Win32.Devices.Fax.FAX_PORT_INFOW_head))) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXGETROUTINGINFOA(FaxPortHandle: Windows.Win32.Foundation.HANDLE, RoutingGuid: Windows.Win32.Foundation.PSTR, RoutingInfoBuffer: POINTER(c_char_p_no), RoutingInfoBufferSize: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXGETROUTINGINFOW(FaxPortHandle: Windows.Win32.Foundation.HANDLE, RoutingGuid: Windows.Win32.Foundation.PWSTR, RoutingInfoBuffer: POINTER(c_char_p_no), RoutingInfoBufferSize: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXINITIALIZEEVENTQUEUE(FaxHandle: Windows.Win32.Foundation.HANDLE, CompletionPort: Windows.Win32.Foundation.HANDLE, CompletionKey: UIntPtr, hWnd: Windows.Win32.Foundation.HWND, MessageStart: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXOPENPORT(FaxHandle: Windows.Win32.Foundation.HANDLE, DeviceId: UInt32, Flags: UInt32, FaxPortHandle: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXPRINTCOVERPAGEA(FaxContextInfo: POINTER(Windows.Win32.Devices.Fax.FAX_CONTEXT_INFOA_head), CoverPageInfo: POINTER(Windows.Win32.Devices.Fax.FAX_COVERPAGE_INFOA_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXPRINTCOVERPAGEW(FaxContextInfo: POINTER(Windows.Win32.Devices.Fax.FAX_CONTEXT_INFOW_head), CoverPageInfo: POINTER(Windows.Win32.Devices.Fax.FAX_COVERPAGE_INFOW_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXREGISTERROUTINGEXTENSIONW(FaxHandle: Windows.Win32.Foundation.HANDLE, ExtensionName: Windows.Win32.Foundation.PWSTR, FriendlyName: Windows.Win32.Foundation.PWSTR, ImageName: Windows.Win32.Foundation.PWSTR, CallBack: Windows.Win32.Devices.Fax.PFAX_ROUTING_INSTALLATION_CALLBACKW, Context: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXREGISTERSERVICEPROVIDERW(DeviceProvider: Windows.Win32.Foundation.PWSTR, FriendlyName: Windows.Win32.Foundation.PWSTR, ImageName: Windows.Win32.Foundation.PWSTR, TspName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXROUTEADDFILE(JobId: UInt32, FileName: Windows.Win32.Foundation.PWSTR, Guid: POINTER(Guid)) -> Int32: ...
@winfunctype_pointer
def PFAXROUTEDELETEFILE(JobId: UInt32, FileName: Windows.Win32.Foundation.PWSTR) -> Int32: ...
@winfunctype_pointer
def PFAXROUTEDEVICECHANGENOTIFICATION(param0: UInt32, param1: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXROUTEDEVICEENABLE(param0: Windows.Win32.Foundation.PWSTR, param1: UInt32, param2: Int32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXROUTEENUMFILE(JobId: UInt32, GuidOwner: POINTER(Guid), GuidCaller: POINTER(Guid), FileName: Windows.Win32.Foundation.PWSTR, Context: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXROUTEENUMFILES(JobId: UInt32, Guid: POINTER(Guid), FileEnumerator: Windows.Win32.Devices.Fax.PFAXROUTEENUMFILE, Context: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXROUTEGETFILE(JobId: UInt32, Index: UInt32, FileNameBuffer: Windows.Win32.Foundation.PWSTR, RequiredSize: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXROUTEGETROUTINGINFO(param0: Windows.Win32.Foundation.PWSTR, param1: UInt32, param2: c_char_p_no, param3: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXROUTEINITIALIZE(param0: Windows.Win32.Foundation.HANDLE, param1: POINTER(Windows.Win32.Devices.Fax.FAX_ROUTE_CALLBACKROUTINES_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXROUTEMETHOD(param0: POINTER(Windows.Win32.Devices.Fax.FAX_ROUTE_head), param1: POINTER(c_void_p), param2: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXROUTEMODIFYROUTINGDATA(JobId: UInt32, RoutingGuid: Windows.Win32.Foundation.PWSTR, RoutingData: c_char_p_no, RoutingDataSize: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXROUTESETROUTINGINFO(param0: Windows.Win32.Foundation.PWSTR, param1: UInt32, param2: c_char_p_no, param3: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXSENDDOCUMENTA(FaxHandle: Windows.Win32.Foundation.HANDLE, FileName: Windows.Win32.Foundation.PSTR, JobParams: POINTER(Windows.Win32.Devices.Fax.FAX_JOB_PARAMA_head), CoverpageInfo: POINTER(Windows.Win32.Devices.Fax.FAX_COVERPAGE_INFOA_head), FaxJobId: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXSENDDOCUMENTFORBROADCASTA(FaxHandle: Windows.Win32.Foundation.HANDLE, FileName: Windows.Win32.Foundation.PSTR, FaxJobId: POINTER(UInt32), FaxRecipientCallback: Windows.Win32.Devices.Fax.PFAX_RECIPIENT_CALLBACKA, Context: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXSENDDOCUMENTFORBROADCASTW(FaxHandle: Windows.Win32.Foundation.HANDLE, FileName: Windows.Win32.Foundation.PWSTR, FaxJobId: POINTER(UInt32), FaxRecipientCallback: Windows.Win32.Devices.Fax.PFAX_RECIPIENT_CALLBACKW, Context: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXSENDDOCUMENTW(FaxHandle: Windows.Win32.Foundation.HANDLE, FileName: Windows.Win32.Foundation.PWSTR, JobParams: POINTER(Windows.Win32.Devices.Fax.FAX_JOB_PARAMW_head), CoverpageInfo: POINTER(Windows.Win32.Devices.Fax.FAX_COVERPAGE_INFOW_head), FaxJobId: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXSETCONFIGURATIONA(FaxHandle: Windows.Win32.Foundation.HANDLE, FaxConfig: POINTER(Windows.Win32.Devices.Fax.FAX_CONFIGURATIONA_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXSETCONFIGURATIONW(FaxHandle: Windows.Win32.Foundation.HANDLE, FaxConfig: POINTER(Windows.Win32.Devices.Fax.FAX_CONFIGURATIONW_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXSETGLOBALROUTINGINFOA(FaxPortHandle: Windows.Win32.Foundation.HANDLE, RoutingInfo: POINTER(Windows.Win32.Devices.Fax.FAX_GLOBAL_ROUTING_INFOA_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXSETGLOBALROUTINGINFOW(FaxPortHandle: Windows.Win32.Foundation.HANDLE, RoutingInfo: POINTER(Windows.Win32.Devices.Fax.FAX_GLOBAL_ROUTING_INFOW_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXSETJOBA(FaxHandle: Windows.Win32.Foundation.HANDLE, JobId: UInt32, Command: UInt32, JobEntry: POINTER(Windows.Win32.Devices.Fax.FAX_JOB_ENTRYA_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXSETJOBW(FaxHandle: Windows.Win32.Foundation.HANDLE, JobId: UInt32, Command: UInt32, JobEntry: POINTER(Windows.Win32.Devices.Fax.FAX_JOB_ENTRYW_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXSETLOGGINGCATEGORIESA(FaxHandle: Windows.Win32.Foundation.HANDLE, Categories: POINTER(Windows.Win32.Devices.Fax.FAX_LOG_CATEGORYA_head), NumberCategories: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXSETLOGGINGCATEGORIESW(FaxHandle: Windows.Win32.Foundation.HANDLE, Categories: POINTER(Windows.Win32.Devices.Fax.FAX_LOG_CATEGORYW_head), NumberCategories: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXSETPORTA(FaxPortHandle: Windows.Win32.Foundation.HANDLE, PortInfo: POINTER(Windows.Win32.Devices.Fax.FAX_PORT_INFOA_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXSETPORTW(FaxPortHandle: Windows.Win32.Foundation.HANDLE, PortInfo: POINTER(Windows.Win32.Devices.Fax.FAX_PORT_INFOW_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXSETROUTINGINFOA(FaxPortHandle: Windows.Win32.Foundation.HANDLE, RoutingGuid: Windows.Win32.Foundation.PSTR, RoutingInfoBuffer: c_char_p_no, RoutingInfoBufferSize: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXSETROUTINGINFOW(FaxPortHandle: Windows.Win32.Foundation.HANDLE, RoutingGuid: Windows.Win32.Foundation.PWSTR, RoutingInfoBuffer: c_char_p_no, RoutingInfoBufferSize: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXSTARTPRINTJOBA(PrinterName: Windows.Win32.Foundation.PSTR, PrintInfo: POINTER(Windows.Win32.Devices.Fax.FAX_PRINT_INFOA_head), FaxJobId: POINTER(UInt32), FaxContextInfo: POINTER(Windows.Win32.Devices.Fax.FAX_CONTEXT_INFOA_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXSTARTPRINTJOBW(PrinterName: Windows.Win32.Foundation.PWSTR, PrintInfo: POINTER(Windows.Win32.Devices.Fax.FAX_PRINT_INFOW_head), FaxJobId: POINTER(UInt32), FaxContextInfo: POINTER(Windows.Win32.Devices.Fax.FAX_CONTEXT_INFOW_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXUNREGISTERSERVICEPROVIDERW(DeviceProvider: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAX_EXT_CONFIG_CHANGE(param0: UInt32, param1: Windows.Win32.Foundation.PWSTR, param2: c_char_p_no, param3: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFAX_EXT_FREE_BUFFER(param0: c_void_p) -> Void: ...
@winfunctype_pointer
def PFAX_EXT_GET_DATA(param0: UInt32, param1: Windows.Win32.Devices.Fax.FAX_ENUM_DEVICE_ID_SOURCE, param2: Windows.Win32.Foundation.PWSTR, param3: POINTER(c_char_p_no), param4: POINTER(UInt32)) -> UInt32: ...
@winfunctype_pointer
def PFAX_EXT_INITIALIZE_CONFIG(param0: Windows.Win32.Devices.Fax.PFAX_EXT_GET_DATA, param1: Windows.Win32.Devices.Fax.PFAX_EXT_SET_DATA, param2: Windows.Win32.Devices.Fax.PFAX_EXT_REGISTER_FOR_EVENTS, param3: Windows.Win32.Devices.Fax.PFAX_EXT_UNREGISTER_FOR_EVENTS, param4: Windows.Win32.Devices.Fax.PFAX_EXT_FREE_BUFFER) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFAX_EXT_REGISTER_FOR_EVENTS(param0: Windows.Win32.Foundation.HINSTANCE, param1: UInt32, param2: Windows.Win32.Devices.Fax.FAX_ENUM_DEVICE_ID_SOURCE, param3: Windows.Win32.Foundation.PWSTR, param4: Windows.Win32.Devices.Fax.PFAX_EXT_CONFIG_CHANGE) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype_pointer
def PFAX_EXT_SET_DATA(param0: Windows.Win32.Foundation.HINSTANCE, param1: UInt32, param2: Windows.Win32.Devices.Fax.FAX_ENUM_DEVICE_ID_SOURCE, param3: Windows.Win32.Foundation.PWSTR, param4: c_char_p_no, param5: UInt32) -> UInt32: ...
@winfunctype_pointer
def PFAX_EXT_UNREGISTER_FOR_EVENTS(param0: Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype_pointer
def PFAX_LINECALLBACK(FaxHandle: Windows.Win32.Foundation.HANDLE, hDevice: UInt32, dwMessage: UInt32, dwInstance: UIntPtr, dwParam1: UIntPtr, dwParam2: UIntPtr, dwParam3: UIntPtr) -> Void: ...
@winfunctype_pointer
def PFAX_RECIPIENT_CALLBACKA(FaxHandle: Windows.Win32.Foundation.HANDLE, RecipientNumber: UInt32, Context: c_void_p, JobParams: POINTER(Windows.Win32.Devices.Fax.FAX_JOB_PARAMA_head), CoverpageInfo: POINTER(Windows.Win32.Devices.Fax.FAX_COVERPAGE_INFOA_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAX_RECIPIENT_CALLBACKW(FaxHandle: Windows.Win32.Foundation.HANDLE, RecipientNumber: UInt32, Context: c_void_p, JobParams: POINTER(Windows.Win32.Devices.Fax.FAX_JOB_PARAMW_head), CoverpageInfo: POINTER(Windows.Win32.Devices.Fax.FAX_COVERPAGE_INFOW_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAX_ROUTING_INSTALLATION_CALLBACKW(FaxHandle: Windows.Win32.Foundation.HANDLE, Context: c_void_p, MethodName: Windows.Win32.Foundation.PWSTR, FriendlyName: Windows.Win32.Foundation.PWSTR, FunctionName: Windows.Win32.Foundation.PWSTR, Guid: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAX_SEND_CALLBACK(FaxHandle: Windows.Win32.Foundation.HANDLE, CallHandle: UInt32, Reserved1: UInt32, Reserved2: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAX_SERVICE_CALLBACK(FaxHandle: Windows.Win32.Foundation.HANDLE, DeviceId: UInt32, Param1: UIntPtr, Param2: UIntPtr, Param3: UIntPtr) -> Windows.Win32.Foundation.BOOL: ...
class STINOTIFY(Structure):
    dwSize: UInt32
    guidNotificationCode: Guid
    abNotificationData: Byte * 64
class STISUBSCRIBE(Structure):
    dwSize: UInt32
    dwFlags: UInt32
    dwFilter: UInt32
    hWndNotify: Windows.Win32.Foundation.HWND
    hEvent: Windows.Win32.Foundation.HANDLE
    uiNotificationMessage: UInt32
class STI_DEVICE_INFORMATIONW(Structure):
    dwSize: UInt32
    DeviceType: UInt32
    szDeviceInternalName: Char * 128
    DeviceCapabilitiesA: Windows.Win32.Devices.Fax.STI_DEV_CAPS
    dwHardwareConfiguration: UInt32
    pszVendorDescription: Windows.Win32.Foundation.PWSTR
    pszDeviceDescription: Windows.Win32.Foundation.PWSTR
    pszPortName: Windows.Win32.Foundation.PWSTR
    pszPropProvider: Windows.Win32.Foundation.PWSTR
    pszLocalName: Windows.Win32.Foundation.PWSTR
STI_DEVICE_MJ_TYPE = Int32
STI_DEVICE_MJ_TYPE_StiDeviceTypeDefault: STI_DEVICE_MJ_TYPE = 0
STI_DEVICE_MJ_TYPE_StiDeviceTypeScanner: STI_DEVICE_MJ_TYPE = 1
STI_DEVICE_MJ_TYPE_StiDeviceTypeDigitalCamera: STI_DEVICE_MJ_TYPE = 2
STI_DEVICE_MJ_TYPE_StiDeviceTypeStreamingVideo: STI_DEVICE_MJ_TYPE = 3
class STI_DEVICE_STATUS(Structure):
    dwSize: UInt32
    StatusMask: UInt32
    dwOnlineState: UInt32
    dwHardwareStatusCode: UInt32
    dwEventHandlingState: UInt32
    dwPollingInterval: UInt32
class STI_DEV_CAPS(Structure):
    dwGeneric: UInt32
class STI_DIAG(Structure):
    dwSize: UInt32
    dwBasicDiagCode: UInt32
    dwVendorDiagCode: UInt32
    dwStatusMask: UInt32
    sErrorInfo: Windows.Win32.Devices.Fax._ERROR_INFOW
class STI_USD_CAPS(Structure):
    dwVersion: UInt32
    dwGenericCaps: UInt32
class STI_WIA_DEVICE_INFORMATIONW(Structure):
    dwSize: UInt32
    DeviceType: UInt32
    szDeviceInternalName: Char * 128
    DeviceCapabilitiesA: Windows.Win32.Devices.Fax.STI_DEV_CAPS
    dwHardwareConfiguration: UInt32
    pszVendorDescription: Windows.Win32.Foundation.PWSTR
    pszDeviceDescription: Windows.Win32.Foundation.PWSTR
    pszPortName: Windows.Win32.Foundation.PWSTR
    pszPropProvider: Windows.Win32.Foundation.PWSTR
    pszLocalName: Windows.Win32.Foundation.PWSTR
    pszUiDll: Windows.Win32.Foundation.PWSTR
    pszServer: Windows.Win32.Foundation.PWSTR
SendToMode = Int32
SEND_TO_FAX_RECIPIENT_ATTACHMENT: SendToMode = 0
class _ERROR_INFOW(Structure):
    dwSize: UInt32
    dwGenericError: UInt32
    dwVendorError: UInt32
    szExtendedErrorText: Char * 255
make_head(_module, 'DEVPKEY_WIA_DeviceType')
make_head(_module, 'DEVPKEY_WIA_USDClassId')
make_head(_module, 'FAX_CONFIGURATIONA')
make_head(_module, 'FAX_CONFIGURATIONW')
make_head(_module, 'FAX_CONTEXT_INFOA')
make_head(_module, 'FAX_CONTEXT_INFOW')
make_head(_module, 'FAX_COVERPAGE_INFOA')
make_head(_module, 'FAX_COVERPAGE_INFOW')
make_head(_module, 'FAX_DEVICE_STATUSA')
make_head(_module, 'FAX_DEVICE_STATUSW')
make_head(_module, 'FAX_DEV_STATUS')
make_head(_module, 'FAX_EVENTA')
make_head(_module, 'FAX_EVENTW')
make_head(_module, 'FAX_GLOBAL_ROUTING_INFOA')
make_head(_module, 'FAX_GLOBAL_ROUTING_INFOW')
make_head(_module, 'FAX_JOB_ENTRYA')
make_head(_module, 'FAX_JOB_ENTRYW')
make_head(_module, 'FAX_JOB_PARAMA')
make_head(_module, 'FAX_JOB_PARAMW')
make_head(_module, 'FAX_LOG_CATEGORYA')
make_head(_module, 'FAX_LOG_CATEGORYW')
make_head(_module, 'FAX_PORT_INFOA')
make_head(_module, 'FAX_PORT_INFOW')
make_head(_module, 'FAX_PRINT_INFOA')
make_head(_module, 'FAX_PRINT_INFOW')
make_head(_module, 'FAX_RECEIVE')
make_head(_module, 'FAX_ROUTE')
make_head(_module, 'FAX_ROUTE_CALLBACKROUTINES')
make_head(_module, 'FAX_ROUTING_METHODA')
make_head(_module, 'FAX_ROUTING_METHODW')
make_head(_module, 'FAX_SEND')
make_head(_module, 'FAX_TIME')
make_head(_module, 'IFaxAccount')
make_head(_module, 'IFaxAccountFolders')
make_head(_module, 'IFaxAccountIncomingArchive')
make_head(_module, 'IFaxAccountIncomingQueue')
make_head(_module, 'IFaxAccountNotify')
make_head(_module, 'IFaxAccountOutgoingArchive')
make_head(_module, 'IFaxAccountOutgoingQueue')
make_head(_module, 'IFaxAccountSet')
make_head(_module, 'IFaxAccounts')
make_head(_module, 'IFaxActivity')
make_head(_module, 'IFaxActivityLogging')
make_head(_module, 'IFaxConfiguration')
make_head(_module, 'IFaxDevice')
make_head(_module, 'IFaxDeviceIds')
make_head(_module, 'IFaxDeviceProvider')
make_head(_module, 'IFaxDeviceProviders')
make_head(_module, 'IFaxDevices')
make_head(_module, 'IFaxDocument')
make_head(_module, 'IFaxDocument2')
make_head(_module, 'IFaxEventLogging')
make_head(_module, 'IFaxFolders')
make_head(_module, 'IFaxInboundRouting')
make_head(_module, 'IFaxInboundRoutingExtension')
make_head(_module, 'IFaxInboundRoutingExtensions')
make_head(_module, 'IFaxInboundRoutingMethod')
make_head(_module, 'IFaxInboundRoutingMethods')
make_head(_module, 'IFaxIncomingArchive')
make_head(_module, 'IFaxIncomingJob')
make_head(_module, 'IFaxIncomingJobs')
make_head(_module, 'IFaxIncomingMessage')
make_head(_module, 'IFaxIncomingMessage2')
make_head(_module, 'IFaxIncomingMessageIterator')
make_head(_module, 'IFaxIncomingQueue')
make_head(_module, 'IFaxJobStatus')
make_head(_module, 'IFaxLoggingOptions')
make_head(_module, 'IFaxOutboundRouting')
make_head(_module, 'IFaxOutboundRoutingGroup')
make_head(_module, 'IFaxOutboundRoutingGroups')
make_head(_module, 'IFaxOutboundRoutingRule')
make_head(_module, 'IFaxOutboundRoutingRules')
make_head(_module, 'IFaxOutgoingArchive')
make_head(_module, 'IFaxOutgoingJob')
make_head(_module, 'IFaxOutgoingJob2')
make_head(_module, 'IFaxOutgoingJobs')
make_head(_module, 'IFaxOutgoingMessage')
make_head(_module, 'IFaxOutgoingMessage2')
make_head(_module, 'IFaxOutgoingMessageIterator')
make_head(_module, 'IFaxOutgoingQueue')
make_head(_module, 'IFaxReceiptOptions')
make_head(_module, 'IFaxRecipient')
make_head(_module, 'IFaxRecipients')
make_head(_module, 'IFaxSecurity')
make_head(_module, 'IFaxSecurity2')
make_head(_module, 'IFaxSender')
make_head(_module, 'IFaxServer')
make_head(_module, 'IFaxServer2')
make_head(_module, 'IFaxServerNotify')
make_head(_module, 'IFaxServerNotify2')
make_head(_module, 'IStiDevice')
make_head(_module, 'IStiDeviceControl')
make_head(_module, 'IStiUSD')
make_head(_module, 'IStillImageW')
make_head(_module, 'PFAXABORT')
make_head(_module, 'PFAXACCESSCHECK')
make_head(_module, 'PFAXCLOSE')
make_head(_module, 'PFAXCOMPLETEJOBPARAMSA')
make_head(_module, 'PFAXCOMPLETEJOBPARAMSW')
make_head(_module, 'PFAXCONNECTFAXSERVERA')
make_head(_module, 'PFAXCONNECTFAXSERVERW')
make_head(_module, 'PFAXDEVABORTOPERATION')
make_head(_module, 'PFAXDEVCONFIGURE')
make_head(_module, 'PFAXDEVENDJOB')
make_head(_module, 'PFAXDEVINITIALIZE')
make_head(_module, 'PFAXDEVRECEIVE')
make_head(_module, 'PFAXDEVREPORTSTATUS')
make_head(_module, 'PFAXDEVSEND')
make_head(_module, 'PFAXDEVSHUTDOWN')
make_head(_module, 'PFAXDEVSTARTJOB')
make_head(_module, 'PFAXDEVVIRTUALDEVICECREATION')
make_head(_module, 'PFAXENABLEROUTINGMETHODA')
make_head(_module, 'PFAXENABLEROUTINGMETHODW')
make_head(_module, 'PFAXENUMGLOBALROUTINGINFOA')
make_head(_module, 'PFAXENUMGLOBALROUTINGINFOW')
make_head(_module, 'PFAXENUMJOBSA')
make_head(_module, 'PFAXENUMJOBSW')
make_head(_module, 'PFAXENUMPORTSA')
make_head(_module, 'PFAXENUMPORTSW')
make_head(_module, 'PFAXENUMROUTINGMETHODSA')
make_head(_module, 'PFAXENUMROUTINGMETHODSW')
make_head(_module, 'PFAXFREEBUFFER')
make_head(_module, 'PFAXGETCONFIGURATIONA')
make_head(_module, 'PFAXGETCONFIGURATIONW')
make_head(_module, 'PFAXGETDEVICESTATUSA')
make_head(_module, 'PFAXGETDEVICESTATUSW')
make_head(_module, 'PFAXGETJOBA')
make_head(_module, 'PFAXGETJOBW')
make_head(_module, 'PFAXGETLOGGINGCATEGORIESA')
make_head(_module, 'PFAXGETLOGGINGCATEGORIESW')
make_head(_module, 'PFAXGETPAGEDATA')
make_head(_module, 'PFAXGETPORTA')
make_head(_module, 'PFAXGETPORTW')
make_head(_module, 'PFAXGETROUTINGINFOA')
make_head(_module, 'PFAXGETROUTINGINFOW')
make_head(_module, 'PFAXINITIALIZEEVENTQUEUE')
make_head(_module, 'PFAXOPENPORT')
make_head(_module, 'PFAXPRINTCOVERPAGEA')
make_head(_module, 'PFAXPRINTCOVERPAGEW')
make_head(_module, 'PFAXREGISTERROUTINGEXTENSIONW')
make_head(_module, 'PFAXREGISTERSERVICEPROVIDERW')
make_head(_module, 'PFAXROUTEADDFILE')
make_head(_module, 'PFAXROUTEDELETEFILE')
make_head(_module, 'PFAXROUTEDEVICECHANGENOTIFICATION')
make_head(_module, 'PFAXROUTEDEVICEENABLE')
make_head(_module, 'PFAXROUTEENUMFILE')
make_head(_module, 'PFAXROUTEENUMFILES')
make_head(_module, 'PFAXROUTEGETFILE')
make_head(_module, 'PFAXROUTEGETROUTINGINFO')
make_head(_module, 'PFAXROUTEINITIALIZE')
make_head(_module, 'PFAXROUTEMETHOD')
make_head(_module, 'PFAXROUTEMODIFYROUTINGDATA')
make_head(_module, 'PFAXROUTESETROUTINGINFO')
make_head(_module, 'PFAXSENDDOCUMENTA')
make_head(_module, 'PFAXSENDDOCUMENTFORBROADCASTA')
make_head(_module, 'PFAXSENDDOCUMENTFORBROADCASTW')
make_head(_module, 'PFAXSENDDOCUMENTW')
make_head(_module, 'PFAXSETCONFIGURATIONA')
make_head(_module, 'PFAXSETCONFIGURATIONW')
make_head(_module, 'PFAXSETGLOBALROUTINGINFOA')
make_head(_module, 'PFAXSETGLOBALROUTINGINFOW')
make_head(_module, 'PFAXSETJOBA')
make_head(_module, 'PFAXSETJOBW')
make_head(_module, 'PFAXSETLOGGINGCATEGORIESA')
make_head(_module, 'PFAXSETLOGGINGCATEGORIESW')
make_head(_module, 'PFAXSETPORTA')
make_head(_module, 'PFAXSETPORTW')
make_head(_module, 'PFAXSETROUTINGINFOA')
make_head(_module, 'PFAXSETROUTINGINFOW')
make_head(_module, 'PFAXSTARTPRINTJOBA')
make_head(_module, 'PFAXSTARTPRINTJOBW')
make_head(_module, 'PFAXUNREGISTERSERVICEPROVIDERW')
make_head(_module, 'PFAX_EXT_CONFIG_CHANGE')
make_head(_module, 'PFAX_EXT_FREE_BUFFER')
make_head(_module, 'PFAX_EXT_GET_DATA')
make_head(_module, 'PFAX_EXT_INITIALIZE_CONFIG')
make_head(_module, 'PFAX_EXT_REGISTER_FOR_EVENTS')
make_head(_module, 'PFAX_EXT_SET_DATA')
make_head(_module, 'PFAX_EXT_UNREGISTER_FOR_EVENTS')
make_head(_module, 'PFAX_LINECALLBACK')
make_head(_module, 'PFAX_RECIPIENT_CALLBACKA')
make_head(_module, 'PFAX_RECIPIENT_CALLBACKW')
make_head(_module, 'PFAX_ROUTING_INSTALLATION_CALLBACKW')
make_head(_module, 'PFAX_SEND_CALLBACK')
make_head(_module, 'PFAX_SERVICE_CALLBACK')
make_head(_module, 'STINOTIFY')
make_head(_module, 'STISUBSCRIBE')
make_head(_module, 'STI_DEVICE_INFORMATIONW')
make_head(_module, 'STI_DEVICE_STATUS')
make_head(_module, 'STI_DEV_CAPS')
make_head(_module, 'STI_DIAG')
make_head(_module, 'STI_USD_CAPS')
make_head(_module, 'STI_WIA_DEVICE_INFORMATIONW')
make_head(_module, '_ERROR_INFOW')
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
    "STI_GENCAP_COMMON_MASK",
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
_arch_optional = [
]
