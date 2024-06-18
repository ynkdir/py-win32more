from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Media.Audio
import win32more.Windows.Win32.Media.DeviceManager
import win32more.Windows.Win32.Media.MediaFoundation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Com.StructuredStorage
import win32more.Windows.Win32.System.Ole
IOCTL_MTP_CUSTOM_COMMAND: UInt32 = 827348045
MTP_NEXTPHASE_READ_DATA: UInt32 = 1
MTP_NEXTPHASE_WRITE_DATA: UInt32 = 2
MTP_NEXTPHASE_NO_DATA: UInt32 = 3
RSA_KEY_LEN: UInt32 = 64
SAC_SESSION_KEYLEN: UInt32 = 8
SAC_PROTOCOL_WMDM: UInt32 = 1
SAC_PROTOCOL_V1: UInt32 = 2
SAC_CERT_X509: UInt32 = 1
SAC_CERT_V1: UInt32 = 2
WMDM_DEVICE_PROTOCOL_MTP: Guid = Guid('{979e54e5-0afc-4604-8d93-dc798a4bcf45}')
WMDM_DEVICE_PROTOCOL_RAPI: Guid = Guid('{2a11ed91-8c8f-41e4-82d1-8386e003561c}')
WMDM_DEVICE_PROTOCOL_MSC: Guid = Guid('{a4d2c26c-a881-44bb-bd5d-1f703c71f7a9}')
WMDM_SERVICE_PROVIDER_VENDOR_MICROSOFT: Guid = Guid('{7de8686d-78ee-43ea-a496-c625ac91cc5d}')
WMDMID_LENGTH: UInt32 = 128
WMDM_MAC_LENGTH: UInt32 = 8
WMDM_S_NOT_ALL_PROPERTIES_APPLIED: Int32 = 282625
WMDM_S_NOT_ALL_PROPERTIES_RETRIEVED: Int32 = 282626
WMDM_E_BUSY: Int32 = -2147201024
WMDM_E_INTERFACEDEAD: Int32 = -2147201023
WMDM_E_INVALIDTYPE: Int32 = -2147201022
WMDM_E_PROCESSFAILED: Int32 = -2147201021
WMDM_E_NOTSUPPORTED: Int32 = -2147201020
WMDM_E_NOTCERTIFIED: Int32 = -2147201019
WMDM_E_NORIGHTS: Int32 = -2147201018
WMDM_E_CALL_OUT_OF_SEQUENCE: Int32 = -2147201017
WMDM_E_BUFFERTOOSMALL: Int32 = -2147201016
WMDM_E_MOREDATA: Int32 = -2147201015
WMDM_E_MAC_CHECK_FAILED: Int32 = -2147201014
WMDM_E_USER_CANCELLED: Int32 = -2147201013
WMDM_E_SDMI_TRIGGER: Int32 = -2147201012
WMDM_E_SDMI_NOMORECOPIES: Int32 = -2147201011
WMDM_E_REVOKED: Int32 = -2147201010
WMDM_E_LICENSE_NOTEXIST: Int32 = -2147201009
WMDM_E_INCORRECT_APPSEC: Int32 = -2147201008
WMDM_E_INCORRECT_RIGHTS: Int32 = -2147201007
WMDM_E_LICENSE_EXPIRED: Int32 = -2147201006
WMDM_E_CANTOPEN_PMSN_SERVICE_PIPE: Int32 = -2147201005
WMDM_E_TOO_MANY_SESSIONS: Int32 = -2147201005
WMDM_WMDM_REVOKED: UInt32 = 1
WMDM_APP_REVOKED: UInt32 = 2
WMDM_SP_REVOKED: UInt32 = 4
WMDM_SCP_REVOKED: UInt32 = 8
WMDM_GET_FORMAT_SUPPORT_AUDIO: UInt32 = 1
WMDM_GET_FORMAT_SUPPORT_VIDEO: UInt32 = 2
WMDM_GET_FORMAT_SUPPORT_FILE: UInt32 = 4
WMDM_RIGHTS_PLAYBACKCOUNT: UInt32 = 1
WMDM_RIGHTS_EXPIRATIONDATE: UInt32 = 2
WMDM_RIGHTS_GROUPID: UInt32 = 4
WMDM_RIGHTS_FREESERIALIDS: UInt32 = 8
WMDM_RIGHTS_NAMEDSERIALIDS: UInt32 = 16
WMDM_DEVICE_TYPE_PLAYBACK: UInt32 = 1
WMDM_DEVICE_TYPE_RECORD: UInt32 = 2
WMDM_DEVICE_TYPE_DECODE: UInt32 = 4
WMDM_DEVICE_TYPE_ENCODE: UInt32 = 8
WMDM_DEVICE_TYPE_STORAGE: UInt32 = 16
WMDM_DEVICE_TYPE_VIRTUAL: UInt32 = 32
WMDM_DEVICE_TYPE_SDMI: UInt32 = 64
WMDM_DEVICE_TYPE_NONSDMI: UInt32 = 128
WMDM_DEVICE_TYPE_NONREENTRANT: UInt32 = 256
WMDM_DEVICE_TYPE_FILELISTRESYNC: UInt32 = 512
WMDM_DEVICE_TYPE_VIEW_PREF_METADATAVIEW: UInt32 = 1024
WMDM_POWER_CAP_BATTERY: UInt32 = 1
WMDM_POWER_CAP_EXTERNAL: UInt32 = 2
WMDM_POWER_IS_BATTERY: UInt32 = 4
WMDM_POWER_IS_EXTERNAL: UInt32 = 8
WMDM_POWER_PERCENT_AVAILABLE: UInt32 = 16
WMDM_STATUS_READY: UInt32 = 1
WMDM_STATUS_BUSY: UInt32 = 2
WMDM_STATUS_DEVICE_NOTPRESENT: UInt32 = 4
WMDM_STATUS_DEVICECONTROL_PLAYING: UInt32 = 8
WMDM_STATUS_DEVICECONTROL_RECORDING: UInt32 = 16
WMDM_STATUS_DEVICECONTROL_PAUSED: UInt32 = 32
WMDM_STATUS_DEVICECONTROL_REMOTE: UInt32 = 64
WMDM_STATUS_DEVICECONTROL_STREAM: UInt32 = 128
WMDM_STATUS_STORAGE_NOTPRESENT: UInt32 = 256
WMDM_STATUS_STORAGE_INITIALIZING: UInt32 = 512
WMDM_STATUS_STORAGE_BROKEN: UInt32 = 1024
WMDM_STATUS_STORAGE_NOTSUPPORTED: UInt32 = 2048
WMDM_STATUS_STORAGE_UNFORMATTED: UInt32 = 4096
WMDM_STATUS_STORAGECONTROL_INSERTING: UInt32 = 8192
WMDM_STATUS_STORAGECONTROL_DELETING: UInt32 = 16384
WMDM_STATUS_STORAGECONTROL_APPENDING: UInt32 = 32768
WMDM_STATUS_STORAGECONTROL_MOVING: UInt32 = 65536
WMDM_STATUS_STORAGECONTROL_READING: UInt32 = 131072
WMDM_DEVICECAP_CANPLAY: UInt32 = 1
WMDM_DEVICECAP_CANSTREAMPLAY: UInt32 = 2
WMDM_DEVICECAP_CANRECORD: UInt32 = 4
WMDM_DEVICECAP_CANSTREAMRECORD: UInt32 = 8
WMDM_DEVICECAP_CANPAUSE: UInt32 = 16
WMDM_DEVICECAP_CANRESUME: UInt32 = 32
WMDM_DEVICECAP_CANSTOP: UInt32 = 64
WMDM_DEVICECAP_CANSEEK: UInt32 = 128
WMDM_DEVICECAP_HASSECURECLOCK: UInt32 = 256
WMDM_SEEK_REMOTECONTROL: UInt32 = 1
WMDM_SEEK_STREAMINGAUDIO: UInt32 = 2
WMDM_STORAGE_ATTR_FILESYSTEM: UInt32 = 1
WMDM_STORAGE_ATTR_REMOVABLE: UInt32 = 2
WMDM_STORAGE_ATTR_NONREMOVABLE: UInt32 = 4
WMDM_FILE_ATTR_FOLDER: UInt32 = 8
WMDM_FILE_ATTR_LINK: UInt32 = 16
WMDM_FILE_ATTR_FILE: UInt32 = 32
WMDM_FILE_ATTR_VIDEO: UInt32 = 64
WMDM_STORAGE_ATTR_CANEDITMETADATA: UInt32 = 128
WMDM_STORAGE_ATTR_FOLDERS: UInt32 = 256
WMDM_FILE_ATTR_AUDIO: UInt32 = 4096
WMDM_FILE_ATTR_DATA: UInt32 = 8192
WMDM_FILE_ATTR_CANPLAY: UInt32 = 16384
WMDM_FILE_ATTR_CANDELETE: UInt32 = 32768
WMDM_FILE_ATTR_CANMOVE: UInt32 = 65536
WMDM_FILE_ATTR_CANRENAME: UInt32 = 131072
WMDM_FILE_ATTR_CANREAD: UInt32 = 262144
WMDM_FILE_ATTR_MUSIC: UInt32 = 524288
WMDM_FILE_CREATE_OVERWRITE: UInt32 = 1048576
WMDM_FILE_ATTR_AUDIOBOOK: UInt32 = 2097152
WMDM_FILE_ATTR_HIDDEN: UInt32 = 4194304
WMDM_FILE_ATTR_SYSTEM: UInt32 = 8388608
WMDM_FILE_ATTR_READONLY: UInt32 = 16777216
WMDM_STORAGE_ATTR_HAS_FOLDERS: UInt32 = 33554432
WMDM_STORAGE_ATTR_HAS_FILES: UInt32 = 67108864
WMDM_STORAGE_IS_DEFAULT: UInt32 = 134217728
WMDM_STORAGE_CONTAINS_DEFAULT: UInt32 = 268435456
WMDM_STORAGE_ATTR_VIRTUAL: UInt32 = 536870912
WMDM_STORAGECAP_FOLDERSINROOT: UInt32 = 1
WMDM_STORAGECAP_FILESINROOT: UInt32 = 2
WMDM_STORAGECAP_FOLDERSINFOLDERS: UInt32 = 4
WMDM_STORAGECAP_FILESINFOLDERS: UInt32 = 8
WMDM_STORAGECAP_FOLDERLIMITEXISTS: UInt32 = 16
WMDM_STORAGECAP_FILELIMITEXISTS: UInt32 = 32
WMDM_STORAGECAP_NOT_INITIALIZABLE: UInt32 = 64
WMDM_MODE_BLOCK: UInt32 = 1
WMDM_MODE_THREAD: UInt32 = 2
WMDM_CONTENT_FILE: UInt32 = 4
WMDM_CONTENT_FOLDER: UInt32 = 8
WMDM_CONTENT_OPERATIONINTERFACE: UInt32 = 16
WMDM_MODE_QUERY: UInt32 = 32
WMDM_MODE_PROGRESS: UInt32 = 64
WMDM_MODE_TRANSFER_PROTECTED: UInt32 = 128
WMDM_MODE_TRANSFER_UNPROTECTED: UInt32 = 256
WMDM_STORAGECONTROL_INSERTBEFORE: UInt32 = 512
WMDM_STORAGECONTROL_INSERTAFTER: UInt32 = 1024
WMDM_STORAGECONTROL_INSERTINTO: UInt32 = 2048
WMDM_MODE_RECURSIVE: UInt32 = 4096
WMDM_RIGHTS_PLAY_ON_PC: UInt32 = 1
WMDM_RIGHTS_COPY_TO_NON_SDMI_DEVICE: UInt32 = 2
WMDM_RIGHTS_COPY_TO_CD: UInt32 = 8
WMDM_RIGHTS_COPY_TO_SDMI_DEVICE: UInt32 = 16
WMDM_SEEK_BEGIN: UInt32 = 1
WMDM_SEEK_CURRENT: UInt32 = 2
WMDM_SEEK_END: UInt32 = 8
DO_NOT_VIRTUALIZE_STORAGES_AS_DEVICES: UInt32 = 1
ALLOW_OUTOFBAND_NOTIFICATION: UInt32 = 2
MDSP_READ: UInt32 = 1
MDSP_WRITE: UInt32 = 2
MDSP_SEEK_BOF: UInt32 = 1
MDSP_SEEK_CUR: UInt32 = 2
MDSP_SEEK_EOF: UInt32 = 4
WMDM_SCP_EXAMINE_EXTENSION: Int32 = 1
WMDM_SCP_EXAMINE_DATA: Int32 = 2
WMDM_SCP_DECIDE_DATA: Int32 = 8
WMDM_SCP_PROTECTED_OUTPUT: Int32 = 16
WMDM_SCP_UNPROTECTED_OUTPUT: Int32 = 32
WMDM_SCP_RIGHTS_DATA: Int32 = 64
WMDM_SCP_TRANSFER_OBJECTDATA: Int32 = 32
WMDM_SCP_NO_MORE_CHANGES: Int32 = 64
WMDM_SCP_DRMINFO_NOT_DRMPROTECTED: Int32 = 0
WMDM_SCP_DRMINFO_V1HEADER: Int32 = 1
WMDM_SCP_DRMINFO_V2HEADER: Int32 = 2
SCP_EVENTID_ACQSECURECLOCK: Guid = Guid('{86248cc9-4a59-43e2-9146-48a7f3f4140c}')
SCP_EVENTID_NEEDTOINDIV: Guid = Guid('{87a507c7-b469-4386-b976-d5d1ce538a6f}')
SCP_EVENTID_DRMINFO: Guid = Guid('{213dd287-41d2-432b-9e3f-3b4f7b3581dd}')
SCP_PARAMID_DRMVERSION: Guid = Guid('{41d0155d-7cc7-4217-ada9-005074624da4}')
SAC_MAC_LEN: UInt32 = 8
WMDM_LOG_SEV_INFO: UInt32 = 1
WMDM_LOG_SEV_WARN: UInt32 = 2
WMDM_LOG_SEV_ERROR: UInt32 = 4
WMDM_LOG_NOTIMESTAMP: UInt32 = 16
g_wszWMDMFileName: String = 'WMDM/FileName'
g_wszWMDMFormatCode: String = 'WMDM/FormatCode'
g_wszWMDMLastModifiedDate: String = 'WMDM/LastModifiedDate'
g_wszWMDMFileCreationDate: String = 'WMDM/FileCreationDate'
g_wszWMDMFileSize: String = 'WMDM/FileSize'
g_wszWMDMFileAttributes: String = 'WMDM/FileAttributes'
g_wszAudioWAVECodec: String = 'WMDM/AudioWAVECodec'
g_wszVideoFourCCCodec: String = 'WMDM/VideoFourCCCodec'
g_wszWMDMTitle: String = 'WMDM/Title'
g_wszWMDMAuthor: String = 'WMDM/Author'
g_wszWMDMDescription: String = 'WMDM/Description'
g_wszWMDMIsProtected: String = 'WMDM/IsProtected'
g_wszWMDMAlbumTitle: String = 'WMDM/AlbumTitle'
g_wszWMDMAlbumArtist: String = 'WMDM/AlbumArtist'
g_wszWMDMTrack: String = 'WMDM/Track'
g_wszWMDMGenre: String = 'WMDM/Genre'
g_wszWMDMTrackMood: String = 'WMDM/TrackMood'
g_wszWMDMAlbumCoverFormat: String = 'WMDM/AlbumCoverFormat'
g_wszWMDMAlbumCoverSize: String = 'WMDM/AlbumCoverSize'
g_wszWMDMAlbumCoverHeight: String = 'WMDM/AlbumCoverHeight'
g_wszWMDMAlbumCoverWidth: String = 'WMDM/AlbumCoverWidth'
g_wszWMDMAlbumCoverDuration: String = 'WMDM/AlbumCoverDuration'
g_wszWMDMAlbumCoverData: String = 'WMDM/AlbumCoverData'
g_wszWMDMYear: String = 'WMDM/Year'
g_wszWMDMComposer: String = 'WMDM/Composer'
g_wszWMDMCodec: String = 'WMDM/Codec'
g_wszWMDMDRMId: String = 'WMDM/DRMId'
g_wszWMDMBitrate: String = 'WMDM/Bitrate'
g_wszWMDMBitRateType: String = 'WMDM/BitRateType'
g_wszWMDMSampleRate: String = 'WMDM/SampleRate'
g_wszWMDMNumChannels: String = 'WMDM/NumChannels'
g_wszWMDMBlockAlignment: String = 'WMDM/BlockAlignment'
g_wszWMDMAudioBitDepth: String = 'WMDM/AudioBitDepth'
g_wszWMDMTotalBitrate: String = 'WMDM/TotalBitrate'
g_wszWMDMVideoBitrate: String = 'WMDM/VideoBitrate'
g_wszWMDMFrameRate: String = 'WMDM/FrameRate'
g_wszWMDMScanType: String = 'WMDM/ScanType'
g_wszWMDMKeyFrameDistance: String = 'WMDM/KeyFrameDistance'
g_wszWMDMBufferSize: String = 'WMDM/BufferSize'
g_wszWMDMQualitySetting: String = 'WMDM/QualitySetting'
g_wszWMDMEncodingProfile: String = 'WMDM/EncodingProfile'
g_wszWMDMDuration: String = 'WMDM/Duration'
g_wszWMDMAlbumArt: String = 'WMDM/AlbumArt'
g_wszWMDMBuyNow: String = 'WMDM/BuyNow'
g_wszWMDMNonConsumable: String = 'WMDM/NonConsumable'
g_wszWMDMediaClassPrimaryID: String = 'WMDM/MediaClassPrimaryID'
g_wszWMDMMediaClassSecondaryID: String = 'WMDM/MediaClassSecondaryID'
g_wszWMDMUserEffectiveRating: String = 'WMDM/UserEffectiveRating'
g_wszWMDMUserRating: String = 'WMDM/UserRating'
g_wszWMDMUserRatingOnDevice: String = 'WMDM/UserRatingOnDevice'
g_wszWMDMPlayCount: String = 'WMDM/PlayCount'
g_wszWMDMDevicePlayCount: String = 'WMDM/DevicePlayCount'
g_wszWMDMAuthorDate: String = 'WMDM/AuthorDate'
g_wszWMDMUserLastPlayTime: String = 'WMDM/UserLastPlayTime'
g_wszWMDMSubTitle: String = 'WMDM/SubTitle'
g_wszWMDMSubTitleDescription: String = 'WMDM/SubTitleDescription'
g_wszWMDMMediaCredits: String = 'WMDM/MediaCredits'
g_wszWMDMMediaStationName: String = 'WMDM/MediaStationName'
g_wszWMDMMediaOriginalChannel: String = 'WMDM/MediaOriginalChannel'
g_wszWMDMMediaOriginalBroadcastDateTime: String = 'WMDM/MediaOriginalBroadcastDateTime'
g_wszWMDMProviderCopyright: String = 'WMDM/ProviderCopyright'
g_wszWMDMSyncID: String = 'WMDM/SyncID'
g_wszWMDMPersistentUniqueID: String = 'WMDM/PersistentUniqueID'
g_wszWMDMWidth: String = 'WMDM/Width'
g_wszWMDMHeight: String = 'WMDM/Height'
g_wszWMDMSyncTime: String = 'WMDM/SyncTime'
g_wszWMDMParentalRating: String = 'WMDM/ParentalRating'
g_wszWMDMMetaGenre: String = 'WMDM/MetaGenre'
g_wszWMDMIsRepeat: String = 'WMDM/IsRepeat'
g_wszWMDMSupportedDeviceProperties: String = 'WMDM/SupportedDeviceProperties'
g_wszWMDMDeviceFriendlyName: String = 'WMDM/DeviceFriendlyName'
g_wszWMDMFormatsSupported: String = 'WMDM/FormatsSupported'
g_wszWMDMFormatsSupportedAreOrdered: String = 'WMDM/FormatsSupportedAreOrdered'
g_wszWMDMSyncRelationshipID: String = 'WMDM/SyncRelationshipID'
g_wszWMDMDeviceModelName: String = 'WMDM/DeviceModelName'
g_wszWMDMDeviceFirmwareVersion: String = 'WMDM/DeviceFirmwareVersion'
g_wszWMDMDeviceVendorExtension: String = 'WMDM/DeviceVendorExtension'
g_wszWMDMDeviceProtocol: String = 'WMDM/DeviceProtocol'
g_wszWMDMDeviceServiceProviderVendor: String = 'WMDM/DeviceServiceProviderVendor'
g_wszWMDMDeviceRevocationInfo: String = 'WMDM/DeviceRevocationInfo'
g_wszWMDMCollectionID: String = 'WMDM/CollectionID'
g_wszWMDMOwner: String = 'WMDM/Owner'
g_wszWMDMEditor: String = 'WMDM/Editor'
g_wszWMDMWebmaster: String = 'WMDM/Webmaster'
g_wszWMDMSourceURL: String = 'WMDM/SourceURL'
g_wszWMDMDestinationURL: String = 'WMDM/DestinationURL'
g_wszWMDMCategory: String = 'WMDM/Category'
g_wszWMDMTimeBookmark: String = 'WMDM/TimeBookmark'
g_wszWMDMObjectBookmark: String = 'WMDM/ObjectBookmark'
g_wszWMDMByteBookmark: String = 'WMDM/ByteBookmark'
g_wszWMDMDataOffset: String = 'WMDM/DataOffset'
g_wszWMDMDataLength: String = 'WMDM/DataLength'
g_wszWMDMDataUnits: String = 'WMDM/DataUnits'
g_wszWMDMTimeToLive: String = 'WMDM/TimeToLive'
g_wszWMDMMediaGuid: String = 'WMDM/MediaGuid'
g_wszWPDPassthroughPropertyValues: String = 'WPD/PassthroughPropertyValues'
EVENT_WMDM_CONTENT_TRANSFER: Guid = Guid('{339c9bf4-bcfe-4ed8-94df-eaf8c26ab61b}')
MTP_COMMAND_MAX_PARAMS: UInt32 = 5
MTP_RESPONSE_MAX_PARAMS: UInt32 = 5
MTP_RESPONSE_OK: UInt16 = 8193
class IComponentAuthenticate(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a9889c00-6d2b-11d3-8496-00c04f79dbc0}')
    @commethod(3)
    def SACAuth(self, dwProtocolID: UInt32, dwPass: UInt32, pbDataIn: POINTER(Byte), dwDataInLen: UInt32, ppbDataOut: POINTER(POINTER(Byte)), pdwDataOutLen: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SACGetProtocols(self, ppdwProtocols: POINTER(POINTER(UInt32)), pdwProtocolCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMDSPDevice(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1dcb3a12-33ed-11d3-8470-00c04f79dbc0}')
    @commethod(3)
    def GetName(self, pwszName: win32more.Windows.Win32.Foundation.PWSTR, nMaxChars: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetManufacturer(self, pwszName: win32more.Windows.Win32.Foundation.PWSTR, nMaxChars: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetVersion(self, pdwVersion: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetType(self, pdwType: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetSerialNumber(self, pSerialNumber: POINTER(win32more.Windows.Win32.Media.DeviceManager.WMDMID), abMac: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetPowerSource(self, pdwPowerSource: POINTER(UInt32), pdwPercentRemaining: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetStatus(self, pdwStatus: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetDeviceIcon(self, hIcon: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def EnumStorage(self, ppEnumStorage: POINTER(win32more.Windows.Win32.Media.DeviceManager.IMDSPEnumStorage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetFormatSupport(self, pFormatEx: POINTER(POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX)), pnFormatCount: POINTER(UInt32), pppwszMimeType: POINTER(POINTER(win32more.Windows.Win32.Foundation.PWSTR)), pnMimeTypeCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SendOpaqueCommand(self, pCommand: POINTER(win32more.Windows.Win32.Media.DeviceManager.OPAQUECOMMAND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMDSPDevice2(ComPtr):
    extends: win32more.Windows.Win32.Media.DeviceManager.IMDSPDevice
    _iid_ = Guid('{420d16ad-c97d-4e00-82aa-00e9f4335ddd}')
    @commethod(14)
    def GetStorage(self, pszStorageName: win32more.Windows.Win32.Foundation.PWSTR, ppStorage: POINTER(win32more.Windows.Win32.Media.DeviceManager.IMDSPStorage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetFormatSupport2(self, dwFlags: UInt32, ppAudioFormatEx: POINTER(POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX)), pnAudioFormatCount: POINTER(UInt32), ppVideoFormatEx: POINTER(POINTER(win32more.Windows.Win32.Media.MediaFoundation.VIDEOINFOHEADER)), pnVideoFormatCount: POINTER(UInt32), ppFileType: POINTER(POINTER(win32more.Windows.Win32.Media.DeviceManager.WMFILECAPABILITIES)), pnFileTypeCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetSpecifyPropertyPages(self, ppSpecifyPropPages: POINTER(win32more.Windows.Win32.System.Ole.ISpecifyPropertyPages), pppUnknowns: POINTER(POINTER(win32more.Windows.Win32.System.Com.IUnknown)), pcUnks: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetCanonicalName(self, pwszPnPName: win32more.Windows.Win32.Foundation.PWSTR, nMaxChars: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMDSPDevice3(ComPtr):
    extends: win32more.Windows.Win32.Media.DeviceManager.IMDSPDevice2
    _iid_ = Guid('{1a839845-fc55-487c-976f-ee38ac0e8c4e}')
    @commethod(18)
    def GetProperty(self, pwszPropName: win32more.Windows.Win32.Foundation.PWSTR, pValue: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetProperty(self, pwszPropName: win32more.Windows.Win32.Foundation.PWSTR, pValue: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetFormatCapability(self, format: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE, pFormatSupport: POINTER(win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMAT_CAPABILITY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def DeviceIoControl(self, dwIoControlCode: UInt32, lpInBuffer: POINTER(Byte), nInBufferSize: UInt32, lpOutBuffer: POINTER(Byte), pnOutBufferSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def FindStorage(self, findScope: win32more.Windows.Win32.Media.DeviceManager.WMDM_FIND_SCOPE, pwszUniqueID: win32more.Windows.Win32.Foundation.PWSTR, ppStorage: POINTER(win32more.Windows.Win32.Media.DeviceManager.IMDSPStorage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMDSPDeviceControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1dcb3a14-33ed-11d3-8470-00c04f79dbc0}')
    @commethod(3)
    def GetDCStatus(self, pdwStatus: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCapabilities(self, pdwCapabilitiesMask: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Play(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Record(self, pFormat: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Pause(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Resume(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Stop(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Seek(self, fuMode: UInt32, nOffset: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMDSPDirectTransfer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c2fe57a8-9304-478c-9ee4-47e397b912d7}')
    @commethod(3)
    def TransferToDevice(self, pwszSourceFilePath: win32more.Windows.Win32.Foundation.PWSTR, pSourceOperation: win32more.Windows.Win32.Media.DeviceManager.IWMDMOperation, fuFlags: UInt32, pwszDestinationName: win32more.Windows.Win32.Foundation.PWSTR, pSourceMetaData: win32more.Windows.Win32.Media.DeviceManager.IWMDMMetaData, pTransferProgress: win32more.Windows.Win32.Media.DeviceManager.IWMDMProgress, ppNewObject: POINTER(win32more.Windows.Win32.Media.DeviceManager.IMDSPStorage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMDSPEnumDevice(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1dcb3a11-33ed-11d3-8470-00c04f79dbc0}')
    @commethod(3)
    def Next(self, celt: UInt32, ppDevice: POINTER(win32more.Windows.Win32.Media.DeviceManager.IMDSPDevice), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32, pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnumDevice: POINTER(win32more.Windows.Win32.Media.DeviceManager.IMDSPEnumDevice)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMDSPEnumStorage(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1dcb3a15-33ed-11d3-8470-00c04f79dbc0}')
    @commethod(3)
    def Next(self, celt: UInt32, ppStorage: POINTER(win32more.Windows.Win32.Media.DeviceManager.IMDSPStorage), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32, pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnumStorage: POINTER(win32more.Windows.Win32.Media.DeviceManager.IMDSPEnumStorage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMDSPObject(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1dcb3a18-33ed-11d3-8470-00c04f79dbc0}')
    @commethod(3)
    def Open(self, fuMode: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Read(self, pData: POINTER(Byte), pdwSize: POINTER(UInt32), abMac: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Write(self, pData: POINTER(Byte), pdwSize: POINTER(UInt32), abMac: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Delete(self, fuMode: UInt32, pProgress: win32more.Windows.Win32.Media.DeviceManager.IWMDMProgress) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Seek(self, fuFlags: UInt32, dwOffset: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Rename(self, pwszNewName: win32more.Windows.Win32.Foundation.PWSTR, pProgress: win32more.Windows.Win32.Media.DeviceManager.IWMDMProgress) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Move(self, fuMode: UInt32, pProgress: win32more.Windows.Win32.Media.DeviceManager.IWMDMProgress, pTarget: win32more.Windows.Win32.Media.DeviceManager.IMDSPStorage) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Close(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMDSPObject2(ComPtr):
    extends: win32more.Windows.Win32.Media.DeviceManager.IMDSPObject
    _iid_ = Guid('{3f34cd3e-5907-4341-9af9-97f4187c3aa5}')
    @commethod(11)
    def ReadOnClearChannel(self, pData: POINTER(Byte), pdwSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def WriteOnClearChannel(self, pData: POINTER(Byte), pdwSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMDSPObjectInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1dcb3a19-33ed-11d3-8470-00c04f79dbc0}')
    @commethod(3)
    def GetPlayLength(self, pdwLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetPlayLength(self, dwLength: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPlayOffset(self, pdwOffset: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetPlayOffset(self, dwOffset: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetTotalLength(self, pdwLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetLastPlayPosition(self, pdwLastPos: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetLongestPlayPosition(self, pdwLongestPos: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMDSPRevoked(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a4e8f2d4-3f31-464d-b53d-4fc335998184}')
    @commethod(3)
    def GetRevocationURL(self, ppwszRevocationURL: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pdwBufferLen: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMDSPStorage(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1dcb3a16-33ed-11d3-8470-00c04f79dbc0}')
    @commethod(3)
    def SetAttributes(self, dwAttributes: UInt32, pFormat: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetStorageGlobals(self, ppStorageGlobals: POINTER(win32more.Windows.Win32.Media.DeviceManager.IMDSPStorageGlobals)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetAttributes(self, pdwAttributes: POINTER(UInt32), pFormat: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetName(self, pwszName: win32more.Windows.Win32.Foundation.PWSTR, nMaxChars: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetDate(self, pDateTimeUTC: POINTER(win32more.Windows.Win32.Media.DeviceManager.WMDMDATETIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetSize(self, pdwSizeLow: POINTER(UInt32), pdwSizeHigh: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRights(self, ppRights: POINTER(POINTER(win32more.Windows.Win32.Media.DeviceManager.WMDMRIGHTS)), pnRightsCount: POINTER(UInt32), abMac: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def CreateStorage(self, dwAttributes: UInt32, pFormat: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX), pwszName: win32more.Windows.Win32.Foundation.PWSTR, ppNewStorage: POINTER(win32more.Windows.Win32.Media.DeviceManager.IMDSPStorage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def EnumStorage(self, ppEnumStorage: POINTER(win32more.Windows.Win32.Media.DeviceManager.IMDSPEnumStorage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SendOpaqueCommand(self, pCommand: POINTER(win32more.Windows.Win32.Media.DeviceManager.OPAQUECOMMAND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMDSPStorage2(ComPtr):
    extends: win32more.Windows.Win32.Media.DeviceManager.IMDSPStorage
    _iid_ = Guid('{0a5e07a5-6454-4451-9c36-1c6ae7e2b1d6}')
    @commethod(13)
    def GetStorage(self, pszStorageName: win32more.Windows.Win32.Foundation.PWSTR, ppStorage: POINTER(win32more.Windows.Win32.Media.DeviceManager.IMDSPStorage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def CreateStorage2(self, dwAttributes: UInt32, dwAttributesEx: UInt32, pAudioFormat: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX), pVideoFormat: POINTER(win32more.Windows.Win32.Media.MediaFoundation.VIDEOINFOHEADER), pwszName: win32more.Windows.Win32.Foundation.PWSTR, qwFileSize: UInt64, ppNewStorage: POINTER(win32more.Windows.Win32.Media.DeviceManager.IMDSPStorage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetAttributes2(self, dwAttributes: UInt32, dwAttributesEx: UInt32, pAudioFormat: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX), pVideoFormat: POINTER(win32more.Windows.Win32.Media.MediaFoundation.VIDEOINFOHEADER)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetAttributes2(self, pdwAttributes: POINTER(UInt32), pdwAttributesEx: POINTER(UInt32), pAudioFormat: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX), pVideoFormat: POINTER(win32more.Windows.Win32.Media.MediaFoundation.VIDEOINFOHEADER)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMDSPStorage3(ComPtr):
    extends: win32more.Windows.Win32.Media.DeviceManager.IMDSPStorage2
    _iid_ = Guid('{6c669867-97ed-4a67-9706-1c5529d2a414}')
    @commethod(17)
    def GetMetadata(self, pMetadata: win32more.Windows.Win32.Media.DeviceManager.IWMDMMetaData) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetMetadata(self, pMetadata: win32more.Windows.Win32.Media.DeviceManager.IWMDMMetaData) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMDSPStorage4(ComPtr):
    extends: win32more.Windows.Win32.Media.DeviceManager.IMDSPStorage3
    _iid_ = Guid('{3133b2c4-515c-481b-b1ce-39327ecb4f74}')
    @commethod(19)
    def SetReferences(self, dwRefs: UInt32, ppISPStorage: POINTER(win32more.Windows.Win32.Media.DeviceManager.IMDSPStorage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetReferences(self, pdwRefs: POINTER(UInt32), pppISPStorage: POINTER(POINTER(win32more.Windows.Win32.Media.DeviceManager.IMDSPStorage))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def CreateStorageWithMetadata(self, dwAttributes: UInt32, pwszName: win32more.Windows.Win32.Foundation.PWSTR, pMetadata: win32more.Windows.Win32.Media.DeviceManager.IWMDMMetaData, qwFileSize: UInt64, ppNewStorage: POINTER(win32more.Windows.Win32.Media.DeviceManager.IMDSPStorage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetSpecifiedMetadata(self, cProperties: UInt32, ppwszPropNames: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pMetadata: win32more.Windows.Win32.Media.DeviceManager.IWMDMMetaData) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def FindStorage(self, findScope: win32more.Windows.Win32.Media.DeviceManager.WMDM_FIND_SCOPE, pwszUniqueID: win32more.Windows.Win32.Foundation.PWSTR, ppStorage: POINTER(win32more.Windows.Win32.Media.DeviceManager.IMDSPStorage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetParent(self, ppStorage: POINTER(win32more.Windows.Win32.Media.DeviceManager.IMDSPStorage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMDSPStorageGlobals(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1dcb3a17-33ed-11d3-8470-00c04f79dbc0}')
    @commethod(3)
    def GetCapabilities(self, pdwCapabilities: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSerialNumber(self, pSerialNum: POINTER(win32more.Windows.Win32.Media.DeviceManager.WMDMID), abMac: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetTotalSize(self, pdwTotalSizeLow: POINTER(UInt32), pdwTotalSizeHigh: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetTotalFree(self, pdwFreeLow: POINTER(UInt32), pdwFreeHigh: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetTotalBad(self, pdwBadLow: POINTER(UInt32), pdwBadHigh: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetStatus(self, pdwStatus: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Initialize(self, fuMode: UInt32, pProgress: win32more.Windows.Win32.Media.DeviceManager.IWMDMProgress) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetDevice(self, ppDevice: POINTER(win32more.Windows.Win32.Media.DeviceManager.IMDSPDevice)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetRootStorage(self, ppRoot: POINTER(win32more.Windows.Win32.Media.DeviceManager.IMDSPStorage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMDServiceProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1dcb3a10-33ed-11d3-8470-00c04f79dbc0}')
    @commethod(3)
    def GetDeviceCount(self, pdwCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EnumDevices(self, ppEnumDevice: POINTER(win32more.Windows.Win32.Media.DeviceManager.IMDSPEnumDevice)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMDServiceProvider2(ComPtr):
    extends: win32more.Windows.Win32.Media.DeviceManager.IMDServiceProvider
    _iid_ = Guid('{b2fa24b7-cda3-4694-9862-413ae1a34819}')
    @commethod(5)
    def CreateDevice(self, pwszDevicePath: win32more.Windows.Win32.Foundation.PWSTR, pdwCount: POINTER(UInt32), pppDeviceArray: POINTER(POINTER(win32more.Windows.Win32.Media.DeviceManager.IMDSPDevice))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMDServiceProvider3(ComPtr):
    extends: win32more.Windows.Win32.Media.DeviceManager.IMDServiceProvider2
    _iid_ = Guid('{4ed13ef3-a971-4d19-9f51-0e1826b2da57}')
    @commethod(6)
    def SetDeviceEnumPreference(self, dwEnumPref: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISCPSecureAuthenticate(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1dcb3a0f-33ed-11d3-8470-00c04f79dbc0}')
    @commethod(3)
    def GetSecureQuery(self, ppSecureQuery: POINTER(win32more.Windows.Win32.Media.DeviceManager.ISCPSecureQuery)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISCPSecureAuthenticate2(ComPtr):
    extends: win32more.Windows.Win32.Media.DeviceManager.ISCPSecureAuthenticate
    _iid_ = Guid('{b580cfae-1672-47e2-acaa-44bbecbcae5b}')
    @commethod(4)
    def GetSCPSession(self, ppSCPSession: POINTER(win32more.Windows.Win32.Media.DeviceManager.ISCPSession)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISCPSecureExchange(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1dcb3a0e-33ed-11d3-8470-00c04f79dbc0}')
    @commethod(3)
    def TransferContainerData(self, pData: POINTER(Byte), dwSize: UInt32, pfuReadyFlags: POINTER(UInt32), abMac: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ObjectData(self, pData: POINTER(Byte), pdwSize: POINTER(UInt32), abMac: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def TransferComplete(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISCPSecureExchange2(ComPtr):
    extends: win32more.Windows.Win32.Media.DeviceManager.ISCPSecureExchange
    _iid_ = Guid('{6c62fc7b-2690-483f-9d44-0a20cb35577c}')
    @commethod(6)
    def TransferContainerData2(self, pData: POINTER(Byte), dwSize: UInt32, pProgressCallback: win32more.Windows.Win32.Media.DeviceManager.IWMDMProgress3, pfuReadyFlags: POINTER(UInt32), abMac: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISCPSecureExchange3(ComPtr):
    extends: win32more.Windows.Win32.Media.DeviceManager.ISCPSecureExchange2
    _iid_ = Guid('{ab4e77e4-8908-4b17-bd2a-b1dbe6dd69e1}')
    @commethod(7)
    def TransferContainerDataOnClearChannel(self, pDevice: win32more.Windows.Win32.Media.DeviceManager.IMDSPDevice, pData: POINTER(Byte), dwSize: UInt32, pProgressCallback: win32more.Windows.Win32.Media.DeviceManager.IWMDMProgress3, pfuReadyFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetObjectDataOnClearChannel(self, pDevice: win32more.Windows.Win32.Media.DeviceManager.IMDSPDevice, pData: POINTER(Byte), pdwSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def TransferCompleteForDevice(self, pDevice: win32more.Windows.Win32.Media.DeviceManager.IMDSPDevice) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISCPSecureQuery(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1dcb3a0d-33ed-11d3-8470-00c04f79dbc0}')
    @commethod(3)
    def GetDataDemands(self, pfuFlags: POINTER(UInt32), pdwMinRightsData: POINTER(UInt32), pdwMinExamineData: POINTER(UInt32), pdwMinDecideData: POINTER(UInt32), abMac: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ExamineData(self, fuFlags: UInt32, pwszExtension: win32more.Windows.Win32.Foundation.PWSTR, pData: POINTER(Byte), dwSize: UInt32, abMac: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MakeDecision(self, fuFlags: UInt32, pData: POINTER(Byte), dwSize: UInt32, dwAppSec: UInt32, pbSPSessionKey: POINTER(Byte), dwSessionKeyLen: UInt32, pStorageGlobals: win32more.Windows.Win32.Media.DeviceManager.IMDSPStorageGlobals, ppExchange: POINTER(win32more.Windows.Win32.Media.DeviceManager.ISCPSecureExchange), abMac: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetRights(self, pData: POINTER(Byte), dwSize: UInt32, pbSPSessionKey: POINTER(Byte), dwSessionKeyLen: UInt32, pStgGlobals: win32more.Windows.Win32.Media.DeviceManager.IMDSPStorageGlobals, ppRights: POINTER(POINTER(win32more.Windows.Win32.Media.DeviceManager.WMDMRIGHTS)), pnRightsCount: POINTER(UInt32), abMac: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISCPSecureQuery2(ComPtr):
    extends: win32more.Windows.Win32.Media.DeviceManager.ISCPSecureQuery
    _iid_ = Guid('{ebe17e25-4fd7-4632-af46-6d93d4fcc72e}')
    @commethod(7)
    def MakeDecision2(self, fuFlags: UInt32, pData: POINTER(Byte), dwSize: UInt32, dwAppSec: UInt32, pbSPSessionKey: POINTER(Byte), dwSessionKeyLen: UInt32, pStorageGlobals: win32more.Windows.Win32.Media.DeviceManager.IMDSPStorageGlobals, pAppCertApp: POINTER(Byte), dwAppCertAppLen: UInt32, pAppCertSP: POINTER(Byte), dwAppCertSPLen: UInt32, pszRevocationURL: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pdwRevocationURLLen: POINTER(UInt32), pdwRevocationBitFlag: POINTER(UInt32), pqwFileSize: POINTER(UInt64), pUnknown: win32more.Windows.Win32.System.Com.IUnknown, ppExchange: POINTER(win32more.Windows.Win32.Media.DeviceManager.ISCPSecureExchange), abMac: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISCPSecureQuery3(ComPtr):
    extends: win32more.Windows.Win32.Media.DeviceManager.ISCPSecureQuery2
    _iid_ = Guid('{b7edd1a2-4dab-484b-b3c5-ad39b8b4c0b1}')
    @commethod(8)
    def GetRightsOnClearChannel(self, pData: POINTER(Byte), dwSize: UInt32, pbSPSessionKey: POINTER(Byte), dwSessionKeyLen: UInt32, pStgGlobals: win32more.Windows.Win32.Media.DeviceManager.IMDSPStorageGlobals, pProgressCallback: win32more.Windows.Win32.Media.DeviceManager.IWMDMProgress3, ppRights: POINTER(POINTER(win32more.Windows.Win32.Media.DeviceManager.WMDMRIGHTS)), pnRightsCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def MakeDecisionOnClearChannel(self, fuFlags: UInt32, pData: POINTER(Byte), dwSize: UInt32, dwAppSec: UInt32, pbSPSessionKey: POINTER(Byte), dwSessionKeyLen: UInt32, pStorageGlobals: win32more.Windows.Win32.Media.DeviceManager.IMDSPStorageGlobals, pProgressCallback: win32more.Windows.Win32.Media.DeviceManager.IWMDMProgress3, pAppCertApp: POINTER(Byte), dwAppCertAppLen: UInt32, pAppCertSP: POINTER(Byte), dwAppCertSPLen: UInt32, pszRevocationURL: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pdwRevocationURLLen: POINTER(UInt32), pdwRevocationBitFlag: POINTER(UInt32), pqwFileSize: POINTER(UInt64), pUnknown: win32more.Windows.Win32.System.Com.IUnknown, ppExchange: POINTER(win32more.Windows.Win32.Media.DeviceManager.ISCPSecureExchange)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISCPSession(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{88a3e6ed-eee4-4619-bbb3-fd4fb62715d1}')
    @commethod(3)
    def BeginSession(self, pIDevice: win32more.Windows.Win32.Media.DeviceManager.IMDSPDevice, pCtx: POINTER(Byte), dwSizeCtx: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EndSession(self, pCtx: POINTER(Byte), dwSizeCtx: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSecureQuery(self, ppSecureQuery: POINTER(win32more.Windows.Win32.Media.DeviceManager.ISCPSecureQuery)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMDMDevice(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1dcb3a02-33ed-11d3-8470-00c04f79dbc0}')
    @commethod(3)
    def GetName(self, pwszName: win32more.Windows.Win32.Foundation.PWSTR, nMaxChars: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetManufacturer(self, pwszName: win32more.Windows.Win32.Foundation.PWSTR, nMaxChars: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetVersion(self, pdwVersion: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetType(self, pdwType: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetSerialNumber(self, pSerialNumber: POINTER(win32more.Windows.Win32.Media.DeviceManager.WMDMID), abMac: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetPowerSource(self, pdwPowerSource: POINTER(UInt32), pdwPercentRemaining: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetStatus(self, pdwStatus: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetDeviceIcon(self, hIcon: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def EnumStorage(self, ppEnumStorage: POINTER(win32more.Windows.Win32.Media.DeviceManager.IWMDMEnumStorage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetFormatSupport(self, ppFormatEx: POINTER(POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX)), pnFormatCount: POINTER(UInt32), pppwszMimeType: POINTER(POINTER(win32more.Windows.Win32.Foundation.PWSTR)), pnMimeTypeCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SendOpaqueCommand(self, pCommand: POINTER(win32more.Windows.Win32.Media.DeviceManager.OPAQUECOMMAND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMDMDevice2(ComPtr):
    extends: win32more.Windows.Win32.Media.DeviceManager.IWMDMDevice
    _iid_ = Guid('{e34f3d37-9d67-4fc1-9252-62d28b2f8b55}')
    @commethod(14)
    def GetStorage(self, pszStorageName: win32more.Windows.Win32.Foundation.PWSTR, ppStorage: POINTER(win32more.Windows.Win32.Media.DeviceManager.IWMDMStorage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetFormatSupport2(self, dwFlags: UInt32, ppAudioFormatEx: POINTER(POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX)), pnAudioFormatCount: POINTER(UInt32), ppVideoFormatEx: POINTER(POINTER(win32more.Windows.Win32.Media.MediaFoundation.VIDEOINFOHEADER)), pnVideoFormatCount: POINTER(UInt32), ppFileType: POINTER(POINTER(win32more.Windows.Win32.Media.DeviceManager.WMFILECAPABILITIES)), pnFileTypeCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetSpecifyPropertyPages(self, ppSpecifyPropPages: POINTER(win32more.Windows.Win32.System.Ole.ISpecifyPropertyPages), pppUnknowns: POINTER(POINTER(win32more.Windows.Win32.System.Com.IUnknown)), pcUnks: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetCanonicalName(self, pwszPnPName: win32more.Windows.Win32.Foundation.PWSTR, nMaxChars: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMDMDevice3(ComPtr):
    extends: win32more.Windows.Win32.Media.DeviceManager.IWMDMDevice2
    _iid_ = Guid('{6c03e4fe-05db-4dda-9e3c-06233a6d5d65}')
    @commethod(18)
    def GetProperty(self, pwszPropName: win32more.Windows.Win32.Foundation.PWSTR, pValue: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetProperty(self, pwszPropName: win32more.Windows.Win32.Foundation.PWSTR, pValue: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetFormatCapability(self, format: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE, pFormatSupport: POINTER(win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMAT_CAPABILITY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def DeviceIoControl(self, dwIoControlCode: UInt32, lpInBuffer: POINTER(Byte), nInBufferSize: UInt32, lpOutBuffer: POINTER(Byte), pnOutBufferSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def FindStorage(self, findScope: win32more.Windows.Win32.Media.DeviceManager.WMDM_FIND_SCOPE, pwszUniqueID: win32more.Windows.Win32.Foundation.PWSTR, ppStorage: POINTER(win32more.Windows.Win32.Media.DeviceManager.IWMDMStorage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMDMDeviceControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1dcb3a04-33ed-11d3-8470-00c04f79dbc0}')
    @commethod(3)
    def GetStatus(self, pdwStatus: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCapabilities(self, pdwCapabilitiesMask: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Play(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Record(self, pFormat: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Pause(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Resume(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Stop(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Seek(self, fuMode: UInt32, nOffset: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMDMDeviceSession(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{82af0a65-9d96-412c-83e5-3c43e4b06cc7}')
    @commethod(3)
    def BeginSession(self, type: win32more.Windows.Win32.Media.DeviceManager.WMDM_SESSION_TYPE, pCtx: POINTER(Byte), dwSizeCtx: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EndSession(self, type: win32more.Windows.Win32.Media.DeviceManager.WMDM_SESSION_TYPE, pCtx: POINTER(Byte), dwSizeCtx: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMDMEnumDevice(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1dcb3a01-33ed-11d3-8470-00c04f79dbc0}')
    @commethod(3)
    def Next(self, celt: UInt32, ppDevice: POINTER(win32more.Windows.Win32.Media.DeviceManager.IWMDMDevice), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32, pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnumDevice: POINTER(win32more.Windows.Win32.Media.DeviceManager.IWMDMEnumDevice)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMDMEnumStorage(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1dcb3a05-33ed-11d3-8470-00c04f79dbc0}')
    @commethod(3)
    def Next(self, celt: UInt32, ppStorage: POINTER(win32more.Windows.Win32.Media.DeviceManager.IWMDMStorage), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32, pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnumStorage: POINTER(win32more.Windows.Win32.Media.DeviceManager.IWMDMEnumStorage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMDMLogger(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{110a3200-5a79-11d3-8d78-444553540000}')
    @commethod(3)
    def IsEnabled(self, pfEnabled: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Enable(self, fEnable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetLogFileName(self, pszFilename: win32more.Windows.Win32.Foundation.PSTR, nMaxChars: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetLogFileName(self, pszFilename: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def LogString(self, dwFlags: UInt32, pszSrcName: win32more.Windows.Win32.Foundation.PSTR, pszLog: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def LogDword(self, dwFlags: UInt32, pszSrcName: win32more.Windows.Win32.Foundation.PSTR, pszLogFormat: win32more.Windows.Win32.Foundation.PSTR, dwLog: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetSizeParams(self, pdwMaxSize: POINTER(UInt32), pdwShrinkToSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetSizeParams(self, dwMaxSize: UInt32, dwShrinkToSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMDMMetaData(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ec3b0663-0951-460a-9a80-0dceed3c043c}')
    @commethod(3)
    def AddItem(self, Type: win32more.Windows.Win32.Media.DeviceManager.WMDM_TAG_DATATYPE, pwszTagName: win32more.Windows.Win32.Foundation.PWSTR, pValue: POINTER(Byte), iLength: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def QueryByName(self, pwszTagName: win32more.Windows.Win32.Foundation.PWSTR, pType: POINTER(win32more.Windows.Win32.Media.DeviceManager.WMDM_TAG_DATATYPE), pValue: POINTER(POINTER(Byte)), pcbLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def QueryByIndex(self, iIndex: UInt32, ppwszName: POINTER(POINTER(UInt16)), pType: POINTER(win32more.Windows.Win32.Media.DeviceManager.WMDM_TAG_DATATYPE), ppValue: POINTER(POINTER(Byte)), pcbLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetItemCount(self, iCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMDMNotification(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3f5e95c0-0f43-4ed4-93d2-c89a45d59b81}')
    @commethod(3)
    def WMDMMessage(self, dwMessageType: UInt32, pwszCanonicalName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMDMObjectInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1dcb3a09-33ed-11d3-8470-00c04f79dbc0}')
    @commethod(3)
    def GetPlayLength(self, pdwLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetPlayLength(self, dwLength: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPlayOffset(self, pdwOffset: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetPlayOffset(self, dwOffset: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetTotalLength(self, pdwLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetLastPlayPosition(self, pdwLastPos: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetLongestPlayPosition(self, pdwLongestPos: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMDMOperation(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1dcb3a0b-33ed-11d3-8470-00c04f79dbc0}')
    @commethod(3)
    def BeginRead(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def BeginWrite(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetObjectName(self, pwszName: win32more.Windows.Win32.Foundation.PWSTR, nMaxChars: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetObjectName(self, pwszName: win32more.Windows.Win32.Foundation.PWSTR, nMaxChars: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetObjectAttributes(self, pdwAttributes: POINTER(UInt32), pFormat: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetObjectAttributes(self, dwAttributes: UInt32, pFormat: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetObjectTotalSize(self, pdwSize: POINTER(UInt32), pdwSizeHigh: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetObjectTotalSize(self, dwSize: UInt32, dwSizeHigh: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def TransferObjectData(self, pData: POINTER(Byte), pdwSize: POINTER(UInt32), abMac: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def End(self, phCompletionCode: POINTER(win32more.Windows.Win32.Foundation.HRESULT), pNewObject: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMDMOperation2(ComPtr):
    extends: win32more.Windows.Win32.Media.DeviceManager.IWMDMOperation
    _iid_ = Guid('{33445b48-7df7-425c-ad8f-0fc6d82f9f75}')
    @commethod(13)
    def SetObjectAttributes2(self, dwAttributes: UInt32, dwAttributesEx: UInt32, pFormat: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX), pVideoFormat: POINTER(win32more.Windows.Win32.Media.MediaFoundation.VIDEOINFOHEADER)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetObjectAttributes2(self, pdwAttributes: POINTER(UInt32), pdwAttributesEx: POINTER(UInt32), pAudioFormat: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX), pVideoFormat: POINTER(win32more.Windows.Win32.Media.MediaFoundation.VIDEOINFOHEADER)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMDMOperation3(ComPtr):
    extends: win32more.Windows.Win32.Media.DeviceManager.IWMDMOperation
    _iid_ = Guid('{d1f9b46a-9ca8-46d8-9d0f-1ec9bae54919}')
    @commethod(13)
    def TransferObjectDataOnClearChannel(self, pData: POINTER(Byte), pdwSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMDMProgress(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1dcb3a0c-33ed-11d3-8470-00c04f79dbc0}')
    @commethod(3)
    def Begin(self, dwEstimatedTicks: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Progress(self, dwTranspiredTicks: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def End(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMDMProgress2(ComPtr):
    extends: win32more.Windows.Win32.Media.DeviceManager.IWMDMProgress
    _iid_ = Guid('{3a43f550-b383-4e92-b04a-e6bbc660fefc}')
    @commethod(6)
    def End2(self, hrCompletionCode: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMDMProgress3(ComPtr):
    extends: win32more.Windows.Win32.Media.DeviceManager.IWMDMProgress2
    _iid_ = Guid('{21de01cb-3bb4-4929-b21a-17af3f80f658}')
    @commethod(7)
    def Begin3(self, EventId: Guid, dwEstimatedTicks: UInt32, pContext: POINTER(win32more.Windows.Win32.Media.DeviceManager.OPAQUECOMMAND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Progress3(self, EventId: Guid, dwTranspiredTicks: UInt32, pContext: POINTER(win32more.Windows.Win32.Media.DeviceManager.OPAQUECOMMAND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def End3(self, EventId: Guid, hrCompletionCode: win32more.Windows.Win32.Foundation.HRESULT, pContext: POINTER(win32more.Windows.Win32.Media.DeviceManager.OPAQUECOMMAND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMDMRevoked(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ebeccedb-88ee-4e55-b6a4-8d9f07d696aa}')
    @commethod(3)
    def GetRevocationURL(self, ppwszRevocationURL: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pdwBufferLen: POINTER(UInt32), pdwRevokedBitFlag: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMDMStorage(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1dcb3a06-33ed-11d3-8470-00c04f79dbc0}')
    @commethod(3)
    def SetAttributes(self, dwAttributes: UInt32, pFormat: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetStorageGlobals(self, ppStorageGlobals: POINTER(win32more.Windows.Win32.Media.DeviceManager.IWMDMStorageGlobals)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetAttributes(self, pdwAttributes: POINTER(UInt32), pFormat: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetName(self, pwszName: win32more.Windows.Win32.Foundation.PWSTR, nMaxChars: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetDate(self, pDateTimeUTC: POINTER(win32more.Windows.Win32.Media.DeviceManager.WMDMDATETIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetSize(self, pdwSizeLow: POINTER(UInt32), pdwSizeHigh: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRights(self, ppRights: POINTER(POINTER(win32more.Windows.Win32.Media.DeviceManager.WMDMRIGHTS)), pnRightsCount: POINTER(UInt32), abMac: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def EnumStorage(self, pEnumStorage: POINTER(win32more.Windows.Win32.Media.DeviceManager.IWMDMEnumStorage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SendOpaqueCommand(self, pCommand: POINTER(win32more.Windows.Win32.Media.DeviceManager.OPAQUECOMMAND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMDMStorage2(ComPtr):
    extends: win32more.Windows.Win32.Media.DeviceManager.IWMDMStorage
    _iid_ = Guid('{1ed5a144-5cd5-4683-9eff-72cbdb2d9533}')
    @commethod(12)
    def GetStorage(self, pszStorageName: win32more.Windows.Win32.Foundation.PWSTR, ppStorage: POINTER(win32more.Windows.Win32.Media.DeviceManager.IWMDMStorage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetAttributes2(self, dwAttributes: UInt32, dwAttributesEx: UInt32, pFormat: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX), pVideoFormat: POINTER(win32more.Windows.Win32.Media.MediaFoundation.VIDEOINFOHEADER)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetAttributes2(self, pdwAttributes: POINTER(UInt32), pdwAttributesEx: POINTER(UInt32), pAudioFormat: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX), pVideoFormat: POINTER(win32more.Windows.Win32.Media.MediaFoundation.VIDEOINFOHEADER)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMDMStorage3(ComPtr):
    extends: win32more.Windows.Win32.Media.DeviceManager.IWMDMStorage2
    _iid_ = Guid('{97717eea-926a-464e-96a4-247b0216026e}')
    @commethod(15)
    def GetMetadata(self, ppMetadata: POINTER(win32more.Windows.Win32.Media.DeviceManager.IWMDMMetaData)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetMetadata(self, pMetadata: win32more.Windows.Win32.Media.DeviceManager.IWMDMMetaData) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def CreateEmptyMetadataObject(self, ppMetadata: POINTER(win32more.Windows.Win32.Media.DeviceManager.IWMDMMetaData)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetEnumPreference(self, pMode: POINTER(win32more.Windows.Win32.Media.DeviceManager.WMDM_STORAGE_ENUM_MODE), nViews: UInt32, pViews: POINTER(win32more.Windows.Win32.Media.DeviceManager.WMDMMetadataView)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMDMStorage4(ComPtr):
    extends: win32more.Windows.Win32.Media.DeviceManager.IWMDMStorage3
    _iid_ = Guid('{c225bac5-a03a-40b8-9a23-91cf478c64a6}')
    @commethod(19)
    def SetReferences(self, dwRefs: UInt32, ppIWMDMStorage: POINTER(win32more.Windows.Win32.Media.DeviceManager.IWMDMStorage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetReferences(self, pdwRefs: POINTER(UInt32), pppIWMDMStorage: POINTER(POINTER(win32more.Windows.Win32.Media.DeviceManager.IWMDMStorage))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetRightsWithProgress(self, pIProgressCallback: win32more.Windows.Win32.Media.DeviceManager.IWMDMProgress3, ppRights: POINTER(POINTER(win32more.Windows.Win32.Media.DeviceManager.WMDMRIGHTS)), pnRightsCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetSpecifiedMetadata(self, cProperties: UInt32, ppwszPropNames: POINTER(win32more.Windows.Win32.Foundation.PWSTR), ppMetadata: POINTER(win32more.Windows.Win32.Media.DeviceManager.IWMDMMetaData)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def FindStorage(self, findScope: win32more.Windows.Win32.Media.DeviceManager.WMDM_FIND_SCOPE, pwszUniqueID: win32more.Windows.Win32.Foundation.PWSTR, ppStorage: POINTER(win32more.Windows.Win32.Media.DeviceManager.IWMDMStorage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetParent(self, ppStorage: POINTER(win32more.Windows.Win32.Media.DeviceManager.IWMDMStorage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMDMStorageControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1dcb3a08-33ed-11d3-8470-00c04f79dbc0}')
    @commethod(3)
    def Insert(self, fuMode: UInt32, pwszFile: win32more.Windows.Win32.Foundation.PWSTR, pOperation: win32more.Windows.Win32.Media.DeviceManager.IWMDMOperation, pProgress: win32more.Windows.Win32.Media.DeviceManager.IWMDMProgress, ppNewObject: POINTER(win32more.Windows.Win32.Media.DeviceManager.IWMDMStorage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Delete(self, fuMode: UInt32, pProgress: win32more.Windows.Win32.Media.DeviceManager.IWMDMProgress) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Rename(self, fuMode: UInt32, pwszNewName: win32more.Windows.Win32.Foundation.PWSTR, pProgress: win32more.Windows.Win32.Media.DeviceManager.IWMDMProgress) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Read(self, fuMode: UInt32, pwszFile: win32more.Windows.Win32.Foundation.PWSTR, pProgress: win32more.Windows.Win32.Media.DeviceManager.IWMDMProgress, pOperation: win32more.Windows.Win32.Media.DeviceManager.IWMDMOperation) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Move(self, fuMode: UInt32, pTargetObject: win32more.Windows.Win32.Media.DeviceManager.IWMDMStorage, pProgress: win32more.Windows.Win32.Media.DeviceManager.IWMDMProgress) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMDMStorageControl2(ComPtr):
    extends: win32more.Windows.Win32.Media.DeviceManager.IWMDMStorageControl
    _iid_ = Guid('{972c2e88-bd6c-4125-8e09-84f837e637b6}')
    @commethod(8)
    def Insert2(self, fuMode: UInt32, pwszFileSource: win32more.Windows.Win32.Foundation.PWSTR, pwszFileDest: win32more.Windows.Win32.Foundation.PWSTR, pOperation: win32more.Windows.Win32.Media.DeviceManager.IWMDMOperation, pProgress: win32more.Windows.Win32.Media.DeviceManager.IWMDMProgress, pUnknown: win32more.Windows.Win32.System.Com.IUnknown, ppNewObject: POINTER(win32more.Windows.Win32.Media.DeviceManager.IWMDMStorage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMDMStorageControl3(ComPtr):
    extends: win32more.Windows.Win32.Media.DeviceManager.IWMDMStorageControl2
    _iid_ = Guid('{b3266365-d4f3-4696-8d53-bd27ec60993a}')
    @commethod(9)
    def Insert3(self, fuMode: UInt32, fuType: UInt32, pwszFileSource: win32more.Windows.Win32.Foundation.PWSTR, pwszFileDest: win32more.Windows.Win32.Foundation.PWSTR, pOperation: win32more.Windows.Win32.Media.DeviceManager.IWMDMOperation, pProgress: win32more.Windows.Win32.Media.DeviceManager.IWMDMProgress, pMetaData: win32more.Windows.Win32.Media.DeviceManager.IWMDMMetaData, pUnknown: win32more.Windows.Win32.System.Com.IUnknown, ppNewObject: POINTER(win32more.Windows.Win32.Media.DeviceManager.IWMDMStorage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMDMStorageGlobals(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1dcb3a07-33ed-11d3-8470-00c04f79dbc0}')
    @commethod(3)
    def GetCapabilities(self, pdwCapabilities: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSerialNumber(self, pSerialNum: POINTER(win32more.Windows.Win32.Media.DeviceManager.WMDMID), abMac: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetTotalSize(self, pdwTotalSizeLow: POINTER(UInt32), pdwTotalSizeHigh: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetTotalFree(self, pdwFreeLow: POINTER(UInt32), pdwFreeHigh: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetTotalBad(self, pdwBadLow: POINTER(UInt32), pdwBadHigh: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetStatus(self, pdwStatus: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Initialize(self, fuMode: UInt32, pProgress: win32more.Windows.Win32.Media.DeviceManager.IWMDMProgress) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMDeviceManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1dcb3a00-33ed-11d3-8470-00c04f79dbc0}')
    @commethod(3)
    def GetRevision(self, pdwRevision: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDeviceCount(self, pdwCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumDevices(self, ppEnumDevice: POINTER(win32more.Windows.Win32.Media.DeviceManager.IWMDMEnumDevice)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMDeviceManager2(ComPtr):
    extends: win32more.Windows.Win32.Media.DeviceManager.IWMDeviceManager
    _iid_ = Guid('{923e5249-8731-4c5b-9b1c-b8b60b6e46af}')
    @commethod(6)
    def GetDeviceFromCanonicalName(self, pwszCanonicalName: win32more.Windows.Win32.Foundation.PWSTR, ppDevice: POINTER(win32more.Windows.Win32.Media.DeviceManager.IWMDMDevice)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def EnumDevices2(self, ppEnumDevice: POINTER(win32more.Windows.Win32.Media.DeviceManager.IWMDMEnumDevice)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Reinitialize(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMDeviceManager3(ComPtr):
    extends: win32more.Windows.Win32.Media.DeviceManager.IWMDeviceManager2
    _iid_ = Guid('{af185c41-100d-46ed-be2e-9ce8c44594ef}')
    @commethod(9)
    def SetDeviceEnumPreference(self, dwEnumPref: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class MACINFO(Structure):
    fUsed: win32more.Windows.Win32.Foundation.BOOL
    abMacState: Byte * 36
class MTP_COMMAND_DATA_IN(Structure):
    OpCode: UInt16
    NumParams: UInt32
    Params: UInt32 * 5
    NextPhase: UInt32
    CommandWriteDataSize: UInt32
    CommandWriteData: Byte * 1
    _pack_ = 1
class MTP_COMMAND_DATA_OUT(Structure):
    ResponseCode: UInt16
    NumParams: UInt32
    Params: UInt32 * 5
    CommandReadDataSize: UInt32
    CommandReadData: Byte * 1
    _pack_ = 1
MediaDevMgr = Guid('{25baad81-3560-11d3-8471-00c04f79dbc0}')
MediaDevMgrClassFactory = Guid('{50040c1d-bdbf-4924-b873-f14d6c5bfd66}')
class OPAQUECOMMAND(Structure):
    guidCommand: Guid
    dwDataLen: UInt32
    pData: POINTER(Byte)
    abMAC: Byte * 20
class WMDMDATETIME(Structure):
    wYear: UInt16
    wMonth: UInt16
    wDay: UInt16
    wHour: UInt16
    wMinute: UInt16
    wSecond: UInt16
class WMDMDetermineMaxPropStringLen(Union):
    sz001: Char * 27
    sz002: Char * 31
    sz003: Char * 14
    sz004: Char * 16
    sz005: Char * 22
    sz006: Char * 14
    sz007: Char * 20
    sz008: Char * 20
    sz009: Char * 22
    sz010: Char * 11
    sz011: Char * 12
    sz012: Char * 17
    sz013: Char * 17
    sz014: Char * 16
    sz015: Char * 17
    sz016: Char * 11
    sz017: Char * 11
    sz018: Char * 15
    sz019: Char * 22
    sz020: Char * 20
    sz021: Char * 22
    sz022: Char * 21
    sz023: Char * 24
    sz024: Char * 20
    sz025: Char * 10
    sz026: Char * 14
    sz027: Char * 11
    sz028: Char * 11
    sz029: Char * 13
    sz030: Char * 17
    sz031: Char * 16
    sz032: Char * 17
    sz033: Char * 20
    sz034: Char * 19
    sz035: Char * 18
    sz036: Char * 18
    sz037: Char * 15
    sz041: Char * 14
    sz043: Char * 22
    sz044: Char * 16
    sz045: Char * 20
    sz046: Char * 14
    sz047: Char * 14
    sz048: Char * 12
    sz049: Char * 25
    sz050: Char * 26
    sz051: Char * 25
    sz052: Char * 16
    sz053: Char * 24
    sz054: Char * 15
    sz055: Char * 21
    sz056: Char * 16
    sz057: Char * 22
    sz058: Char * 14
    sz059: Char * 25
    sz060: Char * 18
    sz061: Char * 22
    sz062: Char * 26
    sz063: Char * 36
    sz064: Char * 23
    sz065: Char * 12
    sz066: Char * 24
    sz067: Char * 11
    sz068: Char * 12
    sz069: Char * 14
    sz070: Char * 20
    sz071: Char * 15
    sz072: Char * 14
    sz073: Char * 31
    sz074: Char * 24
    sz075: Char * 22
    sz076: Char * 24
    sz077: Char * 21
    sz078: Char * 27
    sz079: Char * 27
    sz080: Char * 20
    sz081: Char * 33
    sz082: Char * 21
    sz083: Char * 32
    sz084: Char * 26
    sz085: Char * 18
    sz086: Char * 30
WMDMDevice = Guid('{807b3cdf-357a-11d3-8471-00c04f79dbc0}')
WMDMDeviceEnum = Guid('{430e35af-3971-11d3-8474-00c04f79dbc0}')
class WMDMID(Structure):
    cbSize: UInt32
    dwVendorID: UInt32
    pID: Byte * 128
    SerialNumberLength: UInt32
WMDMLogger = Guid('{110a3202-5a79-11d3-8d78-444553540000}')
WMDMMessage = Int32
WMDM_MSG_DEVICE_ARRIVAL: win32more.Windows.Win32.Media.DeviceManager.WMDMMessage = 0
WMDM_MSG_DEVICE_REMOVAL: win32more.Windows.Win32.Media.DeviceManager.WMDMMessage = 1
WMDM_MSG_MEDIA_ARRIVAL: win32more.Windows.Win32.Media.DeviceManager.WMDMMessage = 2
WMDM_MSG_MEDIA_REMOVAL: win32more.Windows.Win32.Media.DeviceManager.WMDMMessage = 3
class WMDMMetadataView(Structure):
    pwszViewName: win32more.Windows.Win32.Foundation.PWSTR
    nDepth: UInt32
    ppwszTags: POINTER(POINTER(UInt16))
class WMDMRIGHTS(Structure):
    cbSize: UInt32
    dwContentType: UInt32
    fuFlags: UInt32
    fuRights: UInt32
    dwAppSec: UInt32
    dwPlaybackCount: UInt32
    ExpirationDate: win32more.Windows.Win32.Media.DeviceManager.WMDMDATETIME
WMDMStorage = Guid('{807b3ce0-357a-11d3-8471-00c04f79dbc0}')
WMDMStorageEnum = Guid('{eb401a3b-3af7-11d3-8474-00c04f79dbc0}')
WMDMStorageGlobal = Guid('{807b3ce1-357a-11d3-8471-00c04f79dbc0}')
WMDM_ENUM_PROP_VALID_VALUES_FORM = Int32
WMDM_ENUM_PROP_VALID_VALUES_ANY: win32more.Windows.Win32.Media.DeviceManager.WMDM_ENUM_PROP_VALID_VALUES_FORM = 0
WMDM_ENUM_PROP_VALID_VALUES_RANGE: win32more.Windows.Win32.Media.DeviceManager.WMDM_ENUM_PROP_VALID_VALUES_FORM = 1
WMDM_ENUM_PROP_VALID_VALUES_ENUM: win32more.Windows.Win32.Media.DeviceManager.WMDM_ENUM_PROP_VALID_VALUES_FORM = 2
WMDM_FIND_SCOPE = Int32
WMDM_FIND_SCOPE_GLOBAL: win32more.Windows.Win32.Media.DeviceManager.WMDM_FIND_SCOPE = 0
WMDM_FIND_SCOPE_IMMEDIATE_CHILDREN: win32more.Windows.Win32.Media.DeviceManager.WMDM_FIND_SCOPE = 1
WMDM_FORMATCODE = Int32
WMDM_FORMATCODE_NOTUSED: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 0
WMDM_FORMATCODE_ALLIMAGES: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = -1
WMDM_FORMATCODE_UNDEFINED: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 12288
WMDM_FORMATCODE_ASSOCIATION: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 12289
WMDM_FORMATCODE_SCRIPT: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 12290
WMDM_FORMATCODE_EXECUTABLE: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 12291
WMDM_FORMATCODE_TEXT: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 12292
WMDM_FORMATCODE_HTML: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 12293
WMDM_FORMATCODE_DPOF: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 12294
WMDM_FORMATCODE_AIFF: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 12295
WMDM_FORMATCODE_WAVE: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 12296
WMDM_FORMATCODE_MP3: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 12297
WMDM_FORMATCODE_AVI: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 12298
WMDM_FORMATCODE_MPEG: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 12299
WMDM_FORMATCODE_ASF: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 12300
WMDM_FORMATCODE_RESERVED_FIRST: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 12301
WMDM_FORMATCODE_RESERVED_LAST: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 14335
WMDM_FORMATCODE_IMAGE_UNDEFINED: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 14336
WMDM_FORMATCODE_IMAGE_EXIF: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 14337
WMDM_FORMATCODE_IMAGE_TIFFEP: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 14338
WMDM_FORMATCODE_IMAGE_FLASHPIX: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 14339
WMDM_FORMATCODE_IMAGE_BMP: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 14340
WMDM_FORMATCODE_IMAGE_CIFF: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 14341
WMDM_FORMATCODE_IMAGE_GIF: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 14343
WMDM_FORMATCODE_IMAGE_JFIF: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 14344
WMDM_FORMATCODE_IMAGE_PCD: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 14345
WMDM_FORMATCODE_IMAGE_PICT: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 14346
WMDM_FORMATCODE_IMAGE_PNG: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 14347
WMDM_FORMATCODE_IMAGE_TIFF: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 14349
WMDM_FORMATCODE_IMAGE_TIFFIT: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 14350
WMDM_FORMATCODE_IMAGE_JP2: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 14351
WMDM_FORMATCODE_IMAGE_JPX: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 14352
WMDM_FORMATCODE_IMAGE_RESERVED_FIRST: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 14353
WMDM_FORMATCODE_IMAGE_RESERVED_LAST: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 16383
WMDM_FORMATCODE_UNDEFINEDFIRMWARE: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 47106
WMDM_FORMATCODE_WBMP: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 47107
WMDM_FORMATCODE_JPEGXR: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 47108
WMDM_FORMATCODE_WINDOWSIMAGEFORMAT: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 47233
WMDM_FORMATCODE_UNDEFINEDAUDIO: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 47360
WMDM_FORMATCODE_WMA: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 47361
WMDM_FORMATCODE_OGG: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 47362
WMDM_FORMATCODE_AAC: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 47363
WMDM_FORMATCODE_AUDIBLE: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 47364
WMDM_FORMATCODE_FLAC: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 47366
WMDM_FORMATCODE_QCELP: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 47367
WMDM_FORMATCODE_AMR: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 47368
WMDM_FORMATCODE_UNDEFINEDVIDEO: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 47488
WMDM_FORMATCODE_WMV: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 47489
WMDM_FORMATCODE_MP4: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 47490
WMDM_FORMATCODE_MP2: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 47491
WMDM_FORMATCODE_3GP: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 47492
WMDM_FORMATCODE_3G2: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 47493
WMDM_FORMATCODE_AVCHD: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 47494
WMDM_FORMATCODE_ATSCTS: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 47495
WMDM_FORMATCODE_DVBTS: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 47496
WMDM_FORMATCODE_MKV: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 47497
WMDM_FORMATCODE_MKA: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 47498
WMDM_FORMATCODE_MK3D: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 47499
WMDM_FORMATCODE_UNDEFINEDCOLLECTION: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 47616
WMDM_FORMATCODE_ABSTRACTMULTIMEDIAALBUM: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 47617
WMDM_FORMATCODE_ABSTRACTIMAGEALBUM: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 47618
WMDM_FORMATCODE_ABSTRACTAUDIOALBUM: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 47619
WMDM_FORMATCODE_ABSTRACTVIDEOALBUM: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 47620
WMDM_FORMATCODE_ABSTRACTAUDIOVIDEOPLAYLIST: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 47621
WMDM_FORMATCODE_ABSTRACTCONTACTGROUP: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 47622
WMDM_FORMATCODE_ABSTRACTMESSAGEFOLDER: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 47623
WMDM_FORMATCODE_ABSTRACTCHAPTEREDPRODUCTION: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 47624
WMDM_FORMATCODE_MEDIA_CAST: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 47627
WMDM_FORMATCODE_WPLPLAYLIST: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 47632
WMDM_FORMATCODE_M3UPLAYLIST: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 47633
WMDM_FORMATCODE_MPLPLAYLIST: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 47634
WMDM_FORMATCODE_ASXPLAYLIST: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 47635
WMDM_FORMATCODE_PLSPLAYLIST: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 47636
WMDM_FORMATCODE_UNDEFINEDDOCUMENT: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 47744
WMDM_FORMATCODE_ABSTRACTDOCUMENT: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 47745
WMDM_FORMATCODE_XMLDOCUMENT: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 47746
WMDM_FORMATCODE_MICROSOFTWORDDOCUMENT: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 47747
WMDM_FORMATCODE_MHTCOMPILEDHTMLDOCUMENT: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 47748
WMDM_FORMATCODE_MICROSOFTEXCELSPREADSHEET: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 47749
WMDM_FORMATCODE_MICROSOFTPOWERPOINTDOCUMENT: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 47750
WMDM_FORMATCODE_UNDEFINEDMESSAGE: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 47872
WMDM_FORMATCODE_ABSTRACTMESSAGE: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 47873
WMDM_FORMATCODE_UNDEFINEDCONTACT: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 48000
WMDM_FORMATCODE_ABSTRACTCONTACT: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 48001
WMDM_FORMATCODE_VCARD2: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 48002
WMDM_FORMATCODE_VCARD3: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 48003
WMDM_FORMATCODE_UNDEFINEDCALENDARITEM: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 48640
WMDM_FORMATCODE_ABSTRACTCALENDARITEM: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 48641
WMDM_FORMATCODE_VCALENDAR1: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 48642
WMDM_FORMATCODE_VCALENDAR2: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 48643
WMDM_FORMATCODE_UNDEFINEDWINDOWSEXECUTABLE: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 48768
WMDM_FORMATCODE_M4A: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 1297101889
WMDM_FORMATCODE_3GPA: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 860311617
WMDM_FORMATCODE_3G2A: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 860303937
WMDM_FORMATCODE_SECTION: win32more.Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE = 48770
class WMDM_FORMAT_CAPABILITY(Structure):
    nPropConfig: UInt32
    pConfigs: POINTER(win32more.Windows.Win32.Media.DeviceManager.WMDM_PROP_CONFIG)
class WMDM_PROP_CONFIG(Structure):
    nPreference: UInt32
    nPropDesc: UInt32
    pPropDesc: POINTER(win32more.Windows.Win32.Media.DeviceManager.WMDM_PROP_DESC)
class WMDM_PROP_DESC(Structure):
    pwszPropName: win32more.Windows.Win32.Foundation.PWSTR
    ValidValuesForm: win32more.Windows.Win32.Media.DeviceManager.WMDM_ENUM_PROP_VALID_VALUES_FORM
    ValidValues: _ValidValues_e__Union
    class _ValidValues_e__Union(Union):
        ValidValuesRange: win32more.Windows.Win32.Media.DeviceManager.WMDM_PROP_VALUES_RANGE
        EnumeratedValidValues: win32more.Windows.Win32.Media.DeviceManager.WMDM_PROP_VALUES_ENUM
class WMDM_PROP_VALUES_ENUM(Structure):
    cEnumValues: UInt32
    pValues: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)
class WMDM_PROP_VALUES_RANGE(Structure):
    rangeMin: win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT
    rangeMax: win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT
    rangeStep: win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT
WMDM_SESSION_TYPE = Int32
WMDM_SESSION_NONE: win32more.Windows.Win32.Media.DeviceManager.WMDM_SESSION_TYPE = 0
WMDM_SESSION_TRANSFER_TO_DEVICE: win32more.Windows.Win32.Media.DeviceManager.WMDM_SESSION_TYPE = 1
WMDM_SESSION_TRANSFER_FROM_DEVICE: win32more.Windows.Win32.Media.DeviceManager.WMDM_SESSION_TYPE = 16
WMDM_SESSION_DELETE: win32more.Windows.Win32.Media.DeviceManager.WMDM_SESSION_TYPE = 256
WMDM_SESSION_CUSTOM: win32more.Windows.Win32.Media.DeviceManager.WMDM_SESSION_TYPE = 4096
WMDM_STORAGE_ENUM_MODE = Int32
ENUM_MODE_RAW: win32more.Windows.Win32.Media.DeviceManager.WMDM_STORAGE_ENUM_MODE = 0
ENUM_MODE_USE_DEVICE_PREF: win32more.Windows.Win32.Media.DeviceManager.WMDM_STORAGE_ENUM_MODE = 1
ENUM_MODE_METADATA_VIEWS: win32more.Windows.Win32.Media.DeviceManager.WMDM_STORAGE_ENUM_MODE = 2
WMDM_TAG_DATATYPE = Int32
WMDM_TYPE_DWORD: win32more.Windows.Win32.Media.DeviceManager.WMDM_TAG_DATATYPE = 0
WMDM_TYPE_STRING: win32more.Windows.Win32.Media.DeviceManager.WMDM_TAG_DATATYPE = 1
WMDM_TYPE_BINARY: win32more.Windows.Win32.Media.DeviceManager.WMDM_TAG_DATATYPE = 2
WMDM_TYPE_BOOL: win32more.Windows.Win32.Media.DeviceManager.WMDM_TAG_DATATYPE = 3
WMDM_TYPE_QWORD: win32more.Windows.Win32.Media.DeviceManager.WMDM_TAG_DATATYPE = 4
WMDM_TYPE_WORD: win32more.Windows.Win32.Media.DeviceManager.WMDM_TAG_DATATYPE = 5
WMDM_TYPE_GUID: win32more.Windows.Win32.Media.DeviceManager.WMDM_TAG_DATATYPE = 6
WMDM_TYPE_DATE: win32more.Windows.Win32.Media.DeviceManager.WMDM_TAG_DATATYPE = 7
class WMFILECAPABILITIES(Structure):
    pwszMimeType: win32more.Windows.Win32.Foundation.PWSTR
    dwReserved: UInt32


make_ready(__name__)
