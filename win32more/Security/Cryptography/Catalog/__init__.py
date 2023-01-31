from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Security.Cryptography
import win32more.Security.Cryptography.Catalog
import win32more.Security.Cryptography.Sip
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
szOID_CATALOG_LIST: String = '1.3.6.1.4.1.311.12.1.1'
szOID_CATALOG_LIST_MEMBER: String = '1.3.6.1.4.1.311.12.1.2'
szOID_CATALOG_LIST_MEMBER2: String = '1.3.6.1.4.1.311.12.1.3'
CRYPTCAT_FILEEXT: String = 'CAT'
CRYPTCAT_MAX_MEMBERTAG: UInt32 = 64
CRYPTCAT_MEMBER_SORTED: UInt32 = 1073741824
CRYPTCAT_ATTR_AUTHENTICATED: UInt32 = 268435456
CRYPTCAT_ATTR_UNAUTHENTICATED: UInt32 = 536870912
CRYPTCAT_ATTR_NAMEASCII: UInt32 = 1
CRYPTCAT_ATTR_NAMEOBJID: UInt32 = 2
CRYPTCAT_ATTR_DATAASCII: UInt32 = 65536
CRYPTCAT_ATTR_DATABASE64: UInt32 = 131072
CRYPTCAT_ATTR_DATAREPLACE: UInt32 = 262144
CRYPTCAT_ATTR_NO_AUTO_COMPAT_ENTRY: UInt32 = 16777216
CRYPTCAT_E_AREA_HEADER: UInt32 = 0
CRYPTCAT_E_AREA_MEMBER: UInt32 = 65536
CRYPTCAT_E_AREA_ATTRIBUTE: UInt32 = 131072
CRYPTCAT_E_CDF_UNSUPPORTED: UInt32 = 1
CRYPTCAT_E_CDF_DUPLICATE: UInt32 = 2
CRYPTCAT_E_CDF_TAGNOTFOUND: UInt32 = 4
CRYPTCAT_E_CDF_MEMBER_FILE_PATH: UInt32 = 65537
CRYPTCAT_E_CDF_MEMBER_INDIRECTDATA: UInt32 = 65538
CRYPTCAT_E_CDF_MEMBER_FILENOTFOUND: UInt32 = 65540
CRYPTCAT_E_CDF_BAD_GUID_CONV: UInt32 = 131073
CRYPTCAT_E_CDF_ATTR_TOOFEWVALUES: UInt32 = 131074
CRYPTCAT_E_CDF_ATTR_TYPECOMBO: UInt32 = 131076
CRYPTCAT_ADDCATALOG_NONE: UInt32 = 0
CRYPTCAT_ADDCATALOG_HARDLINK: UInt32 = 1
@winfunctype('WINTRUST.dll')
def CryptCATOpen(pwszFileName: win32more.Foundation.PWSTR, fdwOpenFlags: win32more.Security.Cryptography.Catalog.CRYPTCAT_OPEN_FLAGS, hProv: UIntPtr, dwPublicVersion: win32more.Security.Cryptography.Catalog.CRYPTCAT_VERSION, dwEncodingType: UInt32) -> win32more.Foundation.HANDLE: ...
@winfunctype('WINTRUST.dll')
def CryptCATClose(hCatalog: win32more.Foundation.HANDLE) -> win32more.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptCATStoreFromHandle(hCatalog: win32more.Foundation.HANDLE) -> POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATSTORE_head): ...
@winfunctype('WINTRUST.dll')
def CryptCATHandleFromStore(pCatStore: POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATSTORE_head)) -> win32more.Foundation.HANDLE: ...
@winfunctype('WINTRUST.dll')
def CryptCATPersistStore(hCatalog: win32more.Foundation.HANDLE) -> win32more.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptCATGetCatAttrInfo(hCatalog: win32more.Foundation.HANDLE, pwszReferenceTag: win32more.Foundation.PWSTR) -> POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE_head): ...
@winfunctype('WINTRUST.dll')
def CryptCATPutCatAttrInfo(hCatalog: win32more.Foundation.HANDLE, pwszReferenceTag: win32more.Foundation.PWSTR, dwAttrTypeAndAction: UInt32, cbData: UInt32, pbData: c_char_p_no) -> POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE_head): ...
@winfunctype('WINTRUST.dll')
def CryptCATEnumerateCatAttr(hCatalog: win32more.Foundation.HANDLE, pPrevAttr: POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE_head)) -> POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE_head): ...
@winfunctype('WINTRUST.dll')
def CryptCATGetMemberInfo(hCatalog: win32more.Foundation.HANDLE, pwszReferenceTag: win32more.Foundation.PWSTR) -> POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATMEMBER_head): ...
@winfunctype('WINTRUST.dll')
def CryptCATAllocSortedMemberInfo(hCatalog: win32more.Foundation.HANDLE, pwszReferenceTag: win32more.Foundation.PWSTR) -> POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATMEMBER_head): ...
@winfunctype('WINTRUST.dll')
def CryptCATFreeSortedMemberInfo(hCatalog: win32more.Foundation.HANDLE, pCatMember: POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATMEMBER_head)) -> Void: ...
@winfunctype('WINTRUST.dll')
def CryptCATGetAttrInfo(hCatalog: win32more.Foundation.HANDLE, pCatMember: POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATMEMBER_head), pwszReferenceTag: win32more.Foundation.PWSTR) -> POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE_head): ...
@winfunctype('WINTRUST.dll')
def CryptCATPutMemberInfo(hCatalog: win32more.Foundation.HANDLE, pwszFileName: win32more.Foundation.PWSTR, pwszReferenceTag: win32more.Foundation.PWSTR, pgSubjectType: POINTER(Guid), dwCertVersion: UInt32, cbSIPIndirectData: UInt32, pbSIPIndirectData: c_char_p_no) -> POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATMEMBER_head): ...
@winfunctype('WINTRUST.dll')
def CryptCATPutAttrInfo(hCatalog: win32more.Foundation.HANDLE, pCatMember: POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATMEMBER_head), pwszReferenceTag: win32more.Foundation.PWSTR, dwAttrTypeAndAction: UInt32, cbData: UInt32, pbData: c_char_p_no) -> POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE_head): ...
@winfunctype('WINTRUST.dll')
def CryptCATEnumerateMember(hCatalog: win32more.Foundation.HANDLE, pPrevMember: POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATMEMBER_head)) -> POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATMEMBER_head): ...
@winfunctype('WINTRUST.dll')
def CryptCATEnumerateAttr(hCatalog: win32more.Foundation.HANDLE, pCatMember: POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATMEMBER_head), pPrevAttr: POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE_head)) -> POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE_head): ...
@winfunctype('WINTRUST.dll')
def CryptCATCDFOpen(pwszFilePath: win32more.Foundation.PWSTR, pfnParseError: win32more.Security.Cryptography.Catalog.PFN_CDF_PARSE_ERROR_CALLBACK) -> POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATCDF_head): ...
@winfunctype('WINTRUST.dll')
def CryptCATCDFClose(pCDF: POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATCDF_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptCATCDFEnumCatAttributes(pCDF: POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATCDF_head), pPrevAttr: POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE_head), pfnParseError: win32more.Security.Cryptography.Catalog.PFN_CDF_PARSE_ERROR_CALLBACK) -> POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE_head): ...
@winfunctype('WINTRUST.dll')
def CryptCATCDFEnumMembers(pCDF: POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATCDF_head), pPrevMember: POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATMEMBER_head), pfnParseError: win32more.Security.Cryptography.Catalog.PFN_CDF_PARSE_ERROR_CALLBACK) -> POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATMEMBER_head): ...
@winfunctype('WINTRUST.dll')
def CryptCATCDFEnumAttributes(pCDF: POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATCDF_head), pMember: POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATMEMBER_head), pPrevAttr: POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE_head), pfnParseError: win32more.Security.Cryptography.Catalog.PFN_CDF_PARSE_ERROR_CALLBACK) -> POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE_head): ...
@winfunctype('WINTRUST.dll')
def IsCatalogFile(hFile: win32more.Foundation.HANDLE, pwszFileName: win32more.Foundation.PWSTR) -> win32more.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptCATAdminAcquireContext(phCatAdmin: POINTER(IntPtr), pgSubsystem: POINTER(Guid), dwFlags: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptCATAdminAcquireContext2(phCatAdmin: POINTER(IntPtr), pgSubsystem: POINTER(Guid), pwszHashAlgorithm: win32more.Foundation.PWSTR, pStrongHashPolicy: POINTER(win32more.Security.Cryptography.CERT_STRONG_SIGN_PARA_head), dwFlags: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptCATAdminReleaseContext(hCatAdmin: IntPtr, dwFlags: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptCATAdminReleaseCatalogContext(hCatAdmin: IntPtr, hCatInfo: IntPtr, dwFlags: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptCATAdminEnumCatalogFromHash(hCatAdmin: IntPtr, pbHash: c_char_p_no, cbHash: UInt32, dwFlags: UInt32, phPrevCatInfo: POINTER(IntPtr)) -> IntPtr: ...
@winfunctype('WINTRUST.dll')
def CryptCATAdminCalcHashFromFileHandle(hFile: win32more.Foundation.HANDLE, pcbHash: POINTER(UInt32), pbHash: c_char_p_no, dwFlags: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptCATAdminCalcHashFromFileHandle2(hCatAdmin: IntPtr, hFile: win32more.Foundation.HANDLE, pcbHash: POINTER(UInt32), pbHash: c_char_p_no, dwFlags: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptCATAdminAddCatalog(hCatAdmin: IntPtr, pwszCatalogFile: win32more.Foundation.PWSTR, pwszSelectBaseName: win32more.Foundation.PWSTR, dwFlags: UInt32) -> IntPtr: ...
@winfunctype('WINTRUST.dll')
def CryptCATAdminRemoveCatalog(hCatAdmin: IntPtr, pwszCatalogFile: win32more.Foundation.PWSTR, dwFlags: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptCATCatalogInfoFromContext(hCatInfo: IntPtr, psCatInfo: POINTER(win32more.Security.Cryptography.Catalog.CATALOG_INFO_head), dwFlags: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptCATAdminResolveCatalogPath(hCatAdmin: IntPtr, pwszCatalogFile: win32more.Foundation.PWSTR, psCatInfo: POINTER(win32more.Security.Cryptography.Catalog.CATALOG_INFO_head), dwFlags: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptCATAdminPauseServiceForBackup(dwFlags: UInt32, fResume: win32more.Foundation.BOOL) -> win32more.Foundation.BOOL: ...
class CATALOG_INFO(Structure):
    cbStruct: UInt32
    wszCatalogFile: Char * 260
class CRYPTCATATTRIBUTE(Structure):
    cbStruct: UInt32
    pwszReferenceTag: win32more.Foundation.PWSTR
    dwAttrTypeAndAction: UInt32
    cbValue: UInt32
    pbValue: c_char_p_no
    dwReserved: UInt32
class CRYPTCATCDF(Structure):
    cbStruct: UInt32
    hFile: win32more.Foundation.HANDLE
    dwCurFilePos: UInt32
    dwLastMemberOffset: UInt32
    fEOF: win32more.Foundation.BOOL
    pwszResultDir: win32more.Foundation.PWSTR
    hCATStore: win32more.Foundation.HANDLE
class CRYPTCATMEMBER(Structure):
    cbStruct: UInt32
    pwszReferenceTag: win32more.Foundation.PWSTR
    pwszFileName: win32more.Foundation.PWSTR
    gSubjectType: Guid
    fdwMemberFlags: UInt32
    pIndirectData: POINTER(win32more.Security.Cryptography.Sip.SIP_INDIRECT_DATA_head)
    dwCertVersion: UInt32
    dwReserved: UInt32
    hReserved: win32more.Foundation.HANDLE
    sEncodedIndirectData: win32more.Security.Cryptography.CRYPT_INTEGER_BLOB
    sEncodedMemberInfo: win32more.Security.Cryptography.CRYPT_INTEGER_BLOB
class CRYPTCATSTORE(Structure):
    cbStruct: UInt32
    dwPublicVersion: UInt32
    pwszP7File: win32more.Foundation.PWSTR
    hProv: UIntPtr
    dwEncodingType: UInt32
    fdwStoreFlags: win32more.Security.Cryptography.Catalog.CRYPTCAT_OPEN_FLAGS
    hReserved: win32more.Foundation.HANDLE
    hAttrs: win32more.Foundation.HANDLE
    hCryptMsg: c_void_p
    hSorted: win32more.Foundation.HANDLE
CRYPTCAT_OPEN_FLAGS = UInt32
CRYPTCAT_OPEN_ALWAYS: CRYPTCAT_OPEN_FLAGS = 2
CRYPTCAT_OPEN_CREATENEW: CRYPTCAT_OPEN_FLAGS = 1
CRYPTCAT_OPEN_EXISTING: CRYPTCAT_OPEN_FLAGS = 4
CRYPTCAT_OPEN_EXCLUDE_PAGE_HASHES: CRYPTCAT_OPEN_FLAGS = 65536
CRYPTCAT_OPEN_INCLUDE_PAGE_HASHES: CRYPTCAT_OPEN_FLAGS = 131072
CRYPTCAT_OPEN_VERIFYSIGHASH: CRYPTCAT_OPEN_FLAGS = 268435456
CRYPTCAT_OPEN_NO_CONTENT_HCRYPTMSG: CRYPTCAT_OPEN_FLAGS = 536870912
CRYPTCAT_OPEN_SORTED: CRYPTCAT_OPEN_FLAGS = 1073741824
CRYPTCAT_OPEN_FLAGS_MASK: CRYPTCAT_OPEN_FLAGS = 4294901760
CRYPTCAT_VERSION = UInt32
CRYPTCAT_VERSION_1: CRYPTCAT_VERSION = 256
CRYPTCAT_VERSION_2: CRYPTCAT_VERSION = 512
class MS_ADDINFO_CATALOGMEMBER(Structure):
    cbStruct: UInt32
    pStore: POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATSTORE_head)
    pMember: POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATMEMBER_head)
@winfunctype_pointer
def PFN_CDF_PARSE_ERROR_CALLBACK(dwErrorArea: UInt32, dwLocalError: UInt32, pwszLine: win32more.Foundation.PWSTR) -> Void: ...
make_head(_module, 'CATALOG_INFO')
make_head(_module, 'CRYPTCATATTRIBUTE')
make_head(_module, 'CRYPTCATCDF')
make_head(_module, 'CRYPTCATMEMBER')
make_head(_module, 'CRYPTCATSTORE')
make_head(_module, 'MS_ADDINFO_CATALOGMEMBER')
make_head(_module, 'PFN_CDF_PARSE_ERROR_CALLBACK')
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
_arch_optional = [
]
