from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Security
import win32more.Security.Isolation
import win32more.System.Com
import win32more.System.Registry
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
def _define_GetAppContainerNamedObjectPath():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PSID,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32))(('GetAppContainerNamedObjectPath', windll['KERNEL32.dll']), ((1, 'Token'),(1, 'AppContainerSid'),(1, 'ObjectPathLength'),(1, 'ObjectPath'),(1, 'ReturnLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsProcessInWDAGContainer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Foundation.BOOL))(('IsProcessInWDAGContainer', windll['api-ms-win-security-isolatedcontainer-l1-1-1.dll']), ((1, 'Reserved'),(1, 'isProcessInWDAGContainer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsProcessInIsolatedContainer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(('IsProcessInIsolatedContainer', windll['api-ms-win-security-isolatedcontainer-l1-1-0.dll']), ((1, 'isProcessInIsolatedContainer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsProcessInIsolatedWindowsEnvironment():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(('IsProcessInIsolatedWindowsEnvironment', windll['IsolatedWindowsEnvironmentUtils.dll']), ((1, 'isProcessInIsolatedWindowsEnvironment'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateAppContainerProfile():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Security.SID_AND_ATTRIBUTES_head),UInt32,POINTER(win32more.Foundation.PSID))(('CreateAppContainerProfile', windll['USERENV.dll']), ((1, 'pszAppContainerName'),(1, 'pszDisplayName'),(1, 'pszDescription'),(1, 'pCapabilities'),(1, 'dwCapabilityCount'),(1, 'ppSidAppContainerSid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeleteAppContainerProfile():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(('DeleteAppContainerProfile', windll['USERENV.dll']), ((1, 'pszAppContainerName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetAppContainerRegistryLocation():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Registry.HKEY))(('GetAppContainerRegistryLocation', windll['USERENV.dll']), ((1, 'desiredAccess'),(1, 'phAppContainerKey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetAppContainerFolderPath():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR))(('GetAppContainerFolderPath', windll['USERENV.dll']), ((1, 'pszAppContainerSid'),(1, 'ppszPath'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeriveRestrictedAppContainerSidFromAppContainerSidAndRestrictedName():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSID,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PSID))(('DeriveRestrictedAppContainerSidFromAppContainerSidAndRestrictedName', windll['USERENV.dll']), ((1, 'psidAppContainerSid'),(1, 'pszRestrictedAppContainerName'),(1, 'ppsidRestrictedAppContainerSid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeriveAppContainerSidFromAppContainerName():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PSID))(('DeriveAppContainerSidFromAppContainerName', windll['USERENV.dll']), ((1, 'pszAppContainerName'),(1, 'ppsidAppContainerSid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IIsolatedAppLauncher_head():
    class IIsolatedAppLauncher(win32more.System.Com.IUnknown_head):
        Guid = Guid('f686878f-7b42-4cc4-96-fb-f4-f3-b6-e3-d2-4d')
    return IIsolatedAppLauncher
def _define_IIsolatedAppLauncher():
    IIsolatedAppLauncher = win32more.Security.Isolation.IIsolatedAppLauncher_head
    IIsolatedAppLauncher.Launch = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Security.Isolation.IsolatedAppLauncherTelemetryParameters_head))(3, 'Launch', ((1, 'appUserModelId'),(1, 'arguments'),(1, 'telemetryParameters'),)))
    win32more.System.Com.IUnknown
    return IIsolatedAppLauncher
IsolatedAppLauncher = Guid('bc812430-e75e-4fd1-96-41-1f-9f-1e-2d-9a-1f')
def _define_IsolatedAppLauncherTelemetryParameters_head():
    class IsolatedAppLauncherTelemetryParameters(Structure):
        pass
    return IsolatedAppLauncherTelemetryParameters
def _define_IsolatedAppLauncherTelemetryParameters():
    IsolatedAppLauncherTelemetryParameters = win32more.Security.Isolation.IsolatedAppLauncherTelemetryParameters_head
    IsolatedAppLauncherTelemetryParameters._fields_ = [
        ('EnableForLaunch', win32more.Foundation.BOOL),
        ('CorrelationGUID', Guid),
    ]
    return IsolatedAppLauncherTelemetryParameters
__all__ = [
    "CreateAppContainerProfile",
    "DeleteAppContainerProfile",
    "DeriveAppContainerSidFromAppContainerName",
    "DeriveRestrictedAppContainerSidFromAppContainerSidAndRestrictedName",
    "GetAppContainerFolderPath",
    "GetAppContainerNamedObjectPath",
    "GetAppContainerRegistryLocation",
    "IIsolatedAppLauncher",
    "IsProcessInIsolatedContainer",
    "IsProcessInIsolatedWindowsEnvironment",
    "IsProcessInWDAGContainer",
    "IsolatedAppLauncher",
    "IsolatedAppLauncherTelemetryParameters",
]
