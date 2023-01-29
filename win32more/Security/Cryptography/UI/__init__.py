from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Security.Cryptography
import win32more.Security.Cryptography.UI
import win32more.Security.WinTrust
import win32more.UI.Controls
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
CRYTPDLG_FLAGS_MASK: UInt32 = 4278190080
CRYPTDLG_REVOCATION_DEFAULT: UInt32 = 0
CRYPTDLG_REVOCATION_ONLINE: UInt32 = 2147483648
CRYPTDLG_REVOCATION_CACHE: UInt32 = 1073741824
CRYPTDLG_REVOCATION_NONE: UInt32 = 536870912
CRYPTDLG_CACHE_ONLY_URL_RETRIEVAL: UInt32 = 268435456
CRYPTDLG_DISABLE_AIA: UInt32 = 134217728
CRYPTDLG_POLICY_MASK: UInt32 = 65535
POLICY_IGNORE_NON_CRITICAL_BC: UInt32 = 1
CRYPTDLG_ACTION_MASK: UInt32 = 4294901760
ACTION_REVOCATION_DEFAULT_ONLINE: UInt32 = 65536
ACTION_REVOCATION_DEFAULT_CACHE: UInt32 = 131072
CERT_DISPWELL_SELECT: UInt32 = 1
CERT_DISPWELL_TRUST_CA_CERT: UInt32 = 2
CERT_DISPWELL_TRUST_LEAF_CERT: UInt32 = 3
CERT_DISPWELL_TRUST_ADD_CA_CERT: UInt32 = 4
CERT_DISPWELL_TRUST_ADD_LEAF_CERT: UInt32 = 5
CERT_DISPWELL_DISTRUST_CA_CERT: UInt32 = 6
CERT_DISPWELL_DISTRUST_LEAF_CERT: UInt32 = 7
CERT_DISPWELL_DISTRUST_ADD_CA_CERT: UInt32 = 8
CERT_DISPWELL_DISTRUST_ADD_LEAF_CERT: UInt32 = 9
CSS_SELECTCERT_MASK: UInt32 = 16777215
SELCERT_PROPERTIES: UInt32 = 100
SELCERT_FINEPRINT: UInt32 = 101
SELCERT_CERTLIST: UInt32 = 102
SELCERT_ISSUED_TO: UInt32 = 103
SELCERT_VALIDITY: UInt32 = 104
SELCERT_ALGORITHM: UInt32 = 105
SELCERT_SERIAL_NUM: UInt32 = 106
SELCERT_THUMBPRINT: UInt32 = 107
CM_VIEWFLAGS_MASK: UInt32 = 16777215
CERTVIEW_CRYPTUI_LPARAM: UInt32 = 8388608
CERT_FILTER_OP_EXISTS: UInt32 = 1
CERT_FILTER_OP_NOT_EXISTS: UInt32 = 2
CERT_FILTER_OP_EQUALITY: UInt32 = 3
CERT_FILTER_INCLUDE_V1_CERTS: UInt32 = 1
CERT_FILTER_VALID_TIME_RANGE: UInt32 = 2
CERT_FILTER_VALID_SIGNATURE: UInt32 = 4
CERT_FILTER_LEAF_CERTS_ONLY: UInt32 = 8
CERT_FILTER_ISSUER_CERTS_ONLY: UInt32 = 16
CERT_FILTER_KEY_EXISTS: UInt32 = 32
szCERT_CERTIFICATE_ACTION_VERIFY: String = '{7801ebd0-cf4b-11d0-851f-0060979387ea}'
CERT_VALIDITY_BEFORE_START: UInt32 = 1
CERT_VALIDITY_AFTER_END: UInt32 = 2
CERT_VALIDITY_SIGNATURE_FAILS: UInt32 = 4
CERT_VALIDITY_CERTIFICATE_REVOKED: UInt32 = 8
CERT_VALIDITY_KEY_USAGE_EXT_FAILURE: UInt32 = 16
CERT_VALIDITY_EXTENDED_USAGE_FAILURE: UInt32 = 32
CERT_VALIDITY_NAME_CONSTRAINTS_FAILURE: UInt32 = 64
CERT_VALIDITY_UNKNOWN_CRITICAL_EXTENSION: UInt32 = 128
CERT_VALIDITY_ISSUER_INVALID: UInt32 = 256
CERT_VALIDITY_OTHER_EXTENSION_FAILURE: UInt32 = 512
CERT_VALIDITY_PERIOD_NESTING_FAILURE: UInt32 = 1024
CERT_VALIDITY_OTHER_ERROR: UInt32 = 2048
CERT_VALIDITY_ISSUER_DISTRUST: UInt32 = 33554432
CERT_VALIDITY_EXPLICITLY_DISTRUSTED: UInt32 = 16777216
CERT_VALIDITY_NO_ISSUER_CERT_FOUND: UInt32 = 268435456
CERT_VALIDITY_NO_CRL_FOUND: UInt32 = 536870912
CERT_VALIDITY_CRL_OUT_OF_DATE: UInt32 = 1073741824
CERT_VALIDITY_NO_TRUST_DATA: UInt32 = 2147483648
CERT_VALIDITY_MASK_TRUST: UInt32 = 4294901760
CERT_VALIDITY_MASK_VALIDITY: UInt32 = 65535
CERT_TRUST_MASK: UInt32 = 16777215
CERT_TRUST_DO_FULL_SEARCH: UInt32 = 1
CERT_TRUST_PERMIT_MISSING_CRLS: UInt32 = 2
CERT_TRUST_DO_FULL_TRUST: UInt32 = 5
CERT_CREDENTIAL_PROVIDER_ID: Int32 = -509
CRYPTUI_SELECT_ISSUEDTO_COLUMN: UInt64 = 1
CRYPTUI_SELECT_ISSUEDBY_COLUMN: UInt64 = 2
CRYPTUI_SELECT_INTENDEDUSE_COLUMN: UInt64 = 4
CRYPTUI_SELECT_FRIENDLYNAME_COLUMN: UInt64 = 8
CRYPTUI_SELECT_LOCATION_COLUMN: UInt64 = 16
CRYPTUI_SELECT_EXPIRATION_COLUMN: UInt64 = 32
CRYPTUI_CERT_MGR_TAB_MASK: UInt32 = 15
CRYPTUI_CERT_MGR_PUBLISHER_TAB: UInt32 = 4
CRYPTUI_CERT_MGR_SINGLE_TAB_FLAG: UInt32 = 32768
CRYPTUI_WIZ_DIGITAL_SIGN_EXCLUDE_PAGE_HASHES: UInt32 = 2
CRYPTUI_WIZ_DIGITAL_SIGN_INCLUDE_PAGE_HASHES: UInt32 = 4
CRYPTUI_WIZ_EXPORT_FORMAT_SERIALIZED_CERT_STORE: UInt32 = 5
@winfunctype('CRYPTUI.dll')
def CryptUIDlgViewContext(dwContextType: UInt32, pvContext: c_void_p, hwnd: win32more.Foundation.HWND, pwszTitle: win32more.Foundation.PWSTR, dwFlags: UInt32, pvReserved: c_void_p) -> win32more.Foundation.BOOL: ...
@winfunctype('CRYPTUI.dll')
def CryptUIDlgSelectCertificateFromStore(hCertStore: win32more.Security.Cryptography.HCERTSTORE, hwnd: win32more.Foundation.HWND, pwszTitle: win32more.Foundation.PWSTR, pwszDisplayString: win32more.Foundation.PWSTR, dwDontUseColumn: UInt32, dwFlags: UInt32, pvReserved: c_void_p) -> POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head): ...
@winfunctype('CRYPTUI.dll')
def CertSelectionGetSerializedBlob(pcsi: POINTER(win32more.Security.Cryptography.UI.CERT_SELECTUI_INPUT_head), ppOutBuffer: POINTER(c_void_p), pulOutBufferSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('CRYPTUI.dll')
def CryptUIDlgCertMgr(pCryptUICertMgr: POINTER(win32more.Security.Cryptography.UI.CRYPTUI_CERT_MGR_STRUCT_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('CRYPTUI.dll')
def CryptUIWizDigitalSign(dwFlags: UInt32, hwndParent: win32more.Foundation.HWND, pwszWizardTitle: win32more.Foundation.PWSTR, pDigitalSignInfo: POINTER(win32more.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_INFO_head), ppSignContext: POINTER(POINTER(win32more.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_CONTEXT_head))) -> win32more.Foundation.BOOL: ...
@winfunctype('CRYPTUI.dll')
def CryptUIWizFreeDigitalSignContext(pSignContext: POINTER(win32more.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_CONTEXT_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('CRYPTUI.dll')
def CryptUIDlgViewCertificateW(pCertViewInfo: POINTER(win32more.Security.Cryptography.UI.CRYPTUI_VIEWCERTIFICATE_STRUCTW_head), pfPropertiesChanged: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.BOOL: ...
@winfunctype('CRYPTUI.dll')
def CryptUIDlgViewCertificateA(pCertViewInfo: POINTER(win32more.Security.Cryptography.UI.CRYPTUI_VIEWCERTIFICATE_STRUCTA_head), pfPropertiesChanged: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.BOOL: ...
@winfunctype('CRYPTUI.dll')
def CryptUIWizExport(dwFlags: win32more.Security.Cryptography.UI.CRYPTUI_WIZ_FLAGS, hwndParent: win32more.Foundation.HWND, pwszWizardTitle: win32more.Foundation.PWSTR, pExportInfo: POINTER(win32more.Security.Cryptography.UI.CRYPTUI_WIZ_EXPORT_INFO_head), pvoid: c_void_p) -> win32more.Foundation.BOOL: ...
@winfunctype('CRYPTUI.dll')
def CryptUIWizImport(dwFlags: win32more.Security.Cryptography.UI.CRYPTUI_WIZ_FLAGS, hwndParent: win32more.Foundation.HWND, pwszWizardTitle: win32more.Foundation.PWSTR, pImportSrc: POINTER(win32more.Security.Cryptography.UI.CRYPTUI_WIZ_IMPORT_SRC_INFO_head), hDestCertStore: win32more.Security.Cryptography.HCERTSTORE) -> win32more.Foundation.BOOL: ...
class CERT_FILTER_DATA(Structure):
    dwSize: UInt32
    cExtensionChecks: UInt32
    arrayExtensionChecks: POINTER(win32more.Security.Cryptography.UI.CERT_FILTER_EXTENSION_MATCH_head)
    dwCheckingFlags: UInt32
class CERT_FILTER_EXTENSION_MATCH(Structure):
    szExtensionOID: win32more.Foundation.PSTR
    dwTestOperation: UInt32
    pbTestData: c_char_p_no
    cbTestData: UInt32
class CERT_SELECT_STRUCT_A(Structure):
    dwSize: UInt32
    hwndParent: win32more.Foundation.HWND
    hInstance: win32more.Foundation.HINSTANCE
    pTemplateName: win32more.Foundation.PSTR
    dwFlags: win32more.Security.Cryptography.UI.CERT_SELECT_STRUCT_FLAGS
    szTitle: win32more.Foundation.PSTR
    cCertStore: UInt32
    arrayCertStore: POINTER(win32more.Security.Cryptography.HCERTSTORE)
    szPurposeOid: win32more.Foundation.PSTR
    cCertContext: UInt32
    arrayCertContext: POINTER(POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head))
    lCustData: win32more.Foundation.LPARAM
    pfnHook: win32more.Security.Cryptography.UI.PFNCMHOOKPROC
    pfnFilter: win32more.Security.Cryptography.UI.PFNCMFILTERPROC
    szHelpFileName: win32more.Foundation.PSTR
    dwHelpId: UInt32
    hprov: UIntPtr
CERT_SELECT_STRUCT_FLAGS = UInt32
CSS_HIDE_PROPERTIES: CERT_SELECT_STRUCT_FLAGS = 1
CSS_ENABLEHOOK: CERT_SELECT_STRUCT_FLAGS = 2
CSS_ALLOWMULTISELECT: CERT_SELECT_STRUCT_FLAGS = 4
CSS_SHOW_HELP: CERT_SELECT_STRUCT_FLAGS = 16
CSS_ENABLETEMPLATE: CERT_SELECT_STRUCT_FLAGS = 32
CSS_ENABLETEMPLATEHANDLE: CERT_SELECT_STRUCT_FLAGS = 64
class CERT_SELECT_STRUCT_W(Structure):
    dwSize: UInt32
    hwndParent: win32more.Foundation.HWND
    hInstance: win32more.Foundation.HINSTANCE
    pTemplateName: win32more.Foundation.PWSTR
    dwFlags: win32more.Security.Cryptography.UI.CERT_SELECT_STRUCT_FLAGS
    szTitle: win32more.Foundation.PWSTR
    cCertStore: UInt32
    arrayCertStore: POINTER(win32more.Security.Cryptography.HCERTSTORE)
    szPurposeOid: win32more.Foundation.PSTR
    cCertContext: UInt32
    arrayCertContext: POINTER(POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head))
    lCustData: win32more.Foundation.LPARAM
    pfnHook: win32more.Security.Cryptography.UI.PFNCMHOOKPROC
    pfnFilter: win32more.Security.Cryptography.UI.PFNCMFILTERPROC
    szHelpFileName: win32more.Foundation.PWSTR
    dwHelpId: UInt32
    hprov: UIntPtr
class CERT_SELECTUI_INPUT(Structure):
    hStore: win32more.Security.Cryptography.HCERTSTORE
    prgpChain: POINTER(POINTER(win32more.Security.Cryptography.CERT_CHAIN_CONTEXT_head))
    cChain: UInt32
class CERT_VERIFY_CERTIFICATE_TRUST(Structure):
    cbSize: UInt32
    pccert: POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head)
    dwFlags: UInt32
    dwIgnoreErr: UInt32
    pdwErrors: POINTER(UInt32)
    pszUsageOid: win32more.Foundation.PSTR
    hprov: UIntPtr
    cRootStores: UInt32
    rghstoreRoots: POINTER(win32more.Security.Cryptography.HCERTSTORE)
    cStores: UInt32
    rghstoreCAs: POINTER(win32more.Security.Cryptography.HCERTSTORE)
    cTrustStores: UInt32
    rghstoreTrust: POINTER(win32more.Security.Cryptography.HCERTSTORE)
    lCustData: win32more.Foundation.LPARAM
    pfnTrustHelper: win32more.Security.Cryptography.UI.PFNTRUSTHELPER
    pcChain: POINTER(UInt32)
    prgChain: POINTER(POINTER(POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head)))
    prgdwErrors: POINTER(POINTER(UInt32))
    prgpbTrustInfo: POINTER(POINTER(win32more.Security.Cryptography.CRYPT_INTEGER_BLOB_head))
class CERT_VIEWPROPERTIES_STRUCT_A(Structure):
    dwSize: UInt32
    hwndParent: win32more.Foundation.HWND
    hInstance: win32more.Foundation.HINSTANCE
    dwFlags: win32more.Security.Cryptography.UI.CERT_VIEWPROPERTIES_STRUCT_FLAGS
    szTitle: win32more.Foundation.PSTR
    pCertContext: POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head)
    arrayPurposes: POINTER(win32more.Foundation.PSTR)
    cArrayPurposes: UInt32
    cRootStores: UInt32
    rghstoreRoots: POINTER(win32more.Security.Cryptography.HCERTSTORE)
    cStores: UInt32
    rghstoreCAs: POINTER(win32more.Security.Cryptography.HCERTSTORE)
    cTrustStores: UInt32
    rghstoreTrust: POINTER(win32more.Security.Cryptography.HCERTSTORE)
    hprov: UIntPtr
    lCustData: win32more.Foundation.LPARAM
    dwPad: UInt32
    szHelpFileName: win32more.Foundation.PSTR
    dwHelpId: UInt32
    nStartPage: UInt32
    cArrayPropSheetPages: UInt32
    arrayPropSheetPages: POINTER(win32more.UI.Controls.PROPSHEETPAGEA_head)
CERT_VIEWPROPERTIES_STRUCT_FLAGS = UInt32
CM_ENABLEHOOK: CERT_VIEWPROPERTIES_STRUCT_FLAGS = 1
CM_SHOW_HELP: CERT_VIEWPROPERTIES_STRUCT_FLAGS = 2
CM_SHOW_HELPICON: CERT_VIEWPROPERTIES_STRUCT_FLAGS = 4
CM_ENABLETEMPLATE: CERT_VIEWPROPERTIES_STRUCT_FLAGS = 8
CM_HIDE_ADVANCEPAGE: CERT_VIEWPROPERTIES_STRUCT_FLAGS = 16
CM_HIDE_TRUSTPAGE: CERT_VIEWPROPERTIES_STRUCT_FLAGS = 32
CM_NO_NAMECHANGE: CERT_VIEWPROPERTIES_STRUCT_FLAGS = 64
CM_NO_EDITTRUST: CERT_VIEWPROPERTIES_STRUCT_FLAGS = 128
CM_HIDE_DETAILPAGE: CERT_VIEWPROPERTIES_STRUCT_FLAGS = 256
CM_ADD_CERT_STORES: CERT_VIEWPROPERTIES_STRUCT_FLAGS = 512
class CERT_VIEWPROPERTIES_STRUCT_W(Structure):
    dwSize: UInt32
    hwndParent: win32more.Foundation.HWND
    hInstance: win32more.Foundation.HINSTANCE
    dwFlags: win32more.Security.Cryptography.UI.CERT_VIEWPROPERTIES_STRUCT_FLAGS
    szTitle: win32more.Foundation.PWSTR
    pCertContext: POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head)
    arrayPurposes: POINTER(win32more.Foundation.PSTR)
    cArrayPurposes: UInt32
    cRootStores: UInt32
    rghstoreRoots: POINTER(win32more.Security.Cryptography.HCERTSTORE)
    cStores: UInt32
    rghstoreCAs: POINTER(win32more.Security.Cryptography.HCERTSTORE)
    cTrustStores: UInt32
    rghstoreTrust: POINTER(win32more.Security.Cryptography.HCERTSTORE)
    hprov: UIntPtr
    lCustData: win32more.Foundation.LPARAM
    dwPad: UInt32
    szHelpFileName: win32more.Foundation.PWSTR
    dwHelpId: UInt32
    nStartPage: UInt32
    cArrayPropSheetPages: UInt32
    arrayPropSheetPages: POINTER(win32more.UI.Controls.PROPSHEETPAGEA_head)
class CRYPTUI_CERT_MGR_STRUCT(Structure):
    dwSize: UInt32
    hwndParent: win32more.Foundation.HWND
    dwFlags: UInt32
    pwszTitle: win32more.Foundation.PWSTR
    pszInitUsageOID: win32more.Foundation.PSTR
class CRYPTUI_INITDIALOG_STRUCT(Structure):
    lParam: win32more.Foundation.LPARAM
    pCertContext: POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head)
CRYPTUI_VIEWCERTIFICATE_FLAGS = UInt32
CRYPTUI_HIDE_HIERARCHYPAGE: CRYPTUI_VIEWCERTIFICATE_FLAGS = 1
CRYPTUI_HIDE_DETAILPAGE: CRYPTUI_VIEWCERTIFICATE_FLAGS = 2
CRYPTUI_DISABLE_EDITPROPERTIES: CRYPTUI_VIEWCERTIFICATE_FLAGS = 4
CRYPTUI_ENABLE_EDITPROPERTIES: CRYPTUI_VIEWCERTIFICATE_FLAGS = 8
CRYPTUI_DISABLE_ADDTOSTORE: CRYPTUI_VIEWCERTIFICATE_FLAGS = 16
CRYPTUI_ENABLE_ADDTOSTORE: CRYPTUI_VIEWCERTIFICATE_FLAGS = 32
CRYPTUI_ACCEPT_DECLINE_STYLE: CRYPTUI_VIEWCERTIFICATE_FLAGS = 64
CRYPTUI_IGNORE_UNTRUSTED_ROOT: CRYPTUI_VIEWCERTIFICATE_FLAGS = 128
CRYPTUI_DONT_OPEN_STORES: CRYPTUI_VIEWCERTIFICATE_FLAGS = 256
CRYPTUI_ONLY_OPEN_ROOT_STORE: CRYPTUI_VIEWCERTIFICATE_FLAGS = 512
CRYPTUI_WARN_UNTRUSTED_ROOT: CRYPTUI_VIEWCERTIFICATE_FLAGS = 1024
CRYPTUI_ENABLE_REVOCATION_CHECKING: CRYPTUI_VIEWCERTIFICATE_FLAGS = 2048
CRYPTUI_WARN_REMOTE_TRUST: CRYPTUI_VIEWCERTIFICATE_FLAGS = 4096
CRYPTUI_DISABLE_EXPORT: CRYPTUI_VIEWCERTIFICATE_FLAGS = 8192
CRYPTUI_ENABLE_REVOCATION_CHECK_END_CERT: CRYPTUI_VIEWCERTIFICATE_FLAGS = 16384
CRYPTUI_ENABLE_REVOCATION_CHECK_CHAIN: CRYPTUI_VIEWCERTIFICATE_FLAGS = 32768
CRYPTUI_ENABLE_REVOCATION_CHECK_CHAIN_EXCLUDE_ROOT: CRYPTUI_VIEWCERTIFICATE_FLAGS = 2048
CRYPTUI_DISABLE_HTMLLINK: CRYPTUI_VIEWCERTIFICATE_FLAGS = 65536
CRYPTUI_DISABLE_ISSUERSTATEMENT: CRYPTUI_VIEWCERTIFICATE_FLAGS = 131072
CRYPTUI_CACHE_ONLY_URL_RETRIEVAL: CRYPTUI_VIEWCERTIFICATE_FLAGS = 262144
class CRYPTUI_VIEWCERTIFICATE_STRUCTA(Structure):
    dwSize: UInt32
    hwndParent: win32more.Foundation.HWND
    dwFlags: win32more.Security.Cryptography.UI.CRYPTUI_VIEWCERTIFICATE_FLAGS
    szTitle: win32more.Foundation.PSTR
    pCertContext: POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head)
    rgszPurposes: POINTER(win32more.Foundation.PSTR)
    cPurposes: UInt32
    Anonymous: _Anonymous_e__Union
    fpCryptProviderDataTrustedUsage: win32more.Foundation.BOOL
    idxSigner: UInt32
    idxCert: UInt32
    fCounterSigner: win32more.Foundation.BOOL
    idxCounterSigner: UInt32
    cStores: UInt32
    rghStores: POINTER(win32more.Security.Cryptography.HCERTSTORE)
    cPropSheetPages: UInt32
    rgPropSheetPages: POINTER(win32more.UI.Controls.PROPSHEETPAGEA_head)
    nStartPage: UInt32
    class _Anonymous_e__Union(Union):
        pCryptProviderData: POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_DATA_head)
        hWVTStateData: win32more.Foundation.HANDLE
class CRYPTUI_VIEWCERTIFICATE_STRUCTW(Structure):
    dwSize: UInt32
    hwndParent: win32more.Foundation.HWND
    dwFlags: win32more.Security.Cryptography.UI.CRYPTUI_VIEWCERTIFICATE_FLAGS
    szTitle: win32more.Foundation.PWSTR
    pCertContext: POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head)
    rgszPurposes: POINTER(win32more.Foundation.PSTR)
    cPurposes: UInt32
    Anonymous: _Anonymous_e__Union
    fpCryptProviderDataTrustedUsage: win32more.Foundation.BOOL
    idxSigner: UInt32
    idxCert: UInt32
    fCounterSigner: win32more.Foundation.BOOL
    idxCounterSigner: UInt32
    cStores: UInt32
    rghStores: POINTER(win32more.Security.Cryptography.HCERTSTORE)
    cPropSheetPages: UInt32
    rgPropSheetPages: POINTER(win32more.UI.Controls.PROPSHEETPAGEW_head)
    nStartPage: UInt32
    class _Anonymous_e__Union(Union):
        pCryptProviderData: POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_DATA_head)
        hWVTStateData: win32more.Foundation.HANDLE
CRYPTUI_WIZ_DIGITAL_ADDITIONAL_CERT_CHOICE = UInt32
CRYPTUI_WIZ_DIGITAL_SIGN_ADD_CHAIN: CRYPTUI_WIZ_DIGITAL_ADDITIONAL_CERT_CHOICE = 1
CRYPTUI_WIZ_DIGITAL_SIGN_ADD_CHAIN_NO_ROOT: CRYPTUI_WIZ_DIGITAL_ADDITIONAL_CERT_CHOICE = 2
CRYPTUI_WIZ_DIGITAL_SIGN_ADD_NONE: CRYPTUI_WIZ_DIGITAL_ADDITIONAL_CERT_CHOICE = 0
CRYPTUI_WIZ_DIGITAL_SIGN = UInt32
CRYPTUI_WIZ_DIGITAL_SIGN_CERT: CRYPTUI_WIZ_DIGITAL_SIGN = 1
CRYPTUI_WIZ_DIGITAL_SIGN_STORE: CRYPTUI_WIZ_DIGITAL_SIGN = 2
CRYPTUI_WIZ_DIGITAL_SIGN_PVK: CRYPTUI_WIZ_DIGITAL_SIGN = 3
CRYPTUI_WIZ_DIGITAL_SIGN_NONE: CRYPTUI_WIZ_DIGITAL_SIGN = 0
class CRYPTUI_WIZ_DIGITAL_SIGN_BLOB_INFO(Structure):
    dwSize: UInt32
    pGuidSubject: POINTER(Guid)
    cbBlob: UInt32
    pbBlob: c_char_p_no
    pwszDisplayName: win32more.Foundation.PWSTR
class CRYPTUI_WIZ_DIGITAL_SIGN_CERT_PVK_INFO(Structure):
    dwSize: UInt32
    pwszSigningCertFileName: win32more.Foundation.PWSTR
    dwPvkChoice: win32more.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_PVK_OPTION
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        pPvkFileInfo: POINTER(win32more.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_PVK_FILE_INFO_head)
        pPvkProvInfo: POINTER(win32more.Security.Cryptography.CRYPT_KEY_PROV_INFO_head)
class CRYPTUI_WIZ_DIGITAL_SIGN_CONTEXT(Structure):
    dwSize: UInt32
    cbBlob: UInt32
    pbBlob: c_char_p_no
class CRYPTUI_WIZ_DIGITAL_SIGN_EXTENDED_INFO(Structure):
    dwSize: UInt32
    dwAttrFlags: win32more.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_SIG_TYPE
    pwszDescription: win32more.Foundation.PWSTR
    pwszMoreInfoLocation: win32more.Foundation.PWSTR
    pszHashAlg: win32more.Foundation.PSTR
    pwszSigningCertDisplayString: win32more.Foundation.PWSTR
    hAdditionalCertStore: win32more.Security.Cryptography.HCERTSTORE
    psAuthenticated: POINTER(win32more.Security.Cryptography.CRYPT_ATTRIBUTES_head)
    psUnauthenticated: POINTER(win32more.Security.Cryptography.CRYPT_ATTRIBUTES_head)
class CRYPTUI_WIZ_DIGITAL_SIGN_INFO(Structure):
    dwSize: UInt32
    dwSubjectChoice: win32more.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_SUBJECT
    Anonymous1: _Anonymous1_e__Union
    dwSigningCertChoice: win32more.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN
    Anonymous2: _Anonymous2_e__Union
    pwszTimestampURL: win32more.Foundation.PWSTR
    dwAdditionalCertChoice: win32more.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_ADDITIONAL_CERT_CHOICE
    pSignExtInfo: POINTER(win32more.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_EXTENDED_INFO_head)
    class _Anonymous1_e__Union(Union):
        pwszFileName: win32more.Foundation.PWSTR
        pSignBlobInfo: POINTER(win32more.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_BLOB_INFO_head)
    class _Anonymous2_e__Union(Union):
        pSigningCertContext: POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head)
        pSigningCertStore: POINTER(win32more.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_STORE_INFO_head)
        pSigningCertPvkInfo: POINTER(win32more.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_CERT_PVK_INFO_head)
class CRYPTUI_WIZ_DIGITAL_SIGN_PVK_FILE_INFO(Structure):
    dwSize: UInt32
    pwszPvkFileName: win32more.Foundation.PWSTR
    pwszProvName: win32more.Foundation.PWSTR
    dwProvType: UInt32
CRYPTUI_WIZ_DIGITAL_SIGN_PVK_OPTION = UInt32
CRYPTUI_WIZ_DIGITAL_SIGN_PVK_FILE: CRYPTUI_WIZ_DIGITAL_SIGN_PVK_OPTION = 1
CRYPTUI_WIZ_DIGITAL_SIGN_PVK_PROV: CRYPTUI_WIZ_DIGITAL_SIGN_PVK_OPTION = 2
CRYPTUI_WIZ_DIGITAL_SIGN_SIG_TYPE = UInt32
CRYPTUI_WIZ_DIGITAL_SIGN_COMMERCIAL: CRYPTUI_WIZ_DIGITAL_SIGN_SIG_TYPE = 1
CRYPTUI_WIZ_DIGITAL_SIGN_INDIVIDUAL: CRYPTUI_WIZ_DIGITAL_SIGN_SIG_TYPE = 2
class CRYPTUI_WIZ_DIGITAL_SIGN_STORE_INFO(Structure):
    dwSize: UInt32
    cCertStore: UInt32
    rghCertStore: POINTER(win32more.Security.Cryptography.HCERTSTORE)
    pFilterCallback: win32more.Security.Cryptography.UI.PFNCFILTERPROC
    pvCallbackData: c_void_p
CRYPTUI_WIZ_DIGITAL_SIGN_SUBJECT = UInt32
CRYPTUI_WIZ_DIGITAL_SIGN_SUBJECT_BLOB: CRYPTUI_WIZ_DIGITAL_SIGN_SUBJECT = 2
CRYPTUI_WIZ_DIGITAL_SIGN_SUBJECT_FILE: CRYPTUI_WIZ_DIGITAL_SIGN_SUBJECT = 1
CRYPTUI_WIZ_DIGITAL_SIGN_SUBJECT_NONE: CRYPTUI_WIZ_DIGITAL_SIGN_SUBJECT = 0
class CRYPTUI_WIZ_EXPORT_CERTCONTEXT_INFO(Structure):
    dwSize: UInt32
    dwExportFormat: win32more.Security.Cryptography.UI.CRYPTUI_WIZ_EXPORT_FORMAT
    fExportChain: win32more.Foundation.BOOL
    fExportPrivateKeys: win32more.Foundation.BOOL
    pwszPassword: win32more.Foundation.PWSTR
    fStrongEncryption: win32more.Foundation.BOOL
CRYPTUI_WIZ_EXPORT_FORMAT = UInt32
CRYPTUI_WIZ_EXPORT_FORMAT_DER: CRYPTUI_WIZ_EXPORT_FORMAT = 1
CRYPTUI_WIZ_EXPORT_FORMAT_PFX: CRYPTUI_WIZ_EXPORT_FORMAT = 2
CRYPTUI_WIZ_EXPORT_FORMAT_PKCS7: CRYPTUI_WIZ_EXPORT_FORMAT = 3
CRYPTUI_WIZ_EXPORT_FORMAT_BASE64: CRYPTUI_WIZ_EXPORT_FORMAT = 4
CRYPTUI_WIZ_EXPORT_FORMAT_CRL: CRYPTUI_WIZ_EXPORT_FORMAT = 6
CRYPTUI_WIZ_EXPORT_FORMAT_CTL: CRYPTUI_WIZ_EXPORT_FORMAT = 7
class CRYPTUI_WIZ_EXPORT_INFO(Structure):
    dwSize: UInt32
    pwszExportFileName: win32more.Foundation.PWSTR
    dwSubjectChoice: win32more.Security.Cryptography.UI.CRYPTUI_WIZ_EXPORT_SUBJECT
    Anonymous: _Anonymous_e__Union
    cStores: UInt32
    rghStores: POINTER(win32more.Security.Cryptography.HCERTSTORE)
    class _Anonymous_e__Union(Union):
        pCertContext: POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head)
        pCTLContext: POINTER(win32more.Security.Cryptography.CTL_CONTEXT_head)
        pCRLContext: POINTER(win32more.Security.Cryptography.CRL_CONTEXT_head)
        hCertStore: win32more.Security.Cryptography.HCERTSTORE
CRYPTUI_WIZ_EXPORT_SUBJECT = UInt32
CRYPTUI_WIZ_EXPORT_CERT_CONTEXT: CRYPTUI_WIZ_EXPORT_SUBJECT = 1
CRYPTUI_WIZ_EXPORT_CTL_CONTEXT: CRYPTUI_WIZ_EXPORT_SUBJECT = 2
CRYPTUI_WIZ_EXPORT_CRL_CONTEXT: CRYPTUI_WIZ_EXPORT_SUBJECT = 3
CRYPTUI_WIZ_EXPORT_CERT_STORE: CRYPTUI_WIZ_EXPORT_SUBJECT = 4
CRYPTUI_WIZ_EXPORT_CERT_STORE_CERTIFICATES_ONLY: CRYPTUI_WIZ_EXPORT_SUBJECT = 5
CRYPTUI_WIZ_FLAGS = UInt32
CRYPTUI_WIZ_NO_UI: CRYPTUI_WIZ_FLAGS = 1
CRYPTUI_WIZ_IGNORE_NO_UI_FLAG_FOR_CSPS: CRYPTUI_WIZ_FLAGS = 2
CRYPTUI_WIZ_NO_UI_EXCEPT_CSP: CRYPTUI_WIZ_FLAGS = 3
CRYPTUI_WIZ_IMPORT_ALLOW_CERT: CRYPTUI_WIZ_FLAGS = 131072
CRYPTUI_WIZ_IMPORT_ALLOW_CRL: CRYPTUI_WIZ_FLAGS = 262144
CRYPTUI_WIZ_IMPORT_ALLOW_CTL: CRYPTUI_WIZ_FLAGS = 524288
CRYPTUI_WIZ_IMPORT_NO_CHANGE_DEST_STORE: CRYPTUI_WIZ_FLAGS = 65536
CRYPTUI_WIZ_IMPORT_TO_LOCALMACHINE: CRYPTUI_WIZ_FLAGS = 1048576
CRYPTUI_WIZ_IMPORT_TO_CURRENTUSER: CRYPTUI_WIZ_FLAGS = 2097152
CRYPTUI_WIZ_IMPORT_REMOTE_DEST_STORE: CRYPTUI_WIZ_FLAGS = 4194304
CRYPTUI_WIZ_EXPORT_PRIVATE_KEY: CRYPTUI_WIZ_FLAGS = 256
CRYPTUI_WIZ_EXPORT_NO_DELETE_PRIVATE_KEY: CRYPTUI_WIZ_FLAGS = 512
class CRYPTUI_WIZ_IMPORT_SRC_INFO(Structure):
    dwSize: UInt32
    dwSubjectChoice: win32more.Security.Cryptography.UI.CRYPTUI_WIZ_IMPORT_SUBJECT_OPTION
    Anonymous: _Anonymous_e__Union
    dwFlags: win32more.Security.Cryptography.CRYPT_KEY_FLAGS
    pwszPassword: win32more.Foundation.PWSTR
    class _Anonymous_e__Union(Union):
        pwszFileName: win32more.Foundation.PWSTR
        pCertContext: POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head)
        pCTLContext: POINTER(win32more.Security.Cryptography.CTL_CONTEXT_head)
        pCRLContext: POINTER(win32more.Security.Cryptography.CRL_CONTEXT_head)
        hCertStore: win32more.Security.Cryptography.HCERTSTORE
CRYPTUI_WIZ_IMPORT_SUBJECT_OPTION = UInt32
CRYPTUI_WIZ_IMPORT_SUBJECT_FILE: CRYPTUI_WIZ_IMPORT_SUBJECT_OPTION = 1
CRYPTUI_WIZ_IMPORT_SUBJECT_CERT_CONTEXT: CRYPTUI_WIZ_IMPORT_SUBJECT_OPTION = 2
CRYPTUI_WIZ_IMPORT_SUBJECT_CTL_CONTEXT: CRYPTUI_WIZ_IMPORT_SUBJECT_OPTION = 3
CRYPTUI_WIZ_IMPORT_SUBJECT_CRL_CONTEXT: CRYPTUI_WIZ_IMPORT_SUBJECT_OPTION = 4
CRYPTUI_WIZ_IMPORT_SUBJECT_CERT_STORE: CRYPTUI_WIZ_IMPORT_SUBJECT_OPTION = 5
class CTL_MODIFY_REQUEST(Structure):
    pccert: POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head)
    dwOperation: win32more.Security.Cryptography.UI.CTL_MODIFY_REQUEST_OPERATION
    dwError: UInt32
CTL_MODIFY_REQUEST_OPERATION = UInt32
CTL_MODIFY_REQUEST_ADD_TRUSTED: CTL_MODIFY_REQUEST_OPERATION = 3
CTL_MODIFY_REQUEST_ADD_NOT_TRUSTED: CTL_MODIFY_REQUEST_OPERATION = 1
CTL_MODIFY_REQUEST_REMOVE: CTL_MODIFY_REQUEST_OPERATION = 2
@winfunctype_pointer
def PFNCFILTERPROC(pCertContext: POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head), pfInitialSelectedCert: POINTER(win32more.Foundation.BOOL), pvCallbackData: c_void_p) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def PFNCMFILTERPROC(pCertContext: POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head), param1: win32more.Foundation.LPARAM, param2: UInt32, param3: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def PFNCMHOOKPROC(hwndDialog: win32more.Foundation.HWND, message: UInt32, wParam: win32more.Foundation.WPARAM, lParam: win32more.Foundation.LPARAM) -> UInt32: ...
@winfunctype_pointer
def PFNTRUSTHELPER(pCertContext: POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head), lCustData: win32more.Foundation.LPARAM, fLeafCertificate: win32more.Foundation.BOOL, pbTrustBlob: c_char_p_no) -> win32more.Foundation.HRESULT: ...
make_head(_module, 'CERT_FILTER_DATA')
make_head(_module, 'CERT_FILTER_EXTENSION_MATCH')
make_head(_module, 'CERT_SELECT_STRUCT_A')
make_head(_module, 'CERT_SELECT_STRUCT_W')
make_head(_module, 'CERT_SELECTUI_INPUT')
make_head(_module, 'CERT_VERIFY_CERTIFICATE_TRUST')
make_head(_module, 'CERT_VIEWPROPERTIES_STRUCT_A')
make_head(_module, 'CERT_VIEWPROPERTIES_STRUCT_W')
make_head(_module, 'CRYPTUI_CERT_MGR_STRUCT')
make_head(_module, 'CRYPTUI_INITDIALOG_STRUCT')
make_head(_module, 'CRYPTUI_VIEWCERTIFICATE_STRUCTA')
make_head(_module, 'CRYPTUI_VIEWCERTIFICATE_STRUCTW')
make_head(_module, 'CRYPTUI_WIZ_DIGITAL_SIGN_BLOB_INFO')
make_head(_module, 'CRYPTUI_WIZ_DIGITAL_SIGN_CERT_PVK_INFO')
make_head(_module, 'CRYPTUI_WIZ_DIGITAL_SIGN_CONTEXT')
make_head(_module, 'CRYPTUI_WIZ_DIGITAL_SIGN_EXTENDED_INFO')
make_head(_module, 'CRYPTUI_WIZ_DIGITAL_SIGN_INFO')
make_head(_module, 'CRYPTUI_WIZ_DIGITAL_SIGN_PVK_FILE_INFO')
make_head(_module, 'CRYPTUI_WIZ_DIGITAL_SIGN_STORE_INFO')
make_head(_module, 'CRYPTUI_WIZ_EXPORT_CERTCONTEXT_INFO')
make_head(_module, 'CRYPTUI_WIZ_EXPORT_INFO')
make_head(_module, 'CRYPTUI_WIZ_IMPORT_SRC_INFO')
make_head(_module, 'CTL_MODIFY_REQUEST')
make_head(_module, 'PFNCFILTERPROC')
make_head(_module, 'PFNCMFILTERPROC')
make_head(_module, 'PFNCMHOOKPROC')
make_head(_module, 'PFNTRUSTHELPER')
__all__ = [
    "ACTION_REVOCATION_DEFAULT_CACHE",
    "ACTION_REVOCATION_DEFAULT_ONLINE",
    "CERTVIEW_CRYPTUI_LPARAM",
    "CERT_CREDENTIAL_PROVIDER_ID",
    "CERT_DISPWELL_DISTRUST_ADD_CA_CERT",
    "CERT_DISPWELL_DISTRUST_ADD_LEAF_CERT",
    "CERT_DISPWELL_DISTRUST_CA_CERT",
    "CERT_DISPWELL_DISTRUST_LEAF_CERT",
    "CERT_DISPWELL_SELECT",
    "CERT_DISPWELL_TRUST_ADD_CA_CERT",
    "CERT_DISPWELL_TRUST_ADD_LEAF_CERT",
    "CERT_DISPWELL_TRUST_CA_CERT",
    "CERT_DISPWELL_TRUST_LEAF_CERT",
    "CERT_FILTER_DATA",
    "CERT_FILTER_EXTENSION_MATCH",
    "CERT_FILTER_INCLUDE_V1_CERTS",
    "CERT_FILTER_ISSUER_CERTS_ONLY",
    "CERT_FILTER_KEY_EXISTS",
    "CERT_FILTER_LEAF_CERTS_ONLY",
    "CERT_FILTER_OP_EQUALITY",
    "CERT_FILTER_OP_EXISTS",
    "CERT_FILTER_OP_NOT_EXISTS",
    "CERT_FILTER_VALID_SIGNATURE",
    "CERT_FILTER_VALID_TIME_RANGE",
    "CERT_SELECTUI_INPUT",
    "CERT_SELECT_STRUCT_A",
    "CERT_SELECT_STRUCT_FLAGS",
    "CERT_SELECT_STRUCT_W",
    "CERT_TRUST_DO_FULL_SEARCH",
    "CERT_TRUST_DO_FULL_TRUST",
    "CERT_TRUST_MASK",
    "CERT_TRUST_PERMIT_MISSING_CRLS",
    "CERT_VALIDITY_AFTER_END",
    "CERT_VALIDITY_BEFORE_START",
    "CERT_VALIDITY_CERTIFICATE_REVOKED",
    "CERT_VALIDITY_CRL_OUT_OF_DATE",
    "CERT_VALIDITY_EXPLICITLY_DISTRUSTED",
    "CERT_VALIDITY_EXTENDED_USAGE_FAILURE",
    "CERT_VALIDITY_ISSUER_DISTRUST",
    "CERT_VALIDITY_ISSUER_INVALID",
    "CERT_VALIDITY_KEY_USAGE_EXT_FAILURE",
    "CERT_VALIDITY_MASK_TRUST",
    "CERT_VALIDITY_MASK_VALIDITY",
    "CERT_VALIDITY_NAME_CONSTRAINTS_FAILURE",
    "CERT_VALIDITY_NO_CRL_FOUND",
    "CERT_VALIDITY_NO_ISSUER_CERT_FOUND",
    "CERT_VALIDITY_NO_TRUST_DATA",
    "CERT_VALIDITY_OTHER_ERROR",
    "CERT_VALIDITY_OTHER_EXTENSION_FAILURE",
    "CERT_VALIDITY_PERIOD_NESTING_FAILURE",
    "CERT_VALIDITY_SIGNATURE_FAILS",
    "CERT_VALIDITY_UNKNOWN_CRITICAL_EXTENSION",
    "CERT_VERIFY_CERTIFICATE_TRUST",
    "CERT_VIEWPROPERTIES_STRUCT_A",
    "CERT_VIEWPROPERTIES_STRUCT_FLAGS",
    "CERT_VIEWPROPERTIES_STRUCT_W",
    "CM_ADD_CERT_STORES",
    "CM_ENABLEHOOK",
    "CM_ENABLETEMPLATE",
    "CM_HIDE_ADVANCEPAGE",
    "CM_HIDE_DETAILPAGE",
    "CM_HIDE_TRUSTPAGE",
    "CM_NO_EDITTRUST",
    "CM_NO_NAMECHANGE",
    "CM_SHOW_HELP",
    "CM_SHOW_HELPICON",
    "CM_VIEWFLAGS_MASK",
    "CRYPTDLG_ACTION_MASK",
    "CRYPTDLG_CACHE_ONLY_URL_RETRIEVAL",
    "CRYPTDLG_DISABLE_AIA",
    "CRYPTDLG_POLICY_MASK",
    "CRYPTDLG_REVOCATION_CACHE",
    "CRYPTDLG_REVOCATION_DEFAULT",
    "CRYPTDLG_REVOCATION_NONE",
    "CRYPTDLG_REVOCATION_ONLINE",
    "CRYPTUI_ACCEPT_DECLINE_STYLE",
    "CRYPTUI_CACHE_ONLY_URL_RETRIEVAL",
    "CRYPTUI_CERT_MGR_PUBLISHER_TAB",
    "CRYPTUI_CERT_MGR_SINGLE_TAB_FLAG",
    "CRYPTUI_CERT_MGR_STRUCT",
    "CRYPTUI_CERT_MGR_TAB_MASK",
    "CRYPTUI_DISABLE_ADDTOSTORE",
    "CRYPTUI_DISABLE_EDITPROPERTIES",
    "CRYPTUI_DISABLE_EXPORT",
    "CRYPTUI_DISABLE_HTMLLINK",
    "CRYPTUI_DISABLE_ISSUERSTATEMENT",
    "CRYPTUI_DONT_OPEN_STORES",
    "CRYPTUI_ENABLE_ADDTOSTORE",
    "CRYPTUI_ENABLE_EDITPROPERTIES",
    "CRYPTUI_ENABLE_REVOCATION_CHECKING",
    "CRYPTUI_ENABLE_REVOCATION_CHECK_CHAIN",
    "CRYPTUI_ENABLE_REVOCATION_CHECK_CHAIN_EXCLUDE_ROOT",
    "CRYPTUI_ENABLE_REVOCATION_CHECK_END_CERT",
    "CRYPTUI_HIDE_DETAILPAGE",
    "CRYPTUI_HIDE_HIERARCHYPAGE",
    "CRYPTUI_IGNORE_UNTRUSTED_ROOT",
    "CRYPTUI_INITDIALOG_STRUCT",
    "CRYPTUI_ONLY_OPEN_ROOT_STORE",
    "CRYPTUI_SELECT_EXPIRATION_COLUMN",
    "CRYPTUI_SELECT_FRIENDLYNAME_COLUMN",
    "CRYPTUI_SELECT_INTENDEDUSE_COLUMN",
    "CRYPTUI_SELECT_ISSUEDBY_COLUMN",
    "CRYPTUI_SELECT_ISSUEDTO_COLUMN",
    "CRYPTUI_SELECT_LOCATION_COLUMN",
    "CRYPTUI_VIEWCERTIFICATE_FLAGS",
    "CRYPTUI_VIEWCERTIFICATE_STRUCTA",
    "CRYPTUI_VIEWCERTIFICATE_STRUCTW",
    "CRYPTUI_WARN_REMOTE_TRUST",
    "CRYPTUI_WARN_UNTRUSTED_ROOT",
    "CRYPTUI_WIZ_DIGITAL_ADDITIONAL_CERT_CHOICE",
    "CRYPTUI_WIZ_DIGITAL_SIGN",
    "CRYPTUI_WIZ_DIGITAL_SIGN_ADD_CHAIN",
    "CRYPTUI_WIZ_DIGITAL_SIGN_ADD_CHAIN_NO_ROOT",
    "CRYPTUI_WIZ_DIGITAL_SIGN_ADD_NONE",
    "CRYPTUI_WIZ_DIGITAL_SIGN_BLOB_INFO",
    "CRYPTUI_WIZ_DIGITAL_SIGN_CERT",
    "CRYPTUI_WIZ_DIGITAL_SIGN_CERT_PVK_INFO",
    "CRYPTUI_WIZ_DIGITAL_SIGN_COMMERCIAL",
    "CRYPTUI_WIZ_DIGITAL_SIGN_CONTEXT",
    "CRYPTUI_WIZ_DIGITAL_SIGN_EXCLUDE_PAGE_HASHES",
    "CRYPTUI_WIZ_DIGITAL_SIGN_EXTENDED_INFO",
    "CRYPTUI_WIZ_DIGITAL_SIGN_INCLUDE_PAGE_HASHES",
    "CRYPTUI_WIZ_DIGITAL_SIGN_INDIVIDUAL",
    "CRYPTUI_WIZ_DIGITAL_SIGN_INFO",
    "CRYPTUI_WIZ_DIGITAL_SIGN_NONE",
    "CRYPTUI_WIZ_DIGITAL_SIGN_PVK",
    "CRYPTUI_WIZ_DIGITAL_SIGN_PVK_FILE",
    "CRYPTUI_WIZ_DIGITAL_SIGN_PVK_FILE_INFO",
    "CRYPTUI_WIZ_DIGITAL_SIGN_PVK_OPTION",
    "CRYPTUI_WIZ_DIGITAL_SIGN_PVK_PROV",
    "CRYPTUI_WIZ_DIGITAL_SIGN_SIG_TYPE",
    "CRYPTUI_WIZ_DIGITAL_SIGN_STORE",
    "CRYPTUI_WIZ_DIGITAL_SIGN_STORE_INFO",
    "CRYPTUI_WIZ_DIGITAL_SIGN_SUBJECT",
    "CRYPTUI_WIZ_DIGITAL_SIGN_SUBJECT_BLOB",
    "CRYPTUI_WIZ_DIGITAL_SIGN_SUBJECT_FILE",
    "CRYPTUI_WIZ_DIGITAL_SIGN_SUBJECT_NONE",
    "CRYPTUI_WIZ_EXPORT_CERTCONTEXT_INFO",
    "CRYPTUI_WIZ_EXPORT_CERT_CONTEXT",
    "CRYPTUI_WIZ_EXPORT_CERT_STORE",
    "CRYPTUI_WIZ_EXPORT_CERT_STORE_CERTIFICATES_ONLY",
    "CRYPTUI_WIZ_EXPORT_CRL_CONTEXT",
    "CRYPTUI_WIZ_EXPORT_CTL_CONTEXT",
    "CRYPTUI_WIZ_EXPORT_FORMAT",
    "CRYPTUI_WIZ_EXPORT_FORMAT_BASE64",
    "CRYPTUI_WIZ_EXPORT_FORMAT_CRL",
    "CRYPTUI_WIZ_EXPORT_FORMAT_CTL",
    "CRYPTUI_WIZ_EXPORT_FORMAT_DER",
    "CRYPTUI_WIZ_EXPORT_FORMAT_PFX",
    "CRYPTUI_WIZ_EXPORT_FORMAT_PKCS7",
    "CRYPTUI_WIZ_EXPORT_FORMAT_SERIALIZED_CERT_STORE",
    "CRYPTUI_WIZ_EXPORT_INFO",
    "CRYPTUI_WIZ_EXPORT_NO_DELETE_PRIVATE_KEY",
    "CRYPTUI_WIZ_EXPORT_PRIVATE_KEY",
    "CRYPTUI_WIZ_EXPORT_SUBJECT",
    "CRYPTUI_WIZ_FLAGS",
    "CRYPTUI_WIZ_IGNORE_NO_UI_FLAG_FOR_CSPS",
    "CRYPTUI_WIZ_IMPORT_ALLOW_CERT",
    "CRYPTUI_WIZ_IMPORT_ALLOW_CRL",
    "CRYPTUI_WIZ_IMPORT_ALLOW_CTL",
    "CRYPTUI_WIZ_IMPORT_NO_CHANGE_DEST_STORE",
    "CRYPTUI_WIZ_IMPORT_REMOTE_DEST_STORE",
    "CRYPTUI_WIZ_IMPORT_SRC_INFO",
    "CRYPTUI_WIZ_IMPORT_SUBJECT_CERT_CONTEXT",
    "CRYPTUI_WIZ_IMPORT_SUBJECT_CERT_STORE",
    "CRYPTUI_WIZ_IMPORT_SUBJECT_CRL_CONTEXT",
    "CRYPTUI_WIZ_IMPORT_SUBJECT_CTL_CONTEXT",
    "CRYPTUI_WIZ_IMPORT_SUBJECT_FILE",
    "CRYPTUI_WIZ_IMPORT_SUBJECT_OPTION",
    "CRYPTUI_WIZ_IMPORT_TO_CURRENTUSER",
    "CRYPTUI_WIZ_IMPORT_TO_LOCALMACHINE",
    "CRYPTUI_WIZ_NO_UI",
    "CRYPTUI_WIZ_NO_UI_EXCEPT_CSP",
    "CRYTPDLG_FLAGS_MASK",
    "CSS_ALLOWMULTISELECT",
    "CSS_ENABLEHOOK",
    "CSS_ENABLETEMPLATE",
    "CSS_ENABLETEMPLATEHANDLE",
    "CSS_HIDE_PROPERTIES",
    "CSS_SELECTCERT_MASK",
    "CSS_SHOW_HELP",
    "CTL_MODIFY_REQUEST",
    "CTL_MODIFY_REQUEST_ADD_NOT_TRUSTED",
    "CTL_MODIFY_REQUEST_ADD_TRUSTED",
    "CTL_MODIFY_REQUEST_OPERATION",
    "CTL_MODIFY_REQUEST_REMOVE",
    "CertSelectionGetSerializedBlob",
    "CryptUIDlgCertMgr",
    "CryptUIDlgSelectCertificateFromStore",
    "CryptUIDlgViewCertificateA",
    "CryptUIDlgViewCertificateW",
    "CryptUIDlgViewContext",
    "CryptUIWizDigitalSign",
    "CryptUIWizExport",
    "CryptUIWizFreeDigitalSignContext",
    "CryptUIWizImport",
    "PFNCFILTERPROC",
    "PFNCMFILTERPROC",
    "PFNCMHOOKPROC",
    "PFNTRUSTHELPER",
    "POLICY_IGNORE_NON_CRITICAL_BC",
    "SELCERT_ALGORITHM",
    "SELCERT_CERTLIST",
    "SELCERT_FINEPRINT",
    "SELCERT_ISSUED_TO",
    "SELCERT_PROPERTIES",
    "SELCERT_SERIAL_NUM",
    "SELCERT_THUMBPRINT",
    "SELCERT_VALIDITY",
    "szCERT_CERTIFICATE_ACTION_VERIFY",
]
_arch_optional = [
]
