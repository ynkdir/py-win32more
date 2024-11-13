from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Devices.Dvd
import win32more.Windows.Win32.Foundation
class AACS_BINDING_NONCE(Structure):
    BindingNonce: Byte * 16
    MAC: Byte * 16
class AACS_CERTIFICATE(Structure):
    Nonce: Byte * 20
    Certificate: Byte * 92
class AACS_CHALLENGE_KEY(Structure):
    EllipticCurvePoint: Byte * 40
    Signature: Byte * 40
class AACS_MEDIA_ID(Structure):
    MediaID: Byte * 16
    MAC: Byte * 16
class AACS_READ_BINDING_NONCE(Structure):
    SessionId: UInt32
    NumberOfSectors: UInt32
    StartLba: UInt64
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Handle: win32more.Windows.Win32.Foundation.HANDLE
        ForceStructureLengthToMatch64bit: UInt64
class AACS_SEND_CERTIFICATE(Structure):
    SessionId: UInt32
    Certificate: win32more.Windows.Win32.Devices.Dvd.AACS_CERTIFICATE
class AACS_SEND_CHALLENGE_KEY(Structure):
    SessionId: UInt32
    ChallengeKey: win32more.Windows.Win32.Devices.Dvd.AACS_CHALLENGE_KEY
class AACS_SERIAL_NUMBER(Structure):
    PrerecordedSerialNumber: Byte * 16
    MAC: Byte * 16
class AACS_VOLUME_ID(Structure):
    VolumeID: Byte * 16
    MAC: Byte * 16
IOCTL_DVD_BASE: Int32 = 51
IOCTL_DVD_START_SESSION: UInt32 = 3362816
IOCTL_DVD_READ_KEY: UInt32 = 3362820
IOCTL_DVD_SEND_KEY: UInt32 = 3362824
IOCTL_DVD_END_SESSION: UInt32 = 3362828
IOCTL_DVD_SET_READ_AHEAD: UInt32 = 3362832
IOCTL_DVD_GET_REGION: UInt32 = 3362836
IOCTL_DVD_SEND_KEY2: UInt32 = 3395608
IOCTL_AACS_READ_MEDIA_KEY_BLOCK_SIZE: UInt32 = 3363008
IOCTL_AACS_READ_MEDIA_KEY_BLOCK: UInt32 = 3363012
IOCTL_AACS_START_SESSION: UInt32 = 3363016
IOCTL_AACS_END_SESSION: UInt32 = 3363020
IOCTL_AACS_SEND_CERTIFICATE: UInt32 = 3363024
IOCTL_AACS_GET_CERTIFICATE: UInt32 = 3363028
IOCTL_AACS_GET_CHALLENGE_KEY: UInt32 = 3363032
IOCTL_AACS_SEND_CHALLENGE_KEY: UInt32 = 3363036
IOCTL_AACS_READ_VOLUME_ID: UInt32 = 3363040
IOCTL_AACS_READ_SERIAL_NUMBER: UInt32 = 3363044
IOCTL_AACS_READ_MEDIA_ID: UInt32 = 3363048
IOCTL_AACS_READ_BINDING_NONCE: UInt32 = 3363052
IOCTL_AACS_GENERATE_BINDING_NONCE: UInt32 = 3395824
IOCTL_DVD_READ_STRUCTURE: UInt32 = 3363136
IOCTL_STORAGE_SET_READ_AHEAD: UInt32 = 2966528
DVD_CGMS_RESERVED_MASK: UInt32 = 120
DVD_CGMS_COPY_PROTECT_MASK: UInt32 = 24
DVD_CGMS_COPY_PERMITTED: UInt32 = 0
DVD_CGMS_COPY_ONCE: UInt32 = 16
DVD_CGMS_NO_COPY: UInt32 = 24
DVD_COPYRIGHT_MASK: UInt32 = 64
DVD_NOT_COPYRIGHTED: UInt32 = 0
DVD_COPYRIGHTED: UInt32 = 64
DVD_SECTOR_PROTECT_MASK: UInt32 = 32
DVD_SECTOR_NOT_PROTECTED: UInt32 = 0
DVD_SECTOR_PROTECTED: UInt32 = 32
class BD_DISC_WRITE_PROTECT_PAC(Structure):
    Header: win32more.Windows.Win32.Devices.Dvd.BD_PAC_HEADER
    KnownPACEntireDiscFlags: Byte
    Reserved1: Byte * 3
    WriteProtectControlByte: Byte
    Reserved2: Byte * 7
    WriteProtectPassword: Byte * 32
class BD_PAC_HEADER(Structure):
    PACId: Byte * 3
    PACFormatNumber: Byte
    PACUpdateCount: Byte * 4
    UnknownPACRules: Byte * 4
    UnkownPACEntireDiscFlag: Byte
    Reserved1: Byte * 2
    NumberOfSegments: Byte
    Segments: Byte * 256
    Reserved2: Byte * 112
DISC_CONTROL_BLOCK_TYPE = Int32
FormattingDiscControlBlock: win32more.Windows.Win32.Devices.Dvd.DISC_CONTROL_BLOCK_TYPE = 1178878720
WriteInhibitDiscControlBlock: win32more.Windows.Win32.Devices.Dvd.DISC_CONTROL_BLOCK_TYPE = 1464091392
SessionInfoDiscControlBlock: win32more.Windows.Win32.Devices.Dvd.DISC_CONTROL_BLOCK_TYPE = 1396982528
DiscControlBlockList: win32more.Windows.Win32.Devices.Dvd.DISC_CONTROL_BLOCK_TYPE = -1
class DVD_ASF(Structure):
    Reserved0: Byte * 3
    SuccessFlag: Annotated[Byte, 1]
    Reserved1: Annotated[Byte, 7]
class DVD_BCA_DESCRIPTOR(Structure):
    BCAInformation: Byte * 1
class DVD_BD_SPARE_AREA_INFORMATION(Structure):
    Reserved1: Byte * 4
    NumberOfFreeSpareBlocks: Byte * 4
    NumberOfAllocatedSpareBlocks: Byte * 4
class DVD_COPYRIGHT_DESCRIPTOR(Structure):
    CopyrightProtectionType: Byte
    RegionManagementInformation: Byte
    Reserved: UInt16
    _pack_ = 1
class DVD_COPYRIGHT_MANAGEMENT_DESCRIPTOR(Structure):
    Anonymous: _Anonymous_e__Union
    Reserved0: Byte * 3
    class _Anonymous_e__Union(Union):
        Dvdrom: _Dvdrom_e__Struct
        DvdRecordable_Version1: _DvdRecordable_Version1_e__Struct
        Dvdram: _Dvdram_e__Struct
        DvdRecordable: _DvdRecordable_e__Struct
        CPR_MAI: Byte
        class _Dvdrom_e__Struct(Structure):
            CopyProtectionMode: Annotated[Byte, 4]
            ContentGenerationManagementSystem: Annotated[Byte, 2]
            CopyProtectedSector: Annotated[Byte, 1]
            CopyProtectedMaterial: Annotated[Byte, 1]
        class _DvdRecordable_Version1_e__Struct(Structure):
            Reserved0001: Annotated[Byte, 4]
            ContentGenerationManagementSystem: Annotated[Byte, 2]
            Reserved0002: Annotated[Byte, 1]
            CopyProtectedMaterial: Annotated[Byte, 1]
        class _Dvdram_e__Struct(Structure):
            Reserved0003: Byte
        class _DvdRecordable_e__Struct(Structure):
            Reserved0004: Annotated[Byte, 2]
            ADP_TY: Annotated[Byte, 2]
            Reserved0005: Annotated[Byte, 4]
class DVD_COPY_PROTECT_KEY(Structure):
    KeyLength: UInt32
    SessionId: UInt32
    KeyType: win32more.Windows.Win32.Devices.Dvd.DVD_KEY_TYPE
    KeyFlags: UInt32
    Parameters: _Parameters_e__Union
    KeyData: Byte * 1
    _pack_ = 1
    class _Parameters_e__Union(Union):
        FileHandle: win32more.Windows.Win32.Foundation.HANDLE
        TitleOffset: Int64
        _pack_ = 1
class DVD_DESCRIPTOR_HEADER(Structure):
    Length: UInt16
    Reserved: Byte * 2
    Data: Byte * 1
    _pack_ = 1
class DVD_DISC_CONTROL_BLOCK_HEADER(Structure):
    ContentDescriptor: Byte * 4
    ProhibitedActions: _ProhibitedActions_e__Union
    VendorId: Byte * 32
    class _ProhibitedActions_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        AsByte: Byte * 4
        class _Anonymous_e__Struct(Structure):
            ReservedDoNotUse_UseAsByteInstead_0: Byte * 3
            RecordingWithinTheUserDataArea: Annotated[Byte, 1]
            ReadingDiscControlBlocks: Annotated[Byte, 1]
            FormattingTheMedium: Annotated[Byte, 1]
            ModificationOfThisDiscControlBlock: Annotated[Byte, 1]
            ReservedDoNotUse_UseAsByteInstead_1: Annotated[Byte, 4]
class DVD_DISC_CONTROL_BLOCK_LIST(Structure):
    header: win32more.Windows.Win32.Devices.Dvd.DVD_DISC_CONTROL_BLOCK_HEADER
    Reserved0: Byte
    ReadabldDCBs: Byte
    Reserved1: Byte
    WritableDCBs: Byte
    Dcbs: win32more.Windows.Win32.Devices.Dvd.DVD_DISC_CONTROL_BLOCK_LIST_DCB * 1
class DVD_DISC_CONTROL_BLOCK_LIST_DCB(Structure):
    DcbIdentifier: Byte * 4
class DVD_DISC_CONTROL_BLOCK_SESSION(Structure):
    header: win32more.Windows.Win32.Devices.Dvd.DVD_DISC_CONTROL_BLOCK_HEADER
    SessionNumber: Byte * 2
    Reserved0: Byte * 22
    DiscID: Byte * 32
    Reserved1: Byte * 32
    SessionItem: win32more.Windows.Win32.Devices.Dvd.DVD_DISC_CONTROL_BLOCK_SESSION_ITEM * 504
    Reserved2: Byte * 24576
class DVD_DISC_CONTROL_BLOCK_SESSION_ITEM(Structure):
    AsByte: Byte * 16
class DVD_DISC_CONTROL_BLOCK_WRITE_INHIBIT(Structure):
    header: win32more.Windows.Win32.Devices.Dvd.DVD_DISC_CONTROL_BLOCK_HEADER
    UpdateCount: Byte * 4
    WriteProtectActions: _WriteProtectActions_e__Union
    Reserved0: Byte * 16
    UpdatePassword: Byte * 32
    Reserved1: Byte * 32672
    class _WriteProtectActions_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        AsByte: Byte * 4
        class _Anonymous_e__Struct(Structure):
            ReservedDoNotUse_UseAsByteInstead_0: Byte * 3
            WriteProtectStatus: Annotated[Byte, 2]
            ReservedDoNotUse_UseAsByteInstead_1: Annotated[Byte, 5]
            UpdateRequiresPassword: Annotated[Byte, 1]
class DVD_DISK_KEY_DESCRIPTOR(Structure):
    DiskKeyData: Byte * 2048
class DVD_DUAL_LAYER_JUMP_INTERVAL_SIZE(Structure):
    Reserved1: Byte * 4
    JumpIntervalSize: Byte * 4
class DVD_DUAL_LAYER_MANUAL_LAYER_JUMP(Structure):
    Reserved1: Byte * 4
    ManualJumpLayerAddress: Byte * 4
class DVD_DUAL_LAYER_MIDDLE_ZONE_START_ADDRESS(Structure):
    Reserved0: Annotated[Byte, 7]
    InitStatus: Annotated[Byte, 1]
    Reserved1: Byte * 3
    ShiftedMiddleAreaStartAddress: Byte * 4
class DVD_DUAL_LAYER_RECORDING_INFORMATION(Structure):
    Reserved0: Annotated[Byte, 7]
    Layer0SectorsImmutable: Annotated[Byte, 1]
    Reserved1: Byte * 3
    Layer0Sectors: Byte * 4
class DVD_DUAL_LAYER_REMAPPING_INFORMATION(Structure):
    Reserved1: Byte * 4
    RemappingAddress: Byte * 4
class DVD_FULL_LAYER_DESCRIPTOR(Structure):
    commonHeader: win32more.Windows.Win32.Devices.Dvd.DVD_LAYER_DESCRIPTOR
    MediaSpecific: Byte * 2031
DVD_KEY_TYPE = Int32
DvdChallengeKey: win32more.Windows.Win32.Devices.Dvd.DVD_KEY_TYPE = 1
DvdBusKey1: win32more.Windows.Win32.Devices.Dvd.DVD_KEY_TYPE = 2
DvdBusKey2: win32more.Windows.Win32.Devices.Dvd.DVD_KEY_TYPE = 3
DvdTitleKey: win32more.Windows.Win32.Devices.Dvd.DVD_KEY_TYPE = 4
DvdAsf: win32more.Windows.Win32.Devices.Dvd.DVD_KEY_TYPE = 5
DvdSetRpcKey: win32more.Windows.Win32.Devices.Dvd.DVD_KEY_TYPE = 6
DvdGetRpcKey: win32more.Windows.Win32.Devices.Dvd.DVD_KEY_TYPE = 8
DvdDiskKey: win32more.Windows.Win32.Devices.Dvd.DVD_KEY_TYPE = 128
DvdInvalidateAGID: win32more.Windows.Win32.Devices.Dvd.DVD_KEY_TYPE = 63
class DVD_LAYER_DESCRIPTOR(Structure):
    BookVersion: Annotated[Byte, 4]
    BookType: Annotated[Byte, 4]
    MinimumRate: Annotated[Byte, 4]
    DiskSize: Annotated[Byte, 4]
    LayerType: Annotated[Byte, 4]
    TrackPath: Annotated[Byte, 1]
    NumberOfLayers: Annotated[Byte, 2]
    Reserved1: Annotated[Byte, 1]
    TrackDensity: Annotated[Byte, 4]
    LinearDensity: Annotated[Byte, 4]
    StartingDataSector: UInt32
    EndDataSector: UInt32
    EndLayerZeroSector: UInt32
    Reserved5: Annotated[Byte, 7]
    BCAFlag: Annotated[Byte, 1]
    _pack_ = 1
class DVD_LIST_OF_RECOGNIZED_FORMAT_LAYERS(Structure):
    TypeCodeOfFormatLayer: Byte * 2
class DVD_LIST_OF_RECOGNIZED_FORMAT_LAYERS_TYPE_CODE(Structure):
    NumberOfRecognizedFormatLayers: Byte
    OnlineFormatlayer: Annotated[Byte, 2]
    Reserved1: Annotated[Byte, 2]
    DefaultFormatLayer: Annotated[Byte, 2]
    Reserved2: Annotated[Byte, 2]
class DVD_MANUFACTURER_DESCRIPTOR(Structure):
    ManufacturingInformation: Byte * 2048
class DVD_PRERECORDED_INFORMATION(Structure):
    FieldID_1: Byte
    DiscApplicationCode: Byte
    DiscPhysicalCode: Byte
    LastAddressOfDataRecordableArea: Byte * 3
    ExtensionCode: Annotated[Byte, 4]
    PartVers1on: Annotated[Byte, 4]
    Reserved0: Byte
    FieldID_2: Byte
    OpcSuggestedCode: Byte
    WavelengthCode: Byte
    WriteStrategyCode: Byte * 4
    Reserved2: Byte
    FieldID_3: Byte
    ManufacturerId_3: Byte * 6
    Reserved3: Byte
    FieldID_4: Byte
    ManufacturerId_4: Byte * 6
    Reserved4: Byte
    FieldID_5: Byte
    ManufacturerId_5: Byte * 6
    Reserved5: Byte
    Reserved99: Byte * 24
class DVD_RAM_MEDIUM_STATUS(Structure):
    Reserved0: Annotated[Byte, 1]
    PersistentWriteProtect: Annotated[Byte, 1]
    CartridgeWriteProtect: Annotated[Byte, 1]
    MediaSpecificWriteInhibit: Annotated[Byte, 1]
    Reserved1: Annotated[Byte, 2]
    CartridgeNotSealed: Annotated[Byte, 1]
    MediaInCartridge: Annotated[Byte, 1]
    DiscTypeIdentification: Byte
    Reserved2: Byte
    MediaSpecificWriteInhibitInformation: Byte
class DVD_RAM_RECORDING_TYPE(Structure):
    Reserved0: Annotated[Byte, 4]
    RealTimeData: Annotated[Byte, 1]
    Reserved1: Annotated[Byte, 3]
    Reserved2: Byte * 3
class DVD_RAM_SPARE_AREA_INFORMATION(Structure):
    FreePrimarySpareSectors: Byte * 4
    FreeSupplementalSpareSectors: Byte * 4
    AllocatedSupplementalSpareSectors: Byte * 4
class DVD_READ_STRUCTURE(Structure):
    BlockByteOffset: Int64
    Format: win32more.Windows.Win32.Devices.Dvd.DVD_STRUCTURE_FORMAT
    SessionId: UInt32
    LayerNumber: Byte
    _pack_ = 1
class DVD_RECORDING_MANAGEMENT_AREA_DATA(Structure):
    LastRecordedRMASectorNumber: Byte * 4
    RMDBytes: Byte * 1
class DVD_REGION(Structure):
    CopySystem: Byte
    RegionData: Byte
    SystemRegion: Byte
    ResetCount: Byte
class DVD_RPC_KEY(Structure):
    UserResetsAvailable: Annotated[Byte, 3]
    ManufacturerResetsAvailable: Annotated[Byte, 3]
    TypeCode: Annotated[Byte, 2]
    RegionMask: Byte
    RpcScheme: Byte
    Reserved02: Byte
class DVD_SET_RPC_KEY(Structure):
    PreferredDriveRegionCode: Byte
    Reserved: Byte * 3
DVD_STRUCTURE_FORMAT = Int32
DvdPhysicalDescriptor: win32more.Windows.Win32.Devices.Dvd.DVD_STRUCTURE_FORMAT = 0
DvdCopyrightDescriptor: win32more.Windows.Win32.Devices.Dvd.DVD_STRUCTURE_FORMAT = 1
DvdDiskKeyDescriptor: win32more.Windows.Win32.Devices.Dvd.DVD_STRUCTURE_FORMAT = 2
DvdBCADescriptor: win32more.Windows.Win32.Devices.Dvd.DVD_STRUCTURE_FORMAT = 3
DvdManufacturerDescriptor: win32more.Windows.Win32.Devices.Dvd.DVD_STRUCTURE_FORMAT = 4
DvdMaxDescriptor: win32more.Windows.Win32.Devices.Dvd.DVD_STRUCTURE_FORMAT = 5
class DVD_STRUCTURE_LIST_ENTRY(Structure):
    FormatCode: Byte
    Reserved0: Annotated[Byte, 6]
    Readable: Annotated[Byte, 1]
    Sendable: Annotated[Byte, 1]
    FormatLength: Byte * 2
class DVD_UNIQUE_DISC_IDENTIFIER(Structure):
    Reserved0: Byte * 2
    RandomNumber: Byte * 2
    Year: Byte * 4
    Month: Byte * 2
    Day: Byte * 2
    Hour: Byte * 2
    Minute: Byte * 2
    Second: Byte * 2
class DVD_WRITE_PROTECTION_STATUS(Structure):
    SoftwareWriteProtectUntilPowerdown: Annotated[Byte, 1]
    MediaPersistentWriteProtect: Annotated[Byte, 1]
    CartridgeWriteProtect: Annotated[Byte, 1]
    MediaSpecificWriteProtect: Annotated[Byte, 1]
    Reserved0: Annotated[Byte, 4]
    Reserved1: Byte * 3
class HD_DVD_R_MEDIUM_STATUS(Structure):
    ExtendedTestZone: Annotated[Byte, 1]
    Reserved1: Annotated[Byte, 7]
    NumberOfRemainingRMDsInRDZ: Byte
    NumberOfRemainingRMDsInCurrentRMZ: Byte * 2
class STORAGE_SET_READ_AHEAD(Structure):
    TriggerAddress: Int64
    TargetAddress: Int64
    _pack_ = 1


make_ready(__name__)
