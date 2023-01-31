from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Data.RightsManagement
import win32more.Foundation
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
DRMHANDLE_INVALID: UInt32 = 0
DRMENVHANDLE_INVALID: UInt32 = 0
DRMQUERYHANDLE_INVALID: UInt32 = 0
DRMHSESSION_INVALID: UInt32 = 0
DRMPUBHANDLE_INVALID: UInt32 = 0
DRM_AL_NONSILENT: UInt32 = 1
DRM_AL_NOPERSIST: UInt32 = 2
DRM_AL_CANCEL: UInt32 = 4
DRM_AL_FETCHNOADVISORY: UInt32 = 8
DRM_AL_NOUI: UInt32 = 16
DRM_ACTIVATE_MACHINE: UInt32 = 1
DRM_ACTIVATE_GROUPIDENTITY: UInt32 = 2
DRM_ACTIVATE_TEMPORARY: UInt32 = 4
DRM_ACTIVATE_CANCEL: UInt32 = 8
DRM_ACTIVATE_SILENT: UInt32 = 16
DRM_ACTIVATE_SHARED_GROUPIDENTITY: UInt32 = 32
DRM_ACTIVATE_DELAYED: UInt32 = 64
DRM_EL_MACHINE: UInt32 = 1
DRM_EL_GROUPIDENTITY: UInt32 = 2
DRM_EL_GROUPIDENTITY_NAME: UInt32 = 4
DRM_EL_GROUPIDENTITY_LID: UInt32 = 8
DRM_EL_SPECIFIED_GROUPIDENTITY: UInt32 = 16
DRM_EL_EUL: UInt32 = 32
DRM_EL_EUL_LID: UInt32 = 64
DRM_EL_CLIENTLICENSOR: UInt32 = 128
DRM_EL_CLIENTLICENSOR_LID: UInt32 = 256
DRM_EL_SPECIFIED_CLIENTLICENSOR: UInt32 = 512
DRM_EL_REVOCATIONLIST: UInt32 = 1024
DRM_EL_REVOCATIONLIST_LID: UInt32 = 2048
DRM_EL_EXPIRED: UInt32 = 4096
DRM_EL_ISSUERNAME: UInt32 = 8192
DRM_EL_ISSUANCELICENSE_TEMPLATE: UInt32 = 16384
DRM_EL_ISSUANCELICENSE_TEMPLATE_LID: UInt32 = 32768
DRM_ADD_LICENSE_NOPERSIST: UInt32 = 0
DRM_ADD_LICENSE_PERSIST: UInt32 = 1
DRM_SERVICE_TYPE_ACTIVATION: UInt32 = 1
DRM_SERVICE_TYPE_CERTIFICATION: UInt32 = 2
DRM_SERVICE_TYPE_PUBLISHING: UInt32 = 4
DRM_SERVICE_TYPE_CLIENTLICENSOR: UInt32 = 8
DRM_SERVICE_TYPE_SILENT: UInt32 = 16
DRM_SERVICE_LOCATION_INTERNET: UInt32 = 1
DRM_SERVICE_LOCATION_ENTERPRISE: UInt32 = 2
DRM_DEFAULTGROUPIDTYPE_WINDOWSAUTH: String = 'WindowsAuthProvider'
DRM_DEFAULTGROUPIDTYPE_PASSPORT: String = 'PassportAuthProvider'
DRM_SIGN_ONLINE: UInt32 = 1
DRM_SIGN_OFFLINE: UInt32 = 2
DRM_SIGN_CANCEL: UInt32 = 4
DRM_SERVER_ISSUANCELICENSE: UInt32 = 8
DRM_AUTO_GENERATE_KEY: UInt32 = 16
DRM_OWNER_LICENSE_NOPERSIST: UInt32 = 32
DRM_REUSE_KEY: UInt32 = 64
DRM_LOCKBOXTYPE_NONE: UInt32 = 0
DRM_LOCKBOXTYPE_WHITEBOX: UInt32 = 1
DRM_LOCKBOXTYPE_BLACKBOX: UInt32 = 2
DRM_LOCKBOXTYPE_DEFAULT: UInt32 = 2
DRM_AILT_NONSILENT: UInt32 = 1
DRM_AILT_OBTAIN_ALL: UInt32 = 2
DRM_AILT_CANCEL: UInt32 = 4
MSDRM_CLIENT_ZONE: UInt32 = 52992
MSDRM_POLICY_ZONE: UInt32 = 37632
DRMIDVERSION: UInt32 = 0
DRMBOUNDLICENSEPARAMSVERSION: UInt32 = 1
DRMBINDINGFLAGS_IGNORE_VALIDITY_INTERVALS: UInt32 = 1
DRMLICENSEACQDATAVERSION: UInt32 = 0
DRMACTSERVINFOVERSION: UInt32 = 0
DRMCLIENTSTRUCTVERSION: UInt32 = 1
DRMCALLBACKVERSION: UInt32 = 1
@winfunctype('msdrm.dll')
def DRMSetGlobalOptions(eGlobalOptions: win32more.Data.RightsManagement.DRMGLOBALOPTIONS, pvdata: c_void_p, dwlen: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetClientVersion(pDRMClientVersionInfo: POINTER(win32more.Data.RightsManagement.DRM_CLIENT_VERSION_INFO_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMInitEnvironment(eSecurityProviderType: win32more.Data.RightsManagement.DRMSECURITYPROVIDERTYPE, eSpecification: win32more.Data.RightsManagement.DRMSPECTYPE, wszSecurityProvider: win32more.Foundation.PWSTR, wszManifestCredentials: win32more.Foundation.PWSTR, wszMachineCredentials: win32more.Foundation.PWSTR, phEnv: POINTER(UInt32), phDefaultLibrary: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMLoadLibrary(hEnv: UInt32, eSpecification: win32more.Data.RightsManagement.DRMSPECTYPE, wszLibraryProvider: win32more.Foundation.PWSTR, wszCredentials: win32more.Foundation.PWSTR, phLibrary: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMCreateEnablingPrincipal(hEnv: UInt32, hLibrary: UInt32, wszObject: win32more.Foundation.PWSTR, pidPrincipal: POINTER(win32more.Data.RightsManagement.DRMID_head), wszCredentials: win32more.Foundation.PWSTR, phEnablingPrincipal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMCloseHandle(handle: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMCloseEnvironmentHandle(hEnv: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMDuplicateHandle(hToCopy: UInt32, phCopy: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMDuplicateEnvironmentHandle(hToCopy: UInt32, phCopy: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMRegisterRevocationList(hEnv: UInt32, wszRevocationList: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMCheckSecurity(hEnv: UInt32, cLevel: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMRegisterContent(fRegister: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMEncrypt(hCryptoProvider: UInt32, iPosition: UInt32, cNumInBytes: UInt32, pbInData: c_char_p_no, pcNumOutBytes: POINTER(UInt32), pbOutData: c_char_p_no) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMDecrypt(hCryptoProvider: UInt32, iPosition: UInt32, cNumInBytes: UInt32, pbInData: c_char_p_no, pcNumOutBytes: POINTER(UInt32), pbOutData: c_char_p_no) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMCreateBoundLicense(hEnv: UInt32, pParams: POINTER(win32more.Data.RightsManagement.DRMBOUNDLICENSEPARAMS_head), wszLicenseChain: win32more.Foundation.PWSTR, phBoundLicense: POINTER(UInt32), phErrorLog: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMCreateEnablingBitsDecryptor(hBoundLicense: UInt32, wszRight: win32more.Foundation.PWSTR, hAuxLib: UInt32, wszAuxPlug: win32more.Foundation.PWSTR, phDecryptor: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMCreateEnablingBitsEncryptor(hBoundLicense: UInt32, wszRight: win32more.Foundation.PWSTR, hAuxLib: UInt32, wszAuxPlug: win32more.Foundation.PWSTR, phEncryptor: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMAttest(hEnablingPrincipal: UInt32, wszData: win32more.Foundation.PWSTR, eType: win32more.Data.RightsManagement.DRMATTESTTYPE, pcAttestedBlob: POINTER(UInt32), wszAttestedBlob: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetTime(hEnv: UInt32, eTimerIdType: win32more.Data.RightsManagement.DRMTIMETYPE, poTimeObject: POINTER(win32more.Foundation.SYSTEMTIME_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetInfo(handle: UInt32, wszAttribute: win32more.Foundation.PWSTR, peEncoding: POINTER(win32more.Data.RightsManagement.DRMENCODINGTYPE), pcBuffer: POINTER(UInt32), pbBuffer: c_char_p_no) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetEnvironmentInfo(handle: UInt32, wszAttribute: win32more.Foundation.PWSTR, peEncoding: POINTER(win32more.Data.RightsManagement.DRMENCODINGTYPE), pcBuffer: POINTER(UInt32), pbBuffer: c_char_p_no) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetProcAddress(hLibrary: UInt32, wszProcName: win32more.Foundation.PWSTR, ppfnProcAddress: POINTER(win32more.Foundation.FARPROC)) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetBoundLicenseObjectCount(hQueryRoot: UInt32, wszSubObjectType: win32more.Foundation.PWSTR, pcSubObjects: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetBoundLicenseObject(hQueryRoot: UInt32, wszSubObjectType: win32more.Foundation.PWSTR, iWhich: UInt32, phSubObject: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetBoundLicenseAttributeCount(hQueryRoot: UInt32, wszAttribute: win32more.Foundation.PWSTR, pcAttributes: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetBoundLicenseAttribute(hQueryRoot: UInt32, wszAttribute: win32more.Foundation.PWSTR, iWhich: UInt32, peEncoding: POINTER(win32more.Data.RightsManagement.DRMENCODINGTYPE), pcBuffer: POINTER(UInt32), pbBuffer: c_char_p_no) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMCreateClientSession(pfnCallback: win32more.Data.RightsManagement.DRMCALLBACK, uCallbackVersion: UInt32, wszGroupIDProviderType: win32more.Foundation.PWSTR, wszGroupID: win32more.Foundation.PWSTR, phClient: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMIsActivated(hClient: UInt32, uFlags: UInt32, pActServInfo: POINTER(win32more.Data.RightsManagement.DRM_ACTSERV_INFO_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMActivate(hClient: UInt32, uFlags: UInt32, uLangID: UInt32, pActServInfo: POINTER(win32more.Data.RightsManagement.DRM_ACTSERV_INFO_head), pvContext: c_void_p, hParentWnd: win32more.Foundation.HWND) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetServiceLocation(hClient: UInt32, uServiceType: UInt32, uServiceLocation: UInt32, wszIssuanceLicense: win32more.Foundation.PWSTR, puServiceURLLength: POINTER(UInt32), wszServiceURL: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMCreateLicenseStorageSession(hEnv: UInt32, hDefaultLibrary: UInt32, hClient: UInt32, uFlags: UInt32, wszIssuanceLicense: win32more.Foundation.PWSTR, phLicenseStorage: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMAddLicense(hLicenseStorage: UInt32, uFlags: UInt32, wszLicense: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMAcquireAdvisories(hLicenseStorage: UInt32, wszLicense: win32more.Foundation.PWSTR, wszURL: win32more.Foundation.PWSTR, pvContext: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMEnumerateLicense(hSession: UInt32, uFlags: UInt32, uIndex: UInt32, pfSharedFlag: POINTER(win32more.Foundation.BOOL), puCertificateDataLen: POINTER(UInt32), wszCertificateData: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMAcquireLicense(hSession: UInt32, uFlags: UInt32, wszGroupIdentityCredential: win32more.Foundation.PWSTR, wszRequestedRights: win32more.Foundation.PWSTR, wszCustomData: win32more.Foundation.PWSTR, wszURL: win32more.Foundation.PWSTR, pvContext: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMDeleteLicense(hSession: UInt32, wszLicenseId: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMCloseSession(hSession: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMDuplicateSession(hSessionIn: UInt32, phSessionOut: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetSecurityProvider(uFlags: UInt32, puTypeLen: POINTER(UInt32), wszType: win32more.Foundation.PWSTR, puPathLen: POINTER(UInt32), wszPath: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMEncode(wszAlgID: win32more.Foundation.PWSTR, uDataLen: UInt32, pbDecodedData: c_char_p_no, puEncodedStringLen: POINTER(UInt32), wszEncodedString: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMDecode(wszAlgID: win32more.Foundation.PWSTR, wszEncodedString: win32more.Foundation.PWSTR, puDecodedDataLen: POINTER(UInt32), pbDecodedData: c_char_p_no) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMConstructCertificateChain(cCertificates: UInt32, rgwszCertificates: POINTER(win32more.Foundation.PWSTR), pcChain: POINTER(UInt32), wszChain: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMParseUnboundLicense(wszCertificate: win32more.Foundation.PWSTR, phQueryRoot: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMCloseQueryHandle(hQuery: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetUnboundLicenseObjectCount(hQueryRoot: UInt32, wszSubObjectType: win32more.Foundation.PWSTR, pcSubObjects: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetUnboundLicenseObject(hQueryRoot: UInt32, wszSubObjectType: win32more.Foundation.PWSTR, iIndex: UInt32, phSubQuery: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetUnboundLicenseAttributeCount(hQueryRoot: UInt32, wszAttributeType: win32more.Foundation.PWSTR, pcAttributes: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetUnboundLicenseAttribute(hQueryRoot: UInt32, wszAttributeType: win32more.Foundation.PWSTR, iWhich: UInt32, peEncoding: POINTER(win32more.Data.RightsManagement.DRMENCODINGTYPE), pcBuffer: POINTER(UInt32), pbBuffer: c_char_p_no) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetCertificateChainCount(wszChain: win32more.Foundation.PWSTR, pcCertCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMDeconstructCertificateChain(wszChain: win32more.Foundation.PWSTR, iWhich: UInt32, pcCert: POINTER(UInt32), wszCert: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMVerify(wszData: win32more.Foundation.PWSTR, pcAttestedData: POINTER(UInt32), wszAttestedData: win32more.Foundation.PWSTR, peType: POINTER(win32more.Data.RightsManagement.DRMATTESTTYPE), pcPrincipal: POINTER(UInt32), wszPrincipal: win32more.Foundation.PWSTR, pcManifest: POINTER(UInt32), wszManifest: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMCreateUser(wszUserName: win32more.Foundation.PWSTR, wszUserId: win32more.Foundation.PWSTR, wszUserIdType: win32more.Foundation.PWSTR, phUser: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMCreateRight(wszRightName: win32more.Foundation.PWSTR, pstFrom: POINTER(win32more.Foundation.SYSTEMTIME_head), pstUntil: POINTER(win32more.Foundation.SYSTEMTIME_head), cExtendedInfo: UInt32, pwszExtendedInfoName: POINTER(win32more.Foundation.PWSTR), pwszExtendedInfoValue: POINTER(win32more.Foundation.PWSTR), phRight: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMCreateIssuanceLicense(pstTimeFrom: POINTER(win32more.Foundation.SYSTEMTIME_head), pstTimeUntil: POINTER(win32more.Foundation.SYSTEMTIME_head), wszReferralInfoName: win32more.Foundation.PWSTR, wszReferralInfoURL: win32more.Foundation.PWSTR, hOwner: UInt32, wszIssuanceLicense: win32more.Foundation.PWSTR, hBoundLicense: UInt32, phIssuanceLicense: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMAddRightWithUser(hIssuanceLicense: UInt32, hRight: UInt32, hUser: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMClearAllRights(hIssuanceLicense: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMSetMetaData(hIssuanceLicense: UInt32, wszContentId: win32more.Foundation.PWSTR, wszContentIdType: win32more.Foundation.PWSTR, wszSKUId: win32more.Foundation.PWSTR, wszSKUIdType: win32more.Foundation.PWSTR, wszContentType: win32more.Foundation.PWSTR, wszContentName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMSetUsagePolicy(hIssuanceLicense: UInt32, eUsagePolicyType: win32more.Data.RightsManagement.DRM_USAGEPOLICY_TYPE, fDelete: win32more.Foundation.BOOL, fExclusion: win32more.Foundation.BOOL, wszName: win32more.Foundation.PWSTR, wszMinVersion: win32more.Foundation.PWSTR, wszMaxVersion: win32more.Foundation.PWSTR, wszPublicKey: win32more.Foundation.PWSTR, wszDigestAlgorithm: win32more.Foundation.PWSTR, pbDigest: c_char_p_no, cbDigest: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMSetRevocationPoint(hIssuanceLicense: UInt32, fDelete: win32more.Foundation.BOOL, wszId: win32more.Foundation.PWSTR, wszIdType: win32more.Foundation.PWSTR, wszURL: win32more.Foundation.PWSTR, pstFrequency: POINTER(win32more.Foundation.SYSTEMTIME_head), wszName: win32more.Foundation.PWSTR, wszPublicKey: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMSetApplicationSpecificData(hIssuanceLicense: UInt32, fDelete: win32more.Foundation.BOOL, wszName: win32more.Foundation.PWSTR, wszValue: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMSetNameAndDescription(hIssuanceLicense: UInt32, fDelete: win32more.Foundation.BOOL, lcid: UInt32, wszName: win32more.Foundation.PWSTR, wszDescription: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMSetIntervalTime(hIssuanceLicense: UInt32, cDays: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetIssuanceLicenseTemplate(hIssuanceLicense: UInt32, puIssuanceLicenseTemplateLength: POINTER(UInt32), wszIssuanceLicenseTemplate: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetSignedIssuanceLicense(hEnv: UInt32, hIssuanceLicense: UInt32, uFlags: UInt32, pbSymKey: c_char_p_no, cbSymKey: UInt32, wszSymKeyType: win32more.Foundation.PWSTR, wszClientLicensorCertificate: win32more.Foundation.PWSTR, pfnCallback: win32more.Data.RightsManagement.DRMCALLBACK, wszURL: win32more.Foundation.PWSTR, pvContext: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetSignedIssuanceLicenseEx(hEnv: UInt32, hIssuanceLicense: UInt32, uFlags: UInt32, pbSymKey: c_char_p_no, cbSymKey: UInt32, wszSymKeyType: win32more.Foundation.PWSTR, pvReserved: c_void_p, hEnablingPrincipal: UInt32, hBoundLicenseCLC: UInt32, pfnCallback: win32more.Data.RightsManagement.DRMCALLBACK, pvContext: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMClosePubHandle(hPub: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMDuplicatePubHandle(hPubIn: UInt32, phPubOut: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetUserInfo(hUser: UInt32, puUserNameLength: POINTER(UInt32), wszUserName: win32more.Foundation.PWSTR, puUserIdLength: POINTER(UInt32), wszUserId: win32more.Foundation.PWSTR, puUserIdTypeLength: POINTER(UInt32), wszUserIdType: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetRightInfo(hRight: UInt32, puRightNameLength: POINTER(UInt32), wszRightName: win32more.Foundation.PWSTR, pstFrom: POINTER(win32more.Foundation.SYSTEMTIME_head), pstUntil: POINTER(win32more.Foundation.SYSTEMTIME_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetRightExtendedInfo(hRight: UInt32, uIndex: UInt32, puExtendedInfoNameLength: POINTER(UInt32), wszExtendedInfoName: win32more.Foundation.PWSTR, puExtendedInfoValueLength: POINTER(UInt32), wszExtendedInfoValue: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetUsers(hIssuanceLicense: UInt32, uIndex: UInt32, phUser: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetUserRights(hIssuanceLicense: UInt32, hUser: UInt32, uIndex: UInt32, phRight: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetMetaData(hIssuanceLicense: UInt32, puContentIdLength: POINTER(UInt32), wszContentId: win32more.Foundation.PWSTR, puContentIdTypeLength: POINTER(UInt32), wszContentIdType: win32more.Foundation.PWSTR, puSKUIdLength: POINTER(UInt32), wszSKUId: win32more.Foundation.PWSTR, puSKUIdTypeLength: POINTER(UInt32), wszSKUIdType: win32more.Foundation.PWSTR, puContentTypeLength: POINTER(UInt32), wszContentType: win32more.Foundation.PWSTR, puContentNameLength: POINTER(UInt32), wszContentName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetApplicationSpecificData(hIssuanceLicense: UInt32, uIndex: UInt32, puNameLength: POINTER(UInt32), wszName: win32more.Foundation.PWSTR, puValueLength: POINTER(UInt32), wszValue: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetIssuanceLicenseInfo(hIssuanceLicense: UInt32, pstTimeFrom: POINTER(win32more.Foundation.SYSTEMTIME_head), pstTimeUntil: POINTER(win32more.Foundation.SYSTEMTIME_head), uFlags: UInt32, puDistributionPointNameLength: POINTER(UInt32), wszDistributionPointName: win32more.Foundation.PWSTR, puDistributionPointURLLength: POINTER(UInt32), wszDistributionPointURL: win32more.Foundation.PWSTR, phOwner: POINTER(UInt32), pfOfficial: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetRevocationPoint(hIssuanceLicense: UInt32, puIdLength: POINTER(UInt32), wszId: win32more.Foundation.PWSTR, puIdTypeLength: POINTER(UInt32), wszIdType: win32more.Foundation.PWSTR, puURLLength: POINTER(UInt32), wszRL: win32more.Foundation.PWSTR, pstFrequency: POINTER(win32more.Foundation.SYSTEMTIME_head), puNameLength: POINTER(UInt32), wszName: win32more.Foundation.PWSTR, puPublicKeyLength: POINTER(UInt32), wszPublicKey: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetUsagePolicy(hIssuanceLicense: UInt32, uIndex: UInt32, peUsagePolicyType: POINTER(win32more.Data.RightsManagement.DRM_USAGEPOLICY_TYPE), pfExclusion: POINTER(win32more.Foundation.BOOL), puNameLength: POINTER(UInt32), wszName: win32more.Foundation.PWSTR, puMinVersionLength: POINTER(UInt32), wszMinVersion: win32more.Foundation.PWSTR, puMaxVersionLength: POINTER(UInt32), wszMaxVersion: win32more.Foundation.PWSTR, puPublicKeyLength: POINTER(UInt32), wszPublicKey: win32more.Foundation.PWSTR, puDigestAlgorithmLength: POINTER(UInt32), wszDigestAlgorithm: win32more.Foundation.PWSTR, pcbDigest: POINTER(UInt32), pbDigest: c_char_p_no) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetNameAndDescription(hIssuanceLicense: UInt32, uIndex: UInt32, pulcid: POINTER(UInt32), puNameLength: POINTER(UInt32), wszName: win32more.Foundation.PWSTR, puDescriptionLength: POINTER(UInt32), wszDescription: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetOwnerLicense(hIssuanceLicense: UInt32, puOwnerLicenseLength: POINTER(UInt32), wszOwnerLicense: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetIntervalTime(hIssuanceLicense: UInt32, pcDays: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMRepair() -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMRegisterProtectedWindow(hEnv: UInt32, hwnd: win32more.Foundation.HWND) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMIsWindowProtected(hwnd: win32more.Foundation.HWND, pfProtected: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMAcquireIssuanceLicenseTemplate(hClient: UInt32, uFlags: UInt32, pvReserved: c_void_p, cTemplates: UInt32, pwszTemplateIds: POINTER(win32more.Foundation.PWSTR), wszUrl: win32more.Foundation.PWSTR, pvContext: c_void_p) -> win32more.Foundation.HRESULT: ...
DRMATTESTTYPE = Int32
DRMATTESTTYPE_FULLENVIRONMENT: DRMATTESTTYPE = 0
DRMATTESTTYPE_HASHONLY: DRMATTESTTYPE = 1
class DRMBOUNDLICENSEPARAMS(Structure):
    uVersion: UInt32
    hEnablingPrincipal: UInt32
    hSecureStore: UInt32
    wszRightsRequested: win32more.Foundation.PWSTR
    wszRightsGroup: win32more.Foundation.PWSTR
    idResource: win32more.Data.RightsManagement.DRMID
    cAuthenticatorCount: UInt32
    rghAuthenticators: POINTER(UInt32)
    wszDefaultEnablingPrincipalCredentials: win32more.Foundation.PWSTR
    dwFlags: UInt32
@winfunctype_pointer
def DRMCALLBACK(param0: win32more.Data.RightsManagement.DRM_STATUS_MSG, param1: win32more.Foundation.HRESULT, param2: c_void_p, param3: c_void_p) -> win32more.Foundation.HRESULT: ...
DRMENCODINGTYPE = Int32
DRMENCODINGTYPE_BASE64: DRMENCODINGTYPE = 0
DRMENCODINGTYPE_STRING: DRMENCODINGTYPE = 1
DRMENCODINGTYPE_LONG: DRMENCODINGTYPE = 2
DRMENCODINGTYPE_TIME: DRMENCODINGTYPE = 3
DRMENCODINGTYPE_UINT: DRMENCODINGTYPE = 4
DRMENCODINGTYPE_RAW: DRMENCODINGTYPE = 5
DRMGLOBALOPTIONS = Int32
DRMGLOBALOPTIONS_USE_WINHTTP: DRMGLOBALOPTIONS = 0
DRMGLOBALOPTIONS_USE_SERVERSECURITYPROCESSOR: DRMGLOBALOPTIONS = 1
class DRMID(Structure):
    uVersion: UInt32
    wszIDType: win32more.Foundation.PWSTR
    wszID: win32more.Foundation.PWSTR
DRMSECURITYPROVIDERTYPE = Int32
DRMSECURITYPROVIDERTYPE_SOFTWARESECREP: DRMSECURITYPROVIDERTYPE = 0
DRMSPECTYPE = Int32
DRMSPECTYPE_UNKNOWN: DRMSPECTYPE = 0
DRMSPECTYPE_FILENAME: DRMSPECTYPE = 1
DRMTIMETYPE = Int32
DRMTIMETYPE_SYSTEMUTC: DRMTIMETYPE = 0
DRMTIMETYPE_SYSTEMLOCAL: DRMTIMETYPE = 1
class DRM_ACTSERV_INFO(Structure):
    uVersion: UInt32
    wszPubKey: win32more.Foundation.PWSTR
    wszURL: win32more.Foundation.PWSTR
class DRM_CLIENT_VERSION_INFO(Structure):
    uStructVersion: UInt32
    dwVersion: UInt32 * 4
    wszHierarchy: Char * 256
    wszProductId: Char * 256
    wszProductDescription: Char * 256
DRM_DISTRIBUTION_POINT_INFO = Int32
DRM_DISTRIBUTION_POINT_LICENSE_ACQUISITION: DRM_DISTRIBUTION_POINT_INFO = 0
DRM_DISTRIBUTION_POINT_PUBLISHING: DRM_DISTRIBUTION_POINT_INFO = 1
DRM_DISTRIBUTION_POINT_REFERRAL_INFO: DRM_DISTRIBUTION_POINT_INFO = 2
class DRM_LICENSE_ACQ_DATA(Structure):
    uVersion: UInt32
    wszURL: win32more.Foundation.PWSTR
    wszLocalFilename: win32more.Foundation.PWSTR
    pbPostData: c_char_p_no
    dwPostDataSize: UInt32
    wszFriendlyName: win32more.Foundation.PWSTR
DRM_STATUS_MSG = Int32
DRM_MSG_ACTIVATE_MACHINE: DRM_STATUS_MSG = 0
DRM_MSG_ACTIVATE_GROUPIDENTITY: DRM_STATUS_MSG = 1
DRM_MSG_ACQUIRE_LICENSE: DRM_STATUS_MSG = 2
DRM_MSG_ACQUIRE_ADVISORY: DRM_STATUS_MSG = 3
DRM_MSG_SIGN_ISSUANCE_LICENSE: DRM_STATUS_MSG = 4
DRM_MSG_ACQUIRE_CLIENTLICENSOR: DRM_STATUS_MSG = 5
DRM_MSG_ACQUIRE_ISSUANCE_LICENSE_TEMPLATE: DRM_STATUS_MSG = 6
DRM_USAGEPOLICY_TYPE = Int32
DRM_USAGEPOLICY_TYPE_BYNAME: DRM_USAGEPOLICY_TYPE = 0
DRM_USAGEPOLICY_TYPE_BYPUBLICKEY: DRM_USAGEPOLICY_TYPE = 1
DRM_USAGEPOLICY_TYPE_BYDIGEST: DRM_USAGEPOLICY_TYPE = 2
DRM_USAGEPOLICY_TYPE_OSEXCLUSION: DRM_USAGEPOLICY_TYPE = 3
make_head(_module, 'DRMBOUNDLICENSEPARAMS')
make_head(_module, 'DRMCALLBACK')
make_head(_module, 'DRMID')
make_head(_module, 'DRM_ACTSERV_INFO')
make_head(_module, 'DRM_CLIENT_VERSION_INFO')
make_head(_module, 'DRM_LICENSE_ACQ_DATA')
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
_arch_optional = [
]
