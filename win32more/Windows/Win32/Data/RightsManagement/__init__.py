from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Data.RightsManagement
import win32more.Windows.Win32.Foundation
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
def DRMSetGlobalOptions(eGlobalOptions: win32more.Windows.Win32.Data.RightsManagement.DRMGLOBALOPTIONS, pvdata: VoidPtr, dwlen: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetClientVersion(pDRMClientVersionInfo: POINTER(win32more.Windows.Win32.Data.RightsManagement.DRM_CLIENT_VERSION_INFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMInitEnvironment(eSecurityProviderType: win32more.Windows.Win32.Data.RightsManagement.DRMSECURITYPROVIDERTYPE, eSpecification: win32more.Windows.Win32.Data.RightsManagement.DRMSPECTYPE, wszSecurityProvider: win32more.Windows.Win32.Foundation.PWSTR, wszManifestCredentials: win32more.Windows.Win32.Foundation.PWSTR, wszMachineCredentials: win32more.Windows.Win32.Foundation.PWSTR, phEnv: POINTER(UInt32), phDefaultLibrary: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMLoadLibrary(hEnv: UInt32, eSpecification: win32more.Windows.Win32.Data.RightsManagement.DRMSPECTYPE, wszLibraryProvider: win32more.Windows.Win32.Foundation.PWSTR, wszCredentials: win32more.Windows.Win32.Foundation.PWSTR, phLibrary: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMCreateEnablingPrincipal(hEnv: UInt32, hLibrary: UInt32, wszObject: win32more.Windows.Win32.Foundation.PWSTR, pidPrincipal: POINTER(win32more.Windows.Win32.Data.RightsManagement.DRMID), wszCredentials: win32more.Windows.Win32.Foundation.PWSTR, phEnablingPrincipal: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMCloseHandle(handle: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMCloseEnvironmentHandle(hEnv: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMDuplicateHandle(hToCopy: UInt32, phCopy: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMDuplicateEnvironmentHandle(hToCopy: UInt32, phCopy: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMRegisterRevocationList(hEnv: UInt32, wszRevocationList: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMCheckSecurity(hEnv: UInt32, cLevel: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMRegisterContent(fRegister: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMEncrypt(hCryptoProvider: UInt32, iPosition: UInt32, cNumInBytes: UInt32, pbInData: POINTER(Byte), pcNumOutBytes: POINTER(UInt32), pbOutData: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMDecrypt(hCryptoProvider: UInt32, iPosition: UInt32, cNumInBytes: UInt32, pbInData: POINTER(Byte), pcNumOutBytes: POINTER(UInt32), pbOutData: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMCreateBoundLicense(hEnv: UInt32, pParams: POINTER(win32more.Windows.Win32.Data.RightsManagement.DRMBOUNDLICENSEPARAMS), wszLicenseChain: win32more.Windows.Win32.Foundation.PWSTR, phBoundLicense: POINTER(UInt32), phErrorLog: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMCreateEnablingBitsDecryptor(hBoundLicense: UInt32, wszRight: win32more.Windows.Win32.Foundation.PWSTR, hAuxLib: UInt32, wszAuxPlug: win32more.Windows.Win32.Foundation.PWSTR, phDecryptor: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMCreateEnablingBitsEncryptor(hBoundLicense: UInt32, wszRight: win32more.Windows.Win32.Foundation.PWSTR, hAuxLib: UInt32, wszAuxPlug: win32more.Windows.Win32.Foundation.PWSTR, phEncryptor: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMAttest(hEnablingPrincipal: UInt32, wszData: win32more.Windows.Win32.Foundation.PWSTR, eType: win32more.Windows.Win32.Data.RightsManagement.DRMATTESTTYPE, pcAttestedBlob: POINTER(UInt32), wszAttestedBlob: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetTime(hEnv: UInt32, eTimerIdType: win32more.Windows.Win32.Data.RightsManagement.DRMTIMETYPE, poTimeObject: POINTER(win32more.Windows.Win32.Foundation.SYSTEMTIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetInfo(handle: UInt32, wszAttribute: win32more.Windows.Win32.Foundation.PWSTR, peEncoding: POINTER(win32more.Windows.Win32.Data.RightsManagement.DRMENCODINGTYPE), pcBuffer: POINTER(UInt32), pbBuffer: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetEnvironmentInfo(handle: UInt32, wszAttribute: win32more.Windows.Win32.Foundation.PWSTR, peEncoding: POINTER(win32more.Windows.Win32.Data.RightsManagement.DRMENCODINGTYPE), pcBuffer: POINTER(UInt32), pbBuffer: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetProcAddress(hLibrary: UInt32, wszProcName: win32more.Windows.Win32.Foundation.PWSTR, ppfnProcAddress: POINTER(win32more.Windows.Win32.Foundation.FARPROC)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetBoundLicenseObjectCount(hQueryRoot: UInt32, wszSubObjectType: win32more.Windows.Win32.Foundation.PWSTR, pcSubObjects: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetBoundLicenseObject(hQueryRoot: UInt32, wszSubObjectType: win32more.Windows.Win32.Foundation.PWSTR, iWhich: UInt32, phSubObject: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetBoundLicenseAttributeCount(hQueryRoot: UInt32, wszAttribute: win32more.Windows.Win32.Foundation.PWSTR, pcAttributes: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetBoundLicenseAttribute(hQueryRoot: UInt32, wszAttribute: win32more.Windows.Win32.Foundation.PWSTR, iWhich: UInt32, peEncoding: POINTER(win32more.Windows.Win32.Data.RightsManagement.DRMENCODINGTYPE), pcBuffer: POINTER(UInt32), pbBuffer: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMCreateClientSession(pfnCallback: win32more.Windows.Win32.Data.RightsManagement.DRMCALLBACK, uCallbackVersion: UInt32, wszGroupIDProviderType: win32more.Windows.Win32.Foundation.PWSTR, wszGroupID: win32more.Windows.Win32.Foundation.PWSTR, phClient: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMIsActivated(hClient: UInt32, uFlags: UInt32, pActServInfo: POINTER(win32more.Windows.Win32.Data.RightsManagement.DRM_ACTSERV_INFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMActivate(hClient: UInt32, uFlags: UInt32, uLangID: UInt32, pActServInfo: POINTER(win32more.Windows.Win32.Data.RightsManagement.DRM_ACTSERV_INFO), pvContext: VoidPtr, hParentWnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetServiceLocation(hClient: UInt32, uServiceType: UInt32, uServiceLocation: UInt32, wszIssuanceLicense: win32more.Windows.Win32.Foundation.PWSTR, puServiceURLLength: POINTER(UInt32), wszServiceURL: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMCreateLicenseStorageSession(hEnv: UInt32, hDefaultLibrary: UInt32, hClient: UInt32, uFlags: UInt32, wszIssuanceLicense: win32more.Windows.Win32.Foundation.PWSTR, phLicenseStorage: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMAddLicense(hLicenseStorage: UInt32, uFlags: UInt32, wszLicense: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMAcquireAdvisories(hLicenseStorage: UInt32, wszLicense: win32more.Windows.Win32.Foundation.PWSTR, wszURL: win32more.Windows.Win32.Foundation.PWSTR, pvContext: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMEnumerateLicense(hSession: UInt32, uFlags: UInt32, uIndex: UInt32, pfSharedFlag: POINTER(win32more.Windows.Win32.Foundation.BOOL), puCertificateDataLen: POINTER(UInt32), wszCertificateData: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMAcquireLicense(hSession: UInt32, uFlags: UInt32, wszGroupIdentityCredential: win32more.Windows.Win32.Foundation.PWSTR, wszRequestedRights: win32more.Windows.Win32.Foundation.PWSTR, wszCustomData: win32more.Windows.Win32.Foundation.PWSTR, wszURL: win32more.Windows.Win32.Foundation.PWSTR, pvContext: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMDeleteLicense(hSession: UInt32, wszLicenseId: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMCloseSession(hSession: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMDuplicateSession(hSessionIn: UInt32, phSessionOut: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetSecurityProvider(uFlags: UInt32, puTypeLen: POINTER(UInt32), wszType: win32more.Windows.Win32.Foundation.PWSTR, puPathLen: POINTER(UInt32), wszPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMEncode(wszAlgID: win32more.Windows.Win32.Foundation.PWSTR, uDataLen: UInt32, pbDecodedData: POINTER(Byte), puEncodedStringLen: POINTER(UInt32), wszEncodedString: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMDecode(wszAlgID: win32more.Windows.Win32.Foundation.PWSTR, wszEncodedString: win32more.Windows.Win32.Foundation.PWSTR, puDecodedDataLen: POINTER(UInt32), pbDecodedData: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMConstructCertificateChain(cCertificates: UInt32, rgwszCertificates: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pcChain: POINTER(UInt32), wszChain: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMParseUnboundLicense(wszCertificate: win32more.Windows.Win32.Foundation.PWSTR, phQueryRoot: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMCloseQueryHandle(hQuery: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetUnboundLicenseObjectCount(hQueryRoot: UInt32, wszSubObjectType: win32more.Windows.Win32.Foundation.PWSTR, pcSubObjects: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetUnboundLicenseObject(hQueryRoot: UInt32, wszSubObjectType: win32more.Windows.Win32.Foundation.PWSTR, iIndex: UInt32, phSubQuery: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetUnboundLicenseAttributeCount(hQueryRoot: UInt32, wszAttributeType: win32more.Windows.Win32.Foundation.PWSTR, pcAttributes: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetUnboundLicenseAttribute(hQueryRoot: UInt32, wszAttributeType: win32more.Windows.Win32.Foundation.PWSTR, iWhich: UInt32, peEncoding: POINTER(win32more.Windows.Win32.Data.RightsManagement.DRMENCODINGTYPE), pcBuffer: POINTER(UInt32), pbBuffer: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetCertificateChainCount(wszChain: win32more.Windows.Win32.Foundation.PWSTR, pcCertCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMDeconstructCertificateChain(wszChain: win32more.Windows.Win32.Foundation.PWSTR, iWhich: UInt32, pcCert: POINTER(UInt32), wszCert: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMVerify(wszData: win32more.Windows.Win32.Foundation.PWSTR, pcAttestedData: POINTER(UInt32), wszAttestedData: win32more.Windows.Win32.Foundation.PWSTR, peType: POINTER(win32more.Windows.Win32.Data.RightsManagement.DRMATTESTTYPE), pcPrincipal: POINTER(UInt32), wszPrincipal: win32more.Windows.Win32.Foundation.PWSTR, pcManifest: POINTER(UInt32), wszManifest: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMCreateUser(wszUserName: win32more.Windows.Win32.Foundation.PWSTR, wszUserId: win32more.Windows.Win32.Foundation.PWSTR, wszUserIdType: win32more.Windows.Win32.Foundation.PWSTR, phUser: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMCreateRight(wszRightName: win32more.Windows.Win32.Foundation.PWSTR, pstFrom: POINTER(win32more.Windows.Win32.Foundation.SYSTEMTIME), pstUntil: POINTER(win32more.Windows.Win32.Foundation.SYSTEMTIME), cExtendedInfo: UInt32, pwszExtendedInfoName: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pwszExtendedInfoValue: POINTER(win32more.Windows.Win32.Foundation.PWSTR), phRight: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMCreateIssuanceLicense(pstTimeFrom: POINTER(win32more.Windows.Win32.Foundation.SYSTEMTIME), pstTimeUntil: POINTER(win32more.Windows.Win32.Foundation.SYSTEMTIME), wszReferralInfoName: win32more.Windows.Win32.Foundation.PWSTR, wszReferralInfoURL: win32more.Windows.Win32.Foundation.PWSTR, hOwner: UInt32, wszIssuanceLicense: win32more.Windows.Win32.Foundation.PWSTR, hBoundLicense: UInt32, phIssuanceLicense: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMAddRightWithUser(hIssuanceLicense: UInt32, hRight: UInt32, hUser: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMClearAllRights(hIssuanceLicense: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMSetMetaData(hIssuanceLicense: UInt32, wszContentId: win32more.Windows.Win32.Foundation.PWSTR, wszContentIdType: win32more.Windows.Win32.Foundation.PWSTR, wszSKUId: win32more.Windows.Win32.Foundation.PWSTR, wszSKUIdType: win32more.Windows.Win32.Foundation.PWSTR, wszContentType: win32more.Windows.Win32.Foundation.PWSTR, wszContentName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMSetUsagePolicy(hIssuanceLicense: UInt32, eUsagePolicyType: win32more.Windows.Win32.Data.RightsManagement.DRM_USAGEPOLICY_TYPE, fDelete: win32more.Windows.Win32.Foundation.BOOL, fExclusion: win32more.Windows.Win32.Foundation.BOOL, wszName: win32more.Windows.Win32.Foundation.PWSTR, wszMinVersion: win32more.Windows.Win32.Foundation.PWSTR, wszMaxVersion: win32more.Windows.Win32.Foundation.PWSTR, wszPublicKey: win32more.Windows.Win32.Foundation.PWSTR, wszDigestAlgorithm: win32more.Windows.Win32.Foundation.PWSTR, pbDigest: POINTER(Byte), cbDigest: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMSetRevocationPoint(hIssuanceLicense: UInt32, fDelete: win32more.Windows.Win32.Foundation.BOOL, wszId: win32more.Windows.Win32.Foundation.PWSTR, wszIdType: win32more.Windows.Win32.Foundation.PWSTR, wszURL: win32more.Windows.Win32.Foundation.PWSTR, pstFrequency: POINTER(win32more.Windows.Win32.Foundation.SYSTEMTIME), wszName: win32more.Windows.Win32.Foundation.PWSTR, wszPublicKey: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMSetApplicationSpecificData(hIssuanceLicense: UInt32, fDelete: win32more.Windows.Win32.Foundation.BOOL, wszName: win32more.Windows.Win32.Foundation.PWSTR, wszValue: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMSetNameAndDescription(hIssuanceLicense: UInt32, fDelete: win32more.Windows.Win32.Foundation.BOOL, lcid: UInt32, wszName: win32more.Windows.Win32.Foundation.PWSTR, wszDescription: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMSetIntervalTime(hIssuanceLicense: UInt32, cDays: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetIssuanceLicenseTemplate(hIssuanceLicense: UInt32, puIssuanceLicenseTemplateLength: POINTER(UInt32), wszIssuanceLicenseTemplate: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetSignedIssuanceLicense(hEnv: UInt32, hIssuanceLicense: UInt32, uFlags: UInt32, pbSymKey: POINTER(Byte), cbSymKey: UInt32, wszSymKeyType: win32more.Windows.Win32.Foundation.PWSTR, wszClientLicensorCertificate: win32more.Windows.Win32.Foundation.PWSTR, pfnCallback: win32more.Windows.Win32.Data.RightsManagement.DRMCALLBACK, wszURL: win32more.Windows.Win32.Foundation.PWSTR, pvContext: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetSignedIssuanceLicenseEx(hEnv: UInt32, hIssuanceLicense: UInt32, uFlags: UInt32, pbSymKey: POINTER(Byte), cbSymKey: UInt32, wszSymKeyType: win32more.Windows.Win32.Foundation.PWSTR, pvReserved: VoidPtr, hEnablingPrincipal: UInt32, hBoundLicenseCLC: UInt32, pfnCallback: win32more.Windows.Win32.Data.RightsManagement.DRMCALLBACK, pvContext: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMClosePubHandle(hPub: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMDuplicatePubHandle(hPubIn: UInt32, phPubOut: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetUserInfo(hUser: UInt32, puUserNameLength: POINTER(UInt32), wszUserName: win32more.Windows.Win32.Foundation.PWSTR, puUserIdLength: POINTER(UInt32), wszUserId: win32more.Windows.Win32.Foundation.PWSTR, puUserIdTypeLength: POINTER(UInt32), wszUserIdType: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetRightInfo(hRight: UInt32, puRightNameLength: POINTER(UInt32), wszRightName: win32more.Windows.Win32.Foundation.PWSTR, pstFrom: POINTER(win32more.Windows.Win32.Foundation.SYSTEMTIME), pstUntil: POINTER(win32more.Windows.Win32.Foundation.SYSTEMTIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetRightExtendedInfo(hRight: UInt32, uIndex: UInt32, puExtendedInfoNameLength: POINTER(UInt32), wszExtendedInfoName: win32more.Windows.Win32.Foundation.PWSTR, puExtendedInfoValueLength: POINTER(UInt32), wszExtendedInfoValue: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetUsers(hIssuanceLicense: UInt32, uIndex: UInt32, phUser: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetUserRights(hIssuanceLicense: UInt32, hUser: UInt32, uIndex: UInt32, phRight: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetMetaData(hIssuanceLicense: UInt32, puContentIdLength: POINTER(UInt32), wszContentId: win32more.Windows.Win32.Foundation.PWSTR, puContentIdTypeLength: POINTER(UInt32), wszContentIdType: win32more.Windows.Win32.Foundation.PWSTR, puSKUIdLength: POINTER(UInt32), wszSKUId: win32more.Windows.Win32.Foundation.PWSTR, puSKUIdTypeLength: POINTER(UInt32), wszSKUIdType: win32more.Windows.Win32.Foundation.PWSTR, puContentTypeLength: POINTER(UInt32), wszContentType: win32more.Windows.Win32.Foundation.PWSTR, puContentNameLength: POINTER(UInt32), wszContentName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetApplicationSpecificData(hIssuanceLicense: UInt32, uIndex: UInt32, puNameLength: POINTER(UInt32), wszName: win32more.Windows.Win32.Foundation.PWSTR, puValueLength: POINTER(UInt32), wszValue: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetIssuanceLicenseInfo(hIssuanceLicense: UInt32, pstTimeFrom: POINTER(win32more.Windows.Win32.Foundation.SYSTEMTIME), pstTimeUntil: POINTER(win32more.Windows.Win32.Foundation.SYSTEMTIME), uFlags: UInt32, puDistributionPointNameLength: POINTER(UInt32), wszDistributionPointName: win32more.Windows.Win32.Foundation.PWSTR, puDistributionPointURLLength: POINTER(UInt32), wszDistributionPointURL: win32more.Windows.Win32.Foundation.PWSTR, phOwner: POINTER(UInt32), pfOfficial: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetRevocationPoint(hIssuanceLicense: UInt32, puIdLength: POINTER(UInt32), wszId: win32more.Windows.Win32.Foundation.PWSTR, puIdTypeLength: POINTER(UInt32), wszIdType: win32more.Windows.Win32.Foundation.PWSTR, puURLLength: POINTER(UInt32), wszRL: win32more.Windows.Win32.Foundation.PWSTR, pstFrequency: POINTER(win32more.Windows.Win32.Foundation.SYSTEMTIME), puNameLength: POINTER(UInt32), wszName: win32more.Windows.Win32.Foundation.PWSTR, puPublicKeyLength: POINTER(UInt32), wszPublicKey: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetUsagePolicy(hIssuanceLicense: UInt32, uIndex: UInt32, peUsagePolicyType: POINTER(win32more.Windows.Win32.Data.RightsManagement.DRM_USAGEPOLICY_TYPE), pfExclusion: POINTER(win32more.Windows.Win32.Foundation.BOOL), puNameLength: POINTER(UInt32), wszName: win32more.Windows.Win32.Foundation.PWSTR, puMinVersionLength: POINTER(UInt32), wszMinVersion: win32more.Windows.Win32.Foundation.PWSTR, puMaxVersionLength: POINTER(UInt32), wszMaxVersion: win32more.Windows.Win32.Foundation.PWSTR, puPublicKeyLength: POINTER(UInt32), wszPublicKey: win32more.Windows.Win32.Foundation.PWSTR, puDigestAlgorithmLength: POINTER(UInt32), wszDigestAlgorithm: win32more.Windows.Win32.Foundation.PWSTR, pcbDigest: POINTER(UInt32), pbDigest: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetNameAndDescription(hIssuanceLicense: UInt32, uIndex: UInt32, pulcid: POINTER(UInt32), puNameLength: POINTER(UInt32), wszName: win32more.Windows.Win32.Foundation.PWSTR, puDescriptionLength: POINTER(UInt32), wszDescription: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetOwnerLicense(hIssuanceLicense: UInt32, puOwnerLicenseLength: POINTER(UInt32), wszOwnerLicense: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMGetIntervalTime(hIssuanceLicense: UInt32, pcDays: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMRepair() -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMRegisterProtectedWindow(hEnv: UInt32, hwnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMIsWindowProtected(hwnd: win32more.Windows.Win32.Foundation.HWND, pfProtected: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdrm.dll')
def DRMAcquireIssuanceLicenseTemplate(hClient: UInt32, uFlags: UInt32, pvReserved: VoidPtr, cTemplates: UInt32, pwszTemplateIds: POINTER(win32more.Windows.Win32.Foundation.PWSTR), wszUrl: win32more.Windows.Win32.Foundation.PWSTR, pvContext: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
DRMATTESTTYPE = Int32
DRMATTESTTYPE_FULLENVIRONMENT: win32more.Windows.Win32.Data.RightsManagement.DRMATTESTTYPE = 0
DRMATTESTTYPE_HASHONLY: win32more.Windows.Win32.Data.RightsManagement.DRMATTESTTYPE = 1
class DRMBOUNDLICENSEPARAMS(Structure):
    uVersion: UInt32
    hEnablingPrincipal: UInt32
    hSecureStore: UInt32
    wszRightsRequested: win32more.Windows.Win32.Foundation.PWSTR
    wszRightsGroup: win32more.Windows.Win32.Foundation.PWSTR
    idResource: win32more.Windows.Win32.Data.RightsManagement.DRMID
    cAuthenticatorCount: UInt32
    rghAuthenticators: POINTER(UInt32)
    wszDefaultEnablingPrincipalCredentials: win32more.Windows.Win32.Foundation.PWSTR
    dwFlags: UInt32
@winfunctype_pointer
def DRMCALLBACK(param0: win32more.Windows.Win32.Data.RightsManagement.DRM_STATUS_MSG, param1: win32more.Windows.Win32.Foundation.HRESULT, param2: VoidPtr, param3: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
DRMENCODINGTYPE = Int32
DRMENCODINGTYPE_BASE64: win32more.Windows.Win32.Data.RightsManagement.DRMENCODINGTYPE = 0
DRMENCODINGTYPE_STRING: win32more.Windows.Win32.Data.RightsManagement.DRMENCODINGTYPE = 1
DRMENCODINGTYPE_LONG: win32more.Windows.Win32.Data.RightsManagement.DRMENCODINGTYPE = 2
DRMENCODINGTYPE_TIME: win32more.Windows.Win32.Data.RightsManagement.DRMENCODINGTYPE = 3
DRMENCODINGTYPE_UINT: win32more.Windows.Win32.Data.RightsManagement.DRMENCODINGTYPE = 4
DRMENCODINGTYPE_RAW: win32more.Windows.Win32.Data.RightsManagement.DRMENCODINGTYPE = 5
DRMGLOBALOPTIONS = Int32
DRMGLOBALOPTIONS_USE_WINHTTP: win32more.Windows.Win32.Data.RightsManagement.DRMGLOBALOPTIONS = 0
DRMGLOBALOPTIONS_USE_SERVERSECURITYPROCESSOR: win32more.Windows.Win32.Data.RightsManagement.DRMGLOBALOPTIONS = 1
class DRMID(Structure):
    uVersion: UInt32
    wszIDType: win32more.Windows.Win32.Foundation.PWSTR
    wszID: win32more.Windows.Win32.Foundation.PWSTR
DRMSECURITYPROVIDERTYPE = Int32
DRMSECURITYPROVIDERTYPE_SOFTWARESECREP: win32more.Windows.Win32.Data.RightsManagement.DRMSECURITYPROVIDERTYPE = 0
DRMSPECTYPE = Int32
DRMSPECTYPE_UNKNOWN: win32more.Windows.Win32.Data.RightsManagement.DRMSPECTYPE = 0
DRMSPECTYPE_FILENAME: win32more.Windows.Win32.Data.RightsManagement.DRMSPECTYPE = 1
DRMTIMETYPE = Int32
DRMTIMETYPE_SYSTEMUTC: win32more.Windows.Win32.Data.RightsManagement.DRMTIMETYPE = 0
DRMTIMETYPE_SYSTEMLOCAL: win32more.Windows.Win32.Data.RightsManagement.DRMTIMETYPE = 1
class DRM_ACTSERV_INFO(Structure):
    uVersion: UInt32
    wszPubKey: win32more.Windows.Win32.Foundation.PWSTR
    wszURL: win32more.Windows.Win32.Foundation.PWSTR
class DRM_CLIENT_VERSION_INFO(Structure):
    uStructVersion: UInt32
    dwVersion: UInt32 * 4
    wszHierarchy: Char * 256
    wszProductId: Char * 256
    wszProductDescription: Char * 256
DRM_DISTRIBUTION_POINT_INFO = Int32
DRM_DISTRIBUTION_POINT_LICENSE_ACQUISITION: win32more.Windows.Win32.Data.RightsManagement.DRM_DISTRIBUTION_POINT_INFO = 0
DRM_DISTRIBUTION_POINT_PUBLISHING: win32more.Windows.Win32.Data.RightsManagement.DRM_DISTRIBUTION_POINT_INFO = 1
DRM_DISTRIBUTION_POINT_REFERRAL_INFO: win32more.Windows.Win32.Data.RightsManagement.DRM_DISTRIBUTION_POINT_INFO = 2
class DRM_LICENSE_ACQ_DATA(Structure):
    uVersion: UInt32
    wszURL: win32more.Windows.Win32.Foundation.PWSTR
    wszLocalFilename: win32more.Windows.Win32.Foundation.PWSTR
    pbPostData: POINTER(Byte)
    dwPostDataSize: UInt32
    wszFriendlyName: win32more.Windows.Win32.Foundation.PWSTR
DRM_STATUS_MSG = Int32
DRM_MSG_ACTIVATE_MACHINE: win32more.Windows.Win32.Data.RightsManagement.DRM_STATUS_MSG = 0
DRM_MSG_ACTIVATE_GROUPIDENTITY: win32more.Windows.Win32.Data.RightsManagement.DRM_STATUS_MSG = 1
DRM_MSG_ACQUIRE_LICENSE: win32more.Windows.Win32.Data.RightsManagement.DRM_STATUS_MSG = 2
DRM_MSG_ACQUIRE_ADVISORY: win32more.Windows.Win32.Data.RightsManagement.DRM_STATUS_MSG = 3
DRM_MSG_SIGN_ISSUANCE_LICENSE: win32more.Windows.Win32.Data.RightsManagement.DRM_STATUS_MSG = 4
DRM_MSG_ACQUIRE_CLIENTLICENSOR: win32more.Windows.Win32.Data.RightsManagement.DRM_STATUS_MSG = 5
DRM_MSG_ACQUIRE_ISSUANCE_LICENSE_TEMPLATE: win32more.Windows.Win32.Data.RightsManagement.DRM_STATUS_MSG = 6
DRM_USAGEPOLICY_TYPE = Int32
DRM_USAGEPOLICY_TYPE_BYNAME: win32more.Windows.Win32.Data.RightsManagement.DRM_USAGEPOLICY_TYPE = 0
DRM_USAGEPOLICY_TYPE_BYPUBLICKEY: win32more.Windows.Win32.Data.RightsManagement.DRM_USAGEPOLICY_TYPE = 1
DRM_USAGEPOLICY_TYPE_BYDIGEST: win32more.Windows.Win32.Data.RightsManagement.DRM_USAGEPOLICY_TYPE = 2
DRM_USAGEPOLICY_TYPE_OSEXCLUSION: win32more.Windows.Win32.Data.RightsManagement.DRM_USAGEPOLICY_TYPE = 3


make_ready(__name__)
