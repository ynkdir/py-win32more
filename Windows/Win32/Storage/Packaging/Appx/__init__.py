from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.Data.Xml.MsXml
import Windows.Win32.Foundation
import Windows.Win32.Storage.Packaging.Appx
import Windows.Win32.System.Com
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
APPX_BUNDLE_FOOTPRINT_FILE_TYPE = Int32
APPX_BUNDLE_FOOTPRINT_FILE_TYPE_FIRST: APPX_BUNDLE_FOOTPRINT_FILE_TYPE = 0
APPX_BUNDLE_FOOTPRINT_FILE_TYPE_MANIFEST: APPX_BUNDLE_FOOTPRINT_FILE_TYPE = 0
APPX_BUNDLE_FOOTPRINT_FILE_TYPE_BLOCKMAP: APPX_BUNDLE_FOOTPRINT_FILE_TYPE = 1
APPX_BUNDLE_FOOTPRINT_FILE_TYPE_SIGNATURE: APPX_BUNDLE_FOOTPRINT_FILE_TYPE = 2
APPX_BUNDLE_FOOTPRINT_FILE_TYPE_LAST: APPX_BUNDLE_FOOTPRINT_FILE_TYPE = 2
APPX_BUNDLE_PAYLOAD_PACKAGE_TYPE = Int32
APPX_BUNDLE_PAYLOAD_PACKAGE_TYPE_APPLICATION: APPX_BUNDLE_PAYLOAD_PACKAGE_TYPE = 0
APPX_BUNDLE_PAYLOAD_PACKAGE_TYPE_RESOURCE: APPX_BUNDLE_PAYLOAD_PACKAGE_TYPE = 1
APPX_CAPABILITIES = Int32
APPX_CAPABILITY_INTERNET_CLIENT: APPX_CAPABILITIES = 1
APPX_CAPABILITY_INTERNET_CLIENT_SERVER: APPX_CAPABILITIES = 2
APPX_CAPABILITY_PRIVATE_NETWORK_CLIENT_SERVER: APPX_CAPABILITIES = 4
APPX_CAPABILITY_DOCUMENTS_LIBRARY: APPX_CAPABILITIES = 8
APPX_CAPABILITY_PICTURES_LIBRARY: APPX_CAPABILITIES = 16
APPX_CAPABILITY_VIDEOS_LIBRARY: APPX_CAPABILITIES = 32
APPX_CAPABILITY_MUSIC_LIBRARY: APPX_CAPABILITIES = 64
APPX_CAPABILITY_ENTERPRISE_AUTHENTICATION: APPX_CAPABILITIES = 128
APPX_CAPABILITY_SHARED_USER_CERTIFICATES: APPX_CAPABILITIES = 256
APPX_CAPABILITY_REMOVABLE_STORAGE: APPX_CAPABILITIES = 512
APPX_CAPABILITY_APPOINTMENTS: APPX_CAPABILITIES = 1024
APPX_CAPABILITY_CONTACTS: APPX_CAPABILITIES = 2048
APPX_CAPABILITY_CLASS_TYPE = Int32
APPX_CAPABILITY_CLASS_DEFAULT: APPX_CAPABILITY_CLASS_TYPE = 0
APPX_CAPABILITY_CLASS_GENERAL: APPX_CAPABILITY_CLASS_TYPE = 1
APPX_CAPABILITY_CLASS_RESTRICTED: APPX_CAPABILITY_CLASS_TYPE = 2
APPX_CAPABILITY_CLASS_WINDOWS: APPX_CAPABILITY_CLASS_TYPE = 4
APPX_CAPABILITY_CLASS_ALL: APPX_CAPABILITY_CLASS_TYPE = 7
APPX_CAPABILITY_CLASS_CUSTOM: APPX_CAPABILITY_CLASS_TYPE = 8
APPX_COMPRESSION_OPTION = Int32
APPX_COMPRESSION_OPTION_NONE: APPX_COMPRESSION_OPTION = 0
APPX_COMPRESSION_OPTION_NORMAL: APPX_COMPRESSION_OPTION = 1
APPX_COMPRESSION_OPTION_MAXIMUM: APPX_COMPRESSION_OPTION = 2
APPX_COMPRESSION_OPTION_FAST: APPX_COMPRESSION_OPTION = 3
APPX_COMPRESSION_OPTION_SUPERFAST: APPX_COMPRESSION_OPTION = 4
class APPX_ENCRYPTED_EXEMPTIONS(EasyCastStructure):
    count: UInt32
    plainTextFiles: POINTER(Windows.Win32.Foundation.PWSTR)
APPX_ENCRYPTED_PACKAGE_OPTIONS = Int32
APPX_ENCRYPTED_PACKAGE_OPTION_NONE: APPX_ENCRYPTED_PACKAGE_OPTIONS = 0
APPX_ENCRYPTED_PACKAGE_OPTION_DIFFUSION: APPX_ENCRYPTED_PACKAGE_OPTIONS = 1
APPX_ENCRYPTED_PACKAGE_OPTION_PAGE_HASHING: APPX_ENCRYPTED_PACKAGE_OPTIONS = 2
class APPX_ENCRYPTED_PACKAGE_SETTINGS(EasyCastStructure):
    keyLength: UInt32
    encryptionAlgorithm: Windows.Win32.Foundation.PWSTR
    useDiffusion: Windows.Win32.Foundation.BOOL
    blockMapHashAlgorithm: Windows.Win32.System.Com.IUri_head
class APPX_ENCRYPTED_PACKAGE_SETTINGS2(EasyCastStructure):
    keyLength: UInt32
    encryptionAlgorithm: Windows.Win32.Foundation.PWSTR
    blockMapHashAlgorithm: Windows.Win32.System.Com.IUri_head
    options: UInt32
APPX_FOOTPRINT_FILE_TYPE = Int32
APPX_FOOTPRINT_FILE_TYPE_MANIFEST: APPX_FOOTPRINT_FILE_TYPE = 0
APPX_FOOTPRINT_FILE_TYPE_BLOCKMAP: APPX_FOOTPRINT_FILE_TYPE = 1
APPX_FOOTPRINT_FILE_TYPE_SIGNATURE: APPX_FOOTPRINT_FILE_TYPE = 2
APPX_FOOTPRINT_FILE_TYPE_CODEINTEGRITY: APPX_FOOTPRINT_FILE_TYPE = 3
APPX_FOOTPRINT_FILE_TYPE_CONTENTGROUPMAP: APPX_FOOTPRINT_FILE_TYPE = 4
class APPX_KEY_INFO(EasyCastStructure):
    keyLength: UInt32
    keyIdLength: UInt32
    key: POINTER(Byte)
    keyId: POINTER(Byte)
APPX_PACKAGE_ARCHITECTURE = Int32
APPX_PACKAGE_ARCHITECTURE_X86: APPX_PACKAGE_ARCHITECTURE = 0
APPX_PACKAGE_ARCHITECTURE_ARM: APPX_PACKAGE_ARCHITECTURE = 5
APPX_PACKAGE_ARCHITECTURE_X64: APPX_PACKAGE_ARCHITECTURE = 9
APPX_PACKAGE_ARCHITECTURE_NEUTRAL: APPX_PACKAGE_ARCHITECTURE = 11
APPX_PACKAGE_ARCHITECTURE_ARM64: APPX_PACKAGE_ARCHITECTURE = 12
APPX_PACKAGE_ARCHITECTURE2 = Int32
APPX_PACKAGE_ARCHITECTURE2_X86: APPX_PACKAGE_ARCHITECTURE2 = 0
APPX_PACKAGE_ARCHITECTURE2_ARM: APPX_PACKAGE_ARCHITECTURE2 = 5
APPX_PACKAGE_ARCHITECTURE2_X64: APPX_PACKAGE_ARCHITECTURE2 = 9
APPX_PACKAGE_ARCHITECTURE2_NEUTRAL: APPX_PACKAGE_ARCHITECTURE2 = 11
APPX_PACKAGE_ARCHITECTURE2_ARM64: APPX_PACKAGE_ARCHITECTURE2 = 12
APPX_PACKAGE_ARCHITECTURE2_X86_ON_ARM64: APPX_PACKAGE_ARCHITECTURE2 = 14
APPX_PACKAGE_ARCHITECTURE2_UNKNOWN: APPX_PACKAGE_ARCHITECTURE2 = 65535
APPX_PACKAGE_EDITOR_UPDATE_PACKAGE_MANIFEST_OPTIONS = Int32
APPX_PACKAGE_EDITOR_UPDATE_PACKAGE_MANIFEST_OPTION_NONE: APPX_PACKAGE_EDITOR_UPDATE_PACKAGE_MANIFEST_OPTIONS = 0
APPX_PACKAGE_EDITOR_UPDATE_PACKAGE_MANIFEST_OPTION_SKIP_VALIDATION: APPX_PACKAGE_EDITOR_UPDATE_PACKAGE_MANIFEST_OPTIONS = 1
APPX_PACKAGE_EDITOR_UPDATE_PACKAGE_MANIFEST_OPTION_LOCALIZED: APPX_PACKAGE_EDITOR_UPDATE_PACKAGE_MANIFEST_OPTIONS = 2
APPX_PACKAGE_EDITOR_UPDATE_PACKAGE_OPTION = Int32
APPX_PACKAGE_EDITOR_UPDATE_PACKAGE_OPTION_APPEND_DELTA: APPX_PACKAGE_EDITOR_UPDATE_PACKAGE_OPTION = 0
class APPX_PACKAGE_SETTINGS(EasyCastStructure):
    forceZip32: Windows.Win32.Foundation.BOOL
    hashMethod: Windows.Win32.System.Com.IUri_head
class APPX_PACKAGE_WRITER_PAYLOAD_STREAM(EasyCastStructure):
    inputStream: Windows.Win32.System.Com.IStream_head
    fileName: Windows.Win32.Foundation.PWSTR
    contentType: Windows.Win32.Foundation.PWSTR
    compressionOption: Windows.Win32.Storage.Packaging.Appx.APPX_COMPRESSION_OPTION
APPX_PACKAGING_CONTEXT_CHANGE_TYPE = Int32
APPX_PACKAGING_CONTEXT_CHANGE_TYPE_START: APPX_PACKAGING_CONTEXT_CHANGE_TYPE = 0
APPX_PACKAGING_CONTEXT_CHANGE_TYPE_CHANGE: APPX_PACKAGING_CONTEXT_CHANGE_TYPE = 1
APPX_PACKAGING_CONTEXT_CHANGE_TYPE_DETAILS: APPX_PACKAGING_CONTEXT_CHANGE_TYPE = 2
APPX_PACKAGING_CONTEXT_CHANGE_TYPE_END: APPX_PACKAGING_CONTEXT_CHANGE_TYPE = 3
AddPackageDependencyOptions = Int32
AddPackageDependencyOptions_None: AddPackageDependencyOptions = 0
AddPackageDependencyOptions_PrependIfRankCollision: AddPackageDependencyOptions = 1
PACKAGE_PROPERTY_FRAMEWORK: UInt32 = 1
PACKAGE_PROPERTY_RESOURCE: UInt32 = 2
PACKAGE_PROPERTY_BUNDLE: UInt32 = 4
PACKAGE_PROPERTY_OPTIONAL: UInt32 = 8
PACKAGE_FILTER_HEAD: UInt32 = 16
PACKAGE_FILTER_DIRECT: UInt32 = 32
PACKAGE_FILTER_RESOURCE: UInt32 = 64
PACKAGE_FILTER_BUNDLE: UInt32 = 128
PACKAGE_INFORMATION_BASIC: UInt32 = 0
PACKAGE_INFORMATION_FULL: UInt32 = 256
PACKAGE_PROPERTY_DEVELOPMENT_MODE: UInt32 = 65536
PACKAGE_FILTER_OPTIONAL: UInt32 = 131072
PACKAGE_PROPERTY_IS_IN_RELATED_SET: UInt32 = 262144
PACKAGE_FILTER_IS_IN_RELATED_SET: UInt32 = 262144
PACKAGE_PROPERTY_STATIC: UInt32 = 524288
PACKAGE_FILTER_STATIC: UInt32 = 524288
PACKAGE_PROPERTY_DYNAMIC: UInt32 = 1048576
PACKAGE_FILTER_DYNAMIC: UInt32 = 1048576
PACKAGE_PROPERTY_HOSTRUNTIME: UInt32 = 2097152
PACKAGE_FILTER_HOSTRUNTIME: UInt32 = 2097152
PACKAGE_FILTER_ALL_LOADED: UInt32 = 0
PACKAGE_DEPENDENCY_RANK_DEFAULT: UInt32 = 0
@winfunctype('KERNEL32.dll')
def GetCurrentPackageId(bufferLength: POINTER(UInt32), buffer: POINTER(Byte)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def GetCurrentPackageFullName(packageFullNameLength: POINTER(UInt32), packageFullName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def GetCurrentPackageFamilyName(packageFamilyNameLength: POINTER(UInt32), packageFamilyName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def GetCurrentPackagePath(pathLength: POINTER(UInt32), path: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def GetPackageId(hProcess: Windows.Win32.Foundation.HANDLE, bufferLength: POINTER(UInt32), buffer: POINTER(Byte)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def GetPackageFullName(hProcess: Windows.Win32.Foundation.HANDLE, packageFullNameLength: POINTER(UInt32), packageFullName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('api-ms-win-appmodel-runtime-l1-1-1.dll')
def GetPackageFullNameFromToken(token: Windows.Win32.Foundation.HANDLE, packageFullNameLength: POINTER(UInt32), packageFullName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def GetPackageFamilyName(hProcess: Windows.Win32.Foundation.HANDLE, packageFamilyNameLength: POINTER(UInt32), packageFamilyName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('api-ms-win-appmodel-runtime-l1-1-1.dll')
def GetPackageFamilyNameFromToken(token: Windows.Win32.Foundation.HANDLE, packageFamilyNameLength: POINTER(UInt32), packageFamilyName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def GetPackagePath(packageId: POINTER(Windows.Win32.Storage.Packaging.Appx.PACKAGE_ID_head), reserved: UInt32, pathLength: POINTER(UInt32), path: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def GetPackagePathByFullName(packageFullName: Windows.Win32.Foundation.PWSTR, pathLength: POINTER(UInt32), path: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def GetStagedPackagePathByFullName(packageFullName: Windows.Win32.Foundation.PWSTR, pathLength: POINTER(UInt32), path: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('api-ms-win-appmodel-runtime-l1-1-3.dll')
def GetPackagePathByFullName2(packageFullName: Windows.Win32.Foundation.PWSTR, packagePathType: Windows.Win32.Storage.Packaging.Appx.PackagePathType, pathLength: POINTER(UInt32), path: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('api-ms-win-appmodel-runtime-l1-1-3.dll')
def GetStagedPackagePathByFullName2(packageFullName: Windows.Win32.Foundation.PWSTR, packagePathType: Windows.Win32.Storage.Packaging.Appx.PackagePathType, pathLength: POINTER(UInt32), path: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('api-ms-win-appmodel-runtime-l1-1-3.dll')
def GetCurrentPackageInfo2(flags: UInt32, packagePathType: Windows.Win32.Storage.Packaging.Appx.PackagePathType, bufferLength: POINTER(UInt32), buffer: POINTER(Byte), count: POINTER(UInt32)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('api-ms-win-appmodel-runtime-l1-1-3.dll')
def GetCurrentPackagePath2(packagePathType: Windows.Win32.Storage.Packaging.Appx.PackagePathType, pathLength: POINTER(UInt32), path: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def GetCurrentApplicationUserModelId(applicationUserModelIdLength: POINTER(UInt32), applicationUserModelId: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def GetApplicationUserModelId(hProcess: Windows.Win32.Foundation.HANDLE, applicationUserModelIdLength: POINTER(UInt32), applicationUserModelId: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('api-ms-win-appmodel-runtime-l1-1-1.dll')
def GetApplicationUserModelIdFromToken(token: Windows.Win32.Foundation.HANDLE, applicationUserModelIdLength: POINTER(UInt32), applicationUserModelId: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('api-ms-win-appmodel-runtime-l1-1-1.dll')
def VerifyPackageFullName(packageFullName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('api-ms-win-appmodel-runtime-l1-1-1.dll')
def VerifyPackageFamilyName(packageFamilyName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('api-ms-win-appmodel-runtime-l1-1-1.dll')
def VerifyPackageId(packageId: POINTER(Windows.Win32.Storage.Packaging.Appx.PACKAGE_ID_head)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('api-ms-win-appmodel-runtime-l1-1-1.dll')
def VerifyApplicationUserModelId(applicationUserModelId: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('api-ms-win-appmodel-runtime-l1-1-1.dll')
def VerifyPackageRelativeApplicationId(packageRelativeApplicationId: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def PackageIdFromFullName(packageFullName: Windows.Win32.Foundation.PWSTR, flags: UInt32, bufferLength: POINTER(UInt32), buffer: POINTER(Byte)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def PackageFullNameFromId(packageId: POINTER(Windows.Win32.Storage.Packaging.Appx.PACKAGE_ID_head), packageFullNameLength: POINTER(UInt32), packageFullName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def PackageFamilyNameFromId(packageId: POINTER(Windows.Win32.Storage.Packaging.Appx.PACKAGE_ID_head), packageFamilyNameLength: POINTER(UInt32), packageFamilyName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def PackageFamilyNameFromFullName(packageFullName: Windows.Win32.Foundation.PWSTR, packageFamilyNameLength: POINTER(UInt32), packageFamilyName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def PackageNameAndPublisherIdFromFamilyName(packageFamilyName: Windows.Win32.Foundation.PWSTR, packageNameLength: POINTER(UInt32), packageName: Windows.Win32.Foundation.PWSTR, packagePublisherIdLength: POINTER(UInt32), packagePublisherId: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def FormatApplicationUserModelId(packageFamilyName: Windows.Win32.Foundation.PWSTR, packageRelativeApplicationId: Windows.Win32.Foundation.PWSTR, applicationUserModelIdLength: POINTER(UInt32), applicationUserModelId: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def ParseApplicationUserModelId(applicationUserModelId: Windows.Win32.Foundation.PWSTR, packageFamilyNameLength: POINTER(UInt32), packageFamilyName: Windows.Win32.Foundation.PWSTR, packageRelativeApplicationIdLength: POINTER(UInt32), packageRelativeApplicationId: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def GetPackagesByPackageFamily(packageFamilyName: Windows.Win32.Foundation.PWSTR, count: POINTER(UInt32), packageFullNames: POINTER(Windows.Win32.Foundation.PWSTR), bufferLength: POINTER(UInt32), buffer: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def FindPackagesByPackageFamily(packageFamilyName: Windows.Win32.Foundation.PWSTR, packageFilters: UInt32, count: POINTER(UInt32), packageFullNames: POINTER(Windows.Win32.Foundation.PWSTR), bufferLength: POINTER(UInt32), buffer: Windows.Win32.Foundation.PWSTR, packageProperties: POINTER(UInt32)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('api-ms-win-appmodel-runtime-l1-1-1.dll')
def GetStagedPackageOrigin(packageFullName: Windows.Win32.Foundation.PWSTR, origin: POINTER(Windows.Win32.Storage.Packaging.Appx.PackageOrigin)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def GetCurrentPackageInfo(flags: UInt32, bufferLength: POINTER(UInt32), buffer: POINTER(Byte), count: POINTER(UInt32)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def OpenPackageInfoByFullName(packageFullName: Windows.Win32.Foundation.PWSTR, reserved: UInt32, packageInfoReference: POINTER(POINTER(Windows.Win32.Storage.Packaging.Appx._PACKAGE_INFO_REFERENCE_head))) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('api-ms-win-appmodel-runtime-l1-1-1.dll')
def OpenPackageInfoByFullNameForUser(userSid: Windows.Win32.Foundation.PSID, packageFullName: Windows.Win32.Foundation.PWSTR, reserved: UInt32, packageInfoReference: POINTER(POINTER(Windows.Win32.Storage.Packaging.Appx._PACKAGE_INFO_REFERENCE_head))) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def ClosePackageInfo(packageInfoReference: POINTER(Windows.Win32.Storage.Packaging.Appx._PACKAGE_INFO_REFERENCE_head)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def GetPackageInfo(packageInfoReference: POINTER(Windows.Win32.Storage.Packaging.Appx._PACKAGE_INFO_REFERENCE_head), flags: UInt32, bufferLength: POINTER(UInt32), buffer: POINTER(Byte), count: POINTER(UInt32)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def GetPackageApplicationIds(packageInfoReference: POINTER(Windows.Win32.Storage.Packaging.Appx._PACKAGE_INFO_REFERENCE_head), bufferLength: POINTER(UInt32), buffer: POINTER(Byte), count: POINTER(UInt32)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('api-ms-win-appmodel-runtime-l1-1-3.dll')
def GetPackageInfo2(packageInfoReference: POINTER(Windows.Win32.Storage.Packaging.Appx._PACKAGE_INFO_REFERENCE_head), flags: UInt32, packagePathType: Windows.Win32.Storage.Packaging.Appx.PackagePathType, bufferLength: POINTER(UInt32), buffer: POINTER(Byte), count: POINTER(UInt32)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def CheckIsMSIXPackage(packageFullName: Windows.Win32.Foundation.PWSTR, isMSIXPackage: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNELBASE.dll')
def TryCreatePackageDependency(user: Windows.Win32.Foundation.PSID, packageFamilyName: Windows.Win32.Foundation.PWSTR, minVersion: Windows.Win32.Storage.Packaging.Appx.PACKAGE_VERSION, packageDependencyProcessorArchitectures: Windows.Win32.Storage.Packaging.Appx.PackageDependencyProcessorArchitectures, lifetimeKind: Windows.Win32.Storage.Packaging.Appx.PackageDependencyLifetimeKind, lifetimeArtifact: Windows.Win32.Foundation.PWSTR, options: Windows.Win32.Storage.Packaging.Appx.CreatePackageDependencyOptions, packageDependencyId: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNELBASE.dll')
def DeletePackageDependency(packageDependencyId: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNELBASE.dll')
def AddPackageDependency(packageDependencyId: Windows.Win32.Foundation.PWSTR, rank: Int32, options: Windows.Win32.Storage.Packaging.Appx.AddPackageDependencyOptions, packageDependencyContext: POINTER(POINTER(Windows.Win32.Storage.Packaging.Appx.PACKAGEDEPENDENCY_CONTEXT___head)), packageFullName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNELBASE.dll')
def RemovePackageDependency(packageDependencyContext: POINTER(Windows.Win32.Storage.Packaging.Appx.PACKAGEDEPENDENCY_CONTEXT___head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNELBASE.dll')
def GetResolvedPackageFullNameForPackageDependency(packageDependencyId: Windows.Win32.Foundation.PWSTR, packageFullName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNELBASE.dll')
def GetIdForPackageDependencyContext(packageDependencyContext: POINTER(Windows.Win32.Storage.Packaging.Appx.PACKAGEDEPENDENCY_CONTEXT___head), packageDependencyId: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def AppPolicyGetLifecycleManagement(processToken: Windows.Win32.Foundation.HANDLE, policy: POINTER(Windows.Win32.Storage.Packaging.Appx.AppPolicyLifecycleManagement)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def AppPolicyGetWindowingModel(processToken: Windows.Win32.Foundation.HANDLE, policy: POINTER(Windows.Win32.Storage.Packaging.Appx.AppPolicyWindowingModel)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def AppPolicyGetMediaFoundationCodecLoading(processToken: Windows.Win32.Foundation.HANDLE, policy: POINTER(Windows.Win32.Storage.Packaging.Appx.AppPolicyMediaFoundationCodecLoading)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def AppPolicyGetClrCompat(processToken: Windows.Win32.Foundation.HANDLE, policy: POINTER(Windows.Win32.Storage.Packaging.Appx.AppPolicyClrCompat)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def AppPolicyGetThreadInitializationType(processToken: Windows.Win32.Foundation.HANDLE, policy: POINTER(Windows.Win32.Storage.Packaging.Appx.AppPolicyThreadInitializationType)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def AppPolicyGetShowDeveloperDiagnostic(processToken: Windows.Win32.Foundation.HANDLE, policy: POINTER(Windows.Win32.Storage.Packaging.Appx.AppPolicyShowDeveloperDiagnostic)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def AppPolicyGetProcessTerminationMethod(processToken: Windows.Win32.Foundation.HANDLE, policy: POINTER(Windows.Win32.Storage.Packaging.Appx.AppPolicyProcessTerminationMethod)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def AppPolicyGetCreateFileAccess(processToken: Windows.Win32.Foundation.HANDLE, policy: POINTER(Windows.Win32.Storage.Packaging.Appx.AppPolicyCreateFileAccess)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def CreatePackageVirtualizationContext(packageFamilyName: Windows.Win32.Foundation.PWSTR, context: POINTER(POINTER(Windows.Win32.Storage.Packaging.Appx.PACKAGE_VIRTUALIZATION_CONTEXT_HANDLE___head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def ActivatePackageVirtualizationContext(context: POINTER(Windows.Win32.Storage.Packaging.Appx.PACKAGE_VIRTUALIZATION_CONTEXT_HANDLE___head), cookie: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def ReleasePackageVirtualizationContext(context: POINTER(Windows.Win32.Storage.Packaging.Appx.PACKAGE_VIRTUALIZATION_CONTEXT_HANDLE___head)) -> Void: ...
@winfunctype('KERNEL32.dll')
def DeactivatePackageVirtualizationContext(cookie: UIntPtr) -> Void: ...
@winfunctype('KERNEL32.dll')
def DuplicatePackageVirtualizationContext(sourceContext: POINTER(Windows.Win32.Storage.Packaging.Appx.PACKAGE_VIRTUALIZATION_CONTEXT_HANDLE___head), destContext: POINTER(POINTER(Windows.Win32.Storage.Packaging.Appx.PACKAGE_VIRTUALIZATION_CONTEXT_HANDLE___head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def GetCurrentPackageVirtualizationContext() -> POINTER(Windows.Win32.Storage.Packaging.Appx.PACKAGE_VIRTUALIZATION_CONTEXT_HANDLE___head): ...
@winfunctype('KERNEL32.dll')
def GetProcessesInVirtualizationContext(packageFamilyName: Windows.Win32.Foundation.PWSTR, count: POINTER(UInt32), processes: POINTER(POINTER(Windows.Win32.Foundation.HANDLE))) -> Windows.Win32.Foundation.HRESULT: ...
AppPolicyClrCompat = Int32
AppPolicyClrCompat_Other: AppPolicyClrCompat = 0
AppPolicyClrCompat_ClassicDesktop: AppPolicyClrCompat = 1
AppPolicyClrCompat_Universal: AppPolicyClrCompat = 2
AppPolicyClrCompat_PackagedDesktop: AppPolicyClrCompat = 3
AppPolicyCreateFileAccess = Int32
AppPolicyCreateFileAccess_Full: AppPolicyCreateFileAccess = 0
AppPolicyCreateFileAccess_Limited: AppPolicyCreateFileAccess = 1
AppPolicyLifecycleManagement = Int32
AppPolicyLifecycleManagement_Unmanaged: AppPolicyLifecycleManagement = 0
AppPolicyLifecycleManagement_Managed: AppPolicyLifecycleManagement = 1
AppPolicyMediaFoundationCodecLoading = Int32
AppPolicyMediaFoundationCodecLoading_All: AppPolicyMediaFoundationCodecLoading = 0
AppPolicyMediaFoundationCodecLoading_InboxOnly: AppPolicyMediaFoundationCodecLoading = 1
AppPolicyProcessTerminationMethod = Int32
AppPolicyProcessTerminationMethod_ExitProcess: AppPolicyProcessTerminationMethod = 0
AppPolicyProcessTerminationMethod_TerminateProcess: AppPolicyProcessTerminationMethod = 1
AppPolicyShowDeveloperDiagnostic = Int32
AppPolicyShowDeveloperDiagnostic_None: AppPolicyShowDeveloperDiagnostic = 0
AppPolicyShowDeveloperDiagnostic_ShowUI: AppPolicyShowDeveloperDiagnostic = 1
AppPolicyThreadInitializationType = Int32
AppPolicyThreadInitializationType_None: AppPolicyThreadInitializationType = 0
AppPolicyThreadInitializationType_InitializeWinRT: AppPolicyThreadInitializationType = 1
AppPolicyWindowingModel = Int32
AppPolicyWindowingModel_None: AppPolicyWindowingModel = 0
AppPolicyWindowingModel_Universal: AppPolicyWindowingModel = 1
AppPolicyWindowingModel_ClassicDesktop: AppPolicyWindowingModel = 2
AppPolicyWindowingModel_ClassicPhone: AppPolicyWindowingModel = 3
AppxBundleFactory = Guid('378e0446-5384-43b7-88-77-e7-db-dd-88-34-46')
AppxEncryptionFactory = Guid('dc664fdd-d868-46ee-87-80-8d-19-6c-b7-39-f7')
AppxFactory = Guid('5842a140-ff9f-4166-8f-5c-62-f5-b7-b0-c7-81')
AppxPackageEditor = Guid('f004f2ca-aebc-4b0d-bf-58-e5-16-d5-bc-c0-ab')
AppxPackagingDiagnosticEventSinkManager = Guid('50ca0a46-1588-4161-8e-d2-ef-9e-46-9c-ed-5d')
CreatePackageDependencyOptions = Int32
CreatePackageDependencyOptions_None: CreatePackageDependencyOptions = 0
CreatePackageDependencyOptions_DoNotVerifyDependencyResolution: CreatePackageDependencyOptions = 1
CreatePackageDependencyOptions_ScopeIsSystem: CreatePackageDependencyOptions = 2
DX_FEATURE_LEVEL = Int32
DX_FEATURE_LEVEL_UNSPECIFIED: DX_FEATURE_LEVEL = 0
DX_FEATURE_LEVEL_9: DX_FEATURE_LEVEL = 1
DX_FEATURE_LEVEL_10: DX_FEATURE_LEVEL = 2
DX_FEATURE_LEVEL_11: DX_FEATURE_LEVEL = 3
class IAppxAppInstallerReader(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f35bc38c-1d2f-43db-a1-f4-58-64-30-d1-fe-d2')
    @commethod(3)
    def GetXmlDom(self, dom: POINTER(Windows.Win32.Data.Xml.MsXml.IXMLDOMDocument_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxBlockMapBlock(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('75cf3930-3244-4fe0-a8-c8-e0-bc-b2-70-b8-89')
    @commethod(3)
    def GetHash(self, bufferSize: POINTER(UInt32), buffer: POINTER(POINTER(Byte))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCompressedSize(self, size: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxBlockMapBlocksEnumerator(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('6b429b5b-36ef-479e-b9-eb-0c-14-82-b4-9e-16')
    @commethod(3)
    def GetCurrent(self, block: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxBlockMapBlock_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHasCurrent(self, hasCurrent: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MoveNext(self, hasNext: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxBlockMapFile(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('277672ac-4f63-42c1-8a-bc-be-ae-36-00-eb-59')
    @commethod(3)
    def GetBlocks(self, blocks: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxBlockMapBlocksEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLocalFileHeaderSize(self, lfhSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetName(self, name: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetUncompressedSize(self, size: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ValidateFileHash(self, fileStream: Windows.Win32.System.Com.IStream_head, isValid: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxBlockMapFilesEnumerator(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('02b856a2-4262-4070-ba-cb-1a-8c-bb-c4-23-05')
    @commethod(3)
    def GetCurrent(self, file: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxBlockMapFile_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHasCurrent(self, hasCurrent: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MoveNext(self, hasCurrent: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxBlockMapReader(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('5efec991-bca3-42d1-9e-c2-e9-2d-60-9e-c2-2a')
    @commethod(3)
    def GetFile(self, filename: Windows.Win32.Foundation.PWSTR, file: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxBlockMapFile_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFiles(self, enumerator: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxBlockMapFilesEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetHashMethod(self, hashMethod: POINTER(Windows.Win32.System.Com.IUri_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetStream(self, blockMapStream: POINTER(Windows.Win32.System.Com.IStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxBundleFactory(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('bba65864-965f-4a5f-85-5f-f0-74-bd-bf-3a-7b')
    @commethod(3)
    def CreateBundleWriter(self, outputStream: Windows.Win32.System.Com.IStream_head, bundleVersion: UInt64, bundleWriter: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxBundleWriter_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateBundleReader(self, inputStream: Windows.Win32.System.Com.IStream_head, bundleReader: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxBundleReader_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateBundleManifestReader(self, inputStream: Windows.Win32.System.Com.IStream_head, manifestReader: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxBundleManifestReader_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxBundleFactory2(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('7325b83d-0185-42c4-82-ac-be-34-ab-1a-2a-8a')
    @commethod(3)
    def CreateBundleReader2(self, inputStream: Windows.Win32.System.Com.IStream_head, expectedDigest: Windows.Win32.Foundation.PWSTR, bundleReader: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxBundleReader_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxBundleManifestOptionalBundleInfo(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('515bf2e8-bcb0-4d69-8c-48-e3-83-14-7b-6e-12')
    @commethod(3)
    def GetPackageId(self, packageId: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxManifestPackageId_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFileName(self, fileName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPackageInfoItems(self, packageInfoItems: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxBundleManifestPackageInfoEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxBundleManifestOptionalBundleInfoEnumerator(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('9a178793-f97e-46ac-aa-ca-dd-5b-a4-c1-77-c8')
    @commethod(3)
    def GetCurrent(self, optionalBundle: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxBundleManifestOptionalBundleInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHasCurrent(self, hasCurrent: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MoveNext(self, hasNext: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxBundleManifestPackageInfo(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('54cd06c1-268f-40bb-8e-d2-75-7a-9e-ba-ec-8d')
    @commethod(3)
    def GetPackageType(self, packageType: POINTER(Windows.Win32.Storage.Packaging.Appx.APPX_BUNDLE_PAYLOAD_PACKAGE_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPackageId(self, packageId: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxManifestPackageId_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetFileName(self, fileName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetOffset(self, offset: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetSize(self, size: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetResources(self, resources: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxManifestQualifiedResourcesEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxBundleManifestPackageInfo2(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('44c2acbc-b2cf-4ccb-bb-db-9c-6d-a8-c3-bc-9e')
    @commethod(3)
    def GetIsPackageReference(self, isPackageReference: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetIsNonQualifiedResourcePackage(self, isNonQualifiedResourcePackage: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetIsDefaultApplicablePackage(self, isDefaultApplicablePackage: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxBundleManifestPackageInfo3(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('6ba74b98-bb74-4296-80-d0-5f-42-56-a9-96-75')
    @commethod(3)
    def GetTargetDeviceFamilies(self, targetDeviceFamilies: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxManifestTargetDeviceFamiliesEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxBundleManifestPackageInfo4(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('5da6f13d-a8a7-4532-85-7c-13-93-d6-59-37-1d')
    @commethod(3)
    def GetIsStub(self, isStub: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxBundleManifestPackageInfoEnumerator(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f9b856ee-49a6-4e19-b2-b0-6a-24-06-d6-3a-32')
    @commethod(3)
    def GetCurrent(self, packageInfo: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxBundleManifestPackageInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHasCurrent(self, hasCurrent: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MoveNext(self, hasNext: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxBundleManifestReader(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('cf0ebbc1-cc99-4106-91-eb-e6-74-62-e0-4f-b0')
    @commethod(3)
    def GetPackageId(self, packageId: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxManifestPackageId_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPackageInfoItems(self, packageInfoItems: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxBundleManifestPackageInfoEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetStream(self, manifestStream: POINTER(Windows.Win32.System.Com.IStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxBundleManifestReader2(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('5517df70-033f-4af2-82-13-87-d7-66-80-5c-02')
    @commethod(3)
    def GetOptionalBundles(self, optionalBundles: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxBundleManifestOptionalBundleInfoEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxBundleReader(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dd75b8c0-ba76-43b0-ae-0f-68-65-6a-1d-c5-c8')
    @commethod(3)
    def GetFootprintFile(self, fileType: Windows.Win32.Storage.Packaging.Appx.APPX_BUNDLE_FOOTPRINT_FILE_TYPE, footprintFile: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxFile_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetBlockMap(self, blockMapReader: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxBlockMapReader_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetManifest(self, manifestReader: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxBundleManifestReader_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPayloadPackages(self, payloadPackages: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxFilesEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetPayloadPackage(self, fileName: Windows.Win32.Foundation.PWSTR, payloadPackage: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxFile_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxBundleWriter(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('ec446fe8-bfec-4c64-ab-4f-49-f0-38-f0-c6-d2')
    @commethod(3)
    def AddPayloadPackage(self, fileName: Windows.Win32.Foundation.PWSTR, packageStream: Windows.Win32.System.Com.IStream_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Close(self) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxBundleWriter2(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('6d8fe971-01cc-49a0-b6-85-23-38-51-27-99-62')
    @commethod(3)
    def AddExternalPackageReference(self, fileName: Windows.Win32.Foundation.PWSTR, inputStream: Windows.Win32.System.Com.IStream_head) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxBundleWriter3(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('ad711152-f969-4193-82-d5-9d-df-27-86-d2-1a')
    @commethod(3)
    def AddPackageReference(self, fileName: Windows.Win32.Foundation.PWSTR, inputStream: Windows.Win32.System.Com.IStream_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Close(self, hashMethodString: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxBundleWriter4(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('9cd9d523-5009-4c01-98-82-dc-02-9f-bd-47-a3')
    @commethod(3)
    def AddPayloadPackage(self, fileName: Windows.Win32.Foundation.PWSTR, packageStream: Windows.Win32.System.Com.IStream_head, isDefaultApplicablePackage: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddPackageReference(self, fileName: Windows.Win32.Foundation.PWSTR, inputStream: Windows.Win32.System.Com.IStream_head, isDefaultApplicablePackage: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddExternalPackageReference(self, fileName: Windows.Win32.Foundation.PWSTR, inputStream: Windows.Win32.System.Com.IStream_head, isDefaultApplicablePackage: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxContentGroup(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('328f6468-c04f-4e3c-b6-fa-6b-8d-27-f3-00-3a')
    @commethod(3)
    def GetName(self, groupName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFiles(self, enumerator: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxContentGroupFilesEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxContentGroupFilesEnumerator(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1a09a2fd-7440-44eb-8c-84-84-82-05-a6-a1-cc')
    @commethod(3)
    def GetCurrent(self, file: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHasCurrent(self, hasCurrent: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MoveNext(self, hasNext: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxContentGroupMapReader(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('418726d8-dd99-4f5d-98-86-15-7a-dd-20-de-01')
    @commethod(3)
    def GetRequiredGroup(self, requiredGroup: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxContentGroup_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAutomaticGroups(self, automaticGroupsEnumerator: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxContentGroupsEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxContentGroupMapWriter(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d07ab776-a9de-4798-8c-14-3d-b3-1e-68-7c-78')
    @commethod(3)
    def AddAutomaticGroup(self, groupName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddAutomaticFile(self, fileName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Close(self) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxContentGroupsEnumerator(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('3264e477-16d1-4d63-82-3e-7d-29-84-69-66-34')
    @commethod(3)
    def GetCurrent(self, stream: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxContentGroup_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHasCurrent(self, hasCurrent: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MoveNext(self, hasNext: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxDigestProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('9fe2702b-7640-4659-8e-6c-34-9e-43-c4-cd-bd')
    @commethod(3)
    def GetDigest(self, digest: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxEncryptedBundleWriter(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('80b0902f-7bf0-4117-b8-c6-42-79-ef-81-ee-77')
    @commethod(3)
    def AddPayloadPackageEncrypted(self, fileName: Windows.Win32.Foundation.PWSTR, packageStream: Windows.Win32.System.Com.IStream_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Close(self) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxEncryptedBundleWriter2(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('e644be82-f0fa-42b8-a9-56-8d-1c-b4-8e-e3-79')
    @commethod(3)
    def AddExternalPackageReference(self, fileName: Windows.Win32.Foundation.PWSTR, inputStream: Windows.Win32.System.Com.IStream_head) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxEncryptedBundleWriter3(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('0d34deb3-5cae-4dd3-97-7c-50-49-32-a5-1d-31')
    @commethod(3)
    def AddPayloadPackageEncrypted(self, fileName: Windows.Win32.Foundation.PWSTR, packageStream: Windows.Win32.System.Com.IStream_head, isDefaultApplicablePackage: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddExternalPackageReference(self, fileName: Windows.Win32.Foundation.PWSTR, inputStream: Windows.Win32.System.Com.IStream_head, isDefaultApplicablePackage: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxEncryptedPackageWriter(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f43d0b0b-1379-40e2-9b-29-68-2e-a2-bf-42-af')
    @commethod(3)
    def AddPayloadFileEncrypted(self, fileName: Windows.Win32.Foundation.PWSTR, compressionOption: Windows.Win32.Storage.Packaging.Appx.APPX_COMPRESSION_OPTION, inputStream: Windows.Win32.System.Com.IStream_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Close(self) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxEncryptedPackageWriter2(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('3e475447-3a25-40b5-8a-d2-f9-53-ae-50-c9-2d')
    @commethod(3)
    def AddPayloadFilesEncrypted(self, fileCount: UInt32, payloadFiles: POINTER(Windows.Win32.Storage.Packaging.Appx.APPX_PACKAGE_WRITER_PAYLOAD_STREAM_head), memoryLimit: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxEncryptionFactory(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('80e8e04d-8c88-44ae-a0-11-7c-ad-f6-fb-2e-72')
    @commethod(3)
    def EncryptPackage(self, inputStream: Windows.Win32.System.Com.IStream_head, outputStream: Windows.Win32.System.Com.IStream_head, settings: POINTER(Windows.Win32.Storage.Packaging.Appx.APPX_ENCRYPTED_PACKAGE_SETTINGS_head), keyInfo: POINTER(Windows.Win32.Storage.Packaging.Appx.APPX_KEY_INFO_head), exemptedFiles: POINTER(Windows.Win32.Storage.Packaging.Appx.APPX_ENCRYPTED_EXEMPTIONS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DecryptPackage(self, inputStream: Windows.Win32.System.Com.IStream_head, outputStream: Windows.Win32.System.Com.IStream_head, keyInfo: POINTER(Windows.Win32.Storage.Packaging.Appx.APPX_KEY_INFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateEncryptedPackageWriter(self, outputStream: Windows.Win32.System.Com.IStream_head, manifestStream: Windows.Win32.System.Com.IStream_head, settings: POINTER(Windows.Win32.Storage.Packaging.Appx.APPX_ENCRYPTED_PACKAGE_SETTINGS_head), keyInfo: POINTER(Windows.Win32.Storage.Packaging.Appx.APPX_KEY_INFO_head), exemptedFiles: POINTER(Windows.Win32.Storage.Packaging.Appx.APPX_ENCRYPTED_EXEMPTIONS_head), packageWriter: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxEncryptedPackageWriter_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateEncryptedPackageReader(self, inputStream: Windows.Win32.System.Com.IStream_head, keyInfo: POINTER(Windows.Win32.Storage.Packaging.Appx.APPX_KEY_INFO_head), packageReader: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxPackageReader_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def EncryptBundle(self, inputStream: Windows.Win32.System.Com.IStream_head, outputStream: Windows.Win32.System.Com.IStream_head, settings: POINTER(Windows.Win32.Storage.Packaging.Appx.APPX_ENCRYPTED_PACKAGE_SETTINGS_head), keyInfo: POINTER(Windows.Win32.Storage.Packaging.Appx.APPX_KEY_INFO_head), exemptedFiles: POINTER(Windows.Win32.Storage.Packaging.Appx.APPX_ENCRYPTED_EXEMPTIONS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def DecryptBundle(self, inputStream: Windows.Win32.System.Com.IStream_head, outputStream: Windows.Win32.System.Com.IStream_head, keyInfo: POINTER(Windows.Win32.Storage.Packaging.Appx.APPX_KEY_INFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def CreateEncryptedBundleWriter(self, outputStream: Windows.Win32.System.Com.IStream_head, bundleVersion: UInt64, settings: POINTER(Windows.Win32.Storage.Packaging.Appx.APPX_ENCRYPTED_PACKAGE_SETTINGS_head), keyInfo: POINTER(Windows.Win32.Storage.Packaging.Appx.APPX_KEY_INFO_head), exemptedFiles: POINTER(Windows.Win32.Storage.Packaging.Appx.APPX_ENCRYPTED_EXEMPTIONS_head), bundleWriter: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxEncryptedBundleWriter_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def CreateEncryptedBundleReader(self, inputStream: Windows.Win32.System.Com.IStream_head, keyInfo: POINTER(Windows.Win32.Storage.Packaging.Appx.APPX_KEY_INFO_head), bundleReader: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxBundleReader_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxEncryptionFactory2(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c1b11eee-c4ba-4ab2-a5-5d-d0-15-fe-8f-f6-4f')
    @commethod(3)
    def CreateEncryptedPackageWriter(self, outputStream: Windows.Win32.System.Com.IStream_head, manifestStream: Windows.Win32.System.Com.IStream_head, contentGroupMapStream: Windows.Win32.System.Com.IStream_head, settings: POINTER(Windows.Win32.Storage.Packaging.Appx.APPX_ENCRYPTED_PACKAGE_SETTINGS_head), keyInfo: POINTER(Windows.Win32.Storage.Packaging.Appx.APPX_KEY_INFO_head), exemptedFiles: POINTER(Windows.Win32.Storage.Packaging.Appx.APPX_ENCRYPTED_EXEMPTIONS_head), packageWriter: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxEncryptedPackageWriter_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxEncryptionFactory3(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('09edca37-cd64-47d6-b7-e8-1c-b1-1d-4f-7e-05')
    @commethod(3)
    def EncryptPackage(self, inputStream: Windows.Win32.System.Com.IStream_head, outputStream: Windows.Win32.System.Com.IStream_head, settings: POINTER(Windows.Win32.Storage.Packaging.Appx.APPX_ENCRYPTED_PACKAGE_SETTINGS2_head), keyInfo: POINTER(Windows.Win32.Storage.Packaging.Appx.APPX_KEY_INFO_head), exemptedFiles: POINTER(Windows.Win32.Storage.Packaging.Appx.APPX_ENCRYPTED_EXEMPTIONS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateEncryptedPackageWriter(self, outputStream: Windows.Win32.System.Com.IStream_head, manifestStream: Windows.Win32.System.Com.IStream_head, contentGroupMapStream: Windows.Win32.System.Com.IStream_head, settings: POINTER(Windows.Win32.Storage.Packaging.Appx.APPX_ENCRYPTED_PACKAGE_SETTINGS2_head), keyInfo: POINTER(Windows.Win32.Storage.Packaging.Appx.APPX_KEY_INFO_head), exemptedFiles: POINTER(Windows.Win32.Storage.Packaging.Appx.APPX_ENCRYPTED_EXEMPTIONS_head), packageWriter: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxEncryptedPackageWriter_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EncryptBundle(self, inputStream: Windows.Win32.System.Com.IStream_head, outputStream: Windows.Win32.System.Com.IStream_head, settings: POINTER(Windows.Win32.Storage.Packaging.Appx.APPX_ENCRYPTED_PACKAGE_SETTINGS2_head), keyInfo: POINTER(Windows.Win32.Storage.Packaging.Appx.APPX_KEY_INFO_head), exemptedFiles: POINTER(Windows.Win32.Storage.Packaging.Appx.APPX_ENCRYPTED_EXEMPTIONS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateEncryptedBundleWriter(self, outputStream: Windows.Win32.System.Com.IStream_head, bundleVersion: UInt64, settings: POINTER(Windows.Win32.Storage.Packaging.Appx.APPX_ENCRYPTED_PACKAGE_SETTINGS2_head), keyInfo: POINTER(Windows.Win32.Storage.Packaging.Appx.APPX_KEY_INFO_head), exemptedFiles: POINTER(Windows.Win32.Storage.Packaging.Appx.APPX_ENCRYPTED_EXEMPTIONS_head), bundleWriter: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxEncryptedBundleWriter_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxEncryptionFactory4(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a879611f-12fd-41fe-85-d5-06-ae-77-9b-ba-f5')
    @commethod(3)
    def EncryptPackage(self, inputStream: Windows.Win32.System.Com.IStream_head, outputStream: Windows.Win32.System.Com.IStream_head, settings: POINTER(Windows.Win32.Storage.Packaging.Appx.APPX_ENCRYPTED_PACKAGE_SETTINGS2_head), keyInfo: POINTER(Windows.Win32.Storage.Packaging.Appx.APPX_KEY_INFO_head), exemptedFiles: POINTER(Windows.Win32.Storage.Packaging.Appx.APPX_ENCRYPTED_EXEMPTIONS_head), memoryLimit: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxEncryptionFactory5(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('68d6e77a-f446-480f-b0-f0-d9-1a-24-c6-07-46')
    @commethod(3)
    def CreateEncryptedPackageReader2(self, inputStream: Windows.Win32.System.Com.IStream_head, keyInfo: POINTER(Windows.Win32.Storage.Packaging.Appx.APPX_KEY_INFO_head), expectedDigest: Windows.Win32.Foundation.PWSTR, packageReader: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxPackageReader_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateEncryptedBundleReader2(self, inputStream: Windows.Win32.System.Com.IStream_head, keyInfo: POINTER(Windows.Win32.Storage.Packaging.Appx.APPX_KEY_INFO_head), expectedDigest: Windows.Win32.Foundation.PWSTR, bundleReader: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxBundleReader_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxFactory(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('beb94909-e451-438b-b5-a7-d7-9e-76-7b-75-d8')
    @commethod(3)
    def CreatePackageWriter(self, outputStream: Windows.Win32.System.Com.IStream_head, settings: POINTER(Windows.Win32.Storage.Packaging.Appx.APPX_PACKAGE_SETTINGS_head), packageWriter: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxPackageWriter_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreatePackageReader(self, inputStream: Windows.Win32.System.Com.IStream_head, packageReader: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxPackageReader_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateManifestReader(self, inputStream: Windows.Win32.System.Com.IStream_head, manifestReader: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxManifestReader_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateBlockMapReader(self, inputStream: Windows.Win32.System.Com.IStream_head, blockMapReader: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxBlockMapReader_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateValidatedBlockMapReader(self, blockMapStream: Windows.Win32.System.Com.IStream_head, signatureFileName: Windows.Win32.Foundation.PWSTR, blockMapReader: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxBlockMapReader_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxFactory2(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f1346df2-c282-4e22-b9-18-74-3a-92-9a-8d-55')
    @commethod(3)
    def CreateContentGroupMapReader(self, inputStream: Windows.Win32.System.Com.IStream_head, contentGroupMapReader: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxContentGroupMapReader_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateSourceContentGroupMapReader(self, inputStream: Windows.Win32.System.Com.IStream_head, reader: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxSourceContentGroupMapReader_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateContentGroupMapWriter(self, stream: Windows.Win32.System.Com.IStream_head, contentGroupMapWriter: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxContentGroupMapWriter_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxFactory3(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('776b2c05-e21d-4e24-ba-1a-cd-52-9a-8b-fd-bb')
    @commethod(3)
    def CreatePackageReader2(self, inputStream: Windows.Win32.System.Com.IStream_head, expectedDigest: Windows.Win32.Foundation.PWSTR, packageReader: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxPackageReader_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateManifestReader2(self, inputStream: Windows.Win32.System.Com.IStream_head, expectedDigest: Windows.Win32.Foundation.PWSTR, manifestReader: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxManifestReader_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateAppInstallerReader(self, inputStream: Windows.Win32.System.Com.IStream_head, expectedDigest: Windows.Win32.Foundation.PWSTR, appInstallerReader: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxAppInstallerReader_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxFile(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('91df827b-94fd-468f-82-7b-57-f4-1b-2f-6f-2e')
    @commethod(3)
    def GetCompressionOption(self, compressionOption: POINTER(Windows.Win32.Storage.Packaging.Appx.APPX_COMPRESSION_OPTION)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetContentType(self, contentType: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetName(self, fileName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSize(self, size: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetStream(self, stream: POINTER(Windows.Win32.System.Com.IStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxFilesEnumerator(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f007eeaf-9831-411c-98-47-91-7c-dc-62-d1-fe')
    @commethod(3)
    def GetCurrent(self, file: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxFile_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHasCurrent(self, hasCurrent: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MoveNext(self, hasNext: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestApplication(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('5da89bf4-3773-46be-b6-50-7e-74-48-63-b7-e8')
    @commethod(3)
    def GetStringValue(self, name: Windows.Win32.Foundation.PWSTR, value: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAppUserModelId(self, appUserModelId: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestApplicationsEnumerator(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('9eb8a55a-f04b-4d0d-80-8d-68-61-85-d4-84-7a')
    @commethod(3)
    def GetCurrent(self, application: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxManifestApplication_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHasCurrent(self, hasCurrent: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MoveNext(self, hasNext: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestCapabilitiesEnumerator(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('11d22258-f470-42c1-b2-91-83-61-c5-43-7e-41')
    @commethod(3)
    def GetCurrent(self, capability: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHasCurrent(self, hasCurrent: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MoveNext(self, hasNext: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestDeviceCapabilitiesEnumerator(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('30204541-427b-4a1c-ba-cf-65-5b-f4-63-a5-40')
    @commethod(3)
    def GetCurrent(self, deviceCapability: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHasCurrent(self, hasCurrent: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MoveNext(self, hasNext: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestDriverConstraint(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c031bee4-bbcc-48ea-a2-37-c3-40-45-c8-0a-07')
    @commethod(3)
    def GetName(self, name: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMinVersion(self, minVersion: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetMinDate(self, minDate: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestDriverConstraintsEnumerator(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d402b2d1-f600-49e0-95-e6-97-5d-8d-a1-3d-89')
    @commethod(3)
    def GetCurrent(self, driverConstraint: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxManifestDriverConstraint_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHasCurrent(self, hasCurrent: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MoveNext(self, hasNext: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestDriverDependenciesEnumerator(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('fe039db2-467f-4755-84-04-8f-5e-b6-86-5b-33')
    @commethod(3)
    def GetCurrent(self, driverDependency: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxManifestDriverDependency_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHasCurrent(self, hasCurrent: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MoveNext(self, hasNext: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestDriverDependency(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1210cb94-5a92-4602-be-24-79-f3-18-af-4a-f9')
    @commethod(3)
    def GetDriverConstraints(self, driverConstraints: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxManifestDriverConstraintsEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestHostRuntimeDependenciesEnumerator(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('6427a646-7f49-433e-b1-a6-0d-a3-09-f6-88-5a')
    @commethod(3)
    def GetCurrent(self, hostRuntimeDependency: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxManifestHostRuntimeDependency_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHasCurrent(self, hasCurrent: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MoveNext(self, hasNext: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestHostRuntimeDependency(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('3455d234-8414-410d-95-c7-7b-35-25-5b-83-91')
    @commethod(3)
    def GetName(self, name: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPublisher(self, publisher: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetMinVersion(self, minVersion: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestHostRuntimeDependency2(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c26f23a8-ee10-4ad6-b8-98-2b-4d-7a-eb-fe-6a')
    @commethod(3)
    def GetPackageFamilyName(self, packageFamilyName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestMainPackageDependenciesEnumerator(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a99c4f00-51d2-4f0f-ba-46-7e-d5-25-5e-bd-ff')
    @commethod(3)
    def GetCurrent(self, mainPackageDependency: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxManifestMainPackageDependency_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHasCurrent(self, hasCurrent: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MoveNext(self, hasNext: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestMainPackageDependency(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('05d0611c-bc29-46d5-97-e2-84-b9-c7-9b-d8-ae')
    @commethod(3)
    def GetName(self, name: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPublisher(self, publisher: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPackageFamilyName(self, packageFamilyName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestOSPackageDependenciesEnumerator(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b84e2fc3-f8ec-4bc1-8a-e2-15-63-46-f5-ff-ea')
    @commethod(3)
    def GetCurrent(self, osPackageDependency: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxManifestOSPackageDependency_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHasCurrent(self, hasCurrent: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MoveNext(self, hasNext: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestOSPackageDependency(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('154995ee-54a6-4f14-ac-97-d8-cf-05-19-64-4b')
    @commethod(3)
    def GetName(self, name: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetVersion(self, version: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestOptionalPackageInfo(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('2634847d-5b5d-4fe5-a2-43-00-2f-f9-5e-dc-7e')
    @commethod(3)
    def GetIsOptionalPackage(self, isOptionalPackage: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMainPackageName(self, mainPackageName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestPackageDependenciesEnumerator(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b43bbcf9-65a6-42dd-ba-c0-8c-67-41-e7-f5-a4')
    @commethod(3)
    def GetCurrent(self, dependency: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxManifestPackageDependency_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHasCurrent(self, hasCurrent: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MoveNext(self, hasNext: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestPackageDependency(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('e4946b59-733e-43f0-a7-24-3b-de-4c-12-85-a0')
    @commethod(3)
    def GetName(self, name: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPublisher(self, publisher: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetMinVersion(self, minVersion: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestPackageDependency2(c_void_p):
    extends: Windows.Win32.Storage.Packaging.Appx.IAppxManifestPackageDependency
    Guid = Guid('dda0b713-f3ff-49d3-89-8a-27-86-78-0c-5d-98')
    @commethod(6)
    def GetMaxMajorVersionTested(self, maxMajorVersionTested: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestPackageDependency3(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1ac56374-6198-4d6b-92-e4-74-9d-5a-b8-a8-95')
    @commethod(3)
    def GetIsOptional(self, isOptional: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestPackageId(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('283ce2d7-7153-4a91-96-49-7a-0f-72-40-94-5f')
    @commethod(3)
    def GetName(self, name: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetArchitecture(self, architecture: POINTER(Windows.Win32.Storage.Packaging.Appx.APPX_PACKAGE_ARCHITECTURE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPublisher(self, publisher: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetVersion(self, packageVersion: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetResourceId(self, resourceId: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ComparePublisher(self, other: Windows.Win32.Foundation.PWSTR, isSame: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetPackageFullName(self, packageFullName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetPackageFamilyName(self, packageFamilyName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestPackageId2(c_void_p):
    extends: Windows.Win32.Storage.Packaging.Appx.IAppxManifestPackageId
    Guid = Guid('2256999d-d617-42f1-88-0e-0b-a4-54-23-19-d5')
    @commethod(11)
    def GetArchitecture2(self, architecture: POINTER(Windows.Win32.Storage.Packaging.Appx.APPX_PACKAGE_ARCHITECTURE2)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestProperties(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('03faf64d-f26f-4b2c-aa-f7-8f-e7-78-9b-8b-ca')
    @commethod(3)
    def GetBoolValue(self, name: Windows.Win32.Foundation.PWSTR, value: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetStringValue(self, name: Windows.Win32.Foundation.PWSTR, value: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestQualifiedResource(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('3b53a497-3c5c-48d1-9e-a3-bb-7e-ac-8c-d7-d4')
    @commethod(3)
    def GetLanguage(self, language: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetScale(self, scale: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDXFeatureLevel(self, dxFeatureLevel: POINTER(Windows.Win32.Storage.Packaging.Appx.DX_FEATURE_LEVEL)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestQualifiedResourcesEnumerator(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('8ef6adfe-3762-4a8f-93-73-2f-c5-d4-44-c8-d2')
    @commethod(3)
    def GetCurrent(self, resource: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxManifestQualifiedResource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHasCurrent(self, hasCurrent: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MoveNext(self, hasNext: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestReader(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('4e1bd148-55a0-4480-a3-d1-15-54-47-10-63-7c')
    @commethod(3)
    def GetPackageId(self, packageId: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxManifestPackageId_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetProperties(self, packageProperties: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxManifestProperties_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPackageDependencies(self, dependencies: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxManifestPackageDependenciesEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCapabilities(self, capabilities: POINTER(Windows.Win32.Storage.Packaging.Appx.APPX_CAPABILITIES)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetResources(self, resources: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxManifestResourcesEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetDeviceCapabilities(self, deviceCapabilities: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxManifestDeviceCapabilitiesEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetPrerequisite(self, name: Windows.Win32.Foundation.PWSTR, value: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetApplications(self, applications: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxManifestApplicationsEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetStream(self, manifestStream: POINTER(Windows.Win32.System.Com.IStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestReader2(c_void_p):
    extends: Windows.Win32.Storage.Packaging.Appx.IAppxManifestReader
    Guid = Guid('d06f67bc-b31d-4eba-a8-af-63-8e-73-e7-7b-4d')
    @commethod(12)
    def GetQualifiedResources(self, resources: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxManifestQualifiedResourcesEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestReader3(c_void_p):
    extends: Windows.Win32.Storage.Packaging.Appx.IAppxManifestReader2
    Guid = Guid('c43825ab-69b7-400a-97-09-cc-37-f5-a7-2d-24')
    @commethod(13)
    def GetCapabilitiesByCapabilityClass(self, capabilityClass: Windows.Win32.Storage.Packaging.Appx.APPX_CAPABILITY_CLASS_TYPE, capabilities: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxManifestCapabilitiesEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetTargetDeviceFamilies(self, targetDeviceFamilies: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxManifestTargetDeviceFamiliesEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestReader4(c_void_p):
    extends: Windows.Win32.Storage.Packaging.Appx.IAppxManifestReader3
    Guid = Guid('4579bb7c-741d-4161-b5-a1-47-bd-3b-78-ad-9b')
    @commethod(15)
    def GetOptionalPackageInfo(self, optionalPackageInfo: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxManifestOptionalPackageInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestReader5(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('8d7ae132-a690-4c00-b7-5a-6a-ae-1f-ea-ac-80')
    @commethod(3)
    def GetMainPackageDependencies(self, mainPackageDependencies: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxManifestMainPackageDependenciesEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestReader6(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('34deaca4-d3c0-4e3e-b3-12-e4-26-25-e3-80-7e')
    @commethod(3)
    def GetIsNonQualifiedResourcePackage(self, isNonQualifiedResourcePackage: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestReader7(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('8efe6f27-0ce0-4988-b3-2d-73-8e-b6-3d-b3-b7')
    @commethod(3)
    def GetDriverDependencies(self, driverDependencies: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxManifestDriverDependenciesEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetOSPackageDependencies(self, osPackageDependencies: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxManifestOSPackageDependenciesEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetHostRuntimeDependencies(self, hostRuntimeDependencies: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxManifestHostRuntimeDependenciesEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestResourcesEnumerator(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('de4dfbbd-881a-48bb-85-8c-d6-f2-ba-ea-e6-ed')
    @commethod(3)
    def GetCurrent(self, resource: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHasCurrent(self, hasCurrent: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MoveNext(self, hasNext: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestTargetDeviceFamiliesEnumerator(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('36537f36-27a4-4788-88-c0-73-38-19-57-50-17')
    @commethod(3)
    def GetCurrent(self, targetDeviceFamily: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxManifestTargetDeviceFamily_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHasCurrent(self, hasCurrent: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MoveNext(self, hasNext: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestTargetDeviceFamily(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('9091b09b-c8d5-4f31-86-87-a3-38-25-9f-ae-fb')
    @commethod(3)
    def GetName(self, name: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMinVersion(self, minVersion: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetMaxVersionTested(self, maxVersionTested: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxPackageEditor(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('e2adb6dc-5e71-4416-86-b6-86-e5-f5-29-1a-6b')
    @commethod(3)
    def SetWorkingDirectory(self, workingDirectory: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateDeltaPackage(self, updatedPackageStream: Windows.Win32.System.Com.IStream_head, baselinePackageStream: Windows.Win32.System.Com.IStream_head, deltaPackageStream: Windows.Win32.System.Com.IStream_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateDeltaPackageUsingBaselineBlockMap(self, updatedPackageStream: Windows.Win32.System.Com.IStream_head, baselineBlockMapStream: Windows.Win32.System.Com.IStream_head, baselinePackageFullName: Windows.Win32.Foundation.PWSTR, deltaPackageStream: Windows.Win32.System.Com.IStream_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def UpdatePackage(self, baselinePackageStream: Windows.Win32.System.Com.IStream_head, deltaPackageStream: Windows.Win32.System.Com.IStream_head, updateOption: Windows.Win32.Storage.Packaging.Appx.APPX_PACKAGE_EDITOR_UPDATE_PACKAGE_OPTION) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def UpdateEncryptedPackage(self, baselineEncryptedPackageStream: Windows.Win32.System.Com.IStream_head, deltaPackageStream: Windows.Win32.System.Com.IStream_head, updateOption: Windows.Win32.Storage.Packaging.Appx.APPX_PACKAGE_EDITOR_UPDATE_PACKAGE_OPTION, settings: POINTER(Windows.Win32.Storage.Packaging.Appx.APPX_ENCRYPTED_PACKAGE_SETTINGS2_head), keyInfo: POINTER(Windows.Win32.Storage.Packaging.Appx.APPX_KEY_INFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def UpdatePackageManifest(self, packageStream: Windows.Win32.System.Com.IStream_head, updatedManifestStream: Windows.Win32.System.Com.IStream_head, isPackageEncrypted: Windows.Win32.Foundation.BOOL, options: Windows.Win32.Storage.Packaging.Appx.APPX_PACKAGE_EDITOR_UPDATE_PACKAGE_MANIFEST_OPTIONS) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxPackageReader(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b5c49650-99bc-481c-9a-34-3d-53-a4-10-67-08')
    @commethod(3)
    def GetBlockMap(self, blockMapReader: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxBlockMapReader_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFootprintFile(self, type: Windows.Win32.Storage.Packaging.Appx.APPX_FOOTPRINT_FILE_TYPE, file: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxFile_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPayloadFile(self, fileName: Windows.Win32.Foundation.PWSTR, file: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxFile_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPayloadFiles(self, filesEnumerator: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxFilesEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetManifest(self, manifestReader: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxManifestReader_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxPackageWriter(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('9099e33b-246f-41e4-88-1a-00-8e-b6-13-f8-58')
    @commethod(3)
    def AddPayloadFile(self, fileName: Windows.Win32.Foundation.PWSTR, contentType: Windows.Win32.Foundation.PWSTR, compressionOption: Windows.Win32.Storage.Packaging.Appx.APPX_COMPRESSION_OPTION, inputStream: Windows.Win32.System.Com.IStream_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Close(self, manifest: Windows.Win32.System.Com.IStream_head) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxPackageWriter2(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('2cf5c4fd-e54c-4ea5-ba-4e-f8-c4-b1-05-a8-c8')
    @commethod(3)
    def Close(self, manifest: Windows.Win32.System.Com.IStream_head, contentGroupMap: Windows.Win32.System.Com.IStream_head) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxPackageWriter3(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a83aacd3-41c0-4501-b8-a3-74-16-4f-50-b2-fd')
    @commethod(3)
    def AddPayloadFiles(self, fileCount: UInt32, payloadFiles: POINTER(Windows.Win32.Storage.Packaging.Appx.APPX_PACKAGE_WRITER_PAYLOAD_STREAM_head), memoryLimit: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxPackagingDiagnosticEventSink(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('17239d47-6adb-45d2-80-f6-f9-cb-c3-bf-05-9d')
    @commethod(3)
    def ReportContextChange(self, changeType: Windows.Win32.Storage.Packaging.Appx.APPX_PACKAGING_CONTEXT_CHANGE_TYPE, contextId: Int32, contextName: Windows.Win32.Foundation.PSTR, contextMessage: Windows.Win32.Foundation.PWSTR, detailsMessage: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ReportError(self, errorMessage: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxPackagingDiagnosticEventSinkManager(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('369648fa-a7eb-4909-a1-5d-69-54-a0-78-f1-8a')
    @commethod(3)
    def SetSinkForProcess(self, sink: Windows.Win32.Storage.Packaging.Appx.IAppxPackagingDiagnosticEventSink_head) -> Windows.Win32.Foundation.HRESULT: ...
class IAppxSourceContentGroupMapReader(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f329791d-540b-4a9f-bc-75-32-82-b7-d7-31-93')
    @commethod(3)
    def GetRequiredGroup(self, requiredGroup: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxContentGroup_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAutomaticGroups(self, automaticGroupsEnumerator: POINTER(Windows.Win32.Storage.Packaging.Appx.IAppxContentGroupsEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
class PACKAGEDEPENDENCY_CONTEXT__(EasyCastStructure):
    unused: Int32
class PACKAGE_ID(EasyCastStructure):
    reserved: UInt32
    processorArchitecture: UInt32
    version: Windows.Win32.Storage.Packaging.Appx.PACKAGE_VERSION
    name: Windows.Win32.Foundation.PWSTR
    publisher: Windows.Win32.Foundation.PWSTR
    resourceId: Windows.Win32.Foundation.PWSTR
    publisherId: Windows.Win32.Foundation.PWSTR
    _pack_ = 4
class PACKAGE_INFO(EasyCastStructure):
    reserved: UInt32
    flags: UInt32
    path: Windows.Win32.Foundation.PWSTR
    packageFullName: Windows.Win32.Foundation.PWSTR
    packageFamilyName: Windows.Win32.Foundation.PWSTR
    packageId: Windows.Win32.Storage.Packaging.Appx.PACKAGE_ID
    _pack_ = 4
class PACKAGE_VERSION(EasyCastStructure):
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Version: UInt64
        Anonymous: _Anonymous_e__Struct
        _pack_ = 4
        class _Anonymous_e__Struct(EasyCastStructure):
            Revision: UInt16
            Build: UInt16
            Minor: UInt16
            Major: UInt16
class PACKAGE_VIRTUALIZATION_CONTEXT_HANDLE__(EasyCastStructure):
    unused: Int32
PackageDependencyLifetimeKind = Int32
PackageDependencyLifetimeKind_Process: PackageDependencyLifetimeKind = 0
PackageDependencyLifetimeKind_FilePath: PackageDependencyLifetimeKind = 1
PackageDependencyLifetimeKind_RegistryKey: PackageDependencyLifetimeKind = 2
PackageDependencyProcessorArchitectures = Int32
PackageDependencyProcessorArchitectures_None: PackageDependencyProcessorArchitectures = 0
PackageDependencyProcessorArchitectures_Neutral: PackageDependencyProcessorArchitectures = 1
PackageDependencyProcessorArchitectures_X86: PackageDependencyProcessorArchitectures = 2
PackageDependencyProcessorArchitectures_X64: PackageDependencyProcessorArchitectures = 4
PackageDependencyProcessorArchitectures_Arm: PackageDependencyProcessorArchitectures = 8
PackageDependencyProcessorArchitectures_Arm64: PackageDependencyProcessorArchitectures = 16
PackageDependencyProcessorArchitectures_X86A64: PackageDependencyProcessorArchitectures = 32
PackageOrigin = Int32
PackageOrigin_Unknown: PackageOrigin = 0
PackageOrigin_Unsigned: PackageOrigin = 1
PackageOrigin_Inbox: PackageOrigin = 2
PackageOrigin_Store: PackageOrigin = 3
PackageOrigin_DeveloperUnsigned: PackageOrigin = 4
PackageOrigin_DeveloperSigned: PackageOrigin = 5
PackageOrigin_LineOfBusiness: PackageOrigin = 6
PackagePathType = Int32
PackagePathType_Install: PackagePathType = 0
PackagePathType_Mutable: PackagePathType = 1
PackagePathType_Effective: PackagePathType = 2
PackagePathType_MachineExternal: PackagePathType = 3
PackagePathType_UserExternal: PackagePathType = 4
PackagePathType_EffectiveExternal: PackagePathType = 5
class _PACKAGE_INFO_REFERENCE(EasyCastStructure):
    reserved: c_void_p
make_head(_module, 'APPX_ENCRYPTED_EXEMPTIONS')
make_head(_module, 'APPX_ENCRYPTED_PACKAGE_SETTINGS')
make_head(_module, 'APPX_ENCRYPTED_PACKAGE_SETTINGS2')
make_head(_module, 'APPX_KEY_INFO')
make_head(_module, 'APPX_PACKAGE_SETTINGS')
make_head(_module, 'APPX_PACKAGE_WRITER_PAYLOAD_STREAM')
make_head(_module, 'IAppxAppInstallerReader')
make_head(_module, 'IAppxBlockMapBlock')
make_head(_module, 'IAppxBlockMapBlocksEnumerator')
make_head(_module, 'IAppxBlockMapFile')
make_head(_module, 'IAppxBlockMapFilesEnumerator')
make_head(_module, 'IAppxBlockMapReader')
make_head(_module, 'IAppxBundleFactory')
make_head(_module, 'IAppxBundleFactory2')
make_head(_module, 'IAppxBundleManifestOptionalBundleInfo')
make_head(_module, 'IAppxBundleManifestOptionalBundleInfoEnumerator')
make_head(_module, 'IAppxBundleManifestPackageInfo')
make_head(_module, 'IAppxBundleManifestPackageInfo2')
make_head(_module, 'IAppxBundleManifestPackageInfo3')
make_head(_module, 'IAppxBundleManifestPackageInfo4')
make_head(_module, 'IAppxBundleManifestPackageInfoEnumerator')
make_head(_module, 'IAppxBundleManifestReader')
make_head(_module, 'IAppxBundleManifestReader2')
make_head(_module, 'IAppxBundleReader')
make_head(_module, 'IAppxBundleWriter')
make_head(_module, 'IAppxBundleWriter2')
make_head(_module, 'IAppxBundleWriter3')
make_head(_module, 'IAppxBundleWriter4')
make_head(_module, 'IAppxContentGroup')
make_head(_module, 'IAppxContentGroupFilesEnumerator')
make_head(_module, 'IAppxContentGroupMapReader')
make_head(_module, 'IAppxContentGroupMapWriter')
make_head(_module, 'IAppxContentGroupsEnumerator')
make_head(_module, 'IAppxDigestProvider')
make_head(_module, 'IAppxEncryptedBundleWriter')
make_head(_module, 'IAppxEncryptedBundleWriter2')
make_head(_module, 'IAppxEncryptedBundleWriter3')
make_head(_module, 'IAppxEncryptedPackageWriter')
make_head(_module, 'IAppxEncryptedPackageWriter2')
make_head(_module, 'IAppxEncryptionFactory')
make_head(_module, 'IAppxEncryptionFactory2')
make_head(_module, 'IAppxEncryptionFactory3')
make_head(_module, 'IAppxEncryptionFactory4')
make_head(_module, 'IAppxEncryptionFactory5')
make_head(_module, 'IAppxFactory')
make_head(_module, 'IAppxFactory2')
make_head(_module, 'IAppxFactory3')
make_head(_module, 'IAppxFile')
make_head(_module, 'IAppxFilesEnumerator')
make_head(_module, 'IAppxManifestApplication')
make_head(_module, 'IAppxManifestApplicationsEnumerator')
make_head(_module, 'IAppxManifestCapabilitiesEnumerator')
make_head(_module, 'IAppxManifestDeviceCapabilitiesEnumerator')
make_head(_module, 'IAppxManifestDriverConstraint')
make_head(_module, 'IAppxManifestDriverConstraintsEnumerator')
make_head(_module, 'IAppxManifestDriverDependenciesEnumerator')
make_head(_module, 'IAppxManifestDriverDependency')
make_head(_module, 'IAppxManifestHostRuntimeDependenciesEnumerator')
make_head(_module, 'IAppxManifestHostRuntimeDependency')
make_head(_module, 'IAppxManifestHostRuntimeDependency2')
make_head(_module, 'IAppxManifestMainPackageDependenciesEnumerator')
make_head(_module, 'IAppxManifestMainPackageDependency')
make_head(_module, 'IAppxManifestOSPackageDependenciesEnumerator')
make_head(_module, 'IAppxManifestOSPackageDependency')
make_head(_module, 'IAppxManifestOptionalPackageInfo')
make_head(_module, 'IAppxManifestPackageDependenciesEnumerator')
make_head(_module, 'IAppxManifestPackageDependency')
make_head(_module, 'IAppxManifestPackageDependency2')
make_head(_module, 'IAppxManifestPackageDependency3')
make_head(_module, 'IAppxManifestPackageId')
make_head(_module, 'IAppxManifestPackageId2')
make_head(_module, 'IAppxManifestProperties')
make_head(_module, 'IAppxManifestQualifiedResource')
make_head(_module, 'IAppxManifestQualifiedResourcesEnumerator')
make_head(_module, 'IAppxManifestReader')
make_head(_module, 'IAppxManifestReader2')
make_head(_module, 'IAppxManifestReader3')
make_head(_module, 'IAppxManifestReader4')
make_head(_module, 'IAppxManifestReader5')
make_head(_module, 'IAppxManifestReader6')
make_head(_module, 'IAppxManifestReader7')
make_head(_module, 'IAppxManifestResourcesEnumerator')
make_head(_module, 'IAppxManifestTargetDeviceFamiliesEnumerator')
make_head(_module, 'IAppxManifestTargetDeviceFamily')
make_head(_module, 'IAppxPackageEditor')
make_head(_module, 'IAppxPackageReader')
make_head(_module, 'IAppxPackageWriter')
make_head(_module, 'IAppxPackageWriter2')
make_head(_module, 'IAppxPackageWriter3')
make_head(_module, 'IAppxPackagingDiagnosticEventSink')
make_head(_module, 'IAppxPackagingDiagnosticEventSinkManager')
make_head(_module, 'IAppxSourceContentGroupMapReader')
make_head(_module, 'PACKAGEDEPENDENCY_CONTEXT__')
make_head(_module, 'PACKAGE_ID')
make_head(_module, 'PACKAGE_INFO')
make_head(_module, 'PACKAGE_VERSION')
make_head(_module, 'PACKAGE_VIRTUALIZATION_CONTEXT_HANDLE__')
make_head(_module, '_PACKAGE_INFO_REFERENCE')
