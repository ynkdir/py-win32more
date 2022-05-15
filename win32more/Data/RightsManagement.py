from win32more import *
import win32more.Data.RightsManagement
import win32more.Foundation

def __getattr__(name):
    if f"_define_{name}" not in globals():
        raise AttributeError()
    setattr(win32more.Data.RightsManagement, name, globals()[f"_define_{name}"]())
    return getattr(win32more.Data.RightsManagement, name)
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
def _define_DRMID_head():
    class DRMID(Structure):
        pass
    return DRMID
def _define_DRMID():
    DRMID = win32more.Data.RightsManagement.DRMID_head
    DRMID._fields_ = [
        ("uVersion", UInt32),
        ("wszIDType", win32more.Foundation.PWSTR),
        ("wszID", win32more.Foundation.PWSTR),
    ]
    return DRMID
DRMTIMETYPE = Int32
DRMTIMETYPE_SYSTEMUTC = 0
DRMTIMETYPE_SYSTEMLOCAL = 1
DRMENCODINGTYPE = Int32
DRMENCODINGTYPE_BASE64 = 0
DRMENCODINGTYPE_STRING = 1
DRMENCODINGTYPE_LONG = 2
DRMENCODINGTYPE_TIME = 3
DRMENCODINGTYPE_UINT = 4
DRMENCODINGTYPE_RAW = 5
DRMATTESTTYPE = Int32
DRMATTESTTYPE_FULLENVIRONMENT = 0
DRMATTESTTYPE_HASHONLY = 1
DRMSPECTYPE = Int32
DRMSPECTYPE_UNKNOWN = 0
DRMSPECTYPE_FILENAME = 1
DRMSECURITYPROVIDERTYPE = Int32
DRMSECURITYPROVIDERTYPE_SOFTWARESECREP = 0
DRMGLOBALOPTIONS = Int32
DRMGLOBALOPTIONS_USE_WINHTTP = 0
DRMGLOBALOPTIONS_USE_SERVERSECURITYPROCESSOR = 1
def _define_DRMBOUNDLICENSEPARAMS_head():
    class DRMBOUNDLICENSEPARAMS(Structure):
        pass
    return DRMBOUNDLICENSEPARAMS
def _define_DRMBOUNDLICENSEPARAMS():
    DRMBOUNDLICENSEPARAMS = win32more.Data.RightsManagement.DRMBOUNDLICENSEPARAMS_head
    DRMBOUNDLICENSEPARAMS._fields_ = [
        ("uVersion", UInt32),
        ("hEnablingPrincipal", UInt32),
        ("hSecureStore", UInt32),
        ("wszRightsRequested", win32more.Foundation.PWSTR),
        ("wszRightsGroup", win32more.Foundation.PWSTR),
        ("idResource", win32more.Data.RightsManagement.DRMID),
        ("cAuthenticatorCount", UInt32),
        ("rghAuthenticators", POINTER(UInt32)),
        ("wszDefaultEnablingPrincipalCredentials", win32more.Foundation.PWSTR),
        ("dwFlags", UInt32),
    ]
    return DRMBOUNDLICENSEPARAMS
def _define_DRM_LICENSE_ACQ_DATA_head():
    class DRM_LICENSE_ACQ_DATA(Structure):
        pass
    return DRM_LICENSE_ACQ_DATA
def _define_DRM_LICENSE_ACQ_DATA():
    DRM_LICENSE_ACQ_DATA = win32more.Data.RightsManagement.DRM_LICENSE_ACQ_DATA_head
    DRM_LICENSE_ACQ_DATA._fields_ = [
        ("uVersion", UInt32),
        ("wszURL", win32more.Foundation.PWSTR),
        ("wszLocalFilename", win32more.Foundation.PWSTR),
        ("pbPostData", c_char_p_no),
        ("dwPostDataSize", UInt32),
        ("wszFriendlyName", win32more.Foundation.PWSTR),
    ]
    return DRM_LICENSE_ACQ_DATA
def _define_DRM_ACTSERV_INFO_head():
    class DRM_ACTSERV_INFO(Structure):
        pass
    return DRM_ACTSERV_INFO
def _define_DRM_ACTSERV_INFO():
    DRM_ACTSERV_INFO = win32more.Data.RightsManagement.DRM_ACTSERV_INFO_head
    DRM_ACTSERV_INFO._fields_ = [
        ("uVersion", UInt32),
        ("wszPubKey", win32more.Foundation.PWSTR),
        ("wszURL", win32more.Foundation.PWSTR),
    ]
    return DRM_ACTSERV_INFO
def _define_DRM_CLIENT_VERSION_INFO_head():
    class DRM_CLIENT_VERSION_INFO(Structure):
        pass
    return DRM_CLIENT_VERSION_INFO
def _define_DRM_CLIENT_VERSION_INFO():
    DRM_CLIENT_VERSION_INFO = win32more.Data.RightsManagement.DRM_CLIENT_VERSION_INFO_head
    DRM_CLIENT_VERSION_INFO._fields_ = [
        ("uStructVersion", UInt32),
        ("dwVersion", UInt32 * 4),
        ("wszHierarchy", Char * 256),
        ("wszProductId", Char * 256),
        ("wszProductDescription", Char * 256),
    ]
    return DRM_CLIENT_VERSION_INFO
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
DRM_DISTRIBUTION_POINT_INFO = Int32
DRM_DISTRIBUTION_POINT_LICENSE_ACQUISITION = 0
DRM_DISTRIBUTION_POINT_PUBLISHING = 1
DRM_DISTRIBUTION_POINT_REFERRAL_INFO = 2
def _define_DRMCALLBACK():
    return CFUNCTYPE(win32more.Foundation.HRESULT,win32more.Data.RightsManagement.DRM_STATUS_MSG,win32more.Foundation.HRESULT,c_void_p,c_void_p, use_last_error=False)
def _define_DRMSetGlobalOptions():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Data.RightsManagement.DRMGLOBALOPTIONS,c_void_p,UInt32, use_last_error=False)(("DRMSetGlobalOptions", windll["msdrm"]), ((1, 'eGlobalOptions'),(1, 'pvdata'),(1, 'dwlen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetClientVersion():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Data.RightsManagement.DRM_CLIENT_VERSION_INFO_head), use_last_error=False)(("DRMGetClientVersion", windll["msdrm"]), ((1, 'pDRMClientVersionInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMInitEnvironment():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Data.RightsManagement.DRMSECURITYPROVIDERTYPE,win32more.Data.RightsManagement.DRMSPECTYPE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("DRMInitEnvironment", windll["msdrm"]), ((1, 'eSecurityProviderType'),(1, 'eSpecification'),(1, 'wszSecurityProvider'),(1, 'wszManifestCredentials'),(1, 'wszMachineCredentials'),(1, 'phEnv'),(1, 'phDefaultLibrary'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMLoadLibrary():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Data.RightsManagement.DRMSPECTYPE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(("DRMLoadLibrary", windll["msdrm"]), ((1, 'hEnv'),(1, 'eSpecification'),(1, 'wszLibraryProvider'),(1, 'wszCredentials'),(1, 'phLibrary'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMCreateEnablingPrincipal():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,win32more.Foundation.PWSTR,POINTER(win32more.Data.RightsManagement.DRMID_head),win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(("DRMCreateEnablingPrincipal", windll["msdrm"]), ((1, 'hEnv'),(1, 'hLibrary'),(1, 'wszObject'),(1, 'pidPrincipal'),(1, 'wszCredentials'),(1, 'phEnablingPrincipal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMCloseHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(("DRMCloseHandle", windll["msdrm"]), ((1, 'handle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMCloseEnvironmentHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(("DRMCloseEnvironmentHandle", windll["msdrm"]), ((1, 'hEnv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMDuplicateHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(("DRMDuplicateHandle", windll["msdrm"]), ((1, 'hToCopy'),(1, 'phCopy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMDuplicateEnvironmentHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(("DRMDuplicateEnvironmentHandle", windll["msdrm"]), ((1, 'hToCopy'),(1, 'phCopy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMRegisterRevocationList():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR, use_last_error=False)(("DRMRegisterRevocationList", windll["msdrm"]), ((1, 'hEnv'),(1, 'wszRevocationList'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMCheckSecurity():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(("DRMCheckSecurity", windll["msdrm"]), ((1, 'hEnv'),(1, 'cLevel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMRegisterContent():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(("DRMRegisterContent", windll["msdrm"]), ((1, 'fRegister'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMEncrypt():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32,c_char_p_no,POINTER(UInt32),c_char_p_no, use_last_error=False)(("DRMEncrypt", windll["msdrm"]), ((1, 'hCryptoProvider'),(1, 'iPosition'),(1, 'cNumInBytes'),(1, 'pbInData'),(1, 'pcNumOutBytes'),(1, 'pbOutData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMDecrypt():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32,c_char_p_no,POINTER(UInt32),c_char_p_no, use_last_error=False)(("DRMDecrypt", windll["msdrm"]), ((1, 'hCryptoProvider'),(1, 'iPosition'),(1, 'cNumInBytes'),(1, 'pbInData'),(1, 'pcNumOutBytes'),(1, 'pbOutData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMCreateBoundLicense():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Data.RightsManagement.DRMBOUNDLICENSEPARAMS_head),win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("DRMCreateBoundLicense", windll["msdrm"]), ((1, 'hEnv'),(1, 'pParams'),(1, 'wszLicenseChain'),(1, 'phBoundLicense'),(1, 'phErrorLog'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMCreateEnablingBitsDecryptor():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(("DRMCreateEnablingBitsDecryptor", windll["msdrm"]), ((1, 'hBoundLicense'),(1, 'wszRight'),(1, 'hAuxLib'),(1, 'wszAuxPlug'),(1, 'phDecryptor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMCreateEnablingBitsEncryptor():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(("DRMCreateEnablingBitsEncryptor", windll["msdrm"]), ((1, 'hBoundLicense'),(1, 'wszRight'),(1, 'hAuxLib'),(1, 'wszAuxPlug'),(1, 'phEncryptor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMAttest():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,win32more.Data.RightsManagement.DRMATTESTTYPE,POINTER(UInt32),POINTER(Char), use_last_error=False)(("DRMAttest", windll["msdrm"]), ((1, 'hEnablingPrincipal'),(1, 'wszData'),(1, 'eType'),(1, 'pcAttestedBlob'),(1, 'wszAttestedBlob'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Data.RightsManagement.DRMTIMETYPE,POINTER(win32more.Foundation.SYSTEMTIME_head), use_last_error=False)(("DRMGetTime", windll["msdrm"]), ((1, 'hEnv'),(1, 'eTimerIdType'),(1, 'poTimeObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,POINTER(win32more.Data.RightsManagement.DRMENCODINGTYPE),POINTER(UInt32),c_char_p_no, use_last_error=False)(("DRMGetInfo", windll["msdrm"]), ((1, 'handle'),(1, 'wszAttribute'),(1, 'peEncoding'),(1, 'pcBuffer'),(1, 'pbBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetEnvironmentInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,POINTER(win32more.Data.RightsManagement.DRMENCODINGTYPE),POINTER(UInt32),c_char_p_no, use_last_error=False)(("DRMGetEnvironmentInfo", windll["msdrm"]), ((1, 'handle'),(1, 'wszAttribute'),(1, 'peEncoding'),(1, 'pcBuffer'),(1, 'pbBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetProcAddress():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.FARPROC), use_last_error=False)(("DRMGetProcAddress", windll["msdrm"]), ((1, 'hLibrary'),(1, 'wszProcName'),(1, 'ppfnProcAddress'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetBoundLicenseObjectCount():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(("DRMGetBoundLicenseObjectCount", windll["msdrm"]), ((1, 'hQueryRoot'),(1, 'wszSubObjectType'),(1, 'pcSubObjects'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetBoundLicenseObject():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32), use_last_error=False)(("DRMGetBoundLicenseObject", windll["msdrm"]), ((1, 'hQueryRoot'),(1, 'wszSubObjectType'),(1, 'iWhich'),(1, 'phSubObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetBoundLicenseAttributeCount():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(("DRMGetBoundLicenseAttributeCount", windll["msdrm"]), ((1, 'hQueryRoot'),(1, 'wszAttribute'),(1, 'pcAttributes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetBoundLicenseAttribute():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Data.RightsManagement.DRMENCODINGTYPE),POINTER(UInt32),c_char_p_no, use_last_error=False)(("DRMGetBoundLicenseAttribute", windll["msdrm"]), ((1, 'hQueryRoot'),(1, 'wszAttribute'),(1, 'iWhich'),(1, 'peEncoding'),(1, 'pcBuffer'),(1, 'pbBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMCreateClientSession():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Data.RightsManagement.DRMCALLBACK,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(("DRMCreateClientSession", windll["msdrm"]), ((1, 'pfnCallback'),(1, 'uCallbackVersion'),(1, 'wszGroupIDProviderType'),(1, 'wszGroupID'),(1, 'phClient'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMIsActivated():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.Data.RightsManagement.DRM_ACTSERV_INFO_head), use_last_error=False)(("DRMIsActivated", windll["msdrm"]), ((1, 'hClient'),(1, 'uFlags'),(1, 'pActServInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMActivate():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32,POINTER(win32more.Data.RightsManagement.DRM_ACTSERV_INFO_head),c_void_p,win32more.Foundation.HWND, use_last_error=False)(("DRMActivate", windll["msdrm"]), ((1, 'hClient'),(1, 'uFlags'),(1, 'uLangID'),(1, 'pActServInfo'),(1, 'pvContext'),(1, 'hParentWnd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetServiceLocation():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(Char), use_last_error=False)(("DRMGetServiceLocation", windll["msdrm"]), ((1, 'hClient'),(1, 'uServiceType'),(1, 'uServiceLocation'),(1, 'wszIssuanceLicense'),(1, 'puServiceURLLength'),(1, 'wszServiceURL'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMCreateLicenseStorageSession():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(("DRMCreateLicenseStorageSession", windll["msdrm"]), ((1, 'hEnv'),(1, 'hDefaultLibrary'),(1, 'hClient'),(1, 'uFlags'),(1, 'wszIssuanceLicense'),(1, 'phLicenseStorage'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMAddLicense():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,win32more.Foundation.PWSTR, use_last_error=False)(("DRMAddLicense", windll["msdrm"]), ((1, 'hLicenseStorage'),(1, 'uFlags'),(1, 'wszLicense'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMAcquireAdvisories():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,c_void_p, use_last_error=False)(("DRMAcquireAdvisories", windll["msdrm"]), ((1, 'hLicenseStorage'),(1, 'wszLicense'),(1, 'wszURL'),(1, 'pvContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMEnumerateLicense():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32,POINTER(win32more.Foundation.BOOL),POINTER(UInt32),POINTER(Char), use_last_error=False)(("DRMEnumerateLicense", windll["msdrm"]), ((1, 'hSession'),(1, 'uFlags'),(1, 'uIndex'),(1, 'pfSharedFlag'),(1, 'puCertificateDataLen'),(1, 'wszCertificateData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMAcquireLicense():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,c_void_p, use_last_error=False)(("DRMAcquireLicense", windll["msdrm"]), ((1, 'hSession'),(1, 'uFlags'),(1, 'wszGroupIdentityCredential'),(1, 'wszRequestedRights'),(1, 'wszCustomData'),(1, 'wszURL'),(1, 'pvContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMDeleteLicense():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR, use_last_error=False)(("DRMDeleteLicense", windll["msdrm"]), ((1, 'hSession'),(1, 'wszLicenseId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMCloseSession():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(("DRMCloseSession", windll["msdrm"]), ((1, 'hSession'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMDuplicateSession():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(("DRMDuplicateSession", windll["msdrm"]), ((1, 'hSessionIn'),(1, 'phSessionOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetSecurityProvider():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32),POINTER(Char),POINTER(UInt32),POINTER(Char), use_last_error=False)(("DRMGetSecurityProvider", windll["msdrm"]), ((1, 'uFlags'),(1, 'puTypeLen'),(1, 'wszType'),(1, 'puPathLen'),(1, 'wszPath'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMEncode():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,c_char_p_no,POINTER(UInt32),POINTER(Char), use_last_error=False)(("DRMEncode", windll["msdrm"]), ((1, 'wszAlgID'),(1, 'uDataLen'),(1, 'pbDecodedData'),(1, 'puEncodedStringLen'),(1, 'wszEncodedString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMDecode():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32),c_char_p_no, use_last_error=False)(("DRMDecode", windll["msdrm"]), ((1, 'wszAlgID'),(1, 'wszEncodedString'),(1, 'puDecodedDataLen'),(1, 'pbDecodedData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMConstructCertificateChain():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.PWSTR),POINTER(UInt32),POINTER(Char), use_last_error=False)(("DRMConstructCertificateChain", windll["msdrm"]), ((1, 'cCertificates'),(1, 'rgwszCertificates'),(1, 'pcChain'),(1, 'wszChain'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMParseUnboundLicense():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(("DRMParseUnboundLicense", windll["msdrm"]), ((1, 'wszCertificate'),(1, 'phQueryRoot'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMCloseQueryHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(("DRMCloseQueryHandle", windll["msdrm"]), ((1, 'hQuery'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetUnboundLicenseObjectCount():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(("DRMGetUnboundLicenseObjectCount", windll["msdrm"]), ((1, 'hQueryRoot'),(1, 'wszSubObjectType'),(1, 'pcSubObjects'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetUnboundLicenseObject():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32), use_last_error=False)(("DRMGetUnboundLicenseObject", windll["msdrm"]), ((1, 'hQueryRoot'),(1, 'wszSubObjectType'),(1, 'iIndex'),(1, 'phSubQuery'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetUnboundLicenseAttributeCount():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(("DRMGetUnboundLicenseAttributeCount", windll["msdrm"]), ((1, 'hQueryRoot'),(1, 'wszAttributeType'),(1, 'pcAttributes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetUnboundLicenseAttribute():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Data.RightsManagement.DRMENCODINGTYPE),POINTER(UInt32),c_char_p_no, use_last_error=False)(("DRMGetUnboundLicenseAttribute", windll["msdrm"]), ((1, 'hQueryRoot'),(1, 'wszAttributeType'),(1, 'iWhich'),(1, 'peEncoding'),(1, 'pcBuffer'),(1, 'pbBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetCertificateChainCount():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(("DRMGetCertificateChainCount", windll["msdrm"]), ((1, 'wszChain'),(1, 'pcCertCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMDeconstructCertificateChain():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32),POINTER(Char), use_last_error=False)(("DRMDeconstructCertificateChain", windll["msdrm"]), ((1, 'wszChain'),(1, 'iWhich'),(1, 'pcCert'),(1, 'wszCert'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMVerify():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(Char),POINTER(win32more.Data.RightsManagement.DRMATTESTTYPE),POINTER(UInt32),POINTER(Char),POINTER(UInt32),POINTER(Char), use_last_error=False)(("DRMVerify", windll["msdrm"]), ((1, 'wszData'),(1, 'pcAttestedData'),(1, 'wszAttestedData'),(1, 'peType'),(1, 'pcPrincipal'),(1, 'wszPrincipal'),(1, 'pcManifest'),(1, 'wszManifest'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMCreateUser():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(("DRMCreateUser", windll["msdrm"]), ((1, 'wszUserName'),(1, 'wszUserId'),(1, 'wszUserIdType'),(1, 'phUser'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMCreateRight():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.SYSTEMTIME_head),POINTER(win32more.Foundation.SYSTEMTIME_head),UInt32,POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.PWSTR),POINTER(UInt32), use_last_error=False)(("DRMCreateRight", windll["msdrm"]), ((1, 'wszRightName'),(1, 'pstFrom'),(1, 'pstUntil'),(1, 'cExtendedInfo'),(1, 'pwszExtendedInfoName'),(1, 'pwszExtendedInfoValue'),(1, 'phRight'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMCreateIssuanceLicense():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.SYSTEMTIME_head),POINTER(win32more.Foundation.SYSTEMTIME_head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32), use_last_error=False)(("DRMCreateIssuanceLicense", windll["msdrm"]), ((1, 'pstTimeFrom'),(1, 'pstTimeUntil'),(1, 'wszReferralInfoName'),(1, 'wszReferralInfoURL'),(1, 'hOwner'),(1, 'wszIssuanceLicense'),(1, 'hBoundLicense'),(1, 'phIssuanceLicense'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMAddRightWithUser():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32, use_last_error=False)(("DRMAddRightWithUser", windll["msdrm"]), ((1, 'hIssuanceLicense'),(1, 'hRight'),(1, 'hUser'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMClearAllRights():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(("DRMClearAllRights", windll["msdrm"]), ((1, 'hIssuanceLicense'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMSetMetaData():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("DRMSetMetaData", windll["msdrm"]), ((1, 'hIssuanceLicense'),(1, 'wszContentId'),(1, 'wszContentIdType'),(1, 'wszSKUId'),(1, 'wszSKUIdType'),(1, 'wszContentType'),(1, 'wszContentName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMSetUsagePolicy():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Data.RightsManagement.DRM_USAGEPOLICY_TYPE,win32more.Foundation.BOOL,win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,c_char_p_no,UInt32, use_last_error=False)(("DRMSetUsagePolicy", windll["msdrm"]), ((1, 'hIssuanceLicense'),(1, 'eUsagePolicyType'),(1, 'fDelete'),(1, 'fExclusion'),(1, 'wszName'),(1, 'wszMinVersion'),(1, 'wszMaxVersion'),(1, 'wszPublicKey'),(1, 'wszDigestAlgorithm'),(1, 'pbDigest'),(1, 'cbDigest'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMSetRevocationPoint():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.SYSTEMTIME_head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("DRMSetRevocationPoint", windll["msdrm"]), ((1, 'hIssuanceLicense'),(1, 'fDelete'),(1, 'wszId'),(1, 'wszIdType'),(1, 'wszURL'),(1, 'pstFrequency'),(1, 'wszName'),(1, 'wszPublicKey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMSetApplicationSpecificData():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("DRMSetApplicationSpecificData", windll["msdrm"]), ((1, 'hIssuanceLicense'),(1, 'fDelete'),(1, 'wszName'),(1, 'wszValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMSetNameAndDescription():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.BOOL,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("DRMSetNameAndDescription", windll["msdrm"]), ((1, 'hIssuanceLicense'),(1, 'fDelete'),(1, 'lcid'),(1, 'wszName'),(1, 'wszDescription'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMSetIntervalTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(("DRMSetIntervalTime", windll["msdrm"]), ((1, 'hIssuanceLicense'),(1, 'cDays'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetIssuanceLicenseTemplate():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32),POINTER(Char), use_last_error=False)(("DRMGetIssuanceLicenseTemplate", windll["msdrm"]), ((1, 'hIssuanceLicense'),(1, 'puIssuanceLicenseTemplateLength'),(1, 'wszIssuanceLicenseTemplate'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetSignedIssuanceLicense():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32,c_char_p_no,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Data.RightsManagement.DRMCALLBACK,win32more.Foundation.PWSTR,c_void_p, use_last_error=False)(("DRMGetSignedIssuanceLicense", windll["msdrm"]), ((1, 'hEnv'),(1, 'hIssuanceLicense'),(1, 'uFlags'),(1, 'pbSymKey'),(1, 'cbSymKey'),(1, 'wszSymKeyType'),(1, 'wszClientLicensorCertificate'),(1, 'pfnCallback'),(1, 'wszURL'),(1, 'pvContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetSignedIssuanceLicenseEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32,c_char_p_no,UInt32,win32more.Foundation.PWSTR,c_void_p,UInt32,UInt32,win32more.Data.RightsManagement.DRMCALLBACK,c_void_p, use_last_error=False)(("DRMGetSignedIssuanceLicenseEx", windll["msdrm"]), ((1, 'hEnv'),(1, 'hIssuanceLicense'),(1, 'uFlags'),(1, 'pbSymKey'),(1, 'cbSymKey'),(1, 'wszSymKeyType'),(1, 'pvReserved'),(1, 'hEnablingPrincipal'),(1, 'hBoundLicenseCLC'),(1, 'pfnCallback'),(1, 'pvContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMClosePubHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(("DRMClosePubHandle", windll["msdrm"]), ((1, 'hPub'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMDuplicatePubHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(("DRMDuplicatePubHandle", windll["msdrm"]), ((1, 'hPubIn'),(1, 'phPubOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetUserInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32),POINTER(Char),POINTER(UInt32),POINTER(Char),POINTER(UInt32),POINTER(Char), use_last_error=False)(("DRMGetUserInfo", windll["msdrm"]), ((1, 'hUser'),(1, 'puUserNameLength'),(1, 'wszUserName'),(1, 'puUserIdLength'),(1, 'wszUserId'),(1, 'puUserIdTypeLength'),(1, 'wszUserIdType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetRightInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32),POINTER(Char),POINTER(win32more.Foundation.SYSTEMTIME_head),POINTER(win32more.Foundation.SYSTEMTIME_head), use_last_error=False)(("DRMGetRightInfo", windll["msdrm"]), ((1, 'hRight'),(1, 'puRightNameLength'),(1, 'wszRightName'),(1, 'pstFrom'),(1, 'pstUntil'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetRightExtendedInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(UInt32),POINTER(Char),POINTER(UInt32),POINTER(Char), use_last_error=False)(("DRMGetRightExtendedInfo", windll["msdrm"]), ((1, 'hRight'),(1, 'uIndex'),(1, 'puExtendedInfoNameLength'),(1, 'wszExtendedInfoName'),(1, 'puExtendedInfoValueLength'),(1, 'wszExtendedInfoValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetUsers():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(UInt32), use_last_error=False)(("DRMGetUsers", windll["msdrm"]), ((1, 'hIssuanceLicense'),(1, 'uIndex'),(1, 'phUser'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetUserRights():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32,POINTER(UInt32), use_last_error=False)(("DRMGetUserRights", windll["msdrm"]), ((1, 'hIssuanceLicense'),(1, 'hUser'),(1, 'uIndex'),(1, 'phRight'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetMetaData():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32),POINTER(Char),POINTER(UInt32),POINTER(Char),POINTER(UInt32),POINTER(Char),POINTER(UInt32),POINTER(Char),POINTER(UInt32),POINTER(Char),POINTER(UInt32),POINTER(Char), use_last_error=False)(("DRMGetMetaData", windll["msdrm"]), ((1, 'hIssuanceLicense'),(1, 'puContentIdLength'),(1, 'wszContentId'),(1, 'puContentIdTypeLength'),(1, 'wszContentIdType'),(1, 'puSKUIdLength'),(1, 'wszSKUId'),(1, 'puSKUIdTypeLength'),(1, 'wszSKUIdType'),(1, 'puContentTypeLength'),(1, 'wszContentType'),(1, 'puContentNameLength'),(1, 'wszContentName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetApplicationSpecificData():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(UInt32),POINTER(Char),POINTER(UInt32),POINTER(Char), use_last_error=False)(("DRMGetApplicationSpecificData", windll["msdrm"]), ((1, 'hIssuanceLicense'),(1, 'uIndex'),(1, 'puNameLength'),(1, 'wszName'),(1, 'puValueLength'),(1, 'wszValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetIssuanceLicenseInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.SYSTEMTIME_head),POINTER(win32more.Foundation.SYSTEMTIME_head),UInt32,POINTER(UInt32),POINTER(Char),POINTER(UInt32),POINTER(Char),POINTER(UInt32),POINTER(win32more.Foundation.BOOL), use_last_error=False)(("DRMGetIssuanceLicenseInfo", windll["msdrm"]), ((1, 'hIssuanceLicense'),(1, 'pstTimeFrom'),(1, 'pstTimeUntil'),(1, 'uFlags'),(1, 'puDistributionPointNameLength'),(1, 'wszDistributionPointName'),(1, 'puDistributionPointURLLength'),(1, 'wszDistributionPointURL'),(1, 'phOwner'),(1, 'pfOfficial'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetRevocationPoint():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32),POINTER(Char),POINTER(UInt32),POINTER(Char),POINTER(UInt32),POINTER(Char),POINTER(win32more.Foundation.SYSTEMTIME_head),POINTER(UInt32),POINTER(Char),POINTER(UInt32),POINTER(Char), use_last_error=False)(("DRMGetRevocationPoint", windll["msdrm"]), ((1, 'hIssuanceLicense'),(1, 'puIdLength'),(1, 'wszId'),(1, 'puIdTypeLength'),(1, 'wszIdType'),(1, 'puURLLength'),(1, 'wszRL'),(1, 'pstFrequency'),(1, 'puNameLength'),(1, 'wszName'),(1, 'puPublicKeyLength'),(1, 'wszPublicKey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetUsagePolicy():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.Data.RightsManagement.DRM_USAGEPOLICY_TYPE),POINTER(win32more.Foundation.BOOL),POINTER(UInt32),POINTER(Char),POINTER(UInt32),POINTER(Char),POINTER(UInt32),POINTER(Char),POINTER(UInt32),POINTER(Char),POINTER(UInt32),POINTER(Char),POINTER(UInt32),c_char_p_no, use_last_error=False)(("DRMGetUsagePolicy", windll["msdrm"]), ((1, 'hIssuanceLicense'),(1, 'uIndex'),(1, 'peUsagePolicyType'),(1, 'pfExclusion'),(1, 'puNameLength'),(1, 'wszName'),(1, 'puMinVersionLength'),(1, 'wszMinVersion'),(1, 'puMaxVersionLength'),(1, 'wszMaxVersion'),(1, 'puPublicKeyLength'),(1, 'wszPublicKey'),(1, 'puDigestAlgorithmLength'),(1, 'wszDigestAlgorithm'),(1, 'pcbDigest'),(1, 'pbDigest'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetNameAndDescription():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(Char),POINTER(UInt32),POINTER(Char), use_last_error=False)(("DRMGetNameAndDescription", windll["msdrm"]), ((1, 'hIssuanceLicense'),(1, 'uIndex'),(1, 'pulcid'),(1, 'puNameLength'),(1, 'wszName'),(1, 'puDescriptionLength'),(1, 'wszDescription'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetOwnerLicense():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32),POINTER(Char), use_last_error=False)(("DRMGetOwnerLicense", windll["msdrm"]), ((1, 'hIssuanceLicense'),(1, 'puOwnerLicenseLength'),(1, 'wszOwnerLicense'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMGetIntervalTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(("DRMGetIntervalTime", windll["msdrm"]), ((1, 'hIssuanceLicense'),(1, 'pcDays'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMRepair():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(("DRMRepair", windll["msdrm"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMRegisterProtectedWindow():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.HWND, use_last_error=False)(("DRMRegisterProtectedWindow", windll["msdrm"]), ((1, 'hEnv'),(1, 'hwnd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMIsWindowProtected():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(win32more.Foundation.BOOL), use_last_error=False)(("DRMIsWindowProtected", windll["msdrm"]), ((1, 'hwnd'),(1, 'pfProtected'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DRMAcquireIssuanceLicenseTemplate():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,c_void_p,UInt32,POINTER(win32more.Foundation.PWSTR),win32more.Foundation.PWSTR,c_void_p, use_last_error=False)(("DRMAcquireIssuanceLicenseTemplate", windll["msdrm"]), ((1, 'hClient'),(1, 'uFlags'),(1, 'pvReserved'),(1, 'cTemplates'),(1, 'pwszTemplateIds'),(1, 'wszUrl'),(1, 'pvContext'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "DRMHANDLE_INVALID",
    "DRMENVHANDLE_INVALID",
    "DRMQUERYHANDLE_INVALID",
    "DRMHSESSION_INVALID",
    "DRMPUBHANDLE_INVALID",
    "DRM_AL_NONSILENT",
    "DRM_AL_NOPERSIST",
    "DRM_AL_CANCEL",
    "DRM_AL_FETCHNOADVISORY",
    "DRM_AL_NOUI",
    "DRM_ACTIVATE_MACHINE",
    "DRM_ACTIVATE_GROUPIDENTITY",
    "DRM_ACTIVATE_TEMPORARY",
    "DRM_ACTIVATE_CANCEL",
    "DRM_ACTIVATE_SILENT",
    "DRM_ACTIVATE_SHARED_GROUPIDENTITY",
    "DRM_ACTIVATE_DELAYED",
    "DRM_EL_MACHINE",
    "DRM_EL_GROUPIDENTITY",
    "DRM_EL_GROUPIDENTITY_NAME",
    "DRM_EL_GROUPIDENTITY_LID",
    "DRM_EL_SPECIFIED_GROUPIDENTITY",
    "DRM_EL_EUL",
    "DRM_EL_EUL_LID",
    "DRM_EL_CLIENTLICENSOR",
    "DRM_EL_CLIENTLICENSOR_LID",
    "DRM_EL_SPECIFIED_CLIENTLICENSOR",
    "DRM_EL_REVOCATIONLIST",
    "DRM_EL_REVOCATIONLIST_LID",
    "DRM_EL_EXPIRED",
    "DRM_EL_ISSUERNAME",
    "DRM_EL_ISSUANCELICENSE_TEMPLATE",
    "DRM_EL_ISSUANCELICENSE_TEMPLATE_LID",
    "DRM_ADD_LICENSE_NOPERSIST",
    "DRM_ADD_LICENSE_PERSIST",
    "DRM_SERVICE_TYPE_ACTIVATION",
    "DRM_SERVICE_TYPE_CERTIFICATION",
    "DRM_SERVICE_TYPE_PUBLISHING",
    "DRM_SERVICE_TYPE_CLIENTLICENSOR",
    "DRM_SERVICE_TYPE_SILENT",
    "DRM_SERVICE_LOCATION_INTERNET",
    "DRM_SERVICE_LOCATION_ENTERPRISE",
    "DRM_SIGN_ONLINE",
    "DRM_SIGN_OFFLINE",
    "DRM_SIGN_CANCEL",
    "DRM_SERVER_ISSUANCELICENSE",
    "DRM_AUTO_GENERATE_KEY",
    "DRM_OWNER_LICENSE_NOPERSIST",
    "DRM_REUSE_KEY",
    "DRM_LOCKBOXTYPE_NONE",
    "DRM_LOCKBOXTYPE_WHITEBOX",
    "DRM_LOCKBOXTYPE_BLACKBOX",
    "DRM_LOCKBOXTYPE_DEFAULT",
    "DRM_AILT_NONSILENT",
    "DRM_AILT_OBTAIN_ALL",
    "DRM_AILT_CANCEL",
    "MSDRM_CLIENT_ZONE",
    "MSDRM_POLICY_ZONE",
    "DRMIDVERSION",
    "DRMBOUNDLICENSEPARAMSVERSION",
    "DRMBINDINGFLAGS_IGNORE_VALIDITY_INTERVALS",
    "DRMLICENSEACQDATAVERSION",
    "DRMACTSERVINFOVERSION",
    "DRMCLIENTSTRUCTVERSION",
    "DRMCALLBACKVERSION",
    "DRMID",
    "DRMTIMETYPE",
    "DRMTIMETYPE_SYSTEMUTC",
    "DRMTIMETYPE_SYSTEMLOCAL",
    "DRMENCODINGTYPE",
    "DRMENCODINGTYPE_BASE64",
    "DRMENCODINGTYPE_STRING",
    "DRMENCODINGTYPE_LONG",
    "DRMENCODINGTYPE_TIME",
    "DRMENCODINGTYPE_UINT",
    "DRMENCODINGTYPE_RAW",
    "DRMATTESTTYPE",
    "DRMATTESTTYPE_FULLENVIRONMENT",
    "DRMATTESTTYPE_HASHONLY",
    "DRMSPECTYPE",
    "DRMSPECTYPE_UNKNOWN",
    "DRMSPECTYPE_FILENAME",
    "DRMSECURITYPROVIDERTYPE",
    "DRMSECURITYPROVIDERTYPE_SOFTWARESECREP",
    "DRMGLOBALOPTIONS",
    "DRMGLOBALOPTIONS_USE_WINHTTP",
    "DRMGLOBALOPTIONS_USE_SERVERSECURITYPROCESSOR",
    "DRMBOUNDLICENSEPARAMS",
    "DRM_LICENSE_ACQ_DATA",
    "DRM_ACTSERV_INFO",
    "DRM_CLIENT_VERSION_INFO",
    "DRM_STATUS_MSG",
    "DRM_MSG_ACTIVATE_MACHINE",
    "DRM_MSG_ACTIVATE_GROUPIDENTITY",
    "DRM_MSG_ACQUIRE_LICENSE",
    "DRM_MSG_ACQUIRE_ADVISORY",
    "DRM_MSG_SIGN_ISSUANCE_LICENSE",
    "DRM_MSG_ACQUIRE_CLIENTLICENSOR",
    "DRM_MSG_ACQUIRE_ISSUANCE_LICENSE_TEMPLATE",
    "DRM_USAGEPOLICY_TYPE",
    "DRM_USAGEPOLICY_TYPE_BYNAME",
    "DRM_USAGEPOLICY_TYPE_BYPUBLICKEY",
    "DRM_USAGEPOLICY_TYPE_BYDIGEST",
    "DRM_USAGEPOLICY_TYPE_OSEXCLUSION",
    "DRM_DISTRIBUTION_POINT_INFO",
    "DRM_DISTRIBUTION_POINT_LICENSE_ACQUISITION",
    "DRM_DISTRIBUTION_POINT_PUBLISHING",
    "DRM_DISTRIBUTION_POINT_REFERRAL_INFO",
    "DRMCALLBACK",
    "DRMSetGlobalOptions",
    "DRMGetClientVersion",
    "DRMInitEnvironment",
    "DRMLoadLibrary",
    "DRMCreateEnablingPrincipal",
    "DRMCloseHandle",
    "DRMCloseEnvironmentHandle",
    "DRMDuplicateHandle",
    "DRMDuplicateEnvironmentHandle",
    "DRMRegisterRevocationList",
    "DRMCheckSecurity",
    "DRMRegisterContent",
    "DRMEncrypt",
    "DRMDecrypt",
    "DRMCreateBoundLicense",
    "DRMCreateEnablingBitsDecryptor",
    "DRMCreateEnablingBitsEncryptor",
    "DRMAttest",
    "DRMGetTime",
    "DRMGetInfo",
    "DRMGetEnvironmentInfo",
    "DRMGetProcAddress",
    "DRMGetBoundLicenseObjectCount",
    "DRMGetBoundLicenseObject",
    "DRMGetBoundLicenseAttributeCount",
    "DRMGetBoundLicenseAttribute",
    "DRMCreateClientSession",
    "DRMIsActivated",
    "DRMActivate",
    "DRMGetServiceLocation",
    "DRMCreateLicenseStorageSession",
    "DRMAddLicense",
    "DRMAcquireAdvisories",
    "DRMEnumerateLicense",
    "DRMAcquireLicense",
    "DRMDeleteLicense",
    "DRMCloseSession",
    "DRMDuplicateSession",
    "DRMGetSecurityProvider",
    "DRMEncode",
    "DRMDecode",
    "DRMConstructCertificateChain",
    "DRMParseUnboundLicense",
    "DRMCloseQueryHandle",
    "DRMGetUnboundLicenseObjectCount",
    "DRMGetUnboundLicenseObject",
    "DRMGetUnboundLicenseAttributeCount",
    "DRMGetUnboundLicenseAttribute",
    "DRMGetCertificateChainCount",
    "DRMDeconstructCertificateChain",
    "DRMVerify",
    "DRMCreateUser",
    "DRMCreateRight",
    "DRMCreateIssuanceLicense",
    "DRMAddRightWithUser",
    "DRMClearAllRights",
    "DRMSetMetaData",
    "DRMSetUsagePolicy",
    "DRMSetRevocationPoint",
    "DRMSetApplicationSpecificData",
    "DRMSetNameAndDescription",
    "DRMSetIntervalTime",
    "DRMGetIssuanceLicenseTemplate",
    "DRMGetSignedIssuanceLicense",
    "DRMGetSignedIssuanceLicenseEx",
    "DRMClosePubHandle",
    "DRMDuplicatePubHandle",
    "DRMGetUserInfo",
    "DRMGetRightInfo",
    "DRMGetRightExtendedInfo",
    "DRMGetUsers",
    "DRMGetUserRights",
    "DRMGetMetaData",
    "DRMGetApplicationSpecificData",
    "DRMGetIssuanceLicenseInfo",
    "DRMGetRevocationPoint",
    "DRMGetUsagePolicy",
    "DRMGetNameAndDescription",
    "DRMGetOwnerLicense",
    "DRMGetIntervalTime",
    "DRMRepair",
    "DRMRegisterProtectedWindow",
    "DRMIsWindowProtected",
    "DRMAcquireIssuanceLicenseTemplate",
]
