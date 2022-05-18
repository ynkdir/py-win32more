from win32more import *
import win32more.Foundation
import win32more.Management.MobileDeviceManagementRegistration

def __getattr__(name):
    module = globals()
    try:
        f = module[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    module[name] = f()
    return module[name]
def __dir__():
    return __all__
MENROLL_E_DEVICE_MESSAGE_FORMAT_ERROR = -2145910783
MENROLL_E_DEVICE_AUTHENTICATION_ERROR = -2145910782
MENROLL_E_DEVICE_AUTHORIZATION_ERROR = -2145910781
MENROLL_E_DEVICE_CERTIFICATEREQUEST_ERROR = -2145910780
MENROLL_E_DEVICE_CONFIGMGRSERVER_ERROR = -2145910779
MENROLL_E_DEVICE_INTERNALSERVICE_ERROR = -2145910778
MENROLL_E_DEVICE_INVALIDSECURITY_ERROR = -2145910777
MENROLL_E_DEVICE_UNKNOWN_ERROR = -2145910776
MENROLL_E_ENROLLMENT_IN_PROGRESS = -2145910775
MENROLL_E_DEVICE_ALREADY_ENROLLED = -2145910774
MENROLL_E_DISCOVERY_SEC_CERT_DATE_INVALID = -2145910771
MENROLL_E_PASSWORD_NEEDED = -2145910770
MENROLL_E_WAB_ERROR = -2145910769
MENROLL_E_CONNECTIVITY = -2145910768
MENROLL_E_INVALIDSSLCERT = -2145910766
MENROLL_E_DEVICEAPREACHED = -2145910765
MENROLL_E_DEVICENOTSUPPORTED = -2145910764
MENROLL_E_NOT_SUPPORTED = -2145910763
MENROLL_E_NOTELIGIBLETORENEW = -2145910762
MENROLL_E_INMAINTENANCE = -2145910761
MENROLL_E_USER_LICENSE = -2145910760
MENROLL_E_ENROLLMENTDATAINVALID = -2145910759
MENROLL_E_INSECUREREDIRECT = -2145910758
MENROLL_E_PLATFORM_WRONG_STATE = -2145910757
MENROLL_E_PLATFORM_LICENSE_ERROR = -2145910756
MENROLL_E_PLATFORM_UNKNOWN_ERROR = -2145910755
MENROLL_E_PROV_CSP_CERTSTORE = -2145910754
MENROLL_E_PROV_CSP_W7 = -2145910753
MENROLL_E_PROV_CSP_DMCLIENT = -2145910752
MENROLL_E_PROV_CSP_PFW = -2145910751
MENROLL_E_PROV_CSP_MISC = -2145910750
MENROLL_E_PROV_UNKNOWN = -2145910749
MENROLL_E_PROV_SSLCERTNOTFOUND = -2145910748
MENROLL_E_PROV_CSP_APPMGMT = -2145910747
MENROLL_E_DEVICE_MANAGEMENT_BLOCKED = -2145910746
MENROLL_E_CERTPOLICY_PRIVATEKEYCREATION_FAILED = -2145910745
MENROLL_E_CERTAUTH_FAILED_TO_FIND_CERT = -2145910744
MENROLL_E_EMPTY_MESSAGE = -2145910743
MENROLL_E_USER_CANCELLED = -2145910736
MENROLL_E_MDM_NOT_CONFIGURED = -2145910735
MDM_REGISTRATION_FACILITY_CODE = 25
DEVICE_ENROLLER_FACILITY_CODE = 24
MREGISTER_E_DEVICE_MESSAGE_FORMAT_ERROR = -2145845247
MREGISTER_E_DEVICE_AUTHENTICATION_ERROR = -2145845246
MREGISTER_E_DEVICE_AUTHORIZATION_ERROR = -2145845245
MREGISTER_E_DEVICE_CERTIFCATEREQUEST_ERROR = -2145845244
MENROLL_E_DEVICE_CERTIFCATEREQUEST_ERROR = -2145910780
MREGISTER_E_DEVICE_CONFIGMGRSERVER_ERROR = -2145845243
MREGISTER_E_DEVICE_INTERNALSERVICE_ERROR = -2145845242
MREGISTER_E_DEVICE_INVALIDSECURITY_ERROR = -2145845241
MREGISTER_E_DEVICE_UNKNOWN_ERROR = -2145845240
MREGISTER_E_REGISTRATION_IN_PROGRESS = -2145845239
MREGISTER_E_DEVICE_ALREADY_REGISTERED = -2145845238
MREGISTER_E_DEVICE_NOT_REGISTERED = -2145845237
MENROLL_E_DEVICE_NOT_ENROLLED = -2145910773
MREGISTER_E_DISCOVERY_REDIRECTED = -2145845236
MREGISTER_E_DEVICE_NOT_AD_REGISTERED_ERROR = -2145845235
MREGISTER_E_DISCOVERY_FAILED = -2145845234
MENROLL_E_DEVICECAPREACHED = -2145910765
MENROLL_E_NOTSUPPORTED = -2145910763
MENROLL_E_USERLICENSE = -2145910760
MENROLL_E_USER_CANCELED = -2145910742
DEVICEREGISTRATIONTYPE_MDM_ONLY = 0
DEVICEREGISTRATIONTYPE_MAM = 5
DEVICEREGISTRATIONTYPE_MDM_DEVICEWIDE_WITH_AAD = 6
DEVICEREGISTRATIONTYPE_MDM_USERSPECIFIC_WITH_AAD = 13
def _define_MANAGEMENT_SERVICE_INFO_head():
    class MANAGEMENT_SERVICE_INFO(Structure):
        pass
    return MANAGEMENT_SERVICE_INFO
def _define_MANAGEMENT_SERVICE_INFO():
    MANAGEMENT_SERVICE_INFO = win32more.Management.MobileDeviceManagementRegistration.MANAGEMENT_SERVICE_INFO_head
    MANAGEMENT_SERVICE_INFO._fields_ = [
        ("pszMDMServiceUri", win32more.Foundation.PWSTR),
        ("pszAuthenticationUri", win32more.Foundation.PWSTR),
    ]
    return MANAGEMENT_SERVICE_INFO
def _define_MANAGEMENT_REGISTRATION_INFO_head():
    class MANAGEMENT_REGISTRATION_INFO(Structure):
        pass
    return MANAGEMENT_REGISTRATION_INFO
def _define_MANAGEMENT_REGISTRATION_INFO():
    MANAGEMENT_REGISTRATION_INFO = win32more.Management.MobileDeviceManagementRegistration.MANAGEMENT_REGISTRATION_INFO_head
    MANAGEMENT_REGISTRATION_INFO._fields_ = [
        ("fDeviceRegisteredWithManagement", win32more.Foundation.BOOL),
        ("dwDeviceRegistionKind", UInt32),
        ("pszUPN", win32more.Foundation.PWSTR),
        ("pszMDMServiceUri", win32more.Foundation.PWSTR),
    ]
    return MANAGEMENT_REGISTRATION_INFO
REGISTRATION_INFORMATION_CLASS = Int32
REGISTRATION_INFORMATION_CLASS_DeviceRegistrationBasicInfo = 1
REGISTRATION_INFORMATION_CLASS_MaxDeviceInfoClass = 2
def _define_GetDeviceRegistrationInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Management.MobileDeviceManagementRegistration.REGISTRATION_INFORMATION_CLASS,POINTER(c_void_p), use_last_error=False)(("GetDeviceRegistrationInfo", windll["MDMRegistration"]), ((1, 'DeviceInformationClass'),(1, 'ppDeviceRegistrationInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsDeviceRegisteredWithManagement():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL),UInt32,POINTER(Char), use_last_error=False)(("IsDeviceRegisteredWithManagement", windll["MDMRegistration"]), ((1, 'pfIsDeviceRegisteredWithManagement'),(1, 'cchUPN'),(1, 'pszUPN'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsManagementRegistrationAllowed():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(("IsManagementRegistrationAllowed", windll["MDMRegistration"]), ((1, 'pfIsManagementRegistrationAllowed'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsMdmUxWithoutAadAllowed():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(("IsMdmUxWithoutAadAllowed", windll["MDMRegistration"]), ((1, 'isEnrollmentAllowed'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetManagedExternally():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(("SetManagedExternally", windll["MDMRegistration"]), ((1, 'IsManagedExternally'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DiscoverManagementService():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(POINTER(win32more.Management.MobileDeviceManagementRegistration.MANAGEMENT_SERVICE_INFO_head)), use_last_error=False)(("DiscoverManagementService", windll["MDMRegistration"]), ((1, 'pszUPN'),(1, 'ppMgmtInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterDeviceWithManagementUsingAADCredentials():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE, use_last_error=False)(("RegisterDeviceWithManagementUsingAADCredentials", windll["MDMRegistration"]), ((1, 'UserToken'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterDeviceWithManagementUsingAADDeviceCredentials():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(("RegisterDeviceWithManagementUsingAADDeviceCredentials", windll["MDMRegistration"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterDeviceWithManagementUsingAADDeviceCredentials2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(("RegisterDeviceWithManagementUsingAADDeviceCredentials2", windll["MDMRegistration"]), ((1, 'MDMApplicationID'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterDeviceWithManagement():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("RegisterDeviceWithManagement", windll["MDMRegistration"]), ((1, 'pszUPN'),(1, 'ppszMDMServiceUri'),(1, 'ppzsAccessToken'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UnregisterDeviceWithManagement():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(("UnregisterDeviceWithManagement", windll["MDMRegistration"]), ((1, 'enrollmentID'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDeviceManagementConfigInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(Char), use_last_error=False)(("GetDeviceManagementConfigInfo", windll["MDMRegistration"]), ((1, 'providerID'),(1, 'configStringBufferLength'),(1, 'configString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetDeviceManagementConfigInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("SetDeviceManagementConfigInfo", windll["MDMRegistration"]), ((1, 'providerID'),(1, 'configString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetManagementAppHyperlink():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Char), use_last_error=False)(("GetManagementAppHyperlink", windll["MDMRegistration"]), ((1, 'cchHyperlink'),(1, 'pszHyperlink'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DiscoverManagementServiceEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(POINTER(win32more.Management.MobileDeviceManagementRegistration.MANAGEMENT_SERVICE_INFO_head)), use_last_error=False)(("DiscoverManagementServiceEx", windll["MDMRegistration"]), ((1, 'pszUPN'),(1, 'pszDiscoveryServiceCandidate'),(1, 'ppMgmtInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterDeviceWithLocalManagement():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(("RegisterDeviceWithLocalManagement", windll["MDMLocalManagement"]), ((1, 'alreadyRegistered'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ApplyLocalManagementSyncML():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("ApplyLocalManagementSyncML", windll["MDMLocalManagement"]), ((1, 'syncMLRequest'),(1, 'syncMLResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UnregisterDeviceWithLocalManagement():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(("UnregisterDeviceWithLocalManagement", windll["MDMLocalManagement"]), ())
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "MENROLL_E_DEVICE_MESSAGE_FORMAT_ERROR",
    "MENROLL_E_DEVICE_AUTHENTICATION_ERROR",
    "MENROLL_E_DEVICE_AUTHORIZATION_ERROR",
    "MENROLL_E_DEVICE_CERTIFICATEREQUEST_ERROR",
    "MENROLL_E_DEVICE_CONFIGMGRSERVER_ERROR",
    "MENROLL_E_DEVICE_INTERNALSERVICE_ERROR",
    "MENROLL_E_DEVICE_INVALIDSECURITY_ERROR",
    "MENROLL_E_DEVICE_UNKNOWN_ERROR",
    "MENROLL_E_ENROLLMENT_IN_PROGRESS",
    "MENROLL_E_DEVICE_ALREADY_ENROLLED",
    "MENROLL_E_DISCOVERY_SEC_CERT_DATE_INVALID",
    "MENROLL_E_PASSWORD_NEEDED",
    "MENROLL_E_WAB_ERROR",
    "MENROLL_E_CONNECTIVITY",
    "MENROLL_E_INVALIDSSLCERT",
    "MENROLL_E_DEVICEAPREACHED",
    "MENROLL_E_DEVICENOTSUPPORTED",
    "MENROLL_E_NOT_SUPPORTED",
    "MENROLL_E_NOTELIGIBLETORENEW",
    "MENROLL_E_INMAINTENANCE",
    "MENROLL_E_USER_LICENSE",
    "MENROLL_E_ENROLLMENTDATAINVALID",
    "MENROLL_E_INSECUREREDIRECT",
    "MENROLL_E_PLATFORM_WRONG_STATE",
    "MENROLL_E_PLATFORM_LICENSE_ERROR",
    "MENROLL_E_PLATFORM_UNKNOWN_ERROR",
    "MENROLL_E_PROV_CSP_CERTSTORE",
    "MENROLL_E_PROV_CSP_W7",
    "MENROLL_E_PROV_CSP_DMCLIENT",
    "MENROLL_E_PROV_CSP_PFW",
    "MENROLL_E_PROV_CSP_MISC",
    "MENROLL_E_PROV_UNKNOWN",
    "MENROLL_E_PROV_SSLCERTNOTFOUND",
    "MENROLL_E_PROV_CSP_APPMGMT",
    "MENROLL_E_DEVICE_MANAGEMENT_BLOCKED",
    "MENROLL_E_CERTPOLICY_PRIVATEKEYCREATION_FAILED",
    "MENROLL_E_CERTAUTH_FAILED_TO_FIND_CERT",
    "MENROLL_E_EMPTY_MESSAGE",
    "MENROLL_E_USER_CANCELLED",
    "MENROLL_E_MDM_NOT_CONFIGURED",
    "MDM_REGISTRATION_FACILITY_CODE",
    "DEVICE_ENROLLER_FACILITY_CODE",
    "MREGISTER_E_DEVICE_MESSAGE_FORMAT_ERROR",
    "MREGISTER_E_DEVICE_AUTHENTICATION_ERROR",
    "MREGISTER_E_DEVICE_AUTHORIZATION_ERROR",
    "MREGISTER_E_DEVICE_CERTIFCATEREQUEST_ERROR",
    "MENROLL_E_DEVICE_CERTIFCATEREQUEST_ERROR",
    "MREGISTER_E_DEVICE_CONFIGMGRSERVER_ERROR",
    "MREGISTER_E_DEVICE_INTERNALSERVICE_ERROR",
    "MREGISTER_E_DEVICE_INVALIDSECURITY_ERROR",
    "MREGISTER_E_DEVICE_UNKNOWN_ERROR",
    "MREGISTER_E_REGISTRATION_IN_PROGRESS",
    "MREGISTER_E_DEVICE_ALREADY_REGISTERED",
    "MREGISTER_E_DEVICE_NOT_REGISTERED",
    "MENROLL_E_DEVICE_NOT_ENROLLED",
    "MREGISTER_E_DISCOVERY_REDIRECTED",
    "MREGISTER_E_DEVICE_NOT_AD_REGISTERED_ERROR",
    "MREGISTER_E_DISCOVERY_FAILED",
    "MENROLL_E_DEVICECAPREACHED",
    "MENROLL_E_NOTSUPPORTED",
    "MENROLL_E_USERLICENSE",
    "MENROLL_E_USER_CANCELED",
    "DEVICEREGISTRATIONTYPE_MDM_ONLY",
    "DEVICEREGISTRATIONTYPE_MAM",
    "DEVICEREGISTRATIONTYPE_MDM_DEVICEWIDE_WITH_AAD",
    "DEVICEREGISTRATIONTYPE_MDM_USERSPECIFIC_WITH_AAD",
    "MANAGEMENT_SERVICE_INFO",
    "MANAGEMENT_REGISTRATION_INFO",
    "REGISTRATION_INFORMATION_CLASS",
    "REGISTRATION_INFORMATION_CLASS_DeviceRegistrationBasicInfo",
    "REGISTRATION_INFORMATION_CLASS_MaxDeviceInfoClass",
    "GetDeviceRegistrationInfo",
    "IsDeviceRegisteredWithManagement",
    "IsManagementRegistrationAllowed",
    "IsMdmUxWithoutAadAllowed",
    "SetManagedExternally",
    "DiscoverManagementService",
    "RegisterDeviceWithManagementUsingAADCredentials",
    "RegisterDeviceWithManagementUsingAADDeviceCredentials",
    "RegisterDeviceWithManagementUsingAADDeviceCredentials2",
    "RegisterDeviceWithManagement",
    "UnregisterDeviceWithManagement",
    "GetDeviceManagementConfigInfo",
    "SetDeviceManagementConfigInfo",
    "GetManagementAppHyperlink",
    "DiscoverManagementServiceEx",
    "RegisterDeviceWithLocalManagement",
    "ApplyLocalManagementSyncML",
    "UnregisterDeviceWithLocalManagement",
]
