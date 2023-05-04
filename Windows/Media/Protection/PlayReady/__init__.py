from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Media.Core
import Windows.Media.Protection
import Windows.Media.Protection.PlayReady
import Windows.Storage
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class INDClient(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.INDClient'
    _iid_ = Guid('{3bd6781b-61b8-46e2-99a5-8abcb6b9f7d6}')
    @winrt_commethod(6)
    def add_RegistrationCompleted(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Protection.PlayReady.NDClient, Windows.Media.Protection.PlayReady.INDRegistrationCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_RegistrationCompleted(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_ProximityDetectionCompleted(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Protection.PlayReady.NDClient, Windows.Media.Protection.PlayReady.INDProximityDetectionCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_ProximityDetectionCompleted(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_LicenseFetchCompleted(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Protection.PlayReady.NDClient, Windows.Media.Protection.PlayReady.INDLicenseFetchCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_LicenseFetchCompleted(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_ReRegistrationNeeded(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Protection.PlayReady.NDClient, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_ReRegistrationNeeded(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_ClosedCaptionDataReceived(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Protection.PlayReady.NDClient, Windows.Media.Protection.PlayReady.INDClosedCaptionDataReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_ClosedCaptionDataReceived(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def StartAsync(self, contentUrl: Windows.Foundation.Uri, startAsyncOptions: UInt32, registrationCustomData: Windows.Media.Protection.PlayReady.INDCustomData, licenseFetchDescriptor: Windows.Media.Protection.PlayReady.INDLicenseFetchDescriptor) -> Windows.Foundation.IAsyncOperation[Windows.Media.Protection.PlayReady.INDStartResult]: ...
    @winrt_commethod(17)
    def LicenseFetchAsync(self, licenseFetchDescriptor: Windows.Media.Protection.PlayReady.INDLicenseFetchDescriptor) -> Windows.Foundation.IAsyncOperation[Windows.Media.Protection.PlayReady.INDLicenseFetchResult]: ...
    @winrt_commethod(18)
    def ReRegistrationAsync(self, registrationCustomData: Windows.Media.Protection.PlayReady.INDCustomData) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(19)
    def Close(self) -> Void: ...
class INDClientFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.INDClientFactory'
    _iid_ = Guid('{3e53dd62-fee8-451f-b0d4-f706cca3e037}')
    @winrt_commethod(6)
    def CreateInstance(self, downloadEngine: Windows.Media.Protection.PlayReady.INDDownloadEngine, streamParser: Windows.Media.Protection.PlayReady.INDStreamParser, pMessenger: Windows.Media.Protection.PlayReady.INDMessenger) -> Windows.Media.Protection.PlayReady.NDClient: ...
class INDClosedCaptionDataReceivedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.INDClosedCaptionDataReceivedEventArgs'
    _iid_ = Guid('{4738d29f-c345-4649-8468-b8c5fc357190}')
    @winrt_commethod(6)
    def get_ClosedCaptionDataFormat(self) -> Windows.Media.Protection.PlayReady.NDClosedCaptionFormat: ...
    @winrt_commethod(7)
    def get_PresentationTimestamp(self) -> Int64: ...
    @winrt_commethod(8)
    def get_ClosedCaptionData(self) -> c_char_p_no: ...
    ClosedCaptionDataFormat = property(get_ClosedCaptionDataFormat, None)
    PresentationTimestamp = property(get_PresentationTimestamp, None)
    ClosedCaptionData = property(get_ClosedCaptionData, None)
class INDCustomData(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.INDCustomData'
    _iid_ = Guid('{f5cb0fdc-2d09-4f19-b5e1-76a0b3ee9267}')
    @winrt_commethod(6)
    def get_CustomDataTypeID(self) -> c_char_p_no: ...
    @winrt_commethod(7)
    def get_CustomData(self) -> c_char_p_no: ...
    CustomDataTypeID = property(get_CustomDataTypeID, None)
    CustomData = property(get_CustomData, None)
class INDCustomDataFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.INDCustomDataFactory'
    _iid_ = Guid('{d65405ab-3424-4833-8c9a-af5fdeb22872}')
    @winrt_commethod(6)
    def CreateInstance(self, customDataTypeIDBytes: c_char_p_no, customDataBytes: c_char_p_no) -> Windows.Media.Protection.PlayReady.NDCustomData: ...
class INDDownloadEngine(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.INDDownloadEngine'
    _iid_ = Guid('{2d223d65-c4b6-4438-8d46-b96e6d0fb21f}')
    @winrt_commethod(6)
    def Open(self, uri: Windows.Foundation.Uri, sessionIDBytes: c_char_p_no) -> Void: ...
    @winrt_commethod(7)
    def Pause(self) -> Void: ...
    @winrt_commethod(8)
    def Resume(self) -> Void: ...
    @winrt_commethod(9)
    def Close(self) -> Void: ...
    @winrt_commethod(10)
    def Seek(self, startPosition: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(11)
    def get_CanSeek(self) -> Boolean: ...
    @winrt_commethod(12)
    def get_BufferFullMinThresholdInSamples(self) -> UInt32: ...
    @winrt_commethod(13)
    def get_BufferFullMaxThresholdInSamples(self) -> UInt32: ...
    @winrt_commethod(14)
    def get_Notifier(self) -> Windows.Media.Protection.PlayReady.NDDownloadEngineNotifier: ...
    CanSeek = property(get_CanSeek, None)
    BufferFullMinThresholdInSamples = property(get_BufferFullMinThresholdInSamples, None)
    BufferFullMaxThresholdInSamples = property(get_BufferFullMaxThresholdInSamples, None)
    Notifier = property(get_Notifier, None)
class INDDownloadEngineNotifier(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.INDDownloadEngineNotifier'
    _iid_ = Guid('{d720b4d4-f4b8-4530-a809-9193a571e7fc}')
    @winrt_commethod(6)
    def OnStreamOpened(self) -> Void: ...
    @winrt_commethod(7)
    def OnPlayReadyObjectReceived(self, dataBytes: c_char_p_no) -> Void: ...
    @winrt_commethod(8)
    def OnContentIDReceived(self, licenseFetchDescriptor: Windows.Media.Protection.PlayReady.INDLicenseFetchDescriptor) -> Void: ...
    @winrt_commethod(9)
    def OnDataReceived(self, dataBytes: c_char_p_no, bytesReceived: UInt32) -> Void: ...
    @winrt_commethod(10)
    def OnEndOfStream(self) -> Void: ...
    @winrt_commethod(11)
    def OnNetworkError(self) -> Void: ...
class INDLicenseFetchCompletedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.INDLicenseFetchCompletedEventArgs'
    _iid_ = Guid('{1ee30a1a-11b2-4558-8865-e3a516922517}')
    @winrt_commethod(6)
    def get_ResponseCustomData(self) -> Windows.Media.Protection.PlayReady.INDCustomData: ...
    ResponseCustomData = property(get_ResponseCustomData, None)
class INDLicenseFetchDescriptor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.INDLicenseFetchDescriptor'
    _iid_ = Guid('{5498d33a-e686-4935-a567-7ca77ad20fa4}')
    @winrt_commethod(6)
    def get_ContentIDType(self) -> Windows.Media.Protection.PlayReady.NDContentIDType: ...
    @winrt_commethod(7)
    def get_ContentID(self) -> c_char_p_no: ...
    @winrt_commethod(8)
    def get_LicenseFetchChallengeCustomData(self) -> Windows.Media.Protection.PlayReady.INDCustomData: ...
    @winrt_commethod(9)
    def put_LicenseFetchChallengeCustomData(self, licenseFetchChallengeCustomData: Windows.Media.Protection.PlayReady.INDCustomData) -> Void: ...
    ContentIDType = property(get_ContentIDType, None)
    ContentID = property(get_ContentID, None)
    LicenseFetchChallengeCustomData = property(get_LicenseFetchChallengeCustomData, put_LicenseFetchChallengeCustomData)
class INDLicenseFetchDescriptorFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.INDLicenseFetchDescriptorFactory'
    _iid_ = Guid('{d0031202-cfac-4f00-ae6a-97af80b848f2}')
    @winrt_commethod(6)
    def CreateInstance(self, contentIDType: Windows.Media.Protection.PlayReady.NDContentIDType, contentIDBytes: c_char_p_no, licenseFetchChallengeCustomData: Windows.Media.Protection.PlayReady.INDCustomData) -> Windows.Media.Protection.PlayReady.NDLicenseFetchDescriptor: ...
class INDLicenseFetchResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.INDLicenseFetchResult'
    _iid_ = Guid('{21d39698-aa62-45ff-a5ff-8037e5433825}')
    @winrt_commethod(6)
    def get_ResponseCustomData(self) -> Windows.Media.Protection.PlayReady.INDCustomData: ...
    ResponseCustomData = property(get_ResponseCustomData, None)
class INDMessenger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.INDMessenger'
    _iid_ = Guid('{d42df95d-a75b-47bf-8249-bc83820da38a}')
    @winrt_commethod(6)
    def SendRegistrationRequestAsync(self, sessionIDBytes: c_char_p_no, challengeDataBytes: c_char_p_no) -> Windows.Foundation.IAsyncOperation[Windows.Media.Protection.PlayReady.INDSendResult]: ...
    @winrt_commethod(7)
    def SendProximityDetectionStartAsync(self, pdType: Windows.Media.Protection.PlayReady.NDProximityDetectionType, transmitterChannelBytes: c_char_p_no, sessionIDBytes: c_char_p_no, challengeDataBytes: c_char_p_no) -> Windows.Foundation.IAsyncOperation[Windows.Media.Protection.PlayReady.INDSendResult]: ...
    @winrt_commethod(8)
    def SendProximityDetectionResponseAsync(self, pdType: Windows.Media.Protection.PlayReady.NDProximityDetectionType, transmitterChannelBytes: c_char_p_no, sessionIDBytes: c_char_p_no, responseDataBytes: c_char_p_no) -> Windows.Foundation.IAsyncOperation[Windows.Media.Protection.PlayReady.INDSendResult]: ...
    @winrt_commethod(9)
    def SendLicenseFetchRequestAsync(self, sessionIDBytes: c_char_p_no, challengeDataBytes: c_char_p_no) -> Windows.Foundation.IAsyncOperation[Windows.Media.Protection.PlayReady.INDSendResult]: ...
class INDProximityDetectionCompletedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.INDProximityDetectionCompletedEventArgs'
    _iid_ = Guid('{2a706328-da25-4f8c-9eb7-5d0fc3658bca}')
    @winrt_commethod(6)
    def get_ProximityDetectionRetryCount(self) -> UInt32: ...
    ProximityDetectionRetryCount = property(get_ProximityDetectionRetryCount, None)
class INDRegistrationCompletedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.INDRegistrationCompletedEventArgs'
    _iid_ = Guid('{9e39b64d-ab5b-4905-acdc-787a77c6374d}')
    @winrt_commethod(6)
    def get_ResponseCustomData(self) -> Windows.Media.Protection.PlayReady.INDCustomData: ...
    @winrt_commethod(7)
    def get_TransmitterProperties(self) -> Windows.Media.Protection.PlayReady.INDTransmitterProperties: ...
    @winrt_commethod(8)
    def get_TransmitterCertificateAccepted(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_TransmitterCertificateAccepted(self, accept: Boolean) -> Void: ...
    ResponseCustomData = property(get_ResponseCustomData, None)
    TransmitterProperties = property(get_TransmitterProperties, None)
    TransmitterCertificateAccepted = property(get_TransmitterCertificateAccepted, put_TransmitterCertificateAccepted)
class INDSendResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.INDSendResult'
    _iid_ = Guid('{e3685517-a584-479d-90b7-d689c7bf7c80}')
    @winrt_commethod(6)
    def get_Response(self) -> c_char_p_no: ...
    Response = property(get_Response, None)
class INDStartResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.INDStartResult'
    _iid_ = Guid('{79f6e96e-f50f-4015-8ba4-c2bc344ebd4e}')
    @winrt_commethod(6)
    def get_MediaStreamSource(self) -> Windows.Media.Core.MediaStreamSource: ...
    MediaStreamSource = property(get_MediaStreamSource, None)
class INDStorageFileHelper(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.INDStorageFileHelper'
    _iid_ = Guid('{d8f0bef8-91d2-4d47-a3f9-eaff4edb729f}')
    @winrt_commethod(6)
    def GetFileURLs(self, file: Windows.Storage.IStorageFile) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
class INDStreamParser(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.INDStreamParser'
    _iid_ = Guid('{e0baa198-9796-41c9-8695-59437e67e66a}')
    @winrt_commethod(6)
    def ParseData(self, dataBytes: c_char_p_no) -> Void: ...
    @winrt_commethod(7)
    def GetStreamInformation(self, descriptor: Windows.Media.Core.IMediaStreamDescriptor, streamType: POINTER(Windows.Media.Protection.PlayReady.NDMediaStreamType)) -> UInt32: ...
    @winrt_commethod(8)
    def BeginOfStream(self) -> Void: ...
    @winrt_commethod(9)
    def EndOfStream(self) -> Void: ...
    @winrt_commethod(10)
    def get_Notifier(self) -> Windows.Media.Protection.PlayReady.NDStreamParserNotifier: ...
    Notifier = property(get_Notifier, None)
class INDStreamParserNotifier(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.INDStreamParserNotifier'
    _iid_ = Guid('{c167acd0-2ce6-426c-ace5-5e9275fea715}')
    @winrt_commethod(6)
    def OnContentIDReceived(self, licenseFetchDescriptor: Windows.Media.Protection.PlayReady.INDLicenseFetchDescriptor) -> Void: ...
    @winrt_commethod(7)
    def OnMediaStreamDescriptorCreated(self, audioStreamDescriptors: Windows.Foundation.Collections.IVector[Windows.Media.Core.AudioStreamDescriptor], videoStreamDescriptors: Windows.Foundation.Collections.IVector[Windows.Media.Core.VideoStreamDescriptor]) -> Void: ...
    @winrt_commethod(8)
    def OnSampleParsed(self, streamID: UInt32, streamType: Windows.Media.Protection.PlayReady.NDMediaStreamType, streamSample: Windows.Media.Core.MediaStreamSample, pts: Int64, ccFormat: Windows.Media.Protection.PlayReady.NDClosedCaptionFormat, ccDataBytes: c_char_p_no) -> Void: ...
    @winrt_commethod(9)
    def OnBeginSetupDecryptor(self, descriptor: Windows.Media.Core.IMediaStreamDescriptor, keyID: Guid, proBytes: c_char_p_no) -> Void: ...
class INDTCPMessengerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.INDTCPMessengerFactory'
    _iid_ = Guid('{7dd85cfe-1b99-4f68-8f82-8177f7cedf2b}')
    @winrt_commethod(6)
    def CreateInstance(self, remoteHostName: WinRT_String, remoteHostPort: UInt32) -> Windows.Media.Protection.PlayReady.NDTCPMessenger: ...
class INDTransmitterProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.INDTransmitterProperties'
    _iid_ = Guid('{e536af23-ac4f-4adc-8c66-4ff7c2702dd6}')
    @winrt_commethod(6)
    def get_CertificateType(self) -> Windows.Media.Protection.PlayReady.NDCertificateType: ...
    @winrt_commethod(7)
    def get_PlatformIdentifier(self) -> Windows.Media.Protection.PlayReady.NDCertificatePlatformID: ...
    @winrt_commethod(8)
    def get_SupportedFeatures(self) -> POINTER(Windows.Media.Protection.PlayReady.NDCertificateFeature): ...
    @winrt_commethod(9)
    def get_SecurityLevel(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_SecurityVersion(self) -> UInt32: ...
    @winrt_commethod(11)
    def get_ExpirationDate(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(12)
    def get_ClientID(self) -> c_char_p_no: ...
    @winrt_commethod(13)
    def get_ModelDigest(self) -> c_char_p_no: ...
    @winrt_commethod(14)
    def get_ModelManufacturerName(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def get_ModelName(self) -> WinRT_String: ...
    @winrt_commethod(16)
    def get_ModelNumber(self) -> WinRT_String: ...
    CertificateType = property(get_CertificateType, None)
    PlatformIdentifier = property(get_PlatformIdentifier, None)
    SupportedFeatures = property(get_SupportedFeatures, None)
    SecurityLevel = property(get_SecurityLevel, None)
    SecurityVersion = property(get_SecurityVersion, None)
    ExpirationDate = property(get_ExpirationDate, None)
    ClientID = property(get_ClientID, None)
    ModelDigest = property(get_ModelDigest, None)
    ModelManufacturerName = property(get_ModelManufacturerName, None)
    ModelName = property(get_ModelName, None)
    ModelNumber = property(get_ModelNumber, None)
class IPlayReadyContentHeader(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyContentHeader'
    _iid_ = Guid('{9a438a6a-7f4c-452e-88bd-0148c6387a2c}')
    @winrt_commethod(6)
    def get_KeyId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_KeyIdString(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_LicenseAcquisitionUrl(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(9)
    def get_LicenseAcquisitionUserInterfaceUrl(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(10)
    def get_DomainServiceId(self) -> Guid: ...
    @winrt_commethod(11)
    def get_EncryptionType(self) -> Windows.Media.Protection.PlayReady.PlayReadyEncryptionAlgorithm: ...
    @winrt_commethod(12)
    def get_CustomAttributes(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_DecryptorSetup(self) -> Windows.Media.Protection.PlayReady.PlayReadyDecryptorSetup: ...
    @winrt_commethod(14)
    def GetSerializedHeader(self) -> c_char_p_no: ...
    @winrt_commethod(15)
    def get_HeaderWithEmbeddedUpdates(self) -> Windows.Media.Protection.PlayReady.PlayReadyContentHeader: ...
    KeyId = property(get_KeyId, None)
    KeyIdString = property(get_KeyIdString, None)
    LicenseAcquisitionUrl = property(get_LicenseAcquisitionUrl, None)
    LicenseAcquisitionUserInterfaceUrl = property(get_LicenseAcquisitionUserInterfaceUrl, None)
    DomainServiceId = property(get_DomainServiceId, None)
    EncryptionType = property(get_EncryptionType, None)
    CustomAttributes = property(get_CustomAttributes, None)
    DecryptorSetup = property(get_DecryptorSetup, None)
    HeaderWithEmbeddedUpdates = property(get_HeaderWithEmbeddedUpdates, None)
class IPlayReadyContentHeader2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyContentHeader2'
    _iid_ = Guid('{359c79f4-2180-498c-965b-e754d875eab2}')
    @winrt_commethod(6)
    def get_KeyIds(self) -> POINTER(Guid): ...
    @winrt_commethod(7)
    def get_KeyIdStrings(self) -> POINTER(WinRT_String): ...
    KeyIds = property(get_KeyIds, None)
    KeyIdStrings = property(get_KeyIdStrings, None)
class IPlayReadyContentHeaderFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyContentHeaderFactory'
    _iid_ = Guid('{cb97c8ff-b758-4776-bf01-217a8b510b2c}')
    @winrt_commethod(6)
    def CreateInstanceFromWindowsMediaDrmHeader(self, headerBytes: c_char_p_no, licenseAcquisitionUrl: Windows.Foundation.Uri, licenseAcquisitionUserInterfaceUrl: Windows.Foundation.Uri, customAttributes: WinRT_String, domainServiceId: Guid) -> Windows.Media.Protection.PlayReady.PlayReadyContentHeader: ...
    @winrt_commethod(7)
    def CreateInstanceFromComponents(self, contentKeyId: Guid, contentKeyIdString: WinRT_String, contentEncryptionAlgorithm: Windows.Media.Protection.PlayReady.PlayReadyEncryptionAlgorithm, licenseAcquisitionUrl: Windows.Foundation.Uri, licenseAcquisitionUserInterfaceUrl: Windows.Foundation.Uri, customAttributes: WinRT_String, domainServiceId: Guid) -> Windows.Media.Protection.PlayReady.PlayReadyContentHeader: ...
    @winrt_commethod(8)
    def CreateInstanceFromPlayReadyHeader(self, headerBytes: c_char_p_no) -> Windows.Media.Protection.PlayReady.PlayReadyContentHeader: ...
class IPlayReadyContentHeaderFactory2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyContentHeaderFactory2'
    _iid_ = Guid('{d1239cf5-ae6d-4778-97fd-6e3a2eeadbeb}')
    @winrt_commethod(6)
    def CreateInstanceFromComponents2(self, dwFlags: UInt32, contentKeyIds: POINTER(Guid), contentKeyIdStrings: POINTER(WinRT_String), contentEncryptionAlgorithm: Windows.Media.Protection.PlayReady.PlayReadyEncryptionAlgorithm, licenseAcquisitionUrl: Windows.Foundation.Uri, licenseAcquisitionUserInterfaceUrl: Windows.Foundation.Uri, customAttributes: WinRT_String, domainServiceId: Guid) -> Windows.Media.Protection.PlayReady.PlayReadyContentHeader: ...
class IPlayReadyContentResolver(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyContentResolver'
    _iid_ = Guid('{fbfd2523-906d-4982-a6b8-6849565a7ce8}')
    @winrt_commethod(6)
    def ServiceRequest(self, contentHeader: Windows.Media.Protection.PlayReady.PlayReadyContentHeader) -> Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest: ...
class IPlayReadyDomain(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    def get_DomainJoinUrl(self) -> Windows.Foundation.Uri: ...
    AccountId = property(get_AccountId, None)
    ServiceId = property(get_ServiceId, None)
    Revision = property(get_Revision, None)
    FriendlyName = property(get_FriendlyName, None)
    DomainJoinUrl = property(get_DomainJoinUrl, None)
class IPlayReadyDomainIterableFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyDomainIterableFactory'
    _iid_ = Guid('{4df384ee-3121-4df3-a5e8-d0c24c0500fc}')
    @winrt_commethod(6)
    def CreateInstance(self, domainAccountId: Guid) -> Windows.Media.Protection.PlayReady.PlayReadyDomainIterable: ...
class IPlayReadyDomainJoinServiceRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    extends: Windows.Win32.System.WinRT.IInspectable
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyITADataGenerator'
    _iid_ = Guid('{24446b8e-10b9-4530-b25b-901a8029a9b2}')
    @winrt_commethod(6)
    def GenerateData(self, guidCPSystemId: Guid, countOfStreams: UInt32, configuration: Windows.Foundation.Collections.IPropertySet, format: Windows.Media.Protection.PlayReady.PlayReadyITADataFormat) -> c_char_p_no: ...
class IPlayReadyIndividualizationServiceRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyIndividualizationServiceRequest'
    _iid_ = Guid('{21f5a86b-008c-4611-ab2f-aaa6c69f0e24}')
class IPlayReadyLicense(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyLicense'
    _iid_ = Guid('{ee474c4e-fa3c-414d-a9f2-3ffc1ef832d4}')
    @winrt_commethod(6)
    def get_FullyEvaluated(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_UsableForPlay(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_ExpirationDate(self) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_commethod(9)
    def get_ExpireAfterFirstPlay(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_DomainAccountID(self) -> Guid: ...
    @winrt_commethod(11)
    def get_ChainDepth(self) -> UInt32: ...
    @winrt_commethod(12)
    def GetKIDAtChainDepth(self, chainDepth: UInt32) -> Guid: ...
    FullyEvaluated = property(get_FullyEvaluated, None)
    UsableForPlay = property(get_UsableForPlay, None)
    ExpirationDate = property(get_ExpirationDate, None)
    ExpireAfterFirstPlay = property(get_ExpireAfterFirstPlay, None)
    DomainAccountID = property(get_DomainAccountID, None)
    ChainDepth = property(get_ChainDepth, None)
class IPlayReadyLicense2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    SecureStopId = property(get_SecureStopId, None)
    SecurityLevel = property(get_SecurityLevel, None)
    InMemoryOnly = property(get_InMemoryOnly, None)
    ExpiresInRealTime = property(get_ExpiresInRealTime, None)
class IPlayReadyLicenseAcquisitionServiceRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyLicenseAcquisitionServiceRequest'
    _iid_ = Guid('{5d85ff45-3e9f-4f48-93e1-9530c8d58c3e}')
    @winrt_commethod(6)
    def get_ContentHeader(self) -> Windows.Media.Protection.PlayReady.PlayReadyContentHeader: ...
    @winrt_commethod(7)
    def put_ContentHeader(self, value: Windows.Media.Protection.PlayReady.PlayReadyContentHeader) -> Void: ...
    @winrt_commethod(8)
    def get_DomainServiceId(self) -> Guid: ...
    @winrt_commethod(9)
    def put_DomainServiceId(self, value: Guid) -> Void: ...
    ContentHeader = property(get_ContentHeader, put_ContentHeader)
    DomainServiceId = property(get_DomainServiceId, put_DomainServiceId)
class IPlayReadyLicenseAcquisitionServiceRequest2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyLicenseAcquisitionServiceRequest2'
    _iid_ = Guid('{b7fa5eb5-fe0c-b225-bc60-5a9edd32ceb5}')
    @winrt_commethod(6)
    def get_SessionId(self) -> Guid: ...
    SessionId = property(get_SessionId, None)
class IPlayReadyLicenseAcquisitionServiceRequest3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyLicenseAcquisitionServiceRequest3'
    _iid_ = Guid('{394e5f4d-7f75-430d-b2e7-7f75f34b2d75}')
    @winrt_commethod(6)
    def CreateLicenseIterable(self, contentHeader: Windows.Media.Protection.PlayReady.PlayReadyContentHeader, fullyEvaluated: Boolean) -> Windows.Media.Protection.PlayReady.PlayReadyLicenseIterable: ...
class IPlayReadyLicenseIterableFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyLicenseIterableFactory'
    _iid_ = Guid('{d4179f08-0837-4978-8e68-be4293c8d7a6}')
    @winrt_commethod(6)
    def CreateInstance(self, contentHeader: Windows.Media.Protection.PlayReady.PlayReadyContentHeader, fullyEvaluated: Boolean) -> Windows.Media.Protection.PlayReady.PlayReadyLicenseIterable: ...
class IPlayReadyLicenseManagement(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyLicenseManagement'
    _iid_ = Guid('{aaeb2141-0957-4405-b892-8bf3ec5dadd9}')
    @winrt_commethod(6)
    def DeleteLicenses(self, contentHeader: Windows.Media.Protection.PlayReady.PlayReadyContentHeader) -> Windows.Foundation.IAsyncAction: ...
class IPlayReadyLicenseSession(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyLicenseSession'
    _iid_ = Guid('{a1723a39-87fa-4fdd-abbb-a9720e845259}')
    @winrt_commethod(6)
    def CreateLAServiceRequest(self) -> Windows.Media.Protection.PlayReady.IPlayReadyLicenseAcquisitionServiceRequest: ...
    @winrt_commethod(7)
    def ConfigureMediaProtectionManager(self, mpm: Windows.Media.Protection.MediaProtectionManager) -> Void: ...
class IPlayReadyLicenseSession2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyLicenseSession2'
    _iid_ = Guid('{4909be3a-3aed-4656-8ad7-ee0fd7799510}')
    @winrt_commethod(6)
    def CreateLicenseIterable(self, contentHeader: Windows.Media.Protection.PlayReady.PlayReadyContentHeader, fullyEvaluated: Boolean) -> Windows.Media.Protection.PlayReady.PlayReadyLicenseIterable: ...
class IPlayReadyLicenseSessionFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyLicenseSessionFactory'
    _iid_ = Guid('{62492699-6527-429e-98be-48d798ac2739}')
    @winrt_commethod(6)
    def CreateInstance(self, configuration: Windows.Foundation.Collections.IPropertySet) -> Windows.Media.Protection.PlayReady.PlayReadyLicenseSession: ...
class IPlayReadyMeteringReportServiceRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyMeteringReportServiceRequest'
    _iid_ = Guid('{c12b231c-0ecd-4f11-a185-1e24a4a67fb7}')
    @winrt_commethod(6)
    def get_MeteringCertificate(self) -> c_char_p_no: ...
    @winrt_commethod(7)
    def put_MeteringCertificate(self, meteringCertBytes: c_char_p_no) -> Void: ...
    MeteringCertificate = property(get_MeteringCertificate, put_MeteringCertificate)
class IPlayReadyRevocationServiceRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyRevocationServiceRequest'
    _iid_ = Guid('{543d66ac-faf0-4560-84a5-0e4acec939e4}')
class IPlayReadySecureStopIterableFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadySecureStopIterableFactory'
    _iid_ = Guid('{5f1f0165-4214-4d9e-81eb-e89f9d294aee}')
    @winrt_commethod(6)
    def CreateInstance(self, publisherCertBytes: c_char_p_no) -> Windows.Media.Protection.PlayReady.PlayReadySecureStopIterable: ...
class IPlayReadySecureStopServiceRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadySecureStopServiceRequest'
    _iid_ = Guid('{b5501ee5-01bf-4401-9677-05630a6a4cc8}')
    @winrt_commethod(6)
    def get_SessionID(self) -> Guid: ...
    @winrt_commethod(7)
    def get_StartTime(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(8)
    def get_UpdateTime(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(9)
    def get_Stopped(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_PublisherCertificate(self) -> c_char_p_no: ...
    SessionID = property(get_SessionID, None)
    StartTime = property(get_StartTime, None)
    UpdateTime = property(get_UpdateTime, None)
    Stopped = property(get_Stopped, None)
    PublisherCertificate = property(get_PublisherCertificate, None)
class IPlayReadySecureStopServiceRequestFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadySecureStopServiceRequestFactory'
    _iid_ = Guid('{0e448ac9-e67e-494e-9f49-6285438c76cf}')
    @winrt_commethod(6)
    def CreateInstance(self, publisherCertBytes: c_char_p_no) -> Windows.Media.Protection.PlayReady.PlayReadySecureStopServiceRequest: ...
    @winrt_commethod(7)
    def CreateInstanceFromSessionID(self, sessionID: Guid, publisherCertBytes: c_char_p_no) -> Windows.Media.Protection.PlayReady.PlayReadySecureStopServiceRequest: ...
class IPlayReadyServiceRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest'
    _iid_ = Guid('{8bad2836-a703-45a6-a180-76f3565aa725}')
    @winrt_commethod(6)
    def get_Uri(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def put_Uri(self, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(8)
    def get_ResponseCustomData(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_ChallengeCustomData(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def put_ChallengeCustomData(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(11)
    def BeginServiceRequest(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(12)
    def NextServiceRequest(self) -> Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest: ...
    @winrt_commethod(13)
    def GenerateManualEnablingChallenge(self) -> Windows.Media.Protection.PlayReady.PlayReadySoapMessage: ...
    @winrt_commethod(14)
    def ProcessManualEnablingResponse(self, responseBytes: c_char_p_no) -> Windows.Foundation.HResult: ...
    Uri = property(get_Uri, put_Uri)
    ResponseCustomData = property(get_ResponseCustomData, None)
    ChallengeCustomData = property(get_ChallengeCustomData, put_ChallengeCustomData)
class IPlayReadySoapMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadySoapMessage'
    _iid_ = Guid('{b659fcb5-ce41-41ba-8a0d-61df5fffa139}')
    @winrt_commethod(6)
    def GetMessageBody(self) -> c_char_p_no: ...
    @winrt_commethod(7)
    def get_MessageHeaders(self) -> Windows.Foundation.Collections.IPropertySet: ...
    @winrt_commethod(8)
    def get_Uri(self) -> Windows.Foundation.Uri: ...
    MessageHeaders = property(get_MessageHeaders, None)
    Uri = property(get_Uri, None)
class IPlayReadyStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    MeteringReportServiceRequestType = property(get_MeteringReportServiceRequestType, None)
    RevocationServiceRequestType = property(get_RevocationServiceRequestType, None)
    MediaProtectionSystemId = property(get_MediaProtectionSystemId, None)
    PlayReadySecurityVersion = property(get_PlayReadySecurityVersion, None)
class IPlayReadyStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyStatics2'
    _iid_ = Guid('{1f8d6a92-5f9a-423e-9466-b33969af7a3d}')
    @winrt_commethod(6)
    def get_PlayReadyCertificateSecurityLevel(self) -> UInt32: ...
    PlayReadyCertificateSecurityLevel = property(get_PlayReadyCertificateSecurityLevel, None)
class IPlayReadyStatics3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyStatics3'
    _iid_ = Guid('{3fa33f71-2dd3-4bed-ae49-f7148e63e710}')
    @winrt_commethod(6)
    def get_SecureStopServiceRequestType(self) -> Guid: ...
    @winrt_commethod(7)
    def CheckSupportedHardware(self, hwdrmFeature: Windows.Media.Protection.PlayReady.PlayReadyHardwareDRMFeatures) -> Boolean: ...
    SecureStopServiceRequestType = property(get_SecureStopServiceRequestType, None)
class IPlayReadyStatics4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyStatics4'
    _iid_ = Guid('{50a91300-d824-4231-9d5e-78ef8844c7d7}')
    @winrt_commethod(6)
    def get_InputTrustAuthorityToCreate(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ProtectionSystemId(self) -> Guid: ...
    InputTrustAuthorityToCreate = property(get_InputTrustAuthorityToCreate, None)
    ProtectionSystemId = property(get_ProtectionSystemId, None)
class IPlayReadyStatics5(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.IPlayReadyStatics5'
    _iid_ = Guid('{230a7075-dfa0-4f8e-a779-cefea9c6824b}')
    @winrt_commethod(6)
    def get_HardwareDRMDisabledAtTime(self) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_commethod(7)
    def get_HardwareDRMDisabledUntilTime(self) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_commethod(8)
    def ResetHardwareDRMDisabled(self) -> Void: ...
    HardwareDRMDisabledAtTime = property(get_HardwareDRMDisabledAtTime, None)
    HardwareDRMDisabledUntilTime = property(get_HardwareDRMDisabledUntilTime, None)
NDCertificateFeature = Int32
NDCertificateFeature_Transmitter: NDCertificateFeature = 1
NDCertificateFeature_Receiver: NDCertificateFeature = 2
NDCertificateFeature_SharedCertificate: NDCertificateFeature = 3
NDCertificateFeature_SecureClock: NDCertificateFeature = 4
NDCertificateFeature_AntiRollBackClock: NDCertificateFeature = 5
NDCertificateFeature_CRLS: NDCertificateFeature = 9
NDCertificateFeature_PlayReady3Features: NDCertificateFeature = 13
NDCertificatePlatformID = Int32
NDCertificatePlatformID_Windows: NDCertificatePlatformID = 0
NDCertificatePlatformID_OSX: NDCertificatePlatformID = 1
NDCertificatePlatformID_WindowsOnARM: NDCertificatePlatformID = 2
NDCertificatePlatformID_WindowsMobile7: NDCertificatePlatformID = 5
NDCertificatePlatformID_iOSOnARM: NDCertificatePlatformID = 6
NDCertificatePlatformID_XBoxOnPPC: NDCertificatePlatformID = 7
NDCertificatePlatformID_WindowsPhone8OnARM: NDCertificatePlatformID = 8
NDCertificatePlatformID_WindowsPhone8OnX86: NDCertificatePlatformID = 9
NDCertificatePlatformID_XboxOne: NDCertificatePlatformID = 10
NDCertificatePlatformID_AndroidOnARM: NDCertificatePlatformID = 11
NDCertificatePlatformID_WindowsPhone81OnARM: NDCertificatePlatformID = 12
NDCertificatePlatformID_WindowsPhone81OnX86: NDCertificatePlatformID = 13
NDCertificateType = Int32
NDCertificateType_Unknown: NDCertificateType = 0
NDCertificateType_PC: NDCertificateType = 1
NDCertificateType_Device: NDCertificateType = 2
NDCertificateType_Domain: NDCertificateType = 3
NDCertificateType_Issuer: NDCertificateType = 4
NDCertificateType_CrlSigner: NDCertificateType = 5
NDCertificateType_Service: NDCertificateType = 6
NDCertificateType_Silverlight: NDCertificateType = 7
NDCertificateType_Application: NDCertificateType = 8
NDCertificateType_Metering: NDCertificateType = 9
NDCertificateType_KeyFileSigner: NDCertificateType = 10
NDCertificateType_Server: NDCertificateType = 11
NDCertificateType_LicenseSigner: NDCertificateType = 12
class NDClient(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Protection.PlayReady.INDClient
    _classid_ = 'Windows.Media.Protection.PlayReady.NDClient'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.Media.Protection.PlayReady.INDClientFactory, downloadEngine: Windows.Media.Protection.PlayReady.INDDownloadEngine, streamParser: Windows.Media.Protection.PlayReady.INDStreamParser, pMessenger: Windows.Media.Protection.PlayReady.INDMessenger) -> Windows.Media.Protection.PlayReady.NDClient: ...
    @winrt_mixinmethod
    def add_RegistrationCompleted(self: Windows.Media.Protection.PlayReady.INDClient, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Protection.PlayReady.NDClient, Windows.Media.Protection.PlayReady.INDRegistrationCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RegistrationCompleted(self: Windows.Media.Protection.PlayReady.INDClient, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ProximityDetectionCompleted(self: Windows.Media.Protection.PlayReady.INDClient, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Protection.PlayReady.NDClient, Windows.Media.Protection.PlayReady.INDProximityDetectionCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ProximityDetectionCompleted(self: Windows.Media.Protection.PlayReady.INDClient, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_LicenseFetchCompleted(self: Windows.Media.Protection.PlayReady.INDClient, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Protection.PlayReady.NDClient, Windows.Media.Protection.PlayReady.INDLicenseFetchCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_LicenseFetchCompleted(self: Windows.Media.Protection.PlayReady.INDClient, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ReRegistrationNeeded(self: Windows.Media.Protection.PlayReady.INDClient, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Protection.PlayReady.NDClient, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ReRegistrationNeeded(self: Windows.Media.Protection.PlayReady.INDClient, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ClosedCaptionDataReceived(self: Windows.Media.Protection.PlayReady.INDClient, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Protection.PlayReady.NDClient, Windows.Media.Protection.PlayReady.INDClosedCaptionDataReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ClosedCaptionDataReceived(self: Windows.Media.Protection.PlayReady.INDClient, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def StartAsync(self: Windows.Media.Protection.PlayReady.INDClient, contentUrl: Windows.Foundation.Uri, startAsyncOptions: UInt32, registrationCustomData: Windows.Media.Protection.PlayReady.INDCustomData, licenseFetchDescriptor: Windows.Media.Protection.PlayReady.INDLicenseFetchDescriptor) -> Windows.Foundation.IAsyncOperation[Windows.Media.Protection.PlayReady.INDStartResult]: ...
    @winrt_mixinmethod
    def LicenseFetchAsync(self: Windows.Media.Protection.PlayReady.INDClient, licenseFetchDescriptor: Windows.Media.Protection.PlayReady.INDLicenseFetchDescriptor) -> Windows.Foundation.IAsyncOperation[Windows.Media.Protection.PlayReady.INDLicenseFetchResult]: ...
    @winrt_mixinmethod
    def ReRegistrationAsync(self: Windows.Media.Protection.PlayReady.INDClient, registrationCustomData: Windows.Media.Protection.PlayReady.INDCustomData) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def Close(self: Windows.Media.Protection.PlayReady.INDClient) -> Void: ...
NDClosedCaptionFormat = Int32
NDClosedCaptionFormat_ATSC: NDClosedCaptionFormat = 0
NDClosedCaptionFormat_SCTE20: NDClosedCaptionFormat = 1
NDClosedCaptionFormat_Unknown: NDClosedCaptionFormat = 2
NDContentIDType = Int32
NDContentIDType_KeyID: NDContentIDType = 1
NDContentIDType_PlayReadyObject: NDContentIDType = 2
NDContentIDType_Custom: NDContentIDType = 3
class NDCustomData(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Protection.PlayReady.INDCustomData
    _classid_ = 'Windows.Media.Protection.PlayReady.NDCustomData'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.Media.Protection.PlayReady.INDCustomDataFactory, customDataTypeIDBytes: c_char_p_no, customDataBytes: c_char_p_no) -> Windows.Media.Protection.PlayReady.NDCustomData: ...
    @winrt_mixinmethod
    def get_CustomDataTypeID(self: Windows.Media.Protection.PlayReady.INDCustomData) -> c_char_p_no: ...
    @winrt_mixinmethod
    def get_CustomData(self: Windows.Media.Protection.PlayReady.INDCustomData) -> c_char_p_no: ...
    CustomDataTypeID = property(get_CustomDataTypeID, None)
    CustomData = property(get_CustomData, None)
class NDDownloadEngineNotifier(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Protection.PlayReady.INDDownloadEngineNotifier
    _classid_ = 'Windows.Media.Protection.PlayReady.NDDownloadEngineNotifier'
    @winrt_activatemethod
    def New(cls) -> Windows.Media.Protection.PlayReady.NDDownloadEngineNotifier: ...
    @winrt_mixinmethod
    def OnStreamOpened(self: Windows.Media.Protection.PlayReady.INDDownloadEngineNotifier) -> Void: ...
    @winrt_mixinmethod
    def OnPlayReadyObjectReceived(self: Windows.Media.Protection.PlayReady.INDDownloadEngineNotifier, dataBytes: c_char_p_no) -> Void: ...
    @winrt_mixinmethod
    def OnContentIDReceived(self: Windows.Media.Protection.PlayReady.INDDownloadEngineNotifier, licenseFetchDescriptor: Windows.Media.Protection.PlayReady.INDLicenseFetchDescriptor) -> Void: ...
    @winrt_mixinmethod
    def OnDataReceived(self: Windows.Media.Protection.PlayReady.INDDownloadEngineNotifier, dataBytes: c_char_p_no, bytesReceived: UInt32) -> Void: ...
    @winrt_mixinmethod
    def OnEndOfStream(self: Windows.Media.Protection.PlayReady.INDDownloadEngineNotifier) -> Void: ...
    @winrt_mixinmethod
    def OnNetworkError(self: Windows.Media.Protection.PlayReady.INDDownloadEngineNotifier) -> Void: ...
class NDLicenseFetchDescriptor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Protection.PlayReady.INDLicenseFetchDescriptor
    _classid_ = 'Windows.Media.Protection.PlayReady.NDLicenseFetchDescriptor'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.Media.Protection.PlayReady.INDLicenseFetchDescriptorFactory, contentIDType: Windows.Media.Protection.PlayReady.NDContentIDType, contentIDBytes: c_char_p_no, licenseFetchChallengeCustomData: Windows.Media.Protection.PlayReady.INDCustomData) -> Windows.Media.Protection.PlayReady.NDLicenseFetchDescriptor: ...
    @winrt_mixinmethod
    def get_ContentIDType(self: Windows.Media.Protection.PlayReady.INDLicenseFetchDescriptor) -> Windows.Media.Protection.PlayReady.NDContentIDType: ...
    @winrt_mixinmethod
    def get_ContentID(self: Windows.Media.Protection.PlayReady.INDLicenseFetchDescriptor) -> c_char_p_no: ...
    @winrt_mixinmethod
    def get_LicenseFetchChallengeCustomData(self: Windows.Media.Protection.PlayReady.INDLicenseFetchDescriptor) -> Windows.Media.Protection.PlayReady.INDCustomData: ...
    @winrt_mixinmethod
    def put_LicenseFetchChallengeCustomData(self: Windows.Media.Protection.PlayReady.INDLicenseFetchDescriptor, licenseFetchChallengeCustomData: Windows.Media.Protection.PlayReady.INDCustomData) -> Void: ...
    ContentIDType = property(get_ContentIDType, None)
    ContentID = property(get_ContentID, None)
    LicenseFetchChallengeCustomData = property(get_LicenseFetchChallengeCustomData, put_LicenseFetchChallengeCustomData)
NDMediaStreamType = Int32
NDMediaStreamType_Audio: NDMediaStreamType = 1
NDMediaStreamType_Video: NDMediaStreamType = 2
NDProximityDetectionType = Int32
NDProximityDetectionType_UDP: NDProximityDetectionType = 1
NDProximityDetectionType_TCP: NDProximityDetectionType = 2
NDProximityDetectionType_TransportAgnostic: NDProximityDetectionType = 4
NDStartAsyncOptions = Int32
NDStartAsyncOptions_MutualAuthentication: NDStartAsyncOptions = 1
NDStartAsyncOptions_WaitForLicenseDescriptor: NDStartAsyncOptions = 2
class NDStorageFileHelper(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Protection.PlayReady.INDStorageFileHelper
    _classid_ = 'Windows.Media.Protection.PlayReady.NDStorageFileHelper'
    @winrt_activatemethod
    def New(cls) -> Windows.Media.Protection.PlayReady.NDStorageFileHelper: ...
    @winrt_mixinmethod
    def GetFileURLs(self: Windows.Media.Protection.PlayReady.INDStorageFileHelper, file: Windows.Storage.IStorageFile) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
class NDStreamParserNotifier(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Protection.PlayReady.INDStreamParserNotifier
    _classid_ = 'Windows.Media.Protection.PlayReady.NDStreamParserNotifier'
    @winrt_activatemethod
    def New(cls) -> Windows.Media.Protection.PlayReady.NDStreamParserNotifier: ...
    @winrt_mixinmethod
    def OnContentIDReceived(self: Windows.Media.Protection.PlayReady.INDStreamParserNotifier, licenseFetchDescriptor: Windows.Media.Protection.PlayReady.INDLicenseFetchDescriptor) -> Void: ...
    @winrt_mixinmethod
    def OnMediaStreamDescriptorCreated(self: Windows.Media.Protection.PlayReady.INDStreamParserNotifier, audioStreamDescriptors: Windows.Foundation.Collections.IVector[Windows.Media.Core.AudioStreamDescriptor], videoStreamDescriptors: Windows.Foundation.Collections.IVector[Windows.Media.Core.VideoStreamDescriptor]) -> Void: ...
    @winrt_mixinmethod
    def OnSampleParsed(self: Windows.Media.Protection.PlayReady.INDStreamParserNotifier, streamID: UInt32, streamType: Windows.Media.Protection.PlayReady.NDMediaStreamType, streamSample: Windows.Media.Core.MediaStreamSample, pts: Int64, ccFormat: Windows.Media.Protection.PlayReady.NDClosedCaptionFormat, ccDataBytes: c_char_p_no) -> Void: ...
    @winrt_mixinmethod
    def OnBeginSetupDecryptor(self: Windows.Media.Protection.PlayReady.INDStreamParserNotifier, descriptor: Windows.Media.Core.IMediaStreamDescriptor, keyID: Guid, proBytes: c_char_p_no) -> Void: ...
class NDTCPMessenger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Protection.PlayReady.INDMessenger
    _classid_ = 'Windows.Media.Protection.PlayReady.NDTCPMessenger'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.Media.Protection.PlayReady.INDTCPMessengerFactory, remoteHostName: WinRT_String, remoteHostPort: UInt32) -> Windows.Media.Protection.PlayReady.NDTCPMessenger: ...
    @winrt_mixinmethod
    def SendRegistrationRequestAsync(self: Windows.Media.Protection.PlayReady.INDMessenger, sessionIDBytes: c_char_p_no, challengeDataBytes: c_char_p_no) -> Windows.Foundation.IAsyncOperation[Windows.Media.Protection.PlayReady.INDSendResult]: ...
    @winrt_mixinmethod
    def SendProximityDetectionStartAsync(self: Windows.Media.Protection.PlayReady.INDMessenger, pdType: Windows.Media.Protection.PlayReady.NDProximityDetectionType, transmitterChannelBytes: c_char_p_no, sessionIDBytes: c_char_p_no, challengeDataBytes: c_char_p_no) -> Windows.Foundation.IAsyncOperation[Windows.Media.Protection.PlayReady.INDSendResult]: ...
    @winrt_mixinmethod
    def SendProximityDetectionResponseAsync(self: Windows.Media.Protection.PlayReady.INDMessenger, pdType: Windows.Media.Protection.PlayReady.NDProximityDetectionType, transmitterChannelBytes: c_char_p_no, sessionIDBytes: c_char_p_no, responseDataBytes: c_char_p_no) -> Windows.Foundation.IAsyncOperation[Windows.Media.Protection.PlayReady.INDSendResult]: ...
    @winrt_mixinmethod
    def SendLicenseFetchRequestAsync(self: Windows.Media.Protection.PlayReady.INDMessenger, sessionIDBytes: c_char_p_no, challengeDataBytes: c_char_p_no) -> Windows.Foundation.IAsyncOperation[Windows.Media.Protection.PlayReady.INDSendResult]: ...
class PlayReadyContentHeader(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Protection.PlayReady.IPlayReadyContentHeader
    _classid_ = 'Windows.Media.Protection.PlayReady.PlayReadyContentHeader'
    @winrt_factorymethod
    def CreateInstanceFromComponents2(cls: Windows.Media.Protection.PlayReady.IPlayReadyContentHeaderFactory2, dwFlags: UInt32, contentKeyIds: POINTER(Guid), contentKeyIdStrings: POINTER(WinRT_String), contentEncryptionAlgorithm: Windows.Media.Protection.PlayReady.PlayReadyEncryptionAlgorithm, licenseAcquisitionUrl: Windows.Foundation.Uri, licenseAcquisitionUserInterfaceUrl: Windows.Foundation.Uri, customAttributes: WinRT_String, domainServiceId: Guid) -> Windows.Media.Protection.PlayReady.PlayReadyContentHeader: ...
    @winrt_factorymethod
    def CreateInstanceFromWindowsMediaDrmHeader(cls: Windows.Media.Protection.PlayReady.IPlayReadyContentHeaderFactory, headerBytes: c_char_p_no, licenseAcquisitionUrl: Windows.Foundation.Uri, licenseAcquisitionUserInterfaceUrl: Windows.Foundation.Uri, customAttributes: WinRT_String, domainServiceId: Guid) -> Windows.Media.Protection.PlayReady.PlayReadyContentHeader: ...
    @winrt_factorymethod
    def CreateInstanceFromComponents(cls: Windows.Media.Protection.PlayReady.IPlayReadyContentHeaderFactory, contentKeyId: Guid, contentKeyIdString: WinRT_String, contentEncryptionAlgorithm: Windows.Media.Protection.PlayReady.PlayReadyEncryptionAlgorithm, licenseAcquisitionUrl: Windows.Foundation.Uri, licenseAcquisitionUserInterfaceUrl: Windows.Foundation.Uri, customAttributes: WinRT_String, domainServiceId: Guid) -> Windows.Media.Protection.PlayReady.PlayReadyContentHeader: ...
    @winrt_factorymethod
    def CreateInstanceFromPlayReadyHeader(cls: Windows.Media.Protection.PlayReady.IPlayReadyContentHeaderFactory, headerBytes: c_char_p_no) -> Windows.Media.Protection.PlayReady.PlayReadyContentHeader: ...
    @winrt_mixinmethod
    def get_KeyId(self: Windows.Media.Protection.PlayReady.IPlayReadyContentHeader) -> Guid: ...
    @winrt_mixinmethod
    def get_KeyIdString(self: Windows.Media.Protection.PlayReady.IPlayReadyContentHeader) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LicenseAcquisitionUrl(self: Windows.Media.Protection.PlayReady.IPlayReadyContentHeader) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_LicenseAcquisitionUserInterfaceUrl(self: Windows.Media.Protection.PlayReady.IPlayReadyContentHeader) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_DomainServiceId(self: Windows.Media.Protection.PlayReady.IPlayReadyContentHeader) -> Guid: ...
    @winrt_mixinmethod
    def get_EncryptionType(self: Windows.Media.Protection.PlayReady.IPlayReadyContentHeader) -> Windows.Media.Protection.PlayReady.PlayReadyEncryptionAlgorithm: ...
    @winrt_mixinmethod
    def get_CustomAttributes(self: Windows.Media.Protection.PlayReady.IPlayReadyContentHeader) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DecryptorSetup(self: Windows.Media.Protection.PlayReady.IPlayReadyContentHeader) -> Windows.Media.Protection.PlayReady.PlayReadyDecryptorSetup: ...
    @winrt_mixinmethod
    def GetSerializedHeader(self: Windows.Media.Protection.PlayReady.IPlayReadyContentHeader) -> c_char_p_no: ...
    @winrt_mixinmethod
    def get_HeaderWithEmbeddedUpdates(self: Windows.Media.Protection.PlayReady.IPlayReadyContentHeader) -> Windows.Media.Protection.PlayReady.PlayReadyContentHeader: ...
    @winrt_mixinmethod
    def get_KeyIds(self: Windows.Media.Protection.PlayReady.IPlayReadyContentHeader2) -> POINTER(Guid): ...
    @winrt_mixinmethod
    def get_KeyIdStrings(self: Windows.Media.Protection.PlayReady.IPlayReadyContentHeader2) -> POINTER(WinRT_String): ...
    KeyId = property(get_KeyId, None)
    KeyIdString = property(get_KeyIdString, None)
    LicenseAcquisitionUrl = property(get_LicenseAcquisitionUrl, None)
    LicenseAcquisitionUserInterfaceUrl = property(get_LicenseAcquisitionUserInterfaceUrl, None)
    DomainServiceId = property(get_DomainServiceId, None)
    EncryptionType = property(get_EncryptionType, None)
    CustomAttributes = property(get_CustomAttributes, None)
    DecryptorSetup = property(get_DecryptorSetup, None)
    HeaderWithEmbeddedUpdates = property(get_HeaderWithEmbeddedUpdates, None)
    KeyIds = property(get_KeyIds, None)
    KeyIdStrings = property(get_KeyIdStrings, None)
class PlayReadyContentResolver(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.PlayReadyContentResolver'
    @winrt_classmethod
    def ServiceRequest(cls: Windows.Media.Protection.PlayReady.IPlayReadyContentResolver, contentHeader: Windows.Media.Protection.PlayReady.PlayReadyContentHeader) -> Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest: ...
PlayReadyDecryptorSetup = Int32
PlayReadyDecryptorSetup_Uninitialized: PlayReadyDecryptorSetup = 0
PlayReadyDecryptorSetup_OnDemand: PlayReadyDecryptorSetup = 1
class PlayReadyDomain(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Protection.PlayReady.IPlayReadyDomain
    _classid_ = 'Windows.Media.Protection.PlayReady.PlayReadyDomain'
    @winrt_mixinmethod
    def get_AccountId(self: Windows.Media.Protection.PlayReady.IPlayReadyDomain) -> Guid: ...
    @winrt_mixinmethod
    def get_ServiceId(self: Windows.Media.Protection.PlayReady.IPlayReadyDomain) -> Guid: ...
    @winrt_mixinmethod
    def get_Revision(self: Windows.Media.Protection.PlayReady.IPlayReadyDomain) -> UInt32: ...
    @winrt_mixinmethod
    def get_FriendlyName(self: Windows.Media.Protection.PlayReady.IPlayReadyDomain) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DomainJoinUrl(self: Windows.Media.Protection.PlayReady.IPlayReadyDomain) -> Windows.Foundation.Uri: ...
    AccountId = property(get_AccountId, None)
    ServiceId = property(get_ServiceId, None)
    Revision = property(get_Revision, None)
    FriendlyName = property(get_FriendlyName, None)
    DomainJoinUrl = property(get_DomainJoinUrl, None)
class PlayReadyDomainIterable(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Foundation.Collections.IIterable[Windows.Media.Protection.PlayReady.IPlayReadyDomain]
    _classid_ = 'Windows.Media.Protection.PlayReady.PlayReadyDomainIterable'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.Media.Protection.PlayReady.IPlayReadyDomainIterableFactory, domainAccountId: Guid) -> Windows.Media.Protection.PlayReady.PlayReadyDomainIterable: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.Media.Protection.PlayReady.IPlayReadyDomain]) -> Windows.Foundation.Collections.IIterator[Windows.Media.Protection.PlayReady.IPlayReadyDomain]: ...
class PlayReadyDomainIterator(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Foundation.Collections.IIterator[Windows.Media.Protection.PlayReady.IPlayReadyDomain]
    _classid_ = 'Windows.Media.Protection.PlayReady.PlayReadyDomainIterator'
    @winrt_mixinmethod
    def get_Current(self: Windows.Foundation.Collections.IIterator[Windows.Media.Protection.PlayReady.IPlayReadyDomain]) -> Windows.Media.Protection.PlayReady.IPlayReadyDomain: ...
    @winrt_mixinmethod
    def get_HasCurrent(self: Windows.Foundation.Collections.IIterator[Windows.Media.Protection.PlayReady.IPlayReadyDomain]) -> Boolean: ...
    @winrt_mixinmethod
    def MoveNext(self: Windows.Foundation.Collections.IIterator[Windows.Media.Protection.PlayReady.IPlayReadyDomain]) -> Boolean: ...
    @winrt_mixinmethod
    def GetMany(self: Windows.Foundation.Collections.IIterator[Windows.Media.Protection.PlayReady.IPlayReadyDomain], items: POINTER(Windows.Media.Protection.PlayReady.IPlayReadyDomain)) -> UInt32: ...
    Current = property(get_Current, None)
    HasCurrent = property(get_HasCurrent, None)
class PlayReadyDomainJoinServiceRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Protection.PlayReady.IPlayReadyDomainJoinServiceRequest
    _classid_ = 'Windows.Media.Protection.PlayReady.PlayReadyDomainJoinServiceRequest'
    @winrt_activatemethod
    def New(cls) -> Windows.Media.Protection.PlayReady.PlayReadyDomainJoinServiceRequest: ...
    @winrt_mixinmethod
    def get_DomainAccountId(self: Windows.Media.Protection.PlayReady.IPlayReadyDomainJoinServiceRequest) -> Guid: ...
    @winrt_mixinmethod
    def put_DomainAccountId(self: Windows.Media.Protection.PlayReady.IPlayReadyDomainJoinServiceRequest, value: Guid) -> Void: ...
    @winrt_mixinmethod
    def get_DomainFriendlyName(self: Windows.Media.Protection.PlayReady.IPlayReadyDomainJoinServiceRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DomainFriendlyName(self: Windows.Media.Protection.PlayReady.IPlayReadyDomainJoinServiceRequest, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DomainServiceId(self: Windows.Media.Protection.PlayReady.IPlayReadyDomainJoinServiceRequest) -> Guid: ...
    @winrt_mixinmethod
    def put_DomainServiceId(self: Windows.Media.Protection.PlayReady.IPlayReadyDomainJoinServiceRequest, value: Guid) -> Void: ...
    @winrt_mixinmethod
    def get_Uri(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_Uri(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_ResponseCustomData(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ChallengeCustomData(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ChallengeCustomData(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def BeginServiceRequest(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def NextServiceRequest(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest: ...
    @winrt_mixinmethod
    def GenerateManualEnablingChallenge(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> Windows.Media.Protection.PlayReady.PlayReadySoapMessage: ...
    @winrt_mixinmethod
    def ProcessManualEnablingResponse(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest, responseBytes: c_char_p_no) -> Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_ProtectionSystem(self: Windows.Media.Protection.IMediaProtectionServiceRequest) -> Guid: ...
    @winrt_mixinmethod
    def get_Type(self: Windows.Media.Protection.IMediaProtectionServiceRequest) -> Guid: ...
    DomainAccountId = property(get_DomainAccountId, put_DomainAccountId)
    DomainFriendlyName = property(get_DomainFriendlyName, put_DomainFriendlyName)
    DomainServiceId = property(get_DomainServiceId, put_DomainServiceId)
    Uri = property(get_Uri, put_Uri)
    ResponseCustomData = property(get_ResponseCustomData, None)
    ChallengeCustomData = property(get_ChallengeCustomData, put_ChallengeCustomData)
    ProtectionSystem = property(get_ProtectionSystem, None)
    Type = property(get_Type, None)
class PlayReadyDomainLeaveServiceRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Protection.PlayReady.IPlayReadyDomainLeaveServiceRequest
    _classid_ = 'Windows.Media.Protection.PlayReady.PlayReadyDomainLeaveServiceRequest'
    @winrt_activatemethod
    def New(cls) -> Windows.Media.Protection.PlayReady.PlayReadyDomainLeaveServiceRequest: ...
    @winrt_mixinmethod
    def get_DomainAccountId(self: Windows.Media.Protection.PlayReady.IPlayReadyDomainLeaveServiceRequest) -> Guid: ...
    @winrt_mixinmethod
    def put_DomainAccountId(self: Windows.Media.Protection.PlayReady.IPlayReadyDomainLeaveServiceRequest, value: Guid) -> Void: ...
    @winrt_mixinmethod
    def get_DomainServiceId(self: Windows.Media.Protection.PlayReady.IPlayReadyDomainLeaveServiceRequest) -> Guid: ...
    @winrt_mixinmethod
    def put_DomainServiceId(self: Windows.Media.Protection.PlayReady.IPlayReadyDomainLeaveServiceRequest, value: Guid) -> Void: ...
    @winrt_mixinmethod
    def get_Uri(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_Uri(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_ResponseCustomData(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ChallengeCustomData(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ChallengeCustomData(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def BeginServiceRequest(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def NextServiceRequest(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest: ...
    @winrt_mixinmethod
    def GenerateManualEnablingChallenge(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> Windows.Media.Protection.PlayReady.PlayReadySoapMessage: ...
    @winrt_mixinmethod
    def ProcessManualEnablingResponse(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest, responseBytes: c_char_p_no) -> Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_ProtectionSystem(self: Windows.Media.Protection.IMediaProtectionServiceRequest) -> Guid: ...
    @winrt_mixinmethod
    def get_Type(self: Windows.Media.Protection.IMediaProtectionServiceRequest) -> Guid: ...
    DomainAccountId = property(get_DomainAccountId, put_DomainAccountId)
    DomainServiceId = property(get_DomainServiceId, put_DomainServiceId)
    Uri = property(get_Uri, put_Uri)
    ResponseCustomData = property(get_ResponseCustomData, None)
    ChallengeCustomData = property(get_ChallengeCustomData, put_ChallengeCustomData)
    ProtectionSystem = property(get_ProtectionSystem, None)
    Type = property(get_Type, None)
PlayReadyEncryptionAlgorithm = Int32
PlayReadyEncryptionAlgorithm_Unprotected: PlayReadyEncryptionAlgorithm = 0
PlayReadyEncryptionAlgorithm_Aes128Ctr: PlayReadyEncryptionAlgorithm = 1
PlayReadyEncryptionAlgorithm_Cocktail: PlayReadyEncryptionAlgorithm = 4
PlayReadyEncryptionAlgorithm_Aes128Cbc: PlayReadyEncryptionAlgorithm = 5
PlayReadyEncryptionAlgorithm_Unspecified: PlayReadyEncryptionAlgorithm = 65535
PlayReadyEncryptionAlgorithm_Uninitialized: PlayReadyEncryptionAlgorithm = 2147483647
PlayReadyHardwareDRMFeatures = Int32
PlayReadyHardwareDRMFeatures_HardwareDRM: PlayReadyHardwareDRMFeatures = 1
PlayReadyHardwareDRMFeatures_HEVC: PlayReadyHardwareDRMFeatures = 2
PlayReadyHardwareDRMFeatures_Aes128Cbc: PlayReadyHardwareDRMFeatures = 3
PlayReadyITADataFormat = Int32
PlayReadyITADataFormat_SerializedProperties: PlayReadyITADataFormat = 0
PlayReadyITADataFormat_SerializedProperties_WithContentProtectionWrapper: PlayReadyITADataFormat = 1
class PlayReadyITADataGenerator(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Protection.PlayReady.IPlayReadyITADataGenerator
    _classid_ = 'Windows.Media.Protection.PlayReady.PlayReadyITADataGenerator'
    @winrt_activatemethod
    def New(cls) -> Windows.Media.Protection.PlayReady.PlayReadyITADataGenerator: ...
    @winrt_mixinmethod
    def GenerateData(self: Windows.Media.Protection.PlayReady.IPlayReadyITADataGenerator, guidCPSystemId: Guid, countOfStreams: UInt32, configuration: Windows.Foundation.Collections.IPropertySet, format: Windows.Media.Protection.PlayReady.PlayReadyITADataFormat) -> c_char_p_no: ...
class PlayReadyIndividualizationServiceRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Protection.PlayReady.IPlayReadyIndividualizationServiceRequest
    _classid_ = 'Windows.Media.Protection.PlayReady.PlayReadyIndividualizationServiceRequest'
    @winrt_activatemethod
    def New(cls) -> Windows.Media.Protection.PlayReady.PlayReadyIndividualizationServiceRequest: ...
    @winrt_mixinmethod
    def get_Uri(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_Uri(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_ResponseCustomData(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ChallengeCustomData(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ChallengeCustomData(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def BeginServiceRequest(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def NextServiceRequest(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest: ...
    @winrt_mixinmethod
    def GenerateManualEnablingChallenge(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> Windows.Media.Protection.PlayReady.PlayReadySoapMessage: ...
    @winrt_mixinmethod
    def ProcessManualEnablingResponse(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest, responseBytes: c_char_p_no) -> Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_ProtectionSystem(self: Windows.Media.Protection.IMediaProtectionServiceRequest) -> Guid: ...
    @winrt_mixinmethod
    def get_Type(self: Windows.Media.Protection.IMediaProtectionServiceRequest) -> Guid: ...
    Uri = property(get_Uri, put_Uri)
    ResponseCustomData = property(get_ResponseCustomData, None)
    ChallengeCustomData = property(get_ChallengeCustomData, put_ChallengeCustomData)
    ProtectionSystem = property(get_ProtectionSystem, None)
    Type = property(get_Type, None)
class PlayReadyLicense(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Protection.PlayReady.IPlayReadyLicense
    _classid_ = 'Windows.Media.Protection.PlayReady.PlayReadyLicense'
    @winrt_mixinmethod
    def get_FullyEvaluated(self: Windows.Media.Protection.PlayReady.IPlayReadyLicense) -> Boolean: ...
    @winrt_mixinmethod
    def get_UsableForPlay(self: Windows.Media.Protection.PlayReady.IPlayReadyLicense) -> Boolean: ...
    @winrt_mixinmethod
    def get_ExpirationDate(self: Windows.Media.Protection.PlayReady.IPlayReadyLicense) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def get_ExpireAfterFirstPlay(self: Windows.Media.Protection.PlayReady.IPlayReadyLicense) -> UInt32: ...
    @winrt_mixinmethod
    def get_DomainAccountID(self: Windows.Media.Protection.PlayReady.IPlayReadyLicense) -> Guid: ...
    @winrt_mixinmethod
    def get_ChainDepth(self: Windows.Media.Protection.PlayReady.IPlayReadyLicense) -> UInt32: ...
    @winrt_mixinmethod
    def GetKIDAtChainDepth(self: Windows.Media.Protection.PlayReady.IPlayReadyLicense, chainDepth: UInt32) -> Guid: ...
    @winrt_mixinmethod
    def get_SecureStopId(self: Windows.Media.Protection.PlayReady.IPlayReadyLicense2) -> Guid: ...
    @winrt_mixinmethod
    def get_SecurityLevel(self: Windows.Media.Protection.PlayReady.IPlayReadyLicense2) -> UInt32: ...
    @winrt_mixinmethod
    def get_InMemoryOnly(self: Windows.Media.Protection.PlayReady.IPlayReadyLicense2) -> Boolean: ...
    @winrt_mixinmethod
    def get_ExpiresInRealTime(self: Windows.Media.Protection.PlayReady.IPlayReadyLicense2) -> Boolean: ...
    FullyEvaluated = property(get_FullyEvaluated, None)
    UsableForPlay = property(get_UsableForPlay, None)
    ExpirationDate = property(get_ExpirationDate, None)
    ExpireAfterFirstPlay = property(get_ExpireAfterFirstPlay, None)
    DomainAccountID = property(get_DomainAccountID, None)
    ChainDepth = property(get_ChainDepth, None)
    SecureStopId = property(get_SecureStopId, None)
    SecurityLevel = property(get_SecurityLevel, None)
    InMemoryOnly = property(get_InMemoryOnly, None)
    ExpiresInRealTime = property(get_ExpiresInRealTime, None)
class PlayReadyLicenseAcquisitionServiceRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Protection.PlayReady.IPlayReadyLicenseAcquisitionServiceRequest
    _classid_ = 'Windows.Media.Protection.PlayReady.PlayReadyLicenseAcquisitionServiceRequest'
    @winrt_activatemethod
    def New(cls) -> Windows.Media.Protection.PlayReady.PlayReadyLicenseAcquisitionServiceRequest: ...
    @winrt_mixinmethod
    def get_ContentHeader(self: Windows.Media.Protection.PlayReady.IPlayReadyLicenseAcquisitionServiceRequest) -> Windows.Media.Protection.PlayReady.PlayReadyContentHeader: ...
    @winrt_mixinmethod
    def put_ContentHeader(self: Windows.Media.Protection.PlayReady.IPlayReadyLicenseAcquisitionServiceRequest, value: Windows.Media.Protection.PlayReady.PlayReadyContentHeader) -> Void: ...
    @winrt_mixinmethod
    def get_DomainServiceId(self: Windows.Media.Protection.PlayReady.IPlayReadyLicenseAcquisitionServiceRequest) -> Guid: ...
    @winrt_mixinmethod
    def put_DomainServiceId(self: Windows.Media.Protection.PlayReady.IPlayReadyLicenseAcquisitionServiceRequest, value: Guid) -> Void: ...
    @winrt_mixinmethod
    def get_Uri(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_Uri(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_ResponseCustomData(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ChallengeCustomData(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ChallengeCustomData(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def BeginServiceRequest(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def NextServiceRequest(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest: ...
    @winrt_mixinmethod
    def GenerateManualEnablingChallenge(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> Windows.Media.Protection.PlayReady.PlayReadySoapMessage: ...
    @winrt_mixinmethod
    def ProcessManualEnablingResponse(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest, responseBytes: c_char_p_no) -> Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_ProtectionSystem(self: Windows.Media.Protection.IMediaProtectionServiceRequest) -> Guid: ...
    @winrt_mixinmethod
    def get_Type(self: Windows.Media.Protection.IMediaProtectionServiceRequest) -> Guid: ...
    @winrt_mixinmethod
    def get_SessionId(self: Windows.Media.Protection.PlayReady.IPlayReadyLicenseAcquisitionServiceRequest2) -> Guid: ...
    @winrt_mixinmethod
    def CreateLicenseIterable(self: Windows.Media.Protection.PlayReady.IPlayReadyLicenseAcquisitionServiceRequest3, contentHeader: Windows.Media.Protection.PlayReady.PlayReadyContentHeader, fullyEvaluated: Boolean) -> Windows.Media.Protection.PlayReady.PlayReadyLicenseIterable: ...
    ContentHeader = property(get_ContentHeader, put_ContentHeader)
    DomainServiceId = property(get_DomainServiceId, put_DomainServiceId)
    Uri = property(get_Uri, put_Uri)
    ResponseCustomData = property(get_ResponseCustomData, None)
    ChallengeCustomData = property(get_ChallengeCustomData, put_ChallengeCustomData)
    ProtectionSystem = property(get_ProtectionSystem, None)
    Type = property(get_Type, None)
    SessionId = property(get_SessionId, None)
class PlayReadyLicenseIterable(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Foundation.Collections.IIterable[Windows.Media.Protection.PlayReady.IPlayReadyLicense]
    _classid_ = 'Windows.Media.Protection.PlayReady.PlayReadyLicenseIterable'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.Media.Protection.PlayReady.IPlayReadyLicenseIterableFactory, contentHeader: Windows.Media.Protection.PlayReady.PlayReadyContentHeader, fullyEvaluated: Boolean) -> Windows.Media.Protection.PlayReady.PlayReadyLicenseIterable: ...
    @winrt_activatemethod
    def New(cls) -> Windows.Media.Protection.PlayReady.PlayReadyLicenseIterable: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.Media.Protection.PlayReady.IPlayReadyLicense]) -> Windows.Foundation.Collections.IIterator[Windows.Media.Protection.PlayReady.IPlayReadyLicense]: ...
class PlayReadyLicenseIterator(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Foundation.Collections.IIterator[Windows.Media.Protection.PlayReady.IPlayReadyLicense]
    _classid_ = 'Windows.Media.Protection.PlayReady.PlayReadyLicenseIterator'
    @winrt_mixinmethod
    def get_Current(self: Windows.Foundation.Collections.IIterator[Windows.Media.Protection.PlayReady.IPlayReadyLicense]) -> Windows.Media.Protection.PlayReady.IPlayReadyLicense: ...
    @winrt_mixinmethod
    def get_HasCurrent(self: Windows.Foundation.Collections.IIterator[Windows.Media.Protection.PlayReady.IPlayReadyLicense]) -> Boolean: ...
    @winrt_mixinmethod
    def MoveNext(self: Windows.Foundation.Collections.IIterator[Windows.Media.Protection.PlayReady.IPlayReadyLicense]) -> Boolean: ...
    @winrt_mixinmethod
    def GetMany(self: Windows.Foundation.Collections.IIterator[Windows.Media.Protection.PlayReady.IPlayReadyLicense], items: POINTER(Windows.Media.Protection.PlayReady.IPlayReadyLicense)) -> UInt32: ...
    Current = property(get_Current, None)
    HasCurrent = property(get_HasCurrent, None)
class PlayReadyLicenseManagement(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.PlayReadyLicenseManagement'
    @winrt_classmethod
    def DeleteLicenses(cls: Windows.Media.Protection.PlayReady.IPlayReadyLicenseManagement, contentHeader: Windows.Media.Protection.PlayReady.PlayReadyContentHeader) -> Windows.Foundation.IAsyncAction: ...
class PlayReadyLicenseSession(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Protection.PlayReady.IPlayReadyLicenseSession
    _classid_ = 'Windows.Media.Protection.PlayReady.PlayReadyLicenseSession'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.Media.Protection.PlayReady.IPlayReadyLicenseSessionFactory, configuration: Windows.Foundation.Collections.IPropertySet) -> Windows.Media.Protection.PlayReady.PlayReadyLicenseSession: ...
    @winrt_mixinmethod
    def CreateLAServiceRequest(self: Windows.Media.Protection.PlayReady.IPlayReadyLicenseSession) -> Windows.Media.Protection.PlayReady.IPlayReadyLicenseAcquisitionServiceRequest: ...
    @winrt_mixinmethod
    def ConfigureMediaProtectionManager(self: Windows.Media.Protection.PlayReady.IPlayReadyLicenseSession, mpm: Windows.Media.Protection.MediaProtectionManager) -> Void: ...
    @winrt_mixinmethod
    def CreateLicenseIterable(self: Windows.Media.Protection.PlayReady.IPlayReadyLicenseSession2, contentHeader: Windows.Media.Protection.PlayReady.PlayReadyContentHeader, fullyEvaluated: Boolean) -> Windows.Media.Protection.PlayReady.PlayReadyLicenseIterable: ...
class PlayReadyMeteringReportServiceRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Protection.PlayReady.IPlayReadyMeteringReportServiceRequest
    _classid_ = 'Windows.Media.Protection.PlayReady.PlayReadyMeteringReportServiceRequest'
    @winrt_activatemethod
    def New(cls) -> Windows.Media.Protection.PlayReady.PlayReadyMeteringReportServiceRequest: ...
    @winrt_mixinmethod
    def get_MeteringCertificate(self: Windows.Media.Protection.PlayReady.IPlayReadyMeteringReportServiceRequest) -> c_char_p_no: ...
    @winrt_mixinmethod
    def put_MeteringCertificate(self: Windows.Media.Protection.PlayReady.IPlayReadyMeteringReportServiceRequest, meteringCertBytes: c_char_p_no) -> Void: ...
    @winrt_mixinmethod
    def get_Uri(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_Uri(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_ResponseCustomData(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ChallengeCustomData(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ChallengeCustomData(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def BeginServiceRequest(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def NextServiceRequest(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest: ...
    @winrt_mixinmethod
    def GenerateManualEnablingChallenge(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> Windows.Media.Protection.PlayReady.PlayReadySoapMessage: ...
    @winrt_mixinmethod
    def ProcessManualEnablingResponse(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest, responseBytes: c_char_p_no) -> Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_ProtectionSystem(self: Windows.Media.Protection.IMediaProtectionServiceRequest) -> Guid: ...
    @winrt_mixinmethod
    def get_Type(self: Windows.Media.Protection.IMediaProtectionServiceRequest) -> Guid: ...
    MeteringCertificate = property(get_MeteringCertificate, put_MeteringCertificate)
    Uri = property(get_Uri, put_Uri)
    ResponseCustomData = property(get_ResponseCustomData, None)
    ChallengeCustomData = property(get_ChallengeCustomData, put_ChallengeCustomData)
    ProtectionSystem = property(get_ProtectionSystem, None)
    Type = property(get_Type, None)
class PlayReadyRevocationServiceRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Protection.PlayReady.IPlayReadyRevocationServiceRequest
    _classid_ = 'Windows.Media.Protection.PlayReady.PlayReadyRevocationServiceRequest'
    @winrt_activatemethod
    def New(cls) -> Windows.Media.Protection.PlayReady.PlayReadyRevocationServiceRequest: ...
    @winrt_mixinmethod
    def get_Uri(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_Uri(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_ResponseCustomData(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ChallengeCustomData(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ChallengeCustomData(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def BeginServiceRequest(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def NextServiceRequest(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest: ...
    @winrt_mixinmethod
    def GenerateManualEnablingChallenge(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> Windows.Media.Protection.PlayReady.PlayReadySoapMessage: ...
    @winrt_mixinmethod
    def ProcessManualEnablingResponse(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest, responseBytes: c_char_p_no) -> Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_ProtectionSystem(self: Windows.Media.Protection.IMediaProtectionServiceRequest) -> Guid: ...
    @winrt_mixinmethod
    def get_Type(self: Windows.Media.Protection.IMediaProtectionServiceRequest) -> Guid: ...
    Uri = property(get_Uri, put_Uri)
    ResponseCustomData = property(get_ResponseCustomData, None)
    ChallengeCustomData = property(get_ChallengeCustomData, put_ChallengeCustomData)
    ProtectionSystem = property(get_ProtectionSystem, None)
    Type = property(get_Type, None)
class PlayReadySecureStopIterable(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Foundation.Collections.IIterable[Windows.Media.Protection.PlayReady.IPlayReadySecureStopServiceRequest]
    _classid_ = 'Windows.Media.Protection.PlayReady.PlayReadySecureStopIterable'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.Media.Protection.PlayReady.IPlayReadySecureStopIterableFactory, publisherCertBytes: c_char_p_no) -> Windows.Media.Protection.PlayReady.PlayReadySecureStopIterable: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.Media.Protection.PlayReady.IPlayReadySecureStopServiceRequest]) -> Windows.Foundation.Collections.IIterator[Windows.Media.Protection.PlayReady.IPlayReadySecureStopServiceRequest]: ...
class PlayReadySecureStopIterator(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Foundation.Collections.IIterator[Windows.Media.Protection.PlayReady.IPlayReadySecureStopServiceRequest]
    _classid_ = 'Windows.Media.Protection.PlayReady.PlayReadySecureStopIterator'
    @winrt_mixinmethod
    def get_Current(self: Windows.Foundation.Collections.IIterator[Windows.Media.Protection.PlayReady.IPlayReadySecureStopServiceRequest]) -> Windows.Media.Protection.PlayReady.IPlayReadySecureStopServiceRequest: ...
    @winrt_mixinmethod
    def get_HasCurrent(self: Windows.Foundation.Collections.IIterator[Windows.Media.Protection.PlayReady.IPlayReadySecureStopServiceRequest]) -> Boolean: ...
    @winrt_mixinmethod
    def MoveNext(self: Windows.Foundation.Collections.IIterator[Windows.Media.Protection.PlayReady.IPlayReadySecureStopServiceRequest]) -> Boolean: ...
    @winrt_mixinmethod
    def GetMany(self: Windows.Foundation.Collections.IIterator[Windows.Media.Protection.PlayReady.IPlayReadySecureStopServiceRequest], items: POINTER(Windows.Media.Protection.PlayReady.IPlayReadySecureStopServiceRequest)) -> UInt32: ...
    Current = property(get_Current, None)
    HasCurrent = property(get_HasCurrent, None)
class PlayReadySecureStopServiceRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Protection.PlayReady.IPlayReadySecureStopServiceRequest
    _classid_ = 'Windows.Media.Protection.PlayReady.PlayReadySecureStopServiceRequest'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.Media.Protection.PlayReady.IPlayReadySecureStopServiceRequestFactory, publisherCertBytes: c_char_p_no) -> Windows.Media.Protection.PlayReady.PlayReadySecureStopServiceRequest: ...
    @winrt_factorymethod
    def CreateInstanceFromSessionID(cls: Windows.Media.Protection.PlayReady.IPlayReadySecureStopServiceRequestFactory, sessionID: Guid, publisherCertBytes: c_char_p_no) -> Windows.Media.Protection.PlayReady.PlayReadySecureStopServiceRequest: ...
    @winrt_mixinmethod
    def get_SessionID(self: Windows.Media.Protection.PlayReady.IPlayReadySecureStopServiceRequest) -> Guid: ...
    @winrt_mixinmethod
    def get_StartTime(self: Windows.Media.Protection.PlayReady.IPlayReadySecureStopServiceRequest) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_UpdateTime(self: Windows.Media.Protection.PlayReady.IPlayReadySecureStopServiceRequest) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_Stopped(self: Windows.Media.Protection.PlayReady.IPlayReadySecureStopServiceRequest) -> Boolean: ...
    @winrt_mixinmethod
    def get_PublisherCertificate(self: Windows.Media.Protection.PlayReady.IPlayReadySecureStopServiceRequest) -> c_char_p_no: ...
    @winrt_mixinmethod
    def get_Uri(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_Uri(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_ResponseCustomData(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ChallengeCustomData(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ChallengeCustomData(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def BeginServiceRequest(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def NextServiceRequest(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest: ...
    @winrt_mixinmethod
    def GenerateManualEnablingChallenge(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest) -> Windows.Media.Protection.PlayReady.PlayReadySoapMessage: ...
    @winrt_mixinmethod
    def ProcessManualEnablingResponse(self: Windows.Media.Protection.PlayReady.IPlayReadyServiceRequest, responseBytes: c_char_p_no) -> Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_ProtectionSystem(self: Windows.Media.Protection.IMediaProtectionServiceRequest) -> Guid: ...
    @winrt_mixinmethod
    def get_Type(self: Windows.Media.Protection.IMediaProtectionServiceRequest) -> Guid: ...
    SessionID = property(get_SessionID, None)
    StartTime = property(get_StartTime, None)
    UpdateTime = property(get_UpdateTime, None)
    Stopped = property(get_Stopped, None)
    PublisherCertificate = property(get_PublisherCertificate, None)
    Uri = property(get_Uri, put_Uri)
    ResponseCustomData = property(get_ResponseCustomData, None)
    ChallengeCustomData = property(get_ChallengeCustomData, put_ChallengeCustomData)
    ProtectionSystem = property(get_ProtectionSystem, None)
    Type = property(get_Type, None)
class PlayReadySoapMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Protection.PlayReady.IPlayReadySoapMessage
    _classid_ = 'Windows.Media.Protection.PlayReady.PlayReadySoapMessage'
    @winrt_mixinmethod
    def GetMessageBody(self: Windows.Media.Protection.PlayReady.IPlayReadySoapMessage) -> c_char_p_no: ...
    @winrt_mixinmethod
    def get_MessageHeaders(self: Windows.Media.Protection.PlayReady.IPlayReadySoapMessage) -> Windows.Foundation.Collections.IPropertySet: ...
    @winrt_mixinmethod
    def get_Uri(self: Windows.Media.Protection.PlayReady.IPlayReadySoapMessage) -> Windows.Foundation.Uri: ...
    MessageHeaders = property(get_MessageHeaders, None)
    Uri = property(get_Uri, None)
class PlayReadyStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.PlayReady.PlayReadyStatics'
    @winrt_classmethod
    def get_HardwareDRMDisabledAtTime(cls: Windows.Media.Protection.PlayReady.IPlayReadyStatics5) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_classmethod
    def get_HardwareDRMDisabledUntilTime(cls: Windows.Media.Protection.PlayReady.IPlayReadyStatics5) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_classmethod
    def ResetHardwareDRMDisabled(cls: Windows.Media.Protection.PlayReady.IPlayReadyStatics5) -> Void: ...
    @winrt_classmethod
    def get_InputTrustAuthorityToCreate(cls: Windows.Media.Protection.PlayReady.IPlayReadyStatics4) -> WinRT_String: ...
    @winrt_classmethod
    def get_ProtectionSystemId(cls: Windows.Media.Protection.PlayReady.IPlayReadyStatics4) -> Guid: ...
    @winrt_classmethod
    def get_SecureStopServiceRequestType(cls: Windows.Media.Protection.PlayReady.IPlayReadyStatics3) -> Guid: ...
    @winrt_classmethod
    def CheckSupportedHardware(cls: Windows.Media.Protection.PlayReady.IPlayReadyStatics3, hwdrmFeature: Windows.Media.Protection.PlayReady.PlayReadyHardwareDRMFeatures) -> Boolean: ...
    @winrt_classmethod
    def get_PlayReadyCertificateSecurityLevel(cls: Windows.Media.Protection.PlayReady.IPlayReadyStatics2) -> UInt32: ...
    @winrt_classmethod
    def get_DomainJoinServiceRequestType(cls: Windows.Media.Protection.PlayReady.IPlayReadyStatics) -> Guid: ...
    @winrt_classmethod
    def get_DomainLeaveServiceRequestType(cls: Windows.Media.Protection.PlayReady.IPlayReadyStatics) -> Guid: ...
    @winrt_classmethod
    def get_IndividualizationServiceRequestType(cls: Windows.Media.Protection.PlayReady.IPlayReadyStatics) -> Guid: ...
    @winrt_classmethod
    def get_LicenseAcquirerServiceRequestType(cls: Windows.Media.Protection.PlayReady.IPlayReadyStatics) -> Guid: ...
    @winrt_classmethod
    def get_MeteringReportServiceRequestType(cls: Windows.Media.Protection.PlayReady.IPlayReadyStatics) -> Guid: ...
    @winrt_classmethod
    def get_RevocationServiceRequestType(cls: Windows.Media.Protection.PlayReady.IPlayReadyStatics) -> Guid: ...
    @winrt_classmethod
    def get_MediaProtectionSystemId(cls: Windows.Media.Protection.PlayReady.IPlayReadyStatics) -> Guid: ...
    @winrt_classmethod
    def get_PlayReadySecurityVersion(cls: Windows.Media.Protection.PlayReady.IPlayReadyStatics) -> UInt32: ...
    HardwareDRMDisabledAtTime = property(get_HardwareDRMDisabledAtTime, None)
    HardwareDRMDisabledUntilTime = property(get_HardwareDRMDisabledUntilTime, None)
    InputTrustAuthorityToCreate = property(get_InputTrustAuthorityToCreate, None)
    ProtectionSystemId = property(get_ProtectionSystemId, None)
    SecureStopServiceRequestType = property(get_SecureStopServiceRequestType, None)
    PlayReadyCertificateSecurityLevel = property(get_PlayReadyCertificateSecurityLevel, None)
    DomainJoinServiceRequestType = property(get_DomainJoinServiceRequestType, None)
    DomainLeaveServiceRequestType = property(get_DomainLeaveServiceRequestType, None)
    IndividualizationServiceRequestType = property(get_IndividualizationServiceRequestType, None)
    LicenseAcquirerServiceRequestType = property(get_LicenseAcquirerServiceRequestType, None)
    MeteringReportServiceRequestType = property(get_MeteringReportServiceRequestType, None)
    RevocationServiceRequestType = property(get_RevocationServiceRequestType, None)
    MediaProtectionSystemId = property(get_MediaProtectionSystemId, None)
    PlayReadySecurityVersion = property(get_PlayReadySecurityVersion, None)
make_head(_module, 'INDClient')
make_head(_module, 'INDClientFactory')
make_head(_module, 'INDClosedCaptionDataReceivedEventArgs')
make_head(_module, 'INDCustomData')
make_head(_module, 'INDCustomDataFactory')
make_head(_module, 'INDDownloadEngine')
make_head(_module, 'INDDownloadEngineNotifier')
make_head(_module, 'INDLicenseFetchCompletedEventArgs')
make_head(_module, 'INDLicenseFetchDescriptor')
make_head(_module, 'INDLicenseFetchDescriptorFactory')
make_head(_module, 'INDLicenseFetchResult')
make_head(_module, 'INDMessenger')
make_head(_module, 'INDProximityDetectionCompletedEventArgs')
make_head(_module, 'INDRegistrationCompletedEventArgs')
make_head(_module, 'INDSendResult')
make_head(_module, 'INDStartResult')
make_head(_module, 'INDStorageFileHelper')
make_head(_module, 'INDStreamParser')
make_head(_module, 'INDStreamParserNotifier')
make_head(_module, 'INDTCPMessengerFactory')
make_head(_module, 'INDTransmitterProperties')
make_head(_module, 'IPlayReadyContentHeader')
make_head(_module, 'IPlayReadyContentHeader2')
make_head(_module, 'IPlayReadyContentHeaderFactory')
make_head(_module, 'IPlayReadyContentHeaderFactory2')
make_head(_module, 'IPlayReadyContentResolver')
make_head(_module, 'IPlayReadyDomain')
make_head(_module, 'IPlayReadyDomainIterableFactory')
make_head(_module, 'IPlayReadyDomainJoinServiceRequest')
make_head(_module, 'IPlayReadyDomainLeaveServiceRequest')
make_head(_module, 'IPlayReadyITADataGenerator')
make_head(_module, 'IPlayReadyIndividualizationServiceRequest')
make_head(_module, 'IPlayReadyLicense')
make_head(_module, 'IPlayReadyLicense2')
make_head(_module, 'IPlayReadyLicenseAcquisitionServiceRequest')
make_head(_module, 'IPlayReadyLicenseAcquisitionServiceRequest2')
make_head(_module, 'IPlayReadyLicenseAcquisitionServiceRequest3')
make_head(_module, 'IPlayReadyLicenseIterableFactory')
make_head(_module, 'IPlayReadyLicenseManagement')
make_head(_module, 'IPlayReadyLicenseSession')
make_head(_module, 'IPlayReadyLicenseSession2')
make_head(_module, 'IPlayReadyLicenseSessionFactory')
make_head(_module, 'IPlayReadyMeteringReportServiceRequest')
make_head(_module, 'IPlayReadyRevocationServiceRequest')
make_head(_module, 'IPlayReadySecureStopIterableFactory')
make_head(_module, 'IPlayReadySecureStopServiceRequest')
make_head(_module, 'IPlayReadySecureStopServiceRequestFactory')
make_head(_module, 'IPlayReadyServiceRequest')
make_head(_module, 'IPlayReadySoapMessage')
make_head(_module, 'IPlayReadyStatics')
make_head(_module, 'IPlayReadyStatics2')
make_head(_module, 'IPlayReadyStatics3')
make_head(_module, 'IPlayReadyStatics4')
make_head(_module, 'IPlayReadyStatics5')
make_head(_module, 'NDClient')
make_head(_module, 'NDCustomData')
make_head(_module, 'NDDownloadEngineNotifier')
make_head(_module, 'NDLicenseFetchDescriptor')
make_head(_module, 'NDStorageFileHelper')
make_head(_module, 'NDStreamParserNotifier')
make_head(_module, 'NDTCPMessenger')
make_head(_module, 'PlayReadyContentHeader')
make_head(_module, 'PlayReadyContentResolver')
make_head(_module, 'PlayReadyDomain')
make_head(_module, 'PlayReadyDomainIterable')
make_head(_module, 'PlayReadyDomainIterator')
make_head(_module, 'PlayReadyDomainJoinServiceRequest')
make_head(_module, 'PlayReadyDomainLeaveServiceRequest')
make_head(_module, 'PlayReadyITADataGenerator')
make_head(_module, 'PlayReadyIndividualizationServiceRequest')
make_head(_module, 'PlayReadyLicense')
make_head(_module, 'PlayReadyLicenseAcquisitionServiceRequest')
make_head(_module, 'PlayReadyLicenseIterable')
make_head(_module, 'PlayReadyLicenseIterator')
make_head(_module, 'PlayReadyLicenseManagement')
make_head(_module, 'PlayReadyLicenseSession')
make_head(_module, 'PlayReadyMeteringReportServiceRequest')
make_head(_module, 'PlayReadyRevocationServiceRequest')
make_head(_module, 'PlayReadySecureStopIterable')
make_head(_module, 'PlayReadySecureStopIterator')
make_head(_module, 'PlayReadySecureStopServiceRequest')
make_head(_module, 'PlayReadySoapMessage')
make_head(_module, 'PlayReadyStatics')
