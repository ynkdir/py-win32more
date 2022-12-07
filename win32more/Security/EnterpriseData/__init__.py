from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Security.EnterpriseData
import win32more.Storage.Packaging.Appx
import win32more.System.Com
import win32more.System.WinRT
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
@winfunctype('srpapi.dll')
def SrpCreateThreadNetworkContext(enterpriseId: win32more.Foundation.PWSTR, threadNetworkContext: POINTER(win32more.Security.EnterpriseData.HTHREAD_NETWORK_CONTEXT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('srpapi.dll')
def SrpCloseThreadNetworkContext(threadNetworkContext: POINTER(win32more.Security.EnterpriseData.HTHREAD_NETWORK_CONTEXT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('srpapi.dll')
def SrpSetTokenEnterpriseId(tokenHandle: win32more.Foundation.HANDLE, enterpriseId: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('srpapi.dll')
def SrpGetEnterpriseIds(tokenHandle: win32more.Foundation.HANDLE, numberOfBytes: POINTER(UInt32), enterpriseIds: POINTER(win32more.Foundation.PWSTR), enterpriseIdCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('srpapi.dll')
def SrpEnablePermissiveModeFileEncryption(enterpriseId: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('srpapi.dll')
def SrpDisablePermissiveModeFileEncryption() -> win32more.Foundation.HRESULT: ...
@winfunctype('srpapi.dll')
def SrpGetEnterprisePolicy(tokenHandle: win32more.Foundation.HANDLE, policyFlags: POINTER(win32more.Security.EnterpriseData.ENTERPRISE_DATA_POLICIES)) -> win32more.Foundation.HRESULT: ...
@winfunctype('srpapi.dll')
def SrpIsTokenService(TokenHandle: win32more.Foundation.HANDLE, IsTokenService: c_char_p_no) -> win32more.Foundation.NTSTATUS: ...
@winfunctype('srpapi.dll')
def SrpDoesPolicyAllowAppExecution(packageId: POINTER(win32more.Storage.Packaging.Appx.PACKAGE_ID_head), isAllowed: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
@winfunctype('srpapi.dll')
def SrpHostingInitialize(Version: win32more.Security.EnterpriseData.SRPHOSTING_VERSION, Type: win32more.Security.EnterpriseData.SRPHOSTING_TYPE, pvData: c_void_p, cbData: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('srpapi.dll')
def SrpHostingTerminate(Type: win32more.Security.EnterpriseData.SRPHOSTING_TYPE) -> Void: ...
@winfunctype('efswrt.dll')
def ProtectFileToEnterpriseIdentity(fileOrFolderPath: win32more.Foundation.PWSTR, identity: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('efswrt.dll')
def UnprotectFile(fileOrFolderPath: win32more.Foundation.PWSTR, options: POINTER(win32more.Security.EnterpriseData.FILE_UNPROTECT_OPTIONS_head)) -> win32more.Foundation.HRESULT: ...
ENTERPRISE_DATA_POLICIES = UInt32
ENTERPRISE_POLICY_NONE: ENTERPRISE_DATA_POLICIES = 0
ENTERPRISE_POLICY_ALLOWED: ENTERPRISE_DATA_POLICIES = 1
ENTERPRISE_POLICY_ENLIGHTENED: ENTERPRISE_DATA_POLICIES = 2
ENTERPRISE_POLICY_EXEMPT: ENTERPRISE_DATA_POLICIES = 4
class FILE_UNPROTECT_OPTIONS(Structure):
    audit: Byte
class HTHREAD_NETWORK_CONTEXT(Structure):
    ThreadId: UInt32
    ThreadContext: win32more.Foundation.HANDLE
class IProtectionPolicyManagerInterop(c_void_p):
    extends: win32more.System.WinRT.IInspectable
    Guid = Guid('4652651d-c1fe-4ba1-9f-0a-c0-f5-65-96-f7-21')
    @commethod(6)
    def RequestAccessForWindowAsync(appWindow: win32more.Foundation.HWND, sourceIdentity: win32more.System.WinRT.HSTRING, targetIdentity: win32more.System.WinRT.HSTRING, riid: POINTER(Guid), asyncOperation: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetForWindow(appWindow: win32more.Foundation.HWND, riid: POINTER(Guid), result: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IProtectionPolicyManagerInterop2(c_void_p):
    extends: win32more.System.WinRT.IInspectable
    Guid = Guid('157cfbe4-a78d-4156-b3-84-61-fd-ac-41-e6-86')
    @commethod(6)
    def RequestAccessForAppWithWindowAsync(appWindow: win32more.Foundation.HWND, sourceIdentity: win32more.System.WinRT.HSTRING, appPackageFamilyName: win32more.System.WinRT.HSTRING, riid: POINTER(Guid), asyncOperation: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def RequestAccessWithAuditingInfoForWindowAsync(appWindow: win32more.Foundation.HWND, sourceIdentity: win32more.System.WinRT.HSTRING, targetIdentity: win32more.System.WinRT.HSTRING, auditInfoUnk: win32more.System.Com.IUnknown_head, riid: POINTER(Guid), asyncOperation: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def RequestAccessWithMessageForWindowAsync(appWindow: win32more.Foundation.HWND, sourceIdentity: win32more.System.WinRT.HSTRING, targetIdentity: win32more.System.WinRT.HSTRING, auditInfoUnk: win32more.System.Com.IUnknown_head, messageFromApp: win32more.System.WinRT.HSTRING, riid: POINTER(Guid), asyncOperation: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def RequestAccessForAppWithAuditingInfoForWindowAsync(appWindow: win32more.Foundation.HWND, sourceIdentity: win32more.System.WinRT.HSTRING, appPackageFamilyName: win32more.System.WinRT.HSTRING, auditInfoUnk: win32more.System.Com.IUnknown_head, riid: POINTER(Guid), asyncOperation: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def RequestAccessForAppWithMessageForWindowAsync(appWindow: win32more.Foundation.HWND, sourceIdentity: win32more.System.WinRT.HSTRING, appPackageFamilyName: win32more.System.WinRT.HSTRING, auditInfoUnk: win32more.System.Com.IUnknown_head, messageFromApp: win32more.System.WinRT.HSTRING, riid: POINTER(Guid), asyncOperation: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IProtectionPolicyManagerInterop3(c_void_p):
    extends: win32more.System.WinRT.IInspectable
    Guid = Guid('c1c03933-b398-4d93-b0-fd-29-72-ad-f8-02-c2')
    @commethod(6)
    def RequestAccessWithBehaviorForWindowAsync(appWindow: win32more.Foundation.HWND, sourceIdentity: win32more.System.WinRT.HSTRING, targetIdentity: win32more.System.WinRT.HSTRING, auditInfoUnk: win32more.System.Com.IUnknown_head, messageFromApp: win32more.System.WinRT.HSTRING, behavior: UInt32, riid: POINTER(Guid), asyncOperation: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def RequestAccessForAppWithBehaviorForWindowAsync(appWindow: win32more.Foundation.HWND, sourceIdentity: win32more.System.WinRT.HSTRING, appPackageFamilyName: win32more.System.WinRT.HSTRING, auditInfoUnk: win32more.System.Com.IUnknown_head, messageFromApp: win32more.System.WinRT.HSTRING, behavior: UInt32, riid: POINTER(Guid), asyncOperation: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def RequestAccessToFilesForAppForWindowAsync(appWindow: win32more.Foundation.HWND, sourceItemListUnk: win32more.System.Com.IUnknown_head, appPackageFamilyName: win32more.System.WinRT.HSTRING, auditInfoUnk: win32more.System.Com.IUnknown_head, riid: POINTER(Guid), asyncOperation: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def RequestAccessToFilesForAppWithMessageAndBehaviorForWindowAsync(appWindow: win32more.Foundation.HWND, sourceItemListUnk: win32more.System.Com.IUnknown_head, appPackageFamilyName: win32more.System.WinRT.HSTRING, auditInfoUnk: win32more.System.Com.IUnknown_head, messageFromApp: win32more.System.WinRT.HSTRING, behavior: UInt32, riid: POINTER(Guid), asyncOperation: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def RequestAccessToFilesForProcessForWindowAsync(appWindow: win32more.Foundation.HWND, sourceItemListUnk: win32more.System.Com.IUnknown_head, processId: UInt32, auditInfoUnk: win32more.System.Com.IUnknown_head, riid: POINTER(Guid), asyncOperation: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def RequestAccessToFilesForProcessWithMessageAndBehaviorForWindowAsync(appWindow: win32more.Foundation.HWND, sourceItemListUnk: win32more.System.Com.IUnknown_head, processId: UInt32, auditInfoUnk: win32more.System.Com.IUnknown_head, messageFromApp: win32more.System.WinRT.HSTRING, behavior: UInt32, riid: POINTER(Guid), asyncOperation: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
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
__all__ = [
    "ENTERPRISE_DATA_POLICIES",
    "ENTERPRISE_POLICY_ALLOWED",
    "ENTERPRISE_POLICY_ENLIGHTENED",
    "ENTERPRISE_POLICY_EXEMPT",
    "ENTERPRISE_POLICY_NONE",
    "FILE_UNPROTECT_OPTIONS",
    "HTHREAD_NETWORK_CONTEXT",
    "IProtectionPolicyManagerInterop",
    "IProtectionPolicyManagerInterop2",
    "IProtectionPolicyManagerInterop3",
    "ProtectFileToEnterpriseIdentity",
    "SRPHOSTING_TYPE",
    "SRPHOSTING_TYPE_NONE",
    "SRPHOSTING_TYPE_WINHTTP",
    "SRPHOSTING_TYPE_WININET",
    "SRPHOSTING_VERSION",
    "SRPHOSTING_VERSION1",
    "SrpCloseThreadNetworkContext",
    "SrpCreateThreadNetworkContext",
    "SrpDisablePermissiveModeFileEncryption",
    "SrpDoesPolicyAllowAppExecution",
    "SrpEnablePermissiveModeFileEncryption",
    "SrpGetEnterpriseIds",
    "SrpGetEnterprisePolicy",
    "SrpHostingInitialize",
    "SrpHostingTerminate",
    "SrpIsTokenService",
    "SrpSetTokenEnterpriseId",
    "UnprotectFile",
]
