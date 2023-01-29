from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Security.Cryptography
import win32more.Security.Cryptography.Sip
import win32more.Security.WinTrust
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
SPC_SP_AGENCY_INFO_STRUCT: win32more.Foundation.PSTR = 2000
SPC_MINIMAL_CRITERIA_STRUCT: win32more.Foundation.PSTR = 2001
SPC_FINANCIAL_CRITERIA_STRUCT: win32more.Foundation.PSTR = 2002
SPC_INDIRECT_DATA_CONTENT_STRUCT: win32more.Foundation.PSTR = 2003
SPC_PE_IMAGE_DATA_STRUCT: win32more.Foundation.PSTR = 2004
SPC_LINK_STRUCT: win32more.Foundation.PSTR = 2005
SPC_STATEMENT_TYPE_STRUCT: win32more.Foundation.PSTR = 2006
SPC_SP_OPUS_INFO_STRUCT: win32more.Foundation.PSTR = 2007
SPC_CAB_DATA_STRUCT: win32more.Foundation.PSTR = 2008
SPC_JAVA_CLASS_DATA_STRUCT: win32more.Foundation.PSTR = 2009
INTENT_TO_SEAL_ATTRIBUTE_STRUCT: win32more.Foundation.PSTR = 2010
SEALING_SIGNATURE_ATTRIBUTE_STRUCT: win32more.Foundation.PSTR = 2011
SEALING_TIMESTAMP_ATTRIBUTE_STRUCT: win32more.Foundation.PSTR = 2012
SPC_SIGINFO_STRUCT: win32more.Foundation.PSTR = 2130
CAT_NAMEVALUE_STRUCT: win32more.Foundation.PSTR = 2221
CAT_MEMBERINFO_STRUCT: win32more.Foundation.PSTR = 2222
CAT_MEMBERINFO2_STRUCT: win32more.Foundation.PSTR = 2223
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
WT_TRUSTDBDIALOG_NO_UI_FLAG: UInt32 = 1
WT_TRUSTDBDIALOG_ONLY_PUB_TAB_FLAG: UInt32 = 2
WT_TRUSTDBDIALOG_WRITE_LEGACY_REG_FLAG: UInt32 = 256
WT_TRUSTDBDIALOG_WRITE_IEAK_STORE_FLAG: UInt32 = 512
SP_POLICY_PROVIDER_DLL_NAME: String = 'WINTRUST.DLL'
SP_INIT_FUNCTION: String = 'SoftpubInitialize'
SP_OBJTRUST_FUNCTION: String = 'SoftpubLoadMessage'
SP_SIGTRUST_FUNCTION: String = 'SoftpubLoadSignature'
SP_CHKCERT_FUNCTION: String = 'SoftpubCheckCert'
SP_FINALPOLICY_FUNCTION: String = 'SoftpubAuthenticode'
SP_CLEANUPPOLICY_FUNCTION: String = 'SoftpubCleanup'
SP_TESTDUMPPOLICY_FUNCTION_TEST: String = 'SoftpubDumpStructure'
SP_GENERIC_CERT_INIT_FUNCTION: String = 'SoftpubDefCertInit'
GENERIC_CHAIN_FINALPOLICY_FUNCTION: String = 'GenericChainFinalProv'
GENERIC_CHAIN_CERTTRUST_FUNCTION: String = 'GenericChainCertificateTrust'
HTTPS_FINALPOLICY_FUNCTION: String = 'HTTPSFinalProv'
HTTPS_CHKCERT_FUNCTION: String = 'HTTPSCheckCertProv'
HTTPS_CERTTRUST_FUNCTION: String = 'HTTPSCertificateTrust'
OFFICE_POLICY_PROVIDER_DLL_NAME: String = 'WINTRUST.DLL'
OFFICE_INITPROV_FUNCTION: String = 'OfficeInitializePolicy'
OFFICE_CLEANUPPOLICY_FUNCTION: String = 'OfficeCleanupPolicy'
DRIVER_INITPROV_FUNCTION: String = 'DriverInitializePolicy'
DRIVER_FINALPOLPROV_FUNCTION: String = 'DriverFinalPolicy'
DRIVER_CLEANUPPOLICY_FUNCTION: String = 'DriverCleanupPolicy'
CCPI_RESULT_ALLOW: UInt32 = 1
CCPI_RESULT_DENY: UInt32 = 2
CCPI_RESULT_AUDIT: UInt32 = 3
@winfunctype('WINTRUST.dll')
def WinVerifyTrust(hwnd: win32more.Foundation.HWND, pgActionID: POINTER(Guid), pWVTData: c_void_p) -> Int32: ...
@winfunctype('WINTRUST.dll')
def WinVerifyTrustEx(hwnd: win32more.Foundation.HWND, pgActionID: POINTER(Guid), pWinTrustData: POINTER(win32more.Security.WinTrust.WINTRUST_DATA_head)) -> Int32: ...
@winfunctype('WINTRUST.dll')
def WintrustGetRegPolicyFlags(pdwPolicyFlags: POINTER(win32more.Security.WinTrust.WINTRUST_POLICY_FLAGS)) -> Void: ...
@winfunctype('WINTRUST.dll')
def WintrustSetRegPolicyFlags(dwPolicyFlags: win32more.Security.WinTrust.WINTRUST_POLICY_FLAGS) -> win32more.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def WintrustAddActionID(pgActionID: POINTER(Guid), fdwFlags: UInt32, psProvInfo: POINTER(win32more.Security.WinTrust.CRYPT_REGISTER_ACTIONID_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def WintrustRemoveActionID(pgActionID: POINTER(Guid)) -> win32more.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def WintrustLoadFunctionPointers(pgActionID: POINTER(Guid), pPfns: POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_FUNCTIONS_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def WintrustAddDefaultForUsage(pszUsageOID: win32more.Foundation.PSTR, psDefUsage: POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_REGDEFUSAGE_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def WintrustGetDefaultForUsage(dwAction: win32more.Security.WinTrust.WINTRUST_GET_DEFAULT_FOR_USAGE_ACTION, pszUsageOID: win32more.Foundation.PSTR, psUsage: POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_DEFUSAGE_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def WTHelperGetProvSignerFromChain(pProvData: POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_DATA_head), idxSigner: UInt32, fCounterSigner: win32more.Foundation.BOOL, idxCounterSigner: UInt32) -> POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_SGNR_head): ...
@winfunctype('WINTRUST.dll')
def WTHelperGetProvCertFromChain(pSgnr: POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_SGNR_head), idxCert: UInt32) -> POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_CERT_head): ...
@winfunctype('WINTRUST.dll')
def WTHelperProvDataFromStateData(hStateData: win32more.Foundation.HANDLE) -> POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_DATA_head): ...
@winfunctype('WINTRUST.dll')
def WTHelperGetProvPrivateDataFromChain(pProvData: POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_DATA_head), pgProviderID: POINTER(Guid)) -> POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_PRIVDATA_head): ...
@winfunctype('WINTRUST.dll')
def WTHelperCertIsSelfSigned(dwEncoding: UInt32, pCert: POINTER(win32more.Security.Cryptography.CERT_INFO_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def WTHelperCertCheckValidSignature(pProvData: POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_DATA_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WINTRUST.dll')
def OpenPersonalTrustDBDialogEx(hwndParent: win32more.Foundation.HWND, dwFlags: UInt32, pvReserved: POINTER(c_void_p)) -> win32more.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def OpenPersonalTrustDBDialog(hwndParent: win32more.Foundation.HWND) -> win32more.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def WintrustSetDefaultIncludePEPageHashes(fIncludePEPageHashes: win32more.Foundation.BOOL) -> Void: ...
class CAT_MEMBERINFO(Structure):
    pwszSubjGuid: win32more.Foundation.PWSTR
    dwCertVersion: UInt32
class CAT_MEMBERINFO2(Structure):
    SubjectGuid: Guid
    dwCertVersion: UInt32
class CAT_NAMEVALUE(Structure):
    pwszTag: win32more.Foundation.PWSTR
    fdwFlags: UInt32
    Value: win32more.Security.Cryptography.CRYPT_INTEGER_BLOB
class CONFIG_CI_PROV_INFO(Structure):
    cbSize: UInt32
    dwPolicies: UInt32
    pPolicies: POINTER(win32more.Security.Cryptography.CRYPT_INTEGER_BLOB_head)
    result: win32more.Security.WinTrust.CONFIG_CI_PROV_INFO_RESULT
    dwScenario: UInt32
class CONFIG_CI_PROV_INFO_RESULT(Structure):
    hr: win32more.Foundation.HRESULT
    dwResult: UInt32
    dwPolicyIndex: UInt32
    fIsExplicitDeny: win32more.Foundation.BOOLEAN
class CRYPT_PROVIDER_CERT(Structure):
    cbStruct: UInt32
    pCert: POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head)
    fCommercial: win32more.Foundation.BOOL
    fTrustedRoot: win32more.Foundation.BOOL
    fSelfSigned: win32more.Foundation.BOOL
    fTestCert: win32more.Foundation.BOOL
    dwRevokedReason: UInt32
    dwConfidence: UInt32
    dwError: UInt32
    pTrustListContext: POINTER(win32more.Security.Cryptography.CTL_CONTEXT_head)
    fTrustListSignerCert: win32more.Foundation.BOOL
    pCtlContext: POINTER(win32more.Security.Cryptography.CTL_CONTEXT_head)
    dwCtlError: UInt32
    fIsCyclic: win32more.Foundation.BOOL
    pChainElement: POINTER(win32more.Security.Cryptography.CERT_CHAIN_ELEMENT_head)
class CRYPT_PROVIDER_DATA(Structure):
    cbStruct: UInt32
    pWintrustData: POINTER(win32more.Security.WinTrust.WINTRUST_DATA_head)
    fOpenedFile: win32more.Foundation.BOOL
    hWndParent: win32more.Foundation.HWND
    pgActionID: POINTER(Guid)
    hProv: UIntPtr
    dwError: UInt32
    dwRegSecuritySettings: UInt32
    dwRegPolicySettings: UInt32
    psPfns: POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_FUNCTIONS_head)
    cdwTrustStepErrors: UInt32
    padwTrustStepErrors: POINTER(UInt32)
    chStores: UInt32
    pahStores: POINTER(win32more.Security.Cryptography.HCERTSTORE)
    dwEncoding: UInt32
    hMsg: c_void_p
    csSigners: UInt32
    pasSigners: POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_SGNR_head)
    csProvPrivData: UInt32
    pasProvPrivData: POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_PRIVDATA_head)
    dwSubjectChoice: UInt32
    Anonymous: _Anonymous_e__Union
    pszUsageOID: win32more.Foundation.PSTR
    fRecallWithState: win32more.Foundation.BOOL
    sftSystemTime: win32more.Foundation.FILETIME
    pszCTLSignerUsageOID: win32more.Foundation.PSTR
    dwProvFlags: UInt32
    dwFinalError: UInt32
    pRequestUsage: POINTER(win32more.Security.Cryptography.CERT_USAGE_MATCH_head)
    dwTrustPubSettings: UInt32
    dwUIStateFlags: UInt32
    pSigState: POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_SIGSTATE_head)
    pSigSettings: POINTER(win32more.Security.WinTrust.WINTRUST_SIGNATURE_SETTINGS_head)
    class _Anonymous_e__Union(Union):
        pPDSip: POINTER(win32more.Security.WinTrust.PROVDATA_SIP_head)
class CRYPT_PROVIDER_DEFUSAGE(Structure):
    cbStruct: UInt32
    gActionID: Guid
    pDefPolicyCallbackData: c_void_p
    pDefSIPClientData: c_void_p
class CRYPT_PROVIDER_FUNCTIONS(Structure):
    cbStruct: UInt32
    pfnAlloc: win32more.Security.WinTrust.PFN_CPD_MEM_ALLOC
    pfnFree: win32more.Security.WinTrust.PFN_CPD_MEM_FREE
    pfnAddStore2Chain: win32more.Security.WinTrust.PFN_CPD_ADD_STORE
    pfnAddSgnr2Chain: win32more.Security.WinTrust.PFN_CPD_ADD_SGNR
    pfnAddCert2Chain: win32more.Security.WinTrust.PFN_CPD_ADD_CERT
    pfnAddPrivData2Chain: win32more.Security.WinTrust.PFN_CPD_ADD_PRIVDATA
    pfnInitialize: win32more.Security.WinTrust.PFN_PROVIDER_INIT_CALL
    pfnObjectTrust: win32more.Security.WinTrust.PFN_PROVIDER_OBJTRUST_CALL
    pfnSignatureTrust: win32more.Security.WinTrust.PFN_PROVIDER_SIGTRUST_CALL
    pfnCertificateTrust: win32more.Security.WinTrust.PFN_PROVIDER_CERTTRUST_CALL
    pfnFinalPolicy: win32more.Security.WinTrust.PFN_PROVIDER_FINALPOLICY_CALL
    pfnCertCheckPolicy: win32more.Security.WinTrust.PFN_PROVIDER_CERTCHKPOLICY_CALL
    pfnTestFinalPolicy: win32more.Security.WinTrust.PFN_PROVIDER_TESTFINALPOLICY_CALL
    psUIpfns: POINTER(win32more.Security.WinTrust.CRYPT_PROVUI_FUNCS_head)
    pfnCleanupPolicy: win32more.Security.WinTrust.PFN_PROVIDER_CLEANUP_CALL
class CRYPT_PROVIDER_PRIVDATA(Structure):
    cbStruct: UInt32
    gProviderID: Guid
    cbProvData: UInt32
    pvProvData: c_void_p
class CRYPT_PROVIDER_REGDEFUSAGE(Structure):
    cbStruct: UInt32
    pgActionID: POINTER(Guid)
    pwszDllName: win32more.Foundation.PWSTR
    pwszLoadCallbackDataFunctionName: win32more.Foundation.PSTR
    pwszFreeCallbackDataFunctionName: win32more.Foundation.PSTR
class CRYPT_PROVIDER_SGNR(Structure):
    cbStruct: UInt32
    sftVerifyAsOf: win32more.Foundation.FILETIME
    csCertChain: UInt32
    pasCertChain: POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_CERT_head)
    dwSignerType: UInt32
    psSigner: POINTER(win32more.Security.Cryptography.CMSG_SIGNER_INFO_head)
    dwError: UInt32
    csCounterSigners: UInt32
    pasCounterSigners: POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_SGNR_head)
    pChainContext: POINTER(win32more.Security.Cryptography.CERT_CHAIN_CONTEXT_head)
class CRYPT_PROVIDER_SIGSTATE(Structure):
    cbStruct: UInt32
    rhSecondarySigs: POINTER(c_void_p)
    hPrimarySig: c_void_p
    fFirstAttemptMade: win32more.Foundation.BOOL
    fNoMoreSigs: win32more.Foundation.BOOL
    cSecondarySigs: UInt32
    dwCurrentIndex: UInt32
    fSupportMultiSig: win32more.Foundation.BOOL
    dwCryptoPolicySupport: UInt32
    iAttemptCount: UInt32
    fCheckedSealing: win32more.Foundation.BOOL
    pSealingSignature: POINTER(win32more.Security.WinTrust.SEALING_SIGNATURE_ATTRIBUTE_head)
class CRYPT_PROVUI_DATA(Structure):
    cbStruct: UInt32
    dwFinalError: UInt32
    pYesButtonText: win32more.Foundation.PWSTR
    pNoButtonText: win32more.Foundation.PWSTR
    pMoreInfoButtonText: win32more.Foundation.PWSTR
    pAdvancedLinkText: win32more.Foundation.PWSTR
    pCopyActionText: win32more.Foundation.PWSTR
    pCopyActionTextNoTS: win32more.Foundation.PWSTR
    pCopyActionTextNotSigned: win32more.Foundation.PWSTR
class CRYPT_PROVUI_FUNCS(Structure):
    cbStruct: UInt32
    psUIData: POINTER(win32more.Security.WinTrust.CRYPT_PROVUI_DATA_head)
    pfnOnMoreInfoClick: win32more.Security.WinTrust.PFN_PROVUI_CALL
    pfnOnMoreInfoClickDefault: win32more.Security.WinTrust.PFN_PROVUI_CALL
    pfnOnAdvancedClick: win32more.Security.WinTrust.PFN_PROVUI_CALL
    pfnOnAdvancedClickDefault: win32more.Security.WinTrust.PFN_PROVUI_CALL
class CRYPT_REGISTER_ACTIONID(Structure):
    cbStruct: UInt32
    sInitProvider: win32more.Security.WinTrust.CRYPT_TRUST_REG_ENTRY
    sObjectProvider: win32more.Security.WinTrust.CRYPT_TRUST_REG_ENTRY
    sSignatureProvider: win32more.Security.WinTrust.CRYPT_TRUST_REG_ENTRY
    sCertificateProvider: win32more.Security.WinTrust.CRYPT_TRUST_REG_ENTRY
    sCertificatePolicyProvider: win32more.Security.WinTrust.CRYPT_TRUST_REG_ENTRY
    sFinalPolicyProvider: win32more.Security.WinTrust.CRYPT_TRUST_REG_ENTRY
    sTestPolicyProvider: win32more.Security.WinTrust.CRYPT_TRUST_REG_ENTRY
    sCleanupProvider: win32more.Security.WinTrust.CRYPT_TRUST_REG_ENTRY
class CRYPT_TRUST_REG_ENTRY(Structure):
    cbStruct: UInt32
    pwszDLLName: win32more.Foundation.PWSTR
    pwszFunctionName: win32more.Foundation.PWSTR
class DRIVER_VER_INFO(Structure):
    cbStruct: UInt32
    dwReserved1: UIntPtr
    dwReserved2: UIntPtr
    dwPlatform: UInt32
    dwVersion: UInt32
    wszVersion: Char * 260
    wszSignedBy: Char * 260
    pcSignerCertContext: POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head)
    sOSVersionLow: win32more.Security.WinTrust.DRIVER_VER_MAJORMINOR
    sOSVersionHigh: win32more.Security.WinTrust.DRIVER_VER_MAJORMINOR
    dwBuildNumberLow: UInt32
    dwBuildNumberHigh: UInt32
class DRIVER_VER_MAJORMINOR(Structure):
    dwMajor: UInt32
    dwMinor: UInt32
class INTENT_TO_SEAL_ATTRIBUTE(Structure):
    version: UInt32
    seal: win32more.Foundation.BOOLEAN
@winfunctype_pointer
def PFN_ALLOCANDFILLDEFUSAGE(pszUsageOID: win32more.Foundation.PSTR, psDefUsage: POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_DEFUSAGE_head)) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def PFN_CPD_ADD_CERT(pProvData: POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_DATA_head), idxSigner: UInt32, fCounterSigner: win32more.Foundation.BOOL, idxCounterSigner: UInt32, pCert2Add: POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head)) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def PFN_CPD_ADD_PRIVDATA(pProvData: POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_DATA_head), pPrivData2Add: POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_PRIVDATA_head)) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def PFN_CPD_ADD_SGNR(pProvData: POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_DATA_head), fCounterSigner: win32more.Foundation.BOOL, idxSigner: UInt32, pSgnr2Add: POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_SGNR_head)) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def PFN_CPD_ADD_STORE(pProvData: POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_DATA_head), hStore2Add: win32more.Security.Cryptography.HCERTSTORE) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def PFN_CPD_MEM_ALLOC(cbSize: UInt32) -> c_void_p: ...
@winfunctype_pointer
def PFN_CPD_MEM_FREE(pvMem2Free: c_void_p) -> Void: ...
@winfunctype_pointer
def PFN_FREEDEFUSAGE(pszUsageOID: win32more.Foundation.PSTR, psDefUsage: POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_DEFUSAGE_head)) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def PFN_PROVIDER_CERTCHKPOLICY_CALL(pProvData: POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_DATA_head), idxSigner: UInt32, fCounterSignerChain: win32more.Foundation.BOOL, idxCounterSigner: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def PFN_PROVIDER_CERTTRUST_CALL(pProvData: POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_DATA_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def PFN_PROVIDER_CLEANUP_CALL(pProvData: POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_DATA_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def PFN_PROVIDER_FINALPOLICY_CALL(pProvData: POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_DATA_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def PFN_PROVIDER_INIT_CALL(pProvData: POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_DATA_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def PFN_PROVIDER_OBJTRUST_CALL(pProvData: POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_DATA_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def PFN_PROVIDER_SIGTRUST_CALL(pProvData: POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_DATA_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def PFN_PROVIDER_TESTFINALPOLICY_CALL(pProvData: POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_DATA_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def PFN_PROVUI_CALL(hWndSecurityDialog: win32more.Foundation.HWND, pProvData: POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_DATA_head)) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def PFN_WTD_GENERIC_CHAIN_POLICY_CALLBACK(pProvData: POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_DATA_head), dwStepError: UInt32, dwRegPolicySettings: UInt32, cSigner: UInt32, rgpSigner: POINTER(POINTER(win32more.Security.WinTrust.WTD_GENERIC_CHAIN_POLICY_SIGNER_INFO_head)), pvPolicyArg: c_void_p) -> win32more.Foundation.HRESULT: ...
class PROVDATA_SIP(Structure):
    cbStruct: UInt32
    gSubject: Guid
    pSip: POINTER(win32more.Security.Cryptography.Sip.SIP_DISPATCH_INFO_head)
    pCATSip: POINTER(win32more.Security.Cryptography.Sip.SIP_DISPATCH_INFO_head)
    psSipSubjectInfo: POINTER(win32more.Security.Cryptography.Sip.SIP_SUBJECTINFO_head)
    psSipCATSubjectInfo: POINTER(win32more.Security.Cryptography.Sip.SIP_SUBJECTINFO_head)
    psIndirectData: POINTER(win32more.Security.Cryptography.Sip.SIP_INDIRECT_DATA_head)
class SEALING_SIGNATURE_ATTRIBUTE(Structure):
    version: UInt32
    signerIndex: UInt32
    signatureAlgorithm: win32more.Security.Cryptography.CRYPT_ALGORITHM_IDENTIFIER
    encryptedDigest: win32more.Security.Cryptography.CRYPT_INTEGER_BLOB
class SEALING_TIMESTAMP_ATTRIBUTE(Structure):
    version: UInt32
    signerIndex: UInt32
    sealTimeStampToken: win32more.Security.Cryptography.CRYPT_INTEGER_BLOB
class SPC_FINANCIAL_CRITERIA(Structure):
    fFinancialInfoAvailable: win32more.Foundation.BOOL
    fMeetsCriteria: win32more.Foundation.BOOL
class SPC_IMAGE(Structure):
    pImageLink: POINTER(win32more.Security.WinTrust.SPC_LINK_head)
    Bitmap: win32more.Security.Cryptography.CRYPT_INTEGER_BLOB
    Metafile: win32more.Security.Cryptography.CRYPT_INTEGER_BLOB
    EnhancedMetafile: win32more.Security.Cryptography.CRYPT_INTEGER_BLOB
    GifFile: win32more.Security.Cryptography.CRYPT_INTEGER_BLOB
class SPC_INDIRECT_DATA_CONTENT(Structure):
    Data: win32more.Security.Cryptography.CRYPT_ATTRIBUTE_TYPE_VALUE
    DigestAlgorithm: win32more.Security.Cryptography.CRYPT_ALGORITHM_IDENTIFIER
    Digest: win32more.Security.Cryptography.CRYPT_INTEGER_BLOB
class SPC_LINK(Structure):
    dwLinkChoice: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        pwszUrl: win32more.Foundation.PWSTR
        Moniker: win32more.Security.WinTrust.SPC_SERIALIZED_OBJECT
        pwszFile: win32more.Foundation.PWSTR
class SPC_PE_IMAGE_DATA(Structure):
    Flags: win32more.Security.Cryptography.CRYPT_BIT_BLOB
    pFile: POINTER(win32more.Security.WinTrust.SPC_LINK_head)
class SPC_SERIALIZED_OBJECT(Structure):
    ClassId: Byte * 16
    SerializedData: win32more.Security.Cryptography.CRYPT_INTEGER_BLOB
class SPC_SIGINFO(Structure):
    dwSipVersion: UInt32
    gSIPGuid: Guid
    dwReserved1: UInt32
    dwReserved2: UInt32
    dwReserved3: UInt32
    dwReserved4: UInt32
    dwReserved5: UInt32
class SPC_SP_AGENCY_INFO(Structure):
    pPolicyInformation: POINTER(win32more.Security.WinTrust.SPC_LINK_head)
    pwszPolicyDisplayText: win32more.Foundation.PWSTR
    pLogoImage: POINTER(win32more.Security.WinTrust.SPC_IMAGE_head)
    pLogoLink: POINTER(win32more.Security.WinTrust.SPC_LINK_head)
class SPC_SP_OPUS_INFO(Structure):
    pwszProgramName: win32more.Foundation.PWSTR
    pMoreInfo: POINTER(win32more.Security.WinTrust.SPC_LINK_head)
    pPublisherInfo: POINTER(win32more.Security.WinTrust.SPC_LINK_head)
class SPC_STATEMENT_TYPE(Structure):
    cKeyPurposeId: UInt32
    rgpszKeyPurposeId: POINTER(win32more.Foundation.PSTR)
class WIN_CERTIFICATE(Structure):
    dwLength: UInt32
    wRevision: UInt16
    wCertificateType: UInt16
    bCertificate: Byte * 1
class WIN_SPUB_TRUSTED_PUBLISHER_DATA(Structure):
    hClientToken: win32more.Foundation.HANDLE
    lpCertificate: POINTER(win32more.Security.WinTrust.WIN_CERTIFICATE_head)
class WIN_TRUST_ACTDATA_CONTEXT_WITH_SUBJECT(Structure):
    hClientToken: win32more.Foundation.HANDLE
    SubjectType: POINTER(Guid)
    Subject: c_void_p
class WIN_TRUST_ACTDATA_SUBJECT_ONLY(Structure):
    SubjectType: POINTER(Guid)
    Subject: c_void_p
class WIN_TRUST_SUBJECT_FILE(Structure):
    hFile: win32more.Foundation.HANDLE
    lpPath: win32more.Foundation.PWSTR
class WIN_TRUST_SUBJECT_FILE_AND_DISPLAY(Structure):
    hFile: win32more.Foundation.HANDLE
    lpPath: win32more.Foundation.PWSTR
    lpDisplayName: win32more.Foundation.PWSTR
class WINTRUST_BLOB_INFO(Structure):
    cbStruct: UInt32
    gSubject: Guid
    pcwszDisplayName: win32more.Foundation.PWSTR
    cbMemObject: UInt32
    pbMemObject: c_char_p_no
    cbMemSignedMsg: UInt32
    pbMemSignedMsg: c_char_p_no
class WINTRUST_CATALOG_INFO(Structure):
    cbStruct: UInt32
    dwCatalogVersion: UInt32
    pcwszCatalogFilePath: win32more.Foundation.PWSTR
    pcwszMemberTag: win32more.Foundation.PWSTR
    pcwszMemberFilePath: win32more.Foundation.PWSTR
    hMemberFile: win32more.Foundation.HANDLE
    pbCalculatedFileHash: c_char_p_no
    cbCalculatedFileHash: UInt32
    pcCatalogContext: POINTER(win32more.Security.Cryptography.CTL_CONTEXT_head)
    hCatAdmin: IntPtr
class WINTRUST_CERT_INFO(Structure):
    cbStruct: UInt32
    pcwszDisplayName: win32more.Foundation.PWSTR
    psCertContext: POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head)
    chStores: UInt32
    pahStores: POINTER(win32more.Security.Cryptography.HCERTSTORE)
    dwFlags: UInt32
    psftVerifyAsOf: POINTER(win32more.Foundation.FILETIME_head)
class WINTRUST_DATA(Structure):
    cbStruct: UInt32
    pPolicyCallbackData: c_void_p
    pSIPClientData: c_void_p
    dwUIChoice: win32more.Security.WinTrust.WINTRUST_DATA_UICHOICE
    fdwRevocationChecks: win32more.Security.WinTrust.WINTRUST_DATA_REVOCATION_CHECKS
    dwUnionChoice: win32more.Security.WinTrust.WINTRUST_DATA_UNION_CHOICE
    Anonymous: _Anonymous_e__Union
    dwStateAction: win32more.Security.WinTrust.WINTRUST_DATA_STATE_ACTION
    hWVTStateData: win32more.Foundation.HANDLE
    pwszURLReference: win32more.Foundation.PWSTR
    dwProvFlags: win32more.Security.WinTrust.WINTRUST_DATA_PROVIDER_FLAGS
    dwUIContext: win32more.Security.WinTrust.WINTRUST_DATA_UICONTEXT
    pSignatureSettings: POINTER(win32more.Security.WinTrust.WINTRUST_SIGNATURE_SETTINGS_head)
    class _Anonymous_e__Union(Union):
        pFile: POINTER(win32more.Security.WinTrust.WINTRUST_FILE_INFO_head)
        pCatalog: POINTER(win32more.Security.WinTrust.WINTRUST_CATALOG_INFO_head)
        pBlob: POINTER(win32more.Security.WinTrust.WINTRUST_BLOB_INFO_head)
        pSgnr: POINTER(win32more.Security.WinTrust.WINTRUST_SGNR_INFO_head)
        pCert: POINTER(win32more.Security.WinTrust.WINTRUST_CERT_INFO_head)
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
class WINTRUST_FILE_INFO(Structure):
    cbStruct: UInt32
    pcwszFilePath: win32more.Foundation.PWSTR
    hFile: win32more.Foundation.HANDLE
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
class WINTRUST_SGNR_INFO(Structure):
    cbStruct: UInt32
    pcwszDisplayName: win32more.Foundation.PWSTR
    psSignerInfo: POINTER(win32more.Security.Cryptography.CMSG_SIGNER_INFO_head)
    chStores: UInt32
    pahStores: POINTER(win32more.Security.Cryptography.HCERTSTORE)
class WINTRUST_SIGNATURE_SETTINGS(Structure):
    cbStruct: UInt32
    dwIndex: UInt32
    dwFlags: win32more.Security.WinTrust.WINTRUST_SIGNATURE_SETTINGS_FLAGS
    cSecondarySigs: UInt32
    dwVerifiedSigIndex: UInt32
    pCryptoPolicy: POINTER(win32more.Security.Cryptography.CERT_STRONG_SIGN_PARA_head)
WINTRUST_SIGNATURE_SETTINGS_FLAGS = UInt32
WSS_VERIFY_SPECIFIC: WINTRUST_SIGNATURE_SETTINGS_FLAGS = 1
WSS_GET_SECONDARY_SIG_COUNT: WINTRUST_SIGNATURE_SETTINGS_FLAGS = 2
class WTD_GENERIC_CHAIN_POLICY_CREATE_INFO(Structure):
    Anonymous: _Anonymous_e__Union
    hChainEngine: win32more.Security.Cryptography.HCERTCHAINENGINE
    pChainPara: POINTER(win32more.Security.Cryptography.CERT_CHAIN_PARA_head)
    dwFlags: UInt32
    pvReserved: c_void_p
    class _Anonymous_e__Union(Union):
        cbStruct: UInt32
        cbSize: UInt32
class WTD_GENERIC_CHAIN_POLICY_DATA(Structure):
    Anonymous: _Anonymous_e__Union
    pSignerChainInfo: POINTER(win32more.Security.WinTrust.WTD_GENERIC_CHAIN_POLICY_CREATE_INFO_head)
    pCounterSignerChainInfo: POINTER(win32more.Security.WinTrust.WTD_GENERIC_CHAIN_POLICY_CREATE_INFO_head)
    pfnPolicyCallback: win32more.Security.WinTrust.PFN_WTD_GENERIC_CHAIN_POLICY_CALLBACK
    pvPolicyArg: c_void_p
    class _Anonymous_e__Union(Union):
        cbStruct: UInt32
        cbSize: UInt32
class WTD_GENERIC_CHAIN_POLICY_SIGNER_INFO(Structure):
    Anonymous: _Anonymous_e__Union
    pChainContext: POINTER(win32more.Security.Cryptography.CERT_CHAIN_CONTEXT_head)
    dwSignerType: UInt32
    pMsgSignerInfo: POINTER(win32more.Security.Cryptography.CMSG_SIGNER_INFO_head)
    dwError: UInt32
    cCounterSigner: UInt32
    rgpCounterSigner: POINTER(POINTER(win32more.Security.WinTrust.WTD_GENERIC_CHAIN_POLICY_SIGNER_INFO_head))
    class _Anonymous_e__Union(Union):
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
make_head(_module, 'WIN_CERTIFICATE')
make_head(_module, 'WIN_SPUB_TRUSTED_PUBLISHER_DATA')
make_head(_module, 'WIN_TRUST_ACTDATA_CONTEXT_WITH_SUBJECT')
make_head(_module, 'WIN_TRUST_ACTDATA_SUBJECT_ONLY')
make_head(_module, 'WIN_TRUST_SUBJECT_FILE')
make_head(_module, 'WIN_TRUST_SUBJECT_FILE_AND_DISPLAY')
make_head(_module, 'WINTRUST_BLOB_INFO')
make_head(_module, 'WINTRUST_CATALOG_INFO')
make_head(_module, 'WINTRUST_CERT_INFO')
make_head(_module, 'WINTRUST_DATA')
make_head(_module, 'WINTRUST_FILE_INFO')
make_head(_module, 'WINTRUST_SGNR_INFO')
make_head(_module, 'WINTRUST_SIGNATURE_SETTINGS')
make_head(_module, 'WTD_GENERIC_CHAIN_POLICY_CREATE_INFO')
make_head(_module, 'WTD_GENERIC_CHAIN_POLICY_DATA')
make_head(_module, 'WTD_GENERIC_CHAIN_POLICY_SIGNER_INFO')
__all__ = [
    "CAT_MEMBERINFO",
    "CAT_MEMBERINFO2",
    "CAT_MEMBERINFO2_OBJID",
    "CAT_MEMBERINFO2_STRUCT",
    "CAT_MEMBERINFO_OBJID",
    "CAT_MEMBERINFO_STRUCT",
    "CAT_NAMEVALUE",
    "CAT_NAMEVALUE_OBJID",
    "CAT_NAMEVALUE_STRUCT",
    "CCPI_RESULT_ALLOW",
    "CCPI_RESULT_AUDIT",
    "CCPI_RESULT_DENY",
    "CERT_CONFIDENCE_AUTHIDEXT",
    "CERT_CONFIDENCE_HIGHEST",
    "CERT_CONFIDENCE_HYGIENE",
    "CERT_CONFIDENCE_SIG",
    "CERT_CONFIDENCE_TIME",
    "CERT_CONFIDENCE_TIMENEST",
    "CONFIG_CI_PROV_INFO",
    "CONFIG_CI_PROV_INFO_RESULT",
    "CPD_CHOICE_SIP",
    "CPD_RETURN_LOWER_QUALITY_CHAINS",
    "CPD_REVOCATION_CHECK_CHAIN",
    "CPD_REVOCATION_CHECK_CHAIN_EXCLUDE_ROOT",
    "CPD_REVOCATION_CHECK_END_CERT",
    "CPD_REVOCATION_CHECK_NONE",
    "CPD_UISTATE_MODE_ALLOW",
    "CPD_UISTATE_MODE_BLOCK",
    "CPD_UISTATE_MODE_MASK",
    "CPD_UISTATE_MODE_PROMPT",
    "CPD_USE_NT5_CHAIN_FLAG",
    "CRYPT_PROVIDER_CERT",
    "CRYPT_PROVIDER_DATA",
    "CRYPT_PROVIDER_DEFUSAGE",
    "CRYPT_PROVIDER_FUNCTIONS",
    "CRYPT_PROVIDER_PRIVDATA",
    "CRYPT_PROVIDER_REGDEFUSAGE",
    "CRYPT_PROVIDER_SGNR",
    "CRYPT_PROVIDER_SIGSTATE",
    "CRYPT_PROVUI_DATA",
    "CRYPT_PROVUI_FUNCS",
    "CRYPT_REGISTER_ACTIONID",
    "CRYPT_TRUST_REG_ENTRY",
    "DRIVER_CLEANUPPOLICY_FUNCTION",
    "DRIVER_FINALPOLPROV_FUNCTION",
    "DRIVER_INITPROV_FUNCTION",
    "DRIVER_VER_INFO",
    "DRIVER_VER_MAJORMINOR",
    "DWACTION_ALLOCANDFILL",
    "DWACTION_FREE",
    "GENERIC_CHAIN_CERTTRUST_FUNCTION",
    "GENERIC_CHAIN_FINALPOLICY_FUNCTION",
    "HTTPS_CERTTRUST_FUNCTION",
    "HTTPS_CHKCERT_FUNCTION",
    "HTTPS_FINALPOLICY_FUNCTION",
    "INTENT_TO_SEAL_ATTRIBUTE",
    "INTENT_TO_SEAL_ATTRIBUTE_STRUCT",
    "OFFICE_CLEANUPPOLICY_FUNCTION",
    "OFFICE_INITPROV_FUNCTION",
    "OFFICE_POLICY_PROVIDER_DLL_NAME",
    "OpenPersonalTrustDBDialog",
    "OpenPersonalTrustDBDialogEx",
    "PFN_ALLOCANDFILLDEFUSAGE",
    "PFN_CPD_ADD_CERT",
    "PFN_CPD_ADD_PRIVDATA",
    "PFN_CPD_ADD_SGNR",
    "PFN_CPD_ADD_STORE",
    "PFN_CPD_MEM_ALLOC",
    "PFN_CPD_MEM_FREE",
    "PFN_FREEDEFUSAGE",
    "PFN_PROVIDER_CERTCHKPOLICY_CALL",
    "PFN_PROVIDER_CERTTRUST_CALL",
    "PFN_PROVIDER_CLEANUP_CALL",
    "PFN_PROVIDER_FINALPOLICY_CALL",
    "PFN_PROVIDER_INIT_CALL",
    "PFN_PROVIDER_OBJTRUST_CALL",
    "PFN_PROVIDER_SIGTRUST_CALL",
    "PFN_PROVIDER_TESTFINALPOLICY_CALL",
    "PFN_PROVUI_CALL",
    "PFN_WTD_GENERIC_CHAIN_POLICY_CALLBACK",
    "PROVDATA_SIP",
    "SEALING_SIGNATURE_ATTRIBUTE",
    "SEALING_SIGNATURE_ATTRIBUTE_STRUCT",
    "SEALING_TIMESTAMP_ATTRIBUTE",
    "SEALING_TIMESTAMP_ATTRIBUTE_STRUCT",
    "SGNR_TYPE_TIMESTAMP",
    "SPC_CAB_DATA_OBJID",
    "SPC_CAB_DATA_STRUCT",
    "SPC_CERT_EXTENSIONS_OBJID",
    "SPC_COMMERCIAL_SP_KEY_PURPOSE_OBJID",
    "SPC_COMMON_NAME_OBJID",
    "SPC_ENCRYPTED_DIGEST_RETRY_COUNT_OBJID",
    "SPC_FILE_LINK_CHOICE",
    "SPC_FINANCIAL_CRITERIA",
    "SPC_FINANCIAL_CRITERIA_OBJID",
    "SPC_FINANCIAL_CRITERIA_STRUCT",
    "SPC_GLUE_RDN_OBJID",
    "SPC_IMAGE",
    "SPC_INDIRECT_DATA_CONTENT",
    "SPC_INDIRECT_DATA_CONTENT_STRUCT",
    "SPC_INDIRECT_DATA_OBJID",
    "SPC_INDIVIDUAL_SP_KEY_PURPOSE_OBJID",
    "SPC_JAVA_CLASS_DATA_OBJID",
    "SPC_JAVA_CLASS_DATA_STRUCT",
    "SPC_LINK",
    "SPC_LINK_OBJID",
    "SPC_LINK_STRUCT",
    "SPC_MINIMAL_CRITERIA_OBJID",
    "SPC_MINIMAL_CRITERIA_STRUCT",
    "SPC_MONIKER_LINK_CHOICE",
    "SPC_NATURAL_AUTH_PLUGIN_OBJID",
    "SPC_PE_IMAGE_DATA",
    "SPC_PE_IMAGE_DATA_OBJID",
    "SPC_PE_IMAGE_DATA_STRUCT",
    "SPC_PE_IMAGE_PAGE_HASHES_V1_OBJID",
    "SPC_PE_IMAGE_PAGE_HASHES_V2_OBJID",
    "SPC_RAW_FILE_DATA_OBJID",
    "SPC_RELAXED_PE_MARKER_CHECK_OBJID",
    "SPC_SERIALIZED_OBJECT",
    "SPC_SIGINFO",
    "SPC_SIGINFO_OBJID",
    "SPC_SIGINFO_STRUCT",
    "SPC_SP_AGENCY_INFO",
    "SPC_SP_AGENCY_INFO_OBJID",
    "SPC_SP_AGENCY_INFO_STRUCT",
    "SPC_SP_OPUS_INFO",
    "SPC_SP_OPUS_INFO_OBJID",
    "SPC_SP_OPUS_INFO_STRUCT",
    "SPC_STATEMENT_TYPE",
    "SPC_STATEMENT_TYPE_OBJID",
    "SPC_STATEMENT_TYPE_STRUCT",
    "SPC_STRUCTURED_STORAGE_DATA_OBJID",
    "SPC_TIME_STAMP_REQUEST_OBJID",
    "SPC_URL_LINK_CHOICE",
    "SPC_UUID_LENGTH",
    "SPC_WINDOWS_HELLO_COMPATIBILITY_OBJID",
    "SP_CHKCERT_FUNCTION",
    "SP_CLEANUPPOLICY_FUNCTION",
    "SP_FINALPOLICY_FUNCTION",
    "SP_GENERIC_CERT_INIT_FUNCTION",
    "SP_INIT_FUNCTION",
    "SP_OBJTRUST_FUNCTION",
    "SP_POLICY_PROVIDER_DLL_NAME",
    "SP_SIGTRUST_FUNCTION",
    "SP_TESTDUMPPOLICY_FUNCTION_TEST",
    "TRUSTERROR_MAX_STEPS",
    "TRUSTERROR_STEP_CATALOGFILE",
    "TRUSTERROR_STEP_CERTSTORE",
    "TRUSTERROR_STEP_FILEIO",
    "TRUSTERROR_STEP_FINAL_CERTCHKPROV",
    "TRUSTERROR_STEP_FINAL_CERTPROV",
    "TRUSTERROR_STEP_FINAL_INITPROV",
    "TRUSTERROR_STEP_FINAL_OBJPROV",
    "TRUSTERROR_STEP_FINAL_POLICYPROV",
    "TRUSTERROR_STEP_FINAL_SIGPROV",
    "TRUSTERROR_STEP_FINAL_UIPROV",
    "TRUSTERROR_STEP_FINAL_WVTINIT",
    "TRUSTERROR_STEP_MESSAGE",
    "TRUSTERROR_STEP_MSG_CERTCHAIN",
    "TRUSTERROR_STEP_MSG_COUNTERSIGCERT",
    "TRUSTERROR_STEP_MSG_COUNTERSIGINFO",
    "TRUSTERROR_STEP_MSG_INNERCNT",
    "TRUSTERROR_STEP_MSG_INNERCNTTYPE",
    "TRUSTERROR_STEP_MSG_SIGNERCERT",
    "TRUSTERROR_STEP_MSG_SIGNERCOUNT",
    "TRUSTERROR_STEP_MSG_SIGNERINFO",
    "TRUSTERROR_STEP_MSG_STORE",
    "TRUSTERROR_STEP_SIP",
    "TRUSTERROR_STEP_SIPSUBJINFO",
    "TRUSTERROR_STEP_VERIFY_MSGHASH",
    "TRUSTERROR_STEP_VERIFY_MSGINDIRECTDATA",
    "TRUSTERROR_STEP_WVTPARAMS",
    "WINTRUST_BLOB_INFO",
    "WINTRUST_CATALOG_INFO",
    "WINTRUST_CERT_INFO",
    "WINTRUST_CONFIG_REGPATH",
    "WINTRUST_DATA",
    "WINTRUST_DATA_PROVIDER_FLAGS",
    "WINTRUST_DATA_REVOCATION_CHECKS",
    "WINTRUST_DATA_STATE_ACTION",
    "WINTRUST_DATA_UICHOICE",
    "WINTRUST_DATA_UICONTEXT",
    "WINTRUST_DATA_UNION_CHOICE",
    "WINTRUST_FILE_INFO",
    "WINTRUST_GET_DEFAULT_FOR_USAGE_ACTION",
    "WINTRUST_MAX_HASH_BYTES_TO_MAP_DEFAULT",
    "WINTRUST_MAX_HASH_BYTES_TO_MAP_VALUE_NAME",
    "WINTRUST_MAX_HEADER_BYTES_TO_MAP_DEFAULT",
    "WINTRUST_MAX_HEADER_BYTES_TO_MAP_VALUE_NAME",
    "WINTRUST_POLICY_FLAGS",
    "WINTRUST_SGNR_INFO",
    "WINTRUST_SIGNATURE_SETTINGS",
    "WINTRUST_SIGNATURE_SETTINGS_FLAGS",
    "WIN_CERTIFICATE",
    "WIN_CERT_REVISION_1_0",
    "WIN_CERT_REVISION_2_0",
    "WIN_CERT_TYPE_PKCS_SIGNED_DATA",
    "WIN_CERT_TYPE_RESERVED_1",
    "WIN_CERT_TYPE_TS_STACK_SIGNED",
    "WIN_CERT_TYPE_X509",
    "WIN_SPUB_TRUSTED_PUBLISHER_DATA",
    "WIN_TRUST_ACTDATA_CONTEXT_WITH_SUBJECT",
    "WIN_TRUST_ACTDATA_SUBJECT_ONLY",
    "WIN_TRUST_SUBJECT_FILE",
    "WIN_TRUST_SUBJECT_FILE_AND_DISPLAY",
    "WSS_CERTTRUST_SUPPORT",
    "WSS_GET_SECONDARY_SIG_COUNT",
    "WSS_INPUT_FLAG_MASK",
    "WSS_OBJTRUST_SUPPORT",
    "WSS_OUTPUT_FLAG_MASK",
    "WSS_OUT_FILE_SUPPORTS_SEAL",
    "WSS_OUT_HAS_SEALING_INTENT",
    "WSS_OUT_SEALING_STATUS_VERIFIED",
    "WSS_SIGTRUST_SUPPORT",
    "WSS_VERIFY_SEALING",
    "WSS_VERIFY_SPECIFIC",
    "WTCI_DONT_OPEN_STORES",
    "WTCI_OPEN_ONLY_ROOT",
    "WTCI_USE_LOCAL_MACHINE",
    "WTD_CACHE_ONLY_URL_RETRIEVAL",
    "WTD_CHOICE_BLOB",
    "WTD_CHOICE_CATALOG",
    "WTD_CHOICE_CERT",
    "WTD_CHOICE_FILE",
    "WTD_CHOICE_SIGNER",
    "WTD_CODE_INTEGRITY_DRIVER_MODE",
    "WTD_DISABLE_MD2_MD4",
    "WTD_GENERIC_CHAIN_POLICY_CREATE_INFO",
    "WTD_GENERIC_CHAIN_POLICY_DATA",
    "WTD_GENERIC_CHAIN_POLICY_SIGNER_INFO",
    "WTD_HASH_ONLY_FLAG",
    "WTD_LIFETIME_SIGNING_FLAG",
    "WTD_MOTW",
    "WTD_NO_IE4_CHAIN_FLAG",
    "WTD_NO_POLICY_USAGE_FLAG",
    "WTD_PROV_FLAGS_MASK",
    "WTD_REVOCATION_CHECK_CHAIN",
    "WTD_REVOCATION_CHECK_CHAIN_EXCLUDE_ROOT",
    "WTD_REVOCATION_CHECK_END_CERT",
    "WTD_REVOCATION_CHECK_NONE",
    "WTD_REVOKE_NONE",
    "WTD_REVOKE_WHOLECHAIN",
    "WTD_SAFER_FLAG",
    "WTD_STATEACTION_AUTO_CACHE",
    "WTD_STATEACTION_AUTO_CACHE_FLUSH",
    "WTD_STATEACTION_CLOSE",
    "WTD_STATEACTION_IGNORE",
    "WTD_STATEACTION_VERIFY",
    "WTD_UICONTEXT_EXECUTE",
    "WTD_UICONTEXT_INSTALL",
    "WTD_UI_ALL",
    "WTD_UI_NOBAD",
    "WTD_UI_NOGOOD",
    "WTD_UI_NONE",
    "WTD_USE_DEFAULT_OSVER_CHECK",
    "WTD_USE_IE4_TRUST_FLAG",
    "WTHelperCertCheckValidSignature",
    "WTHelperCertIsSelfSigned",
    "WTHelperGetProvCertFromChain",
    "WTHelperGetProvPrivateDataFromChain",
    "WTHelperGetProvSignerFromChain",
    "WTHelperProvDataFromStateData",
    "WTPF_ALLOWONLYPERTRUST",
    "WTPF_IGNOREEXPIRATION",
    "WTPF_IGNOREREVOCATIONONTS",
    "WTPF_IGNOREREVOKATION",
    "WTPF_OFFLINEOKNBU_COM",
    "WTPF_OFFLINEOKNBU_IND",
    "WTPF_OFFLINEOK_COM",
    "WTPF_OFFLINEOK_IND",
    "WTPF_TESTCANBEVALID",
    "WTPF_TRUSTTEST",
    "WTPF_VERIFY_V1_OFF",
    "WT_ADD_ACTION_ID_RET_RESULT_FLAG",
    "WT_CURRENT_VERSION",
    "WT_PROVIDER_CERTTRUST_FUNCTION",
    "WT_PROVIDER_DLL_NAME",
    "WT_TRUSTDBDIALOG_NO_UI_FLAG",
    "WT_TRUSTDBDIALOG_ONLY_PUB_TAB_FLAG",
    "WT_TRUSTDBDIALOG_WRITE_IEAK_STORE_FLAG",
    "WT_TRUSTDBDIALOG_WRITE_LEGACY_REG_FLAG",
    "WinVerifyTrust",
    "WinVerifyTrustEx",
    "WintrustAddActionID",
    "WintrustAddDefaultForUsage",
    "WintrustGetDefaultForUsage",
    "WintrustGetRegPolicyFlags",
    "WintrustLoadFunctionPointers",
    "WintrustRemoveActionID",
    "WintrustSetDefaultIncludePEPageHashes",
    "WintrustSetRegPolicyFlags",
    "szOID_ENHANCED_HASH",
    "szOID_INTENT_TO_SEAL",
    "szOID_NESTED_SIGNATURE",
    "szOID_PKCS_9_SEQUENCE_NUMBER",
    "szOID_SEALING_SIGNATURE",
    "szOID_SEALING_TIMESTAMP",
    "szOID_TRUSTED_CLIENT_AUTH_CA_LIST",
    "szOID_TRUSTED_CODESIGNING_CA_LIST",
    "szOID_TRUSTED_SERVER_AUTH_CA_LIST",
]
_arch_optional = [
]
