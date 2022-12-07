from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Security
import win32more.Security.Isolation
import win32more.System.Com
import win32more.System.Registry
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
@winfunctype('KERNEL32.dll')
def GetAppContainerNamedObjectPath(Token: win32more.Foundation.HANDLE, AppContainerSid: win32more.Foundation.PSID, ObjectPathLength: UInt32, ObjectPath: win32more.Foundation.PWSTR, ReturnLength: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('api-ms-win-security-isolatedcontainer-l1-1-1.dll')
def IsProcessInWDAGContainer(Reserved: c_void_p, isProcessInWDAGContainer: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-security-isolatedcontainer-l1-1-0.dll')
def IsProcessInIsolatedContainer(isProcessInIsolatedContainer: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
@winfunctype('IsolatedWindowsEnvironmentUtils.dll')
def IsProcessInIsolatedWindowsEnvironment(isProcessInIsolatedWindowsEnvironment: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
@winfunctype('USERENV.dll')
def CreateAppContainerProfile(pszAppContainerName: win32more.Foundation.PWSTR, pszDisplayName: win32more.Foundation.PWSTR, pszDescription: win32more.Foundation.PWSTR, pCapabilities: POINTER(win32more.Security.SID_AND_ATTRIBUTES_head), dwCapabilityCount: UInt32, ppSidAppContainerSid: POINTER(win32more.Foundation.PSID)) -> win32more.Foundation.HRESULT: ...
@winfunctype('USERENV.dll')
def DeleteAppContainerProfile(pszAppContainerName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('USERENV.dll')
def GetAppContainerRegistryLocation(desiredAccess: UInt32, phAppContainerKey: POINTER(win32more.System.Registry.HKEY)) -> win32more.Foundation.HRESULT: ...
@winfunctype('USERENV.dll')
def GetAppContainerFolderPath(pszAppContainerSid: win32more.Foundation.PWSTR, ppszPath: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('USERENV.dll')
def DeriveRestrictedAppContainerSidFromAppContainerSidAndRestrictedName(psidAppContainerSid: win32more.Foundation.PSID, pszRestrictedAppContainerName: win32more.Foundation.PWSTR, ppsidRestrictedAppContainerSid: POINTER(win32more.Foundation.PSID)) -> win32more.Foundation.HRESULT: ...
@winfunctype('USERENV.dll')
def DeriveAppContainerSidFromAppContainerName(pszAppContainerName: win32more.Foundation.PWSTR, ppsidAppContainerSid: POINTER(win32more.Foundation.PSID)) -> win32more.Foundation.HRESULT: ...
class IIsolatedAppLauncher(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('f686878f-7b42-4cc4-96-fb-f4-f3-b6-e3-d2-4d')
    @commethod(3)
    def Launch(appUserModelId: win32more.Foundation.PWSTR, arguments: win32more.Foundation.PWSTR, telemetryParameters: POINTER(win32more.Security.Isolation.IsolatedAppLauncherTelemetryParameters_head)) -> win32more.Foundation.HRESULT: ...
IsolatedAppLauncher = Guid('bc812430-e75e-4fd1-96-41-1f-9f-1e-2d-9a-1f')
class IsolatedAppLauncherTelemetryParameters(Structure):
    EnableForLaunch: win32more.Foundation.BOOL
    CorrelationGUID: Guid
make_head(_module, 'IIsolatedAppLauncher')
make_head(_module, 'IsolatedAppLauncherTelemetryParameters')
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
