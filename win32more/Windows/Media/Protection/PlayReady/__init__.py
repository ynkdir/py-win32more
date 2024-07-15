from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Media.Core
import win32more.Windows.Media.Protection
import win32more.Windows.Media.Protection.PlayReady
import win32more.Windows.Storage
import win32more.Windows.Win32.System.WinRT
class INDClient(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.INDClient'
    _iid_ = Guid('{3bd6781b-61b8-46e2-99a5-8abcb6b9f7d6}')
    @winrt_commethod(6)
    def add_RegistrationCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Protection.PlayReady.NDClient, win32more.Windows.Media.Protection.PlayReady.INDRegistrationCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_RegistrationCompleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_ProximityDetectionCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Protection.PlayReady.NDClient, win32more.Windows.Media.Protection.PlayReady.INDProximityDetectionCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_ProximityDetectionCompleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_LicenseFetchCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Protection.PlayReady.NDClient, win32more.Windows.Media.Protection.PlayReady.INDLicenseFetchCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_LicenseFetchCompleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_ReRegistrationNeeded(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Protection.PlayReady.NDClient, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_ReRegistrationNeeded(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_ClosedCaptionDataReceived(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Protection.PlayReady.NDClient, win32more.Windows.Media.Protection.PlayReady.INDClosedCaptionDataReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_ClosedCaptionDataReceived(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def StartAsync(self, contentUrl: win32more.Windows.Foundation.Uri, startAsyncOptions: UInt32, registrationCustomData: win32more.Windows.Media.Protection.PlayReady.INDCustomData, licenseFetchDescriptor: win32more.Windows.Media.Protection.PlayReady.INDLicenseFetchDescriptor) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Protection.PlayReady.INDStartResult]: ...
    @winrt_commethod(17)
    def LicenseFetchAsync(self, licenseFetchDescriptor: win32more.Windows.Media.Protection.PlayReady.INDLicenseFetchDescriptor) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Protection.PlayReady.INDLicenseFetchResult]: ...
    @winrt_commethod(18)
    def ReRegistrationAsync(self, registrationCustomData: win32more.Windows.Media.Protection.PlayReady.INDCustomData) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(19)
    def Close(self) -> Void: ...
    RegistrationCompleted = event()
    ProximityDetectionCompleted = event()
    LicenseFetchCompleted = event()
    ReRegistrationNeeded = event()
    ClosedCaptionDataReceived = event()
class INDClientFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.INDClientFactory'
    _iid_ = Guid('{3e53dd62-fee8-451f-b0d4-f706cca3e037}')
    @winrt_commethod(6)
    def CreateInstance(self, downloadEngine: win32more.Windows.Media.Protection.PlayReady.INDDownloadEngine, streamParser: win32more.Windows.Media.Protection.PlayReady.INDStreamParser, pMessenger: win32more.Windows.Media.Protection.PlayReady.INDMessenger) -> win32more.Windows.Media.Protection.PlayReady.NDClient: ...
class INDClosedCaptionDataReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.INDClosedCaptionDataReceivedEventArgs'
    _iid_ = Guid('{4738d29f-c345-4649-8468-b8c5fc357190}')
    @winrt_commethod(6)
    def get_ClosedCaptionDataFormat(self) -> win32more.Windows.Media.Protection.PlayReady.NDClosedCaptionFormat: ...
    @winrt_commethod(7)
    def get_PresentationTimestamp(self) -> Int64: ...
    @winrt_commethod(8)
    def get_ClosedCaptionData(self) -> ReceiveArray[Byte]: ...
    ClosedCaptionData = property(get_ClosedCaptionData, None)
    ClosedCaptionDataFormat = property(get_ClosedCaptionDataFormat, None)
    PresentationTimestamp = property(get_PresentationTimestamp, None)
class INDCustomData(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.INDCustomData'
    _iid_ = Guid('{f5cb0fdc-2d09-4f19-b5e1-76a0b3ee9267}')
    @winrt_commethod(6)
    def get_CustomDataTypeID(self) -> ReceiveArray[Byte]: ...
    @winrt_commethod(7)
    def get_CustomData(self) -> ReceiveArray[Byte]: ...
    CustomData = property(get_CustomData, None)
    CustomDataTypeID = property(get_CustomDataTypeID, None)
class INDCustomDataFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.INDCustomDataFactory'
    _iid_ = Guid('{d65405ab-3424-4833-8c9a-af5fdeb22872}')
    @winrt_commethod(6)
    def CreateInstance(self, customDataTypeIDBytes: PassArray[Byte], customDataBytes: PassArray[Byte]) -> win32more.Windows.Media.Protection.PlayReady.NDCustomData: ...
class INDDownloadEngine(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.INDDownloadEngine'
    _iid_ = Guid('{2d223d65-c4b6-4438-8d46-b96e6d0fb21f}')
    @winrt_commethod(6)
    def Open(self, uri: win32more.Windows.Foundation.Uri, sessionIDBytes: PassArray[Byte]) -> Void: ...
    @winrt_commethod(7)
    def Pause(self) -> Void: ...
    @winrt_commethod(8)
    def Resume(self) -> Void: ...
    @winrt_commethod(9)
    def Close(self) -> Void: ...
    @winrt_commethod(10)
    def Seek(self, startPosition: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(11)
    def get_CanSeek(self) -> Boolean: ...
    @winrt_commethod(12)
    def get_BufferFullMinThresholdInSamples(self) -> UInt32: ...
    @winrt_commethod(13)
    def get_BufferFullMaxThresholdInSamples(self) -> UInt32: ...
    @winrt_commethod(14)
    def get_Notifier(self) -> win32more.Windows.Media.Protection.PlayReady.NDDownloadEngineNotifier: ...
    BufferFullMaxThresholdInSamples = property(get_BufferFullMaxThresholdInSamples, None)
    BufferFullMinThresholdInSamples = property(get_BufferFullMinThresholdInSamples, None)
    CanSeek = property(get_CanSeek, None)
    Notifier = property(get_Notifier, None)
class INDDownloadEngineNotifier(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.INDDownloadEngineNotifier'
    _iid_ = Guid('{d720b4d4-f4b8-4530-a809-9193a571e7fc}')
    @winrt_commethod(6)
    def OnStreamOpened(self) -> Void: ...
    @winrt_commethod(7)
    def OnPlayReadyObjectReceived(self, dataBytes: PassArray[Byte]) -> Void: ...
    @winrt_commethod(8)
    def OnContentIDReceived(self, licenseFetchDescriptor: win32more.Windows.Media.Protection.PlayReady.INDLicenseFetchDescriptor) -> Void: ...
    @winrt_commethod(9)
    def OnDataReceived(self, dataBytes: PassArray[Byte], bytesReceived: UInt32) -> Void: ...
    @winrt_commethod(10)
    def OnEndOfStream(self) -> Void: ...
    @winrt_commethod(11)
    def OnNetworkError(self) -> Void: ...
class INDLicenseFetchCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.INDLicenseFetchCompletedEventArgs'
    _iid_ = Guid('{1ee30a1a-11b2-4558-8865-e3a516922517}')
    @winrt_commethod(6)
    def get_ResponseCustomData(self) -> win32more.Windows.Media.Protection.PlayReady.INDCustomData: ...
    ResponseCustomData = property(get_ResponseCustomData, None)
class INDLicenseFetchDescriptor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.INDLicenseFetchDescriptor'
    _iid_ = Guid('{5498d33a-e686-4935-a567-7ca77ad20fa4}')
    @winrt_commethod(6)
    def get_ContentIDType(self) -> win32more.Windows.Media.Protection.PlayReady.NDContentIDType: ...
    @winrt_commethod(7)
    def get_ContentID(self) -> ReceiveArray[Byte]: ...
    @winrt_commethod(8)
    def get_LicenseFetchChallengeCustomData(self) -> win32more.Windows.Media.Protection.PlayReady.INDCustomData: ...
    @winrt_commethod(9)
    def put_LicenseFetchChallengeCustomData(self, licenseFetchChallengeCustomData: win32more.Windows.Media.Protection.PlayReady.INDCustomData) -> Void: ...
    ContentID = property(get_ContentID, None)
    ContentIDType = property(get_ContentIDType, None)
    LicenseFetchChallengeCustomData = property(get_LicenseFetchChallengeCustomData, put_LicenseFetchChallengeCustomData)
class INDLicenseFetchDescriptorFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.INDLicenseFetchDescriptorFactory'
    _iid_ = Guid('{d0031202-cfac-4f00-ae6a-97af80b848f2}')
    @winrt_commethod(6)
    def CreateInstance(self, contentIDType: win32more.Windows.Media.Protection.PlayReady.NDContentIDType, contentIDBytes: PassArray[Byte], licenseFetchChallengeCustomData: win32more.Windows.Media.Protection.PlayReady.INDCustomData) -> win32more.Windows.Media.Protection.PlayReady.NDLicenseFetchDescriptor: ...
class INDLicenseFetchResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.INDLicenseFetchResult'
    _iid_ = Guid('{21d39698-aa62-45ff-a5ff-8037e5433825}')
    @winrt_commethod(6)
    def get_ResponseCustomData(self) -> win32more.Windows.Media.Protection.PlayReady.INDCustomData: ...
    ResponseCustomData = property(get_ResponseCustomData, None)
class INDMessenger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.INDMessenger'
    _iid_ = Guid('{d42df95d-a75b-47bf-8249-bc83820da38a}')
    @winrt_commethod(6)
    def SendRegistrationRequestAsync(self, sessionIDBytes: PassArray[Byte], challengeDataBytes: PassArray[Byte]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Protection.PlayReady.INDSendResult]: ...
    @winrt_commethod(7)
    def SendProximityDetectionStartAsync(self, pdType: win32more.Windows.Media.Protection.PlayReady.NDProximityDetectionType, transmitterChannelBytes: PassArray[Byte], sessionIDBytes: PassArray[Byte], challengeDataBytes: PassArray[Byte]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Protection.PlayReady.INDSendResult]: ...
    @winrt_commethod(8)
    def SendProximityDetectionResponseAsync(self, pdType: win32more.Windows.Media.Protection.PlayReady.NDProximityDetectionType, transmitterChannelBytes: PassArray[Byte], sessionIDBytes: PassArray[Byte], responseDataBytes: PassArray[Byte]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Protection.PlayReady.INDSendResult]: ...
    @winrt_commethod(9)
    def SendLicenseFetchRequestAsync(self, sessionIDBytes: PassArray[Byte], challengeDataBytes: PassArray[Byte]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Protection.PlayReady.INDSendResult]: ...
class INDProximityDetectionCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.INDProximityDetectionCompletedEventArgs'
    _iid_ = Guid('{2a706328-da25-4f8c-9eb7-5d0fc3658bca}')
    @winrt_commethod(6)
    def get_ProximityDetectionRetryCount(self) -> UInt32: ...
    ProximityDetectionRetryCount = property(get_ProximityDetectionRetryCount, None)
class INDRegistrationCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.INDRegistrationCompletedEventArgs'
    _iid_ = Guid('{9e39b64d-ab5b-4905-acdc-787a77c6374d}')
    @winrt_commethod(6)
    def get_ResponseCustomData(self) -> win32more.Windows.Media.Protection.PlayReady.INDCustomData: ...
    @winrt_commethod(7)
    def get_TransmitterProperties(self) -> win32more.Windows.Media.Protection.PlayReady.INDTransmitterProperties: ...
    @winrt_commethod(8)
    def get_TransmitterCertificateAccepted(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_TransmitterCertificateAccepted(self, accept: Boolean) -> Void: ...
    ResponseCustomData = property(get_ResponseCustomData, None)
    TransmitterCertificateAccepted = property(get_TransmitterCertificateAccepted, put_TransmitterCertificateAccepted)
    TransmitterProperties = property(get_TransmitterProperties, None)
class INDSendResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.INDSendResult'
    _iid_ = Guid('{e3685517-a584-479d-90b7-d689c7bf7c80}')
    @winrt_commethod(6)
    def get_Response(self) -> ReceiveArray[Byte]: ...
    Response = property(get_Response, None)
class INDStartResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.INDStartResult'
    _iid_ = Guid('{79f6e96e-f50f-4015-8ba4-c2bc344ebd4e}')
    @winrt_commethod(6)
    def get_MediaStreamSource(self) -> win32more.Windows.Media.Core.MediaStreamSource: ...
    MediaStreamSource = property(get_MediaStreamSource, None)
class INDStorageFileHelper(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.INDStorageFileHelper'
    _iid_ = Guid('{d8f0bef8-91d2-4d47-a3f9-eaff4edb729f}')
    @winrt_commethod(6)
    def GetFileURLs(self, file: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
class INDStreamParser(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.INDStreamParser'
    _iid_ = Guid('{e0baa198-9796-41c9-8695-59437e67e66a}')
    @winrt_commethod(6)
    def ParseData(self, dataBytes: PassArray[Byte]) -> Void: ...
    @winrt_commethod(7)
    def GetStreamInformation(self, descriptor: win32more.Windows.Media.Core.IMediaStreamDescriptor, streamType: POINTER(win32more.Windows.Media.Protection.PlayReady.NDMediaStreamType)) -> UInt32: ...
    @winrt_commethod(8)
    def BeginOfStream(self) -> Void: ...
    @winrt_commethod(9)
    def EndOfStream(self) -> Void: ...
    @winrt_commethod(10)
    def get_Notifier(self) -> win32more.Windows.Media.Protection.PlayReady.NDStreamParserNotifier: ...
    Notifier = property(get_Notifier, None)
class INDStreamParserNotifier(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.INDStreamParserNotifier'
    _iid_ = Guid('{c167acd0-2ce6-426c-ace5-5e9275fea715}')
    @winrt_commethod(6)
    def OnContentIDReceived(self, licenseFetchDescriptor: win32more.Windows.Media.Protection.PlayReady.INDLicenseFetchDescriptor) -> Void: ...
    @winrt_commethod(7)
    def OnMediaStreamDescriptorCreated(self, audioStreamDescriptors: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Media.Core.AudioStreamDescriptor], videoStreamDescriptors: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Media.Core.VideoStreamDescriptor]) -> Void: ...
    @winrt_commethod(8)
    def OnSampleParsed(self, streamID: UInt32, streamType: win32more.Windows.Media.Protection.PlayReady.NDMediaStreamType, streamSample: win32more.Windows.Media.Core.MediaStreamSample, pts: Int64, ccFormat: win32more.Windows.Media.Protection.PlayReady.NDClosedCaptionFormat, ccDataBytes: PassArray[Byte]) -> Void: ...
    @winrt_commethod(9)
    def OnBeginSetupDecryptor(self, descriptor: win32more.Windows.Media.Core.IMediaStreamDescriptor, keyID: Guid, proBytes: PassArray[Byte]) -> Void: ...
class INDTCPMessengerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.INDTCPMessengerFactory'
    _iid_ = Guid('{7dd85cfe-1b99-4f68-8f82-8177f7cedf2b}')
    @winrt_commethod(6)
    def CreateInstance(self, remoteHostName: WinRT_String, remoteHostPort: UInt32) -> win32more.Windows.Media.Protection.PlayReady.NDTCPMessenger: ...
class INDTransmitterProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.INDTransmitterProperties'
    _iid_ = Guid('{e536af23-ac4f-4adc-8c66-4ff7c2702dd6}')
    @winrt_commethod(6)
    def get_CertificateType(self) -> win32more.Windows.Media.Protection.PlayReady.NDCertificateType: ...
    @winrt_commethod(7)
    def get_PlatformIdentifier(self) -> win32more.Windows.Media.Protection.PlayReady.NDCertificatePlatformID: ...
    @winrt_commethod(8)
    def get_SupportedFeatures(self) -> ReceiveArray[win32more.Windows.Media.Protection.PlayReady.NDCertificateFeature]: ...
    @winrt_commethod(9)
    def get_SecurityLevel(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_SecurityVersion(self) -> UInt32: ...
    @winrt_commethod(11)
    def get_ExpirationDate(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(12)
    def get_ClientID(self) -> ReceiveArray[Byte]: ...
    @winrt_commethod(13)
    def get_ModelDigest(self) -> ReceiveArray[Byte]: ...
    @winrt_commethod(14)
    def get_ModelManufacturerName(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def get_ModelName(self) -> WinRT_String: ...
    @winrt_commethod(16)
    def get_ModelNumber(self) -> WinRT_String: ...
    CertificateType = property(get_CertificateType, None)
    ClientID = property(get_ClientID, None)
    ExpirationDate = property(get_ExpirationDate, None)
    ModelDigest = property(get_ModelDigest, None)
    ModelManufacturerName = property(get_ModelManufacturerName, None)
    ModelName = property(get_ModelName, None)
    ModelNumber = property(get_ModelNumber, None)
    PlatformIdentifier = property(get_PlatformIdentifier, None)
    SecurityLevel = property(get_SecurityLevel, None)
    SecurityVersion = property(get_SecurityVersion, None)
    SupportedFeatures = property(get_SupportedFeatures, None)
class IPlayReadyContentHeader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyContentHeader'
    _iid_ = Guid('{9a438a6a-7f4c-452e-88bd-0148c6387a2c}')
    @winrt_commethod(6)
    def get_KeyId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_KeyIdString(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_LicenseAcquisitionUrl(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(9)
    def get_LicenseAcquisitionUserInterfaceUrl(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(10)
    def get_DomainServiceId(self) -> Guid: ...
    @winrt_commethod(11)
    def get_EncryptionType(self) -> win32more.Windows.Media.Protection.PlayReady.PlayReadyEncryptionAlgorithm: ...
    @winrt_commethod(12)
    def get_CustomAttributes(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_DecryptorSetup(self) -> win32more.Windows.Media.Protection.PlayReady.PlayReadyDecryptorSetup: ...
    @winrt_commethod(14)
    def GetSerializedHeader(self) -> ReceiveArray[Byte]: ...
    @winrt_commethod(15)
    def get_HeaderWithEmbeddedUpdates(self) -> win32more.Windows.Media.Protection.PlayReady.PlayReadyContentHeader: ...
    CustomAttributes = property(get_CustomAttributes, None)
    DecryptorSetup = property(get_DecryptorSetup, None)
    DomainServiceId = property(get_DomainServiceId, None)
    EncryptionType = property(get_EncryptionType, None)
    HeaderWithEmbeddedUpdates = property(get_HeaderWithEmbeddedUpdates, None)
    KeyId = property(get_KeyId, None)
    KeyIdString = property(get_KeyIdString, None)
    LicenseAcquisitionUrl = property(get_LicenseAcquisitionUrl, None)
    LicenseAcquisitionUserInterfaceUrl = property(get_LicenseAcquisitionUserInterfaceUrl, None)
class IPlayReadyContentHeader2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyContentHeader2'
    _iid_ = Guid('{359c79f4-2180-498c-965b-e754d875eab2}')
    @winrt_commethod(6)
    def get_KeyIds(self) -> ReceiveArray[Guid]: ...
    @winrt_commethod(7)
    def get_KeyIdStrings(self) -> ReceiveArray[WinRT_String]: ...
    KeyIdStrings = property(get_KeyIdStrings, None)
    KeyIds = property(get_KeyIds, None)
class IPlayReadyContentHeaderFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyContentHeaderFactory'
    _iid_ = Guid('{cb97c8ff-b758-4776-bf01-217a8b510b2c}')
    @winrt_commethod(6)
    def CreateInstanceFromWindowsMediaDrmHeader(self, headerBytes: PassArray[Byte], licenseAcquisitionUrl: win32more.Windows.Foundation.Uri, licenseAcquisitionUserInterfaceUrl: win32more.Windows.Foundation.Uri, customAttributes: WinRT_String, domainServiceId: Guid) -> win32more.Windows.Media.Protection.PlayReady.PlayReadyContentHeader: ...
    @winrt_commethod(7)
    def CreateInstanceFromComponents(self, contentKeyId: Guid, contentKeyIdString: WinRT_String, contentEncryptionAlgorithm: win32more.Windows.Media.Protection.PlayReady.PlayReadyEncryptionAlgorithm, licenseAcquisitionUrl: win32more.Windows.Foundation.Uri, licenseAcquisitionUserInterfaceUrl: win32more.Windows.Foundation.Uri, customAttributes: WinRT_String, domainServiceId: Guid) -> win32more.Windows.Media.Protection.PlayReady.PlayReadyContentHeader: ...
    @winrt_commethod(8)
    def CreateInstanceFromPlayReadyHeader(self, headerBytes: PassArray[Byte]) -> win32more.Windows.Media.Protection.PlayReady.PlayReadyContentHeader: ...
class IPlayReadyContentHeaderFactory2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyContentHeaderFactory2'
    _iid_ = Guid('{d1239cf5-ae6d-4778-97fd-6e3a2eeadbeb}')
    @winrt_commethod(6)
    def CreateInstanceFromComponents2(self, dwFlags: UInt32, contentKeyIds: PassArray[Guid], contentKeyIdStrings: PassArray[WinRT_String], contentEncryptionAlgorithm: win32more.Windows.Media.Protection.PlayReady.PlayReadyEncryptionAlgorithm, licenseAcquisitionUrl: win32more.Windows.Foundation.Uri, licenseAcquisitionUserInterfaceUrl: win32more.Windows.Foundation.Uri, customAttributes: WinRT_String, domainServiceId: Guid) -> win32more.Windows.Media.Protection.PlayReady.PlayReadyContentHeader: ...
class IPlayReadyContentResolver(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyContentResolver'
    _iid_ = Guid('{fbfd2523-906d-4982-a6b8-6849565a7ce8}')
    @winrt_commethod(6)
    def ServiceRequest(self, contentHeader: win32more.Windows.Media.Protection.PlayReady.PlayReadyContentHeader) -> win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest: ...
class IPlayReadyDomain(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyDomain'
    _iid_ = Guid('{adcc93ac-97e6-43ef-95e4-d7868f3b16a9}')
    @winrt_commethod(6)
    def get_AccountId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_ServiceId(self) -> Guid: ...
    @winrt_commethod(8)
    def get_Revision(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_FriendlyName(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_DomainJoinUrl(self) -> win32more.Windows.Foundation.Uri: ...
    AccountId = property(get_AccountId, None)
    DomainJoinUrl = property(get_DomainJoinUrl, None)
    FriendlyName = property(get_FriendlyName, None)
    Revision = property(get_Revision, None)
    ServiceId = property(get_ServiceId, None)
class IPlayReadyDomainIterableFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyDomainIterableFactory'
    _iid_ = Guid('{4df384ee-3121-4df3-a5e8-d0c24c0500fc}')
    @winrt_commethod(6)
    def CreateInstance(self, domainAccountId: Guid) -> win32more.Windows.Media.Protection.PlayReady.PlayReadyDomainIterable: ...
class IPlayReadyDomainJoinServiceRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyDomainJoinServiceRequest'
    _iid_ = Guid('{171b4a5a-405f-4739-b040-67b9f0c38758}')
    @winrt_commethod(6)
    def get_DomainAccountId(self) -> Guid: ...
    @winrt_commethod(7)
    def put_DomainAccountId(self, value: Guid) -> Void: ...
    @winrt_commethod(8)
    def get_DomainFriendlyName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_DomainFriendlyName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_DomainServiceId(self) -> Guid: ...
    @winrt_commethod(11)
    def put_DomainServiceId(self, value: Guid) -> Void: ...
    DomainAccountId = property(get_DomainAccountId, put_DomainAccountId)
    DomainFriendlyName = property(get_DomainFriendlyName, put_DomainFriendlyName)
    DomainServiceId = property(get_DomainServiceId, put_DomainServiceId)
class IPlayReadyDomainLeaveServiceRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyDomainLeaveServiceRequest'
    _iid_ = Guid('{062d58be-97ad-4917-aa03-46d4c252d464}')
    @winrt_commethod(6)
    def get_DomainAccountId(self) -> Guid: ...
    @winrt_commethod(7)
    def put_DomainAccountId(self, value: Guid) -> Void: ...
    @winrt_commethod(8)
    def get_DomainServiceId(self) -> Guid: ...
    @winrt_commethod(9)
    def put_DomainServiceId(self, value: Guid) -> Void: ...
    DomainAccountId = property(get_DomainAccountId, put_DomainAccountId)
    DomainServiceId = property(get_DomainServiceId, put_DomainServiceId)
class IPlayReadyITADataGenerator(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyITADataGenerator'
    _iid_ = Guid('{24446b8e-10b9-4530-b25b-901a8029a9b2}')
    @winrt_commethod(6)
    def GenerateData(self, guidCPSystemId: Guid, countOfStreams: UInt32, configuration: win32more.Windows.Foundation.Collections.IPropertySet, format: win32more.Windows.Media.Protection.PlayReady.PlayReadyITADataFormat) -> ReceiveArray[Byte]: ...
class IPlayReadyIndividualizationServiceRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyIndividualizationServiceRequest'
    _iid_ = Guid('{21f5a86b-008c-4611-ab2f-aaa6c69f0e24}')
class IPlayReadyLicense(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyLicense'
    _iid_ = Guid('{ee474c4e-fa3c-414d-a9f2-3ffc1ef832d4}')
    @winrt_commethod(6)
    def get_FullyEvaluated(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_UsableForPlay(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_ExpirationDate(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(9)
    def get_ExpireAfterFirstPlay(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_DomainAccountID(self) -> Guid: ...
    @winrt_commethod(11)
    def get_ChainDepth(self) -> UInt32: ...
    @winrt_commethod(12)
    def GetKIDAtChainDepth(self, chainDepth: UInt32) -> Guid: ...
    ChainDepth = property(get_ChainDepth, None)
    DomainAccountID = property(get_DomainAccountID, None)
    ExpirationDate = property(get_ExpirationDate, None)
    ExpireAfterFirstPlay = property(get_ExpireAfterFirstPlay, None)
    FullyEvaluated = property(get_FullyEvaluated, None)
    UsableForPlay = property(get_UsableForPlay, None)
class IPlayReadyLicense2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyLicense2'
    _iid_ = Guid('{30f4e7a7-d8e3-48a0-bcda-ff9f40530436}')
    @winrt_commethod(6)
    def get_SecureStopId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_SecurityLevel(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_InMemoryOnly(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_ExpiresInRealTime(self) -> Boolean: ...
    ExpiresInRealTime = property(get_ExpiresInRealTime, None)
    InMemoryOnly = property(get_InMemoryOnly, None)
    SecureStopId = property(get_SecureStopId, None)
    SecurityLevel = property(get_SecurityLevel, None)
class IPlayReadyLicenseAcquisitionServiceRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyLicenseAcquisitionServiceRequest'
    _iid_ = Guid('{5d85ff45-3e9f-4f48-93e1-9530c8d58c3e}')
    @winrt_commethod(6)
    def get_ContentHeader(self) -> win32more.Windows.Media.Protection.PlayReady.PlayReadyContentHeader: ...
    @winrt_commethod(7)
    def put_ContentHeader(self, value: win32more.Windows.Media.Protection.PlayReady.PlayReadyContentHeader) -> Void: ...
    @winrt_commethod(8)
    def get_DomainServiceId(self) -> Guid: ...
    @winrt_commethod(9)
    def put_DomainServiceId(self, value: Guid) -> Void: ...
    ContentHeader = property(get_ContentHeader, put_ContentHeader)
    DomainServiceId = property(get_DomainServiceId, put_DomainServiceId)
class IPlayReadyLicenseAcquisitionServiceRequest2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyLicenseAcquisitionServiceRequest2'
    _iid_ = Guid('{b7fa5eb5-fe0c-b225-bc60-5a9edd32ceb5}')
    @winrt_commethod(6)
    def get_SessionId(self) -> Guid: ...
    SessionId = property(get_SessionId, None)
class IPlayReadyLicenseAcquisitionServiceRequest3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyLicenseAcquisitionServiceRequest3'
    _iid_ = Guid('{394e5f4d-7f75-430d-b2e7-7f75f34b2d75}')
    @winrt_commethod(6)
    def CreateLicenseIterable(self, contentHeader: win32more.Windows.Media.Protection.PlayReady.PlayReadyContentHeader, fullyEvaluated: Boolean) -> win32more.Windows.Media.Protection.PlayReady.PlayReadyLicenseIterable: ...
class IPlayReadyLicenseIterableFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyLicenseIterableFactory'
    _iid_ = Guid('{d4179f08-0837-4978-8e68-be4293c8d7a6}')
    @winrt_commethod(6)
    def CreateInstance(self, contentHeader: win32more.Windows.Media.Protection.PlayReady.PlayReadyContentHeader, fullyEvaluated: Boolean) -> win32more.Windows.Media.Protection.PlayReady.PlayReadyLicenseIterable: ...
class IPlayReadyLicenseManagement(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyLicenseManagement'
    _iid_ = Guid('{aaeb2141-0957-4405-b892-8bf3ec5dadd9}')
    @winrt_commethod(6)
    def DeleteLicenses(self, contentHeader: win32more.Windows.Media.Protection.PlayReady.PlayReadyContentHeader) -> win32more.Windows.Foundation.IAsyncAction: ...
class IPlayReadyLicenseSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyLicenseSession'
    _iid_ = Guid('{a1723a39-87fa-4fdd-abbb-a9720e845259}')
    @winrt_commethod(6)
    def CreateLAServiceRequest(self) -> win32more.Windows.Media.Protection.PlayReady.IPlayReadyLicenseAcquisitionServiceRequest: ...
    @winrt_commethod(7)
    def ConfigureMediaProtectionManager(self, mpm: win32more.Windows.Media.Protection.MediaProtectionManager) -> Void: ...
class IPlayReadyLicenseSession2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyLicenseSession2'
    _iid_ = Guid('{4909be3a-3aed-4656-8ad7-ee0fd7799510}')
    @winrt_commethod(6)
    def CreateLicenseIterable(self, contentHeader: win32more.Windows.Media.Protection.PlayReady.PlayReadyContentHeader, fullyEvaluated: Boolean) -> win32more.Windows.Media.Protection.PlayReady.PlayReadyLicenseIterable: ...
class IPlayReadyLicenseSessionFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyLicenseSessionFactory'
    _iid_ = Guid('{62492699-6527-429e-98be-48d798ac2739}')
    @winrt_commethod(6)
    def CreateInstance(self, configuration: win32more.Windows.Foundation.Collections.IPropertySet) -> win32more.Windows.Media.Protection.PlayReady.PlayReadyLicenseSession: ...
class IPlayReadyMeteringReportServiceRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyMeteringReportServiceRequest'
    _iid_ = Guid('{c12b231c-0ecd-4f11-a185-1e24a4a67fb7}')
    @winrt_commethod(6)
    def get_MeteringCertificate(self) -> ReceiveArray[Byte]: ...
    @winrt_commethod(7)
    def put_MeteringCertificate(self, meteringCertBytes: PassArray[Byte]) -> Void: ...
    MeteringCertificate = property(get_MeteringCertificate, put_MeteringCertificate)
class IPlayReadyRevocationServiceRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyRevocationServiceRequest'
    _iid_ = Guid('{543d66ac-faf0-4560-84a5-0e4acec939e4}')
class IPlayReadySecureStopIterableFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadySecureStopIterableFactory'
    _iid_ = Guid('{5f1f0165-4214-4d9e-81eb-e89f9d294aee}')
    @winrt_commethod(6)
    def CreateInstance(self, publisherCertBytes: PassArray[Byte]) -> win32more.Windows.Media.Protection.PlayReady.PlayReadySecureStopIterable: ...
class IPlayReadySecureStopServiceRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadySecureStopServiceRequest'
    _iid_ = Guid('{b5501ee5-01bf-4401-9677-05630a6a4cc8}')
    @winrt_commethod(6)
    def get_SessionID(self) -> Guid: ...
    @winrt_commethod(7)
    def get_StartTime(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(8)
    def get_UpdateTime(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(9)
    def get_Stopped(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_PublisherCertificate(self) -> ReceiveArray[Byte]: ...
    PublisherCertificate = property(get_PublisherCertificate, None)
    SessionID = property(get_SessionID, None)
    StartTime = property(get_StartTime, None)
    Stopped = property(get_Stopped, None)
    UpdateTime = property(get_UpdateTime, None)
class IPlayReadySecureStopServiceRequestFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadySecureStopServiceRequestFactory'
    _iid_ = Guid('{0e448ac9-e67e-494e-9f49-6285438c76cf}')
    @winrt_commethod(6)
    def CreateInstance(self, publisherCertBytes: PassArray[Byte]) -> win32more.Windows.Media.Protection.PlayReady.PlayReadySecureStopServiceRequest: ...
    @winrt_commethod(7)
    def CreateInstanceFromSessionID(self, sessionID: Guid, publisherCertBytes: PassArray[Byte]) -> win32more.Windows.Media.Protection.PlayReady.PlayReadySecureStopServiceRequest: ...
class IPlayReadyServiceRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest'
    _iid_ = Guid('{8bad2836-a703-45a6-a180-76f3565aa725}')
    @winrt_commethod(6)
    def get_Uri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def put_Uri(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(8)
    def get_ResponseCustomData(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_ChallengeCustomData(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def put_ChallengeCustomData(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(11)
    def BeginServiceRequest(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(12)
    def NextServiceRequest(self) -> win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest: ...
    @winrt_commethod(13)
    def GenerateManualEnablingChallenge(self) -> win32more.Windows.Media.Protection.PlayReady.PlayReadySoapMessage: ...
    @winrt_commethod(14)
    def ProcessManualEnablingResponse(self, responseBytes: PassArray[Byte]) -> win32more.Windows.Foundation.HResult: ...
    ChallengeCustomData = property(get_ChallengeCustomData, put_ChallengeCustomData)
    ResponseCustomData = property(get_ResponseCustomData, None)
    Uri = property(get_Uri, put_Uri)
class IPlayReadySoapMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadySoapMessage'
    _iid_ = Guid('{b659fcb5-ce41-41ba-8a0d-61df5fffa139}')
    @winrt_commethod(6)
    def GetMessageBody(self) -> ReceiveArray[Byte]: ...
    @winrt_commethod(7)
    def get_MessageHeaders(self) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    @winrt_commethod(8)
    def get_Uri(self) -> win32more.Windows.Foundation.Uri: ...
    MessageHeaders = property(get_MessageHeaders, None)
    Uri = property(get_Uri, None)
class IPlayReadyStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyStatics'
    _iid_ = Guid('{5e69c00d-247c-469a-8f31-5c1a1571d9c6}')
    @winrt_commethod(6)
    def get_DomainJoinServiceRequestType(self) -> Guid: ...
    @winrt_commethod(7)
    def get_DomainLeaveServiceRequestType(self) -> Guid: ...
    @winrt_commethod(8)
    def get_IndividualizationServiceRequestType(self) -> Guid: ...
    @winrt_commethod(9)
    def get_LicenseAcquirerServiceRequestType(self) -> Guid: ...
    @winrt_commethod(10)
    def get_MeteringReportServiceRequestType(self) -> Guid: ...
    @winrt_commethod(11)
    def get_RevocationServiceRequestType(self) -> Guid: ...
    @winrt_commethod(12)
    def get_MediaProtectionSystemId(self) -> Guid: ...
    @winrt_commethod(13)
    def get_PlayReadySecurityVersion(self) -> UInt32: ...
    DomainJoinServiceRequestType = property(get_DomainJoinServiceRequestType, None)
    DomainLeaveServiceRequestType = property(get_DomainLeaveServiceRequestType, None)
    IndividualizationServiceRequestType = property(get_IndividualizationServiceRequestType, None)
    LicenseAcquirerServiceRequestType = property(get_LicenseAcquirerServiceRequestType, None)
    MediaProtectionSystemId = property(get_MediaProtectionSystemId, None)
    MeteringReportServiceRequestType = property(get_MeteringReportServiceRequestType, None)
    PlayReadySecurityVersion = property(get_PlayReadySecurityVersion, None)
    RevocationServiceRequestType = property(get_RevocationServiceRequestType, None)
class IPlayReadyStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyStatics2'
    _iid_ = Guid('{1f8d6a92-5f9a-423e-9466-b33969af7a3d}')
    @winrt_commethod(6)
    def get_PlayReadyCertificateSecurityLevel(self) -> UInt32: ...
    PlayReadyCertificateSecurityLevel = property(get_PlayReadyCertificateSecurityLevel, None)
class IPlayReadyStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyStatics3'
    _iid_ = Guid('{3fa33f71-2dd3-4bed-ae49-f7148e63e710}')
    @winrt_commethod(6)
    def get_SecureStopServiceRequestType(self) -> Guid: ...
    @winrt_commethod(7)
    def CheckSupportedHardware(self, hwdrmFeature: win32more.Windows.Media.Protection.PlayReady.PlayReadyHardwareDRMFeatures) -> Boolean: ...
    SecureStopServiceRequestType = property(get_SecureStopServiceRequestType, None)
class IPlayReadyStatics4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyStatics4'
    _iid_ = Guid('{50a91300-d824-4231-9d5e-78ef8844c7d7}')
    @winrt_commethod(6)
    def get_InputTrustAuthorityToCreate(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ProtectionSystemId(self) -> Guid: ...
    InputTrustAuthorityToCreate = property(get_InputTrustAuthorityToCreate, None)
    ProtectionSystemId = property(get_ProtectionSystemId, None)
class IPlayReadyStatics5(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyStatics5'
    _iid_ = Guid('{230a7075-dfa0-4f8e-a779-cefea9c6824b}')
    @winrt_commethod(6)
    def get_HardwareDRMDisabledAtTime(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(7)
    def get_HardwareDRMDisabledUntilTime(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(8)
    def ResetHardwareDRMDisabled(self) -> Void: ...
    HardwareDRMDisabledAtTime = property(get_HardwareDRMDisabledAtTime, None)
    HardwareDRMDisabledUntilTime = property(get_HardwareDRMDisabledUntilTime, None)
class NDCertificateFeature(Enum, Int32):
    Transmitter = 1
    Receiver = 2
    SharedCertificate = 3
    SecureClock = 4
    AntiRollBackClock = 5
    CRLS = 9
    PlayReady3Features = 13
class NDCertificatePlatformID(Enum, Int32):
    Windows = 0
    OSX = 1
    WindowsOnARM = 2
    WindowsMobile7 = 5
    iOSOnARM = 6
    XBoxOnPPC = 7
    WindowsPhone8OnARM = 8
    WindowsPhone8OnX86 = 9
    XboxOne = 10
    AndroidOnARM = 11
    WindowsPhone81OnARM = 12
    WindowsPhone81OnX86 = 13
class NDCertificateType(Enum, Int32):
    Unknown = 0
    PC = 1
    Device = 2
    Domain = 3
    Issuer = 4
    CrlSigner = 5
    Service = 6
    Silverlight = 7
    Application = 8
    Metering = 9
    KeyFileSigner = 10
    Server = 11
    LicenseSigner = 12
class NDClient(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Protection.PlayReady.INDClient
    _classid_ = 'Windows.Media.Protection.PlayReady.NDClient'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.Media.Protection.PlayReady.NDClient.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Media.Protection.PlayReady.INDClientFactory, downloadEngine: win32more.Windows.Media.Protection.PlayReady.INDDownloadEngine, streamParser: win32more.Windows.Media.Protection.PlayReady.INDStreamParser, pMessenger: win32more.Windows.Media.Protection.PlayReady.INDMessenger) -> win32more.Windows.Media.Protection.PlayReady.NDClient: ...
    @winrt_mixinmethod
    def add_RegistrationCompleted(self: win32more.Windows.Media.Protection.PlayReady.INDClient, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Protection.PlayReady.NDClient, win32more.Windows.Media.Protection.PlayReady.INDRegistrationCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RegistrationCompleted(self: win32more.Windows.Media.Protection.PlayReady.INDClient, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ProximityDetectionCompleted(self: win32more.Windows.Media.Protection.PlayReady.INDClient, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Protection.PlayReady.NDClient, win32more.Windows.Media.Protection.PlayReady.INDProximityDetectionCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ProximityDetectionCompleted(self: win32more.Windows.Media.Protection.PlayReady.INDClient, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_LicenseFetchCompleted(self: win32more.Windows.Media.Protection.PlayReady.INDClient, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Protection.PlayReady.NDClient, win32more.Windows.Media.Protection.PlayReady.INDLicenseFetchCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_LicenseFetchCompleted(self: win32more.Windows.Media.Protection.PlayReady.INDClient, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ReRegistrationNeeded(self: win32more.Windows.Media.Protection.PlayReady.INDClient, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Protection.PlayReady.NDClient, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ReRegistrationNeeded(self: win32more.Windows.Media.Protection.PlayReady.INDClient, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ClosedCaptionDataReceived(self: win32more.Windows.Media.Protection.PlayReady.INDClient, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Protection.PlayReady.NDClient, win32more.Windows.Media.Protection.PlayReady.INDClosedCaptionDataReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ClosedCaptionDataReceived(self: win32more.Windows.Media.Protection.PlayReady.INDClient, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def StartAsync(self: win32more.Windows.Media.Protection.PlayReady.INDClient, contentUrl: win32more.Windows.Foundation.Uri, startAsyncOptions: UInt32, registrationCustomData: win32more.Windows.Media.Protection.PlayReady.INDCustomData, licenseFetchDescriptor: win32more.Windows.Media.Protection.PlayReady.INDLicenseFetchDescriptor) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Protection.PlayReady.INDStartResult]: ...
    @winrt_mixinmethod
    def LicenseFetchAsync(self: win32more.Windows.Media.Protection.PlayReady.INDClient, licenseFetchDescriptor: win32more.Windows.Media.Protection.PlayReady.INDLicenseFetchDescriptor) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Protection.PlayReady.INDLicenseFetchResult]: ...
    @winrt_mixinmethod
    def ReRegistrationAsync(self: win32more.Windows.Media.Protection.PlayReady.INDClient, registrationCustomData: win32more.Windows.Media.Protection.PlayReady.INDCustomData) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Media.Protection.PlayReady.INDClient) -> Void: ...
    RegistrationCompleted = event()
    ProximityDetectionCompleted = event()
    LicenseFetchCompleted = event()
    ReRegistrationNeeded = event()
    ClosedCaptionDataReceived = event()
class NDClosedCaptionFormat(Enum, Int32):
    ATSC = 0
    SCTE20 = 1
    Unknown = 2
class NDContentIDType(Enum, Int32):
    KeyID = 1
    PlayReadyObject = 2
    Custom = 3
class NDCustomData(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Protection.PlayReady.INDCustomData
    _classid_ = 'Windows.Media.Protection.PlayReady.NDCustomData'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Media.Protection.PlayReady.NDCustomData.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Media.Protection.PlayReady.INDCustomDataFactory, customDataTypeIDBytes: PassArray[Byte], customDataBytes: PassArray[Byte]) -> win32more.Windows.Media.Protection.PlayReady.NDCustomData: ...
    @winrt_mixinmethod
    def get_CustomDataTypeID(self: win32more.Windows.Media.Protection.PlayReady.INDCustomData) -> ReceiveArray[Byte]: ...
    @winrt_mixinmethod
    def get_CustomData(self: win32more.Windows.Media.Protection.PlayReady.INDCustomData) -> ReceiveArray[Byte]: ...
    CustomData = property(get_CustomData, None)
    CustomDataTypeID = property(get_CustomDataTypeID, None)
class NDDownloadEngineNotifier(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Protection.PlayReady.INDDownloadEngineNotifier
    _classid_ = 'Windows.Media.Protection.PlayReady.NDDownloadEngineNotifier'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Media.Protection.PlayReady.NDDownloadEngineNotifier.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.Protection.PlayReady.NDDownloadEngineNotifier: ...
    @winrt_mixinmethod
    def OnStreamOpened(self: win32more.Windows.Media.Protection.PlayReady.INDDownloadEngineNotifier) -> Void: ...
    @winrt_mixinmethod
    def OnPlayReadyObjectReceived(self: win32more.Windows.Media.Protection.PlayReady.INDDownloadEngineNotifier, dataBytes: PassArray[Byte]) -> Void: ...
    @winrt_mixinmethod
    def OnContentIDReceived(self: win32more.Windows.Media.Protection.PlayReady.INDDownloadEngineNotifier, licenseFetchDescriptor: win32more.Windows.Media.Protection.PlayReady.INDLicenseFetchDescriptor) -> Void: ...
    @winrt_mixinmethod
    def OnDataReceived(self: win32more.Windows.Media.Protection.PlayReady.INDDownloadEngineNotifier, dataBytes: PassArray[Byte], bytesReceived: UInt32) -> Void: ...
    @winrt_mixinmethod
    def OnEndOfStream(self: win32more.Windows.Media.Protection.PlayReady.INDDownloadEngineNotifier) -> Void: ...
    @winrt_mixinmethod
    def OnNetworkError(self: win32more.Windows.Media.Protection.PlayReady.INDDownloadEngineNotifier) -> Void: ...
class NDLicenseFetchDescriptor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Protection.PlayReady.INDLicenseFetchDescriptor
    _classid_ = 'Windows.Media.Protection.PlayReady.NDLicenseFetchDescriptor'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.Media.Protection.PlayReady.NDLicenseFetchDescriptor.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Media.Protection.PlayReady.INDLicenseFetchDescriptorFactory, contentIDType: win32more.Windows.Media.Protection.PlayReady.NDContentIDType, contentIDBytes: PassArray[Byte], licenseFetchChallengeCustomData: win32more.Windows.Media.Protection.PlayReady.INDCustomData) -> win32more.Windows.Media.Protection.PlayReady.NDLicenseFetchDescriptor: ...
    @winrt_mixinmethod
    def get_ContentIDType(self: win32more.Windows.Media.Protection.PlayReady.INDLicenseFetchDescriptor) -> win32more.Windows.Media.Protection.PlayReady.NDContentIDType: ...
    @winrt_mixinmethod
    def get_ContentID(self: win32more.Windows.Media.Protection.PlayReady.INDLicenseFetchDescriptor) -> ReceiveArray[Byte]: ...
    @winrt_mixinmethod
    def get_LicenseFetchChallengeCustomData(self: win32more.Windows.Media.Protection.PlayReady.INDLicenseFetchDescriptor) -> win32more.Windows.Media.Protection.PlayReady.INDCustomData: ...
    @winrt_mixinmethod
    def put_LicenseFetchChallengeCustomData(self: win32more.Windows.Media.Protection.PlayReady.INDLicenseFetchDescriptor, licenseFetchChallengeCustomData: win32more.Windows.Media.Protection.PlayReady.INDCustomData) -> Void: ...
    ContentID = property(get_ContentID, None)
    ContentIDType = property(get_ContentIDType, None)
    LicenseFetchChallengeCustomData = property(get_LicenseFetchChallengeCustomData, put_LicenseFetchChallengeCustomData)
class NDMediaStreamType(Enum, Int32):
    Audio = 1
    Video = 2
class NDProximityDetectionType(Enum, Int32):
    UDP = 1
    TCP = 2
    TransportAgnostic = 4
class NDStartAsyncOptions(Enum, Int32):
    MutualAuthentication = 1
    WaitForLicenseDescriptor = 2
class NDStorageFileHelper(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Protection.PlayReady.INDStorageFileHelper
    _classid_ = 'Windows.Media.Protection.PlayReady.NDStorageFileHelper'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Media.Protection.PlayReady.NDStorageFileHelper.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.Protection.PlayReady.NDStorageFileHelper: ...
    @winrt_mixinmethod
    def GetFileURLs(self: win32more.Windows.Media.Protection.PlayReady.INDStorageFileHelper, file: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
class NDStreamParserNotifier(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Protection.PlayReady.INDStreamParserNotifier
    _classid_ = 'Windows.Media.Protection.PlayReady.NDStreamParserNotifier'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Media.Protection.PlayReady.NDStreamParserNotifier.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.Protection.PlayReady.NDStreamParserNotifier: ...
    @winrt_mixinmethod
    def OnContentIDReceived(self: win32more.Windows.Media.Protection.PlayReady.INDStreamParserNotifier, licenseFetchDescriptor: win32more.Windows.Media.Protection.PlayReady.INDLicenseFetchDescriptor) -> Void: ...
    @winrt_mixinmethod
    def OnMediaStreamDescriptorCreated(self: win32more.Windows.Media.Protection.PlayReady.INDStreamParserNotifier, audioStreamDescriptors: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Media.Core.AudioStreamDescriptor], videoStreamDescriptors: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Media.Core.VideoStreamDescriptor]) -> Void: ...
    @winrt_mixinmethod
    def OnSampleParsed(self: win32more.Windows.Media.Protection.PlayReady.INDStreamParserNotifier, streamID: UInt32, streamType: win32more.Windows.Media.Protection.PlayReady.NDMediaStreamType, streamSample: win32more.Windows.Media.Core.MediaStreamSample, pts: Int64, ccFormat: win32more.Windows.Media.Protection.PlayReady.NDClosedCaptionFormat, ccDataBytes: PassArray[Byte]) -> Void: ...
    @winrt_mixinmethod
    def OnBeginSetupDecryptor(self: win32more.Windows.Media.Protection.PlayReady.INDStreamParserNotifier, descriptor: win32more.Windows.Media.Core.IMediaStreamDescriptor, keyID: Guid, proBytes: PassArray[Byte]) -> Void: ...
class NDTCPMessenger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Protection.PlayReady.INDMessenger
    _classid_ = 'Windows.Media.Protection.PlayReady.NDTCPMessenger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Media.Protection.PlayReady.NDTCPMessenger.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Media.Protection.PlayReady.INDTCPMessengerFactory, remoteHostName: WinRT_String, remoteHostPort: UInt32) -> win32more.Windows.Media.Protection.PlayReady.NDTCPMessenger: ...
    @winrt_mixinmethod
    def SendRegistrationRequestAsync(self: win32more.Windows.Media.Protection.PlayReady.INDMessenger, sessionIDBytes: PassArray[Byte], challengeDataBytes: PassArray[Byte]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Protection.PlayReady.INDSendResult]: ...
    @winrt_mixinmethod
    def SendProximityDetectionStartAsync(self: win32more.Windows.Media.Protection.PlayReady.INDMessenger, pdType: win32more.Windows.Media.Protection.PlayReady.NDProximityDetectionType, transmitterChannelBytes: PassArray[Byte], sessionIDBytes: PassArray[Byte], challengeDataBytes: PassArray[Byte]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Protection.PlayReady.INDSendResult]: ...
    @winrt_mixinmethod
    def SendProximityDetectionResponseAsync(self: win32more.Windows.Media.Protection.PlayReady.INDMessenger, pdType: win32more.Windows.Media.Protection.PlayReady.NDProximityDetectionType, transmitterChannelBytes: PassArray[Byte], sessionIDBytes: PassArray[Byte], responseDataBytes: PassArray[Byte]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Protection.PlayReady.INDSendResult]: ...
    @winrt_mixinmethod
    def SendLicenseFetchRequestAsync(self: win32more.Windows.Media.Protection.PlayReady.INDMessenger, sessionIDBytes: PassArray[Byte], challengeDataBytes: PassArray[Byte]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Protection.PlayReady.INDSendResult]: ...
class PlayReadyContentHeader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Protection.PlayReady.IPlayReadyContentHeader
    _classid_ = 'Windows.Media.Protection.PlayReady.PlayReadyContentHeader'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Media.Protection.PlayReady.PlayReadyContentHeader.CreateInstanceFromPlayReadyHeader(*args))
        elif len(args) == 5:
            super().__init__(move=win32more.Windows.Media.Protection.PlayReady.PlayReadyContentHeader.CreateInstanceFromWindowsMediaDrmHeader(*args))
        elif len(args) == 7:
            super().__init__(move=win32more.Windows.Media.Protection.PlayReady.PlayReadyContentHeader.CreateInstanceFromComponents(*args))
        elif len(args) == 8:
            super().__init__(move=win32more.Windows.Media.Protection.PlayReady.PlayReadyContentHeader.CreateInstanceFromComponents2(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceFromPlayReadyHeader(cls: win32more.Windows.Media.Protection.PlayReady.IPlayReadyContentHeaderFactory, headerBytes: PassArray[Byte]) -> win32more.Windows.Media.Protection.PlayReady.PlayReadyContentHeader: ...
    @winrt_factorymethod
    def CreateInstanceFromWindowsMediaDrmHeader(cls: win32more.Windows.Media.Protection.PlayReady.IPlayReadyContentHeaderFactory, headerBytes: PassArray[Byte], licenseAcquisitionUrl: win32more.Windows.Foundation.Uri, licenseAcquisitionUserInterfaceUrl: win32more.Windows.Foundation.Uri, customAttributes: WinRT_String, domainServiceId: Guid) -> win32more.Windows.Media.Protection.PlayReady.PlayReadyContentHeader: ...
    @winrt_factorymethod
    def CreateInstanceFromComponents(cls: win32more.Windows.Media.Protection.PlayReady.IPlayReadyContentHeaderFactory, contentKeyId: Guid, contentKeyIdString: WinRT_String, contentEncryptionAlgorithm: win32more.Windows.Media.Protection.PlayReady.PlayReadyEncryptionAlgorithm, licenseAcquisitionUrl: win32more.Windows.Foundation.Uri, licenseAcquisitionUserInterfaceUrl: win32more.Windows.Foundation.Uri, customAttributes: WinRT_String, domainServiceId: Guid) -> win32more.Windows.Media.Protection.PlayReady.PlayReadyContentHeader: ...
    @winrt_factorymethod
    def CreateInstanceFromComponents2(cls: win32more.Windows.Media.Protection.PlayReady.IPlayReadyContentHeaderFactory2, dwFlags: UInt32, contentKeyIds: PassArray[Guid], contentKeyIdStrings: PassArray[WinRT_String], contentEncryptionAlgorithm: win32more.Windows.Media.Protection.PlayReady.PlayReadyEncryptionAlgorithm, licenseAcquisitionUrl: win32more.Windows.Foundation.Uri, licenseAcquisitionUserInterfaceUrl: win32more.Windows.Foundation.Uri, customAttributes: WinRT_String, domainServiceId: Guid) -> win32more.Windows.Media.Protection.PlayReady.PlayReadyContentHeader: ...
    @winrt_mixinmethod
    def get_KeyId(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyContentHeader) -> Guid: ...
    @winrt_mixinmethod
    def get_KeyIdString(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyContentHeader) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LicenseAcquisitionUrl(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyContentHeader) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_LicenseAcquisitionUserInterfaceUrl(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyContentHeader) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_DomainServiceId(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyContentHeader) -> Guid: ...
    @winrt_mixinmethod
    def get_EncryptionType(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyContentHeader) -> win32more.Windows.Media.Protection.PlayReady.PlayReadyEncryptionAlgorithm: ...
    @winrt_mixinmethod
    def get_CustomAttributes(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyContentHeader) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DecryptorSetup(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyContentHeader) -> win32more.Windows.Media.Protection.PlayReady.PlayReadyDecryptorSetup: ...
    @winrt_mixinmethod
    def GetSerializedHeader(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyContentHeader) -> ReceiveArray[Byte]: ...
    @winrt_mixinmethod
    def get_HeaderWithEmbeddedUpdates(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyContentHeader) -> win32more.Windows.Media.Protection.PlayReady.PlayReadyContentHeader: ...
    @winrt_mixinmethod
    def get_KeyIds(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyContentHeader2) -> ReceiveArray[Guid]: ...
    @winrt_mixinmethod
    def get_KeyIdStrings(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyContentHeader2) -> ReceiveArray[WinRT_String]: ...
    CustomAttributes = property(get_CustomAttributes, None)
    DecryptorSetup = property(get_DecryptorSetup, None)
    DomainServiceId = property(get_DomainServiceId, None)
    EncryptionType = property(get_EncryptionType, None)
    HeaderWithEmbeddedUpdates = property(get_HeaderWithEmbeddedUpdates, None)
    KeyId = property(get_KeyId, None)
    KeyIdString = property(get_KeyIdString, None)
    KeyIdStrings = property(get_KeyIdStrings, None)
    KeyIds = property(get_KeyIds, None)
    LicenseAcquisitionUrl = property(get_LicenseAcquisitionUrl, None)
    LicenseAcquisitionUserInterfaceUrl = property(get_LicenseAcquisitionUserInterfaceUrl, None)
class PlayReadyContentResolver(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.PlayReadyContentResolver'
    @winrt_classmethod
    def ServiceRequest(cls: win32more.Windows.Media.Protection.PlayReady.IPlayReadyContentResolver, contentHeader: win32more.Windows.Media.Protection.PlayReady.PlayReadyContentHeader) -> win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest: ...
class PlayReadyDecryptorSetup(Enum, Int32):
    Uninitialized = 0
    OnDemand = 1
class PlayReadyDomain(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Protection.PlayReady.IPlayReadyDomain
    _classid_ = 'Windows.Media.Protection.PlayReady.PlayReadyDomain'
    @winrt_mixinmethod
    def get_AccountId(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyDomain) -> Guid: ...
    @winrt_mixinmethod
    def get_ServiceId(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyDomain) -> Guid: ...
    @winrt_mixinmethod
    def get_Revision(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyDomain) -> UInt32: ...
    @winrt_mixinmethod
    def get_FriendlyName(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyDomain) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DomainJoinUrl(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyDomain) -> win32more.Windows.Foundation.Uri: ...
    AccountId = property(get_AccountId, None)
    DomainJoinUrl = property(get_DomainJoinUrl, None)
    FriendlyName = property(get_FriendlyName, None)
    Revision = property(get_Revision, None)
    ServiceId = property(get_ServiceId, None)
class PlayReadyDomainIterable(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[IterableProtocol[win32more.Windows.Media.Protection.PlayReady.IPlayReadyDomain]]
    default_interface: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Media.Protection.PlayReady.IPlayReadyDomain]
    _classid_ = 'Windows.Media.Protection.PlayReady.PlayReadyDomainIterable'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Media.Protection.PlayReady.PlayReadyDomainIterable.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Media.Protection.PlayReady.IPlayReadyDomainIterableFactory, domainAccountId: Guid) -> win32more.Windows.Media.Protection.PlayReady.PlayReadyDomainIterable: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Media.Protection.PlayReady.IPlayReadyDomain]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Media.Protection.PlayReady.IPlayReadyDomain]: ...
class PlayReadyDomainIterator(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Media.Protection.PlayReady.IPlayReadyDomain]
    _classid_ = 'Windows.Media.Protection.PlayReady.PlayReadyDomainIterator'
    @winrt_mixinmethod
    def get_Current(self: win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Media.Protection.PlayReady.IPlayReadyDomain]) -> win32more.Windows.Media.Protection.PlayReady.IPlayReadyDomain: ...
    @winrt_mixinmethod
    def get_HasCurrent(self: win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Media.Protection.PlayReady.IPlayReadyDomain]) -> Boolean: ...
    @winrt_mixinmethod
    def MoveNext(self: win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Media.Protection.PlayReady.IPlayReadyDomain]) -> Boolean: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Media.Protection.PlayReady.IPlayReadyDomain], items: FillArray[win32more.Windows.Media.Protection.PlayReady.IPlayReadyDomain]) -> UInt32: ...
    Current = property(get_Current, None)
    HasCurrent = property(get_HasCurrent, None)
class PlayReadyDomainJoinServiceRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Protection.PlayReady.IPlayReadyDomainJoinServiceRequest
    _classid_ = 'Windows.Media.Protection.PlayReady.PlayReadyDomainJoinServiceRequest'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Media.Protection.PlayReady.PlayReadyDomainJoinServiceRequest.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.Protection.PlayReady.PlayReadyDomainJoinServiceRequest: ...
    @winrt_mixinmethod
    def get_DomainAccountId(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyDomainJoinServiceRequest) -> Guid: ...
    @winrt_mixinmethod
    def put_DomainAccountId(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyDomainJoinServiceRequest, value: Guid) -> Void: ...
    @winrt_mixinmethod
    def get_DomainFriendlyName(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyDomainJoinServiceRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DomainFriendlyName(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyDomainJoinServiceRequest, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DomainServiceId(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyDomainJoinServiceRequest) -> Guid: ...
    @winrt_mixinmethod
    def put_DomainServiceId(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyDomainJoinServiceRequest, value: Guid) -> Void: ...
    @winrt_mixinmethod
    def get_Uri(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_Uri(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_ResponseCustomData(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ChallengeCustomData(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ChallengeCustomData(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def BeginServiceRequest(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def NextServiceRequest(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest: ...
    @winrt_mixinmethod
    def GenerateManualEnablingChallenge(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> win32more.Windows.Media.Protection.PlayReady.PlayReadySoapMessage: ...
    @winrt_mixinmethod
    def ProcessManualEnablingResponse(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest, responseBytes: PassArray[Byte]) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_ProtectionSystem(self: win32more.Windows.Media.Protection.IMediaProtectionServiceRequest) -> Guid: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.Media.Protection.IMediaProtectionServiceRequest) -> Guid: ...
    ChallengeCustomData = property(get_ChallengeCustomData, put_ChallengeCustomData)
    DomainAccountId = property(get_DomainAccountId, put_DomainAccountId)
    DomainFriendlyName = property(get_DomainFriendlyName, put_DomainFriendlyName)
    DomainServiceId = property(get_DomainServiceId, put_DomainServiceId)
    ProtectionSystem = property(get_ProtectionSystem, None)
    ResponseCustomData = property(get_ResponseCustomData, None)
    Type = property(get_Type, None)
    Uri = property(get_Uri, put_Uri)
class PlayReadyDomainLeaveServiceRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Protection.PlayReady.IPlayReadyDomainLeaveServiceRequest
    _classid_ = 'Windows.Media.Protection.PlayReady.PlayReadyDomainLeaveServiceRequest'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Media.Protection.PlayReady.PlayReadyDomainLeaveServiceRequest.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.Protection.PlayReady.PlayReadyDomainLeaveServiceRequest: ...
    @winrt_mixinmethod
    def get_DomainAccountId(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyDomainLeaveServiceRequest) -> Guid: ...
    @winrt_mixinmethod
    def put_DomainAccountId(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyDomainLeaveServiceRequest, value: Guid) -> Void: ...
    @winrt_mixinmethod
    def get_DomainServiceId(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyDomainLeaveServiceRequest) -> Guid: ...
    @winrt_mixinmethod
    def put_DomainServiceId(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyDomainLeaveServiceRequest, value: Guid) -> Void: ...
    @winrt_mixinmethod
    def get_Uri(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_Uri(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_ResponseCustomData(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ChallengeCustomData(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ChallengeCustomData(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def BeginServiceRequest(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def NextServiceRequest(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest: ...
    @winrt_mixinmethod
    def GenerateManualEnablingChallenge(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> win32more.Windows.Media.Protection.PlayReady.PlayReadySoapMessage: ...
    @winrt_mixinmethod
    def ProcessManualEnablingResponse(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest, responseBytes: PassArray[Byte]) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_ProtectionSystem(self: win32more.Windows.Media.Protection.IMediaProtectionServiceRequest) -> Guid: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.Media.Protection.IMediaProtectionServiceRequest) -> Guid: ...
    ChallengeCustomData = property(get_ChallengeCustomData, put_ChallengeCustomData)
    DomainAccountId = property(get_DomainAccountId, put_DomainAccountId)
    DomainServiceId = property(get_DomainServiceId, put_DomainServiceId)
    ProtectionSystem = property(get_ProtectionSystem, None)
    ResponseCustomData = property(get_ResponseCustomData, None)
    Type = property(get_Type, None)
    Uri = property(get_Uri, put_Uri)
class PlayReadyEncryptionAlgorithm(Enum, Int32):
    Unprotected = 0
    Aes128Ctr = 1
    Cocktail = 4
    Aes128Cbc = 5
    Unspecified = 65535
    Uninitialized = 2147483647
class PlayReadyHardwareDRMFeatures(Enum, Int32):
    HardwareDRM = 1
    HEVC = 2
    Aes128Cbc = 3
class PlayReadyITADataFormat(Enum, Int32):
    SerializedProperties = 0
    SerializedProperties_WithContentProtectionWrapper = 1
class PlayReadyITADataGenerator(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Protection.PlayReady.IPlayReadyITADataGenerator
    _classid_ = 'Windows.Media.Protection.PlayReady.PlayReadyITADataGenerator'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Media.Protection.PlayReady.PlayReadyITADataGenerator.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.Protection.PlayReady.PlayReadyITADataGenerator: ...
    @winrt_mixinmethod
    def GenerateData(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyITADataGenerator, guidCPSystemId: Guid, countOfStreams: UInt32, configuration: win32more.Windows.Foundation.Collections.IPropertySet, format: win32more.Windows.Media.Protection.PlayReady.PlayReadyITADataFormat) -> ReceiveArray[Byte]: ...
class PlayReadyIndividualizationServiceRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Protection.PlayReady.IPlayReadyIndividualizationServiceRequest
    _classid_ = 'Windows.Media.Protection.PlayReady.PlayReadyIndividualizationServiceRequest'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Media.Protection.PlayReady.PlayReadyIndividualizationServiceRequest.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.Protection.PlayReady.PlayReadyIndividualizationServiceRequest: ...
    @winrt_mixinmethod
    def get_Uri(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_Uri(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_ResponseCustomData(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ChallengeCustomData(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ChallengeCustomData(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def BeginServiceRequest(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def NextServiceRequest(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest: ...
    @winrt_mixinmethod
    def GenerateManualEnablingChallenge(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> win32more.Windows.Media.Protection.PlayReady.PlayReadySoapMessage: ...
    @winrt_mixinmethod
    def ProcessManualEnablingResponse(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest, responseBytes: PassArray[Byte]) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_ProtectionSystem(self: win32more.Windows.Media.Protection.IMediaProtectionServiceRequest) -> Guid: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.Media.Protection.IMediaProtectionServiceRequest) -> Guid: ...
    ChallengeCustomData = property(get_ChallengeCustomData, put_ChallengeCustomData)
    ProtectionSystem = property(get_ProtectionSystem, None)
    ResponseCustomData = property(get_ResponseCustomData, None)
    Type = property(get_Type, None)
    Uri = property(get_Uri, put_Uri)
class PlayReadyLicense(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Protection.PlayReady.IPlayReadyLicense
    _classid_ = 'Windows.Media.Protection.PlayReady.PlayReadyLicense'
    @winrt_mixinmethod
    def get_FullyEvaluated(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyLicense) -> Boolean: ...
    @winrt_mixinmethod
    def get_UsableForPlay(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyLicense) -> Boolean: ...
    @winrt_mixinmethod
    def get_ExpirationDate(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyLicense) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def get_ExpireAfterFirstPlay(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyLicense) -> UInt32: ...
    @winrt_mixinmethod
    def get_DomainAccountID(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyLicense) -> Guid: ...
    @winrt_mixinmethod
    def get_ChainDepth(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyLicense) -> UInt32: ...
    @winrt_mixinmethod
    def GetKIDAtChainDepth(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyLicense, chainDepth: UInt32) -> Guid: ...
    @winrt_mixinmethod
    def get_SecureStopId(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyLicense2) -> Guid: ...
    @winrt_mixinmethod
    def get_SecurityLevel(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyLicense2) -> UInt32: ...
    @winrt_mixinmethod
    def get_InMemoryOnly(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyLicense2) -> Boolean: ...
    @winrt_mixinmethod
    def get_ExpiresInRealTime(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyLicense2) -> Boolean: ...
    ChainDepth = property(get_ChainDepth, None)
    DomainAccountID = property(get_DomainAccountID, None)
    ExpirationDate = property(get_ExpirationDate, None)
    ExpireAfterFirstPlay = property(get_ExpireAfterFirstPlay, None)
    ExpiresInRealTime = property(get_ExpiresInRealTime, None)
    FullyEvaluated = property(get_FullyEvaluated, None)
    InMemoryOnly = property(get_InMemoryOnly, None)
    SecureStopId = property(get_SecureStopId, None)
    SecurityLevel = property(get_SecurityLevel, None)
    UsableForPlay = property(get_UsableForPlay, None)
class PlayReadyLicenseAcquisitionServiceRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Protection.PlayReady.IPlayReadyLicenseAcquisitionServiceRequest
    _classid_ = 'Windows.Media.Protection.PlayReady.PlayReadyLicenseAcquisitionServiceRequest'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Media.Protection.PlayReady.PlayReadyLicenseAcquisitionServiceRequest.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.Protection.PlayReady.PlayReadyLicenseAcquisitionServiceRequest: ...
    @winrt_mixinmethod
    def get_ContentHeader(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyLicenseAcquisitionServiceRequest) -> win32more.Windows.Media.Protection.PlayReady.PlayReadyContentHeader: ...
    @winrt_mixinmethod
    def put_ContentHeader(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyLicenseAcquisitionServiceRequest, value: win32more.Windows.Media.Protection.PlayReady.PlayReadyContentHeader) -> Void: ...
    @winrt_mixinmethod
    def get_DomainServiceId(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyLicenseAcquisitionServiceRequest) -> Guid: ...
    @winrt_mixinmethod
    def put_DomainServiceId(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyLicenseAcquisitionServiceRequest, value: Guid) -> Void: ...
    @winrt_mixinmethod
    def get_Uri(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_Uri(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_ResponseCustomData(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ChallengeCustomData(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ChallengeCustomData(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def BeginServiceRequest(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def NextServiceRequest(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest: ...
    @winrt_mixinmethod
    def GenerateManualEnablingChallenge(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> win32more.Windows.Media.Protection.PlayReady.PlayReadySoapMessage: ...
    @winrt_mixinmethod
    def ProcessManualEnablingResponse(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest, responseBytes: PassArray[Byte]) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_ProtectionSystem(self: win32more.Windows.Media.Protection.IMediaProtectionServiceRequest) -> Guid: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.Media.Protection.IMediaProtectionServiceRequest) -> Guid: ...
    @winrt_mixinmethod
    def get_SessionId(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyLicenseAcquisitionServiceRequest2) -> Guid: ...
    @winrt_mixinmethod
    def CreateLicenseIterable(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyLicenseAcquisitionServiceRequest3, contentHeader: win32more.Windows.Media.Protection.PlayReady.PlayReadyContentHeader, fullyEvaluated: Boolean) -> win32more.Windows.Media.Protection.PlayReady.PlayReadyLicenseIterable: ...
    ChallengeCustomData = property(get_ChallengeCustomData, put_ChallengeCustomData)
    ContentHeader = property(get_ContentHeader, put_ContentHeader)
    DomainServiceId = property(get_DomainServiceId, put_DomainServiceId)
    ProtectionSystem = property(get_ProtectionSystem, None)
    ResponseCustomData = property(get_ResponseCustomData, None)
    SessionId = property(get_SessionId, None)
    Type = property(get_Type, None)
    Uri = property(get_Uri, put_Uri)
class PlayReadyLicenseIterable(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[IterableProtocol[win32more.Windows.Media.Protection.PlayReady.IPlayReadyLicense]]
    default_interface: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Media.Protection.PlayReady.IPlayReadyLicense]
    _classid_ = 'Windows.Media.Protection.PlayReady.PlayReadyLicenseIterable'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Media.Protection.PlayReady.PlayReadyLicenseIterable.CreateInstance(*args))
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Media.Protection.PlayReady.PlayReadyLicenseIterable.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_overload
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.Protection.PlayReady.PlayReadyLicenseIterable: ...
    @CreateInstance.register
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Media.Protection.PlayReady.IPlayReadyLicenseIterableFactory, contentHeader: win32more.Windows.Media.Protection.PlayReady.PlayReadyContentHeader, fullyEvaluated: Boolean) -> win32more.Windows.Media.Protection.PlayReady.PlayReadyLicenseIterable: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Media.Protection.PlayReady.IPlayReadyLicense]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Media.Protection.PlayReady.IPlayReadyLicense]: ...
class PlayReadyLicenseIterator(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Media.Protection.PlayReady.IPlayReadyLicense]
    _classid_ = 'Windows.Media.Protection.PlayReady.PlayReadyLicenseIterator'
    @winrt_mixinmethod
    def get_Current(self: win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Media.Protection.PlayReady.IPlayReadyLicense]) -> win32more.Windows.Media.Protection.PlayReady.IPlayReadyLicense: ...
    @winrt_mixinmethod
    def get_HasCurrent(self: win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Media.Protection.PlayReady.IPlayReadyLicense]) -> Boolean: ...
    @winrt_mixinmethod
    def MoveNext(self: win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Media.Protection.PlayReady.IPlayReadyLicense]) -> Boolean: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Media.Protection.PlayReady.IPlayReadyLicense], items: FillArray[win32more.Windows.Media.Protection.PlayReady.IPlayReadyLicense]) -> UInt32: ...
    Current = property(get_Current, None)
    HasCurrent = property(get_HasCurrent, None)
class PlayReadyLicenseManagement(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.PlayReadyLicenseManagement'
    @winrt_classmethod
    def DeleteLicenses(cls: win32more.Windows.Media.Protection.PlayReady.IPlayReadyLicenseManagement, contentHeader: win32more.Windows.Media.Protection.PlayReady.PlayReadyContentHeader) -> win32more.Windows.Foundation.IAsyncAction: ...
class PlayReadyLicenseSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Protection.PlayReady.IPlayReadyLicenseSession
    _classid_ = 'Windows.Media.Protection.PlayReady.PlayReadyLicenseSession'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Media.Protection.PlayReady.PlayReadyLicenseSession.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Media.Protection.PlayReady.IPlayReadyLicenseSessionFactory, configuration: win32more.Windows.Foundation.Collections.IPropertySet) -> win32more.Windows.Media.Protection.PlayReady.PlayReadyLicenseSession: ...
    @winrt_mixinmethod
    def CreateLAServiceRequest(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyLicenseSession) -> win32more.Windows.Media.Protection.PlayReady.IPlayReadyLicenseAcquisitionServiceRequest: ...
    @winrt_mixinmethod
    def ConfigureMediaProtectionManager(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyLicenseSession, mpm: win32more.Windows.Media.Protection.MediaProtectionManager) -> Void: ...
    @winrt_mixinmethod
    def CreateLicenseIterable(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyLicenseSession2, contentHeader: win32more.Windows.Media.Protection.PlayReady.PlayReadyContentHeader, fullyEvaluated: Boolean) -> win32more.Windows.Media.Protection.PlayReady.PlayReadyLicenseIterable: ...
class PlayReadyMeteringReportServiceRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Protection.PlayReady.IPlayReadyMeteringReportServiceRequest
    _classid_ = 'Windows.Media.Protection.PlayReady.PlayReadyMeteringReportServiceRequest'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Media.Protection.PlayReady.PlayReadyMeteringReportServiceRequest.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.Protection.PlayReady.PlayReadyMeteringReportServiceRequest: ...
    @winrt_mixinmethod
    def get_MeteringCertificate(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyMeteringReportServiceRequest) -> ReceiveArray[Byte]: ...
    @winrt_mixinmethod
    def put_MeteringCertificate(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyMeteringReportServiceRequest, meteringCertBytes: PassArray[Byte]) -> Void: ...
    @winrt_mixinmethod
    def get_Uri(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_Uri(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_ResponseCustomData(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ChallengeCustomData(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ChallengeCustomData(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def BeginServiceRequest(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def NextServiceRequest(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest: ...
    @winrt_mixinmethod
    def GenerateManualEnablingChallenge(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> win32more.Windows.Media.Protection.PlayReady.PlayReadySoapMessage: ...
    @winrt_mixinmethod
    def ProcessManualEnablingResponse(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest, responseBytes: PassArray[Byte]) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_ProtectionSystem(self: win32more.Windows.Media.Protection.IMediaProtectionServiceRequest) -> Guid: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.Media.Protection.IMediaProtectionServiceRequest) -> Guid: ...
    ChallengeCustomData = property(get_ChallengeCustomData, put_ChallengeCustomData)
    MeteringCertificate = property(get_MeteringCertificate, put_MeteringCertificate)
    ProtectionSystem = property(get_ProtectionSystem, None)
    ResponseCustomData = property(get_ResponseCustomData, None)
    Type = property(get_Type, None)
    Uri = property(get_Uri, put_Uri)
class PlayReadyRevocationServiceRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Protection.PlayReady.IPlayReadyRevocationServiceRequest
    _classid_ = 'Windows.Media.Protection.PlayReady.PlayReadyRevocationServiceRequest'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Media.Protection.PlayReady.PlayReadyRevocationServiceRequest.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.Protection.PlayReady.PlayReadyRevocationServiceRequest: ...
    @winrt_mixinmethod
    def get_Uri(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_Uri(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_ResponseCustomData(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ChallengeCustomData(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ChallengeCustomData(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def BeginServiceRequest(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def NextServiceRequest(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest: ...
    @winrt_mixinmethod
    def GenerateManualEnablingChallenge(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> win32more.Windows.Media.Protection.PlayReady.PlayReadySoapMessage: ...
    @winrt_mixinmethod
    def ProcessManualEnablingResponse(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest, responseBytes: PassArray[Byte]) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_ProtectionSystem(self: win32more.Windows.Media.Protection.IMediaProtectionServiceRequest) -> Guid: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.Media.Protection.IMediaProtectionServiceRequest) -> Guid: ...
    ChallengeCustomData = property(get_ChallengeCustomData, put_ChallengeCustomData)
    ProtectionSystem = property(get_ProtectionSystem, None)
    ResponseCustomData = property(get_ResponseCustomData, None)
    Type = property(get_Type, None)
    Uri = property(get_Uri, put_Uri)
class PlayReadySecureStopIterable(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[IterableProtocol[win32more.Windows.Media.Protection.PlayReady.IPlayReadySecureStopServiceRequest]]
    default_interface: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Media.Protection.PlayReady.IPlayReadySecureStopServiceRequest]
    _classid_ = 'Windows.Media.Protection.PlayReady.PlayReadySecureStopIterable'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Media.Protection.PlayReady.PlayReadySecureStopIterable.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Media.Protection.PlayReady.IPlayReadySecureStopIterableFactory, publisherCertBytes: PassArray[Byte]) -> win32more.Windows.Media.Protection.PlayReady.PlayReadySecureStopIterable: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Media.Protection.PlayReady.IPlayReadySecureStopServiceRequest]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Media.Protection.PlayReady.IPlayReadySecureStopServiceRequest]: ...
class PlayReadySecureStopIterator(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Media.Protection.PlayReady.IPlayReadySecureStopServiceRequest]
    _classid_ = 'Windows.Media.Protection.PlayReady.PlayReadySecureStopIterator'
    @winrt_mixinmethod
    def get_Current(self: win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Media.Protection.PlayReady.IPlayReadySecureStopServiceRequest]) -> win32more.Windows.Media.Protection.PlayReady.IPlayReadySecureStopServiceRequest: ...
    @winrt_mixinmethod
    def get_HasCurrent(self: win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Media.Protection.PlayReady.IPlayReadySecureStopServiceRequest]) -> Boolean: ...
    @winrt_mixinmethod
    def MoveNext(self: win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Media.Protection.PlayReady.IPlayReadySecureStopServiceRequest]) -> Boolean: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Media.Protection.PlayReady.IPlayReadySecureStopServiceRequest], items: FillArray[win32more.Windows.Media.Protection.PlayReady.IPlayReadySecureStopServiceRequest]) -> UInt32: ...
    Current = property(get_Current, None)
    HasCurrent = property(get_HasCurrent, None)
class PlayReadySecureStopServiceRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Protection.PlayReady.IPlayReadySecureStopServiceRequest
    _classid_ = 'Windows.Media.Protection.PlayReady.PlayReadySecureStopServiceRequest'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Media.Protection.PlayReady.PlayReadySecureStopServiceRequest.CreateInstance(*args))
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Media.Protection.PlayReady.PlayReadySecureStopServiceRequest.CreateInstanceFromSessionID(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Media.Protection.PlayReady.IPlayReadySecureStopServiceRequestFactory, publisherCertBytes: PassArray[Byte]) -> win32more.Windows.Media.Protection.PlayReady.PlayReadySecureStopServiceRequest: ...
    @winrt_factorymethod
    def CreateInstanceFromSessionID(cls: win32more.Windows.Media.Protection.PlayReady.IPlayReadySecureStopServiceRequestFactory, sessionID: Guid, publisherCertBytes: PassArray[Byte]) -> win32more.Windows.Media.Protection.PlayReady.PlayReadySecureStopServiceRequest: ...
    @winrt_mixinmethod
    def get_SessionID(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadySecureStopServiceRequest) -> Guid: ...
    @winrt_mixinmethod
    def get_StartTime(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadySecureStopServiceRequest) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_UpdateTime(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadySecureStopServiceRequest) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_Stopped(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadySecureStopServiceRequest) -> Boolean: ...
    @winrt_mixinmethod
    def get_PublisherCertificate(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadySecureStopServiceRequest) -> ReceiveArray[Byte]: ...
    @winrt_mixinmethod
    def get_Uri(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_Uri(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_ResponseCustomData(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ChallengeCustomData(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ChallengeCustomData(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def BeginServiceRequest(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def NextServiceRequest(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest: ...
    @winrt_mixinmethod
    def GenerateManualEnablingChallenge(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> win32more.Windows.Media.Protection.PlayReady.PlayReadySoapMessage: ...
    @winrt_mixinmethod
    def ProcessManualEnablingResponse(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest, responseBytes: PassArray[Byte]) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_ProtectionSystem(self: win32more.Windows.Media.Protection.IMediaProtectionServiceRequest) -> Guid: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.Media.Protection.IMediaProtectionServiceRequest) -> Guid: ...
    ChallengeCustomData = property(get_ChallengeCustomData, put_ChallengeCustomData)
    ProtectionSystem = property(get_ProtectionSystem, None)
    PublisherCertificate = property(get_PublisherCertificate, None)
    ResponseCustomData = property(get_ResponseCustomData, None)
    SessionID = property(get_SessionID, None)
    StartTime = property(get_StartTime, None)
    Stopped = property(get_Stopped, None)
    Type = property(get_Type, None)
    UpdateTime = property(get_UpdateTime, None)
    Uri = property(get_Uri, put_Uri)
class PlayReadySoapMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Protection.PlayReady.IPlayReadySoapMessage
    _classid_ = 'Windows.Media.Protection.PlayReady.PlayReadySoapMessage'
    @winrt_mixinmethod
    def GetMessageBody(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadySoapMessage) -> ReceiveArray[Byte]: ...
    @winrt_mixinmethod
    def get_MessageHeaders(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadySoapMessage) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    @winrt_mixinmethod
    def get_Uri(self: win32more.Windows.Media.Protection.PlayReady.IPlayReadySoapMessage) -> win32more.Windows.Foundation.Uri: ...
    MessageHeaders = property(get_MessageHeaders, None)
    Uri = property(get_Uri, None)
class _PlayReadyStatics_Meta_(ComPtr.__class__):
    pass
class PlayReadyStatics(ComPtr, metaclass=_PlayReadyStatics_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.PlayReadyStatics'
    @winrt_classmethod
    def get_HardwareDRMDisabledAtTime(cls: win32more.Windows.Media.Protection.PlayReady.IPlayReadyStatics5) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_classmethod
    def get_HardwareDRMDisabledUntilTime(cls: win32more.Windows.Media.Protection.PlayReady.IPlayReadyStatics5) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_classmethod
    def ResetHardwareDRMDisabled(cls: win32more.Windows.Media.Protection.PlayReady.IPlayReadyStatics5) -> Void: ...
    @winrt_classmethod
    def get_InputTrustAuthorityToCreate(cls: win32more.Windows.Media.Protection.PlayReady.IPlayReadyStatics4) -> WinRT_String: ...
    @winrt_classmethod
    def get_ProtectionSystemId(cls: win32more.Windows.Media.Protection.PlayReady.IPlayReadyStatics4) -> Guid: ...
    @winrt_classmethod
    def get_SecureStopServiceRequestType(cls: win32more.Windows.Media.Protection.PlayReady.IPlayReadyStatics3) -> Guid: ...
    @winrt_classmethod
    def CheckSupportedHardware(cls: win32more.Windows.Media.Protection.PlayReady.IPlayReadyStatics3, hwdrmFeature: win32more.Windows.Media.Protection.PlayReady.PlayReadyHardwareDRMFeatures) -> Boolean: ...
    @winrt_classmethod
    def get_PlayReadyCertificateSecurityLevel(cls: win32more.Windows.Media.Protection.PlayReady.IPlayReadyStatics2) -> UInt32: ...
    @winrt_classmethod
    def get_DomainJoinServiceRequestType(cls: win32more.Windows.Media.Protection.PlayReady.IPlayReadyStatics) -> Guid: ...
    @winrt_classmethod
    def get_DomainLeaveServiceRequestType(cls: win32more.Windows.Media.Protection.PlayReady.IPlayReadyStatics) -> Guid: ...
    @winrt_classmethod
    def get_IndividualizationServiceRequestType(cls: win32more.Windows.Media.Protection.PlayReady.IPlayReadyStatics) -> Guid: ...
    @winrt_classmethod
    def get_LicenseAcquirerServiceRequestType(cls: win32more.Windows.Media.Protection.PlayReady.IPlayReadyStatics) -> Guid: ...
    @winrt_classmethod
    def get_MeteringReportServiceRequestType(cls: win32more.Windows.Media.Protection.PlayReady.IPlayReadyStatics) -> Guid: ...
    @winrt_classmethod
    def get_RevocationServiceRequestType(cls: win32more.Windows.Media.Protection.PlayReady.IPlayReadyStatics) -> Guid: ...
    @winrt_classmethod
    def get_MediaProtectionSystemId(cls: win32more.Windows.Media.Protection.PlayReady.IPlayReadyStatics) -> Guid: ...
    @winrt_classmethod
    def get_PlayReadySecurityVersion(cls: win32more.Windows.Media.Protection.PlayReady.IPlayReadyStatics) -> UInt32: ...
    _PlayReadyStatics_Meta_.DomainJoinServiceRequestType = property(get_DomainJoinServiceRequestType, None)
    _PlayReadyStatics_Meta_.DomainLeaveServiceRequestType = property(get_DomainLeaveServiceRequestType, None)
    _PlayReadyStatics_Meta_.HardwareDRMDisabledAtTime = property(get_HardwareDRMDisabledAtTime, None)
    _PlayReadyStatics_Meta_.HardwareDRMDisabledUntilTime = property(get_HardwareDRMDisabledUntilTime, None)
    _PlayReadyStatics_Meta_.IndividualizationServiceRequestType = property(get_IndividualizationServiceRequestType, None)
    _PlayReadyStatics_Meta_.InputTrustAuthorityToCreate = property(get_InputTrustAuthorityToCreate, None)
    _PlayReadyStatics_Meta_.LicenseAcquirerServiceRequestType = property(get_LicenseAcquirerServiceRequestType, None)
    _PlayReadyStatics_Meta_.MediaProtectionSystemId = property(get_MediaProtectionSystemId, None)
    _PlayReadyStatics_Meta_.MeteringReportServiceRequestType = property(get_MeteringReportServiceRequestType, None)
    _PlayReadyStatics_Meta_.PlayReadyCertificateSecurityLevel = property(get_PlayReadyCertificateSecurityLevel, None)
    _PlayReadyStatics_Meta_.PlayReadySecurityVersion = property(get_PlayReadySecurityVersion, None)
    _PlayReadyStatics_Meta_.ProtectionSystemId = property(get_ProtectionSystemId, None)
    _PlayReadyStatics_Meta_.RevocationServiceRequestType = property(get_RevocationServiceRequestType, None)
    _PlayReadyStatics_Meta_.SecureStopServiceRequestType = property(get_SecureStopServiceRequestType, None)


make_ready(__name__)
