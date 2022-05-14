from win32more import *
import win32more.System.SecurityCenter
import win32more.Foundation
import win32more.System.Com
import win32more.System.Threading

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.System.SecurityCenter, name, eval(f"_define_{name}()"))
    return getattr(win32more.System.SecurityCenter, name)
WSCProductList = Guid('17072f7b-9abe-4a74-a261-1eb76b55107a')
WSCDefaultProduct = Guid('2981a36e-f22d-11e5-9ce9-5e5517507c66')
WSC_SECURITY_PRODUCT_SUBSTATUS = Int32
WSC_SECURITY_PRODUCT_SUBSTATUS_NOT_SET = 0
WSC_SECURITY_PRODUCT_SUBSTATUS_NO_ACTION = 1
WSC_SECURITY_PRODUCT_SUBSTATUS_ACTION_RECOMMENDED = 2
WSC_SECURITY_PRODUCT_SUBSTATUS_ACTION_NEEDED = 3
WSC_SECURITY_PRODUCT_STATE = Int32
WSC_SECURITY_PRODUCT_STATE_ON = 0
WSC_SECURITY_PRODUCT_STATE_OFF = 1
WSC_SECURITY_PRODUCT_STATE_SNOOZED = 2
WSC_SECURITY_PRODUCT_STATE_EXPIRED = 3
SECURITY_PRODUCT_TYPE = Int32
SECURITY_PRODUCT_TYPE_ANTIVIRUS = 0
SECURITY_PRODUCT_TYPE_FIREWALL = 1
SECURITY_PRODUCT_TYPE_ANTISPYWARE = 2
WSC_SECURITY_SIGNATURE_STATUS = Int32
WSC_SECURITY_PRODUCT_OUT_OF_DATE = 0
WSC_SECURITY_PRODUCT_UP_TO_DATE = 1
def _define_IWscProduct_head():
    class IWscProduct(win32more.System.Com.IDispatch_head):
        Guid = Guid('8c38232e-3a45-4a27-92b0-1a16a975f669')
    return IWscProduct
def _define_IWscProduct():
    IWscProduct = win32more.System.SecurityCenter.IWscProduct_head
    IWscProduct.get_ProductName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_ProductName', ((1, 'pVal'),)))
    IWscProduct.get_ProductState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.SecurityCenter.WSC_SECURITY_PRODUCT_STATE), use_last_error=False)(8, 'get_ProductState', ((1, 'pVal'),)))
    IWscProduct.get_SignatureStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.SecurityCenter.WSC_SECURITY_SIGNATURE_STATUS), use_last_error=False)(9, 'get_SignatureStatus', ((1, 'pVal'),)))
    IWscProduct.get_RemediationPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'get_RemediationPath', ((1, 'pVal'),)))
    IWscProduct.get_ProductStateTimestamp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'get_ProductStateTimestamp', ((1, 'pVal'),)))
    IWscProduct.get_ProductGuid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(12, 'get_ProductGuid', ((1, 'pVal'),)))
    IWscProduct.get_ProductIsDefault = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(13, 'get_ProductIsDefault', ((1, 'pVal'),)))
    return IWscProduct
def _define_IWscProduct2_head():
    class IWscProduct2(win32more.System.SecurityCenter.IWscProduct_head):
        Guid = Guid('f896ca54-fe09-4403-86d4-23cb488d81d8')
    return IWscProduct2
def _define_IWscProduct2():
    IWscProduct2 = win32more.System.SecurityCenter.IWscProduct2_head
    IWscProduct2.get_AntivirusScanSubstatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.SecurityCenter.WSC_SECURITY_PRODUCT_SUBSTATUS), use_last_error=False)(14, 'get_AntivirusScanSubstatus', ((1, 'peStatus'),)))
    IWscProduct2.get_AntivirusSettingsSubstatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.SecurityCenter.WSC_SECURITY_PRODUCT_SUBSTATUS), use_last_error=False)(15, 'get_AntivirusSettingsSubstatus', ((1, 'peStatus'),)))
    IWscProduct2.get_AntivirusProtectionUpdateSubstatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.SecurityCenter.WSC_SECURITY_PRODUCT_SUBSTATUS), use_last_error=False)(16, 'get_AntivirusProtectionUpdateSubstatus', ((1, 'peStatus'),)))
    IWscProduct2.get_FirewallDomainProfileSubstatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.SecurityCenter.WSC_SECURITY_PRODUCT_SUBSTATUS), use_last_error=False)(17, 'get_FirewallDomainProfileSubstatus', ((1, 'peStatus'),)))
    IWscProduct2.get_FirewallPrivateProfileSubstatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.SecurityCenter.WSC_SECURITY_PRODUCT_SUBSTATUS), use_last_error=False)(18, 'get_FirewallPrivateProfileSubstatus', ((1, 'peStatus'),)))
    IWscProduct2.get_FirewallPublicProfileSubstatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.SecurityCenter.WSC_SECURITY_PRODUCT_SUBSTATUS), use_last_error=False)(19, 'get_FirewallPublicProfileSubstatus', ((1, 'peStatus'),)))
    return IWscProduct2
def _define_IWscProduct3_head():
    class IWscProduct3(win32more.System.SecurityCenter.IWscProduct2_head):
        Guid = Guid('55536524-d1d1-4726-8c7c-04996a1904e7')
    return IWscProduct3
def _define_IWscProduct3():
    IWscProduct3 = win32more.System.SecurityCenter.IWscProduct3_head
    IWscProduct3.get_AntivirusDaysUntilExpired = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(20, 'get_AntivirusDaysUntilExpired', ((1, 'pdwDays'),)))
    return IWscProduct3
def _define_IWSCProductList_head():
    class IWSCProductList(win32more.System.Com.IDispatch_head):
        Guid = Guid('722a338c-6e8e-4e72-ac27-1417fb0c81c2')
    return IWSCProductList
def _define_IWSCProductList():
    IWSCProductList = win32more.System.SecurityCenter.IWSCProductList_head
    IWSCProductList.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.SecurityCenter.WSC_SECURITY_PROVIDER, use_last_error=False)(7, 'Initialize', ((1, 'provider'),)))
    IWSCProductList.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_Count', ((1, 'pVal'),)))
    IWSCProductList.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.SecurityCenter.IWscProduct_head), use_last_error=False)(9, 'get_Item', ((1, 'index'),(1, 'pVal'),)))
    return IWSCProductList
def _define_IWSCDefaultProduct_head():
    class IWSCDefaultProduct(win32more.System.Com.IDispatch_head):
        Guid = Guid('0476d69c-f21a-11e5-9ce9-5e5517507c66')
    return IWSCDefaultProduct
def _define_IWSCDefaultProduct():
    IWSCDefaultProduct = win32more.System.SecurityCenter.IWSCDefaultProduct_head
    IWSCDefaultProduct.SetDefaultProduct = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.SecurityCenter.SECURITY_PRODUCT_TYPE,win32more.Foundation.BSTR, use_last_error=False)(7, 'SetDefaultProduct', ((1, 'eType'),(1, 'pGuid'),)))
    return IWSCDefaultProduct
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
def _define_WscRegisterForChanges():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Foundation.HANDLE),win32more.System.Threading.LPTHREAD_START_ROUTINE,c_void_p, use_last_error=False)(("WscRegisterForChanges", windll["WSCAPI"]), ((1, 'Reserved'),(1, 'phCallbackRegistration'),(1, 'lpCallbackAddress'),(1, 'pContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WscUnRegisterChanges():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE, use_last_error=False)(("WscUnRegisterChanges", windll["WSCAPI"]), ((1, 'hRegistrationHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WscRegisterForUserNotifications():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(("WscRegisterForUserNotifications", windll["WSCAPI"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_WscGetSecurityProviderHealth():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.SecurityCenter.WSC_SECURITY_PROVIDER_HEALTH), use_last_error=False)(("WscGetSecurityProviderHealth", windll["WSCAPI"]), ((1, 'Providers'),(1, 'pHealth'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WscQueryAntiMalwareUri():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(("WscQueryAntiMalwareUri", windll["WSCAPI"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_WscGetAntiMalwareUri():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("WscGetAntiMalwareUri", windll["WSCAPI"]), ((1, 'ppszUri'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "WSCProductList",
    "WSCDefaultProduct",
    "WSC_SECURITY_PRODUCT_SUBSTATUS",
    "WSC_SECURITY_PRODUCT_SUBSTATUS_NOT_SET",
    "WSC_SECURITY_PRODUCT_SUBSTATUS_NO_ACTION",
    "WSC_SECURITY_PRODUCT_SUBSTATUS_ACTION_RECOMMENDED",
    "WSC_SECURITY_PRODUCT_SUBSTATUS_ACTION_NEEDED",
    "WSC_SECURITY_PRODUCT_STATE",
    "WSC_SECURITY_PRODUCT_STATE_ON",
    "WSC_SECURITY_PRODUCT_STATE_OFF",
    "WSC_SECURITY_PRODUCT_STATE_SNOOZED",
    "WSC_SECURITY_PRODUCT_STATE_EXPIRED",
    "SECURITY_PRODUCT_TYPE",
    "SECURITY_PRODUCT_TYPE_ANTIVIRUS",
    "SECURITY_PRODUCT_TYPE_FIREWALL",
    "SECURITY_PRODUCT_TYPE_ANTISPYWARE",
    "WSC_SECURITY_SIGNATURE_STATUS",
    "WSC_SECURITY_PRODUCT_OUT_OF_DATE",
    "WSC_SECURITY_PRODUCT_UP_TO_DATE",
    "IWscProduct",
    "IWscProduct2",
    "IWscProduct3",
    "IWSCProductList",
    "IWSCDefaultProduct",
    "WSC_SECURITY_PROVIDER",
    "WSC_SECURITY_PROVIDER_FIREWALL",
    "WSC_SECURITY_PROVIDER_AUTOUPDATE_SETTINGS",
    "WSC_SECURITY_PROVIDER_ANTIVIRUS",
    "WSC_SECURITY_PROVIDER_ANTISPYWARE",
    "WSC_SECURITY_PROVIDER_INTERNET_SETTINGS",
    "WSC_SECURITY_PROVIDER_USER_ACCOUNT_CONTROL",
    "WSC_SECURITY_PROVIDER_SERVICE",
    "WSC_SECURITY_PROVIDER_NONE",
    "WSC_SECURITY_PROVIDER_ALL",
    "WSC_SECURITY_PROVIDER_HEALTH",
    "WSC_SECURITY_PROVIDER_HEALTH_GOOD",
    "WSC_SECURITY_PROVIDER_HEALTH_NOTMONITORED",
    "WSC_SECURITY_PROVIDER_HEALTH_POOR",
    "WSC_SECURITY_PROVIDER_HEALTH_SNOOZE",
    "WscRegisterForChanges",
    "WscUnRegisterChanges",
    "WscRegisterForUserNotifications",
    "WscGetSecurityProviderHealth",
    "WscQueryAntiMalwareUri",
    "WscGetAntiMalwareUri",
]
