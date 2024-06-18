from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Security
import win32more.Windows.Win32.Security.Isolation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Registry
WDAG_CLIPBOARD_TAG: String = 'CrossIsolatedEnvironmentContent'
@winfunctype('KERNEL32.dll')
def GetAppContainerNamedObjectPath(Token: win32more.Windows.Win32.Foundation.HANDLE, AppContainerSid: win32more.Windows.Win32.Security.PSID, ObjectPathLength: UInt32, ObjectPath: win32more.Windows.Win32.Foundation.PWSTR, ReturnLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-security-isolatedcontainer-l1-1-1.dll')
def IsProcessInWDAGContainer(Reserved: VoidPtr, isProcessInWDAGContainer: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-security-isolatedcontainer-l1-1-0.dll')
def IsProcessInIsolatedContainer(isProcessInIsolatedContainer: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('IsolatedWindowsEnvironmentUtils.dll')
def IsProcessInIsolatedWindowsEnvironment(isProcessInIsolatedWindowsEnvironment: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('IsolatedWindowsEnvironmentUtils.dll')
def IsCrossIsolatedEnvironmentClipboardContent(isCrossIsolatedEnvironmentClipboardContent: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('USERENV.dll')
def CreateAppContainerProfile(pszAppContainerName: win32more.Windows.Win32.Foundation.PWSTR, pszDisplayName: win32more.Windows.Win32.Foundation.PWSTR, pszDescription: win32more.Windows.Win32.Foundation.PWSTR, pCapabilities: POINTER(win32more.Windows.Win32.Security.SID_AND_ATTRIBUTES), dwCapabilityCount: UInt32, ppSidAppContainerSid: POINTER(win32more.Windows.Win32.Security.PSID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('USERENV.dll')
def DeleteAppContainerProfile(pszAppContainerName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('USERENV.dll')
def GetAppContainerRegistryLocation(desiredAccess: UInt32, phAppContainerKey: POINTER(win32more.Windows.Win32.System.Registry.HKEY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('USERENV.dll')
def GetAppContainerFolderPath(pszAppContainerSid: win32more.Windows.Win32.Foundation.PWSTR, ppszPath: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('USERENV.dll')
def DeriveRestrictedAppContainerSidFromAppContainerSidAndRestrictedName(psidAppContainerSid: win32more.Windows.Win32.Security.PSID, pszRestrictedAppContainerName: win32more.Windows.Win32.Foundation.PWSTR, ppsidRestrictedAppContainerSid: POINTER(win32more.Windows.Win32.Security.PSID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('USERENV.dll')
def DeriveAppContainerSidFromAppContainerName(pszAppContainerName: win32more.Windows.Win32.Foundation.PWSTR, ppsidAppContainerSid: POINTER(win32more.Windows.Win32.Security.PSID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IIsolatedAppLauncher(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f686878f-7b42-4cc4-96fb-f4f3b6e3d24d}')
    @commethod(3)
    def Launch(self, appUserModelId: win32more.Windows.Win32.Foundation.PWSTR, arguments: win32more.Windows.Win32.Foundation.PWSTR, telemetryParameters: POINTER(win32more.Windows.Win32.Security.Isolation.IsolatedAppLauncherTelemetryParameters)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IIsolatedProcessLauncher(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1aa24232-9a91-4201-88cb-122f9d6522e0}')
    @commethod(3)
    def LaunchProcess(self, process: win32more.Windows.Win32.Foundation.PWSTR, arguments: win32more.Windows.Win32.Foundation.PWSTR, workingDirectory: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ShareDirectory(self, hostPath: win32more.Windows.Win32.Foundation.PWSTR, containerPath: win32more.Windows.Win32.Foundation.PWSTR, readOnly: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetContainerGuid(self, guid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AllowSetForegroundAccess(self, pid: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def IsContainerRunning(self, running: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IIsolatedProcessLauncher2(ComPtr):
    extends: win32more.Windows.Win32.Security.Isolation.IIsolatedProcessLauncher
    _iid_ = Guid('{780e4416-5e72-4123-808e-66dc6479feef}')
    @commethod(8)
    def LaunchProcess2(self, process: win32more.Windows.Win32.Foundation.PWSTR, arguments: win32more.Windows.Win32.Foundation.PWSTR, workingDirectory: win32more.Windows.Win32.Foundation.PWSTR, correlationGuid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
IsolatedAppLauncher = Guid('{bc812430-e75e-4fd1-9641-1f9f1e2d9a1f}')
class IsolatedAppLauncherTelemetryParameters(Structure):
    EnableForLaunch: win32more.Windows.Win32.Foundation.BOOL
    CorrelationGUID: Guid


make_ready(__name__)
