from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.Security
import Windows.Win32.Security.Isolation
import Windows.Win32.System.Com
import Windows.Win32.System.Registry
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
WDAG_CLIPBOARD_TAG: String = 'CrossIsolatedEnvironmentContent'
@winfunctype('KERNEL32.dll')
def GetAppContainerNamedObjectPath(Token: Windows.Win32.Foundation.HANDLE, AppContainerSid: Windows.Win32.Foundation.PSID, ObjectPathLength: UInt32, ObjectPath: Windows.Win32.Foundation.PWSTR, ReturnLength: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-security-isolatedcontainer-l1-1-1.dll')
def IsProcessInWDAGContainer(Reserved: c_void_p, isProcessInWDAGContainer: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-security-isolatedcontainer-l1-1-0.dll')
def IsProcessInIsolatedContainer(isProcessInIsolatedContainer: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('IsolatedWindowsEnvironmentUtils.dll')
def IsProcessInIsolatedWindowsEnvironment(isProcessInIsolatedWindowsEnvironment: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('IsolatedWindowsEnvironmentUtils.dll')
def IsCrossIsolatedEnvironmentClipboardContent(isCrossIsolatedEnvironmentClipboardContent: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('USERENV.dll')
def CreateAppContainerProfile(pszAppContainerName: Windows.Win32.Foundation.PWSTR, pszDisplayName: Windows.Win32.Foundation.PWSTR, pszDescription: Windows.Win32.Foundation.PWSTR, pCapabilities: POINTER(Windows.Win32.Security.SID_AND_ATTRIBUTES_head), dwCapabilityCount: UInt32, ppSidAppContainerSid: POINTER(Windows.Win32.Foundation.PSID)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('USERENV.dll')
def DeleteAppContainerProfile(pszAppContainerName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('USERENV.dll')
def GetAppContainerRegistryLocation(desiredAccess: UInt32, phAppContainerKey: POINTER(Windows.Win32.System.Registry.HKEY)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('USERENV.dll')
def GetAppContainerFolderPath(pszAppContainerSid: Windows.Win32.Foundation.PWSTR, ppszPath: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('USERENV.dll')
def DeriveRestrictedAppContainerSidFromAppContainerSidAndRestrictedName(psidAppContainerSid: Windows.Win32.Foundation.PSID, pszRestrictedAppContainerName: Windows.Win32.Foundation.PWSTR, ppsidRestrictedAppContainerSid: POINTER(Windows.Win32.Foundation.PSID)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('USERENV.dll')
def DeriveAppContainerSidFromAppContainerName(pszAppContainerName: Windows.Win32.Foundation.PWSTR, ppsidAppContainerSid: POINTER(Windows.Win32.Foundation.PSID)) -> Windows.Win32.Foundation.HRESULT: ...
class IIsolatedAppLauncher(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f686878f-7b42-4cc4-96fb-f4f3b6e3d24d}')
    @commethod(3)
    def Launch(self, appUserModelId: Windows.Win32.Foundation.PWSTR, arguments: Windows.Win32.Foundation.PWSTR, telemetryParameters: POINTER(Windows.Win32.Security.Isolation.IsolatedAppLauncherTelemetryParameters_head)) -> Windows.Win32.Foundation.HRESULT: ...
IsolatedAppLauncher = Guid('{bc812430-e75e-4fd1-9641-1f9f1e2d9a1f}')
class IsolatedAppLauncherTelemetryParameters(EasyCastStructure):
    EnableForLaunch: Windows.Win32.Foundation.BOOL
    CorrelationGUID: Guid
make_head(_module, 'IIsolatedAppLauncher')
make_head(_module, 'IsolatedAppLauncherTelemetryParameters')
