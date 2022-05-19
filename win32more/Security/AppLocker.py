from win32more import *
import win32more.Foundation
import win32more.Security
import win32more.Security.AppLocker

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
SAFER_SCOPEID_MACHINE = 1
SAFER_SCOPEID_USER = 2
SAFER_LEVELID_FULLYTRUSTED = 262144
SAFER_LEVELID_NORMALUSER = 131072
SAFER_LEVELID_CONSTRAINED = 65536
SAFER_LEVELID_UNTRUSTED = 4096
SAFER_LEVELID_DISALLOWED = 0
SAFER_LEVEL_OPEN = 1
SAFER_MAX_FRIENDLYNAME_SIZE = 256
SAFER_MAX_DESCRIPTION_SIZE = 256
SAFER_MAX_HASH_SIZE = 64
SAFER_CRITERIA_IMAGEPATH = 1
SAFER_CRITERIA_NOSIGNEDHASH = 2
SAFER_CRITERIA_IMAGEHASH = 4
SAFER_CRITERIA_AUTHENTICODE = 8
SAFER_CRITERIA_URLZONE = 16
SAFER_CRITERIA_APPX_PACKAGE = 32
SAFER_CRITERIA_IMAGEPATH_NT = 4096
SAFER_POLICY_JOBID_MASK = 4278190080
SAFER_POLICY_JOBID_CONSTRAINED = 67108864
SAFER_POLICY_JOBID_UNTRUSTED = 50331648
SAFER_POLICY_ONLY_EXES = 65536
SAFER_POLICY_SANDBOX_INERT = 131072
SAFER_POLICY_HASH_DUPLICATE = 262144
SAFER_POLICY_ONLY_AUDIT = 4096
SAFER_POLICY_BLOCK_CLIENT_UI = 8192
SAFER_POLICY_UIFLAGS_MASK = 255
SAFER_POLICY_UIFLAGS_INFORMATION_PROMPT = 1
SAFER_POLICY_UIFLAGS_OPTION_PROMPT = 2
SAFER_POLICY_UIFLAGS_HIDDEN = 4
SAFER_COMPUTE_TOKEN_FROM_LEVEL_FLAGS = UInt32
SAFER_TOKEN_NULL_IF_EQUAL = 1
SAFER_TOKEN_COMPARE_ONLY = 2
SAFER_TOKEN_MAKE_INERT = 4
SAFER_TOKEN_WANT_FLAGS = 8
def _define_SAFER_CODE_PROPERTIES_V1_head():
    class SAFER_CODE_PROPERTIES_V1(Structure):
        pass
    return SAFER_CODE_PROPERTIES_V1
def _define_SAFER_CODE_PROPERTIES_V1():
    SAFER_CODE_PROPERTIES_V1 = win32more.Security.AppLocker.SAFER_CODE_PROPERTIES_V1_head
    SAFER_CODE_PROPERTIES_V1._fields_ = [
        ("cbSize", UInt32),
        ("dwCheckFlags", UInt32),
        ("ImagePath", win32more.Foundation.PWSTR),
        ("hImageFileHandle", win32more.Foundation.HANDLE),
        ("UrlZoneId", UInt32),
        ("ImageHash", Byte * 64),
        ("dwImageHashSize", UInt32),
        ("ImageSize", win32more.Foundation.LARGE_INTEGER),
        ("HashAlgorithm", UInt32),
        ("pByteBlock", c_char_p_no),
        ("hWndParent", win32more.Foundation.HWND),
        ("dwWVTUIChoice", UInt32),
    ]
    return SAFER_CODE_PROPERTIES_V1
def _define_SAFER_CODE_PROPERTIES_V2_head():
    class SAFER_CODE_PROPERTIES_V2(Structure):
        pass
    return SAFER_CODE_PROPERTIES_V2
def _define_SAFER_CODE_PROPERTIES_V2():
    SAFER_CODE_PROPERTIES_V2 = win32more.Security.AppLocker.SAFER_CODE_PROPERTIES_V2_head
    SAFER_CODE_PROPERTIES_V2._fields_ = [
        ("cbSize", UInt32),
        ("dwCheckFlags", UInt32),
        ("ImagePath", win32more.Foundation.PWSTR),
        ("hImageFileHandle", win32more.Foundation.HANDLE),
        ("UrlZoneId", UInt32),
        ("ImageHash", Byte * 64),
        ("dwImageHashSize", UInt32),
        ("ImageSize", win32more.Foundation.LARGE_INTEGER),
        ("HashAlgorithm", UInt32),
        ("pByteBlock", c_char_p_no),
        ("hWndParent", win32more.Foundation.HWND),
        ("dwWVTUIChoice", UInt32),
        ("PackageMoniker", win32more.Foundation.PWSTR),
        ("PackagePublisher", win32more.Foundation.PWSTR),
        ("PackageName", win32more.Foundation.PWSTR),
        ("PackageVersion", UInt64),
        ("PackageIsFramework", win32more.Foundation.BOOL),
    ]
    return SAFER_CODE_PROPERTIES_V2
SAFER_POLICY_INFO_CLASS = Int32
SAFER_POLICY_INFO_CLASS_SaferPolicyLevelList = 1
SAFER_POLICY_INFO_CLASS_SaferPolicyEnableTransparentEnforcement = 2
SAFER_POLICY_INFO_CLASS_SaferPolicyDefaultLevel = 3
SAFER_POLICY_INFO_CLASS_SaferPolicyEvaluateUserScope = 4
SAFER_POLICY_INFO_CLASS_SaferPolicyScopeFlags = 5
SAFER_POLICY_INFO_CLASS_SaferPolicyDefaultLevelFlags = 6
SAFER_POLICY_INFO_CLASS_SaferPolicyAuthenticodeEnabled = 7
SAFER_OBJECT_INFO_CLASS = Int32
SAFER_OBJECT_INFO_CLASS_SaferObjectLevelId = 1
SAFER_OBJECT_INFO_CLASS_SaferObjectScopeId = 2
SAFER_OBJECT_INFO_CLASS_SaferObjectFriendlyName = 3
SAFER_OBJECT_INFO_CLASS_SaferObjectDescription = 4
SAFER_OBJECT_INFO_CLASS_SaferObjectBuiltin = 5
SAFER_OBJECT_INFO_CLASS_SaferObjectDisallowed = 6
SAFER_OBJECT_INFO_CLASS_SaferObjectDisableMaxPrivilege = 7
SAFER_OBJECT_INFO_CLASS_SaferObjectInvertDeletedPrivileges = 8
SAFER_OBJECT_INFO_CLASS_SaferObjectDeletedPrivileges = 9
SAFER_OBJECT_INFO_CLASS_SaferObjectDefaultOwner = 10
SAFER_OBJECT_INFO_CLASS_SaferObjectSidsToDisable = 11
SAFER_OBJECT_INFO_CLASS_SaferObjectRestrictedSidsInverted = 12
SAFER_OBJECT_INFO_CLASS_SaferObjectRestrictedSidsAdded = 13
SAFER_OBJECT_INFO_CLASS_SaferObjectAllIdentificationGuids = 14
SAFER_OBJECT_INFO_CLASS_SaferObjectSingleIdentification = 15
SAFER_OBJECT_INFO_CLASS_SaferObjectExtendedError = 16
SAFER_IDENTIFICATION_TYPES = Int32
SAFER_IDENTIFICATION_TYPES_SaferIdentityDefault = 0
SAFER_IDENTIFICATION_TYPES_SaferIdentityTypeImageName = 1
SAFER_IDENTIFICATION_TYPES_SaferIdentityTypeImageHash = 2
SAFER_IDENTIFICATION_TYPES_SaferIdentityTypeUrlZone = 3
SAFER_IDENTIFICATION_TYPES_SaferIdentityTypeCertificate = 4
def _define_SAFER_IDENTIFICATION_HEADER_head():
    class SAFER_IDENTIFICATION_HEADER(Structure):
        pass
    return SAFER_IDENTIFICATION_HEADER
def _define_SAFER_IDENTIFICATION_HEADER():
    SAFER_IDENTIFICATION_HEADER = win32more.Security.AppLocker.SAFER_IDENTIFICATION_HEADER_head
    SAFER_IDENTIFICATION_HEADER._fields_ = [
        ("dwIdentificationType", win32more.Security.AppLocker.SAFER_IDENTIFICATION_TYPES),
        ("cbStructSize", UInt32),
        ("IdentificationGuid", Guid),
        ("lastModified", win32more.Foundation.FILETIME),
    ]
    return SAFER_IDENTIFICATION_HEADER
def _define_SAFER_PATHNAME_IDENTIFICATION_head():
    class SAFER_PATHNAME_IDENTIFICATION(Structure):
        pass
    return SAFER_PATHNAME_IDENTIFICATION
def _define_SAFER_PATHNAME_IDENTIFICATION():
    SAFER_PATHNAME_IDENTIFICATION = win32more.Security.AppLocker.SAFER_PATHNAME_IDENTIFICATION_head
    SAFER_PATHNAME_IDENTIFICATION._fields_ = [
        ("header", win32more.Security.AppLocker.SAFER_IDENTIFICATION_HEADER),
        ("Description", Char * 256),
        ("ImageName", win32more.Foundation.PWSTR),
        ("dwSaferFlags", UInt32),
    ]
    return SAFER_PATHNAME_IDENTIFICATION
def _define_SAFER_HASH_IDENTIFICATION_head():
    class SAFER_HASH_IDENTIFICATION(Structure):
        pass
    return SAFER_HASH_IDENTIFICATION
def _define_SAFER_HASH_IDENTIFICATION():
    SAFER_HASH_IDENTIFICATION = win32more.Security.AppLocker.SAFER_HASH_IDENTIFICATION_head
    SAFER_HASH_IDENTIFICATION._fields_ = [
        ("header", win32more.Security.AppLocker.SAFER_IDENTIFICATION_HEADER),
        ("Description", Char * 256),
        ("FriendlyName", Char * 256),
        ("HashSize", UInt32),
        ("ImageHash", Byte * 64),
        ("HashAlgorithm", UInt32),
        ("ImageSize", win32more.Foundation.LARGE_INTEGER),
        ("dwSaferFlags", UInt32),
    ]
    return SAFER_HASH_IDENTIFICATION
def _define_SAFER_HASH_IDENTIFICATION2_head():
    class SAFER_HASH_IDENTIFICATION2(Structure):
        pass
    return SAFER_HASH_IDENTIFICATION2
def _define_SAFER_HASH_IDENTIFICATION2():
    SAFER_HASH_IDENTIFICATION2 = win32more.Security.AppLocker.SAFER_HASH_IDENTIFICATION2_head
    SAFER_HASH_IDENTIFICATION2._fields_ = [
        ("hashIdentification", win32more.Security.AppLocker.SAFER_HASH_IDENTIFICATION),
        ("HashSize", UInt32),
        ("ImageHash", Byte * 64),
        ("HashAlgorithm", UInt32),
    ]
    return SAFER_HASH_IDENTIFICATION2
def _define_SAFER_URLZONE_IDENTIFICATION_head():
    class SAFER_URLZONE_IDENTIFICATION(Structure):
        pass
    return SAFER_URLZONE_IDENTIFICATION
def _define_SAFER_URLZONE_IDENTIFICATION():
    SAFER_URLZONE_IDENTIFICATION = win32more.Security.AppLocker.SAFER_URLZONE_IDENTIFICATION_head
    SAFER_URLZONE_IDENTIFICATION._fields_ = [
        ("header", win32more.Security.AppLocker.SAFER_IDENTIFICATION_HEADER),
        ("UrlZoneId", UInt32),
        ("dwSaferFlags", UInt32),
    ]
    return SAFER_URLZONE_IDENTIFICATION
def _define_SaferGetPolicyInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.Security.AppLocker.SAFER_POLICY_INFO_CLASS,UInt32,c_void_p,POINTER(UInt32),c_void_p, use_last_error=True)(("SaferGetPolicyInformation", windll["ADVAPI32"]), ((1, 'dwScopeId'),(1, 'SaferPolicyInfoClass'),(1, 'InfoBufferSize'),(1, 'InfoBuffer'),(1, 'InfoBufferRetSize'),(1, 'lpReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SaferSetPolicyInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.Security.AppLocker.SAFER_POLICY_INFO_CLASS,UInt32,c_void_p,c_void_p, use_last_error=True)(("SaferSetPolicyInformation", windll["ADVAPI32"]), ((1, 'dwScopeId'),(1, 'SaferPolicyInfoClass'),(1, 'InfoBufferSize'),(1, 'InfoBuffer'),(1, 'lpReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SaferCreateLevel():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,UInt32,UInt32,POINTER(win32more.Security.SAFER_LEVEL_HANDLE),c_void_p, use_last_error=True)(("SaferCreateLevel", windll["ADVAPI32"]), ((1, 'dwScopeId'),(1, 'dwLevelId'),(1, 'OpenFlags'),(1, 'pLevelHandle'),(1, 'lpReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SaferCloseLevel():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.SAFER_LEVEL_HANDLE, use_last_error=True)(("SaferCloseLevel", windll["ADVAPI32"]), ((1, 'hLevelHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SaferIdentifyLevel():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,POINTER(win32more.Security.AppLocker.SAFER_CODE_PROPERTIES_V2),POINTER(win32more.Security.SAFER_LEVEL_HANDLE),c_void_p, use_last_error=True)(("SaferIdentifyLevel", windll["ADVAPI32"]), ((1, 'dwNumProperties'),(1, 'pCodeProperties'),(1, 'pLevelHandle'),(1, 'lpReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SaferComputeTokenFromLevel():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.SAFER_LEVEL_HANDLE,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.HANDLE),win32more.Security.AppLocker.SAFER_COMPUTE_TOKEN_FROM_LEVEL_FLAGS,c_void_p, use_last_error=True)(("SaferComputeTokenFromLevel", windll["ADVAPI32"]), ((1, 'LevelHandle'),(1, 'InAccessToken'),(1, 'OutAccessToken'),(1, 'dwFlags'),(1, 'lpReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SaferGetLevelInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.SAFER_LEVEL_HANDLE,win32more.Security.AppLocker.SAFER_OBJECT_INFO_CLASS,c_void_p,UInt32,POINTER(UInt32), use_last_error=True)(("SaferGetLevelInformation", windll["ADVAPI32"]), ((1, 'LevelHandle'),(1, 'dwInfoType'),(1, 'lpQueryBuffer'),(1, 'dwInBufferSize'),(1, 'lpdwOutBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SaferSetLevelInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.SAFER_LEVEL_HANDLE,win32more.Security.AppLocker.SAFER_OBJECT_INFO_CLASS,c_void_p,UInt32, use_last_error=True)(("SaferSetLevelInformation", windll["ADVAPI32"]), ((1, 'LevelHandle'),(1, 'dwInfoType'),(1, 'lpQueryBuffer'),(1, 'dwInBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SaferRecordEventLogEntry():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.SAFER_LEVEL_HANDLE,win32more.Foundation.PWSTR,c_void_p, use_last_error=True)(("SaferRecordEventLogEntry", windll["ADVAPI32"]), ((1, 'hLevel'),(1, 'szTargetPath'),(1, 'lpReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SaferiIsExecutableFileType():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.BOOLEAN, use_last_error=False)(("SaferiIsExecutableFileType", windll["ADVAPI32"]), ((1, 'szFullPathname'),(1, 'bFromShellExecute'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "SAFER_SCOPEID_MACHINE",
    "SAFER_SCOPEID_USER",
    "SAFER_LEVELID_FULLYTRUSTED",
    "SAFER_LEVELID_NORMALUSER",
    "SAFER_LEVELID_CONSTRAINED",
    "SAFER_LEVELID_UNTRUSTED",
    "SAFER_LEVELID_DISALLOWED",
    "SAFER_LEVEL_OPEN",
    "SAFER_MAX_FRIENDLYNAME_SIZE",
    "SAFER_MAX_DESCRIPTION_SIZE",
    "SAFER_MAX_HASH_SIZE",
    "SAFER_CRITERIA_IMAGEPATH",
    "SAFER_CRITERIA_NOSIGNEDHASH",
    "SAFER_CRITERIA_IMAGEHASH",
    "SAFER_CRITERIA_AUTHENTICODE",
    "SAFER_CRITERIA_URLZONE",
    "SAFER_CRITERIA_APPX_PACKAGE",
    "SAFER_CRITERIA_IMAGEPATH_NT",
    "SAFER_POLICY_JOBID_MASK",
    "SAFER_POLICY_JOBID_CONSTRAINED",
    "SAFER_POLICY_JOBID_UNTRUSTED",
    "SAFER_POLICY_ONLY_EXES",
    "SAFER_POLICY_SANDBOX_INERT",
    "SAFER_POLICY_HASH_DUPLICATE",
    "SAFER_POLICY_ONLY_AUDIT",
    "SAFER_POLICY_BLOCK_CLIENT_UI",
    "SAFER_POLICY_UIFLAGS_MASK",
    "SAFER_POLICY_UIFLAGS_INFORMATION_PROMPT",
    "SAFER_POLICY_UIFLAGS_OPTION_PROMPT",
    "SAFER_POLICY_UIFLAGS_HIDDEN",
    "SAFER_COMPUTE_TOKEN_FROM_LEVEL_FLAGS",
    "SAFER_TOKEN_NULL_IF_EQUAL",
    "SAFER_TOKEN_COMPARE_ONLY",
    "SAFER_TOKEN_MAKE_INERT",
    "SAFER_TOKEN_WANT_FLAGS",
    "SAFER_CODE_PROPERTIES_V1",
    "SAFER_CODE_PROPERTIES_V2",
    "SAFER_POLICY_INFO_CLASS",
    "SAFER_POLICY_INFO_CLASS_SaferPolicyLevelList",
    "SAFER_POLICY_INFO_CLASS_SaferPolicyEnableTransparentEnforcement",
    "SAFER_POLICY_INFO_CLASS_SaferPolicyDefaultLevel",
    "SAFER_POLICY_INFO_CLASS_SaferPolicyEvaluateUserScope",
    "SAFER_POLICY_INFO_CLASS_SaferPolicyScopeFlags",
    "SAFER_POLICY_INFO_CLASS_SaferPolicyDefaultLevelFlags",
    "SAFER_POLICY_INFO_CLASS_SaferPolicyAuthenticodeEnabled",
    "SAFER_OBJECT_INFO_CLASS",
    "SAFER_OBJECT_INFO_CLASS_SaferObjectLevelId",
    "SAFER_OBJECT_INFO_CLASS_SaferObjectScopeId",
    "SAFER_OBJECT_INFO_CLASS_SaferObjectFriendlyName",
    "SAFER_OBJECT_INFO_CLASS_SaferObjectDescription",
    "SAFER_OBJECT_INFO_CLASS_SaferObjectBuiltin",
    "SAFER_OBJECT_INFO_CLASS_SaferObjectDisallowed",
    "SAFER_OBJECT_INFO_CLASS_SaferObjectDisableMaxPrivilege",
    "SAFER_OBJECT_INFO_CLASS_SaferObjectInvertDeletedPrivileges",
    "SAFER_OBJECT_INFO_CLASS_SaferObjectDeletedPrivileges",
    "SAFER_OBJECT_INFO_CLASS_SaferObjectDefaultOwner",
    "SAFER_OBJECT_INFO_CLASS_SaferObjectSidsToDisable",
    "SAFER_OBJECT_INFO_CLASS_SaferObjectRestrictedSidsInverted",
    "SAFER_OBJECT_INFO_CLASS_SaferObjectRestrictedSidsAdded",
    "SAFER_OBJECT_INFO_CLASS_SaferObjectAllIdentificationGuids",
    "SAFER_OBJECT_INFO_CLASS_SaferObjectSingleIdentification",
    "SAFER_OBJECT_INFO_CLASS_SaferObjectExtendedError",
    "SAFER_IDENTIFICATION_TYPES",
    "SAFER_IDENTIFICATION_TYPES_SaferIdentityDefault",
    "SAFER_IDENTIFICATION_TYPES_SaferIdentityTypeImageName",
    "SAFER_IDENTIFICATION_TYPES_SaferIdentityTypeImageHash",
    "SAFER_IDENTIFICATION_TYPES_SaferIdentityTypeUrlZone",
    "SAFER_IDENTIFICATION_TYPES_SaferIdentityTypeCertificate",
    "SAFER_IDENTIFICATION_HEADER",
    "SAFER_PATHNAME_IDENTIFICATION",
    "SAFER_HASH_IDENTIFICATION",
    "SAFER_HASH_IDENTIFICATION2",
    "SAFER_URLZONE_IDENTIFICATION",
    "SaferGetPolicyInformation",
    "SaferSetPolicyInformation",
    "SaferCreateLevel",
    "SaferCloseLevel",
    "SaferIdentifyLevel",
    "SaferComputeTokenFromLevel",
    "SaferGetLevelInformation",
    "SaferSetLevelInformation",
    "SaferRecordEventLogEntry",
    "SaferiIsExecutableFileType",
]
