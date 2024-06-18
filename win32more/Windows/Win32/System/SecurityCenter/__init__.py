from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.SecurityCenter
import win32more.Windows.Win32.System.Threading
@winfunctype('WSCAPI.dll')
def WscRegisterForChanges(Reserved: VoidPtr, phCallbackRegistration: POINTER(win32more.Windows.Win32.Foundation.HANDLE), lpCallbackAddress: win32more.Windows.Win32.System.Threading.LPTHREAD_START_ROUTINE, pContext: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WSCAPI.dll')
def WscUnRegisterChanges(hRegistrationHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WSCAPI.dll')
def WscRegisterForUserNotifications() -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WSCAPI.dll')
def WscGetSecurityProviderHealth(Providers: UInt32, pHealth: POINTER(win32more.Windows.Win32.System.SecurityCenter.WSC_SECURITY_PROVIDER_HEALTH)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WSCAPI.dll')
def WscQueryAntiMalwareUri() -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WSCAPI.dll')
def WscGetAntiMalwareUri(ppszUri: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWSCDefaultProduct(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{0476d69c-f21a-11e5-9ce9-5e5517507c66}')
    @commethod(7)
    def SetDefaultProduct(self, eType: win32more.Windows.Win32.System.SecurityCenter.SECURITY_PRODUCT_TYPE, pGuid: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWSCProductList(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{722a338c-6e8e-4e72-ac27-1417fb0c81c2}')
    @commethod(7)
    def Initialize(self, provider: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Count(self, pVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Item(self, index: UInt32, pVal: POINTER(win32more.Windows.Win32.System.SecurityCenter.IWscProduct)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWscProduct(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{8c38232e-3a45-4a27-92b0-1a16a975f669}')
    @commethod(7)
    def get_ProductName(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_ProductState(self, pVal: POINTER(win32more.Windows.Win32.System.SecurityCenter.WSC_SECURITY_PRODUCT_STATE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_SignatureStatus(self, pVal: POINTER(win32more.Windows.Win32.System.SecurityCenter.WSC_SECURITY_SIGNATURE_STATUS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_RemediationPath(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_ProductStateTimestamp(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_ProductGuid(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_ProductIsDefault(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWscProduct2(ComPtr):
    extends: win32more.Windows.Win32.System.SecurityCenter.IWscProduct
    _iid_ = Guid('{f896ca54-fe09-4403-86d4-23cb488d81d8}')
    @commethod(14)
    def get_AntivirusScanSubstatus(self, peStatus: POINTER(win32more.Windows.Win32.System.SecurityCenter.WSC_SECURITY_PRODUCT_SUBSTATUS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_AntivirusSettingsSubstatus(self, peStatus: POINTER(win32more.Windows.Win32.System.SecurityCenter.WSC_SECURITY_PRODUCT_SUBSTATUS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_AntivirusProtectionUpdateSubstatus(self, peStatus: POINTER(win32more.Windows.Win32.System.SecurityCenter.WSC_SECURITY_PRODUCT_SUBSTATUS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_FirewallDomainProfileSubstatus(self, peStatus: POINTER(win32more.Windows.Win32.System.SecurityCenter.WSC_SECURITY_PRODUCT_SUBSTATUS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_FirewallPrivateProfileSubstatus(self, peStatus: POINTER(win32more.Windows.Win32.System.SecurityCenter.WSC_SECURITY_PRODUCT_SUBSTATUS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_FirewallPublicProfileSubstatus(self, peStatus: POINTER(win32more.Windows.Win32.System.SecurityCenter.WSC_SECURITY_PRODUCT_SUBSTATUS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWscProduct3(ComPtr):
    extends: win32more.Windows.Win32.System.SecurityCenter.IWscProduct2
    _iid_ = Guid('{55536524-d1d1-4726-8c7c-04996a1904e7}')
    @commethod(20)
    def get_AntivirusDaysUntilExpired(self, pdwDays: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
SECURITY_PRODUCT_TYPE = Int32
SECURITY_PRODUCT_TYPE_ANTIVIRUS: win32more.Windows.Win32.System.SecurityCenter.SECURITY_PRODUCT_TYPE = 0
SECURITY_PRODUCT_TYPE_FIREWALL: win32more.Windows.Win32.System.SecurityCenter.SECURITY_PRODUCT_TYPE = 1
SECURITY_PRODUCT_TYPE_ANTISPYWARE: win32more.Windows.Win32.System.SecurityCenter.SECURITY_PRODUCT_TYPE = 2
WSCDefaultProduct = Guid('{2981a36e-f22d-11e5-9ce9-5e5517507c66}')
WSCProductList = Guid('{17072f7b-9abe-4a74-a261-1eb76b55107a}')
WSC_SECURITY_PRODUCT_STATE = Int32
WSC_SECURITY_PRODUCT_STATE_ON: win32more.Windows.Win32.System.SecurityCenter.WSC_SECURITY_PRODUCT_STATE = 0
WSC_SECURITY_PRODUCT_STATE_OFF: win32more.Windows.Win32.System.SecurityCenter.WSC_SECURITY_PRODUCT_STATE = 1
WSC_SECURITY_PRODUCT_STATE_SNOOZED: win32more.Windows.Win32.System.SecurityCenter.WSC_SECURITY_PRODUCT_STATE = 2
WSC_SECURITY_PRODUCT_STATE_EXPIRED: win32more.Windows.Win32.System.SecurityCenter.WSC_SECURITY_PRODUCT_STATE = 3
WSC_SECURITY_PRODUCT_SUBSTATUS = Int32
WSC_SECURITY_PRODUCT_SUBSTATUS_NOT_SET: win32more.Windows.Win32.System.SecurityCenter.WSC_SECURITY_PRODUCT_SUBSTATUS = 0
WSC_SECURITY_PRODUCT_SUBSTATUS_NO_ACTION: win32more.Windows.Win32.System.SecurityCenter.WSC_SECURITY_PRODUCT_SUBSTATUS = 1
WSC_SECURITY_PRODUCT_SUBSTATUS_ACTION_RECOMMENDED: win32more.Windows.Win32.System.SecurityCenter.WSC_SECURITY_PRODUCT_SUBSTATUS = 2
WSC_SECURITY_PRODUCT_SUBSTATUS_ACTION_NEEDED: win32more.Windows.Win32.System.SecurityCenter.WSC_SECURITY_PRODUCT_SUBSTATUS = 3
WSC_SECURITY_PROVIDER = Int32
WSC_SECURITY_PROVIDER_FIREWALL: win32more.Windows.Win32.System.SecurityCenter.WSC_SECURITY_PROVIDER = 1
WSC_SECURITY_PROVIDER_AUTOUPDATE_SETTINGS: win32more.Windows.Win32.System.SecurityCenter.WSC_SECURITY_PROVIDER = 2
WSC_SECURITY_PROVIDER_ANTIVIRUS: win32more.Windows.Win32.System.SecurityCenter.WSC_SECURITY_PROVIDER = 4
WSC_SECURITY_PROVIDER_ANTISPYWARE: win32more.Windows.Win32.System.SecurityCenter.WSC_SECURITY_PROVIDER = 8
WSC_SECURITY_PROVIDER_INTERNET_SETTINGS: win32more.Windows.Win32.System.SecurityCenter.WSC_SECURITY_PROVIDER = 16
WSC_SECURITY_PROVIDER_USER_ACCOUNT_CONTROL: win32more.Windows.Win32.System.SecurityCenter.WSC_SECURITY_PROVIDER = 32
WSC_SECURITY_PROVIDER_SERVICE: win32more.Windows.Win32.System.SecurityCenter.WSC_SECURITY_PROVIDER = 64
WSC_SECURITY_PROVIDER_NONE: win32more.Windows.Win32.System.SecurityCenter.WSC_SECURITY_PROVIDER = 0
WSC_SECURITY_PROVIDER_ALL: win32more.Windows.Win32.System.SecurityCenter.WSC_SECURITY_PROVIDER = 127
WSC_SECURITY_PROVIDER_HEALTH = Int32
WSC_SECURITY_PROVIDER_HEALTH_GOOD: win32more.Windows.Win32.System.SecurityCenter.WSC_SECURITY_PROVIDER_HEALTH = 0
WSC_SECURITY_PROVIDER_HEALTH_NOTMONITORED: win32more.Windows.Win32.System.SecurityCenter.WSC_SECURITY_PROVIDER_HEALTH = 1
WSC_SECURITY_PROVIDER_HEALTH_POOR: win32more.Windows.Win32.System.SecurityCenter.WSC_SECURITY_PROVIDER_HEALTH = 2
WSC_SECURITY_PROVIDER_HEALTH_SNOOZE: win32more.Windows.Win32.System.SecurityCenter.WSC_SECURITY_PROVIDER_HEALTH = 3
WSC_SECURITY_SIGNATURE_STATUS = Int32
WSC_SECURITY_PRODUCT_OUT_OF_DATE: win32more.Windows.Win32.System.SecurityCenter.WSC_SECURITY_SIGNATURE_STATUS = 0
WSC_SECURITY_PRODUCT_UP_TO_DATE: win32more.Windows.Win32.System.SecurityCenter.WSC_SECURITY_SIGNATURE_STATUS = 1


make_ready(__name__)
