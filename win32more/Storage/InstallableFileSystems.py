from win32more import *
import win32more.Foundation
import win32more.Security
import win32more.Storage.InstallableFileSystems
import win32more.System.IO

def __getattr__(name):
    module = globals()
    try:
        f = module[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    module[name] = f()
    return module[name]
def __dir__():
    return __all__
FILTER_NAME_MAX_CHARS = 255
VOLUME_NAME_MAX_CHARS = 1024
INSTANCE_NAME_MAX_CHARS = 255
FLTFL_AGGREGATE_INFO_IS_MINIFILTER = 1
FLTFL_AGGREGATE_INFO_IS_LEGACYFILTER = 2
FLTFL_ASI_IS_MINIFILTER = 1
FLTFL_ASI_IS_LEGACYFILTER = 2
FLTFL_VSI_DETACHED_VOLUME = 1
FLTFL_IASI_IS_MINIFILTER = 1
FLTFL_IASI_IS_LEGACYFILTER = 2
FLTFL_IASIM_DETACHED_VOLUME = 1
FLTFL_IASIL_DETACHED_VOLUME = 1
FLT_PORT_FLAG_SYNC_HANDLE = 1
WNNC_NET_MSNET = 65536
WNNC_NET_SMB = 131072
WNNC_NET_NETWARE = 196608
WNNC_NET_VINES = 262144
WNNC_NET_10NET = 327680
WNNC_NET_LOCUS = 393216
WNNC_NET_SUN_PC_NFS = 458752
WNNC_NET_LANSTEP = 524288
WNNC_NET_9TILES = 589824
WNNC_NET_LANTASTIC = 655360
WNNC_NET_AS400 = 720896
WNNC_NET_FTP_NFS = 786432
WNNC_NET_PATHWORKS = 851968
WNNC_NET_LIFENET = 917504
WNNC_NET_POWERLAN = 983040
WNNC_NET_BWNFS = 1048576
WNNC_NET_COGENT = 1114112
WNNC_NET_FARALLON = 1179648
WNNC_NET_APPLETALK = 1245184
WNNC_NET_INTERGRAPH = 1310720
WNNC_NET_SYMFONET = 1376256
WNNC_NET_CLEARCASE = 1441792
WNNC_NET_FRONTIER = 1507328
WNNC_NET_BMC = 1572864
WNNC_NET_DCE = 1638400
WNNC_NET_AVID = 1703936
WNNC_NET_DOCUSPACE = 1769472
WNNC_NET_MANGOSOFT = 1835008
WNNC_NET_SERNET = 1900544
WNNC_NET_RIVERFRONT1 = 1966080
WNNC_NET_RIVERFRONT2 = 2031616
WNNC_NET_DECORB = 2097152
WNNC_NET_PROTSTOR = 2162688
WNNC_NET_FJ_REDIR = 2228224
WNNC_NET_DISTINCT = 2293760
WNNC_NET_TWINS = 2359296
WNNC_NET_RDR2SAMPLE = 2424832
WNNC_NET_CSC = 2490368
WNNC_NET_3IN1 = 2555904
WNNC_NET_EXTENDNET = 2686976
WNNC_NET_STAC = 2752512
WNNC_NET_FOXBAT = 2818048
WNNC_NET_YAHOO = 2883584
WNNC_NET_EXIFS = 2949120
WNNC_NET_DAV = 3014656
WNNC_NET_KNOWARE = 3080192
WNNC_NET_OBJECT_DIRE = 3145728
WNNC_NET_MASFAX = 3211264
WNNC_NET_HOB_NFS = 3276800
WNNC_NET_SHIVA = 3342336
WNNC_NET_IBMAL = 3407872
WNNC_NET_LOCK = 3473408
WNNC_NET_TERMSRV = 3538944
WNNC_NET_SRT = 3604480
WNNC_NET_QUINCY = 3670016
WNNC_NET_OPENAFS = 3735552
WNNC_NET_AVID1 = 3801088
WNNC_NET_DFS = 3866624
WNNC_NET_KWNP = 3932160
WNNC_NET_ZENWORKS = 3997696
WNNC_NET_DRIVEONWEB = 4063232
WNNC_NET_VMWARE = 4128768
WNNC_NET_RSFX = 4194304
WNNC_NET_MFILES = 4259840
WNNC_NET_MS_NFS = 4325376
WNNC_NET_GOOGLE = 4390912
WNNC_NET_NDFS = 4456448
WNNC_NET_DOCUSHARE = 4521984
WNNC_NET_AURISTOR_FS = 4587520
WNNC_NET_SECUREAGENT = 4653056
WNNC_NET_9P = 4718592
WNNC_CRED_MANAGER = 4294901760
WNNC_NET_LANMAN = 131072
HFILTER = IntPtr
HFILTER_INSTANCE = IntPtr
FilterFindHandle = IntPtr
FilterVolumeFindHandle = IntPtr
FilterInstanceFindHandle = IntPtr
FilterVolumeInstanceFindHandle = IntPtr
FLT_FILESYSTEM_TYPE = Int32
FLT_FSTYPE_UNKNOWN = 0
FLT_FSTYPE_RAW = 1
FLT_FSTYPE_NTFS = 2
FLT_FSTYPE_FAT = 3
FLT_FSTYPE_CDFS = 4
FLT_FSTYPE_UDFS = 5
FLT_FSTYPE_LANMAN = 6
FLT_FSTYPE_WEBDAV = 7
FLT_FSTYPE_RDPDR = 8
FLT_FSTYPE_NFS = 9
FLT_FSTYPE_MS_NETWARE = 10
FLT_FSTYPE_NETWARE = 11
FLT_FSTYPE_BSUDF = 12
FLT_FSTYPE_MUP = 13
FLT_FSTYPE_RSFX = 14
FLT_FSTYPE_ROXIO_UDF1 = 15
FLT_FSTYPE_ROXIO_UDF2 = 16
FLT_FSTYPE_ROXIO_UDF3 = 17
FLT_FSTYPE_TACIT = 18
FLT_FSTYPE_FS_REC = 19
FLT_FSTYPE_INCD = 20
FLT_FSTYPE_INCD_FAT = 21
FLT_FSTYPE_EXFAT = 22
FLT_FSTYPE_PSFS = 23
FLT_FSTYPE_GPFS = 24
FLT_FSTYPE_NPFS = 25
FLT_FSTYPE_MSFS = 26
FLT_FSTYPE_CSVFS = 27
FLT_FSTYPE_REFS = 28
FLT_FSTYPE_OPENAFS = 29
FLT_FSTYPE_CIMFS = 30
FILTER_INFORMATION_CLASS = Int32
FILTER_INFORMATION_CLASS_FilterFullInformation = 0
FILTER_INFORMATION_CLASS_FilterAggregateBasicInformation = 1
FILTER_INFORMATION_CLASS_FilterAggregateStandardInformation = 2
def _define_FILTER_FULL_INFORMATION_head():
    class FILTER_FULL_INFORMATION(Structure):
        pass
    return FILTER_FULL_INFORMATION
def _define_FILTER_FULL_INFORMATION():
    FILTER_FULL_INFORMATION = win32more.Storage.InstallableFileSystems.FILTER_FULL_INFORMATION_head
    FILTER_FULL_INFORMATION._fields_ = [
        ("NextEntryOffset", UInt32),
        ("FrameID", UInt32),
        ("NumberOfInstances", UInt32),
        ("FilterNameLength", UInt16),
        ("FilterNameBuffer", Char * 0),
    ]
    return FILTER_FULL_INFORMATION
def _define_FILTER_AGGREGATE_BASIC_INFORMATION_head():
    class FILTER_AGGREGATE_BASIC_INFORMATION(Structure):
        pass
    return FILTER_AGGREGATE_BASIC_INFORMATION
def _define_FILTER_AGGREGATE_BASIC_INFORMATION():
    FILTER_AGGREGATE_BASIC_INFORMATION = win32more.Storage.InstallableFileSystems.FILTER_AGGREGATE_BASIC_INFORMATION_head
    class FILTER_AGGREGATE_BASIC_INFORMATION__Type_e__Union(Union):
        pass
    class FILTER_AGGREGATE_BASIC_INFORMATION__Type_e__Union__MiniFilter_e__Struct(Structure):
        pass
    FILTER_AGGREGATE_BASIC_INFORMATION__Type_e__Union__MiniFilter_e__Struct._fields_ = [
        ("FrameID", UInt32),
        ("NumberOfInstances", UInt32),
        ("FilterNameLength", UInt16),
        ("FilterNameBufferOffset", UInt16),
        ("FilterAltitudeLength", UInt16),
        ("FilterAltitudeBufferOffset", UInt16),
    ]
    class FILTER_AGGREGATE_BASIC_INFORMATION__Type_e__Union__LegacyFilter_e__Struct(Structure):
        pass
    FILTER_AGGREGATE_BASIC_INFORMATION__Type_e__Union__LegacyFilter_e__Struct._fields_ = [
        ("FilterNameLength", UInt16),
        ("FilterNameBufferOffset", UInt16),
    ]
    FILTER_AGGREGATE_BASIC_INFORMATION__Type_e__Union._fields_ = [
        ("MiniFilter", FILTER_AGGREGATE_BASIC_INFORMATION__Type_e__Union__MiniFilter_e__Struct),
        ("LegacyFilter", FILTER_AGGREGATE_BASIC_INFORMATION__Type_e__Union__LegacyFilter_e__Struct),
    ]
    FILTER_AGGREGATE_BASIC_INFORMATION._fields_ = [
        ("NextEntryOffset", UInt32),
        ("Flags", UInt32),
        ("Type", FILTER_AGGREGATE_BASIC_INFORMATION__Type_e__Union),
    ]
    return FILTER_AGGREGATE_BASIC_INFORMATION
def _define_FILTER_AGGREGATE_STANDARD_INFORMATION_head():
    class FILTER_AGGREGATE_STANDARD_INFORMATION(Structure):
        pass
    return FILTER_AGGREGATE_STANDARD_INFORMATION
def _define_FILTER_AGGREGATE_STANDARD_INFORMATION():
    FILTER_AGGREGATE_STANDARD_INFORMATION = win32more.Storage.InstallableFileSystems.FILTER_AGGREGATE_STANDARD_INFORMATION_head
    class FILTER_AGGREGATE_STANDARD_INFORMATION__Type_e__Union(Union):
        pass
    class FILTER_AGGREGATE_STANDARD_INFORMATION__Type_e__Union__MiniFilter_e__Struct(Structure):
        pass
    FILTER_AGGREGATE_STANDARD_INFORMATION__Type_e__Union__MiniFilter_e__Struct._fields_ = [
        ("Flags", UInt32),
        ("FrameID", UInt32),
        ("NumberOfInstances", UInt32),
        ("FilterNameLength", UInt16),
        ("FilterNameBufferOffset", UInt16),
        ("FilterAltitudeLength", UInt16),
        ("FilterAltitudeBufferOffset", UInt16),
    ]
    class FILTER_AGGREGATE_STANDARD_INFORMATION__Type_e__Union__LegacyFilter_e__Struct(Structure):
        pass
    FILTER_AGGREGATE_STANDARD_INFORMATION__Type_e__Union__LegacyFilter_e__Struct._fields_ = [
        ("Flags", UInt32),
        ("FilterNameLength", UInt16),
        ("FilterNameBufferOffset", UInt16),
        ("FilterAltitudeLength", UInt16),
        ("FilterAltitudeBufferOffset", UInt16),
    ]
    FILTER_AGGREGATE_STANDARD_INFORMATION__Type_e__Union._fields_ = [
        ("MiniFilter", FILTER_AGGREGATE_STANDARD_INFORMATION__Type_e__Union__MiniFilter_e__Struct),
        ("LegacyFilter", FILTER_AGGREGATE_STANDARD_INFORMATION__Type_e__Union__LegacyFilter_e__Struct),
    ]
    FILTER_AGGREGATE_STANDARD_INFORMATION._fields_ = [
        ("NextEntryOffset", UInt32),
        ("Flags", UInt32),
        ("Type", FILTER_AGGREGATE_STANDARD_INFORMATION__Type_e__Union),
    ]
    return FILTER_AGGREGATE_STANDARD_INFORMATION
FILTER_VOLUME_INFORMATION_CLASS = Int32
FILTER_VOLUME_INFORMATION_CLASS_FilterVolumeBasicInformation = 0
FILTER_VOLUME_INFORMATION_CLASS_FilterVolumeStandardInformation = 1
def _define_FILTER_VOLUME_BASIC_INFORMATION_head():
    class FILTER_VOLUME_BASIC_INFORMATION(Structure):
        pass
    return FILTER_VOLUME_BASIC_INFORMATION
def _define_FILTER_VOLUME_BASIC_INFORMATION():
    FILTER_VOLUME_BASIC_INFORMATION = win32more.Storage.InstallableFileSystems.FILTER_VOLUME_BASIC_INFORMATION_head
    FILTER_VOLUME_BASIC_INFORMATION._fields_ = [
        ("FilterVolumeNameLength", UInt16),
        ("FilterVolumeName", Char * 0),
    ]
    return FILTER_VOLUME_BASIC_INFORMATION
def _define_FILTER_VOLUME_STANDARD_INFORMATION_head():
    class FILTER_VOLUME_STANDARD_INFORMATION(Structure):
        pass
    return FILTER_VOLUME_STANDARD_INFORMATION
def _define_FILTER_VOLUME_STANDARD_INFORMATION():
    FILTER_VOLUME_STANDARD_INFORMATION = win32more.Storage.InstallableFileSystems.FILTER_VOLUME_STANDARD_INFORMATION_head
    FILTER_VOLUME_STANDARD_INFORMATION._fields_ = [
        ("NextEntryOffset", UInt32),
        ("Flags", UInt32),
        ("FrameID", UInt32),
        ("FileSystemType", win32more.Storage.InstallableFileSystems.FLT_FILESYSTEM_TYPE),
        ("FilterVolumeNameLength", UInt16),
        ("FilterVolumeName", Char * 0),
    ]
    return FILTER_VOLUME_STANDARD_INFORMATION
INSTANCE_INFORMATION_CLASS = Int32
INSTANCE_INFORMATION_CLASS_InstanceBasicInformation = 0
INSTANCE_INFORMATION_CLASS_InstancePartialInformation = 1
INSTANCE_INFORMATION_CLASS_InstanceFullInformation = 2
INSTANCE_INFORMATION_CLASS_InstanceAggregateStandardInformation = 3
def _define_INSTANCE_BASIC_INFORMATION_head():
    class INSTANCE_BASIC_INFORMATION(Structure):
        pass
    return INSTANCE_BASIC_INFORMATION
def _define_INSTANCE_BASIC_INFORMATION():
    INSTANCE_BASIC_INFORMATION = win32more.Storage.InstallableFileSystems.INSTANCE_BASIC_INFORMATION_head
    INSTANCE_BASIC_INFORMATION._fields_ = [
        ("NextEntryOffset", UInt32),
        ("InstanceNameLength", UInt16),
        ("InstanceNameBufferOffset", UInt16),
    ]
    return INSTANCE_BASIC_INFORMATION
def _define_INSTANCE_PARTIAL_INFORMATION_head():
    class INSTANCE_PARTIAL_INFORMATION(Structure):
        pass
    return INSTANCE_PARTIAL_INFORMATION
def _define_INSTANCE_PARTIAL_INFORMATION():
    INSTANCE_PARTIAL_INFORMATION = win32more.Storage.InstallableFileSystems.INSTANCE_PARTIAL_INFORMATION_head
    INSTANCE_PARTIAL_INFORMATION._fields_ = [
        ("NextEntryOffset", UInt32),
        ("InstanceNameLength", UInt16),
        ("InstanceNameBufferOffset", UInt16),
        ("AltitudeLength", UInt16),
        ("AltitudeBufferOffset", UInt16),
    ]
    return INSTANCE_PARTIAL_INFORMATION
def _define_INSTANCE_FULL_INFORMATION_head():
    class INSTANCE_FULL_INFORMATION(Structure):
        pass
    return INSTANCE_FULL_INFORMATION
def _define_INSTANCE_FULL_INFORMATION():
    INSTANCE_FULL_INFORMATION = win32more.Storage.InstallableFileSystems.INSTANCE_FULL_INFORMATION_head
    INSTANCE_FULL_INFORMATION._fields_ = [
        ("NextEntryOffset", UInt32),
        ("InstanceNameLength", UInt16),
        ("InstanceNameBufferOffset", UInt16),
        ("AltitudeLength", UInt16),
        ("AltitudeBufferOffset", UInt16),
        ("VolumeNameLength", UInt16),
        ("VolumeNameBufferOffset", UInt16),
        ("FilterNameLength", UInt16),
        ("FilterNameBufferOffset", UInt16),
    ]
    return INSTANCE_FULL_INFORMATION
def _define_INSTANCE_AGGREGATE_STANDARD_INFORMATION_head():
    class INSTANCE_AGGREGATE_STANDARD_INFORMATION(Structure):
        pass
    return INSTANCE_AGGREGATE_STANDARD_INFORMATION
def _define_INSTANCE_AGGREGATE_STANDARD_INFORMATION():
    INSTANCE_AGGREGATE_STANDARD_INFORMATION = win32more.Storage.InstallableFileSystems.INSTANCE_AGGREGATE_STANDARD_INFORMATION_head
    class INSTANCE_AGGREGATE_STANDARD_INFORMATION__Type_e__Union(Union):
        pass
    class INSTANCE_AGGREGATE_STANDARD_INFORMATION__Type_e__Union__MiniFilter_e__Struct(Structure):
        pass
    INSTANCE_AGGREGATE_STANDARD_INFORMATION__Type_e__Union__MiniFilter_e__Struct._fields_ = [
        ("Flags", UInt32),
        ("FrameID", UInt32),
        ("VolumeFileSystemType", win32more.Storage.InstallableFileSystems.FLT_FILESYSTEM_TYPE),
        ("InstanceNameLength", UInt16),
        ("InstanceNameBufferOffset", UInt16),
        ("AltitudeLength", UInt16),
        ("AltitudeBufferOffset", UInt16),
        ("VolumeNameLength", UInt16),
        ("VolumeNameBufferOffset", UInt16),
        ("FilterNameLength", UInt16),
        ("FilterNameBufferOffset", UInt16),
        ("SupportedFeatures", UInt32),
    ]
    class INSTANCE_AGGREGATE_STANDARD_INFORMATION__Type_e__Union__LegacyFilter_e__Struct(Structure):
        pass
    INSTANCE_AGGREGATE_STANDARD_INFORMATION__Type_e__Union__LegacyFilter_e__Struct._fields_ = [
        ("Flags", UInt32),
        ("AltitudeLength", UInt16),
        ("AltitudeBufferOffset", UInt16),
        ("VolumeNameLength", UInt16),
        ("VolumeNameBufferOffset", UInt16),
        ("FilterNameLength", UInt16),
        ("FilterNameBufferOffset", UInt16),
        ("SupportedFeatures", UInt32),
    ]
    INSTANCE_AGGREGATE_STANDARD_INFORMATION__Type_e__Union._fields_ = [
        ("MiniFilter", INSTANCE_AGGREGATE_STANDARD_INFORMATION__Type_e__Union__MiniFilter_e__Struct),
        ("LegacyFilter", INSTANCE_AGGREGATE_STANDARD_INFORMATION__Type_e__Union__LegacyFilter_e__Struct),
    ]
    INSTANCE_AGGREGATE_STANDARD_INFORMATION._fields_ = [
        ("NextEntryOffset", UInt32),
        ("Flags", UInt32),
        ("Type", INSTANCE_AGGREGATE_STANDARD_INFORMATION__Type_e__Union),
    ]
    return INSTANCE_AGGREGATE_STANDARD_INFORMATION
def _define_FILTER_MESSAGE_HEADER_head():
    class FILTER_MESSAGE_HEADER(Structure):
        pass
    return FILTER_MESSAGE_HEADER
def _define_FILTER_MESSAGE_HEADER():
    FILTER_MESSAGE_HEADER = win32more.Storage.InstallableFileSystems.FILTER_MESSAGE_HEADER_head
    FILTER_MESSAGE_HEADER._fields_ = [
        ("ReplyLength", UInt32),
        ("MessageId", UInt64),
    ]
    return FILTER_MESSAGE_HEADER
def _define_FILTER_REPLY_HEADER_head():
    class FILTER_REPLY_HEADER(Structure):
        pass
    return FILTER_REPLY_HEADER
def _define_FILTER_REPLY_HEADER():
    FILTER_REPLY_HEADER = win32more.Storage.InstallableFileSystems.FILTER_REPLY_HEADER_head
    FILTER_REPLY_HEADER._fields_ = [
        ("Status", win32more.Foundation.NTSTATUS),
        ("MessageId", UInt64),
    ]
    return FILTER_REPLY_HEADER
def _define_FilterLoad():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(("FilterLoad", windll["FLTLIB"]), ((1, 'lpFilterName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FilterUnload():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(("FilterUnload", windll["FLTLIB"]), ((1, 'lpFilterName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FilterCreate():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Storage.InstallableFileSystems.HFILTER), use_last_error=False)(("FilterCreate", windll["FLTLIB"]), ((1, 'lpFilterName'),(1, 'hFilter'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FilterClose():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.InstallableFileSystems.HFILTER, use_last_error=False)(("FilterClose", windll["FLTLIB"]), ((1, 'hFilter'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FilterInstanceCreate():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Storage.InstallableFileSystems.HFILTER_INSTANCE), use_last_error=False)(("FilterInstanceCreate", windll["FLTLIB"]), ((1, 'lpFilterName'),(1, 'lpVolumeName'),(1, 'lpInstanceName'),(1, 'hInstance'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FilterInstanceClose():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.InstallableFileSystems.HFILTER_INSTANCE, use_last_error=False)(("FilterInstanceClose", windll["FLTLIB"]), ((1, 'hInstance'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FilterAttach():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR, use_last_error=False)(("FilterAttach", windll["FLTLIB"]), ((1, 'lpFilterName'),(1, 'lpVolumeName'),(1, 'lpInstanceName'),(1, 'dwCreatedInstanceNameLength'),(1, 'lpCreatedInstanceName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FilterAttachAtAltitude():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR, use_last_error=False)(("FilterAttachAtAltitude", windll["FLTLIB"]), ((1, 'lpFilterName'),(1, 'lpVolumeName'),(1, 'lpAltitude'),(1, 'lpInstanceName'),(1, 'dwCreatedInstanceNameLength'),(1, 'lpCreatedInstanceName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FilterDetach():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("FilterDetach", windll["FLTLIB"]), ((1, 'lpFilterName'),(1, 'lpVolumeName'),(1, 'lpInstanceName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FilterFindFirst():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.InstallableFileSystems.FILTER_INFORMATION_CLASS,c_void_p,UInt32,POINTER(UInt32),POINTER(win32more.Storage.InstallableFileSystems.FilterFindHandle), use_last_error=False)(("FilterFindFirst", windll["FLTLIB"]), ((1, 'dwInformationClass'),(1, 'lpBuffer'),(1, 'dwBufferSize'),(1, 'lpBytesReturned'),(1, 'lpFilterFind'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FilterFindNext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,win32more.Storage.InstallableFileSystems.FILTER_INFORMATION_CLASS,c_void_p,UInt32,POINTER(UInt32), use_last_error=False)(("FilterFindNext", windll["FLTLIB"]), ((1, 'hFilterFind'),(1, 'dwInformationClass'),(1, 'lpBuffer'),(1, 'dwBufferSize'),(1, 'lpBytesReturned'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FilterFindClose():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE, use_last_error=False)(("FilterFindClose", windll["FLTLIB"]), ((1, 'hFilterFind'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FilterVolumeFindFirst():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.InstallableFileSystems.FILTER_VOLUME_INFORMATION_CLASS,c_void_p,UInt32,POINTER(UInt32),POINTER(win32more.Storage.InstallableFileSystems.FilterVolumeFindHandle), use_last_error=False)(("FilterVolumeFindFirst", windll["FLTLIB"]), ((1, 'dwInformationClass'),(1, 'lpBuffer'),(1, 'dwBufferSize'),(1, 'lpBytesReturned'),(1, 'lpVolumeFind'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FilterVolumeFindNext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,win32more.Storage.InstallableFileSystems.FILTER_VOLUME_INFORMATION_CLASS,c_void_p,UInt32,POINTER(UInt32), use_last_error=False)(("FilterVolumeFindNext", windll["FLTLIB"]), ((1, 'hVolumeFind'),(1, 'dwInformationClass'),(1, 'lpBuffer'),(1, 'dwBufferSize'),(1, 'lpBytesReturned'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FilterVolumeFindClose():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE, use_last_error=False)(("FilterVolumeFindClose", windll["FLTLIB"]), ((1, 'hVolumeFind'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FilterInstanceFindFirst():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Storage.InstallableFileSystems.INSTANCE_INFORMATION_CLASS,c_void_p,UInt32,POINTER(UInt32),POINTER(win32more.Storage.InstallableFileSystems.FilterInstanceFindHandle), use_last_error=False)(("FilterInstanceFindFirst", windll["FLTLIB"]), ((1, 'lpFilterName'),(1, 'dwInformationClass'),(1, 'lpBuffer'),(1, 'dwBufferSize'),(1, 'lpBytesReturned'),(1, 'lpFilterInstanceFind'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FilterInstanceFindNext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,win32more.Storage.InstallableFileSystems.INSTANCE_INFORMATION_CLASS,c_void_p,UInt32,POINTER(UInt32), use_last_error=False)(("FilterInstanceFindNext", windll["FLTLIB"]), ((1, 'hFilterInstanceFind'),(1, 'dwInformationClass'),(1, 'lpBuffer'),(1, 'dwBufferSize'),(1, 'lpBytesReturned'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FilterInstanceFindClose():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE, use_last_error=False)(("FilterInstanceFindClose", windll["FLTLIB"]), ((1, 'hFilterInstanceFind'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FilterVolumeInstanceFindFirst():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Storage.InstallableFileSystems.INSTANCE_INFORMATION_CLASS,c_void_p,UInt32,POINTER(UInt32),POINTER(win32more.Storage.InstallableFileSystems.FilterVolumeInstanceFindHandle), use_last_error=False)(("FilterVolumeInstanceFindFirst", windll["FLTLIB"]), ((1, 'lpVolumeName'),(1, 'dwInformationClass'),(1, 'lpBuffer'),(1, 'dwBufferSize'),(1, 'lpBytesReturned'),(1, 'lpVolumeInstanceFind'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FilterVolumeInstanceFindNext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,win32more.Storage.InstallableFileSystems.INSTANCE_INFORMATION_CLASS,c_void_p,UInt32,POINTER(UInt32), use_last_error=False)(("FilterVolumeInstanceFindNext", windll["FLTLIB"]), ((1, 'hVolumeInstanceFind'),(1, 'dwInformationClass'),(1, 'lpBuffer'),(1, 'dwBufferSize'),(1, 'lpBytesReturned'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FilterVolumeInstanceFindClose():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE, use_last_error=False)(("FilterVolumeInstanceFindClose", windll["FLTLIB"]), ((1, 'hVolumeInstanceFind'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FilterGetInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.InstallableFileSystems.HFILTER,win32more.Storage.InstallableFileSystems.FILTER_INFORMATION_CLASS,c_void_p,UInt32,POINTER(UInt32), use_last_error=False)(("FilterGetInformation", windll["FLTLIB"]), ((1, 'hFilter'),(1, 'dwInformationClass'),(1, 'lpBuffer'),(1, 'dwBufferSize'),(1, 'lpBytesReturned'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FilterInstanceGetInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.InstallableFileSystems.HFILTER_INSTANCE,win32more.Storage.InstallableFileSystems.INSTANCE_INFORMATION_CLASS,c_void_p,UInt32,POINTER(UInt32), use_last_error=False)(("FilterInstanceGetInformation", windll["FLTLIB"]), ((1, 'hInstance'),(1, 'dwInformationClass'),(1, 'lpBuffer'),(1, 'dwBufferSize'),(1, 'lpBytesReturned'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FilterConnectCommunicationPort():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,c_void_p,UInt16,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("FilterConnectCommunicationPort", windll["FLTLIB"]), ((1, 'lpPortName'),(1, 'dwOptions'),(1, 'lpContext'),(1, 'wSizeOfContext'),(1, 'lpSecurityAttributes'),(1, 'hPort'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FilterSendMessage():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,c_void_p,UInt32,c_void_p,UInt32,POINTER(UInt32), use_last_error=False)(("FilterSendMessage", windll["FLTLIB"]), ((1, 'hPort'),(1, 'lpInBuffer'),(1, 'dwInBufferSize'),(1, 'lpOutBuffer'),(1, 'dwOutBufferSize'),(1, 'lpBytesReturned'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FilterGetMessage():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(win32more.Storage.InstallableFileSystems.FILTER_MESSAGE_HEADER_head),UInt32,POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(("FilterGetMessage", windll["FLTLIB"]), ((1, 'hPort'),(1, 'lpMessageBuffer'),(1, 'dwMessageBufferSize'),(1, 'lpOverlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FilterReplyMessage():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(win32more.Storage.InstallableFileSystems.FILTER_REPLY_HEADER_head),UInt32, use_last_error=False)(("FilterReplyMessage", windll["FLTLIB"]), ((1, 'hPort'),(1, 'lpReplyBuffer'),(1, 'dwReplyBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FilterGetDosName():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Char),UInt32, use_last_error=False)(("FilterGetDosName", windll["FLTLIB"]), ((1, 'lpVolumeName'),(1, 'lpDosName'),(1, 'dwDosNameBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "FILTER_NAME_MAX_CHARS",
    "VOLUME_NAME_MAX_CHARS",
    "INSTANCE_NAME_MAX_CHARS",
    "FLTFL_AGGREGATE_INFO_IS_MINIFILTER",
    "FLTFL_AGGREGATE_INFO_IS_LEGACYFILTER",
    "FLTFL_ASI_IS_MINIFILTER",
    "FLTFL_ASI_IS_LEGACYFILTER",
    "FLTFL_VSI_DETACHED_VOLUME",
    "FLTFL_IASI_IS_MINIFILTER",
    "FLTFL_IASI_IS_LEGACYFILTER",
    "FLTFL_IASIM_DETACHED_VOLUME",
    "FLTFL_IASIL_DETACHED_VOLUME",
    "FLT_PORT_FLAG_SYNC_HANDLE",
    "WNNC_NET_MSNET",
    "WNNC_NET_SMB",
    "WNNC_NET_NETWARE",
    "WNNC_NET_VINES",
    "WNNC_NET_10NET",
    "WNNC_NET_LOCUS",
    "WNNC_NET_SUN_PC_NFS",
    "WNNC_NET_LANSTEP",
    "WNNC_NET_9TILES",
    "WNNC_NET_LANTASTIC",
    "WNNC_NET_AS400",
    "WNNC_NET_FTP_NFS",
    "WNNC_NET_PATHWORKS",
    "WNNC_NET_LIFENET",
    "WNNC_NET_POWERLAN",
    "WNNC_NET_BWNFS",
    "WNNC_NET_COGENT",
    "WNNC_NET_FARALLON",
    "WNNC_NET_APPLETALK",
    "WNNC_NET_INTERGRAPH",
    "WNNC_NET_SYMFONET",
    "WNNC_NET_CLEARCASE",
    "WNNC_NET_FRONTIER",
    "WNNC_NET_BMC",
    "WNNC_NET_DCE",
    "WNNC_NET_AVID",
    "WNNC_NET_DOCUSPACE",
    "WNNC_NET_MANGOSOFT",
    "WNNC_NET_SERNET",
    "WNNC_NET_RIVERFRONT1",
    "WNNC_NET_RIVERFRONT2",
    "WNNC_NET_DECORB",
    "WNNC_NET_PROTSTOR",
    "WNNC_NET_FJ_REDIR",
    "WNNC_NET_DISTINCT",
    "WNNC_NET_TWINS",
    "WNNC_NET_RDR2SAMPLE",
    "WNNC_NET_CSC",
    "WNNC_NET_3IN1",
    "WNNC_NET_EXTENDNET",
    "WNNC_NET_STAC",
    "WNNC_NET_FOXBAT",
    "WNNC_NET_YAHOO",
    "WNNC_NET_EXIFS",
    "WNNC_NET_DAV",
    "WNNC_NET_KNOWARE",
    "WNNC_NET_OBJECT_DIRE",
    "WNNC_NET_MASFAX",
    "WNNC_NET_HOB_NFS",
    "WNNC_NET_SHIVA",
    "WNNC_NET_IBMAL",
    "WNNC_NET_LOCK",
    "WNNC_NET_TERMSRV",
    "WNNC_NET_SRT",
    "WNNC_NET_QUINCY",
    "WNNC_NET_OPENAFS",
    "WNNC_NET_AVID1",
    "WNNC_NET_DFS",
    "WNNC_NET_KWNP",
    "WNNC_NET_ZENWORKS",
    "WNNC_NET_DRIVEONWEB",
    "WNNC_NET_VMWARE",
    "WNNC_NET_RSFX",
    "WNNC_NET_MFILES",
    "WNNC_NET_MS_NFS",
    "WNNC_NET_GOOGLE",
    "WNNC_NET_NDFS",
    "WNNC_NET_DOCUSHARE",
    "WNNC_NET_AURISTOR_FS",
    "WNNC_NET_SECUREAGENT",
    "WNNC_NET_9P",
    "WNNC_CRED_MANAGER",
    "WNNC_NET_LANMAN",
    "HFILTER",
    "HFILTER_INSTANCE",
    "FilterFindHandle",
    "FilterVolumeFindHandle",
    "FilterInstanceFindHandle",
    "FilterVolumeInstanceFindHandle",
    "FLT_FILESYSTEM_TYPE",
    "FLT_FSTYPE_UNKNOWN",
    "FLT_FSTYPE_RAW",
    "FLT_FSTYPE_NTFS",
    "FLT_FSTYPE_FAT",
    "FLT_FSTYPE_CDFS",
    "FLT_FSTYPE_UDFS",
    "FLT_FSTYPE_LANMAN",
    "FLT_FSTYPE_WEBDAV",
    "FLT_FSTYPE_RDPDR",
    "FLT_FSTYPE_NFS",
    "FLT_FSTYPE_MS_NETWARE",
    "FLT_FSTYPE_NETWARE",
    "FLT_FSTYPE_BSUDF",
    "FLT_FSTYPE_MUP",
    "FLT_FSTYPE_RSFX",
    "FLT_FSTYPE_ROXIO_UDF1",
    "FLT_FSTYPE_ROXIO_UDF2",
    "FLT_FSTYPE_ROXIO_UDF3",
    "FLT_FSTYPE_TACIT",
    "FLT_FSTYPE_FS_REC",
    "FLT_FSTYPE_INCD",
    "FLT_FSTYPE_INCD_FAT",
    "FLT_FSTYPE_EXFAT",
    "FLT_FSTYPE_PSFS",
    "FLT_FSTYPE_GPFS",
    "FLT_FSTYPE_NPFS",
    "FLT_FSTYPE_MSFS",
    "FLT_FSTYPE_CSVFS",
    "FLT_FSTYPE_REFS",
    "FLT_FSTYPE_OPENAFS",
    "FLT_FSTYPE_CIMFS",
    "FILTER_INFORMATION_CLASS",
    "FILTER_INFORMATION_CLASS_FilterFullInformation",
    "FILTER_INFORMATION_CLASS_FilterAggregateBasicInformation",
    "FILTER_INFORMATION_CLASS_FilterAggregateStandardInformation",
    "FILTER_FULL_INFORMATION",
    "FILTER_AGGREGATE_BASIC_INFORMATION",
    "FILTER_AGGREGATE_STANDARD_INFORMATION",
    "FILTER_VOLUME_INFORMATION_CLASS",
    "FILTER_VOLUME_INFORMATION_CLASS_FilterVolumeBasicInformation",
    "FILTER_VOLUME_INFORMATION_CLASS_FilterVolumeStandardInformation",
    "FILTER_VOLUME_BASIC_INFORMATION",
    "FILTER_VOLUME_STANDARD_INFORMATION",
    "INSTANCE_INFORMATION_CLASS",
    "INSTANCE_INFORMATION_CLASS_InstanceBasicInformation",
    "INSTANCE_INFORMATION_CLASS_InstancePartialInformation",
    "INSTANCE_INFORMATION_CLASS_InstanceFullInformation",
    "INSTANCE_INFORMATION_CLASS_InstanceAggregateStandardInformation",
    "INSTANCE_BASIC_INFORMATION",
    "INSTANCE_PARTIAL_INFORMATION",
    "INSTANCE_FULL_INFORMATION",
    "INSTANCE_AGGREGATE_STANDARD_INFORMATION",
    "FILTER_MESSAGE_HEADER",
    "FILTER_REPLY_HEADER",
    "FilterLoad",
    "FilterUnload",
    "FilterCreate",
    "FilterClose",
    "FilterInstanceCreate",
    "FilterInstanceClose",
    "FilterAttach",
    "FilterAttachAtAltitude",
    "FilterDetach",
    "FilterFindFirst",
    "FilterFindNext",
    "FilterFindClose",
    "FilterVolumeFindFirst",
    "FilterVolumeFindNext",
    "FilterVolumeFindClose",
    "FilterInstanceFindFirst",
    "FilterInstanceFindNext",
    "FilterInstanceFindClose",
    "FilterVolumeInstanceFindFirst",
    "FilterVolumeInstanceFindNext",
    "FilterVolumeInstanceFindClose",
    "FilterGetInformation",
    "FilterInstanceGetInformation",
    "FilterConnectCommunicationPort",
    "FilterSendMessage",
    "FilterGetMessage",
    "FilterReplyMessage",
    "FilterGetDosName",
]
