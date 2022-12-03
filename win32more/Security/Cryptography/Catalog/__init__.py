from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Security.Cryptography
import win32more.Security.Cryptography.Catalog
import win32more.Security.Cryptography.Sip
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f'_define_{name}']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
szOID_CATALOG_LIST = '1.3.6.1.4.1.311.12.1.1'
szOID_CATALOG_LIST_MEMBER = '1.3.6.1.4.1.311.12.1.2'
szOID_CATALOG_LIST_MEMBER2 = '1.3.6.1.4.1.311.12.1.3'
CRYPTCAT_FILEEXT = 'CAT'
CRYPTCAT_MAX_MEMBERTAG = 64
CRYPTCAT_MEMBER_SORTED = 1073741824
CRYPTCAT_ATTR_AUTHENTICATED = 268435456
CRYPTCAT_ATTR_UNAUTHENTICATED = 536870912
CRYPTCAT_ATTR_NAMEASCII = 1
CRYPTCAT_ATTR_NAMEOBJID = 2
CRYPTCAT_ATTR_DATAASCII = 65536
CRYPTCAT_ATTR_DATABASE64 = 131072
CRYPTCAT_ATTR_DATAREPLACE = 262144
CRYPTCAT_ATTR_NO_AUTO_COMPAT_ENTRY = 16777216
CRYPTCAT_E_AREA_HEADER = 0
CRYPTCAT_E_AREA_MEMBER = 65536
CRYPTCAT_E_AREA_ATTRIBUTE = 131072
CRYPTCAT_E_CDF_UNSUPPORTED = 1
CRYPTCAT_E_CDF_DUPLICATE = 2
CRYPTCAT_E_CDF_TAGNOTFOUND = 4
CRYPTCAT_E_CDF_MEMBER_FILE_PATH = 65537
CRYPTCAT_E_CDF_MEMBER_INDIRECTDATA = 65538
CRYPTCAT_E_CDF_MEMBER_FILENOTFOUND = 65540
CRYPTCAT_E_CDF_BAD_GUID_CONV = 131073
CRYPTCAT_E_CDF_ATTR_TOOFEWVALUES = 131074
CRYPTCAT_E_CDF_ATTR_TYPECOMBO = 131076
CRYPTCAT_ADDCATALOG_NONE = 0
CRYPTCAT_ADDCATALOG_HARDLINK = 1
def _define_CryptCATOpen():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,win32more.Security.Cryptography.Catalog.CRYPTCAT_OPEN_FLAGS,UIntPtr,win32more.Security.Cryptography.Catalog.CRYPTCAT_VERSION,UInt32)(('CryptCATOpen', windll['WINTRUST.dll']), ((1, 'pwszFileName'),(1, 'fdwOpenFlags'),(1, 'hProv'),(1, 'dwPublicVersion'),(1, 'dwEncodingType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptCATClose():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE)(('CryptCATClose', windll['WINTRUST.dll']), ((1, 'hCatalog'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptCATStoreFromHandle():
    try:
        return WINFUNCTYPE(POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATSTORE_head),win32more.Foundation.HANDLE)(('CryptCATStoreFromHandle', windll['WINTRUST.dll']), ((1, 'hCatalog'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptCATHandleFromStore():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATSTORE_head))(('CryptCATHandleFromStore', windll['WINTRUST.dll']), ((1, 'pCatStore'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptCATPersistStore():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE)(('CryptCATPersistStore', windll['WINTRUST.dll']), ((1, 'hCatalog'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptCATGetCatAttrInfo():
    try:
        return WINFUNCTYPE(POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE_head),win32more.Foundation.HANDLE,win32more.Foundation.PWSTR)(('CryptCATGetCatAttrInfo', windll['WINTRUST.dll']), ((1, 'hCatalog'),(1, 'pwszReferenceTag'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptCATPutCatAttrInfo():
    try:
        return WINFUNCTYPE(POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE_head),win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,UInt32,UInt32,c_char_p_no)(('CryptCATPutCatAttrInfo', windll['WINTRUST.dll']), ((1, 'hCatalog'),(1, 'pwszReferenceTag'),(1, 'dwAttrTypeAndAction'),(1, 'cbData'),(1, 'pbData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptCATEnumerateCatAttr():
    try:
        return WINFUNCTYPE(POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE_head),win32more.Foundation.HANDLE,POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE_head))(('CryptCATEnumerateCatAttr', windll['WINTRUST.dll']), ((1, 'hCatalog'),(1, 'pPrevAttr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptCATGetMemberInfo():
    try:
        return WINFUNCTYPE(POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATMEMBER_head),win32more.Foundation.HANDLE,win32more.Foundation.PWSTR)(('CryptCATGetMemberInfo', windll['WINTRUST.dll']), ((1, 'hCatalog'),(1, 'pwszReferenceTag'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptCATAllocSortedMemberInfo():
    try:
        return WINFUNCTYPE(POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATMEMBER_head),win32more.Foundation.HANDLE,win32more.Foundation.PWSTR)(('CryptCATAllocSortedMemberInfo', windll['WINTRUST.dll']), ((1, 'hCatalog'),(1, 'pwszReferenceTag'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptCATFreeSortedMemberInfo():
    try:
        return WINFUNCTYPE(Void,win32more.Foundation.HANDLE,POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATMEMBER_head))(('CryptCATFreeSortedMemberInfo', windll['WINTRUST.dll']), ((1, 'hCatalog'),(1, 'pCatMember'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptCATGetAttrInfo():
    try:
        return WINFUNCTYPE(POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE_head),win32more.Foundation.HANDLE,POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATMEMBER_head),win32more.Foundation.PWSTR)(('CryptCATGetAttrInfo', windll['WINTRUST.dll']), ((1, 'hCatalog'),(1, 'pCatMember'),(1, 'pwszReferenceTag'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptCATPutMemberInfo():
    try:
        return WINFUNCTYPE(POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATMEMBER_head),win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(Guid),UInt32,UInt32,c_char_p_no)(('CryptCATPutMemberInfo', windll['WINTRUST.dll']), ((1, 'hCatalog'),(1, 'pwszFileName'),(1, 'pwszReferenceTag'),(1, 'pgSubjectType'),(1, 'dwCertVersion'),(1, 'cbSIPIndirectData'),(1, 'pbSIPIndirectData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptCATPutAttrInfo():
    try:
        return WINFUNCTYPE(POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE_head),win32more.Foundation.HANDLE,POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATMEMBER_head),win32more.Foundation.PWSTR,UInt32,UInt32,c_char_p_no)(('CryptCATPutAttrInfo', windll['WINTRUST.dll']), ((1, 'hCatalog'),(1, 'pCatMember'),(1, 'pwszReferenceTag'),(1, 'dwAttrTypeAndAction'),(1, 'cbData'),(1, 'pbData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptCATEnumerateMember():
    try:
        return WINFUNCTYPE(POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATMEMBER_head),win32more.Foundation.HANDLE,POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATMEMBER_head))(('CryptCATEnumerateMember', windll['WINTRUST.dll']), ((1, 'hCatalog'),(1, 'pPrevMember'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptCATEnumerateAttr():
    try:
        return WINFUNCTYPE(POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE_head),win32more.Foundation.HANDLE,POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATMEMBER_head),POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE_head))(('CryptCATEnumerateAttr', windll['WINTRUST.dll']), ((1, 'hCatalog'),(1, 'pCatMember'),(1, 'pPrevAttr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptCATCDFOpen():
    try:
        return WINFUNCTYPE(POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATCDF_head),win32more.Foundation.PWSTR,win32more.Security.Cryptography.Catalog.PFN_CDF_PARSE_ERROR_CALLBACK)(('CryptCATCDFOpen', windll['WINTRUST.dll']), ((1, 'pwszFilePath'),(1, 'pfnParseError'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptCATCDFClose():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATCDF_head))(('CryptCATCDFClose', windll['WINTRUST.dll']), ((1, 'pCDF'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptCATCDFEnumCatAttributes():
    try:
        return WINFUNCTYPE(POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE_head),POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATCDF_head),POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE_head),win32more.Security.Cryptography.Catalog.PFN_CDF_PARSE_ERROR_CALLBACK)(('CryptCATCDFEnumCatAttributes', windll['WINTRUST.dll']), ((1, 'pCDF'),(1, 'pPrevAttr'),(1, 'pfnParseError'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptCATCDFEnumMembers():
    try:
        return WINFUNCTYPE(POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATMEMBER_head),POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATCDF_head),POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATMEMBER_head),win32more.Security.Cryptography.Catalog.PFN_CDF_PARSE_ERROR_CALLBACK)(('CryptCATCDFEnumMembers', windll['WINTRUST.dll']), ((1, 'pCDF'),(1, 'pPrevMember'),(1, 'pfnParseError'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptCATCDFEnumAttributes():
    try:
        return WINFUNCTYPE(POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE_head),POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATCDF_head),POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATMEMBER_head),POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE_head),win32more.Security.Cryptography.Catalog.PFN_CDF_PARSE_ERROR_CALLBACK)(('CryptCATCDFEnumAttributes', windll['WINTRUST.dll']), ((1, 'pCDF'),(1, 'pMember'),(1, 'pPrevAttr'),(1, 'pfnParseError'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsCatalogFile():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR)(('IsCatalogFile', windll['WINTRUST.dll']), ((1, 'hFile'),(1, 'pwszFileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptCATAdminAcquireContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(IntPtr),POINTER(Guid),UInt32)(('CryptCATAdminAcquireContext', windll['WINTRUST.dll']), ((1, 'phCatAdmin'),(1, 'pgSubsystem'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptCATAdminAcquireContext2():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(IntPtr),POINTER(Guid),win32more.Foundation.PWSTR,POINTER(win32more.Security.Cryptography.CERT_STRONG_SIGN_PARA_head),UInt32)(('CryptCATAdminAcquireContext2', windll['WINTRUST.dll']), ((1, 'phCatAdmin'),(1, 'pgSubsystem'),(1, 'pwszHashAlgorithm'),(1, 'pStrongHashPolicy'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptCATAdminReleaseContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,UInt32)(('CryptCATAdminReleaseContext', windll['WINTRUST.dll']), ((1, 'hCatAdmin'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptCATAdminReleaseCatalogContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,IntPtr,UInt32)(('CryptCATAdminReleaseCatalogContext', windll['WINTRUST.dll']), ((1, 'hCatAdmin'),(1, 'hCatInfo'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptCATAdminEnumCatalogFromHash():
    try:
        return WINFUNCTYPE(IntPtr,IntPtr,c_char_p_no,UInt32,UInt32,POINTER(IntPtr))(('CryptCATAdminEnumCatalogFromHash', windll['WINTRUST.dll']), ((1, 'hCatAdmin'),(1, 'pbHash'),(1, 'cbHash'),(1, 'dwFlags'),(1, 'phPrevCatInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptCATAdminCalcHashFromFileHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(UInt32),c_char_p_no,UInt32)(('CryptCATAdminCalcHashFromFileHandle', windll['WINTRUST.dll']), ((1, 'hFile'),(1, 'pcbHash'),(1, 'pbHash'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptCATAdminCalcHashFromFileHandle2():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,win32more.Foundation.HANDLE,POINTER(UInt32),c_char_p_no,UInt32)(('CryptCATAdminCalcHashFromFileHandle2', windll['WINTRUST.dll']), ((1, 'hCatAdmin'),(1, 'hFile'),(1, 'pcbHash'),(1, 'pbHash'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptCATAdminAddCatalog():
    try:
        return WINFUNCTYPE(IntPtr,IntPtr,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32)(('CryptCATAdminAddCatalog', windll['WINTRUST.dll']), ((1, 'hCatAdmin'),(1, 'pwszCatalogFile'),(1, 'pwszSelectBaseName'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptCATAdminRemoveCatalog():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,win32more.Foundation.PWSTR,UInt32)(('CryptCATAdminRemoveCatalog', windll['WINTRUST.dll']), ((1, 'hCatAdmin'),(1, 'pwszCatalogFile'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptCATCatalogInfoFromContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,POINTER(win32more.Security.Cryptography.Catalog.CATALOG_INFO_head),UInt32)(('CryptCATCatalogInfoFromContext', windll['WINTRUST.dll']), ((1, 'hCatInfo'),(1, 'psCatInfo'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptCATAdminResolveCatalogPath():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,win32more.Foundation.PWSTR,POINTER(win32more.Security.Cryptography.Catalog.CATALOG_INFO_head),UInt32)(('CryptCATAdminResolveCatalogPath', windll['WINTRUST.dll']), ((1, 'hCatAdmin'),(1, 'pwszCatalogFile'),(1, 'psCatInfo'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptCATAdminPauseServiceForBackup():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.Foundation.BOOL)(('CryptCATAdminPauseServiceForBackup', windll['WINTRUST.dll']), ((1, 'dwFlags'),(1, 'fResume'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CATALOG_INFO_head():
    class CATALOG_INFO(Structure):
        pass
    return CATALOG_INFO
def _define_CATALOG_INFO():
    CATALOG_INFO = win32more.Security.Cryptography.Catalog.CATALOG_INFO_head
    CATALOG_INFO._fields_ = [
        ('cbStruct', UInt32),
        ('wszCatalogFile', Char * 260),
    ]
    return CATALOG_INFO
CRYPTCAT_OPEN_FLAGS = UInt32
CRYPTCAT_OPEN_ALWAYS = 2
CRYPTCAT_OPEN_CREATENEW = 1
CRYPTCAT_OPEN_EXISTING = 4
CRYPTCAT_OPEN_EXCLUDE_PAGE_HASHES = 65536
CRYPTCAT_OPEN_INCLUDE_PAGE_HASHES = 131072
CRYPTCAT_OPEN_VERIFYSIGHASH = 268435456
CRYPTCAT_OPEN_NO_CONTENT_HCRYPTMSG = 536870912
CRYPTCAT_OPEN_SORTED = 1073741824
CRYPTCAT_OPEN_FLAGS_MASK = 4294901760
CRYPTCAT_VERSION = UInt32
CRYPTCAT_VERSION_1 = 256
CRYPTCAT_VERSION_2 = 512
def _define_CRYPTCATATTRIBUTE_head():
    class CRYPTCATATTRIBUTE(Structure):
        pass
    return CRYPTCATATTRIBUTE
def _define_CRYPTCATATTRIBUTE():
    CRYPTCATATTRIBUTE = win32more.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE_head
    CRYPTCATATTRIBUTE._fields_ = [
        ('cbStruct', UInt32),
        ('pwszReferenceTag', win32more.Foundation.PWSTR),
        ('dwAttrTypeAndAction', UInt32),
        ('cbValue', UInt32),
        ('pbValue', c_char_p_no),
        ('dwReserved', UInt32),
    ]
    return CRYPTCATATTRIBUTE
def _define_CRYPTCATCDF_head():
    class CRYPTCATCDF(Structure):
        pass
    return CRYPTCATCDF
def _define_CRYPTCATCDF():
    CRYPTCATCDF = win32more.Security.Cryptography.Catalog.CRYPTCATCDF_head
    CRYPTCATCDF._fields_ = [
        ('cbStruct', UInt32),
        ('hFile', win32more.Foundation.HANDLE),
        ('dwCurFilePos', UInt32),
        ('dwLastMemberOffset', UInt32),
        ('fEOF', win32more.Foundation.BOOL),
        ('pwszResultDir', win32more.Foundation.PWSTR),
        ('hCATStore', win32more.Foundation.HANDLE),
    ]
    return CRYPTCATCDF
def _define_CRYPTCATMEMBER_head():
    class CRYPTCATMEMBER(Structure):
        pass
    return CRYPTCATMEMBER
def _define_CRYPTCATMEMBER():
    CRYPTCATMEMBER = win32more.Security.Cryptography.Catalog.CRYPTCATMEMBER_head
    CRYPTCATMEMBER._fields_ = [
        ('cbStruct', UInt32),
        ('pwszReferenceTag', win32more.Foundation.PWSTR),
        ('pwszFileName', win32more.Foundation.PWSTR),
        ('gSubjectType', Guid),
        ('fdwMemberFlags', UInt32),
        ('pIndirectData', POINTER(win32more.Security.Cryptography.Sip.SIP_INDIRECT_DATA_head)),
        ('dwCertVersion', UInt32),
        ('dwReserved', UInt32),
        ('hReserved', win32more.Foundation.HANDLE),
        ('sEncodedIndirectData', win32more.Security.Cryptography.CRYPT_INTEGER_BLOB),
        ('sEncodedMemberInfo', win32more.Security.Cryptography.CRYPT_INTEGER_BLOB),
    ]
    return CRYPTCATMEMBER
def _define_CRYPTCATSTORE_head():
    class CRYPTCATSTORE(Structure):
        pass
    return CRYPTCATSTORE
def _define_CRYPTCATSTORE():
    CRYPTCATSTORE = win32more.Security.Cryptography.Catalog.CRYPTCATSTORE_head
    CRYPTCATSTORE._fields_ = [
        ('cbStruct', UInt32),
        ('dwPublicVersion', UInt32),
        ('pwszP7File', win32more.Foundation.PWSTR),
        ('hProv', UIntPtr),
        ('dwEncodingType', UInt32),
        ('fdwStoreFlags', win32more.Security.Cryptography.Catalog.CRYPTCAT_OPEN_FLAGS),
        ('hReserved', win32more.Foundation.HANDLE),
        ('hAttrs', win32more.Foundation.HANDLE),
        ('hCryptMsg', c_void_p),
        ('hSorted', win32more.Foundation.HANDLE),
    ]
    return CRYPTCATSTORE
def _define_MS_ADDINFO_CATALOGMEMBER_head():
    class MS_ADDINFO_CATALOGMEMBER(Structure):
        pass
    return MS_ADDINFO_CATALOGMEMBER
def _define_MS_ADDINFO_CATALOGMEMBER():
    MS_ADDINFO_CATALOGMEMBER = win32more.Security.Cryptography.Catalog.MS_ADDINFO_CATALOGMEMBER_head
    MS_ADDINFO_CATALOGMEMBER._fields_ = [
        ('cbStruct', UInt32),
        ('pStore', POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATSTORE_head)),
        ('pMember', POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATMEMBER_head)),
    ]
    return MS_ADDINFO_CATALOGMEMBER
def _define_PFN_CDF_PARSE_ERROR_CALLBACK():
    return WINFUNCTYPE(Void,UInt32,UInt32,win32more.Foundation.PWSTR)
__all__ = [
    "CATALOG_INFO",
    "CRYPTCATATTRIBUTE",
    "CRYPTCATCDF",
    "CRYPTCATMEMBER",
    "CRYPTCATSTORE",
    "CRYPTCAT_ADDCATALOG_HARDLINK",
    "CRYPTCAT_ADDCATALOG_NONE",
    "CRYPTCAT_ATTR_AUTHENTICATED",
    "CRYPTCAT_ATTR_DATAASCII",
    "CRYPTCAT_ATTR_DATABASE64",
    "CRYPTCAT_ATTR_DATAREPLACE",
    "CRYPTCAT_ATTR_NAMEASCII",
    "CRYPTCAT_ATTR_NAMEOBJID",
    "CRYPTCAT_ATTR_NO_AUTO_COMPAT_ENTRY",
    "CRYPTCAT_ATTR_UNAUTHENTICATED",
    "CRYPTCAT_E_AREA_ATTRIBUTE",
    "CRYPTCAT_E_AREA_HEADER",
    "CRYPTCAT_E_AREA_MEMBER",
    "CRYPTCAT_E_CDF_ATTR_TOOFEWVALUES",
    "CRYPTCAT_E_CDF_ATTR_TYPECOMBO",
    "CRYPTCAT_E_CDF_BAD_GUID_CONV",
    "CRYPTCAT_E_CDF_DUPLICATE",
    "CRYPTCAT_E_CDF_MEMBER_FILENOTFOUND",
    "CRYPTCAT_E_CDF_MEMBER_FILE_PATH",
    "CRYPTCAT_E_CDF_MEMBER_INDIRECTDATA",
    "CRYPTCAT_E_CDF_TAGNOTFOUND",
    "CRYPTCAT_E_CDF_UNSUPPORTED",
    "CRYPTCAT_FILEEXT",
    "CRYPTCAT_MAX_MEMBERTAG",
    "CRYPTCAT_MEMBER_SORTED",
    "CRYPTCAT_OPEN_ALWAYS",
    "CRYPTCAT_OPEN_CREATENEW",
    "CRYPTCAT_OPEN_EXCLUDE_PAGE_HASHES",
    "CRYPTCAT_OPEN_EXISTING",
    "CRYPTCAT_OPEN_FLAGS",
    "CRYPTCAT_OPEN_FLAGS_MASK",
    "CRYPTCAT_OPEN_INCLUDE_PAGE_HASHES",
    "CRYPTCAT_OPEN_NO_CONTENT_HCRYPTMSG",
    "CRYPTCAT_OPEN_SORTED",
    "CRYPTCAT_OPEN_VERIFYSIGHASH",
    "CRYPTCAT_VERSION",
    "CRYPTCAT_VERSION_1",
    "CRYPTCAT_VERSION_2",
    "CryptCATAdminAcquireContext",
    "CryptCATAdminAcquireContext2",
    "CryptCATAdminAddCatalog",
    "CryptCATAdminCalcHashFromFileHandle",
    "CryptCATAdminCalcHashFromFileHandle2",
    "CryptCATAdminEnumCatalogFromHash",
    "CryptCATAdminPauseServiceForBackup",
    "CryptCATAdminReleaseCatalogContext",
    "CryptCATAdminReleaseContext",
    "CryptCATAdminRemoveCatalog",
    "CryptCATAdminResolveCatalogPath",
    "CryptCATAllocSortedMemberInfo",
    "CryptCATCDFClose",
    "CryptCATCDFEnumAttributes",
    "CryptCATCDFEnumCatAttributes",
    "CryptCATCDFEnumMembers",
    "CryptCATCDFOpen",
    "CryptCATCatalogInfoFromContext",
    "CryptCATClose",
    "CryptCATEnumerateAttr",
    "CryptCATEnumerateCatAttr",
    "CryptCATEnumerateMember",
    "CryptCATFreeSortedMemberInfo",
    "CryptCATGetAttrInfo",
    "CryptCATGetCatAttrInfo",
    "CryptCATGetMemberInfo",
    "CryptCATHandleFromStore",
    "CryptCATOpen",
    "CryptCATPersistStore",
    "CryptCATPutAttrInfo",
    "CryptCATPutCatAttrInfo",
    "CryptCATPutMemberInfo",
    "CryptCATStoreFromHandle",
    "IsCatalogFile",
    "MS_ADDINFO_CATALOGMEMBER",
    "PFN_CDF_PARSE_ERROR_CALLBACK",
    "szOID_CATALOG_LIST",
    "szOID_CATALOG_LIST_MEMBER",
    "szOID_CATALOG_LIST_MEMBER2",
]
