from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Security.Cryptography
import win32more.Windows.Win32.Security.Cryptography.Catalog
import win32more.Windows.Win32.Security.Cryptography.Sip
MSSIP_FLAGS_PROHIBIT_RESIZE_ON_CREATE: UInt32 = 65536
MSSIP_FLAGS_USE_CATALOG: UInt32 = 131072
MSSIP_FLAGS_MULTI_HASH: UInt32 = 262144
SPC_RELAXED_PE_MARKER_CHECK: UInt32 = 2048
SPC_MARKER_CHECK_SKIP_SIP_INDIRECT_DATA_FLAG: UInt32 = 1
SPC_MARKER_CHECK_CURRENTLY_SUPPORTED_FLAGS: UInt32 = 1
MSSIP_ADDINFO_NONE: UInt32 = 0
MSSIP_ADDINFO_FLAT: UInt32 = 1
MSSIP_ADDINFO_CATMEMBER: UInt32 = 2
MSSIP_ADDINFO_BLOB: UInt32 = 3
MSSIP_ADDINFO_NONMSSIP: UInt32 = 500
SIP_CAP_SET_VERSION_2: UInt32 = 2
SIP_CAP_SET_VERSION_3: UInt32 = 3
SIP_CAP_SET_CUR_VER: UInt32 = 3
SIP_CAP_FLAG_SEALING: UInt32 = 1
SIP_MAX_MAGIC_NUMBER: UInt32 = 4
@winfunctype('WINTRUST.dll')
def CryptSIPGetSignedDataMsg(pSubjectInfo: POINTER(win32more.Windows.Win32.Security.Cryptography.Sip.SIP_SUBJECTINFO), pdwEncodingType: POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_QUERY_ENCODING_TYPE), dwIndex: UInt32, pcbSignedDataMsg: POINTER(UInt32), pbSignedDataMsg: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptSIPPutSignedDataMsg(pSubjectInfo: POINTER(win32more.Windows.Win32.Security.Cryptography.Sip.SIP_SUBJECTINFO), dwEncodingType: win32more.Windows.Win32.Security.Cryptography.CERT_QUERY_ENCODING_TYPE, pdwIndex: POINTER(UInt32), cbSignedDataMsg: UInt32, pbSignedDataMsg: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptSIPCreateIndirectData(pSubjectInfo: POINTER(win32more.Windows.Win32.Security.Cryptography.Sip.SIP_SUBJECTINFO), pcbIndirectData: POINTER(UInt32), pIndirectData: POINTER(win32more.Windows.Win32.Security.Cryptography.Sip.SIP_INDIRECT_DATA)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptSIPVerifyIndirectData(pSubjectInfo: POINTER(win32more.Windows.Win32.Security.Cryptography.Sip.SIP_SUBJECTINFO), pIndirectData: POINTER(win32more.Windows.Win32.Security.Cryptography.Sip.SIP_INDIRECT_DATA)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptSIPRemoveSignedDataMsg(pSubjectInfo: POINTER(win32more.Windows.Win32.Security.Cryptography.Sip.SIP_SUBJECTINFO), dwIndex: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('CRYPT32.dll')
def CryptSIPLoad(pgSubject: POINTER(Guid), dwFlags: UInt32, pSipDispatch: POINTER(win32more.Windows.Win32.Security.Cryptography.Sip.SIP_DISPATCH_INFO)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('CRYPT32.dll')
def CryptSIPRetrieveSubjectGuid(FileName: win32more.Windows.Win32.Foundation.PWSTR, hFileIn: win32more.Windows.Win32.Foundation.HANDLE, pgSubject: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('CRYPT32.dll')
def CryptSIPRetrieveSubjectGuidForCatalogFile(FileName: win32more.Windows.Win32.Foundation.PWSTR, hFileIn: win32more.Windows.Win32.Foundation.HANDLE, pgSubject: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('CRYPT32.dll')
def CryptSIPAddProvider(psNewProv: POINTER(win32more.Windows.Win32.Security.Cryptography.Sip.SIP_ADD_NEWPROVIDER)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('CRYPT32.dll')
def CryptSIPRemoveProvider(pgProv: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptSIPGetCaps(pSubjInfo: POINTER(win32more.Windows.Win32.Security.Cryptography.Sip.SIP_SUBJECTINFO), pCaps: POINTER(win32more.Windows.Win32.Security.Cryptography.Sip.SIP_CAP_SET_V3)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptSIPGetSealedDigest(pSubjectInfo: POINTER(win32more.Windows.Win32.Security.Cryptography.Sip.SIP_SUBJECTINFO), pSig: POINTER(Byte), dwSig: UInt32, pbDigest: POINTER(Byte), pcbDigest: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
class MS_ADDINFO_BLOB(Structure):
    cbStruct: UInt32
    cbMemObject: UInt32
    pbMemObject: POINTER(Byte)
    cbMemSignedMsg: UInt32
    pbMemSignedMsg: POINTER(Byte)
class MS_ADDINFO_FLAT(Structure):
    cbStruct: UInt32
    pIndirectData: POINTER(win32more.Windows.Win32.Security.Cryptography.Sip.SIP_INDIRECT_DATA)
class SIP_ADD_NEWPROVIDER(Structure):
    cbStruct: UInt32
    pgSubject: POINTER(Guid)
    pwszDLLFileName: win32more.Windows.Win32.Foundation.PWSTR
    pwszMagicNumber: win32more.Windows.Win32.Foundation.PWSTR
    pwszIsFunctionName: win32more.Windows.Win32.Foundation.PWSTR
    pwszGetFuncName: win32more.Windows.Win32.Foundation.PWSTR
    pwszPutFuncName: win32more.Windows.Win32.Foundation.PWSTR
    pwszCreateFuncName: win32more.Windows.Win32.Foundation.PWSTR
    pwszVerifyFuncName: win32more.Windows.Win32.Foundation.PWSTR
    pwszRemoveFuncName: win32more.Windows.Win32.Foundation.PWSTR
    pwszIsFunctionNameFmt2: win32more.Windows.Win32.Foundation.PWSTR
    pwszGetCapFuncName: win32more.Windows.Win32.Foundation.PWSTR
class SIP_CAP_SET_V2(Structure):
    cbSize: UInt32
    dwVersion: UInt32
    isMultiSign: win32more.Windows.Win32.Foundation.BOOL
    dwReserved: UInt32
class SIP_CAP_SET_V3(Structure):
    cbSize: UInt32
    dwVersion: UInt32
    isMultiSign: win32more.Windows.Win32.Foundation.BOOL
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        dwFlags: UInt32
        dwReserved: UInt32
class SIP_DISPATCH_INFO(Structure):
    cbSize: UInt32
    hSIP: win32more.Windows.Win32.Foundation.HANDLE
    pfGet: win32more.Windows.Win32.Security.Cryptography.Sip.pCryptSIPGetSignedDataMsg
    pfPut: win32more.Windows.Win32.Security.Cryptography.Sip.pCryptSIPPutSignedDataMsg
    pfCreate: win32more.Windows.Win32.Security.Cryptography.Sip.pCryptSIPCreateIndirectData
    pfVerify: win32more.Windows.Win32.Security.Cryptography.Sip.pCryptSIPVerifyIndirectData
    pfRemove: win32more.Windows.Win32.Security.Cryptography.Sip.pCryptSIPRemoveSignedDataMsg
class SIP_INDIRECT_DATA(Structure):
    Data: win32more.Windows.Win32.Security.Cryptography.CRYPT_ATTRIBUTE_TYPE_VALUE
    DigestAlgorithm: win32more.Windows.Win32.Security.Cryptography.CRYPT_ALGORITHM_IDENTIFIER
    Digest: win32more.Windows.Win32.Security.Cryptography.CRYPT_INTEGER_BLOB
class SIP_SUBJECTINFO(Structure):
    cbSize: UInt32
    pgSubjectType: POINTER(Guid)
    hFile: win32more.Windows.Win32.Foundation.HANDLE
    pwsFileName: win32more.Windows.Win32.Foundation.PWSTR
    pwsDisplayName: win32more.Windows.Win32.Foundation.PWSTR
    dwReserved1: UInt32
    dwIntVersion: UInt32
    hProv: UIntPtr
    DigestAlgorithm: win32more.Windows.Win32.Security.Cryptography.CRYPT_ALGORITHM_IDENTIFIER
    dwFlags: UInt32
    dwEncodingType: UInt32
    dwReserved2: UInt32
    fdwCAPISettings: UInt32
    fdwSecuritySettings: UInt32
    dwIndex: UInt32
    dwUnionChoice: UInt32
    Anonymous: _Anonymous_e__Union
    pClientData: VoidPtr
    class _Anonymous_e__Union(Union):
        psFlat: POINTER(win32more.Windows.Win32.Security.Cryptography.Sip.MS_ADDINFO_FLAT)
        psCatMember: POINTER(win32more.Windows.Win32.Security.Cryptography.Catalog.MS_ADDINFO_CATALOGMEMBER)
        psBlob: POINTER(win32more.Windows.Win32.Security.Cryptography.Sip.MS_ADDINFO_BLOB)
@winfunctype_pointer
def pCryptSIPCreateIndirectData(pSubjectInfo: POINTER(win32more.Windows.Win32.Security.Cryptography.Sip.SIP_SUBJECTINFO), pcbIndirectData: POINTER(UInt32), pIndirectData: POINTER(win32more.Windows.Win32.Security.Cryptography.Sip.SIP_INDIRECT_DATA)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def pCryptSIPGetCaps(pSubjInfo: POINTER(win32more.Windows.Win32.Security.Cryptography.Sip.SIP_SUBJECTINFO), pCaps: POINTER(win32more.Windows.Win32.Security.Cryptography.Sip.SIP_CAP_SET_V3)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def pCryptSIPGetSealedDigest(pSubjectInfo: POINTER(win32more.Windows.Win32.Security.Cryptography.Sip.SIP_SUBJECTINFO), pSig: POINTER(Byte), dwSig: UInt32, pbDigest: POINTER(Byte), pcbDigest: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def pCryptSIPGetSignedDataMsg(pSubjectInfo: POINTER(win32more.Windows.Win32.Security.Cryptography.Sip.SIP_SUBJECTINFO), pdwEncodingType: POINTER(UInt32), dwIndex: UInt32, pcbSignedDataMsg: POINTER(UInt32), pbSignedDataMsg: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def pCryptSIPPutSignedDataMsg(pSubjectInfo: POINTER(win32more.Windows.Win32.Security.Cryptography.Sip.SIP_SUBJECTINFO), dwEncodingType: UInt32, pdwIndex: POINTER(UInt32), cbSignedDataMsg: UInt32, pbSignedDataMsg: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def pCryptSIPRemoveSignedDataMsg(pSubjectInfo: POINTER(win32more.Windows.Win32.Security.Cryptography.Sip.SIP_SUBJECTINFO), dwIndex: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def pCryptSIPVerifyIndirectData(pSubjectInfo: POINTER(win32more.Windows.Win32.Security.Cryptography.Sip.SIP_SUBJECTINFO), pIndirectData: POINTER(win32more.Windows.Win32.Security.Cryptography.Sip.SIP_INDIRECT_DATA)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def pfnIsFileSupported(hFile: win32more.Windows.Win32.Foundation.HANDLE, pgSubject: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def pfnIsFileSupportedName(pwszFileName: win32more.Windows.Win32.Foundation.PWSTR, pgSubject: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.BOOL: ...


make_ready(__name__)
