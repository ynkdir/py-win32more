from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Security
import win32more.Windows.Win32.Security.AppLocker
import win32more.Windows.Win32.Security.Cryptography
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
def SaferGetPolicyInformation(dwScopeId: UInt32, SaferPolicyInfoClass: win32more.Windows.Win32.Security.AppLocker.SAFER_POLICY_INFO_CLASS, InfoBufferSize: UInt32, InfoBuffer: VoidPtr, InfoBufferRetSize: POINTER(UInt32), lpReserved: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def SaferSetPolicyInformation(dwScopeId: UInt32, SaferPolicyInfoClass: win32more.Windows.Win32.Security.AppLocker.SAFER_POLICY_INFO_CLASS, InfoBufferSize: UInt32, InfoBuffer: VoidPtr, lpReserved: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def SaferCreateLevel(dwScopeId: UInt32, dwLevelId: UInt32, OpenFlags: UInt32, pLevelHandle: POINTER(win32more.Windows.Win32.Security.SAFER_LEVEL_HANDLE), lpReserved: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def SaferCloseLevel(hLevelHandle: win32more.Windows.Win32.Security.SAFER_LEVEL_HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def SaferIdentifyLevel(dwNumProperties: UInt32, pCodeProperties: POINTER(win32more.Windows.Win32.Security.AppLocker.SAFER_CODE_PROPERTIES_V2), pLevelHandle: POINTER(win32more.Windows.Win32.Security.SAFER_LEVEL_HANDLE), lpReserved: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def SaferComputeTokenFromLevel(LevelHandle: win32more.Windows.Win32.Security.SAFER_LEVEL_HANDLE, InAccessToken: win32more.Windows.Win32.Foundation.HANDLE, OutAccessToken: POINTER(win32more.Windows.Win32.Foundation.HANDLE), dwFlags: win32more.Windows.Win32.Security.AppLocker.SAFER_COMPUTE_TOKEN_FROM_LEVEL_FLAGS, lpReserved: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def SaferGetLevelInformation(LevelHandle: win32more.Windows.Win32.Security.SAFER_LEVEL_HANDLE, dwInfoType: win32more.Windows.Win32.Security.AppLocker.SAFER_OBJECT_INFO_CLASS, lpQueryBuffer: VoidPtr, dwInBufferSize: UInt32, lpdwOutBufferSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def SaferSetLevelInformation(LevelHandle: win32more.Windows.Win32.Security.SAFER_LEVEL_HANDLE, dwInfoType: win32more.Windows.Win32.Security.AppLocker.SAFER_OBJECT_INFO_CLASS, lpQueryBuffer: VoidPtr, dwInBufferSize: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def SaferRecordEventLogEntry(hLevel: win32more.Windows.Win32.Security.SAFER_LEVEL_HANDLE, szTargetPath: win32more.Windows.Win32.Foundation.PWSTR, lpReserved: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def SaferiIsExecutableFileType(szFullPathname: win32more.Windows.Win32.Foundation.PWSTR, bFromShellExecute: win32more.Windows.Win32.Foundation.BOOLEAN) -> win32more.Windows.Win32.Foundation.BOOL: ...
class SAFER_CODE_PROPERTIES_V1(Structure):
    cbSize: UInt32
    dwCheckFlags: UInt32
    ImagePath: win32more.Windows.Win32.Foundation.PWSTR
    hImageFileHandle: win32more.Windows.Win32.Foundation.HANDLE
    UrlZoneId: UInt32
    ImageHash: Byte * 64
    dwImageHashSize: UInt32
    ImageSize: Int64
    HashAlgorithm: win32more.Windows.Win32.Security.Cryptography.ALG_ID
    pByteBlock: POINTER(Byte)
    hWndParent: win32more.Windows.Win32.Foundation.HWND
    dwWVTUIChoice: UInt32
class SAFER_CODE_PROPERTIES_V2(Structure):
    cbSize: UInt32
    dwCheckFlags: UInt32
    ImagePath: win32more.Windows.Win32.Foundation.PWSTR
    hImageFileHandle: win32more.Windows.Win32.Foundation.HANDLE
    UrlZoneId: UInt32
    ImageHash: Byte * 64
    dwImageHashSize: UInt32
    ImageSize: Int64
    HashAlgorithm: win32more.Windows.Win32.Security.Cryptography.ALG_ID
    pByteBlock: POINTER(Byte)
    hWndParent: win32more.Windows.Win32.Foundation.HWND
    dwWVTUIChoice: UInt32
    PackageMoniker: win32more.Windows.Win32.Foundation.PWSTR
    PackagePublisher: win32more.Windows.Win32.Foundation.PWSTR
    PackageName: win32more.Windows.Win32.Foundation.PWSTR
    PackageVersion: UInt64
    PackageIsFramework: win32more.Windows.Win32.Foundation.BOOL
SAFER_COMPUTE_TOKEN_FROM_LEVEL_FLAGS = UInt32
SAFER_TOKEN_NULL_IF_EQUAL: win32more.Windows.Win32.Security.AppLocker.SAFER_COMPUTE_TOKEN_FROM_LEVEL_FLAGS = 1
SAFER_TOKEN_COMPARE_ONLY: win32more.Windows.Win32.Security.AppLocker.SAFER_COMPUTE_TOKEN_FROM_LEVEL_FLAGS = 2
SAFER_TOKEN_MAKE_INERT: win32more.Windows.Win32.Security.AppLocker.SAFER_COMPUTE_TOKEN_FROM_LEVEL_FLAGS = 4
SAFER_TOKEN_WANT_FLAGS: win32more.Windows.Win32.Security.AppLocker.SAFER_COMPUTE_TOKEN_FROM_LEVEL_FLAGS = 8
class SAFER_HASH_IDENTIFICATION(Structure):
    header: win32more.Windows.Win32.Security.AppLocker.SAFER_IDENTIFICATION_HEADER
    Description: Char * 256
    FriendlyName: Char * 256
    HashSize: UInt32
    ImageHash: Byte * 64
    HashAlgorithm: win32more.Windows.Win32.Security.Cryptography.ALG_ID
    ImageSize: Int64
    dwSaferFlags: UInt32
class SAFER_HASH_IDENTIFICATION2(Structure):
    hashIdentification: win32more.Windows.Win32.Security.AppLocker.SAFER_HASH_IDENTIFICATION
    HashSize: UInt32
    ImageHash: Byte * 64
    HashAlgorithm: win32more.Windows.Win32.Security.Cryptography.ALG_ID
class SAFER_IDENTIFICATION_HEADER(Structure):
    dwIdentificationType: win32more.Windows.Win32.Security.AppLocker.SAFER_IDENTIFICATION_TYPES
    cbStructSize: UInt32
    IdentificationGuid: Guid
    lastModified: win32more.Windows.Win32.Foundation.FILETIME
SAFER_IDENTIFICATION_TYPES = Int32
SaferIdentityDefault: win32more.Windows.Win32.Security.AppLocker.SAFER_IDENTIFICATION_TYPES = 0
SaferIdentityTypeImageName: win32more.Windows.Win32.Security.AppLocker.SAFER_IDENTIFICATION_TYPES = 1
SaferIdentityTypeImageHash: win32more.Windows.Win32.Security.AppLocker.SAFER_IDENTIFICATION_TYPES = 2
SaferIdentityTypeUrlZone: win32more.Windows.Win32.Security.AppLocker.SAFER_IDENTIFICATION_TYPES = 3
SaferIdentityTypeCertificate: win32more.Windows.Win32.Security.AppLocker.SAFER_IDENTIFICATION_TYPES = 4
SAFER_OBJECT_INFO_CLASS = Int32
SaferObjectLevelId: win32more.Windows.Win32.Security.AppLocker.SAFER_OBJECT_INFO_CLASS = 1
SaferObjectScopeId: win32more.Windows.Win32.Security.AppLocker.SAFER_OBJECT_INFO_CLASS = 2
SaferObjectFriendlyName: win32more.Windows.Win32.Security.AppLocker.SAFER_OBJECT_INFO_CLASS = 3
SaferObjectDescription: win32more.Windows.Win32.Security.AppLocker.SAFER_OBJECT_INFO_CLASS = 4
SaferObjectBuiltin: win32more.Windows.Win32.Security.AppLocker.SAFER_OBJECT_INFO_CLASS = 5
SaferObjectDisallowed: win32more.Windows.Win32.Security.AppLocker.SAFER_OBJECT_INFO_CLASS = 6
SaferObjectDisableMaxPrivilege: win32more.Windows.Win32.Security.AppLocker.SAFER_OBJECT_INFO_CLASS = 7
SaferObjectInvertDeletedPrivileges: win32more.Windows.Win32.Security.AppLocker.SAFER_OBJECT_INFO_CLASS = 8
SaferObjectDeletedPrivileges: win32more.Windows.Win32.Security.AppLocker.SAFER_OBJECT_INFO_CLASS = 9
SaferObjectDefaultOwner: win32more.Windows.Win32.Security.AppLocker.SAFER_OBJECT_INFO_CLASS = 10
SaferObjectSidsToDisable: win32more.Windows.Win32.Security.AppLocker.SAFER_OBJECT_INFO_CLASS = 11
SaferObjectRestrictedSidsInverted: win32more.Windows.Win32.Security.AppLocker.SAFER_OBJECT_INFO_CLASS = 12
SaferObjectRestrictedSidsAdded: win32more.Windows.Win32.Security.AppLocker.SAFER_OBJECT_INFO_CLASS = 13
SaferObjectAllIdentificationGuids: win32more.Windows.Win32.Security.AppLocker.SAFER_OBJECT_INFO_CLASS = 14
SaferObjectSingleIdentification: win32more.Windows.Win32.Security.AppLocker.SAFER_OBJECT_INFO_CLASS = 15
SaferObjectExtendedError: win32more.Windows.Win32.Security.AppLocker.SAFER_OBJECT_INFO_CLASS = 16
class SAFER_PATHNAME_IDENTIFICATION(Structure):
    header: win32more.Windows.Win32.Security.AppLocker.SAFER_IDENTIFICATION_HEADER
    Description: Char * 256
    ImageName: win32more.Windows.Win32.Foundation.PWSTR
    dwSaferFlags: UInt32
SAFER_POLICY_INFO_CLASS = Int32
SaferPolicyLevelList: win32more.Windows.Win32.Security.AppLocker.SAFER_POLICY_INFO_CLASS = 1
SaferPolicyEnableTransparentEnforcement: win32more.Windows.Win32.Security.AppLocker.SAFER_POLICY_INFO_CLASS = 2
SaferPolicyDefaultLevel: win32more.Windows.Win32.Security.AppLocker.SAFER_POLICY_INFO_CLASS = 3
SaferPolicyEvaluateUserScope: win32more.Windows.Win32.Security.AppLocker.SAFER_POLICY_INFO_CLASS = 4
SaferPolicyScopeFlags: win32more.Windows.Win32.Security.AppLocker.SAFER_POLICY_INFO_CLASS = 5
SaferPolicyDefaultLevelFlags: win32more.Windows.Win32.Security.AppLocker.SAFER_POLICY_INFO_CLASS = 6
SaferPolicyAuthenticodeEnabled: win32more.Windows.Win32.Security.AppLocker.SAFER_POLICY_INFO_CLASS = 7
class SAFER_URLZONE_IDENTIFICATION(Structure):
    header: win32more.Windows.Win32.Security.AppLocker.SAFER_IDENTIFICATION_HEADER
    UrlZoneId: UInt32
    dwSaferFlags: UInt32


make_ready(__name__)
