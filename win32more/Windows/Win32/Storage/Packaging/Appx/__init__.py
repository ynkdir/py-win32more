from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Data.Xml.MsXml
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Security
import win32more.Windows.Win32.Storage.Packaging.Appx
import win32more.Windows.Win32.System.Com
APPX_BUNDLE_FOOTPRINT_FILE_TYPE = Int32
APPX_BUNDLE_FOOTPRINT_FILE_TYPE_FIRST: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_BUNDLE_FOOTPRINT_FILE_TYPE = 0
APPX_BUNDLE_FOOTPRINT_FILE_TYPE_MANIFEST: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_BUNDLE_FOOTPRINT_FILE_TYPE = 0
APPX_BUNDLE_FOOTPRINT_FILE_TYPE_BLOCKMAP: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_BUNDLE_FOOTPRINT_FILE_TYPE = 1
APPX_BUNDLE_FOOTPRINT_FILE_TYPE_SIGNATURE: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_BUNDLE_FOOTPRINT_FILE_TYPE = 2
APPX_BUNDLE_FOOTPRINT_FILE_TYPE_LAST: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_BUNDLE_FOOTPRINT_FILE_TYPE = 2
APPX_BUNDLE_PAYLOAD_PACKAGE_TYPE = Int32
APPX_BUNDLE_PAYLOAD_PACKAGE_TYPE_APPLICATION: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_BUNDLE_PAYLOAD_PACKAGE_TYPE = 0
APPX_BUNDLE_PAYLOAD_PACKAGE_TYPE_RESOURCE: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_BUNDLE_PAYLOAD_PACKAGE_TYPE = 1
APPX_CAPABILITIES = Int32
APPX_CAPABILITY_INTERNET_CLIENT: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_CAPABILITIES = 1
APPX_CAPABILITY_INTERNET_CLIENT_SERVER: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_CAPABILITIES = 2
APPX_CAPABILITY_PRIVATE_NETWORK_CLIENT_SERVER: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_CAPABILITIES = 4
APPX_CAPABILITY_DOCUMENTS_LIBRARY: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_CAPABILITIES = 8
APPX_CAPABILITY_PICTURES_LIBRARY: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_CAPABILITIES = 16
APPX_CAPABILITY_VIDEOS_LIBRARY: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_CAPABILITIES = 32
APPX_CAPABILITY_MUSIC_LIBRARY: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_CAPABILITIES = 64
APPX_CAPABILITY_ENTERPRISE_AUTHENTICATION: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_CAPABILITIES = 128
APPX_CAPABILITY_SHARED_USER_CERTIFICATES: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_CAPABILITIES = 256
APPX_CAPABILITY_REMOVABLE_STORAGE: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_CAPABILITIES = 512
APPX_CAPABILITY_APPOINTMENTS: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_CAPABILITIES = 1024
APPX_CAPABILITY_CONTACTS: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_CAPABILITIES = 2048
APPX_CAPABILITY_CLASS_TYPE = Int32
APPX_CAPABILITY_CLASS_DEFAULT: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_CAPABILITY_CLASS_TYPE = 0
APPX_CAPABILITY_CLASS_GENERAL: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_CAPABILITY_CLASS_TYPE = 1
APPX_CAPABILITY_CLASS_RESTRICTED: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_CAPABILITY_CLASS_TYPE = 2
APPX_CAPABILITY_CLASS_WINDOWS: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_CAPABILITY_CLASS_TYPE = 4
APPX_CAPABILITY_CLASS_ALL: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_CAPABILITY_CLASS_TYPE = 7
APPX_CAPABILITY_CLASS_CUSTOM: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_CAPABILITY_CLASS_TYPE = 8
APPX_COMPRESSION_OPTION = Int32
APPX_COMPRESSION_OPTION_NONE: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_COMPRESSION_OPTION = 0
APPX_COMPRESSION_OPTION_NORMAL: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_COMPRESSION_OPTION = 1
APPX_COMPRESSION_OPTION_MAXIMUM: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_COMPRESSION_OPTION = 2
APPX_COMPRESSION_OPTION_FAST: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_COMPRESSION_OPTION = 3
APPX_COMPRESSION_OPTION_SUPERFAST: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_COMPRESSION_OPTION = 4
class APPX_ENCRYPTED_EXEMPTIONS(Structure):
    count: UInt32
    plainTextFiles: POINTER(win32more.Windows.Win32.Foundation.PWSTR)
APPX_ENCRYPTED_PACKAGE_OPTIONS = Int32
APPX_ENCRYPTED_PACKAGE_OPTION_NONE: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_ENCRYPTED_PACKAGE_OPTIONS = 0
APPX_ENCRYPTED_PACKAGE_OPTION_DIFFUSION: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_ENCRYPTED_PACKAGE_OPTIONS = 1
APPX_ENCRYPTED_PACKAGE_OPTION_PAGE_HASHING: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_ENCRYPTED_PACKAGE_OPTIONS = 2
class APPX_ENCRYPTED_PACKAGE_SETTINGS(Structure):
    keyLength: UInt32
    encryptionAlgorithm: win32more.Windows.Win32.Foundation.PWSTR
    useDiffusion: win32more.Windows.Win32.Foundation.BOOL
    blockMapHashAlgorithm: win32more.Windows.Win32.System.Com.IUri
class APPX_ENCRYPTED_PACKAGE_SETTINGS2(Structure):
    keyLength: UInt32
    encryptionAlgorithm: win32more.Windows.Win32.Foundation.PWSTR
    blockMapHashAlgorithm: win32more.Windows.Win32.System.Com.IUri
    options: UInt32
APPX_FOOTPRINT_FILE_TYPE = Int32
APPX_FOOTPRINT_FILE_TYPE_MANIFEST: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_FOOTPRINT_FILE_TYPE = 0
APPX_FOOTPRINT_FILE_TYPE_BLOCKMAP: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_FOOTPRINT_FILE_TYPE = 1
APPX_FOOTPRINT_FILE_TYPE_SIGNATURE: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_FOOTPRINT_FILE_TYPE = 2
APPX_FOOTPRINT_FILE_TYPE_CODEINTEGRITY: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_FOOTPRINT_FILE_TYPE = 3
APPX_FOOTPRINT_FILE_TYPE_CONTENTGROUPMAP: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_FOOTPRINT_FILE_TYPE = 4
class APPX_KEY_INFO(Structure):
    keyLength: UInt32
    keyIdLength: UInt32
    key: POINTER(Byte)
    keyId: POINTER(Byte)
APPX_PACKAGE_ARCHITECTURE = Int32
APPX_PACKAGE_ARCHITECTURE_X86: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_PACKAGE_ARCHITECTURE = 0
APPX_PACKAGE_ARCHITECTURE_ARM: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_PACKAGE_ARCHITECTURE = 5
APPX_PACKAGE_ARCHITECTURE_X64: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_PACKAGE_ARCHITECTURE = 9
APPX_PACKAGE_ARCHITECTURE_NEUTRAL: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_PACKAGE_ARCHITECTURE = 11
APPX_PACKAGE_ARCHITECTURE_ARM64: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_PACKAGE_ARCHITECTURE = 12
APPX_PACKAGE_ARCHITECTURE2 = Int32
APPX_PACKAGE_ARCHITECTURE2_X86: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_PACKAGE_ARCHITECTURE2 = 0
APPX_PACKAGE_ARCHITECTURE2_ARM: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_PACKAGE_ARCHITECTURE2 = 5
APPX_PACKAGE_ARCHITECTURE2_X64: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_PACKAGE_ARCHITECTURE2 = 9
APPX_PACKAGE_ARCHITECTURE2_NEUTRAL: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_PACKAGE_ARCHITECTURE2 = 11
APPX_PACKAGE_ARCHITECTURE2_ARM64: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_PACKAGE_ARCHITECTURE2 = 12
APPX_PACKAGE_ARCHITECTURE2_X86_ON_ARM64: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_PACKAGE_ARCHITECTURE2 = 14
APPX_PACKAGE_ARCHITECTURE2_UNKNOWN: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_PACKAGE_ARCHITECTURE2 = 65535
APPX_PACKAGE_EDITOR_UPDATE_PACKAGE_MANIFEST_OPTIONS = Int32
APPX_PACKAGE_EDITOR_UPDATE_PACKAGE_MANIFEST_OPTION_NONE: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_PACKAGE_EDITOR_UPDATE_PACKAGE_MANIFEST_OPTIONS = 0
APPX_PACKAGE_EDITOR_UPDATE_PACKAGE_MANIFEST_OPTION_SKIP_VALIDATION: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_PACKAGE_EDITOR_UPDATE_PACKAGE_MANIFEST_OPTIONS = 1
APPX_PACKAGE_EDITOR_UPDATE_PACKAGE_MANIFEST_OPTION_LOCALIZED: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_PACKAGE_EDITOR_UPDATE_PACKAGE_MANIFEST_OPTIONS = 2
APPX_PACKAGE_EDITOR_UPDATE_PACKAGE_OPTION = Int32
APPX_PACKAGE_EDITOR_UPDATE_PACKAGE_OPTION_APPEND_DELTA: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_PACKAGE_EDITOR_UPDATE_PACKAGE_OPTION = 0
class APPX_PACKAGE_SETTINGS(Structure):
    forceZip32: win32more.Windows.Win32.Foundation.BOOL
    hashMethod: win32more.Windows.Win32.System.Com.IUri
class APPX_PACKAGE_WRITER_PAYLOAD_STREAM(Structure):
    inputStream: win32more.Windows.Win32.System.Com.IStream
    fileName: win32more.Windows.Win32.Foundation.PWSTR
    contentType: win32more.Windows.Win32.Foundation.PWSTR
    compressionOption: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_COMPRESSION_OPTION
APPX_PACKAGING_CONTEXT_CHANGE_TYPE = Int32
APPX_PACKAGING_CONTEXT_CHANGE_TYPE_START: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_PACKAGING_CONTEXT_CHANGE_TYPE = 0
APPX_PACKAGING_CONTEXT_CHANGE_TYPE_CHANGE: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_PACKAGING_CONTEXT_CHANGE_TYPE = 1
APPX_PACKAGING_CONTEXT_CHANGE_TYPE_DETAILS: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_PACKAGING_CONTEXT_CHANGE_TYPE = 2
APPX_PACKAGING_CONTEXT_CHANGE_TYPE_END: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_PACKAGING_CONTEXT_CHANGE_TYPE = 3
AddPackageDependencyOptions = Int32
AddPackageDependencyOptions_None: win32more.Windows.Win32.Storage.Packaging.Appx.AddPackageDependencyOptions = 0
AddPackageDependencyOptions_PrependIfRankCollision: win32more.Windows.Win32.Storage.Packaging.Appx.AddPackageDependencyOptions = 1
PACKAGE_FULL_NAME_MIN_LENGTH: UInt32 = 30
PACKAGE_FULL_NAME_MAX_LENGTH: UInt32 = 127
PACKAGE_FAMILY_NAME_MIN_LENGTH: UInt32 = 17
PACKAGE_FAMILY_NAME_MAX_LENGTH: UInt32 = 64
PACKAGE_GRAPH_MAX_SIZE: UInt32 = 641
APPLICATION_USER_MODEL_ID_MIN_LENGTH: UInt32 = 20
APPLICATION_USER_MODEL_ID_MAX_LENGTH: UInt32 = 130
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
PACKAGE_ARCHITECTURE_MIN_LENGTH: UInt32 = 3
PACKAGE_ARCHITECTURE_MAX_LENGTH: UInt32 = 7
PACKAGE_VERSION_MIN_LENGTH: UInt32 = 7
PACKAGE_VERSION_MAX_LENGTH: UInt32 = 23
PACKAGE_NAME_MIN_LENGTH: UInt32 = 3
PACKAGE_NAME_MAX_LENGTH: UInt32 = 50
PACKAGE_PUBLISHER_MIN_LENGTH: UInt32 = 3
PACKAGE_PUBLISHER_MAX_LENGTH: UInt32 = 8192
PACKAGE_PUBLISHERID_MIN_LENGTH: UInt32 = 13
PACKAGE_PUBLISHERID_MAX_LENGTH: UInt32 = 13
PACKAGE_RESOURCEID_MIN_LENGTH: UInt32 = 0
PACKAGE_RESOURCEID_MAX_LENGTH: UInt32 = 30
PACKAGE_MIN_DEPENDENCIES: UInt32 = 0
PACKAGE_MAX_DEPENDENCIES: UInt32 = 128
PACKAGE_FAMILY_MIN_RESOURCE_PACKAGES: UInt32 = 0
PACKAGE_FAMILY_MAX_RESOURCE_PACKAGES: UInt32 = 512
PACKAGE_GRAPH_MIN_SIZE: UInt32 = 1
PACKAGE_APPLICATIONS_MIN_COUNT: UInt32 = 0
PACKAGE_APPLICATIONS_MAX_COUNT: UInt32 = 100
PACKAGE_RELATIVE_APPLICATION_ID_MIN_LENGTH: UInt32 = 2
PACKAGE_RELATIVE_APPLICATION_ID_MAX_LENGTH: UInt32 = 65
@winfunctype('KERNEL32.dll')
def GetCurrentPackageId(bufferLength: POINTER(UInt32), buffer: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def GetCurrentPackageFullName(packageFullNameLength: POINTER(UInt32), packageFullName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def GetCurrentPackageFamilyName(packageFamilyNameLength: POINTER(UInt32), packageFamilyName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def GetCurrentPackagePath(pathLength: POINTER(UInt32), path: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def GetPackageId(hProcess: win32more.Windows.Win32.Foundation.HANDLE, bufferLength: POINTER(UInt32), buffer: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def GetPackageFullName(hProcess: win32more.Windows.Win32.Foundation.HANDLE, packageFullNameLength: POINTER(UInt32), packageFullName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('api-ms-win-appmodel-runtime-l1-1-1.dll')
def GetPackageFullNameFromToken(token: win32more.Windows.Win32.Foundation.HANDLE, packageFullNameLength: POINTER(UInt32), packageFullName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def GetPackageFamilyName(hProcess: win32more.Windows.Win32.Foundation.HANDLE, packageFamilyNameLength: POINTER(UInt32), packageFamilyName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('api-ms-win-appmodel-runtime-l1-1-1.dll')
def GetPackageFamilyNameFromToken(token: win32more.Windows.Win32.Foundation.HANDLE, packageFamilyNameLength: POINTER(UInt32), packageFamilyName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def GetPackagePath(packageId: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.PACKAGE_ID), reserved: UInt32, pathLength: POINTER(UInt32), path: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def GetPackagePathByFullName(packageFullName: win32more.Windows.Win32.Foundation.PWSTR, pathLength: POINTER(UInt32), path: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def GetStagedPackagePathByFullName(packageFullName: win32more.Windows.Win32.Foundation.PWSTR, pathLength: POINTER(UInt32), path: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('api-ms-win-appmodel-runtime-l1-1-3.dll')
def GetPackagePathByFullName2(packageFullName: win32more.Windows.Win32.Foundation.PWSTR, packagePathType: win32more.Windows.Win32.Storage.Packaging.Appx.PackagePathType, pathLength: POINTER(UInt32), path: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('api-ms-win-appmodel-runtime-l1-1-3.dll')
def GetStagedPackagePathByFullName2(packageFullName: win32more.Windows.Win32.Foundation.PWSTR, packagePathType: win32more.Windows.Win32.Storage.Packaging.Appx.PackagePathType, pathLength: POINTER(UInt32), path: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('api-ms-win-appmodel-runtime-l1-1-3.dll')
def GetCurrentPackageInfo2(flags: UInt32, packagePathType: win32more.Windows.Win32.Storage.Packaging.Appx.PackagePathType, bufferLength: POINTER(UInt32), buffer: POINTER(Byte), count: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('api-ms-win-appmodel-runtime-l1-1-3.dll')
def GetCurrentPackagePath2(packagePathType: win32more.Windows.Win32.Storage.Packaging.Appx.PackagePathType, pathLength: POINTER(UInt32), path: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def GetCurrentApplicationUserModelId(applicationUserModelIdLength: POINTER(UInt32), applicationUserModelId: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def GetApplicationUserModelId(hProcess: win32more.Windows.Win32.Foundation.HANDLE, applicationUserModelIdLength: POINTER(UInt32), applicationUserModelId: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('api-ms-win-appmodel-runtime-l1-1-1.dll')
def GetApplicationUserModelIdFromToken(token: win32more.Windows.Win32.Foundation.HANDLE, applicationUserModelIdLength: POINTER(UInt32), applicationUserModelId: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('api-ms-win-appmodel-runtime-l1-1-1.dll')
def VerifyPackageFullName(packageFullName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('api-ms-win-appmodel-runtime-l1-1-1.dll')
def VerifyPackageFamilyName(packageFamilyName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('api-ms-win-appmodel-runtime-l1-1-1.dll')
def VerifyPackageId(packageId: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.PACKAGE_ID)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('api-ms-win-appmodel-runtime-l1-1-1.dll')
def VerifyApplicationUserModelId(applicationUserModelId: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('api-ms-win-appmodel-runtime-l1-1-1.dll')
def VerifyPackageRelativeApplicationId(packageRelativeApplicationId: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def PackageIdFromFullName(packageFullName: win32more.Windows.Win32.Foundation.PWSTR, flags: UInt32, bufferLength: POINTER(UInt32), buffer: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def PackageFullNameFromId(packageId: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.PACKAGE_ID), packageFullNameLength: POINTER(UInt32), packageFullName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def PackageFamilyNameFromId(packageId: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.PACKAGE_ID), packageFamilyNameLength: POINTER(UInt32), packageFamilyName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def PackageFamilyNameFromFullName(packageFullName: win32more.Windows.Win32.Foundation.PWSTR, packageFamilyNameLength: POINTER(UInt32), packageFamilyName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def PackageNameAndPublisherIdFromFamilyName(packageFamilyName: win32more.Windows.Win32.Foundation.PWSTR, packageNameLength: POINTER(UInt32), packageName: win32more.Windows.Win32.Foundation.PWSTR, packagePublisherIdLength: POINTER(UInt32), packagePublisherId: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def FormatApplicationUserModelId(packageFamilyName: win32more.Windows.Win32.Foundation.PWSTR, packageRelativeApplicationId: win32more.Windows.Win32.Foundation.PWSTR, applicationUserModelIdLength: POINTER(UInt32), applicationUserModelId: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def ParseApplicationUserModelId(applicationUserModelId: win32more.Windows.Win32.Foundation.PWSTR, packageFamilyNameLength: POINTER(UInt32), packageFamilyName: win32more.Windows.Win32.Foundation.PWSTR, packageRelativeApplicationIdLength: POINTER(UInt32), packageRelativeApplicationId: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def GetPackagesByPackageFamily(packageFamilyName: win32more.Windows.Win32.Foundation.PWSTR, count: POINTER(UInt32), packageFullNames: POINTER(win32more.Windows.Win32.Foundation.PWSTR), bufferLength: POINTER(UInt32), buffer: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def FindPackagesByPackageFamily(packageFamilyName: win32more.Windows.Win32.Foundation.PWSTR, packageFilters: UInt32, count: POINTER(UInt32), packageFullNames: POINTER(win32more.Windows.Win32.Foundation.PWSTR), bufferLength: POINTER(UInt32), buffer: win32more.Windows.Win32.Foundation.PWSTR, packageProperties: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('api-ms-win-appmodel-runtime-l1-1-1.dll')
def GetStagedPackageOrigin(packageFullName: win32more.Windows.Win32.Foundation.PWSTR, origin: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.PackageOrigin)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def GetCurrentPackageInfo(flags: UInt32, bufferLength: POINTER(UInt32), buffer: POINTER(Byte), count: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def OpenPackageInfoByFullName(packageFullName: win32more.Windows.Win32.Foundation.PWSTR, reserved: UInt32, packageInfoReference: POINTER(POINTER(win32more.Windows.Win32.Storage.Packaging.Appx._PACKAGE_INFO_REFERENCE))) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('api-ms-win-appmodel-runtime-l1-1-1.dll')
def OpenPackageInfoByFullNameForUser(userSid: win32more.Windows.Win32.Security.PSID, packageFullName: win32more.Windows.Win32.Foundation.PWSTR, reserved: UInt32, packageInfoReference: POINTER(POINTER(win32more.Windows.Win32.Storage.Packaging.Appx._PACKAGE_INFO_REFERENCE))) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def ClosePackageInfo(packageInfoReference: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx._PACKAGE_INFO_REFERENCE)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def GetPackageInfo(packageInfoReference: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx._PACKAGE_INFO_REFERENCE), flags: UInt32, bufferLength: POINTER(UInt32), buffer: POINTER(Byte), count: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def GetPackageApplicationIds(packageInfoReference: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx._PACKAGE_INFO_REFERENCE), bufferLength: POINTER(UInt32), buffer: POINTER(Byte), count: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('api-ms-win-appmodel-runtime-l1-1-3.dll')
def GetPackageInfo2(packageInfoReference: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx._PACKAGE_INFO_REFERENCE), flags: UInt32, packagePathType: win32more.Windows.Win32.Storage.Packaging.Appx.PackagePathType, bufferLength: POINTER(UInt32), buffer: POINTER(Byte), count: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def CheckIsMSIXPackage(packageFullName: win32more.Windows.Win32.Foundation.PWSTR, isMSIXPackage: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNELBASE.dll')
def TryCreatePackageDependency(user: win32more.Windows.Win32.Security.PSID, packageFamilyName: win32more.Windows.Win32.Foundation.PWSTR, minVersion: win32more.Windows.Win32.Storage.Packaging.Appx.PACKAGE_VERSION, packageDependencyProcessorArchitectures: win32more.Windows.Win32.Storage.Packaging.Appx.PackageDependencyProcessorArchitectures, lifetimeKind: win32more.Windows.Win32.Storage.Packaging.Appx.PackageDependencyLifetimeKind, lifetimeArtifact: win32more.Windows.Win32.Foundation.PWSTR, options: win32more.Windows.Win32.Storage.Packaging.Appx.CreatePackageDependencyOptions, packageDependencyId: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNELBASE.dll')
def DeletePackageDependency(packageDependencyId: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNELBASE.dll')
def AddPackageDependency(packageDependencyId: win32more.Windows.Win32.Foundation.PWSTR, rank: Int32, options: win32more.Windows.Win32.Storage.Packaging.Appx.AddPackageDependencyOptions, packageDependencyContext: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.PACKAGEDEPENDENCY_CONTEXT), packageFullName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNELBASE.dll')
def RemovePackageDependency(packageDependencyContext: win32more.Windows.Win32.Storage.Packaging.Appx.PACKAGEDEPENDENCY_CONTEXT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNELBASE.dll')
def GetResolvedPackageFullNameForPackageDependency(packageDependencyId: win32more.Windows.Win32.Foundation.PWSTR, packageFullName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNELBASE.dll')
def GetIdForPackageDependencyContext(packageDependencyContext: win32more.Windows.Win32.Storage.Packaging.Appx.PACKAGEDEPENDENCY_CONTEXT, packageDependencyId: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-appmodel-runtime-l1-1-6.dll')
def GetPackageGraphRevisionId() -> UInt32: ...
@winfunctype('KERNEL32.dll')
def AppPolicyGetLifecycleManagement(processToken: win32more.Windows.Win32.Foundation.HANDLE, policy: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.AppPolicyLifecycleManagement)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def AppPolicyGetWindowingModel(processToken: win32more.Windows.Win32.Foundation.HANDLE, policy: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.AppPolicyWindowingModel)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def AppPolicyGetMediaFoundationCodecLoading(processToken: win32more.Windows.Win32.Foundation.HANDLE, policy: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.AppPolicyMediaFoundationCodecLoading)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def AppPolicyGetClrCompat(processToken: win32more.Windows.Win32.Foundation.HANDLE, policy: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.AppPolicyClrCompat)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def AppPolicyGetThreadInitializationType(processToken: win32more.Windows.Win32.Foundation.HANDLE, policy: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.AppPolicyThreadInitializationType)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def AppPolicyGetShowDeveloperDiagnostic(processToken: win32more.Windows.Win32.Foundation.HANDLE, policy: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.AppPolicyShowDeveloperDiagnostic)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def AppPolicyGetProcessTerminationMethod(processToken: win32more.Windows.Win32.Foundation.HANDLE, policy: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.AppPolicyProcessTerminationMethod)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def AppPolicyGetCreateFileAccess(processToken: win32more.Windows.Win32.Foundation.HANDLE, policy: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.AppPolicyCreateFileAccess)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('KERNEL32.dll')
def CreatePackageVirtualizationContext(packageFamilyName: win32more.Windows.Win32.Foundation.PWSTR, context: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.PACKAGE_VIRTUALIZATION_CONTEXT_HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def ActivatePackageVirtualizationContext(context: win32more.Windows.Win32.Storage.Packaging.Appx.PACKAGE_VIRTUALIZATION_CONTEXT_HANDLE, cookie: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def ReleasePackageVirtualizationContext(context: win32more.Windows.Win32.Storage.Packaging.Appx.PACKAGE_VIRTUALIZATION_CONTEXT_HANDLE) -> Void: ...
@winfunctype('KERNEL32.dll')
def DeactivatePackageVirtualizationContext(cookie: UIntPtr) -> Void: ...
@winfunctype('KERNEL32.dll')
def DuplicatePackageVirtualizationContext(sourceContext: win32more.Windows.Win32.Storage.Packaging.Appx.PACKAGE_VIRTUALIZATION_CONTEXT_HANDLE, destContext: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.PACKAGE_VIRTUALIZATION_CONTEXT_HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def GetCurrentPackageVirtualizationContext() -> win32more.Windows.Win32.Storage.Packaging.Appx.PACKAGE_VIRTUALIZATION_CONTEXT_HANDLE: ...
@winfunctype('KERNEL32.dll')
def GetProcessesInVirtualizationContext(packageFamilyName: win32more.Windows.Win32.Foundation.PWSTR, count: POINTER(UInt32), processes: POINTER(POINTER(win32more.Windows.Win32.Foundation.HANDLE))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def GetCurrentPackageInfo3(flags: UInt32, packageInfoType: win32more.Windows.Win32.Storage.Packaging.Appx.PackageInfo3Type, bufferLength: POINTER(UInt32), buffer: VoidPtr, count: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
AppPolicyClrCompat = Int32
AppPolicyClrCompat_Other: win32more.Windows.Win32.Storage.Packaging.Appx.AppPolicyClrCompat = 0
AppPolicyClrCompat_ClassicDesktop: win32more.Windows.Win32.Storage.Packaging.Appx.AppPolicyClrCompat = 1
AppPolicyClrCompat_Universal: win32more.Windows.Win32.Storage.Packaging.Appx.AppPolicyClrCompat = 2
AppPolicyClrCompat_PackagedDesktop: win32more.Windows.Win32.Storage.Packaging.Appx.AppPolicyClrCompat = 3
AppPolicyCreateFileAccess = Int32
AppPolicyCreateFileAccess_Full: win32more.Windows.Win32.Storage.Packaging.Appx.AppPolicyCreateFileAccess = 0
AppPolicyCreateFileAccess_Limited: win32more.Windows.Win32.Storage.Packaging.Appx.AppPolicyCreateFileAccess = 1
AppPolicyLifecycleManagement = Int32
AppPolicyLifecycleManagement_Unmanaged: win32more.Windows.Win32.Storage.Packaging.Appx.AppPolicyLifecycleManagement = 0
AppPolicyLifecycleManagement_Managed: win32more.Windows.Win32.Storage.Packaging.Appx.AppPolicyLifecycleManagement = 1
AppPolicyMediaFoundationCodecLoading = Int32
AppPolicyMediaFoundationCodecLoading_All: win32more.Windows.Win32.Storage.Packaging.Appx.AppPolicyMediaFoundationCodecLoading = 0
AppPolicyMediaFoundationCodecLoading_InboxOnly: win32more.Windows.Win32.Storage.Packaging.Appx.AppPolicyMediaFoundationCodecLoading = 1
AppPolicyProcessTerminationMethod = Int32
AppPolicyProcessTerminationMethod_ExitProcess: win32more.Windows.Win32.Storage.Packaging.Appx.AppPolicyProcessTerminationMethod = 0
AppPolicyProcessTerminationMethod_TerminateProcess: win32more.Windows.Win32.Storage.Packaging.Appx.AppPolicyProcessTerminationMethod = 1
AppPolicyShowDeveloperDiagnostic = Int32
AppPolicyShowDeveloperDiagnostic_None: win32more.Windows.Win32.Storage.Packaging.Appx.AppPolicyShowDeveloperDiagnostic = 0
AppPolicyShowDeveloperDiagnostic_ShowUI: win32more.Windows.Win32.Storage.Packaging.Appx.AppPolicyShowDeveloperDiagnostic = 1
AppPolicyThreadInitializationType = Int32
AppPolicyThreadInitializationType_None: win32more.Windows.Win32.Storage.Packaging.Appx.AppPolicyThreadInitializationType = 0
AppPolicyThreadInitializationType_InitializeWinRT: win32more.Windows.Win32.Storage.Packaging.Appx.AppPolicyThreadInitializationType = 1
AppPolicyWindowingModel = Int32
AppPolicyWindowingModel_None: win32more.Windows.Win32.Storage.Packaging.Appx.AppPolicyWindowingModel = 0
AppPolicyWindowingModel_Universal: win32more.Windows.Win32.Storage.Packaging.Appx.AppPolicyWindowingModel = 1
AppPolicyWindowingModel_ClassicDesktop: win32more.Windows.Win32.Storage.Packaging.Appx.AppPolicyWindowingModel = 2
AppPolicyWindowingModel_ClassicPhone: win32more.Windows.Win32.Storage.Packaging.Appx.AppPolicyWindowingModel = 3
AppxBundleFactory = Guid('{378e0446-5384-43b7-8877-e7dbdd883446}')
AppxEncryptionFactory = Guid('{dc664fdd-d868-46ee-8780-8d196cb739f7}')
AppxFactory = Guid('{5842a140-ff9f-4166-8f5c-62f5b7b0c781}')
AppxPackageEditor = Guid('{f004f2ca-aebc-4b0d-bf58-e516d5bcc0ab}')
AppxPackagingDiagnosticEventSinkManager = Guid('{50ca0a46-1588-4161-8ed2-ef9e469ced5d}')
CreatePackageDependencyOptions = Int32
CreatePackageDependencyOptions_None: win32more.Windows.Win32.Storage.Packaging.Appx.CreatePackageDependencyOptions = 0
CreatePackageDependencyOptions_DoNotVerifyDependencyResolution: win32more.Windows.Win32.Storage.Packaging.Appx.CreatePackageDependencyOptions = 1
CreatePackageDependencyOptions_ScopeIsSystem: win32more.Windows.Win32.Storage.Packaging.Appx.CreatePackageDependencyOptions = 2
DX_FEATURE_LEVEL = Int32
DX_FEATURE_LEVEL_UNSPECIFIED: win32more.Windows.Win32.Storage.Packaging.Appx.DX_FEATURE_LEVEL = 0
DX_FEATURE_LEVEL_9: win32more.Windows.Win32.Storage.Packaging.Appx.DX_FEATURE_LEVEL = 1
DX_FEATURE_LEVEL_10: win32more.Windows.Win32.Storage.Packaging.Appx.DX_FEATURE_LEVEL = 2
DX_FEATURE_LEVEL_11: win32more.Windows.Win32.Storage.Packaging.Appx.DX_FEATURE_LEVEL = 3
class IAppxAppInstallerReader(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f35bc38c-1d2f-43db-a1f4-586430d1fed2}')
    @commethod(3)
    def GetXmlDom(self, dom: POINTER(win32more.Windows.Win32.Data.Xml.MsXml.IXMLDOMDocument)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxBlockMapBlock(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{75cf3930-3244-4fe0-a8c8-e0bcb270b889}')
    @commethod(3)
    def GetHash(self, bufferSize: POINTER(UInt32), buffer: POINTER(POINTER(Byte))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCompressedSize(self, size: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxBlockMapBlocksEnumerator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6b429b5b-36ef-479e-b9eb-0c1482b49e16}')
    @commethod(3)
    def GetCurrent(self, block: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxBlockMapBlock)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHasCurrent(self, hasCurrent: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MoveNext(self, hasNext: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxBlockMapFile(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{277672ac-4f63-42c1-8abc-beae3600eb59}')
    @commethod(3)
    def GetBlocks(self, blocks: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxBlockMapBlocksEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLocalFileHeaderSize(self, lfhSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetName(self, name: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetUncompressedSize(self, size: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ValidateFileHash(self, fileStream: win32more.Windows.Win32.System.Com.IStream, isValid: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxBlockMapFilesEnumerator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{02b856a2-4262-4070-bacb-1a8cbbc42305}')
    @commethod(3)
    def GetCurrent(self, file: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxBlockMapFile)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHasCurrent(self, hasCurrent: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MoveNext(self, hasCurrent: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxBlockMapReader(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5efec991-bca3-42d1-9ec2-e92d609ec22a}')
    @commethod(3)
    def GetFile(self, filename: win32more.Windows.Win32.Foundation.PWSTR, file: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxBlockMapFile)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFiles(self, enumerator: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxBlockMapFilesEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetHashMethod(self, hashMethod: POINTER(win32more.Windows.Win32.System.Com.IUri)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetStream(self, blockMapStream: POINTER(win32more.Windows.Win32.System.Com.IStream)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxBundleFactory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bba65864-965f-4a5f-855f-f074bdbf3a7b}')
    @commethod(3)
    def CreateBundleWriter(self, outputStream: win32more.Windows.Win32.System.Com.IStream, bundleVersion: UInt64, bundleWriter: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxBundleWriter)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateBundleReader(self, inputStream: win32more.Windows.Win32.System.Com.IStream, bundleReader: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxBundleReader)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateBundleManifestReader(self, inputStream: win32more.Windows.Win32.System.Com.IStream, manifestReader: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxBundleManifestReader)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxBundleFactory2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7325b83d-0185-42c4-82ac-be34ab1a2a8a}')
    @commethod(3)
    def CreateBundleReader2(self, inputStream: win32more.Windows.Win32.System.Com.IStream, expectedDigest: win32more.Windows.Win32.Foundation.PWSTR, bundleReader: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxBundleReader)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxBundleManifestOptionalBundleInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{515bf2e8-bcb0-4d69-8c48-e383147b6e12}')
    @commethod(3)
    def GetPackageId(self, packageId: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxManifestPackageId)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFileName(self, fileName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPackageInfoItems(self, packageInfoItems: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxBundleManifestPackageInfoEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxBundleManifestOptionalBundleInfoEnumerator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9a178793-f97e-46ac-aaca-dd5ba4c177c8}')
    @commethod(3)
    def GetCurrent(self, optionalBundle: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxBundleManifestOptionalBundleInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHasCurrent(self, hasCurrent: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MoveNext(self, hasNext: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxBundleManifestPackageInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{54cd06c1-268f-40bb-8ed2-757a9ebaec8d}')
    @commethod(3)
    def GetPackageType(self, packageType: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.APPX_BUNDLE_PAYLOAD_PACKAGE_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPackageId(self, packageId: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxManifestPackageId)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetFileName(self, fileName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetOffset(self, offset: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetSize(self, size: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetResources(self, resources: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxManifestQualifiedResourcesEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxBundleManifestPackageInfo2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{44c2acbc-b2cf-4ccb-bbdb-9c6da8c3bc9e}')
    @commethod(3)
    def GetIsPackageReference(self, isPackageReference: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetIsNonQualifiedResourcePackage(self, isNonQualifiedResourcePackage: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetIsDefaultApplicablePackage(self, isDefaultApplicablePackage: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxBundleManifestPackageInfo3(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6ba74b98-bb74-4296-80d0-5f4256a99675}')
    @commethod(3)
    def GetTargetDeviceFamilies(self, targetDeviceFamilies: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxManifestTargetDeviceFamiliesEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxBundleManifestPackageInfo4(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5da6f13d-a8a7-4532-857c-1393d659371d}')
    @commethod(3)
    def GetIsStub(self, isStub: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxBundleManifestPackageInfoEnumerator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f9b856ee-49a6-4e19-b2b0-6a2406d63a32}')
    @commethod(3)
    def GetCurrent(self, packageInfo: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxBundleManifestPackageInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHasCurrent(self, hasCurrent: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MoveNext(self, hasNext: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxBundleManifestReader(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{cf0ebbc1-cc99-4106-91eb-e67462e04fb0}')
    @commethod(3)
    def GetPackageId(self, packageId: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxManifestPackageId)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPackageInfoItems(self, packageInfoItems: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxBundleManifestPackageInfoEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetStream(self, manifestStream: POINTER(win32more.Windows.Win32.System.Com.IStream)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxBundleManifestReader2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5517df70-033f-4af2-8213-87d766805c02}')
    @commethod(3)
    def GetOptionalBundles(self, optionalBundles: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxBundleManifestOptionalBundleInfoEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxBundleReader(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dd75b8c0-ba76-43b0-ae0f-68656a1dc5c8}')
    @commethod(3)
    def GetFootprintFile(self, fileType: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_BUNDLE_FOOTPRINT_FILE_TYPE, footprintFile: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxFile)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetBlockMap(self, blockMapReader: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxBlockMapReader)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetManifest(self, manifestReader: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxBundleManifestReader)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPayloadPackages(self, payloadPackages: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxFilesEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetPayloadPackage(self, fileName: win32more.Windows.Win32.Foundation.PWSTR, payloadPackage: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxFile)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxBundleWriter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ec446fe8-bfec-4c64-ab4f-49f038f0c6d2}')
    @commethod(3)
    def AddPayloadPackage(self, fileName: win32more.Windows.Win32.Foundation.PWSTR, packageStream: win32more.Windows.Win32.System.Com.IStream) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Close(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxBundleWriter2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6d8fe971-01cc-49a0-b685-233851279962}')
    @commethod(3)
    def AddExternalPackageReference(self, fileName: win32more.Windows.Win32.Foundation.PWSTR, inputStream: win32more.Windows.Win32.System.Com.IStream) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxBundleWriter3(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ad711152-f969-4193-82d5-9ddf2786d21a}')
    @commethod(3)
    def AddPackageReference(self, fileName: win32more.Windows.Win32.Foundation.PWSTR, inputStream: win32more.Windows.Win32.System.Com.IStream) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Close(self, hashMethodString: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxBundleWriter4(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9cd9d523-5009-4c01-9882-dc029fbd47a3}')
    @commethod(3)
    def AddPayloadPackage(self, fileName: win32more.Windows.Win32.Foundation.PWSTR, packageStream: win32more.Windows.Win32.System.Com.IStream, isDefaultApplicablePackage: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddPackageReference(self, fileName: win32more.Windows.Win32.Foundation.PWSTR, inputStream: win32more.Windows.Win32.System.Com.IStream, isDefaultApplicablePackage: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddExternalPackageReference(self, fileName: win32more.Windows.Win32.Foundation.PWSTR, inputStream: win32more.Windows.Win32.System.Com.IStream, isDefaultApplicablePackage: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxContentGroup(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{328f6468-c04f-4e3c-b6fa-6b8d27f3003a}')
    @commethod(3)
    def GetName(self, groupName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFiles(self, enumerator: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxContentGroupFilesEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxContentGroupFilesEnumerator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1a09a2fd-7440-44eb-8c84-848205a6a1cc}')
    @commethod(3)
    def GetCurrent(self, file: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHasCurrent(self, hasCurrent: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MoveNext(self, hasNext: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxContentGroupMapReader(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{418726d8-dd99-4f5d-9886-157add20de01}')
    @commethod(3)
    def GetRequiredGroup(self, requiredGroup: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxContentGroup)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAutomaticGroups(self, automaticGroupsEnumerator: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxContentGroupsEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxContentGroupMapWriter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d07ab776-a9de-4798-8c14-3db31e687c78}')
    @commethod(3)
    def AddAutomaticGroup(self, groupName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddAutomaticFile(self, fileName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Close(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxContentGroupsEnumerator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3264e477-16d1-4d63-823e-7d2984696634}')
    @commethod(3)
    def GetCurrent(self, stream: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxContentGroup)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHasCurrent(self, hasCurrent: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MoveNext(self, hasNext: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxDigestProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9fe2702b-7640-4659-8e6c-349e43c4cdbd}')
    @commethod(3)
    def GetDigest(self, digest: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxEncryptedBundleWriter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{80b0902f-7bf0-4117-b8c6-4279ef81ee77}')
    @commethod(3)
    def AddPayloadPackageEncrypted(self, fileName: win32more.Windows.Win32.Foundation.PWSTR, packageStream: win32more.Windows.Win32.System.Com.IStream) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Close(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxEncryptedBundleWriter2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e644be82-f0fa-42b8-a956-8d1cb48ee379}')
    @commethod(3)
    def AddExternalPackageReference(self, fileName: win32more.Windows.Win32.Foundation.PWSTR, inputStream: win32more.Windows.Win32.System.Com.IStream) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxEncryptedBundleWriter3(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0d34deb3-5cae-4dd3-977c-504932a51d31}')
    @commethod(3)
    def AddPayloadPackageEncrypted(self, fileName: win32more.Windows.Win32.Foundation.PWSTR, packageStream: win32more.Windows.Win32.System.Com.IStream, isDefaultApplicablePackage: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddExternalPackageReference(self, fileName: win32more.Windows.Win32.Foundation.PWSTR, inputStream: win32more.Windows.Win32.System.Com.IStream, isDefaultApplicablePackage: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxEncryptedPackageWriter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f43d0b0b-1379-40e2-9b29-682ea2bf42af}')
    @commethod(3)
    def AddPayloadFileEncrypted(self, fileName: win32more.Windows.Win32.Foundation.PWSTR, compressionOption: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_COMPRESSION_OPTION, inputStream: win32more.Windows.Win32.System.Com.IStream) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Close(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxEncryptedPackageWriter2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3e475447-3a25-40b5-8ad2-f953ae50c92d}')
    @commethod(3)
    def AddPayloadFilesEncrypted(self, fileCount: UInt32, payloadFiles: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.APPX_PACKAGE_WRITER_PAYLOAD_STREAM), memoryLimit: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxEncryptionFactory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{80e8e04d-8c88-44ae-a011-7cadf6fb2e72}')
    @commethod(3)
    def EncryptPackage(self, inputStream: win32more.Windows.Win32.System.Com.IStream, outputStream: win32more.Windows.Win32.System.Com.IStream, settings: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.APPX_ENCRYPTED_PACKAGE_SETTINGS), keyInfo: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.APPX_KEY_INFO), exemptedFiles: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.APPX_ENCRYPTED_EXEMPTIONS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DecryptPackage(self, inputStream: win32more.Windows.Win32.System.Com.IStream, outputStream: win32more.Windows.Win32.System.Com.IStream, keyInfo: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.APPX_KEY_INFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateEncryptedPackageWriter(self, outputStream: win32more.Windows.Win32.System.Com.IStream, manifestStream: win32more.Windows.Win32.System.Com.IStream, settings: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.APPX_ENCRYPTED_PACKAGE_SETTINGS), keyInfo: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.APPX_KEY_INFO), exemptedFiles: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.APPX_ENCRYPTED_EXEMPTIONS), packageWriter: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxEncryptedPackageWriter)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateEncryptedPackageReader(self, inputStream: win32more.Windows.Win32.System.Com.IStream, keyInfo: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.APPX_KEY_INFO), packageReader: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxPackageReader)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def EncryptBundle(self, inputStream: win32more.Windows.Win32.System.Com.IStream, outputStream: win32more.Windows.Win32.System.Com.IStream, settings: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.APPX_ENCRYPTED_PACKAGE_SETTINGS), keyInfo: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.APPX_KEY_INFO), exemptedFiles: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.APPX_ENCRYPTED_EXEMPTIONS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def DecryptBundle(self, inputStream: win32more.Windows.Win32.System.Com.IStream, outputStream: win32more.Windows.Win32.System.Com.IStream, keyInfo: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.APPX_KEY_INFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def CreateEncryptedBundleWriter(self, outputStream: win32more.Windows.Win32.System.Com.IStream, bundleVersion: UInt64, settings: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.APPX_ENCRYPTED_PACKAGE_SETTINGS), keyInfo: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.APPX_KEY_INFO), exemptedFiles: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.APPX_ENCRYPTED_EXEMPTIONS), bundleWriter: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxEncryptedBundleWriter)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def CreateEncryptedBundleReader(self, inputStream: win32more.Windows.Win32.System.Com.IStream, keyInfo: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.APPX_KEY_INFO), bundleReader: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxBundleReader)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxEncryptionFactory2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c1b11eee-c4ba-4ab2-a55d-d015fe8ff64f}')
    @commethod(3)
    def CreateEncryptedPackageWriter(self, outputStream: win32more.Windows.Win32.System.Com.IStream, manifestStream: win32more.Windows.Win32.System.Com.IStream, contentGroupMapStream: win32more.Windows.Win32.System.Com.IStream, settings: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.APPX_ENCRYPTED_PACKAGE_SETTINGS), keyInfo: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.APPX_KEY_INFO), exemptedFiles: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.APPX_ENCRYPTED_EXEMPTIONS), packageWriter: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxEncryptedPackageWriter)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxEncryptionFactory3(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{09edca37-cd64-47d6-b7e8-1cb11d4f7e05}')
    @commethod(3)
    def EncryptPackage(self, inputStream: win32more.Windows.Win32.System.Com.IStream, outputStream: win32more.Windows.Win32.System.Com.IStream, settings: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.APPX_ENCRYPTED_PACKAGE_SETTINGS2), keyInfo: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.APPX_KEY_INFO), exemptedFiles: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.APPX_ENCRYPTED_EXEMPTIONS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateEncryptedPackageWriter(self, outputStream: win32more.Windows.Win32.System.Com.IStream, manifestStream: win32more.Windows.Win32.System.Com.IStream, contentGroupMapStream: win32more.Windows.Win32.System.Com.IStream, settings: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.APPX_ENCRYPTED_PACKAGE_SETTINGS2), keyInfo: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.APPX_KEY_INFO), exemptedFiles: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.APPX_ENCRYPTED_EXEMPTIONS), packageWriter: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxEncryptedPackageWriter)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EncryptBundle(self, inputStream: win32more.Windows.Win32.System.Com.IStream, outputStream: win32more.Windows.Win32.System.Com.IStream, settings: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.APPX_ENCRYPTED_PACKAGE_SETTINGS2), keyInfo: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.APPX_KEY_INFO), exemptedFiles: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.APPX_ENCRYPTED_EXEMPTIONS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateEncryptedBundleWriter(self, outputStream: win32more.Windows.Win32.System.Com.IStream, bundleVersion: UInt64, settings: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.APPX_ENCRYPTED_PACKAGE_SETTINGS2), keyInfo: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.APPX_KEY_INFO), exemptedFiles: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.APPX_ENCRYPTED_EXEMPTIONS), bundleWriter: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxEncryptedBundleWriter)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxEncryptionFactory4(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a879611f-12fd-41fe-85d5-06ae779bbaf5}')
    @commethod(3)
    def EncryptPackage(self, inputStream: win32more.Windows.Win32.System.Com.IStream, outputStream: win32more.Windows.Win32.System.Com.IStream, settings: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.APPX_ENCRYPTED_PACKAGE_SETTINGS2), keyInfo: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.APPX_KEY_INFO), exemptedFiles: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.APPX_ENCRYPTED_EXEMPTIONS), memoryLimit: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxEncryptionFactory5(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{68d6e77a-f446-480f-b0f0-d91a24c60746}')
    @commethod(3)
    def CreateEncryptedPackageReader2(self, inputStream: win32more.Windows.Win32.System.Com.IStream, keyInfo: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.APPX_KEY_INFO), expectedDigest: win32more.Windows.Win32.Foundation.PWSTR, packageReader: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxPackageReader)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateEncryptedBundleReader2(self, inputStream: win32more.Windows.Win32.System.Com.IStream, keyInfo: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.APPX_KEY_INFO), expectedDigest: win32more.Windows.Win32.Foundation.PWSTR, bundleReader: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxBundleReader)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxFactory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{beb94909-e451-438b-b5a7-d79e767b75d8}')
    @commethod(3)
    def CreatePackageWriter(self, outputStream: win32more.Windows.Win32.System.Com.IStream, settings: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.APPX_PACKAGE_SETTINGS), packageWriter: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxPackageWriter)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreatePackageReader(self, inputStream: win32more.Windows.Win32.System.Com.IStream, packageReader: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxPackageReader)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateManifestReader(self, inputStream: win32more.Windows.Win32.System.Com.IStream, manifestReader: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxManifestReader)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateBlockMapReader(self, inputStream: win32more.Windows.Win32.System.Com.IStream, blockMapReader: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxBlockMapReader)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateValidatedBlockMapReader(self, blockMapStream: win32more.Windows.Win32.System.Com.IStream, signatureFileName: win32more.Windows.Win32.Foundation.PWSTR, blockMapReader: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxBlockMapReader)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxFactory2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f1346df2-c282-4e22-b918-743a929a8d55}')
    @commethod(3)
    def CreateContentGroupMapReader(self, inputStream: win32more.Windows.Win32.System.Com.IStream, contentGroupMapReader: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxContentGroupMapReader)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateSourceContentGroupMapReader(self, inputStream: win32more.Windows.Win32.System.Com.IStream, reader: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxSourceContentGroupMapReader)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateContentGroupMapWriter(self, stream: win32more.Windows.Win32.System.Com.IStream, contentGroupMapWriter: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxContentGroupMapWriter)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxFactory3(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{776b2c05-e21d-4e24-ba1a-cd529a8bfdbb}')
    @commethod(3)
    def CreatePackageReader2(self, inputStream: win32more.Windows.Win32.System.Com.IStream, expectedDigest: win32more.Windows.Win32.Foundation.PWSTR, packageReader: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxPackageReader)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateManifestReader2(self, inputStream: win32more.Windows.Win32.System.Com.IStream, expectedDigest: win32more.Windows.Win32.Foundation.PWSTR, manifestReader: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxManifestReader)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateAppInstallerReader(self, inputStream: win32more.Windows.Win32.System.Com.IStream, expectedDigest: win32more.Windows.Win32.Foundation.PWSTR, appInstallerReader: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxAppInstallerReader)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxFile(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{91df827b-94fd-468f-827b-57f41b2f6f2e}')
    @commethod(3)
    def GetCompressionOption(self, compressionOption: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.APPX_COMPRESSION_OPTION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetContentType(self, contentType: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetName(self, fileName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSize(self, size: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetStream(self, stream: POINTER(win32more.Windows.Win32.System.Com.IStream)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxFilesEnumerator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f007eeaf-9831-411c-9847-917cdc62d1fe}')
    @commethod(3)
    def GetCurrent(self, file: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxFile)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHasCurrent(self, hasCurrent: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MoveNext(self, hasNext: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestApplication(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5da89bf4-3773-46be-b650-7e744863b7e8}')
    @commethod(3)
    def GetStringValue(self, name: win32more.Windows.Win32.Foundation.PWSTR, value: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAppUserModelId(self, appUserModelId: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestApplicationsEnumerator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9eb8a55a-f04b-4d0d-808d-686185d4847a}')
    @commethod(3)
    def GetCurrent(self, application: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxManifestApplication)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHasCurrent(self, hasCurrent: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MoveNext(self, hasNext: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestCapabilitiesEnumerator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{11d22258-f470-42c1-b291-8361c5437e41}')
    @commethod(3)
    def GetCurrent(self, capability: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHasCurrent(self, hasCurrent: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MoveNext(self, hasNext: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestDeviceCapabilitiesEnumerator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{30204541-427b-4a1c-bacf-655bf463a540}')
    @commethod(3)
    def GetCurrent(self, deviceCapability: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHasCurrent(self, hasCurrent: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MoveNext(self, hasNext: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestDriverConstraint(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c031bee4-bbcc-48ea-a237-c34045c80a07}')
    @commethod(3)
    def GetName(self, name: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMinVersion(self, minVersion: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetMinDate(self, minDate: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestDriverConstraintsEnumerator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d402b2d1-f600-49e0-95e6-975d8da13d89}')
    @commethod(3)
    def GetCurrent(self, driverConstraint: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxManifestDriverConstraint)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHasCurrent(self, hasCurrent: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MoveNext(self, hasNext: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestDriverDependenciesEnumerator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fe039db2-467f-4755-8404-8f5eb6865b33}')
    @commethod(3)
    def GetCurrent(self, driverDependency: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxManifestDriverDependency)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHasCurrent(self, hasCurrent: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MoveNext(self, hasNext: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestDriverDependency(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1210cb94-5a92-4602-be24-79f318af4af9}')
    @commethod(3)
    def GetDriverConstraints(self, driverConstraints: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxManifestDriverConstraintsEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestHostRuntimeDependenciesEnumerator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6427a646-7f49-433e-b1a6-0da309f6885a}')
    @commethod(3)
    def GetCurrent(self, hostRuntimeDependency: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxManifestHostRuntimeDependency)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHasCurrent(self, hasCurrent: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MoveNext(self, hasNext: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestHostRuntimeDependency(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3455d234-8414-410d-95c7-7b35255b8391}')
    @commethod(3)
    def GetName(self, name: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPublisher(self, publisher: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetMinVersion(self, minVersion: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestHostRuntimeDependency2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c26f23a8-ee10-4ad6-b898-2b4d7aebfe6a}')
    @commethod(3)
    def GetPackageFamilyName(self, packageFamilyName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestMainPackageDependenciesEnumerator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a99c4f00-51d2-4f0f-ba46-7ed5255ebdff}')
    @commethod(3)
    def GetCurrent(self, mainPackageDependency: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxManifestMainPackageDependency)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHasCurrent(self, hasCurrent: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MoveNext(self, hasNext: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestMainPackageDependency(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{05d0611c-bc29-46d5-97e2-84b9c79bd8ae}')
    @commethod(3)
    def GetName(self, name: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPublisher(self, publisher: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPackageFamilyName(self, packageFamilyName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestOSPackageDependenciesEnumerator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b84e2fc3-f8ec-4bc1-8ae2-156346f5ffea}')
    @commethod(3)
    def GetCurrent(self, osPackageDependency: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxManifestOSPackageDependency)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHasCurrent(self, hasCurrent: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MoveNext(self, hasNext: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestOSPackageDependency(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{154995ee-54a6-4f14-ac97-d8cf0519644b}')
    @commethod(3)
    def GetName(self, name: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetVersion(self, version: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestOptionalPackageInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2634847d-5b5d-4fe5-a243-002ff95edc7e}')
    @commethod(3)
    def GetIsOptionalPackage(self, isOptionalPackage: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMainPackageName(self, mainPackageName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestPackageDependenciesEnumerator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b43bbcf9-65a6-42dd-bac0-8c6741e7f5a4}')
    @commethod(3)
    def GetCurrent(self, dependency: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxManifestPackageDependency)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHasCurrent(self, hasCurrent: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MoveNext(self, hasNext: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestPackageDependency(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e4946b59-733e-43f0-a724-3bde4c1285a0}')
    @commethod(3)
    def GetName(self, name: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPublisher(self, publisher: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetMinVersion(self, minVersion: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestPackageDependency2(ComPtr):
    extends: win32more.Windows.Win32.Storage.Packaging.Appx.IAppxManifestPackageDependency
    _iid_ = Guid('{dda0b713-f3ff-49d3-898a-2786780c5d98}')
    @commethod(6)
    def GetMaxMajorVersionTested(self, maxMajorVersionTested: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestPackageDependency3(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1ac56374-6198-4d6b-92e4-749d5ab8a895}')
    @commethod(3)
    def GetIsOptional(self, isOptional: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestPackageId(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{283ce2d7-7153-4a91-9649-7a0f7240945f}')
    @commethod(3)
    def GetName(self, name: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetArchitecture(self, architecture: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.APPX_PACKAGE_ARCHITECTURE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPublisher(self, publisher: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetVersion(self, packageVersion: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetResourceId(self, resourceId: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ComparePublisher(self, other: win32more.Windows.Win32.Foundation.PWSTR, isSame: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetPackageFullName(self, packageFullName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetPackageFamilyName(self, packageFamilyName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestPackageId2(ComPtr):
    extends: win32more.Windows.Win32.Storage.Packaging.Appx.IAppxManifestPackageId
    _iid_ = Guid('{2256999d-d617-42f1-880e-0ba4542319d5}')
    @commethod(11)
    def GetArchitecture2(self, architecture: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.APPX_PACKAGE_ARCHITECTURE2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestProperties(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{03faf64d-f26f-4b2c-aaf7-8fe7789b8bca}')
    @commethod(3)
    def GetBoolValue(self, name: win32more.Windows.Win32.Foundation.PWSTR, value: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetStringValue(self, name: win32more.Windows.Win32.Foundation.PWSTR, value: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestQualifiedResource(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3b53a497-3c5c-48d1-9ea3-bb7eac8cd7d4}')
    @commethod(3)
    def GetLanguage(self, language: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetScale(self, scale: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDXFeatureLevel(self, dxFeatureLevel: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.DX_FEATURE_LEVEL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestQualifiedResourcesEnumerator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8ef6adfe-3762-4a8f-9373-2fc5d444c8d2}')
    @commethod(3)
    def GetCurrent(self, resource: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxManifestQualifiedResource)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHasCurrent(self, hasCurrent: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MoveNext(self, hasNext: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestReader(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4e1bd148-55a0-4480-a3d1-15544710637c}')
    @commethod(3)
    def GetPackageId(self, packageId: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxManifestPackageId)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetProperties(self, packageProperties: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxManifestProperties)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPackageDependencies(self, dependencies: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxManifestPackageDependenciesEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCapabilities(self, capabilities: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.APPX_CAPABILITIES)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetResources(self, resources: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxManifestResourcesEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetDeviceCapabilities(self, deviceCapabilities: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxManifestDeviceCapabilitiesEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetPrerequisite(self, name: win32more.Windows.Win32.Foundation.PWSTR, value: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetApplications(self, applications: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxManifestApplicationsEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetStream(self, manifestStream: POINTER(win32more.Windows.Win32.System.Com.IStream)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestReader2(ComPtr):
    extends: win32more.Windows.Win32.Storage.Packaging.Appx.IAppxManifestReader
    _iid_ = Guid('{d06f67bc-b31d-4eba-a8af-638e73e77b4d}')
    @commethod(12)
    def GetQualifiedResources(self, resources: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxManifestQualifiedResourcesEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestReader3(ComPtr):
    extends: win32more.Windows.Win32.Storage.Packaging.Appx.IAppxManifestReader2
    _iid_ = Guid('{c43825ab-69b7-400a-9709-cc37f5a72d24}')
    @commethod(13)
    def GetCapabilitiesByCapabilityClass(self, capabilityClass: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_CAPABILITY_CLASS_TYPE, capabilities: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxManifestCapabilitiesEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetTargetDeviceFamilies(self, targetDeviceFamilies: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxManifestTargetDeviceFamiliesEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestReader4(ComPtr):
    extends: win32more.Windows.Win32.Storage.Packaging.Appx.IAppxManifestReader3
    _iid_ = Guid('{4579bb7c-741d-4161-b5a1-47bd3b78ad9b}')
    @commethod(15)
    def GetOptionalPackageInfo(self, optionalPackageInfo: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxManifestOptionalPackageInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestReader5(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8d7ae132-a690-4c00-b75a-6aae1feaac80}')
    @commethod(3)
    def GetMainPackageDependencies(self, mainPackageDependencies: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxManifestMainPackageDependenciesEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestReader6(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{34deaca4-d3c0-4e3e-b312-e42625e3807e}')
    @commethod(3)
    def GetIsNonQualifiedResourcePackage(self, isNonQualifiedResourcePackage: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestReader7(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8efe6f27-0ce0-4988-b32d-738eb63db3b7}')
    @commethod(3)
    def GetDriverDependencies(self, driverDependencies: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxManifestDriverDependenciesEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetOSPackageDependencies(self, osPackageDependencies: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxManifestOSPackageDependenciesEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetHostRuntimeDependencies(self, hostRuntimeDependencies: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxManifestHostRuntimeDependenciesEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestResourcesEnumerator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{de4dfbbd-881a-48bb-858c-d6f2baeae6ed}')
    @commethod(3)
    def GetCurrent(self, resource: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHasCurrent(self, hasCurrent: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MoveNext(self, hasNext: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestTargetDeviceFamiliesEnumerator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{36537f36-27a4-4788-88c0-733819575017}')
    @commethod(3)
    def GetCurrent(self, targetDeviceFamily: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxManifestTargetDeviceFamily)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHasCurrent(self, hasCurrent: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MoveNext(self, hasNext: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxManifestTargetDeviceFamily(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9091b09b-c8d5-4f31-8687-a338259faefb}')
    @commethod(3)
    def GetName(self, name: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMinVersion(self, minVersion: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetMaxVersionTested(self, maxVersionTested: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxPackageEditor(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e2adb6dc-5e71-4416-86b6-86e5f5291a6b}')
    @commethod(3)
    def SetWorkingDirectory(self, workingDirectory: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateDeltaPackage(self, updatedPackageStream: win32more.Windows.Win32.System.Com.IStream, baselinePackageStream: win32more.Windows.Win32.System.Com.IStream, deltaPackageStream: win32more.Windows.Win32.System.Com.IStream) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateDeltaPackageUsingBaselineBlockMap(self, updatedPackageStream: win32more.Windows.Win32.System.Com.IStream, baselineBlockMapStream: win32more.Windows.Win32.System.Com.IStream, baselinePackageFullName: win32more.Windows.Win32.Foundation.PWSTR, deltaPackageStream: win32more.Windows.Win32.System.Com.IStream) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def UpdatePackage(self, baselinePackageStream: win32more.Windows.Win32.System.Com.IStream, deltaPackageStream: win32more.Windows.Win32.System.Com.IStream, updateOption: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_PACKAGE_EDITOR_UPDATE_PACKAGE_OPTION) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def UpdateEncryptedPackage(self, baselineEncryptedPackageStream: win32more.Windows.Win32.System.Com.IStream, deltaPackageStream: win32more.Windows.Win32.System.Com.IStream, updateOption: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_PACKAGE_EDITOR_UPDATE_PACKAGE_OPTION, settings: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.APPX_ENCRYPTED_PACKAGE_SETTINGS2), keyInfo: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.APPX_KEY_INFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def UpdatePackageManifest(self, packageStream: win32more.Windows.Win32.System.Com.IStream, updatedManifestStream: win32more.Windows.Win32.System.Com.IStream, isPackageEncrypted: win32more.Windows.Win32.Foundation.BOOL, options: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_PACKAGE_EDITOR_UPDATE_PACKAGE_MANIFEST_OPTIONS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxPackageReader(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b5c49650-99bc-481c-9a34-3d53a4106708}')
    @commethod(3)
    def GetBlockMap(self, blockMapReader: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxBlockMapReader)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFootprintFile(self, type: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_FOOTPRINT_FILE_TYPE, file: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxFile)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPayloadFile(self, fileName: win32more.Windows.Win32.Foundation.PWSTR, file: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxFile)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPayloadFiles(self, filesEnumerator: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxFilesEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetManifest(self, manifestReader: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxManifestReader)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxPackageWriter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9099e33b-246f-41e4-881a-008eb613f858}')
    @commethod(3)
    def AddPayloadFile(self, fileName: win32more.Windows.Win32.Foundation.PWSTR, contentType: win32more.Windows.Win32.Foundation.PWSTR, compressionOption: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_COMPRESSION_OPTION, inputStream: win32more.Windows.Win32.System.Com.IStream) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Close(self, manifest: win32more.Windows.Win32.System.Com.IStream) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxPackageWriter2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2cf5c4fd-e54c-4ea5-ba4e-f8c4b105a8c8}')
    @commethod(3)
    def Close(self, manifest: win32more.Windows.Win32.System.Com.IStream, contentGroupMap: win32more.Windows.Win32.System.Com.IStream) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxPackageWriter3(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a83aacd3-41c0-4501-b8a3-74164f50b2fd}')
    @commethod(3)
    def AddPayloadFiles(self, fileCount: UInt32, payloadFiles: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.APPX_PACKAGE_WRITER_PAYLOAD_STREAM), memoryLimit: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxPackagingDiagnosticEventSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{17239d47-6adb-45d2-80f6-f9cbc3bf059d}')
    @commethod(3)
    def ReportContextChange(self, changeType: win32more.Windows.Win32.Storage.Packaging.Appx.APPX_PACKAGING_CONTEXT_CHANGE_TYPE, contextId: Int32, contextName: win32more.Windows.Win32.Foundation.PSTR, contextMessage: win32more.Windows.Win32.Foundation.PWSTR, detailsMessage: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ReportError(self, errorMessage: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxPackagingDiagnosticEventSinkManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{369648fa-a7eb-4909-a15d-6954a078f18a}')
    @commethod(3)
    def SetSinkForProcess(self, sink: win32more.Windows.Win32.Storage.Packaging.Appx.IAppxPackagingDiagnosticEventSink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppxSourceContentGroupMapReader(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f329791d-540b-4a9f-bc75-3282b7d73193}')
    @commethod(3)
    def GetRequiredGroup(self, requiredGroup: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxContentGroup)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAutomaticGroups(self, automaticGroupsEnumerator: POINTER(win32more.Windows.Win32.Storage.Packaging.Appx.IAppxContentGroupsEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
PACKAGEDEPENDENCY_CONTEXT = VoidPtr
if ARCH in 'X64,ARM64':
    class PACKAGE_ID(Structure):
        reserved: UInt32
        processorArchitecture: UInt32
        version: win32more.Windows.Win32.Storage.Packaging.Appx.PACKAGE_VERSION
        name: win32more.Windows.Win32.Foundation.PWSTR
        publisher: win32more.Windows.Win32.Foundation.PWSTR
        resourceId: win32more.Windows.Win32.Foundation.PWSTR
        publisherId: win32more.Windows.Win32.Foundation.PWSTR
        _pack_ = 4
elif ARCH in 'X86':
    class PACKAGE_ID(Structure):
        reserved: UInt32
        processorArchitecture: UInt32
        version: win32more.Windows.Win32.Storage.Packaging.Appx.PACKAGE_VERSION
        name: win32more.Windows.Win32.Foundation.PWSTR
        publisher: win32more.Windows.Win32.Foundation.PWSTR
        resourceId: win32more.Windows.Win32.Foundation.PWSTR
        publisherId: win32more.Windows.Win32.Foundation.PWSTR
if ARCH in 'X64,ARM64':
    class PACKAGE_INFO(Structure):
        reserved: UInt32
        flags: UInt32
        path: win32more.Windows.Win32.Foundation.PWSTR
        packageFullName: win32more.Windows.Win32.Foundation.PWSTR
        packageFamilyName: win32more.Windows.Win32.Foundation.PWSTR
        packageId: win32more.Windows.Win32.Storage.Packaging.Appx.PACKAGE_ID
        _pack_ = 4
elif ARCH in 'X86':
    class PACKAGE_INFO(Structure):
        reserved: UInt32
        flags: UInt32
        path: win32more.Windows.Win32.Foundation.PWSTR
        packageFullName: win32more.Windows.Win32.Foundation.PWSTR
        packageFamilyName: win32more.Windows.Win32.Foundation.PWSTR
        packageId: win32more.Windows.Win32.Storage.Packaging.Appx.PACKAGE_ID
class PACKAGE_VERSION(Structure):
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Version: UInt64
        Anonymous: _Anonymous_e__Struct
        _pack_ = 4
        class _Anonymous_e__Struct(Structure):
            Revision: UInt16
            Build: UInt16
            Minor: UInt16
            Major: UInt16
PACKAGE_VIRTUALIZATION_CONTEXT_HANDLE = VoidPtr
PackageDependencyLifetimeKind = Int32
PackageDependencyLifetimeKind_Process: win32more.Windows.Win32.Storage.Packaging.Appx.PackageDependencyLifetimeKind = 0
PackageDependencyLifetimeKind_FilePath: win32more.Windows.Win32.Storage.Packaging.Appx.PackageDependencyLifetimeKind = 1
PackageDependencyLifetimeKind_RegistryKey: win32more.Windows.Win32.Storage.Packaging.Appx.PackageDependencyLifetimeKind = 2
PackageDependencyProcessorArchitectures = Int32
PackageDependencyProcessorArchitectures_None: win32more.Windows.Win32.Storage.Packaging.Appx.PackageDependencyProcessorArchitectures = 0
PackageDependencyProcessorArchitectures_Neutral: win32more.Windows.Win32.Storage.Packaging.Appx.PackageDependencyProcessorArchitectures = 1
PackageDependencyProcessorArchitectures_X86: win32more.Windows.Win32.Storage.Packaging.Appx.PackageDependencyProcessorArchitectures = 2
PackageDependencyProcessorArchitectures_X64: win32more.Windows.Win32.Storage.Packaging.Appx.PackageDependencyProcessorArchitectures = 4
PackageDependencyProcessorArchitectures_Arm: win32more.Windows.Win32.Storage.Packaging.Appx.PackageDependencyProcessorArchitectures = 8
PackageDependencyProcessorArchitectures_Arm64: win32more.Windows.Win32.Storage.Packaging.Appx.PackageDependencyProcessorArchitectures = 16
PackageDependencyProcessorArchitectures_X86A64: win32more.Windows.Win32.Storage.Packaging.Appx.PackageDependencyProcessorArchitectures = 32
PackageInfo3Type = Int32
PackageInfo3Type_PackageInfoGeneration: win32more.Windows.Win32.Storage.Packaging.Appx.PackageInfo3Type = 16
PackageOrigin = Int32
PackageOrigin_Unknown: win32more.Windows.Win32.Storage.Packaging.Appx.PackageOrigin = 0
PackageOrigin_Unsigned: win32more.Windows.Win32.Storage.Packaging.Appx.PackageOrigin = 1
PackageOrigin_Inbox: win32more.Windows.Win32.Storage.Packaging.Appx.PackageOrigin = 2
PackageOrigin_Store: win32more.Windows.Win32.Storage.Packaging.Appx.PackageOrigin = 3
PackageOrigin_DeveloperUnsigned: win32more.Windows.Win32.Storage.Packaging.Appx.PackageOrigin = 4
PackageOrigin_DeveloperSigned: win32more.Windows.Win32.Storage.Packaging.Appx.PackageOrigin = 5
PackageOrigin_LineOfBusiness: win32more.Windows.Win32.Storage.Packaging.Appx.PackageOrigin = 6
PackagePathType = Int32
PackagePathType_Install: win32more.Windows.Win32.Storage.Packaging.Appx.PackagePathType = 0
PackagePathType_Mutable: win32more.Windows.Win32.Storage.Packaging.Appx.PackagePathType = 1
PackagePathType_Effective: win32more.Windows.Win32.Storage.Packaging.Appx.PackagePathType = 2
PackagePathType_MachineExternal: win32more.Windows.Win32.Storage.Packaging.Appx.PackagePathType = 3
PackagePathType_UserExternal: win32more.Windows.Win32.Storage.Packaging.Appx.PackagePathType = 4
PackagePathType_EffectiveExternal: win32more.Windows.Win32.Storage.Packaging.Appx.PackagePathType = 5
class _PACKAGE_INFO_REFERENCE(Structure):
    reserved: VoidPtr


make_ready(__name__)
