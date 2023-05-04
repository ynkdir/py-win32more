from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Devices.Fax
import Windows.Win32.Devices.Properties
import Windows.Win32.Foundation
import Windows.Win32.Graphics.Gdi
import Windows.Win32.System.Com
import Windows.Win32.System.IO
import Windows.Win32.System.Registry
import Windows.Win32.System.Variant
import Windows.Win32.UI.Controls
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
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
FAXSRV_DEVICE_NODETYPE_GUID: Guid = Guid('{3115a19a-6251-46ac-9425-14782858b8c9}')
FAXSRV_DEVICE_PROVIDER_NODETYPE_GUID: Guid = Guid('{bd38e2ac-b926-4161-8640-0f6956ee2ba3}')
FAXSRV_ROUTING_METHOD_NODETYPE_GUID: Guid = Guid('{220d2cb0-85a9-4a43-b6e8-9d66b44f1af5}')
CF_MSFAXSRV_DEVICE_ID: String = 'FAXSRV_DeviceID'
CF_MSFAXSRV_FSP_GUID: String = 'FAXSRV_FSPGuid'
CF_MSFAXSRV_SERVER_NAME: String = 'FAXSRV_ServerName'
CF_MSFAXSRV_ROUTEEXT_NAME: String = 'FAXSRV_RoutingExtName'
CF_MSFAXSRV_ROUTING_METHOD_GUID: String = 'FAXSRV_RoutingMethodGuid'
STI_UNICODE: UInt32 = 1
CLSID_Sti: Guid = Guid('{b323f8e0-2e68-11d0-90ea-00aa0060f86c}')
GUID_DeviceArrivedLaunch: Guid = Guid('{740d9ee6-70f1-11d1-ad10-00a02438ad48}')
GUID_ScanImage: Guid = Guid('{a6c5a715-8c6e-11d2-977a-0000f87a926f}')
GUID_ScanPrintImage: Guid = Guid('{b441f425-8c6e-11d2-977a-0000f87a926f}')
GUID_ScanFaxImage: Guid = Guid('{c00eb793-8c6e-11d2-977a-0000f87a926f}')
GUID_STIUserDefined1: Guid = Guid('{c00eb795-8c6e-11d2-977a-0000f87a926f}')
GUID_STIUserDefined2: Guid = Guid('{c77ae9c5-8c6e-11d2-977a-0000f87a926f}')
GUID_STIUserDefined3: Guid = Guid('{c77ae9c6-8c6e-11d2-977a-0000f87a926f}')
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
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{6bdd1fc6-810f-11d0-bec7-08002be2092f}'), pid=2)
def DEVPKEY_WIA_USDClassId():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{6bdd1fc6-810f-11d0-bec7-08002be2092f}'), pid=3)
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
def FaxGetPageData(FaxHandle: Windows.Win32.Foundation.HANDLE, JobId: UInt32, Buffer: POINTER(POINTER(Byte)), BufferSize: POINTER(UInt32), ImageWidth: POINTER(UInt32), ImageHeight: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
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
def FaxGetRoutingInfoA(FaxPortHandle: Windows.Win32.Foundation.HANDLE, RoutingGuid: Windows.Win32.Foundation.PSTR, RoutingInfoBuffer: POINTER(POINTER(Byte)), RoutingInfoBufferSize: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxGetRoutingInfoW(FaxPortHandle: Windows.Win32.Foundation.HANDLE, RoutingGuid: Windows.Win32.Foundation.PWSTR, RoutingInfoBuffer: POINTER(POINTER(Byte)), RoutingInfoBufferSize: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxSetRoutingInfoA(FaxPortHandle: Windows.Win32.Foundation.HANDLE, RoutingGuid: Windows.Win32.Foundation.PSTR, RoutingInfoBuffer: POINTER(Byte), RoutingInfoBufferSize: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxSetRoutingInfoW(FaxPortHandle: Windows.Win32.Foundation.HANDLE, RoutingGuid: Windows.Win32.Foundation.PWSTR, RoutingInfoBuffer: POINTER(Byte), RoutingInfoBufferSize: UInt32) -> Windows.Win32.Foundation.BOOL: ...
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
def StiCreateInstanceW(hinst: Windows.Win32.Foundation.HMODULE, dwVer: UInt32, ppSti: POINTER(Windows.Win32.Devices.Fax.IStillImageW_head), punkOuter: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
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
class FAX_CONFIGURATIONA(EasyCastStructure):
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
class FAX_CONFIGURATIONW(EasyCastStructure):
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
class FAX_CONTEXT_INFOA(EasyCastStructure):
    SizeOfStruct: UInt32
    hDC: Windows.Win32.Graphics.Gdi.HDC
    ServerName: Windows.Win32.Foundation.CHAR * 16
class FAX_CONTEXT_INFOW(EasyCastStructure):
    SizeOfStruct: UInt32
    hDC: Windows.Win32.Graphics.Gdi.HDC
    ServerName: Char * 16
class FAX_COVERPAGE_INFOA(EasyCastStructure):
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
class FAX_COVERPAGE_INFOW(EasyCastStructure):
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
class FAX_DEVICE_STATUSA(EasyCastStructure):
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
class FAX_DEVICE_STATUSW(EasyCastStructure):
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
class FAX_DEV_STATUS(EasyCastStructure):
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
class FAX_EVENTA(EasyCastStructure):
    SizeOfStruct: UInt32
    TimeStamp: Windows.Win32.Foundation.FILETIME
    DeviceId: UInt32
    EventId: UInt32
    JobId: UInt32
class FAX_EVENTW(EasyCastStructure):
    SizeOfStruct: UInt32
    TimeStamp: Windows.Win32.Foundation.FILETIME
    DeviceId: UInt32
    EventId: UInt32
    JobId: UInt32
class FAX_GLOBAL_ROUTING_INFOA(EasyCastStructure):
    SizeOfStruct: UInt32
    Priority: UInt32
    Guid: Windows.Win32.Foundation.PSTR
    FriendlyName: Windows.Win32.Foundation.PSTR
    FunctionName: Windows.Win32.Foundation.PSTR
    ExtensionImageName: Windows.Win32.Foundation.PSTR
    ExtensionFriendlyName: Windows.Win32.Foundation.PSTR
class FAX_GLOBAL_ROUTING_INFOW(EasyCastStructure):
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
class FAX_JOB_ENTRYA(EasyCastStructure):
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
class FAX_JOB_ENTRYW(EasyCastStructure):
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
class FAX_JOB_PARAMA(EasyCastStructure):
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
class FAX_JOB_PARAMW(EasyCastStructure):
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
class FAX_LOG_CATEGORYA(EasyCastStructure):
    Name: Windows.Win32.Foundation.PSTR
    Category: UInt32
    Level: UInt32
class FAX_LOG_CATEGORYW(EasyCastStructure):
    Name: Windows.Win32.Foundation.PWSTR
    Category: UInt32
    Level: UInt32
FAX_LOG_LEVEL_ENUM = Int32
FAX_LOG_LEVEL_ENUM_fllNONE: FAX_LOG_LEVEL_ENUM = 0
FAX_LOG_LEVEL_ENUM_fllMIN: FAX_LOG_LEVEL_ENUM = 1
FAX_LOG_LEVEL_ENUM_fllMED: FAX_LOG_LEVEL_ENUM = 2
FAX_LOG_LEVEL_ENUM_fllMAX: FAX_LOG_LEVEL_ENUM = 3
class FAX_PORT_INFOA(EasyCastStructure):
    SizeOfStruct: UInt32
    DeviceId: UInt32
    State: UInt32
    Flags: UInt32
    Rings: UInt32
    Priority: UInt32
    DeviceName: Windows.Win32.Foundation.PSTR
    Tsid: Windows.Win32.Foundation.PSTR
    Csid: Windows.Win32.Foundation.PSTR
class FAX_PORT_INFOW(EasyCastStructure):
    SizeOfStruct: UInt32
    DeviceId: UInt32
    State: UInt32
    Flags: UInt32
    Rings: UInt32
    Priority: UInt32
    DeviceName: Windows.Win32.Foundation.PWSTR
    Tsid: Windows.Win32.Foundation.PWSTR
    Csid: Windows.Win32.Foundation.PWSTR
class FAX_PRINT_INFOA(EasyCastStructure):
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
class FAX_PRINT_INFOW(EasyCastStructure):
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
class FAX_RECEIVE(EasyCastStructure):
    SizeOfStruct: UInt32
    FileName: Windows.Win32.Foundation.PWSTR
    ReceiverName: Windows.Win32.Foundation.PWSTR
    ReceiverNumber: Windows.Win32.Foundation.PWSTR
    Reserved: UInt32 * 4
class FAX_ROUTE(EasyCastStructure):
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
    RoutingInfoData: POINTER(Byte)
    RoutingInfoDataSize: UInt32
class FAX_ROUTE_CALLBACKROUTINES(EasyCastStructure):
    SizeOfStruct: UInt32
    FaxRouteAddFile: Windows.Win32.Devices.Fax.PFAXROUTEADDFILE
    FaxRouteDeleteFile: Windows.Win32.Devices.Fax.PFAXROUTEDELETEFILE
    FaxRouteGetFile: Windows.Win32.Devices.Fax.PFAXROUTEGETFILE
    FaxRouteEnumFiles: Windows.Win32.Devices.Fax.PFAXROUTEENUMFILES
    FaxRouteModifyRoutingData: Windows.Win32.Devices.Fax.PFAXROUTEMODIFYROUTINGDATA
class FAX_ROUTING_METHODA(EasyCastStructure):
    SizeOfStruct: UInt32
    DeviceId: UInt32
    Enabled: Windows.Win32.Foundation.BOOL
    DeviceName: Windows.Win32.Foundation.PSTR
    Guid: Windows.Win32.Foundation.PSTR
    FriendlyName: Windows.Win32.Foundation.PSTR
    FunctionName: Windows.Win32.Foundation.PSTR
    ExtensionImageName: Windows.Win32.Foundation.PSTR
    ExtensionFriendlyName: Windows.Win32.Foundation.PSTR
class FAX_ROUTING_METHODW(EasyCastStructure):
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
class FAX_SEND(EasyCastStructure):
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
class FAX_TIME(EasyCastStructure):
    Hour: UInt16
    Minute: UInt16
FaxAccount = Guid('{a7e0647f-4524-4464-a56d-b9fe666f715e}')
FaxAccountFolders = Guid('{85398f49-c034-4a3f-821c-db7d685e8129}')
FaxAccountIncomingArchive = Guid('{14b33db5-4c40-4ecf-9ef8-a360cbe809ed}')
FaxAccountIncomingQueue = Guid('{9bcf6094-b4da-45f4-b8d6-ddeb2186652c}')
FaxAccountOutgoingArchive = Guid('{851e7af5-433a-4739-a2df-ad245c2cb98e}')
FaxAccountOutgoingQueue = Guid('{feeceefb-c149-48ba-bab8-b791e101f62f}')
FaxAccountSet = Guid('{fbc23c4b-79e0-4291-bc56-c12e253bbf3a}')
FaxAccounts = Guid('{da1f94aa-ee2c-47c0-8f4f-2a217075b76e}')
FaxActivity = Guid('{cfef5d0e-e84d-462e-aabb-87d31eb04fef}')
FaxActivityLogging = Guid('{f0a0294e-3bbd-48b8-8f13-8c591a55bdbc}')
FaxConfiguration = Guid('{5857326f-e7b3-41a7-9c19-a91b463e2d56}')
FaxDevice = Guid('{59e3a5b2-d676-484b-a6de-720bfa89b5af}')
FaxDeviceIds = Guid('{cdc539ea-7277-460e-8de0-48a0a5760d1f}')
FaxDeviceProvider = Guid('{17cf1aa3-f5eb-484a-9c9a-4440a5baabfc}')
FaxDeviceProviders = Guid('{eb8fe768-875a-4f5f-82c5-03f23aac1bd7}')
FaxDevices = Guid('{5589e28e-23cb-4919-8808-e6101846e80d}')
FaxDocument = Guid('{0f3f9f91-c838-415e-a4f3-3e828ca445e0}')
FaxEventLogging = Guid('{a6850930-a0f6-4a6f-95b7-db2ebf3d02e3}')
FaxFolders = Guid('{c35211d7-5776-48cb-af44-c31be3b2cfe5}')
FaxInboundRouting = Guid('{e80248ed-ad65-4218-8108-991924d4e7ed}')
FaxInboundRoutingExtension = Guid('{1d7dfb51-7207-4436-a0d9-24e32ee56988}')
FaxInboundRoutingExtensions = Guid('{189a48ed-623c-4c0d-80f2-d66c7b9efec2}')
FaxInboundRoutingMethod = Guid('{4b9fd75c-0194-4b72-9ce5-02a8205ac7d4}')
FaxInboundRoutingMethods = Guid('{25fcb76a-b750-4b82-9266-fbbbae8922ba}')
FaxIncomingArchive = Guid('{8426c56a-35a1-4c6f-af93-fc952422e2c2}')
FaxIncomingJob = Guid('{c47311ec-ae32-41b8-ae4b-3eae0629d0c9}')
FaxIncomingJobs = Guid('{a1bb8a43-8866-4fb7-a15d-6266c875a5cc}')
FaxIncomingMessage = Guid('{1932fcf7-9d43-4d5a-89ff-03861b321736}')
FaxIncomingMessageIterator = Guid('{6088e1d8-3fc8-45c2-87b1-909a29607ea9}')
FaxIncomingQueue = Guid('{69131717-f3f1-40e3-809d-a6cbf7bd85e5}')
FaxJobStatus = Guid('{7bf222f4-be8d-442f-841d-6132742423bb}')
FaxLoggingOptions = Guid('{1bf9eea6-ece0-4785-a18b-de56e9eef96a}')
FaxOutboundRouting = Guid('{c81b385e-b869-4afd-86c0-616498ed9be2}')
FaxOutboundRoutingGroup = Guid('{0213f3e0-6791-4d77-a271-04d2357c50d6}')
FaxOutboundRoutingGroups = Guid('{ccbea1a5-e2b4-4b57-9421-b04b6289464b}')
FaxOutboundRoutingRule = Guid('{6549eebf-08d1-475a-828b-3bf105952fa0}')
FaxOutboundRoutingRules = Guid('{d385beca-e624-4473-bfaa-9f4000831f54}')
FaxOutgoingArchive = Guid('{43c28403-e04f-474d-990c-b94669148f59}')
FaxOutgoingJob = Guid('{71bb429c-0ef9-4915-bec5-a5d897a3e924}')
FaxOutgoingJobs = Guid('{92bf2a6c-37be-43fa-a37d-cb0e5f753b35}')
FaxOutgoingMessage = Guid('{91b4a378-4ad8-4aef-a4dc-97d96e939a3a}')
FaxOutgoingMessageIterator = Guid('{8a3224d0-d30b-49de-9813-cb385790fbbb}')
FaxOutgoingQueue = Guid('{7421169e-8c43-4b0d-bb16-645c8fa40357}')
FaxReceiptOptions = Guid('{6982487b-227b-4c96-a61c-248348b05ab6}')
FaxRecipient = Guid('{60bf3301-7df8-4bd8-9148-7b5801f9efdf}')
FaxRecipients = Guid('{ea9bdf53-10a9-4d4f-a067-63c8f84f01b0}')
FaxSecurity = Guid('{10c4ddde-abf0-43df-964f-7f3ac21a4c7b}')
FaxSecurity2 = Guid('{735c1248-ec89-4c30-a127-656e92e3c4ea}')
FaxSender = Guid('{265d84d0-1850-4360-b7c8-758bbb5f0b96}')
FaxServer = Guid('{cda8acb0-8cf5-4f6c-9ba2-5931d40c8cae}')
class IFaxAccount(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{68535b33-5dc4-4086-be26-b76f9b711006}')
    @commethod(7)
    def get_AccountName(self, pbstrAccountName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Folders(self, ppFolders: POINTER(Windows.Win32.Devices.Fax.IFaxAccountFolders_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ListenToAccountEvents(self, EventTypes: Windows.Win32.Devices.Fax.FAX_ACCOUNT_EVENTS_TYPE_ENUM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_RegisteredEvents(self, pRegisteredEvents: POINTER(Windows.Win32.Devices.Fax.FAX_ACCOUNT_EVENTS_TYPE_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxAccountFolders(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{6463f89d-23d8-46a9-8f86-c47b77ca7926}')
    @commethod(7)
    def get_OutgoingQueue(self, pFaxOutgoingQueue: POINTER(Windows.Win32.Devices.Fax.IFaxAccountOutgoingQueue_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_IncomingQueue(self, pFaxIncomingQueue: POINTER(Windows.Win32.Devices.Fax.IFaxAccountIncomingQueue_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_IncomingArchive(self, pFaxIncomingArchive: POINTER(Windows.Win32.Devices.Fax.IFaxAccountIncomingArchive_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_OutgoingArchive(self, pFaxOutgoingArchive: POINTER(Windows.Win32.Devices.Fax.IFaxAccountOutgoingArchive_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxAccountIncomingArchive(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{a8a5b6ef-e0d6-4aee-955c-91625bec9db4}')
    @commethod(7)
    def get_SizeLow(self, plSizeLow: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_SizeHigh(self, plSizeHigh: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Refresh(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetMessages(self, lPrefetchSize: Int32, pFaxIncomingMessageIterator: POINTER(Windows.Win32.Devices.Fax.IFaxIncomingMessageIterator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetMessage(self, bstrMessageId: Windows.Win32.Foundation.BSTR, pFaxIncomingMessage: POINTER(Windows.Win32.Devices.Fax.IFaxIncomingMessage_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxAccountIncomingQueue(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{dd142d92-0186-4a95-a090-cbc3eadba6b4}')
    @commethod(7)
    def GetJobs(self, pFaxIncomingJobs: POINTER(Windows.Win32.Devices.Fax.IFaxIncomingJobs_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetJob(self, bstrJobId: Windows.Win32.Foundation.BSTR, pFaxIncomingJob: POINTER(Windows.Win32.Devices.Fax.IFaxIncomingJob_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxAccountNotify(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{b9b3bc81-ac1b-46f3-b39d-0adc30e1b788}')
    @commethod(7)
    def OnIncomingJobAdded(self, pFaxAccount: Windows.Win32.Devices.Fax.IFaxAccount_head, bstrJobId: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnIncomingJobRemoved(self, pFaxAccount: Windows.Win32.Devices.Fax.IFaxAccount_head, bstrJobId: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OnIncomingJobChanged(self, pFaxAccount: Windows.Win32.Devices.Fax.IFaxAccount_head, bstrJobId: Windows.Win32.Foundation.BSTR, pJobStatus: Windows.Win32.Devices.Fax.IFaxJobStatus_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def OnOutgoingJobAdded(self, pFaxAccount: Windows.Win32.Devices.Fax.IFaxAccount_head, bstrJobId: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def OnOutgoingJobRemoved(self, pFaxAccount: Windows.Win32.Devices.Fax.IFaxAccount_head, bstrJobId: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def OnOutgoingJobChanged(self, pFaxAccount: Windows.Win32.Devices.Fax.IFaxAccount_head, bstrJobId: Windows.Win32.Foundation.BSTR, pJobStatus: Windows.Win32.Devices.Fax.IFaxJobStatus_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def OnIncomingMessageAdded(self, pFaxAccount: Windows.Win32.Devices.Fax.IFaxAccount_head, bstrMessageId: Windows.Win32.Foundation.BSTR, fAddedToReceiveFolder: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def OnIncomingMessageRemoved(self, pFaxAccount: Windows.Win32.Devices.Fax.IFaxAccount_head, bstrMessageId: Windows.Win32.Foundation.BSTR, fRemovedFromReceiveFolder: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def OnOutgoingMessageAdded(self, pFaxAccount: Windows.Win32.Devices.Fax.IFaxAccount_head, bstrMessageId: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def OnOutgoingMessageRemoved(self, pFaxAccount: Windows.Win32.Devices.Fax.IFaxAccount_head, bstrMessageId: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def OnServerShutDown(self, pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxAccountOutgoingArchive(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{5463076d-ec14-491f-926e-b3ceda5e5662}')
    @commethod(7)
    def get_SizeLow(self, plSizeLow: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_SizeHigh(self, plSizeHigh: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Refresh(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetMessages(self, lPrefetchSize: Int32, pFaxOutgoingMessageIterator: POINTER(Windows.Win32.Devices.Fax.IFaxOutgoingMessageIterator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetMessage(self, bstrMessageId: Windows.Win32.Foundation.BSTR, pFaxOutgoingMessage: POINTER(Windows.Win32.Devices.Fax.IFaxOutgoingMessage_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxAccountOutgoingQueue(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{0f1424e9-f22d-4553-b7a5-0d24bd0d7e46}')
    @commethod(7)
    def GetJobs(self, pFaxOutgoingJobs: POINTER(Windows.Win32.Devices.Fax.IFaxOutgoingJobs_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetJob(self, bstrJobId: Windows.Win32.Foundation.BSTR, pFaxOutgoingJob: POINTER(Windows.Win32.Devices.Fax.IFaxOutgoingJob_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxAccountSet(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{7428fbae-841e-47b8-86f4-2288946dca1b}')
    @commethod(7)
    def GetAccounts(self, ppFaxAccounts: POINTER(Windows.Win32.Devices.Fax.IFaxAccounts_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetAccount(self, bstrAccountName: Windows.Win32.Foundation.BSTR, pFaxAccount: POINTER(Windows.Win32.Devices.Fax.IFaxAccount_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AddAccount(self, bstrAccountName: Windows.Win32.Foundation.BSTR, pFaxAccount: POINTER(Windows.Win32.Devices.Fax.IFaxAccount_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def RemoveAccount(self, bstrAccountName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxAccounts(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{93ea8162-8be7-42d1-ae7b-ec74e2d989da}')
    @commethod(7)
    def get__NewEnum(self, ppUnk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, vIndex: Windows.Win32.System.Variant.VARIANT, pFaxAccount: POINTER(Windows.Win32.Devices.Fax.IFaxAccount_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(self, plCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxActivity(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{4b106f97-3df5-40f2-bc3c-44cb8115ebdf}')
    @commethod(7)
    def get_IncomingMessages(self, plIncomingMessages: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_RoutingMessages(self, plRoutingMessages: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_OutgoingMessages(self, plOutgoingMessages: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_QueuedMessages(self, plQueuedMessages: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Refresh(self) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxActivityLogging(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{1e29078b-5a69-497b-9592-49b7e7faddb5}')
    @commethod(7)
    def get_LogIncoming(self, pbLogIncoming: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_LogIncoming(self, bLogIncoming: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_LogOutgoing(self, pbLogOutgoing: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_LogOutgoing(self, bLogOutgoing: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_DatabasePath(self, pbstrDatabasePath: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_DatabasePath(self, bstrDatabasePath: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Refresh(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def Save(self) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxConfiguration(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{10f4d0f7-0994-4543-ab6e-506949128c40}')
    @commethod(7)
    def get_UseArchive(self, pbUseArchive: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_UseArchive(self, bUseArchive: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ArchiveLocation(self, pbstrArchiveLocation: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_ArchiveLocation(self, bstrArchiveLocation: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_SizeQuotaWarning(self, pbSizeQuotaWarning: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_SizeQuotaWarning(self, bSizeQuotaWarning: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_HighQuotaWaterMark(self, plHighQuotaWaterMark: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_HighQuotaWaterMark(self, lHighQuotaWaterMark: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_LowQuotaWaterMark(self, plLowQuotaWaterMark: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_LowQuotaWaterMark(self, lLowQuotaWaterMark: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_ArchiveAgeLimit(self, plArchiveAgeLimit: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_ArchiveAgeLimit(self, lArchiveAgeLimit: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_ArchiveSizeLow(self, plSizeLow: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_ArchiveSizeHigh(self, plSizeHigh: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_OutgoingQueueBlocked(self, pbOutgoingBlocked: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_OutgoingQueueBlocked(self, bOutgoingBlocked: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_OutgoingQueuePaused(self, pbOutgoingPaused: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_OutgoingQueuePaused(self, bOutgoingPaused: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_AllowPersonalCoverPages(self, pbAllowPersonalCoverPages: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_AllowPersonalCoverPages(self, bAllowPersonalCoverPages: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_UseDeviceTSID(self, pbUseDeviceTSID: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def put_UseDeviceTSID(self, bUseDeviceTSID: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def get_Retries(self, plRetries: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def put_Retries(self, lRetries: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_RetryDelay(self, plRetryDelay: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def put_RetryDelay(self, lRetryDelay: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_DiscountRateStart(self, pdateDiscountRateStart: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def put_DiscountRateStart(self, dateDiscountRateStart: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def get_DiscountRateEnd(self, pdateDiscountRateEnd: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def put_DiscountRateEnd(self, dateDiscountRateEnd: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def get_OutgoingQueueAgeLimit(self, plOutgoingQueueAgeLimit: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def put_OutgoingQueueAgeLimit(self, lOutgoingQueueAgeLimit: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def get_Branding(self, pbBranding: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def put_Branding(self, bBranding: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def get_IncomingQueueBlocked(self, pbIncomingBlocked: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def put_IncomingQueueBlocked(self, bIncomingBlocked: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def get_AutoCreateAccountOnConnect(self, pbAutoCreateAccountOnConnect: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def put_AutoCreateAccountOnConnect(self, bAutoCreateAccountOnConnect: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def get_IncomingFaxesArePublic(self, pbIncomingFaxesArePublic: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def put_IncomingFaxesArePublic(self, bIncomingFaxesArePublic: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def Refresh(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def Save(self) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxDevice(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{49306c59-b52e-4867-9df4-ca5841c956d0}')
    @commethod(7)
    def get_Id(self, plId: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_DeviceName(self, pbstrDeviceName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ProviderUniqueName(self, pbstrProviderUniqueName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_PoweredOff(self, pbPoweredOff: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_ReceivingNow(self, pbReceivingNow: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_SendingNow(self, pbSendingNow: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_UsedRoutingMethods(self, pvUsedRoutingMethods: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_Description(self, pbstrDescription: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_Description(self, bstrDescription: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_SendEnabled(self, pbSendEnabled: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_SendEnabled(self, bSendEnabled: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_ReceiveMode(self, pReceiveMode: POINTER(Windows.Win32.Devices.Fax.FAX_DEVICE_RECEIVE_MODE_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def put_ReceiveMode(self, ReceiveMode: Windows.Win32.Devices.Fax.FAX_DEVICE_RECEIVE_MODE_ENUM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_RingsBeforeAnswer(self, plRingsBeforeAnswer: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def put_RingsBeforeAnswer(self, lRingsBeforeAnswer: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_CSID(self, pbstrCSID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_CSID(self, bstrCSID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_TSID(self, pbstrTSID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_TSID(self, bstrTSID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def Refresh(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def Save(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetExtensionProperty(self, bstrGUID: Windows.Win32.Foundation.BSTR, pvProperty: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def SetExtensionProperty(self, bstrGUID: Windows.Win32.Foundation.BSTR, vProperty: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def UseRoutingMethod(self, bstrMethodGUID: Windows.Win32.Foundation.BSTR, bUse: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_RingingNow(self, pbRingingNow: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def AnswerCall(self) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxDeviceIds(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{2f0f813f-4ce9-443e-8ca1-738cfaeee149}')
    @commethod(7)
    def get__NewEnum(self, ppUnk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, lIndex: Int32, plDeviceId: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(self, plCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Add(self, lDeviceId: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(self, lIndex: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetOrder(self, lDeviceId: Int32, lNewOrder: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxDeviceProvider(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{290eac63-83ec-449c-8417-f148df8c682a}')
    @commethod(7)
    def get_FriendlyName(self, pbstrFriendlyName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_ImageName(self, pbstrImageName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_UniqueName(self, pbstrUniqueName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_TapiProviderName(self, pbstrTapiProviderName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_MajorVersion(self, plMajorVersion: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_MinorVersion(self, plMinorVersion: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_MajorBuild(self, plMajorBuild: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_MinorBuild(self, plMinorBuild: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Debug(self, pbDebug: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_Status(self, pStatus: POINTER(Windows.Win32.Devices.Fax.FAX_PROVIDER_STATUS_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_InitErrorCode(self, plInitErrorCode: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_DeviceIds(self, pvDeviceIds: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxDeviceProviders(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{9fb76f62-4c7e-43a5-b6fd-502893f7e13e}')
    @commethod(7)
    def get__NewEnum(self, ppUnk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, vIndex: Windows.Win32.System.Variant.VARIANT, pFaxDeviceProvider: POINTER(Windows.Win32.Devices.Fax.IFaxDeviceProvider_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(self, plCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxDevices(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{9e46783e-f34f-482e-a360-0416becbbd96}')
    @commethod(7)
    def get__NewEnum(self, ppUnk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, vIndex: Windows.Win32.System.Variant.VARIANT, pFaxDevice: POINTER(Windows.Win32.Devices.Fax.IFaxDevice_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(self, plCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_ItemById(self, lId: Int32, ppFaxDevice: POINTER(Windows.Win32.Devices.Fax.IFaxDevice_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxDocument(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{b207a246-09e3-4a4e-a7dc-fea31d29458f}')
    @commethod(7)
    def get_Body(self, pbstrBody: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Body(self, bstrBody: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Sender(self, ppFaxSender: POINTER(Windows.Win32.Devices.Fax.IFaxSender_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Recipients(self, ppFaxRecipients: POINTER(Windows.Win32.Devices.Fax.IFaxRecipients_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_CoverPage(self, pbstrCoverPage: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_CoverPage(self, bstrCoverPage: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Subject(self, pbstrSubject: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_Subject(self, bstrSubject: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Note(self, pbstrNote: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_Note(self, bstrNote: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_ScheduleTime(self, pdateScheduleTime: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_ScheduleTime(self, dateScheduleTime: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_ReceiptAddress(self, pbstrReceiptAddress: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_ReceiptAddress(self, bstrReceiptAddress: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_DocumentName(self, pbstrDocumentName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_DocumentName(self, bstrDocumentName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_CallHandle(self, plCallHandle: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_CallHandle(self, lCallHandle: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_CoverPageType(self, pCoverPageType: POINTER(Windows.Win32.Devices.Fax.FAX_COVERPAGE_TYPE_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_CoverPageType(self, CoverPageType: Windows.Win32.Devices.Fax.FAX_COVERPAGE_TYPE_ENUM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_ScheduleType(self, pScheduleType: POINTER(Windows.Win32.Devices.Fax.FAX_SCHEDULE_TYPE_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def put_ScheduleType(self, ScheduleType: Windows.Win32.Devices.Fax.FAX_SCHEDULE_TYPE_ENUM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def get_ReceiptType(self, pReceiptType: POINTER(Windows.Win32.Devices.Fax.FAX_RECEIPT_TYPE_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def put_ReceiptType(self, ReceiptType: Windows.Win32.Devices.Fax.FAX_RECEIPT_TYPE_ENUM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_GroupBroadcastReceipts(self, pbUseGrouping: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def put_GroupBroadcastReceipts(self, bUseGrouping: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_Priority(self, pPriority: POINTER(Windows.Win32.Devices.Fax.FAX_PRIORITY_TYPE_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def put_Priority(self, Priority: Windows.Win32.Devices.Fax.FAX_PRIORITY_TYPE_ENUM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def get_TapiConnection(self, ppTapiConnection: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def putref_TapiConnection(self, pTapiConnection: Windows.Win32.System.Com.IDispatch_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def Submit(self, bstrFaxServerName: Windows.Win32.Foundation.BSTR, pvFaxOutgoingJobIDs: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def ConnectedSubmit(self, pFaxServer: Windows.Win32.Devices.Fax.IFaxServer_head, pvFaxOutgoingJobIDs: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def get_AttachFaxToReceipt(self, pbAttachFax: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def put_AttachFaxToReceipt(self, bAttachFax: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxDocument2(ComPtr):
    extends: Windows.Win32.Devices.Fax.IFaxDocument
    _iid_ = Guid('{e1347661-f9ef-4d6d-b4a5-c0a068b65cff}')
    @commethod(41)
    def get_SubmissionId(self, pbstrSubmissionId: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def get_Bodies(self, pvBodies: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def put_Bodies(self, vBodies: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def Submit2(self, bstrFaxServerName: Windows.Win32.Foundation.BSTR, pvFaxOutgoingJobIDs: POINTER(Windows.Win32.System.Variant.VARIANT_head), plErrorBodyFile: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def ConnectedSubmit2(self, pFaxServer: Windows.Win32.Devices.Fax.IFaxServer_head, pvFaxOutgoingJobIDs: POINTER(Windows.Win32.System.Variant.VARIANT_head), plErrorBodyFile: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxEventLogging(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{0880d965-20e8-42e4-8e17-944f192caad4}')
    @commethod(7)
    def get_InitEventsLevel(self, pInitEventLevel: POINTER(Windows.Win32.Devices.Fax.FAX_LOG_LEVEL_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_InitEventsLevel(self, InitEventLevel: Windows.Win32.Devices.Fax.FAX_LOG_LEVEL_ENUM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_InboundEventsLevel(self, pInboundEventLevel: POINTER(Windows.Win32.Devices.Fax.FAX_LOG_LEVEL_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_InboundEventsLevel(self, InboundEventLevel: Windows.Win32.Devices.Fax.FAX_LOG_LEVEL_ENUM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_OutboundEventsLevel(self, pOutboundEventLevel: POINTER(Windows.Win32.Devices.Fax.FAX_LOG_LEVEL_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_OutboundEventsLevel(self, OutboundEventLevel: Windows.Win32.Devices.Fax.FAX_LOG_LEVEL_ENUM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_GeneralEventsLevel(self, pGeneralEventLevel: POINTER(Windows.Win32.Devices.Fax.FAX_LOG_LEVEL_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_GeneralEventsLevel(self, GeneralEventLevel: Windows.Win32.Devices.Fax.FAX_LOG_LEVEL_ENUM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def Refresh(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Save(self) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxFolders(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{dce3b2a8-a7ab-42bc-9d0a-3149457261a0}')
    @commethod(7)
    def get_OutgoingQueue(self, pFaxOutgoingQueue: POINTER(Windows.Win32.Devices.Fax.IFaxOutgoingQueue_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_IncomingQueue(self, pFaxIncomingQueue: POINTER(Windows.Win32.Devices.Fax.IFaxIncomingQueue_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_IncomingArchive(self, pFaxIncomingArchive: POINTER(Windows.Win32.Devices.Fax.IFaxIncomingArchive_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_OutgoingArchive(self, pFaxOutgoingArchive: POINTER(Windows.Win32.Devices.Fax.IFaxOutgoingArchive_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxInboundRouting(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{8148c20f-9d52-45b1-bf96-38fc12713527}')
    @commethod(7)
    def GetExtensions(self, pFaxInboundRoutingExtensions: POINTER(Windows.Win32.Devices.Fax.IFaxInboundRoutingExtensions_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetMethods(self, pFaxInboundRoutingMethods: POINTER(Windows.Win32.Devices.Fax.IFaxInboundRoutingMethods_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxInboundRoutingExtension(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{885b5e08-c26c-4ef9-af83-51580a750be1}')
    @commethod(7)
    def get_FriendlyName(self, pbstrFriendlyName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_ImageName(self, pbstrImageName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_UniqueName(self, pbstrUniqueName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_MajorVersion(self, plMajorVersion: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_MinorVersion(self, plMinorVersion: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_MajorBuild(self, plMajorBuild: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_MinorBuild(self, plMinorBuild: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_Debug(self, pbDebug: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Status(self, pStatus: POINTER(Windows.Win32.Devices.Fax.FAX_PROVIDER_STATUS_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_InitErrorCode(self, plInitErrorCode: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_Methods(self, pvMethods: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxInboundRoutingExtensions(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{2f6c9673-7b26-42de-8eb0-915dcd2a4f4c}')
    @commethod(7)
    def get__NewEnum(self, ppUnk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, vIndex: Windows.Win32.System.Variant.VARIANT, pFaxInboundRoutingExtension: POINTER(Windows.Win32.Devices.Fax.IFaxInboundRoutingExtension_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(self, plCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxInboundRoutingMethod(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{45700061-ad9d-4776-a8c4-64065492cf4b}')
    @commethod(7)
    def get_Name(self, pbstrName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_GUID(self, pbstrGUID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_FunctionName(self, pbstrFunctionName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_ExtensionFriendlyName(self, pbstrExtensionFriendlyName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_ExtensionImageName(self, pbstrExtensionImageName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Priority(self, plPriority: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_Priority(self, lPriority: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def Refresh(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def Save(self) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxInboundRoutingMethods(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{783fca10-8908-4473-9d69-f67fbea0c6b9}')
    @commethod(7)
    def get__NewEnum(self, ppUnk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, vIndex: Windows.Win32.System.Variant.VARIANT, pFaxInboundRoutingMethod: POINTER(Windows.Win32.Devices.Fax.IFaxInboundRoutingMethod_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(self, plCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxIncomingArchive(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{76062cc7-f714-4fbd-aa06-ed6e4a4b70f3}')
    @commethod(7)
    def get_UseArchive(self, pbUseArchive: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_UseArchive(self, bUseArchive: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ArchiveFolder(self, pbstrArchiveFolder: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_ArchiveFolder(self, bstrArchiveFolder: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_SizeQuotaWarning(self, pbSizeQuotaWarning: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_SizeQuotaWarning(self, bSizeQuotaWarning: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_HighQuotaWaterMark(self, plHighQuotaWaterMark: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_HighQuotaWaterMark(self, lHighQuotaWaterMark: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_LowQuotaWaterMark(self, plLowQuotaWaterMark: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_LowQuotaWaterMark(self, lLowQuotaWaterMark: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_AgeLimit(self, plAgeLimit: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_AgeLimit(self, lAgeLimit: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_SizeLow(self, plSizeLow: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_SizeHigh(self, plSizeHigh: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def Refresh(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def Save(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetMessages(self, lPrefetchSize: Int32, pFaxIncomingMessageIterator: POINTER(Windows.Win32.Devices.Fax.IFaxIncomingMessageIterator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetMessage(self, bstrMessageId: Windows.Win32.Foundation.BSTR, pFaxIncomingMessage: POINTER(Windows.Win32.Devices.Fax.IFaxIncomingMessage_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxIncomingJob(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{207529e6-654a-4916-9f88-4d232ee8a107}')
    @commethod(7)
    def get_Size(self, plSize: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Id(self, pbstrId: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_CurrentPage(self, plCurrentPage: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_DeviceId(self, plDeviceId: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Status(self, pStatus: POINTER(Windows.Win32.Devices.Fax.FAX_JOB_STATUS_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_ExtendedStatusCode(self, pExtendedStatusCode: POINTER(Windows.Win32.Devices.Fax.FAX_JOB_EXTENDED_STATUS_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_ExtendedStatus(self, pbstrExtendedStatus: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_AvailableOperations(self, pAvailableOperations: POINTER(Windows.Win32.Devices.Fax.FAX_JOB_OPERATIONS_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Retries(self, plRetries: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_TransmissionStart(self, pdateTransmissionStart: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_TransmissionEnd(self, pdateTransmissionEnd: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_CSID(self, pbstrCSID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_TSID(self, pbstrTSID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_CallerId(self, pbstrCallerId: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_RoutingInformation(self, pbstrRoutingInformation: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_JobType(self, pJobType: POINTER(Windows.Win32.Devices.Fax.FAX_JOB_TYPE_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def Cancel(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def Refresh(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def CopyTiff(self, bstrTiffPath: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxIncomingJobs(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{011f04e9-4fd6-4c23-9513-b6b66bb26be9}')
    @commethod(7)
    def get__NewEnum(self, ppUnk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, vIndex: Windows.Win32.System.Variant.VARIANT, pFaxIncomingJob: POINTER(Windows.Win32.Devices.Fax.IFaxIncomingJob_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(self, plCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxIncomingMessage(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{7cab88fa-2ef9-4851-b2f3-1d148fed8447}')
    @commethod(7)
    def get_Id(self, pbstrId: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Pages(self, plPages: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Size(self, plSize: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_DeviceName(self, pbstrDeviceName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Retries(self, plRetries: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_TransmissionStart(self, pdateTransmissionStart: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_TransmissionEnd(self, pdateTransmissionEnd: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_CSID(self, pbstrCSID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_TSID(self, pbstrTSID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_CallerId(self, pbstrCallerId: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_RoutingInformation(self, pbstrRoutingInformation: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def CopyTiff(self, bstrTiffPath: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def Delete(self) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxIncomingMessage2(ComPtr):
    extends: Windows.Win32.Devices.Fax.IFaxIncomingMessage
    _iid_ = Guid('{f9208503-e2bc-48f3-9ec0-e6236f9b509a}')
    @commethod(20)
    def get_Subject(self, pbstrSubject: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def put_Subject(self, bstrSubject: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_SenderName(self, pbstrSenderName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_SenderName(self, bstrSenderName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_SenderFaxNumber(self, pbstrSenderFaxNumber: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_SenderFaxNumber(self, bstrSenderFaxNumber: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_HasCoverPage(self, pbHasCoverPage: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_HasCoverPage(self, bHasCoverPage: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_Recipients(self, pbstrRecipients: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def put_Recipients(self, bstrRecipients: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_WasReAssigned(self, pbWasReAssigned: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_Read(self, pbRead: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def put_Read(self, bRead: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def ReAssign(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def Save(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def Refresh(self) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxIncomingMessageIterator(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{fd73ecc4-6f06-4f52-82a8-f7ba06ae3108}')
    @commethod(7)
    def get_Message(self, pFaxIncomingMessage: POINTER(Windows.Win32.Devices.Fax.IFaxIncomingMessage_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_PrefetchSize(self, plPrefetchSize: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_PrefetchSize(self, lPrefetchSize: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_AtEOF(self, pbEOF: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def MoveFirst(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def MoveNext(self) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxIncomingQueue(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{902e64ef-8fd8-4b75-9725-6014df161545}')
    @commethod(7)
    def get_Blocked(self, pbBlocked: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Blocked(self, bBlocked: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Refresh(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Save(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetJobs(self, pFaxIncomingJobs: POINTER(Windows.Win32.Devices.Fax.IFaxIncomingJobs_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetJob(self, bstrJobId: Windows.Win32.Foundation.BSTR, pFaxIncomingJob: POINTER(Windows.Win32.Devices.Fax.IFaxIncomingJob_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxJobStatus(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{8b86f485-fd7f-4824-886b-40c5caa617cc}')
    @commethod(7)
    def get_Status(self, pStatus: POINTER(Windows.Win32.Devices.Fax.FAX_JOB_STATUS_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Pages(self, plPages: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Size(self, plSize: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_CurrentPage(self, plCurrentPage: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_DeviceId(self, plDeviceId: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_CSID(self, pbstrCSID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_TSID(self, pbstrTSID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_ExtendedStatusCode(self, pExtendedStatusCode: POINTER(Windows.Win32.Devices.Fax.FAX_JOB_EXTENDED_STATUS_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_ExtendedStatus(self, pbstrExtendedStatus: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_AvailableOperations(self, pAvailableOperations: POINTER(Windows.Win32.Devices.Fax.FAX_JOB_OPERATIONS_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_Retries(self, plRetries: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_JobType(self, pJobType: POINTER(Windows.Win32.Devices.Fax.FAX_JOB_TYPE_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_ScheduledTime(self, pdateScheduledTime: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_TransmissionStart(self, pdateTransmissionStart: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_TransmissionEnd(self, pdateTransmissionEnd: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_CallerId(self, pbstrCallerId: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_RoutingInformation(self, pbstrRoutingInformation: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxLoggingOptions(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{34e64fb9-6b31-4d32-8b27-d286c0c33606}')
    @commethod(7)
    def get_EventLogging(self, pFaxEventLogging: POINTER(Windows.Win32.Devices.Fax.IFaxEventLogging_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_ActivityLogging(self, pFaxActivityLogging: POINTER(Windows.Win32.Devices.Fax.IFaxActivityLogging_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxOutboundRouting(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{25dc05a4-9909-41bd-a95b-7e5d1dec1d43}')
    @commethod(7)
    def GetGroups(self, pFaxOutboundRoutingGroups: POINTER(Windows.Win32.Devices.Fax.IFaxOutboundRoutingGroups_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetRules(self, pFaxOutboundRoutingRules: POINTER(Windows.Win32.Devices.Fax.IFaxOutboundRoutingRules_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxOutboundRoutingGroup(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{ca6289a1-7e25-4f87-9a0b-93365734962c}')
    @commethod(7)
    def get_Name(self, pbstrName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Status(self, pStatus: POINTER(Windows.Win32.Devices.Fax.FAX_GROUP_STATUS_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_DeviceIds(self, pFaxDeviceIds: POINTER(Windows.Win32.Devices.Fax.IFaxDeviceIds_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxOutboundRoutingGroups(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{235cbef7-c2de-4bfd-b8da-75097c82c87f}')
    @commethod(7)
    def get__NewEnum(self, ppUnk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, vIndex: Windows.Win32.System.Variant.VARIANT, pFaxOutboundRoutingGroup: POINTER(Windows.Win32.Devices.Fax.IFaxOutboundRoutingGroup_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(self, plCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Add(self, bstrName: Windows.Win32.Foundation.BSTR, pFaxOutboundRoutingGroup: POINTER(Windows.Win32.Devices.Fax.IFaxOutboundRoutingGroup_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(self, vIndex: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxOutboundRoutingRule(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{e1f795d5-07c2-469f-b027-acacc23219da}')
    @commethod(7)
    def get_CountryCode(self, plCountryCode: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_AreaCode(self, plAreaCode: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Status(self, pStatus: POINTER(Windows.Win32.Devices.Fax.FAX_RULE_STATUS_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_UseDevice(self, pbUseDevice: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_UseDevice(self, bUseDevice: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_DeviceId(self, plDeviceId: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_DeviceId(self, DeviceId: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_GroupName(self, pbstrGroupName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_GroupName(self, bstrGroupName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Refresh(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def Save(self) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxOutboundRoutingRules(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{dcefa1e7-ae7d-4ed6-8521-369edcca5120}')
    @commethod(7)
    def get__NewEnum(self, ppUnk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, lIndex: Int32, pFaxOutboundRoutingRule: POINTER(Windows.Win32.Devices.Fax.IFaxOutboundRoutingRule_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(self, plCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def ItemByCountryAndArea(self, lCountryCode: Int32, lAreaCode: Int32, pFaxOutboundRoutingRule: POINTER(Windows.Win32.Devices.Fax.IFaxOutboundRoutingRule_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RemoveByCountryAndArea(self, lCountryCode: Int32, lAreaCode: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Remove(self, lIndex: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Add(self, lCountryCode: Int32, lAreaCode: Int32, bUseDevice: Windows.Win32.Foundation.VARIANT_BOOL, bstrGroupName: Windows.Win32.Foundation.BSTR, lDeviceId: Int32, pFaxOutboundRoutingRule: POINTER(Windows.Win32.Devices.Fax.IFaxOutboundRoutingRule_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxOutgoingArchive(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{c9c28f40-8d80-4e53-810f-9a79919b49fd}')
    @commethod(7)
    def get_UseArchive(self, pbUseArchive: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_UseArchive(self, bUseArchive: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ArchiveFolder(self, pbstrArchiveFolder: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_ArchiveFolder(self, bstrArchiveFolder: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_SizeQuotaWarning(self, pbSizeQuotaWarning: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_SizeQuotaWarning(self, bSizeQuotaWarning: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_HighQuotaWaterMark(self, plHighQuotaWaterMark: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_HighQuotaWaterMark(self, lHighQuotaWaterMark: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_LowQuotaWaterMark(self, plLowQuotaWaterMark: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_LowQuotaWaterMark(self, lLowQuotaWaterMark: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_AgeLimit(self, plAgeLimit: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_AgeLimit(self, lAgeLimit: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_SizeLow(self, plSizeLow: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_SizeHigh(self, plSizeHigh: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def Refresh(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def Save(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetMessages(self, lPrefetchSize: Int32, pFaxOutgoingMessageIterator: POINTER(Windows.Win32.Devices.Fax.IFaxOutgoingMessageIterator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetMessage(self, bstrMessageId: Windows.Win32.Foundation.BSTR, pFaxOutgoingMessage: POINTER(Windows.Win32.Devices.Fax.IFaxOutgoingMessage_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxOutgoingJob(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{6356daad-6614-4583-bf7a-3ad67bbfc71c}')
    @commethod(7)
    def get_Subject(self, pbstrSubject: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_DocumentName(self, pbstrDocumentName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Pages(self, plPages: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Size(self, plSize: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_SubmissionId(self, pbstrSubmissionId: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Id(self, pbstrId: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_OriginalScheduledTime(self, pdateOriginalScheduledTime: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_SubmissionTime(self, pdateSubmissionTime: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_ReceiptType(self, pReceiptType: POINTER(Windows.Win32.Devices.Fax.FAX_RECEIPT_TYPE_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_Priority(self, pPriority: POINTER(Windows.Win32.Devices.Fax.FAX_PRIORITY_TYPE_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_Sender(self, ppFaxSender: POINTER(Windows.Win32.Devices.Fax.IFaxSender_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_Recipient(self, ppFaxRecipient: POINTER(Windows.Win32.Devices.Fax.IFaxRecipient_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_CurrentPage(self, plCurrentPage: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_DeviceId(self, plDeviceId: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_Status(self, pStatus: POINTER(Windows.Win32.Devices.Fax.FAX_JOB_STATUS_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_ExtendedStatusCode(self, pExtendedStatusCode: POINTER(Windows.Win32.Devices.Fax.FAX_JOB_EXTENDED_STATUS_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_ExtendedStatus(self, pbstrExtendedStatus: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_AvailableOperations(self, pAvailableOperations: POINTER(Windows.Win32.Devices.Fax.FAX_JOB_OPERATIONS_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_Retries(self, plRetries: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_ScheduledTime(self, pdateScheduledTime: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_TransmissionStart(self, pdateTransmissionStart: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_TransmissionEnd(self, pdateTransmissionEnd: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def get_CSID(self, pbstrCSID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_TSID(self, pbstrTSID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_GroupBroadcastReceipts(self, pbGroupBroadcastReceipts: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def Pause(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def Resume(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def Restart(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def CopyTiff(self, bstrTiffPath: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def Refresh(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def Cancel(self) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxOutgoingJob2(ComPtr):
    extends: Windows.Win32.Devices.Fax.IFaxOutgoingJob
    _iid_ = Guid('{418a8d96-59a0-4789-b176-edf3dc8fa8f7}')
    @commethod(38)
    def get_HasCoverPage(self, pbHasCoverPage: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def get_ReceiptAddress(self, pbstrReceiptAddress: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def get_ScheduleType(self, pScheduleType: POINTER(Windows.Win32.Devices.Fax.FAX_SCHEDULE_TYPE_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxOutgoingJobs(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{2c56d8e6-8c2f-4573-944c-e505f8f5aeed}')
    @commethod(7)
    def get__NewEnum(self, ppUnk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, vIndex: Windows.Win32.System.Variant.VARIANT, pFaxOutgoingJob: POINTER(Windows.Win32.Devices.Fax.IFaxOutgoingJob_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(self, plCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxOutgoingMessage(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{f0ea35de-caa5-4a7c-82c7-2b60ba5f2be2}')
    @commethod(7)
    def get_SubmissionId(self, pbstrSubmissionId: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Id(self, pbstrId: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Subject(self, pbstrSubject: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_DocumentName(self, pbstrDocumentName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Retries(self, plRetries: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Pages(self, plPages: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Size(self, plSize: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_OriginalScheduledTime(self, pdateOriginalScheduledTime: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_SubmissionTime(self, pdateSubmissionTime: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_Priority(self, pPriority: POINTER(Windows.Win32.Devices.Fax.FAX_PRIORITY_TYPE_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_Sender(self, ppFaxSender: POINTER(Windows.Win32.Devices.Fax.IFaxSender_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_Recipient(self, ppFaxRecipient: POINTER(Windows.Win32.Devices.Fax.IFaxRecipient_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_DeviceName(self, pbstrDeviceName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_TransmissionStart(self, pdateTransmissionStart: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_TransmissionEnd(self, pdateTransmissionEnd: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_CSID(self, pbstrCSID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_TSID(self, pbstrTSID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def CopyTiff(self, bstrTiffPath: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def Delete(self) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxOutgoingMessage2(ComPtr):
    extends: Windows.Win32.Devices.Fax.IFaxOutgoingMessage
    _iid_ = Guid('{b37df687-bc88-4b46-b3be-b458b3ea9e7f}')
    @commethod(26)
    def get_HasCoverPage(self, pbHasCoverPage: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_ReceiptType(self, pReceiptType: POINTER(Windows.Win32.Devices.Fax.FAX_RECEIPT_TYPE_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_ReceiptAddress(self, pbstrReceiptAddress: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def get_Read(self, pbRead: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def put_Read(self, bRead: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def Save(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def Refresh(self) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxOutgoingMessageIterator(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{f5ec5d4f-b840-432f-9980-112fe42a9b7a}')
    @commethod(7)
    def get_Message(self, pFaxOutgoingMessage: POINTER(Windows.Win32.Devices.Fax.IFaxOutgoingMessage_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_AtEOF(self, pbEOF: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_PrefetchSize(self, plPrefetchSize: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_PrefetchSize(self, lPrefetchSize: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def MoveFirst(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def MoveNext(self) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxOutgoingQueue(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{80b1df24-d9ac-4333-b373-487cedc80ce5}')
    @commethod(7)
    def get_Blocked(self, pbBlocked: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Blocked(self, bBlocked: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Paused(self, pbPaused: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Paused(self, bPaused: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_AllowPersonalCoverPages(self, pbAllowPersonalCoverPages: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_AllowPersonalCoverPages(self, bAllowPersonalCoverPages: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_UseDeviceTSID(self, pbUseDeviceTSID: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_UseDeviceTSID(self, bUseDeviceTSID: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Retries(self, plRetries: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_Retries(self, lRetries: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_RetryDelay(self, plRetryDelay: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_RetryDelay(self, lRetryDelay: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_DiscountRateStart(self, pdateDiscountRateStart: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_DiscountRateStart(self, dateDiscountRateStart: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_DiscountRateEnd(self, pdateDiscountRateEnd: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_DiscountRateEnd(self, dateDiscountRateEnd: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_AgeLimit(self, plAgeLimit: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_AgeLimit(self, lAgeLimit: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_Branding(self, pbBranding: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_Branding(self, bBranding: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def Refresh(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def Save(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def GetJobs(self, pFaxOutgoingJobs: POINTER(Windows.Win32.Devices.Fax.IFaxOutgoingJobs_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def GetJob(self, bstrJobId: Windows.Win32.Foundation.BSTR, pFaxOutgoingJob: POINTER(Windows.Win32.Devices.Fax.IFaxOutgoingJob_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxReceiptOptions(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{378efaeb-5fcb-4afb-b2ee-e16e80614487}')
    @commethod(7)
    def get_AuthenticationType(self, pType: POINTER(Windows.Win32.Devices.Fax.FAX_SMTP_AUTHENTICATION_TYPE_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_AuthenticationType(self, Type: Windows.Win32.Devices.Fax.FAX_SMTP_AUTHENTICATION_TYPE_ENUM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_SMTPServer(self, pbstrSMTPServer: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_SMTPServer(self, bstrSMTPServer: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_SMTPPort(self, plSMTPPort: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_SMTPPort(self, lSMTPPort: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_SMTPSender(self, pbstrSMTPSender: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_SMTPSender(self, bstrSMTPSender: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_SMTPUser(self, pbstrSMTPUser: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_SMTPUser(self, bstrSMTPUser: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_AllowedReceipts(self, pAllowedReceipts: POINTER(Windows.Win32.Devices.Fax.FAX_RECEIPT_TYPE_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_AllowedReceipts(self, AllowedReceipts: Windows.Win32.Devices.Fax.FAX_RECEIPT_TYPE_ENUM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_SMTPPassword(self, pbstrSMTPPassword: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_SMTPPassword(self, bstrSMTPPassword: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def Refresh(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def Save(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_UseForInboundRouting(self, pbUseForInboundRouting: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_UseForInboundRouting(self, bUseForInboundRouting: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxRecipient(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{9a3da3a0-538d-42b6-9444-aaa57d0ce2bc}')
    @commethod(7)
    def get_FaxNumber(self, pbstrFaxNumber: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_FaxNumber(self, bstrFaxNumber: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Name(self, pbstrName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Name(self, bstrName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxRecipients(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{b9c9de5a-894e-4492-9fa3-08c627c11d5d}')
    @commethod(7)
    def get__NewEnum(self, ppUnk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, lIndex: Int32, ppFaxRecipient: POINTER(Windows.Win32.Devices.Fax.IFaxRecipient_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(self, plCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Add(self, bstrFaxNumber: Windows.Win32.Foundation.BSTR, bstrRecipientName: Windows.Win32.Foundation.BSTR, ppFaxRecipient: POINTER(Windows.Win32.Devices.Fax.IFaxRecipient_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(self, lIndex: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxSecurity(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{77b508c1-09c0-47a2-91eb-fce7fdf2690e}')
    @commethod(7)
    def get_Descriptor(self, pvDescriptor: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Descriptor(self, vDescriptor: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_GrantedRights(self, pGrantedRights: POINTER(Windows.Win32.Devices.Fax.FAX_ACCESS_RIGHTS_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Refresh(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Save(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_InformationType(self, plInformationType: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_InformationType(self, lInformationType: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxSecurity2(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{17d851f4-d09b-48fc-99c9-8f24c4db9ab1}')
    @commethod(7)
    def get_Descriptor(self, pvDescriptor: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Descriptor(self, vDescriptor: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_GrantedRights(self, pGrantedRights: POINTER(Windows.Win32.Devices.Fax.FAX_ACCESS_RIGHTS_ENUM_2)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Refresh(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Save(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_InformationType(self, plInformationType: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_InformationType(self, lInformationType: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxSender(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{0d879d7d-f57a-4cc6-a6f9-3ee5d527b46a}')
    @commethod(7)
    def get_BillingCode(self, pbstrBillingCode: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_BillingCode(self, bstrBillingCode: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_City(self, pbstrCity: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_City(self, bstrCity: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Company(self, pbstrCompany: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_Company(self, bstrCompany: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Country(self, pbstrCountry: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_Country(self, bstrCountry: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Department(self, pbstrDepartment: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_Department(self, bstrDepartment: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_Email(self, pbstrEmail: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_Email(self, bstrEmail: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_FaxNumber(self, pbstrFaxNumber: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_FaxNumber(self, bstrFaxNumber: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_HomePhone(self, pbstrHomePhone: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_HomePhone(self, bstrHomePhone: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_Name(self, pbstrName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_Name(self, bstrName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_TSID(self, pbstrTSID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_TSID(self, bstrTSID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_OfficePhone(self, pbstrOfficePhone: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def put_OfficePhone(self, bstrOfficePhone: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def get_OfficeLocation(self, pbstrOfficeLocation: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def put_OfficeLocation(self, bstrOfficeLocation: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_State(self, pbstrState: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def put_State(self, bstrState: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_StreetAddress(self, pbstrStreetAddress: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def put_StreetAddress(self, bstrStreetAddress: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def get_Title(self, pbstrTitle: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def put_Title(self, bstrTitle: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def get_ZipCode(self, pbstrZipCode: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def put_ZipCode(self, bstrZipCode: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def LoadDefaultSender(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def SaveDefaultSender(self) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxServer(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{475b6469-90a5-4878-a577-17a86e8e3462}')
    @commethod(7)
    def Connect(self, bstrServerName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_ServerName(self, pbstrServerName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetDeviceProviders(self, ppFaxDeviceProviders: POINTER(Windows.Win32.Devices.Fax.IFaxDeviceProviders_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetDevices(self, ppFaxDevices: POINTER(Windows.Win32.Devices.Fax.IFaxDevices_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_InboundRouting(self, ppFaxInboundRouting: POINTER(Windows.Win32.Devices.Fax.IFaxInboundRouting_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Folders(self, pFaxFolders: POINTER(Windows.Win32.Devices.Fax.IFaxFolders_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_LoggingOptions(self, ppFaxLoggingOptions: POINTER(Windows.Win32.Devices.Fax.IFaxLoggingOptions_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_MajorVersion(self, plMajorVersion: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_MinorVersion(self, plMinorVersion: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_MajorBuild(self, plMajorBuild: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_MinorBuild(self, plMinorBuild: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_Debug(self, pbDebug: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_Activity(self, ppFaxActivity: POINTER(Windows.Win32.Devices.Fax.IFaxActivity_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_OutboundRouting(self, ppFaxOutboundRouting: POINTER(Windows.Win32.Devices.Fax.IFaxOutboundRouting_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_ReceiptOptions(self, ppFaxReceiptOptions: POINTER(Windows.Win32.Devices.Fax.IFaxReceiptOptions_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_Security(self, ppFaxSecurity: POINTER(Windows.Win32.Devices.Fax.IFaxSecurity_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def Disconnect(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetExtensionProperty(self, bstrGUID: Windows.Win32.Foundation.BSTR, pvProperty: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def SetExtensionProperty(self, bstrGUID: Windows.Win32.Foundation.BSTR, vProperty: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def ListenToServerEvents(self, EventTypes: Windows.Win32.Devices.Fax.FAX_SERVER_EVENTS_TYPE_ENUM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def RegisterDeviceProvider(self, bstrGUID: Windows.Win32.Foundation.BSTR, bstrFriendlyName: Windows.Win32.Foundation.BSTR, bstrImageName: Windows.Win32.Foundation.BSTR, TspName: Windows.Win32.Foundation.BSTR, lFSPIVersion: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def UnregisterDeviceProvider(self, bstrUniqueName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def RegisterInboundRoutingExtension(self, bstrExtensionName: Windows.Win32.Foundation.BSTR, bstrFriendlyName: Windows.Win32.Foundation.BSTR, bstrImageName: Windows.Win32.Foundation.BSTR, vMethods: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def UnregisterInboundRoutingExtension(self, bstrExtensionUniqueName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_RegisteredEvents(self, pEventTypes: POINTER(Windows.Win32.Devices.Fax.FAX_SERVER_EVENTS_TYPE_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def get_APIVersion(self, pAPIVersion: POINTER(Windows.Win32.Devices.Fax.FAX_SERVER_APIVERSION_ENUM)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxServer2(ComPtr):
    extends: Windows.Win32.Devices.Fax.IFaxServer
    _iid_ = Guid('{571ced0f-5609-4f40-9176-547e3a72ca7c}')
    @commethod(33)
    def get_Configuration(self, ppFaxConfiguration: POINTER(Windows.Win32.Devices.Fax.IFaxConfiguration_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def get_CurrentAccount(self, ppCurrentAccount: POINTER(Windows.Win32.Devices.Fax.IFaxAccount_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def get_FaxAccountSet(self, ppFaxAccountSet: POINTER(Windows.Win32.Devices.Fax.IFaxAccountSet_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def get_Security2(self, ppFaxSecurity2: POINTER(Windows.Win32.Devices.Fax.IFaxSecurity2_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFaxServerNotify(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{2e037b27-cf8a-4abd-b1e0-5704943bea6f}')
class IFaxServerNotify2(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{ec9c69b9-5fe7-4805-9467-82fcd96af903}')
    @commethod(7)
    def OnIncomingJobAdded(self, pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head, bstrJobId: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnIncomingJobRemoved(self, pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head, bstrJobId: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OnIncomingJobChanged(self, pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head, bstrJobId: Windows.Win32.Foundation.BSTR, pJobStatus: Windows.Win32.Devices.Fax.IFaxJobStatus_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def OnOutgoingJobAdded(self, pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head, bstrJobId: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def OnOutgoingJobRemoved(self, pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head, bstrJobId: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def OnOutgoingJobChanged(self, pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head, bstrJobId: Windows.Win32.Foundation.BSTR, pJobStatus: Windows.Win32.Devices.Fax.IFaxJobStatus_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def OnIncomingMessageAdded(self, pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head, bstrMessageId: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def OnIncomingMessageRemoved(self, pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head, bstrMessageId: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def OnOutgoingMessageAdded(self, pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head, bstrMessageId: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def OnOutgoingMessageRemoved(self, pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head, bstrMessageId: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def OnReceiptOptionsChange(self, pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def OnActivityLoggingConfigChange(self, pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def OnSecurityConfigChange(self, pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def OnEventLoggingConfigChange(self, pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def OnOutgoingQueueConfigChange(self, pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def OnOutgoingArchiveConfigChange(self, pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def OnIncomingArchiveConfigChange(self, pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def OnDevicesConfigChange(self, pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def OnOutboundRoutingGroupsConfigChange(self, pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def OnOutboundRoutingRulesConfigChange(self, pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def OnServerActivityChange(self, pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head, lIncomingMessages: Int32, lRoutingMessages: Int32, lOutgoingMessages: Int32, lQueuedMessages: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def OnQueuesStatusChange(self, pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head, bOutgoingQueueBlocked: Windows.Win32.Foundation.VARIANT_BOOL, bOutgoingQueuePaused: Windows.Win32.Foundation.VARIANT_BOOL, bIncomingQueueBlocked: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def OnNewCall(self, pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head, lCallId: Int32, lDeviceId: Int32, bstrCallerId: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def OnServerShutDown(self, pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def OnDeviceStatusChange(self, pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head, lDeviceId: Int32, bPoweredOff: Windows.Win32.Foundation.VARIANT_BOOL, bSending: Windows.Win32.Foundation.VARIANT_BOOL, bReceiving: Windows.Win32.Foundation.VARIANT_BOOL, bRinging: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def OnGeneralServerConfigChanged(self, pFaxServer: Windows.Win32.Devices.Fax.IFaxServer2_head) -> Windows.Win32.Foundation.HRESULT: ...
class IStiDevice(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6cfa5a80-2dc8-11d0-90ea-00aa0060f86c}')
    @commethod(3)
    def Initialize(self, hinst: Windows.Win32.Foundation.HMODULE, pwszDeviceName: Windows.Win32.Foundation.PWSTR, dwVersion: UInt32, dwMode: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCapabilities(self, pDevCaps: POINTER(Windows.Win32.Devices.Fax.STI_DEV_CAPS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetStatus(self, pDevStatus: POINTER(Windows.Win32.Devices.Fax.STI_DEVICE_STATUS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def DeviceReset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Diagnostic(self, pBuffer: POINTER(Windows.Win32.Devices.Fax.STI_DIAG_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Escape(self, EscapeFunction: UInt32, lpInData: c_void_p, cbInDataSize: UInt32, pOutData: c_void_p, dwOutDataSize: UInt32, pdwActualData: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetLastError(self, pdwLastDeviceError: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def LockDevice(self, dwTimeOut: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def UnLockDevice(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def RawReadData(self, lpBuffer: c_void_p, lpdwNumberOfBytes: POINTER(UInt32), lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def RawWriteData(self, lpBuffer: c_void_p, nNumberOfBytes: UInt32, lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def RawReadCommand(self, lpBuffer: c_void_p, lpdwNumberOfBytes: POINTER(UInt32), lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def RawWriteCommand(self, lpBuffer: c_void_p, nNumberOfBytes: UInt32, lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Subscribe(self, lpSubsribe: POINTER(Windows.Win32.Devices.Fax.STISUBSCRIBE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetLastNotificationData(self, lpNotify: POINTER(Windows.Win32.Devices.Fax.STINOTIFY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def UnSubscribe(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetLastErrorInfo(self, pLastErrorInfo: POINTER(Windows.Win32.Devices.Fax._ERROR_INFOW_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IStiDeviceControl(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{128a9860-52dc-11d0-9edf-444553540000}')
    @commethod(3)
    def Initialize(self, dwDeviceType: UInt32, dwMode: UInt32, pwszPortName: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RawReadData(self, lpBuffer: c_void_p, lpdwNumberOfBytes: POINTER(UInt32), lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RawWriteData(self, lpBuffer: c_void_p, nNumberOfBytes: UInt32, lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RawReadCommand(self, lpBuffer: c_void_p, lpdwNumberOfBytes: POINTER(UInt32), lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RawWriteCommand(self, lpBuffer: c_void_p, nNumberOfBytes: UInt32, lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RawDeviceControl(self, EscapeFunction: UInt32, lpInData: c_void_p, cbInDataSize: UInt32, pOutData: c_void_p, dwOutDataSize: UInt32, pdwActualData: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetLastError(self, lpdwLastError: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetMyDevicePortName(self, lpszDevicePath: Windows.Win32.Foundation.PWSTR, cwDevicePathSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetMyDeviceHandle(self, lph: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetMyDeviceOpenMode(self, pdwOpenMode: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def WriteToErrorLog(self, dwMessageType: UInt32, pszMessage: Windows.Win32.Foundation.PWSTR, dwErrorCode: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IStiUSD(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0c9bb460-51ac-11d0-90ea-00aa0060f86c}')
    @commethod(3)
    def Initialize(self, pHelDcb: Windows.Win32.Devices.Fax.IStiDeviceControl_head, dwStiVersion: UInt32, hParametersKey: Windows.Win32.System.Registry.HKEY) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCapabilities(self, pDevCaps: POINTER(Windows.Win32.Devices.Fax.STI_USD_CAPS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetStatus(self, pDevStatus: POINTER(Windows.Win32.Devices.Fax.STI_DEVICE_STATUS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def DeviceReset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Diagnostic(self, pBuffer: POINTER(Windows.Win32.Devices.Fax.STI_DIAG_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Escape(self, EscapeFunction: UInt32, lpInData: c_void_p, cbInDataSize: UInt32, pOutData: c_void_p, cbOutDataSize: UInt32, pdwActualData: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetLastError(self, pdwLastDeviceError: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def LockDevice(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def UnLockDevice(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def RawReadData(self, lpBuffer: c_void_p, lpdwNumberOfBytes: POINTER(UInt32), lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def RawWriteData(self, lpBuffer: c_void_p, nNumberOfBytes: UInt32, lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def RawReadCommand(self, lpBuffer: c_void_p, lpdwNumberOfBytes: POINTER(UInt32), lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def RawWriteCommand(self, lpBuffer: c_void_p, nNumberOfBytes: UInt32, lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetNotificationHandle(self, hEvent: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetNotificationData(self, lpNotify: POINTER(Windows.Win32.Devices.Fax.STINOTIFY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetLastErrorInfo(self, pLastErrorInfo: POINTER(Windows.Win32.Devices.Fax._ERROR_INFOW_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IStillImageW(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{641bd880-2dc8-11d0-90ea-00aa0060f86c}')
    @commethod(3)
    def Initialize(self, hinst: Windows.Win32.Foundation.HMODULE, dwVersion: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDeviceList(self, dwType: UInt32, dwFlags: UInt32, pdwItemsReturned: POINTER(UInt32), ppBuffer: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDeviceInfo(self, pwszDeviceName: Windows.Win32.Foundation.PWSTR, ppBuffer: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateDevice(self, pwszDeviceName: Windows.Win32.Foundation.PWSTR, dwMode: UInt32, pDevice: POINTER(Windows.Win32.Devices.Fax.IStiDevice_head), punkOuter: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetDeviceValue(self, pwszDeviceName: Windows.Win32.Foundation.PWSTR, pValueName: Windows.Win32.Foundation.PWSTR, pType: POINTER(UInt32), pData: POINTER(Byte), cbData: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetDeviceValue(self, pwszDeviceName: Windows.Win32.Foundation.PWSTR, pValueName: Windows.Win32.Foundation.PWSTR, Type: UInt32, pData: POINTER(Byte), cbData: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetSTILaunchInformation(self, pwszDeviceName: Windows.Win32.Foundation.PWSTR, pdwEventCode: POINTER(UInt32), pwszEventName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def RegisterLaunchApplication(self, pwszAppName: Windows.Win32.Foundation.PWSTR, pwszCommandLine: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def UnregisterLaunchApplication(self, pwszAppName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def EnableHwNotifications(self, pwszDeviceName: Windows.Win32.Foundation.PWSTR, bNewState: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetHwNotificationState(self, pwszDeviceName: Windows.Win32.Foundation.PWSTR, pbCurrentState: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def RefreshDeviceBus(self, pwszDeviceName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def LaunchApplicationForDevice(self, pwszDeviceName: Windows.Win32.Foundation.PWSTR, pwszAppName: Windows.Win32.Foundation.PWSTR, pStiNotify: POINTER(Windows.Win32.Devices.Fax.STINOTIFY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetupDeviceParameters(self, param0: POINTER(Windows.Win32.Devices.Fax.STI_DEVICE_INFORMATIONW_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def WriteToErrorLog(self, dwMessageType: UInt32, pszMessage: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
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
def PFAXGETPAGEDATA(FaxHandle: Windows.Win32.Foundation.HANDLE, JobId: UInt32, Buffer: POINTER(POINTER(Byte)), BufferSize: POINTER(UInt32), ImageWidth: POINTER(UInt32), ImageHeight: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXGETPORTA(FaxPortHandle: Windows.Win32.Foundation.HANDLE, PortInfo: POINTER(POINTER(Windows.Win32.Devices.Fax.FAX_PORT_INFOA_head))) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXGETPORTW(FaxPortHandle: Windows.Win32.Foundation.HANDLE, PortInfo: POINTER(POINTER(Windows.Win32.Devices.Fax.FAX_PORT_INFOW_head))) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXGETROUTINGINFOA(FaxPortHandle: Windows.Win32.Foundation.HANDLE, RoutingGuid: Windows.Win32.Foundation.PSTR, RoutingInfoBuffer: POINTER(POINTER(Byte)), RoutingInfoBufferSize: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXGETROUTINGINFOW(FaxPortHandle: Windows.Win32.Foundation.HANDLE, RoutingGuid: Windows.Win32.Foundation.PWSTR, RoutingInfoBuffer: POINTER(POINTER(Byte)), RoutingInfoBufferSize: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
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
def PFAXROUTEGETROUTINGINFO(param0: Windows.Win32.Foundation.PWSTR, param1: UInt32, param2: POINTER(Byte), param3: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXROUTEINITIALIZE(param0: Windows.Win32.Foundation.HANDLE, param1: POINTER(Windows.Win32.Devices.Fax.FAX_ROUTE_CALLBACKROUTINES_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXROUTEMETHOD(param0: POINTER(Windows.Win32.Devices.Fax.FAX_ROUTE_head), param1: POINTER(c_void_p), param2: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXROUTEMODIFYROUTINGDATA(JobId: UInt32, RoutingGuid: Windows.Win32.Foundation.PWSTR, RoutingData: POINTER(Byte), RoutingDataSize: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXROUTESETROUTINGINFO(param0: Windows.Win32.Foundation.PWSTR, param1: UInt32, param2: POINTER(Byte), param3: UInt32) -> Windows.Win32.Foundation.BOOL: ...
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
def PFAXSETROUTINGINFOA(FaxPortHandle: Windows.Win32.Foundation.HANDLE, RoutingGuid: Windows.Win32.Foundation.PSTR, RoutingInfoBuffer: POINTER(Byte), RoutingInfoBufferSize: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXSETROUTINGINFOW(FaxPortHandle: Windows.Win32.Foundation.HANDLE, RoutingGuid: Windows.Win32.Foundation.PWSTR, RoutingInfoBuffer: POINTER(Byte), RoutingInfoBufferSize: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXSTARTPRINTJOBA(PrinterName: Windows.Win32.Foundation.PSTR, PrintInfo: POINTER(Windows.Win32.Devices.Fax.FAX_PRINT_INFOA_head), FaxJobId: POINTER(UInt32), FaxContextInfo: POINTER(Windows.Win32.Devices.Fax.FAX_CONTEXT_INFOA_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXSTARTPRINTJOBW(PrinterName: Windows.Win32.Foundation.PWSTR, PrintInfo: POINTER(Windows.Win32.Devices.Fax.FAX_PRINT_INFOW_head), FaxJobId: POINTER(UInt32), FaxContextInfo: POINTER(Windows.Win32.Devices.Fax.FAX_CONTEXT_INFOW_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXUNREGISTERSERVICEPROVIDERW(DeviceProvider: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAX_EXT_CONFIG_CHANGE(param0: UInt32, param1: Windows.Win32.Foundation.PWSTR, param2: POINTER(Byte), param3: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFAX_EXT_FREE_BUFFER(param0: c_void_p) -> Void: ...
@winfunctype_pointer
def PFAX_EXT_GET_DATA(param0: UInt32, param1: Windows.Win32.Devices.Fax.FAX_ENUM_DEVICE_ID_SOURCE, param2: Windows.Win32.Foundation.PWSTR, param3: POINTER(POINTER(Byte)), param4: POINTER(UInt32)) -> UInt32: ...
@winfunctype_pointer
def PFAX_EXT_INITIALIZE_CONFIG(param0: Windows.Win32.Devices.Fax.PFAX_EXT_GET_DATA, param1: Windows.Win32.Devices.Fax.PFAX_EXT_SET_DATA, param2: Windows.Win32.Devices.Fax.PFAX_EXT_REGISTER_FOR_EVENTS, param3: Windows.Win32.Devices.Fax.PFAX_EXT_UNREGISTER_FOR_EVENTS, param4: Windows.Win32.Devices.Fax.PFAX_EXT_FREE_BUFFER) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFAX_EXT_REGISTER_FOR_EVENTS(param0: Windows.Win32.Foundation.HMODULE, param1: UInt32, param2: Windows.Win32.Devices.Fax.FAX_ENUM_DEVICE_ID_SOURCE, param3: Windows.Win32.Foundation.PWSTR, param4: Windows.Win32.Devices.Fax.PFAX_EXT_CONFIG_CHANGE) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype_pointer
def PFAX_EXT_SET_DATA(param0: Windows.Win32.Foundation.HMODULE, param1: UInt32, param2: Windows.Win32.Devices.Fax.FAX_ENUM_DEVICE_ID_SOURCE, param3: Windows.Win32.Foundation.PWSTR, param4: POINTER(Byte), param5: UInt32) -> UInt32: ...
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
class STINOTIFY(EasyCastStructure):
    dwSize: UInt32
    guidNotificationCode: Guid
    abNotificationData: Byte * 64
class STISUBSCRIBE(EasyCastStructure):
    dwSize: UInt32
    dwFlags: UInt32
    dwFilter: UInt32
    hWndNotify: Windows.Win32.Foundation.HWND
    hEvent: Windows.Win32.Foundation.HANDLE
    uiNotificationMessage: UInt32
class STI_DEVICE_INFORMATIONW(EasyCastStructure):
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
class STI_DEVICE_STATUS(EasyCastStructure):
    dwSize: UInt32
    StatusMask: UInt32
    dwOnlineState: UInt32
    dwHardwareStatusCode: UInt32
    dwEventHandlingState: UInt32
    dwPollingInterval: UInt32
class STI_DEV_CAPS(EasyCastStructure):
    dwGeneric: UInt32
class STI_DIAG(EasyCastStructure):
    dwSize: UInt32
    dwBasicDiagCode: UInt32
    dwVendorDiagCode: UInt32
    dwStatusMask: UInt32
    sErrorInfo: Windows.Win32.Devices.Fax._ERROR_INFOW
class STI_USD_CAPS(EasyCastStructure):
    dwVersion: UInt32
    dwGenericCaps: UInt32
class STI_WIA_DEVICE_INFORMATIONW(EasyCastStructure):
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
class _ERROR_INFOW(EasyCastStructure):
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
