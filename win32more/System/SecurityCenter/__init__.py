from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.Com
import win32more.System.SecurityCenter
import win32more.System.Threading
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
def _define_WscRegisterForChanges():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Foundation.HANDLE),win32more.System.Threading.LPTHREAD_START_ROUTINE,c_void_p)(('WscRegisterForChanges', windll['WSCAPI.dll']), ((1, 'Reserved'),(1, 'phCallbackRegistration'),(1, 'lpCallbackAddress'),(1, 'pContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WscUnRegisterChanges():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE)(('WscUnRegisterChanges', windll['WSCAPI.dll']), ((1, 'hRegistrationHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WscRegisterForUserNotifications():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,)(('WscRegisterForUserNotifications', windll['WSCAPI.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_WscGetSecurityProviderHealth():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.SecurityCenter.WSC_SECURITY_PROVIDER_HEALTH))(('WscGetSecurityProviderHealth', windll['WSCAPI.dll']), ((1, 'Providers'),(1, 'pHealth'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WscQueryAntiMalwareUri():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,)(('WscQueryAntiMalwareUri', windll['WSCAPI.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_WscGetAntiMalwareUri():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(('WscGetAntiMalwareUri', windll['WSCAPI.dll']), ((1, 'ppszUri'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IWSCDefaultProduct_head():
    class IWSCDefaultProduct(win32more.System.Com.IDispatch_head):
        Guid = Guid('0476d69c-f21a-11e5-9c-e9-5e-55-17-50-7c-66')
    return IWSCDefaultProduct
def _define_IWSCDefaultProduct():
    IWSCDefaultProduct = win32more.System.SecurityCenter.IWSCDefaultProduct_head
    IWSCDefaultProduct.SetDefaultProduct = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.SecurityCenter.SECURITY_PRODUCT_TYPE,win32more.Foundation.BSTR)(7, 'SetDefaultProduct', ((1, 'eType'),(1, 'pGuid'),)))
    win32more.System.Com.IDispatch
    return IWSCDefaultProduct
def _define_IWscProduct_head():
    class IWscProduct(win32more.System.Com.IDispatch_head):
        Guid = Guid('8c38232e-3a45-4a27-92-b0-1a-16-a9-75-f6-69')
    return IWscProduct
def _define_IWscProduct():
    IWscProduct = win32more.System.SecurityCenter.IWscProduct_head
    IWscProduct.get_ProductName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_ProductName', ((1, 'pVal'),)))
    IWscProduct.get_ProductState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.SecurityCenter.WSC_SECURITY_PRODUCT_STATE))(8, 'get_ProductState', ((1, 'pVal'),)))
    IWscProduct.get_SignatureStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.SecurityCenter.WSC_SECURITY_SIGNATURE_STATUS))(9, 'get_SignatureStatus', ((1, 'pVal'),)))
    IWscProduct.get_RemediationPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(10, 'get_RemediationPath', ((1, 'pVal'),)))
    IWscProduct.get_ProductStateTimestamp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(11, 'get_ProductStateTimestamp', ((1, 'pVal'),)))
    IWscProduct.get_ProductGuid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(12, 'get_ProductGuid', ((1, 'pVal'),)))
    IWscProduct.get_ProductIsDefault = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(13, 'get_ProductIsDefault', ((1, 'pVal'),)))
    win32more.System.Com.IDispatch
    return IWscProduct
def _define_IWscProduct2_head():
    class IWscProduct2(win32more.System.SecurityCenter.IWscProduct_head):
        Guid = Guid('f896ca54-fe09-4403-86-d4-23-cb-48-8d-81-d8')
    return IWscProduct2
def _define_IWscProduct2():
    IWscProduct2 = win32more.System.SecurityCenter.IWscProduct2_head
    IWscProduct2.get_AntivirusScanSubstatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.SecurityCenter.WSC_SECURITY_PRODUCT_SUBSTATUS))(14, 'get_AntivirusScanSubstatus', ((1, 'peStatus'),)))
    IWscProduct2.get_AntivirusSettingsSubstatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.SecurityCenter.WSC_SECURITY_PRODUCT_SUBSTATUS))(15, 'get_AntivirusSettingsSubstatus', ((1, 'peStatus'),)))
    IWscProduct2.get_AntivirusProtectionUpdateSubstatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.SecurityCenter.WSC_SECURITY_PRODUCT_SUBSTATUS))(16, 'get_AntivirusProtectionUpdateSubstatus', ((1, 'peStatus'),)))
    IWscProduct2.get_FirewallDomainProfileSubstatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.SecurityCenter.WSC_SECURITY_PRODUCT_SUBSTATUS))(17, 'get_FirewallDomainProfileSubstatus', ((1, 'peStatus'),)))
    IWscProduct2.get_FirewallPrivateProfileSubstatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.SecurityCenter.WSC_SECURITY_PRODUCT_SUBSTATUS))(18, 'get_FirewallPrivateProfileSubstatus', ((1, 'peStatus'),)))
    IWscProduct2.get_FirewallPublicProfileSubstatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.SecurityCenter.WSC_SECURITY_PRODUCT_SUBSTATUS))(19, 'get_FirewallPublicProfileSubstatus', ((1, 'peStatus'),)))
    win32more.System.SecurityCenter.IWscProduct
    return IWscProduct2
def _define_IWscProduct3_head():
    class IWscProduct3(win32more.System.SecurityCenter.IWscProduct2_head):
        Guid = Guid('55536524-d1d1-4726-8c-7c-04-99-6a-19-04-e7')
    return IWscProduct3
def _define_IWscProduct3():
    IWscProduct3 = win32more.System.SecurityCenter.IWscProduct3_head
    IWscProduct3.get_AntivirusDaysUntilExpired = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(20, 'get_AntivirusDaysUntilExpired', ((1, 'pdwDays'),)))
    win32more.System.SecurityCenter.IWscProduct2
    return IWscProduct3
def _define_IWSCProductList_head():
    class IWSCProductList(win32more.System.Com.IDispatch_head):
        Guid = Guid('722a338c-6e8e-4e72-ac-27-14-17-fb-0c-81-c2')
    return IWSCProductList
def _define_IWSCProductList():
    IWSCProductList = win32more.System.SecurityCenter.IWSCProductList_head
    IWSCProductList.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.SecurityCenter.WSC_SECURITY_PROVIDER)(7, 'Initialize', ((1, 'provider'),)))
    IWSCProductList.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(8, 'get_Count', ((1, 'pVal'),)))
    IWSCProductList.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.SecurityCenter.IWscProduct_head))(9, 'get_Item', ((1, 'index'),(1, 'pVal'),)))
    win32more.System.Com.IDispatch
    return IWSCProductList
SECURITY_PRODUCT_TYPE = Int32
SECURITY_PRODUCT_TYPE_ANTIVIRUS = 0
SECURITY_PRODUCT_TYPE_FIREWALL = 1
SECURITY_PRODUCT_TYPE_ANTISPYWARE = 2
WSC_SECURITY_PRODUCT_STATE = Int32
WSC_SECURITY_PRODUCT_STATE_ON = 0
WSC_SECURITY_PRODUCT_STATE_OFF = 1
WSC_SECURITY_PRODUCT_STATE_SNOOZED = 2
WSC_SECURITY_PRODUCT_STATE_EXPIRED = 3
WSC_SECURITY_PRODUCT_SUBSTATUS = Int32
WSC_SECURITY_PRODUCT_SUBSTATUS_NOT_SET = 0
WSC_SECURITY_PRODUCT_SUBSTATUS_NO_ACTION = 1
WSC_SECURITY_PRODUCT_SUBSTATUS_ACTION_RECOMMENDED = 2
WSC_SECURITY_PRODUCT_SUBSTATUS_ACTION_NEEDED = 3
WSC_SECURITY_PROVIDER = Int32
WSC_SECURITY_PROVIDER_FIREWALL = 1
WSC_SECURITY_PROVIDER_AUTOUPDATE_SETTINGS = 2
WSC_SECURITY_PROVIDER_ANTIVIRUS = 4
WSC_SECURITY_PROVIDER_ANTISPYWARE = 8
WSC_SECURITY_PROVIDER_INTERNET_SETTINGS = 16
WSC_SECURITY_PROVIDER_USER_ACCOUNT_CONTROL = 32
WSC_SECURITY_PROVIDER_SERVICE = 64
WSC_SECURITY_PROVIDER_NONE = 0
WSC_SECURITY_PROVIDER_ALL = 127
WSC_SECURITY_PROVIDER_HEALTH = Int32
WSC_SECURITY_PROVIDER_HEALTH_GOOD = 0
WSC_SECURITY_PROVIDER_HEALTH_NOTMONITORED = 1
WSC_SECURITY_PROVIDER_HEALTH_POOR = 2
WSC_SECURITY_PROVIDER_HEALTH_SNOOZE = 3
WSC_SECURITY_SIGNATURE_STATUS = Int32
WSC_SECURITY_PRODUCT_OUT_OF_DATE = 0
WSC_SECURITY_PRODUCT_UP_TO_DATE = 1
WSCDefaultProduct = Guid('2981a36e-f22d-11e5-9c-e9-5e-55-17-50-7c-66')
WSCProductList = Guid('17072f7b-9abe-4a74-a2-61-1e-b7-6b-55-10-7a')
__all__ = [
    "IWSCDefaultProduct",
    "IWSCProductList",
    "IWscProduct",
    "IWscProduct2",
    "IWscProduct3",
    "SECURITY_PRODUCT_TYPE",
    "SECURITY_PRODUCT_TYPE_ANTISPYWARE",
    "SECURITY_PRODUCT_TYPE_ANTIVIRUS",
    "SECURITY_PRODUCT_TYPE_FIREWALL",
    "WSCDefaultProduct",
    "WSCProductList",
    "WSC_SECURITY_PRODUCT_OUT_OF_DATE",
    "WSC_SECURITY_PRODUCT_STATE",
    "WSC_SECURITY_PRODUCT_STATE_EXPIRED",
    "WSC_SECURITY_PRODUCT_STATE_OFF",
    "WSC_SECURITY_PRODUCT_STATE_ON",
    "WSC_SECURITY_PRODUCT_STATE_SNOOZED",
    "WSC_SECURITY_PRODUCT_SUBSTATUS",
    "WSC_SECURITY_PRODUCT_SUBSTATUS_ACTION_NEEDED",
    "WSC_SECURITY_PRODUCT_SUBSTATUS_ACTION_RECOMMENDED",
    "WSC_SECURITY_PRODUCT_SUBSTATUS_NOT_SET",
    "WSC_SECURITY_PRODUCT_SUBSTATUS_NO_ACTION",
    "WSC_SECURITY_PRODUCT_UP_TO_DATE",
    "WSC_SECURITY_PROVIDER",
    "WSC_SECURITY_PROVIDER_ALL",
    "WSC_SECURITY_PROVIDER_ANTISPYWARE",
    "WSC_SECURITY_PROVIDER_ANTIVIRUS",
    "WSC_SECURITY_PROVIDER_AUTOUPDATE_SETTINGS",
    "WSC_SECURITY_PROVIDER_FIREWALL",
    "WSC_SECURITY_PROVIDER_HEALTH",
    "WSC_SECURITY_PROVIDER_HEALTH_GOOD",
    "WSC_SECURITY_PROVIDER_HEALTH_NOTMONITORED",
    "WSC_SECURITY_PROVIDER_HEALTH_POOR",
    "WSC_SECURITY_PROVIDER_HEALTH_SNOOZE",
    "WSC_SECURITY_PROVIDER_INTERNET_SETTINGS",
    "WSC_SECURITY_PROVIDER_NONE",
    "WSC_SECURITY_PROVIDER_SERVICE",
    "WSC_SECURITY_PROVIDER_USER_ACCOUNT_CONTROL",
    "WSC_SECURITY_SIGNATURE_STATUS",
    "WscGetAntiMalwareUri",
    "WscGetSecurityProviderHealth",
    "WscQueryAntiMalwareUri",
    "WscRegisterForChanges",
    "WscRegisterForUserNotifications",
    "WscUnRegisterChanges",
]
