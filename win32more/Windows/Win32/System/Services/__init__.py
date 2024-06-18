from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Security
import win32more.Windows.Win32.System.Registry
import win32more.Windows.Win32.System.Services
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
NETWORK_MANAGER_FIRST_IP_ADDRESS_ARRIVAL_GUID: Guid = Guid('{4f27f2de-14e2-430b-a549-7cd48cbc8245}')
NETWORK_MANAGER_LAST_IP_ADDRESS_REMOVAL_GUID: Guid = Guid('{cc4ba62a-162e-4648-847a-b6bdf993e335}')
DOMAIN_JOIN_GUID: Guid = Guid('{1ce20aba-9851-4421-9430-1ddeb766e809}')
DOMAIN_LEAVE_GUID: Guid = Guid('{ddaf516e-58c2-4866-9574-c3b615d42ea1}')
FIREWALL_PORT_OPEN_GUID: Guid = Guid('{b7569e07-8421-4ee0-ad10-86915afdad09}')
FIREWALL_PORT_CLOSE_GUID: Guid = Guid('{a144ed38-8e12-4de4-9d96-e64740b1a524}')
MACHINE_POLICY_PRESENT_GUID: Guid = Guid('{659fcae6-5bdb-4da9-b1ff-ca2a178d46e0}')
USER_POLICY_PRESENT_GUID: Guid = Guid('{54fb46c8-f089-464c-b1fd-59d1b62c3b50}')
RPC_INTERFACE_EVENT_GUID: Guid = Guid('{bc90d167-9470-4139-a9ba-be0bbbf5b74d}')
NAMED_PIPE_EVENT_GUID: Guid = Guid('{1f81d131-3fac-4537-9e0c-7e7b0c2f4b55}')
CUSTOM_SYSTEM_STATE_CHANGE_EVENT_GUID: Guid = Guid('{2d7a2816-0c5e-45fc-9ce7-570e5ecde9c9}')
SERVICE_TRIGGER_STARTED_ARGUMENT: String = 'TriggerStarted'
SC_AGGREGATE_STORAGE_KEY: String = 'System\\CurrentControlSet\\Control\\ServiceAggregatedEvents'
@winfunctype('ADVAPI32.dll')
def SetServiceBits(hServiceStatus: win32more.Windows.Win32.System.Services.SERVICE_STATUS_HANDLE, dwServiceBits: UInt32, bSetBitsOn: win32more.Windows.Win32.Foundation.BOOL, bUpdateImmediately: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ChangeServiceConfigA(hService: win32more.Windows.Win32.System.Services.SC_HANDLE, dwServiceType: win32more.Windows.Win32.System.Services.ENUM_SERVICE_TYPE, dwStartType: win32more.Windows.Win32.System.Services.SERVICE_START_TYPE, dwErrorControl: win32more.Windows.Win32.System.Services.SERVICE_ERROR, lpBinaryPathName: win32more.Windows.Win32.Foundation.PSTR, lpLoadOrderGroup: win32more.Windows.Win32.Foundation.PSTR, lpdwTagId: POINTER(UInt32), lpDependencies: win32more.Windows.Win32.Foundation.PSTR, lpServiceStartName: win32more.Windows.Win32.Foundation.PSTR, lpPassword: win32more.Windows.Win32.Foundation.PSTR, lpDisplayName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ChangeServiceConfigW(hService: win32more.Windows.Win32.System.Services.SC_HANDLE, dwServiceType: win32more.Windows.Win32.System.Services.ENUM_SERVICE_TYPE, dwStartType: win32more.Windows.Win32.System.Services.SERVICE_START_TYPE, dwErrorControl: win32more.Windows.Win32.System.Services.SERVICE_ERROR, lpBinaryPathName: win32more.Windows.Win32.Foundation.PWSTR, lpLoadOrderGroup: win32more.Windows.Win32.Foundation.PWSTR, lpdwTagId: POINTER(UInt32), lpDependencies: win32more.Windows.Win32.Foundation.PWSTR, lpServiceStartName: win32more.Windows.Win32.Foundation.PWSTR, lpPassword: win32more.Windows.Win32.Foundation.PWSTR, lpDisplayName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
ChangeServiceConfig = UnicodeAlias('ChangeServiceConfigW')
@winfunctype('ADVAPI32.dll')
def ChangeServiceConfig2A(hService: win32more.Windows.Win32.System.Services.SC_HANDLE, dwInfoLevel: win32more.Windows.Win32.System.Services.SERVICE_CONFIG, lpInfo: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ChangeServiceConfig2W(hService: win32more.Windows.Win32.System.Services.SC_HANDLE, dwInfoLevel: win32more.Windows.Win32.System.Services.SERVICE_CONFIG, lpInfo: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
ChangeServiceConfig2 = UnicodeAlias('ChangeServiceConfig2W')
@winfunctype('ADVAPI32.dll')
def CloseServiceHandle(hSCObject: win32more.Windows.Win32.System.Services.SC_HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ControlService(hService: win32more.Windows.Win32.System.Services.SC_HANDLE, dwControl: UInt32, lpServiceStatus: POINTER(win32more.Windows.Win32.System.Services.SERVICE_STATUS)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CreateServiceA(hSCManager: win32more.Windows.Win32.System.Services.SC_HANDLE, lpServiceName: win32more.Windows.Win32.Foundation.PSTR, lpDisplayName: win32more.Windows.Win32.Foundation.PSTR, dwDesiredAccess: UInt32, dwServiceType: win32more.Windows.Win32.System.Services.ENUM_SERVICE_TYPE, dwStartType: win32more.Windows.Win32.System.Services.SERVICE_START_TYPE, dwErrorControl: win32more.Windows.Win32.System.Services.SERVICE_ERROR, lpBinaryPathName: win32more.Windows.Win32.Foundation.PSTR, lpLoadOrderGroup: win32more.Windows.Win32.Foundation.PSTR, lpdwTagId: POINTER(UInt32), lpDependencies: win32more.Windows.Win32.Foundation.PSTR, lpServiceStartName: win32more.Windows.Win32.Foundation.PSTR, lpPassword: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.System.Services.SC_HANDLE: ...
@winfunctype('ADVAPI32.dll')
def CreateServiceW(hSCManager: win32more.Windows.Win32.System.Services.SC_HANDLE, lpServiceName: win32more.Windows.Win32.Foundation.PWSTR, lpDisplayName: win32more.Windows.Win32.Foundation.PWSTR, dwDesiredAccess: UInt32, dwServiceType: win32more.Windows.Win32.System.Services.ENUM_SERVICE_TYPE, dwStartType: win32more.Windows.Win32.System.Services.SERVICE_START_TYPE, dwErrorControl: win32more.Windows.Win32.System.Services.SERVICE_ERROR, lpBinaryPathName: win32more.Windows.Win32.Foundation.PWSTR, lpLoadOrderGroup: win32more.Windows.Win32.Foundation.PWSTR, lpdwTagId: POINTER(UInt32), lpDependencies: win32more.Windows.Win32.Foundation.PWSTR, lpServiceStartName: win32more.Windows.Win32.Foundation.PWSTR, lpPassword: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.System.Services.SC_HANDLE: ...
CreateService = UnicodeAlias('CreateServiceW')
@winfunctype('ADVAPI32.dll')
def DeleteService(hService: win32more.Windows.Win32.System.Services.SC_HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def EnumDependentServicesA(hService: win32more.Windows.Win32.System.Services.SC_HANDLE, dwServiceState: win32more.Windows.Win32.System.Services.ENUM_SERVICE_STATE, lpServices: POINTER(win32more.Windows.Win32.System.Services.ENUM_SERVICE_STATUSA), cbBufSize: UInt32, pcbBytesNeeded: POINTER(UInt32), lpServicesReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def EnumDependentServicesW(hService: win32more.Windows.Win32.System.Services.SC_HANDLE, dwServiceState: win32more.Windows.Win32.System.Services.ENUM_SERVICE_STATE, lpServices: POINTER(win32more.Windows.Win32.System.Services.ENUM_SERVICE_STATUSW), cbBufSize: UInt32, pcbBytesNeeded: POINTER(UInt32), lpServicesReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
EnumDependentServices = UnicodeAlias('EnumDependentServicesW')
@winfunctype('ADVAPI32.dll')
def EnumServicesStatusA(hSCManager: win32more.Windows.Win32.System.Services.SC_HANDLE, dwServiceType: win32more.Windows.Win32.System.Services.ENUM_SERVICE_TYPE, dwServiceState: win32more.Windows.Win32.System.Services.ENUM_SERVICE_STATE, lpServices: POINTER(win32more.Windows.Win32.System.Services.ENUM_SERVICE_STATUSA), cbBufSize: UInt32, pcbBytesNeeded: POINTER(UInt32), lpServicesReturned: POINTER(UInt32), lpResumeHandle: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def EnumServicesStatusW(hSCManager: win32more.Windows.Win32.System.Services.SC_HANDLE, dwServiceType: win32more.Windows.Win32.System.Services.ENUM_SERVICE_TYPE, dwServiceState: win32more.Windows.Win32.System.Services.ENUM_SERVICE_STATE, lpServices: POINTER(win32more.Windows.Win32.System.Services.ENUM_SERVICE_STATUSW), cbBufSize: UInt32, pcbBytesNeeded: POINTER(UInt32), lpServicesReturned: POINTER(UInt32), lpResumeHandle: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
EnumServicesStatus = UnicodeAlias('EnumServicesStatusW')
@winfunctype('ADVAPI32.dll')
def EnumServicesStatusExA(hSCManager: win32more.Windows.Win32.System.Services.SC_HANDLE, InfoLevel: win32more.Windows.Win32.System.Services.SC_ENUM_TYPE, dwServiceType: win32more.Windows.Win32.System.Services.ENUM_SERVICE_TYPE, dwServiceState: win32more.Windows.Win32.System.Services.ENUM_SERVICE_STATE, lpServices: POINTER(Byte), cbBufSize: UInt32, pcbBytesNeeded: POINTER(UInt32), lpServicesReturned: POINTER(UInt32), lpResumeHandle: POINTER(UInt32), pszGroupName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def EnumServicesStatusExW(hSCManager: win32more.Windows.Win32.System.Services.SC_HANDLE, InfoLevel: win32more.Windows.Win32.System.Services.SC_ENUM_TYPE, dwServiceType: win32more.Windows.Win32.System.Services.ENUM_SERVICE_TYPE, dwServiceState: win32more.Windows.Win32.System.Services.ENUM_SERVICE_STATE, lpServices: POINTER(Byte), cbBufSize: UInt32, pcbBytesNeeded: POINTER(UInt32), lpServicesReturned: POINTER(UInt32), lpResumeHandle: POINTER(UInt32), pszGroupName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
EnumServicesStatusEx = UnicodeAlias('EnumServicesStatusExW')
@winfunctype('ADVAPI32.dll')
def GetServiceKeyNameA(hSCManager: win32more.Windows.Win32.System.Services.SC_HANDLE, lpDisplayName: win32more.Windows.Win32.Foundation.PSTR, lpServiceName: win32more.Windows.Win32.Foundation.PSTR, lpcchBuffer: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def GetServiceKeyNameW(hSCManager: win32more.Windows.Win32.System.Services.SC_HANDLE, lpDisplayName: win32more.Windows.Win32.Foundation.PWSTR, lpServiceName: win32more.Windows.Win32.Foundation.PWSTR, lpcchBuffer: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
GetServiceKeyName = UnicodeAlias('GetServiceKeyNameW')
@winfunctype('ADVAPI32.dll')
def GetServiceDisplayNameA(hSCManager: win32more.Windows.Win32.System.Services.SC_HANDLE, lpServiceName: win32more.Windows.Win32.Foundation.PSTR, lpDisplayName: win32more.Windows.Win32.Foundation.PSTR, lpcchBuffer: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def GetServiceDisplayNameW(hSCManager: win32more.Windows.Win32.System.Services.SC_HANDLE, lpServiceName: win32more.Windows.Win32.Foundation.PWSTR, lpDisplayName: win32more.Windows.Win32.Foundation.PWSTR, lpcchBuffer: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
GetServiceDisplayName = UnicodeAlias('GetServiceDisplayNameW')
@winfunctype('ADVAPI32.dll')
def LockServiceDatabase(hSCManager: win32more.Windows.Win32.System.Services.SC_HANDLE) -> VoidPtr: ...
@winfunctype('ADVAPI32.dll')
def NotifyBootConfigStatus(BootAcceptable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def OpenSCManagerA(lpMachineName: win32more.Windows.Win32.Foundation.PSTR, lpDatabaseName: win32more.Windows.Win32.Foundation.PSTR, dwDesiredAccess: UInt32) -> win32more.Windows.Win32.System.Services.SC_HANDLE: ...
@winfunctype('ADVAPI32.dll')
def OpenSCManagerW(lpMachineName: win32more.Windows.Win32.Foundation.PWSTR, lpDatabaseName: win32more.Windows.Win32.Foundation.PWSTR, dwDesiredAccess: UInt32) -> win32more.Windows.Win32.System.Services.SC_HANDLE: ...
OpenSCManager = UnicodeAlias('OpenSCManagerW')
@winfunctype('ADVAPI32.dll')
def OpenServiceA(hSCManager: win32more.Windows.Win32.System.Services.SC_HANDLE, lpServiceName: win32more.Windows.Win32.Foundation.PSTR, dwDesiredAccess: UInt32) -> win32more.Windows.Win32.System.Services.SC_HANDLE: ...
@winfunctype('ADVAPI32.dll')
def OpenServiceW(hSCManager: win32more.Windows.Win32.System.Services.SC_HANDLE, lpServiceName: win32more.Windows.Win32.Foundation.PWSTR, dwDesiredAccess: UInt32) -> win32more.Windows.Win32.System.Services.SC_HANDLE: ...
OpenService = UnicodeAlias('OpenServiceW')
@winfunctype('ADVAPI32.dll')
def QueryServiceConfigA(hService: win32more.Windows.Win32.System.Services.SC_HANDLE, lpServiceConfig: POINTER(win32more.Windows.Win32.System.Services.QUERY_SERVICE_CONFIGA), cbBufSize: UInt32, pcbBytesNeeded: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def QueryServiceConfigW(hService: win32more.Windows.Win32.System.Services.SC_HANDLE, lpServiceConfig: POINTER(win32more.Windows.Win32.System.Services.QUERY_SERVICE_CONFIGW), cbBufSize: UInt32, pcbBytesNeeded: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
QueryServiceConfig = UnicodeAlias('QueryServiceConfigW')
@winfunctype('ADVAPI32.dll')
def QueryServiceConfig2A(hService: win32more.Windows.Win32.System.Services.SC_HANDLE, dwInfoLevel: win32more.Windows.Win32.System.Services.SERVICE_CONFIG, lpBuffer: POINTER(Byte), cbBufSize: UInt32, pcbBytesNeeded: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def QueryServiceConfig2W(hService: win32more.Windows.Win32.System.Services.SC_HANDLE, dwInfoLevel: win32more.Windows.Win32.System.Services.SERVICE_CONFIG, lpBuffer: POINTER(Byte), cbBufSize: UInt32, pcbBytesNeeded: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
QueryServiceConfig2 = UnicodeAlias('QueryServiceConfig2W')
@winfunctype('ADVAPI32.dll')
def QueryServiceLockStatusA(hSCManager: win32more.Windows.Win32.System.Services.SC_HANDLE, lpLockStatus: POINTER(win32more.Windows.Win32.System.Services.QUERY_SERVICE_LOCK_STATUSA), cbBufSize: UInt32, pcbBytesNeeded: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def QueryServiceLockStatusW(hSCManager: win32more.Windows.Win32.System.Services.SC_HANDLE, lpLockStatus: POINTER(win32more.Windows.Win32.System.Services.QUERY_SERVICE_LOCK_STATUSW), cbBufSize: UInt32, pcbBytesNeeded: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
QueryServiceLockStatus = UnicodeAlias('QueryServiceLockStatusW')
@winfunctype('ADVAPI32.dll')
def QueryServiceObjectSecurity(hService: win32more.Windows.Win32.System.Services.SC_HANDLE, dwSecurityInformation: UInt32, lpSecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, cbBufSize: UInt32, pcbBytesNeeded: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def QueryServiceStatus(hService: win32more.Windows.Win32.System.Services.SC_HANDLE, lpServiceStatus: POINTER(win32more.Windows.Win32.System.Services.SERVICE_STATUS)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def QueryServiceStatusEx(hService: win32more.Windows.Win32.System.Services.SC_HANDLE, InfoLevel: win32more.Windows.Win32.System.Services.SC_STATUS_TYPE, lpBuffer: POINTER(Byte), cbBufSize: UInt32, pcbBytesNeeded: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def RegisterServiceCtrlHandlerA(lpServiceName: win32more.Windows.Win32.Foundation.PSTR, lpHandlerProc: win32more.Windows.Win32.System.Services.LPHANDLER_FUNCTION) -> win32more.Windows.Win32.System.Services.SERVICE_STATUS_HANDLE: ...
@winfunctype('ADVAPI32.dll')
def RegisterServiceCtrlHandlerW(lpServiceName: win32more.Windows.Win32.Foundation.PWSTR, lpHandlerProc: win32more.Windows.Win32.System.Services.LPHANDLER_FUNCTION) -> win32more.Windows.Win32.System.Services.SERVICE_STATUS_HANDLE: ...
RegisterServiceCtrlHandler = UnicodeAlias('RegisterServiceCtrlHandlerW')
@winfunctype('ADVAPI32.dll')
def RegisterServiceCtrlHandlerExA(lpServiceName: win32more.Windows.Win32.Foundation.PSTR, lpHandlerProc: win32more.Windows.Win32.System.Services.LPHANDLER_FUNCTION_EX, lpContext: VoidPtr) -> win32more.Windows.Win32.System.Services.SERVICE_STATUS_HANDLE: ...
@winfunctype('ADVAPI32.dll')
def RegisterServiceCtrlHandlerExW(lpServiceName: win32more.Windows.Win32.Foundation.PWSTR, lpHandlerProc: win32more.Windows.Win32.System.Services.LPHANDLER_FUNCTION_EX, lpContext: VoidPtr) -> win32more.Windows.Win32.System.Services.SERVICE_STATUS_HANDLE: ...
RegisterServiceCtrlHandlerEx = UnicodeAlias('RegisterServiceCtrlHandlerExW')
@winfunctype('ADVAPI32.dll')
def SetServiceObjectSecurity(hService: win32more.Windows.Win32.System.Services.SC_HANDLE, dwSecurityInformation: win32more.Windows.Win32.Security.OBJECT_SECURITY_INFORMATION, lpSecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def SetServiceStatus(hServiceStatus: win32more.Windows.Win32.System.Services.SERVICE_STATUS_HANDLE, lpServiceStatus: POINTER(win32more.Windows.Win32.System.Services.SERVICE_STATUS)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def StartServiceCtrlDispatcherA(lpServiceStartTable: POINTER(win32more.Windows.Win32.System.Services.SERVICE_TABLE_ENTRYA)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def StartServiceCtrlDispatcherW(lpServiceStartTable: POINTER(win32more.Windows.Win32.System.Services.SERVICE_TABLE_ENTRYW)) -> win32more.Windows.Win32.Foundation.BOOL: ...
StartServiceCtrlDispatcher = UnicodeAlias('StartServiceCtrlDispatcherW')
@winfunctype('ADVAPI32.dll')
def StartServiceA(hService: win32more.Windows.Win32.System.Services.SC_HANDLE, dwNumServiceArgs: UInt32, lpServiceArgVectors: POINTER(win32more.Windows.Win32.Foundation.PSTR)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def StartServiceW(hService: win32more.Windows.Win32.System.Services.SC_HANDLE, dwNumServiceArgs: UInt32, lpServiceArgVectors: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.BOOL: ...
StartService = UnicodeAlias('StartServiceW')
@winfunctype('ADVAPI32.dll')
def UnlockServiceDatabase(ScLock: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def NotifyServiceStatusChangeA(hService: win32more.Windows.Win32.System.Services.SC_HANDLE, dwNotifyMask: win32more.Windows.Win32.System.Services.SERVICE_NOTIFY, pNotifyBuffer: POINTER(win32more.Windows.Win32.System.Services.SERVICE_NOTIFY_2A)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def NotifyServiceStatusChangeW(hService: win32more.Windows.Win32.System.Services.SC_HANDLE, dwNotifyMask: win32more.Windows.Win32.System.Services.SERVICE_NOTIFY, pNotifyBuffer: POINTER(win32more.Windows.Win32.System.Services.SERVICE_NOTIFY_2W)) -> UInt32: ...
NotifyServiceStatusChange = UnicodeAlias('NotifyServiceStatusChangeW')
@winfunctype('ADVAPI32.dll')
def ControlServiceExA(hService: win32more.Windows.Win32.System.Services.SC_HANDLE, dwControl: UInt32, dwInfoLevel: UInt32, pControlParams: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ControlServiceExW(hService: win32more.Windows.Win32.System.Services.SC_HANDLE, dwControl: UInt32, dwInfoLevel: UInt32, pControlParams: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
ControlServiceEx = UnicodeAlias('ControlServiceExW')
@winfunctype('ADVAPI32.dll')
def QueryServiceDynamicInformation(hServiceStatus: win32more.Windows.Win32.System.Services.SERVICE_STATUS_HANDLE, dwInfoLevel: UInt32, ppDynamicInfo: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SecHost.dll')
def SubscribeServiceChangeNotifications(hService: win32more.Windows.Win32.System.Services.SC_HANDLE, eEventType: win32more.Windows.Win32.System.Services.SC_EVENT_TYPE, pCallback: win32more.Windows.Win32.System.Services.PSC_NOTIFICATION_CALLBACK, pCallbackContext: VoidPtr, pSubscription: POINTER(win32more.Windows.Win32.System.Services.PSC_NOTIFICATION_REGISTRATION)) -> UInt32: ...
@winfunctype('SecHost.dll')
def UnsubscribeServiceChangeNotifications(pSubscription: win32more.Windows.Win32.System.Services.PSC_NOTIFICATION_REGISTRATION) -> Void: ...
@winfunctype('ADVAPI32.dll')
def WaitServiceState(hService: win32more.Windows.Win32.System.Services.SC_HANDLE, dwNotify: UInt32, dwTimeout: UInt32, hCancelEvent: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('api-ms-win-service-core-l1-1-3.dll')
def GetServiceRegistryStateKey(ServiceStatusHandle: win32more.Windows.Win32.System.Services.SERVICE_STATUS_HANDLE, StateType: win32more.Windows.Win32.System.Services.SERVICE_REGISTRY_STATE_TYPE, AccessMask: UInt32, ServiceStateKey: POINTER(win32more.Windows.Win32.System.Registry.HKEY)) -> UInt32: ...
@winfunctype('api-ms-win-service-core-l1-1-4.dll')
def GetServiceDirectory(hServiceStatus: win32more.Windows.Win32.System.Services.SERVICE_STATUS_HANDLE, eDirectoryType: win32more.Windows.Win32.System.Services.SERVICE_DIRECTORY_TYPE, lpPathBuffer: win32more.Windows.Win32.Foundation.PWSTR, cchPathBufferLength: UInt32, lpcchRequiredBufferLength: POINTER(UInt32)) -> UInt32: ...
@winfunctype('api-ms-win-service-core-l1-1-5.dll')
def GetSharedServiceRegistryStateKey(ServiceHandle: win32more.Windows.Win32.System.Services.SC_HANDLE, StateType: win32more.Windows.Win32.System.Services.SERVICE_SHARED_REGISTRY_STATE_TYPE, AccessMask: UInt32, ServiceStateKey: POINTER(win32more.Windows.Win32.System.Registry.HKEY)) -> UInt32: ...
@winfunctype('api-ms-win-service-core-l1-1-5.dll')
def GetSharedServiceDirectory(ServiceHandle: win32more.Windows.Win32.System.Services.SC_HANDLE, DirectoryType: win32more.Windows.Win32.System.Services.SERVICE_SHARED_DIRECTORY_TYPE, PathBuffer: win32more.Windows.Win32.Foundation.PWSTR, PathBufferLength: UInt32, RequiredBufferLength: POINTER(UInt32)) -> UInt32: ...
ENUM_SERVICE_STATE = UInt32
SERVICE_ACTIVE: win32more.Windows.Win32.System.Services.ENUM_SERVICE_STATE = 1
SERVICE_INACTIVE: win32more.Windows.Win32.System.Services.ENUM_SERVICE_STATE = 2
SERVICE_STATE_ALL: win32more.Windows.Win32.System.Services.ENUM_SERVICE_STATE = 3
class ENUM_SERVICE_STATUSA(Structure):
    lpServiceName: win32more.Windows.Win32.Foundation.PSTR
    lpDisplayName: win32more.Windows.Win32.Foundation.PSTR
    ServiceStatus: win32more.Windows.Win32.System.Services.SERVICE_STATUS
class ENUM_SERVICE_STATUSW(Structure):
    lpServiceName: win32more.Windows.Win32.Foundation.PWSTR
    lpDisplayName: win32more.Windows.Win32.Foundation.PWSTR
    ServiceStatus: win32more.Windows.Win32.System.Services.SERVICE_STATUS
ENUM_SERVICE_STATUS = UnicodeAlias('ENUM_SERVICE_STATUSW')
class ENUM_SERVICE_STATUS_PROCESSA(Structure):
    lpServiceName: win32more.Windows.Win32.Foundation.PSTR
    lpDisplayName: win32more.Windows.Win32.Foundation.PSTR
    ServiceStatusProcess: win32more.Windows.Win32.System.Services.SERVICE_STATUS_PROCESS
class ENUM_SERVICE_STATUS_PROCESSW(Structure):
    lpServiceName: win32more.Windows.Win32.Foundation.PWSTR
    lpDisplayName: win32more.Windows.Win32.Foundation.PWSTR
    ServiceStatusProcess: win32more.Windows.Win32.System.Services.SERVICE_STATUS_PROCESS
ENUM_SERVICE_STATUS_PROCESS = UnicodeAlias('ENUM_SERVICE_STATUS_PROCESSW')
ENUM_SERVICE_TYPE = UInt32
SERVICE_DRIVER: win32more.Windows.Win32.System.Services.ENUM_SERVICE_TYPE = 11
SERVICE_KERNEL_DRIVER: win32more.Windows.Win32.System.Services.ENUM_SERVICE_TYPE = 1
SERVICE_WIN32: win32more.Windows.Win32.System.Services.ENUM_SERVICE_TYPE = 48
SERVICE_WIN32_SHARE_PROCESS: win32more.Windows.Win32.System.Services.ENUM_SERVICE_TYPE = 32
SERVICE_ADAPTER: win32more.Windows.Win32.System.Services.ENUM_SERVICE_TYPE = 4
SERVICE_FILE_SYSTEM_DRIVER: win32more.Windows.Win32.System.Services.ENUM_SERVICE_TYPE = 2
SERVICE_RECOGNIZER_DRIVER: win32more.Windows.Win32.System.Services.ENUM_SERVICE_TYPE = 8
SERVICE_WIN32_OWN_PROCESS: win32more.Windows.Win32.System.Services.ENUM_SERVICE_TYPE = 16
SERVICE_USER_OWN_PROCESS: win32more.Windows.Win32.System.Services.ENUM_SERVICE_TYPE = 80
SERVICE_USER_SHARE_PROCESS: win32more.Windows.Win32.System.Services.ENUM_SERVICE_TYPE = 96
@winfunctype_pointer
def HANDLER_FUNCTION(dwControl: UInt32) -> Void: ...
@winfunctype_pointer
def HANDLER_FUNCTION_EX(dwControl: UInt32, dwEventType: UInt32, lpEventData: VoidPtr, lpContext: VoidPtr) -> UInt32: ...
@winfunctype_pointer
def LPHANDLER_FUNCTION(dwControl: UInt32) -> Void: ...
@winfunctype_pointer
def LPHANDLER_FUNCTION_EX(dwControl: UInt32, dwEventType: UInt32, lpEventData: VoidPtr, lpContext: VoidPtr) -> UInt32: ...
@winfunctype_pointer
def LPSERVICE_MAIN_FUNCTIONA(dwNumServicesArgs: UInt32, lpServiceArgVectors: POINTER(win32more.Windows.Win32.Foundation.PSTR)) -> Void: ...
@winfunctype_pointer
def LPSERVICE_MAIN_FUNCTIONW(dwNumServicesArgs: UInt32, lpServiceArgVectors: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> Void: ...
LPSERVICE_MAIN_FUNCTION = UnicodeAlias('LPSERVICE_MAIN_FUNCTIONW')
@winfunctype_pointer
def PFN_SC_NOTIFY_CALLBACK(pParameter: VoidPtr) -> Void: ...
@winfunctype_pointer
def PSC_NOTIFICATION_CALLBACK(dwNotify: UInt32, pCallbackContext: VoidPtr) -> Void: ...
PSC_NOTIFICATION_REGISTRATION = IntPtr
class QUERY_SERVICE_CONFIGA(Structure):
    dwServiceType: win32more.Windows.Win32.System.Services.ENUM_SERVICE_TYPE
    dwStartType: win32more.Windows.Win32.System.Services.SERVICE_START_TYPE
    dwErrorControl: win32more.Windows.Win32.System.Services.SERVICE_ERROR
    lpBinaryPathName: win32more.Windows.Win32.Foundation.PSTR
    lpLoadOrderGroup: win32more.Windows.Win32.Foundation.PSTR
    dwTagId: UInt32
    lpDependencies: win32more.Windows.Win32.Foundation.PSTR
    lpServiceStartName: win32more.Windows.Win32.Foundation.PSTR
    lpDisplayName: win32more.Windows.Win32.Foundation.PSTR
class QUERY_SERVICE_CONFIGW(Structure):
    dwServiceType: win32more.Windows.Win32.System.Services.ENUM_SERVICE_TYPE
    dwStartType: win32more.Windows.Win32.System.Services.SERVICE_START_TYPE
    dwErrorControl: win32more.Windows.Win32.System.Services.SERVICE_ERROR
    lpBinaryPathName: win32more.Windows.Win32.Foundation.PWSTR
    lpLoadOrderGroup: win32more.Windows.Win32.Foundation.PWSTR
    dwTagId: UInt32
    lpDependencies: win32more.Windows.Win32.Foundation.PWSTR
    lpServiceStartName: win32more.Windows.Win32.Foundation.PWSTR
    lpDisplayName: win32more.Windows.Win32.Foundation.PWSTR
QUERY_SERVICE_CONFIG = UnicodeAlias('QUERY_SERVICE_CONFIGW')
class QUERY_SERVICE_LOCK_STATUSA(Structure):
    fIsLocked: UInt32
    lpLockOwner: win32more.Windows.Win32.Foundation.PSTR
    dwLockDuration: UInt32
class QUERY_SERVICE_LOCK_STATUSW(Structure):
    fIsLocked: UInt32
    lpLockOwner: win32more.Windows.Win32.Foundation.PWSTR
    dwLockDuration: UInt32
QUERY_SERVICE_LOCK_STATUS = UnicodeAlias('QUERY_SERVICE_LOCK_STATUSW')
class SC_ACTION(Structure):
    Type: win32more.Windows.Win32.System.Services.SC_ACTION_TYPE
    Delay: UInt32
SC_ACTION_TYPE = Int32
SC_ACTION_NONE: win32more.Windows.Win32.System.Services.SC_ACTION_TYPE = 0
SC_ACTION_RESTART: win32more.Windows.Win32.System.Services.SC_ACTION_TYPE = 1
SC_ACTION_REBOOT: win32more.Windows.Win32.System.Services.SC_ACTION_TYPE = 2
SC_ACTION_RUN_COMMAND: win32more.Windows.Win32.System.Services.SC_ACTION_TYPE = 3
SC_ACTION_OWN_RESTART: win32more.Windows.Win32.System.Services.SC_ACTION_TYPE = 4
SC_ENUM_TYPE = Int32
SC_ENUM_PROCESS_INFO: win32more.Windows.Win32.System.Services.SC_ENUM_TYPE = 0
SC_EVENT_TYPE = Int32
SC_EVENT_DATABASE_CHANGE: win32more.Windows.Win32.System.Services.SC_EVENT_TYPE = 0
SC_EVENT_PROPERTY_CHANGE: win32more.Windows.Win32.System.Services.SC_EVENT_TYPE = 1
SC_EVENT_STATUS_CHANGE: win32more.Windows.Win32.System.Services.SC_EVENT_TYPE = 2
SC_HANDLE = VoidPtr
SC_STATUS_TYPE = Int32
SC_STATUS_PROCESS_INFO: win32more.Windows.Win32.System.Services.SC_STATUS_TYPE = 0
SERVICE_CONFIG = UInt32
SERVICE_CONFIG_DELAYED_AUTO_START_INFO: win32more.Windows.Win32.System.Services.SERVICE_CONFIG = 3
SERVICE_CONFIG_DESCRIPTION: win32more.Windows.Win32.System.Services.SERVICE_CONFIG = 1
SERVICE_CONFIG_FAILURE_ACTIONS: win32more.Windows.Win32.System.Services.SERVICE_CONFIG = 2
SERVICE_CONFIG_FAILURE_ACTIONS_FLAG: win32more.Windows.Win32.System.Services.SERVICE_CONFIG = 4
SERVICE_CONFIG_PREFERRED_NODE: win32more.Windows.Win32.System.Services.SERVICE_CONFIG = 9
SERVICE_CONFIG_PRESHUTDOWN_INFO: win32more.Windows.Win32.System.Services.SERVICE_CONFIG = 7
SERVICE_CONFIG_REQUIRED_PRIVILEGES_INFO: win32more.Windows.Win32.System.Services.SERVICE_CONFIG = 6
SERVICE_CONFIG_SERVICE_SID_INFO: win32more.Windows.Win32.System.Services.SERVICE_CONFIG = 5
SERVICE_CONFIG_TRIGGER_INFO: win32more.Windows.Win32.System.Services.SERVICE_CONFIG = 8
SERVICE_CONFIG_LAUNCH_PROTECTED: win32more.Windows.Win32.System.Services.SERVICE_CONFIG = 12
class SERVICE_CONTROL_STATUS_REASON_PARAMSA(Structure):
    dwReason: UInt32
    pszComment: win32more.Windows.Win32.Foundation.PSTR
    ServiceStatus: win32more.Windows.Win32.System.Services.SERVICE_STATUS_PROCESS
class SERVICE_CONTROL_STATUS_REASON_PARAMSW(Structure):
    dwReason: UInt32
    pszComment: win32more.Windows.Win32.Foundation.PWSTR
    ServiceStatus: win32more.Windows.Win32.System.Services.SERVICE_STATUS_PROCESS
SERVICE_CONTROL_STATUS_REASON_PARAMS = UnicodeAlias('SERVICE_CONTROL_STATUS_REASON_PARAMSW')
class SERVICE_CUSTOM_SYSTEM_STATE_CHANGE_DATA_ITEM(Structure):
    u: _u_e__Union
    class _u_e__Union(Union):
        CustomStateId: win32more.Windows.Win32.System.Services.SERVICE_TRIGGER_CUSTOM_STATE_ID
        s: _s_e__Struct
        class _s_e__Struct(Structure):
            DataOffset: UInt32
            Data: Byte * 1
class SERVICE_DELAYED_AUTO_START_INFO(Structure):
    fDelayedAutostart: win32more.Windows.Win32.Foundation.BOOL
class SERVICE_DESCRIPTIONA(Structure):
    lpDescription: win32more.Windows.Win32.Foundation.PSTR
class SERVICE_DESCRIPTIONW(Structure):
    lpDescription: win32more.Windows.Win32.Foundation.PWSTR
SERVICE_DESCRIPTION = UnicodeAlias('SERVICE_DESCRIPTIONW')
SERVICE_DIRECTORY_TYPE = Int32
ServiceDirectoryPersistentState: win32more.Windows.Win32.System.Services.SERVICE_DIRECTORY_TYPE = 0
ServiceDirectoryTypeMax: win32more.Windows.Win32.System.Services.SERVICE_DIRECTORY_TYPE = 1
SERVICE_ERROR = UInt32
SERVICE_ERROR_CRITICAL: win32more.Windows.Win32.System.Services.SERVICE_ERROR = 3
SERVICE_ERROR_IGNORE: win32more.Windows.Win32.System.Services.SERVICE_ERROR = 0
SERVICE_ERROR_NORMAL: win32more.Windows.Win32.System.Services.SERVICE_ERROR = 1
SERVICE_ERROR_SEVERE: win32more.Windows.Win32.System.Services.SERVICE_ERROR = 2
class SERVICE_FAILURE_ACTIONSA(Structure):
    dwResetPeriod: UInt32
    lpRebootMsg: win32more.Windows.Win32.Foundation.PSTR
    lpCommand: win32more.Windows.Win32.Foundation.PSTR
    cActions: UInt32
    lpsaActions: POINTER(win32more.Windows.Win32.System.Services.SC_ACTION)
class SERVICE_FAILURE_ACTIONSW(Structure):
    dwResetPeriod: UInt32
    lpRebootMsg: win32more.Windows.Win32.Foundation.PWSTR
    lpCommand: win32more.Windows.Win32.Foundation.PWSTR
    cActions: UInt32
    lpsaActions: POINTER(win32more.Windows.Win32.System.Services.SC_ACTION)
SERVICE_FAILURE_ACTIONS = UnicodeAlias('SERVICE_FAILURE_ACTIONSW')
class SERVICE_FAILURE_ACTIONS_FLAG(Structure):
    fFailureActionsOnNonCrashFailures: win32more.Windows.Win32.Foundation.BOOL
class SERVICE_LAUNCH_PROTECTED_INFO(Structure):
    dwLaunchProtected: UInt32
@winfunctype_pointer
def SERVICE_MAIN_FUNCTIONA(dwNumServicesArgs: UInt32, lpServiceArgVectors: POINTER(POINTER(SByte))) -> Void: ...
@winfunctype_pointer
def SERVICE_MAIN_FUNCTIONW(dwNumServicesArgs: UInt32, lpServiceArgVectors: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> Void: ...
SERVICE_MAIN_FUNCTION = UnicodeAlias('SERVICE_MAIN_FUNCTIONW')
SERVICE_NOTIFY = UInt32
SERVICE_NOTIFY_CREATED: win32more.Windows.Win32.System.Services.SERVICE_NOTIFY = 128
SERVICE_NOTIFY_CONTINUE_PENDING: win32more.Windows.Win32.System.Services.SERVICE_NOTIFY = 16
SERVICE_NOTIFY_DELETE_PENDING: win32more.Windows.Win32.System.Services.SERVICE_NOTIFY = 512
SERVICE_NOTIFY_DELETED: win32more.Windows.Win32.System.Services.SERVICE_NOTIFY = 256
SERVICE_NOTIFY_PAUSE_PENDING: win32more.Windows.Win32.System.Services.SERVICE_NOTIFY = 32
SERVICE_NOTIFY_PAUSED: win32more.Windows.Win32.System.Services.SERVICE_NOTIFY = 64
SERVICE_NOTIFY_RUNNING: win32more.Windows.Win32.System.Services.SERVICE_NOTIFY = 8
SERVICE_NOTIFY_START_PENDING: win32more.Windows.Win32.System.Services.SERVICE_NOTIFY = 2
SERVICE_NOTIFY_STOP_PENDING: win32more.Windows.Win32.System.Services.SERVICE_NOTIFY = 4
SERVICE_NOTIFY_STOPPED: win32more.Windows.Win32.System.Services.SERVICE_NOTIFY = 1
class SERVICE_NOTIFY_1(Structure):
    dwVersion: UInt32
    pfnNotifyCallback: win32more.Windows.Win32.System.Services.PFN_SC_NOTIFY_CALLBACK
    pContext: VoidPtr
    dwNotificationStatus: UInt32
    ServiceStatus: win32more.Windows.Win32.System.Services.SERVICE_STATUS_PROCESS
class SERVICE_NOTIFY_2A(Structure):
    dwVersion: UInt32
    pfnNotifyCallback: win32more.Windows.Win32.System.Services.PFN_SC_NOTIFY_CALLBACK
    pContext: VoidPtr
    dwNotificationStatus: UInt32
    ServiceStatus: win32more.Windows.Win32.System.Services.SERVICE_STATUS_PROCESS
    dwNotificationTriggered: UInt32
    pszServiceNames: win32more.Windows.Win32.Foundation.PSTR
class SERVICE_NOTIFY_2W(Structure):
    dwVersion: UInt32
    pfnNotifyCallback: win32more.Windows.Win32.System.Services.PFN_SC_NOTIFY_CALLBACK
    pContext: VoidPtr
    dwNotificationStatus: UInt32
    ServiceStatus: win32more.Windows.Win32.System.Services.SERVICE_STATUS_PROCESS
    dwNotificationTriggered: UInt32
    pszServiceNames: win32more.Windows.Win32.Foundation.PWSTR
SERVICE_NOTIFY_2 = UnicodeAlias('SERVICE_NOTIFY_2W')
class SERVICE_PREFERRED_NODE_INFO(Structure):
    usPreferredNode: UInt16
    fDelete: win32more.Windows.Win32.Foundation.BOOLEAN
class SERVICE_PRESHUTDOWN_INFO(Structure):
    dwPreshutdownTimeout: UInt32
SERVICE_REGISTRY_STATE_TYPE = Int32
ServiceRegistryStateParameters: win32more.Windows.Win32.System.Services.SERVICE_REGISTRY_STATE_TYPE = 0
ServiceRegistryStatePersistent: win32more.Windows.Win32.System.Services.SERVICE_REGISTRY_STATE_TYPE = 1
MaxServiceRegistryStateType: win32more.Windows.Win32.System.Services.SERVICE_REGISTRY_STATE_TYPE = 2
class SERVICE_REQUIRED_PRIVILEGES_INFOA(Structure):
    pmszRequiredPrivileges: win32more.Windows.Win32.Foundation.PSTR
class SERVICE_REQUIRED_PRIVILEGES_INFOW(Structure):
    pmszRequiredPrivileges: win32more.Windows.Win32.Foundation.PWSTR
SERVICE_REQUIRED_PRIVILEGES_INFO = UnicodeAlias('SERVICE_REQUIRED_PRIVILEGES_INFOW')
SERVICE_RUNS_IN_PROCESS = UInt32
SERVICE_RUNS_IN_NON_SYSTEM_OR_NOT_RUNNING: win32more.Windows.Win32.System.Services.SERVICE_RUNS_IN_PROCESS = 0
SERVICE_RUNS_IN_SYSTEM_PROCESS: win32more.Windows.Win32.System.Services.SERVICE_RUNS_IN_PROCESS = 1
SERVICE_SHARED_DIRECTORY_TYPE = Int32
ServiceSharedDirectoryPersistentState: win32more.Windows.Win32.System.Services.SERVICE_SHARED_DIRECTORY_TYPE = 0
SERVICE_SHARED_REGISTRY_STATE_TYPE = Int32
ServiceSharedRegistryPersistentState: win32more.Windows.Win32.System.Services.SERVICE_SHARED_REGISTRY_STATE_TYPE = 0
class SERVICE_SID_INFO(Structure):
    dwServiceSidType: UInt32
class SERVICE_START_REASON(Structure):
    dwReason: UInt32
SERVICE_START_TYPE = UInt32
SERVICE_AUTO_START: win32more.Windows.Win32.System.Services.SERVICE_START_TYPE = 2
SERVICE_BOOT_START: win32more.Windows.Win32.System.Services.SERVICE_START_TYPE = 0
SERVICE_DEMAND_START: win32more.Windows.Win32.System.Services.SERVICE_START_TYPE = 3
SERVICE_DISABLED: win32more.Windows.Win32.System.Services.SERVICE_START_TYPE = 4
SERVICE_SYSTEM_START: win32more.Windows.Win32.System.Services.SERVICE_START_TYPE = 1
class SERVICE_STATUS(Structure):
    dwServiceType: win32more.Windows.Win32.System.Services.ENUM_SERVICE_TYPE
    dwCurrentState: win32more.Windows.Win32.System.Services.SERVICE_STATUS_CURRENT_STATE
    dwControlsAccepted: UInt32
    dwWin32ExitCode: UInt32
    dwServiceSpecificExitCode: UInt32
    dwCheckPoint: UInt32
    dwWaitHint: UInt32
SERVICE_STATUS_CURRENT_STATE = UInt32
SERVICE_CONTINUE_PENDING: win32more.Windows.Win32.System.Services.SERVICE_STATUS_CURRENT_STATE = 5
SERVICE_PAUSE_PENDING: win32more.Windows.Win32.System.Services.SERVICE_STATUS_CURRENT_STATE = 6
SERVICE_PAUSED: win32more.Windows.Win32.System.Services.SERVICE_STATUS_CURRENT_STATE = 7
SERVICE_RUNNING: win32more.Windows.Win32.System.Services.SERVICE_STATUS_CURRENT_STATE = 4
SERVICE_START_PENDING: win32more.Windows.Win32.System.Services.SERVICE_STATUS_CURRENT_STATE = 2
SERVICE_STOP_PENDING: win32more.Windows.Win32.System.Services.SERVICE_STATUS_CURRENT_STATE = 3
SERVICE_STOPPED: win32more.Windows.Win32.System.Services.SERVICE_STATUS_CURRENT_STATE = 1
SERVICE_STATUS_HANDLE = VoidPtr
class SERVICE_STATUS_PROCESS(Structure):
    dwServiceType: win32more.Windows.Win32.System.Services.ENUM_SERVICE_TYPE
    dwCurrentState: win32more.Windows.Win32.System.Services.SERVICE_STATUS_CURRENT_STATE
    dwControlsAccepted: UInt32
    dwWin32ExitCode: UInt32
    dwServiceSpecificExitCode: UInt32
    dwCheckPoint: UInt32
    dwWaitHint: UInt32
    dwProcessId: UInt32
    dwServiceFlags: win32more.Windows.Win32.System.Services.SERVICE_RUNS_IN_PROCESS
class SERVICE_TABLE_ENTRYA(Structure):
    lpServiceName: win32more.Windows.Win32.Foundation.PSTR
    lpServiceProc: win32more.Windows.Win32.System.Services.LPSERVICE_MAIN_FUNCTIONA
class SERVICE_TABLE_ENTRYW(Structure):
    lpServiceName: win32more.Windows.Win32.Foundation.PWSTR
    lpServiceProc: win32more.Windows.Win32.System.Services.LPSERVICE_MAIN_FUNCTIONW
SERVICE_TABLE_ENTRY = UnicodeAlias('SERVICE_TABLE_ENTRYW')
class SERVICE_TIMECHANGE_INFO(Structure):
    liNewTime: Int64
    liOldTime: Int64
class SERVICE_TRIGGER(Structure):
    dwTriggerType: win32more.Windows.Win32.System.Services.SERVICE_TRIGGER_TYPE
    dwAction: win32more.Windows.Win32.System.Services.SERVICE_TRIGGER_ACTION
    pTriggerSubtype: POINTER(Guid)
    cDataItems: UInt32
    pDataItems: POINTER(win32more.Windows.Win32.System.Services.SERVICE_TRIGGER_SPECIFIC_DATA_ITEM)
SERVICE_TRIGGER_ACTION = UInt32
SERVICE_TRIGGER_ACTION_SERVICE_START: win32more.Windows.Win32.System.Services.SERVICE_TRIGGER_ACTION = 1
SERVICE_TRIGGER_ACTION_SERVICE_STOP: win32more.Windows.Win32.System.Services.SERVICE_TRIGGER_ACTION = 2
class SERVICE_TRIGGER_CUSTOM_STATE_ID(Structure):
    Data: UInt32 * 2
class SERVICE_TRIGGER_INFO(Structure):
    cTriggers: UInt32
    pTriggers: POINTER(win32more.Windows.Win32.System.Services.SERVICE_TRIGGER)
    pReserved: POINTER(Byte)
class SERVICE_TRIGGER_SPECIFIC_DATA_ITEM(Structure):
    dwDataType: win32more.Windows.Win32.System.Services.SERVICE_TRIGGER_SPECIFIC_DATA_ITEM_DATA_TYPE
    cbData: UInt32
    pData: POINTER(Byte)
SERVICE_TRIGGER_SPECIFIC_DATA_ITEM_DATA_TYPE = UInt32
SERVICE_TRIGGER_DATA_TYPE_BINARY: win32more.Windows.Win32.System.Services.SERVICE_TRIGGER_SPECIFIC_DATA_ITEM_DATA_TYPE = 1
SERVICE_TRIGGER_DATA_TYPE_STRING: win32more.Windows.Win32.System.Services.SERVICE_TRIGGER_SPECIFIC_DATA_ITEM_DATA_TYPE = 2
SERVICE_TRIGGER_DATA_TYPE_LEVEL: win32more.Windows.Win32.System.Services.SERVICE_TRIGGER_SPECIFIC_DATA_ITEM_DATA_TYPE = 3
SERVICE_TRIGGER_DATA_TYPE_KEYWORD_ANY: win32more.Windows.Win32.System.Services.SERVICE_TRIGGER_SPECIFIC_DATA_ITEM_DATA_TYPE = 4
SERVICE_TRIGGER_DATA_TYPE_KEYWORD_ALL: win32more.Windows.Win32.System.Services.SERVICE_TRIGGER_SPECIFIC_DATA_ITEM_DATA_TYPE = 5
SERVICE_TRIGGER_TYPE = UInt32
SERVICE_TRIGGER_TYPE_CUSTOM: win32more.Windows.Win32.System.Services.SERVICE_TRIGGER_TYPE = 20
SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL: win32more.Windows.Win32.System.Services.SERVICE_TRIGGER_TYPE = 1
SERVICE_TRIGGER_TYPE_DOMAIN_JOIN: win32more.Windows.Win32.System.Services.SERVICE_TRIGGER_TYPE = 3
SERVICE_TRIGGER_TYPE_FIREWALL_PORT_EVENT: win32more.Windows.Win32.System.Services.SERVICE_TRIGGER_TYPE = 4
SERVICE_TRIGGER_TYPE_GROUP_POLICY: win32more.Windows.Win32.System.Services.SERVICE_TRIGGER_TYPE = 5
SERVICE_TRIGGER_TYPE_IP_ADDRESS_AVAILABILITY: win32more.Windows.Win32.System.Services.SERVICE_TRIGGER_TYPE = 2
SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT: win32more.Windows.Win32.System.Services.SERVICE_TRIGGER_TYPE = 6


make_ready(__name__)
