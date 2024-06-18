from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Security
import win32more.Windows.Win32.Storage.InstallableFileSystems
import win32more.Windows.Win32.System.IO
FILTER_NAME_MAX_CHARS: UInt32 = 255
VOLUME_NAME_MAX_CHARS: UInt32 = 1024
INSTANCE_NAME_MAX_CHARS: UInt32 = 255
FLTFL_AGGREGATE_INFO_IS_MINIFILTER: UInt32 = 1
FLTFL_AGGREGATE_INFO_IS_LEGACYFILTER: UInt32 = 2
FLTFL_ASI_IS_MINIFILTER: UInt32 = 1
FLTFL_ASI_IS_LEGACYFILTER: UInt32 = 2
FLTFL_VSI_DETACHED_VOLUME: UInt32 = 1
FLTFL_IASI_IS_MINIFILTER: UInt32 = 1
FLTFL_IASI_IS_LEGACYFILTER: UInt32 = 2
FLTFL_IASIM_DETACHED_VOLUME: UInt32 = 1
FLTFL_IASIL_DETACHED_VOLUME: UInt32 = 1
FLT_PORT_FLAG_SYNC_HANDLE: UInt32 = 1
WNNC_NET_MSNET: UInt32 = 65536
WNNC_NET_SMB: UInt32 = 131072
WNNC_NET_NETWARE: UInt32 = 196608
WNNC_NET_VINES: UInt32 = 262144
WNNC_NET_10NET: UInt32 = 327680
WNNC_NET_LOCUS: UInt32 = 393216
WNNC_NET_SUN_PC_NFS: UInt32 = 458752
WNNC_NET_LANSTEP: UInt32 = 524288
WNNC_NET_9TILES: UInt32 = 589824
WNNC_NET_LANTASTIC: UInt32 = 655360
WNNC_NET_AS400: UInt32 = 720896
WNNC_NET_FTP_NFS: UInt32 = 786432
WNNC_NET_PATHWORKS: UInt32 = 851968
WNNC_NET_LIFENET: UInt32 = 917504
WNNC_NET_POWERLAN: UInt32 = 983040
WNNC_NET_BWNFS: UInt32 = 1048576
WNNC_NET_COGENT: UInt32 = 1114112
WNNC_NET_FARALLON: UInt32 = 1179648
WNNC_NET_APPLETALK: UInt32 = 1245184
WNNC_NET_INTERGRAPH: UInt32 = 1310720
WNNC_NET_SYMFONET: UInt32 = 1376256
WNNC_NET_CLEARCASE: UInt32 = 1441792
WNNC_NET_FRONTIER: UInt32 = 1507328
WNNC_NET_BMC: UInt32 = 1572864
WNNC_NET_DCE: UInt32 = 1638400
WNNC_NET_AVID: UInt32 = 1703936
WNNC_NET_DOCUSPACE: UInt32 = 1769472
WNNC_NET_MANGOSOFT: UInt32 = 1835008
WNNC_NET_SERNET: UInt32 = 1900544
WNNC_NET_RIVERFRONT1: UInt32 = 1966080
WNNC_NET_RIVERFRONT2: UInt32 = 2031616
WNNC_NET_DECORB: UInt32 = 2097152
WNNC_NET_PROTSTOR: UInt32 = 2162688
WNNC_NET_FJ_REDIR: UInt32 = 2228224
WNNC_NET_DISTINCT: UInt32 = 2293760
WNNC_NET_TWINS: UInt32 = 2359296
WNNC_NET_RDR2SAMPLE: UInt32 = 2424832
WNNC_NET_CSC: UInt32 = 2490368
WNNC_NET_3IN1: UInt32 = 2555904
WNNC_NET_EXTENDNET: UInt32 = 2686976
WNNC_NET_STAC: UInt32 = 2752512
WNNC_NET_FOXBAT: UInt32 = 2818048
WNNC_NET_YAHOO: UInt32 = 2883584
WNNC_NET_EXIFS: UInt32 = 2949120
WNNC_NET_DAV: UInt32 = 3014656
WNNC_NET_KNOWARE: UInt32 = 3080192
WNNC_NET_OBJECT_DIRE: UInt32 = 3145728
WNNC_NET_MASFAX: UInt32 = 3211264
WNNC_NET_HOB_NFS: UInt32 = 3276800
WNNC_NET_SHIVA: UInt32 = 3342336
WNNC_NET_IBMAL: UInt32 = 3407872
WNNC_NET_LOCK: UInt32 = 3473408
WNNC_NET_TERMSRV: UInt32 = 3538944
WNNC_NET_SRT: UInt32 = 3604480
WNNC_NET_QUINCY: UInt32 = 3670016
WNNC_NET_OPENAFS: UInt32 = 3735552
WNNC_NET_AVID1: UInt32 = 3801088
WNNC_NET_DFS: UInt32 = 3866624
WNNC_NET_KWNP: UInt32 = 3932160
WNNC_NET_ZENWORKS: UInt32 = 3997696
WNNC_NET_DRIVEONWEB: UInt32 = 4063232
WNNC_NET_VMWARE: UInt32 = 4128768
WNNC_NET_RSFX: UInt32 = 4194304
WNNC_NET_MFILES: UInt32 = 4259840
WNNC_NET_MS_NFS: UInt32 = 4325376
WNNC_NET_GOOGLE: UInt32 = 4390912
WNNC_NET_NDFS: UInt32 = 4456448
WNNC_NET_DOCUSHARE: UInt32 = 4521984
WNNC_NET_AURISTOR_FS: UInt32 = 4587520
WNNC_NET_SECUREAGENT: UInt32 = 4653056
WNNC_NET_9P: UInt32 = 4718592
WNNC_CRED_MANAGER: UInt32 = 4294901760
WNNC_NET_LANMAN: UInt32 = 131072
@winfunctype('FLTLIB.dll')
def FilterLoad(lpFilterName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('FLTLIB.dll')
def FilterUnload(lpFilterName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('FLTLIB.dll')
def FilterCreate(lpFilterName: win32more.Windows.Win32.Foundation.PWSTR, hFilter: POINTER(win32more.Windows.Win32.Storage.InstallableFileSystems.HFILTER)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('FLTLIB.dll')
def FilterClose(hFilter: win32more.Windows.Win32.Storage.InstallableFileSystems.HFILTER) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('FLTLIB.dll')
def FilterInstanceCreate(lpFilterName: win32more.Windows.Win32.Foundation.PWSTR, lpVolumeName: win32more.Windows.Win32.Foundation.PWSTR, lpInstanceName: win32more.Windows.Win32.Foundation.PWSTR, hInstance: POINTER(win32more.Windows.Win32.Storage.InstallableFileSystems.HFILTER_INSTANCE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('FLTLIB.dll')
def FilterInstanceClose(hInstance: win32more.Windows.Win32.Storage.InstallableFileSystems.HFILTER_INSTANCE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('FLTLIB.dll')
def FilterAttach(lpFilterName: win32more.Windows.Win32.Foundation.PWSTR, lpVolumeName: win32more.Windows.Win32.Foundation.PWSTR, lpInstanceName: win32more.Windows.Win32.Foundation.PWSTR, dwCreatedInstanceNameLength: UInt32, lpCreatedInstanceName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('FLTLIB.dll')
def FilterAttachAtAltitude(lpFilterName: win32more.Windows.Win32.Foundation.PWSTR, lpVolumeName: win32more.Windows.Win32.Foundation.PWSTR, lpAltitude: win32more.Windows.Win32.Foundation.PWSTR, lpInstanceName: win32more.Windows.Win32.Foundation.PWSTR, dwCreatedInstanceNameLength: UInt32, lpCreatedInstanceName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('FLTLIB.dll')
def FilterDetach(lpFilterName: win32more.Windows.Win32.Foundation.PWSTR, lpVolumeName: win32more.Windows.Win32.Foundation.PWSTR, lpInstanceName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('FLTLIB.dll')
def FilterFindFirst(dwInformationClass: win32more.Windows.Win32.Storage.InstallableFileSystems.FILTER_INFORMATION_CLASS, lpBuffer: VoidPtr, dwBufferSize: UInt32, lpBytesReturned: POINTER(UInt32), lpFilterFind: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('FLTLIB.dll')
def FilterFindNext(hFilterFind: win32more.Windows.Win32.Foundation.HANDLE, dwInformationClass: win32more.Windows.Win32.Storage.InstallableFileSystems.FILTER_INFORMATION_CLASS, lpBuffer: VoidPtr, dwBufferSize: UInt32, lpBytesReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('FLTLIB.dll')
def FilterFindClose(hFilterFind: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('FLTLIB.dll')
def FilterVolumeFindFirst(dwInformationClass: win32more.Windows.Win32.Storage.InstallableFileSystems.FILTER_VOLUME_INFORMATION_CLASS, lpBuffer: VoidPtr, dwBufferSize: UInt32, lpBytesReturned: POINTER(UInt32), lpVolumeFind: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('FLTLIB.dll')
def FilterVolumeFindNext(hVolumeFind: win32more.Windows.Win32.Foundation.HANDLE, dwInformationClass: win32more.Windows.Win32.Storage.InstallableFileSystems.FILTER_VOLUME_INFORMATION_CLASS, lpBuffer: VoidPtr, dwBufferSize: UInt32, lpBytesReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('FLTLIB.dll')
def FilterVolumeFindClose(hVolumeFind: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('FLTLIB.dll')
def FilterInstanceFindFirst(lpFilterName: win32more.Windows.Win32.Foundation.PWSTR, dwInformationClass: win32more.Windows.Win32.Storage.InstallableFileSystems.INSTANCE_INFORMATION_CLASS, lpBuffer: VoidPtr, dwBufferSize: UInt32, lpBytesReturned: POINTER(UInt32), lpFilterInstanceFind: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('FLTLIB.dll')
def FilterInstanceFindNext(hFilterInstanceFind: win32more.Windows.Win32.Foundation.HANDLE, dwInformationClass: win32more.Windows.Win32.Storage.InstallableFileSystems.INSTANCE_INFORMATION_CLASS, lpBuffer: VoidPtr, dwBufferSize: UInt32, lpBytesReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('FLTLIB.dll')
def FilterInstanceFindClose(hFilterInstanceFind: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('FLTLIB.dll')
def FilterVolumeInstanceFindFirst(lpVolumeName: win32more.Windows.Win32.Foundation.PWSTR, dwInformationClass: win32more.Windows.Win32.Storage.InstallableFileSystems.INSTANCE_INFORMATION_CLASS, lpBuffer: VoidPtr, dwBufferSize: UInt32, lpBytesReturned: POINTER(UInt32), lpVolumeInstanceFind: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('FLTLIB.dll')
def FilterVolumeInstanceFindNext(hVolumeInstanceFind: win32more.Windows.Win32.Foundation.HANDLE, dwInformationClass: win32more.Windows.Win32.Storage.InstallableFileSystems.INSTANCE_INFORMATION_CLASS, lpBuffer: VoidPtr, dwBufferSize: UInt32, lpBytesReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('FLTLIB.dll')
def FilterVolumeInstanceFindClose(hVolumeInstanceFind: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('FLTLIB.dll')
def FilterGetInformation(hFilter: win32more.Windows.Win32.Storage.InstallableFileSystems.HFILTER, dwInformationClass: win32more.Windows.Win32.Storage.InstallableFileSystems.FILTER_INFORMATION_CLASS, lpBuffer: VoidPtr, dwBufferSize: UInt32, lpBytesReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('FLTLIB.dll')
def FilterInstanceGetInformation(hInstance: win32more.Windows.Win32.Storage.InstallableFileSystems.HFILTER_INSTANCE, dwInformationClass: win32more.Windows.Win32.Storage.InstallableFileSystems.INSTANCE_INFORMATION_CLASS, lpBuffer: VoidPtr, dwBufferSize: UInt32, lpBytesReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('FLTLIB.dll')
def FilterConnectCommunicationPort(lpPortName: win32more.Windows.Win32.Foundation.PWSTR, dwOptions: UInt32, lpContext: VoidPtr, wSizeOfContext: UInt16, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), hPort: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('FLTLIB.dll')
def FilterSendMessage(hPort: win32more.Windows.Win32.Foundation.HANDLE, lpInBuffer: VoidPtr, dwInBufferSize: UInt32, lpOutBuffer: VoidPtr, dwOutBufferSize: UInt32, lpBytesReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('FLTLIB.dll')
def FilterGetMessage(hPort: win32more.Windows.Win32.Foundation.HANDLE, lpMessageBuffer: POINTER(win32more.Windows.Win32.Storage.InstallableFileSystems.FILTER_MESSAGE_HEADER), dwMessageBufferSize: UInt32, lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('FLTLIB.dll')
def FilterReplyMessage(hPort: win32more.Windows.Win32.Foundation.HANDLE, lpReplyBuffer: POINTER(win32more.Windows.Win32.Storage.InstallableFileSystems.FILTER_REPLY_HEADER), dwReplyBufferSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('FLTLIB.dll')
def FilterGetDosName(lpVolumeName: win32more.Windows.Win32.Foundation.PWSTR, lpDosName: win32more.Windows.Win32.Foundation.PWSTR, dwDosNameBufferSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class FILTER_AGGREGATE_BASIC_INFORMATION(Structure):
    NextEntryOffset: UInt32
    Flags: UInt32
    Type: _Type_e__Union
    class _Type_e__Union(Union):
        MiniFilter: _MiniFilter_e__Struct
        LegacyFilter: _LegacyFilter_e__Struct
        class _MiniFilter_e__Struct(Structure):
            FrameID: UInt32
            NumberOfInstances: UInt32
            FilterNameLength: UInt16
            FilterNameBufferOffset: UInt16
            FilterAltitudeLength: UInt16
            FilterAltitudeBufferOffset: UInt16
        class _LegacyFilter_e__Struct(Structure):
            FilterNameLength: UInt16
            FilterNameBufferOffset: UInt16
class FILTER_AGGREGATE_STANDARD_INFORMATION(Structure):
    NextEntryOffset: UInt32
    Flags: UInt32
    Type: _Type_e__Union
    class _Type_e__Union(Union):
        MiniFilter: _MiniFilter_e__Struct
        LegacyFilter: _LegacyFilter_e__Struct
        class _MiniFilter_e__Struct(Structure):
            Flags: UInt32
            FrameID: UInt32
            NumberOfInstances: UInt32
            FilterNameLength: UInt16
            FilterNameBufferOffset: UInt16
            FilterAltitudeLength: UInt16
            FilterAltitudeBufferOffset: UInt16
        class _LegacyFilter_e__Struct(Structure):
            Flags: UInt32
            FilterNameLength: UInt16
            FilterNameBufferOffset: UInt16
            FilterAltitudeLength: UInt16
            FilterAltitudeBufferOffset: UInt16
class FILTER_FULL_INFORMATION(Structure):
    NextEntryOffset: UInt32
    FrameID: UInt32
    NumberOfInstances: UInt32
    FilterNameLength: UInt16
    FilterNameBuffer: Char * 1
FILTER_INFORMATION_CLASS = Int32
FilterFullInformation: win32more.Windows.Win32.Storage.InstallableFileSystems.FILTER_INFORMATION_CLASS = 0
FilterAggregateBasicInformation: win32more.Windows.Win32.Storage.InstallableFileSystems.FILTER_INFORMATION_CLASS = 1
FilterAggregateStandardInformation: win32more.Windows.Win32.Storage.InstallableFileSystems.FILTER_INFORMATION_CLASS = 2
class FILTER_MESSAGE_HEADER(Structure):
    ReplyLength: UInt32
    MessageId: UInt64
class FILTER_REPLY_HEADER(Structure):
    Status: win32more.Windows.Win32.Foundation.NTSTATUS
    MessageId: UInt64
class FILTER_VOLUME_BASIC_INFORMATION(Structure):
    FilterVolumeNameLength: UInt16
    FilterVolumeName: Char * 1
FILTER_VOLUME_INFORMATION_CLASS = Int32
FilterVolumeBasicInformation: win32more.Windows.Win32.Storage.InstallableFileSystems.FILTER_VOLUME_INFORMATION_CLASS = 0
FilterVolumeStandardInformation: win32more.Windows.Win32.Storage.InstallableFileSystems.FILTER_VOLUME_INFORMATION_CLASS = 1
class FILTER_VOLUME_STANDARD_INFORMATION(Structure):
    NextEntryOffset: UInt32
    Flags: UInt32
    FrameID: UInt32
    FileSystemType: win32more.Windows.Win32.Storage.InstallableFileSystems.FLT_FILESYSTEM_TYPE
    FilterVolumeNameLength: UInt16
    FilterVolumeName: Char * 1
FLT_FILESYSTEM_TYPE = Int32
FLT_FSTYPE_UNKNOWN: win32more.Windows.Win32.Storage.InstallableFileSystems.FLT_FILESYSTEM_TYPE = 0
FLT_FSTYPE_RAW: win32more.Windows.Win32.Storage.InstallableFileSystems.FLT_FILESYSTEM_TYPE = 1
FLT_FSTYPE_NTFS: win32more.Windows.Win32.Storage.InstallableFileSystems.FLT_FILESYSTEM_TYPE = 2
FLT_FSTYPE_FAT: win32more.Windows.Win32.Storage.InstallableFileSystems.FLT_FILESYSTEM_TYPE = 3
FLT_FSTYPE_CDFS: win32more.Windows.Win32.Storage.InstallableFileSystems.FLT_FILESYSTEM_TYPE = 4
FLT_FSTYPE_UDFS: win32more.Windows.Win32.Storage.InstallableFileSystems.FLT_FILESYSTEM_TYPE = 5
FLT_FSTYPE_LANMAN: win32more.Windows.Win32.Storage.InstallableFileSystems.FLT_FILESYSTEM_TYPE = 6
FLT_FSTYPE_WEBDAV: win32more.Windows.Win32.Storage.InstallableFileSystems.FLT_FILESYSTEM_TYPE = 7
FLT_FSTYPE_RDPDR: win32more.Windows.Win32.Storage.InstallableFileSystems.FLT_FILESYSTEM_TYPE = 8
FLT_FSTYPE_NFS: win32more.Windows.Win32.Storage.InstallableFileSystems.FLT_FILESYSTEM_TYPE = 9
FLT_FSTYPE_MS_NETWARE: win32more.Windows.Win32.Storage.InstallableFileSystems.FLT_FILESYSTEM_TYPE = 10
FLT_FSTYPE_NETWARE: win32more.Windows.Win32.Storage.InstallableFileSystems.FLT_FILESYSTEM_TYPE = 11
FLT_FSTYPE_BSUDF: win32more.Windows.Win32.Storage.InstallableFileSystems.FLT_FILESYSTEM_TYPE = 12
FLT_FSTYPE_MUP: win32more.Windows.Win32.Storage.InstallableFileSystems.FLT_FILESYSTEM_TYPE = 13
FLT_FSTYPE_RSFX: win32more.Windows.Win32.Storage.InstallableFileSystems.FLT_FILESYSTEM_TYPE = 14
FLT_FSTYPE_ROXIO_UDF1: win32more.Windows.Win32.Storage.InstallableFileSystems.FLT_FILESYSTEM_TYPE = 15
FLT_FSTYPE_ROXIO_UDF2: win32more.Windows.Win32.Storage.InstallableFileSystems.FLT_FILESYSTEM_TYPE = 16
FLT_FSTYPE_ROXIO_UDF3: win32more.Windows.Win32.Storage.InstallableFileSystems.FLT_FILESYSTEM_TYPE = 17
FLT_FSTYPE_TACIT: win32more.Windows.Win32.Storage.InstallableFileSystems.FLT_FILESYSTEM_TYPE = 18
FLT_FSTYPE_FS_REC: win32more.Windows.Win32.Storage.InstallableFileSystems.FLT_FILESYSTEM_TYPE = 19
FLT_FSTYPE_INCD: win32more.Windows.Win32.Storage.InstallableFileSystems.FLT_FILESYSTEM_TYPE = 20
FLT_FSTYPE_INCD_FAT: win32more.Windows.Win32.Storage.InstallableFileSystems.FLT_FILESYSTEM_TYPE = 21
FLT_FSTYPE_EXFAT: win32more.Windows.Win32.Storage.InstallableFileSystems.FLT_FILESYSTEM_TYPE = 22
FLT_FSTYPE_PSFS: win32more.Windows.Win32.Storage.InstallableFileSystems.FLT_FILESYSTEM_TYPE = 23
FLT_FSTYPE_GPFS: win32more.Windows.Win32.Storage.InstallableFileSystems.FLT_FILESYSTEM_TYPE = 24
FLT_FSTYPE_NPFS: win32more.Windows.Win32.Storage.InstallableFileSystems.FLT_FILESYSTEM_TYPE = 25
FLT_FSTYPE_MSFS: win32more.Windows.Win32.Storage.InstallableFileSystems.FLT_FILESYSTEM_TYPE = 26
FLT_FSTYPE_CSVFS: win32more.Windows.Win32.Storage.InstallableFileSystems.FLT_FILESYSTEM_TYPE = 27
FLT_FSTYPE_REFS: win32more.Windows.Win32.Storage.InstallableFileSystems.FLT_FILESYSTEM_TYPE = 28
FLT_FSTYPE_OPENAFS: win32more.Windows.Win32.Storage.InstallableFileSystems.FLT_FILESYSTEM_TYPE = 29
FLT_FSTYPE_CIMFS: win32more.Windows.Win32.Storage.InstallableFileSystems.FLT_FILESYSTEM_TYPE = 30
HFILTER = IntPtr
HFILTER_INSTANCE = IntPtr
class INSTANCE_AGGREGATE_STANDARD_INFORMATION(Structure):
    NextEntryOffset: UInt32
    Flags: UInt32
    Type: _Type_e__Union
    class _Type_e__Union(Union):
        MiniFilter: _MiniFilter_e__Struct
        LegacyFilter: _LegacyFilter_e__Struct
        class _MiniFilter_e__Struct(Structure):
            Flags: UInt32
            FrameID: UInt32
            VolumeFileSystemType: win32more.Windows.Win32.Storage.InstallableFileSystems.FLT_FILESYSTEM_TYPE
            InstanceNameLength: UInt16
            InstanceNameBufferOffset: UInt16
            AltitudeLength: UInt16
            AltitudeBufferOffset: UInt16
            VolumeNameLength: UInt16
            VolumeNameBufferOffset: UInt16
            FilterNameLength: UInt16
            FilterNameBufferOffset: UInt16
            SupportedFeatures: UInt32
        class _LegacyFilter_e__Struct(Structure):
            Flags: UInt32
            AltitudeLength: UInt16
            AltitudeBufferOffset: UInt16
            VolumeNameLength: UInt16
            VolumeNameBufferOffset: UInt16
            FilterNameLength: UInt16
            FilterNameBufferOffset: UInt16
            SupportedFeatures: UInt32
class INSTANCE_BASIC_INFORMATION(Structure):
    NextEntryOffset: UInt32
    InstanceNameLength: UInt16
    InstanceNameBufferOffset: UInt16
class INSTANCE_FULL_INFORMATION(Structure):
    NextEntryOffset: UInt32
    InstanceNameLength: UInt16
    InstanceNameBufferOffset: UInt16
    AltitudeLength: UInt16
    AltitudeBufferOffset: UInt16
    VolumeNameLength: UInt16
    VolumeNameBufferOffset: UInt16
    FilterNameLength: UInt16
    FilterNameBufferOffset: UInt16
INSTANCE_INFORMATION_CLASS = Int32
InstanceBasicInformation: win32more.Windows.Win32.Storage.InstallableFileSystems.INSTANCE_INFORMATION_CLASS = 0
InstancePartialInformation: win32more.Windows.Win32.Storage.InstallableFileSystems.INSTANCE_INFORMATION_CLASS = 1
InstanceFullInformation: win32more.Windows.Win32.Storage.InstallableFileSystems.INSTANCE_INFORMATION_CLASS = 2
InstanceAggregateStandardInformation: win32more.Windows.Win32.Storage.InstallableFileSystems.INSTANCE_INFORMATION_CLASS = 3
class INSTANCE_PARTIAL_INFORMATION(Structure):
    NextEntryOffset: UInt32
    InstanceNameLength: UInt16
    InstanceNameBufferOffset: UInt16
    AltitudeLength: UInt16
    AltitudeBufferOffset: UInt16


make_ready(__name__)
