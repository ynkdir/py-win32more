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
def CryptSIPGetSignedDataMsg(pSubjectInfo: POINTER(Windows.Win32.Security.Cryptography.Sip.SIP_SUBJECTINFO_head), pdwEncodingType: POINTER(Windows.Win32.Security.Cryptography.CERT_QUERY_ENCODING_TYPE), dwIndex: UInt32, pcbSignedDataMsg: POINTER(UInt32), pbSignedDataMsg: POINTER(Byte)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINTRUST.dll')
def CryptSIPPutSignedDataMsg(pSubjectInfo: POINTER(Windows.Win32.Security.Cryptography.Sip.SIP_SUBJECTINFO_head), dwEncodingType: Windows.Win32.Security.Cryptography.CERT_QUERY_ENCODING_TYPE, pdwIndex: POINTER(UInt32), cbSignedDataMsg: UInt32, pbSignedDataMsg: POINTER(Byte)) -> Windows.Win32.Foundation.BOOL: ...
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
def CryptSIPGetSealedDigest(pSubjectInfo: POINTER(Windows.Win32.Security.Cryptography.Sip.SIP_SUBJECTINFO_head), pSig: POINTER(Byte), dwSig: UInt32, pbDigest: POINTER(Byte), pcbDigest: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
class MS_ADDINFO_BLOB(EasyCastStructure):
    cbStruct: UInt32
    cbMemObject: UInt32
    pbMemObject: POINTER(Byte)
    cbMemSignedMsg: UInt32
    pbMemSignedMsg: POINTER(Byte)
class MS_ADDINFO_FLAT(EasyCastStructure):
    cbStruct: UInt32
    pIndirectData: POINTER(Windows.Win32.Security.Cryptography.Sip.SIP_INDIRECT_DATA_head)
class SIP_ADD_NEWPROVIDER(EasyCastStructure):
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
class SIP_CAP_SET_V2(EasyCastStructure):
    cbSize: UInt32
    dwVersion: UInt32
    isMultiSign: Windows.Win32.Foundation.BOOL
    dwReserved: UInt32
class SIP_CAP_SET_V3(EasyCastStructure):
    cbSize: UInt32
    dwVersion: UInt32
    isMultiSign: Windows.Win32.Foundation.BOOL
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        dwFlags: UInt32
        dwReserved: UInt32
class SIP_DISPATCH_INFO(EasyCastStructure):
    cbSize: UInt32
    hSIP: Windows.Win32.Foundation.HANDLE
    pfGet: Windows.Win32.Security.Cryptography.Sip.pCryptSIPGetSignedDataMsg
    pfPut: Windows.Win32.Security.Cryptography.Sip.pCryptSIPPutSignedDataMsg
    pfCreate: Windows.Win32.Security.Cryptography.Sip.pCryptSIPCreateIndirectData
    pfVerify: Windows.Win32.Security.Cryptography.Sip.pCryptSIPVerifyIndirectData
    pfRemove: Windows.Win32.Security.Cryptography.Sip.pCryptSIPRemoveSignedDataMsg
class SIP_INDIRECT_DATA(EasyCastStructure):
    Data: Windows.Win32.Security.Cryptography.CRYPT_ATTRIBUTE_TYPE_VALUE
    DigestAlgorithm: Windows.Win32.Security.Cryptography.CRYPT_ALGORITHM_IDENTIFIER
    Digest: Windows.Win32.Security.Cryptography.CRYPT_INTEGER_BLOB
class SIP_SUBJECTINFO(EasyCastStructure):
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
    class _Anonymous_e__Union(EasyCastUnion):
        psFlat: POINTER(Windows.Win32.Security.Cryptography.Sip.MS_ADDINFO_FLAT_head)
        psCatMember: POINTER(Windows.Win32.Security.Cryptography.Catalog.MS_ADDINFO_CATALOGMEMBER_head)
        psBlob: POINTER(Windows.Win32.Security.Cryptography.Sip.MS_ADDINFO_BLOB_head)
@winfunctype_pointer
def pCryptSIPCreateIndirectData(pSubjectInfo: POINTER(Windows.Win32.Security.Cryptography.Sip.SIP_SUBJECTINFO_head), pcbIndirectData: POINTER(UInt32), pIndirectData: POINTER(Windows.Win32.Security.Cryptography.Sip.SIP_INDIRECT_DATA_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def pCryptSIPGetCaps(pSubjInfo: POINTER(Windows.Win32.Security.Cryptography.Sip.SIP_SUBJECTINFO_head), pCaps: POINTER(Windows.Win32.Security.Cryptography.Sip.SIP_CAP_SET_V3_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def pCryptSIPGetSealedDigest(pSubjectInfo: POINTER(Windows.Win32.Security.Cryptography.Sip.SIP_SUBJECTINFO_head), pSig: POINTER(Byte), dwSig: UInt32, pbDigest: POINTER(Byte), pcbDigest: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def pCryptSIPGetSignedDataMsg(pSubjectInfo: POINTER(Windows.Win32.Security.Cryptography.Sip.SIP_SUBJECTINFO_head), pdwEncodingType: POINTER(UInt32), dwIndex: UInt32, pcbSignedDataMsg: POINTER(UInt32), pbSignedDataMsg: POINTER(Byte)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def pCryptSIPPutSignedDataMsg(pSubjectInfo: POINTER(Windows.Win32.Security.Cryptography.Sip.SIP_SUBJECTINFO_head), dwEncodingType: UInt32, pdwIndex: POINTER(UInt32), cbSignedDataMsg: UInt32, pbSignedDataMsg: POINTER(Byte)) -> Windows.Win32.Foundation.BOOL: ...
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
