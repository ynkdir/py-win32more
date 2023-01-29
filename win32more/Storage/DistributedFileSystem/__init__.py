from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Security
import win32more.Storage.DistributedFileSystem
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
def NetDfsAdd(DfsEntryPath: win32more.Foundation.PWSTR, ServerName: win32more.Foundation.PWSTR, ShareName: win32more.Foundation.PWSTR, Comment: win32more.Foundation.PWSTR, Flags: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetDfsAddStdRoot(ServerName: win32more.Foundation.PWSTR, RootShare: win32more.Foundation.PWSTR, Comment: win32more.Foundation.PWSTR, Flags: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetDfsRemoveStdRoot(ServerName: win32more.Foundation.PWSTR, RootShare: win32more.Foundation.PWSTR, Flags: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetDfsAddFtRoot(ServerName: win32more.Foundation.PWSTR, RootShare: win32more.Foundation.PWSTR, FtDfsName: win32more.Foundation.PWSTR, Comment: win32more.Foundation.PWSTR, Flags: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetDfsRemoveFtRoot(ServerName: win32more.Foundation.PWSTR, RootShare: win32more.Foundation.PWSTR, FtDfsName: win32more.Foundation.PWSTR, Flags: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetDfsRemoveFtRootForced(DomainName: win32more.Foundation.PWSTR, ServerName: win32more.Foundation.PWSTR, RootShare: win32more.Foundation.PWSTR, FtDfsName: win32more.Foundation.PWSTR, Flags: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetDfsRemove(DfsEntryPath: win32more.Foundation.PWSTR, ServerName: win32more.Foundation.PWSTR, ShareName: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetDfsEnum(DfsName: win32more.Foundation.PWSTR, Level: UInt32, PrefMaxLen: UInt32, Buffer: POINTER(c_char_p_no), EntriesRead: POINTER(UInt32), ResumeHandle: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetDfsGetInfo(DfsEntryPath: win32more.Foundation.PWSTR, ServerName: win32more.Foundation.PWSTR, ShareName: win32more.Foundation.PWSTR, Level: UInt32, Buffer: POINTER(c_char_p_no)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetDfsSetInfo(DfsEntryPath: win32more.Foundation.PWSTR, ServerName: win32more.Foundation.PWSTR, ShareName: win32more.Foundation.PWSTR, Level: UInt32, Buffer: c_char_p_no) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetDfsGetClientInfo(DfsEntryPath: win32more.Foundation.PWSTR, ServerName: win32more.Foundation.PWSTR, ShareName: win32more.Foundation.PWSTR, Level: UInt32, Buffer: POINTER(c_char_p_no)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetDfsSetClientInfo(DfsEntryPath: win32more.Foundation.PWSTR, ServerName: win32more.Foundation.PWSTR, ShareName: win32more.Foundation.PWSTR, Level: UInt32, Buffer: c_char_p_no) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetDfsMove(OldDfsEntryPath: win32more.Foundation.PWSTR, NewDfsEntryPath: win32more.Foundation.PWSTR, Flags: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetDfsAddRootTarget(pDfsPath: win32more.Foundation.PWSTR, pTargetPath: win32more.Foundation.PWSTR, MajorVersion: UInt32, pComment: win32more.Foundation.PWSTR, Flags: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetDfsRemoveRootTarget(pDfsPath: win32more.Foundation.PWSTR, pTargetPath: win32more.Foundation.PWSTR, Flags: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetDfsGetSecurity(DfsEntryPath: win32more.Foundation.PWSTR, SecurityInformation: UInt32, ppSecurityDescriptor: POINTER(win32more.Security.PSECURITY_DESCRIPTOR), lpcbSecurityDescriptor: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetDfsSetSecurity(DfsEntryPath: win32more.Foundation.PWSTR, SecurityInformation: UInt32, pSecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetDfsGetStdContainerSecurity(MachineName: win32more.Foundation.PWSTR, SecurityInformation: UInt32, ppSecurityDescriptor: POINTER(win32more.Security.PSECURITY_DESCRIPTOR), lpcbSecurityDescriptor: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetDfsSetStdContainerSecurity(MachineName: win32more.Foundation.PWSTR, SecurityInformation: UInt32, pSecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetDfsGetFtContainerSecurity(DomainName: win32more.Foundation.PWSTR, SecurityInformation: UInt32, ppSecurityDescriptor: POINTER(win32more.Security.PSECURITY_DESCRIPTOR), lpcbSecurityDescriptor: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetDfsSetFtContainerSecurity(DomainName: win32more.Foundation.PWSTR, SecurityInformation: UInt32, pSecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def NetDfsGetSupportedNamespaceVersion(Origin: win32more.Storage.DistributedFileSystem.DFS_NAMESPACE_VERSION_ORIGIN, pName: win32more.Foundation.PWSTR, ppVersionInfo: POINTER(POINTER(win32more.Storage.DistributedFileSystem.DFS_SUPPORTED_NAMESPACE_VERSION_INFO_head))) -> UInt32: ...
class DFS_GET_PKT_ENTRY_STATE_ARG(Structure):
    DfsEntryPathLen: UInt16
    ServerNameLen: UInt16
    ShareNameLen: UInt16
    Level: UInt32
    Buffer: Char * 1
class DFS_INFO_1(Structure):
    EntryPath: win32more.Foundation.PWSTR
if ARCH in 'X64,ARM64':
    class DFS_INFO_1_32(Structure):
        EntryPath: UInt32
class DFS_INFO_100(Structure):
    Comment: win32more.Foundation.PWSTR
class DFS_INFO_101(Structure):
    State: UInt32
class DFS_INFO_102(Structure):
    Timeout: UInt32
class DFS_INFO_103(Structure):
    PropertyFlagMask: UInt32
    PropertyFlags: UInt32
class DFS_INFO_104(Structure):
    TargetPriority: win32more.Storage.DistributedFileSystem.DFS_TARGET_PRIORITY
class DFS_INFO_105(Structure):
    Comment: win32more.Foundation.PWSTR
    State: UInt32
    Timeout: UInt32
    PropertyFlagMask: UInt32
    PropertyFlags: UInt32
class DFS_INFO_106(Structure):
    State: UInt32
    TargetPriority: win32more.Storage.DistributedFileSystem.DFS_TARGET_PRIORITY
class DFS_INFO_107(Structure):
    Comment: win32more.Foundation.PWSTR
    State: UInt32
    Timeout: UInt32
    PropertyFlagMask: UInt32
    PropertyFlags: UInt32
    SdLengthReserved: UInt32
    pSecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR
class DFS_INFO_150(Structure):
    SdLengthReserved: UInt32
    pSecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR
class DFS_INFO_2(Structure):
    EntryPath: win32more.Foundation.PWSTR
    Comment: win32more.Foundation.PWSTR
    State: UInt32
    NumberOfStorages: UInt32
if ARCH in 'X64,ARM64':
    class DFS_INFO_2_32(Structure):
        EntryPath: UInt32
        Comment: UInt32
        State: UInt32
        NumberOfStorages: UInt32
class DFS_INFO_200(Structure):
    FtDfsName: win32more.Foundation.PWSTR
class DFS_INFO_3(Structure):
    EntryPath: win32more.Foundation.PWSTR
    Comment: win32more.Foundation.PWSTR
    State: UInt32
    NumberOfStorages: UInt32
    Storage: POINTER(win32more.Storage.DistributedFileSystem.DFS_STORAGE_INFO_head)
if ARCH in 'X64,ARM64':
    class DFS_INFO_3_32(Structure):
        EntryPath: UInt32
        Comment: UInt32
        State: UInt32
        NumberOfStorages: UInt32
        Storage: UInt32
class DFS_INFO_300(Structure):
    Flags: UInt32
    DfsName: win32more.Foundation.PWSTR
class DFS_INFO_4(Structure):
    EntryPath: win32more.Foundation.PWSTR
    Comment: win32more.Foundation.PWSTR
    State: UInt32
    Timeout: UInt32
    Guid: Guid
    NumberOfStorages: UInt32
    Storage: POINTER(win32more.Storage.DistributedFileSystem.DFS_STORAGE_INFO_head)
if ARCH in 'X64,ARM64':
    class DFS_INFO_4_32(Structure):
        EntryPath: UInt32
        Comment: UInt32
        State: UInt32
        Timeout: UInt32
        Guid: Guid
        NumberOfStorages: UInt32
        Storage: UInt32
class DFS_INFO_5(Structure):
    EntryPath: win32more.Foundation.PWSTR
    Comment: win32more.Foundation.PWSTR
    State: UInt32
    Timeout: UInt32
    Guid: Guid
    PropertyFlags: UInt32
    MetadataSize: UInt32
    NumberOfStorages: UInt32
class DFS_INFO_50(Structure):
    NamespaceMajorVersion: UInt32
    NamespaceMinorVersion: UInt32
    NamespaceCapabilities: UInt64
class DFS_INFO_6(Structure):
    EntryPath: win32more.Foundation.PWSTR
    Comment: win32more.Foundation.PWSTR
    State: UInt32
    Timeout: UInt32
    Guid: Guid
    PropertyFlags: UInt32
    MetadataSize: UInt32
    NumberOfStorages: UInt32
    Storage: POINTER(win32more.Storage.DistributedFileSystem.DFS_STORAGE_INFO_1_head)
class DFS_INFO_7(Structure):
    GenerationGuid: Guid
class DFS_INFO_8(Structure):
    EntryPath: win32more.Foundation.PWSTR
    Comment: win32more.Foundation.PWSTR
    State: UInt32
    Timeout: UInt32
    Guid: Guid
    PropertyFlags: UInt32
    MetadataSize: UInt32
    SdLengthReserved: UInt32
    pSecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR
    NumberOfStorages: UInt32
class DFS_INFO_9(Structure):
    EntryPath: win32more.Foundation.PWSTR
    Comment: win32more.Foundation.PWSTR
    State: UInt32
    Timeout: UInt32
    Guid: Guid
    PropertyFlags: UInt32
    MetadataSize: UInt32
    SdLengthReserved: UInt32
    pSecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR
    NumberOfStorages: UInt32
    Storage: POINTER(win32more.Storage.DistributedFileSystem.DFS_STORAGE_INFO_1_head)
DFS_NAMESPACE_VERSION_ORIGIN = Int32
DFS_NAMESPACE_VERSION_ORIGIN_COMBINED: DFS_NAMESPACE_VERSION_ORIGIN = 0
DFS_NAMESPACE_VERSION_ORIGIN_SERVER: DFS_NAMESPACE_VERSION_ORIGIN = 1
DFS_NAMESPACE_VERSION_ORIGIN_DOMAIN: DFS_NAMESPACE_VERSION_ORIGIN = 2
class DFS_SITELIST_INFO(Structure):
    cSites: UInt32
    Site: win32more.Storage.DistributedFileSystem.DFS_SITENAME_INFO * 1
class DFS_SITENAME_INFO(Structure):
    SiteFlags: UInt32
    SiteName: win32more.Foundation.PWSTR
class DFS_STORAGE_INFO(Structure):
    State: UInt32
    ServerName: win32more.Foundation.PWSTR
    ShareName: win32more.Foundation.PWSTR
if ARCH in 'X64,ARM64':
    class DFS_STORAGE_INFO_0_32(Structure):
        State: UInt32
        ServerName: UInt32
        ShareName: UInt32
class DFS_STORAGE_INFO_1(Structure):
    State: UInt32
    ServerName: win32more.Foundation.PWSTR
    ShareName: win32more.Foundation.PWSTR
    TargetPriority: win32more.Storage.DistributedFileSystem.DFS_TARGET_PRIORITY
class DFS_SUPPORTED_NAMESPACE_VERSION_INFO(Structure):
    DomainDfsMajorVersion: UInt32
    DomainDfsMinorVersion: UInt32
    DomainDfsCapabilities: UInt64
    StandaloneDfsMajorVersion: UInt32
    StandaloneDfsMinorVersion: UInt32
    StandaloneDfsCapabilities: UInt64
class DFS_TARGET_PRIORITY(Structure):
    TargetPriorityClass: win32more.Storage.DistributedFileSystem.DFS_TARGET_PRIORITY_CLASS
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
if ARCH in 'X64,ARM64':
    make_head(_module, 'DFS_INFO_1_32')
make_head(_module, 'DFS_INFO_100')
make_head(_module, 'DFS_INFO_101')
make_head(_module, 'DFS_INFO_102')
make_head(_module, 'DFS_INFO_103')
make_head(_module, 'DFS_INFO_104')
make_head(_module, 'DFS_INFO_105')
make_head(_module, 'DFS_INFO_106')
make_head(_module, 'DFS_INFO_107')
make_head(_module, 'DFS_INFO_150')
make_head(_module, 'DFS_INFO_2')
if ARCH in 'X64,ARM64':
    make_head(_module, 'DFS_INFO_2_32')
make_head(_module, 'DFS_INFO_200')
make_head(_module, 'DFS_INFO_3')
if ARCH in 'X64,ARM64':
    make_head(_module, 'DFS_INFO_3_32')
make_head(_module, 'DFS_INFO_300')
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
__all__ = [
    "DFS_ADD_VOLUME",
    "DFS_FORCE_REMOVE",
    "DFS_GET_PKT_ENTRY_STATE_ARG",
    "DFS_INFO_1",
    "DFS_INFO_100",
    "DFS_INFO_101",
    "DFS_INFO_102",
    "DFS_INFO_103",
    "DFS_INFO_104",
    "DFS_INFO_105",
    "DFS_INFO_106",
    "DFS_INFO_107",
    "DFS_INFO_150",
    "DFS_INFO_1_32",
    "DFS_INFO_2",
    "DFS_INFO_200",
    "DFS_INFO_2_32",
    "DFS_INFO_3",
    "DFS_INFO_300",
    "DFS_INFO_3_32",
    "DFS_INFO_4",
    "DFS_INFO_4_32",
    "DFS_INFO_5",
    "DFS_INFO_50",
    "DFS_INFO_6",
    "DFS_INFO_7",
    "DFS_INFO_8",
    "DFS_INFO_9",
    "DFS_MOVE_FLAG_REPLACE_IF_EXISTS",
    "DFS_NAMESPACE_VERSION_ORIGIN",
    "DFS_NAMESPACE_VERSION_ORIGIN_COMBINED",
    "DFS_NAMESPACE_VERSION_ORIGIN_DOMAIN",
    "DFS_NAMESPACE_VERSION_ORIGIN_SERVER",
    "DFS_PROPERTY_FLAG_ABDE",
    "DFS_PROPERTY_FLAG_CLUSTER_ENABLED",
    "DFS_PROPERTY_FLAG_INSITE_REFERRALS",
    "DFS_PROPERTY_FLAG_ROOT_SCALABILITY",
    "DFS_PROPERTY_FLAG_SITE_COSTING",
    "DFS_PROPERTY_FLAG_TARGET_FAILBACK",
    "DFS_RESTORE_VOLUME",
    "DFS_SITELIST_INFO",
    "DFS_SITENAME_INFO",
    "DFS_SITE_PRIMARY",
    "DFS_STORAGE_FLAVOR_UNUSED2",
    "DFS_STORAGE_INFO",
    "DFS_STORAGE_INFO_0_32",
    "DFS_STORAGE_INFO_1",
    "DFS_STORAGE_STATES",
    "DFS_STORAGE_STATE_ACTIVE",
    "DFS_STORAGE_STATE_OFFLINE",
    "DFS_STORAGE_STATE_ONLINE",
    "DFS_SUPPORTED_NAMESPACE_VERSION_INFO",
    "DFS_TARGET_PRIORITY",
    "DFS_TARGET_PRIORITY_CLASS",
    "DFS_TARGET_PRIORITY_CLASS_DfsGlobalHighPriorityClass",
    "DFS_TARGET_PRIORITY_CLASS_DfsGlobalLowPriorityClass",
    "DFS_TARGET_PRIORITY_CLASS_DfsInvalidPriorityClass",
    "DFS_TARGET_PRIORITY_CLASS_DfsSiteCostHighPriorityClass",
    "DFS_TARGET_PRIORITY_CLASS_DfsSiteCostLowPriorityClass",
    "DFS_TARGET_PRIORITY_CLASS_DfsSiteCostNormalPriorityClass",
    "DFS_VOLUME_FLAVORS",
    "DFS_VOLUME_FLAVOR_AD_BLOB",
    "DFS_VOLUME_FLAVOR_STANDALONE",
    "DFS_VOLUME_FLAVOR_UNUSED1",
    "DFS_VOLUME_STATES",
    "DFS_VOLUME_STATE_FORCE_SYNC",
    "DFS_VOLUME_STATE_INCONSISTENT",
    "DFS_VOLUME_STATE_OFFLINE",
    "DFS_VOLUME_STATE_OK",
    "DFS_VOLUME_STATE_ONLINE",
    "DFS_VOLUME_STATE_RESYNCHRONIZE",
    "DFS_VOLUME_STATE_STANDBY",
    "FSCTL_DFS_BASE",
    "FSCTL_DFS_GET_PKT_ENTRY_STATE",
    "NET_DFS_SETDC_FLAGS",
    "NET_DFS_SETDC_INITPKT",
    "NET_DFS_SETDC_TIMEOUT",
    "NetDfsAdd",
    "NetDfsAddFtRoot",
    "NetDfsAddRootTarget",
    "NetDfsAddStdRoot",
    "NetDfsEnum",
    "NetDfsGetClientInfo",
    "NetDfsGetFtContainerSecurity",
    "NetDfsGetInfo",
    "NetDfsGetSecurity",
    "NetDfsGetStdContainerSecurity",
    "NetDfsGetSupportedNamespaceVersion",
    "NetDfsMove",
    "NetDfsRemove",
    "NetDfsRemoveFtRoot",
    "NetDfsRemoveFtRootForced",
    "NetDfsRemoveRootTarget",
    "NetDfsRemoveStdRoot",
    "NetDfsSetClientInfo",
    "NetDfsSetFtContainerSecurity",
    "NetDfsSetInfo",
    "NetDfsSetSecurity",
    "NetDfsSetStdContainerSecurity",
]
_arch_optional = [
    "DFS_INFO_1_32",
    "DFS_INFO_2_32",
    "DFS_INFO_3_32",
    "DFS_INFO_4_32",
    "DFS_STORAGE_INFO_0_32",
]
