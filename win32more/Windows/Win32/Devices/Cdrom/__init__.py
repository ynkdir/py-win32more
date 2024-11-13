from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Devices.Cdrom
import win32more.Windows.Win32.Foundation
IOCTL_CDROM_BASE: Int32 = 2
IOCTL_CDROM_UNLOAD_DRIVER: UInt32 = 151560
IOCTL_CDROM_READ_TOC: UInt32 = 147456
IOCTL_CDROM_SEEK_AUDIO_MSF: UInt32 = 147460
IOCTL_CDROM_STOP_AUDIO: UInt32 = 147464
IOCTL_CDROM_PAUSE_AUDIO: UInt32 = 147468
IOCTL_CDROM_RESUME_AUDIO: UInt32 = 147472
IOCTL_CDROM_GET_VOLUME: UInt32 = 147476
IOCTL_CDROM_PLAY_AUDIO_MSF: UInt32 = 147480
IOCTL_CDROM_SET_VOLUME: UInt32 = 147496
IOCTL_CDROM_READ_Q_CHANNEL: UInt32 = 147500
IOCTL_CDROM_GET_CONTROL: UInt32 = 147508
OBSOLETE_IOCTL_CDROM_GET_CONTROL: UInt32 = 147508
IOCTL_CDROM_GET_LAST_SESSION: UInt32 = 147512
IOCTL_CDROM_RAW_READ: UInt32 = 147518
IOCTL_CDROM_DISK_TYPE: UInt32 = 131136
IOCTL_CDROM_GET_DRIVE_GEOMETRY: UInt32 = 147532
IOCTL_CDROM_GET_DRIVE_GEOMETRY_EX: UInt32 = 147536
IOCTL_CDROM_READ_TOC_EX: UInt32 = 147540
IOCTL_CDROM_GET_CONFIGURATION: UInt32 = 147544
IOCTL_CDROM_EXCLUSIVE_ACCESS: UInt32 = 180316
IOCTL_CDROM_SET_SPEED: UInt32 = 147552
IOCTL_CDROM_GET_INQUIRY_DATA: UInt32 = 147556
IOCTL_CDROM_ENABLE_STREAMING: UInt32 = 147560
IOCTL_CDROM_SEND_OPC_INFORMATION: UInt32 = 180332
IOCTL_CDROM_GET_PERFORMANCE: UInt32 = 147568
IOCTL_CDROM_CHECK_VERIFY: UInt32 = 149504
IOCTL_CDROM_MEDIA_REMOVAL: UInt32 = 149508
IOCTL_CDROM_EJECT_MEDIA: UInt32 = 149512
IOCTL_CDROM_LOAD_MEDIA: UInt32 = 149516
IOCTL_CDROM_RESERVE: UInt32 = 149520
IOCTL_CDROM_RELEASE: UInt32 = 149524
IOCTL_CDROM_FIND_NEW_DEVICES: UInt32 = 149528
MINIMUM_CDROM_INQUIRY_SIZE: UInt32 = 36
MAXIMUM_CDROM_INQUIRY_SIZE: UInt32 = 260
IOCTL_CDROM_SIMBAD: UInt32 = 147468
MAXIMUM_NUMBER_TRACKS: UInt32 = 100
MAXIMUM_CDROM_SIZE: UInt32 = 804
MINIMUM_CDROM_READ_TOC_EX_SIZE: UInt32 = 2
CDROM_READ_TOC_EX_FORMAT_TOC: UInt32 = 0
CDROM_READ_TOC_EX_FORMAT_SESSION: UInt32 = 1
CDROM_READ_TOC_EX_FORMAT_FULL_TOC: UInt32 = 2
CDROM_READ_TOC_EX_FORMAT_PMA: UInt32 = 3
CDROM_READ_TOC_EX_FORMAT_ATIP: UInt32 = 4
CDROM_READ_TOC_EX_FORMAT_CDTEXT: UInt32 = 5
CDROM_CD_TEXT_PACK_ALBUM_NAME: UInt32 = 128
CDROM_CD_TEXT_PACK_PERFORMER: UInt32 = 129
CDROM_CD_TEXT_PACK_SONGWRITER: UInt32 = 130
CDROM_CD_TEXT_PACK_COMPOSER: UInt32 = 131
CDROM_CD_TEXT_PACK_ARRANGER: UInt32 = 132
CDROM_CD_TEXT_PACK_MESSAGES: UInt32 = 133
CDROM_CD_TEXT_PACK_DISC_ID: UInt32 = 134
CDROM_CD_TEXT_PACK_GENRE: UInt32 = 135
CDROM_CD_TEXT_PACK_TOC_INFO: UInt32 = 136
CDROM_CD_TEXT_PACK_TOC_INFO2: UInt32 = 137
CDROM_CD_TEXT_PACK_UPC_EAN: UInt32 = 142
CDROM_CD_TEXT_PACK_SIZE_INFO: UInt32 = 143
CDROM_DISK_AUDIO_TRACK: UInt32 = 1
CDROM_DISK_DATA_TRACK: UInt32 = 2
IOCTL_CDROM_SUB_Q_CHANNEL: UInt32 = 0
IOCTL_CDROM_CURRENT_POSITION: UInt32 = 1
IOCTL_CDROM_MEDIA_CATALOG: UInt32 = 2
IOCTL_CDROM_TRACK_ISRC: UInt32 = 3
AUDIO_STATUS_NOT_SUPPORTED: UInt32 = 0
AUDIO_STATUS_IN_PROGRESS: UInt32 = 17
AUDIO_STATUS_PAUSED: UInt32 = 18
AUDIO_STATUS_PLAY_COMPLETE: UInt32 = 19
AUDIO_STATUS_PLAY_ERROR: UInt32 = 20
AUDIO_STATUS_NO_STATUS: UInt32 = 21
ADR_NO_MODE_INFORMATION: UInt32 = 0
ADR_ENCODES_CURRENT_POSITION: UInt32 = 1
ADR_ENCODES_MEDIA_CATALOG: UInt32 = 2
ADR_ENCODES_ISRC: UInt32 = 3
AUDIO_WITH_PREEMPHASIS: UInt32 = 1
DIGITAL_COPY_PERMITTED: UInt32 = 2
AUDIO_DATA_TRACK: UInt32 = 4
TWO_FOUR_CHANNEL_AUDIO: UInt32 = 8
CD_RAW_READ_C2_SIZE: UInt32 = 296
CD_RAW_READ_SUBCODE_SIZE: UInt32 = 96
CD_RAW_SECTOR_WITH_C2_SIZE: UInt32 = 2648
CD_RAW_SECTOR_WITH_SUBCODE_SIZE: UInt32 = 2448
CDROM_EXCLUSIVE_CALLER_LENGTH: UInt32 = 64
CDROM_LOCK_IGNORE_VOLUME: UInt32 = 1
CDROM_NO_MEDIA_NOTIFICATIONS: UInt32 = 2
CDROM_NOT_IN_EXCLUSIVE_MODE: UInt32 = 0
CDROM_IN_EXCLUSIVE_MODE: UInt32 = 1
class CDROM_DISK_DATA(Structure):
    DiskData: UInt32
class CDROM_EXCEPTION_PERFORMANCE_DESCRIPTOR(Structure):
    Lba: Byte * 4
    Time: Byte * 2
class CDROM_EXCLUSIVE_ACCESS(Structure):
    RequestType: win32more.Windows.Win32.Devices.Cdrom.EXCLUSIVE_ACCESS_REQUEST_TYPE
    Flags: UInt32
class CDROM_EXCLUSIVE_LOCK(Structure):
    Access: win32more.Windows.Win32.Devices.Cdrom.CDROM_EXCLUSIVE_ACCESS
    CallerName: Byte * 64
class CDROM_EXCLUSIVE_LOCK_STATE(Structure):
    LockState: win32more.Windows.Win32.Foundation.BOOLEAN
    CallerName: Byte * 64
class CDROM_NOMINAL_PERFORMANCE_DESCRIPTOR(Structure):
    StartLba: Byte * 4
    StartPerformance: Byte * 4
    EndLba: Byte * 4
    EndPerformance: Byte * 4
CDROM_OPC_INFO_TYPE = Int32
SimpleOpcInfo: win32more.Windows.Win32.Devices.Cdrom.CDROM_OPC_INFO_TYPE = 1
CDROM_PERFORMANCE_EXCEPTION_TYPE = Int32
CdromNominalPerformance: win32more.Windows.Win32.Devices.Cdrom.CDROM_PERFORMANCE_EXCEPTION_TYPE = 1
CdromEntirePerformanceList: win32more.Windows.Win32.Devices.Cdrom.CDROM_PERFORMANCE_EXCEPTION_TYPE = 2
CdromPerformanceExceptionsOnly: win32more.Windows.Win32.Devices.Cdrom.CDROM_PERFORMANCE_EXCEPTION_TYPE = 3
class CDROM_PERFORMANCE_HEADER(Structure):
    DataLength: Byte * 4
    Except: Annotated[Byte, 1]
    Write: Annotated[Byte, 1]
    Reserved1: Annotated[Byte, 6]
    Reserved2: Byte * 3
    Data: Byte * 1
class CDROM_PERFORMANCE_REQUEST(Structure):
    RequestType: win32more.Windows.Win32.Devices.Cdrom.CDROM_PERFORMANCE_REQUEST_TYPE
    PerformanceType: win32more.Windows.Win32.Devices.Cdrom.CDROM_PERFORMANCE_TYPE
    Exceptions: win32more.Windows.Win32.Devices.Cdrom.CDROM_PERFORMANCE_EXCEPTION_TYPE
    Tolerance: win32more.Windows.Win32.Devices.Cdrom.CDROM_PERFORMANCE_TOLERANCE_TYPE
    StaringLba: UInt32
CDROM_PERFORMANCE_REQUEST_TYPE = Int32
CdromPerformanceRequest: win32more.Windows.Win32.Devices.Cdrom.CDROM_PERFORMANCE_REQUEST_TYPE = 1
CdromWriteSpeedRequest: win32more.Windows.Win32.Devices.Cdrom.CDROM_PERFORMANCE_REQUEST_TYPE = 2
CDROM_PERFORMANCE_TOLERANCE_TYPE = Int32
Cdrom10Nominal20Exceptions: win32more.Windows.Win32.Devices.Cdrom.CDROM_PERFORMANCE_TOLERANCE_TYPE = 1
CDROM_PERFORMANCE_TYPE = Int32
CdromReadPerformance: win32more.Windows.Win32.Devices.Cdrom.CDROM_PERFORMANCE_TYPE = 1
CdromWritePerformance: win32more.Windows.Win32.Devices.Cdrom.CDROM_PERFORMANCE_TYPE = 2
class CDROM_PLAY_AUDIO_MSF(Structure):
    StartingM: Byte
    StartingS: Byte
    StartingF: Byte
    EndingM: Byte
    EndingS: Byte
    EndingF: Byte
class CDROM_READ_TOC_EX(Structure):
    Format: Annotated[Byte, 4]
    Reserved1: Annotated[Byte, 3]
    Msf: Annotated[Byte, 1]
    SessionTrack: Byte
    Reserved2: Byte
    Reserved3: Byte
class CDROM_SEEK_AUDIO_MSF(Structure):
    M: Byte
    S: Byte
    F: Byte
class CDROM_SET_SPEED(Structure):
    RequestType: win32more.Windows.Win32.Devices.Cdrom.CDROM_SPEED_REQUEST
    ReadSpeed: UInt16
    WriteSpeed: UInt16
    RotationControl: win32more.Windows.Win32.Devices.Cdrom.WRITE_ROTATION
class CDROM_SET_STREAMING(Structure):
    RequestType: win32more.Windows.Win32.Devices.Cdrom.CDROM_SPEED_REQUEST
    ReadSize: UInt32
    ReadTime: UInt32
    WriteSize: UInt32
    WriteTime: UInt32
    StartLba: UInt32
    EndLba: UInt32
    RotationControl: win32more.Windows.Win32.Devices.Cdrom.WRITE_ROTATION
    RestoreDefaults: win32more.Windows.Win32.Foundation.BOOLEAN
    SetExact: win32more.Windows.Win32.Foundation.BOOLEAN
    RandomAccess: win32more.Windows.Win32.Foundation.BOOLEAN
    Persistent: win32more.Windows.Win32.Foundation.BOOLEAN
class CDROM_SIMPLE_OPC_INFO(Structure):
    RequestType: win32more.Windows.Win32.Devices.Cdrom.CDROM_OPC_INFO_TYPE
    Exclude0: win32more.Windows.Win32.Foundation.BOOLEAN
    Exclude1: win32more.Windows.Win32.Foundation.BOOLEAN
CDROM_SPEED_REQUEST = Int32
CdromSetSpeed: win32more.Windows.Win32.Devices.Cdrom.CDROM_SPEED_REQUEST = 0
CdromSetStreaming: win32more.Windows.Win32.Devices.Cdrom.CDROM_SPEED_REQUEST = 1
class CDROM_STREAMING_CONTROL(Structure):
    RequestType: win32more.Windows.Win32.Devices.Cdrom.STREAMING_CONTROL_REQUEST_TYPE
class CDROM_SUB_Q_DATA_FORMAT(Structure):
    Format: Byte
    Track: Byte
class CDROM_TOC(Structure):
    Length: Byte * 2
    FirstTrack: Byte
    LastTrack: Byte
    TrackData: win32more.Windows.Win32.Devices.Cdrom.TRACK_DATA * 100
class CDROM_TOC_ATIP_DATA(Structure):
    Length: Byte * 2
    Reserved1: Byte
    Reserved2: Byte
    Descriptors: win32more.Windows.Win32.Devices.Cdrom.CDROM_TOC_ATIP_DATA_BLOCK * 1
class CDROM_TOC_ATIP_DATA_BLOCK(Structure):
    CdrwReferenceSpeed: Annotated[Byte, 3]
    Reserved3: Annotated[Byte, 1]
    WritePower: Annotated[Byte, 3]
    True1: Annotated[Byte, 1]
    Reserved4: Annotated[Byte, 6]
    UnrestrictedUse: Annotated[Byte, 1]
    Reserved5: Annotated[Byte, 1]
    A3Valid: Annotated[Byte, 1]
    A2Valid: Annotated[Byte, 1]
    A1Valid: Annotated[Byte, 1]
    DiscSubType: Annotated[Byte, 3]
    IsCdrw: Annotated[Byte, 1]
    True2: Annotated[Byte, 1]
    Reserved7: Byte
    LeadInMsf: Byte * 3
    Reserved8: Byte
    LeadOutMsf: Byte * 3
    Reserved9: Byte
    A1Values: Byte * 3
    Reserved10: Byte
    A2Values: Byte * 3
    Reserved11: Byte
    A3Values: Byte * 3
    Reserved12: Byte
class CDROM_TOC_CD_TEXT_DATA(Structure):
    Length: Byte * 2
    Reserved1: Byte
    Reserved2: Byte
    Descriptors: win32more.Windows.Win32.Devices.Cdrom.CDROM_TOC_CD_TEXT_DATA_BLOCK * 1
class CDROM_TOC_CD_TEXT_DATA_BLOCK(Structure):
    PackType: Byte
    TrackNumber: Annotated[Byte, 7]
    ExtensionFlag: Annotated[Byte, 1]
    SequenceNumber: Byte
    CharacterPosition: Annotated[Byte, 4]
    BlockNumber: Annotated[Byte, 3]
    Unicode: Annotated[Byte, 1]
    Anonymous: _Anonymous_e__Union
    CRC: Byte * 2
    class _Anonymous_e__Union(Union):
        Text: Byte * 12
        WText: Char * 6
class CDROM_TOC_FULL_TOC_DATA(Structure):
    Length: Byte * 2
    FirstCompleteSession: Byte
    LastCompleteSession: Byte
    Descriptors: win32more.Windows.Win32.Devices.Cdrom.CDROM_TOC_FULL_TOC_DATA_BLOCK * 1
class CDROM_TOC_FULL_TOC_DATA_BLOCK(Structure):
    SessionNumber: Byte
    Control: Annotated[Byte, 4]
    Adr: Annotated[Byte, 4]
    Reserved1: Byte
    Point: Byte
    MsfExtra: Byte * 3
    Zero: Byte
    Msf: Byte * 3
class CDROM_TOC_PMA_DATA(Structure):
    Length: Byte * 2
    Reserved1: Byte
    Reserved2: Byte
    Descriptors: win32more.Windows.Win32.Devices.Cdrom.CDROM_TOC_FULL_TOC_DATA_BLOCK * 1
class CDROM_TOC_SESSION_DATA(Structure):
    Length: Byte * 2
    FirstCompleteSession: Byte
    LastCompleteSession: Byte
    TrackData: win32more.Windows.Win32.Devices.Cdrom.TRACK_DATA * 1
class CDROM_WRITE_SPEED_DESCRIPTOR(Structure):
    MixedReadWrite: Annotated[Byte, 1]
    Exact: Annotated[Byte, 1]
    Reserved1: Annotated[Byte, 1]
    WriteRotationControl: Annotated[Byte, 2]
    Reserved2: Annotated[Byte, 3]
    Reserved3: Byte * 3
    EndLba: Byte * 4
    ReadSpeed: Byte * 4
    WriteSpeed: Byte * 4
class CDROM_WRITE_SPEED_REQUEST(Structure):
    RequestType: win32more.Windows.Win32.Devices.Cdrom.CDROM_PERFORMANCE_REQUEST_TYPE
EXCLUSIVE_ACCESS_REQUEST_TYPE = Int32
ExclusiveAccessQueryState: win32more.Windows.Win32.Devices.Cdrom.EXCLUSIVE_ACCESS_REQUEST_TYPE = 0
ExclusiveAccessLockDevice: win32more.Windows.Win32.Devices.Cdrom.EXCLUSIVE_ACCESS_REQUEST_TYPE = 1
ExclusiveAccessUnlockDevice: win32more.Windows.Win32.Devices.Cdrom.EXCLUSIVE_ACCESS_REQUEST_TYPE = 2
MEDIA_BLANK_TYPE = Int32
MediaBlankTypeFull: win32more.Windows.Win32.Devices.Cdrom.MEDIA_BLANK_TYPE = 0
MediaBlankTypeMinimal: win32more.Windows.Win32.Devices.Cdrom.MEDIA_BLANK_TYPE = 1
MediaBlankTypeIncompleteTrack: win32more.Windows.Win32.Devices.Cdrom.MEDIA_BLANK_TYPE = 2
MediaBlankTypeUnreserveLastTrack: win32more.Windows.Win32.Devices.Cdrom.MEDIA_BLANK_TYPE = 3
MediaBlankTypeTrackTail: win32more.Windows.Win32.Devices.Cdrom.MEDIA_BLANK_TYPE = 4
MediaBlankTypeUncloseLastSession: win32more.Windows.Win32.Devices.Cdrom.MEDIA_BLANK_TYPE = 5
MediaBlankTypeEraseLastSession: win32more.Windows.Win32.Devices.Cdrom.MEDIA_BLANK_TYPE = 6
class RAW_READ_INFO(Structure):
    DiskOffset: Int64
    SectorCount: UInt32
    TrackMode: win32more.Windows.Win32.Devices.Cdrom.TRACK_MODE_TYPE
STREAMING_CONTROL_REQUEST_TYPE = Int32
CdromStreamingDisable: win32more.Windows.Win32.Devices.Cdrom.STREAMING_CONTROL_REQUEST_TYPE = 1
CdromStreamingEnableForReadOnly: win32more.Windows.Win32.Devices.Cdrom.STREAMING_CONTROL_REQUEST_TYPE = 2
CdromStreamingEnableForWriteOnly: win32more.Windows.Win32.Devices.Cdrom.STREAMING_CONTROL_REQUEST_TYPE = 3
CdromStreamingEnableForReadWrite: win32more.Windows.Win32.Devices.Cdrom.STREAMING_CONTROL_REQUEST_TYPE = 4
class SUB_Q_CHANNEL_DATA(Union):
    CurrentPosition: win32more.Windows.Win32.Devices.Cdrom.SUB_Q_CURRENT_POSITION
    MediaCatalog: win32more.Windows.Win32.Devices.Cdrom.SUB_Q_MEDIA_CATALOG_NUMBER
    TrackIsrc: win32more.Windows.Win32.Devices.Cdrom.SUB_Q_TRACK_ISRC
class SUB_Q_CURRENT_POSITION(Structure):
    Header: win32more.Windows.Win32.Devices.Cdrom.SUB_Q_HEADER
    FormatCode: Byte
    Control: Annotated[Byte, 4]
    ADR: Annotated[Byte, 4]
    TrackNumber: Byte
    IndexNumber: Byte
    AbsoluteAddress: Byte * 4
    TrackRelativeAddress: Byte * 4
class SUB_Q_HEADER(Structure):
    Reserved: Byte
    AudioStatus: Byte
    DataLength: Byte * 2
class SUB_Q_MEDIA_CATALOG_NUMBER(Structure):
    Header: win32more.Windows.Win32.Devices.Cdrom.SUB_Q_HEADER
    FormatCode: Byte
    Reserved: Byte * 3
    Reserved1: Annotated[Byte, 7]
    Mcval: Annotated[Byte, 1]
    MediaCatalog: Byte * 15
class SUB_Q_TRACK_ISRC(Structure):
    Header: win32more.Windows.Win32.Devices.Cdrom.SUB_Q_HEADER
    FormatCode: Byte
    Reserved0: Byte
    Track: Byte
    Reserved1: Byte
    Reserved2: Annotated[Byte, 7]
    Tcval: Annotated[Byte, 1]
    TrackIsrc: Byte * 15
class TRACK_DATA(Structure):
    Reserved: Byte
    Control: Annotated[Byte, 4]
    Adr: Annotated[Byte, 4]
    TrackNumber: Byte
    Reserved1: Byte
    Address: Byte * 4
TRACK_MODE_TYPE = Int32
YellowMode2: win32more.Windows.Win32.Devices.Cdrom.TRACK_MODE_TYPE = 0
XAForm2: win32more.Windows.Win32.Devices.Cdrom.TRACK_MODE_TYPE = 1
CDDA: win32more.Windows.Win32.Devices.Cdrom.TRACK_MODE_TYPE = 2
RawWithC2AndSubCode: win32more.Windows.Win32.Devices.Cdrom.TRACK_MODE_TYPE = 3
RawWithC2: win32more.Windows.Win32.Devices.Cdrom.TRACK_MODE_TYPE = 4
RawWithSubCode: win32more.Windows.Win32.Devices.Cdrom.TRACK_MODE_TYPE = 5
class VOLUME_CONTROL(Structure):
    PortVolume: Byte * 4
WRITE_ROTATION = Int32
CdromDefaultRotation: win32more.Windows.Win32.Devices.Cdrom.WRITE_ROTATION = 0
CdromCAVRotation: win32more.Windows.Win32.Devices.Cdrom.WRITE_ROTATION = 1


make_ready(__name__)
