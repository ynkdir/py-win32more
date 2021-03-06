from win32more import *
import win32more.Foundation
import win32more.Security.Cryptography
import win32more.Security.Cryptography.Sip
import win32more.Security.WinTrust

import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
WINTRUST_MAX_HEADER_BYTES_TO_MAP_DEFAULT = 10485760
WINTRUST_MAX_HASH_BYTES_TO_MAP_DEFAULT = 1048576
WSS_VERIFY_SEALING = 4
WSS_INPUT_FLAG_MASK = 7
WSS_OUT_SEALING_STATUS_VERIFIED = 2147483648
WSS_OUT_HAS_SEALING_INTENT = 1073741824
WSS_OUT_FILE_SUPPORTS_SEAL = 536870912
WSS_OUTPUT_FLAG_MASK = 3758096384
TRUSTERROR_STEP_WVTPARAMS = 0
TRUSTERROR_STEP_FILEIO = 2
TRUSTERROR_STEP_SIP = 3
TRUSTERROR_STEP_SIPSUBJINFO = 5
TRUSTERROR_STEP_CATALOGFILE = 6
TRUSTERROR_STEP_CERTSTORE = 7
TRUSTERROR_STEP_MESSAGE = 8
TRUSTERROR_STEP_MSG_SIGNERCOUNT = 9
TRUSTERROR_STEP_MSG_INNERCNTTYPE = 10
TRUSTERROR_STEP_MSG_INNERCNT = 11
TRUSTERROR_STEP_MSG_STORE = 12
TRUSTERROR_STEP_MSG_SIGNERINFO = 13
TRUSTERROR_STEP_MSG_SIGNERCERT = 14
TRUSTERROR_STEP_MSG_CERTCHAIN = 15
TRUSTERROR_STEP_MSG_COUNTERSIGINFO = 16
TRUSTERROR_STEP_MSG_COUNTERSIGCERT = 17
TRUSTERROR_STEP_VERIFY_MSGHASH = 18
TRUSTERROR_STEP_VERIFY_MSGINDIRECTDATA = 19
TRUSTERROR_STEP_FINAL_WVTINIT = 30
TRUSTERROR_STEP_FINAL_INITPROV = 31
TRUSTERROR_STEP_FINAL_OBJPROV = 32
TRUSTERROR_STEP_FINAL_SIGPROV = 33
TRUSTERROR_STEP_FINAL_CERTPROV = 34
TRUSTERROR_STEP_FINAL_CERTCHKPROV = 35
TRUSTERROR_STEP_FINAL_POLICYPROV = 36
TRUSTERROR_STEP_FINAL_UIPROV = 37
TRUSTERROR_MAX_STEPS = 38
WSS_OBJTRUST_SUPPORT = 1
WSS_SIGTRUST_SUPPORT = 2
WSS_CERTTRUST_SUPPORT = 4
WT_CURRENT_VERSION = 512
WT_ADD_ACTION_ID_RET_RESULT_FLAG = 1
SPC_UUID_LENGTH = 16
WIN_CERT_REVISION_1_0 = 256
WIN_CERT_REVISION_2_0 = 512
WIN_CERT_TYPE_X509 = 1
WIN_CERT_TYPE_PKCS_SIGNED_DATA = 2
WIN_CERT_TYPE_RESERVED_1 = 3
WIN_CERT_TYPE_TS_STACK_SIGNED = 4
WT_TRUSTDBDIALOG_NO_UI_FLAG = 1
WT_TRUSTDBDIALOG_ONLY_PUB_TAB_FLAG = 2
WT_TRUSTDBDIALOG_WRITE_LEGACY_REG_FLAG = 256
WT_TRUSTDBDIALOG_WRITE_IEAK_STORE_FLAG = 512
WINTRUST_GET_DEFAULT_FOR_USAGE_ACTION = UInt32
DWACTION_ALLOCANDFILL = 1
DWACTION_FREE = 2
WINTRUST_POLICY_FLAGS = UInt32
WTPF_TRUSTTEST = 32
WTPF_TESTCANBEVALID = 128
WTPF_IGNOREEXPIRATION = 256
WTPF_IGNOREREVOKATION = 512
WTPF_OFFLINEOK_IND = 1024
WTPF_OFFLINEOK_COM = 2048
WTPF_OFFLINEOKNBU_IND = 4096
WTPF_OFFLINEOKNBU_COM = 8192
WTPF_VERIFY_V1_OFF = 65536
WTPF_IGNOREREVOCATIONONTS = 131072
WTPF_ALLOWONLYPERTRUST = 262144
WINTRUST_DATA_UICHOICE = UInt32
WTD_UI_ALL = 1
WTD_UI_NONE = 2
WTD_UI_NOBAD = 3
WTD_UI_NOGOOD = 4
WINTRUST_SIGNATURE_SETTINGS_FLAGS = UInt32
WSS_VERIFY_SPECIFIC = 1
WSS_GET_SECONDARY_SIG_COUNT = 2
WINTRUST_DATA_STATE_ACTION = UInt32
WTD_STATEACTION_IGNORE = 0
WTD_STATEACTION_VERIFY = 1
WTD_STATEACTION_CLOSE = 2
WTD_STATEACTION_AUTO_CACHE = 3
WTD_STATEACTION_AUTO_CACHE_FLUSH = 4
WINTRUST_DATA_UNION_CHOICE = UInt32
WTD_CHOICE_FILE = 1
WTD_CHOICE_CATALOG = 2
WTD_CHOICE_BLOB = 3
WTD_CHOICE_SIGNER = 4
WTD_CHOICE_CERT = 5
WINTRUST_DATA_REVOCATION_CHECKS = UInt32
WTD_REVOKE_NONE = 0
WTD_REVOKE_WHOLECHAIN = 1
WINTRUST_DATA_UICONTEXT = UInt32
WTD_UICONTEXT_EXECUTE = 0
WTD_UICONTEXT_INSTALL = 1
def _define_WINTRUST_DATA_head():
    class WINTRUST_DATA(Structure):
        pass
    return WINTRUST_DATA
def _define_WINTRUST_DATA():
    WINTRUST_DATA = win32more.Security.WinTrust.WINTRUST_DATA_head
    class WINTRUST_DATA__Anonymous_e__Union(Union):
        pass
    WINTRUST_DATA__Anonymous_e__Union._fields_ = [
        ("pFile", POINTER(win32more.Security.WinTrust.WINTRUST_FILE_INFO_head)),
        ("pCatalog", POINTER(win32more.Security.WinTrust.WINTRUST_CATALOG_INFO_head)),
        ("pBlob", POINTER(win32more.Security.WinTrust.WINTRUST_BLOB_INFO_head)),
        ("pSgnr", POINTER(win32more.Security.WinTrust.WINTRUST_SGNR_INFO_head)),
        ("pCert", POINTER(win32more.Security.WinTrust.WINTRUST_CERT_INFO_head)),
    ]
    WINTRUST_DATA._anonymous_ = [
        'Anonymous',
    ]
    WINTRUST_DATA._fields_ = [
        ("cbStruct", UInt32),
        ("pPolicyCallbackData", c_void_p),
        ("pSIPClientData", c_void_p),
        ("dwUIChoice", win32more.Security.WinTrust.WINTRUST_DATA_UICHOICE),
        ("fdwRevocationChecks", win32more.Security.WinTrust.WINTRUST_DATA_REVOCATION_CHECKS),
        ("dwUnionChoice", win32more.Security.WinTrust.WINTRUST_DATA_UNION_CHOICE),
        ("Anonymous", WINTRUST_DATA__Anonymous_e__Union),
        ("dwStateAction", win32more.Security.WinTrust.WINTRUST_DATA_STATE_ACTION),
        ("hWVTStateData", win32more.Foundation.HANDLE),
        ("pwszURLReference", win32more.Foundation.PWSTR),
        ("dwProvFlags", UInt32),
        ("dwUIContext", win32more.Security.WinTrust.WINTRUST_DATA_UICONTEXT),
        ("pSignatureSettings", POINTER(win32more.Security.WinTrust.WINTRUST_SIGNATURE_SETTINGS_head)),
    ]
    return WINTRUST_DATA
def _define_WINTRUST_SIGNATURE_SETTINGS_head():
    class WINTRUST_SIGNATURE_SETTINGS(Structure):
        pass
    return WINTRUST_SIGNATURE_SETTINGS
def _define_WINTRUST_SIGNATURE_SETTINGS():
    WINTRUST_SIGNATURE_SETTINGS = win32more.Security.WinTrust.WINTRUST_SIGNATURE_SETTINGS_head
    WINTRUST_SIGNATURE_SETTINGS._fields_ = [
        ("cbStruct", UInt32),
        ("dwIndex", UInt32),
        ("dwFlags", win32more.Security.WinTrust.WINTRUST_SIGNATURE_SETTINGS_FLAGS),
        ("cSecondarySigs", UInt32),
        ("dwVerifiedSigIndex", UInt32),
        ("pCryptoPolicy", POINTER(win32more.Security.Cryptography.CERT_STRONG_SIGN_PARA_head)),
    ]
    return WINTRUST_SIGNATURE_SETTINGS
def _define_WINTRUST_FILE_INFO_head():
    class WINTRUST_FILE_INFO(Structure):
        pass
    return WINTRUST_FILE_INFO
def _define_WINTRUST_FILE_INFO():
    WINTRUST_FILE_INFO = win32more.Security.WinTrust.WINTRUST_FILE_INFO_head
    WINTRUST_FILE_INFO._fields_ = [
        ("cbStruct", UInt32),
        ("pcwszFilePath", win32more.Foundation.PWSTR),
        ("hFile", win32more.Foundation.HANDLE),
        ("pgKnownSubject", POINTER(Guid)),
    ]
    return WINTRUST_FILE_INFO
def _define_WINTRUST_CATALOG_INFO_head():
    class WINTRUST_CATALOG_INFO(Structure):
        pass
    return WINTRUST_CATALOG_INFO
def _define_WINTRUST_CATALOG_INFO():
    WINTRUST_CATALOG_INFO = win32more.Security.WinTrust.WINTRUST_CATALOG_INFO_head
    WINTRUST_CATALOG_INFO._fields_ = [
        ("cbStruct", UInt32),
        ("dwCatalogVersion", UInt32),
        ("pcwszCatalogFilePath", win32more.Foundation.PWSTR),
        ("pcwszMemberTag", win32more.Foundation.PWSTR),
        ("pcwszMemberFilePath", win32more.Foundation.PWSTR),
        ("hMemberFile", win32more.Foundation.HANDLE),
        ("pbCalculatedFileHash", c_char_p_no),
        ("cbCalculatedFileHash", UInt32),
        ("pcCatalogContext", POINTER(win32more.Security.Cryptography.CTL_CONTEXT_head)),
        ("hCatAdmin", IntPtr),
    ]
    return WINTRUST_CATALOG_INFO
def _define_WINTRUST_BLOB_INFO_head():
    class WINTRUST_BLOB_INFO(Structure):
        pass
    return WINTRUST_BLOB_INFO
def _define_WINTRUST_BLOB_INFO():
    WINTRUST_BLOB_INFO = win32more.Security.WinTrust.WINTRUST_BLOB_INFO_head
    WINTRUST_BLOB_INFO._fields_ = [
        ("cbStruct", UInt32),
        ("gSubject", Guid),
        ("pcwszDisplayName", win32more.Foundation.PWSTR),
        ("cbMemObject", UInt32),
        ("pbMemObject", c_char_p_no),
        ("cbMemSignedMsg", UInt32),
        ("pbMemSignedMsg", c_char_p_no),
    ]
    return WINTRUST_BLOB_INFO
def _define_WINTRUST_SGNR_INFO_head():
    class WINTRUST_SGNR_INFO(Structure):
        pass
    return WINTRUST_SGNR_INFO
def _define_WINTRUST_SGNR_INFO():
    WINTRUST_SGNR_INFO = win32more.Security.WinTrust.WINTRUST_SGNR_INFO_head
    WINTRUST_SGNR_INFO._fields_ = [
        ("cbStruct", UInt32),
        ("pcwszDisplayName", win32more.Foundation.PWSTR),
        ("psSignerInfo", POINTER(win32more.Security.Cryptography.CMSG_SIGNER_INFO_head)),
        ("chStores", UInt32),
        ("pahStores", POINTER(c_void_p)),
    ]
    return WINTRUST_SGNR_INFO
def _define_WINTRUST_CERT_INFO_head():
    class WINTRUST_CERT_INFO(Structure):
        pass
    return WINTRUST_CERT_INFO
def _define_WINTRUST_CERT_INFO():
    WINTRUST_CERT_INFO = win32more.Security.WinTrust.WINTRUST_CERT_INFO_head
    WINTRUST_CERT_INFO._fields_ = [
        ("cbStruct", UInt32),
        ("pcwszDisplayName", win32more.Foundation.PWSTR),
        ("psCertContext", POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head)),
        ("chStores", UInt32),
        ("pahStores", POINTER(c_void_p)),
        ("dwFlags", UInt32),
        ("psftVerifyAsOf", POINTER(win32more.Foundation.FILETIME_head)),
    ]
    return WINTRUST_CERT_INFO
def _define_PFN_CPD_MEM_ALLOC():
    return CFUNCTYPE(c_void_p,UInt32, use_last_error=False)
def _define_PFN_CPD_MEM_FREE():
    return CFUNCTYPE(Void,c_void_p, use_last_error=False)
def _define_PFN_CPD_ADD_STORE():
    return CFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_DATA_head),c_void_p, use_last_error=False)
def _define_PFN_CPD_ADD_SGNR():
    return CFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_DATA_head),win32more.Foundation.BOOL,UInt32,POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_SGNR_head), use_last_error=False)
def _define_PFN_CPD_ADD_CERT():
    return CFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_DATA_head),UInt32,win32more.Foundation.BOOL,UInt32,POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head), use_last_error=False)
def _define_PFN_CPD_ADD_PRIVDATA():
    return CFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_DATA_head),POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_PRIVDATA_head), use_last_error=False)
def _define_PFN_PROVIDER_INIT_CALL():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_DATA_head), use_last_error=False)
def _define_PFN_PROVIDER_OBJTRUST_CALL():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_DATA_head), use_last_error=False)
def _define_PFN_PROVIDER_SIGTRUST_CALL():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_DATA_head), use_last_error=False)
def _define_PFN_PROVIDER_CERTTRUST_CALL():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_DATA_head), use_last_error=False)
def _define_PFN_PROVIDER_FINALPOLICY_CALL():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_DATA_head), use_last_error=False)
def _define_PFN_PROVIDER_TESTFINALPOLICY_CALL():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_DATA_head), use_last_error=False)
def _define_PFN_PROVIDER_CLEANUP_CALL():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_DATA_head), use_last_error=False)
def _define_PFN_PROVIDER_CERTCHKPOLICY_CALL():
    return CFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_DATA_head),UInt32,win32more.Foundation.BOOL,UInt32, use_last_error=False)
def _define_CRYPT_PROVIDER_DATA_head():
    class CRYPT_PROVIDER_DATA(Structure):
        pass
    return CRYPT_PROVIDER_DATA
def _define_CRYPT_PROVIDER_DATA():
    CRYPT_PROVIDER_DATA = win32more.Security.WinTrust.CRYPT_PROVIDER_DATA_head
    class CRYPT_PROVIDER_DATA__Anonymous_e__Union(Union):
        pass
    CRYPT_PROVIDER_DATA__Anonymous_e__Union._fields_ = [
        ("pPDSip", POINTER(win32more.Security.WinTrust.PROVDATA_SIP_head)),
    ]
    CRYPT_PROVIDER_DATA._anonymous_ = [
        'Anonymous',
    ]
    CRYPT_PROVIDER_DATA._fields_ = [
        ("cbStruct", UInt32),
        ("pWintrustData", POINTER(win32more.Security.WinTrust.WINTRUST_DATA_head)),
        ("fOpenedFile", win32more.Foundation.BOOL),
        ("hWndParent", win32more.Foundation.HWND),
        ("pgActionID", POINTER(Guid)),
        ("hProv", UIntPtr),
        ("dwError", UInt32),
        ("dwRegSecuritySettings", UInt32),
        ("dwRegPolicySettings", UInt32),
        ("psPfns", POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_FUNCTIONS_head)),
        ("cdwTrustStepErrors", UInt32),
        ("padwTrustStepErrors", POINTER(UInt32)),
        ("chStores", UInt32),
        ("pahStores", POINTER(c_void_p)),
        ("dwEncoding", UInt32),
        ("hMsg", c_void_p),
        ("csSigners", UInt32),
        ("pasSigners", POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_SGNR_head)),
        ("csProvPrivData", UInt32),
        ("pasProvPrivData", POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_PRIVDATA_head)),
        ("dwSubjectChoice", UInt32),
        ("Anonymous", CRYPT_PROVIDER_DATA__Anonymous_e__Union),
        ("pszUsageOID", win32more.Foundation.PSTR),
        ("fRecallWithState", win32more.Foundation.BOOL),
        ("sftSystemTime", win32more.Foundation.FILETIME),
        ("pszCTLSignerUsageOID", win32more.Foundation.PSTR),
        ("dwProvFlags", UInt32),
        ("dwFinalError", UInt32),
        ("pRequestUsage", POINTER(win32more.Security.Cryptography.CERT_USAGE_MATCH_head)),
        ("dwTrustPubSettings", UInt32),
        ("dwUIStateFlags", UInt32),
        ("pSigState", POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_SIGSTATE_head)),
        ("pSigSettings", POINTER(win32more.Security.WinTrust.WINTRUST_SIGNATURE_SETTINGS_head)),
    ]
    return CRYPT_PROVIDER_DATA
def _define_CRYPT_PROVIDER_SIGSTATE_head():
    class CRYPT_PROVIDER_SIGSTATE(Structure):
        pass
    return CRYPT_PROVIDER_SIGSTATE
def _define_CRYPT_PROVIDER_SIGSTATE():
    CRYPT_PROVIDER_SIGSTATE = win32more.Security.WinTrust.CRYPT_PROVIDER_SIGSTATE_head
    CRYPT_PROVIDER_SIGSTATE._fields_ = [
        ("cbStruct", UInt32),
        ("rhSecondarySigs", POINTER(c_void_p)),
        ("hPrimarySig", c_void_p),
        ("fFirstAttemptMade", win32more.Foundation.BOOL),
        ("fNoMoreSigs", win32more.Foundation.BOOL),
        ("cSecondarySigs", UInt32),
        ("dwCurrentIndex", UInt32),
        ("fSupportMultiSig", win32more.Foundation.BOOL),
        ("dwCryptoPolicySupport", UInt32),
        ("iAttemptCount", UInt32),
        ("fCheckedSealing", win32more.Foundation.BOOL),
        ("pSealingSignature", POINTER(win32more.Security.WinTrust.SEALING_SIGNATURE_ATTRIBUTE_head)),
    ]
    return CRYPT_PROVIDER_SIGSTATE
def _define_CRYPT_PROVIDER_FUNCTIONS_head():
    class CRYPT_PROVIDER_FUNCTIONS(Structure):
        pass
    return CRYPT_PROVIDER_FUNCTIONS
def _define_CRYPT_PROVIDER_FUNCTIONS():
    CRYPT_PROVIDER_FUNCTIONS = win32more.Security.WinTrust.CRYPT_PROVIDER_FUNCTIONS_head
    CRYPT_PROVIDER_FUNCTIONS._fields_ = [
        ("cbStruct", UInt32),
        ("pfnAlloc", win32more.Security.WinTrust.PFN_CPD_MEM_ALLOC),
        ("pfnFree", win32more.Security.WinTrust.PFN_CPD_MEM_FREE),
        ("pfnAddStore2Chain", win32more.Security.WinTrust.PFN_CPD_ADD_STORE),
        ("pfnAddSgnr2Chain", win32more.Security.WinTrust.PFN_CPD_ADD_SGNR),
        ("pfnAddCert2Chain", win32more.Security.WinTrust.PFN_CPD_ADD_CERT),
        ("pfnAddPrivData2Chain", win32more.Security.WinTrust.PFN_CPD_ADD_PRIVDATA),
        ("pfnInitialize", win32more.Security.WinTrust.PFN_PROVIDER_INIT_CALL),
        ("pfnObjectTrust", win32more.Security.WinTrust.PFN_PROVIDER_OBJTRUST_CALL),
        ("pfnSignatureTrust", win32more.Security.WinTrust.PFN_PROVIDER_SIGTRUST_CALL),
        ("pfnCertificateTrust", win32more.Security.WinTrust.PFN_PROVIDER_CERTTRUST_CALL),
        ("pfnFinalPolicy", win32more.Security.WinTrust.PFN_PROVIDER_FINALPOLICY_CALL),
        ("pfnCertCheckPolicy", win32more.Security.WinTrust.PFN_PROVIDER_CERTCHKPOLICY_CALL),
        ("pfnTestFinalPolicy", win32more.Security.WinTrust.PFN_PROVIDER_TESTFINALPOLICY_CALL),
        ("psUIpfns", POINTER(win32more.Security.WinTrust.CRYPT_PROVUI_FUNCS_head)),
        ("pfnCleanupPolicy", win32more.Security.WinTrust.PFN_PROVIDER_CLEANUP_CALL),
    ]
    return CRYPT_PROVIDER_FUNCTIONS
def _define_PFN_PROVUI_CALL():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_DATA_head), use_last_error=False)
def _define_CRYPT_PROVUI_FUNCS_head():
    class CRYPT_PROVUI_FUNCS(Structure):
        pass
    return CRYPT_PROVUI_FUNCS
def _define_CRYPT_PROVUI_FUNCS():
    CRYPT_PROVUI_FUNCS = win32more.Security.WinTrust.CRYPT_PROVUI_FUNCS_head
    CRYPT_PROVUI_FUNCS._fields_ = [
        ("cbStruct", UInt32),
        ("psUIData", POINTER(win32more.Security.WinTrust.CRYPT_PROVUI_DATA_head)),
        ("pfnOnMoreInfoClick", win32more.Security.WinTrust.PFN_PROVUI_CALL),
        ("pfnOnMoreInfoClickDefault", win32more.Security.WinTrust.PFN_PROVUI_CALL),
        ("pfnOnAdvancedClick", win32more.Security.WinTrust.PFN_PROVUI_CALL),
        ("pfnOnAdvancedClickDefault", win32more.Security.WinTrust.PFN_PROVUI_CALL),
    ]
    return CRYPT_PROVUI_FUNCS
def _define_CRYPT_PROVUI_DATA_head():
    class CRYPT_PROVUI_DATA(Structure):
        pass
    return CRYPT_PROVUI_DATA
def _define_CRYPT_PROVUI_DATA():
    CRYPT_PROVUI_DATA = win32more.Security.WinTrust.CRYPT_PROVUI_DATA_head
    CRYPT_PROVUI_DATA._fields_ = [
        ("cbStruct", UInt32),
        ("dwFinalError", UInt32),
        ("pYesButtonText", win32more.Foundation.PWSTR),
        ("pNoButtonText", win32more.Foundation.PWSTR),
        ("pMoreInfoButtonText", win32more.Foundation.PWSTR),
        ("pAdvancedLinkText", win32more.Foundation.PWSTR),
        ("pCopyActionText", win32more.Foundation.PWSTR),
        ("pCopyActionTextNoTS", win32more.Foundation.PWSTR),
        ("pCopyActionTextNotSigned", win32more.Foundation.PWSTR),
    ]
    return CRYPT_PROVUI_DATA
def _define_CRYPT_PROVIDER_SGNR_head():
    class CRYPT_PROVIDER_SGNR(Structure):
        pass
    return CRYPT_PROVIDER_SGNR
def _define_CRYPT_PROVIDER_SGNR():
    CRYPT_PROVIDER_SGNR = win32more.Security.WinTrust.CRYPT_PROVIDER_SGNR_head
    CRYPT_PROVIDER_SGNR._fields_ = [
        ("cbStruct", UInt32),
        ("sftVerifyAsOf", win32more.Foundation.FILETIME),
        ("csCertChain", UInt32),
        ("pasCertChain", POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_CERT_head)),
        ("dwSignerType", UInt32),
        ("psSigner", POINTER(win32more.Security.Cryptography.CMSG_SIGNER_INFO_head)),
        ("dwError", UInt32),
        ("csCounterSigners", UInt32),
        ("pasCounterSigners", POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_SGNR_head)),
        ("pChainContext", POINTER(win32more.Security.Cryptography.CERT_CHAIN_CONTEXT_head)),
    ]
    return CRYPT_PROVIDER_SGNR
def _define_CRYPT_PROVIDER_CERT_head():
    class CRYPT_PROVIDER_CERT(Structure):
        pass
    return CRYPT_PROVIDER_CERT
def _define_CRYPT_PROVIDER_CERT():
    CRYPT_PROVIDER_CERT = win32more.Security.WinTrust.CRYPT_PROVIDER_CERT_head
    CRYPT_PROVIDER_CERT._fields_ = [
        ("cbStruct", UInt32),
        ("pCert", POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head)),
        ("fCommercial", win32more.Foundation.BOOL),
        ("fTrustedRoot", win32more.Foundation.BOOL),
        ("fSelfSigned", win32more.Foundation.BOOL),
        ("fTestCert", win32more.Foundation.BOOL),
        ("dwRevokedReason", UInt32),
        ("dwConfidence", UInt32),
        ("dwError", UInt32),
        ("pTrustListContext", POINTER(win32more.Security.Cryptography.CTL_CONTEXT_head)),
        ("fTrustListSignerCert", win32more.Foundation.BOOL),
        ("pCtlContext", POINTER(win32more.Security.Cryptography.CTL_CONTEXT_head)),
        ("dwCtlError", UInt32),
        ("fIsCyclic", win32more.Foundation.BOOL),
        ("pChainElement", POINTER(win32more.Security.Cryptography.CERT_CHAIN_ELEMENT_head)),
    ]
    return CRYPT_PROVIDER_CERT
def _define_CRYPT_PROVIDER_PRIVDATA_head():
    class CRYPT_PROVIDER_PRIVDATA(Structure):
        pass
    return CRYPT_PROVIDER_PRIVDATA
def _define_CRYPT_PROVIDER_PRIVDATA():
    CRYPT_PROVIDER_PRIVDATA = win32more.Security.WinTrust.CRYPT_PROVIDER_PRIVDATA_head
    CRYPT_PROVIDER_PRIVDATA._fields_ = [
        ("cbStruct", UInt32),
        ("gProviderID", Guid),
        ("cbProvData", UInt32),
        ("pvProvData", c_void_p),
    ]
    return CRYPT_PROVIDER_PRIVDATA
def _define_PROVDATA_SIP_head():
    class PROVDATA_SIP(Structure):
        pass
    return PROVDATA_SIP
def _define_PROVDATA_SIP():
    PROVDATA_SIP = win32more.Security.WinTrust.PROVDATA_SIP_head
    PROVDATA_SIP._fields_ = [
        ("cbStruct", UInt32),
        ("gSubject", Guid),
        ("pSip", POINTER(win32more.Security.Cryptography.Sip.SIP_DISPATCH_INFO_head)),
        ("pCATSip", POINTER(win32more.Security.Cryptography.Sip.SIP_DISPATCH_INFO_head)),
        ("psSipSubjectInfo", POINTER(win32more.Security.Cryptography.Sip.SIP_SUBJECTINFO_head)),
        ("psSipCATSubjectInfo", POINTER(win32more.Security.Cryptography.Sip.SIP_SUBJECTINFO_head)),
        ("psIndirectData", POINTER(win32more.Security.Cryptography.Sip.SIP_INDIRECT_DATA_head)),
    ]
    return PROVDATA_SIP
def _define_CRYPT_TRUST_REG_ENTRY_head():
    class CRYPT_TRUST_REG_ENTRY(Structure):
        pass
    return CRYPT_TRUST_REG_ENTRY
def _define_CRYPT_TRUST_REG_ENTRY():
    CRYPT_TRUST_REG_ENTRY = win32more.Security.WinTrust.CRYPT_TRUST_REG_ENTRY_head
    CRYPT_TRUST_REG_ENTRY._fields_ = [
        ("cbStruct", UInt32),
        ("pwszDLLName", win32more.Foundation.PWSTR),
        ("pwszFunctionName", win32more.Foundation.PWSTR),
    ]
    return CRYPT_TRUST_REG_ENTRY
def _define_CRYPT_REGISTER_ACTIONID_head():
    class CRYPT_REGISTER_ACTIONID(Structure):
        pass
    return CRYPT_REGISTER_ACTIONID
def _define_CRYPT_REGISTER_ACTIONID():
    CRYPT_REGISTER_ACTIONID = win32more.Security.WinTrust.CRYPT_REGISTER_ACTIONID_head
    CRYPT_REGISTER_ACTIONID._fields_ = [
        ("cbStruct", UInt32),
        ("sInitProvider", win32more.Security.WinTrust.CRYPT_TRUST_REG_ENTRY),
        ("sObjectProvider", win32more.Security.WinTrust.CRYPT_TRUST_REG_ENTRY),
        ("sSignatureProvider", win32more.Security.WinTrust.CRYPT_TRUST_REG_ENTRY),
        ("sCertificateProvider", win32more.Security.WinTrust.CRYPT_TRUST_REG_ENTRY),
        ("sCertificatePolicyProvider", win32more.Security.WinTrust.CRYPT_TRUST_REG_ENTRY),
        ("sFinalPolicyProvider", win32more.Security.WinTrust.CRYPT_TRUST_REG_ENTRY),
        ("sTestPolicyProvider", win32more.Security.WinTrust.CRYPT_TRUST_REG_ENTRY),
        ("sCleanupProvider", win32more.Security.WinTrust.CRYPT_TRUST_REG_ENTRY),
    ]
    return CRYPT_REGISTER_ACTIONID
def _define_PFN_ALLOCANDFILLDEFUSAGE():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_DEFUSAGE_head), use_last_error=False)
def _define_PFN_FREEDEFUSAGE():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_DEFUSAGE_head), use_last_error=False)
def _define_CRYPT_PROVIDER_REGDEFUSAGE_head():
    class CRYPT_PROVIDER_REGDEFUSAGE(Structure):
        pass
    return CRYPT_PROVIDER_REGDEFUSAGE
def _define_CRYPT_PROVIDER_REGDEFUSAGE():
    CRYPT_PROVIDER_REGDEFUSAGE = win32more.Security.WinTrust.CRYPT_PROVIDER_REGDEFUSAGE_head
    CRYPT_PROVIDER_REGDEFUSAGE._fields_ = [
        ("cbStruct", UInt32),
        ("pgActionID", POINTER(Guid)),
        ("pwszDllName", win32more.Foundation.PWSTR),
        ("pwszLoadCallbackDataFunctionName", win32more.Foundation.PSTR),
        ("pwszFreeCallbackDataFunctionName", win32more.Foundation.PSTR),
    ]
    return CRYPT_PROVIDER_REGDEFUSAGE
def _define_CRYPT_PROVIDER_DEFUSAGE_head():
    class CRYPT_PROVIDER_DEFUSAGE(Structure):
        pass
    return CRYPT_PROVIDER_DEFUSAGE
def _define_CRYPT_PROVIDER_DEFUSAGE():
    CRYPT_PROVIDER_DEFUSAGE = win32more.Security.WinTrust.CRYPT_PROVIDER_DEFUSAGE_head
    CRYPT_PROVIDER_DEFUSAGE._fields_ = [
        ("cbStruct", UInt32),
        ("gActionID", Guid),
        ("pDefPolicyCallbackData", c_void_p),
        ("pDefSIPClientData", c_void_p),
    ]
    return CRYPT_PROVIDER_DEFUSAGE
def _define_SPC_SERIALIZED_OBJECT_head():
    class SPC_SERIALIZED_OBJECT(Structure):
        pass
    return SPC_SERIALIZED_OBJECT
def _define_SPC_SERIALIZED_OBJECT():
    SPC_SERIALIZED_OBJECT = win32more.Security.WinTrust.SPC_SERIALIZED_OBJECT_head
    SPC_SERIALIZED_OBJECT._fields_ = [
        ("ClassId", Byte * 16),
        ("SerializedData", win32more.Security.Cryptography.CRYPTOAPI_BLOB),
    ]
    return SPC_SERIALIZED_OBJECT
def _define_SPC_SIGINFO_head():
    class SPC_SIGINFO(Structure):
        pass
    return SPC_SIGINFO
def _define_SPC_SIGINFO():
    SPC_SIGINFO = win32more.Security.WinTrust.SPC_SIGINFO_head
    SPC_SIGINFO._fields_ = [
        ("dwSipVersion", UInt32),
        ("gSIPGuid", Guid),
        ("dwReserved1", UInt32),
        ("dwReserved2", UInt32),
        ("dwReserved3", UInt32),
        ("dwReserved4", UInt32),
        ("dwReserved5", UInt32),
    ]
    return SPC_SIGINFO
def _define_SPC_LINK_head():
    class SPC_LINK(Structure):
        pass
    return SPC_LINK
def _define_SPC_LINK():
    SPC_LINK = win32more.Security.WinTrust.SPC_LINK_head
    class SPC_LINK__Anonymous_e__Union(Union):
        pass
    SPC_LINK__Anonymous_e__Union._fields_ = [
        ("pwszUrl", win32more.Foundation.PWSTR),
        ("Moniker", win32more.Security.WinTrust.SPC_SERIALIZED_OBJECT),
        ("pwszFile", win32more.Foundation.PWSTR),
    ]
    SPC_LINK._anonymous_ = [
        'Anonymous',
    ]
    SPC_LINK._fields_ = [
        ("dwLinkChoice", UInt32),
        ("Anonymous", SPC_LINK__Anonymous_e__Union),
    ]
    return SPC_LINK
def _define_SPC_PE_IMAGE_DATA_head():
    class SPC_PE_IMAGE_DATA(Structure):
        pass
    return SPC_PE_IMAGE_DATA
def _define_SPC_PE_IMAGE_DATA():
    SPC_PE_IMAGE_DATA = win32more.Security.WinTrust.SPC_PE_IMAGE_DATA_head
    SPC_PE_IMAGE_DATA._fields_ = [
        ("Flags", win32more.Security.Cryptography.CRYPT_BIT_BLOB),
        ("pFile", POINTER(win32more.Security.WinTrust.SPC_LINK_head)),
    ]
    return SPC_PE_IMAGE_DATA
def _define_SPC_INDIRECT_DATA_CONTENT_head():
    class SPC_INDIRECT_DATA_CONTENT(Structure):
        pass
    return SPC_INDIRECT_DATA_CONTENT
def _define_SPC_INDIRECT_DATA_CONTENT():
    SPC_INDIRECT_DATA_CONTENT = win32more.Security.WinTrust.SPC_INDIRECT_DATA_CONTENT_head
    SPC_INDIRECT_DATA_CONTENT._fields_ = [
        ("Data", win32more.Security.Cryptography.CRYPT_ATTRIBUTE_TYPE_VALUE),
        ("DigestAlgorithm", win32more.Security.Cryptography.CRYPT_ALGORITHM_IDENTIFIER),
        ("Digest", win32more.Security.Cryptography.CRYPTOAPI_BLOB),
    ]
    return SPC_INDIRECT_DATA_CONTENT
def _define_SPC_FINANCIAL_CRITERIA_head():
    class SPC_FINANCIAL_CRITERIA(Structure):
        pass
    return SPC_FINANCIAL_CRITERIA
def _define_SPC_FINANCIAL_CRITERIA():
    SPC_FINANCIAL_CRITERIA = win32more.Security.WinTrust.SPC_FINANCIAL_CRITERIA_head
    SPC_FINANCIAL_CRITERIA._fields_ = [
        ("fFinancialInfoAvailable", win32more.Foundation.BOOL),
        ("fMeetsCriteria", win32more.Foundation.BOOL),
    ]
    return SPC_FINANCIAL_CRITERIA
def _define_SPC_IMAGE_head():
    class SPC_IMAGE(Structure):
        pass
    return SPC_IMAGE
def _define_SPC_IMAGE():
    SPC_IMAGE = win32more.Security.WinTrust.SPC_IMAGE_head
    SPC_IMAGE._fields_ = [
        ("pImageLink", POINTER(win32more.Security.WinTrust.SPC_LINK_head)),
        ("Bitmap", win32more.Security.Cryptography.CRYPTOAPI_BLOB),
        ("Metafile", win32more.Security.Cryptography.CRYPTOAPI_BLOB),
        ("EnhancedMetafile", win32more.Security.Cryptography.CRYPTOAPI_BLOB),
        ("GifFile", win32more.Security.Cryptography.CRYPTOAPI_BLOB),
    ]
    return SPC_IMAGE
def _define_SPC_SP_AGENCY_INFO_head():
    class SPC_SP_AGENCY_INFO(Structure):
        pass
    return SPC_SP_AGENCY_INFO
def _define_SPC_SP_AGENCY_INFO():
    SPC_SP_AGENCY_INFO = win32more.Security.WinTrust.SPC_SP_AGENCY_INFO_head
    SPC_SP_AGENCY_INFO._fields_ = [
        ("pPolicyInformation", POINTER(win32more.Security.WinTrust.SPC_LINK_head)),
        ("pwszPolicyDisplayText", win32more.Foundation.PWSTR),
        ("pLogoImage", POINTER(win32more.Security.WinTrust.SPC_IMAGE_head)),
        ("pLogoLink", POINTER(win32more.Security.WinTrust.SPC_LINK_head)),
    ]
    return SPC_SP_AGENCY_INFO
def _define_SPC_STATEMENT_TYPE_head():
    class SPC_STATEMENT_TYPE(Structure):
        pass
    return SPC_STATEMENT_TYPE
def _define_SPC_STATEMENT_TYPE():
    SPC_STATEMENT_TYPE = win32more.Security.WinTrust.SPC_STATEMENT_TYPE_head
    SPC_STATEMENT_TYPE._fields_ = [
        ("cKeyPurposeId", UInt32),
        ("rgpszKeyPurposeId", POINTER(win32more.Foundation.PSTR)),
    ]
    return SPC_STATEMENT_TYPE
def _define_SPC_SP_OPUS_INFO_head():
    class SPC_SP_OPUS_INFO(Structure):
        pass
    return SPC_SP_OPUS_INFO
def _define_SPC_SP_OPUS_INFO():
    SPC_SP_OPUS_INFO = win32more.Security.WinTrust.SPC_SP_OPUS_INFO_head
    SPC_SP_OPUS_INFO._fields_ = [
        ("pwszProgramName", win32more.Foundation.PWSTR),
        ("pMoreInfo", POINTER(win32more.Security.WinTrust.SPC_LINK_head)),
        ("pPublisherInfo", POINTER(win32more.Security.WinTrust.SPC_LINK_head)),
    ]
    return SPC_SP_OPUS_INFO
def _define_CAT_NAMEVALUE_head():
    class CAT_NAMEVALUE(Structure):
        pass
    return CAT_NAMEVALUE
def _define_CAT_NAMEVALUE():
    CAT_NAMEVALUE = win32more.Security.WinTrust.CAT_NAMEVALUE_head
    CAT_NAMEVALUE._fields_ = [
        ("pwszTag", win32more.Foundation.PWSTR),
        ("fdwFlags", UInt32),
        ("Value", win32more.Security.Cryptography.CRYPTOAPI_BLOB),
    ]
    return CAT_NAMEVALUE
def _define_CAT_MEMBERINFO_head():
    class CAT_MEMBERINFO(Structure):
        pass
    return CAT_MEMBERINFO
def _define_CAT_MEMBERINFO():
    CAT_MEMBERINFO = win32more.Security.WinTrust.CAT_MEMBERINFO_head
    CAT_MEMBERINFO._fields_ = [
        ("pwszSubjGuid", win32more.Foundation.PWSTR),
        ("dwCertVersion", UInt32),
    ]
    return CAT_MEMBERINFO
def _define_CAT_MEMBERINFO2_head():
    class CAT_MEMBERINFO2(Structure):
        pass
    return CAT_MEMBERINFO2
def _define_CAT_MEMBERINFO2():
    CAT_MEMBERINFO2 = win32more.Security.WinTrust.CAT_MEMBERINFO2_head
    CAT_MEMBERINFO2._fields_ = [
        ("SubjectGuid", Guid),
        ("dwCertVersion", UInt32),
    ]
    return CAT_MEMBERINFO2
def _define_INTENT_TO_SEAL_ATTRIBUTE_head():
    class INTENT_TO_SEAL_ATTRIBUTE(Structure):
        pass
    return INTENT_TO_SEAL_ATTRIBUTE
def _define_INTENT_TO_SEAL_ATTRIBUTE():
    INTENT_TO_SEAL_ATTRIBUTE = win32more.Security.WinTrust.INTENT_TO_SEAL_ATTRIBUTE_head
    INTENT_TO_SEAL_ATTRIBUTE._fields_ = [
        ("version", UInt32),
        ("seal", win32more.Foundation.BOOLEAN),
    ]
    return INTENT_TO_SEAL_ATTRIBUTE
def _define_SEALING_SIGNATURE_ATTRIBUTE_head():
    class SEALING_SIGNATURE_ATTRIBUTE(Structure):
        pass
    return SEALING_SIGNATURE_ATTRIBUTE
def _define_SEALING_SIGNATURE_ATTRIBUTE():
    SEALING_SIGNATURE_ATTRIBUTE = win32more.Security.WinTrust.SEALING_SIGNATURE_ATTRIBUTE_head
    SEALING_SIGNATURE_ATTRIBUTE._fields_ = [
        ("version", UInt32),
        ("signerIndex", UInt32),
        ("signatureAlgorithm", win32more.Security.Cryptography.CRYPT_ALGORITHM_IDENTIFIER),
        ("encryptedDigest", win32more.Security.Cryptography.CRYPTOAPI_BLOB),
    ]
    return SEALING_SIGNATURE_ATTRIBUTE
def _define_SEALING_TIMESTAMP_ATTRIBUTE_head():
    class SEALING_TIMESTAMP_ATTRIBUTE(Structure):
        pass
    return SEALING_TIMESTAMP_ATTRIBUTE
def _define_SEALING_TIMESTAMP_ATTRIBUTE():
    SEALING_TIMESTAMP_ATTRIBUTE = win32more.Security.WinTrust.SEALING_TIMESTAMP_ATTRIBUTE_head
    SEALING_TIMESTAMP_ATTRIBUTE._fields_ = [
        ("version", UInt32),
        ("signerIndex", UInt32),
        ("sealTimeStampToken", win32more.Security.Cryptography.CRYPTOAPI_BLOB),
    ]
    return SEALING_TIMESTAMP_ATTRIBUTE
def _define_WIN_CERTIFICATE_head():
    class WIN_CERTIFICATE(Structure):
        pass
    return WIN_CERTIFICATE
def _define_WIN_CERTIFICATE():
    WIN_CERTIFICATE = win32more.Security.WinTrust.WIN_CERTIFICATE_head
    WIN_CERTIFICATE._fields_ = [
        ("dwLength", UInt32),
        ("wRevision", UInt16),
        ("wCertificateType", UInt16),
        ("bCertificate", Byte * 0),
    ]
    return WIN_CERTIFICATE
def _define_WIN_TRUST_ACTDATA_CONTEXT_WITH_SUBJECT_head():
    class WIN_TRUST_ACTDATA_CONTEXT_WITH_SUBJECT(Structure):
        pass
    return WIN_TRUST_ACTDATA_CONTEXT_WITH_SUBJECT
def _define_WIN_TRUST_ACTDATA_CONTEXT_WITH_SUBJECT():
    WIN_TRUST_ACTDATA_CONTEXT_WITH_SUBJECT = win32more.Security.WinTrust.WIN_TRUST_ACTDATA_CONTEXT_WITH_SUBJECT_head
    WIN_TRUST_ACTDATA_CONTEXT_WITH_SUBJECT._fields_ = [
        ("hClientToken", win32more.Foundation.HANDLE),
        ("SubjectType", POINTER(Guid)),
        ("Subject", c_void_p),
    ]
    return WIN_TRUST_ACTDATA_CONTEXT_WITH_SUBJECT
def _define_WIN_TRUST_ACTDATA_SUBJECT_ONLY_head():
    class WIN_TRUST_ACTDATA_SUBJECT_ONLY(Structure):
        pass
    return WIN_TRUST_ACTDATA_SUBJECT_ONLY
def _define_WIN_TRUST_ACTDATA_SUBJECT_ONLY():
    WIN_TRUST_ACTDATA_SUBJECT_ONLY = win32more.Security.WinTrust.WIN_TRUST_ACTDATA_SUBJECT_ONLY_head
    WIN_TRUST_ACTDATA_SUBJECT_ONLY._fields_ = [
        ("SubjectType", POINTER(Guid)),
        ("Subject", c_void_p),
    ]
    return WIN_TRUST_ACTDATA_SUBJECT_ONLY
def _define_WIN_TRUST_SUBJECT_FILE_head():
    class WIN_TRUST_SUBJECT_FILE(Structure):
        pass
    return WIN_TRUST_SUBJECT_FILE
def _define_WIN_TRUST_SUBJECT_FILE():
    WIN_TRUST_SUBJECT_FILE = win32more.Security.WinTrust.WIN_TRUST_SUBJECT_FILE_head
    WIN_TRUST_SUBJECT_FILE._fields_ = [
        ("hFile", win32more.Foundation.HANDLE),
        ("lpPath", win32more.Foundation.PWSTR),
    ]
    return WIN_TRUST_SUBJECT_FILE
def _define_WIN_TRUST_SUBJECT_FILE_AND_DISPLAY_head():
    class WIN_TRUST_SUBJECT_FILE_AND_DISPLAY(Structure):
        pass
    return WIN_TRUST_SUBJECT_FILE_AND_DISPLAY
def _define_WIN_TRUST_SUBJECT_FILE_AND_DISPLAY():
    WIN_TRUST_SUBJECT_FILE_AND_DISPLAY = win32more.Security.WinTrust.WIN_TRUST_SUBJECT_FILE_AND_DISPLAY_head
    WIN_TRUST_SUBJECT_FILE_AND_DISPLAY._fields_ = [
        ("hFile", win32more.Foundation.HANDLE),
        ("lpPath", win32more.Foundation.PWSTR),
        ("lpDisplayName", win32more.Foundation.PWSTR),
    ]
    return WIN_TRUST_SUBJECT_FILE_AND_DISPLAY
def _define_WIN_SPUB_TRUSTED_PUBLISHER_DATA_head():
    class WIN_SPUB_TRUSTED_PUBLISHER_DATA(Structure):
        pass
    return WIN_SPUB_TRUSTED_PUBLISHER_DATA
def _define_WIN_SPUB_TRUSTED_PUBLISHER_DATA():
    WIN_SPUB_TRUSTED_PUBLISHER_DATA = win32more.Security.WinTrust.WIN_SPUB_TRUSTED_PUBLISHER_DATA_head
    WIN_SPUB_TRUSTED_PUBLISHER_DATA._fields_ = [
        ("hClientToken", win32more.Foundation.HANDLE),
        ("lpCertificate", POINTER(win32more.Security.WinTrust.WIN_CERTIFICATE_head)),
    ]
    return WIN_SPUB_TRUSTED_PUBLISHER_DATA
def _define_WTD_GENERIC_CHAIN_POLICY_SIGNER_INFO_head():
    class WTD_GENERIC_CHAIN_POLICY_SIGNER_INFO(Structure):
        pass
    return WTD_GENERIC_CHAIN_POLICY_SIGNER_INFO
def _define_WTD_GENERIC_CHAIN_POLICY_SIGNER_INFO():
    WTD_GENERIC_CHAIN_POLICY_SIGNER_INFO = win32more.Security.WinTrust.WTD_GENERIC_CHAIN_POLICY_SIGNER_INFO_head
    class WTD_GENERIC_CHAIN_POLICY_SIGNER_INFO__Anonymous_e__Union(Union):
        pass
    WTD_GENERIC_CHAIN_POLICY_SIGNER_INFO__Anonymous_e__Union._fields_ = [
        ("cbStruct", UInt32),
        ("cbSize", UInt32),
    ]
    WTD_GENERIC_CHAIN_POLICY_SIGNER_INFO._anonymous_ = [
        'Anonymous',
    ]
    WTD_GENERIC_CHAIN_POLICY_SIGNER_INFO._fields_ = [
        ("Anonymous", WTD_GENERIC_CHAIN_POLICY_SIGNER_INFO__Anonymous_e__Union),
        ("pChainContext", POINTER(win32more.Security.Cryptography.CERT_CHAIN_CONTEXT_head)),
        ("dwSignerType", UInt32),
        ("pMsgSignerInfo", POINTER(win32more.Security.Cryptography.CMSG_SIGNER_INFO_head)),
        ("dwError", UInt32),
        ("cCounterSigner", UInt32),
        ("rgpCounterSigner", POINTER(POINTER(win32more.Security.WinTrust.WTD_GENERIC_CHAIN_POLICY_SIGNER_INFO_head))),
    ]
    return WTD_GENERIC_CHAIN_POLICY_SIGNER_INFO
def _define_PFN_WTD_GENERIC_CHAIN_POLICY_CALLBACK():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_DATA_head),UInt32,UInt32,UInt32,POINTER(POINTER(win32more.Security.WinTrust.WTD_GENERIC_CHAIN_POLICY_SIGNER_INFO_head)),c_void_p, use_last_error=False)
def _define_WTD_GENERIC_CHAIN_POLICY_CREATE_INFO_head():
    class WTD_GENERIC_CHAIN_POLICY_CREATE_INFO(Structure):
        pass
    return WTD_GENERIC_CHAIN_POLICY_CREATE_INFO
def _define_WTD_GENERIC_CHAIN_POLICY_CREATE_INFO():
    WTD_GENERIC_CHAIN_POLICY_CREATE_INFO = win32more.Security.WinTrust.WTD_GENERIC_CHAIN_POLICY_CREATE_INFO_head
    class WTD_GENERIC_CHAIN_POLICY_CREATE_INFO__Anonymous_e__Union(Union):
        pass
    WTD_GENERIC_CHAIN_POLICY_CREATE_INFO__Anonymous_e__Union._fields_ = [
        ("cbStruct", UInt32),
        ("cbSize", UInt32),
    ]
    WTD_GENERIC_CHAIN_POLICY_CREATE_INFO._anonymous_ = [
        'Anonymous',
    ]
    WTD_GENERIC_CHAIN_POLICY_CREATE_INFO._fields_ = [
        ("Anonymous", WTD_GENERIC_CHAIN_POLICY_CREATE_INFO__Anonymous_e__Union),
        ("hChainEngine", win32more.Security.Cryptography.HCERTCHAINENGINE),
        ("pChainPara", POINTER(win32more.Security.Cryptography.CERT_CHAIN_PARA_head)),
        ("dwFlags", UInt32),
        ("pvReserved", c_void_p),
    ]
    return WTD_GENERIC_CHAIN_POLICY_CREATE_INFO
def _define_WTD_GENERIC_CHAIN_POLICY_DATA_head():
    class WTD_GENERIC_CHAIN_POLICY_DATA(Structure):
        pass
    return WTD_GENERIC_CHAIN_POLICY_DATA
def _define_WTD_GENERIC_CHAIN_POLICY_DATA():
    WTD_GENERIC_CHAIN_POLICY_DATA = win32more.Security.WinTrust.WTD_GENERIC_CHAIN_POLICY_DATA_head
    class WTD_GENERIC_CHAIN_POLICY_DATA__Anonymous_e__Union(Union):
        pass
    WTD_GENERIC_CHAIN_POLICY_DATA__Anonymous_e__Union._fields_ = [
        ("cbStruct", UInt32),
        ("cbSize", UInt32),
    ]
    WTD_GENERIC_CHAIN_POLICY_DATA._anonymous_ = [
        'Anonymous',
    ]
    WTD_GENERIC_CHAIN_POLICY_DATA._fields_ = [
        ("Anonymous", WTD_GENERIC_CHAIN_POLICY_DATA__Anonymous_e__Union),
        ("pSignerChainInfo", POINTER(win32more.Security.WinTrust.WTD_GENERIC_CHAIN_POLICY_CREATE_INFO_head)),
        ("pCounterSignerChainInfo", POINTER(win32more.Security.WinTrust.WTD_GENERIC_CHAIN_POLICY_CREATE_INFO_head)),
        ("pfnPolicyCallback", win32more.Security.WinTrust.PFN_WTD_GENERIC_CHAIN_POLICY_CALLBACK),
        ("pvPolicyArg", c_void_p),
    ]
    return WTD_GENERIC_CHAIN_POLICY_DATA
def _define_DRIVER_VER_MAJORMINOR_head():
    class DRIVER_VER_MAJORMINOR(Structure):
        pass
    return DRIVER_VER_MAJORMINOR
def _define_DRIVER_VER_MAJORMINOR():
    DRIVER_VER_MAJORMINOR = win32more.Security.WinTrust.DRIVER_VER_MAJORMINOR_head
    DRIVER_VER_MAJORMINOR._fields_ = [
        ("dwMajor", UInt32),
        ("dwMinor", UInt32),
    ]
    return DRIVER_VER_MAJORMINOR
def _define_DRIVER_VER_INFO_head():
    class DRIVER_VER_INFO(Structure):
        pass
    return DRIVER_VER_INFO
def _define_DRIVER_VER_INFO():
    DRIVER_VER_INFO = win32more.Security.WinTrust.DRIVER_VER_INFO_head
    DRIVER_VER_INFO._fields_ = [
        ("cbStruct", UInt32),
        ("dwReserved1", UIntPtr),
        ("dwReserved2", UIntPtr),
        ("dwPlatform", UInt32),
        ("dwVersion", UInt32),
        ("wszVersion", Char * 260),
        ("wszSignedBy", Char * 260),
        ("pcSignerCertContext", POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head)),
        ("sOSVersionLow", win32more.Security.WinTrust.DRIVER_VER_MAJORMINOR),
        ("sOSVersionHigh", win32more.Security.WinTrust.DRIVER_VER_MAJORMINOR),
        ("dwBuildNumberLow", UInt32),
        ("dwBuildNumberHigh", UInt32),
    ]
    return DRIVER_VER_INFO
def _define_CONFIG_CI_PROV_INFO_RESULT_head():
    class CONFIG_CI_PROV_INFO_RESULT(Structure):
        pass
    return CONFIG_CI_PROV_INFO_RESULT
def _define_CONFIG_CI_PROV_INFO_RESULT():
    CONFIG_CI_PROV_INFO_RESULT = win32more.Security.WinTrust.CONFIG_CI_PROV_INFO_RESULT_head
    CONFIG_CI_PROV_INFO_RESULT._fields_ = [
        ("hr", win32more.Foundation.HRESULT),
        ("dwResult", UInt32),
        ("dwPolicyIndex", UInt32),
        ("fIsExplicitDeny", win32more.Foundation.BOOLEAN),
    ]
    return CONFIG_CI_PROV_INFO_RESULT
def _define_CONFIG_CI_PROV_INFO_head():
    class CONFIG_CI_PROV_INFO(Structure):
        pass
    return CONFIG_CI_PROV_INFO
def _define_CONFIG_CI_PROV_INFO():
    CONFIG_CI_PROV_INFO = win32more.Security.WinTrust.CONFIG_CI_PROV_INFO_head
    CONFIG_CI_PROV_INFO._fields_ = [
        ("cbSize", UInt32),
        ("dwPolicies", UInt32),
        ("pPolicies", POINTER(win32more.Security.Cryptography.CRYPTOAPI_BLOB_head)),
        ("result", win32more.Security.WinTrust.CONFIG_CI_PROV_INFO_RESULT),
        ("dwScenario", UInt32),
    ]
    return CONFIG_CI_PROV_INFO
def _define_WinVerifyTrust():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HWND,POINTER(Guid),c_void_p, use_last_error=False)(("WinVerifyTrust", windll["WINTRUST"]), ((1, 'hwnd'),(1, 'pgActionID'),(1, 'pWVTData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinVerifyTrustEx():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HWND,POINTER(Guid),POINTER(win32more.Security.WinTrust.WINTRUST_DATA_head), use_last_error=False)(("WinVerifyTrustEx", windll["WINTRUST"]), ((1, 'hwnd'),(1, 'pgActionID'),(1, 'pWinTrustData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WintrustGetRegPolicyFlags():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Security.WinTrust.WINTRUST_POLICY_FLAGS), use_last_error=False)(("WintrustGetRegPolicyFlags", windll["WINTRUST"]), ((1, 'pdwPolicyFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WintrustSetRegPolicyFlags():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.WinTrust.WINTRUST_POLICY_FLAGS, use_last_error=False)(("WintrustSetRegPolicyFlags", windll["WINTRUST"]), ((1, 'dwPolicyFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WintrustAddActionID():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(Guid),UInt32,POINTER(win32more.Security.WinTrust.CRYPT_REGISTER_ACTIONID_head), use_last_error=True)(("WintrustAddActionID", windll["WINTRUST"]), ((1, 'pgActionID'),(1, 'fdwFlags'),(1, 'psProvInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WintrustRemoveActionID():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(Guid), use_last_error=False)(("WintrustRemoveActionID", windll["WINTRUST"]), ((1, 'pgActionID'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WintrustLoadFunctionPointers():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(Guid),POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_FUNCTIONS_head), use_last_error=False)(("WintrustLoadFunctionPointers", windll["WINTRUST"]), ((1, 'pgActionID'),(1, 'pPfns'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WintrustAddDefaultForUsage():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_REGDEFUSAGE_head), use_last_error=True)(("WintrustAddDefaultForUsage", windll["WINTRUST"]), ((1, 'pszUsageOID'),(1, 'psDefUsage'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WintrustGetDefaultForUsage():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.WinTrust.WINTRUST_GET_DEFAULT_FOR_USAGE_ACTION,win32more.Foundation.PSTR,POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_DEFUSAGE_head), use_last_error=True)(("WintrustGetDefaultForUsage", windll["WINTRUST"]), ((1, 'dwAction'),(1, 'pszUsageOID'),(1, 'psUsage'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTHelperGetProvSignerFromChain():
    try:
        return WINFUNCTYPE(POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_SGNR_head),POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_DATA_head),UInt32,win32more.Foundation.BOOL,UInt32, use_last_error=False)(("WTHelperGetProvSignerFromChain", windll["WINTRUST"]), ((1, 'pProvData'),(1, 'idxSigner'),(1, 'fCounterSigner'),(1, 'idxCounterSigner'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTHelperGetProvCertFromChain():
    try:
        return WINFUNCTYPE(POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_CERT_head),POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_SGNR_head),UInt32, use_last_error=False)(("WTHelperGetProvCertFromChain", windll["WINTRUST"]), ((1, 'pSgnr'),(1, 'idxCert'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTHelperProvDataFromStateData():
    try:
        return WINFUNCTYPE(POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_DATA_head),win32more.Foundation.HANDLE, use_last_error=False)(("WTHelperProvDataFromStateData", windll["WINTRUST"]), ((1, 'hStateData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTHelperGetProvPrivateDataFromChain():
    try:
        return WINFUNCTYPE(POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_PRIVDATA_head),POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_DATA_head),POINTER(Guid), use_last_error=False)(("WTHelperGetProvPrivateDataFromChain", windll["WINTRUST"]), ((1, 'pProvData'),(1, 'pgProviderID'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTHelperCertIsSelfSigned():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,POINTER(win32more.Security.Cryptography.CERT_INFO_head), use_last_error=False)(("WTHelperCertIsSelfSigned", windll["WINTRUST"]), ((1, 'dwEncoding'),(1, 'pCert'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTHelperCertCheckValidSignature():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_DATA_head), use_last_error=False)(("WTHelperCertCheckValidSignature", windll["WINTRUST"]), ((1, 'pProvData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenPersonalTrustDBDialogEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,UInt32,POINTER(c_void_p), use_last_error=False)(("OpenPersonalTrustDBDialogEx", windll["WINTRUST"]), ((1, 'hwndParent'),(1, 'dwFlags'),(1, 'pvReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenPersonalTrustDBDialog():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND, use_last_error=False)(("OpenPersonalTrustDBDialog", windll["WINTRUST"]), ((1, 'hwndParent'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WintrustSetDefaultIncludePEPageHashes():
    try:
        return WINFUNCTYPE(Void,win32more.Foundation.BOOL, use_last_error=False)(("WintrustSetDefaultIncludePEPageHashes", windll["WINTRUST"]), ((1, 'fIncludePEPageHashes'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "WINTRUST_MAX_HEADER_BYTES_TO_MAP_DEFAULT",
    "WINTRUST_MAX_HASH_BYTES_TO_MAP_DEFAULT",
    "WSS_VERIFY_SEALING",
    "WSS_INPUT_FLAG_MASK",
    "WSS_OUT_SEALING_STATUS_VERIFIED",
    "WSS_OUT_HAS_SEALING_INTENT",
    "WSS_OUT_FILE_SUPPORTS_SEAL",
    "WSS_OUTPUT_FLAG_MASK",
    "TRUSTERROR_STEP_WVTPARAMS",
    "TRUSTERROR_STEP_FILEIO",
    "TRUSTERROR_STEP_SIP",
    "TRUSTERROR_STEP_SIPSUBJINFO",
    "TRUSTERROR_STEP_CATALOGFILE",
    "TRUSTERROR_STEP_CERTSTORE",
    "TRUSTERROR_STEP_MESSAGE",
    "TRUSTERROR_STEP_MSG_SIGNERCOUNT",
    "TRUSTERROR_STEP_MSG_INNERCNTTYPE",
    "TRUSTERROR_STEP_MSG_INNERCNT",
    "TRUSTERROR_STEP_MSG_STORE",
    "TRUSTERROR_STEP_MSG_SIGNERINFO",
    "TRUSTERROR_STEP_MSG_SIGNERCERT",
    "TRUSTERROR_STEP_MSG_CERTCHAIN",
    "TRUSTERROR_STEP_MSG_COUNTERSIGINFO",
    "TRUSTERROR_STEP_MSG_COUNTERSIGCERT",
    "TRUSTERROR_STEP_VERIFY_MSGHASH",
    "TRUSTERROR_STEP_VERIFY_MSGINDIRECTDATA",
    "TRUSTERROR_STEP_FINAL_WVTINIT",
    "TRUSTERROR_STEP_FINAL_INITPROV",
    "TRUSTERROR_STEP_FINAL_OBJPROV",
    "TRUSTERROR_STEP_FINAL_SIGPROV",
    "TRUSTERROR_STEP_FINAL_CERTPROV",
    "TRUSTERROR_STEP_FINAL_CERTCHKPROV",
    "TRUSTERROR_STEP_FINAL_POLICYPROV",
    "TRUSTERROR_STEP_FINAL_UIPROV",
    "TRUSTERROR_MAX_STEPS",
    "WSS_OBJTRUST_SUPPORT",
    "WSS_SIGTRUST_SUPPORT",
    "WSS_CERTTRUST_SUPPORT",
    "WT_CURRENT_VERSION",
    "WT_ADD_ACTION_ID_RET_RESULT_FLAG",
    "SPC_UUID_LENGTH",
    "WIN_CERT_REVISION_1_0",
    "WIN_CERT_REVISION_2_0",
    "WIN_CERT_TYPE_X509",
    "WIN_CERT_TYPE_PKCS_SIGNED_DATA",
    "WIN_CERT_TYPE_RESERVED_1",
    "WIN_CERT_TYPE_TS_STACK_SIGNED",
    "WT_TRUSTDBDIALOG_NO_UI_FLAG",
    "WT_TRUSTDBDIALOG_ONLY_PUB_TAB_FLAG",
    "WT_TRUSTDBDIALOG_WRITE_LEGACY_REG_FLAG",
    "WT_TRUSTDBDIALOG_WRITE_IEAK_STORE_FLAG",
    "WINTRUST_GET_DEFAULT_FOR_USAGE_ACTION",
    "DWACTION_ALLOCANDFILL",
    "DWACTION_FREE",
    "WINTRUST_POLICY_FLAGS",
    "WTPF_TRUSTTEST",
    "WTPF_TESTCANBEVALID",
    "WTPF_IGNOREEXPIRATION",
    "WTPF_IGNOREREVOKATION",
    "WTPF_OFFLINEOK_IND",
    "WTPF_OFFLINEOK_COM",
    "WTPF_OFFLINEOKNBU_IND",
    "WTPF_OFFLINEOKNBU_COM",
    "WTPF_VERIFY_V1_OFF",
    "WTPF_IGNOREREVOCATIONONTS",
    "WTPF_ALLOWONLYPERTRUST",
    "WINTRUST_DATA_UICHOICE",
    "WTD_UI_ALL",
    "WTD_UI_NONE",
    "WTD_UI_NOBAD",
    "WTD_UI_NOGOOD",
    "WINTRUST_SIGNATURE_SETTINGS_FLAGS",
    "WSS_VERIFY_SPECIFIC",
    "WSS_GET_SECONDARY_SIG_COUNT",
    "WINTRUST_DATA_STATE_ACTION",
    "WTD_STATEACTION_IGNORE",
    "WTD_STATEACTION_VERIFY",
    "WTD_STATEACTION_CLOSE",
    "WTD_STATEACTION_AUTO_CACHE",
    "WTD_STATEACTION_AUTO_CACHE_FLUSH",
    "WINTRUST_DATA_UNION_CHOICE",
    "WTD_CHOICE_FILE",
    "WTD_CHOICE_CATALOG",
    "WTD_CHOICE_BLOB",
    "WTD_CHOICE_SIGNER",
    "WTD_CHOICE_CERT",
    "WINTRUST_DATA_REVOCATION_CHECKS",
    "WTD_REVOKE_NONE",
    "WTD_REVOKE_WHOLECHAIN",
    "WINTRUST_DATA_UICONTEXT",
    "WTD_UICONTEXT_EXECUTE",
    "WTD_UICONTEXT_INSTALL",
    "WINTRUST_DATA",
    "WINTRUST_SIGNATURE_SETTINGS",
    "WINTRUST_FILE_INFO",
    "WINTRUST_CATALOG_INFO",
    "WINTRUST_BLOB_INFO",
    "WINTRUST_SGNR_INFO",
    "WINTRUST_CERT_INFO",
    "PFN_CPD_MEM_ALLOC",
    "PFN_CPD_MEM_FREE",
    "PFN_CPD_ADD_STORE",
    "PFN_CPD_ADD_SGNR",
    "PFN_CPD_ADD_CERT",
    "PFN_CPD_ADD_PRIVDATA",
    "PFN_PROVIDER_INIT_CALL",
    "PFN_PROVIDER_OBJTRUST_CALL",
    "PFN_PROVIDER_SIGTRUST_CALL",
    "PFN_PROVIDER_CERTTRUST_CALL",
    "PFN_PROVIDER_FINALPOLICY_CALL",
    "PFN_PROVIDER_TESTFINALPOLICY_CALL",
    "PFN_PROVIDER_CLEANUP_CALL",
    "PFN_PROVIDER_CERTCHKPOLICY_CALL",
    "CRYPT_PROVIDER_DATA",
    "CRYPT_PROVIDER_SIGSTATE",
    "CRYPT_PROVIDER_FUNCTIONS",
    "PFN_PROVUI_CALL",
    "CRYPT_PROVUI_FUNCS",
    "CRYPT_PROVUI_DATA",
    "CRYPT_PROVIDER_SGNR",
    "CRYPT_PROVIDER_CERT",
    "CRYPT_PROVIDER_PRIVDATA",
    "PROVDATA_SIP",
    "CRYPT_TRUST_REG_ENTRY",
    "CRYPT_REGISTER_ACTIONID",
    "PFN_ALLOCANDFILLDEFUSAGE",
    "PFN_FREEDEFUSAGE",
    "CRYPT_PROVIDER_REGDEFUSAGE",
    "CRYPT_PROVIDER_DEFUSAGE",
    "SPC_SERIALIZED_OBJECT",
    "SPC_SIGINFO",
    "SPC_LINK",
    "SPC_PE_IMAGE_DATA",
    "SPC_INDIRECT_DATA_CONTENT",
    "SPC_FINANCIAL_CRITERIA",
    "SPC_IMAGE",
    "SPC_SP_AGENCY_INFO",
    "SPC_STATEMENT_TYPE",
    "SPC_SP_OPUS_INFO",
    "CAT_NAMEVALUE",
    "CAT_MEMBERINFO",
    "CAT_MEMBERINFO2",
    "INTENT_TO_SEAL_ATTRIBUTE",
    "SEALING_SIGNATURE_ATTRIBUTE",
    "SEALING_TIMESTAMP_ATTRIBUTE",
    "WIN_CERTIFICATE",
    "WIN_TRUST_ACTDATA_CONTEXT_WITH_SUBJECT",
    "WIN_TRUST_ACTDATA_SUBJECT_ONLY",
    "WIN_TRUST_SUBJECT_FILE",
    "WIN_TRUST_SUBJECT_FILE_AND_DISPLAY",
    "WIN_SPUB_TRUSTED_PUBLISHER_DATA",
    "WTD_GENERIC_CHAIN_POLICY_SIGNER_INFO",
    "PFN_WTD_GENERIC_CHAIN_POLICY_CALLBACK",
    "WTD_GENERIC_CHAIN_POLICY_CREATE_INFO",
    "WTD_GENERIC_CHAIN_POLICY_DATA",
    "DRIVER_VER_MAJORMINOR",
    "DRIVER_VER_INFO",
    "CONFIG_CI_PROV_INFO_RESULT",
    "CONFIG_CI_PROV_INFO",
    "WinVerifyTrust",
    "WinVerifyTrustEx",
    "WintrustGetRegPolicyFlags",
    "WintrustSetRegPolicyFlags",
    "WintrustAddActionID",
    "WintrustRemoveActionID",
    "WintrustLoadFunctionPointers",
    "WintrustAddDefaultForUsage",
    "WintrustGetDefaultForUsage",
    "WTHelperGetProvSignerFromChain",
    "WTHelperGetProvCertFromChain",
    "WTHelperProvDataFromStateData",
    "WTHelperGetProvPrivateDataFromChain",
    "WTHelperCertIsSelfSigned",
    "WTHelperCertCheckValidSignature",
    "OpenPersonalTrustDBDialogEx",
    "OpenPersonalTrustDBDialog",
    "WintrustSetDefaultIncludePEPageHashes",
]
