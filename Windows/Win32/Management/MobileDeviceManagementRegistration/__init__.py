from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.Management.MobileDeviceManagementRegistration
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
MENROLL_E_DEVICE_MESSAGE_FORMAT_ERROR: Windows.Win32.Foundation.HRESULT = -2145910783
MENROLL_E_DEVICE_AUTHENTICATION_ERROR: Windows.Win32.Foundation.HRESULT = -2145910782
MENROLL_E_DEVICE_AUTHORIZATION_ERROR: Windows.Win32.Foundation.HRESULT = -2145910781
MENROLL_E_DEVICE_CERTIFICATEREQUEST_ERROR: Windows.Win32.Foundation.HRESULT = -2145910780
MENROLL_E_DEVICE_CONFIGMGRSERVER_ERROR: Windows.Win32.Foundation.HRESULT = -2145910779
MENROLL_E_DEVICE_INTERNALSERVICE_ERROR: Windows.Win32.Foundation.HRESULT = -2145910778
MENROLL_E_DEVICE_INVALIDSECURITY_ERROR: Windows.Win32.Foundation.HRESULT = -2145910777
MENROLL_E_DEVICE_UNKNOWN_ERROR: Windows.Win32.Foundation.HRESULT = -2145910776
MENROLL_E_ENROLLMENT_IN_PROGRESS: Windows.Win32.Foundation.HRESULT = -2145910775
MENROLL_E_DEVICE_ALREADY_ENROLLED: Windows.Win32.Foundation.HRESULT = -2145910774
MENROLL_E_DISCOVERY_SEC_CERT_DATE_INVALID: Windows.Win32.Foundation.HRESULT = -2145910771
MENROLL_E_PASSWORD_NEEDED: Windows.Win32.Foundation.HRESULT = -2145910770
MENROLL_E_WAB_ERROR: Windows.Win32.Foundation.HRESULT = -2145910769
MENROLL_E_CONNECTIVITY: Windows.Win32.Foundation.HRESULT = -2145910768
MENROLL_E_INVALIDSSLCERT: Windows.Win32.Foundation.HRESULT = -2145910766
MENROLL_E_DEVICECAPREACHED: Windows.Win32.Foundation.HRESULT = -2145910765
MENROLL_E_DEVICENOTSUPPORTED: Windows.Win32.Foundation.HRESULT = -2145910764
MENROLL_E_NOT_SUPPORTED: Windows.Win32.Foundation.HRESULT = -2145910763
MENROLL_E_NOTELIGIBLETORENEW: Windows.Win32.Foundation.HRESULT = -2145910762
MENROLL_E_INMAINTENANCE: Windows.Win32.Foundation.HRESULT = -2145910761
MENROLL_E_USER_LICENSE: Windows.Win32.Foundation.HRESULT = -2145910760
MENROLL_E_ENROLLMENTDATAINVALID: Windows.Win32.Foundation.HRESULT = -2145910759
MENROLL_E_INSECUREREDIRECT: Windows.Win32.Foundation.HRESULT = -2145910758
MENROLL_E_PLATFORM_WRONG_STATE: Windows.Win32.Foundation.HRESULT = -2145910757
MENROLL_E_PLATFORM_LICENSE_ERROR: Windows.Win32.Foundation.HRESULT = -2145910756
MENROLL_E_PLATFORM_UNKNOWN_ERROR: Windows.Win32.Foundation.HRESULT = -2145910755
MENROLL_E_PROV_CSP_CERTSTORE: Windows.Win32.Foundation.HRESULT = -2145910754
MENROLL_E_PROV_CSP_W7: Windows.Win32.Foundation.HRESULT = -2145910753
MENROLL_E_PROV_CSP_DMCLIENT: Windows.Win32.Foundation.HRESULT = -2145910752
MENROLL_E_PROV_CSP_PFW: Windows.Win32.Foundation.HRESULT = -2145910751
MENROLL_E_PROV_CSP_MISC: Windows.Win32.Foundation.HRESULT = -2145910750
MENROLL_E_PROV_UNKNOWN: Windows.Win32.Foundation.HRESULT = -2145910749
MENROLL_E_PROV_SSLCERTNOTFOUND: Windows.Win32.Foundation.HRESULT = -2145910748
MENROLL_E_PROV_CSP_APPMGMT: Windows.Win32.Foundation.HRESULT = -2145910747
MENROLL_E_DEVICE_MANAGEMENT_BLOCKED: Windows.Win32.Foundation.HRESULT = -2145910746
MENROLL_E_CERTPOLICY_PRIVATEKEYCREATION_FAILED: Windows.Win32.Foundation.HRESULT = -2145910745
MENROLL_E_CERTAUTH_FAILED_TO_FIND_CERT: Windows.Win32.Foundation.HRESULT = -2145910744
MENROLL_E_EMPTY_MESSAGE: Windows.Win32.Foundation.HRESULT = -2145910743
MENROLL_E_USER_CANCELLED: Windows.Win32.Foundation.HRESULT = -2145910736
MENROLL_E_MDM_NOT_CONFIGURED: Windows.Win32.Foundation.HRESULT = -2145910735
MDM_REGISTRATION_FACILITY_CODE: UInt32 = 25
DEVICE_ENROLLER_FACILITY_CODE: UInt32 = 24
MREGISTER_E_DEVICE_MESSAGE_FORMAT_ERROR: Windows.Win32.Foundation.HRESULT = -2145845247
MREGISTER_E_DEVICE_AUTHENTICATION_ERROR: Windows.Win32.Foundation.HRESULT = -2145845246
MREGISTER_E_DEVICE_AUTHORIZATION_ERROR: Windows.Win32.Foundation.HRESULT = -2145845245
MREGISTER_E_DEVICE_CERTIFCATEREQUEST_ERROR: Windows.Win32.Foundation.HRESULT = -2145845244
MENROLL_E_DEVICE_CERTIFCATEREQUEST_ERROR: Windows.Win32.Foundation.HRESULT = -2145910780
MREGISTER_E_DEVICE_CONFIGMGRSERVER_ERROR: Windows.Win32.Foundation.HRESULT = -2145845243
MREGISTER_E_DEVICE_INTERNALSERVICE_ERROR: Windows.Win32.Foundation.HRESULT = -2145845242
MREGISTER_E_DEVICE_INVALIDSECURITY_ERROR: Windows.Win32.Foundation.HRESULT = -2145845241
MREGISTER_E_DEVICE_UNKNOWN_ERROR: Windows.Win32.Foundation.HRESULT = -2145845240
MREGISTER_E_REGISTRATION_IN_PROGRESS: Windows.Win32.Foundation.HRESULT = -2145845239
MREGISTER_E_DEVICE_ALREADY_REGISTERED: Windows.Win32.Foundation.HRESULT = -2145845238
MREGISTER_E_DEVICE_NOT_REGISTERED: Windows.Win32.Foundation.HRESULT = -2145845237
MENROLL_E_DEVICE_NOT_ENROLLED: Windows.Win32.Foundation.HRESULT = -2145910773
MREGISTER_E_DISCOVERY_REDIRECTED: Windows.Win32.Foundation.HRESULT = -2145845236
MREGISTER_E_DEVICE_NOT_AD_REGISTERED_ERROR: Windows.Win32.Foundation.HRESULT = -2145845235
MREGISTER_E_DISCOVERY_FAILED: Windows.Win32.Foundation.HRESULT = -2145845234
MENROLL_E_NOTSUPPORTED: Windows.Win32.Foundation.HRESULT = -2145910763
MENROLL_E_USERLICENSE: Windows.Win32.Foundation.HRESULT = -2145910760
MENROLL_E_USER_CANCELED: Windows.Win32.Foundation.HRESULT = -2145910742
DEVICEREGISTRATIONTYPE_MDM_ONLY: UInt32 = 0
DEVICEREGISTRATIONTYPE_MAM: UInt32 = 5
DEVICEREGISTRATIONTYPE_MDM_DEVICEWIDE_WITH_AAD: UInt32 = 6
DEVICEREGISTRATIONTYPE_MDM_USERSPECIFIC_WITH_AAD: UInt32 = 13
@winfunctype('MDMRegistration.dll')
def GetDeviceRegistrationInfo(DeviceInformationClass: Windows.Win32.Management.MobileDeviceManagementRegistration.REGISTRATION_INFORMATION_CLASS, ppDeviceRegistrationInfo: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MDMRegistration.dll')
def IsDeviceRegisteredWithManagement(pfIsDeviceRegisteredWithManagement: POINTER(Windows.Win32.Foundation.BOOL), cchUPN: UInt32, pszUPN: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MDMRegistration.dll')
def IsManagementRegistrationAllowed(pfIsManagementRegistrationAllowed: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MDMRegistration.dll')
def IsMdmUxWithoutAadAllowed(isEnrollmentAllowed: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MDMRegistration.dll')
def SetManagedExternally(IsManagedExternally: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MDMRegistration.dll')
def DiscoverManagementService(pszUPN: Windows.Win32.Foundation.PWSTR, ppMgmtInfo: POINTER(POINTER(Windows.Win32.Management.MobileDeviceManagementRegistration.MANAGEMENT_SERVICE_INFO_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MDMRegistration.dll')
def RegisterDeviceWithManagementUsingAADCredentials(UserToken: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MDMRegistration.dll')
def RegisterDeviceWithManagementUsingAADDeviceCredentials() -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MDMRegistration.dll')
def RegisterDeviceWithManagementUsingAADDeviceCredentials2(MDMApplicationID: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MDMRegistration.DLL')
def RegisterDeviceDualEnrollMmpcUsingAADDeviceCredentials(cchEnrollmentId: UInt32, pszEnrollmentId: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MDMRegistration.dll')
def RegisterDeviceWithManagement(pszUPN: Windows.Win32.Foundation.PWSTR, ppszMDMServiceUri: Windows.Win32.Foundation.PWSTR, ppzsAccessToken: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MDMRegistration.dll')
def UnregisterDeviceWithManagement(enrollmentID: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MDMRegistration.dll')
def GetDeviceManagementConfigInfo(providerID: Windows.Win32.Foundation.PWSTR, configStringBufferLength: POINTER(UInt32), configString: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MDMRegistration.dll')
def SetDeviceManagementConfigInfo(providerID: Windows.Win32.Foundation.PWSTR, configString: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MDMRegistration.dll')
def GetManagementAppHyperlink(cchHyperlink: UInt32, pszHyperlink: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MDMRegistration.dll')
def DiscoverManagementServiceEx(pszUPN: Windows.Win32.Foundation.PWSTR, pszDiscoveryServiceCandidate: Windows.Win32.Foundation.PWSTR, ppMgmtInfo: POINTER(POINTER(Windows.Win32.Management.MobileDeviceManagementRegistration.MANAGEMENT_SERVICE_INFO_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MDMLocalManagement.dll')
def RegisterDeviceWithLocalManagement(alreadyRegistered: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MDMLocalManagement.dll')
def ApplyLocalManagementSyncML(syncMLRequest: Windows.Win32.Foundation.PWSTR, syncMLResult: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MDMLocalManagement.dll')
def UnregisterDeviceWithLocalManagement() -> Windows.Win32.Foundation.HRESULT: ...
class MANAGEMENT_REGISTRATION_INFO(EasyCastStructure):
    fDeviceRegisteredWithManagement: Windows.Win32.Foundation.BOOL
    dwDeviceRegistionKind: UInt32
    pszUPN: Windows.Win32.Foundation.PWSTR
    pszMDMServiceUri: Windows.Win32.Foundation.PWSTR
class MANAGEMENT_SERVICE_INFO(EasyCastStructure):
    pszMDMServiceUri: Windows.Win32.Foundation.PWSTR
    pszAuthenticationUri: Windows.Win32.Foundation.PWSTR
REGISTRATION_INFORMATION_CLASS = Int32
REGISTRATION_INFORMATION_CLASS_DeviceRegistrationBasicInfo: REGISTRATION_INFORMATION_CLASS = 1
REGISTRATION_INFORMATION_CLASS_MaxDeviceInfoClass: REGISTRATION_INFORMATION_CLASS = 2
make_head(_module, 'MANAGEMENT_REGISTRATION_INFO')
make_head(_module, 'MANAGEMENT_SERVICE_INFO')
