from win32more import *
import win32more.Foundation
import win32more.Security
import win32more.Security.Isolation
import win32more.System.Com
import win32more.System.Registry

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
IsolatedAppLauncher = Guid('bc812430-e75e-4fd1-9641-1f9f1e2d9a1f')
def _define_IsolatedAppLauncherTelemetryParameters_head():
    class IsolatedAppLauncherTelemetryParameters(Structure):
        pass
    return IsolatedAppLauncherTelemetryParameters
def _define_IsolatedAppLauncherTelemetryParameters():
    IsolatedAppLauncherTelemetryParameters = win32more.Security.Isolation.IsolatedAppLauncherTelemetryParameters_head
    IsolatedAppLauncherTelemetryParameters._fields_ = [
        ("EnableForLaunch", win32more.Foundation.BOOL),
        ("CorrelationGUID", Guid),
    ]
    return IsolatedAppLauncherTelemetryParameters
def _define_IIsolatedAppLauncher_head():
    class IIsolatedAppLauncher(win32more.System.Com.IUnknown_head):
        Guid = Guid('f686878f-7b42-4cc4-96fb-f4f3b6e3d24d')
    return IIsolatedAppLauncher
def _define_IIsolatedAppLauncher():
    IIsolatedAppLauncher = win32more.Security.Isolation.IIsolatedAppLauncher_head
    IIsolatedAppLauncher.Launch = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Security.Isolation.IsolatedAppLauncherTelemetryParameters_head), use_last_error=False)(3, 'Launch', ((1, 'appUserModelId'),(1, 'arguments'),(1, 'telemetryParameters'),)))
    win32more.System.Com.IUnknown
    return IIsolatedAppLauncher
def _define_GetAppContainerNamedObjectPath():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PSID,UInt32,POINTER(Char),POINTER(UInt32), use_last_error=True)(("GetAppContainerNamedObjectPath", windll["KERNEL32"]), ((1, 'Token'),(1, 'AppContainerSid'),(1, 'ObjectPathLength'),(1, 'ObjectPath'),(1, 'ReturnLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsProcessInWDAGContainer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Foundation.BOOL), use_last_error=False)(("IsProcessInWDAGContainer", windll["api-ms-win-security-isolatedcontainer-l1-1-1"]), ((1, 'Reserved'),(1, 'isProcessInWDAGContainer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsProcessInIsolatedContainer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(("IsProcessInIsolatedContainer", windll["api-ms-win-security-isolatedcontainer-l1-1-0"]), ((1, 'isProcessInIsolatedContainer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsProcessInIsolatedWindowsEnvironment():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(("IsProcessInIsolatedWindowsEnvironment", windll["IsolatedWindowsEnvironmentUtils"]), ((1, 'isProcessInIsolatedWindowsEnvironment'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateAppContainerProfile():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Security.SID_AND_ATTRIBUTES),UInt32,POINTER(win32more.Foundation.PSID), use_last_error=False)(("CreateAppContainerProfile", windll["USERENV"]), ((1, 'pszAppContainerName'),(1, 'pszDisplayName'),(1, 'pszDescription'),(1, 'pCapabilities'),(1, 'dwCapabilityCount'),(1, 'ppSidAppContainerSid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeleteAppContainerProfile():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(("DeleteAppContainerProfile", windll["USERENV"]), ((1, 'pszAppContainerName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetAppContainerRegistryLocation():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Registry.HKEY), use_last_error=False)(("GetAppContainerRegistryLocation", windll["USERENV"]), ((1, 'desiredAccess'),(1, 'phAppContainerKey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetAppContainerFolderPath():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("GetAppContainerFolderPath", windll["USERENV"]), ((1, 'pszAppContainerSid'),(1, 'ppszPath'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeriveRestrictedAppContainerSidFromAppContainerSidAndRestrictedName():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSID,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PSID), use_last_error=False)(("DeriveRestrictedAppContainerSidFromAppContainerSidAndRestrictedName", windll["USERENV"]), ((1, 'psidAppContainerSid'),(1, 'pszRestrictedAppContainerName'),(1, 'ppsidRestrictedAppContainerSid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeriveAppContainerSidFromAppContainerName():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PSID), use_last_error=False)(("DeriveAppContainerSidFromAppContainerName", windll["USERENV"]), ((1, 'pszAppContainerName'),(1, 'ppsidAppContainerSid'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "IsolatedAppLauncher",
    "IsolatedAppLauncherTelemetryParameters",
    "IIsolatedAppLauncher",
    "GetAppContainerNamedObjectPath",
    "IsProcessInWDAGContainer",
    "IsProcessInIsolatedContainer",
    "IsProcessInIsolatedWindowsEnvironment",
    "CreateAppContainerProfile",
    "DeleteAppContainerProfile",
    "GetAppContainerRegistryLocation",
    "GetAppContainerFolderPath",
    "DeriveRestrictedAppContainerSidFromAppContainerSidAndRestrictedName",
    "DeriveAppContainerSidFromAppContainerName",
]
