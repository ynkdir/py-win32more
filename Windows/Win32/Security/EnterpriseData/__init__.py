from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.Foundation
import Windows.Win32.Security.EnterpriseData
import Windows.Win32.Storage.Packaging.Appx
import Windows.Win32.System.Com
import Windows.Win32.System.WinRT
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
@winfunctype('srpapi.dll')
def SrpCreateThreadNetworkContext(enterpriseId: Windows.Win32.Foundation.PWSTR, threadNetworkContext: POINTER(Windows.Win32.Security.EnterpriseData.HTHREAD_NETWORK_CONTEXT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('srpapi.dll')
def SrpCloseThreadNetworkContext(threadNetworkContext: POINTER(Windows.Win32.Security.EnterpriseData.HTHREAD_NETWORK_CONTEXT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('srpapi.dll')
def SrpSetTokenEnterpriseId(tokenHandle: Windows.Win32.Foundation.HANDLE, enterpriseId: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('srpapi.dll')
def SrpGetEnterpriseIds(tokenHandle: Windows.Win32.Foundation.HANDLE, numberOfBytes: POINTER(UInt32), enterpriseIds: POINTER(Windows.Win32.Foundation.PWSTR), enterpriseIdCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('srpapi.dll')
def SrpEnablePermissiveModeFileEncryption(enterpriseId: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('srpapi.dll')
def SrpDisablePermissiveModeFileEncryption() -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('srpapi.dll')
def SrpGetEnterprisePolicy(tokenHandle: Windows.Win32.Foundation.HANDLE, policyFlags: POINTER(Windows.Win32.Security.EnterpriseData.ENTERPRISE_DATA_POLICIES)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('srpapi.dll')
def SrpIsTokenService(TokenHandle: Windows.Win32.Foundation.HANDLE, IsTokenService: POINTER(Byte)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('srpapi.dll')
def SrpDoesPolicyAllowAppExecution(packageId: POINTER(Windows.Win32.Storage.Packaging.Appx.PACKAGE_ID_head), isAllowed: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('srpapi.dll')
def SrpHostingInitialize(Version: Windows.Win32.Security.EnterpriseData.SRPHOSTING_VERSION, Type: Windows.Win32.Security.EnterpriseData.SRPHOSTING_TYPE, pvData: c_void_p, cbData: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('srpapi.dll')
def SrpHostingTerminate(Type: Windows.Win32.Security.EnterpriseData.SRPHOSTING_TYPE) -> Void: ...
@winfunctype('efswrt.dll')
def ProtectFileToEnterpriseIdentity(fileOrFolderPath: Windows.Win32.Foundation.PWSTR, identity: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('efswrt.dll')
def UnprotectFile(fileOrFolderPath: Windows.Win32.Foundation.PWSTR, options: POINTER(Windows.Win32.Security.EnterpriseData.FILE_UNPROTECT_OPTIONS_head)) -> Windows.Win32.Foundation.HRESULT: ...
ENTERPRISE_DATA_POLICIES = Int32
ENTERPRISE_POLICY_NONE: ENTERPRISE_DATA_POLICIES = 0
ENTERPRISE_POLICY_ALLOWED: ENTERPRISE_DATA_POLICIES = 1
ENTERPRISE_POLICY_ENLIGHTENED: ENTERPRISE_DATA_POLICIES = 2
ENTERPRISE_POLICY_EXEMPT: ENTERPRISE_DATA_POLICIES = 4
class FILE_UNPROTECT_OPTIONS(EasyCastStructure):
    audit: Byte
class HTHREAD_NETWORK_CONTEXT(EasyCastStructure):
    ThreadId: UInt32
    ThreadContext: Windows.Win32.Foundation.HANDLE
class IProtectionPolicyManagerInterop(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4652651d-c1fe-4ba1-9f-0a-c0-f5-65-96-f7-21')
    @commethod(6)
    def RequestAccessForWindowAsync(self, appWindow: Windows.Win32.Foundation.HWND, sourceIdentity: Windows.Win32.System.WinRT.HSTRING, targetIdentity: Windows.Win32.System.WinRT.HSTRING, riid: POINTER(Guid), asyncOperation: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetForWindow(self, appWindow: Windows.Win32.Foundation.HWND, riid: POINTER(Guid), result: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IProtectionPolicyManagerInterop2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('157cfbe4-a78d-4156-b3-84-61-fd-ac-41-e6-86')
    @commethod(6)
    def RequestAccessForAppWithWindowAsync(self, appWindow: Windows.Win32.Foundation.HWND, sourceIdentity: Windows.Win32.System.WinRT.HSTRING, appPackageFamilyName: Windows.Win32.System.WinRT.HSTRING, riid: POINTER(Guid), asyncOperation: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RequestAccessWithAuditingInfoForWindowAsync(self, appWindow: Windows.Win32.Foundation.HWND, sourceIdentity: Windows.Win32.System.WinRT.HSTRING, targetIdentity: Windows.Win32.System.WinRT.HSTRING, auditInfoUnk: Windows.Win32.System.Com.IUnknown_head, riid: POINTER(Guid), asyncOperation: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RequestAccessWithMessageForWindowAsync(self, appWindow: Windows.Win32.Foundation.HWND, sourceIdentity: Windows.Win32.System.WinRT.HSTRING, targetIdentity: Windows.Win32.System.WinRT.HSTRING, auditInfoUnk: Windows.Win32.System.Com.IUnknown_head, messageFromApp: Windows.Win32.System.WinRT.HSTRING, riid: POINTER(Guid), asyncOperation: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def RequestAccessForAppWithAuditingInfoForWindowAsync(self, appWindow: Windows.Win32.Foundation.HWND, sourceIdentity: Windows.Win32.System.WinRT.HSTRING, appPackageFamilyName: Windows.Win32.System.WinRT.HSTRING, auditInfoUnk: Windows.Win32.System.Com.IUnknown_head, riid: POINTER(Guid), asyncOperation: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def RequestAccessForAppWithMessageForWindowAsync(self, appWindow: Windows.Win32.Foundation.HWND, sourceIdentity: Windows.Win32.System.WinRT.HSTRING, appPackageFamilyName: Windows.Win32.System.WinRT.HSTRING, auditInfoUnk: Windows.Win32.System.Com.IUnknown_head, messageFromApp: Windows.Win32.System.WinRT.HSTRING, riid: POINTER(Guid), asyncOperation: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IProtectionPolicyManagerInterop3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c1c03933-b398-4d93-b0-fd-29-72-ad-f8-02-c2')
    @commethod(6)
    def RequestAccessWithBehaviorForWindowAsync(self, appWindow: Windows.Win32.Foundation.HWND, sourceIdentity: Windows.Win32.System.WinRT.HSTRING, targetIdentity: Windows.Win32.System.WinRT.HSTRING, auditInfoUnk: Windows.Win32.System.Com.IUnknown_head, messageFromApp: Windows.Win32.System.WinRT.HSTRING, behavior: UInt32, riid: POINTER(Guid), asyncOperation: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RequestAccessForAppWithBehaviorForWindowAsync(self, appWindow: Windows.Win32.Foundation.HWND, sourceIdentity: Windows.Win32.System.WinRT.HSTRING, appPackageFamilyName: Windows.Win32.System.WinRT.HSTRING, auditInfoUnk: Windows.Win32.System.Com.IUnknown_head, messageFromApp: Windows.Win32.System.WinRT.HSTRING, behavior: UInt32, riid: POINTER(Guid), asyncOperation: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RequestAccessToFilesForAppForWindowAsync(self, appWindow: Windows.Win32.Foundation.HWND, sourceItemListUnk: Windows.Win32.System.Com.IUnknown_head, appPackageFamilyName: Windows.Win32.System.WinRT.HSTRING, auditInfoUnk: Windows.Win32.System.Com.IUnknown_head, riid: POINTER(Guid), asyncOperation: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def RequestAccessToFilesForAppWithMessageAndBehaviorForWindowAsync(self, appWindow: Windows.Win32.Foundation.HWND, sourceItemListUnk: Windows.Win32.System.Com.IUnknown_head, appPackageFamilyName: Windows.Win32.System.WinRT.HSTRING, auditInfoUnk: Windows.Win32.System.Com.IUnknown_head, messageFromApp: Windows.Win32.System.WinRT.HSTRING, behavior: UInt32, riid: POINTER(Guid), asyncOperation: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def RequestAccessToFilesForProcessForWindowAsync(self, appWindow: Windows.Win32.Foundation.HWND, sourceItemListUnk: Windows.Win32.System.Com.IUnknown_head, processId: UInt32, auditInfoUnk: Windows.Win32.System.Com.IUnknown_head, riid: POINTER(Guid), asyncOperation: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RequestAccessToFilesForProcessWithMessageAndBehaviorForWindowAsync(self, appWindow: Windows.Win32.Foundation.HWND, sourceItemListUnk: Windows.Win32.System.Com.IUnknown_head, processId: UInt32, auditInfoUnk: Windows.Win32.System.Com.IUnknown_head, messageFromApp: Windows.Win32.System.WinRT.HSTRING, behavior: UInt32, riid: POINTER(Guid), asyncOperation: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
SRPHOSTING_TYPE = Int32
SRPHOSTING_TYPE_NONE: SRPHOSTING_TYPE = 0
SRPHOSTING_TYPE_WINHTTP: SRPHOSTING_TYPE = 1
SRPHOSTING_TYPE_WININET: SRPHOSTING_TYPE = 2
SRPHOSTING_VERSION = Int32
SRPHOSTING_VERSION1: SRPHOSTING_VERSION = 1
make_head(_module, 'FILE_UNPROTECT_OPTIONS')
make_head(_module, 'HTHREAD_NETWORK_CONTEXT')
make_head(_module, 'IProtectionPolicyManagerInterop')
make_head(_module, 'IProtectionPolicyManagerInterop2')
make_head(_module, 'IProtectionPolicyManagerInterop3')
