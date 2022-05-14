from win32more import *
import win32more.Security.Cryptography.Sip
import win32more.Foundation
import win32more.Security.Cryptography
import win32more.Security.Cryptography.Catalog

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.Security.Cryptography.Sip, name, eval(f"_define_{name}()"))
    return getattr(win32more.Security.Cryptography.Sip, name)
MSSIP_FLAGS_PROHIBIT_RESIZE_ON_CREATE = 65536
MSSIP_FLAGS_USE_CATALOG = 131072
MSSIP_FLAGS_MULTI_HASH = 262144
SPC_INC_PE_RESOURCES_FLAG = 128
SPC_INC_PE_DEBUG_INFO_FLAG = 64
SPC_INC_PE_IMPORT_ADDR_TABLE_FLAG = 32
SPC_EXC_PE_PAGE_HASHES_FLAG = 16
SPC_INC_PE_PAGE_HASHES_FLAG = 256
SPC_DIGEST_GENERATE_FLAG = 512
SPC_DIGEST_SIGN_FLAG = 1024
SPC_DIGEST_SIGN_EX_FLAG = 16384
SPC_RELAXED_PE_MARKER_CHECK = 2048
SPC_MARKER_CHECK_SKIP_SIP_INDIRECT_DATA_FLAG = 1
SPC_MARKER_CHECK_CURRENTLY_SUPPORTED_FLAGS = 1
SIP_CAP_SET_VERSION_2 = 2
SIP_CAP_SET_VERSION_3 = 3
SIP_CAP_SET_CUR_VER = 3
SIP_CAP_FLAG_SEALING = 1
SIP_MAX_MAGIC_NUMBER = 4
def _define_SIP_SUBJECTINFO_head():
    class SIP_SUBJECTINFO(Structure):
        pass
    return SIP_SUBJECTINFO
def _define_SIP_SUBJECTINFO():
    SIP_SUBJECTINFO = win32more.Security.Cryptography.Sip.SIP_SUBJECTINFO_head
    class SIP_SUBJECTINFO__Anonymous_e__Union(Union):
        pass
    SIP_SUBJECTINFO__Anonymous_e__Union._fields_ = [
        ("psFlat", POINTER(win32more.Security.Cryptography.Sip.MS_ADDINFO_FLAT_head)),
        ("psCatMember", POINTER(win32more.Security.Cryptography.Sip.MS_ADDINFO_CATALOGMEMBER_head)),
        ("psBlob", POINTER(win32more.Security.Cryptography.Sip.MS_ADDINFO_BLOB_head)),
    ]
    SIP_SUBJECTINFO._anonymous_ = [
        'Anonymous',
    ]
    SIP_SUBJECTINFO._fields_ = [
        ("cbSize", UInt32),
        ("pgSubjectType", POINTER(Guid)),
        ("hFile", win32more.Foundation.HANDLE),
        ("pwsFileName", win32more.Foundation.PWSTR),
        ("pwsDisplayName", win32more.Foundation.PWSTR),
        ("dwReserved1", UInt32),
        ("dwIntVersion", UInt32),
        ("hProv", UIntPtr),
        ("DigestAlgorithm", win32more.Security.Cryptography.CRYPT_ALGORITHM_IDENTIFIER),
        ("dwFlags", UInt32),
        ("dwEncodingType", UInt32),
        ("dwReserved2", UInt32),
        ("fdwCAPISettings", UInt32),
        ("fdwSecuritySettings", UInt32),
        ("dwIndex", UInt32),
        ("dwUnionChoice", UInt32),
        ("Anonymous", SIP_SUBJECTINFO__Anonymous_e__Union),
        ("pClientData", c_void_p),
    ]
    return SIP_SUBJECTINFO
def _define_MS_ADDINFO_FLAT_head():
    class MS_ADDINFO_FLAT(Structure):
        pass
    return MS_ADDINFO_FLAT
def _define_MS_ADDINFO_FLAT():
    MS_ADDINFO_FLAT = win32more.Security.Cryptography.Sip.MS_ADDINFO_FLAT_head
    MS_ADDINFO_FLAT._fields_ = [
        ("cbStruct", UInt32),
        ("pIndirectData", POINTER(win32more.Security.Cryptography.Sip.SIP_INDIRECT_DATA_head)),
    ]
    return MS_ADDINFO_FLAT
def _define_MS_ADDINFO_CATALOGMEMBER_head():
    class MS_ADDINFO_CATALOGMEMBER(Structure):
        pass
    return MS_ADDINFO_CATALOGMEMBER
def _define_MS_ADDINFO_CATALOGMEMBER():
    MS_ADDINFO_CATALOGMEMBER = win32more.Security.Cryptography.Sip.MS_ADDINFO_CATALOGMEMBER_head
    MS_ADDINFO_CATALOGMEMBER._fields_ = [
        ("cbStruct", UInt32),
        ("pStore", POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATSTORE_head)),
        ("pMember", POINTER(win32more.Security.Cryptography.Catalog.CRYPTCATMEMBER_head)),
    ]
    return MS_ADDINFO_CATALOGMEMBER
def _define_MS_ADDINFO_BLOB_head():
    class MS_ADDINFO_BLOB(Structure):
        pass
    return MS_ADDINFO_BLOB
def _define_MS_ADDINFO_BLOB():
    MS_ADDINFO_BLOB = win32more.Security.Cryptography.Sip.MS_ADDINFO_BLOB_head
    MS_ADDINFO_BLOB._fields_ = [
        ("cbStruct", UInt32),
        ("cbMemObject", UInt32),
        ("pbMemObject", c_char_p_no),
        ("cbMemSignedMsg", UInt32),
        ("pbMemSignedMsg", c_char_p_no),
    ]
    return MS_ADDINFO_BLOB
def _define_SIP_CAP_SET_V2_head():
    class SIP_CAP_SET_V2(Structure):
        pass
    return SIP_CAP_SET_V2
def _define_SIP_CAP_SET_V2():
    SIP_CAP_SET_V2 = win32more.Security.Cryptography.Sip.SIP_CAP_SET_V2_head
    SIP_CAP_SET_V2._fields_ = [
        ("cbSize", UInt32),
        ("dwVersion", UInt32),
        ("isMultiSign", win32more.Foundation.BOOL),
        ("dwReserved", UInt32),
    ]
    return SIP_CAP_SET_V2
def _define_SIP_CAP_SET_V3_head():
    class SIP_CAP_SET_V3(Structure):
        pass
    return SIP_CAP_SET_V3
def _define_SIP_CAP_SET_V3():
    SIP_CAP_SET_V3 = win32more.Security.Cryptography.Sip.SIP_CAP_SET_V3_head
    class SIP_CAP_SET_V3__Anonymous_e__Union(Union):
        pass
    SIP_CAP_SET_V3__Anonymous_e__Union._fields_ = [
        ("dwFlags", UInt32),
        ("dwReserved", UInt32),
    ]
    SIP_CAP_SET_V3._anonymous_ = [
        'Anonymous',
    ]
    SIP_CAP_SET_V3._fields_ = [
        ("cbSize", UInt32),
        ("dwVersion", UInt32),
        ("isMultiSign", win32more.Foundation.BOOL),
        ("Anonymous", SIP_CAP_SET_V3__Anonymous_e__Union),
    ]
    return SIP_CAP_SET_V3
def _define_SIP_INDIRECT_DATA_head():
    class SIP_INDIRECT_DATA(Structure):
        pass
    return SIP_INDIRECT_DATA
def _define_SIP_INDIRECT_DATA():
    SIP_INDIRECT_DATA = win32more.Security.Cryptography.Sip.SIP_INDIRECT_DATA_head
    SIP_INDIRECT_DATA._fields_ = [
        ("Data", win32more.Security.Cryptography.CRYPT_ATTRIBUTE_TYPE_VALUE),
        ("DigestAlgorithm", win32more.Security.Cryptography.CRYPT_ALGORITHM_IDENTIFIER),
        ("Digest", win32more.Security.Cryptography.CRYPTOAPI_BLOB),
    ]
    return SIP_INDIRECT_DATA
def _define_pCryptSIPGetSignedDataMsg():
    return CFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.Cryptography.Sip.SIP_SUBJECTINFO_head),POINTER(UInt32),UInt32,POINTER(UInt32),c_char_p_no, use_last_error=False)
def _define_pCryptSIPPutSignedDataMsg():
    return CFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.Cryptography.Sip.SIP_SUBJECTINFO_head),UInt32,POINTER(UInt32),UInt32,c_char_p_no, use_last_error=False)
def _define_pCryptSIPCreateIndirectData():
    return CFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.Cryptography.Sip.SIP_SUBJECTINFO_head),POINTER(UInt32),POINTER(win32more.Security.Cryptography.Sip.SIP_INDIRECT_DATA_head), use_last_error=False)
def _define_pCryptSIPVerifyIndirectData():
    return CFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.Cryptography.Sip.SIP_SUBJECTINFO_head),POINTER(win32more.Security.Cryptography.Sip.SIP_INDIRECT_DATA_head), use_last_error=False)
def _define_pCryptSIPRemoveSignedDataMsg():
    return CFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.Cryptography.Sip.SIP_SUBJECTINFO_head),UInt32, use_last_error=False)
def _define_SIP_DISPATCH_INFO_head():
    class SIP_DISPATCH_INFO(Structure):
        pass
    return SIP_DISPATCH_INFO
def _define_SIP_DISPATCH_INFO():
    SIP_DISPATCH_INFO = win32more.Security.Cryptography.Sip.SIP_DISPATCH_INFO_head
    SIP_DISPATCH_INFO._fields_ = [
        ("cbSize", UInt32),
        ("hSIP", win32more.Foundation.HANDLE),
        ("pfGet", win32more.Security.Cryptography.Sip.pCryptSIPGetSignedDataMsg),
        ("pfPut", win32more.Security.Cryptography.Sip.pCryptSIPPutSignedDataMsg),
        ("pfCreate", win32more.Security.Cryptography.Sip.pCryptSIPCreateIndirectData),
        ("pfVerify", win32more.Security.Cryptography.Sip.pCryptSIPVerifyIndirectData),
        ("pfRemove", win32more.Security.Cryptography.Sip.pCryptSIPRemoveSignedDataMsg),
    ]
    return SIP_DISPATCH_INFO
def _define_pfnIsFileSupported():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(Guid), use_last_error=False)
def _define_pfnIsFileSupportedName():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,POINTER(Guid), use_last_error=False)
def _define_SIP_ADD_NEWPROVIDER_head():
    class SIP_ADD_NEWPROVIDER(Structure):
        pass
    return SIP_ADD_NEWPROVIDER
def _define_SIP_ADD_NEWPROVIDER():
    SIP_ADD_NEWPROVIDER = win32more.Security.Cryptography.Sip.SIP_ADD_NEWPROVIDER_head
    SIP_ADD_NEWPROVIDER._fields_ = [
        ("cbStruct", UInt32),
        ("pgSubject", POINTER(Guid)),
        ("pwszDLLFileName", win32more.Foundation.PWSTR),
        ("pwszMagicNumber", win32more.Foundation.PWSTR),
        ("pwszIsFunctionName", win32more.Foundation.PWSTR),
        ("pwszGetFuncName", win32more.Foundation.PWSTR),
        ("pwszPutFuncName", win32more.Foundation.PWSTR),
        ("pwszCreateFuncName", win32more.Foundation.PWSTR),
        ("pwszVerifyFuncName", win32more.Foundation.PWSTR),
        ("pwszRemoveFuncName", win32more.Foundation.PWSTR),
        ("pwszIsFunctionNameFmt2", win32more.Foundation.PWSTR),
        ("pwszGetCapFuncName", win32more.Foundation.PWSTR),
    ]
    return SIP_ADD_NEWPROVIDER
def _define_pCryptSIPGetCaps():
    return CFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.Cryptography.Sip.SIP_SUBJECTINFO_head),POINTER(win32more.Security.Cryptography.Sip.SIP_CAP_SET_V3_head), use_last_error=False)
def _define_pCryptSIPGetSealedDigest():
    return CFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.Cryptography.Sip.SIP_SUBJECTINFO_head),POINTER(Byte),UInt32,POINTER(Byte),POINTER(UInt32), use_last_error=False)
def _define_CryptSIPGetSignedDataMsg():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.Cryptography.Sip.SIP_SUBJECTINFO_head),POINTER(win32more.Security.Cryptography.CERT_QUERY_ENCODING_TYPE),UInt32,POINTER(UInt32),c_char_p_no, use_last_error=True)(("CryptSIPGetSignedDataMsg", windll["WINTRUST"]), ((1, 'pSubjectInfo'),(1, 'pdwEncodingType'),(1, 'dwIndex'),(1, 'pcbSignedDataMsg'),(1, 'pbSignedDataMsg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptSIPPutSignedDataMsg():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.Cryptography.Sip.SIP_SUBJECTINFO_head),win32more.Security.Cryptography.CERT_QUERY_ENCODING_TYPE,POINTER(UInt32),UInt32,c_char_p_no, use_last_error=True)(("CryptSIPPutSignedDataMsg", windll["WINTRUST"]), ((1, 'pSubjectInfo'),(1, 'dwEncodingType'),(1, 'pdwIndex'),(1, 'cbSignedDataMsg'),(1, 'pbSignedDataMsg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptSIPCreateIndirectData():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.Cryptography.Sip.SIP_SUBJECTINFO_head),POINTER(UInt32),POINTER(win32more.Security.Cryptography.Sip.SIP_INDIRECT_DATA_head), use_last_error=True)(("CryptSIPCreateIndirectData", windll["WINTRUST"]), ((1, 'pSubjectInfo'),(1, 'pcbIndirectData'),(1, 'pIndirectData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptSIPVerifyIndirectData():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.Cryptography.Sip.SIP_SUBJECTINFO_head),POINTER(win32more.Security.Cryptography.Sip.SIP_INDIRECT_DATA_head), use_last_error=True)(("CryptSIPVerifyIndirectData", windll["WINTRUST"]), ((1, 'pSubjectInfo'),(1, 'pIndirectData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptSIPRemoveSignedDataMsg():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.Cryptography.Sip.SIP_SUBJECTINFO_head),UInt32, use_last_error=True)(("CryptSIPRemoveSignedDataMsg", windll["WINTRUST"]), ((1, 'pSubjectInfo'),(1, 'dwIndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptSIPLoad():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(Guid),UInt32,POINTER(win32more.Security.Cryptography.Sip.SIP_DISPATCH_INFO_head), use_last_error=True)(("CryptSIPLoad", windll["CRYPT32"]), ((1, 'pgSubject'),(1, 'dwFlags'),(1, 'pSipDispatch'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptSIPRetrieveSubjectGuid():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.HANDLE,POINTER(Guid), use_last_error=True)(("CryptSIPRetrieveSubjectGuid", windll["CRYPT32"]), ((1, 'FileName'),(1, 'hFileIn'),(1, 'pgSubject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptSIPRetrieveSubjectGuidForCatalogFile():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.HANDLE,POINTER(Guid), use_last_error=True)(("CryptSIPRetrieveSubjectGuidForCatalogFile", windll["CRYPT32"]), ((1, 'FileName'),(1, 'hFileIn'),(1, 'pgSubject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptSIPAddProvider():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.Cryptography.Sip.SIP_ADD_NEWPROVIDER_head), use_last_error=True)(("CryptSIPAddProvider", windll["CRYPT32"]), ((1, 'psNewProv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptSIPRemoveProvider():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(Guid), use_last_error=True)(("CryptSIPRemoveProvider", windll["CRYPT32"]), ((1, 'pgProv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptSIPGetCaps():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.Cryptography.Sip.SIP_SUBJECTINFO_head),POINTER(win32more.Security.Cryptography.Sip.SIP_CAP_SET_V3_head), use_last_error=False)(("CryptSIPGetCaps", windll["WINTRUST"]), ((1, 'pSubjInfo'),(1, 'pCaps'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CryptSIPGetSealedDigest():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.Cryptography.Sip.SIP_SUBJECTINFO_head),POINTER(Byte),UInt32,POINTER(Byte),POINTER(UInt32), use_last_error=False)(("CryptSIPGetSealedDigest", windll["WINTRUST"]), ((1, 'pSubjectInfo'),(1, 'pSig'),(1, 'dwSig'),(1, 'pbDigest'),(1, 'pcbDigest'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "MSSIP_FLAGS_PROHIBIT_RESIZE_ON_CREATE",
    "MSSIP_FLAGS_USE_CATALOG",
    "MSSIP_FLAGS_MULTI_HASH",
    "SPC_INC_PE_RESOURCES_FLAG",
    "SPC_INC_PE_DEBUG_INFO_FLAG",
    "SPC_INC_PE_IMPORT_ADDR_TABLE_FLAG",
    "SPC_EXC_PE_PAGE_HASHES_FLAG",
    "SPC_INC_PE_PAGE_HASHES_FLAG",
    "SPC_DIGEST_GENERATE_FLAG",
    "SPC_DIGEST_SIGN_FLAG",
    "SPC_DIGEST_SIGN_EX_FLAG",
    "SPC_RELAXED_PE_MARKER_CHECK",
    "SPC_MARKER_CHECK_SKIP_SIP_INDIRECT_DATA_FLAG",
    "SPC_MARKER_CHECK_CURRENTLY_SUPPORTED_FLAGS",
    "SIP_CAP_SET_VERSION_2",
    "SIP_CAP_SET_VERSION_3",
    "SIP_CAP_SET_CUR_VER",
    "SIP_CAP_FLAG_SEALING",
    "SIP_MAX_MAGIC_NUMBER",
    "SIP_SUBJECTINFO",
    "MS_ADDINFO_FLAT",
    "MS_ADDINFO_CATALOGMEMBER",
    "MS_ADDINFO_BLOB",
    "SIP_CAP_SET_V2",
    "SIP_CAP_SET_V3",
    "SIP_INDIRECT_DATA",
    "pCryptSIPGetSignedDataMsg",
    "pCryptSIPPutSignedDataMsg",
    "pCryptSIPCreateIndirectData",
    "pCryptSIPVerifyIndirectData",
    "pCryptSIPRemoveSignedDataMsg",
    "SIP_DISPATCH_INFO",
    "pfnIsFileSupported",
    "pfnIsFileSupportedName",
    "SIP_ADD_NEWPROVIDER",
    "pCryptSIPGetCaps",
    "pCryptSIPGetSealedDigest",
    "CryptSIPGetSignedDataMsg",
    "CryptSIPPutSignedDataMsg",
    "CryptSIPCreateIndirectData",
    "CryptSIPVerifyIndirectData",
    "CryptSIPRemoveSignedDataMsg",
    "CryptSIPLoad",
    "CryptSIPRetrieveSubjectGuid",
    "CryptSIPRetrieveSubjectGuidForCatalogFile",
    "CryptSIPAddProvider",
    "CryptSIPRemoveProvider",
    "CryptSIPGetCaps",
    "CryptSIPGetSealedDigest",
]
