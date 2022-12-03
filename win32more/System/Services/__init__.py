from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Security
import win32more.System.Registry
import win32more.System.Services
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
def _define__SC_NOTIFICATION_REGISTRATION_head():
    class _SC_NOTIFICATION_REGISTRATION(Structure):
        pass
    return _SC_NOTIFICATION_REGISTRATION
def _define__SC_NOTIFICATION_REGISTRATION():
    _SC_NOTIFICATION_REGISTRATION = win32more.System.Services._SC_NOTIFICATION_REGISTRATION_head
    return _SC_NOTIFICATION_REGISTRATION
SERVICE_ALL_ACCESS = 983551
SC_MANAGER_ALL_ACCESS = 983103
SERVICES_ACTIVE_DATABASEW = 'ServicesActive'
SERVICES_FAILED_DATABASEW = 'ServicesFailed'
SERVICES_ACTIVE_DATABASEA = 'ServicesActive'
SERVICES_FAILED_DATABASEA = 'ServicesFailed'
SERVICES_ACTIVE_DATABASE = 'ServicesActive'
SERVICES_FAILED_DATABASE = 'ServicesFailed'
SERVICE_NO_CHANGE = 4294967295
SERVICE_CONTROL_STOP = 1
SERVICE_CONTROL_PAUSE = 2
SERVICE_CONTROL_CONTINUE = 3
SERVICE_CONTROL_INTERROGATE = 4
SERVICE_CONTROL_SHUTDOWN = 5
SERVICE_CONTROL_PARAMCHANGE = 6
SERVICE_CONTROL_NETBINDADD = 7
SERVICE_CONTROL_NETBINDREMOVE = 8
SERVICE_CONTROL_NETBINDENABLE = 9
SERVICE_CONTROL_NETBINDDISABLE = 10
SERVICE_CONTROL_DEVICEEVENT = 11
SERVICE_CONTROL_HARDWAREPROFILECHANGE = 12
SERVICE_CONTROL_POWEREVENT = 13
SERVICE_CONTROL_SESSIONCHANGE = 14
SERVICE_CONTROL_PRESHUTDOWN = 15
SERVICE_CONTROL_TIMECHANGE = 16
SERVICE_CONTROL_TRIGGEREVENT = 32
SERVICE_CONTROL_LOWRESOURCES = 96
SERVICE_CONTROL_SYSTEMLOWRESOURCES = 97
SERVICE_ACCEPT_STOP = 1
SERVICE_ACCEPT_PAUSE_CONTINUE = 2
SERVICE_ACCEPT_SHUTDOWN = 4
SERVICE_ACCEPT_PARAMCHANGE = 8
SERVICE_ACCEPT_NETBINDCHANGE = 16
SERVICE_ACCEPT_HARDWAREPROFILECHANGE = 32
SERVICE_ACCEPT_POWEREVENT = 64
SERVICE_ACCEPT_SESSIONCHANGE = 128
SERVICE_ACCEPT_PRESHUTDOWN = 256
SERVICE_ACCEPT_TIMECHANGE = 512
SERVICE_ACCEPT_TRIGGEREVENT = 1024
SERVICE_ACCEPT_USER_LOGOFF = 2048
SERVICE_ACCEPT_LOWRESOURCES = 8192
SERVICE_ACCEPT_SYSTEMLOWRESOURCES = 16384
SC_MANAGER_CONNECT = 1
SC_MANAGER_CREATE_SERVICE = 2
SC_MANAGER_ENUMERATE_SERVICE = 4
SC_MANAGER_LOCK = 8
SC_MANAGER_QUERY_LOCK_STATUS = 16
SC_MANAGER_MODIFY_BOOT_CONFIG = 32
SERVICE_QUERY_CONFIG = 1
SERVICE_CHANGE_CONFIG = 2
SERVICE_QUERY_STATUS = 4
SERVICE_ENUMERATE_DEPENDENTS = 8
SERVICE_START = 16
SERVICE_STOP = 32
SERVICE_PAUSE_CONTINUE = 64
SERVICE_INTERROGATE = 128
SERVICE_USER_DEFINED_CONTROL = 256
SERVICE_NOTIFY_STATUS_CHANGE_1 = 1
SERVICE_NOTIFY_STATUS_CHANGE_2 = 2
SERVICE_NOTIFY_STATUS_CHANGE = 2
SERVICE_STOP_REASON_FLAG_MIN = 0
SERVICE_STOP_REASON_FLAG_UNPLANNED = 268435456
SERVICE_STOP_REASON_FLAG_CUSTOM = 536870912
SERVICE_STOP_REASON_FLAG_PLANNED = 1073741824
SERVICE_STOP_REASON_FLAG_MAX = 2147483648
SERVICE_STOP_REASON_MAJOR_MIN = 0
SERVICE_STOP_REASON_MAJOR_OTHER = 65536
SERVICE_STOP_REASON_MAJOR_HARDWARE = 131072
SERVICE_STOP_REASON_MAJOR_OPERATINGSYSTEM = 196608
SERVICE_STOP_REASON_MAJOR_SOFTWARE = 262144
SERVICE_STOP_REASON_MAJOR_APPLICATION = 327680
SERVICE_STOP_REASON_MAJOR_NONE = 393216
SERVICE_STOP_REASON_MAJOR_MAX = 458752
SERVICE_STOP_REASON_MAJOR_MIN_CUSTOM = 4194304
SERVICE_STOP_REASON_MAJOR_MAX_CUSTOM = 16711680
SERVICE_STOP_REASON_MINOR_MIN = 0
SERVICE_STOP_REASON_MINOR_OTHER = 1
SERVICE_STOP_REASON_MINOR_MAINTENANCE = 2
SERVICE_STOP_REASON_MINOR_INSTALLATION = 3
SERVICE_STOP_REASON_MINOR_UPGRADE = 4
SERVICE_STOP_REASON_MINOR_RECONFIG = 5
SERVICE_STOP_REASON_MINOR_HUNG = 6
SERVICE_STOP_REASON_MINOR_UNSTABLE = 7
SERVICE_STOP_REASON_MINOR_DISK = 8
SERVICE_STOP_REASON_MINOR_NETWORKCARD = 9
SERVICE_STOP_REASON_MINOR_ENVIRONMENT = 10
SERVICE_STOP_REASON_MINOR_HARDWARE_DRIVER = 11
SERVICE_STOP_REASON_MINOR_OTHERDRIVER = 12
SERVICE_STOP_REASON_MINOR_SERVICEPACK = 13
SERVICE_STOP_REASON_MINOR_SOFTWARE_UPDATE = 14
SERVICE_STOP_REASON_MINOR_SECURITYFIX = 15
SERVICE_STOP_REASON_MINOR_SECURITY = 16
SERVICE_STOP_REASON_MINOR_NETWORK_CONNECTIVITY = 17
SERVICE_STOP_REASON_MINOR_WMI = 18
SERVICE_STOP_REASON_MINOR_SERVICEPACK_UNINSTALL = 19
SERVICE_STOP_REASON_MINOR_SOFTWARE_UPDATE_UNINSTALL = 20
SERVICE_STOP_REASON_MINOR_SECURITYFIX_UNINSTALL = 21
SERVICE_STOP_REASON_MINOR_MMC = 22
SERVICE_STOP_REASON_MINOR_NONE = 23
SERVICE_STOP_REASON_MINOR_MEMOTYLIMIT = 24
SERVICE_STOP_REASON_MINOR_MAX = 25
SERVICE_STOP_REASON_MINOR_MIN_CUSTOM = 256
SERVICE_STOP_REASON_MINOR_MAX_CUSTOM = 65535
SERVICE_CONTROL_STATUS_REASON_INFO = 1
SERVICE_SID_TYPE_NONE = 0
SERVICE_SID_TYPE_UNRESTRICTED = 1
SERVICE_TRIGGER_TYPE_CUSTOM_SYSTEM_STATE_CHANGE = 7
SERVICE_TRIGGER_TYPE_AGGREGATE = 30
SERVICE_START_REASON_DEMAND = 1
SERVICE_START_REASON_AUTO = 2
SERVICE_START_REASON_TRIGGER = 4
SERVICE_START_REASON_RESTART_ON_FAILURE = 8
SERVICE_START_REASON_DELAYEDAUTO = 16
SERVICE_DYNAMIC_INFORMATION_LEVEL_START_REASON = 1
SERVICE_LAUNCH_PROTECTED_NONE = 0
SERVICE_LAUNCH_PROTECTED_WINDOWS = 1
SERVICE_LAUNCH_PROTECTED_WINDOWS_LIGHT = 2
SERVICE_LAUNCH_PROTECTED_ANTIMALWARE_LIGHT = 3
def _define_NETWORK_MANAGER_FIRST_IP_ADDRESS_ARRIVAL_GUID():
    return Guid('4f27f2de-14e2-430b-a5-49-7c-d4-8c-bc-82-45')
def _define_NETWORK_MANAGER_LAST_IP_ADDRESS_REMOVAL_GUID():
    return Guid('cc4ba62a-162e-4648-84-7a-b6-bd-f9-93-e3-35')
def _define_DOMAIN_JOIN_GUID():
    return Guid('1ce20aba-9851-4421-94-30-1d-de-b7-66-e8-09')
def _define_DOMAIN_LEAVE_GUID():
    return Guid('ddaf516e-58c2-4866-95-74-c3-b6-15-d4-2e-a1')
def _define_FIREWALL_PORT_OPEN_GUID():
    return Guid('b7569e07-8421-4ee0-ad-10-86-91-5a-fd-ad-09')
def _define_FIREWALL_PORT_CLOSE_GUID():
    return Guid('a144ed38-8e12-4de4-9d-96-e6-47-40-b1-a5-24')
def _define_MACHINE_POLICY_PRESENT_GUID():
    return Guid('659fcae6-5bdb-4da9-b1-ff-ca-2a-17-8d-46-e0')
def _define_USER_POLICY_PRESENT_GUID():
    return Guid('54fb46c8-f089-464c-b1-fd-59-d1-b6-2c-3b-50')
def _define_RPC_INTERFACE_EVENT_GUID():
    return Guid('bc90d167-9470-4139-a9-ba-be-0b-bb-f5-b7-4d')
def _define_NAMED_PIPE_EVENT_GUID():
    return Guid('1f81d131-3fac-4537-9e-0c-7e-7b-0c-2f-4b-55')
def _define_CUSTOM_SYSTEM_STATE_CHANGE_EVENT_GUID():
    return Guid('2d7a2816-0c5e-45fc-9c-e7-57-0e-5e-cd-e9-c9')
SERVICE_TRIGGER_STARTED_ARGUMENT = 'TriggerStarted'
SC_AGGREGATE_STORAGE_KEY = 'System\\CurrentControlSet\\Control\\ServiceAggregatedEvents'
def _define_SetServiceBits():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.Services.SERVICE_STATUS_HANDLE,UInt32,win32more.Foundation.BOOL,win32more.Foundation.BOOL)(('SetServiceBits', windll['ADVAPI32.dll']), ((1, 'hServiceStatus'),(1, 'dwServiceBits'),(1, 'bSetBitsOn'),(1, 'bUpdateImmediately'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ChangeServiceConfigA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.SC_HANDLE,UInt32,win32more.System.Services.SERVICE_START_TYPE,win32more.System.Services.SERVICE_ERROR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(UInt32),win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR)(('ChangeServiceConfigA', windll['ADVAPI32.dll']), ((1, 'hService'),(1, 'dwServiceType'),(1, 'dwStartType'),(1, 'dwErrorControl'),(1, 'lpBinaryPathName'),(1, 'lpLoadOrderGroup'),(1, 'lpdwTagId'),(1, 'lpDependencies'),(1, 'lpServiceStartName'),(1, 'lpPassword'),(1, 'lpDisplayName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ChangeServiceConfigW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.SC_HANDLE,UInt32,win32more.System.Services.SERVICE_START_TYPE,win32more.System.Services.SERVICE_ERROR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('ChangeServiceConfigW', windll['ADVAPI32.dll']), ((1, 'hService'),(1, 'dwServiceType'),(1, 'dwStartType'),(1, 'dwErrorControl'),(1, 'lpBinaryPathName'),(1, 'lpLoadOrderGroup'),(1, 'lpdwTagId'),(1, 'lpDependencies'),(1, 'lpServiceStartName'),(1, 'lpPassword'),(1, 'lpDisplayName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ChangeServiceConfig2A():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.SC_HANDLE,win32more.System.Services.SERVICE_CONFIG,c_void_p)(('ChangeServiceConfig2A', windll['ADVAPI32.dll']), ((1, 'hService'),(1, 'dwInfoLevel'),(1, 'lpInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ChangeServiceConfig2W():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.SC_HANDLE,win32more.System.Services.SERVICE_CONFIG,c_void_p)(('ChangeServiceConfig2W', windll['ADVAPI32.dll']), ((1, 'hService'),(1, 'dwInfoLevel'),(1, 'lpInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CloseServiceHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.SC_HANDLE)(('CloseServiceHandle', windll['ADVAPI32.dll']), ((1, 'hSCObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ControlService():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.SC_HANDLE,UInt32,POINTER(win32more.System.Services.SERVICE_STATUS_head))(('ControlService', windll['ADVAPI32.dll']), ((1, 'hService'),(1, 'dwControl'),(1, 'lpServiceStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateServiceA():
    try:
        return WINFUNCTYPE(win32more.Security.SC_HANDLE,win32more.Security.SC_HANDLE,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32,win32more.System.Services.ENUM_SERVICE_TYPE,win32more.System.Services.SERVICE_START_TYPE,win32more.System.Services.SERVICE_ERROR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(UInt32),win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR)(('CreateServiceA', windll['ADVAPI32.dll']), ((1, 'hSCManager'),(1, 'lpServiceName'),(1, 'lpDisplayName'),(1, 'dwDesiredAccess'),(1, 'dwServiceType'),(1, 'dwStartType'),(1, 'dwErrorControl'),(1, 'lpBinaryPathName'),(1, 'lpLoadOrderGroup'),(1, 'lpdwTagId'),(1, 'lpDependencies'),(1, 'lpServiceStartName'),(1, 'lpPassword'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateServiceW():
    try:
        return WINFUNCTYPE(win32more.Security.SC_HANDLE,win32more.Security.SC_HANDLE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,win32more.System.Services.ENUM_SERVICE_TYPE,win32more.System.Services.SERVICE_START_TYPE,win32more.System.Services.SERVICE_ERROR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('CreateServiceW', windll['ADVAPI32.dll']), ((1, 'hSCManager'),(1, 'lpServiceName'),(1, 'lpDisplayName'),(1, 'dwDesiredAccess'),(1, 'dwServiceType'),(1, 'dwStartType'),(1, 'dwErrorControl'),(1, 'lpBinaryPathName'),(1, 'lpLoadOrderGroup'),(1, 'lpdwTagId'),(1, 'lpDependencies'),(1, 'lpServiceStartName'),(1, 'lpPassword'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeleteService():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.SC_HANDLE)(('DeleteService', windll['ADVAPI32.dll']), ((1, 'hService'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumDependentServicesA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.SC_HANDLE,win32more.System.Services.ENUM_SERVICE_STATE,POINTER(win32more.System.Services.ENUM_SERVICE_STATUSA_head),UInt32,POINTER(UInt32),POINTER(UInt32))(('EnumDependentServicesA', windll['ADVAPI32.dll']), ((1, 'hService'),(1, 'dwServiceState'),(1, 'lpServices'),(1, 'cbBufSize'),(1, 'pcbBytesNeeded'),(1, 'lpServicesReturned'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumDependentServicesW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.SC_HANDLE,win32more.System.Services.ENUM_SERVICE_STATE,POINTER(win32more.System.Services.ENUM_SERVICE_STATUSW_head),UInt32,POINTER(UInt32),POINTER(UInt32))(('EnumDependentServicesW', windll['ADVAPI32.dll']), ((1, 'hService'),(1, 'dwServiceState'),(1, 'lpServices'),(1, 'cbBufSize'),(1, 'pcbBytesNeeded'),(1, 'lpServicesReturned'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumServicesStatusA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.SC_HANDLE,win32more.System.Services.ENUM_SERVICE_TYPE,win32more.System.Services.ENUM_SERVICE_STATE,POINTER(win32more.System.Services.ENUM_SERVICE_STATUSA_head),UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32))(('EnumServicesStatusA', windll['ADVAPI32.dll']), ((1, 'hSCManager'),(1, 'dwServiceType'),(1, 'dwServiceState'),(1, 'lpServices'),(1, 'cbBufSize'),(1, 'pcbBytesNeeded'),(1, 'lpServicesReturned'),(1, 'lpResumeHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumServicesStatusW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.SC_HANDLE,win32more.System.Services.ENUM_SERVICE_TYPE,win32more.System.Services.ENUM_SERVICE_STATE,POINTER(win32more.System.Services.ENUM_SERVICE_STATUSW_head),UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32))(('EnumServicesStatusW', windll['ADVAPI32.dll']), ((1, 'hSCManager'),(1, 'dwServiceType'),(1, 'dwServiceState'),(1, 'lpServices'),(1, 'cbBufSize'),(1, 'pcbBytesNeeded'),(1, 'lpServicesReturned'),(1, 'lpResumeHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumServicesStatusExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.SC_HANDLE,win32more.System.Services.SC_ENUM_TYPE,win32more.System.Services.ENUM_SERVICE_TYPE,win32more.System.Services.ENUM_SERVICE_STATE,c_char_p_no,UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32),win32more.Foundation.PSTR)(('EnumServicesStatusExA', windll['ADVAPI32.dll']), ((1, 'hSCManager'),(1, 'InfoLevel'),(1, 'dwServiceType'),(1, 'dwServiceState'),(1, 'lpServices'),(1, 'cbBufSize'),(1, 'pcbBytesNeeded'),(1, 'lpServicesReturned'),(1, 'lpResumeHandle'),(1, 'pszGroupName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumServicesStatusExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.SC_HANDLE,win32more.System.Services.SC_ENUM_TYPE,win32more.System.Services.ENUM_SERVICE_TYPE,win32more.System.Services.ENUM_SERVICE_STATE,c_char_p_no,UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32),win32more.Foundation.PWSTR)(('EnumServicesStatusExW', windll['ADVAPI32.dll']), ((1, 'hSCManager'),(1, 'InfoLevel'),(1, 'dwServiceType'),(1, 'dwServiceState'),(1, 'lpServices'),(1, 'cbBufSize'),(1, 'pcbBytesNeeded'),(1, 'lpServicesReturned'),(1, 'lpResumeHandle'),(1, 'pszGroupName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetServiceKeyNameA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.SC_HANDLE,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(UInt32))(('GetServiceKeyNameA', windll['ADVAPI32.dll']), ((1, 'hSCManager'),(1, 'lpDisplayName'),(1, 'lpServiceName'),(1, 'lpcchBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetServiceKeyNameW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.SC_HANDLE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32))(('GetServiceKeyNameW', windll['ADVAPI32.dll']), ((1, 'hSCManager'),(1, 'lpDisplayName'),(1, 'lpServiceName'),(1, 'lpcchBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetServiceDisplayNameA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.SC_HANDLE,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(UInt32))(('GetServiceDisplayNameA', windll['ADVAPI32.dll']), ((1, 'hSCManager'),(1, 'lpServiceName'),(1, 'lpDisplayName'),(1, 'lpcchBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetServiceDisplayNameW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.SC_HANDLE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32))(('GetServiceDisplayNameW', windll['ADVAPI32.dll']), ((1, 'hSCManager'),(1, 'lpServiceName'),(1, 'lpDisplayName'),(1, 'lpcchBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LockServiceDatabase():
    try:
        return WINFUNCTYPE(c_void_p,win32more.Security.SC_HANDLE)(('LockServiceDatabase', windll['ADVAPI32.dll']), ((1, 'hSCManager'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NotifyBootConfigStatus():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.BOOL)(('NotifyBootConfigStatus', windll['ADVAPI32.dll']), ((1, 'BootAcceptable'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenSCManagerA():
    try:
        return WINFUNCTYPE(win32more.Security.SC_HANDLE,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32)(('OpenSCManagerA', windll['ADVAPI32.dll']), ((1, 'lpMachineName'),(1, 'lpDatabaseName'),(1, 'dwDesiredAccess'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenSCManagerW():
    try:
        return WINFUNCTYPE(win32more.Security.SC_HANDLE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32)(('OpenSCManagerW', windll['ADVAPI32.dll']), ((1, 'lpMachineName'),(1, 'lpDatabaseName'),(1, 'dwDesiredAccess'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenServiceA():
    try:
        return WINFUNCTYPE(win32more.Security.SC_HANDLE,win32more.Security.SC_HANDLE,win32more.Foundation.PSTR,UInt32)(('OpenServiceA', windll['ADVAPI32.dll']), ((1, 'hSCManager'),(1, 'lpServiceName'),(1, 'dwDesiredAccess'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenServiceW():
    try:
        return WINFUNCTYPE(win32more.Security.SC_HANDLE,win32more.Security.SC_HANDLE,win32more.Foundation.PWSTR,UInt32)(('OpenServiceW', windll['ADVAPI32.dll']), ((1, 'hSCManager'),(1, 'lpServiceName'),(1, 'dwDesiredAccess'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryServiceConfigA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.SC_HANDLE,POINTER(win32more.System.Services.QUERY_SERVICE_CONFIGA_head),UInt32,POINTER(UInt32))(('QueryServiceConfigA', windll['ADVAPI32.dll']), ((1, 'hService'),(1, 'lpServiceConfig'),(1, 'cbBufSize'),(1, 'pcbBytesNeeded'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryServiceConfigW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.SC_HANDLE,POINTER(win32more.System.Services.QUERY_SERVICE_CONFIGW_head),UInt32,POINTER(UInt32))(('QueryServiceConfigW', windll['ADVAPI32.dll']), ((1, 'hService'),(1, 'lpServiceConfig'),(1, 'cbBufSize'),(1, 'pcbBytesNeeded'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryServiceConfig2A():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.SC_HANDLE,win32more.System.Services.SERVICE_CONFIG,c_char_p_no,UInt32,POINTER(UInt32))(('QueryServiceConfig2A', windll['ADVAPI32.dll']), ((1, 'hService'),(1, 'dwInfoLevel'),(1, 'lpBuffer'),(1, 'cbBufSize'),(1, 'pcbBytesNeeded'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryServiceConfig2W():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.SC_HANDLE,win32more.System.Services.SERVICE_CONFIG,c_char_p_no,UInt32,POINTER(UInt32))(('QueryServiceConfig2W', windll['ADVAPI32.dll']), ((1, 'hService'),(1, 'dwInfoLevel'),(1, 'lpBuffer'),(1, 'cbBufSize'),(1, 'pcbBytesNeeded'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryServiceLockStatusA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.SC_HANDLE,POINTER(win32more.System.Services.QUERY_SERVICE_LOCK_STATUSA_head),UInt32,POINTER(UInt32))(('QueryServiceLockStatusA', windll['ADVAPI32.dll']), ((1, 'hSCManager'),(1, 'lpLockStatus'),(1, 'cbBufSize'),(1, 'pcbBytesNeeded'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryServiceLockStatusW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.SC_HANDLE,POINTER(win32more.System.Services.QUERY_SERVICE_LOCK_STATUSW_head),UInt32,POINTER(UInt32))(('QueryServiceLockStatusW', windll['ADVAPI32.dll']), ((1, 'hSCManager'),(1, 'lpLockStatus'),(1, 'cbBufSize'),(1, 'pcbBytesNeeded'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryServiceObjectSecurity():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.SC_HANDLE,UInt32,win32more.Security.PSECURITY_DESCRIPTOR,UInt32,POINTER(UInt32))(('QueryServiceObjectSecurity', windll['ADVAPI32.dll']), ((1, 'hService'),(1, 'dwSecurityInformation'),(1, 'lpSecurityDescriptor'),(1, 'cbBufSize'),(1, 'pcbBytesNeeded'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryServiceStatus():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.SC_HANDLE,POINTER(win32more.System.Services.SERVICE_STATUS_head))(('QueryServiceStatus', windll['ADVAPI32.dll']), ((1, 'hService'),(1, 'lpServiceStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryServiceStatusEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.SC_HANDLE,win32more.System.Services.SC_STATUS_TYPE,c_char_p_no,UInt32,POINTER(UInt32))(('QueryServiceStatusEx', windll['ADVAPI32.dll']), ((1, 'hService'),(1, 'InfoLevel'),(1, 'lpBuffer'),(1, 'cbBufSize'),(1, 'pcbBytesNeeded'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterServiceCtrlHandlerA():
    try:
        return WINFUNCTYPE(win32more.System.Services.SERVICE_STATUS_HANDLE,win32more.Foundation.PSTR,win32more.System.Services.LPHANDLER_FUNCTION)(('RegisterServiceCtrlHandlerA', windll['ADVAPI32.dll']), ((1, 'lpServiceName'),(1, 'lpHandlerProc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterServiceCtrlHandlerW():
    try:
        return WINFUNCTYPE(win32more.System.Services.SERVICE_STATUS_HANDLE,win32more.Foundation.PWSTR,win32more.System.Services.LPHANDLER_FUNCTION)(('RegisterServiceCtrlHandlerW', windll['ADVAPI32.dll']), ((1, 'lpServiceName'),(1, 'lpHandlerProc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterServiceCtrlHandlerExA():
    try:
        return WINFUNCTYPE(win32more.System.Services.SERVICE_STATUS_HANDLE,win32more.Foundation.PSTR,win32more.System.Services.LPHANDLER_FUNCTION_EX,c_void_p)(('RegisterServiceCtrlHandlerExA', windll['ADVAPI32.dll']), ((1, 'lpServiceName'),(1, 'lpHandlerProc'),(1, 'lpContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterServiceCtrlHandlerExW():
    try:
        return WINFUNCTYPE(win32more.System.Services.SERVICE_STATUS_HANDLE,win32more.Foundation.PWSTR,win32more.System.Services.LPHANDLER_FUNCTION_EX,c_void_p)(('RegisterServiceCtrlHandlerExW', windll['ADVAPI32.dll']), ((1, 'lpServiceName'),(1, 'lpHandlerProc'),(1, 'lpContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetServiceObjectSecurity():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.SC_HANDLE,win32more.Security.OBJECT_SECURITY_INFORMATION,win32more.Security.PSECURITY_DESCRIPTOR)(('SetServiceObjectSecurity', windll['ADVAPI32.dll']), ((1, 'hService'),(1, 'dwSecurityInformation'),(1, 'lpSecurityDescriptor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetServiceStatus():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.Services.SERVICE_STATUS_HANDLE,POINTER(win32more.System.Services.SERVICE_STATUS_head))(('SetServiceStatus', windll['ADVAPI32.dll']), ((1, 'hServiceStatus'),(1, 'lpServiceStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_StartServiceCtrlDispatcherA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Services.SERVICE_TABLE_ENTRYA_head))(('StartServiceCtrlDispatcherA', windll['ADVAPI32.dll']), ((1, 'lpServiceStartTable'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_StartServiceCtrlDispatcherW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Services.SERVICE_TABLE_ENTRYW_head))(('StartServiceCtrlDispatcherW', windll['ADVAPI32.dll']), ((1, 'lpServiceStartTable'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_StartServiceA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.SC_HANDLE,UInt32,POINTER(win32more.Foundation.PSTR))(('StartServiceA', windll['ADVAPI32.dll']), ((1, 'hService'),(1, 'dwNumServiceArgs'),(1, 'lpServiceArgVectors'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_StartServiceW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.SC_HANDLE,UInt32,POINTER(win32more.Foundation.PWSTR))(('StartServiceW', windll['ADVAPI32.dll']), ((1, 'hService'),(1, 'dwNumServiceArgs'),(1, 'lpServiceArgVectors'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UnlockServiceDatabase():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p)(('UnlockServiceDatabase', windll['ADVAPI32.dll']), ((1, 'ScLock'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NotifyServiceStatusChangeA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Security.SC_HANDLE,win32more.System.Services.SERVICE_NOTIFY,POINTER(win32more.System.Services.SERVICE_NOTIFY_2A_head))(('NotifyServiceStatusChangeA', windll['ADVAPI32.dll']), ((1, 'hService'),(1, 'dwNotifyMask'),(1, 'pNotifyBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NotifyServiceStatusChangeW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Security.SC_HANDLE,win32more.System.Services.SERVICE_NOTIFY,POINTER(win32more.System.Services.SERVICE_NOTIFY_2W_head))(('NotifyServiceStatusChangeW', windll['ADVAPI32.dll']), ((1, 'hService'),(1, 'dwNotifyMask'),(1, 'pNotifyBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ControlServiceExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.SC_HANDLE,UInt32,UInt32,c_void_p)(('ControlServiceExA', windll['ADVAPI32.dll']), ((1, 'hService'),(1, 'dwControl'),(1, 'dwInfoLevel'),(1, 'pControlParams'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ControlServiceExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.SC_HANDLE,UInt32,UInt32,c_void_p)(('ControlServiceExW', windll['ADVAPI32.dll']), ((1, 'hService'),(1, 'dwControl'),(1, 'dwInfoLevel'),(1, 'pControlParams'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryServiceDynamicInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.Services.SERVICE_STATUS_HANDLE,UInt32,POINTER(c_void_p))(('QueryServiceDynamicInformation', windll['ADVAPI32.dll']), ((1, 'hServiceStatus'),(1, 'dwInfoLevel'),(1, 'ppDynamicInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WaitServiceState():
    try:
        return WINFUNCTYPE(UInt32,win32more.Security.SC_HANDLE,UInt32,UInt32,win32more.Foundation.HANDLE)(('WaitServiceState', windll['ADVAPI32.dll']), ((1, 'hService'),(1, 'dwNotify'),(1, 'dwTimeout'),(1, 'hCancelEvent'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetServiceRegistryStateKey():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Services.SERVICE_STATUS_HANDLE,win32more.System.Services.SERVICE_REGISTRY_STATE_TYPE,UInt32,POINTER(win32more.System.Registry.HKEY))(('GetServiceRegistryStateKey', windll['api-ms-win-service-core-l1-1-3.dll']), ((1, 'ServiceStatusHandle'),(1, 'StateType'),(1, 'AccessMask'),(1, 'ServiceStateKey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetServiceDirectory():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Services.SERVICE_STATUS_HANDLE,win32more.System.Services.SERVICE_DIRECTORY_TYPE,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32))(('GetServiceDirectory', windll['api-ms-win-service-core-l1-1-4.dll']), ((1, 'hServiceStatus'),(1, 'eDirectoryType'),(1, 'lpPathBuffer'),(1, 'cchPathBufferLength'),(1, 'lpcchRequiredBufferLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSharedServiceRegistryStateKey():
    try:
        return WINFUNCTYPE(UInt32,win32more.Security.SC_HANDLE,win32more.System.Services.SERVICE_SHARED_REGISTRY_STATE_TYPE,UInt32,POINTER(win32more.System.Registry.HKEY))(('GetSharedServiceRegistryStateKey', windll['api-ms-win-service-core-l1-1-5.dll']), ((1, 'ServiceHandle'),(1, 'StateType'),(1, 'AccessMask'),(1, 'ServiceStateKey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSharedServiceDirectory():
    try:
        return WINFUNCTYPE(UInt32,win32more.Security.SC_HANDLE,win32more.System.Services.SERVICE_SHARED_DIRECTORY_TYPE,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32))(('GetSharedServiceDirectory', windll['api-ms-win-service-core-l1-1-5.dll']), ((1, 'ServiceHandle'),(1, 'DirectoryType'),(1, 'PathBuffer'),(1, 'PathBufferLength'),(1, 'RequiredBufferLength'),))
    except (FileNotFoundError, AttributeError):
        return None
ENUM_SERVICE_STATE = UInt32
SERVICE_ACTIVE = 1
SERVICE_INACTIVE = 2
SERVICE_STATE_ALL = 3
def _define_ENUM_SERVICE_STATUS_PROCESSA_head():
    class ENUM_SERVICE_STATUS_PROCESSA(Structure):
        pass
    return ENUM_SERVICE_STATUS_PROCESSA
def _define_ENUM_SERVICE_STATUS_PROCESSA():
    ENUM_SERVICE_STATUS_PROCESSA = win32more.System.Services.ENUM_SERVICE_STATUS_PROCESSA_head
    ENUM_SERVICE_STATUS_PROCESSA._fields_ = [
        ('lpServiceName', win32more.Foundation.PSTR),
        ('lpDisplayName', win32more.Foundation.PSTR),
        ('ServiceStatusProcess', win32more.System.Services.SERVICE_STATUS_PROCESS),
    ]
    return ENUM_SERVICE_STATUS_PROCESSA
def _define_ENUM_SERVICE_STATUS_PROCESSW_head():
    class ENUM_SERVICE_STATUS_PROCESSW(Structure):
        pass
    return ENUM_SERVICE_STATUS_PROCESSW
def _define_ENUM_SERVICE_STATUS_PROCESSW():
    ENUM_SERVICE_STATUS_PROCESSW = win32more.System.Services.ENUM_SERVICE_STATUS_PROCESSW_head
    ENUM_SERVICE_STATUS_PROCESSW._fields_ = [
        ('lpServiceName', win32more.Foundation.PWSTR),
        ('lpDisplayName', win32more.Foundation.PWSTR),
        ('ServiceStatusProcess', win32more.System.Services.SERVICE_STATUS_PROCESS),
    ]
    return ENUM_SERVICE_STATUS_PROCESSW
def _define_ENUM_SERVICE_STATUSA_head():
    class ENUM_SERVICE_STATUSA(Structure):
        pass
    return ENUM_SERVICE_STATUSA
def _define_ENUM_SERVICE_STATUSA():
    ENUM_SERVICE_STATUSA = win32more.System.Services.ENUM_SERVICE_STATUSA_head
    ENUM_SERVICE_STATUSA._fields_ = [
        ('lpServiceName', win32more.Foundation.PSTR),
        ('lpDisplayName', win32more.Foundation.PSTR),
        ('ServiceStatus', win32more.System.Services.SERVICE_STATUS),
    ]
    return ENUM_SERVICE_STATUSA
def _define_ENUM_SERVICE_STATUSW_head():
    class ENUM_SERVICE_STATUSW(Structure):
        pass
    return ENUM_SERVICE_STATUSW
def _define_ENUM_SERVICE_STATUSW():
    ENUM_SERVICE_STATUSW = win32more.System.Services.ENUM_SERVICE_STATUSW_head
    ENUM_SERVICE_STATUSW._fields_ = [
        ('lpServiceName', win32more.Foundation.PWSTR),
        ('lpDisplayName', win32more.Foundation.PWSTR),
        ('ServiceStatus', win32more.System.Services.SERVICE_STATUS),
    ]
    return ENUM_SERVICE_STATUSW
ENUM_SERVICE_TYPE = UInt32
SERVICE_DRIVER = 11
SERVICE_KERNEL_DRIVER = 1
SERVICE_WIN32 = 48
SERVICE_WIN32_SHARE_PROCESS = 32
SERVICE_ADAPTER = 4
SERVICE_FILE_SYSTEM_DRIVER = 2
SERVICE_RECOGNIZER_DRIVER = 8
SERVICE_WIN32_OWN_PROCESS = 16
SERVICE_USER_OWN_PROCESS = 80
SERVICE_USER_SHARE_PROCESS = 96
def _define_HANDLER_FUNCTION():
    return WINFUNCTYPE(Void,UInt32)
def _define_HANDLER_FUNCTION_EX():
    return WINFUNCTYPE(UInt32,UInt32,UInt32,c_void_p,c_void_p)
def _define_LPHANDLER_FUNCTION():
    return WINFUNCTYPE(Void,UInt32)
def _define_LPHANDLER_FUNCTION_EX():
    return WINFUNCTYPE(UInt32,UInt32,UInt32,c_void_p,c_void_p)
def _define_LPSERVICE_MAIN_FUNCTIONA():
    return WINFUNCTYPE(Void,UInt32,POINTER(win32more.Foundation.PSTR))
def _define_LPSERVICE_MAIN_FUNCTIONW():
    return WINFUNCTYPE(Void,UInt32,POINTER(win32more.Foundation.PWSTR))
def _define_PFN_SC_NOTIFY_CALLBACK():
    return WINFUNCTYPE(Void,c_void_p)
def _define_PSC_NOTIFICATION_CALLBACK():
    return WINFUNCTYPE(Void,UInt32,c_void_p)
def _define_QUERY_SERVICE_CONFIGA_head():
    class QUERY_SERVICE_CONFIGA(Structure):
        pass
    return QUERY_SERVICE_CONFIGA
def _define_QUERY_SERVICE_CONFIGA():
    QUERY_SERVICE_CONFIGA = win32more.System.Services.QUERY_SERVICE_CONFIGA_head
    QUERY_SERVICE_CONFIGA._fields_ = [
        ('dwServiceType', win32more.System.Services.ENUM_SERVICE_TYPE),
        ('dwStartType', win32more.System.Services.SERVICE_START_TYPE),
        ('dwErrorControl', win32more.System.Services.SERVICE_ERROR),
        ('lpBinaryPathName', win32more.Foundation.PSTR),
        ('lpLoadOrderGroup', win32more.Foundation.PSTR),
        ('dwTagId', UInt32),
        ('lpDependencies', win32more.Foundation.PSTR),
        ('lpServiceStartName', win32more.Foundation.PSTR),
        ('lpDisplayName', win32more.Foundation.PSTR),
    ]
    return QUERY_SERVICE_CONFIGA
def _define_QUERY_SERVICE_CONFIGW_head():
    class QUERY_SERVICE_CONFIGW(Structure):
        pass
    return QUERY_SERVICE_CONFIGW
def _define_QUERY_SERVICE_CONFIGW():
    QUERY_SERVICE_CONFIGW = win32more.System.Services.QUERY_SERVICE_CONFIGW_head
    QUERY_SERVICE_CONFIGW._fields_ = [
        ('dwServiceType', win32more.System.Services.ENUM_SERVICE_TYPE),
        ('dwStartType', win32more.System.Services.SERVICE_START_TYPE),
        ('dwErrorControl', win32more.System.Services.SERVICE_ERROR),
        ('lpBinaryPathName', win32more.Foundation.PWSTR),
        ('lpLoadOrderGroup', win32more.Foundation.PWSTR),
        ('dwTagId', UInt32),
        ('lpDependencies', win32more.Foundation.PWSTR),
        ('lpServiceStartName', win32more.Foundation.PWSTR),
        ('lpDisplayName', win32more.Foundation.PWSTR),
    ]
    return QUERY_SERVICE_CONFIGW
def _define_QUERY_SERVICE_LOCK_STATUSA_head():
    class QUERY_SERVICE_LOCK_STATUSA(Structure):
        pass
    return QUERY_SERVICE_LOCK_STATUSA
def _define_QUERY_SERVICE_LOCK_STATUSA():
    QUERY_SERVICE_LOCK_STATUSA = win32more.System.Services.QUERY_SERVICE_LOCK_STATUSA_head
    QUERY_SERVICE_LOCK_STATUSA._fields_ = [
        ('fIsLocked', UInt32),
        ('lpLockOwner', win32more.Foundation.PSTR),
        ('dwLockDuration', UInt32),
    ]
    return QUERY_SERVICE_LOCK_STATUSA
def _define_QUERY_SERVICE_LOCK_STATUSW_head():
    class QUERY_SERVICE_LOCK_STATUSW(Structure):
        pass
    return QUERY_SERVICE_LOCK_STATUSW
def _define_QUERY_SERVICE_LOCK_STATUSW():
    QUERY_SERVICE_LOCK_STATUSW = win32more.System.Services.QUERY_SERVICE_LOCK_STATUSW_head
    QUERY_SERVICE_LOCK_STATUSW._fields_ = [
        ('fIsLocked', UInt32),
        ('lpLockOwner', win32more.Foundation.PWSTR),
        ('dwLockDuration', UInt32),
    ]
    return QUERY_SERVICE_LOCK_STATUSW
def _define_SC_ACTION_head():
    class SC_ACTION(Structure):
        pass
    return SC_ACTION
def _define_SC_ACTION():
    SC_ACTION = win32more.System.Services.SC_ACTION_head
    SC_ACTION._fields_ = [
        ('Type', win32more.System.Services.SC_ACTION_TYPE),
        ('Delay', UInt32),
    ]
    return SC_ACTION
SC_ACTION_TYPE = Int32
SC_ACTION_NONE = 0
SC_ACTION_RESTART = 1
SC_ACTION_REBOOT = 2
SC_ACTION_RUN_COMMAND = 3
SC_ACTION_OWN_RESTART = 4
SC_ENUM_TYPE = Int32
SC_ENUM_PROCESS_INFO = 0
SC_EVENT_TYPE = Int32
SC_EVENT_DATABASE_CHANGE = 0
SC_EVENT_PROPERTY_CHANGE = 1
SC_EVENT_STATUS_CHANGE = 2
SC_STATUS_TYPE = Int32
SC_STATUS_PROCESS_INFO = 0
SERVICE_CONFIG = UInt32
SERVICE_CONFIG_DELAYED_AUTO_START_INFO = 3
SERVICE_CONFIG_DESCRIPTION = 1
SERVICE_CONFIG_FAILURE_ACTIONS = 2
SERVICE_CONFIG_FAILURE_ACTIONS_FLAG = 4
SERVICE_CONFIG_PREFERRED_NODE = 9
SERVICE_CONFIG_PRESHUTDOWN_INFO = 7
SERVICE_CONFIG_REQUIRED_PRIVILEGES_INFO = 6
SERVICE_CONFIG_SERVICE_SID_INFO = 5
SERVICE_CONFIG_TRIGGER_INFO = 8
SERVICE_CONFIG_LAUNCH_PROTECTED = 12
def _define_SERVICE_CONTROL_STATUS_REASON_PARAMSA_head():
    class SERVICE_CONTROL_STATUS_REASON_PARAMSA(Structure):
        pass
    return SERVICE_CONTROL_STATUS_REASON_PARAMSA
def _define_SERVICE_CONTROL_STATUS_REASON_PARAMSA():
    SERVICE_CONTROL_STATUS_REASON_PARAMSA = win32more.System.Services.SERVICE_CONTROL_STATUS_REASON_PARAMSA_head
    SERVICE_CONTROL_STATUS_REASON_PARAMSA._fields_ = [
        ('dwReason', UInt32),
        ('pszComment', win32more.Foundation.PSTR),
        ('ServiceStatus', win32more.System.Services.SERVICE_STATUS_PROCESS),
    ]
    return SERVICE_CONTROL_STATUS_REASON_PARAMSA
def _define_SERVICE_CONTROL_STATUS_REASON_PARAMSW_head():
    class SERVICE_CONTROL_STATUS_REASON_PARAMSW(Structure):
        pass
    return SERVICE_CONTROL_STATUS_REASON_PARAMSW
def _define_SERVICE_CONTROL_STATUS_REASON_PARAMSW():
    SERVICE_CONTROL_STATUS_REASON_PARAMSW = win32more.System.Services.SERVICE_CONTROL_STATUS_REASON_PARAMSW_head
    SERVICE_CONTROL_STATUS_REASON_PARAMSW._fields_ = [
        ('dwReason', UInt32),
        ('pszComment', win32more.Foundation.PWSTR),
        ('ServiceStatus', win32more.System.Services.SERVICE_STATUS_PROCESS),
    ]
    return SERVICE_CONTROL_STATUS_REASON_PARAMSW
def _define_SERVICE_CUSTOM_SYSTEM_STATE_CHANGE_DATA_ITEM_head():
    class SERVICE_CUSTOM_SYSTEM_STATE_CHANGE_DATA_ITEM(Structure):
        pass
    return SERVICE_CUSTOM_SYSTEM_STATE_CHANGE_DATA_ITEM
def _define_SERVICE_CUSTOM_SYSTEM_STATE_CHANGE_DATA_ITEM():
    SERVICE_CUSTOM_SYSTEM_STATE_CHANGE_DATA_ITEM = win32more.System.Services.SERVICE_CUSTOM_SYSTEM_STATE_CHANGE_DATA_ITEM_head
    class SERVICE_CUSTOM_SYSTEM_STATE_CHANGE_DATA_ITEM__u_e__Union(Union):
        pass
    class SERVICE_CUSTOM_SYSTEM_STATE_CHANGE_DATA_ITEM__u_e__Union__s_e__Struct(Structure):
        pass
    SERVICE_CUSTOM_SYSTEM_STATE_CHANGE_DATA_ITEM__u_e__Union__s_e__Struct._fields_ = [
        ('DataOffset', UInt32),
        ('Data', Byte * 1),
    ]
    SERVICE_CUSTOM_SYSTEM_STATE_CHANGE_DATA_ITEM__u_e__Union._fields_ = [
        ('CustomStateId', win32more.System.Services.SERVICE_TRIGGER_CUSTOM_STATE_ID),
        ('s', SERVICE_CUSTOM_SYSTEM_STATE_CHANGE_DATA_ITEM__u_e__Union__s_e__Struct),
    ]
    SERVICE_CUSTOM_SYSTEM_STATE_CHANGE_DATA_ITEM._fields_ = [
        ('u', SERVICE_CUSTOM_SYSTEM_STATE_CHANGE_DATA_ITEM__u_e__Union),
    ]
    return SERVICE_CUSTOM_SYSTEM_STATE_CHANGE_DATA_ITEM
def _define_SERVICE_DELAYED_AUTO_START_INFO_head():
    class SERVICE_DELAYED_AUTO_START_INFO(Structure):
        pass
    return SERVICE_DELAYED_AUTO_START_INFO
def _define_SERVICE_DELAYED_AUTO_START_INFO():
    SERVICE_DELAYED_AUTO_START_INFO = win32more.System.Services.SERVICE_DELAYED_AUTO_START_INFO_head
    SERVICE_DELAYED_AUTO_START_INFO._fields_ = [
        ('fDelayedAutostart', win32more.Foundation.BOOL),
    ]
    return SERVICE_DELAYED_AUTO_START_INFO
def _define_SERVICE_DESCRIPTIONA_head():
    class SERVICE_DESCRIPTIONA(Structure):
        pass
    return SERVICE_DESCRIPTIONA
def _define_SERVICE_DESCRIPTIONA():
    SERVICE_DESCRIPTIONA = win32more.System.Services.SERVICE_DESCRIPTIONA_head
    SERVICE_DESCRIPTIONA._fields_ = [
        ('lpDescription', win32more.Foundation.PSTR),
    ]
    return SERVICE_DESCRIPTIONA
def _define_SERVICE_DESCRIPTIONW_head():
    class SERVICE_DESCRIPTIONW(Structure):
        pass
    return SERVICE_DESCRIPTIONW
def _define_SERVICE_DESCRIPTIONW():
    SERVICE_DESCRIPTIONW = win32more.System.Services.SERVICE_DESCRIPTIONW_head
    SERVICE_DESCRIPTIONW._fields_ = [
        ('lpDescription', win32more.Foundation.PWSTR),
    ]
    return SERVICE_DESCRIPTIONW
SERVICE_DIRECTORY_TYPE = Int32
SERVICE_DIRECTORY_TYPE_ServiceDirectoryPersistentState = 0
SERVICE_DIRECTORY_TYPE_ServiceDirectoryTypeMax = 1
SERVICE_ERROR = UInt32
SERVICE_ERROR_CRITICAL = 3
SERVICE_ERROR_IGNORE = 0
SERVICE_ERROR_NORMAL = 1
SERVICE_ERROR_SEVERE = 2
def _define_SERVICE_FAILURE_ACTIONS_FLAG_head():
    class SERVICE_FAILURE_ACTIONS_FLAG(Structure):
        pass
    return SERVICE_FAILURE_ACTIONS_FLAG
def _define_SERVICE_FAILURE_ACTIONS_FLAG():
    SERVICE_FAILURE_ACTIONS_FLAG = win32more.System.Services.SERVICE_FAILURE_ACTIONS_FLAG_head
    SERVICE_FAILURE_ACTIONS_FLAG._fields_ = [
        ('fFailureActionsOnNonCrashFailures', win32more.Foundation.BOOL),
    ]
    return SERVICE_FAILURE_ACTIONS_FLAG
def _define_SERVICE_FAILURE_ACTIONSA_head():
    class SERVICE_FAILURE_ACTIONSA(Structure):
        pass
    return SERVICE_FAILURE_ACTIONSA
def _define_SERVICE_FAILURE_ACTIONSA():
    SERVICE_FAILURE_ACTIONSA = win32more.System.Services.SERVICE_FAILURE_ACTIONSA_head
    SERVICE_FAILURE_ACTIONSA._fields_ = [
        ('dwResetPeriod', UInt32),
        ('lpRebootMsg', win32more.Foundation.PSTR),
        ('lpCommand', win32more.Foundation.PSTR),
        ('cActions', UInt32),
        ('lpsaActions', POINTER(win32more.System.Services.SC_ACTION_head)),
    ]
    return SERVICE_FAILURE_ACTIONSA
def _define_SERVICE_FAILURE_ACTIONSW_head():
    class SERVICE_FAILURE_ACTIONSW(Structure):
        pass
    return SERVICE_FAILURE_ACTIONSW
def _define_SERVICE_FAILURE_ACTIONSW():
    SERVICE_FAILURE_ACTIONSW = win32more.System.Services.SERVICE_FAILURE_ACTIONSW_head
    SERVICE_FAILURE_ACTIONSW._fields_ = [
        ('dwResetPeriod', UInt32),
        ('lpRebootMsg', win32more.Foundation.PWSTR),
        ('lpCommand', win32more.Foundation.PWSTR),
        ('cActions', UInt32),
        ('lpsaActions', POINTER(win32more.System.Services.SC_ACTION_head)),
    ]
    return SERVICE_FAILURE_ACTIONSW
def _define_SERVICE_LAUNCH_PROTECTED_INFO_head():
    class SERVICE_LAUNCH_PROTECTED_INFO(Structure):
        pass
    return SERVICE_LAUNCH_PROTECTED_INFO
def _define_SERVICE_LAUNCH_PROTECTED_INFO():
    SERVICE_LAUNCH_PROTECTED_INFO = win32more.System.Services.SERVICE_LAUNCH_PROTECTED_INFO_head
    SERVICE_LAUNCH_PROTECTED_INFO._fields_ = [
        ('dwLaunchProtected', UInt32),
    ]
    return SERVICE_LAUNCH_PROTECTED_INFO
def _define_SERVICE_MAIN_FUNCTIONA():
    return WINFUNCTYPE(Void,UInt32,POINTER(POINTER(SByte)))
def _define_SERVICE_MAIN_FUNCTIONW():
    return WINFUNCTYPE(Void,UInt32,POINTER(win32more.Foundation.PWSTR))
SERVICE_NOTIFY = UInt32
SERVICE_NOTIFY_CREATED = 128
SERVICE_NOTIFY_CONTINUE_PENDING = 16
SERVICE_NOTIFY_DELETE_PENDING = 512
SERVICE_NOTIFY_DELETED = 256
SERVICE_NOTIFY_PAUSE_PENDING = 32
SERVICE_NOTIFY_PAUSED = 64
SERVICE_NOTIFY_RUNNING = 8
SERVICE_NOTIFY_START_PENDING = 2
SERVICE_NOTIFY_STOP_PENDING = 4
SERVICE_NOTIFY_STOPPED = 1
def _define_SERVICE_NOTIFY_1_head():
    class SERVICE_NOTIFY_1(Structure):
        pass
    return SERVICE_NOTIFY_1
def _define_SERVICE_NOTIFY_1():
    SERVICE_NOTIFY_1 = win32more.System.Services.SERVICE_NOTIFY_1_head
    SERVICE_NOTIFY_1._fields_ = [
        ('dwVersion', UInt32),
        ('pfnNotifyCallback', win32more.System.Services.PFN_SC_NOTIFY_CALLBACK),
        ('pContext', c_void_p),
        ('dwNotificationStatus', UInt32),
        ('ServiceStatus', win32more.System.Services.SERVICE_STATUS_PROCESS),
    ]
    return SERVICE_NOTIFY_1
def _define_SERVICE_NOTIFY_2A_head():
    class SERVICE_NOTIFY_2A(Structure):
        pass
    return SERVICE_NOTIFY_2A
def _define_SERVICE_NOTIFY_2A():
    SERVICE_NOTIFY_2A = win32more.System.Services.SERVICE_NOTIFY_2A_head
    SERVICE_NOTIFY_2A._fields_ = [
        ('dwVersion', UInt32),
        ('pfnNotifyCallback', win32more.System.Services.PFN_SC_NOTIFY_CALLBACK),
        ('pContext', c_void_p),
        ('dwNotificationStatus', UInt32),
        ('ServiceStatus', win32more.System.Services.SERVICE_STATUS_PROCESS),
        ('dwNotificationTriggered', UInt32),
        ('pszServiceNames', win32more.Foundation.PSTR),
    ]
    return SERVICE_NOTIFY_2A
def _define_SERVICE_NOTIFY_2W_head():
    class SERVICE_NOTIFY_2W(Structure):
        pass
    return SERVICE_NOTIFY_2W
def _define_SERVICE_NOTIFY_2W():
    SERVICE_NOTIFY_2W = win32more.System.Services.SERVICE_NOTIFY_2W_head
    SERVICE_NOTIFY_2W._fields_ = [
        ('dwVersion', UInt32),
        ('pfnNotifyCallback', win32more.System.Services.PFN_SC_NOTIFY_CALLBACK),
        ('pContext', c_void_p),
        ('dwNotificationStatus', UInt32),
        ('ServiceStatus', win32more.System.Services.SERVICE_STATUS_PROCESS),
        ('dwNotificationTriggered', UInt32),
        ('pszServiceNames', win32more.Foundation.PWSTR),
    ]
    return SERVICE_NOTIFY_2W
def _define_SERVICE_PREFERRED_NODE_INFO_head():
    class SERVICE_PREFERRED_NODE_INFO(Structure):
        pass
    return SERVICE_PREFERRED_NODE_INFO
def _define_SERVICE_PREFERRED_NODE_INFO():
    SERVICE_PREFERRED_NODE_INFO = win32more.System.Services.SERVICE_PREFERRED_NODE_INFO_head
    SERVICE_PREFERRED_NODE_INFO._fields_ = [
        ('usPreferredNode', UInt16),
        ('fDelete', win32more.Foundation.BOOLEAN),
    ]
    return SERVICE_PREFERRED_NODE_INFO
def _define_SERVICE_PRESHUTDOWN_INFO_head():
    class SERVICE_PRESHUTDOWN_INFO(Structure):
        pass
    return SERVICE_PRESHUTDOWN_INFO
def _define_SERVICE_PRESHUTDOWN_INFO():
    SERVICE_PRESHUTDOWN_INFO = win32more.System.Services.SERVICE_PRESHUTDOWN_INFO_head
    SERVICE_PRESHUTDOWN_INFO._fields_ = [
        ('dwPreshutdownTimeout', UInt32),
    ]
    return SERVICE_PRESHUTDOWN_INFO
SERVICE_REGISTRY_STATE_TYPE = Int32
SERVICE_REGISTRY_STATE_TYPE_ServiceRegistryStateParameters = 0
SERVICE_REGISTRY_STATE_TYPE_ServiceRegistryStatePersistent = 1
SERVICE_REGISTRY_STATE_TYPE_MaxServiceRegistryStateType = 2
def _define_SERVICE_REQUIRED_PRIVILEGES_INFOA_head():
    class SERVICE_REQUIRED_PRIVILEGES_INFOA(Structure):
        pass
    return SERVICE_REQUIRED_PRIVILEGES_INFOA
def _define_SERVICE_REQUIRED_PRIVILEGES_INFOA():
    SERVICE_REQUIRED_PRIVILEGES_INFOA = win32more.System.Services.SERVICE_REQUIRED_PRIVILEGES_INFOA_head
    SERVICE_REQUIRED_PRIVILEGES_INFOA._fields_ = [
        ('pmszRequiredPrivileges', win32more.Foundation.PSTR),
    ]
    return SERVICE_REQUIRED_PRIVILEGES_INFOA
def _define_SERVICE_REQUIRED_PRIVILEGES_INFOW_head():
    class SERVICE_REQUIRED_PRIVILEGES_INFOW(Structure):
        pass
    return SERVICE_REQUIRED_PRIVILEGES_INFOW
def _define_SERVICE_REQUIRED_PRIVILEGES_INFOW():
    SERVICE_REQUIRED_PRIVILEGES_INFOW = win32more.System.Services.SERVICE_REQUIRED_PRIVILEGES_INFOW_head
    SERVICE_REQUIRED_PRIVILEGES_INFOW._fields_ = [
        ('pmszRequiredPrivileges', win32more.Foundation.PWSTR),
    ]
    return SERVICE_REQUIRED_PRIVILEGES_INFOW
SERVICE_RUNS_IN_PROCESS = UInt32
SERVICE_RUNS_IN_NON_SYSTEM_OR_NOT_RUNNING = 0
SERVICE_RUNS_IN_SYSTEM_PROCESS = 1
SERVICE_SHARED_DIRECTORY_TYPE = Int32
SERVICE_SHARED_DIRECTORY_TYPE_ServiceSharedDirectoryPersistentState = 0
SERVICE_SHARED_REGISTRY_STATE_TYPE = Int32
SERVICE_SHARED_REGISTRY_STATE_TYPE_ServiceSharedRegistryPersistentState = 0
def _define_SERVICE_SID_INFO_head():
    class SERVICE_SID_INFO(Structure):
        pass
    return SERVICE_SID_INFO
def _define_SERVICE_SID_INFO():
    SERVICE_SID_INFO = win32more.System.Services.SERVICE_SID_INFO_head
    SERVICE_SID_INFO._fields_ = [
        ('dwServiceSidType', UInt32),
    ]
    return SERVICE_SID_INFO
def _define_SERVICE_START_REASON_head():
    class SERVICE_START_REASON(Structure):
        pass
    return SERVICE_START_REASON
def _define_SERVICE_START_REASON():
    SERVICE_START_REASON = win32more.System.Services.SERVICE_START_REASON_head
    SERVICE_START_REASON._fields_ = [
        ('dwReason', UInt32),
    ]
    return SERVICE_START_REASON
SERVICE_START_TYPE = UInt32
SERVICE_AUTO_START = 2
SERVICE_BOOT_START = 0
SERVICE_DEMAND_START = 3
SERVICE_DISABLED = 4
SERVICE_SYSTEM_START = 1
def _define_SERVICE_STATUS_head():
    class SERVICE_STATUS(Structure):
        pass
    return SERVICE_STATUS
def _define_SERVICE_STATUS():
    SERVICE_STATUS = win32more.System.Services.SERVICE_STATUS_head
    SERVICE_STATUS._fields_ = [
        ('dwServiceType', win32more.System.Services.ENUM_SERVICE_TYPE),
        ('dwCurrentState', win32more.System.Services.SERVICE_STATUS_CURRENT_STATE),
        ('dwControlsAccepted', UInt32),
        ('dwWin32ExitCode', UInt32),
        ('dwServiceSpecificExitCode', UInt32),
        ('dwCheckPoint', UInt32),
        ('dwWaitHint', UInt32),
    ]
    return SERVICE_STATUS
SERVICE_STATUS_CURRENT_STATE = UInt32
SERVICE_CONTINUE_PENDING = 5
SERVICE_PAUSE_PENDING = 6
SERVICE_PAUSED = 7
SERVICE_RUNNING = 4
SERVICE_START_PENDING = 2
SERVICE_STOP_PENDING = 3
SERVICE_STOPPED = 1
SERVICE_STATUS_HANDLE = IntPtr
def _define_SERVICE_STATUS_PROCESS_head():
    class SERVICE_STATUS_PROCESS(Structure):
        pass
    return SERVICE_STATUS_PROCESS
def _define_SERVICE_STATUS_PROCESS():
    SERVICE_STATUS_PROCESS = win32more.System.Services.SERVICE_STATUS_PROCESS_head
    SERVICE_STATUS_PROCESS._fields_ = [
        ('dwServiceType', win32more.System.Services.ENUM_SERVICE_TYPE),
        ('dwCurrentState', win32more.System.Services.SERVICE_STATUS_CURRENT_STATE),
        ('dwControlsAccepted', UInt32),
        ('dwWin32ExitCode', UInt32),
        ('dwServiceSpecificExitCode', UInt32),
        ('dwCheckPoint', UInt32),
        ('dwWaitHint', UInt32),
        ('dwProcessId', UInt32),
        ('dwServiceFlags', win32more.System.Services.SERVICE_RUNS_IN_PROCESS),
    ]
    return SERVICE_STATUS_PROCESS
def _define_SERVICE_TABLE_ENTRYA_head():
    class SERVICE_TABLE_ENTRYA(Structure):
        pass
    return SERVICE_TABLE_ENTRYA
def _define_SERVICE_TABLE_ENTRYA():
    SERVICE_TABLE_ENTRYA = win32more.System.Services.SERVICE_TABLE_ENTRYA_head
    SERVICE_TABLE_ENTRYA._fields_ = [
        ('lpServiceName', win32more.Foundation.PSTR),
        ('lpServiceProc', win32more.System.Services.LPSERVICE_MAIN_FUNCTIONA),
    ]
    return SERVICE_TABLE_ENTRYA
def _define_SERVICE_TABLE_ENTRYW_head():
    class SERVICE_TABLE_ENTRYW(Structure):
        pass
    return SERVICE_TABLE_ENTRYW
def _define_SERVICE_TABLE_ENTRYW():
    SERVICE_TABLE_ENTRYW = win32more.System.Services.SERVICE_TABLE_ENTRYW_head
    SERVICE_TABLE_ENTRYW._fields_ = [
        ('lpServiceName', win32more.Foundation.PWSTR),
        ('lpServiceProc', win32more.System.Services.LPSERVICE_MAIN_FUNCTIONW),
    ]
    return SERVICE_TABLE_ENTRYW
def _define_SERVICE_TIMECHANGE_INFO_head():
    class SERVICE_TIMECHANGE_INFO(Structure):
        pass
    return SERVICE_TIMECHANGE_INFO
def _define_SERVICE_TIMECHANGE_INFO():
    SERVICE_TIMECHANGE_INFO = win32more.System.Services.SERVICE_TIMECHANGE_INFO_head
    SERVICE_TIMECHANGE_INFO._fields_ = [
        ('liNewTime', win32more.Foundation.LARGE_INTEGER),
        ('liOldTime', win32more.Foundation.LARGE_INTEGER),
    ]
    return SERVICE_TIMECHANGE_INFO
def _define_SERVICE_TRIGGER_head():
    class SERVICE_TRIGGER(Structure):
        pass
    return SERVICE_TRIGGER
def _define_SERVICE_TRIGGER():
    SERVICE_TRIGGER = win32more.System.Services.SERVICE_TRIGGER_head
    SERVICE_TRIGGER._fields_ = [
        ('dwTriggerType', win32more.System.Services.SERVICE_TRIGGER_TYPE),
        ('dwAction', win32more.System.Services.SERVICE_TRIGGER_ACTION),
        ('pTriggerSubtype', POINTER(Guid)),
        ('cDataItems', UInt32),
        ('pDataItems', POINTER(win32more.System.Services.SERVICE_TRIGGER_SPECIFIC_DATA_ITEM_head)),
    ]
    return SERVICE_TRIGGER
SERVICE_TRIGGER_ACTION = UInt32
SERVICE_TRIGGER_ACTION_SERVICE_START = 1
SERVICE_TRIGGER_ACTION_SERVICE_STOP = 2
def _define_SERVICE_TRIGGER_CUSTOM_STATE_ID_head():
    class SERVICE_TRIGGER_CUSTOM_STATE_ID(Structure):
        pass
    return SERVICE_TRIGGER_CUSTOM_STATE_ID
def _define_SERVICE_TRIGGER_CUSTOM_STATE_ID():
    SERVICE_TRIGGER_CUSTOM_STATE_ID = win32more.System.Services.SERVICE_TRIGGER_CUSTOM_STATE_ID_head
    SERVICE_TRIGGER_CUSTOM_STATE_ID._fields_ = [
        ('Data', UInt32 * 2),
    ]
    return SERVICE_TRIGGER_CUSTOM_STATE_ID
def _define_SERVICE_TRIGGER_INFO_head():
    class SERVICE_TRIGGER_INFO(Structure):
        pass
    return SERVICE_TRIGGER_INFO
def _define_SERVICE_TRIGGER_INFO():
    SERVICE_TRIGGER_INFO = win32more.System.Services.SERVICE_TRIGGER_INFO_head
    SERVICE_TRIGGER_INFO._fields_ = [
        ('cTriggers', UInt32),
        ('pTriggers', POINTER(win32more.System.Services.SERVICE_TRIGGER_head)),
        ('pReserved', c_char_p_no),
    ]
    return SERVICE_TRIGGER_INFO
def _define_SERVICE_TRIGGER_SPECIFIC_DATA_ITEM_head():
    class SERVICE_TRIGGER_SPECIFIC_DATA_ITEM(Structure):
        pass
    return SERVICE_TRIGGER_SPECIFIC_DATA_ITEM
def _define_SERVICE_TRIGGER_SPECIFIC_DATA_ITEM():
    SERVICE_TRIGGER_SPECIFIC_DATA_ITEM = win32more.System.Services.SERVICE_TRIGGER_SPECIFIC_DATA_ITEM_head
    SERVICE_TRIGGER_SPECIFIC_DATA_ITEM._fields_ = [
        ('dwDataType', win32more.System.Services.SERVICE_TRIGGER_SPECIFIC_DATA_ITEM_DATA_TYPE),
        ('cbData', UInt32),
        ('pData', c_char_p_no),
    ]
    return SERVICE_TRIGGER_SPECIFIC_DATA_ITEM
SERVICE_TRIGGER_SPECIFIC_DATA_ITEM_DATA_TYPE = UInt32
SERVICE_TRIGGER_DATA_TYPE_BINARY = 1
SERVICE_TRIGGER_DATA_TYPE_STRING = 2
SERVICE_TRIGGER_DATA_TYPE_LEVEL = 3
SERVICE_TRIGGER_DATA_TYPE_KEYWORD_ANY = 4
SERVICE_TRIGGER_DATA_TYPE_KEYWORD_ALL = 5
SERVICE_TRIGGER_TYPE = UInt32
SERVICE_TRIGGER_TYPE_CUSTOM = 20
SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL = 1
SERVICE_TRIGGER_TYPE_DOMAIN_JOIN = 3
SERVICE_TRIGGER_TYPE_FIREWALL_PORT_EVENT = 4
SERVICE_TRIGGER_TYPE_GROUP_POLICY = 5
SERVICE_TRIGGER_TYPE_IP_ADDRESS_AVAILABILITY = 2
SERVICE_TRIGGER_TYPE_NETWORK_ENDPOINT = 6
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
