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
import Windows.Devices.Enumeration
import Windows.Devices.WiFiDirect
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Networking
import Windows.Security.Credentials
import Windows.Storage.Streams
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IWiFiDirectAdvertisement(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('ab511a2d-2a06-49a1-a5-84-61-43-5c-79-05-a6')
    @winrt_commethod(6)
    def get_InformationElements(self) -> Windows.Foundation.Collections.IVector[Windows.Devices.WiFiDirect.WiFiDirectInformationElement]: ...
    @winrt_commethod(7)
    def put_InformationElements(self, value: Windows.Foundation.Collections.IVector[Windows.Devices.WiFiDirect.WiFiDirectInformationElement]) -> Void: ...
    @winrt_commethod(8)
    def get_ListenStateDiscoverability(self) -> Windows.Devices.WiFiDirect.WiFiDirectAdvertisementListenStateDiscoverability: ...
    @winrt_commethod(9)
    def put_ListenStateDiscoverability(self, value: Windows.Devices.WiFiDirect.WiFiDirectAdvertisementListenStateDiscoverability) -> Void: ...
    @winrt_commethod(10)
    def get_IsAutonomousGroupOwnerEnabled(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_IsAutonomousGroupOwnerEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_LegacySettings(self) -> Windows.Devices.WiFiDirect.WiFiDirectLegacySettings: ...
    InformationElements = property(get_InformationElements, put_InformationElements)
    ListenStateDiscoverability = property(get_ListenStateDiscoverability, put_ListenStateDiscoverability)
    IsAutonomousGroupOwnerEnabled = property(get_IsAutonomousGroupOwnerEnabled, put_IsAutonomousGroupOwnerEnabled)
    LegacySettings = property(get_LegacySettings, None)
class IWiFiDirectAdvertisement2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('b759aa46-d816-491b-91-7a-b4-0d-7d-c4-03-a2')
    @winrt_commethod(6)
    def get_SupportedConfigurationMethods(self) -> Windows.Foundation.Collections.IVector[Windows.Devices.WiFiDirect.WiFiDirectConfigurationMethod]: ...
    SupportedConfigurationMethods = property(get_SupportedConfigurationMethods, None)
class IWiFiDirectAdvertisementPublisher(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('b35a2d1a-9b1f-45d9-92-5a-69-4d-66-df-68-ef')
    @winrt_commethod(6)
    def get_Advertisement(self) -> Windows.Devices.WiFiDirect.WiFiDirectAdvertisement: ...
    @winrt_commethod(7)
    def get_Status(self) -> Windows.Devices.WiFiDirect.WiFiDirectAdvertisementPublisherStatus: ...
    @winrt_commethod(8)
    def add_StatusChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.WiFiDirect.WiFiDirectAdvertisementPublisher, Windows.Devices.WiFiDirect.WiFiDirectAdvertisementPublisherStatusChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_StatusChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def Start(self) -> Void: ...
    @winrt_commethod(11)
    def Stop(self) -> Void: ...
    Advertisement = property(get_Advertisement, None)
    Status = property(get_Status, None)
class IWiFiDirectAdvertisementPublisherStatusChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('aafde53c-5481-46e6-90-dd-32-11-65-18-f1-92')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Devices.WiFiDirect.WiFiDirectAdvertisementPublisherStatus: ...
    @winrt_commethod(7)
    def get_Error(self) -> Windows.Devices.WiFiDirect.WiFiDirectError: ...
    Status = property(get_Status, None)
    Error = property(get_Error, None)
class IWiFiDirectConnectionListener(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('699c1b0d-8d13-4ee9-b9-ec-9c-72-f8-25-1f-7d')
    @winrt_commethod(6)
    def add_ConnectionRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.WiFiDirect.WiFiDirectConnectionListener, Windows.Devices.WiFiDirect.WiFiDirectConnectionRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ConnectionRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IWiFiDirectConnectionParameters(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('b2e55405-5702-4b16-a0-2c-bb-cd-21-ef-60-98')
    @winrt_commethod(6)
    def get_GroupOwnerIntent(self) -> Int16: ...
    @winrt_commethod(7)
    def put_GroupOwnerIntent(self, value: Int16) -> Void: ...
    GroupOwnerIntent = property(get_GroupOwnerIntent, put_GroupOwnerIntent)
class IWiFiDirectConnectionParameters2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('ab3b0fbe-aa82-44b4-88-c8-e3-05-6b-89-80-1d')
    @winrt_commethod(6)
    def get_PreferenceOrderedConfigurationMethods(self) -> Windows.Foundation.Collections.IVector[Windows.Devices.WiFiDirect.WiFiDirectConfigurationMethod]: ...
    @winrt_commethod(7)
    def get_PreferredPairingProcedure(self) -> Windows.Devices.WiFiDirect.WiFiDirectPairingProcedure: ...
    @winrt_commethod(8)
    def put_PreferredPairingProcedure(self, value: Windows.Devices.WiFiDirect.WiFiDirectPairingProcedure) -> Void: ...
    PreferenceOrderedConfigurationMethods = property(get_PreferenceOrderedConfigurationMethods, None)
    PreferredPairingProcedure = property(get_PreferredPairingProcedure, put_PreferredPairingProcedure)
class IWiFiDirectConnectionParametersStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('598af493-7642-456f-b9-d8-e8-a9-eb-1f-40-1a')
    @winrt_commethod(6)
    def GetDevicePairingKinds(self, configurationMethod: Windows.Devices.WiFiDirect.WiFiDirectConfigurationMethod) -> Windows.Devices.Enumeration.DevicePairingKinds: ...
class IWiFiDirectConnectionRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('8eb99605-914f-49c3-a6-14-d1-8d-c5-b1-9b-43')
    @winrt_commethod(6)
    def get_DeviceInformation(self) -> Windows.Devices.Enumeration.DeviceInformation: ...
    DeviceInformation = property(get_DeviceInformation, None)
class IWiFiDirectConnectionRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('f99d20be-d38d-484f-82-15-e7-b6-5a-bf-24-4c')
    @winrt_commethod(6)
    def GetConnectionRequest(self) -> Windows.Devices.WiFiDirect.WiFiDirectConnectionRequest: ...
class IWiFiDirectDevice(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('72deaaa8-72eb-4dae-8a-28-85-13-35-5d-27-77')
    @winrt_commethod(6)
    def get_ConnectionStatus(self) -> Windows.Devices.WiFiDirect.WiFiDirectConnectionStatus: ...
    @winrt_commethod(7)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def add_ConnectionStatusChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.WiFiDirect.WiFiDirectDevice, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_ConnectionStatusChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def GetConnectionEndpointPairs(self) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.EndpointPair]: ...
    ConnectionStatus = property(get_ConnectionStatus, None)
    DeviceId = property(get_DeviceId, None)
class IWiFiDirectDeviceStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('e86cb57c-3aac-4851-a7-92-48-2a-af-93-1b-04')
    @winrt_commethod(6)
    def GetDeviceSelector(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def FromIdAsync(self, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.WiFiDirect.WiFiDirectDevice]: ...
class IWiFiDirectDeviceStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('1a953e49-b103-437e-92-26-ab-67-97-13-42-f9')
    @winrt_commethod(6)
    def GetDeviceSelector(self, type: Windows.Devices.WiFiDirect.WiFiDirectDeviceSelectorType) -> WinRT_String: ...
    @winrt_commethod(7)
    def FromIdAsync(self, deviceId: WinRT_String, connectionParameters: Windows.Devices.WiFiDirect.WiFiDirectConnectionParameters) -> Windows.Foundation.IAsyncOperation[Windows.Devices.WiFiDirect.WiFiDirectDevice]: ...
class IWiFiDirectInformationElement(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('affb72d6-76bb-497e-ac-8b-dc-72-83-8b-c3-09')
    @winrt_commethod(6)
    def get_Oui(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(7)
    def put_Oui(self, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(8)
    def get_OuiType(self) -> Byte: ...
    @winrt_commethod(9)
    def put_OuiType(self, value: Byte) -> Void: ...
    @winrt_commethod(10)
    def get_Value(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(11)
    def put_Value(self, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    Oui = property(get_Oui, put_Oui)
    OuiType = property(get_OuiType, put_OuiType)
    Value = property(get_Value, put_Value)
class IWiFiDirectInformationElementStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('dbd02f16-11a5-4e60-8c-aa-34-77-21-48-37-8a')
    @winrt_commethod(6)
    def CreateFromBuffer(self, buffer: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.Collections.IVector[Windows.Devices.WiFiDirect.WiFiDirectInformationElement]: ...
    @winrt_commethod(7)
    def CreateFromDeviceInformation(self, deviceInformation: Windows.Devices.Enumeration.DeviceInformation) -> Windows.Foundation.Collections.IVector[Windows.Devices.WiFiDirect.WiFiDirectInformationElement]: ...
class IWiFiDirectLegacySettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('a64fdbba-f2fd-4567-a9-1b-f5-c2-f5-32-10-57')
    @winrt_commethod(6)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_Ssid(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Ssid(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_Passphrase(self) -> Windows.Security.Credentials.PasswordCredential: ...
    @winrt_commethod(11)
    def put_Passphrase(self, value: Windows.Security.Credentials.PasswordCredential) -> Void: ...
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    Ssid = property(get_Ssid, put_Ssid)
    Passphrase = property(get_Passphrase, put_Passphrase)
class WiFiDirectAdvertisement(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.WiFiDirect.WiFiDirectAdvertisement'
    @winrt_mixinmethod
    def get_InformationElements(self: Windows.Devices.WiFiDirect.IWiFiDirectAdvertisement) -> Windows.Foundation.Collections.IVector[Windows.Devices.WiFiDirect.WiFiDirectInformationElement]: ...
    @winrt_mixinmethod
    def put_InformationElements(self: Windows.Devices.WiFiDirect.IWiFiDirectAdvertisement, value: Windows.Foundation.Collections.IVector[Windows.Devices.WiFiDirect.WiFiDirectInformationElement]) -> Void: ...
    @winrt_mixinmethod
    def get_ListenStateDiscoverability(self: Windows.Devices.WiFiDirect.IWiFiDirectAdvertisement) -> Windows.Devices.WiFiDirect.WiFiDirectAdvertisementListenStateDiscoverability: ...
    @winrt_mixinmethod
    def put_ListenStateDiscoverability(self: Windows.Devices.WiFiDirect.IWiFiDirectAdvertisement, value: Windows.Devices.WiFiDirect.WiFiDirectAdvertisementListenStateDiscoverability) -> Void: ...
    @winrt_mixinmethod
    def get_IsAutonomousGroupOwnerEnabled(self: Windows.Devices.WiFiDirect.IWiFiDirectAdvertisement) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsAutonomousGroupOwnerEnabled(self: Windows.Devices.WiFiDirect.IWiFiDirectAdvertisement, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_LegacySettings(self: Windows.Devices.WiFiDirect.IWiFiDirectAdvertisement) -> Windows.Devices.WiFiDirect.WiFiDirectLegacySettings: ...
    @winrt_mixinmethod
    def get_SupportedConfigurationMethods(self: Windows.Devices.WiFiDirect.IWiFiDirectAdvertisement2) -> Windows.Foundation.Collections.IVector[Windows.Devices.WiFiDirect.WiFiDirectConfigurationMethod]: ...
    InformationElements = property(get_InformationElements, put_InformationElements)
    ListenStateDiscoverability = property(get_ListenStateDiscoverability, put_ListenStateDiscoverability)
    IsAutonomousGroupOwnerEnabled = property(get_IsAutonomousGroupOwnerEnabled, put_IsAutonomousGroupOwnerEnabled)
    LegacySettings = property(get_LegacySettings, None)
    SupportedConfigurationMethods = property(get_SupportedConfigurationMethods, None)
WiFiDirectAdvertisementListenStateDiscoverability = Int32
WiFiDirectAdvertisementListenStateDiscoverability_None: WiFiDirectAdvertisementListenStateDiscoverability = 0
WiFiDirectAdvertisementListenStateDiscoverability_Normal: WiFiDirectAdvertisementListenStateDiscoverability = 1
WiFiDirectAdvertisementListenStateDiscoverability_Intensive: WiFiDirectAdvertisementListenStateDiscoverability = 2
class WiFiDirectAdvertisementPublisher(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.WiFiDirect.WiFiDirectAdvertisementPublisher'
    @winrt_activatemethod
    def New(cls) -> Windows.Devices.WiFiDirect.WiFiDirectAdvertisementPublisher: ...
    @winrt_mixinmethod
    def get_Advertisement(self: Windows.Devices.WiFiDirect.IWiFiDirectAdvertisementPublisher) -> Windows.Devices.WiFiDirect.WiFiDirectAdvertisement: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.WiFiDirect.IWiFiDirectAdvertisementPublisher) -> Windows.Devices.WiFiDirect.WiFiDirectAdvertisementPublisherStatus: ...
    @winrt_mixinmethod
    def add_StatusChanged(self: Windows.Devices.WiFiDirect.IWiFiDirectAdvertisementPublisher, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.WiFiDirect.WiFiDirectAdvertisementPublisher, Windows.Devices.WiFiDirect.WiFiDirectAdvertisementPublisherStatusChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StatusChanged(self: Windows.Devices.WiFiDirect.IWiFiDirectAdvertisementPublisher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Start(self: Windows.Devices.WiFiDirect.IWiFiDirectAdvertisementPublisher) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: Windows.Devices.WiFiDirect.IWiFiDirectAdvertisementPublisher) -> Void: ...
    Advertisement = property(get_Advertisement, None)
    Status = property(get_Status, None)
WiFiDirectAdvertisementPublisherStatus = Int32
WiFiDirectAdvertisementPublisherStatus_Created: WiFiDirectAdvertisementPublisherStatus = 0
WiFiDirectAdvertisementPublisherStatus_Started: WiFiDirectAdvertisementPublisherStatus = 1
WiFiDirectAdvertisementPublisherStatus_Stopped: WiFiDirectAdvertisementPublisherStatus = 2
WiFiDirectAdvertisementPublisherStatus_Aborted: WiFiDirectAdvertisementPublisherStatus = 3
class WiFiDirectAdvertisementPublisherStatusChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.WiFiDirect.WiFiDirectAdvertisementPublisherStatusChangedEventArgs'
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.WiFiDirect.IWiFiDirectAdvertisementPublisherStatusChangedEventArgs) -> Windows.Devices.WiFiDirect.WiFiDirectAdvertisementPublisherStatus: ...
    @winrt_mixinmethod
    def get_Error(self: Windows.Devices.WiFiDirect.IWiFiDirectAdvertisementPublisherStatusChangedEventArgs) -> Windows.Devices.WiFiDirect.WiFiDirectError: ...
    Status = property(get_Status, None)
    Error = property(get_Error, None)
WiFiDirectConfigurationMethod = Int32
WiFiDirectConfigurationMethod_ProvidePin: WiFiDirectConfigurationMethod = 0
WiFiDirectConfigurationMethod_DisplayPin: WiFiDirectConfigurationMethod = 1
WiFiDirectConfigurationMethod_PushButton: WiFiDirectConfigurationMethod = 2
class WiFiDirectConnectionListener(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.WiFiDirect.WiFiDirectConnectionListener'
    @winrt_activatemethod
    def New(cls) -> Windows.Devices.WiFiDirect.WiFiDirectConnectionListener: ...
    @winrt_mixinmethod
    def add_ConnectionRequested(self: Windows.Devices.WiFiDirect.IWiFiDirectConnectionListener, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.WiFiDirect.WiFiDirectConnectionListener, Windows.Devices.WiFiDirect.WiFiDirectConnectionRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ConnectionRequested(self: Windows.Devices.WiFiDirect.IWiFiDirectConnectionListener, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class WiFiDirectConnectionParameters(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.WiFiDirect.WiFiDirectConnectionParameters'
    @winrt_activatemethod
    def New(cls) -> Windows.Devices.WiFiDirect.WiFiDirectConnectionParameters: ...
    @winrt_mixinmethod
    def get_GroupOwnerIntent(self: Windows.Devices.WiFiDirect.IWiFiDirectConnectionParameters) -> Int16: ...
    @winrt_mixinmethod
    def put_GroupOwnerIntent(self: Windows.Devices.WiFiDirect.IWiFiDirectConnectionParameters, value: Int16) -> Void: ...
    @winrt_mixinmethod
    def get_PreferenceOrderedConfigurationMethods(self: Windows.Devices.WiFiDirect.IWiFiDirectConnectionParameters2) -> Windows.Foundation.Collections.IVector[Windows.Devices.WiFiDirect.WiFiDirectConfigurationMethod]: ...
    @winrt_mixinmethod
    def get_PreferredPairingProcedure(self: Windows.Devices.WiFiDirect.IWiFiDirectConnectionParameters2) -> Windows.Devices.WiFiDirect.WiFiDirectPairingProcedure: ...
    @winrt_mixinmethod
    def put_PreferredPairingProcedure(self: Windows.Devices.WiFiDirect.IWiFiDirectConnectionParameters2, value: Windows.Devices.WiFiDirect.WiFiDirectPairingProcedure) -> Void: ...
    @winrt_classmethod
    def GetDevicePairingKinds(cls: Windows.Devices.WiFiDirect.IWiFiDirectConnectionParametersStatics, configurationMethod: Windows.Devices.WiFiDirect.WiFiDirectConfigurationMethod) -> Windows.Devices.Enumeration.DevicePairingKinds: ...
    GroupOwnerIntent = property(get_GroupOwnerIntent, put_GroupOwnerIntent)
    PreferenceOrderedConfigurationMethods = property(get_PreferenceOrderedConfigurationMethods, None)
    PreferredPairingProcedure = property(get_PreferredPairingProcedure, put_PreferredPairingProcedure)
class WiFiDirectConnectionRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.WiFiDirect.WiFiDirectConnectionRequest'
    @winrt_mixinmethod
    def get_DeviceInformation(self: Windows.Devices.WiFiDirect.IWiFiDirectConnectionRequest) -> Windows.Devices.Enumeration.DeviceInformation: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    DeviceInformation = property(get_DeviceInformation, None)
class WiFiDirectConnectionRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.WiFiDirect.WiFiDirectConnectionRequestedEventArgs'
    @winrt_mixinmethod
    def GetConnectionRequest(self: Windows.Devices.WiFiDirect.IWiFiDirectConnectionRequestedEventArgs) -> Windows.Devices.WiFiDirect.WiFiDirectConnectionRequest: ...
WiFiDirectConnectionStatus = Int32
WiFiDirectConnectionStatus_Disconnected: WiFiDirectConnectionStatus = 0
WiFiDirectConnectionStatus_Connected: WiFiDirectConnectionStatus = 1
class WiFiDirectDevice(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.WiFiDirect.WiFiDirectDevice'
    @winrt_mixinmethod
    def get_ConnectionStatus(self: Windows.Devices.WiFiDirect.IWiFiDirectDevice) -> Windows.Devices.WiFiDirect.WiFiDirectConnectionStatus: ...
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.WiFiDirect.IWiFiDirectDevice) -> WinRT_String: ...
    @winrt_mixinmethod
    def add_ConnectionStatusChanged(self: Windows.Devices.WiFiDirect.IWiFiDirectDevice, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.WiFiDirect.WiFiDirectDevice, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ConnectionStatusChanged(self: Windows.Devices.WiFiDirect.IWiFiDirectDevice, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetConnectionEndpointPairs(self: Windows.Devices.WiFiDirect.IWiFiDirectDevice) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.EndpointPair]: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Devices.WiFiDirect.IWiFiDirectDeviceStatics, type: Windows.Devices.WiFiDirect.WiFiDirectDeviceSelectorType) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.WiFiDirect.IWiFiDirectDeviceStatics, deviceId: WinRT_String, connectionParameters: Windows.Devices.WiFiDirect.WiFiDirectConnectionParameters) -> Windows.Foundation.IAsyncOperation[Windows.Devices.WiFiDirect.WiFiDirectDevice]: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Devices.WiFiDirect.IWiFiDirectDeviceStatics) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.WiFiDirect.IWiFiDirectDeviceStatics, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.WiFiDirect.WiFiDirectDevice]: ...
    ConnectionStatus = property(get_ConnectionStatus, None)
    DeviceId = property(get_DeviceId, None)
WiFiDirectDeviceSelectorType = Int32
WiFiDirectDeviceSelectorType_DeviceInterface: WiFiDirectDeviceSelectorType = 0
WiFiDirectDeviceSelectorType_AssociationEndpoint: WiFiDirectDeviceSelectorType = 1
WiFiDirectError = Int32
WiFiDirectError_Success: WiFiDirectError = 0
WiFiDirectError_RadioNotAvailable: WiFiDirectError = 1
WiFiDirectError_ResourceInUse: WiFiDirectError = 2
class WiFiDirectInformationElement(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.WiFiDirect.WiFiDirectInformationElement'
    @winrt_activatemethod
    def New(cls) -> Windows.Devices.WiFiDirect.WiFiDirectInformationElement: ...
    @winrt_mixinmethod
    def get_Oui(self: Windows.Devices.WiFiDirect.IWiFiDirectInformationElement) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def put_Oui(self: Windows.Devices.WiFiDirect.IWiFiDirectInformationElement, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def get_OuiType(self: Windows.Devices.WiFiDirect.IWiFiDirectInformationElement) -> Byte: ...
    @winrt_mixinmethod
    def put_OuiType(self: Windows.Devices.WiFiDirect.IWiFiDirectInformationElement, value: Byte) -> Void: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Devices.WiFiDirect.IWiFiDirectInformationElement) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def put_Value(self: Windows.Devices.WiFiDirect.IWiFiDirectInformationElement, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_classmethod
    def CreateFromBuffer(cls: Windows.Devices.WiFiDirect.IWiFiDirectInformationElementStatics, buffer: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.Collections.IVector[Windows.Devices.WiFiDirect.WiFiDirectInformationElement]: ...
    @winrt_classmethod
    def CreateFromDeviceInformation(cls: Windows.Devices.WiFiDirect.IWiFiDirectInformationElementStatics, deviceInformation: Windows.Devices.Enumeration.DeviceInformation) -> Windows.Foundation.Collections.IVector[Windows.Devices.WiFiDirect.WiFiDirectInformationElement]: ...
    Oui = property(get_Oui, put_Oui)
    OuiType = property(get_OuiType, put_OuiType)
    Value = property(get_Value, put_Value)
class WiFiDirectLegacySettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.WiFiDirect.WiFiDirectLegacySettings'
    @winrt_mixinmethod
    def get_IsEnabled(self: Windows.Devices.WiFiDirect.IWiFiDirectLegacySettings) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsEnabled(self: Windows.Devices.WiFiDirect.IWiFiDirectLegacySettings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Ssid(self: Windows.Devices.WiFiDirect.IWiFiDirectLegacySettings) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Ssid(self: Windows.Devices.WiFiDirect.IWiFiDirectLegacySettings, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Passphrase(self: Windows.Devices.WiFiDirect.IWiFiDirectLegacySettings) -> Windows.Security.Credentials.PasswordCredential: ...
    @winrt_mixinmethod
    def put_Passphrase(self: Windows.Devices.WiFiDirect.IWiFiDirectLegacySettings, value: Windows.Security.Credentials.PasswordCredential) -> Void: ...
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    Ssid = property(get_Ssid, put_Ssid)
    Passphrase = property(get_Passphrase, put_Passphrase)
WiFiDirectPairingProcedure = Int32
WiFiDirectPairingProcedure_GroupOwnerNegotiation: WiFiDirectPairingProcedure = 0
WiFiDirectPairingProcedure_Invitation: WiFiDirectPairingProcedure = 1
make_head(_module, 'IWiFiDirectAdvertisement')
make_head(_module, 'IWiFiDirectAdvertisement2')
make_head(_module, 'IWiFiDirectAdvertisementPublisher')
make_head(_module, 'IWiFiDirectAdvertisementPublisherStatusChangedEventArgs')
make_head(_module, 'IWiFiDirectConnectionListener')
make_head(_module, 'IWiFiDirectConnectionParameters')
make_head(_module, 'IWiFiDirectConnectionParameters2')
make_head(_module, 'IWiFiDirectConnectionParametersStatics')
make_head(_module, 'IWiFiDirectConnectionRequest')
make_head(_module, 'IWiFiDirectConnectionRequestedEventArgs')
make_head(_module, 'IWiFiDirectDevice')
make_head(_module, 'IWiFiDirectDeviceStatics')
make_head(_module, 'IWiFiDirectDeviceStatics2')
make_head(_module, 'IWiFiDirectInformationElement')
make_head(_module, 'IWiFiDirectInformationElementStatics')
make_head(_module, 'IWiFiDirectLegacySettings')
make_head(_module, 'WiFiDirectAdvertisement')
make_head(_module, 'WiFiDirectAdvertisementPublisher')
make_head(_module, 'WiFiDirectAdvertisementPublisherStatusChangedEventArgs')
make_head(_module, 'WiFiDirectConnectionListener')
make_head(_module, 'WiFiDirectConnectionParameters')
make_head(_module, 'WiFiDirectConnectionRequest')
make_head(_module, 'WiFiDirectConnectionRequestedEventArgs')
make_head(_module, 'WiFiDirectDevice')
make_head(_module, 'WiFiDirectInformationElement')
make_head(_module, 'WiFiDirectLegacySettings')
