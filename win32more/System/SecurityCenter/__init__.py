from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.System.Com
import win32more.System.SecurityCenter
import win32more.System.Threading
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        if name in _arch_optional:
            return None
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
@winfunctype('WSCAPI.dll')
def WscRegisterForChanges(Reserved: c_void_p, phCallbackRegistration: POINTER(win32more.Foundation.HANDLE), lpCallbackAddress: win32more.System.Threading.LPTHREAD_START_ROUTINE, pContext: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('WSCAPI.dll')
def WscUnRegisterChanges(hRegistrationHandle: win32more.Foundation.HANDLE) -> win32more.Foundation.HRESULT: ...
@winfunctype('WSCAPI.dll')
def WscRegisterForUserNotifications() -> win32more.Foundation.HRESULT: ...
@winfunctype('WSCAPI.dll')
def WscGetSecurityProviderHealth(Providers: UInt32, pHealth: POINTER(win32more.System.SecurityCenter.WSC_SECURITY_PROVIDER_HEALTH)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WSCAPI.dll')
def WscQueryAntiMalwareUri() -> win32more.Foundation.HRESULT: ...
@winfunctype('WSCAPI.dll')
def WscGetAntiMalwareUri(ppszUri: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
class IWSCDefaultProduct(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('0476d69c-f21a-11e5-9c-e9-5e-55-17-50-7c-66')
    @commethod(7)
    def SetDefaultProduct(eType: win32more.System.SecurityCenter.SECURITY_PRODUCT_TYPE, pGuid: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class IWSCProductList(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('722a338c-6e8e-4e72-ac-27-14-17-fb-0c-81-c2')
    @commethod(7)
    def Initialize(provider: win32more.System.SecurityCenter.WSC_SECURITY_PROVIDER) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Count(pVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Item(index: UInt32, pVal: POINTER(win32more.System.SecurityCenter.IWscProduct_head)) -> win32more.Foundation.HRESULT: ...
class IWscProduct(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('8c38232e-3a45-4a27-92-b0-1a-16-a9-75-f6-69')
    @commethod(7)
    def get_ProductName(pVal: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_ProductState(pVal: POINTER(win32more.System.SecurityCenter.WSC_SECURITY_PRODUCT_STATE)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_SignatureStatus(pVal: POINTER(win32more.System.SecurityCenter.WSC_SECURITY_SIGNATURE_STATUS)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_RemediationPath(pVal: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_ProductStateTimestamp(pVal: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_ProductGuid(pVal: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_ProductIsDefault(pVal: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
class IWscProduct2(c_void_p):
    extends: win32more.System.SecurityCenter.IWscProduct
    Guid = Guid('f896ca54-fe09-4403-86-d4-23-cb-48-8d-81-d8')
    @commethod(14)
    def get_AntivirusScanSubstatus(peStatus: POINTER(win32more.System.SecurityCenter.WSC_SECURITY_PRODUCT_SUBSTATUS)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_AntivirusSettingsSubstatus(peStatus: POINTER(win32more.System.SecurityCenter.WSC_SECURITY_PRODUCT_SUBSTATUS)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_AntivirusProtectionUpdateSubstatus(peStatus: POINTER(win32more.System.SecurityCenter.WSC_SECURITY_PRODUCT_SUBSTATUS)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_FirewallDomainProfileSubstatus(peStatus: POINTER(win32more.System.SecurityCenter.WSC_SECURITY_PRODUCT_SUBSTATUS)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def get_FirewallPrivateProfileSubstatus(peStatus: POINTER(win32more.System.SecurityCenter.WSC_SECURITY_PRODUCT_SUBSTATUS)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get_FirewallPublicProfileSubstatus(peStatus: POINTER(win32more.System.SecurityCenter.WSC_SECURITY_PRODUCT_SUBSTATUS)) -> win32more.Foundation.HRESULT: ...
class IWscProduct3(c_void_p):
    extends: win32more.System.SecurityCenter.IWscProduct2
    Guid = Guid('55536524-d1d1-4726-8c-7c-04-99-6a-19-04-e7')
    @commethod(20)
    def get_AntivirusDaysUntilExpired(pdwDays: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
SECURITY_PRODUCT_TYPE = Int32
SECURITY_PRODUCT_TYPE_ANTIVIRUS: SECURITY_PRODUCT_TYPE = 0
SECURITY_PRODUCT_TYPE_FIREWALL: SECURITY_PRODUCT_TYPE = 1
SECURITY_PRODUCT_TYPE_ANTISPYWARE: SECURITY_PRODUCT_TYPE = 2
WSCDefaultProduct = Guid('2981a36e-f22d-11e5-9c-e9-5e-55-17-50-7c-66')
WSCProductList = Guid('17072f7b-9abe-4a74-a2-61-1e-b7-6b-55-10-7a')
WSC_SECURITY_PRODUCT_STATE = Int32
WSC_SECURITY_PRODUCT_STATE_ON: WSC_SECURITY_PRODUCT_STATE = 0
WSC_SECURITY_PRODUCT_STATE_OFF: WSC_SECURITY_PRODUCT_STATE = 1
WSC_SECURITY_PRODUCT_STATE_SNOOZED: WSC_SECURITY_PRODUCT_STATE = 2
WSC_SECURITY_PRODUCT_STATE_EXPIRED: WSC_SECURITY_PRODUCT_STATE = 3
WSC_SECURITY_PRODUCT_SUBSTATUS = Int32
WSC_SECURITY_PRODUCT_SUBSTATUS_NOT_SET: WSC_SECURITY_PRODUCT_SUBSTATUS = 0
WSC_SECURITY_PRODUCT_SUBSTATUS_NO_ACTION: WSC_SECURITY_PRODUCT_SUBSTATUS = 1
WSC_SECURITY_PRODUCT_SUBSTATUS_ACTION_RECOMMENDED: WSC_SECURITY_PRODUCT_SUBSTATUS = 2
WSC_SECURITY_PRODUCT_SUBSTATUS_ACTION_NEEDED: WSC_SECURITY_PRODUCT_SUBSTATUS = 3
WSC_SECURITY_PROVIDER = Int32
WSC_SECURITY_PROVIDER_FIREWALL: WSC_SECURITY_PROVIDER = 1
WSC_SECURITY_PROVIDER_AUTOUPDATE_SETTINGS: WSC_SECURITY_PROVIDER = 2
WSC_SECURITY_PROVIDER_ANTIVIRUS: WSC_SECURITY_PROVIDER = 4
WSC_SECURITY_PROVIDER_ANTISPYWARE: WSC_SECURITY_PROVIDER = 8
WSC_SECURITY_PROVIDER_INTERNET_SETTINGS: WSC_SECURITY_PROVIDER = 16
WSC_SECURITY_PROVIDER_USER_ACCOUNT_CONTROL: WSC_SECURITY_PROVIDER = 32
WSC_SECURITY_PROVIDER_SERVICE: WSC_SECURITY_PROVIDER = 64
WSC_SECURITY_PROVIDER_NONE: WSC_SECURITY_PROVIDER = 0
WSC_SECURITY_PROVIDER_ALL: WSC_SECURITY_PROVIDER = 127
WSC_SECURITY_PROVIDER_HEALTH = Int32
WSC_SECURITY_PROVIDER_HEALTH_GOOD: WSC_SECURITY_PROVIDER_HEALTH = 0
WSC_SECURITY_PROVIDER_HEALTH_NOTMONITORED: WSC_SECURITY_PROVIDER_HEALTH = 1
WSC_SECURITY_PROVIDER_HEALTH_POOR: WSC_SECURITY_PROVIDER_HEALTH = 2
WSC_SECURITY_PROVIDER_HEALTH_SNOOZE: WSC_SECURITY_PROVIDER_HEALTH = 3
WSC_SECURITY_SIGNATURE_STATUS = Int32
WSC_SECURITY_PRODUCT_OUT_OF_DATE: WSC_SECURITY_SIGNATURE_STATUS = 0
WSC_SECURITY_PRODUCT_UP_TO_DATE: WSC_SECURITY_SIGNATURE_STATUS = 1
make_head(_module, 'IWSCDefaultProduct')
make_head(_module, 'IWSCProductList')
make_head(_module, 'IWscProduct')
make_head(_module, 'IWscProduct2')
make_head(_module, 'IWscProduct3')
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
_arch_optional = [
]
