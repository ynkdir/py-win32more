from win32more import *
import win32more.Foundation
import win32more.Media.DeviceManager
import win32more.System.Com
import win32more.System.Com.StructuredStorage
import win32more.System.Ole

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
IOCTL_MTP_CUSTOM_COMMAND = 827348045
MTP_NEXTPHASE_READ_DATA = 1
MTP_NEXTPHASE_WRITE_DATA = 2
MTP_NEXTPHASE_NO_DATA = 3
RSA_KEY_LEN = 64
SAC_SESSION_KEYLEN = 8
SAC_PROTOCOL_WMDM = 1
SAC_PROTOCOL_V1 = 2
SAC_CERT_X509 = 1
SAC_CERT_V1 = 2
WMDM_DEVICE_PROTOCOL_MTP = '979e54e5-0afc-4604-8d93-dc798a4bcf45'
WMDM_DEVICE_PROTOCOL_RAPI = '2a11ed91-8c8f-41e4-82d1-8386e003561c'
WMDM_DEVICE_PROTOCOL_MSC = 'a4d2c26c-a881-44bb-bd5d-1f703c71f7a9'
WMDM_SERVICE_PROVIDER_VENDOR_MICROSOFT = '7de8686d-78ee-43ea-a496-c625ac91cc5d'
WMDMID_LENGTH = 128
WMDM_MAC_LENGTH = 8
WMDM_S_NOT_ALL_PROPERTIES_APPLIED = 282625
WMDM_S_NOT_ALL_PROPERTIES_RETRIEVED = 282626
WMDM_E_BUSY = -2147201024
WMDM_E_INTERFACEDEAD = -2147201023
WMDM_E_INVALIDTYPE = -2147201022
WMDM_E_PROCESSFAILED = -2147201021
WMDM_E_NOTSUPPORTED = -2147201020
WMDM_E_NOTCERTIFIED = -2147201019
WMDM_E_NORIGHTS = -2147201018
WMDM_E_CALL_OUT_OF_SEQUENCE = -2147201017
WMDM_E_BUFFERTOOSMALL = -2147201016
WMDM_E_MOREDATA = -2147201015
WMDM_E_MAC_CHECK_FAILED = -2147201014
WMDM_E_USER_CANCELLED = -2147201013
WMDM_E_SDMI_TRIGGER = -2147201012
WMDM_E_SDMI_NOMORECOPIES = -2147201011
WMDM_E_REVOKED = -2147201010
WMDM_E_LICENSE_NOTEXIST = -2147201009
WMDM_E_INCORRECT_APPSEC = -2147201008
WMDM_E_INCORRECT_RIGHTS = -2147201007
WMDM_E_LICENSE_EXPIRED = -2147201006
WMDM_E_CANTOPEN_PMSN_SERVICE_PIPE = -2147201005
WMDM_E_TOO_MANY_SESSIONS = -2147201005
WMDM_WMDM_REVOKED = 1
WMDM_APP_REVOKED = 2
WMDM_SP_REVOKED = 4
WMDM_SCP_REVOKED = 8
WMDM_GET_FORMAT_SUPPORT_AUDIO = 1
WMDM_GET_FORMAT_SUPPORT_VIDEO = 2
WMDM_GET_FORMAT_SUPPORT_FILE = 4
WMDM_RIGHTS_PLAYBACKCOUNT = 1
WMDM_RIGHTS_EXPIRATIONDATE = 2
WMDM_RIGHTS_GROUPID = 4
WMDM_RIGHTS_FREESERIALIDS = 8
WMDM_RIGHTS_NAMEDSERIALIDS = 16
WMDM_DEVICE_TYPE_PLAYBACK = 1
WMDM_DEVICE_TYPE_RECORD = 2
WMDM_DEVICE_TYPE_DECODE = 4
WMDM_DEVICE_TYPE_ENCODE = 8
WMDM_DEVICE_TYPE_STORAGE = 16
WMDM_DEVICE_TYPE_VIRTUAL = 32
WMDM_DEVICE_TYPE_SDMI = 64
WMDM_DEVICE_TYPE_NONSDMI = 128
WMDM_DEVICE_TYPE_NONREENTRANT = 256
WMDM_DEVICE_TYPE_FILELISTRESYNC = 512
WMDM_DEVICE_TYPE_VIEW_PREF_METADATAVIEW = 1024
WMDM_POWER_CAP_BATTERY = 1
WMDM_POWER_CAP_EXTERNAL = 2
WMDM_POWER_IS_BATTERY = 4
WMDM_POWER_IS_EXTERNAL = 8
WMDM_POWER_PERCENT_AVAILABLE = 16
WMDM_STATUS_READY = 1
WMDM_STATUS_BUSY = 2
WMDM_STATUS_DEVICE_NOTPRESENT = 4
WMDM_STATUS_DEVICECONTROL_PLAYING = 8
WMDM_STATUS_DEVICECONTROL_RECORDING = 16
WMDM_STATUS_DEVICECONTROL_PAUSED = 32
WMDM_STATUS_DEVICECONTROL_REMOTE = 64
WMDM_STATUS_DEVICECONTROL_STREAM = 128
WMDM_STATUS_STORAGE_NOTPRESENT = 256
WMDM_STATUS_STORAGE_INITIALIZING = 512
WMDM_STATUS_STORAGE_BROKEN = 1024
WMDM_STATUS_STORAGE_NOTSUPPORTED = 2048
WMDM_STATUS_STORAGE_UNFORMATTED = 4096
WMDM_STATUS_STORAGECONTROL_INSERTING = 8192
WMDM_STATUS_STORAGECONTROL_DELETING = 16384
WMDM_STATUS_STORAGECONTROL_APPENDING = 32768
WMDM_STATUS_STORAGECONTROL_MOVING = 65536
WMDM_STATUS_STORAGECONTROL_READING = 131072
WMDM_DEVICECAP_CANPLAY = 1
WMDM_DEVICECAP_CANSTREAMPLAY = 2
WMDM_DEVICECAP_CANRECORD = 4
WMDM_DEVICECAP_CANSTREAMRECORD = 8
WMDM_DEVICECAP_CANPAUSE = 16
WMDM_DEVICECAP_CANRESUME = 32
WMDM_DEVICECAP_CANSTOP = 64
WMDM_DEVICECAP_CANSEEK = 128
WMDM_DEVICECAP_HASSECURECLOCK = 256
WMDM_SEEK_REMOTECONTROL = 1
WMDM_SEEK_STREAMINGAUDIO = 2
WMDM_STORAGE_ATTR_FILESYSTEM = 1
WMDM_STORAGE_ATTR_REMOVABLE = 2
WMDM_STORAGE_ATTR_NONREMOVABLE = 4
WMDM_FILE_ATTR_FOLDER = 8
WMDM_FILE_ATTR_LINK = 16
WMDM_FILE_ATTR_FILE = 32
WMDM_FILE_ATTR_VIDEO = 64
WMDM_STORAGE_ATTR_CANEDITMETADATA = 128
WMDM_STORAGE_ATTR_FOLDERS = 256
WMDM_FILE_ATTR_AUDIO = 4096
WMDM_FILE_ATTR_DATA = 8192
WMDM_FILE_ATTR_CANPLAY = 16384
WMDM_FILE_ATTR_CANDELETE = 32768
WMDM_FILE_ATTR_CANMOVE = 65536
WMDM_FILE_ATTR_CANRENAME = 131072
WMDM_FILE_ATTR_CANREAD = 262144
WMDM_FILE_ATTR_MUSIC = 524288
WMDM_FILE_CREATE_OVERWRITE = 1048576
WMDM_FILE_ATTR_AUDIOBOOK = 2097152
WMDM_FILE_ATTR_HIDDEN = 4194304
WMDM_FILE_ATTR_SYSTEM = 8388608
WMDM_FILE_ATTR_READONLY = 16777216
WMDM_STORAGE_ATTR_HAS_FOLDERS = 33554432
WMDM_STORAGE_ATTR_HAS_FILES = 67108864
WMDM_STORAGE_IS_DEFAULT = 134217728
WMDM_STORAGE_CONTAINS_DEFAULT = 268435456
WMDM_STORAGE_ATTR_VIRTUAL = 536870912
WMDM_STORAGECAP_FOLDERSINROOT = 1
WMDM_STORAGECAP_FILESINROOT = 2
WMDM_STORAGECAP_FOLDERSINFOLDERS = 4
WMDM_STORAGECAP_FILESINFOLDERS = 8
WMDM_STORAGECAP_FOLDERLIMITEXISTS = 16
WMDM_STORAGECAP_FILELIMITEXISTS = 32
WMDM_STORAGECAP_NOT_INITIALIZABLE = 64
WMDM_MODE_BLOCK = 1
WMDM_MODE_THREAD = 2
WMDM_CONTENT_FILE = 4
WMDM_CONTENT_FOLDER = 8
WMDM_CONTENT_OPERATIONINTERFACE = 16
WMDM_MODE_QUERY = 32
WMDM_MODE_PROGRESS = 64
WMDM_MODE_TRANSFER_PROTECTED = 128
WMDM_MODE_TRANSFER_UNPROTECTED = 256
WMDM_STORAGECONTROL_INSERTBEFORE = 512
WMDM_STORAGECONTROL_INSERTAFTER = 1024
WMDM_STORAGECONTROL_INSERTINTO = 2048
WMDM_MODE_RECURSIVE = 4096
WMDM_RIGHTS_PLAY_ON_PC = 1
WMDM_RIGHTS_COPY_TO_NON_SDMI_DEVICE = 2
WMDM_RIGHTS_COPY_TO_CD = 8
WMDM_RIGHTS_COPY_TO_SDMI_DEVICE = 16
WMDM_SEEK_BEGIN = 1
WMDM_SEEK_CURRENT = 2
WMDM_SEEK_END = 8
DO_NOT_VIRTUALIZE_STORAGES_AS_DEVICES = 1
ALLOW_OUTOFBAND_NOTIFICATION = 2
MDSP_READ = 1
MDSP_WRITE = 2
MDSP_SEEK_BOF = 1
MDSP_SEEK_CUR = 2
MDSP_SEEK_EOF = 4
WMDM_SCP_EXAMINE_EXTENSION = 1
WMDM_SCP_EXAMINE_DATA = 2
WMDM_SCP_DECIDE_DATA = 8
WMDM_SCP_PROTECTED_OUTPUT = 16
WMDM_SCP_UNPROTECTED_OUTPUT = 32
WMDM_SCP_RIGHTS_DATA = 64
WMDM_SCP_TRANSFER_OBJECTDATA = 32
WMDM_SCP_NO_MORE_CHANGES = 64
WMDM_SCP_DRMINFO_NOT_DRMPROTECTED = 0
WMDM_SCP_DRMINFO_V1HEADER = 1
WMDM_SCP_DRMINFO_V2HEADER = 2
SCP_EVENTID_ACQSECURECLOCK = '86248cc9-4a59-43e2-9146-48a7f3f4140c'
SCP_EVENTID_NEEDTOINDIV = '87a507c7-b469-4386-b976-d5d1ce538a6f'
SCP_EVENTID_DRMINFO = '213dd287-41d2-432b-9e3f-3b4f7b3581dd'
SCP_PARAMID_DRMVERSION = '41d0155d-7cc7-4217-ada9-005074624da4'
SAC_MAC_LEN = 8
WMDM_LOG_SEV_INFO = 1
WMDM_LOG_SEV_WARN = 2
WMDM_LOG_SEV_ERROR = 4
WMDM_LOG_NOTIMESTAMP = 16
g_wszWMDMFileName = 'WMDM/FileName'
g_wszWMDMFormatCode = 'WMDM/FormatCode'
g_wszWMDMLastModifiedDate = 'WMDM/LastModifiedDate'
g_wszWMDMFileCreationDate = 'WMDM/FileCreationDate'
g_wszWMDMFileSize = 'WMDM/FileSize'
g_wszWMDMFileAttributes = 'WMDM/FileAttributes'
g_wszAudioWAVECodec = 'WMDM/AudioWAVECodec'
g_wszVideoFourCCCodec = 'WMDM/VideoFourCCCodec'
g_wszWMDMTitle = 'WMDM/Title'
g_wszWMDMAuthor = 'WMDM/Author'
g_wszWMDMDescription = 'WMDM/Description'
g_wszWMDMIsProtected = 'WMDM/IsProtected'
g_wszWMDMAlbumTitle = 'WMDM/AlbumTitle'
g_wszWMDMAlbumArtist = 'WMDM/AlbumArtist'
g_wszWMDMTrack = 'WMDM/Track'
g_wszWMDMGenre = 'WMDM/Genre'
g_wszWMDMTrackMood = 'WMDM/TrackMood'
g_wszWMDMAlbumCoverFormat = 'WMDM/AlbumCoverFormat'
g_wszWMDMAlbumCoverSize = 'WMDM/AlbumCoverSize'
g_wszWMDMAlbumCoverHeight = 'WMDM/AlbumCoverHeight'
g_wszWMDMAlbumCoverWidth = 'WMDM/AlbumCoverWidth'
g_wszWMDMAlbumCoverDuration = 'WMDM/AlbumCoverDuration'
g_wszWMDMAlbumCoverData = 'WMDM/AlbumCoverData'
g_wszWMDMYear = 'WMDM/Year'
g_wszWMDMComposer = 'WMDM/Composer'
g_wszWMDMCodec = 'WMDM/Codec'
g_wszWMDMDRMId = 'WMDM/DRMId'
g_wszWMDMBitrate = 'WMDM/Bitrate'
g_wszWMDMBitRateType = 'WMDM/BitRateType'
g_wszWMDMSampleRate = 'WMDM/SampleRate'
g_wszWMDMNumChannels = 'WMDM/NumChannels'
g_wszWMDMBlockAlignment = 'WMDM/BlockAlignment'
g_wszWMDMAudioBitDepth = 'WMDM/AudioBitDepth'
g_wszWMDMTotalBitrate = 'WMDM/TotalBitrate'
g_wszWMDMVideoBitrate = 'WMDM/VideoBitrate'
g_wszWMDMFrameRate = 'WMDM/FrameRate'
g_wszWMDMScanType = 'WMDM/ScanType'
g_wszWMDMKeyFrameDistance = 'WMDM/KeyFrameDistance'
g_wszWMDMBufferSize = 'WMDM/BufferSize'
g_wszWMDMQualitySetting = 'WMDM/QualitySetting'
g_wszWMDMEncodingProfile = 'WMDM/EncodingProfile'
g_wszWMDMDuration = 'WMDM/Duration'
g_wszWMDMAlbumArt = 'WMDM/AlbumArt'
g_wszWMDMBuyNow = 'WMDM/BuyNow'
g_wszWMDMNonConsumable = 'WMDM/NonConsumable'
g_wszWMDMediaClassPrimaryID = 'WMDM/MediaClassPrimaryID'
g_wszWMDMMediaClassSecondaryID = 'WMDM/MediaClassSecondaryID'
g_wszWMDMUserEffectiveRating = 'WMDM/UserEffectiveRating'
g_wszWMDMUserRating = 'WMDM/UserRating'
g_wszWMDMUserRatingOnDevice = 'WMDM/UserRatingOnDevice'
g_wszWMDMPlayCount = 'WMDM/PlayCount'
g_wszWMDMDevicePlayCount = 'WMDM/DevicePlayCount'
g_wszWMDMAuthorDate = 'WMDM/AuthorDate'
g_wszWMDMUserLastPlayTime = 'WMDM/UserLastPlayTime'
g_wszWMDMSubTitle = 'WMDM/SubTitle'
g_wszWMDMSubTitleDescription = 'WMDM/SubTitleDescription'
g_wszWMDMMediaCredits = 'WMDM/MediaCredits'
g_wszWMDMMediaStationName = 'WMDM/MediaStationName'
g_wszWMDMMediaOriginalChannel = 'WMDM/MediaOriginalChannel'
g_wszWMDMMediaOriginalBroadcastDateTime = 'WMDM/MediaOriginalBroadcastDateTime'
g_wszWMDMProviderCopyright = 'WMDM/ProviderCopyright'
g_wszWMDMSyncID = 'WMDM/SyncID'
g_wszWMDMPersistentUniqueID = 'WMDM/PersistentUniqueID'
g_wszWMDMWidth = 'WMDM/Width'
g_wszWMDMHeight = 'WMDM/Height'
g_wszWMDMSyncTime = 'WMDM/SyncTime'
g_wszWMDMParentalRating = 'WMDM/ParentalRating'
g_wszWMDMMetaGenre = 'WMDM/MetaGenre'
g_wszWMDMIsRepeat = 'WMDM/IsRepeat'
g_wszWMDMSupportedDeviceProperties = 'WMDM/SupportedDeviceProperties'
g_wszWMDMDeviceFriendlyName = 'WMDM/DeviceFriendlyName'
g_wszWMDMFormatsSupported = 'WMDM/FormatsSupported'
g_wszWMDMFormatsSupportedAreOrdered = 'WMDM/FormatsSupportedAreOrdered'
g_wszWMDMSyncRelationshipID = 'WMDM/SyncRelationshipID'
g_wszWMDMDeviceModelName = 'WMDM/DeviceModelName'
g_wszWMDMDeviceFirmwareVersion = 'WMDM/DeviceFirmwareVersion'
g_wszWMDMDeviceVendorExtension = 'WMDM/DeviceVendorExtension'
g_wszWMDMDeviceProtocol = 'WMDM/DeviceProtocol'
g_wszWMDMDeviceServiceProviderVendor = 'WMDM/DeviceServiceProviderVendor'
g_wszWMDMDeviceRevocationInfo = 'WMDM/DeviceRevocationInfo'
g_wszWMDMCollectionID = 'WMDM/CollectionID'
g_wszWMDMOwner = 'WMDM/Owner'
g_wszWMDMEditor = 'WMDM/Editor'
g_wszWMDMWebmaster = 'WMDM/Webmaster'
g_wszWMDMSourceURL = 'WMDM/SourceURL'
g_wszWMDMDestinationURL = 'WMDM/DestinationURL'
g_wszWMDMCategory = 'WMDM/Category'
g_wszWMDMTimeBookmark = 'WMDM/TimeBookmark'
g_wszWMDMObjectBookmark = 'WMDM/ObjectBookmark'
g_wszWMDMByteBookmark = 'WMDM/ByteBookmark'
g_wszWMDMDataOffset = 'WMDM/DataOffset'
g_wszWMDMDataLength = 'WMDM/DataLength'
g_wszWMDMDataUnits = 'WMDM/DataUnits'
g_wszWMDMTimeToLive = 'WMDM/TimeToLive'
g_wszWMDMMediaGuid = 'WMDM/MediaGuid'
g_wszWPDPassthroughPropertyValues = 'WPD/PassthroughPropertyValues'
EVENT_WMDM_CONTENT_TRANSFER = '339c9bf4-bcfe-4ed8-94df-eaf8c26ab61b'
MTP_COMMAND_MAX_PARAMS = 5
MTP_RESPONSE_MAX_PARAMS = 5
MTP_RESPONSE_OK = 8193
def _define___MACINFO_head():
    class __MACINFO(Structure):
        pass
    return __MACINFO
def _define___MACINFO():
    __MACINFO = win32more.Media.DeviceManager.__MACINFO_head
    __MACINFO._fields_ = [
        ("fUsed", win32more.Foundation.BOOL),
        ("abMacState", Byte * 36),
    ]
    return __MACINFO
MediaDevMgrClassFactory = Guid('50040c1d-bdbf-4924-b873-f14d6c5bfd66')
MediaDevMgr = Guid('25baad81-3560-11d3-8471-00c04f79dbc0')
WMDMDevice = Guid('807b3cdf-357a-11d3-8471-00c04f79dbc0')
WMDMStorage = Guid('807b3ce0-357a-11d3-8471-00c04f79dbc0')
WMDMStorageGlobal = Guid('807b3ce1-357a-11d3-8471-00c04f79dbc0')
WMDMDeviceEnum = Guid('430e35af-3971-11d3-8474-00c04f79dbc0')
WMDMStorageEnum = Guid('eb401a3b-3af7-11d3-8474-00c04f79dbc0')
WMDM_TAG_DATATYPE = Int32
WMDM_TYPE_DWORD = 0
WMDM_TYPE_STRING = 1
WMDM_TYPE_BINARY = 2
WMDM_TYPE_BOOL = 3
WMDM_TYPE_QWORD = 4
WMDM_TYPE_WORD = 5
WMDM_TYPE_GUID = 6
WMDM_TYPE_DATE = 7
WMDM_SESSION_TYPE = Int32
WMDM_SESSION_NONE = 0
WMDM_SESSION_TRANSFER_TO_DEVICE = 1
WMDM_SESSION_TRANSFER_FROM_DEVICE = 16
WMDM_SESSION_DELETE = 256
WMDM_SESSION_CUSTOM = 4096
def _define__WAVEFORMATEX_head():
    class _WAVEFORMATEX(Structure):
        pass
    return _WAVEFORMATEX
def _define__WAVEFORMATEX():
    _WAVEFORMATEX = win32more.Media.DeviceManager._WAVEFORMATEX_head
    _WAVEFORMATEX._fields_ = [
        ("wFormatTag", UInt16),
        ("nChannels", UInt16),
        ("nSamplesPerSec", UInt32),
        ("nAvgBytesPerSec", UInt32),
        ("nBlockAlign", UInt16),
        ("wBitsPerSample", UInt16),
        ("cbSize", UInt16),
    ]
    return _WAVEFORMATEX
def _define__BITMAPINFOHEADER_head():
    class _BITMAPINFOHEADER(Structure):
        pass
    return _BITMAPINFOHEADER
def _define__BITMAPINFOHEADER():
    _BITMAPINFOHEADER = win32more.Media.DeviceManager._BITMAPINFOHEADER_head
    _BITMAPINFOHEADER._fields_ = [
        ("biSize", UInt32),
        ("biWidth", Int32),
        ("biHeight", Int32),
        ("biPlanes", UInt16),
        ("biBitCount", UInt16),
        ("biCompression", UInt32),
        ("biSizeImage", UInt32),
        ("biXPelsPerMeter", Int32),
        ("biYPelsPerMeter", Int32),
        ("biClrUsed", UInt32),
        ("biClrImportant", UInt32),
    ]
    return _BITMAPINFOHEADER
def _define__VIDEOINFOHEADER_head():
    class _VIDEOINFOHEADER(Structure):
        pass
    return _VIDEOINFOHEADER
def _define__VIDEOINFOHEADER():
    _VIDEOINFOHEADER = win32more.Media.DeviceManager._VIDEOINFOHEADER_head
    _VIDEOINFOHEADER._fields_ = [
        ("rcSource", win32more.Foundation.RECT),
        ("rcTarget", win32more.Foundation.RECT),
        ("dwBitRate", UInt32),
        ("dwBitErrorRate", UInt32),
        ("AvgTimePerFrame", Int64),
        ("bmiHeader", win32more.Media.DeviceManager._BITMAPINFOHEADER),
    ]
    return _VIDEOINFOHEADER
def _define_WMFILECAPABILITIES_head():
    class WMFILECAPABILITIES(Structure):
        pass
    return WMFILECAPABILITIES
def _define_WMFILECAPABILITIES():
    WMFILECAPABILITIES = win32more.Media.DeviceManager.WMFILECAPABILITIES_head
    WMFILECAPABILITIES._fields_ = [
        ("pwszMimeType", win32more.Foundation.PWSTR),
        ("dwReserved", UInt32),
    ]
    return WMFILECAPABILITIES
def _define_OPAQUECOMMAND_head():
    class OPAQUECOMMAND(Structure):
        pass
    return OPAQUECOMMAND
def _define_OPAQUECOMMAND():
    OPAQUECOMMAND = win32more.Media.DeviceManager.OPAQUECOMMAND_head
    OPAQUECOMMAND._fields_ = [
        ("guidCommand", Guid),
        ("dwDataLen", UInt32),
        ("pData", c_char_p_no),
        ("abMAC", Byte * 20),
    ]
    return OPAQUECOMMAND
def _define_WMDMID_head():
    class WMDMID(Structure):
        pass
    return WMDMID
def _define_WMDMID():
    WMDMID = win32more.Media.DeviceManager.WMDMID_head
    WMDMID._fields_ = [
        ("cbSize", UInt32),
        ("dwVendorID", UInt32),
        ("pID", Byte * 128),
        ("SerialNumberLength", UInt32),
    ]
    return WMDMID
def _define_WMDMDATETIME_head():
    class WMDMDATETIME(Structure):
        pass
    return WMDMDATETIME
def _define_WMDMDATETIME():
    WMDMDATETIME = win32more.Media.DeviceManager.WMDMDATETIME_head
    WMDMDATETIME._fields_ = [
        ("wYear", UInt16),
        ("wMonth", UInt16),
        ("wDay", UInt16),
        ("wHour", UInt16),
        ("wMinute", UInt16),
        ("wSecond", UInt16),
    ]
    return WMDMDATETIME
def _define_WMDMRIGHTS_head():
    class WMDMRIGHTS(Structure):
        pass
    return WMDMRIGHTS
def _define_WMDMRIGHTS():
    WMDMRIGHTS = win32more.Media.DeviceManager.WMDMRIGHTS_head
    WMDMRIGHTS._fields_ = [
        ("cbSize", UInt32),
        ("dwContentType", UInt32),
        ("fuFlags", UInt32),
        ("fuRights", UInt32),
        ("dwAppSec", UInt32),
        ("dwPlaybackCount", UInt32),
        ("ExpirationDate", win32more.Media.DeviceManager.WMDMDATETIME),
    ]
    return WMDMRIGHTS
def _define_WMDMMetadataView_head():
    class WMDMMetadataView(Structure):
        pass
    return WMDMMetadataView
def _define_WMDMMetadataView():
    WMDMMetadataView = win32more.Media.DeviceManager.WMDMMetadataView_head
    WMDMMetadataView._fields_ = [
        ("pwszViewName", win32more.Foundation.PWSTR),
        ("nDepth", UInt32),
        ("ppwszTags", POINTER(POINTER(UInt16))),
    ]
    return WMDMMetadataView
WMDM_STORAGE_ENUM_MODE = Int32
ENUM_MODE_RAW = 0
ENUM_MODE_USE_DEVICE_PREF = 1
ENUM_MODE_METADATA_VIEWS = 2
WMDM_FORMATCODE = Int32
WMDM_FORMATCODE_NOTUSED = 0
WMDM_FORMATCODE_ALLIMAGES = -1
WMDM_FORMATCODE_UNDEFINED = 12288
WMDM_FORMATCODE_ASSOCIATION = 12289
WMDM_FORMATCODE_SCRIPT = 12290
WMDM_FORMATCODE_EXECUTABLE = 12291
WMDM_FORMATCODE_TEXT = 12292
WMDM_FORMATCODE_HTML = 12293
WMDM_FORMATCODE_DPOF = 12294
WMDM_FORMATCODE_AIFF = 12295
WMDM_FORMATCODE_WAVE = 12296
WMDM_FORMATCODE_MP3 = 12297
WMDM_FORMATCODE_AVI = 12298
WMDM_FORMATCODE_MPEG = 12299
WMDM_FORMATCODE_ASF = 12300
WMDM_FORMATCODE_RESERVED_FIRST = 12301
WMDM_FORMATCODE_RESERVED_LAST = 14335
WMDM_FORMATCODE_IMAGE_UNDEFINED = 14336
WMDM_FORMATCODE_IMAGE_EXIF = 14337
WMDM_FORMATCODE_IMAGE_TIFFEP = 14338
WMDM_FORMATCODE_IMAGE_FLASHPIX = 14339
WMDM_FORMATCODE_IMAGE_BMP = 14340
WMDM_FORMATCODE_IMAGE_CIFF = 14341
WMDM_FORMATCODE_IMAGE_GIF = 14343
WMDM_FORMATCODE_IMAGE_JFIF = 14344
WMDM_FORMATCODE_IMAGE_PCD = 14345
WMDM_FORMATCODE_IMAGE_PICT = 14346
WMDM_FORMATCODE_IMAGE_PNG = 14347
WMDM_FORMATCODE_IMAGE_TIFF = 14349
WMDM_FORMATCODE_IMAGE_TIFFIT = 14350
WMDM_FORMATCODE_IMAGE_JP2 = 14351
WMDM_FORMATCODE_IMAGE_JPX = 14352
WMDM_FORMATCODE_IMAGE_RESERVED_FIRST = 14353
WMDM_FORMATCODE_IMAGE_RESERVED_LAST = 16383
WMDM_FORMATCODE_UNDEFINEDFIRMWARE = 47106
WMDM_FORMATCODE_WBMP = 47107
WMDM_FORMATCODE_JPEGXR = 47108
WMDM_FORMATCODE_WINDOWSIMAGEFORMAT = 47233
WMDM_FORMATCODE_UNDEFINEDAUDIO = 47360
WMDM_FORMATCODE_WMA = 47361
WMDM_FORMATCODE_OGG = 47362
WMDM_FORMATCODE_AAC = 47363
WMDM_FORMATCODE_AUDIBLE = 47364
WMDM_FORMATCODE_FLAC = 47366
WMDM_FORMATCODE_QCELP = 47367
WMDM_FORMATCODE_AMR = 47368
WMDM_FORMATCODE_UNDEFINEDVIDEO = 47488
WMDM_FORMATCODE_WMV = 47489
WMDM_FORMATCODE_MP4 = 47490
WMDM_FORMATCODE_MP2 = 47491
WMDM_FORMATCODE_3GP = 47492
WMDM_FORMATCODE_3G2 = 47493
WMDM_FORMATCODE_AVCHD = 47494
WMDM_FORMATCODE_ATSCTS = 47495
WMDM_FORMATCODE_DVBTS = 47496
WMDM_FORMATCODE_MKV = 47497
WMDM_FORMATCODE_MKA = 47498
WMDM_FORMATCODE_MK3D = 47499
WMDM_FORMATCODE_UNDEFINEDCOLLECTION = 47616
WMDM_FORMATCODE_ABSTRACTMULTIMEDIAALBUM = 47617
WMDM_FORMATCODE_ABSTRACTIMAGEALBUM = 47618
WMDM_FORMATCODE_ABSTRACTAUDIOALBUM = 47619
WMDM_FORMATCODE_ABSTRACTVIDEOALBUM = 47620
WMDM_FORMATCODE_ABSTRACTAUDIOVIDEOPLAYLIST = 47621
WMDM_FORMATCODE_ABSTRACTCONTACTGROUP = 47622
WMDM_FORMATCODE_ABSTRACTMESSAGEFOLDER = 47623
WMDM_FORMATCODE_ABSTRACTCHAPTEREDPRODUCTION = 47624
WMDM_FORMATCODE_MEDIA_CAST = 47627
WMDM_FORMATCODE_WPLPLAYLIST = 47632
WMDM_FORMATCODE_M3UPLAYLIST = 47633
WMDM_FORMATCODE_MPLPLAYLIST = 47634
WMDM_FORMATCODE_ASXPLAYLIST = 47635
WMDM_FORMATCODE_PLSPLAYLIST = 47636
WMDM_FORMATCODE_UNDEFINEDDOCUMENT = 47744
WMDM_FORMATCODE_ABSTRACTDOCUMENT = 47745
WMDM_FORMATCODE_XMLDOCUMENT = 47746
WMDM_FORMATCODE_MICROSOFTWORDDOCUMENT = 47747
WMDM_FORMATCODE_MHTCOMPILEDHTMLDOCUMENT = 47748
WMDM_FORMATCODE_MICROSOFTEXCELSPREADSHEET = 47749
WMDM_FORMATCODE_MICROSOFTPOWERPOINTDOCUMENT = 47750
WMDM_FORMATCODE_UNDEFINEDMESSAGE = 47872
WMDM_FORMATCODE_ABSTRACTMESSAGE = 47873
WMDM_FORMATCODE_UNDEFINEDCONTACT = 48000
WMDM_FORMATCODE_ABSTRACTCONTACT = 48001
WMDM_FORMATCODE_VCARD2 = 48002
WMDM_FORMATCODE_VCARD3 = 48003
WMDM_FORMATCODE_UNDEFINEDCALENDARITEM = 48640
WMDM_FORMATCODE_ABSTRACTCALENDARITEM = 48641
WMDM_FORMATCODE_VCALENDAR1 = 48642
WMDM_FORMATCODE_VCALENDAR2 = 48643
WMDM_FORMATCODE_UNDEFINEDWINDOWSEXECUTABLE = 48768
WMDM_FORMATCODE_M4A = 1297101889
WMDM_FORMATCODE_3GPA = 860311617
WMDM_FORMATCODE_3G2A = 860303937
WMDM_FORMATCODE_SECTION = 48770
WMDM_ENUM_PROP_VALID_VALUES_FORM = Int32
WMDM_ENUM_PROP_VALID_VALUES_ANY = 0
WMDM_ENUM_PROP_VALID_VALUES_RANGE = 1
WMDM_ENUM_PROP_VALID_VALUES_ENUM = 2
def _define_WMDM_PROP_VALUES_RANGE_head():
    class WMDM_PROP_VALUES_RANGE(Structure):
        pass
    return WMDM_PROP_VALUES_RANGE
def _define_WMDM_PROP_VALUES_RANGE():
    WMDM_PROP_VALUES_RANGE = win32more.Media.DeviceManager.WMDM_PROP_VALUES_RANGE_head
    WMDM_PROP_VALUES_RANGE._fields_ = [
        ("rangeMin", win32more.System.Com.StructuredStorage.PROPVARIANT),
        ("rangeMax", win32more.System.Com.StructuredStorage.PROPVARIANT),
        ("rangeStep", win32more.System.Com.StructuredStorage.PROPVARIANT),
    ]
    return WMDM_PROP_VALUES_RANGE
def _define_WMDM_PROP_VALUES_ENUM_head():
    class WMDM_PROP_VALUES_ENUM(Structure):
        pass
    return WMDM_PROP_VALUES_ENUM
def _define_WMDM_PROP_VALUES_ENUM():
    WMDM_PROP_VALUES_ENUM = win32more.Media.DeviceManager.WMDM_PROP_VALUES_ENUM_head
    WMDM_PROP_VALUES_ENUM._fields_ = [
        ("cEnumValues", UInt32),
        ("pValues", POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)),
    ]
    return WMDM_PROP_VALUES_ENUM
def _define_WMDM_PROP_DESC_head():
    class WMDM_PROP_DESC(Structure):
        pass
    return WMDM_PROP_DESC
def _define_WMDM_PROP_DESC():
    WMDM_PROP_DESC = win32more.Media.DeviceManager.WMDM_PROP_DESC_head
    class WMDM_PROP_DESC__ValidValues_e__Union(Union):
        pass
    WMDM_PROP_DESC__ValidValues_e__Union._fields_ = [
        ("ValidValuesRange", win32more.Media.DeviceManager.WMDM_PROP_VALUES_RANGE),
        ("EnumeratedValidValues", win32more.Media.DeviceManager.WMDM_PROP_VALUES_ENUM),
    ]
    WMDM_PROP_DESC._fields_ = [
        ("pwszPropName", win32more.Foundation.PWSTR),
        ("ValidValuesForm", win32more.Media.DeviceManager.WMDM_ENUM_PROP_VALID_VALUES_FORM),
        ("ValidValues", WMDM_PROP_DESC__ValidValues_e__Union),
    ]
    return WMDM_PROP_DESC
def _define_WMDM_PROP_CONFIG_head():
    class WMDM_PROP_CONFIG(Structure):
        pass
    return WMDM_PROP_CONFIG
def _define_WMDM_PROP_CONFIG():
    WMDM_PROP_CONFIG = win32more.Media.DeviceManager.WMDM_PROP_CONFIG_head
    WMDM_PROP_CONFIG._fields_ = [
        ("nPreference", UInt32),
        ("nPropDesc", UInt32),
        ("pPropDesc", POINTER(win32more.Media.DeviceManager.WMDM_PROP_DESC_head)),
    ]
    return WMDM_PROP_CONFIG
def _define_WMDM_FORMAT_CAPABILITY_head():
    class WMDM_FORMAT_CAPABILITY(Structure):
        pass
    return WMDM_FORMAT_CAPABILITY
def _define_WMDM_FORMAT_CAPABILITY():
    WMDM_FORMAT_CAPABILITY = win32more.Media.DeviceManager.WMDM_FORMAT_CAPABILITY_head
    WMDM_FORMAT_CAPABILITY._fields_ = [
        ("nPropConfig", UInt32),
        ("pConfigs", POINTER(win32more.Media.DeviceManager.WMDM_PROP_CONFIG_head)),
    ]
    return WMDM_FORMAT_CAPABILITY
WMDM_FIND_SCOPE = Int32
WMDM_FIND_SCOPE_GLOBAL = 0
WMDM_FIND_SCOPE_IMMEDIATE_CHILDREN = 1
WMDMMessage = Int32
WMDM_MSG_DEVICE_ARRIVAL = 0
WMDM_MSG_DEVICE_REMOVAL = 1
WMDM_MSG_MEDIA_ARRIVAL = 2
WMDM_MSG_MEDIA_REMOVAL = 3
def _define_IWMDMMetaData_head():
    class IWMDMMetaData(win32more.System.Com.IUnknown_head):
        Guid = Guid('ec3b0663-0951-460a-9a80-0dceed3c043c')
    return IWMDMMetaData
def _define_IWMDMMetaData():
    IWMDMMetaData = win32more.Media.DeviceManager.IWMDMMetaData_head
    IWMDMMetaData.AddItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.DeviceManager.WMDM_TAG_DATATYPE,win32more.Foundation.PWSTR,POINTER(Byte),UInt32, use_last_error=False)(3, 'AddItem', ((1, 'Type'),(1, 'pwszTagName'),(1, 'pValue'),(1, 'iLength'),)))
    IWMDMMetaData.QueryByName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Media.DeviceManager.WMDM_TAG_DATATYPE),POINTER(c_char_p_no),POINTER(UInt32), use_last_error=False)(4, 'QueryByName', ((1, 'pwszTagName'),(1, 'pType'),(1, 'pValue'),(1, 'pcbLength'),)))
    IWMDMMetaData.QueryByIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(POINTER(UInt16)),POINTER(win32more.Media.DeviceManager.WMDM_TAG_DATATYPE),POINTER(c_char_p_no),POINTER(UInt32), use_last_error=False)(5, 'QueryByIndex', ((1, 'iIndex'),(1, 'ppwszName'),(1, 'pType'),(1, 'ppValue'),(1, 'pcbLength'),)))
    IWMDMMetaData.GetItemCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(6, 'GetItemCount', ((1, 'iCount'),)))
    win32more.System.Com.IUnknown
    return IWMDMMetaData
def _define_IWMDeviceManager_head():
    class IWMDeviceManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('1dcb3a00-33ed-11d3-8470-00c04f79dbc0')
    return IWMDeviceManager
def _define_IWMDeviceManager():
    IWMDeviceManager = win32more.Media.DeviceManager.IWMDeviceManager_head
    IWMDeviceManager.GetRevision = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetRevision', ((1, 'pdwRevision'),)))
    IWMDeviceManager.GetDeviceCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(4, 'GetDeviceCount', ((1, 'pdwCount'),)))
    IWMDeviceManager.EnumDevices = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.DeviceManager.IWMDMEnumDevice_head), use_last_error=False)(5, 'EnumDevices', ((1, 'ppEnumDevice'),)))
    win32more.System.Com.IUnknown
    return IWMDeviceManager
def _define_IWMDeviceManager2_head():
    class IWMDeviceManager2(win32more.Media.DeviceManager.IWMDeviceManager_head):
        Guid = Guid('923e5249-8731-4c5b-9b1c-b8b60b6e46af')
    return IWMDeviceManager2
def _define_IWMDeviceManager2():
    IWMDeviceManager2 = win32more.Media.DeviceManager.IWMDeviceManager2_head
    IWMDeviceManager2.GetDeviceFromCanonicalName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Media.DeviceManager.IWMDMDevice_head), use_last_error=False)(6, 'GetDeviceFromCanonicalName', ((1, 'pwszCanonicalName'),(1, 'ppDevice'),)))
    IWMDeviceManager2.EnumDevices2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.DeviceManager.IWMDMEnumDevice_head), use_last_error=False)(7, 'EnumDevices2', ((1, 'ppEnumDevice'),)))
    IWMDeviceManager2.Reinitialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'Reinitialize', ()))
    win32more.Media.DeviceManager.IWMDeviceManager
    return IWMDeviceManager2
def _define_IWMDeviceManager3_head():
    class IWMDeviceManager3(win32more.Media.DeviceManager.IWMDeviceManager2_head):
        Guid = Guid('af185c41-100d-46ed-be2e-9ce8c44594ef')
    return IWMDeviceManager3
def _define_IWMDeviceManager3():
    IWMDeviceManager3 = win32more.Media.DeviceManager.IWMDeviceManager3_head
    IWMDeviceManager3.SetDeviceEnumPreference = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(9, 'SetDeviceEnumPreference', ((1, 'dwEnumPref'),)))
    win32more.Media.DeviceManager.IWMDeviceManager2
    return IWMDeviceManager3
def _define_IWMDMStorageGlobals_head():
    class IWMDMStorageGlobals(win32more.System.Com.IUnknown_head):
        Guid = Guid('1dcb3a07-33ed-11d3-8470-00c04f79dbc0')
    return IWMDMStorageGlobals
def _define_IWMDMStorageGlobals():
    IWMDMStorageGlobals = win32more.Media.DeviceManager.IWMDMStorageGlobals_head
    IWMDMStorageGlobals.GetCapabilities = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetCapabilities', ((1, 'pdwCapabilities'),)))
    IWMDMStorageGlobals.GetSerialNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.DeviceManager.WMDMID_head),c_char_p_no, use_last_error=False)(4, 'GetSerialNumber', ((1, 'pSerialNum'),(1, 'abMac'),)))
    IWMDMStorageGlobals.GetTotalSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(5, 'GetTotalSize', ((1, 'pdwTotalSizeLow'),(1, 'pdwTotalSizeHigh'),)))
    IWMDMStorageGlobals.GetTotalFree = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(6, 'GetTotalFree', ((1, 'pdwFreeLow'),(1, 'pdwFreeHigh'),)))
    IWMDMStorageGlobals.GetTotalBad = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(7, 'GetTotalBad', ((1, 'pdwBadLow'),(1, 'pdwBadHigh'),)))
    IWMDMStorageGlobals.GetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(8, 'GetStatus', ((1, 'pdwStatus'),)))
    IWMDMStorageGlobals.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Media.DeviceManager.IWMDMProgress_head, use_last_error=False)(9, 'Initialize', ((1, 'fuMode'),(1, 'pProgress'),)))
    win32more.System.Com.IUnknown
    return IWMDMStorageGlobals
def _define_IWMDMStorage_head():
    class IWMDMStorage(win32more.System.Com.IUnknown_head):
        Guid = Guid('1dcb3a06-33ed-11d3-8470-00c04f79dbc0')
    return IWMDMStorage
def _define_IWMDMStorage():
    IWMDMStorage = win32more.Media.DeviceManager.IWMDMStorage_head
    IWMDMStorage.SetAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.DeviceManager._WAVEFORMATEX_head), use_last_error=False)(3, 'SetAttributes', ((1, 'dwAttributes'),(1, 'pFormat'),)))
    IWMDMStorage.GetStorageGlobals = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.DeviceManager.IWMDMStorageGlobals_head), use_last_error=False)(4, 'GetStorageGlobals', ((1, 'ppStorageGlobals'),)))
    IWMDMStorage.GetAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(win32more.Media.DeviceManager._WAVEFORMATEX_head), use_last_error=False)(5, 'GetAttributes', ((1, 'pdwAttributes'),(1, 'pFormat'),)))
    IWMDMStorage.GetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),UInt32, use_last_error=False)(6, 'GetName', ((1, 'pwszName'),(1, 'nMaxChars'),)))
    IWMDMStorage.GetDate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.DeviceManager.WMDMDATETIME_head), use_last_error=False)(7, 'GetDate', ((1, 'pDateTimeUTC'),)))
    IWMDMStorage.GetSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(8, 'GetSize', ((1, 'pdwSizeLow'),(1, 'pdwSizeHigh'),)))
    IWMDMStorage.GetRights = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Media.DeviceManager.WMDMRIGHTS_head)),POINTER(UInt32),c_char_p_no, use_last_error=False)(9, 'GetRights', ((1, 'ppRights'),(1, 'pnRightsCount'),(1, 'abMac'),)))
    IWMDMStorage.EnumStorage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.DeviceManager.IWMDMEnumStorage_head), use_last_error=False)(10, 'EnumStorage', ((1, 'pEnumStorage'),)))
    IWMDMStorage.SendOpaqueCommand = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.DeviceManager.OPAQUECOMMAND_head), use_last_error=False)(11, 'SendOpaqueCommand', ((1, 'pCommand'),)))
    win32more.System.Com.IUnknown
    return IWMDMStorage
def _define_IWMDMStorage2_head():
    class IWMDMStorage2(win32more.Media.DeviceManager.IWMDMStorage_head):
        Guid = Guid('1ed5a144-5cd5-4683-9eff-72cbdb2d9533')
    return IWMDMStorage2
def _define_IWMDMStorage2():
    IWMDMStorage2 = win32more.Media.DeviceManager.IWMDMStorage2_head
    IWMDMStorage2.GetStorage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Media.DeviceManager.IWMDMStorage_head), use_last_error=False)(12, 'GetStorage', ((1, 'pszStorageName'),(1, 'ppStorage'),)))
    IWMDMStorage2.SetAttributes2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.Media.DeviceManager._WAVEFORMATEX_head),POINTER(win32more.Media.DeviceManager._VIDEOINFOHEADER_head), use_last_error=False)(13, 'SetAttributes2', ((1, 'dwAttributes'),(1, 'dwAttributesEx'),(1, 'pFormat'),(1, 'pVideoFormat'),)))
    IWMDMStorage2.GetAttributes2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32),POINTER(win32more.Media.DeviceManager._WAVEFORMATEX_head),POINTER(win32more.Media.DeviceManager._VIDEOINFOHEADER_head), use_last_error=False)(14, 'GetAttributes2', ((1, 'pdwAttributes'),(1, 'pdwAttributesEx'),(1, 'pAudioFormat'),(1, 'pVideoFormat'),)))
    win32more.Media.DeviceManager.IWMDMStorage
    return IWMDMStorage2
def _define_IWMDMStorage3_head():
    class IWMDMStorage3(win32more.Media.DeviceManager.IWMDMStorage2_head):
        Guid = Guid('97717eea-926a-464e-96a4-247b0216026e')
    return IWMDMStorage3
def _define_IWMDMStorage3():
    IWMDMStorage3 = win32more.Media.DeviceManager.IWMDMStorage3_head
    IWMDMStorage3.GetMetadata = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.DeviceManager.IWMDMMetaData_head), use_last_error=False)(15, 'GetMetadata', ((1, 'ppMetadata'),)))
    IWMDMStorage3.SetMetadata = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.DeviceManager.IWMDMMetaData_head, use_last_error=False)(16, 'SetMetadata', ((1, 'pMetadata'),)))
    IWMDMStorage3.CreateEmptyMetadataObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.DeviceManager.IWMDMMetaData_head), use_last_error=False)(17, 'CreateEmptyMetadataObject', ((1, 'ppMetadata'),)))
    IWMDMStorage3.SetEnumPreference = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.DeviceManager.WMDM_STORAGE_ENUM_MODE),UInt32,POINTER(win32more.Media.DeviceManager.WMDMMetadataView), use_last_error=False)(18, 'SetEnumPreference', ((1, 'pMode'),(1, 'nViews'),(1, 'pViews'),)))
    win32more.Media.DeviceManager.IWMDMStorage2
    return IWMDMStorage3
def _define_IWMDMStorage4_head():
    class IWMDMStorage4(win32more.Media.DeviceManager.IWMDMStorage3_head):
        Guid = Guid('c225bac5-a03a-40b8-9a23-91cf478c64a6')
    return IWMDMStorage4
def _define_IWMDMStorage4():
    IWMDMStorage4 = win32more.Media.DeviceManager.IWMDMStorage4_head
    IWMDMStorage4.SetReferences = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.DeviceManager.IWMDMStorage_head), use_last_error=False)(19, 'SetReferences', ((1, 'dwRefs'),(1, 'ppIWMDMStorage'),)))
    IWMDMStorage4.GetReferences = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(POINTER(win32more.Media.DeviceManager.IWMDMStorage_head)), use_last_error=False)(20, 'GetReferences', ((1, 'pdwRefs'),(1, 'pppIWMDMStorage'),)))
    IWMDMStorage4.GetRightsWithProgress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.DeviceManager.IWMDMProgress3_head,POINTER(POINTER(win32more.Media.DeviceManager.WMDMRIGHTS_head)),POINTER(UInt32), use_last_error=False)(21, 'GetRightsWithProgress', ((1, 'pIProgressCallback'),(1, 'ppRights'),(1, 'pnRightsCount'),)))
    IWMDMStorage4.GetSpecifiedMetadata = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Media.DeviceManager.IWMDMMetaData_head), use_last_error=False)(22, 'GetSpecifiedMetadata', ((1, 'cProperties'),(1, 'ppwszPropNames'),(1, 'ppMetadata'),)))
    IWMDMStorage4.FindStorage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.DeviceManager.WMDM_FIND_SCOPE,win32more.Foundation.PWSTR,POINTER(win32more.Media.DeviceManager.IWMDMStorage_head), use_last_error=False)(23, 'FindStorage', ((1, 'findScope'),(1, 'pwszUniqueID'),(1, 'ppStorage'),)))
    IWMDMStorage4.GetParent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.DeviceManager.IWMDMStorage_head), use_last_error=False)(24, 'GetParent', ((1, 'ppStorage'),)))
    win32more.Media.DeviceManager.IWMDMStorage3
    return IWMDMStorage4
def _define_IWMDMOperation_head():
    class IWMDMOperation(win32more.System.Com.IUnknown_head):
        Guid = Guid('1dcb3a0b-33ed-11d3-8470-00c04f79dbc0')
    return IWMDMOperation
def _define_IWMDMOperation():
    IWMDMOperation = win32more.Media.DeviceManager.IWMDMOperation_head
    IWMDMOperation.BeginRead = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'BeginRead', ()))
    IWMDMOperation.BeginWrite = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'BeginWrite', ()))
    IWMDMOperation.GetObjectName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),UInt32, use_last_error=False)(5, 'GetObjectName', ((1, 'pwszName'),(1, 'nMaxChars'),)))
    IWMDMOperation.SetObjectName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),UInt32, use_last_error=False)(6, 'SetObjectName', ((1, 'pwszName'),(1, 'nMaxChars'),)))
    IWMDMOperation.GetObjectAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(win32more.Media.DeviceManager._WAVEFORMATEX_head), use_last_error=False)(7, 'GetObjectAttributes', ((1, 'pdwAttributes'),(1, 'pFormat'),)))
    IWMDMOperation.SetObjectAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.DeviceManager._WAVEFORMATEX_head), use_last_error=False)(8, 'SetObjectAttributes', ((1, 'dwAttributes'),(1, 'pFormat'),)))
    IWMDMOperation.GetObjectTotalSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(9, 'GetObjectTotalSize', ((1, 'pdwSize'),(1, 'pdwSizeHigh'),)))
    IWMDMOperation.SetObjectTotalSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(10, 'SetObjectTotalSize', ((1, 'dwSize'),(1, 'dwSizeHigh'),)))
    IWMDMOperation.TransferObjectData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),POINTER(UInt32),c_char_p_no, use_last_error=False)(11, 'TransferObjectData', ((1, 'pData'),(1, 'pdwSize'),(1, 'abMac'),)))
    IWMDMOperation.End = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HRESULT),win32more.System.Com.IUnknown_head, use_last_error=False)(12, 'End', ((1, 'phCompletionCode'),(1, 'pNewObject'),)))
    win32more.System.Com.IUnknown
    return IWMDMOperation
def _define_IWMDMOperation2_head():
    class IWMDMOperation2(win32more.Media.DeviceManager.IWMDMOperation_head):
        Guid = Guid('33445b48-7df7-425c-ad8f-0fc6d82f9f75')
    return IWMDMOperation2
def _define_IWMDMOperation2():
    IWMDMOperation2 = win32more.Media.DeviceManager.IWMDMOperation2_head
    IWMDMOperation2.SetObjectAttributes2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.Media.DeviceManager._WAVEFORMATEX_head),POINTER(win32more.Media.DeviceManager._VIDEOINFOHEADER_head), use_last_error=False)(13, 'SetObjectAttributes2', ((1, 'dwAttributes'),(1, 'dwAttributesEx'),(1, 'pFormat'),(1, 'pVideoFormat'),)))
    IWMDMOperation2.GetObjectAttributes2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32),POINTER(win32more.Media.DeviceManager._WAVEFORMATEX_head),POINTER(win32more.Media.DeviceManager._VIDEOINFOHEADER_head), use_last_error=False)(14, 'GetObjectAttributes2', ((1, 'pdwAttributes'),(1, 'pdwAttributesEx'),(1, 'pAudioFormat'),(1, 'pVideoFormat'),)))
    win32more.Media.DeviceManager.IWMDMOperation
    return IWMDMOperation2
def _define_IWMDMOperation3_head():
    class IWMDMOperation3(win32more.Media.DeviceManager.IWMDMOperation_head):
        Guid = Guid('d1f9b46a-9ca8-46d8-9d0f-1ec9bae54919')
    return IWMDMOperation3
def _define_IWMDMOperation3():
    IWMDMOperation3 = win32more.Media.DeviceManager.IWMDMOperation3_head
    IWMDMOperation3.TransferObjectDataOnClearChannel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),POINTER(UInt32), use_last_error=False)(13, 'TransferObjectDataOnClearChannel', ((1, 'pData'),(1, 'pdwSize'),)))
    win32more.Media.DeviceManager.IWMDMOperation
    return IWMDMOperation3
def _define_IWMDMProgress_head():
    class IWMDMProgress(win32more.System.Com.IUnknown_head):
        Guid = Guid('1dcb3a0c-33ed-11d3-8470-00c04f79dbc0')
    return IWMDMProgress
def _define_IWMDMProgress():
    IWMDMProgress = win32more.Media.DeviceManager.IWMDMProgress_head
    IWMDMProgress.Begin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(3, 'Begin', ((1, 'dwEstimatedTicks'),)))
    IWMDMProgress.Progress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'Progress', ((1, 'dwTranspiredTicks'),)))
    IWMDMProgress.End = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'End', ()))
    win32more.System.Com.IUnknown
    return IWMDMProgress
def _define_IWMDMProgress2_head():
    class IWMDMProgress2(win32more.Media.DeviceManager.IWMDMProgress_head):
        Guid = Guid('3a43f550-b383-4e92-b04a-e6bbc660fefc')
    return IWMDMProgress2
def _define_IWMDMProgress2():
    IWMDMProgress2 = win32more.Media.DeviceManager.IWMDMProgress2_head
    IWMDMProgress2.End2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT, use_last_error=False)(6, 'End2', ((1, 'hrCompletionCode'),)))
    win32more.Media.DeviceManager.IWMDMProgress
    return IWMDMProgress2
def _define_IWMDMProgress3_head():
    class IWMDMProgress3(win32more.Media.DeviceManager.IWMDMProgress2_head):
        Guid = Guid('21de01cb-3bb4-4929-b21a-17af3f80f658')
    return IWMDMProgress3
def _define_IWMDMProgress3():
    IWMDMProgress3 = win32more.Media.DeviceManager.IWMDMProgress3_head
    IWMDMProgress3.Begin3 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,UInt32,POINTER(win32more.Media.DeviceManager.OPAQUECOMMAND_head), use_last_error=False)(7, 'Begin3', ((1, 'EventId'),(1, 'dwEstimatedTicks'),(1, 'pContext'),)))
    IWMDMProgress3.Progress3 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,UInt32,POINTER(win32more.Media.DeviceManager.OPAQUECOMMAND_head), use_last_error=False)(8, 'Progress3', ((1, 'EventId'),(1, 'dwTranspiredTicks'),(1, 'pContext'),)))
    IWMDMProgress3.End3 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,win32more.Foundation.HRESULT,POINTER(win32more.Media.DeviceManager.OPAQUECOMMAND_head), use_last_error=False)(9, 'End3', ((1, 'EventId'),(1, 'hrCompletionCode'),(1, 'pContext'),)))
    win32more.Media.DeviceManager.IWMDMProgress2
    return IWMDMProgress3
def _define_IWMDMDevice_head():
    class IWMDMDevice(win32more.System.Com.IUnknown_head):
        Guid = Guid('1dcb3a02-33ed-11d3-8470-00c04f79dbc0')
    return IWMDMDevice
def _define_IWMDMDevice():
    IWMDMDevice = win32more.Media.DeviceManager.IWMDMDevice_head
    IWMDMDevice.GetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),UInt32, use_last_error=False)(3, 'GetName', ((1, 'pwszName'),(1, 'nMaxChars'),)))
    IWMDMDevice.GetManufacturer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),UInt32, use_last_error=False)(4, 'GetManufacturer', ((1, 'pwszName'),(1, 'nMaxChars'),)))
    IWMDMDevice.GetVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(5, 'GetVersion', ((1, 'pdwVersion'),)))
    IWMDMDevice.GetType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(6, 'GetType', ((1, 'pdwType'),)))
    IWMDMDevice.GetSerialNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.DeviceManager.WMDMID_head),c_char_p_no, use_last_error=False)(7, 'GetSerialNumber', ((1, 'pSerialNumber'),(1, 'abMac'),)))
    IWMDMDevice.GetPowerSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(8, 'GetPowerSource', ((1, 'pdwPowerSource'),(1, 'pdwPercentRemaining'),)))
    IWMDMDevice.GetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(9, 'GetStatus', ((1, 'pdwStatus'),)))
    IWMDMDevice.GetDeviceIcon = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(10, 'GetDeviceIcon', ((1, 'hIcon'),)))
    IWMDMDevice.EnumStorage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.DeviceManager.IWMDMEnumStorage_head), use_last_error=False)(11, 'EnumStorage', ((1, 'ppEnumStorage'),)))
    IWMDMDevice.GetFormatSupport = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Media.DeviceManager._WAVEFORMATEX_head)),POINTER(UInt32),POINTER(POINTER(win32more.Foundation.PWSTR)),POINTER(UInt32), use_last_error=False)(12, 'GetFormatSupport', ((1, 'ppFormatEx'),(1, 'pnFormatCount'),(1, 'pppwszMimeType'),(1, 'pnMimeTypeCount'),)))
    IWMDMDevice.SendOpaqueCommand = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.DeviceManager.OPAQUECOMMAND_head), use_last_error=False)(13, 'SendOpaqueCommand', ((1, 'pCommand'),)))
    win32more.System.Com.IUnknown
    return IWMDMDevice
def _define_IWMDMDevice2_head():
    class IWMDMDevice2(win32more.Media.DeviceManager.IWMDMDevice_head):
        Guid = Guid('e34f3d37-9d67-4fc1-9252-62d28b2f8b55')
    return IWMDMDevice2
def _define_IWMDMDevice2():
    IWMDMDevice2 = win32more.Media.DeviceManager.IWMDMDevice2_head
    IWMDMDevice2.GetStorage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Media.DeviceManager.IWMDMStorage_head), use_last_error=False)(14, 'GetStorage', ((1, 'pszStorageName'),(1, 'ppStorage'),)))
    IWMDMDevice2.GetFormatSupport2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(POINTER(win32more.Media.DeviceManager._WAVEFORMATEX_head)),POINTER(UInt32),POINTER(POINTER(win32more.Media.DeviceManager._VIDEOINFOHEADER_head)),POINTER(UInt32),POINTER(POINTER(win32more.Media.DeviceManager.WMFILECAPABILITIES_head)),POINTER(UInt32), use_last_error=False)(15, 'GetFormatSupport2', ((1, 'dwFlags'),(1, 'ppAudioFormatEx'),(1, 'pnAudioFormatCount'),(1, 'ppVideoFormatEx'),(1, 'pnVideoFormatCount'),(1, 'ppFileType'),(1, 'pnFileTypeCount'),)))
    IWMDMDevice2.GetSpecifyPropertyPages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.ISpecifyPropertyPages_head),POINTER(POINTER(win32more.System.Com.IUnknown_head)),POINTER(UInt32), use_last_error=False)(16, 'GetSpecifyPropertyPages', ((1, 'ppSpecifyPropPages'),(1, 'pppUnknowns'),(1, 'pcUnks'),)))
    IWMDMDevice2.GetCanonicalName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),UInt32, use_last_error=False)(17, 'GetCanonicalName', ((1, 'pwszPnPName'),(1, 'nMaxChars'),)))
    win32more.Media.DeviceManager.IWMDMDevice
    return IWMDMDevice2
def _define_IWMDMDevice3_head():
    class IWMDMDevice3(win32more.Media.DeviceManager.IWMDMDevice2_head):
        Guid = Guid('6c03e4fe-05db-4dda-9e3c-06233a6d5d65')
    return IWMDMDevice3
def _define_IWMDMDevice3():
    IWMDMDevice3 = win32more.Media.DeviceManager.IWMDMDevice3_head
    IWMDMDevice3.GetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(18, 'GetProperty', ((1, 'pwszPropName'),(1, 'pValue'),)))
    IWMDMDevice3.SetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(19, 'SetProperty', ((1, 'pwszPropName'),(1, 'pValue'),)))
    IWMDMDevice3.GetFormatCapability = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.DeviceManager.WMDM_FORMATCODE,POINTER(win32more.Media.DeviceManager.WMDM_FORMAT_CAPABILITY_head), use_last_error=False)(20, 'GetFormatCapability', ((1, 'format'),(1, 'pFormatSupport'),)))
    IWMDMDevice3.DeviceIoControl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Byte),UInt32,POINTER(Byte),POINTER(UInt32), use_last_error=False)(21, 'DeviceIoControl', ((1, 'dwIoControlCode'),(1, 'lpInBuffer'),(1, 'nInBufferSize'),(1, 'lpOutBuffer'),(1, 'pnOutBufferSize'),)))
    IWMDMDevice3.FindStorage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.DeviceManager.WMDM_FIND_SCOPE,win32more.Foundation.PWSTR,POINTER(win32more.Media.DeviceManager.IWMDMStorage_head), use_last_error=False)(22, 'FindStorage', ((1, 'findScope'),(1, 'pwszUniqueID'),(1, 'ppStorage'),)))
    win32more.Media.DeviceManager.IWMDMDevice2
    return IWMDMDevice3
def _define_IWMDMDeviceSession_head():
    class IWMDMDeviceSession(win32more.System.Com.IUnknown_head):
        Guid = Guid('82af0a65-9d96-412c-83e5-3c43e4b06cc7')
    return IWMDMDeviceSession
def _define_IWMDMDeviceSession():
    IWMDMDeviceSession = win32more.Media.DeviceManager.IWMDMDeviceSession_head
    IWMDMDeviceSession.BeginSession = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.DeviceManager.WMDM_SESSION_TYPE,POINTER(Byte),UInt32, use_last_error=False)(3, 'BeginSession', ((1, 'type'),(1, 'pCtx'),(1, 'dwSizeCtx'),)))
    IWMDMDeviceSession.EndSession = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.DeviceManager.WMDM_SESSION_TYPE,POINTER(Byte),UInt32, use_last_error=False)(4, 'EndSession', ((1, 'type'),(1, 'pCtx'),(1, 'dwSizeCtx'),)))
    win32more.System.Com.IUnknown
    return IWMDMDeviceSession
def _define_IWMDMEnumDevice_head():
    class IWMDMEnumDevice(win32more.System.Com.IUnknown_head):
        Guid = Guid('1dcb3a01-33ed-11d3-8470-00c04f79dbc0')
    return IWMDMEnumDevice
def _define_IWMDMEnumDevice():
    IWMDMEnumDevice = win32more.Media.DeviceManager.IWMDMEnumDevice_head
    IWMDMEnumDevice.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.DeviceManager.IWMDMDevice_head),POINTER(UInt32), use_last_error=False)(3, 'Next', ((1, 'celt'),(1, 'ppDevice'),(1, 'pceltFetched'),)))
    IWMDMEnumDevice.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(4, 'Skip', ((1, 'celt'),(1, 'pceltFetched'),)))
    IWMDMEnumDevice.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IWMDMEnumDevice.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.DeviceManager.IWMDMEnumDevice_head), use_last_error=False)(6, 'Clone', ((1, 'ppEnumDevice'),)))
    win32more.System.Com.IUnknown
    return IWMDMEnumDevice
def _define_IWMDMDeviceControl_head():
    class IWMDMDeviceControl(win32more.System.Com.IUnknown_head):
        Guid = Guid('1dcb3a04-33ed-11d3-8470-00c04f79dbc0')
    return IWMDMDeviceControl
def _define_IWMDMDeviceControl():
    IWMDMDeviceControl = win32more.Media.DeviceManager.IWMDMDeviceControl_head
    IWMDMDeviceControl.GetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetStatus', ((1, 'pdwStatus'),)))
    IWMDMDeviceControl.GetCapabilities = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(4, 'GetCapabilities', ((1, 'pdwCapabilitiesMask'),)))
    IWMDMDeviceControl.Play = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Play', ()))
    IWMDMDeviceControl.Record = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.DeviceManager._WAVEFORMATEX_head), use_last_error=False)(6, 'Record', ((1, 'pFormat'),)))
    IWMDMDeviceControl.Pause = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'Pause', ()))
    IWMDMDeviceControl.Resume = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'Resume', ()))
    IWMDMDeviceControl.Stop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(9, 'Stop', ()))
    IWMDMDeviceControl.Seek = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Int32, use_last_error=False)(10, 'Seek', ((1, 'fuMode'),(1, 'nOffset'),)))
    win32more.System.Com.IUnknown
    return IWMDMDeviceControl
def _define_IWMDMEnumStorage_head():
    class IWMDMEnumStorage(win32more.System.Com.IUnknown_head):
        Guid = Guid('1dcb3a05-33ed-11d3-8470-00c04f79dbc0')
    return IWMDMEnumStorage
def _define_IWMDMEnumStorage():
    IWMDMEnumStorage = win32more.Media.DeviceManager.IWMDMEnumStorage_head
    IWMDMEnumStorage.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.DeviceManager.IWMDMStorage_head),POINTER(UInt32), use_last_error=False)(3, 'Next', ((1, 'celt'),(1, 'ppStorage'),(1, 'pceltFetched'),)))
    IWMDMEnumStorage.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(4, 'Skip', ((1, 'celt'),(1, 'pceltFetched'),)))
    IWMDMEnumStorage.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IWMDMEnumStorage.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.DeviceManager.IWMDMEnumStorage_head), use_last_error=False)(6, 'Clone', ((1, 'ppEnumStorage'),)))
    win32more.System.Com.IUnknown
    return IWMDMEnumStorage
def _define_IWMDMStorageControl_head():
    class IWMDMStorageControl(win32more.System.Com.IUnknown_head):
        Guid = Guid('1dcb3a08-33ed-11d3-8470-00c04f79dbc0')
    return IWMDMStorageControl
def _define_IWMDMStorageControl():
    IWMDMStorageControl = win32more.Media.DeviceManager.IWMDMStorageControl_head
    IWMDMStorageControl.Insert = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,win32more.Media.DeviceManager.IWMDMOperation_head,win32more.Media.DeviceManager.IWMDMProgress_head,POINTER(win32more.Media.DeviceManager.IWMDMStorage_head), use_last_error=False)(3, 'Insert', ((1, 'fuMode'),(1, 'pwszFile'),(1, 'pOperation'),(1, 'pProgress'),(1, 'ppNewObject'),)))
    IWMDMStorageControl.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Media.DeviceManager.IWMDMProgress_head, use_last_error=False)(4, 'Delete', ((1, 'fuMode'),(1, 'pProgress'),)))
    IWMDMStorageControl.Rename = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,win32more.Media.DeviceManager.IWMDMProgress_head, use_last_error=False)(5, 'Rename', ((1, 'fuMode'),(1, 'pwszNewName'),(1, 'pProgress'),)))
    IWMDMStorageControl.Read = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,win32more.Media.DeviceManager.IWMDMProgress_head,win32more.Media.DeviceManager.IWMDMOperation_head, use_last_error=False)(6, 'Read', ((1, 'fuMode'),(1, 'pwszFile'),(1, 'pProgress'),(1, 'pOperation'),)))
    IWMDMStorageControl.Move = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Media.DeviceManager.IWMDMStorage_head,win32more.Media.DeviceManager.IWMDMProgress_head, use_last_error=False)(7, 'Move', ((1, 'fuMode'),(1, 'pTargetObject'),(1, 'pProgress'),)))
    win32more.System.Com.IUnknown
    return IWMDMStorageControl
def _define_IWMDMStorageControl2_head():
    class IWMDMStorageControl2(win32more.Media.DeviceManager.IWMDMStorageControl_head):
        Guid = Guid('972c2e88-bd6c-4125-8e09-84f837e637b6')
    return IWMDMStorageControl2
def _define_IWMDMStorageControl2():
    IWMDMStorageControl2 = win32more.Media.DeviceManager.IWMDMStorageControl2_head
    IWMDMStorageControl2.Insert2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Media.DeviceManager.IWMDMOperation_head,win32more.Media.DeviceManager.IWMDMProgress_head,win32more.System.Com.IUnknown_head,POINTER(win32more.Media.DeviceManager.IWMDMStorage_head), use_last_error=False)(8, 'Insert2', ((1, 'fuMode'),(1, 'pwszFileSource'),(1, 'pwszFileDest'),(1, 'pOperation'),(1, 'pProgress'),(1, 'pUnknown'),(1, 'ppNewObject'),)))
    win32more.Media.DeviceManager.IWMDMStorageControl
    return IWMDMStorageControl2
def _define_IWMDMStorageControl3_head():
    class IWMDMStorageControl3(win32more.Media.DeviceManager.IWMDMStorageControl2_head):
        Guid = Guid('b3266365-d4f3-4696-8d53-bd27ec60993a')
    return IWMDMStorageControl3
def _define_IWMDMStorageControl3():
    IWMDMStorageControl3 = win32more.Media.DeviceManager.IWMDMStorageControl3_head
    IWMDMStorageControl3.Insert3 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Media.DeviceManager.IWMDMOperation_head,win32more.Media.DeviceManager.IWMDMProgress_head,win32more.Media.DeviceManager.IWMDMMetaData_head,win32more.System.Com.IUnknown_head,POINTER(win32more.Media.DeviceManager.IWMDMStorage_head), use_last_error=False)(9, 'Insert3', ((1, 'fuMode'),(1, 'fuType'),(1, 'pwszFileSource'),(1, 'pwszFileDest'),(1, 'pOperation'),(1, 'pProgress'),(1, 'pMetaData'),(1, 'pUnknown'),(1, 'ppNewObject'),)))
    win32more.Media.DeviceManager.IWMDMStorageControl2
    return IWMDMStorageControl3
def _define_IWMDMObjectInfo_head():
    class IWMDMObjectInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('1dcb3a09-33ed-11d3-8470-00c04f79dbc0')
    return IWMDMObjectInfo
def _define_IWMDMObjectInfo():
    IWMDMObjectInfo = win32more.Media.DeviceManager.IWMDMObjectInfo_head
    IWMDMObjectInfo.GetPlayLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetPlayLength', ((1, 'pdwLength'),)))
    IWMDMObjectInfo.SetPlayLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'SetPlayLength', ((1, 'dwLength'),)))
    IWMDMObjectInfo.GetPlayOffset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(5, 'GetPlayOffset', ((1, 'pdwOffset'),)))
    IWMDMObjectInfo.SetPlayOffset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'SetPlayOffset', ((1, 'dwOffset'),)))
    IWMDMObjectInfo.GetTotalLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(7, 'GetTotalLength', ((1, 'pdwLength'),)))
    IWMDMObjectInfo.GetLastPlayPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(8, 'GetLastPlayPosition', ((1, 'pdwLastPos'),)))
    IWMDMObjectInfo.GetLongestPlayPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(9, 'GetLongestPlayPosition', ((1, 'pdwLongestPos'),)))
    win32more.System.Com.IUnknown
    return IWMDMObjectInfo
def _define_IWMDMRevoked_head():
    class IWMDMRevoked(win32more.System.Com.IUnknown_head):
        Guid = Guid('ebeccedb-88ee-4e55-b6a4-8d9f07d696aa')
    return IWMDMRevoked
def _define_IWMDMRevoked():
    IWMDMRevoked = win32more.Media.DeviceManager.IWMDMRevoked_head
    IWMDMRevoked.GetRevocationURL = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(3, 'GetRevocationURL', ((1, 'ppwszRevocationURL'),(1, 'pdwBufferLen'),(1, 'pdwRevokedBitFlag'),)))
    win32more.System.Com.IUnknown
    return IWMDMRevoked
def _define_IWMDMNotification_head():
    class IWMDMNotification(win32more.System.Com.IUnknown_head):
        Guid = Guid('3f5e95c0-0f43-4ed4-93d2-c89a45d59b81')
    return IWMDMNotification
def _define_IWMDMNotification():
    IWMDMNotification = win32more.Media.DeviceManager.IWMDMNotification_head
    IWMDMNotification.WMDMMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR, use_last_error=False)(3, 'WMDMMessage', ((1, 'dwMessageType'),(1, 'pwszCanonicalName'),)))
    win32more.System.Com.IUnknown
    return IWMDMNotification
def _define_WMDMDetermineMaxPropStringLen_head():
    class WMDMDetermineMaxPropStringLen(Union):
        pass
    return WMDMDetermineMaxPropStringLen
def _define_WMDMDetermineMaxPropStringLen():
    WMDMDetermineMaxPropStringLen = win32more.Media.DeviceManager.WMDMDetermineMaxPropStringLen_head
    WMDMDetermineMaxPropStringLen._fields_ = [
        ("sz001", Char * 27),
        ("sz002", Char * 31),
        ("sz003", Char * 14),
        ("sz004", Char * 16),
        ("sz005", Char * 22),
        ("sz006", Char * 14),
        ("sz007", Char * 20),
        ("sz008", Char * 20),
        ("sz009", Char * 22),
        ("sz010", Char * 11),
        ("sz011", Char * 12),
        ("sz012", Char * 17),
        ("sz013", Char * 17),
        ("sz014", Char * 16),
        ("sz015", Char * 17),
        ("sz016", Char * 11),
        ("sz017", Char * 11),
        ("sz018", Char * 15),
        ("sz019", Char * 22),
        ("sz020", Char * 20),
        ("sz021", Char * 22),
        ("sz022", Char * 21),
        ("sz023", Char * 24),
        ("sz024", Char * 20),
        ("sz025", Char * 10),
        ("sz026", Char * 14),
        ("sz027", Char * 11),
        ("sz028", Char * 11),
        ("sz029", Char * 13),
        ("sz030", Char * 17),
        ("sz031", Char * 16),
        ("sz032", Char * 17),
        ("sz033", Char * 20),
        ("sz034", Char * 19),
        ("sz035", Char * 18),
        ("sz036", Char * 18),
        ("sz037", Char * 15),
        ("sz041", Char * 14),
        ("sz043", Char * 22),
        ("sz044", Char * 16),
        ("sz045", Char * 20),
        ("sz046", Char * 14),
        ("sz047", Char * 14),
        ("sz048", Char * 12),
        ("sz049", Char * 25),
        ("sz050", Char * 26),
        ("sz051", Char * 25),
        ("sz052", Char * 16),
        ("sz053", Char * 24),
        ("sz054", Char * 15),
        ("sz055", Char * 21),
        ("sz056", Char * 16),
        ("sz057", Char * 22),
        ("sz058", Char * 14),
        ("sz059", Char * 25),
        ("sz060", Char * 18),
        ("sz061", Char * 22),
        ("sz062", Char * 26),
        ("sz063", Char * 36),
        ("sz064", Char * 23),
        ("sz065", Char * 12),
        ("sz066", Char * 24),
        ("sz067", Char * 11),
        ("sz068", Char * 12),
        ("sz069", Char * 14),
        ("sz070", Char * 20),
        ("sz071", Char * 15),
        ("sz072", Char * 14),
        ("sz073", Char * 31),
        ("sz074", Char * 24),
        ("sz075", Char * 22),
        ("sz076", Char * 24),
        ("sz077", Char * 21),
        ("sz078", Char * 27),
        ("sz079", Char * 27),
        ("sz080", Char * 20),
        ("sz081", Char * 33),
        ("sz082", Char * 21),
        ("sz083", Char * 32),
        ("sz084", Char * 26),
        ("sz085", Char * 18),
        ("sz086", Char * 30),
    ]
    return WMDMDetermineMaxPropStringLen
def _define_IMDServiceProvider_head():
    class IMDServiceProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('1dcb3a10-33ed-11d3-8470-00c04f79dbc0')
    return IMDServiceProvider
def _define_IMDServiceProvider():
    IMDServiceProvider = win32more.Media.DeviceManager.IMDServiceProvider_head
    IMDServiceProvider.GetDeviceCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetDeviceCount', ((1, 'pdwCount'),)))
    IMDServiceProvider.EnumDevices = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.DeviceManager.IMDSPEnumDevice_head), use_last_error=False)(4, 'EnumDevices', ((1, 'ppEnumDevice'),)))
    win32more.System.Com.IUnknown
    return IMDServiceProvider
def _define_IMDServiceProvider2_head():
    class IMDServiceProvider2(win32more.Media.DeviceManager.IMDServiceProvider_head):
        Guid = Guid('b2fa24b7-cda3-4694-9862-413ae1a34819')
    return IMDServiceProvider2
def _define_IMDServiceProvider2():
    IMDServiceProvider2 = win32more.Media.DeviceManager.IMDServiceProvider2_head
    IMDServiceProvider2.CreateDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(POINTER(win32more.Media.DeviceManager.IMDSPDevice_head)), use_last_error=False)(5, 'CreateDevice', ((1, 'pwszDevicePath'),(1, 'pdwCount'),(1, 'pppDeviceArray'),)))
    win32more.Media.DeviceManager.IMDServiceProvider
    return IMDServiceProvider2
def _define_IMDServiceProvider3_head():
    class IMDServiceProvider3(win32more.Media.DeviceManager.IMDServiceProvider2_head):
        Guid = Guid('4ed13ef3-a971-4d19-9f51-0e1826b2da57')
    return IMDServiceProvider3
def _define_IMDServiceProvider3():
    IMDServiceProvider3 = win32more.Media.DeviceManager.IMDServiceProvider3_head
    IMDServiceProvider3.SetDeviceEnumPreference = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'SetDeviceEnumPreference', ((1, 'dwEnumPref'),)))
    win32more.Media.DeviceManager.IMDServiceProvider2
    return IMDServiceProvider3
def _define_IMDSPEnumDevice_head():
    class IMDSPEnumDevice(win32more.System.Com.IUnknown_head):
        Guid = Guid('1dcb3a11-33ed-11d3-8470-00c04f79dbc0')
    return IMDSPEnumDevice
def _define_IMDSPEnumDevice():
    IMDSPEnumDevice = win32more.Media.DeviceManager.IMDSPEnumDevice_head
    IMDSPEnumDevice.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.DeviceManager.IMDSPDevice_head),POINTER(UInt32), use_last_error=False)(3, 'Next', ((1, 'celt'),(1, 'ppDevice'),(1, 'pceltFetched'),)))
    IMDSPEnumDevice.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(4, 'Skip', ((1, 'celt'),(1, 'pceltFetched'),)))
    IMDSPEnumDevice.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IMDSPEnumDevice.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.DeviceManager.IMDSPEnumDevice_head), use_last_error=False)(6, 'Clone', ((1, 'ppEnumDevice'),)))
    win32more.System.Com.IUnknown
    return IMDSPEnumDevice
def _define_IMDSPDevice_head():
    class IMDSPDevice(win32more.System.Com.IUnknown_head):
        Guid = Guid('1dcb3a12-33ed-11d3-8470-00c04f79dbc0')
    return IMDSPDevice
def _define_IMDSPDevice():
    IMDSPDevice = win32more.Media.DeviceManager.IMDSPDevice_head
    IMDSPDevice.GetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),UInt32, use_last_error=False)(3, 'GetName', ((1, 'pwszName'),(1, 'nMaxChars'),)))
    IMDSPDevice.GetManufacturer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),UInt32, use_last_error=False)(4, 'GetManufacturer', ((1, 'pwszName'),(1, 'nMaxChars'),)))
    IMDSPDevice.GetVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(5, 'GetVersion', ((1, 'pdwVersion'),)))
    IMDSPDevice.GetType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(6, 'GetType', ((1, 'pdwType'),)))
    IMDSPDevice.GetSerialNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.DeviceManager.WMDMID_head),c_char_p_no, use_last_error=False)(7, 'GetSerialNumber', ((1, 'pSerialNumber'),(1, 'abMac'),)))
    IMDSPDevice.GetPowerSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(8, 'GetPowerSource', ((1, 'pdwPowerSource'),(1, 'pdwPercentRemaining'),)))
    IMDSPDevice.GetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(9, 'GetStatus', ((1, 'pdwStatus'),)))
    IMDSPDevice.GetDeviceIcon = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(10, 'GetDeviceIcon', ((1, 'hIcon'),)))
    IMDSPDevice.EnumStorage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.DeviceManager.IMDSPEnumStorage_head), use_last_error=False)(11, 'EnumStorage', ((1, 'ppEnumStorage'),)))
    IMDSPDevice.GetFormatSupport = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Media.DeviceManager._WAVEFORMATEX_head)),POINTER(UInt32),POINTER(POINTER(win32more.Foundation.PWSTR)),POINTER(UInt32), use_last_error=False)(12, 'GetFormatSupport', ((1, 'pFormatEx'),(1, 'pnFormatCount'),(1, 'pppwszMimeType'),(1, 'pnMimeTypeCount'),)))
    IMDSPDevice.SendOpaqueCommand = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.DeviceManager.OPAQUECOMMAND_head), use_last_error=False)(13, 'SendOpaqueCommand', ((1, 'pCommand'),)))
    win32more.System.Com.IUnknown
    return IMDSPDevice
def _define_IMDSPDevice2_head():
    class IMDSPDevice2(win32more.Media.DeviceManager.IMDSPDevice_head):
        Guid = Guid('420d16ad-c97d-4e00-82aa-00e9f4335ddd')
    return IMDSPDevice2
def _define_IMDSPDevice2():
    IMDSPDevice2 = win32more.Media.DeviceManager.IMDSPDevice2_head
    IMDSPDevice2.GetStorage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Media.DeviceManager.IMDSPStorage_head), use_last_error=False)(14, 'GetStorage', ((1, 'pszStorageName'),(1, 'ppStorage'),)))
    IMDSPDevice2.GetFormatSupport2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(POINTER(win32more.Media.DeviceManager._WAVEFORMATEX_head)),POINTER(UInt32),POINTER(POINTER(win32more.Media.DeviceManager._VIDEOINFOHEADER_head)),POINTER(UInt32),POINTER(POINTER(win32more.Media.DeviceManager.WMFILECAPABILITIES_head)),POINTER(UInt32), use_last_error=False)(15, 'GetFormatSupport2', ((1, 'dwFlags'),(1, 'ppAudioFormatEx'),(1, 'pnAudioFormatCount'),(1, 'ppVideoFormatEx'),(1, 'pnVideoFormatCount'),(1, 'ppFileType'),(1, 'pnFileTypeCount'),)))
    IMDSPDevice2.GetSpecifyPropertyPages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.ISpecifyPropertyPages_head),POINTER(POINTER(win32more.System.Com.IUnknown_head)),POINTER(UInt32), use_last_error=False)(16, 'GetSpecifyPropertyPages', ((1, 'ppSpecifyPropPages'),(1, 'pppUnknowns'),(1, 'pcUnks'),)))
    IMDSPDevice2.GetCanonicalName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),UInt32, use_last_error=False)(17, 'GetCanonicalName', ((1, 'pwszPnPName'),(1, 'nMaxChars'),)))
    win32more.Media.DeviceManager.IMDSPDevice
    return IMDSPDevice2
def _define_IMDSPDevice3_head():
    class IMDSPDevice3(win32more.Media.DeviceManager.IMDSPDevice2_head):
        Guid = Guid('1a839845-fc55-487c-976f-ee38ac0e8c4e')
    return IMDSPDevice3
def _define_IMDSPDevice3():
    IMDSPDevice3 = win32more.Media.DeviceManager.IMDSPDevice3_head
    IMDSPDevice3.GetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(18, 'GetProperty', ((1, 'pwszPropName'),(1, 'pValue'),)))
    IMDSPDevice3.SetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(19, 'SetProperty', ((1, 'pwszPropName'),(1, 'pValue'),)))
    IMDSPDevice3.GetFormatCapability = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.DeviceManager.WMDM_FORMATCODE,POINTER(win32more.Media.DeviceManager.WMDM_FORMAT_CAPABILITY_head), use_last_error=False)(20, 'GetFormatCapability', ((1, 'format'),(1, 'pFormatSupport'),)))
    IMDSPDevice3.DeviceIoControl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Byte),UInt32,POINTER(Byte),POINTER(UInt32), use_last_error=False)(21, 'DeviceIoControl', ((1, 'dwIoControlCode'),(1, 'lpInBuffer'),(1, 'nInBufferSize'),(1, 'lpOutBuffer'),(1, 'pnOutBufferSize'),)))
    IMDSPDevice3.FindStorage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.DeviceManager.WMDM_FIND_SCOPE,win32more.Foundation.PWSTR,POINTER(win32more.Media.DeviceManager.IMDSPStorage_head), use_last_error=False)(22, 'FindStorage', ((1, 'findScope'),(1, 'pwszUniqueID'),(1, 'ppStorage'),)))
    win32more.Media.DeviceManager.IMDSPDevice2
    return IMDSPDevice3
def _define_IMDSPDeviceControl_head():
    class IMDSPDeviceControl(win32more.System.Com.IUnknown_head):
        Guid = Guid('1dcb3a14-33ed-11d3-8470-00c04f79dbc0')
    return IMDSPDeviceControl
def _define_IMDSPDeviceControl():
    IMDSPDeviceControl = win32more.Media.DeviceManager.IMDSPDeviceControl_head
    IMDSPDeviceControl.GetDCStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetDCStatus', ((1, 'pdwStatus'),)))
    IMDSPDeviceControl.GetCapabilities = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(4, 'GetCapabilities', ((1, 'pdwCapabilitiesMask'),)))
    IMDSPDeviceControl.Play = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Play', ()))
    IMDSPDeviceControl.Record = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.DeviceManager._WAVEFORMATEX_head), use_last_error=False)(6, 'Record', ((1, 'pFormat'),)))
    IMDSPDeviceControl.Pause = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'Pause', ()))
    IMDSPDeviceControl.Resume = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'Resume', ()))
    IMDSPDeviceControl.Stop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(9, 'Stop', ()))
    IMDSPDeviceControl.Seek = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Int32, use_last_error=False)(10, 'Seek', ((1, 'fuMode'),(1, 'nOffset'),)))
    win32more.System.Com.IUnknown
    return IMDSPDeviceControl
def _define_IMDSPEnumStorage_head():
    class IMDSPEnumStorage(win32more.System.Com.IUnknown_head):
        Guid = Guid('1dcb3a15-33ed-11d3-8470-00c04f79dbc0')
    return IMDSPEnumStorage
def _define_IMDSPEnumStorage():
    IMDSPEnumStorage = win32more.Media.DeviceManager.IMDSPEnumStorage_head
    IMDSPEnumStorage.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.DeviceManager.IMDSPStorage_head),POINTER(UInt32), use_last_error=False)(3, 'Next', ((1, 'celt'),(1, 'ppStorage'),(1, 'pceltFetched'),)))
    IMDSPEnumStorage.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(4, 'Skip', ((1, 'celt'),(1, 'pceltFetched'),)))
    IMDSPEnumStorage.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IMDSPEnumStorage.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.DeviceManager.IMDSPEnumStorage_head), use_last_error=False)(6, 'Clone', ((1, 'ppEnumStorage'),)))
    win32more.System.Com.IUnknown
    return IMDSPEnumStorage
def _define_IMDSPStorage_head():
    class IMDSPStorage(win32more.System.Com.IUnknown_head):
        Guid = Guid('1dcb3a16-33ed-11d3-8470-00c04f79dbc0')
    return IMDSPStorage
def _define_IMDSPStorage():
    IMDSPStorage = win32more.Media.DeviceManager.IMDSPStorage_head
    IMDSPStorage.SetAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.DeviceManager._WAVEFORMATEX_head), use_last_error=False)(3, 'SetAttributes', ((1, 'dwAttributes'),(1, 'pFormat'),)))
    IMDSPStorage.GetStorageGlobals = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.DeviceManager.IMDSPStorageGlobals_head), use_last_error=False)(4, 'GetStorageGlobals', ((1, 'ppStorageGlobals'),)))
    IMDSPStorage.GetAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(win32more.Media.DeviceManager._WAVEFORMATEX_head), use_last_error=False)(5, 'GetAttributes', ((1, 'pdwAttributes'),(1, 'pFormat'),)))
    IMDSPStorage.GetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),UInt32, use_last_error=False)(6, 'GetName', ((1, 'pwszName'),(1, 'nMaxChars'),)))
    IMDSPStorage.GetDate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.DeviceManager.WMDMDATETIME_head), use_last_error=False)(7, 'GetDate', ((1, 'pDateTimeUTC'),)))
    IMDSPStorage.GetSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(8, 'GetSize', ((1, 'pdwSizeLow'),(1, 'pdwSizeHigh'),)))
    IMDSPStorage.GetRights = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Media.DeviceManager.WMDMRIGHTS_head)),POINTER(UInt32),c_char_p_no, use_last_error=False)(9, 'GetRights', ((1, 'ppRights'),(1, 'pnRightsCount'),(1, 'abMac'),)))
    IMDSPStorage.CreateStorage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.DeviceManager._WAVEFORMATEX_head),win32more.Foundation.PWSTR,POINTER(win32more.Media.DeviceManager.IMDSPStorage_head), use_last_error=False)(10, 'CreateStorage', ((1, 'dwAttributes'),(1, 'pFormat'),(1, 'pwszName'),(1, 'ppNewStorage'),)))
    IMDSPStorage.EnumStorage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.DeviceManager.IMDSPEnumStorage_head), use_last_error=False)(11, 'EnumStorage', ((1, 'ppEnumStorage'),)))
    IMDSPStorage.SendOpaqueCommand = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.DeviceManager.OPAQUECOMMAND_head), use_last_error=False)(12, 'SendOpaqueCommand', ((1, 'pCommand'),)))
    win32more.System.Com.IUnknown
    return IMDSPStorage
def _define_IMDSPStorage2_head():
    class IMDSPStorage2(win32more.Media.DeviceManager.IMDSPStorage_head):
        Guid = Guid('0a5e07a5-6454-4451-9c36-1c6ae7e2b1d6')
    return IMDSPStorage2
def _define_IMDSPStorage2():
    IMDSPStorage2 = win32more.Media.DeviceManager.IMDSPStorage2_head
    IMDSPStorage2.GetStorage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Media.DeviceManager.IMDSPStorage_head), use_last_error=False)(13, 'GetStorage', ((1, 'pszStorageName'),(1, 'ppStorage'),)))
    IMDSPStorage2.CreateStorage2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.Media.DeviceManager._WAVEFORMATEX_head),POINTER(win32more.Media.DeviceManager._VIDEOINFOHEADER_head),win32more.Foundation.PWSTR,UInt64,POINTER(win32more.Media.DeviceManager.IMDSPStorage_head), use_last_error=False)(14, 'CreateStorage2', ((1, 'dwAttributes'),(1, 'dwAttributesEx'),(1, 'pAudioFormat'),(1, 'pVideoFormat'),(1, 'pwszName'),(1, 'qwFileSize'),(1, 'ppNewStorage'),)))
    IMDSPStorage2.SetAttributes2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.Media.DeviceManager._WAVEFORMATEX_head),POINTER(win32more.Media.DeviceManager._VIDEOINFOHEADER_head), use_last_error=False)(15, 'SetAttributes2', ((1, 'dwAttributes'),(1, 'dwAttributesEx'),(1, 'pAudioFormat'),(1, 'pVideoFormat'),)))
    IMDSPStorage2.GetAttributes2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32),POINTER(win32more.Media.DeviceManager._WAVEFORMATEX_head),POINTER(win32more.Media.DeviceManager._VIDEOINFOHEADER_head), use_last_error=False)(16, 'GetAttributes2', ((1, 'pdwAttributes'),(1, 'pdwAttributesEx'),(1, 'pAudioFormat'),(1, 'pVideoFormat'),)))
    win32more.Media.DeviceManager.IMDSPStorage
    return IMDSPStorage2
def _define_IMDSPStorage3_head():
    class IMDSPStorage3(win32more.Media.DeviceManager.IMDSPStorage2_head):
        Guid = Guid('6c669867-97ed-4a67-9706-1c5529d2a414')
    return IMDSPStorage3
def _define_IMDSPStorage3():
    IMDSPStorage3 = win32more.Media.DeviceManager.IMDSPStorage3_head
    IMDSPStorage3.GetMetadata = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.DeviceManager.IWMDMMetaData_head, use_last_error=False)(17, 'GetMetadata', ((1, 'pMetadata'),)))
    IMDSPStorage3.SetMetadata = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.DeviceManager.IWMDMMetaData_head, use_last_error=False)(18, 'SetMetadata', ((1, 'pMetadata'),)))
    win32more.Media.DeviceManager.IMDSPStorage2
    return IMDSPStorage3
def _define_IMDSPStorage4_head():
    class IMDSPStorage4(win32more.Media.DeviceManager.IMDSPStorage3_head):
        Guid = Guid('3133b2c4-515c-481b-b1ce-39327ecb4f74')
    return IMDSPStorage4
def _define_IMDSPStorage4():
    IMDSPStorage4 = win32more.Media.DeviceManager.IMDSPStorage4_head
    IMDSPStorage4.SetReferences = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.DeviceManager.IMDSPStorage_head), use_last_error=False)(19, 'SetReferences', ((1, 'dwRefs'),(1, 'ppISPStorage'),)))
    IMDSPStorage4.GetReferences = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(POINTER(win32more.Media.DeviceManager.IMDSPStorage_head)), use_last_error=False)(20, 'GetReferences', ((1, 'pdwRefs'),(1, 'pppISPStorage'),)))
    IMDSPStorage4.CreateStorageWithMetadata = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,win32more.Media.DeviceManager.IWMDMMetaData_head,UInt64,POINTER(win32more.Media.DeviceManager.IMDSPStorage_head), use_last_error=False)(21, 'CreateStorageWithMetadata', ((1, 'dwAttributes'),(1, 'pwszName'),(1, 'pMetadata'),(1, 'qwFileSize'),(1, 'ppNewStorage'),)))
    IMDSPStorage4.GetSpecifiedMetadata = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.PWSTR),win32more.Media.DeviceManager.IWMDMMetaData_head, use_last_error=False)(22, 'GetSpecifiedMetadata', ((1, 'cProperties'),(1, 'ppwszPropNames'),(1, 'pMetadata'),)))
    IMDSPStorage4.FindStorage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.DeviceManager.WMDM_FIND_SCOPE,win32more.Foundation.PWSTR,POINTER(win32more.Media.DeviceManager.IMDSPStorage_head), use_last_error=False)(23, 'FindStorage', ((1, 'findScope'),(1, 'pwszUniqueID'),(1, 'ppStorage'),)))
    IMDSPStorage4.GetParent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.DeviceManager.IMDSPStorage_head), use_last_error=False)(24, 'GetParent', ((1, 'ppStorage'),)))
    win32more.Media.DeviceManager.IMDSPStorage3
    return IMDSPStorage4
def _define_IMDSPStorageGlobals_head():
    class IMDSPStorageGlobals(win32more.System.Com.IUnknown_head):
        Guid = Guid('1dcb3a17-33ed-11d3-8470-00c04f79dbc0')
    return IMDSPStorageGlobals
def _define_IMDSPStorageGlobals():
    IMDSPStorageGlobals = win32more.Media.DeviceManager.IMDSPStorageGlobals_head
    IMDSPStorageGlobals.GetCapabilities = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetCapabilities', ((1, 'pdwCapabilities'),)))
    IMDSPStorageGlobals.GetSerialNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.DeviceManager.WMDMID_head),c_char_p_no, use_last_error=False)(4, 'GetSerialNumber', ((1, 'pSerialNum'),(1, 'abMac'),)))
    IMDSPStorageGlobals.GetTotalSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(5, 'GetTotalSize', ((1, 'pdwTotalSizeLow'),(1, 'pdwTotalSizeHigh'),)))
    IMDSPStorageGlobals.GetTotalFree = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(6, 'GetTotalFree', ((1, 'pdwFreeLow'),(1, 'pdwFreeHigh'),)))
    IMDSPStorageGlobals.GetTotalBad = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(7, 'GetTotalBad', ((1, 'pdwBadLow'),(1, 'pdwBadHigh'),)))
    IMDSPStorageGlobals.GetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(8, 'GetStatus', ((1, 'pdwStatus'),)))
    IMDSPStorageGlobals.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Media.DeviceManager.IWMDMProgress_head, use_last_error=False)(9, 'Initialize', ((1, 'fuMode'),(1, 'pProgress'),)))
    IMDSPStorageGlobals.GetDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.DeviceManager.IMDSPDevice_head), use_last_error=False)(10, 'GetDevice', ((1, 'ppDevice'),)))
    IMDSPStorageGlobals.GetRootStorage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.DeviceManager.IMDSPStorage_head), use_last_error=False)(11, 'GetRootStorage', ((1, 'ppRoot'),)))
    win32more.System.Com.IUnknown
    return IMDSPStorageGlobals
def _define_IMDSPObjectInfo_head():
    class IMDSPObjectInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('1dcb3a19-33ed-11d3-8470-00c04f79dbc0')
    return IMDSPObjectInfo
def _define_IMDSPObjectInfo():
    IMDSPObjectInfo = win32more.Media.DeviceManager.IMDSPObjectInfo_head
    IMDSPObjectInfo.GetPlayLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetPlayLength', ((1, 'pdwLength'),)))
    IMDSPObjectInfo.SetPlayLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'SetPlayLength', ((1, 'dwLength'),)))
    IMDSPObjectInfo.GetPlayOffset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(5, 'GetPlayOffset', ((1, 'pdwOffset'),)))
    IMDSPObjectInfo.SetPlayOffset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'SetPlayOffset', ((1, 'dwOffset'),)))
    IMDSPObjectInfo.GetTotalLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(7, 'GetTotalLength', ((1, 'pdwLength'),)))
    IMDSPObjectInfo.GetLastPlayPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(8, 'GetLastPlayPosition', ((1, 'pdwLastPos'),)))
    IMDSPObjectInfo.GetLongestPlayPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(9, 'GetLongestPlayPosition', ((1, 'pdwLongestPos'),)))
    win32more.System.Com.IUnknown
    return IMDSPObjectInfo
def _define_IMDSPObject_head():
    class IMDSPObject(win32more.System.Com.IUnknown_head):
        Guid = Guid('1dcb3a18-33ed-11d3-8470-00c04f79dbc0')
    return IMDSPObject
def _define_IMDSPObject():
    IMDSPObject = win32more.Media.DeviceManager.IMDSPObject_head
    IMDSPObject.Open = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(3, 'Open', ((1, 'fuMode'),)))
    IMDSPObject.Read = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),POINTER(UInt32),c_char_p_no, use_last_error=False)(4, 'Read', ((1, 'pData'),(1, 'pdwSize'),(1, 'abMac'),)))
    IMDSPObject.Write = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),POINTER(UInt32),c_char_p_no, use_last_error=False)(5, 'Write', ((1, 'pData'),(1, 'pdwSize'),(1, 'abMac'),)))
    IMDSPObject.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Media.DeviceManager.IWMDMProgress_head, use_last_error=False)(6, 'Delete', ((1, 'fuMode'),(1, 'pProgress'),)))
    IMDSPObject.Seek = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(7, 'Seek', ((1, 'fuFlags'),(1, 'dwOffset'),)))
    IMDSPObject.Rename = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Media.DeviceManager.IWMDMProgress_head, use_last_error=False)(8, 'Rename', ((1, 'pwszNewName'),(1, 'pProgress'),)))
    IMDSPObject.Move = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Media.DeviceManager.IWMDMProgress_head,win32more.Media.DeviceManager.IMDSPStorage_head, use_last_error=False)(9, 'Move', ((1, 'fuMode'),(1, 'pProgress'),(1, 'pTarget'),)))
    IMDSPObject.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(10, 'Close', ()))
    win32more.System.Com.IUnknown
    return IMDSPObject
def _define_IMDSPObject2_head():
    class IMDSPObject2(win32more.Media.DeviceManager.IMDSPObject_head):
        Guid = Guid('3f34cd3e-5907-4341-9af9-97f4187c3aa5')
    return IMDSPObject2
def _define_IMDSPObject2():
    IMDSPObject2 = win32more.Media.DeviceManager.IMDSPObject2_head
    IMDSPObject2.ReadOnClearChannel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),POINTER(UInt32), use_last_error=False)(11, 'ReadOnClearChannel', ((1, 'pData'),(1, 'pdwSize'),)))
    IMDSPObject2.WriteOnClearChannel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),POINTER(UInt32), use_last_error=False)(12, 'WriteOnClearChannel', ((1, 'pData'),(1, 'pdwSize'),)))
    win32more.Media.DeviceManager.IMDSPObject
    return IMDSPObject2
def _define_IMDSPDirectTransfer_head():
    class IMDSPDirectTransfer(win32more.System.Com.IUnknown_head):
        Guid = Guid('c2fe57a8-9304-478c-9ee4-47e397b912d7')
    return IMDSPDirectTransfer
def _define_IMDSPDirectTransfer():
    IMDSPDirectTransfer = win32more.Media.DeviceManager.IMDSPDirectTransfer_head
    IMDSPDirectTransfer.TransferToDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Media.DeviceManager.IWMDMOperation_head,UInt32,win32more.Foundation.PWSTR,win32more.Media.DeviceManager.IWMDMMetaData_head,win32more.Media.DeviceManager.IWMDMProgress_head,POINTER(win32more.Media.DeviceManager.IMDSPStorage_head), use_last_error=False)(3, 'TransferToDevice', ((1, 'pwszSourceFilePath'),(1, 'pSourceOperation'),(1, 'fuFlags'),(1, 'pwszDestinationName'),(1, 'pSourceMetaData'),(1, 'pTransferProgress'),(1, 'ppNewObject'),)))
    win32more.System.Com.IUnknown
    return IMDSPDirectTransfer
def _define_IMDSPRevoked_head():
    class IMDSPRevoked(win32more.System.Com.IUnknown_head):
        Guid = Guid('a4e8f2d4-3f31-464d-b53d-4fc335998184')
    return IMDSPRevoked
def _define_IMDSPRevoked():
    IMDSPRevoked = win32more.Media.DeviceManager.IMDSPRevoked_head
    IMDSPRevoked.GetRevocationURL = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR),POINTER(UInt32), use_last_error=False)(3, 'GetRevocationURL', ((1, 'ppwszRevocationURL'),(1, 'pdwBufferLen'),)))
    win32more.System.Com.IUnknown
    return IMDSPRevoked
def _define_ISCPSecureAuthenticate_head():
    class ISCPSecureAuthenticate(win32more.System.Com.IUnknown_head):
        Guid = Guid('1dcb3a0f-33ed-11d3-8470-00c04f79dbc0')
    return ISCPSecureAuthenticate
def _define_ISCPSecureAuthenticate():
    ISCPSecureAuthenticate = win32more.Media.DeviceManager.ISCPSecureAuthenticate_head
    ISCPSecureAuthenticate.GetSecureQuery = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.DeviceManager.ISCPSecureQuery_head), use_last_error=False)(3, 'GetSecureQuery', ((1, 'ppSecureQuery'),)))
    win32more.System.Com.IUnknown
    return ISCPSecureAuthenticate
def _define_ISCPSecureAuthenticate2_head():
    class ISCPSecureAuthenticate2(win32more.Media.DeviceManager.ISCPSecureAuthenticate_head):
        Guid = Guid('b580cfae-1672-47e2-acaa-44bbecbcae5b')
    return ISCPSecureAuthenticate2
def _define_ISCPSecureAuthenticate2():
    ISCPSecureAuthenticate2 = win32more.Media.DeviceManager.ISCPSecureAuthenticate2_head
    ISCPSecureAuthenticate2.GetSCPSession = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.DeviceManager.ISCPSession_head), use_last_error=False)(4, 'GetSCPSession', ((1, 'ppSCPSession'),)))
    win32more.Media.DeviceManager.ISCPSecureAuthenticate
    return ISCPSecureAuthenticate2
def _define_ISCPSecureQuery_head():
    class ISCPSecureQuery(win32more.System.Com.IUnknown_head):
        Guid = Guid('1dcb3a0d-33ed-11d3-8470-00c04f79dbc0')
    return ISCPSecureQuery
def _define_ISCPSecureQuery():
    ISCPSecureQuery = win32more.Media.DeviceManager.ISCPSecureQuery_head
    ISCPSecureQuery.GetDataDemands = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32),POINTER(UInt32),c_char_p_no, use_last_error=False)(3, 'GetDataDemands', ((1, 'pfuFlags'),(1, 'pdwMinRightsData'),(1, 'pdwMinExamineData'),(1, 'pdwMinDecideData'),(1, 'abMac'),)))
    ISCPSecureQuery.ExamineData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,POINTER(Byte),UInt32,c_char_p_no, use_last_error=False)(4, 'ExamineData', ((1, 'fuFlags'),(1, 'pwszExtension'),(1, 'pData'),(1, 'dwSize'),(1, 'abMac'),)))
    ISCPSecureQuery.MakeDecision = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Byte),UInt32,UInt32,POINTER(Byte),UInt32,win32more.Media.DeviceManager.IMDSPStorageGlobals_head,POINTER(win32more.Media.DeviceManager.ISCPSecureExchange_head),c_char_p_no, use_last_error=False)(5, 'MakeDecision', ((1, 'fuFlags'),(1, 'pData'),(1, 'dwSize'),(1, 'dwAppSec'),(1, 'pbSPSessionKey'),(1, 'dwSessionKeyLen'),(1, 'pStorageGlobals'),(1, 'ppExchange'),(1, 'abMac'),)))
    ISCPSecureQuery.GetRights = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),UInt32,POINTER(Byte),UInt32,win32more.Media.DeviceManager.IMDSPStorageGlobals_head,POINTER(POINTER(win32more.Media.DeviceManager.WMDMRIGHTS_head)),POINTER(UInt32),c_char_p_no, use_last_error=False)(6, 'GetRights', ((1, 'pData'),(1, 'dwSize'),(1, 'pbSPSessionKey'),(1, 'dwSessionKeyLen'),(1, 'pStgGlobals'),(1, 'ppRights'),(1, 'pnRightsCount'),(1, 'abMac'),)))
    win32more.System.Com.IUnknown
    return ISCPSecureQuery
def _define_ISCPSecureQuery2_head():
    class ISCPSecureQuery2(win32more.Media.DeviceManager.ISCPSecureQuery_head):
        Guid = Guid('ebe17e25-4fd7-4632-af46-6d93d4fcc72e')
    return ISCPSecureQuery2
def _define_ISCPSecureQuery2():
    ISCPSecureQuery2 = win32more.Media.DeviceManager.ISCPSecureQuery2_head
    ISCPSecureQuery2.MakeDecision2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Byte),UInt32,UInt32,POINTER(Byte),UInt32,win32more.Media.DeviceManager.IMDSPStorageGlobals_head,POINTER(Byte),UInt32,POINTER(Byte),UInt32,POINTER(win32more.Foundation.PWSTR),POINTER(UInt32),POINTER(UInt32),POINTER(UInt64),win32more.System.Com.IUnknown_head,POINTER(win32more.Media.DeviceManager.ISCPSecureExchange_head),c_char_p_no, use_last_error=False)(7, 'MakeDecision2', ((1, 'fuFlags'),(1, 'pData'),(1, 'dwSize'),(1, 'dwAppSec'),(1, 'pbSPSessionKey'),(1, 'dwSessionKeyLen'),(1, 'pStorageGlobals'),(1, 'pAppCertApp'),(1, 'dwAppCertAppLen'),(1, 'pAppCertSP'),(1, 'dwAppCertSPLen'),(1, 'pszRevocationURL'),(1, 'pdwRevocationURLLen'),(1, 'pdwRevocationBitFlag'),(1, 'pqwFileSize'),(1, 'pUnknown'),(1, 'ppExchange'),(1, 'abMac'),)))
    win32more.Media.DeviceManager.ISCPSecureQuery
    return ISCPSecureQuery2
def _define_ISCPSecureExchange_head():
    class ISCPSecureExchange(win32more.System.Com.IUnknown_head):
        Guid = Guid('1dcb3a0e-33ed-11d3-8470-00c04f79dbc0')
    return ISCPSecureExchange
def _define_ISCPSecureExchange():
    ISCPSecureExchange = win32more.Media.DeviceManager.ISCPSecureExchange_head
    ISCPSecureExchange.TransferContainerData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),UInt32,POINTER(UInt32),c_char_p_no, use_last_error=False)(3, 'TransferContainerData', ((1, 'pData'),(1, 'dwSize'),(1, 'pfuReadyFlags'),(1, 'abMac'),)))
    ISCPSecureExchange.ObjectData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),POINTER(UInt32),c_char_p_no, use_last_error=False)(4, 'ObjectData', ((1, 'pData'),(1, 'pdwSize'),(1, 'abMac'),)))
    ISCPSecureExchange.TransferComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'TransferComplete', ()))
    win32more.System.Com.IUnknown
    return ISCPSecureExchange
def _define_ISCPSecureExchange2_head():
    class ISCPSecureExchange2(win32more.Media.DeviceManager.ISCPSecureExchange_head):
        Guid = Guid('6c62fc7b-2690-483f-9d44-0a20cb35577c')
    return ISCPSecureExchange2
def _define_ISCPSecureExchange2():
    ISCPSecureExchange2 = win32more.Media.DeviceManager.ISCPSecureExchange2_head
    ISCPSecureExchange2.TransferContainerData2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),UInt32,win32more.Media.DeviceManager.IWMDMProgress3_head,POINTER(UInt32),c_char_p_no, use_last_error=False)(6, 'TransferContainerData2', ((1, 'pData'),(1, 'dwSize'),(1, 'pProgressCallback'),(1, 'pfuReadyFlags'),(1, 'abMac'),)))
    win32more.Media.DeviceManager.ISCPSecureExchange
    return ISCPSecureExchange2
def _define_ISCPSecureExchange3_head():
    class ISCPSecureExchange3(win32more.Media.DeviceManager.ISCPSecureExchange2_head):
        Guid = Guid('ab4e77e4-8908-4b17-bd2a-b1dbe6dd69e1')
    return ISCPSecureExchange3
def _define_ISCPSecureExchange3():
    ISCPSecureExchange3 = win32more.Media.DeviceManager.ISCPSecureExchange3_head
    ISCPSecureExchange3.TransferContainerDataOnClearChannel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.DeviceManager.IMDSPDevice_head,POINTER(Byte),UInt32,win32more.Media.DeviceManager.IWMDMProgress3_head,POINTER(UInt32), use_last_error=False)(7, 'TransferContainerDataOnClearChannel', ((1, 'pDevice'),(1, 'pData'),(1, 'dwSize'),(1, 'pProgressCallback'),(1, 'pfuReadyFlags'),)))
    ISCPSecureExchange3.GetObjectDataOnClearChannel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.DeviceManager.IMDSPDevice_head,POINTER(Byte),POINTER(UInt32), use_last_error=False)(8, 'GetObjectDataOnClearChannel', ((1, 'pDevice'),(1, 'pData'),(1, 'pdwSize'),)))
    ISCPSecureExchange3.TransferCompleteForDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.DeviceManager.IMDSPDevice_head, use_last_error=False)(9, 'TransferCompleteForDevice', ((1, 'pDevice'),)))
    win32more.Media.DeviceManager.ISCPSecureExchange2
    return ISCPSecureExchange3
def _define_ISCPSession_head():
    class ISCPSession(win32more.System.Com.IUnknown_head):
        Guid = Guid('88a3e6ed-eee4-4619-bbb3-fd4fb62715d1')
    return ISCPSession
def _define_ISCPSession():
    ISCPSession = win32more.Media.DeviceManager.ISCPSession_head
    ISCPSession.BeginSession = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.DeviceManager.IMDSPDevice_head,POINTER(Byte),UInt32, use_last_error=False)(3, 'BeginSession', ((1, 'pIDevice'),(1, 'pCtx'),(1, 'dwSizeCtx'),)))
    ISCPSession.EndSession = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),UInt32, use_last_error=False)(4, 'EndSession', ((1, 'pCtx'),(1, 'dwSizeCtx'),)))
    ISCPSession.GetSecureQuery = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.DeviceManager.ISCPSecureQuery_head), use_last_error=False)(5, 'GetSecureQuery', ((1, 'ppSecureQuery'),)))
    win32more.System.Com.IUnknown
    return ISCPSession
def _define_ISCPSecureQuery3_head():
    class ISCPSecureQuery3(win32more.Media.DeviceManager.ISCPSecureQuery2_head):
        Guid = Guid('b7edd1a2-4dab-484b-b3c5-ad39b8b4c0b1')
    return ISCPSecureQuery3
def _define_ISCPSecureQuery3():
    ISCPSecureQuery3 = win32more.Media.DeviceManager.ISCPSecureQuery3_head
    ISCPSecureQuery3.GetRightsOnClearChannel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),UInt32,POINTER(Byte),UInt32,win32more.Media.DeviceManager.IMDSPStorageGlobals_head,win32more.Media.DeviceManager.IWMDMProgress3_head,POINTER(POINTER(win32more.Media.DeviceManager.WMDMRIGHTS_head)),POINTER(UInt32), use_last_error=False)(8, 'GetRightsOnClearChannel', ((1, 'pData'),(1, 'dwSize'),(1, 'pbSPSessionKey'),(1, 'dwSessionKeyLen'),(1, 'pStgGlobals'),(1, 'pProgressCallback'),(1, 'ppRights'),(1, 'pnRightsCount'),)))
    ISCPSecureQuery3.MakeDecisionOnClearChannel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Byte),UInt32,UInt32,POINTER(Byte),UInt32,win32more.Media.DeviceManager.IMDSPStorageGlobals_head,win32more.Media.DeviceManager.IWMDMProgress3_head,POINTER(Byte),UInt32,POINTER(Byte),UInt32,POINTER(win32more.Foundation.PWSTR),POINTER(UInt32),POINTER(UInt32),POINTER(UInt64),win32more.System.Com.IUnknown_head,POINTER(win32more.Media.DeviceManager.ISCPSecureExchange_head), use_last_error=False)(9, 'MakeDecisionOnClearChannel', ((1, 'fuFlags'),(1, 'pData'),(1, 'dwSize'),(1, 'dwAppSec'),(1, 'pbSPSessionKey'),(1, 'dwSessionKeyLen'),(1, 'pStorageGlobals'),(1, 'pProgressCallback'),(1, 'pAppCertApp'),(1, 'dwAppCertAppLen'),(1, 'pAppCertSP'),(1, 'dwAppCertSPLen'),(1, 'pszRevocationURL'),(1, 'pdwRevocationURLLen'),(1, 'pdwRevocationBitFlag'),(1, 'pqwFileSize'),(1, 'pUnknown'),(1, 'ppExchange'),)))
    win32more.Media.DeviceManager.ISCPSecureQuery2
    return ISCPSecureQuery3
def _define_IComponentAuthenticate_head():
    class IComponentAuthenticate(win32more.System.Com.IUnknown_head):
        Guid = Guid('a9889c00-6d2b-11d3-8496-00c04f79dbc0')
    return IComponentAuthenticate
def _define_IComponentAuthenticate():
    IComponentAuthenticate = win32more.Media.DeviceManager.IComponentAuthenticate_head
    IComponentAuthenticate.SACAuth = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(Byte),UInt32,POINTER(c_char_p_no),POINTER(UInt32), use_last_error=False)(3, 'SACAuth', ((1, 'dwProtocolID'),(1, 'dwPass'),(1, 'pbDataIn'),(1, 'dwDataInLen'),(1, 'ppbDataOut'),(1, 'pdwDataOutLen'),)))
    IComponentAuthenticate.SACGetProtocols = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(UInt32)),POINTER(UInt32), use_last_error=False)(4, 'SACGetProtocols', ((1, 'ppdwProtocols'),(1, 'pdwProtocolCount'),)))
    win32more.System.Com.IUnknown
    return IComponentAuthenticate
WMDMLogger = Guid('110a3202-5a79-11d3-8d78-444553540000')
def _define_IWMDMLogger_head():
    class IWMDMLogger(win32more.System.Com.IUnknown_head):
        Guid = Guid('110a3200-5a79-11d3-8d78-444553540000')
    return IWMDMLogger
def _define_IWMDMLogger():
    IWMDMLogger = win32more.Media.DeviceManager.IWMDMLogger_head
    IWMDMLogger.IsEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(3, 'IsEnabled', ((1, 'pfEnabled'),)))
    IWMDMLogger.Enable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(4, 'Enable', ((1, 'fEnable'),)))
    IWMDMLogger.GetLogFileName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSTR,UInt32, use_last_error=False)(5, 'GetLogFileName', ((1, 'pszFilename'),(1, 'nMaxChars'),)))
    IWMDMLogger.SetLogFileName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSTR, use_last_error=False)(6, 'SetLogFileName', ((1, 'pszFilename'),)))
    IWMDMLogger.LogString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(7, 'LogString', ((1, 'dwFlags'),(1, 'pszSrcName'),(1, 'pszLog'),)))
    IWMDMLogger.LogDword = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32, use_last_error=False)(8, 'LogDword', ((1, 'dwFlags'),(1, 'pszSrcName'),(1, 'pszLogFormat'),(1, 'dwLog'),)))
    IWMDMLogger.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(9, 'Reset', ()))
    IWMDMLogger.GetSizeParams = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(10, 'GetSizeParams', ((1, 'pdwMaxSize'),(1, 'pdwShrinkToSize'),)))
    IWMDMLogger.SetSizeParams = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(11, 'SetSizeParams', ((1, 'dwMaxSize'),(1, 'dwShrinkToSize'),)))
    win32more.System.Com.IUnknown
    return IWMDMLogger
def _define_MTP_COMMAND_DATA_IN_head():
    class MTP_COMMAND_DATA_IN(Structure):
        pass
    return MTP_COMMAND_DATA_IN
def _define_MTP_COMMAND_DATA_IN():
    MTP_COMMAND_DATA_IN = win32more.Media.DeviceManager.MTP_COMMAND_DATA_IN_head
    MTP_COMMAND_DATA_IN._pack_ = 1
    MTP_COMMAND_DATA_IN._fields_ = [
        ("OpCode", UInt16),
        ("NumParams", UInt32),
        ("Params", UInt32 * 5),
        ("NextPhase", UInt32),
        ("CommandWriteDataSize", UInt32),
        ("CommandWriteData", Byte * 0),
    ]
    return MTP_COMMAND_DATA_IN
def _define_MTP_COMMAND_DATA_OUT_head():
    class MTP_COMMAND_DATA_OUT(Structure):
        pass
    return MTP_COMMAND_DATA_OUT
def _define_MTP_COMMAND_DATA_OUT():
    MTP_COMMAND_DATA_OUT = win32more.Media.DeviceManager.MTP_COMMAND_DATA_OUT_head
    MTP_COMMAND_DATA_OUT._pack_ = 1
    MTP_COMMAND_DATA_OUT._fields_ = [
        ("ResponseCode", UInt16),
        ("NumParams", UInt32),
        ("Params", UInt32 * 5),
        ("CommandReadDataSize", UInt32),
        ("CommandReadData", Byte * 0),
    ]
    return MTP_COMMAND_DATA_OUT
__all__ = [
    "IOCTL_MTP_CUSTOM_COMMAND",
    "MTP_NEXTPHASE_READ_DATA",
    "MTP_NEXTPHASE_WRITE_DATA",
    "MTP_NEXTPHASE_NO_DATA",
    "RSA_KEY_LEN",
    "SAC_SESSION_KEYLEN",
    "SAC_PROTOCOL_WMDM",
    "SAC_PROTOCOL_V1",
    "SAC_CERT_X509",
    "SAC_CERT_V1",
    "WMDM_DEVICE_PROTOCOL_MTP",
    "WMDM_DEVICE_PROTOCOL_RAPI",
    "WMDM_DEVICE_PROTOCOL_MSC",
    "WMDM_SERVICE_PROVIDER_VENDOR_MICROSOFT",
    "WMDMID_LENGTH",
    "WMDM_MAC_LENGTH",
    "WMDM_S_NOT_ALL_PROPERTIES_APPLIED",
    "WMDM_S_NOT_ALL_PROPERTIES_RETRIEVED",
    "WMDM_E_BUSY",
    "WMDM_E_INTERFACEDEAD",
    "WMDM_E_INVALIDTYPE",
    "WMDM_E_PROCESSFAILED",
    "WMDM_E_NOTSUPPORTED",
    "WMDM_E_NOTCERTIFIED",
    "WMDM_E_NORIGHTS",
    "WMDM_E_CALL_OUT_OF_SEQUENCE",
    "WMDM_E_BUFFERTOOSMALL",
    "WMDM_E_MOREDATA",
    "WMDM_E_MAC_CHECK_FAILED",
    "WMDM_E_USER_CANCELLED",
    "WMDM_E_SDMI_TRIGGER",
    "WMDM_E_SDMI_NOMORECOPIES",
    "WMDM_E_REVOKED",
    "WMDM_E_LICENSE_NOTEXIST",
    "WMDM_E_INCORRECT_APPSEC",
    "WMDM_E_INCORRECT_RIGHTS",
    "WMDM_E_LICENSE_EXPIRED",
    "WMDM_E_CANTOPEN_PMSN_SERVICE_PIPE",
    "WMDM_E_TOO_MANY_SESSIONS",
    "WMDM_WMDM_REVOKED",
    "WMDM_APP_REVOKED",
    "WMDM_SP_REVOKED",
    "WMDM_SCP_REVOKED",
    "WMDM_GET_FORMAT_SUPPORT_AUDIO",
    "WMDM_GET_FORMAT_SUPPORT_VIDEO",
    "WMDM_GET_FORMAT_SUPPORT_FILE",
    "WMDM_RIGHTS_PLAYBACKCOUNT",
    "WMDM_RIGHTS_EXPIRATIONDATE",
    "WMDM_RIGHTS_GROUPID",
    "WMDM_RIGHTS_FREESERIALIDS",
    "WMDM_RIGHTS_NAMEDSERIALIDS",
    "WMDM_DEVICE_TYPE_PLAYBACK",
    "WMDM_DEVICE_TYPE_RECORD",
    "WMDM_DEVICE_TYPE_DECODE",
    "WMDM_DEVICE_TYPE_ENCODE",
    "WMDM_DEVICE_TYPE_STORAGE",
    "WMDM_DEVICE_TYPE_VIRTUAL",
    "WMDM_DEVICE_TYPE_SDMI",
    "WMDM_DEVICE_TYPE_NONSDMI",
    "WMDM_DEVICE_TYPE_NONREENTRANT",
    "WMDM_DEVICE_TYPE_FILELISTRESYNC",
    "WMDM_DEVICE_TYPE_VIEW_PREF_METADATAVIEW",
    "WMDM_POWER_CAP_BATTERY",
    "WMDM_POWER_CAP_EXTERNAL",
    "WMDM_POWER_IS_BATTERY",
    "WMDM_POWER_IS_EXTERNAL",
    "WMDM_POWER_PERCENT_AVAILABLE",
    "WMDM_STATUS_READY",
    "WMDM_STATUS_BUSY",
    "WMDM_STATUS_DEVICE_NOTPRESENT",
    "WMDM_STATUS_DEVICECONTROL_PLAYING",
    "WMDM_STATUS_DEVICECONTROL_RECORDING",
    "WMDM_STATUS_DEVICECONTROL_PAUSED",
    "WMDM_STATUS_DEVICECONTROL_REMOTE",
    "WMDM_STATUS_DEVICECONTROL_STREAM",
    "WMDM_STATUS_STORAGE_NOTPRESENT",
    "WMDM_STATUS_STORAGE_INITIALIZING",
    "WMDM_STATUS_STORAGE_BROKEN",
    "WMDM_STATUS_STORAGE_NOTSUPPORTED",
    "WMDM_STATUS_STORAGE_UNFORMATTED",
    "WMDM_STATUS_STORAGECONTROL_INSERTING",
    "WMDM_STATUS_STORAGECONTROL_DELETING",
    "WMDM_STATUS_STORAGECONTROL_APPENDING",
    "WMDM_STATUS_STORAGECONTROL_MOVING",
    "WMDM_STATUS_STORAGECONTROL_READING",
    "WMDM_DEVICECAP_CANPLAY",
    "WMDM_DEVICECAP_CANSTREAMPLAY",
    "WMDM_DEVICECAP_CANRECORD",
    "WMDM_DEVICECAP_CANSTREAMRECORD",
    "WMDM_DEVICECAP_CANPAUSE",
    "WMDM_DEVICECAP_CANRESUME",
    "WMDM_DEVICECAP_CANSTOP",
    "WMDM_DEVICECAP_CANSEEK",
    "WMDM_DEVICECAP_HASSECURECLOCK",
    "WMDM_SEEK_REMOTECONTROL",
    "WMDM_SEEK_STREAMINGAUDIO",
    "WMDM_STORAGE_ATTR_FILESYSTEM",
    "WMDM_STORAGE_ATTR_REMOVABLE",
    "WMDM_STORAGE_ATTR_NONREMOVABLE",
    "WMDM_FILE_ATTR_FOLDER",
    "WMDM_FILE_ATTR_LINK",
    "WMDM_FILE_ATTR_FILE",
    "WMDM_FILE_ATTR_VIDEO",
    "WMDM_STORAGE_ATTR_CANEDITMETADATA",
    "WMDM_STORAGE_ATTR_FOLDERS",
    "WMDM_FILE_ATTR_AUDIO",
    "WMDM_FILE_ATTR_DATA",
    "WMDM_FILE_ATTR_CANPLAY",
    "WMDM_FILE_ATTR_CANDELETE",
    "WMDM_FILE_ATTR_CANMOVE",
    "WMDM_FILE_ATTR_CANRENAME",
    "WMDM_FILE_ATTR_CANREAD",
    "WMDM_FILE_ATTR_MUSIC",
    "WMDM_FILE_CREATE_OVERWRITE",
    "WMDM_FILE_ATTR_AUDIOBOOK",
    "WMDM_FILE_ATTR_HIDDEN",
    "WMDM_FILE_ATTR_SYSTEM",
    "WMDM_FILE_ATTR_READONLY",
    "WMDM_STORAGE_ATTR_HAS_FOLDERS",
    "WMDM_STORAGE_ATTR_HAS_FILES",
    "WMDM_STORAGE_IS_DEFAULT",
    "WMDM_STORAGE_CONTAINS_DEFAULT",
    "WMDM_STORAGE_ATTR_VIRTUAL",
    "WMDM_STORAGECAP_FOLDERSINROOT",
    "WMDM_STORAGECAP_FILESINROOT",
    "WMDM_STORAGECAP_FOLDERSINFOLDERS",
    "WMDM_STORAGECAP_FILESINFOLDERS",
    "WMDM_STORAGECAP_FOLDERLIMITEXISTS",
    "WMDM_STORAGECAP_FILELIMITEXISTS",
    "WMDM_STORAGECAP_NOT_INITIALIZABLE",
    "WMDM_MODE_BLOCK",
    "WMDM_MODE_THREAD",
    "WMDM_CONTENT_FILE",
    "WMDM_CONTENT_FOLDER",
    "WMDM_CONTENT_OPERATIONINTERFACE",
    "WMDM_MODE_QUERY",
    "WMDM_MODE_PROGRESS",
    "WMDM_MODE_TRANSFER_PROTECTED",
    "WMDM_MODE_TRANSFER_UNPROTECTED",
    "WMDM_STORAGECONTROL_INSERTBEFORE",
    "WMDM_STORAGECONTROL_INSERTAFTER",
    "WMDM_STORAGECONTROL_INSERTINTO",
    "WMDM_MODE_RECURSIVE",
    "WMDM_RIGHTS_PLAY_ON_PC",
    "WMDM_RIGHTS_COPY_TO_NON_SDMI_DEVICE",
    "WMDM_RIGHTS_COPY_TO_CD",
    "WMDM_RIGHTS_COPY_TO_SDMI_DEVICE",
    "WMDM_SEEK_BEGIN",
    "WMDM_SEEK_CURRENT",
    "WMDM_SEEK_END",
    "DO_NOT_VIRTUALIZE_STORAGES_AS_DEVICES",
    "ALLOW_OUTOFBAND_NOTIFICATION",
    "MDSP_READ",
    "MDSP_WRITE",
    "MDSP_SEEK_BOF",
    "MDSP_SEEK_CUR",
    "MDSP_SEEK_EOF",
    "WMDM_SCP_EXAMINE_EXTENSION",
    "WMDM_SCP_EXAMINE_DATA",
    "WMDM_SCP_DECIDE_DATA",
    "WMDM_SCP_PROTECTED_OUTPUT",
    "WMDM_SCP_UNPROTECTED_OUTPUT",
    "WMDM_SCP_RIGHTS_DATA",
    "WMDM_SCP_TRANSFER_OBJECTDATA",
    "WMDM_SCP_NO_MORE_CHANGES",
    "WMDM_SCP_DRMINFO_NOT_DRMPROTECTED",
    "WMDM_SCP_DRMINFO_V1HEADER",
    "WMDM_SCP_DRMINFO_V2HEADER",
    "SCP_EVENTID_ACQSECURECLOCK",
    "SCP_EVENTID_NEEDTOINDIV",
    "SCP_EVENTID_DRMINFO",
    "SCP_PARAMID_DRMVERSION",
    "SAC_MAC_LEN",
    "WMDM_LOG_SEV_INFO",
    "WMDM_LOG_SEV_WARN",
    "WMDM_LOG_SEV_ERROR",
    "WMDM_LOG_NOTIMESTAMP",
    "g_wszWMDMFileName",
    "g_wszWMDMFormatCode",
    "g_wszWMDMLastModifiedDate",
    "g_wszWMDMFileCreationDate",
    "g_wszWMDMFileSize",
    "g_wszWMDMFileAttributes",
    "g_wszAudioWAVECodec",
    "g_wszVideoFourCCCodec",
    "g_wszWMDMTitle",
    "g_wszWMDMAuthor",
    "g_wszWMDMDescription",
    "g_wszWMDMIsProtected",
    "g_wszWMDMAlbumTitle",
    "g_wszWMDMAlbumArtist",
    "g_wszWMDMTrack",
    "g_wszWMDMGenre",
    "g_wszWMDMTrackMood",
    "g_wszWMDMAlbumCoverFormat",
    "g_wszWMDMAlbumCoverSize",
    "g_wszWMDMAlbumCoverHeight",
    "g_wszWMDMAlbumCoverWidth",
    "g_wszWMDMAlbumCoverDuration",
    "g_wszWMDMAlbumCoverData",
    "g_wszWMDMYear",
    "g_wszWMDMComposer",
    "g_wszWMDMCodec",
    "g_wszWMDMDRMId",
    "g_wszWMDMBitrate",
    "g_wszWMDMBitRateType",
    "g_wszWMDMSampleRate",
    "g_wszWMDMNumChannels",
    "g_wszWMDMBlockAlignment",
    "g_wszWMDMAudioBitDepth",
    "g_wszWMDMTotalBitrate",
    "g_wszWMDMVideoBitrate",
    "g_wszWMDMFrameRate",
    "g_wszWMDMScanType",
    "g_wszWMDMKeyFrameDistance",
    "g_wszWMDMBufferSize",
    "g_wszWMDMQualitySetting",
    "g_wszWMDMEncodingProfile",
    "g_wszWMDMDuration",
    "g_wszWMDMAlbumArt",
    "g_wszWMDMBuyNow",
    "g_wszWMDMNonConsumable",
    "g_wszWMDMediaClassPrimaryID",
    "g_wszWMDMMediaClassSecondaryID",
    "g_wszWMDMUserEffectiveRating",
    "g_wszWMDMUserRating",
    "g_wszWMDMUserRatingOnDevice",
    "g_wszWMDMPlayCount",
    "g_wszWMDMDevicePlayCount",
    "g_wszWMDMAuthorDate",
    "g_wszWMDMUserLastPlayTime",
    "g_wszWMDMSubTitle",
    "g_wszWMDMSubTitleDescription",
    "g_wszWMDMMediaCredits",
    "g_wszWMDMMediaStationName",
    "g_wszWMDMMediaOriginalChannel",
    "g_wszWMDMMediaOriginalBroadcastDateTime",
    "g_wszWMDMProviderCopyright",
    "g_wszWMDMSyncID",
    "g_wszWMDMPersistentUniqueID",
    "g_wszWMDMWidth",
    "g_wszWMDMHeight",
    "g_wszWMDMSyncTime",
    "g_wszWMDMParentalRating",
    "g_wszWMDMMetaGenre",
    "g_wszWMDMIsRepeat",
    "g_wszWMDMSupportedDeviceProperties",
    "g_wszWMDMDeviceFriendlyName",
    "g_wszWMDMFormatsSupported",
    "g_wszWMDMFormatsSupportedAreOrdered",
    "g_wszWMDMSyncRelationshipID",
    "g_wszWMDMDeviceModelName",
    "g_wszWMDMDeviceFirmwareVersion",
    "g_wszWMDMDeviceVendorExtension",
    "g_wszWMDMDeviceProtocol",
    "g_wszWMDMDeviceServiceProviderVendor",
    "g_wszWMDMDeviceRevocationInfo",
    "g_wszWMDMCollectionID",
    "g_wszWMDMOwner",
    "g_wszWMDMEditor",
    "g_wszWMDMWebmaster",
    "g_wszWMDMSourceURL",
    "g_wszWMDMDestinationURL",
    "g_wszWMDMCategory",
    "g_wszWMDMTimeBookmark",
    "g_wszWMDMObjectBookmark",
    "g_wszWMDMByteBookmark",
    "g_wszWMDMDataOffset",
    "g_wszWMDMDataLength",
    "g_wszWMDMDataUnits",
    "g_wszWMDMTimeToLive",
    "g_wszWMDMMediaGuid",
    "g_wszWPDPassthroughPropertyValues",
    "EVENT_WMDM_CONTENT_TRANSFER",
    "MTP_COMMAND_MAX_PARAMS",
    "MTP_RESPONSE_MAX_PARAMS",
    "MTP_RESPONSE_OK",
    "__MACINFO",
    "MediaDevMgrClassFactory",
    "MediaDevMgr",
    "WMDMDevice",
    "WMDMStorage",
    "WMDMStorageGlobal",
    "WMDMDeviceEnum",
    "WMDMStorageEnum",
    "WMDM_TAG_DATATYPE",
    "WMDM_TYPE_DWORD",
    "WMDM_TYPE_STRING",
    "WMDM_TYPE_BINARY",
    "WMDM_TYPE_BOOL",
    "WMDM_TYPE_QWORD",
    "WMDM_TYPE_WORD",
    "WMDM_TYPE_GUID",
    "WMDM_TYPE_DATE",
    "WMDM_SESSION_TYPE",
    "WMDM_SESSION_NONE",
    "WMDM_SESSION_TRANSFER_TO_DEVICE",
    "WMDM_SESSION_TRANSFER_FROM_DEVICE",
    "WMDM_SESSION_DELETE",
    "WMDM_SESSION_CUSTOM",
    "_WAVEFORMATEX",
    "_BITMAPINFOHEADER",
    "_VIDEOINFOHEADER",
    "WMFILECAPABILITIES",
    "OPAQUECOMMAND",
    "WMDMID",
    "WMDMDATETIME",
    "WMDMRIGHTS",
    "WMDMMetadataView",
    "WMDM_STORAGE_ENUM_MODE",
    "ENUM_MODE_RAW",
    "ENUM_MODE_USE_DEVICE_PREF",
    "ENUM_MODE_METADATA_VIEWS",
    "WMDM_FORMATCODE",
    "WMDM_FORMATCODE_NOTUSED",
    "WMDM_FORMATCODE_ALLIMAGES",
    "WMDM_FORMATCODE_UNDEFINED",
    "WMDM_FORMATCODE_ASSOCIATION",
    "WMDM_FORMATCODE_SCRIPT",
    "WMDM_FORMATCODE_EXECUTABLE",
    "WMDM_FORMATCODE_TEXT",
    "WMDM_FORMATCODE_HTML",
    "WMDM_FORMATCODE_DPOF",
    "WMDM_FORMATCODE_AIFF",
    "WMDM_FORMATCODE_WAVE",
    "WMDM_FORMATCODE_MP3",
    "WMDM_FORMATCODE_AVI",
    "WMDM_FORMATCODE_MPEG",
    "WMDM_FORMATCODE_ASF",
    "WMDM_FORMATCODE_RESERVED_FIRST",
    "WMDM_FORMATCODE_RESERVED_LAST",
    "WMDM_FORMATCODE_IMAGE_UNDEFINED",
    "WMDM_FORMATCODE_IMAGE_EXIF",
    "WMDM_FORMATCODE_IMAGE_TIFFEP",
    "WMDM_FORMATCODE_IMAGE_FLASHPIX",
    "WMDM_FORMATCODE_IMAGE_BMP",
    "WMDM_FORMATCODE_IMAGE_CIFF",
    "WMDM_FORMATCODE_IMAGE_GIF",
    "WMDM_FORMATCODE_IMAGE_JFIF",
    "WMDM_FORMATCODE_IMAGE_PCD",
    "WMDM_FORMATCODE_IMAGE_PICT",
    "WMDM_FORMATCODE_IMAGE_PNG",
    "WMDM_FORMATCODE_IMAGE_TIFF",
    "WMDM_FORMATCODE_IMAGE_TIFFIT",
    "WMDM_FORMATCODE_IMAGE_JP2",
    "WMDM_FORMATCODE_IMAGE_JPX",
    "WMDM_FORMATCODE_IMAGE_RESERVED_FIRST",
    "WMDM_FORMATCODE_IMAGE_RESERVED_LAST",
    "WMDM_FORMATCODE_UNDEFINEDFIRMWARE",
    "WMDM_FORMATCODE_WBMP",
    "WMDM_FORMATCODE_JPEGXR",
    "WMDM_FORMATCODE_WINDOWSIMAGEFORMAT",
    "WMDM_FORMATCODE_UNDEFINEDAUDIO",
    "WMDM_FORMATCODE_WMA",
    "WMDM_FORMATCODE_OGG",
    "WMDM_FORMATCODE_AAC",
    "WMDM_FORMATCODE_AUDIBLE",
    "WMDM_FORMATCODE_FLAC",
    "WMDM_FORMATCODE_QCELP",
    "WMDM_FORMATCODE_AMR",
    "WMDM_FORMATCODE_UNDEFINEDVIDEO",
    "WMDM_FORMATCODE_WMV",
    "WMDM_FORMATCODE_MP4",
    "WMDM_FORMATCODE_MP2",
    "WMDM_FORMATCODE_3GP",
    "WMDM_FORMATCODE_3G2",
    "WMDM_FORMATCODE_AVCHD",
    "WMDM_FORMATCODE_ATSCTS",
    "WMDM_FORMATCODE_DVBTS",
    "WMDM_FORMATCODE_MKV",
    "WMDM_FORMATCODE_MKA",
    "WMDM_FORMATCODE_MK3D",
    "WMDM_FORMATCODE_UNDEFINEDCOLLECTION",
    "WMDM_FORMATCODE_ABSTRACTMULTIMEDIAALBUM",
    "WMDM_FORMATCODE_ABSTRACTIMAGEALBUM",
    "WMDM_FORMATCODE_ABSTRACTAUDIOALBUM",
    "WMDM_FORMATCODE_ABSTRACTVIDEOALBUM",
    "WMDM_FORMATCODE_ABSTRACTAUDIOVIDEOPLAYLIST",
    "WMDM_FORMATCODE_ABSTRACTCONTACTGROUP",
    "WMDM_FORMATCODE_ABSTRACTMESSAGEFOLDER",
    "WMDM_FORMATCODE_ABSTRACTCHAPTEREDPRODUCTION",
    "WMDM_FORMATCODE_MEDIA_CAST",
    "WMDM_FORMATCODE_WPLPLAYLIST",
    "WMDM_FORMATCODE_M3UPLAYLIST",
    "WMDM_FORMATCODE_MPLPLAYLIST",
    "WMDM_FORMATCODE_ASXPLAYLIST",
    "WMDM_FORMATCODE_PLSPLAYLIST",
    "WMDM_FORMATCODE_UNDEFINEDDOCUMENT",
    "WMDM_FORMATCODE_ABSTRACTDOCUMENT",
    "WMDM_FORMATCODE_XMLDOCUMENT",
    "WMDM_FORMATCODE_MICROSOFTWORDDOCUMENT",
    "WMDM_FORMATCODE_MHTCOMPILEDHTMLDOCUMENT",
    "WMDM_FORMATCODE_MICROSOFTEXCELSPREADSHEET",
    "WMDM_FORMATCODE_MICROSOFTPOWERPOINTDOCUMENT",
    "WMDM_FORMATCODE_UNDEFINEDMESSAGE",
    "WMDM_FORMATCODE_ABSTRACTMESSAGE",
    "WMDM_FORMATCODE_UNDEFINEDCONTACT",
    "WMDM_FORMATCODE_ABSTRACTCONTACT",
    "WMDM_FORMATCODE_VCARD2",
    "WMDM_FORMATCODE_VCARD3",
    "WMDM_FORMATCODE_UNDEFINEDCALENDARITEM",
    "WMDM_FORMATCODE_ABSTRACTCALENDARITEM",
    "WMDM_FORMATCODE_VCALENDAR1",
    "WMDM_FORMATCODE_VCALENDAR2",
    "WMDM_FORMATCODE_UNDEFINEDWINDOWSEXECUTABLE",
    "WMDM_FORMATCODE_M4A",
    "WMDM_FORMATCODE_3GPA",
    "WMDM_FORMATCODE_3G2A",
    "WMDM_FORMATCODE_SECTION",
    "WMDM_ENUM_PROP_VALID_VALUES_FORM",
    "WMDM_ENUM_PROP_VALID_VALUES_ANY",
    "WMDM_ENUM_PROP_VALID_VALUES_RANGE",
    "WMDM_ENUM_PROP_VALID_VALUES_ENUM",
    "WMDM_PROP_VALUES_RANGE",
    "WMDM_PROP_VALUES_ENUM",
    "WMDM_PROP_DESC",
    "WMDM_PROP_CONFIG",
    "WMDM_FORMAT_CAPABILITY",
    "WMDM_FIND_SCOPE",
    "WMDM_FIND_SCOPE_GLOBAL",
    "WMDM_FIND_SCOPE_IMMEDIATE_CHILDREN",
    "WMDMMessage",
    "WMDM_MSG_DEVICE_ARRIVAL",
    "WMDM_MSG_DEVICE_REMOVAL",
    "WMDM_MSG_MEDIA_ARRIVAL",
    "WMDM_MSG_MEDIA_REMOVAL",
    "IWMDMMetaData",
    "IWMDeviceManager",
    "IWMDeviceManager2",
    "IWMDeviceManager3",
    "IWMDMStorageGlobals",
    "IWMDMStorage",
    "IWMDMStorage2",
    "IWMDMStorage3",
    "IWMDMStorage4",
    "IWMDMOperation",
    "IWMDMOperation2",
    "IWMDMOperation3",
    "IWMDMProgress",
    "IWMDMProgress2",
    "IWMDMProgress3",
    "IWMDMDevice",
    "IWMDMDevice2",
    "IWMDMDevice3",
    "IWMDMDeviceSession",
    "IWMDMEnumDevice",
    "IWMDMDeviceControl",
    "IWMDMEnumStorage",
    "IWMDMStorageControl",
    "IWMDMStorageControl2",
    "IWMDMStorageControl3",
    "IWMDMObjectInfo",
    "IWMDMRevoked",
    "IWMDMNotification",
    "WMDMDetermineMaxPropStringLen",
    "IMDServiceProvider",
    "IMDServiceProvider2",
    "IMDServiceProvider3",
    "IMDSPEnumDevice",
    "IMDSPDevice",
    "IMDSPDevice2",
    "IMDSPDevice3",
    "IMDSPDeviceControl",
    "IMDSPEnumStorage",
    "IMDSPStorage",
    "IMDSPStorage2",
    "IMDSPStorage3",
    "IMDSPStorage4",
    "IMDSPStorageGlobals",
    "IMDSPObjectInfo",
    "IMDSPObject",
    "IMDSPObject2",
    "IMDSPDirectTransfer",
    "IMDSPRevoked",
    "ISCPSecureAuthenticate",
    "ISCPSecureAuthenticate2",
    "ISCPSecureQuery",
    "ISCPSecureQuery2",
    "ISCPSecureExchange",
    "ISCPSecureExchange2",
    "ISCPSecureExchange3",
    "ISCPSession",
    "ISCPSecureQuery3",
    "IComponentAuthenticate",
    "WMDMLogger",
    "IWMDMLogger",
    "MTP_COMMAND_DATA_IN",
    "MTP_COMMAND_DATA_OUT",
]
