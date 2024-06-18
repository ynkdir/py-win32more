from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Security.EnterpriseData
import win32more.Windows.Win32.Storage.Packaging.Appx
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT
@winfunctype('srpapi.dll')
def SrpCreateThreadNetworkContext(enterpriseId: win32more.Windows.Win32.Foundation.PWSTR, threadNetworkContext: POINTER(win32more.Windows.Win32.Security.EnterpriseData.HTHREAD_NETWORK_CONTEXT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('srpapi.dll')
def SrpCloseThreadNetworkContext(threadNetworkContext: POINTER(win32more.Windows.Win32.Security.EnterpriseData.HTHREAD_NETWORK_CONTEXT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('srpapi.dll')
def SrpSetTokenEnterpriseId(tokenHandle: win32more.Windows.Win32.Foundation.HANDLE, enterpriseId: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('srpapi.dll')
def SrpGetEnterpriseIds(tokenHandle: win32more.Windows.Win32.Foundation.HANDLE, numberOfBytes: POINTER(UInt32), enterpriseIds: POINTER(win32more.Windows.Win32.Foundation.PWSTR), enterpriseIdCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('srpapi.dll')
def SrpEnablePermissiveModeFileEncryption(enterpriseId: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('srpapi.dll')
def SrpDisablePermissiveModeFileEncryption() -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('srpapi.dll')
def SrpGetEnterprisePolicy(tokenHandle: win32more.Windows.Win32.Foundation.HANDLE, policyFlags: POINTER(win32more.Windows.Win32.Security.EnterpriseData.ENTERPRISE_DATA_POLICIES)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('srpapi.dll')
def SrpIsTokenService(TokenHandle: win32more.Windows.Win32.Foundation.HANDLE, IsTokenService: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('srpapi.dll')
def SrpDoesPolicyAllowAppExecution(packageId: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.PACKAGE_ID), isAllowed: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('srpapi.dll')
def SrpHostingInitialize(Version: win32more.Windows.Win32.Security.EnterpriseData.SRPHOSTING_VERSION, Type: win32more.Windows.Win32.Security.EnterpriseData.SRPHOSTING_TYPE, pvData: VoidPtr, cbData: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('srpapi.dll')
def SrpHostingTerminate(Type: win32more.Windows.Win32.Security.EnterpriseData.SRPHOSTING_TYPE) -> Void: ...
@winfunctype('efswrt.dll')
def ProtectFileToEnterpriseIdentity(fileOrFolderPath: win32more.Windows.Win32.Foundation.PWSTR, identity: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('efswrt.dll')
def UnprotectFile(fileOrFolderPath: win32more.Windows.Win32.Foundation.PWSTR, options: POINTER(win32more.Windows.Win32.Security.EnterpriseData.FILE_UNPROTECT_OPTIONS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
ENTERPRISE_DATA_POLICIES = Int32
ENTERPRISE_POLICY_NONE: win32more.Windows.Win32.Security.EnterpriseData.ENTERPRISE_DATA_POLICIES = 0
ENTERPRISE_POLICY_ALLOWED: win32more.Windows.Win32.Security.EnterpriseData.ENTERPRISE_DATA_POLICIES = 1
ENTERPRISE_POLICY_ENLIGHTENED: win32more.Windows.Win32.Security.EnterpriseData.ENTERPRISE_DATA_POLICIES = 2
ENTERPRISE_POLICY_EXEMPT: win32more.Windows.Win32.Security.EnterpriseData.ENTERPRISE_DATA_POLICIES = 4
class FILE_UNPROTECT_OPTIONS(Structure):
    audit: Byte
class HTHREAD_NETWORK_CONTEXT(Structure):
    ThreadId: UInt32
    ThreadContext: win32more.Windows.Win32.Foundation.HANDLE
class IProtectionPolicyManagerInterop(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{4652651d-c1fe-4ba1-9f0a-c0f56596f721}')
    @commethod(6)
    def RequestAccessForWindowAsync(self, appWindow: win32more.Windows.Win32.Foundation.HWND, sourceIdentity: win32more.Windows.Win32.System.WinRT.HSTRING, targetIdentity: win32more.Windows.Win32.System.WinRT.HSTRING, riid: POINTER(Guid), asyncOperation: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetForWindow(self, appWindow: win32more.Windows.Win32.Foundation.HWND, riid: POINTER(Guid), result: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IProtectionPolicyManagerInterop2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{157cfbe4-a78d-4156-b384-61fdac41e686}')
    @commethod(6)
    def RequestAccessForAppWithWindowAsync(self, appWindow: win32more.Windows.Win32.Foundation.HWND, sourceIdentity: win32more.Windows.Win32.System.WinRT.HSTRING, appPackageFamilyName: win32more.Windows.Win32.System.WinRT.HSTRING, riid: POINTER(Guid), asyncOperation: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RequestAccessWithAuditingInfoForWindowAsync(self, appWindow: win32more.Windows.Win32.Foundation.HWND, sourceIdentity: win32more.Windows.Win32.System.WinRT.HSTRING, targetIdentity: win32more.Windows.Win32.System.WinRT.HSTRING, auditInfoUnk: win32more.Windows.Win32.System.Com.IUnknown, riid: POINTER(Guid), asyncOperation: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RequestAccessWithMessageForWindowAsync(self, appWindow: win32more.Windows.Win32.Foundation.HWND, sourceIdentity: win32more.Windows.Win32.System.WinRT.HSTRING, targetIdentity: win32more.Windows.Win32.System.WinRT.HSTRING, auditInfoUnk: win32more.Windows.Win32.System.Com.IUnknown, messageFromApp: win32more.Windows.Win32.System.WinRT.HSTRING, riid: POINTER(Guid), asyncOperation: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def RequestAccessForAppWithAuditingInfoForWindowAsync(self, appWindow: win32more.Windows.Win32.Foundation.HWND, sourceIdentity: win32more.Windows.Win32.System.WinRT.HSTRING, appPackageFamilyName: win32more.Windows.Win32.System.WinRT.HSTRING, auditInfoUnk: win32more.Windows.Win32.System.Com.IUnknown, riid: POINTER(Guid), asyncOperation: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def RequestAccessForAppWithMessageForWindowAsync(self, appWindow: win32more.Windows.Win32.Foundation.HWND, sourceIdentity: win32more.Windows.Win32.System.WinRT.HSTRING, appPackageFamilyName: win32more.Windows.Win32.System.WinRT.HSTRING, auditInfoUnk: win32more.Windows.Win32.System.Com.IUnknown, messageFromApp: win32more.Windows.Win32.System.WinRT.HSTRING, riid: POINTER(Guid), asyncOperation: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IProtectionPolicyManagerInterop3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{c1c03933-b398-4d93-b0fd-2972adf802c2}')
    @commethod(6)
    def RequestAccessWithBehaviorForWindowAsync(self, appWindow: win32more.Windows.Win32.Foundation.HWND, sourceIdentity: win32more.Windows.Win32.System.WinRT.HSTRING, targetIdentity: win32more.Windows.Win32.System.WinRT.HSTRING, auditInfoUnk: win32more.Windows.Win32.System.Com.IUnknown, messageFromApp: win32more.Windows.Win32.System.WinRT.HSTRING, behavior: UInt32, riid: POINTER(Guid), asyncOperation: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RequestAccessForAppWithBehaviorForWindowAsync(self, appWindow: win32more.Windows.Win32.Foundation.HWND, sourceIdentity: win32more.Windows.Win32.System.WinRT.HSTRING, appPackageFamilyName: win32more.Windows.Win32.System.WinRT.HSTRING, auditInfoUnk: win32more.Windows.Win32.System.Com.IUnknown, messageFromApp: win32more.Windows.Win32.System.WinRT.HSTRING, behavior: UInt32, riid: POINTER(Guid), asyncOperation: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RequestAccessToFilesForAppForWindowAsync(self, appWindow: win32more.Windows.Win32.Foundation.HWND, sourceItemListUnk: win32more.Windows.Win32.System.Com.IUnknown, appPackageFamilyName: win32more.Windows.Win32.System.WinRT.HSTRING, auditInfoUnk: win32more.Windows.Win32.System.Com.IUnknown, riid: POINTER(Guid), asyncOperation: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def RequestAccessToFilesForAppWithMessageAndBehaviorForWindowAsync(self, appWindow: win32more.Windows.Win32.Foundation.HWND, sourceItemListUnk: win32more.Windows.Win32.System.Com.IUnknown, appPackageFamilyName: win32more.Windows.Win32.System.WinRT.HSTRING, auditInfoUnk: win32more.Windows.Win32.System.Com.IUnknown, messageFromApp: win32more.Windows.Win32.System.WinRT.HSTRING, behavior: UInt32, riid: POINTER(Guid), asyncOperation: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def RequestAccessToFilesForProcessForWindowAsync(self, appWindow: win32more.Windows.Win32.Foundation.HWND, sourceItemListUnk: win32more.Windows.Win32.System.Com.IUnknown, processId: UInt32, auditInfoUnk: win32more.Windows.Win32.System.Com.IUnknown, riid: POINTER(Guid), asyncOperation: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RequestAccessToFilesForProcessWithMessageAndBehaviorForWindowAsync(self, appWindow: win32more.Windows.Win32.Foundation.HWND, sourceItemListUnk: win32more.Windows.Win32.System.Com.IUnknown, processId: UInt32, auditInfoUnk: win32more.Windows.Win32.System.Com.IUnknown, messageFromApp: win32more.Windows.Win32.System.WinRT.HSTRING, behavior: UInt32, riid: POINTER(Guid), asyncOperation: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
SRPHOSTING_TYPE = Int32
SRPHOSTING_TYPE_NONE: win32more.Windows.Win32.Security.EnterpriseData.SRPHOSTING_TYPE = 0
SRPHOSTING_TYPE_WINHTTP: win32more.Windows.Win32.Security.EnterpriseData.SRPHOSTING_TYPE = 1
SRPHOSTING_TYPE_WININET: win32more.Windows.Win32.Security.EnterpriseData.SRPHOSTING_TYPE = 2
SRPHOSTING_VERSION = Int32
SRPHOSTING_VERSION1: win32more.Windows.Win32.Security.EnterpriseData.SRPHOSTING_VERSION = 1


make_ready(__name__)
