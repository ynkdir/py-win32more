from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Security.Cryptography
import win32more.Windows.Win32.Security.Cryptography.Sip
import win32more.Windows.Win32.Security.WinTrust
WINTRUST_CONFIG_REGPATH: String = 'Software\\Microsoft\\Cryptography\\Wintrust\\Config'
WINTRUST_MAX_HEADER_BYTES_TO_MAP_VALUE_NAME: String = 'MaxHeaderBytesToMap'
WINTRUST_MAX_HEADER_BYTES_TO_MAP_DEFAULT: UInt32 = 10485760
WINTRUST_MAX_HASH_BYTES_TO_MAP_VALUE_NAME: String = 'MaxHashBytesToMap'
WINTRUST_MAX_HASH_BYTES_TO_MAP_DEFAULT: UInt32 = 1048576
WTD_PROV_FLAGS_MASK: UInt32 = 65535
WTD_CODE_INTEGRITY_DRIVER_MODE: UInt32 = 32768
WSS_VERIFY_SEALING: UInt32 = 4
WSS_INPUT_FLAG_MASK: UInt32 = 7
WSS_OUT_SEALING_STATUS_VERIFIED: UInt32 = 2147483648
WSS_OUT_HAS_SEALING_INTENT: UInt32 = 1073741824
WSS_OUT_FILE_SUPPORTS_SEAL: UInt32 = 536870912
WSS_OUTPUT_FLAG_MASK: UInt32 = 3758096384
WTCI_DONT_OPEN_STORES: UInt32 = 1
WTCI_OPEN_ONLY_ROOT: UInt32 = 2
WTCI_USE_LOCAL_MACHINE: UInt32 = 4
TRUSTERROR_STEP_WVTPARAMS: UInt32 = 0
TRUSTERROR_STEP_FILEIO: UInt32 = 2
TRUSTERROR_STEP_SIP: UInt32 = 3
TRUSTERROR_STEP_SIPSUBJINFO: UInt32 = 5
TRUSTERROR_STEP_CATALOGFILE: UInt32 = 6
TRUSTERROR_STEP_CERTSTORE: UInt32 = 7
TRUSTERROR_STEP_MESSAGE: UInt32 = 8
TRUSTERROR_STEP_MSG_SIGNERCOUNT: UInt32 = 9
TRUSTERROR_STEP_MSG_INNERCNTTYPE: UInt32 = 10
TRUSTERROR_STEP_MSG_INNERCNT: UInt32 = 11
TRUSTERROR_STEP_MSG_STORE: UInt32 = 12
TRUSTERROR_STEP_MSG_SIGNERINFO: UInt32 = 13
TRUSTERROR_STEP_MSG_SIGNERCERT: UInt32 = 14
TRUSTERROR_STEP_MSG_CERTCHAIN: UInt32 = 15
TRUSTERROR_STEP_MSG_COUNTERSIGINFO: UInt32 = 16
TRUSTERROR_STEP_MSG_COUNTERSIGCERT: UInt32 = 17
TRUSTERROR_STEP_VERIFY_MSGHASH: UInt32 = 18
TRUSTERROR_STEP_VERIFY_MSGINDIRECTDATA: UInt32 = 19
TRUSTERROR_STEP_FINAL_WVTINIT: UInt32 = 30
TRUSTERROR_STEP_FINAL_INITPROV: UInt32 = 31
TRUSTERROR_STEP_FINAL_OBJPROV: UInt32 = 32
TRUSTERROR_STEP_FINAL_SIGPROV: UInt32 = 33
TRUSTERROR_STEP_FINAL_CERTPROV: UInt32 = 34
TRUSTERROR_STEP_FINAL_CERTCHKPROV: UInt32 = 35
TRUSTERROR_STEP_FINAL_POLICYPROV: UInt32 = 36
TRUSTERROR_STEP_FINAL_UIPROV: UInt32 = 37
TRUSTERROR_MAX_STEPS: UInt32 = 38
CPD_CHOICE_SIP: UInt32 = 1
CPD_USE_NT5_CHAIN_FLAG: UInt32 = 2147483648
CPD_REVOCATION_CHECK_NONE: UInt32 = 65536
CPD_REVOCATION_CHECK_END_CERT: UInt32 = 131072
CPD_REVOCATION_CHECK_CHAIN: UInt32 = 262144
CPD_REVOCATION_CHECK_CHAIN_EXCLUDE_ROOT: UInt32 = 524288
CPD_RETURN_LOWER_QUALITY_CHAINS: UInt32 = 1048576
CPD_RFC3161v21: UInt32 = 2097152
CPD_UISTATE_MODE_PROMPT: UInt32 = 0
CPD_UISTATE_MODE_BLOCK: UInt32 = 1
CPD_UISTATE_MODE_ALLOW: UInt32 = 2
CPD_UISTATE_MODE_MASK: UInt32 = 3
WSS_OBJTRUST_SUPPORT: UInt32 = 1
WSS_SIGTRUST_SUPPORT: UInt32 = 2
WSS_CERTTRUST_SUPPORT: UInt32 = 4
SGNR_TYPE_TIMESTAMP: UInt32 = 16
CERT_CONFIDENCE_SIG: UInt32 = 268435456
CERT_CONFIDENCE_TIME: UInt32 = 16777216
CERT_CONFIDENCE_TIMENEST: UInt32 = 1048576
CERT_CONFIDENCE_AUTHIDEXT: UInt32 = 65536
CERT_CONFIDENCE_HYGIENE: UInt32 = 4096
CERT_CONFIDENCE_HIGHEST: UInt32 = 286330880
WT_CURRENT_VERSION: UInt32 = 512
WT_PROVIDER_DLL_NAME: String = 'WINTRUST.DLL'
WT_PROVIDER_CERTTRUST_FUNCTION: String = 'WintrustCertificateTrust'
WT_ADD_ACTION_ID_RET_RESULT_FLAG: UInt32 = 1
szOID_TRUSTED_CODESIGNING_CA_LIST: String = '1.3.6.1.4.1.311.2.2.1'
szOID_TRUSTED_CLIENT_AUTH_CA_LIST: String = '1.3.6.1.4.1.311.2.2.2'
szOID_TRUSTED_SERVER_AUTH_CA_LIST: String = '1.3.6.1.4.1.311.2.2.3'
SPC_COMMON_NAME_OBJID: String = '2.5.4.3'
SPC_TIME_STAMP_REQUEST_OBJID: String = '1.3.6.1.4.1.311.3.2.1'
SPC_INDIRECT_DATA_OBJID: String = '1.3.6.1.4.1.311.2.1.4'
SPC_SP_AGENCY_INFO_OBJID: String = '1.3.6.1.4.1.311.2.1.10'
SPC_STATEMENT_TYPE_OBJID: String = '1.3.6.1.4.1.311.2.1.11'
SPC_SP_OPUS_INFO_OBJID: String = '1.3.6.1.4.1.311.2.1.12'
SPC_CERT_EXTENSIONS_OBJID: String = '1.3.6.1.4.1.311.2.1.14'
SPC_PE_IMAGE_DATA_OBJID: String = '1.3.6.1.4.1.311.2.1.15'
SPC_RAW_FILE_DATA_OBJID: String = '1.3.6.1.4.1.311.2.1.18'
SPC_STRUCTURED_STORAGE_DATA_OBJID: String = '1.3.6.1.4.1.311.2.1.19'
SPC_JAVA_CLASS_DATA_OBJID: String = '1.3.6.1.4.1.311.2.1.20'
SPC_INDIVIDUAL_SP_KEY_PURPOSE_OBJID: String = '1.3.6.1.4.1.311.2.1.21'
SPC_COMMERCIAL_SP_KEY_PURPOSE_OBJID: String = '1.3.6.1.4.1.311.2.1.22'
SPC_CAB_DATA_OBJID: String = '1.3.6.1.4.1.311.2.1.25'
SPC_GLUE_RDN_OBJID: String = '1.3.6.1.4.1.311.2.1.25'
SPC_MINIMAL_CRITERIA_OBJID: String = '1.3.6.1.4.1.311.2.1.26'
SPC_FINANCIAL_CRITERIA_OBJID: String = '1.3.6.1.4.1.311.2.1.27'
SPC_LINK_OBJID: String = '1.3.6.1.4.1.311.2.1.28'
SPC_SIGINFO_OBJID: String = '1.3.6.1.4.1.311.2.1.30'
SPC_PE_IMAGE_PAGE_HASHES_V1_OBJID: String = '1.3.6.1.4.1.311.2.3.1'
SPC_PE_IMAGE_PAGE_HASHES_V2_OBJID: String = '1.3.6.1.4.1.311.2.3.2'
szOID_NESTED_SIGNATURE: String = '1.3.6.1.4.1.311.2.4.1'
szOID_INTENT_TO_SEAL: String = '1.3.6.1.4.1.311.2.4.2'
szOID_SEALING_SIGNATURE: String = '1.3.6.1.4.1.311.2.4.3'
szOID_SEALING_TIMESTAMP: String = '1.3.6.1.4.1.311.2.4.4'
szOID_ENHANCED_HASH: String = '1.3.6.1.4.1.311.2.5.1'
SPC_RELAXED_PE_MARKER_CHECK_OBJID: String = '1.3.6.1.4.1.311.2.6.1'
SPC_ENCRYPTED_DIGEST_RETRY_COUNT_OBJID: String = '1.3.6.1.4.1.311.2.6.2'
szOID_PKCS_9_SEQUENCE_NUMBER: String = '1.2.840.113549.1.9.25.4'
CAT_NAMEVALUE_OBJID: String = '1.3.6.1.4.1.311.12.2.1'
CAT_MEMBERINFO_OBJID: String = '1.3.6.1.4.1.311.12.2.2'
CAT_MEMBERINFO2_OBJID: String = '1.3.6.1.4.1.311.12.2.3'
SPC_WINDOWS_HELLO_COMPATIBILITY_OBJID: String = '1.3.6.1.4.1.311.10.41.1'
SPC_NATURAL_AUTH_PLUGIN_OBJID: String = '1.3.6.1.4.1.311.96.1.1'
SPC_SP_AGENCY_INFO_STRUCT: win32more.Windows.Win32.Foundation.PSTR = 2000
SPC_MINIMAL_CRITERIA_STRUCT: win32more.Windows.Win32.Foundation.PSTR = 2001
SPC_FINANCIAL_CRITERIA_STRUCT: win32more.Windows.Win32.Foundation.PSTR = 2002
SPC_INDIRECT_DATA_CONTENT_STRUCT: win32more.Windows.Win32.Foundation.PSTR = 2003
SPC_PE_IMAGE_DATA_STRUCT: win32more.Windows.Win32.Foundation.PSTR = 2004
SPC_LINK_STRUCT: win32more.Windows.Win32.Foundation.PSTR = 2005
SPC_STATEMENT_TYPE_STRUCT: win32more.Windows.Win32.Foundation.PSTR = 2006
SPC_SP_OPUS_INFO_STRUCT: win32more.Windows.Win32.Foundation.PSTR = 2007
SPC_CAB_DATA_STRUCT: win32more.Windows.Win32.Foundation.PSTR = 2008
SPC_JAVA_CLASS_DATA_STRUCT: win32more.Windows.Win32.Foundation.PSTR = 2009
INTENT_TO_SEAL_ATTRIBUTE_STRUCT: win32more.Windows.Win32.Foundation.PSTR = 2010
SEALING_SIGNATURE_ATTRIBUTE_STRUCT: win32more.Windows.Win32.Foundation.PSTR = 2011
SEALING_TIMESTAMP_ATTRIBUTE_STRUCT: win32more.Windows.Win32.Foundation.PSTR = 2012
SPC_SIGINFO_STRUCT: win32more.Windows.Win32.Foundation.PSTR = 2130
CAT_NAMEVALUE_STRUCT: win32more.Windows.Win32.Foundation.PSTR = 2221
CAT_MEMBERINFO_STRUCT: win32more.Windows.Win32.Foundation.PSTR = 2222
CAT_MEMBERINFO2_STRUCT: win32more.Windows.Win32.Foundation.PSTR = 2223
SPC_UUID_LENGTH: UInt32 = 16
SPC_URL_LINK_CHOICE: UInt32 = 1
SPC_MONIKER_LINK_CHOICE: UInt32 = 2
SPC_FILE_LINK_CHOICE: UInt32 = 3
WIN_CERT_REVISION_1_0: UInt32 = 256
WIN_CERT_REVISION_2_0: UInt32 = 512
WIN_CERT_TYPE_X509: UInt32 = 1
WIN_CERT_TYPE_PKCS_SIGNED_DATA: UInt32 = 2
WIN_CERT_TYPE_RESERVED_1: UInt32 = 3
WIN_CERT_TYPE_TS_STACK_SIGNED: UInt32 = 4
WIN_TRUST_SUBJTYPE_RAW_FILE: Guid = Guid('{959dc450-8d9e-11cf-8736-00aa00a485eb}')
WIN_TRUST_SUBJTYPE_PE_IMAGE: Guid = Guid('{43c9a1e0-8da0-11cf-8736-00aa00a485eb}')
WIN_TRUST_SUBJTYPE_JAVA_CLASS: Guid = Guid('{08ad3990-8da1-11cf-8736-00aa00a485eb}')
WIN_TRUST_SUBJTYPE_CABINET: Guid = Guid('{d17c5374-a392-11cf-9df5-00aa00c184e0}')
WIN_TRUST_SUBJTYPE_RAW_FILEEX: Guid = Guid('{6f458110-c2f1-11cf-8a69-00aa006c3706}')
WIN_TRUST_SUBJTYPE_PE_IMAGEEX: Guid = Guid('{6f458111-c2f1-11cf-8a69-00aa006c3706}')
WIN_TRUST_SUBJTYPE_JAVA_CLASSEX: Guid = Guid('{6f458113-c2f1-11cf-8a69-00aa006c3706}')
WIN_TRUST_SUBJTYPE_CABINETEX: Guid = Guid('{6f458114-c2f1-11cf-8a69-00aa006c3706}')
WIN_TRUST_SUBJTYPE_OLE_STORAGE: Guid = Guid('{c257e740-8da0-11cf-8736-00aa00a485eb}')
WIN_SPUB_ACTION_TRUSTED_PUBLISHER: Guid = Guid('{66426730-8da1-11cf-8736-00aa00a485eb}')
WIN_SPUB_ACTION_NT_ACTIVATE_IMAGE: Guid = Guid('{8bc96b00-8da1-11cf-8736-00aa00a485eb}')
WIN_SPUB_ACTION_PUBLISHED_SOFTWARE: Guid = Guid('{64b9d180-8da2-11cf-8736-00aa00a485eb}')
WT_TRUSTDBDIALOG_NO_UI_FLAG: UInt32 = 1
WT_TRUSTDBDIALOG_ONLY_PUB_TAB_FLAG: UInt32 = 2
WT_TRUSTDBDIALOG_WRITE_LEGACY_REG_FLAG: UInt32 = 256
WT_TRUSTDBDIALOG_WRITE_IEAK_STORE_FLAG: UInt32 = 512
SP_POLICY_PROVIDER_DLL_NAME: String = 'WINTRUST.DLL'
WINTRUST_ACTION_GENERIC_VERIFY_V2: Guid = Guid('{00aac56b-cd44-11d0-8cc2-00c04fc295ee}')
SP_INIT_FUNCTION: String = 'SoftpubInitialize'
SP_OBJTRUST_FUNCTION: String = 'SoftpubLoadMessage'
SP_SIGTRUST_FUNCTION: String = 'SoftpubLoadSignature'
SP_CHKCERT_FUNCTION: String = 'SoftpubCheckCert'
SP_FINALPOLICY_FUNCTION: String = 'SoftpubAuthenticode'
SP_CLEANUPPOLICY_FUNCTION: String = 'SoftpubCleanup'
WINTRUST_ACTION_TRUSTPROVIDER_TEST: Guid = Guid('{573e31f8-ddba-11d0-8ccb-00c04fc295ee}')
SP_TESTDUMPPOLICY_FUNCTION_TEST: String = 'SoftpubDumpStructure'
WINTRUST_ACTION_GENERIC_CERT_VERIFY: Guid = Guid('{189a3842-3041-11d1-85e1-00c04fc295ee}')
SP_GENERIC_CERT_INIT_FUNCTION: String = 'SoftpubDefCertInit'
WINTRUST_ACTION_GENERIC_CHAIN_VERIFY: Guid = Guid('{fc451c16-ac75-11d1-b4b8-00c04fb66ea0}')
GENERIC_CHAIN_FINALPOLICY_FUNCTION: String = 'GenericChainFinalProv'
GENERIC_CHAIN_CERTTRUST_FUNCTION: String = 'GenericChainCertificateTrust'
HTTPSPROV_ACTION: Guid = Guid('{573e31f8-aaba-11d0-8ccb-00c04fc295ee}')
HTTPS_FINALPOLICY_FUNCTION: String = 'HTTPSFinalProv'
HTTPS_CHKCERT_FUNCTION: String = 'HTTPSCheckCertProv'
HTTPS_CERTTRUST_FUNCTION: String = 'HTTPSCertificateTrust'
OFFICESIGN_ACTION_VERIFY: Guid = Guid('{5555c2cd-17fb-11d1-85c4-00c04fc295ee}')
OFFICE_POLICY_PROVIDER_DLL_NAME: String = 'WINTRUST.DLL'
OFFICE_INITPROV_FUNCTION: String = 'OfficeInitializePolicy'
OFFICE_CLEANUPPOLICY_FUNCTION: String = 'OfficeCleanupPolicy'
DRIVER_ACTION_VERIFY: Guid = Guid('{f750e6c3-38ee-11d1-85e5-00c04fc295ee}')
DRIVER_INITPROV_FUNCTION: String = 'DriverInitializePolicy'
DRIVER_FINALPOLPROV_FUNCTION: String = 'DriverFinalPolicy'
DRIVER_CLEANUPPOLICY_FUNCTION: String = 'DriverCleanupPolicy'
CONFIG_CI_ACTION_VERIFY: Guid = Guid('{6078065b-8f22-4b13-bd9b-5b762776f386}')
CCPI_RESULT_ALLOW: UInt32 = 1
CCPI_RESULT_DENY: UInt32 = 2
CCPI_RESULT_AUDIT: UInt32 = 3
@winfunctype('WINTRUST.dll')
def WinVerifyTrust(hwnd: win32more.Windows.Win32.Foundation.HWND, pgActionID: POINTER(Guid), pWVTData: VoidPtr) -> Int32: ...
@winfunctype('WINTRUST.dll')
def WinVerifyTrustEx(hwnd: win32more.Windows.Win32.Foundation.HWND, pgActionID: POINTER(Guid), pWinTrustData: POINTER(win32more.Windows.Win32.Security.WinTrust.WINTRUST_DATA)) -> Int32: ...
@winfunctype('WINTRUST.dll')
def WintrustGetRegPolicyFlags(pdwPolicyFlags: POINTER(win32more.Windows.Win32.Security.WinTrust.WINTRUST_POLICY_FLAGS)) -> Void: ...
@winfunctype('WINTRUST.dll')
def WintrustSetRegPolicyFlags(dwPolicyFlags: win32more.Windows.Win32.Security.WinTrust.WINTRUST_POLICY_FLAGS) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def WintrustAddActionID(pgActionID: POINTER(Guid), fdwFlags: UInt32, psProvInfo: POINTER(win32more.Windows.Win32.Security.WinTrust.CRYPT_REGISTER_ACTIONID)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def WintrustRemoveActionID(pgActionID: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def WintrustLoadFunctionPointers(pgActionID: POINTER(Guid), pPfns: POINTER(win32more.Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_FUNCTIONS)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def WintrustAddDefaultForUsage(pszUsageOID: win32more.Windows.Win32.Foundation.PSTR, psDefUsage: POINTER(win32more.Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_REGDEFUSAGE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def WintrustGetDefaultForUsage(dwAction: win32more.Windows.Win32.Security.WinTrust.WINTRUST_GET_DEFAULT_FOR_USAGE_ACTION, pszUsageOID: win32more.Windows.Win32.Foundation.PSTR, psUsage: POINTER(win32more.Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_DEFUSAGE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def WTHelperGetProvSignerFromChain(pProvData: POINTER(win32more.Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_DATA), idxSigner: UInt32, fCounterSigner: win32more.Windows.Win32.Foundation.BOOL, idxCounterSigner: UInt32) -> POINTER(win32more.Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_SGNR): ...
@winfunctype('WINTRUST.dll')
def WTHelperGetProvCertFromChain(pSgnr: POINTER(win32more.Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_SGNR), idxCert: UInt32) -> POINTER(win32more.Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_CERT): ...
@winfunctype('WINTRUST.dll')
def WTHelperProvDataFromStateData(hStateData: win32more.Windows.Win32.Foundation.HANDLE) -> POINTER(win32more.Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_DATA): ...
@winfunctype('WINTRUST.dll')
def WTHelperGetProvPrivateDataFromChain(pProvData: POINTER(win32more.Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_DATA), pgProviderID: POINTER(Guid)) -> POINTER(win32more.Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_PRIVDATA): ...
@winfunctype('WINTRUST.dll')
def WTHelperCertIsSelfSigned(dwEncoding: UInt32, pCert: POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_INFO)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def WTHelperCertCheckValidSignature(pProvData: POINTER(win32more.Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_DATA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WINTRUST.dll')
def OpenPersonalTrustDBDialogEx(hwndParent: win32more.Windows.Win32.Foundation.HWND, dwFlags: UInt32, pvReserved: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def OpenPersonalTrustDBDialog(hwndParent: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def WintrustSetDefaultIncludePEPageHashes(fIncludePEPageHashes: win32more.Windows.Win32.Foundation.BOOL) -> Void: ...
class CAT_MEMBERINFO(Structure):
    pwszSubjGuid: win32more.Windows.Win32.Foundation.PWSTR
    dwCertVersion: UInt32
class CAT_MEMBERINFO2(Structure):
    SubjectGuid: Guid
    dwCertVersion: UInt32
class CAT_NAMEVALUE(Structure):
    pwszTag: win32more.Windows.Win32.Foundation.PWSTR
    fdwFlags: UInt32
    Value: win32more.Windows.Win32.Security.Cryptography.CRYPT_INTEGER_BLOB
class CONFIG_CI_PROV_INFO(Structure):
    cbSize: UInt32
    dwPolicies: UInt32
    pPolicies: POINTER(win32more.Windows.Win32.Security.Cryptography.CRYPT_INTEGER_BLOB)
    result: win32more.Windows.Win32.Security.WinTrust.CONFIG_CI_PROV_INFO_RESULT
    dwScenario: UInt32
    result2: POINTER(win32more.Windows.Win32.Security.WinTrust.CONFIG_CI_PROV_INFO_RESULT2)
class CONFIG_CI_PROV_INFO_RESULT(Structure):
    hr: win32more.Windows.Win32.Foundation.HRESULT
    dwResult: UInt32
    dwPolicyIndex: UInt32
    fIsExplicitDeny: win32more.Windows.Win32.Foundation.BOOLEAN
class CONFIG_CI_PROV_INFO_RESULT2(Structure):
    cbSize: UInt32
    hr: win32more.Windows.Win32.Foundation.HRESULT
    dwResult: UInt32
    dwPolicyIndex: UInt32
    fIsExplicitDeny: win32more.Windows.Win32.Foundation.BOOLEAN
    cbCalculatedFileHash: UInt32
    pbCalculatedFileHash: POINTER(Byte)
class CRYPT_PROVIDER_CERT(Structure):
    cbStruct: UInt32
    pCert: POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CONTEXT)
    fCommercial: win32more.Windows.Win32.Foundation.BOOL
    fTrustedRoot: win32more.Windows.Win32.Foundation.BOOL
    fSelfSigned: win32more.Windows.Win32.Foundation.BOOL
    fTestCert: win32more.Windows.Win32.Foundation.BOOL
    dwRevokedReason: UInt32
    dwConfidence: UInt32
    dwError: UInt32
    pTrustListContext: POINTER(win32more.Windows.Win32.Security.Cryptography.CTL_CONTEXT)
    fTrustListSignerCert: win32more.Windows.Win32.Foundation.BOOL
    pCtlContext: POINTER(win32more.Windows.Win32.Security.Cryptography.CTL_CONTEXT)
    dwCtlError: UInt32
    fIsCyclic: win32more.Windows.Win32.Foundation.BOOL
    pChainElement: POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CHAIN_ELEMENT)
class CRYPT_PROVIDER_DATA(Structure):
    cbStruct: UInt32
    pWintrustData: POINTER(win32more.Windows.Win32.Security.WinTrust.WINTRUST_DATA)
    fOpenedFile: win32more.Windows.Win32.Foundation.BOOL
    hWndParent: win32more.Windows.Win32.Foundation.HWND
    pgActionID: POINTER(Guid)
    hProv: UIntPtr
    dwError: UInt32
    dwRegSecuritySettings: UInt32
    dwRegPolicySettings: UInt32
    psPfns: POINTER(win32more.Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_FUNCTIONS)
    cdwTrustStepErrors: UInt32
    padwTrustStepErrors: POINTER(UInt32)
    chStores: UInt32
    pahStores: POINTER(win32more.Windows.Win32.Security.Cryptography.HCERTSTORE)
    dwEncoding: UInt32
    hMsg: VoidPtr
    csSigners: UInt32
    pasSigners: POINTER(win32more.Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_SGNR)
    csProvPrivData: UInt32
    pasProvPrivData: POINTER(win32more.Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_PRIVDATA)
    dwSubjectChoice: UInt32
    Anonymous: _Anonymous_e__Union
    pszUsageOID: win32more.Windows.Win32.Foundation.PSTR
    fRecallWithState: win32more.Windows.Win32.Foundation.BOOL
    sftSystemTime: win32more.Windows.Win32.Foundation.FILETIME
    pszCTLSignerUsageOID: win32more.Windows.Win32.Foundation.PSTR
    dwProvFlags: UInt32
    dwFinalError: UInt32
    pRequestUsage: POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_USAGE_MATCH)
    dwTrustPubSettings: UInt32
    dwUIStateFlags: UInt32
    pSigState: POINTER(win32more.Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_SIGSTATE)
    pSigSettings: POINTER(win32more.Windows.Win32.Security.WinTrust.WINTRUST_SIGNATURE_SETTINGS)
    class _Anonymous_e__Union(Union):
        pPDSip: POINTER(win32more.Windows.Win32.Security.WinTrust.PROVDATA_SIP)
class CRYPT_PROVIDER_DEFUSAGE(Structure):
    cbStruct: UInt32
    gActionID: Guid
    pDefPolicyCallbackData: VoidPtr
    pDefSIPClientData: VoidPtr
class CRYPT_PROVIDER_FUNCTIONS(Structure):
    cbStruct: UInt32
    pfnAlloc: win32more.Windows.Win32.Security.WinTrust.PFN_CPD_MEM_ALLOC
    pfnFree: win32more.Windows.Win32.Security.WinTrust.PFN_CPD_MEM_FREE
    pfnAddStore2Chain: win32more.Windows.Win32.Security.WinTrust.PFN_CPD_ADD_STORE
    pfnAddSgnr2Chain: win32more.Windows.Win32.Security.WinTrust.PFN_CPD_ADD_SGNR
    pfnAddCert2Chain: win32more.Windows.Win32.Security.WinTrust.PFN_CPD_ADD_CERT
    pfnAddPrivData2Chain: win32more.Windows.Win32.Security.WinTrust.PFN_CPD_ADD_PRIVDATA
    pfnInitialize: win32more.Windows.Win32.Security.WinTrust.PFN_PROVIDER_INIT_CALL
    pfnObjectTrust: win32more.Windows.Win32.Security.WinTrust.PFN_PROVIDER_OBJTRUST_CALL
    pfnSignatureTrust: win32more.Windows.Win32.Security.WinTrust.PFN_PROVIDER_SIGTRUST_CALL
    pfnCertificateTrust: win32more.Windows.Win32.Security.WinTrust.PFN_PROVIDER_CERTTRUST_CALL
    pfnFinalPolicy: win32more.Windows.Win32.Security.WinTrust.PFN_PROVIDER_FINALPOLICY_CALL
    pfnCertCheckPolicy: win32more.Windows.Win32.Security.WinTrust.PFN_PROVIDER_CERTCHKPOLICY_CALL
    pfnTestFinalPolicy: win32more.Windows.Win32.Security.WinTrust.PFN_PROVIDER_TESTFINALPOLICY_CALL
    psUIpfns: POINTER(win32more.Windows.Win32.Security.WinTrust.CRYPT_PROVUI_FUNCS)
    pfnCleanupPolicy: win32more.Windows.Win32.Security.WinTrust.PFN_PROVIDER_CLEANUP_CALL
class CRYPT_PROVIDER_PRIVDATA(Structure):
    cbStruct: UInt32
    gProviderID: Guid
    cbProvData: UInt32
    pvProvData: VoidPtr
class CRYPT_PROVIDER_REGDEFUSAGE(Structure):
    cbStruct: UInt32
    pgActionID: POINTER(Guid)
    pwszDllName: win32more.Windows.Win32.Foundation.PWSTR
    pwszLoadCallbackDataFunctionName: win32more.Windows.Win32.Foundation.PSTR
    pwszFreeCallbackDataFunctionName: win32more.Windows.Win32.Foundation.PSTR
class CRYPT_PROVIDER_SGNR(Structure):
    cbStruct: UInt32
    sftVerifyAsOf: win32more.Windows.Win32.Foundation.FILETIME
    csCertChain: UInt32
    pasCertChain: POINTER(win32more.Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_CERT)
    dwSignerType: UInt32
    psSigner: POINTER(win32more.Windows.Win32.Security.Cryptography.CMSG_SIGNER_INFO)
    dwError: UInt32
    csCounterSigners: UInt32
    pasCounterSigners: POINTER(win32more.Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_SGNR)
    pChainContext: POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CHAIN_CONTEXT)
class CRYPT_PROVIDER_SIGSTATE(Structure):
    cbStruct: UInt32
    rhSecondarySigs: POINTER(VoidPtr)
    hPrimarySig: VoidPtr
    fFirstAttemptMade: win32more.Windows.Win32.Foundation.BOOL
    fNoMoreSigs: win32more.Windows.Win32.Foundation.BOOL
    cSecondarySigs: UInt32
    dwCurrentIndex: UInt32
    fSupportMultiSig: win32more.Windows.Win32.Foundation.BOOL
    dwCryptoPolicySupport: UInt32
    iAttemptCount: UInt32
    fCheckedSealing: win32more.Windows.Win32.Foundation.BOOL
    pSealingSignature: POINTER(win32more.Windows.Win32.Security.WinTrust.SEALING_SIGNATURE_ATTRIBUTE)
class CRYPT_PROVUI_DATA(Structure):
    cbStruct: UInt32
    dwFinalError: UInt32
    pYesButtonText: win32more.Windows.Win32.Foundation.PWSTR
    pNoButtonText: win32more.Windows.Win32.Foundation.PWSTR
    pMoreInfoButtonText: win32more.Windows.Win32.Foundation.PWSTR
    pAdvancedLinkText: win32more.Windows.Win32.Foundation.PWSTR
    pCopyActionText: win32more.Windows.Win32.Foundation.PWSTR
    pCopyActionTextNoTS: win32more.Windows.Win32.Foundation.PWSTR
    pCopyActionTextNotSigned: win32more.Windows.Win32.Foundation.PWSTR
class CRYPT_PROVUI_FUNCS(Structure):
    cbStruct: UInt32
    psUIData: POINTER(win32more.Windows.Win32.Security.WinTrust.CRYPT_PROVUI_DATA)
    pfnOnMoreInfoClick: win32more.Windows.Win32.Security.WinTrust.PFN_PROVUI_CALL
    pfnOnMoreInfoClickDefault: win32more.Windows.Win32.Security.WinTrust.PFN_PROVUI_CALL
    pfnOnAdvancedClick: win32more.Windows.Win32.Security.WinTrust.PFN_PROVUI_CALL
    pfnOnAdvancedClickDefault: win32more.Windows.Win32.Security.WinTrust.PFN_PROVUI_CALL
class CRYPT_REGISTER_ACTIONID(Structure):
    cbStruct: UInt32
    sInitProvider: win32more.Windows.Win32.Security.WinTrust.CRYPT_TRUST_REG_ENTRY
    sObjectProvider: win32more.Windows.Win32.Security.WinTrust.CRYPT_TRUST_REG_ENTRY
    sSignatureProvider: win32more.Windows.Win32.Security.WinTrust.CRYPT_TRUST_REG_ENTRY
    sCertificateProvider: win32more.Windows.Win32.Security.WinTrust.CRYPT_TRUST_REG_ENTRY
    sCertificatePolicyProvider: win32more.Windows.Win32.Security.WinTrust.CRYPT_TRUST_REG_ENTRY
    sFinalPolicyProvider: win32more.Windows.Win32.Security.WinTrust.CRYPT_TRUST_REG_ENTRY
    sTestPolicyProvider: win32more.Windows.Win32.Security.WinTrust.CRYPT_TRUST_REG_ENTRY
    sCleanupProvider: win32more.Windows.Win32.Security.WinTrust.CRYPT_TRUST_REG_ENTRY
class CRYPT_TRUST_REG_ENTRY(Structure):
    cbStruct: UInt32
    pwszDLLName: win32more.Windows.Win32.Foundation.PWSTR
    pwszFunctionName: win32more.Windows.Win32.Foundation.PWSTR
class DRIVER_VER_INFO(Structure):
    cbStruct: UInt32
    dwReserved1: UIntPtr
    dwReserved2: UIntPtr
    dwPlatform: UInt32
    dwVersion: UInt32
    wszVersion: Char * 260
    wszSignedBy: Char * 260
    pcSignerCertContext: POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CONTEXT)
    sOSVersionLow: win32more.Windows.Win32.Security.WinTrust.DRIVER_VER_MAJORMINOR
    sOSVersionHigh: win32more.Windows.Win32.Security.WinTrust.DRIVER_VER_MAJORMINOR
    dwBuildNumberLow: UInt32
    dwBuildNumberHigh: UInt32
class DRIVER_VER_MAJORMINOR(Structure):
    dwMajor: UInt32
    dwMinor: UInt32
class INTENT_TO_SEAL_ATTRIBUTE(Structure):
    version: UInt32
    seal: win32more.Windows.Win32.Foundation.BOOLEAN
@winfunctype_pointer
def PFN_ALLOCANDFILLDEFUSAGE(pszUsageOID: win32more.Windows.Win32.Foundation.PSTR, psDefUsage: POINTER(win32more.Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_DEFUSAGE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFN_CPD_ADD_CERT(pProvData: POINTER(win32more.Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_DATA), idxSigner: UInt32, fCounterSigner: win32more.Windows.Win32.Foundation.BOOL, idxCounterSigner: UInt32, pCert2Add: POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CONTEXT)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFN_CPD_ADD_PRIVDATA(pProvData: POINTER(win32more.Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_DATA), pPrivData2Add: POINTER(win32more.Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_PRIVDATA)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFN_CPD_ADD_SGNR(pProvData: POINTER(win32more.Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_DATA), fCounterSigner: win32more.Windows.Win32.Foundation.BOOL, idxSigner: UInt32, pSgnr2Add: POINTER(win32more.Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_SGNR)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFN_CPD_ADD_STORE(pProvData: POINTER(win32more.Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_DATA), hStore2Add: win32more.Windows.Win32.Security.Cryptography.HCERTSTORE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFN_CPD_MEM_ALLOC(cbSize: UInt32) -> VoidPtr: ...
@winfunctype_pointer
def PFN_CPD_MEM_FREE(pvMem2Free: VoidPtr) -> Void: ...
@winfunctype_pointer
def PFN_FREEDEFUSAGE(pszUsageOID: win32more.Windows.Win32.Foundation.PSTR, psDefUsage: POINTER(win32more.Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_DEFUSAGE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFN_PROVIDER_CERTCHKPOLICY_CALL(pProvData: POINTER(win32more.Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_DATA), idxSigner: UInt32, fCounterSignerChain: win32more.Windows.Win32.Foundation.BOOL, idxCounterSigner: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFN_PROVIDER_CERTTRUST_CALL(pProvData: POINTER(win32more.Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_DATA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFN_PROVIDER_CLEANUP_CALL(pProvData: POINTER(win32more.Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_DATA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFN_PROVIDER_FINALPOLICY_CALL(pProvData: POINTER(win32more.Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_DATA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFN_PROVIDER_INIT_CALL(pProvData: POINTER(win32more.Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_DATA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFN_PROVIDER_OBJTRUST_CALL(pProvData: POINTER(win32more.Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_DATA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFN_PROVIDER_SIGTRUST_CALL(pProvData: POINTER(win32more.Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_DATA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFN_PROVIDER_TESTFINALPOLICY_CALL(pProvData: POINTER(win32more.Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_DATA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFN_PROVUI_CALL(hWndSecurityDialog: win32more.Windows.Win32.Foundation.HWND, pProvData: POINTER(win32more.Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_DATA)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFN_WTD_GENERIC_CHAIN_POLICY_CALLBACK(pProvData: POINTER(win32more.Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_DATA), dwStepError: UInt32, dwRegPolicySettings: UInt32, cSigner: UInt32, rgpSigner: POINTER(POINTER(win32more.Windows.Win32.Security.WinTrust.WTD_GENERIC_CHAIN_POLICY_SIGNER_INFO)), pvPolicyArg: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class PROVDATA_SIP(Structure):
    cbStruct: UInt32
    gSubject: Guid
    pSip: POINTER(win32more.Windows.Win32.Security.Cryptography.Sip.SIP_DISPATCH_INFO)
    pCATSip: POINTER(win32more.Windows.Win32.Security.Cryptography.Sip.SIP_DISPATCH_INFO)
    psSipSubjectInfo: POINTER(win32more.Windows.Win32.Security.Cryptography.Sip.SIP_SUBJECTINFO)
    psSipCATSubjectInfo: POINTER(win32more.Windows.Win32.Security.Cryptography.Sip.SIP_SUBJECTINFO)
    psIndirectData: POINTER(win32more.Windows.Win32.Security.Cryptography.Sip.SIP_INDIRECT_DATA)
class SEALING_SIGNATURE_ATTRIBUTE(Structure):
    version: UInt32
    signerIndex: UInt32
    signatureAlgorithm: win32more.Windows.Win32.Security.Cryptography.CRYPT_ALGORITHM_IDENTIFIER
    encryptedDigest: win32more.Windows.Win32.Security.Cryptography.CRYPT_INTEGER_BLOB
class SEALING_TIMESTAMP_ATTRIBUTE(Structure):
    version: UInt32
    signerIndex: UInt32
    sealTimeStampToken: win32more.Windows.Win32.Security.Cryptography.CRYPT_INTEGER_BLOB
class SPC_FINANCIAL_CRITERIA(Structure):
    fFinancialInfoAvailable: win32more.Windows.Win32.Foundation.BOOL
    fMeetsCriteria: win32more.Windows.Win32.Foundation.BOOL
class SPC_IMAGE(Structure):
    pImageLink: POINTER(win32more.Windows.Win32.Security.WinTrust.SPC_LINK)
    Bitmap: win32more.Windows.Win32.Security.Cryptography.CRYPT_INTEGER_BLOB
    Metafile: win32more.Windows.Win32.Security.Cryptography.CRYPT_INTEGER_BLOB
    EnhancedMetafile: win32more.Windows.Win32.Security.Cryptography.CRYPT_INTEGER_BLOB
    GifFile: win32more.Windows.Win32.Security.Cryptography.CRYPT_INTEGER_BLOB
class SPC_INDIRECT_DATA_CONTENT(Structure):
    Data: win32more.Windows.Win32.Security.Cryptography.CRYPT_ATTRIBUTE_TYPE_VALUE
    DigestAlgorithm: win32more.Windows.Win32.Security.Cryptography.CRYPT_ALGORITHM_IDENTIFIER
    Digest: win32more.Windows.Win32.Security.Cryptography.CRYPT_INTEGER_BLOB
class SPC_LINK(Structure):
    dwLinkChoice: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        pwszUrl: win32more.Windows.Win32.Foundation.PWSTR
        Moniker: win32more.Windows.Win32.Security.WinTrust.SPC_SERIALIZED_OBJECT
        pwszFile: win32more.Windows.Win32.Foundation.PWSTR
class SPC_PE_IMAGE_DATA(Structure):
    Flags: win32more.Windows.Win32.Security.Cryptography.CRYPT_BIT_BLOB
    pFile: POINTER(win32more.Windows.Win32.Security.WinTrust.SPC_LINK)
class SPC_SERIALIZED_OBJECT(Structure):
    ClassId: Byte * 16
    SerializedData: win32more.Windows.Win32.Security.Cryptography.CRYPT_INTEGER_BLOB
class SPC_SIGINFO(Structure):
    dwSipVersion: UInt32
    gSIPGuid: Guid
    dwReserved1: UInt32
    dwReserved2: UInt32
    dwReserved3: UInt32
    dwReserved4: UInt32
    dwReserved5: UInt32
class SPC_SP_AGENCY_INFO(Structure):
    pPolicyInformation: POINTER(win32more.Windows.Win32.Security.WinTrust.SPC_LINK)
    pwszPolicyDisplayText: win32more.Windows.Win32.Foundation.PWSTR
    pLogoImage: POINTER(win32more.Windows.Win32.Security.WinTrust.SPC_IMAGE)
    pLogoLink: POINTER(win32more.Windows.Win32.Security.WinTrust.SPC_LINK)
class SPC_SP_OPUS_INFO(Structure):
    pwszProgramName: win32more.Windows.Win32.Foundation.PWSTR
    pMoreInfo: POINTER(win32more.Windows.Win32.Security.WinTrust.SPC_LINK)
    pPublisherInfo: POINTER(win32more.Windows.Win32.Security.WinTrust.SPC_LINK)
class SPC_STATEMENT_TYPE(Structure):
    cKeyPurposeId: UInt32
    rgpszKeyPurposeId: POINTER(win32more.Windows.Win32.Foundation.PSTR)
class WINTRUST_BLOB_INFO(Structure):
    cbStruct: UInt32
    gSubject: Guid
    pcwszDisplayName: win32more.Windows.Win32.Foundation.PWSTR
    cbMemObject: UInt32
    pbMemObject: POINTER(Byte)
    cbMemSignedMsg: UInt32
    pbMemSignedMsg: POINTER(Byte)
class WINTRUST_CATALOG_INFO(Structure):
    cbStruct: UInt32
    dwCatalogVersion: UInt32
    pcwszCatalogFilePath: win32more.Windows.Win32.Foundation.PWSTR
    pcwszMemberTag: win32more.Windows.Win32.Foundation.PWSTR
    pcwszMemberFilePath: win32more.Windows.Win32.Foundation.PWSTR
    hMemberFile: win32more.Windows.Win32.Foundation.HANDLE
    pbCalculatedFileHash: POINTER(Byte)
    cbCalculatedFileHash: UInt32
    pcCatalogContext: POINTER(win32more.Windows.Win32.Security.Cryptography.CTL_CONTEXT)
    hCatAdmin: IntPtr
class WINTRUST_CERT_INFO(Structure):
    cbStruct: UInt32
    pcwszDisplayName: win32more.Windows.Win32.Foundation.PWSTR
    psCertContext: POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CONTEXT)
    chStores: UInt32
    pahStores: POINTER(win32more.Windows.Win32.Security.Cryptography.HCERTSTORE)
    dwFlags: UInt32
    psftVerifyAsOf: POINTER(win32more.Windows.Win32.Foundation.FILETIME)
class WINTRUST_DATA(Structure):
    cbStruct: UInt32
    pPolicyCallbackData: VoidPtr
    pSIPClientData: VoidPtr
    dwUIChoice: win32more.Windows.Win32.Security.WinTrust.WINTRUST_DATA_UICHOICE
    fdwRevocationChecks: win32more.Windows.Win32.Security.WinTrust.WINTRUST_DATA_REVOCATION_CHECKS
    dwUnionChoice: win32more.Windows.Win32.Security.WinTrust.WINTRUST_DATA_UNION_CHOICE
    Anonymous: _Anonymous_e__Union
    dwStateAction: win32more.Windows.Win32.Security.WinTrust.WINTRUST_DATA_STATE_ACTION
    hWVTStateData: win32more.Windows.Win32.Foundation.HANDLE
    pwszURLReference: win32more.Windows.Win32.Foundation.PWSTR
    dwProvFlags: win32more.Windows.Win32.Security.WinTrust.WINTRUST_DATA_PROVIDER_FLAGS
    dwUIContext: win32more.Windows.Win32.Security.WinTrust.WINTRUST_DATA_UICONTEXT
    pSignatureSettings: POINTER(win32more.Windows.Win32.Security.WinTrust.WINTRUST_SIGNATURE_SETTINGS)
    class _Anonymous_e__Union(Union):
        pFile: POINTER(win32more.Windows.Win32.Security.WinTrust.WINTRUST_FILE_INFO)
        pCatalog: POINTER(win32more.Windows.Win32.Security.WinTrust.WINTRUST_CATALOG_INFO)
        pBlob: POINTER(win32more.Windows.Win32.Security.WinTrust.WINTRUST_BLOB_INFO)
        pSgnr: POINTER(win32more.Windows.Win32.Security.WinTrust.WINTRUST_SGNR_INFO)
        pCert: POINTER(win32more.Windows.Win32.Security.WinTrust.WINTRUST_CERT_INFO)
WINTRUST_DATA_PROVIDER_FLAGS = UInt32
WTD_USE_IE4_TRUST_FLAG: win32more.Windows.Win32.Security.WinTrust.WINTRUST_DATA_PROVIDER_FLAGS = 1
WTD_NO_IE4_CHAIN_FLAG: win32more.Windows.Win32.Security.WinTrust.WINTRUST_DATA_PROVIDER_FLAGS = 2
WTD_NO_POLICY_USAGE_FLAG: win32more.Windows.Win32.Security.WinTrust.WINTRUST_DATA_PROVIDER_FLAGS = 4
WTD_REVOCATION_CHECK_NONE: win32more.Windows.Win32.Security.WinTrust.WINTRUST_DATA_PROVIDER_FLAGS = 16
WTD_REVOCATION_CHECK_END_CERT: win32more.Windows.Win32.Security.WinTrust.WINTRUST_DATA_PROVIDER_FLAGS = 32
WTD_REVOCATION_CHECK_CHAIN: win32more.Windows.Win32.Security.WinTrust.WINTRUST_DATA_PROVIDER_FLAGS = 64
WTD_REVOCATION_CHECK_CHAIN_EXCLUDE_ROOT: win32more.Windows.Win32.Security.WinTrust.WINTRUST_DATA_PROVIDER_FLAGS = 128
WTD_SAFER_FLAG: win32more.Windows.Win32.Security.WinTrust.WINTRUST_DATA_PROVIDER_FLAGS = 256
WTD_HASH_ONLY_FLAG: win32more.Windows.Win32.Security.WinTrust.WINTRUST_DATA_PROVIDER_FLAGS = 512
WTD_USE_DEFAULT_OSVER_CHECK: win32more.Windows.Win32.Security.WinTrust.WINTRUST_DATA_PROVIDER_FLAGS = 1024
WTD_LIFETIME_SIGNING_FLAG: win32more.Windows.Win32.Security.WinTrust.WINTRUST_DATA_PROVIDER_FLAGS = 2048
WTD_CACHE_ONLY_URL_RETRIEVAL: win32more.Windows.Win32.Security.WinTrust.WINTRUST_DATA_PROVIDER_FLAGS = 4096
WTD_DISABLE_MD2_MD4: win32more.Windows.Win32.Security.WinTrust.WINTRUST_DATA_PROVIDER_FLAGS = 8192
WTD_MOTW: win32more.Windows.Win32.Security.WinTrust.WINTRUST_DATA_PROVIDER_FLAGS = 16384
WINTRUST_DATA_REVOCATION_CHECKS = UInt32
WTD_REVOKE_NONE: win32more.Windows.Win32.Security.WinTrust.WINTRUST_DATA_REVOCATION_CHECKS = 0
WTD_REVOKE_WHOLECHAIN: win32more.Windows.Win32.Security.WinTrust.WINTRUST_DATA_REVOCATION_CHECKS = 1
WINTRUST_DATA_STATE_ACTION = UInt32
WTD_STATEACTION_IGNORE: win32more.Windows.Win32.Security.WinTrust.WINTRUST_DATA_STATE_ACTION = 0
WTD_STATEACTION_VERIFY: win32more.Windows.Win32.Security.WinTrust.WINTRUST_DATA_STATE_ACTION = 1
WTD_STATEACTION_CLOSE: win32more.Windows.Win32.Security.WinTrust.WINTRUST_DATA_STATE_ACTION = 2
WTD_STATEACTION_AUTO_CACHE: win32more.Windows.Win32.Security.WinTrust.WINTRUST_DATA_STATE_ACTION = 3
WTD_STATEACTION_AUTO_CACHE_FLUSH: win32more.Windows.Win32.Security.WinTrust.WINTRUST_DATA_STATE_ACTION = 4
WINTRUST_DATA_UICHOICE = UInt32
WTD_UI_ALL: win32more.Windows.Win32.Security.WinTrust.WINTRUST_DATA_UICHOICE = 1
WTD_UI_NONE: win32more.Windows.Win32.Security.WinTrust.WINTRUST_DATA_UICHOICE = 2
WTD_UI_NOBAD: win32more.Windows.Win32.Security.WinTrust.WINTRUST_DATA_UICHOICE = 3
WTD_UI_NOGOOD: win32more.Windows.Win32.Security.WinTrust.WINTRUST_DATA_UICHOICE = 4
WINTRUST_DATA_UICONTEXT = UInt32
WTD_UICONTEXT_EXECUTE: win32more.Windows.Win32.Security.WinTrust.WINTRUST_DATA_UICONTEXT = 0
WTD_UICONTEXT_INSTALL: win32more.Windows.Win32.Security.WinTrust.WINTRUST_DATA_UICONTEXT = 1
WINTRUST_DATA_UNION_CHOICE = UInt32
WTD_CHOICE_FILE: win32more.Windows.Win32.Security.WinTrust.WINTRUST_DATA_UNION_CHOICE = 1
WTD_CHOICE_CATALOG: win32more.Windows.Win32.Security.WinTrust.WINTRUST_DATA_UNION_CHOICE = 2
WTD_CHOICE_BLOB: win32more.Windows.Win32.Security.WinTrust.WINTRUST_DATA_UNION_CHOICE = 3
WTD_CHOICE_SIGNER: win32more.Windows.Win32.Security.WinTrust.WINTRUST_DATA_UNION_CHOICE = 4
WTD_CHOICE_CERT: win32more.Windows.Win32.Security.WinTrust.WINTRUST_DATA_UNION_CHOICE = 5
class WINTRUST_FILE_INFO(Structure):
    cbStruct: UInt32
    pcwszFilePath: win32more.Windows.Win32.Foundation.PWSTR
    hFile: win32more.Windows.Win32.Foundation.HANDLE
    pgKnownSubject: POINTER(Guid)
WINTRUST_GET_DEFAULT_FOR_USAGE_ACTION = UInt32
DWACTION_ALLOCANDFILL: win32more.Windows.Win32.Security.WinTrust.WINTRUST_GET_DEFAULT_FOR_USAGE_ACTION = 1
DWACTION_FREE: win32more.Windows.Win32.Security.WinTrust.WINTRUST_GET_DEFAULT_FOR_USAGE_ACTION = 2
WINTRUST_POLICY_FLAGS = UInt32
WTPF_TRUSTTEST: win32more.Windows.Win32.Security.WinTrust.WINTRUST_POLICY_FLAGS = 32
WTPF_TESTCANBEVALID: win32more.Windows.Win32.Security.WinTrust.WINTRUST_POLICY_FLAGS = 128
WTPF_IGNOREEXPIRATION: win32more.Windows.Win32.Security.WinTrust.WINTRUST_POLICY_FLAGS = 256
WTPF_IGNOREREVOKATION: win32more.Windows.Win32.Security.WinTrust.WINTRUST_POLICY_FLAGS = 512
WTPF_OFFLINEOK_IND: win32more.Windows.Win32.Security.WinTrust.WINTRUST_POLICY_FLAGS = 1024
WTPF_OFFLINEOK_COM: win32more.Windows.Win32.Security.WinTrust.WINTRUST_POLICY_FLAGS = 2048
WTPF_OFFLINEOKNBU_IND: win32more.Windows.Win32.Security.WinTrust.WINTRUST_POLICY_FLAGS = 4096
WTPF_OFFLINEOKNBU_COM: win32more.Windows.Win32.Security.WinTrust.WINTRUST_POLICY_FLAGS = 8192
WTPF_VERIFY_V1_OFF: win32more.Windows.Win32.Security.WinTrust.WINTRUST_POLICY_FLAGS = 65536
WTPF_IGNOREREVOCATIONONTS: win32more.Windows.Win32.Security.WinTrust.WINTRUST_POLICY_FLAGS = 131072
WTPF_ALLOWONLYPERTRUST: win32more.Windows.Win32.Security.WinTrust.WINTRUST_POLICY_FLAGS = 262144
class WINTRUST_SGNR_INFO(Structure):
    cbStruct: UInt32
    pcwszDisplayName: win32more.Windows.Win32.Foundation.PWSTR
    psSignerInfo: POINTER(win32more.Windows.Win32.Security.Cryptography.CMSG_SIGNER_INFO)
    chStores: UInt32
    pahStores: POINTER(win32more.Windows.Win32.Security.Cryptography.HCERTSTORE)
class WINTRUST_SIGNATURE_SETTINGS(Structure):
    cbStruct: UInt32
    dwIndex: UInt32
    dwFlags: win32more.Windows.Win32.Security.WinTrust.WINTRUST_SIGNATURE_SETTINGS_FLAGS
    cSecondarySigs: UInt32
    dwVerifiedSigIndex: UInt32
    pCryptoPolicy: POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_STRONG_SIGN_PARA)
WINTRUST_SIGNATURE_SETTINGS_FLAGS = UInt32
WSS_VERIFY_SPECIFIC: win32more.Windows.Win32.Security.WinTrust.WINTRUST_SIGNATURE_SETTINGS_FLAGS = 1
WSS_GET_SECONDARY_SIG_COUNT: win32more.Windows.Win32.Security.WinTrust.WINTRUST_SIGNATURE_SETTINGS_FLAGS = 2
class WIN_CERTIFICATE(Structure):
    dwLength: UInt32
    wRevision: UInt16
    wCertificateType: UInt16
    bCertificate: Byte * 1
class WIN_SPUB_TRUSTED_PUBLISHER_DATA(Structure):
    hClientToken: win32more.Windows.Win32.Foundation.HANDLE
    lpCertificate: POINTER(win32more.Windows.Win32.Security.WinTrust.WIN_CERTIFICATE)
class WIN_TRUST_ACTDATA_CONTEXT_WITH_SUBJECT(Structure):
    hClientToken: win32more.Windows.Win32.Foundation.HANDLE
    SubjectType: POINTER(Guid)
    Subject: VoidPtr
class WIN_TRUST_ACTDATA_SUBJECT_ONLY(Structure):
    SubjectType: POINTER(Guid)
    Subject: VoidPtr
class WIN_TRUST_SUBJECT_FILE(Structure):
    hFile: win32more.Windows.Win32.Foundation.HANDLE
    lpPath: win32more.Windows.Win32.Foundation.PWSTR
class WIN_TRUST_SUBJECT_FILE_AND_DISPLAY(Structure):
    hFile: win32more.Windows.Win32.Foundation.HANDLE
    lpPath: win32more.Windows.Win32.Foundation.PWSTR
    lpDisplayName: win32more.Windows.Win32.Foundation.PWSTR
class WTD_GENERIC_CHAIN_POLICY_CREATE_INFO(Structure):
    Anonymous: _Anonymous_e__Union
    hChainEngine: win32more.Windows.Win32.Security.Cryptography.HCERTCHAINENGINE
    pChainPara: POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CHAIN_PARA)
    dwFlags: UInt32
    pvReserved: VoidPtr
    class _Anonymous_e__Union(Union):
        cbStruct: UInt32
        cbSize: UInt32
class WTD_GENERIC_CHAIN_POLICY_DATA(Structure):
    Anonymous: _Anonymous_e__Union
    pSignerChainInfo: POINTER(win32more.Windows.Win32.Security.WinTrust.WTD_GENERIC_CHAIN_POLICY_CREATE_INFO)
    pCounterSignerChainInfo: POINTER(win32more.Windows.Win32.Security.WinTrust.WTD_GENERIC_CHAIN_POLICY_CREATE_INFO)
    pfnPolicyCallback: win32more.Windows.Win32.Security.WinTrust.PFN_WTD_GENERIC_CHAIN_POLICY_CALLBACK
    pvPolicyArg: VoidPtr
    class _Anonymous_e__Union(Union):
        cbStruct: UInt32
        cbSize: UInt32
class WTD_GENERIC_CHAIN_POLICY_SIGNER_INFO(Structure):
    Anonymous: _Anonymous_e__Union
    pChainContext: POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CHAIN_CONTEXT)
    dwSignerType: UInt32
    pMsgSignerInfo: POINTER(win32more.Windows.Win32.Security.Cryptography.CMSG_SIGNER_INFO)
    dwError: UInt32
    cCounterSigner: UInt32
    rgpCounterSigner: POINTER(POINTER(win32more.Windows.Win32.Security.WinTrust.WTD_GENERIC_CHAIN_POLICY_SIGNER_INFO))
    class _Anonymous_e__Union(Union):
        cbStruct: UInt32
        cbSize: UInt32


make_ready(__name__)
