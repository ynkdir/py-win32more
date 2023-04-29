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
import Windows.ApplicationModel.Background
import Windows.Devices.Enumeration
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Security.Credentials
import Windows.Storage.Streams
import Windows.UI
import Windows.UI.Popups
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class DeviceAccessChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Enumeration.DeviceAccessChangedEventArgs'
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.Enumeration.IDeviceAccessChangedEventArgs) -> Windows.Devices.Enumeration.DeviceAccessStatus: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.Devices.Enumeration.IDeviceAccessChangedEventArgs2) -> WinRT_String: ...
    Status = property(get_Status, None)
    Id = property(get_Id, None)
class DeviceAccessInformation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Enumeration.DeviceAccessInformation'
    @winrt_mixinmethod
    def add_AccessChanged(self: Windows.Devices.Enumeration.IDeviceAccessInformation, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Enumeration.DeviceAccessInformation, Windows.Devices.Enumeration.DeviceAccessChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AccessChanged(self: Windows.Devices.Enumeration.IDeviceAccessInformation, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_CurrentStatus(self: Windows.Devices.Enumeration.IDeviceAccessInformation) -> Windows.Devices.Enumeration.DeviceAccessStatus: ...
    @winrt_classmethod
    def CreateFromId(cls: Windows.Devices.Enumeration.IDeviceAccessInformationStatics, deviceId: WinRT_String) -> Windows.Devices.Enumeration.DeviceAccessInformation: ...
    @winrt_classmethod
    def CreateFromDeviceClassId(cls: Windows.Devices.Enumeration.IDeviceAccessInformationStatics, deviceClassId: Guid) -> Windows.Devices.Enumeration.DeviceAccessInformation: ...
    @winrt_classmethod
    def CreateFromDeviceClass(cls: Windows.Devices.Enumeration.IDeviceAccessInformationStatics, deviceClass: Windows.Devices.Enumeration.DeviceClass) -> Windows.Devices.Enumeration.DeviceAccessInformation: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Enumeration.DeviceConnectionChangeTriggerDetails'
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Enumeration.IDeviceConnectionChangeTriggerDetails) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
class DeviceDisconnectButtonClickedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Enumeration.DeviceDisconnectButtonClickedEventArgs'
    @winrt_mixinmethod
    def get_Device(self: Windows.Devices.Enumeration.IDeviceDisconnectButtonClickedEventArgs) -> Windows.Devices.Enumeration.DeviceInformation: ...
    Device = property(get_Device, None)
class DeviceInformation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Enumeration.DeviceInformation'
    @winrt_mixinmethod
    def get_Id(self: Windows.Devices.Enumeration.IDeviceInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.Devices.Enumeration.IDeviceInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsEnabled(self: Windows.Devices.Enumeration.IDeviceInformation) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsDefault(self: Windows.Devices.Enumeration.IDeviceInformation) -> Boolean: ...
    @winrt_mixinmethod
    def get_EnclosureLocation(self: Windows.Devices.Enumeration.IDeviceInformation) -> Windows.Devices.Enumeration.EnclosureLocation: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Devices.Enumeration.IDeviceInformation) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_mixinmethod
    def Update(self: Windows.Devices.Enumeration.IDeviceInformation, updateInfo: Windows.Devices.Enumeration.DeviceInformationUpdate) -> Void: ...
    @winrt_mixinmethod
    def GetThumbnailAsync(self: Windows.Devices.Enumeration.IDeviceInformation) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.DeviceThumbnail]: ...
    @winrt_mixinmethod
    def GetGlyphThumbnailAsync(self: Windows.Devices.Enumeration.IDeviceInformation) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.DeviceThumbnail]: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.Devices.Enumeration.IDeviceInformation2) -> Windows.Devices.Enumeration.DeviceInformationKind: ...
    @winrt_mixinmethod
    def get_Pairing(self: Windows.Devices.Enumeration.IDeviceInformation2) -> Windows.Devices.Enumeration.DeviceInformationPairing: ...
    @winrt_classmethod
    def GetAqsFilterFromDeviceClass(cls: Windows.Devices.Enumeration.IDeviceInformationStatics2, deviceClass: Windows.Devices.Enumeration.DeviceClass) -> WinRT_String: ...
    @winrt_classmethod
    def CreateFromIdAsyncWithKindAndAdditionalProperties(cls: Windows.Devices.Enumeration.IDeviceInformationStatics2, deviceId: WinRT_String, additionalProperties: Windows.Foundation.Collections.IIterable[WinRT_String], kind: Windows.Devices.Enumeration.DeviceInformationKind) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.DeviceInformation]: ...
    @winrt_classmethod
    def FindAllAsyncWithKindAqsFilterAndAdditionalProperties(cls: Windows.Devices.Enumeration.IDeviceInformationStatics2, aqsFilter: WinRT_String, additionalProperties: Windows.Foundation.Collections.IIterable[WinRT_String], kind: Windows.Devices.Enumeration.DeviceInformationKind) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.DeviceInformationCollection]: ...
    @winrt_classmethod
    def CreateWatcherWithKindAqsFilterAndAdditionalProperties(cls: Windows.Devices.Enumeration.IDeviceInformationStatics2, aqsFilter: WinRT_String, additionalProperties: Windows.Foundation.Collections.IIterable[WinRT_String], kind: Windows.Devices.Enumeration.DeviceInformationKind) -> Windows.Devices.Enumeration.DeviceWatcher: ...
    @winrt_classmethod
    def CreateFromIdAsync(cls: Windows.Devices.Enumeration.IDeviceInformationStatics, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.DeviceInformation]: ...
    @winrt_classmethod
    def CreateFromIdAsyncAdditionalProperties(cls: Windows.Devices.Enumeration.IDeviceInformationStatics, deviceId: WinRT_String, additionalProperties: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.DeviceInformation]: ...
    @winrt_classmethod
    def FindAllAsync(cls: Windows.Devices.Enumeration.IDeviceInformationStatics) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.DeviceInformationCollection]: ...
    @winrt_classmethod
    def FindAllAsyncDeviceClass(cls: Windows.Devices.Enumeration.IDeviceInformationStatics, deviceClass: Windows.Devices.Enumeration.DeviceClass) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.DeviceInformationCollection]: ...
    @winrt_classmethod
    def FindAllAsyncAqsFilter(cls: Windows.Devices.Enumeration.IDeviceInformationStatics, aqsFilter: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.DeviceInformationCollection]: ...
    @winrt_classmethod
    def FindAllAsyncAqsFilterAndAdditionalProperties(cls: Windows.Devices.Enumeration.IDeviceInformationStatics, aqsFilter: WinRT_String, additionalProperties: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.DeviceInformationCollection]: ...
    @winrt_classmethod
    def CreateWatcher(cls: Windows.Devices.Enumeration.IDeviceInformationStatics) -> Windows.Devices.Enumeration.DeviceWatcher: ...
    @winrt_classmethod
    def CreateWatcherDeviceClass(cls: Windows.Devices.Enumeration.IDeviceInformationStatics, deviceClass: Windows.Devices.Enumeration.DeviceClass) -> Windows.Devices.Enumeration.DeviceWatcher: ...
    @winrt_classmethod
    def CreateWatcherAqsFilter(cls: Windows.Devices.Enumeration.IDeviceInformationStatics, aqsFilter: WinRT_String) -> Windows.Devices.Enumeration.DeviceWatcher: ...
    @winrt_classmethod
    def CreateWatcherAqsFilterAndAdditionalProperties(cls: Windows.Devices.Enumeration.IDeviceInformationStatics, aqsFilter: WinRT_String, additionalProperties: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Devices.Enumeration.DeviceWatcher: ...
    Id = property(get_Id, None)
    Name = property(get_Name, None)
    IsEnabled = property(get_IsEnabled, None)
    IsDefault = property(get_IsDefault, None)
    EnclosureLocation = property(get_EnclosureLocation, None)
    Properties = property(get_Properties, None)
    Kind = property(get_Kind, None)
    Pairing = property(get_Pairing, None)
class DeviceInformationCollection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Enumeration.DeviceInformationCollection'
    @winrt_mixinmethod
    def GetAt(self: Windows.Foundation.Collections.IVectorView[Windows.Devices.Enumeration.DeviceInformation], index: UInt32) -> Windows.Devices.Enumeration.DeviceInformation: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IVectorView[Windows.Devices.Enumeration.DeviceInformation]) -> UInt32: ...
    @winrt_mixinmethod
    def IndexOf(self: Windows.Foundation.Collections.IVectorView[Windows.Devices.Enumeration.DeviceInformation], value: Windows.Devices.Enumeration.DeviceInformation, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def GetMany(self: Windows.Foundation.Collections.IVectorView[Windows.Devices.Enumeration.DeviceInformation], startIndex: UInt32, items: POINTER(Windows.Devices.Enumeration.DeviceInformation)) -> UInt32: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.Devices.Enumeration.DeviceInformation]) -> Windows.Foundation.Collections.IIterator[Windows.Devices.Enumeration.DeviceInformation]: ...
    Size = property(get_Size, None)
class DeviceInformationCustomPairing(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Enumeration.DeviceInformationCustomPairing'
    @winrt_mixinmethod
    def PairAsync(self: Windows.Devices.Enumeration.IDeviceInformationCustomPairing, pairingKindsSupported: Windows.Devices.Enumeration.DevicePairingKinds) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.DevicePairingResult]: ...
    @winrt_mixinmethod
    def PairWithProtectionLevelAsync(self: Windows.Devices.Enumeration.IDeviceInformationCustomPairing, pairingKindsSupported: Windows.Devices.Enumeration.DevicePairingKinds, minProtectionLevel: Windows.Devices.Enumeration.DevicePairingProtectionLevel) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.DevicePairingResult]: ...
    @winrt_mixinmethod
    def PairWithProtectionLevelAndSettingsAsync(self: Windows.Devices.Enumeration.IDeviceInformationCustomPairing, pairingKindsSupported: Windows.Devices.Enumeration.DevicePairingKinds, minProtectionLevel: Windows.Devices.Enumeration.DevicePairingProtectionLevel, devicePairingSettings: Windows.Devices.Enumeration.IDevicePairingSettings) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.DevicePairingResult]: ...
    @winrt_mixinmethod
    def add_PairingRequested(self: Windows.Devices.Enumeration.IDeviceInformationCustomPairing, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Enumeration.DeviceInformationCustomPairing, Windows.Devices.Enumeration.DevicePairingRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PairingRequested(self: Windows.Devices.Enumeration.IDeviceInformationCustomPairing, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Enumeration.DeviceInformationPairing'
    @winrt_mixinmethod
    def get_IsPaired(self: Windows.Devices.Enumeration.IDeviceInformationPairing) -> Boolean: ...
    @winrt_mixinmethod
    def get_CanPair(self: Windows.Devices.Enumeration.IDeviceInformationPairing) -> Boolean: ...
    @winrt_mixinmethod
    def PairAsync(self: Windows.Devices.Enumeration.IDeviceInformationPairing) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.DevicePairingResult]: ...
    @winrt_mixinmethod
    def PairWithProtectionLevelAsync(self: Windows.Devices.Enumeration.IDeviceInformationPairing, minProtectionLevel: Windows.Devices.Enumeration.DevicePairingProtectionLevel) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.DevicePairingResult]: ...
    @winrt_mixinmethod
    def get_ProtectionLevel(self: Windows.Devices.Enumeration.IDeviceInformationPairing2) -> Windows.Devices.Enumeration.DevicePairingProtectionLevel: ...
    @winrt_mixinmethod
    def get_Custom(self: Windows.Devices.Enumeration.IDeviceInformationPairing2) -> Windows.Devices.Enumeration.DeviceInformationCustomPairing: ...
    @winrt_mixinmethod
    def PairWithProtectionLevelAndSettingsAsync(self: Windows.Devices.Enumeration.IDeviceInformationPairing2, minProtectionLevel: Windows.Devices.Enumeration.DevicePairingProtectionLevel, devicePairingSettings: Windows.Devices.Enumeration.IDevicePairingSettings) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.DevicePairingResult]: ...
    @winrt_mixinmethod
    def UnpairAsync(self: Windows.Devices.Enumeration.IDeviceInformationPairing2) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.DeviceUnpairingResult]: ...
    @winrt_classmethod
    def TryRegisterForAllInboundPairingRequestsWithProtectionLevel(cls: Windows.Devices.Enumeration.IDeviceInformationPairingStatics2, pairingKindsSupported: Windows.Devices.Enumeration.DevicePairingKinds, minProtectionLevel: Windows.Devices.Enumeration.DevicePairingProtectionLevel) -> Boolean: ...
    @winrt_classmethod
    def TryRegisterForAllInboundPairingRequests(cls: Windows.Devices.Enumeration.IDeviceInformationPairingStatics, pairingKindsSupported: Windows.Devices.Enumeration.DevicePairingKinds) -> Boolean: ...
    IsPaired = property(get_IsPaired, None)
    CanPair = property(get_CanPair, None)
    ProtectionLevel = property(get_ProtectionLevel, None)
    Custom = property(get_Custom, None)
class DeviceInformationUpdate(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Enumeration.DeviceInformationUpdate'
    @winrt_mixinmethod
    def get_Id(self: Windows.Devices.Enumeration.IDeviceInformationUpdate) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Devices.Enumeration.IDeviceInformationUpdate) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.Devices.Enumeration.IDeviceInformationUpdate2) -> Windows.Devices.Enumeration.DeviceInformationKind: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Enumeration.DevicePairingRequestedEventArgs'
    @winrt_mixinmethod
    def get_DeviceInformation(self: Windows.Devices.Enumeration.IDevicePairingRequestedEventArgs) -> Windows.Devices.Enumeration.DeviceInformation: ...
    @winrt_mixinmethod
    def get_PairingKind(self: Windows.Devices.Enumeration.IDevicePairingRequestedEventArgs) -> Windows.Devices.Enumeration.DevicePairingKinds: ...
    @winrt_mixinmethod
    def get_Pin(self: Windows.Devices.Enumeration.IDevicePairingRequestedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def Accept(self: Windows.Devices.Enumeration.IDevicePairingRequestedEventArgs) -> Void: ...
    @winrt_mixinmethod
    def AcceptWithPin(self: Windows.Devices.Enumeration.IDevicePairingRequestedEventArgs, pin: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Devices.Enumeration.IDevicePairingRequestedEventArgs) -> Windows.Foundation.Deferral: ...
    @winrt_mixinmethod
    def AcceptWithPasswordCredential(self: Windows.Devices.Enumeration.IDevicePairingRequestedEventArgs2, passwordCredential: Windows.Security.Credentials.PasswordCredential) -> Void: ...
    DeviceInformation = property(get_DeviceInformation, None)
    PairingKind = property(get_PairingKind, None)
    Pin = property(get_Pin, None)
class DevicePairingResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Enumeration.DevicePairingResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.Enumeration.IDevicePairingResult) -> Windows.Devices.Enumeration.DevicePairingResultStatus: ...
    @winrt_mixinmethod
    def get_ProtectionLevelUsed(self: Windows.Devices.Enumeration.IDevicePairingResult) -> Windows.Devices.Enumeration.DevicePairingProtectionLevel: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Enumeration.DevicePicker'
    @winrt_activatemethod
    def New(cls) -> Windows.Devices.Enumeration.DevicePicker: ...
    @winrt_mixinmethod
    def get_Filter(self: Windows.Devices.Enumeration.IDevicePicker) -> Windows.Devices.Enumeration.DevicePickerFilter: ...
    @winrt_mixinmethod
    def get_Appearance(self: Windows.Devices.Enumeration.IDevicePicker) -> Windows.Devices.Enumeration.DevicePickerAppearance: ...
    @winrt_mixinmethod
    def get_RequestedProperties(self: Windows.Devices.Enumeration.IDevicePicker) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def add_DeviceSelected(self: Windows.Devices.Enumeration.IDevicePicker, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Enumeration.DevicePicker, Windows.Devices.Enumeration.DeviceSelectedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DeviceSelected(self: Windows.Devices.Enumeration.IDevicePicker, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DisconnectButtonClicked(self: Windows.Devices.Enumeration.IDevicePicker, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Enumeration.DevicePicker, Windows.Devices.Enumeration.DeviceDisconnectButtonClickedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DisconnectButtonClicked(self: Windows.Devices.Enumeration.IDevicePicker, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DevicePickerDismissed(self: Windows.Devices.Enumeration.IDevicePicker, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Enumeration.DevicePicker, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DevicePickerDismissed(self: Windows.Devices.Enumeration.IDevicePicker, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Show(self: Windows.Devices.Enumeration.IDevicePicker, selection: Windows.Foundation.Rect) -> Void: ...
    @winrt_mixinmethod
    def ShowWithPlacement(self: Windows.Devices.Enumeration.IDevicePicker, selection: Windows.Foundation.Rect, placement: Windows.UI.Popups.Placement) -> Void: ...
    @winrt_mixinmethod
    def PickSingleDeviceAsync(self: Windows.Devices.Enumeration.IDevicePicker, selection: Windows.Foundation.Rect) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.DeviceInformation]: ...
    @winrt_mixinmethod
    def PickSingleDeviceAsyncWithPlacement(self: Windows.Devices.Enumeration.IDevicePicker, selection: Windows.Foundation.Rect, placement: Windows.UI.Popups.Placement) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.DeviceInformation]: ...
    @winrt_mixinmethod
    def Hide(self: Windows.Devices.Enumeration.IDevicePicker) -> Void: ...
    @winrt_mixinmethod
    def SetDisplayStatus(self: Windows.Devices.Enumeration.IDevicePicker, device: Windows.Devices.Enumeration.DeviceInformation, status: WinRT_String, options: Windows.Devices.Enumeration.DevicePickerDisplayStatusOptions) -> Void: ...
    Filter = property(get_Filter, None)
    Appearance = property(get_Appearance, None)
    RequestedProperties = property(get_RequestedProperties, None)
class DevicePickerAppearance(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Enumeration.DevicePickerAppearance'
    @winrt_mixinmethod
    def get_Title(self: Windows.Devices.Enumeration.IDevicePickerAppearance) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Title(self: Windows.Devices.Enumeration.IDevicePickerAppearance, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ForegroundColor(self: Windows.Devices.Enumeration.IDevicePickerAppearance) -> Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_ForegroundColor(self: Windows.Devices.Enumeration.IDevicePickerAppearance, value: Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_BackgroundColor(self: Windows.Devices.Enumeration.IDevicePickerAppearance) -> Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_BackgroundColor(self: Windows.Devices.Enumeration.IDevicePickerAppearance, value: Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_AccentColor(self: Windows.Devices.Enumeration.IDevicePickerAppearance) -> Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_AccentColor(self: Windows.Devices.Enumeration.IDevicePickerAppearance, value: Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_SelectedForegroundColor(self: Windows.Devices.Enumeration.IDevicePickerAppearance) -> Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_SelectedForegroundColor(self: Windows.Devices.Enumeration.IDevicePickerAppearance, value: Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_SelectedBackgroundColor(self: Windows.Devices.Enumeration.IDevicePickerAppearance) -> Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_SelectedBackgroundColor(self: Windows.Devices.Enumeration.IDevicePickerAppearance, value: Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_SelectedAccentColor(self: Windows.Devices.Enumeration.IDevicePickerAppearance) -> Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_SelectedAccentColor(self: Windows.Devices.Enumeration.IDevicePickerAppearance, value: Windows.UI.Color) -> Void: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Enumeration.DevicePickerFilter'
    @winrt_mixinmethod
    def get_SupportedDeviceClasses(self: Windows.Devices.Enumeration.IDevicePickerFilter) -> Windows.Foundation.Collections.IVector[Windows.Devices.Enumeration.DeviceClass]: ...
    @winrt_mixinmethod
    def get_SupportedDeviceSelectors(self: Windows.Devices.Enumeration.IDevicePickerFilter) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    SupportedDeviceClasses = property(get_SupportedDeviceClasses, None)
    SupportedDeviceSelectors = property(get_SupportedDeviceSelectors, None)
class DeviceSelectedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Enumeration.DeviceSelectedEventArgs'
    @winrt_mixinmethod
    def get_SelectedDevice(self: Windows.Devices.Enumeration.IDeviceSelectedEventArgs) -> Windows.Devices.Enumeration.DeviceInformation: ...
    SelectedDevice = property(get_SelectedDevice, None)
class DeviceThumbnail(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Enumeration.DeviceThumbnail'
    @winrt_mixinmethod
    def get_Size(self: Windows.Storage.Streams.IRandomAccessStream) -> UInt64: ...
    @winrt_mixinmethod
    def put_Size(self: Windows.Storage.Streams.IRandomAccessStream, value: UInt64) -> Void: ...
    @winrt_mixinmethod
    def GetInputStreamAt(self: Windows.Storage.Streams.IRandomAccessStream, position: UInt64) -> Windows.Storage.Streams.IInputStream: ...
    @winrt_mixinmethod
    def GetOutputStreamAt(self: Windows.Storage.Streams.IRandomAccessStream, position: UInt64) -> Windows.Storage.Streams.IOutputStream: ...
    @winrt_mixinmethod
    def get_Position(self: Windows.Storage.Streams.IRandomAccessStream) -> UInt64: ...
    @winrt_mixinmethod
    def Seek(self: Windows.Storage.Streams.IRandomAccessStream, position: UInt64) -> Void: ...
    @winrt_mixinmethod
    def CloneStream(self: Windows.Storage.Streams.IRandomAccessStream) -> Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_mixinmethod
    def get_CanRead(self: Windows.Storage.Streams.IRandomAccessStream) -> Boolean: ...
    @winrt_mixinmethod
    def get_CanWrite(self: Windows.Storage.Streams.IRandomAccessStream) -> Boolean: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def ReadAsync(self: Windows.Storage.Streams.IInputStream, buffer: Windows.Storage.Streams.IBuffer, count: UInt32, options: Windows.Storage.Streams.InputStreamOptions) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Storage.Streams.IBuffer, UInt32]: ...
    @winrt_mixinmethod
    def WriteAsync(self: Windows.Storage.Streams.IOutputStream, buffer: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperationWithProgress[UInt32, UInt32]: ...
    @winrt_mixinmethod
    def FlushAsync(self: Windows.Storage.Streams.IOutputStream) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def get_ContentType(self: Windows.Storage.Streams.IContentTypeProvider) -> WinRT_String: ...
    Size = property(get_Size, put_Size)
    Position = property(get_Position, None)
    CanRead = property(get_CanRead, None)
    CanWrite = property(get_CanWrite, None)
    ContentType = property(get_ContentType, None)
class DeviceUnpairingResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Enumeration.DeviceUnpairingResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.Enumeration.IDeviceUnpairingResult) -> Windows.Devices.Enumeration.DeviceUnpairingResultStatus: ...
    Status = property(get_Status, None)
DeviceUnpairingResultStatus = Int32
DeviceUnpairingResultStatus_Unpaired: DeviceUnpairingResultStatus = 0
DeviceUnpairingResultStatus_AlreadyUnpaired: DeviceUnpairingResultStatus = 1
DeviceUnpairingResultStatus_OperationAlreadyInProgress: DeviceUnpairingResultStatus = 2
DeviceUnpairingResultStatus_AccessDenied: DeviceUnpairingResultStatus = 3
DeviceUnpairingResultStatus_Failed: DeviceUnpairingResultStatus = 4
class DeviceWatcher(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Enumeration.DeviceWatcher'
    @winrt_mixinmethod
    def add_Added(self: Windows.Devices.Enumeration.IDeviceWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Enumeration.DeviceWatcher, Windows.Devices.Enumeration.DeviceInformation]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Added(self: Windows.Devices.Enumeration.IDeviceWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Updated(self: Windows.Devices.Enumeration.IDeviceWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Enumeration.DeviceWatcher, Windows.Devices.Enumeration.DeviceInformationUpdate]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Updated(self: Windows.Devices.Enumeration.IDeviceWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Removed(self: Windows.Devices.Enumeration.IDeviceWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Enumeration.DeviceWatcher, Windows.Devices.Enumeration.DeviceInformationUpdate]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Removed(self: Windows.Devices.Enumeration.IDeviceWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_EnumerationCompleted(self: Windows.Devices.Enumeration.IDeviceWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Enumeration.DeviceWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_EnumerationCompleted(self: Windows.Devices.Enumeration.IDeviceWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Stopped(self: Windows.Devices.Enumeration.IDeviceWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Enumeration.DeviceWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Stopped(self: Windows.Devices.Enumeration.IDeviceWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.Enumeration.IDeviceWatcher) -> Windows.Devices.Enumeration.DeviceWatcherStatus: ...
    @winrt_mixinmethod
    def Start(self: Windows.Devices.Enumeration.IDeviceWatcher) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: Windows.Devices.Enumeration.IDeviceWatcher) -> Void: ...
    @winrt_mixinmethod
    def GetBackgroundTrigger(self: Windows.Devices.Enumeration.IDeviceWatcher2, requestedEventKinds: Windows.Foundation.Collections.IIterable[Windows.Devices.Enumeration.DeviceWatcherEventKind]) -> Windows.ApplicationModel.Background.DeviceWatcherTrigger: ...
    Status = property(get_Status, None)
class DeviceWatcherEvent(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Enumeration.DeviceWatcherEvent'
    @winrt_mixinmethod
    def get_Kind(self: Windows.Devices.Enumeration.IDeviceWatcherEvent) -> Windows.Devices.Enumeration.DeviceWatcherEventKind: ...
    @winrt_mixinmethod
    def get_DeviceInformation(self: Windows.Devices.Enumeration.IDeviceWatcherEvent) -> Windows.Devices.Enumeration.DeviceInformation: ...
    @winrt_mixinmethod
    def get_DeviceInformationUpdate(self: Windows.Devices.Enumeration.IDeviceWatcherEvent) -> Windows.Devices.Enumeration.DeviceInformationUpdate: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Enumeration.DeviceWatcherTriggerDetails'
    @winrt_mixinmethod
    def get_DeviceWatcherEvents(self: Windows.Devices.Enumeration.IDeviceWatcherTriggerDetails) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Enumeration.DeviceWatcherEvent]: ...
    DeviceWatcherEvents = property(get_DeviceWatcherEvents, None)
class EnclosureLocation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Enumeration.EnclosureLocation'
    @winrt_mixinmethod
    def get_InDock(self: Windows.Devices.Enumeration.IEnclosureLocation) -> Boolean: ...
    @winrt_mixinmethod
    def get_InLid(self: Windows.Devices.Enumeration.IEnclosureLocation) -> Boolean: ...
    @winrt_mixinmethod
    def get_Panel(self: Windows.Devices.Enumeration.IEnclosureLocation) -> Windows.Devices.Enumeration.Panel: ...
    @winrt_mixinmethod
    def get_RotationAngleInDegreesClockwise(self: Windows.Devices.Enumeration.IEnclosureLocation2) -> UInt32: ...
    InDock = property(get_InDock, None)
    InLid = property(get_InLid, None)
    Panel = property(get_Panel, None)
    RotationAngleInDegreesClockwise = property(get_RotationAngleInDegreesClockwise, None)
class IDeviceAccessChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('deda0bcc-4f9d-4f58-9d-ba-a9-bc-80-04-08-d5')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Devices.Enumeration.DeviceAccessStatus: ...
    Status = property(get_Status, None)
class IDeviceAccessChangedEventArgs2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('82523262-934b-4b30-a1-78-ad-c3-9f-2f-2b-e3')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    Id = property(get_Id, None)
class IDeviceAccessInformation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('0baa9a73-6de5-4915-8d-dd-9a-05-54-a6-f5-45')
    @winrt_commethod(6)
    def add_AccessChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Enumeration.DeviceAccessInformation, Windows.Devices.Enumeration.DeviceAccessChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_AccessChanged(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def get_CurrentStatus(self) -> Windows.Devices.Enumeration.DeviceAccessStatus: ...
    CurrentStatus = property(get_CurrentStatus, None)
class IDeviceAccessInformationStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('574bd3d3-5f30-45cd-8a-94-72-4f-e5-97-30-84')
    @winrt_commethod(6)
    def CreateFromId(self, deviceId: WinRT_String) -> Windows.Devices.Enumeration.DeviceAccessInformation: ...
    @winrt_commethod(7)
    def CreateFromDeviceClassId(self, deviceClassId: Guid) -> Windows.Devices.Enumeration.DeviceAccessInformation: ...
    @winrt_commethod(8)
    def CreateFromDeviceClass(self, deviceClass: Windows.Devices.Enumeration.DeviceClass) -> Windows.Devices.Enumeration.DeviceAccessInformation: ...
class IDeviceConnectionChangeTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('b8578c0c-bbc1-484b-bf-fa-7b-31-dc-c2-00-b2')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
class IDeviceDisconnectButtonClickedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('8e44b56d-f902-4a00-b5-36-f3-79-92-e6-a2-a7')
    @winrt_commethod(6)
    def get_Device(self) -> Windows.Devices.Enumeration.DeviceInformation: ...
    Device = property(get_Device, None)
class IDeviceInformation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('aba0fb95-4398-489d-8e-44-e6-13-09-27-01-1f')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsDefault(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_EnclosureLocation(self) -> Windows.Devices.Enumeration.EnclosureLocation: ...
    @winrt_commethod(11)
    def get_Properties(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_commethod(12)
    def Update(self, updateInfo: Windows.Devices.Enumeration.DeviceInformationUpdate) -> Void: ...
    @winrt_commethod(13)
    def GetThumbnailAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.DeviceThumbnail]: ...
    @winrt_commethod(14)
    def GetGlyphThumbnailAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.DeviceThumbnail]: ...
    Id = property(get_Id, None)
    Name = property(get_Name, None)
    IsEnabled = property(get_IsEnabled, None)
    IsDefault = property(get_IsDefault, None)
    EnclosureLocation = property(get_EnclosureLocation, None)
    Properties = property(get_Properties, None)
class IDeviceInformation2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('f156a638-7997-48d9-a1-0c-26-9d-46-53-3f-48')
    @winrt_commethod(6)
    def get_Kind(self) -> Windows.Devices.Enumeration.DeviceInformationKind: ...
    @winrt_commethod(7)
    def get_Pairing(self) -> Windows.Devices.Enumeration.DeviceInformationPairing: ...
    Kind = property(get_Kind, None)
    Pairing = property(get_Pairing, None)
class IDeviceInformationCustomPairing(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('85138c02-4ee6-4914-83-70-10-7a-39-14-4c-0e')
    @winrt_commethod(6)
    def PairAsync(self, pairingKindsSupported: Windows.Devices.Enumeration.DevicePairingKinds) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.DevicePairingResult]: ...
    @winrt_commethod(7)
    def PairWithProtectionLevelAsync(self, pairingKindsSupported: Windows.Devices.Enumeration.DevicePairingKinds, minProtectionLevel: Windows.Devices.Enumeration.DevicePairingProtectionLevel) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.DevicePairingResult]: ...
    @winrt_commethod(8)
    def PairWithProtectionLevelAndSettingsAsync(self, pairingKindsSupported: Windows.Devices.Enumeration.DevicePairingKinds, minProtectionLevel: Windows.Devices.Enumeration.DevicePairingProtectionLevel, devicePairingSettings: Windows.Devices.Enumeration.IDevicePairingSettings) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.DevicePairingResult]: ...
    @winrt_commethod(9)
    def add_PairingRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Enumeration.DeviceInformationCustomPairing, Windows.Devices.Enumeration.DevicePairingRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_PairingRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IDeviceInformationPairing(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('2c4769f5-f684-40d5-84-69-e8-db-aa-b7-04-85')
    @winrt_commethod(6)
    def get_IsPaired(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_CanPair(self) -> Boolean: ...
    @winrt_commethod(8)
    def PairAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.DevicePairingResult]: ...
    @winrt_commethod(9)
    def PairWithProtectionLevelAsync(self, minProtectionLevel: Windows.Devices.Enumeration.DevicePairingProtectionLevel) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.DevicePairingResult]: ...
    IsPaired = property(get_IsPaired, None)
    CanPair = property(get_CanPair, None)
class IDeviceInformationPairing2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('f68612fd-0aee-4328-85-cc-1c-74-2b-b1-79-0d')
    @winrt_commethod(6)
    def get_ProtectionLevel(self) -> Windows.Devices.Enumeration.DevicePairingProtectionLevel: ...
    @winrt_commethod(7)
    def get_Custom(self) -> Windows.Devices.Enumeration.DeviceInformationCustomPairing: ...
    @winrt_commethod(8)
    def PairWithProtectionLevelAndSettingsAsync(self, minProtectionLevel: Windows.Devices.Enumeration.DevicePairingProtectionLevel, devicePairingSettings: Windows.Devices.Enumeration.IDevicePairingSettings) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.DevicePairingResult]: ...
    @winrt_commethod(9)
    def UnpairAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.DeviceUnpairingResult]: ...
    ProtectionLevel = property(get_ProtectionLevel, None)
    Custom = property(get_Custom, None)
class IDeviceInformationPairingStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('e915c408-36d4-49a1-bf-13-51-41-73-79-9b-6b')
    @winrt_commethod(6)
    def TryRegisterForAllInboundPairingRequests(self, pairingKindsSupported: Windows.Devices.Enumeration.DevicePairingKinds) -> Boolean: ...
class IDeviceInformationPairingStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('04de5372-b7b7-476b-a7-4f-c5-83-6a-70-4d-98')
    @winrt_commethod(6)
    def TryRegisterForAllInboundPairingRequestsWithProtectionLevel(self, pairingKindsSupported: Windows.Devices.Enumeration.DevicePairingKinds, minProtectionLevel: Windows.Devices.Enumeration.DevicePairingProtectionLevel) -> Boolean: ...
class IDeviceInformationStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('c17f100e-3a46-4a78-80-13-76-9d-c9-b9-73-90')
    @winrt_commethod(6)
    def CreateFromIdAsync(self, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.DeviceInformation]: ...
    @winrt_commethod(7)
    def CreateFromIdAsyncAdditionalProperties(self, deviceId: WinRT_String, additionalProperties: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.DeviceInformation]: ...
    @winrt_commethod(8)
    def FindAllAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.DeviceInformationCollection]: ...
    @winrt_commethod(9)
    def FindAllAsyncDeviceClass(self, deviceClass: Windows.Devices.Enumeration.DeviceClass) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.DeviceInformationCollection]: ...
    @winrt_commethod(10)
    def FindAllAsyncAqsFilter(self, aqsFilter: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.DeviceInformationCollection]: ...
    @winrt_commethod(11)
    def FindAllAsyncAqsFilterAndAdditionalProperties(self, aqsFilter: WinRT_String, additionalProperties: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.DeviceInformationCollection]: ...
    @winrt_commethod(12)
    def CreateWatcher(self) -> Windows.Devices.Enumeration.DeviceWatcher: ...
    @winrt_commethod(13)
    def CreateWatcherDeviceClass(self, deviceClass: Windows.Devices.Enumeration.DeviceClass) -> Windows.Devices.Enumeration.DeviceWatcher: ...
    @winrt_commethod(14)
    def CreateWatcherAqsFilter(self, aqsFilter: WinRT_String) -> Windows.Devices.Enumeration.DeviceWatcher: ...
    @winrt_commethod(15)
    def CreateWatcherAqsFilterAndAdditionalProperties(self, aqsFilter: WinRT_String, additionalProperties: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Devices.Enumeration.DeviceWatcher: ...
class IDeviceInformationStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('493b4f34-a84f-45fd-91-67-15-d1-cb-1b-d1-f9')
    @winrt_commethod(6)
    def GetAqsFilterFromDeviceClass(self, deviceClass: Windows.Devices.Enumeration.DeviceClass) -> WinRT_String: ...
    @winrt_commethod(7)
    def CreateFromIdAsyncWithKindAndAdditionalProperties(self, deviceId: WinRT_String, additionalProperties: Windows.Foundation.Collections.IIterable[WinRT_String], kind: Windows.Devices.Enumeration.DeviceInformationKind) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.DeviceInformation]: ...
    @winrt_commethod(8)
    def FindAllAsyncWithKindAqsFilterAndAdditionalProperties(self, aqsFilter: WinRT_String, additionalProperties: Windows.Foundation.Collections.IIterable[WinRT_String], kind: Windows.Devices.Enumeration.DeviceInformationKind) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.DeviceInformationCollection]: ...
    @winrt_commethod(9)
    def CreateWatcherWithKindAqsFilterAndAdditionalProperties(self, aqsFilter: WinRT_String, additionalProperties: Windows.Foundation.Collections.IIterable[WinRT_String], kind: Windows.Devices.Enumeration.DeviceInformationKind) -> Windows.Devices.Enumeration.DeviceWatcher: ...
class IDeviceInformationUpdate(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('8f315305-d972-44b7-a3-7e-9e-82-2c-78-21-3b')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Properties(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    Id = property(get_Id, None)
    Properties = property(get_Properties, None)
class IDeviceInformationUpdate2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('5d9d148c-a873-485e-ba-a6-aa-62-07-88-e3-cc')
    @winrt_commethod(6)
    def get_Kind(self) -> Windows.Devices.Enumeration.DeviceInformationKind: ...
    Kind = property(get_Kind, None)
class IDevicePairingRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('f717fc56-de6b-487f-83-76-01-80-ac-a6-99-63')
    @winrt_commethod(6)
    def get_DeviceInformation(self) -> Windows.Devices.Enumeration.DeviceInformation: ...
    @winrt_commethod(7)
    def get_PairingKind(self) -> Windows.Devices.Enumeration.DevicePairingKinds: ...
    @winrt_commethod(8)
    def get_Pin(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def Accept(self) -> Void: ...
    @winrt_commethod(10)
    def AcceptWithPin(self, pin: WinRT_String) -> Void: ...
    @winrt_commethod(11)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    DeviceInformation = property(get_DeviceInformation, None)
    PairingKind = property(get_PairingKind, None)
    Pin = property(get_Pin, None)
class IDevicePairingRequestedEventArgs2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('c83752d9-e4d3-4db0-a3-60-a1-05-e4-37-db-dc')
    @winrt_commethod(6)
    def AcceptWithPasswordCredential(self, passwordCredential: Windows.Security.Credentials.PasswordCredential) -> Void: ...
class IDevicePairingResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('072b02bf-dd95-4025-9b-37-de-51-ad-ba-37-b7')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Devices.Enumeration.DevicePairingResultStatus: ...
    @winrt_commethod(7)
    def get_ProtectionLevelUsed(self) -> Windows.Devices.Enumeration.DevicePairingProtectionLevel: ...
    Status = property(get_Status, None)
    ProtectionLevelUsed = property(get_ProtectionLevelUsed, None)
class IDevicePairingSettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('482cb27c-83bb-420e-be-51-66-02-b2-22-de-54')
class IDevicePicker(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('84997aa2-034a-4440-88-13-7d-0b-d4-79-bf-5a')
    @winrt_commethod(6)
    def get_Filter(self) -> Windows.Devices.Enumeration.DevicePickerFilter: ...
    @winrt_commethod(7)
    def get_Appearance(self) -> Windows.Devices.Enumeration.DevicePickerAppearance: ...
    @winrt_commethod(8)
    def get_RequestedProperties(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(9)
    def add_DeviceSelected(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Enumeration.DevicePicker, Windows.Devices.Enumeration.DeviceSelectedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_DeviceSelected(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_DisconnectButtonClicked(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Enumeration.DevicePicker, Windows.Devices.Enumeration.DeviceDisconnectButtonClickedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_DisconnectButtonClicked(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def add_DevicePickerDismissed(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Enumeration.DevicePicker, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_DevicePickerDismissed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(15)
    def Show(self, selection: Windows.Foundation.Rect) -> Void: ...
    @winrt_commethod(16)
    def ShowWithPlacement(self, selection: Windows.Foundation.Rect, placement: Windows.UI.Popups.Placement) -> Void: ...
    @winrt_commethod(17)
    def PickSingleDeviceAsync(self, selection: Windows.Foundation.Rect) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.DeviceInformation]: ...
    @winrt_commethod(18)
    def PickSingleDeviceAsyncWithPlacement(self, selection: Windows.Foundation.Rect, placement: Windows.UI.Popups.Placement) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.DeviceInformation]: ...
    @winrt_commethod(19)
    def Hide(self) -> Void: ...
    @winrt_commethod(20)
    def SetDisplayStatus(self, device: Windows.Devices.Enumeration.DeviceInformation, status: WinRT_String, options: Windows.Devices.Enumeration.DevicePickerDisplayStatusOptions) -> Void: ...
    Filter = property(get_Filter, None)
    Appearance = property(get_Appearance, None)
    RequestedProperties = property(get_RequestedProperties, None)
class IDevicePickerAppearance(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('e69a12c6-e627-4ed8-9b-6c-46-0a-f4-45-e5-6d')
    @winrt_commethod(6)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Title(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_ForegroundColor(self) -> Windows.UI.Color: ...
    @winrt_commethod(9)
    def put_ForegroundColor(self, value: Windows.UI.Color) -> Void: ...
    @winrt_commethod(10)
    def get_BackgroundColor(self) -> Windows.UI.Color: ...
    @winrt_commethod(11)
    def put_BackgroundColor(self, value: Windows.UI.Color) -> Void: ...
    @winrt_commethod(12)
    def get_AccentColor(self) -> Windows.UI.Color: ...
    @winrt_commethod(13)
    def put_AccentColor(self, value: Windows.UI.Color) -> Void: ...
    @winrt_commethod(14)
    def get_SelectedForegroundColor(self) -> Windows.UI.Color: ...
    @winrt_commethod(15)
    def put_SelectedForegroundColor(self, value: Windows.UI.Color) -> Void: ...
    @winrt_commethod(16)
    def get_SelectedBackgroundColor(self) -> Windows.UI.Color: ...
    @winrt_commethod(17)
    def put_SelectedBackgroundColor(self, value: Windows.UI.Color) -> Void: ...
    @winrt_commethod(18)
    def get_SelectedAccentColor(self) -> Windows.UI.Color: ...
    @winrt_commethod(19)
    def put_SelectedAccentColor(self, value: Windows.UI.Color) -> Void: ...
    Title = property(get_Title, put_Title)
    ForegroundColor = property(get_ForegroundColor, put_ForegroundColor)
    BackgroundColor = property(get_BackgroundColor, put_BackgroundColor)
    AccentColor = property(get_AccentColor, put_AccentColor)
    SelectedForegroundColor = property(get_SelectedForegroundColor, put_SelectedForegroundColor)
    SelectedBackgroundColor = property(get_SelectedBackgroundColor, put_SelectedBackgroundColor)
    SelectedAccentColor = property(get_SelectedAccentColor, put_SelectedAccentColor)
class IDevicePickerFilter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('91db92a2-57cb-48f1-9b-59-a5-9b-7a-1f-02-a2')
    @winrt_commethod(6)
    def get_SupportedDeviceClasses(self) -> Windows.Foundation.Collections.IVector[Windows.Devices.Enumeration.DeviceClass]: ...
    @winrt_commethod(7)
    def get_SupportedDeviceSelectors(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    SupportedDeviceClasses = property(get_SupportedDeviceClasses, None)
    SupportedDeviceSelectors = property(get_SupportedDeviceSelectors, None)
class IDeviceSelectedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('269edade-1d2f-4940-84-02-41-56-b8-1d-3c-77')
    @winrt_commethod(6)
    def get_SelectedDevice(self) -> Windows.Devices.Enumeration.DeviceInformation: ...
    SelectedDevice = property(get_SelectedDevice, None)
class IDeviceUnpairingResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('66f44ad3-79d9-444b-92-cf-a9-2e-f7-25-71-c7')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Devices.Enumeration.DeviceUnpairingResultStatus: ...
    Status = property(get_Status, None)
class IDeviceWatcher(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('c9eab97d-8f6b-4f96-a9-f4-ab-c8-14-e2-22-71')
    @winrt_commethod(6)
    def add_Added(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Enumeration.DeviceWatcher, Windows.Devices.Enumeration.DeviceInformation]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Added(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_Updated(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Enumeration.DeviceWatcher, Windows.Devices.Enumeration.DeviceInformationUpdate]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_Updated(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_Removed(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Enumeration.DeviceWatcher, Windows.Devices.Enumeration.DeviceInformationUpdate]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_Removed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_EnumerationCompleted(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Enumeration.DeviceWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_EnumerationCompleted(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_Stopped(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Enumeration.DeviceWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_Stopped(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def get_Status(self) -> Windows.Devices.Enumeration.DeviceWatcherStatus: ...
    @winrt_commethod(17)
    def Start(self) -> Void: ...
    @winrt_commethod(18)
    def Stop(self) -> Void: ...
    Status = property(get_Status, None)
class IDeviceWatcher2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('ff08456e-ed14-49e9-9a-69-81-17-c5-4a-e9-71')
    @winrt_commethod(6)
    def GetBackgroundTrigger(self, requestedEventKinds: Windows.Foundation.Collections.IIterable[Windows.Devices.Enumeration.DeviceWatcherEventKind]) -> Windows.ApplicationModel.Background.DeviceWatcherTrigger: ...
class IDeviceWatcherEvent(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('74aa9c0b-1dbd-47fd-b6-35-3c-c5-56-d0-ff-8b')
    @winrt_commethod(6)
    def get_Kind(self) -> Windows.Devices.Enumeration.DeviceWatcherEventKind: ...
    @winrt_commethod(7)
    def get_DeviceInformation(self) -> Windows.Devices.Enumeration.DeviceInformation: ...
    @winrt_commethod(8)
    def get_DeviceInformationUpdate(self) -> Windows.Devices.Enumeration.DeviceInformationUpdate: ...
    Kind = property(get_Kind, None)
    DeviceInformation = property(get_DeviceInformation, None)
    DeviceInformationUpdate = property(get_DeviceInformationUpdate, None)
class IDeviceWatcherTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('38808119-4cb7-4e57-a5-6d-77-6d-07-cb-fe-f9')
    @winrt_commethod(6)
    def get_DeviceWatcherEvents(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Enumeration.DeviceWatcherEvent]: ...
    DeviceWatcherEvents = property(get_DeviceWatcherEvents, None)
class IEnclosureLocation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('42340a27-5810-459c-aa-bb-c6-5e-1f-81-3e-cf')
    @winrt_commethod(6)
    def get_InDock(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_InLid(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_Panel(self) -> Windows.Devices.Enumeration.Panel: ...
    InDock = property(get_InDock, None)
    InLid = property(get_InLid, None)
    Panel = property(get_Panel, None)
class IEnclosureLocation2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('2885995b-e07d-485d-8a-9e-bd-f2-9a-ef-4f-66')
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
make_head(_module, 'DeviceAccessChangedEventArgs')
make_head(_module, 'DeviceAccessInformation')
make_head(_module, 'DeviceConnectionChangeTriggerDetails')
make_head(_module, 'DeviceDisconnectButtonClickedEventArgs')
make_head(_module, 'DeviceInformation')
make_head(_module, 'DeviceInformationCollection')
make_head(_module, 'DeviceInformationCustomPairing')
make_head(_module, 'DeviceInformationPairing')
make_head(_module, 'DeviceInformationUpdate')
make_head(_module, 'DevicePairingRequestedEventArgs')
make_head(_module, 'DevicePairingResult')
make_head(_module, 'DevicePicker')
make_head(_module, 'DevicePickerAppearance')
make_head(_module, 'DevicePickerFilter')
make_head(_module, 'DeviceSelectedEventArgs')
make_head(_module, 'DeviceThumbnail')
make_head(_module, 'DeviceUnpairingResult')
make_head(_module, 'DeviceWatcher')
make_head(_module, 'DeviceWatcherEvent')
make_head(_module, 'DeviceWatcherTriggerDetails')
make_head(_module, 'EnclosureLocation')
make_head(_module, 'IDeviceAccessChangedEventArgs')
make_head(_module, 'IDeviceAccessChangedEventArgs2')
make_head(_module, 'IDeviceAccessInformation')
make_head(_module, 'IDeviceAccessInformationStatics')
make_head(_module, 'IDeviceConnectionChangeTriggerDetails')
make_head(_module, 'IDeviceDisconnectButtonClickedEventArgs')
make_head(_module, 'IDeviceInformation')
make_head(_module, 'IDeviceInformation2')
make_head(_module, 'IDeviceInformationCustomPairing')
make_head(_module, 'IDeviceInformationPairing')
make_head(_module, 'IDeviceInformationPairing2')
make_head(_module, 'IDeviceInformationPairingStatics')
make_head(_module, 'IDeviceInformationPairingStatics2')
make_head(_module, 'IDeviceInformationStatics')
make_head(_module, 'IDeviceInformationStatics2')
make_head(_module, 'IDeviceInformationUpdate')
make_head(_module, 'IDeviceInformationUpdate2')
make_head(_module, 'IDevicePairingRequestedEventArgs')
make_head(_module, 'IDevicePairingRequestedEventArgs2')
make_head(_module, 'IDevicePairingResult')
make_head(_module, 'IDevicePairingSettings')
make_head(_module, 'IDevicePicker')
make_head(_module, 'IDevicePickerAppearance')
make_head(_module, 'IDevicePickerFilter')
make_head(_module, 'IDeviceSelectedEventArgs')
make_head(_module, 'IDeviceUnpairingResult')
make_head(_module, 'IDeviceWatcher')
make_head(_module, 'IDeviceWatcher2')
make_head(_module, 'IDeviceWatcherEvent')
make_head(_module, 'IDeviceWatcherTriggerDetails')
make_head(_module, 'IEnclosureLocation')
make_head(_module, 'IEnclosureLocation2')
