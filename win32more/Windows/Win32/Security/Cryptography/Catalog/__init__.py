from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Security.Cryptography
import win32more.Windows.Win32.Security.Cryptography.Catalog
import win32more.Windows.Win32.Security.Cryptography.Sip
szOID_CATALOG_LIST: String = '1.3.6.1.4.1.311.12.1.1'
szOID_CATALOG_LIST_MEMBER: String = '1.3.6.1.4.1.311.12.1.2'
szOID_CATALOG_LIST_MEMBER2: String = '1.3.6.1.4.1.311.12.1.3'
CRYPTCAT_FILEEXT: String = 'CAT'
CRYPTCAT_MAX_MEMBERTAG: UInt32 = 64
CRYPTCAT_MEMBER_SORTED: UInt32 = 1073741824
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
def CryptCATOpen(pwszFileName: win32more.Windows.Win32.Foundation.PWSTR, fdwOpenFlags: win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCAT_OPEN_FLAGS, hProv: UIntPtr, dwPublicVersion: win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCAT_VERSION, dwEncodingType: UInt32) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('WINTRUST.dll')
def CryptCATClose(hCatalog: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptCATStoreFromHandle(hCatalog: win32more.Windows.Win32.Foundation.HANDLE) -> POINTER(win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCATSTORE): ...
@winfunctype('WINTRUST.dll')
def CryptCATHandleFromStore(pCatStore: POINTER(win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCATSTORE)) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('WINTRUST.dll')
def CryptCATPersistStore(hCatalog: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptCATGetCatAttrInfo(hCatalog: win32more.Windows.Win32.Foundation.HANDLE, pwszReferenceTag: win32more.Windows.Win32.Foundation.PWSTR) -> POINTER(win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE): ...
@winfunctype('WINTRUST.dll')
def CryptCATPutCatAttrInfo(hCatalog: win32more.Windows.Win32.Foundation.HANDLE, pwszReferenceTag: win32more.Windows.Win32.Foundation.PWSTR, dwAttrTypeAndAction: UInt32, cbData: UInt32, pbData: POINTER(Byte)) -> POINTER(win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE): ...
@winfunctype('WINTRUST.dll')
def CryptCATEnumerateCatAttr(hCatalog: win32more.Windows.Win32.Foundation.HANDLE, pPrevAttr: POINTER(win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE)) -> POINTER(win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE): ...
@winfunctype('WINTRUST.dll')
def CryptCATGetMemberInfo(hCatalog: win32more.Windows.Win32.Foundation.HANDLE, pwszReferenceTag: win32more.Windows.Win32.Foundation.PWSTR) -> POINTER(win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCATMEMBER): ...
@winfunctype('WINTRUST.dll')
def CryptCATAllocSortedMemberInfo(hCatalog: win32more.Windows.Win32.Foundation.HANDLE, pwszReferenceTag: win32more.Windows.Win32.Foundation.PWSTR) -> POINTER(win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCATMEMBER): ...
@winfunctype('WINTRUST.dll')
def CryptCATFreeSortedMemberInfo(hCatalog: win32more.Windows.Win32.Foundation.HANDLE, pCatMember: POINTER(win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCATMEMBER)) -> Void: ...
@winfunctype('WINTRUST.dll')
def CryptCATGetAttrInfo(hCatalog: win32more.Windows.Win32.Foundation.HANDLE, pCatMember: POINTER(win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCATMEMBER), pwszReferenceTag: win32more.Windows.Win32.Foundation.PWSTR) -> POINTER(win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE): ...
@winfunctype('WINTRUST.dll')
def CryptCATPutMemberInfo(hCatalog: win32more.Windows.Win32.Foundation.HANDLE, pwszFileName: win32more.Windows.Win32.Foundation.PWSTR, pwszReferenceTag: win32more.Windows.Win32.Foundation.PWSTR, pgSubjectType: POINTER(Guid), dwCertVersion: UInt32, cbSIPIndirectData: UInt32, pbSIPIndirectData: POINTER(Byte)) -> POINTER(win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCATMEMBER): ...
@winfunctype('WINTRUST.dll')
def CryptCATPutAttrInfo(hCatalog: win32more.Windows.Win32.Foundation.HANDLE, pCatMember: POINTER(win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCATMEMBER), pwszReferenceTag: win32more.Windows.Win32.Foundation.PWSTR, dwAttrTypeAndAction: UInt32, cbData: UInt32, pbData: POINTER(Byte)) -> POINTER(win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE): ...
@winfunctype('WINTRUST.dll')
def CryptCATEnumerateMember(hCatalog: win32more.Windows.Win32.Foundation.HANDLE, pPrevMember: POINTER(win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCATMEMBER)) -> POINTER(win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCATMEMBER): ...
@winfunctype('WINTRUST.dll')
def CryptCATEnumerateAttr(hCatalog: win32more.Windows.Win32.Foundation.HANDLE, pCatMember: POINTER(win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCATMEMBER), pPrevAttr: POINTER(win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE)) -> POINTER(win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE): ...
@winfunctype('WINTRUST.dll')
def CryptCATCDFOpen(pwszFilePath: win32more.Windows.Win32.Foundation.PWSTR, pfnParseError: win32more.Windows.Win32.Security.Cryptography.Catalog.PFN_CDF_PARSE_ERROR_CALLBACK) -> POINTER(win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCATCDF): ...
@winfunctype('WINTRUST.dll')
def CryptCATCDFClose(pCDF: POINTER(win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCATCDF)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptCATCDFEnumCatAttributes(pCDF: POINTER(win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCATCDF), pPrevAttr: POINTER(win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE), pfnParseError: win32more.Windows.Win32.Security.Cryptography.Catalog.PFN_CDF_PARSE_ERROR_CALLBACK) -> POINTER(win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE): ...
@winfunctype('WINTRUST.dll')
def CryptCATCDFEnumMembers(pCDF: POINTER(win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCATCDF), pPrevMember: POINTER(win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCATMEMBER), pfnParseError: win32more.Windows.Win32.Security.Cryptography.Catalog.PFN_CDF_PARSE_ERROR_CALLBACK) -> POINTER(win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCATMEMBER): ...
@winfunctype('WINTRUST.dll')
def CryptCATCDFEnumAttributes(pCDF: POINTER(win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCATCDF), pMember: POINTER(win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCATMEMBER), pPrevAttr: POINTER(win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE), pfnParseError: win32more.Windows.Win32.Security.Cryptography.Catalog.PFN_CDF_PARSE_ERROR_CALLBACK) -> POINTER(win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE): ...
@winfunctype('WINTRUST.dll')
def IsCatalogFile(hFile: win32more.Windows.Win32.Foundation.HANDLE, pwszFileName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptCATAdminAcquireContext(phCatAdmin: POINTER(IntPtr), pgSubsystem: POINTER(Guid), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptCATAdminAcquireContext2(phCatAdmin: POINTER(IntPtr), pgSubsystem: POINTER(Guid), pwszHashAlgorithm: win32more.Windows.Win32.Foundation.PWSTR, pStrongHashPolicy: POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_STRONG_SIGN_PARA), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptCATAdminReleaseContext(hCatAdmin: IntPtr, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptCATAdminReleaseCatalogContext(hCatAdmin: IntPtr, hCatInfo: IntPtr, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptCATAdminEnumCatalogFromHash(hCatAdmin: IntPtr, pbHash: POINTER(Byte), cbHash: UInt32, dwFlags: UInt32, phPrevCatInfo: POINTER(IntPtr)) -> IntPtr: ...
@winfunctype('WINTRUST.dll')
def CryptCATAdminCalcHashFromFileHandle(hFile: win32more.Windows.Win32.Foundation.HANDLE, pcbHash: POINTER(UInt32), pbHash: POINTER(Byte), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptCATAdminCalcHashFromFileHandle2(hCatAdmin: IntPtr, hFile: win32more.Windows.Win32.Foundation.HANDLE, pcbHash: POINTER(UInt32), pbHash: POINTER(Byte), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptCATAdminAddCatalog(hCatAdmin: IntPtr, pwszCatalogFile: win32more.Windows.Win32.Foundation.PWSTR, pwszSelectBaseName: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> IntPtr: ...
@winfunctype('WINTRUST.dll')
def CryptCATAdminRemoveCatalog(hCatAdmin: IntPtr, pwszCatalogFile: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptCATCatalogInfoFromContext(hCatInfo: IntPtr, psCatInfo: POINTER(win32more.Windows.Win32.Security.Cryptography.Catalog.CATALOG_INFO), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptCATAdminResolveCatalogPath(hCatAdmin: IntPtr, pwszCatalogFile: win32more.Windows.Win32.Foundation.PWSTR, psCatInfo: POINTER(win32more.Windows.Win32.Security.Cryptography.Catalog.CATALOG_INFO), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptCATAdminPauseServiceForBackup(dwFlags: UInt32, fResume: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptCATCDFEnumMembersByCDFTagEx(pCDF: POINTER(win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCATCDF), pwszPrevCDFTag: win32more.Windows.Win32.Foundation.PWSTR, pfnParseError: win32more.Windows.Win32.Security.Cryptography.Catalog.PFN_CDF_PARSE_ERROR_CALLBACK, ppMember: POINTER(POINTER(win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCATMEMBER)), fContinueOnError: win32more.Windows.Win32.Foundation.BOOL, pvReserved: VoidPtr) -> win32more.Windows.Win32.Foundation.PWSTR: ...
@winfunctype('WINTRUST.dll')
def CryptCATCDFEnumAttributesWithCDFTag(pCDF: POINTER(win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCATCDF), pwszMemberTag: win32more.Windows.Win32.Foundation.PWSTR, pMember: POINTER(win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCATMEMBER), pPrevAttr: POINTER(win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE), pfnParseError: win32more.Windows.Win32.Security.Cryptography.Catalog.PFN_CDF_PARSE_ERROR_CALLBACK) -> POINTER(win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE): ...
class CATALOG_INFO(Structure):
    cbStruct: UInt32
    wszCatalogFile: Char * 260
class CRYPTCATATTRIBUTE(Structure):
    cbStruct: UInt32
    pwszReferenceTag: win32more.Windows.Win32.Foundation.PWSTR
    dwAttrTypeAndAction: win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE_FLAGS
    cbValue: UInt32
    pbValue: POINTER(Byte)
    dwReserved: UInt32
CRYPTCATATTRIBUTE_FLAGS = UInt32
CRYPTCAT_ATTR_AUTHENTICATED: win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE_FLAGS = 268435456
CRYPTCAT_ATTR_UNAUTHENTICATED: win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE_FLAGS = 536870912
CRYPTCAT_ATTR_NAMEASCII: win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE_FLAGS = 1
CRYPTCAT_ATTR_NAMEOBJID: win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE_FLAGS = 2
CRYPTCAT_ATTR_DATAASCII: win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE_FLAGS = 65536
CRYPTCAT_ATTR_DATABASE64: win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE_FLAGS = 131072
CRYPTCAT_ATTR_DATAREPLACE: win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE_FLAGS = 262144
CRYPTCAT_ATTR_NO_AUTO_COMPAT_ENTRY: win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCATATTRIBUTE_FLAGS = 16777216
class CRYPTCATCDF(Structure):
    cbStruct: UInt32
    hFile: win32more.Windows.Win32.Foundation.HANDLE
    dwCurFilePos: UInt32
    dwLastMemberOffset: UInt32
    fEOF: win32more.Windows.Win32.Foundation.BOOL
    pwszResultDir: win32more.Windows.Win32.Foundation.PWSTR
    hCATStore: win32more.Windows.Win32.Foundation.HANDLE
class CRYPTCATMEMBER(Structure):
    cbStruct: UInt32
    pwszReferenceTag: win32more.Windows.Win32.Foundation.PWSTR
    pwszFileName: win32more.Windows.Win32.Foundation.PWSTR
    gSubjectType: Guid
    fdwMemberFlags: UInt32
    pIndirectData: POINTER(win32more.Windows.Win32.Security.Cryptography.Sip.SIP_INDIRECT_DATA)
    dwCertVersion: UInt32
    dwReserved: UInt32
    hReserved: win32more.Windows.Win32.Foundation.HANDLE
    sEncodedIndirectData: win32more.Windows.Win32.Security.Cryptography.CRYPT_INTEGER_BLOB
    sEncodedMemberInfo: win32more.Windows.Win32.Security.Cryptography.CRYPT_INTEGER_BLOB
class CRYPTCATSTORE(Structure):
    cbStruct: UInt32
    dwPublicVersion: UInt32
    pwszP7File: win32more.Windows.Win32.Foundation.PWSTR
    hProv: UIntPtr
    dwEncodingType: UInt32
    fdwStoreFlags: win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCAT_OPEN_FLAGS
    hReserved: win32more.Windows.Win32.Foundation.HANDLE
    hAttrs: win32more.Windows.Win32.Foundation.HANDLE
    hCryptMsg: VoidPtr
    hSorted: win32more.Windows.Win32.Foundation.HANDLE
CRYPTCAT_OPEN_FLAGS = UInt32
CRYPTCAT_OPEN_ALWAYS: win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCAT_OPEN_FLAGS = 2
CRYPTCAT_OPEN_CREATENEW: win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCAT_OPEN_FLAGS = 1
CRYPTCAT_OPEN_EXISTING: win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCAT_OPEN_FLAGS = 4
CRYPTCAT_OPEN_EXCLUDE_PAGE_HASHES: win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCAT_OPEN_FLAGS = 65536
CRYPTCAT_OPEN_INCLUDE_PAGE_HASHES: win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCAT_OPEN_FLAGS = 131072
CRYPTCAT_OPEN_VERIFYSIGHASH: win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCAT_OPEN_FLAGS = 268435456
CRYPTCAT_OPEN_NO_CONTENT_HCRYPTMSG: win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCAT_OPEN_FLAGS = 536870912
CRYPTCAT_OPEN_SORTED: win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCAT_OPEN_FLAGS = 1073741824
CRYPTCAT_OPEN_FLAGS_MASK: win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCAT_OPEN_FLAGS = 4294901760
CRYPTCAT_VERSION = UInt32
CRYPTCAT_VERSION_1: win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCAT_VERSION = 256
CRYPTCAT_VERSION_2: win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCAT_VERSION = 512
class MS_ADDINFO_CATALOGMEMBER(Structure):
    cbStruct: UInt32
    pStore: POINTER(win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCATSTORE)
    pMember: POINTER(win32more.Windows.Win32.Security.Cryptography.Catalog.CRYPTCATMEMBER)
@winfunctype_pointer
def PFN_CDF_PARSE_ERROR_CALLBACK(dwErrorArea: UInt32, dwLocalError: UInt32, pwszLine: win32more.Windows.Win32.Foundation.PWSTR) -> Void: ...


make_ready(__name__)
