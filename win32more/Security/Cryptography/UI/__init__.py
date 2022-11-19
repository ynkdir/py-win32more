from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, PROPERTYKEY, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Security.Cryptography
import win32more.Security.Cryptography.UI
import win32more.Security.WinTrust
import win32more.UI.Controls

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
CRYTPDLG_FLAGS_MASK = 4278190080
CRYPTDLG_REVOCATION_DEFAULT = 0
CRYPTDLG_REVOCATION_ONLINE = 2147483648
CRYPTDLG_REVOCATION_CACHE = 1073741824
CRYPTDLG_REVOCATION_NONE = 536870912
CRYPTDLG_CACHE_ONLY_URL_RETRIEVAL = 268435456
CRYPTDLG_DISABLE_AIA = 134217728
CRYPTDLG_POLICY_MASK = 65535
POLICY_IGNORE_NON_CRITICAL_BC = 1
CRYPTDLG_ACTION_MASK = 4294901760
ACTION_REVOCATION_DEFAULT_ONLINE = 65536
ACTION_REVOCATION_DEFAULT_CACHE = 131072
CERT_DISPWELL_SELECT = 1
CERT_DISPWELL_TRUST_CA_CERT = 2
CERT_DISPWELL_TRUST_LEAF_CERT = 3
CERT_DISPWELL_TRUST_ADD_CA_CERT = 4
CERT_DISPWELL_TRUST_ADD_LEAF_CERT = 5
CERT_DISPWELL_DISTRUST_CA_CERT = 6
CERT_DISPWELL_DISTRUST_LEAF_CERT = 7
CERT_DISPWELL_DISTRUST_ADD_CA_CERT = 8
CERT_DISPWELL_DISTRUST_ADD_LEAF_CERT = 9
CSS_SELECTCERT_MASK = 16777215
SELCERT_PROPERTIES = 100
SELCERT_FINEPRINT = 101
SELCERT_CERTLIST = 102
SELCERT_ISSUED_TO = 103
SELCERT_VALIDITY = 104
SELCERT_ALGORITHM = 105
SELCERT_SERIAL_NUM = 106
SELCERT_THUMBPRINT = 107
CM_VIEWFLAGS_MASK = 16777215
CERTVIEW_CRYPTUI_LPARAM = 8388608
CERT_FILTER_OP_EXISTS = 1
CERT_FILTER_OP_NOT_EXISTS = 2
CERT_FILTER_OP_EQUALITY = 3
CERT_FILTER_INCLUDE_V1_CERTS = 1
CERT_FILTER_VALID_TIME_RANGE = 2
CERT_FILTER_VALID_SIGNATURE = 4
CERT_FILTER_LEAF_CERTS_ONLY = 8
CERT_FILTER_ISSUER_CERTS_ONLY = 16
CERT_FILTER_KEY_EXISTS = 32
CERT_VALIDITY_BEFORE_START = 1
CERT_VALIDITY_AFTER_END = 2
CERT_VALIDITY_SIGNATURE_FAILS = 4
CERT_VALIDITY_CERTIFICATE_REVOKED = 8
CERT_VALIDITY_KEY_USAGE_EXT_FAILURE = 16
CERT_VALIDITY_EXTENDED_USAGE_FAILURE = 32
CERT_VALIDITY_NAME_CONSTRAINTS_FAILURE = 64
CERT_VALIDITY_UNKNOWN_CRITICAL_EXTENSION = 128
CERT_VALIDITY_ISSUER_INVALID = 256
CERT_VALIDITY_OTHER_EXTENSION_FAILURE = 512
CERT_VALIDITY_PERIOD_NESTING_FAILURE = 1024
CERT_VALIDITY_OTHER_ERROR = 2048
CERT_VALIDITY_ISSUER_DISTRUST = 33554432
CERT_VALIDITY_EXPLICITLY_DISTRUSTED = 16777216
CERT_VALIDITY_NO_ISSUER_CERT_FOUND = 268435456
CERT_VALIDITY_NO_CRL_FOUND = 536870912
CERT_VALIDITY_CRL_OUT_OF_DATE = 1073741824
CERT_VALIDITY_NO_TRUST_DATA = 2147483648
CERT_VALIDITY_MASK_TRUST = 4294901760
CERT_VALIDITY_MASK_VALIDITY = 65535
CERT_TRUST_MASK = 16777215
CERT_TRUST_DO_FULL_SEARCH = 1
CERT_TRUST_PERMIT_MISSING_CRLS = 2
CERT_TRUST_DO_FULL_TRUST = 5
CERT_CREDENTIAL_PROVIDER_ID = -509
CRYPTUI_SELECT_ISSUEDTO_COLUMN = 1
CRYPTUI_SELECT_ISSUEDBY_COLUMN = 2
CRYPTUI_SELECT_INTENDEDUSE_COLUMN = 4
CRYPTUI_SELECT_FRIENDLYNAME_COLUMN = 8
CRYPTUI_SELECT_LOCATION_COLUMN = 16
CRYPTUI_SELECT_EXPIRATION_COLUMN = 32
CRYPTUI_CERT_MGR_TAB_MASK = 15
CRYPTUI_CERT_MGR_PUBLISHER_TAB = 4
CRYPTUI_CERT_MGR_SINGLE_TAB_FLAG = 32768
CRYPTUI_WIZ_DIGITAL_SIGN_EXCLUDE_PAGE_HASHES = 2
CRYPTUI_WIZ_DIGITAL_SIGN_INCLUDE_PAGE_HASHES = 4
CRYPTUI_WIZ_EXPORT_FORMAT_SERIALIZED_CERT_STORE = 5
CRYPTUI_WIZ_FLAGS = UInt32
CRYPTUI_WIZ_NO_UI = 1
CRYPTUI_WIZ_IGNORE_NO_UI_FLAG_FOR_CSPS = 2
CRYPTUI_WIZ_NO_UI_EXCEPT_CSP = 3
CRYPTUI_WIZ_IMPORT_ALLOW_CERT = 131072
CRYPTUI_WIZ_IMPORT_ALLOW_CRL = 262144
CRYPTUI_WIZ_IMPORT_ALLOW_CTL = 524288
CRYPTUI_WIZ_IMPORT_NO_CHANGE_DEST_STORE = 65536
CRYPTUI_WIZ_IMPORT_TO_LOCALMACHINE = 1048576
CRYPTUI_WIZ_IMPORT_TO_CURRENTUSER = 2097152
CRYPTUI_WIZ_IMPORT_REMOTE_DEST_STORE = 4194304
CRYPTUI_WIZ_EXPORT_PRIVATE_KEY = 256
CRYPTUI_WIZ_EXPORT_NO_DELETE_PRIVATE_KEY = 512
CRYPTUI_VIEWCERTIFICATE_FLAGS = UInt32
CRYPTUI_HIDE_HIERARCHYPAGE = 1
CRYPTUI_HIDE_DETAILPAGE = 2
CRYPTUI_DISABLE_EDITPROPERTIES = 4
CRYPTUI_ENABLE_EDITPROPERTIES = 8
CRYPTUI_DISABLE_ADDTOSTORE = 16
CRYPTUI_ENABLE_ADDTOSTORE = 32
CRYPTUI_ACCEPT_DECLINE_STYLE = 64
CRYPTUI_IGNORE_UNTRUSTED_ROOT = 128
CRYPTUI_DONT_OPEN_STORES = 256
CRYPTUI_ONLY_OPEN_ROOT_STORE = 512
CRYPTUI_WARN_UNTRUSTED_ROOT = 1024
CRYPTUI_ENABLE_REVOCATION_CHECKING = 2048
CRYPTUI_WARN_REMOTE_TRUST = 4096
CRYPTUI_DISABLE_EXPORT = 8192
CRYPTUI_ENABLE_REVOCATION_CHECK_END_CERT = 16384
CRYPTUI_ENABLE_REVOCATION_CHECK_CHAIN = 32768
CRYPTUI_ENABLE_REVOCATION_CHECK_CHAIN_EXCLUDE_ROOT = 2048
CRYPTUI_DISABLE_HTMLLINK = 65536
CRYPTUI_DISABLE_ISSUERSTATEMENT = 131072
CRYPTUI_CACHE_ONLY_URL_RETRIEVAL = 262144
CERT_SELECT_STRUCT_FLAGS = UInt32
CSS_HIDE_PROPERTIES = 1
CSS_ENABLEHOOK = 2
CSS_ALLOWMULTISELECT = 4
CSS_SHOW_HELP = 16
CSS_ENABLETEMPLATE = 32
CSS_ENABLETEMPLATEHANDLE = 64
CRYPTUI_WIZ_IMPORT_SUBJECT_OPTION = UInt32
CRYPTUI_WIZ_IMPORT_SUBJECT_FILE = 1
CRYPTUI_WIZ_IMPORT_SUBJECT_CERT_CONTEXT = 2
CRYPTUI_WIZ_IMPORT_SUBJECT_CTL_CONTEXT = 3
CRYPTUI_WIZ_IMPORT_SUBJECT_CRL_CONTEXT = 4
CRYPTUI_WIZ_IMPORT_SUBJECT_CERT_STORE = 5
CRYPTUI_WIZ_DIGITAL_SIGN_SUBJECT = UInt32
CRYPTUI_WIZ_DIGITAL_SIGN_SUBJECT_BLOB = 2
CRYPTUI_WIZ_DIGITAL_SIGN_SUBJECT_FILE = 1
CRYPTUI_WIZ_DIGITAL_SIGN_SUBJECT_NONE = 0
CRYPTUI_WIZ_DIGITAL_SIGN = UInt32
CRYPTUI_WIZ_DIGITAL_SIGN_CERT = 1
CRYPTUI_WIZ_DIGITAL_SIGN_STORE = 2
CRYPTUI_WIZ_DIGITAL_SIGN_PVK = 3
CRYPTUI_WIZ_DIGITAL_SIGN_NONE = 0
CRYPTUI_WIZ_EXPORT_SUBJECT = UInt32
CRYPTUI_WIZ_EXPORT_CERT_CONTEXT = 1
CRYPTUI_WIZ_EXPORT_CTL_CONTEXT = 2
CRYPTUI_WIZ_EXPORT_CRL_CONTEXT = 3
CRYPTUI_WIZ_EXPORT_CERT_STORE = 4
CRYPTUI_WIZ_EXPORT_CERT_STORE_CERTIFICATES_ONLY = 5
CRYPTUI_WIZ_DIGITAL_SIGN_SIG_TYPE = UInt32
CRYPTUI_WIZ_DIGITAL_SIGN_COMMERCIAL = 1
CRYPTUI_WIZ_DIGITAL_SIGN_INDIVIDUAL = 2
CRYPTUI_WIZ_DIGITAL_SIGN_PVK_OPTION = UInt32
CRYPTUI_WIZ_DIGITAL_SIGN_PVK_FILE = 1
CRYPTUI_WIZ_DIGITAL_SIGN_PVK_PROV = 2
CERT_VIEWPROPERTIES_STRUCT_FLAGS = UInt32
CM_ENABLEHOOK = 1
CM_SHOW_HELP = 2
CM_SHOW_HELPICON = 4
CM_ENABLETEMPLATE = 8
CM_HIDE_ADVANCEPAGE = 16
CM_HIDE_TRUSTPAGE = 32
CM_NO_NAMECHANGE = 64
CM_NO_EDITTRUST = 128
CM_HIDE_DETAILPAGE = 256
CM_ADD_CERT_STORES = 512
CRYPTUI_WIZ_EXPORT_FORMAT = UInt32
CRYPTUI_WIZ_EXPORT_FORMAT_DER = 1
CRYPTUI_WIZ_EXPORT_FORMAT_PFX = 2
CRYPTUI_WIZ_EXPORT_FORMAT_PKCS7 = 3
CRYPTUI_WIZ_EXPORT_FORMAT_BASE64 = 4
CRYPTUI_WIZ_EXPORT_FORMAT_CRL = 6
CRYPTUI_WIZ_EXPORT_FORMAT_CTL = 7
CRYPTUI_WIZ_DIGITAL_ADDITIONAL_CERT_CHOICE = UInt32
CRYPTUI_WIZ_DIGITAL_SIGN_ADD_CHAIN = 1
CRYPTUI_WIZ_DIGITAL_SIGN_ADD_CHAIN_NO_ROOT = 2
CRYPTUI_WIZ_DIGITAL_SIGN_ADD_NONE = 0
CTL_MODIFY_REQUEST_OPERATION = UInt32
CTL_MODIFY_REQUEST_ADD_TRUSTED = 3
CTL_MODIFY_REQUEST_ADD_NOT_TRUSTED = 1
CTL_MODIFY_REQUEST_REMOVE = 2
def _define_PFNCMFILTERPROC():
    return CFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head),win32more.Foundation.LPARAM,UInt32,UInt32, use_last_error=False)
def _define_PFNCMHOOKPROC():
    return CFUNCTYPE(UInt32,win32more.Foundation.HWND,UInt32,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM, use_last_error=False)
def _define_CERT_SELECT_STRUCT_A_head():
    class CERT_SELECT_STRUCT_A(Structure):
        pass
    return CERT_SELECT_STRUCT_A
def _define_CERT_SELECT_STRUCT_A():
    CERT_SELECT_STRUCT_A = win32more.Security.Cryptography.UI.CERT_SELECT_STRUCT_A_head
    CERT_SELECT_STRUCT_A._fields_ = [
        ("dwSize", UInt32),
        ("hwndParent", win32more.Foundation.HWND),
        ("hInstance", win32more.Foundation.HINSTANCE),
        ("pTemplateName", win32more.Foundation.PSTR),
        ("dwFlags", win32more.Security.Cryptography.UI.CERT_SELECT_STRUCT_FLAGS),
        ("szTitle", win32more.Foundation.PSTR),
        ("cCertStore", UInt32),
        ("arrayCertStore", POINTER(c_void_p)),
        ("szPurposeOid", win32more.Foundation.PSTR),
        ("cCertContext", UInt32),
        ("arrayCertContext", POINTER(POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head))),
        ("lCustData", win32more.Foundation.LPARAM),
        ("pfnHook", win32more.Security.Cryptography.UI.PFNCMHOOKPROC),
        ("pfnFilter", win32more.Security.Cryptography.UI.PFNCMFILTERPROC),
        ("szHelpFileName", win32more.Foundation.PSTR),
        ("dwHelpId", UInt32),
        ("hprov", UIntPtr),
    ]
    return CERT_SELECT_STRUCT_A
def _define_CERT_SELECT_STRUCT_W_head():
    class CERT_SELECT_STRUCT_W(Structure):
        pass
    return CERT_SELECT_STRUCT_W
def _define_CERT_SELECT_STRUCT_W():
    CERT_SELECT_STRUCT_W = win32more.Security.Cryptography.UI.CERT_SELECT_STRUCT_W_head
    CERT_SELECT_STRUCT_W._fields_ = [
        ("dwSize", UInt32),
        ("hwndParent", win32more.Foundation.HWND),
        ("hInstance", win32more.Foundation.HINSTANCE),
        ("pTemplateName", win32more.Foundation.PWSTR),
        ("dwFlags", win32more.Security.Cryptography.UI.CERT_SELECT_STRUCT_FLAGS),
        ("szTitle", win32more.Foundation.PWSTR),
        ("cCertStore", UInt32),
        ("arrayCertStore", POINTER(c_void_p)),
        ("szPurposeOid", win32more.Foundation.PSTR),
        ("cCertContext", UInt32),
        ("arrayCertContext", POINTER(POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head))),
        ("lCustData", win32more.Foundation.LPARAM),
        ("pfnHook", win32more.Security.Cryptography.UI.PFNCMHOOKPROC),
        ("pfnFilter", win32more.Security.Cryptography.UI.PFNCMFILTERPROC),
        ("szHelpFileName", win32more.Foundation.PWSTR),
        ("dwHelpId", UInt32),
        ("hprov", UIntPtr),
    ]
    return CERT_SELECT_STRUCT_W
def _define_CERT_VIEWPROPERTIES_STRUCT_A_head():
    class CERT_VIEWPROPERTIES_STRUCT_A(Structure):
        pass
    return CERT_VIEWPROPERTIES_STRUCT_A
def _define_CERT_VIEWPROPERTIES_STRUCT_A():
    CERT_VIEWPROPERTIES_STRUCT_A = win32more.Security.Cryptography.UI.CERT_VIEWPROPERTIES_STRUCT_A_head
    CERT_VIEWPROPERTIES_STRUCT_A._fields_ = [
        ("dwSize", UInt32),
        ("hwndParent", win32more.Foundation.HWND),
        ("hInstance", win32more.Foundation.HINSTANCE),
        ("dwFlags", win32more.Security.Cryptography.UI.CERT_VIEWPROPERTIES_STRUCT_FLAGS),
        ("szTitle", win32more.Foundation.PSTR),
        ("pCertContext", POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head)),
        ("arrayPurposes", POINTER(win32more.Foundation.PSTR)),
        ("cArrayPurposes", UInt32),
        ("cRootStores", UInt32),
        ("rghstoreRoots", POINTER(c_void_p)),
        ("cStores", UInt32),
        ("rghstoreCAs", POINTER(c_void_p)),
        ("cTrustStores", UInt32),
        ("rghstoreTrust", POINTER(c_void_p)),
        ("hprov", UIntPtr),
        ("lCustData", win32more.Foundation.LPARAM),
        ("dwPad", UInt32),
        ("szHelpFileName", win32more.Foundation.PSTR),
        ("dwHelpId", UInt32),
        ("nStartPage", UInt32),
        ("cArrayPropSheetPages", UInt32),
        ("arrayPropSheetPages", POINTER(win32more.UI.Controls.PROPSHEETPAGEA_head)),
    ]
    return CERT_VIEWPROPERTIES_STRUCT_A
def _define_CERT_VIEWPROPERTIES_STRUCT_W_head():
    class CERT_VIEWPROPERTIES_STRUCT_W(Structure):
        pass
    return CERT_VIEWPROPERTIES_STRUCT_W
def _define_CERT_VIEWPROPERTIES_STRUCT_W():
    CERT_VIEWPROPERTIES_STRUCT_W = win32more.Security.Cryptography.UI.CERT_VIEWPROPERTIES_STRUCT_W_head
    CERT_VIEWPROPERTIES_STRUCT_W._fields_ = [
        ("dwSize", UInt32),
        ("hwndParent", win32more.Foundation.HWND),
        ("hInstance", win32more.Foundation.HINSTANCE),
        ("dwFlags", win32more.Security.Cryptography.UI.CERT_VIEWPROPERTIES_STRUCT_FLAGS),
        ("szTitle", win32more.Foundation.PWSTR),
        ("pCertContext", POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head)),
        ("arrayPurposes", POINTER(win32more.Foundation.PSTR)),
        ("cArrayPurposes", UInt32),
        ("cRootStores", UInt32),
        ("rghstoreRoots", POINTER(c_void_p)),
        ("cStores", UInt32),
        ("rghstoreCAs", POINTER(c_void_p)),
        ("cTrustStores", UInt32),
        ("rghstoreTrust", POINTER(c_void_p)),
        ("hprov", UIntPtr),
        ("lCustData", win32more.Foundation.LPARAM),
        ("dwPad", UInt32),
        ("szHelpFileName", win32more.Foundation.PWSTR),
        ("dwHelpId", UInt32),
        ("nStartPage", UInt32),
        ("cArrayPropSheetPages", UInt32),
        ("arrayPropSheetPages", POINTER(win32more.UI.Controls.PROPSHEETPAGEA_head)),
    ]
    return CERT_VIEWPROPERTIES_STRUCT_W
def _define_CMOID_head():
    class CMOID(Structure):
        pass
    return CMOID
def _define_CMOID():
    CMOID = win32more.Security.Cryptography.UI.CMOID_head
    CMOID._fields_ = [
        ("szExtensionOID", win32more.Foundation.PSTR),
        ("dwTestOperation", UInt32),
        ("pbTestData", c_char_p_no),
        ("cbTestData", UInt32),
    ]
    return CMOID
def _define_CMFLTR_head():
    class CMFLTR(Structure):
        pass
    return CMFLTR
def _define_CMFLTR():
    CMFLTR = win32more.Security.Cryptography.UI.CMFLTR_head
    CMFLTR._fields_ = [
        ("dwSize", UInt32),
        ("cExtensionChecks", UInt32),
        ("arrayExtensionChecks", POINTER(win32more.Security.Cryptography.UI.CMOID_head)),
        ("dwCheckingFlags", UInt32),
    ]
    return CMFLTR
def _define_PFNTRUSTHELPER():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head),win32more.Foundation.LPARAM,win32more.Foundation.BOOL,c_char_p_no, use_last_error=False)
def _define_CERT_VERIFY_CERTIFICATE_TRUST_head():
    class CERT_VERIFY_CERTIFICATE_TRUST(Structure):
        pass
    return CERT_VERIFY_CERTIFICATE_TRUST
def _define_CERT_VERIFY_CERTIFICATE_TRUST():
    CERT_VERIFY_CERTIFICATE_TRUST = win32more.Security.Cryptography.UI.CERT_VERIFY_CERTIFICATE_TRUST_head
    CERT_VERIFY_CERTIFICATE_TRUST._fields_ = [
        ("cbSize", UInt32),
        ("pccert", POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head)),
        ("dwFlags", UInt32),
        ("dwIgnoreErr", UInt32),
        ("pdwErrors", POINTER(UInt32)),
        ("pszUsageOid", win32more.Foundation.PSTR),
        ("hprov", UIntPtr),
        ("cRootStores", UInt32),
        ("rghstoreRoots", POINTER(c_void_p)),
        ("cStores", UInt32),
        ("rghstoreCAs", POINTER(c_void_p)),
        ("cTrustStores", UInt32),
        ("rghstoreTrust", POINTER(c_void_p)),
        ("lCustData", win32more.Foundation.LPARAM),
        ("pfnTrustHelper", win32more.Security.Cryptography.UI.PFNTRUSTHELPER),
        ("pcChain", POINTER(UInt32)),
        ("prgChain", POINTER(POINTER(POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head)))),
        ("prgdwErrors", POINTER(POINTER(UInt32))),
        ("prgpbTrustInfo", POINTER(POINTER(win32more.Security.Cryptography.CRYPTOAPI_BLOB_head))),
    ]
    return CERT_VERIFY_CERTIFICATE_TRUST
def _define_CTL_MODIFY_REQUEST_head():
    class CTL_MODIFY_REQUEST(Structure):
        pass
    return CTL_MODIFY_REQUEST
def _define_CTL_MODIFY_REQUEST():
    CTL_MODIFY_REQUEST = win32more.Security.Cryptography.UI.CTL_MODIFY_REQUEST_head
    CTL_MODIFY_REQUEST._fields_ = [
        ("pccert", POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head)),
        ("dwOperation", win32more.Security.Cryptography.UI.CTL_MODIFY_REQUEST_OPERATION),
        ("dwError", UInt32),
    ]
    return CTL_MODIFY_REQUEST
def _define_PFNCFILTERPROC():
    return CFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head),POINTER(win32more.Foundation.BOOL),c_void_p, use_last_error=False)
def _define_CERT_SELECTUI_INPUT_head():
    class CERT_SELECTUI_INPUT(Structure):
        pass
    return CERT_SELECTUI_INPUT
def _define_CERT_SELECTUI_INPUT():
    CERT_SELECTUI_INPUT = win32more.Security.Cryptography.UI.CERT_SELECTUI_INPUT_head
    CERT_SELECTUI_INPUT._fields_ = [
        ("hStore", c_void_p),
        ("prgpChain", POINTER(POINTER(win32more.Security.Cryptography.CERT_CHAIN_CONTEXT_head))),
        ("cChain", UInt32),
    ]
    return CERT_SELECTUI_INPUT
def _define_CRYPTUI_CERT_MGR_STRUCT_head():
    class CRYPTUI_CERT_MGR_STRUCT(Structure):
        pass
    return CRYPTUI_CERT_MGR_STRUCT
def _define_CRYPTUI_CERT_MGR_STRUCT():
    CRYPTUI_CERT_MGR_STRUCT = win32more.Security.Cryptography.UI.CRYPTUI_CERT_MGR_STRUCT_head
    CRYPTUI_CERT_MGR_STRUCT._fields_ = [
        ("dwSize", UInt32),
        ("hwndParent", win32more.Foundation.HWND),
        ("dwFlags", UInt32),
        ("pwszTitle", win32more.Foundation.PWSTR),
        ("pszInitUsageOID", win32more.Foundation.PSTR),
    ]
    return CRYPTUI_CERT_MGR_STRUCT
def _define_CRYPTUI_WIZ_DIGITAL_SIGN_BLOB_INFO_head():
    class CRYPTUI_WIZ_DIGITAL_SIGN_BLOB_INFO(Structure):
        pass
    return CRYPTUI_WIZ_DIGITAL_SIGN_BLOB_INFO
def _define_CRYPTUI_WIZ_DIGITAL_SIGN_BLOB_INFO():
    CRYPTUI_WIZ_DIGITAL_SIGN_BLOB_INFO = win32more.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_BLOB_INFO_head
    CRYPTUI_WIZ_DIGITAL_SIGN_BLOB_INFO._fields_ = [
        ("dwSize", UInt32),
        ("pGuidSubject", POINTER(Guid)),
        ("cbBlob", UInt32),
        ("pbBlob", c_char_p_no),
        ("pwszDisplayName", win32more.Foundation.PWSTR),
    ]
    return CRYPTUI_WIZ_DIGITAL_SIGN_BLOB_INFO
def _define_CRYPTUI_WIZ_DIGITAL_SIGN_STORE_INFO_head():
    class CRYPTUI_WIZ_DIGITAL_SIGN_STORE_INFO(Structure):
        pass
    return CRYPTUI_WIZ_DIGITAL_SIGN_STORE_INFO
def _define_CRYPTUI_WIZ_DIGITAL_SIGN_STORE_INFO():
    CRYPTUI_WIZ_DIGITAL_SIGN_STORE_INFO = win32more.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_STORE_INFO_head
    CRYPTUI_WIZ_DIGITAL_SIGN_STORE_INFO._fields_ = [
        ("dwSize", UInt32),
        ("cCertStore", UInt32),
        ("rghCertStore", POINTER(c_void_p)),
        ("pFilterCallback", win32more.Security.Cryptography.UI.PFNCFILTERPROC),
        ("pvCallbackData", c_void_p),
    ]
    return CRYPTUI_WIZ_DIGITAL_SIGN_STORE_INFO
def _define_CRYPTUI_WIZ_DIGITAL_SIGN_PVK_FILE_INFO_head():
    class CRYPTUI_WIZ_DIGITAL_SIGN_PVK_FILE_INFO(Structure):
        pass
    return CRYPTUI_WIZ_DIGITAL_SIGN_PVK_FILE_INFO
def _define_CRYPTUI_WIZ_DIGITAL_SIGN_PVK_FILE_INFO():
    CRYPTUI_WIZ_DIGITAL_SIGN_PVK_FILE_INFO = win32more.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_PVK_FILE_INFO_head
    CRYPTUI_WIZ_DIGITAL_SIGN_PVK_FILE_INFO._fields_ = [
        ("dwSize", UInt32),
        ("pwszPvkFileName", win32more.Foundation.PWSTR),
        ("pwszProvName", win32more.Foundation.PWSTR),
        ("dwProvType", UInt32),
    ]
    return CRYPTUI_WIZ_DIGITAL_SIGN_PVK_FILE_INFO
def _define_CRYPTUI_WIZ_DIGITAL_SIGN_CERT_PVK_INFO_head():
    class CRYPTUI_WIZ_DIGITAL_SIGN_CERT_PVK_INFO(Structure):
        pass
    return CRYPTUI_WIZ_DIGITAL_SIGN_CERT_PVK_INFO
def _define_CRYPTUI_WIZ_DIGITAL_SIGN_CERT_PVK_INFO():
    CRYPTUI_WIZ_DIGITAL_SIGN_CERT_PVK_INFO = win32more.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_CERT_PVK_INFO_head
    class CRYPTUI_WIZ_DIGITAL_SIGN_CERT_PVK_INFO__Anonymous_e__Union(Union):
        pass
    CRYPTUI_WIZ_DIGITAL_SIGN_CERT_PVK_INFO__Anonymous_e__Union._fields_ = [
        ("pPvkFileInfo", POINTER(win32more.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_PVK_FILE_INFO_head)),
        ("pPvkProvInfo", POINTER(win32more.Security.Cryptography.CRYPT_KEY_PROV_INFO_head)),
    ]
    CRYPTUI_WIZ_DIGITAL_SIGN_CERT_PVK_INFO._anonymous_ = [
        'Anonymous',
    ]
    CRYPTUI_WIZ_DIGITAL_SIGN_CERT_PVK_INFO._fields_ = [
        ("dwSize", UInt32),
        ("pwszSigningCertFileName", win32more.Foundation.PWSTR),
        ("dwPvkChoice", win32more.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_PVK_OPTION),
        ("Anonymous", CRYPTUI_WIZ_DIGITAL_SIGN_CERT_PVK_INFO__Anonymous_e__Union),
    ]
    return CRYPTUI_WIZ_DIGITAL_SIGN_CERT_PVK_INFO
def _define_CRYPTUI_WIZ_DIGITAL_SIGN_EXTENDED_INFO_head():
    class CRYPTUI_WIZ_DIGITAL_SIGN_EXTENDED_INFO(Structure):
        pass
    return CRYPTUI_WIZ_DIGITAL_SIGN_EXTENDED_INFO
def _define_CRYPTUI_WIZ_DIGITAL_SIGN_EXTENDED_INFO():
    CRYPTUI_WIZ_DIGITAL_SIGN_EXTENDED_INFO = win32more.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_EXTENDED_INFO_head
    CRYPTUI_WIZ_DIGITAL_SIGN_EXTENDED_INFO._fields_ = [
        ("dwSize", UInt32),
        ("dwAttrFlags", win32more.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_SIG_TYPE),
        ("pwszDescription", win32more.Foundation.PWSTR),
        ("pwszMoreInfoLocation", win32more.Foundation.PWSTR),
        ("pszHashAlg", win32more.Foundation.PSTR),
        ("pwszSigningCertDisplayString", win32more.Foundation.PWSTR),
        ("hAdditionalCertStore", c_void_p),
        ("psAuthenticated", POINTER(win32more.Security.Cryptography.CRYPT_ATTRIBUTES_head)),
        ("psUnauthenticated", POINTER(win32more.Security.Cryptography.CRYPT_ATTRIBUTES_head)),
    ]
    return CRYPTUI_WIZ_DIGITAL_SIGN_EXTENDED_INFO
def _define_CRYPTUI_WIZ_DIGITAL_SIGN_INFO_head():
    class CRYPTUI_WIZ_DIGITAL_SIGN_INFO(Structure):
        pass
    return CRYPTUI_WIZ_DIGITAL_SIGN_INFO
def _define_CRYPTUI_WIZ_DIGITAL_SIGN_INFO():
    CRYPTUI_WIZ_DIGITAL_SIGN_INFO = win32more.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_INFO_head
    class CRYPTUI_WIZ_DIGITAL_SIGN_INFO__Anonymous2_e__Union(Union):
        pass
    CRYPTUI_WIZ_DIGITAL_SIGN_INFO__Anonymous2_e__Union._fields_ = [
        ("pSigningCertContext", POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head)),
        ("pSigningCertStore", POINTER(win32more.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_STORE_INFO_head)),
        ("pSigningCertPvkInfo", POINTER(win32more.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_CERT_PVK_INFO_head)),
    ]
    class CRYPTUI_WIZ_DIGITAL_SIGN_INFO__Anonymous1_e__Union(Union):
        pass
    CRYPTUI_WIZ_DIGITAL_SIGN_INFO__Anonymous1_e__Union._fields_ = [
        ("pwszFileName", win32more.Foundation.PWSTR),
        ("pSignBlobInfo", POINTER(win32more.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_BLOB_INFO_head)),
    ]
    CRYPTUI_WIZ_DIGITAL_SIGN_INFO._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
    ]
    CRYPTUI_WIZ_DIGITAL_SIGN_INFO._fields_ = [
        ("dwSize", UInt32),
        ("dwSubjectChoice", win32more.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_SUBJECT),
        ("Anonymous1", CRYPTUI_WIZ_DIGITAL_SIGN_INFO__Anonymous1_e__Union),
        ("dwSigningCertChoice", win32more.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN),
        ("Anonymous2", CRYPTUI_WIZ_DIGITAL_SIGN_INFO__Anonymous2_e__Union),
        ("pwszTimestampURL", win32more.Foundation.PWSTR),
        ("dwAdditionalCertChoice", win32more.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_ADDITIONAL_CERT_CHOICE),
        ("pSignExtInfo", POINTER(win32more.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_EXTENDED_INFO_head)),
    ]
    return CRYPTUI_WIZ_DIGITAL_SIGN_INFO
def _define_CRYPTUI_WIZ_DIGITAL_SIGN_CONTEXT_head():
    class CRYPTUI_WIZ_DIGITAL_SIGN_CONTEXT(Structure):
        pass
    return CRYPTUI_WIZ_DIGITAL_SIGN_CONTEXT
def _define_CRYPTUI_WIZ_DIGITAL_SIGN_CONTEXT():
    CRYPTUI_WIZ_DIGITAL_SIGN_CONTEXT = win32more.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_CONTEXT_head
    CRYPTUI_WIZ_DIGITAL_SIGN_CONTEXT._fields_ = [
        ("dwSize", UInt32),
        ("cbBlob", UInt32),
        ("pbBlob", c_char_p_no),
    ]
    return CRYPTUI_WIZ_DIGITAL_SIGN_CONTEXT
def _define_CRYPTUI_INITDIALOG_STRUCT_head():
    class CRYPTUI_INITDIALOG_STRUCT(Structure):
        pass
    return CRYPTUI_INITDIALOG_STRUCT
def _define_CRYPTUI_INITDIALOG_STRUCT():
    CRYPTUI_INITDIALOG_STRUCT = win32more.Security.Cryptography.UI.CRYPTUI_INITDIALOG_STRUCT_head
    CRYPTUI_INITDIALOG_STRUCT._fields_ = [
        ("lParam", win32more.Foundation.LPARAM),
        ("pCertContext", POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head)),
    ]
    return CRYPTUI_INITDIALOG_STRUCT
def _define_CRYPTUI_VIEWCERTIFICATE_STRUCTW_head():
    class CRYPTUI_VIEWCERTIFICATE_STRUCTW(Structure):
        pass
    return CRYPTUI_VIEWCERTIFICATE_STRUCTW
def _define_CRYPTUI_VIEWCERTIFICATE_STRUCTW():
    CRYPTUI_VIEWCERTIFICATE_STRUCTW = win32more.Security.Cryptography.UI.CRYPTUI_VIEWCERTIFICATE_STRUCTW_head
    class CRYPTUI_VIEWCERTIFICATE_STRUCTW__Anonymous_e__Union(Union):
        pass
    CRYPTUI_VIEWCERTIFICATE_STRUCTW__Anonymous_e__Union._fields_ = [
        ("pCryptProviderData", POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_DATA_head)),
        ("hWVTStateData", win32more.Foundation.HANDLE),
    ]
    CRYPTUI_VIEWCERTIFICATE_STRUCTW._anonymous_ = [
        'Anonymous',
    ]
    CRYPTUI_VIEWCERTIFICATE_STRUCTW._fields_ = [
        ("dwSize", UInt32),
        ("hwndParent", win32more.Foundation.HWND),
        ("dwFlags", win32more.Security.Cryptography.UI.CRYPTUI_VIEWCERTIFICATE_FLAGS),
        ("szTitle", win32more.Foundation.PWSTR),
        ("pCertContext", POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head)),
        ("rgszPurposes", POINTER(win32more.Foundation.PSTR)),
        ("cPurposes", UInt32),
        ("Anonymous", CRYPTUI_VIEWCERTIFICATE_STRUCTW__Anonymous_e__Union),
        ("fpCryptProviderDataTrustedUsage", win32more.Foundation.BOOL),
        ("idxSigner", UInt32),
        ("idxCert", UInt32),
        ("fCounterSigner", win32more.Foundation.BOOL),
        ("idxCounterSigner", UInt32),
        ("cStores", UInt32),
        ("rghStores", POINTER(c_void_p)),
        ("cPropSheetPages", UInt32),
        ("rgPropSheetPages", POINTER(win32more.UI.Controls.PROPSHEETPAGEW_head)),
        ("nStartPage", UInt32),
    ]
    return CRYPTUI_VIEWCERTIFICATE_STRUCTW
def _define_CRYPTUI_VIEWCERTIFICATE_STRUCTA_head():
    class CRYPTUI_VIEWCERTIFICATE_STRUCTA(Structure):
        pass
    return CRYPTUI_VIEWCERTIFICATE_STRUCTA
def _define_CRYPTUI_VIEWCERTIFICATE_STRUCTA():
    CRYPTUI_VIEWCERTIFICATE_STRUCTA = win32more.Security.Cryptography.UI.CRYPTUI_VIEWCERTIFICATE_STRUCTA_head
    class CRYPTUI_VIEWCERTIFICATE_STRUCTA__Anonymous_e__Union(Union):
        pass
    CRYPTUI_VIEWCERTIFICATE_STRUCTA__Anonymous_e__Union._fields_ = [
        ("pCryptProviderData", POINTER(win32more.Security.WinTrust.CRYPT_PROVIDER_DATA_head)),
        ("hWVTStateData", win32more.Foundation.HANDLE),
    ]
    CRYPTUI_VIEWCERTIFICATE_STRUCTA._anonymous_ = [
        'Anonymous',
    ]
    CRYPTUI_VIEWCERTIFICATE_STRUCTA._fields_ = [
        ("dwSize", UInt32),
        ("hwndParent", win32more.Foundation.HWND),
        ("dwFlags", win32more.Security.Cryptography.UI.CRYPTUI_VIEWCERTIFICATE_FLAGS),
        ("szTitle", win32more.Foundation.PSTR),
        ("pCertContext", POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head)),
        ("rgszPurposes", POINTER(win32more.Foundation.PSTR)),
        ("cPurposes", UInt32),
        ("Anonymous", CRYPTUI_VIEWCERTIFICATE_STRUCTA__Anonymous_e__Union),
        ("fpCryptProviderDataTrustedUsage", win32more.Foundation.BOOL),
        ("idxSigner", UInt32),
        ("idxCert", UInt32),
        ("fCounterSigner", win32more.Foundation.BOOL),
        ("idxCounterSigner", UInt32),
        ("cStores", UInt32),
        ("rghStores", POINTER(c_void_p)),
        ("cPropSheetPages", UInt32),
        ("rgPropSheetPages", POINTER(win32more.UI.Controls.PROPSHEETPAGEA_head)),
        ("nStartPage", UInt32),
    ]
    return CRYPTUI_VIEWCERTIFICATE_STRUCTA
def _define_CRYPTUI_WIZ_EXPORT_INFO_head():
    class CRYPTUI_WIZ_EXPORT_INFO(Structure):
        pass
    return CRYPTUI_WIZ_EXPORT_INFO
def _define_CRYPTUI_WIZ_EXPORT_INFO():
    CRYPTUI_WIZ_EXPORT_INFO = win32more.Security.Cryptography.UI.CRYPTUI_WIZ_EXPORT_INFO_head
    class CRYPTUI_WIZ_EXPORT_INFO__Anonymous_e__Union(Union):
        pass
    CRYPTUI_WIZ_EXPORT_INFO__Anonymous_e__Union._fields_ = [
        ("pCertContext", POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head)),
        ("pCTLContext", POINTER(win32more.Security.Cryptography.CTL_CONTEXT_head)),
        ("pCRLContext", POINTER(win32more.Security.Cryptography.CRL_CONTEXT_head)),
        ("hCertStore", c_void_p),
    ]
    CRYPTUI_WIZ_EXPORT_INFO._anonymous_ = [
        'Anonymous',
    ]
    CRYPTUI_WIZ_EXPORT_INFO._fields_ = [
        ("dwSize", UInt32),
        ("pwszExportFileName", win32more.Foundation.PWSTR),
        ("dwSubjectChoice", win32more.Security.Cryptography.UI.CRYPTUI_WIZ_EXPORT_SUBJECT),
        ("Anonymous", CRYPTUI_WIZ_EXPORT_INFO__Anonymous_e__Union),
        ("cStores", UInt32),
        ("rghStores", POINTER(c_void_p)),
    ]
    return CRYPTUI_WIZ_EXPORT_INFO
def _define_CRYPTUI_WIZ_EXPORT_CERTCONTEXT_INFO_head():
    class CRYPTUI_WIZ_EXPORT_CERTCONTEXT_INFO(Structure):
        pass
    return CRYPTUI_WIZ_EXPORT_CERTCONTEXT_INFO
def _define_CRYPTUI_WIZ_EXPORT_CERTCONTEXT_INFO():
    CRYPTUI_WIZ_EXPORT_CERTCONTEXT_INFO = win32more.Security.Cryptography.UI.CRYPTUI_WIZ_EXPORT_CERTCONTEXT_INFO_head
    CRYPTUI_WIZ_EXPORT_CERTCONTEXT_INFO._fields_ = [
        ("dwSize", UInt32),
        ("dwExportFormat", win32more.Security.Cryptography.UI.CRYPTUI_WIZ_EXPORT_FORMAT),
        ("fExportChain", win32more.Foundation.BOOL),
        ("fExportPrivateKeys", win32more.Foundation.BOOL),
        ("pwszPassword", win32more.Foundation.PWSTR),
        ("fStrongEncryption", win32more.Foundation.BOOL),
    ]
    return CRYPTUI_WIZ_EXPORT_CERTCONTEXT_INFO
def _define_CRYPTUI_WIZ_IMPORT_SRC_INFO_head():
    class CRYPTUI_WIZ_IMPORT_SRC_INFO(Structure):
        pass
    return CRYPTUI_WIZ_IMPORT_SRC_INFO
def _define_CRYPTUI_WIZ_IMPORT_SRC_INFO():
    CRYPTUI_WIZ_IMPORT_SRC_INFO = win32more.Security.Cryptography.UI.CRYPTUI_WIZ_IMPORT_SRC_INFO_head
    class CRYPTUI_WIZ_IMPORT_SRC_INFO__Anonymous_e__Union(Union):
        pass
    CRYPTUI_WIZ_IMPORT_SRC_INFO__Anonymous_e__Union._fields_ = [
        ("pwszFileName", win32more.Foundation.PWSTR),
        ("pCertContext", POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head)),
        ("pCTLContext", POINTER(win32more.Security.Cryptography.CTL_CONTEXT_head)),
        ("pCRLContext", POINTER(win32more.Security.Cryptography.CRL_CONTEXT_head)),
        ("hCertStore", c_void_p),
    ]
    CRYPTUI_WIZ_IMPORT_SRC_INFO._anonymous_ = [
        'Anonymous',
    ]
    CRYPTUI_WIZ_IMPORT_SRC_INFO._fields_ = [
        ("dwSize", UInt32),
        ("dwSubjectChoice", win32more.Security.Cryptography.UI.CRYPTUI_WIZ_IMPORT_SUBJECT_OPTION),
        ("Anonymous", CRYPTUI_WIZ_IMPORT_SRC_INFO__Anonymous_e__Union),
        ("dwFlags", win32more.Security.Cryptography.CRYPT_KEY_FLAGS),
        ("pwszPassword", win32more.Foundation.PWSTR),
    ]
    return CRYPTUI_WIZ_IMPORT_SRC_INFO
def _define_CryptUIDlgViewContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,c_void_p,win32more.Foundation.HWND,win32more.Foundation.PWSTR,UInt32,c_void_p, use_last_error=False)(("CryptUIDlgViewContext", windll["CRYPTUI"]), ((1, 'dwContextType'),(1, 'pvContext'),(1, 'hwnd'),(1, 'pwszTitle'),(1, 'dwFlags'),(1, 'pvReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptUIDlgSelectCertificateFromStore():
    try:
        return WINFUNCTYPE(POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head),c_void_p,win32more.Foundation.HWND,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,UInt32,c_void_p, use_last_error=False)(("CryptUIDlgSelectCertificateFromStore", windll["CRYPTUI"]), ((1, 'hCertStore'),(1, 'hwnd'),(1, 'pwszTitle'),(1, 'pwszDisplayString'),(1, 'dwDontUseColumn'),(1, 'dwFlags'),(1, 'pvReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CertSelectionGetSerializedBlob():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.UI.CERT_SELECTUI_INPUT_head),POINTER(c_void_p),POINTER(UInt32), use_last_error=False)(("CertSelectionGetSerializedBlob", windll["CRYPTUI"]), ((1, 'pcsi'),(1, 'ppOutBuffer'),(1, 'pulOutBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptUIDlgCertMgr():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.Cryptography.UI.CRYPTUI_CERT_MGR_STRUCT_head), use_last_error=False)(("CryptUIDlgCertMgr", windll["CRYPTUI"]), ((1, 'pCryptUICertMgr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptUIWizDigitalSign():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.Foundation.HWND,win32more.Foundation.PWSTR,POINTER(win32more.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_INFO_head),POINTER(POINTER(win32more.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_CONTEXT_head)), use_last_error=False)(("CryptUIWizDigitalSign", windll["CRYPTUI"]), ((1, 'dwFlags'),(1, 'hwndParent'),(1, 'pwszWizardTitle'),(1, 'pDigitalSignInfo'),(1, 'ppSignContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptUIWizFreeDigitalSignContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.Cryptography.UI.CRYPTUI_WIZ_DIGITAL_SIGN_CONTEXT_head), use_last_error=False)(("CryptUIWizFreeDigitalSignContext", windll["CRYPTUI"]), ((1, 'pSignContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptUIDlgViewCertificateW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.Cryptography.UI.CRYPTUI_VIEWCERTIFICATE_STRUCTW_head),POINTER(win32more.Foundation.BOOL), use_last_error=True)(("CryptUIDlgViewCertificateW", windll["CRYPTUI"]), ((1, 'pCertViewInfo'),(1, 'pfPropertiesChanged'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptUIDlgViewCertificate():
    return win32more.Security.Cryptography.UI.CryptUIDlgViewCertificateW
def _define_CryptUIDlgViewCertificateA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.Cryptography.UI.CRYPTUI_VIEWCERTIFICATE_STRUCTA_head),POINTER(win32more.Foundation.BOOL), use_last_error=True)(("CryptUIDlgViewCertificateA", windll["CRYPTUI"]), ((1, 'pCertViewInfo'),(1, 'pfPropertiesChanged'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptUIWizExport():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.Cryptography.UI.CRYPTUI_WIZ_FLAGS,win32more.Foundation.HWND,win32more.Foundation.PWSTR,POINTER(win32more.Security.Cryptography.UI.CRYPTUI_WIZ_EXPORT_INFO_head),c_void_p, use_last_error=True)(("CryptUIWizExport", windll["CRYPTUI"]), ((1, 'dwFlags'),(1, 'hwndParent'),(1, 'pwszWizardTitle'),(1, 'pExportInfo'),(1, 'pvoid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptUIWizImport():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.Cryptography.UI.CRYPTUI_WIZ_FLAGS,win32more.Foundation.HWND,win32more.Foundation.PWSTR,POINTER(win32more.Security.Cryptography.UI.CRYPTUI_WIZ_IMPORT_SRC_INFO_head),c_void_p, use_last_error=True)(("CryptUIWizImport", windll["CRYPTUI"]), ((1, 'dwFlags'),(1, 'hwndParent'),(1, 'pwszWizardTitle'),(1, 'pImportSrc'),(1, 'hDestCertStore'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "CRYTPDLG_FLAGS_MASK",
    "CRYPTDLG_REVOCATION_DEFAULT",
    "CRYPTDLG_REVOCATION_ONLINE",
    "CRYPTDLG_REVOCATION_CACHE",
    "CRYPTDLG_REVOCATION_NONE",
    "CRYPTDLG_CACHE_ONLY_URL_RETRIEVAL",
    "CRYPTDLG_DISABLE_AIA",
    "CRYPTDLG_POLICY_MASK",
    "POLICY_IGNORE_NON_CRITICAL_BC",
    "CRYPTDLG_ACTION_MASK",
    "ACTION_REVOCATION_DEFAULT_ONLINE",
    "ACTION_REVOCATION_DEFAULT_CACHE",
    "CERT_DISPWELL_SELECT",
    "CERT_DISPWELL_TRUST_CA_CERT",
    "CERT_DISPWELL_TRUST_LEAF_CERT",
    "CERT_DISPWELL_TRUST_ADD_CA_CERT",
    "CERT_DISPWELL_TRUST_ADD_LEAF_CERT",
    "CERT_DISPWELL_DISTRUST_CA_CERT",
    "CERT_DISPWELL_DISTRUST_LEAF_CERT",
    "CERT_DISPWELL_DISTRUST_ADD_CA_CERT",
    "CERT_DISPWELL_DISTRUST_ADD_LEAF_CERT",
    "CSS_SELECTCERT_MASK",
    "SELCERT_PROPERTIES",
    "SELCERT_FINEPRINT",
    "SELCERT_CERTLIST",
    "SELCERT_ISSUED_TO",
    "SELCERT_VALIDITY",
    "SELCERT_ALGORITHM",
    "SELCERT_SERIAL_NUM",
    "SELCERT_THUMBPRINT",
    "CM_VIEWFLAGS_MASK",
    "CERTVIEW_CRYPTUI_LPARAM",
    "CERT_FILTER_OP_EXISTS",
    "CERT_FILTER_OP_NOT_EXISTS",
    "CERT_FILTER_OP_EQUALITY",
    "CERT_FILTER_INCLUDE_V1_CERTS",
    "CERT_FILTER_VALID_TIME_RANGE",
    "CERT_FILTER_VALID_SIGNATURE",
    "CERT_FILTER_LEAF_CERTS_ONLY",
    "CERT_FILTER_ISSUER_CERTS_ONLY",
    "CERT_FILTER_KEY_EXISTS",
    "CERT_VALIDITY_BEFORE_START",
    "CERT_VALIDITY_AFTER_END",
    "CERT_VALIDITY_SIGNATURE_FAILS",
    "CERT_VALIDITY_CERTIFICATE_REVOKED",
    "CERT_VALIDITY_KEY_USAGE_EXT_FAILURE",
    "CERT_VALIDITY_EXTENDED_USAGE_FAILURE",
    "CERT_VALIDITY_NAME_CONSTRAINTS_FAILURE",
    "CERT_VALIDITY_UNKNOWN_CRITICAL_EXTENSION",
    "CERT_VALIDITY_ISSUER_INVALID",
    "CERT_VALIDITY_OTHER_EXTENSION_FAILURE",
    "CERT_VALIDITY_PERIOD_NESTING_FAILURE",
    "CERT_VALIDITY_OTHER_ERROR",
    "CERT_VALIDITY_ISSUER_DISTRUST",
    "CERT_VALIDITY_EXPLICITLY_DISTRUSTED",
    "CERT_VALIDITY_NO_ISSUER_CERT_FOUND",
    "CERT_VALIDITY_NO_CRL_FOUND",
    "CERT_VALIDITY_CRL_OUT_OF_DATE",
    "CERT_VALIDITY_NO_TRUST_DATA",
    "CERT_VALIDITY_MASK_TRUST",
    "CERT_VALIDITY_MASK_VALIDITY",
    "CERT_TRUST_MASK",
    "CERT_TRUST_DO_FULL_SEARCH",
    "CERT_TRUST_PERMIT_MISSING_CRLS",
    "CERT_TRUST_DO_FULL_TRUST",
    "CERT_CREDENTIAL_PROVIDER_ID",
    "CRYPTUI_SELECT_ISSUEDTO_COLUMN",
    "CRYPTUI_SELECT_ISSUEDBY_COLUMN",
    "CRYPTUI_SELECT_INTENDEDUSE_COLUMN",
    "CRYPTUI_SELECT_FRIENDLYNAME_COLUMN",
    "CRYPTUI_SELECT_LOCATION_COLUMN",
    "CRYPTUI_SELECT_EXPIRATION_COLUMN",
    "CRYPTUI_CERT_MGR_TAB_MASK",
    "CRYPTUI_CERT_MGR_PUBLISHER_TAB",
    "CRYPTUI_CERT_MGR_SINGLE_TAB_FLAG",
    "CRYPTUI_WIZ_DIGITAL_SIGN_EXCLUDE_PAGE_HASHES",
    "CRYPTUI_WIZ_DIGITAL_SIGN_INCLUDE_PAGE_HASHES",
    "CRYPTUI_WIZ_EXPORT_FORMAT_SERIALIZED_CERT_STORE",
    "CRYPTUI_WIZ_FLAGS",
    "CRYPTUI_WIZ_NO_UI",
    "CRYPTUI_WIZ_IGNORE_NO_UI_FLAG_FOR_CSPS",
    "CRYPTUI_WIZ_NO_UI_EXCEPT_CSP",
    "CRYPTUI_WIZ_IMPORT_ALLOW_CERT",
    "CRYPTUI_WIZ_IMPORT_ALLOW_CRL",
    "CRYPTUI_WIZ_IMPORT_ALLOW_CTL",
    "CRYPTUI_WIZ_IMPORT_NO_CHANGE_DEST_STORE",
    "CRYPTUI_WIZ_IMPORT_TO_LOCALMACHINE",
    "CRYPTUI_WIZ_IMPORT_TO_CURRENTUSER",
    "CRYPTUI_WIZ_IMPORT_REMOTE_DEST_STORE",
    "CRYPTUI_WIZ_EXPORT_PRIVATE_KEY",
    "CRYPTUI_WIZ_EXPORT_NO_DELETE_PRIVATE_KEY",
    "CRYPTUI_VIEWCERTIFICATE_FLAGS",
    "CRYPTUI_HIDE_HIERARCHYPAGE",
    "CRYPTUI_HIDE_DETAILPAGE",
    "CRYPTUI_DISABLE_EDITPROPERTIES",
    "CRYPTUI_ENABLE_EDITPROPERTIES",
    "CRYPTUI_DISABLE_ADDTOSTORE",
    "CRYPTUI_ENABLE_ADDTOSTORE",
    "CRYPTUI_ACCEPT_DECLINE_STYLE",
    "CRYPTUI_IGNORE_UNTRUSTED_ROOT",
    "CRYPTUI_DONT_OPEN_STORES",
    "CRYPTUI_ONLY_OPEN_ROOT_STORE",
    "CRYPTUI_WARN_UNTRUSTED_ROOT",
    "CRYPTUI_ENABLE_REVOCATION_CHECKING",
    "CRYPTUI_WARN_REMOTE_TRUST",
    "CRYPTUI_DISABLE_EXPORT",
    "CRYPTUI_ENABLE_REVOCATION_CHECK_END_CERT",
    "CRYPTUI_ENABLE_REVOCATION_CHECK_CHAIN",
    "CRYPTUI_ENABLE_REVOCATION_CHECK_CHAIN_EXCLUDE_ROOT",
    "CRYPTUI_DISABLE_HTMLLINK",
    "CRYPTUI_DISABLE_ISSUERSTATEMENT",
    "CRYPTUI_CACHE_ONLY_URL_RETRIEVAL",
    "CERT_SELECT_STRUCT_FLAGS",
    "CSS_HIDE_PROPERTIES",
    "CSS_ENABLEHOOK",
    "CSS_ALLOWMULTISELECT",
    "CSS_SHOW_HELP",
    "CSS_ENABLETEMPLATE",
    "CSS_ENABLETEMPLATEHANDLE",
    "CRYPTUI_WIZ_IMPORT_SUBJECT_OPTION",
    "CRYPTUI_WIZ_IMPORT_SUBJECT_FILE",
    "CRYPTUI_WIZ_IMPORT_SUBJECT_CERT_CONTEXT",
    "CRYPTUI_WIZ_IMPORT_SUBJECT_CTL_CONTEXT",
    "CRYPTUI_WIZ_IMPORT_SUBJECT_CRL_CONTEXT",
    "CRYPTUI_WIZ_IMPORT_SUBJECT_CERT_STORE",
    "CRYPTUI_WIZ_DIGITAL_SIGN_SUBJECT",
    "CRYPTUI_WIZ_DIGITAL_SIGN_SUBJECT_BLOB",
    "CRYPTUI_WIZ_DIGITAL_SIGN_SUBJECT_FILE",
    "CRYPTUI_WIZ_DIGITAL_SIGN_SUBJECT_NONE",
    "CRYPTUI_WIZ_DIGITAL_SIGN",
    "CRYPTUI_WIZ_DIGITAL_SIGN_CERT",
    "CRYPTUI_WIZ_DIGITAL_SIGN_STORE",
    "CRYPTUI_WIZ_DIGITAL_SIGN_PVK",
    "CRYPTUI_WIZ_DIGITAL_SIGN_NONE",
    "CRYPTUI_WIZ_EXPORT_SUBJECT",
    "CRYPTUI_WIZ_EXPORT_CERT_CONTEXT",
    "CRYPTUI_WIZ_EXPORT_CTL_CONTEXT",
    "CRYPTUI_WIZ_EXPORT_CRL_CONTEXT",
    "CRYPTUI_WIZ_EXPORT_CERT_STORE",
    "CRYPTUI_WIZ_EXPORT_CERT_STORE_CERTIFICATES_ONLY",
    "CRYPTUI_WIZ_DIGITAL_SIGN_SIG_TYPE",
    "CRYPTUI_WIZ_DIGITAL_SIGN_COMMERCIAL",
    "CRYPTUI_WIZ_DIGITAL_SIGN_INDIVIDUAL",
    "CRYPTUI_WIZ_DIGITAL_SIGN_PVK_OPTION",
    "CRYPTUI_WIZ_DIGITAL_SIGN_PVK_FILE",
    "CRYPTUI_WIZ_DIGITAL_SIGN_PVK_PROV",
    "CERT_VIEWPROPERTIES_STRUCT_FLAGS",
    "CM_ENABLEHOOK",
    "CM_SHOW_HELP",
    "CM_SHOW_HELPICON",
    "CM_ENABLETEMPLATE",
    "CM_HIDE_ADVANCEPAGE",
    "CM_HIDE_TRUSTPAGE",
    "CM_NO_NAMECHANGE",
    "CM_NO_EDITTRUST",
    "CM_HIDE_DETAILPAGE",
    "CM_ADD_CERT_STORES",
    "CRYPTUI_WIZ_EXPORT_FORMAT",
    "CRYPTUI_WIZ_EXPORT_FORMAT_DER",
    "CRYPTUI_WIZ_EXPORT_FORMAT_PFX",
    "CRYPTUI_WIZ_EXPORT_FORMAT_PKCS7",
    "CRYPTUI_WIZ_EXPORT_FORMAT_BASE64",
    "CRYPTUI_WIZ_EXPORT_FORMAT_CRL",
    "CRYPTUI_WIZ_EXPORT_FORMAT_CTL",
    "CRYPTUI_WIZ_DIGITAL_ADDITIONAL_CERT_CHOICE",
    "CRYPTUI_WIZ_DIGITAL_SIGN_ADD_CHAIN",
    "CRYPTUI_WIZ_DIGITAL_SIGN_ADD_CHAIN_NO_ROOT",
    "CRYPTUI_WIZ_DIGITAL_SIGN_ADD_NONE",
    "CTL_MODIFY_REQUEST_OPERATION",
    "CTL_MODIFY_REQUEST_ADD_TRUSTED",
    "CTL_MODIFY_REQUEST_ADD_NOT_TRUSTED",
    "CTL_MODIFY_REQUEST_REMOVE",
    "PFNCMFILTERPROC",
    "PFNCMHOOKPROC",
    "CERT_SELECT_STRUCT_A",
    "CERT_SELECT_STRUCT_W",
    "CERT_VIEWPROPERTIES_STRUCT_A",
    "CERT_VIEWPROPERTIES_STRUCT_W",
    "CMOID",
    "CMFLTR",
    "PFNTRUSTHELPER",
    "CERT_VERIFY_CERTIFICATE_TRUST",
    "CTL_MODIFY_REQUEST",
    "PFNCFILTERPROC",
    "CERT_SELECTUI_INPUT",
    "CRYPTUI_CERT_MGR_STRUCT",
    "CRYPTUI_WIZ_DIGITAL_SIGN_BLOB_INFO",
    "CRYPTUI_WIZ_DIGITAL_SIGN_STORE_INFO",
    "CRYPTUI_WIZ_DIGITAL_SIGN_PVK_FILE_INFO",
    "CRYPTUI_WIZ_DIGITAL_SIGN_CERT_PVK_INFO",
    "CRYPTUI_WIZ_DIGITAL_SIGN_EXTENDED_INFO",
    "CRYPTUI_WIZ_DIGITAL_SIGN_INFO",
    "CRYPTUI_WIZ_DIGITAL_SIGN_CONTEXT",
    "CRYPTUI_INITDIALOG_STRUCT",
    "CRYPTUI_VIEWCERTIFICATE_STRUCTW",
    "CRYPTUI_VIEWCERTIFICATE_STRUCTA",
    "CRYPTUI_WIZ_EXPORT_INFO",
    "CRYPTUI_WIZ_EXPORT_CERTCONTEXT_INFO",
    "CRYPTUI_WIZ_IMPORT_SRC_INFO",
    "CryptUIDlgViewContext",
    "CryptUIDlgSelectCertificateFromStore",
    "CertSelectionGetSerializedBlob",
    "CryptUIDlgCertMgr",
    "CryptUIWizDigitalSign",
    "CryptUIWizFreeDigitalSignContext",
    "CryptUIDlgViewCertificateW",
    "CryptUIDlgViewCertificate",
    "CryptUIDlgViewCertificateA",
    "CryptUIWizExport",
    "CryptUIWizImport",
]
