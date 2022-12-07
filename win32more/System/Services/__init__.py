from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Security
import win32more.System.Registry
import win32more.System.Services
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
class _SC_NOTIFICATION_REGISTRATION(Structure):
    pass
SERVICE_ALL_ACCESS: UInt32 = 983551
SC_MANAGER_ALL_ACCESS: UInt32 = 983103
SERVICES_ACTIVE_DATABASEW: String = 'ServicesActive'
SERVICES_FAILED_DATABASEW: String = 'ServicesFailed'
SERVICES_ACTIVE_DATABASEA: String = 'ServicesActive'
SERVICES_FAILED_DATABASEA: String = 'ServicesFailed'
SERVICES_ACTIVE_DATABASE: String = 'ServicesActive'
SERVICES_FAILED_DATABASE: String = 'ServicesFailed'
SERVICE_NO_CHANGE: UInt32 = 4294967295
SERVICE_CONTROL_STOP: UInt32 = 1
SERVICE_CONTROL_PAUSE: UInt32 = 2
SERVICE_CONTROL_CONTINUE: UInt32 = 3
SERVICE_CONTROL_INTERROGATE: UInt32 = 4
SERVICE_CONTROL_SHUTDOWN: UInt32 = 5
SERVICE_CONTROL_PARAMCHANGE: UInt32 = 6
SERVICE_CONTROL_NETBINDADD: UInt32 = 7
SERVICE_CONTROL_NETBINDREMOVE: UInt32 = 8
SERVICE_CONTROL_NETBINDENABLE: UInt32 = 9
SERVICE_CONTROL_NETBINDDISABLE: UInt32 = 10
SERVICE_CONTROL_DEVICEEVENT: UInt32 = 11
SERVICE_CONTROL_HARDWAREPROFILECHANGE: UInt32 = 12
SERVICE_CONTROL_POWEREVENT: UInt32 = 13
SERVICE_CONTROL_SESSIONCHANGE: UInt32 = 14
SERVICE_CONTROL_PRESHUTDOWN: UInt32 = 15
SERVICE_CONTROL_TIMECHANGE: UInt32 = 16
SERVICE_CONTROL_TRIGGEREVENT: UInt32 = 32
SERVICE_CONTROL_LOWRESOURCES: UInt32 = 96
SERVICE_CONTROL_SYSTEMLOWRESOURCES: UInt32 = 97
SERVICE_ACCEPT_STOP: UInt32 = 1
SERVICE_ACCEPT_PAUSE_CONTINUE: UInt32 = 2
SERVICE_ACCEPT_SHUTDOWN: UInt32 = 4
SERVICE_ACCEPT_PARAMCHANGE: UInt32 = 8
SERVICE_ACCEPT_NETBINDCHANGE: UInt32 = 16
SERVICE_ACCEPT_HARDWAREPROFILECHANGE: UInt32 = 32
SERVICE_ACCEPT_POWEREVENT: UInt32 = 64
SERVICE_ACCEPT_SESSIONCHANGE: UInt32 = 128
SERVICE_ACCEPT_PRESHUTDOWN: UInt32 = 256
SERVICE_ACCEPT_TIMECHANGE: UInt32 = 512
SERVICE_ACCEPT_TRIGGEREVENT: UInt32 = 1024
SERVICE_ACCEPT_USER_LOGOFF: UInt32 = 2048
SERVICE_ACCEPT_LOWRESOURCES: UInt32 = 8192
SERVICE_ACCEPT_SYSTEMLOWRESOURCES: UInt32 = 16384
SC_MANAGER_CONNECT: UInt32 = 1
SC_MANAGER_CREATE_SERVICE: UInt32 = 2
SC_MANAGER_ENUMERATE_SERVICE: UInt32 = 4
SC_MANAGER_LOCK: UInt32 = 8
SC_MANAGER_QUERY_LOCK_STATUS: UInt32 = 16
SC_MANAGER_MODIFY_BOOT_CONFIG: UInt32 = 32
SERVICE_QUERY_CONFIG: UInt32 = 1
SERVICE_CHANGE_CONFIG: UInt32 = 2
SERVICE_QUERY_STATUS: UInt32 = 4
SERVICE_ENUMERATE_DEPENDENTS: UInt32 = 8
SERVICE_START: UInt32 = 16
SERVICE_STOP: UInt32 = 32
SERVICE_PAUSE_CONTINUE: UInt32 = 64
SERVICE_INTERROGATE: UInt32 = 128
SERVICE_USER_DEFINED_CONTROL: UInt32 = 256
SERVICE_NOTIFY_STATUS_CHANGE_1: UInt32 = 1
SERVICE_NOTIFY_STATUS_CHANGE_2: UInt32 = 2
SERVICE_NOTIFY_STATUS_CHANGE: UInt32 = 2
SERVICE_STOP_REASON_FLAG_MIN: UInt32 = 0
SERVICE_STOP_REASON_FLAG_UNPLANNED: UInt32 = 268435456
SERVICE_STOP_REASON_FLAG_CUSTOM: UInt32 = 536870912
SERVICE_STOP_REASON_FLAG_PLANNED: UInt32 = 1073741824
SERVICE_STOP_REASON_FLAG_MAX: UInt32 = 2147483648
SERVICE_STOP_REASON_MAJOR_MIN: UInt32 = 0
SERVICE_STOP_REASON_MAJOR_OTHER: UInt32 = 65536
SERVICE_STOP_REASON_MAJOR_HARDWARE: UInt32 = 131072
SERVICE_STOP_REASON_MAJOR_OPERATINGSYSTEM: UInt32 = 196608
SERVICE_STOP_REASON_MAJOR_SOFTWARE: UInt32 = 262144
SERVICE_STOP_REASON_MAJOR_APPLICATION: UInt32 = 327680
SERVICE_STOP_REASON_MAJOR_NONE: UInt32 = 393216
SERVICE_STOP_REASON_MAJOR_MAX: UInt32 = 458752
SERVICE_STOP_REASON_MAJOR_MIN_CUSTOM: UInt32 = 4194304
SERVICE_STOP_REASON_MAJOR_MAX_CUSTOM: UInt32 = 16711680
SERVICE_STOP_REASON_MINOR_MIN: UInt32 = 0
SERVICE_STOP_REASON_MINOR_OTHER: UInt32 = 1
SERVICE_STOP_REASON_MINOR_MAINTENANCE: UInt32 = 2
SERVICE_STOP_REASON_MINOR_INSTALLATION: UInt32 = 3
SERVICE_STOP_REASON_MINOR_UPGRADE: UInt32 = 4
SERVICE_STOP_REASON_MINOR_RECONFIG: UInt32 = 5
SERVICE_STOP_REASON_MINOR_HUNG: UInt32 = 6
SERVICE_STOP_REASON_MINOR_UNSTABLE: UInt32 = 7
SERVICE_STOP_REASON_MINOR_DISK: UInt32 = 8
SERVICE_STOP_REASON_MINOR_NETWORKCARD: UInt32 = 9
SERVICE_STOP_REASON_MINOR_ENVIRONMENT: UInt32 = 10
SERVICE_STOP_REASON_MINOR_HARDWARE_DRIVER: UInt32 = 11
SERVICE_STOP_REASON_MINOR_OTHERDRIVER: UInt32 = 12
SERVICE_STOP_REASON_MINOR_SERVICEPACK: UInt32 = 13
SERVICE_STOP_REASON_MINOR_SOFTWARE_UPDATE: UInt32 = 14
SERVICE_STOP_REASON_MINOR_SECURITYFIX: UInt32 = 15
SERVICE_STOP_REASON_MINOR_SECURITY: UInt32 = 16
SERVICE_STOP_REASON_MINOR_NETWORK_CONNECTIVITY: UInt32 = 17
SERVICE_STOP_REASON_MINOR_WMI: UInt32 = 18
SERVICE_STOP_REASON_MINOR_SERVICEPACK_UNINSTALL: UInt32 = 19
SERVICE_STOP_REASON_MINOR_SOFTWARE_UPDATE_UNINSTALL: UInt32 = 20
SERVICE_STOP_REASON_MINOR_SECURITYFIX_UNINSTALL: UInt32 = 21
SERVICE_STOP_REASON_MINOR_MMC: UInt32 = 22
SERVICE_STOP_REASON_MINOR_NONE: UInt32 = 23
SERVICE_STOP_REASON_MINOR_MEMOTYLIMIT: UInt32 = 24
SERVICE_STOP_REASON_MINOR_MAX: UInt32 = 25
SERVICE_STOP_REASON_MINOR_MIN_CUSTOM: UInt32 = 256
SERVICE_STOP_REASON_MINOR_MAX_CUSTOM: UInt32 = 65535
SERVICE_CONTROL_STATUS_REASON_INFO: UInt32 = 1
SERVICE_SID_TYPE_NONE: UInt32 = 0
SERVICE_SID_TYPE_UNRESTRICTED: UInt32 = 1
SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE: UInt32 = 7
SERVICE_TRIGGER_TYPE_AGGREGATE: UInt32 = 30
SERVICE_START_REASON_DEMAND: UInt32 = 1
SERVICE_START_REASON_AUTO: UInt32 = 2
SERVICE_START_REASON_TRIGGER: UInt32 = 4
SERVICE_START_REASON_RESTART_ON_FAILURE: UInt32 = 8
SERVICE_START_REASON_DELAYEDAUTO: UInt32 = 16
SERVICE_DYNAMIC_INFORMATION_LEVEL_START_REASON: UInt32 = 1
SERVICE_LAUNCH_PROTECTED_NONE: UInt32 = 0
SERVICE_LAUNCH_PROTECTED_WINDOWS: UInt32 = 1
SERVICE_LAUNCH_PROTECTED_WINDOWS_LIGHT: UInt32 = 2
SERVICE_LAUNCH_PROTECTED_ANTIMALWARE_LIGHT: UInt32 = 3
NETWORK_MANAGER_FIRST_IP_ADDRESS_ARRIVAL_GUID: Guid = Guid('4f27f2de-14e2-430b-a5-49-7c-d4-8c-bc-82-45')
NETWORK_MANAGER_LAST_IP_ADDRESS_REMOVAL_GUID: Guid = Guid('cc4ba62a-162e-4648-84-7a-b6-bd-f9-93-e3-35')
DOMAIN_JOIN_GUID: Guid = Guid('1ce20aba-9851-4421-94-30-1d-de-b7-66-e8-09')
DOMAIN_LEAVE_GUID: Guid = Guid('ddaf516e-58c2-4866-95-74-c3-b6-15-d4-2e-a1')
FIREWALL_PORT_OPEN_GUID: Guid = Guid('b7569e07-8421-4ee0-ad-10-86-91-5a-fd-ad-09')
FIREWALL_PORT_CLOSE_GUID: Guid = Guid('a144ed38-8e12-4de4-9d-96-e6-47-40-b1-a5-24')
MACHINE_POLICY_PRESENT_GUID: Guid = Guid('659fcae6-5bdb-4da9-b1-ff-ca-2a-17-8d-46-e0')
USER_POLICY_PRESENT_GUID: Guid = Guid('54fb46c8-f089-464c-b1-fd-59-d1-b6-2c-3b-50')
RPC_INTERFACE_EVENT_GUID: Guid = Guid('bc90d167-9470-4139-a9-ba-be-0b-bb-f5-b7-4d')
NAMED_PIPE_EVENT_GUID: Guid = Guid('1f81d131-3fac-4537-9e-0c-7e-7b-0c-2f-4b-55')
CUSTOM_SYSTEM_STATE_CHANGE_EVENT_GUID: Guid = Guid('2d7a2816-0c5e-45fc-9c-e7-57-0e-5e-cd-e9-c9')
SERVICE_TRIGGER_STARTED_ARGUMENT: String = 'TriggerStarted'
SC_AGGREGATE_STORAGE_KEY: String = 'System\\CurrentControlSet\\Control\\ServiceAggregatedEvents'
@winfunctype('ADVAPI32.dll')
def SetServiceBits(hServiceStatus: win32more.System.Services.SERVICE_STATUS_HANDLE, dwServiceBits: UInt32, bSetBitsOn: win32more.Foundation.BOOL, bUpdateImmediately: win32more.Foundation.BOOL) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ChangeServiceConfigA(hService: win32more.Security.SC_HANDLE, dwServiceType: UInt32, dwStartType: win32more.System.Services.SERVICE_START_TYPE, dwErrorControl: win32more.System.Services.SERVICE_ERROR, lpBinaryPathName: win32more.Foundation.PSTR, lpLoadOrderGroup: win32more.Foundation.PSTR, lpdwTagId: POINTER(UInt32), lpDependencies: win32more.Foundation.PSTR, lpServiceStartName: win32more.Foundation.PSTR, lpPassword: win32more.Foundation.PSTR, lpDisplayName: win32more.Foundation.PSTR) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ChangeServiceConfigW(hService: win32more.Security.SC_HANDLE, dwServiceType: UInt32, dwStartType: win32more.System.Services.SERVICE_START_TYPE, dwErrorControl: win32more.System.Services.SERVICE_ERROR, lpBinaryPathName: win32more.Foundation.PWSTR, lpLoadOrderGroup: win32more.Foundation.PWSTR, lpdwTagId: POINTER(UInt32), lpDependencies: win32more.Foundation.PWSTR, lpServiceStartName: win32more.Foundation.PWSTR, lpPassword: win32more.Foundation.PWSTR, lpDisplayName: win32more.Foundation.PWSTR) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ChangeServiceConfig2A(hService: win32more.Security.SC_HANDLE, dwInfoLevel: win32more.System.Services.SERVICE_CONFIG, lpInfo: c_void_p) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ChangeServiceConfig2W(hService: win32more.Security.SC_HANDLE, dwInfoLevel: win32more.System.Services.SERVICE_CONFIG, lpInfo: c_void_p) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CloseServiceHandle(hSCObject: win32more.Security.SC_HANDLE) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ControlService(hService: win32more.Security.SC_HANDLE, dwControl: UInt32, lpServiceStatus: POINTER(win32more.System.Services.SERVICE_STATUS_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CreateServiceA(hSCManager: win32more.Security.SC_HANDLE, lpServiceName: win32more.Foundation.PSTR, lpDisplayName: win32more.Foundation.PSTR, dwDesiredAccess: UInt32, dwServiceType: win32more.System.Services.ENUM_SERVICE_TYPE, dwStartType: win32more.System.Services.SERVICE_START_TYPE, dwErrorControl: win32more.System.Services.SERVICE_ERROR, lpBinaryPathName: win32more.Foundation.PSTR, lpLoadOrderGroup: win32more.Foundation.PSTR, lpdwTagId: POINTER(UInt32), lpDependencies: win32more.Foundation.PSTR, lpServiceStartName: win32more.Foundation.PSTR, lpPassword: win32more.Foundation.PSTR) -> win32more.Security.SC_HANDLE: ...
@winfunctype('ADVAPI32.dll')
def CreateServiceW(hSCManager: win32more.Security.SC_HANDLE, lpServiceName: win32more.Foundation.PWSTR, lpDisplayName: win32more.Foundation.PWSTR, dwDesiredAccess: UInt32, dwServiceType: win32more.System.Services.ENUM_SERVICE_TYPE, dwStartType: win32more.System.Services.SERVICE_START_TYPE, dwErrorControl: win32more.System.Services.SERVICE_ERROR, lpBinaryPathName: win32more.Foundation.PWSTR, lpLoadOrderGroup: win32more.Foundation.PWSTR, lpdwTagId: POINTER(UInt32), lpDependencies: win32more.Foundation.PWSTR, lpServiceStartName: win32more.Foundation.PWSTR, lpPassword: win32more.Foundation.PWSTR) -> win32more.Security.SC_HANDLE: ...
@winfunctype('ADVAPI32.dll')
def DeleteService(hService: win32more.Security.SC_HANDLE) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def EnumDependentServicesA(hService: win32more.Security.SC_HANDLE, dwServiceState: win32more.System.Services.ENUM_SERVICE_STATE, lpServices: POINTER(win32more.System.Services.ENUM_SERVICE_STATUSA_head), cbBufSize: UInt32, pcbBytesNeeded: POINTER(UInt32), lpServicesReturned: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def EnumDependentServicesW(hService: win32more.Security.SC_HANDLE, dwServiceState: win32more.System.Services.ENUM_SERVICE_STATE, lpServices: POINTER(win32more.System.Services.ENUM_SERVICE_STATUSW_head), cbBufSize: UInt32, pcbBytesNeeded: POINTER(UInt32), lpServicesReturned: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def EnumServicesStatusA(hSCManager: win32more.Security.SC_HANDLE, dwServiceType: win32more.System.Services.ENUM_SERVICE_TYPE, dwServiceState: win32more.System.Services.ENUM_SERVICE_STATE, lpServices: POINTER(win32more.System.Services.ENUM_SERVICE_STATUSA_head), cbBufSize: UInt32, pcbBytesNeeded: POINTER(UInt32), lpServicesReturned: POINTER(UInt32), lpResumeHandle: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def EnumServicesStatusW(hSCManager: win32more.Security.SC_HANDLE, dwServiceType: win32more.System.Services.ENUM_SERVICE_TYPE, dwServiceState: win32more.System.Services.ENUM_SERVICE_STATE, lpServices: POINTER(win32more.System.Services.ENUM_SERVICE_STATUSW_head), cbBufSize: UInt32, pcbBytesNeeded: POINTER(UInt32), lpServicesReturned: POINTER(UInt32), lpResumeHandle: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def EnumServicesStatusExA(hSCManager: win32more.Security.SC_HANDLE, InfoLevel: win32more.System.Services.SC_ENUM_TYPE, dwServiceType: win32more.System.Services.ENUM_SERVICE_TYPE, dwServiceState: win32more.System.Services.ENUM_SERVICE_STATE, lpServices: c_char_p_no, cbBufSize: UInt32, pcbBytesNeeded: POINTER(UInt32), lpServicesReturned: POINTER(UInt32), lpResumeHandle: POINTER(UInt32), pszGroupName: win32more.Foundation.PSTR) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def EnumServicesStatusExW(hSCManager: win32more.Security.SC_HANDLE, InfoLevel: win32more.System.Services.SC_ENUM_TYPE, dwServiceType: win32more.System.Services.ENUM_SERVICE_TYPE, dwServiceState: win32more.System.Services.ENUM_SERVICE_STATE, lpServices: c_char_p_no, cbBufSize: UInt32, pcbBytesNeeded: POINTER(UInt32), lpServicesReturned: POINTER(UInt32), lpResumeHandle: POINTER(UInt32), pszGroupName: win32more.Foundation.PWSTR) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def GetServiceKeyNameA(hSCManager: win32more.Security.SC_HANDLE, lpDisplayName: win32more.Foundation.PSTR, lpServiceName: win32more.Foundation.PSTR, lpcchBuffer: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def GetServiceKeyNameW(hSCManager: win32more.Security.SC_HANDLE, lpDisplayName: win32more.Foundation.PWSTR, lpServiceName: win32more.Foundation.PWSTR, lpcchBuffer: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def GetServiceDisplayNameA(hSCManager: win32more.Security.SC_HANDLE, lpServiceName: win32more.Foundation.PSTR, lpDisplayName: win32more.Foundation.PSTR, lpcchBuffer: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def GetServiceDisplayNameW(hSCManager: win32more.Security.SC_HANDLE, lpServiceName: win32more.Foundation.PWSTR, lpDisplayName: win32more.Foundation.PWSTR, lpcchBuffer: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def LockServiceDatabase(hSCManager: win32more.Security.SC_HANDLE) -> c_void_p: ...
@winfunctype('ADVAPI32.dll')
def NotifyBootConfigStatus(BootAcceptable: win32more.Foundation.BOOL) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def OpenSCManagerA(lpMachineName: win32more.Foundation.PSTR, lpDatabaseName: win32more.Foundation.PSTR, dwDesiredAccess: UInt32) -> win32more.Security.SC_HANDLE: ...
@winfunctype('ADVAPI32.dll')
def OpenSCManagerW(lpMachineName: win32more.Foundation.PWSTR, lpDatabaseName: win32more.Foundation.PWSTR, dwDesiredAccess: UInt32) -> win32more.Security.SC_HANDLE: ...
@winfunctype('ADVAPI32.dll')
def OpenServiceA(hSCManager: win32more.Security.SC_HANDLE, lpServiceName: win32more.Foundation.PSTR, dwDesiredAccess: UInt32) -> win32more.Security.SC_HANDLE: ...
@winfunctype('ADVAPI32.dll')
def OpenServiceW(hSCManager: win32more.Security.SC_HANDLE, lpServiceName: win32more.Foundation.PWSTR, dwDesiredAccess: UInt32) -> win32more.Security.SC_HANDLE: ...
@winfunctype('ADVAPI32.dll')
def QueryServiceConfigA(hService: win32more.Security.SC_HANDLE, lpServiceConfig: POINTER(win32more.System.Services.QUERY_SERVICE_CONFIGA_head), cbBufSize: UInt32, pcbBytesNeeded: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def QueryServiceConfigW(hService: win32more.Security.SC_HANDLE, lpServiceConfig: POINTER(win32more.System.Services.QUERY_SERVICE_CONFIGW_head), cbBufSize: UInt32, pcbBytesNeeded: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def QueryServiceConfig2A(hService: win32more.Security.SC_HANDLE, dwInfoLevel: win32more.System.Services.SERVICE_CONFIG, lpBuffer: c_char_p_no, cbBufSize: UInt32, pcbBytesNeeded: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def QueryServiceConfig2W(hService: win32more.Security.SC_HANDLE, dwInfoLevel: win32more.System.Services.SERVICE_CONFIG, lpBuffer: c_char_p_no, cbBufSize: UInt32, pcbBytesNeeded: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def QueryServiceLockStatusA(hSCManager: win32more.Security.SC_HANDLE, lpLockStatus: POINTER(win32more.System.Services.QUERY_SERVICE_LOCK_STATUSA_head), cbBufSize: UInt32, pcbBytesNeeded: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def QueryServiceLockStatusW(hSCManager: win32more.Security.SC_HANDLE, lpLockStatus: POINTER(win32more.System.Services.QUERY_SERVICE_LOCK_STATUSW_head), cbBufSize: UInt32, pcbBytesNeeded: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def QueryServiceObjectSecurity(hService: win32more.Security.SC_HANDLE, dwSecurityInformation: UInt32, lpSecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR, cbBufSize: UInt32, pcbBytesNeeded: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def QueryServiceStatus(hService: win32more.Security.SC_HANDLE, lpServiceStatus: POINTER(win32more.System.Services.SERVICE_STATUS_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def QueryServiceStatusEx(hService: win32more.Security.SC_HANDLE, InfoLevel: win32more.System.Services.SC_STATUS_TYPE, lpBuffer: c_char_p_no, cbBufSize: UInt32, pcbBytesNeeded: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def RegisterServiceCtrlHandlerA(lpServiceName: win32more.Foundation.PSTR, lpHandlerProc: win32more.System.Services.LPHANDLER_FUNCTION) -> win32more.System.Services.SERVICE_STATUS_HANDLE: ...
@winfunctype('ADVAPI32.dll')
def RegisterServiceCtrlHandlerW(lpServiceName: win32more.Foundation.PWSTR, lpHandlerProc: win32more.System.Services.LPHANDLER_FUNCTION) -> win32more.System.Services.SERVICE_STATUS_HANDLE: ...
@winfunctype('ADVAPI32.dll')
def RegisterServiceCtrlHandlerExA(lpServiceName: win32more.Foundation.PSTR, lpHandlerProc: win32more.System.Services.LPHANDLER_FUNCTION_EX, lpContext: c_void_p) -> win32more.System.Services.SERVICE_STATUS_HANDLE: ...
@winfunctype('ADVAPI32.dll')
def RegisterServiceCtrlHandlerExW(lpServiceName: win32more.Foundation.PWSTR, lpHandlerProc: win32more.System.Services.LPHANDLER_FUNCTION_EX, lpContext: c_void_p) -> win32more.System.Services.SERVICE_STATUS_HANDLE: ...
@winfunctype('ADVAPI32.dll')
def SetServiceObjectSecurity(hService: win32more.Security.SC_HANDLE, dwSecurityInformation: win32more.Security.OBJECT_SECURITY_INFORMATION, lpSecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def SetServiceStatus(hServiceStatus: win32more.System.Services.SERVICE_STATUS_HANDLE, lpServiceStatus: POINTER(win32more.System.Services.SERVICE_STATUS_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def StartServiceCtrlDispatcherA(lpServiceStartTable: POINTER(win32more.System.Services.SERVICE_TABLE_ENTRYA_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def StartServiceCtrlDispatcherW(lpServiceStartTable: POINTER(win32more.System.Services.SERVICE_TABLE_ENTRYW_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def StartServiceA(hService: win32more.Security.SC_HANDLE, dwNumServiceArgs: UInt32, lpServiceArgVectors: POINTER(win32more.Foundation.PSTR)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def StartServiceW(hService: win32more.Security.SC_HANDLE, dwNumServiceArgs: UInt32, lpServiceArgVectors: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def UnlockServiceDatabase(ScLock: c_void_p) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def NotifyServiceStatusChangeA(hService: win32more.Security.SC_HANDLE, dwNotifyMask: win32more.System.Services.SERVICE_NOTIFY, pNotifyBuffer: POINTER(win32more.System.Services.SERVICE_NOTIFY_2A_head)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def NotifyServiceStatusChangeW(hService: win32more.Security.SC_HANDLE, dwNotifyMask: win32more.System.Services.SERVICE_NOTIFY, pNotifyBuffer: POINTER(win32more.System.Services.SERVICE_NOTIFY_2W_head)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def ControlServiceExA(hService: win32more.Security.SC_HANDLE, dwControl: UInt32, dwInfoLevel: UInt32, pControlParams: c_void_p) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ControlServiceExW(hService: win32more.Security.SC_HANDLE, dwControl: UInt32, dwInfoLevel: UInt32, pControlParams: c_void_p) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def QueryServiceDynamicInformation(hServiceStatus: win32more.System.Services.SERVICE_STATUS_HANDLE, dwInfoLevel: UInt32, ppDynamicInfo: POINTER(c_void_p)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def WaitServiceState(hService: win32more.Security.SC_HANDLE, dwNotify: UInt32, dwTimeout: UInt32, hCancelEvent: win32more.Foundation.HANDLE) -> UInt32: ...
@winfunctype('api-ms-win-service-core-l1-1-3.dll')
def GetServiceRegistryStateKey(ServiceStatusHandle: win32more.System.Services.SERVICE_STATUS_HANDLE, StateType: win32more.System.Services.SERVICE_REGISTRY_STATE_TYPE, AccessMask: UInt32, ServiceStateKey: POINTER(win32more.System.Registry.HKEY)) -> UInt32: ...
@winfunctype('api-ms-win-service-core-l1-1-4.dll')
def GetServiceDirectory(hServiceStatus: win32more.System.Services.SERVICE_STATUS_HANDLE, eDirectoryType: win32more.System.Services.SERVICE_DIRECTORY_TYPE, lpPathBuffer: win32more.Foundation.PWSTR, cchPathBufferLength: UInt32, lpcchRequiredBufferLength: POINTER(UInt32)) -> UInt32: ...
@winfunctype('api-ms-win-service-core-l1-1-5.dll')
def GetSharedServiceRegistryStateKey(ServiceHandle: win32more.Security.SC_HANDLE, StateType: win32more.System.Services.SERVICE_SHARED_REGISTRY_STATE_TYPE, AccessMask: UInt32, ServiceStateKey: POINTER(win32more.System.Registry.HKEY)) -> UInt32: ...
@winfunctype('api-ms-win-service-core-l1-1-5.dll')
def GetSharedServiceDirectory(ServiceHandle: win32more.Security.SC_HANDLE, DirectoryType: win32more.System.Services.SERVICE_SHARED_DIRECTORY_TYPE, PathBuffer: win32more.Foundation.PWSTR, PathBufferLength: UInt32, RequiredBufferLength: POINTER(UInt32)) -> UInt32: ...
ENUM_SERVICE_STATE = UInt32
SERVICE_ACTIVE: ENUM_SERVICE_STATE = 1
SERVICE_INACTIVE: ENUM_SERVICE_STATE = 2
SERVICE_STATE_ALL: ENUM_SERVICE_STATE = 3
class ENUM_SERVICE_STATUS_PROCESSA(Structure):
    lpServiceName: win32more.Foundation.PSTR
    lpDisplayName: win32more.Foundation.PSTR
    ServiceStatusProcess: win32more.System.Services.SERVICE_STATUS_PROCESS
class ENUM_SERVICE_STATUS_PROCESSW(Structure):
    lpServiceName: win32more.Foundation.PWSTR
    lpDisplayName: win32more.Foundation.PWSTR
    ServiceStatusProcess: win32more.System.Services.SERVICE_STATUS_PROCESS
class ENUM_SERVICE_STATUSA(Structure):
    lpServiceName: win32more.Foundation.PSTR
    lpDisplayName: win32more.Foundation.PSTR
    ServiceStatus: win32more.System.Services.SERVICE_STATUS
class ENUM_SERVICE_STATUSW(Structure):
    lpServiceName: win32more.Foundation.PWSTR
    lpDisplayName: win32more.Foundation.PWSTR
    ServiceStatus: win32more.System.Services.SERVICE_STATUS
ENUM_SERVICE_TYPE = UInt32
SERVICE_DRIVER: ENUM_SERVICE_TYPE = 11
SERVICE_KERNEL_DRIVER: ENUM_SERVICE_TYPE = 1
SERVICE_WIN32: ENUM_SERVICE_TYPE = 48
SERVICE_WIN32_SHARE_PROCESS: ENUM_SERVICE_TYPE = 32
SERVICE_ADAPTER: ENUM_SERVICE_TYPE = 4
SERVICE_FILE_SYSTEM_DRIVER: ENUM_SERVICE_TYPE = 2
SERVICE_RECOGNIZER_DRIVER: ENUM_SERVICE_TYPE = 8
SERVICE_WIN32_OWN_PROCESS: ENUM_SERVICE_TYPE = 16
SERVICE_USER_OWN_PROCESS: ENUM_SERVICE_TYPE = 80
SERVICE_USER_SHARE_PROCESS: ENUM_SERVICE_TYPE = 96
@winfunctype_pointer
def HANDLER_FUNCTION(dwControl: UInt32) -> Void: ...
@winfunctype_pointer
def HANDLER_FUNCTION_EX(dwControl: UInt32, dwEventType: UInt32, lpEventData: c_void_p, lpContext: c_void_p) -> UInt32: ...
@winfunctype_pointer
def LPHANDLER_FUNCTION(dwControl: UInt32) -> Void: ...
@winfunctype_pointer
def LPHANDLER_FUNCTION_EX(dwControl: UInt32, dwEventType: UInt32, lpEventData: c_void_p, lpContext: c_void_p) -> UInt32: ...
@winfunctype_pointer
def LPSERVICE_MAIN_FUNCTIONA(dwNumServicesArgs: UInt32, lpServiceArgVectors: POINTER(win32more.Foundation.PSTR)) -> Void: ...
@winfunctype_pointer
def LPSERVICE_MAIN_FUNCTIONW(dwNumServicesArgs: UInt32, lpServiceArgVectors: POINTER(win32more.Foundation.PWSTR)) -> Void: ...
@winfunctype_pointer
def PFN_SC_NOTIFY_CALLBACK(pParameter: c_void_p) -> Void: ...
@winfunctype_pointer
def PSC_NOTIFICATION_CALLBACK(dwNotify: UInt32, pCallbackContext: c_void_p) -> Void: ...
class QUERY_SERVICE_CONFIGA(Structure):
    dwServiceType: win32more.System.Services.ENUM_SERVICE_TYPE
    dwStartType: win32more.System.Services.SERVICE_START_TYPE
    dwErrorControl: win32more.System.Services.SERVICE_ERROR
    lpBinaryPathName: win32more.Foundation.PSTR
    lpLoadOrderGroup: win32more.Foundation.PSTR
    dwTagId: UInt32
    lpDependencies: win32more.Foundation.PSTR
    lpServiceStartName: win32more.Foundation.PSTR
    lpDisplayName: win32more.Foundation.PSTR
class QUERY_SERVICE_CONFIGW(Structure):
    dwServiceType: win32more.System.Services.ENUM_SERVICE_TYPE
    dwStartType: win32more.System.Services.SERVICE_START_TYPE
    dwErrorControl: win32more.System.Services.SERVICE_ERROR
    lpBinaryPathName: win32more.Foundation.PWSTR
    lpLoadOrderGroup: win32more.Foundation.PWSTR
    dwTagId: UInt32
    lpDependencies: win32more.Foundation.PWSTR
    lpServiceStartName: win32more.Foundation.PWSTR
    lpDisplayName: win32more.Foundation.PWSTR
class QUERY_SERVICE_LOCK_STATUSA(Structure):
    fIsLocked: UInt32
    lpLockOwner: win32more.Foundation.PSTR
    dwLockDuration: UInt32
class QUERY_SERVICE_LOCK_STATUSW(Structure):
    fIsLocked: UInt32
    lpLockOwner: win32more.Foundation.PWSTR
    dwLockDuration: UInt32
class SC_ACTION(Structure):
    Type: win32more.System.Services.SC_ACTION_TYPE
    Delay: UInt32
SC_ACTION_TYPE = Int32
SC_ACTION_NONE: SC_ACTION_TYPE = 0
SC_ACTION_RESTART: SC_ACTION_TYPE = 1
SC_ACTION_REBOOT: SC_ACTION_TYPE = 2
SC_ACTION_RUN_COMMAND: SC_ACTION_TYPE = 3
SC_ACTION_OWN_RESTART: SC_ACTION_TYPE = 4
SC_ENUM_TYPE = Int32
SC_ENUM_PROCESS_INFO: SC_ENUM_TYPE = 0
SC_EVENT_TYPE = Int32
SC_EVENT_DATABASE_CHANGE: SC_EVENT_TYPE = 0
SC_EVENT_PROPERTY_CHANGE: SC_EVENT_TYPE = 1
SC_EVENT_STATUS_CHANGE: SC_EVENT_TYPE = 2
SC_STATUS_TYPE = Int32
SC_STATUS_PROCESS_INFO: SC_STATUS_TYPE = 0
SERVICE_CONFIG = UInt32
SERVICE_CONFIG_DELAYED_AUTO_START_INFO: SERVICE_CONFIG = 3
SERVICE_CONFIG_DESCRIPTION: SERVICE_CONFIG = 1
SERVICE_CONFIG_FAILURE_ACTIONS: SERVICE_CONFIG = 2
SERVICE_CONFIG_FAILURE_ACTIONS_FLAG: SERVICE_CONFIG = 4
SERVICE_CONFIG_PREFERRED_NODE: SERVICE_CONFIG = 9
SERVICE_CONFIG_PRESHUTDOWN_INFO: SERVICE_CONFIG = 7
SERVICE_CONFIG_REQUIRED_PRIVILEGES_INFO: SERVICE_CONFIG = 6
SERVICE_CONFIG_SERVICE_SID_INFO: SERVICE_CONFIG = 5
SERVICE_CONFIG_TRIGGER_INFO: SERVICE_CONFIG = 8
SERVICE_CONFIG_LAUNCH_PROTECTED: SERVICE_CONFIG = 12
class SERVICE_CONTROL_STATUS_REASON_PARAMSA(Structure):
    dwReason: UInt32
    pszComment: win32more.Foundation.PSTR
    ServiceStatus: win32more.System.Services.SERVICE_STATUS_PROCESS
class SERVICE_CONTROL_STATUS_REASON_PARAMSW(Structure):
    dwReason: UInt32
    pszComment: win32more.Foundation.PWSTR
    ServiceStatus: win32more.System.Services.SERVICE_STATUS_PROCESS
class SERVICE_CUSTOM_SYSTEM_STATE_CHANGE_DATA_ITEM(Structure):
    u: _u_e__Union
    class _u_e__Union(Union):
        CustomStateId: win32more.System.Services.SERVICE_TRIGGER_CUSTOM_STATE_ID
        s: _s_e__Struct
        class _s_e__Struct(Structure):
            DataOffset: UInt32
            Data: Byte * 1
class SERVICE_DELAYED_AUTO_START_INFO(Structure):
    fDelayedAutostart: win32more.Foundation.BOOL
class SERVICE_DESCRIPTIONA(Structure):
    lpDescription: win32more.Foundation.PSTR
class SERVICE_DESCRIPTIONW(Structure):
    lpDescription: win32more.Foundation.PWSTR
SERVICE_DIRECTORY_TYPE = Int32
SERVICE_DIRECTORY_TYPE_ServiceDirectoryPersistentState: SERVICE_DIRECTORY_TYPE = 0
SERVICE_DIRECTORY_TYPE_ServiceDirectoryTypeMax: SERVICE_DIRECTORY_TYPE = 1
SERVICE_ERROR = UInt32
SERVICE_ERROR_CRITICAL: SERVICE_ERROR = 3
SERVICE_ERROR_IGNORE: SERVICE_ERROR = 0
SERVICE_ERROR_NORMAL: SERVICE_ERROR = 1
SERVICE_ERROR_SEVERE: SERVICE_ERROR = 2
class SERVICE_FAILURE_ACTIONS_FLAG(Structure):
    fFailureActionsOnNonCrashFailures: win32more.Foundation.BOOL
class SERVICE_FAILURE_ACTIONSA(Structure):
    dwResetPeriod: UInt32
    lpRebootMsg: win32more.Foundation.PSTR
    lpCommand: win32more.Foundation.PSTR
    cActions: UInt32
    lpsaActions: POINTER(win32more.System.Services.SC_ACTION_head)
class SERVICE_FAILURE_ACTIONSW(Structure):
    dwResetPeriod: UInt32
    lpRebootMsg: win32more.Foundation.PWSTR
    lpCommand: win32more.Foundation.PWSTR
    cActions: UInt32
    lpsaActions: POINTER(win32more.System.Services.SC_ACTION_head)
class SERVICE_LAUNCH_PROTECTED_INFO(Structure):
    dwLaunchProtected: UInt32
@winfunctype_pointer
def SERVICE_MAIN_FUNCTIONA(dwNumServicesArgs: UInt32, lpServiceArgVectors: POINTER(POINTER(SByte))) -> Void: ...
@winfunctype_pointer
def SERVICE_MAIN_FUNCTIONW(dwNumServicesArgs: UInt32, lpServiceArgVectors: POINTER(win32more.Foundation.PWSTR)) -> Void: ...
SERVICE_NOTIFY = UInt32
SERVICE_NOTIFY_CREATED: SERVICE_NOTIFY = 128
SERVICE_NOTIFY_CONTINUE_PENDING: SERVICE_NOTIFY = 16
SERVICE_NOTIFY_DELETE_PENDING: SERVICE_NOTIFY = 512
SERVICE_NOTIFY_DELETED: SERVICE_NOTIFY = 256
SERVICE_NOTIFY_PAUSE_PENDING: SERVICE_NOTIFY = 32
SERVICE_NOTIFY_PAUSED: SERVICE_NOTIFY = 64
SERVICE_NOTIFY_RUNNING: SERVICE_NOTIFY = 8
SERVICE_NOTIFY_START_PENDING: SERVICE_NOTIFY = 2
SERVICE_NOTIFY_STOP_PENDING: SERVICE_NOTIFY = 4
SERVICE_NOTIFY_STOPPED: SERVICE_NOTIFY = 1
class SERVICE_NOTIFY_1(Structure):
    dwVersion: UInt32
    pfnNotifyCallback: win32more.System.Services.PFN_SC_NOTIFY_CALLBACK
    pContext: c_void_p
    dwNotificationStatus: UInt32
    ServiceStatus: win32more.System.Services.SERVICE_STATUS_PROCESS
class SERVICE_NOTIFY_2A(Structure):
    dwVersion: UInt32
    pfnNotifyCallback: win32more.System.Services.PFN_SC_NOTIFY_CALLBACK
    pContext: c_void_p
    dwNotificationStatus: UInt32
    ServiceStatus: win32more.System.Services.SERVICE_STATUS_PROCESS
    dwNotificationTriggered: UInt32
    pszServiceNames: win32more.Foundation.PSTR
class SERVICE_NOTIFY_2W(Structure):
    dwVersion: UInt32
    pfnNotifyCallback: win32more.System.Services.PFN_SC_NOTIFY_CALLBACK
    pContext: c_void_p
    dwNotificationStatus: UInt32
    ServiceStatus: win32more.System.Services.SERVICE_STATUS_PROCESS
    dwNotificationTriggered: UInt32
    pszServiceNames: win32more.Foundation.PWSTR
class SERVICE_PREFERRED_NODE_INFO(Structure):
    usPreferredNode: UInt16
    fDelete: win32more.Foundation.BOOLEAN
class SERVICE_PRESHUTDOWN_INFO(Structure):
    dwPreshutdownTimeout: UInt32
SERVICE_REGISTRY_STATE_TYPE = Int32
SERVICE_REGISTRY_STATE_TYPE_ServiceRegistryStateParameters: SERVICE_REGISTRY_STATE_TYPE = 0
SERVICE_REGISTRY_STATE_TYPE_ServiceRegistryStatePersistent: SERVICE_REGISTRY_STATE_TYPE = 1
SERVICE_REGISTRY_STATE_TYPE_MaxServiceRegistryStateType: SERVICE_REGISTRY_STATE_TYPE = 2
class SERVICE_REQUIRED_PRIVILEGES_INFOA(Structure):
    pmszRequiredPrivileges: win32more.Foundation.PSTR
class SERVICE_REQUIRED_PRIVILEGES_INFOW(Structure):
    pmszRequiredPrivileges: win32more.Foundation.PWSTR
SERVICE_RUNS_IN_PROCESS = UInt32
SERVICE_RUNS_IN_NON_SYSTEM_OR_NOT_RUNNING: SERVICE_RUNS_IN_PROCESS = 0
SERVICE_RUNS_IN_SYSTEM_PROCESS: SERVICE_RUNS_IN_PROCESS = 1
SERVICE_SHARED_DIRECTORY_TYPE = Int32
SERVICE_SHARED_DIRECTORY_TYPE_ServiceSharedDirectoryPersistentState: SERVICE_SHARED_DIRECTORY_TYPE = 0
SERVICE_SHARED_REGISTRY_STATE_TYPE = Int32
SERVICE_SHARED_REGISTRY_STATE_TYPE_ServiceSharedRegistryPersistentState: SERVICE_SHARED_REGISTRY_STATE_TYPE = 0
class SERVICE_SID_INFO(Structure):
    dwServiceSidType: UInt32
class SERVICE_START_REASON(Structure):
    dwReason: UInt32
SERVICE_START_TYPE = UInt32
SERVICE_AUTO_START: SERVICE_START_TYPE = 2
SERVICE_BOOT_START: SERVICE_START_TYPE = 0
SERVICE_DEMAND_START: SERVICE_START_TYPE = 3
SERVICE_DISABLED: SERVICE_START_TYPE = 4
SERVICE_SYSTEM_START: SERVICE_START_TYPE = 1
class SERVICE_STATUS(Structure):
    dwServiceType: win32more.System.Services.ENUM_SERVICE_TYPE
    dwCurrentState: win32more.System.Services.SERVICE_STATUS_CURRENT_STATE
    dwControlsAccepted: UInt32
    dwWin32ExitCode: UInt32
    dwServiceSpecificExitCode: UInt32
    dwCheckPoint: UInt32
    dwWaitHint: UInt32
SERVICE_STATUS_CURRENT_STATE = UInt32
SERVICE_CONTINUE_PENDING: SERVICE_STATUS_CURRENT_STATE = 5
SERVICE_PAUSE_PENDING: SERVICE_STATUS_CURRENT_STATE = 6
SERVICE_PAUSED: SERVICE_STATUS_CURRENT_STATE = 7
SERVICE_RUNNING: SERVICE_STATUS_CURRENT_STATE = 4
SERVICE_START_PENDING: SERVICE_STATUS_CURRENT_STATE = 2
SERVICE_STOP_PENDING: SERVICE_STATUS_CURRENT_STATE = 3
SERVICE_STOPPED: SERVICE_STATUS_CURRENT_STATE = 1
SERVICE_STATUS_HANDLE = IntPtr
class SERVICE_STATUS_PROCESS(Structure):
    dwServiceType: win32more.System.Services.ENUM_SERVICE_TYPE
    dwCurrentState: win32more.System.Services.SERVICE_STATUS_CURRENT_STATE
    dwControlsAccepted: UInt32
    dwWin32ExitCode: UInt32
    dwServiceSpecificExitCode: UInt32
    dwCheckPoint: UInt32
    dwWaitHint: UInt32
    dwProcessId: UInt32
    dwServiceFlags: win32more.System.Services.SERVICE_RUNS_IN_PROCESS
class SERVICE_TABLE_ENTRYA(Structure):
    lpServiceName: win32more.Foundation.PSTR
    lpServiceProc: win32more.System.Services.LPSERVICE_MAIN_FUNCTIONA
class SERVICE_TABLE_ENTRYW(Structure):
    lpServiceName: win32more.Foundation.PWSTR
    lpServiceProc: win32more.System.Services.LPSERVICE_MAIN_FUNCTIONW
class SERVICE_TIMECHANGE_INFO(Structure):
    liNewTime: win32more.Foundation.LARGE_INTEGER
    liOldTime: win32more.Foundation.LARGE_INTEGER
class SERVICE_TRIGGER(Structure):
    dwTriggerType: win32more.System.Services.SERVICE_TRIGGER_TYPE
    dwAction: win32more.System.Services.SERVICE_TRIGGER_ACTION
    pTriggerSubtype: POINTER(Guid)
    cDataItems: UInt32
    pDataItems: POINTER(win32more.System.Services.SERVICE_TRIGGER_SPECIFIC_DATA_ITEM_head)
SERVICE_TRIGGER_ACTION = UInt32
SERVICE_TRIGGER_ACTION_SERVICE_START: SERVICE_TRIGGER_ACTION = 1
SERVICE_TRIGGER_ACTION_SERVICE_STOP: SERVICE_TRIGGER_ACTION = 2
class SERVICE_TRIGGER_CUSTOM_STATE_ID(Structure):
    Data: UInt32 * 2
class SERVICE_TRIGGER_INFO(Structure):
    cTriggers: UInt32
    pTriggers: POINTER(win32more.System.Services.SERVICE_TRIGGER_head)
    pReserved: c_char_p_no
class SERVICE_TRIGGER_SPECIFIC_DATA_ITEM(Structure):
    dwDataType: win32more.System.Services.SERVICE_TRIGGER_SPECIFIC_DATA_ITEM_DATA_TYPE
    cbData: UInt32
    pData: c_char_p_no
SERVICE_TRIGGER_SPECIFIC_DATA_ITEM_DATA_TYPE = UInt32
SERVICE_TRIGGER_DATA_TYPE_BINARY: SERVICE_TRIGGER_SPECIFIC_DATA_ITEM_DATA_TYPE = 1
SERVICE_TRIGGER_DATA_TYPE_STRING: SERVICE_TRIGGER_SPECIFIC_DATA_ITEM_DATA_TYPE = 2
SERVICE_TRIGGER_DATA_TYPE_LEVEL: SERVICE_TRIGGER_SPECIFIC_DATA_ITEM_DATA_TYPE = 3
SERVICE_TRIGGER_DATA_TYPE_KEYWORD_ANY: SERVICE_TRIGGER_SPECIFIC_DATA_ITEM_DATA_TYPE = 4
SERVICE_TRIGGER_DATA_TYPE_KEYWORD_ALL: SERVICE_TRIGGER_SPECIFIC_DATA_ITEM_DATA_TYPE = 5
SERVICE_TRIGGER_TYPE = UInt32
SERVICE_TRIGGER_TYPE_CUSTOM: SERVICE_TRIGGER_TYPE = 20
SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL: SERVICE_TRIGGER_TYPE = 1
SERVICE_TRIGGER_TYPE_DOMAIN_JOIN: SERVICE_TRIGGER_TYPE = 3
SERVICE_TRIGGER_TYPE_FIREWALL_PORT_EVENT: SERVICE_TRIGGER_TYPE = 4
SERVICE_TRIGGER_TYPE_GROUP_POLICY: SERVICE_TRIGGER_TYPE = 5
SERVICE_TRIGGER_TYPE_IP_ADDRESS_AVAILABILITY: SERVICE_TRIGGER_TYPE = 2
SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT: SERVICE_TRIGGER_TYPE = 6
make_head(_module, '_SC_NOTIFICATION_REGISTRATION')
make_head(_module, 'ENUM_SERVICE_STATUS_PROCESSA')
make_head(_module, 'ENUM_SERVICE_STATUS_PROCESSW')
make_head(_module, 'ENUM_SERVICE_STATUSA')
make_head(_module, 'ENUM_SERVICE_STATUSW')
make_head(_module, 'HANDLER_FUNCTION')
make_head(_module, 'HANDLER_FUNCTION_EX')
make_head(_module, 'LPHANDLER_FUNCTION')
make_head(_module, 'LPHANDLER_FUNCTION_EX')
make_head(_module, 'LPSERVICE_MAIN_FUNCTIONA')
make_head(_module, 'LPSERVICE_MAIN_FUNCTIONW')
make_head(_module, 'PFN_SC_NOTIFY_CALLBACK')
make_head(_module, 'PSC_NOTIFICATION_CALLBACK')
make_head(_module, 'QUERY_SERVICE_CONFIGA')
make_head(_module, 'QUERY_SERVICE_CONFIGW')
make_head(_module, 'QUERY_SERVICE_LOCK_STATUSA')
make_head(_module, 'QUERY_SERVICE_LOCK_STATUSW')
make_head(_module, 'SC_ACTION')
make_head(_module, 'SERVICE_CONTROL_STATUS_REASON_PARAMSA')
make_head(_module, 'SERVICE_CONTROL_STATUS_REASON_PARAMSW')
make_head(_module, 'SERVICE_CUSTOM_SYSTEM_STATE_CHANGE_DATA_ITEM')
make_head(_module, 'SERVICE_DELAYED_AUTO_START_INFO')
make_head(_module, 'SERVICE_DESCRIPTIONA')
make_head(_module, 'SERVICE_DESCRIPTIONW')
make_head(_module, 'SERVICE_FAILURE_ACTIONS_FLAG')
make_head(_module, 'SERVICE_FAILURE_ACTIONSA')
make_head(_module, 'SERVICE_FAILURE_ACTIONSW')
make_head(_module, 'SERVICE_LAUNCH_PROTECTED_INFO')
make_head(_module, 'SERVICE_MAIN_FUNCTIONA')
make_head(_module, 'SERVICE_MAIN_FUNCTIONW')
make_head(_module, 'SERVICE_NOTIFY_1')
make_head(_module, 'SERVICE_NOTIFY_2A')
make_head(_module, 'SERVICE_NOTIFY_2W')
make_head(_module, 'SERVICE_PREFERRED_NODE_INFO')
make_head(_module, 'SERVICE_PRESHUTDOWN_INFO')
make_head(_module, 'SERVICE_REQUIRED_PRIVILEGES_INFOA')
make_head(_module, 'SERVICE_REQUIRED_PRIVILEGES_INFOW')
make_head(_module, 'SERVICE_SID_INFO')
make_head(_module, 'SERVICE_START_REASON')
make_head(_module, 'SERVICE_STATUS')
make_head(_module, 'SERVICE_STATUS_PROCESS')
make_head(_module, 'SERVICE_TABLE_ENTRYA')
make_head(_module, 'SERVICE_TABLE_ENTRYW')
make_head(_module, 'SERVICE_TIMECHANGE_INFO')
make_head(_module, 'SERVICE_TRIGGER')
make_head(_module, 'SERVICE_TRIGGER_CUSTOM_STATE_ID')
make_head(_module, 'SERVICE_TRIGGER_INFO')
make_head(_module, 'SERVICE_TRIGGER_SPECIFIC_DATA_ITEM')
__all__ = [
    "CUSTOM_SYSTEM_STATE_CHANGE_EVENT_GUID",
    "ChangeServiceConfig2A",
    "ChangeServiceConfig2W",
    "ChangeServiceConfigA",
    "ChangeServiceConfigW",
    "CloseServiceHandle",
    "ControlService",
    "ControlServiceExA",
    "ControlServiceExW",
    "CreateServiceA",
    "CreateServiceW",
    "DOMAIN_JOIN_GUID",
    "DOMAIN_LEAVE_GUID",
    "DeleteService",
    "ENUM_SERVICE_STATE",
    "ENUM_SERVICE_STATUSA",
    "ENUM_SERVICE_STATUSW",
    "ENUM_SERVICE_STATUS_PROCESSA",
    "ENUM_SERVICE_STATUS_PROCESSW",
    "ENUM_SERVICE_TYPE",
    "EnumDependentServicesA",
    "EnumDependentServicesW",
    "EnumServicesStatusA",
    "EnumServicesStatusExA",
    "EnumServicesStatusExW",
    "EnumServicesStatusW",
    "FIREWALL_PORT_CLOSE_GUID",
    "FIREWALL_PORT_OPEN_GUID",
    "GetServiceDirectory",
    "GetServiceDisplayNameA",
    "GetServiceDisplayNameW",
    "GetServiceKeyNameA",
    "GetServiceKeyNameW",
    "GetServiceRegistryStateKey",
    "GetSharedServiceDirectory",
    "GetSharedServiceRegistryStateKey",
    "HANDLER_FUNCTION",
    "HANDLER_FUNCTION_EX",
    "LPHANDLER_FUNCTION",
    "LPHANDLER_FUNCTION_EX",
    "LPSERVICE_MAIN_FUNCTIONA",
    "LPSERVICE_MAIN_FUNCTIONW",
    "LockServiceDatabase",
    "MACHINE_POLICY_PRESENT_GUID",
    "NAMED_PIPE_EVENT_GUID",
    "NETWORK_MANAGER_FIRST_IP_ADDRESS_ARRIVAL_GUID",
    "NETWORK_MANAGER_LAST_IP_ADDRESS_REMOVAL_GUID",
    "NotifyBootConfigStatus",
    "NotifyServiceStatusChangeA",
    "NotifyServiceStatusChangeW",
    "OpenSCManagerA",
    "OpenSCManagerW",
    "OpenServiceA",
    "OpenServiceW",
    "PFN_SC_NOTIFY_CALLBACK",
    "PSC_NOTIFICATION_CALLBACK",
    "QUERY_SERVICE_CONFIGA",
    "QUERY_SERVICE_CONFIGW",
    "QUERY_SERVICE_LOCK_STATUSA",
    "QUERY_SERVICE_LOCK_STATUSW",
    "QueryServiceConfig2A",
    "QueryServiceConfig2W",
    "QueryServiceConfigA",
    "QueryServiceConfigW",
    "QueryServiceDynamicInformation",
    "QueryServiceLockStatusA",
    "QueryServiceLockStatusW",
    "QueryServiceObjectSecurity",
    "QueryServiceStatus",
    "QueryServiceStatusEx",
    "RPC_INTERFACE_EVENT_GUID",
    "RegisterServiceCtrlHandlerA",
    "RegisterServiceCtrlHandlerExA",
    "RegisterServiceCtrlHandlerExW",
    "RegisterServiceCtrlHandlerW",
    "SC_ACTION",
    "SC_ACTION_NONE",
    "SC_ACTION_OWN_RESTART",
    "SC_ACTION_REBOOT",
    "SC_ACTION_RESTART",
    "SC_ACTION_RUN_COMMAND",
    "SC_ACTION_TYPE",
    "SC_AGGREGATE_STORAGE_KEY",
    "SC_ENUM_PROCESS_INFO",
    "SC_ENUM_TYPE",
    "SC_EVENT_DATABASE_CHANGE",
    "SC_EVENT_PROPERTY_CHANGE",
    "SC_EVENT_STATUS_CHANGE",
    "SC_EVENT_TYPE",
    "SC_MANAGER_ALL_ACCESS",
    "SC_MANAGER_CONNECT",
    "SC_MANAGER_CREATE_SERVICE",
    "SC_MANAGER_ENUMERATE_SERVICE",
    "SC_MANAGER_LOCK",
    "SC_MANAGER_MODIFY_BOOT_CONFIG",
    "SC_MANAGER_QUERY_LOCK_STATUS",
    "SC_STATUS_PROCESS_INFO",
    "SC_STATUS_TYPE",
    "SERVICES_ACTIVE_DATABASE",
    "SERVICES_ACTIVE_DATABASEA",
    "SERVICES_ACTIVE_DATABASEW",
    "SERVICES_FAILED_DATABASE",
    "SERVICES_FAILED_DATABASEA",
    "SERVICES_FAILED_DATABASEW",
    "SERVICE_ACCEPT_HARDWAREPROFILECHANGE",
    "SERVICE_ACCEPT_LOWRESOURCES",
    "SERVICE_ACCEPT_NETBINDCHANGE",
    "SERVICE_ACCEPT_PARAMCHANGE",
    "SERVICE_ACCEPT_PAUSE_CONTINUE",
    "SERVICE_ACCEPT_POWEREVENT",
    "SERVICE_ACCEPT_PRESHUTDOWN",
    "SERVICE_ACCEPT_SESSIONCHANGE",
    "SERVICE_ACCEPT_SHUTDOWN",
    "SERVICE_ACCEPT_STOP",
    "SERVICE_ACCEPT_SYSTEMLOWRESOURCES",
    "SERVICE_ACCEPT_TIMECHANGE",
    "SERVICE_ACCEPT_TRIGGEREVENT",
    "SERVICE_ACCEPT_USER_LOGOFF",
    "SERVICE_ACTIVE",
    "SERVICE_ADAPTER",
    "SERVICE_ALL_ACCESS",
    "SERVICE_AUTO_START",
    "SERVICE_BOOT_START",
    "SERVICE_CHANGE_CONFIG",
    "SERVICE_CONFIG",
    "SERVICE_CONFIG_DELAYED_AUTO_START_INFO",
    "SERVICE_CONFIG_DESCRIPTION",
    "SERVICE_CONFIG_FAILURE_ACTIONS",
    "SERVICE_CONFIG_FAILURE_ACTIONS_FLAG",
    "SERVICE_CONFIG_LAUNCH_PROTECTED",
    "SERVICE_CONFIG_PREFERRED_NODE",
    "SERVICE_CONFIG_PRESHUTDOWN_INFO",
    "SERVICE_CONFIG_REQUIRED_PRIVILEGES_INFO",
    "SERVICE_CONFIG_SERVICE_SID_INFO",
    "SERVICE_CONFIG_TRIGGER_INFO",
    "SERVICE_CONTINUE_PENDING",
    "SERVICE_CONTROL_CONTINUE",
    "SERVICE_CONTROL_DEVICEEVENT",
    "SERVICE_CONTROL_HARDWAREPROFILECHANGE",
    "SERVICE_CONTROL_INTERROGATE",
    "SERVICE_CONTROL_LOWRESOURCES",
    "SERVICE_CONTROL_NETBINDADD",
    "SERVICE_CONTROL_NETBINDDISABLE",
    "SERVICE_CONTROL_NETBINDENABLE",
    "SERVICE_CONTROL_NETBINDREMOVE",
    "SERVICE_CONTROL_PARAMCHANGE",
    "SERVICE_CONTROL_PAUSE",
    "SERVICE_CONTROL_POWEREVENT",
    "SERVICE_CONTROL_PRESHUTDOWN",
    "SERVICE_CONTROL_SESSIONCHANGE",
    "SERVICE_CONTROL_SHUTDOWN",
    "SERVICE_CONTROL_STATUS_REASON_INFO",
    "SERVICE_CONTROL_STATUS_REASON_PARAMSA",
    "SERVICE_CONTROL_STATUS_REASON_PARAMSW",
    "SERVICE_CONTROL_STOP",
    "SERVICE_CONTROL_SYSTEMLOWRESOURCES",
    "SERVICE_CONTROL_TIMECHANGE",
    "SERVICE_CONTROL_TRIGGEREVENT",
    "SERVICE_CUSTOM_SYSTEM_STATE_CHANGE_DATA_ITEM",
    "SERVICE_DELAYED_AUTO_START_INFO",
    "SERVICE_DEMAND_START",
    "SERVICE_DESCRIPTIONA",
    "SERVICE_DESCRIPTIONW",
    "SERVICE_DIRECTORY_TYPE",
    "SERVICE_DIRECTORY_TYPE_ServiceDirectoryPersistentState",
    "SERVICE_DIRECTORY_TYPE_ServiceDirectoryTypeMax",
    "SERVICE_DISABLED",
    "SERVICE_DRIVER",
    "SERVICE_DYNAMIC_INFORMATION_LEVEL_START_REASON",
    "SERVICE_ENUMERATE_DEPENDENTS",
    "SERVICE_ERROR",
    "SERVICE_ERROR_CRITICAL",
    "SERVICE_ERROR_IGNORE",
    "SERVICE_ERROR_NORMAL",
    "SERVICE_ERROR_SEVERE",
    "SERVICE_FAILURE_ACTIONSA",
    "SERVICE_FAILURE_ACTIONSW",
    "SERVICE_FAILURE_ACTIONS_FLAG",
    "SERVICE_FILE_SYSTEM_DRIVER",
    "SERVICE_INACTIVE",
    "SERVICE_INTERROGATE",
    "SERVICE_KERNEL_DRIVER",
    "SERVICE_LAUNCH_PROTECTED_ANTIMALWARE_LIGHT",
    "SERVICE_LAUNCH_PROTECTED_INFO",
    "SERVICE_LAUNCH_PROTECTED_NONE",
    "SERVICE_LAUNCH_PROTECTED_WINDOWS",
    "SERVICE_LAUNCH_PROTECTED_WINDOWS_LIGHT",
    "SERVICE_MAIN_FUNCTIONA",
    "SERVICE_MAIN_FUNCTIONW",
    "SERVICE_NOTIFY",
    "SERVICE_NOTIFY_1",
    "SERVICE_NOTIFY_2A",
    "SERVICE_NOTIFY_2W",
    "SERVICE_NOTIFY_CONTINUE_PENDING",
    "SERVICE_NOTIFY_CREATED",
    "SERVICE_NOTIFY_DELETED",
    "SERVICE_NOTIFY_DELETE_PENDING",
    "SERVICE_NOTIFY_PAUSED",
    "SERVICE_NOTIFY_PAUSE_PENDING",
    "SERVICE_NOTIFY_RUNNING",
    "SERVICE_NOTIFY_START_PENDING",
    "SERVICE_NOTIFY_STATUS_CHANGE",
    "SERVICE_NOTIFY_STATUS_CHANGE_1",
    "SERVICE_NOTIFY_STATUS_CHANGE_2",
    "SERVICE_NOTIFY_STOPPED",
    "SERVICE_NOTIFY_STOP_PENDING",
    "SERVICE_NO_CHANGE",
    "SERVICE_PAUSED",
    "SERVICE_PAUSE_CONTINUE",
    "SERVICE_PAUSE_PENDING",
    "SERVICE_PREFERRED_NODE_INFO",
    "SERVICE_PRESHUTDOWN_INFO",
    "SERVICE_QUERY_CONFIG",
    "SERVICE_QUERY_STATUS",
    "SERVICE_RECOGNIZER_DRIVER",
    "SERVICE_REGISTRY_STATE_TYPE",
    "SERVICE_REGISTRY_STATE_TYPE_MaxServiceRegistryStateType",
    "SERVICE_REGISTRY_STATE_TYPE_ServiceRegistryStateParameters",
    "SERVICE_REGISTRY_STATE_TYPE_ServiceRegistryStatePersistent",
    "SERVICE_REQUIRED_PRIVILEGES_INFOA",
    "SERVICE_REQUIRED_PRIVILEGES_INFOW",
    "SERVICE_RUNNING",
    "SERVICE_RUNS_IN_NON_SYSTEM_OR_NOT_RUNNING",
    "SERVICE_RUNS_IN_PROCESS",
    "SERVICE_RUNS_IN_SYSTEM_PROCESS",
    "SERVICE_SHARED_DIRECTORY_TYPE",
    "SERVICE_SHARED_DIRECTORY_TYPE_ServiceSharedDirectoryPersistentState",
    "SERVICE_SHARED_REGISTRY_STATE_TYPE",
    "SERVICE_SHARED_REGISTRY_STATE_TYPE_ServiceSharedRegistryPersistentState",
    "SERVICE_SID_INFO",
    "SERVICE_SID_TYPE_NONE",
    "SERVICE_SID_TYPE_UNRESTRICTED",
    "SERVICE_START",
    "SERVICE_START_PENDING",
    "SERVICE_START_REASON",
    "SERVICE_START_REASON_AUTO",
    "SERVICE_START_REASON_DELAYEDAUTO",
    "SERVICE_START_REASON_DEMAND",
    "SERVICE_START_REASON_RESTART_ON_FAILURE",
    "SERVICE_START_REASON_TRIGGER",
    "SERVICE_START_TYPE",
    "SERVICE_STATE_ALL",
    "SERVICE_STATUS",
    "SERVICE_STATUS_CURRENT_STATE",
    "SERVICE_STATUS_HANDLE",
    "SERVICE_STATUS_PROCESS",
    "SERVICE_STOP",
    "SERVICE_STOPPED",
    "SERVICE_STOP_PENDING",
    "SERVICE_STOP_REASON_FLAG_CUSTOM",
    "SERVICE_STOP_REASON_FLAG_MAX",
    "SERVICE_STOP_REASON_FLAG_MIN",
    "SERVICE_STOP_REASON_FLAG_PLANNED",
    "SERVICE_STOP_REASON_FLAG_UNPLANNED",
    "SERVICE_STOP_REASON_MAJOR_APPLICATION",
    "SERVICE_STOP_REASON_MAJOR_HARDWARE",
    "SERVICE_STOP_REASON_MAJOR_MAX",
    "SERVICE_STOP_REASON_MAJOR_MAX_CUSTOM",
    "SERVICE_STOP_REASON_MAJOR_MIN",
    "SERVICE_STOP_REASON_MAJOR_MIN_CUSTOM",
    "SERVICE_STOP_REASON_MAJOR_NONE",
    "SERVICE_STOP_REASON_MAJOR_OPERATINGSYSTEM",
    "SERVICE_STOP_REASON_MAJOR_OTHER",
    "SERVICE_STOP_REASON_MAJOR_SOFTWARE",
    "SERVICE_STOP_REASON_MINOR_DISK",
    "SERVICE_STOP_REASON_MINOR_ENVIRONMENT",
    "SERVICE_STOP_REASON_MINOR_HARDWARE_DRIVER",
    "SERVICE_STOP_REASON_MINOR_HUNG",
    "SERVICE_STOP_REASON_MINOR_INSTALLATION",
    "SERVICE_STOP_REASON_MINOR_MAINTENANCE",
    "SERVICE_STOP_REASON_MINOR_MAX",
    "SERVICE_STOP_REASON_MINOR_MAX_CUSTOM",
    "SERVICE_STOP_REASON_MINOR_MEMOTYLIMIT",
    "SERVICE_STOP_REASON_MINOR_MIN",
    "SERVICE_STOP_REASON_MINOR_MIN_CUSTOM",
    "SERVICE_STOP_REASON_MINOR_MMC",
    "SERVICE_STOP_REASON_MINOR_NETWORKCARD",
    "SERVICE_STOP_REASON_MINOR_NETWORK_CONNECTIVITY",
    "SERVICE_STOP_REASON_MINOR_NONE",
    "SERVICE_STOP_REASON_MINOR_OTHER",
    "SERVICE_STOP_REASON_MINOR_OTHERDRIVER",
    "SERVICE_STOP_REASON_MINOR_RECONFIG",
    "SERVICE_STOP_REASON_MINOR_SECURITY",
    "SERVICE_STOP_REASON_MINOR_SECURITYFIX",
    "SERVICE_STOP_REASON_MINOR_SECURITYFIX_UNINSTALL",
    "SERVICE_STOP_REASON_MINOR_SERVICEPACK",
    "SERVICE_STOP_REASON_MINOR_SERVICEPACK_UNINSTALL",
    "SERVICE_STOP_REASON_MINOR_SOFTWARE_UPDATE",
    "SERVICE_STOP_REASON_MINOR_SOFTWARE_UPDATE_UNINSTALL",
    "SERVICE_STOP_REASON_MINOR_UNSTABLE",
    "SERVICE_STOP_REASON_MINOR_UPGRADE",
    "SERVICE_STOP_REASON_MINOR_WMI",
    "SERVICE_SYSTEM_START",
    "SERVICE_TABLE_ENTRYA",
    "SERVICE_TABLE_ENTRYW",
    "SERVICE_TIMECHANGE_INFO",
    "SERVICE_TRIGGER",
    "SERVICE_TRIGGER_ACTION",
    "SERVICE_TRIGGER_ACTION_SERVICE_START",
    "SERVICE_TRIGGER_ACTION_SERVICE_STOP",
    "SERVICE_TRIGGER_CUSTOM_STATE_ID",
    "SERVICE_TRIGGER_DATA_TYPE_BINARY",
    "SERVICE_TRIGGER_DATA_TYPE_KEYWORD_ALL",
    "SERVICE_TRIGGER_DATA_TYPE_KEYWORD_ANY",
    "SERVICE_TRIGGER_DATA_TYPE_LEVEL",
    "SERVICE_TRIGGER_DATA_TYPE_STRING",
    "SERVICE_TRIGGER_INFO",
    "SERVICE_TRIGGER_SPECIFIC_DATA_ITEM",
    "SERVICE_TRIGGER_SPECIFIC_DATA_ITEM_DATA_TYPE",
    "SERVICE_TRIGGER_STARTED_ARGUMENT",
    "SERVICE_TRIGGER_TYPE",
    "SERVICE_TRIGGER_TYPE_AGGREGATE",
    "SERVICE_TRIGGER_TYPE_CUSTOM",
    "SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE",
    "SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL",
    "SERVICE_TRIGGER_TYPE_DOMAIN_JOIN",
    "SERVICE_TRIGGER_TYPE_FIREWALL_PORT_EVENT",
    "SERVICE_TRIGGER_TYPE_GROUP_POLICY",
    "SERVICE_TRIGGER_TYPE_IP_ADDRESS_AVAILABILITY",
    "SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT",
    "SERVICE_USER_DEFINED_CONTROL",
    "SERVICE_USER_OWN_PROCESS",
    "SERVICE_USER_SHARE_PROCESS",
    "SERVICE_WIN32",
    "SERVICE_WIN32_OWN_PROCESS",
    "SERVICE_WIN32_SHARE_PROCESS",
    "SetServiceBits",
    "SetServiceObjectSecurity",
    "SetServiceStatus",
    "StartServiceA",
    "StartServiceCtrlDispatcherA",
    "StartServiceCtrlDispatcherW",
    "StartServiceW",
    "USER_POLICY_PRESENT_GUID",
    "UnlockServiceDatabase",
    "WaitServiceState",
    "_SC_NOTIFICATION_REGISTRATION",
]
