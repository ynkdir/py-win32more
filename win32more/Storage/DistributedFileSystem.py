from win32more import *
import win32more.Foundation
import win32more.Security
import win32more.Storage.DistributedFileSystem

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
FSCTL_DFS_BASE = 6
DFS_VOLUME_STATES = 15
DFS_VOLUME_STATE_OK = 1
DFS_VOLUME_STATE_INCONSISTENT = 2
DFS_VOLUME_STATE_OFFLINE = 3
DFS_VOLUME_STATE_ONLINE = 4
DFS_VOLUME_STATE_RESYNCHRONIZE = 16
DFS_VOLUME_STATE_STANDBY = 32
DFS_VOLUME_STATE_FORCE_SYNC = 64
DFS_VOLUME_FLAVORS = 768
DFS_VOLUME_FLAVOR_UNUSED1 = 0
DFS_VOLUME_FLAVOR_STANDALONE = 256
DFS_VOLUME_FLAVOR_AD_BLOB = 512
DFS_STORAGE_FLAVOR_UNUSED2 = 768
DFS_STORAGE_STATES = 15
DFS_STORAGE_STATE_OFFLINE = 1
DFS_STORAGE_STATE_ONLINE = 2
DFS_STORAGE_STATE_ACTIVE = 4
DFS_PROPERTY_FLAG_INSITE_REFERRALS = 1
DFS_PROPERTY_FLAG_ROOT_SCALABILITY = 2
DFS_PROPERTY_FLAG_SITE_COSTING = 4
DFS_PROPERTY_FLAG_TARGET_FAILBACK = 8
DFS_PROPERTY_FLAG_CLUSTER_ENABLED = 16
DFS_PROPERTY_FLAG_ABDE = 32
DFS_ADD_VOLUME = 1
DFS_RESTORE_VOLUME = 2
NET_DFS_SETDC_FLAGS = 0
NET_DFS_SETDC_TIMEOUT = 1
NET_DFS_SETDC_INITPKT = 2
DFS_SITE_PRIMARY = 1
DFS_MOVE_FLAG_REPLACE_IF_EXISTS = 1
DFS_FORCE_REMOVE = 2147483648
FSCTL_DFS_GET_PKT_ENTRY_STATE = 401340
DFS_TARGET_PRIORITY_CLASS = Int32
DFS_TARGET_PRIORITY_CLASS_DfsInvalidPriorityClass = -1
DFS_TARGET_PRIORITY_CLASS_DfsSiteCostNormalPriorityClass = 0
DFS_TARGET_PRIORITY_CLASS_DfsGlobalHighPriorityClass = 1
DFS_TARGET_PRIORITY_CLASS_DfsSiteCostHighPriorityClass = 2
DFS_TARGET_PRIORITY_CLASS_DfsSiteCostLowPriorityClass = 3
DFS_TARGET_PRIORITY_CLASS_DfsGlobalLowPriorityClass = 4
def _define_DFS_TARGET_PRIORITY_head():
    class DFS_TARGET_PRIORITY(Structure):
        pass
    return DFS_TARGET_PRIORITY
def _define_DFS_TARGET_PRIORITY():
    DFS_TARGET_PRIORITY = win32more.Storage.DistributedFileSystem.DFS_TARGET_PRIORITY_head
    DFS_TARGET_PRIORITY._fields_ = [
        ("TargetPriorityClass", win32more.Storage.DistributedFileSystem.DFS_TARGET_PRIORITY_CLASS),
        ("TargetPriorityRank", UInt16),
        ("Reserved", UInt16),
    ]
    return DFS_TARGET_PRIORITY
def _define_DFS_INFO_1_head():
    class DFS_INFO_1(Structure):
        pass
    return DFS_INFO_1
def _define_DFS_INFO_1():
    DFS_INFO_1 = win32more.Storage.DistributedFileSystem.DFS_INFO_1_head
    DFS_INFO_1._fields_ = [
        ("EntryPath", win32more.Foundation.PWSTR),
    ]
    return DFS_INFO_1
def _define_DFS_INFO_1_32_head():
    class DFS_INFO_1_32(Structure):
        pass
    return DFS_INFO_1_32
def _define_DFS_INFO_1_32():
    DFS_INFO_1_32 = win32more.Storage.DistributedFileSystem.DFS_INFO_1_32_head
    DFS_INFO_1_32._fields_ = [
        ("EntryPath", UInt32),
    ]
    return DFS_INFO_1_32
def _define_DFS_INFO_2_head():
    class DFS_INFO_2(Structure):
        pass
    return DFS_INFO_2
def _define_DFS_INFO_2():
    DFS_INFO_2 = win32more.Storage.DistributedFileSystem.DFS_INFO_2_head
    DFS_INFO_2._fields_ = [
        ("EntryPath", win32more.Foundation.PWSTR),
        ("Comment", win32more.Foundation.PWSTR),
        ("State", UInt32),
        ("NumberOfStorages", UInt32),
    ]
    return DFS_INFO_2
def _define_DFS_INFO_2_32_head():
    class DFS_INFO_2_32(Structure):
        pass
    return DFS_INFO_2_32
def _define_DFS_INFO_2_32():
    DFS_INFO_2_32 = win32more.Storage.DistributedFileSystem.DFS_INFO_2_32_head
    DFS_INFO_2_32._fields_ = [
        ("EntryPath", UInt32),
        ("Comment", UInt32),
        ("State", UInt32),
        ("NumberOfStorages", UInt32),
    ]
    return DFS_INFO_2_32
def _define_DFS_STORAGE_INFO_head():
    class DFS_STORAGE_INFO(Structure):
        pass
    return DFS_STORAGE_INFO
def _define_DFS_STORAGE_INFO():
    DFS_STORAGE_INFO = win32more.Storage.DistributedFileSystem.DFS_STORAGE_INFO_head
    DFS_STORAGE_INFO._fields_ = [
        ("State", UInt32),
        ("ServerName", win32more.Foundation.PWSTR),
        ("ShareName", win32more.Foundation.PWSTR),
    ]
    return DFS_STORAGE_INFO
def _define_DFS_STORAGE_INFO_0_32_head():
    class DFS_STORAGE_INFO_0_32(Structure):
        pass
    return DFS_STORAGE_INFO_0_32
def _define_DFS_STORAGE_INFO_0_32():
    DFS_STORAGE_INFO_0_32 = win32more.Storage.DistributedFileSystem.DFS_STORAGE_INFO_0_32_head
    DFS_STORAGE_INFO_0_32._fields_ = [
        ("State", UInt32),
        ("ServerName", UInt32),
        ("ShareName", UInt32),
    ]
    return DFS_STORAGE_INFO_0_32
def _define_DFS_STORAGE_INFO_1_head():
    class DFS_STORAGE_INFO_1(Structure):
        pass
    return DFS_STORAGE_INFO_1
def _define_DFS_STORAGE_INFO_1():
    DFS_STORAGE_INFO_1 = win32more.Storage.DistributedFileSystem.DFS_STORAGE_INFO_1_head
    DFS_STORAGE_INFO_1._fields_ = [
        ("State", UInt32),
        ("ServerName", win32more.Foundation.PWSTR),
        ("ShareName", win32more.Foundation.PWSTR),
        ("TargetPriority", win32more.Storage.DistributedFileSystem.DFS_TARGET_PRIORITY),
    ]
    return DFS_STORAGE_INFO_1
def _define_DFS_INFO_3_head():
    class DFS_INFO_3(Structure):
        pass
    return DFS_INFO_3
def _define_DFS_INFO_3():
    DFS_INFO_3 = win32more.Storage.DistributedFileSystem.DFS_INFO_3_head
    DFS_INFO_3._fields_ = [
        ("EntryPath", win32more.Foundation.PWSTR),
        ("Comment", win32more.Foundation.PWSTR),
        ("State", UInt32),
        ("NumberOfStorages", UInt32),
        ("Storage", POINTER(win32more.Storage.DistributedFileSystem.DFS_STORAGE_INFO_head)),
    ]
    return DFS_INFO_3
def _define_DFS_INFO_3_32_head():
    class DFS_INFO_3_32(Structure):
        pass
    return DFS_INFO_3_32
def _define_DFS_INFO_3_32():
    DFS_INFO_3_32 = win32more.Storage.DistributedFileSystem.DFS_INFO_3_32_head
    DFS_INFO_3_32._fields_ = [
        ("EntryPath", UInt32),
        ("Comment", UInt32),
        ("State", UInt32),
        ("NumberOfStorages", UInt32),
        ("Storage", UInt32),
    ]
    return DFS_INFO_3_32
def _define_DFS_INFO_4_head():
    class DFS_INFO_4(Structure):
        pass
    return DFS_INFO_4
def _define_DFS_INFO_4():
    DFS_INFO_4 = win32more.Storage.DistributedFileSystem.DFS_INFO_4_head
    DFS_INFO_4._fields_ = [
        ("EntryPath", win32more.Foundation.PWSTR),
        ("Comment", win32more.Foundation.PWSTR),
        ("State", UInt32),
        ("Timeout", UInt32),
        ("Guid", Guid),
        ("NumberOfStorages", UInt32),
        ("Storage", POINTER(win32more.Storage.DistributedFileSystem.DFS_STORAGE_INFO_head)),
    ]
    return DFS_INFO_4
def _define_DFS_INFO_4_32_head():
    class DFS_INFO_4_32(Structure):
        pass
    return DFS_INFO_4_32
def _define_DFS_INFO_4_32():
    DFS_INFO_4_32 = win32more.Storage.DistributedFileSystem.DFS_INFO_4_32_head
    DFS_INFO_4_32._fields_ = [
        ("EntryPath", UInt32),
        ("Comment", UInt32),
        ("State", UInt32),
        ("Timeout", UInt32),
        ("Guid", Guid),
        ("NumberOfStorages", UInt32),
        ("Storage", UInt32),
    ]
    return DFS_INFO_4_32
def _define_DFS_INFO_5_head():
    class DFS_INFO_5(Structure):
        pass
    return DFS_INFO_5
def _define_DFS_INFO_5():
    DFS_INFO_5 = win32more.Storage.DistributedFileSystem.DFS_INFO_5_head
    DFS_INFO_5._fields_ = [
        ("EntryPath", win32more.Foundation.PWSTR),
        ("Comment", win32more.Foundation.PWSTR),
        ("State", UInt32),
        ("Timeout", UInt32),
        ("Guid", Guid),
        ("PropertyFlags", UInt32),
        ("MetadataSize", UInt32),
        ("NumberOfStorages", UInt32),
    ]
    return DFS_INFO_5
def _define_DFS_INFO_6_head():
    class DFS_INFO_6(Structure):
        pass
    return DFS_INFO_6
def _define_DFS_INFO_6():
    DFS_INFO_6 = win32more.Storage.DistributedFileSystem.DFS_INFO_6_head
    DFS_INFO_6._fields_ = [
        ("EntryPath", win32more.Foundation.PWSTR),
        ("Comment", win32more.Foundation.PWSTR),
        ("State", UInt32),
        ("Timeout", UInt32),
        ("Guid", Guid),
        ("PropertyFlags", UInt32),
        ("MetadataSize", UInt32),
        ("NumberOfStorages", UInt32),
        ("Storage", POINTER(win32more.Storage.DistributedFileSystem.DFS_STORAGE_INFO_1_head)),
    ]
    return DFS_INFO_6
def _define_DFS_INFO_7_head():
    class DFS_INFO_7(Structure):
        pass
    return DFS_INFO_7
def _define_DFS_INFO_7():
    DFS_INFO_7 = win32more.Storage.DistributedFileSystem.DFS_INFO_7_head
    DFS_INFO_7._fields_ = [
        ("GenerationGuid", Guid),
    ]
    return DFS_INFO_7
def _define_DFS_INFO_8_head():
    class DFS_INFO_8(Structure):
        pass
    return DFS_INFO_8
def _define_DFS_INFO_8():
    DFS_INFO_8 = win32more.Storage.DistributedFileSystem.DFS_INFO_8_head
    DFS_INFO_8._fields_ = [
        ("EntryPath", win32more.Foundation.PWSTR),
        ("Comment", win32more.Foundation.PWSTR),
        ("State", UInt32),
        ("Timeout", UInt32),
        ("Guid", Guid),
        ("PropertyFlags", UInt32),
        ("MetadataSize", UInt32),
        ("SdLengthReserved", UInt32),
        ("pSecurityDescriptor", POINTER(win32more.Security.SECURITY_DESCRIPTOR_head)),
        ("NumberOfStorages", UInt32),
    ]
    return DFS_INFO_8
def _define_DFS_INFO_9_head():
    class DFS_INFO_9(Structure):
        pass
    return DFS_INFO_9
def _define_DFS_INFO_9():
    DFS_INFO_9 = win32more.Storage.DistributedFileSystem.DFS_INFO_9_head
    DFS_INFO_9._fields_ = [
        ("EntryPath", win32more.Foundation.PWSTR),
        ("Comment", win32more.Foundation.PWSTR),
        ("State", UInt32),
        ("Timeout", UInt32),
        ("Guid", Guid),
        ("PropertyFlags", UInt32),
        ("MetadataSize", UInt32),
        ("SdLengthReserved", UInt32),
        ("pSecurityDescriptor", POINTER(win32more.Security.SECURITY_DESCRIPTOR_head)),
        ("NumberOfStorages", UInt32),
        ("Storage", POINTER(win32more.Storage.DistributedFileSystem.DFS_STORAGE_INFO_1_head)),
    ]
    return DFS_INFO_9
def _define_DFS_INFO_50_head():
    class DFS_INFO_50(Structure):
        pass
    return DFS_INFO_50
def _define_DFS_INFO_50():
    DFS_INFO_50 = win32more.Storage.DistributedFileSystem.DFS_INFO_50_head
    DFS_INFO_50._fields_ = [
        ("NamespaceMajorVersion", UInt32),
        ("NamespaceMinorVersion", UInt32),
        ("NamespaceCapabilities", UInt64),
    ]
    return DFS_INFO_50
def _define_DFS_INFO_100_head():
    class DFS_INFO_100(Structure):
        pass
    return DFS_INFO_100
def _define_DFS_INFO_100():
    DFS_INFO_100 = win32more.Storage.DistributedFileSystem.DFS_INFO_100_head
    DFS_INFO_100._fields_ = [
        ("Comment", win32more.Foundation.PWSTR),
    ]
    return DFS_INFO_100
def _define_DFS_INFO_101_head():
    class DFS_INFO_101(Structure):
        pass
    return DFS_INFO_101
def _define_DFS_INFO_101():
    DFS_INFO_101 = win32more.Storage.DistributedFileSystem.DFS_INFO_101_head
    DFS_INFO_101._fields_ = [
        ("State", UInt32),
    ]
    return DFS_INFO_101
def _define_DFS_INFO_102_head():
    class DFS_INFO_102(Structure):
        pass
    return DFS_INFO_102
def _define_DFS_INFO_102():
    DFS_INFO_102 = win32more.Storage.DistributedFileSystem.DFS_INFO_102_head
    DFS_INFO_102._fields_ = [
        ("Timeout", UInt32),
    ]
    return DFS_INFO_102
def _define_DFS_INFO_103_head():
    class DFS_INFO_103(Structure):
        pass
    return DFS_INFO_103
def _define_DFS_INFO_103():
    DFS_INFO_103 = win32more.Storage.DistributedFileSystem.DFS_INFO_103_head
    DFS_INFO_103._fields_ = [
        ("PropertyFlagMask", UInt32),
        ("PropertyFlags", UInt32),
    ]
    return DFS_INFO_103
def _define_DFS_INFO_104_head():
    class DFS_INFO_104(Structure):
        pass
    return DFS_INFO_104
def _define_DFS_INFO_104():
    DFS_INFO_104 = win32more.Storage.DistributedFileSystem.DFS_INFO_104_head
    DFS_INFO_104._fields_ = [
        ("TargetPriority", win32more.Storage.DistributedFileSystem.DFS_TARGET_PRIORITY),
    ]
    return DFS_INFO_104
def _define_DFS_INFO_105_head():
    class DFS_INFO_105(Structure):
        pass
    return DFS_INFO_105
def _define_DFS_INFO_105():
    DFS_INFO_105 = win32more.Storage.DistributedFileSystem.DFS_INFO_105_head
    DFS_INFO_105._fields_ = [
        ("Comment", win32more.Foundation.PWSTR),
        ("State", UInt32),
        ("Timeout", UInt32),
        ("PropertyFlagMask", UInt32),
        ("PropertyFlags", UInt32),
    ]
    return DFS_INFO_105
def _define_DFS_INFO_106_head():
    class DFS_INFO_106(Structure):
        pass
    return DFS_INFO_106
def _define_DFS_INFO_106():
    DFS_INFO_106 = win32more.Storage.DistributedFileSystem.DFS_INFO_106_head
    DFS_INFO_106._fields_ = [
        ("State", UInt32),
        ("TargetPriority", win32more.Storage.DistributedFileSystem.DFS_TARGET_PRIORITY),
    ]
    return DFS_INFO_106
def _define_DFS_INFO_107_head():
    class DFS_INFO_107(Structure):
        pass
    return DFS_INFO_107
def _define_DFS_INFO_107():
    DFS_INFO_107 = win32more.Storage.DistributedFileSystem.DFS_INFO_107_head
    DFS_INFO_107._fields_ = [
        ("Comment", win32more.Foundation.PWSTR),
        ("State", UInt32),
        ("Timeout", UInt32),
        ("PropertyFlagMask", UInt32),
        ("PropertyFlags", UInt32),
        ("SdLengthReserved", UInt32),
        ("pSecurityDescriptor", POINTER(win32more.Security.SECURITY_DESCRIPTOR_head)),
    ]
    return DFS_INFO_107
def _define_DFS_INFO_150_head():
    class DFS_INFO_150(Structure):
        pass
    return DFS_INFO_150
def _define_DFS_INFO_150():
    DFS_INFO_150 = win32more.Storage.DistributedFileSystem.DFS_INFO_150_head
    DFS_INFO_150._fields_ = [
        ("SdLengthReserved", UInt32),
        ("pSecurityDescriptor", POINTER(win32more.Security.SECURITY_DESCRIPTOR_head)),
    ]
    return DFS_INFO_150
def _define_DFS_INFO_200_head():
    class DFS_INFO_200(Structure):
        pass
    return DFS_INFO_200
def _define_DFS_INFO_200():
    DFS_INFO_200 = win32more.Storage.DistributedFileSystem.DFS_INFO_200_head
    DFS_INFO_200._fields_ = [
        ("FtDfsName", win32more.Foundation.PWSTR),
    ]
    return DFS_INFO_200
def _define_DFS_INFO_300_head():
    class DFS_INFO_300(Structure):
        pass
    return DFS_INFO_300
def _define_DFS_INFO_300():
    DFS_INFO_300 = win32more.Storage.DistributedFileSystem.DFS_INFO_300_head
    DFS_INFO_300._fields_ = [
        ("Flags", UInt32),
        ("DfsName", win32more.Foundation.PWSTR),
    ]
    return DFS_INFO_300
def _define_DFS_SITENAME_INFO_head():
    class DFS_SITENAME_INFO(Structure):
        pass
    return DFS_SITENAME_INFO
def _define_DFS_SITENAME_INFO():
    DFS_SITENAME_INFO = win32more.Storage.DistributedFileSystem.DFS_SITENAME_INFO_head
    DFS_SITENAME_INFO._fields_ = [
        ("SiteFlags", UInt32),
        ("SiteName", win32more.Foundation.PWSTR),
    ]
    return DFS_SITENAME_INFO
def _define_DFS_SITELIST_INFO_head():
    class DFS_SITELIST_INFO(Structure):
        pass
    return DFS_SITELIST_INFO
def _define_DFS_SITELIST_INFO():
    DFS_SITELIST_INFO = win32more.Storage.DistributedFileSystem.DFS_SITELIST_INFO_head
    DFS_SITELIST_INFO._fields_ = [
        ("cSites", UInt32),
        ("Site", win32more.Storage.DistributedFileSystem.DFS_SITENAME_INFO * 0),
    ]
    return DFS_SITELIST_INFO
DFS_NAMESPACE_VERSION_ORIGIN = Int32
DFS_NAMESPACE_VERSION_ORIGIN_COMBINED = 0
DFS_NAMESPACE_VERSION_ORIGIN_SERVER = 1
DFS_NAMESPACE_VERSION_ORIGIN_DOMAIN = 2
def _define_DFS_SUPPORTED_NAMESPACE_VERSION_INFO_head():
    class DFS_SUPPORTED_NAMESPACE_VERSION_INFO(Structure):
        pass
    return DFS_SUPPORTED_NAMESPACE_VERSION_INFO
def _define_DFS_SUPPORTED_NAMESPACE_VERSION_INFO():
    DFS_SUPPORTED_NAMESPACE_VERSION_INFO = win32more.Storage.DistributedFileSystem.DFS_SUPPORTED_NAMESPACE_VERSION_INFO_head
    DFS_SUPPORTED_NAMESPACE_VERSION_INFO._fields_ = [
        ("DomainDfsMajorVersion", UInt32),
        ("DomainDfsMinorVersion", UInt32),
        ("DomainDfsCapabilities", UInt64),
        ("StandaloneDfsMajorVersion", UInt32),
        ("StandaloneDfsMinorVersion", UInt32),
        ("StandaloneDfsCapabilities", UInt64),
    ]
    return DFS_SUPPORTED_NAMESPACE_VERSION_INFO
def _define_DFS_GET_PKT_ENTRY_STATE_ARG_head():
    class DFS_GET_PKT_ENTRY_STATE_ARG(Structure):
        pass
    return DFS_GET_PKT_ENTRY_STATE_ARG
def _define_DFS_GET_PKT_ENTRY_STATE_ARG():
    DFS_GET_PKT_ENTRY_STATE_ARG = win32more.Storage.DistributedFileSystem.DFS_GET_PKT_ENTRY_STATE_ARG_head
    DFS_GET_PKT_ENTRY_STATE_ARG._fields_ = [
        ("DfsEntryPathLen", UInt16),
        ("ServerNameLen", UInt16),
        ("ShareNameLen", UInt16),
        ("Level", UInt32),
        ("Buffer", Char * 0),
    ]
    return DFS_GET_PKT_ENTRY_STATE_ARG
def _define_NetDfsAdd():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(("NetDfsAdd", windll["NETAPI32"]), ((1, 'DfsEntryPath'),(1, 'ServerName'),(1, 'ShareName'),(1, 'Comment'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetDfsAddStdRoot():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(("NetDfsAddStdRoot", windll["NETAPI32"]), ((1, 'ServerName'),(1, 'RootShare'),(1, 'Comment'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetDfsRemoveStdRoot():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(("NetDfsRemoveStdRoot", windll["NETAPI32"]), ((1, 'ServerName'),(1, 'RootShare'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetDfsAddFtRoot():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(("NetDfsAddFtRoot", windll["NETAPI32"]), ((1, 'ServerName'),(1, 'RootShare'),(1, 'FtDfsName'),(1, 'Comment'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetDfsRemoveFtRoot():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(("NetDfsRemoveFtRoot", windll["NETAPI32"]), ((1, 'ServerName'),(1, 'RootShare'),(1, 'FtDfsName'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetDfsRemoveFtRootForced():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(("NetDfsRemoveFtRootForced", windll["NETAPI32"]), ((1, 'DomainName'),(1, 'ServerName'),(1, 'RootShare'),(1, 'FtDfsName'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetDfsRemove():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("NetDfsRemove", windll["NETAPI32"]), ((1, 'DfsEntryPath'),(1, 'ServerName'),(1, 'ShareName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetDfsEnum():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(c_char_p_no),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("NetDfsEnum", windll["NETAPI32"]), ((1, 'DfsName'),(1, 'Level'),(1, 'PrefMaxLen'),(1, 'Buffer'),(1, 'EntriesRead'),(1, 'ResumeHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetDfsGetInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(c_char_p_no), use_last_error=False)(("NetDfsGetInfo", windll["NETAPI32"]), ((1, 'DfsEntryPath'),(1, 'ServerName'),(1, 'ShareName'),(1, 'Level'),(1, 'Buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetDfsSetInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,c_char_p_no, use_last_error=False)(("NetDfsSetInfo", windll["NETAPI32"]), ((1, 'DfsEntryPath'),(1, 'ServerName'),(1, 'ShareName'),(1, 'Level'),(1, 'Buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetDfsGetClientInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(c_char_p_no), use_last_error=False)(("NetDfsGetClientInfo", windll["NETAPI32"]), ((1, 'DfsEntryPath'),(1, 'ServerName'),(1, 'ShareName'),(1, 'Level'),(1, 'Buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetDfsSetClientInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,c_char_p_no, use_last_error=False)(("NetDfsSetClientInfo", windll["NETAPI32"]), ((1, 'DfsEntryPath'),(1, 'ServerName'),(1, 'ShareName'),(1, 'Level'),(1, 'Buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetDfsMove():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(("NetDfsMove", windll["NETAPI32"]), ((1, 'OldDfsEntryPath'),(1, 'NewDfsEntryPath'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetDfsAddRootTarget():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(("NetDfsAddRootTarget", windll["NETAPI32"]), ((1, 'pDfsPath'),(1, 'pTargetPath'),(1, 'MajorVersion'),(1, 'pComment'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetDfsRemoveRootTarget():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(("NetDfsRemoveRootTarget", windll["NETAPI32"]), ((1, 'pDfsPath'),(1, 'pTargetPath'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetDfsGetSecurity():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(POINTER(win32more.Security.SECURITY_DESCRIPTOR_head)),POINTER(UInt32), use_last_error=False)(("NetDfsGetSecurity", windll["NETAPI32"]), ((1, 'DfsEntryPath'),(1, 'SecurityInformation'),(1, 'ppSecurityDescriptor'),(1, 'lpcbSecurityDescriptor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetDfsSetSecurity():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head), use_last_error=False)(("NetDfsSetSecurity", windll["NETAPI32"]), ((1, 'DfsEntryPath'),(1, 'SecurityInformation'),(1, 'pSecurityDescriptor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetDfsGetStdContainerSecurity():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(POINTER(win32more.Security.SECURITY_DESCRIPTOR_head)),POINTER(UInt32), use_last_error=False)(("NetDfsGetStdContainerSecurity", windll["NETAPI32"]), ((1, 'MachineName'),(1, 'SecurityInformation'),(1, 'ppSecurityDescriptor'),(1, 'lpcbSecurityDescriptor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetDfsSetStdContainerSecurity():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head), use_last_error=False)(("NetDfsSetStdContainerSecurity", windll["NETAPI32"]), ((1, 'MachineName'),(1, 'SecurityInformation'),(1, 'pSecurityDescriptor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetDfsGetFtContainerSecurity():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(POINTER(win32more.Security.SECURITY_DESCRIPTOR_head)),POINTER(UInt32), use_last_error=False)(("NetDfsGetFtContainerSecurity", windll["NETAPI32"]), ((1, 'DomainName'),(1, 'SecurityInformation'),(1, 'ppSecurityDescriptor'),(1, 'lpcbSecurityDescriptor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetDfsSetFtContainerSecurity():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head), use_last_error=False)(("NetDfsSetFtContainerSecurity", windll["NETAPI32"]), ((1, 'DomainName'),(1, 'SecurityInformation'),(1, 'pSecurityDescriptor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetDfsGetSupportedNamespaceVersion():
    try:
        return WINFUNCTYPE(UInt32,win32more.Storage.DistributedFileSystem.DFS_NAMESPACE_VERSION_ORIGIN,win32more.Foundation.PWSTR,POINTER(POINTER(win32more.Storage.DistributedFileSystem.DFS_SUPPORTED_NAMESPACE_VERSION_INFO_head)), use_last_error=False)(("NetDfsGetSupportedNamespaceVersion", windll["NETAPI32"]), ((1, 'Origin'),(1, 'pName'),(1, 'ppVersionInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "FSCTL_DFS_BASE",
    "DFS_VOLUME_STATES",
    "DFS_VOLUME_STATE_OK",
    "DFS_VOLUME_STATE_INCONSISTENT",
    "DFS_VOLUME_STATE_OFFLINE",
    "DFS_VOLUME_STATE_ONLINE",
    "DFS_VOLUME_STATE_RESYNCHRONIZE",
    "DFS_VOLUME_STATE_STANDBY",
    "DFS_VOLUME_STATE_FORCE_SYNC",
    "DFS_VOLUME_FLAVORS",
    "DFS_VOLUME_FLAVOR_UNUSED1",
    "DFS_VOLUME_FLAVOR_STANDALONE",
    "DFS_VOLUME_FLAVOR_AD_BLOB",
    "DFS_STORAGE_FLAVOR_UNUSED2",
    "DFS_STORAGE_STATES",
    "DFS_STORAGE_STATE_OFFLINE",
    "DFS_STORAGE_STATE_ONLINE",
    "DFS_STORAGE_STATE_ACTIVE",
    "DFS_PROPERTY_FLAG_INSITE_REFERRALS",
    "DFS_PROPERTY_FLAG_ROOT_SCALABILITY",
    "DFS_PROPERTY_FLAG_SITE_COSTING",
    "DFS_PROPERTY_FLAG_TARGET_FAILBACK",
    "DFS_PROPERTY_FLAG_CLUSTER_ENABLED",
    "DFS_PROPERTY_FLAG_ABDE",
    "DFS_ADD_VOLUME",
    "DFS_RESTORE_VOLUME",
    "NET_DFS_SETDC_FLAGS",
    "NET_DFS_SETDC_TIMEOUT",
    "NET_DFS_SETDC_INITPKT",
    "DFS_SITE_PRIMARY",
    "DFS_MOVE_FLAG_REPLACE_IF_EXISTS",
    "DFS_FORCE_REMOVE",
    "FSCTL_DFS_GET_PKT_ENTRY_STATE",
    "DFS_TARGET_PRIORITY_CLASS",
    "DFS_TARGET_PRIORITY_CLASS_DfsInvalidPriorityClass",
    "DFS_TARGET_PRIORITY_CLASS_DfsSiteCostNormalPriorityClass",
    "DFS_TARGET_PRIORITY_CLASS_DfsGlobalHighPriorityClass",
    "DFS_TARGET_PRIORITY_CLASS_DfsSiteCostHighPriorityClass",
    "DFS_TARGET_PRIORITY_CLASS_DfsSiteCostLowPriorityClass",
    "DFS_TARGET_PRIORITY_CLASS_DfsGlobalLowPriorityClass",
    "DFS_TARGET_PRIORITY",
    "DFS_INFO_1",
    "DFS_INFO_1_32",
    "DFS_INFO_2",
    "DFS_INFO_2_32",
    "DFS_STORAGE_INFO",
    "DFS_STORAGE_INFO_0_32",
    "DFS_STORAGE_INFO_1",
    "DFS_INFO_3",
    "DFS_INFO_3_32",
    "DFS_INFO_4",
    "DFS_INFO_4_32",
    "DFS_INFO_5",
    "DFS_INFO_6",
    "DFS_INFO_7",
    "DFS_INFO_8",
    "DFS_INFO_9",
    "DFS_INFO_50",
    "DFS_INFO_100",
    "DFS_INFO_101",
    "DFS_INFO_102",
    "DFS_INFO_103",
    "DFS_INFO_104",
    "DFS_INFO_105",
    "DFS_INFO_106",
    "DFS_INFO_107",
    "DFS_INFO_150",
    "DFS_INFO_200",
    "DFS_INFO_300",
    "DFS_SITENAME_INFO",
    "DFS_SITELIST_INFO",
    "DFS_NAMESPACE_VERSION_ORIGIN",
    "DFS_NAMESPACE_VERSION_ORIGIN_COMBINED",
    "DFS_NAMESPACE_VERSION_ORIGIN_SERVER",
    "DFS_NAMESPACE_VERSION_ORIGIN_DOMAIN",
    "DFS_SUPPORTED_NAMESPACE_VERSION_INFO",
    "DFS_GET_PKT_ENTRY_STATE_ARG",
    "NetDfsAdd",
    "NetDfsAddStdRoot",
    "NetDfsRemoveStdRoot",
    "NetDfsAddFtRoot",
    "NetDfsRemoveFtRoot",
    "NetDfsRemoveFtRootForced",
    "NetDfsRemove",
    "NetDfsEnum",
    "NetDfsGetInfo",
    "NetDfsSetInfo",
    "NetDfsGetClientInfo",
    "NetDfsSetClientInfo",
    "NetDfsMove",
    "NetDfsAddRootTarget",
    "NetDfsRemoveRootTarget",
    "NetDfsGetSecurity",
    "NetDfsSetSecurity",
    "NetDfsGetStdContainerSecurity",
    "NetDfsSetStdContainerSecurity",
    "NetDfsGetFtContainerSecurity",
    "NetDfsSetFtContainerSecurity",
    "NetDfsGetSupportedNamespaceVersion",
]
