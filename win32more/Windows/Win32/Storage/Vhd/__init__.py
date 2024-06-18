from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Security
import win32more.Windows.Win32.Storage.Vhd
import win32more.Windows.Win32.System.IO
APPLY_SNAPSHOT_VHDSET_FLAG = Int32
APPLY_SNAPSHOT_VHDSET_FLAG_NONE: win32more.Windows.Win32.Storage.Vhd.APPLY_SNAPSHOT_VHDSET_FLAG = 0
APPLY_SNAPSHOT_VHDSET_FLAG_WRITEABLE: win32more.Windows.Win32.Storage.Vhd.APPLY_SNAPSHOT_VHDSET_FLAG = 1
class APPLY_SNAPSHOT_VHDSET_PARAMETERS(Structure):
    Version: win32more.Windows.Win32.Storage.Vhd.APPLY_SNAPSHOT_VHDSET_VERSION
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Version1: _Version1_e__Struct
        class _Version1_e__Struct(Structure):
            SnapshotId: Guid
            LeafSnapshotId: Guid
APPLY_SNAPSHOT_VHDSET_VERSION = Int32
APPLY_SNAPSHOT_VHDSET_VERSION_UNSPECIFIED: win32more.Windows.Win32.Storage.Vhd.APPLY_SNAPSHOT_VHDSET_VERSION = 0
APPLY_SNAPSHOT_VHDSET_VERSION_1: win32more.Windows.Win32.Storage.Vhd.APPLY_SNAPSHOT_VHDSET_VERSION = 1
ATTACH_VIRTUAL_DISK_FLAG = Int32
ATTACH_VIRTUAL_DISK_FLAG_NONE: win32more.Windows.Win32.Storage.Vhd.ATTACH_VIRTUAL_DISK_FLAG = 0
ATTACH_VIRTUAL_DISK_FLAG_READ_ONLY: win32more.Windows.Win32.Storage.Vhd.ATTACH_VIRTUAL_DISK_FLAG = 1
ATTACH_VIRTUAL_DISK_FLAG_NO_DRIVE_LETTER: win32more.Windows.Win32.Storage.Vhd.ATTACH_VIRTUAL_DISK_FLAG = 2
ATTACH_VIRTUAL_DISK_FLAG_PERMANENT_LIFETIME: win32more.Windows.Win32.Storage.Vhd.ATTACH_VIRTUAL_DISK_FLAG = 4
ATTACH_VIRTUAL_DISK_FLAG_NO_LOCAL_HOST: win32more.Windows.Win32.Storage.Vhd.ATTACH_VIRTUAL_DISK_FLAG = 8
ATTACH_VIRTUAL_DISK_FLAG_NO_SECURITY_DESCRIPTOR: win32more.Windows.Win32.Storage.Vhd.ATTACH_VIRTUAL_DISK_FLAG = 16
ATTACH_VIRTUAL_DISK_FLAG_BYPASS_DEFAULT_ENCRYPTION_POLICY: win32more.Windows.Win32.Storage.Vhd.ATTACH_VIRTUAL_DISK_FLAG = 32
ATTACH_VIRTUAL_DISK_FLAG_NON_PNP: win32more.Windows.Win32.Storage.Vhd.ATTACH_VIRTUAL_DISK_FLAG = 64
ATTACH_VIRTUAL_DISK_FLAG_RESTRICTED_RANGE: win32more.Windows.Win32.Storage.Vhd.ATTACH_VIRTUAL_DISK_FLAG = 128
ATTACH_VIRTUAL_DISK_FLAG_SINGLE_PARTITION: win32more.Windows.Win32.Storage.Vhd.ATTACH_VIRTUAL_DISK_FLAG = 256
ATTACH_VIRTUAL_DISK_FLAG_REGISTER_VOLUME: win32more.Windows.Win32.Storage.Vhd.ATTACH_VIRTUAL_DISK_FLAG = 512
ATTACH_VIRTUAL_DISK_FLAG_AT_BOOT: win32more.Windows.Win32.Storage.Vhd.ATTACH_VIRTUAL_DISK_FLAG = 1024
class ATTACH_VIRTUAL_DISK_PARAMETERS(Structure):
    Version: win32more.Windows.Win32.Storage.Vhd.ATTACH_VIRTUAL_DISK_VERSION
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Version1: _Version1_e__Struct
        Version2: _Version2_e__Struct
        class _Version1_e__Struct(Structure):
            Reserved: UInt32
        class _Version2_e__Struct(Structure):
            RestrictedOffset: UInt64
            RestrictedLength: UInt64
ATTACH_VIRTUAL_DISK_VERSION = Int32
ATTACH_VIRTUAL_DISK_VERSION_UNSPECIFIED: win32more.Windows.Win32.Storage.Vhd.ATTACH_VIRTUAL_DISK_VERSION = 0
ATTACH_VIRTUAL_DISK_VERSION_1: win32more.Windows.Win32.Storage.Vhd.ATTACH_VIRTUAL_DISK_VERSION = 1
ATTACH_VIRTUAL_DISK_VERSION_2: win32more.Windows.Win32.Storage.Vhd.ATTACH_VIRTUAL_DISK_VERSION = 2
VIRTUAL_STORAGE_TYPE_VENDOR_UNKNOWN: Guid = Guid('{00000000-0000-0000-0000-000000000000}')
VIRTUAL_STORAGE_TYPE_VENDOR_MICROSOFT: Guid = Guid('{ec984aec-a0f9-47e9-901f-71415a66345b}')
VIRTUAL_STORAGE_TYPE_DEVICE_UNKNOWN: UInt32 = 0
VIRTUAL_STORAGE_TYPE_DEVICE_ISO: UInt32 = 1
VIRTUAL_STORAGE_TYPE_DEVICE_VHD: UInt32 = 2
VIRTUAL_STORAGE_TYPE_DEVICE_VHDX: UInt32 = 3
VIRTUAL_STORAGE_TYPE_DEVICE_VHDSET: UInt32 = 4
OPEN_VIRTUAL_DISK_RW_DEPTH_DEFAULT: UInt32 = 1
CREATE_VIRTUAL_DISK_PARAMETERS_DEFAULT_BLOCK_SIZE: UInt32 = 0
CREATE_VIRTUAL_DISK_PARAMETERS_DEFAULT_SECTOR_SIZE: UInt32 = 0
VIRTUAL_DISK_MAXIMUM_CHANGE_TRACKING_ID_LENGTH: UInt32 = 256
MERGE_VIRTUAL_DISK_DEFAULT_MERGE_DEPTH: UInt32 = 1
@winfunctype('VirtDisk.dll')
def OpenVirtualDisk(VirtualStorageType: POINTER(win32more.Windows.Win32.Storage.Vhd.VIRTUAL_STORAGE_TYPE), Path: win32more.Windows.Win32.Foundation.PWSTR, VirtualDiskAccessMask: win32more.Windows.Win32.Storage.Vhd.VIRTUAL_DISK_ACCESS_MASK, Flags: win32more.Windows.Win32.Storage.Vhd.OPEN_VIRTUAL_DISK_FLAG, Parameters: POINTER(win32more.Windows.Win32.Storage.Vhd.OPEN_VIRTUAL_DISK_PARAMETERS), Handle: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def CreateVirtualDisk(VirtualStorageType: POINTER(win32more.Windows.Win32.Storage.Vhd.VIRTUAL_STORAGE_TYPE), Path: win32more.Windows.Win32.Foundation.PWSTR, VirtualDiskAccessMask: win32more.Windows.Win32.Storage.Vhd.VIRTUAL_DISK_ACCESS_MASK, SecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, Flags: win32more.Windows.Win32.Storage.Vhd.CREATE_VIRTUAL_DISK_FLAG, ProviderSpecificFlags: UInt32, Parameters: POINTER(win32more.Windows.Win32.Storage.Vhd.CREATE_VIRTUAL_DISK_PARAMETERS), Overlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED), Handle: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def AttachVirtualDisk(VirtualDiskHandle: win32more.Windows.Win32.Foundation.HANDLE, SecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, Flags: win32more.Windows.Win32.Storage.Vhd.ATTACH_VIRTUAL_DISK_FLAG, ProviderSpecificFlags: UInt32, Parameters: POINTER(win32more.Windows.Win32.Storage.Vhd.ATTACH_VIRTUAL_DISK_PARAMETERS), Overlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def DetachVirtualDisk(VirtualDiskHandle: win32more.Windows.Win32.Foundation.HANDLE, Flags: win32more.Windows.Win32.Storage.Vhd.DETACH_VIRTUAL_DISK_FLAG, ProviderSpecificFlags: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def GetVirtualDiskPhysicalPath(VirtualDiskHandle: win32more.Windows.Win32.Foundation.HANDLE, DiskPathSizeInBytes: POINTER(UInt32), DiskPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def GetAllAttachedVirtualDiskPhysicalPaths(PathsBufferSizeInBytes: POINTER(UInt32), PathsBuffer: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def GetStorageDependencyInformation(ObjectHandle: win32more.Windows.Win32.Foundation.HANDLE, Flags: win32more.Windows.Win32.Storage.Vhd.GET_STORAGE_DEPENDENCY_FLAG, StorageDependencyInfoSize: UInt32, StorageDependencyInfo: POINTER(win32more.Windows.Win32.Storage.Vhd.STORAGE_DEPENDENCY_INFO), SizeUsed: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def GetVirtualDiskInformation(VirtualDiskHandle: win32more.Windows.Win32.Foundation.HANDLE, VirtualDiskInfoSize: POINTER(UInt32), VirtualDiskInfo: POINTER(win32more.Windows.Win32.Storage.Vhd.GET_VIRTUAL_DISK_INFO), SizeUsed: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def SetVirtualDiskInformation(VirtualDiskHandle: win32more.Windows.Win32.Foundation.HANDLE, VirtualDiskInfo: POINTER(win32more.Windows.Win32.Storage.Vhd.SET_VIRTUAL_DISK_INFO)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def EnumerateVirtualDiskMetadata(VirtualDiskHandle: win32more.Windows.Win32.Foundation.HANDLE, NumberOfItems: POINTER(UInt32), Items: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def GetVirtualDiskMetadata(VirtualDiskHandle: win32more.Windows.Win32.Foundation.HANDLE, Item: POINTER(Guid), MetaDataSize: POINTER(UInt32), MetaData: VoidPtr) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def SetVirtualDiskMetadata(VirtualDiskHandle: win32more.Windows.Win32.Foundation.HANDLE, Item: POINTER(Guid), MetaDataSize: UInt32, MetaData: VoidPtr) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def DeleteVirtualDiskMetadata(VirtualDiskHandle: win32more.Windows.Win32.Foundation.HANDLE, Item: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def GetVirtualDiskOperationProgress(VirtualDiskHandle: win32more.Windows.Win32.Foundation.HANDLE, Overlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED), Progress: POINTER(win32more.Windows.Win32.Storage.Vhd.VIRTUAL_DISK_PROGRESS)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def CompactVirtualDisk(VirtualDiskHandle: win32more.Windows.Win32.Foundation.HANDLE, Flags: win32more.Windows.Win32.Storage.Vhd.COMPACT_VIRTUAL_DISK_FLAG, Parameters: POINTER(win32more.Windows.Win32.Storage.Vhd.COMPACT_VIRTUAL_DISK_PARAMETERS), Overlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def MergeVirtualDisk(VirtualDiskHandle: win32more.Windows.Win32.Foundation.HANDLE, Flags: win32more.Windows.Win32.Storage.Vhd.MERGE_VIRTUAL_DISK_FLAG, Parameters: POINTER(win32more.Windows.Win32.Storage.Vhd.MERGE_VIRTUAL_DISK_PARAMETERS), Overlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def ExpandVirtualDisk(VirtualDiskHandle: win32more.Windows.Win32.Foundation.HANDLE, Flags: win32more.Windows.Win32.Storage.Vhd.EXPAND_VIRTUAL_DISK_FLAG, Parameters: POINTER(win32more.Windows.Win32.Storage.Vhd.EXPAND_VIRTUAL_DISK_PARAMETERS), Overlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def ResizeVirtualDisk(VirtualDiskHandle: win32more.Windows.Win32.Foundation.HANDLE, Flags: win32more.Windows.Win32.Storage.Vhd.RESIZE_VIRTUAL_DISK_FLAG, Parameters: POINTER(win32more.Windows.Win32.Storage.Vhd.RESIZE_VIRTUAL_DISK_PARAMETERS), Overlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def MirrorVirtualDisk(VirtualDiskHandle: win32more.Windows.Win32.Foundation.HANDLE, Flags: win32more.Windows.Win32.Storage.Vhd.MIRROR_VIRTUAL_DISK_FLAG, Parameters: POINTER(win32more.Windows.Win32.Storage.Vhd.MIRROR_VIRTUAL_DISK_PARAMETERS), Overlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def BreakMirrorVirtualDisk(VirtualDiskHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def AddVirtualDiskParent(VirtualDiskHandle: win32more.Windows.Win32.Foundation.HANDLE, ParentPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def QueryChangesVirtualDisk(VirtualDiskHandle: win32more.Windows.Win32.Foundation.HANDLE, ChangeTrackingId: win32more.Windows.Win32.Foundation.PWSTR, ByteOffset: UInt64, ByteLength: UInt64, Flags: win32more.Windows.Win32.Storage.Vhd.QUERY_CHANGES_VIRTUAL_DISK_FLAG, Ranges: POINTER(win32more.Windows.Win32.Storage.Vhd.QUERY_CHANGES_VIRTUAL_DISK_RANGE), RangeCount: POINTER(UInt32), ProcessedLength: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def TakeSnapshotVhdSet(VirtualDiskHandle: win32more.Windows.Win32.Foundation.HANDLE, Parameters: POINTER(win32more.Windows.Win32.Storage.Vhd.TAKE_SNAPSHOT_VHDSET_PARAMETERS), Flags: win32more.Windows.Win32.Storage.Vhd.TAKE_SNAPSHOT_VHDSET_FLAG) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def DeleteSnapshotVhdSet(VirtualDiskHandle: win32more.Windows.Win32.Foundation.HANDLE, Parameters: POINTER(win32more.Windows.Win32.Storage.Vhd.DELETE_SNAPSHOT_VHDSET_PARAMETERS), Flags: win32more.Windows.Win32.Storage.Vhd.DELETE_SNAPSHOT_VHDSET_FLAG) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def ModifyVhdSet(VirtualDiskHandle: win32more.Windows.Win32.Foundation.HANDLE, Parameters: POINTER(win32more.Windows.Win32.Storage.Vhd.MODIFY_VHDSET_PARAMETERS), Flags: win32more.Windows.Win32.Storage.Vhd.MODIFY_VHDSET_FLAG) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def ApplySnapshotVhdSet(VirtualDiskHandle: win32more.Windows.Win32.Foundation.HANDLE, Parameters: POINTER(win32more.Windows.Win32.Storage.Vhd.APPLY_SNAPSHOT_VHDSET_PARAMETERS), Flags: win32more.Windows.Win32.Storage.Vhd.APPLY_SNAPSHOT_VHDSET_FLAG) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def RawSCSIVirtualDisk(VirtualDiskHandle: win32more.Windows.Win32.Foundation.HANDLE, Parameters: POINTER(win32more.Windows.Win32.Storage.Vhd.RAW_SCSI_VIRTUAL_DISK_PARAMETERS), Flags: win32more.Windows.Win32.Storage.Vhd.RAW_SCSI_VIRTUAL_DISK_FLAG, Response: POINTER(win32more.Windows.Win32.Storage.Vhd.RAW_SCSI_VIRTUAL_DISK_RESPONSE)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def ForkVirtualDisk(VirtualDiskHandle: win32more.Windows.Win32.Foundation.HANDLE, Flags: win32more.Windows.Win32.Storage.Vhd.FORK_VIRTUAL_DISK_FLAG, Parameters: POINTER(win32more.Windows.Win32.Storage.Vhd.FORK_VIRTUAL_DISK_PARAMETERS), Overlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def CompleteForkVirtualDisk(VirtualDiskHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
COMPACT_VIRTUAL_DISK_FLAG = Int32
COMPACT_VIRTUAL_DISK_FLAG_NONE: win32more.Windows.Win32.Storage.Vhd.COMPACT_VIRTUAL_DISK_FLAG = 0
COMPACT_VIRTUAL_DISK_FLAG_NO_ZERO_SCAN: win32more.Windows.Win32.Storage.Vhd.COMPACT_VIRTUAL_DISK_FLAG = 1
COMPACT_VIRTUAL_DISK_FLAG_NO_BLOCK_MOVES: win32more.Windows.Win32.Storage.Vhd.COMPACT_VIRTUAL_DISK_FLAG = 2
class COMPACT_VIRTUAL_DISK_PARAMETERS(Structure):
    Version: win32more.Windows.Win32.Storage.Vhd.COMPACT_VIRTUAL_DISK_VERSION
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Version1: _Version1_e__Struct
        class _Version1_e__Struct(Structure):
            Reserved: UInt32
COMPACT_VIRTUAL_DISK_VERSION = Int32
COMPACT_VIRTUAL_DISK_VERSION_UNSPECIFIED: win32more.Windows.Win32.Storage.Vhd.COMPACT_VIRTUAL_DISK_VERSION = 0
COMPACT_VIRTUAL_DISK_VERSION_1: win32more.Windows.Win32.Storage.Vhd.COMPACT_VIRTUAL_DISK_VERSION = 1
CREATE_VIRTUAL_DISK_FLAG = Int32
CREATE_VIRTUAL_DISK_FLAG_NONE: win32more.Windows.Win32.Storage.Vhd.CREATE_VIRTUAL_DISK_FLAG = 0
CREATE_VIRTUAL_DISK_FLAG_FULL_PHYSICAL_ALLOCATION: win32more.Windows.Win32.Storage.Vhd.CREATE_VIRTUAL_DISK_FLAG = 1
CREATE_VIRTUAL_DISK_FLAG_PREVENT_WRITES_TO_SOURCE_DISK: win32more.Windows.Win32.Storage.Vhd.CREATE_VIRTUAL_DISK_FLAG = 2
CREATE_VIRTUAL_DISK_FLAG_DO_NOT_COPY_METADATA_FROM_PARENT: win32more.Windows.Win32.Storage.Vhd.CREATE_VIRTUAL_DISK_FLAG = 4
CREATE_VIRTUAL_DISK_FLAG_CREATE_BACKING_STORAGE: win32more.Windows.Win32.Storage.Vhd.CREATE_VIRTUAL_DISK_FLAG = 8
CREATE_VIRTUAL_DISK_FLAG_USE_CHANGE_TRACKING_SOURCE_LIMIT: win32more.Windows.Win32.Storage.Vhd.CREATE_VIRTUAL_DISK_FLAG = 16
CREATE_VIRTUAL_DISK_FLAG_PRESERVE_PARENT_CHANGE_TRACKING_STATE: win32more.Windows.Win32.Storage.Vhd.CREATE_VIRTUAL_DISK_FLAG = 32
CREATE_VIRTUAL_DISK_FLAG_VHD_SET_USE_ORIGINAL_BACKING_STORAGE: win32more.Windows.Win32.Storage.Vhd.CREATE_VIRTUAL_DISK_FLAG = 64
CREATE_VIRTUAL_DISK_FLAG_SPARSE_FILE: win32more.Windows.Win32.Storage.Vhd.CREATE_VIRTUAL_DISK_FLAG = 128
CREATE_VIRTUAL_DISK_FLAG_PMEM_COMPATIBLE: win32more.Windows.Win32.Storage.Vhd.CREATE_VIRTUAL_DISK_FLAG = 256
CREATE_VIRTUAL_DISK_FLAG_SUPPORT_COMPRESSED_VOLUMES: win32more.Windows.Win32.Storage.Vhd.CREATE_VIRTUAL_DISK_FLAG = 512
CREATE_VIRTUAL_DISK_FLAG_SUPPORT_SPARSE_FILES_ANY_FS: win32more.Windows.Win32.Storage.Vhd.CREATE_VIRTUAL_DISK_FLAG = 1024
class CREATE_VIRTUAL_DISK_PARAMETERS(Structure):
    Version: win32more.Windows.Win32.Storage.Vhd.CREATE_VIRTUAL_DISK_VERSION
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Version1: _Version1_e__Struct
        Version2: _Version2_e__Struct
        Version3: _Version3_e__Struct
        Version4: _Version4_e__Struct
        class _Version1_e__Struct(Structure):
            UniqueId: Guid
            MaximumSize: UInt64
            BlockSizeInBytes: UInt32
            SectorSizeInBytes: UInt32
            ParentPath: win32more.Windows.Win32.Foundation.PWSTR
            SourcePath: win32more.Windows.Win32.Foundation.PWSTR
        class _Version2_e__Struct(Structure):
            UniqueId: Guid
            MaximumSize: UInt64
            BlockSizeInBytes: UInt32
            SectorSizeInBytes: UInt32
            PhysicalSectorSizeInBytes: UInt32
            ParentPath: win32more.Windows.Win32.Foundation.PWSTR
            SourcePath: win32more.Windows.Win32.Foundation.PWSTR
            OpenFlags: win32more.Windows.Win32.Storage.Vhd.OPEN_VIRTUAL_DISK_FLAG
            ParentVirtualStorageType: win32more.Windows.Win32.Storage.Vhd.VIRTUAL_STORAGE_TYPE
            SourceVirtualStorageType: win32more.Windows.Win32.Storage.Vhd.VIRTUAL_STORAGE_TYPE
            ResiliencyGuid: Guid
        class _Version3_e__Struct(Structure):
            UniqueId: Guid
            MaximumSize: UInt64
            BlockSizeInBytes: UInt32
            SectorSizeInBytes: UInt32
            PhysicalSectorSizeInBytes: UInt32
            ParentPath: win32more.Windows.Win32.Foundation.PWSTR
            SourcePath: win32more.Windows.Win32.Foundation.PWSTR
            OpenFlags: win32more.Windows.Win32.Storage.Vhd.OPEN_VIRTUAL_DISK_FLAG
            ParentVirtualStorageType: win32more.Windows.Win32.Storage.Vhd.VIRTUAL_STORAGE_TYPE
            SourceVirtualStorageType: win32more.Windows.Win32.Storage.Vhd.VIRTUAL_STORAGE_TYPE
            ResiliencyGuid: Guid
            SourceLimitPath: win32more.Windows.Win32.Foundation.PWSTR
            BackingStorageType: win32more.Windows.Win32.Storage.Vhd.VIRTUAL_STORAGE_TYPE
        class _Version4_e__Struct(Structure):
            UniqueId: Guid
            MaximumSize: UInt64
            BlockSizeInBytes: UInt32
            SectorSizeInBytes: UInt32
            PhysicalSectorSizeInBytes: UInt32
            ParentPath: win32more.Windows.Win32.Foundation.PWSTR
            SourcePath: win32more.Windows.Win32.Foundation.PWSTR
            OpenFlags: win32more.Windows.Win32.Storage.Vhd.OPEN_VIRTUAL_DISK_FLAG
            ParentVirtualStorageType: win32more.Windows.Win32.Storage.Vhd.VIRTUAL_STORAGE_TYPE
            SourceVirtualStorageType: win32more.Windows.Win32.Storage.Vhd.VIRTUAL_STORAGE_TYPE
            ResiliencyGuid: Guid
            SourceLimitPath: win32more.Windows.Win32.Foundation.PWSTR
            BackingStorageType: win32more.Windows.Win32.Storage.Vhd.VIRTUAL_STORAGE_TYPE
            PmemAddressAbstractionType: Guid
            DataAlignment: UInt64
CREATE_VIRTUAL_DISK_VERSION = Int32
CREATE_VIRTUAL_DISK_VERSION_UNSPECIFIED: win32more.Windows.Win32.Storage.Vhd.CREATE_VIRTUAL_DISK_VERSION = 0
CREATE_VIRTUAL_DISK_VERSION_1: win32more.Windows.Win32.Storage.Vhd.CREATE_VIRTUAL_DISK_VERSION = 1
CREATE_VIRTUAL_DISK_VERSION_2: win32more.Windows.Win32.Storage.Vhd.CREATE_VIRTUAL_DISK_VERSION = 2
CREATE_VIRTUAL_DISK_VERSION_3: win32more.Windows.Win32.Storage.Vhd.CREATE_VIRTUAL_DISK_VERSION = 3
CREATE_VIRTUAL_DISK_VERSION_4: win32more.Windows.Win32.Storage.Vhd.CREATE_VIRTUAL_DISK_VERSION = 4
DELETE_SNAPSHOT_VHDSET_FLAG = Int32
DELETE_SNAPSHOT_VHDSET_FLAG_NONE: win32more.Windows.Win32.Storage.Vhd.DELETE_SNAPSHOT_VHDSET_FLAG = 0
DELETE_SNAPSHOT_VHDSET_FLAG_PERSIST_RCT: win32more.Windows.Win32.Storage.Vhd.DELETE_SNAPSHOT_VHDSET_FLAG = 1
class DELETE_SNAPSHOT_VHDSET_PARAMETERS(Structure):
    Version: win32more.Windows.Win32.Storage.Vhd.DELETE_SNAPSHOT_VHDSET_VERSION
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Version1: _Version1_e__Struct
        class _Version1_e__Struct(Structure):
            SnapshotId: Guid
DELETE_SNAPSHOT_VHDSET_VERSION = Int32
DELETE_SNAPSHOT_VHDSET_VERSION_UNSPECIFIED: win32more.Windows.Win32.Storage.Vhd.DELETE_SNAPSHOT_VHDSET_VERSION = 0
DELETE_SNAPSHOT_VHDSET_VERSION_1: win32more.Windows.Win32.Storage.Vhd.DELETE_SNAPSHOT_VHDSET_VERSION = 1
DEPENDENT_DISK_FLAG = Int32
DEPENDENT_DISK_FLAG_NONE: win32more.Windows.Win32.Storage.Vhd.DEPENDENT_DISK_FLAG = 0
DEPENDENT_DISK_FLAG_MULT_BACKING_FILES: win32more.Windows.Win32.Storage.Vhd.DEPENDENT_DISK_FLAG = 1
DEPENDENT_DISK_FLAG_FULLY_ALLOCATED: win32more.Windows.Win32.Storage.Vhd.DEPENDENT_DISK_FLAG = 2
DEPENDENT_DISK_FLAG_READ_ONLY: win32more.Windows.Win32.Storage.Vhd.DEPENDENT_DISK_FLAG = 4
DEPENDENT_DISK_FLAG_REMOTE: win32more.Windows.Win32.Storage.Vhd.DEPENDENT_DISK_FLAG = 8
DEPENDENT_DISK_FLAG_SYSTEM_VOLUME: win32more.Windows.Win32.Storage.Vhd.DEPENDENT_DISK_FLAG = 16
DEPENDENT_DISK_FLAG_SYSTEM_VOLUME_PARENT: win32more.Windows.Win32.Storage.Vhd.DEPENDENT_DISK_FLAG = 32
DEPENDENT_DISK_FLAG_REMOVABLE: win32more.Windows.Win32.Storage.Vhd.DEPENDENT_DISK_FLAG = 64
DEPENDENT_DISK_FLAG_NO_DRIVE_LETTER: win32more.Windows.Win32.Storage.Vhd.DEPENDENT_DISK_FLAG = 128
DEPENDENT_DISK_FLAG_PARENT: win32more.Windows.Win32.Storage.Vhd.DEPENDENT_DISK_FLAG = 256
DEPENDENT_DISK_FLAG_NO_HOST_DISK: win32more.Windows.Win32.Storage.Vhd.DEPENDENT_DISK_FLAG = 512
DEPENDENT_DISK_FLAG_PERMANENT_LIFETIME: win32more.Windows.Win32.Storage.Vhd.DEPENDENT_DISK_FLAG = 1024
DEPENDENT_DISK_FLAG_SUPPORT_COMPRESSED_VOLUMES: win32more.Windows.Win32.Storage.Vhd.DEPENDENT_DISK_FLAG = 2048
DEPENDENT_DISK_FLAG_ALWAYS_ALLOW_SPARSE: win32more.Windows.Win32.Storage.Vhd.DEPENDENT_DISK_FLAG = 4096
DEPENDENT_DISK_FLAG_SUPPORT_ENCRYPTED_FILES: win32more.Windows.Win32.Storage.Vhd.DEPENDENT_DISK_FLAG = 8192
DETACH_VIRTUAL_DISK_FLAG = Int32
DETACH_VIRTUAL_DISK_FLAG_NONE: win32more.Windows.Win32.Storage.Vhd.DETACH_VIRTUAL_DISK_FLAG = 0
EXPAND_VIRTUAL_DISK_FLAG = Int32
EXPAND_VIRTUAL_DISK_FLAG_NONE: win32more.Windows.Win32.Storage.Vhd.EXPAND_VIRTUAL_DISK_FLAG = 0
EXPAND_VIRTUAL_DISK_FLAG_NOTIFY_CHANGE: win32more.Windows.Win32.Storage.Vhd.EXPAND_VIRTUAL_DISK_FLAG = 1
class EXPAND_VIRTUAL_DISK_PARAMETERS(Structure):
    Version: win32more.Windows.Win32.Storage.Vhd.EXPAND_VIRTUAL_DISK_VERSION
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Version1: _Version1_e__Struct
        class _Version1_e__Struct(Structure):
            NewSize: UInt64
EXPAND_VIRTUAL_DISK_VERSION = Int32
EXPAND_VIRTUAL_DISK_VERSION_UNSPECIFIED: win32more.Windows.Win32.Storage.Vhd.EXPAND_VIRTUAL_DISK_VERSION = 0
EXPAND_VIRTUAL_DISK_VERSION_1: win32more.Windows.Win32.Storage.Vhd.EXPAND_VIRTUAL_DISK_VERSION = 1
FORK_VIRTUAL_DISK_FLAG = Int32
FORK_VIRTUAL_DISK_FLAG_NONE: win32more.Windows.Win32.Storage.Vhd.FORK_VIRTUAL_DISK_FLAG = 0
FORK_VIRTUAL_DISK_FLAG_EXISTING_FILE: win32more.Windows.Win32.Storage.Vhd.FORK_VIRTUAL_DISK_FLAG = 1
class FORK_VIRTUAL_DISK_PARAMETERS(Structure):
    Version: win32more.Windows.Win32.Storage.Vhd.FORK_VIRTUAL_DISK_VERSION
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Version1: _Version1_e__Struct
        class _Version1_e__Struct(Structure):
            ForkedVirtualDiskPath: win32more.Windows.Win32.Foundation.PWSTR
FORK_VIRTUAL_DISK_VERSION = Int32
FORK_VIRTUAL_DISK_VERSION_UNSPECIFIED: win32more.Windows.Win32.Storage.Vhd.FORK_VIRTUAL_DISK_VERSION = 0
FORK_VIRTUAL_DISK_VERSION_1: win32more.Windows.Win32.Storage.Vhd.FORK_VIRTUAL_DISK_VERSION = 1
GET_STORAGE_DEPENDENCY_FLAG = Int32
GET_STORAGE_DEPENDENCY_FLAG_NONE: win32more.Windows.Win32.Storage.Vhd.GET_STORAGE_DEPENDENCY_FLAG = 0
GET_STORAGE_DEPENDENCY_FLAG_HOST_VOLUMES: win32more.Windows.Win32.Storage.Vhd.GET_STORAGE_DEPENDENCY_FLAG = 1
GET_STORAGE_DEPENDENCY_FLAG_DISK_HANDLE: win32more.Windows.Win32.Storage.Vhd.GET_STORAGE_DEPENDENCY_FLAG = 2
class GET_VIRTUAL_DISK_INFO(Structure):
    Version: win32more.Windows.Win32.Storage.Vhd.GET_VIRTUAL_DISK_INFO_VERSION
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Size: _Size_e__Struct
        Identifier: Guid
        ParentLocation: _ParentLocation_e__Struct
        ParentIdentifier: Guid
        ParentTimestamp: UInt32
        VirtualStorageType: win32more.Windows.Win32.Storage.Vhd.VIRTUAL_STORAGE_TYPE
        ProviderSubtype: UInt32
        Is4kAligned: win32more.Windows.Win32.Foundation.BOOL
        IsLoaded: win32more.Windows.Win32.Foundation.BOOL
        PhysicalDisk: _PhysicalDisk_e__Struct
        VhdPhysicalSectorSize: UInt32
        SmallestSafeVirtualSize: UInt64
        FragmentationPercentage: UInt32
        VirtualDiskId: Guid
        ChangeTrackingState: _ChangeTrackingState_e__Struct
        class _Size_e__Struct(Structure):
            VirtualSize: UInt64
            PhysicalSize: UInt64
            BlockSize: UInt32
            SectorSize: UInt32
        class _ParentLocation_e__Struct(Structure):
            ParentResolved: win32more.Windows.Win32.Foundation.BOOL
            ParentLocationBuffer: Char * 1
        class _PhysicalDisk_e__Struct(Structure):
            LogicalSectorSize: UInt32
            PhysicalSectorSize: UInt32
            IsRemote: win32more.Windows.Win32.Foundation.BOOL
        class _ChangeTrackingState_e__Struct(Structure):
            Enabled: win32more.Windows.Win32.Foundation.BOOL
            NewerChanges: win32more.Windows.Win32.Foundation.BOOL
            MostRecentId: Char * 1
GET_VIRTUAL_DISK_INFO_VERSION = Int32
GET_VIRTUAL_DISK_INFO_UNSPECIFIED: win32more.Windows.Win32.Storage.Vhd.GET_VIRTUAL_DISK_INFO_VERSION = 0
GET_VIRTUAL_DISK_INFO_SIZE: win32more.Windows.Win32.Storage.Vhd.GET_VIRTUAL_DISK_INFO_VERSION = 1
GET_VIRTUAL_DISK_INFO_IDENTIFIER: win32more.Windows.Win32.Storage.Vhd.GET_VIRTUAL_DISK_INFO_VERSION = 2
GET_VIRTUAL_DISK_INFO_PARENT_LOCATION: win32more.Windows.Win32.Storage.Vhd.GET_VIRTUAL_DISK_INFO_VERSION = 3
GET_VIRTUAL_DISK_INFO_PARENT_IDENTIFIER: win32more.Windows.Win32.Storage.Vhd.GET_VIRTUAL_DISK_INFO_VERSION = 4
GET_VIRTUAL_DISK_INFO_PARENT_TIMESTAMP: win32more.Windows.Win32.Storage.Vhd.GET_VIRTUAL_DISK_INFO_VERSION = 5
GET_VIRTUAL_DISK_INFO_VIRTUAL_STORAGE_TYPE: win32more.Windows.Win32.Storage.Vhd.GET_VIRTUAL_DISK_INFO_VERSION = 6
GET_VIRTUAL_DISK_INFO_PROVIDER_SUBTYPE: win32more.Windows.Win32.Storage.Vhd.GET_VIRTUAL_DISK_INFO_VERSION = 7
GET_VIRTUAL_DISK_INFO_IS_4K_ALIGNED: win32more.Windows.Win32.Storage.Vhd.GET_VIRTUAL_DISK_INFO_VERSION = 8
GET_VIRTUAL_DISK_INFO_PHYSICAL_DISK: win32more.Windows.Win32.Storage.Vhd.GET_VIRTUAL_DISK_INFO_VERSION = 9
GET_VIRTUAL_DISK_INFO_VHD_PHYSICAL_SECTOR_SIZE: win32more.Windows.Win32.Storage.Vhd.GET_VIRTUAL_DISK_INFO_VERSION = 10
GET_VIRTUAL_DISK_INFO_SMALLEST_SAFE_VIRTUAL_SIZE: win32more.Windows.Win32.Storage.Vhd.GET_VIRTUAL_DISK_INFO_VERSION = 11
GET_VIRTUAL_DISK_INFO_FRAGMENTATION: win32more.Windows.Win32.Storage.Vhd.GET_VIRTUAL_DISK_INFO_VERSION = 12
GET_VIRTUAL_DISK_INFO_IS_LOADED: win32more.Windows.Win32.Storage.Vhd.GET_VIRTUAL_DISK_INFO_VERSION = 13
GET_VIRTUAL_DISK_INFO_VIRTUAL_DISK_ID: win32more.Windows.Win32.Storage.Vhd.GET_VIRTUAL_DISK_INFO_VERSION = 14
GET_VIRTUAL_DISK_INFO_CHANGE_TRACKING_STATE: win32more.Windows.Win32.Storage.Vhd.GET_VIRTUAL_DISK_INFO_VERSION = 15
MERGE_VIRTUAL_DISK_FLAG = Int32
MERGE_VIRTUAL_DISK_FLAG_NONE: win32more.Windows.Win32.Storage.Vhd.MERGE_VIRTUAL_DISK_FLAG = 0
class MERGE_VIRTUAL_DISK_PARAMETERS(Structure):
    Version: win32more.Windows.Win32.Storage.Vhd.MERGE_VIRTUAL_DISK_VERSION
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Version1: _Version1_e__Struct
        Version2: _Version2_e__Struct
        class _Version1_e__Struct(Structure):
            MergeDepth: UInt32
        class _Version2_e__Struct(Structure):
            MergeSourceDepth: UInt32
            MergeTargetDepth: UInt32
MERGE_VIRTUAL_DISK_VERSION = Int32
MERGE_VIRTUAL_DISK_VERSION_UNSPECIFIED: win32more.Windows.Win32.Storage.Vhd.MERGE_VIRTUAL_DISK_VERSION = 0
MERGE_VIRTUAL_DISK_VERSION_1: win32more.Windows.Win32.Storage.Vhd.MERGE_VIRTUAL_DISK_VERSION = 1
MERGE_VIRTUAL_DISK_VERSION_2: win32more.Windows.Win32.Storage.Vhd.MERGE_VIRTUAL_DISK_VERSION = 2
MIRROR_VIRTUAL_DISK_FLAG = Int32
MIRROR_VIRTUAL_DISK_FLAG_NONE: win32more.Windows.Win32.Storage.Vhd.MIRROR_VIRTUAL_DISK_FLAG = 0
MIRROR_VIRTUAL_DISK_FLAG_EXISTING_FILE: win32more.Windows.Win32.Storage.Vhd.MIRROR_VIRTUAL_DISK_FLAG = 1
MIRROR_VIRTUAL_DISK_FLAG_SKIP_MIRROR_ACTIVATION: win32more.Windows.Win32.Storage.Vhd.MIRROR_VIRTUAL_DISK_FLAG = 2
MIRROR_VIRTUAL_DISK_FLAG_ENABLE_SMB_COMPRESSION: win32more.Windows.Win32.Storage.Vhd.MIRROR_VIRTUAL_DISK_FLAG = 4
MIRROR_VIRTUAL_DISK_FLAG_IS_LIVE_MIGRATION: win32more.Windows.Win32.Storage.Vhd.MIRROR_VIRTUAL_DISK_FLAG = 8
class MIRROR_VIRTUAL_DISK_PARAMETERS(Structure):
    Version: win32more.Windows.Win32.Storage.Vhd.MIRROR_VIRTUAL_DISK_VERSION
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Version1: _Version1_e__Struct
        class _Version1_e__Struct(Structure):
            MirrorVirtualDiskPath: win32more.Windows.Win32.Foundation.PWSTR
MIRROR_VIRTUAL_DISK_VERSION = Int32
MIRROR_VIRTUAL_DISK_VERSION_UNSPECIFIED: win32more.Windows.Win32.Storage.Vhd.MIRROR_VIRTUAL_DISK_VERSION = 0
MIRROR_VIRTUAL_DISK_VERSION_1: win32more.Windows.Win32.Storage.Vhd.MIRROR_VIRTUAL_DISK_VERSION = 1
MODIFY_VHDSET_FLAG = Int32
MODIFY_VHDSET_FLAG_NONE: win32more.Windows.Win32.Storage.Vhd.MODIFY_VHDSET_FLAG = 0
MODIFY_VHDSET_FLAG_WRITEABLE_SNAPSHOT: win32more.Windows.Win32.Storage.Vhd.MODIFY_VHDSET_FLAG = 1
class MODIFY_VHDSET_PARAMETERS(Structure):
    Version: win32more.Windows.Win32.Storage.Vhd.MODIFY_VHDSET_VERSION
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        SnapshotPath: _SnapshotPath_e__Struct
        SnapshotId: Guid
        DefaultFilePath: win32more.Windows.Win32.Foundation.PWSTR
        class _SnapshotPath_e__Struct(Structure):
            SnapshotId: Guid
            SnapshotFilePath: win32more.Windows.Win32.Foundation.PWSTR
MODIFY_VHDSET_VERSION = Int32
MODIFY_VHDSET_UNSPECIFIED: win32more.Windows.Win32.Storage.Vhd.MODIFY_VHDSET_VERSION = 0
MODIFY_VHDSET_SNAPSHOT_PATH: win32more.Windows.Win32.Storage.Vhd.MODIFY_VHDSET_VERSION = 1
MODIFY_VHDSET_REMOVE_SNAPSHOT: win32more.Windows.Win32.Storage.Vhd.MODIFY_VHDSET_VERSION = 2
MODIFY_VHDSET_DEFAULT_SNAPSHOT_PATH: win32more.Windows.Win32.Storage.Vhd.MODIFY_VHDSET_VERSION = 3
OPEN_VIRTUAL_DISK_FLAG = Int32
OPEN_VIRTUAL_DISK_FLAG_NONE: win32more.Windows.Win32.Storage.Vhd.OPEN_VIRTUAL_DISK_FLAG = 0
OPEN_VIRTUAL_DISK_FLAG_NO_PARENTS: win32more.Windows.Win32.Storage.Vhd.OPEN_VIRTUAL_DISK_FLAG = 1
OPEN_VIRTUAL_DISK_FLAG_BLANK_FILE: win32more.Windows.Win32.Storage.Vhd.OPEN_VIRTUAL_DISK_FLAG = 2
OPEN_VIRTUAL_DISK_FLAG_BOOT_DRIVE: win32more.Windows.Win32.Storage.Vhd.OPEN_VIRTUAL_DISK_FLAG = 4
OPEN_VIRTUAL_DISK_FLAG_CACHED_IO: win32more.Windows.Win32.Storage.Vhd.OPEN_VIRTUAL_DISK_FLAG = 8
OPEN_VIRTUAL_DISK_FLAG_CUSTOM_DIFF_CHAIN: win32more.Windows.Win32.Storage.Vhd.OPEN_VIRTUAL_DISK_FLAG = 16
OPEN_VIRTUAL_DISK_FLAG_PARENT_CACHED_IO: win32more.Windows.Win32.Storage.Vhd.OPEN_VIRTUAL_DISK_FLAG = 32
OPEN_VIRTUAL_DISK_FLAG_VHDSET_FILE_ONLY: win32more.Windows.Win32.Storage.Vhd.OPEN_VIRTUAL_DISK_FLAG = 64
OPEN_VIRTUAL_DISK_FLAG_IGNORE_RELATIVE_PARENT_LOCATOR: win32more.Windows.Win32.Storage.Vhd.OPEN_VIRTUAL_DISK_FLAG = 128
OPEN_VIRTUAL_DISK_FLAG_NO_WRITE_HARDENING: win32more.Windows.Win32.Storage.Vhd.OPEN_VIRTUAL_DISK_FLAG = 256
OPEN_VIRTUAL_DISK_FLAG_SUPPORT_COMPRESSED_VOLUMES: win32more.Windows.Win32.Storage.Vhd.OPEN_VIRTUAL_DISK_FLAG = 512
OPEN_VIRTUAL_DISK_FLAG_SUPPORT_SPARSE_FILES_ANY_FS: win32more.Windows.Win32.Storage.Vhd.OPEN_VIRTUAL_DISK_FLAG = 1024
OPEN_VIRTUAL_DISK_FLAG_SUPPORT_ENCRYPTED_FILES: win32more.Windows.Win32.Storage.Vhd.OPEN_VIRTUAL_DISK_FLAG = 2048
class OPEN_VIRTUAL_DISK_PARAMETERS(Structure):
    Version: win32more.Windows.Win32.Storage.Vhd.OPEN_VIRTUAL_DISK_VERSION
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Version1: _Version1_e__Struct
        Version2: _Version2_e__Struct
        Version3: _Version3_e__Struct
        class _Version1_e__Struct(Structure):
            RWDepth: UInt32
        class _Version2_e__Struct(Structure):
            GetInfoOnly: win32more.Windows.Win32.Foundation.BOOL
            ReadOnly: win32more.Windows.Win32.Foundation.BOOL
            ResiliencyGuid: Guid
        class _Version3_e__Struct(Structure):
            GetInfoOnly: win32more.Windows.Win32.Foundation.BOOL
            ReadOnly: win32more.Windows.Win32.Foundation.BOOL
            ResiliencyGuid: Guid
            SnapshotId: Guid
OPEN_VIRTUAL_DISK_VERSION = Int32
OPEN_VIRTUAL_DISK_VERSION_UNSPECIFIED: win32more.Windows.Win32.Storage.Vhd.OPEN_VIRTUAL_DISK_VERSION = 0
OPEN_VIRTUAL_DISK_VERSION_1: win32more.Windows.Win32.Storage.Vhd.OPEN_VIRTUAL_DISK_VERSION = 1
OPEN_VIRTUAL_DISK_VERSION_2: win32more.Windows.Win32.Storage.Vhd.OPEN_VIRTUAL_DISK_VERSION = 2
OPEN_VIRTUAL_DISK_VERSION_3: win32more.Windows.Win32.Storage.Vhd.OPEN_VIRTUAL_DISK_VERSION = 3
QUERY_CHANGES_VIRTUAL_DISK_FLAG = Int32
QUERY_CHANGES_VIRTUAL_DISK_FLAG_NONE: win32more.Windows.Win32.Storage.Vhd.QUERY_CHANGES_VIRTUAL_DISK_FLAG = 0
class QUERY_CHANGES_VIRTUAL_DISK_RANGE(Structure):
    ByteOffset: UInt64
    ByteLength: UInt64
    Reserved: UInt64
RAW_SCSI_VIRTUAL_DISK_FLAG = Int32
RAW_SCSI_VIRTUAL_DISK_FLAG_NONE: win32more.Windows.Win32.Storage.Vhd.RAW_SCSI_VIRTUAL_DISK_FLAG = 0
class RAW_SCSI_VIRTUAL_DISK_PARAMETERS(Structure):
    Version: win32more.Windows.Win32.Storage.Vhd.RAW_SCSI_VIRTUAL_DISK_VERSION
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Version1: _Version1_e__Struct
        class _Version1_e__Struct(Structure):
            RSVDHandle: win32more.Windows.Win32.Foundation.BOOL
            DataIn: Byte
            CdbLength: Byte
            SenseInfoLength: Byte
            SrbFlags: UInt32
            DataTransferLength: UInt32
            DataBuffer: VoidPtr
            SenseInfo: POINTER(Byte)
            Cdb: POINTER(Byte)
class RAW_SCSI_VIRTUAL_DISK_RESPONSE(Structure):
    Version: win32more.Windows.Win32.Storage.Vhd.RAW_SCSI_VIRTUAL_DISK_VERSION
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Version1: _Version1_e__Struct
        class _Version1_e__Struct(Structure):
            ScsiStatus: Byte
            SenseInfoLength: Byte
            DataTransferLength: UInt32
RAW_SCSI_VIRTUAL_DISK_VERSION = Int32
RAW_SCSI_VIRTUAL_DISK_VERSION_UNSPECIFIED: win32more.Windows.Win32.Storage.Vhd.RAW_SCSI_VIRTUAL_DISK_VERSION = 0
RAW_SCSI_VIRTUAL_DISK_VERSION_1: win32more.Windows.Win32.Storage.Vhd.RAW_SCSI_VIRTUAL_DISK_VERSION = 1
RESIZE_VIRTUAL_DISK_FLAG = Int32
RESIZE_VIRTUAL_DISK_FLAG_NONE: win32more.Windows.Win32.Storage.Vhd.RESIZE_VIRTUAL_DISK_FLAG = 0
RESIZE_VIRTUAL_DISK_FLAG_ALLOW_UNSAFE_VIRTUAL_SIZE: win32more.Windows.Win32.Storage.Vhd.RESIZE_VIRTUAL_DISK_FLAG = 1
RESIZE_VIRTUAL_DISK_FLAG_RESIZE_TO_SMALLEST_SAFE_VIRTUAL_SIZE: win32more.Windows.Win32.Storage.Vhd.RESIZE_VIRTUAL_DISK_FLAG = 2
class RESIZE_VIRTUAL_DISK_PARAMETERS(Structure):
    Version: win32more.Windows.Win32.Storage.Vhd.RESIZE_VIRTUAL_DISK_VERSION
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Version1: _Version1_e__Struct
        class _Version1_e__Struct(Structure):
            NewSize: UInt64
RESIZE_VIRTUAL_DISK_VERSION = Int32
RESIZE_VIRTUAL_DISK_VERSION_UNSPECIFIED: win32more.Windows.Win32.Storage.Vhd.RESIZE_VIRTUAL_DISK_VERSION = 0
RESIZE_VIRTUAL_DISK_VERSION_1: win32more.Windows.Win32.Storage.Vhd.RESIZE_VIRTUAL_DISK_VERSION = 1
class SET_VIRTUAL_DISK_INFO(Structure):
    Version: win32more.Windows.Win32.Storage.Vhd.SET_VIRTUAL_DISK_INFO_VERSION
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        ParentFilePath: win32more.Windows.Win32.Foundation.PWSTR
        UniqueIdentifier: Guid
        ParentPathWithDepthInfo: _ParentPathWithDepthInfo_e__Struct
        VhdPhysicalSectorSize: UInt32
        VirtualDiskId: Guid
        ChangeTrackingEnabled: win32more.Windows.Win32.Foundation.BOOL
        ParentLocator: _ParentLocator_e__Struct
        class _ParentPathWithDepthInfo_e__Struct(Structure):
            ChildDepth: UInt32
            ParentFilePath: win32more.Windows.Win32.Foundation.PWSTR
        class _ParentLocator_e__Struct(Structure):
            LinkageId: Guid
            ParentFilePath: win32more.Windows.Win32.Foundation.PWSTR
SET_VIRTUAL_DISK_INFO_VERSION = Int32
SET_VIRTUAL_DISK_INFO_UNSPECIFIED: win32more.Windows.Win32.Storage.Vhd.SET_VIRTUAL_DISK_INFO_VERSION = 0
SET_VIRTUAL_DISK_INFO_PARENT_PATH: win32more.Windows.Win32.Storage.Vhd.SET_VIRTUAL_DISK_INFO_VERSION = 1
SET_VIRTUAL_DISK_INFO_IDENTIFIER: win32more.Windows.Win32.Storage.Vhd.SET_VIRTUAL_DISK_INFO_VERSION = 2
SET_VIRTUAL_DISK_INFO_PARENT_PATH_WITH_DEPTH: win32more.Windows.Win32.Storage.Vhd.SET_VIRTUAL_DISK_INFO_VERSION = 3
SET_VIRTUAL_DISK_INFO_PHYSICAL_SECTOR_SIZE: win32more.Windows.Win32.Storage.Vhd.SET_VIRTUAL_DISK_INFO_VERSION = 4
SET_VIRTUAL_DISK_INFO_VIRTUAL_DISK_ID: win32more.Windows.Win32.Storage.Vhd.SET_VIRTUAL_DISK_INFO_VERSION = 5
SET_VIRTUAL_DISK_INFO_CHANGE_TRACKING_STATE: win32more.Windows.Win32.Storage.Vhd.SET_VIRTUAL_DISK_INFO_VERSION = 6
SET_VIRTUAL_DISK_INFO_PARENT_LOCATOR: win32more.Windows.Win32.Storage.Vhd.SET_VIRTUAL_DISK_INFO_VERSION = 7
class STORAGE_DEPENDENCY_INFO(Structure):
    Version: win32more.Windows.Win32.Storage.Vhd.STORAGE_DEPENDENCY_INFO_VERSION
    NumberEntries: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Version1Entries: win32more.Windows.Win32.Storage.Vhd.STORAGE_DEPENDENCY_INFO_TYPE_1 * 1
        Version2Entries: win32more.Windows.Win32.Storage.Vhd.STORAGE_DEPENDENCY_INFO_TYPE_2 * 1
class STORAGE_DEPENDENCY_INFO_TYPE_1(Structure):
    DependencyTypeFlags: win32more.Windows.Win32.Storage.Vhd.DEPENDENT_DISK_FLAG
    ProviderSpecificFlags: UInt32
    VirtualStorageType: win32more.Windows.Win32.Storage.Vhd.VIRTUAL_STORAGE_TYPE
class STORAGE_DEPENDENCY_INFO_TYPE_2(Structure):
    DependencyTypeFlags: win32more.Windows.Win32.Storage.Vhd.DEPENDENT_DISK_FLAG
    ProviderSpecificFlags: UInt32
    VirtualStorageType: win32more.Windows.Win32.Storage.Vhd.VIRTUAL_STORAGE_TYPE
    AncestorLevel: UInt32
    DependencyDeviceName: win32more.Windows.Win32.Foundation.PWSTR
    HostVolumeName: win32more.Windows.Win32.Foundation.PWSTR
    DependentVolumeName: win32more.Windows.Win32.Foundation.PWSTR
    DependentVolumeRelativePath: win32more.Windows.Win32.Foundation.PWSTR
STORAGE_DEPENDENCY_INFO_VERSION = Int32
STORAGE_DEPENDENCY_INFO_VERSION_UNSPECIFIED: win32more.Windows.Win32.Storage.Vhd.STORAGE_DEPENDENCY_INFO_VERSION = 0
STORAGE_DEPENDENCY_INFO_VERSION_1: win32more.Windows.Win32.Storage.Vhd.STORAGE_DEPENDENCY_INFO_VERSION = 1
STORAGE_DEPENDENCY_INFO_VERSION_2: win32more.Windows.Win32.Storage.Vhd.STORAGE_DEPENDENCY_INFO_VERSION = 2
TAKE_SNAPSHOT_VHDSET_FLAG = Int32
TAKE_SNAPSHOT_VHDSET_FLAG_NONE: win32more.Windows.Win32.Storage.Vhd.TAKE_SNAPSHOT_VHDSET_FLAG = 0
TAKE_SNAPSHOT_VHDSET_FLAG_WRITEABLE: win32more.Windows.Win32.Storage.Vhd.TAKE_SNAPSHOT_VHDSET_FLAG = 1
class TAKE_SNAPSHOT_VHDSET_PARAMETERS(Structure):
    Version: win32more.Windows.Win32.Storage.Vhd.TAKE_SNAPSHOT_VHDSET_VERSION
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Version1: _Version1_e__Struct
        class _Version1_e__Struct(Structure):
            SnapshotId: Guid
TAKE_SNAPSHOT_VHDSET_VERSION = Int32
TAKE_SNAPSHOT_VHDSET_VERSION_UNSPECIFIED: win32more.Windows.Win32.Storage.Vhd.TAKE_SNAPSHOT_VHDSET_VERSION = 0
TAKE_SNAPSHOT_VHDSET_VERSION_1: win32more.Windows.Win32.Storage.Vhd.TAKE_SNAPSHOT_VHDSET_VERSION = 1
VIRTUAL_DISK_ACCESS_MASK = Int32
VIRTUAL_DISK_ACCESS_NONE: win32more.Windows.Win32.Storage.Vhd.VIRTUAL_DISK_ACCESS_MASK = 0
VIRTUAL_DISK_ACCESS_ATTACH_RO: win32more.Windows.Win32.Storage.Vhd.VIRTUAL_DISK_ACCESS_MASK = 65536
VIRTUAL_DISK_ACCESS_ATTACH_RW: win32more.Windows.Win32.Storage.Vhd.VIRTUAL_DISK_ACCESS_MASK = 131072
VIRTUAL_DISK_ACCESS_DETACH: win32more.Windows.Win32.Storage.Vhd.VIRTUAL_DISK_ACCESS_MASK = 262144
VIRTUAL_DISK_ACCESS_GET_INFO: win32more.Windows.Win32.Storage.Vhd.VIRTUAL_DISK_ACCESS_MASK = 524288
VIRTUAL_DISK_ACCESS_CREATE: win32more.Windows.Win32.Storage.Vhd.VIRTUAL_DISK_ACCESS_MASK = 1048576
VIRTUAL_DISK_ACCESS_METAOPS: win32more.Windows.Win32.Storage.Vhd.VIRTUAL_DISK_ACCESS_MASK = 2097152
VIRTUAL_DISK_ACCESS_READ: win32more.Windows.Win32.Storage.Vhd.VIRTUAL_DISK_ACCESS_MASK = 851968
VIRTUAL_DISK_ACCESS_ALL: win32more.Windows.Win32.Storage.Vhd.VIRTUAL_DISK_ACCESS_MASK = 4128768
VIRTUAL_DISK_ACCESS_WRITABLE: win32more.Windows.Win32.Storage.Vhd.VIRTUAL_DISK_ACCESS_MASK = 3276800
class VIRTUAL_DISK_PROGRESS(Structure):
    OperationStatus: UInt32
    CurrentValue: UInt64
    CompletionValue: UInt64
class VIRTUAL_STORAGE_TYPE(Structure):
    DeviceId: UInt32
    VendorId: Guid


make_ready(__name__)
