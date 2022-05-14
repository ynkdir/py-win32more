from win32more import *
import win32more.Storage.Vhd
import win32more.Foundation
import win32more.Security
import win32more.System.IO

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.Storage.Vhd, name, eval(f"_define_{name}()"))
    return getattr(win32more.Storage.Vhd, name)
VIRTUAL_STORAGE_TYPE_VENDOR_UNKNOWN = '00000000-0000-0000-0000-000000000000'
VIRTUAL_STORAGE_TYPE_VENDOR_MICROSOFT = 'ec984aec-a0f9-47e9-901f-71415a66345b'
VIRTUAL_STORAGE_TYPE_DEVICE_UNKNOWN = 0
VIRTUAL_STORAGE_TYPE_DEVICE_ISO = 1
VIRTUAL_STORAGE_TYPE_DEVICE_VHD = 2
VIRTUAL_STORAGE_TYPE_DEVICE_VHDX = 3
VIRTUAL_STORAGE_TYPE_DEVICE_VHDSET = 4
OPEN_VIRTUAL_DISK_RW_DEPTH_DEFAULT = 1
CREATE_VIRTUAL_DISK_PARAMETERS_DEFAULT_BLOCK_SIZE = 0
CREATE_VIRTUAL_DISK_PARAMETERS_DEFAULT_SECTOR_SIZE = 0
VIRTUAL_DISK_MAXIMUM_CHANGE_TRACKING_ID_LENGTH = 256
MERGE_VIRTUAL_DISK_DEFAULT_MERGE_DEPTH = 1
def _define_VIRTUAL_STORAGE_TYPE_head():
    class VIRTUAL_STORAGE_TYPE(Structure):
        pass
    return VIRTUAL_STORAGE_TYPE
def _define_VIRTUAL_STORAGE_TYPE():
    VIRTUAL_STORAGE_TYPE = win32more.Storage.Vhd.VIRTUAL_STORAGE_TYPE_head
    VIRTUAL_STORAGE_TYPE._fields_ = [
        ("DeviceId", UInt32),
        ("VendorId", Guid),
    ]
    return VIRTUAL_STORAGE_TYPE
OPEN_VIRTUAL_DISK_VERSION = Int32
OPEN_VIRTUAL_DISK_VERSION_UNSPECIFIED = 0
OPEN_VIRTUAL_DISK_VERSION_1 = 1
OPEN_VIRTUAL_DISK_VERSION_2 = 2
OPEN_VIRTUAL_DISK_VERSION_3 = 3
def _define_OPEN_VIRTUAL_DISK_PARAMETERS_head():
    class OPEN_VIRTUAL_DISK_PARAMETERS(Structure):
        pass
    return OPEN_VIRTUAL_DISK_PARAMETERS
def _define_OPEN_VIRTUAL_DISK_PARAMETERS():
    OPEN_VIRTUAL_DISK_PARAMETERS = win32more.Storage.Vhd.OPEN_VIRTUAL_DISK_PARAMETERS_head
    class OPEN_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union(Union):
        pass
    class OPEN_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version3_e__Struct(Structure):
        pass
    OPEN_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version3_e__Struct._fields_ = [
        ("GetInfoOnly", win32more.Foundation.BOOL),
        ("ReadOnly", win32more.Foundation.BOOL),
        ("ResiliencyGuid", Guid),
        ("SnapshotId", Guid),
    ]
    class OPEN_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version1_e__Struct(Structure):
        pass
    OPEN_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version1_e__Struct._fields_ = [
        ("RWDepth", UInt32),
    ]
    class OPEN_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version2_e__Struct(Structure):
        pass
    OPEN_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version2_e__Struct._fields_ = [
        ("GetInfoOnly", win32more.Foundation.BOOL),
        ("ReadOnly", win32more.Foundation.BOOL),
        ("ResiliencyGuid", Guid),
    ]
    OPEN_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union._fields_ = [
        ("Version1", OPEN_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version1_e__Struct),
        ("Version2", OPEN_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version2_e__Struct),
        ("Version3", OPEN_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version3_e__Struct),
    ]
    OPEN_VIRTUAL_DISK_PARAMETERS._anonymous_ = [
        'Anonymous',
    ]
    OPEN_VIRTUAL_DISK_PARAMETERS._fields_ = [
        ("Version", win32more.Storage.Vhd.OPEN_VIRTUAL_DISK_VERSION),
        ("Anonymous", OPEN_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union),
    ]
    return OPEN_VIRTUAL_DISK_PARAMETERS
VIRTUAL_DISK_ACCESS_MASK = UInt32
VIRTUAL_DISK_ACCESS_NONE = 0
VIRTUAL_DISK_ACCESS_ATTACH_RO = 65536
VIRTUAL_DISK_ACCESS_ATTACH_RW = 131072
VIRTUAL_DISK_ACCESS_DETACH = 262144
VIRTUAL_DISK_ACCESS_GET_INFO = 524288
VIRTUAL_DISK_ACCESS_CREATE = 1048576
VIRTUAL_DISK_ACCESS_METAOPS = 2097152
VIRTUAL_DISK_ACCESS_READ = 851968
VIRTUAL_DISK_ACCESS_ALL = 4128768
VIRTUAL_DISK_ACCESS_WRITABLE = 3276800
OPEN_VIRTUAL_DISK_FLAG = UInt32
OPEN_VIRTUAL_DISK_FLAG_NONE = 0
OPEN_VIRTUAL_DISK_FLAG_NO_PARENTS = 1
OPEN_VIRTUAL_DISK_FLAG_BLANK_FILE = 2
OPEN_VIRTUAL_DISK_FLAG_BOOT_DRIVE = 4
OPEN_VIRTUAL_DISK_FLAG_CACHED_IO = 8
OPEN_VIRTUAL_DISK_FLAG_CUSTOM_DIFF_CHAIN = 16
OPEN_VIRTUAL_DISK_FLAG_PARENT_CACHED_IO = 32
OPEN_VIRTUAL_DISK_FLAG_VHDSET_FILE_ONLY = 64
OPEN_VIRTUAL_DISK_FLAG_IGNORE_RELATIVE_PARENT_LOCATOR = 128
OPEN_VIRTUAL_DISK_FLAG_NO_WRITE_HARDENING = 256
OPEN_VIRTUAL_DISK_FLAG_SUPPORT_COMPRESSED_VOLUMES = 512
OPEN_VIRTUAL_DISK_FLAG_SUPPORT_SPARSE_FILES_ANY_FS = 1024
OPEN_VIRTUAL_DISK_FLAG_SUPPORT_ENCRYPTED_FILES = 2048
CREATE_VIRTUAL_DISK_VERSION = Int32
CREATE_VIRTUAL_DISK_VERSION_UNSPECIFIED = 0
CREATE_VIRTUAL_DISK_VERSION_1 = 1
CREATE_VIRTUAL_DISK_VERSION_2 = 2
CREATE_VIRTUAL_DISK_VERSION_3 = 3
CREATE_VIRTUAL_DISK_VERSION_4 = 4
def _define_CREATE_VIRTUAL_DISK_PARAMETERS_head():
    class CREATE_VIRTUAL_DISK_PARAMETERS(Structure):
        pass
    return CREATE_VIRTUAL_DISK_PARAMETERS
def _define_CREATE_VIRTUAL_DISK_PARAMETERS():
    CREATE_VIRTUAL_DISK_PARAMETERS = win32more.Storage.Vhd.CREATE_VIRTUAL_DISK_PARAMETERS_head
    class CREATE_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union(Union):
        pass
    class CREATE_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version4_e__Struct(Structure):
        pass
    CREATE_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version4_e__Struct._fields_ = [
        ("UniqueId", Guid),
        ("MaximumSize", UInt64),
        ("BlockSizeInBytes", UInt32),
        ("SectorSizeInBytes", UInt32),
        ("PhysicalSectorSizeInBytes", UInt32),
        ("ParentPath", win32more.Foundation.PWSTR),
        ("SourcePath", win32more.Foundation.PWSTR),
        ("OpenFlags", win32more.Storage.Vhd.OPEN_VIRTUAL_DISK_FLAG),
        ("ParentVirtualStorageType", win32more.Storage.Vhd.VIRTUAL_STORAGE_TYPE),
        ("SourceVirtualStorageType", win32more.Storage.Vhd.VIRTUAL_STORAGE_TYPE),
        ("ResiliencyGuid", Guid),
        ("SourceLimitPath", win32more.Foundation.PWSTR),
        ("BackingStorageType", win32more.Storage.Vhd.VIRTUAL_STORAGE_TYPE),
        ("PmemAddressAbstractionType", Guid),
        ("DataAlignment", UInt64),
    ]
    class CREATE_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version2_e__Struct(Structure):
        pass
    CREATE_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version2_e__Struct._fields_ = [
        ("UniqueId", Guid),
        ("MaximumSize", UInt64),
        ("BlockSizeInBytes", UInt32),
        ("SectorSizeInBytes", UInt32),
        ("PhysicalSectorSizeInBytes", UInt32),
        ("ParentPath", win32more.Foundation.PWSTR),
        ("SourcePath", win32more.Foundation.PWSTR),
        ("OpenFlags", win32more.Storage.Vhd.OPEN_VIRTUAL_DISK_FLAG),
        ("ParentVirtualStorageType", win32more.Storage.Vhd.VIRTUAL_STORAGE_TYPE),
        ("SourceVirtualStorageType", win32more.Storage.Vhd.VIRTUAL_STORAGE_TYPE),
        ("ResiliencyGuid", Guid),
    ]
    class CREATE_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version3_e__Struct(Structure):
        pass
    CREATE_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version3_e__Struct._fields_ = [
        ("UniqueId", Guid),
        ("MaximumSize", UInt64),
        ("BlockSizeInBytes", UInt32),
        ("SectorSizeInBytes", UInt32),
        ("PhysicalSectorSizeInBytes", UInt32),
        ("ParentPath", win32more.Foundation.PWSTR),
        ("SourcePath", win32more.Foundation.PWSTR),
        ("OpenFlags", win32more.Storage.Vhd.OPEN_VIRTUAL_DISK_FLAG),
        ("ParentVirtualStorageType", win32more.Storage.Vhd.VIRTUAL_STORAGE_TYPE),
        ("SourceVirtualStorageType", win32more.Storage.Vhd.VIRTUAL_STORAGE_TYPE),
        ("ResiliencyGuid", Guid),
        ("SourceLimitPath", win32more.Foundation.PWSTR),
        ("BackingStorageType", win32more.Storage.Vhd.VIRTUAL_STORAGE_TYPE),
    ]
    class CREATE_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version1_e__Struct(Structure):
        pass
    CREATE_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version1_e__Struct._fields_ = [
        ("UniqueId", Guid),
        ("MaximumSize", UInt64),
        ("BlockSizeInBytes", UInt32),
        ("SectorSizeInBytes", UInt32),
        ("ParentPath", win32more.Foundation.PWSTR),
        ("SourcePath", win32more.Foundation.PWSTR),
    ]
    CREATE_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union._fields_ = [
        ("Version1", CREATE_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version1_e__Struct),
        ("Version2", CREATE_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version2_e__Struct),
        ("Version3", CREATE_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version3_e__Struct),
        ("Version4", CREATE_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version4_e__Struct),
    ]
    CREATE_VIRTUAL_DISK_PARAMETERS._anonymous_ = [
        'Anonymous',
    ]
    CREATE_VIRTUAL_DISK_PARAMETERS._fields_ = [
        ("Version", win32more.Storage.Vhd.CREATE_VIRTUAL_DISK_VERSION),
        ("Anonymous", CREATE_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union),
    ]
    return CREATE_VIRTUAL_DISK_PARAMETERS
CREATE_VIRTUAL_DISK_FLAG = UInt32
CREATE_VIRTUAL_DISK_FLAG_NONE = 0
CREATE_VIRTUAL_DISK_FLAG_FULL_PHYSICAL_ALLOCATION = 1
CREATE_VIRTUAL_DISK_FLAG_PREVENT_WRITES_TO_SOURCE_DISK = 2
CREATE_VIRTUAL_DISK_FLAG_DO_NOT_COPY_METADATA_FROM_PARENT = 4
CREATE_VIRTUAL_DISK_FLAG_CREATE_BACKING_STORAGE = 8
CREATE_VIRTUAL_DISK_FLAG_USE_CHANGE_TRACKING_SOURCE_LIMIT = 16
CREATE_VIRTUAL_DISK_FLAG_PRESERVE_PARENT_CHANGE_TRACKING_STATE = 32
CREATE_VIRTUAL_DISK_FLAG_VHD_SET_USE_ORIGINAL_BACKING_STORAGE = 64
CREATE_VIRTUAL_DISK_FLAG_SPARSE_FILE = 128
CREATE_VIRTUAL_DISK_FLAG_PMEM_COMPATIBLE = 256
CREATE_VIRTUAL_DISK_FLAG_SUPPORT_COMPRESSED_VOLUMES = 512
CREATE_VIRTUAL_DISK_FLAG_SUPPORT_SPARSE_FILES_ANY_FS = 1024
ATTACH_VIRTUAL_DISK_VERSION = Int32
ATTACH_VIRTUAL_DISK_VERSION_UNSPECIFIED = 0
ATTACH_VIRTUAL_DISK_VERSION_1 = 1
ATTACH_VIRTUAL_DISK_VERSION_2 = 2
def _define_ATTACH_VIRTUAL_DISK_PARAMETERS_head():
    class ATTACH_VIRTUAL_DISK_PARAMETERS(Structure):
        pass
    return ATTACH_VIRTUAL_DISK_PARAMETERS
def _define_ATTACH_VIRTUAL_DISK_PARAMETERS():
    ATTACH_VIRTUAL_DISK_PARAMETERS = win32more.Storage.Vhd.ATTACH_VIRTUAL_DISK_PARAMETERS_head
    class ATTACH_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union(Union):
        pass
    class ATTACH_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version2_e__Struct(Structure):
        pass
    ATTACH_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version2_e__Struct._fields_ = [
        ("RestrictedOffset", UInt64),
        ("RestrictedLength", UInt64),
    ]
    class ATTACH_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version1_e__Struct(Structure):
        pass
    ATTACH_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version1_e__Struct._fields_ = [
        ("Reserved", UInt32),
    ]
    ATTACH_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union._fields_ = [
        ("Version1", ATTACH_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version1_e__Struct),
        ("Version2", ATTACH_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version2_e__Struct),
    ]
    ATTACH_VIRTUAL_DISK_PARAMETERS._anonymous_ = [
        'Anonymous',
    ]
    ATTACH_VIRTUAL_DISK_PARAMETERS._fields_ = [
        ("Version", win32more.Storage.Vhd.ATTACH_VIRTUAL_DISK_VERSION),
        ("Anonymous", ATTACH_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union),
    ]
    return ATTACH_VIRTUAL_DISK_PARAMETERS
ATTACH_VIRTUAL_DISK_FLAG = UInt32
ATTACH_VIRTUAL_DISK_FLAG_NONE = 0
ATTACH_VIRTUAL_DISK_FLAG_READ_ONLY = 1
ATTACH_VIRTUAL_DISK_FLAG_NO_DRIVE_LETTER = 2
ATTACH_VIRTUAL_DISK_FLAG_PERMANENT_LIFETIME = 4
ATTACH_VIRTUAL_DISK_FLAG_NO_LOCAL_HOST = 8
ATTACH_VIRTUAL_DISK_FLAG_NO_SECURITY_DESCRIPTOR = 16
ATTACH_VIRTUAL_DISK_FLAG_BYPASS_DEFAULT_ENCRYPTION_POLICY = 32
ATTACH_VIRTUAL_DISK_FLAG_NON_PNP = 64
ATTACH_VIRTUAL_DISK_FLAG_RESTRICTED_RANGE = 128
ATTACH_VIRTUAL_DISK_FLAG_SINGLE_PARTITION = 256
ATTACH_VIRTUAL_DISK_FLAG_REGISTER_VOLUME = 512
DETACH_VIRTUAL_DISK_FLAG = UInt32
DETACH_VIRTUAL_DISK_FLAG_NONE = 0
DEPENDENT_DISK_FLAG = UInt32
DEPENDENT_DISK_FLAG_NONE = 0
DEPENDENT_DISK_FLAG_MULT_BACKING_FILES = 1
DEPENDENT_DISK_FLAG_FULLY_ALLOCATED = 2
DEPENDENT_DISK_FLAG_READ_ONLY = 4
DEPENDENT_DISK_FLAG_REMOTE = 8
DEPENDENT_DISK_FLAG_SYSTEM_VOLUME = 16
DEPENDENT_DISK_FLAG_SYSTEM_VOLUME_PARENT = 32
DEPENDENT_DISK_FLAG_REMOVABLE = 64
DEPENDENT_DISK_FLAG_NO_DRIVE_LETTER = 128
DEPENDENT_DISK_FLAG_PARENT = 256
DEPENDENT_DISK_FLAG_NO_HOST_DISK = 512
DEPENDENT_DISK_FLAG_PERMANENT_LIFETIME = 1024
DEPENDENT_DISK_FLAG_SUPPORT_COMPRESSED_VOLUMES = 2048
DEPENDENT_DISK_FLAG_ALWAYS_ALLOW_SPARSE = 4096
DEPENDENT_DISK_FLAG_SUPPORT_ENCRYPTED_FILES = 8192
STORAGE_DEPENDENCY_INFO_VERSION = Int32
STORAGE_DEPENDENCY_INFO_VERSION_UNSPECIFIED = 0
STORAGE_DEPENDENCY_INFO_VERSION_1 = 1
STORAGE_DEPENDENCY_INFO_VERSION_2 = 2
def _define_STORAGE_DEPENDENCY_INFO_TYPE_1_head():
    class STORAGE_DEPENDENCY_INFO_TYPE_1(Structure):
        pass
    return STORAGE_DEPENDENCY_INFO_TYPE_1
def _define_STORAGE_DEPENDENCY_INFO_TYPE_1():
    STORAGE_DEPENDENCY_INFO_TYPE_1 = win32more.Storage.Vhd.STORAGE_DEPENDENCY_INFO_TYPE_1_head
    STORAGE_DEPENDENCY_INFO_TYPE_1._fields_ = [
        ("DependencyTypeFlags", win32more.Storage.Vhd.DEPENDENT_DISK_FLAG),
        ("ProviderSpecificFlags", UInt32),
        ("VirtualStorageType", win32more.Storage.Vhd.VIRTUAL_STORAGE_TYPE),
    ]
    return STORAGE_DEPENDENCY_INFO_TYPE_1
def _define_STORAGE_DEPENDENCY_INFO_TYPE_2_head():
    class STORAGE_DEPENDENCY_INFO_TYPE_2(Structure):
        pass
    return STORAGE_DEPENDENCY_INFO_TYPE_2
def _define_STORAGE_DEPENDENCY_INFO_TYPE_2():
    STORAGE_DEPENDENCY_INFO_TYPE_2 = win32more.Storage.Vhd.STORAGE_DEPENDENCY_INFO_TYPE_2_head
    STORAGE_DEPENDENCY_INFO_TYPE_2._fields_ = [
        ("DependencyTypeFlags", win32more.Storage.Vhd.DEPENDENT_DISK_FLAG),
        ("ProviderSpecificFlags", UInt32),
        ("VirtualStorageType", win32more.Storage.Vhd.VIRTUAL_STORAGE_TYPE),
        ("AncestorLevel", UInt32),
        ("DependencyDeviceName", win32more.Foundation.PWSTR),
        ("HostVolumeName", win32more.Foundation.PWSTR),
        ("DependentVolumeName", win32more.Foundation.PWSTR),
        ("DependentVolumeRelativePath", win32more.Foundation.PWSTR),
    ]
    return STORAGE_DEPENDENCY_INFO_TYPE_2
def _define_STORAGE_DEPENDENCY_INFO_head():
    class STORAGE_DEPENDENCY_INFO(Structure):
        pass
    return STORAGE_DEPENDENCY_INFO
def _define_STORAGE_DEPENDENCY_INFO():
    STORAGE_DEPENDENCY_INFO = win32more.Storage.Vhd.STORAGE_DEPENDENCY_INFO_head
    class STORAGE_DEPENDENCY_INFO__Anonymous_e__Union(Union):
        pass
    STORAGE_DEPENDENCY_INFO__Anonymous_e__Union._fields_ = [
        ("Version1Entries", win32more.Storage.Vhd.STORAGE_DEPENDENCY_INFO_TYPE_1 * 0),
        ("Version2Entries", win32more.Storage.Vhd.STORAGE_DEPENDENCY_INFO_TYPE_2 * 0),
    ]
    STORAGE_DEPENDENCY_INFO._anonymous_ = [
        'Anonymous',
    ]
    STORAGE_DEPENDENCY_INFO._fields_ = [
        ("Version", win32more.Storage.Vhd.STORAGE_DEPENDENCY_INFO_VERSION),
        ("NumberEntries", UInt32),
        ("Anonymous", STORAGE_DEPENDENCY_INFO__Anonymous_e__Union),
    ]
    return STORAGE_DEPENDENCY_INFO
GET_STORAGE_DEPENDENCY_FLAG = UInt32
GET_STORAGE_DEPENDENCY_FLAG_NONE = 0
GET_STORAGE_DEPENDENCY_FLAG_HOST_VOLUMES = 1
GET_STORAGE_DEPENDENCY_FLAG_DISK_HANDLE = 2
GET_VIRTUAL_DISK_INFO_VERSION = Int32
GET_VIRTUAL_DISK_INFO_UNSPECIFIED = 0
GET_VIRTUAL_DISK_INFO_SIZE = 1
GET_VIRTUAL_DISK_INFO_IDENTIFIER = 2
GET_VIRTUAL_DISK_INFO_PARENT_LOCATION = 3
GET_VIRTUAL_DISK_INFO_PARENT_IDENTIFIER = 4
GET_VIRTUAL_DISK_INFO_PARENT_TIMESTAMP = 5
GET_VIRTUAL_DISK_INFO_VIRTUAL_STORAGE_TYPE = 6
GET_VIRTUAL_DISK_INFO_PROVIDER_SUBTYPE = 7
GET_VIRTUAL_DISK_INFO_IS_4K_ALIGNED = 8
GET_VIRTUAL_DISK_INFO_PHYSICAL_DISK = 9
GET_VIRTUAL_DISK_INFO_VHD_PHYSICAL_SECTOR_SIZE = 10
GET_VIRTUAL_DISK_INFO_SMALLEST_SAFE_VIRTUAL_SIZE = 11
GET_VIRTUAL_DISK_INFO_FRAGMENTATION = 12
GET_VIRTUAL_DISK_INFO_IS_LOADED = 13
GET_VIRTUAL_DISK_INFO_VIRTUAL_DISK_ID = 14
GET_VIRTUAL_DISK_INFO_CHANGE_TRACKING_STATE = 15
def _define_GET_VIRTUAL_DISK_INFO_head():
    class GET_VIRTUAL_DISK_INFO(Structure):
        pass
    return GET_VIRTUAL_DISK_INFO
def _define_GET_VIRTUAL_DISK_INFO():
    GET_VIRTUAL_DISK_INFO = win32more.Storage.Vhd.GET_VIRTUAL_DISK_INFO_head
    class GET_VIRTUAL_DISK_INFO__Anonymous_e__Union(Union):
        pass
    class GET_VIRTUAL_DISK_INFO__Anonymous_e__Union__PhysicalDisk_e__Struct(Structure):
        pass
    GET_VIRTUAL_DISK_INFO__Anonymous_e__Union__PhysicalDisk_e__Struct._fields_ = [
        ("LogicalSectorSize", UInt32),
        ("PhysicalSectorSize", UInt32),
        ("IsRemote", win32more.Foundation.BOOL),
    ]
    class GET_VIRTUAL_DISK_INFO__Anonymous_e__Union__Size_e__Struct(Structure):
        pass
    GET_VIRTUAL_DISK_INFO__Anonymous_e__Union__Size_e__Struct._fields_ = [
        ("VirtualSize", UInt64),
        ("PhysicalSize", UInt64),
        ("BlockSize", UInt32),
        ("SectorSize", UInt32),
    ]
    class GET_VIRTUAL_DISK_INFO__Anonymous_e__Union__ChangeTrackingState_e__Struct(Structure):
        pass
    GET_VIRTUAL_DISK_INFO__Anonymous_e__Union__ChangeTrackingState_e__Struct._fields_ = [
        ("Enabled", win32more.Foundation.BOOL),
        ("NewerChanges", win32more.Foundation.BOOL),
        ("MostRecentId", Char * 0),
    ]
    class GET_VIRTUAL_DISK_INFO__Anonymous_e__Union__ParentLocation_e__Struct(Structure):
        pass
    GET_VIRTUAL_DISK_INFO__Anonymous_e__Union__ParentLocation_e__Struct._fields_ = [
        ("ParentResolved", win32more.Foundation.BOOL),
        ("ParentLocationBuffer", Char * 0),
    ]
    GET_VIRTUAL_DISK_INFO__Anonymous_e__Union._fields_ = [
        ("Size", GET_VIRTUAL_DISK_INFO__Anonymous_e__Union__Size_e__Struct),
        ("Identifier", Guid),
        ("ParentLocation", GET_VIRTUAL_DISK_INFO__Anonymous_e__Union__ParentLocation_e__Struct),
        ("ParentIdentifier", Guid),
        ("ParentTimestamp", UInt32),
        ("VirtualStorageType", win32more.Storage.Vhd.VIRTUAL_STORAGE_TYPE),
        ("ProviderSubtype", UInt32),
        ("Is4kAligned", win32more.Foundation.BOOL),
        ("IsLoaded", win32more.Foundation.BOOL),
        ("PhysicalDisk", GET_VIRTUAL_DISK_INFO__Anonymous_e__Union__PhysicalDisk_e__Struct),
        ("VhdPhysicalSectorSize", UInt32),
        ("SmallestSafeVirtualSize", UInt64),
        ("FragmentationPercentage", UInt32),
        ("VirtualDiskId", Guid),
        ("ChangeTrackingState", GET_VIRTUAL_DISK_INFO__Anonymous_e__Union__ChangeTrackingState_e__Struct),
    ]
    GET_VIRTUAL_DISK_INFO._anonymous_ = [
        'Anonymous',
    ]
    GET_VIRTUAL_DISK_INFO._fields_ = [
        ("Version", win32more.Storage.Vhd.GET_VIRTUAL_DISK_INFO_VERSION),
        ("Anonymous", GET_VIRTUAL_DISK_INFO__Anonymous_e__Union),
    ]
    return GET_VIRTUAL_DISK_INFO
SET_VIRTUAL_DISK_INFO_VERSION = Int32
SET_VIRTUAL_DISK_INFO_UNSPECIFIED = 0
SET_VIRTUAL_DISK_INFO_PARENT_PATH = 1
SET_VIRTUAL_DISK_INFO_IDENTIFIER = 2
SET_VIRTUAL_DISK_INFO_PARENT_PATH_WITH_DEPTH = 3
SET_VIRTUAL_DISK_INFO_PHYSICAL_SECTOR_SIZE = 4
SET_VIRTUAL_DISK_INFO_VIRTUAL_DISK_ID = 5
SET_VIRTUAL_DISK_INFO_CHANGE_TRACKING_STATE = 6
SET_VIRTUAL_DISK_INFO_PARENT_LOCATOR = 7
def _define_SET_VIRTUAL_DISK_INFO_head():
    class SET_VIRTUAL_DISK_INFO(Structure):
        pass
    return SET_VIRTUAL_DISK_INFO
def _define_SET_VIRTUAL_DISK_INFO():
    SET_VIRTUAL_DISK_INFO = win32more.Storage.Vhd.SET_VIRTUAL_DISK_INFO_head
    class SET_VIRTUAL_DISK_INFO__Anonymous_e__Union(Union):
        pass
    class SET_VIRTUAL_DISK_INFO__Anonymous_e__Union__ParentPathWithDepthInfo_e__Struct(Structure):
        pass
    SET_VIRTUAL_DISK_INFO__Anonymous_e__Union__ParentPathWithDepthInfo_e__Struct._fields_ = [
        ("ChildDepth", UInt32),
        ("ParentFilePath", win32more.Foundation.PWSTR),
    ]
    class SET_VIRTUAL_DISK_INFO__Anonymous_e__Union__ParentLocator_e__Struct(Structure):
        pass
    SET_VIRTUAL_DISK_INFO__Anonymous_e__Union__ParentLocator_e__Struct._fields_ = [
        ("LinkageId", Guid),
        ("ParentFilePath", win32more.Foundation.PWSTR),
    ]
    SET_VIRTUAL_DISK_INFO__Anonymous_e__Union._fields_ = [
        ("ParentFilePath", win32more.Foundation.PWSTR),
        ("UniqueIdentifier", Guid),
        ("ParentPathWithDepthInfo", SET_VIRTUAL_DISK_INFO__Anonymous_e__Union__ParentPathWithDepthInfo_e__Struct),
        ("VhdPhysicalSectorSize", UInt32),
        ("VirtualDiskId", Guid),
        ("ChangeTrackingEnabled", win32more.Foundation.BOOL),
        ("ParentLocator", SET_VIRTUAL_DISK_INFO__Anonymous_e__Union__ParentLocator_e__Struct),
    ]
    SET_VIRTUAL_DISK_INFO._anonymous_ = [
        'Anonymous',
    ]
    SET_VIRTUAL_DISK_INFO._fields_ = [
        ("Version", win32more.Storage.Vhd.SET_VIRTUAL_DISK_INFO_VERSION),
        ("Anonymous", SET_VIRTUAL_DISK_INFO__Anonymous_e__Union),
    ]
    return SET_VIRTUAL_DISK_INFO
def _define_VIRTUAL_DISK_PROGRESS_head():
    class VIRTUAL_DISK_PROGRESS(Structure):
        pass
    return VIRTUAL_DISK_PROGRESS
def _define_VIRTUAL_DISK_PROGRESS():
    VIRTUAL_DISK_PROGRESS = win32more.Storage.Vhd.VIRTUAL_DISK_PROGRESS_head
    VIRTUAL_DISK_PROGRESS._fields_ = [
        ("OperationStatus", UInt32),
        ("CurrentValue", UInt64),
        ("CompletionValue", UInt64),
    ]
    return VIRTUAL_DISK_PROGRESS
COMPACT_VIRTUAL_DISK_VERSION = Int32
COMPACT_VIRTUAL_DISK_VERSION_UNSPECIFIED = 0
COMPACT_VIRTUAL_DISK_VERSION_1 = 1
def _define_COMPACT_VIRTUAL_DISK_PARAMETERS_head():
    class COMPACT_VIRTUAL_DISK_PARAMETERS(Structure):
        pass
    return COMPACT_VIRTUAL_DISK_PARAMETERS
def _define_COMPACT_VIRTUAL_DISK_PARAMETERS():
    COMPACT_VIRTUAL_DISK_PARAMETERS = win32more.Storage.Vhd.COMPACT_VIRTUAL_DISK_PARAMETERS_head
    class COMPACT_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union(Union):
        pass
    class COMPACT_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version1_e__Struct(Structure):
        pass
    COMPACT_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version1_e__Struct._fields_ = [
        ("Reserved", UInt32),
    ]
    COMPACT_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union._fields_ = [
        ("Version1", COMPACT_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version1_e__Struct),
    ]
    COMPACT_VIRTUAL_DISK_PARAMETERS._anonymous_ = [
        'Anonymous',
    ]
    COMPACT_VIRTUAL_DISK_PARAMETERS._fields_ = [
        ("Version", win32more.Storage.Vhd.COMPACT_VIRTUAL_DISK_VERSION),
        ("Anonymous", COMPACT_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union),
    ]
    return COMPACT_VIRTUAL_DISK_PARAMETERS
COMPACT_VIRTUAL_DISK_FLAG = UInt32
COMPACT_VIRTUAL_DISK_FLAG_NONE = 0
COMPACT_VIRTUAL_DISK_FLAG_NO_ZERO_SCAN = 1
COMPACT_VIRTUAL_DISK_FLAG_NO_BLOCK_MOVES = 2
MERGE_VIRTUAL_DISK_VERSION = Int32
MERGE_VIRTUAL_DISK_VERSION_UNSPECIFIED = 0
MERGE_VIRTUAL_DISK_VERSION_1 = 1
MERGE_VIRTUAL_DISK_VERSION_2 = 2
def _define_MERGE_VIRTUAL_DISK_PARAMETERS_head():
    class MERGE_VIRTUAL_DISK_PARAMETERS(Structure):
        pass
    return MERGE_VIRTUAL_DISK_PARAMETERS
def _define_MERGE_VIRTUAL_DISK_PARAMETERS():
    MERGE_VIRTUAL_DISK_PARAMETERS = win32more.Storage.Vhd.MERGE_VIRTUAL_DISK_PARAMETERS_head
    class MERGE_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union(Union):
        pass
    class MERGE_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version2_e__Struct(Structure):
        pass
    MERGE_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version2_e__Struct._fields_ = [
        ("MergeSourceDepth", UInt32),
        ("MergeTargetDepth", UInt32),
    ]
    class MERGE_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version1_e__Struct(Structure):
        pass
    MERGE_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version1_e__Struct._fields_ = [
        ("MergeDepth", UInt32),
    ]
    MERGE_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union._fields_ = [
        ("Version1", MERGE_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version1_e__Struct),
        ("Version2", MERGE_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version2_e__Struct),
    ]
    MERGE_VIRTUAL_DISK_PARAMETERS._anonymous_ = [
        'Anonymous',
    ]
    MERGE_VIRTUAL_DISK_PARAMETERS._fields_ = [
        ("Version", win32more.Storage.Vhd.MERGE_VIRTUAL_DISK_VERSION),
        ("Anonymous", MERGE_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union),
    ]
    return MERGE_VIRTUAL_DISK_PARAMETERS
MERGE_VIRTUAL_DISK_FLAG = UInt32
MERGE_VIRTUAL_DISK_FLAG_NONE = 0
EXPAND_VIRTUAL_DISK_VERSION = Int32
EXPAND_VIRTUAL_DISK_VERSION_UNSPECIFIED = 0
EXPAND_VIRTUAL_DISK_VERSION_1 = 1
def _define_EXPAND_VIRTUAL_DISK_PARAMETERS_head():
    class EXPAND_VIRTUAL_DISK_PARAMETERS(Structure):
        pass
    return EXPAND_VIRTUAL_DISK_PARAMETERS
def _define_EXPAND_VIRTUAL_DISK_PARAMETERS():
    EXPAND_VIRTUAL_DISK_PARAMETERS = win32more.Storage.Vhd.EXPAND_VIRTUAL_DISK_PARAMETERS_head
    class EXPAND_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union(Union):
        pass
    class EXPAND_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version1_e__Struct(Structure):
        pass
    EXPAND_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version1_e__Struct._fields_ = [
        ("NewSize", UInt64),
    ]
    EXPAND_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union._fields_ = [
        ("Version1", EXPAND_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version1_e__Struct),
    ]
    EXPAND_VIRTUAL_DISK_PARAMETERS._anonymous_ = [
        'Anonymous',
    ]
    EXPAND_VIRTUAL_DISK_PARAMETERS._fields_ = [
        ("Version", win32more.Storage.Vhd.EXPAND_VIRTUAL_DISK_VERSION),
        ("Anonymous", EXPAND_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union),
    ]
    return EXPAND_VIRTUAL_DISK_PARAMETERS
EXPAND_VIRTUAL_DISK_FLAG = UInt32
EXPAND_VIRTUAL_DISK_FLAG_NONE = 0
EXPAND_VIRTUAL_DISK_FLAG_NOTIFY_CHANGE = 1
RESIZE_VIRTUAL_DISK_VERSION = Int32
RESIZE_VIRTUAL_DISK_VERSION_UNSPECIFIED = 0
RESIZE_VIRTUAL_DISK_VERSION_1 = 1
def _define_RESIZE_VIRTUAL_DISK_PARAMETERS_head():
    class RESIZE_VIRTUAL_DISK_PARAMETERS(Structure):
        pass
    return RESIZE_VIRTUAL_DISK_PARAMETERS
def _define_RESIZE_VIRTUAL_DISK_PARAMETERS():
    RESIZE_VIRTUAL_DISK_PARAMETERS = win32more.Storage.Vhd.RESIZE_VIRTUAL_DISK_PARAMETERS_head
    class RESIZE_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union(Union):
        pass
    class RESIZE_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version1_e__Struct(Structure):
        pass
    RESIZE_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version1_e__Struct._fields_ = [
        ("NewSize", UInt64),
    ]
    RESIZE_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union._fields_ = [
        ("Version1", RESIZE_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version1_e__Struct),
    ]
    RESIZE_VIRTUAL_DISK_PARAMETERS._anonymous_ = [
        'Anonymous',
    ]
    RESIZE_VIRTUAL_DISK_PARAMETERS._fields_ = [
        ("Version", win32more.Storage.Vhd.RESIZE_VIRTUAL_DISK_VERSION),
        ("Anonymous", RESIZE_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union),
    ]
    return RESIZE_VIRTUAL_DISK_PARAMETERS
RESIZE_VIRTUAL_DISK_FLAG = UInt32
RESIZE_VIRTUAL_DISK_FLAG_NONE = 0
RESIZE_VIRTUAL_DISK_FLAG_ALLOW_UNSAFE_VIRTUAL_SIZE = 1
RESIZE_VIRTUAL_DISK_FLAG_RESIZE_TO_SMALLEST_SAFE_VIRTUAL_SIZE = 2
MIRROR_VIRTUAL_DISK_VERSION = Int32
MIRROR_VIRTUAL_DISK_VERSION_UNSPECIFIED = 0
MIRROR_VIRTUAL_DISK_VERSION_1 = 1
def _define_MIRROR_VIRTUAL_DISK_PARAMETERS_head():
    class MIRROR_VIRTUAL_DISK_PARAMETERS(Structure):
        pass
    return MIRROR_VIRTUAL_DISK_PARAMETERS
def _define_MIRROR_VIRTUAL_DISK_PARAMETERS():
    MIRROR_VIRTUAL_DISK_PARAMETERS = win32more.Storage.Vhd.MIRROR_VIRTUAL_DISK_PARAMETERS_head
    class MIRROR_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union(Union):
        pass
    class MIRROR_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version1_e__Struct(Structure):
        pass
    MIRROR_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version1_e__Struct._fields_ = [
        ("MirrorVirtualDiskPath", win32more.Foundation.PWSTR),
    ]
    MIRROR_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union._fields_ = [
        ("Version1", MIRROR_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version1_e__Struct),
    ]
    MIRROR_VIRTUAL_DISK_PARAMETERS._anonymous_ = [
        'Anonymous',
    ]
    MIRROR_VIRTUAL_DISK_PARAMETERS._fields_ = [
        ("Version", win32more.Storage.Vhd.MIRROR_VIRTUAL_DISK_VERSION),
        ("Anonymous", MIRROR_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union),
    ]
    return MIRROR_VIRTUAL_DISK_PARAMETERS
MIRROR_VIRTUAL_DISK_FLAG = UInt32
MIRROR_VIRTUAL_DISK_FLAG_NONE = 0
MIRROR_VIRTUAL_DISK_FLAG_EXISTING_FILE = 1
MIRROR_VIRTUAL_DISK_FLAG_SKIP_MIRROR_ACTIVATION = 2
MIRROR_VIRTUAL_DISK_FLAG_ENABLE_SMB_COMPRESSION = 4
MIRROR_VIRTUAL_DISK_FLAG_IS_LIVE_MIGRATION = 8
def _define_QUERY_CHANGES_VIRTUAL_DISK_RANGE_head():
    class QUERY_CHANGES_VIRTUAL_DISK_RANGE(Structure):
        pass
    return QUERY_CHANGES_VIRTUAL_DISK_RANGE
def _define_QUERY_CHANGES_VIRTUAL_DISK_RANGE():
    QUERY_CHANGES_VIRTUAL_DISK_RANGE = win32more.Storage.Vhd.QUERY_CHANGES_VIRTUAL_DISK_RANGE_head
    QUERY_CHANGES_VIRTUAL_DISK_RANGE._fields_ = [
        ("ByteOffset", UInt64),
        ("ByteLength", UInt64),
        ("Reserved", UInt64),
    ]
    return QUERY_CHANGES_VIRTUAL_DISK_RANGE
QUERY_CHANGES_VIRTUAL_DISK_FLAG = UInt32
QUERY_CHANGES_VIRTUAL_DISK_FLAG_NONE = 0
TAKE_SNAPSHOT_VHDSET_FLAG = UInt32
TAKE_SNAPSHOT_VHDSET_FLAG_NONE = 0
TAKE_SNAPSHOT_VHDSET_FLAG_WRITEABLE = 1
TAKE_SNAPSHOT_VHDSET_VERSION = Int32
TAKE_SNAPSHOT_VHDSET_VERSION_UNSPECIFIED = 0
TAKE_SNAPSHOT_VHDSET_VERSION_1 = 1
def _define_TAKE_SNAPSHOT_VHDSET_PARAMETERS_head():
    class TAKE_SNAPSHOT_VHDSET_PARAMETERS(Structure):
        pass
    return TAKE_SNAPSHOT_VHDSET_PARAMETERS
def _define_TAKE_SNAPSHOT_VHDSET_PARAMETERS():
    TAKE_SNAPSHOT_VHDSET_PARAMETERS = win32more.Storage.Vhd.TAKE_SNAPSHOT_VHDSET_PARAMETERS_head
    class TAKE_SNAPSHOT_VHDSET_PARAMETERS__Anonymous_e__Union(Union):
        pass
    class TAKE_SNAPSHOT_VHDSET_PARAMETERS__Anonymous_e__Union__Version1_e__Struct(Structure):
        pass
    TAKE_SNAPSHOT_VHDSET_PARAMETERS__Anonymous_e__Union__Version1_e__Struct._fields_ = [
        ("SnapshotId", Guid),
    ]
    TAKE_SNAPSHOT_VHDSET_PARAMETERS__Anonymous_e__Union._fields_ = [
        ("Version1", TAKE_SNAPSHOT_VHDSET_PARAMETERS__Anonymous_e__Union__Version1_e__Struct),
    ]
    TAKE_SNAPSHOT_VHDSET_PARAMETERS._anonymous_ = [
        'Anonymous',
    ]
    TAKE_SNAPSHOT_VHDSET_PARAMETERS._fields_ = [
        ("Version", win32more.Storage.Vhd.TAKE_SNAPSHOT_VHDSET_VERSION),
        ("Anonymous", TAKE_SNAPSHOT_VHDSET_PARAMETERS__Anonymous_e__Union),
    ]
    return TAKE_SNAPSHOT_VHDSET_PARAMETERS
DELETE_SNAPSHOT_VHDSET_FLAG = UInt32
DELETE_SNAPSHOT_VHDSET_FLAG_NONE = 0
DELETE_SNAPSHOT_VHDSET_FLAG_PERSIST_RCT = 1
DELETE_SNAPSHOT_VHDSET_VERSION = Int32
DELETE_SNAPSHOT_VHDSET_VERSION_UNSPECIFIED = 0
DELETE_SNAPSHOT_VHDSET_VERSION_1 = 1
def _define_DELETE_SNAPSHOT_VHDSET_PARAMETERS_head():
    class DELETE_SNAPSHOT_VHDSET_PARAMETERS(Structure):
        pass
    return DELETE_SNAPSHOT_VHDSET_PARAMETERS
def _define_DELETE_SNAPSHOT_VHDSET_PARAMETERS():
    DELETE_SNAPSHOT_VHDSET_PARAMETERS = win32more.Storage.Vhd.DELETE_SNAPSHOT_VHDSET_PARAMETERS_head
    class DELETE_SNAPSHOT_VHDSET_PARAMETERS__Anonymous_e__Union(Union):
        pass
    class DELETE_SNAPSHOT_VHDSET_PARAMETERS__Anonymous_e__Union__Version1_e__Struct(Structure):
        pass
    DELETE_SNAPSHOT_VHDSET_PARAMETERS__Anonymous_e__Union__Version1_e__Struct._fields_ = [
        ("SnapshotId", Guid),
    ]
    DELETE_SNAPSHOT_VHDSET_PARAMETERS__Anonymous_e__Union._fields_ = [
        ("Version1", DELETE_SNAPSHOT_VHDSET_PARAMETERS__Anonymous_e__Union__Version1_e__Struct),
    ]
    DELETE_SNAPSHOT_VHDSET_PARAMETERS._anonymous_ = [
        'Anonymous',
    ]
    DELETE_SNAPSHOT_VHDSET_PARAMETERS._fields_ = [
        ("Version", win32more.Storage.Vhd.DELETE_SNAPSHOT_VHDSET_VERSION),
        ("Anonymous", DELETE_SNAPSHOT_VHDSET_PARAMETERS__Anonymous_e__Union),
    ]
    return DELETE_SNAPSHOT_VHDSET_PARAMETERS
MODIFY_VHDSET_VERSION = Int32
MODIFY_VHDSET_UNSPECIFIED = 0
MODIFY_VHDSET_SNAPSHOT_PATH = 1
MODIFY_VHDSET_REMOVE_SNAPSHOT = 2
MODIFY_VHDSET_DEFAULT_SNAPSHOT_PATH = 3
MODIFY_VHDSET_FLAG = UInt32
MODIFY_VHDSET_FLAG_NONE = 0
MODIFY_VHDSET_FLAG_WRITEABLE_SNAPSHOT = 1
def _define_MODIFY_VHDSET_PARAMETERS_head():
    class MODIFY_VHDSET_PARAMETERS(Structure):
        pass
    return MODIFY_VHDSET_PARAMETERS
def _define_MODIFY_VHDSET_PARAMETERS():
    MODIFY_VHDSET_PARAMETERS = win32more.Storage.Vhd.MODIFY_VHDSET_PARAMETERS_head
    class MODIFY_VHDSET_PARAMETERS__Anonymous_e__Union(Union):
        pass
    class MODIFY_VHDSET_PARAMETERS__Anonymous_e__Union__SnapshotPath_e__Struct(Structure):
        pass
    MODIFY_VHDSET_PARAMETERS__Anonymous_e__Union__SnapshotPath_e__Struct._fields_ = [
        ("SnapshotId", Guid),
        ("SnapshotFilePath", win32more.Foundation.PWSTR),
    ]
    MODIFY_VHDSET_PARAMETERS__Anonymous_e__Union._fields_ = [
        ("SnapshotPath", MODIFY_VHDSET_PARAMETERS__Anonymous_e__Union__SnapshotPath_e__Struct),
        ("SnapshotId", Guid),
        ("DefaultFilePath", win32more.Foundation.PWSTR),
    ]
    MODIFY_VHDSET_PARAMETERS._anonymous_ = [
        'Anonymous',
    ]
    MODIFY_VHDSET_PARAMETERS._fields_ = [
        ("Version", win32more.Storage.Vhd.MODIFY_VHDSET_VERSION),
        ("Anonymous", MODIFY_VHDSET_PARAMETERS__Anonymous_e__Union),
    ]
    return MODIFY_VHDSET_PARAMETERS
APPLY_SNAPSHOT_VHDSET_FLAG = UInt32
APPLY_SNAPSHOT_VHDSET_FLAG_NONE = 0
APPLY_SNAPSHOT_VHDSET_FLAG_WRITEABLE = 1
APPLY_SNAPSHOT_VHDSET_VERSION = Int32
APPLY_SNAPSHOT_VHDSET_VERSION_UNSPECIFIED = 0
APPLY_SNAPSHOT_VHDSET_VERSION_1 = 1
def _define_APPLY_SNAPSHOT_VHDSET_PARAMETERS_head():
    class APPLY_SNAPSHOT_VHDSET_PARAMETERS(Structure):
        pass
    return APPLY_SNAPSHOT_VHDSET_PARAMETERS
def _define_APPLY_SNAPSHOT_VHDSET_PARAMETERS():
    APPLY_SNAPSHOT_VHDSET_PARAMETERS = win32more.Storage.Vhd.APPLY_SNAPSHOT_VHDSET_PARAMETERS_head
    class APPLY_SNAPSHOT_VHDSET_PARAMETERS__Anonymous_e__Union(Union):
        pass
    class APPLY_SNAPSHOT_VHDSET_PARAMETERS__Anonymous_e__Union__Version1_e__Struct(Structure):
        pass
    APPLY_SNAPSHOT_VHDSET_PARAMETERS__Anonymous_e__Union__Version1_e__Struct._fields_ = [
        ("SnapshotId", Guid),
        ("LeafSnapshotId", Guid),
    ]
    APPLY_SNAPSHOT_VHDSET_PARAMETERS__Anonymous_e__Union._fields_ = [
        ("Version1", APPLY_SNAPSHOT_VHDSET_PARAMETERS__Anonymous_e__Union__Version1_e__Struct),
    ]
    APPLY_SNAPSHOT_VHDSET_PARAMETERS._anonymous_ = [
        'Anonymous',
    ]
    APPLY_SNAPSHOT_VHDSET_PARAMETERS._fields_ = [
        ("Version", win32more.Storage.Vhd.APPLY_SNAPSHOT_VHDSET_VERSION),
        ("Anonymous", APPLY_SNAPSHOT_VHDSET_PARAMETERS__Anonymous_e__Union),
    ]
    return APPLY_SNAPSHOT_VHDSET_PARAMETERS
RAW_SCSI_VIRTUAL_DISK_FLAG = UInt32
RAW_SCSI_VIRTUAL_DISK_FLAG_NONE = 0
RAW_SCSI_VIRTUAL_DISK_VERSION = Int32
RAW_SCSI_VIRTUAL_DISK_VERSION_UNSPECIFIED = 0
RAW_SCSI_VIRTUAL_DISK_VERSION_1 = 1
def _define_RAW_SCSI_VIRTUAL_DISK_PARAMETERS_head():
    class RAW_SCSI_VIRTUAL_DISK_PARAMETERS(Structure):
        pass
    return RAW_SCSI_VIRTUAL_DISK_PARAMETERS
def _define_RAW_SCSI_VIRTUAL_DISK_PARAMETERS():
    RAW_SCSI_VIRTUAL_DISK_PARAMETERS = win32more.Storage.Vhd.RAW_SCSI_VIRTUAL_DISK_PARAMETERS_head
    class RAW_SCSI_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union(Union):
        pass
    class RAW_SCSI_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version1_e__Struct(Structure):
        pass
    RAW_SCSI_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version1_e__Struct._fields_ = [
        ("RSVDHandle", win32more.Foundation.BOOL),
        ("DataIn", Byte),
        ("CdbLength", Byte),
        ("SenseInfoLength", Byte),
        ("SrbFlags", UInt32),
        ("DataTransferLength", UInt32),
        ("DataBuffer", c_void_p),
        ("SenseInfo", c_char_p_no),
        ("Cdb", c_char_p_no),
    ]
    RAW_SCSI_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union._fields_ = [
        ("Version1", RAW_SCSI_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version1_e__Struct),
    ]
    RAW_SCSI_VIRTUAL_DISK_PARAMETERS._anonymous_ = [
        'Anonymous',
    ]
    RAW_SCSI_VIRTUAL_DISK_PARAMETERS._fields_ = [
        ("Version", win32more.Storage.Vhd.RAW_SCSI_VIRTUAL_DISK_VERSION),
        ("Anonymous", RAW_SCSI_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union),
    ]
    return RAW_SCSI_VIRTUAL_DISK_PARAMETERS
def _define_RAW_SCSI_VIRTUAL_DISK_RESPONSE_head():
    class RAW_SCSI_VIRTUAL_DISK_RESPONSE(Structure):
        pass
    return RAW_SCSI_VIRTUAL_DISK_RESPONSE
def _define_RAW_SCSI_VIRTUAL_DISK_RESPONSE():
    RAW_SCSI_VIRTUAL_DISK_RESPONSE = win32more.Storage.Vhd.RAW_SCSI_VIRTUAL_DISK_RESPONSE_head
    class RAW_SCSI_VIRTUAL_DISK_RESPONSE__Anonymous_e__Union(Union):
        pass
    class RAW_SCSI_VIRTUAL_DISK_RESPONSE__Anonymous_e__Union__Version1_e__Struct(Structure):
        pass
    RAW_SCSI_VIRTUAL_DISK_RESPONSE__Anonymous_e__Union__Version1_e__Struct._fields_ = [
        ("ScsiStatus", Byte),
        ("SenseInfoLength", Byte),
        ("DataTransferLength", UInt32),
    ]
    RAW_SCSI_VIRTUAL_DISK_RESPONSE__Anonymous_e__Union._fields_ = [
        ("Version1", RAW_SCSI_VIRTUAL_DISK_RESPONSE__Anonymous_e__Union__Version1_e__Struct),
    ]
    RAW_SCSI_VIRTUAL_DISK_RESPONSE._anonymous_ = [
        'Anonymous',
    ]
    RAW_SCSI_VIRTUAL_DISK_RESPONSE._fields_ = [
        ("Version", win32more.Storage.Vhd.RAW_SCSI_VIRTUAL_DISK_VERSION),
        ("Anonymous", RAW_SCSI_VIRTUAL_DISK_RESPONSE__Anonymous_e__Union),
    ]
    return RAW_SCSI_VIRTUAL_DISK_RESPONSE
FORK_VIRTUAL_DISK_VERSION = Int32
FORK_VIRTUAL_DISK_VERSION_UNSPECIFIED = 0
FORK_VIRTUAL_DISK_VERSION_1 = 1
def _define_FORK_VIRTUAL_DISK_PARAMETERS_head():
    class FORK_VIRTUAL_DISK_PARAMETERS(Structure):
        pass
    return FORK_VIRTUAL_DISK_PARAMETERS
def _define_FORK_VIRTUAL_DISK_PARAMETERS():
    FORK_VIRTUAL_DISK_PARAMETERS = win32more.Storage.Vhd.FORK_VIRTUAL_DISK_PARAMETERS_head
    class FORK_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union(Union):
        pass
    class FORK_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version1_e__Struct(Structure):
        pass
    FORK_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version1_e__Struct._fields_ = [
        ("ForkedVirtualDiskPath", win32more.Foundation.PWSTR),
    ]
    FORK_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union._fields_ = [
        ("Version1", FORK_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union__Version1_e__Struct),
    ]
    FORK_VIRTUAL_DISK_PARAMETERS._anonymous_ = [
        'Anonymous',
    ]
    FORK_VIRTUAL_DISK_PARAMETERS._fields_ = [
        ("Version", win32more.Storage.Vhd.FORK_VIRTUAL_DISK_VERSION),
        ("Anonymous", FORK_VIRTUAL_DISK_PARAMETERS__Anonymous_e__Union),
    ]
    return FORK_VIRTUAL_DISK_PARAMETERS
FORK_VIRTUAL_DISK_FLAG = UInt32
FORK_VIRTUAL_DISK_FLAG_NONE = 0
FORK_VIRTUAL_DISK_FLAG_EXISTING_FILE = 1
def _define_OpenVirtualDisk():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Storage.Vhd.VIRTUAL_STORAGE_TYPE_head),win32more.Foundation.PWSTR,win32more.Storage.Vhd.VIRTUAL_DISK_ACCESS_MASK,win32more.Storage.Vhd.OPEN_VIRTUAL_DISK_FLAG,POINTER(win32more.Storage.Vhd.OPEN_VIRTUAL_DISK_PARAMETERS_head),POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("OpenVirtualDisk", windll["VirtDisk"]), ((1, 'VirtualStorageType'),(1, 'Path'),(1, 'VirtualDiskAccessMask'),(1, 'Flags'),(1, 'Parameters'),(1, 'Handle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateVirtualDisk():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Storage.Vhd.VIRTUAL_STORAGE_TYPE_head),win32more.Foundation.PWSTR,win32more.Storage.Vhd.VIRTUAL_DISK_ACCESS_MASK,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),win32more.Storage.Vhd.CREATE_VIRTUAL_DISK_FLAG,UInt32,POINTER(win32more.Storage.Vhd.CREATE_VIRTUAL_DISK_PARAMETERS_head),POINTER(win32more.System.IO.OVERLAPPED_head),POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("CreateVirtualDisk", windll["VirtDisk"]), ((1, 'VirtualStorageType'),(1, 'Path'),(1, 'VirtualDiskAccessMask'),(1, 'SecurityDescriptor'),(1, 'Flags'),(1, 'ProviderSpecificFlags'),(1, 'Parameters'),(1, 'Overlapped'),(1, 'Handle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AttachVirtualDisk():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),win32more.Storage.Vhd.ATTACH_VIRTUAL_DISK_FLAG,UInt32,POINTER(win32more.Storage.Vhd.ATTACH_VIRTUAL_DISK_PARAMETERS_head),POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(("AttachVirtualDisk", windll["VirtDisk"]), ((1, 'VirtualDiskHandle'),(1, 'SecurityDescriptor'),(1, 'Flags'),(1, 'ProviderSpecificFlags'),(1, 'Parameters'),(1, 'Overlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DetachVirtualDisk():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Storage.Vhd.DETACH_VIRTUAL_DISK_FLAG,UInt32, use_last_error=False)(("DetachVirtualDisk", windll["VirtDisk"]), ((1, 'VirtualDiskHandle'),(1, 'Flags'),(1, 'ProviderSpecificFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetVirtualDiskPhysicalPath():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(UInt32),win32more.Foundation.PWSTR, use_last_error=False)(("GetVirtualDiskPhysicalPath", windll["VirtDisk"]), ((1, 'VirtualDiskHandle'),(1, 'DiskPathSizeInBytes'),(1, 'DiskPath'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetAllAttachedVirtualDiskPhysicalPaths():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),win32more.Foundation.PWSTR, use_last_error=False)(("GetAllAttachedVirtualDiskPhysicalPaths", windll["VirtDisk"]), ((1, 'PathsBufferSizeInBytes'),(1, 'PathsBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetStorageDependencyInformation():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Storage.Vhd.GET_STORAGE_DEPENDENCY_FLAG,UInt32,POINTER(win32more.Storage.Vhd.STORAGE_DEPENDENCY_INFO_head),POINTER(UInt32), use_last_error=False)(("GetStorageDependencyInformation", windll["VirtDisk"]), ((1, 'ObjectHandle'),(1, 'Flags'),(1, 'StorageDependencyInfoSize'),(1, 'StorageDependencyInfo'),(1, 'SizeUsed'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetVirtualDiskInformation():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(UInt32),POINTER(win32more.Storage.Vhd.GET_VIRTUAL_DISK_INFO_head),POINTER(UInt32), use_last_error=False)(("GetVirtualDiskInformation", windll["VirtDisk"]), ((1, 'VirtualDiskHandle'),(1, 'VirtualDiskInfoSize'),(1, 'VirtualDiskInfo'),(1, 'SizeUsed'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetVirtualDiskInformation():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(win32more.Storage.Vhd.SET_VIRTUAL_DISK_INFO_head), use_last_error=False)(("SetVirtualDiskInformation", windll["VirtDisk"]), ((1, 'VirtualDiskHandle'),(1, 'VirtualDiskInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumerateVirtualDiskMetadata():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(UInt32),POINTER(Guid), use_last_error=False)(("EnumerateVirtualDiskMetadata", windll["VirtDisk"]), ((1, 'VirtualDiskHandle'),(1, 'NumberOfItems'),(1, 'Items'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetVirtualDiskMetadata():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(Guid),POINTER(UInt32),c_void_p, use_last_error=False)(("GetVirtualDiskMetadata", windll["VirtDisk"]), ((1, 'VirtualDiskHandle'),(1, 'Item'),(1, 'MetaDataSize'),(1, 'MetaData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetVirtualDiskMetadata():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(Guid),UInt32,c_void_p, use_last_error=False)(("SetVirtualDiskMetadata", windll["VirtDisk"]), ((1, 'VirtualDiskHandle'),(1, 'Item'),(1, 'MetaDataSize'),(1, 'MetaData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeleteVirtualDiskMetadata():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(Guid), use_last_error=False)(("DeleteVirtualDiskMetadata", windll["VirtDisk"]), ((1, 'VirtualDiskHandle'),(1, 'Item'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetVirtualDiskOperationProgress():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(win32more.System.IO.OVERLAPPED_head),POINTER(win32more.Storage.Vhd.VIRTUAL_DISK_PROGRESS_head), use_last_error=False)(("GetVirtualDiskOperationProgress", windll["VirtDisk"]), ((1, 'VirtualDiskHandle'),(1, 'Overlapped'),(1, 'Progress'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CompactVirtualDisk():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Storage.Vhd.COMPACT_VIRTUAL_DISK_FLAG,POINTER(win32more.Storage.Vhd.COMPACT_VIRTUAL_DISK_PARAMETERS_head),POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(("CompactVirtualDisk", windll["VirtDisk"]), ((1, 'VirtualDiskHandle'),(1, 'Flags'),(1, 'Parameters'),(1, 'Overlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MergeVirtualDisk():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Storage.Vhd.MERGE_VIRTUAL_DISK_FLAG,POINTER(win32more.Storage.Vhd.MERGE_VIRTUAL_DISK_PARAMETERS_head),POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(("MergeVirtualDisk", windll["VirtDisk"]), ((1, 'VirtualDiskHandle'),(1, 'Flags'),(1, 'Parameters'),(1, 'Overlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ExpandVirtualDisk():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Storage.Vhd.EXPAND_VIRTUAL_DISK_FLAG,POINTER(win32more.Storage.Vhd.EXPAND_VIRTUAL_DISK_PARAMETERS_head),POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(("ExpandVirtualDisk", windll["VirtDisk"]), ((1, 'VirtualDiskHandle'),(1, 'Flags'),(1, 'Parameters'),(1, 'Overlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ResizeVirtualDisk():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Storage.Vhd.RESIZE_VIRTUAL_DISK_FLAG,POINTER(win32more.Storage.Vhd.RESIZE_VIRTUAL_DISK_PARAMETERS_head),POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(("ResizeVirtualDisk", windll["VirtDisk"]), ((1, 'VirtualDiskHandle'),(1, 'Flags'),(1, 'Parameters'),(1, 'Overlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MirrorVirtualDisk():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Storage.Vhd.MIRROR_VIRTUAL_DISK_FLAG,POINTER(win32more.Storage.Vhd.MIRROR_VIRTUAL_DISK_PARAMETERS_head),POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(("MirrorVirtualDisk", windll["VirtDisk"]), ((1, 'VirtualDiskHandle'),(1, 'Flags'),(1, 'Parameters'),(1, 'Overlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BreakMirrorVirtualDisk():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE, use_last_error=False)(("BreakMirrorVirtualDisk", windll["VirtDisk"]), ((1, 'VirtualDiskHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddVirtualDiskParent():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR, use_last_error=False)(("AddVirtualDiskParent", windll["VirtDisk"]), ((1, 'VirtualDiskHandle'),(1, 'ParentPath'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryChangesVirtualDisk():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,UInt64,UInt64,win32more.Storage.Vhd.QUERY_CHANGES_VIRTUAL_DISK_FLAG,POINTER(win32more.Storage.Vhd.QUERY_CHANGES_VIRTUAL_DISK_RANGE),POINTER(UInt32),POINTER(UInt64), use_last_error=False)(("QueryChangesVirtualDisk", windll["VirtDisk"]), ((1, 'VirtualDiskHandle'),(1, 'ChangeTrackingId'),(1, 'ByteOffset'),(1, 'ByteLength'),(1, 'Flags'),(1, 'Ranges'),(1, 'RangeCount'),(1, 'ProcessedLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TakeSnapshotVhdSet():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(win32more.Storage.Vhd.TAKE_SNAPSHOT_VHDSET_PARAMETERS_head),win32more.Storage.Vhd.TAKE_SNAPSHOT_VHDSET_FLAG, use_last_error=False)(("TakeSnapshotVhdSet", windll["VirtDisk"]), ((1, 'VirtualDiskHandle'),(1, 'Parameters'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeleteSnapshotVhdSet():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(win32more.Storage.Vhd.DELETE_SNAPSHOT_VHDSET_PARAMETERS_head),win32more.Storage.Vhd.DELETE_SNAPSHOT_VHDSET_FLAG, use_last_error=False)(("DeleteSnapshotVhdSet", windll["VirtDisk"]), ((1, 'VirtualDiskHandle'),(1, 'Parameters'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ModifyVhdSet():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(win32more.Storage.Vhd.MODIFY_VHDSET_PARAMETERS_head),win32more.Storage.Vhd.MODIFY_VHDSET_FLAG, use_last_error=False)(("ModifyVhdSet", windll["VirtDisk"]), ((1, 'VirtualDiskHandle'),(1, 'Parameters'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ApplySnapshotVhdSet():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(win32more.Storage.Vhd.APPLY_SNAPSHOT_VHDSET_PARAMETERS_head),win32more.Storage.Vhd.APPLY_SNAPSHOT_VHDSET_FLAG, use_last_error=False)(("ApplySnapshotVhdSet", windll["VirtDisk"]), ((1, 'VirtualDiskHandle'),(1, 'Parameters'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RawSCSIVirtualDisk():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(win32more.Storage.Vhd.RAW_SCSI_VIRTUAL_DISK_PARAMETERS_head),win32more.Storage.Vhd.RAW_SCSI_VIRTUAL_DISK_FLAG,POINTER(win32more.Storage.Vhd.RAW_SCSI_VIRTUAL_DISK_RESPONSE_head), use_last_error=False)(("RawSCSIVirtualDisk", windll["VirtDisk"]), ((1, 'VirtualDiskHandle'),(1, 'Parameters'),(1, 'Flags'),(1, 'Response'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ForkVirtualDisk():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Storage.Vhd.FORK_VIRTUAL_DISK_FLAG,POINTER(win32more.Storage.Vhd.FORK_VIRTUAL_DISK_PARAMETERS_head),POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(("ForkVirtualDisk", windll["VirtDisk"]), ((1, 'VirtualDiskHandle'),(1, 'Flags'),(1, 'Parameters'),(1, 'Overlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CompleteForkVirtualDisk():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE, use_last_error=False)(("CompleteForkVirtualDisk", windll["VirtDisk"]), ((1, 'VirtualDiskHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "VIRTUAL_STORAGE_TYPE_VENDOR_UNKNOWN",
    "VIRTUAL_STORAGE_TYPE_VENDOR_MICROSOFT",
    "VIRTUAL_STORAGE_TYPE_DEVICE_UNKNOWN",
    "VIRTUAL_STORAGE_TYPE_DEVICE_ISO",
    "VIRTUAL_STORAGE_TYPE_DEVICE_VHD",
    "VIRTUAL_STORAGE_TYPE_DEVICE_VHDX",
    "VIRTUAL_STORAGE_TYPE_DEVICE_VHDSET",
    "OPEN_VIRTUAL_DISK_RW_DEPTH_DEFAULT",
    "CREATE_VIRTUAL_DISK_PARAMETERS_DEFAULT_BLOCK_SIZE",
    "CREATE_VIRTUAL_DISK_PARAMETERS_DEFAULT_SECTOR_SIZE",
    "VIRTUAL_DISK_MAXIMUM_CHANGE_TRACKING_ID_LENGTH",
    "MERGE_VIRTUAL_DISK_DEFAULT_MERGE_DEPTH",
    "VIRTUAL_STORAGE_TYPE",
    "OPEN_VIRTUAL_DISK_VERSION",
    "OPEN_VIRTUAL_DISK_VERSION_UNSPECIFIED",
    "OPEN_VIRTUAL_DISK_VERSION_1",
    "OPEN_VIRTUAL_DISK_VERSION_2",
    "OPEN_VIRTUAL_DISK_VERSION_3",
    "OPEN_VIRTUAL_DISK_PARAMETERS",
    "VIRTUAL_DISK_ACCESS_MASK",
    "VIRTUAL_DISK_ACCESS_NONE",
    "VIRTUAL_DISK_ACCESS_ATTACH_RO",
    "VIRTUAL_DISK_ACCESS_ATTACH_RW",
    "VIRTUAL_DISK_ACCESS_DETACH",
    "VIRTUAL_DISK_ACCESS_GET_INFO",
    "VIRTUAL_DISK_ACCESS_CREATE",
    "VIRTUAL_DISK_ACCESS_METAOPS",
    "VIRTUAL_DISK_ACCESS_READ",
    "VIRTUAL_DISK_ACCESS_ALL",
    "VIRTUAL_DISK_ACCESS_WRITABLE",
    "OPEN_VIRTUAL_DISK_FLAG",
    "OPEN_VIRTUAL_DISK_FLAG_NONE",
    "OPEN_VIRTUAL_DISK_FLAG_NO_PARENTS",
    "OPEN_VIRTUAL_DISK_FLAG_BLANK_FILE",
    "OPEN_VIRTUAL_DISK_FLAG_BOOT_DRIVE",
    "OPEN_VIRTUAL_DISK_FLAG_CACHED_IO",
    "OPEN_VIRTUAL_DISK_FLAG_CUSTOM_DIFF_CHAIN",
    "OPEN_VIRTUAL_DISK_FLAG_PARENT_CACHED_IO",
    "OPEN_VIRTUAL_DISK_FLAG_VHDSET_FILE_ONLY",
    "OPEN_VIRTUAL_DISK_FLAG_IGNORE_RELATIVE_PARENT_LOCATOR",
    "OPEN_VIRTUAL_DISK_FLAG_NO_WRITE_HARDENING",
    "OPEN_VIRTUAL_DISK_FLAG_SUPPORT_COMPRESSED_VOLUMES",
    "OPEN_VIRTUAL_DISK_FLAG_SUPPORT_SPARSE_FILES_ANY_FS",
    "OPEN_VIRTUAL_DISK_FLAG_SUPPORT_ENCRYPTED_FILES",
    "CREATE_VIRTUAL_DISK_VERSION",
    "CREATE_VIRTUAL_DISK_VERSION_UNSPECIFIED",
    "CREATE_VIRTUAL_DISK_VERSION_1",
    "CREATE_VIRTUAL_DISK_VERSION_2",
    "CREATE_VIRTUAL_DISK_VERSION_3",
    "CREATE_VIRTUAL_DISK_VERSION_4",
    "CREATE_VIRTUAL_DISK_PARAMETERS",
    "CREATE_VIRTUAL_DISK_FLAG",
    "CREATE_VIRTUAL_DISK_FLAG_NONE",
    "CREATE_VIRTUAL_DISK_FLAG_FULL_PHYSICAL_ALLOCATION",
    "CREATE_VIRTUAL_DISK_FLAG_PREVENT_WRITES_TO_SOURCE_DISK",
    "CREATE_VIRTUAL_DISK_FLAG_DO_NOT_COPY_METADATA_FROM_PARENT",
    "CREATE_VIRTUAL_DISK_FLAG_CREATE_BACKING_STORAGE",
    "CREATE_VIRTUAL_DISK_FLAG_USE_CHANGE_TRACKING_SOURCE_LIMIT",
    "CREATE_VIRTUAL_DISK_FLAG_PRESERVE_PARENT_CHANGE_TRACKING_STATE",
    "CREATE_VIRTUAL_DISK_FLAG_VHD_SET_USE_ORIGINAL_BACKING_STORAGE",
    "CREATE_VIRTUAL_DISK_FLAG_SPARSE_FILE",
    "CREATE_VIRTUAL_DISK_FLAG_PMEM_COMPATIBLE",
    "CREATE_VIRTUAL_DISK_FLAG_SUPPORT_COMPRESSED_VOLUMES",
    "CREATE_VIRTUAL_DISK_FLAG_SUPPORT_SPARSE_FILES_ANY_FS",
    "ATTACH_VIRTUAL_DISK_VERSION",
    "ATTACH_VIRTUAL_DISK_VERSION_UNSPECIFIED",
    "ATTACH_VIRTUAL_DISK_VERSION_1",
    "ATTACH_VIRTUAL_DISK_VERSION_2",
    "ATTACH_VIRTUAL_DISK_PARAMETERS",
    "ATTACH_VIRTUAL_DISK_FLAG",
    "ATTACH_VIRTUAL_DISK_FLAG_NONE",
    "ATTACH_VIRTUAL_DISK_FLAG_READ_ONLY",
    "ATTACH_VIRTUAL_DISK_FLAG_NO_DRIVE_LETTER",
    "ATTACH_VIRTUAL_DISK_FLAG_PERMANENT_LIFETIME",
    "ATTACH_VIRTUAL_DISK_FLAG_NO_LOCAL_HOST",
    "ATTACH_VIRTUAL_DISK_FLAG_NO_SECURITY_DESCRIPTOR",
    "ATTACH_VIRTUAL_DISK_FLAG_BYPASS_DEFAULT_ENCRYPTION_POLICY",
    "ATTACH_VIRTUAL_DISK_FLAG_NON_PNP",
    "ATTACH_VIRTUAL_DISK_FLAG_RESTRICTED_RANGE",
    "ATTACH_VIRTUAL_DISK_FLAG_SINGLE_PARTITION",
    "ATTACH_VIRTUAL_DISK_FLAG_REGISTER_VOLUME",
    "DETACH_VIRTUAL_DISK_FLAG",
    "DETACH_VIRTUAL_DISK_FLAG_NONE",
    "DEPENDENT_DISK_FLAG",
    "DEPENDENT_DISK_FLAG_NONE",
    "DEPENDENT_DISK_FLAG_MULT_BACKING_FILES",
    "DEPENDENT_DISK_FLAG_FULLY_ALLOCATED",
    "DEPENDENT_DISK_FLAG_READ_ONLY",
    "DEPENDENT_DISK_FLAG_REMOTE",
    "DEPENDENT_DISK_FLAG_SYSTEM_VOLUME",
    "DEPENDENT_DISK_FLAG_SYSTEM_VOLUME_PARENT",
    "DEPENDENT_DISK_FLAG_REMOVABLE",
    "DEPENDENT_DISK_FLAG_NO_DRIVE_LETTER",
    "DEPENDENT_DISK_FLAG_PARENT",
    "DEPENDENT_DISK_FLAG_NO_HOST_DISK",
    "DEPENDENT_DISK_FLAG_PERMANENT_LIFETIME",
    "DEPENDENT_DISK_FLAG_SUPPORT_COMPRESSED_VOLUMES",
    "DEPENDENT_DISK_FLAG_ALWAYS_ALLOW_SPARSE",
    "DEPENDENT_DISK_FLAG_SUPPORT_ENCRYPTED_FILES",
    "STORAGE_DEPENDENCY_INFO_VERSION",
    "STORAGE_DEPENDENCY_INFO_VERSION_UNSPECIFIED",
    "STORAGE_DEPENDENCY_INFO_VERSION_1",
    "STORAGE_DEPENDENCY_INFO_VERSION_2",
    "STORAGE_DEPENDENCY_INFO_TYPE_1",
    "STORAGE_DEPENDENCY_INFO_TYPE_2",
    "STORAGE_DEPENDENCY_INFO",
    "GET_STORAGE_DEPENDENCY_FLAG",
    "GET_STORAGE_DEPENDENCY_FLAG_NONE",
    "GET_STORAGE_DEPENDENCY_FLAG_HOST_VOLUMES",
    "GET_STORAGE_DEPENDENCY_FLAG_DISK_HANDLE",
    "GET_VIRTUAL_DISK_INFO_VERSION",
    "GET_VIRTUAL_DISK_INFO_UNSPECIFIED",
    "GET_VIRTUAL_DISK_INFO_SIZE",
    "GET_VIRTUAL_DISK_INFO_IDENTIFIER",
    "GET_VIRTUAL_DISK_INFO_PARENT_LOCATION",
    "GET_VIRTUAL_DISK_INFO_PARENT_IDENTIFIER",
    "GET_VIRTUAL_DISK_INFO_PARENT_TIMESTAMP",
    "GET_VIRTUAL_DISK_INFO_VIRTUAL_STORAGE_TYPE",
    "GET_VIRTUAL_DISK_INFO_PROVIDER_SUBTYPE",
    "GET_VIRTUAL_DISK_INFO_IS_4K_ALIGNED",
    "GET_VIRTUAL_DISK_INFO_PHYSICAL_DISK",
    "GET_VIRTUAL_DISK_INFO_VHD_PHYSICAL_SECTOR_SIZE",
    "GET_VIRTUAL_DISK_INFO_SMALLEST_SAFE_VIRTUAL_SIZE",
    "GET_VIRTUAL_DISK_INFO_FRAGMENTATION",
    "GET_VIRTUAL_DISK_INFO_IS_LOADED",
    "GET_VIRTUAL_DISK_INFO_VIRTUAL_DISK_ID",
    "GET_VIRTUAL_DISK_INFO_CHANGE_TRACKING_STATE",
    "GET_VIRTUAL_DISK_INFO",
    "SET_VIRTUAL_DISK_INFO_VERSION",
    "SET_VIRTUAL_DISK_INFO_UNSPECIFIED",
    "SET_VIRTUAL_DISK_INFO_PARENT_PATH",
    "SET_VIRTUAL_DISK_INFO_IDENTIFIER",
    "SET_VIRTUAL_DISK_INFO_PARENT_PATH_WITH_DEPTH",
    "SET_VIRTUAL_DISK_INFO_PHYSICAL_SECTOR_SIZE",
    "SET_VIRTUAL_DISK_INFO_VIRTUAL_DISK_ID",
    "SET_VIRTUAL_DISK_INFO_CHANGE_TRACKING_STATE",
    "SET_VIRTUAL_DISK_INFO_PARENT_LOCATOR",
    "SET_VIRTUAL_DISK_INFO",
    "VIRTUAL_DISK_PROGRESS",
    "COMPACT_VIRTUAL_DISK_VERSION",
    "COMPACT_VIRTUAL_DISK_VERSION_UNSPECIFIED",
    "COMPACT_VIRTUAL_DISK_VERSION_1",
    "COMPACT_VIRTUAL_DISK_PARAMETERS",
    "COMPACT_VIRTUAL_DISK_FLAG",
    "COMPACT_VIRTUAL_DISK_FLAG_NONE",
    "COMPACT_VIRTUAL_DISK_FLAG_NO_ZERO_SCAN",
    "COMPACT_VIRTUAL_DISK_FLAG_NO_BLOCK_MOVES",
    "MERGE_VIRTUAL_DISK_VERSION",
    "MERGE_VIRTUAL_DISK_VERSION_UNSPECIFIED",
    "MERGE_VIRTUAL_DISK_VERSION_1",
    "MERGE_VIRTUAL_DISK_VERSION_2",
    "MERGE_VIRTUAL_DISK_PARAMETERS",
    "MERGE_VIRTUAL_DISK_FLAG",
    "MERGE_VIRTUAL_DISK_FLAG_NONE",
    "EXPAND_VIRTUAL_DISK_VERSION",
    "EXPAND_VIRTUAL_DISK_VERSION_UNSPECIFIED",
    "EXPAND_VIRTUAL_DISK_VERSION_1",
    "EXPAND_VIRTUAL_DISK_PARAMETERS",
    "EXPAND_VIRTUAL_DISK_FLAG",
    "EXPAND_VIRTUAL_DISK_FLAG_NONE",
    "EXPAND_VIRTUAL_DISK_FLAG_NOTIFY_CHANGE",
    "RESIZE_VIRTUAL_DISK_VERSION",
    "RESIZE_VIRTUAL_DISK_VERSION_UNSPECIFIED",
    "RESIZE_VIRTUAL_DISK_VERSION_1",
    "RESIZE_VIRTUAL_DISK_PARAMETERS",
    "RESIZE_VIRTUAL_DISK_FLAG",
    "RESIZE_VIRTUAL_DISK_FLAG_NONE",
    "RESIZE_VIRTUAL_DISK_FLAG_ALLOW_UNSAFE_VIRTUAL_SIZE",
    "RESIZE_VIRTUAL_DISK_FLAG_RESIZE_TO_SMALLEST_SAFE_VIRTUAL_SIZE",
    "MIRROR_VIRTUAL_DISK_VERSION",
    "MIRROR_VIRTUAL_DISK_VERSION_UNSPECIFIED",
    "MIRROR_VIRTUAL_DISK_VERSION_1",
    "MIRROR_VIRTUAL_DISK_PARAMETERS",
    "MIRROR_VIRTUAL_DISK_FLAG",
    "MIRROR_VIRTUAL_DISK_FLAG_NONE",
    "MIRROR_VIRTUAL_DISK_FLAG_EXISTING_FILE",
    "MIRROR_VIRTUAL_DISK_FLAG_SKIP_MIRROR_ACTIVATION",
    "MIRROR_VIRTUAL_DISK_FLAG_ENABLE_SMB_COMPRESSION",
    "MIRROR_VIRTUAL_DISK_FLAG_IS_LIVE_MIGRATION",
    "QUERY_CHANGES_VIRTUAL_DISK_RANGE",
    "QUERY_CHANGES_VIRTUAL_DISK_FLAG",
    "QUERY_CHANGES_VIRTUAL_DISK_FLAG_NONE",
    "TAKE_SNAPSHOT_VHDSET_FLAG",
    "TAKE_SNAPSHOT_VHDSET_FLAG_NONE",
    "TAKE_SNAPSHOT_VHDSET_FLAG_WRITEABLE",
    "TAKE_SNAPSHOT_VHDSET_VERSION",
    "TAKE_SNAPSHOT_VHDSET_VERSION_UNSPECIFIED",
    "TAKE_SNAPSHOT_VHDSET_VERSION_1",
    "TAKE_SNAPSHOT_VHDSET_PARAMETERS",
    "DELETE_SNAPSHOT_VHDSET_FLAG",
    "DELETE_SNAPSHOT_VHDSET_FLAG_NONE",
    "DELETE_SNAPSHOT_VHDSET_FLAG_PERSIST_RCT",
    "DELETE_SNAPSHOT_VHDSET_VERSION",
    "DELETE_SNAPSHOT_VHDSET_VERSION_UNSPECIFIED",
    "DELETE_SNAPSHOT_VHDSET_VERSION_1",
    "DELETE_SNAPSHOT_VHDSET_PARAMETERS",
    "MODIFY_VHDSET_VERSION",
    "MODIFY_VHDSET_UNSPECIFIED",
    "MODIFY_VHDSET_SNAPSHOT_PATH",
    "MODIFY_VHDSET_REMOVE_SNAPSHOT",
    "MODIFY_VHDSET_DEFAULT_SNAPSHOT_PATH",
    "MODIFY_VHDSET_FLAG",
    "MODIFY_VHDSET_FLAG_NONE",
    "MODIFY_VHDSET_FLAG_WRITEABLE_SNAPSHOT",
    "MODIFY_VHDSET_PARAMETERS",
    "APPLY_SNAPSHOT_VHDSET_FLAG",
    "APPLY_SNAPSHOT_VHDSET_FLAG_NONE",
    "APPLY_SNAPSHOT_VHDSET_FLAG_WRITEABLE",
    "APPLY_SNAPSHOT_VHDSET_VERSION",
    "APPLY_SNAPSHOT_VHDSET_VERSION_UNSPECIFIED",
    "APPLY_SNAPSHOT_VHDSET_VERSION_1",
    "APPLY_SNAPSHOT_VHDSET_PARAMETERS",
    "RAW_SCSI_VIRTUAL_DISK_FLAG",
    "RAW_SCSI_VIRTUAL_DISK_FLAG_NONE",
    "RAW_SCSI_VIRTUAL_DISK_VERSION",
    "RAW_SCSI_VIRTUAL_DISK_VERSION_UNSPECIFIED",
    "RAW_SCSI_VIRTUAL_DISK_VERSION_1",
    "RAW_SCSI_VIRTUAL_DISK_PARAMETERS",
    "RAW_SCSI_VIRTUAL_DISK_RESPONSE",
    "FORK_VIRTUAL_DISK_VERSION",
    "FORK_VIRTUAL_DISK_VERSION_UNSPECIFIED",
    "FORK_VIRTUAL_DISK_VERSION_1",
    "FORK_VIRTUAL_DISK_PARAMETERS",
    "FORK_VIRTUAL_DISK_FLAG",
    "FORK_VIRTUAL_DISK_FLAG_NONE",
    "FORK_VIRTUAL_DISK_FLAG_EXISTING_FILE",
    "OpenVirtualDisk",
    "CreateVirtualDisk",
    "AttachVirtualDisk",
    "DetachVirtualDisk",
    "GetVirtualDiskPhysicalPath",
    "GetAllAttachedVirtualDiskPhysicalPaths",
    "GetStorageDependencyInformation",
    "GetVirtualDiskInformation",
    "SetVirtualDiskInformation",
    "EnumerateVirtualDiskMetadata",
    "GetVirtualDiskMetadata",
    "SetVirtualDiskMetadata",
    "DeleteVirtualDiskMetadata",
    "GetVirtualDiskOperationProgress",
    "CompactVirtualDisk",
    "MergeVirtualDisk",
    "ExpandVirtualDisk",
    "ResizeVirtualDisk",
    "MirrorVirtualDisk",
    "BreakMirrorVirtualDisk",
    "AddVirtualDiskParent",
    "QueryChangesVirtualDisk",
    "TakeSnapshotVhdSet",
    "DeleteSnapshotVhdSet",
    "ModifyVhdSet",
    "ApplySnapshotVhdSet",
    "RawSCSIVirtualDisk",
    "ForkVirtualDisk",
    "CompleteForkVirtualDisk",
]
