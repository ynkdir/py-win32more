from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.System.Com
import Windows.Win32.System.SecurityCenter
import Windows.Win32.System.Threading
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
@winfunctype('WSCAPI.dll')
def WscRegisterForChanges(Reserved: c_void_p, phCallbackRegistration: POINTER(Windows.Win32.Foundation.HANDLE), lpCallbackAddress: Windows.Win32.System.Threading.LPTHREAD_START_ROUTINE, pContext: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WSCAPI.dll')
def WscUnRegisterChanges(hRegistrationHandle: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WSCAPI.dll')
def WscRegisterForUserNotifications() -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WSCAPI.dll')
def WscGetSecurityProviderHealth(Providers: UInt32, pHealth: POINTER(Windows.Win32.System.SecurityCenter.WSC_SECURITY_PROVIDER_HEALTH)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WSCAPI.dll')
def WscQueryAntiMalwareUri() -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WSCAPI.dll')
def WscGetAntiMalwareUri(ppszUri: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IWSCDefaultProduct(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('0476d69c-f21a-11e5-9c-e9-5e-55-17-50-7c-66')
    @commethod(7)
    def SetDefaultProduct(self, eType: Windows.Win32.System.SecurityCenter.SECURITY_PRODUCT_TYPE, pGuid: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IWSCProductList(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('722a338c-6e8e-4e72-ac-27-14-17-fb-0c-81-c2')
    @commethod(7)
    def Initialize(self, provider: Windows.Win32.System.SecurityCenter.WSC_SECURITY_PROVIDER) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Count(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Item(self, index: UInt32, pVal: POINTER(Windows.Win32.System.SecurityCenter.IWscProduct_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWscProduct(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('8c38232e-3a45-4a27-92-b0-1a-16-a9-75-f6-69')
    @commethod(7)
    def get_ProductName(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_ProductState(self, pVal: POINTER(Windows.Win32.System.SecurityCenter.WSC_SECURITY_PRODUCT_STATE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_SignatureStatus(self, pVal: POINTER(Windows.Win32.System.SecurityCenter.WSC_SECURITY_SIGNATURE_STATUS)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_RemediationPath(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_ProductStateTimestamp(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_ProductGuid(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_ProductIsDefault(self, pVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IWscProduct2(ComPtr):
    extends: Windows.Win32.System.SecurityCenter.IWscProduct
    Guid = Guid('f896ca54-fe09-4403-86-d4-23-cb-48-8d-81-d8')
    @commethod(14)
    def get_AntivirusScanSubstatus(self, peStatus: POINTER(Windows.Win32.System.SecurityCenter.WSC_SECURITY_PRODUCT_SUBSTATUS)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_AntivirusSettingsSubstatus(self, peStatus: POINTER(Windows.Win32.System.SecurityCenter.WSC_SECURITY_PRODUCT_SUBSTATUS)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_AntivirusProtectionUpdateSubstatus(self, peStatus: POINTER(Windows.Win32.System.SecurityCenter.WSC_SECURITY_PRODUCT_SUBSTATUS)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_FirewallDomainProfileSubstatus(self, peStatus: POINTER(Windows.Win32.System.SecurityCenter.WSC_SECURITY_PRODUCT_SUBSTATUS)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_FirewallPrivateProfileSubstatus(self, peStatus: POINTER(Windows.Win32.System.SecurityCenter.WSC_SECURITY_PRODUCT_SUBSTATUS)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_FirewallPublicProfileSubstatus(self, peStatus: POINTER(Windows.Win32.System.SecurityCenter.WSC_SECURITY_PRODUCT_SUBSTATUS)) -> Windows.Win32.Foundation.HRESULT: ...
class IWscProduct3(ComPtr):
    extends: Windows.Win32.System.SecurityCenter.IWscProduct2
    Guid = Guid('55536524-d1d1-4726-8c-7c-04-99-6a-19-04-e7')
    @commethod(20)
    def get_AntivirusDaysUntilExpired(self, pdwDays: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
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
