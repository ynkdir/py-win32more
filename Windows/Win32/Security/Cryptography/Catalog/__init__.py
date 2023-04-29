from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.Security.Cryptography
import Windows.Win32.Security.Cryptography.Catalog
import Windows.Win32.Security.Cryptography.Sip
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
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
def CryptCATOpen(pwszFileName: Windows.Win32.Foundation.PWSTR, fdwOpenFlags: Windows.Win32.Security.Cryptography.Catalog.CRYPTCAT_OPEN_FLAGS, hProv: UIntPtr, dwPublicVersion: Windows.Win32.Security.Cryptography.Catalog.CRYPTCAT_VERSION, dwEncodingType: UInt32) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('WINTRUST.dll')
def CryptCATClose(hCatalog: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptCATStoreFromHandle(hCatalog: Windows.Win32.Foundation.HANDLE) -> POINTER(Windows.Win32.Security.Cryptography.Catalog.CRYPTCATSTORE_head): ...
@winfunctype('WINTRUST.dll')
def CryptCATHandleFromStore(pCatStore: POINTER(Windows.Win32.Security.Cryptography.Catalog.CRYPTCATSTORE_head)) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('WINTRUST.dll')
def CryptCATPersistStore(hCatalog: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptCATGetCatAttrInfo(hCatalog: Windows.Win32.Foundation.HANDLE, pwszReferenceTag: Windows.Win32.Foundation.PWSTR) -> POINTER(Windows.Win32.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE_head): ...
@winfunctype('WINTRUST.dll')
def CryptCATPutCatAttrInfo(hCatalog: Windows.Win32.Foundation.HANDLE, pwszReferenceTag: Windows.Win32.Foundation.PWSTR, dwAttrTypeAndAction: UInt32, cbData: UInt32, pbData: POINTER(Byte)) -> POINTER(Windows.Win32.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE_head): ...
@winfunctype('WINTRUST.dll')
def CryptCATEnumerateCatAttr(hCatalog: Windows.Win32.Foundation.HANDLE, pPrevAttr: POINTER(Windows.Win32.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE_head)) -> POINTER(Windows.Win32.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE_head): ...
@winfunctype('WINTRUST.dll')
def CryptCATGetMemberInfo(hCatalog: Windows.Win32.Foundation.HANDLE, pwszReferenceTag: Windows.Win32.Foundation.PWSTR) -> POINTER(Windows.Win32.Security.Cryptography.Catalog.CRYPTCATMEMBER_head): ...
@winfunctype('WINTRUST.dll')
def CryptCATAllocSortedMemberInfo(hCatalog: Windows.Win32.Foundation.HANDLE, pwszReferenceTag: Windows.Win32.Foundation.PWSTR) -> POINTER(Windows.Win32.Security.Cryptography.Catalog.CRYPTCATMEMBER_head): ...
@winfunctype('WINTRUST.dll')
def CryptCATFreeSortedMemberInfo(hCatalog: Windows.Win32.Foundation.HANDLE, pCatMember: POINTER(Windows.Win32.Security.Cryptography.Catalog.CRYPTCATMEMBER_head)) -> Void: ...
@winfunctype('WINTRUST.dll')
def CryptCATGetAttrInfo(hCatalog: Windows.Win32.Foundation.HANDLE, pCatMember: POINTER(Windows.Win32.Security.Cryptography.Catalog.CRYPTCATMEMBER_head), pwszReferenceTag: Windows.Win32.Foundation.PWSTR) -> POINTER(Windows.Win32.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE_head): ...
@winfunctype('WINTRUST.dll')
def CryptCATPutMemberInfo(hCatalog: Windows.Win32.Foundation.HANDLE, pwszFileName: Windows.Win32.Foundation.PWSTR, pwszReferenceTag: Windows.Win32.Foundation.PWSTR, pgSubjectType: POINTER(Guid), dwCertVersion: UInt32, cbSIPIndirectData: UInt32, pbSIPIndirectData: POINTER(Byte)) -> POINTER(Windows.Win32.Security.Cryptography.Catalog.CRYPTCATMEMBER_head): ...
@winfunctype('WINTRUST.dll')
def CryptCATPutAttrInfo(hCatalog: Windows.Win32.Foundation.HANDLE, pCatMember: POINTER(Windows.Win32.Security.Cryptography.Catalog.CRYPTCATMEMBER_head), pwszReferenceTag: Windows.Win32.Foundation.PWSTR, dwAttrTypeAndAction: UInt32, cbData: UInt32, pbData: POINTER(Byte)) -> POINTER(Windows.Win32.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE_head): ...
@winfunctype('WINTRUST.dll')
def CryptCATEnumerateMember(hCatalog: Windows.Win32.Foundation.HANDLE, pPrevMember: POINTER(Windows.Win32.Security.Cryptography.Catalog.CRYPTCATMEMBER_head)) -> POINTER(Windows.Win32.Security.Cryptography.Catalog.CRYPTCATMEMBER_head): ...
@winfunctype('WINTRUST.dll')
def CryptCATEnumerateAttr(hCatalog: Windows.Win32.Foundation.HANDLE, pCatMember: POINTER(Windows.Win32.Security.Cryptography.Catalog.CRYPTCATMEMBER_head), pPrevAttr: POINTER(Windows.Win32.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE_head)) -> POINTER(Windows.Win32.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE_head): ...
@winfunctype('WINTRUST.dll')
def CryptCATCDFOpen(pwszFilePath: Windows.Win32.Foundation.PWSTR, pfnParseError: Windows.Win32.Security.Cryptography.Catalog.PFN_CDF_PARSE_ERROR_CALLBACK) -> POINTER(Windows.Win32.Security.Cryptography.Catalog.CRYPTCATCDF_head): ...
@winfunctype('WINTRUST.dll')
def CryptCATCDFClose(pCDF: POINTER(Windows.Win32.Security.Cryptography.Catalog.CRYPTCATCDF_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptCATCDFEnumCatAttributes(pCDF: POINTER(Windows.Win32.Security.Cryptography.Catalog.CRYPTCATCDF_head), pPrevAttr: POINTER(Windows.Win32.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE_head), pfnParseError: Windows.Win32.Security.Cryptography.Catalog.PFN_CDF_PARSE_ERROR_CALLBACK) -> POINTER(Windows.Win32.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE_head): ...
@winfunctype('WINTRUST.dll')
def CryptCATCDFEnumMembers(pCDF: POINTER(Windows.Win32.Security.Cryptography.Catalog.CRYPTCATCDF_head), pPrevMember: POINTER(Windows.Win32.Security.Cryptography.Catalog.CRYPTCATMEMBER_head), pfnParseError: Windows.Win32.Security.Cryptography.Catalog.PFN_CDF_PARSE_ERROR_CALLBACK) -> POINTER(Windows.Win32.Security.Cryptography.Catalog.CRYPTCATMEMBER_head): ...
@winfunctype('WINTRUST.dll')
def CryptCATCDFEnumAttributes(pCDF: POINTER(Windows.Win32.Security.Cryptography.Catalog.CRYPTCATCDF_head), pMember: POINTER(Windows.Win32.Security.Cryptography.Catalog.CRYPTCATMEMBER_head), pPrevAttr: POINTER(Windows.Win32.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE_head), pfnParseError: Windows.Win32.Security.Cryptography.Catalog.PFN_CDF_PARSE_ERROR_CALLBACK) -> POINTER(Windows.Win32.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE_head): ...
@winfunctype('WINTRUST.dll')
def IsCatalogFile(hFile: Windows.Win32.Foundation.HANDLE, pwszFileName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptCATAdminAcquireContext(phCatAdmin: POINTER(IntPtr), pgSubsystem: POINTER(Guid), dwFlags: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptCATAdminAcquireContext2(phCatAdmin: POINTER(IntPtr), pgSubsystem: POINTER(Guid), pwszHashAlgorithm: Windows.Win32.Foundation.PWSTR, pStrongHashPolicy: POINTER(Windows.Win32.Security.Cryptography.CERT_STRONG_SIGN_PARA_head), dwFlags: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptCATAdminReleaseContext(hCatAdmin: IntPtr, dwFlags: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptCATAdminReleaseCatalogContext(hCatAdmin: IntPtr, hCatInfo: IntPtr, dwFlags: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptCATAdminEnumCatalogFromHash(hCatAdmin: IntPtr, pbHash: POINTER(Byte), cbHash: UInt32, dwFlags: UInt32, phPrevCatInfo: POINTER(IntPtr)) -> IntPtr: ...
@winfunctype('WINTRUST.dll')
def CryptCATAdminCalcHashFromFileHandle(hFile: Windows.Win32.Foundation.HANDLE, pcbHash: POINTER(UInt32), pbHash: POINTER(Byte), dwFlags: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptCATAdminCalcHashFromFileHandle2(hCatAdmin: IntPtr, hFile: Windows.Win32.Foundation.HANDLE, pcbHash: POINTER(UInt32), pbHash: POINTER(Byte), dwFlags: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptCATAdminAddCatalog(hCatAdmin: IntPtr, pwszCatalogFile: Windows.Win32.Foundation.PWSTR, pwszSelectBaseName: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> IntPtr: ...
@winfunctype('WINTRUST.dll')
def CryptCATAdminRemoveCatalog(hCatAdmin: IntPtr, pwszCatalogFile: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptCATCatalogInfoFromContext(hCatInfo: IntPtr, psCatInfo: POINTER(Windows.Win32.Security.Cryptography.Catalog.CATALOG_INFO_head), dwFlags: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptCATAdminResolveCatalogPath(hCatAdmin: IntPtr, pwszCatalogFile: Windows.Win32.Foundation.PWSTR, psCatInfo: POINTER(Windows.Win32.Security.Cryptography.Catalog.CATALOG_INFO_head), dwFlags: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptCATAdminPauseServiceForBackup(dwFlags: UInt32, fResume: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
class CATALOG_INFO(EasyCastStructure):
    cbStruct: UInt32
    wszCatalogFile: Char * 260
class CRYPTCATATTRIBUTE(EasyCastStructure):
    cbStruct: UInt32
    pwszReferenceTag: Windows.Win32.Foundation.PWSTR
    dwAttrTypeAndAction: UInt32
    cbValue: UInt32
    pbValue: POINTER(Byte)
    dwReserved: UInt32
class CRYPTCATCDF(EasyCastStructure):
    cbStruct: UInt32
    hFile: Windows.Win32.Foundation.HANDLE
    dwCurFilePos: UInt32
    dwLastMemberOffset: UInt32
    fEOF: Windows.Win32.Foundation.BOOL
    pwszResultDir: Windows.Win32.Foundation.PWSTR
    hCATStore: Windows.Win32.Foundation.HANDLE
class CRYPTCATMEMBER(EasyCastStructure):
    cbStruct: UInt32
    pwszReferenceTag: Windows.Win32.Foundation.PWSTR
    pwszFileName: Windows.Win32.Foundation.PWSTR
    gSubjectType: Guid
    fdwMemberFlags: UInt32
    pIndirectData: POINTER(Windows.Win32.Security.Cryptography.Sip.SIP_INDIRECT_DATA_head)
    dwCertVersion: UInt32
    dwReserved: UInt32
    hReserved: Windows.Win32.Foundation.HANDLE
    sEncodedIndirectData: Windows.Win32.Security.Cryptography.CRYPT_INTEGER_BLOB
    sEncodedMemberInfo: Windows.Win32.Security.Cryptography.CRYPT_INTEGER_BLOB
class CRYPTCATSTORE(EasyCastStructure):
    cbStruct: UInt32
    dwPublicVersion: UInt32
    pwszP7File: Windows.Win32.Foundation.PWSTR
    hProv: UIntPtr
    dwEncodingType: UInt32
    fdwStoreFlags: Windows.Win32.Security.Cryptography.Catalog.CRYPTCAT_OPEN_FLAGS
    hReserved: Windows.Win32.Foundation.HANDLE
    hAttrs: Windows.Win32.Foundation.HANDLE
    hCryptMsg: c_void_p
    hSorted: Windows.Win32.Foundation.HANDLE
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
class MS_ADDINFO_CATALOGMEMBER(EasyCastStructure):
    cbStruct: UInt32
    pStore: POINTER(Windows.Win32.Security.Cryptography.Catalog.CRYPTCATSTORE_head)
    pMember: POINTER(Windows.Win32.Security.Cryptography.Catalog.CRYPTCATMEMBER_head)
@winfunctype_pointer
def PFN_CDF_PARSE_ERROR_CALLBACK(dwErrorArea: UInt32, dwLocalError: UInt32, pwszLine: Windows.Win32.Foundation.PWSTR) -> Void: ...
make_head(_module, 'CATALOG_INFO')
make_head(_module, 'CRYPTCATATTRIBUTE')
make_head(_module, 'CRYPTCATCDF')
make_head(_module, 'CRYPTCATMEMBER')
make_head(_module, 'CRYPTCATSTORE')
make_head(_module, 'MS_ADDINFO_CATALOGMEMBER')
make_head(_module, 'PFN_CDF_PARSE_ERROR_CALLBACK')
