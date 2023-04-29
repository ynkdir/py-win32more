from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.Security.Cryptography
import Windows.Win32.Security.Cryptography.UI
import Windows.Win32.Security.WinTrust
import Windows.Win32.UI.Controls
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
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
def CryptUIDlgViewContext(dwContextType: UInt32, pvContext: c_void_p, hwnd: Windows.Win32.Foundation.HWND, pwszTitle: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, pvReserved: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('CRYPTUI.dll')
def CryptUIDlgSelectCertificateFromStore(hCertStore: Windows.Win32.Security.Cryptography.HCERTSTORE, hwnd: Windows.Win32.Foundation.HWND, pwszTitle: Windows.Win32.Foundation.PWSTR, pwszDisplayString: Windows.Win32.Foundation.PWSTR, dwDontUseColumn: UInt32, dwFlags: UInt32, pvReserved: c_void_p) -> POINTER(Windows.Win32.Security.Cryptography.CERT_CONTEXT_head): ...
@winfunctype('CRYPTUI.dll')
def CertSelectionGetSerializedBlob(pcsi: POINTER(Windows.Win32.Security.Cryptography.UI.CERT_SELECTUI_INPUT_head), ppOutBuffer: POINTER(c_void_p), pulOutBufferSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('CRYPTUI.dll')
def CryptUIDlgCertMgr(pCryptUICertMgr: POINTER(Windows.Win32.Security.Cryptography.UI.CRYPTUI_CERT_MGR_STRUCT_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('CRYPTUI.dll')
def CryptUIWizDigitalSign(dwFlags: UInt32, hwndParent: Windows.Win32.Foundation.HWND, pwszWizardTitle: Windows.Win32.Foundation.PWSTR, pDigitalSignInfo: POINTER(Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_INFO_head), ppSignContext: POINTER(POINTER(Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_CONTEXT_head))) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('CRYPTUI.dll')
def CryptUIWizFreeDigitalSignContext(pSignContext: POINTER(Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_CONTEXT_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('CRYPTUI.dll')
def CryptUIDlgViewCertificateW(pCertViewInfo: POINTER(Windows.Win32.Security.Cryptography.UI.CRYPTUI_VIEWCERTIFICATE_STRUCTW_head), pfPropertiesChanged: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('CRYPTUI.dll')
def CryptUIDlgViewCertificateA(pCertViewInfo: POINTER(Windows.Win32.Security.Cryptography.UI.CRYPTUI_VIEWCERTIFICATE_STRUCTA_head), pfPropertiesChanged: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('CRYPTUI.dll')
def CryptUIWizExport(dwFlags: Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_FLAGS, hwndParent: Windows.Win32.Foundation.HWND, pwszWizardTitle: Windows.Win32.Foundation.PWSTR, pExportInfo: POINTER(Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_EXPORT_INFO_head), pvoid: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('CRYPTUI.dll')
def CryptUIWizImport(dwFlags: Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_FLAGS, hwndParent: Windows.Win32.Foundation.HWND, pwszWizardTitle: Windows.Win32.Foundation.PWSTR, pImportSrc: POINTER(Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_IMPORT_SRC_INFO_head), hDestCertStore: Windows.Win32.Security.Cryptography.HCERTSTORE) -> Windows.Win32.Foundation.BOOL: ...
class CERT_FILTER_DATA(EasyCastStructure):
    dwSize: UInt32
    cExtensionChecks: UInt32
    arrayExtensionChecks: POINTER(Windows.Win32.Security.Cryptography.UI.CERT_FILTER_EXTENSION_MATCH_head)
    dwCheckingFlags: UInt32
class CERT_FILTER_EXTENSION_MATCH(EasyCastStructure):
    szExtensionOID: Windows.Win32.Foundation.PSTR
    dwTestOperation: UInt32
    pbTestData: POINTER(Byte)
    cbTestData: UInt32
class CERT_SELECTUI_INPUT(EasyCastStructure):
    hStore: Windows.Win32.Security.Cryptography.HCERTSTORE
    prgpChain: POINTER(POINTER(Windows.Win32.Security.Cryptography.CERT_CHAIN_CONTEXT_head))
    cChain: UInt32
class CERT_SELECT_STRUCT_A(EasyCastStructure):
    dwSize: UInt32
    hwndParent: Windows.Win32.Foundation.HWND
    hInstance: Windows.Win32.Foundation.HMODULE
    pTemplateName: Windows.Win32.Foundation.PSTR
    dwFlags: Windows.Win32.Security.Cryptography.UI.CERT_SELECT_STRUCT_FLAGS
    szTitle: Windows.Win32.Foundation.PSTR
    cCertStore: UInt32
    arrayCertStore: POINTER(Windows.Win32.Security.Cryptography.HCERTSTORE)
    szPurposeOid: Windows.Win32.Foundation.PSTR
    cCertContext: UInt32
    arrayCertContext: POINTER(POINTER(Windows.Win32.Security.Cryptography.CERT_CONTEXT_head))
    lCustData: Windows.Win32.Foundation.LPARAM
    pfnHook: Windows.Win32.Security.Cryptography.UI.PFNCMHOOKPROC
    pfnFilter: Windows.Win32.Security.Cryptography.UI.PFNCMFILTERPROC
    szHelpFileName: Windows.Win32.Foundation.PSTR
    dwHelpId: UInt32
    hprov: UIntPtr
CERT_SELECT_STRUCT_FLAGS = UInt32
CSS_HIDE_PROPERTIES: CERT_SELECT_STRUCT_FLAGS = 1
CSS_ENABLEHOOK: CERT_SELECT_STRUCT_FLAGS = 2
CSS_ALLOWMULTISELECT: CERT_SELECT_STRUCT_FLAGS = 4
CSS_SHOW_HELP: CERT_SELECT_STRUCT_FLAGS = 16
CSS_ENABLETEMPLATE: CERT_SELECT_STRUCT_FLAGS = 32
CSS_ENABLETEMPLATEHANDLE: CERT_SELECT_STRUCT_FLAGS = 64
class CERT_SELECT_STRUCT_W(EasyCastStructure):
    dwSize: UInt32
    hwndParent: Windows.Win32.Foundation.HWND
    hInstance: Windows.Win32.Foundation.HMODULE
    pTemplateName: Windows.Win32.Foundation.PWSTR
    dwFlags: Windows.Win32.Security.Cryptography.UI.CERT_SELECT_STRUCT_FLAGS
    szTitle: Windows.Win32.Foundation.PWSTR
    cCertStore: UInt32
    arrayCertStore: POINTER(Windows.Win32.Security.Cryptography.HCERTSTORE)
    szPurposeOid: Windows.Win32.Foundation.PSTR
    cCertContext: UInt32
    arrayCertContext: POINTER(POINTER(Windows.Win32.Security.Cryptography.CERT_CONTEXT_head))
    lCustData: Windows.Win32.Foundation.LPARAM
    pfnHook: Windows.Win32.Security.Cryptography.UI.PFNCMHOOKPROC
    pfnFilter: Windows.Win32.Security.Cryptography.UI.PFNCMFILTERPROC
    szHelpFileName: Windows.Win32.Foundation.PWSTR
    dwHelpId: UInt32
    hprov: UIntPtr
class CERT_VERIFY_CERTIFICATE_TRUST(EasyCastStructure):
    cbSize: UInt32
    pccert: POINTER(Windows.Win32.Security.Cryptography.CERT_CONTEXT_head)
    dwFlags: UInt32
    dwIgnoreErr: UInt32
    pdwErrors: POINTER(UInt32)
    pszUsageOid: Windows.Win32.Foundation.PSTR
    hprov: UIntPtr
    cRootStores: UInt32
    rghstoreRoots: POINTER(Windows.Win32.Security.Cryptography.HCERTSTORE)
    cStores: UInt32
    rghstoreCAs: POINTER(Windows.Win32.Security.Cryptography.HCERTSTORE)
    cTrustStores: UInt32
    rghstoreTrust: POINTER(Windows.Win32.Security.Cryptography.HCERTSTORE)
    lCustData: Windows.Win32.Foundation.LPARAM
    pfnTrustHelper: Windows.Win32.Security.Cryptography.UI.PFNTRUSTHELPER
    pcChain: POINTER(UInt32)
    prgChain: POINTER(POINTER(POINTER(Windows.Win32.Security.Cryptography.CERT_CONTEXT_head)))
    prgdwErrors: POINTER(POINTER(UInt32))
    prgpbTrustInfo: POINTER(POINTER(Windows.Win32.Security.Cryptography.CRYPT_INTEGER_BLOB_head))
class CERT_VIEWPROPERTIES_STRUCT_A(EasyCastStructure):
    dwSize: UInt32
    hwndParent: Windows.Win32.Foundation.HWND
    hInstance: Windows.Win32.Foundation.HMODULE
    dwFlags: Windows.Win32.Security.Cryptography.UI.CERT_VIEWPROPERTIES_STRUCT_FLAGS
    szTitle: Windows.Win32.Foundation.PSTR
    pCertContext: POINTER(Windows.Win32.Security.Cryptography.CERT_CONTEXT_head)
    arrayPurposes: POINTER(Windows.Win32.Foundation.PSTR)
    cArrayPurposes: UInt32
    cRootStores: UInt32
    rghstoreRoots: POINTER(Windows.Win32.Security.Cryptography.HCERTSTORE)
    cStores: UInt32
    rghstoreCAs: POINTER(Windows.Win32.Security.Cryptography.HCERTSTORE)
    cTrustStores: UInt32
    rghstoreTrust: POINTER(Windows.Win32.Security.Cryptography.HCERTSTORE)
    hprov: UIntPtr
    lCustData: Windows.Win32.Foundation.LPARAM
    dwPad: UInt32
    szHelpFileName: Windows.Win32.Foundation.PSTR
    dwHelpId: UInt32
    nStartPage: UInt32
    cArrayPropSheetPages: UInt32
    arrayPropSheetPages: POINTER(Windows.Win32.UI.Controls.PROPSHEETPAGEA_head)
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
class CERT_VIEWPROPERTIES_STRUCT_W(EasyCastStructure):
    dwSize: UInt32
    hwndParent: Windows.Win32.Foundation.HWND
    hInstance: Windows.Win32.Foundation.HMODULE
    dwFlags: Windows.Win32.Security.Cryptography.UI.CERT_VIEWPROPERTIES_STRUCT_FLAGS
    szTitle: Windows.Win32.Foundation.PWSTR
    pCertContext: POINTER(Windows.Win32.Security.Cryptography.CERT_CONTEXT_head)
    arrayPurposes: POINTER(Windows.Win32.Foundation.PSTR)
    cArrayPurposes: UInt32
    cRootStores: UInt32
    rghstoreRoots: POINTER(Windows.Win32.Security.Cryptography.HCERTSTORE)
    cStores: UInt32
    rghstoreCAs: POINTER(Windows.Win32.Security.Cryptography.HCERTSTORE)
    cTrustStores: UInt32
    rghstoreTrust: POINTER(Windows.Win32.Security.Cryptography.HCERTSTORE)
    hprov: UIntPtr
    lCustData: Windows.Win32.Foundation.LPARAM
    dwPad: UInt32
    szHelpFileName: Windows.Win32.Foundation.PWSTR
    dwHelpId: UInt32
    nStartPage: UInt32
    cArrayPropSheetPages: UInt32
    arrayPropSheetPages: POINTER(Windows.Win32.UI.Controls.PROPSHEETPAGEA_head)
class CRYPTUI_CERT_MGR_STRUCT(EasyCastStructure):
    dwSize: UInt32
    hwndParent: Windows.Win32.Foundation.HWND
    dwFlags: UInt32
    pwszTitle: Windows.Win32.Foundation.PWSTR
    pszInitUsageOID: Windows.Win32.Foundation.PSTR
class CRYPTUI_INITDIALOG_STRUCT(EasyCastStructure):
    lParam: Windows.Win32.Foundation.LPARAM
    pCertContext: POINTER(Windows.Win32.Security.Cryptography.CERT_CONTEXT_head)
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
class CRYPTUI_VIEWCERTIFICATE_STRUCTA(EasyCastStructure):
    dwSize: UInt32
    hwndParent: Windows.Win32.Foundation.HWND
    dwFlags: Windows.Win32.Security.Cryptography.UI.CRYPTUI_VIEWCERTIFICATE_FLAGS
    szTitle: Windows.Win32.Foundation.PSTR
    pCertContext: POINTER(Windows.Win32.Security.Cryptography.CERT_CONTEXT_head)
    rgszPurposes: POINTER(Windows.Win32.Foundation.PSTR)
    cPurposes: UInt32
    Anonymous: _Anonymous_e__Union
    fpCryptProviderDataTrustedUsage: Windows.Win32.Foundation.BOOL
    idxSigner: UInt32
    idxCert: UInt32
    fCounterSigner: Windows.Win32.Foundation.BOOL
    idxCounterSigner: UInt32
    cStores: UInt32
    rghStores: POINTER(Windows.Win32.Security.Cryptography.HCERTSTORE)
    cPropSheetPages: UInt32
    rgPropSheetPages: POINTER(Windows.Win32.UI.Controls.PROPSHEETPAGEA_head)
    nStartPage: UInt32
    class _Anonymous_e__Union(EasyCastUnion):
        pCryptProviderData: POINTER(Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_DATA_head)
        hWVTStateData: Windows.Win32.Foundation.HANDLE
class CRYPTUI_VIEWCERTIFICATE_STRUCTW(EasyCastStructure):
    dwSize: UInt32
    hwndParent: Windows.Win32.Foundation.HWND
    dwFlags: Windows.Win32.Security.Cryptography.UI.CRYPTUI_VIEWCERTIFICATE_FLAGS
    szTitle: Windows.Win32.Foundation.PWSTR
    pCertContext: POINTER(Windows.Win32.Security.Cryptography.CERT_CONTEXT_head)
    rgszPurposes: POINTER(Windows.Win32.Foundation.PSTR)
    cPurposes: UInt32
    Anonymous: _Anonymous_e__Union
    fpCryptProviderDataTrustedUsage: Windows.Win32.Foundation.BOOL
    idxSigner: UInt32
    idxCert: UInt32
    fCounterSigner: Windows.Win32.Foundation.BOOL
    idxCounterSigner: UInt32
    cStores: UInt32
    rghStores: POINTER(Windows.Win32.Security.Cryptography.HCERTSTORE)
    cPropSheetPages: UInt32
    rgPropSheetPages: POINTER(Windows.Win32.UI.Controls.PROPSHEETPAGEW_head)
    nStartPage: UInt32
    class _Anonymous_e__Union(EasyCastUnion):
        pCryptProviderData: POINTER(Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_DATA_head)
        hWVTStateData: Windows.Win32.Foundation.HANDLE
CRYPTUI_WIZ_DIGITAL_ADDITIONAL_CERT_CHOICE = UInt32
CRYPTUI_WIZ_DIGITAL_SIGN_ADD_CHAIN: CRYPTUI_WIZ_DIGITAL_ADDITIONAL_CERT_CHOICE = 1
CRYPTUI_WIZ_DIGITAL_SIGN_ADD_CHAIN_NO_ROOT: CRYPTUI_WIZ_DIGITAL_ADDITIONAL_CERT_CHOICE = 2
CRYPTUI_WIZ_DIGITAL_SIGN_ADD_NONE: CRYPTUI_WIZ_DIGITAL_ADDITIONAL_CERT_CHOICE = 0
CRYPTUI_WIZ_DIGITAL_SIGN = UInt32
CRYPTUI_WIZ_DIGITAL_SIGN_CERT: CRYPTUI_WIZ_DIGITAL_SIGN = 1
CRYPTUI_WIZ_DIGITAL_SIGN_STORE: CRYPTUI_WIZ_DIGITAL_SIGN = 2
CRYPTUI_WIZ_DIGITAL_SIGN_PVK: CRYPTUI_WIZ_DIGITAL_SIGN = 3
CRYPTUI_WIZ_DIGITAL_SIGN_NONE: CRYPTUI_WIZ_DIGITAL_SIGN = 0
class CRYPTUI_WIZ_DIGITAL_SIGN_BLOB_INFO(EasyCastStructure):
    dwSize: UInt32
    pGuidSubject: POINTER(Guid)
    cbBlob: UInt32
    pbBlob: POINTER(Byte)
    pwszDisplayName: Windows.Win32.Foundation.PWSTR
class CRYPTUI_WIZ_DIGITAL_SIGN_CERT_PVK_INFO(EasyCastStructure):
    dwSize: UInt32
    pwszSigningCertFileName: Windows.Win32.Foundation.PWSTR
    dwPvkChoice: Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_PVK_OPTION
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        pPvkFileInfo: POINTER(Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_PVK_FILE_INFO_head)
        pPvkProvInfo: POINTER(Windows.Win32.Security.Cryptography.CRYPT_KEY_PROV_INFO_head)
class CRYPTUI_WIZ_DIGITAL_SIGN_CONTEXT(EasyCastStructure):
    dwSize: UInt32
    cbBlob: UInt32
    pbBlob: POINTER(Byte)
class CRYPTUI_WIZ_DIGITAL_SIGN_EXTENDED_INFO(EasyCastStructure):
    dwSize: UInt32
    dwAttrFlags: Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_SIG_TYPE
    pwszDescription: Windows.Win32.Foundation.PWSTR
    pwszMoreInfoLocation: Windows.Win32.Foundation.PWSTR
    pszHashAlg: Windows.Win32.Foundation.PSTR
    pwszSigningCertDisplayString: Windows.Win32.Foundation.PWSTR
    hAdditionalCertStore: Windows.Win32.Security.Cryptography.HCERTSTORE
    psAuthenticated: POINTER(Windows.Win32.Security.Cryptography.CRYPT_ATTRIBUTES_head)
    psUnauthenticated: POINTER(Windows.Win32.Security.Cryptography.CRYPT_ATTRIBUTES_head)
class CRYPTUI_WIZ_DIGITAL_SIGN_INFO(EasyCastStructure):
    dwSize: UInt32
    dwSubjectChoice: Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_SUBJECT
    Anonymous1: _Anonymous1_e__Union
    dwSigningCertChoice: Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN
    Anonymous2: _Anonymous2_e__Union
    pwszTimestampURL: Windows.Win32.Foundation.PWSTR
    dwAdditionalCertChoice: Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_ADDITIONAL_CERT_CHOICE
    pSignExtInfo: POINTER(Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_EXTENDED_INFO_head)
    class _Anonymous1_e__Union(EasyCastUnion):
        pwszFileName: Windows.Win32.Foundation.PWSTR
        pSignBlobInfo: POINTER(Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_BLOB_INFO_head)
    class _Anonymous2_e__Union(EasyCastUnion):
        pSigningCertContext: POINTER(Windows.Win32.Security.Cryptography.CERT_CONTEXT_head)
        pSigningCertStore: POINTER(Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_STORE_INFO_head)
        pSigningCertPvkInfo: POINTER(Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_CERT_PVK_INFO_head)
class CRYPTUI_WIZ_DIGITAL_SIGN_PVK_FILE_INFO(EasyCastStructure):
    dwSize: UInt32
    pwszPvkFileName: Windows.Win32.Foundation.PWSTR
    pwszProvName: Windows.Win32.Foundation.PWSTR
    dwProvType: UInt32
CRYPTUI_WIZ_DIGITAL_SIGN_PVK_OPTION = UInt32
CRYPTUI_WIZ_DIGITAL_SIGN_PVK_FILE: CRYPTUI_WIZ_DIGITAL_SIGN_PVK_OPTION = 1
CRYPTUI_WIZ_DIGITAL_SIGN_PVK_PROV: CRYPTUI_WIZ_DIGITAL_SIGN_PVK_OPTION = 2
CRYPTUI_WIZ_DIGITAL_SIGN_SIG_TYPE = UInt32
CRYPTUI_WIZ_DIGITAL_SIGN_COMMERCIAL: CRYPTUI_WIZ_DIGITAL_SIGN_SIG_TYPE = 1
CRYPTUI_WIZ_DIGITAL_SIGN_INDIVIDUAL: CRYPTUI_WIZ_DIGITAL_SIGN_SIG_TYPE = 2
class CRYPTUI_WIZ_DIGITAL_SIGN_STORE_INFO(EasyCastStructure):
    dwSize: UInt32
    cCertStore: UInt32
    rghCertStore: POINTER(Windows.Win32.Security.Cryptography.HCERTSTORE)
    pFilterCallback: Windows.Win32.Security.Cryptography.UI.PFNCFILTERPROC
    pvCallbackData: c_void_p
CRYPTUI_WIZ_DIGITAL_SIGN_SUBJECT = UInt32
CRYPTUI_WIZ_DIGITAL_SIGN_SUBJECT_BLOB: CRYPTUI_WIZ_DIGITAL_SIGN_SUBJECT = 2
CRYPTUI_WIZ_DIGITAL_SIGN_SUBJECT_FILE: CRYPTUI_WIZ_DIGITAL_SIGN_SUBJECT = 1
CRYPTUI_WIZ_DIGITAL_SIGN_SUBJECT_NONE: CRYPTUI_WIZ_DIGITAL_SIGN_SUBJECT = 0
class CRYPTUI_WIZ_EXPORT_CERTCONTEXT_INFO(EasyCastStructure):
    dwSize: UInt32
    dwExportFormat: Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_EXPORT_FORMAT
    fExportChain: Windows.Win32.Foundation.BOOL
    fExportPrivateKeys: Windows.Win32.Foundation.BOOL
    pwszPassword: Windows.Win32.Foundation.PWSTR
    fStrongEncryption: Windows.Win32.Foundation.BOOL
CRYPTUI_WIZ_EXPORT_FORMAT = UInt32
CRYPTUI_WIZ_EXPORT_FORMAT_DER: CRYPTUI_WIZ_EXPORT_FORMAT = 1
CRYPTUI_WIZ_EXPORT_FORMAT_PFX: CRYPTUI_WIZ_EXPORT_FORMAT = 2
CRYPTUI_WIZ_EXPORT_FORMAT_PKCS7: CRYPTUI_WIZ_EXPORT_FORMAT = 3
CRYPTUI_WIZ_EXPORT_FORMAT_BASE64: CRYPTUI_WIZ_EXPORT_FORMAT = 4
CRYPTUI_WIZ_EXPORT_FORMAT_CRL: CRYPTUI_WIZ_EXPORT_FORMAT = 6
CRYPTUI_WIZ_EXPORT_FORMAT_CTL: CRYPTUI_WIZ_EXPORT_FORMAT = 7
class CRYPTUI_WIZ_EXPORT_INFO(EasyCastStructure):
    dwSize: UInt32
    pwszExportFileName: Windows.Win32.Foundation.PWSTR
    dwSubjectChoice: Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_EXPORT_SUBJECT
    Anonymous: _Anonymous_e__Union
    cStores: UInt32
    rghStores: POINTER(Windows.Win32.Security.Cryptography.HCERTSTORE)
    class _Anonymous_e__Union(EasyCastUnion):
        pCertContext: POINTER(Windows.Win32.Security.Cryptography.CERT_CONTEXT_head)
        pCTLContext: POINTER(Windows.Win32.Security.Cryptography.CTL_CONTEXT_head)
        pCRLContext: POINTER(Windows.Win32.Security.Cryptography.CRL_CONTEXT_head)
        hCertStore: Windows.Win32.Security.Cryptography.HCERTSTORE
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
class CRYPTUI_WIZ_IMPORT_SRC_INFO(EasyCastStructure):
    dwSize: UInt32
    dwSubjectChoice: Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_IMPORT_SUBJECT_OPTION
    Anonymous: _Anonymous_e__Union
    dwFlags: Windows.Win32.Security.Cryptography.CRYPT_KEY_FLAGS
    pwszPassword: Windows.Win32.Foundation.PWSTR
    class _Anonymous_e__Union(EasyCastUnion):
        pwszFileName: Windows.Win32.Foundation.PWSTR
        pCertContext: POINTER(Windows.Win32.Security.Cryptography.CERT_CONTEXT_head)
        pCTLContext: POINTER(Windows.Win32.Security.Cryptography.CTL_CONTEXT_head)
        pCRLContext: POINTER(Windows.Win32.Security.Cryptography.CRL_CONTEXT_head)
        hCertStore: Windows.Win32.Security.Cryptography.HCERTSTORE
CRYPTUI_WIZ_IMPORT_SUBJECT_OPTION = UInt32
CRYPTUI_WIZ_IMPORT_SUBJECT_FILE: CRYPTUI_WIZ_IMPORT_SUBJECT_OPTION = 1
CRYPTUI_WIZ_IMPORT_SUBJECT_CERT_CONTEXT: CRYPTUI_WIZ_IMPORT_SUBJECT_OPTION = 2
CRYPTUI_WIZ_IMPORT_SUBJECT_CTL_CONTEXT: CRYPTUI_WIZ_IMPORT_SUBJECT_OPTION = 3
CRYPTUI_WIZ_IMPORT_SUBJECT_CRL_CONTEXT: CRYPTUI_WIZ_IMPORT_SUBJECT_OPTION = 4
CRYPTUI_WIZ_IMPORT_SUBJECT_CERT_STORE: CRYPTUI_WIZ_IMPORT_SUBJECT_OPTION = 5
class CTL_MODIFY_REQUEST(EasyCastStructure):
    pccert: POINTER(Windows.Win32.Security.Cryptography.CERT_CONTEXT_head)
    dwOperation: Windows.Win32.Security.Cryptography.UI.CTL_MODIFY_REQUEST_OPERATION
    dwError: UInt32
CTL_MODIFY_REQUEST_OPERATION = UInt32
CTL_MODIFY_REQUEST_ADD_TRUSTED: CTL_MODIFY_REQUEST_OPERATION = 3
CTL_MODIFY_REQUEST_ADD_NOT_TRUSTED: CTL_MODIFY_REQUEST_OPERATION = 1
CTL_MODIFY_REQUEST_REMOVE: CTL_MODIFY_REQUEST_OPERATION = 2
@winfunctype_pointer
def PFNCFILTERPROC(pCertContext: POINTER(Windows.Win32.Security.Cryptography.CERT_CONTEXT_head), pfInitialSelectedCert: POINTER(Windows.Win32.Foundation.BOOL), pvCallbackData: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFNCMFILTERPROC(pCertContext: POINTER(Windows.Win32.Security.Cryptography.CERT_CONTEXT_head), param1: Windows.Win32.Foundation.LPARAM, param2: UInt32, param3: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFNCMHOOKPROC(hwndDialog: Windows.Win32.Foundation.HWND, message: UInt32, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM) -> UInt32: ...
@winfunctype_pointer
def PFNTRUSTHELPER(pCertContext: POINTER(Windows.Win32.Security.Cryptography.CERT_CONTEXT_head), lCustData: Windows.Win32.Foundation.LPARAM, fLeafCertificate: Windows.Win32.Foundation.BOOL, pbTrustBlob: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'CERT_FILTER_DATA')
make_head(_module, 'CERT_FILTER_EXTENSION_MATCH')
make_head(_module, 'CERT_SELECTUI_INPUT')
make_head(_module, 'CERT_SELECT_STRUCT_A')
make_head(_module, 'CERT_SELECT_STRUCT_W')
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
