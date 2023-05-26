from __future__ import annotations
from ctypes import POINTER
from Windows import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import Windows.Win32.Foundation
import Windows.Win32.Security
import Windows.Win32.Storage.DistributedFileSystem
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
FSCTL_DFS_BASE: UInt32 = 6
DFS_VOLUME_STATES: UInt32 = 15
DFS_VOLUME_STATE_OK: UInt32 = 1
DFS_VOLUME_STATE_INCONSISTENT: UInt32 = 2
DFS_VOLUME_STATE_OFFLINE: UInt32 = 3
DFS_VOLUME_STATE_ONLINE: UInt32 = 4
DFS_VOLUME_STATE_RESYNCHRONIZE: UInt32 = 16
DFS_VOLUME_STATE_STANDBY: UInt32 = 32
DFS_VOLUME_STATE_FORCE_SYNC: UInt32 = 64
DFS_VOLUME_FLAVORS: UInt32 = 768
DFS_VOLUME_FLAVOR_UNUSED1: UInt32 = 0
DFS_VOLUME_FLAVOR_STANDALONE: UInt32 = 256
DFS_VOLUME_FLAVOR_AD_BLOB: UInt32 = 512
DFS_STORAGE_FLAVOR_UNUSED2: UInt32 = 768
DFS_STORAGE_STATES: UInt32 = 15
DFS_STORAGE_STATE_OFFLINE: UInt32 = 1
DFS_STORAGE_STATE_ONLINE: UInt32 = 2
DFS_STORAGE_STATE_ACTIVE: UInt32 = 4
DFS_PROPERTY_FLAG_INSITE_REFERRALS: UInt32 = 1
DFS_PROPERTY_FLAG_ROOT_SCALABILITY: UInt32 = 2
DFS_PROPERTY_FLAG_SITE_COSTING: UInt32 = 4
DFS_PROPERTY_FLAG_TARGET_FAILBACK: UInt32 = 8
DFS_PROPERTY_FLAG_CLUSTER_ENABLED: UInt32 = 16
DFS_PROPERTY_FLAG_ABDE: UInt32 = 32
DFS_ADD_VOLUME: UInt32 = 1
DFS_RESTORE_VOLUME: UInt32 = 2
NET_DFS_SETDC_FLAGS: UInt32 = 0
NET_DFS_SETDC_TIMEOUT: UInt32 = 1
NET_DFS_SETDC_INITPKT: UInt32 = 2
DFS_SITE_PRIMARY: UInt32 = 1
DFS_MOVE_FLAG_REPLACE_IF_EXISTS: UInt32 = 1
DFS_FORCE_REMOVE: UInt32 = 2147483648
FSCTL_DFS_GET_PKT_ENTRY_STATE: UInt32 = 401340
@winfunctype('NETAPI32.dll')
def NetDfsAdd(DfsEntryPath: Windows.Win32.Foundation.PWSTR, ServerName: Windows.Win32.Foundation.PWSTR, ShareName: Windows.Win32.Foundation.PWSTR, Comment: Windows.Win32.Foundation.PWSTR, Flags: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetDfsAddStdRoot(ServerName: Windows.Win32.Foundation.PWSTR, RootShare: Windows.Win32.Foundation.PWSTR, Comment: Windows.Win32.Foundation.PWSTR, Flags: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetDfsRemoveStdRoot(ServerName: Windows.Win32.Foundation.PWSTR, RootShare: Windows.Win32.Foundation.PWSTR, Flags: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetDfsAddFtRoot(ServerName: Windows.Win32.Foundation.PWSTR, RootShare: Windows.Win32.Foundation.PWSTR, FtDfsName: Windows.Win32.Foundation.PWSTR, Comment: Windows.Win32.Foundation.PWSTR, Flags: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetDfsRemoveFtRoot(ServerName: Windows.Win32.Foundation.PWSTR, RootShare: Windows.Win32.Foundation.PWSTR, FtDfsName: Windows.Win32.Foundation.PWSTR, Flags: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetDfsRemoveFtRootForced(DomainName: Windows.Win32.Foundation.PWSTR, ServerName: Windows.Win32.Foundation.PWSTR, RootShare: Windows.Win32.Foundation.PWSTR, FtDfsName: Windows.Win32.Foundation.PWSTR, Flags: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetDfsRemove(DfsEntryPath: Windows.Win32.Foundation.PWSTR, ServerName: Windows.Win32.Foundation.PWSTR, ShareName: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetDfsEnum(DfsName: Windows.Win32.Foundation.PWSTR, Level: UInt32, PrefMaxLen: UInt32, Buffer: POINTER(POINTER(Byte)), EntriesRead: POINTER(UInt32), ResumeHandle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetDfsGetInfo(DfsEntryPath: Windows.Win32.Foundation.PWSTR, ServerName: Windows.Win32.Foundation.PWSTR, ShareName: Windows.Win32.Foundation.PWSTR, Level: UInt32, Buffer: POINTER(POINTER(Byte))) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetDfsSetInfo(DfsEntryPath: Windows.Win32.Foundation.PWSTR, ServerName: Windows.Win32.Foundation.PWSTR, ShareName: Windows.Win32.Foundation.PWSTR, Level: UInt32, Buffer: POINTER(Byte)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetDfsGetClientInfo(DfsEntryPath: Windows.Win32.Foundation.PWSTR, ServerName: Windows.Win32.Foundation.PWSTR, ShareName: Windows.Win32.Foundation.PWSTR, Level: UInt32, Buffer: POINTER(POINTER(Byte))) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetDfsSetClientInfo(DfsEntryPath: Windows.Win32.Foundation.PWSTR, ServerName: Windows.Win32.Foundation.PWSTR, ShareName: Windows.Win32.Foundation.PWSTR, Level: UInt32, Buffer: POINTER(Byte)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetDfsMove(OldDfsEntryPath: Windows.Win32.Foundation.PWSTR, NewDfsEntryPath: Windows.Win32.Foundation.PWSTR, Flags: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetDfsAddRootTarget(pDfsPath: Windows.Win32.Foundation.PWSTR, pTargetPath: Windows.Win32.Foundation.PWSTR, MajorVersion: UInt32, pComment: Windows.Win32.Foundation.PWSTR, Flags: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetDfsRemoveRootTarget(pDfsPath: Windows.Win32.Foundation.PWSTR, pTargetPath: Windows.Win32.Foundation.PWSTR, Flags: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetDfsGetSecurity(DfsEntryPath: Windows.Win32.Foundation.PWSTR, SecurityInformation: UInt32, ppSecurityDescriptor: POINTER(Windows.Win32.Security.PSECURITY_DESCRIPTOR), lpcbSecurityDescriptor: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetDfsSetSecurity(DfsEntryPath: Windows.Win32.Foundation.PWSTR, SecurityInformation: UInt32, pSecurityDescriptor: Windows.Win32.Security.PSECURITY_DESCRIPTOR) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetDfsGetStdContainerSecurity(MachineName: Windows.Win32.Foundation.PWSTR, SecurityInformation: UInt32, ppSecurityDescriptor: POINTER(Windows.Win32.Security.PSECURITY_DESCRIPTOR), lpcbSecurityDescriptor: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetDfsSetStdContainerSecurity(MachineName: Windows.Win32.Foundation.PWSTR, SecurityInformation: UInt32, pSecurityDescriptor: Windows.Win32.Security.PSECURITY_DESCRIPTOR) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetDfsGetFtContainerSecurity(DomainName: Windows.Win32.Foundation.PWSTR, SecurityInformation: UInt32, ppSecurityDescriptor: POINTER(Windows.Win32.Security.PSECURITY_DESCRIPTOR), lpcbSecurityDescriptor: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetDfsSetFtContainerSecurity(DomainName: Windows.Win32.Foundation.PWSTR, SecurityInformation: UInt32, pSecurityDescriptor: Windows.Win32.Security.PSECURITY_DESCRIPTOR) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetDfsGetSupportedNamespaceVersion(Origin: Windows.Win32.Storage.DistributedFileSystem.DFS_NAMESPACE_VERSION_ORIGIN, pName: Windows.Win32.Foundation.PWSTR, ppVersionInfo: POINTER(POINTER(Windows.Win32.Storage.DistributedFileSystem.DFS_SUPPORTED_NAMESPACE_VERSION_INFO_head))) -> UInt32: ...
class DFS_GET_PKT_ENTRY_STATE_ARG(EasyCastStructure):
    DfsEntryPathLen: UInt16
    ServerNameLen: UInt16
    ShareNameLen: UInt16
    Level: UInt32
    Buffer: Char * 1
class DFS_INFO_1(EasyCastStructure):
    EntryPath: Windows.Win32.Foundation.PWSTR
class DFS_INFO_100(EasyCastStructure):
    Comment: Windows.Win32.Foundation.PWSTR
class DFS_INFO_101(EasyCastStructure):
    State: UInt32
class DFS_INFO_102(EasyCastStructure):
    Timeout: UInt32
class DFS_INFO_103(EasyCastStructure):
    PropertyFlagMask: UInt32
    PropertyFlags: UInt32
class DFS_INFO_104(EasyCastStructure):
    TargetPriority: Windows.Win32.Storage.DistributedFileSystem.DFS_TARGET_PRIORITY
class DFS_INFO_105(EasyCastStructure):
    Comment: Windows.Win32.Foundation.PWSTR
    State: UInt32
    Timeout: UInt32
    PropertyFlagMask: UInt32
    PropertyFlags: UInt32
class DFS_INFO_106(EasyCastStructure):
    State: UInt32
    TargetPriority: Windows.Win32.Storage.DistributedFileSystem.DFS_TARGET_PRIORITY
class DFS_INFO_107(EasyCastStructure):
    Comment: Windows.Win32.Foundation.PWSTR
    State: UInt32
    Timeout: UInt32
    PropertyFlagMask: UInt32
    PropertyFlags: UInt32
    SdLengthReserved: UInt32
    pSecurityDescriptor: Windows.Win32.Security.PSECURITY_DESCRIPTOR
class DFS_INFO_150(EasyCastStructure):
    SdLengthReserved: UInt32
    pSecurityDescriptor: Windows.Win32.Security.PSECURITY_DESCRIPTOR
if ARCH in 'X64,ARM64':
    class DFS_INFO_1_32(EasyCastStructure):
        EntryPath: UInt32
class DFS_INFO_2(EasyCastStructure):
    EntryPath: Windows.Win32.Foundation.PWSTR
    Comment: Windows.Win32.Foundation.PWSTR
    State: UInt32
    NumberOfStorages: UInt32
class DFS_INFO_200(EasyCastStructure):
    FtDfsName: Windows.Win32.Foundation.PWSTR
if ARCH in 'X64,ARM64':
    class DFS_INFO_2_32(EasyCastStructure):
        EntryPath: UInt32
        Comment: UInt32
        State: UInt32
        NumberOfStorages: UInt32
class DFS_INFO_3(EasyCastStructure):
    EntryPath: Windows.Win32.Foundation.PWSTR
    Comment: Windows.Win32.Foundation.PWSTR
    State: UInt32
    NumberOfStorages: UInt32
    Storage: POINTER(Windows.Win32.Storage.DistributedFileSystem.DFS_STORAGE_INFO_head)
class DFS_INFO_300(EasyCastStructure):
    Flags: UInt32
    DfsName: Windows.Win32.Foundation.PWSTR
if ARCH in 'X64,ARM64':
    class DFS_INFO_3_32(EasyCastStructure):
        EntryPath: UInt32
        Comment: UInt32
        State: UInt32
        NumberOfStorages: UInt32
        Storage: UInt32
class DFS_INFO_4(EasyCastStructure):
    EntryPath: Windows.Win32.Foundation.PWSTR
    Comment: Windows.Win32.Foundation.PWSTR
    State: UInt32
    Timeout: UInt32
    Guid: Guid
    NumberOfStorages: UInt32
    Storage: POINTER(Windows.Win32.Storage.DistributedFileSystem.DFS_STORAGE_INFO_head)
if ARCH in 'X64,ARM64':
    class DFS_INFO_4_32(EasyCastStructure):
        EntryPath: UInt32
        Comment: UInt32
        State: UInt32
        Timeout: UInt32
        Guid: Guid
        NumberOfStorages: UInt32
        Storage: UInt32
class DFS_INFO_5(EasyCastStructure):
    EntryPath: Windows.Win32.Foundation.PWSTR
    Comment: Windows.Win32.Foundation.PWSTR
    State: UInt32
    Timeout: UInt32
    Guid: Guid
    PropertyFlags: UInt32
    MetadataSize: UInt32
    NumberOfStorages: UInt32
class DFS_INFO_50(EasyCastStructure):
    NamespaceMajorVersion: UInt32
    NamespaceMinorVersion: UInt32
    NamespaceCapabilities: UInt64
class DFS_INFO_6(EasyCastStructure):
    EntryPath: Windows.Win32.Foundation.PWSTR
    Comment: Windows.Win32.Foundation.PWSTR
    State: UInt32
    Timeout: UInt32
    Guid: Guid
    PropertyFlags: UInt32
    MetadataSize: UInt32
    NumberOfStorages: UInt32
    Storage: POINTER(Windows.Win32.Storage.DistributedFileSystem.DFS_STORAGE_INFO_1_head)
class DFS_INFO_7(EasyCastStructure):
    GenerationGuid: Guid
class DFS_INFO_8(EasyCastStructure):
    EntryPath: Windows.Win32.Foundation.PWSTR
    Comment: Windows.Win32.Foundation.PWSTR
    State: UInt32
    Timeout: UInt32
    Guid: Guid
    PropertyFlags: UInt32
    MetadataSize: UInt32
    SdLengthReserved: UInt32
    pSecurityDescriptor: Windows.Win32.Security.PSECURITY_DESCRIPTOR
    NumberOfStorages: UInt32
class DFS_INFO_9(EasyCastStructure):
    EntryPath: Windows.Win32.Foundation.PWSTR
    Comment: Windows.Win32.Foundation.PWSTR
    State: UInt32
    Timeout: UInt32
    Guid: Guid
    PropertyFlags: UInt32
    MetadataSize: UInt32
    SdLengthReserved: UInt32
    pSecurityDescriptor: Windows.Win32.Security.PSECURITY_DESCRIPTOR
    NumberOfStorages: UInt32
    Storage: POINTER(Windows.Win32.Storage.DistributedFileSystem.DFS_STORAGE_INFO_1_head)
DFS_NAMESPACE_VERSION_ORIGIN = Int32
DFS_NAMESPACE_VERSION_ORIGIN_COMBINED: DFS_NAMESPACE_VERSION_ORIGIN = 0
DFS_NAMESPACE_VERSION_ORIGIN_SERVER: DFS_NAMESPACE_VERSION_ORIGIN = 1
DFS_NAMESPACE_VERSION_ORIGIN_DOMAIN: DFS_NAMESPACE_VERSION_ORIGIN = 2
class DFS_SITELIST_INFO(EasyCastStructure):
    cSites: UInt32
    Site: Windows.Win32.Storage.DistributedFileSystem.DFS_SITENAME_INFO * 1
class DFS_SITENAME_INFO(EasyCastStructure):
    SiteFlags: UInt32
    SiteName: Windows.Win32.Foundation.PWSTR
class DFS_STORAGE_INFO(EasyCastStructure):
    State: UInt32
    ServerName: Windows.Win32.Foundation.PWSTR
    ShareName: Windows.Win32.Foundation.PWSTR
if ARCH in 'X64,ARM64':
    class DFS_STORAGE_INFO_0_32(EasyCastStructure):
        State: UInt32
        ServerName: UInt32
        ShareName: UInt32
class DFS_STORAGE_INFO_1(EasyCastStructure):
    State: UInt32
    ServerName: Windows.Win32.Foundation.PWSTR
    ShareName: Windows.Win32.Foundation.PWSTR
    TargetPriority: Windows.Win32.Storage.DistributedFileSystem.DFS_TARGET_PRIORITY
class DFS_SUPPORTED_NAMESPACE_VERSION_INFO(EasyCastStructure):
    DomainDfsMajorVersion: UInt32
    DomainDfsMinorVersion: UInt32
    DomainDfsCapabilities: UInt64
    StandaloneDfsMajorVersion: UInt32
    StandaloneDfsMinorVersion: UInt32
    StandaloneDfsCapabilities: UInt64
class DFS_TARGET_PRIORITY(EasyCastStructure):
    TargetPriorityClass: Windows.Win32.Storage.DistributedFileSystem.DFS_TARGET_PRIORITY_CLASS
    TargetPriorityRank: UInt16
    Reserved: UInt16
DFS_TARGET_PRIORITY_CLASS = Int32
DFS_TARGET_PRIORITY_CLASS_DfsInvalidPriorityClass: DFS_TARGET_PRIORITY_CLASS = -1
DFS_TARGET_PRIORITY_CLASS_DfsSiteCostNormalPriorityClass: DFS_TARGET_PRIORITY_CLASS = 0
DFS_TARGET_PRIORITY_CLASS_DfsGlobalHighPriorityClass: DFS_TARGET_PRIORITY_CLASS = 1
DFS_TARGET_PRIORITY_CLASS_DfsSiteCostHighPriorityClass: DFS_TARGET_PRIORITY_CLASS = 2
DFS_TARGET_PRIORITY_CLASS_DfsSiteCostLowPriorityClass: DFS_TARGET_PRIORITY_CLASS = 3
DFS_TARGET_PRIORITY_CLASS_DfsGlobalLowPriorityClass: DFS_TARGET_PRIORITY_CLASS = 4
make_head(_module, 'DFS_GET_PKT_ENTRY_STATE_ARG')
make_head(_module, 'DFS_INFO_1')
make_head(_module, 'DFS_INFO_100')
make_head(_module, 'DFS_INFO_101')
make_head(_module, 'DFS_INFO_102')
make_head(_module, 'DFS_INFO_103')
make_head(_module, 'DFS_INFO_104')
make_head(_module, 'DFS_INFO_105')
make_head(_module, 'DFS_INFO_106')
make_head(_module, 'DFS_INFO_107')
make_head(_module, 'DFS_INFO_150')
if ARCH in 'X64,ARM64':
    make_head(_module, 'DFS_INFO_1_32')
make_head(_module, 'DFS_INFO_2')
make_head(_module, 'DFS_INFO_200')
if ARCH in 'X64,ARM64':
    make_head(_module, 'DFS_INFO_2_32')
make_head(_module, 'DFS_INFO_3')
make_head(_module, 'DFS_INFO_300')
if ARCH in 'X64,ARM64':
    make_head(_module, 'DFS_INFO_3_32')
make_head(_module, 'DFS_INFO_4')
if ARCH in 'X64,ARM64':
    make_head(_module, 'DFS_INFO_4_32')
make_head(_module, 'DFS_INFO_5')
make_head(_module, 'DFS_INFO_50')
make_head(_module, 'DFS_INFO_6')
make_head(_module, 'DFS_INFO_7')
make_head(_module, 'DFS_INFO_8')
make_head(_module, 'DFS_INFO_9')
make_head(_module, 'DFS_SITELIST_INFO')
make_head(_module, 'DFS_SITENAME_INFO')
make_head(_module, 'DFS_STORAGE_INFO')
if ARCH in 'X64,ARM64':
    make_head(_module, 'DFS_STORAGE_INFO_0_32')
make_head(_module, 'DFS_STORAGE_INFO_1')
make_head(_module, 'DFS_SUPPORTED_NAMESPACE_VERSION_INFO')
make_head(_module, 'DFS_TARGET_PRIORITY')
