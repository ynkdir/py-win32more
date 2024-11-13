from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Devices.Fax
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Gdi
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.IO
import win32more.Windows.Win32.System.Registry
import win32more.Windows.Win32.System.Variant
import win32more.Windows.Win32.UI.Controls
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
FAX_E_SRV_OUTOFMEMORY: win32more.Windows.Win32.Foundation.HRESULT = -2147214503
FAX_E_GROUP_NOT_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -2147214502
FAX_E_BAD_GROUP_CONFIGURATION: win32more.Windows.Win32.Foundation.HRESULT = -2147214501
FAX_E_GROUP_IN_USE: win32more.Windows.Win32.Foundation.HRESULT = -2147214500
FAX_E_RULE_NOT_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -2147214499
FAX_E_NOT_NTFS: win32more.Windows.Win32.Foundation.HRESULT = -2147214498
FAX_E_DIRECTORY_IN_USE: win32more.Windows.Win32.Foundation.HRESULT = -2147214497
FAX_E_FILE_ACCESS_DENIED: win32more.Windows.Win32.Foundation.HRESULT = -2147214496
FAX_E_MESSAGE_NOT_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -2147214495
FAX_E_DEVICE_NUM_LIMIT_EXCEEDED: win32more.Windows.Win32.Foundation.HRESULT = -2147214494
FAX_E_NOT_SUPPORTED_ON_THIS_SKU: win32more.Windows.Win32.Foundation.HRESULT = -2147214493
FAX_E_VERSION_MISMATCH: win32more.Windows.Win32.Foundation.HRESULT = -2147214492
FAX_E_RECIPIENTS_LIMIT: win32more.Windows.Win32.Foundation.HRESULT = -2147214491
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
STIERR_OLD_VERSION: win32more.Windows.Win32.Foundation.HRESULT = -2147023746
STIERR_BETA_VERSION: win32more.Windows.Win32.Foundation.HRESULT = -2147023743
STIERR_BADDRIVER: win32more.Windows.Win32.Foundation.HRESULT = -2147024777
STIERR_DEVICENOTREG: Int32 = -2147221164
STIERR_OBJECTNOTFOUND: win32more.Windows.Win32.Foundation.HRESULT = -2147024894
STIERR_INVALID_PARAM: Int32 = -2147024809
STIERR_NOINTERFACE: Int32 = -2147467262
STIERR_GENERIC: Int32 = -2147467259
STIERR_OUTOFMEMORY: Int32 = -2147024882
STIERR_UNSUPPORTED: Int32 = -2147467263
STIERR_NOT_INITIALIZED: win32more.Windows.Win32.Foundation.HRESULT = -2147024875
STIERR_ALREADY_INITIALIZED: win32more.Windows.Win32.Foundation.HRESULT = -2147023649
STIERR_DEVICE_LOCKED: win32more.Windows.Win32.Foundation.HRESULT = -2147024863
STIERR_READONLY: Int32 = -2147024891
STIERR_NOTINITIALIZED: Int32 = -2147024891
STIERR_NEEDS_LOCK: win32more.Windows.Win32.Foundation.HRESULT = -2147024738
STIERR_SHARING_VIOLATION: win32more.Windows.Win32.Foundation.HRESULT = -2147024864
STIERR_HANDLEEXISTS: win32more.Windows.Win32.Foundation.HRESULT = -2147024713
STIERR_INVALID_DEVICE_NAME: win32more.Windows.Win32.Foundation.HRESULT = -2147024773
STIERR_INVALID_HW_TYPE: win32more.Windows.Win32.Foundation.HRESULT = -2147024883
STIERR_NOEVENTS: win32more.Windows.Win32.Foundation.HRESULT = -2147024637
STIERR_DEVICE_NOTREADY: win32more.Windows.Win32.Foundation.HRESULT = -2147024875
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
DEVPKEY_WIA_DeviceType: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{6bdd1fc6-810f-11d0-bec7-08002be2092f}'), pid=2)
DEVPKEY_WIA_USDClassId: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{6bdd1fc6-810f-11d0-bec7-08002be2092f}'), pid=3)
STI_USD_GENCAP_NATIVE_PUSHSUPPORT: UInt32 = 1
STI_DEVICE_CREATE_FOR_MONITOR: UInt32 = 16777216
lDEFAULT_PREFETCH_SIZE: Int32 = 100
wcharREASSIGN_RECIPIENTS_DELIMITER: UInt16 = 59
@winfunctype('WINFAX.dll')
def FaxConnectFaxServerA(MachineName: win32more.Windows.Win32.Foundation.PSTR, FaxHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxConnectFaxServerW(MachineName: win32more.Windows.Win32.Foundation.PWSTR, FaxHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
FaxConnectFaxServer = UnicodeAlias('FaxConnectFaxServerW')
@winfunctype('WINFAX.dll')
def FaxClose(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxOpenPort(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, DeviceId: UInt32, Flags: UInt32, FaxPortHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxCompleteJobParamsA(JobParams: POINTER(POINTER(win32more.Windows.Win32.Devices.Fax.FAX_JOB_PARAMA)), CoverpageInfo: POINTER(POINTER(win32more.Windows.Win32.Devices.Fax.FAX_COVERPAGE_INFOA))) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxCompleteJobParamsW(JobParams: POINTER(POINTER(win32more.Windows.Win32.Devices.Fax.FAX_JOB_PARAMW)), CoverpageInfo: POINTER(POINTER(win32more.Windows.Win32.Devices.Fax.FAX_COVERPAGE_INFOW))) -> win32more.Windows.Win32.Foundation.BOOL: ...
FaxCompleteJobParams = UnicodeAlias('FaxCompleteJobParamsW')
@winfunctype('WINFAX.dll')
def FaxSendDocumentA(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, FileName: win32more.Windows.Win32.Foundation.PSTR, JobParams: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_JOB_PARAMA), CoverpageInfo: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_COVERPAGE_INFOA), FaxJobId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxSendDocumentW(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, FileName: win32more.Windows.Win32.Foundation.PWSTR, JobParams: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_JOB_PARAMW), CoverpageInfo: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_COVERPAGE_INFOW), FaxJobId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
FaxSendDocument = UnicodeAlias('FaxSendDocumentW')
@winfunctype('WINFAX.dll')
def FaxSendDocumentForBroadcastA(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, FileName: win32more.Windows.Win32.Foundation.PSTR, FaxJobId: POINTER(UInt32), FaxRecipientCallback: win32more.Windows.Win32.Devices.Fax.PFAX_RECIPIENT_CALLBACKA, Context: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxSendDocumentForBroadcastW(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, FileName: win32more.Windows.Win32.Foundation.PWSTR, FaxJobId: POINTER(UInt32), FaxRecipientCallback: win32more.Windows.Win32.Devices.Fax.PFAX_RECIPIENT_CALLBACKW, Context: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
FaxSendDocumentForBroadcast = UnicodeAlias('FaxSendDocumentForBroadcastW')
@winfunctype('WINFAX.dll')
def FaxEnumJobsA(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, JobEntry: POINTER(POINTER(win32more.Windows.Win32.Devices.Fax.FAX_JOB_ENTRYA)), JobsReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxEnumJobsW(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, JobEntry: POINTER(POINTER(win32more.Windows.Win32.Devices.Fax.FAX_JOB_ENTRYW)), JobsReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
FaxEnumJobs = UnicodeAlias('FaxEnumJobsW')
@winfunctype('WINFAX.dll')
def FaxGetJobA(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, JobId: UInt32, JobEntry: POINTER(POINTER(win32more.Windows.Win32.Devices.Fax.FAX_JOB_ENTRYA))) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxGetJobW(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, JobId: UInt32, JobEntry: POINTER(POINTER(win32more.Windows.Win32.Devices.Fax.FAX_JOB_ENTRYW))) -> win32more.Windows.Win32.Foundation.BOOL: ...
FaxGetJob = UnicodeAlias('FaxGetJobW')
@winfunctype('WINFAX.dll')
def FaxSetJobA(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, JobId: UInt32, Command: UInt32, JobEntry: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_JOB_ENTRYA)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxSetJobW(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, JobId: UInt32, Command: UInt32, JobEntry: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_JOB_ENTRYW)) -> win32more.Windows.Win32.Foundation.BOOL: ...
FaxSetJob = UnicodeAlias('FaxSetJobW')
@winfunctype('WINFAX.dll')
def FaxGetPageData(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, JobId: UInt32, Buffer: POINTER(POINTER(Byte)), BufferSize: POINTER(UInt32), ImageWidth: POINTER(UInt32), ImageHeight: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxGetDeviceStatusA(FaxPortHandle: win32more.Windows.Win32.Foundation.HANDLE, DeviceStatus: POINTER(POINTER(win32more.Windows.Win32.Devices.Fax.FAX_DEVICE_STATUSA))) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxGetDeviceStatusW(FaxPortHandle: win32more.Windows.Win32.Foundation.HANDLE, DeviceStatus: POINTER(POINTER(win32more.Windows.Win32.Devices.Fax.FAX_DEVICE_STATUSW))) -> win32more.Windows.Win32.Foundation.BOOL: ...
FaxGetDeviceStatus = UnicodeAlias('FaxGetDeviceStatusW')
@winfunctype('WINFAX.dll')
def FaxAbort(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, JobId: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxGetConfigurationA(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, FaxConfig: POINTER(POINTER(win32more.Windows.Win32.Devices.Fax.FAX_CONFIGURATIONA))) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxGetConfigurationW(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, FaxConfig: POINTER(POINTER(win32more.Windows.Win32.Devices.Fax.FAX_CONFIGURATIONW))) -> win32more.Windows.Win32.Foundation.BOOL: ...
FaxGetConfiguration = UnicodeAlias('FaxGetConfigurationW')
@winfunctype('WINFAX.dll')
def FaxSetConfigurationA(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, FaxConfig: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_CONFIGURATIONA)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxSetConfigurationW(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, FaxConfig: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_CONFIGURATIONW)) -> win32more.Windows.Win32.Foundation.BOOL: ...
FaxSetConfiguration = UnicodeAlias('FaxSetConfigurationW')
@winfunctype('WINFAX.dll')
def FaxGetLoggingCategoriesA(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, Categories: POINTER(POINTER(win32more.Windows.Win32.Devices.Fax.FAX_LOG_CATEGORYA)), NumberCategories: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxGetLoggingCategoriesW(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, Categories: POINTER(POINTER(win32more.Windows.Win32.Devices.Fax.FAX_LOG_CATEGORYW)), NumberCategories: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
FaxGetLoggingCategories = UnicodeAlias('FaxGetLoggingCategoriesW')
@winfunctype('WINFAX.dll')
def FaxSetLoggingCategoriesA(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, Categories: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_LOG_CATEGORYA), NumberCategories: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxSetLoggingCategoriesW(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, Categories: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_LOG_CATEGORYW), NumberCategories: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
FaxSetLoggingCategories = UnicodeAlias('FaxSetLoggingCategoriesW')
@winfunctype('WINFAX.dll')
def FaxEnumPortsA(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, PortInfo: POINTER(POINTER(win32more.Windows.Win32.Devices.Fax.FAX_PORT_INFOA)), PortsReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxEnumPortsW(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, PortInfo: POINTER(POINTER(win32more.Windows.Win32.Devices.Fax.FAX_PORT_INFOW)), PortsReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
FaxEnumPorts = UnicodeAlias('FaxEnumPortsW')
@winfunctype('WINFAX.dll')
def FaxGetPortA(FaxPortHandle: win32more.Windows.Win32.Foundation.HANDLE, PortInfo: POINTER(POINTER(win32more.Windows.Win32.Devices.Fax.FAX_PORT_INFOA))) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxGetPortW(FaxPortHandle: win32more.Windows.Win32.Foundation.HANDLE, PortInfo: POINTER(POINTER(win32more.Windows.Win32.Devices.Fax.FAX_PORT_INFOW))) -> win32more.Windows.Win32.Foundation.BOOL: ...
FaxGetPort = UnicodeAlias('FaxGetPortW')
@winfunctype('WINFAX.dll')
def FaxSetPortA(FaxPortHandle: win32more.Windows.Win32.Foundation.HANDLE, PortInfo: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_PORT_INFOA)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxSetPortW(FaxPortHandle: win32more.Windows.Win32.Foundation.HANDLE, PortInfo: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_PORT_INFOW)) -> win32more.Windows.Win32.Foundation.BOOL: ...
FaxSetPort = UnicodeAlias('FaxSetPortW')
@winfunctype('WINFAX.dll')
def FaxEnumRoutingMethodsA(FaxPortHandle: win32more.Windows.Win32.Foundation.HANDLE, RoutingMethod: POINTER(POINTER(win32more.Windows.Win32.Devices.Fax.FAX_ROUTING_METHODA)), MethodsReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxEnumRoutingMethodsW(FaxPortHandle: win32more.Windows.Win32.Foundation.HANDLE, RoutingMethod: POINTER(POINTER(win32more.Windows.Win32.Devices.Fax.FAX_ROUTING_METHODW)), MethodsReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
FaxEnumRoutingMethods = UnicodeAlias('FaxEnumRoutingMethodsW')
@winfunctype('WINFAX.dll')
def FaxEnableRoutingMethodA(FaxPortHandle: win32more.Windows.Win32.Foundation.HANDLE, RoutingGuid: win32more.Windows.Win32.Foundation.PSTR, Enabled: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxEnableRoutingMethodW(FaxPortHandle: win32more.Windows.Win32.Foundation.HANDLE, RoutingGuid: win32more.Windows.Win32.Foundation.PWSTR, Enabled: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
FaxEnableRoutingMethod = UnicodeAlias('FaxEnableRoutingMethodW')
@winfunctype('WINFAX.dll')
def FaxEnumGlobalRoutingInfoA(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, RoutingInfo: POINTER(POINTER(win32more.Windows.Win32.Devices.Fax.FAX_GLOBAL_ROUTING_INFOA)), MethodsReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxEnumGlobalRoutingInfoW(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, RoutingInfo: POINTER(POINTER(win32more.Windows.Win32.Devices.Fax.FAX_GLOBAL_ROUTING_INFOW)), MethodsReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
FaxEnumGlobalRoutingInfo = UnicodeAlias('FaxEnumGlobalRoutingInfoW')
@winfunctype('WINFAX.dll')
def FaxSetGlobalRoutingInfoA(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, RoutingInfo: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_GLOBAL_ROUTING_INFOA)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxSetGlobalRoutingInfoW(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, RoutingInfo: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_GLOBAL_ROUTING_INFOW)) -> win32more.Windows.Win32.Foundation.BOOL: ...
FaxSetGlobalRoutingInfo = UnicodeAlias('FaxSetGlobalRoutingInfoW')
@winfunctype('WINFAX.dll')
def FaxGetRoutingInfoA(FaxPortHandle: win32more.Windows.Win32.Foundation.HANDLE, RoutingGuid: win32more.Windows.Win32.Foundation.PSTR, RoutingInfoBuffer: POINTER(POINTER(Byte)), RoutingInfoBufferSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxGetRoutingInfoW(FaxPortHandle: win32more.Windows.Win32.Foundation.HANDLE, RoutingGuid: win32more.Windows.Win32.Foundation.PWSTR, RoutingInfoBuffer: POINTER(POINTER(Byte)), RoutingInfoBufferSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
FaxGetRoutingInfo = UnicodeAlias('FaxGetRoutingInfoW')
@winfunctype('WINFAX.dll')
def FaxSetRoutingInfoA(FaxPortHandle: win32more.Windows.Win32.Foundation.HANDLE, RoutingGuid: win32more.Windows.Win32.Foundation.PSTR, RoutingInfoBuffer: POINTER(Byte), RoutingInfoBufferSize: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxSetRoutingInfoW(FaxPortHandle: win32more.Windows.Win32.Foundation.HANDLE, RoutingGuid: win32more.Windows.Win32.Foundation.PWSTR, RoutingInfoBuffer: POINTER(Byte), RoutingInfoBufferSize: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
FaxSetRoutingInfo = UnicodeAlias('FaxSetRoutingInfoW')
@winfunctype('WINFAX.dll')
def FaxInitializeEventQueue(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, CompletionPort: win32more.Windows.Win32.Foundation.HANDLE, CompletionKey: UIntPtr, hWnd: win32more.Windows.Win32.Foundation.HWND, MessageStart: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxFreeBuffer(Buffer: VoidPtr) -> Void: ...
@winfunctype('WINFAX.dll')
def FaxStartPrintJobA(PrinterName: win32more.Windows.Win32.Foundation.PSTR, PrintInfo: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_PRINT_INFOA), FaxJobId: POINTER(UInt32), FaxContextInfo: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_CONTEXT_INFOA)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxStartPrintJobW(PrinterName: win32more.Windows.Win32.Foundation.PWSTR, PrintInfo: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_PRINT_INFOW), FaxJobId: POINTER(UInt32), FaxContextInfo: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_CONTEXT_INFOW)) -> win32more.Windows.Win32.Foundation.BOOL: ...
FaxStartPrintJob = UnicodeAlias('FaxStartPrintJobW')
@winfunctype('WINFAX.dll')
def FaxPrintCoverPageA(FaxContextInfo: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_CONTEXT_INFOA), CoverPageInfo: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_COVERPAGE_INFOA)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxPrintCoverPageW(FaxContextInfo: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_CONTEXT_INFOW), CoverPageInfo: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_COVERPAGE_INFOW)) -> win32more.Windows.Win32.Foundation.BOOL: ...
FaxPrintCoverPage = UnicodeAlias('FaxPrintCoverPageW')
@winfunctype('WINFAX.dll')
def FaxRegisterServiceProviderW(DeviceProvider: win32more.Windows.Win32.Foundation.PWSTR, FriendlyName: win32more.Windows.Win32.Foundation.PWSTR, ImageName: win32more.Windows.Win32.Foundation.PWSTR, TspName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxUnregisterServiceProviderW(DeviceProvider: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxRegisterRoutingExtensionW(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, ExtensionName: win32more.Windows.Win32.Foundation.PWSTR, FriendlyName: win32more.Windows.Win32.Foundation.PWSTR, ImageName: win32more.Windows.Win32.Foundation.PWSTR, CallBack: win32more.Windows.Win32.Devices.Fax.PFAX_ROUTING_INSTALLATION_CALLBACKW, Context: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINFAX.dll')
def FaxAccessCheck(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, AccessMask: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('fxsutility.dll')
def CanSendToFaxRecipient() -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('fxsutility.dll')
def SendToFaxRecipient(sndMode: win32more.Windows.Win32.Devices.Fax.SendToMode, lpFileName: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('STI.dll')
def StiCreateInstanceW(hinst: win32more.Windows.Win32.Foundation.HINSTANCE, dwVer: UInt32, ppSti: POINTER(win32more.Windows.Win32.Devices.Fax.IStillImageW), punkOuter: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
FAXROUTE_ENABLE = Int32
QUERY_STATUS: win32more.Windows.Win32.Devices.Fax.FAXROUTE_ENABLE = -1
STATUS_DISABLE: win32more.Windows.Win32.Devices.Fax.FAXROUTE_ENABLE = 0
STATUS_ENABLE: win32more.Windows.Win32.Devices.Fax.FAXROUTE_ENABLE = 1
FAX_ACCESS_RIGHTS_ENUM = Int32
farSUBMIT_LOW: win32more.Windows.Win32.Devices.Fax.FAX_ACCESS_RIGHTS_ENUM = 1
farSUBMIT_NORMAL: win32more.Windows.Win32.Devices.Fax.FAX_ACCESS_RIGHTS_ENUM = 2
farSUBMIT_HIGH: win32more.Windows.Win32.Devices.Fax.FAX_ACCESS_RIGHTS_ENUM = 4
farQUERY_JOBS: win32more.Windows.Win32.Devices.Fax.FAX_ACCESS_RIGHTS_ENUM = 8
farMANAGE_JOBS: win32more.Windows.Win32.Devices.Fax.FAX_ACCESS_RIGHTS_ENUM = 16
farQUERY_CONFIG: win32more.Windows.Win32.Devices.Fax.FAX_ACCESS_RIGHTS_ENUM = 32
farMANAGE_CONFIG: win32more.Windows.Win32.Devices.Fax.FAX_ACCESS_RIGHTS_ENUM = 64
farQUERY_IN_ARCHIVE: win32more.Windows.Win32.Devices.Fax.FAX_ACCESS_RIGHTS_ENUM = 128
farMANAGE_IN_ARCHIVE: win32more.Windows.Win32.Devices.Fax.FAX_ACCESS_RIGHTS_ENUM = 256
farQUERY_OUT_ARCHIVE: win32more.Windows.Win32.Devices.Fax.FAX_ACCESS_RIGHTS_ENUM = 512
farMANAGE_OUT_ARCHIVE: win32more.Windows.Win32.Devices.Fax.FAX_ACCESS_RIGHTS_ENUM = 1024
FAX_ACCESS_RIGHTS_ENUM_2 = Int32
far2SUBMIT_LOW: win32more.Windows.Win32.Devices.Fax.FAX_ACCESS_RIGHTS_ENUM_2 = 1
far2SUBMIT_NORMAL: win32more.Windows.Win32.Devices.Fax.FAX_ACCESS_RIGHTS_ENUM_2 = 2
far2SUBMIT_HIGH: win32more.Windows.Win32.Devices.Fax.FAX_ACCESS_RIGHTS_ENUM_2 = 4
far2QUERY_OUT_JOBS: win32more.Windows.Win32.Devices.Fax.FAX_ACCESS_RIGHTS_ENUM_2 = 8
far2MANAGE_OUT_JOBS: win32more.Windows.Win32.Devices.Fax.FAX_ACCESS_RIGHTS_ENUM_2 = 16
far2QUERY_CONFIG: win32more.Windows.Win32.Devices.Fax.FAX_ACCESS_RIGHTS_ENUM_2 = 32
far2MANAGE_CONFIG: win32more.Windows.Win32.Devices.Fax.FAX_ACCESS_RIGHTS_ENUM_2 = 64
far2QUERY_ARCHIVES: win32more.Windows.Win32.Devices.Fax.FAX_ACCESS_RIGHTS_ENUM_2 = 128
far2MANAGE_ARCHIVES: win32more.Windows.Win32.Devices.Fax.FAX_ACCESS_RIGHTS_ENUM_2 = 256
far2MANAGE_RECEIVE_FOLDER: win32more.Windows.Win32.Devices.Fax.FAX_ACCESS_RIGHTS_ENUM_2 = 512
FAX_ACCOUNT_EVENTS_TYPE_ENUM = Int32
faetNONE: win32more.Windows.Win32.Devices.Fax.FAX_ACCOUNT_EVENTS_TYPE_ENUM = 0
faetIN_QUEUE: win32more.Windows.Win32.Devices.Fax.FAX_ACCOUNT_EVENTS_TYPE_ENUM = 1
faetOUT_QUEUE: win32more.Windows.Win32.Devices.Fax.FAX_ACCOUNT_EVENTS_TYPE_ENUM = 2
faetIN_ARCHIVE: win32more.Windows.Win32.Devices.Fax.FAX_ACCOUNT_EVENTS_TYPE_ENUM = 4
faetOUT_ARCHIVE: win32more.Windows.Win32.Devices.Fax.FAX_ACCOUNT_EVENTS_TYPE_ENUM = 8
faetFXSSVC_ENDED: win32more.Windows.Win32.Devices.Fax.FAX_ACCOUNT_EVENTS_TYPE_ENUM = 16
class FAX_CONFIGURATIONA(Structure):
    SizeOfStruct: UInt32
    Retries: UInt32
    RetryDelay: UInt32
    DirtyDays: UInt32
    Branding: win32more.Windows.Win32.Foundation.BOOL
    UseDeviceTsid: win32more.Windows.Win32.Foundation.BOOL
    ServerCp: win32more.Windows.Win32.Foundation.BOOL
    PauseServerQueue: win32more.Windows.Win32.Foundation.BOOL
    StartCheapTime: win32more.Windows.Win32.Devices.Fax.FAX_TIME
    StopCheapTime: win32more.Windows.Win32.Devices.Fax.FAX_TIME
    ArchiveOutgoingFaxes: win32more.Windows.Win32.Foundation.BOOL
    ArchiveDirectory: win32more.Windows.Win32.Foundation.PSTR
    Reserved: win32more.Windows.Win32.Foundation.PSTR
class FAX_CONFIGURATIONW(Structure):
    SizeOfStruct: UInt32
    Retries: UInt32
    RetryDelay: UInt32
    DirtyDays: UInt32
    Branding: win32more.Windows.Win32.Foundation.BOOL
    UseDeviceTsid: win32more.Windows.Win32.Foundation.BOOL
    ServerCp: win32more.Windows.Win32.Foundation.BOOL
    PauseServerQueue: win32more.Windows.Win32.Foundation.BOOL
    StartCheapTime: win32more.Windows.Win32.Devices.Fax.FAX_TIME
    StopCheapTime: win32more.Windows.Win32.Devices.Fax.FAX_TIME
    ArchiveOutgoingFaxes: win32more.Windows.Win32.Foundation.BOOL
    ArchiveDirectory: win32more.Windows.Win32.Foundation.PWSTR
    Reserved: win32more.Windows.Win32.Foundation.PWSTR
FAX_CONFIGURATION = UnicodeAlias('FAX_CONFIGURATIONW')
class FAX_CONTEXT_INFOA(Structure):
    SizeOfStruct: UInt32
    hDC: win32more.Windows.Win32.Graphics.Gdi.HDC
    ServerName: win32more.Windows.Win32.Foundation.CHAR * 16
class FAX_CONTEXT_INFOW(Structure):
    SizeOfStruct: UInt32
    hDC: win32more.Windows.Win32.Graphics.Gdi.HDC
    ServerName: Char * 16
FAX_CONTEXT_INFO = UnicodeAlias('FAX_CONTEXT_INFOW')
class FAX_COVERPAGE_INFOA(Structure):
    SizeOfStruct: UInt32
    CoverPageName: win32more.Windows.Win32.Foundation.PSTR
    UseServerCoverPage: win32more.Windows.Win32.Foundation.BOOL
    RecName: win32more.Windows.Win32.Foundation.PSTR
    RecFaxNumber: win32more.Windows.Win32.Foundation.PSTR
    RecCompany: win32more.Windows.Win32.Foundation.PSTR
    RecStreetAddress: win32more.Windows.Win32.Foundation.PSTR
    RecCity: win32more.Windows.Win32.Foundation.PSTR
    RecState: win32more.Windows.Win32.Foundation.PSTR
    RecZip: win32more.Windows.Win32.Foundation.PSTR
    RecCountry: win32more.Windows.Win32.Foundation.PSTR
    RecTitle: win32more.Windows.Win32.Foundation.PSTR
    RecDepartment: win32more.Windows.Win32.Foundation.PSTR
    RecOfficeLocation: win32more.Windows.Win32.Foundation.PSTR
    RecHomePhone: win32more.Windows.Win32.Foundation.PSTR
    RecOfficePhone: win32more.Windows.Win32.Foundation.PSTR
    SdrName: win32more.Windows.Win32.Foundation.PSTR
    SdrFaxNumber: win32more.Windows.Win32.Foundation.PSTR
    SdrCompany: win32more.Windows.Win32.Foundation.PSTR
    SdrAddress: win32more.Windows.Win32.Foundation.PSTR
    SdrTitle: win32more.Windows.Win32.Foundation.PSTR
    SdrDepartment: win32more.Windows.Win32.Foundation.PSTR
    SdrOfficeLocation: win32more.Windows.Win32.Foundation.PSTR
    SdrHomePhone: win32more.Windows.Win32.Foundation.PSTR
    SdrOfficePhone: win32more.Windows.Win32.Foundation.PSTR
    Note: win32more.Windows.Win32.Foundation.PSTR
    Subject: win32more.Windows.Win32.Foundation.PSTR
    TimeSent: win32more.Windows.Win32.Foundation.SYSTEMTIME
    PageCount: UInt32
class FAX_COVERPAGE_INFOW(Structure):
    SizeOfStruct: UInt32
    CoverPageName: win32more.Windows.Win32.Foundation.PWSTR
    UseServerCoverPage: win32more.Windows.Win32.Foundation.BOOL
    RecName: win32more.Windows.Win32.Foundation.PWSTR
    RecFaxNumber: win32more.Windows.Win32.Foundation.PWSTR
    RecCompany: win32more.Windows.Win32.Foundation.PWSTR
    RecStreetAddress: win32more.Windows.Win32.Foundation.PWSTR
    RecCity: win32more.Windows.Win32.Foundation.PWSTR
    RecState: win32more.Windows.Win32.Foundation.PWSTR
    RecZip: win32more.Windows.Win32.Foundation.PWSTR
    RecCountry: win32more.Windows.Win32.Foundation.PWSTR
    RecTitle: win32more.Windows.Win32.Foundation.PWSTR
    RecDepartment: win32more.Windows.Win32.Foundation.PWSTR
    RecOfficeLocation: win32more.Windows.Win32.Foundation.PWSTR
    RecHomePhone: win32more.Windows.Win32.Foundation.PWSTR
    RecOfficePhone: win32more.Windows.Win32.Foundation.PWSTR
    SdrName: win32more.Windows.Win32.Foundation.PWSTR
    SdrFaxNumber: win32more.Windows.Win32.Foundation.PWSTR
    SdrCompany: win32more.Windows.Win32.Foundation.PWSTR
    SdrAddress: win32more.Windows.Win32.Foundation.PWSTR
    SdrTitle: win32more.Windows.Win32.Foundation.PWSTR
    SdrDepartment: win32more.Windows.Win32.Foundation.PWSTR
    SdrOfficeLocation: win32more.Windows.Win32.Foundation.PWSTR
    SdrHomePhone: win32more.Windows.Win32.Foundation.PWSTR
    SdrOfficePhone: win32more.Windows.Win32.Foundation.PWSTR
    Note: win32more.Windows.Win32.Foundation.PWSTR
    Subject: win32more.Windows.Win32.Foundation.PWSTR
    TimeSent: win32more.Windows.Win32.Foundation.SYSTEMTIME
    PageCount: UInt32
FAX_COVERPAGE_INFO = UnicodeAlias('FAX_COVERPAGE_INFOW')
FAX_COVERPAGE_TYPE_ENUM = Int32
fcptNONE: win32more.Windows.Win32.Devices.Fax.FAX_COVERPAGE_TYPE_ENUM = 0
fcptLOCAL: win32more.Windows.Win32.Devices.Fax.FAX_COVERPAGE_TYPE_ENUM = 1
fcptSERVER: win32more.Windows.Win32.Devices.Fax.FAX_COVERPAGE_TYPE_ENUM = 2
FAX_DEVICE_RECEIVE_MODE_ENUM = Int32
fdrmNO_ANSWER: win32more.Windows.Win32.Devices.Fax.FAX_DEVICE_RECEIVE_MODE_ENUM = 0
fdrmAUTO_ANSWER: win32more.Windows.Win32.Devices.Fax.FAX_DEVICE_RECEIVE_MODE_ENUM = 1
fdrmMANUAL_ANSWER: win32more.Windows.Win32.Devices.Fax.FAX_DEVICE_RECEIVE_MODE_ENUM = 2
class FAX_DEVICE_STATUSA(Structure):
    SizeOfStruct: UInt32
    CallerId: win32more.Windows.Win32.Foundation.PSTR
    Csid: win32more.Windows.Win32.Foundation.PSTR
    CurrentPage: UInt32
    DeviceId: UInt32
    DeviceName: win32more.Windows.Win32.Foundation.PSTR
    DocumentName: win32more.Windows.Win32.Foundation.PSTR
    JobType: UInt32
    PhoneNumber: win32more.Windows.Win32.Foundation.PSTR
    RoutingString: win32more.Windows.Win32.Foundation.PSTR
    SenderName: win32more.Windows.Win32.Foundation.PSTR
    RecipientName: win32more.Windows.Win32.Foundation.PSTR
    Size: UInt32
    StartTime: win32more.Windows.Win32.Foundation.FILETIME
    Status: UInt32
    StatusString: win32more.Windows.Win32.Foundation.PSTR
    SubmittedTime: win32more.Windows.Win32.Foundation.FILETIME
    TotalPages: UInt32
    Tsid: win32more.Windows.Win32.Foundation.PSTR
    UserName: win32more.Windows.Win32.Foundation.PSTR
class FAX_DEVICE_STATUSW(Structure):
    SizeOfStruct: UInt32
    CallerId: win32more.Windows.Win32.Foundation.PWSTR
    Csid: win32more.Windows.Win32.Foundation.PWSTR
    CurrentPage: UInt32
    DeviceId: UInt32
    DeviceName: win32more.Windows.Win32.Foundation.PWSTR
    DocumentName: win32more.Windows.Win32.Foundation.PWSTR
    JobType: UInt32
    PhoneNumber: win32more.Windows.Win32.Foundation.PWSTR
    RoutingString: win32more.Windows.Win32.Foundation.PWSTR
    SenderName: win32more.Windows.Win32.Foundation.PWSTR
    RecipientName: win32more.Windows.Win32.Foundation.PWSTR
    Size: UInt32
    StartTime: win32more.Windows.Win32.Foundation.FILETIME
    Status: UInt32
    StatusString: win32more.Windows.Win32.Foundation.PWSTR
    SubmittedTime: win32more.Windows.Win32.Foundation.FILETIME
    TotalPages: UInt32
    Tsid: win32more.Windows.Win32.Foundation.PWSTR
    UserName: win32more.Windows.Win32.Foundation.PWSTR
FAX_DEVICE_STATUS = UnicodeAlias('FAX_DEVICE_STATUSW')
class FAX_DEV_STATUS(Structure):
    SizeOfStruct: UInt32
    StatusId: UInt32
    StringId: UInt32
    PageCount: UInt32
    CSI: win32more.Windows.Win32.Foundation.PWSTR
    CallerId: win32more.Windows.Win32.Foundation.PWSTR
    RoutingInfo: win32more.Windows.Win32.Foundation.PWSTR
    ErrorCode: UInt32
    Reserved: UInt32 * 3
FAX_ENUM_DELIVERY_REPORT_TYPES = Int32
DRT_NONE: win32more.Windows.Win32.Devices.Fax.FAX_ENUM_DELIVERY_REPORT_TYPES = 0
DRT_EMAIL: win32more.Windows.Win32.Devices.Fax.FAX_ENUM_DELIVERY_REPORT_TYPES = 1
DRT_INBOX: win32more.Windows.Win32.Devices.Fax.FAX_ENUM_DELIVERY_REPORT_TYPES = 2
FAX_ENUM_DEVICE_ID_SOURCE = Int32
DEV_ID_SRC_FAX: win32more.Windows.Win32.Devices.Fax.FAX_ENUM_DEVICE_ID_SOURCE = 0
DEV_ID_SRC_TAPI: win32more.Windows.Win32.Devices.Fax.FAX_ENUM_DEVICE_ID_SOURCE = 1
FAX_ENUM_JOB_COMMANDS = Int32
JC_UNKNOWN: win32more.Windows.Win32.Devices.Fax.FAX_ENUM_JOB_COMMANDS = 0
JC_DELETE: win32more.Windows.Win32.Devices.Fax.FAX_ENUM_JOB_COMMANDS = 1
JC_PAUSE: win32more.Windows.Win32.Devices.Fax.FAX_ENUM_JOB_COMMANDS = 2
JC_RESUME: win32more.Windows.Win32.Devices.Fax.FAX_ENUM_JOB_COMMANDS = 3
FAX_ENUM_JOB_SEND_ATTRIBUTES = Int32
JSA_NOW: win32more.Windows.Win32.Devices.Fax.FAX_ENUM_JOB_SEND_ATTRIBUTES = 0
JSA_SPECIFIC_TIME: win32more.Windows.Win32.Devices.Fax.FAX_ENUM_JOB_SEND_ATTRIBUTES = 1
JSA_DISCOUNT_PERIOD: win32more.Windows.Win32.Devices.Fax.FAX_ENUM_JOB_SEND_ATTRIBUTES = 2
FAX_ENUM_LOG_CATEGORIES = Int32
FAXLOG_CATEGORY_INIT: win32more.Windows.Win32.Devices.Fax.FAX_ENUM_LOG_CATEGORIES = 1
FAXLOG_CATEGORY_OUTBOUND: win32more.Windows.Win32.Devices.Fax.FAX_ENUM_LOG_CATEGORIES = 2
FAXLOG_CATEGORY_INBOUND: win32more.Windows.Win32.Devices.Fax.FAX_ENUM_LOG_CATEGORIES = 3
FAXLOG_CATEGORY_UNKNOWN: win32more.Windows.Win32.Devices.Fax.FAX_ENUM_LOG_CATEGORIES = 4
FAX_ENUM_LOG_LEVELS = Int32
FAXLOG_LEVEL_NONE: win32more.Windows.Win32.Devices.Fax.FAX_ENUM_LOG_LEVELS = 0
FAXLOG_LEVEL_MIN: win32more.Windows.Win32.Devices.Fax.FAX_ENUM_LOG_LEVELS = 1
FAXLOG_LEVEL_MED: win32more.Windows.Win32.Devices.Fax.FAX_ENUM_LOG_LEVELS = 2
FAXLOG_LEVEL_MAX: win32more.Windows.Win32.Devices.Fax.FAX_ENUM_LOG_LEVELS = 3
FAX_ENUM_PORT_OPEN_TYPE = Int32
PORT_OPEN_QUERY: win32more.Windows.Win32.Devices.Fax.FAX_ENUM_PORT_OPEN_TYPE = 1
PORT_OPEN_MODIFY: win32more.Windows.Win32.Devices.Fax.FAX_ENUM_PORT_OPEN_TYPE = 2
class FAX_EVENTA(Structure):
    SizeOfStruct: UInt32
    TimeStamp: win32more.Windows.Win32.Foundation.FILETIME
    DeviceId: UInt32
    EventId: UInt32
    JobId: UInt32
class FAX_EVENTW(Structure):
    SizeOfStruct: UInt32
    TimeStamp: win32more.Windows.Win32.Foundation.FILETIME
    DeviceId: UInt32
    EventId: UInt32
    JobId: UInt32
FAX_EVENT = UnicodeAlias('FAX_EVENTW')
class FAX_GLOBAL_ROUTING_INFOA(Structure):
    SizeOfStruct: UInt32
    Priority: UInt32
    Guid: win32more.Windows.Win32.Foundation.PSTR
    FriendlyName: win32more.Windows.Win32.Foundation.PSTR
    FunctionName: win32more.Windows.Win32.Foundation.PSTR
    ExtensionImageName: win32more.Windows.Win32.Foundation.PSTR
    ExtensionFriendlyName: win32more.Windows.Win32.Foundation.PSTR
class FAX_GLOBAL_ROUTING_INFOW(Structure):
    SizeOfStruct: UInt32
    Priority: UInt32
    Guid: win32more.Windows.Win32.Foundation.PWSTR
    FriendlyName: win32more.Windows.Win32.Foundation.PWSTR
    FunctionName: win32more.Windows.Win32.Foundation.PWSTR
    ExtensionImageName: win32more.Windows.Win32.Foundation.PWSTR
    ExtensionFriendlyName: win32more.Windows.Win32.Foundation.PWSTR
FAX_GLOBAL_ROUTING_INFO = UnicodeAlias('FAX_GLOBAL_ROUTING_INFOW')
FAX_GROUP_STATUS_ENUM = Int32
fgsALL_DEV_VALID: win32more.Windows.Win32.Devices.Fax.FAX_GROUP_STATUS_ENUM = 0
fgsEMPTY: win32more.Windows.Win32.Devices.Fax.FAX_GROUP_STATUS_ENUM = 1
fgsALL_DEV_NOT_VALID: win32more.Windows.Win32.Devices.Fax.FAX_GROUP_STATUS_ENUM = 2
fgsSOME_DEV_NOT_VALID: win32more.Windows.Win32.Devices.Fax.FAX_GROUP_STATUS_ENUM = 3
class FAX_JOB_ENTRYA(Structure):
    SizeOfStruct: UInt32
    JobId: UInt32
    UserName: win32more.Windows.Win32.Foundation.PSTR
    JobType: UInt32
    QueueStatus: UInt32
    Status: UInt32
    Size: UInt32
    PageCount: UInt32
    RecipientNumber: win32more.Windows.Win32.Foundation.PSTR
    RecipientName: win32more.Windows.Win32.Foundation.PSTR
    Tsid: win32more.Windows.Win32.Foundation.PSTR
    SenderName: win32more.Windows.Win32.Foundation.PSTR
    SenderCompany: win32more.Windows.Win32.Foundation.PSTR
    SenderDept: win32more.Windows.Win32.Foundation.PSTR
    BillingCode: win32more.Windows.Win32.Foundation.PSTR
    ScheduleAction: UInt32
    ScheduleTime: win32more.Windows.Win32.Foundation.SYSTEMTIME
    DeliveryReportType: UInt32
    DeliveryReportAddress: win32more.Windows.Win32.Foundation.PSTR
    DocumentName: win32more.Windows.Win32.Foundation.PSTR
class FAX_JOB_ENTRYW(Structure):
    SizeOfStruct: UInt32
    JobId: UInt32
    UserName: win32more.Windows.Win32.Foundation.PWSTR
    JobType: UInt32
    QueueStatus: UInt32
    Status: UInt32
    Size: UInt32
    PageCount: UInt32
    RecipientNumber: win32more.Windows.Win32.Foundation.PWSTR
    RecipientName: win32more.Windows.Win32.Foundation.PWSTR
    Tsid: win32more.Windows.Win32.Foundation.PWSTR
    SenderName: win32more.Windows.Win32.Foundation.PWSTR
    SenderCompany: win32more.Windows.Win32.Foundation.PWSTR
    SenderDept: win32more.Windows.Win32.Foundation.PWSTR
    BillingCode: win32more.Windows.Win32.Foundation.PWSTR
    ScheduleAction: UInt32
    ScheduleTime: win32more.Windows.Win32.Foundation.SYSTEMTIME
    DeliveryReportType: UInt32
    DeliveryReportAddress: win32more.Windows.Win32.Foundation.PWSTR
    DocumentName: win32more.Windows.Win32.Foundation.PWSTR
FAX_JOB_ENTRY = UnicodeAlias('FAX_JOB_ENTRYW')
FAX_JOB_EXTENDED_STATUS_ENUM = Int32
fjesNONE: win32more.Windows.Win32.Devices.Fax.FAX_JOB_EXTENDED_STATUS_ENUM = 0
fjesDISCONNECTED: win32more.Windows.Win32.Devices.Fax.FAX_JOB_EXTENDED_STATUS_ENUM = 1
fjesINITIALIZING: win32more.Windows.Win32.Devices.Fax.FAX_JOB_EXTENDED_STATUS_ENUM = 2
fjesDIALING: win32more.Windows.Win32.Devices.Fax.FAX_JOB_EXTENDED_STATUS_ENUM = 3
fjesTRANSMITTING: win32more.Windows.Win32.Devices.Fax.FAX_JOB_EXTENDED_STATUS_ENUM = 4
fjesANSWERED: win32more.Windows.Win32.Devices.Fax.FAX_JOB_EXTENDED_STATUS_ENUM = 5
fjesRECEIVING: win32more.Windows.Win32.Devices.Fax.FAX_JOB_EXTENDED_STATUS_ENUM = 6
fjesLINE_UNAVAILABLE: win32more.Windows.Win32.Devices.Fax.FAX_JOB_EXTENDED_STATUS_ENUM = 7
fjesBUSY: win32more.Windows.Win32.Devices.Fax.FAX_JOB_EXTENDED_STATUS_ENUM = 8
fjesNO_ANSWER: win32more.Windows.Win32.Devices.Fax.FAX_JOB_EXTENDED_STATUS_ENUM = 9
fjesBAD_ADDRESS: win32more.Windows.Win32.Devices.Fax.FAX_JOB_EXTENDED_STATUS_ENUM = 10
fjesNO_DIAL_TONE: win32more.Windows.Win32.Devices.Fax.FAX_JOB_EXTENDED_STATUS_ENUM = 11
fjesFATAL_ERROR: win32more.Windows.Win32.Devices.Fax.FAX_JOB_EXTENDED_STATUS_ENUM = 12
fjesCALL_DELAYED: win32more.Windows.Win32.Devices.Fax.FAX_JOB_EXTENDED_STATUS_ENUM = 13
fjesCALL_BLACKLISTED: win32more.Windows.Win32.Devices.Fax.FAX_JOB_EXTENDED_STATUS_ENUM = 14
fjesNOT_FAX_CALL: win32more.Windows.Win32.Devices.Fax.FAX_JOB_EXTENDED_STATUS_ENUM = 15
fjesPARTIALLY_RECEIVED: win32more.Windows.Win32.Devices.Fax.FAX_JOB_EXTENDED_STATUS_ENUM = 16
fjesHANDLED: win32more.Windows.Win32.Devices.Fax.FAX_JOB_EXTENDED_STATUS_ENUM = 17
fjesCALL_COMPLETED: win32more.Windows.Win32.Devices.Fax.FAX_JOB_EXTENDED_STATUS_ENUM = 18
fjesCALL_ABORTED: win32more.Windows.Win32.Devices.Fax.FAX_JOB_EXTENDED_STATUS_ENUM = 19
fjesPROPRIETARY: win32more.Windows.Win32.Devices.Fax.FAX_JOB_EXTENDED_STATUS_ENUM = 16777216
FAX_JOB_OPERATIONS_ENUM = Int32
fjoVIEW: win32more.Windows.Win32.Devices.Fax.FAX_JOB_OPERATIONS_ENUM = 1
fjoPAUSE: win32more.Windows.Win32.Devices.Fax.FAX_JOB_OPERATIONS_ENUM = 2
fjoRESUME: win32more.Windows.Win32.Devices.Fax.FAX_JOB_OPERATIONS_ENUM = 4
fjoRESTART: win32more.Windows.Win32.Devices.Fax.FAX_JOB_OPERATIONS_ENUM = 8
fjoDELETE: win32more.Windows.Win32.Devices.Fax.FAX_JOB_OPERATIONS_ENUM = 16
fjoRECIPIENT_INFO: win32more.Windows.Win32.Devices.Fax.FAX_JOB_OPERATIONS_ENUM = 32
fjoSENDER_INFO: win32more.Windows.Win32.Devices.Fax.FAX_JOB_OPERATIONS_ENUM = 64
class FAX_JOB_PARAMA(Structure):
    SizeOfStruct: UInt32
    RecipientNumber: win32more.Windows.Win32.Foundation.PSTR
    RecipientName: win32more.Windows.Win32.Foundation.PSTR
    Tsid: win32more.Windows.Win32.Foundation.PSTR
    SenderName: win32more.Windows.Win32.Foundation.PSTR
    SenderCompany: win32more.Windows.Win32.Foundation.PSTR
    SenderDept: win32more.Windows.Win32.Foundation.PSTR
    BillingCode: win32more.Windows.Win32.Foundation.PSTR
    ScheduleAction: UInt32
    ScheduleTime: win32more.Windows.Win32.Foundation.SYSTEMTIME
    DeliveryReportType: UInt32
    DeliveryReportAddress: win32more.Windows.Win32.Foundation.PSTR
    DocumentName: win32more.Windows.Win32.Foundation.PSTR
    CallHandle: UInt32
    Reserved: UIntPtr * 3
class FAX_JOB_PARAMW(Structure):
    SizeOfStruct: UInt32
    RecipientNumber: win32more.Windows.Win32.Foundation.PWSTR
    RecipientName: win32more.Windows.Win32.Foundation.PWSTR
    Tsid: win32more.Windows.Win32.Foundation.PWSTR
    SenderName: win32more.Windows.Win32.Foundation.PWSTR
    SenderCompany: win32more.Windows.Win32.Foundation.PWSTR
    SenderDept: win32more.Windows.Win32.Foundation.PWSTR
    BillingCode: win32more.Windows.Win32.Foundation.PWSTR
    ScheduleAction: UInt32
    ScheduleTime: win32more.Windows.Win32.Foundation.SYSTEMTIME
    DeliveryReportType: UInt32
    DeliveryReportAddress: win32more.Windows.Win32.Foundation.PWSTR
    DocumentName: win32more.Windows.Win32.Foundation.PWSTR
    CallHandle: UInt32
    Reserved: UIntPtr * 3
FAX_JOB_PARAM = UnicodeAlias('FAX_JOB_PARAMW')
FAX_JOB_STATUS_ENUM = Int32
fjsPENDING: win32more.Windows.Win32.Devices.Fax.FAX_JOB_STATUS_ENUM = 1
fjsINPROGRESS: win32more.Windows.Win32.Devices.Fax.FAX_JOB_STATUS_ENUM = 2
fjsFAILED: win32more.Windows.Win32.Devices.Fax.FAX_JOB_STATUS_ENUM = 8
fjsPAUSED: win32more.Windows.Win32.Devices.Fax.FAX_JOB_STATUS_ENUM = 16
fjsNOLINE: win32more.Windows.Win32.Devices.Fax.FAX_JOB_STATUS_ENUM = 32
fjsRETRYING: win32more.Windows.Win32.Devices.Fax.FAX_JOB_STATUS_ENUM = 64
fjsRETRIES_EXCEEDED: win32more.Windows.Win32.Devices.Fax.FAX_JOB_STATUS_ENUM = 128
fjsCOMPLETED: win32more.Windows.Win32.Devices.Fax.FAX_JOB_STATUS_ENUM = 256
fjsCANCELED: win32more.Windows.Win32.Devices.Fax.FAX_JOB_STATUS_ENUM = 512
fjsCANCELING: win32more.Windows.Win32.Devices.Fax.FAX_JOB_STATUS_ENUM = 1024
fjsROUTING: win32more.Windows.Win32.Devices.Fax.FAX_JOB_STATUS_ENUM = 2048
FAX_JOB_TYPE_ENUM = Int32
fjtSEND: win32more.Windows.Win32.Devices.Fax.FAX_JOB_TYPE_ENUM = 0
fjtRECEIVE: win32more.Windows.Win32.Devices.Fax.FAX_JOB_TYPE_ENUM = 1
fjtROUTING: win32more.Windows.Win32.Devices.Fax.FAX_JOB_TYPE_ENUM = 2
class FAX_LOG_CATEGORYA(Structure):
    Name: win32more.Windows.Win32.Foundation.PSTR
    Category: UInt32
    Level: UInt32
class FAX_LOG_CATEGORYW(Structure):
    Name: win32more.Windows.Win32.Foundation.PWSTR
    Category: UInt32
    Level: UInt32
FAX_LOG_CATEGORY = UnicodeAlias('FAX_LOG_CATEGORYW')
FAX_LOG_LEVEL_ENUM = Int32
fllNONE: win32more.Windows.Win32.Devices.Fax.FAX_LOG_LEVEL_ENUM = 0
fllMIN: win32more.Windows.Win32.Devices.Fax.FAX_LOG_LEVEL_ENUM = 1
fllMED: win32more.Windows.Win32.Devices.Fax.FAX_LOG_LEVEL_ENUM = 2
fllMAX: win32more.Windows.Win32.Devices.Fax.FAX_LOG_LEVEL_ENUM = 3
class FAX_PORT_INFOA(Structure):
    SizeOfStruct: UInt32
    DeviceId: UInt32
    State: UInt32
    Flags: UInt32
    Rings: UInt32
    Priority: UInt32
    DeviceName: win32more.Windows.Win32.Foundation.PSTR
    Tsid: win32more.Windows.Win32.Foundation.PSTR
    Csid: win32more.Windows.Win32.Foundation.PSTR
class FAX_PORT_INFOW(Structure):
    SizeOfStruct: UInt32
    DeviceId: UInt32
    State: UInt32
    Flags: UInt32
    Rings: UInt32
    Priority: UInt32
    DeviceName: win32more.Windows.Win32.Foundation.PWSTR
    Tsid: win32more.Windows.Win32.Foundation.PWSTR
    Csid: win32more.Windows.Win32.Foundation.PWSTR
FAX_PORT_INFO = UnicodeAlias('FAX_PORT_INFOW')
class FAX_PRINT_INFOA(Structure):
    SizeOfStruct: UInt32
    DocName: win32more.Windows.Win32.Foundation.PSTR
    RecipientName: win32more.Windows.Win32.Foundation.PSTR
    RecipientNumber: win32more.Windows.Win32.Foundation.PSTR
    SenderName: win32more.Windows.Win32.Foundation.PSTR
    SenderCompany: win32more.Windows.Win32.Foundation.PSTR
    SenderDept: win32more.Windows.Win32.Foundation.PSTR
    SenderBillingCode: win32more.Windows.Win32.Foundation.PSTR
    Reserved: win32more.Windows.Win32.Foundation.PSTR
    DrEmailAddress: win32more.Windows.Win32.Foundation.PSTR
    OutputFileName: win32more.Windows.Win32.Foundation.PSTR
class FAX_PRINT_INFOW(Structure):
    SizeOfStruct: UInt32
    DocName: win32more.Windows.Win32.Foundation.PWSTR
    RecipientName: win32more.Windows.Win32.Foundation.PWSTR
    RecipientNumber: win32more.Windows.Win32.Foundation.PWSTR
    SenderName: win32more.Windows.Win32.Foundation.PWSTR
    SenderCompany: win32more.Windows.Win32.Foundation.PWSTR
    SenderDept: win32more.Windows.Win32.Foundation.PWSTR
    SenderBillingCode: win32more.Windows.Win32.Foundation.PWSTR
    Reserved: win32more.Windows.Win32.Foundation.PWSTR
    DrEmailAddress: win32more.Windows.Win32.Foundation.PWSTR
    OutputFileName: win32more.Windows.Win32.Foundation.PWSTR
FAX_PRINT_INFO = UnicodeAlias('FAX_PRINT_INFOW')
FAX_PRIORITY_TYPE_ENUM = Int32
fptLOW: win32more.Windows.Win32.Devices.Fax.FAX_PRIORITY_TYPE_ENUM = 0
fptNORMAL: win32more.Windows.Win32.Devices.Fax.FAX_PRIORITY_TYPE_ENUM = 1
fptHIGH: win32more.Windows.Win32.Devices.Fax.FAX_PRIORITY_TYPE_ENUM = 2
FAX_PROVIDER_STATUS_ENUM = Int32
fpsSUCCESS: win32more.Windows.Win32.Devices.Fax.FAX_PROVIDER_STATUS_ENUM = 0
fpsSERVER_ERROR: win32more.Windows.Win32.Devices.Fax.FAX_PROVIDER_STATUS_ENUM = 1
fpsBAD_GUID: win32more.Windows.Win32.Devices.Fax.FAX_PROVIDER_STATUS_ENUM = 2
fpsBAD_VERSION: win32more.Windows.Win32.Devices.Fax.FAX_PROVIDER_STATUS_ENUM = 3
fpsCANT_LOAD: win32more.Windows.Win32.Devices.Fax.FAX_PROVIDER_STATUS_ENUM = 4
fpsCANT_LINK: win32more.Windows.Win32.Devices.Fax.FAX_PROVIDER_STATUS_ENUM = 5
fpsCANT_INIT: win32more.Windows.Win32.Devices.Fax.FAX_PROVIDER_STATUS_ENUM = 6
FAX_RECEIPT_TYPE_ENUM = Int32
frtNONE: win32more.Windows.Win32.Devices.Fax.FAX_RECEIPT_TYPE_ENUM = 0
frtMAIL: win32more.Windows.Win32.Devices.Fax.FAX_RECEIPT_TYPE_ENUM = 1
frtMSGBOX: win32more.Windows.Win32.Devices.Fax.FAX_RECEIPT_TYPE_ENUM = 4
class FAX_RECEIVE(Structure):
    SizeOfStruct: UInt32
    FileName: win32more.Windows.Win32.Foundation.PWSTR
    ReceiverName: win32more.Windows.Win32.Foundation.PWSTR
    ReceiverNumber: win32more.Windows.Win32.Foundation.PWSTR
    Reserved: UInt32 * 4
class FAX_ROUTE(Structure):
    SizeOfStruct: UInt32
    JobId: UInt32
    ElapsedTime: UInt64
    ReceiveTime: UInt64
    PageCount: UInt32
    Csid: win32more.Windows.Win32.Foundation.PWSTR
    Tsid: win32more.Windows.Win32.Foundation.PWSTR
    CallerId: win32more.Windows.Win32.Foundation.PWSTR
    RoutingInfo: win32more.Windows.Win32.Foundation.PWSTR
    ReceiverName: win32more.Windows.Win32.Foundation.PWSTR
    ReceiverNumber: win32more.Windows.Win32.Foundation.PWSTR
    DeviceName: win32more.Windows.Win32.Foundation.PWSTR
    DeviceId: UInt32
    RoutingInfoData: POINTER(Byte)
    RoutingInfoDataSize: UInt32
class FAX_ROUTE_CALLBACKROUTINES(Structure):
    SizeOfStruct: UInt32
    FaxRouteAddFile: win32more.Windows.Win32.Devices.Fax.PFAXROUTEADDFILE
    FaxRouteDeleteFile: win32more.Windows.Win32.Devices.Fax.PFAXROUTEDELETEFILE
    FaxRouteGetFile: win32more.Windows.Win32.Devices.Fax.PFAXROUTEGETFILE
    FaxRouteEnumFiles: win32more.Windows.Win32.Devices.Fax.PFAXROUTEENUMFILES
    FaxRouteModifyRoutingData: win32more.Windows.Win32.Devices.Fax.PFAXROUTEMODIFYROUTINGDATA
class FAX_ROUTING_METHODA(Structure):
    SizeOfStruct: UInt32
    DeviceId: UInt32
    Enabled: win32more.Windows.Win32.Foundation.BOOL
    DeviceName: win32more.Windows.Win32.Foundation.PSTR
    Guid: win32more.Windows.Win32.Foundation.PSTR
    FriendlyName: win32more.Windows.Win32.Foundation.PSTR
    FunctionName: win32more.Windows.Win32.Foundation.PSTR
    ExtensionImageName: win32more.Windows.Win32.Foundation.PSTR
    ExtensionFriendlyName: win32more.Windows.Win32.Foundation.PSTR
class FAX_ROUTING_METHODW(Structure):
    SizeOfStruct: UInt32
    DeviceId: UInt32
    Enabled: win32more.Windows.Win32.Foundation.BOOL
    DeviceName: win32more.Windows.Win32.Foundation.PWSTR
    Guid: win32more.Windows.Win32.Foundation.PWSTR
    FriendlyName: win32more.Windows.Win32.Foundation.PWSTR
    FunctionName: win32more.Windows.Win32.Foundation.PWSTR
    ExtensionImageName: win32more.Windows.Win32.Foundation.PWSTR
    ExtensionFriendlyName: win32more.Windows.Win32.Foundation.PWSTR
FAX_ROUTING_METHOD = UnicodeAlias('FAX_ROUTING_METHODW')
FAX_ROUTING_RULE_CODE_ENUM = Int32
frrcANY_CODE: win32more.Windows.Win32.Devices.Fax.FAX_ROUTING_RULE_CODE_ENUM = 0
FAX_RULE_STATUS_ENUM = Int32
frsVALID: win32more.Windows.Win32.Devices.Fax.FAX_RULE_STATUS_ENUM = 0
frsEMPTY_GROUP: win32more.Windows.Win32.Devices.Fax.FAX_RULE_STATUS_ENUM = 1
frsALL_GROUP_DEV_NOT_VALID: win32more.Windows.Win32.Devices.Fax.FAX_RULE_STATUS_ENUM = 2
frsSOME_GROUP_DEV_NOT_VALID: win32more.Windows.Win32.Devices.Fax.FAX_RULE_STATUS_ENUM = 3
frsBAD_DEVICE: win32more.Windows.Win32.Devices.Fax.FAX_RULE_STATUS_ENUM = 4
FAX_SCHEDULE_TYPE_ENUM = Int32
fstNOW: win32more.Windows.Win32.Devices.Fax.FAX_SCHEDULE_TYPE_ENUM = 0
fstSPECIFIC_TIME: win32more.Windows.Win32.Devices.Fax.FAX_SCHEDULE_TYPE_ENUM = 1
fstDISCOUNT_PERIOD: win32more.Windows.Win32.Devices.Fax.FAX_SCHEDULE_TYPE_ENUM = 2
class FAX_SEND(Structure):
    SizeOfStruct: UInt32
    FileName: win32more.Windows.Win32.Foundation.PWSTR
    CallerName: win32more.Windows.Win32.Foundation.PWSTR
    CallerNumber: win32more.Windows.Win32.Foundation.PWSTR
    ReceiverName: win32more.Windows.Win32.Foundation.PWSTR
    ReceiverNumber: win32more.Windows.Win32.Foundation.PWSTR
    Branding: win32more.Windows.Win32.Foundation.BOOL
    CallHandle: UInt32
    Reserved: UInt32 * 3
FAX_SERVER_APIVERSION_ENUM = Int32
fsAPI_VERSION_0: win32more.Windows.Win32.Devices.Fax.FAX_SERVER_APIVERSION_ENUM = 0
fsAPI_VERSION_1: win32more.Windows.Win32.Devices.Fax.FAX_SERVER_APIVERSION_ENUM = 65536
fsAPI_VERSION_2: win32more.Windows.Win32.Devices.Fax.FAX_SERVER_APIVERSION_ENUM = 131072
fsAPI_VERSION_3: win32more.Windows.Win32.Devices.Fax.FAX_SERVER_APIVERSION_ENUM = 196608
FAX_SERVER_EVENTS_TYPE_ENUM = Int32
fsetNONE: win32more.Windows.Win32.Devices.Fax.FAX_SERVER_EVENTS_TYPE_ENUM = 0
fsetIN_QUEUE: win32more.Windows.Win32.Devices.Fax.FAX_SERVER_EVENTS_TYPE_ENUM = 1
fsetOUT_QUEUE: win32more.Windows.Win32.Devices.Fax.FAX_SERVER_EVENTS_TYPE_ENUM = 2
fsetCONFIG: win32more.Windows.Win32.Devices.Fax.FAX_SERVER_EVENTS_TYPE_ENUM = 4
fsetACTIVITY: win32more.Windows.Win32.Devices.Fax.FAX_SERVER_EVENTS_TYPE_ENUM = 8
fsetQUEUE_STATE: win32more.Windows.Win32.Devices.Fax.FAX_SERVER_EVENTS_TYPE_ENUM = 16
fsetIN_ARCHIVE: win32more.Windows.Win32.Devices.Fax.FAX_SERVER_EVENTS_TYPE_ENUM = 32
fsetOUT_ARCHIVE: win32more.Windows.Win32.Devices.Fax.FAX_SERVER_EVENTS_TYPE_ENUM = 64
fsetFXSSVC_ENDED: win32more.Windows.Win32.Devices.Fax.FAX_SERVER_EVENTS_TYPE_ENUM = 128
fsetDEVICE_STATUS: win32more.Windows.Win32.Devices.Fax.FAX_SERVER_EVENTS_TYPE_ENUM = 256
fsetINCOMING_CALL: win32more.Windows.Win32.Devices.Fax.FAX_SERVER_EVENTS_TYPE_ENUM = 512
FAX_SMTP_AUTHENTICATION_TYPE_ENUM = Int32
fsatANONYMOUS: win32more.Windows.Win32.Devices.Fax.FAX_SMTP_AUTHENTICATION_TYPE_ENUM = 0
fsatBASIC: win32more.Windows.Win32.Devices.Fax.FAX_SMTP_AUTHENTICATION_TYPE_ENUM = 1
fsatNTLM: win32more.Windows.Win32.Devices.Fax.FAX_SMTP_AUTHENTICATION_TYPE_ENUM = 2
class FAX_TIME(Structure):
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
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{68535b33-5dc4-4086-be26-b76f9b711006}')
    @commethod(7)
    def get_AccountName(self, pbstrAccountName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Folders(self, ppFolders: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxAccountFolders)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ListenToAccountEvents(self, EventTypes: win32more.Windows.Win32.Devices.Fax.FAX_ACCOUNT_EVENTS_TYPE_ENUM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_RegisteredEvents(self, pRegisteredEvents: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_ACCOUNT_EVENTS_TYPE_ENUM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxAccountFolders(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{6463f89d-23d8-46a9-8f86-c47b77ca7926}')
    @commethod(7)
    def get_OutgoingQueue(self, pFaxOutgoingQueue: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxAccountOutgoingQueue)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_IncomingQueue(self, pFaxIncomingQueue: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxAccountIncomingQueue)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_IncomingArchive(self, pFaxIncomingArchive: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxAccountIncomingArchive)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_OutgoingArchive(self, pFaxOutgoingArchive: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxAccountOutgoingArchive)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxAccountIncomingArchive(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{a8a5b6ef-e0d6-4aee-955c-91625bec9db4}')
    @commethod(7)
    def get_SizeLow(self, plSizeLow: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_SizeHigh(self, plSizeHigh: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Refresh(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetMessages(self, lPrefetchSize: Int32, pFaxIncomingMessageIterator: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxIncomingMessageIterator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetMessage(self, bstrMessageId: win32more.Windows.Win32.Foundation.BSTR, pFaxIncomingMessage: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxIncomingMessage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxAccountIncomingQueue(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{dd142d92-0186-4a95-a090-cbc3eadba6b4}')
    @commethod(7)
    def GetJobs(self, pFaxIncomingJobs: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxIncomingJobs)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetJob(self, bstrJobId: win32more.Windows.Win32.Foundation.BSTR, pFaxIncomingJob: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxIncomingJob)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxAccountNotify(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{b9b3bc81-ac1b-46f3-b39d-0adc30e1b788}')
    @commethod(7)
    def OnIncomingJobAdded(self, pFaxAccount: win32more.Windows.Win32.Devices.Fax.IFaxAccount, bstrJobId: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnIncomingJobRemoved(self, pFaxAccount: win32more.Windows.Win32.Devices.Fax.IFaxAccount, bstrJobId: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OnIncomingJobChanged(self, pFaxAccount: win32more.Windows.Win32.Devices.Fax.IFaxAccount, bstrJobId: win32more.Windows.Win32.Foundation.BSTR, pJobStatus: win32more.Windows.Win32.Devices.Fax.IFaxJobStatus) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def OnOutgoingJobAdded(self, pFaxAccount: win32more.Windows.Win32.Devices.Fax.IFaxAccount, bstrJobId: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def OnOutgoingJobRemoved(self, pFaxAccount: win32more.Windows.Win32.Devices.Fax.IFaxAccount, bstrJobId: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def OnOutgoingJobChanged(self, pFaxAccount: win32more.Windows.Win32.Devices.Fax.IFaxAccount, bstrJobId: win32more.Windows.Win32.Foundation.BSTR, pJobStatus: win32more.Windows.Win32.Devices.Fax.IFaxJobStatus) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def OnIncomingMessageAdded(self, pFaxAccount: win32more.Windows.Win32.Devices.Fax.IFaxAccount, bstrMessageId: win32more.Windows.Win32.Foundation.BSTR, fAddedToReceiveFolder: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def OnIncomingMessageRemoved(self, pFaxAccount: win32more.Windows.Win32.Devices.Fax.IFaxAccount, bstrMessageId: win32more.Windows.Win32.Foundation.BSTR, fRemovedFromReceiveFolder: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def OnOutgoingMessageAdded(self, pFaxAccount: win32more.Windows.Win32.Devices.Fax.IFaxAccount, bstrMessageId: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def OnOutgoingMessageRemoved(self, pFaxAccount: win32more.Windows.Win32.Devices.Fax.IFaxAccount, bstrMessageId: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def OnServerShutDown(self, pFaxServer: win32more.Windows.Win32.Devices.Fax.IFaxServer2) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxAccountOutgoingArchive(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{5463076d-ec14-491f-926e-b3ceda5e5662}')
    @commethod(7)
    def get_SizeLow(self, plSizeLow: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_SizeHigh(self, plSizeHigh: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Refresh(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetMessages(self, lPrefetchSize: Int32, pFaxOutgoingMessageIterator: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxOutgoingMessageIterator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetMessage(self, bstrMessageId: win32more.Windows.Win32.Foundation.BSTR, pFaxOutgoingMessage: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxOutgoingMessage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxAccountOutgoingQueue(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{0f1424e9-f22d-4553-b7a5-0d24bd0d7e46}')
    @commethod(7)
    def GetJobs(self, pFaxOutgoingJobs: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxOutgoingJobs)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetJob(self, bstrJobId: win32more.Windows.Win32.Foundation.BSTR, pFaxOutgoingJob: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxOutgoingJob)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxAccountSet(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{7428fbae-841e-47b8-86f4-2288946dca1b}')
    @commethod(7)
    def GetAccounts(self, ppFaxAccounts: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxAccounts)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetAccount(self, bstrAccountName: win32more.Windows.Win32.Foundation.BSTR, pFaxAccount: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxAccount)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AddAccount(self, bstrAccountName: win32more.Windows.Win32.Foundation.BSTR, pFaxAccount: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxAccount)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def RemoveAccount(self, bstrAccountName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxAccounts(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{93ea8162-8be7-42d1-ae7b-ec74e2d989da}')
    @commethod(7)
    def get__NewEnum(self, ppUnk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, vIndex: win32more.Windows.Win32.System.Variant.VARIANT, pFaxAccount: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxAccount)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(self, plCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxActivity(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{4b106f97-3df5-40f2-bc3c-44cb8115ebdf}')
    @commethod(7)
    def get_IncomingMessages(self, plIncomingMessages: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_RoutingMessages(self, plRoutingMessages: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_OutgoingMessages(self, plOutgoingMessages: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_QueuedMessages(self, plQueuedMessages: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Refresh(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxActivityLogging(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{1e29078b-5a69-497b-9592-49b7e7faddb5}')
    @commethod(7)
    def get_LogIncoming(self, pbLogIncoming: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_LogIncoming(self, bLogIncoming: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_LogOutgoing(self, pbLogOutgoing: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_LogOutgoing(self, bLogOutgoing: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_DatabasePath(self, pbstrDatabasePath: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_DatabasePath(self, bstrDatabasePath: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Refresh(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def Save(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{10f4d0f7-0994-4543-ab6e-506949128c40}')
    @commethod(7)
    def get_UseArchive(self, pbUseArchive: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_UseArchive(self, bUseArchive: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ArchiveLocation(self, pbstrArchiveLocation: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_ArchiveLocation(self, bstrArchiveLocation: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_SizeQuotaWarning(self, pbSizeQuotaWarning: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_SizeQuotaWarning(self, bSizeQuotaWarning: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_HighQuotaWaterMark(self, plHighQuotaWaterMark: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_HighQuotaWaterMark(self, lHighQuotaWaterMark: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_LowQuotaWaterMark(self, plLowQuotaWaterMark: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_LowQuotaWaterMark(self, lLowQuotaWaterMark: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_ArchiveAgeLimit(self, plArchiveAgeLimit: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_ArchiveAgeLimit(self, lArchiveAgeLimit: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_ArchiveSizeLow(self, plSizeLow: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_ArchiveSizeHigh(self, plSizeHigh: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_OutgoingQueueBlocked(self, pbOutgoingBlocked: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_OutgoingQueueBlocked(self, bOutgoingBlocked: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_OutgoingQueuePaused(self, pbOutgoingPaused: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_OutgoingQueuePaused(self, bOutgoingPaused: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_AllowPersonalCoverPages(self, pbAllowPersonalCoverPages: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_AllowPersonalCoverPages(self, bAllowPersonalCoverPages: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_UseDeviceTSID(self, pbUseDeviceTSID: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def put_UseDeviceTSID(self, bUseDeviceTSID: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def get_Retries(self, plRetries: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def put_Retries(self, lRetries: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_RetryDelay(self, plRetryDelay: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def put_RetryDelay(self, lRetryDelay: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_DiscountRateStart(self, pdateDiscountRateStart: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def put_DiscountRateStart(self, dateDiscountRateStart: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def get_DiscountRateEnd(self, pdateDiscountRateEnd: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def put_DiscountRateEnd(self, dateDiscountRateEnd: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def get_OutgoingQueueAgeLimit(self, plOutgoingQueueAgeLimit: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def put_OutgoingQueueAgeLimit(self, lOutgoingQueueAgeLimit: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def get_Branding(self, pbBranding: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def put_Branding(self, bBranding: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def get_IncomingQueueBlocked(self, pbIncomingBlocked: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def put_IncomingQueueBlocked(self, bIncomingBlocked: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def get_AutoCreateAccountOnConnect(self, pbAutoCreateAccountOnConnect: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def put_AutoCreateAccountOnConnect(self, bAutoCreateAccountOnConnect: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def get_IncomingFaxesArePublic(self, pbIncomingFaxesArePublic: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def put_IncomingFaxesArePublic(self, bIncomingFaxesArePublic: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def Refresh(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def Save(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxDevice(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{49306c59-b52e-4867-9df4-ca5841c956d0}')
    @commethod(7)
    def get_Id(self, plId: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_DeviceName(self, pbstrDeviceName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ProviderUniqueName(self, pbstrProviderUniqueName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_PoweredOff(self, pbPoweredOff: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_ReceivingNow(self, pbReceivingNow: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_SendingNow(self, pbSendingNow: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_UsedRoutingMethods(self, pvUsedRoutingMethods: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_Description(self, pbstrDescription: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_Description(self, bstrDescription: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_SendEnabled(self, pbSendEnabled: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_SendEnabled(self, bSendEnabled: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_ReceiveMode(self, pReceiveMode: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_DEVICE_RECEIVE_MODE_ENUM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def put_ReceiveMode(self, ReceiveMode: win32more.Windows.Win32.Devices.Fax.FAX_DEVICE_RECEIVE_MODE_ENUM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_RingsBeforeAnswer(self, plRingsBeforeAnswer: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def put_RingsBeforeAnswer(self, lRingsBeforeAnswer: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_CSID(self, pbstrCSID: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_CSID(self, bstrCSID: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_TSID(self, pbstrTSID: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_TSID(self, bstrTSID: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def Refresh(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def Save(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetExtensionProperty(self, bstrGUID: win32more.Windows.Win32.Foundation.BSTR, pvProperty: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def SetExtensionProperty(self, bstrGUID: win32more.Windows.Win32.Foundation.BSTR, vProperty: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def UseRoutingMethod(self, bstrMethodGUID: win32more.Windows.Win32.Foundation.BSTR, bUse: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_RingingNow(self, pbRingingNow: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def AnswerCall(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxDeviceIds(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{2f0f813f-4ce9-443e-8ca1-738cfaeee149}')
    @commethod(7)
    def get__NewEnum(self, ppUnk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, lIndex: Int32, plDeviceId: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(self, plCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Add(self, lDeviceId: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(self, lIndex: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetOrder(self, lDeviceId: Int32, lNewOrder: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxDeviceProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{290eac63-83ec-449c-8417-f148df8c682a}')
    @commethod(7)
    def get_FriendlyName(self, pbstrFriendlyName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_ImageName(self, pbstrImageName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_UniqueName(self, pbstrUniqueName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_TapiProviderName(self, pbstrTapiProviderName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_MajorVersion(self, plMajorVersion: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_MinorVersion(self, plMinorVersion: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_MajorBuild(self, plMajorBuild: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_MinorBuild(self, plMinorBuild: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Debug(self, pbDebug: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_Status(self, pStatus: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_PROVIDER_STATUS_ENUM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_InitErrorCode(self, plInitErrorCode: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_DeviceIds(self, pvDeviceIds: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxDeviceProviders(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{9fb76f62-4c7e-43a5-b6fd-502893f7e13e}')
    @commethod(7)
    def get__NewEnum(self, ppUnk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, vIndex: win32more.Windows.Win32.System.Variant.VARIANT, pFaxDeviceProvider: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxDeviceProvider)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(self, plCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxDevices(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{9e46783e-f34f-482e-a360-0416becbbd96}')
    @commethod(7)
    def get__NewEnum(self, ppUnk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, vIndex: win32more.Windows.Win32.System.Variant.VARIANT, pFaxDevice: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxDevice)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(self, plCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_ItemById(self, lId: Int32, ppFaxDevice: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxDevice)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxDocument(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{b207a246-09e3-4a4e-a7dc-fea31d29458f}')
    @commethod(7)
    def get_Body(self, pbstrBody: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Body(self, bstrBody: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Sender(self, ppFaxSender: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxSender)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Recipients(self, ppFaxRecipients: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxRecipients)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_CoverPage(self, pbstrCoverPage: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_CoverPage(self, bstrCoverPage: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Subject(self, pbstrSubject: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_Subject(self, bstrSubject: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Note(self, pbstrNote: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_Note(self, bstrNote: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_ScheduleTime(self, pdateScheduleTime: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_ScheduleTime(self, dateScheduleTime: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_ReceiptAddress(self, pbstrReceiptAddress: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_ReceiptAddress(self, bstrReceiptAddress: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_DocumentName(self, pbstrDocumentName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_DocumentName(self, bstrDocumentName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_CallHandle(self, plCallHandle: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_CallHandle(self, lCallHandle: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_CoverPageType(self, pCoverPageType: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_COVERPAGE_TYPE_ENUM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_CoverPageType(self, CoverPageType: win32more.Windows.Win32.Devices.Fax.FAX_COVERPAGE_TYPE_ENUM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_ScheduleType(self, pScheduleType: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_SCHEDULE_TYPE_ENUM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def put_ScheduleType(self, ScheduleType: win32more.Windows.Win32.Devices.Fax.FAX_SCHEDULE_TYPE_ENUM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def get_ReceiptType(self, pReceiptType: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_RECEIPT_TYPE_ENUM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def put_ReceiptType(self, ReceiptType: win32more.Windows.Win32.Devices.Fax.FAX_RECEIPT_TYPE_ENUM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_GroupBroadcastReceipts(self, pbUseGrouping: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def put_GroupBroadcastReceipts(self, bUseGrouping: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_Priority(self, pPriority: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_PRIORITY_TYPE_ENUM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def put_Priority(self, Priority: win32more.Windows.Win32.Devices.Fax.FAX_PRIORITY_TYPE_ENUM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def get_TapiConnection(self, ppTapiConnection: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def putref_TapiConnection(self, pTapiConnection: win32more.Windows.Win32.System.Com.IDispatch) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def Submit(self, bstrFaxServerName: win32more.Windows.Win32.Foundation.BSTR, pvFaxOutgoingJobIDs: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def ConnectedSubmit(self, pFaxServer: win32more.Windows.Win32.Devices.Fax.IFaxServer, pvFaxOutgoingJobIDs: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def get_AttachFaxToReceipt(self, pbAttachFax: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def put_AttachFaxToReceipt(self, bAttachFax: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxDocument2(ComPtr):
    extends: win32more.Windows.Win32.Devices.Fax.IFaxDocument
    _iid_ = Guid('{e1347661-f9ef-4d6d-b4a5-c0a068b65cff}')
    @commethod(41)
    def get_SubmissionId(self, pbstrSubmissionId: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def get_Bodies(self, pvBodies: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def put_Bodies(self, vBodies: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def Submit2(self, bstrFaxServerName: win32more.Windows.Win32.Foundation.BSTR, pvFaxOutgoingJobIDs: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), plErrorBodyFile: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def ConnectedSubmit2(self, pFaxServer: win32more.Windows.Win32.Devices.Fax.IFaxServer, pvFaxOutgoingJobIDs: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), plErrorBodyFile: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxEventLogging(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{0880d965-20e8-42e4-8e17-944f192caad4}')
    @commethod(7)
    def get_InitEventsLevel(self, pInitEventLevel: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_LOG_LEVEL_ENUM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_InitEventsLevel(self, InitEventLevel: win32more.Windows.Win32.Devices.Fax.FAX_LOG_LEVEL_ENUM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_InboundEventsLevel(self, pInboundEventLevel: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_LOG_LEVEL_ENUM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_InboundEventsLevel(self, InboundEventLevel: win32more.Windows.Win32.Devices.Fax.FAX_LOG_LEVEL_ENUM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_OutboundEventsLevel(self, pOutboundEventLevel: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_LOG_LEVEL_ENUM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_OutboundEventsLevel(self, OutboundEventLevel: win32more.Windows.Win32.Devices.Fax.FAX_LOG_LEVEL_ENUM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_GeneralEventsLevel(self, pGeneralEventLevel: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_LOG_LEVEL_ENUM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_GeneralEventsLevel(self, GeneralEventLevel: win32more.Windows.Win32.Devices.Fax.FAX_LOG_LEVEL_ENUM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def Refresh(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Save(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxFolders(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{dce3b2a8-a7ab-42bc-9d0a-3149457261a0}')
    @commethod(7)
    def get_OutgoingQueue(self, pFaxOutgoingQueue: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxOutgoingQueue)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_IncomingQueue(self, pFaxIncomingQueue: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxIncomingQueue)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_IncomingArchive(self, pFaxIncomingArchive: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxIncomingArchive)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_OutgoingArchive(self, pFaxOutgoingArchive: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxOutgoingArchive)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxInboundRouting(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{8148c20f-9d52-45b1-bf96-38fc12713527}')
    @commethod(7)
    def GetExtensions(self, pFaxInboundRoutingExtensions: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxInboundRoutingExtensions)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetMethods(self, pFaxInboundRoutingMethods: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxInboundRoutingMethods)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxInboundRoutingExtension(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{885b5e08-c26c-4ef9-af83-51580a750be1}')
    @commethod(7)
    def get_FriendlyName(self, pbstrFriendlyName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_ImageName(self, pbstrImageName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_UniqueName(self, pbstrUniqueName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_MajorVersion(self, plMajorVersion: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_MinorVersion(self, plMinorVersion: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_MajorBuild(self, plMajorBuild: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_MinorBuild(self, plMinorBuild: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_Debug(self, pbDebug: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Status(self, pStatus: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_PROVIDER_STATUS_ENUM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_InitErrorCode(self, plInitErrorCode: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_Methods(self, pvMethods: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxInboundRoutingExtensions(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{2f6c9673-7b26-42de-8eb0-915dcd2a4f4c}')
    @commethod(7)
    def get__NewEnum(self, ppUnk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, vIndex: win32more.Windows.Win32.System.Variant.VARIANT, pFaxInboundRoutingExtension: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxInboundRoutingExtension)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(self, plCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxInboundRoutingMethod(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{45700061-ad9d-4776-a8c4-64065492cf4b}')
    @commethod(7)
    def get_Name(self, pbstrName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_GUID(self, pbstrGUID: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_FunctionName(self, pbstrFunctionName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_ExtensionFriendlyName(self, pbstrExtensionFriendlyName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_ExtensionImageName(self, pbstrExtensionImageName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Priority(self, plPriority: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_Priority(self, lPriority: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def Refresh(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def Save(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxInboundRoutingMethods(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{783fca10-8908-4473-9d69-f67fbea0c6b9}')
    @commethod(7)
    def get__NewEnum(self, ppUnk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, vIndex: win32more.Windows.Win32.System.Variant.VARIANT, pFaxInboundRoutingMethod: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxInboundRoutingMethod)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(self, plCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxIncomingArchive(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{76062cc7-f714-4fbd-aa06-ed6e4a4b70f3}')
    @commethod(7)
    def get_UseArchive(self, pbUseArchive: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_UseArchive(self, bUseArchive: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ArchiveFolder(self, pbstrArchiveFolder: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_ArchiveFolder(self, bstrArchiveFolder: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_SizeQuotaWarning(self, pbSizeQuotaWarning: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_SizeQuotaWarning(self, bSizeQuotaWarning: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_HighQuotaWaterMark(self, plHighQuotaWaterMark: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_HighQuotaWaterMark(self, lHighQuotaWaterMark: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_LowQuotaWaterMark(self, plLowQuotaWaterMark: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_LowQuotaWaterMark(self, lLowQuotaWaterMark: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_AgeLimit(self, plAgeLimit: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_AgeLimit(self, lAgeLimit: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_SizeLow(self, plSizeLow: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_SizeHigh(self, plSizeHigh: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def Refresh(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def Save(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetMessages(self, lPrefetchSize: Int32, pFaxIncomingMessageIterator: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxIncomingMessageIterator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetMessage(self, bstrMessageId: win32more.Windows.Win32.Foundation.BSTR, pFaxIncomingMessage: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxIncomingMessage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxIncomingJob(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{207529e6-654a-4916-9f88-4d232ee8a107}')
    @commethod(7)
    def get_Size(self, plSize: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Id(self, pbstrId: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_CurrentPage(self, plCurrentPage: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_DeviceId(self, plDeviceId: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Status(self, pStatus: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_JOB_STATUS_ENUM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_ExtendedStatusCode(self, pExtendedStatusCode: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_JOB_EXTENDED_STATUS_ENUM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_ExtendedStatus(self, pbstrExtendedStatus: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_AvailableOperations(self, pAvailableOperations: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_JOB_OPERATIONS_ENUM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Retries(self, plRetries: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_TransmissionStart(self, pdateTransmissionStart: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_TransmissionEnd(self, pdateTransmissionEnd: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_CSID(self, pbstrCSID: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_TSID(self, pbstrTSID: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_CallerId(self, pbstrCallerId: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_RoutingInformation(self, pbstrRoutingInformation: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_JobType(self, pJobType: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_JOB_TYPE_ENUM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def Cancel(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def Refresh(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def CopyTiff(self, bstrTiffPath: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxIncomingJobs(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{011f04e9-4fd6-4c23-9513-b6b66bb26be9}')
    @commethod(7)
    def get__NewEnum(self, ppUnk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, vIndex: win32more.Windows.Win32.System.Variant.VARIANT, pFaxIncomingJob: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxIncomingJob)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(self, plCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxIncomingMessage(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{7cab88fa-2ef9-4851-b2f3-1d148fed8447}')
    @commethod(7)
    def get_Id(self, pbstrId: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Pages(self, plPages: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Size(self, plSize: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_DeviceName(self, pbstrDeviceName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Retries(self, plRetries: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_TransmissionStart(self, pdateTransmissionStart: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_TransmissionEnd(self, pdateTransmissionEnd: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_CSID(self, pbstrCSID: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_TSID(self, pbstrTSID: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_CallerId(self, pbstrCallerId: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_RoutingInformation(self, pbstrRoutingInformation: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def CopyTiff(self, bstrTiffPath: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def Delete(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxIncomingMessage2(ComPtr):
    extends: win32more.Windows.Win32.Devices.Fax.IFaxIncomingMessage
    _iid_ = Guid('{f9208503-e2bc-48f3-9ec0-e6236f9b509a}')
    @commethod(20)
    def get_Subject(self, pbstrSubject: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def put_Subject(self, bstrSubject: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_SenderName(self, pbstrSenderName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_SenderName(self, bstrSenderName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_SenderFaxNumber(self, pbstrSenderFaxNumber: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_SenderFaxNumber(self, bstrSenderFaxNumber: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_HasCoverPage(self, pbHasCoverPage: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_HasCoverPage(self, bHasCoverPage: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_Recipients(self, pbstrRecipients: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def put_Recipients(self, bstrRecipients: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_WasReAssigned(self, pbWasReAssigned: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_Read(self, pbRead: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def put_Read(self, bRead: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def ReAssign(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def Save(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def Refresh(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxIncomingMessageIterator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{fd73ecc4-6f06-4f52-82a8-f7ba06ae3108}')
    @commethod(7)
    def get_Message(self, pFaxIncomingMessage: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxIncomingMessage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_PrefetchSize(self, plPrefetchSize: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_PrefetchSize(self, lPrefetchSize: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_AtEOF(self, pbEOF: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def MoveFirst(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def MoveNext(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxIncomingQueue(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{902e64ef-8fd8-4b75-9725-6014df161545}')
    @commethod(7)
    def get_Blocked(self, pbBlocked: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Blocked(self, bBlocked: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Refresh(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Save(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetJobs(self, pFaxIncomingJobs: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxIncomingJobs)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetJob(self, bstrJobId: win32more.Windows.Win32.Foundation.BSTR, pFaxIncomingJob: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxIncomingJob)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxJobStatus(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{8b86f485-fd7f-4824-886b-40c5caa617cc}')
    @commethod(7)
    def get_Status(self, pStatus: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_JOB_STATUS_ENUM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Pages(self, plPages: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Size(self, plSize: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_CurrentPage(self, plCurrentPage: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_DeviceId(self, plDeviceId: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_CSID(self, pbstrCSID: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_TSID(self, pbstrTSID: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_ExtendedStatusCode(self, pExtendedStatusCode: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_JOB_EXTENDED_STATUS_ENUM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_ExtendedStatus(self, pbstrExtendedStatus: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_AvailableOperations(self, pAvailableOperations: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_JOB_OPERATIONS_ENUM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_Retries(self, plRetries: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_JobType(self, pJobType: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_JOB_TYPE_ENUM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_ScheduledTime(self, pdateScheduledTime: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_TransmissionStart(self, pdateTransmissionStart: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_TransmissionEnd(self, pdateTransmissionEnd: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_CallerId(self, pbstrCallerId: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_RoutingInformation(self, pbstrRoutingInformation: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxLoggingOptions(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{34e64fb9-6b31-4d32-8b27-d286c0c33606}')
    @commethod(7)
    def get_EventLogging(self, pFaxEventLogging: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxEventLogging)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_ActivityLogging(self, pFaxActivityLogging: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxActivityLogging)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxOutboundRouting(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{25dc05a4-9909-41bd-a95b-7e5d1dec1d43}')
    @commethod(7)
    def GetGroups(self, pFaxOutboundRoutingGroups: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxOutboundRoutingGroups)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetRules(self, pFaxOutboundRoutingRules: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxOutboundRoutingRules)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxOutboundRoutingGroup(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{ca6289a1-7e25-4f87-9a0b-93365734962c}')
    @commethod(7)
    def get_Name(self, pbstrName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Status(self, pStatus: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_GROUP_STATUS_ENUM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_DeviceIds(self, pFaxDeviceIds: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxDeviceIds)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxOutboundRoutingGroups(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{235cbef7-c2de-4bfd-b8da-75097c82c87f}')
    @commethod(7)
    def get__NewEnum(self, ppUnk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, vIndex: win32more.Windows.Win32.System.Variant.VARIANT, pFaxOutboundRoutingGroup: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxOutboundRoutingGroup)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(self, plCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Add(self, bstrName: win32more.Windows.Win32.Foundation.BSTR, pFaxOutboundRoutingGroup: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxOutboundRoutingGroup)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(self, vIndex: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxOutboundRoutingRule(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{e1f795d5-07c2-469f-b027-acacc23219da}')
    @commethod(7)
    def get_CountryCode(self, plCountryCode: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_AreaCode(self, plAreaCode: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Status(self, pStatus: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_RULE_STATUS_ENUM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_UseDevice(self, pbUseDevice: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_UseDevice(self, bUseDevice: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_DeviceId(self, plDeviceId: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_DeviceId(self, DeviceId: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_GroupName(self, pbstrGroupName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_GroupName(self, bstrGroupName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Refresh(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def Save(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxOutboundRoutingRules(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{dcefa1e7-ae7d-4ed6-8521-369edcca5120}')
    @commethod(7)
    def get__NewEnum(self, ppUnk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, lIndex: Int32, pFaxOutboundRoutingRule: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxOutboundRoutingRule)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(self, plCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def ItemByCountryAndArea(self, lCountryCode: Int32, lAreaCode: Int32, pFaxOutboundRoutingRule: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxOutboundRoutingRule)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RemoveByCountryAndArea(self, lCountryCode: Int32, lAreaCode: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Remove(self, lIndex: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Add(self, lCountryCode: Int32, lAreaCode: Int32, bUseDevice: win32more.Windows.Win32.Foundation.VARIANT_BOOL, bstrGroupName: win32more.Windows.Win32.Foundation.BSTR, lDeviceId: Int32, pFaxOutboundRoutingRule: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxOutboundRoutingRule)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxOutgoingArchive(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{c9c28f40-8d80-4e53-810f-9a79919b49fd}')
    @commethod(7)
    def get_UseArchive(self, pbUseArchive: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_UseArchive(self, bUseArchive: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ArchiveFolder(self, pbstrArchiveFolder: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_ArchiveFolder(self, bstrArchiveFolder: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_SizeQuotaWarning(self, pbSizeQuotaWarning: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_SizeQuotaWarning(self, bSizeQuotaWarning: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_HighQuotaWaterMark(self, plHighQuotaWaterMark: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_HighQuotaWaterMark(self, lHighQuotaWaterMark: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_LowQuotaWaterMark(self, plLowQuotaWaterMark: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_LowQuotaWaterMark(self, lLowQuotaWaterMark: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_AgeLimit(self, plAgeLimit: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_AgeLimit(self, lAgeLimit: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_SizeLow(self, plSizeLow: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_SizeHigh(self, plSizeHigh: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def Refresh(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def Save(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetMessages(self, lPrefetchSize: Int32, pFaxOutgoingMessageIterator: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxOutgoingMessageIterator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetMessage(self, bstrMessageId: win32more.Windows.Win32.Foundation.BSTR, pFaxOutgoingMessage: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxOutgoingMessage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxOutgoingJob(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{6356daad-6614-4583-bf7a-3ad67bbfc71c}')
    @commethod(7)
    def get_Subject(self, pbstrSubject: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_DocumentName(self, pbstrDocumentName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Pages(self, plPages: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Size(self, plSize: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_SubmissionId(self, pbstrSubmissionId: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Id(self, pbstrId: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_OriginalScheduledTime(self, pdateOriginalScheduledTime: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_SubmissionTime(self, pdateSubmissionTime: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_ReceiptType(self, pReceiptType: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_RECEIPT_TYPE_ENUM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_Priority(self, pPriority: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_PRIORITY_TYPE_ENUM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_Sender(self, ppFaxSender: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxSender)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_Recipient(self, ppFaxRecipient: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxRecipient)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_CurrentPage(self, plCurrentPage: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_DeviceId(self, plDeviceId: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_Status(self, pStatus: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_JOB_STATUS_ENUM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_ExtendedStatusCode(self, pExtendedStatusCode: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_JOB_EXTENDED_STATUS_ENUM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_ExtendedStatus(self, pbstrExtendedStatus: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_AvailableOperations(self, pAvailableOperations: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_JOB_OPERATIONS_ENUM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_Retries(self, plRetries: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_ScheduledTime(self, pdateScheduledTime: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_TransmissionStart(self, pdateTransmissionStart: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_TransmissionEnd(self, pdateTransmissionEnd: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def get_CSID(self, pbstrCSID: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_TSID(self, pbstrTSID: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_GroupBroadcastReceipts(self, pbGroupBroadcastReceipts: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def Pause(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def Resume(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def Restart(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def CopyTiff(self, bstrTiffPath: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def Refresh(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def Cancel(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxOutgoingJob2(ComPtr):
    extends: win32more.Windows.Win32.Devices.Fax.IFaxOutgoingJob
    _iid_ = Guid('{418a8d96-59a0-4789-b176-edf3dc8fa8f7}')
    @commethod(38)
    def get_HasCoverPage(self, pbHasCoverPage: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def get_ReceiptAddress(self, pbstrReceiptAddress: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def get_ScheduleType(self, pScheduleType: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_SCHEDULE_TYPE_ENUM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxOutgoingJobs(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{2c56d8e6-8c2f-4573-944c-e505f8f5aeed}')
    @commethod(7)
    def get__NewEnum(self, ppUnk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, vIndex: win32more.Windows.Win32.System.Variant.VARIANT, pFaxOutgoingJob: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxOutgoingJob)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(self, plCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxOutgoingMessage(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{f0ea35de-caa5-4a7c-82c7-2b60ba5f2be2}')
    @commethod(7)
    def get_SubmissionId(self, pbstrSubmissionId: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Id(self, pbstrId: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Subject(self, pbstrSubject: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_DocumentName(self, pbstrDocumentName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Retries(self, plRetries: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Pages(self, plPages: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Size(self, plSize: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_OriginalScheduledTime(self, pdateOriginalScheduledTime: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_SubmissionTime(self, pdateSubmissionTime: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_Priority(self, pPriority: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_PRIORITY_TYPE_ENUM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_Sender(self, ppFaxSender: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxSender)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_Recipient(self, ppFaxRecipient: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxRecipient)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_DeviceName(self, pbstrDeviceName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_TransmissionStart(self, pdateTransmissionStart: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_TransmissionEnd(self, pdateTransmissionEnd: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_CSID(self, pbstrCSID: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_TSID(self, pbstrTSID: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def CopyTiff(self, bstrTiffPath: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def Delete(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxOutgoingMessage2(ComPtr):
    extends: win32more.Windows.Win32.Devices.Fax.IFaxOutgoingMessage
    _iid_ = Guid('{b37df687-bc88-4b46-b3be-b458b3ea9e7f}')
    @commethod(26)
    def get_HasCoverPage(self, pbHasCoverPage: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_ReceiptType(self, pReceiptType: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_RECEIPT_TYPE_ENUM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_ReceiptAddress(self, pbstrReceiptAddress: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def get_Read(self, pbRead: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def put_Read(self, bRead: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def Save(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def Refresh(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxOutgoingMessageIterator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{f5ec5d4f-b840-432f-9980-112fe42a9b7a}')
    @commethod(7)
    def get_Message(self, pFaxOutgoingMessage: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxOutgoingMessage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_AtEOF(self, pbEOF: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_PrefetchSize(self, plPrefetchSize: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_PrefetchSize(self, lPrefetchSize: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def MoveFirst(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def MoveNext(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxOutgoingQueue(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{80b1df24-d9ac-4333-b373-487cedc80ce5}')
    @commethod(7)
    def get_Blocked(self, pbBlocked: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Blocked(self, bBlocked: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Paused(self, pbPaused: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Paused(self, bPaused: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_AllowPersonalCoverPages(self, pbAllowPersonalCoverPages: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_AllowPersonalCoverPages(self, bAllowPersonalCoverPages: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_UseDeviceTSID(self, pbUseDeviceTSID: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_UseDeviceTSID(self, bUseDeviceTSID: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Retries(self, plRetries: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_Retries(self, lRetries: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_RetryDelay(self, plRetryDelay: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_RetryDelay(self, lRetryDelay: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_DiscountRateStart(self, pdateDiscountRateStart: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_DiscountRateStart(self, dateDiscountRateStart: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_DiscountRateEnd(self, pdateDiscountRateEnd: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_DiscountRateEnd(self, dateDiscountRateEnd: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_AgeLimit(self, plAgeLimit: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_AgeLimit(self, lAgeLimit: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_Branding(self, pbBranding: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_Branding(self, bBranding: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def Refresh(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def Save(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def GetJobs(self, pFaxOutgoingJobs: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxOutgoingJobs)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def GetJob(self, bstrJobId: win32more.Windows.Win32.Foundation.BSTR, pFaxOutgoingJob: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxOutgoingJob)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxReceiptOptions(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{378efaeb-5fcb-4afb-b2ee-e16e80614487}')
    @commethod(7)
    def get_AuthenticationType(self, pType: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_SMTP_AUTHENTICATION_TYPE_ENUM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_AuthenticationType(self, Type: win32more.Windows.Win32.Devices.Fax.FAX_SMTP_AUTHENTICATION_TYPE_ENUM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_SMTPServer(self, pbstrSMTPServer: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_SMTPServer(self, bstrSMTPServer: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_SMTPPort(self, plSMTPPort: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_SMTPPort(self, lSMTPPort: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_SMTPSender(self, pbstrSMTPSender: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_SMTPSender(self, bstrSMTPSender: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_SMTPUser(self, pbstrSMTPUser: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_SMTPUser(self, bstrSMTPUser: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_AllowedReceipts(self, pAllowedReceipts: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_RECEIPT_TYPE_ENUM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_AllowedReceipts(self, AllowedReceipts: win32more.Windows.Win32.Devices.Fax.FAX_RECEIPT_TYPE_ENUM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_SMTPPassword(self, pbstrSMTPPassword: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_SMTPPassword(self, bstrSMTPPassword: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def Refresh(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def Save(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_UseForInboundRouting(self, pbUseForInboundRouting: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_UseForInboundRouting(self, bUseForInboundRouting: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxRecipient(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{9a3da3a0-538d-42b6-9444-aaa57d0ce2bc}')
    @commethod(7)
    def get_FaxNumber(self, pbstrFaxNumber: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_FaxNumber(self, bstrFaxNumber: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Name(self, pbstrName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Name(self, bstrName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxRecipients(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{b9c9de5a-894e-4492-9fa3-08c627c11d5d}')
    @commethod(7)
    def get__NewEnum(self, ppUnk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, lIndex: Int32, ppFaxRecipient: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxRecipient)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(self, plCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Add(self, bstrFaxNumber: win32more.Windows.Win32.Foundation.BSTR, bstrRecipientName: win32more.Windows.Win32.Foundation.BSTR, ppFaxRecipient: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxRecipient)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(self, lIndex: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxSecurity(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{77b508c1-09c0-47a2-91eb-fce7fdf2690e}')
    @commethod(7)
    def get_Descriptor(self, pvDescriptor: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Descriptor(self, vDescriptor: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_GrantedRights(self, pGrantedRights: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_ACCESS_RIGHTS_ENUM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Refresh(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Save(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_InformationType(self, plInformationType: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_InformationType(self, lInformationType: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxSecurity2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{17d851f4-d09b-48fc-99c9-8f24c4db9ab1}')
    @commethod(7)
    def get_Descriptor(self, pvDescriptor: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Descriptor(self, vDescriptor: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_GrantedRights(self, pGrantedRights: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_ACCESS_RIGHTS_ENUM_2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Refresh(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Save(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_InformationType(self, plInformationType: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_InformationType(self, lInformationType: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxSender(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{0d879d7d-f57a-4cc6-a6f9-3ee5d527b46a}')
    @commethod(7)
    def get_BillingCode(self, pbstrBillingCode: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_BillingCode(self, bstrBillingCode: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_City(self, pbstrCity: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_City(self, bstrCity: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Company(self, pbstrCompany: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_Company(self, bstrCompany: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Country(self, pbstrCountry: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_Country(self, bstrCountry: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Department(self, pbstrDepartment: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_Department(self, bstrDepartment: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_Email(self, pbstrEmail: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_Email(self, bstrEmail: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_FaxNumber(self, pbstrFaxNumber: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_FaxNumber(self, bstrFaxNumber: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_HomePhone(self, pbstrHomePhone: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_HomePhone(self, bstrHomePhone: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_Name(self, pbstrName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_Name(self, bstrName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_TSID(self, pbstrTSID: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_TSID(self, bstrTSID: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_OfficePhone(self, pbstrOfficePhone: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def put_OfficePhone(self, bstrOfficePhone: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def get_OfficeLocation(self, pbstrOfficeLocation: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def put_OfficeLocation(self, bstrOfficeLocation: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_State(self, pbstrState: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def put_State(self, bstrState: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_StreetAddress(self, pbstrStreetAddress: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def put_StreetAddress(self, bstrStreetAddress: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def get_Title(self, pbstrTitle: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def put_Title(self, bstrTitle: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def get_ZipCode(self, pbstrZipCode: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def put_ZipCode(self, bstrZipCode: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def LoadDefaultSender(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def SaveDefaultSender(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxServer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{475b6469-90a5-4878-a577-17a86e8e3462}')
    @commethod(7)
    def Connect(self, bstrServerName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_ServerName(self, pbstrServerName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetDeviceProviders(self, ppFaxDeviceProviders: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxDeviceProviders)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetDevices(self, ppFaxDevices: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxDevices)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_InboundRouting(self, ppFaxInboundRouting: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxInboundRouting)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Folders(self, pFaxFolders: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxFolders)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_LoggingOptions(self, ppFaxLoggingOptions: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxLoggingOptions)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_MajorVersion(self, plMajorVersion: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_MinorVersion(self, plMinorVersion: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_MajorBuild(self, plMajorBuild: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_MinorBuild(self, plMinorBuild: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_Debug(self, pbDebug: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_Activity(self, ppFaxActivity: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxActivity)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_OutboundRouting(self, ppFaxOutboundRouting: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxOutboundRouting)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_ReceiptOptions(self, ppFaxReceiptOptions: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxReceiptOptions)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_Security(self, ppFaxSecurity: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxSecurity)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def Disconnect(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetExtensionProperty(self, bstrGUID: win32more.Windows.Win32.Foundation.BSTR, pvProperty: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def SetExtensionProperty(self, bstrGUID: win32more.Windows.Win32.Foundation.BSTR, vProperty: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def ListenToServerEvents(self, EventTypes: win32more.Windows.Win32.Devices.Fax.FAX_SERVER_EVENTS_TYPE_ENUM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def RegisterDeviceProvider(self, bstrGUID: win32more.Windows.Win32.Foundation.BSTR, bstrFriendlyName: win32more.Windows.Win32.Foundation.BSTR, bstrImageName: win32more.Windows.Win32.Foundation.BSTR, TspName: win32more.Windows.Win32.Foundation.BSTR, lFSPIVersion: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def UnregisterDeviceProvider(self, bstrUniqueName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def RegisterInboundRoutingExtension(self, bstrExtensionName: win32more.Windows.Win32.Foundation.BSTR, bstrFriendlyName: win32more.Windows.Win32.Foundation.BSTR, bstrImageName: win32more.Windows.Win32.Foundation.BSTR, vMethods: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def UnregisterInboundRoutingExtension(self, bstrExtensionUniqueName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_RegisteredEvents(self, pEventTypes: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_SERVER_EVENTS_TYPE_ENUM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def get_APIVersion(self, pAPIVersion: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_SERVER_APIVERSION_ENUM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxServer2(ComPtr):
    extends: win32more.Windows.Win32.Devices.Fax.IFaxServer
    _iid_ = Guid('{571ced0f-5609-4f40-9176-547e3a72ca7c}')
    @commethod(33)
    def get_Configuration(self, ppFaxConfiguration: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxConfiguration)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def get_CurrentAccount(self, ppCurrentAccount: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxAccount)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def get_FaxAccountSet(self, ppFaxAccountSet: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxAccountSet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def get_Security2(self, ppFaxSecurity2: POINTER(win32more.Windows.Win32.Devices.Fax.IFaxSecurity2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFaxServerNotify(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{2e037b27-cf8a-4abd-b1e0-5704943bea6f}')
class IFaxServerNotify2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{ec9c69b9-5fe7-4805-9467-82fcd96af903}')
    @commethod(7)
    def OnIncomingJobAdded(self, pFaxServer: win32more.Windows.Win32.Devices.Fax.IFaxServer2, bstrJobId: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnIncomingJobRemoved(self, pFaxServer: win32more.Windows.Win32.Devices.Fax.IFaxServer2, bstrJobId: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OnIncomingJobChanged(self, pFaxServer: win32more.Windows.Win32.Devices.Fax.IFaxServer2, bstrJobId: win32more.Windows.Win32.Foundation.BSTR, pJobStatus: win32more.Windows.Win32.Devices.Fax.IFaxJobStatus) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def OnOutgoingJobAdded(self, pFaxServer: win32more.Windows.Win32.Devices.Fax.IFaxServer2, bstrJobId: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def OnOutgoingJobRemoved(self, pFaxServer: win32more.Windows.Win32.Devices.Fax.IFaxServer2, bstrJobId: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def OnOutgoingJobChanged(self, pFaxServer: win32more.Windows.Win32.Devices.Fax.IFaxServer2, bstrJobId: win32more.Windows.Win32.Foundation.BSTR, pJobStatus: win32more.Windows.Win32.Devices.Fax.IFaxJobStatus) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def OnIncomingMessageAdded(self, pFaxServer: win32more.Windows.Win32.Devices.Fax.IFaxServer2, bstrMessageId: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def OnIncomingMessageRemoved(self, pFaxServer: win32more.Windows.Win32.Devices.Fax.IFaxServer2, bstrMessageId: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def OnOutgoingMessageAdded(self, pFaxServer: win32more.Windows.Win32.Devices.Fax.IFaxServer2, bstrMessageId: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def OnOutgoingMessageRemoved(self, pFaxServer: win32more.Windows.Win32.Devices.Fax.IFaxServer2, bstrMessageId: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def OnReceiptOptionsChange(self, pFaxServer: win32more.Windows.Win32.Devices.Fax.IFaxServer2) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def OnActivityLoggingConfigChange(self, pFaxServer: win32more.Windows.Win32.Devices.Fax.IFaxServer2) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def OnSecurityConfigChange(self, pFaxServer: win32more.Windows.Win32.Devices.Fax.IFaxServer2) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def OnEventLoggingConfigChange(self, pFaxServer: win32more.Windows.Win32.Devices.Fax.IFaxServer2) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def OnOutgoingQueueConfigChange(self, pFaxServer: win32more.Windows.Win32.Devices.Fax.IFaxServer2) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def OnOutgoingArchiveConfigChange(self, pFaxServer: win32more.Windows.Win32.Devices.Fax.IFaxServer2) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def OnIncomingArchiveConfigChange(self, pFaxServer: win32more.Windows.Win32.Devices.Fax.IFaxServer2) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def OnDevicesConfigChange(self, pFaxServer: win32more.Windows.Win32.Devices.Fax.IFaxServer2) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def OnOutboundRoutingGroupsConfigChange(self, pFaxServer: win32more.Windows.Win32.Devices.Fax.IFaxServer2) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def OnOutboundRoutingRulesConfigChange(self, pFaxServer: win32more.Windows.Win32.Devices.Fax.IFaxServer2) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def OnServerActivityChange(self, pFaxServer: win32more.Windows.Win32.Devices.Fax.IFaxServer2, lIncomingMessages: Int32, lRoutingMessages: Int32, lOutgoingMessages: Int32, lQueuedMessages: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def OnQueuesStatusChange(self, pFaxServer: win32more.Windows.Win32.Devices.Fax.IFaxServer2, bOutgoingQueueBlocked: win32more.Windows.Win32.Foundation.VARIANT_BOOL, bOutgoingQueuePaused: win32more.Windows.Win32.Foundation.VARIANT_BOOL, bIncomingQueueBlocked: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def OnNewCall(self, pFaxServer: win32more.Windows.Win32.Devices.Fax.IFaxServer2, lCallId: Int32, lDeviceId: Int32, bstrCallerId: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def OnServerShutDown(self, pFaxServer: win32more.Windows.Win32.Devices.Fax.IFaxServer2) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def OnDeviceStatusChange(self, pFaxServer: win32more.Windows.Win32.Devices.Fax.IFaxServer2, lDeviceId: Int32, bPoweredOff: win32more.Windows.Win32.Foundation.VARIANT_BOOL, bSending: win32more.Windows.Win32.Foundation.VARIANT_BOOL, bReceiving: win32more.Windows.Win32.Foundation.VARIANT_BOOL, bRinging: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def OnGeneralServerConfigChanged(self, pFaxServer: win32more.Windows.Win32.Devices.Fax.IFaxServer2) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IStiDevice(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6cfa5a80-2dc8-11d0-90ea-00aa0060f86c}')
    @commethod(3)
    def Initialize(self, hinst: win32more.Windows.Win32.Foundation.HINSTANCE, pwszDeviceName: win32more.Windows.Win32.Foundation.PWSTR, dwVersion: UInt32, dwMode: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCapabilities(self, pDevCaps: POINTER(win32more.Windows.Win32.Devices.Fax.STI_DEV_CAPS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetStatus(self, pDevStatus: POINTER(win32more.Windows.Win32.Devices.Fax.STI_DEVICE_STATUS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def DeviceReset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Diagnostic(self, pBuffer: POINTER(win32more.Windows.Win32.Devices.Fax.STI_DIAG)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Escape(self, EscapeFunction: UInt32, lpInData: VoidPtr, cbInDataSize: UInt32, pOutData: VoidPtr, dwOutDataSize: UInt32, pdwActualData: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetLastError(self, pdwLastDeviceError: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def LockDevice(self, dwTimeOut: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def UnLockDevice(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def RawReadData(self, lpBuffer: VoidPtr, lpdwNumberOfBytes: POINTER(UInt32), lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def RawWriteData(self, lpBuffer: VoidPtr, nNumberOfBytes: UInt32, lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def RawReadCommand(self, lpBuffer: VoidPtr, lpdwNumberOfBytes: POINTER(UInt32), lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def RawWriteCommand(self, lpBuffer: VoidPtr, nNumberOfBytes: UInt32, lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Subscribe(self, lpSubsribe: POINTER(win32more.Windows.Win32.Devices.Fax.STISUBSCRIBE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetLastNotificationData(self, lpNotify: POINTER(win32more.Windows.Win32.Devices.Fax.STINOTIFY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def UnSubscribe(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetLastErrorInfo(self, pLastErrorInfo: POINTER(win32more.Windows.Win32.Devices.Fax._ERROR_INFOW)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IStiDeviceControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{128a9860-52dc-11d0-9edf-444553540000}')
    @commethod(3)
    def Initialize(self, dwDeviceType: UInt32, dwMode: UInt32, pwszPortName: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RawReadData(self, lpBuffer: VoidPtr, lpdwNumberOfBytes: POINTER(UInt32), lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RawWriteData(self, lpBuffer: VoidPtr, nNumberOfBytes: UInt32, lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RawReadCommand(self, lpBuffer: VoidPtr, lpdwNumberOfBytes: POINTER(UInt32), lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RawWriteCommand(self, lpBuffer: VoidPtr, nNumberOfBytes: UInt32, lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RawDeviceControl(self, EscapeFunction: UInt32, lpInData: VoidPtr, cbInDataSize: UInt32, pOutData: VoidPtr, dwOutDataSize: UInt32, pdwActualData: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetLastError(self, lpdwLastError: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetMyDevicePortName(self, lpszDevicePath: win32more.Windows.Win32.Foundation.PWSTR, cwDevicePathSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetMyDeviceHandle(self, lph: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetMyDeviceOpenMode(self, pdwOpenMode: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def WriteToErrorLog(self, dwMessageType: UInt32, pszMessage: win32more.Windows.Win32.Foundation.PWSTR, dwErrorCode: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IStiUSD(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0c9bb460-51ac-11d0-90ea-00aa0060f86c}')
    @commethod(3)
    def Initialize(self, pHelDcb: win32more.Windows.Win32.Devices.Fax.IStiDeviceControl, dwStiVersion: UInt32, hParametersKey: win32more.Windows.Win32.System.Registry.HKEY) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCapabilities(self, pDevCaps: POINTER(win32more.Windows.Win32.Devices.Fax.STI_USD_CAPS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetStatus(self, pDevStatus: POINTER(win32more.Windows.Win32.Devices.Fax.STI_DEVICE_STATUS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def DeviceReset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Diagnostic(self, pBuffer: POINTER(win32more.Windows.Win32.Devices.Fax.STI_DIAG)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Escape(self, EscapeFunction: UInt32, lpInData: VoidPtr, cbInDataSize: UInt32, pOutData: VoidPtr, cbOutDataSize: UInt32, pdwActualData: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetLastError(self, pdwLastDeviceError: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def LockDevice(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def UnLockDevice(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def RawReadData(self, lpBuffer: VoidPtr, lpdwNumberOfBytes: POINTER(UInt32), lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def RawWriteData(self, lpBuffer: VoidPtr, nNumberOfBytes: UInt32, lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def RawReadCommand(self, lpBuffer: VoidPtr, lpdwNumberOfBytes: POINTER(UInt32), lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def RawWriteCommand(self, lpBuffer: VoidPtr, nNumberOfBytes: UInt32, lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetNotificationHandle(self, hEvent: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetNotificationData(self, lpNotify: POINTER(win32more.Windows.Win32.Devices.Fax.STINOTIFY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetLastErrorInfo(self, pLastErrorInfo: POINTER(win32more.Windows.Win32.Devices.Fax._ERROR_INFOW)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IStillImageW(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{641bd880-2dc8-11d0-90ea-00aa0060f86c}')
    @commethod(3)
    def Initialize(self, hinst: win32more.Windows.Win32.Foundation.HINSTANCE, dwVersion: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDeviceList(self, dwType: UInt32, dwFlags: UInt32, pdwItemsReturned: POINTER(UInt32), ppBuffer: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDeviceInfo(self, pwszDeviceName: win32more.Windows.Win32.Foundation.PWSTR, ppBuffer: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateDevice(self, pwszDeviceName: win32more.Windows.Win32.Foundation.PWSTR, dwMode: UInt32, pDevice: POINTER(win32more.Windows.Win32.Devices.Fax.IStiDevice), punkOuter: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetDeviceValue(self, pwszDeviceName: win32more.Windows.Win32.Foundation.PWSTR, pValueName: win32more.Windows.Win32.Foundation.PWSTR, pType: POINTER(UInt32), pData: POINTER(Byte), cbData: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetDeviceValue(self, pwszDeviceName: win32more.Windows.Win32.Foundation.PWSTR, pValueName: win32more.Windows.Win32.Foundation.PWSTR, Type: UInt32, pData: POINTER(Byte), cbData: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetSTILaunchInformation(self, pwszDeviceName: win32more.Windows.Win32.Foundation.PWSTR, pdwEventCode: POINTER(UInt32), pwszEventName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def RegisterLaunchApplication(self, pwszAppName: win32more.Windows.Win32.Foundation.PWSTR, pwszCommandLine: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def UnregisterLaunchApplication(self, pwszAppName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def EnableHwNotifications(self, pwszDeviceName: win32more.Windows.Win32.Foundation.PWSTR, bNewState: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetHwNotificationState(self, pwszDeviceName: win32more.Windows.Win32.Foundation.PWSTR, pbCurrentState: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def RefreshDeviceBus(self, pwszDeviceName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def LaunchApplicationForDevice(self, pwszDeviceName: win32more.Windows.Win32.Foundation.PWSTR, pwszAppName: win32more.Windows.Win32.Foundation.PWSTR, pStiNotify: POINTER(win32more.Windows.Win32.Devices.Fax.STINOTIFY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetupDeviceParameters(self, param0: POINTER(win32more.Windows.Win32.Devices.Fax.STI_DEVICE_INFORMATIONW)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def WriteToErrorLog(self, dwMessageType: UInt32, pszMessage: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFAXABORT(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, JobId: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXACCESSCHECK(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, AccessMask: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXCLOSE(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXCOMPLETEJOBPARAMSA(JobParams: POINTER(POINTER(win32more.Windows.Win32.Devices.Fax.FAX_JOB_PARAMA)), CoverpageInfo: POINTER(POINTER(win32more.Windows.Win32.Devices.Fax.FAX_COVERPAGE_INFOA))) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXCOMPLETEJOBPARAMSW(JobParams: POINTER(POINTER(win32more.Windows.Win32.Devices.Fax.FAX_JOB_PARAMW)), CoverpageInfo: POINTER(POINTER(win32more.Windows.Win32.Devices.Fax.FAX_COVERPAGE_INFOW))) -> win32more.Windows.Win32.Foundation.BOOL: ...
PFAXCOMPLETEJOBPARAMS = UnicodeAlias('PFAXCOMPLETEJOBPARAMSW')
@winfunctype_pointer
def PFAXCONNECTFAXSERVERA(MachineName: win32more.Windows.Win32.Foundation.PSTR, FaxHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXCONNECTFAXSERVERW(MachineName: win32more.Windows.Win32.Foundation.PWSTR, FaxHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
PFAXCONNECTFAXSERVER = UnicodeAlias('PFAXCONNECTFAXSERVERW')
@winfunctype_pointer
def PFAXDEVABORTOPERATION(param0: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXDEVCONFIGURE(param0: POINTER(win32more.Windows.Win32.UI.Controls.HPROPSHEETPAGE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXDEVENDJOB(param0: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXDEVINITIALIZE(param0: UInt32, param1: win32more.Windows.Win32.Foundation.HANDLE, param2: POINTER(win32more.Windows.Win32.Devices.Fax.PFAX_LINECALLBACK), param3: win32more.Windows.Win32.Devices.Fax.PFAX_SERVICE_CALLBACK) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXDEVRECEIVE(param0: win32more.Windows.Win32.Foundation.HANDLE, param1: UInt32, param2: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_RECEIVE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXDEVREPORTSTATUS(param0: win32more.Windows.Win32.Foundation.HANDLE, param1: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_DEV_STATUS), param2: UInt32, param3: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXDEVSEND(param0: win32more.Windows.Win32.Foundation.HANDLE, param1: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_SEND), param2: win32more.Windows.Win32.Devices.Fax.PFAX_SEND_CALLBACK) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXDEVSHUTDOWN() -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFAXDEVSTARTJOB(param0: UInt32, param1: UInt32, param2: POINTER(win32more.Windows.Win32.Foundation.HANDLE), param3: win32more.Windows.Win32.Foundation.HANDLE, param4: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXDEVVIRTUALDEVICECREATION(DeviceCount: POINTER(UInt32), DeviceNamePrefix: win32more.Windows.Win32.Foundation.PWSTR, DeviceIdPrefix: POINTER(UInt32), CompletionPort: win32more.Windows.Win32.Foundation.HANDLE, CompletionKey: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXENABLEROUTINGMETHODA(FaxPortHandle: win32more.Windows.Win32.Foundation.HANDLE, RoutingGuid: win32more.Windows.Win32.Foundation.PSTR, Enabled: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXENABLEROUTINGMETHODW(FaxPortHandle: win32more.Windows.Win32.Foundation.HANDLE, RoutingGuid: win32more.Windows.Win32.Foundation.PWSTR, Enabled: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
PFAXENABLEROUTINGMETHOD = UnicodeAlias('PFAXENABLEROUTINGMETHODW')
@winfunctype_pointer
def PFAXENUMGLOBALROUTINGINFOA(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, RoutingInfo: POINTER(POINTER(win32more.Windows.Win32.Devices.Fax.FAX_GLOBAL_ROUTING_INFOA)), MethodsReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXENUMGLOBALROUTINGINFOW(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, RoutingInfo: POINTER(POINTER(win32more.Windows.Win32.Devices.Fax.FAX_GLOBAL_ROUTING_INFOW)), MethodsReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
PFAXENUMGLOBALROUTINGINFO = UnicodeAlias('PFAXENUMGLOBALROUTINGINFOW')
@winfunctype_pointer
def PFAXENUMJOBSA(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, JobEntry: POINTER(POINTER(win32more.Windows.Win32.Devices.Fax.FAX_JOB_ENTRYA)), JobsReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXENUMJOBSW(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, JobEntry: POINTER(POINTER(win32more.Windows.Win32.Devices.Fax.FAX_JOB_ENTRYW)), JobsReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
PFAXENUMJOBS = UnicodeAlias('PFAXENUMJOBSW')
@winfunctype_pointer
def PFAXENUMPORTSA(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, PortInfo: POINTER(POINTER(win32more.Windows.Win32.Devices.Fax.FAX_PORT_INFOA)), PortsReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXENUMPORTSW(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, PortInfo: POINTER(POINTER(win32more.Windows.Win32.Devices.Fax.FAX_PORT_INFOW)), PortsReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
PFAXENUMPORTS = UnicodeAlias('PFAXENUMPORTSW')
@winfunctype_pointer
def PFAXENUMROUTINGMETHODSA(FaxPortHandle: win32more.Windows.Win32.Foundation.HANDLE, RoutingMethod: POINTER(POINTER(win32more.Windows.Win32.Devices.Fax.FAX_ROUTING_METHODA)), MethodsReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXENUMROUTINGMETHODSW(FaxPortHandle: win32more.Windows.Win32.Foundation.HANDLE, RoutingMethod: POINTER(POINTER(win32more.Windows.Win32.Devices.Fax.FAX_ROUTING_METHODW)), MethodsReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
PFAXENUMROUTINGMETHODS = UnicodeAlias('PFAXENUMROUTINGMETHODSW')
@winfunctype_pointer
def PFAXFREEBUFFER(Buffer: VoidPtr) -> Void: ...
@winfunctype_pointer
def PFAXGETCONFIGURATIONA(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, FaxConfig: POINTER(POINTER(win32more.Windows.Win32.Devices.Fax.FAX_CONFIGURATIONA))) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXGETCONFIGURATIONW(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, FaxConfig: POINTER(POINTER(win32more.Windows.Win32.Devices.Fax.FAX_CONFIGURATIONW))) -> win32more.Windows.Win32.Foundation.BOOL: ...
PFAXGETCONFIGURATION = UnicodeAlias('PFAXGETCONFIGURATIONW')
@winfunctype_pointer
def PFAXGETDEVICESTATUSA(FaxPortHandle: win32more.Windows.Win32.Foundation.HANDLE, DeviceStatus: POINTER(POINTER(win32more.Windows.Win32.Devices.Fax.FAX_DEVICE_STATUSA))) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXGETDEVICESTATUSW(FaxPortHandle: win32more.Windows.Win32.Foundation.HANDLE, DeviceStatus: POINTER(POINTER(win32more.Windows.Win32.Devices.Fax.FAX_DEVICE_STATUSW))) -> win32more.Windows.Win32.Foundation.BOOL: ...
PFAXGETDEVICESTATUS = UnicodeAlias('PFAXGETDEVICESTATUSW')
@winfunctype_pointer
def PFAXGETJOBA(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, JobId: UInt32, JobEntry: POINTER(POINTER(win32more.Windows.Win32.Devices.Fax.FAX_JOB_ENTRYA))) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXGETJOBW(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, JobId: UInt32, JobEntry: POINTER(POINTER(win32more.Windows.Win32.Devices.Fax.FAX_JOB_ENTRYW))) -> win32more.Windows.Win32.Foundation.BOOL: ...
PFAXGETJOB = UnicodeAlias('PFAXGETJOBW')
@winfunctype_pointer
def PFAXGETLOGGINGCATEGORIESA(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, Categories: POINTER(POINTER(win32more.Windows.Win32.Devices.Fax.FAX_LOG_CATEGORYA)), NumberCategories: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXGETLOGGINGCATEGORIESW(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, Categories: POINTER(POINTER(win32more.Windows.Win32.Devices.Fax.FAX_LOG_CATEGORYW)), NumberCategories: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
PFAXGETLOGGINGCATEGORIES = UnicodeAlias('PFAXGETLOGGINGCATEGORIESW')
@winfunctype_pointer
def PFAXGETPAGEDATA(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, JobId: UInt32, Buffer: POINTER(POINTER(Byte)), BufferSize: POINTER(UInt32), ImageWidth: POINTER(UInt32), ImageHeight: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXGETPORTA(FaxPortHandle: win32more.Windows.Win32.Foundation.HANDLE, PortInfo: POINTER(POINTER(win32more.Windows.Win32.Devices.Fax.FAX_PORT_INFOA))) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXGETPORTW(FaxPortHandle: win32more.Windows.Win32.Foundation.HANDLE, PortInfo: POINTER(POINTER(win32more.Windows.Win32.Devices.Fax.FAX_PORT_INFOW))) -> win32more.Windows.Win32.Foundation.BOOL: ...
PFAXGETPORT = UnicodeAlias('PFAXGETPORTW')
@winfunctype_pointer
def PFAXGETROUTINGINFOA(FaxPortHandle: win32more.Windows.Win32.Foundation.HANDLE, RoutingGuid: win32more.Windows.Win32.Foundation.PSTR, RoutingInfoBuffer: POINTER(POINTER(Byte)), RoutingInfoBufferSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXGETROUTINGINFOW(FaxPortHandle: win32more.Windows.Win32.Foundation.HANDLE, RoutingGuid: win32more.Windows.Win32.Foundation.PWSTR, RoutingInfoBuffer: POINTER(POINTER(Byte)), RoutingInfoBufferSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
PFAXGETROUTINGINFO = UnicodeAlias('PFAXGETROUTINGINFOW')
@winfunctype_pointer
def PFAXINITIALIZEEVENTQUEUE(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, CompletionPort: win32more.Windows.Win32.Foundation.HANDLE, CompletionKey: UIntPtr, hWnd: win32more.Windows.Win32.Foundation.HWND, MessageStart: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXOPENPORT(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, DeviceId: UInt32, Flags: UInt32, FaxPortHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXPRINTCOVERPAGEA(FaxContextInfo: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_CONTEXT_INFOA), CoverPageInfo: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_COVERPAGE_INFOA)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXPRINTCOVERPAGEW(FaxContextInfo: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_CONTEXT_INFOW), CoverPageInfo: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_COVERPAGE_INFOW)) -> win32more.Windows.Win32.Foundation.BOOL: ...
PFAXPRINTCOVERPAGE = UnicodeAlias('PFAXPRINTCOVERPAGEW')
@winfunctype_pointer
def PFAXREGISTERROUTINGEXTENSIONW(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, ExtensionName: win32more.Windows.Win32.Foundation.PWSTR, FriendlyName: win32more.Windows.Win32.Foundation.PWSTR, ImageName: win32more.Windows.Win32.Foundation.PWSTR, CallBack: win32more.Windows.Win32.Devices.Fax.PFAX_ROUTING_INSTALLATION_CALLBACKW, Context: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXREGISTERSERVICEPROVIDERW(DeviceProvider: win32more.Windows.Win32.Foundation.PWSTR, FriendlyName: win32more.Windows.Win32.Foundation.PWSTR, ImageName: win32more.Windows.Win32.Foundation.PWSTR, TspName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXROUTEADDFILE(JobId: UInt32, FileName: win32more.Windows.Win32.Foundation.PWSTR, Guid: POINTER(Guid)) -> Int32: ...
@winfunctype_pointer
def PFAXROUTEDELETEFILE(JobId: UInt32, FileName: win32more.Windows.Win32.Foundation.PWSTR) -> Int32: ...
@winfunctype_pointer
def PFAXROUTEDEVICECHANGENOTIFICATION(param0: UInt32, param1: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXROUTEDEVICEENABLE(param0: win32more.Windows.Win32.Foundation.PWSTR, param1: UInt32, param2: Int32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXROUTEENUMFILE(JobId: UInt32, GuidOwner: POINTER(Guid), GuidCaller: POINTER(Guid), FileName: win32more.Windows.Win32.Foundation.PWSTR, Context: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXROUTEENUMFILES(JobId: UInt32, Guid: POINTER(Guid), FileEnumerator: win32more.Windows.Win32.Devices.Fax.PFAXROUTEENUMFILE, Context: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXROUTEGETFILE(JobId: UInt32, Index: UInt32, FileNameBuffer: win32more.Windows.Win32.Foundation.PWSTR, RequiredSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXROUTEGETROUTINGINFO(param0: win32more.Windows.Win32.Foundation.PWSTR, param1: UInt32, param2: POINTER(Byte), param3: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXROUTEINITIALIZE(param0: win32more.Windows.Win32.Foundation.HANDLE, param1: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_ROUTE_CALLBACKROUTINES)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXROUTEMETHOD(param0: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_ROUTE), param1: POINTER(VoidPtr), param2: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXROUTEMODIFYROUTINGDATA(JobId: UInt32, RoutingGuid: win32more.Windows.Win32.Foundation.PWSTR, RoutingData: POINTER(Byte), RoutingDataSize: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXROUTESETROUTINGINFO(param0: win32more.Windows.Win32.Foundation.PWSTR, param1: UInt32, param2: POINTER(Byte), param3: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXSENDDOCUMENTA(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, FileName: win32more.Windows.Win32.Foundation.PSTR, JobParams: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_JOB_PARAMA), CoverpageInfo: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_COVERPAGE_INFOA), FaxJobId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXSENDDOCUMENTFORBROADCASTA(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, FileName: win32more.Windows.Win32.Foundation.PSTR, FaxJobId: POINTER(UInt32), FaxRecipientCallback: win32more.Windows.Win32.Devices.Fax.PFAX_RECIPIENT_CALLBACKA, Context: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXSENDDOCUMENTFORBROADCASTW(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, FileName: win32more.Windows.Win32.Foundation.PWSTR, FaxJobId: POINTER(UInt32), FaxRecipientCallback: win32more.Windows.Win32.Devices.Fax.PFAX_RECIPIENT_CALLBACKW, Context: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
PFAXSENDDOCUMENTFORBROADCAST = UnicodeAlias('PFAXSENDDOCUMENTFORBROADCASTW')
@winfunctype_pointer
def PFAXSENDDOCUMENTW(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, FileName: win32more.Windows.Win32.Foundation.PWSTR, JobParams: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_JOB_PARAMW), CoverpageInfo: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_COVERPAGE_INFOW), FaxJobId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
PFAXSENDDOCUMENT = UnicodeAlias('PFAXSENDDOCUMENTW')
@winfunctype_pointer
def PFAXSETCONFIGURATIONA(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, FaxConfig: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_CONFIGURATIONA)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXSETCONFIGURATIONW(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, FaxConfig: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_CONFIGURATIONW)) -> win32more.Windows.Win32.Foundation.BOOL: ...
PFAXSETCONFIGURATION = UnicodeAlias('PFAXSETCONFIGURATIONW')
@winfunctype_pointer
def PFAXSETGLOBALROUTINGINFOA(FaxPortHandle: win32more.Windows.Win32.Foundation.HANDLE, RoutingInfo: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_GLOBAL_ROUTING_INFOA)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXSETGLOBALROUTINGINFOW(FaxPortHandle: win32more.Windows.Win32.Foundation.HANDLE, RoutingInfo: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_GLOBAL_ROUTING_INFOW)) -> win32more.Windows.Win32.Foundation.BOOL: ...
PFAXSETGLOBALROUTINGINFO = UnicodeAlias('PFAXSETGLOBALROUTINGINFOW')
@winfunctype_pointer
def PFAXSETJOBA(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, JobId: UInt32, Command: UInt32, JobEntry: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_JOB_ENTRYA)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXSETJOBW(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, JobId: UInt32, Command: UInt32, JobEntry: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_JOB_ENTRYW)) -> win32more.Windows.Win32.Foundation.BOOL: ...
PFAXSETJOB = UnicodeAlias('PFAXSETJOBW')
@winfunctype_pointer
def PFAXSETLOGGINGCATEGORIESA(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, Categories: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_LOG_CATEGORYA), NumberCategories: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXSETLOGGINGCATEGORIESW(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, Categories: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_LOG_CATEGORYW), NumberCategories: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
PFAXSETLOGGINGCATEGORIES = UnicodeAlias('PFAXSETLOGGINGCATEGORIESW')
@winfunctype_pointer
def PFAXSETPORTA(FaxPortHandle: win32more.Windows.Win32.Foundation.HANDLE, PortInfo: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_PORT_INFOA)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXSETPORTW(FaxPortHandle: win32more.Windows.Win32.Foundation.HANDLE, PortInfo: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_PORT_INFOW)) -> win32more.Windows.Win32.Foundation.BOOL: ...
PFAXSETPORT = UnicodeAlias('PFAXSETPORTW')
@winfunctype_pointer
def PFAXSETROUTINGINFOA(FaxPortHandle: win32more.Windows.Win32.Foundation.HANDLE, RoutingGuid: win32more.Windows.Win32.Foundation.PSTR, RoutingInfoBuffer: POINTER(Byte), RoutingInfoBufferSize: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXSETROUTINGINFOW(FaxPortHandle: win32more.Windows.Win32.Foundation.HANDLE, RoutingGuid: win32more.Windows.Win32.Foundation.PWSTR, RoutingInfoBuffer: POINTER(Byte), RoutingInfoBufferSize: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
PFAXSETROUTINGINFO = UnicodeAlias('PFAXSETROUTINGINFOW')
@winfunctype_pointer
def PFAXSTARTPRINTJOBA(PrinterName: win32more.Windows.Win32.Foundation.PSTR, PrintInfo: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_PRINT_INFOA), FaxJobId: POINTER(UInt32), FaxContextInfo: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_CONTEXT_INFOA)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAXSTARTPRINTJOBW(PrinterName: win32more.Windows.Win32.Foundation.PWSTR, PrintInfo: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_PRINT_INFOW), FaxJobId: POINTER(UInt32), FaxContextInfo: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_CONTEXT_INFOW)) -> win32more.Windows.Win32.Foundation.BOOL: ...
PFAXSTARTPRINTJOB = UnicodeAlias('PFAXSTARTPRINTJOBW')
@winfunctype_pointer
def PFAXUNREGISTERSERVICEPROVIDERW(DeviceProvider: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAX_EXT_CONFIG_CHANGE(param0: UInt32, param1: win32more.Windows.Win32.Foundation.PWSTR, param2: POINTER(Byte), param3: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFAX_EXT_FREE_BUFFER(param0: VoidPtr) -> Void: ...
@winfunctype_pointer
def PFAX_EXT_GET_DATA(param0: UInt32, param1: win32more.Windows.Win32.Devices.Fax.FAX_ENUM_DEVICE_ID_SOURCE, param2: win32more.Windows.Win32.Foundation.PWSTR, param3: POINTER(POINTER(Byte)), param4: POINTER(UInt32)) -> UInt32: ...
@winfunctype_pointer
def PFAX_EXT_INITIALIZE_CONFIG(param0: win32more.Windows.Win32.Devices.Fax.PFAX_EXT_GET_DATA, param1: win32more.Windows.Win32.Devices.Fax.PFAX_EXT_SET_DATA, param2: win32more.Windows.Win32.Devices.Fax.PFAX_EXT_REGISTER_FOR_EVENTS, param3: win32more.Windows.Win32.Devices.Fax.PFAX_EXT_UNREGISTER_FOR_EVENTS, param4: win32more.Windows.Win32.Devices.Fax.PFAX_EXT_FREE_BUFFER) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFAX_EXT_REGISTER_FOR_EVENTS(param0: win32more.Windows.Win32.Foundation.HINSTANCE, param1: UInt32, param2: win32more.Windows.Win32.Devices.Fax.FAX_ENUM_DEVICE_ID_SOURCE, param3: win32more.Windows.Win32.Foundation.PWSTR, param4: win32more.Windows.Win32.Devices.Fax.PFAX_EXT_CONFIG_CHANGE) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype_pointer
def PFAX_EXT_SET_DATA(param0: win32more.Windows.Win32.Foundation.HINSTANCE, param1: UInt32, param2: win32more.Windows.Win32.Devices.Fax.FAX_ENUM_DEVICE_ID_SOURCE, param3: win32more.Windows.Win32.Foundation.PWSTR, param4: POINTER(Byte), param5: UInt32) -> UInt32: ...
@winfunctype_pointer
def PFAX_EXT_UNREGISTER_FOR_EVENTS(param0: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype_pointer
def PFAX_LINECALLBACK(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, hDevice: UInt32, dwMessage: UInt32, dwInstance: UIntPtr, dwParam1: UIntPtr, dwParam2: UIntPtr, dwParam3: UIntPtr) -> Void: ...
@winfunctype_pointer
def PFAX_RECIPIENT_CALLBACKA(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, RecipientNumber: UInt32, Context: VoidPtr, JobParams: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_JOB_PARAMA), CoverpageInfo: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_COVERPAGE_INFOA)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAX_RECIPIENT_CALLBACKW(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, RecipientNumber: UInt32, Context: VoidPtr, JobParams: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_JOB_PARAMW), CoverpageInfo: POINTER(win32more.Windows.Win32.Devices.Fax.FAX_COVERPAGE_INFOW)) -> win32more.Windows.Win32.Foundation.BOOL: ...
PFAX_RECIPIENT_CALLBACK = UnicodeAlias('PFAX_RECIPIENT_CALLBACKW')
@winfunctype_pointer
def PFAX_ROUTING_INSTALLATION_CALLBACKW(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, Context: VoidPtr, MethodName: win32more.Windows.Win32.Foundation.PWSTR, FriendlyName: win32more.Windows.Win32.Foundation.PWSTR, FunctionName: win32more.Windows.Win32.Foundation.PWSTR, Guid: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAX_SEND_CALLBACK(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, CallHandle: UInt32, Reserved1: UInt32, Reserved2: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFAX_SERVICE_CALLBACK(FaxHandle: win32more.Windows.Win32.Foundation.HANDLE, DeviceId: UInt32, Param1: UIntPtr, Param2: UIntPtr, Param3: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
class STINOTIFY(Structure):
    dwSize: UInt32
    guidNotificationCode: Guid
    abNotificationData: Byte * 64
class STISUBSCRIBE(Structure):
    dwSize: UInt32
    dwFlags: UInt32
    dwFilter: UInt32
    hWndNotify: win32more.Windows.Win32.Foundation.HWND
    hEvent: win32more.Windows.Win32.Foundation.HANDLE
    uiNotificationMessage: UInt32
class STI_DEVICE_INFORMATIONW(Structure):
    dwSize: UInt32
    DeviceType: UInt32
    szDeviceInternalName: Char * 128
    DeviceCapabilitiesA: win32more.Windows.Win32.Devices.Fax.STI_DEV_CAPS
    dwHardwareConfiguration: UInt32
    pszVendorDescription: win32more.Windows.Win32.Foundation.PWSTR
    pszDeviceDescription: win32more.Windows.Win32.Foundation.PWSTR
    pszPortName: win32more.Windows.Win32.Foundation.PWSTR
    pszPropProvider: win32more.Windows.Win32.Foundation.PWSTR
    pszLocalName: win32more.Windows.Win32.Foundation.PWSTR
STI_DEVICE_MJ_TYPE = Int32
StiDeviceTypeDefault: win32more.Windows.Win32.Devices.Fax.STI_DEVICE_MJ_TYPE = 0
StiDeviceTypeScanner: win32more.Windows.Win32.Devices.Fax.STI_DEVICE_MJ_TYPE = 1
StiDeviceTypeDigitalCamera: win32more.Windows.Win32.Devices.Fax.STI_DEVICE_MJ_TYPE = 2
StiDeviceTypeStreamingVideo: win32more.Windows.Win32.Devices.Fax.STI_DEVICE_MJ_TYPE = 3
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
    sErrorInfo: win32more.Windows.Win32.Devices.Fax._ERROR_INFOW
class STI_USD_CAPS(Structure):
    dwVersion: UInt32
    dwGenericCaps: UInt32
class STI_WIA_DEVICE_INFORMATIONW(Structure):
    dwSize: UInt32
    DeviceType: UInt32
    szDeviceInternalName: Char * 128
    DeviceCapabilitiesA: win32more.Windows.Win32.Devices.Fax.STI_DEV_CAPS
    dwHardwareConfiguration: UInt32
    pszVendorDescription: win32more.Windows.Win32.Foundation.PWSTR
    pszDeviceDescription: win32more.Windows.Win32.Foundation.PWSTR
    pszPortName: win32more.Windows.Win32.Foundation.PWSTR
    pszPropProvider: win32more.Windows.Win32.Foundation.PWSTR
    pszLocalName: win32more.Windows.Win32.Foundation.PWSTR
    pszUiDll: win32more.Windows.Win32.Foundation.PWSTR
    pszServer: win32more.Windows.Win32.Foundation.PWSTR
SendToMode = Int32
SEND_TO_FAX_RECIPIENT_ATTACHMENT: win32more.Windows.Win32.Devices.Fax.SendToMode = 0
class _ERROR_INFOW(Structure):
    dwSize: UInt32
    dwGenericError: UInt32
    dwVendorError: UInt32
    szExtendedErrorText: Char * 255


make_ready(__name__)
