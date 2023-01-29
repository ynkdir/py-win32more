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
MSSIP_FLAGS_PROHIBIT_RESIZE_ON_CREATE: UInt32 = 65536
MSSIP_FLAGS_USE_CATALOG: UInt32 = 131072
MSSIP_FLAGS_MULTI_HASH: UInt32 = 262144
SPC_INC_PE_RESOURCES_FLAG: UInt32 = 128
SPC_INC_PE_DEBUG_INFO_FLAG: UInt32 = 64
SPC_INC_PE_IMPORT_ADDR_TABLE_FLAG: UInt32 = 32
SPC_EXC_PE_PAGE_HASHES_FLAG: UInt32 = 16
SPC_INC_PE_PAGE_HASHES_FLAG: UInt32 = 256
SPC_DIGEST_GENERATE_FLAG: UInt32 = 512
SPC_DIGEST_SIGN_FLAG: UInt32 = 1024
SPC_DIGEST_SIGN_EX_FLAG: UInt32 = 16384
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
def CryptSIPGetSignedDataMsg(pSubjectInfo: POINTER(win32more.Security.Cryptography.Sip.SIP_SUBJECTINFO_head), pdwEncodingType: POINTER(win32more.Security.Cryptography.CERT_QUERY_ENCODING_TYPE), dwIndex: UInt32, pcbSignedDataMsg: POINTER(UInt32), pbSignedDataMsg: c_char_p_no) -> win32more.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptSIPPutSignedDataMsg(pSubjectInfo: POINTER(win32more.Security.Cryptography.Sip.SIP_SUBJECTINFO_head), dwEncodingType: win32more.Security.Cryptography.CERT_QUERY_ENCODING_TYPE, pdwIndex: POINTER(UInt32), cbSignedDataMsg: UInt32, pbSignedDataMsg: c_char_p_no) -> win32more.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptSIPCreateIndirectData(pSubjectInfo: POINTER(win32more.Security.Cryptography.Sip.SIP_SUBJECTINFO_head), pcbIndirectData: POINTER(UInt32), pIndirectData: POINTER(win32more.Security.Cryptography.Sip.SIP_INDIRECT_DATA_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptSIPVerifyIndirectData(pSubjectInfo: POINTER(win32more.Security.Cryptography.Sip.SIP_SUBJECTINFO_head), pIndirectData: POINTER(win32more.Security.Cryptography.Sip.SIP_INDIRECT_DATA_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptSIPRemoveSignedDataMsg(pSubjectInfo: POINTER(win32more.Security.Cryptography.Sip.SIP_SUBJECTINFO_head), dwIndex: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('CRYPT32.dll')
def CryptSIPLoad(pgSubject: POINTER(Guid), dwFlags: UInt32, pSipDispatch: POINTER(win32more.Security.Cryptography.Sip.SIP_DISPATCH_INFO_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('CRYPT32.dll')
def CryptSIPRetrieveSubjectGuid(FileName: win32more.Foundation.PWSTR, hFileIn: win32more.Foundation.HANDLE, pgSubject: POINTER(Guid)) -> win32more.Foundation.BOOL: ...
@winfunctype('CRYPT32.dll')
def CryptSIPRetrieveSubjectGuidForCatalogFile(FileName: win32more.Foundation.PWSTR, hFileIn: win32more.Foundation.HANDLE, pgSubject: POINTER(Guid)) -> win32more.Foundation.BOOL: ...
@winfunctype('CRYPT32.dll')
def CryptSIPAddProvider(psNewProv: POINTER(win32more.Security.Cryptography.Sip.SIP_ADD_NEWPROVIDER_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('CRYPT32.dll')
def CryptSIPRemoveProvider(pgProv: POINTER(Guid)) -> win32more.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptSIPGetCaps(pSubjInfo: POINTER(win32more.Security.Cryptography.Sip.SIP_SUBJECTINFO_head), pCaps: POINTER(win32more.Security.Cryptography.Sip.SIP_CAP_SET_V3_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptSIPGetSealedDigest(pSubjectInfo: POINTER(win32more.Security.Cryptography.Sip.SIP_SUBJECTINFO_head), pSig: c_char_p_no, dwSig: UInt32, pbDigest: c_char_p_no, pcbDigest: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
class MS_ADDINFO_BLOB(Structure):
    cbStruct: UInt32
    cbMemObject: UInt32
    pbMemObject: c_char_p_no
    cbMemSignedMsg: UInt32
    pbMemSignedMsg: c_char_p_no
class MS_ADDINFO_FLAT(Structure):
    cbStruct: UInt32
    pIndirectData: POINTER(win32more.Security.Cryptography.Sip.SIP_INDIRECT_DATA_head)
@winfunctype_pointer
def pCryptSIPCreateIndirectData(pSubjectInfo: POINTER(win32more.Security.Cryptography.Sip.SIP_SUBJECTINFO_head), pcbIndirectData: POINTER(UInt32), pIndirectData: POINTER(win32more.Security.Cryptography.Sip.SIP_INDIRECT_DATA_head)) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def pCryptSIPGetCaps(pSubjInfo: POINTER(win32more.Security.Cryptography.Sip.SIP_SUBJECTINFO_head), pCaps: POINTER(win32more.Security.Cryptography.Sip.SIP_CAP_SET_V3_head)) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def pCryptSIPGetSealedDigest(pSubjectInfo: POINTER(win32more.Security.Cryptography.Sip.SIP_SUBJECTINFO_head), pSig: c_char_p_no, dwSig: UInt32, pbDigest: c_char_p_no, pcbDigest: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def pCryptSIPGetSignedDataMsg(pSubjectInfo: POINTER(win32more.Security.Cryptography.Sip.SIP_SUBJECTINFO_head), pdwEncodingType: POINTER(UInt32), dwIndex: UInt32, pcbSignedDataMsg: POINTER(UInt32), pbSignedDataMsg: c_char_p_no) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def pCryptSIPPutSignedDataMsg(pSubjectInfo: POINTER(win32more.Security.Cryptography.Sip.SIP_SUBJECTINFO_head), dwEncodingType: UInt32, pdwIndex: POINTER(UInt32), cbSignedDataMsg: UInt32, pbSignedDataMsg: c_char_p_no) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def pCryptSIPRemoveSignedDataMsg(pSubjectInfo: POINTER(win32more.Security.Cryptography.Sip.SIP_SUBJECTINFO_head), dwIndex: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def pCryptSIPVerifyIndirectData(pSubjectInfo: POINTER(win32more.Security.Cryptography.Sip.SIP_SUBJECTINFO_head), pIndirectData: POINTER(win32more.Security.Cryptography.Sip.SIP_INDIRECT_DATA_head)) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def pfnIsFileSupported(hFile: win32more.Foundation.HANDLE, pgSubject: POINTER(Guid)) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def pfnIsFileSupportedName(pwszFileName: win32more.Foundation.PWSTR, pgSubject: POINTER(Guid)) -> win32more.Foundation.BOOL: ...
class SIP_ADD_NEWPROVIDER(Structure):
    cbStruct: UInt32
    pgSubject: POINTER(Guid)
    pwszDLLFileName: win32more.Foundation.PWSTR
    pwszMagicNumber: win32more.Foundation.PWSTR
    pwszIsFunctionName: win32more.Foundation.PWSTR
    pwszGetFuncName: win32more.Foundation.PWSTR
    pwszPutFuncName: win32more.Foundation.PWSTR
    pwszCreateFuncName: win32more.Foundation.PWSTR
    pwszVerifyFuncName: win32more.Foundation.PWSTR
    pwszRemoveFuncName: win32more.Foundation.PWSTR
    pwszIsFunctionNameFmt2: win32more.Foundation.PWSTR
    pwszGetCapFuncName: win32more.Foundation.PWSTR
class SIP_CAP_SET_V2(Structure):
    cbSize: UInt32
    dwVersion: UInt32
    isMultiSign: win32more.Foundation.BOOL
    dwReserved: UInt32
class SIP_CAP_SET_V3(Structure):
    cbSize: UInt32
    dwVersion: UInt32
    isMultiSign: win32more.Foundation.BOOL
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        dwFlags: UInt32
        dwReserved: UInt32
class SIP_DISPATCH_INFO(Structure):
    cbSize: UInt32
    hSIP: win32more.Foundation.HANDLE
    pfGet: win32more.Security.Cryptography.Sip.pCryptSIPGetSignedDataMsg
    pfPut: win32more.Security.Cryptography.Sip.pCryptSIPPutSignedDataMsg
    pfCreate: win32more.Security.Cryptography.Sip.pCryptSIPCreateIndirectData
    pfVerify: win32more.Security.Cryptography.Sip.pCryptSIPVerifyIndirectData
    pfRemove: win32more.Security.Cryptography.Sip.pCryptSIPRemoveSignedDataMsg
class SIP_INDIRECT_DATA(Structure):
    Data: win32more.Security.Cryptography.CRYPT_ATTRIBUTE_TYPE_VALUE
    DigestAlgorithm: win32more.Security.Cryptography.CRYPT_ALGORITHM_IDENTIFIER
    Digest: win32more.Security.Cryptography.CRYPT_INTEGER_BLOB
class SIP_SUBJECTINFO(Structure):
    cbSize: UInt32
    pgSubjectType: POINTER(Guid)
    hFile: win32more.Foundation.HANDLE
    pwsFileName: win32more.Foundation.PWSTR
    pwsDisplayName: win32more.Foundation.PWSTR
    dwReserved1: UInt32
    dwIntVersion: UInt32
    hProv: UIntPtr
    DigestAlgorithm: win32more.Security.Cryptography.CRYPT_ALGORITHM_IDENTIFIER
    dwFlags: UInt32
    dwEncodingType: UInt32
    dwReserved2: UInt32
    fdwCAPISettings: UInt32
    fdwSecuritySettings: UInt32
    dwIndex: UInt32
    dwUnionChoice: UInt32
    Anonymous: _Anonymous_e__Union
    pClientData: c_void_p
    class _Anonymous_e__Union(Union):
        psFlat: POINTER(win32more.Security.Cryptography.Sip.MS_ADDINFO_FLAT_head)
        psCatMember: POINTER(win32more.Security.Cryptography.Catalog.MS_ADDINFO_CATALOGMEMBER_head)
        psBlob: POINTER(win32more.Security.Cryptography.Sip.MS_ADDINFO_BLOB_head)
make_head(_module, 'MS_ADDINFO_BLOB')
make_head(_module, 'MS_ADDINFO_FLAT')
make_head(_module, 'pCryptSIPCreateIndirectData')
make_head(_module, 'pCryptSIPGetCaps')
make_head(_module, 'pCryptSIPGetSealedDigest')
make_head(_module, 'pCryptSIPGetSignedDataMsg')
make_head(_module, 'pCryptSIPPutSignedDataMsg')
make_head(_module, 'pCryptSIPRemoveSignedDataMsg')
make_head(_module, 'pCryptSIPVerifyIndirectData')
make_head(_module, 'pfnIsFileSupported')
make_head(_module, 'pfnIsFileSupportedName')
make_head(_module, 'SIP_ADD_NEWPROVIDER')
make_head(_module, 'SIP_CAP_SET_V2')
make_head(_module, 'SIP_CAP_SET_V3')
make_head(_module, 'SIP_DISPATCH_INFO')
make_head(_module, 'SIP_INDIRECT_DATA')
make_head(_module, 'SIP_SUBJECTINFO')
__all__ = [
    "CryptSIPAddProvider",
    "CryptSIPCreateIndirectData",
    "CryptSIPGetCaps",
    "CryptSIPGetSealedDigest",
    "CryptSIPGetSignedDataMsg",
    "CryptSIPLoad",
    "CryptSIPPutSignedDataMsg",
    "CryptSIPRemoveProvider",
    "CryptSIPRemoveSignedDataMsg",
    "CryptSIPRetrieveSubjectGuid",
    "CryptSIPRetrieveSubjectGuidForCatalogFile",
    "CryptSIPVerifyIndirectData",
    "MSSIP_ADDINFO_BLOB",
    "MSSIP_ADDINFO_CATMEMBER",
    "MSSIP_ADDINFO_FLAT",
    "MSSIP_ADDINFO_NONE",
    "MSSIP_ADDINFO_NONMSSIP",
    "MSSIP_FLAGS_MULTI_HASH",
    "MSSIP_FLAGS_PROHIBIT_RESIZE_ON_CREATE",
    "MSSIP_FLAGS_USE_CATALOG",
    "MS_ADDINFO_BLOB",
    "MS_ADDINFO_FLAT",
    "SIP_ADD_NEWPROVIDER",
    "SIP_CAP_FLAG_SEALING",
    "SIP_CAP_SET_CUR_VER",
    "SIP_CAP_SET_V2",
    "SIP_CAP_SET_V3",
    "SIP_CAP_SET_VERSION_2",
    "SIP_CAP_SET_VERSION_3",
    "SIP_DISPATCH_INFO",
    "SIP_INDIRECT_DATA",
    "SIP_MAX_MAGIC_NUMBER",
    "SIP_SUBJECTINFO",
    "SPC_DIGEST_GENERATE_FLAG",
    "SPC_DIGEST_SIGN_EX_FLAG",
    "SPC_DIGEST_SIGN_FLAG",
    "SPC_EXC_PE_PAGE_HASHES_FLAG",
    "SPC_INC_PE_DEBUG_INFO_FLAG",
    "SPC_INC_PE_IMPORT_ADDR_TABLE_FLAG",
    "SPC_INC_PE_PAGE_HASHES_FLAG",
    "SPC_INC_PE_RESOURCES_FLAG",
    "SPC_MARKER_CHECK_CURRENTLY_SUPPORTED_FLAGS",
    "SPC_MARKER_CHECK_SKIP_SIP_INDIRECT_DATA_FLAG",
    "SPC_RELAXED_PE_MARKER_CHECK",
    "pCryptSIPCreateIndirectData",
    "pCryptSIPGetCaps",
    "pCryptSIPGetSealedDigest",
    "pCryptSIPGetSignedDataMsg",
    "pCryptSIPPutSignedDataMsg",
    "pCryptSIPRemoveSignedDataMsg",
    "pCryptSIPVerifyIndirectData",
    "pfnIsFileSupported",
    "pfnIsFileSupportedName",
]
_arch_optional = [
]
