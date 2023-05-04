from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.Security.Cryptography
import Windows.Win32.Security.Cryptography.Sip
import Windows.Win32.Security.WinTrust
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
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
SPC_SP_AGENCY_INFO_STRUCT: Windows.Win32.Foundation.PSTR = 2000
SPC_MINIMAL_CRITERIA_STRUCT: Windows.Win32.Foundation.PSTR = 2001
SPC_FINANCIAL_CRITERIA_STRUCT: Windows.Win32.Foundation.PSTR = 2002
SPC_INDIRECT_DATA_CONTENT_STRUCT: Windows.Win32.Foundation.PSTR = 2003
SPC_PE_IMAGE_DATA_STRUCT: Windows.Win32.Foundation.PSTR = 2004
SPC_LINK_STRUCT: Windows.Win32.Foundation.PSTR = 2005
SPC_STATEMENT_TYPE_STRUCT: Windows.Win32.Foundation.PSTR = 2006
SPC_SP_OPUS_INFO_STRUCT: Windows.Win32.Foundation.PSTR = 2007
SPC_CAB_DATA_STRUCT: Windows.Win32.Foundation.PSTR = 2008
SPC_JAVA_CLASS_DATA_STRUCT: Windows.Win32.Foundation.PSTR = 2009
INTENT_TO_SEAL_ATTRIBUTE_STRUCT: Windows.Win32.Foundation.PSTR = 2010
SEALING_SIGNATURE_ATTRIBUTE_STRUCT: Windows.Win32.Foundation.PSTR = 2011
SEALING_TIMESTAMP_ATTRIBUTE_STRUCT: Windows.Win32.Foundation.PSTR = 2012
SPC_SIGINFO_STRUCT: Windows.Win32.Foundation.PSTR = 2130
CAT_NAMEVALUE_STRUCT: Windows.Win32.Foundation.PSTR = 2221
CAT_MEMBERINFO_STRUCT: Windows.Win32.Foundation.PSTR = 2222
CAT_MEMBERINFO2_STRUCT: Windows.Win32.Foundation.PSTR = 2223
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
def WinVerifyTrust(hwnd: Windows.Win32.Foundation.HWND, pgActionID: POINTER(Guid), pWVTData: c_void_p) -> Int32: ...
@winfunctype('WINTRUST.dll')
def WinVerifyTrustEx(hwnd: Windows.Win32.Foundation.HWND, pgActionID: POINTER(Guid), pWinTrustData: POINTER(Windows.Win32.Security.WinTrust.WINTRUST_DATA_head)) -> Int32: ...
@winfunctype('WINTRUST.dll')
def WintrustGetRegPolicyFlags(pdwPolicyFlags: POINTER(Windows.Win32.Security.WinTrust.WINTRUST_POLICY_FLAGS)) -> Void: ...
@winfunctype('WINTRUST.dll')
def WintrustSetRegPolicyFlags(dwPolicyFlags: Windows.Win32.Security.WinTrust.WINTRUST_POLICY_FLAGS) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def WintrustAddActionID(pgActionID: POINTER(Guid), fdwFlags: UInt32, psProvInfo: POINTER(Windows.Win32.Security.WinTrust.CRYPT_REGISTER_ACTIONID_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def WintrustRemoveActionID(pgActionID: POINTER(Guid)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def WintrustLoadFunctionPointers(pgActionID: POINTER(Guid), pPfns: POINTER(Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_FUNCTIONS_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def WintrustAddDefaultForUsage(pszUsageOID: Windows.Win32.Foundation.PSTR, psDefUsage: POINTER(Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_REGDEFUSAGE_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def WintrustGetDefaultForUsage(dwAction: Windows.Win32.Security.WinTrust.WINTRUST_GET_DEFAULT_FOR_USAGE_ACTION, pszUsageOID: Windows.Win32.Foundation.PSTR, psUsage: POINTER(Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_DEFUSAGE_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def WTHelperGetProvSignerFromChain(pProvData: POINTER(Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_DATA_head), idxSigner: UInt32, fCounterSigner: Windows.Win32.Foundation.BOOL, idxCounterSigner: UInt32) -> POINTER(Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_SGNR_head): ...
@winfunctype('WINTRUST.dll')
def WTHelperGetProvCertFromChain(pSgnr: POINTER(Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_SGNR_head), idxCert: UInt32) -> POINTER(Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_CERT_head): ...
@winfunctype('WINTRUST.dll')
def WTHelperProvDataFromStateData(hStateData: Windows.Win32.Foundation.HANDLE) -> POINTER(Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_DATA_head): ...
@winfunctype('WINTRUST.dll')
def WTHelperGetProvPrivateDataFromChain(pProvData: POINTER(Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_DATA_head), pgProviderID: POINTER(Guid)) -> POINTER(Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_PRIVDATA_head): ...
@winfunctype('WINTRUST.dll')
def WTHelperCertIsSelfSigned(dwEncoding: UInt32, pCert: POINTER(Windows.Win32.Security.Cryptography.CERT_INFO_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def WTHelperCertCheckValidSignature(pProvData: POINTER(Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_DATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WINTRUST.dll')
def OpenPersonalTrustDBDialogEx(hwndParent: Windows.Win32.Foundation.HWND, dwFlags: UInt32, pvReserved: POINTER(c_void_p)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def OpenPersonalTrustDBDialog(hwndParent: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def WintrustSetDefaultIncludePEPageHashes(fIncludePEPageHashes: Windows.Win32.Foundation.BOOL) -> Void: ...
class CAT_MEMBERINFO(EasyCastStructure):
    pwszSubjGuid: Windows.Win32.Foundation.PWSTR
    dwCertVersion: UInt32
class CAT_MEMBERINFO2(EasyCastStructure):
    SubjectGuid: Guid
    dwCertVersion: UInt32
class CAT_NAMEVALUE(EasyCastStructure):
    pwszTag: Windows.Win32.Foundation.PWSTR
    fdwFlags: UInt32
    Value: Windows.Win32.Security.Cryptography.CRYPT_INTEGER_BLOB
class CONFIG_CI_PROV_INFO(EasyCastStructure):
    cbSize: UInt32
    dwPolicies: UInt32
    pPolicies: POINTER(Windows.Win32.Security.Cryptography.CRYPT_INTEGER_BLOB_head)
    result: Windows.Win32.Security.WinTrust.CONFIG_CI_PROV_INFO_RESULT
    dwScenario: UInt32
class CONFIG_CI_PROV_INFO_RESULT(EasyCastStructure):
    hr: Windows.Win32.Foundation.HRESULT
    dwResult: UInt32
    dwPolicyIndex: UInt32
    fIsExplicitDeny: Windows.Win32.Foundation.BOOLEAN
class CRYPT_PROVIDER_CERT(EasyCastStructure):
    cbStruct: UInt32
    pCert: POINTER(Windows.Win32.Security.Cryptography.CERT_CONTEXT_head)
    fCommercial: Windows.Win32.Foundation.BOOL
    fTrustedRoot: Windows.Win32.Foundation.BOOL
    fSelfSigned: Windows.Win32.Foundation.BOOL
    fTestCert: Windows.Win32.Foundation.BOOL
    dwRevokedReason: UInt32
    dwConfidence: UInt32
    dwError: UInt32
    pTrustListContext: POINTER(Windows.Win32.Security.Cryptography.CTL_CONTEXT_head)
    fTrustListSignerCert: Windows.Win32.Foundation.BOOL
    pCtlContext: POINTER(Windows.Win32.Security.Cryptography.CTL_CONTEXT_head)
    dwCtlError: UInt32
    fIsCyclic: Windows.Win32.Foundation.BOOL
    pChainElement: POINTER(Windows.Win32.Security.Cryptography.CERT_CHAIN_ELEMENT_head)
class CRYPT_PROVIDER_DATA(EasyCastStructure):
    cbStruct: UInt32
    pWintrustData: POINTER(Windows.Win32.Security.WinTrust.WINTRUST_DATA_head)
    fOpenedFile: Windows.Win32.Foundation.BOOL
    hWndParent: Windows.Win32.Foundation.HWND
    pgActionID: POINTER(Guid)
    hProv: UIntPtr
    dwError: UInt32
    dwRegSecuritySettings: UInt32
    dwRegPolicySettings: UInt32
    psPfns: POINTER(Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_FUNCTIONS_head)
    cdwTrustStepErrors: UInt32
    padwTrustStepErrors: POINTER(UInt32)
    chStores: UInt32
    pahStores: POINTER(Windows.Win32.Security.Cryptography.HCERTSTORE)
    dwEncoding: UInt32
    hMsg: c_void_p
    csSigners: UInt32
    pasSigners: POINTER(Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_SGNR_head)
    csProvPrivData: UInt32
    pasProvPrivData: POINTER(Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_PRIVDATA_head)
    dwSubjectChoice: UInt32
    Anonymous: _Anonymous_e__Union
    pszUsageOID: Windows.Win32.Foundation.PSTR
    fRecallWithState: Windows.Win32.Foundation.BOOL
    sftSystemTime: Windows.Win32.Foundation.FILETIME
    pszCTLSignerUsageOID: Windows.Win32.Foundation.PSTR
    dwProvFlags: UInt32
    dwFinalError: UInt32
    pRequestUsage: POINTER(Windows.Win32.Security.Cryptography.CERT_USAGE_MATCH_head)
    dwTrustPubSettings: UInt32
    dwUIStateFlags: UInt32
    pSigState: POINTER(Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_SIGSTATE_head)
    pSigSettings: POINTER(Windows.Win32.Security.WinTrust.WINTRUST_SIGNATURE_SETTINGS_head)
    class _Anonymous_e__Union(EasyCastUnion):
        pPDSip: POINTER(Windows.Win32.Security.WinTrust.PROVDATA_SIP_head)
class CRYPT_PROVIDER_DEFUSAGE(EasyCastStructure):
    cbStruct: UInt32
    gActionID: Guid
    pDefPolicyCallbackData: c_void_p
    pDefSIPClientData: c_void_p
class CRYPT_PROVIDER_FUNCTIONS(EasyCastStructure):
    cbStruct: UInt32
    pfnAlloc: Windows.Win32.Security.WinTrust.PFN_CPD_MEM_ALLOC
    pfnFree: Windows.Win32.Security.WinTrust.PFN_CPD_MEM_FREE
    pfnAddStore2Chain: Windows.Win32.Security.WinTrust.PFN_CPD_ADD_STORE
    pfnAddSgnr2Chain: Windows.Win32.Security.WinTrust.PFN_CPD_ADD_SGNR
    pfnAddCert2Chain: Windows.Win32.Security.WinTrust.PFN_CPD_ADD_CERT
    pfnAddPrivData2Chain: Windows.Win32.Security.WinTrust.PFN_CPD_ADD_PRIVDATA
    pfnInitialize: Windows.Win32.Security.WinTrust.PFN_PROVIDER_INIT_CALL
    pfnObjectTrust: Windows.Win32.Security.WinTrust.PFN_PROVIDER_OBJTRUST_CALL
    pfnSignatureTrust: Windows.Win32.Security.WinTrust.PFN_PROVIDER_SIGTRUST_CALL
    pfnCertificateTrust: Windows.Win32.Security.WinTrust.PFN_PROVIDER_CERTTRUST_CALL
    pfnFinalPolicy: Windows.Win32.Security.WinTrust.PFN_PROVIDER_FINALPOLICY_CALL
    pfnCertCheckPolicy: Windows.Win32.Security.WinTrust.PFN_PROVIDER_CERTCHKPOLICY_CALL
    pfnTestFinalPolicy: Windows.Win32.Security.WinTrust.PFN_PROVIDER_TESTFINALPOLICY_CALL
    psUIpfns: POINTER(Windows.Win32.Security.WinTrust.CRYPT_PROVUI_FUNCS_head)
    pfnCleanupPolicy: Windows.Win32.Security.WinTrust.PFN_PROVIDER_CLEANUP_CALL
class CRYPT_PROVIDER_PRIVDATA(EasyCastStructure):
    cbStruct: UInt32
    gProviderID: Guid
    cbProvData: UInt32
    pvProvData: c_void_p
class CRYPT_PROVIDER_REGDEFUSAGE(EasyCastStructure):
    cbStruct: UInt32
    pgActionID: POINTER(Guid)
    pwszDllName: Windows.Win32.Foundation.PWSTR
    pwszLoadCallbackDataFunctionName: Windows.Win32.Foundation.PSTR
    pwszFreeCallbackDataFunctionName: Windows.Win32.Foundation.PSTR
class CRYPT_PROVIDER_SGNR(EasyCastStructure):
    cbStruct: UInt32
    sftVerifyAsOf: Windows.Win32.Foundation.FILETIME
    csCertChain: UInt32
    pasCertChain: POINTER(Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_CERT_head)
    dwSignerType: UInt32
    psSigner: POINTER(Windows.Win32.Security.Cryptography.CMSG_SIGNER_INFO_head)
    dwError: UInt32
    csCounterSigners: UInt32
    pasCounterSigners: POINTER(Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_SGNR_head)
    pChainContext: POINTER(Windows.Win32.Security.Cryptography.CERT_CHAIN_CONTEXT_head)
class CRYPT_PROVIDER_SIGSTATE(EasyCastStructure):
    cbStruct: UInt32
    rhSecondarySigs: POINTER(c_void_p)
    hPrimarySig: c_void_p
    fFirstAttemptMade: Windows.Win32.Foundation.BOOL
    fNoMoreSigs: Windows.Win32.Foundation.BOOL
    cSecondarySigs: UInt32
    dwCurrentIndex: UInt32
    fSupportMultiSig: Windows.Win32.Foundation.BOOL
    dwCryptoPolicySupport: UInt32
    iAttemptCount: UInt32
    fCheckedSealing: Windows.Win32.Foundation.BOOL
    pSealingSignature: POINTER(Windows.Win32.Security.WinTrust.SEALING_SIGNATURE_ATTRIBUTE_head)
class CRYPT_PROVUI_DATA(EasyCastStructure):
    cbStruct: UInt32
    dwFinalError: UInt32
    pYesButtonText: Windows.Win32.Foundation.PWSTR
    pNoButtonText: Windows.Win32.Foundation.PWSTR
    pMoreInfoButtonText: Windows.Win32.Foundation.PWSTR
    pAdvancedLinkText: Windows.Win32.Foundation.PWSTR
    pCopyActionText: Windows.Win32.Foundation.PWSTR
    pCopyActionTextNoTS: Windows.Win32.Foundation.PWSTR
    pCopyActionTextNotSigned: Windows.Win32.Foundation.PWSTR
class CRYPT_PROVUI_FUNCS(EasyCastStructure):
    cbStruct: UInt32
    psUIData: POINTER(Windows.Win32.Security.WinTrust.CRYPT_PROVUI_DATA_head)
    pfnOnMoreInfoClick: Windows.Win32.Security.WinTrust.PFN_PROVUI_CALL
    pfnOnMoreInfoClickDefault: Windows.Win32.Security.WinTrust.PFN_PROVUI_CALL
    pfnOnAdvancedClick: Windows.Win32.Security.WinTrust.PFN_PROVUI_CALL
    pfnOnAdvancedClickDefault: Windows.Win32.Security.WinTrust.PFN_PROVUI_CALL
class CRYPT_REGISTER_ACTIONID(EasyCastStructure):
    cbStruct: UInt32
    sInitProvider: Windows.Win32.Security.WinTrust.CRYPT_TRUST_REG_ENTRY
    sObjectProvider: Windows.Win32.Security.WinTrust.CRYPT_TRUST_REG_ENTRY
    sSignatureProvider: Windows.Win32.Security.WinTrust.CRYPT_TRUST_REG_ENTRY
    sCertificateProvider: Windows.Win32.Security.WinTrust.CRYPT_TRUST_REG_ENTRY
    sCertificatePolicyProvider: Windows.Win32.Security.WinTrust.CRYPT_TRUST_REG_ENTRY
    sFinalPolicyProvider: Windows.Win32.Security.WinTrust.CRYPT_TRUST_REG_ENTRY
    sTestPolicyProvider: Windows.Win32.Security.WinTrust.CRYPT_TRUST_REG_ENTRY
    sCleanupProvider: Windows.Win32.Security.WinTrust.CRYPT_TRUST_REG_ENTRY
class CRYPT_TRUST_REG_ENTRY(EasyCastStructure):
    cbStruct: UInt32
    pwszDLLName: Windows.Win32.Foundation.PWSTR
    pwszFunctionName: Windows.Win32.Foundation.PWSTR
class DRIVER_VER_INFO(EasyCastStructure):
    cbStruct: UInt32
    dwReserved1: UIntPtr
    dwReserved2: UIntPtr
    dwPlatform: UInt32
    dwVersion: UInt32
    wszVersion: Char * 260
    wszSignedBy: Char * 260
    pcSignerCertContext: POINTER(Windows.Win32.Security.Cryptography.CERT_CONTEXT_head)
    sOSVersionLow: Windows.Win32.Security.WinTrust.DRIVER_VER_MAJORMINOR
    sOSVersionHigh: Windows.Win32.Security.WinTrust.DRIVER_VER_MAJORMINOR
    dwBuildNumberLow: UInt32
    dwBuildNumberHigh: UInt32
class DRIVER_VER_MAJORMINOR(EasyCastStructure):
    dwMajor: UInt32
    dwMinor: UInt32
class INTENT_TO_SEAL_ATTRIBUTE(EasyCastStructure):
    version: UInt32
    seal: Windows.Win32.Foundation.BOOLEAN
@winfunctype_pointer
def PFN_ALLOCANDFILLDEFUSAGE(pszUsageOID: Windows.Win32.Foundation.PSTR, psDefUsage: POINTER(Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_DEFUSAGE_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFN_CPD_ADD_CERT(pProvData: POINTER(Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_DATA_head), idxSigner: UInt32, fCounterSigner: Windows.Win32.Foundation.BOOL, idxCounterSigner: UInt32, pCert2Add: POINTER(Windows.Win32.Security.Cryptography.CERT_CONTEXT_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFN_CPD_ADD_PRIVDATA(pProvData: POINTER(Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_DATA_head), pPrivData2Add: POINTER(Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_PRIVDATA_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFN_CPD_ADD_SGNR(pProvData: POINTER(Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_DATA_head), fCounterSigner: Windows.Win32.Foundation.BOOL, idxSigner: UInt32, pSgnr2Add: POINTER(Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_SGNR_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFN_CPD_ADD_STORE(pProvData: POINTER(Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_DATA_head), hStore2Add: Windows.Win32.Security.Cryptography.HCERTSTORE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFN_CPD_MEM_ALLOC(cbSize: UInt32) -> c_void_p: ...
@winfunctype_pointer
def PFN_CPD_MEM_FREE(pvMem2Free: c_void_p) -> Void: ...
@winfunctype_pointer
def PFN_FREEDEFUSAGE(pszUsageOID: Windows.Win32.Foundation.PSTR, psDefUsage: POINTER(Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_DEFUSAGE_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFN_PROVIDER_CERTCHKPOLICY_CALL(pProvData: POINTER(Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_DATA_head), idxSigner: UInt32, fCounterSignerChain: Windows.Win32.Foundation.BOOL, idxCounterSigner: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFN_PROVIDER_CERTTRUST_CALL(pProvData: POINTER(Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_DATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFN_PROVIDER_CLEANUP_CALL(pProvData: POINTER(Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_DATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFN_PROVIDER_FINALPOLICY_CALL(pProvData: POINTER(Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_DATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFN_PROVIDER_INIT_CALL(pProvData: POINTER(Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_DATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFN_PROVIDER_OBJTRUST_CALL(pProvData: POINTER(Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_DATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFN_PROVIDER_SIGTRUST_CALL(pProvData: POINTER(Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_DATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFN_PROVIDER_TESTFINALPOLICY_CALL(pProvData: POINTER(Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_DATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFN_PROVUI_CALL(hWndSecurityDialog: Windows.Win32.Foundation.HWND, pProvData: POINTER(Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_DATA_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFN_WTD_GENERIC_CHAIN_POLICY_CALLBACK(pProvData: POINTER(Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_DATA_head), dwStepError: UInt32, dwRegPolicySettings: UInt32, cSigner: UInt32, rgpSigner: POINTER(POINTER(Windows.Win32.Security.WinTrust.WTD_GENERIC_CHAIN_POLICY_SIGNER_INFO_head)), pvPolicyArg: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
class PROVDATA_SIP(EasyCastStructure):
    cbStruct: UInt32
    gSubject: Guid
    pSip: POINTER(Windows.Win32.Security.Cryptography.Sip.SIP_DISPATCH_INFO_head)
    pCATSip: POINTER(Windows.Win32.Security.Cryptography.Sip.SIP_DISPATCH_INFO_head)
    psSipSubjectInfo: POINTER(Windows.Win32.Security.Cryptography.Sip.SIP_SUBJECTINFO_head)
    psSipCATSubjectInfo: POINTER(Windows.Win32.Security.Cryptography.Sip.SIP_SUBJECTINFO_head)
    psIndirectData: POINTER(Windows.Win32.Security.Cryptography.Sip.SIP_INDIRECT_DATA_head)
class SEALING_SIGNATURE_ATTRIBUTE(EasyCastStructure):
    version: UInt32
    signerIndex: UInt32
    signatureAlgorithm: Windows.Win32.Security.Cryptography.CRYPT_ALGORITHM_IDENTIFIER
    encryptedDigest: Windows.Win32.Security.Cryptography.CRYPT_INTEGER_BLOB
class SEALING_TIMESTAMP_ATTRIBUTE(EasyCastStructure):
    version: UInt32
    signerIndex: UInt32
    sealTimeStampToken: Windows.Win32.Security.Cryptography.CRYPT_INTEGER_BLOB
class SPC_FINANCIAL_CRITERIA(EasyCastStructure):
    fFinancialInfoAvailable: Windows.Win32.Foundation.BOOL
    fMeetsCriteria: Windows.Win32.Foundation.BOOL
class SPC_IMAGE(EasyCastStructure):
    pImageLink: POINTER(Windows.Win32.Security.WinTrust.SPC_LINK_head)
    Bitmap: Windows.Win32.Security.Cryptography.CRYPT_INTEGER_BLOB
    Metafile: Windows.Win32.Security.Cryptography.CRYPT_INTEGER_BLOB
    EnhancedMetafile: Windows.Win32.Security.Cryptography.CRYPT_INTEGER_BLOB
    GifFile: Windows.Win32.Security.Cryptography.CRYPT_INTEGER_BLOB
class SPC_INDIRECT_DATA_CONTENT(EasyCastStructure):
    Data: Windows.Win32.Security.Cryptography.CRYPT_ATTRIBUTE_TYPE_VALUE
    DigestAlgorithm: Windows.Win32.Security.Cryptography.CRYPT_ALGORITHM_IDENTIFIER
    Digest: Windows.Win32.Security.Cryptography.CRYPT_INTEGER_BLOB
class SPC_LINK(EasyCastStructure):
    dwLinkChoice: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        pwszUrl: Windows.Win32.Foundation.PWSTR
        Moniker: Windows.Win32.Security.WinTrust.SPC_SERIALIZED_OBJECT
        pwszFile: Windows.Win32.Foundation.PWSTR
class SPC_PE_IMAGE_DATA(EasyCastStructure):
    Flags: Windows.Win32.Security.Cryptography.CRYPT_BIT_BLOB
    pFile: POINTER(Windows.Win32.Security.WinTrust.SPC_LINK_head)
class SPC_SERIALIZED_OBJECT(EasyCastStructure):
    ClassId: Byte * 16
    SerializedData: Windows.Win32.Security.Cryptography.CRYPT_INTEGER_BLOB
class SPC_SIGINFO(EasyCastStructure):
    dwSipVersion: UInt32
    gSIPGuid: Guid
    dwReserved1: UInt32
    dwReserved2: UInt32
    dwReserved3: UInt32
    dwReserved4: UInt32
    dwReserved5: UInt32
class SPC_SP_AGENCY_INFO(EasyCastStructure):
    pPolicyInformation: POINTER(Windows.Win32.Security.WinTrust.SPC_LINK_head)
    pwszPolicyDisplayText: Windows.Win32.Foundation.PWSTR
    pLogoImage: POINTER(Windows.Win32.Security.WinTrust.SPC_IMAGE_head)
    pLogoLink: POINTER(Windows.Win32.Security.WinTrust.SPC_LINK_head)
class SPC_SP_OPUS_INFO(EasyCastStructure):
    pwszProgramName: Windows.Win32.Foundation.PWSTR
    pMoreInfo: POINTER(Windows.Win32.Security.WinTrust.SPC_LINK_head)
    pPublisherInfo: POINTER(Windows.Win32.Security.WinTrust.SPC_LINK_head)
class SPC_STATEMENT_TYPE(EasyCastStructure):
    cKeyPurposeId: UInt32
    rgpszKeyPurposeId: POINTER(Windows.Win32.Foundation.PSTR)
class WINTRUST_BLOB_INFO(EasyCastStructure):
    cbStruct: UInt32
    gSubject: Guid
    pcwszDisplayName: Windows.Win32.Foundation.PWSTR
    cbMemObject: UInt32
    pbMemObject: POINTER(Byte)
    cbMemSignedMsg: UInt32
    pbMemSignedMsg: POINTER(Byte)
class WINTRUST_CATALOG_INFO(EasyCastStructure):
    cbStruct: UInt32
    dwCatalogVersion: UInt32
    pcwszCatalogFilePath: Windows.Win32.Foundation.PWSTR
    pcwszMemberTag: Windows.Win32.Foundation.PWSTR
    pcwszMemberFilePath: Windows.Win32.Foundation.PWSTR
    hMemberFile: Windows.Win32.Foundation.HANDLE
    pbCalculatedFileHash: POINTER(Byte)
    cbCalculatedFileHash: UInt32
    pcCatalogContext: POINTER(Windows.Win32.Security.Cryptography.CTL_CONTEXT_head)
    hCatAdmin: IntPtr
class WINTRUST_CERT_INFO(EasyCastStructure):
    cbStruct: UInt32
    pcwszDisplayName: Windows.Win32.Foundation.PWSTR
    psCertContext: POINTER(Windows.Win32.Security.Cryptography.CERT_CONTEXT_head)
    chStores: UInt32
    pahStores: POINTER(Windows.Win32.Security.Cryptography.HCERTSTORE)
    dwFlags: UInt32
    psftVerifyAsOf: POINTER(Windows.Win32.Foundation.FILETIME_head)
class WINTRUST_DATA(EasyCastStructure):
    cbStruct: UInt32
    pPolicyCallbackData: c_void_p
    pSIPClientData: c_void_p
    dwUIChoice: Windows.Win32.Security.WinTrust.WINTRUST_DATA_UICHOICE
    fdwRevocationChecks: Windows.Win32.Security.WinTrust.WINTRUST_DATA_REVOCATION_CHECKS
    dwUnionChoice: Windows.Win32.Security.WinTrust.WINTRUST_DATA_UNION_CHOICE
    Anonymous: _Anonymous_e__Union
    dwStateAction: Windows.Win32.Security.WinTrust.WINTRUST_DATA_STATE_ACTION
    hWVTStateData: Windows.Win32.Foundation.HANDLE
    pwszURLReference: Windows.Win32.Foundation.PWSTR
    dwProvFlags: Windows.Win32.Security.WinTrust.WINTRUST_DATA_PROVIDER_FLAGS
    dwUIContext: Windows.Win32.Security.WinTrust.WINTRUST_DATA_UICONTEXT
    pSignatureSettings: POINTER(Windows.Win32.Security.WinTrust.WINTRUST_SIGNATURE_SETTINGS_head)
    class _Anonymous_e__Union(EasyCastUnion):
        pFile: POINTER(Windows.Win32.Security.WinTrust.WINTRUST_FILE_INFO_head)
        pCatalog: POINTER(Windows.Win32.Security.WinTrust.WINTRUST_CATALOG_INFO_head)
        pBlob: POINTER(Windows.Win32.Security.WinTrust.WINTRUST_BLOB_INFO_head)
        pSgnr: POINTER(Windows.Win32.Security.WinTrust.WINTRUST_SGNR_INFO_head)
        pCert: POINTER(Windows.Win32.Security.WinTrust.WINTRUST_CERT_INFO_head)
WINTRUST_DATA_PROVIDER_FLAGS = UInt32
WTD_USE_IE4_TRUST_FLAG: WINTRUST_DATA_PROVIDER_FLAGS = 1
WTD_NO_IE4_CHAIN_FLAG: WINTRUST_DATA_PROVIDER_FLAGS = 2
WTD_NO_POLICY_USAGE_FLAG: WINTRUST_DATA_PROVIDER_FLAGS = 4
WTD_REVOCATION_CHECK_NONE: WINTRUST_DATA_PROVIDER_FLAGS = 16
WTD_REVOCATION_CHECK_END_CERT: WINTRUST_DATA_PROVIDER_FLAGS = 32
WTD_REVOCATION_CHECK_CHAIN: WINTRUST_DATA_PROVIDER_FLAGS = 64
WTD_REVOCATION_CHECK_CHAIN_EXCLUDE_ROOT: WINTRUST_DATA_PROVIDER_FLAGS = 128
WTD_SAFER_FLAG: WINTRUST_DATA_PROVIDER_FLAGS = 256
WTD_HASH_ONLY_FLAG: WINTRUST_DATA_PROVIDER_FLAGS = 512
WTD_USE_DEFAULT_OSVER_CHECK: WINTRUST_DATA_PROVIDER_FLAGS = 1024
WTD_LIFETIME_SIGNING_FLAG: WINTRUST_DATA_PROVIDER_FLAGS = 2048
WTD_CACHE_ONLY_URL_RETRIEVAL: WINTRUST_DATA_PROVIDER_FLAGS = 4096
WTD_DISABLE_MD2_MD4: WINTRUST_DATA_PROVIDER_FLAGS = 8192
WTD_MOTW: WINTRUST_DATA_PROVIDER_FLAGS = 16384
WINTRUST_DATA_REVOCATION_CHECKS = UInt32
WTD_REVOKE_NONE: WINTRUST_DATA_REVOCATION_CHECKS = 0
WTD_REVOKE_WHOLECHAIN: WINTRUST_DATA_REVOCATION_CHECKS = 1
WINTRUST_DATA_STATE_ACTION = UInt32
WTD_STATEACTION_IGNORE: WINTRUST_DATA_STATE_ACTION = 0
WTD_STATEACTION_VERIFY: WINTRUST_DATA_STATE_ACTION = 1
WTD_STATEACTION_CLOSE: WINTRUST_DATA_STATE_ACTION = 2
WTD_STATEACTION_AUTO_CACHE: WINTRUST_DATA_STATE_ACTION = 3
WTD_STATEACTION_AUTO_CACHE_FLUSH: WINTRUST_DATA_STATE_ACTION = 4
WINTRUST_DATA_UICHOICE = UInt32
WTD_UI_ALL: WINTRUST_DATA_UICHOICE = 1
WTD_UI_NONE: WINTRUST_DATA_UICHOICE = 2
WTD_UI_NOBAD: WINTRUST_DATA_UICHOICE = 3
WTD_UI_NOGOOD: WINTRUST_DATA_UICHOICE = 4
WINTRUST_DATA_UICONTEXT = UInt32
WTD_UICONTEXT_EXECUTE: WINTRUST_DATA_UICONTEXT = 0
WTD_UICONTEXT_INSTALL: WINTRUST_DATA_UICONTEXT = 1
WINTRUST_DATA_UNION_CHOICE = UInt32
WTD_CHOICE_FILE: WINTRUST_DATA_UNION_CHOICE = 1
WTD_CHOICE_CATALOG: WINTRUST_DATA_UNION_CHOICE = 2
WTD_CHOICE_BLOB: WINTRUST_DATA_UNION_CHOICE = 3
WTD_CHOICE_SIGNER: WINTRUST_DATA_UNION_CHOICE = 4
WTD_CHOICE_CERT: WINTRUST_DATA_UNION_CHOICE = 5
class WINTRUST_FILE_INFO(EasyCastStructure):
    cbStruct: UInt32
    pcwszFilePath: Windows.Win32.Foundation.PWSTR
    hFile: Windows.Win32.Foundation.HANDLE
    pgKnownSubject: POINTER(Guid)
WINTRUST_GET_DEFAULT_FOR_USAGE_ACTION = UInt32
DWACTION_ALLOCANDFILL: WINTRUST_GET_DEFAULT_FOR_USAGE_ACTION = 1
DWACTION_FREE: WINTRUST_GET_DEFAULT_FOR_USAGE_ACTION = 2
WINTRUST_POLICY_FLAGS = UInt32
WTPF_TRUSTTEST: WINTRUST_POLICY_FLAGS = 32
WTPF_TESTCANBEVALID: WINTRUST_POLICY_FLAGS = 128
WTPF_IGNOREEXPIRATION: WINTRUST_POLICY_FLAGS = 256
WTPF_IGNOREREVOKATION: WINTRUST_POLICY_FLAGS = 512
WTPF_OFFLINEOK_IND: WINTRUST_POLICY_FLAGS = 1024
WTPF_OFFLINEOK_COM: WINTRUST_POLICY_FLAGS = 2048
WTPF_OFFLINEOKNBU_IND: WINTRUST_POLICY_FLAGS = 4096
WTPF_OFFLINEOKNBU_COM: WINTRUST_POLICY_FLAGS = 8192
WTPF_VERIFY_V1_OFF: WINTRUST_POLICY_FLAGS = 65536
WTPF_IGNOREREVOCATIONONTS: WINTRUST_POLICY_FLAGS = 131072
WTPF_ALLOWONLYPERTRUST: WINTRUST_POLICY_FLAGS = 262144
class WINTRUST_SGNR_INFO(EasyCastStructure):
    cbStruct: UInt32
    pcwszDisplayName: Windows.Win32.Foundation.PWSTR
    psSignerInfo: POINTER(Windows.Win32.Security.Cryptography.CMSG_SIGNER_INFO_head)
    chStores: UInt32
    pahStores: POINTER(Windows.Win32.Security.Cryptography.HCERTSTORE)
class WINTRUST_SIGNATURE_SETTINGS(EasyCastStructure):
    cbStruct: UInt32
    dwIndex: UInt32
    dwFlags: Windows.Win32.Security.WinTrust.WINTRUST_SIGNATURE_SETTINGS_FLAGS
    cSecondarySigs: UInt32
    dwVerifiedSigIndex: UInt32
    pCryptoPolicy: POINTER(Windows.Win32.Security.Cryptography.CERT_STRONG_SIGN_PARA_head)
WINTRUST_SIGNATURE_SETTINGS_FLAGS = UInt32
WSS_VERIFY_SPECIFIC: WINTRUST_SIGNATURE_SETTINGS_FLAGS = 1
WSS_GET_SECONDARY_SIG_COUNT: WINTRUST_SIGNATURE_SETTINGS_FLAGS = 2
class WIN_CERTIFICATE(EasyCastStructure):
    dwLength: UInt32
    wRevision: UInt16
    wCertificateType: UInt16
    bCertificate: Byte * 1
class WIN_SPUB_TRUSTED_PUBLISHER_DATA(EasyCastStructure):
    hClientToken: Windows.Win32.Foundation.HANDLE
    lpCertificate: POINTER(Windows.Win32.Security.WinTrust.WIN_CERTIFICATE_head)
class WIN_TRUST_ACTDATA_CONTEXT_WITH_SUBJECT(EasyCastStructure):
    hClientToken: Windows.Win32.Foundation.HANDLE
    SubjectType: POINTER(Guid)
    Subject: c_void_p
class WIN_TRUST_ACTDATA_SUBJECT_ONLY(EasyCastStructure):
    SubjectType: POINTER(Guid)
    Subject: c_void_p
class WIN_TRUST_SUBJECT_FILE(EasyCastStructure):
    hFile: Windows.Win32.Foundation.HANDLE
    lpPath: Windows.Win32.Foundation.PWSTR
class WIN_TRUST_SUBJECT_FILE_AND_DISPLAY(EasyCastStructure):
    hFile: Windows.Win32.Foundation.HANDLE
    lpPath: Windows.Win32.Foundation.PWSTR
    lpDisplayName: Windows.Win32.Foundation.PWSTR
class WTD_GENERIC_CHAIN_POLICY_CREATE_INFO(EasyCastStructure):
    Anonymous: _Anonymous_e__Union
    hChainEngine: Windows.Win32.Security.Cryptography.HCERTCHAINENGINE
    pChainPara: POINTER(Windows.Win32.Security.Cryptography.CERT_CHAIN_PARA_head)
    dwFlags: UInt32
    pvReserved: c_void_p
    class _Anonymous_e__Union(EasyCastUnion):
        cbStruct: UInt32
        cbSize: UInt32
class WTD_GENERIC_CHAIN_POLICY_DATA(EasyCastStructure):
    Anonymous: _Anonymous_e__Union
    pSignerChainInfo: POINTER(Windows.Win32.Security.WinTrust.WTD_GENERIC_CHAIN_POLICY_CREATE_INFO_head)
    pCounterSignerChainInfo: POINTER(Windows.Win32.Security.WinTrust.WTD_GENERIC_CHAIN_POLICY_CREATE_INFO_head)
    pfnPolicyCallback: Windows.Win32.Security.WinTrust.PFN_WTD_GENERIC_CHAIN_POLICY_CALLBACK
    pvPolicyArg: c_void_p
    class _Anonymous_e__Union(EasyCastUnion):
        cbStruct: UInt32
        cbSize: UInt32
class WTD_GENERIC_CHAIN_POLICY_SIGNER_INFO(EasyCastStructure):
    Anonymous: _Anonymous_e__Union
    pChainContext: POINTER(Windows.Win32.Security.Cryptography.CERT_CHAIN_CONTEXT_head)
    dwSignerType: UInt32
    pMsgSignerInfo: POINTER(Windows.Win32.Security.Cryptography.CMSG_SIGNER_INFO_head)
    dwError: UInt32
    cCounterSigner: UInt32
    rgpCounterSigner: POINTER(POINTER(Windows.Win32.Security.WinTrust.WTD_GENERIC_CHAIN_POLICY_SIGNER_INFO_head))
    class _Anonymous_e__Union(EasyCastUnion):
        cbStruct: UInt32
        cbSize: UInt32
make_head(_module, 'CAT_MEMBERINFO')
make_head(_module, 'CAT_MEMBERINFO2')
make_head(_module, 'CAT_NAMEVALUE')
make_head(_module, 'CONFIG_CI_PROV_INFO')
make_head(_module, 'CONFIG_CI_PROV_INFO_RESULT')
make_head(_module, 'CRYPT_PROVIDER_CERT')
make_head(_module, 'CRYPT_PROVIDER_DATA')
make_head(_module, 'CRYPT_PROVIDER_DEFUSAGE')
make_head(_module, 'CRYPT_PROVIDER_FUNCTIONS')
make_head(_module, 'CRYPT_PROVIDER_PRIVDATA')
make_head(_module, 'CRYPT_PROVIDER_REGDEFUSAGE')
make_head(_module, 'CRYPT_PROVIDER_SGNR')
make_head(_module, 'CRYPT_PROVIDER_SIGSTATE')
make_head(_module, 'CRYPT_PROVUI_DATA')
make_head(_module, 'CRYPT_PROVUI_FUNCS')
make_head(_module, 'CRYPT_REGISTER_ACTIONID')
make_head(_module, 'CRYPT_TRUST_REG_ENTRY')
make_head(_module, 'DRIVER_VER_INFO')
make_head(_module, 'DRIVER_VER_MAJORMINOR')
make_head(_module, 'INTENT_TO_SEAL_ATTRIBUTE')
make_head(_module, 'PFN_ALLOCANDFILLDEFUSAGE')
make_head(_module, 'PFN_CPD_ADD_CERT')
make_head(_module, 'PFN_CPD_ADD_PRIVDATA')
make_head(_module, 'PFN_CPD_ADD_SGNR')
make_head(_module, 'PFN_CPD_ADD_STORE')
make_head(_module, 'PFN_CPD_MEM_ALLOC')
make_head(_module, 'PFN_CPD_MEM_FREE')
make_head(_module, 'PFN_FREEDEFUSAGE')
make_head(_module, 'PFN_PROVIDER_CERTCHKPOLICY_CALL')
make_head(_module, 'PFN_PROVIDER_CERTTRUST_CALL')
make_head(_module, 'PFN_PROVIDER_CLEANUP_CALL')
make_head(_module, 'PFN_PROVIDER_FINALPOLICY_CALL')
make_head(_module, 'PFN_PROVIDER_INIT_CALL')
make_head(_module, 'PFN_PROVIDER_OBJTRUST_CALL')
make_head(_module, 'PFN_PROVIDER_SIGTRUST_CALL')
make_head(_module, 'PFN_PROVIDER_TESTFINALPOLICY_CALL')
make_head(_module, 'PFN_PROVUI_CALL')
make_head(_module, 'PFN_WTD_GENERIC_CHAIN_POLICY_CALLBACK')
make_head(_module, 'PROVDATA_SIP')
make_head(_module, 'SEALING_SIGNATURE_ATTRIBUTE')
make_head(_module, 'SEALING_TIMESTAMP_ATTRIBUTE')
make_head(_module, 'SPC_FINANCIAL_CRITERIA')
make_head(_module, 'SPC_IMAGE')
make_head(_module, 'SPC_INDIRECT_DATA_CONTENT')
make_head(_module, 'SPC_LINK')
make_head(_module, 'SPC_PE_IMAGE_DATA')
make_head(_module, 'SPC_SERIALIZED_OBJECT')
make_head(_module, 'SPC_SIGINFO')
make_head(_module, 'SPC_SP_AGENCY_INFO')
make_head(_module, 'SPC_SP_OPUS_INFO')
make_head(_module, 'SPC_STATEMENT_TYPE')
make_head(_module, 'WINTRUST_BLOB_INFO')
make_head(_module, 'WINTRUST_CATALOG_INFO')
make_head(_module, 'WINTRUST_CERT_INFO')
make_head(_module, 'WINTRUST_DATA')
make_head(_module, 'WINTRUST_FILE_INFO')
make_head(_module, 'WINTRUST_SGNR_INFO')
make_head(_module, 'WINTRUST_SIGNATURE_SETTINGS')
make_head(_module, 'WIN_CERTIFICATE')
make_head(_module, 'WIN_SPUB_TRUSTED_PUBLISHER_DATA')
make_head(_module, 'WIN_TRUST_ACTDATA_CONTEXT_WITH_SUBJECT')
make_head(_module, 'WIN_TRUST_ACTDATA_SUBJECT_ONLY')
make_head(_module, 'WIN_TRUST_SUBJECT_FILE')
make_head(_module, 'WIN_TRUST_SUBJECT_FILE_AND_DISPLAY')
make_head(_module, 'WTD_GENERIC_CHAIN_POLICY_CREATE_INFO')
make_head(_module, 'WTD_GENERIC_CHAIN_POLICY_DATA')
make_head(_module, 'WTD_GENERIC_CHAIN_POLICY_SIGNER_INFO')
