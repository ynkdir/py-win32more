from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Management.MobileDeviceManagementRegistration
MENROLL_E_DEVICE_MESSAGE_FORMAT_ERROR: win32more.Windows.Win32.Foundation.HRESULT = -2145910783
MENROLL_E_DEVICE_AUTHENTICATION_ERROR: win32more.Windows.Win32.Foundation.HRESULT = -2145910782
MENROLL_E_DEVICE_AUTHORIZATION_ERROR: win32more.Windows.Win32.Foundation.HRESULT = -2145910781
MENROLL_E_DEVICE_CERTIFICATEREQUEST_ERROR: win32more.Windows.Win32.Foundation.HRESULT = -2145910780
MENROLL_E_DEVICE_CONFIGMGRSERVER_ERROR: win32more.Windows.Win32.Foundation.HRESULT = -2145910779
MENROLL_E_DEVICE_INTERNALSERVICE_ERROR: win32more.Windows.Win32.Foundation.HRESULT = -2145910778
MENROLL_E_DEVICE_INVALIDSECURITY_ERROR: win32more.Windows.Win32.Foundation.HRESULT = -2145910777
MENROLL_E_DEVICE_UNKNOWN_ERROR: win32more.Windows.Win32.Foundation.HRESULT = -2145910776
MENROLL_E_ENROLLMENT_IN_PROGRESS: win32more.Windows.Win32.Foundation.HRESULT = -2145910775
MENROLL_E_DEVICE_ALREADY_ENROLLED: win32more.Windows.Win32.Foundation.HRESULT = -2145910774
MENROLL_E_DISCOVERY_SEC_CERT_DATE_INVALID: win32more.Windows.Win32.Foundation.HRESULT = -2145910771
MENROLL_E_PASSWORD_NEEDED: win32more.Windows.Win32.Foundation.HRESULT = -2145910770
MENROLL_E_WAB_ERROR: win32more.Windows.Win32.Foundation.HRESULT = -2145910769
MENROLL_E_CONNECTIVITY: win32more.Windows.Win32.Foundation.HRESULT = -2145910768
MENROLL_E_INVALIDSSLCERT: win32more.Windows.Win32.Foundation.HRESULT = -2145910766
MENROLL_E_DEVICECAPREACHED: win32more.Windows.Win32.Foundation.HRESULT = -2145910765
MENROLL_E_DEVICENOTSUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -2145910764
MENROLL_E_NOT_SUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -2145910763
MENROLL_E_NOTELIGIBLETORENEW: win32more.Windows.Win32.Foundation.HRESULT = -2145910762
MENROLL_E_INMAINTENANCE: win32more.Windows.Win32.Foundation.HRESULT = -2145910761
MENROLL_E_USER_LICENSE: win32more.Windows.Win32.Foundation.HRESULT = -2145910760
MENROLL_E_ENROLLMENTDATAINVALID: win32more.Windows.Win32.Foundation.HRESULT = -2145910759
MENROLL_E_INSECUREREDIRECT: win32more.Windows.Win32.Foundation.HRESULT = -2145910758
MENROLL_E_PLATFORM_WRONG_STATE: win32more.Windows.Win32.Foundation.HRESULT = -2145910757
MENROLL_E_PLATFORM_LICENSE_ERROR: win32more.Windows.Win32.Foundation.HRESULT = -2145910756
MENROLL_E_PLATFORM_UNKNOWN_ERROR: win32more.Windows.Win32.Foundation.HRESULT = -2145910755
MENROLL_E_PROV_CSP_CERTSTORE: win32more.Windows.Win32.Foundation.HRESULT = -2145910754
MENROLL_E_PROV_CSP_W7: win32more.Windows.Win32.Foundation.HRESULT = -2145910753
MENROLL_E_PROV_CSP_DMCLIENT: win32more.Windows.Win32.Foundation.HRESULT = -2145910752
MENROLL_E_PROV_CSP_PFW: win32more.Windows.Win32.Foundation.HRESULT = -2145910751
MENROLL_E_PROV_CSP_MISC: win32more.Windows.Win32.Foundation.HRESULT = -2145910750
MENROLL_E_PROV_UNKNOWN: win32more.Windows.Win32.Foundation.HRESULT = -2145910749
MENROLL_E_PROV_SSLCERTNOTFOUND: win32more.Windows.Win32.Foundation.HRESULT = -2145910748
MENROLL_E_PROV_CSP_APPMGMT: win32more.Windows.Win32.Foundation.HRESULT = -2145910747
MENROLL_E_DEVICE_MANAGEMENT_BLOCKED: win32more.Windows.Win32.Foundation.HRESULT = -2145910746
MENROLL_E_CERTPOLICY_PRIVATEKEYCREATION_FAILED: win32more.Windows.Win32.Foundation.HRESULT = -2145910745
MENROLL_E_CERTAUTH_FAILED_TO_FIND_CERT: win32more.Windows.Win32.Foundation.HRESULT = -2145910744
MENROLL_E_EMPTY_MESSAGE: win32more.Windows.Win32.Foundation.HRESULT = -2145910743
MENROLL_E_USER_CANCELLED: win32more.Windows.Win32.Foundation.HRESULT = -2145910736
MENROLL_E_MDM_NOT_CONFIGURED: win32more.Windows.Win32.Foundation.HRESULT = -2145910735
MENROLL_E_CUSTOMSERVERERROR: win32more.Windows.Win32.Foundation.HRESULT = -2145910734
MDM_REGISTRATION_FACILITY_CODE: UInt32 = 25
DEVICE_ENROLLER_FACILITY_CODE: UInt32 = 24
MREGISTER_E_DEVICE_MESSAGE_FORMAT_ERROR: win32more.Windows.Win32.Foundation.HRESULT = -2145845247
MREGISTER_E_DEVICE_AUTHENTICATION_ERROR: win32more.Windows.Win32.Foundation.HRESULT = -2145845246
MREGISTER_E_DEVICE_AUTHORIZATION_ERROR: win32more.Windows.Win32.Foundation.HRESULT = -2145845245
MREGISTER_E_DEVICE_CERTIFCATEREQUEST_ERROR: win32more.Windows.Win32.Foundation.HRESULT = -2145845244
MENROLL_E_DEVICE_CERTIFCATEREQUEST_ERROR: win32more.Windows.Win32.Foundation.HRESULT = -2145910780
MREGISTER_E_DEVICE_CONFIGMGRSERVER_ERROR: win32more.Windows.Win32.Foundation.HRESULT = -2145845243
MREGISTER_E_DEVICE_INTERNALSERVICE_ERROR: win32more.Windows.Win32.Foundation.HRESULT = -2145845242
MREGISTER_E_DEVICE_INVALIDSECURITY_ERROR: win32more.Windows.Win32.Foundation.HRESULT = -2145845241
MREGISTER_E_DEVICE_UNKNOWN_ERROR: win32more.Windows.Win32.Foundation.HRESULT = -2145845240
MREGISTER_E_REGISTRATION_IN_PROGRESS: win32more.Windows.Win32.Foundation.HRESULT = -2145845239
MREGISTER_E_DEVICE_ALREADY_REGISTERED: win32more.Windows.Win32.Foundation.HRESULT = -2145845238
MREGISTER_E_DEVICE_NOT_REGISTERED: win32more.Windows.Win32.Foundation.HRESULT = -2145845237
MENROLL_E_DEVICE_NOT_ENROLLED: win32more.Windows.Win32.Foundation.HRESULT = -2145910773
MREGISTER_E_DISCOVERY_REDIRECTED: win32more.Windows.Win32.Foundation.HRESULT = -2145845236
MREGISTER_E_DEVICE_NOT_AD_REGISTERED_ERROR: win32more.Windows.Win32.Foundation.HRESULT = -2145845235
MREGISTER_E_DISCOVERY_FAILED: win32more.Windows.Win32.Foundation.HRESULT = -2145845234
MENROLL_E_NOTSUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -2145910763
MENROLL_E_USERLICENSE: win32more.Windows.Win32.Foundation.HRESULT = -2145910760
MENROLL_E_USER_CANCELED: win32more.Windows.Win32.Foundation.HRESULT = -2145910742
DEVICEREGISTRATIONTYPE_MDM_ONLY: UInt32 = 0
DEVICEREGISTRATIONTYPE_MAM: UInt32 = 5
DEVICEREGISTRATIONTYPE_MDM_DEVICEWIDE_WITH_AAD: UInt32 = 6
DEVICEREGISTRATIONTYPE_MDM_USERSPECIFIC_WITH_AAD: UInt32 = 13
@winfunctype('MDMRegistration.dll')
def GetDeviceRegistrationInfo(DeviceInformationClass: win32more.Windows.Win32.Management.MobileDeviceManagementRegistration.REGISTRATION_INFORMATION_CLASS, ppDeviceRegistrationInfo: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MDMRegistration.dll')
def IsDeviceRegisteredWithManagement(pfIsDeviceRegisteredWithManagement: POINTER(win32more.Windows.Win32.Foundation.BOOL), cchUPN: UInt32, pszUPN: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MDMRegistration.dll')
def IsManagementRegistrationAllowed(pfIsManagementRegistrationAllowed: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MDMRegistration.dll')
def IsMdmUxWithoutAadAllowed(isEnrollmentAllowed: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MDMRegistration.dll')
def SetManagedExternally(IsManagedExternally: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MDMRegistration.dll')
def DiscoverManagementService(pszUPN: win32more.Windows.Win32.Foundation.PWSTR, ppMgmtInfo: POINTER(POINTER(win32more.Windows.Win32.Management.MobileDeviceManagementRegistration.MANAGEMENT_SERVICE_INFO))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MDMRegistration.dll')
def RegisterDeviceWithManagementUsingAADCredentials(UserToken: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MDMRegistration.dll')
def RegisterDeviceWithManagementUsingAADDeviceCredentials() -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MDMRegistration.dll')
def RegisterDeviceWithManagementUsingAADDeviceCredentials2(MDMApplicationID: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MDMRegistration.dll')
def RegisterDeviceWithManagement(pszUPN: win32more.Windows.Win32.Foundation.PWSTR, ppszMDMServiceUri: win32more.Windows.Win32.Foundation.PWSTR, ppzsAccessToken: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MDMRegistration.dll')
def UnregisterDeviceWithManagement(enrollmentID: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MDMRegistration.dll')
def GetDeviceManagementConfigInfo(providerID: win32more.Windows.Win32.Foundation.PWSTR, configStringBufferLength: POINTER(UInt32), configString: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MDMRegistration.dll')
def SetDeviceManagementConfigInfo(providerID: win32more.Windows.Win32.Foundation.PWSTR, configString: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MDMRegistration.dll')
def GetManagementAppHyperlink(cchHyperlink: UInt32, pszHyperlink: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MDMRegistration.dll')
def DiscoverManagementServiceEx(pszUPN: win32more.Windows.Win32.Foundation.PWSTR, pszDiscoveryServiceCandidate: win32more.Windows.Win32.Foundation.PWSTR, ppMgmtInfo: POINTER(POINTER(win32more.Windows.Win32.Management.MobileDeviceManagementRegistration.MANAGEMENT_SERVICE_INFO))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MDMLocalManagement.dll')
def RegisterDeviceWithLocalManagement(alreadyRegistered: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MDMLocalManagement.dll')
def ApplyLocalManagementSyncML(syncMLRequest: win32more.Windows.Win32.Foundation.PWSTR, syncMLResult: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MDMLocalManagement.dll')
def UnregisterDeviceWithLocalManagement() -> win32more.Windows.Win32.Foundation.HRESULT: ...
class MANAGEMENT_REGISTRATION_INFO(Structure):
    fDeviceRegisteredWithManagement: win32more.Windows.Win32.Foundation.BOOL
    dwDeviceRegistionKind: UInt32
    pszUPN: win32more.Windows.Win32.Foundation.PWSTR
    pszMDMServiceUri: win32more.Windows.Win32.Foundation.PWSTR
class MANAGEMENT_SERVICE_INFO(Structure):
    pszMDMServiceUri: win32more.Windows.Win32.Foundation.PWSTR
    pszAuthenticationUri: win32more.Windows.Win32.Foundation.PWSTR
REGISTRATION_INFORMATION_CLASS = Int32
DeviceRegistrationBasicInfo: win32more.Windows.Win32.Management.MobileDeviceManagementRegistration.REGISTRATION_INFORMATION_CLASS = 1
MaxDeviceInfoClass: win32more.Windows.Win32.Management.MobileDeviceManagementRegistration.REGISTRATION_INFORMATION_CLASS = 2


make_ready(__name__)
