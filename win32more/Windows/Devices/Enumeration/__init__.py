from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import Annotated, Generic, K, MulticastDelegate, SZArray, T, TProgress, TResult, TSender, V, WinRT_String, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel.Background
import win32more.Windows.Devices.Enumeration
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Security.Credentials
import win32more.Windows.Storage.Streams
import win32more.Windows.UI
import win32more.Windows.UI.Popups
import win32more.Windows.Win32.System.WinRT
class DeviceAccessChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Enumeration.IDeviceAccessChangedEventArgs
    _classid_ = 'Windows.Devices.Enumeration.DeviceAccessChangedEventArgs'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Devices.Enumeration.IDeviceAccessChangedEventArgs) -> win32more.Windows.Devices.Enumeration.DeviceAccessStatus: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Devices.Enumeration.IDeviceAccessChangedEventArgs2) -> WinRT_String: ...
    Status = property(get_Status, None)
    Id = property(get_Id, None)
class DeviceAccessInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Enumeration.IDeviceAccessInformation
    _classid_ = 'Windows.Devices.Enumeration.DeviceAccessInformation'
    @winrt_mixinmethod
    def add_AccessChanged(self: win32more.Windows.Devices.Enumeration.IDeviceAccessInformation, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Enumeration.DeviceAccessInformation, win32more.Windows.Devices.Enumeration.DeviceAccessChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AccessChanged(self: win32more.Windows.Devices.Enumeration.IDeviceAccessInformation, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_CurrentStatus(self: win32more.Windows.Devices.Enumeration.IDeviceAccessInformation) -> win32more.Windows.Devices.Enumeration.DeviceAccessStatus: ...
    @winrt_classmethod
    def CreateFromId(cls: win32more.Windows.Devices.Enumeration.IDeviceAccessInformationStatics, deviceId: WinRT_String) -> win32more.Windows.Devices.Enumeration.DeviceAccessInformation: ...
    @winrt_classmethod
    def CreateFromDeviceClassId(cls: win32more.Windows.Devices.Enumeration.IDeviceAccessInformationStatics, deviceClassId: Guid) -> win32more.Windows.Devices.Enumeration.DeviceAccessInformation: ...
    @winrt_classmethod
    def CreateFromDeviceClass(cls: win32more.Windows.Devices.Enumeration.IDeviceAccessInformationStatics, deviceClass: win32more.Windows.Devices.Enumeration.DeviceClass) -> win32more.Windows.Devices.Enumeration.DeviceAccessInformation: ...
    CurrentStatus = property(get_CurrentStatus, None)
DeviceAccessStatus = Int32
DeviceAccessStatus_Unspecified: DeviceAccessStatus = 0
DeviceAccessStatus_Allowed: DeviceAccessStatus = 1
DeviceAccessStatus_DeniedByUser: DeviceAccessStatus = 2
DeviceAccessStatus_DeniedBySystem: DeviceAccessStatus = 3
DeviceClass = Int32
DeviceClass_All: DeviceClass = 0
DeviceClass_AudioCapture: DeviceClass = 1
DeviceClass_AudioRender: DeviceClass = 2
DeviceClass_PortableStorageDevice: DeviceClass = 3
DeviceClass_VideoCapture: DeviceClass = 4
DeviceClass_ImageScanner: DeviceClass = 5
DeviceClass_Location: DeviceClass = 6
class DeviceConnectionChangeTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Enumeration.IDeviceConnectionChangeTriggerDetails
    _classid_ = 'Windows.Devices.Enumeration.DeviceConnectionChangeTriggerDetails'
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.Devices.Enumeration.IDeviceConnectionChangeTriggerDetails) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
class DeviceDisconnectButtonClickedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Enumeration.IDeviceDisconnectButtonClickedEventArgs
    _classid_ = 'Windows.Devices.Enumeration.DeviceDisconnectButtonClickedEventArgs'
    @winrt_mixinmethod
    def get_Device(self: win32more.Windows.Devices.Enumeration.IDeviceDisconnectButtonClickedEventArgs) -> win32more.Windows.Devices.Enumeration.DeviceInformation: ...
    Device = property(get_Device, None)
class DeviceInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Enumeration.IDeviceInformation
    _classid_ = 'Windows.Devices.Enumeration.DeviceInformation'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Devices.Enumeration.IDeviceInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Devices.Enumeration.IDeviceInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsEnabled(self: win32more.Windows.Devices.Enumeration.IDeviceInformation) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsDefault(self: win32more.Windows.Devices.Enumeration.IDeviceInformation) -> Boolean: ...
    @winrt_mixinmethod
    def get_EnclosureLocation(self: win32more.Windows.Devices.Enumeration.IDeviceInformation) -> win32more.Windows.Devices.Enumeration.EnclosureLocation: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Devices.Enumeration.IDeviceInformation) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    @winrt_mixinmethod
    def Update(self: win32more.Windows.Devices.Enumeration.IDeviceInformation, updateInfo: win32more.Windows.Devices.Enumeration.DeviceInformationUpdate) -> Void: ...
    @winrt_mixinmethod
    def GetThumbnailAsync(self: win32more.Windows.Devices.Enumeration.IDeviceInformation) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.DeviceThumbnail]: ...
    @winrt_mixinmethod
    def GetGlyphThumbnailAsync(self: win32more.Windows.Devices.Enumeration.IDeviceInformation) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.DeviceThumbnail]: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.Devices.Enumeration.IDeviceInformation2) -> win32more.Windows.Devices.Enumeration.DeviceInformationKind: ...
    @winrt_mixinmethod
    def get_Pairing(self: win32more.Windows.Devices.Enumeration.IDeviceInformation2) -> win32more.Windows.Devices.Enumeration.DeviceInformationPairing: ...
    @winrt_classmethod
    def GetAqsFilterFromDeviceClass(cls: win32more.Windows.Devices.Enumeration.IDeviceInformationStatics2, deviceClass: win32more.Windows.Devices.Enumeration.DeviceClass) -> WinRT_String: ...
    @winrt_classmethod
    def CreateFromIdAsyncWithKindAndAdditionalProperties(cls: win32more.Windows.Devices.Enumeration.IDeviceInformationStatics2, deviceId: WinRT_String, additionalProperties: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], kind: win32more.Windows.Devices.Enumeration.DeviceInformationKind) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.DeviceInformation]: ...
    @winrt_classmethod
    def FindAllAsyncWithKindAqsFilterAndAdditionalProperties(cls: win32more.Windows.Devices.Enumeration.IDeviceInformationStatics2, aqsFilter: WinRT_String, additionalProperties: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], kind: win32more.Windows.Devices.Enumeration.DeviceInformationKind) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.DeviceInformationCollection]: ...
    @winrt_classmethod
    def CreateWatcherWithKindAqsFilterAndAdditionalProperties(cls: win32more.Windows.Devices.Enumeration.IDeviceInformationStatics2, aqsFilter: WinRT_String, additionalProperties: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], kind: win32more.Windows.Devices.Enumeration.DeviceInformationKind) -> win32more.Windows.Devices.Enumeration.DeviceWatcher: ...
    @winrt_classmethod
    def CreateFromIdAsync(cls: win32more.Windows.Devices.Enumeration.IDeviceInformationStatics, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.DeviceInformation]: ...
    @winrt_classmethod
    def CreateFromIdAsyncAdditionalProperties(cls: win32more.Windows.Devices.Enumeration.IDeviceInformationStatics, deviceId: WinRT_String, additionalProperties: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.DeviceInformation]: ...
    @winrt_classmethod
    def FindAllAsync(cls: win32more.Windows.Devices.Enumeration.IDeviceInformationStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.DeviceInformationCollection]: ...
    @winrt_classmethod
    def FindAllAsyncDeviceClass(cls: win32more.Windows.Devices.Enumeration.IDeviceInformationStatics, deviceClass: win32more.Windows.Devices.Enumeration.DeviceClass) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.DeviceInformationCollection]: ...
    @winrt_classmethod
    def FindAllAsyncAqsFilter(cls: win32more.Windows.Devices.Enumeration.IDeviceInformationStatics, aqsFilter: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.DeviceInformationCollection]: ...
    @winrt_classmethod
    def FindAllAsyncAqsFilterAndAdditionalProperties(cls: win32more.Windows.Devices.Enumeration.IDeviceInformationStatics, aqsFilter: WinRT_String, additionalProperties: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.DeviceInformationCollection]: ...
    @winrt_classmethod
    def CreateWatcher(cls: win32more.Windows.Devices.Enumeration.IDeviceInformationStatics) -> win32more.Windows.Devices.Enumeration.DeviceWatcher: ...
    @winrt_classmethod
    def CreateWatcherDeviceClass(cls: win32more.Windows.Devices.Enumeration.IDeviceInformationStatics, deviceClass: win32more.Windows.Devices.Enumeration.DeviceClass) -> win32more.Windows.Devices.Enumeration.DeviceWatcher: ...
    @winrt_classmethod
    def CreateWatcherAqsFilter(cls: win32more.Windows.Devices.Enumeration.IDeviceInformationStatics, aqsFilter: WinRT_String) -> win32more.Windows.Devices.Enumeration.DeviceWatcher: ...
    @winrt_classmethod
    def CreateWatcherAqsFilterAndAdditionalProperties(cls: win32more.Windows.Devices.Enumeration.IDeviceInformationStatics, aqsFilter: WinRT_String, additionalProperties: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Devices.Enumeration.DeviceWatcher: ...
    Id = property(get_Id, None)
    Name = property(get_Name, None)
    IsEnabled = property(get_IsEnabled, None)
    IsDefault = property(get_IsDefault, None)
    EnclosureLocation = property(get_EnclosureLocation, None)
    Properties = property(get_Properties, None)
    Kind = property(get_Kind, None)
    Pairing = property(get_Pairing, None)
class DeviceInformationCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Enumeration.DeviceInformation]
    _classid_ = 'Windows.Devices.Enumeration.DeviceInformationCollection'
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Enumeration.DeviceInformation], index: UInt32) -> win32more.Windows.Devices.Enumeration.DeviceInformation: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Enumeration.DeviceInformation]) -> UInt32: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Enumeration.DeviceInformation], value: win32more.Windows.Devices.Enumeration.DeviceInformation, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Enumeration.DeviceInformation], startIndex: UInt32, items: Annotated[SZArray[win32more.Windows.Devices.Enumeration.DeviceInformation], 'Out']) -> UInt32: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Devices.Enumeration.DeviceInformation]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Devices.Enumeration.DeviceInformation]: ...
    Size = property(get_Size, None)
class DeviceInformationCustomPairing(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Enumeration.IDeviceInformationCustomPairing
    _classid_ = 'Windows.Devices.Enumeration.DeviceInformationCustomPairing'
    @winrt_mixinmethod
    def PairAsync(self: win32more.Windows.Devices.Enumeration.IDeviceInformationCustomPairing, pairingKindsSupported: win32more.Windows.Devices.Enumeration.DevicePairingKinds) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.DevicePairingResult]: ...
    @winrt_mixinmethod
    def PairWithProtectionLevelAsync(self: win32more.Windows.Devices.Enumeration.IDeviceInformationCustomPairing, pairingKindsSupported: win32more.Windows.Devices.Enumeration.DevicePairingKinds, minProtectionLevel: win32more.Windows.Devices.Enumeration.DevicePairingProtectionLevel) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.DevicePairingResult]: ...
    @winrt_mixinmethod
    def PairWithProtectionLevelAndSettingsAsync(self: win32more.Windows.Devices.Enumeration.IDeviceInformationCustomPairing, pairingKindsSupported: win32more.Windows.Devices.Enumeration.DevicePairingKinds, minProtectionLevel: win32more.Windows.Devices.Enumeration.DevicePairingProtectionLevel, devicePairingSettings: win32more.Windows.Devices.Enumeration.IDevicePairingSettings) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.DevicePairingResult]: ...
    @winrt_mixinmethod
    def add_PairingRequested(self: win32more.Windows.Devices.Enumeration.IDeviceInformationCustomPairing, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Enumeration.DeviceInformationCustomPairing, win32more.Windows.Devices.Enumeration.DevicePairingRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PairingRequested(self: win32more.Windows.Devices.Enumeration.IDeviceInformationCustomPairing, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
DeviceInformationKind = Int32
DeviceInformationKind_Unknown: DeviceInformationKind = 0
DeviceInformationKind_DeviceInterface: DeviceInformationKind = 1
DeviceInformationKind_DeviceContainer: DeviceInformationKind = 2
DeviceInformationKind_Device: DeviceInformationKind = 3
DeviceInformationKind_DeviceInterfaceClass: DeviceInformationKind = 4
DeviceInformationKind_AssociationEndpoint: DeviceInformationKind = 5
DeviceInformationKind_AssociationEndpointContainer: DeviceInformationKind = 6
DeviceInformationKind_AssociationEndpointService: DeviceInformationKind = 7
DeviceInformationKind_DevicePanel: DeviceInformationKind = 8
class DeviceInformationPairing(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Enumeration.IDeviceInformationPairing
    _classid_ = 'Windows.Devices.Enumeration.DeviceInformationPairing'
    @winrt_mixinmethod
    def get_IsPaired(self: win32more.Windows.Devices.Enumeration.IDeviceInformationPairing) -> Boolean: ...
    @winrt_mixinmethod
    def get_CanPair(self: win32more.Windows.Devices.Enumeration.IDeviceInformationPairing) -> Boolean: ...
    @winrt_mixinmethod
    def PairAsync(self: win32more.Windows.Devices.Enumeration.IDeviceInformationPairing) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.DevicePairingResult]: ...
    @winrt_mixinmethod
    def PairWithProtectionLevelAsync(self: win32more.Windows.Devices.Enumeration.IDeviceInformationPairing, minProtectionLevel: win32more.Windows.Devices.Enumeration.DevicePairingProtectionLevel) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.DevicePairingResult]: ...
    @winrt_mixinmethod
    def get_ProtectionLevel(self: win32more.Windows.Devices.Enumeration.IDeviceInformationPairing2) -> win32more.Windows.Devices.Enumeration.DevicePairingProtectionLevel: ...
    @winrt_mixinmethod
    def get_Custom(self: win32more.Windows.Devices.Enumeration.IDeviceInformationPairing2) -> win32more.Windows.Devices.Enumeration.DeviceInformationCustomPairing: ...
    @winrt_mixinmethod
    def PairWithProtectionLevelAndSettingsAsync(self: win32more.Windows.Devices.Enumeration.IDeviceInformationPairing2, minProtectionLevel: win32more.Windows.Devices.Enumeration.DevicePairingProtectionLevel, devicePairingSettings: win32more.Windows.Devices.Enumeration.IDevicePairingSettings) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.DevicePairingResult]: ...
    @winrt_mixinmethod
    def UnpairAsync(self: win32more.Windows.Devices.Enumeration.IDeviceInformationPairing2) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.DeviceUnpairingResult]: ...
    @winrt_classmethod
    def TryRegisterForAllInboundPairingRequestsWithProtectionLevel(cls: win32more.Windows.Devices.Enumeration.IDeviceInformationPairingStatics2, pairingKindsSupported: win32more.Windows.Devices.Enumeration.DevicePairingKinds, minProtectionLevel: win32more.Windows.Devices.Enumeration.DevicePairingProtectionLevel) -> Boolean: ...
    @winrt_classmethod
    def TryRegisterForAllInboundPairingRequests(cls: win32more.Windows.Devices.Enumeration.IDeviceInformationPairingStatics, pairingKindsSupported: win32more.Windows.Devices.Enumeration.DevicePairingKinds) -> Boolean: ...
    IsPaired = property(get_IsPaired, None)
    CanPair = property(get_CanPair, None)
    ProtectionLevel = property(get_ProtectionLevel, None)
    Custom = property(get_Custom, None)
class DeviceInformationUpdate(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Enumeration.IDeviceInformationUpdate
    _classid_ = 'Windows.Devices.Enumeration.DeviceInformationUpdate'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Devices.Enumeration.IDeviceInformationUpdate) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Devices.Enumeration.IDeviceInformationUpdate) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.Devices.Enumeration.IDeviceInformationUpdate2) -> win32more.Windows.Devices.Enumeration.DeviceInformationKind: ...
    Id = property(get_Id, None)
    Properties = property(get_Properties, None)
    Kind = property(get_Kind, None)
DevicePairingKinds = UInt32
DevicePairingKinds_None: DevicePairingKinds = 0
DevicePairingKinds_ConfirmOnly: DevicePairingKinds = 1
DevicePairingKinds_DisplayPin: DevicePairingKinds = 2
DevicePairingKinds_ProvidePin: DevicePairingKinds = 4
DevicePairingKinds_ConfirmPinMatch: DevicePairingKinds = 8
DevicePairingKinds_ProvidePasswordCredential: DevicePairingKinds = 16
DevicePairingProtectionLevel = Int32
DevicePairingProtectionLevel_Default: DevicePairingProtectionLevel = 0
DevicePairingProtectionLevel_None: DevicePairingProtectionLevel = 1
DevicePairingProtectionLevel_Encryption: DevicePairingProtectionLevel = 2
DevicePairingProtectionLevel_EncryptionAndAuthentication: DevicePairingProtectionLevel = 3
class DevicePairingRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Enumeration.IDevicePairingRequestedEventArgs
    _classid_ = 'Windows.Devices.Enumeration.DevicePairingRequestedEventArgs'
    @winrt_mixinmethod
    def get_DeviceInformation(self: win32more.Windows.Devices.Enumeration.IDevicePairingRequestedEventArgs) -> win32more.Windows.Devices.Enumeration.DeviceInformation: ...
    @winrt_mixinmethod
    def get_PairingKind(self: win32more.Windows.Devices.Enumeration.IDevicePairingRequestedEventArgs) -> win32more.Windows.Devices.Enumeration.DevicePairingKinds: ...
    @winrt_mixinmethod
    def get_Pin(self: win32more.Windows.Devices.Enumeration.IDevicePairingRequestedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def Accept(self: win32more.Windows.Devices.Enumeration.IDevicePairingRequestedEventArgs) -> Void: ...
    @winrt_mixinmethod
    def AcceptWithPin(self: win32more.Windows.Devices.Enumeration.IDevicePairingRequestedEventArgs, pin: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Devices.Enumeration.IDevicePairingRequestedEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    @winrt_mixinmethod
    def AcceptWithPasswordCredential(self: win32more.Windows.Devices.Enumeration.IDevicePairingRequestedEventArgs2, passwordCredential: win32more.Windows.Security.Credentials.PasswordCredential) -> Void: ...
    DeviceInformation = property(get_DeviceInformation, None)
    PairingKind = property(get_PairingKind, None)
    Pin = property(get_Pin, None)
class DevicePairingResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Enumeration.IDevicePairingResult
    _classid_ = 'Windows.Devices.Enumeration.DevicePairingResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Devices.Enumeration.IDevicePairingResult) -> win32more.Windows.Devices.Enumeration.DevicePairingResultStatus: ...
    @winrt_mixinmethod
    def get_ProtectionLevelUsed(self: win32more.Windows.Devices.Enumeration.IDevicePairingResult) -> win32more.Windows.Devices.Enumeration.DevicePairingProtectionLevel: ...
    Status = property(get_Status, None)
    ProtectionLevelUsed = property(get_ProtectionLevelUsed, None)
DevicePairingResultStatus = Int32
DevicePairingResultStatus_Paired: DevicePairingResultStatus = 0
DevicePairingResultStatus_NotReadyToPair: DevicePairingResultStatus = 1
DevicePairingResultStatus_NotPaired: DevicePairingResultStatus = 2
DevicePairingResultStatus_AlreadyPaired: DevicePairingResultStatus = 3
DevicePairingResultStatus_ConnectionRejected: DevicePairingResultStatus = 4
DevicePairingResultStatus_TooManyConnections: DevicePairingResultStatus = 5
DevicePairingResultStatus_HardwareFailure: DevicePairingResultStatus = 6
DevicePairingResultStatus_AuthenticationTimeout: DevicePairingResultStatus = 7
DevicePairingResultStatus_AuthenticationNotAllowed: DevicePairingResultStatus = 8
DevicePairingResultStatus_AuthenticationFailure: DevicePairingResultStatus = 9
DevicePairingResultStatus_NoSupportedProfiles: DevicePairingResultStatus = 10
DevicePairingResultStatus_ProtectionLevelCouldNotBeMet: DevicePairingResultStatus = 11
DevicePairingResultStatus_AccessDenied: DevicePairingResultStatus = 12
DevicePairingResultStatus_InvalidCeremonyData: DevicePairingResultStatus = 13
DevicePairingResultStatus_PairingCanceled: DevicePairingResultStatus = 14
DevicePairingResultStatus_OperationAlreadyInProgress: DevicePairingResultStatus = 15
DevicePairingResultStatus_RequiredHandlerNotRegistered: DevicePairingResultStatus = 16
DevicePairingResultStatus_RejectedByHandler: DevicePairingResultStatus = 17
DevicePairingResultStatus_RemoteDeviceHasAssociation: DevicePairingResultStatus = 18
DevicePairingResultStatus_Failed: DevicePairingResultStatus = 19
class DevicePicker(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Enumeration.IDevicePicker
    _classid_ = 'Windows.Devices.Enumeration.DevicePicker'
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 0:
            return win32more.Windows.Devices.Enumeration.DevicePicker.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.Enumeration.DevicePicker: ...
    @winrt_mixinmethod
    def get_Filter(self: win32more.Windows.Devices.Enumeration.IDevicePicker) -> win32more.Windows.Devices.Enumeration.DevicePickerFilter: ...
    @winrt_mixinmethod
    def get_Appearance(self: win32more.Windows.Devices.Enumeration.IDevicePicker) -> win32more.Windows.Devices.Enumeration.DevicePickerAppearance: ...
    @winrt_mixinmethod
    def get_RequestedProperties(self: win32more.Windows.Devices.Enumeration.IDevicePicker) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def add_DeviceSelected(self: win32more.Windows.Devices.Enumeration.IDevicePicker, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Enumeration.DevicePicker, win32more.Windows.Devices.Enumeration.DeviceSelectedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DeviceSelected(self: win32more.Windows.Devices.Enumeration.IDevicePicker, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DisconnectButtonClicked(self: win32more.Windows.Devices.Enumeration.IDevicePicker, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Enumeration.DevicePicker, win32more.Windows.Devices.Enumeration.DeviceDisconnectButtonClickedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DisconnectButtonClicked(self: win32more.Windows.Devices.Enumeration.IDevicePicker, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DevicePickerDismissed(self: win32more.Windows.Devices.Enumeration.IDevicePicker, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Enumeration.DevicePicker, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DevicePickerDismissed(self: win32more.Windows.Devices.Enumeration.IDevicePicker, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Show(self: win32more.Windows.Devices.Enumeration.IDevicePicker, selection: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_mixinmethod
    def ShowWithPlacement(self: win32more.Windows.Devices.Enumeration.IDevicePicker, selection: win32more.Windows.Foundation.Rect, placement: win32more.Windows.UI.Popups.Placement) -> Void: ...
    @winrt_mixinmethod
    def PickSingleDeviceAsync(self: win32more.Windows.Devices.Enumeration.IDevicePicker, selection: win32more.Windows.Foundation.Rect) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.DeviceInformation]: ...
    @winrt_mixinmethod
    def PickSingleDeviceAsyncWithPlacement(self: win32more.Windows.Devices.Enumeration.IDevicePicker, selection: win32more.Windows.Foundation.Rect, placement: win32more.Windows.UI.Popups.Placement) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.DeviceInformation]: ...
    @winrt_mixinmethod
    def Hide(self: win32more.Windows.Devices.Enumeration.IDevicePicker) -> Void: ...
    @winrt_mixinmethod
    def SetDisplayStatus(self: win32more.Windows.Devices.Enumeration.IDevicePicker, device: win32more.Windows.Devices.Enumeration.DeviceInformation, status: WinRT_String, options: win32more.Windows.Devices.Enumeration.DevicePickerDisplayStatusOptions) -> Void: ...
    Filter = property(get_Filter, None)
    Appearance = property(get_Appearance, None)
    RequestedProperties = property(get_RequestedProperties, None)
class DevicePickerAppearance(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Enumeration.IDevicePickerAppearance
    _classid_ = 'Windows.Devices.Enumeration.DevicePickerAppearance'
    @winrt_mixinmethod
    def get_Title(self: win32more.Windows.Devices.Enumeration.IDevicePickerAppearance) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Title(self: win32more.Windows.Devices.Enumeration.IDevicePickerAppearance, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ForegroundColor(self: win32more.Windows.Devices.Enumeration.IDevicePickerAppearance) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_ForegroundColor(self: win32more.Windows.Devices.Enumeration.IDevicePickerAppearance, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_BackgroundColor(self: win32more.Windows.Devices.Enumeration.IDevicePickerAppearance) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_BackgroundColor(self: win32more.Windows.Devices.Enumeration.IDevicePickerAppearance, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_AccentColor(self: win32more.Windows.Devices.Enumeration.IDevicePickerAppearance) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_AccentColor(self: win32more.Windows.Devices.Enumeration.IDevicePickerAppearance, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_SelectedForegroundColor(self: win32more.Windows.Devices.Enumeration.IDevicePickerAppearance) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_SelectedForegroundColor(self: win32more.Windows.Devices.Enumeration.IDevicePickerAppearance, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_SelectedBackgroundColor(self: win32more.Windows.Devices.Enumeration.IDevicePickerAppearance) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_SelectedBackgroundColor(self: win32more.Windows.Devices.Enumeration.IDevicePickerAppearance, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_SelectedAccentColor(self: win32more.Windows.Devices.Enumeration.IDevicePickerAppearance) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_SelectedAccentColor(self: win32more.Windows.Devices.Enumeration.IDevicePickerAppearance, value: win32more.Windows.UI.Color) -> Void: ...
    Title = property(get_Title, put_Title)
    ForegroundColor = property(get_ForegroundColor, put_ForegroundColor)
    BackgroundColor = property(get_BackgroundColor, put_BackgroundColor)
    AccentColor = property(get_AccentColor, put_AccentColor)
    SelectedForegroundColor = property(get_SelectedForegroundColor, put_SelectedForegroundColor)
    SelectedBackgroundColor = property(get_SelectedBackgroundColor, put_SelectedBackgroundColor)
    SelectedAccentColor = property(get_SelectedAccentColor, put_SelectedAccentColor)
DevicePickerDisplayStatusOptions = UInt32
DevicePickerDisplayStatusOptions_None: DevicePickerDisplayStatusOptions = 0
DevicePickerDisplayStatusOptions_ShowProgress: DevicePickerDisplayStatusOptions = 1
DevicePickerDisplayStatusOptions_ShowDisconnectButton: DevicePickerDisplayStatusOptions = 2
DevicePickerDisplayStatusOptions_ShowRetryButton: DevicePickerDisplayStatusOptions = 4
class DevicePickerFilter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Enumeration.IDevicePickerFilter
    _classid_ = 'Windows.Devices.Enumeration.DevicePickerFilter'
    @winrt_mixinmethod
    def get_SupportedDeviceClasses(self: win32more.Windows.Devices.Enumeration.IDevicePickerFilter) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Devices.Enumeration.DeviceClass]: ...
    @winrt_mixinmethod
    def get_SupportedDeviceSelectors(self: win32more.Windows.Devices.Enumeration.IDevicePickerFilter) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    SupportedDeviceClasses = property(get_SupportedDeviceClasses, None)
    SupportedDeviceSelectors = property(get_SupportedDeviceSelectors, None)
class DeviceSelectedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Enumeration.IDeviceSelectedEventArgs
    _classid_ = 'Windows.Devices.Enumeration.DeviceSelectedEventArgs'
    @winrt_mixinmethod
    def get_SelectedDevice(self: win32more.Windows.Devices.Enumeration.IDeviceSelectedEventArgs) -> win32more.Windows.Devices.Enumeration.DeviceInformation: ...
    SelectedDevice = property(get_SelectedDevice, None)
class DeviceThumbnail(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Streams.IRandomAccessStreamWithContentType
    _classid_ = 'Windows.Devices.Enumeration.DeviceThumbnail'
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Storage.Streams.IRandomAccessStream) -> UInt64: ...
    @winrt_mixinmethod
    def put_Size(self: win32more.Windows.Storage.Streams.IRandomAccessStream, value: UInt64) -> Void: ...
    @winrt_mixinmethod
    def GetInputStreamAt(self: win32more.Windows.Storage.Streams.IRandomAccessStream, position: UInt64) -> win32more.Windows.Storage.Streams.IInputStream: ...
    @winrt_mixinmethod
    def GetOutputStreamAt(self: win32more.Windows.Storage.Streams.IRandomAccessStream, position: UInt64) -> win32more.Windows.Storage.Streams.IOutputStream: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.Storage.Streams.IRandomAccessStream) -> UInt64: ...
    @winrt_mixinmethod
    def Seek(self: win32more.Windows.Storage.Streams.IRandomAccessStream, position: UInt64) -> Void: ...
    @winrt_mixinmethod
    def CloneStream(self: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_mixinmethod
    def get_CanRead(self: win32more.Windows.Storage.Streams.IRandomAccessStream) -> Boolean: ...
    @winrt_mixinmethod
    def get_CanWrite(self: win32more.Windows.Storage.Streams.IRandomAccessStream) -> Boolean: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def ReadAsync(self: win32more.Windows.Storage.Streams.IInputStream, buffer: win32more.Windows.Storage.Streams.IBuffer, count: UInt32, options: win32more.Windows.Storage.Streams.InputStreamOptions) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Storage.Streams.IBuffer, UInt32]: ...
    @winrt_mixinmethod
    def WriteAsync(self: win32more.Windows.Storage.Streams.IOutputStream, buffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[UInt32, UInt32]: ...
    @winrt_mixinmethod
    def FlushAsync(self: win32more.Windows.Storage.Streams.IOutputStream) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def get_ContentType(self: win32more.Windows.Storage.Streams.IContentTypeProvider) -> WinRT_String: ...
    Size = property(get_Size, put_Size)
    Position = property(get_Position, None)
    CanRead = property(get_CanRead, None)
    CanWrite = property(get_CanWrite, None)
    ContentType = property(get_ContentType, None)
class DeviceUnpairingResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Enumeration.IDeviceUnpairingResult
    _classid_ = 'Windows.Devices.Enumeration.DeviceUnpairingResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Devices.Enumeration.IDeviceUnpairingResult) -> win32more.Windows.Devices.Enumeration.DeviceUnpairingResultStatus: ...
    Status = property(get_Status, None)
DeviceUnpairingResultStatus = Int32
DeviceUnpairingResultStatus_Unpaired: DeviceUnpairingResultStatus = 0
DeviceUnpairingResultStatus_AlreadyUnpaired: DeviceUnpairingResultStatus = 1
DeviceUnpairingResultStatus_OperationAlreadyInProgress: DeviceUnpairingResultStatus = 2
DeviceUnpairingResultStatus_AccessDenied: DeviceUnpairingResultStatus = 3
DeviceUnpairingResultStatus_Failed: DeviceUnpairingResultStatus = 4
class DeviceWatcher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Enumeration.IDeviceWatcher
    _classid_ = 'Windows.Devices.Enumeration.DeviceWatcher'
    @winrt_mixinmethod
    def add_Added(self: win32more.Windows.Devices.Enumeration.IDeviceWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Enumeration.DeviceWatcher, win32more.Windows.Devices.Enumeration.DeviceInformation]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Added(self: win32more.Windows.Devices.Enumeration.IDeviceWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Updated(self: win32more.Windows.Devices.Enumeration.IDeviceWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Enumeration.DeviceWatcher, win32more.Windows.Devices.Enumeration.DeviceInformationUpdate]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Updated(self: win32more.Windows.Devices.Enumeration.IDeviceWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Removed(self: win32more.Windows.Devices.Enumeration.IDeviceWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Enumeration.DeviceWatcher, win32more.Windows.Devices.Enumeration.DeviceInformationUpdate]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Removed(self: win32more.Windows.Devices.Enumeration.IDeviceWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_EnumerationCompleted(self: win32more.Windows.Devices.Enumeration.IDeviceWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Enumeration.DeviceWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_EnumerationCompleted(self: win32more.Windows.Devices.Enumeration.IDeviceWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Stopped(self: win32more.Windows.Devices.Enumeration.IDeviceWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Enumeration.DeviceWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Stopped(self: win32more.Windows.Devices.Enumeration.IDeviceWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Devices.Enumeration.IDeviceWatcher) -> win32more.Windows.Devices.Enumeration.DeviceWatcherStatus: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.Devices.Enumeration.IDeviceWatcher) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.Devices.Enumeration.IDeviceWatcher) -> Void: ...
    @winrt_mixinmethod
    def GetBackgroundTrigger(self: win32more.Windows.Devices.Enumeration.IDeviceWatcher2, requestedEventKinds: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Devices.Enumeration.DeviceWatcherEventKind]) -> win32more.Windows.ApplicationModel.Background.DeviceWatcherTrigger: ...
    Status = property(get_Status, None)
class DeviceWatcherEvent(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Enumeration.IDeviceWatcherEvent
    _classid_ = 'Windows.Devices.Enumeration.DeviceWatcherEvent'
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.Devices.Enumeration.IDeviceWatcherEvent) -> win32more.Windows.Devices.Enumeration.DeviceWatcherEventKind: ...
    @winrt_mixinmethod
    def get_DeviceInformation(self: win32more.Windows.Devices.Enumeration.IDeviceWatcherEvent) -> win32more.Windows.Devices.Enumeration.DeviceInformation: ...
    @winrt_mixinmethod
    def get_DeviceInformationUpdate(self: win32more.Windows.Devices.Enumeration.IDeviceWatcherEvent) -> win32more.Windows.Devices.Enumeration.DeviceInformationUpdate: ...
    Kind = property(get_Kind, None)
    DeviceInformation = property(get_DeviceInformation, None)
    DeviceInformationUpdate = property(get_DeviceInformationUpdate, None)
DeviceWatcherEventKind = Int32
DeviceWatcherEventKind_Add: DeviceWatcherEventKind = 0
DeviceWatcherEventKind_Update: DeviceWatcherEventKind = 1
DeviceWatcherEventKind_Remove: DeviceWatcherEventKind = 2
DeviceWatcherStatus = Int32
DeviceWatcherStatus_Created: DeviceWatcherStatus = 0
DeviceWatcherStatus_Started: DeviceWatcherStatus = 1
DeviceWatcherStatus_EnumerationCompleted: DeviceWatcherStatus = 2
DeviceWatcherStatus_Stopping: DeviceWatcherStatus = 3
DeviceWatcherStatus_Stopped: DeviceWatcherStatus = 4
DeviceWatcherStatus_Aborted: DeviceWatcherStatus = 5
class DeviceWatcherTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Enumeration.IDeviceWatcherTriggerDetails
    _classid_ = 'Windows.Devices.Enumeration.DeviceWatcherTriggerDetails'
    @winrt_mixinmethod
    def get_DeviceWatcherEvents(self: win32more.Windows.Devices.Enumeration.IDeviceWatcherTriggerDetails) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Enumeration.DeviceWatcherEvent]: ...
    DeviceWatcherEvents = property(get_DeviceWatcherEvents, None)
class EnclosureLocation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Enumeration.IEnclosureLocation
    _classid_ = 'Windows.Devices.Enumeration.EnclosureLocation'
    @winrt_mixinmethod
    def get_InDock(self: win32more.Windows.Devices.Enumeration.IEnclosureLocation) -> Boolean: ...
    @winrt_mixinmethod
    def get_InLid(self: win32more.Windows.Devices.Enumeration.IEnclosureLocation) -> Boolean: ...
    @winrt_mixinmethod
    def get_Panel(self: win32more.Windows.Devices.Enumeration.IEnclosureLocation) -> win32more.Windows.Devices.Enumeration.Panel: ...
    @winrt_mixinmethod
    def get_RotationAngleInDegreesClockwise(self: win32more.Windows.Devices.Enumeration.IEnclosureLocation2) -> UInt32: ...
    InDock = property(get_InDock, None)
    InLid = property(get_InLid, None)
    Panel = property(get_Panel, None)
    RotationAngleInDegreesClockwise = property(get_RotationAngleInDegreesClockwise, None)
class IDeviceAccessChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Enumeration.IDeviceAccessChangedEventArgs'
    _iid_ = Guid('{deda0bcc-4f9d-4f58-9dba-a9bc800408d5}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Devices.Enumeration.DeviceAccessStatus: ...
    Status = property(get_Status, None)
class IDeviceAccessChangedEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Enumeration.IDeviceAccessChangedEventArgs2'
    _iid_ = Guid('{82523262-934b-4b30-a178-adc39f2f2be3}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    Id = property(get_Id, None)
class IDeviceAccessInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Enumeration.IDeviceAccessInformation'
    _iid_ = Guid('{0baa9a73-6de5-4915-8ddd-9a0554a6f545}')
    @winrt_commethod(6)
    def add_AccessChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Enumeration.DeviceAccessInformation, win32more.Windows.Devices.Enumeration.DeviceAccessChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_AccessChanged(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def get_CurrentStatus(self) -> win32more.Windows.Devices.Enumeration.DeviceAccessStatus: ...
    CurrentStatus = property(get_CurrentStatus, None)
class IDeviceAccessInformationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Enumeration.IDeviceAccessInformationStatics'
    _iid_ = Guid('{574bd3d3-5f30-45cd-8a94-724fe5973084}')
    @winrt_commethod(6)
    def CreateFromId(self, deviceId: WinRT_String) -> win32more.Windows.Devices.Enumeration.DeviceAccessInformation: ...
    @winrt_commethod(7)
    def CreateFromDeviceClassId(self, deviceClassId: Guid) -> win32more.Windows.Devices.Enumeration.DeviceAccessInformation: ...
    @winrt_commethod(8)
    def CreateFromDeviceClass(self, deviceClass: win32more.Windows.Devices.Enumeration.DeviceClass) -> win32more.Windows.Devices.Enumeration.DeviceAccessInformation: ...
class IDeviceConnectionChangeTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Enumeration.IDeviceConnectionChangeTriggerDetails'
    _iid_ = Guid('{b8578c0c-bbc1-484b-bffa-7b31dcc200b2}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
class IDeviceDisconnectButtonClickedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Enumeration.IDeviceDisconnectButtonClickedEventArgs'
    _iid_ = Guid('{8e44b56d-f902-4a00-b536-f37992e6a2a7}')
    @winrt_commethod(6)
    def get_Device(self) -> win32more.Windows.Devices.Enumeration.DeviceInformation: ...
    Device = property(get_Device, None)
class IDeviceInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Enumeration.IDeviceInformation'
    _iid_ = Guid('{aba0fb95-4398-489d-8e44-e6130927011f}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsDefault(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_EnclosureLocation(self) -> win32more.Windows.Devices.Enumeration.EnclosureLocation: ...
    @winrt_commethod(11)
    def get_Properties(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    @winrt_commethod(12)
    def Update(self, updateInfo: win32more.Windows.Devices.Enumeration.DeviceInformationUpdate) -> Void: ...
    @winrt_commethod(13)
    def GetThumbnailAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.DeviceThumbnail]: ...
    @winrt_commethod(14)
    def GetGlyphThumbnailAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.DeviceThumbnail]: ...
    Id = property(get_Id, None)
    Name = property(get_Name, None)
    IsEnabled = property(get_IsEnabled, None)
    IsDefault = property(get_IsDefault, None)
    EnclosureLocation = property(get_EnclosureLocation, None)
    Properties = property(get_Properties, None)
class IDeviceInformation2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Enumeration.IDeviceInformation2'
    _iid_ = Guid('{f156a638-7997-48d9-a10c-269d46533f48}')
    @winrt_commethod(6)
    def get_Kind(self) -> win32more.Windows.Devices.Enumeration.DeviceInformationKind: ...
    @winrt_commethod(7)
    def get_Pairing(self) -> win32more.Windows.Devices.Enumeration.DeviceInformationPairing: ...
    Kind = property(get_Kind, None)
    Pairing = property(get_Pairing, None)
class IDeviceInformationCustomPairing(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Enumeration.IDeviceInformationCustomPairing'
    _iid_ = Guid('{85138c02-4ee6-4914-8370-107a39144c0e}')
    @winrt_commethod(6)
    def PairAsync(self, pairingKindsSupported: win32more.Windows.Devices.Enumeration.DevicePairingKinds) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.DevicePairingResult]: ...
    @winrt_commethod(7)
    def PairWithProtectionLevelAsync(self, pairingKindsSupported: win32more.Windows.Devices.Enumeration.DevicePairingKinds, minProtectionLevel: win32more.Windows.Devices.Enumeration.DevicePairingProtectionLevel) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.DevicePairingResult]: ...
    @winrt_commethod(8)
    def PairWithProtectionLevelAndSettingsAsync(self, pairingKindsSupported: win32more.Windows.Devices.Enumeration.DevicePairingKinds, minProtectionLevel: win32more.Windows.Devices.Enumeration.DevicePairingProtectionLevel, devicePairingSettings: win32more.Windows.Devices.Enumeration.IDevicePairingSettings) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.DevicePairingResult]: ...
    @winrt_commethod(9)
    def add_PairingRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Enumeration.DeviceInformationCustomPairing, win32more.Windows.Devices.Enumeration.DevicePairingRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_PairingRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class IDeviceInformationPairing(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Enumeration.IDeviceInformationPairing'
    _iid_ = Guid('{2c4769f5-f684-40d5-8469-e8dbaab70485}')
    @winrt_commethod(6)
    def get_IsPaired(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_CanPair(self) -> Boolean: ...
    @winrt_commethod(8)
    def PairAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.DevicePairingResult]: ...
    @winrt_commethod(9)
    def PairWithProtectionLevelAsync(self, minProtectionLevel: win32more.Windows.Devices.Enumeration.DevicePairingProtectionLevel) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.DevicePairingResult]: ...
    IsPaired = property(get_IsPaired, None)
    CanPair = property(get_CanPair, None)
class IDeviceInformationPairing2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Enumeration.IDeviceInformationPairing2'
    _iid_ = Guid('{f68612fd-0aee-4328-85cc-1c742bb1790d}')
    @winrt_commethod(6)
    def get_ProtectionLevel(self) -> win32more.Windows.Devices.Enumeration.DevicePairingProtectionLevel: ...
    @winrt_commethod(7)
    def get_Custom(self) -> win32more.Windows.Devices.Enumeration.DeviceInformationCustomPairing: ...
    @winrt_commethod(8)
    def PairWithProtectionLevelAndSettingsAsync(self, minProtectionLevel: win32more.Windows.Devices.Enumeration.DevicePairingProtectionLevel, devicePairingSettings: win32more.Windows.Devices.Enumeration.IDevicePairingSettings) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.DevicePairingResult]: ...
    @winrt_commethod(9)
    def UnpairAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.DeviceUnpairingResult]: ...
    ProtectionLevel = property(get_ProtectionLevel, None)
    Custom = property(get_Custom, None)
class IDeviceInformationPairingStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Enumeration.IDeviceInformationPairingStatics'
    _iid_ = Guid('{e915c408-36d4-49a1-bf13-514173799b6b}')
    @winrt_commethod(6)
    def TryRegisterForAllInboundPairingRequests(self, pairingKindsSupported: win32more.Windows.Devices.Enumeration.DevicePairingKinds) -> Boolean: ...
class IDeviceInformationPairingStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Enumeration.IDeviceInformationPairingStatics2'
    _iid_ = Guid('{04de5372-b7b7-476b-a74f-c5836a704d98}')
    @winrt_commethod(6)
    def TryRegisterForAllInboundPairingRequestsWithProtectionLevel(self, pairingKindsSupported: win32more.Windows.Devices.Enumeration.DevicePairingKinds, minProtectionLevel: win32more.Windows.Devices.Enumeration.DevicePairingProtectionLevel) -> Boolean: ...
class IDeviceInformationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Enumeration.IDeviceInformationStatics'
    _iid_ = Guid('{c17f100e-3a46-4a78-8013-769dc9b97390}')
    @winrt_commethod(6)
    def CreateFromIdAsync(self, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.DeviceInformation]: ...
    @winrt_commethod(7)
    def CreateFromIdAsyncAdditionalProperties(self, deviceId: WinRT_String, additionalProperties: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.DeviceInformation]: ...
    @winrt_commethod(8)
    def FindAllAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.DeviceInformationCollection]: ...
    @winrt_commethod(9)
    def FindAllAsyncDeviceClass(self, deviceClass: win32more.Windows.Devices.Enumeration.DeviceClass) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.DeviceInformationCollection]: ...
    @winrt_commethod(10)
    def FindAllAsyncAqsFilter(self, aqsFilter: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.DeviceInformationCollection]: ...
    @winrt_commethod(11)
    def FindAllAsyncAqsFilterAndAdditionalProperties(self, aqsFilter: WinRT_String, additionalProperties: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.DeviceInformationCollection]: ...
    @winrt_commethod(12)
    def CreateWatcher(self) -> win32more.Windows.Devices.Enumeration.DeviceWatcher: ...
    @winrt_commethod(13)
    def CreateWatcherDeviceClass(self, deviceClass: win32more.Windows.Devices.Enumeration.DeviceClass) -> win32more.Windows.Devices.Enumeration.DeviceWatcher: ...
    @winrt_commethod(14)
    def CreateWatcherAqsFilter(self, aqsFilter: WinRT_String) -> win32more.Windows.Devices.Enumeration.DeviceWatcher: ...
    @winrt_commethod(15)
    def CreateWatcherAqsFilterAndAdditionalProperties(self, aqsFilter: WinRT_String, additionalProperties: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Devices.Enumeration.DeviceWatcher: ...
class IDeviceInformationStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Enumeration.IDeviceInformationStatics2'
    _iid_ = Guid('{493b4f34-a84f-45fd-9167-15d1cb1bd1f9}')
    @winrt_commethod(6)
    def GetAqsFilterFromDeviceClass(self, deviceClass: win32more.Windows.Devices.Enumeration.DeviceClass) -> WinRT_String: ...
    @winrt_commethod(7)
    def CreateFromIdAsyncWithKindAndAdditionalProperties(self, deviceId: WinRT_String, additionalProperties: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], kind: win32more.Windows.Devices.Enumeration.DeviceInformationKind) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.DeviceInformation]: ...
    @winrt_commethod(8)
    def FindAllAsyncWithKindAqsFilterAndAdditionalProperties(self, aqsFilter: WinRT_String, additionalProperties: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], kind: win32more.Windows.Devices.Enumeration.DeviceInformationKind) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.DeviceInformationCollection]: ...
    @winrt_commethod(9)
    def CreateWatcherWithKindAqsFilterAndAdditionalProperties(self, aqsFilter: WinRT_String, additionalProperties: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], kind: win32more.Windows.Devices.Enumeration.DeviceInformationKind) -> win32more.Windows.Devices.Enumeration.DeviceWatcher: ...
class IDeviceInformationUpdate(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Enumeration.IDeviceInformationUpdate'
    _iid_ = Guid('{8f315305-d972-44b7-a37e-9e822c78213b}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Properties(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    Id = property(get_Id, None)
    Properties = property(get_Properties, None)
class IDeviceInformationUpdate2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Enumeration.IDeviceInformationUpdate2'
    _iid_ = Guid('{5d9d148c-a873-485e-baa6-aa620788e3cc}')
    @winrt_commethod(6)
    def get_Kind(self) -> win32more.Windows.Devices.Enumeration.DeviceInformationKind: ...
    Kind = property(get_Kind, None)
class IDevicePairingRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Enumeration.IDevicePairingRequestedEventArgs'
    _iid_ = Guid('{f717fc56-de6b-487f-8376-0180aca69963}')
    @winrt_commethod(6)
    def get_DeviceInformation(self) -> win32more.Windows.Devices.Enumeration.DeviceInformation: ...
    @winrt_commethod(7)
    def get_PairingKind(self) -> win32more.Windows.Devices.Enumeration.DevicePairingKinds: ...
    @winrt_commethod(8)
    def get_Pin(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def Accept(self) -> Void: ...
    @winrt_commethod(10)
    def AcceptWithPin(self, pin: WinRT_String) -> Void: ...
    @winrt_commethod(11)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    DeviceInformation = property(get_DeviceInformation, None)
    PairingKind = property(get_PairingKind, None)
    Pin = property(get_Pin, None)
class IDevicePairingRequestedEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Enumeration.IDevicePairingRequestedEventArgs2'
    _iid_ = Guid('{c83752d9-e4d3-4db0-a360-a105e437dbdc}')
    @winrt_commethod(6)
    def AcceptWithPasswordCredential(self, passwordCredential: win32more.Windows.Security.Credentials.PasswordCredential) -> Void: ...
class IDevicePairingResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Enumeration.IDevicePairingResult'
    _iid_ = Guid('{072b02bf-dd95-4025-9b37-de51adba37b7}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Devices.Enumeration.DevicePairingResultStatus: ...
    @winrt_commethod(7)
    def get_ProtectionLevelUsed(self) -> win32more.Windows.Devices.Enumeration.DevicePairingProtectionLevel: ...
    Status = property(get_Status, None)
    ProtectionLevelUsed = property(get_ProtectionLevelUsed, None)
class IDevicePairingSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Enumeration.IDevicePairingSettings'
    _iid_ = Guid('{482cb27c-83bb-420e-be51-6602b222de54}')
class IDevicePicker(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Enumeration.IDevicePicker'
    _iid_ = Guid('{84997aa2-034a-4440-8813-7d0bd479bf5a}')
    @winrt_commethod(6)
    def get_Filter(self) -> win32more.Windows.Devices.Enumeration.DevicePickerFilter: ...
    @winrt_commethod(7)
    def get_Appearance(self) -> win32more.Windows.Devices.Enumeration.DevicePickerAppearance: ...
    @winrt_commethod(8)
    def get_RequestedProperties(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(9)
    def add_DeviceSelected(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Enumeration.DevicePicker, win32more.Windows.Devices.Enumeration.DeviceSelectedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_DeviceSelected(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_DisconnectButtonClicked(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Enumeration.DevicePicker, win32more.Windows.Devices.Enumeration.DeviceDisconnectButtonClickedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_DisconnectButtonClicked(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def add_DevicePickerDismissed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Enumeration.DevicePicker, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_DevicePickerDismissed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(15)
    def Show(self, selection: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_commethod(16)
    def ShowWithPlacement(self, selection: win32more.Windows.Foundation.Rect, placement: win32more.Windows.UI.Popups.Placement) -> Void: ...
    @winrt_commethod(17)
    def PickSingleDeviceAsync(self, selection: win32more.Windows.Foundation.Rect) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.DeviceInformation]: ...
    @winrt_commethod(18)
    def PickSingleDeviceAsyncWithPlacement(self, selection: win32more.Windows.Foundation.Rect, placement: win32more.Windows.UI.Popups.Placement) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.DeviceInformation]: ...
    @winrt_commethod(19)
    def Hide(self) -> Void: ...
    @winrt_commethod(20)
    def SetDisplayStatus(self, device: win32more.Windows.Devices.Enumeration.DeviceInformation, status: WinRT_String, options: win32more.Windows.Devices.Enumeration.DevicePickerDisplayStatusOptions) -> Void: ...
    Filter = property(get_Filter, None)
    Appearance = property(get_Appearance, None)
    RequestedProperties = property(get_RequestedProperties, None)
class IDevicePickerAppearance(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Enumeration.IDevicePickerAppearance'
    _iid_ = Guid('{e69a12c6-e627-4ed8-9b6c-460af445e56d}')
    @winrt_commethod(6)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Title(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_ForegroundColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(9)
    def put_ForegroundColor(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(10)
    def get_BackgroundColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(11)
    def put_BackgroundColor(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(12)
    def get_AccentColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(13)
    def put_AccentColor(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(14)
    def get_SelectedForegroundColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(15)
    def put_SelectedForegroundColor(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(16)
    def get_SelectedBackgroundColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(17)
    def put_SelectedBackgroundColor(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(18)
    def get_SelectedAccentColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(19)
    def put_SelectedAccentColor(self, value: win32more.Windows.UI.Color) -> Void: ...
    Title = property(get_Title, put_Title)
    ForegroundColor = property(get_ForegroundColor, put_ForegroundColor)
    BackgroundColor = property(get_BackgroundColor, put_BackgroundColor)
    AccentColor = property(get_AccentColor, put_AccentColor)
    SelectedForegroundColor = property(get_SelectedForegroundColor, put_SelectedForegroundColor)
    SelectedBackgroundColor = property(get_SelectedBackgroundColor, put_SelectedBackgroundColor)
    SelectedAccentColor = property(get_SelectedAccentColor, put_SelectedAccentColor)
class IDevicePickerFilter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Enumeration.IDevicePickerFilter'
    _iid_ = Guid('{91db92a2-57cb-48f1-9b59-a59b7a1f02a2}')
    @winrt_commethod(6)
    def get_SupportedDeviceClasses(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Devices.Enumeration.DeviceClass]: ...
    @winrt_commethod(7)
    def get_SupportedDeviceSelectors(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    SupportedDeviceClasses = property(get_SupportedDeviceClasses, None)
    SupportedDeviceSelectors = property(get_SupportedDeviceSelectors, None)
class IDeviceSelectedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Enumeration.IDeviceSelectedEventArgs'
    _iid_ = Guid('{269edade-1d2f-4940-8402-4156b81d3c77}')
    @winrt_commethod(6)
    def get_SelectedDevice(self) -> win32more.Windows.Devices.Enumeration.DeviceInformation: ...
    SelectedDevice = property(get_SelectedDevice, None)
class IDeviceUnpairingResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Enumeration.IDeviceUnpairingResult'
    _iid_ = Guid('{66f44ad3-79d9-444b-92cf-a92ef72571c7}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Devices.Enumeration.DeviceUnpairingResultStatus: ...
    Status = property(get_Status, None)
class IDeviceWatcher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Enumeration.IDeviceWatcher'
    _iid_ = Guid('{c9eab97d-8f6b-4f96-a9f4-abc814e22271}')
    @winrt_commethod(6)
    def add_Added(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Enumeration.DeviceWatcher, win32more.Windows.Devices.Enumeration.DeviceInformation]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Added(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_Updated(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Enumeration.DeviceWatcher, win32more.Windows.Devices.Enumeration.DeviceInformationUpdate]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_Updated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_Removed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Enumeration.DeviceWatcher, win32more.Windows.Devices.Enumeration.DeviceInformationUpdate]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_Removed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_EnumerationCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Enumeration.DeviceWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_EnumerationCompleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_Stopped(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Enumeration.DeviceWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_Stopped(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def get_Status(self) -> win32more.Windows.Devices.Enumeration.DeviceWatcherStatus: ...
    @winrt_commethod(17)
    def Start(self) -> Void: ...
    @winrt_commethod(18)
    def Stop(self) -> Void: ...
    Status = property(get_Status, None)
class IDeviceWatcher2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Enumeration.IDeviceWatcher2'
    _iid_ = Guid('{ff08456e-ed14-49e9-9a69-8117c54ae971}')
    @winrt_commethod(6)
    def GetBackgroundTrigger(self, requestedEventKinds: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Devices.Enumeration.DeviceWatcherEventKind]) -> win32more.Windows.ApplicationModel.Background.DeviceWatcherTrigger: ...
class IDeviceWatcherEvent(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Enumeration.IDeviceWatcherEvent'
    _iid_ = Guid('{74aa9c0b-1dbd-47fd-b635-3cc556d0ff8b}')
    @winrt_commethod(6)
    def get_Kind(self) -> win32more.Windows.Devices.Enumeration.DeviceWatcherEventKind: ...
    @winrt_commethod(7)
    def get_DeviceInformation(self) -> win32more.Windows.Devices.Enumeration.DeviceInformation: ...
    @winrt_commethod(8)
    def get_DeviceInformationUpdate(self) -> win32more.Windows.Devices.Enumeration.DeviceInformationUpdate: ...
    Kind = property(get_Kind, None)
    DeviceInformation = property(get_DeviceInformation, None)
    DeviceInformationUpdate = property(get_DeviceInformationUpdate, None)
class IDeviceWatcherTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Enumeration.IDeviceWatcherTriggerDetails'
    _iid_ = Guid('{38808119-4cb7-4e57-a56d-776d07cbfef9}')
    @winrt_commethod(6)
    def get_DeviceWatcherEvents(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Enumeration.DeviceWatcherEvent]: ...
    DeviceWatcherEvents = property(get_DeviceWatcherEvents, None)
class IEnclosureLocation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Enumeration.IEnclosureLocation'
    _iid_ = Guid('{42340a27-5810-459c-aabb-c65e1f813ecf}')
    @winrt_commethod(6)
    def get_InDock(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_InLid(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_Panel(self) -> win32more.Windows.Devices.Enumeration.Panel: ...
    InDock = property(get_InDock, None)
    InLid = property(get_InLid, None)
    Panel = property(get_Panel, None)
class IEnclosureLocation2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Enumeration.IEnclosureLocation2'
    _iid_ = Guid('{2885995b-e07d-485d-8a9e-bdf29aef4f66}')
    @winrt_commethod(6)
    def get_RotationAngleInDegreesClockwise(self) -> UInt32: ...
    RotationAngleInDegreesClockwise = property(get_RotationAngleInDegreesClockwise, None)
Panel = Int32
Panel_Unknown: Panel = 0
Panel_Front: Panel = 1
Panel_Back: Panel = 2
Panel_Top: Panel = 3
Panel_Bottom: Panel = 4
Panel_Left: Panel = 5
Panel_Right: Panel = 6


make_ready(__name__)
