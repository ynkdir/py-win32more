from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
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
def CryptSIPGetSignedDataMsg(pSubjectInfo: POINTER(Windows.Win32.Security.Cryptography.Sip.SIP_SUBJECTINFO_head), pdwEncodingType: POINTER(Windows.Win32.Security.Cryptography.CERT_QUERY_ENCODING_TYPE), dwIndex: UInt32, pcbSignedDataMsg: POINTER(UInt32), pbSignedDataMsg: c_char_p_no) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptSIPPutSignedDataMsg(pSubjectInfo: POINTER(Windows.Win32.Security.Cryptography.Sip.SIP_SUBJECTINFO_head), dwEncodingType: Windows.Win32.Security.Cryptography.CERT_QUERY_ENCODING_TYPE, pdwIndex: POINTER(UInt32), cbSignedDataMsg: UInt32, pbSignedDataMsg: c_char_p_no) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptSIPCreateIndirectData(pSubjectInfo: POINTER(Windows.Win32.Security.Cryptography.Sip.SIP_SUBJECTINFO_head), pcbIndirectData: POINTER(UInt32), pIndirectData: POINTER(Windows.Win32.Security.Cryptography.Sip.SIP_INDIRECT_DATA_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptSIPVerifyIndirectData(pSubjectInfo: POINTER(Windows.Win32.Security.Cryptography.Sip.SIP_SUBJECTINFO_head), pIndirectData: POINTER(Windows.Win32.Security.Cryptography.Sip.SIP_INDIRECT_DATA_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptSIPRemoveSignedDataMsg(pSubjectInfo: POINTER(Windows.Win32.Security.Cryptography.Sip.SIP_SUBJECTINFO_head), dwIndex: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('CRYPT32.dll')
def CryptSIPLoad(pgSubject: POINTER(Guid), dwFlags: UInt32, pSipDispatch: POINTER(Windows.Win32.Security.Cryptography.Sip.SIP_DISPATCH_INFO_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('CRYPT32.dll')
def CryptSIPRetrieveSubjectGuid(FileName: Windows.Win32.Foundation.PWSTR, hFileIn: Windows.Win32.Foundation.HANDLE, pgSubject: POINTER(Guid)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('CRYPT32.dll')
def CryptSIPRetrieveSubjectGuidForCatalogFile(FileName: Windows.Win32.Foundation.PWSTR, hFileIn: Windows.Win32.Foundation.HANDLE, pgSubject: POINTER(Guid)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('CRYPT32.dll')
def CryptSIPAddProvider(psNewProv: POINTER(Windows.Win32.Security.Cryptography.Sip.SIP_ADD_NEWPROVIDER_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('CRYPT32.dll')
def CryptSIPRemoveProvider(pgProv: POINTER(Guid)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptSIPGetCaps(pSubjInfo: POINTER(Windows.Win32.Security.Cryptography.Sip.SIP_SUBJECTINFO_head), pCaps: POINTER(Windows.Win32.Security.Cryptography.Sip.SIP_CAP_SET_V3_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptSIPGetSealedDigest(pSubjectInfo: POINTER(Windows.Win32.Security.Cryptography.Sip.SIP_SUBJECTINFO_head), pSig: c_char_p_no, dwSig: UInt32, pbDigest: c_char_p_no, pcbDigest: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
class MS_ADDINFO_BLOB(Structure):
    cbStruct: UInt32
    cbMemObject: UInt32
    pbMemObject: c_char_p_no
    cbMemSignedMsg: UInt32
    pbMemSignedMsg: c_char_p_no
class MS_ADDINFO_FLAT(Structure):
    cbStruct: UInt32
    pIndirectData: POINTER(Windows.Win32.Security.Cryptography.Sip.SIP_INDIRECT_DATA_head)
class SIP_ADD_NEWPROVIDER(Structure):
    cbStruct: UInt32
    pgSubject: POINTER(Guid)
    pwszDLLFileName: Windows.Win32.Foundation.PWSTR
    pwszMagicNumber: Windows.Win32.Foundation.PWSTR
    pwszIsFunctionName: Windows.Win32.Foundation.PWSTR
    pwszGetFuncName: Windows.Win32.Foundation.PWSTR
    pwszPutFuncName: Windows.Win32.Foundation.PWSTR
    pwszCreateFuncName: Windows.Win32.Foundation.PWSTR
    pwszVerifyFuncName: Windows.Win32.Foundation.PWSTR
    pwszRemoveFuncName: Windows.Win32.Foundation.PWSTR
    pwszIsFunctionNameFmt2: Windows.Win32.Foundation.PWSTR
    pwszGetCapFuncName: Windows.Win32.Foundation.PWSTR
class SIP_CAP_SET_V2(Structure):
    cbSize: UInt32
    dwVersion: UInt32
    isMultiSign: Windows.Win32.Foundation.BOOL
    dwReserved: UInt32
class SIP_CAP_SET_V3(Structure):
    cbSize: UInt32
    dwVersion: UInt32
    isMultiSign: Windows.Win32.Foundation.BOOL
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        dwFlags: UInt32
        dwReserved: UInt32
class SIP_DISPATCH_INFO(Structure):
    cbSize: UInt32
    hSIP: Windows.Win32.Foundation.HANDLE
    pfGet: Windows.Win32.Security.Cryptography.Sip.pCryptSIPGetSignedDataMsg
    pfPut: Windows.Win32.Security.Cryptography.Sip.pCryptSIPPutSignedDataMsg
    pfCreate: Windows.Win32.Security.Cryptography.Sip.pCryptSIPCreateIndirectData
    pfVerify: Windows.Win32.Security.Cryptography.Sip.pCryptSIPVerifyIndirectData
    pfRemove: Windows.Win32.Security.Cryptography.Sip.pCryptSIPRemoveSignedDataMsg
class SIP_INDIRECT_DATA(Structure):
    Data: Windows.Win32.Security.Cryptography.CRYPT_ATTRIBUTE_TYPE_VALUE
    DigestAlgorithm: Windows.Win32.Security.Cryptography.CRYPT_ALGORITHM_IDENTIFIER
    Digest: Windows.Win32.Security.Cryptography.CRYPT_INTEGER_BLOB
class SIP_SUBJECTINFO(Structure):
    cbSize: UInt32
    pgSubjectType: POINTER(Guid)
    hFile: Windows.Win32.Foundation.HANDLE
    pwsFileName: Windows.Win32.Foundation.PWSTR
    pwsDisplayName: Windows.Win32.Foundation.PWSTR
    dwReserved1: UInt32
    dwIntVersion: UInt32
    hProv: UIntPtr
    DigestAlgorithm: Windows.Win32.Security.Cryptography.CRYPT_ALGORITHM_IDENTIFIER
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
        psFlat: POINTER(Windows.Win32.Security.Cryptography.Sip.MS_ADDINFO_FLAT_head)
        psCatMember: POINTER(Windows.Win32.Security.Cryptography.Catalog.MS_ADDINFO_CATALOGMEMBER_head)
        psBlob: POINTER(Windows.Win32.Security.Cryptography.Sip.MS_ADDINFO_BLOB_head)
@winfunctype_pointer
def pCryptSIPCreateIndirectData(pSubjectInfo: POINTER(Windows.Win32.Security.Cryptography.Sip.SIP_SUBJECTINFO_head), pcbIndirectData: POINTER(UInt32), pIndirectData: POINTER(Windows.Win32.Security.Cryptography.Sip.SIP_INDIRECT_DATA_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def pCryptSIPGetCaps(pSubjInfo: POINTER(Windows.Win32.Security.Cryptography.Sip.SIP_SUBJECTINFO_head), pCaps: POINTER(Windows.Win32.Security.Cryptography.Sip.SIP_CAP_SET_V3_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def pCryptSIPGetSealedDigest(pSubjectInfo: POINTER(Windows.Win32.Security.Cryptography.Sip.SIP_SUBJECTINFO_head), pSig: c_char_p_no, dwSig: UInt32, pbDigest: c_char_p_no, pcbDigest: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def pCryptSIPGetSignedDataMsg(pSubjectInfo: POINTER(Windows.Win32.Security.Cryptography.Sip.SIP_SUBJECTINFO_head), pdwEncodingType: POINTER(UInt32), dwIndex: UInt32, pcbSignedDataMsg: POINTER(UInt32), pbSignedDataMsg: c_char_p_no) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def pCryptSIPPutSignedDataMsg(pSubjectInfo: POINTER(Windows.Win32.Security.Cryptography.Sip.SIP_SUBJECTINFO_head), dwEncodingType: UInt32, pdwIndex: POINTER(UInt32), cbSignedDataMsg: UInt32, pbSignedDataMsg: c_char_p_no) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def pCryptSIPRemoveSignedDataMsg(pSubjectInfo: POINTER(Windows.Win32.Security.Cryptography.Sip.SIP_SUBJECTINFO_head), dwIndex: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def pCryptSIPVerifyIndirectData(pSubjectInfo: POINTER(Windows.Win32.Security.Cryptography.Sip.SIP_SUBJECTINFO_head), pIndirectData: POINTER(Windows.Win32.Security.Cryptography.Sip.SIP_INDIRECT_DATA_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def pfnIsFileSupported(hFile: Windows.Win32.Foundation.HANDLE, pgSubject: POINTER(Guid)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def pfnIsFileSupportedName(pwszFileName: Windows.Win32.Foundation.PWSTR, pgSubject: POINTER(Guid)) -> Windows.Win32.Foundation.BOOL: ...
make_head(_module, 'MS_ADDINFO_BLOB')
make_head(_module, 'MS_ADDINFO_FLAT')
make_head(_module, 'SIP_ADD_NEWPROVIDER')
make_head(_module, 'SIP_CAP_SET_V2')
make_head(_module, 'SIP_CAP_SET_V3')
make_head(_module, 'SIP_DISPATCH_INFO')
make_head(_module, 'SIP_INDIRECT_DATA')
make_head(_module, 'SIP_SUBJECTINFO')
make_head(_module, 'pCryptSIPCreateIndirectData')
make_head(_module, 'pCryptSIPGetCaps')
make_head(_module, 'pCryptSIPGetSealedDigest')
make_head(_module, 'pCryptSIPGetSignedDataMsg')
make_head(_module, 'pCryptSIPPutSignedDataMsg')
make_head(_module, 'pCryptSIPRemoveSignedDataMsg')
make_head(_module, 'pCryptSIPVerifyIndirectData')
make_head(_module, 'pfnIsFileSupported')
make_head(_module, 'pfnIsFileSupportedName')
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
