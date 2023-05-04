from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.Security
import Windows.Win32.Storage.Vhd
import Windows.Win32.System.IO
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
APPLY_SNAPSHOT_VHDSET_FLAG = Int32
APPLY_SNAPSHOT_VHDSET_FLAG_NONE: APPLY_SNAPSHOT_VHDSET_FLAG = 0
APPLY_SNAPSHOT_VHDSET_FLAG_WRITEABLE: APPLY_SNAPSHOT_VHDSET_FLAG = 1
class APPLY_SNAPSHOT_VHDSET_PARAMETERS(EasyCastStructure):
    Version: Windows.Win32.Storage.Vhd.APPLY_SNAPSHOT_VHDSET_VERSION
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Version1: _Version1_e__Struct
        class _Version1_e__Struct(EasyCastStructure):
            SnapshotId: Guid
            LeafSnapshotId: Guid
APPLY_SNAPSHOT_VHDSET_VERSION = Int32
APPLY_SNAPSHOT_VHDSET_VERSION_UNSPECIFIED: APPLY_SNAPSHOT_VHDSET_VERSION = 0
APPLY_SNAPSHOT_VHDSET_VERSION_1: APPLY_SNAPSHOT_VHDSET_VERSION = 1
ATTACH_VIRTUAL_DISK_FLAG = Int32
ATTACH_VIRTUAL_DISK_FLAG_NONE: ATTACH_VIRTUAL_DISK_FLAG = 0
ATTACH_VIRTUAL_DISK_FLAG_READ_ONLY: ATTACH_VIRTUAL_DISK_FLAG = 1
ATTACH_VIRTUAL_DISK_FLAG_NO_DRIVE_LETTER: ATTACH_VIRTUAL_DISK_FLAG = 2
ATTACH_VIRTUAL_DISK_FLAG_PERMANENT_LIFETIME: ATTACH_VIRTUAL_DISK_FLAG = 4
ATTACH_VIRTUAL_DISK_FLAG_NO_LOCAL_HOST: ATTACH_VIRTUAL_DISK_FLAG = 8
ATTACH_VIRTUAL_DISK_FLAG_NO_SECURITY_DESCRIPTOR: ATTACH_VIRTUAL_DISK_FLAG = 16
ATTACH_VIRTUAL_DISK_FLAG_BYPASS_DEFAULT_ENCRYPTION_POLICY: ATTACH_VIRTUAL_DISK_FLAG = 32
ATTACH_VIRTUAL_DISK_FLAG_NON_PNP: ATTACH_VIRTUAL_DISK_FLAG = 64
ATTACH_VIRTUAL_DISK_FLAG_RESTRICTED_RANGE: ATTACH_VIRTUAL_DISK_FLAG = 128
ATTACH_VIRTUAL_DISK_FLAG_SINGLE_PARTITION: ATTACH_VIRTUAL_DISK_FLAG = 256
ATTACH_VIRTUAL_DISK_FLAG_REGISTER_VOLUME: ATTACH_VIRTUAL_DISK_FLAG = 512
class ATTACH_VIRTUAL_DISK_PARAMETERS(EasyCastStructure):
    Version: Windows.Win32.Storage.Vhd.ATTACH_VIRTUAL_DISK_VERSION
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Version1: _Version1_e__Struct
        Version2: _Version2_e__Struct
        class _Version1_e__Struct(EasyCastStructure):
            Reserved: UInt32
        class _Version2_e__Struct(EasyCastStructure):
            RestrictedOffset: UInt64
            RestrictedLength: UInt64
ATTACH_VIRTUAL_DISK_VERSION = Int32
ATTACH_VIRTUAL_DISK_VERSION_UNSPECIFIED: ATTACH_VIRTUAL_DISK_VERSION = 0
ATTACH_VIRTUAL_DISK_VERSION_1: ATTACH_VIRTUAL_DISK_VERSION = 1
ATTACH_VIRTUAL_DISK_VERSION_2: ATTACH_VIRTUAL_DISK_VERSION = 2
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
def OpenVirtualDisk(VirtualStorageType: POINTER(Windows.Win32.Storage.Vhd.VIRTUAL_STORAGE_TYPE_head), Path: Windows.Win32.Foundation.PWSTR, VirtualDiskAccessMask: Windows.Win32.Storage.Vhd.VIRTUAL_DISK_ACCESS_MASK, Flags: Windows.Win32.Storage.Vhd.OPEN_VIRTUAL_DISK_FLAG, Parameters: POINTER(Windows.Win32.Storage.Vhd.OPEN_VIRTUAL_DISK_PARAMETERS_head), Handle: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def CreateVirtualDisk(VirtualStorageType: POINTER(Windows.Win32.Storage.Vhd.VIRTUAL_STORAGE_TYPE_head), Path: Windows.Win32.Foundation.PWSTR, VirtualDiskAccessMask: Windows.Win32.Storage.Vhd.VIRTUAL_DISK_ACCESS_MASK, SecurityDescriptor: Windows.Win32.Security.PSECURITY_DESCRIPTOR, Flags: Windows.Win32.Storage.Vhd.CREATE_VIRTUAL_DISK_FLAG, ProviderSpecificFlags: UInt32, Parameters: POINTER(Windows.Win32.Storage.Vhd.CREATE_VIRTUAL_DISK_PARAMETERS_head), Overlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head), Handle: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def AttachVirtualDisk(VirtualDiskHandle: Windows.Win32.Foundation.HANDLE, SecurityDescriptor: Windows.Win32.Security.PSECURITY_DESCRIPTOR, Flags: Windows.Win32.Storage.Vhd.ATTACH_VIRTUAL_DISK_FLAG, ProviderSpecificFlags: UInt32, Parameters: POINTER(Windows.Win32.Storage.Vhd.ATTACH_VIRTUAL_DISK_PARAMETERS_head), Overlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def DetachVirtualDisk(VirtualDiskHandle: Windows.Win32.Foundation.HANDLE, Flags: Windows.Win32.Storage.Vhd.DETACH_VIRTUAL_DISK_FLAG, ProviderSpecificFlags: UInt32) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def GetVirtualDiskPhysicalPath(VirtualDiskHandle: Windows.Win32.Foundation.HANDLE, DiskPathSizeInBytes: POINTER(UInt32), DiskPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def GetAllAttachedVirtualDiskPhysicalPaths(PathsBufferSizeInBytes: POINTER(UInt32), PathsBuffer: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def GetStorageDependencyInformation(ObjectHandle: Windows.Win32.Foundation.HANDLE, Flags: Windows.Win32.Storage.Vhd.GET_STORAGE_DEPENDENCY_FLAG, StorageDependencyInfoSize: UInt32, StorageDependencyInfo: POINTER(Windows.Win32.Storage.Vhd.STORAGE_DEPENDENCY_INFO_head), SizeUsed: POINTER(UInt32)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def GetVirtualDiskInformation(VirtualDiskHandle: Windows.Win32.Foundation.HANDLE, VirtualDiskInfoSize: POINTER(UInt32), VirtualDiskInfo: POINTER(Windows.Win32.Storage.Vhd.GET_VIRTUAL_DISK_INFO_head), SizeUsed: POINTER(UInt32)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def SetVirtualDiskInformation(VirtualDiskHandle: Windows.Win32.Foundation.HANDLE, VirtualDiskInfo: POINTER(Windows.Win32.Storage.Vhd.SET_VIRTUAL_DISK_INFO_head)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def EnumerateVirtualDiskMetadata(VirtualDiskHandle: Windows.Win32.Foundation.HANDLE, NumberOfItems: POINTER(UInt32), Items: POINTER(Guid)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def GetVirtualDiskMetadata(VirtualDiskHandle: Windows.Win32.Foundation.HANDLE, Item: POINTER(Guid), MetaDataSize: POINTER(UInt32), MetaData: c_void_p) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def SetVirtualDiskMetadata(VirtualDiskHandle: Windows.Win32.Foundation.HANDLE, Item: POINTER(Guid), MetaDataSize: UInt32, MetaData: c_void_p) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def DeleteVirtualDiskMetadata(VirtualDiskHandle: Windows.Win32.Foundation.HANDLE, Item: POINTER(Guid)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def GetVirtualDiskOperationProgress(VirtualDiskHandle: Windows.Win32.Foundation.HANDLE, Overlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head), Progress: POINTER(Windows.Win32.Storage.Vhd.VIRTUAL_DISK_PROGRESS_head)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def CompactVirtualDisk(VirtualDiskHandle: Windows.Win32.Foundation.HANDLE, Flags: Windows.Win32.Storage.Vhd.COMPACT_VIRTUAL_DISK_FLAG, Parameters: POINTER(Windows.Win32.Storage.Vhd.COMPACT_VIRTUAL_DISK_PARAMETERS_head), Overlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def MergeVirtualDisk(VirtualDiskHandle: Windows.Win32.Foundation.HANDLE, Flags: Windows.Win32.Storage.Vhd.MERGE_VIRTUAL_DISK_FLAG, Parameters: POINTER(Windows.Win32.Storage.Vhd.MERGE_VIRTUAL_DISK_PARAMETERS_head), Overlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def ExpandVirtualDisk(VirtualDiskHandle: Windows.Win32.Foundation.HANDLE, Flags: Windows.Win32.Storage.Vhd.EXPAND_VIRTUAL_DISK_FLAG, Parameters: POINTER(Windows.Win32.Storage.Vhd.EXPAND_VIRTUAL_DISK_PARAMETERS_head), Overlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def ResizeVirtualDisk(VirtualDiskHandle: Windows.Win32.Foundation.HANDLE, Flags: Windows.Win32.Storage.Vhd.RESIZE_VIRTUAL_DISK_FLAG, Parameters: POINTER(Windows.Win32.Storage.Vhd.RESIZE_VIRTUAL_DISK_PARAMETERS_head), Overlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def MirrorVirtualDisk(VirtualDiskHandle: Windows.Win32.Foundation.HANDLE, Flags: Windows.Win32.Storage.Vhd.MIRROR_VIRTUAL_DISK_FLAG, Parameters: POINTER(Windows.Win32.Storage.Vhd.MIRROR_VIRTUAL_DISK_PARAMETERS_head), Overlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def BreakMirrorVirtualDisk(VirtualDiskHandle: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def AddVirtualDiskParent(VirtualDiskHandle: Windows.Win32.Foundation.HANDLE, ParentPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def QueryChangesVirtualDisk(VirtualDiskHandle: Windows.Win32.Foundation.HANDLE, ChangeTrackingId: Windows.Win32.Foundation.PWSTR, ByteOffset: UInt64, ByteLength: UInt64, Flags: Windows.Win32.Storage.Vhd.QUERY_CHANGES_VIRTUAL_DISK_FLAG, Ranges: POINTER(Windows.Win32.Storage.Vhd.QUERY_CHANGES_VIRTUAL_DISK_RANGE_head), RangeCount: POINTER(UInt32), ProcessedLength: POINTER(UInt64)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def TakeSnapshotVhdSet(VirtualDiskHandle: Windows.Win32.Foundation.HANDLE, Parameters: POINTER(Windows.Win32.Storage.Vhd.TAKE_SNAPSHOT_VHDSET_PARAMETERS_head), Flags: Windows.Win32.Storage.Vhd.TAKE_SNAPSHOT_VHDSET_FLAG) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def DeleteSnapshotVhdSet(VirtualDiskHandle: Windows.Win32.Foundation.HANDLE, Parameters: POINTER(Windows.Win32.Storage.Vhd.DELETE_SNAPSHOT_VHDSET_PARAMETERS_head), Flags: Windows.Win32.Storage.Vhd.DELETE_SNAPSHOT_VHDSET_FLAG) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def ModifyVhdSet(VirtualDiskHandle: Windows.Win32.Foundation.HANDLE, Parameters: POINTER(Windows.Win32.Storage.Vhd.MODIFY_VHDSET_PARAMETERS_head), Flags: Windows.Win32.Storage.Vhd.MODIFY_VHDSET_FLAG) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def ApplySnapshotVhdSet(VirtualDiskHandle: Windows.Win32.Foundation.HANDLE, Parameters: POINTER(Windows.Win32.Storage.Vhd.APPLY_SNAPSHOT_VHDSET_PARAMETERS_head), Flags: Windows.Win32.Storage.Vhd.APPLY_SNAPSHOT_VHDSET_FLAG) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def RawSCSIVirtualDisk(VirtualDiskHandle: Windows.Win32.Foundation.HANDLE, Parameters: POINTER(Windows.Win32.Storage.Vhd.RAW_SCSI_VIRTUAL_DISK_PARAMETERS_head), Flags: Windows.Win32.Storage.Vhd.RAW_SCSI_VIRTUAL_DISK_FLAG, Response: POINTER(Windows.Win32.Storage.Vhd.RAW_SCSI_VIRTUAL_DISK_RESPONSE_head)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def ForkVirtualDisk(VirtualDiskHandle: Windows.Win32.Foundation.HANDLE, Flags: Windows.Win32.Storage.Vhd.FORK_VIRTUAL_DISK_FLAG, Parameters: POINTER(Windows.Win32.Storage.Vhd.FORK_VIRTUAL_DISK_PARAMETERS_head), Overlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('VirtDisk.dll')
def CompleteForkVirtualDisk(VirtualDiskHandle: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.WIN32_ERROR: ...
COMPACT_VIRTUAL_DISK_FLAG = Int32
COMPACT_VIRTUAL_DISK_FLAG_NONE: COMPACT_VIRTUAL_DISK_FLAG = 0
COMPACT_VIRTUAL_DISK_FLAG_NO_ZERO_SCAN: COMPACT_VIRTUAL_DISK_FLAG = 1
COMPACT_VIRTUAL_DISK_FLAG_NO_BLOCK_MOVES: COMPACT_VIRTUAL_DISK_FLAG = 2
class COMPACT_VIRTUAL_DISK_PARAMETERS(EasyCastStructure):
    Version: Windows.Win32.Storage.Vhd.COMPACT_VIRTUAL_DISK_VERSION
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Version1: _Version1_e__Struct
        class _Version1_e__Struct(EasyCastStructure):
            Reserved: UInt32
COMPACT_VIRTUAL_DISK_VERSION = Int32
COMPACT_VIRTUAL_DISK_VERSION_UNSPECIFIED: COMPACT_VIRTUAL_DISK_VERSION = 0
COMPACT_VIRTUAL_DISK_VERSION_1: COMPACT_VIRTUAL_DISK_VERSION = 1
CREATE_VIRTUAL_DISK_FLAG = Int32
CREATE_VIRTUAL_DISK_FLAG_NONE: CREATE_VIRTUAL_DISK_FLAG = 0
CREATE_VIRTUAL_DISK_FLAG_FULL_PHYSICAL_ALLOCATION: CREATE_VIRTUAL_DISK_FLAG = 1
CREATE_VIRTUAL_DISK_FLAG_PREVENT_WRITES_TO_SOURCE_DISK: CREATE_VIRTUAL_DISK_FLAG = 2
CREATE_VIRTUAL_DISK_FLAG_DO_NOT_COPY_METADATA_FROM_PARENT: CREATE_VIRTUAL_DISK_FLAG = 4
CREATE_VIRTUAL_DISK_FLAG_CREATE_BACKING_STORAGE: CREATE_VIRTUAL_DISK_FLAG = 8
CREATE_VIRTUAL_DISK_FLAG_USE_CHANGE_TRACKING_SOURCE_LIMIT: CREATE_VIRTUAL_DISK_FLAG = 16
CREATE_VIRTUAL_DISK_FLAG_PRESERVE_PARENT_CHANGE_TRACKING_STATE: CREATE_VIRTUAL_DISK_FLAG = 32
CREATE_VIRTUAL_DISK_FLAG_VHD_SET_USE_ORIGINAL_BACKING_STORAGE: CREATE_VIRTUAL_DISK_FLAG = 64
CREATE_VIRTUAL_DISK_FLAG_SPARSE_FILE: CREATE_VIRTUAL_DISK_FLAG = 128
CREATE_VIRTUAL_DISK_FLAG_PMEM_COMPATIBLE: CREATE_VIRTUAL_DISK_FLAG = 256
CREATE_VIRTUAL_DISK_FLAG_SUPPORT_COMPRESSED_VOLUMES: CREATE_VIRTUAL_DISK_FLAG = 512
CREATE_VIRTUAL_DISK_FLAG_SUPPORT_SPARSE_FILES_ANY_FS: CREATE_VIRTUAL_DISK_FLAG = 1024
class CREATE_VIRTUAL_DISK_PARAMETERS(EasyCastStructure):
    Version: Windows.Win32.Storage.Vhd.CREATE_VIRTUAL_DISK_VERSION
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Version1: _Version1_e__Struct
        Version2: _Version2_e__Struct
        Version3: _Version3_e__Struct
        Version4: _Version4_e__Struct
        class _Version1_e__Struct(EasyCastStructure):
            UniqueId: Guid
            MaximumSize: UInt64
            BlockSizeInBytes: UInt32
            SectorSizeInBytes: UInt32
            ParentPath: Windows.Win32.Foundation.PWSTR
            SourcePath: Windows.Win32.Foundation.PWSTR
        class _Version2_e__Struct(EasyCastStructure):
            UniqueId: Guid
            MaximumSize: UInt64
            BlockSizeInBytes: UInt32
            SectorSizeInBytes: UInt32
            PhysicalSectorSizeInBytes: UInt32
            ParentPath: Windows.Win32.Foundation.PWSTR
            SourcePath: Windows.Win32.Foundation.PWSTR
            OpenFlags: Windows.Win32.Storage.Vhd.OPEN_VIRTUAL_DISK_FLAG
            ParentVirtualStorageType: Windows.Win32.Storage.Vhd.VIRTUAL_STORAGE_TYPE
            SourceVirtualStorageType: Windows.Win32.Storage.Vhd.VIRTUAL_STORAGE_TYPE
            ResiliencyGuid: Guid
        class _Version3_e__Struct(EasyCastStructure):
            UniqueId: Guid
            MaximumSize: UInt64
            BlockSizeInBytes: UInt32
            SectorSizeInBytes: UInt32
            PhysicalSectorSizeInBytes: UInt32
            ParentPath: Windows.Win32.Foundation.PWSTR
            SourcePath: Windows.Win32.Foundation.PWSTR
            OpenFlags: Windows.Win32.Storage.Vhd.OPEN_VIRTUAL_DISK_FLAG
            ParentVirtualStorageType: Windows.Win32.Storage.Vhd.VIRTUAL_STORAGE_TYPE
            SourceVirtualStorageType: Windows.Win32.Storage.Vhd.VIRTUAL_STORAGE_TYPE
            ResiliencyGuid: Guid
            SourceLimitPath: Windows.Win32.Foundation.PWSTR
            BackingStorageType: Windows.Win32.Storage.Vhd.VIRTUAL_STORAGE_TYPE
        class _Version4_e__Struct(EasyCastStructure):
            UniqueId: Guid
            MaximumSize: UInt64
            BlockSizeInBytes: UInt32
            SectorSizeInBytes: UInt32
            PhysicalSectorSizeInBytes: UInt32
            ParentPath: Windows.Win32.Foundation.PWSTR
            SourcePath: Windows.Win32.Foundation.PWSTR
            OpenFlags: Windows.Win32.Storage.Vhd.OPEN_VIRTUAL_DISK_FLAG
            ParentVirtualStorageType: Windows.Win32.Storage.Vhd.VIRTUAL_STORAGE_TYPE
            SourceVirtualStorageType: Windows.Win32.Storage.Vhd.VIRTUAL_STORAGE_TYPE
            ResiliencyGuid: Guid
            SourceLimitPath: Windows.Win32.Foundation.PWSTR
            BackingStorageType: Windows.Win32.Storage.Vhd.VIRTUAL_STORAGE_TYPE
            PmemAddressAbstractionType: Guid
            DataAlignment: UInt64
CREATE_VIRTUAL_DISK_VERSION = Int32
CREATE_VIRTUAL_DISK_VERSION_UNSPECIFIED: CREATE_VIRTUAL_DISK_VERSION = 0
CREATE_VIRTUAL_DISK_VERSION_1: CREATE_VIRTUAL_DISK_VERSION = 1
CREATE_VIRTUAL_DISK_VERSION_2: CREATE_VIRTUAL_DISK_VERSION = 2
CREATE_VIRTUAL_DISK_VERSION_3: CREATE_VIRTUAL_DISK_VERSION = 3
CREATE_VIRTUAL_DISK_VERSION_4: CREATE_VIRTUAL_DISK_VERSION = 4
DELETE_SNAPSHOT_VHDSET_FLAG = Int32
DELETE_SNAPSHOT_VHDSET_FLAG_NONE: DELETE_SNAPSHOT_VHDSET_FLAG = 0
DELETE_SNAPSHOT_VHDSET_FLAG_PERSIST_RCT: DELETE_SNAPSHOT_VHDSET_FLAG = 1
class DELETE_SNAPSHOT_VHDSET_PARAMETERS(EasyCastStructure):
    Version: Windows.Win32.Storage.Vhd.DELETE_SNAPSHOT_VHDSET_VERSION
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Version1: _Version1_e__Struct
        class _Version1_e__Struct(EasyCastStructure):
            SnapshotId: Guid
DELETE_SNAPSHOT_VHDSET_VERSION = Int32
DELETE_SNAPSHOT_VHDSET_VERSION_UNSPECIFIED: DELETE_SNAPSHOT_VHDSET_VERSION = 0
DELETE_SNAPSHOT_VHDSET_VERSION_1: DELETE_SNAPSHOT_VHDSET_VERSION = 1
DEPENDENT_DISK_FLAG = Int32
DEPENDENT_DISK_FLAG_NONE: DEPENDENT_DISK_FLAG = 0
DEPENDENT_DISK_FLAG_MULT_BACKING_FILES: DEPENDENT_DISK_FLAG = 1
DEPENDENT_DISK_FLAG_FULLY_ALLOCATED: DEPENDENT_DISK_FLAG = 2
DEPENDENT_DISK_FLAG_READ_ONLY: DEPENDENT_DISK_FLAG = 4
DEPENDENT_DISK_FLAG_REMOTE: DEPENDENT_DISK_FLAG = 8
DEPENDENT_DISK_FLAG_SYSTEM_VOLUME: DEPENDENT_DISK_FLAG = 16
DEPENDENT_DISK_FLAG_SYSTEM_VOLUME_PARENT: DEPENDENT_DISK_FLAG = 32
DEPENDENT_DISK_FLAG_REMOVABLE: DEPENDENT_DISK_FLAG = 64
DEPENDENT_DISK_FLAG_NO_DRIVE_LETTER: DEPENDENT_DISK_FLAG = 128
DEPENDENT_DISK_FLAG_PARENT: DEPENDENT_DISK_FLAG = 256
DEPENDENT_DISK_FLAG_NO_HOST_DISK: DEPENDENT_DISK_FLAG = 512
DEPENDENT_DISK_FLAG_PERMANENT_LIFETIME: DEPENDENT_DISK_FLAG = 1024
DEPENDENT_DISK_FLAG_SUPPORT_COMPRESSED_VOLUMES: DEPENDENT_DISK_FLAG = 2048
DEPENDENT_DISK_FLAG_ALWAYS_ALLOW_SPARSE: DEPENDENT_DISK_FLAG = 4096
DEPENDENT_DISK_FLAG_SUPPORT_ENCRYPTED_FILES: DEPENDENT_DISK_FLAG = 8192
DETACH_VIRTUAL_DISK_FLAG = Int32
DETACH_VIRTUAL_DISK_FLAG_NONE: DETACH_VIRTUAL_DISK_FLAG = 0
EXPAND_VIRTUAL_DISK_FLAG = Int32
EXPAND_VIRTUAL_DISK_FLAG_NONE: EXPAND_VIRTUAL_DISK_FLAG = 0
EXPAND_VIRTUAL_DISK_FLAG_NOTIFY_CHANGE: EXPAND_VIRTUAL_DISK_FLAG = 1
class EXPAND_VIRTUAL_DISK_PARAMETERS(EasyCastStructure):
    Version: Windows.Win32.Storage.Vhd.EXPAND_VIRTUAL_DISK_VERSION
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Version1: _Version1_e__Struct
        class _Version1_e__Struct(EasyCastStructure):
            NewSize: UInt64
EXPAND_VIRTUAL_DISK_VERSION = Int32
EXPAND_VIRTUAL_DISK_VERSION_UNSPECIFIED: EXPAND_VIRTUAL_DISK_VERSION = 0
EXPAND_VIRTUAL_DISK_VERSION_1: EXPAND_VIRTUAL_DISK_VERSION = 1
FORK_VIRTUAL_DISK_FLAG = Int32
FORK_VIRTUAL_DISK_FLAG_NONE: FORK_VIRTUAL_DISK_FLAG = 0
FORK_VIRTUAL_DISK_FLAG_EXISTING_FILE: FORK_VIRTUAL_DISK_FLAG = 1
class FORK_VIRTUAL_DISK_PARAMETERS(EasyCastStructure):
    Version: Windows.Win32.Storage.Vhd.FORK_VIRTUAL_DISK_VERSION
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Version1: _Version1_e__Struct
        class _Version1_e__Struct(EasyCastStructure):
            ForkedVirtualDiskPath: Windows.Win32.Foundation.PWSTR
FORK_VIRTUAL_DISK_VERSION = Int32
FORK_VIRTUAL_DISK_VERSION_UNSPECIFIED: FORK_VIRTUAL_DISK_VERSION = 0
FORK_VIRTUAL_DISK_VERSION_1: FORK_VIRTUAL_DISK_VERSION = 1
GET_STORAGE_DEPENDENCY_FLAG = Int32
GET_STORAGE_DEPENDENCY_FLAG_NONE: GET_STORAGE_DEPENDENCY_FLAG = 0
GET_STORAGE_DEPENDENCY_FLAG_HOST_VOLUMES: GET_STORAGE_DEPENDENCY_FLAG = 1
GET_STORAGE_DEPENDENCY_FLAG_DISK_HANDLE: GET_STORAGE_DEPENDENCY_FLAG = 2
class GET_VIRTUAL_DISK_INFO(EasyCastStructure):
    Version: Windows.Win32.Storage.Vhd.GET_VIRTUAL_DISK_INFO_VERSION
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Size: _Size_e__Struct
        Identifier: Guid
        ParentLocation: _ParentLocation_e__Struct
        ParentIdentifier: Guid
        ParentTimestamp: UInt32
        VirtualStorageType: Windows.Win32.Storage.Vhd.VIRTUAL_STORAGE_TYPE
        ProviderSubtype: UInt32
        Is4kAligned: Windows.Win32.Foundation.BOOL
        IsLoaded: Windows.Win32.Foundation.BOOL
        PhysicalDisk: _PhysicalDisk_e__Struct
        VhdPhysicalSectorSize: UInt32
        SmallestSafeVirtualSize: UInt64
        FragmentationPercentage: UInt32
        VirtualDiskId: Guid
        ChangeTrackingState: _ChangeTrackingState_e__Struct
        class _Size_e__Struct(EasyCastStructure):
            VirtualSize: UInt64
            PhysicalSize: UInt64
            BlockSize: UInt32
            SectorSize: UInt32
        class _ParentLocation_e__Struct(EasyCastStructure):
            ParentResolved: Windows.Win32.Foundation.BOOL
            ParentLocationBuffer: Char * 1
        class _PhysicalDisk_e__Struct(EasyCastStructure):
            LogicalSectorSize: UInt32
            PhysicalSectorSize: UInt32
            IsRemote: Windows.Win32.Foundation.BOOL
        class _ChangeTrackingState_e__Struct(EasyCastStructure):
            Enabled: Windows.Win32.Foundation.BOOL
            NewerChanges: Windows.Win32.Foundation.BOOL
            MostRecentId: Char * 1
GET_VIRTUAL_DISK_INFO_VERSION = Int32
GET_VIRTUAL_DISK_INFO_UNSPECIFIED: GET_VIRTUAL_DISK_INFO_VERSION = 0
GET_VIRTUAL_DISK_INFO_SIZE: GET_VIRTUAL_DISK_INFO_VERSION = 1
GET_VIRTUAL_DISK_INFO_IDENTIFIER: GET_VIRTUAL_DISK_INFO_VERSION = 2
GET_VIRTUAL_DISK_INFO_PARENT_LOCATION: GET_VIRTUAL_DISK_INFO_VERSION = 3
GET_VIRTUAL_DISK_INFO_PARENT_IDENTIFIER: GET_VIRTUAL_DISK_INFO_VERSION = 4
GET_VIRTUAL_DISK_INFO_PARENT_TIMESTAMP: GET_VIRTUAL_DISK_INFO_VERSION = 5
GET_VIRTUAL_DISK_INFO_VIRTUAL_STORAGE_TYPE: GET_VIRTUAL_DISK_INFO_VERSION = 6
GET_VIRTUAL_DISK_INFO_PROVIDER_SUBTYPE: GET_VIRTUAL_DISK_INFO_VERSION = 7
GET_VIRTUAL_DISK_INFO_IS_4K_ALIGNED: GET_VIRTUAL_DISK_INFO_VERSION = 8
GET_VIRTUAL_DISK_INFO_PHYSICAL_DISK: GET_VIRTUAL_DISK_INFO_VERSION = 9
GET_VIRTUAL_DISK_INFO_VHD_PHYSICAL_SECTOR_SIZE: GET_VIRTUAL_DISK_INFO_VERSION = 10
GET_VIRTUAL_DISK_INFO_SMALLEST_SAFE_VIRTUAL_SIZE: GET_VIRTUAL_DISK_INFO_VERSION = 11
GET_VIRTUAL_DISK_INFO_FRAGMENTATION: GET_VIRTUAL_DISK_INFO_VERSION = 12
GET_VIRTUAL_DISK_INFO_IS_LOADED: GET_VIRTUAL_DISK_INFO_VERSION = 13
GET_VIRTUAL_DISK_INFO_VIRTUAL_DISK_ID: GET_VIRTUAL_DISK_INFO_VERSION = 14
GET_VIRTUAL_DISK_INFO_CHANGE_TRACKING_STATE: GET_VIRTUAL_DISK_INFO_VERSION = 15
MERGE_VIRTUAL_DISK_FLAG = Int32
MERGE_VIRTUAL_DISK_FLAG_NONE: MERGE_VIRTUAL_DISK_FLAG = 0
class MERGE_VIRTUAL_DISK_PARAMETERS(EasyCastStructure):
    Version: Windows.Win32.Storage.Vhd.MERGE_VIRTUAL_DISK_VERSION
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Version1: _Version1_e__Struct
        Version2: _Version2_e__Struct
        class _Version1_e__Struct(EasyCastStructure):
            MergeDepth: UInt32
        class _Version2_e__Struct(EasyCastStructure):
            MergeSourceDepth: UInt32
            MergeTargetDepth: UInt32
MERGE_VIRTUAL_DISK_VERSION = Int32
MERGE_VIRTUAL_DISK_VERSION_UNSPECIFIED: MERGE_VIRTUAL_DISK_VERSION = 0
MERGE_VIRTUAL_DISK_VERSION_1: MERGE_VIRTUAL_DISK_VERSION = 1
MERGE_VIRTUAL_DISK_VERSION_2: MERGE_VIRTUAL_DISK_VERSION = 2
MIRROR_VIRTUAL_DISK_FLAG = Int32
MIRROR_VIRTUAL_DISK_FLAG_NONE: MIRROR_VIRTUAL_DISK_FLAG = 0
MIRROR_VIRTUAL_DISK_FLAG_EXISTING_FILE: MIRROR_VIRTUAL_DISK_FLAG = 1
MIRROR_VIRTUAL_DISK_FLAG_SKIP_MIRROR_ACTIVATION: MIRROR_VIRTUAL_DISK_FLAG = 2
MIRROR_VIRTUAL_DISK_FLAG_ENABLE_SMB_COMPRESSION: MIRROR_VIRTUAL_DISK_FLAG = 4
MIRROR_VIRTUAL_DISK_FLAG_IS_LIVE_MIGRATION: MIRROR_VIRTUAL_DISK_FLAG = 8
class MIRROR_VIRTUAL_DISK_PARAMETERS(EasyCastStructure):
    Version: Windows.Win32.Storage.Vhd.MIRROR_VIRTUAL_DISK_VERSION
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Version1: _Version1_e__Struct
        class _Version1_e__Struct(EasyCastStructure):
            MirrorVirtualDiskPath: Windows.Win32.Foundation.PWSTR
MIRROR_VIRTUAL_DISK_VERSION = Int32
MIRROR_VIRTUAL_DISK_VERSION_UNSPECIFIED: MIRROR_VIRTUAL_DISK_VERSION = 0
MIRROR_VIRTUAL_DISK_VERSION_1: MIRROR_VIRTUAL_DISK_VERSION = 1
MODIFY_VHDSET_FLAG = Int32
MODIFY_VHDSET_FLAG_NONE: MODIFY_VHDSET_FLAG = 0
MODIFY_VHDSET_FLAG_WRITEABLE_SNAPSHOT: MODIFY_VHDSET_FLAG = 1
class MODIFY_VHDSET_PARAMETERS(EasyCastStructure):
    Version: Windows.Win32.Storage.Vhd.MODIFY_VHDSET_VERSION
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        SnapshotPath: _SnapshotPath_e__Struct
        SnapshotId: Guid
        DefaultFilePath: Windows.Win32.Foundation.PWSTR
        class _SnapshotPath_e__Struct(EasyCastStructure):
            SnapshotId: Guid
            SnapshotFilePath: Windows.Win32.Foundation.PWSTR
MODIFY_VHDSET_VERSION = Int32
MODIFY_VHDSET_UNSPECIFIED: MODIFY_VHDSET_VERSION = 0
MODIFY_VHDSET_SNAPSHOT_PATH: MODIFY_VHDSET_VERSION = 1
MODIFY_VHDSET_REMOVE_SNAPSHOT: MODIFY_VHDSET_VERSION = 2
MODIFY_VHDSET_DEFAULT_SNAPSHOT_PATH: MODIFY_VHDSET_VERSION = 3
OPEN_VIRTUAL_DISK_FLAG = Int32
OPEN_VIRTUAL_DISK_FLAG_NONE: OPEN_VIRTUAL_DISK_FLAG = 0
OPEN_VIRTUAL_DISK_FLAG_NO_PARENTS: OPEN_VIRTUAL_DISK_FLAG = 1
OPEN_VIRTUAL_DISK_FLAG_BLANK_FILE: OPEN_VIRTUAL_DISK_FLAG = 2
OPEN_VIRTUAL_DISK_FLAG_BOOT_DRIVE: OPEN_VIRTUAL_DISK_FLAG = 4
OPEN_VIRTUAL_DISK_FLAG_CACHED_IO: OPEN_VIRTUAL_DISK_FLAG = 8
OPEN_VIRTUAL_DISK_FLAG_CUSTOM_DIFF_CHAIN: OPEN_VIRTUAL_DISK_FLAG = 16
OPEN_VIRTUAL_DISK_FLAG_PARENT_CACHED_IO: OPEN_VIRTUAL_DISK_FLAG = 32
OPEN_VIRTUAL_DISK_FLAG_VHDSET_FILE_ONLY: OPEN_VIRTUAL_DISK_FLAG = 64
OPEN_VIRTUAL_DISK_FLAG_IGNORE_RELATIVE_PARENT_LOCATOR: OPEN_VIRTUAL_DISK_FLAG = 128
OPEN_VIRTUAL_DISK_FLAG_NO_WRITE_HARDENING: OPEN_VIRTUAL_DISK_FLAG = 256
OPEN_VIRTUAL_DISK_FLAG_SUPPORT_COMPRESSED_VOLUMES: OPEN_VIRTUAL_DISK_FLAG = 512
OPEN_VIRTUAL_DISK_FLAG_SUPPORT_SPARSE_FILES_ANY_FS: OPEN_VIRTUAL_DISK_FLAG = 1024
OPEN_VIRTUAL_DISK_FLAG_SUPPORT_ENCRYPTED_FILES: OPEN_VIRTUAL_DISK_FLAG = 2048
class OPEN_VIRTUAL_DISK_PARAMETERS(EasyCastStructure):
    Version: Windows.Win32.Storage.Vhd.OPEN_VIRTUAL_DISK_VERSION
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Version1: _Version1_e__Struct
        Version2: _Version2_e__Struct
        Version3: _Version3_e__Struct
        class _Version1_e__Struct(EasyCastStructure):
            RWDepth: UInt32
        class _Version2_e__Struct(EasyCastStructure):
            GetInfoOnly: Windows.Win32.Foundation.BOOL
            ReadOnly: Windows.Win32.Foundation.BOOL
            ResiliencyGuid: Guid
        class _Version3_e__Struct(EasyCastStructure):
            GetInfoOnly: Windows.Win32.Foundation.BOOL
            ReadOnly: Windows.Win32.Foundation.BOOL
            ResiliencyGuid: Guid
            SnapshotId: Guid
OPEN_VIRTUAL_DISK_VERSION = Int32
OPEN_VIRTUAL_DISK_VERSION_UNSPECIFIED: OPEN_VIRTUAL_DISK_VERSION = 0
OPEN_VIRTUAL_DISK_VERSION_1: OPEN_VIRTUAL_DISK_VERSION = 1
OPEN_VIRTUAL_DISK_VERSION_2: OPEN_VIRTUAL_DISK_VERSION = 2
OPEN_VIRTUAL_DISK_VERSION_3: OPEN_VIRTUAL_DISK_VERSION = 3
QUERY_CHANGES_VIRTUAL_DISK_FLAG = Int32
QUERY_CHANGES_VIRTUAL_DISK_FLAG_NONE: QUERY_CHANGES_VIRTUAL_DISK_FLAG = 0
class QUERY_CHANGES_VIRTUAL_DISK_RANGE(EasyCastStructure):
    ByteOffset: UInt64
    ByteLength: UInt64
    Reserved: UInt64
RAW_SCSI_VIRTUAL_DISK_FLAG = Int32
RAW_SCSI_VIRTUAL_DISK_FLAG_NONE: RAW_SCSI_VIRTUAL_DISK_FLAG = 0
class RAW_SCSI_VIRTUAL_DISK_PARAMETERS(EasyCastStructure):
    Version: Windows.Win32.Storage.Vhd.RAW_SCSI_VIRTUAL_DISK_VERSION
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Version1: _Version1_e__Struct
        class _Version1_e__Struct(EasyCastStructure):
            RSVDHandle: Windows.Win32.Foundation.BOOL
            DataIn: Byte
            CdbLength: Byte
            SenseInfoLength: Byte
            SrbFlags: UInt32
            DataTransferLength: UInt32
            DataBuffer: c_void_p
            SenseInfo: POINTER(Byte)
            Cdb: POINTER(Byte)
class RAW_SCSI_VIRTUAL_DISK_RESPONSE(EasyCastStructure):
    Version: Windows.Win32.Storage.Vhd.RAW_SCSI_VIRTUAL_DISK_VERSION
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Version1: _Version1_e__Struct
        class _Version1_e__Struct(EasyCastStructure):
            ScsiStatus: Byte
            SenseInfoLength: Byte
            DataTransferLength: UInt32
RAW_SCSI_VIRTUAL_DISK_VERSION = Int32
RAW_SCSI_VIRTUAL_DISK_VERSION_UNSPECIFIED: RAW_SCSI_VIRTUAL_DISK_VERSION = 0
RAW_SCSI_VIRTUAL_DISK_VERSION_1: RAW_SCSI_VIRTUAL_DISK_VERSION = 1
RESIZE_VIRTUAL_DISK_FLAG = Int32
RESIZE_VIRTUAL_DISK_FLAG_NONE: RESIZE_VIRTUAL_DISK_FLAG = 0
RESIZE_VIRTUAL_DISK_FLAG_ALLOW_UNSAFE_VIRTUAL_SIZE: RESIZE_VIRTUAL_DISK_FLAG = 1
RESIZE_VIRTUAL_DISK_FLAG_RESIZE_TO_SMALLEST_SAFE_VIRTUAL_SIZE: RESIZE_VIRTUAL_DISK_FLAG = 2
class RESIZE_VIRTUAL_DISK_PARAMETERS(EasyCastStructure):
    Version: Windows.Win32.Storage.Vhd.RESIZE_VIRTUAL_DISK_VERSION
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Version1: _Version1_e__Struct
        class _Version1_e__Struct(EasyCastStructure):
            NewSize: UInt64
RESIZE_VIRTUAL_DISK_VERSION = Int32
RESIZE_VIRTUAL_DISK_VERSION_UNSPECIFIED: RESIZE_VIRTUAL_DISK_VERSION = 0
RESIZE_VIRTUAL_DISK_VERSION_1: RESIZE_VIRTUAL_DISK_VERSION = 1
class SET_VIRTUAL_DISK_INFO(EasyCastStructure):
    Version: Windows.Win32.Storage.Vhd.SET_VIRTUAL_DISK_INFO_VERSION
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        ParentFilePath: Windows.Win32.Foundation.PWSTR
        UniqueIdentifier: Guid
        ParentPathWithDepthInfo: _ParentPathWithDepthInfo_e__Struct
        VhdPhysicalSectorSize: UInt32
        VirtualDiskId: Guid
        ChangeTrackingEnabled: Windows.Win32.Foundation.BOOL
        ParentLocator: _ParentLocator_e__Struct
        class _ParentPathWithDepthInfo_e__Struct(EasyCastStructure):
            ChildDepth: UInt32
            ParentFilePath: Windows.Win32.Foundation.PWSTR
        class _ParentLocator_e__Struct(EasyCastStructure):
            LinkageId: Guid
            ParentFilePath: Windows.Win32.Foundation.PWSTR
SET_VIRTUAL_DISK_INFO_VERSION = Int32
SET_VIRTUAL_DISK_INFO_UNSPECIFIED: SET_VIRTUAL_DISK_INFO_VERSION = 0
SET_VIRTUAL_DISK_INFO_PARENT_PATH: SET_VIRTUAL_DISK_INFO_VERSION = 1
SET_VIRTUAL_DISK_INFO_IDENTIFIER: SET_VIRTUAL_DISK_INFO_VERSION = 2
SET_VIRTUAL_DISK_INFO_PARENT_PATH_WITH_DEPTH: SET_VIRTUAL_DISK_INFO_VERSION = 3
SET_VIRTUAL_DISK_INFO_PHYSICAL_SECTOR_SIZE: SET_VIRTUAL_DISK_INFO_VERSION = 4
SET_VIRTUAL_DISK_INFO_VIRTUAL_DISK_ID: SET_VIRTUAL_DISK_INFO_VERSION = 5
SET_VIRTUAL_DISK_INFO_CHANGE_TRACKING_STATE: SET_VIRTUAL_DISK_INFO_VERSION = 6
SET_VIRTUAL_DISK_INFO_PARENT_LOCATOR: SET_VIRTUAL_DISK_INFO_VERSION = 7
class STORAGE_DEPENDENCY_INFO(EasyCastStructure):
    Version: Windows.Win32.Storage.Vhd.STORAGE_DEPENDENCY_INFO_VERSION
    NumberEntries: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Version1Entries: Windows.Win32.Storage.Vhd.STORAGE_DEPENDENCY_INFO_TYPE_1 * 1
        Version2Entries: Windows.Win32.Storage.Vhd.STORAGE_DEPENDENCY_INFO_TYPE_2 * 1
class STORAGE_DEPENDENCY_INFO_TYPE_1(EasyCastStructure):
    DependencyTypeFlags: Windows.Win32.Storage.Vhd.DEPENDENT_DISK_FLAG
    ProviderSpecificFlags: UInt32
    VirtualStorageType: Windows.Win32.Storage.Vhd.VIRTUAL_STORAGE_TYPE
class STORAGE_DEPENDENCY_INFO_TYPE_2(EasyCastStructure):
    DependencyTypeFlags: Windows.Win32.Storage.Vhd.DEPENDENT_DISK_FLAG
    ProviderSpecificFlags: UInt32
    VirtualStorageType: Windows.Win32.Storage.Vhd.VIRTUAL_STORAGE_TYPE
    AncestorLevel: UInt32
    DependencyDeviceName: Windows.Win32.Foundation.PWSTR
    HostVolumeName: Windows.Win32.Foundation.PWSTR
    DependentVolumeName: Windows.Win32.Foundation.PWSTR
    DependentVolumeRelativePath: Windows.Win32.Foundation.PWSTR
STORAGE_DEPENDENCY_INFO_VERSION = Int32
STORAGE_DEPENDENCY_INFO_VERSION_UNSPECIFIED: STORAGE_DEPENDENCY_INFO_VERSION = 0
STORAGE_DEPENDENCY_INFO_VERSION_1: STORAGE_DEPENDENCY_INFO_VERSION = 1
STORAGE_DEPENDENCY_INFO_VERSION_2: STORAGE_DEPENDENCY_INFO_VERSION = 2
TAKE_SNAPSHOT_VHDSET_FLAG = Int32
TAKE_SNAPSHOT_VHDSET_FLAG_NONE: TAKE_SNAPSHOT_VHDSET_FLAG = 0
TAKE_SNAPSHOT_VHDSET_FLAG_WRITEABLE: TAKE_SNAPSHOT_VHDSET_FLAG = 1
class TAKE_SNAPSHOT_VHDSET_PARAMETERS(EasyCastStructure):
    Version: Windows.Win32.Storage.Vhd.TAKE_SNAPSHOT_VHDSET_VERSION
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Version1: _Version1_e__Struct
        class _Version1_e__Struct(EasyCastStructure):
            SnapshotId: Guid
TAKE_SNAPSHOT_VHDSET_VERSION = Int32
TAKE_SNAPSHOT_VHDSET_VERSION_UNSPECIFIED: TAKE_SNAPSHOT_VHDSET_VERSION = 0
TAKE_SNAPSHOT_VHDSET_VERSION_1: TAKE_SNAPSHOT_VHDSET_VERSION = 1
VIRTUAL_DISK_ACCESS_MASK = Int32
VIRTUAL_DISK_ACCESS_NONE: VIRTUAL_DISK_ACCESS_MASK = 0
VIRTUAL_DISK_ACCESS_ATTACH_RO: VIRTUAL_DISK_ACCESS_MASK = 65536
VIRTUAL_DISK_ACCESS_ATTACH_RW: VIRTUAL_DISK_ACCESS_MASK = 131072
VIRTUAL_DISK_ACCESS_DETACH: VIRTUAL_DISK_ACCESS_MASK = 262144
VIRTUAL_DISK_ACCESS_GET_INFO: VIRTUAL_DISK_ACCESS_MASK = 524288
VIRTUAL_DISK_ACCESS_CREATE: VIRTUAL_DISK_ACCESS_MASK = 1048576
VIRTUAL_DISK_ACCESS_METAOPS: VIRTUAL_DISK_ACCESS_MASK = 2097152
VIRTUAL_DISK_ACCESS_READ: VIRTUAL_DISK_ACCESS_MASK = 851968
VIRTUAL_DISK_ACCESS_ALL: VIRTUAL_DISK_ACCESS_MASK = 4128768
VIRTUAL_DISK_ACCESS_WRITABLE: VIRTUAL_DISK_ACCESS_MASK = 3276800
class VIRTUAL_DISK_PROGRESS(EasyCastStructure):
    OperationStatus: UInt32
    CurrentValue: UInt64
    CompletionValue: UInt64
class VIRTUAL_STORAGE_TYPE(EasyCastStructure):
    DeviceId: UInt32
    VendorId: Guid
make_head(_module, 'APPLY_SNAPSHOT_VHDSET_PARAMETERS')
make_head(_module, 'ATTACH_VIRTUAL_DISK_PARAMETERS')
make_head(_module, 'COMPACT_VIRTUAL_DISK_PARAMETERS')
make_head(_module, 'CREATE_VIRTUAL_DISK_PARAMETERS')
make_head(_module, 'DELETE_SNAPSHOT_VHDSET_PARAMETERS')
make_head(_module, 'EXPAND_VIRTUAL_DISK_PARAMETERS')
make_head(_module, 'FORK_VIRTUAL_DISK_PARAMETERS')
make_head(_module, 'GET_VIRTUAL_DISK_INFO')
make_head(_module, 'MERGE_VIRTUAL_DISK_PARAMETERS')
make_head(_module, 'MIRROR_VIRTUAL_DISK_PARAMETERS')
make_head(_module, 'MODIFY_VHDSET_PARAMETERS')
make_head(_module, 'OPEN_VIRTUAL_DISK_PARAMETERS')
make_head(_module, 'QUERY_CHANGES_VIRTUAL_DISK_RANGE')
make_head(_module, 'RAW_SCSI_VIRTUAL_DISK_PARAMETERS')
make_head(_module, 'RAW_SCSI_VIRTUAL_DISK_RESPONSE')
make_head(_module, 'RESIZE_VIRTUAL_DISK_PARAMETERS')
make_head(_module, 'SET_VIRTUAL_DISK_INFO')
make_head(_module, 'STORAGE_DEPENDENCY_INFO')
make_head(_module, 'STORAGE_DEPENDENCY_INFO_TYPE_1')
make_head(_module, 'STORAGE_DEPENDENCY_INFO_TYPE_2')
make_head(_module, 'TAKE_SNAPSHOT_VHDSET_PARAMETERS')
make_head(_module, 'VIRTUAL_DISK_PROGRESS')
make_head(_module, 'VIRTUAL_STORAGE_TYPE')
