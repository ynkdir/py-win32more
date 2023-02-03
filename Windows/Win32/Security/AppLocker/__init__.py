from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.Security
import Windows.Win32.Security.AppLocker
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
SAFER_SCOPEID_MACHINE: UInt32 = 1
SAFER_SCOPEID_USER: UInt32 = 2
SAFER_LEVELID_FULLYTRUSTED: UInt32 = 262144
SAFER_LEVELID_NORMALUSER: UInt32 = 131072
SAFER_LEVELID_CONSTRAINED: UInt32 = 65536
SAFER_LEVELID_UNTRUSTED: UInt32 = 4096
SAFER_LEVELID_DISALLOWED: UInt32 = 0
SAFER_LEVEL_OPEN: UInt32 = 1
SAFER_MAX_FRIENDLYNAME_SIZE: UInt32 = 256
SAFER_MAX_DESCRIPTION_SIZE: UInt32 = 256
SAFER_MAX_HASH_SIZE: UInt32 = 64
SAFER_CRITERIA_IMAGEPATH: UInt32 = 1
SAFER_CRITERIA_NOSIGNEDHASH: UInt32 = 2
SAFER_CRITERIA_IMAGEHASH: UInt32 = 4
SAFER_CRITERIA_AUTHENTICODE: UInt32 = 8
SAFER_CRITERIA_URLZONE: UInt32 = 16
SAFER_CRITERIA_APPX_PACKAGE: UInt32 = 32
SAFER_CRITERIA_IMAGEPATH_NT: UInt32 = 4096
SAFER_POLICY_JOBID_MASK: UInt32 = 4278190080
SAFER_POLICY_JOBID_CONSTRAINED: UInt32 = 67108864
SAFER_POLICY_JOBID_UNTRUSTED: UInt32 = 50331648
SAFER_POLICY_ONLY_EXES: UInt32 = 65536
SAFER_POLICY_SANDBOX_INERT: UInt32 = 131072
SAFER_POLICY_HASH_DUPLICATE: UInt32 = 262144
SAFER_POLICY_ONLY_AUDIT: UInt32 = 4096
SAFER_POLICY_BLOCK_CLIENT_UI: UInt32 = 8192
SAFER_POLICY_UIFLAGS_MASK: UInt32 = 255
SAFER_POLICY_UIFLAGS_INFORMATION_PROMPT: UInt32 = 1
SAFER_POLICY_UIFLAGS_OPTION_PROMPT: UInt32 = 2
SAFER_POLICY_UIFLAGS_HIDDEN: UInt32 = 4
SRP_POLICY_EXE: String = 'EXE'
SRP_POLICY_DLL: String = 'DLL'
SRP_POLICY_MSI: String = 'MSI'
SRP_POLICY_SCRIPT: String = 'SCRIPT'
SRP_POLICY_SHELL: String = 'SHELL'
SRP_POLICY_NOV2: String = 'IGNORESRPV2'
SRP_POLICY_APPX: String = 'APPX'
SRP_POLICY_WLDPMSI: String = 'WLDPMSI'
SRP_POLICY_WLDPSCRIPT: String = 'WLDPSCRIPT'
SRP_POLICY_WLDPCONFIGCI: String = 'WLDPCONFIGCI'
SRP_POLICY_MANAGEDINSTALLER: String = 'MANAGEDINSTALLER'
@winfunctype('ADVAPI32.dll')
def SaferGetPolicyInformation(dwScopeId: UInt32, SaferPolicyInfoClass: Windows.Win32.Security.AppLocker.SAFER_POLICY_INFO_CLASS, InfoBufferSize: UInt32, InfoBuffer: c_void_p, InfoBufferRetSize: POINTER(UInt32), lpReserved: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def SaferSetPolicyInformation(dwScopeId: UInt32, SaferPolicyInfoClass: Windows.Win32.Security.AppLocker.SAFER_POLICY_INFO_CLASS, InfoBufferSize: UInt32, InfoBuffer: c_void_p, lpReserved: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def SaferCreateLevel(dwScopeId: UInt32, dwLevelId: UInt32, OpenFlags: UInt32, pLevelHandle: POINTER(Windows.Win32.Security.SAFER_LEVEL_HANDLE), lpReserved: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def SaferCloseLevel(hLevelHandle: Windows.Win32.Security.SAFER_LEVEL_HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def SaferIdentifyLevel(dwNumProperties: UInt32, pCodeProperties: POINTER(Windows.Win32.Security.AppLocker.SAFER_CODE_PROPERTIES_V2_head), pLevelHandle: POINTER(Windows.Win32.Security.SAFER_LEVEL_HANDLE), lpReserved: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def SaferComputeTokenFromLevel(LevelHandle: Windows.Win32.Security.SAFER_LEVEL_HANDLE, InAccessToken: Windows.Win32.Foundation.HANDLE, OutAccessToken: POINTER(Windows.Win32.Foundation.HANDLE), dwFlags: Windows.Win32.Security.AppLocker.SAFER_COMPUTE_TOKEN_FROM_LEVEL_FLAGS, lpReserved: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def SaferGetLevelInformation(LevelHandle: Windows.Win32.Security.SAFER_LEVEL_HANDLE, dwInfoType: Windows.Win32.Security.AppLocker.SAFER_OBJECT_INFO_CLASS, lpQueryBuffer: c_void_p, dwInBufferSize: UInt32, lpdwOutBufferSize: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def SaferSetLevelInformation(LevelHandle: Windows.Win32.Security.SAFER_LEVEL_HANDLE, dwInfoType: Windows.Win32.Security.AppLocker.SAFER_OBJECT_INFO_CLASS, lpQueryBuffer: c_void_p, dwInBufferSize: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def SaferRecordEventLogEntry(hLevel: Windows.Win32.Security.SAFER_LEVEL_HANDLE, szTargetPath: Windows.Win32.Foundation.PWSTR, lpReserved: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def SaferiIsExecutableFileType(szFullPathname: Windows.Win32.Foundation.PWSTR, bFromShellExecute: Windows.Win32.Foundation.BOOLEAN) -> Windows.Win32.Foundation.BOOL: ...
class SAFER_CODE_PROPERTIES_V1(Structure):
    cbSize: UInt32
    dwCheckFlags: UInt32
    ImagePath: Windows.Win32.Foundation.PWSTR
    hImageFileHandle: Windows.Win32.Foundation.HANDLE
    UrlZoneId: UInt32
    ImageHash: Byte * 64
    dwImageHashSize: UInt32
    ImageSize: Windows.Win32.Foundation.LARGE_INTEGER
    HashAlgorithm: UInt32
    pByteBlock: c_char_p_no
    hWndParent: Windows.Win32.Foundation.HWND
    dwWVTUIChoice: UInt32
class SAFER_CODE_PROPERTIES_V2(Structure):
    cbSize: UInt32
    dwCheckFlags: UInt32
    ImagePath: Windows.Win32.Foundation.PWSTR
    hImageFileHandle: Windows.Win32.Foundation.HANDLE
    UrlZoneId: UInt32
    ImageHash: Byte * 64
    dwImageHashSize: UInt32
    ImageSize: Windows.Win32.Foundation.LARGE_INTEGER
    HashAlgorithm: UInt32
    pByteBlock: c_char_p_no
    hWndParent: Windows.Win32.Foundation.HWND
    dwWVTUIChoice: UInt32
    PackageMoniker: Windows.Win32.Foundation.PWSTR
    PackagePublisher: Windows.Win32.Foundation.PWSTR
    PackageName: Windows.Win32.Foundation.PWSTR
    PackageVersion: UInt64
    PackageIsFramework: Windows.Win32.Foundation.BOOL
SAFER_COMPUTE_TOKEN_FROM_LEVEL_FLAGS = UInt32
SAFER_TOKEN_NULL_IF_EQUAL: SAFER_COMPUTE_TOKEN_FROM_LEVEL_FLAGS = 1
SAFER_TOKEN_COMPARE_ONLY: SAFER_COMPUTE_TOKEN_FROM_LEVEL_FLAGS = 2
SAFER_TOKEN_MAKE_INERT: SAFER_COMPUTE_TOKEN_FROM_LEVEL_FLAGS = 4
SAFER_TOKEN_WANT_FLAGS: SAFER_COMPUTE_TOKEN_FROM_LEVEL_FLAGS = 8
class SAFER_HASH_IDENTIFICATION(Structure):
    header: Windows.Win32.Security.AppLocker.SAFER_IDENTIFICATION_HEADER
    Description: Char * 256
    FriendlyName: Char * 256
    HashSize: UInt32
    ImageHash: Byte * 64
    HashAlgorithm: UInt32
    ImageSize: Windows.Win32.Foundation.LARGE_INTEGER
    dwSaferFlags: UInt32
class SAFER_HASH_IDENTIFICATION2(Structure):
    hashIdentification: Windows.Win32.Security.AppLocker.SAFER_HASH_IDENTIFICATION
    HashSize: UInt32
    ImageHash: Byte * 64
    HashAlgorithm: UInt32
class SAFER_IDENTIFICATION_HEADER(Structure):
    dwIdentificationType: Windows.Win32.Security.AppLocker.SAFER_IDENTIFICATION_TYPES
    cbStructSize: UInt32
    IdentificationGuid: Guid
    lastModified: Windows.Win32.Foundation.FILETIME
SAFER_IDENTIFICATION_TYPES = Int32
SAFER_IDENTIFICATION_TYPES_SaferIdentityDefault: SAFER_IDENTIFICATION_TYPES = 0
SAFER_IDENTIFICATION_TYPES_SaferIdentityTypeImageName: SAFER_IDENTIFICATION_TYPES = 1
SAFER_IDENTIFICATION_TYPES_SaferIdentityTypeImageHash: SAFER_IDENTIFICATION_TYPES = 2
SAFER_IDENTIFICATION_TYPES_SaferIdentityTypeUrlZone: SAFER_IDENTIFICATION_TYPES = 3
SAFER_IDENTIFICATION_TYPES_SaferIdentityTypeCertificate: SAFER_IDENTIFICATION_TYPES = 4
SAFER_OBJECT_INFO_CLASS = Int32
SAFER_OBJECT_INFO_CLASS_SaferObjectLevelId: SAFER_OBJECT_INFO_CLASS = 1
SAFER_OBJECT_INFO_CLASS_SaferObjectScopeId: SAFER_OBJECT_INFO_CLASS = 2
SAFER_OBJECT_INFO_CLASS_SaferObjectFriendlyName: SAFER_OBJECT_INFO_CLASS = 3
SAFER_OBJECT_INFO_CLASS_SaferObjectDescription: SAFER_OBJECT_INFO_CLASS = 4
SAFER_OBJECT_INFO_CLASS_SaferObjectBuiltin: SAFER_OBJECT_INFO_CLASS = 5
SAFER_OBJECT_INFO_CLASS_SaferObjectDisallowed: SAFER_OBJECT_INFO_CLASS = 6
SAFER_OBJECT_INFO_CLASS_SaferObjectDisableMaxPrivilege: SAFER_OBJECT_INFO_CLASS = 7
SAFER_OBJECT_INFO_CLASS_SaferObjectInvertDeletedPrivileges: SAFER_OBJECT_INFO_CLASS = 8
SAFER_OBJECT_INFO_CLASS_SaferObjectDeletedPrivileges: SAFER_OBJECT_INFO_CLASS = 9
SAFER_OBJECT_INFO_CLASS_SaferObjectDefaultOwner: SAFER_OBJECT_INFO_CLASS = 10
SAFER_OBJECT_INFO_CLASS_SaferObjectSidsToDisable: SAFER_OBJECT_INFO_CLASS = 11
SAFER_OBJECT_INFO_CLASS_SaferObjectRestrictedSidsInverted: SAFER_OBJECT_INFO_CLASS = 12
SAFER_OBJECT_INFO_CLASS_SaferObjectRestrictedSidsAdded: SAFER_OBJECT_INFO_CLASS = 13
SAFER_OBJECT_INFO_CLASS_SaferObjectAllIdentificationGuids: SAFER_OBJECT_INFO_CLASS = 14
SAFER_OBJECT_INFO_CLASS_SaferObjectSingleIdentification: SAFER_OBJECT_INFO_CLASS = 15
SAFER_OBJECT_INFO_CLASS_SaferObjectExtendedError: SAFER_OBJECT_INFO_CLASS = 16
class SAFER_PATHNAME_IDENTIFICATION(Structure):
    header: Windows.Win32.Security.AppLocker.SAFER_IDENTIFICATION_HEADER
    Description: Char * 256
    ImageName: Windows.Win32.Foundation.PWSTR
    dwSaferFlags: UInt32
SAFER_POLICY_INFO_CLASS = Int32
SAFER_POLICY_INFO_CLASS_SaferPolicyLevelList: SAFER_POLICY_INFO_CLASS = 1
SAFER_POLICY_INFO_CLASS_SaferPolicyEnableTransparentEnforcement: SAFER_POLICY_INFO_CLASS = 2
SAFER_POLICY_INFO_CLASS_SaferPolicyDefaultLevel: SAFER_POLICY_INFO_CLASS = 3
SAFER_POLICY_INFO_CLASS_SaferPolicyEvaluateUserScope: SAFER_POLICY_INFO_CLASS = 4
SAFER_POLICY_INFO_CLASS_SaferPolicyScopeFlags: SAFER_POLICY_INFO_CLASS = 5
SAFER_POLICY_INFO_CLASS_SaferPolicyDefaultLevelFlags: SAFER_POLICY_INFO_CLASS = 6
SAFER_POLICY_INFO_CLASS_SaferPolicyAuthenticodeEnabled: SAFER_POLICY_INFO_CLASS = 7
class SAFER_URLZONE_IDENTIFICATION(Structure):
    header: Windows.Win32.Security.AppLocker.SAFER_IDENTIFICATION_HEADER
    UrlZoneId: UInt32
    dwSaferFlags: UInt32
make_head(_module, 'SAFER_CODE_PROPERTIES_V1')
make_head(_module, 'SAFER_CODE_PROPERTIES_V2')
make_head(_module, 'SAFER_HASH_IDENTIFICATION')
make_head(_module, 'SAFER_HASH_IDENTIFICATION2')
make_head(_module, 'SAFER_IDENTIFICATION_HEADER')
make_head(_module, 'SAFER_PATHNAME_IDENTIFICATION')
make_head(_module, 'SAFER_URLZONE_IDENTIFICATION')
__all__ = [
    "SAFER_CODE_PROPERTIES_V1",
    "SAFER_CODE_PROPERTIES_V2",
    "SAFER_COMPUTE_TOKEN_FROM_LEVEL_FLAGS",
    "SAFER_CRITERIA_APPX_PACKAGE",
    "SAFER_CRITERIA_AUTHENTICODE",
    "SAFER_CRITERIA_IMAGEHASH",
    "SAFER_CRITERIA_IMAGEPATH",
    "SAFER_CRITERIA_IMAGEPATH_NT",
    "SAFER_CRITERIA_NOSIGNEDHASH",
    "SAFER_CRITERIA_URLZONE",
    "SAFER_HASH_IDENTIFICATION",
    "SAFER_HASH_IDENTIFICATION2",
    "SAFER_IDENTIFICATION_HEADER",
    "SAFER_IDENTIFICATION_TYPES",
    "SAFER_IDENTIFICATION_TYPES_SaferIdentityDefault",
    "SAFER_IDENTIFICATION_TYPES_SaferIdentityTypeCertificate",
    "SAFER_IDENTIFICATION_TYPES_SaferIdentityTypeImageHash",
    "SAFER_IDENTIFICATION_TYPES_SaferIdentityTypeImageName",
    "SAFER_IDENTIFICATION_TYPES_SaferIdentityTypeUrlZone",
    "SAFER_LEVELID_CONSTRAINED",
    "SAFER_LEVELID_DISALLOWED",
    "SAFER_LEVELID_FULLYTRUSTED",
    "SAFER_LEVELID_NORMALUSER",
    "SAFER_LEVELID_UNTRUSTED",
    "SAFER_LEVEL_OPEN",
    "SAFER_MAX_DESCRIPTION_SIZE",
    "SAFER_MAX_FRIENDLYNAME_SIZE",
    "SAFER_MAX_HASH_SIZE",
    "SAFER_OBJECT_INFO_CLASS",
    "SAFER_OBJECT_INFO_CLASS_SaferObjectAllIdentificationGuids",
    "SAFER_OBJECT_INFO_CLASS_SaferObjectBuiltin",
    "SAFER_OBJECT_INFO_CLASS_SaferObjectDefaultOwner",
    "SAFER_OBJECT_INFO_CLASS_SaferObjectDeletedPrivileges",
    "SAFER_OBJECT_INFO_CLASS_SaferObjectDescription",
    "SAFER_OBJECT_INFO_CLASS_SaferObjectDisableMaxPrivilege",
    "SAFER_OBJECT_INFO_CLASS_SaferObjectDisallowed",
    "SAFER_OBJECT_INFO_CLASS_SaferObjectExtendedError",
    "SAFER_OBJECT_INFO_CLASS_SaferObjectFriendlyName",
    "SAFER_OBJECT_INFO_CLASS_SaferObjectInvertDeletedPrivileges",
    "SAFER_OBJECT_INFO_CLASS_SaferObjectLevelId",
    "SAFER_OBJECT_INFO_CLASS_SaferObjectRestrictedSidsAdded",
    "SAFER_OBJECT_INFO_CLASS_SaferObjectRestrictedSidsInverted",
    "SAFER_OBJECT_INFO_CLASS_SaferObjectScopeId",
    "SAFER_OBJECT_INFO_CLASS_SaferObjectSidsToDisable",
    "SAFER_OBJECT_INFO_CLASS_SaferObjectSingleIdentification",
    "SAFER_PATHNAME_IDENTIFICATION",
    "SAFER_POLICY_BLOCK_CLIENT_UI",
    "SAFER_POLICY_HASH_DUPLICATE",
    "SAFER_POLICY_INFO_CLASS",
    "SAFER_POLICY_INFO_CLASS_SaferPolicyAuthenticodeEnabled",
    "SAFER_POLICY_INFO_CLASS_SaferPolicyDefaultLevel",
    "SAFER_POLICY_INFO_CLASS_SaferPolicyDefaultLevelFlags",
    "SAFER_POLICY_INFO_CLASS_SaferPolicyEnableTransparentEnforcement",
    "SAFER_POLICY_INFO_CLASS_SaferPolicyEvaluateUserScope",
    "SAFER_POLICY_INFO_CLASS_SaferPolicyLevelList",
    "SAFER_POLICY_INFO_CLASS_SaferPolicyScopeFlags",
    "SAFER_POLICY_JOBID_CONSTRAINED",
    "SAFER_POLICY_JOBID_MASK",
    "SAFER_POLICY_JOBID_UNTRUSTED",
    "SAFER_POLICY_ONLY_AUDIT",
    "SAFER_POLICY_ONLY_EXES",
    "SAFER_POLICY_SANDBOX_INERT",
    "SAFER_POLICY_UIFLAGS_HIDDEN",
    "SAFER_POLICY_UIFLAGS_INFORMATION_PROMPT",
    "SAFER_POLICY_UIFLAGS_MASK",
    "SAFER_POLICY_UIFLAGS_OPTION_PROMPT",
    "SAFER_SCOPEID_MACHINE",
    "SAFER_SCOPEID_USER",
    "SAFER_TOKEN_COMPARE_ONLY",
    "SAFER_TOKEN_MAKE_INERT",
    "SAFER_TOKEN_NULL_IF_EQUAL",
    "SAFER_TOKEN_WANT_FLAGS",
    "SAFER_URLZONE_IDENTIFICATION",
    "SRP_POLICY_APPX",
    "SRP_POLICY_DLL",
    "SRP_POLICY_EXE",
    "SRP_POLICY_MANAGEDINSTALLER",
    "SRP_POLICY_MSI",
    "SRP_POLICY_NOV2",
    "SRP_POLICY_SCRIPT",
    "SRP_POLICY_SHELL",
    "SRP_POLICY_WLDPCONFIGCI",
    "SRP_POLICY_WLDPMSI",
    "SRP_POLICY_WLDPSCRIPT",
    "SaferCloseLevel",
    "SaferComputeTokenFromLevel",
    "SaferCreateLevel",
    "SaferGetLevelInformation",
    "SaferGetPolicyInformation",
    "SaferIdentifyLevel",
    "SaferRecordEventLogEntry",
    "SaferSetLevelInformation",
    "SaferSetPolicyInformation",
    "SaferiIsExecutableFileType",
]
_arch_optional = [
]
