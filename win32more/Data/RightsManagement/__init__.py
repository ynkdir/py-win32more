from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Data.RightsManagement
import win32more.Foundation
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
DRMHANDLE_INVALID = 0
DRMENVHANDLE_INVALID = 0
DRMQUERYHANDLE_INVALID = 0
DRMHSESSION_INVALID = 0
DRMPUBHANDLE_INVALID = 0
DRM_AL_NONSILENT = 1
DRM_AL_NOPERSIST = 2
DRM_AL_CANCEL = 4
DRM_AL_FETCHNOADVISORY = 8
DRM_AL_NOUI = 16
DRM_ACTIVATE_MACHINE = 1
DRM_ACTIVATE_GROUPIDENTITY = 2
DRM_ACTIVATE_TEMPORARY = 4
DRM_ACTIVATE_CANCEL = 8
DRM_ACTIVATE_SILENT = 16
DRM_ACTIVATE_SHARED_GROUPIDENTITY = 32
DRM_ACTIVATE_DELAYED = 64
DRM_EL_MACHINE = 1
DRM_EL_GROUPIDENTITY = 2
DRM_EL_GROUPIDENTITY_NAME = 4
DRM_EL_GROUPIDENTITY_LID = 8
DRM_EL_SPECIFIED_GROUPIDENTITY = 16
DRM_EL_EUL = 32
DRM_EL_EUL_LID = 64
DRM_EL_CLIENTLICENSOR = 128
DRM_EL_CLIENTLICENSOR_LID = 256
DRM_EL_SPECIFIED_CLIENTLICENSOR = 512
DRM_EL_REVOCATIONLIST = 1024
DRM_EL_REVOCATIONLIST_LID = 2048
DRM_EL_EXPIRED = 4096
DRM_EL_ISSUERNAME = 8192
DRM_EL_ISSUANCELICENSE_TEMPLATE = 16384
DRM_EL_ISSUANCELICENSE_TEMPLATE_LID = 32768
DRM_ADD_LICENSE_NOPERSIST = 0
DRM_ADD_LICENSE_PERSIST = 1
DRM_SERVICE_TYPE_ACTIVATION = 1
DRM_SERVICE_TYPE_CERTIFICATION = 2
DRM_SERVICE_TYPE_PUBLISHING = 4
DRM_SERVICE_TYPE_CLIENTLICENSOR = 8
DRM_SERVICE_TYPE_SILENT = 16
DRM_SERVICE_LOCATION_INTERNET = 1
DRM_SERVICE_LOCATION_ENTERPRISE = 2
DRM_DEFAULTGROUPIDTYPE_WINDOWSAUTH = 'WindowsAuthProvider'
DRM_DEFAULTGROUPIDTYPE_PASSPORT = 'PassportAuthProvider'
DRM_SIGN_ONLINE = 1
DRM_SIGN_OFFLINE = 2
DRM_SIGN_CANCEL = 4
DRM_SERVER_ISSUANCELICENSE = 8
DRM_AUTO_GENERATE_KEY = 16
DRM_OWNER_LICENSE_NOPERSIST = 32
DRM_REUSE_KEY = 64
DRM_LOCKBOXTYPE_NONE = 0
DRM_LOCKBOXTYPE_WHITEBOX = 1
DRM_LOCKBOXTYPE_BLACKBOX = 2
DRM_LOCKBOXTYPE_DEFAULT = 2
DRM_AILT_NONSILENT = 1
DRM_AILT_OBTAIN_ALL = 2
DRM_AILT_CANCEL = 4
MSDRM_CLIENT_ZONE = 52992
MSDRM_POLICY_ZONE = 37632
DRMIDVERSION = 0
DRMBOUNDLICENSEPARAMSVERSION = 1
DRMBINDINGFLAGS_IGNORE_VALIDITY_INTERVALS = 1
DRMLICENSEACQDATAVERSION = 0
DRMACTSERVINFOVERSION = 0
DRMCLIENTSTRUCTVERSION = 1
DRMCALLBACKVERSION = 1
def _define_DRMSetGlobalOptions():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Data.RightsManagement.DRMGLOBALOPTIONS,c_void_p,UInt32)(('DRMSetGlobalOptions', windll['msdrm.dll']), ((1, 'eGlobalOptions'),(1, 'pvdata'),(1, 'dwlen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetClientVersion():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Data.RightsManagement.DRM_CLIENT_VERSION_INFO_head))(('DRMGetClientVersion', windll['msdrm.dll']), ((1, 'pDRMClientVersionInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMInitEnvironment():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Data.RightsManagement.DRMSECURITYPROVIDERTYPE,win32more.Data.RightsManagement.DRMSPECTYPE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(UInt32))(('DRMInitEnvironment', windll['msdrm.dll']), ((1, 'eSecurityProviderType'),(1, 'eSpecification'),(1, 'wszSecurityProvider'),(1, 'wszManifestCredentials'),(1, 'wszMachineCredentials'),(1, 'phEnv'),(1, 'phDefaultLibrary'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMLoadLibrary():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Data.RightsManagement.DRMSPECTYPE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32))(('DRMLoadLibrary', windll['msdrm.dll']), ((1, 'hEnv'),(1, 'eSpecification'),(1, 'wszLibraryProvider'),(1, 'wszCredentials'),(1, 'phLibrary'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMCreateEnablingPrincipal():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,win32more.Foundation.PWSTR,POINTER(win32more.Data.RightsManagement.DRMID_head),win32more.Foundation.PWSTR,POINTER(UInt32))(('DRMCreateEnablingPrincipal', windll['msdrm.dll']), ((1, 'hEnv'),(1, 'hLibrary'),(1, 'wszObject'),(1, 'pidPrincipal'),(1, 'wszCredentials'),(1, 'phEnablingPrincipal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMCloseHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(('DRMCloseHandle', windll['msdrm.dll']), ((1, 'handle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMCloseEnvironmentHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(('DRMCloseEnvironmentHandle', windll['msdrm.dll']), ((1, 'hEnv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMDuplicateHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32))(('DRMDuplicateHandle', windll['msdrm.dll']), ((1, 'hToCopy'),(1, 'phCopy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMDuplicateEnvironmentHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32))(('DRMDuplicateEnvironmentHandle', windll['msdrm.dll']), ((1, 'hToCopy'),(1, 'phCopy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMRegisterRevocationList():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR)(('DRMRegisterRevocationList', windll['msdrm.dll']), ((1, 'hEnv'),(1, 'wszRevocationList'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMCheckSecurity():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32)(('DRMCheckSecurity', windll['msdrm.dll']), ((1, 'hEnv'),(1, 'cLevel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMRegisterContent():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(('DRMRegisterContent', windll['msdrm.dll']), ((1, 'fRegister'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMEncrypt():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32,c_char_p_no,POINTER(UInt32),c_char_p_no)(('DRMEncrypt', windll['msdrm.dll']), ((1, 'hCryptoProvider'),(1, 'iPosition'),(1, 'cNumInBytes'),(1, 'pbInData'),(1, 'pcNumOutBytes'),(1, 'pbOutData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMDecrypt():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32,c_char_p_no,POINTER(UInt32),c_char_p_no)(('DRMDecrypt', windll['msdrm.dll']), ((1, 'hCryptoProvider'),(1, 'iPosition'),(1, 'cNumInBytes'),(1, 'pbInData'),(1, 'pcNumOutBytes'),(1, 'pbOutData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMCreateBoundLicense():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Data.RightsManagement.DRMBOUNDLICENSEPARAMS_head),win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(UInt32))(('DRMCreateBoundLicense', windll['msdrm.dll']), ((1, 'hEnv'),(1, 'pParams'),(1, 'wszLicenseChain'),(1, 'phBoundLicense'),(1, 'phErrorLog'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMCreateEnablingBitsDecryptor():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32))(('DRMCreateEnablingBitsDecryptor', windll['msdrm.dll']), ((1, 'hBoundLicense'),(1, 'wszRight'),(1, 'hAuxLib'),(1, 'wszAuxPlug'),(1, 'phDecryptor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMCreateEnablingBitsEncryptor():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32))(('DRMCreateEnablingBitsEncryptor', windll['msdrm.dll']), ((1, 'hBoundLicense'),(1, 'wszRight'),(1, 'hAuxLib'),(1, 'wszAuxPlug'),(1, 'phEncryptor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMAttest():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,win32more.Data.RightsManagement.DRMATTESTTYPE,POINTER(UInt32),win32more.Foundation.PWSTR)(('DRMAttest', windll['msdrm.dll']), ((1, 'hEnablingPrincipal'),(1, 'wszData'),(1, 'eType'),(1, 'pcAttestedBlob'),(1, 'wszAttestedBlob'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Data.RightsManagement.DRMTIMETYPE,POINTER(win32more.Foundation.SYSTEMTIME_head))(('DRMGetTime', windll['msdrm.dll']), ((1, 'hEnv'),(1, 'eTimerIdType'),(1, 'poTimeObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,POINTER(win32more.Data.RightsManagement.DRMENCODINGTYPE),POINTER(UInt32),c_char_p_no)(('DRMGetInfo', windll['msdrm.dll']), ((1, 'handle'),(1, 'wszAttribute'),(1, 'peEncoding'),(1, 'pcBuffer'),(1, 'pbBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetEnvironmentInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,POINTER(win32more.Data.RightsManagement.DRMENCODINGTYPE),POINTER(UInt32),c_char_p_no)(('DRMGetEnvironmentInfo', windll['msdrm.dll']), ((1, 'handle'),(1, 'wszAttribute'),(1, 'peEncoding'),(1, 'pcBuffer'),(1, 'pbBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetProcAddress():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.FARPROC))(('DRMGetProcAddress', windll['msdrm.dll']), ((1, 'hLibrary'),(1, 'wszProcName'),(1, 'ppfnProcAddress'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetBoundLicenseObjectCount():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32))(('DRMGetBoundLicenseObjectCount', windll['msdrm.dll']), ((1, 'hQueryRoot'),(1, 'wszSubObjectType'),(1, 'pcSubObjects'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetBoundLicenseObject():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32))(('DRMGetBoundLicenseObject', windll['msdrm.dll']), ((1, 'hQueryRoot'),(1, 'wszSubObjectType'),(1, 'iWhich'),(1, 'phSubObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetBoundLicenseAttributeCount():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32))(('DRMGetBoundLicenseAttributeCount', windll['msdrm.dll']), ((1, 'hQueryRoot'),(1, 'wszAttribute'),(1, 'pcAttributes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetBoundLicenseAttribute():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Data.RightsManagement.DRMENCODINGTYPE),POINTER(UInt32),c_char_p_no)(('DRMGetBoundLicenseAttribute', windll['msdrm.dll']), ((1, 'hQueryRoot'),(1, 'wszAttribute'),(1, 'iWhich'),(1, 'peEncoding'),(1, 'pcBuffer'),(1, 'pbBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMCreateClientSession():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Data.RightsManagement.DRMCALLBACK,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32))(('DRMCreateClientSession', windll['msdrm.dll']), ((1, 'pfnCallback'),(1, 'uCallbackVersion'),(1, 'wszGroupIDProviderType'),(1, 'wszGroupID'),(1, 'phClient'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMIsActivated():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.Data.RightsManagement.DRM_ACTSERV_INFO_head))(('DRMIsActivated', windll['msdrm.dll']), ((1, 'hClient'),(1, 'uFlags'),(1, 'pActServInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMActivate():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32,POINTER(win32more.Data.RightsManagement.DRM_ACTSERV_INFO_head),c_void_p,win32more.Foundation.HWND)(('DRMActivate', windll['msdrm.dll']), ((1, 'hClient'),(1, 'uFlags'),(1, 'uLangID'),(1, 'pActServInfo'),(1, 'pvContext'),(1, 'hParentWnd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetServiceLocation():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32),win32more.Foundation.PWSTR)(('DRMGetServiceLocation', windll['msdrm.dll']), ((1, 'hClient'),(1, 'uServiceType'),(1, 'uServiceLocation'),(1, 'wszIssuanceLicense'),(1, 'puServiceURLLength'),(1, 'wszServiceURL'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMCreateLicenseStorageSession():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32))(('DRMCreateLicenseStorageSession', windll['msdrm.dll']), ((1, 'hEnv'),(1, 'hDefaultLibrary'),(1, 'hClient'),(1, 'uFlags'),(1, 'wszIssuanceLicense'),(1, 'phLicenseStorage'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMAddLicense():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,win32more.Foundation.PWSTR)(('DRMAddLicense', windll['msdrm.dll']), ((1, 'hLicenseStorage'),(1, 'uFlags'),(1, 'wszLicense'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMAcquireAdvisories():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,c_void_p)(('DRMAcquireAdvisories', windll['msdrm.dll']), ((1, 'hLicenseStorage'),(1, 'wszLicense'),(1, 'wszURL'),(1, 'pvContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMEnumerateLicense():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32,POINTER(win32more.Foundation.BOOL),POINTER(UInt32),win32more.Foundation.PWSTR)(('DRMEnumerateLicense', windll['msdrm.dll']), ((1, 'hSession'),(1, 'uFlags'),(1, 'uIndex'),(1, 'pfSharedFlag'),(1, 'puCertificateDataLen'),(1, 'wszCertificateData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMAcquireLicense():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,c_void_p)(('DRMAcquireLicense', windll['msdrm.dll']), ((1, 'hSession'),(1, 'uFlags'),(1, 'wszGroupIdentityCredential'),(1, 'wszRequestedRights'),(1, 'wszCustomData'),(1, 'wszURL'),(1, 'pvContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMDeleteLicense():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR)(('DRMDeleteLicense', windll['msdrm.dll']), ((1, 'hSession'),(1, 'wszLicenseId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMCloseSession():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(('DRMCloseSession', windll['msdrm.dll']), ((1, 'hSession'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMDuplicateSession():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32))(('DRMDuplicateSession', windll['msdrm.dll']), ((1, 'hSessionIn'),(1, 'phSessionOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetSecurityProvider():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32),win32more.Foundation.PWSTR,POINTER(UInt32),win32more.Foundation.PWSTR)(('DRMGetSecurityProvider', windll['msdrm.dll']), ((1, 'uFlags'),(1, 'puTypeLen'),(1, 'wszType'),(1, 'puPathLen'),(1, 'wszPath'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMEncode():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,c_char_p_no,POINTER(UInt32),win32more.Foundation.PWSTR)(('DRMEncode', windll['msdrm.dll']), ((1, 'wszAlgID'),(1, 'uDataLen'),(1, 'pbDecodedData'),(1, 'puEncodedStringLen'),(1, 'wszEncodedString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMDecode():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32),c_char_p_no)(('DRMDecode', windll['msdrm.dll']), ((1, 'wszAlgID'),(1, 'wszEncodedString'),(1, 'puDecodedDataLen'),(1, 'pbDecodedData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMConstructCertificateChain():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.PWSTR),POINTER(UInt32),win32more.Foundation.PWSTR)(('DRMConstructCertificateChain', windll['msdrm.dll']), ((1, 'cCertificates'),(1, 'rgwszCertificates'),(1, 'pcChain'),(1, 'wszChain'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMParseUnboundLicense():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(UInt32))(('DRMParseUnboundLicense', windll['msdrm.dll']), ((1, 'wszCertificate'),(1, 'phQueryRoot'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMCloseQueryHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(('DRMCloseQueryHandle', windll['msdrm.dll']), ((1, 'hQuery'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetUnboundLicenseObjectCount():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32))(('DRMGetUnboundLicenseObjectCount', windll['msdrm.dll']), ((1, 'hQueryRoot'),(1, 'wszSubObjectType'),(1, 'pcSubObjects'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetUnboundLicenseObject():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32))(('DRMGetUnboundLicenseObject', windll['msdrm.dll']), ((1, 'hQueryRoot'),(1, 'wszSubObjectType'),(1, 'iIndex'),(1, 'phSubQuery'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetUnboundLicenseAttributeCount():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32))(('DRMGetUnboundLicenseAttributeCount', windll['msdrm.dll']), ((1, 'hQueryRoot'),(1, 'wszAttributeType'),(1, 'pcAttributes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetUnboundLicenseAttribute():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Data.RightsManagement.DRMENCODINGTYPE),POINTER(UInt32),c_char_p_no)(('DRMGetUnboundLicenseAttribute', windll['msdrm.dll']), ((1, 'hQueryRoot'),(1, 'wszAttributeType'),(1, 'iWhich'),(1, 'peEncoding'),(1, 'pcBuffer'),(1, 'pbBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetCertificateChainCount():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(UInt32))(('DRMGetCertificateChainCount', windll['msdrm.dll']), ((1, 'wszChain'),(1, 'pcCertCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMDeconstructCertificateChain():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32),win32more.Foundation.PWSTR)(('DRMDeconstructCertificateChain', windll['msdrm.dll']), ((1, 'wszChain'),(1, 'iWhich'),(1, 'pcCert'),(1, 'wszCert'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMVerify():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(UInt32),win32more.Foundation.PWSTR,POINTER(win32more.Data.RightsManagement.DRMATTESTTYPE),POINTER(UInt32),win32more.Foundation.PWSTR,POINTER(UInt32),win32more.Foundation.PWSTR)(('DRMVerify', windll['msdrm.dll']), ((1, 'wszData'),(1, 'pcAttestedData'),(1, 'wszAttestedData'),(1, 'peType'),(1, 'pcPrincipal'),(1, 'wszPrincipal'),(1, 'pcManifest'),(1, 'wszManifest'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMCreateUser():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32))(('DRMCreateUser', windll['msdrm.dll']), ((1, 'wszUserName'),(1, 'wszUserId'),(1, 'wszUserIdType'),(1, 'phUser'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMCreateRight():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.SYSTEMTIME_head),POINTER(win32more.Foundation.SYSTEMTIME_head),UInt32,POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.PWSTR),POINTER(UInt32))(('DRMCreateRight', windll['msdrm.dll']), ((1, 'wszRightName'),(1, 'pstFrom'),(1, 'pstUntil'),(1, 'cExtendedInfo'),(1, 'pwszExtendedInfoName'),(1, 'pwszExtendedInfoValue'),(1, 'phRight'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMCreateIssuanceLicense():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.SYSTEMTIME_head),POINTER(win32more.Foundation.SYSTEMTIME_head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32))(('DRMCreateIssuanceLicense', windll['msdrm.dll']), ((1, 'pstTimeFrom'),(1, 'pstTimeUntil'),(1, 'wszReferralInfoName'),(1, 'wszReferralInfoURL'),(1, 'hOwner'),(1, 'wszIssuanceLicense'),(1, 'hBoundLicense'),(1, 'phIssuanceLicense'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMAddRightWithUser():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32)(('DRMAddRightWithUser', windll['msdrm.dll']), ((1, 'hIssuanceLicense'),(1, 'hRight'),(1, 'hUser'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMClearAllRights():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(('DRMClearAllRights', windll['msdrm.dll']), ((1, 'hIssuanceLicense'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMSetMetaData():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('DRMSetMetaData', windll['msdrm.dll']), ((1, 'hIssuanceLicense'),(1, 'wszContentId'),(1, 'wszContentIdType'),(1, 'wszSKUId'),(1, 'wszSKUIdType'),(1, 'wszContentType'),(1, 'wszContentName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMSetUsagePolicy():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Data.RightsManagement.DRM_USAGEPOLICY_TYPE,win32more.Foundation.BOOL,win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,c_char_p_no,UInt32)(('DRMSetUsagePolicy', windll['msdrm.dll']), ((1, 'hIssuanceLicense'),(1, 'eUsagePolicyType'),(1, 'fDelete'),(1, 'fExclusion'),(1, 'wszName'),(1, 'wszMinVersion'),(1, 'wszMaxVersion'),(1, 'wszPublicKey'),(1, 'wszDigestAlgorithm'),(1, 'pbDigest'),(1, 'cbDigest'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMSetRevocationPoint():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.SYSTEMTIME_head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('DRMSetRevocationPoint', windll['msdrm.dll']), ((1, 'hIssuanceLicense'),(1, 'fDelete'),(1, 'wszId'),(1, 'wszIdType'),(1, 'wszURL'),(1, 'pstFrequency'),(1, 'wszName'),(1, 'wszPublicKey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMSetApplicationSpecificData():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('DRMSetApplicationSpecificData', windll['msdrm.dll']), ((1, 'hIssuanceLicense'),(1, 'fDelete'),(1, 'wszName'),(1, 'wszValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMSetNameAndDescription():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.BOOL,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('DRMSetNameAndDescription', windll['msdrm.dll']), ((1, 'hIssuanceLicense'),(1, 'fDelete'),(1, 'lcid'),(1, 'wszName'),(1, 'wszDescription'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMSetIntervalTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32)(('DRMSetIntervalTime', windll['msdrm.dll']), ((1, 'hIssuanceLicense'),(1, 'cDays'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetIssuanceLicenseTemplate():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32),win32more.Foundation.PWSTR)(('DRMGetIssuanceLicenseTemplate', windll['msdrm.dll']), ((1, 'hIssuanceLicense'),(1, 'puIssuanceLicenseTemplateLength'),(1, 'wszIssuanceLicenseTemplate'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetSignedIssuanceLicense():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32,c_char_p_no,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Data.RightsManagement.DRMCALLBACK,win32more.Foundation.PWSTR,c_void_p)(('DRMGetSignedIssuanceLicense', windll['msdrm.dll']), ((1, 'hEnv'),(1, 'hIssuanceLicense'),(1, 'uFlags'),(1, 'pbSymKey'),(1, 'cbSymKey'),(1, 'wszSymKeyType'),(1, 'wszClientLicensorCertificate'),(1, 'pfnCallback'),(1, 'wszURL'),(1, 'pvContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetSignedIssuanceLicenseEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32,c_char_p_no,UInt32,win32more.Foundation.PWSTR,c_void_p,UInt32,UInt32,win32more.Data.RightsManagement.DRMCALLBACK,c_void_p)(('DRMGetSignedIssuanceLicenseEx', windll['msdrm.dll']), ((1, 'hEnv'),(1, 'hIssuanceLicense'),(1, 'uFlags'),(1, 'pbSymKey'),(1, 'cbSymKey'),(1, 'wszSymKeyType'),(1, 'pvReserved'),(1, 'hEnablingPrincipal'),(1, 'hBoundLicenseCLC'),(1, 'pfnCallback'),(1, 'pvContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMClosePubHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(('DRMClosePubHandle', windll['msdrm.dll']), ((1, 'hPub'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMDuplicatePubHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32))(('DRMDuplicatePubHandle', windll['msdrm.dll']), ((1, 'hPubIn'),(1, 'phPubOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetUserInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32),win32more.Foundation.PWSTR,POINTER(UInt32),win32more.Foundation.PWSTR,POINTER(UInt32),win32more.Foundation.PWSTR)(('DRMGetUserInfo', windll['msdrm.dll']), ((1, 'hUser'),(1, 'puUserNameLength'),(1, 'wszUserName'),(1, 'puUserIdLength'),(1, 'wszUserId'),(1, 'puUserIdTypeLength'),(1, 'wszUserIdType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetRightInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32),win32more.Foundation.PWSTR,POINTER(win32more.Foundation.SYSTEMTIME_head),POINTER(win32more.Foundation.SYSTEMTIME_head))(('DRMGetRightInfo', windll['msdrm.dll']), ((1, 'hRight'),(1, 'puRightNameLength'),(1, 'wszRightName'),(1, 'pstFrom'),(1, 'pstUntil'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetRightExtendedInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(UInt32),win32more.Foundation.PWSTR,POINTER(UInt32),win32more.Foundation.PWSTR)(('DRMGetRightExtendedInfo', windll['msdrm.dll']), ((1, 'hRight'),(1, 'uIndex'),(1, 'puExtendedInfoNameLength'),(1, 'wszExtendedInfoName'),(1, 'puExtendedInfoValueLength'),(1, 'wszExtendedInfoValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetUsers():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(UInt32))(('DRMGetUsers', windll['msdrm.dll']), ((1, 'hIssuanceLicense'),(1, 'uIndex'),(1, 'phUser'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetUserRights():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32,POINTER(UInt32))(('DRMGetUserRights', windll['msdrm.dll']), ((1, 'hIssuanceLicense'),(1, 'hUser'),(1, 'uIndex'),(1, 'phRight'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetMetaData():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32),win32more.Foundation.PWSTR,POINTER(UInt32),win32more.Foundation.PWSTR,POINTER(UInt32),win32more.Foundation.PWSTR,POINTER(UInt32),win32more.Foundation.PWSTR,POINTER(UInt32),win32more.Foundation.PWSTR,POINTER(UInt32),win32more.Foundation.PWSTR)(('DRMGetMetaData', windll['msdrm.dll']), ((1, 'hIssuanceLicense'),(1, 'puContentIdLength'),(1, 'wszContentId'),(1, 'puContentIdTypeLength'),(1, 'wszContentIdType'),(1, 'puSKUIdLength'),(1, 'wszSKUId'),(1, 'puSKUIdTypeLength'),(1, 'wszSKUIdType'),(1, 'puContentTypeLength'),(1, 'wszContentType'),(1, 'puContentNameLength'),(1, 'wszContentName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetApplicationSpecificData():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(UInt32),win32more.Foundation.PWSTR,POINTER(UInt32),win32more.Foundation.PWSTR)(('DRMGetApplicationSpecificData', windll['msdrm.dll']), ((1, 'hIssuanceLicense'),(1, 'uIndex'),(1, 'puNameLength'),(1, 'wszName'),(1, 'puValueLength'),(1, 'wszValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetIssuanceLicenseInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.SYSTEMTIME_head),POINTER(win32more.Foundation.SYSTEMTIME_head),UInt32,POINTER(UInt32),win32more.Foundation.PWSTR,POINTER(UInt32),win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(win32more.Foundation.BOOL))(('DRMGetIssuanceLicenseInfo', windll['msdrm.dll']), ((1, 'hIssuanceLicense'),(1, 'pstTimeFrom'),(1, 'pstTimeUntil'),(1, 'uFlags'),(1, 'puDistributionPointNameLength'),(1, 'wszDistributionPointName'),(1, 'puDistributionPointURLLength'),(1, 'wszDistributionPointURL'),(1, 'phOwner'),(1, 'pfOfficial'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetRevocationPoint():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32),win32more.Foundation.PWSTR,POINTER(UInt32),win32more.Foundation.PWSTR,POINTER(UInt32),win32more.Foundation.PWSTR,POINTER(win32more.Foundation.SYSTEMTIME_head),POINTER(UInt32),win32more.Foundation.PWSTR,POINTER(UInt32),win32more.Foundation.PWSTR)(('DRMGetRevocationPoint', windll['msdrm.dll']), ((1, 'hIssuanceLicense'),(1, 'puIdLength'),(1, 'wszId'),(1, 'puIdTypeLength'),(1, 'wszIdType'),(1, 'puURLLength'),(1, 'wszRL'),(1, 'pstFrequency'),(1, 'puNameLength'),(1, 'wszName'),(1, 'puPublicKeyLength'),(1, 'wszPublicKey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetUsagePolicy():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.Data.RightsManagement.DRM_USAGEPOLICY_TYPE),POINTER(win32more.Foundation.BOOL),POINTER(UInt32),win32more.Foundation.PWSTR,POINTER(UInt32),win32more.Foundation.PWSTR,POINTER(UInt32),win32more.Foundation.PWSTR,POINTER(UInt32),win32more.Foundation.PWSTR,POINTER(UInt32),win32more.Foundation.PWSTR,POINTER(UInt32),c_char_p_no)(('DRMGetUsagePolicy', windll['msdrm.dll']), ((1, 'hIssuanceLicense'),(1, 'uIndex'),(1, 'peUsagePolicyType'),(1, 'pfExclusion'),(1, 'puNameLength'),(1, 'wszName'),(1, 'puMinVersionLength'),(1, 'wszMinVersion'),(1, 'puMaxVersionLength'),(1, 'wszMaxVersion'),(1, 'puPublicKeyLength'),(1, 'wszPublicKey'),(1, 'puDigestAlgorithmLength'),(1, 'wszDigestAlgorithm'),(1, 'pcbDigest'),(1, 'pbDigest'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetNameAndDescription():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(UInt32),POINTER(UInt32),win32more.Foundation.PWSTR,POINTER(UInt32),win32more.Foundation.PWSTR)(('DRMGetNameAndDescription', windll['msdrm.dll']), ((1, 'hIssuanceLicense'),(1, 'uIndex'),(1, 'pulcid'),(1, 'puNameLength'),(1, 'wszName'),(1, 'puDescriptionLength'),(1, 'wszDescription'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetOwnerLicense():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32),win32more.Foundation.PWSTR)(('DRMGetOwnerLicense', windll['msdrm.dll']), ((1, 'hIssuanceLicense'),(1, 'puOwnerLicenseLength'),(1, 'wszOwnerLicense'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetIntervalTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32))(('DRMGetIntervalTime', windll['msdrm.dll']), ((1, 'hIssuanceLicense'),(1, 'pcDays'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMRepair():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,)(('DRMRepair', windll['msdrm.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMRegisterProtectedWindow():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.HWND)(('DRMRegisterProtectedWindow', windll['msdrm.dll']), ((1, 'hEnv'),(1, 'hwnd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMIsWindowProtected():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(win32more.Foundation.BOOL))(('DRMIsWindowProtected', windll['msdrm.dll']), ((1, 'hwnd'),(1, 'pfProtected'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMAcquireIssuanceLicenseTemplate():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,c_void_p,UInt32,POINTER(win32more.Foundation.PWSTR),win32more.Foundation.PWSTR,c_void_p)(('DRMAcquireIssuanceLicenseTemplate', windll['msdrm.dll']), ((1, 'hClient'),(1, 'uFlags'),(1, 'pvReserved'),(1, 'cTemplates'),(1, 'pwszTemplateIds'),(1, 'wszUrl'),(1, 'pvContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRM_ACTSERV_INFO_head():
    class DRM_ACTSERV_INFO(Structure):
        pass
    return DRM_ACTSERV_INFO
def _define_DRM_ACTSERV_INFO():
    DRM_ACTSERV_INFO = win32more.Data.RightsManagement.DRM_ACTSERV_INFO_head
    DRM_ACTSERV_INFO._fields_ = [
        ('uVersion', UInt32),
        ('wszPubKey', win32more.Foundation.PWSTR),
        ('wszURL', win32more.Foundation.PWSTR),
    ]
    return DRM_ACTSERV_INFO
def _define_DRM_CLIENT_VERSION_INFO_head():
    class DRM_CLIENT_VERSION_INFO(Structure):
        pass
    return DRM_CLIENT_VERSION_INFO
def _define_DRM_CLIENT_VERSION_INFO():
    DRM_CLIENT_VERSION_INFO = win32more.Data.RightsManagement.DRM_CLIENT_VERSION_INFO_head
    DRM_CLIENT_VERSION_INFO._fields_ = [
        ('uStructVersion', UInt32),
        ('dwVersion', UInt32 * 4),
        ('wszHierarchy', Char * 256),
        ('wszProductId', Char * 256),
        ('wszProductDescription', Char * 256),
    ]
    return DRM_CLIENT_VERSION_INFO
DRM_DISTRIBUTION_POINT_INFO = Int32
DRM_DISTRIBUTION_POINT_LICENSE_ACQUISITION = 0
DRM_DISTRIBUTION_POINT_PUBLISHING = 1
DRM_DISTRIBUTION_POINT_REFERRAL_INFO = 2
def _define_DRM_LICENSE_ACQ_DATA_head():
    class DRM_LICENSE_ACQ_DATA(Structure):
        pass
    return DRM_LICENSE_ACQ_DATA
def _define_DRM_LICENSE_ACQ_DATA():
    DRM_LICENSE_ACQ_DATA = win32more.Data.RightsManagement.DRM_LICENSE_ACQ_DATA_head
    DRM_LICENSE_ACQ_DATA._fields_ = [
        ('uVersion', UInt32),
        ('wszURL', win32more.Foundation.PWSTR),
        ('wszLocalFilename', win32more.Foundation.PWSTR),
        ('pbPostData', c_char_p_no),
        ('dwPostDataSize', UInt32),
        ('wszFriendlyName', win32more.Foundation.PWSTR),
    ]
    return DRM_LICENSE_ACQ_DATA
DRM_STATUS_MSG = Int32
DRM_MSG_ACTIVATE_MACHINE = 0
DRM_MSG_ACTIVATE_GROUPIDENTITY = 1
DRM_MSG_ACQUIRE_LICENSE = 2
DRM_MSG_ACQUIRE_ADVISORY = 3
DRM_MSG_SIGN_ISSUANCE_LICENSE = 4
DRM_MSG_ACQUIRE_CLIENTLICENSOR = 5
DRM_MSG_ACQUIRE_ISSUANCE_LICENSE_TEMPLATE = 6
DRM_USAGEPOLICY_TYPE = Int32
DRM_USAGEPOLICY_TYPE_BYNAME = 0
DRM_USAGEPOLICY_TYPE_BYPUBLICKEY = 1
DRM_USAGEPOLICY_TYPE_BYDIGEST = 2
DRM_USAGEPOLICY_TYPE_OSEXCLUSION = 3
DRMATTESTTYPE = Int32
DRMATTESTTYPE_FULLENVIRONMENT = 0
DRMATTESTTYPE_HASHONLY = 1
def _define_DRMBOUNDLICENSEPARAMS_head():
    class DRMBOUNDLICENSEPARAMS(Structure):
        pass
    return DRMBOUNDLICENSEPARAMS
def _define_DRMBOUNDLICENSEPARAMS():
    DRMBOUNDLICENSEPARAMS = win32more.Data.RightsManagement.DRMBOUNDLICENSEPARAMS_head
    DRMBOUNDLICENSEPARAMS._fields_ = [
        ('uVersion', UInt32),
        ('hEnablingPrincipal', UInt32),
        ('hSecureStore', UInt32),
        ('wszRightsRequested', win32more.Foundation.PWSTR),
        ('wszRightsGroup', win32more.Foundation.PWSTR),
        ('idResource', win32more.Data.RightsManagement.DRMID),
        ('cAuthenticatorCount', UInt32),
        ('rghAuthenticators', POINTER(UInt32)),
        ('wszDefaultEnablingPrincipalCredentials', win32more.Foundation.PWSTR),
        ('dwFlags', UInt32),
    ]
    return DRMBOUNDLICENSEPARAMS
def _define_DRMCALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Data.RightsManagement.DRM_STATUS_MSG,win32more.Foundation.HRESULT,c_void_p,c_void_p)
DRMENCODINGTYPE = Int32
DRMENCODINGTYPE_BASE64 = 0
DRMENCODINGTYPE_STRING = 1
DRMENCODINGTYPE_LONG = 2
DRMENCODINGTYPE_TIME = 3
DRMENCODINGTYPE_UINT = 4
DRMENCODINGTYPE_RAW = 5
DRMGLOBALOPTIONS = Int32
DRMGLOBALOPTIONS_USE_WINHTTP = 0
DRMGLOBALOPTIONS_USE_SERVERSECURITYPROCESSOR = 1
def _define_DRMID_head():
    class DRMID(Structure):
        pass
    return DRMID
def _define_DRMID():
    DRMID = win32more.Data.RightsManagement.DRMID_head
    DRMID._fields_ = [
        ('uVersion', UInt32),
        ('wszIDType', win32more.Foundation.PWSTR),
        ('wszID', win32more.Foundation.PWSTR),
    ]
    return DRMID
DRMSECURITYPROVIDERTYPE = Int32
DRMSECURITYPROVIDERTYPE_SOFTWARESECREP = 0
DRMSPECTYPE = Int32
DRMSPECTYPE_UNKNOWN = 0
DRMSPECTYPE_FILENAME = 1
DRMTIMETYPE = Int32
DRMTIMETYPE_SYSTEMUTC = 0
DRMTIMETYPE_SYSTEMLOCAL = 1
__all__ = [
    "DRMACTSERVINFOVERSION",
    "DRMATTESTTYPE",
    "DRMATTESTTYPE_FULLENVIRONMENT",
    "DRMATTESTTYPE_HASHONLY",
    "DRMAcquireAdvisories",
    "DRMAcquireIssuanceLicenseTemplate",
    "DRMAcquireLicense",
    "DRMActivate",
    "DRMAddLicense",
    "DRMAddRightWithUser",
    "DRMAttest",
    "DRMBINDINGFLAGS_IGNORE_VALIDITY_INTERVALS",
    "DRMBOUNDLICENSEPARAMS",
    "DRMBOUNDLICENSEPARAMSVERSION",
    "DRMCALLBACK",
    "DRMCALLBACKVERSION",
    "DRMCLIENTSTRUCTVERSION",
    "DRMCheckSecurity",
    "DRMClearAllRights",
    "DRMCloseEnvironmentHandle",
    "DRMCloseHandle",
    "DRMClosePubHandle",
    "DRMCloseQueryHandle",
    "DRMCloseSession",
    "DRMConstructCertificateChain",
    "DRMCreateBoundLicense",
    "DRMCreateClientSession",
    "DRMCreateEnablingBitsDecryptor",
    "DRMCreateEnablingBitsEncryptor",
    "DRMCreateEnablingPrincipal",
    "DRMCreateIssuanceLicense",
    "DRMCreateLicenseStorageSession",
    "DRMCreateRight",
    "DRMCreateUser",
    "DRMDecode",
    "DRMDeconstructCertificateChain",
    "DRMDecrypt",
    "DRMDeleteLicense",
    "DRMDuplicateEnvironmentHandle",
    "DRMDuplicateHandle",
    "DRMDuplicatePubHandle",
    "DRMDuplicateSession",
    "DRMENCODINGTYPE",
    "DRMENCODINGTYPE_BASE64",
    "DRMENCODINGTYPE_LONG",
    "DRMENCODINGTYPE_RAW",
    "DRMENCODINGTYPE_STRING",
    "DRMENCODINGTYPE_TIME",
    "DRMENCODINGTYPE_UINT",
    "DRMENVHANDLE_INVALID",
    "DRMEncode",
    "DRMEncrypt",
    "DRMEnumerateLicense",
    "DRMGLOBALOPTIONS",
    "DRMGLOBALOPTIONS_USE_SERVERSECURITYPROCESSOR",
    "DRMGLOBALOPTIONS_USE_WINHTTP",
    "DRMGetApplicationSpecificData",
    "DRMGetBoundLicenseAttribute",
    "DRMGetBoundLicenseAttributeCount",
    "DRMGetBoundLicenseObject",
    "DRMGetBoundLicenseObjectCount",
    "DRMGetCertificateChainCount",
    "DRMGetClientVersion",
    "DRMGetEnvironmentInfo",
    "DRMGetInfo",
    "DRMGetIntervalTime",
    "DRMGetIssuanceLicenseInfo",
    "DRMGetIssuanceLicenseTemplate",
    "DRMGetMetaData",
    "DRMGetNameAndDescription",
    "DRMGetOwnerLicense",
    "DRMGetProcAddress",
    "DRMGetRevocationPoint",
    "DRMGetRightExtendedInfo",
    "DRMGetRightInfo",
    "DRMGetSecurityProvider",
    "DRMGetServiceLocation",
    "DRMGetSignedIssuanceLicense",
    "DRMGetSignedIssuanceLicenseEx",
    "DRMGetTime",
    "DRMGetUnboundLicenseAttribute",
    "DRMGetUnboundLicenseAttributeCount",
    "DRMGetUnboundLicenseObject",
    "DRMGetUnboundLicenseObjectCount",
    "DRMGetUsagePolicy",
    "DRMGetUserInfo",
    "DRMGetUserRights",
    "DRMGetUsers",
    "DRMHANDLE_INVALID",
    "DRMHSESSION_INVALID",
    "DRMID",
    "DRMIDVERSION",
    "DRMInitEnvironment",
    "DRMIsActivated",
    "DRMIsWindowProtected",
    "DRMLICENSEACQDATAVERSION",
    "DRMLoadLibrary",
    "DRMPUBHANDLE_INVALID",
    "DRMParseUnboundLicense",
    "DRMQUERYHANDLE_INVALID",
    "DRMRegisterContent",
    "DRMRegisterProtectedWindow",
    "DRMRegisterRevocationList",
    "DRMRepair",
    "DRMSECURITYPROVIDERTYPE",
    "DRMSECURITYPROVIDERTYPE_SOFTWARESECREP",
    "DRMSPECTYPE",
    "DRMSPECTYPE_FILENAME",
    "DRMSPECTYPE_UNKNOWN",
    "DRMSetApplicationSpecificData",
    "DRMSetGlobalOptions",
    "DRMSetIntervalTime",
    "DRMSetMetaData",
    "DRMSetNameAndDescription",
    "DRMSetRevocationPoint",
    "DRMSetUsagePolicy",
    "DRMTIMETYPE",
    "DRMTIMETYPE_SYSTEMLOCAL",
    "DRMTIMETYPE_SYSTEMUTC",
    "DRMVerify",
    "DRM_ACTIVATE_CANCEL",
    "DRM_ACTIVATE_DELAYED",
    "DRM_ACTIVATE_GROUPIDENTITY",
    "DRM_ACTIVATE_MACHINE",
    "DRM_ACTIVATE_SHARED_GROUPIDENTITY",
    "DRM_ACTIVATE_SILENT",
    "DRM_ACTIVATE_TEMPORARY",
    "DRM_ACTSERV_INFO",
    "DRM_ADD_LICENSE_NOPERSIST",
    "DRM_ADD_LICENSE_PERSIST",
    "DRM_AILT_CANCEL",
    "DRM_AILT_NONSILENT",
    "DRM_AILT_OBTAIN_ALL",
    "DRM_AL_CANCEL",
    "DRM_AL_FETCHNOADVISORY",
    "DRM_AL_NONSILENT",
    "DRM_AL_NOPERSIST",
    "DRM_AL_NOUI",
    "DRM_AUTO_GENERATE_KEY",
    "DRM_CLIENT_VERSION_INFO",
    "DRM_DEFAULTGROUPIDTYPE_PASSPORT",
    "DRM_DEFAULTGROUPIDTYPE_WINDOWSAUTH",
    "DRM_DISTRIBUTION_POINT_INFO",
    "DRM_DISTRIBUTION_POINT_LICENSE_ACQUISITION",
    "DRM_DISTRIBUTION_POINT_PUBLISHING",
    "DRM_DISTRIBUTION_POINT_REFERRAL_INFO",
    "DRM_EL_CLIENTLICENSOR",
    "DRM_EL_CLIENTLICENSOR_LID",
    "DRM_EL_EUL",
    "DRM_EL_EUL_LID",
    "DRM_EL_EXPIRED",
    "DRM_EL_GROUPIDENTITY",
    "DRM_EL_GROUPIDENTITY_LID",
    "DRM_EL_GROUPIDENTITY_NAME",
    "DRM_EL_ISSUANCELICENSE_TEMPLATE",
    "DRM_EL_ISSUANCELICENSE_TEMPLATE_LID",
    "DRM_EL_ISSUERNAME",
    "DRM_EL_MACHINE",
    "DRM_EL_REVOCATIONLIST",
    "DRM_EL_REVOCATIONLIST_LID",
    "DRM_EL_SPECIFIED_CLIENTLICENSOR",
    "DRM_EL_SPECIFIED_GROUPIDENTITY",
    "DRM_LICENSE_ACQ_DATA",
    "DRM_LOCKBOXTYPE_BLACKBOX",
    "DRM_LOCKBOXTYPE_DEFAULT",
    "DRM_LOCKBOXTYPE_NONE",
    "DRM_LOCKBOXTYPE_WHITEBOX",
    "DRM_MSG_ACQUIRE_ADVISORY",
    "DRM_MSG_ACQUIRE_CLIENTLICENSOR",
    "DRM_MSG_ACQUIRE_ISSUANCE_LICENSE_TEMPLATE",
    "DRM_MSG_ACQUIRE_LICENSE",
    "DRM_MSG_ACTIVATE_GROUPIDENTITY",
    "DRM_MSG_ACTIVATE_MACHINE",
    "DRM_MSG_SIGN_ISSUANCE_LICENSE",
    "DRM_OWNER_LICENSE_NOPERSIST",
    "DRM_REUSE_KEY",
    "DRM_SERVER_ISSUANCELICENSE",
    "DRM_SERVICE_LOCATION_ENTERPRISE",
    "DRM_SERVICE_LOCATION_INTERNET",
    "DRM_SERVICE_TYPE_ACTIVATION",
    "DRM_SERVICE_TYPE_CERTIFICATION",
    "DRM_SERVICE_TYPE_CLIENTLICENSOR",
    "DRM_SERVICE_TYPE_PUBLISHING",
    "DRM_SERVICE_TYPE_SILENT",
    "DRM_SIGN_CANCEL",
    "DRM_SIGN_OFFLINE",
    "DRM_SIGN_ONLINE",
    "DRM_STATUS_MSG",
    "DRM_USAGEPOLICY_TYPE",
    "DRM_USAGEPOLICY_TYPE_BYDIGEST",
    "DRM_USAGEPOLICY_TYPE_BYNAME",
    "DRM_USAGEPOLICY_TYPE_BYPUBLICKEY",
    "DRM_USAGEPOLICY_TYPE_OSEXCLUSION",
    "MSDRM_CLIENT_ZONE",
    "MSDRM_POLICY_ZONE",
]
