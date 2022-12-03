from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Security.EnterpriseData
import win32more.Storage.Packaging.Appx
import win32more.System.Com
import win32more.System.WinRT
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
def _define_SrpCreateThreadNetworkContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Security.EnterpriseData.HTHREAD_NETWORK_CONTEXT_head))(('SrpCreateThreadNetworkContext', windll['srpapi.dll']), ((1, 'enterpriseId'),(1, 'threadNetworkContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SrpCloseThreadNetworkContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.EnterpriseData.HTHREAD_NETWORK_CONTEXT_head))(('SrpCloseThreadNetworkContext', windll['srpapi.dll']), ((1, 'threadNetworkContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SrpSetTokenEnterpriseId():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR)(('SrpSetTokenEnterpriseId', windll['srpapi.dll']), ((1, 'tokenHandle'),(1, 'enterpriseId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SrpGetEnterpriseIds():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(UInt32),POINTER(win32more.Foundation.PWSTR),POINTER(UInt32))(('SrpGetEnterpriseIds', windll['srpapi.dll']), ((1, 'tokenHandle'),(1, 'numberOfBytes'),(1, 'enterpriseIds'),(1, 'enterpriseIdCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SrpEnablePermissiveModeFileEncryption():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(('SrpEnablePermissiveModeFileEncryption', windll['srpapi.dll']), ((1, 'enterpriseId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SrpDisablePermissiveModeFileEncryption():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,)(('SrpDisablePermissiveModeFileEncryption', windll['srpapi.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_SrpGetEnterprisePolicy():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(win32more.Security.EnterpriseData.ENTERPRISE_DATA_POLICIES))(('SrpGetEnterprisePolicy', windll['srpapi.dll']), ((1, 'tokenHandle'),(1, 'policyFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SrpIsTokenService():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,win32more.Foundation.HANDLE,c_char_p_no)(('SrpIsTokenService', windll['srpapi.dll']), ((1, 'TokenHandle'),(1, 'IsTokenService'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SrpDoesPolicyAllowAppExecution():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.PACKAGE_ID_head),POINTER(win32more.Foundation.BOOL))(('SrpDoesPolicyAllowAppExecution', windll['srpapi.dll']), ((1, 'packageId'),(1, 'isAllowed'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SrpHostingInitialize():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.EnterpriseData.SRPHOSTING_VERSION,win32more.Security.EnterpriseData.SRPHOSTING_TYPE,c_void_p,UInt32)(('SrpHostingInitialize', windll['srpapi.dll']), ((1, 'Version'),(1, 'Type'),(1, 'pvData'),(1, 'cbData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SrpHostingTerminate():
    try:
        return WINFUNCTYPE(Void,win32more.Security.EnterpriseData.SRPHOSTING_TYPE)(('SrpHostingTerminate', windll['srpapi.dll']), ((1, 'Type'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ProtectFileToEnterpriseIdentity():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('ProtectFileToEnterpriseIdentity', windll['efswrt.dll']), ((1, 'fileOrFolderPath'),(1, 'identity'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UnprotectFile():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Security.EnterpriseData.FILE_UNPROTECT_OPTIONS_head))(('UnprotectFile', windll['efswrt.dll']), ((1, 'fileOrFolderPath'),(1, 'options'),))
    except (FileNotFoundError, AttributeError):
        return None
ENTERPRISE_DATA_POLICIES = UInt32
ENTERPRISE_POLICY_NONE = 0
ENTERPRISE_POLICY_ALLOWED = 1
ENTERPRISE_POLICY_ENLIGHTENED = 2
ENTERPRISE_POLICY_EXEMPT = 4
def _define_FILE_UNPROTECT_OPTIONS_head():
    class FILE_UNPROTECT_OPTIONS(Structure):
        pass
    return FILE_UNPROTECT_OPTIONS
def _define_FILE_UNPROTECT_OPTIONS():
    FILE_UNPROTECT_OPTIONS = win32more.Security.EnterpriseData.FILE_UNPROTECT_OPTIONS_head
    FILE_UNPROTECT_OPTIONS._fields_ = [
        ('audit', Byte),
    ]
    return FILE_UNPROTECT_OPTIONS
def _define_HTHREAD_NETWORK_CONTEXT_head():
    class HTHREAD_NETWORK_CONTEXT(Structure):
        pass
    return HTHREAD_NETWORK_CONTEXT
def _define_HTHREAD_NETWORK_CONTEXT():
    HTHREAD_NETWORK_CONTEXT = win32more.Security.EnterpriseData.HTHREAD_NETWORK_CONTEXT_head
    HTHREAD_NETWORK_CONTEXT._fields_ = [
        ('ThreadId', UInt32),
        ('ThreadContext', win32more.Foundation.HANDLE),
    ]
    return HTHREAD_NETWORK_CONTEXT
def _define_IProtectionPolicyManagerInterop_head():
    class IProtectionPolicyManagerInterop(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('4652651d-c1fe-4ba1-9f-0a-c0-f5-65-96-f7-21')
    return IProtectionPolicyManagerInterop
def _define_IProtectionPolicyManagerInterop():
    IProtectionPolicyManagerInterop = win32more.Security.EnterpriseData.IProtectionPolicyManagerInterop_head
    IProtectionPolicyManagerInterop.RequestAccessForWindowAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,POINTER(Guid),POINTER(c_void_p))(6, 'RequestAccessForWindowAsync', ((1, 'appWindow'),(1, 'sourceIdentity'),(1, 'targetIdentity'),(1, 'riid'),(1, 'asyncOperation'),)))
    IProtectionPolicyManagerInterop.GetForWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(Guid),POINTER(c_void_p))(7, 'GetForWindow', ((1, 'appWindow'),(1, 'riid'),(1, 'result'),)))
    win32more.System.WinRT.IInspectable
    return IProtectionPolicyManagerInterop
def _define_IProtectionPolicyManagerInterop2_head():
    class IProtectionPolicyManagerInterop2(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('157cfbe4-a78d-4156-b3-84-61-fd-ac-41-e6-86')
    return IProtectionPolicyManagerInterop2
def _define_IProtectionPolicyManagerInterop2():
    IProtectionPolicyManagerInterop2 = win32more.Security.EnterpriseData.IProtectionPolicyManagerInterop2_head
    IProtectionPolicyManagerInterop2.RequestAccessForAppWithWindowAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,POINTER(Guid),POINTER(c_void_p))(6, 'RequestAccessForAppWithWindowAsync', ((1, 'appWindow'),(1, 'sourceIdentity'),(1, 'appPackageFamilyName'),(1, 'riid'),(1, 'asyncOperation'),)))
    IProtectionPolicyManagerInterop2.RequestAccessWithAuditingInfoForWindowAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,win32more.System.Com.IUnknown_head,POINTER(Guid),POINTER(c_void_p))(7, 'RequestAccessWithAuditingInfoForWindowAsync', ((1, 'appWindow'),(1, 'sourceIdentity'),(1, 'targetIdentity'),(1, 'auditInfoUnk'),(1, 'riid'),(1, 'asyncOperation'),)))
    IProtectionPolicyManagerInterop2.RequestAccessWithMessageForWindowAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,win32more.System.Com.IUnknown_head,win32more.System.WinRT.HSTRING,POINTER(Guid),POINTER(c_void_p))(8, 'RequestAccessWithMessageForWindowAsync', ((1, 'appWindow'),(1, 'sourceIdentity'),(1, 'targetIdentity'),(1, 'auditInfoUnk'),(1, 'messageFromApp'),(1, 'riid'),(1, 'asyncOperation'),)))
    IProtectionPolicyManagerInterop2.RequestAccessForAppWithAuditingInfoForWindowAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,win32more.System.Com.IUnknown_head,POINTER(Guid),POINTER(c_void_p))(9, 'RequestAccessForAppWithAuditingInfoForWindowAsync', ((1, 'appWindow'),(1, 'sourceIdentity'),(1, 'appPackageFamilyName'),(1, 'auditInfoUnk'),(1, 'riid'),(1, 'asyncOperation'),)))
    IProtectionPolicyManagerInterop2.RequestAccessForAppWithMessageForWindowAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,win32more.System.Com.IUnknown_head,win32more.System.WinRT.HSTRING,POINTER(Guid),POINTER(c_void_p))(10, 'RequestAccessForAppWithMessageForWindowAsync', ((1, 'appWindow'),(1, 'sourceIdentity'),(1, 'appPackageFamilyName'),(1, 'auditInfoUnk'),(1, 'messageFromApp'),(1, 'riid'),(1, 'asyncOperation'),)))
    win32more.System.WinRT.IInspectable
    return IProtectionPolicyManagerInterop2
def _define_IProtectionPolicyManagerInterop3_head():
    class IProtectionPolicyManagerInterop3(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('c1c03933-b398-4d93-b0-fd-29-72-ad-f8-02-c2')
    return IProtectionPolicyManagerInterop3
def _define_IProtectionPolicyManagerInterop3():
    IProtectionPolicyManagerInterop3 = win32more.Security.EnterpriseData.IProtectionPolicyManagerInterop3_head
    IProtectionPolicyManagerInterop3.RequestAccessWithBehaviorForWindowAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,win32more.System.Com.IUnknown_head,win32more.System.WinRT.HSTRING,UInt32,POINTER(Guid),POINTER(c_void_p))(6, 'RequestAccessWithBehaviorForWindowAsync', ((1, 'appWindow'),(1, 'sourceIdentity'),(1, 'targetIdentity'),(1, 'auditInfoUnk'),(1, 'messageFromApp'),(1, 'behavior'),(1, 'riid'),(1, 'asyncOperation'),)))
    IProtectionPolicyManagerInterop3.RequestAccessForAppWithBehaviorForWindowAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,win32more.System.Com.IUnknown_head,win32more.System.WinRT.HSTRING,UInt32,POINTER(Guid),POINTER(c_void_p))(7, 'RequestAccessForAppWithBehaviorForWindowAsync', ((1, 'appWindow'),(1, 'sourceIdentity'),(1, 'appPackageFamilyName'),(1, 'auditInfoUnk'),(1, 'messageFromApp'),(1, 'behavior'),(1, 'riid'),(1, 'asyncOperation'),)))
    IProtectionPolicyManagerInterop3.RequestAccessToFilesForAppForWindowAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.System.Com.IUnknown_head,win32more.System.WinRT.HSTRING,win32more.System.Com.IUnknown_head,POINTER(Guid),POINTER(c_void_p))(8, 'RequestAccessToFilesForAppForWindowAsync', ((1, 'appWindow'),(1, 'sourceItemListUnk'),(1, 'appPackageFamilyName'),(1, 'auditInfoUnk'),(1, 'riid'),(1, 'asyncOperation'),)))
    IProtectionPolicyManagerInterop3.RequestAccessToFilesForAppWithMessageAndBehaviorForWindowAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.System.Com.IUnknown_head,win32more.System.WinRT.HSTRING,win32more.System.Com.IUnknown_head,win32more.System.WinRT.HSTRING,UInt32,POINTER(Guid),POINTER(c_void_p))(9, 'RequestAccessToFilesForAppWithMessageAndBehaviorForWindowAsync', ((1, 'appWindow'),(1, 'sourceItemListUnk'),(1, 'appPackageFamilyName'),(1, 'auditInfoUnk'),(1, 'messageFromApp'),(1, 'behavior'),(1, 'riid'),(1, 'asyncOperation'),)))
    IProtectionPolicyManagerInterop3.RequestAccessToFilesForProcessForWindowAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.System.Com.IUnknown_head,UInt32,win32more.System.Com.IUnknown_head,POINTER(Guid),POINTER(c_void_p))(10, 'RequestAccessToFilesForProcessForWindowAsync', ((1, 'appWindow'),(1, 'sourceItemListUnk'),(1, 'processId'),(1, 'auditInfoUnk'),(1, 'riid'),(1, 'asyncOperation'),)))
    IProtectionPolicyManagerInterop3.RequestAccessToFilesForProcessWithMessageAndBehaviorForWindowAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.System.Com.IUnknown_head,UInt32,win32more.System.Com.IUnknown_head,win32more.System.WinRT.HSTRING,UInt32,POINTER(Guid),POINTER(c_void_p))(11, 'RequestAccessToFilesForProcessWithMessageAndBehaviorForWindowAsync', ((1, 'appWindow'),(1, 'sourceItemListUnk'),(1, 'processId'),(1, 'auditInfoUnk'),(1, 'messageFromApp'),(1, 'behavior'),(1, 'riid'),(1, 'asyncOperation'),)))
    win32more.System.WinRT.IInspectable
    return IProtectionPolicyManagerInterop3
SRPHOSTING_TYPE = Int32
SRPHOSTING_TYPE_NONE = 0
SRPHOSTING_TYPE_WINHTTP = 1
SRPHOSTING_TYPE_WININET = 2
SRPHOSTING_VERSION = Int32
SRPHOSTING_VERSION1 = 1
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
