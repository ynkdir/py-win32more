from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Security.Cryptography
import win32more.Windows.Win32.Security.Cryptography.UI
import win32more.Windows.Win32.Security.WinTrust
import win32more.Windows.Win32.UI.Controls
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
CERT_CERTIFICATE_ACTION_VERIFY: Guid = Guid('{7801ebd0-cf4b-11d0-851f-0060979387ea}')
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
def CryptUIDlgViewContext(dwContextType: UInt32, pvContext: VoidPtr, hwnd: win32more.Windows.Win32.Foundation.HWND, pwszTitle: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, pvReserved: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('CRYPTUI.dll')
def CryptUIDlgSelectCertificateFromStore(hCertStore: win32more.Windows.Win32.Security.Cryptography.HCERTSTORE, hwnd: win32more.Windows.Win32.Foundation.HWND, pwszTitle: win32more.Windows.Win32.Foundation.PWSTR, pwszDisplayString: win32more.Windows.Win32.Foundation.PWSTR, dwDontUseColumn: UInt32, dwFlags: UInt32, pvReserved: VoidPtr) -> POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CONTEXT): ...
@winfunctype('CRYPTUI.dll')
def CertSelectionGetSerializedBlob(pcsi: POINTER(win32more.Windows.Win32.Security.Cryptography.UI.CERT_SELECTUI_INPUT), ppOutBuffer: POINTER(VoidPtr), pulOutBufferSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('CRYPTUI.dll')
def CryptUIDlgCertMgr(pCryptUICertMgr: POINTER(win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_CERT_MGR_STRUCT)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('CRYPTUI.dll')
def CryptUIWizDigitalSign(dwFlags: UInt32, hwndParent: win32more.Windows.Win32.Foundation.HWND, pwszWizardTitle: win32more.Windows.Win32.Foundation.PWSTR, pDigitalSignInfo: POINTER(win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_INFO), ppSignContext: POINTER(POINTER(win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_CONTEXT))) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('CRYPTUI.dll')
def CryptUIWizFreeDigitalSignContext(pSignContext: POINTER(win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_CONTEXT)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('CRYPTUI.dll')
def CryptUIDlgViewCertificateW(pCertViewInfo: POINTER(win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_VIEWCERTIFICATE_STRUCTW), pfPropertiesChanged: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
CryptUIDlgViewCertificate = UnicodeAlias('CryptUIDlgViewCertificateW')
@winfunctype('CRYPTUI.dll')
def CryptUIDlgViewCertificateA(pCertViewInfo: POINTER(win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_VIEWCERTIFICATE_STRUCTA), pfPropertiesChanged: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('CRYPTUI.dll')
def CryptUIWizExport(dwFlags: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_FLAGS, hwndParent: win32more.Windows.Win32.Foundation.HWND, pwszWizardTitle: win32more.Windows.Win32.Foundation.PWSTR, pExportInfo: POINTER(win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_EXPORT_INFO), pvoid: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('CRYPTUI.dll')
def CryptUIWizImport(dwFlags: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_FLAGS, hwndParent: win32more.Windows.Win32.Foundation.HWND, pwszWizardTitle: win32more.Windows.Win32.Foundation.PWSTR, pImportSrc: POINTER(win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_IMPORT_SRC_INFO), hDestCertStore: win32more.Windows.Win32.Security.Cryptography.HCERTSTORE) -> win32more.Windows.Win32.Foundation.BOOL: ...
class CERT_FILTER_DATA(Structure):
    dwSize: UInt32
    cExtensionChecks: UInt32
    arrayExtensionChecks: POINTER(win32more.Windows.Win32.Security.Cryptography.UI.CERT_FILTER_EXTENSION_MATCH)
    dwCheckingFlags: UInt32
class CERT_FILTER_EXTENSION_MATCH(Structure):
    szExtensionOID: win32more.Windows.Win32.Foundation.PSTR
    dwTestOperation: UInt32
    pbTestData: POINTER(Byte)
    cbTestData: UInt32
class CERT_SELECTUI_INPUT(Structure):
    hStore: win32more.Windows.Win32.Security.Cryptography.HCERTSTORE
    prgpChain: POINTER(POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CHAIN_CONTEXT))
    cChain: UInt32
class CERT_SELECT_STRUCT_A(Structure):
    dwSize: UInt32
    hwndParent: win32more.Windows.Win32.Foundation.HWND
    hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
    pTemplateName: win32more.Windows.Win32.Foundation.PSTR
    dwFlags: win32more.Windows.Win32.Security.Cryptography.UI.CERT_SELECT_STRUCT_FLAGS
    szTitle: win32more.Windows.Win32.Foundation.PSTR
    cCertStore: UInt32
    arrayCertStore: POINTER(win32more.Windows.Win32.Security.Cryptography.HCERTSTORE)
    szPurposeOid: win32more.Windows.Win32.Foundation.PSTR
    cCertContext: UInt32
    arrayCertContext: POINTER(POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CONTEXT))
    lCustData: win32more.Windows.Win32.Foundation.LPARAM
    pfnHook: win32more.Windows.Win32.Security.Cryptography.UI.PFNCMHOOKPROC
    pfnFilter: win32more.Windows.Win32.Security.Cryptography.UI.PFNCMFILTERPROC
    szHelpFileName: win32more.Windows.Win32.Foundation.PSTR
    dwHelpId: UInt32
    hprov: UIntPtr
CERT_SELECT_STRUCT_FLAGS = UInt32
CSS_HIDE_PROPERTIES: win32more.Windows.Win32.Security.Cryptography.UI.CERT_SELECT_STRUCT_FLAGS = 1
CSS_ENABLEHOOK: win32more.Windows.Win32.Security.Cryptography.UI.CERT_SELECT_STRUCT_FLAGS = 2
CSS_ALLOWMULTISELECT: win32more.Windows.Win32.Security.Cryptography.UI.CERT_SELECT_STRUCT_FLAGS = 4
CSS_SHOW_HELP: win32more.Windows.Win32.Security.Cryptography.UI.CERT_SELECT_STRUCT_FLAGS = 16
CSS_ENABLETEMPLATE: win32more.Windows.Win32.Security.Cryptography.UI.CERT_SELECT_STRUCT_FLAGS = 32
CSS_ENABLETEMPLATEHANDLE: win32more.Windows.Win32.Security.Cryptography.UI.CERT_SELECT_STRUCT_FLAGS = 64
class CERT_SELECT_STRUCT_W(Structure):
    dwSize: UInt32
    hwndParent: win32more.Windows.Win32.Foundation.HWND
    hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
    pTemplateName: win32more.Windows.Win32.Foundation.PWSTR
    dwFlags: win32more.Windows.Win32.Security.Cryptography.UI.CERT_SELECT_STRUCT_FLAGS
    szTitle: win32more.Windows.Win32.Foundation.PWSTR
    cCertStore: UInt32
    arrayCertStore: POINTER(win32more.Windows.Win32.Security.Cryptography.HCERTSTORE)
    szPurposeOid: win32more.Windows.Win32.Foundation.PSTR
    cCertContext: UInt32
    arrayCertContext: POINTER(POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CONTEXT))
    lCustData: win32more.Windows.Win32.Foundation.LPARAM
    pfnHook: win32more.Windows.Win32.Security.Cryptography.UI.PFNCMHOOKPROC
    pfnFilter: win32more.Windows.Win32.Security.Cryptography.UI.PFNCMFILTERPROC
    szHelpFileName: win32more.Windows.Win32.Foundation.PWSTR
    dwHelpId: UInt32
    hprov: UIntPtr
CERT_SELECT_STRUCT = UnicodeAlias('CERT_SELECT_STRUCT_W')
class CERT_VERIFY_CERTIFICATE_TRUST(Structure):
    cbSize: UInt32
    pccert: POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CONTEXT)
    dwFlags: UInt32
    dwIgnoreErr: UInt32
    pdwErrors: POINTER(UInt32)
    pszUsageOid: win32more.Windows.Win32.Foundation.PSTR
    hprov: UIntPtr
    cRootStores: UInt32
    rghstoreRoots: POINTER(win32more.Windows.Win32.Security.Cryptography.HCERTSTORE)
    cStores: UInt32
    rghstoreCAs: POINTER(win32more.Windows.Win32.Security.Cryptography.HCERTSTORE)
    cTrustStores: UInt32
    rghstoreTrust: POINTER(win32more.Windows.Win32.Security.Cryptography.HCERTSTORE)
    lCustData: win32more.Windows.Win32.Foundation.LPARAM
    pfnTrustHelper: win32more.Windows.Win32.Security.Cryptography.UI.PFNTRUSTHELPER
    pcChain: POINTER(UInt32)
    prgChain: POINTER(POINTER(POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CONTEXT)))
    prgdwErrors: POINTER(POINTER(UInt32))
    prgpbTrustInfo: POINTER(POINTER(win32more.Windows.Win32.Security.Cryptography.CRYPT_INTEGER_BLOB))
class CERT_VIEWPROPERTIES_STRUCT_A(Structure):
    dwSize: UInt32
    hwndParent: win32more.Windows.Win32.Foundation.HWND
    hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
    dwFlags: win32more.Windows.Win32.Security.Cryptography.UI.CERT_VIEWPROPERTIES_STRUCT_FLAGS
    szTitle: win32more.Windows.Win32.Foundation.PSTR
    pCertContext: POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CONTEXT)
    arrayPurposes: POINTER(win32more.Windows.Win32.Foundation.PSTR)
    cArrayPurposes: UInt32
    cRootStores: UInt32
    rghstoreRoots: POINTER(win32more.Windows.Win32.Security.Cryptography.HCERTSTORE)
    cStores: UInt32
    rghstoreCAs: POINTER(win32more.Windows.Win32.Security.Cryptography.HCERTSTORE)
    cTrustStores: UInt32
    rghstoreTrust: POINTER(win32more.Windows.Win32.Security.Cryptography.HCERTSTORE)
    hprov: UIntPtr
    lCustData: win32more.Windows.Win32.Foundation.LPARAM
    dwPad: UInt32
    szHelpFileName: win32more.Windows.Win32.Foundation.PSTR
    dwHelpId: UInt32
    nStartPage: UInt32
    cArrayPropSheetPages: UInt32
    arrayPropSheetPages: POINTER(win32more.Windows.Win32.UI.Controls.PROPSHEETPAGEA)
CERT_VIEWPROPERTIES_STRUCT_FLAGS = UInt32
CM_ENABLEHOOK: win32more.Windows.Win32.Security.Cryptography.UI.CERT_VIEWPROPERTIES_STRUCT_FLAGS = 1
CM_SHOW_HELP: win32more.Windows.Win32.Security.Cryptography.UI.CERT_VIEWPROPERTIES_STRUCT_FLAGS = 2
CM_SHOW_HELPICON: win32more.Windows.Win32.Security.Cryptography.UI.CERT_VIEWPROPERTIES_STRUCT_FLAGS = 4
CM_ENABLETEMPLATE: win32more.Windows.Win32.Security.Cryptography.UI.CERT_VIEWPROPERTIES_STRUCT_FLAGS = 8
CM_HIDE_ADVANCEPAGE: win32more.Windows.Win32.Security.Cryptography.UI.CERT_VIEWPROPERTIES_STRUCT_FLAGS = 16
CM_HIDE_TRUSTPAGE: win32more.Windows.Win32.Security.Cryptography.UI.CERT_VIEWPROPERTIES_STRUCT_FLAGS = 32
CM_NO_NAMECHANGE: win32more.Windows.Win32.Security.Cryptography.UI.CERT_VIEWPROPERTIES_STRUCT_FLAGS = 64
CM_NO_EDITTRUST: win32more.Windows.Win32.Security.Cryptography.UI.CERT_VIEWPROPERTIES_STRUCT_FLAGS = 128
CM_HIDE_DETAILPAGE: win32more.Windows.Win32.Security.Cryptography.UI.CERT_VIEWPROPERTIES_STRUCT_FLAGS = 256
CM_ADD_CERT_STORES: win32more.Windows.Win32.Security.Cryptography.UI.CERT_VIEWPROPERTIES_STRUCT_FLAGS = 512
class CERT_VIEWPROPERTIES_STRUCT_W(Structure):
    dwSize: UInt32
    hwndParent: win32more.Windows.Win32.Foundation.HWND
    hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
    dwFlags: win32more.Windows.Win32.Security.Cryptography.UI.CERT_VIEWPROPERTIES_STRUCT_FLAGS
    szTitle: win32more.Windows.Win32.Foundation.PWSTR
    pCertContext: POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CONTEXT)
    arrayPurposes: POINTER(win32more.Windows.Win32.Foundation.PSTR)
    cArrayPurposes: UInt32
    cRootStores: UInt32
    rghstoreRoots: POINTER(win32more.Windows.Win32.Security.Cryptography.HCERTSTORE)
    cStores: UInt32
    rghstoreCAs: POINTER(win32more.Windows.Win32.Security.Cryptography.HCERTSTORE)
    cTrustStores: UInt32
    rghstoreTrust: POINTER(win32more.Windows.Win32.Security.Cryptography.HCERTSTORE)
    hprov: UIntPtr
    lCustData: win32more.Windows.Win32.Foundation.LPARAM
    dwPad: UInt32
    szHelpFileName: win32more.Windows.Win32.Foundation.PWSTR
    dwHelpId: UInt32
    nStartPage: UInt32
    cArrayPropSheetPages: UInt32
    arrayPropSheetPages: POINTER(win32more.Windows.Win32.UI.Controls.PROPSHEETPAGEA)
CERT_VIEWPROPERTIES_STRUCT = UnicodeAlias('CERT_VIEWPROPERTIES_STRUCT_W')
class CRYPTUI_CERT_MGR_STRUCT(Structure):
    dwSize: UInt32
    hwndParent: win32more.Windows.Win32.Foundation.HWND
    dwFlags: UInt32
    pwszTitle: win32more.Windows.Win32.Foundation.PWSTR
    pszInitUsageOID: win32more.Windows.Win32.Foundation.PSTR
class CRYPTUI_INITDIALOG_STRUCT(Structure):
    lParam: win32more.Windows.Win32.Foundation.LPARAM
    pCertContext: POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CONTEXT)
CRYPTUI_VIEWCERTIFICATE_FLAGS = UInt32
CRYPTUI_HIDE_HIERARCHYPAGE: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_VIEWCERTIFICATE_FLAGS = 1
CRYPTUI_HIDE_DETAILPAGE: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_VIEWCERTIFICATE_FLAGS = 2
CRYPTUI_DISABLE_EDITPROPERTIES: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_VIEWCERTIFICATE_FLAGS = 4
CRYPTUI_ENABLE_EDITPROPERTIES: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_VIEWCERTIFICATE_FLAGS = 8
CRYPTUI_DISABLE_ADDTOSTORE: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_VIEWCERTIFICATE_FLAGS = 16
CRYPTUI_ENABLE_ADDTOSTORE: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_VIEWCERTIFICATE_FLAGS = 32
CRYPTUI_ACCEPT_DECLINE_STYLE: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_VIEWCERTIFICATE_FLAGS = 64
CRYPTUI_IGNORE_UNTRUSTED_ROOT: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_VIEWCERTIFICATE_FLAGS = 128
CRYPTUI_DONT_OPEN_STORES: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_VIEWCERTIFICATE_FLAGS = 256
CRYPTUI_ONLY_OPEN_ROOT_STORE: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_VIEWCERTIFICATE_FLAGS = 512
CRYPTUI_WARN_UNTRUSTED_ROOT: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_VIEWCERTIFICATE_FLAGS = 1024
CRYPTUI_ENABLE_REVOCATION_CHECKING: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_VIEWCERTIFICATE_FLAGS = 2048
CRYPTUI_WARN_REMOTE_TRUST: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_VIEWCERTIFICATE_FLAGS = 4096
CRYPTUI_DISABLE_EXPORT: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_VIEWCERTIFICATE_FLAGS = 8192
CRYPTUI_ENABLE_REVOCATION_CHECK_END_CERT: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_VIEWCERTIFICATE_FLAGS = 16384
CRYPTUI_ENABLE_REVOCATION_CHECK_CHAIN: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_VIEWCERTIFICATE_FLAGS = 32768
CRYPTUI_ENABLE_REVOCATION_CHECK_CHAIN_EXCLUDE_ROOT: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_VIEWCERTIFICATE_FLAGS = 2048
CRYPTUI_DISABLE_HTMLLINK: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_VIEWCERTIFICATE_FLAGS = 65536
CRYPTUI_DISABLE_ISSUERSTATEMENT: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_VIEWCERTIFICATE_FLAGS = 131072
CRYPTUI_CACHE_ONLY_URL_RETRIEVAL: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_VIEWCERTIFICATE_FLAGS = 262144
class CRYPTUI_VIEWCERTIFICATE_STRUCTA(Structure):
    dwSize: UInt32
    hwndParent: win32more.Windows.Win32.Foundation.HWND
    dwFlags: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_VIEWCERTIFICATE_FLAGS
    szTitle: win32more.Windows.Win32.Foundation.PSTR
    pCertContext: POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CONTEXT)
    rgszPurposes: POINTER(win32more.Windows.Win32.Foundation.PSTR)
    cPurposes: UInt32
    Anonymous: _Anonymous_e__Union
    fpCryptProviderDataTrustedUsage: win32more.Windows.Win32.Foundation.BOOL
    idxSigner: UInt32
    idxCert: UInt32
    fCounterSigner: win32more.Windows.Win32.Foundation.BOOL
    idxCounterSigner: UInt32
    cStores: UInt32
    rghStores: POINTER(win32more.Windows.Win32.Security.Cryptography.HCERTSTORE)
    cPropSheetPages: UInt32
    rgPropSheetPages: POINTER(win32more.Windows.Win32.UI.Controls.PROPSHEETPAGEA)
    nStartPage: UInt32
    class _Anonymous_e__Union(Union):
        pCryptProviderData: POINTER(win32more.Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_DATA)
        hWVTStateData: win32more.Windows.Win32.Foundation.HANDLE
class CRYPTUI_VIEWCERTIFICATE_STRUCTW(Structure):
    dwSize: UInt32
    hwndParent: win32more.Windows.Win32.Foundation.HWND
    dwFlags: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_VIEWCERTIFICATE_FLAGS
    szTitle: win32more.Windows.Win32.Foundation.PWSTR
    pCertContext: POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CONTEXT)
    rgszPurposes: POINTER(win32more.Windows.Win32.Foundation.PSTR)
    cPurposes: UInt32
    Anonymous: _Anonymous_e__Union
    fpCryptProviderDataTrustedUsage: win32more.Windows.Win32.Foundation.BOOL
    idxSigner: UInt32
    idxCert: UInt32
    fCounterSigner: win32more.Windows.Win32.Foundation.BOOL
    idxCounterSigner: UInt32
    cStores: UInt32
    rghStores: POINTER(win32more.Windows.Win32.Security.Cryptography.HCERTSTORE)
    cPropSheetPages: UInt32
    rgPropSheetPages: POINTER(win32more.Windows.Win32.UI.Controls.PROPSHEETPAGEW)
    nStartPage: UInt32
    class _Anonymous_e__Union(Union):
        pCryptProviderData: POINTER(win32more.Windows.Win32.Security.WinTrust.CRYPT_PROVIDER_DATA)
        hWVTStateData: win32more.Windows.Win32.Foundation.HANDLE
CRYPTUI_VIEWCERTIFICATE_STRUCT = UnicodeAlias('CRYPTUI_VIEWCERTIFICATE_STRUCTW')
CRYPTUI_WIZ_DIGITAL_ADDITIONAL_CERT_CHOICE = UInt32
CRYPTUI_WIZ_DIGITAL_SIGN_ADD_CHAIN: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_ADDITIONAL_CERT_CHOICE = 1
CRYPTUI_WIZ_DIGITAL_SIGN_ADD_CHAIN_NO_ROOT: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_ADDITIONAL_CERT_CHOICE = 2
CRYPTUI_WIZ_DIGITAL_SIGN_ADD_NONE: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_ADDITIONAL_CERT_CHOICE = 0
CRYPTUI_WIZ_DIGITAL_SIGN = UInt32
CRYPTUI_WIZ_DIGITAL_SIGN_CERT: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN = 1
CRYPTUI_WIZ_DIGITAL_SIGN_STORE: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN = 2
CRYPTUI_WIZ_DIGITAL_SIGN_PVK: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN = 3
CRYPTUI_WIZ_DIGITAL_SIGN_NONE: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN = 0
class CRYPTUI_WIZ_DIGITAL_SIGN_BLOB_INFO(Structure):
    dwSize: UInt32
    pGuidSubject: POINTER(Guid)
    cbBlob: UInt32
    pbBlob: POINTER(Byte)
    pwszDisplayName: win32more.Windows.Win32.Foundation.PWSTR
class CRYPTUI_WIZ_DIGITAL_SIGN_CERT_PVK_INFO(Structure):
    dwSize: UInt32
    pwszSigningCertFileName: win32more.Windows.Win32.Foundation.PWSTR
    dwPvkChoice: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_PVK_OPTION
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        pPvkFileInfo: POINTER(win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_PVK_FILE_INFO)
        pPvkProvInfo: POINTER(win32more.Windows.Win32.Security.Cryptography.CRYPT_KEY_PROV_INFO)
class CRYPTUI_WIZ_DIGITAL_SIGN_CONTEXT(Structure):
    dwSize: UInt32
    cbBlob: UInt32
    pbBlob: POINTER(Byte)
class CRYPTUI_WIZ_DIGITAL_SIGN_EXTENDED_INFO(Structure):
    dwSize: UInt32
    dwAttrFlags: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_SIG_TYPE
    pwszDescription: win32more.Windows.Win32.Foundation.PWSTR
    pwszMoreInfoLocation: win32more.Windows.Win32.Foundation.PWSTR
    pszHashAlg: win32more.Windows.Win32.Foundation.PSTR
    pwszSigningCertDisplayString: win32more.Windows.Win32.Foundation.PWSTR
    hAdditionalCertStore: win32more.Windows.Win32.Security.Cryptography.HCERTSTORE
    psAuthenticated: POINTER(win32more.Windows.Win32.Security.Cryptography.CRYPT_ATTRIBUTES)
    psUnauthenticated: POINTER(win32more.Windows.Win32.Security.Cryptography.CRYPT_ATTRIBUTES)
class CRYPTUI_WIZ_DIGITAL_SIGN_INFO(Structure):
    dwSize: UInt32
    dwSubjectChoice: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_SUBJECT
    Anonymous1: _Anonymous1_e__Union
    dwSigningCertChoice: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN
    Anonymous2: _Anonymous2_e__Union
    pwszTimestampURL: win32more.Windows.Win32.Foundation.PWSTR
    dwAdditionalCertChoice: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_ADDITIONAL_CERT_CHOICE
    pSignExtInfo: POINTER(win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_EXTENDED_INFO)
    class _Anonymous1_e__Union(Union):
        pwszFileName: win32more.Windows.Win32.Foundation.PWSTR
        pSignBlobInfo: POINTER(win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_BLOB_INFO)
    class _Anonymous2_e__Union(Union):
        pSigningCertContext: POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CONTEXT)
        pSigningCertStore: POINTER(win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_STORE_INFO)
        pSigningCertPvkInfo: POINTER(win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_CERT_PVK_INFO)
class CRYPTUI_WIZ_DIGITAL_SIGN_PVK_FILE_INFO(Structure):
    dwSize: UInt32
    pwszPvkFileName: win32more.Windows.Win32.Foundation.PWSTR
    pwszProvName: win32more.Windows.Win32.Foundation.PWSTR
    dwProvType: UInt32
CRYPTUI_WIZ_DIGITAL_SIGN_PVK_OPTION = UInt32
CRYPTUI_WIZ_DIGITAL_SIGN_PVK_FILE: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_PVK_OPTION = 1
CRYPTUI_WIZ_DIGITAL_SIGN_PVK_PROV: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_PVK_OPTION = 2
CRYPTUI_WIZ_DIGITAL_SIGN_SIG_TYPE = UInt32
CRYPTUI_WIZ_DIGITAL_SIGN_COMMERCIAL: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_SIG_TYPE = 1
CRYPTUI_WIZ_DIGITAL_SIGN_INDIVIDUAL: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_SIG_TYPE = 2
class CRYPTUI_WIZ_DIGITAL_SIGN_STORE_INFO(Structure):
    dwSize: UInt32
    cCertStore: UInt32
    rghCertStore: POINTER(win32more.Windows.Win32.Security.Cryptography.HCERTSTORE)
    pFilterCallback: win32more.Windows.Win32.Security.Cryptography.UI.PFNCFILTERPROC
    pvCallbackData: VoidPtr
CRYPTUI_WIZ_DIGITAL_SIGN_SUBJECT = UInt32
CRYPTUI_WIZ_DIGITAL_SIGN_SUBJECT_BLOB: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_SUBJECT = 2
CRYPTUI_WIZ_DIGITAL_SIGN_SUBJECT_FILE: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_SUBJECT = 1
CRYPTUI_WIZ_DIGITAL_SIGN_SUBJECT_NONE: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_SUBJECT = 0
class CRYPTUI_WIZ_EXPORT_CERTCONTEXT_INFO(Structure):
    dwSize: UInt32
    dwExportFormat: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_EXPORT_FORMAT
    fExportChain: win32more.Windows.Win32.Foundation.BOOL
    fExportPrivateKeys: win32more.Windows.Win32.Foundation.BOOL
    pwszPassword: win32more.Windows.Win32.Foundation.PWSTR
    fStrongEncryption: win32more.Windows.Win32.Foundation.BOOL
CRYPTUI_WIZ_EXPORT_FORMAT = UInt32
CRYPTUI_WIZ_EXPORT_FORMAT_DER: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_EXPORT_FORMAT = 1
CRYPTUI_WIZ_EXPORT_FORMAT_PFX: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_EXPORT_FORMAT = 2
CRYPTUI_WIZ_EXPORT_FORMAT_PKCS7: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_EXPORT_FORMAT = 3
CRYPTUI_WIZ_EXPORT_FORMAT_BASE64: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_EXPORT_FORMAT = 4
CRYPTUI_WIZ_EXPORT_FORMAT_CRL: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_EXPORT_FORMAT = 6
CRYPTUI_WIZ_EXPORT_FORMAT_CTL: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_EXPORT_FORMAT = 7
class CRYPTUI_WIZ_EXPORT_INFO(Structure):
    dwSize: UInt32
    pwszExportFileName: win32more.Windows.Win32.Foundation.PWSTR
    dwSubjectChoice: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_EXPORT_SUBJECT
    Anonymous: _Anonymous_e__Union
    cStores: UInt32
    rghStores: POINTER(win32more.Windows.Win32.Security.Cryptography.HCERTSTORE)
    class _Anonymous_e__Union(Union):
        pCertContext: POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CONTEXT)
        pCTLContext: POINTER(win32more.Windows.Win32.Security.Cryptography.CTL_CONTEXT)
        pCRLContext: POINTER(win32more.Windows.Win32.Security.Cryptography.CRL_CONTEXT)
        hCertStore: win32more.Windows.Win32.Security.Cryptography.HCERTSTORE
CRYPTUI_WIZ_EXPORT_SUBJECT = UInt32
CRYPTUI_WIZ_EXPORT_CERT_CONTEXT: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_EXPORT_SUBJECT = 1
CRYPTUI_WIZ_EXPORT_CTL_CONTEXT: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_EXPORT_SUBJECT = 2
CRYPTUI_WIZ_EXPORT_CRL_CONTEXT: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_EXPORT_SUBJECT = 3
CRYPTUI_WIZ_EXPORT_CERT_STORE: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_EXPORT_SUBJECT = 4
CRYPTUI_WIZ_EXPORT_CERT_STORE_CERTIFICATES_ONLY: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_EXPORT_SUBJECT = 5
CRYPTUI_WIZ_FLAGS = UInt32
CRYPTUI_WIZ_NO_UI: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_FLAGS = 1
CRYPTUI_WIZ_IGNORE_NO_UI_FLAG_FOR_CSPS: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_FLAGS = 2
CRYPTUI_WIZ_NO_UI_EXCEPT_CSP: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_FLAGS = 3
CRYPTUI_WIZ_IMPORT_ALLOW_CERT: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_FLAGS = 131072
CRYPTUI_WIZ_IMPORT_ALLOW_CRL: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_FLAGS = 262144
CRYPTUI_WIZ_IMPORT_ALLOW_CTL: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_FLAGS = 524288
CRYPTUI_WIZ_IMPORT_NO_CHANGE_DEST_STORE: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_FLAGS = 65536
CRYPTUI_WIZ_IMPORT_TO_LOCALMACHINE: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_FLAGS = 1048576
CRYPTUI_WIZ_IMPORT_TO_CURRENTUSER: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_FLAGS = 2097152
CRYPTUI_WIZ_IMPORT_REMOTE_DEST_STORE: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_FLAGS = 4194304
CRYPTUI_WIZ_EXPORT_PRIVATE_KEY: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_FLAGS = 256
CRYPTUI_WIZ_EXPORT_NO_DELETE_PRIVATE_KEY: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_FLAGS = 512
class CRYPTUI_WIZ_IMPORT_SRC_INFO(Structure):
    dwSize: UInt32
    dwSubjectChoice: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_IMPORT_SUBJECT_OPTION
    Anonymous: _Anonymous_e__Union
    dwFlags: win32more.Windows.Win32.Security.Cryptography.CRYPT_KEY_FLAGS
    pwszPassword: win32more.Windows.Win32.Foundation.PWSTR
    class _Anonymous_e__Union(Union):
        pwszFileName: win32more.Windows.Win32.Foundation.PWSTR
        pCertContext: POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CONTEXT)
        pCTLContext: POINTER(win32more.Windows.Win32.Security.Cryptography.CTL_CONTEXT)
        pCRLContext: POINTER(win32more.Windows.Win32.Security.Cryptography.CRL_CONTEXT)
        hCertStore: win32more.Windows.Win32.Security.Cryptography.HCERTSTORE
CRYPTUI_WIZ_IMPORT_SUBJECT_OPTION = UInt32
CRYPTUI_WIZ_IMPORT_SUBJECT_FILE: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_IMPORT_SUBJECT_OPTION = 1
CRYPTUI_WIZ_IMPORT_SUBJECT_CERT_CONTEXT: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_IMPORT_SUBJECT_OPTION = 2
CRYPTUI_WIZ_IMPORT_SUBJECT_CTL_CONTEXT: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_IMPORT_SUBJECT_OPTION = 3
CRYPTUI_WIZ_IMPORT_SUBJECT_CRL_CONTEXT: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_IMPORT_SUBJECT_OPTION = 4
CRYPTUI_WIZ_IMPORT_SUBJECT_CERT_STORE: win32more.Windows.Win32.Security.Cryptography.UI.CRYPTUI_WIZ_IMPORT_SUBJECT_OPTION = 5
class CTL_MODIFY_REQUEST(Structure):
    pccert: POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CONTEXT)
    dwOperation: win32more.Windows.Win32.Security.Cryptography.UI.CTL_MODIFY_REQUEST_OPERATION
    dwError: UInt32
CTL_MODIFY_REQUEST_OPERATION = UInt32
CTL_MODIFY_REQUEST_ADD_TRUSTED: win32more.Windows.Win32.Security.Cryptography.UI.CTL_MODIFY_REQUEST_OPERATION = 3
CTL_MODIFY_REQUEST_ADD_NOT_TRUSTED: win32more.Windows.Win32.Security.Cryptography.UI.CTL_MODIFY_REQUEST_OPERATION = 1
CTL_MODIFY_REQUEST_REMOVE: win32more.Windows.Win32.Security.Cryptography.UI.CTL_MODIFY_REQUEST_OPERATION = 2
@winfunctype_pointer
def PFNCFILTERPROC(pCertContext: POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CONTEXT), pfInitialSelectedCert: POINTER(win32more.Windows.Win32.Foundation.BOOL), pvCallbackData: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFNCMFILTERPROC(pCertContext: POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CONTEXT), param1: win32more.Windows.Win32.Foundation.LPARAM, param2: UInt32, param3: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFNCMHOOKPROC(hwndDialog: win32more.Windows.Win32.Foundation.HWND, message: UInt32, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> UInt32: ...
@winfunctype_pointer
def PFNTRUSTHELPER(pCertContext: POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CONTEXT), lCustData: win32more.Windows.Win32.Foundation.LPARAM, fLeafCertificate: win32more.Windows.Win32.Foundation.BOOL, pbTrustBlob: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...


make_ready(__name__)
